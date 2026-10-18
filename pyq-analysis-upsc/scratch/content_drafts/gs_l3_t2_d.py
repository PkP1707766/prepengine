# -*- coding: utf-8 -*-
"""Level 3 · Test 2 (GS Integrated Test 2) -- part D: Geography (10) (upsc_l3_cell_targets.mjs 2).
Geography cells: Resources e-SI; Transport e-pairs; Climatology h-MCQ, m-stmt; Indian Physiography h-SI, m-stmt;
World Regions m-MCQ, m-stmt; Indian Rivers m-stmt; Geomorphology m-stmt.
Every fact was grepped against the Level-2 digests, all Level-1 drafts and Level 3 Test 1, and is one none of them
tests: Andhra Pradesh's shrimp farming; the mountain railways; the monsoon of northern Australia; cloudbursts; the
Tonle Sap's reversing river; cyclone naming in the north Indian Ocean; the Barak's course; hotspot volcanism and the
Reunion track; the Northern Sea Route; Kathiawar's relief and drainage. MCQ keys are pinned (pos)."""
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
IMD = "India Meteorological Department"

# ---------------------------------------------------------------- Resources (e-SI)
A("Resources: Minerals, Energy & Agriculture", "easy",
  "Statement-I: Andhra Pradesh is the leading State in India's farmed shrimp production.",
  "कथन-I: आंध्र प्रदेश भारत में पालित झींगा उत्पादन में अग्रणी राज्य है।",
  "Statement-II: Its long coastline and the brackish-water areas around the Godavari and Krishna deltas suit coastal aquaculture.",
  "कथन-II: इसकी लंबी तटरेखा और गोदावरी तथा कृष्णा डेल्टाओं के आसपास के खारे पानी वाले क्षेत्र तटीय जलकृषि के अनुकूल हैं।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I. Shrimp farming needs flat coastal land with access to brackish water, and the deltas of the Godavari and the Krishna, around districts such as Nellore, West Godavari and Krishna, offer it in plenty; Andhra Pradesh produces the largest share of India's farmed shrimp, most of it the whiteleg shrimp (Litopenaeus vannamei) introduced in 2009. "
  "Frozen shrimp is India's leading seafood export, though conversion of farmland and mangroves into ponds and the salinisation of soils are concerns.",
  "दोनों कथन सही हैं, और कथन-II कथन-I की व्याख्या करता है। झींगा पालन के लिए खारे पानी की पहुँच वाली समतल तटीय भूमि चाहिए, और नेल्लोर, पश्चिम गोदावरी और कृष्णा जैसे ज़िलों के आसपास गोदावरी और कृष्णा के डेल्टा यह प्रचुरता से देते हैं; भारत के पालित झींगे का सबसे बड़ा हिस्सा आंध्र प्रदेश पैदा करता है, जिसमें से अधिकांश 2009 में शुरू किया गया व्हाइटलेग झींगा (लिटोपेनियस वन्नामेई) है। "
  "जमा हुआ झींगा भारत का प्रमुख समुद्री खाद्य निर्यात है, यद्यपि खेतों और मैंग्रोव का तालाबों में बदलना और मिट्टी का लवणीकरण चिंता के विषय हैं।",
  f"Department of Fisheries, Handbook on Fisheries Statistics; {IPEc}.",
  "l3-t2-geo-andhra-shrimp-aquaculture", craft="linkage")

