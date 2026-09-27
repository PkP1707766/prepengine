# -*- coding: utf-8 -*-
"""Polity batch 6: every remaining cell for Fundamental Rights, DPSP & Duties (11), Constitutional &
Statutory Bodies (4), Judicial-Verdicts (4), Panchayati Raj & Local Governance (5), Elections (4) and
Judiciary (2), from the live gap report (config e6f68e99, regenerated 2026-09-27). Answers in this
batch were steered toward the under-used ladder answers (All three / None, Only one / All four,
2 only / Neither) after a live tally of batches 1-5. 2024 verdicts and the CEC Act, 2023 were
cross-checked by web search on 2026-09-27."""
import os
from polity_common import *

FR = "Fundamental Rights, DPSP & Duties"
BO = "Constitutional & Statutory Bodies"
JV = "Judicial-Verdicts"
PR = "Panchayati Raj & Local Governance"
EL = "Elections"
JU = "Judiciary"

# ================= FUNDAMENTAL RIGHTS, DPSP & DUTIES =================
stmt(FR, "medium", "Consider the following statements regarding the Fundamental Rights:",
  ["Article 17 abolishes 'untouchability' and forbids its practice in any form.",
   "Article 18 prohibits the State from conferring titles, but exempts military and academic distinctions.",
   "The prohibition of discrimination in access to shops, public restaurants, hotels and places of public entertainment under Article 15(2) applies to private individuals as well as to the State."],
  C3, 2,
  "All three statements are correct. Art. 17 abolishes untouchability, and its enforcement is backed by the Protection of Civil Rights Act, 1955. Art. 18 bars the State from conferring titles other than military and academic distinctions. Art. 15(2) is one of the few Fundamental Rights that operate against private individuals too -- the tempting error is to assume that every Fundamental Right binds only the State.",
  "rights-articles-15-17-18", f"Constitution of India, Arts. 15, 17 and 18; {LAX} -- chapter on Fundamental Rights.")

stmt(FR, "medium", "Consider the following statements regarding the right to freedom of religion:",
  ["Article 25 guarantees freedom of conscience and the right to profess, practise and propagate religion to citizens only.",
   "Article 28 permits religious instruction in educational institutions wholly maintained out of State funds.",
   "Article 27 permits the State to compel a person to pay taxes whose proceeds are specifically appropriated for the promotion of a particular religion."],
  C3, 3,
  "None of the statements is correct. Art. 25 is available to all persons, citizens and foreigners alike. Art. 28(1) prohibits religious instruction in educational institutions wholly maintained out of State funds. Art. 27 does the opposite of statement 3: no person can be compelled to pay taxes whose proceeds are specifically appropriated for promoting or maintaining any particular religion.",
  "rights-freedom-of-religion-25-28", f"Constitution of India, Arts. 25-28; {LAX} -- chapter on Fundamental Rights.")

stmt(FR, "medium", "Consider the following statements regarding the Directive Principles of State Policy:",
  ["Article 45 directs the State to provide early childhood care and education for all children until they complete the age of six years.",
   "Article 40 directs the State to organise village panchayats.",
   "Article 44 directs the State to endeavour to secure a Uniform Civil Code for the citizens throughout the territory of India.",
   "Article 50 directs the State to take steps to separate the judiciary from the executive in the public services of the State."],
  C4, 3,
  "All four statements are correct. Art. 45 was recast by the 86th Amendment (2002) to cover early childhood care and education up to the age of six, once elementary education for 6-14 year-olds became a Fundamental Right under Art. 21A; Arts. 40, 44 and 50 are Gandhian and liberal-intellectual principles that have remained unchanged.",
  "rights-dpsp-articles-40-44-45-50", f"Constitution of India, Arts. 40, 44, 45 and 50; {LAX} -- chapter on Directive Principles of State Policy.")

stmt(FR, "medium", "Consider the following statements regarding the Fundamental Duties:",
  ["The Fundamental Duties were part of the Constitution as originally adopted in 1949.",
   "The Fundamental Duties are not enforceable by the courts."],
  T2, 1,
  "Only statement 2 is correct: the Fundamental Duties in Art. 51A are non-justiciable, though courts may take them into account when judging the reasonableness of a law. Statement 1 is incorrect: they were added by the 42nd Amendment (1976) on the recommendation of the Swaran Singh Committee, with the eleventh duty added by the 86th Amendment (2002).",
  "rights-fundamental-duties-origin", f"Constitution of India, Art. 51A (Part IV-A); {LAX} -- chapter on Fundamental Duties.")

