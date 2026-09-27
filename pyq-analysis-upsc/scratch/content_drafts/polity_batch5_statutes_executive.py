# -*- coding: utf-8 -*-
"""Polity batch 5: every remaining Statutory-Laws cell (12) and Union & State Executive cell (10)
from the live gap report (config e6f68e99, regenerated 2026-09-27). Post-2023 facts were
cross-checked by web search on 2026-09-27 (criminal laws, Public Examinations Act, Bharatiya
Vayuyan Adhiniyam, Immigration and Foreigners Act, Telecommunications Act, DPDP penalties,
the November 2025 Presidential Reference opinion, the September 2025 Vice-Presidential election)."""
import os
from polity_common import *

SL = "Statutory-Laws"
EX = "Union & State Executive"

# ================= STATUTORY-LAWS =================
# ---------------- medium statement_based x4 ----------------
stmt(SL, "medium", "Consider the following statements regarding India's new criminal laws:",
  ["The Bharatiya Nyaya Sanhita, 2023 replaced the Indian Penal Code, 1860.",
   "The Bharatiya Sakshya Adhiniyam, 2023 replaced the Code of Criminal Procedure, 1973.",
   "The three new criminal laws came into force on 1 January 2024."],
  C3, 0,
  "Only statement 1 is correct. Statement 2 swaps the laws: the Bharatiya Sakshya Adhiniyam replaced the Indian Evidence Act, 1872, while the Code of Criminal Procedure was replaced by the Bharatiya Nagarik Suraksha Sanhita, 2023. Statement 3 is incorrect: the three laws were enacted in December 2023 but came into force on 1 July 2024.",
  "statute-new-criminal-laws-replacements", "Bharatiya Nyaya Sanhita, 2023; Bharatiya Nagarik Suraksha Sanhita, 2023; Bharatiya Sakshya Adhiniyam, 2023; Ministry of Home Affairs notifications (commencement 1 July 2024).")

stmt(SL, "medium", "With reference to the Digital Personal Data Protection Act, 2023, consider the following statements:",
  ["It provides for the establishment of the Data Protection Board of India.",
   "It applies to personal data collected in digital form, and to personal data collected in non-digital form that is digitised subsequently.",
   "It applies to the processing of personal data outside India even when the processing is not connected with offering goods or services to Data Principals in India."],
  C3, 1,
  "Statements 1 and 2 are correct: the Act sets up the Data Protection Board of India to adjudicate breaches, and under Section 3 it covers digital personal data, including data collected offline and later digitised. Statement 3 is incorrect: processing outside India is covered only if it is connected with offering goods or services to Data Principals within India. The DPDP Rules notified in November 2025 phase in most obligations over 18 months.",
  "statute-dpdp-act-2023-scope", "Digital Personal Data Protection Act, 2023 (Sections 3 and 18); Digital Personal Data Protection Rules, 2025.")

stmt(SL, "medium", "Consider the following statements regarding the Right to Information Act, 2005:",
  ["Information concerning the life or liberty of a person must be provided within 48 hours of the receipt of the request.",
   "The RTI (Amendment) Act, 2019 empowered the Central Government to prescribe the term of office and the salaries of the Chief Information Commissioner and the Information Commissioners."],
  T2, 2,
  "Both statements are correct. The proviso to Section 7(1) requires information concerning the life or liberty of a person to be supplied within 48 hours (the general limit is 30 days). The 2019 amendment removed the fixed five-year term and the salary parity with the Election Commission, leaving both to be prescribed by the Central Government by rules.",
  "statute-rti-48-hours-2019-amendment", "Right to Information Act, 2005 (Sections 7, 13 and 16); Right to Information (Amendment) Act, 2019.")

stmt(SL, "medium", "Consider the following statements regarding the Public Examinations (Prevention of Unfair Means) Act, 2024:",
  ["Offences under the Act are bailable and can be compounded with the consent of the examination authority.",
   "It covers public examinations conducted by bodies such as the Union Public Service Commission, the Staff Selection Commission and the National Testing Agency.",
   "It applies directly to the recruitment examinations conducted by the State Public Service Commissions."],
  C3, 0,
  "Only statement 2 is correct: the Act applies to the public examination authorities listed in its Schedule, including UPSC, SSC, the Railway Recruitment Boards, IBPS and NTA, as well as central ministries and departments. Statement 1 is incorrect: every offence under the Act is cognizable, non-bailable and non-compoundable. Statement 3 is incorrect: the Act applies to central examinations; State examinations are outside it unless a State adopts it or enacts its own law.",
  "statute-public-examinations-act-2024", "Public Examinations (Prevention of Unfair Means) Act, 2024 (Sections 2, 9 and the Schedule).")

