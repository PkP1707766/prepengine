# -*- coding: utf-8 -*-
"""Level 2 · Test 10 (Environment 2: Climate Change & Pollution) -- Climate Agreements &
Carbon Markets, 14 new bilingual rows against the live gap report: medium statement 5, easy
statement 2, hard statement 2, medium MCQ 2, hard MCQ 1, easy Statement-I/II 1, medium pairs 1.
Concepts already in the bank (CCTS, COP basics and outcomes, Global Stocktake, Green Credit
Programme, ISA, Kyoto targets, Loss and Damage Fund, NCQG, Panchamrit, Article 6, NDC design,
UNFCCC basics) are not repeated. India's 2031-35 NDC figures are taken from the NDC document
submitted to the UNFCCC in April 2026."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Environment & Ecology"
G = "Climate Agreements & Carbon Markets"
NDC35 = "Government of India, India's Nationally Determined Contribution (2031-2035), submitted to the UNFCCC, April 2026"

# ---------------------------------------------------------------- medium statements (5)
S(G, "medium", "Consider the following statements about India's Nationally Determined Contribution for 2031-2035:",
  "2031-2035 के लिए भारत के राष्ट्रीय स्तर पर निर्धारित योगदान (NDC) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It aims to reduce the emissions intensity of India's GDP by 47 per cent by 2035 from the 2005 level.",
   "It commits India to an absolute cap on its total greenhouse gas emissions from 2035.",
   "It aims for about 60 per cent of cumulative installed electric power capacity to come from non-fossil sources by 2035."],
  ["इसका लक्ष्य 2035 तक भारत के GDP की उत्सर्जन तीव्रता को 2005 के स्तर से 47 प्रतिशत घटाना है।",
   "यह भारत को 2035 से अपने कुल ग्रीनहाउस गैस उत्सर्जन पर एक निरपेक्ष सीमा (absolute cap) के लिए प्रतिबद्ध करता है।",
   "इसका लक्ष्य 2035 तक संचयी स्थापित विद्युत क्षमता का लगभग 60 प्रतिशत गैर-जीवाश्म स्रोतों से प्राप्त करना है।"],
  C3, 1,
  "Statements 1 and 3 are correct. The NDC submitted in April 2026 raises the intensity target from 45 per cent by 2030 to 47 per cent by 2035 (against 2005), sets about 60 per cent non-fossil installed capacity by 2035 -- 'with the help of transfer of technology and low-cost international finance' -- and aims for a carbon sink of 3.5 to 4.0 billion tonnes of CO2 equivalent through forest and tree cover by 2035. India had already crossed 50 per cent non-fossil capacity in 2025, five years ahead of its 2030 goal. "
  "Statement 2 is wrong: India's targets remain intensity-based, so total emissions can keep growing with the economy while each unit of GDP gets cleaner -- consistent with its position that a developing country's emissions will peak later, on the way to net zero by 2070.",
  "कथन 1 और 3 सही हैं। अप्रैल 2026 में प्रस्तुत NDC तीव्रता लक्ष्य को 2030 तक 45 प्रतिशत से बढ़ाकर 2035 तक 47 प्रतिशत (2005 की तुलना में) करता है, 2035 तक लगभग 60 प्रतिशत गैर-जीवाश्म स्थापित क्षमता तय करता है, 'प्रौद्योगिकी हस्तांतरण और कम लागत के अंतरराष्ट्रीय वित्त की सहायता से', और 2035 तक वन तथा वृक्ष आवरण से 3.5 से 4.0 अरब टन CO2 समतुल्य के कार्बन सिंक का लक्ष्य रखता है। भारत 2025 में ही 50 प्रतिशत गैर-जीवाश्म क्षमता पार कर चुका था, अपने 2030 के लक्ष्य से पाँच वर्ष पहले। "
  "कथन 2 गलत है: भारत के लक्ष्य तीव्रता-आधारित ही हैं, इसलिए GDP की हर इकाई के स्वच्छ होते जाने के साथ भी कुल उत्सर्जन अर्थव्यवस्था के साथ बढ़ सकता है; यह उसकी इस स्थिति के अनुरूप है कि विकासशील देश का उत्सर्जन देर से चरम पर पहुँचेगा, 2070 तक नेट ज़ीरो की राह पर।",
  f"{NDC35}; Ministry of New and Renewable Energy -- non-fossil share of installed capacity (July 2025).",
  "env-india-ndc-2035")

S(G, "medium", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Green Climate Fund was set up by the Parties to the UNFCCC at COP16 in Cancun in 2010.",
   "The headquarters of the Green Climate Fund are at Songdo, in the Republic of Korea.",
   "The Adaptation Fund was financed initially by a share of the proceeds from Clean Development Mechanism projects."],
  ["हरित जलवायु कोष (Green Climate Fund) की स्थापना UNFCCC के पक्षकारों ने 2010 में कैनकुन में COP16 में की थी।",
   "हरित जलवायु कोष का मुख्यालय कोरिया गणराज्य के सोंगडो में है।",
   "अनुकूलन कोष (Adaptation Fund) को प्रारंभ में स्वच्छ विकास तंत्र (CDM) परियोजनाओं की आय के एक हिस्से से वित्तपोषित किया गया था।"],
  C3, 2,
  "All three statements are correct. The Cancun Agreements (COP16, 2010) created the Green Climate Fund as an operating entity of the UNFCCC's financial mechanism; it is based in Songdo, Incheon, and funds both mitigation and adaptation in developing countries. "
  "The Adaptation Fund was set up under the Kyoto Protocol and drew its first money from a 2 per cent levy on the Certified Emission Reductions issued for CDM projects -- an early example of a market mechanism paying for adaptation. It now also serves the Paris Agreement.",
  "तीनों कथन सही हैं। कैनकुन समझौतों (COP16, 2010) ने हरित जलवायु कोष को UNFCCC के वित्तीय तंत्र की एक संचालन इकाई के रूप में बनाया; यह इंचियॉन के सोंगडो में स्थित है और विकासशील देशों में शमन तथा अनुकूलन, दोनों के लिए धन देता है। "
  "अनुकूलन कोष क्योटो प्रोटोकॉल के तहत बना और इसका पहला धन CDM परियोजनाओं के लिए जारी प्रमाणित उत्सर्जन कटौतियों (CERs) पर 2 प्रतिशत शुल्क से आया; यह बाज़ार-तंत्र द्वारा अनुकूलन के लिए भुगतान का एक शुरुआती उदाहरण है। अब यह पेरिस समझौते की भी सेवा करता है।",
  "UNFCCC -- Cancun Agreements, decision 1/CP.16 (2010); Green Climate Fund -- Governing Instrument; Adaptation Fund -- sources of funding.",
  "env-gcf-adaptation-fund")

S(G, "medium", "Consider the following statements about the Annexes of the UNFCCC:",
  "UNFCCC के अनुलग्नकों (Annexes) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["India is an Annex I Party to the UNFCCC.",
   "Annex II Parties are the developing countries that are entitled to receive climate finance.",
   "Every Annex I Party is also an Annex II Party."],
  ["भारत UNFCCC का अनुलग्नक I (Annex I) पक्षकार है।",
   "अनुलग्नक II के पक्षकार वे विकासशील देश हैं जो जलवायु वित्त पाने के अधिकारी हैं।",
   "अनुलग्नक I का हर पक्षकार अनुलग्नक II का भी पक्षकार है।"],
  C3, 3,
  "None of the statements is correct. Annex I lists the industrialised countries of 1992 together with the 'economies in transition' of the former Soviet bloc; India, like China and other developing countries, is a non-Annex I Party. "
  "Annex II is a subset of Annex I -- the OECD members of 1992 -- which are obliged to provide finance and technology to developing countries; it is the givers, not the receivers. The economies in transition, such as Russia and Ukraine, are in Annex I but not in Annex II, so not every Annex I Party is in Annex II. These lists put 'common but differentiated responsibilities' into practice.",
  "कोई भी कथन सही नहीं है। अनुलग्नक I में 1992 के औद्योगिक देश और पूर्व सोवियत गुट की 'संक्रमणशील अर्थव्यवस्थाएँ' हैं; भारत, चीन और दूसरे विकासशील देशों की तरह, गैर-अनुलग्नक I पक्षकार है। "
  "अनुलग्नक II, अनुलग्नक I का एक उपसमूह है, यानी 1992 के OECD सदस्य, जो विकासशील देशों को वित्त और प्रौद्योगिकी देने के लिए बाध्य हैं; ये देने वाले हैं, पाने वाले नहीं। रूस और यूक्रेन जैसी संक्रमणशील अर्थव्यवस्थाएँ अनुलग्नक I में हैं पर अनुलग्नक II में नहीं, इसलिए अनुलग्नक I का हर पक्षकार अनुलग्नक II में नहीं है। ये सूचियाँ 'साझा किंतु विभेदित उत्तरदायित्व' को व्यवहार में उतारती हैं।",
  "United Nations Framework Convention on Climate Change (1992), Articles 4.2 and 4.3 and Annexes I and II; UNFCCC -- Parties and observers.",
  "env-unfccc-annexes")

S(G, "medium", "Consider the following statements about the European Union's Carbon Border Adjustment Mechanism (CBAM):",
  "यूरोपीय संघ के कार्बन सीमा समायोजन तंत्र (CBAM) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It puts a price on the carbon emitted in producing certain goods imported into the EU, such as iron and steel, aluminium, cement and fertilisers.",
   "It applies to all goods imported into the European Union.",
   "Importers began paying for CBAM certificates in 2023, when the mechanism first came into force."],
  ["यह यूरोपीय संघ में आयात होने वाली कुछ वस्तुओं, जैसे लोहा और इस्पात, एल्युमिनियम, सीमेंट और उर्वरक, के उत्पादन में उत्सर्जित कार्बन पर कीमत लगाता है।",
   "यह यूरोपीय संघ में आयात होने वाली सभी वस्तुओं पर लागू होता है।",
   "आयातकों ने CBAM प्रमाणपत्रों के लिए भुगतान 2023 में शुरू कर दिया था, जब यह तंत्र पहली बार लागू हुआ।"],
  C3, 0,
  "Only statement 1 is correct. CBAM covers six sectors -- cement, iron and steel, aluminium, fertilisers, electricity and hydrogen -- chosen because they are carbon-intensive and at risk of 'carbon leakage'; the charge is meant to match what EU producers pay under the EU Emissions Trading System. Indian steel and aluminium exporters are among those most affected. "
  "Statement 2 is wrong: it applies only to goods in these sectors, and a de minimis rule exempts importers bringing in less than 50 tonnes a year. "
  "Statement 3 is wrong: from October 2023 to 2025 there was only a transitional phase of reporting embedded emissions, with no payment; the definitive phase began on 1 January 2026, and the sale of CBAM certificates starts in February 2027, for imports made from 2026.",
  "केवल कथन 1 सही है। CBAM छह क्षेत्रों पर लागू है: सीमेंट, लोहा और इस्पात, एल्युमिनियम, उर्वरक, बिजली और हाइड्रोजन; इन्हें इसलिए चुना गया कि ये कार्बन-गहन हैं और इनमें 'कार्बन रिसाव' का जोखिम है; शुल्क का उद्देश्य उस कीमत के बराबर होना है जो यूरोपीय संघ के उत्पादक EU उत्सर्जन व्यापार प्रणाली के तहत चुकाते हैं। भारत के इस्पात और एल्युमिनियम निर्यातक सबसे अधिक प्रभावितों में हैं। "
  "कथन 2 गलत है: यह केवल इन क्षेत्रों की वस्तुओं पर लागू होता है, और एक न्यूनतम-सीमा नियम वर्ष में 50 टन से कम आयात करने वालों को छूट देता है। "
  "कथन 3 गलत है: अक्टूबर 2023 से 2025 तक केवल एक संक्रमणकालीन चरण था, जिसमें अंतर्निहित उत्सर्जन की रिपोर्टिंग होती थी, कोई भुगतान नहीं; निश्चित चरण 1 जनवरी 2026 से शुरू हुआ, और CBAM प्रमाणपत्रों की बिक्री फ़रवरी 2027 से शुरू होती है, 2026 से किए गए आयात के लिए।",
  "Regulation (EU) 2023/956 establishing a carbon border adjustment mechanism, as amended in 2025; European Commission, Taxation and Customs Union -- CBAM definitive regime.",
  "env-eu-cbam")

S(G, "medium", "Consider the following statements about Just Energy Transition Partnerships (JETPs):",
  "न्यायसंगत ऊर्जा संक्रमण साझेदारियों (JETPs) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["South Africa was the first country to agree a JETP, announced at COP26 in 2021.",
   "Indonesia and Vietnam have also agreed JETPs.",
   "India has signed a JETP with the G7 countries."],
  ["दक्षिण अफ़्रीका JETP पर सहमत होने वाला पहला देश था, जिसकी घोषणा 2021 में COP26 में हुई।",
   "इंडोनेशिया और वियतनाम ने भी JETPs पर सहमति दी है।",
   "भारत ने G7 देशों के साथ एक JETP पर हस्ताक्षर किए हैं।"],
  C3, 1,
  "Statements 1 and 2 are correct. A JETP is a financing deal in which a group of developed countries and lenders commit money to help a coal-dependent developing country retire coal plants early and expand clean power while protecting affected workers and communities. South Africa's came first (COP26, 2021), followed by Indonesia and Vietnam (2022) and Senegal (2023). "
  "Statement 3 is wrong: India has not signed a JETP. It has preferred to set its own transition pace through its NDC, arguing that coal remains necessary for its energy security while demand grows.",
  "कथन 1 और 2 सही हैं। JETP एक वित्तपोषण समझौता है, जिसमें विकसित देशों और ऋणदाताओं का एक समूह कोयले पर निर्भर किसी विकासशील देश को कोयला संयंत्र जल्दी बंद करने और स्वच्छ बिजली बढ़ाने के लिए, प्रभावित श्रमिकों और समुदायों की रक्षा करते हुए, धन देने का वादा करता है। पहला दक्षिण अफ़्रीका का था (COP26, 2021), फिर इंडोनेशिया और वियतनाम (2022) और सेनेगल (2023)। "
  "कथन 3 गलत है: भारत ने कोई JETP नहीं किया है। उसने अपने NDC के ज़रिए संक्रमण की अपनी गति तय करना पसंद किया है, यह तर्क देते हुए कि माँग बढ़ने के दौर में ऊर्जा सुरक्षा के लिए कोयला अभी ज़रूरी है।",
  "UK Government / European Commission -- Political Declaration on the Just Energy Transition in South Africa (COP26, 2021); JETP statements for Indonesia (G20 Bali, 2022), Viet Nam (2022) and Senegal (2023).",
  "env-jetp")

# ---------------------------------------------------------------- easy statements (2)
S(G, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The secretariat of the UNFCCC is located in Bonn, Germany.",
   "India hosted COP8 of the UNFCCC in New Delhi in 2002."],
  ["UNFCCC का सचिवालय जर्मनी के बॉन में स्थित है।",
   "भारत ने 2002 में नई दिल्ली में UNFCCC के COP8 की मेज़बानी की थी।"],
  T2, 2,
  "Both statements are correct. The UNFCCC secretariat (UN Climate Change) has been in Bonn since 1996. COP8 in New Delhi (2002) adopted the Delhi Ministerial Declaration, which stressed that adaptation and sustainable development had to be at the centre of climate action for developing countries -- an early statement of the priorities India still argues for.",
  "दोनों कथन सही हैं। UNFCCC सचिवालय (UN Climate Change) 1996 से बॉन में है। नई दिल्ली में हुए COP8 (2002) ने दिल्ली मंत्रिस्तरीय घोषणा अपनाई, जिसने ज़ोर दिया कि विकासशील देशों के लिए जलवायु कार्रवाई के केंद्र में अनुकूलन और सतत विकास होने चाहिए; यह उन प्राथमिकताओं का शुरुआती वक्तव्य था जिनके लिए भारत आज भी तर्क देता है।",
  "UNFCCC -- secretariat; Delhi Ministerial Declaration on Climate Change and Sustainable Development, decision 1/CP.8 (2002).",
  "env-unfccc-bonn-cop8-delhi")

S(G, "easy", "Consider the following statements about the Paris Agreement:",
  "पेरिस समझौते के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It aims to hold the rise in global average temperature to well below 2 degrees Celsius above pre-industrial levels and to pursue efforts to limit it to 1.5 degrees.",
   "It entered into force in December 2015, at COP21 itself.",
   "The United States has never withdrawn from it."],
  ["इसका लक्ष्य वैश्विक औसत तापमान में वृद्धि को पूर्व-औद्योगिक स्तर से 2 डिग्री सेल्सियस से काफ़ी नीचे रखना और इसे 1.5 डिग्री तक सीमित करने के प्रयास करना है।",
   "यह दिसंबर 2015 में, COP21 में ही, लागू हो गया।",
   "संयुक्त राज्य अमेरिका कभी इससे अलग नहीं हुआ है।"],
  C3, 0,
  "Only statement 1 is correct. Statement 2 confuses adoption with entry into force: adopted at COP21 in December 2015, the Agreement entered into force only on 4 November 2016, once at least 55 Parties accounting for at least 55 per cent of global emissions had ratified it; India ratified on 2 October 2016. "
  "Statement 3 is wrong: the United States withdrew in November 2020, rejoined in February 2021 and gave notice of withdrawal again in January 2025, which took effect a year later.",
  "केवल कथन 1 सही है। कथन 2 अपनाए जाने और लागू होने को गड्डमड्ड करता है: दिसंबर 2015 में COP21 में अपनाया गया यह समझौता 4 नवंबर 2016 को ही लागू हुआ, जब वैश्विक उत्सर्जन के कम से कम 55 प्रतिशत के लिए ज़िम्मेदार कम से कम 55 पक्षकारों ने इसका अनुसमर्थन कर दिया; भारत ने 2 अक्टूबर 2016 को अनुसमर्थन किया। "
  "कथन 3 गलत है: संयुक्त राज्य अमेरिका नवंबर 2020 में अलग हुआ, फ़रवरी 2021 में फिर शामिल हुआ, और जनवरी 2025 में फिर अलग होने की सूचना दी, जो एक वर्ष बाद प्रभावी हुई।",
  "Paris Agreement (2015), Articles 2 and 21; UN Treaty Collection -- status of the Paris Agreement.",
  "env-paris-agreement-basics")

# ---------------------------------------------------------------- hard statements (2)
S(G, "hard", "Consider the following statements about the market mechanisms of the Kyoto Protocol:",
  "क्योटो प्रोटोकॉल के बाज़ार तंत्रों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Under the Clean Development Mechanism, emission-reduction projects in developing countries could earn tradable credits.",
   "The credits issued under the Clean Development Mechanism are called Emission Reduction Units.",
   "Joint Implementation involved emission-reduction projects carried out jointly by two developing countries.",
   "International emissions trading allowed countries with Kyoto targets to buy and sell parts of their allowed emissions."],
  ["स्वच्छ विकास तंत्र (CDM) के तहत विकासशील देशों की उत्सर्जन-कटौती परियोजनाएँ व्यापार योग्य क्रेडिट अर्जित कर सकती थीं।",
   "स्वच्छ विकास तंत्र के तहत जारी क्रेडिट को उत्सर्जन कटौती इकाइयाँ (Emission Reduction Units) कहा जाता है।",
   "संयुक्त कार्यान्वयन (Joint Implementation) में दो विकासशील देशों द्वारा मिलकर की जाने वाली उत्सर्जन-कटौती परियोजनाएँ शामिल थीं।",
   "अंतरराष्ट्रीय उत्सर्जन व्यापार ने क्योटो लक्ष्यों वाले देशों को अपने अनुमत उत्सर्जन के हिस्से खरीदने और बेचने की अनुमति दी।"],
  C4, 1,
  "Statements 1 and 4 are correct. Under the CDM, a project in a non-Annex I country -- a wind farm in Gujarat, say -- earned Certified Emission Reductions (CERs), each worth one tonne of CO2 equivalent, which industrialised countries could count against their targets; India and China hosted the largest numbers of CDM projects. Statement 2 swaps the names: Emission Reduction Units (ERUs) were the credits of Joint Implementation. "
  "Statement 3 is wrong: Joint Implementation was between two countries that both had Kyoto targets (Annex B), typically an investor from Western Europe and a host in Eastern Europe, and it generated Emission Reduction Units. Emissions trading let a country that cut more than its target sell the surplus of its 'assigned amount' to one that fell short. Under the Paris Agreement, the Article 6.4 mechanism is the CDM's successor.",
  "कथन 1 और 4 सही हैं। CDM के तहत किसी गैर-अनुलग्नक I देश की परियोजना, जैसे गुजरात का कोई पवन फ़ार्म, प्रमाणित उत्सर्जन कटौतियाँ (CERs) अर्जित करती थी, जिनमें हर एक एक टन CO2 समतुल्य के बराबर थी, और औद्योगिक देश इन्हें अपने लक्ष्यों में गिन सकते थे; सबसे अधिक CDM परियोजनाएँ भारत और चीन में थीं। कथन 2 नामों की अदला-बदली करता है: उत्सर्जन कटौती इकाइयाँ (ERUs) संयुक्त कार्यान्वयन के क्रेडिट थे। "
  "कथन 3 गलत है: संयुक्त कार्यान्वयन ऐसे दो देशों के बीच था जिन दोनों के क्योटो लक्ष्य थे (अनुलग्नक B), आम तौर पर पश्चिमी यूरोप का निवेशक और पूर्वी यूरोप का मेज़बान, और इससे उत्सर्जन कटौती इकाइयाँ (ERUs) बनती थीं। उत्सर्जन व्यापार ने अपने लक्ष्य से अधिक कटौती करने वाले देश को अपनी 'निर्धारित मात्रा' (assigned amount) का अधिशेष पीछे रह गए देश को बेचने दिया। पेरिस समझौते के तहत अनुच्छेद 6.4 का तंत्र CDM का उत्तराधिकारी है।",
  "Kyoto Protocol (1997), Articles 6, 12 and 17; UNFCCC -- CDM project registry.",
  "env-kyoto-cdm-ji")

S(G, "hard", "Consider the following statements about pricing carbon:",
  "कार्बन के मूल्य-निर्धारण के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["A carbon tax fixes the price of emissions and lets the quantity of emissions adjust.",
   "A cap-and-trade system fixes the quantity of emissions allowed and lets the price adjust.",
   "The EU Emissions Trading System, launched in 2005, is a cap-and-trade system."],
  ["कार्बन कर (carbon tax) उत्सर्जन की कीमत तय करता है और उत्सर्जन की मात्रा को स्वयं समायोजित होने देता है।",
   "कैप-एंड-ट्रेड प्रणाली अनुमत उत्सर्जन की मात्रा तय करती है और कीमत को स्वयं समायोजित होने देती है।",
   "2005 में शुरू हुई EU उत्सर्जन व्यापार प्रणाली एक कैप-एंड-ट्रेड प्रणाली है।"],
  C3, 2,
  "All three statements are correct. The two instruments are mirror images: a tax gives certainty about the cost but not about how much emissions will fall, while a cap gives certainty about the quantity but lets the market set the price of allowances. "
  "The EU ETS, the world's first major carbon market, caps the emissions of power plants, industry and aviation, and lowers the cap every year; firms that cut emissions can sell their spare allowances. India's Carbon Credit Trading Scheme differs in that it sets emission-intensity targets for each covered unit rather than an absolute cap.",
  "तीनों कथन सही हैं। दोनों साधन एक-दूसरे के दर्पण-प्रतिबिंब हैं: कर लागत के बारे में निश्चितता देता है, पर इस बारे में नहीं कि उत्सर्जन कितना घटेगा, जबकि सीमा (cap) मात्रा के बारे में निश्चितता देती है पर भत्तों (allowances) की कीमत बाज़ार पर छोड़ देती है। "
  "विश्व का पहला बड़ा कार्बन बाज़ार EU ETS बिजली संयंत्रों, उद्योग और विमानन के उत्सर्जन पर सीमा लगाता है और हर वर्ष उसे घटाता है; जो कंपनियाँ उत्सर्जन घटाती हैं वे अपने बचे भत्ते बेच सकती हैं। भारत की कार्बन क्रेडिट ट्रेडिंग योजना इस अर्थ में अलग है कि वह निरपेक्ष सीमा के बजाय हर शामिल इकाई के लिए उत्सर्जन-तीव्रता लक्ष्य तय करती है।",
  "European Commission -- EU Emissions Trading System (Directive 2003/87/EC); World Bank -- State and Trends of Carbon Pricing; Bureau of Energy Efficiency -- Carbon Credit Trading Scheme, 2023.",
  "env-carbon-tax-vs-cap-and-trade")

# ---------------------------------------------------------------- MCQs (3)
M(G, "medium", "'Biennial Transparency Reports', in which countries report their emissions and their progress towards their climate targets, are submitted under:",
  "'द्विवार्षिक पारदर्शिता रिपोर्ट' (Biennial Transparency Reports), जिनमें देश अपने उत्सर्जन और अपने जलवायु लक्ष्यों की दिशा में प्रगति की रिपोर्ट देते हैं, किसके तहत प्रस्तुत की जाती हैं?",
  ["The Paris Agreement", "The Kyoto Protocol", "The Montreal Protocol", "The Convention on Biological Diversity"],
  ["पेरिस समझौता", "क्योटो प्रोटोकॉल", "मॉन्ट्रियल प्रोटोकॉल", "जैव विविधता पर अभिसमय"],
  0,
  "Biennial Transparency Reports are the core of the Paris Agreement's Enhanced Transparency Framework (Article 13), which applies common rules to all Parties, with flexibility for developing countries that need it; the first reports were due by the end of 2024. "
  "Their predecessors under the UNFCCC were the Biennial Reports of developed countries and the Biennial Update Reports of developing countries such as India. The Montreal Protocol and the CBD have their own, separate reporting systems.",
  "द्विवार्षिक पारदर्शिता रिपोर्ट पेरिस समझौते के संवर्धित पारदर्शिता ढाँचे (अनुच्छेद 13) का मूल हैं, जो सभी पक्षकारों पर साझा नियम लागू करता है, और जिन विकासशील देशों को ज़रूरत हो उन्हें लचीलापन देता है; पहली रिपोर्टें 2024 के अंत तक देनी थीं। "
  "UNFCCC के तहत इनकी पूर्ववर्ती विकसित देशों की द्विवार्षिक रिपोर्ट और भारत जैसे विकासशील देशों की द्विवार्षिक अद्यतन रिपोर्ट (BURs) थीं। मॉन्ट्रियल प्रोटोकॉल और CBD की अपनी अलग रिपोर्टिंग प्रणालियाँ हैं।",
  "Paris Agreement, Article 13; UNFCCC decision 18/CMA.1 (modalities, procedures and guidelines for the Enhanced Transparency Framework).",
  "env-btr-enhanced-transparency")

M(G, "medium", "Which one of the following is NOT among the greenhouse gases covered by the Kyoto Protocol?",
  "निम्नलिखित में से कौन-सी क्योटो प्रोटोकॉल के अंतर्गत आने वाली ग्रीनहाउस गैसों में नहीं है?",
  ["Chlorofluorocarbons", "Sulphur hexafluoride", "Perfluorocarbons", "Nitrous oxide"],
  ["क्लोरोफ़्लोरोकार्बन (CFC)", "सल्फ़र हेक्साफ़्लोराइड", "परफ़्लोरोकार्बन", "नाइट्रस ऑक्साइड"],
  0,
  "The Kyoto 'basket' covers carbon dioxide, methane, nitrous oxide, hydrofluorocarbons, perfluorocarbons and sulphur hexafluoride, with nitrogen trifluoride added for the second commitment period. "
  "CFCs are powerful greenhouse gases too, but they were left out deliberately because they were already being phased out under the Montreal Protocol, which deals with ozone-depleting substances -- the trap is to assume that every greenhouse gas must be in the climate treaty.",
  "क्योटो 'बास्केट' में कार्बन डाइऑक्साइड, मीथेन, नाइट्रस ऑक्साइड, हाइड्रोफ़्लोरोकार्बन, परफ़्लोरोकार्बन और सल्फ़र हेक्साफ़्लोराइड हैं, और दूसरी प्रतिबद्धता अवधि के लिए नाइट्रोजन ट्राइफ़्लोराइड जोड़ी गई। "
  "CFC भी शक्तिशाली ग्रीनहाउस गैसें हैं, पर इन्हें जान-बूझकर बाहर रखा गया, क्योंकि ओज़ोन-क्षयकारी पदार्थों से संबंधित मॉन्ट्रियल प्रोटोकॉल के तहत इन्हें पहले से ही समाप्त किया जा रहा था; जाल यह मान लेना है कि हर ग्रीनहाउस गैस जलवायु संधि में होनी ही चाहिए।",
  "Kyoto Protocol (1997), Annex A; Doha Amendment (2012) -- nitrogen trifluoride.",
  "env-kyoto-basket-cfc")

M(G, "hard", "The 'Warsaw International Mechanism', set up at COP19 in 2013, deals with:",
  "2013 में COP19 में स्थापित 'वॉरसॉ अंतरराष्ट्रीय तंत्र' (Warsaw International Mechanism) किससे संबंधित है?",
  ["Loss and damage from climate change impacts", "Reducing emissions from deforestation (REDD+)", "Transfer of climate technology", "Finance for adaptation projects"],
  ["जलवायु परिवर्तन के प्रभावों से होने वाली हानि और क्षति", "वनोन्मूलन से होने वाले उत्सर्जन में कमी (REDD+)", "जलवायु प्रौद्योगिकी का हस्तांतरण", "अनुकूलन परियोजनाओं के लिए वित्त"],
  0,
  "The Warsaw International Mechanism for Loss and Damage (2013) was the UNFCCC's first formal arrangement for loss and damage -- harm that goes beyond what adaptation can prevent, such as land lost to the sea; the Santiago Network, set up later, gives technical help under it, and the separate Fund for responding to Loss and Damage was agreed in 2022. "
  "The strongest distractor is REDD+, because the same COP19 in Warsaw also adopted the 'Warsaw Framework for REDD+' -- two different Warsaw outcomes that are easy to confuse.",
  "हानि और क्षति के लिए वॉरसॉ अंतरराष्ट्रीय तंत्र (2013) हानि और क्षति के लिए UNFCCC की पहली औपचारिक व्यवस्था थी, यानी वह नुकसान जो अनुकूलन से नहीं रोका जा सकता, जैसे समुद्र में समा गई भूमि; बाद में बना सैंटियागो नेटवर्क इसके तहत तकनीकी सहायता देता है, और हानि और क्षति से निपटने के लिए अलग कोष पर 2022 में सहमति बनी। "
  "सबसे मज़बूत गलत विकल्प REDD+ है, क्योंकि वॉरसॉ के उसी COP19 ने 'REDD+ के लिए वॉरसॉ ढाँचा' भी अपनाया था; वॉरसॉ के ये दो अलग परिणाम आसानी से गड्डमड्ड हो जाते हैं।",
  "UNFCCC decision 2/CP.19 (Warsaw International Mechanism for Loss and Damage); decisions 9/CP.19 to 15/CP.19 (Warsaw Framework for REDD+).",
  "env-warsaw-international-mechanism")

# ---------------------------------------------------------------- Statement-I/II (easy)
A(G, "easy",
  "Small island developing States have been among the strongest supporters of the 1.5 degrees Celsius limit.",
  "छोटे द्वीपीय विकासशील देश 1.5 डिग्री सेल्सियस की सीमा के सबसे प्रबल समर्थकों में रहे हैं।",
  "Sea-level rise threatens the very existence of low-lying island nations.",
  "समुद्र-स्तर में वृद्धि निचले द्वीपीय देशों के अस्तित्व के लिए ही खतरा है।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I. For countries such as Tuvalu, Kiribati and the Maldives, much of whose land lies only a metre or two above the sea, the difference between 1.5 and 2 degrees of warming is a difference in how much of the country survives; their campaign of '1.5 to stay alive' helped get the 1.5-degree aim written into the Paris Agreement.",
  "दोनों कथन सही हैं, और कथन-II कथन-I की व्याख्या करता है। तुवालु, किरिबाती और मालदीव जैसे देशों के लिए, जिनकी अधिकांश भूमि समुद्र से केवल एक-दो मीटर ऊपर है, 1.5 और 2 डिग्री तापन का अंतर इस बात का अंतर है कि देश का कितना भाग बचेगा; उनके '1.5 to stay alive' अभियान ने 1.5 डिग्री के लक्ष्य को पेरिस समझौते में लिखवाने में मदद की।",
  "Paris Agreement, Article 2.1(a); Alliance of Small Island States (AOSIS); IPCC Special Report on Global Warming of 1.5 degrees C (2018).",
  "env-sids-one-point-five")

# ---------------------------------------------------------------- pairs (1, medium)
P(G, "medium", "Consider the following pairs of international initiatives and where they were launched:",
  "अंतरराष्ट्रीय पहलों और उनके शुरू होने के स्थान के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Coalition for Disaster Resilient Infrastructure : UN Climate Action Summit, New York, 2019",
   "Leadership Group for Industry Transition (LeadIT) : UN Climate Action Summit, New York, 2019",
   "Global Biofuels Alliance : G20 Summit, New Delhi, 2023",
   "Global Methane Pledge : COP21, Paris, 2015"],
  ["आपदा रोधी अवसंरचना गठबंधन (CDRI) : संयुक्त राष्ट्र जलवायु कार्रवाई शिखर सम्मेलन, न्यूयॉर्क, 2019",
   "उद्योग संक्रमण के लिए नेतृत्व समूह (LeadIT) : संयुक्त राष्ट्र जलवायु कार्रवाई शिखर सम्मेलन, न्यूयॉर्क, 2019",
   "वैश्विक जैव ईंधन गठबंधन : G20 शिखर सम्मेलन, नई दिल्ली, 2023",
   "वैश्विक मीथेन संकल्प : COP21, पेरिस, 2015"],
  2,
  "Three pairs are correct. India launched the CDRI, and India and Sweden launched LeadIT (for decarbonising heavy industry), at the UN Secretary-General's Climate Action Summit in New York in September 2019; the Global Biofuels Alliance was launched under India's G20 presidency in New Delhi in September 2023. "
  "Pair 4 is wrong: the Global Methane Pledge, to cut methane emissions by at least 30 per cent from 2020 levels by 2030, was launched by the United States and the European Union at COP26 in Glasgow in 2021. India has not joined it, citing the weight of agriculture and livestock in its methane emissions.",
  "तीन युग्म सही हैं। सितंबर 2019 में न्यूयॉर्क में संयुक्त राष्ट्र महासचिव के जलवायु कार्रवाई शिखर सम्मेलन में भारत ने CDRI, और भारत तथा स्वीडन ने LeadIT (भारी उद्योग के डीकार्बनीकरण के लिए) शुरू किया; वैश्विक जैव ईंधन गठबंधन सितंबर 2023 में नई दिल्ली में भारत की G20 अध्यक्षता के दौरान शुरू हुआ। "
  "युग्म 4 गलत है: 2030 तक मीथेन उत्सर्जन को 2020 के स्तर से कम से कम 30 प्रतिशत घटाने का वैश्विक मीथेन संकल्प संयुक्त राज्य अमेरिका और यूरोपीय संघ ने 2021 में ग्लासगो में COP26 में शुरू किया था। भारत इसमें शामिल नहीं हुआ है, और इसका कारण अपने मीथेन उत्सर्जन में कृषि और पशुधन का बड़ा हिस्सा बताता है।",
  "Ministry of External Affairs -- CDRI and LeadIT (UN Climate Action Summit, September 2019); Ministry of Petroleum and Natural Gas -- Global Biofuels Alliance (2023); Global Methane Pledge (COP26, 2021).",
  "env-climate-initiatives-pairs")

if __name__ == "__main__":
    write("env_l2_t10_agreements.sql")
