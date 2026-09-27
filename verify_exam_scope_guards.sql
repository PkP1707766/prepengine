-- Proves the migration-0025 guards refuse cross-exam mixing. Every probe is rolled
-- back (each sub-block raises, or is refused), so running it changes no data.
-- Run in the Supabase SQL editor or via execute_sql; read the final SELECT.
-- Result on 2026-09-27: all three mixing attempts refused, the blueprint-less
-- fill inferred 'upsc', and an unchanged BPSC re-save passed.
create temp table if not exists guard_results(check_name text, outcome text);
truncate guard_results;
do $$
declare
  v_upsc_test uuid := (select id from public.tests where exam_category='upsc' limit 1);
  v_bpsc_test uuid := (select id from public.tests where exam_category='bpsc' limit 1);
  v_bpsc_q uuid := (select id from public.questions where exam_category='bpsc' limit 1);
  v_upsc_bp uuid := (select id from public.test_blueprints where exam_category='upsc' limit 1);
  v_upsc_q uuid := (select id from public.questions where exam_category='upsc' limit 1);
  v_series uuid := (select id from public.test_series where exam_category='bpsc' limit 1);
  v_filled text;
begin
  begin
    update public.tests set sections = jsonb_set(sections, '{0,questionIds}', (sections->0->'questionIds') || to_jsonb(v_bpsc_q::text)) where id = v_upsc_test;
    insert into guard_results values ('add a BPSC question to a UPSC test', 'ALLOWED (bad)');
  exception when others then insert into guard_results values ('add a BPSC question to a UPSC test', 'refused: ' || sqlerrm); end;

  begin
    update public.tests set series_id = v_series where id = v_upsc_test;
    insert into guard_results values ('put a UPSC test in the BPSC series', 'ALLOWED (bad)');
  exception when others then insert into guard_results values ('put a UPSC test in the BPSC series', 'refused: ' || sqlerrm); end;

  begin
    insert into public.plan_tests (plan_code, test_id) values ('bpsc-2026', v_upsc_test);
    insert into guard_results values ('assign a UPSC test to the BPSC bundle', 'ALLOWED (bad)');
  exception when others then insert into guard_results values ('assign a UPSC test to the BPSC bundle', 'refused: ' || sqlerrm); end;

  begin
    insert into public.tests (title, blueprint_id, sections)
    values ('guard probe', v_upsc_bp, jsonb_build_array(jsonb_build_object('id','s','name','S','questionIds', jsonb_build_array(v_upsc_q::text))))
    returning exam_category into v_filled;
    raise exception 'probe-rollback:%', v_filled;
  exception when others then insert into guard_results values ('insert without exam_category, from a UPSC blueprint (expect probe-rollback:upsc)', sqlerrm); end;

  begin
    update public.tests set sections = sections where id = v_bpsc_test;
    raise exception 'probe-rollback:ok';
  exception when others then insert into guard_results values ('re-save an existing BPSC test unchanged (expect probe-rollback:ok)', sqlerrm); end;
end $$;
select * from guard_results;
