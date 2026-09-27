# -*- coding: utf-8 -*-
"""Polity batch 3: every remaining Governance cell (14) and Federalism & Special Provisions cell (13)
from the live gap report (config e6f68e99, regenerated 2026-09-27)."""
import os
from polity_common import *

GV = "Governance"
FD = "Federalism & Special Provisions"
GOVBK = "M. Laxmikanth, Governance in India"

# ---------------- GOVERNANCE: medium statement_based x5 ----------------
stmt(GV, "medium", "Consider the following statements regarding the All India Services:",
  ["Parliament can create a new All India Service if the Rajya Sabha passes a resolution, supported by not less than two-thirds of the members present and voting, declaring that it is necessary in the national interest.",
   "The Indian Forest Service has been an All India Service since the commencement of the Constitution, along with the IAS and the IPS.",
   "Since members of the All India Services serve under the State Governments, a State Government can dismiss such an officer from service."],
  C3, 0,
  "Only statement 1 is correct: this is the procedure laid down in Art. 312(1). Statement 2 is incorrect: Art. 312(2) deemed only the IAS and the IPS to be All India Services at the commencement of the Constitution; the Indian Forest Service was constituted in 1966 under the All India Services Act, 1951. Statement 3 is incorrect: the State Government has immediate control over these officers, but ultimate control lies with the Centre, and a major penalty such as dismissal can be imposed only by the Central Government.",
  "polity-all-india-services-art312", f"Constitution of India, Art. 312; All India Services Act, 1951; {LAX} -- chapter on Public Services.")

stmt(GV, "medium", "Consider the following statements regarding the Cabinet Secretariat:",
  ["The Government of India (Allocation of Business) Rules, 1961 are made by the President under Article 77 of the Constitution.",
   "The Cabinet Secretariat functions directly under the Prime Minister.",
   "The Cabinet Secretary is the ex-officio Chairman of the Civil Services Board."],
  C3, 2,
  "All three statements are correct. Art. 77(3) empowers the President to make rules for the more convenient transaction of the Government's business and its allocation among Ministers; the Allocation of Business Rules and the Transaction of Business Rules, both of 1961, are made under it. The Cabinet Secretariat works under the direct charge of the Prime Minister, with the Cabinet Secretary as its administrative head, and the Cabinet Secretary is also the ex-officio Chairman of the Civil Services Board.",
  "governance-cabinet-secretariat-art77", f"Constitution of India, Art. 77; Government of India (Allocation of Business) Rules, 1961; {GOVBK} -- chapter on the Cabinet Secretariat.")

stmt(GV, "medium", "With reference to the Members of Parliament Local Area Development Scheme (MPLADS), consider the following statements:",
  ["Each Member of Parliament can recommend works worth up to Rs 5 crore per annum under the scheme.",
   "An elected Member of the Rajya Sabha can recommend works in the districts of any State of his or her choice.",
   "The scheme is administered by the Ministry of Statistics and Programme Implementation."],
  C3, 1,
  "Statements 1 and 3 are correct: the annual entitlement per MP is Rs 5 crore, and the scheme is administered by the Ministry of Statistics and Programme Implementation. Statement 2 is incorrect: an elected Rajya Sabha member may recommend works in one or more districts of the State from which he or she has been elected, not in any State of choice.",
  "governance-mplads-entitlement-rules", "Ministry of Statistics and Programme Implementation, Guidelines on the Members of Parliament Local Area Development Scheme (2023).")

