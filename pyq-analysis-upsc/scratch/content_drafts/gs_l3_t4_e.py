# -*- coding: utf-8 -*-
"""Level 3 · Test 4 (GS Integrated Test 4) -- part E: Economy (17) (upsc_l3_cell_targets.mjs 4).
Same cell plan as Tests 1-3.
Every fact was grepped against the Level-2 digests, all Level-1 drafts and Level 3 Tests 1-3, and is one none of them
tests: SEBI's curbs on unregistered 'finfluencers'; GIFT Nifty; online
bond platform providers; the RBI's Financial Inclusion Index; the National Manufacturing Mission; the scheme for
electric passenger-car manufacturing; the Electronics Component Manufacturing Scheme; a 'K-shaped' recovery; global bond-index inclusion and passive
inflows; UPI's international linkages and NIPL; the GST composition scheme and inter-State supplies; PM-YASASVI, the
PM Internship Scheme, SHREYAS and PM-DAKSH; the Mission for Aatmanirbharta in Pulses; 'One Nation One Fertiliser'; the
VRRR; the RBI's 2025 directions on gold and silver loans; the States' Consolidated Sinking Fund and Guarantee
Redemption Fund. MCQ keys are pinned (pos). One Statement-I/II/III row (SI3)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Economy"
d.REQUIRE_CRAFT = True
FM = "Financial Markets, Instruments & Fintech"
MB = "Money, Banking & Monetary Policy"
IN = "Industry, Infrastructure, Energy & Services"
EX = "External Sector & International Institutions"
AG = "Agriculture & Food Economy"
RBI = "Reserve Bank of India"
SEBI = "Securities and Exchange Board of India"
NCM = "NCERT Class XII, Introductory Macroeconomics"
MOF = "Ministry of Finance"

# ---------------------------------------------------------------- Financial Markets, Instruments & Fintech (e, h, m, m)
S(FM, "easy", "Consider the following statements about SEBI's rules on financial influencers ('finfluencers'):",
  "वित्तीय प्रभावकों ('फ़िनफ़्लुएंसरों') पर सेबी के नियमों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Entities regulated by SEBI, such as brokers and mutual funds, may not associate with unregistered persons who give investment advice or claim returns.",
   "SEBI has banned all discussion of shares and markets on social-media platforms."],
  ["सेबी द्वारा विनियमित संस्थाएँ, जैसे ब्रोकर और म्यूचुअल फ़ंड, ऐसे अपंजीकृत व्यक्तियों से नहीं जुड़ सकतीं जो निवेश-सलाह देते हैं या रिटर्न का दावा करते हैं।",
   "सेबी ने सोशल-मीडिया मंचों पर शेयरों और बाज़ारों की हर चर्चा पर प्रतिबंध लगा दिया है।"],
  T2, 0,
  "Only statement 1 is correct. In 2024 SEBI told regulated entities and their agents not to have any association -- paid promotion, referrals, revenue sharing -- with people who are not registered with it but who give investment advice or recommendations or make claims of returns, because unregistered tipsters had become a channel for mis-selling and manipulation. "
  "Statement 2 is wrong: SEBI did not ban discussion; people who only educate investors, without advising on specific securities or promising returns, are outside the restriction, and those who wish to advise can register as investment advisers or research analysts.",
  "केवल कथन 1 सही है। 2024 में सेबी ने विनियमित संस्थाओं और उनके एजेंटों से कहा कि वे ऐसे लोगों से किसी प्रकार का संबंध -- भुगतान वाला प्रचार, रेफ़रल, राजस्व-बँटवारा -- न रखें जो उसके पास पंजीकृत नहीं हैं पर निवेश-सलाह या सिफ़ारिशें देते हैं या रिटर्न का दावा करते हैं, क्योंकि अपंजीकृत टिप देने वाले ग़लत बिक्री और हेरफेर का माध्यम बन गए थे। "
  "कथन 2 ग़लत है: सेबी ने चर्चा पर रोक नहीं लगाई; जो लोग विशिष्ट प्रतिभूतियों पर सलाह दिए या रिटर्न का वादा किए बिना केवल निवेशकों को शिक्षित करते हैं, वे इस प्रतिबंध से बाहर हैं, और जो सलाह देना चाहते हैं वे निवेश सलाहकार या अनुसंधान विश्लेषक के रूप में पंजीकरण करा सकते हैं।",
  SEBI + ": circular on association with unregistered persons (2024); SEBI (Investment Advisers) and (Research Analysts) Regulations.",
  "l3-t4-eco-sebi-finfluencers", craft="recall")

S(FM, "hard", "With reference to 'GIFT Nifty', consider the following statements:",
  "'गिफ़्ट निफ़्टी' के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Trading in Nifty-linked derivatives that used to take place on the Singapore Exchange moved in 2023 to the NSE International Exchange in GIFT City.",
   "Its contracts are denominated in US dollars.",
   "It trades for about 21 hours a day across two sessions.",
   "Orders from members of the Singapore Exchange reach it through a 'connect' arrangement between the two exchanges."],
  ["सिंगापुर एक्सचेंज पर होने वाला निफ़्टी-आधारित व्युत्पन्नों का कारोबार 2023 में गिफ़्ट सिटी के NSE इंटरनेशनल एक्सचेंज पर आ गया।",
   "इसके अनुबंध अमेरिकी डॉलर में अंकित होते हैं।",
   "इसमें दो सत्रों में प्रतिदिन लगभग 21 घंटे कारोबार होता है।",
   "सिंगापुर एक्सचेंज के सदस्यों के ऑर्डर दोनों एक्सचेंजों के बीच एक 'कनेक्ट' व्यवस्था से इस तक पहुँचते हैं।"],
  C4, 3,
  "All four statements are correct. For years the most liquid offshore contract on Indian equities, 'SGX Nifty', traded in Singapore, so price discovery and the business it brought sat outside India; under an agreement between NSE and SGX, the contracts were moved to NSE IX in the International Financial Services Centre at GIFT City in July 2023 and renamed GIFT Nifty, with SGX members' orders routed there through the NSE IX-SGX Connect. "
  "Being in the IFSC, the contracts are dollar-denominated and open to foreign investors and eligible residents, and the long trading hours let global investors react to news while Indian exchanges are shut -- which is why GIFT Nifty is watched as an early indicator of how the domestic market will open.",
  "चारों कथन सही हैं। वर्षों तक भारतीय शेयरों पर सबसे तरल विदेशी अनुबंध, 'SGX निफ़्टी', सिंगापुर में कारोबार करता रहा, इसलिए मूल्य-निर्धारण और उससे आने वाला कारोबार भारत से बाहर रहा; NSE और SGX के बीच समझौते के अंतर्गत जुलाई 2023 में ये अनुबंध गिफ़्ट सिटी के अंतरराष्ट्रीय वित्तीय सेवा केंद्र में NSE IX पर लाए गए और इनका नाम गिफ़्ट निफ़्टी हुआ, और SGX सदस्यों के ऑर्डर NSE IX-SGX कनेक्ट के माध्यम से वहाँ पहुँचते हैं। "
  "IFSC में होने के कारण अनुबंध डॉलर में अंकित हैं और विदेशी निवेशकों तथा पात्र निवासियों के लिए खुले हैं, और लंबे कारोबारी घंटे वैश्विक निवेशकों को भारतीय एक्सचेंजों के बंद रहने पर भी समाचारों पर प्रतिक्रिया देने देते हैं -- इसीलिए गिफ़्ट निफ़्टी को इस बात के आरंभिक संकेतक के रूप में देखा जाता है कि घरेलू बाज़ार कैसे खुलेगा।",
  "NSE International Exchange (NSE IX); International Financial Services Centres Authority; National Stock Exchange of India.",
  "l3-t4-eco-gift-nifty", craft="linkage")

S(FM, "medium", "Consider the following statements about online bond platform providers (OBPPs) in India:",
  "भारत में ऑनलाइन बॉन्ड प्लेटफ़ॉर्म प्रदाताओं (OBPP) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["They must be registered with SEBI as stock brokers.",
   "Bonds bought through them carry a guarantee from the Government of India.",
   "They may sell only government securities, not corporate bonds."],
  ["उन्हें सेबी के पास स्टॉक ब्रोकर के रूप में पंजीकृत होना होता है।",
   "उनके माध्यम से ख़रीदे गए बॉन्ड पर भारत सरकार की गारंटी होती है।",
   "वे केवल सरकारी प्रतिभूतियाँ बेच सकते हैं, कॉरपोरेट बॉन्ड नहीं।"],
  C3, 0,
  "Only statement 1 is correct. As apps selling bonds to retail investors multiplied, SEBI brought them under regulation in 2022: an online bond platform must be a SEBI-registered stock broker in the debt segment, may offer only listed (or to-be-listed) debt securities, and must route trades through the exchanges' settlement systems, which protects investors' money. "
  "Statements 2 and 3 are wrong: most products on these platforms are corporate bonds, whose repayment depends on the issuer, so credit ratings and default risk matter; the platform does not guarantee anything, and only government securities carry the sovereign promise. SEBI has also cut the face value of privately placed corporate bonds to draw in small investors.",
  "केवल कथन 1 सही है। जैसे-जैसे खुदरा निवेशकों को बॉन्ड बेचने वाले ऐप बढ़े, सेबी ने 2022 में उन्हें विनियमन में लाया: ऑनलाइन बॉन्ड प्लेटफ़ॉर्म को ऋण खंड में सेबी-पंजीकृत स्टॉक ब्रोकर होना चाहिए, वह केवल सूचीबद्ध (या सूचीबद्ध होने वाली) ऋण प्रतिभूतियाँ दे सकता है, और सौदे एक्सचेंजों की निपटान प्रणाली से होने चाहिए, जो निवेशकों के पैसे की रक्षा करता है। "
  "कथन 2 और 3 ग़लत हैं: इन मंचों पर अधिकांश उत्पाद कॉरपोरेट बॉन्ड हैं, जिनकी वापसी जारीकर्ता पर निर्भर है, इसलिए क्रेडिट रेटिंग और चूक का जोखिम मायने रखते हैं; मंच कोई गारंटी नहीं देता, और केवल सरकारी प्रतिभूतियों पर संप्रभु वचन होता है। सेबी ने छोटे निवेशकों को आकर्षित करने के लिए निजी रूप से रखे गए कॉरपोरेट बॉन्डों का अंकित मूल्य भी घटाया है।",
  SEBI + ": framework for online bond platform providers (2022) and circulars on the face value of debt securities.",
  "l3-t4-eco-online-bond-platforms", craft="precision")

S(FM, "medium", "Consider the following statements about the Reserve Bank of India's Financial Inclusion Index (FI-Index):",
  "भारतीय रिज़र्व बैंक के वित्तीय समावेशन सूचकांक (FI-Index) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is published by the RBI every year.",
   "It is measured on a scale from 0 to 100.",
   "It has three parameters -- access, usage and quality -- of which usage carries the largest weight.",
   "It covers banking, investments, insurance, postal services and pensions."],
  ["इसे RBI हर वर्ष प्रकाशित करता है।",
   "इसे 0 से 100 के पैमाने पर मापा जाता है।",
   "इसके तीन मानदंड हैं -- पहुँच, उपयोग और गुणवत्ता -- जिनमें उपयोग का भार सबसे अधिक है।",
   "इसमें बैंकिंग, निवेश, बीमा, डाक सेवाएँ और पेंशन शामिल हैं।"],
  C4, 3,
  "All four statements are correct. The RBI introduced the FI-Index in 2021 and publishes it each July for the year ending March, with 0 meaning complete exclusion and 100 full inclusion. Its three parameters are access (35 per cent), usage (45 per cent) and quality (20 per cent), the last capturing financial literacy, consumer protection and inequalities in service. "
  "Weighting usage most heavily is deliberate: India's account-opening drives, such as Jan Dhan, had already widened access, so the index is designed to show whether people actually use the accounts, insurance and pension products open to them; it has risen every year since its launch.",
  "चारों कथन सही हैं। RBI ने 2021 में FI-Index शुरू किया और वह हर जुलाई मार्च में समाप्त वर्ष के लिए इसे प्रकाशित करता है, जिसमें 0 का अर्थ पूर्ण बहिष्करण और 100 का पूर्ण समावेशन है। इसके तीन मानदंड पहुँच (35 प्रतिशत), उपयोग (45 प्रतिशत) और गुणवत्ता (20 प्रतिशत) हैं, अंतिम में वित्तीय साक्षरता, उपभोक्ता संरक्षण और सेवा की असमानताएँ आती हैं। "
  "उपयोग को सबसे अधिक भार देना सोच-समझकर किया गया है: जन धन जैसे खाता-खोलो अभियानों ने पहुँच पहले ही बढ़ा दी थी, इसलिए सूचकांक यह दिखाने के लिए बना है कि लोग अपने लिए उपलब्ध खातों, बीमा और पेंशन उत्पादों का वास्तव में उपयोग करते हैं या नहीं; अपनी शुरुआत से यह हर वर्ष बढ़ा है।",
  RBI + ": Financial Inclusion Index (press releases, 2021 onwards).",
  "l3-t4-eco-rbi-fi-index", craft="multi")

# ---------------------------------------------------------------- Industry, Infrastructure, Energy & Services (e-stmt, m-MCQ, m-stmt)
S(IN, "easy", "Consider the following statements about the National Manufacturing Mission announced in the Union Budget 2025-26:",
  "केंद्रीय बजट 2025-26 में घोषित राष्ट्रीय विनिर्माण मिशन के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is meant to cover small, medium and large industries under 'Make in India'.",
   "Its focus includes clean-technology manufacturing, such as solar cells, electric-vehicle batteries and electrolysers."],
  ["इसका उद्देश्य 'मेक इन इंडिया' के अंतर्गत छोटे, मध्यम और बड़े उद्योगों को शामिल करना है।",
   "इसके केंद्र में स्वच्छ-प्रौद्योगिकी विनिर्माण शामिल है, जैसे सौर सेल, विद्युत-वाहन बैटरियाँ और इलेक्ट्रोलाइज़र।"],
  T2, 2,
  "Both statements are correct. The Budget announced the mission to give policy support, execution roadmaps and a governance and monitoring framework to Central ministries and States for manufacturing across firm sizes, as a step towards raising manufacturing's share of the economy. "
  "It singled out clean-tech manufacturing -- solar PV cells, EV batteries, motors and controllers, electrolysers, wind turbines, very-high-voltage transmission equipment and grid-scale batteries -- so that India's energy transition does not depend on imported equipment, a concern sharpened by the concentration of such supply chains in a few countries.",
  "दोनों कथन सही हैं। बजट ने इस मिशन की घोषणा केंद्रीय मंत्रालयों और राज्यों को हर आकार की फ़र्मों के विनिर्माण के लिए नीतिगत सहायता, क्रियान्वयन रोडमैप और शासन व निगरानी ढाँचा देने के लिए की, अर्थव्यवस्था में विनिर्माण का हिस्सा बढ़ाने की दिशा में एक क़दम के रूप में। "
  "इसने स्वच्छ-तकनीक विनिर्माण -- सौर PV सेल, EV बैटरियाँ, मोटर और नियंत्रक, इलेक्ट्रोलाइज़र, पवन टर्बाइन, अति-उच्च वोल्टेज पारेषण उपकरण और ग्रिड-स्तरीय बैटरियाँ -- को विशेष रूप से चुना, ताकि भारत का ऊर्जा-संक्रमण आयातित उपकरणों पर निर्भर न रहे, यह चिंता ऐसी आपूर्ति-शृंखलाओं के कुछ ही देशों में केंद्रित होने से और तीखी हुई है।",
  MOF + ": Budget Speech 2025-26.",
  "l3-t4-eco-national-manufacturing-mission", craft="recall")

M(IN, "medium",
  "Under the 2024 scheme to promote the manufacture of electric passenger cars in India, a company that commits a large minimum investment and agrees to rising local value addition is allowed to:",
  "भारत में विद्युत यात्री कारों के निर्माण को बढ़ावा देने वाली 2024 की योजना के अंतर्गत, बड़े न्यूनतम निवेश और बढ़ते स्थानीय मूल्य-वर्धन के लिए वचनबद्ध कंपनी को क्या करने की अनुमति है?",
  ["import a limited number of fully built electric cars at a reduced customs duty of 15 per cent",
   "receive a subsidy of five lakh rupees on every electric car it sells to private buyers in India",
   "sell its electric cars free of GST for five years from the start of local production",
   "sell its electric cars only to government departments and public-sector fleets"],
  ["सीमित संख्या में पूरी बनी विद्युत कारें 15 प्रतिशत की घटी सीमा-शुल्क दर पर आयात करना",
   "भारत में निजी ख़रीदारों को बेची गई अपनी हर विद्युत कार पर केंद्र से पाँच लाख रुपये की सब्सिडी पाना",
   "स्थानीय उत्पादन शुरू होने से पाँच वर्ष तक अपनी विद्युत कारें बिना GST के बेचना",
   "अपनी विद्युत कारें केवल सरकारी विभागों और सार्वजनिक क्षेत्र के बेड़ों को बेचना"],
  0,
  "The scheme, notified in 2024, lets an approved manufacturer import completely built electric cars above a minimum price at a concessional 15 per cent customs duty for five years and up to a yearly cap -- provided it invests at least about 4,150 crore rupees in Indian manufacturing and reaches 25 per cent domestic value addition within three years and 50 per cent within five. "
  "The idea is to use limited duty relief to attract global EV makers to build plants and supply chains in India, rather than to subsidise sales; demand-side support for two- and three-wheelers, buses and trucks comes through a separate scheme, and private electric cars get no purchase subsidy from the Centre.",
  "2024 में अधिसूचित यह योजना स्वीकृत निर्माता को एक न्यूनतम कीमत से ऊपर की पूरी बनी विद्युत कारें 15 प्रतिशत की रियायती सीमा-शुल्क दर पर, पाँच वर्ष तक और वार्षिक सीमा के भीतर, आयात करने देती है -- बशर्ते वह भारतीय विनिर्माण में कम-से-कम लगभग 4,150 करोड़ रुपये निवेश करे और तीन वर्ष में 25 प्रतिशत तथा पाँच वर्ष में 50 प्रतिशत घरेलू मूल्य-वर्धन तक पहुँचे। "
  "उद्देश्य बिक्री पर सब्सिडी देने के बजाय सीमित शुल्क-राहत से वैश्विक EV निर्माताओं को भारत में संयंत्र और आपूर्ति-शृंखलाएँ बनाने के लिए आकर्षित करना है; दोपहिया, तिपहिया, बसों और ट्रकों के लिए माँग-पक्ष सहायता एक अलग योजना से आती है, और निजी विद्युत कारों को केंद्र से कोई ख़रीद सब्सिडी नहीं मिलती।",
  "Ministry of Heavy Industries: Scheme to Promote Manufacturing of Electric Passenger Cars in India (2024).",
  "l3-t4-eco-ev-car-manufacturing-scheme", pos=0, craft="application")

S(IN, "medium", "Consider the following statements about the Electronics Component Manufacturing Scheme:",
  "इलेक्ट्रॉनिक्स कंपोनेंट विनिर्माण योजना के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It was approved in 2025 to build a domestic base for electronic components and sub-assemblies, not just the assembly of finished devices.",
   "Its incentives are linked to turnover, to capital expenditure, or to a mix of the two.",
   "It covers items such as printed circuit boards, camera and display modules, and passive components such as capacitors."],
  ["इसे 2025 में स्वीकृति दी गई, ताकि केवल तैयार उपकरणों की असेंबली नहीं, बल्कि इलेक्ट्रॉनिक घटकों और उप-असेंबलियों का घरेलू आधार बने।",
   "इसके प्रोत्साहन कारोबार से, पूँजीगत व्यय से, या दोनों के मिश्रण से जुड़े हैं।",
   "इसमें मुद्रित परिपथ बोर्ड, कैमरा और डिस्प्ले मॉड्यूल, और संधारित्र जैसे निष्क्रिय घटक शामिल हैं।"],
  C3, 2,
  "All three statements are correct. The production-linked incentive scheme for mobile phones made India a large assembler and exporter of handsets, but most components were still imported, so domestic value addition stayed low; the component scheme, approved in March 2025, targets that gap with incentives over six years. "
  "Depending on the category, support is tied to incremental turnover, to capital investment in plant and machinery, or to both, and the list runs from bare components such as multi-layer PCBs and passive components to sub-assemblies such as display and camera modules and the capital equipment used to make them -- the layers of the supply chain that decide how much of a device's value stays in the country.",
  "तीनों कथन सही हैं। मोबाइल फ़ोनों की उत्पादन-संबद्ध प्रोत्साहन योजना ने भारत को हैंडसेट का बड़ा असेंबलर और निर्यातक बनाया, पर अधिकांश घटक अब भी आयात होते थे, इसलिए घरेलू मूल्य-वर्धन कम रहा; मार्च 2025 में स्वीकृत घटक योजना छह वर्षों के प्रोत्साहनों से इसी कमी को लक्षित करती है। "
  "श्रेणी के अनुसार सहायता बढ़े हुए कारोबार से, संयंत्र और मशीनरी में पूँजी-निवेश से, या दोनों से जुड़ी है, और सूची बहु-परतीय PCB और निष्क्रिय घटकों जैसे मूल घटकों से लेकर डिस्प्ले और कैमरा मॉड्यूल जैसी उप-असेंबलियों और उन्हें बनाने के पूँजीगत उपकरणों तक जाती है -- आपूर्ति-शृंखला की वे परतें जो तय करती हैं कि किसी उपकरण के मूल्य का कितना भाग देश में रहता है।",
  "Ministry of Electronics and Information Technology: Electronics Component Manufacturing Scheme (Cabinet approval, March 2025).",
  "l3-t4-eco-electronics-component-scheme", craft="linkage")

# ---------------------------------------------------------------- Macro Concepts (e-SI)
A("Macro Concepts, National Income & Inflation", "easy",
  "A 'K-shaped' recovery describes an economy in which some sectors and groups recover quickly after a downturn while others continue to decline.",
  "'K-आकार' की बहाली ऐसी अर्थव्यवस्था का वर्णन करती है जिसमें मंदी के बाद कुछ क्षेत्र और समूह तेज़ी से उबरते हैं जबकि अन्य गिरते रहते हैं।",
  "In a K-shaped recovery, the economy's total output necessarily keeps contracting.",
  "K-आकार की बहाली में अर्थव्यवस्था का कुल उत्पादन अनिवार्य रूप से सिकुड़ता रहता है।",
  2,
  "Statement I is correct but Statement II is wrong. The letter K captures divergence: the upper arm stands for sectors and households that bounce back or prosper -- after the pandemic, for instance, digital services, large listed firms and asset-owners -- and the lower arm for those that keep losing ground, such as informal workers and contact-intensive small businesses. "
  "Aggregate GDP can grow strongly during a K-shaped recovery; the term is about the distribution of the recovery, which is why it is used to argue for targeted support rather than to describe a recession. V-, U-, W- and L-shaped recoveries, by contrast, describe the path of total output.",
  "कथन I सही है पर कथन II ग़लत है। अक्षर K विचलन को दर्शाता है: ऊपरी भुजा उन क्षेत्रों और परिवारों को दर्शाती है जो उछलकर उबरते या समृद्ध होते हैं -- जैसे महामारी के बाद डिजिटल सेवाएँ, बड़ी सूचीबद्ध फ़र्में और परिसंपत्ति-स्वामी -- और निचली भुजा उन्हें जो पिछड़ते रहते हैं, जैसे अनौपचारिक श्रमिक और संपर्क-आधारित छोटे व्यवसाय। "
  "K-आकार की बहाली के दौरान कुल GDP तेज़ी से बढ़ सकता है; यह शब्द बहाली के वितरण से संबंधित है, इसीलिए इसका उपयोग मंदी का वर्णन करने के बजाय लक्षित सहायता के पक्ष में तर्क देने में होता है। इसके विपरीत V, U, W और L आकार की बहालियाँ कुल उत्पादन के मार्ग का वर्णन करती हैं।",
  NCM + "; " + MOF + ", Economic Survey.",
  "l3-t4-eco-k-shaped-recovery", craft="inference")

# ---------------------------------------------------------------- External Sector & International Institutions (e-SI, m-stmt)
A(EX, "easy",
  "The inclusion of Indian government bonds in global bond indices was expected to bring large foreign portfolio inflows.",
  "वैश्विक बॉन्ड सूचकांकों में भारतीय सरकारी बॉन्डों के शामिल होने से बड़े विदेशी पोर्टफ़ोलियो अंतर्वाह आने की अपेक्षा थी।",
  "Funds that passively track such an index must buy the included bonds in proportion to their weight in the index.",
  "ऐसे सूचकांक का निष्क्रिय रूप से अनुसरण करने वाले फ़ंडों को शामिल बॉन्डों को सूचकांक में उनके भार के अनुपात में ख़रीदना पड़ता है।",
  0,
  "Both statements are correct and Statement II explains Statement I. Indian government securities issued under the Fully Accessible Route, which carries no limit on foreign ownership, were added to J.P. Morgan's emerging-market government bond index from June 2024, building up to a 10 per cent weight, and later to Bloomberg and FTSE emerging-market indices. "
  "Because index-tracking funds must hold each country's bonds at its index weight, inclusion brings fairly predictable 'passive' demand, lowering borrowing costs and deepening the market; the flip side is that these flows can reverse if India's weight or global conditions change, which is why the RBI watches them closely.",
  "दोनों कथन सही हैं और कथन II, कथन I की व्याख्या करता है। पूर्णतः सुलभ मार्ग के अंतर्गत जारी भारतीय सरकारी प्रतिभूतियाँ, जिन पर विदेशी स्वामित्व की कोई सीमा नहीं है, जून 2024 से जे.पी. मॉर्गन के उभरते-बाज़ार सरकारी बॉन्ड सूचकांक में जोड़ी गईं, जिनका भार बढ़ते हुए 10 प्रतिशत तक पहुँचा, और बाद में ब्लूमबर्ग और FTSE के उभरते-बाज़ार सूचकांकों में भी। "
  "चूँकि सूचकांक का अनुसरण करने वाले फ़ंडों को हर देश के बॉन्ड उसके सूचकांक-भार पर रखने होते हैं, शामिल होने से अपेक्षाकृत पूर्वानुमेय 'निष्क्रिय' माँग आती है, जिससे उधार लेने की लागत घटती है और बाज़ार गहरा होता है; दूसरा पहलू यह है कि भारत का भार या वैश्विक परिस्थितियाँ बदलने पर ये प्रवाह उलट सकते हैं, इसीलिए RBI उन पर बारीकी से नज़र रखता है।",
  RBI + ": Fully Accessible Route for non-residents (2020); " + MOF + ", Economic Survey 2024-25.",
  "l3-t4-eco-bond-index-inclusion-passive", craft="linkage")

S(EX, "medium", "Consider the following statements about the Unified Payments Interface (UPI) beyond India:",
  "भारत से बाहर एकीकृत भुगतान इंटरफ़ेस (UPI) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["UPI has been linked with Singapore's PayNow for real-time cross-border remittances.",
   "UPI payments are accepted at merchants in several countries, including the UAE, Bhutan, Nepal, Sri Lanka, Mauritius and France.",
   "NPCI International Payments Limited, a subsidiary of the National Payments Corporation of India, promotes UPI abroad.",
   "NPCI International has agreed to help countries such as Namibia build real-time payment systems modelled on UPI."],
  ["UPI को वास्तविक-समय सीमा-पार प्रेषण के लिए सिंगापुर के PayNow से जोड़ा गया है।",
   "कई देशों में व्यापारियों के पास UPI भुगतान स्वीकार किए जाते हैं, जिनमें UAE, भूटान, नेपाल, श्रीलंका, मॉरीशस और फ़्रांस शामिल हैं।",
   "भारतीय राष्ट्रीय भुगतान निगम की सहायक कंपनी, NPCI इंटरनेशनल पेमेंट्स लिमिटेड, विदेशों में UPI का प्रसार करती है।",
   "NPCI इंटरनेशनल ने नामीबिया जैसे देशों को UPI के मॉडल पर वास्तविक-समय भुगतान प्रणालियाँ बनाने में मदद करने पर सहमति दी है।"],
  C4, 3,
  "All four statements are correct. The UPI-PayNow link, launched in 2023, was the first to connect two countries' fast-payment systems for person-to-person remittances; merchant acceptance has since spread to tourist and remittance corridors, and in France UPI first worked at the Eiffel Tower. "
  "NPCI International, set up in 2020, pursues three routes -- accepting UPI abroad, linking it with other fast-payment systems, and helping central banks such as Namibia's build their own UPI-like systems. This is also part of India's push to cut the cost of remittances and to export its digital public infrastructure.",
  "चारों कथन सही हैं। 2023 में शुरू हुआ UPI-PayNow लिंक व्यक्ति-से-व्यक्ति प्रेषण के लिए दो देशों की त्वरित-भुगतान प्रणालियों को जोड़ने वाला पहला था; तब से व्यापारियों द्वारा स्वीकार्यता पर्यटन और प्रेषण गलियारों में फैली है, और फ़्रांस में UPI पहले एफ़िल टावर पर चला। "
  "2020 में स्थापित NPCI इंटरनेशनल तीन रास्ते अपनाती है -- विदेश में UPI की स्वीकार्यता, इसे अन्य त्वरित-भुगतान प्रणालियों से जोड़ना, और नामीबिया जैसे केंद्रीय बैंकों को UPI जैसी अपनी प्रणालियाँ बनाने में मदद करना। यह प्रेषण की लागत घटाने और भारत के डिजिटल सार्वजनिक ढाँचे के निर्यात के प्रयास का भी हिस्सा है।",
  "National Payments Corporation of India; " + RBI + ", Payment Systems Report.",
  "l3-t4-eco-upi-international-nipl", craft="multi")

# ---------------------------------------------------------------- Taxation & Fiscal Federalism (h-SI3)
A("Taxation & Fiscal Federalism", "hard",
  "A dealer who has opted for the GST composition scheme cannot make inter-State supplies of goods.",
  "GST संयोजन (कंपोज़िशन) योजना चुनने वाला व्यापारी वस्तुओं की अंतर-राज्यीय आपूर्ति नहीं कर सकता।",
  "A composition dealer cannot issue tax invoices or pass on input tax credit, whereas inter-State supplies are taxed under IGST, whose credit must flow to the destination State.",
  "संयोजन व्यापारी कर-बीजक जारी नहीं कर सकता या इनपुट टैक्स क्रेडिट आगे नहीं दे सकता, जबकि अंतर-राज्यीय आपूर्तियों पर IGST लगता है, जिसका क्रेडिट गंतव्य राज्य तक पहुँचना चाहिए।",
  2,
  "Statements I and II are correct and II explains I; Statement III is wrong, so the answer is (c). The composition scheme lets small taxpayers -- turnover up to 1.5 crore rupees in most States -- pay a low flat rate on turnover with minimal paperwork, but in return they stay outside the input-tax-credit chain: they issue a bill of supply, cannot charge GST to buyers and cannot claim credit. "
  "Since IGST on an inter-State sale is apportioned to the consuming State through the credit chain, the law bars composition dealers from making inter-State outward supplies. Statement III is wrong: manufacturers of ice cream, pan masala and tobacco products are specifically excluded from the scheme, which is meant for small traders, restaurants and manufacturers of ordinary goods.",
  "कथन I और II सही हैं और II, I की व्याख्या करता है; कथन III ग़लत है, इसलिए उत्तर (ग) है। संयोजन योजना छोटे करदाताओं को -- अधिकांश राज्यों में 1.5 करोड़ रुपये तक के कारोबार वाले -- न्यूनतम काग़ज़ी कार्रवाई के साथ कारोबार पर कम सपाट दर से कर देने देती है, पर बदले में वे इनपुट-टैक्स-क्रेडिट शृंखला से बाहर रहते हैं: वे आपूर्ति का बिल जारी करते हैं, ख़रीदारों से GST नहीं ले सकते और क्रेडिट का दावा नहीं कर सकते। "
  "चूँकि अंतर-राज्यीय बिक्री पर IGST क्रेडिट शृंखला के माध्यम से उपभोग करने वाले राज्य को बाँटा जाता है, क़ानून संयोजन व्यापारियों को अंतर-राज्यीय बाहरी आपूर्ति से रोकता है। कथन III ग़लत है: आइसक्रीम, पान मसाला और तंबाकू उत्पादों के निर्माता योजना से विशेष रूप से बाहर रखे गए हैं, जो छोटे व्यापारियों, रेस्तराँ और सामान्य वस्तुओं के निर्माताओं के लिए बनी है।",
  "Central Goods and Services Tax Act, 2017, section 10; Integrated Goods and Services Tax Act, 2017; CBIC notifications on the composition levy.",
  "l3-t4-eco-gst-composition-inter-state",
  s3="The composition scheme is open to manufacturers of ice cream, pan masala and tobacco products.",
  s3_hi="संयोजन योजना आइसक्रीम, पान मसाला और तंबाकू उत्पादों के निर्माताओं के लिए खुली है।",
  craft="inference")

# ---------------------------------------------------------------- Inclusive Growth, Welfare & Demography (h-pairs)
P("Inclusive Growth, Welfare & Demography", "hard", "Consider the following pairs of schemes and what they provide:",
  "योजनाओं और वे जो प्रदान करती हैं, उनके निम्नलिखित युग्मों पर विचार कीजिए:",
  ["PM-YASASVI : Scholarships for students from Other Backward Classes, Economically Backward Classes and De-notified Tribes",
   "PM Internship Scheme : Internships in leading companies for young people aged 21 to 24",
   "SHREYAS : Pensions for elderly workers in the unorganised sector",
   "PM-DAKSH : Collateral-free working-capital loans for street vendors"],
  ["पीएम-यशस्वी : अन्य पिछड़ा वर्ग, आर्थिक रूप से पिछड़े वर्गों और विमुक्त जनजातियों के विद्यार्थियों के लिए छात्रवृत्तियाँ",
   "पीएम इंटर्नशिप योजना : 21 से 24 वर्ष के युवाओं के लिए प्रमुख कंपनियों में इंटर्नशिप",
   "श्रेयस : असंगठित क्षेत्र के वृद्ध श्रमिकों के लिए पेंशन",
   "पीएम-दक्ष : रेहड़ी-पटरी वालों के लिए बिना ज़मानत कार्यशील-पूँजी ऋण"],
  1,
  "Only the first two pairs are correct. PM-YASASVI is the umbrella of pre- and post-matric and top-class scholarships for OBC, EBC and DNT students; the PM Internship Scheme, announced in the 2024-25 Budget, places young people aged 21 to 24 who are not in full-time work or study in top companies for a year with a monthly stipend. "
  "SHREYAS (Scholarships for Higher Education for Young Achievers) is an umbrella of scholarships, free coaching and overseas study support for Scheduled Caste students, not a pension; and PM-DAKSH provides skill training to marginalised groups such as SCs, OBCs, De-notified Tribes and sanitation workers -- collateral-free loans for street vendors come under PM SVANidhi.",
  "केवल पहले दो युग्म सही हैं। पीएम-यशस्वी OBC, EBC और DNT विद्यार्थियों के लिए प्री- और पोस्ट-मैट्रिक तथा उच्च-स्तरीय छात्रवृत्तियों की छत्र योजना है; 2024-25 के बजट में घोषित पीएम इंटर्नशिप योजना 21 से 24 वर्ष के उन युवाओं को, जो पूर्णकालिक काम या पढ़ाई में नहीं हैं, मासिक भत्ते के साथ एक वर्ष के लिए शीर्ष कंपनियों में भेजती है। "
  "श्रेयस (युवा उपलब्धि-प्राप्तकर्ताओं के लिए उच्च शिक्षा छात्रवृत्ति) अनुसूचित जाति के विद्यार्थियों के लिए छात्रवृत्तियों, मुफ़्त कोचिंग और विदेश-अध्ययन सहायता की छत्र योजना है, पेंशन नहीं; और पीएम-दक्ष अनुसूचित जातियों, OBC, विमुक्त जनजातियों और सफ़ाई कर्मियों जैसे वंचित समूहों को कौशल प्रशिक्षण देती है -- रेहड़ी-पटरी वालों के लिए बिना ज़मानत ऋण पीएम स्वनिधि के अंतर्गत आते हैं।",
  "Ministry of Social Justice and Empowerment; Ministry of Corporate Affairs (PM Internship Scheme); " + MOF + ", Budget Speech 2024-25.",
  "l3-t4-eco-yasasvi-internship-shreyas-daksh", craft="precision")

# ---------------------------------------------------------------- Agriculture & Food Economy (m-MCQ, m-stmt)
M(AG, "medium",
  "The 'Mission for Aatmanirbharta in Pulses' announced in the Union Budget 2025-26 gives special focus to which of the following?",
  "केंद्रीय बजट 2025-26 में घोषित 'दलहन में आत्मनिर्भरता मिशन' निम्नलिखित में से किन पर विशेष ध्यान देता है?",
  ["Chana and moong",
   "Rajma and kabuli chana grown for export",
   "Soybean and groundnut",
   "Tur, urad and masoor"],
  ["चना और मूँग",
   "निर्यात के लिए उगाए जाने वाले राजमा और काबुली चना",
   "सोयाबीन और मूँगफली",
   "तूर (अरहर), उड़द और मसूर"],
  3,
  "The six-year mission targets the pulses India imports most -- tur (arhar), urad and masoor -- through climate-resilient seeds, better productivity and post-harvest support, and the Budget promised that central agencies such as NAFED and NCCF would buy these three pulses from registered farmers, as much as offered, for four years. "
  "Assured procurement addresses the main reason farmers avoid pulses -- price risk compared with irrigated rice and wheat -- while chana and moong, where India is close to self-sufficient, are not its focus; soybean and groundnut are oilseeds, covered by the edible-oils mission.",
  "छह वर्षीय यह मिशन उन दालों को लक्षित करता है जिनका भारत सबसे अधिक आयात करता है -- तूर (अरहर), उड़द और मसूर -- जलवायु-सहनशील बीजों, बेहतर उत्पादकता और कटाई-उपरांत सहायता के माध्यम से, और बजट ने वादा किया कि NAFED और NCCF जैसी केंद्रीय एजेंसियाँ चार वर्ष तक पंजीकृत किसानों से ये तीन दालें, जितनी भी पेश की जाएँ, ख़रीदेंगी। "
  "सुनिश्चित ख़रीद उस मुख्य कारण को संबोधित करती है जिससे किसान दालों से बचते हैं -- सिंचित धान और गेहूँ की तुलना में मूल्य जोखिम -- जबकि चना और मूँग, जिनमें भारत लगभग आत्मनिर्भर है, इसके केंद्र में नहीं हैं; सोयाबीन और मूँगफली तिलहन हैं, जो खाद्य तेल मिशन के अंतर्गत आते हैं।",
  MOF + ": Budget Speech 2025-26; Ministry of Agriculture and Farmers Welfare.",
  "l3-t4-eco-pulses-mission-tur-urad-masoor", pos=3, craft="application")

S(AG, "medium", "Consider the following statements about the fertiliser reforms launched in 2022:",
  "2022 में शुरू किए गए उर्वरक सुधारों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Under 'One Nation One Fertiliser', subsidised fertilisers are sold in bags carrying a single brand name, 'Bharat'.",
   "Pradhan Mantri Kisan Samriddhi Kendras convert fertiliser retail shops into one-stop centres offering farm inputs, soil testing and advice.",
   "The reforms ended the government subsidy on urea."],
  ["'एक राष्ट्र एक उर्वरक' के अंतर्गत रियायती उर्वरक एक ही ब्रांड नाम, 'भारत', वाले बोरों में बेचे जाते हैं।",
   "प्रधानमंत्री किसान समृद्धि केंद्र उर्वरक की खुदरा दुकानों को कृषि-आदान, मृदा परीक्षण और सलाह देने वाले एक ही स्थान के केंद्रों में बदलते हैं।",
   "इन सुधारों ने यूरिया पर सरकारी सब्सिडी समाप्त कर दी।"],
  C3, 1,
  "Statements 1 and 2 are correct. Since the Centre pays a large subsidy on urea and on phosphatic and potassic fertilisers, it argued that companies should not compete through brands for products whose price the State largely bears; from 2022 urea, DAP, MOP and NPK are sold under the 'Bharat' name, with the company's name in smaller print, which also eases movement of stocks between regions. "
  "Statement 3 is wrong: urea remains under a statutory maximum retail price, with the government paying the gap between the cost of supply and that price, while the nutrient-based subsidy covers the other fertilisers. The Kisan Samriddhi Kendras are meant to turn input shops into advisory points as well.",
  "कथन 1 और 2 सही हैं। चूँकि केंद्र यूरिया और फ़ॉस्फ़ेटिक तथा पोटैशिक उर्वरकों पर भारी सब्सिडी देता है, उसका तर्क था कि कंपनियों को उन उत्पादों के लिए ब्रांडों से प्रतिस्पर्धा नहीं करनी चाहिए जिनकी कीमत का बड़ा भाग राज्य वहन करता है; 2022 से यूरिया, DAP, MOP और NPK 'भारत' नाम से बिकते हैं, कंपनी का नाम छोटे अक्षरों में रहता है, जिससे क्षेत्रों के बीच भंडार ले जाना भी आसान होता है। "
  "कथन 3 ग़लत है: यूरिया वैधानिक अधिकतम खुदरा मूल्य के अंतर्गत बना हुआ है, और आपूर्ति-लागत तथा उस मूल्य के अंतर का भुगतान सरकार करती है, जबकि पोषक-तत्व आधारित सब्सिडी अन्य उर्वरकों को शामिल करती है। किसान समृद्धि केंद्रों का उद्देश्य आदान-दुकानों को सलाह-केंद्र भी बनाना है।",
  "Department of Fertilizers: One Nation One Fertiliser (Pradhanmantri Bhartiya Janurvarak Pariyojana) and PM Kisan Samriddhi Kendras (2022).",
  "l3-t4-eco-one-nation-one-fertiliser", craft="precision")

# ---------------------------------------------------------------- Money, Banking & Monetary Policy (m-MCQ, m-stmt)
M(MB, "medium",
  "The Reserve Bank of India's Variable Rate Reverse Repo (VRRR) auctions are used to:",
  "भारतीय रिज़र्व बैंक की परिवर्ती दर रिवर्स रेपो (VRRR) नीलामियों का उपयोग किसके लिए किया जाता है?",
  ["inject long-term funds into banks at a fixed rate equal to the policy repo rate",
   "lend to banks against government securities when they face a sudden shortage of funds",
   "set the interest rates that banks must pay on their customers' savings deposits",
   "absorb surplus liquidity from banks at rates discovered through bidding"],
  ["बैंकों में नीतिगत रेपो दर के बराबर स्थिर दर पर दीर्घकालिक धन डालने के लिए",
   "धन की अचानक कमी होने पर सरकारी प्रतिभूतियों के बदले बैंकों को उधार देने के लिए",
   "बैंकों द्वारा अपने ग्राहकों की बचत जमाओं पर दी जाने वाली ब्याज दरें तय करने के लिए",
   "बोली से तय होने वाली दरों पर बैंकों से अधिशेष तरलता सोखने के लिए"],
  3,
  "In a VRRR auction the RBI invites banks to park surplus funds with it for a fixed period, and the rate is set by the bids, between the Standing Deposit Facility rate and the repo rate; it is one of the tools of the liquidity adjustment facility for draining excess liquidity that could otherwise push short-term market rates below the policy rate. "
  "Its mirror image, the Variable Rate Repo (VRR), injects liquidity when the system is short; lending to banks in an emergency is done through the Marginal Standing Facility, and banks have set their own savings-deposit rates since deregulation in 2011.",
  "VRRR नीलामी में RBI बैंकों को एक निश्चित अवधि के लिए अपने पास अधिशेष धन रखने को आमंत्रित करता है, और दर बोलियों से तय होती है, स्थायी जमा सुविधा की दर और रेपो दर के बीच; यह चलनिधि समायोजन सुविधा के उन साधनों में से है जिनसे अतिरिक्त तरलता निकाली जाती है, जो अन्यथा अल्पकालिक बाज़ार दरों को नीतिगत दर से नीचे धकेल सकती है। "
  "इसका दर्पण-रूप, परिवर्ती दर रेपो (VRR), तंत्र में कमी होने पर तरलता डालता है; आपात स्थिति में बैंकों को उधार सीमांत स्थायी सुविधा से दिया जाता है, और 2011 के विनियंत्रण के बाद से बैंक बचत-जमा दरें स्वयं तय करते हैं।",
  RBI + ": Revised Liquidity Management Framework; Monetary Policy Statements.",
  "l3-t4-eco-vrrr-liquidity-absorption", pos=3, craft="application")

S(MB, "medium", "With reference to the Reserve Bank of India's 2025 directions on loans against gold and silver, consider the following statements:",
  "सोने और चाँदी के बदले ऋणों पर भारतीय रिज़र्व बैंक के 2025 के निर्देशों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Banks and NBFCs may lend against silver jewellery and coins as well as gold.",
   "For small loans, of up to 2.5 lakh rupees, the loan may be as much as 85 per cent of the value of the pledged gold.",
   "Lenders may lend against primary gold, such as bullion bars."],
  ["बैंक और NBFC सोने के साथ-साथ चाँदी के आभूषणों और सिक्कों के बदले भी ऋण दे सकते हैं।",
   "2.5 लाख रुपये तक के छोटे ऋणों में ऋण गिरवी रखे सोने के मूल्य के 85 प्रतिशत तक हो सकता है।",
   "ऋणदाता प्राथमिक सोने, जैसे बुलियन छड़ों, के बदले ऋण दे सकते हैं।"],
  C3, 1,
  "Statements 1 and 2 are correct. The 2025 directions brought gold-loan rules for banks and NBFCs under one framework, allowed loans against silver ornaments and coins for the first time, and set a tiered loan-to-value limit -- up to 85 per cent for loans of 2.5 lakh rupees or less, falling for larger loans -- so that small borrowers can raise more against their jewellery while lenders keep a cushion against price falls. "
  "Statement 3 is wrong: lending against primary gold or silver, such as bars and bullion, is barred, because such loans could finance speculation in the metal; the directions also require standard purity assessment and the return of the pledged jewellery promptly on repayment.",
  "कथन 1 और 2 सही हैं। 2025 के निर्देशों ने बैंकों और NBFC के स्वर्ण-ऋण नियमों को एक ढाँचे में लाया, पहली बार चाँदी के आभूषणों और सिक्कों के बदले ऋण की अनुमति दी, और श्रेणीबद्ध ऋण-से-मूल्य सीमा तय की -- 2.5 लाख रुपये या उससे कम के ऋणों पर 85 प्रतिशत तक, बड़े ऋणों पर घटती हुई -- ताकि छोटे उधारकर्ता अपने आभूषणों के बदले अधिक धन जुटा सकें और ऋणदाताओं के पास कीमतें गिरने के विरुद्ध गद्दी बनी रहे। "
  "कथन 3 ग़लत है: छड़ों और बुलियन जैसे प्राथमिक सोने या चाँदी के बदले ऋण वर्जित है, क्योंकि ऐसे ऋण धातु में सट्टे को वित्त दे सकते हैं; निर्देश शुद्धता के मानक आकलन और ऋण चुकाने पर गिरवी आभूषणों की शीघ्र वापसी भी अनिवार्य करते हैं।",
  RBI + ": (Lending Against Gold and Silver Collateral) Directions, 2025.",
  "l3-t4-eco-gold-silver-loan-directions", craft="precision")

# ---------------------------------------------------------------- Budget, Deficits & Public Debt (m-stmt)
S("Budget, Deficits & Public Debt", "medium", "With reference to the management of the debt of State governments in India, consider the following statements:",
  "भारत में राज्य सरकारों के ऋण के प्रबंधन के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Many States maintain a Consolidated Sinking Fund to provide for the repayment of their market borrowings.",
   "A Guarantee Redemption Fund helps a State meet the guarantees invoked on loans it has guaranteed for its enterprises and agencies.",
   "Both these funds are administered by the Comptroller and Auditor General of India."],
  ["कई राज्य अपने बाज़ार उधारों की वापसी का प्रबंध करने के लिए समेकित निक्षेप निधि (कंसॉलिडेटेड सिंकिंग फ़ंड) रखते हैं।",
   "गारंटी मोचन निधि किसी राज्य को अपने उद्यमों और एजेंसियों के ऋणों पर दी गई गारंटियों के लागू होने पर उन्हें चुकाने में मदद करती है।",
   "ये दोनों निधियाँ भारत के नियंत्रक-महालेखापरीक्षक द्वारा प्रशासित होती हैं।"],
  C3, 1,
  "Statements 1 and 2 are correct. States set aside money every year in a Consolidated Sinking Fund, invested in government securities, so that a bunching of repayments does not force fresh borrowing at a bad time; the Guarantee Redemption Fund does the same for contingent liabilities -- the loans of State power utilities, irrigation corporations and other bodies that the State has guaranteed, which become the State's burden if the borrower defaults. "
  "Statement 3 is wrong: both funds are administered by the Reserve Bank of India, which acts as banker and debt manager to the States and invests the money; the CAG audits State accounts, including these funds, but does not run them. The RBI has urged States to build up both funds as their guarantees and debt have grown.",
  "कथन 1 और 2 सही हैं। राज्य हर वर्ष समेकित निक्षेप निधि में धन अलग रखते हैं, जो सरकारी प्रतिभूतियों में निवेशित होता है, ताकि भुगतानों के एक साथ आ पड़ने पर ग़लत समय पर नया उधार न लेना पड़े; गारंटी मोचन निधि आकस्मिक देनदारियों के लिए यही करती है -- राज्य की बिजली कंपनियों, सिंचाई निगमों और अन्य निकायों के वे ऋण जिनकी राज्य ने गारंटी दी है, जो उधारकर्ता के चूकने पर राज्य का बोझ बन जाते हैं। "
  "कथन 3 ग़लत है: दोनों निधियों का प्रशासन भारतीय रिज़र्व बैंक करता है, जो राज्यों के बैंकर और ऋण-प्रबंधक के रूप में धन का निवेश करता है; CAG इन निधियों सहित राज्यों के लेखों की लेखापरीक्षा करता है, पर इन्हें चलाता नहीं। राज्यों की गारंटियाँ और ऋण बढ़ने के साथ RBI ने उनसे दोनों निधियाँ बढ़ाने का आग्रह किया है।",
  RBI + ", State Finances: A Study of Budgets; Ministry of Finance.",
  "l3-t4-eco-state-csf-grf", craft="precision")

write("gs_l3_t4_e.sql")
