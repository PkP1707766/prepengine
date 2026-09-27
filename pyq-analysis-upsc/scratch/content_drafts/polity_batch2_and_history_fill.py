# -*- coding: utf-8 -*-
"""History: 3 cells left short by the margin-preserving apportionment.
Polity: gap-report rows 1-2 (medium statement_based, Constitutional Framework x7, Parliament & State Legislature x7)."""
import json, os

def q(s):
    return "'" + s.replace("'", "''") + "'"

def opts(bodies, i):
    return json.dumps([{"id": "abcd"[k], "body": b, "isCorrect": k == i} for k, b in enumerate(bodies)])

C3 = ["Only one", "Only two", "All three", "None"]
C4 = ["Only one", "Only two", "Only three", "All four"]
T2 = ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"]
P4 = ["Only one pair", "Only two pairs", "Only three pairs", "All four pairs"]
HOW_MANY = "How many of the above statements are correct?"
WHICH = "Which of the statements given above is/are correct?"
PAIRS = "How many of the pairs given above are correctly matched?"
LAX = "M. Laxmikanth, Indian Polity"

def row(subject, topic, typ, diff, body, qdata, bodies, ans, expl, cg, cite):
    return ("('upsc'," + q(subject) + "," + q(topic) + "," + q(typ) + "," + q(diff) + "," + q(body) + "," + q(json.dumps(qdata)) + "::jsonb,"
            + q(opts(bodies, ans)) + "::jsonb,2,0.66," + q(expl) + "," + q(cg) + ",'original_pattern_matched'," + q(cite) + ",'draft')")

def stmt(topic, body, statements, ladder, ans, expl, cg, cite):
    closing = WHICH if ladder is T2 else HOW_MANY
    return row("Polity", topic, "statement_based", "medium", body,
               {"statements": statements, "closing": closing, "fixed_option_order": True}, ladder, ans, expl, cg, cite)

rows, tally = [], {}
def add(r, ladder, ans):
    rows.append(r); key = ("T2:" if ladder is T2 else f"{len(ladder)}-ladder:") + ladder[ans]; tally[key] = tally.get(key, 0) + 1

# ================= HISTORY fillers =================
rows.append(row("History", "Architecture", "match_the_following", "hard", "Consider the following pairs of temples and the dynasties under which they were built:",
  {"list_1": ["1. Brihadeshwara temple, Thanjavur", "2. Kailasa temple, Ellora", "3. Virupaksha temple, Pattadakal", "4. Sun temple, Modhera"],
   "list_2": ["Chola", "Pallava", "Chalukya of Badami", "Paramara"], "closing": PAIRS, "fixed_option_order": True},
  P4, 1,
  "Only pairs 1 and 3 are correct. The Brihadeshwara temple at Thanjavur was built by the Chola king Rajaraja I, and the Virupaksha temple at Pattadakal was built by Queen Lokamahadevi to commemorate the victory of her husband, the Chalukya king Vikramaditya II, over the Pallavas. Pair 2 is a name trap: the monolithic Kailasa temple at Ellora was built under the Rashtrakuta king Krishna I -- it is the Kailasanatha temple at Kanchipuram that is Pallava. Pair 4 is incorrect: the Modhera Sun temple was built under Bhima I of the Chaulukya (Solanki) dynasty, not the Paramaras.",
  "art-culture-temples-dynasties-pairs", "NCERT, An Introduction to Indian Art (Class XI) -- chapters on temple architecture."))

rows.append(row("History", "Iconography", "match_the_following", "hard", "Consider the following pairs of deities and the mounts (vahanas) associated with them in Hindu iconography:",
  {"list_1": ["1. Kartikeya", "2. Yamuna", "3. Agni", "4. Shiva"],
   "list_2": ["Peacock", "Makara", "Ram", "Nandi (bull)"], "closing": PAIRS, "fixed_option_order": True},
  P4, 2,
  "Pairs 1, 3 and 4 are correct: Kartikeya (Skanda) rides a peacock, Agni a ram, and Shiva the bull Nandi. Pair 2 is a swap between the two river goddesses: the makara (a crocodile-like creature) is the mount of Ganga, while Yamuna is shown standing on a tortoise (kurma) -- the pairing that appears on temple doorways from the Gupta period onward.",
  "art-culture-deity-vahana-pairs", "NCERT, An Introduction to Indian Art (Class XI) -- chapters on sculpture and iconography."))

