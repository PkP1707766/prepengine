-- One-off (2026-10-06): the SQL builders wrote their files in Windows text mode, so every line break inside a
-- quoted multi-line body reached the database as CRLF. The builders now write LF (newline="\n"), and
-- .gitattributes keeps this folder's SQL LF on checkout. This turns the stored CRLFs back into LF for UPSC rows
-- only; nothing visible changes (the exam and review screens render with white-space: pre-wrap).
update public.questions
set body = replace(body, chr(13) || chr(10), chr(10)),
    body_hi = replace(body_hi, chr(13) || chr(10), chr(10)),
    explanation = replace(explanation, chr(13) || chr(10), chr(10)),
    explanation_hi = replace(explanation_hi, chr(13) || chr(10), chr(10))
where exam_category = 'upsc'
  and position(chr(13) in coalesce(body, '') || coalesce(body_hi, '') || coalesce(explanation, '') || coalesce(explanation_hi, '')) > 0
returning concept_group_id, status;
