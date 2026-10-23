-- The exam screen labels Statement-I/II rows itself (ex_statement_1/2), so the
-- "Statement-I: " / "कथन-I: " written into the text of the Level 3 Tests 1-3
-- drafts rendered twice ("Statement-I: Statement-I: ..."). Strip the prefix from
-- the 27 affected drafts; published rows never carried it.
update questions
set question_data = question_data
  || jsonb_build_object(
       'assertion',    regexp_replace(question_data->>'assertion',    '^\s*Statement-I:\s*', ''),
       'reason',       regexp_replace(question_data->>'reason',       '^\s*Statement-II:\s*', ''),
       'assertion_hi', regexp_replace(question_data->>'assertion_hi', '^\s*कथन-I:\s*', ''),
       'reason_hi',    regexp_replace(question_data->>'reason_hi',    '^\s*कथन-II:\s*', ''))
where type = 'assertion_reason'
  and status = 'draft'
  and concept_group_id ~ '^l3-t[123]-'
  and (question_data->>'assertion' ~ '^\s*Statement-I:' or question_data->>'reason' ~ '^\s*Statement-II:'
       or question_data->>'assertion_hi' ~ '^\s*कथन-I:' or question_data->>'reason_hi' ~ '^\s*कथन-II:')
returning concept_group_id;