# ---------------------------------------------------------------- Transport, Ports & Human Geography (e-pairs)
P("Transport, Ports & Human Geography", "easy", "Consider the following pairs of mountain railways and the States through which they run:",
  "पर्वतीय रेलों और उन राज्यों के निम्नलिखित युग्मों पर विचार कीजिए जिनसे होकर वे चलती हैं:",
  ["Darjeeling Himalayan Railway : West Bengal",
   "Nilgiri Mountain Railway : Tamil Nadu",
   "Kalka-Shimla Railway : Haryana and Himachal Pradesh",
   "Matheran Light Railway : Maharashtra"],
  ["दार्जिलिंग हिमालयन रेलवे : पश्चिम बंगाल",
   "नीलगिरि पर्वतीय रेलवे : तमिलनाडु",
   "कालका-शिमला रेलवे : हरियाणा और हिमाचल प्रदेश",
   "माथेरान लाइट रेलवे : महाराष्ट्र"],
  3,
  "All four pairs are correct. The Darjeeling Himalayan Railway (1881), the Nilgiri Mountain Railway (1908), which climbs to Udhagamandalam with a rack-and-pinion section, and the Kalka-Shimla Railway (1903), which starts at Kalka in Haryana, together form the 'Mountain Railways of India' World Heritage Site. "
  "The Matheran Light Railway near Mumbai, opened in 1907, is on India's tentative list but not yet inscribed. These narrow-gauge lines were built to reach colonial hill stations, which is why they climb so steeply with loops, zigzags and reversing stations.",
  "चारों युग्म सही हैं। दार्जिलिंग हिमालयन रेलवे (1881), रैक-और-पिनियन खंड के सहारे उदगमंडलम तक चढ़ने वाली नीलगिरि पर्वतीय रेलवे (1908), और हरियाणा के कालका से शुरू होने वाली कालका-शिमला रेलवे (1903) मिलकर 'भारत की पर्वतीय रेलें' विश्व धरोहर स्थल बनाती हैं। "
  "मुंबई के पास 1907 में खुली माथेरान लाइट रेलवे भारत की संभावित सूची में है पर अभी अंकित नहीं है। ये नैरो-गेज लाइनें औपनिवेशिक पर्वतीय नगरों तक पहुँचने के लिए बनी थीं, इसीलिए वे लूपों, ज़िगज़ैग और रिवर्सिंग स्टेशनों के साथ इतनी तीखी चढ़ाई करती हैं।",
  f"UNESCO World Heritage List (Mountain Railways of India, 1999, 2005, 2008); Ministry of Railways; {IPEc}.",
  "l3-t2-geo-mountain-railways", craft="recall")

# ---------------------------------------------------------------- Climatology & Biomes (h-MCQ, m-stmt)
M("Climatology & Biomes", "hard",
  "Darwin, on the northern coast of Australia, gets most of its rain between December and March. The main reason is that during these months:",
  "ऑस्ट्रेलिया के उत्तरी तट पर स्थित डार्विन में अधिकांश वर्षा दिसंबर से मार्च के बीच होती है। इसका मुख्य कारण यह है कि इन महीनों में:",
  ["the westerlies move north and bring frontal rain, as they do at Perth and Adelaide",
   "the south-east trade winds strengthen and are forced up the Great Dividing Range",
   "the cold West Australian current weakens and lets warm water reach the coast",
   "the ITCZ shifts south and moist north-westerly winds blow in from the sea"],
  ["पछुआ पवनें उत्तर की ओर खिसककर वाताग्री वर्षा लाती हैं, जैसे वे पर्थ और एडिलेड में लाती हैं",
   "दक्षिण-पूर्वी व्यापारिक पवनें तेज़ होकर ग्रेट डिवाइडिंग रेंज पर चढ़ने को बाध्य होती हैं",
   "ठंडी पश्चिम ऑस्ट्रेलियाई धारा कमज़ोर होकर गर्म पानी को तट तक आने देती है",
   "ITCZ दक्षिण की ओर खिसकता है और समुद्र से नम उत्तर-पश्चिमी पवनें आती हैं"],
  3,
  "Northern Australia has a monsoon climate that mirrors India's. In the southern summer the continent heats up, a low forms over it and the Inter-Tropical Convergence Zone moves south across the Timor and Arafura seas; winds from the northern hemisphere cross the equator, are turned left by the Coriolis force and arrive as moist north-westerlies, giving the 'wet'. "
  "From May to October the south-east trades blow off the dry interior and the north has its 'dry'. Frontal rain from the westerlies falls in the south-west and south in winter, and the trades give rain to the Queensland coast, not to Darwin.",
  "उत्तरी ऑस्ट्रेलिया की मानसूनी जलवायु भारत की दर्पण-छवि है। दक्षिणी गर्मियों में महाद्वीप गर्म होता है, उस पर निम्न दाब बनता है और अंतर-उष्णकटिबंधीय अभिसरण क्षेत्र तिमोर और अराफ़ुरा सागरों के पार दक्षिण की ओर आता है; उत्तरी गोलार्ध की पवनें भूमध्यरेखा पार करती हैं, कोरिऑलिस बल से बाईं ओर मुड़ती हैं और नम उत्तर-पश्चिमी पवनों के रूप में पहुँचकर 'वर्षा ऋतु' लाती हैं। "
  "मई से अक्टूबर तक दक्षिण-पूर्वी व्यापारिक पवनें शुष्क भीतरी भाग से बहती हैं और उत्तर में 'शुष्क ऋतु' होती है। पछुआ पवनों की वाताग्री वर्षा सर्दियों में दक्षिण-पश्चिम और दक्षिण में होती है, और व्यापारिक पवनें क्वींसलैंड तट को वर्षा देती हैं, डार्विन को नहीं।",
  FPG + " (World Climate; Atmospheric Circulation).",
  "l3-t2-geo-northern-australia-monsoon", pos=3, craft="application")