stmt(GV, "medium", "Consider the following statements regarding the Central Bureau of Investigation (CBI):",
  ["The CBI derives its power to investigate from the Delhi Special Police Establishment Act, 1946.",
   "The Director of the CBI is appointed on the recommendation of a committee chaired by the Prime Minister."],
  T2, 2,
  "Both statements are correct. The CBI's legal basis for investigation is the Delhi Special Police Establishment Act, 1946. Since the Lokpal and Lokayuktas Act, 2013 amended the DSPE Act, the Director is appointed on the recommendation of a committee of the Prime Minister (Chairperson), the Leader of the Opposition or leader of the single largest opposition party in the Lok Sabha, and the Chief Justice of India or a Supreme Court judge nominated by the CJI. Readers relying on older notes may wrongly reject statement 2: before 2014 the committee was chaired by the Central Vigilance Commissioner.",
  "governance-cbi-dspe-director-appointment", f"Delhi Special Police Establishment Act, 1946 (as amended by the Lokpal and Lokayuktas Act, 2013); {LAX} -- chapter on the Central Bureau of Investigation.")

stmt(GV, "medium", "Consider the following statements regarding the Administrative Reforms Commissions (ARCs) of India:",
  ["The first ARC, set up in 1966, was initially chaired by Morarji Desai.",
   "The second ARC was constituted in 1999.",
   "The ARCs are constitutional bodies set up under Article 312 of the Constitution."],
  C3, 0,
  "Only statement 1 is correct: the first ARC was constituted in January 1966 with Morarji Desai as chairman (later succeeded by K. Hanumanthaiya). Statement 2 is incorrect: the second ARC was constituted in 2005, chaired by M. Veerappa Moily. Statement 3 is incorrect: both ARCs were set up by executive resolutions of the Government of India; Art. 312 deals with the All India Services.",
  "governance-administrative-reforms-commissions", f"Government of India resolutions constituting the ARCs (1966, 2005); {GOVBK} -- chapter on Administrative Reforms.")

# ---------------- GOVERNANCE: hard statement_based x3 ----------------
stmt(GV, "hard", "With reference to Mission Karmayogi, consider the following statements:",
  ["It was approved by the Union Cabinet in 2020 as the National Programme for Civil Services Capacity Building.",
   "The Prime Minister's Public Human Resources Council, which provides strategic direction to the programme, is chaired by the Prime Minister.",
   "The Capacity Building Commission set up under the programme assists in approving the Annual Capacity Building Plans of government departments.",
   "Karmayogi Bharat, a not-for-profit company, owns and manages the iGOT-Karmayogi digital learning platform."],
  C4, 3,
  "All four statements are correct. The Union Cabinet approved Mission Karmayogi (NPCSCB) in September 2020. Its apex body is the Prime Minister's Public Human Resources Council, chaired by the Prime Minister. The Capacity Building Commission, operational from April 2021, assists the Council in approving Annual Capacity Building Plans. Karmayogi Bharat, a wholly government-owned Section 8 (not-for-profit) company incorporated in 2022, owns and manages the iGOT-Karmayogi platform. This is a trap-in-the-absence question: the reader keeps looking for the planted error.",
  "governance-mission-karmayogi-structure", "Union Cabinet decision on the National Programme for Civil Services Capacity Building, September 2020 (PIB); Capacity Building Commission.")

stmt(GV, "hard", "Consider the following statements regarding the National Investigation Agency (NIA):",
  ["The NIA was constituted under the National Investigation Agency Act, 2008, enacted after the Mumbai terror attacks of November 2008.",
   "After the 2019 amendment of the Act, the NIA can investigate scheduled offences committed outside India against Indian citizens or affecting the interests of India.",
   "The NIA can take over the investigation of a scheduled offence in a State only with the consent of that State Government."],
  C3, 1,
  "Statements 1 and 2 are correct: the NIA Act was passed in December 2008 after the Mumbai attacks, and the 2019 amendment extended the agency's jurisdiction to scheduled offences committed beyond India (while also adding offences such as human trafficking and cyber-terrorism). Statement 3 is incorrect: under Section 6 of the Act, the Central Government can direct the NIA, even suo motu, to investigate a scheduled offence anywhere in India without the State's consent -- unlike the CBI, which ordinarily needs State consent under the DSPE Act.",
  "governance-nia-jurisdiction-consent", "National Investigation Agency Act, 2008 (Section 6) and the NIA (Amendment) Act, 2019.")

