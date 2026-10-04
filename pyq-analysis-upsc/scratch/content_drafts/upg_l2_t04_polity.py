# -*- coding: utf-8 -*-
"""Level 2 · Test 4 (Polity 4: Federalism, Governance & Local Government) -- depth audit of 2026-10-04
(docs/upsc-question-design-standard.md §6).

All 105 rows in the test's three sub-topics were read and classified. Before: analytic 10, precision 44,
recall 51 (5 rows are Test 21's, already tagged). 27 rows are rewritten in place with the same concept id,
type and difficulty.
  - 21 recall rows become cases, inferences or linkages:
      why the Governor acts on advice; why no State can secede; six subjects and the 42nd Amendment; a
      Tribes Advisory Council where there are no Scheduled Areas; a border dispute in a Zonal Council; a
      dispute before the Inter-State Council; 42 to 41 per cent; elections and complaints in a multi-State
      co-operative; one app for many services; delta ranking; a delayed service under a Citizen's Charter;
      a pregnant woman and a 72-year-old under Mission Shakti and PM-JAY; SVAMITVA cards; a CBI Director
      with no Leader of the Opposition; NGOs and pressure groups; grouped ranking in the Good Governance
      Index; roles-based training; a village Common Services Centre; a 22-year-old candidate; a
      metropolitan area; a self-help group seeking credit.
  - 6 precision rows become cases:
      a State prohibition law and imported liquor; an oral order and a quick transfer; Aadhaar for a SIM
      and a school; MPLADS nodal districts; an 18-lakh State's Panchayats; a mine in a Scheduled Area.
After: analytic 37, precision 38, recall 30. The other 78 rows keep their content and get their craft tag.
Leaks avoided while drafting:
  - the Zonal Council's and Inter-State Council's chairs (answer the chairs pairs row);
  - 'residuary powers' and Article 254 in the pith-and-substance options (answer the legislative-relations
    and repugnancy rows);
  - 'net proceeds' and cesses in the Finance Commission row (answer the divisible-pool AR);
  - CPGRAMS by name in the Citizen's Charter row (answers the PRAGATI MCQ);
  - 'extends Part IX to the Fifth Schedule areas' in the PESA row (answers the Article 243M AR)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write_updates, CODE
from polity_common import C3, C4, T2

d.SUBJECT = "Polity"
d.REQUIRE_CRAFT = True
FED = "Federalism & Special Provisions"
GOV = "Governance"
PR = "Panchayati Raj & Local Governance"
COI = "Constitution of India"
SC = "Supreme Court of India"
CAD = "Constituent Assembly Debates"

# ================================================================ ASSERTION-REASON (2)
A(FED, "easy", "The Governor of a State normally acts on the advice of the State Council of Ministers.",
  "राज्य का राज्यपाल सामान्यतः राज्य मंत्रिपरिषद की सलाह पर कार्य करता है।",
  "The Governor is the constitutional head of the State, while real executive power lies with the Council of Ministers headed by the Chief Minister.",
  "राज्यपाल राज्य का संवैधानिक प्रमुख है, जबकि वास्तविक कार्यकारी शक्ति मुख्यमंत्री की अध्यक्षता वाली मंत्रिपरिषद के पास होती है।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I. The States follow the same parliamentary model as the Union: executive power is vested in the Governor in name, but under Article 163 it is exercised on the aid and advice of the Council of Ministers, which is responsible to the Legislative Assembly. "
  "The exceptions are the matters in which the Constitution requires the Governor to act in his discretion, such as reserving a Bill for the President or sending a report under Article 356. The Supreme Court in Nabam Rebia (2016) held that this discretion is confined to the matters the Constitution specifies.",
  "दोनों कथन सही हैं, और कथन-II कथन-I की व्याख्या करता है। राज्य भी संघ जैसे संसदीय मॉडल का पालन करते हैं: कार्यकारी शक्ति नाम से राज्यपाल में निहित है, पर अनुच्छेद 163 के तहत उसका प्रयोग मंत्रिपरिषद की सहायता और सलाह पर होता है, जो विधानसभा के प्रति उत्तरदायी है। "
  "अपवाद वे विषय हैं जिनमें संविधान राज्यपाल से अपने विवेक से कार्य करने की अपेक्षा करता है, जैसे किसी विधेयक को राष्ट्रपति के लिए आरक्षित करना या अनुच्छेद 356 के तहत प्रतिवेदन भेजना। सर्वोच्च न्यायालय ने नबाम रेबिया (2016) में कहा कि यह विवेक संविधान द्वारा बताए गए विषयों तक ही सीमित है।",
  f"{COI} -- Articles 154 and 163; {SC} -- Nabam Rebia v. Deputy Speaker (2016).",
  "fed-governor-head-appointment-easy", craft="linkage")

A(FED, "medium", "No State has a right to secede from the Indian Union.",
  "किसी राज्य को भारतीय संघ से अलग होने का अधिकार नहीं है।",
  "The Constitution calls India a 'Union of States' because the Union is not the result of an agreement among the States.",
  "संविधान भारत को 'राज्यों का संघ' इसलिए कहता है कि यह संघ राज्यों के बीच किसी समझौते का परिणाम नहीं है।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I. Dr. B.R. Ambedkar told the Constituent Assembly that 'Union' was chosen deliberately: the Indian federation was not formed by States agreeing to join it, as the American one was, and because it was not the result of an agreement, no State has the right to secede from it. "
  "The States are not even indestructible: under Articles 3 and 4 Parliament can change their areas, boundaries and names by ordinary law, after only seeking the views of the State Legislature concerned. Hence the description of India as 'an indestructible Union of destructible States'.",
  "दोनों कथन सही हैं, और कथन-II कथन-I की व्याख्या करता है। डॉ. बी.आर. आंबेडकर ने संविधान सभा में बताया कि 'संघ' (Union) शब्द जानबूझकर चुना गया: भारतीय संघ अमेरिकी संघ की तरह राज्यों के सहमत होकर जुड़ने से नहीं बना, और चूँकि यह किसी समझौते का परिणाम नहीं है, इसलिए किसी राज्य को इससे अलग होने का अधिकार नहीं है। "
  "राज्य अविनाशी भी नहीं हैं: अनुच्छेद 3 और 4 के तहत संसद साधारण क़ानून से उनके क्षेत्र, सीमाएँ और नाम बदल सकती है, केवल संबंधित राज्य विधानमंडल के विचार लेकर। इसीलिए भारत को 'विनाशी राज्यों का अविनाशी संघ' कहा जाता है।",
  f"{COI} -- Article 1; {CAD}, 4 November 1948.",
  "federalism-union-of-states-art1", craft="linkage")

# ================================================================ MCQs (5)
M(FED, "medium", "Which of the following subjects were moved from the State List to the Concurrent List by the 42nd Amendment Act, 1976?\n1. Forests\n2. Education\n3. Public health and sanitation\n4. Weights and measures\n5. Agriculture\n6. Protection of wild animals and birds\nSelect the correct answer using the code given below.",
  "निम्नलिखित में से कौन-से विषय 42वें संशोधन अधिनियम, 1976 द्वारा राज्य सूची से समवर्ती सूची में ले जाए गए?\n1. वन\n2. शिक्षा\n3. लोक स्वास्थ्य और स्वच्छता\n4. बाट और माप\n5. कृषि\n6. वन्य पशुओं और पक्षियों का संरक्षण\nनीचे दिए गए कूट का प्रयोग कर सही उत्तर चुनिए।",
  ["1, 2, 4 and 6 only", "1, 2 and 6 only", "2, 3, 4 and 5 only", "1, 3, 5 and 6 only"],
  ["केवल 1, 2, 4 और 6", "केवल 1, 2 और 6", "केवल 2, 3, 4 और 5", "केवल 1, 3, 5 और 6"],
  0,
  "The 42nd Amendment moved five subjects from the State List to the Concurrent List: education, forests, weights and measures (except the establishment of standards), the protection of wild animals and birds, and the administration of justice and the constitution of courts other than the Supreme Court and the High Courts. "
  "Public health and sanitation and agriculture are still in the State List. The change let the Union legislate on forests and wildlife -- the Forest (Conservation) Act, 1980 followed -- and on education, and it remains one of the most centralising shifts in the distribution of powers.",
  "42वें संशोधन ने पाँच विषय राज्य सूची से समवर्ती सूची में डाले: शिक्षा, वन, बाट और माप (मानकों की स्थापना को छोड़कर), वन्य पशुओं और पक्षियों का संरक्षण, तथा न्याय प्रशासन और सर्वोच्च न्यायालय व उच्च न्यायालयों के सिवा अन्य न्यायालयों का गठन। "
  "लोक स्वास्थ्य और स्वच्छता तथा कृषि अब भी राज्य सूची में हैं। इस बदलाव से संघ वन और वन्यजीवों पर, जिसके बाद वन (संरक्षण) अधिनियम, 1980 आया, और शिक्षा पर क़ानून बना सका; यह शक्तियों के बँटवारे में सबसे केंद्रीकरण वाले बदलावों में से एक है।",
  f"{COI} -- Seventh Schedule; Constitution (Forty-second Amendment) Act, 1976.",
  "fed-42nd-state-to-concurrent", craft="multi")

M(FED, "medium", "A State has a sizeable Scheduled Tribe population but no Scheduled Areas. Under the Fifth Schedule, a Tribes Advisory Council:",
  "एक राज्य में अनुसूचित जनजातियों की बड़ी आबादी है, पर कोई अनुसूचित क्षेत्र नहीं है। पाँचवीं अनुसूची के तहत जनजाति सलाहकार परिषद:",
  ["may be set up in the State if the President so directs",
   "must be set up, since the State has Scheduled Tribes",
   "cannot be set up, since only States with Scheduled Areas may have one",
   "may be set up by the Governor on his own, with up to thirty members"],
  ["राष्ट्रपति के निर्देश देने पर राज्य में बनाई जा सकती है",
   "बनानी ही होगी, क्योंकि राज्य में अनुसूचित जनजातियाँ हैं",
   "नहीं बनाई जा सकती, क्योंकि यह केवल अनुसूचित क्षेत्रों वाले राज्यों में हो सकती है",
   "राज्यपाल अपनी ओर से बना सकता है, जिसमें तीस तक सदस्य हों"],
  0,
  "Paragraph 4 of the Fifth Schedule requires a Tribes Advisory Council in every State that has Scheduled Areas, and also in any State that has Scheduled Tribes but no Scheduled Areas if the President so directs -- as Tamil Nadu and West Bengal have. "
  "The Council has not more than twenty members, of whom as nearly as possible three-fourths are Scheduled Tribe members of the State Legislative Assembly, and it advises on matters concerning the welfare of the Scheduled Tribes that the Governor refers to it.",
  "पाँचवीं अनुसूची का पैरा 4 हर उस राज्य में जनजाति सलाहकार परिषद अनिवार्य करता है जहाँ अनुसूचित क्षेत्र हैं, और उस राज्य में भी जहाँ अनुसूचित जनजातियाँ हैं पर अनुसूचित क्षेत्र नहीं, यदि राष्ट्रपति ऐसा निर्देश दें; तमिलनाडु और पश्चिम बंगाल में ऐसा ही हुआ है। "
  "परिषद में बीस से अधिक सदस्य नहीं होते, जिनमें यथासंभव तीन-चौथाई राज्य विधानसभा के अनुसूचित जनजाति सदस्य होते हैं, और यह अनुसूचित जनजातियों के कल्याण से जुड़े उन विषयों पर सलाह देती है जो राज्यपाल उसे भेजे।",
  f"{COI} -- Fifth Schedule, paragraph 4.",
  "fed-tribes-advisory-council", craft="application")

M(FED, "medium", "A State law prohibits the sale and possession of liquor, a State List subject, and in doing so it also restricts liquor imported from abroad, a Union List matter. Applying the doctrine of pith and substance, a court would most likely:",
  "एक राज्य क़ानून शराब की बिक्री और रखने पर प्रतिबंध लगाता है, जो राज्य सूची का विषय है, और ऐसा करते हुए वह विदेश से आयातित शराब को भी प्रतिबंधित करता है, जो संघ सूची का विषय है। 'सार और तत्व' का सिद्धांत लागू करते हुए न्यायालय संभवतः:",
  ["uphold it, since in its true nature it is a law on a State List subject",
   "strike it down, since a State law cannot touch a Union List matter even incidentally",
   "uphold it only in so far as it does not apply to imported liquor",
   "strike it down, since only Parliament can make a law that overlaps two Lists"],
  ["इसे वैध ठहराएगा, क्योंकि अपने वास्तविक स्वरूप में यह राज्य सूची के विषय पर क़ानून है",
   "इसे रद्द करेगा, क्योंकि राज्य क़ानून संघ सूची के विषय को प्रासंगिक रूप से भी नहीं छू सकता",
   "इसे केवल वहीं तक वैध ठहराएगा जहाँ तक यह आयातित शराब पर लागू नहीं होता",
   "इसे रद्द करेगा, क्योंकि दो सूचियों में फैला क़ानून केवल संसद बना सकती है"],
  0,
  "Laws often touch entries in more than one List. Under the doctrine of pith and substance the court asks what the law is really about; if that falls within the enacting legislature's List, an incidental effect on a subject in another List does not invalidate it. "
  "This was the reasoning in State of Bombay v. F.N. Balsara (1951), where the Bombay Prohibition Act was upheld as a law on intoxicating liquors even though it affected imported liquor. Reading the law down to exclude imports would ignore the doctrine, and no rule reserves overlapping laws to Parliament.",
  "क़ानून प्रायः एक से अधिक सूचियों की प्रविष्टियों को छूते हैं। 'सार और तत्व' के सिद्धांत में न्यायालय देखता है कि क़ानून वास्तव में किस बारे में है; यदि वह बनाने वाले विधानमंडल की सूची में आता है, तो किसी अन्य सूची के विषय पर प्रासंगिक प्रभाव उसे अवैध नहीं बनाता। "
  "बॉम्बे राज्य बनाम एफ़.एन. बलसारा (1951) में यही तर्क था, जहाँ बॉम्बे मद्यनिषेध अधिनियम को मादक शराब पर क़ानून मानकर वैध ठहराया गया, यद्यपि वह आयातित शराब को प्रभावित करता था। आयात को बाहर करके क़ानून को सीमित पढ़ना इस सिद्धांत की उपेक्षा होगी, और ऐसा कोई नियम नहीं जो फैले हुए क़ानून संसद के लिए आरक्षित करे।",
  f"{SC} -- State of Bombay v. F.N. Balsara (1951); {COI} -- Article 246.",
  "fed-pith-and-substance", craft="application")

M(GOV, "hard", "A multi-State co-operative society's board elections are due, and one of its members has a complaint about how the society is run. Under the Multi-State Co-operative Societies Act, 2002, as amended in 2023, which one of the following is correct?",
  "एक बहु-राज्य सहकारी समिति के बोर्ड के चुनाव होने हैं, और उसके एक सदस्य को समिति के संचालन के बारे में शिकायत है। 2023 में संशोधित बहु-राज्य सहकारी सोसाइटी अधिनियम, 2002 के तहत निम्नलिखित में से कौन-सा सही है?",
  ["The Co-operative Election Authority will conduct the election, and the complaint can go to the Co-operative Ombudsman",
   "The Central Registrar will conduct the election and also decide the complaint, as the Act creates no separate body for either",
   "The State Election Commission will conduct the election, and the complaint can go to the Co-operative Ombudsman",
   "The Co-operative Election Authority will conduct the election, and the complaint can go to the NCDC"],
  ["सहकारी निर्वाचन प्राधिकरण चुनाव कराएगा, और शिकायत सहकारी लोकपाल के पास जा सकती है",
   "केंद्रीय रजिस्ट्रार चुनाव कराएगा और शिकायत पर भी निर्णय करेगा, क्योंकि अधिनियम दोनों के लिए कोई अलग निकाय नहीं बनाता",
   "राज्य निर्वाचन आयोग चुनाव कराएगा, और शिकायत सहकारी लोकपाल के पास जा सकती है",
   "सहकारी निर्वाचन प्राधिकरण चुनाव कराएगा, और शिकायत NCDC के पास जा सकती है"],
  0,
  "The 2023 amendment created two separate bodies for multi-State co-operatives. The Co-operative Election Authority conducts their board elections, to make them free and fair. The Co-operative Ombudsman hears members' complaints about their deposits, the society's functioning and their individual rights. "
  "State Election Commissions conduct Panchayat and municipal elections, not these, and the National Co-operative Development Corporation is a financing body. The amendment also set up a fund to revive sick co-operatives.",
  "2023 के संशोधन ने बहु-राज्य सहकारी समितियों के लिए दो अलग निकाय बनाए। सहकारी निर्वाचन प्राधिकरण उनके बोर्ड चुनाव कराता है, ताकि वे स्वतंत्र और निष्पक्ष हों। सहकारी लोकपाल सदस्यों की उनकी जमा राशि, समिति के कामकाज और उनके व्यक्तिगत अधिकारों से जुड़ी शिकायतें सुनता है। "
  "राज्य निर्वाचन आयोग पंचायत और नगरपालिका चुनाव कराते हैं, ये नहीं, और राष्ट्रीय सहकारी विकास निगम एक वित्तपोषक निकाय है। संशोधन ने बीमार सहकारी समितियों को पुनर्जीवित करने के लिए एक कोष भी बनाया।",
  "Multi-State Co-operative Societies (Amendment) Act, 2023.",
  "gov-cooperative-election-authority", craft="application")

M(GOV, "medium", "A worker wants to check his provident fund balance, book a gas cylinder and apply for a passport, all from a single app on his phone. Which one of the following is designed for this?",
  "एक कामगार अपने फ़ोन पर एक ही ऐप से अपना भविष्य निधि शेष देखना, गैस सिलेंडर बुक करना और पासपोर्ट के लिए आवेदन करना चाहता है। निम्नलिखित में से कौन-सा इसी के लिए बनाया गया है?",
  ["UMANG", "DigiLocker", "MyGov", "Bhashini"],
  ["उमंग (UMANG)", "डिजिलॉकर", "माईगव (MyGov)", "भाषिणी"],
  0,
  "The Unified Mobile Application for New-age Governance (UMANG), launched in 2017, brings hundreds of Central and State services -- provident fund, gas booking, passport, utility bills and more -- onto one app. "
  "DigiLocker stores and shares verified digital documents, MyGov invites citizens to give suggestions and take part in policy discussions, and Bhashini is the national platform for translation between Indian languages.",
  "यूनिफ़ाइड मोबाइल एप्लिकेशन फ़ॉर न्यू-एज गवर्नेंस (उमंग), 2017 में शुरू, केंद्र और राज्यों की सैकड़ों सेवाएँ, जैसे भविष्य निधि, गैस बुकिंग, पासपोर्ट और बिल भुगतान, एक ही ऐप पर लाता है। "
  "डिजिलॉकर सत्यापित डिजिटल दस्तावेज़ रखता और साझा करता है, माईगव नागरिकों को सुझाव देने और नीतिगत चर्चाओं में भाग लेने के लिए आमंत्रित करता है, और भाषिणी भारतीय भाषाओं के बीच अनुवाद का राष्ट्रीय मंच है।",
  "Ministry of Electronics and Information Technology -- UMANG.",
  "gov-umang-app", craft="application")

# ================================================================ STATEMENTS (20)
S(FED, "medium", "Two neighbouring southern States disagree over their common border and over the facilities for a linguistic minority living along it. Consider the following statements:",
  "दक्षिण के दो पड़ोसी राज्यों में अपनी साझा सीमा और उसके किनारे रहने वाले एक भाषाई अल्पसंख्यक समुदाय की सुविधाओं को लेकर असहमति है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The two States can take up the matter in the Southern Zonal Council.",
   "The Zonal Council can settle the dispute by a decision that binds both States.",
   "The Chief Ministers of the States of the zone hold the office of Vice-Chairman of the Council by rotation."],
  ["दोनों राज्य यह विषय दक्षिणी क्षेत्रीय परिषद में उठा सकते हैं।",
   "क्षेत्रीय परिषद ऐसे निर्णय से विवाद सुलझा सकती है जो दोनों राज्यों को बाँधे।",
   "क्षेत्र के राज्यों के मुख्यमंत्री बारी-बारी से परिषद के उपाध्यक्ष का पद धारण करते हैं।"],
  C3, 1,
  "Statements 1 and 3 are correct. The five Zonal Councils -- Northern, Central, Eastern, Western and Southern -- are statutory bodies under the States Reorganisation Act, 1956, set up to foster co-operation and to discuss common problems such as border disputes, linguistic minorities and inter-State transport. The Union Home Minister chairs each Council, and the Chief Ministers of its States are Vice-Chairman in turn, a year at a time. "
  "Statement 2 is wrong: the Councils are advisory and can only recommend. The north-eastern States are served instead by the North Eastern Council, set up under a separate Act of 1971.",
  "कथन 1 और 3 सही हैं। पाँच क्षेत्रीय परिषदें, यानी उत्तरी, मध्य, पूर्वी, पश्चिमी और दक्षिणी, राज्य पुनर्गठन अधिनियम, 1956 के तहत वैधानिक निकाय हैं, जो सहयोग बढ़ाने और सीमा विवाद, भाषाई अल्पसंख्यक तथा अंतरराज्यीय परिवहन जैसी साझा समस्याओं पर चर्चा के लिए बनीं। केंद्रीय गृह मंत्री हर परिषद की अध्यक्षता करते हैं, और उसके राज्यों के मुख्यमंत्री एक-एक वर्ष के लिए बारी-बारी से उपाध्यक्ष होते हैं। "
  "कथन 2 गलत है: परिषदें सलाहकारी हैं और केवल सिफ़ारिश कर सकती हैं। पूर्वोत्तर राज्यों के लिए इसके बजाय 1971 के एक अलग अधिनियम के तहत बनी पूर्वोत्तर परिषद है।",
  "States Reorganisation Act, 1956, Part III; Ministry of Home Affairs -- Zonal Councils.",
  "fed-zonal-councils-nec", craft="application")

S(FED, "medium", "Two States are in dispute over a matter of common interest. Consider the following statements:",
  "दो राज्यों के बीच साझा हित के एक विषय पर विवाद है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["Article 263 allows the President to set up a council to inquire into and advise upon such a dispute.",
   "The Inter-State Council set up in 1990 has been given the duty of inquiring into disputes between States.",
   "Any recommendation of the Inter-State Council on the matter would bind the two States."],
  ["अनुच्छेद 263 राष्ट्रपति को ऐसे विवाद की जाँच कर सलाह देने के लिए एक परिषद बनाने देता है।",
   "1990 में बनी अंतरराज्यीय परिषद को राज्यों के बीच विवादों की जाँच का दायित्व दिया गया है।",
   "इस विषय पर अंतरराज्यीय परिषद की कोई भी सिफ़ारिश दोनों राज्यों को बाँधेगी।"],
  C3, 0,
  "Only statement 1 is correct. Article 263 lets the President, by order, set up a council with three possible duties: (a) inquiring into and advising upon disputes between States, (b) investigating subjects of common interest, and (c) recommending better co-ordination of policy. "
  "Statement 2 is wrong: the Presidential order of 1990, issued on the Sarkaria Commission's recommendation, gave the Inter-State Council only duties (b) and (c), not the dispute-inquiry function in clause (a). Statement 3 is wrong: the Council is recommendatory, and its strength lies in bringing the Union and the States to one table.",
  "केवल कथन 1 सही है। अनुच्छेद 263 राष्ट्रपति को आदेश द्वारा एक परिषद बनाने देता है, जिसके तीन संभावित कर्तव्य हैं: (क) राज्यों के बीच विवादों की जाँच कर सलाह देना, (ख) साझा हित के विषयों की जाँच करना, और (ग) नीतियों के बेहतर समन्वय की सिफ़ारिश करना। "
  "कथन 2 गलत है: सरकारिया आयोग की सिफ़ारिश पर जारी 1990 के राष्ट्रपति आदेश ने अंतरराज्यीय परिषद को केवल (ख) और (ग) कर्तव्य दिए, खंड (क) का विवाद-जाँच कार्य नहीं। कथन 3 गलत है: परिषद सिफ़ारिशी है, और उसकी शक्ति संघ और राज्यों को एक मेज़ पर लाने में है।",
  f"{COI} -- Article 263; Inter-State Council Order, 1990.",
  "fed-inter-state-council", craft="application")

S(FED, "medium", "The Fourteenth Finance Commission recommended that 42 per cent of the divisible pool of Union taxes go to the States; the Fifteenth recommended 41 per cent. Consider the following statements:",
  "चौदहवें वित्त आयोग ने सिफ़ारिश की थी कि संघीय करों के विभाज्य पूल का 42 प्रतिशत राज्यों को मिले; पंद्रहवें ने 41 प्रतिशत की सिफ़ारिश की। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The one-point fall roughly corresponds to the share of the former State of Jammu and Kashmir, which became two Union Territories in 2019.",
   "Since the 80th Amendment, the States' share is drawn from a single pool of almost all Union taxes, rather than from income tax and Union excise duties alone.",
   "The share recommended by the Commission takes effect through an order of the President."],
  ["एक अंक की कमी मोटे तौर पर पूर्व जम्मू-कश्मीर राज्य के हिस्से के बराबर है, जो 2019 में दो केंद्रशासित प्रदेश बन गया।",
   "80वें संशोधन से राज्यों का हिस्सा केवल आयकर और संघीय उत्पाद शुल्क से नहीं, बल्कि लगभग सभी संघीय करों के एक ही पूल से आता है।",
   "आयोग द्वारा सुझाया गया हिस्सा राष्ट्रपति के आदेश से लागू होता है।"],
  C3, 2,
  "All three are correct. The Fifteenth Commission kept the States' share at the Fourteenth's level in substance; the one point it took off was about the share that would have gone to Jammu and Kashmir, whose needs as Union Territories are met by the Union. "
  "The 80th Amendment of 2000, following the Tenth Commission's 'alternative scheme of devolution', replaced the older sharing of income tax and Union excise duties with a common pool of almost all Union taxes. Under Article 270 the States' percentage is 'prescribed' -- that is, fixed by an order of the President after considering the Commission's recommendation, which the Union has so far always accepted.",
  "तीनों कथन सही हैं। पंद्रहवें आयोग ने राज्यों का हिस्सा सार रूप में चौदहवें के स्तर पर रखा; जो एक अंक घटाया, वह लगभग जम्मू-कश्मीर के हिस्से के बराबर था, जिसकी केंद्रशासित प्रदेशों के रूप में ज़रूरतें संघ पूरी करता है। "
  "2000 के 80वें संशोधन ने, दसवें आयोग की 'हस्तांतरण की वैकल्पिक योजना' के बाद, आयकर और संघीय उत्पाद शुल्क के पुराने बँटवारे की जगह लगभग सभी संघीय करों का साझा पूल बनाया। अनुच्छेद 270 के तहत राज्यों का प्रतिशत 'विहित' होता है, यानी आयोग की सिफ़ारिश पर विचार कर राष्ट्रपति के आदेश से तय होता है, और संघ ने अब तक इसे सदा स्वीकार किया है।",
  f"Fifteenth Finance Commission, Report for 2021-26; {COI} -- Article 270.",
  "fed-divisible-pool-80th-15th-fc", craft="inference")

S(GOV, "medium", "Under the Aspirational Districts Programme, districts are ranked each month on their improvement across a set of indicators, rather than on their absolute level. Consider the following statements:",
  "आकांक्षी ज़िला कार्यक्रम के तहत ज़िलों को कुछ संकेतकों पर उनके निरपेक्ष स्तर के बजाय उनके सुधार के आधार पर हर महीने रैंक किया जाता है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["A district with poor indicators can rank above a district that is better off.",
   "The ranking relies on Census data, since that is the most reliable source.",
   "The method is meant to spur competition among the districts."],
  ["कमज़ोर संकेतकों वाला ज़िला बेहतर स्थिति वाले ज़िले से ऊपर रैंक पा सकता है।",
   "रैंकिंग जनगणना के आँकड़ों पर टिकी है, क्योंकि वही सबसे विश्वसनीय स्रोत है।",
   "यह तरीक़ा ज़िलों के बीच प्रतिस्पर्धा बढ़ाने के लिए है।"],
  C3, 1,
  "Statements 1 and 3 are correct. Ranking by improvement ('delta ranking') means a backward district that moves fast can outrank one that started higher, and that is the purpose: the programme, launched in 2018 for 112 districts, rests on convergence of schemes, collaboration between governments, and competition among districts. "
  "Statement 2 is wrong: a ten-yearly Census could not show monthly progress. The districts are tracked on a real-time online dashboard across health and nutrition, education, agriculture and water resources, financial inclusion and skills, and basic infrastructure.",
  "कथन 1 और 3 सही हैं। सुधार के आधार पर रैंकिंग ('डेल्टा रैंकिंग') का अर्थ है कि तेज़ी से आगे बढ़ने वाला पिछड़ा ज़िला ऊँचे स्तर से शुरू करने वाले ज़िले से आगे निकल सकता है, और यही उद्देश्य है: 2018 में 112 ज़िलों के लिए शुरू यह कार्यक्रम योजनाओं के अभिसरण, सरकारों के सहयोग और ज़िलों के बीच प्रतिस्पर्धा पर टिका है। "
  "कथन 2 गलत है: दस साल में एक बार होने वाली जनगणना मासिक प्रगति नहीं दिखा सकती। ज़िलों की निगरानी स्वास्थ्य और पोषण, शिक्षा, कृषि और जल संसाधन, वित्तीय समावेशन और कौशल, तथा बुनियादी ढाँचे पर एक रियल-टाइम ऑनलाइन डैशबोर्ड से होती है।",
  "NITI Aayog -- Aspirational Districts Programme.",
  "gov-aspirational-districts", craft="inference")

S(GOV, "hard", "A Union Ministry's Citizen's Charter promises that a service will be delivered within 30 days, but a citizen's application has been pending for three months. Consider the following statements:",
  "एक केंद्रीय मंत्रालय का नागरिक चार्टर वादा करता है कि एक सेवा 30 दिनों में दी जाएगी, पर एक नागरिक का आवेदन तीन महीने से लंबित है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The citizen can sue the Ministry to enforce the Charter's time limit, since the Charter is legally binding.",
   "The citizen can lodge a grievance on the Union's centralised online grievance portal, run by the Department of Administrative Reforms and Public Grievances.",
   "Under the Sevottam model, the Citizen's Charter and grievance redress are both components of excellence in service delivery.",
   "The Central Information Commission can order the Ministry to deliver the service within the promised time."],
  ["नागरिक चार्टर की समय-सीमा लागू कराने के लिए मंत्रालय पर मुक़दमा कर सकता है, क्योंकि चार्टर क़ानूनी रूप से बाध्यकारी है।",
   "नागरिक प्रशासनिक सुधार और लोक शिकायत विभाग द्वारा चलाए जाने वाले केंद्र के केंद्रीकृत ऑनलाइन शिकायत पोर्टल पर शिकायत दर्ज कर सकता है।",
   "सेवोत्तम मॉडल में नागरिक चार्टर और शिकायत निवारण दोनों सेवा प्रदायगी में उत्कृष्टता के घटक हैं।",
   "केंद्रीय सूचना आयोग मंत्रालय को वादे के समय में सेवा देने का आदेश दे सकता है।"],
  C4, 1,
  "Statements 2 and 3 are correct. India adopted Citizen's Charters in 1997, on the British model of 1991, but they are declarations of intent, not law, so statement 1 is wrong -- which is why many States have passed Right to Public Services Acts that make time limits enforceable with penalties. "
  "The citizen's remedy is a grievance on the centralised portal that DARPG runs for the Union. DARPG's Sevottam model treats the Charter, grievance redress and service-delivery capability as its three modules. Statement 4 is wrong: the Information Commission enforces the right to information, not the delivery of services.",
  "कथन 2 और 3 सही हैं। भारत ने 1997 में, 1991 के ब्रिटिश मॉडल पर, नागरिक चार्टर अपनाए, पर वे क़ानून नहीं, आशय की घोषणाएँ हैं, इसलिए कथन 1 गलत है; इसी कारण कई राज्यों ने लोक सेवा अधिकार अधिनियम बनाए जो समय-सीमाओं को दंड के साथ लागू कराने योग्य बनाते हैं। "
  "नागरिक का उपाय उस केंद्रीकृत पोर्टल पर शिकायत है जिसे प्रशासनिक सुधार और लोक शिकायत विभाग केंद्र के लिए चलाता है। इस विभाग का सेवोत्तम मॉडल चार्टर, शिकायत निवारण और सेवा-प्रदायगी क्षमता को अपने तीन मॉड्यूल मानता है। कथन 4 गलत है: सूचना आयोग सूचना का अधिकार लागू कराता है, सेवाओं की प्रदायगी नहीं।",
  "Department of Administrative Reforms and Public Grievances -- Citizen's Charters, Sevottam.",
  "governance-citizen-charter-sevottam", craft="application")

S(GOV, "medium", "A poor rural family includes a woman expecting her first child and a 72-year-old grandfather who needs heart surgery. Consider the following statements:",
  "एक ग़रीब ग्रामीण परिवार में अपने पहले बच्चे की अपेक्षा कर रही एक महिला और हृदय की शल्य-चिकित्सा की ज़रूरत वाले 72 वर्षीय दादा हैं। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The ₹5,000 maternity benefit for her first child is now provided under Mission Shakti.",
   "The family's cover of up to ₹5 lakh a year under Ayushman Bharat-PM-JAY can pay for the grandfather's surgery.",
   "Because of his age, he is entitled to an additional cover of up to ₹5 lakh a year that the younger members do not share."],
  ["उसके पहले बच्चे के लिए ₹5,000 का मातृत्व लाभ अब मिशन शक्ति के तहत दिया जाता है।",
   "आयुष्मान भारत-PM-JAY के तहत परिवार का ₹5 लाख प्रति वर्ष तक का कवर दादा की शल्य-चिकित्सा का ख़र्च उठा सकता है।",
   "अपनी आयु के कारण वह ₹5 लाख प्रति वर्ष तक के अतिरिक्त कवर का हक़दार है, जिसे परिवार के कम आयु वाले सदस्य साझा नहीं करते।"],
  C3, 2,
  "All three are correct. Since 2022 the Pradhan Mantri Matru Vandana Yojana, which pays ₹5,000 for the first child, has been part of 'Samarthya', one of the two sub-schemes of Mission Shakti, the Women and Child Development Ministry's umbrella scheme for women's safety and empowerment. "
  "PM-JAY gives eligible families cover of up to ₹5 lakh a year for hospital treatment. Since October 2024 every citizen aged 70 or more is covered irrespective of income, and one whose family is already covered gets an extra top-up of up to ₹5 lakh a year for himself, not shared with members below 70.",
  "तीनों कथन सही हैं। 2022 से प्रधानमंत्री मातृ वंदना योजना, जो पहले बच्चे के लिए ₹5,000 देती है, महिला एवं बाल विकास मंत्रालय की महिलाओं की सुरक्षा और सशक्तीकरण की छत्र योजना मिशन शक्ति की दो उप-योजनाओं में से एक 'सामर्थ्य' का भाग है। "
  "PM-JAY पात्र परिवारों को अस्पताल में उपचार के लिए ₹5 लाख प्रति वर्ष तक का कवर देती है। अक्टूबर 2024 से 70 वर्ष या उससे अधिक आयु का हर नागरिक आय से अलग शामिल है, और जिसका परिवार पहले से शामिल है उसे अपने लिए ₹5 लाख प्रति वर्ष तक का अतिरिक्त टॉप-अप मिलता है, जो 70 से कम आयु वालों के साथ साझा नहीं होता।",
  "Ministry of Women and Child Development -- Mission Shakti guidelines (2022); National Health Authority -- AB PM-JAY.",
  "gov-poshan-mission-shakti-pmjay", craft="application")

S(GOV, "medium", "A villager has lived for decades in a house in the inhabited ('abadi') area of his village but has no document of title. Consider the following statements in the light of the SVAMITVA scheme:",
  "एक ग्रामीण दशकों से अपने गाँव के आबादी क्षेत्र के एक घर में रहता है, पर उसके पास स्वामित्व का कोई दस्तावेज़ नहीं है। स्वामित्व (SVAMITVA) योजना के आलोक में निम्नलिखित कथनों पर विचार कीजिए:",
  ["A drone survey can map his plot, and he can be given a property card.",
   "He can use the property card to raise a loan from a bank.",
   "The cards can help the Gram Panchayat assess property tax.",
   "The card will also settle his ownership of the farmland he tills outside the village."],
  ["ड्रोन सर्वेक्षण से उसके भूखंड का मानचित्र बन सकता है, और उसे संपत्ति कार्ड दिया जा सकता है।",
   "वह संपत्ति कार्ड से बैंक से ऋण ले सकता है।",
   "ये कार्ड ग्राम पंचायत को संपत्ति कर का आकलन करने में मदद कर सकते हैं।",
   "यह कार्ड गाँव के बाहर उसके द्वारा जोते जाने वाले खेत पर भी उसका स्वामित्व तय कर देगा।"],
  C4, 2,
  "Statements 1, 2 and 3 are correct. Rural residential land had rarely been surveyed, so owners could not prove title. The scheme, launched on National Panchayati Raj Day in 2020, uses drones to map abadi plots and gives owners a 'record of rights' or property card. This lets them borrow against the property, reduces disputes, and gives Panchayats a base for property tax and village planning. "
  "Statement 4 is wrong: the scheme covers only inhabited village land. Agricultural land is recorded separately in the States' revenue land records.",
  "कथन 1, 2 और 3 सही हैं। ग्रामीण आवासीय भूमि का शायद ही कभी सर्वेक्षण हुआ था, इसलिए मालिक स्वामित्व सिद्ध नहीं कर पाते थे। 2020 में राष्ट्रीय पंचायती राज दिवस पर शुरू हुई यह योजना ड्रोन से आबादी भूखंडों का मानचित्र बनाती है और मालिकों को 'अधिकार अभिलेख' या संपत्ति कार्ड देती है। इससे वे संपत्ति पर ऋण ले सकते हैं, विवाद घटते हैं, और पंचायतों को संपत्ति कर तथा ग्राम नियोजन का आधार मिलता है। "
  "कथन 4 गलत है: योजना केवल गाँव की आबादी वाली भूमि को शामिल करती है। कृषि भूमि राज्यों के राजस्व भूमि अभिलेखों में अलग से दर्ज होती है।",
  "Ministry of Panchayati Raj -- SVAMITVA scheme.",
  "gov-svamitva", craft="application")

S(GOV, "medium", "The post of Director of the Central Bureau of Investigation falls vacant at a time when no one is recognised as the Leader of the Opposition in the Lok Sabha. Consider the following statements:",
  "केंद्रीय अन्वेषण ब्यूरो के निदेशक का पद ऐसे समय रिक्त होता है जब लोकसभा में किसी को विपक्ष के नेता के रूप में मान्यता नहीं है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The leader of the single largest opposition party in the Lok Sabha takes the Leader of the Opposition's place on the selection committee.",
   "Once appointed, the Director can be given extensions a year at a time, up to five years in all."],
  ["लोकसभा में सबसे बड़े विपक्षी दल का नेता चयन समिति में विपक्ष के नेता का स्थान लेता है।",
   "नियुक्ति के बाद निदेशक को एक-एक वर्ष का विस्तार दिया जा सकता है, कुल मिलाकर पाँच वर्ष तक।"],
  T2, 2,
  "Both statements are correct. Since the Lokpal and Lokayuktas Act, 2013, the Director is appointed on the recommendation of a committee of the Prime Minister, the Leader of the Opposition and the Chief Justice of India or a judge nominated by him. A 2014 amendment provided that where there is no recognised Leader of the Opposition, the leader of the single largest opposition party in the Lok Sabha sits instead -- the situation after the 2014 and 2019 elections. "
  "The Director has a minimum tenure of two years. A 2021 amendment allows extensions of up to one year at a time, to a total of five years, in the public interest and on the committee's recommendation; the Supreme Court upheld it in 2023.",
  "दोनों कथन सही हैं। लोकपाल और लोकायुक्त अधिनियम, 2013 से निदेशक की नियुक्ति प्रधानमंत्री, विपक्ष के नेता और भारत के मुख्य न्यायाधीश या उनके द्वारा नामित न्यायाधीश की समिति की सिफ़ारिश पर होती है। 2014 के एक संशोधन ने प्रावधान किया कि मान्यता प्राप्त विपक्ष का नेता न होने पर लोकसभा में सबसे बड़े विपक्षी दल का नेता बैठेगा; 2014 और 2019 के चुनावों के बाद यही स्थिति थी। "
  "निदेशक का न्यूनतम कार्यकाल दो वर्ष है। 2021 का एक संशोधन लोकहित में और समिति की सिफ़ारिश पर एक बार में एक वर्ष तक, कुल पाँच वर्ष तक, विस्तार की अनुमति देता है; सर्वोच्च न्यायालय ने 2023 में इसे वैध ठहराया।",
  "Delhi Special Police Establishment Act, 1946, sections 4A and 4B, as amended in 2014 and 2021.",
  "governance-cbi-dspe-director-appointment", craft="application")

S(GOV, "medium", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["A farmers' union becomes a political party once it campaigns to change government policy.",
   "An NGO registered as a company under section 8 of the Companies Act, 2013 may pay its surplus to its members as dividend.",
   "An NGO may accept a grant from a foundation abroad without any permission, so long as it shows the receipt in its annual accounts."],
  ["कोई किसान संघ सरकारी नीति बदलवाने के लिए अभियान चलाते ही राजनीतिक दल बन जाता है।",
   "कंपनी अधिनियम, 2013 की धारा 8 के तहत कंपनी के रूप में पंजीकृत NGO अपना अधिशेष सदस्यों को लाभांश के रूप में दे सकता है।",
   "कोई NGO विदेश के किसी प्रतिष्ठान से अनुदान बिना किसी अनुमति के ले सकता है, बशर्ते वह प्राप्ति को अपने वार्षिक खातों में दिखाए।"],
  C3, 3,
  "None is correct. A pressure group seeks to influence policy without contesting elections to capture power, so a farmers' union that campaigns but fields no candidates remains a pressure group. "
  "NGOs may be registered as societies, trusts or not-for-profit companies under section 8, and a section 8 company must apply its income to its objects and is barred from paying dividends to members. "
  "To receive foreign contribution an NGO needs registration or prior permission under the Foreign Contribution (Regulation) Act; showing the money in its accounts is no substitute.",
  "कोई भी कथन सही नहीं है। दबाव समूह सत्ता पाने के लिए चुनाव लड़े बिना नीति को प्रभावित करना चाहता है, इसलिए अभियान चलाने वाला पर कोई उम्मीदवार न उतारने वाला किसान संघ दबाव समूह ही रहता है। "
  "NGO सोसाइटी, न्यास या धारा 8 के तहत ग़ैर-लाभकारी कंपनी के रूप में पंजीकृत हो सकते हैं, और धारा 8 की कंपनी को अपनी आय अपने उद्देश्यों पर लगानी होती है तथा उसे सदस्यों को लाभांश देने की मनाही है। "
  "विदेशी अंशदान लेने के लिए NGO को विदेशी अंशदान (विनियमन) अधिनियम के तहत पंजीकरण या पूर्व अनुमति चाहिए; खातों में पैसा दिखाना इसका विकल्प नहीं है।",
  "Companies Act, 2013, section 8; Foreign Contribution (Regulation) Act, 2010.",
  "gov-pressure-groups-ngos", craft="application")

S(GOV, "medium", "The Good Governance Index ranks States and Union Territories within separate groups -- such as large States, and north-eastern and hill States -- across several sectors of governance. Consider the following statements:",
  "सुशासन सूचकांक राज्यों और केंद्रशासित प्रदेशों को शासन के कई क्षेत्रों में अलग-अलग समूहों, जैसे बड़े राज्य तथा पूर्वोत्तर और पहाड़ी राज्य, के भीतर रैंक करता है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["A hill State is compared mainly with other hill States rather than with the large States.",
   "The index looks only at the delivery of welfare schemes.",
   "It is prepared by NITI Aayog."],
  ["किसी पहाड़ी राज्य की तुलना मुख्यतः अन्य पहाड़ी राज्यों से होती है, बड़े राज्यों से नहीं।",
   "सूचकांक केवल कल्याणकारी योजनाओं की प्रदायगी को देखता है।",
   "इसे नीति आयोग तैयार करता है।"],
  C3, 0,
  "Only statement 1 is correct. Grouping is meant to compare like with like, so that small hill States with very different conditions are not ranked against large plains States. "
  "Statement 2 is wrong: the index, first released in 2019, covers ten sectors: agriculture, commerce and industry, human resources, public health, public infrastructure, economic governance, social welfare, judicial and public security, environment, and citizen-centric governance. "
  "Statement 3 is wrong: it is prepared by the Department of Administrative Reforms and Public Grievances.",
  "केवल कथन 1 सही है। समूह बनाने का उद्देश्य समान की समान से तुलना है, ताकि बहुत अलग परिस्थितियों वाले छोटे पहाड़ी राज्यों को बड़े मैदानी राज्यों के सामने रैंक न किया जाए। "
  "कथन 2 गलत है: 2019 में पहली बार जारी सूचकांक दस क्षेत्रों को शामिल करता है: कृषि, वाणिज्य और उद्योग, मानव संसाधन, सार्वजनिक स्वास्थ्य, सार्वजनिक बुनियादी ढाँचा, आर्थिक शासन, सामाजिक कल्याण, न्यायिक और सार्वजनिक सुरक्षा, पर्यावरण, तथा नागरिक-केंद्रित शासन। "
  "कथन 3 गलत है: इसे प्रशासनिक सुधार और लोक शिकायत विभाग तैयार करता है।",
  "Department of Administrative Reforms and Public Grievances -- Good Governance Index.",
  "gov-good-governance-index", craft="inference")

S(GOV, "hard", "Mission Karmayogi seeks to shift civil-service capacity building from a 'rules-based' to a 'roles-based' approach, with continuous learning. Consider the following statements:",
  "मिशन कर्मयोगी सिविल सेवा क्षमता निर्माण को 'नियम-आधारित' से 'भूमिका-आधारित' दृष्टिकोण की ओर, निरंतर सीखने के साथ, ले जाना चाहता है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["Each post is to be mapped to the roles, activities and competencies it requires, and training planned to match.",
   "Officers are to keep learning through the iGOT Karmayogi online platform, not only at fixed points in their careers.",
   "The programme's apex body, the Public Human Resources Council, is chaired by the Cabinet Secretary.",
   "The programme replaces the induction training given at the national training academies."],
  ["हर पद को उसकी आवश्यक भूमिकाओं, गतिविधियों और दक्षताओं से जोड़ा जाना है, और प्रशिक्षण उसी के अनुसार नियोजित होना है।",
   "अधिकारियों को अपने करियर के कुछ निश्चित पड़ावों पर ही नहीं, बल्कि iGOT कर्मयोगी ऑनलाइन मंच से लगातार सीखते रहना है।",
   "कार्यक्रम की शीर्ष संस्था, लोक मानव संसाधन परिषद, की अध्यक्षता कैबिनेट सचिव करते हैं।",
   "कार्यक्रम राष्ट्रीय प्रशिक्षण अकादमियों में दिए जाने वाले प्रारंभिक प्रशिक्षण की जगह लेता है।"],
  C4, 1,
  "Statements 1 and 2 are correct, and both follow from the approach. A roles-based system maps each post to a Framework of Roles, Activities and Competencies (FRAC) and trains the officer for it. Continuous learning is delivered through the iGOT Karmayogi platform, owned by the not-for-profit company Karmayogi Bharat. "
  "Statement 3 is wrong: the Prime Minister's Public Human Resources Council is chaired by the Prime Minister; a Cabinet Secretary Coordination Unit monitors implementation, and the Capacity Building Commission helps approve departments' annual plans. Statement 4 is wrong: the programme, approved in 2020, adds to the academies' training rather than replacing it.",
  "कथन 1 और 2 सही हैं, और दोनों इसी दृष्टिकोण से निकलते हैं। भूमिका-आधारित व्यवस्था हर पद को भूमिकाओं, गतिविधियों और दक्षताओं के ढाँचे (FRAC) से जोड़ती है और अधिकारी को उसी के लिए प्रशिक्षित करती है। निरंतर सीखना iGOT कर्मयोगी मंच से होता है, जिसकी स्वामी ग़ैर-लाभकारी कंपनी कर्मयोगी भारत है। "
  "कथन 3 गलत है: प्रधानमंत्री की लोक मानव संसाधन परिषद की अध्यक्षता प्रधानमंत्री करते हैं; कैबिनेट सचिव समन्वय इकाई क्रियान्वयन की निगरानी करती है, और क्षमता निर्माण आयोग विभागों की वार्षिक योजनाओं की स्वीकृति में मदद करता है। कथन 4 गलत है: 2020 में स्वीकृत यह कार्यक्रम अकादमियों के प्रशिक्षण की जगह नहीं लेता, उसमें जुड़ता है।",
  "Department of Personnel and Training -- National Programme for Civil Services Capacity Building (Mission Karmayogi), 2020.",
  "governance-mission-karmayogi-structure", craft="inference")

S(GOV, "medium", "A farmer in a village, with no internet access at home, wants a copy of his land record and an income certificate. Consider the following statements:",
  "गाँव का एक किसान, जिसके घर में इंटरनेट नहीं है, अपने भूमि अभिलेख की प्रति और आय प्रमाण-पत्र चाहता है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["He can get both through a Common Services Centre run by a local entrepreneur in or near his village.",
   "The National e-Governance Plan was launched as part of the Digital India programme of 2015.",
   "Digital India replaced the Common Services Centres with direct online delivery to citizens."],
  ["वह अपने गाँव में या उसके पास किसी स्थानीय उद्यमी द्वारा चलाए जाने वाले कॉमन सर्विस सेंटर से दोनों प्राप्त कर सकता है।",
   "राष्ट्रीय ई-गवर्नेंस योजना 2015 के डिजिटल इंडिया कार्यक्रम के भाग के रूप में शुरू हुई थी।",
   "डिजिटल इंडिया ने कॉमन सर्विस सेंटरों की जगह नागरिकों को सीधी ऑनलाइन सेवा दे दी।"],
  C3, 0,
  "Only statement 1 is correct. Common Services Centres, run by village-level entrepreneurs, are the assisted access points for government e-services in rural areas. Certificates and land records were among the Mission Mode Projects of the National e-Governance Plan. "
  "Statement 2 reverses the order: the NeGP was approved in 2006, and Digital India (2015) built on it, carrying its projects forward as 'e-Kranti'. Statement 3 is wrong: Digital India expanded the CSC network under its public internet access pillar, because many citizens still need assisted access.",
  "केवल कथन 1 सही है। ग्राम-स्तरीय उद्यमियों द्वारा चलाए जाने वाले कॉमन सर्विस सेंटर ग्रामीण क्षेत्रों में सरकारी ई-सेवाओं के सहायता-प्राप्त पहुँच बिंदु हैं। प्रमाण-पत्र और भूमि अभिलेख राष्ट्रीय ई-गवर्नेंस योजना की मिशन मोड परियोजनाओं में थे। "
  "कथन 2 क्रम उलट देता है: राष्ट्रीय ई-गवर्नेंस योजना 2006 में स्वीकृत हुई, और डिजिटल इंडिया (2015) ने उस पर आगे काम करते हुए उसकी परियोजनाओं को 'ई-क्रांति' के रूप में आगे बढ़ाया। कथन 3 गलत है: डिजिटल इंडिया ने अपने सार्वजनिक इंटरनेट पहुँच स्तंभ के तहत CSC नेटवर्क का विस्तार किया, क्योंकि कई नागरिकों को अब भी सहायता-प्राप्त पहुँच चाहिए।",
  "Ministry of Electronics and Information Technology -- National e-Governance Plan, Digital India, CSC scheme.",
  "gov-negp-digital-india-csc", craft="application")

S(GOV, "hard", "A minister orally instructs a Secretary to cancel a contract. When the Secretary asks for written orders, he is transferred within four months of his posting. Consider the following statements in the light of the Supreme Court's judgment in T.S.R. Subramanian v. Union of India (2013):",
  "एक मंत्री एक सचिव को मौखिक रूप से एक अनुबंध रद्द करने का निर्देश देता है। जब सचिव लिखित आदेश माँगता है, तो उसकी तैनाती के चार महीने के भीतर उसका तबादला कर दिया जाता है। टी.एस.आर. सुब्रमण्यन बनाम भारत संघ (2013) में सर्वोच्च न्यायालय के निर्णय के आलोक में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Secretary was right to seek the instruction in writing before acting on it.",
   "The judgment called for a minimum fixed tenure and for transfers to be considered by a Civil Services Board.",
   "The judgment itself laid down a binding code on postings and transfers that replaced the service rules."],
  ["सचिव का उस पर कार्य करने से पहले निर्देश लिखित में माँगना सही था।",
   "निर्णय ने न्यूनतम निश्चित कार्यकाल और तबादलों पर सिविल सेवा बोर्ड द्वारा विचार की माँग की।",
   "निर्णय ने स्वयं तैनाती और तबादलों पर एक बाध्यकारी संहिता बनाई, जिसने सेवा नियमों की जगह ले ली।"],
  C3, 1,
  "Statements 1 and 2 are correct. The petition by retired civil servants argued that arbitrary transfers and oral orders were eroding the neutrality of the services. The Court said civil servants should not act on oral instructions except in emergencies, and then should record them as soon as possible. It directed a minimum fixed tenure and Civil Services Boards to recommend postings and transfers. "
  "Statement 3 is wrong: the Court did not legislate. It urged Parliament to enact a law regulating postings, transfers and disciplinary action, which has not yet been done.",
  "कथन 1 और 2 सही हैं। सेवानिवृत्त सिविल सेवकों की याचिका का तर्क था कि मनमाने तबादले और मौखिक आदेश सेवाओं की तटस्थता को कमज़ोर कर रहे हैं। न्यायालय ने कहा कि सिविल सेवक आपात स्थिति के सिवा मौखिक निर्देशों पर कार्य न करें, और तब भी उन्हें यथाशीघ्र दर्ज करें। उसने न्यूनतम निश्चित कार्यकाल और तैनाती व तबादलों की सिफ़ारिश के लिए सिविल सेवा बोर्डों का निर्देश दिया। "
  "कथन 3 गलत है: न्यायालय ने क़ानून नहीं बनाया। उसने संसद से तैनाती, तबादलों और अनुशासनात्मक कार्रवाई को नियमित करने वाला क़ानून बनाने का आग्रह किया, जो अभी तक नहीं बना है।",
  f"{SC} -- T.S.R. Subramanian v. Union of India (2013).",
  "gov-tsr-subramanian-civil-services", craft="application")

S(GOV, "medium", "Consider the following statements in the light of the Supreme Court's 2018 judgment on Aadhaar and the law since then:",
  "आधार पर सर्वोच्च न्यायालय के 2018 के निर्णय और उसके बाद के क़ानून के आलोक में निम्नलिखित कथनों पर विचार कीजिए:",
  ["A mobile company cannot insist on Aadhaar authentication as the only way of verifying a new customer.",
   "A private school can make an Aadhaar number compulsory for admission."],
  ["कोई मोबाइल कंपनी नए ग्राहक के सत्यापन के एकमात्र तरीक़े के रूप में आधार प्रमाणीकरण पर ज़ोर नहीं दे सकती।",
   "कोई निजी विद्यालय प्रवेश के लिए आधार संख्या अनिवार्य कर सकता है।"],
  T2, 0,
  "Only statement 1 is correct. In Justice K.S. Puttaswamy v. Union of India (2018), the Court upheld Aadhaar for subsidies and benefits paid from the Consolidated Fund and for linking with PAN. It struck down section 57, which had let private entities demand Aadhaar authentication under a contract. "
  "A 2019 amendment then allowed banks and telecom companies to use Aadhaar only with the customer's consent, alongside other documents, and barred denying a service to anyone who does not give it. The Court also held that Aadhaar cannot be made compulsory for school admission, so statement 2 is wrong.",
  "केवल कथन 1 सही है। न्यायमूर्ति के.एस. पुट्टस्वामी बनाम भारत संघ (2018) में न्यायालय ने संचित निधि से दी जाने वाली सब्सिडी और लाभों तथा PAN से जोड़ने के लिए आधार को वैध ठहराया। उसने धारा 57 रद्द की, जो निजी संस्थाओं को अनुबंध के आधार पर आधार प्रमाणीकरण माँगने देती थी। "
  "फिर 2019 के एक संशोधन ने बैंकों और दूरसंचार कंपनियों को ग्राहक की सहमति से ही, अन्य दस्तावेज़ों के साथ, आधार का उपयोग करने दिया, और उसे न देने वाले को सेवा से वंचित करने पर रोक लगाई। न्यायालय ने यह भी कहा कि विद्यालय में प्रवेश के लिए आधार अनिवार्य नहीं किया जा सकता, इसलिए कथन 2 गलत है।",
  f"{SC} -- Justice K.S. Puttaswamy v. Union of India (Aadhaar, 2018); Aadhaar and Other Laws (Amendment) Act, 2019.",
  "gov-aadhaar-uidai-section-57", craft="application")

S(GOV, "medium", "Consider the following choices made by Members of Parliament under the Members of Parliament Local Area Development Scheme (MPLADS):",
  "सांसद स्थानीय क्षेत्र विकास योजना (MPLADS) के तहत सांसदों द्वारा किए गए निम्नलिखित चयनों पर विचार कीजिए:",
  ["A nominated member of the Rajya Sabha selects a district in a State of her choice as her nodal district.",
   "An elected member of the Rajya Sabha from Bihar selects a district of Uttar Pradesh as his nodal district.",
   "A Lok Sabha member recommends works worth ₹5 crore in a year within his own constituency."],
  ["राज्यसभा की एक मनोनीत सदस्य अपनी पसंद के किसी राज्य का एक ज़िला अपने नोडल ज़िले के रूप में चुनती है।",
   "बिहार से निर्वाचित राज्यसभा का एक सदस्य उत्तर प्रदेश का एक ज़िला अपने नोडल ज़िले के रूप में चुनता है।",
   "लोकसभा का एक सदस्य एक वर्ष में अपने निर्वाचन क्षेत्र के भीतर ₹5 करोड़ के कार्यों की सिफ़ारिश करता है।"],
  None, 0,
  "Choices 1 and 3 are permitted. Each MP is entitled to recommend works worth up to ₹5 crore a year. A Lok Sabha member recommends them in his constituency, and an elected Rajya Sabha member in one or more districts of the State from which he was elected. A nominated member of the Rajya Sabha may choose any one district in the country as the nodal district. "
  "So the Bihar member in case 2 must choose a district in Bihar. The scheme is administered by the Ministry of Statistics and Programme Implementation, and the works must create durable community assets.",
  "चयन 1 और 3 अनुमत हैं। हर सांसद एक वर्ष में ₹5 करोड़ तक के कार्यों की सिफ़ारिश का हक़दार है। लोकसभा सदस्य अपने निर्वाचन क्षेत्र में, और निर्वाचित राज्यसभा सदस्य उस राज्य के एक या अधिक ज़िलों में सिफ़ारिश करता है जहाँ से वह निर्वाचित हुआ। राज्यसभा का मनोनीत सदस्य देश का कोई एक ज़िला नोडल ज़िले के रूप में चुन सकता है। "
  "इसलिए मामले 2 के बिहार के सदस्य को बिहार का ही ज़िला चुनना होगा। योजना का प्रशासन सांख्यिकी और कार्यक्रम क्रियान्वयन मंत्रालय करता है, और कार्यों से टिकाऊ सामुदायिक परिसंपत्तियाँ बननी चाहिए।",
  "Ministry of Statistics and Programme Implementation -- MPLADS Guidelines, 2023.",
  "governance-mplads-entitlement-rules", opts=["1 and 3 only", "1 only", "2 and 3 only", "1, 2 and 3"],
  opts_hi=["केवल 1 और 3", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
  closing="Which of the above choices are permitted under the scheme?", closing_hi="उपर्युक्त में से कौन-से चयन योजना के तहत अनुमत हैं?", craft="application")

S(GOV, "medium", "Ten poor women in a village form a self-help group and want credit to start a small dairy. Consider the following statements:",
  "एक गाँव की दस ग़रीब महिलाएँ एक स्वयं सहायता समूह बनाती हैं और एक छोटी डेयरी शुरू करने के लिए ऋण चाहती हैं। निम्नलिखित कथनों पर विचार कीजिए:",
  ["A bank can lend to the group as a whole without asking for collateral, up to a prescribed limit.",
   "The group can be supported under the Deendayal Antyodaya Yojana-National Rural Livelihoods Mission, which is implemented by the Ministry of Rural Development.",
   "The group must first register as a co-operative society before a bank can lend to it."],
  ["कोई बैंक एक निर्धारित सीमा तक बिना संपार्श्विक माँगे पूरे समूह को ऋण दे सकता है।",
   "समूह को दीनदयाल अंत्योदय योजना-राष्ट्रीय ग्रामीण आजीविका मिशन के तहत सहायता मिल सकती है, जिसे ग्रामीण विकास मंत्रालय लागू करता है।",
   "बैंक के ऋण देने से पहले समूह को सहकारी समिति के रूप में पंजीकृत होना होगा।"],
  C3, 1,
  "Statements 1 and 2 are correct. Under the SHG-Bank Linkage Programme, which began as a NABARD pilot in 1992, banks lend to the group on the strength of its savings record and its members' joint responsibility, without collateral up to a limit set by the Reserve Bank. "
  "DAY-NRLM, launched as 'Aajeevika' in 2011 under the Ministry of Rural Development, organises poor rural women into such groups and gives them revolving funds, interest subvention and links to markets. "
  "Statement 3 is wrong: a self-help group is an informal body. It needs no registration to open a savings account and borrow, which is precisely why the model reached the very poor.",
  "कथन 1 और 2 सही हैं। 1992 में NABARD की प्रायोगिक परियोजना के रूप में शुरू हुए SHG-बैंक लिंकेज कार्यक्रम के तहत बैंक समूह के बचत रिकॉर्ड और सदस्यों की संयुक्त ज़िम्मेदारी के आधार पर, रिज़र्व बैंक द्वारा तय सीमा तक बिना संपार्श्विक के, ऋण देते हैं। "
  "ग्रामीण विकास मंत्रालय के तहत 2011 में 'आजीविका' के रूप में शुरू हुआ DAY-NRLM ग़रीब ग्रामीण महिलाओं को ऐसे समूहों में संगठित करता है और उन्हें परिक्रामी निधि, ब्याज सहायता और बाज़ार से जुड़ाव देता है। "
  "कथन 3 गलत है: स्वयं सहायता समूह एक अनौपचारिक निकाय है। उसे बचत खाता खोलने और ऋण लेने के लिए पंजीकरण की ज़रूरत नहीं, और ठीक इसी कारण यह मॉडल बहुत ग़रीब लोगों तक पहुँचा।",
  "Ministry of Rural Development -- DAY-NRLM; NABARD -- SHG-Bank Linkage Programme.",
  "gov-shg-nrlm-linkage", craft="application")

S(PR, "easy", "A 22-year-old woman's name is on the electoral roll of her village. Consider the following statements:",
  "एक 22 वर्षीय महिला का नाम उसके गाँव की निर्वाचक नामावली में है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["She can contest the election to her village Panchayat.",
   "She can contest the election to the State Legislative Assembly from her area."],
  ["वह अपनी ग्राम पंचायत का चुनाव लड़ सकती है।",
   "वह अपने क्षेत्र से राज्य विधानसभा का चुनाव लड़ सकती है।"],
  T2, 0,
  "Only statement 1 is correct. Under Article 243F, anyone qualified to be elected to the State Legislature is qualified for a Panchayat, with one change: the minimum age is 21, not 25. "
  "She cannot yet contest the Assembly election, for which Article 173 requires the age of 25. The 73rd Amendment, 1992, which gave Panchayats constitutional status, lowered the age so that more young people could enter local government.",
  "केवल कथन 1 सही है। अनुच्छेद 243F के तहत जो व्यक्ति राज्य विधानमंडल के लिए निर्वाचित होने योग्य है, वह पंचायत के लिए भी योग्य है, केवल एक अंतर के साथ: न्यूनतम आयु 25 नहीं, 21 वर्ष है। "
  "वह अभी विधानसभा चुनाव नहीं लड़ सकती, जिसके लिए अनुच्छेद 173 25 वर्ष की आयु माँगता है। पंचायतों को संवैधानिक दर्जा देने वाले 73वें संशोधन, 1992 ने आयु कम रखी ताकि अधिक युवा स्थानीय शासन में आ सकें।",
  f"{COI} -- Articles 173 and 243F.",
  "panchayat-constitutional-status-age-easy", craft="application")

S(PR, "medium", "The Governor has notified a city region of 12 lakh people, spread over two municipalities, as a metropolitan area. The larger municipality has 9 lakh residents. Consider the following statements:",
  "राज्यपाल ने दो नगरपालिकाओं में फैले 12 लाख लोगों वाले एक नगर क्षेत्र को महानगर क्षेत्र अधिसूचित किया है। बड़ी नगरपालिका में 9 लाख निवासी हैं। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The larger municipality must constitute Wards Committees.",
   "A Metropolitan Planning Committee must be constituted for the region.",
   "At least two-thirds of the members of that Committee must be elected by and from the elected members of the municipalities and the chairpersons of the Panchayats in the area."],
  ["बड़ी नगरपालिका को वार्ड समितियाँ बनानी होंगी।",
   "इस क्षेत्र के लिए महानगर योजना समिति बनानी होगी।",
   "उस समिति के कम से कम दो-तिहाई सदस्य क्षेत्र की नगरपालिकाओं के निर्वाचित सदस्यों और पंचायतों के अध्यक्षों द्वारा उन्हीं में से चुने जाने चाहिए।"],
  C3, 2,
  "All three are correct. Wards Committees are compulsory in every municipality with a population of three lakh or more. A Metropolitan Planning Committee is required for every metropolitan area, which the 74th Amendment defines as an area of ten lakh or more, in one or more districts, with two or more municipalities or Panchayats, notified by the Governor. "
  "Article 243ZE requires that not less than two-thirds of its members be elected in this way, in proportion to the urban and rural populations of the area, so that planning for the region stays in the hands of elected local bodies.",
  "तीनों कथन सही हैं। तीन लाख या अधिक आबादी वाली हर नगरपालिका में वार्ड समितियाँ अनिवार्य हैं। हर महानगर क्षेत्र के लिए महानगर योजना समिति आवश्यक है; 74वाँ संशोधन महानगर क्षेत्र को दस लाख या अधिक आबादी वाले, एक या अधिक ज़िलों में फैले, दो या अधिक नगरपालिकाओं या पंचायतों वाले और राज्यपाल द्वारा अधिसूचित क्षेत्र के रूप में परिभाषित करता है। "
  "अनुच्छेद 243ZE अपेक्षा करता है कि इसके कम से कम दो-तिहाई सदस्य इसी तरह, क्षेत्र की शहरी और ग्रामीण आबादी के अनुपात में, चुने जाएँ, ताकि क्षेत्र का नियोजन निर्वाचित स्थानीय निकायों के हाथ में रहे।",
  f"{COI} -- Articles 243P, 243S and 243ZE.",
  "panchayat-74th-wards-mpc-term", craft="application")

S(PR, "medium", "A State has a population of 18 lakh. Consider the following statements:",
  "एक राज्य की आबादी 18 लाख है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["It may choose not to constitute Panchayats at the intermediate level.",
   "Its village Panchayat chairpersons must be directly elected by the voters.",
   "Its Panchayat elections are conducted by the Election Commission of India."],
  ["वह मध्यवर्ती स्तर पर पंचायतें न बनाने का विकल्प चुन सकता है।",
   "उसकी ग्राम पंचायतों के अध्यक्षों का मतदाताओं द्वारा प्रत्यक्ष निर्वाचन अनिवार्य है।",
   "उसके पंचायत चुनाव भारत निर्वाचन आयोग कराता है।"],
  C3, 0,
  "Only statement 1 is correct. Article 243B(2) lets a State with a population not exceeding 20 lakh do without the intermediate (block) tier, which is why small States such as Goa and Sikkim have two tiers. "
  "Statement 2 is wrong: Article 243C(5) leaves the manner of electing the village Panchayat chairperson to State law, so it may be direct or indirect; only the intermediate and district chairpersons must be elected by and from the elected members. "
  "Statement 3 is wrong: Panchayat elections are conducted by the State Election Commission under Article 243K.",
  "केवल कथन 1 सही है। अनुच्छेद 243B(2) 20 लाख से अधिक आबादी न रखने वाले राज्य को मध्यवर्ती (प्रखंड) स्तर के बिना काम चलाने देता है, इसीलिए गोवा और सिक्किम जैसे छोटे राज्यों में दो स्तर हैं। "
  "कथन 2 गलत है: अनुच्छेद 243C(5) ग्राम पंचायत अध्यक्ष के निर्वाचन का तरीक़ा राज्य क़ानून पर छोड़ता है, इसलिए वह प्रत्यक्ष या अप्रत्यक्ष हो सकता है; केवल मध्यवर्ती और ज़िला स्तर के अध्यक्ष निर्वाचित सदस्यों द्वारा उन्हीं में से चुने जाने चाहिए। "
  "कथन 3 गलत है: पंचायत चुनाव अनुच्छेद 243K के तहत राज्य निर्वाचन आयोग कराता है।",
  f"{COI} -- Articles 243B, 243C and 243K.",
  "panchayat-73rd-gram-sabha-tiers-chair", craft="application")

S(PR, "hard", "A company wants to acquire land and obtain a prospecting licence for a minor mineral in a Fifth Schedule area. Consider the following statements in the light of the Provisions of the Panchayats (Extension to the Scheduled Areas) Act, 1996:",
  "एक कंपनी पाँचवीं अनुसूची के एक क्षेत्र में भूमि अधिग्रहण करना और एक गौण खनिज का पूर्वेक्षण लाइसेंस लेना चाहती है। पंचायत उपबंध (अनुसूचित क्षेत्रों पर विस्तार) अधिनियम, 1996 के आलोक में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Gram Sabha or the Panchayat at the appropriate level must be consulted before the land is acquired.",
   "The prior recommendation of the Gram Sabha or the Panchayat at the appropriate level is mandatory before the licence is granted.",
   "The chairpersons of the Panchayats in the area must belong to the Scheduled Tribes.",
   "The matter would be decided by an autonomous district council, since the area is a Scheduled Area."],
  ["भूमि अधिग्रहण से पहले ग्राम सभा या उपयुक्त स्तर की पंचायत से परामर्श अनिवार्य है।",
   "लाइसेंस देने से पहले ग्राम सभा या उपयुक्त स्तर की पंचायत की पूर्व सिफ़ारिश अनिवार्य है।",
   "क्षेत्र की पंचायतों के अध्यक्ष अनुसूचित जनजातियों के होने चाहिए।",
   "यह विषय एक स्वायत्त ज़िला परिषद तय करेगी, क्योंकि क्षेत्र अनुसूचित क्षेत्र है।"],
  C4, 2,
  "Statements 1, 2 and 3 are correct under section 4 of PESA. The Gram Sabha or the appropriate Panchayat must be consulted before land is acquired for development projects and before people are resettled. Its prior recommendation is mandatory for prospecting licences and mining leases for minor minerals. All chairperson posts in Panchayats in Scheduled Areas are reserved for the Scheduled Tribes. "
  "Statement 4 is wrong: autonomous district councils belong to the Sixth Schedule areas of the North-East. Fifth Schedule areas are governed through PESA's Gram Sabhas and Panchayats, with the Governor's special powers in the background.",
  "PESA की धारा 4 के तहत कथन 1, 2 और 3 सही हैं। विकास परियोजनाओं के लिए भूमि अधिग्रहण से पहले और लोगों के पुनर्वास से पहले ग्राम सभा या उपयुक्त पंचायत से परामर्श अनिवार्य है। गौण खनिजों के पूर्वेक्षण लाइसेंस और खनन पट्टों के लिए उसकी पूर्व सिफ़ारिश अनिवार्य है। अनुसूचित क्षेत्रों की पंचायतों में अध्यक्ष के सभी पद अनुसूचित जनजातियों के लिए आरक्षित हैं। "
  "कथन 4 गलत है: स्वायत्त ज़िला परिषदें पूर्वोत्तर के छठी अनुसूची वाले क्षेत्रों की हैं। पाँचवीं अनुसूची के क्षेत्रों का शासन PESA की ग्राम सभाओं और पंचायतों से होता है, और पृष्ठभूमि में राज्यपाल की विशेष शक्तियाँ रहती हैं।",
  "Provisions of the Panchayats (Extension to the Scheduled Areas) Act, 1996, section 4.",
  "panchayat-pesa-1996-provisions", craft="application")

# ================================================================ TAGS for the 78 kept rows (Test 21's 5 are tagged already)
TAGS = {
 "fed-divisible-pool-net-proceeds": "linkage", "federalism-art254-repugnancy-presidential-assent": "linkage", "fed-art355-deployment": "precision",
 "fed-rajya-sabha-unequal-representation": "linkage", "fed-intergovernmental-bodies-chairs-pairs": "recall", "fed-special-provisions-371c-371j-pairs": "recall",
 "fed-union-territories-pairs": "recall", "federalism-special-provision-articles-pairs": "recall", "fed-first-presidents-rule-punjab": "recall",
 "federalism-art268-stamp-duties": "precision", "federalism-centre-state-commissions": "recall", "fed-three-lists-easy": "recall",
 "fed-art365-356-rameshwar-prasad": "precision", "fed-full-faith-credit-261": "precision", "fed-sarkaria-punchhi-recommendations": "precision",
 "fed-sixth-schedule-coverage": "precision", "fed-state-borrowing-293": "precision", "federalism-emergency-effects-358-359-360": "precision",
 "federalism-gst-council-mohit-minerals": "precision", "federalism-sixth-schedule-district-councils": "precision", "fed-delhi-services-2023": "precision",
 "fed-fifth-schedule-governor-president": "precision", "fed-grants-275-282": "precision", "fed-jammu-kashmir-2019-2024": "recall",
 "fed-special-provisions-371-371a-371b": "precision", "fed-trade-commerce-301-304": "precision", "federalism-administrative-relations-256-258": "precision",
 "federalism-inter-state-water-disputes-art262": "precision", "federalism-legislative-relations-248-249-253": "precision", "federalism-national-emergency-approval": "precision",
 "federalism-presidents-rule-art356": "precision",
 "gov-lateral-entry-contract": "linkage", "governance-cbi-state-consent-police-state-subject": "linkage", "gov-aadhaar-not-citizenship": "linkage",
 "gov-dbt-leakages-direct-credit": "precision", "gov-egovernance-grievance-redress": "inference", "governance-vb-g-ram-g-act-2025": "precision",
 "gov-digital-systems-pairs": "recall", "gov-indices-bodies-pairs": "recall", "gov-programmes-ministries-pairs": "recall",
 "governance-regulators-parent-ministries": "recall", "gov-freedom-of-information-2002": "recall", "governance-right-to-public-services-first-state": "recall",
 "gov-aspirational-districts-niti": "recall", "gov-good-governance-day": "recall", "governance-pragati-review-platform": "recall",
 "gov-shg-mygov-easy": "recall", "governance-digilocker-legal-status": "recall", "gov-cert-in-nciipc": "precision",
 "gov-civil-servant-310-311-conduct": "precision", "gov-cooperatives-ministry-part-ixb": "precision", "gov-niti-aayog-structure": "precision",
 "gov-social-audit": "precision", "governance-nia-jurisdiction-consent": "precision", "gov-civil-services-day": "recall",
 "gov-direct-benefit-transfer": "recall", "gov-ecourts-njdg": "recall", "gov-gem-procurement": "precision",
 "governance-administrative-reforms-commissions": "recall", "governance-cabinet-secretariat-art77": "precision", "polity-all-india-services-art312": "precision",
 "panchayat-243m-exempted-states": "linkage", "panchayat-dissolution-reconstitution-243e": "precision", "panchayat-part-ix-articles-pairs": "recall",
 "panchayat-wards-committees-243s": "recall", "panchayat-ashok-mehta-two-tier": "recall", "panchayat-state-finance-commission-243i": "recall",
 "panchayat-finances-243h-243j": "precision", "panchayat-gram-nyayalayas": "precision", "panchayat-73rd-amendment-reservations": "precision",
 "panchayat-74th-amendment-dpc": "precision", "panchayat-balwantrai-nagaur": "recall", "panchayat-state-election-commissioner": "precision"}

if __name__ == "__main__":
    write_updates("upg_l2_t04_polity.sql", statuses=("draft", "published"), tags=TAGS)
