-- 0035: long questions on the Mains tables.
--
-- A GS-IV case study runs to 300-450 words, and a topper's copy quotes it
-- whole. The unique keys on topper_answers and essay_pyqs indexed the full
-- normalised text (question_key, topic_key), and a b-tree entry cannot hold
-- more than about 2,700 bytes, so such a row could not be inserted at all.
--
-- The keys now index a hash of the same normalised text. Two questions are
-- still "the same" exactly when their normalised text is the same; only what
-- the index stores has changed. question_key and topic_key stay as columns
-- (the importer and the autolinker compare them), just no longer indexed.

alter table public.topper_answers
  add column if not exists question_hash text
    generated always as (md5(public.essay_key(question))) stored;

do $$ begin
  if exists (select 1 from pg_constraint where conname = 'topper_answers_uniq') then
    alter table public.topper_answers drop constraint topper_answers_uniq;
  end if;
  if not exists (select 1 from pg_constraint where conname = 'topper_answers_hash_uniq') then
    alter table public.topper_answers add constraint topper_answers_hash_uniq
      unique (copy_id, question_hash, page_key);
  end if;
end $$;
drop index if exists public.topper_answers_paper_key_idx;
create index if not exists topper_answers_paper_hash_idx on public.topper_answers (paper, question_hash);

alter table public.essay_pyqs
  add column if not exists topic_hash text
    generated always as (md5(public.essay_key(topic))) stored;

do $$ begin
  -- Both text keys go: the original (year, topic_key) and 0034's per-paper one.
  if exists (select 1 from pg_constraint where conname = 'essay_pyqs_year_topic_uniq') then
    alter table public.essay_pyqs drop constraint essay_pyqs_year_topic_uniq;
  end if;
  if exists (select 1 from pg_constraint where conname = 'essay_pyqs_paper_year_topic_uniq') then
    alter table public.essay_pyqs drop constraint essay_pyqs_paper_year_topic_uniq;
  end if;
  if not exists (select 1 from pg_constraint where conname = 'essay_pyqs_paper_year_hash_uniq') then
    alter table public.essay_pyqs add constraint essay_pyqs_paper_year_hash_uniq
      unique (paper, year, topic_hash);
  end if;
end $$;
drop index if exists public.essay_pyqs_key_idx;
create index if not exists essay_pyqs_hash_idx on public.essay_pyqs (topic_hash);