S("Climatology & Biomes", "medium", "Consider the following statements about the naming of tropical cyclones over the north Indian Ocean:",
  "उत्तरी हिंद महासागर के उष्णकटिबंधीय चक्रवातों के नामकरण के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The names come from a list contributed by the member countries of the WMO/ESCAP Panel on Tropical Cyclones.",
   "The names are assigned by the India Meteorological Department's Regional Specialised Meteorological Centre in New Delhi.",
   "A name is reused after ten years, when the list comes round again."],
  ["नाम WMO/ESCAP उष्णकटिबंधीय चक्रवात पैनल के सदस्य देशों द्वारा दी गई सूची से आते हैं।",
   "नाम भारत मौसम विज्ञान विभाग का नई दिल्ली स्थित क्षेत्रीय विशिष्ट मौसम विज्ञान केंद्र देता है।",
   "सूची के फिर से घूमकर आने पर दस वर्ष बाद किसी नाम का पुनः उपयोग होता है।"],
  C3, 1,
  "Statements 1 and 2 are correct. The thirteen members of the Panel -- from Bangladesh, India, Myanmar, Sri Lanka and Thailand to Iran, Oman, Saudi Arabia and Yemen -- each gave thirteen names for the list adopted in 2020, which RSMC New Delhi uses in turn for storms over the Bay of Bengal and the Arabian Sea. "
  "Statement 3 is wrong: each name is used only once and then struck off. Short, distinct names make warnings easier to issue and remember.",
  "कथन 1 और 2 सही हैं। पैनल के तेरह सदस्यों -- बांग्लादेश, भारत, म्यांमार, श्रीलंका और थाईलैंड से लेकर ईरान, ओमान, सऊदी अरब और यमन तक -- ने 2020 में अपनाई गई सूची के लिए तेरह-तेरह नाम दिए, जिनका उपयोग RSMC नई दिल्ली बंगाल की खाड़ी और अरब सागर के तूफ़ानों के लिए बारी-बारी से करता है। "
  "कथन 3 ग़लत है: हर नाम केवल एक बार प्रयुक्त होकर हटा दिया जाता है। छोटे, अलग नाम चेतावनियाँ जारी करना और याद रखना आसान बनाते हैं।",
  f"{IMD} (RSMC New Delhi); World Meteorological Organization.",
  "l3-t2-geo-cyclone-naming", craft="precision")

