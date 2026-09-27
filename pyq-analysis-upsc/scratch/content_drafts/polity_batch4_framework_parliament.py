# -*- coding: utf-8 -*-
"""Polity batch 4: every remaining Constitutional Framework cell (11) and Parliament & State
Legislature cell (12) from the live gap report (config e6f68e99, regenerated 2026-09-27)."""
import os
from polity_common import *

CF = "Constitutional Framework"
PL = "Parliament & State Legislature"

# ================= CONSTITUTIONAL FRAMEWORK =================
# ---------------- hard statement_based x4 ----------------
stmt(CF, "hard", "Consider the following statements regarding the Union and its territory:",
  ["A Bill for forming a new State or altering the boundaries of an existing State can be introduced in Parliament only on the recommendation of the President.",
   "Before recommending such a Bill, the President must refer it to the Legislature of the State concerned for expressing its views within a specified period, but Parliament is not bound by those views.",
   "A law made under Articles 2 and 3 is not deemed to be an amendment of the Constitution for the purposes of Article 368, even though it amends the First and Fourth Schedules.",
   "In the Berubari Union case (1960), the Supreme Court held that the cession of Indian territory to a foreign country requires an amendment of the Constitution under Article 368."],
  C4, 3,
  "All four statements are correct. The proviso to Art. 3 requires the President's recommendation and a reference to the State Legislature, whose views are not binding on Parliament. Art. 4(2) provides that laws under Arts. 2 and 3 are not amendments for the purposes of Art. 368, so they pass by simple majority. In the Berubari Union reference (1960), the Court held that Parliament's power under Art. 3 does not cover ceding Indian territory to a foreign State, which needs an Art. 368 amendment -- hence the 9th Amendment (1960).",
  "polity-union-territory-art3-berubari", f"Constitution of India, Arts. 2-4; In re Berubari Union (1960); {LAX} -- chapter on the Union and its Territory.")

stmt(CF, "hard", "Consider the following statements regarding the Citizenship (Amendment) Act, 2019:",
  ["It makes persons belonging to the Hindu, Sikh, Buddhist, Jain, Parsi and Christian communities from Afghanistan, Bangladesh and Pakistan eligible for citizenship.",
   "To be eligible under the Act, such persons must have entered India on or before 31 December 2016.",
   "It reduced the period of residence required for naturalisation of such persons from eleven years to seven years."],
  C3, 0,
  "Only statement 1 is correct: the Act covers these six communities from the three countries. Statement 2 changes the cut-off date: the Act applies to those who entered India on or before 31 December 2014. Statement 3 changes the number: the naturalisation residence requirement for them was reduced from eleven years to five years, not seven. The Citizenship (Amendment) Rules were notified in March 2024. The Act also does not apply to the Sixth Schedule tribal areas of Assam, Meghalaya, Mizoram and Tripura, or to areas under the Inner Line Permit.",
  "polity-caa-2019-cutoff-naturalisation", f"Citizenship (Amendment) Act, 2019; Citizenship (Amendment) Rules, 2024; {LAX} -- chapter on Citizenship.")

stmt(CF, "hard", "Consider the following statements regarding the Schedules of the Constitution of India:",
  ["The Ninth Schedule was added by the Constitution (First Amendment) Act, 1951.",
   "The Eleventh Schedule contains 29 subjects within the functional domain of Panchayats.",
   "The Twelfth Schedule contains 18 subjects within the functional domain of Municipalities.",
   "The Concurrent List of the Seventh Schedule originally contained 47 subjects."],
  C4, 3,
  "All four statements are correct. The First Amendment (1951) created the Ninth Schedule to protect land-reform laws; the 73rd and 74th Amendments (1992) added the Eleventh (29 Panchayat subjects) and Twelfth (18 Municipal subjects) Schedules; and the Concurrent List originally had 47 subjects (it now has 52, mainly because the 42nd Amendment moved subjects such as education and forests from the State List).",
  "polity-schedules-ninth-eleventh-twelfth", f"Constitution of India, Seventh, Ninth, Eleventh and Twelfth Schedules; {LAX} -- chapter on the Schedules of the Constitution.")

