# -*- coding: utf-8 -*-
"""Current Affairs · Test 4 (October to December 2026) -- part A: international affairs, awards, sports and national.

Framed as the 2025-26 papers frame current affairs (design doc, section 7): each item names the person, grouping or
programme and tests what it is, why it matters and where the wording misleads -- Navi Pillay and the international
courts, the year's Nobel Prizes, BIMSTEC's first Home Ministers' meeting, India and Poland (and the wartime refuge of
Polish children), the Asian Games in Japan, and Lakshadweep under ULLAS. Written month by month: October 2026 first.
No stem carries a date, and every fact was searched in the whole UPSC bank."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2
from ca_common import MX, finish
from ca_t4_format import FORMAT, POS

d.SUBJECT = "Current Affairs"
d.REQUIRE_CRAFT = True
IN, NA, AW, SP = "International", "National", "Awards & Persons", "Sports"

# ---------------------------------------------------------------- October 2026

S(AW, "medium", "Navi Pillay was awarded the Nobel Peace Prize for 2026 for her efforts to promote peace and international law. Consider the following statements about her career:",
  "नवी पिल्लै को शांति और अंतरराष्ट्रीय विधि को बढ़ावा देने के प्रयासों के लिए 2026 का नोबेल शांति पुरस्कार दिया गया। उनके करियर के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["She served as a judge of both the International Criminal Tribunal for Rwanda and the International Criminal Court.",
   "She was the United Nations High Commissioner for Human Rights.",
   "The Commission of Inquiry on the Occupied Palestinian Territory that she chaired was set up by the UN Human Rights Council."],
  ["उन्होंने रवांडा के लिए अंतरराष्ट्रीय आपराधिक अधिकरण और अंतरराष्ट्रीय आपराधिक न्यायालय, दोनों में न्यायाधीश के रूप में कार्य किया।",
   "वे संयुक्त राष्ट्र मानवाधिकार उच्चायुक्त रहीं।",
   "उनकी अध्यक्षता वाले अधिकृत फ़िलिस्तीनी क्षेत्र संबंधी जाँच आयोग को संयुक्त राष्ट्र मानवाधिकार परिषद ने स्थापित किया था।"],
  C3, 2,
  "All three statements are correct. Born in Durban to a family of Indian Tamil origin, Pillay defended opponents of apartheid, among them Nelson Mandela, before she became a judge of South Africa's High Court. At the International Criminal Tribunal for Rwanda, set up by the Security Council in 1994, she helped establish that rape and sexual violence can constitute genocide and crimes against humanity, and that spreading propaganda alone can amount to incitement to genocide; she then sat on the International Criminal Court, created by the Rome Statute of 1998, to which India is not a party. "
  "As High Commissioner for Human Rights she headed an office that the General Assembly created in 1993 and that forms part of the UN Secretariat, not of the Security Council. The Human Rights Council, a subsidiary body of the General Assembly, set up the Commission of Inquiry in 2021. She now sits on the International Court of Justice in the case in which Myanmar is accused of genocide. The Norwegian Nobel Committee chose her as a defender of the rule of law at a time when international courts and their judges are under attack.",
  "तीनों कथन सही हैं। भारतीय तमिल मूल के परिवार में डरबन में जन्मी पिल्लै ने रंगभेद के विरोधियों, जिनमें नेल्सन मंडेला भी थे, की पैरवी की और फिर दक्षिण अफ़्रीका के उच्च न्यायालय की न्यायाधीश बनीं। सुरक्षा परिषद द्वारा 1994 में स्थापित रवांडा के लिए अंतरराष्ट्रीय आपराधिक अधिकरण में उन्होंने यह स्थापित करने में मदद की कि बलात्कार और यौन हिंसा नरसंहार और मानवता के विरुद्ध अपराध हो सकते हैं, और कि केवल प्रचार फैलाना भी नरसंहार के लिए उकसावा हो सकता है; फिर वे 1998 के रोम संविधि से बने अंतरराष्ट्रीय आपराधिक न्यायालय में रहीं, जिसका भारत पक्षकार नहीं है। "
  "मानवाधिकार उच्चायुक्त के रूप में उन्होंने उस कार्यालय का नेतृत्व किया जिसे महासभा ने 1993 में बनाया और जो संयुक्त राष्ट्र सचिवालय का भाग है, सुरक्षा परिषद का नहीं। महासभा के सहायक निकाय मानवाधिकार परिषद ने 2021 में जाँच आयोग स्थापित किया। अब वे अंतरराष्ट्रीय न्यायालय में उस मामले में न्यायाधीश हैं जिसमें म्यांमार पर नरसंहार का आरोप है। नॉर्वेजियन नोबेल समिति ने उन्हें ऐसे समय विधि के शासन की रक्षक के रूप में चुना जब अंतरराष्ट्रीय न्यायालयों और उनके न्यायाधीशों पर हमले हो रहे हैं।",
  "Norwegian Nobel Committee, announcement of the Nobel Peace Prize 2026 (9 October 2026); UN General Assembly resolution 48/141 (1993); Human Rights Council, Commission of Inquiry on the Occupied Palestinian Territory (2021).",
  "ca-t4-ca-navi-pillay-ictr-icc-ohchr-hrc-coi", craft="precision")

MX(AW, "easy", "Match List-I (Nobel Prize of 2026) with List-II (the field of the work it recognised):",
   "सूची-I (2026 का नोबेल पुरस्कार) का सूची-II (पुरस्कृत कार्य का क्षेत्र) से मिलान कीजिए:",
   ["Physics", "Chemistry", "Physiology or Medicine", "Economic Sciences"],
   ["भौतिकी", "रसायन", "शरीरक्रिया विज्ञान या चिकित्सा", "आर्थिक विज्ञान"],
   ["Optogenetics", "Macroeconomic stabilisation", "Neutrino astronomy", "Asymmetric organic synthesis"],
   ["ऑप्टोजेनेटिक्स", "समष्टि-आर्थिक स्थिरीकरण", "न्यूट्रिनो खगोलिकी", "असममित कार्बनिक संश्लेषण"],
   (3, 4, 1, 2), POS.get("ca-t4-ca-nobel-2026-fields-match", 0),
   "The correct code is A-3, B-4, C-1, D-2. Physics went to Francis Halzen for the IceCube Neutrino Observatory, a cubic kilometre of Antarctic ice fitted with light sensors, and the discovery of high-energy neutrinos from beyond the solar system. Chemistry went to Henri Kagan of France and Kenso Soai of Japan for showing how a reaction can be steered to give only one of two mirror-image molecules, the puzzle of why life uses one form. "
   "Physiology or Medicine went to Karl Deisseroth, Peter Hegemann and Georg Nagel for channelrhodopsin, an algal protein that lets nerve cells be switched on with light. Economic Sciences went to Robert Hall and Michael Woodford for building macroeconomic models on how forward-looking households and firms behave, the basis of the models central banks now use. Each wrong code swaps one pair.",
   "सही कूट A-3, B-4, C-1, D-2 है। भौतिकी का पुरस्कार फ़्रांसिस हाल्ज़ेन को आइसक्यूब न्यूट्रिनो वेधशाला -- प्रकाश-संवेदकों से युक्त अंटार्कटिक बर्फ़ का एक घन किलोमीटर -- और सौरमंडल से परे से आने वाले उच्च-ऊर्जा न्यूट्रिनो की खोज के लिए मिला। रसायन का पुरस्कार फ़्रांस के हेनरी कागन और जापान के केन्सो सोआई को यह दिखाने के लिए मिला कि किसी अभिक्रिया को दो दर्पण-प्रतिबिंब अणुओं में से केवल एक देने की ओर कैसे मोड़ा जा सकता है, यानी जीवन केवल एक रूप क्यों अपनाता है। "
   "शरीरक्रिया विज्ञान या चिकित्सा का पुरस्कार कार्ल डाइसरोथ, पीटर हेगमान और गेओर्ग नागेल को चैनलरोडॉप्सिन के लिए मिला, एक शैवालीय प्रोटीन जिससे तंत्रिका कोशिकाओं को प्रकाश से सक्रिय किया जा सकता है। आर्थिक विज्ञान का पुरस्कार रॉबर्ट हॉल और माइकल वुडफ़र्ड को आगे देखने वाले परिवारों और फ़र्मों के व्यवहार पर समष्टि-आर्थिक मॉडल खड़े करने के लिए मिला, जो आज केंद्रीय बैंकों के मॉडलों का आधार हैं। प्रत्येक ग़लत कूट एक जोड़ी को अदल-बदल देता है।",
   "Royal Swedish Academy of Sciences and Nobel Assembly at Karolinska Institutet, press releases for the Nobel Prizes of 2026 (5-12 October 2026).",
   "ca-t4-ca-nobel-2026-fields-match", "recall")

S(IN, "medium", "The first meeting of BIMSTEC's Home Ministers, held in New Delhi, adopted a declaration on terrorism and transnational crime. With reference to BIMSTEC, consider the following statements:",
  "नई दिल्ली में हुई बिम्सटेक के गृह मंत्रियों की पहली बैठक ने आतंकवाद और अंतरराष्ट्रीय अपराध पर एक घोषणा अपनाई। बिम्सटेक के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Every member of BIMSTEC has a coastline on the Bay of Bengal.",
   "Its permanent secretariat is in Dhaka.",
   "Its Charter, which gives the grouping a legal personality, has entered into force."],
  ["बिम्सटेक के प्रत्येक सदस्य की तटरेखा बंगाल की खाड़ी पर है।",
   "इसका स्थायी सचिवालय ढाका में है।",
   "इसका चार्टर, जो समूह को विधिक व्यक्तित्व देता है, प्रवृत्त हो चुका है।"],
  C3, 1,
  "Statements 2 and 3 are correct. The Bay of Bengal Initiative for Multi-Sectoral Technical and Economic Cooperation began with the Bangkok Declaration of 1997 as a group of Bangladesh, India, Sri Lanka and Thailand; Myanmar joined that year and Nepal and Bhutan in 2004. Its secretariat opened in Dhaka in 2014. The Charter, signed at the Colombo summit in 2022, entered into force in 2024 once all seven members had ratified it, turning a loose initiative into an organisation with legal personality and set rules for its meetings. "
  "Statement 1 is wrong: Nepal and Bhutan are landlocked; they belong because the Bay is the outlet of the river basins that drain them, and the group links South Asia with South-East Asia at a time when SAARC is stalled. The Home Ministers' meeting built on a BIMSTEC convention on combating terrorism, organised crime and drug trafficking and on regular meetings of national security chiefs; its Delhi Declaration condemned terrorism in all its forms, including cross-border terrorism.",
  "कथन 2 और 3 सही हैं। बहुक्षेत्रीय तकनीकी और आर्थिक सहयोग के लिए बंगाल की खाड़ी पहल 1997 की बैंकॉक घोषणा से बांग्लादेश, भारत, श्रीलंका और थाईलैंड के समूह के रूप में आरंभ हुई; म्यांमार उसी वर्ष और नेपाल तथा भूटान 2004 में जुड़े। इसका सचिवालय 2014 में ढाका में खुला। 2022 के कोलंबो शिखर सम्मेलन में हस्ताक्षरित चार्टर सभी सात सदस्यों के अनुसमर्थन के बाद 2024 में प्रवृत्त हुआ, जिससे एक ढीली पहल विधिक व्यक्तित्व और बैठकों के तय नियमों वाला संगठन बन गई। "
  "कथन 1 ग़लत है: नेपाल और भूटान स्थलरुद्ध हैं; वे इसलिए सदस्य हैं कि खाड़ी उन्हें सींचने वाली नदी-घाटियों का निकास है, और यह समूह ऐसे समय दक्षिण एशिया को दक्षिण-पूर्व एशिया से जोड़ता है जब सार्क ठप है। गृह मंत्रियों की बैठक आतंकवाद, संगठित अपराध और मादक पदार्थों की तस्करी से निपटने संबंधी बिम्सटेक अभिसमय और राष्ट्रीय सुरक्षा प्रमुखों की नियमित बैठकों पर आधारित थी; इसकी दिल्ली घोषणा ने सीमा-पार आतंकवाद सहित आतंकवाद के सभी रूपों की निंदा की।",
  "Ministry of Home Affairs and PIB, First BIMSTEC Home Ministers' Meeting and Delhi Declaration (October 2026); BIMSTEC Charter (signed 2022, in force 2024); BIMSTEC Secretariat, Dhaka.",
  "ca-t4-ca-bimstec-home-ministers-landlocked-dhaka-charter", craft="precision")

S(IN, "medium", "The Polish Prime Minister visited India in 2026 with the largest delegation of its kind in the history of the relationship. With reference to India-Poland relations, consider the following statements:",
  "पोलैंड के प्रधानमंत्री 2026 में संबंधों के इतिहास के अपनी तरह के सबसे बड़े प्रतिनिधिमंडल के साथ भारत आए। भारत-पोलैंड संबंधों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["During the Second World War, the Jam Sahib of Nawanagar sheltered Polish refugee children at a camp near Jamnagar.",
   "A settlement for Polish refugees was also run at Valivade near Kolhapur.",
   "The two countries raised their relations to a Strategic Partnership in 2024."],
  ["द्वितीय विश्व युद्ध के दौरान नवानगर के जाम साहब ने जामनगर के पास एक शिविर में पोलिश शरणार्थी बच्चों को आश्रय दिया।",
   "पोलिश शरणार्थियों के लिए कोल्हापुर के पास वलिवडे में भी एक बस्ती चलाई गई।",
   "दोनों देशों ने 2024 में अपने संबंधों को रणनीतिक साझेदारी तक उन्नत किया।"],
  C3, 2,
  "All three statements are correct. In 1942 Maharaja Jam Saheb Digvijaysinhji of Nawanagar took in hundreds of Polish children, many of them orphans who had been deported to the Soviet Union and released after 1941, at Balachadi near Jamnagar; Warsaw has a square named after the 'Good Maharaja'. A larger camp at Valivade near Kolhapur sheltered about 5,000 Poles between 1943 and 1948. "
  "The Indian Prime Minister's visit to Warsaw in 2024, the first in 45 years, raised ties to a Strategic Partnership with an action plan for 2024-28, and the Polish Prime Minister's visit in 2026 put trade, defence industry and technology at the centre. The wartime story is why both sides call the relationship one with no conflicts to resolve, only a history of goodwill to build on.",
  "तीनों कथन सही हैं। 1942 में नवानगर के महाराजा जाम साहब दिग्विजयसिंहजी ने जामनगर के पास बालाचड़ी में सैकड़ों पोलिश बच्चों को आश्रय दिया, जिनमें से अनेक सोवियत संघ में निर्वासित किए गए और 1941 के बाद छोड़े गए अनाथ थे; वारसा में ‘अच्छे महाराजा’ के नाम पर एक चौक है। कोल्हापुर के पास वलिवडे के एक बड़े शिविर ने 1943 से 1948 के बीच लगभग 5,000 पोलिश लोगों को आश्रय दिया। "
  "2024 में भारतीय प्रधानमंत्री की वारसा यात्रा ने, जो 45 वर्षों में पहली थी, संबंधों को 2024-28 की कार्य-योजना के साथ रणनीतिक साझेदारी तक उन्नत किया, और 2026 में पोलिश प्रधानमंत्री की यात्रा ने व्यापार, रक्षा उद्योग और प्रौद्योगिकी को केंद्र में रखा। युद्धकालीन प्रसंग के कारण ही दोनों पक्ष इस संबंध को ऐसा बताते हैं जिसमें सुलझाने को कोई विवाद नहीं, केवल आगे बढ़ाने को सद्भाव का इतिहास है।",
  "Ministry of External Affairs, India-Poland joint statement and Action Plan 2024-28 (August 2024) and visit of the Prime Minister of Poland (October 2026); Embassy of India, Warsaw, history of the Polish refugees in India.",
  "ca-t4-ca-india-poland-jam-sahib-balachadi-valivade-sp-2024", craft="linkage")

S(SP, "easy", "With reference to the 2026 Asian Games, consider the following statements:",
  "2026 के एशियाई खेलों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["They were held in Japan, which had hosted the Asian Games twice before.",
   "India finished among the top three nations in the medal table.",
   "India won more medals than at any earlier edition of the Games."],
  ["ये जापान में हुए, जिसने इससे पहले दो बार एशियाई खेलों की मेज़बानी की थी।",
   "भारत पदक तालिका में शीर्ष तीन देशों में रहा।",
   "भारत ने खेलों के किसी भी पिछले संस्करण से अधिक पदक जीते।"],
  C3, 0,
  "Only statement 1 is correct. The 20th Asian Games were held in Aichi and Nagoya from September to early October 2026; Japan had hosted them in Tokyo (1958) and Hiroshima (1994). "
  "Statement 2 is wrong: India finished fourth, with 85 medals (21 gold, 27 silver and 37 bronze), its last gold coming in men's hockey; the table is ranked by gold medals, and China led it by a wide margin. Statement 3 is wrong: India's best haul remains the 107 medals it won at Hangzhou in 2023, so 2026 was its second-best showing.",
  "केवल कथन 1 सही है। 20वें एशियाई खेल सितंबर से अक्टूबर 2026 के आरंभ तक आइची और नागोया में हुए; जापान ने इससे पहले टोक्यो (1958) और हिरोशिमा (1994) में इनकी मेज़बानी की थी। "
  "कथन 2 ग़लत है: भारत 85 पदकों (21 स्वर्ण, 27 रजत और 37 कांस्य) के साथ चौथे स्थान पर रहा, उसका अंतिम स्वर्ण पुरुष हॉकी में आया; तालिका स्वर्ण पदकों के आधार पर क्रमित होती है, और चीन भारी अंतर से शीर्ष पर रहा। कथन 3 ग़लत है: भारत का सर्वश्रेष्ठ प्रदर्शन अब भी 2023 में हांगझोउ में जीते गए 107 पदक हैं, इसलिए 2026 उसका दूसरा सर्वश्रेष्ठ प्रदर्शन था।",
  "Ministry of Youth Affairs and Sports and Olympic Council of Asia, 20th Asian Games, Aichi-Nagoya 2026, final medal table.",
  "ca-t4-ca-asian-games-aichi-nagoya-india-fourth-85", craft="recall")

S(NA, "medium", "Lakshadweep was declared 'fully literate' in 2026 under ULLAS (Nav Bharat Saaksharta Karyakram). Consider the following statements:",
  "2026 में लक्षद्वीप को उल्लास (नव भारत साक्षरता कार्यक्रम) के अंतर्गत ‘पूर्ण साक्षर’ घोषित किया गया। निम्नलिखित कथनों पर विचार कीजिए:",
  ["ULLAS is meant for adults aged 15 years and above who missed formal schooling.",
   "Under ULLAS, a region is declared fully literate only when every adult in it has passed the literacy test.",
   "Lakshadweep is the first Union Territory to have been declared fully literate under ULLAS."],
  ["उल्लास 15 वर्ष और उससे अधिक आयु के उन वयस्कों के लिए है जो औपचारिक स्कूली शिक्षा से वंचित रह गए।",
   "उल्लास के अंतर्गत किसी क्षेत्र को पूर्ण साक्षर तभी घोषित किया जाता है जब उसका हर वयस्क साक्षरता परीक्षा उत्तीर्ण कर ले।",
   "लक्षद्वीप उल्लास के अंतर्गत पूर्ण साक्षर घोषित होने वाला पहला केंद्रशासित प्रदेश है।"],
  C3, 0,
  "Only statement 1 is correct. ULLAS -- Understanding of Lifelong Learning for All in Society -- is a centrally sponsored scheme of the Ministry of Education for 2022-27, in line with the National Education Policy 2020; volunteers teach, and learners take a Foundational Literacy and Numeracy Assessment Test. "
  "Statement 2 is wrong: the benchmark is 95 per cent literacy, which the Ministry treats as equivalent to full literacy; the label does not mean that every adult has passed. Statement 3 is wrong: Ladakh was the first administrative unit to be declared fully literate, in June 2024, and Mizoram the first State, in 2025; Lakshadweep, whose literacy was about 92 per cent in the 2011 Census, joined them in 2026 after all the learners it had identified cleared the test.",
  "केवल कथन 1 सही है। उल्लास -- समाज में सभी के लिए आजीवन सीखने की समझ -- 2022-27 के लिए शिक्षा मंत्रालय की केंद्र प्रायोजित योजना है, जो राष्ट्रीय शिक्षा नीति 2020 के अनुरूप है; स्वयंसेवक पढ़ाते हैं और शिक्षार्थी आधारभूत साक्षरता और संख्याज्ञान मूल्यांकन परीक्षा देते हैं। "
  "कथन 2 ग़लत है: मानक 95 प्रतिशत साक्षरता है, जिसे मंत्रालय पूर्ण साक्षरता के समतुल्य मानता है; इस उपाधि का अर्थ यह नहीं कि हर वयस्क उत्तीर्ण हो गया। कथन 3 ग़लत है: जून 2024 में लद्दाख पूर्ण साक्षर घोषित होने वाली पहली प्रशासनिक इकाई और 2025 में मिज़ोरम पहला राज्य बना; 2011 की जनगणना में लगभग 92 प्रतिशत साक्षरता वाला लक्षद्वीप, पहचाने गए सभी शिक्षार्थियों के परीक्षा उत्तीर्ण करने के बाद, 2026 में उनसे जुड़ा।",
  "Ministry of Education, ULLAS - Nav Bharat Saaksharta Karyakram guidelines (2022-27); UT Administration of Lakshadweep, declaration of full literacy (October 2026); Census of India 2011.",
  "ca-t4-ca-ullas-lakshadweep-95-ladakh-first", craft="precision")

finish("ca_t4_a.sql", FORMAT, "2026-Q4", update="--update" in sys.argv)