stmt(FR, "hard", "Consider the following statements regarding the Fundamental Rights:",
  ["Under Article 20(3), no person accused of an offence shall be compelled to be a witness against himself.",
   "The protection against double jeopardy under Article 20(2) also bars proceedings before departmental or administrative authorities.",
   "Article 21A makes free and compulsory education a Fundamental Right for all children up to the age of eighteen years.",
   "Article 20(1) prohibits retrospective civil and tax laws as well as retrospective criminal laws."],
  C4, 0,
  "Only statement 1 is correct: Art. 20(3) is the protection against self-incrimination. Statement 2 is incorrect: double jeopardy protection applies only to proceedings before a court of law or a judicial tribunal, not departmental or administrative proceedings. Statement 3 is incorrect: Art. 21A covers children of the age of six to fourteen years. Statement 4 is incorrect: Art. 20(1) bars only ex post facto criminal laws; civil or tax laws can be made retrospective.",
  "rights-article-20-21a-scope", f"Constitution of India, Arts. 20 and 21A; {LAX} -- chapter on Fundamental Rights.")

stmt(FR, "hard", "Consider the following statements regarding reservation for the economically weaker sections (EWS):",
  ["The 103rd Amendment Act, 2019 inserted Articles 15(5) and 16(5) to enable reservation for the economically weaker sections.",
   "In Janhit Abhiyan v. Union of India (2022), a Constitution Bench upheld the EWS reservation by a 4:1 majority.",
   "Persons belonging to the Scheduled Castes, Scheduled Tribes and Other Backward Classes are eligible for the EWS quota if they satisfy the income criterion."],
  C3, 3,
  "None of the statements is correct. The 103rd Amendment inserted Arts. 15(6) and 16(6); Art. 15(5), inserted by the 93rd Amendment (2005), concerns reservation in educational institutions for socially and educationally backward classes, SCs and STs. The EWS reservation was upheld in Janhit Abhiyan by a 3:2 majority of the five-judge bench. The EWS quota expressly excludes persons who already benefit from SC, ST or OBC reservation.",
  "rights-ews-reservation-103rd", f"Constitution of India, Arts. 15(6) and 16(6); Janhit Abhiyan v. Union of India (2022); {LAX} -- chapter on Fundamental Rights.")

mcq(FR, "hard", "Which one of the following Directive Principles was inserted by the 97th Amendment Act, 2011?",
  ["Promotion of co-operative societies (Article 43B)", "Equal justice and free legal aid (Article 39A)", "Participation of workers in the management of industries (Article 43A)", "Protection and improvement of the environment (Article 48A)"], 0,
  "The 97th Amendment (2011) inserted Art. 43B on the promotion of co-operative societies, along with Part IXB and the words 'or co-operative societies' in Art. 19(1)(c). Arts. 39A, 43A and 48A were all inserted earlier, by the 42nd Amendment (1976).",
  "rights-dpsp-97th-amendment-43b", f"Constitution of India, Arts. 39A, 43A, 43B and 48A; {LAX} -- chapter on Directive Principles of State Policy.")

mcq(FR, "medium", "Which Article of the Constitution did Dr. B. R. Ambedkar describe as the 'heart and soul' of the Constitution?",
  ["Article 14", "Article 19", "Article 32", "Article 21"], 2,
  "Dr. Ambedkar called Art. 32 -- the right to move the Supreme Court for the enforcement of Fundamental Rights -- the very soul and heart of the Constitution, since without a remedy the other rights would be meaningless. The Supreme Court has held Art. 32 to be part of the basic structure.",
  "rights-article-32-heart-and-soul", f"Constitution of India, Art. 32; {LAX} -- chapter on Fundamental Rights (right to constitutional remedies).")