stmt(CF, "hard", "Consider the following statements regarding the official language provisions of the Constitution of India:",
  ["Article 343 declares Hindi in the Devanagari script to be the official language of the Union.",
   "The Constitution declares Hindi to be the national language of India.",
   "The Official Languages Act, 1963 permits the continued use of English, in addition to Hindi, for the official purposes of the Union without any time limit.",
   "Under Article 348, until Parliament by law provides otherwise, all proceedings in the Supreme Court and in every High Court shall be in English."],
  C4, 2,
  "Statements 1, 3 and 4 are correct. Art. 343(1) makes Hindi in Devanagari the official language of the Union; the Official Languages Act, 1963 (as amended in 1967) allows English to continue indefinitely alongside Hindi; and Art. 348(1) keeps English as the language of the Supreme Court and High Courts until Parliament provides otherwise. Statement 2 is incorrect: the Constitution does not declare any national language -- Part XVII speaks only of the official language.",
  "polity-official-language-part-xvii", f"Constitution of India, Arts. 343-351 (Part XVII); Official Languages Act, 1963; {LAX} -- chapter on Official Language.")

# ---------------- easy statement_based x1 ----------------
stmt(CF, "easy", "Consider the following statements regarding the Constitution of India:",
  ["It is the lengthiest written constitution of any sovereign country in the world.",
   "The original Constitution contained twelve Schedules."],
  T2, 0,
  "Only statement 1 is correct: the Constitution of India is the lengthiest written constitution of any sovereign country. Statement 2 is incorrect: the original Constitution had 395 Articles, 22 Parts and 8 Schedules; the number of Schedules has since grown to 12 through amendments.",
  "polity-constitution-length-schedules", f"{LAX} -- chapter on the Salient Features of the Constitution.")

# ---------------- mcq (medium 2, hard 1) ----------------
mcq(CF, "medium", "Which one of the following Schedules of the Constitution of India deals with the allocation of seats in the Council of States (Rajya Sabha)?",
  ["Second Schedule", "Fourth Schedule", "Sixth Schedule", "Eighth Schedule"], 1,
  "The Fourth Schedule allocates Rajya Sabha seats among the States and Union Territories. The Second Schedule covers the emoluments of constitutional functionaries, the Sixth the administration of tribal areas in Assam, Meghalaya, Tripura and Mizoram, and the Eighth the recognised languages.",
  "polity-fourth-schedule-rajya-sabha-seats", f"Constitution of India, Arts. 4(1) and 80(2), Fourth Schedule; {LAX} -- chapter on the Schedules of the Constitution.")

mcq(CF, "medium", "Which one of the following Constitution Amendment Acts is known as the 'mini-Constitution' because of the large number of changes it made?",
  ["24th Amendment Act", "44th Amendment Act", "73rd Amendment Act", "42nd Amendment Act"], 3,
  "The 42nd Amendment Act, 1976, enacted on the recommendations of the Swaran Singh Committee, is called the 'mini-Constitution': among much else it amended the Preamble, added the Fundamental Duties and moved five subjects to the Concurrent List. The 44th Amendment (1978) reversed several of its changes.",
  "polity-42nd-amendment-mini-constitution", f"{LAX} -- chapter on the Amendment of the Constitution (list of important amendments).")

mcq(CF, "hard", "Which one of the following committees of the Constituent Assembly was chaired by Jawaharlal Nehru?",
  ["Drafting Committee", "Union Powers Committee", "Provincial Constitution Committee", "Rules of Procedure Committee"], 1,
  "Jawaharlal Nehru chaired the Union Powers Committee (as well as the Union Constitution Committee and the States Committee). The Drafting Committee was chaired by Dr. B. R. Ambedkar, the Provincial Constitution Committee by Sardar Vallabhbhai Patel, and the Rules of Procedure Committee by Dr. Rajendra Prasad.",
  "polity-constituent-assembly-committees-chairs", f"{LAX} -- chapter on the Making of the Constitution.")

# ---------------- assertion_reason (hard 1, medium 1) ----------------
ar(CF, "hard",
  "The Preamble to the Constitution of India cannot be amended under Article 368.",
  "The Preamble is a part of the Constitution.",
  3,
  "Statement-I is incorrect: in Kesavananda Bharati (1973) the Supreme Court held that the Preamble can be amended under Art. 368, subject to the basic structure, and it has been amended once -- by the 42nd Amendment (1976), which added 'Socialist', 'Secular' and 'Integrity'. Statement-II is correct: the same case held that the Preamble is a part of the Constitution, overruling the view taken in the Berubari reference (1960).",
  "polity-preamble-amendability-kesavananda", f"Kesavananda Bharati v. State of Kerala (1973); {LAX} -- chapter on the Preamble.")

