# -*- coding: utf-8 -*-
"""Level 2 · Test 13 (Geography 2: India -- Physiography, Climate, Rivers) -- depth audit of 2026-10-04, part A:
Indian Physiography, Climate & Regions (docs/upsc-question-design-standard.md §6). Part B
(upg_l2_t13_igeo_b.py) has Indian Rivers, Lakes & Wetlands and the tags for the kept rows.

Before the audit the test had analytic 19, precision 24, recall 60. Part A rewrites 15 recall rows in place
with the same concept id, type and difficulty:
  - analytic: how the karewas and the valley lake came about, what the Palghat gap does, why the Shiwaliks
    erode, how canal irrigation makes saline soil, why Thar streams die in the sand, why ships avoid the
    Palk Strait, why the plains hold so many people, where the tropics fall, a State identified from its
    features, and why Gujarat's coast is so long;
  - precision: near-miss versions of the local storms, the Peninsula's hills, the coasts, the passes and the
    hill ranges.
Leaks avoided while drafting:
  - the Aravallis lying parallel to the monsoon (the Aravalli AR's Statement II);
  - the Coromandel coast's position (the Coromandel AR's stem names Tamil Nadu);
  - Lakshadweep's coral origin (answers the islands row's statement 3);
  - basalt and black soil in the plateau pairs (the black-soil row's statement 1), so those pairs were left;
  - evaporation concentrating salts (the Ladakh-lakes AR's Statement II)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write_updates, CODE
from polity_common import C3, C4, T2

d.SUBJECT = "Geography"
d.REQUIRE_CRAFT = True
PH = "Indian Physiography, Climate & Regions"
NI = "NCERT Class XI, India: Physical Environment"
NC9 = "NCERT Class IX, Contemporary India I"

# ================================================================ MCQs (3)
M(PH, "easy", "Large ships sailing between India's west and east coasts go round Sri Lanka instead of passing through the Palk Strait. The main reason is that:",
  "भारत के पश्चिमी और पूर्वी तटों के बीच चलने वाले बड़े जहाज़ पाक जलडमरूमध्य से गुज़रने के बजाय श्रीलंका का चक्कर लगाते हैं। इसका मुख्य कारण यह है कि:",
  ["the strait and the shoals of Adam's Bridge are too shallow for them",
   "the strait is blocked by drifting sea ice for several months each winter",
   "Sri Lanka charges a very heavy toll on every ship that uses the strait",
   "strong cold ocean currents in the strait make it unsafe to cross at all"],
  ["जलडमरूमध्य और एडम्स ब्रिज के उथले टीले उनके लिए बहुत उथले हैं",
   "हर सर्दी में कई महीनों तक जलडमरूमध्य बहती समुद्री बर्फ़ से अवरुद्ध रहता है",
   "श्रीलंका जलडमरूमध्य का उपयोग करने वाले हर जहाज़ से बहुत भारी शुल्क लेता है",
   "जलडमरूमध्य की तेज़ ठंडी महासागरीय धाराएँ उसे पार करना बिल्कुल असुरक्षित बना देती हैं"],
  0,
  "The Palk Strait and the Gulf of Mannar separate Tamil Nadu from Sri Lanka, but the chain of limestone shoals called Adam's Bridge (Rama Setu), running from Rameswaram to Mannar island, and the shallow strait itself leave only a few metres of water -- too little for large ships. They must sail round Sri Lanka, adding hundreds of kilometres to the voyage, which is why the Sethusamudram ship canal was proposed. "
  "The strait, in the tropics, never freezes, and no toll is levied on it.",
  "पाक जलडमरूमध्य और मन्नार की खाड़ी तमिलनाडु को श्रीलंका से अलग करते हैं, पर रामेश्वरम से मन्नार द्वीप तक फैली चूना-पत्थर के टीलों की शृंखला एडम्स ब्रिज (राम सेतु) और स्वयं उथला जलडमरूमध्य केवल कुछ मीटर पानी छोड़ते हैं, जो बड़े जहाज़ों के लिए बहुत कम है। उन्हें श्रीलंका का चक्कर लगाना पड़ता है, जिससे यात्रा सैकड़ों किलोमीटर लंबी हो जाती है, इसीलिए सेतुसमुद्रम जहाज़-नहर प्रस्तावित की गई। "
  "उष्णकटिबंध में स्थित यह जलडमरूमध्य कभी नहीं जमता, और इस पर कोई शुल्क नहीं लगता।",
  NC9, "igeo-palk-strait-easy", craft="linkage")

M(PH, "easy", "A State covers about a tenth of India's area and shares a long border with Pakistan, but has no coastline. The State is:",
  "एक राज्य भारत के लगभग दसवें भाग में फैला है और पाकिस्तान के साथ लंबी सीमा रखता है, पर उसकी कोई तटरेखा नहीं है। वह राज्य है:",
  ["Rajasthan", "Gujarat", "Madhya Pradesh", "Punjab"],
  ["राजस्थान", "गुजरात", "मध्य प्रदेश", "पंजाब"],
  0,
  "Rajasthan, at about 3.42 lakh sq km, is India's largest State, about a tenth of the country's area; its border with Pakistan runs for more than 1,000 km, and the Thar covers most of its western part. "
  "Gujarat also borders Pakistan, along the Rann of Kachchh, but it has the longest coastline of any State and covers only about 6 per cent of India; Madhya Pradesh, the second-largest State, has no international border; and Punjab is small and lies on the fertile plain of the Indus tributaries.",
  "लगभग 3.42 लाख वर्ग किमी वाला राजस्थान भारत का सबसे बड़ा राज्य है, देश के क्षेत्रफल का लगभग दसवाँ भाग; पाकिस्तान के साथ इसकी सीमा 1,000 किमी से अधिक है, और थार इसके पश्चिमी भाग के अधिकांश हिस्से में फैला है। "
  "गुजरात भी कच्छ के रण के साथ-साथ पाकिस्तान से लगता है, पर उसकी तटरेखा किसी भी राज्य से लंबी है और वह भारत के केवल लगभग 6 प्रतिशत भाग में है; दूसरा सबसे बड़ा राज्य मध्य प्रदेश किसी अंतरराष्ट्रीय सीमा से नहीं लगता; और पंजाब छोटा है तथा सिंधु की सहायक नदियों के उपजाऊ मैदान पर है।",
  NC9, "igeo-largest-state-rajasthan-easy", craft="application")

M(PH, "medium", "Gujarat has the longest coastline of any Indian State. The main reason is that:",
  "किसी भी भारतीय राज्य में सबसे लंबी तटरेखा गुजरात की है। इसका मुख्य कारण यह है कि:",
  ["its coast is deeply indented by the Gulfs of Kachchh and Khambhat around Kathiawar",
   "it includes far more inhabited offshore islands than any other coastal State of India",
   "it faces both the Arabian Sea and the Bay of Bengal along different stretches of its shore",
   "the great deltas of its rivers push its shoreline far out into the sea every year"],
  ["इसका तट काठियावाड़ के दोनों ओर कच्छ और खंभात की खाड़ियों से गहराई तक कटा-फटा है",
   "इसमें भारत के किसी भी अन्य तटीय राज्य से कहीं अधिक बसे हुए अपतटीय द्वीप हैं",
   "इसके तट के अलग-अलग भाग अरब सागर और बंगाल की खाड़ी दोनों की ओर हैं",
   "इसकी नदियों के बड़े डेल्टा हर साल इसकी तटरेखा को समुद्र में दूर तक धकेलते हैं"],
  0,
  "Gujarat's coast, about 2,340 km by the recent re-measurement of India's coastline and roughly a fifth of the total, is long because it is so indented: the Gulf of Kachchh and the Gulf of Khambhat cut deep into the land on either side of the Kathiawar peninsula, so the shoreline doubles back on itself, far ahead of any other State. "
  "Gujarat faces only the Arabian Sea, and it has few inhabited islands; its coast is lengthened by gulfs, not by deltas.",
  "भारत की तटरेखा के हाल के पुनर्मापन के अनुसार लगभग 2,340 किमी और कुल का लगभग पाँचवाँ भाग गुजरात का तट इसलिए लंबा है कि वह बहुत कटा-फटा है: कच्छ की खाड़ी और खंभात की खाड़ी काठियावाड़ प्रायद्वीप के दोनों ओर भूमि में गहराई तक घुसती हैं, इसलिए तटरेखा मुड़-मुड़कर लौटती है, और किसी भी अन्य राज्य से बहुत आगे है। "
  "गुजरात केवल अरब सागर की ओर है, और उसके बसे हुए द्वीप कम हैं; उसका तट खाड़ियों से लंबा हुआ है, डेल्टाओं से नहीं।",
  NC9, "igeo-longest-coastline-gujarat", craft="linkage")

# ================================================================ pairs (3)
P(PH, "medium", "Consider the following pairs of coastal stretches and the States along which they lie:",
  "तटीय भागों और उन राज्यों के निम्नलिखित युग्मों पर विचार कीजिए जिनके साथ-साथ वे स्थित हैं:",
  ["Konkan coast : Karnataka", "Kanara coast : Kerala", "Malabar coast : Kerala", "Northern Circars : Andhra Pradesh and Odisha"],
  ["कोंकण तट : कर्नाटक", "कनारा तट : केरल", "मालाबार तट : केरल", "उत्तरी सरकार : आंध्र प्रदेश और ओडिशा"],
  1,
  "Only pairs 3 and 4 are correct. Pairs 1 and 2 shift the western coast one State south: from north to south it runs as the Konkan coast of Maharashtra and Goa (Mumbai to Goa), the Kanara or Karnataka coast, and the Malabar coast of Kerala. On the east, the Northern Circars are the northern part of the eastern coastal plain, along Odisha and Andhra Pradesh, and the Coromandel coast lies to the south.",
  "केवल युग्म 3 और 4 सही हैं। युग्म 1 और 2 पश्चिमी तट को एक राज्य दक्षिण की ओर खिसका देते हैं: उत्तर से दक्षिण यह महाराष्ट्र और गोवा का कोंकण तट (मुंबई से गोवा), कनारा या कर्नाटक तट, और केरल का मालाबार तट है। पूर्व में उत्तरी सरकार ओडिशा और आंध्र प्रदेश के साथ-साथ पूर्वी तटीय मैदान का उत्तरी भाग है, और कोरोमंडल तट उसके दक्षिण में है।",
  NI, "igeo-coasts-states-pairs", craft="precision")

P(PH, "medium", "Consider the following pairs of Himalayan passes and the States/UTs in which they lie:",
  "हिमालयी दर्रों और उन राज्यों/केंद्रशासित प्रदेशों के निम्नलिखित युग्मों पर विचार कीजिए जिनमें वे स्थित हैं:",
  ["Shipki La : Himachal Pradesh", "Jelep La : Sikkim", "Bomdi La : Arunachal Pradesh", "Lipulekh : Sikkim"],
  ["शिपकी ला : हिमाचल प्रदेश", "जेलेप ला : सिक्किम", "बोमडी ला : अरुणाचल प्रदेश", "लिपुलेख : सिक्किम"],
  2,
  "Three pairs are correct. Shipki La, where the Satluj enters India, links Himachal Pradesh with Tibet; Jelep La, like the nearby Nathu La, links Sikkim with the Chumbi valley; and Bomdi La, on the road to Tawang, is in western Arunachal Pradesh. "
  "Pair 4 is the near-miss: both Lipulekh and Nathu La are used by the Kailash-Mansarovar pilgrimage, but Lipulekh lies in Pithoragarh district of Uttarakhand, at the meeting point of India, Nepal and Tibet.",
  "तीन युग्म सही हैं। शिपकी ला, जहाँ से सतलुज भारत में आती है, हिमाचल प्रदेश को तिब्बत से जोड़ता है; पास के नाथू ला की तरह जेलेप ला सिक्किम को चुम्बी घाटी से जोड़ता है; और तवांग के रास्ते पर बोमडी ला पश्चिमी अरुणाचल प्रदेश में है। "
  "युग्म 4 निकट-भ्रम है: लिपुलेख और नाथू ला दोनों कैलाश-मानसरोवर यात्रा के मार्ग हैं, पर लिपुलेख उत्तराखंड के पिथौरागढ़ ज़िले में, भारत, नेपाल और तिब्बत के मिलन-बिंदु पर है।",
  NI, "igeo-himalayan-passes-pairs", craft="precision")

P(PH, "hard", "Consider the following pairs of hills and the ranges or plateaus to which they belong:",
  "पहाड़ियों और उन श्रेणियों या पठारों के निम्नलिखित युग्मों पर विचार कीजिए जिनसे वे संबंधित हैं:",
  ["Nallamala hills : Eastern Ghats", "Mikir hills : Meghalaya plateau, as an outlier", "Shevaroy hills : Western Ghats", "Javadi hills : Eastern Ghats"],
  ["नल्लामला पहाड़ियाँ : पूर्वी घाट", "मिकिर पहाड़ियाँ : मेघालय पठार, एक बाह्य भाग के रूप में", "शेवरॉय पहाड़ियाँ : पश्चिमी घाट", "जवादी पहाड़ियाँ : पूर्वी घाट"],
  2,
  "Three pairs are correct. The Nallamala hills of Andhra Pradesh, cut through by the Krishna at Srisailam, are part of the Eastern Ghats, as are the Javadi hills of northern Tamil Nadu; the Mikir (Karbi Anglong) hills of Assam are an outlier of the Meghalaya plateau, which is itself a detached block of the Peninsula. "
  "Pair 3 is the near-miss: the Shevaroy hills, with the hill station of Yercaud near Salem, belong to the Eastern Ghats of Tamil Nadu, not the Western Ghats.",
  "तीन युग्म सही हैं। आंध्र प्रदेश की नल्लामला पहाड़ियाँ, जिन्हें श्रीशैलम पर कृष्णा काटती है, पूर्वी घाट का भाग हैं, और उत्तरी तमिलनाडु की जवादी पहाड़ियाँ भी; असम की मिकिर (कार्बी आंगलोंग) पहाड़ियाँ मेघालय पठार का बाह्य भाग हैं, जो स्वयं प्रायद्वीप का अलग हुआ खंड है। "
  "युग्म 3 निकट-भ्रम है: सलेम के पास यरकॉड पर्वतीय स्थल वाली शेवरॉय पहाड़ियाँ पश्चिमी घाट की नहीं, तमिलनाडु के पूर्वी घाट की हैं।",
  NI, "igeo-hills-states-pairs", craft="precision")

# ================================================================ statements (9)
S(PH, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Deccan plateau is roughly triangular in shape.",
   "The Northern Plains are among the most densely settled regions of the world, because their deep alluvial soil is fertile and the level land is easy to irrigate."],
  ["दक्कन का पठार मोटे तौर पर त्रिभुजाकार है।",
   "उत्तरी मैदान संसार के सबसे घने बसे क्षेत्रों में हैं, क्योंकि उनकी गहरी जलोढ़ मिट्टी उपजाऊ है और समतल भूमि की सिंचाई आसान है।"],
  T2, 2,
  "Both statements are correct. The Deccan lies south of the Narmada, bounded by the Satpura, the Mahadeo, the Kaimur and the Maikal hills in the north and by the Western and Eastern Ghats on its sides, so it narrows to a point in the south. "
  "The Northern Plains, built of alluvium laid down by the Indus, the Ganga and the Brahmaputra systems, are flat, fertile and well watered, so they have supported intensive farming and large populations for thousands of years.",
  "दोनों कथन सही हैं। दक्कन नर्मदा के दक्षिण में है, उत्तर में सतपुड़ा, महादेव, कैमूर और मैकाल पहाड़ियों से और किनारों पर पश्चिमी और पूर्वी घाट से घिरा है, इसलिए यह दक्षिण में एक नोक तक सँकरा हो जाता है। "
  "सिंधु, गंगा और ब्रह्मपुत्र तंत्रों द्वारा जमा जलोढ़ से बने उत्तरी मैदान समतल, उपजाऊ और अच्छी तरह सिंचित हैं, इसलिए वे हज़ारों वर्षों से गहन खेती और बड़ी आबादियों को सहारा देते आए हैं।",
  NC9, "igeo-deccan-shape-northern-plains-easy", craft="linkage")

S(PH, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["India lies partly in the Southern Hemisphere, through its southernmost islands.",
   "Since the Tropic of Cancer passes roughly through the middle of India, the country's southern half lies within the tropics."],
  ["अपने सबसे दक्षिणी द्वीपों के कारण भारत आंशिक रूप से दक्षिणी गोलार्ध में है।",
   "चूँकि कर्क रेखा मोटे तौर पर भारत के बीच से गुज़रती है, इसलिए देश का दक्षिणी आधा भाग उष्णकटिबंध में है।"],
  T2, 1,
  "Only statement 2 is correct. India's mainland extends from about 8°4' N to 37°6' N, and the Tropic of Cancer (about 23.5° N) runs almost through the middle, across eight States from Gujarat to Mizoram; so the southern half lies in the tropical zone and the northern half in the subtropical and warm temperate belt. "
  "Statement 1 is wrong: even India's southernmost point, Indira Point on Great Nicobar, lies at about 6°45' N, so the whole country is in the Northern Hemisphere.",
  "केवल कथन 2 सही है। भारत की मुख्य भूमि लगभग 8°4' उत्तर से 37°6' उत्तर तक फैली है, और कर्क रेखा (लगभग 23.5° उत्तर) गुजरात से मिज़ोरम तक आठ राज्यों से होकर लगभग बीच से गुज़रती है; इसलिए दक्षिणी आधा भाग उष्णकटिबंधीय क्षेत्र में और उत्तरी आधा उपोष्ण और गर्म शीतोष्ण पट्टी में है। "
  "कथन 1 गलत है: भारत का सबसे दक्षिणी बिंदु, ग्रेट निकोबार का इंदिरा पॉइंट, भी लगभग 6°45' उत्तर पर है, इसलिए पूरा देश उत्तरी गोलार्ध में है।",
  NC9, "igeo-hemisphere-size-easy", craft="inference")

S(PH, "hard", "Consider the following statements about the Kashmir Himalaya:",
  "कश्मीर हिमालय के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Karewas, the thick lake deposits of the Kashmir valley, are used for growing saffron.",
   "The Kashmir valley was once occupied by a large lake, which drained away when an outlet was cut through the mountains near Baramulla.",
   "The Pir Panjal is part of the Greater Himalaya."],
  ["करेवा, कश्मीर घाटी के मोटे झील-निक्षेप, केसर उगाने के काम आते हैं।",
   "कश्मीर घाटी कभी एक बड़ी झील से भरी थी, जो बारामूला के पास पर्वतों में निकास कटने पर बह गई।",
   "पीर पंजाल महान हिमालय का भाग है।"],
  C3, 1,
  "Statements 1 and 2 are correct, and they are linked: the valley held a great lake in the Pleistocene, and the clay, sand and silt laid down in it form the flat-topped terraces called karewas, on which saffron (zafran) is grown around Pampore, along with almonds and walnuts. When the Jhelum cut down through the gorge near Baramulla, the lake drained, leaving the valley floor and lakes such as the Wular. "
  "Statement 3 is wrong: the Pir Panjal, the valley's southern wall, is the main range of the Lesser Himalaya (Himachal) in Kashmir; the Great Himalaya lies to the north-east.",
  "कथन 1 और 2 सही हैं, और वे जुड़े हैं: प्लीस्टोसीन में घाटी में एक बड़ी झील थी, और उसमें जमी मिट्टी, रेत और गाद सपाट शिखर वाली उन वेदिकाओं को बनाती है जिन्हें करेवा कहते हैं, जिन पर पांपोर के आसपास केसर (ज़ाफ़रान) के साथ बादाम और अख़रोट उगाए जाते हैं। जब झेलम ने बारामूला के पास गॉर्ज को काटकर गहरा किया, तो झील बह गई, और घाटी का तल तथा वुलर जैसी झीलें बचीं। "
  "कथन 3 गलत है: घाटी की दक्षिणी दीवार पीर पंजाल कश्मीर में लघु हिमालय (हिमाचल) की मुख्य श्रेणी है; महान हिमालय उत्तर-पूर्व में है।",
  NI, "igeo-kashmir-karewas-pir-panjal", craft="linkage")

S(PH, "hard", "Consider the following statements about the hills of southern India:",
  "दक्षिण भारत की पहाड़ियों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Nilgiri hills are the meeting point of the Western and the Eastern Ghats.",
   "The Palghat (Palakkad) gap, the widest break in the Western Ghats, lets moist winds from the Arabian Sea reach the Coimbatore region and carries the main road and railway between Kerala and Tamil Nadu.",
   "Doddabetta lies in the Cardamom hills."],
  ["नीलगिरि पहाड़ियाँ पश्चिमी और पूर्वी घाट का मिलन-बिंदु हैं।",
   "पश्चिमी घाट का सबसे चौड़ा अंतराल, पालघाट (पालक्काड) दर्रा, अरब सागर की नम हवाओं को कोयंबटूर क्षेत्र तक पहुँचने देता है और केरल तथा तमिलनाडु के बीच मुख्य सड़क और रेलमार्ग ले जाता है।",
   "डोडाबेट्टा इलायची पहाड़ियों में है।"],
  C3, 1,
  "Statements 1 and 2 are correct. The Eastern Ghats curve south-west to join the Western Ghats in the Nilgiris. South of them, the Palghat gap, some 30-40 km wide, opens the otherwise unbroken wall of the Ghats: through it the south-west monsoon winds reach Palakkad and Coimbatore, which is why the Coimbatore plateau is milder and moister than the plains further east, and through it run the main road and railway linking Kerala with Tamil Nadu. "
  "Statement 3 is wrong: Doddabetta (about 2,637 m), above Udhagamandalam, is the highest peak of the Nilgiris; the Cardamom hills lie much further south, on the Kerala-Tamil Nadu border.",
  "कथन 1 और 2 सही हैं। पूर्वी घाट दक्षिण-पश्चिम की ओर मुड़कर नीलगिरि में पश्चिमी घाट से मिलते हैं। उनके दक्षिण में लगभग 30-40 किमी चौड़ा पालघाट दर्रा घाट की अन्यथा अखंड दीवार को खोलता है: इससे दक्षिण-पश्चिम मानसून की हवाएँ पालक्काड और कोयंबटूर तक पहुँचती हैं, इसीलिए कोयंबटूर पठार पूर्व के मैदानों से अधिक सौम्य और नम है, और इसी से केरल को तमिलनाडु से जोड़ने वाली मुख्य सड़क और रेलमार्ग गुज़रते हैं। "
  "कथन 3 गलत है: उदगमंडलम के ऊपर डोडाबेट्टा (लगभग 2,637 मीटर) नीलगिरि की सबसे ऊँची चोटी है; इलायची पहाड़ियाँ बहुत दक्षिण में, केरल-तमिलनाडु सीमा पर हैं।",
  NI, "igeo-nilgiris-doddabetta-palghat", craft="linkage")

S(PH, "medium", "Consider the following statements about the Himalaya:",
  "हिमालय के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Shiwaliks, the youngest and outermost range, are built of loose river sediments, which makes them prone to landslides and gully erosion.",
   "The Greater Himalaya (Himadri) has a core of granite and is the most continuous range.",
   "Duns such as Dehradun are longitudinal valleys lying between the Lesser Himalaya and the Shiwaliks."],
  ["सबसे नई और सबसे बाहरी श्रेणी शिवालिक नदियों के ढीले अवसादों से बनी है, जिससे उसमें भूस्खलन और अवनालिका अपरदन की प्रवृत्ति है।",
   "महान हिमालय (हिमाद्रि) का क्रोड ग्रेनाइट का है और यह सबसे अधिक निरंतर श्रेणी है।",
   "देहरादून जैसे दून लघु हिमालय और शिवालिक के बीच स्थित अनुदैर्ध्य घाटियाँ हैं।"],
  C3, 2,
  "All three are correct. The Shiwaliks, about 900-1,100 m high, were raised from gravels and clays that rivers had washed down from the main ranges; poorly consolidated, and in many parts stripped of forest, they erode fast, as the seasonal 'cho' torrents of the Punjab and Himachal Shiwaliks show. "
  "The Himadri, averaging about 6,000 m, holds the loftiest peaks and is snowbound throughout the year. Between the Lesser Himalaya and the Shiwaliks lie flat-floored longitudinal valleys called duns -- Dehradun, Kotli Dun and Patli Dun among them.",
  "तीनों कथन सही हैं। लगभग 900-1,100 मीटर ऊँचे शिवालिक उन बजरी और मिट्टी से उठे हैं जिन्हें नदियाँ मुख्य श्रेणियों से बहाकर लाई थीं; कम सघन और कई भागों में वनविहीन होने से वे तेज़ी से घिसते हैं, जैसा पंजाब और हिमाचल के शिवालिक की मौसमी 'चो' धाराएँ दिखाती हैं। "
  "औसतन लगभग 6,000 मीटर ऊँचे हिमाद्रि में सबसे ऊँची चोटियाँ हैं और यह साल भर हिमाच्छादित रहता है। लघु हिमालय और शिवालिक के बीच सपाट तल वाली अनुदैर्ध्य घाटियाँ हैं जिन्हें दून कहते हैं, जैसे देहरादून, कोटली दून और पतली दून।",
  NI, "igeo-himalaya-ranges-duns", craft="linkage")

S(PH, "medium", "Consider the following statements about local weather phenomena in India:",
  "भारत की स्थानीय मौसमी घटनाओं के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Pre-monsoon showers in Kerala and coastal Karnataka are known as mango showers.",
   "Kalbaisakhi (nor'westers) are violent evening thunderstorms in West Bengal and Assam.",
   "The 'loo' is a hot, dry wind that blows over the northern plains in summer.",
   "'Cherry blossoms' are pre-monsoon showers that help the apple orchards of Himachal Pradesh to flower."],
  ["केरल और तटीय कर्नाटक की मानसून-पूर्व बौछारें आम्र-वर्षा (मैंगो शावर) कहलाती हैं।",
   "कालबैसाखी (नॉर'वेस्टर) पश्चिम बंगाल और असम के प्रचंड सांध्य गरज-तूफ़ान हैं।",
   "'लू' ग्रीष्म में उत्तरी मैदानों पर चलने वाली गर्म, शुष्क हवा है।",
   "'चेरी ब्लॉसम' वे मानसून-पूर्व बौछारें हैं जो हिमाचल प्रदेश के सेब के बाग़ों को फूलने में मदद करती हैं।"],
  C4, 2,
  "Statements 1, 2 and 3 are correct. Mango showers help the mangoes ripen; kalbaisakhi, the 'calamity of the month of Baisakh', bring rain that helps the tea, jute and rice of Assam and Bengal; and the loo can push temperatures to 45-50 °C and cause heatstroke. "
  "Statement 4 is the near-miss: 'cherry blossoms', or blossom showers, are the pre-monsoon showers that make the coffee plants of Karnataka and Kerala flower -- coffee, not apples.",
  "कथन 1, 2 और 3 सही हैं। आम्र-वर्षा आमों को पकने में मदद करती है; 'बैसाख की विपदा' कालबैसाखी ऐसी वर्षा लाती है जो असम और बंगाल की चाय, जूट और धान के लिए उपयोगी है; और लू तापमान को 45-50 °C तक पहुँचाकर लू लगने का कारण बन सकती है। "
  "कथन 4 निकट-भ्रम है: 'चेरी ब्लॉसम' या फूलों वाली बौछारें वे मानसून-पूर्व बौछारें हैं जो कर्नाटक और केरल के कॉफ़ी के पौधों को फूलने देती हैं, सेब को नहीं, कॉफ़ी को।",
  NI, "igeo-local-storms-mango-kalbaisakhi-loo", craft="precision")

S(PH, "medium", "Consider the following statements about the Peninsular plateau:",
  "प्रायद्वीपीय पठार के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Rajmahal hills mark the north-eastern edge of the Peninsular plateau.",
   "The Kaimur hills are an eastern extension of the Vindhyan range.",
   "The Mahadeo hills are part of the Vindhyan range."],
  ["राजमहल पहाड़ियाँ प्रायद्वीपीय पठार के उत्तर-पूर्वी किनारे को चिह्नित करती हैं।",
   "कैमूर पहाड़ियाँ विंध्य श्रेणी का पूर्वी विस्तार हैं।",
   "महादेव पहाड़ियाँ विंध्य श्रेणी का भाग हैं।"],
  C3, 1,
  "Statements 1 and 2 are correct. The northern boundary of the Peninsular block runs from Kachchh along the Aravallis and then roughly parallel to the Yamuna and the Ganga as far as the Rajmahal hills in Jharkhand. The Vindhyas, north of the Narmada, continue east as the Kaimur hills. "
  "Statement 3 is the near-miss: the Mahadeo hills, with Pachmarhi and Dhupgarh, the highest point of central India, belong to the Satpura range south of the Narmada, as do the Maikal hills at its eastern end.",
  "कथन 1 और 2 सही हैं। प्रायद्वीपीय खंड की उत्तरी सीमा कच्छ से अरावली के साथ-साथ और फिर मोटे तौर पर यमुना और गंगा के समानांतर झारखंड की राजमहल पहाड़ियों तक जाती है। नर्मदा के उत्तर में विंध्य पूर्व की ओर कैमूर पहाड़ियों के रूप में जारी रहते हैं। "
  "कथन 3 निकट-भ्रम है: पचमढ़ी और मध्य भारत के सबसे ऊँचे बिंदु धूपगढ़ वाली महादेव पहाड़ियाँ नर्मदा के दक्षिण की सतपुड़ा श्रेणी की हैं, जैसे उसके पूर्वी छोर की मैकाल पहाड़ियाँ।",
  NI, "igeo-peninsula-rajmahal-kaimur-mahadeo", craft="precision")

S(PH, "medium", "Consider the following statements about the soils of India:",
  "भारत की मिट्टियों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Red soils are red because they are rich in humus.",
   "In canal-irrigated tracts with poor drainage, a rising water table brings salts up to the surface, turning good land into saline soil.",
   "Alluvial soils are generally poor in potash."],
  ["लाल मिट्टियाँ इसलिए लाल हैं कि उनमें ह्यूमस प्रचुर होता है।",
   "जिन नहर-सिंचित क्षेत्रों में जल-निकास ख़राब है, वहाँ ऊपर उठता भौम-जल स्तर लवणों को सतह तक ले आता है, जिससे अच्छी भूमि लवणीय मिट्टी बन जाती है।",
   "जलोढ़ मिट्टियों में सामान्यतः पोटाश की कमी होती है।"],
  C3, 0,
  "Only statement 2 is correct. Where canals bring in more water than drains take away, as in parts of Punjab, Haryana and western Uttar Pradesh, the water table rises and carries dissolved salts up through the soil; as the water dries off in the hot months, a white crust of sodium, calcium and magnesium salts is left behind -- the reh, kallar or usar soils, reclaimed with gypsum and better drainage. "
  "Statement 1 is wrong: red soils owe their colour to iron oxides spread through crystalline and metamorphic rocks, and they are poor in humus. Statement 3 is wrong: alluvial soils are generally rich in potash and poor in phosphorus.",
  "केवल कथन 2 सही है। जहाँ नहरें जितना पानी लाती हैं उतना नालियाँ नहीं निकालतीं, जैसे पंजाब, हरियाणा और पश्चिमी उत्तर प्रदेश के कुछ भागों में, वहाँ भौम-जल स्तर उठता है और घुले लवणों को मिट्टी में ऊपर ले आता है; गर्म महीनों में पानी सूखने पर सोडियम, कैल्शियम और मैग्नीशियम लवणों की सफ़ेद परत बच जाती है, जो रेह, कल्लर या ऊसर मिट्टी है, जिसे जिप्सम और बेहतर जल-निकास से सुधारा जाता है। "
  "कथन 1 गलत है: लाल मिट्टियों का रंग क्रिस्टलीय और कायांतरित चट्टानों में फैले लौह ऑक्साइडों से है, और उनमें ह्यूमस कम होता है। कथन 3 गलत है: जलोढ़ मिट्टियाँ सामान्यतः पोटाश में समृद्ध और फ़ॉस्फ़ोरस में कमज़ोर होती हैं।",
  NI, "igeo-soils-red-alluvial-saline", craft="linkage")

S(PH, "medium", "Consider the following statements about western Rajasthan and the Aravallis:",
  "पश्चिमी राजस्थान और अरावली के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Luni turns brackish in its lower course, which gives it its name, from the Sanskrit for 'salt river'.",
   "Most streams of the Thar are short-lived and end in the sand or in salt lakes, because the rain is too scanty and irregular to keep them flowing to the sea.",
   "Guru Shikhar, the highest peak of the Aravallis, lies in the Mount Abu area."],
  ["लूणी अपने निचले मार्ग में खारी हो जाती है, जिससे इसे संस्कृत के 'लवण-नदी' से अपना नाम मिला।",
   "थार की अधिकांश धाराएँ अल्पजीवी हैं और रेत में या खारी झीलों में समाप्त हो जाती हैं, क्योंकि वर्षा इतनी कम और अनियमित है कि वे समुद्र तक बहती नहीं रह पातीं।",
   "अरावली की सबसे ऊँची चोटी गुरु शिखर माउंट आबू क्षेत्र में है।"],
  C3, 2,
  "All three are correct. The Luni rises near Ajmer and flows south-west for about 495 km to be lost in the marshes of the Rann of Kachchh; its water is fresh as far as about Balotra and turns saline below, as it picks up salts from the arid ground. "
  "The Thar has mostly inland drainage: with 10-25 cm of rain a year, falling in a few heavy bursts, streams vanish into the sand or end in salt lakes such as Didwana and Pachpadra. Guru Shikhar (about 1,722 m) rises in the Mount Abu hills at the south-western end of the Aravallis.",
  "तीनों कथन सही हैं। लूणी अजमेर के पास निकलकर लगभग 495 किमी दक्षिण-पश्चिम बहती है और कच्छ के रण के दलदलों में खो जाती है; इसका पानी लगभग बालोतरा तक मीठा रहता है और उसके नीचे शुष्क भूमि से लवण उठाकर खारा हो जाता है। "
  "थार में अधिकतर आंतरिक अपवाह है: साल में 10-25 सेमी वर्षा, जो कुछ भारी बौछारों में गिरती है, के कारण धाराएँ रेत में समा जाती हैं या डीडवाना और पचपदरा जैसी खारी झीलों में समाप्त होती हैं। गुरु शिखर (लगभग 1,722 मीटर) अरावली के दक्षिण-पश्चिमी छोर पर माउंट आबू की पहाड़ियों में है।",
  NI, "igeo-thar-luni-barchans-guru-shikhar", craft="linkage")

if __name__ == "__main__":
    write_updates("upg_l2_t13_igeo_a.sql", statuses=("draft", "published"))
