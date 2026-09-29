# -*- coding: utf-8 -*-
"""Level 2 · Test 2 (Polity 2: Parliament & Executive) -- Parliament & State Legislature, 48 new
bilingual rows against the live gap report: medium statement 18, hard statement 10, medium MCQ 4,
medium Statement-I/II 4, hard MCQ 3, medium pairs 3, hard Statement-I/II(/III) 2, easy statement 1,
hard pairs 1, easy MCQ 1, easy Statement-I/II 1. The 20 existing rows are not repeated: no new row
says who presides over a joint sitting or how often one has been held, what the Speaker's Money
Bill certificate settles, who chairs or sits on the PAC, Estimates, COPU, Business Advisory or
department-related committees, which cut motions exist, what Article 169 requires, what the
quorum or the gap between sessions is, which privileges exist, what Articles 105/110/112/123
contain, or that the Rajya Sabha is not dissolved -- and none states anything that answers them."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Polity"
PL = "Parliament & State Legislature"
COI = "Constitution of India"
NC = "NCERT Class XI, Political Science -- Indian Constitution at Work"
LSR = "Rules of Procedure and Conduct of Business in Lok Sabha"
SC = "Supreme Court of India"
PRS = "Lok Sabha Secretariat -- Practice and Procedure of Parliament"

# ---------------------------------------------------------------- medium statements (18)
S(PL, "medium", "Consider the following statements about the Rajya Sabha:",
  "राज्यसभा के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Its maximum strength fixed by the Constitution is 250.",
   "The President nominates twelve members from persons with special knowledge of literature, science, art, social service and the co-operative movement.",
   "Some of its seats are reserved for the Scheduled Castes and Scheduled Tribes."],
  ["संविधान द्वारा निर्धारित इसकी अधिकतम सदस्य-संख्या 250 है।",
   "राष्ट्रपति साहित्य, विज्ञान, कला, समाज सेवा और सहकारी आंदोलन का विशेष ज्ञान रखने वाले व्यक्तियों में से बारह सदस्य मनोनीत करते हैं।",
   "इसकी कुछ सीटें अनुसूचित जातियों और अनुसूचित जनजातियों के लिए आरक्षित हैं।"],
  C3, 0,
  "Only statement 1 is correct: Article 80 provides for 238 representatives of the States and Union Territories and 12 nominated members. "
  "Statement 2 slips in one field: Article 80(3) lists literature, science, art and social service; the co-operative movement appears only in Article 171(5), for nominations to a State Legislative Council. "
  "Statement 3 is wrong: Articles 330 and 332 reserve seats for the Scheduled Castes and Scheduled Tribes only in the Lok Sabha and the State Assemblies; members of the Rajya Sabha are elected by the Assemblies by proportional representation, which leaves no room for reserved seats.",
  "केवल कथन 1 सही है: अनुच्छेद 80 राज्यों और केंद्रशासित प्रदेशों के 238 प्रतिनिधियों और 12 मनोनीत सदस्यों का प्रावधान करता है। "
  "कथन 2 में एक क्षेत्र चुपके से जोड़ा गया है: अनुच्छेद 80(3) साहित्य, विज्ञान, कला और समाज सेवा गिनाता है; सहकारी आंदोलन केवल अनुच्छेद 171(5) में, राज्य विधान परिषद में मनोनयन के लिए, आता है। "
  "कथन 3 गलत है: अनुच्छेद 330 और 332 अनुसूचित जातियों और अनुसूचित जनजातियों के लिए सीटें केवल लोकसभा और राज्य विधानसभाओं में आरक्षित करते हैं; राज्यसभा के सदस्य विधानसभाओं द्वारा आनुपातिक प्रतिनिधित्व से चुने जाते हैं, जिसमें आरक्षित सीटों की गुंजाइश नहीं रहती।",
  f"{COI}, Articles 80, 171(5), 330 and 332.",
  "parl-rajya-sabha-strength-nomination")

S(PL, "medium", "Consider the following statements about Financial Bills:",
  "वित्त विधेयकों (Financial Bills) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["A Financial Bill under Article 117(1) can be introduced only in the Lok Sabha and only on the recommendation of the President.",
   "A Financial Bill under Article 117(3), which involves expenditure from the Consolidated Fund of India, can be introduced only in the Lok Sabha.",
   "The Rajya Sabha can reject a Financial Bill under Article 117(1)."],
  ["अनुच्छेद 117(1) के तहत वित्त विधेयक केवल लोकसभा में और केवल राष्ट्रपति की सिफ़ारिश पर प्रस्तुत किया जा सकता है।",
   "अनुच्छेद 117(3) के तहत वित्त विधेयक, जिसमें भारत की संचित निधि से व्यय शामिल है, केवल लोकसभा में प्रस्तुत किया जा सकता है।",
   "राज्यसभा अनुच्छेद 117(1) के तहत वित्त विधेयक को अस्वीकार कर सकती है।"],
  C3, 1,
  "Statements 1 and 3 are correct. A Bill under Article 117(1) contains some Money Bill matters along with others, so it shares the Money Bill's two entry conditions; once introduced, however, it is treated like an ordinary Bill -- the Rajya Sabha can amend or reject it, and a deadlock can go to a joint sitting. "
  "Statement 2 is wrong: a Bill under Article 117(3) can be introduced in either House; the only special condition is that no House can pass it unless the President has recommended its consideration.",
  "कथन 1 और 3 सही हैं। अनुच्छेद 117(1) के विधेयक में धन विधेयक के कुछ विषयों के साथ दूसरे विषय भी होते हैं, इसलिए उस पर धन विधेयक की दोनों प्रवेश-शर्तें लागू होती हैं; पर प्रस्तुत होने के बाद उसे सामान्य विधेयक की तरह माना जाता है: राज्यसभा उसमें संशोधन कर सकती है या उसे अस्वीकार कर सकती है, और गतिरोध संयुक्त बैठक तक जा सकता है। "
  "कथन 2 गलत है: अनुच्छेद 117(3) का विधेयक किसी भी सदन में प्रस्तुत किया जा सकता है; एकमात्र विशेष शर्त यह है कि कोई भी सदन उसे तब तक पारित नहीं कर सकता जब तक राष्ट्रपति ने उस पर विचार की सिफ़ारिश न की हो।",
  f"{COI}, Articles 108 and 117; {PRS}.",
  "parl-financial-bills-117")

S(PL, "medium", "Consider the following statements about expenditure charged on the Consolidated Fund of India:",
  "भारत की संचित निधि पर भारित व्यय के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is not submitted to the vote of Parliament, but it can be discussed in Parliament.",
   "The salaries, allowances and pensions of the judges of the Supreme Court are charged on it.",
   "The salary of the Comptroller and Auditor-General of India is charged on it."],
  ["इसे संसद के मतदान के लिए नहीं रखा जाता, पर संसद में इस पर चर्चा हो सकती है।",
   "उच्चतम न्यायालय के न्यायाधीशों के वेतन, भत्ते और पेंशन इस पर भारित हैं।",
   "भारत के नियंत्रक-महालेखापरीक्षक का वेतन इस पर भारित है।"],
  C3, 2,
  "All three statements are correct. Article 113(1) keeps charged expenditure out of the vote but not out of discussion, which is the point most students miss. Article 112(3) lists the charged items -- among them the emoluments of the President, the presiding officers of both Houses, the judges of the Supreme Court and the CAG -- so that offices that must stay independent of the government of the day are not at the mercy of an annual vote.",
  "तीनों कथन सही हैं। अनुच्छेद 113(1) भारित व्यय को मतदान से बाहर रखता है, चर्चा से नहीं; अधिकांश विद्यार्थी यही बिंदु चूकते हैं। अनुच्छेद 112(3) भारित मदें गिनाता है, जिनमें राष्ट्रपति, दोनों सदनों के पीठासीन अधिकारियों, उच्चतम न्यायालय के न्यायाधीशों और CAG की उपलब्धियाँ हैं, ताकि जिन पदों को तत्कालीन सरकार से स्वतंत्र रहना चाहिए, वे वार्षिक मतदान की दया पर न रहें।",
  f"{COI}, Articles 112(3), 113 and 148(3).",
  "parl-charged-expenditure")

S(PL, "medium", "Consider the following statements about the Appropriation Bill:",
  "विनियोग विधेयक के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["No money can be withdrawn from the Consolidated Fund of India except under an appropriation made by law.",
   "An amendment to the Appropriation Bill can be proposed in Parliament to vary the amount of any expenditure charged on the Consolidated Fund.",
   "The Appropriation Bill is introduced before the Lok Sabha votes on the demands for grants."],
  ["भारत की संचित निधि से कोई धन विधि द्वारा किए गए विनियोग के अधीन ही निकाला जा सकता है, अन्यथा नहीं।",
   "संचित निधि पर भारित किसी व्यय की राशि बदलने के लिए संसद में विनियोग विधेयक में संशोधन प्रस्तावित किया जा सकता है।",
   "विनियोग विधेयक लोकसभा द्वारा अनुदान की माँगों पर मतदान से पहले प्रस्तुत किया जाता है।"],
  C3, 0,
  "Only statement 1 is correct: Article 114(3) is the legal basis of parliamentary control over spending. "
  "Statement 3 reverses the order: Article 114(1) provides for the Bill to be introduced 'as soon as may be after the grants ... have been made by the House of the People', since it must cover those grants together with the charged expenditure. "
  "Statement 2 is wrong: Article 114(2) bars any amendment that would vary the amount or alter the destination of a grant, or vary the amount of charged expenditure. The debate on the demands is where the House can cut; the Appropriation Bill only gives legal form to what has been voted.",
  "केवल कथन 1 सही है: अनुच्छेद 114(3) व्यय पर संसदीय नियंत्रण का विधिक आधार है। "
  "कथन 3 क्रम उलट देता है: अनुच्छेद 114(1) विधेयक को 'लोकसभा द्वारा अनुदान दिए जाने के बाद यथाशीघ्र' प्रस्तुत करने का प्रावधान करता है, क्योंकि उसमें वे अनुदान और भारित व्यय, दोनों शामिल होने चाहिए। "
  "कथन 2 गलत है: अनुच्छेद 114(2) ऐसे किसी संशोधन को रोकता है जो किसी अनुदान की राशि बदले या उसका लक्ष्य बदले, या भारित व्यय की राशि बदले। कटौती की गुंजाइश माँगों पर बहस में है; विनियोग विधेयक केवल मतदान किए गए को विधिक रूप देता है।",
  f"{COI}, Article 114.",
  "parl-appropriation-bill")

S(PL, "medium", "Consider the following statements about the funds of the Government of India:",
  "भारत सरकार की निधियों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Contingency Fund of India is placed at the disposal of the Finance Minister.",
   "Payments out of the Public Account of India require an appropriation by Parliament.",
   "The Contingency Fund of India is held by the Comptroller and Auditor-General on behalf of the President."],
  ["भारत की आकस्मिकता निधि वित्त मंत्री के अधिकार में रखी जाती है।",
   "भारत के लोक लेखे से भुगतान के लिए संसद द्वारा विनियोग आवश्यक है।",
   "भारत की आकस्मिकता निधि राष्ट्रपति की ओर से नियंत्रक-महालेखापरीक्षक के पास रहती है।"],
  C3, 3,
  "None of the statements is correct. Statement 1 is wrong: under Article 267 and the Contingency Fund of India Act, 1950, the Fund is placed at the disposal of the President, who can make advances from it for unforeseen expenditure pending authorisation by Parliament. "
  "Statement 2 is wrong: the Public Account holds money the government receives as a banker or trustee -- provident funds, small savings and deposits -- so payments from it are made by executive action without appropriation. "
  "Statement 3 is wrong: the Fund is held by the Finance Secretary (Department of Economic Affairs) on the President's behalf; the CAG audits accounts but holds no fund.",
  "कोई भी कथन सही नहीं है। कथन 1 गलत है: अनुच्छेद 267 और भारत की आकस्मिकता निधि अधिनियम, 1950 के तहत निधि राष्ट्रपति के अधिकार में रखी जाती है, जो संसद की स्वीकृति मिलने तक अप्रत्याशित व्यय के लिए इससे अग्रिम दे सकते हैं। "
  "कथन 2 गलत है: लोक लेखे में वह धन रहता है जो सरकार बैंकर या न्यासी के रूप में प्राप्त करती है, जैसे भविष्य निधि, लघु बचत और जमा; इसलिए इससे भुगतान विनियोग के बिना कार्यकारी कार्रवाई से होता है। "
  "कथन 3 गलत है: निधि राष्ट्रपति की ओर से वित्त सचिव (आर्थिक कार्य विभाग) के पास रहती है; CAG लेखों की लेखापरीक्षा करता है, कोई निधि नहीं रखता।",
  f"{COI}, Articles 266 and 267; Contingency Fund of India Act, 1950.",
  "parl-contingency-fund-public-account")

S(PL, "medium", "Consider the following statements about the Rajya Sabha:",
  "राज्यसभा के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["A resolution of the Rajya Sabha is required before Parliament can create a new All-India Service.",
   "The Rajya Sabha can pass a motion of no-confidence against the Council of Ministers."],
  ["संसद द्वारा कोई नई अखिल भारतीय सेवा बनाने से पहले राज्यसभा का संकल्प आवश्यक है।",
   "राज्यसभा मंत्रिपरिषद के विरुद्ध अविश्वास प्रस्ताव पारित कर सकती है।"],
  T2, 0,
  "Only statement 1 is correct: Article 312 requires a Rajya Sabha resolution, supported by two-thirds of the members present and voting, declaring such a service necessary in the national interest -- a power given to the House of the States because the service will work in the States. "
  "Statement 2 is wrong: the Council of Ministers is collectively responsible to the Lok Sabha alone (Article 75(3)), so only the Lok Sabha can remove it by a vote of no-confidence.",
  "केवल कथन 1 सही है: अनुच्छेद 312 राज्यसभा के ऐसे संकल्प की अपेक्षा करता है, जो उपस्थित और मत देने वाले सदस्यों के दो-तिहाई से समर्थित हो और ऐसी सेवा को राष्ट्रीय हित में आवश्यक घोषित करे; यह शक्ति राज्यों के सदन को इसलिए दी गई है कि सेवा राज्यों में काम करेगी। "
  "कथन 2 गलत है: मंत्रिपरिषद सामूहिक रूप से केवल लोकसभा के प्रति उत्तरदायी है (अनुच्छेद 75(3)), इसलिए केवल लोकसभा ही अविश्वास मत से उसे हटा सकती है।",
  f"{COI}, Articles 75(3) and 312.",
  "parl-rajya-sabha-312-no-confidence")

S(PL, "medium", "Consider the following statements about the Speaker of the Lok Sabha:",
  "लोकसभा के अध्यक्ष के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Speaker does not vacate office when the Lok Sabha is dissolved, but continues until immediately before the first meeting of the new House.",
   "While a resolution for the Speaker's removal is under consideration, the Speaker cannot vote at all.",
   "In the absence of a quorum, the Speaker must adjourn the House or suspend the sitting until there is a quorum."],
  ["लोकसभा के विघटन पर अध्यक्ष पद रिक्त नहीं करता, बल्कि नए सदन की पहली बैठक के ठीक पहले तक पद पर बना रहता है।",
   "जब अध्यक्ष को हटाने का संकल्प विचाराधीन हो, तब अध्यक्ष बिल्कुल भी मत नहीं दे सकता।",
   "गणपूर्ति (कोरम) के अभाव में अध्यक्ष को सदन स्थगित करना होता है या गणपूर्ति होने तक बैठक निलंबित करनी होती है।"],
  C3, 1,
  "Statements 1 and 3 are correct (Articles 94 and 100(3)); the Speaker's continuity after dissolution ensures that the Lok Sabha Secretariat and its committees are never without a head. "
  "Statement 2 is wrong: under Article 96, while a removal resolution is being considered the Speaker cannot preside, but can speak and take part in the proceedings and can vote in the first instance -- only the casting vote in a tie is lost.",
  "कथन 1 और 3 सही हैं (अनुच्छेद 94 और 100(3)); विघटन के बाद अध्यक्ष की निरंतरता यह सुनिश्चित करती है कि लोकसभा सचिवालय और उसकी समितियाँ कभी प्रमुख के बिना न रहें। "
  "कथन 2 गलत है: अनुच्छेद 96 के तहत हटाने का संकल्प विचाराधीन होने पर अध्यक्ष अध्यक्षता नहीं कर सकता, पर बोल सकता है, कार्यवाही में भाग ले सकता है और पहली बार में मत दे सकता है; केवल बराबरी की स्थिति वाला निर्णायक मत नहीं रहता।",
  f"{COI}, Articles 94, 96 and 100(3).",
  "parl-speaker-continuity-removal-quorum")

S(PL, "medium", "Consider the following statements about the sessions of Parliament:",
  "संसद के सत्रों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Adjournment sine die is done by the presiding officer of the House.",
   "Prorogation of a House does not affect the Bills pending before it.",
   "Prorogation of a House is done by its presiding officer."],
  ["अनिश्चित काल के लिए स्थगन (adjournment sine die) सदन के पीठासीन अधिकारी द्वारा किया जाता है।",
   "किसी सदन का सत्रावसान (prorogation) उसके सामने लंबित विधेयकों को प्रभावित नहीं करता।",
   "किसी सदन का सत्रावसान उसका पीठासीन अधिकारी करता है।"],
  C3, 1,
  "Statements 1 and 2 are correct: adjournment and adjournment sine die, which end a sitting or a session's sittings, are the presiding officer's acts, and pending Bills survive a prorogation -- only dissolution of the Lok Sabha makes Bills lapse, while pending notices other than those for introducing Bills lapse on prorogation. "
  "Statement 3 is wrong: prorogation, which ends the session itself, is done by the President under Article 85(2), usually a few days after the House is adjourned sine die.",
  "कथन 1 और 2 सही हैं: स्थगन और अनिश्चित काल के लिए स्थगन, जो किसी बैठक या सत्र की बैठकों को समाप्त करते हैं, पीठासीन अधिकारी के कार्य हैं, और लंबित विधेयक सत्रावसान के बाद भी बने रहते हैं; विधेयक केवल लोकसभा के विघटन पर व्यपगत होते हैं, जबकि सत्रावसान पर विधेयक प्रस्तुत करने की सूचनाओं को छोड़कर बाकी लंबित सूचनाएँ व्यपगत हो जाती हैं। "
  "कथन 3 गलत है: सत्रावसान, जो स्वयं सत्र को समाप्त करता है, अनुच्छेद 85(2) के तहत राष्ट्रपति करते हैं, प्रायः सदन के अनिश्चित काल के लिए स्थगित होने के कुछ दिन बाद।",
  f"{COI}, Article 85; {PRS}.",
  "parl-adjournment-prorogation")

S(PL, "medium", "Consider the following statements about parliamentary committees:",
  "संसदीय समितियों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Committee on Petitions exists only in the Lok Sabha.",
   "A Joint Parliamentary Committee set up to examine a particular Bill or issue is an ad hoc committee.",
   "The Lok Sabha constituted an Ethics Committee before the Rajya Sabha did."],
  ["याचिका समिति केवल लोकसभा में होती है।",
   "किसी विशेष विधेयक या मुद्दे की जाँच के लिए बनी संयुक्त संसदीय समिति एक तदर्थ (ad hoc) समिति होती है।",
   "लोकसभा ने राज्यसभा से पहले आचार समिति (Ethics Committee) बनाई।"],
  C3, 0,
  "Only statement 2 is correct: ad hoc committees are formed for a specific purpose and end when their report is made, unlike standing committees that are constituted every year or periodically. "
  "Statement 1 is wrong: each House has its own Committee on Petitions, which examines petitions on Bills and matters of public importance. "
  "Statement 3 reverses the order: the Rajya Sabha set up its Ethics Committee in 1997; the Lok Sabha formed one in 2000 and made it permanent only in 2015.",
  "केवल कथन 2 सही है: तदर्थ समितियाँ किसी विशेष उद्देश्य के लिए बनती हैं और रिपोर्ट देने पर समाप्त हो जाती हैं, स्थायी समितियों के विपरीत जो हर वर्ष या समय-समय पर गठित होती हैं। "
  "कथन 1 गलत है: हर सदन की अपनी याचिका समिति है, जो विधेयकों और सार्वजनिक महत्त्व के विषयों पर याचिकाओं की जाँच करती है। "
  "कथन 3 क्रम उलट देता है: राज्यसभा ने 1997 में अपनी आचार समिति बनाई; लोकसभा ने 2000 में समिति बनाई और उसे स्थायी केवल 2015 में किया।",
  f"{PRS}; Rajya Sabha Secretariat -- Committees of Rajya Sabha.",
  "parl-committees-petitions-jpc-ethics")

S(PL, "medium", "Consider the following statements about the State Legislative Council:",
  "राज्य विधान परिषद के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Its total membership cannot exceed one-half of the total membership of the Legislative Assembly of the State.",
   "Its total membership cannot be less than 60.",
   "Its Chairman is nominated by the Governor."],
  ["इसकी कुल सदस्य-संख्या राज्य की विधानसभा की कुल सदस्य-संख्या के आधे से अधिक नहीं हो सकती।",
   "इसकी कुल सदस्य-संख्या 60 से कम नहीं हो सकती।",
   "इसके सभापति को राज्यपाल मनोनीत करते हैं।"],
  C3, 3,
  "None of the statements is correct. Under Article 171(1) a Council cannot exceed one-third of the Assembly's strength and cannot have fewer than 40 members; 60 is the minimum for an Assembly under Article 170, which is the number the statement borrows. "
  "Under Article 182, the Council chooses its own Chairman and Deputy Chairman from among its members.",
  "कोई भी कथन सही नहीं है। अनुच्छेद 171(1) के तहत परिषद विधानसभा की सदस्य-संख्या के एक-तिहाई से अधिक नहीं हो सकती और उसमें 40 से कम सदस्य नहीं हो सकते; 60 अनुच्छेद 170 के तहत विधानसभा के लिए न्यूनतम संख्या है, जिसे कथन उधार लेता है। "
  "अनुच्छेद 182 के तहत परिषद अपने सदस्यों में से अपना सभापति और उपसभापति स्वयं चुनती है।",
  f"{COI}, Articles 170, 171 and 182.",
  "parl-legislative-council-size-chairman")

S(PL, "medium", "Consider the following statements about the panel of chairpersons of the Lok Sabha:",
  "लोकसभा के सभापति-तालिका (panel of chairpersons) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Its members are nominated by the Speaker from among the members of the House.",
   "A member of the panel presides over the House when both the Speaker and the Deputy Speaker are absent.",
   "A member of the panel presides over the House when the offices of both the Speaker and the Deputy Speaker are vacant."],
  ["इसके सदस्यों को अध्यक्ष सदन के सदस्यों में से मनोनीत करता है।",
   "जब अध्यक्ष और उपाध्यक्ष, दोनों अनुपस्थित हों, तब तालिका का कोई सदस्य सदन की अध्यक्षता करता है।",
   "जब अध्यक्ष और उपाध्यक्ष, दोनों के पद रिक्त हों, तब तालिका का कोई सदस्य सदन की अध्यक्षता करता है।"],
  C3, 1,
  "Statements 1 and 2 are correct: the Speaker nominates up to ten members to the panel, and one of them presides in the absence of both presiding officers. "
  "Statement 3 turns on the difference between 'absent' and 'vacant': when both offices are vacant, the Speaker's duties are performed by a member whom the President appoints under Article 95(1), not by a panel member.",
  "कथन 1 और 2 सही हैं: अध्यक्ष तालिका में अधिकतम दस सदस्य मनोनीत करता है, और दोनों पीठासीन अधिकारियों की अनुपस्थिति में उनमें से एक अध्यक्षता करता है। "
  "कथन 3 'अनुपस्थित' और 'रिक्त' के अंतर पर टिका है: जब दोनों पद रिक्त हों, तब अध्यक्ष के कर्तव्य अनुच्छेद 95(1) के तहत राष्ट्रपति द्वारा नियुक्त सदस्य करता है, तालिका का सदस्य नहीं।",
  f"{COI}, Article 95; {LSR}, Rule 9.",
  "parl-panel-of-chairpersons")

S(PL, "medium", "Consider the following statements about elections to the Rajya Sabha:",
  "राज्यसभा के चुनावों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Since 2003, a candidate need not be an elector in the State from which he or she is elected.",
   "Voting in these elections is by open ballot.",
   "In Kuldip Nayar (2006), the Supreme Court struck down the removal of the domicile requirement."],
  ["2003 से किसी उम्मीदवार का उस राज्य का निर्वाचक होना ज़रूरी नहीं है जिससे वह चुना जाता है।",
   "इन चुनावों में मतदान खुले मतपत्र से होता है।",
   "कुलदीप नैयर (2006) में उच्चतम न्यायालय ने निवास (domicile) की शर्त हटाए जाने को रद्द कर दिया।"],
  C3, 1,
  "Statements 1 and 2 are correct. The Representation of the People (Amendment) Act, 2003 let a candidate be an elector in any parliamentary constituency in India and introduced open ballot, under which a party's MLAs show their ballots to the party's authorised agent, to curb cross-voting and money power. "
  "Statement 3 is wrong: in Kuldip Nayar a Constitution Bench upheld both changes, holding that residence is not an essential feature of federalism or of the Rajya Sabha's character.",
  "कथन 1 और 2 सही हैं। लोक प्रतिनिधित्व (संशोधन) अधिनियम, 2003 ने उम्मीदवार को भारत के किसी भी संसदीय निर्वाचन क्षेत्र का निर्वाचक होने की छूट दी और खुला मतदान शुरू किया, जिसमें किसी दल के विधायक अपना मतपत्र दल के अधिकृत एजेंट को दिखाते हैं, ताकि क्रॉस-वोटिंग और धनबल पर रोक लगे। "
  "कथन 3 गलत है: कुलदीप नैयर में संविधान पीठ ने दोनों परिवर्तनों को सही ठहराया, यह मानते हुए कि निवास संघवाद या राज्यसभा के स्वरूप की अनिवार्य विशेषता नहीं है।",
  f"Representation of the People Act, 1951, sections 3 and 59 (as amended in 2003); {SC} -- Kuldip Nayar v. Union of India (2006).",
  "parl-rajya-sabha-elections-domicile-open-ballot")

S(PL, "medium", "Consider the following statements about the two Houses of Parliament:",
  "संसद के दोनों सदनों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["A minister can speak in, and take part in the proceedings of, the House of which he or she is not a member, but cannot vote there.",
   "The Rajya Sabha can discuss the Union Budget but cannot vote on the demands for grants.",
   "The Rajya Sabha has equal power with the Lok Sabha in the impeachment of the President."],
  ["मंत्री उस सदन में बोल सकता है और उसकी कार्यवाही में भाग ले सकता है जिसका वह सदस्य नहीं है, पर वहाँ मत नहीं दे सकता।",
   "राज्यसभा केंद्रीय बजट पर चर्चा कर सकती है, पर अनुदान की माँगों पर मतदान नहीं कर सकती।",
   "राष्ट्रपति पर महाभियोग में राज्यसभा को लोकसभा के बराबर शक्ति है।"],
  C3, 2,
  "All three statements are correct. Article 88 lets every minister and the Attorney General speak in either House, in a joint sitting and in any committee they are named to, with a vote only where they are members. Article 113 gives the power to vote on demands to the Lok Sabha alone. In impeachment under Article 61, either House can bring the charge and the other investigates it, so the two are equal.",
  "तीनों कथन सही हैं। अनुच्छेद 88 हर मंत्री और महान्यायवादी को किसी भी सदन में, संयुक्त बैठक में और जिस समिति में वे नामित हों उसमें बोलने देता है, पर मत केवल वहीं जहाँ वे सदस्य हैं। अनुच्छेद 113 माँगों पर मतदान की शक्ति केवल लोकसभा को देता है। अनुच्छेद 61 के तहत महाभियोग में कोई भी सदन आरोप ला सकता है और दूसरा उसकी जाँच करता है, इसलिए दोनों बराबर हैं।",
  f"{COI}, Articles 61, 88 and 113.",
  "parl-houses-art88-demands-impeachment")

S(PL, "medium", "Consider the following statements about the Lok Sabha:",
  "लोकसभा के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Its maximum strength under the Constitution is 550.",
   "Its members from the Union Territories are nominated by the President.",
   "Seats are reserved in it for the Scheduled Castes, the Scheduled Tribes and the Other Backward Classes."],
  ["संविधान के तहत इसकी अधिकतम सदस्य-संख्या 550 है।",
   "केंद्रशासित प्रदेशों से इसके सदस्य राष्ट्रपति द्वारा मनोनीत किए जाते हैं।",
   "इसमें अनुसूचित जातियों, अनुसूचित जनजातियों और अन्य पिछड़े वर्गों के लिए सीटें आरक्षित हैं।"],
  C3, 0,
  "Only statement 1 is correct: Article 81 allows up to 530 members from the States and 20 from the Union Territories. "
  "Statement 2 is wrong: under the Union Territories (Direct Election to the House of the People) Act, 1965, UT members are directly elected like all others. "
  "Statement 3 is wrong: Article 330 reserves Lok Sabha seats only for the Scheduled Castes and Scheduled Tribes; OBC reservation exists in local bodies and in jobs and education, not in Parliament.",
  "केवल कथन 1 सही है: अनुच्छेद 81 राज्यों से अधिकतम 530 और केंद्रशासित प्रदेशों से 20 सदस्यों की अनुमति देता है। "
  "कथन 2 गलत है: केंद्रशासित प्रदेश (लोकसभा के लिए प्रत्यक्ष निर्वाचन) अधिनियम, 1965 के तहत केंद्रशासित प्रदेशों के सदस्य भी बाकी सबकी तरह प्रत्यक्ष रूप से चुने जाते हैं। "
  "कथन 3 गलत है: अनुच्छेद 330 लोकसभा में केवल अनुसूचित जातियों और अनुसूचित जनजातियों के लिए सीटें आरक्षित करता है; OBC आरक्षण स्थानीय निकायों और नौकरियों तथा शिक्षा में है, संसद में नहीं।",
  f"{COI}, Articles 81 and 330; Union Territories (Direct Election to the House of the People) Act, 1965.",
  "parl-lok-sabha-strength-ut-reservation")

S(PL, "medium", "Consider the following statements about the State Legislative Assemblies:",
  "राज्य विधानसभाओं के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Constitution fixes the strength of an Assembly at not more than 500 and not less than 60 members.",
   "The Assemblies of Sikkim, Goa and Mizoram have fewer than 60 members.",
   "The Governor can nominate one member of the Anglo-Indian community to the Assembly."],
  ["संविधान विधानसभा की सदस्य-संख्या अधिकतम 500 और न्यूनतम 60 निर्धारित करता है।",
   "सिक्किम, गोवा और मिज़ोरम की विधानसभाओं में 60 से कम सदस्य हैं।",
   "राज्यपाल विधानसभा में आंग्ल-भारतीय समुदाय के एक सदस्य को मनोनीत कर सकते हैं।"],
  C3, 1,
  "Statements 1 and 2 are correct: Article 170 sets the range, and small States have been allowed smaller Assemblies -- Sikkim has 32, and Goa and Mizoram 40 each -- through special provisions and laws of Parliament. "
  "Statement 3 is wrong: the Governor's power under Article 333 to nominate an Anglo-Indian lapsed in January 2020, when the 104th Amendment did not extend it.",
  "कथन 1 और 2 सही हैं: अनुच्छेद 170 यह सीमा तय करता है, और छोटे राज्यों को विशेष प्रावधानों और संसद के कानूनों के ज़रिए छोटी विधानसभाओं की छूट दी गई है: सिक्किम में 32, और गोवा तथा मिज़ोरम में 40-40 सदस्य हैं। "
  "कथन 3 गलत है: अनुच्छेद 333 के तहत आंग्ल-भारतीय को मनोनीत करने की राज्यपाल की शक्ति जनवरी 2020 में समाप्त हो गई, जब 104वें संशोधन ने उसे आगे नहीं बढ़ाया।",
  f"{COI}, Articles 170, 333 and 371F; Constitution (One Hundred and Fourth Amendment) Act, 2019.",
  "parl-state-assembly-strength")

S(PL, "medium", "Consider the following statements about the conduct of business in Parliament:",
  "संसद में कार्य-संचालन के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The rules of procedure made by each House of Parliament come into force only after the President approves them.",
   "The rules of procedure for joint sittings are made by the President after consulting the Chairman of the Rajya Sabha and the Speaker of the Lok Sabha.",
   "Business in Parliament can be transacted only in English."],
  ["संसद के हर सदन द्वारा बनाए गए प्रक्रिया-नियम राष्ट्रपति के अनुमोदन के बाद ही लागू होते हैं।",
   "संयुक्त बैठकों की प्रक्रिया के नियम राष्ट्रपति राज्यसभा के सभापति और लोकसभा के अध्यक्ष से परामर्श करके बनाते हैं।",
   "संसद में कार्य केवल अंग्रेज़ी में किया जा सकता है।"],
  C3, 0,
  "Only statement 2 is correct (Article 118(3)). "
  "Statement 1 is wrong: under Article 118(1) each House makes its own rules and no approval of the President is needed -- an expression of each House's control over its own proceedings; the President's role is limited to the rules for joint sittings. "
  "Statement 3 is wrong: under Article 120, business is transacted in Hindi or English, and the presiding officer can permit a member who cannot express himself adequately in either to address the House in his mother tongue; members today speak in all the Eighth Schedule languages with simultaneous interpretation.",
  "केवल कथन 2 सही है (अनुच्छेद 118(3))। "
  "कथन 1 गलत है: अनुच्छेद 118(1) के तहत हर सदन अपने नियम स्वयं बनाता है और राष्ट्रपति के अनुमोदन की ज़रूरत नहीं होती; यह अपनी कार्यवाही पर हर सदन के नियंत्रण की अभिव्यक्ति है; राष्ट्रपति की भूमिका केवल संयुक्त बैठकों के नियमों तक है। "
  "कथन 3 गलत है: अनुच्छेद 120 के तहत कार्य हिंदी या अंग्रेज़ी में होता है, और पीठासीन अधिकारी किसी ऐसे सदस्य को, जो दोनों में से किसी में ठीक से अपनी बात न कह सके, अपनी मातृभाषा में सदन को संबोधित करने की अनुमति दे सकता है; आज सदस्य आठवीं अनुसूची की सभी भाषाओं में बोलते हैं और साथ-साथ अनुवाद होता है।",
  f"{COI}, Articles 118 and 120.",
  "parl-rules-language")

S(PL, "medium", "Consider the following statements about private members' Bills:",
  "निजी सदस्यों के विधेयकों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Notice of one month is required for introducing a private member's Bill.",
   "The drafting of a private member's Bill is the responsibility of the member concerned.",
   "No private member's Bill has been passed by both Houses of Parliament since 1970."],
  ["निजी सदस्य का विधेयक प्रस्तुत करने के लिए एक महीने की सूचना आवश्यक है।",
   "निजी सदस्य के विधेयक का प्रारूप तैयार करना संबंधित सदस्य की ज़िम्मेदारी है।",
   "1970 के बाद से संसद के दोनों सदनों द्वारा कोई भी निजी सदस्य का विधेयक पारित नहीं हुआ है।"],
  C3, 2,
  "All three statements are correct. A government Bill is drafted by the ministry with the Law Ministry's help and needs seven days' notice, while a private member's Bill needs a month and is drafted by the member. Only fourteen private members' Bills have ever become law, the last -- on the Supreme Court's appellate jurisdiction in criminal matters -- in 1970; since then some have passed one House, but none both.",
  "तीनों कथन सही हैं। सरकारी विधेयक का प्रारूप मंत्रालय विधि मंत्रालय की मदद से बनाता है और उसके लिए सात दिन की सूचना चाहिए, जबकि निजी सदस्य के विधेयक के लिए एक महीना चाहिए और उसका प्रारूप सदस्य स्वयं बनाता है। अब तक केवल चौदह निजी सदस्यों के विधेयक कानून बने हैं, अंतिम 1970 में, दांडिक मामलों में उच्चतम न्यायालय के अपीलीय क्षेत्राधिकार पर; तब से कुछ एक सदन में पारित हुए हैं, पर दोनों में कोई नहीं।",
  f"{LSR}, Rules 65-67; {PRS}.",
  "parl-private-members-bills")

S(PL, "medium", "Consider the following statements about the adjournment motion:",
  "स्थगन प्रस्ताव के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is regarded as an extraordinary device because it interrupts the normal business of the House.",
   "It involves an element of censure against the Government.",
   "It can be used to raise a matter that is pending before a court of law."],
  ["इसे असाधारण उपाय माना जाता है क्योंकि यह सदन के सामान्य कार्य को बाधित करता है।",
   "इसमें सरकार के विरुद्ध निंदा का तत्व होता है।",
   "इसके ज़रिए किसी ऐसे विषय को उठाया जा सकता है जो न्यायालय में लंबित है।"],
  C3, 1,
  "Statements 1 and 2 are correct: the motion sets aside the day's business to discuss a definite matter of urgent public importance, and because its adoption implies criticism of the Government, the Rajya Sabha does not use it. "
  "Statement 3 is wrong: the rules bar an adjournment motion on a matter under adjudication by a court, along with matters that are not recent, specific and of public importance, and questions of privilege.",
  "कथन 1 और 2 सही हैं: यह प्रस्ताव तात्कालिक सार्वजनिक महत्त्व के किसी निश्चित विषय पर चर्चा के लिए दिन का कार्य अलग रख देता है, और चूँकि इसका स्वीकृत होना सरकार की आलोचना का संकेत है, इसलिए राज्यसभा इसका उपयोग नहीं करती। "
  "कथन 3 गलत है: नियम न्यायालय में विचाराधीन विषय पर स्थगन प्रस्ताव को रोकते हैं, साथ ही ऐसे विषयों को जो हाल के, विशिष्ट और सार्वजनिक महत्त्व के न हों, और विशेषाधिकार के प्रश्नों को भी।",
  f"{LSR}, Rules 56-63.",
  "parl-adjournment-motion-features")

# ---------------------------------------------------------------- hard statements (10)
S(PL, "hard", "Consider the following statements about Money Bills:",
  "धन विधेयकों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Speaker's certificate that a Bill is a Money Bill is endorsed on it when it is presented to the President for assent.",
   "In the Aadhaar judgment (2018), the majority upheld the passing of the Aadhaar Act as a Money Bill.",
   "In Rojer Mathew (2019), a five-judge bench referred the question of the scope of Money Bills to a larger bench.",
   "If the Rajya Sabha does not return a Money Bill within fourteen days, the Bill is deemed to have been passed by both Houses."],
  ["अध्यक्ष का यह प्रमाणपत्र कि विधेयक धन विधेयक है, उस पर तब पृष्ठांकित किया जाता है जब वह अनुमति के लिए राष्ट्रपति के सामने रखा जाता है।",
   "आधार निर्णय (2018) में बहुमत ने आधार अधिनियम के धन विधेयक के रूप में पारित होने को सही ठहराया।",
   "रोजर मैथ्यू (2019) में पाँच न्यायाधीशों की पीठ ने धन विधेयकों के दायरे का प्रश्न बड़ी पीठ को भेजा।",
   "यदि राज्यसभा चौदह दिनों के भीतर धन विधेयक नहीं लौटाती, तो विधेयक दोनों सदनों द्वारा पारित माना जाता है।"],
  C4, 3,
  "All four statements are correct. Article 110(4) requires the certificate to be endorsed both when the Bill goes to the Rajya Sabha and when it goes to the President. Justice Chandrachud dissented in the Aadhaar case, calling the use of the Money Bill route a fraud on the Constitution, and Rojer Mathew, finding the majority's reasoning thin, sent the question to a larger bench. "
  "Statement 4 completes Article 109: the Rajya Sabha can only make recommendations, which the Lok Sabha may accept or reject, and if it does not return the Bill within fourteen days the Bill is deemed passed in the form the Lok Sabha passed it.",
  "चारों कथन सही हैं। अनुच्छेद 110(4) अपेक्षा करता है कि प्रमाणपत्र विधेयक के राज्यसभा जाने पर भी और राष्ट्रपति के पास जाने पर भी पृष्ठांकित हो। आधार मामले में न्यायमूर्ति चंद्रचूड़ ने असहमति जताई और धन विधेयक के मार्ग के उपयोग को संविधान के साथ धोखा कहा, और रोजर मैथ्यू ने बहुमत के तर्क को कमज़ोर पाकर प्रश्न बड़ी पीठ को भेजा। "
  "कथन 4 अनुच्छेद 109 को पूरा करता है: राज्यसभा केवल सिफ़ारिशें कर सकती है, जिन्हें लोकसभा मान भी सकती है और ठुकरा भी सकती है, और यदि वह चौदह दिनों के भीतर विधेयक नहीं लौटाती, तो विधेयक उसी रूप में पारित माना जाता है जिसमें लोकसभा ने उसे पारित किया था।",
  f"{COI}, Articles 109 and 110; {SC} -- K.S. Puttaswamy v. Union of India (Aadhaar, 2018); Rojer Mathew v. South Indian Bank Ltd. (2019).",
  "parl-money-bill-certificate-aadhaar")

S(PL, "hard", "Consider the following statements about the Tenth Schedule:",
  "दसवीं अनुसूची के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["A nominated member who joins a political party within six months of taking his or her seat is not disqualified.",
   "The question of disqualification on the ground of defection is decided by the presiding officer of the House.",
   "The 91st Amendment Act introduced an exception for a split by one-third of a legislature party.",
   "An independent member who joins a political party after the election is not disqualified."],
  ["जो मनोनीत सदस्य अपना स्थान ग्रहण करने के छह महीने के भीतर किसी राजनीतिक दल में शामिल होता है, वह निरर्हित नहीं होता।",
   "दल-बदल के आधार पर निरर्हता का प्रश्न सदन का पीठासीन अधिकारी तय करता है।",
   "91वें संशोधन अधिनियम ने विधायक दल के एक-तिहाई द्वारा विभाजन (split) का अपवाद जोड़ा।",
   "जो निर्दलीय सदस्य चुनाव के बाद किसी राजनीतिक दल में शामिल होता है, वह निरर्हित नहीं होता।"],
  C4, 1,
  "Statements 1 and 2 are correct (paragraphs 2(3) and 6 of the Schedule). "
  "Statement 3 reverses the history: the original 1985 Schedule allowed a 'split' by one-third of a legislature party; the 91st Amendment (2003) deleted that exception because it encouraged defections in instalments, leaving only a merger backed by two-thirds. "
  "Statement 4 is wrong: an independent who joins a party is disqualified, since he or she was elected on the strength of not belonging to one.",
  "कथन 1 और 2 सही हैं (अनुसूची के अनुच्छेद 2(3) और 6)। "
  "कथन 3 इतिहास उलट देता है: 1985 की मूल अनुसूची विधायक दल के एक-तिहाई द्वारा 'विभाजन' की अनुमति देती थी; 91वें संशोधन (2003) ने यह अपवाद हटा दिया, क्योंकि यह किस्तों में दल-बदल को बढ़ावा देता था, और केवल दो-तिहाई के समर्थन वाला विलय (merger) बचा। "
  "कथन 4 गलत है: जो निर्दलीय किसी दल में शामिल होता है वह निरर्हित होता है, क्योंकि वह किसी दल का न होने के आधार पर ही चुना गया था।",
  f"{COI}, Tenth Schedule; Constitution (Fifty-second Amendment) Act, 1985; Constitution (Ninety-first Amendment) Act, 2003.",
  "parl-tenth-schedule-members-split")

S(PL, "hard", "Consider the following statements about the Union Budget:",
  "केंद्रीय बजट के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Constitution does not use the word 'budget'; it speaks of the 'annual financial statement'.",
   "The Railway Budget was merged with the General Budget from 2017-18.",
   "The Constitution requires the estimates of expenditure to distinguish expenditure on revenue account from other expenditure."],
  ["संविधान 'बजट' शब्द का प्रयोग नहीं करता; वह 'वार्षिक वित्तीय विवरण' की बात करता है।",
   "रेल बजट को 2017-18 से सामान्य बजट में मिला दिया गया।",
   "संविधान अपेक्षा करता है कि व्यय के अनुमान राजस्व खाते के व्यय को अन्य व्यय से अलग दिखाएँ।"],
  C3, 2,
  "All three statements are correct. 'Budget' is the everyday name for the statement that Article 112 requires; clause (2) of that Article requires charged and voted expenditure to be shown separately and revenue expenditure to be distinguished from other expenditure. The separate Railway Budget, a practice begun in 1924 on the Acworth Committee's advice, ended in 2017 on the Bibek Debroy Committee's recommendation.",
  "तीनों कथन सही हैं। 'बजट' उस विवरण का प्रचलित नाम है जिसकी अपेक्षा अनुच्छेद 112 करता है; उसी अनुच्छेद का खंड (2) भारित और मतदेय व्यय को अलग-अलग दिखाने और राजस्व व्यय को अन्य व्यय से अलग करने की अपेक्षा करता है। 1924 में एकवर्थ समिति की सलाह पर शुरू हुई अलग रेल बजट की प्रथा 2017 में बिबेक देबरॉय समिति की सिफ़ारिश पर समाप्त हुई।",
  f"{COI}, Article 112; Ministry of Finance -- Union Budget 2017-18.",
  "parl-budget-term-railway-revenue")

S(PL, "hard", "Consider the following statements about Parliament and the courts:",
  "संसद और न्यायालयों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The validity of any proceedings in Parliament cannot be called in question in a court on the ground of any alleged irregularity of procedure.",
   "In Raja Ram Pal (2007), the Supreme Court held that the expulsion of members by a House is open to judicial review on limited grounds such as illegality or unconstitutionality.",
   "In Sita Soren (2024), the Supreme Court held that members enjoy immunity from prosecution for taking a bribe to vote or speak in the House."],
  ["संसद की किसी भी कार्यवाही की वैधता पर प्रक्रिया की किसी कथित अनियमितता के आधार पर न्यायालय में प्रश्न नहीं उठाया जा सकता।",
   "राजा राम पाल (2007) में उच्चतम न्यायालय ने माना कि सदन द्वारा सदस्यों का निष्कासन अवैधता या असंवैधानिकता जैसे सीमित आधारों पर न्यायिक समीक्षा के अधीन है।",
   "सीता सोरेन (2024) में उच्चतम न्यायालय ने माना कि सदन में मत देने या बोलने के लिए रिश्वत लेने पर सदस्यों को अभियोजन से उन्मुक्ति है।"],
  C3, 1,
  "Statements 1 and 2 are correct: Article 122 shields internal procedure from the courts, but Raja Ram Pal, while upholding the expulsion of MPs caught in a cash-for-questions sting, held that substantive illegality or unconstitutionality can still be examined. "
  "Statement 3 reverses Sita Soren: a seven-judge bench overruled P.V. Narasimha Rao (1998) and held that the privileges in Articles 105 and 194 do not protect bribery, because the offence is complete when the bribe is taken, whatever the vote.",
  "कथन 1 और 2 सही हैं: अनुच्छेद 122 आंतरिक प्रक्रिया को न्यायालयों से बचाता है, पर राजा राम पाल ने, सवाल के बदले नकदी वाले स्टिंग में पकड़े गए सांसदों के निष्कासन को सही ठहराते हुए, माना कि मूल अवैधता या असंवैधानिकता की जाँच फिर भी हो सकती है। "
  "कथन 3 सीता सोरेन को उलट देता है: सात न्यायाधीशों की पीठ ने पी.वी. नरसिम्हा राव (1998) को पलटा और माना कि अनुच्छेद 105 और 194 के विशेषाधिकार रिश्वतखोरी की रक्षा नहीं करते, क्योंकि रिश्वत लेते ही अपराध पूरा हो जाता है, मत चाहे जो हो।",
  f"{COI}, Articles 105, 122 and 194; {SC} -- Raja Ram Pal v. Hon'ble Speaker, Lok Sabha (2007); Sita Soren v. Union of India (2024).",
  "parl-courts-122-raja-ram-pal-sita-soren")

S(PL, "hard", "Consider the following statements about grants voted by the Lok Sabha:",
  "लोकसभा द्वारा दिए जाने वाले अनुदानों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["A demand for an excess grant is presented to the Lok Sabha only after it has been approved by the Public Accounts Committee.",
   "A token grant is sought when the funds for a new service can be made available by re-appropriation.",
   "A vote of credit is a grant for an unexpected demand whose magnitude or indefinite character prevents it from being stated in the usual detail."],
  ["अतिरिक्त (excess) अनुदान की माँग लोकसभा में लोक लेखा समिति के अनुमोदन के बाद ही रखी जाती है।",
   "सांकेतिक (token) अनुदान तब माँगा जाता है जब किसी नई सेवा के लिए धन पुनर्विनियोग से उपलब्ध कराया जा सकता हो।",
   "प्रत्यय-अनुदान (vote of credit) ऐसी अप्रत्याशित माँग के लिए अनुदान है जिसका परिमाण या अनिश्चित स्वरूप उसे सामान्य विस्तार से बताने नहीं देता।"],
  C3, 2,
  "All three statements are correct. Excess grants regularise spending beyond what was voted, so the House first waits for the PAC to examine the excess. A token grant, usually for one rupee, lets the House approve a new service while the money comes by re-appropriation. A vote of credit, provided for with exceptional grants in Article 116, is like a blank cheque and is meant for emergencies such as war.",
  "तीनों कथन सही हैं। अतिरिक्त अनुदान स्वीकृत राशि से अधिक व्यय को नियमित करते हैं, इसलिए सदन पहले लोक लेखा समिति द्वारा उस अधिकता की जाँच की प्रतीक्षा करता है। सांकेतिक अनुदान, प्रायः एक रुपये का, सदन को किसी नई सेवा को मंज़ूरी देने देता है जबकि धन पुनर्विनियोग से आता है। अनुच्छेद 116 में असाधारण अनुदानों के साथ प्रावधानित प्रत्यय-अनुदान एक कोरे चेक जैसा है और युद्ध जैसी आपात स्थितियों के लिए है।",
  f"{COI}, Articles 115 and 116; {PRS}.",
  "parl-excess-token-credit-grants")

S(PL, "hard", "Consider the following statements about members of Parliament:",
  "संसद सदस्यों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["A person who sits or votes as a member before taking the oath is liable to a penalty of five hundred rupees for each day.",
   "Members take the oath or affirmation before the Chief Justice of India.",
   "A member who wishes to resign addresses the resignation to the President."],
  ["शपथ लेने से पहले सदस्य के रूप में बैठने या मत देने वाला व्यक्ति हर दिन के लिए पाँच सौ रुपये के दंड का भागी है।",
   "सदस्य भारत के मुख्य न्यायाधीश के सामने शपथ या प्रतिज्ञान करते हैं।",
   "त्यागपत्र देना चाहने वाला सदस्य अपना त्यागपत्र राष्ट्रपति को संबोधित करता है।"],
  C3, 0,
  "Only statement 1 is correct: Article 104 imposes the penalty, recoverable as a debt due to the Union. "
  "Statement 2 is wrong: under Article 99 members make the oath before the President or a person appointed by him -- in practice the Speaker pro tem and those assisting him. "
  "Statement 3 is wrong: under Article 101(3)(b) a member resigns by writing to the Speaker or the Chairman, who must be satisfied that the resignation is voluntary and genuine before accepting it.",
  "केवल कथन 1 सही है: अनुच्छेद 104 यह दंड लगाता है, जो संघ को देय ऋण की तरह वसूला जा सकता है। "
  "कथन 2 गलत है: अनुच्छेद 99 के तहत सदस्य राष्ट्रपति या उनके द्वारा नियुक्त व्यक्ति के सामने शपथ लेते हैं; व्यवहार में यह अध्यक्ष प्रो-टेम और उसकी सहायता करने वाले होते हैं। "
  "कथन 3 गलत है: अनुच्छेद 101(3)(b) के तहत सदस्य अध्यक्ष या सभापति को लिखकर त्यागपत्र देता है, जिन्हें स्वीकार करने से पहले संतुष्ट होना होता है कि त्यागपत्र स्वैच्छिक और वास्तविक है।",
  f"{COI}, Articles 99, 101(3) and 104.",
  "parl-members-oath-penalty-resignation")

S(PL, "hard", "At present, which of the following States have a Legislative Council?",
  "वर्तमान में निम्नलिखित में से किन राज्यों में विधान परिषद है?",
  ["Bihar", "Tamil Nadu", "Madhya Pradesh", "Rajasthan"],
  ["बिहार", "तमिलनाडु", "मध्य प्रदेश", "राजस्थान"],
  C4, 0,
  "Only Bihar has one. Six States have a Legislative Council -- Andhra Pradesh, Bihar, Karnataka, Maharashtra, Telangana and Uttar Pradesh. "
  "Tamil Nadu abolished its Council in 1986; a 2010 law to revive it was not acted on after a change of government. Madhya Pradesh is the subtle trap: Article 168 still names it among the States with two Houses, but its Council has never been constituted. Rajasthan's proposal has never been enacted by Parliament.",
  "केवल बिहार में है। छह राज्यों में विधान परिषद है: आंध्र प्रदेश, बिहार, कर्नाटक, महाराष्ट्र, तेलंगाना और उत्तर प्रदेश। "
  "तमिलनाडु ने 1986 में अपनी परिषद समाप्त कर दी; 2010 में उसे फिर से बनाने का कानून सरकार बदलने के बाद लागू नहीं हुआ। मध्य प्रदेश सूक्ष्म जाल है: अनुच्छेद 168 अब भी उसे दो सदनों वाले राज्यों में गिनाता है, पर उसकी परिषद कभी गठित नहीं हुई। राजस्थान का प्रस्ताव संसद ने कभी अधिनियमित नहीं किया।",
  f"{COI}, Articles 168 and 169; Tamil Nadu Legislative Council (Abolition) Act, 1986.",
  "parl-states-with-legislative-council",
  closing="How many of the above States have a Legislative Council at present?",
  closing_hi="उपर्युक्त में से कितने राज्यों में वर्तमान में विधान परिषद है?")

S(PL, "hard", "Consider the following statements about the President's addresses to Parliament:",
  "संसद को राष्ट्रपति के अभिभाषणों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The President addresses both Houses assembled together at the commencement of the first session after each general election to the Lok Sabha.",
   "The President addresses both Houses assembled together at the commencement of the first session of each year.",
   "The President can address the two Houses only when they are assembled together, and not either House separately."],
  ["राष्ट्रपति लोकसभा के हर आम चुनाव के बाद के पहले सत्र के आरंभ में एक साथ समवेत दोनों सदनों को संबोधित करते हैं।",
   "राष्ट्रपति हर वर्ष के पहले सत्र के आरंभ में एक साथ समवेत दोनों सदनों को संबोधित करते हैं।",
   "राष्ट्रपति दोनों सदनों को केवल तब संबोधित कर सकते हैं जब वे एक साथ समवेत हों, किसी एक सदन को अलग से नहीं।"],
  C3, 1,
  "Statements 1 and 2 are correct: these are the two occasions for the special address under Article 87, which sets out the Government's policies and is followed by the Motion of Thanks. "
  "Statement 3 is wrong: Article 86(1) lets the President address either House separately or both together at any time, and Article 86(2) lets him send messages to either House, for instance about a pending Bill.",
  "कथन 1 और 2 सही हैं: ये अनुच्छेद 87 के तहत विशेष अभिभाषण के दो अवसर हैं, जो सरकार की नीतियाँ बताता है और जिसके बाद धन्यवाद प्रस्ताव आता है। "
  "कथन 3 गलत है: अनुच्छेद 86(1) राष्ट्रपति को किसी भी समय किसी एक सदन को अलग से या दोनों को एक साथ संबोधित करने देता है, और अनुच्छेद 86(2) उन्हें किसी भी सदन को संदेश भेजने देता है, उदाहरण के लिए किसी लंबित विधेयक के बारे में।",
  f"{COI}, Articles 86 and 87.",
  "parl-president-addresses-86-87")

S(PL, "hard", "Consider the following statements about the Deputy Speaker of the Lok Sabha:",
  "लोकसभा के उपाध्यक्ष के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Deputy Speaker is subordinate to the Speaker and responsible to him.",
   "When appointed a member of a parliamentary committee, the Deputy Speaker automatically becomes its chairman.",
   "The Constitution requires the Deputy Speaker to be chosen from the Opposition."],
  ["उपाध्यक्ष अध्यक्ष के अधीन है और उसके प्रति उत्तरदायी है।",
   "किसी संसदीय समिति का सदस्य नियुक्त होने पर उपाध्यक्ष स्वतः उसका सभापति बन जाता है।",
   "संविधान अपेक्षा करता है कि उपाध्यक्ष विपक्ष से चुना जाए।"],
  C3, 0,
  "Only statement 2 is correct: this is a privilege of the office under the House's rules. "
  "Statement 1 is wrong: the Deputy Speaker is elected by the House and responsible to it, not to the Speaker; addressing a resignation to the Speaker does not make the office subordinate. "
  "Statement 3 is wrong: giving the post to the Opposition is only a convention followed from time to time. Article 93 simply requires the House to choose a Speaker and a Deputy Speaker 'as soon as may be' -- and the office stayed vacant through the whole of the 17th Lok Sabha.",
  "केवल कथन 2 सही है: यह सदन के नियमों के तहत इस पद का विशेषाधिकार है। "
  "कथन 1 गलत है: उपाध्यक्ष सदन द्वारा चुना जाता है और उसी के प्रति उत्तरदायी है, अध्यक्ष के प्रति नहीं; त्यागपत्र अध्यक्ष को संबोधित करने से पद अधीन नहीं हो जाता। "
  "कथन 3 गलत है: यह पद विपक्ष को देना केवल एक परिपाटी है, जिसका समय-समय पर पालन हुआ है। अनुच्छेद 93 केवल यह अपेक्षा करता है कि सदन 'यथाशीघ्र' अध्यक्ष और उपाध्यक्ष चुने; और 17वीं लोकसभा के पूरे कार्यकाल में यह पद रिक्त रहा।",
  f"{COI}, Articles 93-95; {PRS}.",
  "parl-deputy-speaker-position")

S(PL, "hard", "Consider the following statements about motions in Parliament:",
  "संसद में प्रस्तावों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["A closure motion is moved by a member to cut short the debate on a matter before the House.",
   "A privilege motion can be moved only by the presiding officer of the House.",
   "A 'no-day-yet-named' motion is one that the Speaker has declined to admit."],
  ["समापन प्रस्ताव (closure motion) किसी सदस्य द्वारा सदन के सामने किसी विषय पर बहस को छोटा करने के लिए लाया जाता है।",
   "विशेषाधिकार प्रस्ताव केवल सदन का पीठासीन अधिकारी ला सकता है।",
   "'अनिर्दिष्ट दिवस' (no-day-yet-named) प्रस्ताव वह है जिसे अध्यक्ष ने स्वीकार करने से इनकार कर दिया है।"],
  C3, 0,
  "Only statement 1 is correct: closure has several forms (simple, compartment, kangaroo and guillotine). "
  "Statement 3 is wrong: a 'no-day-yet-named' motion is one the Speaker has admitted but for which no date has yet been fixed for discussion -- it is waiting for time, not rejected. "
  "Statement 2 is wrong: a privilege motion is moved by a member who believes that a minister or anyone else has committed a breach of the privilege of the House or its members, for instance by withholding or distorting facts; the presiding officer decides whether to admit it.",
  "केवल कथन 1 सही है: समापन के कई रूप हैं (साधारण, खंडवार, कंगारू और गिलोटिन)। "
  "कथन 3 गलत है: 'अनिर्दिष्ट दिवस' प्रस्ताव वह है जिसे अध्यक्ष ने स्वीकार कर लिया है, पर जिस पर चर्चा की कोई तिथि अभी तय नहीं हुई है; वह समय की प्रतीक्षा में है, अस्वीकृत नहीं। "
  "कथन 2 गलत है: विशेषाधिकार प्रस्ताव वह सदस्य लाता है जो मानता है कि किसी मंत्री या किसी और ने सदन या उसके सदस्यों के विशेषाधिकार का उल्लंघन किया है, उदाहरण के लिए तथ्य छिपाकर या तोड़-मरोड़कर; उसे स्वीकार करना है या नहीं, यह पीठासीन अधिकारी तय करता है।",
  f"{LSR}; {PRS}.",
  "parl-closure-privilege-motions")

# ---------------------------------------------------------------- MCQs (medium 4, hard 3, easy 1)
M(PL, "medium", "Under Article 110, which one of the following would NOT by itself make a Bill a Money Bill?",
  "अनुच्छेद 110 के तहत निम्नलिखित में से कौन-सा प्रावधान अपने आप में किसी विधेयक को धन विधेयक नहीं बनाएगा?",
  ["A provision for the imposition of fines or other pecuniary penalties",
   "A provision for the imposition, abolition or regulation of any tax",
   "A provision for regulating the borrowing of money by the Government of India",
   "A provision for the custody of the Consolidated Fund of India"],
  ["जुर्माने या अन्य आर्थिक दंड लगाने का प्रावधान",
   "किसी कर को लगाने, हटाने या उसके नियमन का प्रावधान",
   "भारत सरकार द्वारा धन उधार लेने के नियमन का प्रावधान",
   "भारत की संचित निधि की अभिरक्षा का प्रावधान"],
  0,
  "Article 110(2) says a Bill is not a Money Bill merely because it provides for fines or other pecuniary penalties, fees for licences or services, or taxes by a local authority. The other three are among the matters in Article 110(1)(a)-(g), and a Bill is a Money Bill only if it deals with such matters alone -- the word 'only' is at the centre of the Aadhaar controversy.",
  "अनुच्छेद 110(2) कहता है कि कोई विधेयक केवल इस कारण धन विधेयक नहीं है कि उसमें जुर्माने या अन्य आर्थिक दंड, लाइसेंस या सेवाओं के शुल्क, या किसी स्थानीय प्राधिकरण के करों का प्रावधान है। बाकी तीन अनुच्छेद 110(1)(a)-(g) के विषयों में हैं, और कोई विधेयक तभी धन विधेयक है जब वह केवल ऐसे विषयों से संबंधित हो; 'केवल' शब्द ही आधार विवाद के केंद्र में है।",
  f"{COI}, Article 110.",
  "parl-money-bill-fines-not")

M(PL, "medium", "The Consolidated Fund of India is constituted under which Article of the Constitution?",
  "भारत की संचित निधि संविधान के किस अनुच्छेद के तहत गठित है?",
  ["Article 266", "Article 267", "Article 112", "Article 280"],
  ["अनुच्छेद 266", "अनुच्छेद 267", "अनुच्छेद 112", "अनुच्छेद 280"],
  0,
  "Article 266(1) creates the Consolidated Fund of India, into which go all revenues received by the Union, loans it raises and money received in repayment of loans; Article 266(2) creates the Public Account. Article 267 is the Contingency Fund, the closest distractor, and Article 280 the Finance Commission.",
  "अनुच्छेद 266(1) भारत की संचित निधि बनाता है, जिसमें संघ को प्राप्त सारा राजस्व, उसके द्वारा लिए गए ऋण और ऋणों की वापसी में मिला धन जाता है; अनुच्छेद 266(2) लोक लेखा बनाता है। अनुच्छेद 267 आकस्मिकता निधि है, जो सबसे निकट का गलत विकल्प है, और अनुच्छेद 280 वित्त आयोग।",
  f"{COI}, Articles 266, 267 and 280.",
  "parl-consolidated-fund-266")

M(PL, "medium", "In the Lok Sabha, the Question Hour is normally:",
  "लोकसभा में प्रश्नकाल सामान्यतः होता है:",
  ["the first hour of every sitting", "the last hour of every sitting", "the hour immediately after the Zero Hour", "the first hour after the lunch break"],
  ["हर बैठक का पहला घंटा", "हर बैठक का अंतिम घंटा", "शून्यकाल के ठीक बाद का घंटा", "भोजनावकाश के बाद का पहला घंटा"],
  0,
  "Under the rules of both Houses, the first hour of a sitting is kept for questions, when ministers are held to account on the floor. The Zero Hour follows it, which is why the option placing the Question Hour after the Zero Hour is reversed.",
  "दोनों सदनों के नियमों के तहत बैठक का पहला घंटा प्रश्नों के लिए रखा जाता है, जब सदन में मंत्रियों से जवाब लिया जाता है। शून्यकाल उसके बाद आता है, इसीलिए प्रश्नकाल को शून्यकाल के बाद रखने वाला विकल्प उलटा है।",
  f"{LSR}, Rule 32.",
  "parl-question-hour-first-hour")

M(PL, "medium", "A motion of no-confidence in the Council of Ministers is admitted for discussion in the Lok Sabha only if it is supported by at least:",
  "लोकसभा में मंत्रिपरिषद के विरुद्ध अविश्वास प्रस्ताव चर्चा के लिए तभी स्वीकार होता है जब उसे कम से कम किसका समर्थन हो?",
  ["50 members", "100 members", "one-tenth of the total membership of the House", "one-fourth of the members present"],
  ["50 सदस्य", "100 सदस्य", "सदन की कुल सदस्य-संख्या का दसवाँ भाग", "उपस्थित सदस्यों का एक-चौथाई"],
  0,
  "Rule 198 of the Lok Sabha's rules requires the leave of the House, which is granted if at least 50 members rise in support. The motion need not state reasons, and if adopted the Council of Ministers must resign. 'One-tenth' is the quorum of the House, which is why that option tempts.",
  "लोकसभा के नियमों का नियम 198 सदन की अनुमति की अपेक्षा करता है, जो तब मिलती है जब कम से कम 50 सदस्य समर्थन में खड़े हों। प्रस्ताव में कारण बताना ज़रूरी नहीं है, और स्वीकृत होने पर मंत्रिपरिषद को त्यागपत्र देना होता है। 'दसवाँ भाग' सदन की गणपूर्ति है, इसीलिए वह विकल्प आकर्षक लगता है।",
  f"{LSR}, Rule 198.",
  "parl-no-confidence-50-members")

M(PL, "hard", "The first joint sitting of the two Houses of Parliament, held in 1961, was on the:",
  "संसद के दोनों सदनों की पहली संयुक्त बैठक, जो 1961 में हुई, किस पर थी?",
  ["Dowry Prohibition Bill", "Hindu Marriage Bill", "Special Marriage Bill", "Untouchability (Offences) Bill"],
  ["दहेज प्रतिषेध विधेयक", "हिंदू विवाह विधेयक", "विशेष विवाह विधेयक", "अस्पृश्यता (अपराध) विधेयक"],
  0,
  "The Rajya Sabha and the Lok Sabha disagreed over amendments to the Dowry Prohibition Bill, 1959, and President Rajendra Prasad summoned the Houses to a joint sitting in May 1961, which passed it as the Dowry Prohibition Act, 1961. The other three were social reform laws of the 1950s passed without a joint sitting.",
  "राज्यसभा और लोकसभा दहेज प्रतिषेध विधेयक, 1959 के संशोधनों पर असहमत थीं, और राष्ट्रपति राजेंद्र प्रसाद ने मई 1961 में सदनों को संयुक्त बैठक में बुलाया, जिसने इसे दहेज प्रतिषेध अधिनियम, 1961 के रूप में पारित किया। बाकी तीन 1950 के दशक के सामाजिक सुधार कानून थे, जो संयुक्त बैठक के बिना पारित हुए।",
  f"{PRS}; Dowry Prohibition Act, 1961.",
  "parl-first-joint-sitting-dowry")

M(PL, "hard", "The Leader of the Opposition in the Lok Sabha is NOT a member of the committee or authority concerned with the appointment of:",
  "लोकसभा में विपक्ष का नेता किसकी नियुक्ति से संबंधित समिति या प्राधिकरण का सदस्य नहीं है?",
  ["the Comptroller and Auditor-General of India", "the Director of the Central Bureau of Investigation",
   "the Chairperson of the National Human Rights Commission", "the Chief Election Commissioner"],
  ["भारत के नियंत्रक-महालेखापरीक्षक", "केंद्रीय अन्वेषण ब्यूरो (CBI) के निदेशक",
   "राष्ट्रीय मानवाधिकार आयोग के अध्यक्ष", "मुख्य निर्वाचन आयुक्त"],
  0,
  "The CAG is appointed by the President under Article 148 on the Government's advice, with no selection committee. The Leader of the Opposition sits on the committees for the CBI Director (with the Prime Minister and the Chief Justice of India), the NHRC Chairperson, and -- since the 2023 Act -- the Chief Election Commissioner. The office is statutory, created by a 1977 Act, and has become a check through these committees.",
  "CAG की नियुक्ति राष्ट्रपति अनुच्छेद 148 के तहत सरकार की सलाह पर करते हैं, कोई चयन समिति नहीं होती। विपक्ष का नेता CBI निदेशक (प्रधानमंत्री और भारत के मुख्य न्यायाधीश के साथ), NHRC अध्यक्ष, और 2023 के अधिनियम के बाद से मुख्य निर्वाचन आयुक्त की समितियों में होता है। यह पद वैधानिक है, 1977 के एक अधिनियम से बना, और इन समितियों के ज़रिए एक नियंत्रण बन गया है।",
  f"{COI}, Article 148; Delhi Special Police Establishment Act, 1946, section 4A; Protection of Human Rights Act, 1993, section 4; Chief Election Commissioner and Other Election Commissioners Act, 2023; Salary and Allowances of Leaders of Opposition in Parliament Act, 1977.",
  "parl-leader-of-opposition-committees")

M(PL, "hard", "Which one of the following legislative Houses is presided over by a person who is not a member of that House?",
  "निम्नलिखित में से किस विधायी सदन की अध्यक्षता ऐसा व्यक्ति करता है जो उस सदन का सदस्य नहीं है?",
  ["Rajya Sabha", "Lok Sabha", "State Legislative Council", "State Legislative Assembly"],
  ["राज्यसभा", "लोकसभा", "राज्य विधान परिषद", "राज्य विधानसभा"],
  0,
  "The Vice-President is the ex officio Chairman of the Rajya Sabha (Article 64) but is not a member of it -- which is why he has no vote in the first instance and exercises only a casting vote. The Speaker, the Chairman of a Legislative Council and the Speaker of an Assembly are all chosen from among the members of their Houses; the State Council is the closest trap because its presiding officer also bears the title 'Chairman'.",
  "उपराष्ट्रपति राज्यसभा के पदेन सभापति हैं (अनुच्छेद 64), पर उसके सदस्य नहीं; इसीलिए उन्हें पहली बार में मत नहीं मिलता और वे केवल निर्णायक मत देते हैं। लोकसभा अध्यक्ष, विधान परिषद के सभापति और विधानसभा अध्यक्ष, सभी अपने सदनों के सदस्यों में से चुने जाते हैं; राज्य विधान परिषद सबसे निकट का जाल है, क्योंकि उसके पीठासीन अधिकारी का पदनाम भी 'सभापति' है।",
  f"{COI}, Articles 64, 89, 93, 178 and 182.",
  "parl-rajya-sabha-chairman-not-member")

M(PL, "easy", "A joint sitting of the two Houses of Parliament is provided for in:",
  "संसद के दोनों सदनों की संयुक्त बैठक का प्रावधान किसमें है?",
  ["Article 108", "Article 109", "Article 101", "Article 111"],
  ["अनुच्छेद 108", "अनुच्छेद 109", "अनुच्छेद 101", "अनुच्छेद 111"],
  0,
  "Article 108 lets the President summon a joint sitting when a Bill passed by one House is rejected by the other, when the Houses disagree on amendments, or when more than six months pass without the other House passing it. Article 109 is the special procedure for Money Bills, Article 101 deals with vacation of seats, and Article 111 with assent to Bills.",
  "अनुच्छेद 108 राष्ट्रपति को संयुक्त बैठक बुलाने देता है जब एक सदन द्वारा पारित विधेयक दूसरा सदन अस्वीकार कर दे, जब सदन संशोधनों पर असहमत हों, या जब दूसरे सदन के उसे पारित किए बिना छह महीने से अधिक बीत जाएँ। अनुच्छेद 109 धन विधेयकों की विशेष प्रक्रिया है, अनुच्छेद 101 स्थानों के रिक्त होने से संबंधित है, और अनुच्छेद 111 विधेयकों पर अनुमति से।",
  f"{COI}, Articles 101, 108, 109 and 111.",
  "parl-joint-sitting-art108-easy")

# ---------------------------------------------------------------- Statement-I/II (medium 4, easy 1) and hard (2)
A(PL, "medium",
  "A House of Parliament may declare the seat of a member vacant if he or she is absent from all its meetings for sixty days without its permission.",
  "यदि कोई सदस्य सदन की अनुमति के बिना साठ दिनों तक उसकी सभी बैठकों से अनुपस्थित रहे, तो संसद का सदन उसका स्थान रिक्त घोषित कर सकता है।",
  "In computing the period of sixty days, periods during which the House is prorogued or adjourned for more than four consecutive days are not counted.",
  "साठ दिनों की अवधि की गणना में वे अवधियाँ नहीं गिनी जातीं जिनमें सदन का सत्रावसान हो या वह लगातार चार दिनों से अधिक के लिए स्थगित हो।",
  1,
  "Both statements are correct, but Statement-II does not explain Statement-I. Article 101(4) gives the House the power to declare the seat vacant; Statement-II is only the rule for counting the sixty days, which ensures that breaks in sittings do not work against a member.",
  "दोनों कथन सही हैं, पर कथन-II कथन-I की व्याख्या नहीं करता। अनुच्छेद 101(4) सदन को स्थान रिक्त घोषित करने की शक्ति देता है; कथन-II केवल साठ दिनों की गणना का नियम है, जो सुनिश्चित करता है कि बैठकों के अंतराल किसी सदस्य के विरुद्ध न जाएँ।",
  f"{COI}, Article 101(4).",
  "parl-sixty-days-absence")

A(PL, "medium",
  "The Rajya Sabha can, by a resolution, empower Parliament to make laws on a matter in the State List in the national interest.",
  "राज्यसभा संकल्प द्वारा संसद को राष्ट्रीय हित में राज्य सूची के किसी विषय पर कानून बनाने की शक्ति दे सकती है।",
  "The Rajya Sabha represents the States in the federal structure.",
  "राज्यसभा संघीय ढाँचे में राज्यों का प्रतिनिधित्व करती है।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I. Article 249 gives this power to the Rajya Sabha alone -- by a two-thirds majority of members present and voting, for a year at a time -- precisely because it is the House of the States: an intrusion into the State List is allowed only with the consent of the States' own chamber.",
  "दोनों कथन सही हैं, और कथन-II कथन-I की व्याख्या करता है। अनुच्छेद 249 यह शक्ति केवल राज्यसभा को देता है, उपस्थित और मत देने वाले सदस्यों के दो-तिहाई बहुमत से और एक बार में एक वर्ष के लिए, ठीक इसलिए कि वह राज्यों का सदन है: राज्य सूची में दख़ल केवल राज्यों के अपने सदन की सहमति से ही होने दिया गया है।",
  f"{COI}, Article 249; {NC} -- Legislature.",
  "parl-art249-rajya-sabha-states")

A(PL, "medium",
  "A person cannot be a member of both Houses of Parliament at the same time.",
  "कोई व्यक्ति एक ही समय में संसद के दोनों सदनों का सदस्य नहीं हो सकता।",
  "If a person elected to both Houses does not choose one within the prescribed period, his or her seat in the Lok Sabha falls vacant.",
  "यदि दोनों सदनों के लिए चुना गया व्यक्ति निर्धारित अवधि के भीतर एक सदन नहीं चुनता, तो लोकसभा में उसका स्थान रिक्त हो जाता है।",
  2,
  "Statement-I is correct but Statement-II is incorrect. Article 101(1) bars dual membership and leaves the details to Parliament; under section 68 of the Representation of the People Act, 1951, such a person must intimate a choice within ten days, failing which it is the seat in the Rajya Sabha that falls vacant.",
  "कथन-I सही है पर कथन-II गलत है। अनुच्छेद 101(1) दोहरी सदस्यता को रोकता है और ब्योरा संसद पर छोड़ता है; लोक प्रतिनिधित्व अधिनियम, 1951 की धारा 68 के तहत ऐसे व्यक्ति को दस दिनों के भीतर अपनी पसंद बतानी होती है, अन्यथा राज्यसभा वाला स्थान रिक्त हो जाता है।",
  f"{COI}, Article 101(1); Representation of the People Act, 1951, section 68.",
  "parl-dual-membership-both-houses")

A(PL, "medium",
  "Parliament can discuss the conduct of a judge of the Supreme Court in the discharge of his duties during the debate on the budget.",
  "संसद बजट पर बहस के दौरान उच्चतम न्यायालय के किसी न्यायाधीश के कर्तव्यों के निर्वहन में आचरण पर चर्चा कर सकती है।",
  "Article 121 bars any discussion in Parliament on the conduct of a judge of the Supreme Court or a High Court in the discharge of his duties, except upon a motion for his removal.",
  "अनुच्छेद 121 संसद में उच्चतम न्यायालय या उच्च न्यायालय के किसी न्यायाधीश के कर्तव्यों के निर्वहन में आचरण पर किसी भी चर्चा को रोकता है, सिवाय उसे हटाने के प्रस्ताव के।",
  3,
  "Statement-I is incorrect but Statement-II is correct. Article 121 protects judicial independence by keeping judges' conduct out of ordinary parliamentary debate -- the budget debate included -- so that the only route is the removal procedure, with its special majority and inquiry.",
  "कथन-I गलत है पर कथन-II सही है। अनुच्छेद 121 न्यायाधीशों के आचरण को सामान्य संसदीय बहस से, बजट पर बहस सहित, बाहर रखकर न्यायिक स्वतंत्रता की रक्षा करता है, ताकि एकमात्र रास्ता विशेष बहुमत और जाँच वाली हटाने की प्रक्रिया ही रहे।",
  f"{COI}, Articles 121 and 124(4).",
  "parl-art121-judges-conduct")

A(PL, "easy",
  "The Speaker presides over the Lok Sabha.",
  "अध्यक्ष लोकसभा की अध्यक्षता करता है।",
  "The Speaker is elected by the members of the Lok Sabha from among themselves.",
  "अध्यक्ष को लोकसभा के सदस्य अपने में से चुनते हैं।",
  1,
  "Both statements are correct, but Statement-II does not explain Statement-I. The Speaker presides because the Constitution and the rules give that office the duty of conducting the House; how the Speaker is chosen, by election under Article 93, is a separate matter.",
  "दोनों कथन सही हैं, पर कथन-II कथन-I की व्याख्या नहीं करता। अध्यक्ष इसलिए अध्यक्षता करता है कि संविधान और नियम उस पद को सदन के संचालन का कर्तव्य देते हैं; अध्यक्ष कैसे चुना जाता है, यानी अनुच्छेद 93 के तहत चुनाव से, यह एक अलग बात है।",
  f"{COI}, Article 93; {NC} -- Legislature.",
  "parl-speaker-presides-elected-easy")

A(PL, "hard",
  "A Bill pending in the Lok Sabha lapses when the Lok Sabha is dissolved.",
  "लोकसभा में लंबित विधेयक लोकसभा के विघटन पर व्यपगत हो जाता है।",
  "Dissolution brings the life of the existing Lok Sabha to an end.",
  "विघटन वर्तमान लोकसभा के जीवनकाल को समाप्त कर देता है।",
  2,
  "Only one of Statements II and III is correct -- Statement II -- and it explains Statement I: business pending before a House that has ceased to exist cannot survive, so Bills pending in the Lok Sabha, and Bills passed by it and pending in the Rajya Sabha, lapse. "
  "Statement III is wrong: a Bill pending in the Rajya Sabha that the Lok Sabha has not yet passed does not lapse. Nor does a Bill for which a joint sitting was notified before dissolution, or one passed by both Houses and awaiting the President's assent or returned by him.",
  "कथन II और III में से केवल एक, कथन II, सही है और वह कथन I की व्याख्या करता है: जिस सदन का अस्तित्व समाप्त हो गया, उसके सामने लंबित कार्य बचा नहीं रह सकता; इसलिए लोकसभा में लंबित विधेयक, और उसके द्वारा पारित और राज्यसभा में लंबित विधेयक, व्यपगत हो जाते हैं। "
  "कथन III गलत है: राज्यसभा में लंबित जो विधेयक लोकसभा ने अभी पारित नहीं किया है, वह व्यपगत नहीं होता। न ही वह विधेयक जिसके लिए विघटन से पहले संयुक्त बैठक अधिसूचित हो चुकी थी, या जो दोनों सदनों से पारित होकर राष्ट्रपति की अनुमति की प्रतीक्षा में हो या उनके द्वारा लौटाया गया हो।",
  f"{COI}, Articles 83(2), 85(2)(b) and 107(5); {PRS}.",
  "parl-lapse-of-bills-dissolution",
  s3="A Bill pending in the Rajya Sabha that has not yet been passed by the Lok Sabha also lapses on the dissolution of the Lok Sabha.",
  s3_hi="राज्यसभा में लंबित जो विधेयक लोकसभा ने अभी पारित नहीं किया है, वह भी लोकसभा के विघटन पर व्यपगत हो जाता है।")

A(PL, "hard",
  "A presiding officer's decision on disqualification under the Tenth Schedule can be challenged in the courts.",
  "दसवीं अनुसूची के तहत निरर्हता पर पीठासीन अधिकारी के निर्णय को न्यायालयों में चुनौती दी जा सकती है।",
  "In Kihoto Hollohan (1992), the Supreme Court struck down paragraph 7 of the Tenth Schedule, which barred the jurisdiction of courts.",
  "किहोतो होलोहन (1992) में उच्चतम न्यायालय ने दसवीं अनुसूची के अनुच्छेद 7 को रद्द कर दिया, जो न्यायालयों के क्षेत्राधिकार को रोकता था।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I. The Court upheld the anti-defection law but struck down paragraph 7 because, affecting the High Courts' and Supreme Court's jurisdiction, it needed ratification by the States and had not received it. The presiding officer acts as a tribunal, and his decision can be reviewed for mala fides, perversity or violation of natural justice or constitutional mandates.",
  "दोनों कथन सही हैं, और कथन-II कथन-I की व्याख्या करता है। न्यायालय ने दल-बदल विरोधी कानून को सही ठहराया, पर अनुच्छेद 7 को रद्द कर दिया, क्योंकि उच्च न्यायालयों और उच्चतम न्यायालय के क्षेत्राधिकार को प्रभावित करने के कारण उसके लिए राज्यों का अनुसमर्थन आवश्यक था, जो नहीं मिला था। पीठासीन अधिकारी एक अधिकरण की तरह कार्य करता है, और उसके निर्णय की दुर्भावना, विकृति, या प्राकृतिक न्याय अथवा संवैधानिक आदेशों के उल्लंघन के आधार पर समीक्षा हो सकती है।",
  f"{SC} -- Kihoto Hollohan v. Zachillhu (1992); {COI}, Tenth Schedule.",
  "parl-kihoto-paragraph-7")

# ---------------------------------------------------------------- pairs (medium 3, hard 1)
P(PL, "medium", "Consider the following pairs of parliamentary devices and their features:",
  "संसदीय उपायों और उनकी विशेषताओं के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Starred question : Answered orally, and supplementary questions can follow",
   "Unstarred question : Answered in writing, and supplementary questions can follow",
   "Short duration discussion : Held without a formal motion before the House, and no vote is taken",
   "Half-an-hour discussion : Used to censure a minister for his conduct"],
  ["तारांकित प्रश्न : मौखिक उत्तर दिया जाता है, और अनुपूरक प्रश्न पूछे जा सकते हैं",
   "अतारांकित प्रश्न : लिखित उत्तर दिया जाता है, और अनुपूरक प्रश्न पूछे जा सकते हैं",
   "अल्पकालिक चर्चा : सदन के सामने औपचारिक प्रस्ताव के बिना होती है, और मतदान नहीं होता",
   "आधे घंटे की चर्चा : किसी मंत्री की उसके आचरण के लिए निंदा करने में उपयोग होती है"],
  1,
  "Only pairs 1 and 3 are correct. A starred question is distinguished by an asterisk and invites supplementaries, and a short duration discussion, introduced in 1953, lets the House discuss a matter of urgent public importance without a vote. "
  "Pair 2 is wrong: an unstarred question gets a written answer and no supplementaries. Pair 4 is wrong: a half-an-hour discussion is for elucidating a matter of public importance arising out of answers to questions; censure is done by a censure motion.",
  "केवल युग्म 1 और 3 सही हैं। तारांकित प्रश्न तारे के चिह्न से पहचाना जाता है और उस पर अनुपूरक प्रश्न पूछे जा सकते हैं, और 1953 में शुरू हुई अल्पकालिक चर्चा सदन को तात्कालिक सार्वजनिक महत्त्व के विषय पर बिना मतदान के चर्चा करने देती है। "
  "युग्म 2 गलत है: अतारांकित प्रश्न का लिखित उत्तर मिलता है और अनुपूरक प्रश्न नहीं होते। युग्म 4 गलत है: आधे घंटे की चर्चा प्रश्नों के उत्तरों से उठे सार्वजनिक महत्त्व के किसी विषय को स्पष्ट करने के लिए है; निंदा के लिए निंदा प्रस्ताव लाया जाता है।",
  f"{LSR}, Rules 36-55 and 193; {PRS}.",
  "parl-devices-questions-discussions-pairs")

P(PL, "medium", "Consider the following pairs of Articles of the Constitution and their subject matter:",
  "संविधान के अनुच्छेदों और उनकी विषय-वस्तु के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Article 85 : Sessions of Parliament, prorogation and dissolution", "Article 100 : Voting in the Houses and the quorum",
   "Article 116 : Votes on account, votes of credit and exceptional grants", "Article 99 : Salaries and allowances of members"],
  ["अनुच्छेद 85 : संसद के सत्र, सत्रावसान और विघटन", "अनुच्छेद 100 : सदनों में मतदान और गणपूर्ति",
   "अनुच्छेद 116 : लेखानुदान, प्रत्यय-अनुदान और असाधारण अनुदान", "अनुच्छेद 99 : सदस्यों के वेतन और भत्ते"],
  2,
  "Three pairs are correct. Pair 4 is wrong: Article 99 deals with the oath or affirmation by members; salaries and allowances are in Article 106, which leaves them to be fixed by Parliament by law.",
  "तीन युग्म सही हैं। युग्म 4 गलत है: अनुच्छेद 99 सदस्यों द्वारा शपथ या प्रतिज्ञान से संबंधित है; वेतन और भत्ते अनुच्छेद 106 में हैं, जो उन्हें संसद के कानून से तय होने के लिए छोड़ता है।",
  f"{COI}, Articles 85, 99, 100, 106 and 116.",
  "parl-articles-85-100-116-pairs")

P(PL, "medium", "Consider the following pairs of majorities and the purposes for which they are required:",
  "बहुमतों और जिन प्रयोजनों के लिए वे आवश्यक हैं, उनके निम्नलिखित युग्मों पर विचार कीजिए:",
  ["A majority of all the then members of the House : Removal of the Deputy Speaker of the Lok Sabha",
   "A majority of the total membership and two-thirds of the members present and voting in each House : Passing a Constitution Amendment Bill",
   "A majority of the members present and voting : Passing a Money Bill in the Lok Sabha",
   "Two-thirds of the total membership of the House : Impeachment of the President"],
  ["सदन के तत्कालीन सभी सदस्यों का बहुमत : लोकसभा के उपाध्यक्ष को हटाना",
   "हर सदन में कुल सदस्य-संख्या का बहुमत और उपस्थित तथा मत देने वाले सदस्यों का दो-तिहाई : संविधान संशोधन विधेयक पारित करना",
   "उपस्थित और मत देने वाले सदस्यों का बहुमत : लोकसभा में धन विधेयक पारित करना",
   "सदन की कुल सदस्य-संख्या का दो-तिहाई : राष्ट्रपति पर महाभियोग"],
  3,
  "All four pairs are correct. The 'effective majority' of pair 1 (Article 94(c)) excludes vacancies; the special majority of pair 2 comes from Article 368(2); a Money Bill, like other Bills, needs only a simple majority; and impeachment (Article 61) needs two-thirds of the total membership of each House -- the highest threshold in the Constitution. "
  "Students who expect one mismatch in every set will fall for 'Only three pairs'.",
  "चारों युग्म सही हैं। युग्म 1 का 'प्रभावी बहुमत' (अनुच्छेद 94(c)) रिक्तियों को छोड़कर गिना जाता है; युग्म 2 का विशेष बहुमत अनुच्छेद 368(2) से आता है; धन विधेयक को, दूसरे विधेयकों की तरह, केवल साधारण बहुमत चाहिए; और महाभियोग (अनुच्छेद 61) के लिए हर सदन की कुल सदस्य-संख्या का दो-तिहाई चाहिए, जो संविधान की सबसे ऊँची सीमा है। "
  "जो विद्यार्थी हर सेट में एक बेमेल की अपेक्षा करते हैं, वे 'केवल तीन युग्म' के जाल में फँसेंगे।",
  f"{COI}, Articles 61, 94, 100 and 368.",
  "parl-majorities-purposes-pairs")

P(PL, "hard", "Consider the following pairs of financial committees and the year in which they were first constituted:",
  "वित्तीय समितियों और उनके पहली बार गठित होने के वर्ष के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Public Accounts Committee : 1921", "Estimates Committee : 1950", "Committee on Public Undertakings : 1975", "Department-related Standing Committees : 1993"],
  ["लोक लेखा समिति : 1921", "प्राक्कलन समिति : 1950", "सार्वजनिक उपक्रम समिति : 1975", "विभाग-संबंधी स्थायी समितियाँ : 1993"],
  2,
  "Three pairs are correct. The PAC was first set up in 1921 under the Government of India Act, 1919; the Estimates Committee in 1950 on the suggestion of the Finance Minister John Mathai; and the department-related standing committees in 1993, to let Parliament scrutinise the demands for grants of each ministry in detail. "
  "Pair 3 is wrong: the Committee on Public Undertakings was created in 1964 on the recommendation of the Krishna Menon Committee.",
  "तीन युग्म सही हैं। लोक लेखा समिति पहली बार 1921 में भारत सरकार अधिनियम, 1919 के तहत बनी; प्राक्कलन समिति 1950 में वित्त मंत्री जॉन मथाई के सुझाव पर; और विभाग-संबंधी स्थायी समितियाँ 1993 में, ताकि संसद हर मंत्रालय की अनुदान माँगों की विस्तार से जाँच कर सके। "
  "युग्म 3 गलत है: सार्वजनिक उपक्रम समिति 1964 में कृष्ण मेनन समिति की सिफ़ारिश पर बनी।",
  f"{PRS}; Lok Sabha Secretariat -- Parliamentary Committees.",
  "parl-committees-years-pairs")

# ---------------------------------------------------------------- easy statement (1)
S(PL, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Members of the Lok Sabha are directly elected by the people.",
   "The term of a member of the Rajya Sabha is five years."],
  ["लोकसभा के सदस्य जनता द्वारा प्रत्यक्ष रूप से चुने जाते हैं।",
   "राज्यसभा के सदस्य का कार्यकाल पाँच वर्ष है।"],
  T2, 0,
  "Only statement 1 is correct: Lok Sabha members are chosen by direct election from territorial constituencies on the basis of adult suffrage. Statement 2 is wrong: a member of the Rajya Sabha serves for six years, and one-third of the members retire every second year, as fixed by the Representation of the People Act, 1951.",
  "केवल कथन 1 सही है: लोकसभा के सदस्य वयस्क मताधिकार के आधार पर क्षेत्रीय निर्वाचन क्षेत्रों से प्रत्यक्ष चुनाव द्वारा चुने जाते हैं। कथन 2 गलत है: राज्यसभा का सदस्य छह वर्ष के लिए होता है, और लोक प्रतिनिधित्व अधिनियम, 1951 के अनुसार हर दूसरे वर्ष एक-तिहाई सदस्य सेवानिवृत्त होते हैं।",
  f"{COI}, Articles 81 and 83; Representation of the People Act, 1951, section 154.",
  "parl-lok-sabha-direct-rajya-term-easy")

if __name__ == "__main__":
    write("pol_l2_t2_parliament.sql")