ar(FR, "hard",
  "A law giving effect to the Directive Principles in Article 39(b) or (c) cannot be challenged on the ground that it violates Article 14 or Article 19.",
  "In Minerva Mills (1980), the Supreme Court held that the harmony and balance between the Fundamental Rights and the Directive Principles is an essential feature of the basic structure.",
  1,
  "Both statements are correct, but Statement-II does not explain Statement-I. Statement-I is the protection in Art. 31C as it survives after Kesavananda Bharati and Minerva Mills. Statement-II is the reasoning Minerva Mills used to strike down the 42nd Amendment's extension of that protection to all the Directive Principles -- it explains why Art. 31C was cut back, not why the Art. 39(b)-(c) protection exists.",
  "rights-art31c-minerva-harmony", f"Constitution of India, Art. 31C; Minerva Mills v. Union of India (1980); {LAX} -- chapters on Directive Principles and the Basic Structure.")

ar(FR, "medium",
  "The Directive Principles of State Policy cannot be enforced by the courts.",
  "Article 37 expressly provides that the Directive Principles shall not be enforceable by any court, though they are fundamental in the governance of the country.",
  0,
  "Both statements are correct and Statement-II explains Statement-I: the non-justiciability of the Directive Principles flows directly from the text of Art. 37, which also makes it the duty of the State to apply them in making laws.",
  "rights-dpsp-non-justiciable-art37", f"Constitution of India, Art. 37; {LAX} -- chapter on Directive Principles of State Policy.")

pairs(FR, "medium", "Consider the following pairs of Fundamental Rights and the persons to whom they are available:",
  ["Article 15 (prohibition of discrimination)", "Article 21 (protection of life and personal liberty)", "Article 29 (protection of the interests of minorities)", "Article 25 (freedom of religion)"],
  ["Citizens only", "All persons, including foreigners", "Citizens only", "All persons, including foreigners"],
  3,
  "All four pairs are correct. Arts. 15, 16, 19, 29 and 30 are available only to citizens (Art. 29(1) speaks of 'any section of the citizens'), while Arts. 14, 20, 21, 21A, 22, 23, 24, 25, 26, 27 and 28 are available to all persons, citizens or foreigners, except enemy aliens in some cases.",
  "rights-citizens-vs-all-persons-pairs", f"Constitution of India, Part III; {LAX} -- chapter on Fundamental Rights.")

# ================= CONSTITUTIONAL & STATUTORY BODIES =================
stmt(BO, "medium", "Consider the following statements regarding the Union Public Service Commission (UPSC):",
  ["The UPSC is consulted on disciplinary matters affecting a person serving under the Government of India in a civil capacity.",
   "The UPSC is not consulted on the reservation of appointments or posts in favour of backward classes under Article 16(4).",
   "The UPSC presents an annual report on its work to the President."],
  C3, 2,
  "All three statements are correct: Art. 320(3)(c) requires consultation on disciplinary matters, Art. 320(4) excludes reservations made under Art. 16(4) from its consultative role, and under Art. 323 the Commission reports annually to the President, who lays the report before Parliament with a memorandum explaining any cases where its advice was not accepted.",
  "bodies-upsc-functions-art320", f"Constitution of India, Arts. 320 and 323; {LAX} -- chapter on the Union Public Service Commission.")

stmt(BO, "medium", "Consider the following statements regarding a State Public Service Commission:",
  ["A member of a State Public Service Commission can be removed from office by the Governor.",
   "The Chairman of a State Public Service Commission is eligible for appointment as the Chairman or a member of the UPSC."],
  T2, 1,
  "Only statement 2 is correct: under Art. 319(c) the Chairman of a State PSC may be appointed Chairman or member of the UPSC, or Chairman of another State PSC, but to no other government office. Statement 1 is incorrect: although the Governor appoints them, members of a State PSC can be removed only by the President (Art. 317) -- an appointment-removal split that is a favourite trap.",
  "bodies-state-psc-removal-eligibility", f"Constitution of India, Arts. 316, 317 and 319; {LAX} -- chapter on the State Public Service Commission.")

