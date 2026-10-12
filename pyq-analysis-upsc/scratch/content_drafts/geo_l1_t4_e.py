# -*- coding: utf-8 -*-
"""Level 1 · Test 4 (Geography, NCERT Foundation) -- part E: Transport, Ports & Human Geography (7) and
Resources: Minerals, Energy & Agriculture (7) (upsc_l1_cell_targets.mjs 4).
Transport/human: easy MCQ 1, easy statement 1, easy pairs 1, medium MCQ 1, medium statement 2, medium Statement-I/II 1.
Resources: easy MCQ 1, easy statement 1, easy Statement-I/II 1, medium MCQ 1, medium statement 2, medium Statement-I/II 1.
The angle is NCERT Fundamentals of Human Geography and India: People and Economy (population, settlements, human
development, sea routes, functional towns) and Contemporary India II and Resource and Development (resource
classes, soil conservation, modes of mineral occurrence, crop seasons). Level-2 facts are not repeated: Census
figures, migration streams, demographic transition, HDI basics, settlement types, ports, railways, roads, pipelines,
waterways, the European rivers; mineral belts, crops' climates and producers, revolutions, energy projects, and the
age pyramids of Level-2 Environment. MCQ keys are pinned (pos)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, T2

d.SUBJECT = "Geography"
d.REQUIRE_CRAFT = True
TH = "Transport, Ports & Human Geography"
RS = "Resources: Minerals, Energy & Agriculture"
FHG = "NCERT Class XII, Geography -- Fundamentals of Human Geography"
IPR = "NCERT Class XII, Geography -- India: People and Economy"
CI2 = "NCERT Class X, Geography -- Contemporary India II"
RD8 = "NCERT Class VIII, Geography -- Resource and Development"

# ================================================================ TRANSPORT & HUMAN (7)
# ---------------------------------------------------------------- easy MCQ (1)
M(TH, "easy", "For the Census of India, a 'literate' is a person who can read and write with understanding in any language, and who is aged",
  "भारत की जनगणना के लिए 'साक्षर' वह व्यक्ति है जो किसी भी भाषा को समझ के साथ पढ़-लिख सकता है, और जिसकी आयु है",
  ["7 years or above", "5 years or above", "6 years or above", "10 years or above"],
  ["7 वर्ष या अधिक", "5 वर्ष या अधिक", "6 वर्ष या अधिक", "10 वर्ष या अधिक"],
  0,
  "The Census counts as literate a person aged seven years and above who can both read and write with understanding in any language; children below seven are treated as non-literate whatever they can read. "
  "This is why the literacy rate is worked out on the population aged seven and above, not on the whole population.",
  "जनगणना सात वर्ष और अधिक आयु के उस व्यक्ति को साक्षर गिनती है जो किसी भी भाषा को समझ के साथ पढ़ और लिख दोनों सके; सात वर्ष से कम आयु के बच्चे, वे जो भी पढ़ सकें, निरक्षर माने जाते हैं। "
  "इसीलिए साक्षरता दर पूरी जनसंख्या पर नहीं, सात वर्ष और अधिक आयु की जनसंख्या पर निकाली जाती है।",
  f"{IPR} (Population: Distribution, Density, Growth and Composition).",
  "l1-geo-census-literate-seven-years", pos=3, craft="recall")

# ---------------------------------------------------------------- easy statement (1)
S(TH, "easy", "Consider the following statements about the distribution of the world's population:",
  "विश्व की जनसंख्या के वितरण के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["About 90 per cent of the world's population lives in about 10 per cent of its land area.",
   "Population density is the ratio between the number of people and the size of the land, usually given as persons per sq km."],
  ["विश्व की लगभग 90 प्रतिशत जनसंख्या उसके लगभग 10 प्रतिशत भू-क्षेत्र में रहती है।",
   "जनसंख्या घनत्व लोगों की संख्या और भूमि के आकार का अनुपात है, जिसे सामान्यतः व्यक्ति प्रति वर्ग किमी में बताया जाता है।"],
  T2, 2,
  "Both statements are correct. People are very unevenly spread: they crowd into plains with fertile soil, fresh water, moderate climates and jobs, while mountains, deserts and polar lands remain thinly settled. "
  "The ten most populous countries together hold about 60 per cent of the world's people, and six of them are in Asia.",
  "दोनों कथन सही हैं। लोग बहुत असमान रूप से फैले हैं: वे उपजाऊ मिट्टी, मीठे पानी, सम जलवायु और रोज़गार वाले मैदानों में सघन रूप से बसते हैं, जबकि पर्वत, मरुस्थल और ध्रुवीय भूमियाँ विरल रूप से बसी रहती हैं। "
  "दस सबसे अधिक जनसंख्या वाले देशों में मिलाकर विश्व के लगभग 60 प्रतिशत लोग रहते हैं, और उनमें से छह एशिया में हैं।",
  f"{FHG} (The World Population).",
  "l1-geo-world-population-90-10-density", craft="recall")

# ---------------------------------------------------------------- easy pairs (1)
P(TH, "easy", "Consider the following pairs of Indian towns and the functions for which they are best known:",
  "भारतीय नगरों और उन कार्यों के निम्नलिखित युग्मों पर विचार कीजिए जिनके लिए वे सबसे अधिक जाने जाते हैं:",
  ["Jamshedpur : industrial town",
   "Mhow : garrison (cantonment) town",
   "Digboi : religious town",
   "Roorkee : educational town"],
  ["जमशेदपुर : औद्योगिक नगर",
   "महू : छावनी (cantonment) नगर",
   "डिगबोई : धार्मिक नगर",
   "रुड़की : शैक्षिक नगर"],
  2,
  "Pairs 1, 2 and 4 are correctly matched. Towns are classified by their dominant function: Jamshedpur grew around its steel works, Mhow is a military cantonment, and Roorkee is known for its engineering institution, now an IIT. "
  "Pair 3 is wrong: Digboi in Assam, with Raniganj, Jharia and Ankaleshwar, is a mining town -- the site of India's oldest oil field; Varanasi, Mathura, Amritsar, Madurai and Puri are examples of religious and cultural towns.",
  "युग्म 1, 2 और 4 सही सुमेलित हैं। नगरों का वर्गीकरण उनके प्रमुख कार्य के आधार पर होता है: जमशेदपुर अपने इस्पात कारख़ाने के चारों ओर बढ़ा, महू सैनिक छावनी है, और रुड़की अपने इंजीनियरिंग संस्थान, अब IIT, के लिए जाना जाता है। "
  "युग्म 3 गलत है: असम का डिगबोई, रानीगंज, झरिया और अंकलेश्वर की तरह, खनन नगर है -- भारत के सबसे पुराने तेल क्षेत्र का स्थान; वाराणसी, मथुरा, अमृतसर, मदुरै और पुरी धार्मिक और सांस्कृतिक नगरों के उदाहरण हैं।",
  f"{IPR} (Human Settlements).",
  "l1-geo-functional-towns-pairs", craft="precision")

# ---------------------------------------------------------------- medium MCQ (1)
M(TH, "medium", "The North Atlantic sea route, the busiest in the world and called the 'Big Trunk Route', links",
  "विश्व का सबसे व्यस्त, 'बिग ट्रंक रूट' कहलाने वाला उत्तरी अटलांटिक समुद्री मार्ग किन्हें जोड़ता है?",
  ["north-eastern USA with north-western Europe", "Western Europe with East Asia through the Suez Canal",
   "the west coast of the Americas with East Asia", "Western Europe with South Africa round the Cape"],
  ["उत्तर-पूर्वी अमेरिका को उत्तर-पश्चिमी यूरोप से", "स्वेज़ नहर के रास्ते पश्चिमी यूरोप को पूर्वी एशिया से",
   "दोनों अमेरिकाओं के पश्चिमी तट को पूर्वी एशिया से", "उत्तमाशा अंतरीप के रास्ते पश्चिमी यूरोप को दक्षिण अफ़्रीका से"],
  0,
  "The North Atlantic route joins the two most industrialised regions of the world, north-eastern USA and north-western Europe; about a quarter of the world's foreign trade moves on it, and both coasts have advanced ports and harbour facilities. "
  "The Mediterranean-Indian Ocean route through the Suez Canal links Western Europe with Asia and serves more countries and people than any other route, while the Cape of Good Hope route is used mainly when the canal cannot be.",
  "उत्तरी अटलांटिक मार्ग विश्व के दो सबसे औद्योगीकृत क्षेत्रों, उत्तर-पूर्वी अमेरिका और उत्तर-पश्चिमी यूरोप, को जोड़ता है; विश्व का लगभग एक-चौथाई विदेशी व्यापार इस पर चलता है, और दोनों तटों पर उन्नत पत्तन और पोताश्रय सुविधाएँ हैं। "
  "स्वेज़ नहर से होकर जाने वाला भूमध्यसागर-हिंद महासागर मार्ग पश्चिमी यूरोप को एशिया से जोड़ता है और किसी भी अन्य मार्ग से अधिक देशों और लोगों की सेवा करता है, जबकि उत्तमाशा अंतरीप मार्ग मुख्यतः तब प्रयुक्त होता है जब नहर का उपयोग संभव न हो।",
  f"{FHG} (Transport and Communication).",
  "l1-geo-north-atlantic-big-trunk-route", pos=3, craft="recall")

# ---------------------------------------------------------------- medium statement (2)
S(TH, "medium", "Consider the following statements about the shapes of rural settlements:",
  "ग्रामीण बस्तियों के आकारों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Linear settlements develop with houses strung along a road, railway line, river, canal or levee.",
   "Star-like settlements develop where several roads converge on a place, with houses built along each road.",
   "A 'double village' develops at a tri-junction of roads."],
  ["रैखिक बस्तियाँ किसी सड़क, रेलमार्ग, नदी, नहर या तटबंध के साथ बने मकानों की कतार के रूप में विकसित होती हैं।",
   "तारे जैसी बस्तियाँ वहाँ विकसित होती हैं जहाँ कई सड़कें एक स्थान पर मिलती हैं, और हर सड़क के साथ मकान बनते हैं।",
   "'दोहरा गाँव' (double village) सड़कों के तिराहे पर विकसित होता है।"],
  C3, 1,
  "Statements 1 and 2 are correct: the shape of a village follows the lines along which it can grow, such as routes, rivers and the edges of valleys. "
  "Statement 3 is wrong: a T-shaped settlement develops at a tri-junction of roads; a double village extends on both sides of a river where there is a bridge or a ferry. Circular villages grow around lakes and tanks, and cross-shaped ones at crossroads.",
  "कथन 1 और 2 सही हैं: गाँव का आकार उन रेखाओं का अनुसरण करता है जिनके साथ वह बढ़ सकता है, जैसे मार्ग, नदियाँ और घाटियों के किनारे। "
  "कथन 3 गलत है: सड़कों के तिराहे पर T-आकार की बस्ती विकसित होती है; दोहरा गाँव नदी के दोनों ओर वहाँ फैलता है जहाँ पुल या नौका-घाट हो। वृत्ताकार गाँव झीलों और तालाबों के चारों ओर, और क्रॉस-आकार के गाँव चौराहों पर बसते हैं।",
  f"{FHG} (Human Settlements).",
  "l1-geo-settlement-shapes-linear-star-double", craft="precision")

S(TH, "medium", "Consider the following statements about the four pillars of human development:",
  "मानव विकास के चार स्तंभों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Equity means making access to opportunities equally available to everybody, irrespective of gender, race, income or caste.",
   "Sustainability means that each generation must have the same opportunities, so that the availability of opportunities continues.",
   "Productivity, as a pillar of human development, refers mainly to raising the output of machines and land."],
  ["समता (equity) का अर्थ है लिंग, नस्ल, आय या जाति का भेद किए बिना सभी को अवसरों तक समान पहुँच उपलब्ध कराना।",
   "सतत पोषणीयता (sustainability) का अर्थ है कि हर पीढ़ी को समान अवसर मिलें, ताकि अवसरों की उपलब्धता बनी रहे।",
   "मानव विकास के स्तंभ के रूप में उत्पादकता का अर्थ मुख्यतः मशीनों और भूमि का उत्पादन बढ़ाना है।"],
  C3, 1,
  "Statements 1 and 2 are correct: all environmental, financial and human resources must be used keeping the future in mind, or future generations will have fewer choices. "
  "Statement 3 is wrong: productivity here means human labour productivity, which must be constantly enriched by building people's capabilities through better health and education. The fourth pillar, empowerment, is the power to make choices, which comes from increasing freedom and capability.",
  "कथन 1 और 2 सही हैं: सभी पर्यावरणीय, वित्तीय और मानव संसाधनों का उपयोग भविष्य को ध्यान में रखकर होना चाहिए, नहीं तो आने वाली पीढ़ियों के पास कम विकल्प होंगे। "
  "कथन 3 गलत है: यहाँ उत्पादकता का अर्थ मानव श्रम की उत्पादकता है, जिसे बेहतर स्वास्थ्य और शिक्षा द्वारा लोगों की क्षमताएँ बढ़ाकर लगातार समृद्ध करना होता है। चौथा स्तंभ, सशक्तीकरण, विकल्प चुनने की शक्ति है, जो बढ़ती स्वतंत्रता और क्षमता से आती है।",
  f"{FHG} (Human Development).",
  "l1-geo-human-development-four-pillars", craft="precision")

# ---------------------------------------------------------------- medium Statement-I/II (1)
A(TH, "medium",
  "The world's population took far longer to reach its first billion than to grow from five billion to six billion.",
  "विश्व की जनसंख्या को पहले एक अरब तक पहुँचने में, पाँच अरब से छह अरब होने की तुलना में, कहीं अधिक समय लगा।",
  "Since the Industrial Revolution, better food supply, medicine and sanitation have sharply cut death rates, while birth rates stayed high for a long time.",
  "औद्योगिक क्रांति के बाद से बेहतर खाद्य आपूर्ति, चिकित्सा और स्वच्छता ने मृत्यु दर को तेज़ी से घटाया, जबकि जन्म दर लंबे समय तक ऊँची बनी रही।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I. It took more than a million years for humanity to reach one billion, but only about 12 years to go from five billion to six; the growth is explained by the widening gap between births and deaths once death rates fell. "
  "This is why the time taken for the population to double has shrunk so dramatically over the last few centuries.",
  "दोनों कथन सही हैं, और कथन-II कथन-I की व्याख्या करता है। मानव जाति को एक अरब तक पहुँचने में दस लाख से अधिक वर्ष लगे, पर पाँच अरब से छह अरब होने में केवल लगभग 12 वर्ष; मृत्यु दर घटने के बाद जन्म और मृत्यु के बीच बढ़ता अंतर इस वृद्धि की व्याख्या करता है। "
  "इसीलिए पिछली कुछ शताब्दियों में जनसंख्या के दोगुना होने का समय इतना अधिक घट गया है।",
  f"{FHG} (The World Population).",
  "l1-geo-population-billions-death-rates", craft="inference")

# ================================================================ RESOURCES (7)
# ---------------------------------------------------------------- easy MCQ (1)
M(RS, "easy", "The rearing of silkworms for the production of silk fibre is called",
  "रेशम के रेशे के उत्पादन के लिए रेशम के कीड़ों का पालन क्या कहलाता है?",
  ["sericulture", "apiculture", "pisciculture", "viticulture"],
  ["रेशम कीट पालन (sericulture)", "मधुमक्खी पालन (apiculture)", "मत्स्य पालन (pisciculture)", "अंगूर की खेती (viticulture)"],
  0,
  "Sericulture is the rearing of silkworms, which feed on mulberry and other leaves, for silk. "
  "Apiculture is bee-keeping for honey and wax, pisciculture is the breeding of fish in specially built tanks and ponds, and viticulture is the cultivation of grapes; growing vegetables, flowers and fruit for sale is horticulture.",
  "सेरीकल्चर रेशम के लिए रेशम के कीड़ों का पालन है, जो शहतूत और अन्य पत्तियाँ खाते हैं। "
  "एपीकल्चर शहद और मोम के लिए मधुमक्खी पालन है, पिसीकल्चर विशेष रूप से बनाए गए टैंकों और तालाबों में मछली पालन है, और विटीकल्चर अंगूर की खेती है; बिक्री के लिए सब्ज़ियाँ, फूल और फल उगाना उद्यान-कृषि (horticulture) है।",
  f"{RD8} (Agriculture).",
  "l1-geo-sericulture-terms", pos=2, craft="recall")

# ---------------------------------------------------------------- easy statement (1)
S(RS, "easy", "Consider the following statements about coal mining in Meghalaya:",
  "मेघालय में कोयला खनन के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Coal at Jowai and Cherrapunji has been mined by family members through long, narrow tunnels, known as 'rat-hole' mining.",
   "The National Green Tribunal has endorsed rat-hole mining as a safe, low-impact method."],
  ["जोवाई और चेरापूंजी में परिवार के सदस्य लंबी, सँकरी सुरंगों द्वारा कोयला निकालते रहे हैं, जिसे 'रैट-होल' खनन कहते हैं।",
   "राष्ट्रीय हरित अधिकरण (NGT) ने रैट-होल खनन को सुरक्षित और कम प्रभाव वाली विधि के रूप में समर्थन दिया है।"],
  T2, 0,
  "Only statement 1 is correct. In the North-East, minerals are owned by individuals or communities, and Meghalaya has large deposits of coal, iron ore, limestone and dolomite; the narrow, unsupported pits are dangerous for the miners and pollute streams with acid drainage. "
  "Statement 2 is wrong: the National Green Tribunal declared such mining illegal and recommended that it be stopped forthwith.",
  "केवल कथन 1 सही है। पूर्वोत्तर में खनिज व्यक्तियों या समुदायों के स्वामित्व में हैं, और मेघालय में कोयले, लौह अयस्क, चूना पत्थर और डोलोमाइट के बड़े भंडार हैं; बिना सहारे वाले सँकरे गड्ढे खनिकों के लिए ख़तरनाक हैं और अम्लीय निकासी से नालों को प्रदूषित करते हैं। "
  "कथन 2 गलत है: राष्ट्रीय हरित अधिकरण ने ऐसे खनन को अवैध घोषित किया और इसे तुरंत रोकने की सिफ़ारिश की।",
  f"{CI2} (Minerals and Energy Resources).",
  "l1-geo-rat-hole-mining-meghalaya", craft="precision")

# ---------------------------------------------------------------- easy Statement-I/II (1)
A(RS, "easy",
  "Shelter belts have helped stabilise sand dunes in western India.",
  "आश्रय पट्टियों (shelter belts) ने पश्चिमी भारत में रेत के टीलों को स्थिर करने में सहायता की है।",
  "Rows of trees planted as shelter belts break the force of the wind.",
  "आश्रय पट्टियों के रूप में लगाई गई पेड़ों की कतारें पवन की शक्ति को तोड़ती हैं।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I: by slowing the wind near the ground, the lines of trees stop it from lifting and shifting sand, which has helped stabilise the desert in western India. "
  "Other methods of soil conservation suit other landscapes: contour ploughing and terracing on slopes, and strip cropping, in which strips of grass are left to grow between crops to break the wind.",
  "दोनों कथन सही हैं, और कथन-II कथन-I की व्याख्या करता है: भूमि के निकट पवन को धीमा करके पेड़ों की कतारें उसे रेत उठाने और खिसकाने से रोकती हैं, जिससे पश्चिमी भारत में मरुस्थल को स्थिर करने में सहायता मिली है। "
  "मृदा संरक्षण की अन्य विधियाँ अन्य भू-दृश्यों के अनुकूल हैं: ढलानों पर समोच्च जुताई और सीढ़ीदार खेत, और पट्टीदार कृषि, जिसमें पवन को तोड़ने के लिए फ़सलों के बीच घास की पट्टियाँ उगने दी जाती हैं।",
  f"{CI2} (Resources and Development).",
  "l1-geo-shelter-belts-sand-dunes", craft="inference")

# ---------------------------------------------------------------- medium MCQ (1)
M(RS, "medium", "Gold, silver, tin and platinum often occur in the sands of valley floors and at the base of hills, deposited by streams. Such deposits are called",
  "सोना, चाँदी, टिन और प्लैटिनम प्रायः घाटियों के तल की रेत में और पहाड़ियों के आधार पर, धाराओं द्वारा जमा, मिलते हैं। ऐसे निक्षेप क्या कहलाते हैं?",
  ["placer deposits", "veins and lodes", "residual deposits", "sedimentary beds"],
  ["प्लेसर निक्षेप", "शिराएँ और लोड", "अवशिष्ट निक्षेप", "अवसादी संस्तर"],
  0,
  "Placer deposits are alluvial deposits that generally contain minerals which are not corroded by water, which is why heavy, stable metals such as gold, silver, tin and platinum collect in them. "
  "In igneous and metamorphic rocks, minerals fill cracks and faults as veins (small) and lodes (large); in sedimentary rocks they lie in beds or layers, like coal and gypsum; and the decomposition of surface rocks, leaving the soluble parts to be washed away, leaves residual ores such as bauxite.",
  "प्लेसर निक्षेप जलोढ़ निक्षेप हैं जिनमें सामान्यतः वे खनिज होते हैं जिन्हें जल संक्षारित नहीं करता, इसीलिए सोना, चाँदी, टिन और प्लैटिनम जैसी भारी, स्थिर धातुएँ उनमें जमा होती हैं। "
  "आग्नेय और कायांतरित शैलों में खनिज दरारों और भ्रंशों को शिराओं (छोटी) और लोड (बड़ी) के रूप में भरते हैं; अवसादी शैलों में वे कोयले और जिप्सम की तरह संस्तरों या परतों में मिलते हैं; और सतही शैलों के अपघटन से, घुलनशील भाग बह जाने पर, बॉक्साइट जैसे अवशिष्ट अयस्क बचते हैं।",
  f"{CI2} (Minerals and Energy Resources).",
  "l1-geo-placer-deposits-mineral-modes", pos=3, craft="precision")

# ---------------------------------------------------------------- medium statement (2)
S(RS, "medium", "Consider the following statements about crop seasons in India:",
  "भारत में फ़सल ऋतुओं के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Sesamum (til) is a kharif crop in the north and a rabi crop in the south.",
   "Castor seed is grown both as a rabi and as a kharif crop.",
   "Maize is grown only in the kharif season, everywhere in India."],
  ["तिल उत्तर में खरीफ़ फ़सल और दक्षिण में रबी फ़सल है।",
   "अरंडी के बीज रबी और खरीफ़ दोनों फ़सलों के रूप में उगाए जाते हैं।",
   "मक्का पूरे भारत में केवल खरीफ़ ऋतु में उगाया जाता है।"],
  C3, 1,
  "Statements 1 and 2 are correct: the same crop can belong to different seasons in different regions, depending on temperature and the timing of the rain. "
  "Statement 3 is wrong: maize, which needs temperatures of about 21-27 degrees Celsius and grows well in old alluvial soil, is mainly a kharif crop, but in some States, such as Bihar, it is grown in the rabi season also.",
  "कथन 1 और 2 सही हैं: तापमान और वर्षा के समय के अनुसार एक ही फ़सल अलग-अलग क्षेत्रों में अलग-अलग ऋतुओं की हो सकती है। "
  "कथन 3 गलत है: लगभग 21-27 डिग्री सेल्सियस तापमान चाहने वाला और पुरानी जलोढ़ मिट्टी में अच्छी तरह उगने वाला मक्का मुख्यतः खरीफ़ फ़सल है, पर बिहार जैसे कुछ राज्यों में यह रबी ऋतु में भी उगाया जाता है।",
  f"{CI2} (Agriculture).",
  "l1-geo-sesamum-castor-maize-seasons", craft="precision")

S(RS, "medium", "Consider the following statements about the classification of resources:",
  "संसाधनों के वर्गीकरण के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The hydrogen in water, which could be a rich source of energy but which we lack the technology to use for this purpose, is an example of 'stock'.",
   "'Reserves' are resources that cannot be used with existing technical know-how.",
   "Village commons such as grazing grounds, burial grounds and village ponds are 'national' resources."],
  ["जल में मौजूद हाइड्रोजन, जो ऊर्जा का समृद्ध स्रोत हो सकती है पर जिसका इस काम में उपयोग करने की तकनीक हमारे पास नहीं है, 'भंडार' (stock) का उदाहरण है।",
   "'संचित कोष' (reserves) वे संसाधन हैं जिनका मौजूदा तकनीकी ज्ञान से उपयोग नहीं किया जा सकता।",
   "चरागाह, श्मशान और गाँव के तालाब जैसी ग्राम-साझा भूमियाँ 'राष्ट्रीय' संसाधन हैं।"],
  C3, 0,
  "Only statement 1 is correct. Statement 2 is wrong: reserves are the subset of the stock that can be put to use with existing technical know-how but whose use has not yet begun -- water in dams and forests, for example; it is the stock that awaits the technology. "
  "Statement 3 is wrong: village commons, and public parks and playgrounds in towns, are community-owned resources, accessible to all the members of the community; national resources include minerals, water, forests and wildlife within the country's boundaries and its territorial waters.",
  "केवल कथन 1 सही है। कथन 2 गलत है: संचित कोष भंडार का वह उपसमूह है जिसका मौजूदा तकनीकी ज्ञान से उपयोग हो सकता है पर जिसका उपयोग अभी आरंभ नहीं हुआ -- जैसे बाँधों में जल और वन; तकनीक की प्रतीक्षा तो भंडार करता है। "
  "कथन 3 गलत है: ग्राम-साझा भूमियाँ, और नगरों में सार्वजनिक उद्यान तथा खेल के मैदान, सामुदायिक स्वामित्व वाले संसाधन हैं, जो समुदाय के सभी सदस्यों के लिए सुलभ हैं; राष्ट्रीय संसाधनों में देश की सीमाओं और उसके प्रादेशिक जल के भीतर के खनिज, जल, वन और वन्यजीव आते हैं।",
  f"{CI2} (Resources and Development).",
  "l1-geo-resource-classes-stock-reserves", craft="application")

# ---------------------------------------------------------------- medium Statement-I/II (1)
A(RS, "medium",
  "Natural gas is considered an environment-friendly fuel.",
  "प्राकृतिक गैस को पर्यावरण-अनुकूल ईंधन माना जाता है।",
  "When burnt, it releases more carbon dioxide than coal does.",
  "जलने पर यह कोयले से अधिक कार्बन डाइऑक्साइड छोड़ती है।",
  2,
  "Statement-I is correct but Statement-II is incorrect. Natural gas is regarded as a cleaner fuel precisely because it gives off less carbon dioxide, and far less ash and sulphur, than coal or oil for the same energy -- which is why it is used as compressed natural gas (CNG) in city transport and as a feedstock for fertilisers. "
  "It is still a fossil fuel, though, and leaks of methane, its main component and a strong greenhouse gas, reduce its advantage.",
  "कथन-I सही है, पर कथन-II गलत है। प्राकृतिक गैस को स्वच्छ ईंधन ठीक इसलिए माना जाता है कि समान ऊर्जा के लिए यह कोयले या तेल से कम कार्बन डाइऑक्साइड, और कहीं कम राख तथा सल्फ़र, छोड़ती है -- इसीलिए नगरीय परिवहन में संपीडित प्राकृतिक गैस (CNG) के रूप में और उर्वरकों के कच्चे माल के रूप में इसका उपयोग होता है। "
  "फिर भी यह एक जीवाश्म ईंधन है, और इसके मुख्य घटक, प्रबल ग्रीनहाउस गैस मीथेन, का रिसाव इसका लाभ घटा देता है।",
  f"{CI2} (Minerals and Energy Resources).",
  "l1-geo-natural-gas-cleaner-fuel", craft="inference")

write("geo_l1_t4_e.sql")
