# -*- coding: utf-8 -*-
"""Polity checkpoint: the first 5 gap-report priority rows (one question each)."""
import json, os

def q(s):
    return "'" + s.replace("'", "''") + "'"

def opts(bodies, i):
    return json.dumps([{"id": "abcd"[k], "body": b, "isCorrect": k == i} for k, b in enumerate(bodies)])

COUNT3 = ["Only one", "Only two", "All three", "None"]
COUNT4 = ["Only one", "Only two", "Only three", "All four"]
T2 = ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"]
AR = ["Both A and R are true and R is the correct explanation of A",
      "Both A and R are true but R is NOT the correct explanation of A",
      "A is true but R is false",
      "A is false but R is true"]

def row(typ, diff, body, qdata, option_bodies, ans, expl, cg, cite):
    return ("('upsc','Polity','Governance'," + q(typ) + "," + q(diff) + "," + q(body) + "," + q(json.dumps(qdata)) + "::jsonb,"
            + q(opts(option_bodies, ans)) + "::jsonb,2,0.66," + q(expl) + "," + q(cg) + ",'original_pattern_matched'," + q(cite) + ",'draft')")

rows = []

# 1. medium / statement_based / Governance -- 3 statements, article-body swap + reversed absolute (2 false -> Only one)
rows.append(row("statement_based", "medium", "Consider the following statements regarding the Comptroller and Auditor General of India (CAG):",
  {"statements": [
     "The CAG is appointed by the President and can be removed only in the manner and on the grounds prescribed for the removal of a Judge of the Supreme Court.",
     "The CAG submits his audit reports relating to the accounts of the Union to the Speaker of the Lok Sabha, who causes them to be laid before the House.",
     "The CAG is eligible for further office under the Government of India after he has ceased to hold his office."],
   "closing": "How many of the above statements are correct?"},
  COUNT3, 0,
  "Only statement 1 is correct: under Art. 148 the CAG is appointed by the President and is removable only in the manner and on the grounds applicable to a Supreme Court judge. Statement 2 is an article-body swap: under Art. 151 the CAG's audit reports on the Union's accounts are submitted to the President, who causes them to be laid before each House of Parliament -- not to the Speaker. Statement 3 reverses Art. 148(4): the CAG is not eligible for any further office under the Government of India or of any State after ceasing to hold office, which protects his independence.",
  "polity-cag-independence-reports",
  "Constitution of India, Arts. 148-151; M. Laxmikanth, Indian Polity -- chapter on the Comptroller and Auditor General of India."))

# 2. easy / statement_based / Governance -- T2, 2 statements, body swap (ECI vs State Election Commission)
rows.append(row("statement_based", "easy", "Consider the following statements regarding the Election Commission of India:",
  {"statements": [
     "The Election Commission of India is a constitutional body.",
     "The Election Commission of India conducts elections to the Panchayats and Municipalities in the States."],
   "closing": "Which of the statements given above is/are correct?"},
  T2, 0,
  "Only statement 1 is correct: the Election Commission is a constitutional body under Art. 324. Statement 2 is incorrect: the Election Commission superintends elections to Parliament, the State Legislatures and the offices of the President and Vice-President, but elections to Panchayats and Municipalities are conducted by the State Election Commissions (Arts. 243K and 243ZA).",
  "polity-election-commission-vs-state-ec",
  "Constitution of India, Arts. 324, 243K and 243ZA; M. Laxmikanth, Indian Polity -- chapters on the Election Commission, Panchayati Raj and Municipalities."))

