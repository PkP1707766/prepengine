# -*- coding: utf-8 -*-
"""Level 2 · Test 14 (Geography 3: Resources, Transport and Human Geography) -- depth audit of 2026-10-04, part A:
Resources: Minerals, Energy & Agriculture (docs/upsc-question-design-standard.md §6). Part B
(upg_l2_t14_geo_b.py) has Transport, Ports & Human Geography and the tags for the kept rows.

Before the audit the test had analytic 22, precision 12, recall 68. Part A rewrites 17 recall rows in place
with the same concept id, type and difficulty:
  - analytic: why Jharia's families are resettled, how Operation Flood worked, what fills the zaid gap,
    what a biogas plant gives a village and why it slows in the cold, why thorium shapes the nuclear plan, how Koyna uses the Ghats,
    why north-eastern coal suits steel badly, what the Indira Gandhi Canal brought and cost, why drip
    irrigation saves water, why millets suit dry land, and why jute is wanted again;
  - precision: near-miss versions of the 'revolutions', India's crop ranks, iron ores, the coffee and
    rubber States, the foreign partners of the steel plants, and fossil fuels.
Leaks avoided while drafting:
  - wheat, mustard or gram in the zaid case (the mustard-wheat and cropping-seasons rows), and paddy sown
    with the monsoon (the cropping-seasons row's statement 1);
  - weight-losing raw materials (states the pit-head AR's Statement II), so the Neyveli MCQ was left;
  - biogas as the non-fossil key (the biogas row says it is made from dung), so uranium is the key;
  - jute in the dry west as a distractor (the jute AR's false Statement I)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write_updates, CODE
from polity_common import C3, C4, T2

d.SUBJECT = "Geography"
d.REQUIRE_CRAFT = True
RS = "Resources: Minerals, Energy & Agriculture"
NC10 = "NCERT Class X, Contemporary India II"
NC12 = "NCERT Class XII, India: People and Economy"

# ================================================================ MCQs (5)
M(RS, "medium", "Thousands of families in the Jharia coalfield of Jharkhand have had to be resettled in recent decades. The main reason is that:",
  "झारखंड के झरिया कोयला क्षेत्र में हाल के दशकों में हज़ारों परिवारों को पुनर्वासित करना पड़ा है। इसका मुख्य कारण यह है कि:",
  ["fires burning for a century in the coal seams below have made the ground unstable and the air toxic",
   "the coalfield lies in a flood plain that the Damodar submerges completely in every monsoon season",
   "the coal seams there have been completely exhausted, so the mines and the towns have had to close",
   "the land is needed for a large new reservoir to be built on the Subarnarekha river downstream of it"],
  ["नीचे की कोयला परतों में सौ वर्षों से जलती आग ने भूमि को अस्थिर और वायु को विषैला बना दिया है",
   "कोयला क्षेत्र ऐसे बाढ़-मैदान में है जिसे दामोदर हर मानसून में पूरी तरह डुबो देती है",
   "वहाँ की कोयला परतें पूरी तरह समाप्त हो चुकी हैं, इसलिए खदानें और नगर बंद करने पड़े हैं",
   "भूमि की आवश्यकता उसके नीचे की ओर सुवर्णरेखा नदी पर बनने वाले एक बड़े नए जलाशय के लिए है"],
  0,
  "Jharia, near Dhanbad in the Damodar valley, is India's main source of prime coking coal. Fires in its underground seams, first noticed in 1916 and spread by unscientific mining, still burn; they cause subsidence, open cracks that vent smoke and gas, and bring down homes and roads, so the Jharia Master Plan provides for moving families out of the fire- and subsidence-affected areas. "
  "The field still holds large reserves; it is the fires, not exhaustion or a dam, that drive the resettlement.",
  "दामोदर घाटी में धनबाद के पास झरिया भारत के उत्तम कोकिंग कोयले का मुख्य स्रोत है। इसकी भूमिगत परतों की आग, जो पहली बार 1916 में दिखी और अवैज्ञानिक खनन से फैली, अब भी जल रही है; इससे भूमि धँसती है, धुआँ और गैस छोड़ने वाली दरारें खुलती हैं, और घर तथा सड़कें गिरती हैं, इसलिए झरिया मास्टर प्लान आग और धँसाव से प्रभावित क्षेत्रों से परिवारों को हटाने का प्रावधान करता है। "
  "क्षेत्र में अब भी बड़े भंडार हैं; पुनर्वास का कारण आग है, भंडार का ख़त्म होना या कोई बाँध नहीं।",
  "Ministry of Coal -- Jharia Master Plan.", "res-jharia-coalfield", craft="linkage")

M(RS, "medium", "'Operation Flood', launched in 1970, helped make India the world's largest producer of milk. It did so mainly by:",
  "1970 में शुरू हुए 'ऑपरेशन फ़्लड' ने भारत को संसार का सबसे बड़ा दुग्ध उत्पादक बनाने में मदद की। इसने ऐसा मुख्यतः किस प्रकार किया?",
  ["linking village milk co-operatives to city markets through a national milk grid",
   "importing high-yielding cattle breeds to replace India's local cows and buffaloes",
   "setting up large state-owned dairy farms on the edge of each of the major cities",
   "paying farmers a subsidy to switch from growing grain to keeping dairy animals"],
  ["गाँवों की दुग्ध सहकारी समितियों को राष्ट्रीय दुग्ध ग्रिड के माध्यम से शहरी बाज़ारों से जोड़कर",
   "भारत की देशी गायों और भैंसों के स्थान पर अधिक उपज वाली विदेशी नस्लें आयात करके",
   "हर बड़े शहर के किनारे बड़े सरकारी डेयरी फ़ार्म स्थापित करके",
   "किसानों को अनाज उगाने के बजाय दुधारू पशु पालने के लिए सब्सिडी देकर"],
  0,
  "Under the National Dairy Development Board, led by Verghese Kurien, Operation Flood spread the Anand (Amul) model of village co-operatives, which collected milk twice a day from small producers, chilled and processed it, and sold it in cities through a national grid of chilling plants, dairies and rail tankers. The farmers, mostly with one or two animals, got a steady market and a fair price. "
  "It was not built on imported breeds or state farms; donated milk powder was sold only to raise money for the programme.",
  "राष्ट्रीय डेयरी विकास बोर्ड के अधीन, वर्गीज़ कुरियन के नेतृत्व में, ऑपरेशन फ़्लड ने गाँवों की सहकारी समितियों के आणंद (अमूल) मॉडल को फैलाया, जो छोटे उत्पादकों से दिन में दो बार दूध इकट्ठा करतीं, उसे ठंडा और संसाधित करतीं, और शीतलन संयंत्रों, डेयरियों और रेल टैंकरों के राष्ट्रीय ग्रिड से शहरों में बेचतीं। प्रायः एक-दो पशुओं वाले किसानों को स्थिर बाज़ार और उचित मूल्य मिला। "
  "यह आयातित नस्लों या सरकारी फ़ार्मों पर नहीं टिका था; दान में मिला दूध-पाउडर केवल कार्यक्रम के लिए धन जुटाने हेतु बेचा गया।",
  "National Dairy Development Board -- Operation Flood.", "res-operation-flood-milk", craft="linkage")

M(RS, "medium", "A farmer in Uttar Pradesh has a field lying empty from April to late June, between one season's harvest and the next season's sowing. With irrigation, the crops she could best grow in this gap are:",
  "उत्तर प्रदेश की एक किसान का खेत अप्रैल से जून के अंत तक, एक ऋतु की कटाई और अगली ऋतु की बुआई के बीच, ख़ाली रहता है। सिंचाई के साथ इस अंतराल में वह सबसे उपयुक्त रूप से कौन-सी फ़सलें उगा सकती है?",
  ["watermelon and cucumber", "barley and linseed", "soybean and cotton", "arhar (pigeon pea) and jowar"],
  ["तरबूज़ और खीरा", "जौ और अलसी", "सोयाबीन और कपास", "अरहर और ज्वार"],
  0,
  "The gap between the rabi harvest and the kharif sowing is the zaid season, roughly March to June: hot and dry, so it suits quick summer crops grown with irrigation, such as watermelon, muskmelon, cucumber, vegetables and fodder. "
  "Barley and linseed are rabi crops, sown in winter; soybean, cotton, arhar and jowar are kharif crops, sown with the monsoon and harvested in autumn.",
  "रबी की कटाई और ख़रीफ़ की बुआई के बीच का अंतराल ज़ायद ऋतु है, मोटे तौर पर मार्च से जून: गर्म और शुष्क, इसलिए सिंचाई से उगाई जाने वाली जल्दी तैयार होने वाली ग्रीष्म फ़सलों, जैसे तरबूज़, ख़रबूज़ा, खीरा, सब्ज़ियाँ और चारा, के लिए उपयुक्त है। "
  "जौ और अलसी रबी फ़सलें हैं, जो सर्दियों में बोई जाती हैं; सोयाबीन, कपास, अरहर और ज्वार ख़रीफ़ फ़सलें हैं, जो मानसून के साथ बोई और शरद में काटी जाती हैं।",
  NC10, "res-zaid-watermelon", craft="application")

M(RS, "easy", "Which one of the following is NOT a fossil fuel?",
  "निम्नलिखित में से कौन-सा जीवाश्म ईंधन नहीं है?",
  ["Uranium", "Lignite", "Natural gas", "Petroleum"],
  ["यूरेनियम", "लिग्नाइट", "प्राकृतिक गैस", "पेट्रोलियम"],
  0,
  "Fossil fuels -- coal, including lignite, petroleum and natural gas -- formed over millions of years from the buried remains of plants and animals, and release their energy when their carbon is burnt. Uranium is non-renewable too, but it is a mineral mined from rocks, and it gives energy by nuclear fission, not by burning. "
  "Lignite, or brown coal, is a young, low-grade coal with much moisture, but it is still a fossil fuel.",
  "जीवाश्म ईंधन, यानी लिग्नाइट सहित कोयला, पेट्रोलियम और प्राकृतिक गैस, लाखों वर्षों में दबे हुए पौधों और जीवों के अवशेषों से बने हैं, और अपने कार्बन के जलने पर ऊर्जा देते हैं। यूरेनियम भी अनवीकरणीय है, पर वह चट्टानों से निकाला जाने वाला खनिज है, और जलने से नहीं, नाभिकीय विखंडन से ऊर्जा देता है। "
  "लिग्नाइट, या भूरा कोयला, अधिक नमी वाला नया, निम्न श्रेणी का कोयला है, पर फिर भी जीवाश्म ईंधन है।",
  NC10, "res-fossil-fuel-natural-gas-easy", craft="precision")

M(RS, "easy", "Jute, the 'golden fibre', is again in demand in India and abroad. The main reason is that:",
  "'सुनहरा रेशा' जूट भारत और विदेश में फिर माँग में है। इसका मुख्य कारण यह है कि:",
  ["it is a biodegradable substitute for plastic packaging",
   "it has replaced cotton as the main fibre for everyday clothing",
   "its seeds yield an oil now used widely as a cooking medium",
   "it is the only natural fibre that needs no processing at all"],
  ["यह प्लास्टिक पैकेजिंग का जैव-अपघटनीय विकल्प है",
   "इसने रोज़मर्रा के कपड़ों के मुख्य रेशे के रूप में कपास का स्थान ले लिया है",
   "इसके बीजों से मिलने वाला तेल अब खाना पकाने में व्यापक रूप से काम आता है",
   "यह अकेला प्राकृतिक रेशा है जिसे किसी प्रसंस्करण की आवश्यकता नहीं होती"],
  0,
  "Jute bags, sacks, mats and packaging break down naturally, so curbs on single-use plastic and the demand for green packaging have revived interest in them, and India requires much of its foodgrain and sugar to be packed in jute under the Jute Packaging Materials Act, 1987. "
  "Jute is a coarse fibre unsuited to most clothing, it is valued for its fibre rather than for oil, and it has to be retted in water and stripped before it can be used.",
  "जूट के थैले, बोरे, चटाइयाँ और पैकेजिंग स्वाभाविक रूप से नष्ट हो जाते हैं, इसलिए एकल-उपयोग प्लास्टिक पर रोक और पर्यावरण-अनुकूल पैकेजिंग की माँग ने इनमें रुचि लौटाई है, और भारत जूट पैकेजिंग सामग्री अधिनियम, 1987 के तहत अपने बहुत-से अनाज और चीनी को जूट में पैक करना अनिवार्य करता है। "
  "जूट एक मोटा रेशा है जो अधिकांश कपड़ों के लिए उपयुक्त नहीं है, इसका मूल्य तेल के लिए नहीं रेशे के लिए है, और उपयोग से पहले इसे पानी में सड़ाकर छीलना पड़ता है।",
  "Ministry of Textiles -- Jute Packaging Materials (Compulsory Use in Packing Commodities) Act, 1987.", "res-golden-fibre-jute-easy", craft="linkage")

# ================================================================ pairs (1)
P(RS, "easy", "Consider the following pairs of 'revolutions' and the fields they relate to:",
  "'क्रांतियों' और उनसे संबंधित क्षेत्रों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Yellow Revolution : Oilseeds", "Blue Revolution : Fisheries", "Silver Revolution : Milk", "Golden Revolution : Horticulture and honey"],
  ["पीली क्रांति : तिलहन", "नीली क्रांति : मत्स्य पालन", "रजत क्रांति : दूध", "स्वर्णिम क्रांति : बाग़बानी और शहद"],
  2,
  "Three pairs are correct. The Yellow Revolution raised oilseed output through the Technology Mission on Oilseeds from 1986; the Blue Revolution boosted fisheries and aquaculture; and the Golden Revolution refers to the growth of horticulture and honey. "
  "Pair 3 is the near-miss: milk is the White Revolution; the Silver Revolution relates to eggs and poultry.",
  "तीन युग्म सही हैं। पीली क्रांति ने 1986 से तिलहन प्रौद्योगिकी मिशन के माध्यम से तिलहन उत्पादन बढ़ाया; नीली क्रांति ने मत्स्य पालन और जलकृषि को बढ़ावा दिया; और स्वर्णिम क्रांति बाग़बानी और शहद की वृद्धि से जुड़ी है। "
  "युग्म 3 निकट-भ्रम है: दूध श्वेत क्रांति है; रजत क्रांति अंडों और मुर्गीपालन से जुड़ी है।",
  NC12, "res-revolutions-pairs-easy", craft="precision")

# ================================================================ statements (11)
S(RS, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["A biogas plant gives a household both fuel and manure, since what is left after the gas is drawn off is a rich fertiliser.",
   "A biogas plant works best in very cold weather, since low temperatures speed up the digestion of the dung."],
  ["बायोगैस संयंत्र एक परिवार को ईंधन और खाद दोनों देता है, क्योंकि गैस निकालने के बाद बचा पदार्थ समृद्ध उर्वरक है।",
   "बायोगैस संयंत्र बहुत ठंडे मौसम में सबसे अच्छा काम करता है, क्योंकि कम तापमान गोबर के पाचन को तेज़ करता है।"],
  T2, 0,
  "Only statement 1 is correct. In a biogas plant, cattle dung and other organic waste decompose without air, giving a gas that is mostly methane, used for cooking and lighting; the digested slurry is a better manure than dung cakes, which are burnt and lost, so the plant saves both fuel wood and soil fertility. "
  "Statement 2 is the reverse: the bacteria that make the gas work fastest at about 30-40 degrees Celsius, and below about 15 degrees gas output falls sharply, which is why plants in cold hill areas give little gas in winter unless they are insulated or warmed.",
  "केवल कथन 1 सही है। बायोगैस संयंत्र में गोबर और अन्य जैविक कचरा बिना वायु के सड़ता है, जिससे मुख्यतः मीथेन वाली गैस बनती है, जो खाना पकाने और रोशनी के काम आती है; बची हुई सड़ी गाद उपलों से बेहतर खाद है, जो जलकर नष्ट हो जाते हैं, इसलिए संयंत्र ईंधन-लकड़ी और मिट्टी की उर्वरता दोनों बचाता है। "
  "कथन 2 उलटा है: गैस बनाने वाले जीवाणु लगभग 30-40 डिग्री सेल्सियस पर सबसे तेज़ काम करते हैं, और लगभग 15 डिग्री से नीचे गैस उत्पादन बहुत गिर जाता है, इसीलिए ठंडे पहाड़ी क्षेत्रों के संयंत्र सर्दियों में, ऊष्मारोधन या गर्मी के बिना, कम गैस देते हैं।",
  NC10, "res-biogas-geothermal-easy", craft="linkage")

S(RS, "hard", "Consider the following statements about atomic minerals and nuclear energy in India:",
  "भारत में परमाणु खनिजों और नाभिकीय ऊर्जा के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The monazite sands of the Kerala coast are a source of thorium.",
   "Jaduguda in Jharkhand has uranium mines.",
   "The Tummalapalle uranium deposit lies in Karnataka.",
   "Because India has far more thorium than uranium, its three-stage nuclear power programme aims ultimately at using thorium."],
  ["केरल तट की मोनाज़ाइट रेत थोरियम का स्रोत है।",
   "झारखंड के जादूगोड़ा में यूरेनियम की खदानें हैं।",
   "तुम्मलपल्ले यूरेनियम भंडार कर्नाटक में है।",
   "चूँकि भारत में यूरेनियम की तुलना में थोरियम बहुत अधिक है, इसलिए इसका त्रि-चरणीय नाभिकीय ऊर्जा कार्यक्रम अंततः थोरियम के उपयोग को लक्षित करता है।"],
  C4, 2,
  "Statements 1, 2 and 4 are correct. India has among the world's largest thorium reserves, in the monazite beach sands of Kerala, Tamil Nadu and Odisha, but only modest uranium, mined at Jaduguda in the Singhbhum belt since 1967. Homi Bhabha's plan follows from that imbalance: natural-uranium reactors in the first stage, fast breeder reactors in the second, and thorium-based reactors in the third. "
  "Statement 3 is wrong: Tummalapalle lies in Kadapa district of Andhra Pradesh.",
  "कथन 1, 2 और 4 सही हैं। केरल, तमिलनाडु और ओडिशा की मोनाज़ाइट तटीय रेत में भारत के पास संसार के सबसे बड़े थोरियम भंडारों में से कुछ हैं, पर यूरेनियम सीमित है, जो 1967 से सिंहभूम पट्टी के जादूगोड़ा में निकाला जाता है। होमी भाभा की योजना इसी असंतुलन से निकलती है: पहले चरण में प्राकृतिक-यूरेनियम रिएक्टर, दूसरे में फ़ास्ट ब्रीडर रिएक्टर और तीसरे में थोरियम-आधारित रिएक्टर। "
  "कथन 3 गलत है: तुम्मलपल्ले आंध्र प्रदेश के कडप्पा ज़िले में है।",
  "Department of Atomic Energy -- India's three-stage nuclear power programme.", "res-atomic-minerals-three-stage", craft="linkage")

S(RS, "hard", "Consider the following statements about hydroelectric projects:",
  "जलविद्युत परियोजनाओं के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Subansiri Lower project lies on the border of Assam and Arunachal Pradesh.",
   "The Salal project is on the Chenab.",
   "The Koyna project generates power by sending the water of a river on the plateau down the steep western face of the Ghats to power stations near the coast."],
  ["सुबनसिरी लोअर परियोजना असम और अरुणाचल प्रदेश की सीमा पर है।",
   "सलाल परियोजना चिनाब पर है।",
   "कोयना परियोजना पठार पर बहने वाली एक नदी के पानी को घाट के खड़े पश्चिमी ढाल से नीचे तट के पास के बिजलीघरों तक भेजकर बिजली बनाती है।"],
  C3, 2,
  "All three are correct. The 2,000 MW Subansiri Lower project of NHPC stands at Gerukamukh on the Assam-Arunachal border. Salal, in Reasi district of Jammu and Kashmir, is a run-of-the-river project on the Chenab. "
  "The Koyna, a tributary of the Krishna, flows east on the Deccan plateau, but at Koyna the dammed water is diverted west through tunnels and dropped several hundred metres down the scarp of the Western Ghats to powerhouses on the Konkan side -- using the Ghats' steep edge as the head that drives the turbines.",
  "तीनों कथन सही हैं। NHPC की 2,000 मेगावाट की सुबनसिरी लोअर परियोजना असम-अरुणाचल सीमा पर गेरुकामुख में है। जम्मू और कश्मीर के रियासी ज़िले में सलाल चिनाब पर नदी-प्रवाह परियोजना है। "
  "कृष्णा की सहायक नदी कोयना दक्कन पठार पर पूर्व की ओर बहती है, पर कोयना में बाँधा गया पानी सुरंगों से पश्चिम की ओर मोड़कर पश्चिमी घाट के कगार से कई सौ मीटर नीचे कोंकण की ओर के बिजलीघरों में गिराया जाता है, यानी घाट के खड़े किनारे को टरबाइन चलाने वाली ऊँचाई के रूप में उपयोग किया जाता है।",
  NC12, "res-hydro-subansiri-salal-koyna", craft="linkage")

S(RS, "medium", "Consider the following statements about coal in India:",
  "भारत में कोयले के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Most of India's coal reserves are of Gondwana age.",
   "The tertiary coal of the north-eastern States is high in sulphur, which makes it less suited to metallurgical use.",
   "Anthracite is the most abundant type of coal in India."],
  ["भारत के अधिकांश कोयला भंडार गोंडवाना काल के हैं।",
   "उत्तर-पूर्वी राज्यों के टर्शियरी कोयले में गंधक अधिक है, जिससे यह धातुकर्मीय उपयोग के लिए कम उपयुक्त है।",
   "एन्थ्रेसाइट भारत में सबसे प्रचुर प्रकार का कोयला है।"],
  C3, 1,
  "Statements 1 and 2 are correct. About 98 per cent of India's coal lies in Gondwana formations, a little over 200 million years old, in the valleys of the Damodar, the Mahanadi, the Godavari and the Son. The younger tertiary coal of Assam, Meghalaya, Arunachal Pradesh and Nagaland is friable and rich in sulphur, which harms the iron and the furnaces, so it is used mostly for fuel and not for steel-making. "
  "Statement 3 is wrong: most Indian coal is bituminous, and much of it has a high ash content; anthracite, the hardest coal, is found only in small quantities in Jammu and Kashmir.",
  "कथन 1 और 2 सही हैं। भारत का लगभग 98 प्रतिशत कोयला दामोदर, महानदी, गोदावरी और सोन घाटियों की गोंडवाना संरचनाओं में है, जो 20 करोड़ वर्ष से कुछ अधिक पुरानी हैं। असम, मेघालय, अरुणाचल प्रदेश और नागालैंड का नया टर्शियरी कोयला भुरभुरा और गंधक-समृद्ध है, जो लोहे और भट्ठियों को हानि पहुँचाता है, इसलिए यह मुख्यतः ईंधन के रूप में काम आता है, इस्पात बनाने में नहीं। "
  "कथन 3 गलत है: अधिकांश भारतीय कोयला बिटुमिनस है, और उसके बड़े भाग में राख अधिक है; सबसे कठोर कोयला एन्थ्रेसाइट केवल थोड़ी मात्रा में जम्मू और कश्मीर में मिलता है।",
  NC12, "res-coal-gondwana-tertiary", craft="linkage")

S(RS, "medium", "Consider the following statements about India's place in world agriculture:",
  "विश्व कृषि में भारत के स्थान के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["India is the largest producer of bananas in the world.",
   "India is the largest producer of pulses in the world.",
   "India is the largest producer of jute in the world.",
   "India is the largest producer of fruits and vegetables, taken together, in the world."],
  ["भारत संसार में केले का सबसे बड़ा उत्पादक है।",
   "भारत संसार में दालों का सबसे बड़ा उत्पादक है।",
   "भारत संसार में जूट का सबसे बड़ा उत्पादक है।",
   "फलों और सब्ज़ियों को मिलाकर भारत संसार में उनका सबसे बड़ा उत्पादक है।"],
  C4, 2,
  "Statements 1, 2 and 3 are correct: India leads the world in bananas, pulses and jute. Statement 4 is the near-miss: in fruits and vegetables taken together India is second, after China. India also imports pulses in years of shortfall, because its consumption is the highest in the world.",
  "कथन 1, 2 और 3 सही हैं: भारत केले, दालों और जूट में संसार में सबसे आगे है। कथन 4 निकट-भ्रम है: फलों और सब्ज़ियों को मिलाकर भारत चीन के बाद दूसरे स्थान पर है। कमी के वर्षों में भारत दालों का आयात भी करता है, क्योंकि उसकी खपत संसार में सबसे अधिक है।",
  "Food and Agriculture Organization -- FAOSTAT.", "res-india-world-rank-crops", craft="precision")

S(RS, "medium", "Consider the following statements about the Indira Gandhi Canal:",
  "इंदिरा गांधी नहर के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It draws water from the Harike barrage, near the confluence of the Satluj and the Beas.",
   "It has spread cultivation in the Thar, but seepage and over-irrigation have caused waterlogging and salinity in parts of its command area.",
   "It runs mainly through Gujarat."],
  ["यह सतलुज और ब्यास के संगम के पास हरिके बराज से पानी लेती है।",
   "इसने थार में खेती फैलाई है, पर रिसाव और अत्यधिक सिंचाई ने इसके कमान क्षेत्र के कुछ भागों में जलभराव और लवणता पैदा की है।",
   "यह मुख्यतः गुजरात से होकर बहती है।"],
  C3, 1,
  "Statements 1 and 2 are correct. One of the largest canal systems in the world, it starts at Harike in Punjab and runs parallel to the Pakistan border through western Rajasthan, bringing wheat, cotton, groundnut and mustard to districts such as Sri Ganganagar, Bikaner and Jaisalmer. "
  "But water-hungry crops, unlined channels and poor drainage on soils with a hard layer below have raised the water table in parts of the command area, bringing waterlogging and salt to the surface -- which is why the project now stresses lining, drainage and less thirsty crops. Statement 3 is wrong: it runs through Rajasthan.",
  "कथन 1 और 2 सही हैं। संसार की सबसे बड़ी नहर प्रणालियों में से एक यह पंजाब के हरिके से शुरू होकर पाकिस्तान सीमा के समानांतर पश्चिमी राजस्थान से गुज़रती है, और श्री गंगानगर, बीकानेर और जैसलमेर जैसे ज़िलों में गेहूँ, कपास, मूँगफली और सरसों लाई है। "
  "पर अधिक पानी माँगने वाली फ़सलें, बिना पक्की नालियाँ और नीचे कठोर परत वाली मिट्टियों पर ख़राब जल-निकास ने कमान क्षेत्र के कुछ भागों में भौम-जल स्तर उठाया है, जिससे जलभराव और सतह पर लवण आए हैं; इसीलिए परियोजना अब नालियों को पक्का करने, जल-निकास और कम पानी वाली फ़सलों पर ज़ोर देती है। कथन 3 गलत है: यह राजस्थान से होकर बहती है।",
  NC12, "res-indira-gandhi-canal", craft="linkage")

S(RS, "medium", "Consider the following statements about iron ore in India:",
  "भारत में लौह अयस्क के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Bailadila hills, known for high-grade haematite, lie in Jharkhand.",
   "Odisha is the largest producer of iron ore.",
   "Haematite has a higher iron content than magnetite."],
  ["उच्च श्रेणी के हेमेटाइट के लिए प्रसिद्ध बैलाडीला पहाड़ियाँ झारखंड में हैं।",
   "ओडिशा लौह अयस्क का सबसे बड़ा उत्पादक है।",
   "हेमेटाइट में मैग्नेटाइट से अधिक लोहा होता है।"],
  C3, 0,
  "Only statement 2 is correct: Odisha, with the Keonjhar, Sundargarh and Mayurbhanj deposits, produces more iron ore than any other State. Statement 1 is wrong: the Bailadila hills, named for their hump-like shape, are in Dantewada district of Chhattisgarh, and their haematite is among the finest in the world. "
  "Statement 3 reverses the two ores: magnetite, the finest ore, holds up to about 70 per cent iron, while haematite, the most important ore by quantity, holds about 50-60 per cent.",
  "केवल कथन 2 सही है: क्योंझर, सुंदरगढ़ और मयूरभंज के भंडारों के साथ ओडिशा किसी भी अन्य राज्य से अधिक लौह अयस्क का उत्पादन करता है। कथन 1 गलत है: कूबड़ जैसे आकार के कारण नामित बैलाडीला पहाड़ियाँ छत्तीसगढ़ के दंतेवाड़ा ज़िले में हैं, और उनका हेमेटाइट संसार के सर्वोत्तम में है। "
  "कथन 3 दोनों अयस्कों को उलट देता है: सबसे उत्तम अयस्क मैग्नेटाइट में लगभग 70 प्रतिशत तक लोहा होता है, जबकि मात्रा में सबसे महत्वपूर्ण हेमेटाइट में लगभग 50-60 प्रतिशत।",
  NC10, "res-iron-ore-bailadila-odisha", craft="precision")

S(RS, "medium", "Consider the following statements about irrigation in India:",
  "भारत में सिंचाई के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Canals irrigate the largest share of India's net irrigated area.",
   "Tank irrigation is important mainly in Punjab and Haryana.",
   "Drip irrigation saves water because it delivers water straight to the roots, cutting the losses to evaporation and run-off."],
  ["नहरें भारत के शुद्ध सिंचित क्षेत्र के सबसे बड़े भाग की सिंचाई करती हैं।",
   "तालाब सिंचाई मुख्यतः पंजाब और हरियाणा में महत्वपूर्ण है।",
   "टपक (ड्रिप) सिंचाई पानी बचाती है क्योंकि वह पानी सीधे जड़ों तक पहुँचाती है, जिससे वाष्पीकरण और बहाव से होने वाली हानि घटती है।"],
  C3, 0,
  "Only statement 3 is correct: by dripping water at the roots through pipes and emitters, drip irrigation can cut water use by a third or more compared with flooding a field, and it lets fertiliser be given with the water. "
  "Statement 1 is wrong: wells and tube-wells, drawing on groundwater, irrigate well over half of the net irrigated area; canals come second. Statement 2 is wrong: tanks -- small reservoirs that store monsoon run-off -- matter most on the hard rocks of the Peninsula, in Tamil Nadu, Andhra Pradesh, Telangana and Karnataka, where groundwater is scarce and the land is uneven.",
  "केवल कथन 3 सही है: पाइपों और उत्सर्जकों से जड़ों पर बूँद-बूँद पानी देकर टपक सिंचाई खेत को पानी से भरने की तुलना में पानी का उपयोग एक-तिहाई या उससे अधिक घटा सकती है, और पानी के साथ उर्वरक देने देती है। "
  "कथन 1 गलत है: भौम-जल लेने वाले कुएँ और नलकूप शुद्ध सिंचित क्षेत्र के आधे से कहीं अधिक भाग को सींचते हैं; नहरें दूसरे स्थान पर हैं। कथन 2 गलत है: तालाब, यानी मानसूनी बहाव को रोकने वाले छोटे जलाशय, प्रायद्वीप की कठोर चट्टानों पर, तमिलनाडु, आंध्र प्रदेश, तेलंगाना और कर्नाटक में, सबसे महत्वपूर्ण हैं, जहाँ भौम-जल कम है और भूमि ऊबड़-खाबड़ है।",
  NC12, "res-irrigation-sources", craft="linkage")

S(RS, "medium", "Consider the following statements about millets:",
  "मोटे अनाजों (मिलेट्स) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Jowar, bajra and ragi are millets.",
   "Millets suit dry regions because they need little water and tolerate poor soils and high temperatures.",
   "Rajasthan is the largest producer of bajra."],
  ["ज्वार, बाजरा और रागी मोटे अनाज हैं।",
   "मोटे अनाज शुष्क क्षेत्रों के लिए उपयुक्त हैं क्योंकि उन्हें कम पानी चाहिए और वे कमज़ोर मिट्टी और ऊँचे तापमान को सह लेते हैं।",
   "राजस्थान बाजरे का सबसे बड़ा उत्पादक है।"],
  C3, 2,
  "All three are correct. Millets -- promoted as 'Shree Anna' after India led the International Year of Millets in 2023 -- have short growing seasons and deep roots, so they grow on sandy or shallow soils with 40-75 cm of rain where rice and wheat would fail, and they are rich in fibre, iron and calcium. "
  "Bajra, the hardiest, is grown most widely in the dry west, and Rajasthan is its largest producer; ragi thrives in the red soils of dry Karnataka.",
  "तीनों कथन सही हैं। 2023 में भारत के नेतृत्व में अंतरराष्ट्रीय मोटा अनाज वर्ष के बाद 'श्री अन्न' के रूप में प्रचारित मोटे अनाजों की वृद्धि-अवधि छोटी और जड़ें गहरी होती हैं, इसलिए वे 40-75 सेमी वर्षा वाली रेतीली या उथली मिट्टियों पर उग जाते हैं जहाँ धान और गेहूँ विफल होंगे, और वे रेशे, लोहे और कैल्शियम से भरपूर हैं। "
  "सबसे कठोर बाजरा शुष्क पश्चिम में सबसे व्यापक रूप से उगाया जाता है, और राजस्थान इसका सबसे बड़ा उत्पादक है; रागी शुष्क कर्नाटक की लाल मिट्टियों में पनपती है।",
  NC10, "res-millets-ragi-bajra", craft="linkage")

S(RS, "medium", "Consider the following statements about plantation crops in India:",
  "भारत की बागान फ़सलों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Arabica coffee grown in India was first brought from Yemen.",
   "Kerala is the largest producer of coffee.",
   "Karnataka is the largest producer of natural rubber."],
  ["भारत में उगाई जाने वाली अरेबिका कॉफ़ी पहले यमन से लाई गई थी।",
   "केरल कॉफ़ी का सबसे बड़ा उत्पादक है।",
   "कर्नाटक प्राकृतिक रबड़ का सबसे बड़ा उत्पादक है।"],
  C3, 0,
  "Only statement 1 is correct: by tradition, coffee first came to the Baba Budan hills of Karnataka with seeds brought from Yemen in the seventeenth century. Statements 2 and 3 swap the two southern States: Karnataka grows about 70 per cent of India's coffee, in Kodagu, Chikkamagaluru and Hassan, while Kerala produces most of India's natural rubber, on the humid slopes of its midlands.",
  "केवल कथन 1 सही है: परंपरा के अनुसार कॉफ़ी सत्रहवीं सदी में यमन से लाए गए बीजों के साथ कर्नाटक की बाबा बुदन पहाड़ियों में पहली बार आई। कथन 2 और 3 दो दक्षिणी राज्यों को आपस में बदल देते हैं: कर्नाटक भारत की लगभग 70 प्रतिशत कॉफ़ी कोडगु, चिक्कमगलूरु और हासन में उगाता है, जबकि केरल अपने मध्य भाग की नम ढलानों पर भारत का अधिकांश प्राकृतिक रबड़ पैदा करता है।",
  NC10, "res-plantation-coffee-rubber", craft="precision")

S(RS, "medium", "Consider the following statements about the iron and steel industry:",
  "लौह और इस्पात उद्योग के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Bhilai steel plant was set up with the help of the United Kingdom.",
   "The Rourkela steel plant was set up with the help of the Soviet Union.",
   "The Durgapur steel plant was set up with the help of West Germany."],
  ["भिलाई इस्पात संयंत्र यूनाइटेड किंगडम की सहायता से स्थापित किया गया।",
   "राउरकेला इस्पात संयंत्र सोवियत संघ की सहायता से स्थापित किया गया।",
   "दुर्गापुर इस्पात संयंत्र पश्चिमी जर्मनी की सहायता से स्थापित किया गया।"],
  C3, 3,
  "None is correct; the three statements rotate the partners. In the Second Five Year Plan three public-sector plants were built with foreign help: Bhilai (Chhattisgarh) with the Soviet Union, Rourkela (Odisha) with West Germany and Durgapur (West Bengal) with the United Kingdom. Bokaro, later, was also built with Soviet help.",
  "कोई भी कथन सही नहीं है; तीनों कथन साझेदारों को घुमा देते हैं। दूसरी पंचवर्षीय योजना में तीन सार्वजनिक क्षेत्र के संयंत्र विदेशी सहायता से बने: भिलाई (छत्तीसगढ़) सोवियत संघ के साथ, राउरकेला (ओडिशा) पश्चिमी जर्मनी के साथ और दुर्गापुर (पश्चिम बंगाल) यूनाइटेड किंगडम के साथ। बाद में बोकारो भी सोवियत सहायता से बना।",
  NC12, "res-steel-plants-foreign-help", craft="precision")

if __name__ == "__main__":
    write_updates("upg_l2_t14_geo_a.sql", statuses=("draft", "published"))
