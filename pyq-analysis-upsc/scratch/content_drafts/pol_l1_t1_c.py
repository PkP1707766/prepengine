# -*- coding: utf-8 -*-
"""Level 1 · Test 1 (Polity, NCERT Foundation) -- part C: Governance (12) and Statutory-Laws (10).
22 new bilingual rows on the Level-1 cell targets:
  Governance: easy MCQ 1, easy statement 2, easy Statement-I/II 1, medium MCQ 1, medium statement 4,
    medium Statement-I/II 1, medium pairs 1, hard statement 1.
  Statutory-Laws: easy MCQ 1, easy statement 2, easy Statement-I/II 1, medium MCQ 1, medium statement 3,
    medium Statement-I/II 1, hard statement 1.
NCERT's angle on governance -- the outcomes of democracy, planning and the Kerala model, public facilities,
pressure groups and party systems, the ombudsman -- and on law: the laws that NCERT uses to show how law
meets social justice (succession, child and bonded labour, manual scavenging, atrocities, forest rights,
land acquisition, Bhopal). The Level-2 rows on schemes, digital services, NITI Aayog's structure, the
Lokpal's structure, RTI, consumer protection, dowry and senior citizens are not repeated."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Polity"
d.REQUIRE_CRAFT = True
GV = "Governance"
SL = "Statutory-Laws"
DP10 = "NCERT Class X, Democratic Politics -- II"
NC12 = "NCERT Class XII, Political Science -- Politics in India since Independence"
SPL8 = "NCERT Class VIII, Social and Political Life -- III"
FIVE = ["Only two", "Only three", "Only four", "All five"]
FIVE_HI = ["केवल दो", "केवल तीन", "केवल चार", "सभी पाँच"]

# ================================================================ GOVERNANCE (12)
M(GV, "easy", "In the context of democratic government, 'transparency' means that:",
  "लोकतांत्रिक शासन के संदर्भ में 'पारदर्शिता' का अर्थ है कि:",
  ["citizens have the right and the means to check that decisions follow the correct procedure",
   "every decision of the government is taken by a vote of all the citizens of the country in a referendum",
   "the government publishes its budget once a year and need not explain any other decision to the people",
   "ministers hold their meetings in public so that every citizen can attend them and take part in the vote"],
  ["नागरिकों के पास यह जाँचने का अधिकार और साधन हों कि निर्णय सही प्रक्रिया से लिए गए या नहीं",
   "सरकार का हर निर्णय जनमत संग्रह में देश के सभी नागरिकों के मतदान से लिया जाता है",
   "सरकार साल में एक बार अपना बजट प्रकाशित करती है और किसी और निर्णय पर जनता को सफ़ाई देने की ज़रूरत नहीं",
   "मंत्री अपनी बैठकें सार्वजनिक रूप से करते हैं ताकि हर नागरिक उनमें आए और मतदान में भाग ले"],
  0,
  "Transparency is the openness of the decision-making process: a citizen who wants to know whether a decision was taken according to the rules can find out, because there is a right and a means to examine the process. It is one of the outcomes expected of democratic government, alongside accountability and responsiveness. "
  "It does not require every decision to be put to a referendum or every meeting to be held in public, and publishing a budget alone does not make the rest of government open.",
  "पारदर्शिता निर्णय-प्रक्रिया का खुलापन है: जो नागरिक जानना चाहे कि कोई निर्णय नियमों के अनुसार लिया गया या नहीं, वह पता लगा सकता है, क्योंकि प्रक्रिया की जाँच का अधिकार और साधन मौजूद हैं। जवाबदेही और संवेदनशीलता के साथ यह लोकतांत्रिक शासन से अपेक्षित परिणामों में से एक है। "
  "इसके लिए हर निर्णय को जनमत संग्रह में रखना या हर बैठक सार्वजनिक रूप से करना ज़रूरी नहीं, और केवल बजट प्रकाशित करने से बाकी शासन खुला नहीं हो जाता।",
  f"{DP10}, Chapter 7 (Outcomes of Democracy).",
  "l1-pol-transparency-meaning", craft="precision")

S(GV, "easy", "Consider the following statements about the outcomes of democracy:",
  "लोकतंत्र के परिणामों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Democracies have done better at producing accountable, responsive and legitimate government than at reducing economic inequality.",
   "Democracy guarantees a faster rate of economic growth than dictatorship.",
   "Democracy allows citizens to correct the mistakes of a government through elections and public debate."],
  ["लोकतंत्रों ने आर्थिक असमानता घटाने की तुलना में जवाबदेह, संवेदनशील और वैध सरकार देने में बेहतर काम किया है।",
   "लोकतंत्र तानाशाही की तुलना में तेज़ आर्थिक विकास की गारंटी देता है।",
   "लोकतंत्र नागरिकों को चुनावों और सार्वजनिक बहस के माध्यम से सरकार की ग़लतियाँ सुधारने देता है।"],
  C3, 1,
  "Statements 1 and 3 are correct. The evidence NCERT discusses shows democracies doing well on accountability, responsiveness and legitimacy, while poverty and inequality persist in many of them. "
  "And the great strength of democracy is that mistakes can be corrected -- a government can be questioned in public and replaced at the next election. "
  "Statement 2 is wrong: on the data for 1950-2000, dictatorships grew slightly faster on average; democracy is preferred for other reasons, not because it guarantees faster growth.",
  "कथन 1 और 3 सही हैं। एनसीईआरटी जिन साक्ष्यों पर चर्चा करता है वे दिखाते हैं कि लोकतंत्र जवाबदेही, संवेदनशीलता और वैधता में अच्छे रहे हैं, जबकि उनमें से कई में ग़रीबी और असमानता बनी हुई है। "
  "और लोकतंत्र की बड़ी ताक़त यह है कि ग़लतियाँ सुधारी जा सकती हैं -- सरकार से सार्वजनिक रूप से प्रश्न पूछे जा सकते हैं और अगले चुनाव में उसे बदला जा सकता है। "
  "कथन 2 गलत है: 1950-2000 के आँकड़ों पर तानाशाहियों की औसत वृद्धि थोड़ी तेज़ रही; लोकतंत्र को दूसरे कारणों से पसंद किया जाता है, इसलिए नहीं कि वह तेज़ वृद्धि की गारंटी देता है।",
  f"{DP10}, Chapter 7 (Outcomes of Democracy).",
  "l1-pol-outcomes-of-democracy", craft="inference")

S(GV, "easy", "Consider the following statements about pressure groups:",
  "दबाव समूहों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Pressure groups try to influence government policy without themselves seeking to form the government.",
   "A pressure group that begins to contest elections in order to win power remains a pressure group."],
  ["दबाव समूह स्वयं सरकार बनाने की कोशिश किए बिना सरकार की नीति को प्रभावित करने का प्रयास करते हैं।",
   "सत्ता पाने के लिए चुनाव लड़ना शुरू करने वाला दबाव समूह दबाव समूह ही बना रहता है।"],
  T2, 0,
  "Only statement 1 is correct. Trade unions, business associations, farmers' organisations and other interest groups press their demands on the government -- through petitions, campaigns and lobbying -- but do not aim to take power. "
  "Statement 2 is wrong: seeking power through elections is what defines a political party, so a group that does so has become a party, even if it grew out of a movement or an interest group.",
  "केवल कथन 1 सही है। श्रमिक संघ, व्यापारिक संघ, किसान संगठन और अन्य हित समूह याचिकाओं, अभियानों और पैरवी के माध्यम से सरकार पर अपनी माँगों का दबाव डालते हैं -- पर सत्ता लेने का लक्ष्य नहीं रखते। "
  "कथन 2 गलत है: चुनावों के माध्यम से सत्ता पाना ही राजनीतिक दल की पहचान है, इसलिए ऐसा करने वाला समूह दल बन चुका है, भले ही वह किसी आंदोलन या हित समूह से निकला हो।",
  f"{DP10} (Political Parties; pressure groups and movements).",
  "l1-pol-pressure-groups-vs-parties", craft="precision")

A(GV, "easy",
  "Democratic governments usually reach decisions faster than non-democratic ones.",
  "लोकतांत्रिक सरकारें सामान्यतः अलोकतांत्रिक सरकारों से जल्दी निर्णय लेती हैं।",
  "Democracy rests on deliberation and negotiation among different points of view.",
  "लोकतंत्र अलग-अलग दृष्टिकोणों के बीच विचार-विमर्श और बातचीत पर टिका होता है।",
  3,
  "Statement-I is incorrect and Statement-II is correct. Because decisions in a democracy pass through discussion, consultation and the institutions that represent different interests, they usually take longer than in a non-democratic government -- Statement-II is the reason Statement-I is false. "
  "NCERT's point is that the delay buys something: decisions reached this way are more acceptable to the people and so more likely to be effective.",
  "कथन-I गलत है और कथन-II सही है। लोकतंत्र में निर्णय चर्चा, परामर्श और अलग-अलग हितों का प्रतिनिधित्व करने वाली संस्थाओं से गुज़रते हैं, इसलिए उनमें प्रायः अलोकतांत्रिक सरकार से अधिक समय लगता है -- कथन-II ही वह कारण है जिससे कथन-I गलत है। "
  "एनसीईआरटी का कहना है कि इस देरी का मोल मिलता है: इस तरह लिए गए निर्णय जनता को अधिक स्वीकार्य होते हैं और इसलिए अधिक प्रभावी होने की संभावना रखते हैं।",
  f"{DP10}, Chapter 7 (Outcomes of Democracy).",
  "l1-pol-democracy-slower-deliberation", craft="inference")

M(GV, "medium", "Which one of the following best describes the 'Kerala model' of development?",
  "निम्नलिखित में से कौन-सा विकास के 'केरल मॉडल' का सबसे अच्छा वर्णन करता है?",
  ["High levels of literacy and health achieved at a modest income, through public action",
   "Rapid industrial growth led by private investment in heavy industry and large export zones",
   "Development based mainly on large dams, big irrigation projects and capital-intensive farming",
   "Growth driven by foreign capital, with the State withdrawing from education and public health"],
  ["सार्वजनिक प्रयासों से मामूली आय पर साक्षरता और स्वास्थ्य के ऊँचे स्तर प्राप्त करना",
   "भारी उद्योग और बड़े निर्यात क्षेत्रों में निजी निवेश के नेतृत्व में तेज़ औद्योगिक वृद्धि",
   "मुख्यतः बड़े बाँधों, बड़ी सिंचाई परियोजनाओं और पूँजी-प्रधान खेती पर आधारित विकास",
   "विदेशी पूँजी से संचालित वृद्धि, जिसमें राज्य शिक्षा और सार्वजनिक स्वास्थ्य से हट जाए"],
  0,
  "Kerala reached levels of literacy, life expectancy and infant survival close to those of much richer societies while its income was modest, through investment in education and health, land reform, effective food distribution and, later, decentralised planning through the panchayats. "
  "NCERT discusses it as an alternative to development measured only by industrial growth or big projects; the other options describe industry-led, project-led or market-led strategies.",
  "केरल ने मामूली आय के बावजूद साक्षरता, जीवन-प्रत्याशा और शिशु जीवन-रक्षा के ऐसे स्तर पाए जो कहीं अधिक समृद्ध समाजों के निकट हैं -- शिक्षा और स्वास्थ्य में निवेश, भूमि सुधार, प्रभावी खाद्य वितरण और बाद में पंचायतों के माध्यम से विकेंद्रीकृत नियोजन द्वारा। "
  "एनसीईआरटी इसे केवल औद्योगिक वृद्धि या बड़ी परियोजनाओं से मापे जाने वाले विकास के विकल्प के रूप में देखता है; बाकी विकल्प उद्योग, परियोजना या बाज़ार के नेतृत्व वाली रणनीतियों का वर्णन करते हैं।",
  f"{NC12}, Chapter 3 (Politics of Planned Development).",
  "l1-pol-kerala-model", pos=3, craft="precision")

S(GV, "medium", "Consider the following statements about planning in India:",
  "भारत में नियोजन के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The First Five-Year Plan gave priority to agriculture, including irrigation.",
   "The Second Five-Year Plan, drawn up on the Mahalanobis model, stressed heavy industry.",
   "The Planning Commission was chaired by the Prime Minister."],
  ["पहली पंचवर्षीय योजना ने सिंचाई सहित कृषि को प्राथमिकता दी।",
   "महालनोबिस मॉडल पर बनी दूसरी पंचवर्षीय योजना ने भारी उद्योग पर बल दिया।",
   "योजना आयोग की अध्यक्षता प्रधानमंत्री करते थे।"],
  C3, 2,
  "All three statements are correct. The First Plan (1951-56), facing food shortages after Partition, put the largest share into agriculture, irrigation and power -- the years of the Bhakra-Nangal project. "
  "The Second Plan (1956-61), shaped by P.C. Mahalanobis, shifted the stress to heavy and capital-goods industries in the public sector. Throughout its life, from 1950 to 2014, the Planning Commission had the Prime Minister as its chairperson.",
  "तीनों कथन सही हैं। विभाजन के बाद खाद्य संकट से जूझती पहली योजना (1951-56) ने सबसे बड़ा हिस्सा कृषि, सिंचाई और बिजली को दिया -- यही भाखड़ा-नांगल परियोजना के वर्ष थे। "
  "पी.सी. महालनोबिस द्वारा रूपित दूसरी योजना (1956-61) ने ज़ोर सार्वजनिक क्षेत्र के भारी और पूँजीगत वस्तु उद्योगों पर कर दिया। 1950 से 2014 तक अपने पूरे जीवनकाल में योजना आयोग के अध्यक्ष प्रधानमंत्री रहे।",
  f"{NC12}, Chapter 3 (Politics of Planned Development).",
  "l1-pol-first-second-plans", craft="recall")

S(GV, "medium", "Consider the following statements about public facilities such as water and sanitation:",
  "जल और स्वच्छता जैसी सार्वजनिक सुविधाओं के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The government is expected to provide them because private suppliers may not serve everyone at an affordable price.",
   "Once a government contracts a private company to supply water, it has no further responsibility for the supply.",
   "Large differences in access to water between the rich and poor localities of a city go against the idea of equality in public provision."],
  ["सरकार से इन्हें उपलब्ध कराने की अपेक्षा की जाती है क्योंकि निजी आपूर्तिकर्ता हर किसी को किफ़ायती दाम पर सेवा न दें, ऐसा हो सकता है।",
   "जल आपूर्ति के लिए किसी निजी कंपनी से अनुबंध करने के बाद सरकार की आपूर्ति के प्रति कोई ज़िम्मेदारी नहीं रहती।",
   "किसी शहर के अमीर और ग़रीब इलाकों के बीच जल की उपलब्धता में बड़े अंतर सार्वजनिक प्रावधान में समानता के विचार के विरुद्ध हैं।"],
  C3, 1,
  "Statements 1 and 3 are correct. Facilities such as water, sanitation, health care and public transport are needed by everyone, and a private supplier aiming at profit may price the poor out of them, so the government is expected to ensure them. "
  "NCERT's Chennai example shows how unequal the supply can be within one city, which runs against the idea that public facilities should reach all equally. "
  "Statement 2 is wrong: a government may involve private firms in parts of the work, but it remains responsible for ensuring that the facility reaches everyone at an affordable price.",
  "कथन 1 और 3 सही हैं। जल, स्वच्छता, स्वास्थ्य सेवा और सार्वजनिक परिवहन जैसी सुविधाएँ सबको चाहिए, और मुनाफ़े के लक्ष्य वाला निजी आपूर्तिकर्ता ग़रीबों को उनसे बाहर कर सकता है, इसलिए सरकार से इन्हें सुनिश्चित करने की अपेक्षा है। "
  "एनसीईआरटी का चेन्नई उदाहरण दिखाता है कि एक ही शहर में आपूर्ति कितनी असमान हो सकती है, जो इस विचार के विरुद्ध है कि सार्वजनिक सुविधाएँ सब तक बराबर पहुँचें। "
  "कथन 2 गलत है: सरकार काम के कुछ हिस्सों में निजी कंपनियों को शामिल कर सकती है, पर सुविधा को किफ़ायती दाम पर सब तक पहुँचाने की ज़िम्मेदारी उसी की रहती है।",
  f"{SPL8}, Chapter 8 (Public Facilities).",
  "l1-pol-public-facilities-responsibility", craft="inference")

S(GV, "medium", "Consider the following statements about the institution of the ombudsman:",
  "लोकपाल (ओम्बड्समैन) संस्था के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The office of the ombudsman originated in Sweden.",
   "An ombudsman examines complaints of maladministration against public authorities.",
   "In India, Maharashtra was the first State to set up the office of Lokayukta."],
  ["ओम्बड्समैन का पद स्वीडन में शुरू हुआ।",
   "ओम्बड्समैन सार्वजनिक प्राधिकारियों के विरुद्ध कुप्रशासन की शिकायतों की जाँच करता है।",
   "भारत में लोकायुक्त का पद स्थापित करने वाला पहला राज्य महाराष्ट्र था।"],
  C3, 2,
  "All three statements are correct. Sweden created the ombudsman in 1809 as an officer of the legislature to receive citizens' complaints against officials; the idea spread to other Scandinavian countries and beyond. "
  "In India the first Administrative Reforms Commission (1966) proposed a Lokpal at the Centre and Lokayuktas in the States; Maharashtra set up its Lokayukta in 1971, long before the Lokpal and Lokayuktas Act of 2013.",
  "तीनों कथन सही हैं। स्वीडन ने 1809 में ओम्बड्समैन को विधायिका के एक अधिकारी के रूप में बनाया, जो अधिकारियों के विरुद्ध नागरिकों की शिकायतें सुने; यह विचार अन्य स्कैंडिनेवियाई देशों और उनसे आगे फैला। "
  "भारत में पहले प्रशासनिक सुधार आयोग (1966) ने केंद्र में लोकपाल और राज्यों में लोकायुक्त का प्रस्ताव किया; महाराष्ट्र ने 1971 में अपना लोकायुक्त स्थापित किया, 2013 के लोकपाल और लोकायुक्त अधिनियम से बहुत पहले।",
  "Report of the First Administrative Reforms Commission (1966); Maharashtra Lokayukta and Upa-Lokayuktas Act, 1971.",
  "l1-pol-ombudsman-origin-lokayukta", craft="recall")

S(GV, "medium", "Consider the following statements about party systems:",
  "दलीय प्रणालियों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["India has a two-party system.",
   "In a two-party system, only two parties are allowed to contest elections.",
   "A one-party system, as in China, is regarded as a democratic arrangement because the party represents the whole people."],
  ["भारत में दो-दलीय प्रणाली है।",
   "दो-दलीय प्रणाली में केवल दो दलों को चुनाव लड़ने की अनुमति होती है।",
   "चीन जैसी एकदलीय प्रणाली को लोकतांत्रिक व्यवस्था माना जाता है क्योंकि दल पूरी जनता का प्रतिनिधित्व करता है।"],
  C3, 3,
  "None of the statements is correct. Statement 1 is wrong: India has a multi-party system, in which many parties compete and several have a serious chance of coming to power, alone or in alliance. "
  "Statement 2 is wrong: a two-party system, as in the USA or the UK, is one where power usually alternates between two main parties; other parties exist and contest, but rarely win more than a few seats. "
  "Statement 3 is wrong: where only one party is allowed to rule and voters have no real choice, the arrangement is not democratic -- a free choice between parties is part of what democracy means.",
  "कोई भी कथन सही नहीं है। कथन 1 गलत है: भारत में बहुदलीय प्रणाली है, जिसमें कई दल प्रतिस्पर्धा करते हैं और कई के पास अकेले या गठबंधन में सत्ता में आने का गंभीर अवसर होता है। "
  "कथन 2 गलत है: दो-दलीय प्रणाली, जैसे अमेरिका या ब्रिटेन में, वह है जिसमें सत्ता सामान्यतः दो प्रमुख दलों के बीच बदलती रहती है; अन्य दल भी होते हैं और चुनाव लड़ते हैं, पर शायद ही कुछ सीटों से अधिक जीतते हैं। "
  "कथन 3 गलत है: जहाँ केवल एक दल को शासन की अनुमति हो और मतदाताओं के पास कोई वास्तविक विकल्प न हो, वह व्यवस्था लोकतांत्रिक नहीं है -- दलों के बीच स्वतंत्र चुनाव लोकतंत्र के अर्थ का हिस्सा है।",
  f"{DP10}, Chapter 6 (Political Parties).",
  "l1-pol-party-systems", craft="precision")

A(GV, "medium",
  "A political party in India needs recognition by the Election Commission to get a symbol reserved for its candidates across a State or the country.",
  "भारत में किसी राजनीतिक दल को किसी राज्य या पूरे देश में अपने उम्मीदवारों के लिए आरक्षित चुनाव चिह्न पाने हेतु निर्वाचन आयोग की मान्यता चाहिए।",
  "The Constitution of India, as originally adopted, laid down detailed rules for the recognition of political parties.",
  "भारत के मूल रूप से अंगीकृत संविधान ने राजनीतिक दलों की मान्यता के विस्तृत नियम निर्धारित किए थे।",
  2,
  "Statement-I is correct and Statement-II is incorrect. Recognition as a national or State party is granted by the Election Commission under the Election Symbols (Reservation and Allotment) Order, 1968, and it brings a reserved symbol and other privileges. "
  "The original Constitution did not mention political parties at all; they entered the text only with the anti-defection law (Tenth Schedule) added in 1985, and even that says nothing about recognition.",
  "कथन-I सही है और कथन-II गलत है। राष्ट्रीय या राज्य दल के रूप में मान्यता निर्वाचन आयोग चुनाव चिह्न (आरक्षण और आवंटन) आदेश, 1968 के तहत देता है, और उससे आरक्षित चुनाव चिह्न और अन्य सुविधाएँ मिलती हैं। "
  "मूल संविधान में राजनीतिक दलों का उल्लेख ही नहीं था; वे पाठ में 1985 में जोड़े गए दल-बदल विरोधी कानून (दसवीं अनुसूची) से ही आए, और वह भी मान्यता के बारे में कुछ नहीं कहता।",
  f"{DP10}, Chapter 6; Election Symbols (Reservation and Allotment) Order, 1968.",
  "l1-pol-party-recognition-not-in-original-constitution", craft="linkage")

P(GV, "medium", "Consider the following pairs of a term and its meaning:",
  "किसी शब्द और उसके अर्थ के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Accountability : The duty of those in power to answer to the people for their decisions",
   "Responsiveness : Attending to the needs and expectations of citizens",
   "Legitimacy : People's acceptance that a government has the right to rule",
   "Decentralisation : Concentrating all decisions in the national capital"],
  ["जवाबदेही : सत्ता में बैठे लोगों का अपने निर्णयों के लिए जनता को उत्तर देने का दायित्व",
   "संवेदनशीलता : नागरिकों की आवश्यकताओं और अपेक्षाओं पर ध्यान देना",
   "वैधता : जनता द्वारा यह स्वीकार करना कि सरकार को शासन करने का अधिकार है",
   "विकेंद्रीकरण : सभी निर्णय राष्ट्रीय राजधानी में केंद्रित करना"],
  2,
  "Pairs 1, 2 and 3 are correctly matched. Pair 4 inverts the term: decentralisation means taking power away from the central and State governments and giving it to local government -- in India, the panchayats and municipalities strengthened by the 73rd and 74th Amendments. "
  "Concentrating decisions at the centre is centralisation.",
  "युग्म 1, 2 और 3 सही सुमेलित हैं। युग्म 4 शब्द को उलट देता है: विकेंद्रीकरण का अर्थ है केंद्र और राज्य सरकारों से शक्ति लेकर स्थानीय शासन को देना -- भारत में 73वें और 74वें संशोधनों से सशक्त पंचायतें और नगरपालिकाएँ। "
  "निर्णयों को केंद्र में केंद्रित करना केंद्रीकरण है।",
  f"{DP10}, Chapters 2 (Federalism) and 7 (Outcomes of Democracy).",
  "l1-pol-governance-terms-pairs", craft="precision")

S(GV, "hard", "Consider the following bodies:",
  "निम्नलिखित निकायों पर विचार कीजिए:",
  ["The Planning Commission", "The NITI Aayog", "The National Development Council", "The Finance Commission", "The Zonal Councils"],
  ["योजना आयोग", "नीति आयोग", "राष्ट्रीय विकास परिषद", "वित्त आयोग", "क्षेत्रीय परिषदें"],
  None, 1,
  "Three were created by an executive resolution of the Union government: the Planning Commission (1950), the National Development Council (1952), which brought the Chief Ministers into the approval of the Plans, and the NITI Aayog (2015). "
  "The Finance Commission is a constitutional body under Article 280, and the Zonal Councils are statutory bodies set up under the States Reorganisation Act, 1956. A body set up by resolution can be wound up the same way, as the Planning Commission was.",
  "तीन संघ सरकार के कार्यकारी संकल्प से बने: योजना आयोग (1950), राष्ट्रीय विकास परिषद (1952), जिसने योजनाओं के अनुमोदन में मुख्यमंत्रियों को शामिल किया, और नीति आयोग (2015)। "
  "वित्त आयोग अनुच्छेद 280 के तहत संवैधानिक निकाय है, और क्षेत्रीय परिषदें राज्य पुनर्गठन अधिनियम, 1956 के तहत स्थापित सांविधिक निकाय हैं। संकल्प से बना निकाय उसी तरह समाप्त भी किया जा सकता है, जैसा योजना आयोग के साथ हुआ।",
  f"{NC12}, Chapter 3; Constitution of India, Article 280; States Reorganisation Act, 1956.",
  "l1-pol-bodies-set-up-by-resolution", opts=FIVE, opts_hi=FIVE_HI,
  closing="How many of the above were set up by an executive resolution of the Union government?",
  closing_hi="उपर्युक्त में से कितने संघ सरकार के कार्यकारी संकल्प द्वारा स्थापित किए गए?", craft="multi")

# ================================================================ STATUTORY LAWS (10)
M(SL, "easy", "The Hindu Succession (Amendment) Act, 2005 is important because it:",
  "हिंदू उत्तराधिकार (संशोधन) अधिनियम, 2005 इसलिए महत्वपूर्ण है क्योंकि यह:",
  ["made daughters coparceners in joint family property, with the same rights as sons",
   "allowed only unmarried daughters to inherit a share of their father's self-acquired property",
   "abolished the joint Hindu family and divided all ancestral property equally among the State's residents",
   "gave widows the right to inherit property only if they had no sons living at the time of the death"],
  ["बेटियों को संयुक्त परिवार की संपत्ति में बेटों के समान अधिकारों के साथ सहदायिक बनाता है",
   "केवल अविवाहित बेटियों को पिता की स्वअर्जित संपत्ति में हिस्सा पाने का अधिकार देता है",
   "संयुक्त हिंदू परिवार को समाप्त करके सारी पैतृक संपत्ति राज्य के निवासियों में बराबर बाँटता है",
   "विधवाओं को संपत्ति का उत्तराधिकार केवल तभी देता है जब मृत्यु के समय कोई पुत्र जीवित न हो"],
  0,
  "Until 2005 only sons were coparceners -- members who acquire a share in joint family property by birth. The 2005 amendment made daughters coparceners in their own right, married or not, with the same rights and liabilities as sons. "
  "NCERT uses it as an example of a law changed to remove discrimination against women. The other options describe rules the Act did not make.",
  "2005 तक केवल पुत्र सहदायिक थे -- ऐसे सदस्य जो जन्म से संयुक्त परिवार की संपत्ति में हिस्सा पाते हैं। 2005 के संशोधन ने बेटियों को, विवाहित हों या नहीं, अपने अधिकार से सहदायिक बनाया, बेटों के समान अधिकारों और दायित्वों के साथ। "
  "एनसीईआरटी इसे महिलाओं के विरुद्ध भेदभाव हटाने के लिए बदले गए कानून के उदाहरण के रूप में लेता है। बाकी विकल्प ऐसे नियम बताते हैं जो इस अधिनियम ने नहीं बनाए।",
  f"{SPL8}, Chapter 4 (Understanding Laws); Hindu Succession (Amendment) Act, 2005.",
  "l1-pol-hindu-succession-2005-daughters", craft="recall")

S(SL, "easy", "Consider the following statements about the law on child labour as amended in 2016:",
  "2016 में संशोधित बाल श्रम कानून के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It prohibits the employment of children below 14 years in all occupations, with narrow exceptions such as helping the family after school hours.",
   "It prohibits the employment of adolescents aged 14 to 18 years in hazardous occupations and processes."],
  ["यह 14 वर्ष से कम आयु के बच्चों को सभी व्यवसायों में काम पर रखने पर रोक लगाता है, कुछ सीमित अपवादों के साथ, जैसे स्कूल के समय के बाद परिवार की मदद करना।",
   "यह 14 से 18 वर्ष के किशोरों को खतरनाक व्यवसायों और प्रक्रियाओं में काम पर रखने पर रोक लगाता है।"],
  T2, 2,
  "Both statements are correct. The Child Labour (Prohibition and Regulation) Amendment Act, 2016 renamed the 1986 law the Child and Adolescent Labour (Prohibition and Regulation) Act. It replaced the old list of banned occupations with a ban on all employment of children below 14 -- except helping in a family enterprise after school or working as an artist under conditions -- and added a ban on adolescents in hazardous work.",
  "दोनों कथन सही हैं। बाल श्रम (प्रतिषेध और विनियमन) संशोधन अधिनियम, 2016 ने 1986 के कानून का नाम बदलकर बालक और किशोर श्रम (प्रतिषेध और विनियमन) अधिनियम कर दिया। इसने प्रतिबंधित व्यवसायों की पुरानी सूची की जगह 14 वर्ष से कम आयु के बच्चों के सभी रोज़गार पर रोक लगा दी -- स्कूल के बाद पारिवारिक उद्यम में मदद करने या शर्तों के साथ कलाकार के रूप में काम करने के सिवा -- और खतरनाक काम में किशोरों पर रोक जोड़ी।",
  f"{SPL8}, Chapter 10 (Law and Social Justice); Child Labour (Prohibition and Regulation) Amendment Act, 2016.",
  "l1-pol-child-adolescent-labour-2016", craft="precision")

S(SL, "easy", "Consider the following statements about laws against manual scavenging:",
  "हाथ से मैला ढोने के विरुद्ध कानूनों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["A law prohibiting the employment of manual scavengers and the construction of dry latrines was passed in 1993.",
   "The 2013 Act on manual scavenging also covers the hazardous cleaning of sewers and septic tanks.",
   "Under the 2013 Act, employing a person as a manual scavenger is a civil wrong that attracts only a fine."],
  ["हाथ से मैला ढोने वालों के नियोजन और शुष्क शौचालयों के निर्माण पर रोक लगाने वाला कानून 1993 में पारित हुआ।",
   "हाथ से मैला ढोने पर 2013 का अधिनियम सीवरों और सेप्टिक टैंकों की खतरनाक सफ़ाई को भी शामिल करता है।",
   "2013 के अधिनियम के तहत किसी व्यक्ति को हाथ से मैला ढोने के काम पर रखना केवल जुर्माने वाला दीवानी दोष है।"],
  C3, 1,
  "Statements 1 and 2 are correct. The Employment of Manual Scavengers and Construction of Dry Latrines (Prohibition) Act, 1993 was the first ban; the Prohibition of Employment as Manual Scavengers and their Rehabilitation Act, 2013 widened it to the hazardous cleaning of sewers and septic tanks without protective gear and provided for rehabilitation. "
  "Statement 3 is wrong: contraventions are criminal offences punishable with imprisonment as well as fine, and they are cognisable and non-bailable.",
  "कथन 1 और 2 सही हैं। हाथ से मैला ढोने वालों का नियोजन और शुष्क शौचालय निर्माण (प्रतिषेध) अधिनियम, 1993 पहला प्रतिबंध था; हाथ से मैला ढोने वालों के रूप में नियोजन का प्रतिषेध और उनका पुनर्वास अधिनियम, 2013 ने इसे बिना सुरक्षा उपकरण के सीवरों और सेप्टिक टैंकों की खतरनाक सफ़ाई तक बढ़ाया और पुनर्वास का प्रावधान किया। "
  "कथन 3 गलत है: उल्लंघन आपराधिक अपराध हैं जिनमें जुर्माने के साथ कारावास भी हो सकता है, और वे संज्ञेय और गैर-जमानती हैं।",
  f"{SPL8}, Chapter 7 (Confronting Marginalisation); Prohibition of Employment as Manual Scavengers and their Rehabilitation Act, 2013.",
  "l1-pol-manual-scavenging-1993-2013", craft="precision")

A(SL, "easy",
  "Laws in a democracy can be shaped by people's campaigns as well as by legislators.",
  "लोकतंत्र में कानून जन-अभियानों से भी आकार ले सकते हैं, केवल विधायकों से ही नहीं।",
  "The Protection of Women from Domestic Violence Act, 2005 was passed after years of campaigning by women's organisations.",
  "घरेलू हिंसा से महिलाओं का संरक्षण अधिनियम, 2005 महिला संगठनों के वर्षों के अभियान के बाद पारित हुआ।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I by example. NCERT traces how women's groups documented domestic violence, drafted a Bill, and kept up the pressure through public meetings and representations until Parliament passed the 2005 Act. "
  "In a democracy citizens can bring an issue to Parliament's attention and influence the shape of a law, not only obey it.",
  "दोनों कथन सही हैं, और कथन-II उदाहरण द्वारा कथन-I की व्याख्या करता है। एनसीईआरटी दिखाता है कि कैसे महिला संगठनों ने घरेलू हिंसा का दस्तावेज़ीकरण किया, एक विधेयक का मसौदा बनाया, और सार्वजनिक सभाओं और ज्ञापनों से दबाव बनाए रखा जब तक संसद ने 2005 का अधिनियम पारित नहीं किया। "
  "लोकतंत्र में नागरिक किसी मुद्दे को संसद के ध्यान में ला सकते हैं और किसी कानून के रूप को प्रभावित कर सकते हैं, केवल उसका पालन ही नहीं।",
  f"{SPL8}, Chapter 4 (Understanding Laws).",
  "l1-pol-laws-shaped-by-campaigns", craft="linkage")

M(SL, "medium", "Under the Scheduled Tribes and Other Traditional Forest Dwellers (Recognition of Forest Rights) Act, 2006, which body starts the process of determining the forest rights of individuals and communities?",
  "अनुसूचित जनजाति और अन्य परंपरागत वन निवासी (वन अधिकारों की मान्यता) अधिनियम, 2006 के तहत व्यक्तियों और समुदायों के वन अधिकार निर्धारित करने की प्रक्रिया कौन-सा निकाय शुरू करता है?",
  ["The Gram Sabha", "The Divisional Forest Officer", "The State Board for Wildlife", "The National Commission for Scheduled Tribes"],
  ["ग्राम सभा", "प्रभागीय वन अधिकारी", "राज्य वन्यजीव बोर्ड", "राष्ट्रीय अनुसूचित जनजाति आयोग"],
  0,
  "The Act makes the Gram Sabha the authority to initiate the process: it receives claims, verifies them and passes a resolution, which then goes to a Sub-Divisional Level Committee and finally to a District Level Committee for a decision. "
  "Putting the village assembly first was meant to undo the 'historical injustice' of forest dwellers' rights going unrecorded; the forest department, the State wildlife board and the National Commission for Scheduled Tribes have no such role at the start.",
  "अधिनियम ग्राम सभा को प्रक्रिया शुरू करने वाला प्राधिकारी बनाता है: वह दावे प्राप्त करती है, उनका सत्यापन करती है और संकल्प पारित करती है, जो फिर उप-मंडल स्तरीय समिति और अंत में ज़िला स्तरीय समिति के पास निर्णय के लिए जाता है। "
  "ग्राम सभा को पहले रखने का उद्देश्य वन निवासियों के अधिकार दर्ज न होने के 'ऐतिहासिक अन्याय' को दूर करना था; वन विभाग, राज्य वन्यजीव बोर्ड और राष्ट्रीय अनुसूचित जनजाति आयोग की आरंभ में ऐसी कोई भूमिका नहीं है।",
  f"{SPL8}, Chapter 7 (Confronting Marginalisation); Forest Rights Act, 2006, Section 6.",
  "l1-pol-forest-rights-gram-sabha", craft="precision")

S(SL, "medium", "Consider the following statements about the Scheduled Castes and the Scheduled Tribes (Prevention of Atrocities) Act, 1989:",
  "अनुसूचित जाति और अनुसूचित जनजाति (अत्याचार निवारण) अधिनियम, 1989 के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It lists specific acts against members of the Scheduled Castes and Scheduled Tribes as offences of atrocity.",
   "Its offences are tried only by ordinary civil courts.",
   "It applies only to offences committed by public servants."],
  ["यह अनुसूचित जातियों और अनुसूचित जनजातियों के सदस्यों के विरुद्ध विशिष्ट कृत्यों को अत्याचार के अपराधों के रूप में सूचीबद्ध करता है।",
   "इसके अपराधों का विचारण केवल सामान्य दीवानी न्यायालय करते हैं।",
   "यह केवल लोक सेवकों द्वारा किए गए अपराधों पर लागू होता है।"],
  C3, 0,
  "Only statement 1 is correct. The Act was passed because the general criminal law had not checked the humiliation and violence faced by Dalits and Adivasis; it names specific atrocities -- from forcing a person to eat inedible substances to wrongfully occupying land allotted to him -- and prescribes punishment. "
  "Statement 2 is wrong: these are criminal offences, tried by Special Courts and, since the 2015 amendment, by Exclusive Special Courts. Statement 3 is wrong: the offences apply to any person who is not a member of a Scheduled Caste or Scheduled Tribe, while public servants who neglect their duties under it are separately punishable.",
  "केवल कथन 1 सही है। यह अधिनियम इसलिए पारित हुआ कि सामान्य आपराधिक कानून दलितों और आदिवासियों के अपमान और उनके विरुद्ध हिंसा को नहीं रोक पाया था; यह विशिष्ट अत्याचारों के नाम देता है -- किसी व्यक्ति को अखाद्य पदार्थ खाने को विवश करने से लेकर उसे आवंटित भूमि पर ग़लत कब्ज़ा करने तक -- और दंड निर्धारित करता है। "
  "कथन 2 गलत है: ये आपराधिक अपराध हैं, जिनका विचारण विशेष न्यायालय और 2015 के संशोधन के बाद से अनन्य विशेष न्यायालय करते हैं। कथन 3 गलत है: अपराध ऐसे किसी भी व्यक्ति पर लागू होते हैं जो अनुसूचित जाति या अनुसूचित जनजाति का सदस्य न हो, जबकि इसके तहत अपने कर्तव्यों की उपेक्षा करने वाले लोक सेवक अलग से दंडनीय हैं।",
  f"{SPL8}, Chapter 7 (Confronting Marginalisation); SC and ST (Prevention of Atrocities) Act, 1989.",
  "l1-pol-atrocities-act-1989", craft="precision")

S(SL, "medium", "Consider the following statements about the Bonded Labour System (Abolition) Act, 1976:",
  "बंधुआ मज़दूरी प्रथा (उन्मूलन) अधिनियम, 1976 के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It freed every bonded labourer and wiped out the debts that bound them.",
   "It made compelling a person to render bonded labour a punishable offence.",
   "Bonded labourers freed under the law are entitled to rehabilitation assistance from the government."],
  ["इसने हर बंधुआ मज़दूर को मुक्त किया और उन्हें बाँधने वाले ऋण समाप्त कर दिए।",
   "इसने किसी व्यक्ति को बंधुआ मज़दूरी के लिए विवश करना दंडनीय अपराध बना दिया।",
   "कानून के तहत मुक्त कराए गए बंधुआ मज़दूर सरकार से पुनर्वास सहायता के हकदार हैं।"],
  C3, 2,
  "All three statements are correct. The Act declared the bonded labour system abolished, discharged every bonded labourer from any obligation to render such labour and extinguished the bonded debt, and made enforcing bonded labour punishable with imprisonment and fine. "
  "Freed labourers are rehabilitated under a Central Sector Scheme (revamped in 2016) that provides cash assistance and links them to land, housing and other schemes; the Act itself gives effect to Article 23, which prohibits 'begar and other similar forms of forced labour'.",
  "तीनों कथन सही हैं। अधिनियम ने बंधुआ मज़दूरी प्रथा को समाप्त घोषित किया, हर बंधुआ मज़दूर को ऐसा श्रम करने के किसी भी दायित्व से मुक्त किया और बंधुआ ऋण समाप्त किया, और बंधुआ मज़दूरी करवाने को कारावास और जुर्माने से दंडनीय बनाया। "
  "मुक्त मज़दूरों का पुनर्वास एक केंद्रीय क्षेत्र योजना (2016 में नवीकृत) के तहत होता है, जो नकद सहायता देती है और उन्हें भूमि, आवास और अन्य योजनाओं से जोड़ती है; अधिनियम स्वयं अनुच्छेद 23 को लागू करता है, जो 'बेगार और इसी प्रकार के अन्य बलात् श्रम' का निषेध करता है।",
  f"Bonded Labour System (Abolition) Act, 1976; Ministry of Labour and Employment, Central Sector Scheme for Rehabilitation of Bonded Labourer, 2016; Constitution of India, Article 23.",
  "l1-pol-bonded-labour-abolition-1976", craft="linkage")

S(SL, "medium", "Consider the following statements about the Right to Fair Compensation and Transparency in Land Acquisition, Rehabilitation and Resettlement Act, 2013:",
  "भूमि अर्जन, पुनर्वासन और पुनर्व्यवस्थापन में उचित प्रतिकर और पारदर्शिता का अधिकार अधिनियम, 2013 के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["For land acquired for private companies, it requires the consent of at least 80 per cent of the affected families.",
   "It requires a Social Impact Assessment before most acquisitions.",
   "It applies only to land acquired for defence purposes."],
  ["निजी कंपनियों के लिए अर्जित भूमि के मामले में यह कम से कम 80 प्रतिशत प्रभावित परिवारों की सहमति अपेक्षित करता है।",
   "यह अधिकांश अर्जनों से पहले सामाजिक प्रभाव आकलन अपेक्षित करता है।",
   "यह केवल रक्षा उद्देश्यों के लिए अर्जित भूमि पर लागू होता है।"],
  C3, 1,
  "Statements 1 and 2 are correct. The 2013 Act replaced the Land Acquisition Act, 1894: acquisition for private companies needs the consent of 80 per cent of the affected families (70 per cent for public-private partnerships), and a Social Impact Assessment must study who will be affected and how. "
  "It also raised compensation and made rehabilitation a right. Statement 3 is wrong: the Act is the general law of land acquisition for public purposes, which include infrastructure, industry and urbanisation.",
  "कथन 1 और 2 सही हैं। 2013 के अधिनियम ने भूमि अर्जन अधिनियम, 1894 का स्थान लिया: निजी कंपनियों के लिए अर्जन में 80 प्रतिशत प्रभावित परिवारों की सहमति चाहिए (सार्वजनिक-निजी भागीदारी में 70 प्रतिशत), और सामाजिक प्रभाव आकलन में अध्ययन करना होता है कि कौन और कैसे प्रभावित होगा। "
  "इसने प्रतिकर भी बढ़ाया और पुनर्वास को अधिकार बनाया। कथन 3 गलत है: यह अधिनियम सार्वजनिक प्रयोजनों के लिए भूमि अर्जन का सामान्य कानून है, जिनमें अवसंरचना, उद्योग और शहरीकरण शामिल हैं।",
  "Right to Fair Compensation and Transparency in Land Acquisition, Rehabilitation and Resettlement Act, 2013, Sections 2 and 4.",
  "l1-pol-larr-2013-consent-sia", craft="precision")

A(SL, "medium",
  "Laws by themselves have ended practices such as child marriage.",
  "केवल कानूनों से ही बाल विवाह जैसी प्रथाएँ समाप्त हो गई हैं।",
  "How well a social law works depends on social attitudes and on the will of the agencies that enforce it.",
  "कोई सामाजिक कानून कितनी अच्छी तरह काम करता है, यह सामाजिक दृष्टिकोण और उसे लागू करने वाली एजेंसियों की इच्छाशक्ति पर निर्भर करता है।",
  3,
  "Statement-I is incorrect and Statement-II is correct. Child marriage has been an offence since the Child Marriage Restraint Act of 1929 and is now governed by the Prohibition of Child Marriage Act, 2006, yet it persists where custom, poverty and weak enforcement keep it alive. "
  "NCERT's point is that a law sets a standard and gives the victim a remedy, but social change also needs awareness and active enforcement.",
  "कथन-I गलत है और कथन-II सही है। बाल विवाह 1929 के बाल विवाह निरोध अधिनियम से अपराध है और अब बाल विवाह प्रतिषेध अधिनियम, 2006 से शासित है, फिर भी वह वहाँ बना हुआ है जहाँ प्रथा, ग़रीबी और कमज़ोर प्रवर्तन उसे जीवित रखते हैं। "
  "एनसीईआरटी का कहना है कि कानून एक मानक तय करता है और पीड़ित को उपचार देता है, पर सामाजिक बदलाव के लिए जागरूकता और सक्रिय प्रवर्तन भी चाहिए।",
  f"{SPL8}, Chapters 4 and 10; Prohibition of Child Marriage Act, 2006.",
  "l1-pol-laws-and-social-attitudes", craft="inference")

S(SL, "hard", "Consider the following statements about the Bhopal gas tragedy and its legal aftermath:",
  "भोपाल गैस त्रासदी और उसके कानूनी परिणामों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The disaster of December 1984 was caused by a leak of methyl isocyanate from a pesticide plant of Union Carbide.",
   "A law of 1985 made the Union government the sole representative of the victims in pursuing their claims.",
   "The settlement reached with the company in 1989 was for 470 million US dollars.",
   "Soon after, the Supreme Court laid down the rule of absolute liability for enterprises engaged in hazardous activities."],
  ["दिसंबर 1984 की आपदा यूनियन कार्बाइड के एक कीटनाशक संयंत्र से मिथाइल आइसोसाइनेट के रिसाव से हुई थी।",
   "1985 के एक कानून ने दावों के लिए केंद्र सरकार को पीड़ितों का एकमात्र प्रतिनिधि बनाया।",
   "1989 में कंपनी के साथ हुआ समझौता 47 करोड़ अमेरिकी डॉलर का था।",
   "इसके कुछ ही समय बाद सर्वोच्च न्यायालय ने खतरनाक गतिविधियों में लगे उद्यमों के लिए पूर्ण दायित्व का नियम निर्धारित किया।"],
  C4, 3,
  "All four statements are correct. The gas leak killed thousands and injured lakhs; the Bhopal Gas Leak Disaster (Processing of Claims) Act, 1985 let the Union government represent all claimants against the company, and the 1989 settlement of US$470 million was widely criticised as far too low. "
  "In M.C. Mehta v. Union of India (1986), arising from the oleum gas leak in Delhi, the Supreme Court held that an enterprise carrying on a hazardous activity is absolutely liable for the harm it causes, without the exceptions of the older strict-liability rule. NCERT uses Bhopal to show why workers' and citizens' safety needs strong laws and enforcement.",
  "चारों कथन सही हैं। गैस रिसाव में हज़ारों लोग मारे गए और लाखों घायल हुए; भोपाल गैस रिसाव आपदा (दावों का प्रसंस्करण) अधिनियम, 1985 ने केंद्र सरकार को कंपनी के विरुद्ध सभी दावेदारों का प्रतिनिधित्व करने दिया, और 1989 के 47 करोड़ अमेरिकी डॉलर के समझौते की बहुत कम होने के कारण व्यापक आलोचना हुई। "
  "दिल्ली के ओलियम गैस रिसाव से निकले एम.सी. मेहता बनाम भारत संघ (1986) में सर्वोच्च न्यायालय ने माना कि खतरनाक गतिविधि चलाने वाला उद्यम अपने द्वारा हुई हानि के लिए पूर्ण रूप से उत्तरदायी है, पुराने कठोर दायित्व नियम के अपवादों के बिना। एनसीईआरटी भोपाल के उदाहरण से दिखाता है कि श्रमिकों और नागरिकों की सुरक्षा के लिए मज़बूत कानून और प्रवर्तन क्यों ज़रूरी हैं।",
  f"{SPL8}, Chapter 10 (Law and Social Justice); Bhopal Gas Leak Disaster (Processing of Claims) Act, 1985; Supreme Court of India, M.C. Mehta v. Union of India (1986).",
  "l1-pol-bhopal-legal-aftermath", craft="multi")

write("pol_l1_t1_c.sql")