# ---------------- hard statement_based x2 ----------------
stmt(SL, "hard", "Consider the following statements regarding the Bharatiya Nyaya Sanhita (BNS) and the Bharatiya Nagarik Suraksha Sanhita (BNSS), 2023:",
  ["The BNS introduces community service as a form of punishment for certain petty offences.",
   "The BNS retains the offence of sedition under the same name, with the same wording as Section 124A of the Indian Penal Code.",
   "Under the BNSS, a forensic expert must visit the crime scene in offences punishable with imprisonment of seven years or more.",
   "The BNSS provides for the trial of proclaimed offenders in their absence in certain circumstances."],
  C4, 2,
  "Statements 1, 3 and 4 are correct: community service is a new punishment under the BNS for petty offences; Section 176(3) of the BNSS makes forensic investigation at the scene mandatory for offences punishable with seven years or more; and Section 356 of the BNSS allows trial in absentia of proclaimed offenders who abscond to evade trial. Statement 2 is incorrect: the BNS drops the offence named 'sedition'; Section 152 instead punishes acts endangering the sovereignty, unity and integrity of India, with different wording.",
  "statute-bns-bnss-new-features", "Bharatiya Nyaya Sanhita, 2023 (Sections 4 and 152); Bharatiya Nagarik Suraksha Sanhita, 2023 (Sections 176 and 356).")

stmt(SL, "hard", "Consider the following statements regarding the Telecommunications Act, 2023:",
  ["It repealed the Indian Telegraph Act, 1885 and the Indian Wireless Telegraphy Act, 1933.",
   "It allows spectrum for the services listed in its First Schedule, including certain satellite-based services, to be assigned through an administrative process instead of an auction.",
   "It dissolved the Telecom Regulatory Authority of India and transferred its functions to the Department of Telecommunications."],
  C3, 1,
  "Statements 1 and 2 are correct: the Act replaced the colonial-era telegraph and wireless laws, and while spectrum is ordinarily assigned by auction, Section 4 and the First Schedule allow administrative assignment for listed uses such as satellite-based services. Statement 3 is incorrect: TRAI continues to exist under the TRAI Act, 1997; the Telecommunications Act only amended certain provisions of that Act.",
  "statute-telecommunications-act-2023", "Telecommunications Act, 2023 (Section 4 and the First Schedule); Telecom Regulatory Authority of India Act, 1997.")

# ---------------- mcq (hard 1, medium 1) ----------------
mcq(SL, "hard", "Under the Digital Personal Data Protection Act, 2023, what is the maximum penalty that may be imposed for failure to take reasonable security safeguards to prevent a personal data breach?",
  ["Rs 250 crore", "Rs 200 crore", "Rs 150 crore", "Rs 50 crore"], 0,
  "The Schedule to the Act sets the highest penalty, up to Rs 250 crore, for failing to take reasonable security safeguards to prevent a personal data breach. Up to Rs 200 crore applies to failing to notify a breach and to breaching obligations relating to children's data, up to Rs 150 crore to breaching the additional obligations of Significant Data Fiduciaries, and up to Rs 50 crore is the residual category.",
  "statute-dpdp-penalty-schedule", "Digital Personal Data Protection Act, 2023 (Section 33 and the Schedule).")

mcq(SL, "medium", "Under the Juvenile Justice (Care and Protection of Children) Act, 2015, a child in the age group of 16 to 18 years may be tried as an adult, after a preliminary assessment, for which category of offences?",
  ["Any offence", "Heinous offences", "Petty offences", "Serious offences"], 1,
  "The 2015 Act allows a child aged 16 to 18 who is alleged to have committed a heinous offence -- one punishable with a minimum of seven years' imprisonment -- to be tried as an adult after a preliminary assessment by the Juvenile Justice Board of the child's mental and physical capacity. Petty and serious offences remain within the juvenile system.",
  "statute-juvenile-justice-heinous-offences", "Juvenile Justice (Care and Protection of Children) Act, 2015 (Sections 2 and 15).")

# ---------------- assertion_reason (hard 1, medium 1) ----------------
ar(SL, "hard",
  "The Right to Information Act, 2005 does not apply to the intelligence and security organisations specified in its Second Schedule, except for information pertaining to allegations of corruption and human rights violations.",
  "The provisions of the Right to Information Act, 2005 have effect notwithstanding anything inconsistent with them in the Official Secrets Act, 1923.",
  1,
  "Both statements are correct, but Statement-II does not explain Statement-I. Section 24 exempts the organisations in the Second Schedule, with the corruption and human-rights exception. Section 22 separately gives the RTI Act overriding effect over the Official Secrets Act and other inconsistent laws. The exemption in Statement-I exists because of Section 24, not because of the overriding clause -- if anything, the overriding clause cuts the other way.",
  "statute-rti-section-24-22", "Right to Information Act, 2005 (Sections 22 and 24, Second Schedule).")