stmt(BO, "hard", "Consider the following statements regarding national commissions for weaker sections:",
  ["The National Commission for Backward Classes was given constitutional status by the 102nd Amendment Act, 2018.",
   "The National Commission for Scheduled Tribes was created as a separate body by the 65th Amendment Act, 1990.",
   "The National Commission for Minorities is a constitutional body.",
   "The Chairperson of the National Commission for Scheduled Castes is appointed by the Prime Minister."],
  C4, 0,
  "Only statement 1 is correct: the 102nd Amendment inserted Art. 338B. Statement 2 is incorrect: the 65th Amendment (1990) created a combined National Commission for SCs and STs; the separate NCST (Art. 338A) came with the 89th Amendment (2003). Statement 3 is incorrect: the National Commission for Minorities is a statutory body under the NCM Act, 1992. Statement 4 is incorrect: the NCSC's Chairperson is appointed by the President by warrant under his hand and seal (Art. 338(3)).",
  "bodies-national-commissions-338-338a-338b", f"Constitution of India, Arts. 338, 338A and 338B; National Commission for Minorities Act, 1992; {LAX} -- chapters on the National Commissions.")

ar(BO, "medium",
  "The Comptroller and Auditor General of India is appointed by the President on the recommendation of a committee headed by the Prime Minister.",
  "The salary and other conditions of service of the Comptroller and Auditor General are determined by Parliament.",
  3,
  "Statement-I is incorrect: Art. 148 simply provides that the CAG shall be appointed by the President by warrant under his hand and seal; no selection committee is prescribed. Statement-II is correct: under Art. 148(3) the CAG's salary and conditions of service are determined by Parliament (now under the CAG's (Duties, Powers and Conditions of Service) Act, 1971), and cannot be varied to his disadvantage after appointment.",
  "bodies-cag-appointment-service-conditions", f"Constitution of India, Art. 148; {LAX} -- chapter on the Comptroller and Auditor General of India.")

# ================= JUDICIAL-VERDICTS =================
stmt(JV, "medium", "Consider the following statements regarding landmark judgments on the amending power:",
  ["In Kesavananda Bharati (1973), the Supreme Court held that Parliament cannot amend the basic structure of the Constitution.",
   "In Minerva Mills (1980), the Supreme Court struck down the clauses of the 42nd Amendment that had excluded judicial review of constitutional amendments.",
   "In I.R. Coelho (2007), the Supreme Court held that laws placed in the Ninth Schedule after 24 April 1973 can be challenged if they violate the basic structure.",
   "In Golaknath (1967), the Supreme Court held that Parliament could not amend the Fundamental Rights."],
  C4, 3,
  "All four statements are correct. Golaknath (1967) held that Parliament could not abridge Fundamental Rights; Kesavananda Bharati (1973) replaced this with the basic structure limit; Minerva Mills (1980) struck down clauses (4) and (5) of Art. 368, inserted by the 42nd Amendment, which had barred judicial review of amendments; and I.R. Coelho (2007) held Ninth Schedule laws added after 24 April 1973 (the date of the Kesavananda judgment) open to basic-structure review.",
  "verdicts-basic-structure-sequence", f"Golaknath (1967); Kesavananda Bharati (1973); Minerva Mills (1980); I.R. Coelho (2007); {LAX} -- chapter on the Basic Structure of the Constitution.")

stmt(JV, "medium", "Consider the following statements regarding recent Supreme Court judgments:",
  ["In Association for Democratic Reforms v. Union of India (2024), the Supreme Court struck down the Electoral Bond Scheme as violative of the voters' right to information under Article 19(1)(a).",
   "In State of Punjab v. Davinder Singh (2024), the Supreme Court held that the States can sub-classify the Scheduled Castes for the purpose of reservation.",
   "In the Article 370 case (2023), the Supreme Court upheld the constitutional validity of the abrogation of the special status of Jammu and Kashmir."],
  C3, 2,
  "All three statements are correct. The electoral bonds judgment (February 2024) struck down the scheme and the related amendments for violating the right to information; the seven-judge bench in Davinder Singh (August 2024) allowed sub-classification of SCs, overruling E.V. Chinnaiah (2004); and In re Article 370 (December 2023) upheld the 2019 Presidential Orders, while directing restoration of statehood at the earliest and elections to the Assembly.",
  "verdicts-2023-2024-bonds-subclassification-370", "Association for Democratic Reforms v. Union of India (2024); State of Punjab v. Davinder Singh (2024); In re Article 370 of the Constitution (2023).")

