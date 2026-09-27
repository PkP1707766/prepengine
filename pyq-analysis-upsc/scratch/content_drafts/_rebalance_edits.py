# -*- coding: utf-8 -*-
"""One-off: flip one statement in 7 already-inserted Polity rows so no answer dominates its ladder
(C3 'Only two' 13/27, C4 'Only three' 10/21, T2 '1 only' 6/11 before this). Edits the batch scripts,
which stay the source of truth; the DB rows are then updated from the regenerated records."""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def edit(path, old, new):
    s = open(path, encoding="utf-8").read()
    assert s.count(old) == 1, (path, old[:70], s.count(old))
    open(path, "w", encoding="utf-8").write(s.replace(old, new))

b3 = "polity_batch3_governance_federalism.py"
# Governance / CBI (T2): 1 only -> Both 1 and 2
edit(b3, '''   "The Director of the CBI is appointed on the recommendation of a committee chaired by the Central Vigilance Commissioner."],
  T2, 0,
  "Only statement 1 is correct: the CBI's legal basis for investigation is the Delhi Special Police Establishment Act, 1946. Statement 2 describes the position before 2014: the Lokpal and Lokayuktas Act, 2013 amended the DSPE Act so that the Director is now appointed on the recommendation of a committee of the Prime Minister (Chairperson), the Leader of the Opposition or leader of the single largest opposition party in the Lok Sabha, and the Chief Justice of India or a Supreme Court judge nominated by the CJI. The CVC-chaired committee is a trap for older notes.",''',
'''   "The Director of the CBI is appointed on the recommendation of a committee chaired by the Prime Minister."],
  T2, 2,
  "Both statements are correct. The CBI's legal basis for investigation is the Delhi Special Police Establishment Act, 1946. Since the Lokpal and Lokayuktas Act, 2013 amended the DSPE Act, the Director is appointed on the recommendation of a committee of the Prime Minister (Chairperson), the Leader of the Opposition or leader of the single largest opposition party in the Lok Sabha, and the Chief Justice of India or a Supreme Court judge nominated by the CJI. Readers relying on older notes may wrongly reject statement 2: before 2014 the committee was chaired by the Central Vigilance Commissioner.",''')

# Federalism / water disputes (C3): Only two -> All three
edit(b3, '''   "Water disputes tribunals under the Inter-State River Water Disputes Act, 1956 are constituted by the Supreme Court.",
   "The decision of a water disputes tribunal under the Act has the same force as an order or decree of the Supreme Court."],
  C3, 1,
  "Statements 1 and 3 are correct: Art. 262(2) allows Parliament to exclude the jurisdiction of all courts, and Section 6(2) of the Inter-State River Water Disputes Act, 1956 (inserted in 2002) gives a tribunal's decision the same force as an order or decree of the Supreme Court. Statement 2 is incorrect: the tribunals are constituted by the Central Government, when negotiations between the States concerned fail.",''',
'''   "Water disputes tribunals under the Inter-State River Water Disputes Act, 1956 are constituted by the Central Government.",
   "The decision of a water disputes tribunal under the Act has the same force as an order or decree of the Supreme Court."],
  C3, 2,
  "All three statements are correct. Art. 262(2) allows Parliament to exclude the jurisdiction of all courts, including the Supreme Court, over such disputes; under the Inter-State River Water Disputes Act, 1956 the Central Government constitutes a tribunal when a dispute cannot be settled by negotiation; and Section 6(2) of the Act (inserted in 2002) gives a tribunal's decision the same force as an order or decree of the Supreme Court. The tempting error is to assume that the Supreme Court sets up the tribunals.",''')

b4 = "polity_batch4_framework_parliament.py"
# Constitutional Framework / CAA (C3): Only two -> Only one
edit(b4, '''   "It reduced the period of residence required for naturalisation of such persons from eleven years to five years."],
  C3, 1,
  "Statements 1 and 3 are correct: the Act covers these six communities from the three countries and relaxes the naturalisation residence requirement from eleven years to five years for them. Statement 2 changes the cut-off date: the Act applies to those who entered India on or before 31 December 2014.''',
'''   "It reduced the period of residence required for naturalisation of such persons from eleven years to seven years."],
  C3, 0,
  "Only statement 1 is correct: the Act covers these six communities from the three countries. Statement 2 changes the cut-off date: the Act applies to those who entered India on or before 31 December 2014. Statement 3 changes the number: the naturalisation residence requirement for them was reduced from eleven years to five years, not seven.''')