stmt(GV, "hard", "Consider the following statements regarding citizen-centric administration in India:",
  ["The Citizen's Charter initiative was taken up in India in 1997, drawing on a model introduced in the United Kingdom in 1991.",
   "Sevottam is a service delivery excellence model developed by the Department of Administrative Reforms and Public Grievances.",
   "Citizen's Charters issued by Union Ministries are legally enforceable in a court of law.",
   "The Centralized Public Grievance Redress and Monitoring System (CPGRAMS) is operated by the Department of Administrative Reforms and Public Grievances."],
  C4, 2,
  "Statements 1, 2 and 4 are correct. India adopted the Citizen's Charter idea in 1997 (the UK had launched it in 1991); DARPG developed the Sevottam model for service delivery excellence, later endorsed by the Second ARC; and CPGRAMS is DARPG's online grievance platform. Statement 3 is incorrect: Citizen's Charters are voluntary declarations of service standards and are not justiciable -- the Citizens' Charter and Grievance Redressal Bill, 2011 that would have made them enforceable lapsed.",
  "governance-citizen-charter-sevottam", f"Department of Administrative Reforms and Public Grievances; Second ARC, 12th Report 'Citizen Centric Administration'; {GOVBK}.")

# ---------------- GOVERNANCE: easy statement_based x1 ----------------
stmt(GV, "easy", "Consider the following statements regarding DigiLocker:",
  ["DigiLocker is an initiative under the Digital India programme.",
   "Documents issued through DigiLocker are treated as legally at par with the original physical documents under the Information Technology rules."],
  T2, 2,
  "Both statements are correct. DigiLocker is a Ministry of Electronics and Information Technology platform under Digital India, and documents issued through it are deemed at par with original physical documents under the Information Technology (Preservation and Retention of Information by Intermediaries Providing Digital Locker Facilities) Rules, 2016.",
  "governance-digilocker-legal-status", "Ministry of Electronics and Information Technology; Information Technology (Preservation and Retention of Information by Intermediaries Providing Digital Locker Facilities) Rules, 2016.")

# ---------------- GOVERNANCE: mcq (hard 1, medium 1) ----------------
mcq(GV, "hard", "Which one of the following States was the first in India to enact a law guaranteeing the delivery of specified public services to citizens within a stipulated time?",
  ["Bihar", "Madhya Pradesh", "Kerala", "Punjab"], 1,
  "Madhya Pradesh enacted the Madhya Pradesh Lok Sewaon ke Pradan ki Guarantee Adhiniyam in August 2010, the first Right to Public Services law in the country; it makes time-bound delivery legally binding and fines officials for delay. Bihar followed in 2011, which makes it the tempting wrong pick.",
  "governance-right-to-public-services-first-state", "Madhya Pradesh Lok Sewaon ke Pradan ki Guarantee Adhiniyam, 2010; Second ARC, 12th Report 'Citizen Centric Administration'.")

mcq(GV, "medium", "Which one of the following is the ICT-based platform through which the Prime Minister reviews major infrastructure projects, government programmes and public grievances directly with Union Secretaries and State Chief Secretaries?",
  ["CPGRAMS", "e-SAKSHI", "PM Gati Shakti National Master Plan", "PRAGATI"], 3,
  "PRAGATI (Pro-Active Governance and Timely Implementation), launched in 2015, is the multi-purpose platform on which the Prime Minister holds review meetings with Union Secretaries and State Chief Secretaries. CPGRAMS is the grievance portal run by DARPG, e-SAKSHI is the MPLADS fund-flow portal, and PM Gati Shakti is a GIS-based plan for multimodal infrastructure connectivity.",
  "governance-pragati-review-platform", "Prime Minister's Office, PRAGATI platform (2015); Ministry of Statistics and Programme Implementation (e-SAKSHI).")