# ---------------------------------------------------------------- Indian Physiography, Climate & Regions (h-SI, m-stmt)
A("Indian Physiography, Climate & Regions", "hard",
  "Statement-I: Cloudbursts occur only in the Himalaya and never over the Western Ghats or the plains.",
  "कथन-I: बादल फटने की घटनाएँ केवल हिमालय में होती हैं, पश्चिमी घाट या मैदानों पर कभी नहीं।",
  "Statement-II: The India Meteorological Department treats rainfall of about 100 mm or more in an hour over a small area as a cloudburst.",
  "कथन-II: भारत मौसम विज्ञान विभाग किसी छोटे क्षेत्र पर एक घंटे में लगभग 100 मिमी या उससे अधिक वर्षा को बादल फटना मानता है।",
  3,
  "Statement-I is incorrect and Statement-II is correct. A cloudburst is a short, extreme downpour from a towering cumulonimbus cloud over an area of a few tens of square kilometres. "
  "Cloudbursts are most frequent on Himalayan slopes in the monsoon, because moist air forced up steep terrain rises fast and builds very tall clouds, and the rain falls into narrow valleys where it turns at once into flash floods and debris flows -- hence the disasters in Uttarakhand and Himachal Pradesh. But the same convective process can produce them over the Western Ghats and, more rarely, over the plains; what defines a cloudburst is the intensity of rain, not the place.",
  "कथन-I ग़लत है और कथन-II सही है। बादल फटना कुछ दसियों वर्ग किलोमीटर क्षेत्र पर किसी विशाल कपासी-वर्षी बादल से होने वाली छोटी, अत्यधिक मूसलाधार वर्षा है। "
  "मानसून में ये हिमालयी ढलानों पर सबसे अधिक होते हैं, क्योंकि खड़ी ढलान पर चढ़ने को बाध्य नम हवा तेज़ी से उठकर बहुत ऊँचे बादल बनाती है, और वर्षा संकरी घाटियों में गिरकर तुरंत आकस्मिक बाढ़ और मलबा-प्रवाह बन जाती है -- इसीलिए उत्तराखंड और हिमाचल प्रदेश में आपदाएँ होती हैं। पर यही संवहनी प्रक्रिया पश्चिमी घाट पर और, कम बार, मैदानों पर भी इन्हें पैदा कर सकती है; बादल फटने की पहचान वर्षा की तीव्रता से है, स्थान से नहीं।",
  f"{IMD} (glossary: cloudburst); National Disaster Management Authority; {IPE} (Climate).",
  "l3-t2-geo-cloudbursts", craft="inference")

S("Indian Physiography, Climate & Regions", "medium", "Consider the following statements about the Kathiawar (Saurashtra) peninsula:",
  "काठियावाड़ (सौराष्ट्र) प्रायद्वीप के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Its highest point is in the Girnar hills, an old igneous massif.",
   "The Gulf of Khambhat lies to its east and the Gulf of Kachchh to its north.",
   "Its rivers flow outwards in all directions from a central upland."],
  ["इसका सबसे ऊँचा बिंदु गिरनार पहाड़ियों में है, जो एक प्राचीन आग्नेय पुंज है।",
   "खंभात की खाड़ी इसके पूर्व में और कच्छ की खाड़ी इसके उत्तर में है।",
   "इसकी नदियाँ एक केंद्रीय उच्चभूमि से सभी दिशाओं में बाहर की ओर बहती हैं।"],
  C3, 2,
  "All three statements are correct. Girnar, near Junagadh, rises to about 1,070 m and is formed of igneous rocks intruded into the Deccan lavas that cover much of the peninsula. "
  "Kathiawar juts into the Arabian Sea between the two gulfs, and its short rivers, such as the Bhadar and the Shetrunji, radiate outwards from the central uplands, a radial pattern. Its low, seasonal rainfall and the salinity that creeps into its coastal aquifers make water the peninsula's chronic problem.",
  "तीनों कथन सही हैं। जूनागढ़ के पास गिरनार लगभग 1,070 मीटर ऊँचा है और उन आग्नेय चट्टानों से बना है जो प्रायद्वीप के बड़े भाग को ढकने वाले दक्कन लावा में घुस आई थीं। "
  "काठियावाड़ दोनों खाड़ियों के बीच अरब सागर में निकला हुआ है, और भादर और शेत्रुंजी जैसी इसकी छोटी नदियाँ केंद्रीय उच्चभूमि से बाहर की ओर अरीय प्रतिरूप में बहती हैं। कम, मौसमी वर्षा और तटीय जलभृतों में घुसती लवणता के कारण पानी इस प्रायद्वीप की स्थायी समस्या है।",
  f"{IPE} (Structure and Physiography; Drainage System).",
  "l3-t2-geo-kathiawar-girnar-radial", craft="precision")