ar(SL, "medium",
  "The Protection of Children from Sexual Offences (POCSO) Act, 2012 is a gender-neutral law.",
  "Under the POCSO Act, a 'child' means any person below the age of sixteen years.",
  2,
  "Statement-I is correct: the POCSO Act protects all children from sexual offences irrespective of gender. Statement-II is incorrect: Section 2(1)(d) defines a child as any person below the age of eighteen years.",
  "statute-pocso-gender-neutral-age", "Protection of Children from Sexual Offences Act, 2012 (Section 2).")

# ---------------- match (hard 1, medium 1) ----------------
pairs(SL, "hard", "Consider the following pairs of recent laws and the older laws they replaced or repealed:",
  ["Bharatiya Vayuyan Adhiniyam, 2024", "Immigration and Foreigners Act, 2025", "Bharatiya Sakshya Adhiniyam, 2023", "Telecommunications Act, 2023"],
  ["Aircraft Act, 1934", "Foreigners Act, 1946", "Code of Criminal Procedure, 1973", "Cable Television Networks (Regulation) Act, 1995"],
  1,
  "Only pairs 1 and 2 are correct. The Bharatiya Vayuyan Adhiniyam, 2024 (in force from 1 January 2025) repealed the Aircraft Act, 1934, and the Immigration and Foreigners Act, 2025 (in force from 1 September 2025) repealed the Foreigners Act, 1946 along with three other laws. Pair 3 is incorrect: the Bharatiya Sakshya Adhiniyam replaced the Indian Evidence Act, 1872. Pair 4 is incorrect: the Telecommunications Act replaced the Indian Telegraph Act, 1885 and the Indian Wireless Telegraphy Act, 1933; cable television remains under its own 1995 Act.",
  "statute-recent-laws-replaced-pairs", "Bharatiya Vayuyan Adhiniyam, 2024; Immigration and Foreigners Act, 2025; Bharatiya Sakshya Adhiniyam, 2023; Telecommunications Act, 2023.")

pairs(SL, "medium", "Consider the following pairs of Acts passed in 2023 and their subject matter:",
  ["Mediation Act, 2023", "Jan Vishwas (Amendment of Provisions) Act, 2023", "Press and Registration of Periodicals Act, 2023", "Post Office Act, 2023"],
  ["An institutional framework for mediation, including online mediation", "Decriminalisation of minor offences across a number of central laws", "Regulation of OTT streaming platforms", "Replacement of the Indian Post Office Act, 1898"],
  2,
  "Pairs 1, 2 and 4 are correct: the Mediation Act created a statutory framework for mediation (with a Mediation Council of India and provision for online mediation), the Jan Vishwas Act decriminalised minor offences in 42 central Acts to improve ease of doing business, and the Post Office Act replaced the 1898 law. Pair 3 is incorrect: the Press and Registration of Periodicals Act replaced the Press and Registration of Books Act, 1867 and deals with the registration of periodicals through the Press Registrar General; it does not regulate OTT platforms.",
  "statute-acts-2023-subject-pairs", "Mediation Act, 2023; Jan Vishwas (Amendment of Provisions) Act, 2023; Press and Registration of Periodicals Act, 2023; Post Office Act, 2023.")

# ================= UNION & STATE EXECUTIVE =================
# ---------------- medium statement_based x4 ----------------
stmt(EX, "medium", "Consider the following statements regarding the Governor of a State:",
  ["The Governor is appointed by the President by warrant under his hand and seal.",
   "The same person can be appointed as Governor of two or more States.",
   "The Constitution lays down the grounds on which a Governor can be removed from office."],
  C3, 1,
  "Statements 1 and 2 are correct: Art. 155 provides for appointment by the President by warrant under his hand and seal, and the 7th Amendment (1956) allowed one person to be Governor of two or more States. Statement 3 is incorrect: the Governor holds office during the pleasure of the President (Art. 156) and the Constitution lays down no grounds for removal -- though in B.P. Singhal (2010) the Supreme Court held that the pleasure cannot be exercised arbitrarily.",
  "executive-governor-appointment-removal", f"Constitution of India, Arts. 153, 155 and 156; B.P. Singhal v. Union of India (2010); {LAX} -- chapter on the Governor.")