rows.append(row("History", "Painting", "mcq", "easy", "Madhubani painting, which has received a Geographical Indication (GI) tag, is traditionally associated with which of the following States?",
  {}, ["Odisha", "Maharashtra", "West Bengal", "Bihar"], 3,
  "Madhubani (Mithila) painting belongs to the Mithila region of Bihar and received a GI tag. The other States are known for different traditions: Odisha for Pattachitra, Maharashtra for the Warli paintings of the Warli tribe, and West Bengal for Kalighat painting.",
  "art-culture-madhubani-painting", "NCERT, An Introduction to Indian Art (Class XI) -- chapter on folk and tribal art; Geographical Indications Registry."))

# ================= POLITY: Constitutional Framework x7 =================
CF = "Constitutional Framework"
add(stmt(CF, "Consider the following statements regarding the making of the Constitution of India:",
  ["The Constituent Assembly was constituted under the scheme formulated by the Cabinet Mission Plan of 1946.",
   "Dr. Rajendra Prasad was the Chairman of the Drafting Committee of the Constituent Assembly.",
   "The Constitution of India was adopted by the Constituent Assembly on 26 January 1950."], C3, 0,
  "Only statement 1 is correct: the Constituent Assembly was set up in 1946 under the Cabinet Mission Plan. Statement 2 swaps the office-holders: Dr. B. R. Ambedkar chaired the Drafting Committee, while Dr. Rajendra Prasad was the President of the Constituent Assembly. Statement 3 confuses two dates: the Constitution was adopted on 26 November 1949 and came into force on 26 January 1950.",
  "polity-making-of-constitution", f"{LAX} -- chapter on the Making of the Constitution."), C3, 0)

add(stmt(CF, "Consider the following statements regarding the procedure for amending the Constitution of India:",
  ["An amendment affecting any of the lists in the Seventh Schedule requires ratification by the legislatures of not less than one-half of the States, in addition to a special majority in Parliament.",
   "An amendment of the Fundamental Rights in Part III requires ratification by the legislatures of not less than one-half of the States.",
   "The President is bound to give assent to a Constitution Amendment Bill duly passed under Article 368, and cannot withhold assent or return it for reconsideration."], C3, 1,
  "Statements 1 and 3 are correct. Under the proviso to Art. 368(2), amendments to the Seventh Schedule lists (among other federal provisions) also need ratification by half the States. After the 24th Amendment (1971), the President must assent to a duly passed Constitution Amendment Bill. Statement 2 is incorrect: Fundamental Rights are amended by a special majority of Parliament alone -- they are not among the provisions listed in the proviso that require State ratification, a common assumption because of their importance.",
  "polity-amendment-ratification-art368", f"Constitution of India, Art. 368; {LAX} -- chapter on Amendment of the Constitution."), C3, 1)

add(stmt(CF, "Consider the following statements regarding the Schedules of the Constitution of India:",
  ["The Tenth Schedule contains the provisions for disqualification of members of Parliament and State Legislatures on the ground of defection.",
   "The Eighth Schedule originally listed 22 languages when the Constitution came into force."], T2, 0,
  "Only statement 1 is correct: the Tenth Schedule, added by the 52nd Amendment (1985), contains the anti-defection provisions. Statement 2 is incorrect: the Eighth Schedule originally listed 14 languages; it has grown to 22 through later amendments.",
  "polity-schedules-tenth-eighth", f"{LAX} -- chapter on the Schedules of the Constitution."), T2, 0)

add(stmt(CF, "Consider the following statements regarding citizenship in India:",
  ["The Constitution itself lays down the provisions for the acquisition and termination of citizenship after its commencement.",
   "Article 11 empowers Parliament to make any provision with respect to the acquisition and termination of citizenship.",
   "An Indian citizen who voluntarily acquires the citizenship of another country ceases to be a citizen of India."], C3, 1,
  "Statements 2 and 3 are correct: Art. 11 empowers Parliament to regulate citizenship, and under the Citizenship Act, 1955 voluntary acquisition of foreign citizenship terminates Indian citizenship. Statement 1 is incorrect: Part II of the Constitution (Arts. 5-11) deals only with who were citizens at its commencement; acquisition and loss of citizenship afterwards are governed by the Citizenship Act, 1955, enacted by Parliament.",
  "polity-citizenship-part-ii", f"Constitution of India, Arts. 5-11; Citizenship Act, 1955; {LAX} -- chapter on Citizenship."), C3, 1)