# ---------------------------------------------------------------- World Regions, Water Bodies & Places (m-MCQ, m-stmt)
M("World Regions, Water Bodies & Places", "medium",
  "The Tonle Sap, a lake that swells several times in area each rainy season as the Mekong's floodwaters force its outflow river to run backwards, lies in:",
  "टोनले साप, एक झील जो हर वर्षा ऋतु में कई गुना फैल जाती है क्योंकि मेकांग का बाढ़-जल उसकी निकास नदी को उलटी दिशा में बहने को बाध्य करता है, कहाँ स्थित है?",
  ["Cambodia", "Myanmar", "Thailand", "Vietnam"],
  ["कंबोडिया", "म्यांमार", "थाईलैंड", "वियतनाम"],
  0,
  "In the monsoon the Mekong rises so high at Phnom Penh that the Tonle Sap river, which normally drains the lake into the Mekong, reverses and pushes water up into the lake, which grows several-fold and floods the surrounding forest; in the dry season the flow turns round again. "
  "The flood pulse makes the lake one of the richest freshwater fisheries in the world and a mainstay of Cambodia's food supply -- which is why dams on the upper Mekong, which even out its flow, worry the downstream countries.",
  "मानसून में फ़्नोम पेन्ह पर मेकांग इतनी ऊँची उठती है कि टोनले साप नदी, जो सामान्यतः झील का पानी मेकांग में ले जाती है, उलटकर पानी को झील में धकेलती है, जो कई गुना बढ़कर आसपास के वन को डुबो देती है; शुष्क ऋतु में प्रवाह फिर पलट जाता है। "
  "यह बाढ़-स्पंद झील को विश्व के सबसे समृद्ध मीठे पानी के मत्स्य क्षेत्रों में से एक और कंबोडिया की खाद्य आपूर्ति का आधार बनाता है -- इसीलिए ऊपरी मेकांग पर बने बाँध, जो उसके प्रवाह को समतल करते हैं, निचले देशों को चिंतित करते हैं।",
  f"{FPG}; Mekong River Commission.",
  "l3-t2-geo-tonle-sap-reversal", pos=0, craft="application")

