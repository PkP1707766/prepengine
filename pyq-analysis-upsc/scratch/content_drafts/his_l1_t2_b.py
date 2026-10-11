# -*- coding: utf-8 -*-
"""Level 1 · Test 2 (History, NCERT Foundation) -- part B: Ancient India, the medium statement and pairs rows and
the hard rows (20 of the 36 Ancient rows; upsc_l1_cell_targets.mjs 2):
  medium statement 11, medium pairs 3, hard MCQ 2, hard statement 3, hard pairs 1.
Same angle and Level-2 exclusions as part A (his_l1_t2_a.py)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, write
from polity_common import C3, C4, T2

d.SUBJECT = "History"
d.REQUIRE_CRAFT = True
AN = "Ancient"
OP1 = "NCERT Class VI, History -- Our Pasts I"
TH1 = "NCERT Class XII, History -- Themes in Indian History, Part I"

# ---------------------------------------------------------------- medium statement (11)
S(AN, "medium", "Consider the following statements about agriculture in the Harappan civilisation:",
  "हड़प्पा सभ्यता में कृषि के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Terracotta models of the plough have been found at sites in Cholistan and at Banawali in Haryana.",
   "Traces of canals have been found at most Harappan sites in Punjab and Sind.",
   "Grains such as wheat, barley, lentil, chickpea and sesame have been found at Harappan sites."],
  ["चोलिस्तान के स्थलों और हरियाणा के बनावली में हल के मिट्टी (टेराकोटा) के प्रतिरूप मिले हैं।",
   "पंजाब और सिंध के अधिकांश हड़प्पा स्थलों पर नहरों के निशान मिले हैं।",
   "हड़प्पा स्थलों पर गेहूँ, जौ, मसूर, चना और तिल जैसे अनाज मिले हैं।"],
  C3, 1,
  "Statements 1 and 3 are correct. Plough models, along with representations of the bull on seals, suggest that oxen were used for ploughing, and charred grains show what was grown; millets come from sites in Gujarat, and rice is found less often. "
  "Statement 2 is wrong: traces of canals have been found only at Shortughai in Afghanistan, not in Punjab or Sind. Ancient canals may have silted up long ago, and water drawn from wells, or stored in reservoirs as at Dholavira, may also have been used.",
  "कथन 1 और 3 सही हैं। हल के प्रतिरूप, मुहरों पर बैल के चित्रों के साथ, बताते हैं कि जुताई के लिए बैलों का उपयोग होता था, और जले हुए दाने बताते हैं कि क्या उगाया जाता था; बाजरा गुजरात के स्थलों से मिलता है, और चावल कम मिलता है। "
  "कथन 2 गलत है: नहरों के निशान केवल अफ़ग़ानिस्तान के शोर्तुघई में मिले हैं, पंजाब या सिंध में नहीं। संभव है कि प्राचीन नहरें बहुत पहले गाद से भर गई हों, और कुओं से निकाले गए पानी, या धौलावीरा की तरह जलाशयों में जमा पानी, का भी उपयोग होता रहा हो।",
  f"{TH1}, Chapter 1 (Bricks, Beads and Bones).",
  "l1-his-harappan-agriculture-evidence", craft="precision")

S(AN, "medium", "Consider the following statements about the end of the mature Harappan civilisation:",
  "परिपक्व हड़प्पा सभ्यता के अंत के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["By about 1800 BCE most of the mature Harappan sites in regions such as Cholistan had been abandoned.",
   "Distinctive artefacts such as weights, seals and special beads disappeared, and writing, long-distance trade and craft specialisation declined."],
  ["लगभग 1800 ई.पू. तक चोलिस्तान जैसे क्षेत्रों के अधिकांश परिपक्व हड़प्पा स्थल छोड़ दिए गए थे।",
   "बाट, मुहरें और विशेष मनके जैसी विशिष्ट वस्तुएँ लुप्त हो गईं, और लेखन, लंबी दूरी का व्यापार तथा शिल्प विशेषज्ञता घट गए।"],
  T2, 2,
  "Both statements are correct. After about 1800 BCE many sites in regions like Cholistan were abandoned, while population moved to new settlements in Gujarat, Haryana and western Uttar Pradesh; the late Harappan cultures that followed were mainly rural. "
  "Weights, seals, special beads, writing, long-distance trade and craft specialisation disappeared. The explanations offered -- climatic change, deforestation, floods, the shifting or drying up of rivers, the overuse of the landscape -- may each apply to some settlements, but none accounts for the whole collapse.",
  "दोनों कथन सही हैं। लगभग 1800 ई.पू. के बाद चोलिस्तान जैसे क्षेत्रों के कई स्थल छोड़ दिए गए, जबकि आबादी गुजरात, हरियाणा और पश्चिमी उत्तर प्रदेश की नई बस्तियों में गई; बाद की उत्तर-हड़प्पा संस्कृतियाँ मुख्यतः ग्रामीण थीं। "
  "बाट, मुहरें, विशेष मनके, लेखन, लंबी दूरी का व्यापार और शिल्प विशेषज्ञता लुप्त हो गए। सुझाए गए कारण -- जलवायु परिवर्तन, वनों की कटाई, बाढ़, नदियों का मार्ग बदलना या सूखना, भूमि का अति-उपयोग -- कुछ बस्तियों पर लागू हो सकते हैं, पर कोई भी पूरे पतन की व्याख्या नहीं करता।",
  f"{TH1}, Chapter 1 (Bricks, Beads and Bones).",
  "l1-his-harappan-decline", craft="linkage")

S(AN, "medium", "Consider the following statements about the norms of family and marriage laid down in the Dharmasutras and Dharmashastras:",
  "धर्मसूत्रों और धर्मशास्त्रों में निर्धारित परिवार और विवाह के मानदंडों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["They recognised eight forms of marriage, of which the first four were considered 'good'.",
   "They encouraged marriage within one's own gotra.",
   "Under the rule of patriliny that they upheld, daughters had an equal claim with sons to the resources of the household."],
  ["उन्होंने विवाह के आठ प्रकार माने, जिनमें से पहले चार 'उत्तम' माने गए।",
   "उन्होंने अपने ही गोत्र के भीतर विवाह को प्रोत्साहित किया।",
   "उनके द्वारा समर्थित पितृवंशिकता के नियम में बेटियों का घर के संसाधनों पर बेटों के बराबर दावा था।"],
  C3, 0,
  "Only statement 1 is correct: the eight forms ranged from those considered 'good' -- the first four -- to those that were condemned. "
  "Statement 2 is wrong: members of the same gotra could not marry; a woman was expected to give up her father's gotra and adopt her husband's on marriage. "
  "Statement 3 is wrong: under patriliny, sons claimed the resources of their fathers, including the throne in royal families, while daughters were thought to have no claim to the household's resources.",
  "केवल कथन 1 सही है: आठ प्रकार 'उत्तम' माने गए -- पहले चार -- से लेकर निंदित प्रकारों तक थे। "
  "कथन 2 गलत है: एक ही गोत्र के सदस्य विवाह नहीं कर सकते थे; विवाह पर स्त्री से पिता का गोत्र छोड़कर पति का गोत्र अपनाने की अपेक्षा थी। "
  "कथन 3 गलत है: पितृवंशिकता में बेटे पिता के संसाधनों पर, राजपरिवारों में सिंहासन सहित, दावा करते थे, जबकि बेटियों का घर के संसाधनों पर कोई दावा नहीं माना जाता था।",
  f"{TH1}, Chapter 3 (Kinship, Caste and Class).",
  "l1-his-dharmasutra-marriage-gotra", craft="precision")

S(AN, "medium", "Consider the following statements about women in early Buddhism:",
  "प्रारंभिक बौद्ध धर्म में महिलाओं के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Mahapajapati Gotami, the Buddha's foster mother, was the first woman to be ordained as a bhikkhuni.",
   "The Therigatha is a collection of verses composed by bhikkhunis.",
   "Bhikkhunis were barred from teaching the dhamma, which only monks could do."],
  ["बुद्ध की धाय माँ महाप्रजापति गोतमी भिक्खुनी के रूप में दीक्षित होने वाली पहली महिला थीं।",
   "थेरीगाथा भिक्खुनियों द्वारा रचित पद्यों का संग्रह है।",
   "भिक्खुनियों को धम्म का उपदेश देने से रोका गया था, जो केवल भिक्षु कर सकते थे।"],
  C3, 1,
  "Statements 1 and 2 are correct. According to Buddhist texts, the Buddha's foster mother Mahapajapati Gotami was the first woman ordained, after his disciple Ananda persuaded him to admit women. "
  "The Therigatha, part of the Sutta Pitaka, is a unique collection of verses composed by bhikkhunis, which gives an insight into women's social and spiritual experiences. "
  "Statement 3 is wrong: many women who entered the sangha became teachers of the dhamma and went on to become theris, respected women who had attained liberation.",
  "कथन 1 और 2 सही हैं। बौद्ध ग्रंथों के अनुसार, बुद्ध की धाय माँ महाप्रजापति गोतमी पहली दीक्षित महिला थीं, जब उनके शिष्य आनंद ने उन्हें महिलाओं को प्रवेश देने के लिए मनाया। "
  "सुत्त पिटक का भाग थेरीगाथा भिक्खुनियों द्वारा रचित पद्यों का एक अनूठा संग्रह है, जो महिलाओं के सामाजिक और आध्यात्मिक अनुभवों की झलक देता है। "
  "कथन 3 गलत है: संघ में आई कई महिलाएँ धम्म की उपदेशिका बनीं और आगे चलकर थेरी, यानी मुक्ति प्राप्त सम्मानित महिलाएँ, बनीं।",
  f"{TH1}, Chapter 4 (Thinkers, Beliefs and Buildings).",
  "l1-his-bhikkhunis-therigatha", craft="precision")

S(AN, "medium", "Consider the following statements about the building of stupas:",
  "स्तूपों के निर्माण के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Stupas were built over relics, such as bodily remains of the Buddha or objects he had used.",
   "Inscriptions at Sanchi record that a guild of ivory workers financed part of one of its gateways.",
   "Stupas were paid for only by kings, since ordinary men and women could not make gifts to the sangha."],
  ["स्तूप अवशेषों, जैसे बुद्ध के शरीर के अवशेषों या उनकी प्रयुक्त वस्तुओं, के ऊपर बनाए गए।",
   "साँची के अभिलेख बताते हैं कि हाथीदाँत के कारीगरों की एक श्रेणी ने उसके एक तोरणद्वार के एक भाग का ख़र्च उठाया।",
   "स्तूपों का ख़र्च केवल राजा उठाते थे, क्योंकि सामान्य स्त्री-पुरुष संघ को दान नहीं दे सकते थे।"],
  C3, 1,
  "Statements 1 and 2 are correct. Relics placed in stupas -- bodily remains of the Buddha or objects he used -- made them sacred. "
  "Inscriptions on railings and pillars record the donors: kings such as the Satavahanas, guilds such as the ivory workers who financed part of a gateway at Sanchi, and hundreds of women and men, including bhikkhus and bhikkhunis, who named their villages or towns and sometimes their occupations. "
  "Statement 3 is wrong: the gifts of ordinary people are recorded in large numbers.",
  "कथन 1 और 2 सही हैं। स्तूपों में रखे अवशेष -- बुद्ध के शरीर के अवशेष या उनकी प्रयुक्त वस्तुएँ -- उन्हें पवित्र बनाते थे। "
  "वेदिकाओं और स्तंभों पर अंकित अभिलेख दानदाताओं को दर्ज करते हैं: सातवाहनों जैसे राजा, साँची में एक तोरणद्वार के भाग का ख़र्च उठाने वाले हाथीदाँत के कारीगरों जैसी श्रेणियाँ, और भिक्खुओं-भिक्खुनियों सहित सैकड़ों स्त्री-पुरुष, जिन्होंने अपने गाँव या नगर और कभी-कभी अपने व्यवसाय के नाम दिए। "
  "कथन 3 गलत है: सामान्य लोगों के दान बड़ी संख्या में दर्ज हैं।",
  f"{TH1}, Chapter 4 (Thinkers, Beliefs and Buildings).",
  "l1-his-stupa-relics-donors", craft="precision")

S(AN, "medium", "Consider the following statements about the kingdoms of south India in the sixth and seventh centuries CE:",
  "छठी और सातवीं सदी ईस्वी के दक्षिण भारत के राज्यों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The prashasti of Pulakeshin II at Aihole was composed by Banabhatta, the court poet of Harshavardhana.",
   "Under the Pallavas, the nagaram was an assembly of brahmana landowners."],
  ["ऐहोल में पुलकेशिन द्वितीय की प्रशस्ति हर्षवर्धन के दरबारी कवि बाणभट्ट ने रची थी।",
   "पल्लवों के अधीन नगरम ब्राह्मण भूस्वामियों की सभा थी।"],
  T2, 3,
  "Neither statement is correct. Statement 1 is wrong in the poet: Pulakeshin II's prashasti at Aihole was composed by his own court poet, Ravikirti; Banabhatta wrote the Harshacharita, a biography of Harshavardhana -- whom, Ravikirti claims, Pulakeshin checked. "
  "Statement 2 is wrong: the sabha was the assembly of brahmana landowners; the ur was a village assembly in areas where the landowners were not brahmanas, and the nagaram was an organisation of merchants.",
  "कोई भी कथन सही नहीं है। कथन 1 कवि में गलत है: ऐहोल में पुलकेशिन द्वितीय की प्रशस्ति उनके अपने दरबारी कवि रविकीर्ति ने रची थी; बाणभट्ट ने हर्षवर्धन की जीवनी हर्षचरित लिखी -- वही हर्ष, जिसे रविकीर्ति के अनुसार पुलकेशिन ने रोका। "
  "कथन 2 गलत है: सभा ब्राह्मण भूस्वामियों की सभा थी; उर उन क्षेत्रों की ग्राम सभा थी जहाँ भूस्वामी ब्राह्मण नहीं थे, और नगरम व्यापारियों का संगठन था।",
  f"{OP1}, Chapter 11 (New Empires and Kingdoms).",
  "l1-his-aihole-ravikirti-assemblies", craft="precision")

S(AN, "medium", "Consider the following statements about how the rulers of the early kingdoms raised resources, about 2,500 years ago:",
  "लगभग 2,500 वर्ष पहले के प्रारंभिक राज्यों के शासक संसाधन कैसे जुटाते थे, इसके बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The tax on crops was usually fixed at one-sixth of what was produced.",
   "Craftspersons could pay their taxes in the form of labour, working for the king for a day every month.",
   "Herders were expected to pay taxes in the form of animals and animal produce."],
  ["फ़सलों पर कर प्रायः उपज का छठा भाग तय होता था।",
   "शिल्पकार अपने कर श्रम के रूप में, हर महीने एक दिन राजा के लिए काम करके, चुका सकते थे।",
   "पशुपालकों से पशुओं और पशु-उत्पादों के रूप में कर देने की अपेक्षा थी।"],
  C3, 2,
  "All three statements are correct. Taxes on crops, usually a sixth of the produce and known as bhaga or 'share', were the most important, since most people were farmers. "
  "A weaver or a smith might work a day a month for the king, herders gave animals and animal produce, traders paid taxes on goods bought and sold, and hunters and gatherers gave forest produce. The new taxes paid for armies, forts and officials.",
  "तीनों कथन सही हैं। फ़सलों पर कर, प्रायः उपज का छठा भाग और 'भाग' कहलाने वाला, सबसे महत्वपूर्ण था, क्योंकि अधिकांश लोग किसान थे। "
  "बुनकर या लोहार महीने में एक दिन राजा के लिए काम कर सकता था, पशुपालक पशु और पशु-उत्पाद देते थे, व्यापारी ख़रीदी-बेची गई वस्तुओं पर कर देते थे, और शिकारी-संग्राहक वन-उपज देते थे। नए करों से सेनाओं, किलों और अधिकारियों का ख़र्च चलता था।",
  f"{OP1}, Chapter 6 (Kingdoms, Kings and an Early Republic).",
  "l1-his-janapada-taxes-bhaga", craft="recall")

S(AN, "medium", "Consider the following statements about the growth of agriculture in the Ganga valley and beyond from about 600 BCE:",
  "लगभग 600 ई.पू. से गंगा घाटी और उसके बाहर कृषि के विकास के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The transplantation of paddy increased yields, though it was labour-intensive.",
   "The iron-tipped ploughshare was used mainly in dry areas with light, sandy soils.",
   "As production grew, the differences among the people who worked the land disappeared."],
  ["धान की रोपाई से उपज बढ़ी, यद्यपि इसमें श्रम बहुत लगता था।",
   "लोहे के फाल वाला हल मुख्य रूप से हल्की, रेतीली मिट्टी वाले शुष्क क्षेत्रों में प्रयुक्त होता था।",
   "उत्पादन बढ़ने के साथ भूमि पर काम करने वाले लोगों के बीच के अंतर मिट गए।"],
  C3, 0,
  "Only statement 1 is correct: transplantation dramatically raised paddy production in parts of the Ganga valley, though it meant back-breaking work for the producers. "
  "Statement 2 is wrong: the iron-tipped ploughshare was used to turn the heavy alluvial soil of areas with high rainfall; cultivators in semi-arid areas such as parts of Punjab and Rajasthan did not adopt it until much later, and hill peoples kept to hoe agriculture. "
  "Statement 3 is wrong: the benefits were very uneven -- the texts describe a growing differentiation, from large landowners and village headmen to small peasants and landless labourers.",
  "केवल कथन 1 सही है: रोपाई से गंगा घाटी के कुछ भागों में धान का उत्पादन बहुत बढ़ा, यद्यपि उत्पादकों के लिए इसका अर्थ कमरतोड़ मेहनत था। "
  "कथन 2 गलत है: लोहे के फाल वाले हल से अधिक वर्षा वाले क्षेत्रों की भारी जलोढ़ मिट्टी पलटी जाती थी; पंजाब और राजस्थान के कुछ भागों जैसे अर्ध-शुष्क क्षेत्रों के किसानों ने इसे बहुत बाद में अपनाया, और पहाड़ी लोग कुदाल की खेती करते रहे। "
  "कथन 3 गलत है: लाभ बहुत असमान थे -- ग्रंथ बढ़ते विभेदन का वर्णन करते हैं, बड़े भूस्वामियों और ग्राम-प्रधानों से लेकर छोटे किसानों और भूमिहीन मज़दूरों तक।",
  f"{TH1}, Chapter 2 (Kings, Farmers and Towns).",
  "l1-his-iron-plough-transplantation", craft="precision")

S(AN, "medium", "Consider the following places:",
  "निम्नलिखित स्थानों पर विचार कीजिए:",
  ["Taxila", "Ujjayini", "Tosali", "Suvarnagiri"],
  ["तक्षशिला", "उज्जयिनी", "तोसली", "सुवर्णगिरि"],
  C4, 3,
  "All four were provincial centres. Ashokan inscriptions mention five major political centres in the empire: the capital Pataliputra and the provincial centres of Taxila in the north-west, Ujjayini in Malwa, Tosali in Kalinga (Odisha) and Suvarnagiri in Karnataka. "
  "The great distances between them are one reason historians doubt that the empire could have been run uniformly from the capital.",
  "चारों प्रांतीय केंद्र थे। अशोक के अभिलेख साम्राज्य के पाँच प्रमुख राजनीतिक केंद्रों का उल्लेख करते हैं: राजधानी पाटलिपुत्र और प्रांतीय केंद्र उत्तर-पश्चिम में तक्षशिला, मालवा में उज्जयिनी, कलिंग (ओडिशा) में तोसली और कर्नाटक में सुवर्णगिरि। "
  "उनके बीच की बड़ी दूरियाँ एक कारण हैं जिनसे इतिहासकार संदेह करते हैं कि साम्राज्य राजधानी से एक समान रूप से चलाया जा सकता था।",
  f"{TH1}, Chapter 2 (Kings, Farmers and Towns).",
  "l1-his-mauryan-provincial-centres", craft="recall",
  closing="How many of the above were provincial centres of the Mauryan empire?",
  closing_hi="उपर्युक्त में से कितने मौर्य साम्राज्य के प्रांतीय केंद्र थे?")

S(AN, "medium", "Consider the following statements about the idea of bhakti in the early centuries CE:",
  "प्रारंभिक ईस्वी सदियों में भक्ति के विचार के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Bhagavad Gita, in which Krishna asks Arjuna to abandon all dharmas and take refuge in him, is an early expression of the idea of bhakti.",
   "Bhakti was directed only towards Vishnu and his avatars."],
  ["भगवद्गीता, जिसमें कृष्ण अर्जुन से सब धर्म छोड़कर अपनी शरण में आने को कहते हैं, भक्ति के विचार की एक प्रारंभिक अभिव्यक्ति है।",
   "भक्ति केवल विष्णु और उनके अवतारों के प्रति थी।"],
  T2, 0,
  "Only statement 1 is correct. In the Gita, a sacred text included in the Mahabharata, Krishna promises to free from evil those who take refuge in him. "
  "Bhakti -- usually understood as a person's devotion to his or her chosen deity -- could be offered by anyone, rich or poor, of 'high' or 'low' caste, man or woman. "
  "Statement 2 is wrong: devotees worshipped deities such as Shiva, Vishnu and Durga, and the idea became so popular that even Buddhists and Jainas adopted it.",
  "केवल कथन 1 सही है। महाभारत में सम्मिलित पवित्र ग्रंथ गीता में कृष्ण अपनी शरण में आने वालों को बुराई से मुक्त करने का वचन देते हैं। "
  "भक्ति -- प्रायः किसी व्यक्ति की अपने चुने हुए देवता के प्रति श्रद्धा -- कोई भी कर सकता था, धनी या निर्धन, 'ऊँची' या 'नीची' जाति का, स्त्री या पुरुष। "
  "कथन 2 गलत है: भक्त शिव, विष्णु और दुर्गा जैसे देवी-देवताओं की उपासना करते थे, और यह विचार इतना लोकप्रिय हुआ कि बौद्धों और जैनों ने भी इसे अपनाया।",
  f"{OP1}, Chapter 10 (Traders, Kings and Pilgrims).",
  "l1-his-bhakti-gita-early", craft="precision")

S(AN, "medium", "Consider the following statements about the thinkers of the sixth century BCE and their teachings:",
  "छठी सदी ई.पू. के चिंतकों और उनकी शिक्षाओं के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Buddha's teachings were written down during his lifetime by his disciples.",
   "According to Jaina teaching, only human beings have a soul or life.",
   "Mahavira taught that the cycle of birth and rebirth could be broken only by performing Vedic sacrifices."],
  ["बुद्ध की शिक्षाएँ उनके जीवनकाल में ही उनके शिष्यों ने लिख ली थीं।",
   "जैन शिक्षा के अनुसार केवल मनुष्यों में आत्मा या जीवन होता है।",
   "महावीर ने सिखाया कि जन्म और पुनर्जन्म का चक्र केवल वैदिक यज्ञ करके तोड़ा जा सकता है।"],
  C3, 3,
  "None of the statements is correct. Statement 1 is wrong: neither the Buddha nor Mahavira wrote down his teachings; the Buddha's were compiled by his disciples after his death. "
  "Statement 2 is wrong: the Jainas held that the entire world is animated -- even stones, rocks and water have life -- which is why non-injury to all living beings is central to their teaching. "
  "Statement 3 is wrong: the Jainas, like the Buddhists, rejected sacrifice as the path to liberation; the cycle of karma could be broken only through renunciation and penance, which meant leaving home and living in monasteries.",
  "कोई भी कथन सही नहीं है। कथन 1 गलत है: न बुद्ध ने, न महावीर ने अपनी शिक्षाएँ लिखीं; बुद्ध की शिक्षाएँ उनकी मृत्यु के बाद उनके शिष्यों ने संकलित कीं। "
  "कथन 2 गलत है: जैन मानते थे कि पूरा संसार सजीव है -- पत्थरों, चट्टानों और जल में भी जीवन है -- इसीलिए सभी जीवों के प्रति अहिंसा उनकी शिक्षा का केंद्र है। "
  "कथन 3 गलत है: बौद्धों की तरह जैनों ने भी यज्ञ को मुक्ति का मार्ग नहीं माना; कर्म का चक्र केवल त्याग और तपस्या से तोड़ा जा सकता था, जिसका अर्थ था घर छोड़कर विहारों में रहना।",
  f"{TH1}, Chapter 4 (Thinkers, Beliefs and Buildings).",
  "l1-his-early-thinkers-jiva-karma", craft="precision")

# ---------------------------------------------------------------- medium pairs (3)
P(AN, "medium", "Consider the following pairs of places and the raw materials the Harappans obtained from or near them:",
  "स्थानों और उन कच्चे मालों के निम्नलिखित युग्मों पर विचार कीजिए जो हड़प्पावासी वहाँ से या उनके पास से प्राप्त करते थे:",
  ["Shortughai : Lapis lazuli, a blue stone", "Nageshwar : Shell", "Lothal : Carnelian", "Khetri : Tin"],
  ["शोर्तुघई : लाजवर्द (lapis lazuli), एक नीला पत्थर", "नागेश्वर : सीप (शंख)", "लोथल : कार्नेलियन (इंद्रगोप)", "खेतड़ी : टिन"],
  2,
  "Pairs 1, 2 and 3 are correctly matched. The Harappans set up settlements close to sources of raw material: Nageshwar and Balakot near the coast for shell, Shortughai in Afghanistan near the best source of lapis lazuli, and Lothal near sources of carnelian (from Bharuch in Gujarat), steatite and metal. "
  "Pair 4 is wrong: the Harappans sent expeditions to the Khetri region of Rajasthan for copper (and to south India for gold).",
  "युग्म 1, 2 और 3 सही सुमेलित हैं। हड़प्पावासियों ने कच्चे माल के स्रोतों के पास बस्तियाँ बसाईं: सीप के लिए तट के पास नागेश्वर और बालाकोट, लाजवर्द के सबसे अच्छे स्रोत के पास अफ़ग़ानिस्तान में शोर्तुघई, और कार्नेलियन (गुजरात के भरूच से), सेलखड़ी और धातु के स्रोतों के पास लोथल। "
  "युग्म 4 गलत है: हड़प्पावासियों ने ताँबे के लिए राजस्थान के खेतड़ी क्षेत्र में (और सोने के लिए दक्षिण भारत में) अभियान भेजे।",
  f"{TH1}, Chapter 1 (Bricks, Beads and Bones).",
  "l1-his-harappan-raw-material-sites", craft="linkage")

P(AN, "medium", "Consider the following pairs of terms found in early texts and inscriptions and their meanings:",
  "प्रारंभिक ग्रंथों और अभिलेखों में मिलने वाले शब्दों और उनके अर्थों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Agrahara : Land granted to a brahmana, usually free of land revenue", "Kammakara : A hired labourer",
   "Uzhavar : A ploughman, in early Tamil compositions", "Dasa : A slave"],
  ["अग्रहार : ब्राह्मण को दी गई भूमि, जो प्रायः भू-राजस्व से मुक्त होती थी", "कम्मकार : भाड़े का मज़दूर",
   "उऴवर : प्रारंभिक तमिल रचनाओं में हलवाहा", "दास : ग़ुलाम"],
  3,
  "All four pairs are correctly matched. An agrahara was land granted to a brahmana, who was usually exempt from land revenue and other dues and was often given the right to collect them from the local people. "
  "Early Buddhist texts speak of dasas (slaves) and kammakaras (hired workers) at the bottom of rural society, and early Tamil compositions distinguish the vellalar (large landowners), the uzhavar (ploughmen) and the adimai (slaves).",
  "चारों युग्म सही सुमेलित हैं। अग्रहार ब्राह्मण को दी गई भूमि थी, जिस पर वह प्रायः भू-राजस्व और अन्य देयों से मुक्त होता था और जिसे अक्सर स्थानीय लोगों से ये वसूलने का अधिकार भी मिलता था। "
  "प्रारंभिक बौद्ध ग्रंथ ग्रामीण समाज के निचले स्तर पर दासों और कम्मकारों (भाड़े के कामगारों) का उल्लेख करते हैं, और प्रारंभिक तमिल रचनाएँ वेल्लालर (बड़े भूस्वामी), उऴवर (हलवाहे) और अडिमै (दास) में भेद करती हैं।",
  f"{TH1}, Chapter 2 (Kings, Farmers and Towns).",
  "l1-his-early-agrarian-terms-pairs", craft="precision")

P(AN, "medium", "Consider the following pairs of archaeologists and their work:",
  "पुरातत्वविदों और उनके कार्य के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Alexander Cunningham : First Director-General of the Archaeological Survey of India",
   "John Marshall : Announced the discovery of a new civilisation in the Indus valley in 1924",
   "R.E.M. Wheeler : Insisted that excavation follow the stratigraphy of a mound rather than uniform horizontal units",
   "Daya Ram Sahni : Found seals at Harappa in the early 1920s"],
  ["अलेक्ज़ेंडर कनिंघम : भारतीय पुरातत्व सर्वेक्षण के पहले महानिदेशक",
   "जॉन मार्शल : 1924 में सिंधु घाटी में एक नई सभ्यता की खोज की घोषणा की",
   "आर.ई.एम. व्हीलर : इस पर ज़ोर दिया कि उत्खनन एक समान क्षैतिज इकाइयों के बजाय टीले के स्तरों (stratigraphy) के अनुसार हो",
   "दयाराम साहनी : 1920 के दशक के आरंभ में हड़प्पा में मुहरें खोजीं"],
  3,
  "All four pairs are correctly matched. Cunningham, the first Director-General of the Archaeological Survey of India, used the accounts of Chinese Buddhist pilgrims to locate early settlements, and did not realise how old the Harappan seal he was shown was. "
  "Daya Ram Sahni found seals at Harappa in the early 1920s and R.D. Banerji similar seals at Mohenjodaro; on that basis John Marshall, the Director-General, announced a new civilisation in 1924. "
  "Marshall dug in uniform horizontal units, ignoring stratigraphy, so finds from different layers were mixed up; R.E.M. Wheeler, Director-General from 1944, corrected this by following the stratigraphy of the mound.",
  "चारों युग्म सही सुमेलित हैं। भारतीय पुरातत्व सर्वेक्षण के पहले महानिदेशक कनिंघम ने प्रारंभिक बस्तियों को खोजने के लिए चीनी बौद्ध तीर्थयात्रियों के वृत्तांतों का उपयोग किया, और उन्हें दिखाई गई हड़प्पा मुहर कितनी पुरानी है, यह वे नहीं समझ पाए। "
  "दयाराम साहनी ने 1920 के दशक के आरंभ में हड़प्पा में और आर.डी. बनर्जी ने मोहनजोदड़ो में वैसी ही मुहरें खोजीं; इसी आधार पर महानिदेशक जॉन मार्शल ने 1924 में एक नई सभ्यता की घोषणा की। "
  "मार्शल ने एक समान क्षैतिज इकाइयों में खुदाई की और स्तरों की उपेक्षा की, जिससे अलग-अलग परतों की वस्तुएँ मिल गईं; 1944 से महानिदेशक आर.ई.एम. व्हीलर ने टीले के स्तरों का अनुसरण करके इसे सुधारा।",
  f"{TH1}, Chapter 1 (Bricks, Beads and Bones).",
  "l1-his-harappan-archaeologists-pairs", craft="precision")

# ---------------------------------------------------------------- hard MCQ (2)
M(AN, "hard", "Inscriptions are a key source for early Indian history. Which one of the following is a limitation that historians must keep in mind when using them?",
  "अभिलेख प्रारंभिक भारतीय इतिहास का एक प्रमुख स्रोत हैं। निम्नलिखित में से कौन-सी एक सीमा है जिसे इनका उपयोग करते समय इतिहासकारों को ध्यान में रखना चाहिए?",
  ["They record what their patrons wanted remembered, and may omit or exaggerate events",
   "They cannot be dated in any way, because none of them mentions a ruler or an era",
   "They were always written in a single language and script throughout the subcontinent",
   "They record only the daily lives of ordinary peasants and say nothing about rulers"],
  ["वे वही दर्ज करते हैं जो उनके संरक्षक याद रखवाना चाहते थे, और घटनाओं को छोड़ या बढ़ा-चढ़ा सकते हैं",
   "उनकी तिथि किसी भी तरह तय नहीं की जा सकती, क्योंकि उनमें से कोई भी किसी शासक या संवत् का उल्लेख नहीं करता",
   "वे पूरे उपमहाद्वीप में सदा एक ही भाषा और लिपि में लिखे गए",
   "वे केवल सामान्य किसानों का दैनिक जीवन दर्ज करते हैं और शासकों के बारे में कुछ नहीं कहते"],
  0,
  "Inscriptions present the point of view of those who commissioned them -- kings, donors, officials -- so routine agricultural practices and the joys and sorrows of daily life are rarely recorded, and claims such as a prashasti's victories may be exaggerated. "
  "There are technical limits too: letters may be faint, damaged or missing, the exact meaning of some words is uncertain, and many inscriptions have not been deciphered, published or even preserved. "
  "Many inscriptions do name rulers or give dates in eras, they are found in several languages and scripts, and most record the deeds of the powerful rather than peasants' lives.",
  "अभिलेख उन्हें बनवाने वालों -- राजाओं, दानदाताओं, अधिकारियों -- का दृष्टिकोण प्रस्तुत करते हैं, इसलिए सामान्य कृषि-कार्य और दैनिक जीवन के सुख-दुख शायद ही दर्ज होते हैं, और प्रशस्ति में विजयों जैसे दावे बढ़ा-चढ़ाकर हो सकते हैं। "
  "तकनीकी सीमाएँ भी हैं: अक्षर धुँधले, क्षतिग्रस्त या ग़ायब हो सकते हैं, कुछ शब्दों का सटीक अर्थ अनिश्चित है, और कई अभिलेख न पढ़े गए, न प्रकाशित हुए, न ही बचे रहे। "
  "कई अभिलेख शासकों के नाम या संवत् में तिथि देते हैं, वे कई भाषाओं और लिपियों में मिलते हैं, और अधिकांश किसानों के जीवन के बजाय शक्तिशाली लोगों के कार्य दर्ज करते हैं।",
  f"{TH1}, Chapter 2 (Kings, Farmers and Towns).",
  "l1-his-inscriptions-limits", pos=3, craft="inference")

M(AN, "hard", "Thousands of copper coins issued by the Yaudheyas, a tribal republic of Punjab and Haryana, have been found. What does this suggest to historians?",
  "पंजाब और हरियाणा के एक जनजातीय गणराज्य, यौधेयों, द्वारा जारी ताँबे के हज़ारों सिक्के मिले हैं। इससे इतिहासकारों को क्या संकेत मिलता है?",
  ["Republics, and not only kingdoms, took part in trade and could issue their own coins",
   "The Yaudheyas used coins only as ornaments, since republics had no need for trade",
   "The Yaudheyas were officials who minted coins on behalf of the Kushana emperors",
   "Copper coins came into use only after gold and silver coins had gone out of circulation"],
  ["केवल राज्य ही नहीं, गणराज्य भी व्यापार में भाग लेते थे और अपने सिक्के जारी कर सकते थे",
   "यौधेय सिक्कों का उपयोग केवल आभूषण के रूप में करते थे, क्योंकि गणराज्यों को व्यापार की आवश्यकता नहीं थी",
   "यौधेय कुषाण सम्राटों की ओर से सिक्के ढालने वाले अधिकारी थे",
   "ताँबे के सिक्के तभी प्रचलन में आए जब सोने और चाँदी के सिक्के प्रचलन से बाहर हो गए"],
  0,
  "Coins were issued not only by kings but also by merchants, bankers and townspeople, and by tribal republics such as the Yaudheyas (about the first century CE); several thousand Yaudheya copper coins point to their interest and participation in economic exchange. "
  "The earliest coins, the punch-marked ones, were of silver and copper, and copper coinage continued alongside the gold coins issued later.",
  "सिक्के केवल राजा ही नहीं, व्यापारी, साहूकार और नगरवासी भी, और यौधेयों (लगभग पहली सदी ईस्वी) जैसे जनजातीय गणराज्य भी जारी करते थे; यौधेयों के कई हज़ार ताँबे के सिक्के आर्थिक लेन-देन में उनकी रुचि और भागीदारी की ओर संकेत करते हैं। "
  "सबसे प्रारंभिक, आहत (punch-marked) सिक्के चाँदी और ताँबे के थे, और बाद में जारी सोने के सिक्कों के साथ-साथ ताँबे के सिक्के भी चलते रहे।",
  f"{TH1}, Chapter 2 (Kings, Farmers and Towns).",
  "l1-his-yaudheya-coins-republics", pos=1, craft="inference")

# ---------------------------------------------------------------- hard statement (3)
S(AN, "hard", "Consider the following statements about the debate on political authority in the Harappan civilisation:",
  "हड़प्पा सभ्यता में राजनीतिक सत्ता पर बहस के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Royal burials and inscriptions naming kings show that the Harappan cities were ruled by kings.",
   "Some archaeologists think that Harappan society had no rulers, and that everybody enjoyed equal status.",
   "The uniformity of Harappan artefacts and the planning of settlements suggest to some scholars that a central authority took decisions."],
  ["राजसी समाधियाँ और राजाओं के नाम वाले अभिलेख दिखाते हैं कि हड़प्पा के नगरों पर राजा शासन करते थे।",
   "कुछ पुरातत्वविद मानते हैं कि हड़प्पा समाज में कोई शासक नहीं था, और सबकी हैसियत बराबर थी।",
   "हड़प्पा की वस्तुओं की एकरूपता और बस्तियों की योजना कुछ विद्वानों को बताती है कि निर्णय कोई केंद्रीय सत्ता लेती थी।"],
  C3, 1,
  "Statements 2 and 3 are correct. Three views are put forward: that there were no rulers and everybody enjoyed equal status; that there was no single ruler but several, with cities such as Mohenjodaro and Harappa having their own; and that there was a single state, given the similarity of artefacts, the planned settlements, the standard ratio of brick sizes and the settlements near sources of raw material. "
  "Statement 1 is wrong: no royal burials or inscriptions naming kings have been found -- the script is undeciphered, and the large building labelled a 'palace' at Mohenjodaro yielded no spectacular finds.",
  "कथन 2 और 3 सही हैं। तीन मत रखे गए हैं: कि कोई शासक नहीं था और सबकी हैसियत बराबर थी; कि एक नहीं, कई शासक थे, और मोहनजोदड़ो तथा हड़प्पा जैसे नगरों के अपने-अपने शासक थे; और कि एक ही राज्य था, क्योंकि वस्तुओं में समानता, नियोजित बस्तियाँ, ईंटों के आकार का मानक अनुपात और कच्चे माल के स्रोतों के पास बस्तियाँ मिलती हैं। "
  "कथन 1 गलत है: कोई राजसी समाधि या राजाओं के नाम वाला अभिलेख नहीं मिला है -- लिपि अपठित है, और मोहनजोदड़ो में 'महल' कहलाने वाली बड़ी इमारत से कोई असाधारण वस्तु नहीं मिली।",
  f"{TH1}, Chapter 1 (Bricks, Beads and Bones).",
  "l1-his-harappan-political-authority", craft="inference")

S(AN, "hard", "Consider the following statements about the Mahabharata as a historical source:",
  "एक ऐतिहासिक स्रोत के रूप में महाभारत के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It was composed by a single author over a short period.",
   "Historians divide its contents into 'narrative' and 'didactic' sections, the latter dealing with social norms.",
   "The text has traditionally been classified as itihasa, a word meaning 'thus it was'."],
  ["इसकी रचना एक ही लेखक ने थोड़े समय में की।",
   "इतिहासकार इसकी सामग्री को 'आख्यानात्मक' और 'उपदेशात्मक' भागों में बाँटते हैं, जिनमें दूसरा भाग सामाजिक मानदंडों से संबंधित है।",
   "इस ग्रंथ को परंपरागत रूप से इतिहास माना गया है, जिस शब्द का अर्थ है 'ऐसा ही था'।"],
  C3, 1,
  "Statements 2 and 3 are correct. The didactic sections lay down social norms, while the narrative sections tell the stories -- though the division is not watertight. Many historians think that, as itihasa, the text may preserve memories of real conflicts between kinfolk. "
  "Statement 1 is wrong: the epic grew over about a thousand years from about 500 BCE; the original story was probably composed by charioteer-bards called sutas, and from about the fifth century BCE brahmanas took it over and began to write it down, so the present text, of over 100,000 verses, has many layers.",
  "कथन 2 और 3 सही हैं। उपदेशात्मक भाग सामाजिक मानदंड निर्धारित करते हैं, जबकि आख्यानात्मक भाग कथाएँ सुनाते हैं -- यद्यपि यह विभाजन पूर्णतः अलग नहीं है। कई इतिहासकार मानते हैं कि इतिहास होने के नाते यह ग्रंथ बंधु-बांधवों के बीच वास्तविक संघर्षों की स्मृति सँजोए हो सकता है। "
  "कथन 1 गलत है: महाकाव्य लगभग 500 ई.पू. से लगभग एक हज़ार वर्षों में बढ़ा; मूल कथा संभवतः सूत कहलाने वाले सारथी-चारणों ने रची, और लगभग पाँचवीं सदी ई.पू. से ब्राह्मणों ने इसे अपनाकर लिखना शुरू किया, इसलिए एक लाख से अधिक श्लोकों वाले वर्तमान पाठ में कई परतें हैं।",
  f"{TH1}, Chapter 3 (Kinship, Caste and Class).",
  "l1-his-mahabharata-narrative-didactic", craft="precision")

S(AN, "hard", "Consider the following statements about how archaeologists have interpreted Harappan religion:",
  "पुरातत्वविदों ने हड़प्पा धर्म की व्याख्या कैसे की है, इसके बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Some early archaeologists identified a figure seated cross-legged on some seals, sometimes surrounded by animals, as a 'proto-Shiva'.",
   "Such identifications rest on comparisons with much later texts and practices, so historians treat them with caution.",
   "Heavily jewelled terracotta figurines of women have been regarded by some as mother goddesses."],
  ["कुछ प्रारंभिक पुरातत्वविदों ने कुछ मुहरों पर पालथी मारकर बैठी, कभी-कभी जानवरों से घिरी एक आकृति को 'आद्य-शिव' माना।",
   "ऐसी पहचानें बहुत बाद के ग्रंथों और प्रथाओं से तुलना पर टिकी हैं, इसलिए इतिहासकार इन्हें सावधानी से देखते हैं।",
   "भारी आभूषणों से सजी स्त्रियों की मिट्टी (टेराकोटा) की मूर्तियों को कुछ लोगों ने मातृदेवी माना है।"],
  C3, 2,
  "All three statements are correct. Objects that seemed unusual or unfamiliar -- jewelled female figurines, some regarded as mother goddesses; stone statues of men in a standardised posture; a cross-legged 'yogic' figure on seals, sometimes surrounded by animals, regarded as 'proto-Shiva'; and conical stones classified as lingas -- have often been taken to have religious significance. "
  "But these readings assume that later traditions offer parallels to earlier ones: the Rigveda mentions Rudra, a name used for Shiva in later traditions, yet does not describe him as Pashupati or as a yogi, so historians treat such identifications with caution.",
  "तीनों कथन सही हैं। असामान्य या अपरिचित लगने वाली वस्तुओं -- आभूषणों से सजी स्त्री-मूर्तियाँ, जिनमें से कुछ को मातृदेवी माना गया; एक मानक मुद्रा में पुरुषों की पत्थर की मूर्तियाँ; मुहरों पर पालथी मारे 'योगी' जैसी आकृति, कभी-कभी जानवरों से घिरी, जिसे 'आद्य-शिव' माना गया; और लिंग के रूप में वर्गीकृत शंक्वाकार पत्थर -- को प्रायः धार्मिक महत्व का माना गया है। "
  "पर ये व्याख्याएँ मानती हैं कि बाद की परंपराएँ पहले की परंपराओं के समानांतर हैं: ऋग्वेद रुद्र का उल्लेख करता है, जो नाम बाद की परंपराओं में शिव के लिए प्रयुक्त हुआ, पर उन्हें पशुपति या योगी के रूप में नहीं बताता, इसलिए इतिहासकार ऐसी पहचानों को सावधानी से देखते हैं।",
  f"{TH1}, Chapter 1 (Bricks, Beads and Bones).",
  "l1-his-harappan-religion-reconstruction", craft="inference")

# ---------------------------------------------------------------- hard pairs (1)
P(AN, "hard", "Consider the following pairs of materials used by Harappan craftspersons and their descriptions:",
  "हड़प्पा के शिल्पकारों द्वारा प्रयुक्त सामग्रियों और उनके विवरणों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Faience : Ground sand or silica mixed with colour and gum, and then fired",
   "Steatite : A very soft stone, used for seals and beads",
   "Carnelian : A stone whose red colour was obtained by firing the yellowish raw material",
   "Chert : A soft clay used for making toys"],
  ["फ़ायंस (faience) : पिसी हुई रेत या सिलिका में रंग और गोंद मिलाकर, फिर पकाकर बनाई गई सामग्री",
   "सेलखड़ी (steatite) : एक बहुत नरम पत्थर, जिससे मुहरें और मनके बनते थे",
   "कार्नेलियन : एक पत्थर, जिसका लाल रंग पीले कच्चे पत्थर को पकाकर लाया जाता था",
   "चर्ट (chert) : खिलौने बनाने की एक नरम मिट्टी"],
  2,
  "Pairs 1, 2 and 3 are correctly matched. Bead-makers worked with carnelian, jasper, crystal, quartz and steatite as well as copper, bronze, gold, shell, faience and terracotta; carnelian nodules were chipped into rough shapes, flaked, and then ground, polished and drilled, and their red colour came from firing. "
  "Pair 4 is wrong: chert is a hard stone, from which the Harappans made their cubical weights; toys were made of terracotta.",
  "युग्म 1, 2 और 3 सही सुमेलित हैं। मनके बनाने वाले कार्नेलियन, जैस्पर, स्फटिक, क्वार्ट्ज़ और सेलखड़ी के साथ ताँबे, काँसे, सोने, सीप, फ़ायंस और पकी मिट्टी से काम करते थे; कार्नेलियन के टुकड़ों को पहले मोटे आकार में तोड़ा, फिर परतों में छीला, घिसा, चमकाया और छेदा जाता था, और उनका लाल रंग पकाने से आता था। "
  "युग्म 4 गलत है: चर्ट एक कठोर पत्थर है, जिससे हड़प्पावासी अपने घनाकार बाट बनाते थे; खिलौने पकी मिट्टी के बनते थे।",
  f"{TH1}, Chapter 1 (Bricks, Beads and Bones).",
  "l1-his-harappan-craft-materials-pairs", craft="precision")

write("his_l1_t2_b.sql")
