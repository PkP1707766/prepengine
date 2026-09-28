# -*- coding: utf-8 -*-
"""Level 2 · Test 9 (Environment 1: Ecology & Biodiversity) -- Flora, Fungi & Forests,
16 new bilingual rows against the live gap report: medium statement 6, easy statement 2,
hard statement 2, medium MCQ 1, easy MCQ 1, hard MCQ 1, medium Statement-I/II 1,
hard Statement-I/II/III 1, medium pairs 1. Concepts already in the bank (mangroves, khejri,
sandalwood/Cycas, lichens, seagrass, invasive plants, bamboo, orchid/Cuscuta, insectivorous
plants, Venus flytrap, gymnosperms, xerophytes, Neelakurinji) are not repeated."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Environment & Ecology"
F = "Flora, Fungi & Forests"
IUCN = "IUCN Red List of Threatened Species"
GEO11 = "NCERT Class XI, India: Physical Environment -- Natural Vegetation"
BIO11 = "NCERT Class XI, Biology -- Plant Kingdom"
MICRO12 = "NCERT Class XII, Biology -- Microbes in Human Welfare"

# ---------------------------------------------------------------- medium statements (6)
S(F, "medium", "Consider the following statements about fungi:",
  "कवकों (fungi) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Mycorrhizal fungi living with plant roots help the plant absorb phosphorus from the soil.",
   "The cell walls of fungi are made mainly of cellulose, as in green plants.",
   "Trichoderma, a fungus, is used as a biocontrol agent against several plant pathogens."],
  ["पौधों की जड़ों के साथ रहने वाले कवकमूल (mycorrhizal) कवक पौधे को मिट्टी से फ़ॉस्फ़ोरस सोखने में मदद करते हैं।",
   "हरे पौधों की तरह कवकों की कोशिका-भित्ति मुख्य रूप से सेलुलोज़ की बनी होती है।",
   "ट्राइकोडर्मा नामक कवक का उपयोग कई पादप रोगजनकों के विरुद्ध जैव-नियंत्रण कारक (biocontrol agent) के रूप में होता है।"],
  C3, 1,
  "Statements 1 and 3 are correct. In mycorrhiza, the fungus takes sugars from the root and in return passes on phosphorus and water from a wider volume of soil; some plants, such as pines, establish poorly without it, which is why mycorrhizae are sold as biofertilisers. Trichoderma, a free-living soil fungus, attacks the fungi that cause root diseases and is widely used in organic and integrated pest management. "
  "Statement 2 is wrong: fungal cell walls are made mainly of chitin, the same substance as the outer skeleton of insects. This is one reason fungi are placed in a kingdom of their own and are closer to animals than to plants.",
  "कथन 1 और 3 सही हैं। कवकमूल (mycorrhiza) में कवक जड़ से शर्करा लेता है और बदले में मिट्टी के बड़े दायरे से फ़ॉस्फ़ोरस और पानी पहुँचाता है; चीड़ जैसे कुछ पौधे इसके बिना ठीक से नहीं पनपते, इसीलिए कवकमूल जैव-उर्वरक के रूप में बेचे जाते हैं। मिट्टी में स्वतंत्र रूप से रहने वाला कवक ट्राइकोडर्मा जड़ों के रोग पैदा करने वाले कवकों पर हमला करता है और जैविक खेती तथा समेकित नाशीजीव प्रबंधन में खूब उपयोग होता है। "
  "कथन 2 गलत है: कवकों की कोशिका-भित्ति मुख्य रूप से काइटिन की बनी होती है, जो कीटों के बाहरी कंकाल का भी पदार्थ है। यह एक कारण है कि कवकों को अलग जगत में रखा गया है और वे पौधों की तुलना में जंतुओं के अधिक निकट हैं।",
  f"{MICRO12} (biofertilisers, biocontrol agents); NCERT Class XI, Biology -- Biological Classification (Kingdom Fungi).",
  "env-fungi-mycorrhiza-trichoderma")

S(F, "medium", "Consider the following statements about sacred groves in India:",
  "भारत के पवित्र उपवनों (sacred groves) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["They are patches of forest protected by local communities for religious and cultural reasons.",
   "They are known by local names such as 'devrai' in Maharashtra, 'kavu' in Kerala and 'oran' in Rajasthan.",
   "Under the Wildlife (Protection) Act, 1972, community or private land can be declared a 'community reserve' where the community volunteers to conserve it."],
  ["ये वन के वे टुकड़े हैं जिन्हें स्थानीय समुदाय धार्मिक और सांस्कृतिक कारणों से बचाकर रखते हैं।",
   "इन्हें स्थानीय नामों से जाना जाता है, जैसे महाराष्ट्र में 'देवराई', केरल में 'कावु' और राजस्थान में 'ओरण'।",
   "वन्यजीव (संरक्षण) अधिनियम, 1972 के तहत सामुदायिक या निजी भूमि को, जहाँ समुदाय स्वेच्छा से उसके संरक्षण के लिए आगे आए, 'सामुदायिक आरक्षित क्षेत्र' (community reserve) घोषित किया जा सकता है।"],
  C3, 2,
  "All three statements are correct. Sacred groves, dedicated to a local deity, have been left uncut for generations and often shelter plants lost from the surrounding landscape; they are found, among other places, in the Khasi and Jaintia Hills of Meghalaya, the Aravalli of Rajasthan and the Western Ghats. "
  "The 2002 amendment to the Wildlife (Protection) Act, in force from 2003, created two new categories of protected area -- conservation reserves and community reserves (section 36C) -- which give legal backing to such community conservation without taking away the people's rights.",
  "तीनों कथन सही हैं। किसी स्थानीय देवता को समर्पित पवित्र उपवन पीढ़ियों से नहीं काटे गए हैं, और इनमें प्रायः वे पौधे बचे रहते हैं जो आसपास के भू-दृश्य से लुप्त हो चुके हैं; ये मेघालय की खासी और जयंतिया पहाड़ियों, राजस्थान की अरावली और पश्चिमी घाट सहित कई स्थानों पर मिलते हैं। "
  "वन्यजीव (संरक्षण) अधिनियम के 2002 के संशोधन ने, जो 2003 से लागू हुआ, संरक्षित क्षेत्रों की दो नई श्रेणियाँ बनाईं: संरक्षण आरक्षित क्षेत्र और सामुदायिक आरक्षित क्षेत्र (धारा 36C); ये लोगों के अधिकार छीने बिना ऐसे सामुदायिक संरक्षण को कानूनी आधार देती हैं।",
  "NCERT Class XII, Biology -- Biodiversity and Conservation (sacred groves); Wildlife (Protection) Act, 1972, section 36C (inserted by the Amendment Act of 2002).",
  "env-sacred-groves")

S(F, "medium", "Consider the following statements about the tropical evergreen forests of India:",
  "भारत के उष्णकटिबंधीय सदाबहार वनों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["They grow in areas that receive more than about 200 cm of rain a year and have only a short dry season.",
   "All their trees shed their leaves together at one time of the year.",
   "Rosewood, mahogany and ebony are typical trees of the tropical deciduous forests."],
  ["ये उन क्षेत्रों में उगते हैं जहाँ वर्ष में लगभग 200 सेमी से अधिक वर्षा होती है और शुष्क ऋतु छोटी होती है।",
   "इनके सभी पेड़ वर्ष के एक ही समय पर एक साथ अपनी पत्तियाँ गिराते हैं।",
   "रोज़वुड, महोगनी और आबनूस उष्णकटिबंधीय पर्णपाती वनों के विशिष्ट पेड़ हैं।"],
  C3, 0,
  "Only statement 1 is correct: these forests occur on the western slopes of the Western Ghats, the hills of the north-east and the Andaman and Nicobar Islands, where rainfall is heavy and the temperature stays high. "
  "Statement 2 is wrong: because there is no marked dry season, there is no common leaf-fall; each tree sheds and renews its leaves at its own time, so the forest looks green all year -- which is what 'evergreen' means. "
  "Statement 3 is wrong: rosewood, mahogany and ebony (with rubber and cinchona) are trees of the evergreen forests. The deciduous forests are known for teak, sal, shisham, mahua and sandalwood.",
  "केवल कथन 1 सही है: ये वन पश्चिमी घाट के पश्चिमी ढलानों, पूर्वोत्तर की पहाड़ियों और अंडमान तथा निकोबार द्वीपसमूह में मिलते हैं, जहाँ भारी वर्षा होती है और तापमान ऊँचा रहता है। "
  "कथन 2 गलत है: स्पष्ट शुष्क ऋतु न होने के कारण पत्तियाँ गिरने का कोई साझा समय नहीं होता; हर पेड़ अपने समय पर पत्तियाँ गिराता और नई लाता है, इसलिए वन पूरे वर्ष हरा दिखता है, और 'सदाबहार' का यही अर्थ है। "
  "कथन 3 गलत है: रोज़वुड, महोगनी और आबनूस (रबर और सिनकोना के साथ) सदाबहार वनों के पेड़ हैं। पर्णपाती वन सागौन, साल, शीशम, महुआ और चंदन के लिए जाने जाते हैं।",
  f"{GEO11}; NCERT Class IX, Contemporary India I -- Natural Vegetation and Wildlife.",
  "env-tropical-evergreen-forests")

S(F, "medium", "Consider the following statements about the shola forests:",
  "शोला वनों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["They are stunted montane evergreen forests found in the sheltered valleys of the Nilgiri, Anamalai and Palani hills.",
   "The grasslands around them are kept from turning into forest partly by frost and fire.",
   "Wattle, pine and eucalyptus planted since colonial times have spread into these grasslands."],
  ["ये नीलगिरि, अन्नामलाई और पलनी पहाड़ियों की सुरक्षित घाटियों में मिलने वाले ठिगने पर्वतीय सदाबहार वन हैं।",
   "इनके आसपास के घास के मैदान कुछ हद तक पाले और आग के कारण वन में नहीं बदल पाते।",
   "औपनिवेशिक काल से लगाए गए वॉटल, चीड़ और यूकेलिप्टस इन घास के मैदानों में फैल गए हैं।"],
  C3, 2,
  "All three statements are correct. Above about 1,800 m in the southern Western Ghats, small patches of evergreen forest (sholas) grow in the folds and hollows, while the rolling hilltops carry grassland; together they form the shola-grassland mosaic that feeds many of south India's rivers. "
  "Frost on the open slopes kills tree seedlings, and fire keeps the grass going, so the boundary stays sharp. The grasslands were long treated as 'wasteland' and planted with exotic wattle, pine and eucalyptus, which have since spread on their own -- one of the main threats to the Nilgiri tahr's habitat.",
  "तीनों कथन सही हैं। दक्षिणी पश्चिमी घाट में लगभग 1,800 मीटर से ऊपर सदाबहार वन के छोटे टुकड़े (शोला) तहों और गड्ढों में उगते हैं, जबकि लहरदार पहाड़ी चोटियों पर घास के मैदान होते हैं; दोनों मिलकर शोला-घास मैदान का वह मोज़ेक बनाते हैं जिससे दक्षिण भारत की कई नदियों को पानी मिलता है। "
  "खुले ढलानों पर पड़ने वाला पाला पेड़ों के पौधों को मार देता है, और आग घास को बनाए रखती है, इसलिए दोनों की सीमा साफ़ बनी रहती है। इन घास के मैदानों को लंबे समय तक 'बंजर भूमि' मानकर उनमें विदेशी वॉटल, चीड़ और यूकेलिप्टस लगाए गए, जो तब से अपने-आप फैल गए हैं; यह नीलगिरि तहर के आवास के लिए प्रमुख खतरों में से एक है।",
  f"{GEO11} (montane forests: 'sholas'); Tamil Nadu Forest Department -- Shola grassland restoration in the Nilgiris.",
  "env-shola-grasslands")

S(F, "medium", "Consider the following statements about forest produce in India:",
  "भारत में वनोपज के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Lac is obtained from the resin of the palash tree.",
   "Kattha, eaten with paan, is obtained from the bark of the neem tree.",
   "Tendu leaves, used to roll bidis, come from the mahua tree."],
  ["लाख पलाश के पेड़ की राल (resin) से प्राप्त होती है।",
   "पान के साथ खाया जाने वाला कत्था नीम के पेड़ की छाल से प्राप्त होता है।",
   "बीड़ी लपेटने में उपयोग होने वाले तेंदू पत्ते महुआ के पेड़ से आते हैं।"],
  C3, 3,
  "None of the statements is correct. Lac is secreted by a tiny insect, Kerria lacca, which lives on host trees such as palash, kusum and ber; the palash is only the host, and Jharkhand is the largest producer. "
  "Kattha (catechu) is extracted from the heartwood of the khair tree (Acacia catechu), not from neem. Tendu leaves come from the tendu or kendu tree (Diospyros melanoxylon); the mahua is a different tree, valued for its edible flowers and oil-rich seeds. "
  "Each statement links a real product to a real, familiar tree -- the trap is the wrong pairing.",
  "कोई भी कथन सही नहीं है। लाख एक छोटे कीट, Kerria lacca, द्वारा स्रावित होती है, जो पलाश, कुसुम और बेर जैसे मेज़बान पेड़ों पर रहता है; पलाश केवल मेज़बान है, और झारखंड सबसे बड़ा उत्पादक है। "
  "कत्था नीम से नहीं, खैर के पेड़ (Acacia catechu) की अंतःकाष्ठ (heartwood) से निकाला जाता है। तेंदू पत्ते तेंदू या केंदू के पेड़ (Diospyros melanoxylon) से आते हैं; महुआ एक अलग पेड़ है, जो अपने खाने योग्य फूलों और तेल से भरे बीजों के लिए मूल्यवान है। "
  "हर कथन एक असली उत्पाद को एक असली, जाने-पहचाने पेड़ से जोड़ता है; जाल गलत जोड़ी में है।",
  "ICAR -- Indian Institute of Natural Resins and Gums, Ranchi (lac); Ministry of Tribal Affairs -- minor forest produce; NCERT Class VII, Science -- Forests: Our Lifeline.",
  "env-forest-produce-lac-kattha-tendu")

S(F, "medium", "Consider the following statements about the vegetation of the Himalaya:",
  "हिमालय की वनस्पति के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Deodar is a characteristic tree of the temperate forests of the western Himalaya.",
   "Chir pine forests typically occur above the zone of fir and spruce.",
   "Alpine meadows lie below the zone of coniferous forests."],
  ["देवदार पश्चिमी हिमालय के शीतोष्ण वनों का एक विशिष्ट पेड़ है।",
   "चीड़ के वन सामान्यतः फ़र और स्प्रूस के क्षेत्र से ऊपर मिलते हैं।",
   "अल्पाइन घास के मैदान शंकुधारी वनों के क्षेत्र से नीचे स्थित होते हैं।"],
  C3, 0,
  "Only statement 1 is correct: deodar forests grow at roughly 1,500 to 3,000 m in the western Himalaya, and deodar is Himachal Pradesh's State tree. "
  "Statements 2 and 3 invert the order of the zones. Vegetation changes with height much as it changes with latitude: tropical and subtropical forests with sal and chir pine in the foothills and lower slopes (chir at about 900 to 1,800 m), then oak, deodar and blue pine, then fir, spruce and birch near the tree line, and only above the tree line the alpine meadows ('bugyals' in Uttarakhand), used for summer grazing.",
  "केवल कथन 1 सही है: देवदार के वन पश्चिमी हिमालय में लगभग 1,500 से 3,000 मीटर पर उगते हैं, और देवदार हिमाचल प्रदेश का राज्य वृक्ष है। "
  "कथन 2 और 3 क्षेत्रों के क्रम को उलट देते हैं। ऊँचाई के साथ वनस्पति वैसे ही बदलती है जैसे अक्षांश के साथ: तलहटी और निचले ढलानों पर साल और चीड़ वाले उष्णकटिबंधीय और उपोष्ण वन (चीड़ लगभग 900 से 1,800 मीटर पर), फिर बांज (oak), देवदार और कैल (blue pine), फिर वृक्ष-रेखा के पास फ़र, स्प्रूस और भोजपत्र, और वृक्ष-रेखा के ऊपर ही अल्पाइन घास के मैदान (उत्तराखंड में 'बुग्याल'), जो गर्मियों में चराई के काम आते हैं।",
  f"{GEO11} (montane forests); Forest Survey of India -- forest types of India.",
  "env-himalayan-vegetation-zones")

# ---------------------------------------------------------------- easy statements (2)
S(F, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Bryophytes such as mosses are called the amphibians of the plant kingdom.",
   "Ferns reproduce by seeds."],
  ["मॉस जैसे ब्रायोफ़ाइट को पादप जगत के उभयचर कहा जाता है।",
   "फ़र्न बीजों से प्रजनन करते हैं।"],
  T2, 0,
  "Only statement 1 is correct. Bryophytes live on land but need water for fertilisation, as their sperm must swim to the egg -- hence 'amphibians of the plant kingdom'; with lichens they are among the first colonisers of bare rock. "
  "Statement 2 is wrong: ferns, like mosses, reproduce by spores, which form in small brown patches (sori) under their leaves. Seeds appear only in gymnosperms and flowering plants.",
  "केवल कथन 1 सही है। ब्रायोफ़ाइट भूमि पर रहते हैं, पर निषेचन के लिए उन्हें पानी चाहिए, क्योंकि उनके शुक्राणु तैरकर अंड तक पहुँचते हैं; इसीलिए इन्हें 'पादप जगत के उभयचर' कहते हैं; लाइकेन के साथ ये नंगी चट्टान पर सबसे पहले बसने वालों में हैं। "
  "कथन 2 गलत है: मॉस की तरह फ़र्न भी बीजाणुओं (spores) से प्रजनन करते हैं, जो उनकी पत्तियों के नीचे छोटे भूरे धब्बों (सोराई) में बनते हैं। बीज केवल अनावृतबीजी और पुष्पी पौधों में होते हैं।",
  f"{BIO11} (Bryophyta, Pteridophyta).",
  "env-bryophytes-ferns")

S(F, "easy", "Consider the following statements about pollination and seed dispersal:",
  "परागण और बीज-प्रकीर्णन के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Wind-pollinated flowers are usually small and dull and produce no nectar.",
   "The water hyacinth and the water lily are pollinated by water.",
   "The coconut is dispersed mainly by water."],
  ["पवन-परागित फूल सामान्यतः छोटे और फीके होते हैं और उनमें मकरंद नहीं होता।",
   "जलकुंभी और कुमुदिनी (water lily) का परागण पानी द्वारा होता है।",
   "नारियल का प्रकीर्णन मुख्य रूप से पानी द्वारा होता है।"],
  C3, 1,
  "Statements 1 and 3 are correct. Wind-pollinated flowers, as in grasses and maize, have no need to attract animals, so they lack bright petals, scent and nectar, and produce large amounts of light pollen. The coconut's fibrous husk lets it float for weeks, which is how it spread across tropical coasts. "
  "Statement 2 is the trap: living in water does not mean pollination by water. In most aquatic plants, including the water hyacinth and the water lily, the flowers rise above the surface and are pollinated by insects or wind; true water pollination is rare, seen in plants such as Vallisneria and Hydrilla.",
  "कथन 1 और 3 सही हैं। घास और मक्का जैसे पवन-परागित फूलों को जंतुओं को आकर्षित नहीं करना पड़ता, इसलिए उनमें चटकीली पंखुड़ियाँ, गंध और मकरंद नहीं होते, और वे बड़ी मात्रा में हल्के परागकण बनाते हैं। नारियल का रेशेदार छिलका उसे हफ़्तों तक तैरने देता है, और इसी तरह वह उष्णकटिबंधीय तटों पर फैला। "
  "कथन 2 जाल है: पानी में रहने का अर्थ पानी से परागण नहीं है। जलकुंभी और कुमुदिनी सहित अधिकांश जलीय पौधों में फूल सतह से ऊपर उठ आते हैं और कीटों या हवा से परागित होते हैं; वास्तविक जल-परागण दुर्लभ है, जो वैलिसनेरिया और हाइड्रिला जैसे पौधों में दिखता है।",
  "NCERT Class XII, Biology -- Sexual Reproduction in Flowering Plants (pollination); NCERT Class VII, Science -- Reproduction in Plants.",
  "env-pollination-dispersal")

# ---------------------------------------------------------------- hard statements (2)
S(F, "hard", "Consider the following statements about photosynthetic pathways in plants:",
  "पौधों में प्रकाश-संश्लेषण के मार्गों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Rice and wheat are C3 plants.",
   "Maize and sugarcane are C4 plants.",
   "In CAM plants such as the pineapple, the stomata open mainly at night.",
   "C4 plants lose more carbon to photorespiration than C3 plants do."],
  ["धान और गेहूँ C3 पौधे हैं।",
   "मक्का और गन्ना C4 पौधे हैं।",
   "अनानास जैसे CAM पौधों में रंध्र मुख्य रूप से रात में खुलते हैं।",
   "C4 पौधे प्रकाश-श्वसन (photorespiration) में C3 पौधों से अधिक कार्बन खोते हैं।"],
  C4, 2,
  "Statements 1, 2 and 3 are correct. Most crops, including rice and wheat, are C3 plants; maize, sugarcane, sorghum and many tropical grasses use the C4 pathway; and CAM plants such as the pineapple and cacti take in carbon dioxide at night, when it is cooler, which saves water. "
  "Statement 4 reverses the point of the C4 pathway: by concentrating carbon dioxide inside special bundle-sheath cells, C4 plants almost eliminate photorespiration, which is why they photosynthesise efficiently in heat and strong light. C3 plants lose much more to photorespiration, especially in hot, dry weather -- which matters for how rising temperatures will affect rice and wheat.",
  "कथन 1, 2 और 3 सही हैं। धान और गेहूँ सहित अधिकांश फ़सलें C3 पौधे हैं; मक्का, गन्ना, ज्वार और कई उष्णकटिबंधीय घासें C4 मार्ग का उपयोग करती हैं; और अनानास तथा कैक्टस जैसे CAM पौधे कार्बन डाइऑक्साइड रात में, जब ठंडक होती है, लेते हैं, जिससे पानी बचता है। "
  "कथन 4 C4 मार्ग के मूल उद्देश्य को ही उलट देता है: विशेष पूलाच्छद (bundle-sheath) कोशिकाओं में कार्बन डाइऑक्साइड को सांद्रित करके C4 पौधे प्रकाश-श्वसन को लगभग समाप्त कर देते हैं, इसीलिए वे गर्मी और तेज़ रोशनी में कुशलता से प्रकाश-संश्लेषण करते हैं। C3 पौधे, विशेषकर गर्म और शुष्क मौसम में, प्रकाश-श्वसन में कहीं अधिक खोते हैं; यह बात इसके लिए महत्त्वपूर्ण है कि बढ़ता तापमान धान और गेहूँ को कैसे प्रभावित करेगा।",
  "NCERT Class XI, Biology -- Photosynthesis in Higher Plants (C3 and C4 pathways, photorespiration).",
  "env-c3-c4-cam-plants")

S(F, "hard", "Consider the following statements about fire in forests:",
  "वनों में आग के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The resin-rich fallen needles of the chir pine make its forests highly prone to fire.",
   "In some plants, the heat of a fire helps release or germinate their seeds.",
   "In most of India, forest fires peak in the dry months before the monsoon."],
  ["चीड़ की गिरी हुई, राल से भरी पत्तियाँ (सुइयाँ) इसके वनों को आग के प्रति अत्यधिक संवेदनशील बनाती हैं।",
   "कुछ पौधों में आग की गर्मी उनके बीजों को मुक्त करने या अंकुरित करने में मदद करती है।",
   "भारत के अधिकांश भागों में वनाग्नि मानसून से पहले के शुष्क महीनों में चरम पर होती है।"],
  C3, 2,
  "All three statements are correct. The thick layer of dry chir pine needles on the forest floor burns easily, and fires in the chir forests of Uttarakhand and Himachal Pradesh are an annual problem. "
  "Some plants are adapted to fire: in certain pines and eucalypts the cones or capsules open only after being heated (serotiny), and the seeds of others germinate better after a fire. "
  "In India the fire season runs roughly from November to June and peaks in March to May, when the forests are dry; the Forest Survey of India issues near-real-time fire alerts from satellite data.",
  "तीनों कथन सही हैं। वन की ज़मीन पर चीड़ की सूखी पत्तियों की मोटी परत आसानी से जलती है, और उत्तराखंड तथा हिमाचल प्रदेश के चीड़ वनों में आग हर वर्ष की समस्या है। "
  "कुछ पौधे आग के प्रति अनुकूलित हैं: कुछ चीड़ और यूकेलिप्टस में शंकु या फल-संपुट गर्म होने के बाद ही खुलते हैं (serotiny), और कुछ दूसरे पौधों के बीज आग के बाद बेहतर अंकुरित होते हैं। "
  "भारत में आग का मौसम लगभग नवंबर से जून तक रहता है और मार्च से मई में चरम पर होता है, जब वन सूखे होते हैं; भारतीय वन सर्वेक्षण उपग्रह आँकड़ों से लगभग तुरंत आग की चेतावनी जारी करता है।",
  "Forest Survey of India -- Forest Fire Alert System and India State of Forest Report (forest fire chapter); Uttarakhand Forest Department -- chir pine and forest fires.",
  "env-forest-fire-ecology")

# ---------------------------------------------------------------- MCQs (3)
M(F, "easy", "Brahma kamal, a flower of the high Himalaya, is the State flower of:",
  "ऊँचे हिमालय का फूल ब्रह्म कमल किस राज्य का राज्य पुष्प है?",
  ["Uttarakhand", "Himachal Pradesh", "Sikkim", "Arunachal Pradesh"],
  ["उत्तराखंड", "हिमाचल प्रदेश", "सिक्किम", "अरुणाचल प्रदेश"],
  0,
  "Brahma kamal (Saussurea obvallata), which grows in the alpine zone at about 3,000 to 4,800 m and blooms in the monsoon, is the State flower of Uttarakhand, where it is offered at shrines such as Kedarnath and Badrinath. Despite its name it is not a lotus but a member of the sunflower family. "
  "Himachal Pradesh's State flower is the pink rhododendron, Sikkim's the noble dendrobium orchid and Arunachal Pradesh's the foxtail orchid.",
  "ब्रह्म कमल (Saussurea obvallata), जो लगभग 3,000 से 4,800 मीटर पर अल्पाइन क्षेत्र में उगता है और मानसून में खिलता है, उत्तराखंड का राज्य पुष्प है, जहाँ इसे केदारनाथ और बद्रीनाथ जैसे मंदिरों में चढ़ाया जाता है। नाम के बावजूद यह कमल नहीं, सूरजमुखी कुल का सदस्य है। "
  "हिमाचल प्रदेश का राज्य पुष्प गुलाबी बुरांस (pink rhododendron), सिक्किम का नोबल डेंड्रोबियम ऑर्किड और अरुणाचल प्रदेश का फ़ॉक्सटेल ऑर्किड है।",
  "Uttarakhand Forest Department -- State symbols; Botanical Survey of India -- Saussurea obvallata.",
  "env-brahma-kamal")

M(F, "medium", "Which one of the following is NOT a fungus?",
  "निम्नलिखित में से कौन-सा एक कवक (fungus) नहीं है?",
  ["Spirulina", "Yeast", "Penicillium", "Truffle"],
  ["स्पाइरुलिना", "यीस्ट (खमीर)", "पेनिसिलियम", "ट्रफ़ल"],
  0,
  "Spirulina, sold as a protein-rich food supplement, is a cyanobacterium (blue-green 'alga'), a photosynthesising prokaryote -- neither a fungus nor a true alga. "
  "Yeast, used in baking and brewing, is a single-celled fungus; Penicillium is the mould from which Alexander Fleming discovered penicillin; and the truffle is the underground fruiting body of a fungus that lives in mycorrhizal partnership with tree roots.",
  "प्रोटीन से भरपूर आहार-पूरक के रूप में बिकने वाला स्पाइरुलिना एक सायनोबैक्टीरियम (नील-हरित 'शैवाल') है, यानी प्रकाश-संश्लेषण करने वाला प्रोकैरियोट; यह न कवक है, न वास्तविक शैवाल। "
  "बेकरी और किण्वन में उपयोग होने वाला यीस्ट एककोशिकीय कवक है; पेनिसिलियम वह फफूँद है जिससे एलेक्ज़ेंडर फ़्लेमिंग ने पेनिसिलिन की खोज की; और ट्रफ़ल एक कवक का भूमिगत फलनकाय है, जो पेड़ों की जड़ों के साथ कवकमूल साझेदारी में रहता है।",
  f"{MICRO12} (single cell protein, antibiotics); NCERT Class XI, Biology -- Biological Classification.",
  "env-not-a-fungus-spirulina")

M(F, "hard", "Which one of the following plants produces the largest single flower in the world?",
  "निम्नलिखित में से कौन-सा पौधा विश्व का सबसे बड़ा एकल फूल पैदा करता है?",
  ["Rafflesia arnoldii", "Titan arum (Amorphophallus titanum)", "Giant water lily (Victoria amazonica)", "Talipot palm (Corypha umbraculifera)"],
  ["रैफ़्लेसिया आर्नोल्डी", "टाइटन एरम (Amorphophallus titanum)", "विशाल जल-कुमुदिनी (Victoria amazonica)", "तालीपॉट ताड़ (Corypha umbraculifera)"],
  0,
  "Rafflesia arnoldii of the rainforests of Sumatra and Borneo bears a single flower that can be about a metre across and weigh several kilograms. It is a parasite on Tetrastigma vines, with no leaves, stem or roots of its own, and it smells of rotting meat to attract carrion flies. "
  "The traps rest on the difference between a flower and an inflorescence: the titan arum holds the record for the largest unbranched inflorescence -- a spike bearing many small flowers -- and the talipot palm, found in India and Sri Lanka, for the largest branched inflorescence, after which the palm dies. The giant water lily is famous for its huge floating leaves.",
  "सुमात्रा और बोर्नियो के वर्षावनों का रैफ़्लेसिया आर्नोल्डी एक ऐसा एकल फूल देता है जो लगभग एक मीटर चौड़ा और कई किलोग्राम भारी हो सकता है। यह Tetrastigma लताओं पर परजीवी है, इसकी अपनी पत्तियाँ, तना या जड़ें नहीं होतीं, और यह सड़े मांस जैसी गंध से मृतजीवी मक्खियों को आकर्षित करता है। "
  "जाल फूल और पुष्पक्रम (inflorescence) के अंतर पर टिके हैं: टाइटन एरम के पास सबसे बड़े अशाखित पुष्पक्रम का रिकॉर्ड है, यानी कई छोटे फूलों वाली एक बाली, और भारत तथा श्रीलंका में मिलने वाले तालीपॉट ताड़ के पास सबसे बड़े शाखित पुष्पक्रम का, जिसके बाद ताड़ मर जाता है। विशाल जल-कुमुदिनी अपनी विशाल तैरती पत्तियों के लिए प्रसिद्ध है।",
  "Royal Botanic Gardens, Kew -- Rafflesia arnoldii, Amorphophallus titanum; NCERT Class XI, Biology -- Morphology of Flowering Plants (inflorescence).",
  "env-largest-flower-rafflesia")

# ---------------------------------------------------------------- Statement-I/II (medium) and I/II/III (hard)
A(F, "medium",
  "Most trees of India's tropical deciduous forests shed their leaves in the dry season.",
  "भारत के उष्णकटिबंधीय पर्णपाती वनों के अधिकांश पेड़ शुष्क ऋतु में अपनी पत्तियाँ गिरा देते हैं।",
  "Teak is the dominant tree in many of India's tropical deciduous forests.",
  "भारत के कई उष्णकटिबंधीय पर्णपाती वनों में सागौन प्रमुख पेड़ है।",
  1,
  "Both statements are correct, but Statement-II does not explain Statement-I. The trees of these monsoon forests shed their leaves for some weeks in the dry season because, with little water in the soil, keeping leaves would mean losing more water through transpiration than the roots can replace. "
  "That teak dominates many such forests is a separate fact about their composition (sal dominates others); it says nothing about why the trees drop their leaves.",
  "दोनों कथन सही हैं, पर कथन-II कथन-I की व्याख्या नहीं करता। इन मानसूनी वनों के पेड़ शुष्क ऋतु में कुछ सप्ताह के लिए पत्तियाँ गिरा देते हैं, क्योंकि मिट्टी में पानी कम होने पर पत्तियाँ रखने का अर्थ होगा वाष्पोत्सर्जन से उतना पानी खोना जितना जड़ें पूरा नहीं कर सकतीं। "
  "कई ऐसे वनों में सागौन का प्रभुत्व उनकी संरचना के बारे में एक अलग तथ्य है (कुछ दूसरे वनों में साल प्रमुख है); इससे यह पता नहीं चलता कि पेड़ पत्तियाँ क्यों गिराते हैं।",
  f"{GEO11} (tropical deciduous forests); NCERT Class IX, Contemporary India I -- Natural Vegetation and Wildlife.",
  "env-deciduous-leaf-fall-teak")

A(F, "hard",
  "The Himalayan yew (Taxus wallichiana) is listed as Endangered on the IUCN Red List.",
  "हिमालयी यू (थुनेर, Taxus wallichiana) IUCN रेड लिस्ट में संकटग्रस्त (Endangered) श्रेणी में है।",
  "Its bark and leaves have been heavily harvested for taxol (paclitaxel), a drug used in treating cancer.",
  "कैंसर के उपचार में उपयोग होने वाली दवा टैक्सॉल (पैक्लिटैक्सेल) के लिए इसकी छाल और पत्तियों का भारी दोहन हुआ है।",
  0,
  "Both Statement II and Statement III are correct, and both explain Statement I. After taxol was found in yew bark, the Himalayan yew was stripped on a large scale from the 1990s for the drug industry, as well as for fuelwood and traditional medicine. "
  "Because it grows slowly and regenerates poorly in the wild, the populations could not recover from that harvest; the combination of heavy exploitation and slow replacement is what pushed the species to Endangered. Trade in it is regulated under CITES Appendix II.",
  "कथन-II और कथन-III दोनों सही हैं, और दोनों कथन-I की व्याख्या करते हैं। यू की छाल में टैक्सॉल मिलने के बाद 1990 के दशक से दवा उद्योग के लिए, साथ ही ईंधन और पारंपरिक औषधि के लिए, हिमालयी यू का बड़े पैमाने पर दोहन हुआ। "
  "धीरे बढ़ने और जंगल में कमज़ोर पुनर्जनन के कारण इसकी आबादियाँ उस दोहन से उबर नहीं सकीं; भारी दोहन और धीमी भरपाई का यही मेल इस प्रजाति को संकटग्रस्त श्रेणी तक ले गया। इसका व्यापार CITES परिशिष्ट II के तहत नियंत्रित है।",
  f"{IUCN}: Taxus wallichiana; CITES Appendix II (Taxus wallichiana).",
  "env-himalayan-yew-taxol",
  s3="It grows slowly and regenerates poorly in the wild.",
  s3_hi="यह धीरे बढ़ता है और जंगल में इसका पुनर्जनन कमज़ोर होता है।")

# ---------------------------------------------------------------- pairs (1, medium)
P(F, "medium", "Consider the following pairs of plants and the medicinal compounds obtained from them:",
  "पौधों और उनसे प्राप्त होने वाले औषधीय यौगिकों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Sarpagandha (Rauvolfia serpentina) : Reserpine", "Neem : Nicotine", "Sweet wormwood (Artemisia annua) : Artemisinin", "Foxglove (Digitalis) : Quinine"],
  ["सर्पगंधा (Rauvolfia serpentina) : रेसर्पीन", "नीम : निकोटीन", "आर्टेमिसिया (sweet wormwood, Artemisia annua) : आर्टेमिसिनिन", "फ़ॉक्सग्लोव (Digitalis) : कुनैन (quinine)"],
  1,
  "Only pairs 1 and 3 are correct. Reserpine from sarpagandha root was one of the first modern drugs for high blood pressure; artemisinin from sweet wormwood is the basis of today's front-line malaria treatment, and its discovery won Tu Youyou the 2015 Nobel Prize. "
  "Pair 2 is wrong: neem's main active compound is azadirachtin, used as a natural insecticide; nicotine comes from tobacco. Pair 4 is wrong: foxglove gives digitalis glycosides such as digoxin, used for heart failure; quinine comes from the bark of the cinchona tree.",
  "केवल युग्म 1 और 3 सही हैं। सर्पगंधा की जड़ से मिलने वाला रेसर्पीन उच्च रक्तचाप की पहली आधुनिक दवाओं में था; आर्टेमिसिया से मिलने वाला आर्टेमिसिनिन आज के प्रमुख मलेरिया उपचार का आधार है, और इसकी खोज के लिए तू यूयू को 2015 का नोबेल पुरस्कार मिला। "
  "युग्म 2 गलत है: नीम का मुख्य सक्रिय यौगिक एज़ाडिरेक्टिन है, जो प्राकृतिक कीटनाशक के रूप में उपयोग होता है; निकोटीन तंबाकू से आता है। युग्म 4 गलत है: फ़ॉक्सग्लोव से डिजॉक्सिन जैसे डिजिटेलिस ग्लाइकोसाइड मिलते हैं, जो हृदय-विफलता में उपयोग होते हैं; कुनैन सिनकोना पेड़ की छाल से आती है।",
  "National Medicinal Plants Board -- Rauvolfia serpentina; Nobel Prize in Physiology or Medicine 2015 (Tu Youyou, artemisinin); WHO Guidelines for Malaria.",
  "env-medicinal-plants-pairs")

if __name__ == "__main__":
    write("env_l2_t9_flora.sql")
