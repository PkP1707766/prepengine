# -*- coding: utf-8 -*-
"""Level 2 · Test 13 (Geography 2: Indian Physical Geography) -- Indian Physiography, Climate & Regions:
53 new bilingual rows against the live gap report: medium statement 15, medium MCQ 8, hard statement 6,
medium Statement-I/II 6, easy statement 5, hard MCQ 3, easy MCQ 2, easy Statement-I/II 2, hard
Statement-I/II 1 + I/II/III 1, medium pairs 2, easy pairs 1, hard pairs 1.
The bank already tests the Western vs Eastern Ghats (continuity, height, Anamudi), so those facts are
left alone. Shola forests, Himalayan vegetation zones, Delhi's winter inversion and national parks sit
in the Environment tests; crops and minerals are left to Test 14."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Geography"
PH = "Indian Physiography, Climate & Regions"
NC11I = "NCERT Class XI, India: Physical Environment"
NC9 = "NCERT Class IX, Contemporary India I"
IMD = "India Meteorological Department"

# ================================================================ MEDIUM STATEMENTS (15)
S(PH, "medium", "Consider the following statements about India's location and extent:",
  "भारत की स्थिति और विस्तार के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Standard Meridian of India (82°30' E) passes through five States.",
   "The difference in local time between the easternmost and westernmost points of India is about one hour.",
   "India's latitudinal and longitudinal extents are each roughly 30 degrees."],
  ["भारत की मानक याम्योत्तर (82°30' पू.) पाँच राज्यों से होकर गुज़रती है।",
   "भारत के सबसे पूर्वी और सबसे पश्चिमी बिंदुओं के स्थानीय समय में लगभग एक घंटे का अंतर है।",
   "भारत का अक्षांशीय और देशांतरीय विस्तार, दोनों लगभग 30-30 अंश हैं।"],
  C3, 1,
  "Statements 1 and 3 are correct. The Standard Meridian passes through Uttar Pradesh (near Mirzapur), Madhya Pradesh, Chhattisgarh, Odisha and Andhra Pradesh. The mainland stretches from about 8°4' N to 37°6' N and from about 68°7' E to 97°25' E -- close to 30 degrees each way, although the north-south distance (about 3,214 km) is greater than the east-west distance (about 2,933 km) because degrees of longitude shrink away from the Equator. "
  "Statement 2 is wrong: 30 degrees of longitude make a difference of about two hours -- the Sun rises in Arunachal Pradesh about two hours before it does in Gujarat.",
  "कथन 1 और 3 सही हैं। मानक याम्योत्तर उत्तर प्रदेश (मिर्ज़ापुर के पास), मध्य प्रदेश, छत्तीसगढ़, ओडिशा और आंध्र प्रदेश से होकर गुज़रती है। मुख्य भूमि लगभग 8°4' उ. से 37°6' उ. और लगभग 68°7' पू. से 97°25' पू. तक फैली है, यानी दोनों ओर लगभग 30 अंश; फिर भी उत्तर-दक्षिण दूरी (लगभग 3,214 किमी) पूर्व-पश्चिम दूरी (लगभग 2,933 किमी) से अधिक है, क्योंकि विषुवत रेखा से दूर जाने पर देशांतर के अंशों के बीच की दूरी घटती जाती है। "
  "कथन 2 गलत है: 30 अंश देशांतर से लगभग दो घंटे का अंतर होता है; अरुणाचल प्रदेश में सूर्य गुजरात की तुलना में लगभग दो घंटे पहले उगता है।",
  f"{NC9} -- India: Size and Location.",
  "igeo-location-meridian-extent")

S(PH, "medium", "Consider the following States:",
  "निम्नलिखित राज्यों पर विचार कीजिए:",
  ["Sikkim", "Uttarakhand", "Bihar", "Himachal Pradesh"],
  ["सिक्किम", "उत्तराखंड", "बिहार", "हिमाचल प्रदेश"],
  C4, 2,
  "Sikkim, Uttarakhand and Bihar border Nepal; the other two Nepal-border States are Uttar Pradesh and West Bengal. "
  "Himachal Pradesh is the trap: it lies close to Nepal on the map, but Uttarakhand lies between them, and Himachal's international border is with China (Tibet).",
  "सिक्किम, उत्तराखंड और बिहार की सीमा नेपाल से लगती है; नेपाल से सीमा वाले अन्य दो राज्य उत्तर प्रदेश और पश्चिम बंगाल हैं। "
  "हिमाचल प्रदेश ही जाल है: मानचित्र पर यह नेपाल के पास दिखता है, पर दोनों के बीच उत्तराखंड है, और हिमाचल की अंतरराष्ट्रीय सीमा चीन (तिब्बत) से लगती है।",
  f"{NC9} -- India: Size and Location; Ministry of Home Affairs -- Department of Border Management.",
  "igeo-nepal-border-states",
  closing="How many of the above States share a border with Nepal?",
  closing_hi="उपर्युक्त में से कितने राज्यों की सीमा नेपाल से लगती है?")

S(PH, "medium", "Consider the following statements about the Himalaya:",
  "हिमालय के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Shiwaliks are the youngest and outermost range of the Himalaya.",
   "The Greater Himalaya (Himadri) has a core of granite and is the most continuous range.",
   "Duns such as Dehradun are longitudinal valleys lying between the Lesser Himalaya and the Shiwaliks."],
  ["शिवालिक हिमालय की सबसे नवीन और सबसे बाहरी श्रेणी है।",
   "महान हिमालय (हिमाद्रि) का कोर ग्रेनाइट से बना है और यह सबसे सतत श्रेणी है।",
   "देहरादून जैसे दून लघु हिमालय और शिवालिक के बीच स्थित अनुदैर्ध्य घाटियाँ हैं।"],
  C3, 2,
  "All three statements are correct. The Shiwaliks, only about 900-1,100 m high, are built of unconsolidated sediments brought down by rivers from the main ranges. The Himadri, averaging about 6,000 m, holds the loftiest peaks and is perennially snowbound. Between the Lesser Himalaya (Himachal) and the Shiwaliks lie flat-floored longitudinal valleys called duns -- Dehradun, Kotli Dun and Patli Dun.",
  "तीनों कथन सही हैं। केवल लगभग 900-1,100 मीटर ऊँची शिवालिक श्रेणी मुख्य श्रेणियों से नदियों द्वारा लाए गए असंगठित अवसादों से बनी है। औसतन लगभग 6,000 मीटर ऊँचे हिमाद्रि में सबसे ऊँची चोटियाँ हैं और यह सदा हिमाच्छादित रहता है। लघु हिमालय (हिमाचल) और शिवालिक के बीच समतल तल वाली अनुदैर्ध्य घाटियाँ हैं, जिन्हें दून कहते हैं, जैसे देहरादून, कोटली दून और पाटली दून।",
  f"{NC9} -- Physical Features of India; {NC11I} -- Structure and Physiography.",
  "igeo-himalaya-ranges-duns")

S(PH, "medium", "Consider the following statements about the regional divisions of the Himalaya:",
  "हिमालय के प्रादेशिक विभाजनों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Punjab Himalaya lie between the Indus and the Satluj.",
   "The Kumaon Himalaya lie between the Kali and the Teesta.",
   "The Assam Himalaya lie between the Teesta and the Dihang."],
  ["पंजाब हिमालय सिंधु और सतलुज के बीच स्थित है।",
   "कुमाऊँ हिमालय काली और तीस्ता के बीच स्थित है।",
   "असम हिमालय तीस्ता और दिहांग के बीच स्थित है।"],
  C3, 1,
  "Statements 1 and 3 are correct. River valleys divide the Himalaya from west to east into the Punjab Himalaya (Indus to Satluj), the Kumaon Himalaya (Satluj to Kali), the Nepal Himalaya (Kali to Teesta) and the Assam Himalaya (Teesta to Dihang). "
  "Statement 2 is wrong: the stretch between the Kali and the Teesta is the Nepal Himalaya; the Kumaon Himalaya lie further west, between the Satluj and the Kali.",
  "कथन 1 और 3 सही हैं। नदी घाटियाँ हिमालय को पश्चिम से पूर्व की ओर पंजाब हिमालय (सिंधु से सतलुज), कुमाऊँ हिमालय (सतलुज से काली), नेपाल हिमालय (काली से तीस्ता) और असम हिमालय (तीस्ता से दिहांग) में बाँटती हैं। "
  "कथन 2 गलत है: काली और तीस्ता के बीच का भाग नेपाल हिमालय है; कुमाऊँ हिमालय इससे पश्चिम में, सतलुज और काली के बीच है।",
  f"{NC9} -- Physical Features of India.",
  "igeo-himalaya-regional-divisions")

S(PH, "medium", "Consider the following statements about the Northern Plains:",
  "उत्तरी मैदानों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Bhabar is a narrow belt of pebbles at the foot of the Shiwaliks where streams disappear underground.",
   "The Terai lies to the north of the Bhabar.",
   "Khadar is the older alluvium lying above the flood level of rivers."],
  ["भाबर शिवालिक के गिरिपद पर कंकड़-पत्थरों की एक संकरी पट्टी है, जहाँ जलधाराएँ भूमिगत हो जाती हैं।",
   "तराई भाबर के उत्तर में स्थित है।",
   "खादर नदियों के बाढ़ तल से ऊपर स्थित पुराना जलोढ़ है।"],
  C3, 0,
  "Only statement 1 is correct: the Bhabar, about 8-16 km wide, is made of coarse material dropped by rivers leaving the hills, and the water sinks into it. "
  "Statement 2 is wrong: the Terai lies south of the Bhabar, where the streams re-emerge and create a wet, marshy, once densely forested belt. "
  "Statement 3 is wrong: khadar is the newer alluvium of the floodplains, renewed almost every year; the older alluvium above flood level, often with kankar nodules, is bhangar.",
  "केवल कथन 1 सही है: लगभग 8-16 किमी चौड़ा भाबर पहाड़ियों से निकलती नदियों द्वारा गिराए गए मोटे पदार्थों से बना है, और जल इसमें समा जाता है। "
  "कथन 2 गलत है: तराई भाबर के दक्षिण में है, जहाँ जलधाराएँ फिर से ऊपर निकलती हैं और एक नम, दलदली, कभी घने वन वाली पट्टी बनाती हैं। "
  "कथन 3 गलत है: खादर बाढ़ के मैदानों का नया जलोढ़ है, जो लगभग हर वर्ष नवीनीकृत होता है; बाढ़ तल से ऊपर का पुराना जलोढ़, जिसमें प्रायः कंकड़ की ग्रंथियाँ होती हैं, बांगर है।",
  f"{NC9} -- Physical Features of India; {NC11I} -- Structure and Physiography.",
  "igeo-northern-plains-bhabar-terai-khadar")

S(PH, "medium", "Consider the following statements about western Rajasthan and the Aravallis:",
  "पश्चिमी राजस्थान और अरावली के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Luni, the main river of the region, ends in the Rann of Kachchh.",
   "Crescent-shaped sand dunes called barchans are common in the Thar.",
   "Guru Shikhar, the highest peak of the Aravallis, lies in the Mount Abu area."],
  ["इस क्षेत्र की मुख्य नदी लूनी कच्छ के रण में समाप्त हो जाती है।",
   "थार में बरखान कहलाने वाले अर्धचंद्राकार बालू के टीले आम हैं।",
   "अरावली की सबसे ऊँची चोटी गुरु शिखर माउंट आबू क्षेत्र में है।"],
  C3, 2,
  "All three statements are correct. The Luni rises near Ajmer and flows south-west to be lost in the Rann of Kachchh; most other streams of the Thar are short-lived and end in the sand or in salt lakes. Barchans, crescent-shaped dunes with horns pointing downwind, cover large areas near the India-Pakistan border. Guru Shikhar (about 1,722 m) rises above Mount Abu at the south-western end of the Aravallis.",
  "तीनों कथन सही हैं। लूनी अजमेर के पास से निकलकर दक्षिण-पश्चिम की ओर बहती है और कच्छ के रण में विलीन हो जाती है; थार की अधिकांश अन्य धाराएँ अल्पकालिक हैं और रेत या खारी झीलों में समाप्त हो जाती हैं। बरखान, जिनकी भुजाएँ हवा की दिशा में होती हैं, भारत-पाकिस्तान सीमा के पास बड़े क्षेत्रों में फैले हैं। गुरु शिखर (लगभग 1,722 मीटर) अरावली के दक्षिण-पश्चिमी छोर पर माउंट आबू के ऊपर उठा है।",
  f"{NC9} -- Physical Features of India; {NC11I} -- Structure and Physiography.",
  "igeo-thar-luni-barchans-guru-shikhar")

S(PH, "medium", "Consider the following statements about the ranges of central India:",
  "मध्य भारत की पर्वत श्रेणियों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Satpura range lies between the Narmada and the Tapi.",
   "The Vindhyan range lies to the south of the Narmada.",
   "The Satpura range is a fold mountain range."],
  ["सतपुड़ा श्रेणी नर्मदा और तापी के बीच स्थित है।",
   "विंध्य श्रेणी नर्मदा के दक्षिण में स्थित है।",
   "सतपुड़ा एक वलित पर्वत श्रेणी है।"],
  C3, 0,
  "Only statement 1 is correct. "
  "Statement 2 is wrong: the Vindhyas rise north of the Narmada, overlooking its valley, and continue east as the Kaimur hills; the Satpuras lie to its south. "
  "Statement 3 is wrong: the Satpura, with its highest peak Dhupgarh in the Mahadeo hills, is a block mountain range raised along faults; the only old fold mountains of the Peninsula are the Aravallis.",
  "केवल कथन 1 सही है। "
  "कथन 2 गलत है: विंध्य श्रेणी नर्मदा के उत्तर में उसकी घाटी के ऊपर उठी है और पूर्व में कैमूर पहाड़ियों के रूप में आगे बढ़ती है; सतपुड़ा उसके दक्षिण में है। "
  "कथन 3 गलत है: महादेव पहाड़ियों में स्थित सबसे ऊँची चोटी धूपगढ़ वाली सतपुड़ा भ्रंशों के साथ उठी एक खंड पर्वत (block mountain) श्रेणी है; प्रायद्वीप के एकमात्र पुराने वलित पर्वत अरावली हैं।",
  f"{NC11I} -- Structure and Physiography.",
  "igeo-satpura-vindhya")

S(PH, "medium", "Consider the following statements about the Peninsular plateau:",
  "प्रायद्वीपीय पठार के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Rajmahal hills mark the north-eastern edge of the Peninsular plateau.",
   "The Kaimur hills are an eastern extension of the Vindhyan range.",
   "The Mahadeo hills are part of the Satpura range."],
  ["राजमहल पहाड़ियाँ प्रायद्वीपीय पठार के उत्तर-पूर्वी किनारे को चिह्नित करती हैं।",
   "कैमूर पहाड़ियाँ विंध्य श्रेणी का पूर्वी विस्तार हैं।",
   "महादेव पहाड़ियाँ सतपुड़ा श्रेणी का भाग हैं।"],
  C3, 2,
  "All three statements are correct. The northern boundary of the Peninsular block runs from Kachchh along the Aravallis and then roughly parallel to the Yamuna and the Ganga as far as the Rajmahal hills in Jharkhand. The Kaimur hills carry the Vindhyas east into southern Uttar Pradesh and Bihar, and the Mahadeo hills around Pachmarhi form the central part of the Satpura range.",
  "तीनों कथन सही हैं। प्रायद्वीपीय खंड की उत्तरी सीमा कच्छ से अरावली के साथ-साथ और फिर मोटे तौर पर यमुना और गंगा के समानांतर झारखंड की राजमहल पहाड़ियों तक जाती है। कैमूर पहाड़ियाँ विंध्य श्रेणी को पूर्व में दक्षिणी उत्तर प्रदेश और बिहार तक ले जाती हैं, और पचमढ़ी के आसपास की महादेव पहाड़ियाँ सतपुड़ा श्रेणी का मध्य भाग हैं।",
  f"{NC11I} -- Structure and Physiography.",
  "igeo-peninsula-rajmahal-kaimur-mahadeo")

S(PH, "medium", "Consider the following statements about the coastal plains of India:",
  "भारत के तटीय मैदानों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The western coastal plain is an example of an emergent coast.",
   "The eastern coastal plain is narrower than the western coastal plain.",
   "Kayals (backwaters) are a feature of the Coromandel coast."],
  ["पश्चिमी तटीय मैदान उभरे हुए (emergent) तट का उदाहरण है।",
   "पूर्वी तटीय मैदान पश्चिमी तटीय मैदान से संकरा है।",
   "कयाल (पश्चजल) कोरोमंडल तट की विशेषता हैं।"],
  C3, 3,
  "None of the statements is correct. "
  "Statement 1 is wrong: the western coastal plain is a submerged coast -- part of the old land, including the legendary city of Dwarka, is believed to lie under the sea -- which is why it is narrow and has natural harbours; the eastern plain is the emergent one. "
  "Statement 2 is wrong: the eastern coastal plain is broader, built by the deltas of the Mahanadi, the Godavari, the Krishna and the Kaveri. "
  "Statement 3 is wrong: kayals, the lagoons and backwaters used for fishing, inland navigation and tourism, are a feature of the Malabar coast of Kerala.",
  "कोई भी कथन सही नहीं है। "
  "कथन 1 गलत है: पश्चिमी तटीय मैदान एक निमज्जित (submerged) तट है; माना जाता है कि पुरानी भूमि का कुछ भाग, जिसमें पौराणिक नगर द्वारका भी है, समुद्र के नीचे है; इसीलिए यह संकरा है और इसमें प्राकृतिक बंदरगाह हैं; उभरा हुआ तट पूर्वी मैदान है। "
  "कथन 2 गलत है: पूर्वी तटीय मैदान अधिक चौड़ा है, जो महानदी, गोदावरी, कृष्णा और कावेरी के डेल्टाओं से बना है। "
  "कथन 3 गलत है: मछली पकड़ने, आंतरिक जलमार्ग और पर्यटन के लिए प्रयुक्त लैगून और पश्चजल, यानी कयाल, केरल के मालाबार तट की विशेषता हैं।",
  f"{NC11I} -- Structure and Physiography; {NC9} -- Physical Features of India.",
  "igeo-coastal-plains-submerged-kayals")

S(PH, "medium", "Consider the following statements about India's islands:",
  "भारत के द्वीपों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Barren Island, India's only active volcano, lies in the Andaman and Nicobar Islands.",
   "The Ten Degree Channel separates the Andaman group from the Nicobar group.",
   "The Lakshadweep islands are of volcanic origin.",
   "Saddle Peak, the highest point of the Andaman and Nicobar Islands, lies in the Nicobar group."],
  ["भारत का एकमात्र सक्रिय ज्वालामुखी बैरन द्वीप अंडमान और निकोबार द्वीपसमूह में है।",
   "दस डिग्री चैनल अंडमान समूह को निकोबार समूह से अलग करता है।",
   "लक्षद्वीप के द्वीप ज्वालामुखी से बने हैं।",
   "अंडमान और निकोबार द्वीपसमूह का सबसे ऊँचा बिंदु सैडल पीक निकोबार समूह में है।"],
  C4, 1,
  "Statements 1 and 2 are correct. Barren Island, east of the main Andaman chain, has erupted repeatedly since the 1990s; the Ten Degree Channel runs between Little Andaman and Car Nicobar. "
  "Statement 3 is wrong: the Lakshadweep islands are coral atolls and reefs built on a submarine ridge; it is the Andaman and Nicobar chain that is an extension of submarine mountains, with volcanic Barren and Narcondam. "
  "Statement 4 is wrong: Saddle Peak (about 737 m) is in North Andaman.",
  "कथन 1 और 2 सही हैं। मुख्य अंडमान श्रृंखला के पूर्व में स्थित बैरन द्वीप में 1990 के दशक से बार-बार उद्गार हुए हैं; दस डिग्री चैनल लिटिल अंडमान और कार निकोबार के बीच है। "
  "कथन 3 गलत है: लक्षद्वीप के द्वीप एक समुद्री कटक पर बने प्रवाल वलयद्वीप (atoll) और भित्तियाँ हैं; अंडमान और निकोबार श्रृंखला समुद्र के नीचे के पर्वतों का विस्तार है, जिसमें ज्वालामुखी बैरन और नारकोंडम हैं। "
  "कथन 4 गलत है: सैडल पीक (लगभग 737 मीटर) उत्तरी अंडमान में है।",
  f"{NC11I} -- Structure and Physiography; {NC9} -- Physical Features of India.",
  "igeo-islands-barren-channels-saddle-peak")

S(PH, "medium", "Consider the following statements about the Indian monsoon:",
  "भारतीय मानसून के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The intense heating of the Tibetan Plateau in summer helps strengthen the south-west monsoon.",
   "A tropical easterly jet stream develops over the southern part of the Peninsula in summer.",
   "El Niño years are generally associated with above-normal monsoon rainfall in India."],
  ["ग्रीष्म ऋतु में तिब्बत के पठार का तीव्र गर्म होना दक्षिण-पश्चिम मानसून को प्रबल बनाने में सहायक होता है।",
   "ग्रीष्म ऋतु में प्रायद्वीप के दक्षिणी भाग के ऊपर एक उष्णकटिबंधीय पूर्वी जेट धारा विकसित होती है।",
   "एल नीनो वाले वर्ष सामान्यतः भारत में सामान्य से अधिक मानसूनी वर्षा से जुड़े होते हैं।"],
  C3, 1,
  "Statements 1 and 2 are correct. The heated Tibetan Plateau warms the air above it, which rises and spreads out, creating an upper-air high that helps set up the easterly flow; the tropical easterly jet then blows over peninsular India in June and July. "
  "Statement 3 is wrong: El Niño, the warming of the eastern Pacific, usually weakens the monsoon -- many of India's worst droughts, including 2002, 2009 and 2015, came in El Niño years.",
  "कथन 1 और 2 सही हैं। गर्म हुआ तिब्बत का पठार अपने ऊपर की वायु को गर्म करता है, जो ऊपर उठकर फैलती है और ऊपरी वायु में एक उच्च दाब बनाती है, जिससे पूर्वी प्रवाह स्थापित होने में मदद मिलती है; फिर जून और जुलाई में प्रायद्वीपीय भारत के ऊपर उष्णकटिबंधीय पूर्वी जेट धारा चलती है। "
  "कथन 3 गलत है: पूर्वी प्रशांत के गर्म होने से जुड़ा एल नीनो सामान्यतः मानसून को कमज़ोर करता है; भारत के कई सबसे बुरे सूखे, जिनमें 2002, 2009 और 2015 के सूखे भी हैं, एल नीनो वर्षों में पड़े।",
  f"{NC11I} -- Climate; {IMD} -- Monsoon.",
  "igeo-monsoon-tibet-tej-el-nino")

S(PH, "medium", "Consider the following statements about local weather phenomena in India:",
  "भारत की स्थानीय मौसमी घटनाओं के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Pre-monsoon showers in Kerala and coastal Karnataka are known as mango showers.",
   "Kalbaisakhi (nor'westers) are violent evening thunderstorms in West Bengal and Assam.",
   "The 'loo' is a hot, dry wind that blows over the northern plains in summer.",
   "'Cherry blossoms' are pre-monsoon showers that help coffee plants flower in Karnataka and Kerala."],
  ["केरल और तटीय कर्नाटक की मानसून-पूर्व बौछारें 'आम्र वर्षा' (mango showers) कहलाती हैं।",
   "काल बैसाखी (नॉर्वेस्टर) पश्चिम बंगाल और असम में शाम को आने वाले प्रचंड तूफ़ान हैं।",
   "'लू' ग्रीष्म ऋतु में उत्तरी मैदानों पर चलने वाली गर्म, शुष्क पवन है।",
   "'चेरी ब्लॉसम' (फूलों वाली बौछार) कर्नाटक और केरल में कॉफ़ी के पौधों में फूल आने में मदद करने वाली मानसून-पूर्व बौछारें हैं।"],
  C4, 3,
  "All four statements are correct. Mango showers help the mangoes ripen; kalbaisakhi, the 'calamity of the month of Baisakh', are useful for tea, jute and rice; the loo can raise temperatures to 45-50 °C and cause heatstroke; and blossom showers bring coffee into flower in Karnataka and Kerala. "
  "A student who expects one statement in four to be false will lose marks here.",
  "चारों कथन सही हैं। आम्र वर्षा आमों को पकने में मदद करती है; 'बैसाख महीने की विपत्ति' कहलाने वाली काल बैसाखी चाय, जूट और धान के लिए उपयोगी है; लू तापमान को 45-50 °C तक पहुँचा सकती है और लू लगने का कारण बनती है; और फूलों वाली बौछार कर्नाटक और केरल में कॉफ़ी में फूल लाती है। "
  "जो विद्यार्थी मानकर चलता है कि चार में से एक कथन गलत होगा, वह यहाँ अंक गँवाएगा।",
  f"{NC11I} -- Climate; {NC9} -- Climate.",
  "igeo-local-storms-mango-kalbaisakhi-loo")

S(PH, "medium", "Consider the following statements about rainfall in India:",
  "भारत में वर्षा के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Parts of western Rajasthan receive less than 20 cm of rain a year.",
   "Leh receives heavy rainfall from the Arabian Sea branch of the monsoon.",
   "The south-west monsoon withdraws from Kerala before it withdraws from Punjab."],
  ["पश्चिमी राजस्थान के कुछ भागों में वर्ष में 20 सेमी से कम वर्षा होती है।",
   "लेह में मानसून की अरब सागर शाखा से भारी वर्षा होती है।",
   "दक्षिण-पश्चिम मानसून पंजाब से पहले केरल से लौटता है।"],
  C3, 0,
  "Only statement 1 is correct: the far west of Rajasthan, around Jaisalmer, is the driest part of the plains. "
  "Statement 2 is wrong: Leh lies in the rain shadow of the Great Himalaya and gets only about 10 cm of rain a year -- Ladakh is a cold desert. "
  "Statement 3 is wrong: the monsoon withdraws in the order it is least firmly established -- it begins to leave western Rajasthan and Punjab in September and has normally withdrawn from the whole country by mid-October, the southern Peninsula last.",
  "केवल कथन 1 सही है: जैसलमेर के आसपास का राजस्थान का सुदूर पश्चिमी भाग मैदानों का सबसे शुष्क भाग है। "
  "कथन 2 गलत है: लेह महान हिमालय के वृष्टि-छाया क्षेत्र में है और वहाँ वर्ष में केवल लगभग 10 सेमी वर्षा होती है; लद्दाख एक ठंडा मरुस्थल है। "
  "कथन 3 गलत है: मानसून पहले वहाँ से लौटता है जहाँ वह सबसे कम जमा होता है; यह सितंबर में पश्चिमी राजस्थान और पंजाब से लौटना शुरू करता है और सामान्यतः मध्य अक्टूबर तक पूरे देश से लौट जाता है, सबसे अंत में दक्षिणी प्रायद्वीप से।",
  f"{NC11I} -- Climate; {IMD} -- Monsoon withdrawal.",
  "igeo-rainfall-rajasthan-leh-withdrawal")

S(PH, "medium", "Consider the following statements about the soils of India:",
  "भारत की मिट्टियों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Black soils have developed mainly from the weathering of basalt of the Deccan trap.",
   "Black soils are rich in nitrogen and phosphorus.",
   "Laterite soils develop in areas of low rainfall where there is little leaching."],
  ["काली मिट्टियाँ मुख्य रूप से दक्कन ट्रैप के बेसाल्ट के अपक्षय से बनी हैं।",
   "काली मिट्टियाँ नाइट्रोजन और फ़ॉस्फ़ोरस से समृद्ध होती हैं।",
   "लैटेराइट मिट्टियाँ कम वर्षा वाले उन क्षेत्रों में बनती हैं जहाँ निक्षालन (leaching) कम होता है।"],
  C3, 0,
  "Only statement 1 is correct: the black soils of Maharashtra, Gujarat and western Madhya Pradesh formed on the lava plateau of the Deccan trap. "
  "Statement 2 is wrong: black soils are rich in lime, iron, magnesia and alumina, and often potash, but are generally poor in nitrogen, phosphorus and organic matter. "
  "Statement 3 is wrong: laterite forms under high temperature and heavy rainfall, which leach away lime and silica and leave iron and aluminium oxides behind -- as in the Western Ghats, Kerala and the hills of Odisha and the north-east.",
  "केवल कथन 1 सही है: महाराष्ट्र, गुजरात और पश्चिमी मध्य प्रदेश की काली मिट्टियाँ दक्कन ट्रैप के लावा पठार पर बनी हैं। "
  "कथन 2 गलत है: काली मिट्टियाँ चूना, लोहा, मैग्नीशिया और ऐलुमिना से, और प्रायः पोटाश से भी, समृद्ध होती हैं, पर सामान्यतः नाइट्रोजन, फ़ॉस्फ़ोरस और जैव पदार्थों में कम होती हैं। "
  "कथन 3 गलत है: लैटेराइट उच्च तापमान और भारी वर्षा में बनती है, जो चूने और सिलिका को बहा ले जाती है और लोहे तथा ऐलुमिनियम के ऑक्साइड पीछे छोड़ देती है, जैसे पश्चिमी घाट, केरल और ओडिशा तथा पूर्वोत्तर की पहाड़ियों में।",
  f"{NC11I} -- Soils.",
  "igeo-soils-black-laterite")

S(PH, "medium", "Consider the following statements about the soils of India:",
  "भारत की मिट्टियों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Red soils get their colour from iron oxides.",
   "Alluvial soils are generally poor in potash.",
   "Saline soils are also known as reh, kallar or usar."],
  ["लाल मिट्टियों का रंग लोहे के ऑक्साइडों के कारण होता है।",
   "जलोढ़ मिट्टियाँ सामान्यतः पोटाश में कम होती हैं।",
   "लवणीय मिट्टियों को रेह, कल्लर या ऊसर भी कहा जाता है।"],
  C3, 1,
  "Statements 1 and 3 are correct. Red soils develop on crystalline and metamorphic rocks where iron is widely spread; they look yellow when hydrated. Saline soils, with a white crust of salts, occur in dry areas and in canal-irrigated tracts of Punjab and Haryana where waterlogging has drawn salts up to the surface. "
  "Statement 2 is wrong: alluvial soils are generally rich in potash but poor in phosphorus.",
  "कथन 1 और 3 सही हैं। लाल मिट्टियाँ रवेदार और कायांतरित चट्टानों पर बनती हैं, जिनमें लोहा व्यापक रूप से फैला होता है; जलयोजित होने पर ये पीली दिखती हैं। नमक की सफ़ेद परत वाली लवणीय मिट्टियाँ शुष्क क्षेत्रों में और पंजाब तथा हरियाणा के नहर-सिंचित भागों में मिलती हैं, जहाँ जलभराव ने लवणों को सतह तक खींच लिया है। "
  "कथन 2 गलत है: जलोढ़ मिट्टियाँ सामान्यतः पोटाश से समृद्ध पर फ़ॉस्फ़ोरस में कम होती हैं।",
  f"{NC11I} -- Soils.",
  "igeo-soils-red-alluvial-saline")

# ================================================================ HARD STATEMENTS (6)
S(PH, "hard", "Consider the following statements about the mechanism of the south-west monsoon:",
  "दक्षिण-पश्चिम मानसून की क्रियाविधि के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Somali jet is a low-level, cross-equatorial flow off the East African coast that strengthens the monsoon winds.",
   "A positive Indian Ocean Dipole generally favours good monsoon rainfall in India.",
   "In July, the monsoon trough lies over the Indian Ocean south of the Equator."],
  ["सोमाली जेट पूर्वी अफ़्रीकी तट के पास विषुवत रेखा को पार करने वाला निम्न-स्तरीय वायु प्रवाह है, जो मानसूनी पवनों को प्रबल बनाता है।",
   "धनात्मक हिंद महासागर द्विध्रुव (Indian Ocean Dipole) सामान्यतः भारत में अच्छी मानसूनी वर्षा के अनुकूल होता है।",
   "जुलाई में मानसून द्रोणी (monsoon trough) विषुवत रेखा के दक्षिण में हिंद महासागर के ऊपर होती है।"],
  C3, 1,
  "Statements 1 and 2 are correct. The Somali (Findlater) jet carries air from the southern Indian Ocean across the Equator and along the Somali coast into the Arabian Sea, feeding the monsoon current. In a positive dipole the western Indian Ocean is warmer than the eastern, which tends to boost Indian rainfall and can offset an El Niño, as in 1997 and 2019. "
  "Statement 3 is wrong: in July the monsoon trough -- the northern limb of the Inter-Tropical Convergence Zone -- lies over the Indo-Gangetic plain, roughly from Rajasthan to the head of the Bay of Bengal, drawing the moist winds far inland.",
  "कथन 1 और 2 सही हैं। सोमाली (फ़िंडलेटर) जेट दक्षिणी हिंद महासागर की वायु को विषुवत रेखा के पार और सोमालिया के तट के साथ अरब सागर तक लाती है, जिससे मानसूनी प्रवाह को बल मिलता है। धनात्मक द्विध्रुव में पश्चिमी हिंद महासागर पूर्वी भाग से अधिक गर्म होता है, जो भारत की वर्षा को बढ़ाने की प्रवृत्ति रखता है और एल नीनो के प्रभाव की भरपाई कर सकता है, जैसे 1997 और 2019 में। "
  "कथन 3 गलत है: जुलाई में मानसून द्रोणी, जो अंतर-उष्णकटिबंधीय अभिसरण क्षेत्र की उत्तरी भुजा है, सिंधु-गंगा मैदान के ऊपर, मोटे तौर पर राजस्थान से बंगाल की खाड़ी के शीर्ष तक, रहती है और नम पवनों को भीतर तक खींचती है।",
  f"{NC11I} -- Climate; {IMD} -- Monsoon.",
  "igeo-monsoon-somali-jet-iod-trough")

S(PH, "hard", "Consider the following statements about Köppen's climatic regions of India:",
  "भारत के कोपेन जलवायु प्रदेशों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The west coast of India south of Goa has an 'Amw' climate.",
   "Most of the Ganga plain has a 'BShw' climate.",
   "Arunachal Pradesh has an 'Aw' climate."],
  ["गोवा के दक्षिण में भारत के पश्चिमी तट की जलवायु 'Amw' है।",
   "गंगा के मैदान के अधिकांश भाग की जलवायु 'BShw' है।",
   "अरुणाचल प्रदेश की जलवायु 'Aw' है।"],
  C3, 0,
  "Only statement 1 is correct: 'Amw' is a monsoon climate with a short dry season. "
  "Statement 2 is wrong: most of the Ganga plain has 'Cwg' -- a humid climate with dry winters; 'BShw', the semi-arid steppe type, is found in north-western Gujarat, parts of western Rajasthan and Punjab, with 'BWhw' hot desert in the extreme west of Rajasthan. "
  "Statement 3 is wrong: Arunachal Pradesh has 'Dfc', a cold humid climate with short summers; 'Aw', the tropical savanna type, covers most of the Peninsular plateau south of the Tropic of Cancer.",
  "केवल कथन 1 सही है: 'Amw' छोटी शुष्क ऋतु वाली मानसूनी जलवायु है। "
  "कथन 2 गलत है: गंगा के मैदान के अधिकांश भाग में 'Cwg' है, यानी शुष्क शीत ऋतु वाली आर्द्र जलवायु; अर्ध-शुष्क स्टेपी प्रकार 'BShw' उत्तर-पश्चिमी गुजरात, पश्चिमी राजस्थान के कुछ भागों और पंजाब में है, और राजस्थान के सुदूर पश्चिम में 'BWhw' गर्म मरुस्थल है। "
  "कथन 3 गलत है: अरुणाचल प्रदेश में 'Dfc' है, यानी छोटी ग्रीष्म ऋतु वाली ठंडी आर्द्र जलवायु; उष्णकटिबंधीय सवाना प्रकार 'Aw' कर्क रेखा के दक्षिण में प्रायद्वीपीय पठार के अधिकांश भाग में है।",
  f"{NC11I} -- Climate.",
  "igeo-koppen-india")

S(PH, "hard", "Consider the following statements about the Trans-Himalaya and the Karakoram:",
  "पार-हिमालय (Trans-Himalaya) और काराकोरम के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["K2 (Godwin Austen) lies in the Karakoram range.",
   "The Zaskar range lies to the north of the Ladakh range.",
   "The Karakoram range forms India's border with Nepal."],
  ["K2 (गॉडविन ऑस्टिन) काराकोरम श्रेणी में स्थित है।",
   "ज़ास्कर श्रेणी लद्दाख श्रेणी के उत्तर में स्थित है।",
   "काराकोरम श्रेणी भारत की नेपाल से लगने वाली सीमा बनाती है।"],
  C3, 0,
  "Only statement 1 is correct: K2, at 8,611 m the second-highest peak in the world, lies in the Karakoram, which also holds the Siachen and Baltoro glaciers. "
  "Statement 2 is wrong: going north from the Great Himalaya, the ranges are the Zaskar, the Ladakh and then the Karakoram -- the Zaskar lies south of the Ladakh range, and the Indus flows between the Ladakh and Zaskar ranges. "
  "Statement 3 is wrong: the Karakoram lies in the far north, in Ladakh and Gilgit-Baltistan along the frontier with China; Nepal borders India far to the south-east, along Uttarakhand, Uttar Pradesh, Bihar, West Bengal and Sikkim.",
  "केवल कथन 1 सही है: 8,611 मीटर ऊँची, विश्व की दूसरी सबसे ऊँची चोटी K2 काराकोरम में है, जिसमें सियाचिन और बाल्टोरो हिमनद भी हैं। "
  "कथन 2 गलत है: महान हिमालय से उत्तर की ओर जाने पर श्रेणियाँ क्रम से ज़ास्कर, लद्दाख और फिर काराकोरम हैं; ज़ास्कर लद्दाख श्रेणी के दक्षिण में है, और सिंधु लद्दाख तथा ज़ास्कर श्रेणियों के बीच बहती है। "
  "कथन 3 गलत है: काराकोरम सुदूर उत्तर में, चीन से लगी सीमा के साथ लद्दाख और गिलगित-बाल्टिस्तान में है; नेपाल की सीमा इससे बहुत दूर दक्षिण-पूर्व में, उत्तराखंड, उत्तर प्रदेश, बिहार, पश्चिम बंगाल और सिक्किम के साथ लगती है।",
  f"{NC11I} -- Structure and Physiography.",
  "igeo-trans-himalaya-karakoram")

S(PH, "hard", "Consider the following statements about the Kashmir Himalaya:",
  "कश्मीर हिमालय के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Karewas are thick lake deposits of the Kashmir valley that are used for growing saffron.",
   "The Kashmir valley lies between the Pir Panjal and the Great Himalaya.",
   "The Pir Panjal is part of the Lesser Himalaya."],
  ["करेवा कश्मीर घाटी के मोटे झील-निक्षेप हैं, जिनका उपयोग केसर उगाने के लिए होता है।",
   "कश्मीर घाटी पीर पंजाल और महान हिमालय के बीच स्थित है।",
   "पीर पंजाल लघु हिमालय का भाग है।"],
  C3, 2,
  "All three statements are correct. The Kashmir valley was once occupied by a large lake; its thick glacial clay and lake sediments form flat-topped terraces called karewas, on which saffron (zafran) is grown around Pampore. The valley is enclosed by the Pir Panjal range of the Lesser Himalaya on the south-west and the Great Himalaya on the north-east, and the Jhelum meanders across its floor.",
  "तीनों कथन सही हैं। कश्मीर घाटी में कभी एक बड़ी झील थी; उसकी हिमनदी मिट्टी और झील के अवसादों की मोटी परतें समतल शीर्ष वाली वेदिकाएँ बनाती हैं, जिन्हें करेवा कहते हैं, और इन पर पंपोर के आसपास केसर (ज़ाफ़रान) उगाया जाता है। घाटी दक्षिण-पश्चिम में लघु हिमालय की पीर पंजाल श्रेणी और उत्तर-पूर्व में महान हिमालय से घिरी है, और झेलम इसके तल पर घुमावदार मार्ग में बहती है।",
  f"{NC11I} -- Structure and Physiography.",
  "igeo-kashmir-karewas-pir-panjal")

S(PH, "hard", "Consider the following statements about the natural vegetation of India:",
  "भारत की प्राकृतिक वनस्पति के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Tropical evergreen forests are found mainly in areas receiving more than 200 cm of rain.",
   "Teak and sal are among the important trees of the tropical moist deciduous forests.",
   "Tropical thorn forests are found in areas receiving more than 150 cm of rain."],
  ["उष्णकटिबंधीय सदाबहार वन मुख्य रूप से 200 सेमी से अधिक वर्षा वाले क्षेत्रों में पाए जाते हैं।",
   "सागौन और साल उष्णकटिबंधीय आर्द्र पर्णपाती वनों के महत्त्वपूर्ण वृक्षों में से हैं।",
   "उष्णकटिबंधीय कँटीले वन 150 सेमी से अधिक वर्षा वाले क्षेत्रों में पाए जाते हैं।"],
  C3, 1,
  "Statements 1 and 2 are correct. Evergreen forests grow on the western slopes of the Western Ghats, the hills of the north-east and the Andaman and Nicobar Islands; moist deciduous forests, where rain is roughly 100-200 cm, cover the north-east foothills, the eastern slopes of the Western Ghats and Odisha, and are dominated by teak and sal. "
  "Statement 3 is wrong: thorn forests of acacia, palms, euphorbias and cacti grow where rainfall is below about 70 cm -- in Rajasthan, Gujarat, and the dry interior of the Deccan.",
  "कथन 1 और 2 सही हैं। सदाबहार वन पश्चिमी घाट की पश्चिमी ढलानों, पूर्वोत्तर की पहाड़ियों और अंडमान-निकोबार द्वीपसमूह में उगते हैं; लगभग 100-200 सेमी वर्षा वाले क्षेत्रों के आर्द्र पर्णपाती वन पूर्वोत्तर की तलहटी, पश्चिमी घाट की पूर्वी ढलानों और ओडिशा में फैले हैं, जिनमें सागौन और साल प्रमुख हैं। "
  "कथन 3 गलत है: बबूल, खजूर, यूफ़ोर्बिया और नागफनी वाले कँटीले वन वहाँ उगते हैं जहाँ वर्षा लगभग 70 सेमी से कम होती है, जैसे राजस्थान, गुजरात और दक्कन के शुष्क आंतरिक भाग में।",
  f"{NC9} -- Natural Vegetation and Wildlife; {NC11I} -- Natural Vegetation.",
  "igeo-forest-types-rainfall")

S(PH, "hard", "Consider the following statements about the hills of southern India:",
  "दक्षिण भारत की पहाड़ियों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Nilgiri hills are the meeting point of the Western and the Eastern Ghats.",
   "Doddabetta is the highest peak of the Nilgiris.",
   "The Palghat (Palakkad) gap lies in Karnataka."],
  ["नीलगिरि पहाड़ियाँ पश्चिमी और पूर्वी घाट का मिलन-बिंदु हैं।",
   "डोडाबेट्टा नीलगिरि की सबसे ऊँची चोटी है।",
   "पालघाट (पालक्काड) दर्रा कर्नाटक में स्थित है।"],
  C3, 1,
  "Statements 1 and 2 are correct. The Eastern Ghats curve south-west to join the Western Ghats in the Nilgiris, where Doddabetta rises to about 2,637 m above Udhagamandalam (Ooty). "
  "Statement 3 is wrong: the Palghat gap, a break about 30 km wide in the Western Ghats between the Nilgiris and the Anamalai hills, lies on the Kerala-Tamil Nadu border; it lets rail and road cross from Coimbatore to Palakkad and lets the monsoon winds reach the Coimbatore region.",
  "कथन 1 और 2 सही हैं। पूर्वी घाट दक्षिण-पश्चिम की ओर मुड़कर नीलगिरि में पश्चिमी घाट से मिल जाता है, जहाँ उदगमंडलम (ऊटी) के ऊपर डोडाबेट्टा लगभग 2,637 मीटर तक उठा है। "
  "कथन 3 गलत है: नीलगिरि और अन्नामलाई पहाड़ियों के बीच पश्चिमी घाट में लगभग 30 किमी चौड़ा अंतराल, पालघाट दर्रा, केरल-तमिलनाडु सीमा पर है; इससे कोयंबटूर से पालक्काड तक रेल और सड़क जाती है और मानसूनी पवनें कोयंबटूर क्षेत्र तक पहुँचती हैं।",
  f"{NC11I} -- Structure and Physiography.",
  "igeo-nilgiris-doddabetta-palghat")

# ================================================================ EASY STATEMENTS (5)
S(PH, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["India lies entirely in the Northern Hemisphere.",
   "India is the seventh largest country in the world by area."],
  ["भारत पूरी तरह उत्तरी गोलार्ध में स्थित है।",
   "क्षेत्रफल के अनुसार भारत विश्व का सातवाँ सबसे बड़ा देश है।"],
  T2, 2,
  "Both statements are correct. India's southernmost point lies at about 6°45' N, and its area of about 3.28 million sq km is about 2.4 per cent of the world's land.",
  "दोनों कथन सही हैं। भारत का सबसे दक्षिणी बिंदु लगभग 6°45' उ. पर है, और इसका लगभग 32.8 लाख वर्ग किमी क्षेत्रफल विश्व के स्थल भाग का लगभग 2.4 प्रतिशत है।",
  f"{NC9} -- India: Size and Location.",
  "igeo-hemisphere-size-easy")

S(PH, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Thar Desert lies mainly in Rajasthan.",
   "Kanchenjunga lies in Himachal Pradesh."],
  ["थार मरुस्थल मुख्य रूप से राजस्थान में स्थित है।",
   "कंचनजंगा हिमाचल प्रदेश में स्थित है।"],
  T2, 0,
  "Only statement 1 is correct. Statement 2 is wrong: Kanchenjunga (8,586 m), the third-highest peak in the world, lies on the border of Sikkim and Nepal.",
  "केवल कथन 1 सही है। कथन 2 गलत है: विश्व की तीसरी सबसे ऊँची चोटी कंचनजंगा (8,586 मीटर) सिक्किम और नेपाल की सीमा पर स्थित है।",
  f"{NC9} -- Physical Features of India.",
  "igeo-thar-kanchenjunga-easy")

S(PH, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Most of India receives the bulk of its rainfall in winter.",
   "The south-west monsoon usually reaches Kerala around the first week of June."],
  ["भारत के अधिकांश भाग में अधिकतर वर्षा शीत ऋतु में होती है।",
   "दक्षिण-पश्चिम मानसून सामान्यतः जून के पहले सप्ताह के आसपास केरल पहुँचता है।"],
  T2, 1,
  "Only statement 2 is correct: the normal date of onset over Kerala is 1 June. Statement 1 is wrong: most of India gets about three-quarters of its annual rain from the south-west monsoon between June and September; only the Coromandel coast and parts of the north-west get significant winter rain.",
  "केवल कथन 2 सही है: केरल में मानसून आगमन की सामान्य तिथि 1 जून है। कथन 1 गलत है: भारत के अधिकांश भाग को अपनी वार्षिक वर्षा का लगभग तीन-चौथाई भाग जून से सितंबर के बीच दक्षिण-पश्चिम मानसून से मिलता है; केवल कोरोमंडल तट और उत्तर-पश्चिम के कुछ भागों में शीत ऋतु में उल्लेखनीय वर्षा होती है।",
  f"{NC9} -- Climate; {IMD} -- Monsoon onset.",
  "igeo-rainy-season-kerala-onset-easy")

S(PH, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Andaman and Nicobar Islands lie in the Arabian Sea.",
   "Lakshadweep is the largest group of islands of India."],
  ["अंडमान और निकोबार द्वीपसमूह अरब सागर में स्थित है।",
   "लक्षद्वीप भारत का सबसे बड़ा द्वीप समूह है।"],
  T2, 3,
  "Neither statement is correct. The Andaman and Nicobar Islands lie in the Bay of Bengal and are much the larger group; Lakshadweep, in the Arabian Sea, is India's smallest Union Territory, with a land area of only about 32 sq km.",
  "कोई भी कथन सही नहीं है। अंडमान और निकोबार द्वीपसमूह बंगाल की खाड़ी में है और कहीं बड़ा समूह है; अरब सागर में स्थित लक्षद्वीप भारत का सबसे छोटा केंद्र शासित प्रदेश है, जिसका स्थल क्षेत्रफल केवल लगभग 32 वर्ग किमी है।",
  f"{NC9} -- Physical Features of India.",
  "igeo-island-groups-easy")

S(PH, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Deccan plateau is roughly triangular in shape.",
   "The Northern Plains have been formed mainly by the Indus, the Ganga and the Brahmaputra and their tributaries."],
  ["दक्कन का पठार मोटे तौर पर त्रिभुजाकार है।",
   "उत्तरी मैदान मुख्य रूप से सिंधु, गंगा और ब्रह्मपुत्र तथा उनकी सहायक नदियों से बने हैं।"],
  T2, 2,
  "Both statements are correct. The Deccan plateau lies south of the Narmada, bounded by the Satpura, the Mahadeo, the Kaimur and the Maikal hills in the north and by the Western and Eastern Ghats on its sides. The Northern Plains, built of river alluvium, are among the most fertile and densely populated regions of the world.",
  "दोनों कथन सही हैं। दक्कन का पठार नर्मदा के दक्षिण में है, जो उत्तर में सतपुड़ा, महादेव, कैमूर और मैकाल पहाड़ियों से और दोनों किनारों पर पश्चिमी तथा पूर्वी घाट से घिरा है। नदियों के जलोढ़ से बने उत्तरी मैदान विश्व के सबसे उपजाऊ और घनी आबादी वाले क्षेत्रों में से हैं।",
  f"{NC9} -- Physical Features of India.",
  "igeo-deccan-shape-northern-plains-easy")

# ================================================================ MCQs (medium 8, hard 3, easy 2)
M(PH, "medium", "Which one of the following States has the longest coastline in India?",
  "निम्नलिखित में से किस राज्य की तटरेखा भारत में सबसे लंबी है?",
  ["Gujarat", "Andhra Pradesh", "Tamil Nadu", "Maharashtra"],
  ["गुजरात", "आंध्र प्रदेश", "तमिलनाडु", "महाराष्ट्र"],
  0,
  "Gujarat, with the long, indented coasts of the Gulf of Kachchh, the Kathiawar peninsula and the Gulf of Khambhat, has the longest coastline of any State -- about 2,340 km by the recent re-measurement of India's coastline, roughly a fifth of the total. Andhra Pradesh and Tamil Nadu come next.",
  "कच्छ की खाड़ी, काठियावाड़ प्रायद्वीप और खंभात की खाड़ी के लंबे, कटे-फटे तटों वाले गुजरात की तटरेखा किसी भी राज्य से सबसे लंबी है; भारत की तटरेखा के हाल के पुनर्मापन के अनुसार लगभग 2,340 किमी, यानी कुल तटरेखा का लगभग पाँचवाँ भाग। इसके बाद आंध्र प्रदेश और तमिलनाडु आते हैं।",
  f"{NC9} -- India: Size and Location; Ministry of Home Affairs -- revised coastline figures.",
  "igeo-longest-coastline-gujarat")

M(PH, "medium", "Which one of the following is the southernmost point of India?",
  "निम्नलिखित में से कौन-सा भारत का सबसे दक्षिणी बिंदु है?",
  ["Indira Point", "Kanyakumari", "Rameswaram", "Point Calimere"],
  ["इंदिरा पॉइंट", "कन्याकुमारी", "रामेश्वरम", "पॉइंट कैलिमेर"],
  0,
  "Indira Point, at the southern tip of Great Nicobar (about 6°45' N), is the southernmost point of India; parts of it were submerged in the 2004 tsunami. Kanyakumari (about 8°4' N) is the southern tip of the mainland -- the usual trap. Rameswaram and Point Calimere lie further north on the Tamil Nadu coast.",
  "ग्रेट निकोबार के दक्षिणी छोर पर (लगभग 6°45' उ.) स्थित इंदिरा पॉइंट भारत का सबसे दक्षिणी बिंदु है; 2004 की सुनामी में इसका कुछ भाग डूब गया था। कन्याकुमारी (लगभग 8°4' उ.) मुख्य भूमि का दक्षिणी छोर है, और यही सामान्य जाल है। रामेश्वरम और पॉइंट कैलिमेर तमिलनाडु के तट पर और उत्तर में हैं।",
  f"{NC9} -- India: Size and Location.",
  "igeo-southernmost-indira-point")

M(PH, "medium", "India shares its longest international land border with:",
  "भारत की सबसे लंबी अंतरराष्ट्रीय स्थलीय सीमा किस देश के साथ है?",
  ["Bangladesh", "China", "Pakistan", "Afghanistan"],
  ["बांग्लादेश", "चीन", "पाकिस्तान", "अफ़ग़ानिस्तान"],
  0,
  "The India-Bangladesh border is about 4,097 km long, running through West Bengal, Assam, Meghalaya, Tripura and Mizoram. China (about 3,488 km) is the usual trap, followed by Pakistan (about 3,323 km); the border with Afghanistan, about 106 km, lies in the part of Jammu and Kashmir under Pakistan's occupation.",
  "भारत-बांग्लादेश सीमा लगभग 4,097 किमी लंबी है, जो पश्चिम बंगाल, असम, मेघालय, त्रिपुरा और मिज़ोरम से होकर जाती है। चीन (लगभग 3,488 किमी) सामान्य जाल है, जिसके बाद पाकिस्तान (लगभग 3,323 किमी) आता है; लगभग 106 किमी की अफ़ग़ानिस्तान सीमा जम्मू-कश्मीर के पाकिस्तान के कब्ज़े वाले भाग में है।",
  "Ministry of Home Affairs -- Department of Border Management.",
  "igeo-longest-border-bangladesh")

M(PH, "medium", "The term 'October heat' in India refers to:",
  "भारत में 'अक्टूबर हीट' (October heat) किसे कहते हैं?",
  ["hot, humid weather after the monsoon withdraws", "dry, dusty winds blowing in from the Thar Desert",
   "heat waves caused by cyclones in the Arabian Sea", "warm spells brought by western disturbances"],
  ["मानसून लौटने के बाद का गर्म और उमस भरा मौसम", "थार मरुस्थल से आने वाली शुष्क, धूल भरी पवनें",
   "अरब सागर के चक्रवातों से आने वाली लू की लहरें", "पश्चिमी विक्षोभों से आने वाली गर्म अवधियाँ"],
  0,
  "In October, as the monsoon retreats, the skies clear and day temperatures rise again, while the land is still moist from the rains; the combination of high temperature and humidity makes the weather oppressive -- this is 'October heat'. Temperatures then begin to fall steadily, especially in the north.",
  "अक्टूबर में जब मानसून लौटता है, आकाश साफ़ हो जाता है और दिन का तापमान फिर बढ़ता है, जबकि भूमि वर्षा से अभी भी नम रहती है; ऊँचे तापमान और आर्द्रता के मेल से मौसम कष्टदायक हो जाता है, इसे ही 'अक्टूबर हीट' कहते हैं। इसके बाद तापमान, विशेषकर उत्तर में, लगातार घटने लगता है।",
  f"{NC9} -- Climate.",
  "igeo-october-heat")

M(PH, "medium", "The Tropic of Cancer does NOT pass through which one of the following States?",
  "कर्क रेखा निम्नलिखित में से किस राज्य से होकर नहीं गुज़रती?",
  ["Odisha", "Jharkhand", "Chhattisgarh", "Mizoram"],
  ["ओडिशा", "झारखंड", "छत्तीसगढ़", "मिज़ोरम"],
  0,
  "The Tropic of Cancer passes through eight States: Gujarat, Rajasthan, Madhya Pradesh, Chhattisgarh, Jharkhand, West Bengal, Tripura and Mizoram. Odisha is the trap -- it lies between Chhattisgarh, Jharkhand and West Bengal, but its northern boundary stays south of 23°26' N.",
  "कर्क रेखा आठ राज्यों से गुज़रती है: गुजरात, राजस्थान, मध्य प्रदेश, छत्तीसगढ़, झारखंड, पश्चिम बंगाल, त्रिपुरा और मिज़ोरम। ओडिशा ही जाल है; यह छत्तीसगढ़, झारखंड और पश्चिम बंगाल के बीच है, पर इसकी उत्तरी सीमा 23°26' उ. से दक्षिण में ही रहती है।",
  f"{NC9} -- India: Size and Location.",
  "igeo-tropic-of-cancer-not-odisha")

M(PH, "medium", "The Rann of Kachchh is best described as:",
  "कच्छ के रण का सबसे अच्छा वर्णन कौन-सा है?",
  ["a seasonally flooded salt marsh", "a sandy desert with shifting dunes",
   "a coral reef enclosing a lagoon", "a freshwater lake fed by Himalayan rivers"],
  ["मौसमी रूप से जलमग्न होने वाला लवणीय दलदल", "खिसकते टीलों वाला रेतीला मरुस्थल",
   "एक लैगून को घेरने वाली प्रवाल भित्ति", "हिमालयी नदियों से पोषित मीठे जल की झील"],
  0,
  "The Great and Little Rann of Kachchh are vast flat salt marshes, once an arm of the sea: in the monsoon they are covered by shallow water from the sea and streams, and in the dry season they turn into a hard, white salt crust. They are home to the Indian wild ass and to salt-making communities.",
  "कच्छ का बड़ा और छोटा रण विशाल समतल लवणीय दलदल हैं, जो कभी समुद्र की एक भुजा थे: मानसून में ये समुद्र और धाराओं के उथले जल से ढक जाते हैं और शुष्क ऋतु में नमक की कठोर, सफ़ेद परत में बदल जाते हैं। यहाँ भारतीय जंगली गधा (घुड़खर) और नमक बनाने वाले समुदाय रहते हैं।",
  f"{NC11I} -- Structure and Physiography.",
  "igeo-rann-of-kachchh")

M(PH, "medium", "Which one of the following is NOT a part of the Purvanchal (the eastern hills)?",
  "निम्नलिखित में से कौन-सा पूर्वांचल (पूर्वी पहाड़ियों) का भाग नहीं है?",
  ["Garo hills", "Patkai Bum", "Naga hills", "Mizo hills"],
  ["गारो पहाड़ियाँ", "पटकाई बुम", "नागा पहाड़ियाँ", "मिज़ो पहाड़ियाँ"],
  0,
  "The Purvanchal is the eastward bend of the Himalaya along India's border with Myanmar -- the Patkai Bum, the Naga hills, the Manipur hills and the Mizo (Lushai) hills, made of strong sandstones. The Garo, Khasi and Jaintia hills are different: they form the Meghalaya plateau, an old block of the Peninsular plateau cut off from the Chotanagpur plateau by the Garo-Rajmahal (Malda) gap.",
  "पूर्वांचल म्यांमार से लगी भारत की सीमा के साथ हिमालय का पूर्व की ओर मुड़ा भाग है, यानी पटकाई बुम, नागा पहाड़ियाँ, मणिपुर पहाड़ियाँ और मिज़ो (लुशाई) पहाड़ियाँ, जो मज़बूत बलुआ पत्थरों से बनी हैं। गारो, खासी और जयंतिया पहाड़ियाँ इनसे भिन्न हैं: ये मेघालय पठार बनाती हैं, जो प्रायद्वीपीय पठार का एक पुराना खंड है और गारो-राजमहल (मालदा) अंतराल से छोटानागपुर पठार से अलग हो गया है।",
  f"{NC9} -- Physical Features of India; {NC11I} -- Structure and Physiography.",
  "igeo-purvanchal-garo-not")

M(PH, "medium", "Which one of the following is the largest physiographic division of India by area?",
  "क्षेत्रफल के अनुसार निम्नलिखित में से कौन-सा भारत का सबसे बड़ा भू-आकृतिक विभाग है?",
  ["The Peninsular Plateau", "The Northern Plains", "The Himalayan mountains", "The coastal plains and islands"],
  ["प्रायद्वीपीय पठार", "उत्तरी मैदान", "हिमालयी पर्वत", "तटीय मैदान और द्वीप"],
  0,
  "The Peninsular Plateau, a tableland of old crystalline, igneous and metamorphic rocks, covers roughly half of India's area -- far more than the Northern Plains (about a fifth) or the Himalayan ranges. It is also the oldest part of the Indian landmass, a fragment of the ancient Gondwana land.",
  "पुरानी रवेदार, आग्नेय और कायांतरित चट्टानों से बना मेज़ जैसा प्रायद्वीपीय पठार भारत के लगभग आधे क्षेत्रफल में फैला है, जो उत्तरी मैदानों (लगभग पाँचवाँ भाग) या हिमालयी श्रेणियों से कहीं अधिक है। यह भारतीय भूभाग का सबसे पुराना भाग भी है, प्राचीन गोंडवाना भूमि का एक टुकड़ा।",
  f"{NC9} -- Physical Features of India.",
  "igeo-largest-division-peninsular-plateau")

M(PH, "hard", "Mawsynram and Cherrapunji receive exceptionally heavy rainfall mainly because:",
  "मॉसिनराम और चेरापूँजी में असाधारण रूप से भारी वर्षा मुख्य रूप से किस कारण होती है?",
  ["the funnel-shaped Khasi hills force moist winds from the Bay of Bengal to rise sharply",
   "they stand higher above sea level than any other inhabited place in India",
   "western disturbances from the Mediterranean bring them heavy rain and snow in winter",
   "cyclones formed over the Arabian Sea cross over them regularly during the retreating monsoon"],
  ["कीप (funnel) के आकार की खासी पहाड़ियाँ बंगाल की खाड़ी की नम पवनों को तेज़ी से ऊपर उठने को विवश करती हैं",
   "ये भारत के किसी भी अन्य बसे हुए स्थान से अधिक ऊँचाई पर हैं",
   "भूमध्य सागर से आने वाले पश्चिमी विक्षोभ इन्हें शीत ऋतु में भारी वर्षा और हिमपात देते हैं",
   "लौटते मानसून के दौरान अरब सागर में बने चक्रवात नियमित रूप से इनके ऊपर से गुज़रते हैं"],
  0,
  "The Bay of Bengal branch, after crossing the plains of Bangladesh, meets the steep southern face of the Khasi hills; the valleys narrow like a funnel, so the saturated air is forced up abruptly and drops its moisture -- Mawsynram averages more than 11,000 mm a year. At about 1,400 m they are far from the highest settlements in India -- villages in Ladakh lie above 4,000 m and are dry; western disturbances and Arabian Sea cyclones do not affect Meghalaya.",
  "बंगाल की खाड़ी शाखा बांग्लादेश के मैदानों को पार करने के बाद खासी पहाड़ियों की खड़ी दक्षिणी ढलान से टकराती है; घाटियाँ कीप की तरह संकरी होती जाती हैं, इसलिए संतृप्त वायु अचानक ऊपर उठने को विवश होती है और अपनी नमी गिरा देती है; मॉसिनराम में औसतन 11,000 मिमी से अधिक वार्षिक वर्षा होती है। लगभग 1,400 मीटर की ऊँचाई पर ये भारत की सबसे ऊँची बस्तियों से बहुत नीचे हैं; लद्दाख के गाँव 4,000 मीटर से ऊपर हैं और शुष्क हैं; पश्चिमी विक्षोभ और अरब सागर के चक्रवात मेघालय को प्रभावित नहीं करते।",
  f"{NC11I} -- Climate; {NC9} -- Climate.",
  "igeo-mawsynram-rainfall-reason")

M(PH, "hard", "Which one of the following is the correct order of these hill ranges of the Western Ghats from north to south?",
  "पश्चिमी घाट की इन पहाड़ी श्रेणियों का उत्तर से दक्षिण की ओर सही क्रम कौन-सा है?",
  ["Sahyadri - Nilgiri - Anamalai - Cardamom", "Nilgiri - Sahyadri - Cardamom - Anamalai",
   "Sahyadri - Anamalai - Nilgiri - Cardamom", "Cardamom - Nilgiri - Sahyadri - Anamalai"],
  ["सह्याद्रि - नीलगिरि - अन्नामलाई - इलायची (कार्डमम)", "नीलगिरि - सह्याद्रि - इलायची - अन्नामलाई",
   "सह्याद्रि - अन्नामलाई - नीलगिरि - इलायची", "इलायची - नीलगिरि - सह्याद्रि - अन्नामलाई"],
  0,
  "The Sahyadri runs through Maharashtra, Goa and Karnataka; the Nilgiris stand at the Karnataka-Kerala-Tamil Nadu junction; south of the Palghat gap come the Anamalai hills, holding Anamudi; and the Cardamom hills lie furthest south, on the Kerala-Tamil Nadu border.",
  "सह्याद्रि महाराष्ट्र, गोवा और कर्नाटक से होकर जाती है; नीलगिरि कर्नाटक-केरल-तमिलनाडु के मिलन-स्थल पर है; पालघाट दर्रे के दक्षिण में अन्नामलाई पहाड़ियाँ हैं, जिनमें अनामुडी है; और इलायची (कार्डमम) पहाड़ियाँ सबसे दक्षिण में, केरल-तमिलनाडु सीमा पर हैं।",
  f"{NC11I} -- Structure and Physiography.",
  "igeo-western-ghats-order")

M(PH, "hard", "By about which date does the south-west monsoon normally cover the whole of India, according to the India Meteorological Department's current normal dates?",
  "भारत मौसम विज्ञान विभाग की वर्तमान सामान्य तिथियों के अनुसार दक्षिण-पश्चिम मानसून सामान्यतः लगभग किस तिथि तक पूरे भारत पर छा जाता है?",
  ["8 July", "15 June", "15 August", "1 September"],
  ["8 जुलाई", "15 जून", "15 अगस्त", "1 सितंबर"],
  0,
  "In 2020 the IMD revised its normal dates: the monsoon now normally covers the entire country by 8 July, a week earlier than the old date of 15 July, and its withdrawal from north-west India normally begins around 17 September instead of 1 September. Onset over Kerala stays at 1 June. By 15 June it has usually covered only the south, the west coast up to Gujarat and the north-east.",
  "2020 में IMD ने अपनी सामान्य तिथियाँ संशोधित कीं: अब मानसून सामान्यतः 8 जुलाई तक पूरे देश पर छा जाता है, जो पुरानी तिथि 15 जुलाई से एक सप्ताह पहले है, और उत्तर-पश्चिम भारत से इसकी वापसी सामान्यतः 1 सितंबर के बजाय लगभग 17 सितंबर से शुरू होती है। केरल पर आगमन की तिथि 1 जून ही है। 15 जून तक यह सामान्यतः केवल दक्षिण, गुजरात तक के पश्चिमी तट और पूर्वोत्तर पर ही छाया होता है।",
  f"{IMD} -- Revised normal dates of onset and withdrawal of the south-west monsoon (2020).",
  "igeo-monsoon-covers-country-date")

M(PH, "easy", "Which one of the following is the largest State of India by area?",
  "क्षेत्रफल के अनुसार निम्नलिखित में से कौन-सा भारत का सबसे बड़ा राज्य है?",
  ["Rajasthan", "Madhya Pradesh", "Maharashtra", "Uttar Pradesh"],
  ["राजस्थान", "मध्य प्रदेश", "महाराष्ट्र", "उत्तर प्रदेश"],
  0,
  "Rajasthan, at about 3.42 lakh sq km, is the largest State -- about a tenth of India's area. Madhya Pradesh is second and Maharashtra third; Uttar Pradesh is the most populous State but only fourth in area.",
  "लगभग 3.42 लाख वर्ग किमी वाला राजस्थान सबसे बड़ा राज्य है, जो भारत के क्षेत्रफल का लगभग दसवाँ भाग है। मध्य प्रदेश दूसरे और महाराष्ट्र तीसरे स्थान पर है; उत्तर प्रदेश सबसे अधिक जनसंख्या वाला राज्य है, पर क्षेत्रफल में केवल चौथा।",
  f"{NC9} -- India: Size and Location.",
  "igeo-largest-state-rajasthan-easy")

M(PH, "easy", "The Palk Strait separates India from:",
  "पाक जलडमरूमध्य (Palk Strait) भारत को किस देश से अलग करता है?",
  ["Sri Lanka", "Maldives", "Myanmar", "Indonesia"],
  ["श्रीलंका", "मालदीव", "म्यांमार", "इंडोनेशिया"],
  0,
  "The Palk Strait, between Tamil Nadu and the Jaffna peninsula of Sri Lanka, together with the Gulf of Mannar to its south, separates India from Sri Lanka; the chain of shoals called Adam's Bridge (Rama Setu) runs across it from Rameswaram.",
  "तमिलनाडु और श्रीलंका के जाफ़ना प्रायद्वीप के बीच स्थित पाक जलडमरूमध्य, अपने दक्षिण की मन्नार की खाड़ी के साथ, भारत को श्रीलंका से अलग करता है; रामेश्वरम से इसके आर-पार 'ऐडम्स ब्रिज' (राम सेतु) कहलाने वाली उथली चट्टानों की श्रृंखला है।",
  f"{NC9} -- India: Size and Location.",
  "igeo-palk-strait-easy")

# ================================================================ STATEMENT-I/II (medium 6, easy 2, hard 1 + I/II/III 1)
A(PH, "medium",
  "The western slopes of the Western Ghats receive very heavy rainfall, while the interior of the Deccan to their east is comparatively dry.",
  "पश्चिमी घाट की पश्चिमी ढलानों पर बहुत भारी वर्षा होती है, जबकि उनके पूर्व में दक्कन का आंतरिक भाग अपेक्षाकृत शुष्क है।",
  "Moist south-west monsoon winds rise over the Ghats and shed most of their moisture on the windward side, leaving a rain-shadow area to the east.",
  "नम दक्षिण-पश्चिम मानसूनी पवनें घाटों पर ऊपर उठती हैं और अपनी अधिकांश नमी पवनमुखी ढलान पर गिरा देती हैं, जिससे पूर्व में वृष्टि-छाया क्षेत्र बन जाता है।",
  0,
  "Both statements are correct and Statement-II explains Statement-I. Places on the western slopes, such as Agumbe and Mahabaleshwar, get 500-700 cm of rain, while Pune and the plateau beyond, only about 100 km inland, get well under 100 cm as the descending air warms and dries.",
  "दोनों कथन सही हैं और कथन-II कथन-I की व्याख्या करता है। पश्चिमी ढलानों के आगुम्बे और महाबलेश्वर जैसे स्थानों पर 500-700 सेमी वर्षा होती है, जबकि केवल लगभग 100 किमी भीतर स्थित पुणे और उससे आगे के पठार पर 100 सेमी से काफ़ी कम वर्षा होती है, क्योंकि नीचे उतरती वायु गर्म और शुष्क हो जाती है।",
  f"{NC11I} -- Climate.",
  "igeo-western-ghats-rain-shadow")

A(PH, "medium",
  "Delhi receives more annual rainfall than Kolkata.",
  "दिल्ली में कोलकाता से अधिक वार्षिक वर्षा होती है।",
  "In the northern plains, monsoon rainfall generally decreases from east to west.",
  "उत्तरी मैदानों में मानसूनी वर्षा सामान्यतः पूर्व से पश्चिम की ओर घटती जाती है।",
  3,
  "Statement-I is incorrect but Statement-II is correct. The Bay of Bengal branch enters the plains from the east and loses moisture as it moves up the Ganga valley, so Kolkata gets about 160 cm of rain a year, Patna about 110 cm, Prayagraj about 100 cm and Delhi only about 70-80 cm.",
  "कथन-I गलत है पर कथन-II सही है। बंगाल की खाड़ी शाखा पूर्व से मैदानों में प्रवेश करती है और गंगा घाटी में आगे बढ़ते हुए नमी खोती जाती है, इसलिए कोलकाता में वर्ष में लगभग 160 सेमी, पटना में लगभग 110 सेमी, प्रयागराज में लगभग 100 सेमी और दिल्ली में केवल लगभग 70-80 सेमी वर्षा होती है।",
  f"{NC11I} -- Climate.",
  "igeo-rainfall-east-west-plains")

A(PH, "medium",
  "Parts of north-western India receive rain in winter.",
  "उत्तर-पश्चिमी भारत के कुछ भागों में शीत ऋतु में वर्षा होती है।",
  "Western disturbances that originate over the Mediterranean region are brought into India by the westerly jet stream.",
  "भूमध्यसागरीय क्षेत्र में उत्पन्न होने वाले पश्चिमी विक्षोभ पछुआ जेट धारा द्वारा भारत में लाए जाते हैं।",
  0,
  "Both statements are correct and Statement-II explains Statement-I. These shallow cyclonic depressions, steered by the subtropical westerly jet that lies south of the Himalaya in winter, bring light rain to Punjab, Haryana and western Uttar Pradesh and snow to the western Himalaya. Though small in amount, this rain is valuable for the rabi wheat crop.",
  "दोनों कथन सही हैं और कथन-II कथन-I की व्याख्या करता है। शीत ऋतु में हिमालय के दक्षिण में स्थित उपोष्ण पछुआ जेट द्वारा दिशा दिए जाने वाले ये उथले चक्रवाती अवदाब पंजाब, हरियाणा और पश्चिमी उत्तर प्रदेश में हल्की वर्षा और पश्चिमी हिमालय में हिमपात लाते हैं। मात्रा में कम होते हुए भी यह वर्षा रबी की गेहूँ फ़सल के लिए मूल्यवान है।",
  f"{NC11I} -- Climate.",
  "igeo-western-disturbances-winter-rain")

A(PH, "medium",
  "The Himalaya shield the Indian subcontinent from the cold winds of Central Asia.",
  "हिमालय भारतीय उपमहाद्वीप को मध्य एशिया की ठंडी पवनों से बचाता है।",
  "The Himalaya are young fold mountains.",
  "हिमालय नवीन वलित पर्वत हैं।",
  1,
  "Both statements are correct, but Statement-II does not explain Statement-I. The Himalaya protect India because of their great height and unbroken east-west extent, which block the bitterly cold, dry air of Central Asia in winter and trap the monsoon winds in summer. That they are young fold mountains explains their height and their earthquakes, not their role as a climatic barrier.",
  "दोनों कथन सही हैं, पर कथन-II कथन-I की व्याख्या नहीं करता। हिमालय अपनी बड़ी ऊँचाई और पूर्व-पश्चिम में अटूट विस्तार के कारण भारत की रक्षा करता है; यह शीत ऋतु में मध्य एशिया की अत्यधिक ठंडी, शुष्क वायु को रोकता है और ग्रीष्म में मानसूनी पवनों को रोक लेता है। उसका नवीन वलित पर्वत होना उसकी ऊँचाई और भूकंपों की व्याख्या करता है, जलवायु अवरोध के रूप में उसकी भूमिका की नहीं।",
  f"{NC11I} -- Climate; {NC9} -- Physical Features of India.",
  "igeo-himalaya-climatic-barrier")

A(PH, "medium",
  "Black soils are often called 'self-ploughing' soils.",
  "काली मिट्टियों को प्रायः 'स्वतः जुताई वाली' (self-ploughing) मिट्टियाँ कहा जाता है।",
  "They swell when wet and shrink and crack when dry, so that the soil turns itself over.",
  "ये गीली होने पर फूल जाती हैं और सूखने पर सिकुड़कर फट जाती हैं, जिससे मिट्टी स्वयं उलट-पलट जाती है।",
  0,
  "Both statements are correct and Statement-II explains Statement-I. Rich in clay, black soil becomes sticky when wet; in the dry season it develops wide cracks into which loose topsoil falls, so the soil is mixed as if it had been ploughed. Its capacity to hold moisture is why it can support crops without much irrigation.",
  "दोनों कथन सही हैं और कथन-II कथन-I की व्याख्या करता है। चिकनी मिट्टी से भरपूर काली मिट्टी गीली होने पर चिपचिपी हो जाती है; शुष्क ऋतु में इसमें चौड़ी दरारें पड़ती हैं, जिनमें ऊपर की ढीली मिट्टी गिर जाती है, और मिट्टी ऐसे मिल जाती है मानो उसकी जुताई हुई हो। नमी धारण करने की अपनी क्षमता के कारण यह बिना अधिक सिंचाई के फ़सलों को सहारा दे सकती है।",
  f"{NC11I} -- Soils.",
  "igeo-black-soil-self-ploughing")

A(PH, "medium",
  "The Deccan plateau slopes generally towards the east.",
  "दक्कन का पठार सामान्यतः पूर्व की ओर ढलान वाला है।",
  "Most rivers of the Peninsula drain into the Arabian Sea.",
  "प्रायद्वीप की अधिकांश नदियाँ अरब सागर में गिरती हैं।",
  2,
  "Statement-I is correct but Statement-II is incorrect. Because the plateau is highest along the Western Ghats and tilts east, most peninsular rivers -- the Mahanadi, the Godavari, the Krishna and the Kaveri among them -- rise in the west and flow east into the Bay of Bengal. Only a few, such as the Narmada and the Tapi, flow west, through rift valleys, and the short, swift streams of the Western Ghats.",
  "कथन-I सही है पर कथन-II गलत है। पठार पश्चिमी घाट के साथ सबसे ऊँचा है और पूर्व की ओर झुका है, इसलिए अधिकांश प्रायद्वीपीय नदियाँ, जिनमें महानदी, गोदावरी, कृष्णा और कावेरी हैं, पश्चिम में निकलकर पूर्व की ओर बंगाल की खाड़ी में गिरती हैं। केवल कुछ, जैसे नर्मदा और तापी, भ्रंश घाटियों से होकर पश्चिम की ओर बहती हैं, और पश्चिमी घाट की छोटी, तेज़ धाराएँ।",
  f"{NC11I} -- Structure and Physiography; Drainage System.",
  "igeo-deccan-slope-east")

A(PH, "easy",
  "Shimla is usually warmer than Delhi in summer.",
  "ग्रीष्म ऋतु में शिमला सामान्यतः दिल्ली से अधिक गर्म होता है।",
  "Temperature generally decreases with increasing altitude.",
  "ऊँचाई बढ़ने के साथ तापमान सामान्यतः घटता है।",
  3,
  "Statement-I is incorrect but Statement-II is correct. Shimla stands at about 2,200 m, so its summer days are around 25 °C while Delhi's often cross 40 °C -- the reason the British made hill stations their summer retreats.",
  "कथन-I गलत है पर कथन-II सही है। शिमला लगभग 2,200 मीटर की ऊँचाई पर है, इसलिए वहाँ ग्रीष्म के दिन लगभग 25 °C रहते हैं, जबकि दिल्ली में तापमान प्रायः 40 °C से ऊपर चला जाता है; इसीलिए अंग्रेज़ों ने पहाड़ी स्थानों को अपना ग्रीष्मकालीन ठिकाना बनाया।",
  f"{NC9} -- Climate.",
  "igeo-shimla-altitude-easy")

A(PH, "easy",
  "The Peninsular plateau is one of the oldest landmasses of India.",
  "प्रायद्वीपीय पठार भारत के सबसे पुराने भूभागों में से एक है।",
  "It was formed by the collision of the Indian plate with the Eurasian plate.",
  "यह भारतीय प्लेट और यूरेशियाई प्लेट की टक्कर से बना।",
  2,
  "Statement-I is correct but Statement-II is incorrect. The plateau is a part of the ancient Gondwana landmass, made of rocks that are hundreds of millions of years old. It was the collision of the Indian plate with the Eurasian plate that raised the Himalaya, much later.",
  "कथन-I सही है पर कथन-II गलत है। यह पठार प्राचीन गोंडवाना भूभाग का भाग है, जो करोड़ों वर्ष पुरानी चट्टानों से बना है। भारतीय प्लेट और यूरेशियाई प्लेट की टक्कर से तो बहुत बाद में हिमालय उठा।",
  f"{NC9} -- Physical Features of India.",
  "igeo-peninsula-oldest-easy")

A(PH, "hard",
  "The Aravallis are the oldest fold mountains of India.",
  "अरावली भारत के सबसे पुराने वलित पर्वत हैं।",
  "The Aravallis lie parallel to the path of the Arabian Sea branch of the monsoon.",
  "अरावली मानसून की अरब सागर शाखा के मार्ग के समानांतर स्थित है।",
  1,
  "Both statements are correct, but Statement-II does not explain Statement-I. The Aravallis are old because they were folded in the Precambrian era and have since been worn down to broken, residual hills running from Gujarat to Delhi. Their alignment parallel to the monsoon winds is a separate fact -- it explains why they fail to stop the winds and why the Thar stays dry, not their age.",
  "दोनों कथन सही हैं, पर कथन-II कथन-I की व्याख्या नहीं करता। अरावली इसलिए पुराने हैं कि वे पूर्व-कैम्ब्रियन युग में वलित हुए थे और तब से घिसकर गुजरात से दिल्ली तक फैली टूटी-फूटी, अवशिष्ट पहाड़ियाँ रह गए हैं। मानसूनी पवनों के समानांतर उनकी दिशा एक अलग तथ्य है; यह बताता है कि वे पवनों को क्यों नहीं रोक पाते और थार क्यों शुष्क रहता है, उनकी आयु नहीं।",
  f"{NC11I} -- Structure and Physiography; Climate.",
  "igeo-aravalli-old-parallel-monsoon")

A(PH, "hard",
  "The Coromandel coast of Tamil Nadu receives much of its annual rainfall between October and December.",
  "तमिलनाडु के कोरोमंडल तट पर वार्षिक वर्षा का बड़ा भाग अक्टूबर और दिसंबर के बीच होता है।",
  "During this season the north-east monsoon winds pick up moisture while crossing the Bay of Bengal before reaching the coast.",
  "इस ऋतु में उत्तर-पूर्वी मानसूनी पवनें तट तक पहुँचने से पहले बंगाल की खाड़ी को पार करते हुए नमी ग्रहण करती हैं।",
  0,
  "Both Statements II and III are correct, and both explain Statement I. The north-east winds, which are dry over land, become moist over the Bay and bring rain to Tamil Nadu and the adjoining coast, while cyclonic depressions that form over the Bay in October-November add heavy spells. In the south-west monsoon season the same coast lies in the rain shadow of the Western Ghats and parallel to the Bay of Bengal branch, so it gets relatively little rain.",
  "कथन II और III दोनों सही हैं, और दोनों कथन I की व्याख्या करते हैं। स्थल पर शुष्क रहने वाली उत्तर-पूर्वी पवनें खाड़ी के ऊपर नम हो जाती हैं और तमिलनाडु तथा उससे लगे तट पर वर्षा लाती हैं, जबकि अक्टूबर-नवंबर में खाड़ी पर बनने वाले चक्रवाती अवदाब भारी वर्षा की अवधियाँ जोड़ते हैं। दक्षिण-पश्चिम मानसून की ऋतु में यही तट पश्चिमी घाट के वृष्टि-छाया क्षेत्र में और बंगाल की खाड़ी शाखा के समानांतर रहता है, इसलिए वहाँ अपेक्षाकृत कम वर्षा होती है।",
  f"{NC11I} -- Climate; {IMD} -- North-east monsoon.",
  "igeo-coromandel-winter-rain",
  s3="Cyclonic depressions from the Bay of Bengal often cross the coast in this season.",
  s3_hi="इस ऋतु में बंगाल की खाड़ी के चक्रवाती अवदाब प्रायः तट को पार करते हैं।")

# ================================================================ PAIRS (medium 2, easy 1, hard 1)
P(PH, "easy", "Consider the following pairs of plateaus and the States in which they mainly lie:",
  "पठारों और उन राज्यों के निम्नलिखित युग्मों पर विचार कीजिए जिनमें वे मुख्य रूप से स्थित हैं:",
  ["Chotanagpur plateau : Jharkhand", "Malwa plateau : Madhya Pradesh", "Baghelkhand : Gujarat", "Dandakaranya : Chhattisgarh and Odisha"],
  ["छोटानागपुर पठार : झारखंड", "मालवा पठार : मध्य प्रदेश", "बघेलखंड : गुजरात", "दंडकारण्य : छत्तीसगढ़ और ओडिशा"],
  2,
  "Pairs 1, 2 and 4 are correct. The Chotanagpur plateau covers most of Jharkhand; the Malwa plateau lies in western Madhya Pradesh around Indore and Ujjain; and the forested Dandakaranya spreads over southern Chhattisgarh (Bastar), Odisha and the neighbouring parts of Telangana and Andhra Pradesh. "
  "Pair 3 is wrong: Baghelkhand lies in north-eastern Madhya Pradesh and the adjoining part of Uttar Pradesh, around Rewa.",
  "युग्म 1, 2 और 4 सही हैं। छोटानागपुर पठार झारखंड के अधिकांश भाग में फैला है; मालवा पठार पश्चिमी मध्य प्रदेश में इंदौर और उज्जैन के आसपास है; और वनों से भरा दंडकारण्य दक्षिणी छत्तीसगढ़ (बस्तर), ओडिशा और तेलंगाना तथा आंध्र प्रदेश के पड़ोसी भागों में फैला है। "
  "युग्म 3 गलत है: बघेलखंड रीवा के आसपास, उत्तर-पूर्वी मध्य प्रदेश और उत्तर प्रदेश के निकटवर्ती भाग में है।",
  f"{NC11I} -- Structure and Physiography.",
  "igeo-plateaus-states-pairs-easy")

P(PH, "medium", "Consider the following pairs of Himalayan passes and the States/UTs in which they lie:",
  "हिमालयी दर्रों और उन राज्यों/केंद्र शासित प्रदेशों के निम्नलिखित युग्मों पर विचार कीजिए जिनमें वे स्थित हैं:",
  ["Shipki La : Himachal Pradesh", "Nathu La : Sikkim", "Bomdi La : Arunachal Pradesh", "Lipulekh : Uttarakhand"],
  ["शिपकी ला : हिमाचल प्रदेश", "नाथू ला : सिक्किम", "बोमडी ला : अरुणाचल प्रदेश", "लिपुलेख : उत्तराखंड"],
  3,
  "All four pairs are correct. Shipki La, where the Satluj enters India, links Himachal with Tibet; Nathu La, on the old silk route, links Sikkim with the Chumbi valley; Bomdi La, on the road to Tawang, is in western Arunachal Pradesh; and Lipulekh, in Pithoragarh district, is used by pilgrims to Kailash-Mansarovar. "
  "A student who expects one mismatch will fall for 'Only three pairs'.",
  "चारों युग्म सही हैं। शिपकी ला, जहाँ से सतलुज भारत में प्रवेश करती है, हिमाचल को तिब्बत से जोड़ता है; पुराने रेशम मार्ग पर स्थित नाथू ला सिक्किम को चुंबी घाटी से जोड़ता है; तवांग के रास्ते पर स्थित बोमडी ला पश्चिमी अरुणाचल प्रदेश में है; और पिथौरागढ़ ज़िले का लिपुलेख कैलाश-मानसरोवर के तीर्थयात्रियों द्वारा प्रयुक्त होता है। "
  "जो विद्यार्थी एक बेमेल की अपेक्षा करता है, वह 'केवल तीन युग्म' के जाल में फँसेगा।",
  f"{NC9} -- Physical Features of India.",
  "igeo-himalayan-passes-pairs")

P(PH, "medium", "Consider the following pairs of coastal stretches and the States along which they lie:",
  "तटीय खंडों और उन राज्यों के निम्नलिखित युग्मों पर विचार कीजिए जिनके साथ वे स्थित हैं:",
  ["Konkan coast : Maharashtra", "Kanara coast : Karnataka", "Malabar coast : Kerala", "Northern Circars : West Bengal"],
  ["कोंकण तट : महाराष्ट्र", "कन्नड़ (कनारा) तट : कर्नाटक", "मालाबार तट : केरल", "उत्तरी सरकार : पश्चिम बंगाल"],
  2,
  "Pairs 1, 2 and 3 are correct: the western coastal plain is divided into the Konkan (Mumbai to Goa), the Kanara or Karnataka coast, and the Malabar coast of Kerala. "
  "Pair 4 is wrong: the Northern Circars are the northern part of the eastern coastal plain, along Odisha and northern Andhra Pradesh; its southern part, along Tamil Nadu, is the Coromandel coast.",
  "युग्म 1, 2 और 3 सही हैं: पश्चिमी तटीय मैदान कोंकण (मुंबई से गोवा), कन्नड़ या कर्नाटक तट और केरल के मालाबार तट में बँटा है। "
  "युग्म 4 गलत है: उत्तरी सरकार पूर्वी तटीय मैदान का उत्तरी भाग है, जो ओडिशा और उत्तरी आंध्र प्रदेश के साथ है; इसका तमिलनाडु के साथ वाला दक्षिणी भाग कोरोमंडल तट है।",
  f"{NC9} -- Physical Features of India.",
  "igeo-coasts-states-pairs")

P(PH, "hard", "Consider the following pairs of hills and the States in which they lie:",
  "पहाड़ियों और उन राज्यों के निम्नलिखित युग्मों पर विचार कीजिए जिनमें वे स्थित हैं:",
  ["Mikir hills : Assam", "Nallamala hills : Andhra Pradesh", "Shevaroy hills : Kerala", "Rajmahal hills : West Bengal"],
  ["मिकिर पहाड़ियाँ : असम", "नल्लामला पहाड़ियाँ : आंध्र प्रदेश", "शेवरॉय पहाड़ियाँ : केरल", "राजमहल पहाड़ियाँ : पश्चिम बंगाल"],
  1,
  "Pairs 1 and 2 are correct: the Mikir (Karbi Anglong) hills, an outlier of the Meghalaya plateau, lie in Assam; the Nallamala hills of the Eastern Ghats, cut through by the Krishna at Srisailam, are in Andhra Pradesh. "
  "Pair 3 is wrong: the Shevaroy hills, with the hill station of Yercaud, are in Tamil Nadu's Salem district. "
  "Pair 4 is wrong: the Rajmahal hills lie in the Santhal Parganas of Jharkhand, close to the West Bengal border.",
  "युग्म 1 और 2 सही हैं: मेघालय पठार का एक अलग हुआ भाग, मिकिर (कार्बी आंगलोंग) पहाड़ियाँ, असम में हैं; पूर्वी घाट की नल्लामला पहाड़ियाँ, जिन्हें श्रीशैलम पर कृष्णा काटती है, आंध्र प्रदेश में हैं। "
  "युग्म 3 गलत है: पहाड़ी स्थान येरकॉड वाली शेवरॉय पहाड़ियाँ तमिलनाडु के सेलम ज़िले में हैं। "
  "युग्म 4 गलत है: राजमहल पहाड़ियाँ झारखंड के संथाल परगना में, पश्चिम बंगाल की सीमा के पास हैं।",
  f"{NC11I} -- Structure and Physiography.",
  "igeo-hills-states-pairs")

if __name__ == "__main__":
    write("geo_l2_t13_physiography.sql")