stmt(EX, "medium", "Consider the following statements regarding the President's veto power over Bills passed by Parliament:",
  ["The President can exercise an absolute veto over a private member's Bill.",
   "The President can exercise a suspensive veto by returning a Money Bill to the Lok Sabha for reconsideration.",
   "The Constitution does not prescribe a time limit within which the President must act on a Bill presented for assent, which makes a pocket veto possible.",
   "The President has no veto power over a Constitution Amendment Bill."],
  C4, 2,
  "Statements 1, 3 and 4 are correct: an absolute veto (withholding assent) is typically used for private members' Bills; Art. 111 sets no time limit, which enabled President Zail Singh's pocket veto of the Indian Post Office (Amendment) Bill in 1986; and after the 24th Amendment the President must assent to a Constitution Amendment Bill. Statement 2 is incorrect: a Money Bill cannot be returned for reconsideration -- the President may give or withhold assent, but has no suspensive veto over it.",
  "executive-presidential-veto-types", f"Constitution of India, Arts. 111 and 368(2); {LAX} -- chapter on the President (veto power).")

stmt(EX, "medium", "Consider the following statements regarding the Prime Minister of India:",
  ["The Constitution lays down a specific procedure for the selection and appointment of the Prime Minister.",
   "A person must be a member of the Lok Sabha at the time of appointment as Prime Minister."],
  T2, 3,
  "Neither statement is correct. Statement 1 is incorrect: Art. 75 merely says the Prime Minister shall be appointed by the President and lays down no procedure for the selection; by convention the President appoints the leader of the majority party or coalition in the Lok Sabha. Statement 2 is incorrect: a member of either House -- or even a non-member, who must then become a member of either House within six months -- can be appointed; several Prime Ministers have been members of the Rajya Sabha.",
  "executive-prime-minister-appointment", f"Constitution of India, Art. 75; {LAX} -- chapter on the Prime Minister.")

stmt(EX, "medium", "Consider the following statements regarding the Chief Minister and the State Council of Ministers:",
  ["The Chief Minister is appointed by the President on the recommendation of the Governor.",
   "A person who is not a member of the State Legislature can be appointed Chief Minister, but must be elected to the Legislature within three months.",
   "The total number of ministers in a State, including the Chief Minister, cannot be less than fifteen."],
  C3, 3,
  "None of the statements is correct. The Chief Minister is appointed by the Governor (Art. 164(1)), not the President. A non-member may be appointed but must become a member of the State Legislature within six months, not three (Art. 164(4)). Under Art. 164(1A), inserted by the 91st Amendment, the total number of ministers including the Chief Minister cannot exceed 15 per cent of the Assembly's strength, but cannot be less than twelve.",
  "executive-chief-minister-council-state", f"Constitution of India, Art. 164; {LAX} -- chapters on the Chief Minister and the State Council of Ministers.")

# ---------------- hard statement_based x2 ----------------
stmt(EX, "hard", "Consider the following statements regarding the Supreme Court's opinion of November 2025 on the Presidential Reference relating to assent to State Bills:",
  ["The reference was made by the President under Article 143 of the Constitution.",
   "The Court opined that constitutional courts cannot prescribe timelines for the Governor to act on Bills presented under Article 200.",
   "The Court held that a Bill can be deemed to have received assent if the Governor does not act on it within a reasonable time.",
   "The Court held that the Governor can keep a Bill pending indefinitely without communicating any decision."],
  C4, 1,
  "Statements 1 and 2 are correct. After a two-judge bench in State of Tamil Nadu v. Governor of Tamil Nadu (April 2025) had fixed timelines and declared ten Bills 'deemed' assented, the President sought the Court's opinion under Art. 143. On 20 November 2025 the Constitution Bench opined that courts cannot impose timelines on the Governor or the President. Statement 3 is incorrect: the Court rejected the concept of 'deemed assent'. Statement 4 is incorrect: the Court also held that the Governor cannot sit on Bills indefinitely; prolonged, unexplained inaction can attract limited judicial review directing a decision, without the court going into the merits.",
  "executive-presidential-reference-2025-assent", f"Special Reference No. 1 of 2025 (opinion of 20 November 2025); Constitution of India, Arts. 143, 200 and 201; {LAX} -- chapter on the Governor.")