stmt(JV, "hard", "Consider the following statements regarding Supreme Court judgments delivered in 2024:",
  ["In Property Owners Association v. State of Maharashtra, a nine-judge bench held that not every privately owned resource is a 'material resource of the community' under Article 39(b).",
   "In Mineral Area Development Authority v. Steel Authority of India, the Court held that royalty on minerals is a tax, so the States cannot levy a separate tax on mineral rights.",
   "In Sita Soren v. Union of India, the Court held that legislators do not enjoy immunity from prosecution for accepting a bribe in connection with a vote or speech in the House.",
   "In the Aligarh Muslim University case, the Court held that an institution established by a statute can never claim minority status under Article 30."],
  C4, 1,
  "Statements 1 and 3 are correct: Property Owners Association (November 2024) rejected the view that all private property is a community resource, and Sita Soren (March 2024) overruled P.V. Narasimha Rao (1998) on legislators' immunity for bribery. Statement 2 reverses the holding: in Mineral Area Development Authority (July 2024) the Court held by 8:1 that royalty is not a tax and that the States do have the power to tax mineral rights. Statement 4 is incorrect: the seven-judge bench (November 2024) overruled Azeez Basha (1967) and held that statutory incorporation does not by itself take away an institution's minority character.",
  "verdicts-2024-poa-mada-sita-soren-amu", "Property Owners Association v. State of Maharashtra (2024); Mineral Area Development Authority v. Steel Authority of India (2024); Sita Soren v. Union of India (2024); Aligarh Muslim University v. Naresh Agarwal (2024).")

mcq(JV, "hard", "In which one of the following cases did the Supreme Court hold that the decision of the presiding officer on disqualification under the Tenth Schedule is subject to judicial review?",
  ["S.R. Bommai v. Union of India", "Nabam Rebia v. Deputy Speaker", "Kihoto Hollohan v. Zachillhu", "Indra Sawhney v. Union of India"], 2,
  "In Kihoto Hollohan (1992) the Supreme Court upheld the Tenth Schedule but struck down paragraph 7, which barred courts' jurisdiction, holding that the presiding officer acts as a tribunal whose decisions are subject to judicial review. S.R. Bommai (1994) concerned President's Rule, Nabam Rebia (2016) a Speaker facing a removal notice deciding disqualification petitions, and Indra Sawhney (1992) OBC reservation.",
  "verdicts-kihoto-hollohan-tenth-schedule", f"Kihoto Hollohan v. Zachillhu (1992); {LAX} -- chapter on the Anti-Defection Law.")

# ================= PANCHAYATI RAJ & LOCAL GOVERNANCE =================
stmt(PR, "medium", "Consider the following statements regarding the 73rd Constitutional Amendment Act, 1992:",
  ["It added Part IX and the Eleventh Schedule to the Constitution.",
   "It reserves not less than one-half of the seats in every Panchayat for women.",
   "It makes it mandatory for every State to reserve seats for the Other Backward Classes in the Panchayats."],
  C3, 0,
  "Only statement 1 is correct. Statement 2 is incorrect: Art. 243D reserves not less than one-third of the seats (and chairperson posts) for women; the one-half reservation found in many States comes from State laws. Statement 3 is incorrect: Art. 243D(6) only enables a State to reserve seats for backward classes -- it is a voluntary provision.",
  "panchayat-73rd-amendment-reservations", f"Constitution of India, Arts. 243D and Part IX; {LAX} -- chapter on Panchayati Raj.")

stmt(PR, "medium", "Consider the following statements regarding urban local government under the 74th Constitutional Amendment Act, 1992:",
  ["It provides for a Municipal Corporation for an area in transition from a rural area to an urban area.",
   "The District Planning Committee consolidates only the plans prepared by the Panchayats in the district."],
  T2, 3,
  "Neither statement is correct. Art. 243Q provides for a Nagar Panchayat for a transitional area, a Municipal Council for a smaller urban area and a Municipal Corporation for a larger urban area. Under Art. 243ZD, the District Planning Committee consolidates the plans prepared by both the Panchayats and the Municipalities in the district.",
  "panchayat-74th-amendment-dpc", f"Constitution of India, Arts. 243Q and 243ZD; {LAX} -- chapter on Municipalities.")

