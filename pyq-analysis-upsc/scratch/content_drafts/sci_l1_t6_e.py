# -*- coding: utf-8 -*-
"""Level 1 · Test 6 (Science & Technology, NCERT Foundation) -- part E: Defence, Aerospace & Security Technology (10)
(upsc_l1_cell_targets.mjs 6): easy MCQ 1, easy statement 2, medium MCQ 1, medium statement 4, medium
Statement-I/II 1, hard statement 1.
NCERT has little on defence, so the angle is the foundation layer from official sources -- the Ministry of Defence,
DRDO and the services -- plus the physics of thermal imaging: the guided-missile programme, the nuclear triad, the
tri-service agencies, Agnipath, the acquisition procedure, defence corridors, exercises and warship building.
Level-2 S&T facts are not repeated (BrahMos, Prithvi and Agni Prime, cruise versus ballistic, Akash and S-400, Tejas,
Rafale and the Kaveri engine, AMCA, Vikrant as the first indigenous carrier, Arihant, no first use, iDEX and the
positive indigenisation lists, drones, hypersonics, MIRV, Mission Shakti, Kavach). MCQ keys are pinned (pos)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Science & Technology"
d.REQUIRE_CRAFT = True
DF = "Defence, Aerospace & Security Technology"
MOD = "Ministry of Defence"
DRDO = "Defence Research and Development Organisation"

# ---------------------------------------------------------------- easy MCQ (1)
M(DF, "easy", "The Integrated Guided Missile Development Programme, launched in 1983, was led by",
  "1983 में आरंभ एकीकृत निर्देशित प्रक्षेपास्त्र विकास कार्यक्रम (IGMDP) का नेतृत्व किसने किया?",
  ["A.P.J. Abdul Kalam", "Homi Jehangir Bhabha", "Vikram Sarabhai", "Satish Dhawan"],
  ["ए.पी.जे. अब्दुल कलाम", "होमी जहाँगीर भाभा", "विक्रम साराभाई", "सतीश धवन"],
  0,
  "Dr A.P.J. Abdul Kalam, who had led the SLV-3 project that put Rohini into orbit in 1980, moved to DRDO to head the programme, which produced Prithvi, Agni, Akash, Trishul and Nag and earned him the title 'Missile Man of India'; he later served as President of India (2002-07). "
  "Homi Bhabha founded India's nuclear programme, and Vikram Sarabhai and Satish Dhawan led its space programme.",
  "डॉ. ए.पी.जे. अब्दुल कलाम, जिन्होंने 1980 में रोहिणी को कक्षा में पहुँचाने वाली SLV-3 परियोजना का नेतृत्व किया था, कार्यक्रम के प्रमुख बनकर DRDO आए, जिससे पृथ्वी, अग्नि, आकाश, त्रिशूल और नाग बने और उन्हें 'भारत के मिसाइल मैन' की उपाधि मिली; बाद में वे भारत के राष्ट्रपति (2002-07) रहे। "
  "होमी भाभा ने भारत के नाभिकीय कार्यक्रम की नींव रखी, और विक्रम साराभाई तथा सतीश धवन ने अंतरिक्ष कार्यक्रम का नेतृत्व किया।",
  f"{DRDO} (history of the IGMDP).",
  "l1-sci-igmdp-kalam", pos=0, craft="recall")

# ---------------------------------------------------------------- easy statement (2)
S(DF, "easy", "Consider the following statements about missiles developed under India's guided missile programme:",
  "भारत के निर्देशित प्रक्षेपास्त्र कार्यक्रम के अंतर्गत विकसित प्रक्षेपास्त्रों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Nag is an anti-tank guided missile.",
   "Trishul was a short-range surface-to-air missile."],
  ["नाग एक टैंक-रोधी निर्देशित प्रक्षेपास्त्र है।",
   "त्रिशूल एक कम दूरी का सतह-से-हवा प्रक्षेपास्त्र था।"],
  T2, 2,
  "Both statements are correct. Nag is a 'fire-and-forget' anti-tank missile that guides itself to the target after launch, and its versions are fired from vehicles and helicopters. "
  "Trishul ran into technical problems and was closed in 2008, but the experience gained fed into later air-defence missiles; the programme as a whole built the design and testing base on which India's missile industry stands.",
  "दोनों कथन सही हैं। नाग 'दागो और भूल जाओ' टैंक-रोधी प्रक्षेपास्त्र है जो छोड़े जाने के बाद स्वयं लक्ष्य तक पहुँचता है, और इसके संस्करण वाहनों और हेलिकॉप्टरों से दागे जाते हैं। "
  "त्रिशूल तकनीकी समस्याओं में फँसा और 2008 में बंद कर दिया गया, पर उससे मिला अनुभव बाद के वायु-रक्षा प्रक्षेपास्त्रों में काम आया; पूरे कार्यक्रम ने वह डिज़ाइन और परीक्षण आधार बनाया जिस पर भारत का प्रक्षेपास्त्र उद्योग खड़ा है।",
  f"{DRDO}.",
  "l1-sci-nag-trishul", craft="recall")

S(DF, "easy", "Consider the following statements about military exercises:",
  "सैन्य अभ्यासों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Malabar is a naval exercise involving India, the USA, Japan and Australia.",
   "Garuda is a naval exercise between India and Russia."],
  ["मालाबार भारत, अमेरिका, जापान और ऑस्ट्रेलिया का नौसैनिक अभ्यास है।",
   "गरुड़ भारत और रूस के बीच का नौसैनिक अभ्यास है।"],
  T2, 0,
  "Only statement 1 is correct: Malabar began in 1992 as an India-US exercise; Japan became a regular participant in 2015 and Australia rejoined in 2020, so that all four Quad countries now take part. "
  "Statement 2 is wrong: Garuda is an air exercise between the Indian Air Force and the French Air and Space Force; India's exercise with Russia across services is called INDRA.",
  "केवल कथन 1 सही है: मालाबार 1992 में भारत-अमेरिका अभ्यास के रूप में आरंभ हुआ; जापान 2015 में नियमित प्रतिभागी बना और ऑस्ट्रेलिया 2020 में फिर जुड़ा, जिससे अब क्वाड के चारों देश भाग लेते हैं। "
  "कथन 2 गलत है: गरुड़ भारतीय वायु सेना और फ़्रांसीसी वायु एवं अंतरिक्ष सेना के बीच का वायु अभ्यास है; रूस के साथ भारत का बहु-सेवा अभ्यास इंद्र (INDRA) कहलाता है।",
  f"{MOD} (Annual Report; exercises with friendly foreign countries).",
  "l1-sci-malabar-garuda-exercises", craft="precision")

# ---------------------------------------------------------------- medium MCQ (1)
M(DF, "medium", "The two Defence Industrial Corridors announced in 2018 to build a defence manufacturing base are in",
  "रक्षा विनिर्माण आधार बनाने के लिए 2018 में घोषित दो रक्षा औद्योगिक गलियारे कहाँ हैं?",
  ["Uttar Pradesh and Tamil Nadu", "Gujarat and Maharashtra", "Karnataka and Telangana", "Madhya Pradesh and Maharashtra"],
  ["उत्तर प्रदेश और तमिलनाडु", "गुजरात और महाराष्ट्र", "कर्नाटक और तेलंगाना", "मध्य प्रदेश और महाराष्ट्र"],
  0,
  "The Uttar Pradesh corridor has nodes at Agra, Aligarh, Chitrakoot, Jhansi, Kanpur and Lucknow, and the Tamil Nadu corridor at Chennai, Coimbatore, Hosur, Salem and Tiruchirappalli. "
  "The corridors aim to cluster public and private defence firms, their small suppliers and testing facilities, cutting import dependence and building exports.",
  "उत्तर प्रदेश गलियारे के केंद्र आगरा, अलीगढ़, चित्रकूट, झाँसी, कानपुर और लखनऊ में हैं, और तमिलनाडु गलियारे के चेन्नई, कोयंबटूर, होसुर, सेलम और तिरुचिरापल्ली में। "
  "गलियारों का उद्देश्य सार्वजनिक और निजी रक्षा फ़र्मों, उनके छोटे आपूर्तिकर्ताओं और परीक्षण सुविधाओं को एक साथ लाकर आयात निर्भरता घटाना और निर्यात बढ़ाना है।",
  f"{MOD} (Department of Defence Production).",
  "l1-sci-defence-industrial-corridors", pos=3, craft="recall")

# ---------------------------------------------------------------- medium statement (4)
S(DF, "medium", "Consider the following statements about India's nuclear triad:",
  "भारत के नाभिकीय त्रिक (nuclear triad) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The triad means the ability to deliver nuclear weapons from land-based missiles, from aircraft and from submarines.",
   "The K-15 and K-4 are submarine-launched ballistic missiles.",
   "The Agni series are cruise missiles."],
  ["त्रिक का अर्थ है स्थल-आधारित प्रक्षेपास्त्रों, विमानों और पनडुब्बियों से नाभिकीय हथियार दागने की क्षमता।",
   "K-15 और K-4 पनडुब्बी से छोड़े जाने वाले बैलिस्टिक प्रक्षेपास्त्र हैं।",
   "अग्नि शृंखला के प्रक्षेपास्त्र क्रूज़ प्रक्षेपास्त्र हैं।"],
  C3, 1,
  "Statements 1 and 2 are correct: the triad was completed in 2018, when INS Arihant finished its first deterrence patrol; a submarine hidden at sea is the hardest leg for an enemy to destroy, which makes retaliation credible under a no-first-use doctrine. "
  "Statement 3 is wrong: the Agni missiles are ballistic missiles, which follow a high arc after their rockets burn out, and form the land leg of the triad.",
  "कथन 1 और 2 सही हैं: त्रिक 2018 में पूरा हुआ, जब INS अरिहंत ने अपना पहला निवारक गश्त पूरा किया; समुद्र में छिपी पनडुब्बी शत्रु के लिए नष्ट करने में सबसे कठिन अंग है, जो 'पहले प्रयोग नहीं' के सिद्धांत के अंतर्गत जवाबी कार्रवाई को विश्वसनीय बनाती है। "
  "कथन 3 गलत है: अग्नि प्रक्षेपास्त्र बैलिस्टिक प्रक्षेपास्त्र हैं, जो रॉकेट जल जाने के बाद ऊँचे चाप में चलते हैं, और त्रिक का स्थल अंग हैं।",
  f"{MOD}; {DRDO}.",
  "l1-sci-nuclear-triad-k4-agni", craft="linkage")

S(DF, "medium", "Consider the following tri-service agencies set up in 2019:",
  "2019 में स्थापित निम्नलिखित त्रि-सेवा एजेंसियों पर विचार कीजिए:",
  ["The Defence Space Agency, to handle the military use of space.",
   "The Defence Cyber Agency, to deal with threats in cyberspace.",
   "The Armed Forces Special Operations Division, to plan and run special operations."],
  ["सेना द्वारा अंतरिक्ष के उपयोग को सँभालने के लिए रक्षा अंतरिक्ष एजेंसी।",
   "साइबर स्पेस के ख़तरों से निपटने के लिए रक्षा साइबर एजेंसी।",
   "विशेष अभियानों की योजना बनाने और उन्हें चलाने के लिए सशस्त्र बल विशेष अभियान प्रभाग।"],
  C3, 2,
  "All three were set up, and each draws personnel from the Army, the Navy and the Air Force. Space, cyberspace and special operations cut across the domains of the individual services, so a joint agency avoids duplication and builds a common capability. "
  "They reflect the wider move towards 'jointness', taken further by the post of Chief of Defence Staff and the Department of Military Affairs created in 2020.",
  "तीनों स्थापित की गईं, और हर एक में थल सेना, नौसेना और वायु सेना के कर्मी हैं। अंतरिक्ष, साइबर स्पेस और विशेष अभियान अलग-अलग सेनाओं के क्षेत्रों के आर-पार हैं, इसलिए संयुक्त एजेंसी दोहराव से बचाती और साझा क्षमता बनाती है। "
  "ये 'संयुक्तता' की व्यापक दिशा को दर्शाती हैं, जिसे 2020 में बने चीफ़ ऑफ़ डिफ़ेंस स्टाफ़ के पद और सैन्य कार्य विभाग ने आगे बढ़ाया।",
  f"{MOD} (Integrated Defence Staff).",
  "l1-sci-tri-service-space-cyber-sof", craft="recall")

S(DF, "medium", "Consider the following statements about the Agnipath scheme, launched in 2022:",
  "2022 में आरंभ अग्निपथ योजना के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Recruits under it, called Agniveers, are enrolled for four years.",
   "Up to 25 per cent of each batch may be selected for the regular cadre.",
   "It applies to the Army, the Navy and the Air Force.",
   "Agniveers who leave after four years receive a lump-sum 'Seva Nidhi' package."],
  ["इसके अंतर्गत भर्ती, जिन्हें अग्निवीर कहा जाता है, चार वर्ष के लिए नामांकित होते हैं।",
   "हर बैच के 25 प्रतिशत तक को नियमित कैडर के लिए चुना जा सकता है।",
   "यह थल सेना, नौसेना और वायु सेना पर लागू होती है।",
   "चार वर्ष बाद सेवा छोड़ने वाले अग्निवीरों को एकमुश्त 'सेवा निधि' पैकेज मिलता है।"],
  C4, 3,
  "All four statements are correct. The scheme replaced earlier recruitment to the ranks below officers, with the aims of a younger force and a lower pension bill, since those who leave after four years are not entitled to pensions. "
  "The Seva Nidhi combines the Agniveer's own contributions with a matching government contribution and interest; several States and central forces reserve jobs for former Agniveers.",
  "चारों कथन सही हैं। इस योजना ने अधिकारी से नीचे के पदों की पहले की भर्ती का स्थान लिया, युवा सेना और कम पेंशन बोझ के उद्देश्य से, क्योंकि चार वर्ष बाद जाने वालों को पेंशन का अधिकार नहीं है। "
  "सेवा निधि में अग्निवीर का अपना अंशदान, उतना ही सरकारी अंशदान और ब्याज जुड़ता है; कई राज्य और केंद्रीय बल पूर्व अग्निवीरों के लिए नौकरियाँ आरक्षित करते हैं।",
  f"{MOD} (Agnipath scheme).",
  "l1-sci-agnipath-scheme", craft="recall")

S(DF, "medium", "Consider the following statements about the Defence Acquisition Procedure, 2020:",
  "रक्षा अधिग्रहण प्रक्रिया (DAP), 2020 के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It replaced the Defence Procurement Procedure of 2016.",
   "It gives the highest priority to the 'Buy (Indian-IDDM)' category.",
   "IDDM stands for 'Indigenously Designed, Developed and Manufactured'.",
   "It introduced leasing as a new way of acquiring military equipment."],
  ["इसने 2016 की रक्षा ख़रीद प्रक्रिया का स्थान लिया।",
   "यह 'Buy (Indian-IDDM)' श्रेणी को सर्वोच्च प्राथमिकता देती है।",
   "IDDM का अर्थ है 'स्वदेशी रूप से डिज़ाइन, विकसित और निर्मित'।",
   "इसने सैन्य उपकरण पाने के नए तरीक़े के रूप में पट्टे (leasing) की शुरुआत की।"],
  C4, 3,
  "All four statements are correct. Ranking indigenously designed products first, ahead of buying from Indian firms that make foreign designs and ahead of imports, rewards design capability rather than assembly alone. "
  "Leasing lets the services use costly assets, such as surveillance drones or transport aircraft, without paying the full price at once -- the Navy leased MQ-9B drones in this way.",
  "चारों कथन सही हैं। स्वदेशी रूप से डिज़ाइन किए उत्पादों को सबसे ऊपर रखना, विदेशी डिज़ाइन बनाने वाली भारतीय फ़र्मों से ख़रीद और आयात से पहले, केवल संयोजन के बजाय डिज़ाइन क्षमता को पुरस्कृत करता है। "
  "पट्टा सेनाओं को निगरानी ड्रोन या परिवहन विमान जैसी महँगी परिसंपत्तियों का उपयोग पूरी कीमत एक साथ चुकाए बिना करने देता है -- नौसेना ने इसी तरह MQ-9B ड्रोन पट्टे पर लिए।",
  f"{MOD} (Defence Acquisition Procedure 2020).",
  "l1-sci-dap-2020-iddm-leasing", craft="precision")

# ---------------------------------------------------------------- medium Statement-I/II (1)
A(DF, "medium",
  "A thermal imaging camera can show a person in complete darkness and through light smoke.",
  "ताप प्रतिबिंबन (thermal imaging) कैमरा पूर्ण अंधकार में और हल्के धुएँ के आर-पार भी किसी व्यक्ति को दिखा सकता है।",
  "It detects the infrared radiation that warm bodies give out, rather than visible light reflected from them.",
  "यह गर्म पिंडों द्वारा उत्सर्जित अवरक्त विकिरण का पता लगाता है, न कि उनसे परावर्तित दृश्य प्रकाश का।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I. Every warm object emits infrared radiation, more strongly the hotter it is, so a person stands out against a cooler background even with no light at all -- which is why thermal imagers are used for border surveillance, search and rescue and firefighting. "
  "The older kind of night-vision device, the image intensifier, amplifies faint starlight or moonlight and so needs at least some light to work.",
  "दोनों कथन सही हैं, और कथन-II कथन-I की व्याख्या करता है। हर गर्म वस्तु अवरक्त विकिरण उत्सर्जित करती है, जितनी अधिक गर्म उतना अधिक, इसलिए बिल्कुल प्रकाश न होने पर भी व्यक्ति ठंडी पृष्ठभूमि के सामने अलग दिखता है -- इसीलिए ताप प्रतिबिंबक सीमा निगरानी, खोज और बचाव तथा अग्निशमन में प्रयुक्त होते हैं। "
  "रात्रि-दृष्टि का पुराना प्रकार, प्रतिबिंब तीव्रक (image intensifier), तारों या चाँद के मंद प्रकाश को बढ़ाता है, इसलिए उसे काम करने के लिए कुछ प्रकाश चाहिए।",
  "NCERT Class XI, Physics (Thermal Properties of Matter: radiation); NCERT Class XII, Physics (Electromagnetic Waves).",
  "l1-sci-thermal-imaging-infrared", craft="inference")

# ---------------------------------------------------------------- hard statement (1)
S(DF, "hard", "Consider the following statements about warships and submarines built in India:",
  "भारत में बने युद्धपोतों और पनडुब्बियों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The aircraft carrier INS Vikrant was built at Cochin Shipyard.",
   "The Kalvari-class submarines, of the French Scorpene design, were built at Mazagon Dock in Mumbai.",
   "INS Vikrant is powered by a nuclear reactor."],
  ["विमानवाहक पोत INS विक्रांत कोचीन शिपयार्ड में बना।",
   "फ़्रांसीसी स्कॉर्पीन डिज़ाइन की कलवरी-श्रेणी की पनडुब्बियाँ मुंबई के मझगाँव डॉक में बनीं।",
   "INS विक्रांत नाभिकीय रिएक्टर से चलता है।"],
  C3, 1,
  "Statements 1 and 2 are correct: the Kalvari class was built under Project 75 with technology transfer from France, a step towards designing submarines in India. "
  "Statement 3 is wrong: Vikrant is driven by gas turbines; India's nuclear-powered vessels are its ballistic-missile submarines of the Arihant class, for which a nuclear reactor allows months underwater without surfacing.",
  "कथन 1 और 2 सही हैं: कलवरी श्रेणी परियोजना 75 के अंतर्गत फ़्रांस से तकनीक हस्तांतरण के साथ बनी, जो भारत में पनडुब्बियाँ डिज़ाइन करने की दिशा में एक कदम था। "
  "कथन 3 गलत है: विक्रांत गैस टरबाइनों से चलता है; भारत के नाभिकीय ऊर्जा से चलने वाले पोत अरिहंत श्रेणी की बैलिस्टिक प्रक्षेपास्त्र पनडुब्बियाँ हैं, जिनके लिए नाभिकीय रिएक्टर बिना सतह पर आए महीनों पानी के भीतर रहना संभव बनाता है।",
  f"{MOD}; Indian Navy.",
  "l1-sci-vikrant-kalvari-shipyards", craft="precision")

write("sci_l1_t6_e.sql")
