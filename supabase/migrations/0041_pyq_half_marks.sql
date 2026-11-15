-- 0041: PYQ marks may be fractional.
--
-- Until 2016, GS I-III questions carried 12.5 marks each (20 questions,
-- 250 marks, 200 words). A smallint cannot hold that, so marks become
-- numeric(4,1). Every existing value is a whole number and keeps its value;
-- PostgREST still returns it as a JSON number.

alter table public.essay_pyqs
  alter column marks type numeric(4,1) using marks::numeric(4,1);