# ---------------- GOVERNANCE: assertion_reason (hard 1, medium 1) ----------------
ar(GV, "hard",
  "Under the Delhi Special Police Establishment Act, 1946, the CBI ordinarily needs the consent of the State Government to investigate an offence within that State.",
  "'Police' is a subject in the State List of the Seventh Schedule.",
  0,
  "Both statements are correct and Statement-II explains Statement-I. Because police and public order are State subjects (State List entries 1 and 2), a central police agency cannot operate in a State's territory as of right; Section 6 of the DSPE Act therefore requires the State's consent (general or case-specific), except where a constitutional court directs a CBI investigation.",
  "governance-cbi-state-consent-police-state-subject", f"Delhi Special Police Establishment Act, 1946 (Section 6); Constitution of India, Seventh Schedule, List II; {LAX} -- chapter on the Central Bureau of Investigation.")

ar(GV, "medium",
  "The Mahatma Gandhi National Rural Employment Guarantee Act, 2005 requires the Gram Sabha to conduct social audits of all the projects taken up under the scheme within the Gram Panchayat.",
  "The Act guarantees 150 days of wage employment in a financial year to every rural household whose adult members volunteer to do unskilled manual work.",
  2,
  "Statement-I is correct: Section 17 of MGNREGA makes the Gram Sabha responsible for regular social audits of all projects under the scheme within the Gram Panchayat. Statement-II is incorrect: the Act guarantees at least 100 days of wage employment per household per financial year; additional days (up to 150) have been allowed only in specific cases, such as drought-notified areas and forest-rights holders, by government decision.",
  "governance-mgnrega-social-audit", "Mahatma Gandhi National Rural Employment Guarantee Act, 2005 (Sections 3 and 17); Ministry of Rural Development.")

# ---------------- GOVERNANCE: match medium x1 ----------------
pairs(GV, "medium", "Consider the following pairs of organisations and the Ministries under which they function:",
  ["Bureau of Energy Efficiency", "Central Pollution Control Board", "Food Safety and Standards Authority of India", "Pension Fund Regulatory and Development Authority"],
  ["Ministry of Power", "Ministry of Environment, Forest and Climate Change", "Ministry of Consumer Affairs, Food and Public Distribution", "Ministry of Labour and Employment"],
  1,
  "Only pairs 1 and 2 are correct. The Bureau of Energy Efficiency is a statutory body under the Ministry of Power (Energy Conservation Act, 2001), and the Central Pollution Control Board functions under the Ministry of Environment, Forest and Climate Change. Pair 3 is a name trap: FSSAI (Food Safety and Standards Act, 2006) is under the Ministry of Health and Family Welfare, not the food ministry. Pair 4 is incorrect: PFRDA is under the Ministry of Finance (Department of Financial Services), not the labour ministry.",
  "governance-regulators-parent-ministries", "Energy Conservation Act, 2001; Water (Prevention and Control of Pollution) Act, 1974; Food Safety and Standards Act, 2006; PFRDA Act, 2013.")

# ================= FEDERALISM & SPECIAL PROVISIONS =================
# ---------------- medium statement_based x5 ----------------
stmt(FD, "medium", "Consider the following statements regarding a proclamation of National Emergency under Article 352:",
  ["It must be approved by both Houses of Parliament within two months of its issue.",
   "Once approved by Parliament, it remains in force for one year, and can be extended one year at a time.",
   "A resolution disapproving the continuation of the Emergency must be passed by a special majority of the Lok Sabha."],
  C3, 3,
  "None of the statements is correct. After the 44th Amendment (1978), a proclamation of National Emergency must be approved by both Houses within one month (not two months -- that is the period for President's Rule and Financial Emergency). Once approved it continues for six months and can be extended indefinitely by Parliament's approval every six months. A resolution disapproving its continuation needs only a simple majority of the Lok Sabha; one-tenth of the Lok Sabha's members can seek a special sitting for that purpose.",
  "federalism-national-emergency-approval", f"Constitution of India, Art. 352; {LAX} -- chapter on Emergency Provisions.")