add(stmt(CF, "Consider the following statements regarding the Preamble to the Constitution of India:",
  ["The words 'Socialist', 'Secular' and 'Integrity' were added to the Preamble by the 42nd Amendment Act, 1976.",
   "The Preamble declares India to be a federal republic.",
   "In the Berubari Union case (1960), the Supreme Court held that the Preamble is a part of the Constitution."], C3, 0,
  "Only statement 1 is correct: the 42nd Amendment (1976) inserted 'Socialist', 'Secular' and 'Integrity'. Statement 2 is incorrect: the Preamble describes India as a Sovereign Socialist Secular Democratic Republic -- the word 'federal' appears nowhere in the Preamble or the Constitution. Statement 3 swaps the cases: in Berubari (1960) the Court held that the Preamble is NOT a part of the Constitution; it was in Kesavananda Bharati (1973) that the Court held it is a part.",
  "polity-preamble-amendment-cases", f"{LAX} -- chapter on the Preamble."), C3, 0)

add(stmt(CF, "Consider the following Parts of the Constitution of India and their subject matter:",
  ["Part XI deals with the relations between the Union and the States.",
   "Part XIV deals with services under the Union and the States.",
   "Part XV deals with elections."], C3, 2,
  "All three statements are correct: Part XI (Arts. 245-263) covers Union-State relations, Part XIV (Arts. 308-323) covers services under the Union and the States, including the Public Service Commissions, and Part XV (Arts. 324-329A) covers elections.",
  "polity-constitution-parts-xi-xiv-xv", f"Constitution of India; {LAX} -- chapter on the Parts of the Constitution."), C3, 2)

add(stmt(CF, "Consider the following statements regarding the sources from which features of the Constitution of India were borrowed:",
  ["The Directive Principles of State Policy were borrowed from the Irish Constitution.",
   "The procedure for amendment of the Constitution was borrowed from the Constitution of South Africa.",
   "The Fundamental Duties were borrowed from the Constitution of the USA.",
   "The suspension of Fundamental Rights during an Emergency was borrowed from the Weimar Constitution of Germany."], C4, 2,
  "Statements 1, 2 and 4 are correct: the Directive Principles came from the Irish Constitution, the amendment procedure (and the election of Rajya Sabha members) from South Africa, and the suspension of Fundamental Rights during an Emergency from the Weimar Constitution of Germany. Statement 3 is incorrect: the Fundamental Duties were drawn from the Constitution of the erstwhile USSR, not the USA.",
  "polity-borrowed-features-sources", f"{LAX} -- chapter on the Salient Features of the Constitution."), C4, 2)

# ================= POLITY: Parliament & State Legislature x7 =================
PL = "Parliament & State Legislature"
add(stmt(PL, "Consider the following statements regarding the Public Accounts Committee of Parliament:",
  ["The Public Accounts Committee consists of members of both the Lok Sabha and the Rajya Sabha.",
   "Its Chairman is appointed by the Speaker, and since 1967 the Chairman has by convention been chosen from the Opposition.",
   "It examines the audit reports of the Comptroller and Auditor General on the appropriation accounts and finance accounts of the Union Government."], C3, 2,
  "All three statements are correct. The Public Accounts Committee has 22 members, 15 from the Lok Sabha and 7 from the Rajya Sabha. Its Chairman is appointed by the Speaker, and by convention since 1967 is from the Opposition. It examines the CAG's audit reports on the appropriation and finance accounts of the Union Government.",
  "polity-public-accounts-committee", f"{LAX} -- chapter on Parliamentary Committees."), C3, 2)

add(stmt(PL, "Consider the following statements regarding the financial committees of Parliament:",
  ["The Committee on Public Undertakings consists of members of the Lok Sabha only.",
   "The Estimates Committee consists of members of both the Lok Sabha and the Rajya Sabha.",
   "The Business Advisory Committee of the Lok Sabha is chaired by the Leader of the House."], C3, 3,
  "None of the statements is correct. The Committee on Public Undertakings has members from both Houses (15 from the Lok Sabha and 7 from the Rajya Sabha). The Estimates Committee is the one drawn from the Lok Sabha alone -- all 30 of its members are from the Lok Sabha. The Business Advisory Committee of the Lok Sabha is chaired by the Speaker, not the Leader of the House.",
  "polity-financial-committees-composition", f"{LAX} -- chapter on Parliamentary Committees."), C3, 3)

add(stmt(PL, "Consider the following statements regarding the functioning of Parliament:",
  ["The quorum to constitute a meeting of either House of Parliament is one-tenth of the total number of members of that House.",
   "The Constitution provides that the interval between two sessions of Parliament shall not exceed six months.",
   "The secretariat of the Lok Sabha functions under the control of the Ministry of Parliamentary Affairs."], C3, 1,
  "Statements 1 and 2 are correct: under Art. 100(3) the quorum is one-tenth of the total membership of the House, and under Art. 85 the gap between two sessions cannot exceed six months. Statement 3 is incorrect: Art. 98 gives each House its own secretariat, and the Lok Sabha Secretariat works under the control of the Speaker, not any ministry -- which keeps it independent of the executive.",
  "polity-quorum-sessions-secretariat", f"Constitution of India, Arts. 85, 98 and 100; {LAX} -- chapter on Parliament."), C3, 1)