# 3. hard / statement_based / Governance -- 4 statements, 3 false (number swap, binding/advisory, constitutional/statutory) -> Only one
rows.append(row("statement_based", "hard", "Consider the following statements regarding the Finance Commission of India:",
  {"statements": [
     "The Finance Commission is constituted by the President every fourth year, or earlier if he considers it necessary.",
     "The recommendations of the Finance Commission are binding on the Union Government.",
     "The Finance Commission is a statutory body established under the Finance Commission (Miscellaneous Provisions) Act, 1951.",
     "The Finance Commission recommends measures needed to augment the Consolidated Fund of a State to supplement the resources of the Panchayats and Municipalities in the State, on the basis of the recommendations of the State Finance Commission."],
   "closing": "How many of the above statements are correct?"},
  COUNT4, 0,
  "Only statement 4 is correct: under Art. 280(3), as amended by the 73rd and 74th Amendments, the Finance Commission recommends measures to augment a State's Consolidated Fund to supplement the resources of Panchayats and Municipalities, on the basis of the State Finance Commission's recommendations. Statement 1 changes the interval: the Commission is constituted at the expiration of every fifth year, not fourth. Statement 2 is incorrect: its recommendations are advisory and not binding on the Union Government. Statement 3 is incorrect: the Finance Commission is a constitutional body under Art. 280; the 1951 Act only lays down its qualifications and procedure.",
  "polity-finance-commission-art280",
  "Constitution of India, Art. 280; Finance Commission (Miscellaneous Provisions) Act, 1951; M. Laxmikanth, Indian Polity -- chapter on the Finance Commission."))

# 4. medium / mcq / Governance -- negative framing, statutory-vs-non-statutory (CVC is the tempting wrong pick)
rows.append(row("mcq", "medium", "Which one of the following bodies is neither a constitutional body nor a statutory body?",
  {},
  ["Central Vigilance Commission", "Competition Commission of India", "NITI Aayog", "National Human Rights Commission"], 2,
  "NITI Aayog was set up in 2015 by a Union Cabinet resolution, replacing the Planning Commission, and has neither a constitutional nor a statutory basis. The other three are statutory: the National Human Rights Commission under the Protection of Human Rights Act, 1993; the Competition Commission of India under the Competition Act, 2002; and the Central Vigilance Commission, which began in 1964 by executive resolution but has been statutory since the Central Vigilance Commission Act, 2003 -- the tempting wrong pick for anyone using older notes.",
  "polity-constitutional-statutory-nonstatutory-bodies",
  "M. Laxmikanth, Indian Polity -- chapters on Constitutional Bodies, Non-Constitutional Bodies and NITI Aayog; Protection of Human Rights Act, 1993; Competition Act, 2002; CVC Act, 2003."))

# 5. medium / assertion_reason / Governance -- both true, R does not explain A -> (b)
rows.append(row("assertion_reason", "medium", "Consider the following Assertion (A) and Reason (R) regarding the Houses of Parliament:",
  {"assertion": "The Rajya Sabha is not subject to dissolution, whereas the Lok Sabha can be dissolved before the expiry of its term.",
   "reason": "Members of the Rajya Sabha are elected by the elected members of the State Legislative Assemblies through proportional representation by means of the single transferable vote."},
  AR, 1,
  "Both A and R are true, but R does not explain A. A is true: under Art. 83 the Council of States is not subject to dissolution, while the House of the People continues for five years unless sooner dissolved. R is true: under Art. 80(4), Rajya Sabha members are elected by the elected members of the State Legislative Assemblies by proportional representation with the single transferable vote. But the Rajya Sabha escapes dissolution because it is a permanent House, with one-third of its members retiring every second year (Art. 83(1)) -- not because of the manner of their election.",
  "polity-rajya-sabha-dissolution-election",
  "Constitution of India, Arts. 80 and 83; M. Laxmikanth, Indian Polity -- chapter on Parliament."))

sql = ("insert into public.questions\n(exam_category, subject, topic, type, difficulty, body, question_data, options, marks_correct, marks_wrong, explanation, concept_group_id, source_type, source_citation, status)\nvalues\n"
       + ",\n".join(rows) + "\nreturning id, type, difficulty;\n")
out = os.path.join(os.path.dirname(__file__), "polity_batch1_insert.sql")
open(out, "w", encoding="utf-8").write(sql)
print("wrote", out, len(sql), "chars,", len(rows), "rows")