stmt(FD, "medium", "Consider the following statements regarding President's Rule under Article 356:",
  ["A proclamation of President's Rule must be approved by both Houses of Parliament within two months of its issue.",
   "It can be continued beyond one year only if a National Emergency is in operation and the Election Commission certifies that elections to the State Legislative Assembly cannot be held.",
   "During President's Rule, the State Legislative Assembly may be either dissolved or kept in suspended animation.",
   "President's Rule can be continued for a maximum period of three years."],
  C4, 3,
  "All four statements are correct. The proclamation needs parliamentary approval within two months (Art. 356(3)); continuation beyond one year requires both a National Emergency in operation and the Election Commission's certification (Art. 356(5), inserted by the 44th Amendment); the Assembly may be dissolved or kept in suspended animation; and with six-monthly approvals it can run for at most three years.",
  "federalism-presidents-rule-art356", f"Constitution of India, Art. 356; {LAX} -- chapter on Emergency Provisions.")

stmt(FD, "medium", "Consider the following statements regarding the legislative relations between the Centre and the States:",
  ["The residuary powers of legislation are vested in the State Legislatures.",
   "A law made by Parliament on a State List subject under Article 249 remains in force indefinitely, even after the Rajya Sabha's resolution lapses.",
   "Parliament can make a law on a State List subject to implement an international treaty only with the consent of the States concerned."],
  C3, 3,
  "None of the statements is correct. Residuary powers belong to Parliament under Art. 248 (a Canadian-style feature). A resolution under Art. 249 remains in force for one year (renewable), and a law made under it ceases to have effect six months after the resolution ceases. Under Art. 253, Parliament can legislate on any subject, including State List subjects, to implement international treaties, agreements and conventions, without the consent of the States.",
  "federalism-legislative-relations-248-249-253", f"Constitution of India, Arts. 248, 249 and 253; {LAX} -- chapter on Centre-State Relations.")

stmt(FD, "medium", "Consider the following statements regarding administrative relations between the Centre and the States:",
  ["Article 256 requires the executive power of every State to be exercised so as to ensure compliance with the laws made by Parliament.",
   "Under Article 258, the President may, without the consent of a State Government, entrust to that Government functions in relation to any matter to which the executive power of the Union extends."],
  T2, 0,
  "Only statement 1 is correct: Art. 256 obliges States to exercise their executive power so as to ensure compliance with Union laws, and the Union may give directions for this purpose. Statement 2 is incorrect: under Art. 258(1) the President can entrust Union functions to a State Government only with that Government's consent; entrustment without consent is possible only by a law of Parliament under Art. 258(2).",
  "federalism-administrative-relations-256-258", f"Constitution of India, Arts. 256 and 258; {LAX} -- chapter on Centre-State Relations.")

stmt(FD, "medium", "Consider the following statements regarding inter-State river water disputes:",
  ["Under Article 262, Parliament may by law provide that neither the Supreme Court nor any other court shall exercise jurisdiction over such disputes.",
   "Water disputes tribunals under the Inter-State River Water Disputes Act, 1956 are constituted by the Central Government.",
   "The decision of a water disputes tribunal under the Act has the same force as an order or decree of the Supreme Court."],
  C3, 2,
  "All three statements are correct. Art. 262(2) allows Parliament to exclude the jurisdiction of all courts, including the Supreme Court, over such disputes; under the Inter-State River Water Disputes Act, 1956 the Central Government constitutes a tribunal when a dispute cannot be settled by negotiation; and Section 6(2) of the Act (inserted in 2002) gives a tribunal's decision the same force as an order or decree of the Supreme Court. The tempting error is to assume that the Supreme Court sets up the tribunals.",
  "federalism-inter-state-water-disputes-art262", f"Constitution of India, Art. 262; Inter-State River Water Disputes Act, 1956; {LAX} -- chapter on Inter-State Relations.")