# Parliament / DRSCs (C4): Only three -> Only two
edit(b4, '''   "A minister is not eligible to be nominated as a member of any DRSC.",
   "The recommendations of the DRSCs on the demands for grants are binding on the Government."],
  C4, 2,
  "Statements 1, 2 and 3 are correct: the system set up in 1993 was expanded in 2004 to 24 committees (16 serviced by the Lok Sabha and 8 by the Rajya Sabha), each with 31 members (21 + 10), and ministers cannot be members. Statement 4 is incorrect: DRSC reports are advisory and do not bind the Government; they also do not consider the day-to-day administration of ministries.",''',
'''   "The Chairperson of every DRSC is appointed by the Speaker of the Lok Sabha.",
   "The recommendations of the DRSCs on the demands for grants are binding on the Government."],
  C4, 1,
  "Statements 1 and 2 are correct: the system set up in 1993 was expanded in 2004 to 24 committees (16 serviced by the Lok Sabha and 8 by the Rajya Sabha), each with 31 members (21 + 10); ministers cannot be members. Statement 3 is incorrect: the Speaker appoints the Chairpersons of the 16 Lok Sabha committees, but the Chairpersons of the 8 Rajya Sabha committees are appointed by the Chairman of the Rajya Sabha. Statement 4 is incorrect: DRSC reports are advisory and do not bind the Government.",''')

b5 = "polity_batch5_statutes_executive.py"
# Statutory-Laws / Public Examinations Act (C3): Only two -> Only one
edit(b5, '''  ["All offences under the Act are cognizable, non-bailable and non-compoundable.",
   "It covers public examinations conducted by bodies such as the Union Public Service Commission, the Staff Selection Commission and the National Testing Agency.",
   "It applies directly to the recruitment examinations conducted by the State Public Service Commissions."],
  C3, 1,
  "Statements 1 and 2 are correct: every offence under the Act is cognizable, non-bailable and non-compoundable, and it applies to the public examination authorities listed in its Schedule, including UPSC, SSC, the Railway Recruitment Boards, IBPS and NTA, as well as central ministries and departments. Statement 3 is incorrect:''',
'''  ["Offences under the Act are bailable and can be compounded with the consent of the examination authority.",
   "It covers public examinations conducted by bodies such as the Union Public Service Commission, the Staff Selection Commission and the National Testing Agency.",
   "It applies directly to the recruitment examinations conducted by the State Public Service Commissions."],
  C3, 0,
  "Only statement 2 is correct: the Act applies to the public examination authorities listed in its Schedule, including UPSC, SSC, the Railway Recruitment Boards, IBPS and NTA, as well as central ministries and departments. Statement 1 is incorrect: every offence under the Act is cognizable, non-bailable and non-compoundable. Statement 3 is incorrect:''')

# Executive / Prime Minister (T2): 1 only -> Neither 1 nor 2
edit(b5, '''  ["The Constitution does not contain any specific procedure for the selection and appointment of the Prime Minister.",
   "A person must be a member of the Lok Sabha at the time of appointment as Prime Minister."],
  T2, 0,
  "Only statement 1 is correct: Art. 75 merely says the Prime Minister shall be appointed by the President; by convention the President appoints the leader of the majority party or coalition in the Lok Sabha. Statement 2 is incorrect:''',
'''  ["The Constitution lays down a specific procedure for the selection and appointment of the Prime Minister.",
   "A person must be a member of the Lok Sabha at the time of appointment as Prime Minister."],
  T2, 3,
  "Neither statement is correct. Statement 1 is incorrect: Art. 75 merely says the Prime Minister shall be appointed by the President and lays down no procedure for the selection; by convention the President appoints the leader of the majority party or coalition in the Lok Sabha. Statement 2 is incorrect:''')

# Executive / Vice-President (C4): Only three -> Only two
edit(b5, '''   "Unlike in the Presidential election, the nominated members of Parliament also vote in the election of the Vice-President.",''',
'''   "As in the Presidential election, the elected members of the State Legislative Assemblies also vote in the election of the Vice-President.",''')
edit(b5, '''  C4, 2,
  "Statements 1, 2 and 3 are correct: the electoral college under Art. 66 comprises all members, elected and nominated, of both Houses (State Legislative Assemblies have no role), and under Art. 67(b) the Vice-President is removed by a Rajya Sabha resolution passed by a majority of all its then members and agreed to by the Lok Sabha -- no impeachment is needed. Statement 4 is incorrect:''',
'''  C4, 1,
  "Statements 1 and 3 are correct: the electoral college under Art. 66 comprises all members, elected and nominated, of both Houses of Parliament, and under Art. 67(b) the Vice-President is removed by a Rajya Sabha resolution passed by a majority of all its then members and agreed to by the Lok Sabha -- no impeachment is needed. Statement 2 is incorrect: unlike the Presidential electoral college, the Vice-Presidential one includes no members of the State Legislative Assemblies. Statement 4 is incorrect:''')
print("7 row edits applied")
