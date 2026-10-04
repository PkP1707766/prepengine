# -*- coding: utf-8 -*-
"""Level 2 · Test 13 (Geography 2) -- depth audit of 2026-10-04, part B: Indian Rivers, Lakes & Wetlands, and the
craft tags for the 72 kept rows (docs/upsc-question-design-standard.md §6). Part A is upg_l2_t13_igeo_a.py.

Part B rewrites 13 recall rows in place with the same concept id, type and difficulty:
  - analytic: what a Chinese dam on the Yarlung Tsangpo means downstream, what reopening Chilika's mouth
    did, why the Damodar Valley Corporation was set up, how the Wular steadies the Jhelum, how the Chambal
    ravines formed, why India's projects on the western rivers are run-of-the-river, why Dal is shrinking,
    how ice dams on the Shyok burst, and a 5-item list of the Kaveri's tributaries;
  - precision: near-miss versions of the city-river pairs, the Panch Prayag confluences, the Godavari's
    source and basin, and the large lakes.
Two kept rows are tagged precision because the stem itself sets the condition the trap turns on: 'within
India' (the longest-river MCQ) and 'of India' against the mainland (the southernmost-point MCQ).
Test 13 after both parts: analytic 38, precision 35, recall 30.
Leaks avoided while drafting:
  - the Kosi's westward shift as a Damodar distractor (states the Kosi row's statement 1);
  - the Satluj or the Indus flowing out of Tibet in Yarlung distractors (the Satluj MCQ, the Indus row);
  - antecedent rivers in a Satluj gorge stem (the Himalayan-vs-Peninsular row's statement 1), so the Satluj
    MCQ was left;
  - the Kaveri's two monsoons (supports the Coromandel AR's Statement I), so the Kaveri-Satluj row was left;
  - the Brahmaputra's sediment load in new stems (the Assam-floods AR's Statement II);
  - a lagoon's link to the sea making it brackish, as a general rule (bears on the Kolleru AR)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write_updates, CODE
from polity_common import C3, C4, T2

d.SUBJECT = "Geography"
d.REQUIRE_CRAFT = True
RV = "Indian Rivers, Lakes & Wetlands"
NI = "NCERT Class XI, India: Physical Environment"
NC9 = "NCERT Class IX, Contemporary India I"
FIVE = ["Only two", "Only three", "Only four", "All five"]
FIVE_HI = ["केवल दो", "केवल तीन", "केवल चार", "सभी पाँच"]

# ================================================================ MCQs (5)
M(RV, "hard", "In 2025 China began building a very large hydropower project on the lower Yarlung Tsangpo, near the great bend where the river turns south towards India. India's main concern about it is that:",
  "2025 में चीन ने यारलुंग त्सांगपो के निचले भाग पर, उस बड़े मोड़ के पास जहाँ नदी भारत की ओर दक्षिण में मुड़ती है, एक बहुत बड़ी जलविद्युत परियोजना बनानी शुरू की। इसके बारे में भारत की मुख्य चिंता यह है कि:",
  ["lying upstream, it could alter the flow, silt and floods of the Siang and the Brahmaputra",
   "lying downstream of Assam, it could make the river's water back up deep into Indian territory",
   "it would take water from the Ganga's headwaters in Uttarakhand, lowering the Ganga's flow",
   "it stands in a region free of earthquakes, so it could store water for China all year round"],
  ["ऊपर की ओर होने से यह सियांग और ब्रह्मपुत्र के प्रवाह, गाद और बाढ़ों को बदल सकती है",
   "असम से नीचे की ओर होने से यह नदी के पानी को भारतीय क्षेत्र में गहराई तक पीछे लौटा सकती है",
   "यह उत्तराखंड में गंगा के उद्गम-क्षेत्र से पानी लेकर गंगा का प्रवाह घटा देगी",
   "यह भूकंप-मुक्त क्षेत्र में है, इसलिए चीन के लिए साल भर पानी संचित कर सकती है"],
  0,
  "The Yarlung Tsangpo rises near Mount Kailash, flows east across southern Tibet, makes a great U-turn around Namcha Barwa through one of the deepest gorges on Earth, and enters Arunachal Pradesh as the Siang (Dihang), becoming the Brahmaputra in Assam. A dam so far upstream could change how much water and fertile silt reach India, especially in the dry season, and a sudden release could worsen floods; the site also lies in a highly earthquake-prone zone. "
  "India has asked for transparency and consultation, and has planned the Upper Siang project partly as buffer storage. The project has nothing to do with the Ganga, whose sources lie in India.",
  "यारलुंग त्सांगपो कैलाश पर्वत के पास निकलती है, दक्षिणी तिब्बत में पूर्व की ओर बहती है, पृथ्वी के सबसे गहरे गॉर्जों में से एक से होकर नामचा बरवा के चारों ओर बड़ा U-मोड़ लेती है, और सियांग (दिहांग) के रूप में अरुणाचल प्रदेश में आकर असम में ब्रह्मपुत्र बनती है। इतनी ऊपर बना बाँध बदल सकता है कि कितना पानी और उपजाऊ गाद भारत पहुँचे, विशेषकर शुष्क ऋतु में, और अचानक छोड़ा गया पानी बाढ़ें बढ़ा सकता है; स्थल भी अत्यधिक भूकंप-प्रवण क्षेत्र में है। "
  "भारत ने पारदर्शिता और परामर्श माँगा है, और अपर सियांग परियोजना को आंशिक रूप से बफ़र भंडारण के रूप में नियोजित किया है। परियोजना का गंगा से कोई संबंध नहीं है, जिसके उद्गम भारत में हैं।",
  "Ministry of External Affairs -- statements on the Yarlung Tsangpo project (2025).", "irv-yarlung-tsangpo-siang", craft="linkage")

M(RV, "medium", "By the late 1990s the mouth linking Chilika to the Bay of Bengal had silted up, its fish catch had collapsed and freshwater weeds were spreading. In 2000 a new mouth was cut through the sand bar. The main result was that:",
  "1990 के दशक के अंत तक चिलिका को बंगाल की खाड़ी से जोड़ने वाला मुहाना गाद से भर गया था, उसका मत्स्य-उत्पादन गिर गया था और मीठे पानी की खरपतवार फैल रही थी। 2000 में रेत की रोधिका को काटकर एक नया मुहाना बनाया गया। इसका मुख्य परिणाम यह हुआ कि:",
  ["sea water flowed in again, restoring the brackish water on which its fish and prawns depend",
   "the lagoon turned fully into a freshwater lake, which suits its fish and its prawns much better",
   "the whole lagoon drained into the sea and dried up, so the weeds died and the fishing ended",
   "river floods could no longer enter it, so silt stopped reaching its bed and its fish returned"],
  ["समुद्री जल फिर भीतर आया, और वह खारा-मीठा जल लौटा जिस पर इसकी मछलियाँ और झींगे निर्भर हैं",
   "लैगून पूरी तरह मीठे पानी की झील बन गया, जो इसकी मछलियों और झींगों के लिए कहीं बेहतर है",
   "पूरा लैगून समुद्र में बहकर सूख गया, जिससे खरपतवार मर गई और मछली पकड़ना बंद हो गया",
   "नदियों की बाढ़ अब इसमें नहीं आ सकती थी, इसलिए गाद इसके तल तक नहीं पहुँची और मछलियाँ लौट आईं"],
  0,
  "Chilika, India's largest brackish-water lagoon, on the Odisha coast, depends on a balance between fresh water from the Mahanadi's distributaries and sea water entering through its mouth. As silt choked the old mouth, salinity fell, freshwater weeds spread, and the fish, prawns and crabs that breed in the sea declined. "
  "The new mouth cut by the Chilika Development Authority in 2000 restored the tidal exchange: salinity rose again, the weeds receded and the fish catch multiplied several times over. The rivers still flow in; it is the sea's share that was restored.",
  "ओडिशा तट पर भारत का सबसे बड़ा खारे पानी का लैगून चिलिका महानदी की वितरिकाओं के मीठे पानी और मुहाने से आने वाले समुद्री जल के संतुलन पर निर्भर है। गाद से पुराना मुहाना रुकने पर लवणता घटी, मीठे पानी की खरपतवार फैली, और समुद्र में प्रजनन करने वाली मछलियाँ, झींगे और केकड़े घट गए। "
  "2000 में चिलिका विकास प्राधिकरण द्वारा काटे गए नए मुहाने ने ज्वारीय आदान-प्रदान लौटाया: लवणता फिर बढ़ी, खरपतवार घटी और मत्स्य-उत्पादन कई गुना बढ़ गया। नदियाँ अब भी भीतर बहती हैं; जो लौटाया गया, वह समुद्र का हिस्सा था।",
  "Chilika Development Authority, Government of Odisha.", "irv-chilika-largest-lagoon", craft="linkage")

M(RV, "medium", "The Damodar Valley Corporation, set up in 1948 on the model of the Tennessee Valley Authority, built a series of dams on the Damodar and its tributaries. The main reason was that the river:",
  "टेनेसी वैली अथॉरिटी के आदर्श पर 1948 में बने दामोदर घाटी निगम ने दामोदर और उसकी सहायक नदियों पर बाँधों की एक शृंखला बनाई। इसका मुख्य कारण यह था कि यह नदी:",
  ["poured off the Chotanagpur plateau in sudden floods that ruined the plains of West Bengal",
   "dried up completely every summer, leaving the towns of the coalfield with no water to drink",
   "carried glacial meltwater that froze over in winter and blocked the movement of river boats",
   "formed the border with East Pakistan, so all of its waters had to be shared under a treaty"],
  ["छोटानागपुर पठार से अचानक बाढ़ों के रूप में उतरती थी जो पश्चिम बंगाल के मैदानों को उजाड़ देती थीं",
   "हर गर्मी में पूरी तरह सूख जाती थी, जिससे कोयला क्षेत्र के नगरों को पीने का पानी नहीं मिलता था",
   "हिमनदों का पिघला पानी लाती थी जो सर्दियों में जमकर नावों की आवाजाही रोक देता था",
   "पूर्वी पाकिस्तान के साथ सीमा बनाती थी, इसलिए उसका सारा पानी एक संधि के तहत बाँटना पड़ता था"],
  0,
  "The Damodar flows east from the Chotanagpur plateau through a rift valley; its catchment gets intense monsoon storms on hard, steep ground, so floods came suddenly and spread over the lower plains of Bardhaman and Hooghly -- the reason it was called the 'Sorrow of Bengal'. "
  "After the disastrous flood of 1943, the Damodar Valley Corporation, India's first multipurpose river valley project, built dams such as Tilaiya, Konar, Maithon and Panchet to control floods, irrigate the plains and generate power for the coal and steel belt. The river is rain-fed, not glacier-fed, and lies wholly in India.",
  "दामोदर छोटानागपुर पठार से एक भ्रंश घाटी से होकर पूर्व की ओर बहती है; इसके जलग्रहण क्षेत्र में कठोर, तीव्र ढाल वाली भूमि पर तीव्र मानसूनी तूफ़ान आते हैं, इसलिए बाढ़ें अचानक आतीं और बर्धमान तथा हुगली के निचले मैदानों पर फैल जातीं, इसीलिए इसे 'बंगाल का शोक' कहा गया। "
  "1943 की विनाशकारी बाढ़ के बाद भारत की पहली बहुउद्देशीय नदी घाटी परियोजना, दामोदर घाटी निगम, ने बाढ़ नियंत्रण, मैदानों की सिंचाई और कोयला-इस्पात पट्टी के लिए बिजली के लिए तिलैया, कोनार, मैथन और पंचेत जैसे बाँध बनाए। नदी वर्षा-पोषित है, हिमनद-पोषित नहीं, और पूरी तरह भारत में है।",
  NC9, "irv-damodar-sorrow-of-bengal", craft="linkage")

M(RV, "easy", "Dal lake in Srinagar has shrunk and become choked with weeds over the past century. The main reason is that:",
  "श्रीनगर की डल झील पिछली सदी में सिकुड़ गई है और खरपतवार से भर गई है। इसका मुख्य कारण यह है कि:",
  ["sewage, silt and encroachments from its surroundings have been filling it up",
   "the Jhelum has been diverted away from it, so the lake no longer receives any water",
   "an earthquake cracked its floor and much of its water drained away underground",
   "the glaciers that once fed it have vanished, leaving it without inflow in summer"],
  ["आसपास के सीवेज, गाद और अतिक्रमण उसे भरते जा रहे हैं",
   "झेलम को उससे दूर मोड़ दिया गया है, इसलिए झील को अब कोई पानी नहीं मिलता",
   "एक भूकंप ने उसका तल चीर दिया और उसका बहुत-सा पानी भूमिगत बह गया",
   "जिन हिमनदों से वह पोषित थी वे लुप्त हो गए हैं, जिससे गर्मियों में उसमें पानी नहीं आता"],
  0,
  "Untreated sewage from houseboats and the city, fertiliser from the floating gardens and silt washed from the deforested hills around it have loaded Dal with nutrients and sediment, so weeds spread and the shallow lake fills up; land reclaimed for settlements and gardens has also eaten into its open water. "
  "The lake is fed mainly by springs and streams from the surrounding hills; dredging, de-weeding and sewage treatment are the main remedies.",
  "हाउसबोटों और शहर का अनुपचारित सीवेज, तैरते बाग़ों की खाद और आसपास की वनविहीन पहाड़ियों से बहकर आई गाद ने डल को पोषक तत्वों और अवसाद से भर दिया है, इसलिए खरपतवार फैलती है और उथली झील भरती जाती है; बस्तियों और बाग़ों के लिए पाटी गई भूमि ने भी उसके खुले जल को घटाया है। "
  "झील मुख्यतः आसपास की पहाड़ियों के झरनों और धाराओं से पोषित है; ड्रेजिंग, खरपतवार हटाना और सीवेज उपचार मुख्य उपाय हैं।",
  "Jammu and Kashmir Lake Conservation and Management Authority.", "irv-dal-lake-easy", craft="linkage")

M(RV, "medium", "The Shyok, an Indus tributary that rises from the Rimo glacier in the Karakoram, has caused several sudden, destructive floods in the past. The main reason is that:",
  "काराकोरम के रिमो हिमनद से निकलने वाली सिंधु की सहायक नदी श्योक ने अतीत में कई अचानक, विनाशकारी बाढ़ें लाई हैं। इसका मुख्य कारण यह है कि:",
  ["glaciers advancing from side valleys have dammed it, and the ice dams later burst",
   "monsoon cyclones from the Bay of Bengal regularly reach Ladakh and stall over its valley",
   "it flows through a rift valley whose floor drops suddenly whenever an earthquake strikes",
   "high tides from the Arabian Sea push far up the Indus and back up its water each month"],
  ["बगल की घाटियों से आगे बढ़ते हिमनदों ने उसे बाँध दिया, और बाद में ये हिम-बाँध टूट गए",
   "बंगाल की खाड़ी के मानसूनी चक्रवात नियमित रूप से लद्दाख पहुँचकर उसकी घाटी पर रुक जाते हैं",
   "यह एक भ्रंश घाटी से बहती है जिसका तल हर भूकंप पर अचानक धँस जाता है",
   "अरब सागर के ऊँचे ज्वार हर महीने सिंधु में दूर तक चढ़कर उसके पानी को पीछे लौटा देते हैं"],
  0,
  "Surging glaciers of the Karakoram, such as the Chong Kumdan, have more than once advanced across the narrow Shyok valley and blocked the river; the lake that formed behind the ice later broke through, as in 1929, sending a flood wave down the Shyok and the Indus for hundreds of kilometres. "
  "Monsoon storms rarely reach so far into the mountains, and tides do not travel that far inland.",
  "चोंग कुमदान जैसे काराकोरम के तेज़ी से बढ़ने वाले हिमनद एक से अधिक बार श्योक की सँकरी घाटी के आर-पार बढ़कर नदी को रोक चुके हैं; बर्फ़ के पीछे बनी झील बाद में फूट पड़ी, जैसे 1929 में, और श्योक तथा सिंधु में सैकड़ों किलोमीटर तक बाढ़ की लहर दौड़ी। "
  "मानसूनी तूफ़ान पर्वतों के इतने भीतर कम ही पहुँचते हैं, और ज्वार इतनी दूर भीतर नहीं जाते।",
  NI, "irv-shyok-ladakh", craft="linkage")

# ================================================================ pairs (1)
P(RV, "medium", "Consider the following pairs of cities and the rivers on which they stand:",
  "शहरों और उन नदियों के निम्नलिखित युग्मों पर विचार कीजिए जिन पर वे स्थित हैं:",
  ["Jabalpur : Narmada", "Hyderabad : Krishna", "Lucknow : Gomti", "Surat : Narmada"],
  ["जबलपुर : नर्मदा", "हैदराबाद : कृष्णा", "लखनऊ : गोमती", "सूरत : नर्मदा"],
  1,
  "Only pairs 1 and 3 are correct: Jabalpur stands near the Narmada, and Lucknow on the Gomti. Pairs 2 and 4 are near-misses. Hyderabad stands on the Musi, which is a tributary of the Krishna, not on the Krishna itself. Surat stands on the Tapi near its mouth; the city on the lower Narmada is Bharuch.",
  "केवल युग्म 1 और 3 सही हैं: जबलपुर नर्मदा के पास है, और लखनऊ गोमती पर। युग्म 2 और 4 निकट-भ्रम हैं। हैदराबाद मूसी पर है, जो कृष्णा की सहायक नदी है, स्वयं कृष्णा पर नहीं। सूरत अपने मुहाने के पास ताप्ती पर है; निचली नर्मदा पर बसा शहर भरूच है।",
  NC9, "irv-cities-rivers-pairs", craft="precision")

# ================================================================ statements (7)
S(RV, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Chilika lake lies in Odisha.",
   "Wular lake, on the course of the Jhelum, takes in the river's floodwaters and so acts as a natural flood reservoir for the Kashmir valley."],
  ["चिलिका झील ओडिशा में है।",
   "झेलम के मार्ग पर स्थित वुलर झील नदी के बाढ़-जल को समा लेती है और इस प्रकार कश्मीर घाटी के लिए एक प्राकृतिक बाढ़-जलाशय का काम करती है।"],
  T2, 2,
  "Both statements are correct. Chilika is the great lagoon of the Odisha coast. The Jhelum flows into the Wular near Bandipora and out again near Sopore, so when the river is in flood the shallow lake spreads over a much larger area and holds back the water, easing floods downstream; as silt and encroachment have shrunk it, that buffering has weakened.",
  "दोनों कथन सही हैं। चिलिका ओडिशा तट का विशाल लैगून है। झेलम बांदीपोरा के पास वुलर में आती है और सोपोर के पास फिर निकलती है, इसलिए नदी में बाढ़ आने पर उथली झील बहुत बड़े क्षेत्र में फैलकर पानी रोक लेती है और नीचे की ओर बाढ़ घटाती है; गाद और अतिक्रमण से उसके सिकुड़ने पर यह क्षमता कमज़ोर हुई है।",
  NC9, "irv-chilika-wular-easy", craft="linkage")

S(RV, "medium", "Consider the following statements about rivers of central India:",
  "मध्य भारत की नदियों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Chambal flows through a belt of deep ravines, carved by gully erosion of the soft alluvium along its banks.",
   "The Son rises in the Chotanagpur plateau.",
   "The Son is a tributary of the Yamuna."],
  ["चंबल गहरे बीहड़ों की एक पट्टी से बहती है, जो उसके किनारों की नरम जलोढ़ मिट्टी के अवनालिका अपरदन से बने हैं।",
   "सोन छोटानागपुर पठार से निकलती है।",
   "सोन यमुना की सहायक नदी है।"],
  C3, 0,
  "Only statement 1 is correct. Rising at Janapav near Mhow in the Vindhyan range of the Malwa plateau, the Chambal flows north-east into the Yamuna; along its lower course, monsoon run-off has cut the deep alluvial banks into a maze of gullies -- the Chambal ravines of Madhya Pradesh, Rajasthan and Uttar Pradesh, which eat into farmland and long sheltered outlaws. "
  "Statements 2 and 3 are wrong: the Son rises near Amarkantak in the Maikal hills and flows north and then east to join the Ganga near Patna.",
  "केवल कथन 1 सही है। मालवा पठार की विंध्य श्रेणी में महू के पास जानापाव से निकलकर चंबल उत्तर-पूर्व की ओर यमुना में मिलती है; अपने निचले मार्ग में मानसूनी अपवाह ने उसके गहरे जलोढ़ किनारों को अवनालिकाओं की भूलभुलैया में काट दिया है, जो मध्य प्रदेश, राजस्थान और उत्तर प्रदेश के चंबल बीहड़ हैं, जो खेती की भूमि को खाते हैं और लंबे समय तक डाकुओं के आश्रय रहे। "
  "कथन 2 और 3 गलत हैं: सोन मैकाल पहाड़ियों में अमरकंटक के पास निकलती है और उत्तर तथा फिर पूर्व की ओर बहकर पटना के पास गंगा में मिलती है।",
  NI, "irv-chambal-son-origins", craft="linkage")

S(RV, "medium", "Consider the following statements about the headstreams of the Ganga:",
  "गंगा की शीर्ष-धाराओं के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Bhagirathi and the Alaknanda meet at Devprayag to form the Ganga.",
   "The Mandakini joins the Alaknanda at Karnaprayag.",
   "The Pindar joins the Alaknanda at Rudraprayag."],
  ["भागीरथी और अलकनंदा देवप्रयाग में मिलकर गंगा बनाती हैं।",
   "मंदाकिनी कर्णप्रयाग में अलकनंदा से मिलती है।",
   "पिंडर रुद्रप्रयाग में अलकनंदा से मिलती है।"],
  C3, 0,
  "Only statement 1 is correct. Statements 2 and 3 swap two of the five prayags. Going down the Alaknanda, the confluences are Vishnuprayag (with the Dhauliganga), Nandprayag (the Nandakini), Karnaprayag (the Pindar), Rudraprayag (the Mandakini, which comes down from Kedarnath) and finally Devprayag, where the Alaknanda meets the Bhagirathi and the river takes the name Ganga.",
  "केवल कथन 1 सही है। कथन 2 और 3 पाँच प्रयागों में से दो को आपस में बदल देते हैं। अलकनंदा में नीचे की ओर संगम इस क्रम में हैं: विष्णुप्रयाग (धौलीगंगा), नंदप्रयाग (नंदाकिनी), कर्णप्रयाग (पिंडर), रुद्रप्रयाग (केदारनाथ से आने वाली मंदाकिनी) और अंत में देवप्रयाग, जहाँ अलकनंदा भागीरथी से मिलती है और नदी गंगा कहलाती है।",
  NI, "irv-ganga-panch-prayag", craft="precision")

S(RV, "medium", "Consider the following statements about the Godavari:",
  "गोदावरी के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It rises at Amarkantak in the Maikal hills.",
   "It has the second-largest basin among the rivers of the Peninsula, after the Krishna.",
   "The Indravati is a tributary of the Mahanadi."],
  ["यह मैकाल पहाड़ियों में अमरकंटक से निकलती है।",
   "प्रायद्वीप की नदियों में कृष्णा के बाद इसका बेसिन दूसरा सबसे बड़ा है।",
   "इंद्रावती महानदी की सहायक नदी है।"],
  C3, 3,
  "None is correct; each statement borrows a fact from a neighbouring river. The Godavari rises at Trimbakeshwar near Nashik in the Western Ghats; Amarkantak is the source of the Narmada and the Son. Its basin, about a tenth of India's area across Maharashtra, Telangana, Chhattisgarh, Odisha and Andhra Pradesh, is the largest in the Peninsula, larger than the Krishna's. "
  "The Indravati, rising in Odisha and flowing through Bastar, is a Godavari tributary, along with the Pranhita, the Manjira and the Sabari.",
  "कोई भी कथन सही नहीं है; हर कथन किसी पड़ोसी नदी का तथ्य उधार लेता है। गोदावरी पश्चिमी घाट में नासिक के पास त्र्यंबकेश्वर से निकलती है; अमरकंटक नर्मदा और सोन का उद्गम है। महाराष्ट्र, तेलंगाना, छत्तीसगढ़, ओडिशा और आंध्र प्रदेश में फैला इसका बेसिन, भारत के क्षेत्रफल का लगभग दसवाँ भाग, प्रायद्वीप में सबसे बड़ा है, कृष्णा से बड़ा। "
  "ओडिशा से निकलकर बस्तर से बहने वाली इंद्रावती प्राणहिता, मंजीरा और सबरी के साथ गोदावरी की सहायक नदी है।",
  NI, "irv-godavari-source-basin", craft="precision")

S(RV, "medium", "Consider the following statements about the Indus Waters Treaty, 1960:",
  "सिंधु जल संधि, 1960 के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It allocated the waters of the Ravi, the Beas and the Satluj to India.",
   "It was brokered by the World Bank.",
   "India placed the treaty in abeyance in April 2025.",
   "Because the western rivers were given mainly to Pakistan, India's projects on them, such as Kishanganga and Ratle, had to be run-of-the-river plants with only limited storage."],
  ["इसने रावी, ब्यास और सतलुज का जल भारत को आवंटित किया।",
   "इसकी मध्यस्थता विश्व बैंक ने की।",
   "भारत ने अप्रैल 2025 में संधि को स्थगित कर दिया।",
   "चूँकि पश्चिमी नदियाँ मुख्यतः पाकिस्तान को दी गईं, इसलिए उन पर किशनगंगा और रतले जैसी भारत की परियोजनाओं को केवल सीमित भंडारण वाले नदी-प्रवाह (रन-ऑफ़-द-रिवर) संयंत्र होना पड़ा।"],
  C4, 3,
  "All four are correct. Signed at Karachi in 1960, with the World Bank as broker and a signatory, the treaty gave India the eastern rivers and gave the western rivers -- the Indus, the Jhelum and the Chenab -- mainly to Pakistan, while letting India use them for domestic needs, limited irrigation and run-of-the-river hydropower within strict limits on storage and on the design of spillways and outlets. "
  "Those limits are why Pakistan has repeatedly challenged Indian projects such as Kishanganga and Ratle before the treaty's neutral expert and court of arbitration. After the terrorist attack at Pahalgam in April 2025, India placed the treaty in abeyance.",
  "चारों कथन सही हैं। 1960 में कराची में हस्ताक्षरित इस संधि ने, जिसमें विश्व बैंक मध्यस्थ और हस्ताक्षरकर्ता था, पूर्वी नदियाँ भारत को और पश्चिमी नदियाँ, सिंधु, झेलम और चिनाब, मुख्यतः पाकिस्तान को दीं, पर भारत को उनका घरेलू आवश्यकताओं, सीमित सिंचाई और भंडारण तथा स्पिलवे और निकास की बनावट की कड़ी सीमाओं के भीतर नदी-प्रवाह जलविद्युत के लिए उपयोग करने दिया। "
  "इन्हीं सीमाओं के कारण पाकिस्तान ने किशनगंगा और रतले जैसी भारतीय परियोजनाओं को संधि के तटस्थ विशेषज्ञ और मध्यस्थता न्यायालय के सामने बार-बार चुनौती दी है। अप्रैल 2025 में पहलगाम आतंकी हमले के बाद भारत ने संधि को स्थगित कर दिया।",
  "Ministry of Jal Shakti -- Indus Waters Treaty, 1960.", "irv-indus-waters-treaty", craft="linkage")

S(RV, "medium", "Consider the following rivers:",
  "निम्नलिखित नदियों पर विचार कीजिए:",
  ["Kabini", "Hemavati", "Bhavani", "Amaravati", "Bhima"],
  ["काबिनी", "हेमावती", "भवानी", "अमरावती", "भीमा"],
  None, 2,
  "Only four -- the Kabini, the Hemavati, the Bhavani and the Amaravati. The Kaveri, rising at Talakaveri in Kodagu, gathers the Hemavati and the Kabini (from Wayanad) in Karnataka, and the Bhavani and the Amaravati from the Western Ghats in Tamil Nadu. "
  "The Bhima is the trap: it rises near Bhimashankar in the Sahyadri and is a major tributary of the Krishna, which it joins near Raichur.",
  "केवल चार -- काबिनी, हेमावती, भवानी और अमरावती। कोडगु के तलकावेरी से निकलने वाली कावेरी कर्नाटक में हेमावती और (वायनाड से आने वाली) काबिनी को, और तमिलनाडु में पश्चिमी घाट से आने वाली भवानी और अमरावती को समेटती है। "
  "भीमा जाल है: यह सह्याद्रि में भीमाशंकर के पास निकलती है और कृष्णा की प्रमुख सहायक नदी है, जिससे यह रायचूर के पास मिलती है।",
  NI, "irv-kaveri-source-kabini-shivasamudram", opts=FIVE, opts_hi=FIVE_HI,
  closing="How many of the above are tributaries of the Kaveri?", closing_hi="उपर्युक्त में से कितनी कावेरी की सहायक नदियाँ हैं?", craft="multi")

S(RV, "medium", "Consider the following statements about lakes of India:",
  "भारत की झीलों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Wular is the largest freshwater lake in India.",
   "Sambhar is a freshwater lake fed by the Luni.",
   "Pulicat lake is separated from the sea by Rameswaram island."],
  ["वुलर भारत की सबसे बड़ी मीठे पानी की झील है।",
   "सांभर लूणी से पोषित मीठे पानी की झील है।",
   "पुलिकट झील को रामेश्वरम द्वीप समुद्र से अलग करता है।"],
  C3, 0,
  "Only statement 1 is correct: Wular, in Jammu and Kashmir, is India's largest freshwater lake. Statement 2 is wrong: Sambhar, west of Jaipur, is India's largest inland saline lake and a major source of salt; it is fed by seasonal streams such as the Mendha and the Rupangarh, not by the Luni. "
  "Statement 3 is the near-miss: Pulicat, the second-largest brackish lagoon in India, on the Andhra Pradesh-Tamil Nadu border, is separated from the Bay of Bengal by Sriharikota island, home of the Satish Dhawan Space Centre; Rameswaram island lies far to the south, off the Palk Strait.",
  "केवल कथन 1 सही है: जम्मू और कश्मीर की वुलर भारत की सबसे बड़ी मीठे पानी की झील है। कथन 2 गलत है: जयपुर के पश्चिम में सांभर भारत की सबसे बड़ी अंतर्देशीय खारी झील और नमक का बड़ा स्रोत है; यह लूणी से नहीं, मेंढा और रूपनगढ़ जैसी मौसमी धाराओं से पोषित है। "
  "कथन 3 निकट-भ्रम है: आंध्र प्रदेश-तमिलनाडु सीमा पर भारत का दूसरा सबसे बड़ा खारा लैगून पुलिकट बंगाल की खाड़ी से श्रीहरिकोटा द्वीप द्वारा अलग है, जहाँ सतीश धवन अंतरिक्ष केंद्र है; रामेश्वरम द्वीप बहुत दक्षिण में, पाक जलडमरूमध्य के पास है।",
  NI, "irv-lakes-wular-sambhar-pulicat", craft="precision")

# ================================================================ TAGS for the 72 kept rows (Test 21's 3 are tagged already)
TAGS = {
 "igeo-peninsula-oldest-easy": "precision", "igeo-shimla-altitude-easy": "linkage", "igeo-aravalli-old-parallel-monsoon": "linkage",
 "igeo-coromandel-winter-rain": "linkage", "igeo-black-soil-self-ploughing": "linkage", "igeo-deccan-slope-east": "linkage",
 "igeo-himalaya-climatic-barrier": "linkage", "igeo-rainfall-east-west-plains": "inference", "igeo-western-disturbances-winter-rain": "linkage",
 "igeo-western-ghats-rain-shadow": "linkage", "igeo-plateaus-states-pairs-easy": "recall", "igeo-mawsynram-rainfall-reason": "linkage",
 "igeo-monsoon-covers-country-date": "recall", "igeo-western-ghats-order": "precision", "igeo-largest-division-peninsular-plateau": "recall",
 "igeo-longest-border-bangladesh": "recall", "igeo-october-heat": "precision", "igeo-purvanchal-garo-not": "precision",
 "igeo-rann-of-kachchh": "recall", "igeo-southernmost-indira-point": "precision", "igeo-tropic-of-cancer-not-odisha": "recall",
 "igeo-island-groups-easy": "recall", "igeo-rainy-season-kerala-onset-easy": "recall", "igeo-thar-kanchenjunga-easy": "recall",
 "igeo-forest-types-rainfall": "precision", "igeo-koppen-india": "precision", "igeo-monsoon-somali-jet-iod-trough": "precision",
 "igeo-trans-himalaya-karakoram": "precision", "igeo-coastal-plains-submerged-kayals": "precision", "igeo-himalaya-regional-divisions": "precision",
 "igeo-islands-barren-channels-saddle-peak": "precision", "igeo-location-meridian-extent": "inference", "igeo-monsoon-tibet-tej-el-nino": "linkage",
 "igeo-nepal-border-states": "multi", "igeo-northern-plains-bhabar-terai-khadar": "precision", "igeo-rainfall-rajasthan-leh-withdrawal": "linkage",
 "igeo-satpura-vindhya": "precision", "igeo-soils-black-laterite": "precision", "ugeo-western-eastern-ghats": "precision",
 "irv-western-ghats-waterfalls-easy": "linkage", "irv-assam-floods-silt": "linkage", "irv-mahi-tropic-twice": "precision",
 "irv-ganga-delta-national-river": "recall", "irv-himalayan-rivers-perennial": "linkage", "irv-kolleru-freshwater": "precision",
 "irv-ladakh-saline-lakes": "linkage", "irv-yamuna-prayagraj-yamunotri": "precision", "irv-lakes-states-pairs": "recall",
 "irv-waterfalls-rivers-pairs": "recall", "irv-longest-river-ganga-easy": "precision", "irv-bist-doab": "recall",
 "irv-jog-falls-sharavathi": "recall", "irv-largest-indus-tributary-chenab": "recall", "irv-longest-west-flowing-narmada": "recall",
 "irv-satluj-tibet": "recall", "irv-basin-water-divide-easy": "precision", "irv-kaveri-satluj-easy": "recall",
 "irv-oxbow-glacial-lakes-easy": "precision", "irv-sambhar-vembanad-easy": "recall", "irv-brahmaputra-tributaries": "recall",
 "irv-dams-tehri-bhakra-nagarjuna": "recall", "irv-ganga-basin-ramganga-haridwar": "recall", "irv-himalayan-vs-peninsular-rivers": "precision",
 "irv-peninsular-river-sources": "recall", "irv-brahmaputra-assam-jamuna-majuli": "recall", "irv-ganga-tributaries-kosi-gomti-ghaghara": "precision",
 "irv-indus-system-chenab-jhelum": "recall", "irv-ken-betwa-farakka": "precision", "irv-krishna-source-tungabhadra-delta": "recall",
 "irv-lakes-vembanad-lonar-loktak": "recall", "irv-west-flowing-sabarmati-periyar": "recall", "ugeo-peninsular-river-mouths": "precision"}

if __name__ == "__main__":
    write_updates("upg_l2_t13_igeo_b.sql", statuses=("draft", "published"), tags=TAGS)