ar(CF, "medium",
  "The Constitution of India is described as a blend of rigidity and flexibility.",
  "Some provisions of the Constitution can be amended by a simple majority of Parliament, some need a special majority, and some also need ratification by half of the State Legislatures.",
  0,
  "Both statements are correct and Statement-II explains Statement-I. The Constitution is neither as rigid as the American nor as flexible as the British because it provides three modes of amendment: by simple majority (outside Art. 368, e.g. creating new States), by special majority under Art. 368, and by special majority plus ratification by half the States for federal provisions.",
  "polity-rigid-flexible-amendment-modes", f"Constitution of India, Art. 368; {LAX} -- chapters on the Salient Features and the Amendment of the Constitution.")

# ---------------- match medium x1 ----------------
pairs(CF, "medium", "Consider the following pairs of Constitution Amendment Acts and their subject matter:",
  ["61st Amendment Act", "86th Amendment Act", "91st Amendment Act", "73rd Amendment Act"],
  ["Reduction of the voting age from 21 to 18 years", "Anti-defection law (Tenth Schedule)", "Goods and Services Tax", "Municipalities"],
  0,
  "Only pair 1 is correct: the 61st Amendment (1988) lowered the voting age to 18. Pair 2 is incorrect: the anti-defection law was added by the 52nd Amendment (1985); the 86th Amendment (2002) made elementary education a Fundamental Right (Art. 21A). Pair 3 is incorrect: GST came with the 101st Amendment (2016); the 91st Amendment (2003) capped the size of Councils of Ministers and deleted the split exception from the Tenth Schedule. Pair 4 is incorrect: the 73rd Amendment deals with Panchayats; Municipalities came with the 74th.",
  "polity-amendment-acts-subject-pairs", f"{LAX} -- chapter on the Amendment of the Constitution (list of important amendments).")

# ================= PARLIAMENT & STATE LEGISLATURE =================
# ---------------- hard statement_based x4 ----------------
stmt(PL, "hard", "Consider the following statements regarding a State having a bicameral legislature:",
  ["The Legislative Council can detain an ordinary Bill passed by the Legislative Assembly for a maximum period of four months.",
   "There is no provision for a joint sitting of the two Houses of a State Legislature to resolve a deadlock.",
   "The Legislative Council can reject a Money Bill passed by the Legislative Assembly.",
   "An ordinary Bill that originates in the Legislative Council and is rejected by the Legislative Assembly comes to an end."],
  C4, 2,
  "Statements 1, 2 and 4 are correct. Under Art. 197 the Council can hold up an ordinary Bill for at most three months the first time and one month the second time, after which the Assembly's version is deemed passed; there is no joint sitting in a State Legislature; and a Council-originated Bill rejected by the Assembly dies. Statement 3 is incorrect: the Council cannot reject or amend a Money Bill -- it must return it within 14 days, and the Assembly may accept or reject its recommendations.",
  "polity-state-legislative-council-powers", f"Constitution of India, Arts. 197 and 198; {LAX} -- chapter on the State Legislature.")

stmt(PL, "hard", "Consider the following statements regarding cut motions in Parliament:",
  ["A 'policy cut' motion seeks to reduce the amount of a demand by Rs 100.",
   "An 'economy cut' motion seeks to reduce the amount of a demand by a specified amount.",
   "A 'token cut' motion seeks to reduce the amount of a demand to Re 1.",
   "Cut motions can be moved in both Houses of Parliament."],
  C4, 0,
  "Only statement 2 is correct: an economy cut proposes reducing the demand by a specified amount, representing the economy that can be effected. Statements 1 and 3 swap the other two: a disapproval of policy cut reduces the demand to Re 1, while a token cut reduces it by Rs 100 to ventilate a specific grievance. Statement 4 is incorrect: demands for grants are voted only in the Lok Sabha, so cut motions can be moved only there.",
  "polity-cut-motions-types", f"{LAX} -- chapter on Parliament (budget in Parliament).")