stmt(EX, "hard", "Consider the following statements regarding the Vice-President of India:",
  ["The Vice-President is elected by an electoral college consisting of the members of both Houses of Parliament.",
   "As in the Presidential election, the elected members of the State Legislative Assemblies also vote in the election of the Vice-President.",
   "A formal impeachment is not required for the removal of the Vice-President.",
   "The Vice-President elected in September 2025 after a mid-term vacancy holds office only for the remainder of the predecessor's term."],
  C4, 1,
  "Statements 1 and 3 are correct: the electoral college under Art. 66 comprises all members, elected and nominated, of both Houses of Parliament, and under Art. 67(b) the Vice-President is removed by a Rajya Sabha resolution passed by a majority of all its then members and agreed to by the Lok Sabha -- no impeachment is needed. Statement 2 is incorrect: unlike the Presidential electoral college, the Vice-Presidential one includes no members of the State Legislative Assemblies. Statement 4 is incorrect: under Art. 68(2), a person elected to fill a vacancy caused by resignation holds office for a full term of five years from the date of entering office; C.P. Radhakrishnan, elected on 9 September 2025, therefore has a full five-year term.",
  "executive-vice-president-election-term", f"Constitution of India, Arts. 66-68; Election Commission of India, Vice-Presidential Election 2025; {LAX} -- chapter on the Vice-President.")

# ---------------- mcq (hard 1, medium 1) ----------------
mcq(EX, "hard", "Who discharges the functions of the President of India when the offices of both the President and the Vice-President are vacant?",
  ["The Prime Minister", "The Chief Justice of India", "The Speaker of the Lok Sabha", "The Deputy Chairman of the Rajya Sabha"], 1,
  "Under the President (Discharge of Functions) Act, 1969, when both offices are vacant the Chief Justice of India -- or, if that office is also vacant, the senior-most available judge of the Supreme Court -- discharges the functions of the President until a new President is elected. This happened in 1969, when Chief Justice M. Hidayatullah acted as President.",
  "executive-president-discharge-functions-cji", f"President (Discharge of Functions) Act, 1969; Constitution of India, Art. 65; {LAX} -- chapter on the Vice-President.")

mcq(EX, "medium", "Which one of the following is NOT a power of the Governor of a State?",
  ["Appointing the Advocate General of the State", "Nominating members to the State Legislative Council", "Summoning and proroguing the State Legislature", "Appointing the judges of the High Court of the State"], 3,
  "The judges of a High Court are appointed by the President (Art. 217); the Governor is only consulted. The Governor appoints the Advocate General (Art. 165), nominates one-sixth of the members of a Legislative Council (Art. 171), and summons and prorogues the State Legislature (Art. 174).",
  "executive-governor-powers-not-hc-judges", f"Constitution of India, Arts. 165, 171, 174 and 217; {LAX} -- chapter on the Governor.")

# ---------------- assertion_reason medium x1 ----------------
ar(EX, "medium",
  "The Prime Minister holds office during the pleasure of the President.",
  "The President can dismiss the Prime Minister at his discretion at any time, even while the Prime Minister enjoys the confidence of the Lok Sabha.",
  2,
  "Statement-I is correct: under Art. 75(2) the ministers, including the Prime Minister, hold office during the pleasure of the President. Statement-II is incorrect: because the Council of Ministers is collectively responsible to the Lok Sabha (Art. 75(3)), the President's pleasure in practice means that the Prime Minister cannot be dismissed as long as he or she enjoys the Lok Sabha's confidence.",
  "executive-pm-pleasure-collective-responsibility", f"Constitution of India, Art. 75; {LAX} -- chapter on the Prime Minister.")

# ---------------- match medium x1 ----------------
pairs(EX, "medium", "Consider the following pairs of Articles of the Constitution and their subject matter:",
  ["Article 74", "Article 75", "Article 164", "Article 166"],
  ["Council of Ministers to aid and advise the President", "Duties of the Prime Minister as respects the furnishing of information to the President", "Appointment of the Chief Minister by the President", "Duties of the Chief Minister as respects the furnishing of information to the Governor"],
  0,
  "Only pair 1 is correct: Art. 74 provides for the Council of Ministers to aid and advise the President. Pair 2 is incorrect: the Prime Minister's duty to furnish information is in Art. 78 (Art. 75 covers appointment and other provisions as to ministers). Pair 3 is incorrect: Art. 164 provides for the appointment of the Chief Minister by the Governor. Pair 4 is incorrect: the Chief Minister's duty to furnish information is in Art. 167; Art. 166 deals with the conduct of business of the State Government.",
  "executive-articles-74-78-164-167-pairs", f"Constitution of India, Arts. 74, 75, 78, 164, 166 and 167; {LAX} -- chapters on the Union and State Executive.")

write_sql(os.path.dirname(os.path.abspath(__file__)), "polity_batch5_insert.sql")
