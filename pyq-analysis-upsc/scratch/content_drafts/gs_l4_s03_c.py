# -*- coding: utf-8 -*-
"""Level 4 · Simulator 3 (GS Paper I full mock, Layout C: the 2026 shape) -- part C: Environment (9)
(upsc_l4_gs_cell_targets.mjs 3).
Every tested proposition was swept against the whole UPSC bank and no row tests it: AOSIS and the negotiating blocs;
the Meghalayan Age and Mawmluh Cave; character displacement; the bearded vulture; the sociable lapwing and the
spoon-billed sandpiper; Arisaema; the Ballast Water, Bamako, Barcelona and Nairobi Conventions; red mud, phosphogypsum
and acid mine drainage; Neora Valley, Singalila, Papikonda and Bhagwan Mahavir. MCQ keys are pinned (pos)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, write
from ca_common import combo
from bilingual import combo_hi

d.SUBJECT = "Environment & Ecology"
d.REQUIRE_CRAFT = True

def SC(topic, diff, body, body_hi, st, st_hi, truth, pos, expl, expl_hi, cite, cg, craft):
    opts = combo(truth, pos)
    S(topic, diff, body, body_hi, st, st_hi, None, pos, expl, expl_hi, cite, cg, opts=opts, opts_hi=[combo_hi(o) for o in opts], craft=craft)

# ---------------------------------------------------------------- Climate Agreements & Carbon Markets (MCQ, medium)
M("Climate Agreements & Carbon Markets", "medium",
  "In the UN climate negotiations, which grouping has pressed hardest for the 1.5 degree limit, because its members face rising seas?",
  "संयुक्त राष्ट्र जलवायु वार्ताओं में किस समूह ने 1.5 डिग्री की सीमा के लिए सबसे अधिक ज़ोर दिया है, क्योंकि उसके सदस्यों को बढ़ते समुद्र का सामना है?",
  ["Alliance of Small Island States",
   "Like-Minded Developing Countries",
   "The BASIC countries",
   "The Umbrella Group of developed countries"],
  ["लघु द्वीपीय राज्यों का गठबंधन",
   "समान विचार वाले विकासशील देश",
   "बेसिक देश",
   "विकसित देशों का अंब्रेला समूह"],
  0,
  "The Alliance of Small Island States (AOSIS), formed in 1990, speaks for low-lying coastal and island countries, for which sea-level rise and storms are a threat to survival; it pushed to have the 1.5 degree goal written into the Paris Agreement and has led the demand for finance for loss and damage. Blocs matter because the UNFCCC works by consensus. "
  "The Like-Minded Developing Countries, which include India and China, stress the differentiated responsibilities of rich and poor countries; the BASIC group (Brazil, South Africa, India and China) coordinates the large emerging economies; and the Umbrella Group is a loose coalition of developed countries outside the European Union, such as Japan, Australia and Canada.",
  "1990 में बना लघु द्वीपीय राज्यों का गठबंधन (एओएसआईएस) निचले तटीय और द्वीपीय देशों की आवाज़ है, जिनके लिए समुद्र-स्तर वृद्धि और तूफ़ान अस्तित्व का संकट हैं; इसने पेरिस समझौते में 1.5 डिग्री का लक्ष्य लिखवाने का प्रयास किया और हानि और क्षति के लिए वित्त की माँग का नेतृत्व किया। समूह इसलिए महत्त्वपूर्ण हैं क्योंकि यूएनएफ़सीसीसी आम सहमति से चलता है। "
  "भारत और चीन सहित समान विचार वाले विकासशील देश धनी और निर्धन देशों के विभेदित उत्तरदायित्वों पर बल देते हैं; बेसिक समूह (ब्राज़ील, दक्षिण अफ़्रीका, भारत और चीन) बड़ी उभरती अर्थव्यवस्थाओं का समन्वय करता है; और अंब्रेला समूह जापान, ऑस्ट्रेलिया और कनाडा जैसे यूरोपीय संघ से बाहर के विकसित देशों का ढीला गठजोड़ है।",
  "UNFCCC, Party groupings; Paris Agreement (2015), Article 2.",
  "l4-s03-env-aosis-lmdc-basic-umbrella-blocs", pos=2, craft="recall")

# ---------------------------------------------------------------- Climate Science & Mitigation (statement, medium)
SC("Climate Science & Mitigation", "medium", "With reference to the Meghalayan Age in the geological time scale, consider the following statements:",
   "भूवैज्ञानिक समय-मापक्रम में मेघालयी युग के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
   ["It began about 42,000 years ago.",
    "It takes its name from a stalagmite in Mawmluh Cave in Meghalaya, which records a severe drought.",
    "Oxygen isotopes in such cave deposits help to reconstruct past rainfall."],
   ["यह लगभग 42,000 वर्ष पहले आरंभ हुआ।",
    "इसका नाम मेघालय की मावमलुह गुफा के एक निक्षेप-स्तंभ (स्टैलेग्माइट) से है, जो एक भीषण सूखे को दर्ज करता है।",
    "ऐसे गुफा निक्षेपों में ऑक्सीजन समस्थानिक पिछली वर्षा का पुनर्निर्माण करने में सहायक होते हैं।"],
   (0, 1, 1), 1,
   "Only statements 2 and 3 are correct. In 2018 the International Commission on Stratigraphy divided the Holocene into three ages: the Greenlandian, the Northgrippian and the Meghalayan, the last of them beginning about 4,250 years ago. Its reference point is a stalagmite from Mawmluh Cave near Cherrapunji, whose layers record an abrupt mega-drought that was felt across the world and has been linked with the troubles of early civilisations in Egypt, Mesopotamia and the Indus valley. "
   "Statement 1 is wrong: 42,000 years ago lies far back in the last ice age, before the Holocene began. Cave deposits (speleothems) grow layer by layer from dripping water, and the ratio of oxygen isotopes in those layers reflects the strength of the rains, so they serve as natural archives of the past monsoon, alongside ice cores and tree rings.",
   "केवल कथन 2 और 3 सही हैं। 2018 में अंतरराष्ट्रीय स्तरिकी आयोग ने होलोसीन को तीन युगों में बाँटा: ग्रीनलैंडियन, नॉर्थग्रिपियन और मेघालयी, जिनमें अंतिम लगभग 4,250 वर्ष पहले आरंभ हुआ। इसका संदर्भ बिंदु चेरापूंजी के निकट मावमलुह गुफा का एक निक्षेप-स्तंभ है, जिसकी परतें एक अचानक महासूखे को दर्ज करती हैं जो विश्वभर में अनुभव हुआ और जिसे मिस्र, मेसोपोटामिया और सिंधु घाटी की आरंभिक सभ्यताओं की कठिनाइयों से जोड़ा गया है। "
   "कथन 1 ग़लत है: 42,000 वर्ष पहले का समय होलोसीन के आरंभ से बहुत पहले, पिछले हिमयुग में पड़ता है। गुफा निक्षेप (स्पेलियोथेम) टपकते जल से परत-दर-परत बढ़ते हैं, और उन परतों में ऑक्सीजन समस्थानिकों का अनुपात वर्षा की प्रबलता को दर्शाता है, इसलिए वे हिम क्रोडों और वृक्ष वलयों के साथ पिछले मानसून के प्राकृतिक अभिलेखागार हैं।",
   "International Commission on Stratigraphy, International Chronostratigraphic Chart (2018); Geological Survey of India; Indian Institute of Tropical Meteorology.",
   "l4-s03-env-meghalayan-age-mawmluh-speleothem", "linkage")

# ---------------------------------------------------------------- Ecosystems & Ecological Processes (MCQ, hard)
M("Ecosystems & Ecological Processes", "hard",
  "Where two similar species of finch live on the same island, their beaks often differ more than where each lives alone, which reduces competition for food. This is an example of",
  "जहाँ एक ही द्वीप पर फ़िंच की दो समान प्रजातियाँ रहती हैं, वहाँ उनकी चोंचें प्रायः अकेले रहने की स्थिति से अधिक भिन्न होती हैं, जिससे भोजन के लिए प्रतिस्पर्धा घटती है। यह किसका उदाहरण है?",
  ["character displacement",
   "the competitive exclusion principle",
   "convergent evolution in unrelated species",
   "Batesian mimicry of a distasteful species"],
  ["लक्षण विस्थापन",
   "प्रतिस्पर्धी अपवर्जन का सिद्धांत",
   "असंबंधित प्रजातियों में अभिसारी विकास",
   "अरुचिकर प्रजाति की बेट्सियन अनुकृति"],
  0,
  "Character displacement occurs when natural selection pushes two competing species apart in some trait where their ranges overlap: each specialises on a different food or habitat, so they compete less. The classic evidence comes from the ground finches of the Galapagos, whose beak sizes differ more on islands they share, as Peter and Rosemary Grant showed by measuring changes over decades. "
  "The competitive exclusion principle says instead that two species using exactly the same limiting resource cannot coexist for long, one of them driving out the other; character displacement is one way of escaping that outcome. Convergent evolution makes unrelated species look alike, and Batesian mimicry is the imitation of a harmful species by a harmless one -- neither reduces competition between close relatives.",
  "लक्षण विस्थापन तब होता है जब प्राकृतिक चयन दो प्रतिस्पर्धी प्रजातियों को, जहाँ उनके क्षेत्र मिलते हैं, किसी लक्षण में एक-दूसरे से दूर कर देता है: दोनों अलग भोजन या आवास में विशेषज्ञ हो जाती हैं, इसलिए कम प्रतिस्पर्धा करती हैं। इसका शास्त्रीय प्रमाण गैलापागोस के भू-फ़िंचों से मिलता है, जिनके चोंच के आकार साझा द्वीपों पर अधिक भिन्न होते हैं, जैसा पीटर और रोज़मेरी ग्रांट ने दशकों तक बदलाव मापकर दिखाया। "
  "प्रतिस्पर्धी अपवर्जन का सिद्धांत इसके बजाय कहता है कि ठीक एक ही सीमित संसाधन का उपयोग करने वाली दो प्रजातियाँ लंबे समय तक साथ नहीं रह सकतीं, और एक दूसरी को बाहर कर देती है; लक्षण विस्थापन उस परिणाम से बचने का एक तरीक़ा है। अभिसारी विकास असंबंधित प्रजातियों को एक जैसा बनाता है, और बेट्सियन अनुकृति किसी हानिरहित प्रजाति द्वारा हानिकारक प्रजाति की नक़ल है -- दोनों में से कोई निकट संबंधियों के बीच प्रतिस्पर्धा नहीं घटाता।",
  "NCERT, Class XII, Biology, chapter on organisms and populations; Peter and Rosemary Grant's long-term studies of Galapagos finches.",
  "l4-s03-env-character-displacement-finch-beaks", pos=3, craft="application")

# ---------------------------------------------------------------- Fauna & Animal Behaviour (statement, easy)
SC("Fauna & Animal Behaviour", "easy", "With reference to the bearded vulture (lammergeier), consider the following statements:",
   "दाढ़ी वाले गिद्ध (लैमरगेयर) के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
   ["It feeds largely on bones, dropping the bigger ones from a height to break them.",
    "It lives in high mountains, including the Himalaya.",
    "It nests in the mangrove forests of the Sundarbans."],
   ["यह मुख्यतः हड्डियाँ खाता है, और बड़ी हड्डियों को तोड़ने के लिए ऊँचाई से गिराता है।",
    "यह हिमालय सहित ऊँचे पर्वतों पर रहता है।",
    "यह सुंदरबन के मैंग्रोव वनों में घोंसला बनाता है।"],
   (1, 1, 0), 0,
   "Only statements 1 and 2 are correct. The bearded vulture is one of the few animals whose diet is mostly bone and marrow; its very strong stomach acid dissolves bones, and it carries large ones up and drops them on rocks to split them. It soars over high mountains and cliffs from the Himalaya and Central Asia to the Pyrenees and East Africa. "
   "Statement 3 is wrong: it needs high crags for nesting, not coastal mangroves. Unlike the Gyps vultures of the Indian plains, which crashed after feeding on carcasses of cattle treated with diclofenac, it feeds little on fresh flesh, though it too is declining in much of its range.",
   "केवल कथन 1 और 2 सही हैं। दाढ़ी वाला गिद्ध उन कुछ प्राणियों में है जिनके भोजन में अधिकतर हड्डी और मज्जा होती है; इसका बहुत प्रबल आमाशय अम्ल हड्डियाँ घोल देता है, और यह बड़ी हड्डियों को ऊपर ले जाकर चट्टानों पर गिराता है ताकि वे टूट जाएँ। यह हिमालय और मध्य एशिया से पिरेनीज़ और पूर्वी अफ़्रीका तक ऊँचे पर्वतों और चट्टानों के ऊपर उड़ता है। "
   "कथन 3 ग़लत है: इसे घोंसले के लिए ऊँची चट्टानें चाहिए, तटीय मैंग्रोव नहीं। भारतीय मैदानों के जिप्स गिद्धों के विपरीत, जिनकी संख्या डाइक्लोफ़ेनाक से उपचारित पशुओं के शव खाने के बाद तेज़ी से गिरी, यह ताज़ा मांस कम खाता है, यद्यपि अपने क्षेत्र के बड़े भाग में यह भी घट रहा है।",
   "IUCN Red List assessment for Gypaetus barbatus; Bombay Natural History Society.",
   "l4-s03-env-bearded-vulture-bones-himalaya", "recall")

# ---------------------------------------------------------------- Fauna & Animal Behaviour (statement, medium)
SC("Fauna & Animal Behaviour", "medium", "With reference to the sociable lapwing and the spoon-billed sandpiper, consider the following statements:",
   "सोशिएबल लैपविंग और स्पून-बिल्ड सैंडपाइपर के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
   ["The sociable lapwing breeds on the steppes of Kazakhstan and winters partly in north-western India.",
    "The spoon-billed sandpiper breeds in the Western Ghats.",
    "The spoon-billed sandpiper winters on the coasts of South and Southeast Asia.",
    "Both birds are assessed as Critically Endangered."],
   ["सोशिएबल लैपविंग कज़ाख़स्तान के स्टेपी में प्रजनन करती है और आंशिक रूप से उत्तर-पश्चिमी भारत में शीतकाल बिताती है।",
    "स्पून-बिल्ड सैंडपाइपर पश्चिमी घाट में प्रजनन करता है।",
    "स्पून-बिल्ड सैंडपाइपर दक्षिण और दक्षिण-पूर्व एशिया के तटों पर शीतकाल बिताता है।",
    "दोनों पक्षी गंभीर रूप से संकटग्रस्त आँके गए हैं।"],
   (1, 0, 1, 1), 1,
   "Statements 1, 3 and 4 are correct. The sociable lapwing nests on the Central Asian steppes, above all in Kazakhstan, and migrates to wintering grounds that include north-western India, Pakistan and north-east Africa; it depends on dry grasslands and fallow fields there, which makes grassland protection and hunting along the route important. The spoon-billed sandpiper, with its unique spatula-shaped bill, winters on the mudflats of Bangladesh, Myanmar and Southeast Asia, with rare records from India. "
   "Statement 2 is wrong: it breeds only on the coastal tundra of the Russian Far East, in Chukotka and Kamchatka. The loss of intertidal mudflats along the East Asian flyway has left only a few hundred pairs, and it is among the rarest waders; both species are listed as Critically Endangered.",
   "केवल कथन 1, 3 और 4 सही हैं। सोशिएबल लैपविंग मध्य एशियाई स्टेपी, सबसे बढ़कर कज़ाख़स्तान, में घोंसला बनाती है और उन शीतकालीन स्थलों की ओर प्रवास करती है जिनमें उत्तर-पश्चिमी भारत, पाकिस्तान और उत्तर-पूर्वी अफ़्रीका शामिल हैं; वहाँ वह सूखे घास के मैदानों और परती खेतों पर निर्भर है, जिससे मार्ग पर घास के मैदानों की रक्षा और शिकार का प्रश्न महत्त्वपूर्ण हो जाता है। अपनी अनूठी चपटी चोंच वाला स्पून-बिल्ड सैंडपाइपर बांग्लादेश, म्यांमार और दक्षिण-पूर्व एशिया के कीचड़ वाले तटों पर शीतकाल बिताता है, और भारत से इसके दुर्लभ अभिलेख हैं। "
   "कथन 2 ग़लत है: यह केवल रूस के सुदूर पूर्व में, चुकोटका और कामचटका के तटीय टुंड्रा पर प्रजनन करता है। पूर्वी एशियाई उड़ान-मार्ग पर ज्वारीय कीचड़-क्षेत्रों के नष्ट होने से इसके केवल कुछ सौ जोड़े बचे हैं, और यह सबसे दुर्लभ जल-पक्षियों में है; दोनों प्रजातियाँ गंभीर रूप से संकटग्रस्त सूचीबद्ध हैं।",
   "IUCN Red List assessments for Vanellus gregarius and Calidris pygmaea; Convention on Migratory Species; Bombay Natural History Society.",
   "l4-s03-env-sociable-lapwing-spoon-billed-sandpiper", "precision")

# ---------------------------------------------------------------- Flora, Fungi & Forests (statement, medium)
SC("Flora, Fungi & Forests", "medium", "With reference to the cobra lilies (Arisaema) of India, consider the following statements:",
   "भारत की कोबरा लिली (एरिसीमा) के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
   ["Their hooded spathe resembles the raised hood of a cobra.",
    "They grow mainly in the deserts of western Rajasthan.",
    "In many species an individual plant can change sex, with the larger plants bearing female flowers."],
   ["उनका फणधारी स्पेथ कोबरा के उठे हुए फन जैसा दिखता है।",
    "वे मुख्यतः पश्चिमी राजस्थान के मरुस्थलों में उगती हैं।",
    "अनेक प्रजातियों में एक ही पौधा लिंग बदल सकता है, और बड़े पौधों पर मादा फूल आते हैं।"],
   (1, 0, 1), 2,
   "Only statements 1 and 3 are correct. Arisaema is named for its striking spathe, a leaf-like hood around a central spike, often curved over like a cobra's raised head; the flowers are hidden inside and pollinated by small flies trapped in the hood. Many species are unusual in that an individual's sex depends on its size: small plants with little stored food produce male flowers, and only large plants, which can afford to make seeds, produce female ones, so a plant may change sex from year to year. "
   "Statement 2 is wrong: they grow on the moist forest floor, from the Himalaya and the north-east to the Western Ghats. Some are at risk from collection for trade and from loss of their shaded forest habitat.",
   "केवल कथन 1 और 3 सही हैं। एरिसीमा अपने आकर्षक स्पेथ से पहचानी जाती है, जो एक मध्य शूकी के चारों ओर पत्ती जैसा फन होता है और प्रायः कोबरा के उठे सिर की तरह मुड़ा रहता है; फूल भीतर छिपे होते हैं और फन में फँसी छोटी मक्खियों से परागित होते हैं। अनेक प्रजातियाँ इस बात में असामान्य हैं कि किसी पौधे का लिंग उसके आकार पर निर्भर होता है: कम संचित भोजन वाले छोटे पौधे नर फूल देते हैं, और केवल बड़े पौधे, जो बीज बनाने में समर्थ हैं, मादा फूल देते हैं, इसलिए कोई पौधा वर्ष-दर-वर्ष लिंग बदल सकता है। "
   "कथन 2 ग़लत है: वे हिमालय और पूर्वोत्तर से पश्चिमी घाट तक नम वन-भूमि पर उगती हैं। कुछ प्रजातियाँ व्यापार के लिए संग्रह और अपने छायादार वन-आवास के नष्ट होने से संकट में हैं।",
   "Botanical Survey of India, Flora of India; peer-reviewed studies on sex change in Arisaema.",
   "l4-s03-env-arisaema-cobra-lily-sex-change", "precision")

# ---------------------------------------------------------------- International Conventions & Organisations (statement, hard)
SC("International Conventions & Organisations", "hard", "Consider the following statements about international environmental conventions:",
   "अंतरराष्ट्रीय पर्यावरण अभिसमयों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
   ["The Ballast Water Management Convention was adopted under the UN Environment Programme.",
    "The Bamako Convention bans the import of hazardous waste into Africa.",
    "The Barcelona Convention protects the marine environment of the Mediterranean.",
    "The Nairobi Convention covers the Western Indian Ocean."],
   ["बैलास्ट जल प्रबंधन अभिसमय संयुक्त राष्ट्र पर्यावरण कार्यक्रम के अंतर्गत अंगीकृत हुआ।",
    "बामाको अभिसमय अफ़्रीका में ख़तरनाक कचरे के आयात पर रोक लगाता है।",
    "बार्सिलोना अभिसमय भूमध्य सागर के समुद्री पर्यावरण की रक्षा करता है।",
    "नैरोबी अभिसमय पश्चिमी हिंद महासागर को समाहित करता है।"],
   (0, 1, 1, 1), 3,
   "Statements 2, 3 and 4 are correct. The Bamako Convention (1991), negotiated by African states through the then Organisation of African Unity, goes beyond the Basel Convention by banning hazardous waste imports into Africa altogether. The Barcelona Convention (1976) and the Nairobi Convention (1985) belong to UNEP's Regional Seas Programme, which brings neighbouring countries together to protect shared seas; the Nairobi Convention covers East African coastal and island states. "
   "Statement 1 is wrong: the Ballast Water Management Convention was adopted in 2004 by the International Maritime Organization and came into force in 2017. It requires ships to manage the water they take on as ballast, which has spread invasive species around the world, such as the comb jelly that devastated fisheries in the Black Sea.",
   "केवल कथन 2, 3 और 4 सही हैं। अफ़्रीकी राज्यों द्वारा तत्कालीन अफ़्रीकी एकता संगठन के माध्यम से तय बामाको अभिसमय (1991) बासेल अभिसमय से आगे जाकर अफ़्रीका में ख़तरनाक कचरे के आयात पर पूरी रोक लगाता है। बार्सिलोना अभिसमय (1976) और नैरोबी अभिसमय (1985) यूएनईपी के क्षेत्रीय समुद्र कार्यक्रम के अंग हैं, जो साझा समुद्रों की रक्षा के लिए पड़ोसी देशों को एक साथ लाता है; नैरोबी अभिसमय पूर्वी अफ़्रीका के तटीय और द्वीपीय राज्यों को समाहित करता है। "
   "कथन 1 ग़लत है: बैलास्ट जल प्रबंधन अभिसमय 2004 में अंतरराष्ट्रीय समुद्री संगठन द्वारा अंगीकृत हुआ और 2017 में प्रवृत्त हुआ। यह जहाज़ों से संतुलन के लिए लिए गए जल का प्रबंधन करने की अपेक्षा करता है, जिसने विश्वभर में आक्रामक प्रजातियाँ फैलाई हैं, जैसे वह कोंब जेली जिसने काला सागर की मत्स्य-संपदा को तबाह किया।",
   "Bamako Convention (1991); UNEP Regional Seas Programme (Barcelona and Nairobi Conventions); International Maritime Organization, Ballast Water Management Convention (2004).",
   "l4-s03-env-ballast-bamako-barcelona-nairobi", "precision")

# ---------------------------------------------------------------- Pollution, Waste & Resources (statement, medium)
SC("Pollution, Waste & Resources", "medium", "With reference to industrial and mining wastes, consider the following statements:",
   "औद्योगिक और खनन अपशिष्टों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
   ["Red mud is the waste left when alumina is refined from bauxite.",
    "Phosphogypsum is a by-product of making phosphoric acid for fertilisers.",
    "Acid mine drainage forms when sulphide minerals exposed by mining react with air and water."],
   ["रेड मड बॉक्साइट से ऐलुमिना के शोधन के बाद बचा अपशिष्ट है।",
    "फ़ॉस्फ़ोजिप्सम उर्वरकों के लिए फ़ॉस्फ़ोरिक अम्ल बनाने का उपोत्पाद है।",
    "अम्लीय खान अपवाह तब बनता है जब खनन से उजागर सल्फ़ाइड खनिज हवा और जल से अभिक्रिया करते हैं।"],
   (1, 1, 1), 2,
   "All three statements are correct. Refining bauxite by the Bayer process leaves behind about one to one and a half tonnes of caustic red mud for each tonne of alumina, stored in large ponds that can fail, as at Ajka in Hungary in 2010; efforts are on to use it in cement and bricks and to recover metals from it. Phosphogypsum, produced in large stacks by the fertiliser industry, contains traces of radioactive elements and fluorides, and India's rules govern its safe use in cement, roads and soil. "
   "Acid mine drainage arises when pyrite and other sulphides form sulphuric acid, which dissolves heavy metals and can kill rivers; the unregulated rat-hole coal mining of Meghalaya's Jaintia Hills turned streams there acidic, one reason for the National Green Tribunal's ban in 2014.",
   "तीनों कथन सही हैं। बेयर प्रक्रिया से बॉक्साइट का शोधन प्रति टन ऐलुमिना पर लगभग एक से डेढ़ टन क्षारीय रेड मड छोड़ता है, जो बड़े तालाबों में रखा जाता है जो टूट सकते हैं, जैसे 2010 में हंगरी के अजका में हुआ; इसे सीमेंट और ईंटों में उपयोग करने और इससे धातुएँ निकालने के प्रयास चल रहे हैं। उर्वरक उद्योग से बड़े ढेरों में बनने वाले फ़ॉस्फ़ोजिप्सम में रेडियोधर्मी तत्वों और फ़्लोराइड के अंश होते हैं, और भारत के नियम सीमेंट, सड़कों और मिट्टी में इसके सुरक्षित उपयोग को नियंत्रित करते हैं। "
   "अम्लीय खान अपवाह तब उत्पन्न होता है जब पाइराइट और अन्य सल्फ़ाइड सल्फ़्यूरिक अम्ल बनाते हैं, जो भारी धातुओं को घोलता है और नदियों को मार सकता है; मेघालय की जयंती पहाड़ियों में अनियमित रैट-होल कोयला खनन ने वहाँ की धाराओं को अम्लीय बना दिया, जो 2014 में राष्ट्रीय हरित अधिकरण की रोक का एक कारण था।",
   "Ministry of Mines and National Institute of Secondary Steel Technology reports on red mud; Central Pollution Control Board, guidelines on phosphogypsum; National Green Tribunal, orders on rat-hole mining in Meghalaya (2014).",
   "l4-s03-env-red-mud-phosphogypsum-acid-mine-drainage", "precision")

# ---------------------------------------------------------------- Protected Areas & Wildlife Protection (statement, medium)
SC("Protected Areas & Wildlife Protection", "medium", "With reference to some protected areas of India, consider the following statements:",
   "भारत के कुछ संरक्षित क्षेत्रों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
   ["Neora Valley National Park, in West Bengal, is a habitat of the red panda.",
    "Singalila National Park lies along the border with Bhutan.",
    "Papikonda National Park lies along the Godavari in Andhra Pradesh.",
    "The Bhagwan Mahavir Sanctuary, which includes the Dudhsagar falls, is in Goa."],
   ["पश्चिम बंगाल में नेओरा वैली राष्ट्रीय उद्यान लाल पांडा का आवास है।",
    "सिंगालीला राष्ट्रीय उद्यान भूटान की सीमा के साथ स्थित है।",
    "पापिकोंडा राष्ट्रीय उद्यान आंध्र प्रदेश में गोदावरी के किनारे स्थित है।",
    "दूधसागर जलप्रपात को समेटने वाला भगवान महावीर अभयारण्य गोवा में है।"],
   (1, 0, 1, 1), 0,
   "Statements 1, 3 and 4 are correct. Neora Valley, in the Kalimpong hills, is one of the richest forests of the eastern Himalaya, with red pandas in its bamboo and rhododendron belts. Papikonda protects the forests along the Godavari where the river cuts through the Eastern Ghats in a scenic gorge, and part of it is affected by the Polavaram project. The Bhagwan Mahavir Sanctuary and the adjoining Mollem National Park, on the Goa-Karnataka border, include the Dudhsagar falls on the Mandovi. "
   "Statement 2 is wrong: Singalila, in Darjeeling district, lies along the ridge on the border with Nepal, with Sandakphu, the highest peak of West Bengal, on it. It too is known for red pandas, and for the Singalila ridge trek.",
   "केवल कथन 1, 3 और 4 सही हैं। कलिम्पोंग की पहाड़ियों में नेओरा वैली पूर्वी हिमालय के सबसे समृद्ध वनों में से है, जिसके बाँस और बुरांश क्षेत्रों में लाल पांडा हैं। पापिकोंडा उन वनों की रक्षा करता है जहाँ गोदावरी एक सुंदर गॉर्ज में पूर्वी घाट को काटती है, और इसका एक भाग पोलावरम परियोजना से प्रभावित है। गोवा-कर्नाटक सीमा पर भगवान महावीर अभयारण्य और उससे सटे मोलेम राष्ट्रीय उद्यान में मांडवी पर दूधसागर जलप्रपात है। "
   "कथन 2 ग़लत है: दार्जिलिंग ज़िले में सिंगालीला नेपाल की सीमा पर कटक के साथ स्थित है, जिस पर पश्चिम बंगाल की सबसे ऊँची चोटी संदकफू है। यह भी लाल पांडा और सिंगालीला कटक की ट्रेकिंग के लिए जाना जाता है।",
   "West Bengal Forest Department; Andhra Pradesh Forest Department; Goa Forest Department; Ministry of Environment, Forest and Climate Change, National Wildlife Database.",
   "l4-s03-env-neora-singalila-papikonda-bhagwan-mahavir", "precision")

write("gs_l4_s03_c.sql")