stmt(PR, "hard", "Consider the following statements regarding the Provisions of the Panchayats (Extension to the Scheduled Areas) Act, 1996 (PESA):",
  ["It extends Part IX of the Constitution to the Fifth Schedule areas, with certain modifications.",
   "The Gram Sabha or the Panchayat at the appropriate level must be consulted before land is acquired in the Scheduled Areas for development projects.",
   "The reservation for Scheduled Tribes in every Panchayat in the Scheduled Areas must be not less than one-half of the total number of seats.",
   "All seats of chairpersons of Panchayats at all levels in the Scheduled Areas are reserved for the Scheduled Tribes."],
  C4, 3,
  "All four statements are correct under Section 4 of PESA: Part IX, which does not otherwise apply to Fifth Schedule areas (Art. 243M), is extended to them with modifications; consultation with the Gram Sabha or appropriate Panchayat is required before land acquisition; ST reservation must be at least one-half of the seats; and all chairperson posts at every level are reserved for STs.",
  "panchayat-pesa-1996-provisions", f"Provisions of the Panchayats (Extension to the Scheduled Areas) Act, 1996 (Section 4); Constitution of India, Art. 243M; {LAX} -- chapter on Panchayati Raj.")

mcq(PR, "medium", "Which Article of the Constitution provides for a State Finance Commission to review the financial position of the Panchayats?",
  ["Article 243G", "Article 243H", "Article 243K", "Article 243I"], 3,
  "Art. 243I requires the Governor to constitute a Finance Commission every five years to review the financial position of the Panchayats and recommend the distribution of taxes and grants. Art. 243G deals with the powers and functions of Panchayats, Art. 243H with their power to impose taxes, and Art. 243K with the State Election Commission.",
  "panchayat-state-finance-commission-243i", f"Constitution of India, Arts. 243G-243K; {LAX} -- chapter on Panchayati Raj.")

ar(PR, "medium",
  "A Panchayat constituted after the premature dissolution of a Panchayat continues only for the remainder of the period for which the dissolved Panchayat would have continued.",
  "An election to constitute a Panchayat must be completed within six months from the date of its dissolution.",
  1,
  "Both statements are correct, but Statement-II does not explain Statement-I. Art. 243E(4) limits the reconstituted Panchayat to the balance of the original five-year term, while Art. 243E(3)(b) separately sets the six-month deadline for holding the election. One is a rule about the new body's term, the other about the timing of the poll.",
  "panchayat-dissolution-reconstitution-243e", f"Constitution of India, Art. 243E; {LAX} -- chapter on Panchayati Raj.")

# ================= ELECTIONS =================
ar(EL, "easy",
  "The option of 'None of the Above' (NOTA) was introduced in Indian elections following a Supreme Court judgment.",
  "If NOTA polls the highest number of votes in a constituency, a fresh election must be held there.",
  2,
  "Statement-I is correct: the Election Commission introduced NOTA in 2013 after the Supreme Court's judgment in People's Union for Civil Liberties v. Union of India (2013). Statement-II is incorrect: NOTA votes have no electoral value under the present law; even if NOTA receives the most votes, the candidate with the highest number of votes among the candidates is declared elected.",
  "elections-nota-pucl-2013", "People's Union for Civil Liberties v. Union of India (2013); Election Commission of India instructions on NOTA (2013).")

pairs(EL, "easy", "Consider the following pairs of Articles of the Constitution and their subject matter:",
  ["Article 324", "Article 325", "Article 326", "Article 329"],
  ["Superintendence, direction and control of elections vested in the Election Commission", "No person to be ineligible for inclusion in the electoral roll on grounds of religion, race, caste or sex", "Elections to the Lok Sabha and State Legislative Assemblies on the basis of adult suffrage", "Bar to interference by courts in electoral matters"],
  3,
  "All four pairs are correct: these are the core provisions of Part XV (Elections). Art. 324 vests the superintendence of elections in the Election Commission, Art. 325 provides a single general electoral roll without discrimination, Art. 326 provides for adult suffrage, and Art. 329 bars courts from interfering in electoral matters except through election petitions.",
  "elections-part-xv-articles-pairs", f"Constitution of India, Arts. 324-329 (Part XV); {LAX} -- chapter on Elections.")

