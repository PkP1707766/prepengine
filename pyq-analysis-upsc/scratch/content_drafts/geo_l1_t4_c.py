# -*- coding: utf-8 -*-
"""Level 1 · Test 4 (Geography, NCERT Foundation) -- part C: Indian Physiography, Climate & Regions (16) and
Oceanography & Hydrosphere (4) (upsc_l1_cell_targets.mjs 4).
India: easy MCQ 1, easy statement 2, easy Statement-I/II 1, medium MCQ 2, medium statement 5, medium Statement-I/II 2,
medium pairs 1, hard MCQ 1, hard statement 1. Oceans: easy statement 1, medium statement 1, hard pairs 2.
The angle is NCERT Contemporary India I (size and location, physical features, climate) and India: Physical
Environment (peaks, rainfall variability), and the ocean chapters of Fundamentals of Physical Geography.
Level-2 facts are not repeated: the Himalayan ranges and duns, Anamudi, the Ghats compared, the islands' origin and
the Ten Degree Channel, the Standard Meridian and the 30-degree extent, the Bay of Bengal cyclones of the retreating
monsoon, Kerala onset, local storms, the monsoon trough in July, soils, forests, currents, tides and salinity
averages. MCQ keys are pinned (pos)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Geography"
d.REQUIRE_CRAFT = True
IP = "Indian Physiography, Climate & Regions"
OC = "Oceanography & Hydrosphere"
CI1 = "NCERT Class IX, Geography -- Contemporary India I"
IPE = "NCERT Class XI, Geography -- India: Physical Environment"
FPG = "NCERT Class XI, Geography -- Fundamentals of Physical Geography"

# ================================================================ INDIA (16)
# ---------------------------------------------------------------- easy MCQ (1)
M(IP, "easy", "The word 'monsoon' is derived from the Arabic word 'mausim', which means",
  "'मानसून' शब्द अरबी शब्द 'मौसिम' से बना है, जिसका अर्थ है",
  ["season", "rainfall", "sea wind", "thunderstorm"],
  ["ऋतु", "वर्षा", "समुद्री हवा", "तड़ित-झंझा"],
  0,
  "'Mausim' means season, and 'monsoon' refers to the seasonal reversal in the direction of the winds during a year. "
  "Arab sailors, who used these regularly reversing winds to cross the Arabian Sea, gave them the name; the rain they bring to India in summer came to be called the monsoon only later.",
  "'मौसिम' का अर्थ है ऋतु, और 'मानसून' वर्ष के दौरान हवाओं की दिशा के मौसमी उलटाव को कहते हैं। "
  "नियमित रूप से दिशा बदलने वाली इन हवाओं के सहारे अरब सागर पार करने वाले अरब नाविकों ने इन्हें यह नाम दिया; गर्मियों में भारत में इनके द्वारा लाई जाने वाली वर्षा बाद में मानसून कहलाने लगी।",
  f"{CI1} (Climate).",
  "l1-geo-monsoon-mausim-season", pos=2, craft="recall")

# ---------------------------------------------------------------- easy statement (2)
S(IP, "easy", "Consider the following statements about the Lakshadweep islands:",
  "लक्षद्वीप द्वीपों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Kavaratti island is the administrative headquarters of Lakshadweep.",
   "The uninhabited Pitti island has a bird sanctuary.",
   "The group, earlier known as the Laccadive, Minicoy and Amindivi islands, was renamed Lakshadweep in 1973."],
  ["कवरत्ती द्वीप लक्षद्वीप का प्रशासनिक मुख्यालय है।",
   "निर्जन पिट्टी द्वीप पर एक पक्षी अभयारण्य है।",
   "पहले लक्कादीव, मिनिकॉय और अमीनदीवी द्वीप कहलाने वाले इस समूह का नाम 1973 में लक्षद्वीप रखा गया।"],
  C3, 2,
  "All three statements are correct. The Lakshadweep group lies close to the Malabar coast of Kerala and covers a small area of about 32 sq km. "
  "It has a great diversity of flora and fauna; Pitti, which no one lives on, is kept as a sanctuary for sea birds.",
  "तीनों कथन सही हैं। लक्षद्वीप समूह केरल के मालाबार तट के निकट है और लगभग 32 वर्ग किमी के छोटे क्षेत्र में फैला है। "
  "यहाँ वनस्पतियों और जीवों की बड़ी विविधता है; पिट्टी, जहाँ कोई नहीं रहता, समुद्री पक्षियों के अभयारण्य के रूप में सुरक्षित है।",
  f"{CI1} (Physical Features of India).",
  "l1-geo-lakshadweep-kavaratti-pitti", craft="recall")

S(IP, "easy", "Consider the following statements about the Himalaya:",
  "हिमालय के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["They form an arc about 2,400 km long, running west to east from the Indus to the Brahmaputra.",
   "Their width is greatest in Arunachal Pradesh, about 400 km, and least in Kashmir, about 150 km.",
   "Their altitudinal variations are greater in the eastern half than in the western half."],
  ["वे लगभग 2,400 किमी लंबा चाप बनाते हैं, जो पश्चिम से पूर्व सिंधु से ब्रह्मपुत्र तक फैला है।",
   "उनकी चौड़ाई अरुणाचल प्रदेश में सबसे अधिक, लगभग 400 किमी, और कश्मीर में सबसे कम, लगभग 150 किमी, है।",
   "उनकी ऊँचाई में अंतर पश्चिमी आधे भाग की अपेक्षा पूर्वी आधे भाग में अधिक है।"],
  C3, 1,
  "Statements 1 and 3 are correct: the Himalaya, geologically young fold mountains, are among the loftiest and most rugged mountain barriers in the world, and in the east the land climbs from the plains to the high peaks over a much shorter distance. "
  "Statement 2 reverses the facts: the width is about 400 km in Kashmir and narrows to about 150 km in Arunachal Pradesh.",
  "कथन 1 और 3 सही हैं: भूगर्भिक रूप से नवीन वलित पर्वत, हिमालय, विश्व की सबसे ऊँची और सबसे दुर्गम पर्वतीय बाधाओं में हैं, और पूर्व में भूमि मैदानों से ऊँची चोटियों तक कहीं कम दूरी में चढ़ जाती है। "
  "कथन 2 तथ्यों को उलट देता है: चौड़ाई कश्मीर में लगभग 400 किमी है और अरुणाचल प्रदेश में घटकर लगभग 150 किमी रह जाती है।",
  f"{CI1} (Physical Features of India).",
  "l1-geo-himalaya-width-arc", craft="precision")

# ---------------------------------------------------------------- easy Statement-I/II (1)
A(IP, "easy",
  "The southern Peninsula of India has no well-defined cold season.",
  "भारत के दक्षिणी प्रायद्वीप में कोई सुस्पष्ट शीत ऋतु नहीं होती।",
  "The sea, which surrounds the Peninsula on three sides, has a moderating influence on its temperatures.",
  "तीन ओर से प्रायद्वीप को घेरने वाला समुद्र उसके तापमान पर समकारी (moderating) प्रभाव डालता है।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I. Because of the sea's moderating influence, and the region's nearness to the Equator, there is hardly any noticeable seasonal change in the temperature pattern of the Peninsula in winter: Chennai on the east coast has a mean January temperature of about 24-25 degrees Celsius, "
  "while over most of northern India the mean daily temperature then stays below 21 degrees and frost can occur.",
  "दोनों कथन सही हैं, और कथन-II कथन-I की व्याख्या करता है। समुद्र के समकारी प्रभाव और विषुवत रेखा से निकटता के कारण सर्दियों में प्रायद्वीप के तापमान प्रतिरूप में शायद ही कोई उल्लेखनीय मौसमी परिवर्तन होता है: पूर्वी तट पर चेन्नई का जनवरी का औसत तापमान लगभग 24-25 डिग्री सेल्सियस रहता है, "
  "जबकि उत्तरी भारत के अधिकांश भाग में तब औसत दैनिक तापमान 21 डिग्री से नीचे रहता है और पाला पड़ सकता है।",
  f"{CI1} (Climate).",
  "l1-geo-peninsula-no-cold-season", craft="inference")

# ---------------------------------------------------------------- medium MCQ (2)
M(IP, "medium", "Which one of the following is the highest peak of the Eastern Ghats?",
  "निम्नलिखित में से कौन-सी पूर्वी घाट की सबसे ऊँची चोटी है?",
  ["Mahendragiri, in Odisha", "Anai Mudi, in Kerala", "Doddabetta, in Tamil Nadu", "Kudremukh, in Karnataka"],
  ["महेंद्रगिरि, ओडिशा में", "अनाई मुडी, केरल में", "डोडाबेटा, तमिलनाडु में", "कुद्रेमुख, कर्नाटक में"],
  0,
  "Mahendragiri, at about 1,501 m, is the highest peak of the Eastern Ghats, which are discontinuous and have been cut through by the rivers flowing into the Bay of Bengal. "
  "The other three are Western Ghats peaks: Kudremukh in Karnataka, Doddabetta in the Nilgiris and Anai Mudi in the Anaimalai hills, the highest of all in Peninsular India -- the Western Ghats rise steadily higher from north to south.",
  "लगभग 1,501 मीटर ऊँचा महेंद्रगिरि पूर्वी घाट की सबसे ऊँची चोटी है; पूर्वी घाट असतत हैं और बंगाल की खाड़ी में गिरने वाली नदियों ने उन्हें जगह-जगह काट दिया है। "
  "शेष तीनों पश्चिमी घाट की चोटियाँ हैं: कर्नाटक में कुद्रेमुख, नीलगिरि में डोडाबेटा और अन्नामलाई पहाड़ियों में अनाई मुडी, जो प्रायद्वीपीय भारत में सबसे ऊँची है -- पश्चिमी घाट उत्तर से दक्षिण की ओर लगातार ऊँचे होते जाते हैं।",
  f"{IPE} (Structure and Physiography).",
  "l1-geo-mahendragiri-eastern-ghats", pos=0, craft="precision")

M(IP, "medium", "The monsoon depressions that bring much of the rain to the northern plains during the rainy season generally form over",
  "वर्षा ऋतु में उत्तरी मैदानों में अधिकांश वर्षा लाने वाले मानसूनी अवदाब (depressions) सामान्यतः कहाँ बनते हैं?",
  ["the head of the Bay of Bengal", "the Arabian Sea off the Gujarat coast", "the Gulf of Mannar", "the Thar desert"],
  ["बंगाल की खाड़ी के शीर्ष पर", "गुजरात तट के पास अरब सागर में", "मन्नार की खाड़ी में", "थार मरुस्थल पर"],
  0,
  "The tropical depressions of the monsoon season form at the head of the Bay of Bengal and cross over to the mainland, following the axis of the monsoon trough of low pressure up the Ganga plain. "
  "Their frequency and intensity help decide the amount and duration of monsoon rain, which is one reason the rain decreases from east to west along the plains.",
  "मानसून ऋतु के उष्णकटिबंधीय अवदाब बंगाल की खाड़ी के शीर्ष पर बनते हैं और मुख्य भूमि पर आकर कम वायुदाब की मानसून द्रोणी (trough) की अक्ष के साथ गंगा के मैदान में ऊपर की ओर बढ़ते हैं। "
  "उनकी आवृत्ति और तीव्रता मानसूनी वर्षा की मात्रा और अवधि तय करने में सहायक होती है, यह भी एक कारण है कि मैदानों में वर्षा पूर्व से पश्चिम की ओर घटती है।",
  f"{CI1} (Climate).",
  "l1-geo-monsoon-depressions-bay-head", pos=3, craft="recall")

# ---------------------------------------------------------------- medium statement (5)
S(IP, "medium", "Consider the following statements about contrasts in India's climate:",
  "भारत की जलवायु के विरोधाभासों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["In summer, temperatures in parts of the Rajasthan desert can touch 50°C, while Pahalgam in Kashmir may be around 20°C.",
   "In winter, the temperature at Dras in Ladakh may fall to about minus 45°C, while Thiruvananthapuram may be around 22°C.",
   "In the upper reaches of the Himalaya, most precipitation falls as rain rather than snow."],
  ["गर्मियों में राजस्थान मरुस्थल के कुछ भागों में तापमान 50°C तक पहुँच सकता है, जबकि कश्मीर के पहलगाम में यह लगभग 20°C हो सकता है।",
   "सर्दियों में लद्दाख के द्रास में तापमान लगभग शून्य से 45°C नीचे तक गिर सकता है, जबकि तिरुवनंतपुरम में यह लगभग 22°C हो सकता है।",
   "हिमालय के ऊपरी भागों में अधिकांश वर्षण हिम के बजाय वर्षा के रूप में होता है।"],
  C3, 1,
  "Statements 1 and 2 are correct: they show how latitude, altitude and distance from the sea together give India very different climates within one monsoon type. "
  "Statement 3 is wrong: the upper parts of the Himalaya receive precipitation mostly as snowfall, while the rest of the country receives it as rain.",
  "कथन 1 और 2 सही हैं: वे दिखाते हैं कि अक्षांश, ऊँचाई और समुद्र से दूरी मिलकर एक ही मानसूनी प्रकार के भीतर भारत को बहुत भिन्न जलवायु देते हैं। "
  "कथन 3 गलत है: हिमालय के ऊपरी भागों में वर्षण अधिकतर हिमपात के रूप में होता है, जबकि देश के शेष भाग में वर्षा के रूप में।",
  f"{CI1} (Climate).",
  "l1-geo-climate-contrasts-dras-pahalgam", craft="application")

S(IP, "medium", "Consider the following statements about 'breaks' in the monsoon:",
  "मानसून में 'विराम' (breaks) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Breaks in the monsoon are caused mainly by the arrival of western disturbances.",
   "When the axis of the monsoon trough lies over the plains, rainfall in the plains is good.",
   "When the axis shifts close to the Himalaya, the plains get longer dry spells, while heavy rain in the mountain catchments can bring floods to the plains."],
  ["मानसून में विराम मुख्यतः पश्चिमी विक्षोभों के आगमन से होते हैं।",
   "जब मानसून द्रोणी की अक्ष मैदानों के ऊपर होती है, तब मैदानों में अच्छी वर्षा होती है।",
   "जब अक्ष हिमालय के निकट खिसक जाती है, तब मैदानों में लंबे शुष्क दौर आते हैं, जबकि पर्वतीय जलग्रहण क्षेत्रों में भारी वर्षा मैदानों में बाढ़ ला सकती है।"],
  C3, 1,
  "Statements 2 and 3 are correct. Monsoon rain falls for a few days at a time, with rainless intervals in between, and these breaks are related to the movement of the monsoon trough, which keeps shifting north or south and so decides where the rain falls. "
  "Statement 1 is wrong: western disturbances are winter systems from the Mediterranean region that bring rain and snow to north-western India; they do not cause the monsoon breaks.",
  "कथन 2 और 3 सही हैं। मानसूनी वर्षा कुछ दिनों तक होती है, फिर बीच में वर्षाहीन अंतराल आते हैं, और ये विराम मानसून द्रोणी की गति से जुड़े हैं, जो उत्तर या दक्षिण की ओर खिसकती रहती है और इसी से तय होता है कि वर्षा कहाँ होगी। "
  "कथन 1 गलत है: पश्चिमी विक्षोभ भूमध्यसागरीय क्षेत्र से आने वाले शीतकालीन तंत्र हैं, जो उत्तर-पश्चिमी भारत में वर्षा और हिमपात लाते हैं; वे मानसून के विराम का कारण नहीं हैं।",
  f"{CI1} (Climate).",
  "l1-geo-monsoon-breaks-trough-axis", craft="inference")

S(IP, "medium", "Consider the following statements about India's size and location:",
  "भारत के आकार और स्थिति के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["India is the seventh largest country in the world by area.",
   "India's area is about 2.4 per cent of the total geographical area of the world.",
   "Since the opening of the Suez Canal in 1869, India's distance from Europe has been reduced by about 7,000 km.",
   "India's land boundary, about 15,200 km, is roughly twice the length of its coastline including the islands."],
  ["क्षेत्रफल की दृष्टि से भारत विश्व का सातवाँ सबसे बड़ा देश है।",
   "भारत का क्षेत्रफल विश्व के कुल भौगोलिक क्षेत्रफल का लगभग 2.4 प्रतिशत है।",
   "1869 में स्वेज़ नहर खुलने के बाद से यूरोप से भारत की दूरी लगभग 7,000 किमी कम हो गई है।",
   "भारत की लगभग 15,200 किमी लंबी स्थल सीमा द्वीपों सहित उसकी तटरेखा की लगभग दोगुनी है।"],
  C4, 3,
  "All four statements are correct. India's 3.28 million sq km make it the seventh largest country; its mainland coastline with the Andaman and Nicobar and Lakshadweep islands measures about 7,516.6 km, roughly half its land frontier. "
  "Lying at the centre of the trans-Indian Ocean routes between Europe in the west and East Asia, India gained greatly from the shorter sea route that the Suez Canal opened.",
  "चारों कथन सही हैं। 32.8 लाख वर्ग किमी क्षेत्रफल भारत को सातवाँ सबसे बड़ा देश बनाता है; अंडमान-निकोबार और लक्षद्वीप सहित मुख्य भूमि की तटरेखा लगभग 7,516.6 किमी है, यानी स्थल सीमा की लगभग आधी। "
  "पश्चिम में यूरोप और पूर्वी एशिया के बीच हिंद महासागर के आर-पार के मार्गों के केंद्र में स्थित भारत को स्वेज़ नहर से खुले छोटे समुद्री मार्ग से बहुत लाभ हुआ।",
  f"{CI1} (India -- Size and Location).",
  "l1-geo-india-size-suez-boundary", craft="recall")

S(IP, "medium", "Consider the following statements about the mechanism of India's climate:",
  "भारत की जलवायु की क्रियाविधि के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["In summer, the Indian landmass develops low pressure, while the surrounding seas have relatively high pressure.",
   "In winter, the landmass has lower pressure than the surrounding seas, so the winds blow from sea to land.",
   "The Indian monsoon is unaffected by pressure conditions south of the Equator."],
  ["गर्मियों में भारतीय भूभाग पर निम्न वायुदाब बनता है, जबकि आसपास के समुद्रों पर अपेक्षाकृत उच्च वायुदाब रहता है।",
   "सर्दियों में भूभाग पर आसपास के समुद्रों से कम वायुदाब होता है, इसलिए हवाएँ समुद्र से स्थल की ओर बहती हैं।",
   "भारतीय मानसून विषुवत रेखा के दक्षिण की वायुदाब दशाओं से अप्रभावित रहता है।"],
  C3, 0,
  "Only statement 1 is correct: the differential heating of land and sea draws the moist winds of the south-west monsoon towards the hot landmass. "
  "Statement 2 is wrong: in winter the land is colder, high pressure develops over northern India, and the north-east winds blow from land to sea, which is why most of the country is dry then. "
  "Statement 3 is wrong: the intensity and position of a high-pressure area east of Madagascar, at about 20 degrees south over the Indian Ocean, affect the monsoon, and the Southern Oscillation links Indian rainfall to pressure changes across the Pacific.",
  "केवल कथन 1 सही है: स्थल और समुद्र के असमान गर्म होने से दक्षिण-पश्चिम मानसून की नम हवाएँ गर्म भूभाग की ओर खिंचती हैं। "
  "कथन 2 गलत है: सर्दियों में स्थल ठंडा होता है, उत्तरी भारत पर उच्च वायुदाब बनता है, और उत्तर-पूर्वी हवाएँ स्थल से समुद्र की ओर बहती हैं, इसीलिए तब देश का अधिकांश भाग शुष्क रहता है। "
  "कथन 3 गलत है: हिंद महासागर में लगभग 20 डिग्री दक्षिण पर मेडागास्कर के पूर्व स्थित उच्च वायुदाब क्षेत्र की तीव्रता और स्थिति मानसून को प्रभावित करती है, और दक्षिणी दोलन (Southern Oscillation) भारतीय वर्षा को प्रशांत महासागर के वायुदाब परिवर्तनों से जोड़ता है।",
  f"{CI1} (Climate).",
  "l1-geo-monsoon-pressure-madagascar", craft="inference")

S(IP, "medium", "Consider the following statements about the Northern Plains of India:",
  "भारत के उत्तरी मैदानों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The larger part of the Punjab plains, formed by the Indus and its tributaries, lies in Pakistan.",
   "The Ganga plain extends between the Ghaggar and the Teesta rivers.",
   "The Brahmaputra plain lies mainly in West Bengal."],
  ["सिंधु और उसकी सहायक नदियों से बने पंजाब के मैदानों का बड़ा भाग पाकिस्तान में है।",
   "गंगा का मैदान घग्घर और तीस्ता नदियों के बीच फैला है।",
   "ब्रह्मपुत्र का मैदान मुख्यतः पश्चिम बंगाल में है।"],
  C3, 1,
  "Statements 1 and 2 are correct. The Northern Plain, about 2,400 km long and 240-320 km broad, falls into three sections: the Punjab plains in the west, dominated by doabs; the Ganga plain, spread over Haryana, Delhi, Uttar Pradesh, Bihar, part of Jharkhand and West Bengal; "
  "and, to its east, the Brahmaputra plain. Statement 3 is wrong: the Brahmaputra plain lies mainly in Assam.",
  "कथन 1 और 2 सही हैं। लगभग 2,400 किमी लंबा और 240-320 किमी चौड़ा उत्तरी मैदान तीन भागों में बँटता है: पश्चिम में दोआबों से भरे पंजाब के मैदान; हरियाणा, दिल्ली, उत्तर प्रदेश, बिहार, झारखंड के कुछ भाग और पश्चिम बंगाल में फैला गंगा का मैदान; "
  "और उसके पूर्व में ब्रह्मपुत्र का मैदान। कथन 3 गलत है: ब्रह्मपुत्र का मैदान मुख्यतः असम में है।",
  f"{CI1} (Physical Features of India).",
  "l1-geo-northern-plains-three-sections", craft="precision")

# ---------------------------------------------------------------- medium Statement-I/II (2)
A(IP, "medium",
  "The Chambal, the Sind, the Betwa and the Ken flow from south-west to north-east.",
  "चंबल, सिंध, बेतवा और केन दक्षिण-पश्चिम से उत्तर-पूर्व की ओर बहती हैं।",
  "The Central Highlands, which these rivers drain, slope generally towards the north-east.",
  "ये नदियाँ जिन मध्य उच्चभूमियों (Central Highlands) को अपवाहित करती हैं, उनका ढाल सामान्यतः उत्तर-पूर्व की ओर है।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I: rivers follow the slope of the land, and the direction of these rivers is itself the evidence NCERT gives for the slope of the Central Highlands. "
  "The Central Highlands, north of the Narmada, are wider in the west and narrower in the east; their eastward extensions are known locally as Bundelkhand and Baghelkhand, and the Chotanagpur plateau beyond is drained by the Damodar.",
  "दोनों कथन सही हैं, और कथन-II कथन-I की व्याख्या करता है: नदियाँ भूमि के ढाल का अनुसरण करती हैं, और इन नदियों की दिशा ही वह प्रमाण है जो NCERT मध्य उच्चभूमियों के ढाल के लिए देता है। "
  "नर्मदा के उत्तर में स्थित मध्य उच्चभूमियाँ पश्चिम में चौड़ी और पूर्व में सँकरी हैं; उनके पूर्वी विस्तार स्थानीय रूप से बुंदेलखंड और बघेलखंड कहलाते हैं, और आगे छोटानागपुर पठार को दामोदर अपवाहित करती है।",
  f"{CI1} (Physical Features of India).",
  "l1-geo-central-highlands-ne-slope", craft="application")

A(IP, "medium",
  "Tripura shares a land border with Myanmar.",
  "त्रिपुरा की स्थल सीमा म्यांमार से लगती है।",
  "Mizoram shares land borders with both Myanmar and Bangladesh.",
  "मिज़ोरम की स्थल सीमाएँ म्यांमार और बांग्लादेश दोनों से लगती हैं।",
  3,
  "Statement-I is incorrect but Statement-II is correct. Tripura is bounded by Bangladesh on three sides, and by Assam and Mizoram on the east; it does not touch Myanmar. "
  "The four States along the Myanmar border are Arunachal Pradesh, Nagaland, Manipur and Mizoram, and Mizoram, wedged between Myanmar and Bangladesh, borders both countries.",
  "कथन-I गलत है, पर कथन-II सही है। त्रिपुरा तीन ओर से बांग्लादेश से, और पूर्व में असम तथा मिज़ोरम से घिरा है; यह म्यांमार को नहीं छूता। "
  "म्यांमार सीमा पर स्थित चार राज्य अरुणाचल प्रदेश, नागालैंड, मणिपुर और मिज़ोरम हैं, और म्यांमार तथा बांग्लादेश के बीच स्थित मिज़ोरम की सीमा दोनों देशों से लगती है।",
  f"{CI1} (India -- Size and Location).",
  "l1-geo-tripura-mizoram-myanmar-border", craft="precision")

# ---------------------------------------------------------------- medium pairs (1)
P(IP, "medium", "Consider the following pairs of peaks and their locations:",
  "चोटियों और उनके स्थानों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Kamet : Garhwal Himalaya, Uttarakhand",
   "Namcha Barwa : near the great U-turn of the Brahmaputra, at the eastern end of the Himalaya",
   "Dhupgarh : highest peak of the Satpura range, near Pachmarhi",
   "Nanda Devi : Sikkim Himalaya"],
  ["कामेट : गढ़वाल हिमालय, उत्तराखंड",
   "नामचा बरवा : हिमालय के पूर्वी छोर पर, ब्रह्मपुत्र के बड़े U-मोड़ के निकट",
   "धूपगढ़ : सतपुड़ा श्रेणी की सबसे ऊँची चोटी, पचमढ़ी के निकट",
   "नंदा देवी : सिक्किम हिमालय"],
  2,
  "Pairs 1, 2 and 3 are correctly matched. Kamet stands in the Garhwal Himalaya; the Tsangpo, flowing east through Tibet, takes a sharp U-turn around Namcha Barwa and enters India as the Dihang; and Dhupgarh, about 1,350 m, rises on the Mahadeo hills near Pachmarhi in Madhya Pradesh. "
  "Pair 4 is wrong: Nanda Devi, the highest peak lying wholly in India, is in the Kumaon-Garhwal Himalaya of Uttarakhand, not in Sikkim.",
  "युग्म 1, 2 और 3 सही सुमेलित हैं। कामेट गढ़वाल हिमालय में है; तिब्बत में पूर्व की ओर बहने वाली सांगपो नामचा बरवा के चारों ओर तीखा U-मोड़ लेकर दिहांग के रूप में भारत में प्रवेश करती है; और लगभग 1,350 मीटर ऊँचा धूपगढ़ मध्य प्रदेश में पचमढ़ी के निकट महादेव पहाड़ियों पर है। "
  "युग्म 4 गलत है: पूरी तरह भारत में स्थित सबसे ऊँची चोटी, नंदा देवी, सिक्किम में नहीं, उत्तराखंड के कुमाऊँ-गढ़वाल हिमालय में है।",
  f"{IPE} (Structure and Physiography; Drainage System).",
  "l1-geo-peaks-kamet-namcha-dhupgarh-pairs", craft="precision")

# ---------------------------------------------------------------- hard MCQ (1)
M(IP, "hard", "The Eight Degree Channel separates",
  "आठ डिग्री चैनल किन्हें अलग करता है?",
  ["Minicoy from the Maldives", "the Andaman group from the Nicobar group", "Minicoy from the main Lakshadweep group", "Great Nicobar from Sumatra"],
  ["मिनिकॉय को मालदीव से", "अंडमान समूह को निकोबार समूह से", "मिनिकॉय को मुख्य लक्षद्वीप समूह से", "ग्रेट निकोबार को सुमात्रा से"],
  0,
  "The Eight Degree Channel, near 8 degrees north in the Arabian Sea, separates Minicoy, India's southernmost island in the Lakshadweep group, from the Maldives. "
  "The Nine Degree Channel separates Minicoy from the main Lakshadweep islands to its north, the Ten Degree Channel in the Bay of Bengal separates the Andaman group from the Nicobar group, and the Great (Six Degree) Channel lies between Great Nicobar and Sumatra in Indonesia.",
  "अरब सागर में लगभग 8 डिग्री उत्तर पर स्थित आठ डिग्री चैनल लक्षद्वीप समूह में भारत के सबसे दक्षिणी द्वीप मिनिकॉय को मालदीव से अलग करता है। "
  "नौ डिग्री चैनल मिनिकॉय को उसके उत्तर के मुख्य लक्षद्वीप द्वीपों से अलग करता है, बंगाल की खाड़ी में दस डिग्री चैनल अंडमान समूह को निकोबार समूह से अलग करता है, और ग्रेट (छह डिग्री) चैनल ग्रेट निकोबार और इंडोनेशिया के सुमात्रा के बीच है।",
  f"{IPE} (Structure and Physiography).",
  "l1-geo-eight-degree-channel-minicoy", pos=0, craft="precision")

# ---------------------------------------------------------------- hard statement (1)
S(IP, "hard", "Consider the following statements about the variability of rainfall in India:",
  "भारत में वर्षा की परिवर्तनशीलता के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The coefficient of variation used to measure it is the mean annual rainfall divided by the standard deviation.",
   "Regions with more than 100 cm of annual rainfall, such as the western coast, generally show a variability above 50 per cent.",
   "The interior of the Deccan plateau has a variability of less than 25 per cent."],
  ["इसे मापने में प्रयुक्त विचरण गुणांक (coefficient of variation) औसत वार्षिक वर्षा को मानक विचलन से भाग देकर निकलता है।",
   "100 सेमी से अधिक वार्षिक वर्षा वाले क्षेत्र, जैसे पश्चिमी तट, सामान्यतः 50 प्रतिशत से अधिक परिवर्तनशीलता दिखाते हैं।",
   "दक्कन पठार के आंतरिक भाग में परिवर्तनशीलता 25 प्रतिशत से कम है।"],
  C3, 3,
  "None of the statements is correct. The coefficient of variation is the standard deviation divided by the mean, multiplied by 100. Variability runs inversely to the amount of rain: it is below 25 per cent on the western coast, the Western Ghats, the north-eastern Peninsula, the eastern Ganga plain and the North-East, which get over 100 cm, "
  "and above 50 per cent in western Rajasthan, northern Jammu and Kashmir and the interior of the Deccan plateau, which get less than 50 cm -- so the driest areas are also the least dependable, and the most prone to drought.",
  "कोई भी कथन सही नहीं है। विचरण गुणांक मानक विचलन को माध्य से भाग देकर 100 से गुणा करने पर निकलता है। परिवर्तनशीलता वर्षा की मात्रा के विपरीत चलती है: 100 सेमी से अधिक वर्षा पाने वाले पश्चिमी तट, पश्चिमी घाट, उत्तर-पूर्वी प्रायद्वीप, पूर्वी गंगा मैदान और पूर्वोत्तर में यह 25 प्रतिशत से कम है, "
  "और 50 सेमी से कम वर्षा पाने वाले पश्चिमी राजस्थान, उत्तरी जम्मू-कश्मीर और दक्कन पठार के आंतरिक भाग में 50 प्रतिशत से अधिक -- इसलिए सबसे शुष्क क्षेत्र ही सबसे अनिश्चित और सूखे के प्रति सबसे संवेदनशील हैं।",
  f"{IPE} (Climate).",
  "l1-geo-rainfall-variability-cv", craft="multi")

# ================================================================ OCEANS (4)
# ---------------------------------------------------------------- easy statement (1)
S(OC, "easy", "Consider the following statements about the temperature of ocean water:",
  "महासागरीय जल के तापमान के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The temperature of surface water generally decreases from the Equator towards the poles.",
   "Oceans in the Northern Hemisphere receive more heat than those in the Southern Hemisphere, because they are in contact with a larger extent of land."],
  ["सतही जल का तापमान सामान्यतः विषुवत रेखा से ध्रुवों की ओर घटता है।",
   "उत्तरी गोलार्ध के महासागर दक्षिणी गोलार्ध के महासागरों से अधिक ऊष्मा पाते हैं, क्योंकि वे अधिक विस्तृत स्थल के संपर्क में हैं।"],
  T2, 2,
  "Both statements are correct. The average temperature of surface water is about 27 degrees Celsius, falling with latitude as the insolation weakens; the highest temperatures are recorded slightly north of the Equator rather than on it. "
  "Prevailing winds, ocean currents and the land around a sea also matter: enclosed seas in low latitudes are warmer than the open oceans.",
  "दोनों कथन सही हैं। सतही जल का औसत तापमान लगभग 27 डिग्री सेल्सियस है, जो सूर्यातप के कमज़ोर पड़ने से अक्षांश के साथ घटता है; सबसे ऊँचे तापमान ठीक विषुवत रेखा पर नहीं, उसके थोड़ा उत्तर में दर्ज होते हैं। "
  "प्रचलित पवनें, महासागरीय धाराएँ और समुद्र के आसपास का स्थल भी असर डालते हैं: निम्न अक्षांशों के घिरे हुए समुद्र खुले महासागरों से अधिक गर्म होते हैं।",
  f"{FPG} (Water (Oceans)).",
  "l1-geo-ocean-temperature-latitude-land", craft="recall")

# ---------------------------------------------------------------- medium statement (1)
S(OC, "medium", "Consider the following statements about the vertical temperature structure of the oceans:",
  "महासागरों की ऊर्ध्वाधर तापीय संरचना के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["In low latitudes, the top layer of warm water is about 500 m thick, with temperatures of about 20°-25°C.",
   "Below it lies the thermocline, a layer in which temperature falls rapidly with increasing depth.",
   "Near the poles, the oceans show the same three layers as in the tropics."],
  ["निम्न अक्षांशों में गर्म जल की ऊपरी परत लगभग 500 मीटर मोटी होती है, जिसका तापमान लगभग 20°-25°C होता है।",
   "उसके नीचे ताप-प्रवणता परत (thermocline) है, जिसमें गहराई बढ़ने के साथ तापमान तेज़ी से गिरता है।",
   "ध्रुवों के निकट महासागरों में भी उष्ण कटिबंध जैसी तीनों परतें मिलती हैं।"],
  C3, 1,
  "Statements 1 and 2 are correct: over the middle and low latitudes the ocean is a three-layer system -- a warm surface layer, a thermocline 500-1,000 m thick, and a very cold layer reaching down to the ocean floor; in mid-latitudes the warm top layer develops only in summer. "
  "Statement 3 is wrong: within the Arctic and Antarctic circles the surface water is close to 0 degrees Celsius, so temperature changes very little with depth and only one layer of cold water exists.",
  "कथन 1 और 2 सही हैं: मध्य और निम्न अक्षांशों पर महासागर त्रि-स्तरीय तंत्र है -- एक गर्म सतही परत, 500-1,000 मीटर मोटी ताप-प्रवणता परत, और समुद्र तल तक जाने वाली बहुत ठंडी परत; मध्य अक्षांशों में गर्म ऊपरी परत केवल गर्मियों में बनती है। "
  "कथन 3 गलत है: आर्कटिक और अंटार्कटिक वृत्तों के भीतर सतही जल लगभग 0 डिग्री सेल्सियस होता है, इसलिए गहराई के साथ तापमान बहुत कम बदलता है और ठंडे जल की केवल एक परत होती है।",
  f"{FPG} (Water (Oceans)).",
  "l1-geo-ocean-three-layers-thermocline", craft="precision")

# ---------------------------------------------------------------- hard pairs (2)
P(OC, "hard", "Consider the following pairs of relief features of the ocean floor and their descriptions:",
  "समुद्र तल की उच्चावच आकृतियों और उनके विवरणों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Guyot : a flat-topped seamount",
   "Atoll : low islands of coral reefs surrounding a central depression",
   "Submarine canyon : a deep valley cutting across the continental shelf and slope",
   "Seamount : a mountain with a pointed summit that rises above the sea surface as an island"],
  ["गायट (Guyot) : सपाट शीर्ष वाला समुद्री पर्वत (seamount)",
   "एटॉल : किसी केंद्रीय गर्त को घेरे प्रवाल भित्तियों के निचले द्वीप",
   "अंतःसागरीय कैनियन : महाद्वीपीय मग्नतट और ढाल को काटने वाली गहरी घाटी",
   "समुद्री पर्वत (Seamount) : नुकीले शिखर वाला पर्वत जो द्वीप के रूप में समुद्र सतह से ऊपर उठता है"],
  2,
  "Pairs 1, 2 and 3 are correctly matched. Guyots show stages of subsidence, as flat-topped seamounts sink slowly; atolls are found in tropical oceans, their reefs ringing a lagoon; and submarine canyons, some as large as the Grand Canyon, often begin at the mouths of large rivers -- the Hudson Canyon is the best known. "
  "Pair 4 is wrong: a seamount, volcanic in origin and 3,000-4,500 m tall, rises from the sea floor but does not reach the surface of the ocean; the Emperor seamount chain, an extension of the Hawaiian Islands, is an example.",
  "युग्म 1, 2 और 3 सही सुमेलित हैं। गायट धीरे-धीरे धँसते सपाट शीर्ष वाले समुद्री पर्वतों के अवतलन की अवस्थाएँ दिखाते हैं; एटॉल उष्णकटिबंधीय महासागरों में मिलते हैं, जिनकी भित्तियाँ किसी लैगून को घेरे रहती हैं; और अंतःसागरीय कैनियन, जिनमें कुछ ग्रैंड कैनियन जितने बड़े हैं, प्रायः बड़ी नदियों के मुहानों से आरंभ होते हैं -- हडसन कैनियन सबसे प्रसिद्ध है। "
  "युग्म 4 गलत है: ज्वालामुखी से बना, 3,000-4,500 मीटर ऊँचा समुद्री पर्वत समुद्र तल से उठता है, पर महासागर की सतह तक नहीं पहुँचता; हवाई द्वीपों का विस्तार, एम्परर समुद्री पर्वत शृंखला, इसका उदाहरण है।",
  f"{FPG} (Water (Oceans)).",
  "l1-geo-ocean-floor-relief-pairs", craft="precision")

P(OC, "hard", "Consider the following pairs of water bodies and the salinity typical of them:",
  "जलाशयों और उनकी विशिष्ट लवणता के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Baltic Sea : low salinity, owing to a large inflow of river water",
   "Mediterranean Sea : higher salinity, owing to high evaporation",
   "Black Sea : very low salinity, owing to an enormous inflow of fresh water from rivers",
   "Bay of Bengal : lower salinity than the Arabian Sea, owing to the inflow of the Ganga"],
  ["बाल्टिक सागर : नदियों के जल के भारी प्रवाह के कारण कम लवणता",
   "भूमध्य सागर : उच्च वाष्पीकरण के कारण अधिक लवणता",
   "काला सागर : नदियों से मीठे जल के विशाल प्रवाह के कारण बहुत कम लवणता",
   "बंगाल की खाड़ी : गंगा के जल-प्रवाह के कारण अरब सागर से कम लवणता"],
  3,
  "All four pairs are correctly matched. Salinity is set by the balance between what adds fresh water -- rain, rivers and melting ice -- and what removes it, chiefly evaporation; partly enclosed seas show the contrast most sharply. "
  "So the Arabian Sea, with high evaporation and little fresh-water inflow, is saltier than the Bay of Bengal, and inland water bodies in dry regions are the saltiest of all: Lake Van in Turkey, the Dead Sea and the Great Salt Lake in the USA record about 330, 238 and 220 parts per thousand.",
  "चारों युग्म सही सुमेलित हैं। लवणता इस संतुलन से तय होती है कि मीठा जल क्या जोड़ता है -- वर्षा, नदियाँ और पिघलती बर्फ़ -- और क्या उसे हटाता है, मुख्यतः वाष्पीकरण; आंशिक रूप से घिरे समुद्रों में यह अंतर सबसे स्पष्ट दिखता है। "
  "इसीलिए उच्च वाष्पीकरण और कम मीठे जल-प्रवाह वाला अरब सागर बंगाल की खाड़ी से अधिक खारा है, और शुष्क क्षेत्रों के आंतरिक जलाशय सबसे अधिक खारे हैं: तुर्की की वान झील, मृत सागर और अमेरिका की ग्रेट सॉल्ट झील में लगभग 330, 238 और 220 भाग प्रति हज़ार लवणता दर्ज होती है।",
  f"{FPG} (Water (Oceans)).",
  "l1-geo-salinity-seas-pairs", craft="linkage")

write("geo_l1_t4_c.sql")