stmt(PL, "hard", "Consider the following statements regarding the Department-related Standing Committees (DRSCs) of Parliament:",
  ["There are 24 DRSCs, of which 16 function under the Lok Sabha and 8 under the Rajya Sabha.",
   "Each DRSC consists of 31 members: 21 from the Lok Sabha and 10 from the Rajya Sabha.",
   "The Chairperson of every DRSC is appointed by the Speaker of the Lok Sabha.",
   "The recommendations of the DRSCs on the demands for grants are binding on the Government."],
  C4, 1,
  "Statements 1 and 2 are correct: the system set up in 1993 was expanded in 2004 to 24 committees (16 serviced by the Lok Sabha and 8 by the Rajya Sabha), each with 31 members (21 + 10); ministers cannot be members. Statement 3 is incorrect: the Speaker appoints the Chairpersons of the 16 Lok Sabha committees, but the Chairpersons of the 8 Rajya Sabha committees are appointed by the Chairman of the Rajya Sabha. Statement 4 is incorrect: DRSC reports are advisory and do not bind the Government.",
  "polity-department-related-standing-committees", f"{LAX} -- chapter on Parliamentary Committees.")

stmt(PL, "hard", "Consider the following statements regarding parliamentary privileges:",
  ["Parliamentary privileges are available to the President, as he is an integral part of Parliament.",
   "Parliamentary privileges are also available to the Attorney General of India.",
   "Parliament has not yet enacted a law codifying all the privileges of its Houses and members.",
   "Members of Parliament enjoy freedom from arrest in criminal cases during the session of Parliament."],
  C4, 1,
  "Statements 2 and 3 are correct: privileges extend to persons entitled to speak in the Houses, including the Attorney General and Union ministers, and Parliament has not codified its privileges (Art. 105(3) continues them as they are). Statement 1 is incorrect: the President, though an integral part of Parliament, does not enjoy parliamentary privileges. Statement 4 is incorrect: freedom from arrest applies only in civil cases, during the session and 40 days before and after it -- not in criminal or preventive-detention cases.",
  "polity-parliamentary-privileges-scope", f"Constitution of India, Art. 105; {LAX} -- chapter on Parliament (parliamentary privileges).")

# ---------------- easy statement_based x1 ----------------
stmt(PL, "easy", "Consider the following statements regarding membership of Parliament:",
  ["The minimum age for membership of the Lok Sabha is 21 years.",
   "The minimum age for membership of the Rajya Sabha is 30 years."],
  T2, 1,
  "Only statement 2 is correct: under Art. 84 a person must be at least 30 years old to be chosen for the Rajya Sabha. Statement 1 is incorrect: the minimum age for the Lok Sabha is 25 years; 21 is not the qualifying age for either House.",
  "polity-mp-qualification-age", f"Constitution of India, Art. 84; {LAX} -- chapter on Parliament.")

# ---------------- mcq (medium 2, hard 1) ----------------
mcq(PL, "medium", "Who decides whether a Member of Parliament has become subject to a disqualification under Article 102(1), such as holding an office of profit?",
  ["The Speaker or Chairman of the House concerned", "The Supreme Court", "The President, acting according to the opinion of the Election Commission", "The Election Commission alone"], 2,
  "Under Art. 103, questions of disqualification under Art. 102(1) are decided by the President, whose decision is final, but the President must obtain and act according to the opinion of the Election Commission. By contrast, disqualification on the ground of defection (Art. 102(2), Tenth Schedule) is decided by the Speaker or Chairman.",
  "polity-art103-disqualification-president-ec", f"Constitution of India, Arts. 102 and 103; {LAX} -- chapter on Parliament.")

mcq(PL, "medium", "In the context of the budget in the Lok Sabha, the term 'guillotine' refers to",
  ["putting all the outstanding demands for grants to vote on the last day allotted, whether or not they have been discussed",
   "the Speaker's power to close the debate on a Bill at the end of Question Hour",
   "the suspension of a member for the remainder of the session",
   "the expunging of unparliamentary words from the record"], 0,
  "On the last of the days allotted for discussing the demands for grants, the Speaker puts all the remaining demands to vote at once, whether discussed or not -- the 'guillotine'. It ensures the budget is passed in time, though many demands are voted without discussion.",
  "polity-budget-guillotine", f"{LAX} -- chapter on Parliament (budget in Parliament).")