S("World Regions, Water Bodies & Places", "medium", "Consider the following statements about the Northern Sea Route:",
  "उत्तरी समुद्री मार्ग के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It runs through the islands of the Canadian Arctic, linking the Atlantic and the Pacific.",
   "For voyages between northern Europe and East Asia, it is shorter than the route through the Suez Canal.",
   "It is open all year to ordinary ships, with no need for ice-strengthened hulls or icebreaker escort."],
  ["यह कनाडा के आर्कटिक द्वीपों से होकर अटलांटिक और प्रशांत को जोड़ता है।",
   "उत्तरी यूरोप और पूर्वी एशिया के बीच की यात्राओं के लिए यह स्वेज़ नहर वाले मार्ग से छोटा है।",
   "यह साधारण जहाज़ों के लिए पूरे वर्ष खुला रहता है, बर्फ़-रोधी पतवार या हिमभंजक अनुरक्षण की आवश्यकता नहीं होती।"],
  C3, 0,
  "Only statement 2 is correct. Statement 1 describes the Northwest Passage; the Northern Sea Route runs along Russia's Arctic coast, from the Kara Sea to the Bering Strait. Between Rotterdam and Yokohama the Northern Sea Route is roughly a third shorter than the Suez route, which is why shrinking Arctic sea ice has made it commercially interesting, and why India has begun to look at it alongside the proposed Chennai-Vladivostok sea corridor. "
  "Statement 3 is wrong: the route is reliably usable only for a few summer months, and even then Russia generally requires ice-class ships or icebreaker escort, besides permits -- costs and risks that still limit its use.",
  "केवल कथन 2 सही है। कथन 1 उत्तर-पश्चिमी मार्ग (नॉर्थवेस्ट पैसेज) का वर्णन करता है; उत्तरी समुद्री मार्ग रूस के आर्कटिक तट के साथ, कारा सागर से बेरिंग जलडमरूमध्य तक चलता है। रॉटरडैम और योकोहामा के बीच उत्तरी समुद्री मार्ग स्वेज़ मार्ग से लगभग एक-तिहाई छोटा है, इसीलिए सिकुड़ती आर्कटिक समुद्री बर्फ़ ने इसे व्यावसायिक रूप से आकर्षक बनाया है, और इसीलिए भारत ने प्रस्तावित चेन्नई-व्लादिवोस्तोक समुद्री गलियारे के साथ इस पर भी ध्यान देना शुरू किया है। "
  "कथन 3 ग़लत है: यह मार्ग केवल गर्मियों के कुछ महीनों में भरोसे से उपयोग योग्य है, और तब भी रूस सामान्यतः अनुमति-पत्रों के अलावा हिम-श्रेणी के जहाज़ों या हिमभंजक अनुरक्षण की अपेक्षा करता है -- ऐसी लागतें और जोखिम जो अब भी इसके उपयोग को सीमित करते हैं।",
  f"{FHG} (Transport and Communication); Ministry of Ports, Shipping and Waterways.",
  "l3-t2-geo-northern-sea-route", craft="linkage")

# ---------------------------------------------------------------- Indian Rivers, Lakes & Wetlands (m-stmt)
S("Indian Rivers, Lakes & Wetlands", "medium", "Consider the following statements about the Barak river:",
  "बराक नदी के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It rises in the hills of Manipur and flows through the Cachar plains of southern Assam.",
   "On entering Bangladesh it divides into the Surma and the Kushiyara, whose waters later form the Meghna.",
   "It joins the Brahmaputra near Guwahati."],
  ["यह मणिपुर की पहाड़ियों से निकलकर दक्षिणी असम के कछार मैदानों से होकर बहती है।",
   "बांग्लादेश में प्रवेश करने पर यह सुरमा और कुशियारा में बँट जाती है, जिनका पानी बाद में मेघना बनाता है।",
   "यह गुवाहाटी के पास ब्रह्मपुत्र में मिलती है।"],
  C3, 1,
  "Statements 1 and 2 are correct. The Barak rises in the Manipur hills, skirts the Manipur-Mizoram border and flows west through the Barak valley around Silchar before crossing into Bangladesh near Karimganj, where it splits into the Surma and the Kushiyara; these reunite as the Meghna, which joins the combined Ganga and Brahmaputra waters near the sea. "
  "Statement 3 is wrong: the Barak drains a separate basin south of the Brahmaputra valley, divided from it by the hills of Meghalaya and the Karbi plateau. The long-proposed Tipaimukh dam on the Barak has been opposed in Bangladesh and Manipur.",
  "कथन 1 और 2 सही हैं। बराक मणिपुर की पहाड़ियों से निकलती है, मणिपुर-मिज़ोरम सीमा के साथ बहती है और सिलचर के आसपास बराक घाटी से पश्चिम की ओर बहकर करीमगंज के पास बांग्लादेश में प्रवेश करती है, जहाँ यह सुरमा और कुशियारा में बँट जाती है; ये फिर मिलकर मेघना बनती हैं, जो समुद्र के पास गंगा और ब्रह्मपुत्र के संयुक्त जल से मिलती है। "
  "कथन 3 ग़लत है: बराक ब्रह्मपुत्र घाटी के दक्षिण में एक अलग बेसिन को अपवाहित करती है, जो मेघालय की पहाड़ियों और कार्बी पठार द्वारा उससे अलग है। बराक पर लंबे समय से प्रस्तावित टिपाईमुख बाँध का बांग्लादेश और मणिपुर में विरोध हुआ है।",
  f"{IPE} (Drainage System); Central Water Commission.",
  "l3-t2-geo-barak-surma-kushiyara", craft="precision")

