# -*- coding: utf-8 -*-
"""Level 3 · Test 1 (GS Integrated Test 1) -- part D: Geography (10) (upsc_l3_cell_targets.mjs 1).
Geography cells: Resources e-SI; Transport e-pairs; Climatology h-MCQ, m-stmt; Indian Physiography h-SI, m-stmt;
World Regions m-MCQ, m-stmt; Indian Rivers m-stmt; Geomorphology m-stmt.
Level 2 holds 310 Geography rows and Level 1 another 112, covering the standard India and world lists down to the
Palghat gap, Doddabetta, the Somali jet and the transcontinental railways. Every fact here was grepped against both and
is one neither tests: shale gas; the Kiel, Corinth and Volga-Don canals and the Soo Locks; the Madden-Julian
Oscillation; the Thal and Bhor ghats; the Okavango; the Atacama; the Bharathapuzha and the Tamraparni; isostasy and
post-glacial rebound; Lake Chad, the Drake Passage and the Wallace Line; Karbi Anglong, the Shencottah gap and Parasnath.
MCQ keys are pinned (pos)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, T2

d.SUBJECT = "Geography"
d.REQUIRE_CRAFT = True
FPG = "NCERT Class XI, Fundamentals of Physical Geography"
IPE = "NCERT Class XI, India: Physical Environment"
FHG = "NCERT Class XII, Fundamentals of Human Geography"
IPEc = "NCERT Class XII, India: People and Economy"

# ---------------------------------------------------------------- Resources (e-SI)
A("Resources: Minerals, Energy & Agriculture", "easy",
  "Statement-I: Shale gas does not flow readily into an ordinary vertical well.",
  "कथन-I: शेल गैस किसी साधारण ऊर्ध्वाधर कुएँ में आसानी से प्रवाहित नहीं होती।",
  "Statement-II: Shale gas is produced by drilling horizontally through the rock and fracturing it with water, sand and chemicals pumped in at high pressure.",
  "कथन-II: शेल गैस चट्टान में क्षैतिज वेधन करके और उच्च दाब पर पानी, रेत और रसायन डालकर उसे तोड़कर निकाली जाती है।",
  1,
  "Both statements are correct, but Statement-II does not explain Statement-I. The gas does not flow because shale is a fine-grained rock of very low permeability, which holds the gas in tiny, poorly connected pores; that is the reason. "
  "Statement-II describes the method -- horizontal drilling and hydraulic fracturing ('fracking') -- that the low permeability makes necessary; it is a consequence of Statement-I, not its explanation. Fracking's large use of water and the risk to groundwater are the main concerns about it.",
  "दोनों कथन सही हैं, पर कथन-II कथन-I की व्याख्या नहीं करता। गैस इसलिए प्रवाहित नहीं होती कि शेल बहुत कम पारगम्यता वाली महीन कणों की चट्टान है, जो गैस को सूक्ष्म, कम जुड़े छिद्रों में रोके रखती है; यही कारण है। "
  "कथन-II वह विधि बताता है -- क्षैतिज वेधन और हाइड्रोलिक फ्रैक्चरिंग ('फ्रैकिंग') -- जिसे कम पारगम्यता आवश्यक बनाती है; यह कथन-I का परिणाम है, उसकी व्याख्या नहीं। फ्रैकिंग में पानी का भारी उपयोग और भूजल को ख़तरा इसकी मुख्य चिंताएँ हैं।",
  f"{IPEc} (Mineral and Energy Resources); Directorate General of Hydrocarbons.",
  "l3-t1-geo-shale-gas-fracking", craft="inference")

# ---------------------------------------------------------------- Transport, Ports & Human Geography (e-pairs)
P("Transport, Ports & Human Geography", "easy", "Consider the following pairs of canals and the waters they link:",
  "नहरों और उनके द्वारा जोड़े गए जलक्षेत्रों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Kiel Canal : The North Sea and the Baltic Sea",
   "Corinth Canal : The Gulf of Corinth and the Saronic Gulf of the Aegean",
   "Volga-Don Canal : The Volga and the Don, linking the Caspian Sea with the Sea of Azov",
   "Soo Locks : Lake Erie and Lake Ontario"],
  ["कील नहर : उत्तरी सागर और बाल्टिक सागर",
   "कोरिंथ नहर : कोरिंथ की खाड़ी और ईजियन सागर की सारोनिक खाड़ी",
   "वोल्गा-डॉन नहर : वोल्गा और डॉन, जो कैस्पियन सागर को आज़ोव सागर से जोड़ती है",
   "सू लॉक्स : ईरी झील और ओंटारियो झील"],
  2,
  "The first three pairs are correct. The Kiel Canal crosses the base of the Jutland peninsula in Germany; the Corinth Canal cuts through the narrow isthmus of Corinth in Greece; and the Volga-Don Canal joins Russia's two great rivers, giving the landlocked Caspian a waterway to the Sea of Azov and the Black Sea. "
  "The fourth is wrong: the Soo Locks, at Sault Ste. Marie, lift ships between Lake Superior and Lake Huron; it is the Welland Canal that bypasses Niagara Falls between Lake Erie and Lake Ontario.",
  "पहले तीन युग्म सही हैं। कील नहर जर्मनी में जटलैंड प्रायद्वीप के आधार को पार करती है; कोरिंथ नहर यूनान के कोरिंथ के संकीर्ण स्थलडमरूमध्य को काटती है; और वोल्गा-डॉन नहर रूस की दो बड़ी नदियों को जोड़ती है, जिससे स्थलरुद्ध कैस्पियन को आज़ोव सागर और काला सागर तक जलमार्ग मिलता है। "
  "चौथा ग़लत है: सॉल्ट सेंट मैरी के सू लॉक्स जहाज़ों को सुपीरियर झील और ह्यूरन झील के बीच उठाते-उतारते हैं; ईरी और ओंटारियो झीलों के बीच नियाग्रा प्रपात से बचाकर जाने वाली वेलैंड नहर है।",
  f"{FHG} (Transport and Communication).",
  "l3-t1-geo-canals-kiel-corinth-volga-don-soo", craft="recall")

# ---------------------------------------------------------------- Climatology & Biomes (h-MCQ, m-stmt)
M("Climatology & Biomes", "hard",
  "Which one of the following best describes the Madden-Julian Oscillation (MJO), which forecasters watch for its effect on the Indian monsoon?",
  "निम्नलिखित में से कौन-सा मैडेन-जूलियन दोलन (MJO) का सबसे अच्छा वर्णन करता है, जिस पर पूर्वानुमानकर्ता भारतीय मानसून पर उसके प्रभाव के कारण नज़र रखते हैं?",
  ["A warming of the eastern Pacific that recurs every two to seven years and tends to weaken the monsoon",
   "A difference between the sea-surface temperatures of the western and the eastern Indian Ocean",
   "A seasonal reversal of the winds over the Arabian Sea caused by the unequal heating of land and sea",
   "An eastward-moving pulse of cloud and rain near the equator that returns every 30 to 60 days or so"],
  ["पूर्वी प्रशांत का गर्म होना जो हर दो से सात वर्षों में लौटता है और मानसून को कमज़ोर करता है",
   "पश्चिमी और पूर्वी हिंद महासागर के समुद्री सतही तापमानों के बीच का अंतर",
   "स्थल और समुद्र के असमान गर्म होने से अरब सागर पर हवाओं का मौसमी उलटाव",
   "भूमध्यरेखा के पास पूर्व की ओर बढ़ता बादल-वर्षा स्पंद, जो लगभग 30 से 60 दिनों में लौटता है"],
  3,
  "The MJO is a travelling disturbance of clouds, rainfall, winds and pressure that moves east along the equator, from the Indian Ocean into the Pacific, and recurs roughly every 30 to 60 days. When its wet phase is over the Indian Ocean it tends to favour an active spell of the monsoon, and its dry phase can bring a break. "
  "The other options describe El Niño, the Indian Ocean Dipole and the monsoon itself -- all slower, seasonal-to-yearly phenomena, whereas the MJO acts within a season.",
  "MJO बादलों, वर्षा, हवाओं और दाब का एक चलायमान विक्षोभ है जो भूमध्यरेखा के साथ हिंद महासागर से प्रशांत की ओर पूर्व में बढ़ता है और लगभग हर 30 से 60 दिनों में लौटता है। जब उसका आर्द्र चरण हिंद महासागर पर होता है तो वह मानसून की सक्रिय अवधि में सहायक होता है, और उसका शुष्क चरण विराम ला सकता है। "
  "बाक़ी विकल्प एल नीनो, हिंद महासागर द्विध्रुव और स्वयं मानसून का वर्णन करते हैं -- ये सभी धीमी, मौसमी से वार्षिक घटनाएँ हैं, जबकि MJO एक ही मौसम के भीतर काम करता है।",
  "India Meteorological Department (extended-range forecasts); " + IPE + " (Climate).",
  "l3-t1-geo-madden-julian-oscillation", pos=3, craft="precision")

S("Climatology & Biomes", "medium", "With reference to the Atacama Desert, consider the following statements:",
  "अटाकामा मरुस्थल के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["It lies on the eastern side of the Andes, mostly in Argentina.",
   "It lies in the belt of the westerlies, which bring it most of its rain in winter."],
  ["यह एंडीज़ के पूर्वी ओर, अधिकतर अर्जेंटीना में स्थित है।",
   "यह पछुआ पवनों की पेटी में स्थित है, जो इसे अधिकांश वर्षा शीत ऋतु में लाती हैं।"],
  T2, 3,
  "Neither statement is correct. The Atacama lies on the Pacific side of the Andes, mostly in northern Chile, and is among the driest places on Earth. "
  "It lies under the subtropical high-pressure belt, not the westerlies; the cold Humboldt (Peru) current offshore chills the air and keeps it stable, and the Andes block moisture from the Amazon side -- so almost no rain falls in any season. Its fog, called camanchaca, is the main source of moisture for life near the coast.",
  "कोई भी कथन सही नहीं है। अटाकामा एंडीज़ के प्रशांत की ओर, अधिकतर उत्तरी चिली में स्थित है, और पृथ्वी के सबसे शुष्क स्थानों में से है। "
  "यह पछुआ पवनों की नहीं, उपोष्ण उच्च-दाब पेटी के नीचे है; तट के पास की ठंडी हम्बोल्ट (पेरू) धारा हवा को ठंडा और स्थिर रखती है, और एंडीज़ अमेज़न की ओर की नमी रोक लेते हैं -- इसलिए किसी भी ऋतु में लगभग वर्षा नहीं होती। इसका कोहरा, जिसे कामांचाका कहते हैं, तट के पास जीवन के लिए नमी का मुख्य स्रोत है।",
  f"{FPG} (World Climate; Water in the Atmosphere); {FHG}.",
  "l3-t1-geo-atacama-desert", craft="inference")

# ---------------------------------------------------------------- Indian Physiography, Climate & Regions (h-SI, m-stmt)
A("Indian Physiography, Climate & Regions", "hard",
  "Statement-I: The Thal Ghat and the Bhor Ghat carry the main road and railway routes from Mumbai onto the Deccan plateau.",
  "कथन-I: थाल घाट और भोर घाट मुंबई से दक्कन पठार तक मुख्य सड़क और रेल मार्ग ले जाते हैं।",
  "Statement-II: The Western Ghats rise steeply from the narrow coastal plain as an almost continuous wall, which roads and railways can climb only at a few passes.",
  "कथन-II: पश्चिमी घाट संकीर्ण तटीय मैदान से लगभग सतत दीवार के रूप में खड़ी ढलान से उठते हैं, जिन पर सड़कें और रेलें केवल कुछ दर्रों पर ही चढ़ सकती हैं।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I. The Sahyadri present a steep escarpment to the west and slope gently east; because the wall is so continuous, routes from the coast are funnelled through a few passes, "
  "which is why the Thal Ghat (towards Nashik) and the Bhor Ghat (towards Pune) became the gateways from Mumbai to the plateau, with the railways climbing them through tunnels and reversing stations. The Eastern Ghats, by contrast, are broken into separate hill groups by the rivers that cut through them.",
  "दोनों कथन सही हैं, और कथन-II कथन-I की व्याख्या करता है। सह्याद्रि पश्चिम की ओर खड़ा कगार बनाते हैं और पूर्व की ओर धीरे ढलते हैं; दीवार इतनी सतत है कि तट से आने वाले मार्ग कुछ ही दर्रों से होकर गुज़रते हैं, "
  "इसीलिए थाल घाट (नासिक की ओर) और भोर घाट (पुणे की ओर) मुंबई से पठार के प्रवेश-द्वार बने, जिन पर रेलें सुरंगों और उलटाव स्टेशनों से होकर चढ़ती हैं। इसके विपरीत पूर्वी घाट उन्हें काटने वाली नदियों से अलग-अलग पहाड़ी समूहों में बँटे हैं।",
  f"{IPE} (Structure and Physiography); Indian Railways (Central Railway ghat sections).",
  "l3-t1-geo-thal-bhor-ghats", craft="inference")

S("Indian Physiography, Climate & Regions", "medium", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Karbi Anglong plateau of Assam, like the Meghalaya plateau, is a part of the Peninsular block that stands detached from its main mass.",
   "The Shencottah gap in the southern Western Ghats carries a road and a railway between Kerala and Tamil Nadu.",
   "Parasnath, the highest point of the Chota Nagpur plateau, lies in Odisha."],
  ["असम का कार्बी आंगलोंग पठार, मेघालय पठार की तरह, प्रायद्वीपीय खंड का एक भाग है जो उसके मुख्य भाग से अलग है।",
   "दक्षिणी पश्चिमी घाट का शेनकोट्टा दर्रा केरल और तमिलनाडु के बीच एक सड़क और एक रेलमार्ग ले जाता है।",
   "छोटानागपुर पठार का सबसे ऊँचा स्थान पारसनाथ ओडिशा में है।"],
  C3, 1,
  "Statements 1 and 2 are correct. The Meghalaya and Karbi Anglong plateaus are outliers of the old Peninsular block, cut off from it by the Garo-Rajmahal gap, which is why ancient rocks surface so far to the north-east. "
  "The Shencottah (Sengottai) gap carries the Kollam-Tirunelveli road and railway across the southern Ghats. Statement 3 is wrong: Parasnath, about 1,365 m high and sacred to the Jains, is in the Giridih district of Jharkhand.",
  "कथन 1 और 2 सही हैं। मेघालय और कार्बी आंगलोंग पठार पुराने प्रायद्वीपीय खंड के बाहरी भाग हैं, जो गारो-राजमहल दरार से उससे कट गए हैं, इसीलिए प्राचीन चट्टानें इतनी दूर उत्तर-पूर्व में सतह पर दिखती हैं। "
  "शेनकोट्टा (सेंगोट्टई) दर्रा दक्षिणी घाटों के पार कोल्लम-तिरुनेलवेली सड़क और रेलमार्ग ले जाता है। कथन 3 ग़लत है: लगभग 1,365 मीटर ऊँचा और जैनों के लिए पवित्र पारसनाथ झारखंड के गिरिडीह ज़िले में है।",
  f"{IPE} (Structure and Physiography).",
  "l3-t1-geo-karbi-anglong-shencottah-parasnath", craft="precision")

# ---------------------------------------------------------------- World Regions, Water Bodies & Places (m-MCQ, m-stmt)
M("World Regions, Water Bodies & Places", "medium",
  "The Okavango river does not reach the sea; it ends in a vast inland delta in the Kalahari that floods each year. In which country does that delta lie?",
  "ओकावांगो नदी समुद्र तक नहीं पहुँचती; वह कालाहारी में एक विशाल आंतरिक डेल्टा में समाप्त होती है जिसमें हर वर्ष बाढ़ आती है। वह डेल्टा किस देश में स्थित है?",
  ["Angola, where the river rises in the highlands", "Namibia, through whose Caprivi strip the river flows", "Zambia, on the upper Zambezi", "Botswana, whose capital is Gaborone"],
  ["अंगोला, जहाँ नदी पठारों से निकलती है", "नामीबिया, जिसकी कैप्रिवी पट्टी से नदी बहती है", "ज़ाम्बिया, ऊपरी ज़ाम्बेज़ी पर", "बोत्सवाना, जिसकी राजधानी गैबोरोन है"],
  3,
  "The Okavango rises in the highlands of Angola, crosses the Caprivi strip of Namibia and spreads out in northern Botswana into the Okavango Delta, where almost all its water evaporates or seeps into the Kalahari sands. "
  "The flood arrives in the dry winter months, months after the rains upstream, and draws great herds of wildlife; the delta is both a Ramsar site and a World Heritage Site.",
  "ओकावांगो अंगोला के पठारों से निकलती है, नामीबिया की कैप्रिवी पट्टी पार करती है और उत्तरी बोत्सवाना में ओकावांगो डेल्टा में फैल जाती है, जहाँ उसका लगभग सारा पानी वाष्पित हो जाता है या कालाहारी की रेत में रिस जाता है। "
  "बाढ़ ऊपर की वर्षा के महीनों बाद, शुष्क शीत ऋतु में आती है, और वन्यजीवों के बड़े झुंडों को आकर्षित करती है; डेल्टा रामसर स्थल भी है और विश्व धरोहर स्थल भी।",
  f"{FHG}; UNESCO World Heritage List (Okavango Delta, 2014).",
  "l3-t1-geo-okavango-inland-delta", pos=2, craft="recall")

S("World Regions, Water Bodies & Places", "medium", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Lake Chad, shared by Chad, Cameroon, Niger and Nigeria, has shrunk greatly since the 1960s.",
   "The Drake Passage separates the southern tip of Africa from Antarctica.",
   "The Wallace Line, which separates the animals of Asia from those of Australasia, runs between Sumatra and Java."],
  ["चाड, कैमरून, नाइजर और नाइजीरिया के बीच साझा चाड झील 1960 के दशक से बहुत सिकुड़ गई है।",
   "ड्रेक पैसेज अफ़्रीका के दक्षिणी सिरे को अंटार्कटिका से अलग करता है।",
   "वालेस रेखा, जो एशिया के जीवों को ऑस्ट्रेलेशिया के जीवों से अलग करती है, सुमात्रा और जावा के बीच से गुज़रती है।"],
  C3, 0,
  "Only statement 1 is correct. Lake Chad, a shallow lake on the edge of the Sahara, has lost most of its open water since the 1960s through drought and irrigation, with grave effects on the millions who depend on it. "
  "The Drake Passage separates South America (Cape Horn) from Antarctica, not Africa. The Wallace Line runs between Bali and Lombok and between Borneo and Sulawesi; Sumatra and Java both lie on the Asian side, on the shallow Sunda shelf.",
  "केवल कथन 1 सही है। सहारा के किनारे की उथली चाड झील ने 1960 के दशक से सूखे और सिंचाई के कारण अपना अधिकांश खुला जल खो दिया है, जिसका उस पर निर्भर लाखों लोगों पर गंभीर प्रभाव पड़ा है। "
  "ड्रेक पैसेज दक्षिण अमेरिका (केप हॉर्न) को अंटार्कटिका से अलग करता है, अफ़्रीका को नहीं। वालेस रेखा बाली और लोम्बोक के बीच तथा बोर्नियो और सुलावेसी के बीच से गुज़रती है; सुमात्रा और जावा दोनों उथले सुंडा शेल्फ़ पर एशियाई ओर हैं।",
  f"{FPG}; {FHG}.",
  "l3-t1-geo-lake-chad-drake-wallace", craft="precision")

# ---------------------------------------------------------------- Indian Rivers, Lakes & Wetlands (m-stmt)
S("Indian Rivers, Lakes & Wetlands", "medium", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Bharathapuzha, the second longest river of Kerala, flows west through the Palghat gap to the Arabian Sea.",
   "The Tamraparni rises in the Western Ghats and flows east into the Gulf of Mannar.",
   "Both are short rivers that reach the sea directly, without joining the Kaveri."],
  ["केरल की दूसरी सबसे लंबी नदी भारतपुझा पालघाट दर्रे से होकर पश्चिम की ओर अरब सागर में बहती है।",
   "ताम्रपर्णी पश्चिमी घाट से निकलती है और पूर्व की ओर मन्नार की खाड़ी में बहती है।",
   "दोनों छोटी नदियाँ हैं जो कावेरी से मिले बिना सीधे समुद्र तक पहुँचती हैं।"],
  C3, 2,
  "All three are correct. The Bharathapuzha (Nila) rises in the Anamalai hills, gathers tributaries from both sides of the Palghat gap and enters the sea at Ponnani; only the Periyar is longer in Kerala. "
  "The Tamraparni rises near Agasthyamalai and flows east through Tirunelveli and Thoothukudi districts to the Gulf of Mannar; fed by both monsoons, it is unusual among Tamil Nadu's rivers in carrying water through much of the year. Neither is a tributary of the Kaveri.",
  "तीनों सही हैं। भारतपुझा (नीला) अनामलाई पहाड़ियों से निकलती है, पालघाट दर्रे के दोनों ओर से सहायक नदियाँ लेती है और पोन्नानी में समुद्र में मिलती है; केरल में केवल पेरियार उससे लंबी है। "
  "ताम्रपर्णी अगस्त्यमलई के पास से निकलती है और तिरुनेलवेली और थूथुकुडी ज़िलों से होकर पूर्व में मन्नार की खाड़ी तक बहती है; दोनों मानसूनों से पोषित, वह तमिलनाडु की नदियों में असामान्य है क्योंकि उसमें वर्ष के अधिकांश भाग में पानी रहता है। कोई भी कावेरी की सहायक नदी नहीं है।",
  f"{IPE} (Drainage System); Central Water Commission.",
  "l3-t1-geo-bharathapuzha-tamraparni", craft="recall")

# ---------------------------------------------------------------- Geomorphology & Earth's Interior (m-stmt)
S("Geomorphology & Earth's Interior", "medium", "With reference to isostasy, consider the following statements:",
  "समस्थिति (आइसोस्टेसी) के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["The idea holds that the crust 'floats' on the denser mantle beneath, so that high mountains are balanced by deep roots of lighter rock.",
   "Pratt's version explains differences in elevation by differences in the density of crustal blocks rather than in their thickness.",
   "Where great ice sheets have melted, the land beneath them has gone on sinking ever since."],
  ["यह धारणा कहती है कि भूपर्पटी नीचे के अधिक सघन मेंटल पर 'तैरती' है, इसलिए ऊँचे पर्वतों का संतुलन हल्की चट्टानों की गहरी 'जड़ों' से होता है।",
   "प्रैट का रूप ऊँचाई के अंतर को भूपर्पटी के खंडों की मोटाई के बजाय उनके घनत्व के अंतर से समझाता है।",
   "जहाँ विशाल हिम-चादरें पिघली हैं, वहाँ उनके नीचे की भूमि तब से लगातार धँसती गई है।"],
  C3, 1,
  "Statements 1 and 2 are correct. Isostasy is the balance of crustal blocks on the denser mantle: in Airy's version, mountains stand high because they have thick roots, like a large iceberg; in Pratt's, because they are made of lighter rock. "
  "Statement 3 is wrong: when an ice sheet melts, its weight is removed and the land rises -- a slow post-glacial rebound still lifting Scandinavia and the shores of Hudson Bay thousands of years after the ice left.",
  "कथन 1 और 2 सही हैं। समस्थिति सघन मेंटल पर भूपर्पटी के खंडों का संतुलन है: एयरी के रूप में पर्वत इसलिए ऊँचे हैं कि उनकी मोटी जड़ें हैं, जैसे बड़े हिमशैल की; प्रैट के रूप में इसलिए कि वे हल्की चट्टानों के बने हैं। "
  "कथन 3 ग़लत है: जब हिम-चादर पिघलती है तो उसका भार हट जाता है और भूमि ऊपर उठती है -- यह धीमा हिमनदोत्तर उत्थान बर्फ़ हटने के हज़ारों वर्ष बाद भी स्कैंडिनेविया और हडसन खाड़ी के तटों को उठा रहा है।",
  f"{FPG} (The Origin and Evolution of the Earth; Interior of the Earth).",
  "l3-t1-geo-isostasy-airy-pratt-rebound", craft="inference")

write("gs_l3_t1_d.sql")