add(stmt(PL, "Consider the following statements regarding the Legislative Councils in the States:",
  ["Parliament may by law create or abolish the Legislative Council of a State if the Legislative Assembly of that State passes a resolution to that effect by a special majority.",
   "Such a law of Parliament is deemed to be an amendment of the Constitution for the purposes of Article 368.",
   "One-third of the members of a Legislative Council are nominated by the Governor."], C3, 0,
  "Only statement 1 is correct: under Art. 169 Parliament can create or abolish a Legislative Council on a resolution of the State Assembly passed by a special majority. Statement 2 reverses Art. 169(3): such a law is expressly NOT deemed an amendment of the Constitution for the purposes of Art. 368, so it needs only a simple majority. Statement 3 is incorrect: only one-sixth of the members are nominated by the Governor; one-third are elected by the members of the Legislative Assembly and one-third by local bodies.",
  "polity-legislative-council-art169", f"Constitution of India, Arts. 169 and 171; {LAX} -- chapter on the State Legislature."), C3, 0)

add(stmt(PL, "Consider the following statements regarding devices of parliamentary proceedings:",
  ["A short notice question can be asked with less than ten days' notice on a matter of public importance, and is answered orally.",
   "The calling attention motion is an Indian innovation in parliamentary procedure, but it is not mentioned in the Rules of Procedure.",
   "Zero Hour is not mentioned in the Rules of Procedure."], C3, 1,
  "Statements 1 and 3 are correct: a short notice question is asked with less than ten days' notice and answered orally, and Zero Hour (in use since 1962) is an informal device with no mention in the Rules of Procedure. Statement 2 is incorrect: the calling attention motion is an Indian innovation, in use since 1954, but unlike Zero Hour it is provided for in the Rules of Procedure.",
  "polity-parliamentary-devices-zero-hour", f"{LAX} -- chapter on Parliament (devices of parliamentary proceedings)."), C3, 1)

add(stmt(PL, "Consider the following statements regarding a joint sitting of the two Houses of Parliament:",
  ["A joint sitting of the two Houses is presided over by the Chairman of the Rajya Sabha.",
   "Since 1950, the provision for a joint sitting has been invoked more than five times."], T2, 3,
  "Neither statement is correct. Under Art. 118(4) a joint sitting is presided over by the Speaker of the Lok Sabha (in the Speaker's absence, the Deputy Speaker, and then the Deputy Chairman of the Rajya Sabha) -- not the Chairman of the Rajya Sabha. The provision has been invoked only three times: for the Dowry Prohibition Bill (1961), the Banking Service Commission (Repeal) Bill (1978) and the Prevention of Terrorism Bill (2002).",
  "polity-joint-sitting-art108", f"Constitution of India, Arts. 108 and 118; {LAX} -- chapter on Parliament."), T2, 3)

add(stmt(PL, "Consider the following statements regarding the presiding officers of the Lok Sabha:",
  ["The Speaker pro tem is appointed by the President.",
   "The office of the Leader of the Opposition in the Lok Sabha is provided for in the Constitution.",
   "The Deputy Speaker may resign from office by writing addressed to the Speaker.",
   "The decision of the Speaker on whether a Bill is a Money Bill is final."], C4, 2,
  "Statements 1, 3 and 4 are correct: the President appoints the Speaker pro tem; under Art. 94 the Deputy Speaker resigns by writing to the Speaker; and under Art. 110(3) the Speaker's decision on whether a Bill is a Money Bill is final. Statement 2 is incorrect: the Leader of the Opposition has statutory, not constitutional, recognition, under the Salary and Allowances of Leaders of Opposition in Parliament Act, 1977.",
  "polity-presiding-officers-lok-sabha", f"Constitution of India, Arts. 94 and 110; {LAX} -- chapter on Parliament."), C4, 2)

sql = ("insert into public.questions\n(exam_category, subject, topic, type, difficulty, body, question_data, options, marks_correct, marks_wrong, explanation, concept_group_id, source_type, source_citation, status)\nvalues\n"
       + ",\n".join(rows) + "\nreturning subject, topic, type, difficulty, concept_group_id;\n")
out = os.path.join(os.path.dirname(__file__), "polity_batch2_insert.sql")
open(out, "w", encoding="utf-8").write(sql)
print("rows:", len(rows), "| new Polity answer tally:", tally)