# ---------------------------------------------------------------- Geomorphology & Earth's Interior (m-stmt)
S("Geomorphology & Earth's Interior", "medium", "Consider the following statements about hotspots:",
  "हॉटस्पॉट (तप्त स्थलों) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["A hotspot is a plume of hot material from deep in the mantle that stays roughly fixed while a plate moves over it, leaving a chain of volcanoes.",
   "In the Hawaiian chain the islands become older towards the north-west, and the volcanoes of the island of Hawaii in the south-east are still active.",
   "The Deccan Traps are thought to have erupted when the Indian plate passed over the hotspot that now lies beneath Reunion island."],
  ["हॉटस्पॉट मेंटल की गहराई से आने वाली गर्म सामग्री का एक प्लूम है जो लगभग स्थिर रहता है जबकि प्लेट उसके ऊपर से खिसकती है, और ज्वालामुखियों की एक शृंखला छोड़ जाता है।",
   "हवाई शृंखला में द्वीप उत्तर-पश्चिम की ओर अधिक पुराने होते जाते हैं, और दक्षिण-पूर्व में हवाई द्वीप के ज्वालामुखी अब भी सक्रिय हैं।",
   "माना जाता है कि दक्कन ट्रैप तब फूटे जब भारतीय प्लेट उस हॉटस्पॉट के ऊपर से गुज़री जो अब रियूनियन द्वीप के नीचे है।"],
  C3, 2,
  "All three statements are correct. Most volcanoes lie on plate boundaries, but hotspots explain volcanoes in the middle of plates: as the Pacific plate moves north-west over the Hawaiian plume, older islands are carried away and worn down while new ones form over the plume. "
  "About 66 million years ago the Indian plate, moving north, passed over the plume now under Reunion, and floods of basalt built the Deccan Traps; as India moved on, the same plume left a trail of volcanic ridges that underlie the Lakshadweep and the Maldives -- so the Deccan plateau and the coral islands to its south-west share a single origin.",
  "तीनों कथन सही हैं। अधिकांश ज्वालामुखी प्लेट सीमाओं पर हैं, पर हॉटस्पॉट प्लेटों के बीच के ज्वालामुखियों की व्याख्या करते हैं: जैसे-जैसे प्रशांत प्लेट हवाई प्लूम के ऊपर से उत्तर-पश्चिम की ओर खिसकती है, पुराने द्वीप दूर चले जाते और घिसते हैं जबकि प्लूम के ऊपर नए बनते हैं। "
  "लगभग 6.6 करोड़ वर्ष पहले उत्तर की ओर बढ़ती भारतीय प्लेट उस प्लूम के ऊपर से गुज़री जो अब रियूनियन के नीचे है, और बेसाल्ट की बाढ़ ने दक्कन ट्रैप बनाए; भारत के आगे बढ़ने पर उसी प्लूम ने ज्वालामुखीय कटकों की एक पगडंडी छोड़ी जो लक्षद्वीप और मालदीव के नीचे है -- इसलिए दक्कन पठार और उसके दक्षिण-पश्चिम के प्रवाल द्वीपों का उद्गम एक ही है।",
  f"{FPG} (Distribution of Oceans and Continents); {IPE}.",
  "l3-t2-geo-hotspots-hawaii-reunion", craft="linkage")

write("gs_l3_t2_d.sql")