stmt(EL, "hard", "Consider the following statements regarding the Chief Election Commissioner and Other Election Commissioners (Appointment, Conditions of Service and Term of Office) Act, 2023:",
  ["The Selection Committee under the Act consists of the Prime Minister, a Union Cabinet Minister nominated by the Prime Minister, and the Leader of the Opposition in the Lok Sabha.",
   "The Chief Justice of India is a member of the Selection Committee under the Act.",
   "The Search Committee that prepares a panel of five names for the Selection Committee is headed by the Cabinet Secretary.",
   "The Chief Election Commissioner can be removed by the President on the recommendation of the Selection Committee."],
  C4, 0,
  "Only statement 1 is correct: the Act provides a Selection Committee of the Prime Minister (Chairperson), a Union Cabinet Minister nominated by the Prime Minister, and the Leader of the Opposition (or leader of the single largest opposition party) in the Lok Sabha. Statement 2 is incorrect: the Chief Justice figured only in the interim arrangement ordered in Anoop Baranwal (2023), which the Act replaced. Statement 3 is incorrect: the Search Committee is headed by the Union Minister of Law and Justice. Statement 4 is incorrect: the CEC can be removed only in the like manner and on the like grounds as a Supreme Court judge.",
  "elections-cec-appointment-act-2023", "Chief Election Commissioner and Other Election Commissioners (Appointment, Conditions of Service and Term of Office) Act, 2023; Anoop Baranwal v. Union of India (2023); Constitution of India, Art. 324(5).")

stmt(EL, "medium", "Consider the following statements regarding the Representation of the People Act, 1951:",
  ["A person convicted of an offence and sentenced to imprisonment for not less than two years is disqualified from the date of conviction and for a further six years after release.",
   "In Lily Thomas v. Union of India (2013), the Supreme Court struck down Section 8(4) of the Act, which had allowed sitting legislators to continue despite a conviction if they appealed within three months.",
   "A candidate cannot contest a general election to the Lok Sabha from more than two constituencies."],
  C3, 2,
  "All three statements are correct: Section 8(3) prescribes disqualification from the date of conviction and for six years after release; Lily Thomas (2013) struck down the Section 8(4) protection for sitting legislators, so disqualification is immediate on conviction; and Section 33(7), inserted in 1996, limits a candidate to two constituencies in a general election.",
  "elections-rpa-disqualification-two-seats", "Representation of the People Act, 1951 (Sections 8 and 33(7)); Lily Thomas v. Union of India (2013).")

# ================= JUDICIARY =================
pairs(JU, "easy", "Consider the following pairs of Articles of the Constitution and their subject matter:",
  ["Article 124", "Article 214", "Article 32", "Article 143"],
  ["Establishment and constitution of the Supreme Court", "High Courts for States", "Power of the High Courts to issue writs", "Power of the President to consult the Supreme Court"],
  2,
  "Pairs 1, 2 and 4 are correct. Pair 3 is incorrect: Art. 32 is the right to move the Supreme Court for the enforcement of Fundamental Rights; the High Courts' power to issue writs is in Art. 226, and it is wider because it extends to 'any other purpose' besides Fundamental Rights.",
  "judiciary-articles-124-214-226-143-pairs", f"Constitution of India, Arts. 32, 124, 143, 214 and 226; {LAX} -- chapters on the Supreme Court and High Courts.")

stmt(JU, "medium", "Consider the following statements regarding the Supreme Court of India:",
  ["The Constitution itself fixes the number of judges of the Supreme Court at 34, including the Chief Justice.",
   "A judge of the Supreme Court can be removed by the President on the advice of the Chief Justice of India.",
   "A retired judge of the Supreme Court can plead in any High Court, though not in the Supreme Court."],
  C3, 3,
  "None of the statements is correct. The present strength of 34 judges (including the CJI) is fixed by Parliament under the Supreme Court (Number of Judges) Act, as Art. 124(1) permits -- not by the Constitution itself. A judge can be removed only by an order of the President passed after an address by each House of Parliament, supported by a special majority, on the ground of proved misbehaviour or incapacity (Art. 124(4)). Under Art. 124(7), a retired Supreme Court judge cannot plead or act in any court or before any authority in India.",
  "judiciary-supreme-court-strength-removal", f"Constitution of India, Art. 124; Supreme Court (Number of Judges) Act, 1956 (as amended in 2019); {LAX} -- chapter on the Supreme Court.")

write_sql(os.path.dirname(os.path.abspath(__file__)), "polity_batch6_insert.sql")