# ---------------- hard statement_based x3 ----------------
stmt(FD, "hard", "Consider the following statements regarding the Sixth Schedule to the Constitution of India:",
  ["Each autonomous district has a District Council of not more than thirty members, of whom not more than four are nominated by the Governor.",
   "The Governor can organise and reorganise the autonomous districts, including increasing or decreasing their areas.",
   "Acts of Parliament and of the State Legislature apply to the autonomous districts automatically and without modification.",
   "The District Councils can constitute village councils or courts for the trial of suits and cases between the Scheduled Tribes."],
  C4, 2,
  "Statements 1, 2 and 4 are correct under paragraphs 1, 2 and 4 of the Sixth Schedule. Statement 3 is incorrect: Acts of Parliament or of the State Legislature do not apply automatically to autonomous districts -- the Governor (or, for some States, the President) can direct that they shall not apply or shall apply with modifications and exceptions (paragraph 12 and related provisions).",
  "federalism-sixth-schedule-district-councils", f"Constitution of India, Sixth Schedule; {LAX} -- chapter on Scheduled and Tribal Areas.")

stmt(FD, "hard", "Consider the following statements regarding the GST Council:",
  ["It is a constitutional body established under Article 279A.",
   "Its decisions require a majority of not less than three-fourths of the weighted votes of the members present and voting, with the Central Government's vote carrying a weightage of one-third of the total votes cast.",
   "In Union of India v. Mohit Minerals (2022), the Supreme Court held that the recommendations of the GST Council are binding on Parliament and the State Legislatures."],
  C3, 1,
  "Statements 1 and 2 are correct: Art. 279A (inserted by the 101st Amendment, 2016) creates the Council, and its voting rule gives the Centre one-third and all States together two-thirds of the weighted votes, with a three-fourths majority needed. Statement 3 reverses the holding: in Mohit Minerals (May 2022) the Court held that the Council's recommendations are not binding and have only persuasive value, since Parliament and the State Legislatures have simultaneous power to legislate on GST.",
  "federalism-gst-council-mohit-minerals", f"Constitution of India, Art. 279A; Union of India v. Mohit Minerals Pvt. Ltd. (2022); {LAX} -- chapter on the Goods and Services Tax Council.")

stmt(FD, "hard", "Consider the following statements regarding the effect of Emergencies on citizens and finances:",
  ["Article 19 is automatically suspended on any proclamation of National Emergency, including one made on the ground of armed rebellion.",
   "During a National Emergency, the President cannot suspend the right to move courts for the enforcement of the rights guaranteed by Articles 20 and 21.",
   "A proclamation of Financial Emergency under Article 360 must be approved by both Houses of Parliament within one month of its issue.",
   "No Financial Emergency has been proclaimed in India so far."],
  C4, 1,
  "Statements 2 and 4 are correct: after the 44th Amendment, Art. 359 cannot be used to suspend the enforcement of Arts. 20 and 21, and Art. 360 has never been invoked. Statement 1 is incorrect: under Art. 358 (as amended by the 44th Amendment), Art. 19 is automatically suspended only when the Emergency is declared on the ground of war or external aggression, not armed rebellion. Statement 3 is incorrect: a Financial Emergency must be approved within two months, and once approved it continues indefinitely until revoked.",
  "federalism-emergency-effects-358-359-360", f"Constitution of India, Arts. 358, 359 and 360; {LAX} -- chapter on Emergency Provisions.")

