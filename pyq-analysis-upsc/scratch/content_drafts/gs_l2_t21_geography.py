# -*- coding: utf-8 -*-
"""Level 2 · Test 21 (GS Comprehensive Revision, full syllabus) -- Geography block (10 of the paper's 84 static rows).
  Indian Physiography 2, World Regions 2, Climatology 2, Resources 1, Transport 1, Indian Rivers 1, Geomorphology 1.
  Cells: medium statement 3, easy statement 1, hard statement 1, medium pairs 1, medium MCQ 1, hard MCQ 1,
    medium Statement-I/II 1, easy Statement-I/II 1.
Tests 12-14 hold the Earth's interior, pressure belts, jet streams, local winds, inversion, humidity and dew point,
the blue sky, the Roaring Forties, the horse latitudes, the IOD, soils, the monsoon, the Himalayan ranges and duns,
Bhabar-Terai, karewas, kayals, the Rann, the Aravallis, lakes and Ramsar lakes, the big dams (Tehri, Bhakra,
Nagarjuna Sagar, Sardar Sarovar, Koyna, Idukki), the Chenab/Pamban/Atal bridges, ports, DFCs, straits and grasslands,
so none of those is tested. Checked-clean facts used: Kuttanad, Bagar, teris, Mishmi and Dafla hills, the
Angel/Iguazu/Tugela/Kaieteur falls, the Alliance of Sahel States, adiabatic cooling, El Nino and the Walker
circulation, Sukinda, Rampura Agucha, Kolar, Bogibeel, Hirakud/Almatti/Ukai and exfoliation."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Geography"
PH = "Indian Physiography, Climate & Regions"
WR = "World Regions, Water Bodies & Places"
CL = "Climatology & Biomes"
RS = "Resources: Minerals, Energy & Agriculture"
TH = "Transport, Ports & Human Geography"
RV = "Indian Rivers, Lakes & Wetlands"
GM = "Geomorphology & Earth's Interior"
NC11 = "NCERT Class XI, Fundamentals of Physical Geography"
NC11I = "NCERT Class XI, India: Physical Environment"
NC12I = "NCERT Class XII, India: People and Economy"
ATLAS = "Oxford School Atlas"
IBM = "Indian Bureau of Mines -- Indian Minerals Yearbook"
IMD = "India Meteorological Department"

# ================================================================ INDIAN PHYSIOGRAPHY (2)
S(PH, "medium", "Consider the following statements about regions of India:",
  "भारत के क्षेत्रों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Kuttanad in Kerala is among the few places in the world where farming is carried on below mean sea level.",
   "The Bagar is a semi-arid tract lying between the Marusthali and the Aravalli hills.",
   "The red sand dunes known as teris are found along the Konkan coast."],
  ["केरल का कुट्टनाड दुनिया के उन गिने-चुने स्थानों में है जहाँ माध्य समुद्र तल से नीचे खेती की जाती है।",
   "बागर मरुस्थली और अरावली पहाड़ियों के बीच स्थित एक अर्ध-शुष्क पट्टी है।",
   "टेरी नाम से जाने जाने वाले लाल बालू के टीले कोंकण तट पर पाए जाते हैं।"],
  C3, 1,
  "Statements 1 and 2 are correct. Kuttanad, in the Alappuzha-Kottayam region, grows rice on reclaimed land one to two metres below sea level, protected by dykes; the FAO recognises it as a Globally Important Agricultural Heritage System. "
  "The Bagar is the semi-arid strip east of the true desert (Marusthali) and west of the Aravallis, crossed by short seasonal streams. "
  "Statement 3 is wrong: teris are red sand dunes of the Tamil Nadu coast, mainly in Thoothukudi and Tirunelveli districts.",
  "कथन 1 और 2 सही हैं। अलप्पुझा-कोट्टयम क्षेत्र का कुट्टनाड समुद्र तल से एक-दो मीटर नीचे की पुनः प्राप्त भूमि पर, तटबंधों की सुरक्षा में, धान उगाता है; FAO इसे विश्व स्तर पर महत्वपूर्ण कृषि विरासत प्रणाली (GIAHS) मानता है। "
  "बागर वास्तविक मरुस्थल (मरुस्थली) के पूर्व और अरावली के पश्चिम की अर्ध-शुष्क पट्टी है, जिसे छोटी मौसमी धाराएँ पार करती हैं। "
  "कथन 3 गलत है: टेरी तमिलनाडु तट के लाल बालू के टीले हैं, मुख्यतः थूथुकुडी और तिरुनेलवेली ज़िलों में।",
  f"{NC11I} -- Structure and Physiography; FAO -- Globally Important Agricultural Heritage Systems.",
  "igeo-kuttanad-bagar-teri")

S(PH, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Mishmi Hills lie in Arunachal Pradesh.",
   "The Dafla Hills lie in Nagaland."],
  ["मिशमी पहाड़ियाँ अरुणाचल प्रदेश में हैं।",
   "डफला पहाड़ियाँ नागालैंड में हैं।"],
  T2, 0,
  "Only statement 1 is correct. The Mishmi Hills rise in eastern Arunachal Pradesh, around the Dibang and Lohit valleys, where the Himalaya bends south. "
  "The Dafla Hills are also in Arunachal Pradesh, in its western-central part, named after the Nyishi people once called Daflas; Nagaland's hills belong to the Patkai-Naga system along the Myanmar border.",
  "केवल कथन 1 सही है। मिशमी पहाड़ियाँ पूर्वी अरुणाचल प्रदेश में दिबांग और लोहित घाटियों के आसपास उठती हैं, जहाँ हिमालय दक्षिण की ओर मुड़ता है। "
  "डफला पहाड़ियाँ भी अरुणाचल प्रदेश में, उसके पश्चिम-मध्य भाग में हैं, जिनका नाम उन न्यिशी लोगों पर पड़ा जिन्हें पहले डफला कहा जाता था; नागालैंड की पहाड़ियाँ म्यांमार सीमा के साथ पटकाई-नागा श्रेणी का भाग हैं।",
  f"{NC11I} -- Structure and Physiography; {ATLAS}.",
  "igeo-mishmi-dafla-hills-easy")

# ================================================================ WORLD REGIONS (2)
P(WR, "medium", "Consider the following pairs of waterfalls and the countries where they are located:",
  "जलप्रपातों और उन देशों के निम्नलिखित युग्मों पर विचार कीजिए जहाँ वे स्थित हैं:",
  ["Angel Falls : Venezuela", "Iguazu Falls : Argentina and Brazil", "Tugela Falls : Tanzania", "Kaieteur Falls : Suriname"],
  ["एंजेल जलप्रपात : वेनेज़ुएला", "इगुआज़ू जलप्रपात : अर्जेंटीना और ब्राज़ील", "तुगेला जलप्रपात : तंज़ानिया", "काइएतूर जलप्रपात : सूरीनाम"],
  1,
  "Only the first two pairs are correct. Angel Falls, in Venezuela's Canaima National Park, is the world's highest uninterrupted waterfall, at about 979 m. "
  "The Iguazu Falls, a chain of some 275 falls on the Iguazu river, lie on the border of Argentina and Brazil. "
  "Tugela Falls is in South Africa's Drakensberg range, in KwaZulu-Natal, and is often ranked second in height. Kaieteur Falls, on the Potaro river, is in Guyana and is known for its great single drop.",
  "केवल पहले दो युग्म सही हैं। वेनेज़ुएला के कनाइमा राष्ट्रीय उद्यान का एंजेल जलप्रपात लगभग 979 मीटर के साथ दुनिया का सबसे ऊँचा अविच्छिन्न जलप्रपात है। "
  "इगुआज़ू नदी पर लगभग 275 जलप्रपातों की शृंखला, इगुआज़ू जलप्रपात, अर्जेंटीना और ब्राज़ील की सीमा पर है। "
  "तुगेला जलप्रपात दक्षिण अफ़्रीका के क्वाज़ुलु-नटाल में ड्रैकेन्सबर्ग पर्वत में है और ऊँचाई में प्रायः दूसरे स्थान पर गिना जाता है। पोटारो नदी पर काइएतूर जलप्रपात गुयाना में है और अपनी विशाल एकल धार के लिए प्रसिद्ध है।",
  f"{ATLAS} -- South America and Africa.",
  "geo-waterfalls-countries-pairs")

M(WR, "hard", "The Alliance of Sahel States, whose members left the Economic Community of West African States (ECOWAS) in January 2025, comprises",
  "साहेल राज्यों का गठबंधन (Alliance of Sahel States), जिसके सदस्य जनवरी 2025 में पश्चिम अफ़्रीकी राज्यों के आर्थिक समुदाय (ECOWAS) से अलग हो गए, किन देशों से मिलकर बना है?",
  ["Mali, Burkina Faso and Niger", "Mali, Chad and Sudan", "Niger, Nigeria and Cameroon", "Burkina Faso, Senegal and Mauritania"],
  ["माली, बुर्किना फ़ासो और नाइजर", "माली, चाड और सूडान", "नाइजर, नाइजीरिया और कैमरून", "बुर्किना फ़ासो, सेनेगल और मॉरिटानिया"],
  0,
  "Mali, Burkina Faso and Niger, all under military governments, signed a mutual-defence charter in 2023 and formed a confederation in 2024; their exit from ECOWAS took effect in January 2025. "
  "The Sahel is the semi-arid belt between the Sahara to the north and the Sudanian savanna to the south, stretching from Senegal and Mauritania across to Sudan and Eritrea. "
  "Chad, Senegal and Mauritania are Sahel countries too but are not members of the Alliance, while Nigeria and Cameroon lie mostly south of the belt.",
  "सैन्य सरकारों वाले माली, बुर्किना फ़ासो और नाइजर ने 2023 में पारस्परिक रक्षा चार्टर पर हस्ताक्षर किए और 2024 में एक परिसंघ बनाया; ECOWAS से उनका अलग होना जनवरी 2025 से प्रभावी हुआ। "
  "साहेल उत्तर में सहारा और दक्षिण में सूडानी सवाना के बीच की अर्ध-शुष्क पट्टी है, जो सेनेगल और मॉरिटानिया से सूडान और इरिट्रिया तक फैली है। "
  "चाड, सेनेगल और मॉरिटानिया भी साहेल देश हैं पर गठबंधन के सदस्य नहीं हैं, जबकि नाइजीरिया और कैमरून अधिकतर इस पट्टी के दक्षिण में हैं।",
  f"{ATLAS} -- Africa; Economic Community of West African States.",
  "geo-alliance-of-sahel-states")

# ================================================================ CLIMATOLOGY (2)
S(CL, "medium", "Consider the following statements about the cooling and warming of moving air:",
  "गतिशील वायु के ठंडे और गर्म होने के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Air that rises cools because it expands under lower pressure, even though it loses no heat to its surroundings.",
   "Rising saturated air cools more slowly than rising dry air, because condensation releases latent heat.",
   "Sinking air warms as it is compressed, which is why areas under high pressure usually have clear skies."],
  ["ऊपर उठती वायु ठंडी होती है क्योंकि कम दाब में वह फैलती है, भले ही वह अपने परिवेश को कोई ऊष्मा न खोए।",
   "ऊपर उठती संतृप्त वायु शुष्क वायु की तुलना में धीरे ठंडी होती है, क्योंकि संघनन से गुप्त ऊष्मा मुक्त होती है।",
   "नीचे उतरती वायु संपीड़ित होने से गर्म होती है, इसी कारण उच्च दाब वाले क्षेत्रों में प्रायः आकाश साफ़ रहता है।"],
  C3, 2,
  "All three are correct. A rising parcel of air expands into lower pressure and does work on its surroundings, so its temperature falls even though no heat leaves it -- adiabatic cooling, at about 9.8 °C per km for dry air. "
  "Once the air is saturated, condensation releases latent heat, so the wet adiabatic rate is lower, roughly 4-7 °C per km depending on moisture. "
  "Sinking air does the reverse: compression warms it, clouds evaporate, and so anticyclones and the subtropical highs bring clear, dry weather.",
  "तीनों कथन सही हैं। ऊपर उठता वायु-पिंड कम दाब में फैलता है और अपने परिवेश पर कार्य करता है, इसलिए उसका तापमान गिरता है जबकि कोई ऊष्मा बाहर नहीं जाती; यह रुद्धोष्म (adiabatic) शीतलन है, जो शुष्क वायु के लिए लगभग 9.8 °C प्रति किमी होता है। "
  "वायु संतृप्त होने पर संघनन से गुप्त ऊष्मा मुक्त होती है, इसलिए आर्द्र रुद्धोष्म दर कम, नमी के अनुसार लगभग 4-7 °C प्रति किमी होती है। "
  "नीचे उतरती वायु में उल्टा होता है: संपीड़न से वह गर्म होती है, बादल वाष्पित हो जाते हैं, और इसलिए प्रतिचक्रवात तथा उपोष्ण उच्च दाब क्षेत्र साफ़ और शुष्क मौसम लाते हैं।",
  f"{NC11} -- Water in the Atmosphere; Atmospheric Circulation and Weather Systems.",
  "geo-adiabatic-dry-wet-subsidence")

A(CL, "medium",
  "Years of El Nino are often marked by a weaker than normal south-west monsoon in India.",
  "अल नीनो वाले वर्षों में भारत में दक्षिण-पश्चिम मानसून प्रायः सामान्य से कमज़ोर रहता है।",
  "During El Nino, the warm water and rising air of the Walker circulation shift eastward across the Pacific, leaving sinking air over the Indian region.",
  "अल नीनो के दौरान वॉकर परिसंचरण का गर्म जल और ऊपर उठती वायु प्रशांत महासागर में पूर्व की ओर खिसक जाते हैं, और भारतीय क्षेत्र के ऊपर नीचे उतरती वायु रह जाती है।",
  0,
  "Both statements are correct and Statement-II explains Statement-I. Normally the trade winds pile warm water in the western Pacific, where air rises, while cool water and sinking air lie off South America. "
  "In El Nino years the trades weaken, warm water spreads east and the rising limb of the Walker circulation moves toward the central and eastern Pacific; the compensating sinking air over the Indian Ocean and South Asia suppresses rain. "
  "The link is strong but not fixed -- 1997 brought a strong El Nino and a normal monsoon -- because conditions in the Indian Ocean and over Eurasia also shape the season.",
  "दोनों कथन सही हैं और कथन-II कथन-I की व्याख्या करता है। सामान्यतः व्यापारिक पवनें गर्म जल को पश्चिमी प्रशांत में इकट्ठा करती हैं, जहाँ वायु ऊपर उठती है, जबकि दक्षिण अमेरिका के पास ठंडा जल और नीचे उतरती वायु रहती है। "
  "अल नीनो वर्षों में व्यापारिक पवनें कमज़ोर पड़ती हैं, गर्म जल पूर्व की ओर फैलता है और वॉकर परिसंचरण की ऊपर उठती भुजा मध्य और पूर्वी प्रशांत की ओर चली जाती है; इसकी भरपाई में हिंद महासागर और दक्षिण एशिया के ऊपर नीचे उतरती वायु वर्षा को दबा देती है। "
  "यह संबंध मज़बूत है पर निश्चित नहीं; 1997 में प्रबल अल नीनो के बावजूद मानसून सामान्य रहा, क्योंकि हिंद महासागर और यूरेशिया की परिस्थितियाँ भी इस ऋतु को प्रभावित करती हैं।",
  f"{NC11} -- Atmospheric Circulation and Weather Systems; {IMD} -- monsoon and ENSO.",
  "geo-el-nino-walker-monsoon")

# ================================================================ RESOURCES (1)
S(RS, "medium", "Consider the following statements about mining in India:",
  "भारत में खनन के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Sukinda valley in Odisha holds the bulk of India's chromite reserves.",
   "Rampura Agucha in Rajasthan is one of the world's largest zinc-lead mines.",
   "The Kolar Gold Fields in Karnataka remain India's largest producer of gold."],
  ["ओडिशा की सुकिंडा घाटी में भारत के क्रोमाइट भंडार का अधिकांश भाग है।",
   "राजस्थान का रामपुरा अगुचा दुनिया की सबसे बड़ी जस्ता-सीसा खदानों में से एक है।",
   "कर्नाटक का कोलार स्वर्ण क्षेत्र आज भी भारत का सबसे बड़ा सोना उत्पादक है।"],
  C3, 1,
  "Statements 1 and 2 are correct. Sukinda, in Jajpur district, accounts for most of India's chromite, the ore of chromium; the heaps of mine waste have also made it one of the country's worst hot-spots of hexavalent chromium pollution. "
  "Rampura Agucha in Bhilwara district is a giant zinc-lead deposit mined by Hindustan Zinc. "
  "Statement 3 is wrong: the Kolar Gold Fields, among the deepest mines in the world, closed in 2001 when costs outran output; most of India's mined gold now comes from the Hutti mines, also in Karnataka.",
  "कथन 1 और 2 सही हैं। जाजपुर ज़िले का सुकिंडा भारत के अधिकांश क्रोमाइट, यानी क्रोमियम के अयस्क, का स्रोत है; खदानों के कचरे के ढेरों ने इसे हेक्सावैलेंट क्रोमियम प्रदूषण के देश के सबसे बुरे केंद्रों में भी बना दिया है। "
  "भीलवाड़ा ज़िले का रामपुरा अगुचा जस्ता-सीसा का विशाल भंडार है, जिसका खनन हिंदुस्तान ज़िंक करता है। "
  "कथन 3 गलत है: दुनिया की सबसे गहरी खदानों में गिना जाने वाला कोलार स्वर्ण क्षेत्र 2001 में बंद हो गया जब लागत उत्पादन से अधिक हो गई; अब भारत का अधिकांश खनित सोना कर्नाटक की ही हट्टी खदानों से आता है।",
  f"{IBM}; {NC12I} -- Mineral and Energy Resources.",
  "res-sukinda-rampura-kolar")

# ================================================================ TRANSPORT (1)
M(TH, "medium", "The Bogibeel bridge, India's longest rail-cum-road bridge, spans which river?",
  "भारत का सबसे लंबा रेल-सह-सड़क पुल, बोगीबील पुल, किस नदी पर बना है?",
  ["Brahmaputra, in Assam", "Ganga, in Bihar", "Godavari, in Andhra Pradesh", "Mahanadi, in Odisha"],
  ["ब्रह्मपुत्र, असम में", "गंगा, बिहार में", "गोदावरी, आंध्र प्रदेश में", "महानदी, ओडिशा में"],
  0,
  "Bogibeel, opened in 2018 near Dibrugarh, is about 4.9 km long and carries a double railway line below a three-lane road, linking the south bank of the Brahmaputra with Dhemaji and the border areas of Arunachal Pradesh on the north bank; its strategic value lies in faster movement toward the eastern frontier. "
  "The Digha-Sonpur bridge over the Ganga at Patna and the Godavari bridges at Rajahmundry are other long rail-cum-road bridges.",
  "2018 में डिब्रूगढ़ के पास खुला बोगीबील पुल लगभग 4.9 किमी लंबा है और तीन लेन की सड़क के नीचे दोहरी रेल लाइन ले जाता है; यह ब्रह्मपुत्र के दक्षिणी तट को उत्तरी तट पर धेमाजी और अरुणाचल प्रदेश के सीमावर्ती क्षेत्रों से जोड़ता है, और इसका सामरिक महत्व पूर्वी सीमा की ओर तेज़ आवाजाही में है। "
  "पटना में गंगा पर दीघा-सोनपुर पुल और राजमुंदरी में गोदावरी के पुल भी लंबे रेल-सह-सड़क पुल हैं।",
  "Ministry of Railways -- Bogibeel rail-cum-road bridge; Northeast Frontier Railway.",
  "tr-bogibeel-brahmaputra")

# ================================================================ INDIAN RIVERS (1)
S(RV, "hard", "Consider the following statements about dams and the rivers they are built on:",
  "बाँधों और उन नदियों के बारे में निम्नलिखित कथनों पर विचार कीजिए जिन पर वे बने हैं:",
  ["The Hirakud dam is built across the Mahanadi.",
   "The Almatti dam is built across the Godavari.",
   "The Ukai dam is built across the Narmada."],
  ["हीराकुड बाँध महानदी पर बना है।",
   "अलमट्टी बाँध गोदावरी पर बना है।",
   "उकाई बाँध नर्मदा पर बना है।"],
  C3, 0,
  "Only statement 1 is correct. Hirakud, near Sambalpur in Odisha (completed in 1957), is one of the longest earthen dams in the world, built to control the Mahanadi's floods and irrigate its delta. "
  "Statement 2 is wrong: Almatti, in the Vijayapura district of Karnataka, is on the Krishna and forms the main reservoir of the Upper Krishna Project. "
  "Statement 3 is wrong: Ukai, in Gujarat, is on the Tapi, upstream of Surat.",
  "केवल कथन 1 सही है। ओडिशा में संबलपुर के पास हीराकुड (1957 में पूर्ण) दुनिया के सबसे लंबे मिट्टी के बाँधों में से है, जो महानदी की बाढ़ रोकने और उसके डेल्टा की सिंचाई के लिए बना। "
  "कथन 2 गलत है: कर्नाटक के विजयपुरा ज़िले का अलमट्टी बाँध कृष्णा पर है और ऊपरी कृष्णा परियोजना का मुख्य जलाशय बनाता है। "
  "कथन 3 गलत है: गुजरात का उकाई बाँध सूरत से ऊपर की ओर तापी पर है।",
  f"{NC11I} -- Drainage System; Central Water Commission -- National Register of Large Dams.",
  "irv-dams-hirakud-almatti-ukai")

# ================================================================ GEOMORPHOLOGY (1)
A(GM, "easy",
  "In hot deserts, the outer layers of exposed rocks often peel off in curved sheets.",
  "गर्म मरुस्थलों में खुली चट्टानों की बाहरी परतें प्रायः घुमावदार परतों के रूप में उतर जाती हैं।",
  "Hot deserts receive very little rainfall in a year.",
  "गर्म मरुस्थलों में वर्ष भर में बहुत कम वर्षा होती है।",
  1,
  "Both statements are correct, but Statement-II does not explain Statement-I. The peeling, called exfoliation or onion-skin weathering, comes from the wide gap between day and night temperatures: the outer shell of a rock heats and expands by day and cools and contracts by night more than its interior, until it loosens and flakes away; the release of pressure on rock exposed by erosion helps too. "
  "Low rainfall is simply another feature of deserts, not the cause of the peeling.",
  "दोनों कथन सही हैं, पर कथन-II कथन-I की व्याख्या नहीं करता। इस परत-उतरने को अपशल्कन (exfoliation) या प्याज़-छिलका अपक्षय कहते हैं; यह दिन और रात के तापमान के बड़े अंतर से होता है: चट्टान का बाहरी खोल दिन में गर्म होकर फैलता है और रात में भीतरी भाग से अधिक ठंडा होकर सिकुड़ता है, जब तक वह ढीला होकर उतर न जाए; अपरदन से खुली चट्टान पर दाब कम होने से भी यह होता है। "
  "कम वर्षा मरुस्थल की एक अन्य विशेषता मात्र है, परत उतरने का कारण नहीं।",
  f"{NC11} -- Geomorphic Processes.",
  "geo-exfoliation-diurnal-range")

if __name__ == "__main__":
    write("gs_l2_t21_geography.sql")