mcq(PL, "hard", "The present allocation of seats in the Lok Sabha among the States is based on the population figures of which Census?",
  ["2011", "2001", "1991", "1971"], 3,
  "The allocation of Lok Sabha seats among the States is frozen on the basis of the 1971 Census: the 42nd Amendment froze it until 2000, and the 84th Amendment (2001) extended the freeze until the first Census taken after 2026. The 87th Amendment (2003) allowed constituencies within each State to be redrawn on the basis of the 2001 Census without changing the number of seats per State -- the tempting wrong answer.",
  "polity-lok-sabha-seat-freeze-1971", f"Constitution of India, Arts. 81 and 82; {LAX} -- chapter on Parliament (composition of the Lok Sabha).")

# ---------------- assertion_reason (medium 1, hard 1) ----------------
ar(PL, "medium",
  "A member of the Lok Sabha elected as Speaker is required by the Constitution to resign from his or her political party.",
  "The Speaker does not vote in the first instance, but exercises a casting vote in the case of an equality of votes.",
  3,
  "Statement-I is incorrect: no constitutional provision requires the Speaker to resign party membership; the British convention of a non-party Speaker has not been adopted in India. Statement-II is correct: under Art. 100(1) the Speaker does not vote in the first instance but has a casting vote in the event of a tie.",
  "polity-speaker-party-casting-vote", f"Constitution of India, Arts. 93-96 and 100; {LAX} -- chapter on Parliament (Speaker of the Lok Sabha).")

ar(PL, "hard",
  "The term of the Lok Sabha can be extended beyond five years while a Proclamation of National Emergency is in operation.",
  "While a Proclamation of National Emergency is in operation, the term of a State Legislative Assembly can also be extended by a law of Parliament.",
  1,
  "Both statements are correct, but Statement-II does not explain Statement-I. Under the proviso to Art. 83(2), Parliament can by law extend the Lok Sabha's term one year at a time during a National Emergency (and not beyond six months after it ceases). The proviso to Art. 172(1) separately allows Parliament to extend a State Assembly's term in the same way. They are parallel provisions for two different Houses; one is not the reason for the other.",
  "polity-house-term-extension-emergency", f"Constitution of India, Arts. 83(2) and 172(1); {LAX} -- chapters on Parliament and Emergency Provisions.")

# ---------------- match (hard 1, medium 1) ----------------
pairs(PL, "hard", "Consider the following pairs of parliamentary motions and their features:",
  ["Adjournment motion", "Censure motion", "No-confidence motion", "Motion of Thanks"],
  ["Can be introduced only in the Lok Sabha", "Can be moved only against the entire Council of Ministers", "Must state the reasons for its adoption", "Its defeat in the Lok Sabha amounts to the defeat of the Government"],
  1,
  "Only pairs 1 and 4 are correct: the Rajya Sabha is not permitted to use the adjournment motion, and defeat of the Motion of Thanks on the President's address means the Government has lost the House's confidence. Pair 2 is incorrect: a censure motion can be moved against an individual minister, a group of ministers or the entire Council of Ministers. Pair 3 swaps the two motions: it is the censure motion that must state the reasons for its adoption; a no-confidence motion need not.",
  "polity-parliamentary-motions-features-pairs", f"{LAX} -- chapter on Parliament (devices of parliamentary proceedings).")

pairs(PL, "medium", "Consider the following pairs of Articles of the Constitution and their subject matter:",
  ["Article 105", "Article 110", "Article 112", "Article 123"],
  ["Powers and privileges of the Houses of Parliament and their members", "Definition of Money Bills", "Annual Financial Statement", "Ordinance-making power of the Governor"],
  2,
  "Pairs 1, 2 and 3 are correct: Art. 105 deals with parliamentary privileges, Art. 110 defines Money Bills, and Art. 112 requires the Annual Financial Statement (the budget) to be laid before Parliament. Pair 4 is incorrect: Art. 123 is the President's ordinance-making power; the Governor's corresponding power is in Art. 213.",
  "polity-parliament-articles-pairs", f"Constitution of India, Arts. 105, 110, 112, 123 and 213; {LAX} -- chapter on Parliament.")

write_sql(os.path.dirname(os.path.abspath(__file__)), "polity_batch4_insert.sql")