# ---------------- mcq (hard 1, medium 1) ----------------
mcq(FD, "hard", "Which one of the following is levied by the Union but collected and appropriated by the States under Article 268 of the Constitution?",
  ["Stamp duties on bills of exchange, cheques and promissory notes", "Corporation tax", "Customs duties", "Taxes on agricultural income"], 0,
  "Art. 268 covers duties levied by the Union but collected and appropriated by the States -- stamp duties on bills of exchange, cheques, promissory notes and similar instruments mentioned in the Union List (the 101st Amendment removed the excise duties on medicinal and toilet preparations from this Article). Corporation tax and customs duties are levied and collected by the Union, and tax on agricultural income is a State tax.",
  "federalism-art268-stamp-duties", f"Constitution of India, Arts. 268-270; {LAX} -- chapter on Centre-State Relations (financial relations).")

mcq(FD, "medium", "Which one of the following committees on Centre-State relations was appointed by a State Government rather than by the Union Government?",
  ["Sarkaria Commission", "Punchhi Commission", "Rajamannar Committee", "National Commission to Review the Working of the Constitution"], 2,
  "The Rajamannar Committee was appointed by the Tamil Nadu Government in 1969 to examine Centre-State relations and recommended greater State autonomy. The Sarkaria Commission (1983), the Punchhi Commission (2007) and the National Commission to Review the Working of the Constitution (Venkatachaliah, 2000) were all appointed by the Union Government.",
  "federalism-centre-state-commissions", f"{LAX} -- chapter on Centre-State Relations.")

# ---------------- assertion_reason (hard 1, medium 1) ----------------
ar(FD, "hard",
  "A law made by a State Legislature on a Concurrent List subject can prevail in that State even though it is repugnant to an earlier law made by Parliament on that subject.",
  "Under Article 254(2), such a State law prevails in that State if it has been reserved for the consideration of the President and has received his assent.",
  0,
  "Both statements are correct and Statement-II explains Statement-I. The general rule in Art. 254(1) is that the Union law prevails over a repugnant State law on a Concurrent List subject, but Art. 254(2) creates the exception: a State law reserved for and assented to by the President prevails in that State. Parliament can still later override it by a fresh law on the same matter.",
  "federalism-art254-repugnancy-presidential-assent", f"Constitution of India, Art. 254; {LAX} -- chapter on Centre-State Relations.")

ar(FD, "medium",
  "The word 'federation' is used in Article 1 of the Constitution to describe India.",
  "Article 1 describes India as a 'Union of States'.",
  3,
  "Statement-I is incorrect: the word 'federation' does not appear anywhere in the Constitution. Statement-II is correct: Art. 1 describes India, that is Bharat, as a 'Union of States'. Dr. B. R. Ambedkar explained that the phrase indicates the federation is not the result of an agreement among the States, and that no State has the right to secede from it.",
  "federalism-union-of-states-art1", f"Constitution of India, Art. 1; {LAX} -- chapter on the Federal System.")

# ---------------- match medium x1 ----------------
pairs(FD, "medium", "Consider the following pairs of Articles of the Constitution and the matters for which they make special provision:",
  ["Article 244A", "Article 371G", "Article 371H", "Article 239AA"],
  ["An autonomous State within Assam comprising certain tribal areas", "Goa", "Sikkim", "The National Capital Territory of Delhi"],
  1,
  "Only pairs 1 and 4 are correct: Art. 244A (22nd Amendment, 1969) allows Parliament to form an autonomous State within Assam, and Art. 239AA (69th Amendment, 1991) contains the special provisions for Delhi. Pair 2 is incorrect: Art. 371G relates to Mizoram (Goa is Art. 371I). Pair 3 is incorrect: Art. 371H relates to Arunachal Pradesh (Sikkim is Art. 371F).",
  "federalism-special-provision-articles-pairs", f"Constitution of India, Arts. 239AA, 244A and 371-371J; {LAX} -- chapter on Special Provisions for Some States.")

write_sql(os.path.dirname(os.path.abspath(__file__)), "polity_batch3_insert.sql")
