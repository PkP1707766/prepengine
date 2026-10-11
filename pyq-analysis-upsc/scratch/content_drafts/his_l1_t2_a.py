# -*- coding: utf-8 -*-
"""Level 1 · Test 2 (History, NCERT Foundation) -- part A: Ancient India, the easy rows and the medium MCQs
(16 of the 36 Ancient rows; upsc_l1_cell_targets.mjs 2):
  easy MCQ 3, easy statement 6, easy pairs 1, medium MCQ 6.
Level 1 tests what the NCERT history books teach -- how historians know (sources, methods, the limits of
evidence), the Harappan city and its crafts, early villages and towns, the Vedic and Buddhist traditions, and
the Themes in Indian History chapters -- in the UPSC formats. The Level-2 History rows are not repeated: no row
here turns on a fact a Level-2 row already tests (Chanhudaro's bead workshops, the Kalibangan field, Harappan
weights, the Vajji assembly, Magadha's rise, the Rajagriha capital, Inamgaon, the Great Bath, Fa-hien's
Chandalas, the councils, the Tipitaka's language)."""
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

# ---------------------------------------------------------------- easy MCQ (3)
M(AN, "easy", "A historian studies the shape of the letters on an undated copper-plate land grant and compares them with the letters of dated inscriptions, to judge when the grant was written. Which discipline is the historian mainly using?",
  "एक इतिहासकार किसी बिना तिथि वाले ताम्रपत्र भूमि-अनुदान के अक्षरों की बनावट का अध्ययन करता है और उनकी तुलना तिथि वाले अभिलेखों के अक्षरों से करता है, ताकि यह आँका जा सके कि अनुदान कब लिखा गया। इतिहासकार मुख्य रूप से किस विधा का उपयोग कर रहा है?",
  ["Palaeography", "Numismatics", "Iconography", "Stratigraphy"],
  ["पुरालिपिशास्त्र (palaeography)", "मुद्राशास्त्र (numismatics)", "प्रतिमाशास्त्र (iconography)", "स्तरविज्ञान (stratigraphy)"],
  0,
  "Palaeography is the study of old scripts and handwriting. Letter forms change over time, so their shape helps date a record that carries no date of its own -- and can expose a grant written later than it claims. "
  "Numismatics is the study of coins, iconography the study of images of deities and other figures, and stratigraphy the study of the layers of an archaeological site.",
  "पुरालिपिशास्त्र पुरानी लिपियों और लिखावट का अध्ययन है। अक्षरों की बनावट समय के साथ बदलती है, इसलिए उनका आकार किसी ऐसे अभिलेख की तिथि आँकने में मदद करता है जिस पर अपनी कोई तिथि न हो -- और ऐसे अनुदान को भी पकड़ सकता है जो अपने दावे से बाद में लिखा गया हो। "
  "मुद्राशास्त्र सिक्कों का, प्रतिमाशास्त्र देवताओं और अन्य आकृतियों की प्रतिमाओं का, और स्तरविज्ञान किसी पुरातात्विक स्थल की परतों का अध्ययन है।",
  f"{OP1}, Chapter 1 (What, Where, How and When?); {TH1}, Chapter 2 (Kings, Farmers and Towns).",
  "l1-his-palaeography-copper-plate", craft="application")

M(AN, "easy", "Which one of the following features of the Lower Town of Mohenjodaro suggests that the settlement was planned before its houses were built?",
  "मोहनजोदड़ो के निचले शहर की निम्नलिखित में से कौन-सी विशेषता बताती है कि बस्ती की योजना उसके घर बनने से पहले बना ली गई थी?",
  ["Streets with drains were laid out first, and houses were then built along them",
   "Every house had large windows opening onto the main street, to let in light and air",
   "The houses of the Lower Town were built of stone, unlike those of the Citadel",
   "Each house was built facing the Great Bath at the centre of the Lower Town"],
  ["पहले नालियों वाली सड़कें बिछाई गईं, और फिर उनके किनारे घर बनाए गए",
   "हर घर में रोशनी और हवा के लिए मुख्य सड़क की ओर खुलने वाली बड़ी खिड़कियाँ थीं",
   "निचले शहर के घर नगर-दुर्ग (Citadel) के घरों के विपरीत पत्थर से बने थे",
   "हर घर निचले शहर के केंद्र में स्थित विशाल स्नानागार की ओर मुँह करके बनाया गया था"],
  0,
  "Streets and lanes with covered drains seem to have been laid out first, and houses built along them -- a sign of planning, like the bricks of standard proportions and the platforms on which the settlement was raised. "
  "Harappan houses had no windows in the walls along the ground level, for privacy; both parts of the city were built of bricks, not stone; and the Great Bath stood in the Citadel, not in the Lower Town.",
  "ढकी हुई नालियों वाली सड़कें और गलियाँ पहले बिछाई गईं, और घर उनके किनारे बने -- यह योजना का संकेत है, जैसे मानक अनुपात वाली ईंटें और वे चबूतरे जिन पर बस्ती बसाई गई। "
  "हड़प्पा के घरों में भूतल की दीवारों में निजता के लिए खिड़कियाँ नहीं थीं; शहर के दोनों भाग ईंटों से बने थे, पत्थर से नहीं; और विशाल स्नानागार नगर-दुर्ग में था, निचले शहर में नहीं।",
  f"{TH1}, Chapter 1 (Bricks, Beads and Bones).",
  "l1-his-mohenjodaro-drains-first", craft="inference")

M(AN, "easy", "Archaeologists describe some Palaeolithic sites as 'factory sites'. What does the term indicate?",
  "पुरातत्वविद कुछ पुरापाषाण कालीन स्थलों को 'कारख़ाना स्थल' (factory sites) कहते हैं। यह शब्द क्या बताता है?",
  ["Stone tools were made there, close to sources of good-quality stone",
   "Pottery was produced there in large kilns for trade with distant villages",
   "Metal tools were cast there from copper brought from distant mines",
   "Grain from nearby fields was stored there in large common granaries"],
  ["वहाँ अच्छे पत्थर के स्रोतों के पास पत्थर के औज़ार बनाए जाते थे",
   "वहाँ दूर के गाँवों से व्यापार के लिए बड़े भट्ठों में मिट्टी के बर्तन बनते थे",
   "वहाँ दूर की खानों से लाए गए ताँबे से धातु के औज़ार ढाले जाते थे",
   "वहाँ आसपास के खेतों का अनाज बड़े साझा अन्नागारों में रखा जाता था"],
  0,
  "Where good stone was found, people made tools on the spot; the blocks, chips and discarded tools left behind mark such factory sites, and some, like Hunsgi in Karnataka, were also habitation sites. "
  "Palaeolithic people had no pottery, no metal and no farming: pots, copper tools and granaries all belong to much later times.",
  "जहाँ अच्छा पत्थर मिलता था, लोग वहीं औज़ार बनाते थे; पीछे छूटे पत्थर के टुकड़े, छिलपे और फेंके गए औज़ार ऐसे कारख़ाना स्थलों की पहचान हैं, और कर्नाटक के हुँसगी जैसे कुछ स्थल रहने के स्थान भी थे। "
  "पुरापाषाण काल के लोगों के पास न मिट्टी के बर्तन थे, न धातु, न खेती: बर्तन, ताँबे के औज़ार और अन्नागार सब बहुत बाद के समय के हैं।",
  f"{OP1}, Chapter 2 (On the Trail of the Earliest People).",
  "l1-his-palaeolithic-factory-sites", craft="inference")

# ---------------------------------------------------------------- easy statement (6)
S(AN, "easy", "Consider the following statements about the earliest people of the subcontinent:",
  "उपमहाद्वीप के सबसे प्रारंभिक लोगों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Traces of ash found in the Kurnool caves suggest that the people living there knew the use of fire.",
   "Microliths, tiny stone tools fixed onto handles of bone or wood, are characteristic of the Palaeolithic period."],
  ["कुरनूल की गुफाओं में मिले राख के अवशेष बताते हैं कि वहाँ रहने वाले लोग आग का उपयोग जानते थे।",
   "हड्डी या लकड़ी के हत्थों में लगाए जाने वाले छोटे पत्थर के औज़ार, माइक्रोलिथ, पुरापाषाण काल की विशेषता हैं।"],
  T2, 0,
  "Only statement 1 is correct. Ash in the Kurnool caves (Andhra Pradesh) shows that fire was used -- for light, for cooking meat and to keep away animals. "
  "Statement 2 is wrong: microliths are the typical tools of the Mesolithic or Middle Stone Age, about 12,000 to 10,000 years ago; the Palaeolithic, the long period before it, is known for larger tools such as hand-axes and choppers.",
  "केवल कथन 1 सही है। कुरनूल (आंध्र प्रदेश) की गुफाओं की राख बताती है कि आग का उपयोग होता था -- रोशनी के लिए, मांस पकाने के लिए और जानवरों को दूर रखने के लिए। "
  "कथन 2 गलत है: माइक्रोलिथ मध्यपाषाण काल के, लगभग 12,000 से 10,000 वर्ष पहले के, विशिष्ट औज़ार हैं; उससे पहले का लंबा पुरापाषाण काल हाथ की कुल्हाड़ी और गँडासे जैसे बड़े औज़ारों के लिए जाना जाता है।",
  f"{OP1}, Chapter 2 (On the Trail of the Earliest People).",
  "l1-his-kurnool-fire-microliths", craft="precision")

S(AN, "easy", "Consider the following statements about the megalithic burials of the Deccan and south India:",
  "दक्कन और दक्षिण भारत की महापाषाण (megalithic) समाधियों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["At Brahmagiri, one skeleton was buried with 33 gold beads, while others had only a few pots -- which suggests that some people had a higher status than others.",
   "Some megaliths had a port-hole through which later members of the same family could be buried in the same place."],
  ["ब्रह्मगिरि में एक कंकाल के साथ सोने के 33 मनके दफ़नाए गए थे, जबकि अन्य के साथ केवल कुछ बर्तन थे -- जिससे लगता है कि कुछ लोगों की हैसियत दूसरों से ऊँची थी।",
   "कुछ महापाषाणों में एक छेद (port-hole) होता था, जिससे उसी परिवार के बाद के सदस्यों को उसी स्थान पर दफ़नाया जा सकता था।"],
  T2, 2,
  "Both statements are correct. Grave goods let archaeologists infer differences in status: at Brahmagiri (Karnataka) one burial held 33 gold beads, two stone beads, four copper bangles and a conch shell, while others had only a few pots. "
  "Megaliths, burials marked by big stones, sometimes held several skeletons of one family buried at different times; the bodies of those who died later were brought in through the port-hole.",
  "दोनों कथन सही हैं। समाधि में रखी वस्तुओं से पुरातत्वविद हैसियत के अंतर का अनुमान लगाते हैं: ब्रह्मगिरि (कर्नाटक) में एक समाधि में सोने के 33 मनके, पत्थर के दो मनके, ताँबे की चार चूड़ियाँ और एक शंख मिले, जबकि अन्य में केवल कुछ बर्तन थे। "
  "बड़े पत्थरों से चिह्नित समाधियों, महापाषाणों, में कभी-कभी एक ही परिवार के कई कंकाल होते थे, जिन्हें अलग-अलग समय पर दफ़नाया गया; बाद में मरने वालों के शव उस छेद से भीतर लाए जाते थे।",
  f"{OP1}, Chapter 5 (What Books and Burials Tell Us).",
  "l1-his-brahmagiri-megalith-status", craft="inference")

S(AN, "easy", "Consider the following statements about the Rigveda:",
  "ऋग्वेद के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Its hymns were recited and heard rather than read, and they were written down several centuries after they were composed.",
   "It was first printed less than two hundred years ago.",
   "Its hymns were composed in Prakrit."],
  ["इसके सूक्त पढ़े जाने के बजाय बोले और सुने जाते थे, और उनकी रचना के कई सदियों बाद उन्हें लिखा गया।",
   "यह पहली बार दो सौ वर्ष से भी कम समय पहले छपा।",
   "इसके सूक्त प्राकृत में रचे गए थे।"],
  C3, 1,
  "Statements 1 and 2 are correct. The Rigveda, composed about 3,500 years ago, was passed on orally and learnt by heart; it was written down only several centuries later and printed less than two hundred years ago. "
  "Statement 3 is wrong: its more than a thousand hymns, the suktas, are in Vedic or old Sanskrit, which differs from the Sanskrit learnt today; Prakrits were the languages of ordinary people in later times.",
  "कथन 1 और 2 सही हैं। लगभग 3,500 वर्ष पहले रचा गया ऋग्वेद मौखिक रूप से आगे बढ़ाया गया और कंठस्थ किया गया; इसे कई सदियों बाद लिखा गया और दो सौ वर्ष से भी कम समय पहले छापा गया। "
  "कथन 3 गलत है: इसके एक हज़ार से अधिक सूक्त वैदिक या पुरानी संस्कृत में हैं, जो आज सीखी जाने वाली संस्कृत से भिन्न है; प्राकृत बाद के समय में सामान्य लोगों की भाषाएँ थीं।",
  f"{OP1}, Chapter 5 (What Books and Burials Tell Us).",
  "l1-his-rigveda-oral-transmission", craft="precision")

S(AN, "easy", "Consider the following statements about the towns of the Ganga valley that grew up about 2,500 years ago:",
  "लगभग 2,500 वर्ष पहले विकसित हुए गंगा घाटी के नगरों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Ring wells found in many of these towns were probably used as toilets, drains or garbage dumps.",
   "Iron tools such as axes and ploughshares helped clear forests and raise farm output.",
   "Some towns, such as Mathura, were centres of both trade and religious activity."],
  ["इनमें से कई नगरों में मिले वलय कूप (ring wells) संभवतः शौचालय, नाली या कूड़ेदान के रूप में प्रयुक्त होते थे।",
   "कुल्हाड़ी और हल के फाल जैसे लोहे के औज़ारों ने जंगल साफ़ करने और खेती की उपज बढ़ाने में मदद की।",
   "मथुरा जैसे कुछ नगर व्यापार और धार्मिक गतिविधि, दोनों के केंद्र थे।"],
  C3, 2,
  "All three statements are correct. Rows of pots or ceramic rings placed one on top of the other -- ring wells -- seem to have served as toilets, drains and garbage dumps, usually in individual houses. "
  "Iron came into use about 3,000 years ago, and iron axes and ploughshares helped clear land and grow more, which fed the towns. "
  "Mathura stood where routes of travel and trade met; it was the second capital of the Kushanas, and had Buddhist monasteries, Jaina shrines and a centre of the worship of Krishna.",
  "तीनों कथन सही हैं। एक के ऊपर एक रखे बर्तनों या मिट्टी के छल्लों की पंक्तियाँ -- वलय कूप -- प्रायः अलग-अलग घरों में शौचालय, नाली और कूड़ेदान का काम करती थीं। "
  "लोहे का उपयोग लगभग 3,000 वर्ष पहले शुरू हुआ, और लोहे की कुल्हाड़ियों और फालों ने ज़मीन साफ़ करने और अधिक उपजाने में मदद की, जिससे नगरों का पेट भरा। "
  "मथुरा वहाँ बसा था जहाँ यात्रा और व्यापार के मार्ग मिलते थे; यह कुषाणों की दूसरी राजधानी था, और यहाँ बौद्ध विहार, जैन मंदिर और कृष्ण की उपासना का केंद्र था।",
  f"{OP1}, Chapter 9 (Vital Villages, Thriving Towns).",
  "l1-his-ganga-towns-ring-wells-mathura", craft="linkage")

S(AN, "easy", "Consider the following statements about the Silk Route:",
  "रेशम मार्ग (Silk Route) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It got its name because silk from China was carried along it to lands in the west.",
   "The technique of making silk was first invented in the Roman empire and later spread to China."],
  ["इसका यह नाम इसलिए पड़ा कि चीन का रेशम इसी के रास्ते पश्चिम के देशों तक ले जाया जाता था।",
   "रेशम बनाने की तकनीक पहले रोमन साम्राज्य में खोजी गई और बाद में चीन पहुँची।"],
  T2, 0,
  "Only statement 1 is correct. Silk was a prized cloth in Rome, and the routes along which it travelled overland from China across Central Asia came to be called the Silk Route; some kings tried to control large stretches of it so as to tax the traders. "
  "Statement 2 is wrong: making silk -- drawing thread from the cocoons of silkworms and weaving it -- was invented in China around 7,000 years ago, and the Chinese kept the method a secret for a long time.",
  "केवल कथन 1 सही है। रोम में रेशम बहुमूल्य वस्त्र था, और चीन से मध्य एशिया होकर जिन स्थल-मार्गों से यह जाता था, वे रेशम मार्ग कहलाए; कुछ राजाओं ने व्यापारियों पर कर लगाने के लिए इसके बड़े हिस्सों पर नियंत्रण की कोशिश की। "
  "कथन 2 गलत है: रेशम बनाना -- रेशम के कीड़ों के कोकून से धागा निकालकर बुनना -- लगभग 7,000 वर्ष पहले चीन में खोजा गया, और चीनियों ने यह विधि लंबे समय तक गुप्त रखी।",
  f"{OP1}, Chapter 10 (Traders, Kings and Pilgrims).",
  "l1-his-silk-route-origin", craft="recall")

S(AN, "easy", "Consider the following statements about the Buddhist sangha:",
  "बौद्ध संघ के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["A slave who wished to join the sangha needed his master's permission.",
   "Monks were not allowed to beg for food, and lived only on what they grew themselves.",
   "Monks and nuns lived in viharas, often built on land given by rich merchants, landowners or kings."],
  ["संघ में शामिल होने के इच्छुक दास को अपने स्वामी की अनुमति लेनी पड़ती थी।",
   "भिक्षुओं को भोजन की भिक्षा माँगने की अनुमति नहीं थी, और वे केवल अपने उगाए अन्न पर जीते थे।",
   "भिक्षु और भिक्षुणियाँ विहारों में रहते थे, जो प्रायः धनी व्यापारियों, भूस्वामियों या राजाओं की दी हुई भूमि पर बने होते थे।"],
  C3, 1,
  "Statements 1 and 3 are correct. The rules of the sangha required children to take their parents' permission, slaves their masters', those in the king's service the king's, and debtors their creditors'. "
  "Statement 2 is wrong: monks and nuns lived simple lives and went to the towns and villages to beg for food -- which is why they were called bhikkhus and bhikkhunis. "
  "Their viharas, at first of wood and later of brick, stood on land donated by merchants, landowners or kings; some were cut into hillsides, especially in western India.",
  "कथन 1 और 3 सही हैं। संघ के नियमों के अनुसार बच्चों को माता-पिता की, दासों को स्वामियों की, राजा की सेवा करने वालों को राजा की और कर्ज़दारों को लेनदारों की अनुमति लेनी होती थी। "
  "कथन 2 गलत है: भिक्षु और भिक्षुणियाँ सादा जीवन जीते थे और भोजन की भिक्षा माँगने नगरों और गाँवों में जाते थे -- इसीलिए वे भिक्खु और भिक्खुनी कहलाए। "
  "उनके विहार, पहले लकड़ी के और बाद में ईंट के, व्यापारियों, भूस्वामियों या राजाओं की दान की हुई भूमि पर बने थे; कुछ, विशेषकर पश्चिमी भारत में, पहाड़ियों को काटकर बनाए गए।",
  f"{OP1}, Chapter 7 (New Questions and Ideas).",
  "l1-his-sangha-rules-viharas", craft="precision")

# ---------------------------------------------------------------- easy pairs (1)
P(AN, "easy", "Consider the following pairs of terms used by historians and their meanings:",
  "इतिहासकारों द्वारा प्रयुक्त शब्दों और उनके अर्थों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Manuscript : A book written by hand, often on palm leaf or on the bark of the birch tree",
   "Inscription : Writing on a relatively hard surface such as stone or metal",
   "Archaeologist : One who studies the remains of buildings, tools, pots, weapons and bones",
   "Epigraphist : One who studies the remains of plants and animals"],
  ["पांडुलिपि : हाथ से लिखी पुस्तक, प्रायः ताड़ के पत्ते या भोजपत्र पर",
   "अभिलेख : पत्थर या धातु जैसी अपेक्षाकृत कठोर सतह पर लिखा गया लेख",
   "पुरातत्वविद : इमारतों, औज़ारों, बर्तनों, हथियारों और हड्डियों के अवशेषों का अध्ययन करने वाला",
   "अभिलेखशास्त्री : पौधों और जानवरों के अवशेषों का अध्ययन करने वाला"],
  2,
  "Pairs 1, 2 and 3 are correctly matched. Manuscripts were usually written on palm leaf or on the specially prepared bark of the birch tree; inscriptions were written on hard surfaces so that they would last. "
  "Pair 4 is wrong: an epigraphist studies inscriptions; ancient plant remains are studied by palaeobotanists and animal bones by zooarchaeologists, whose work helps reconstruct what people ate.",
  "युग्म 1, 2 और 3 सही सुमेलित हैं। पांडुलिपियाँ प्रायः ताड़ के पत्तों या विशेष रूप से तैयार भोजपत्र पर लिखी जाती थीं; अभिलेख कठोर सतहों पर लिखे जाते थे ताकि वे टिके रहें। "
  "युग्म 4 गलत है: अभिलेखशास्त्री अभिलेखों का अध्ययन करता है; प्राचीन पौधों के अवशेषों का अध्ययन पुरावनस्पतिविद और जानवरों की हड्डियों का अध्ययन पुराप्राणिविद करते हैं, जिनका काम यह जानने में मदद करता है कि लोग क्या खाते थे।",
  f"{OP1}, Chapter 1 (What, Where, How and When?); {TH1}, Chapter 1.",
  "l1-his-sources-terms-pairs", craft="precision")

# ---------------------------------------------------------------- medium MCQ (6)
M(AN, "medium", "The critical edition of the Mahabharata, prepared by comparing manuscripts of the epic collected from across the subcontinent, was a project of which institution?",
  "पूरे उपमहाद्वीप से एकत्र महाभारत की पांडुलिपियों की तुलना करके तैयार किया गया इसका समालोचनात्मक संस्करण (critical edition) किस संस्था की परियोजना थी?",
  ["The Bhandarkar Oriental Research Institute, Pune",
   "The Asiatic Society, Kolkata",
   "The Archaeological Survey of India, headquartered in New Delhi",
   "The National Library of India, Kolkata"],
  ["भंडारकर ओरिएंटल रिसर्च इंस्टिट्यूट, पुणे",
   "एशियाटिक सोसाइटी, कोलकाता",
   "नई दिल्ली में मुख्यालय वाला भारतीय पुरातत्व सर्वेक्षण",
   "भारत का राष्ट्रीय पुस्तकालय, कोलकाता"],
  0,
  "The project began in 1919 under the Sanskritist V.S. Sukthankar at the Bhandarkar Oriental Research Institute, Pune, and took 47 years. "
  "Scholars compared Sanskrit manuscripts from all over the subcontinent, chose the verses common to most of them and recorded the variations in footnotes -- revealing both a remarkable unity and many regional variations in how the epic was transmitted.",
  "यह परियोजना 1919 में संस्कृतविद वी.एस. सुकथनकर के नेतृत्व में भंडारकर ओरिएंटल रिसर्च इंस्टिट्यूट, पुणे में शुरू हुई और इसमें 47 वर्ष लगे। "
  "विद्वानों ने पूरे उपमहाद्वीप की संस्कृत पांडुलिपियों की तुलना की, अधिकांश में समान श्लोकों को चुना और भिन्नताओं को पादटिप्पणियों में दर्ज किया -- जिससे महाकाव्य के संचरण में उल्लेखनीय एकता और अनेक क्षेत्रीय भिन्नताएँ, दोनों सामने आईं।",
  f"{TH1}, Chapter 3 (Kinship, Caste and Class).",
  "l1-his-mahabharata-critical-edition", craft="precision")

M(AN, "medium", "Which one of the following best describes how historians now see the extent of Mauryan control over the empire?",
  "निम्नलिखित में से कौन-सा कथन सबसे अच्छी तरह बताता है कि इतिहासकार अब साम्राज्य पर मौर्य नियंत्रण की सीमा को कैसे देखते हैं?",
  ["Control was strongest around the capital and provincial centres, and looser in forests and distant areas",
   "Every region was governed directly from Pataliputra in exactly the same way, through a uniform administration",
   "The empire was a loose league of independent kingdoms that only sent gifts to the Mauryan court",
   "Mauryan rule reached only the area around Pataliputra, as no Mauryan inscription has been found elsewhere"],
  ["नियंत्रण राजधानी और प्रांतीय केंद्रों के आसपास सबसे सशक्त था, और वनों तथा दूर के क्षेत्रों में ढीला था",
   "हर क्षेत्र का शासन एक समान प्रशासन के माध्यम से ठीक एक ही तरह पाटलिपुत्र से सीधे चलता था",
   "साम्राज्य स्वतंत्र राज्यों का एक ढीला संघ था, जो मौर्य दरबार को केवल उपहार भेजते थे",
   "मौर्य शासन केवल पाटलिपुत्र के आसपास तक था, क्योंकि कहीं और कोई मौर्य अभिलेख नहीं मिला है"],
  0,
  "Historians now think the empire was not administered uniformly: the regions were too diverse, from the hills of the north-west to the coast of Odisha. "
  "Control was probably strongest around the capital and the provincial centres named in Ashoka's inscriptions; forest peoples and distant regions were probably tapped mainly for resources such as timber and elephants. "
  "Ashokan inscriptions have been found from the north-west frontier to Andhra Pradesh and Karnataka, so Mauryan rule was neither confined to Magadha nor a mere league.",
  "इतिहासकार अब मानते हैं कि साम्राज्य का प्रशासन एक समान नहीं था: उत्तर-पश्चिम की पहाड़ियों से ओडिशा के तट तक के क्षेत्र बहुत विविध थे। "
  "नियंत्रण संभवतः राजधानी और अशोक के अभिलेखों में वर्णित प्रांतीय केंद्रों के आसपास सबसे सशक्त था; वनवासी लोगों और दूर के क्षेत्रों से संभवतः मुख्य रूप से लकड़ी और हाथी जैसे संसाधन लिए जाते थे। "
  "अशोक के अभिलेख उत्तर-पश्चिमी सीमा से आंध्र प्रदेश और कर्नाटक तक मिले हैं, इसलिए मौर्य शासन न तो मगध तक सीमित था, न ही केवल एक संघ था।",
  f"{TH1}, Chapter 2 (Kings, Farmers and Towns).",
  "l1-his-mauryan-control-uneven", craft="inference")

M(AN, "medium", "Prabhavati Gupta, daughter of the Gupta king Chandragupta II and queen of the Vakataka kingdom, made a grant of land that is recorded in an inscription. Why do historians find this record significant?",
  "गुप्त राजा चंद्रगुप्त द्वितीय की पुत्री और वाकाटक राज्य की रानी प्रभावती गुप्त ने भूमि का एक अनुदान दिया, जो एक अभिलेख में दर्ज है। इतिहासकार इस अभिलेख को महत्वपूर्ण क्यों मानते हैं?",
  ["It shows a royal woman granting land in her own right, though the texts did not expect women to hold land",
   "It is the earliest inscription found anywhere in the subcontinent that uses the Brahmi script for its text",
   "It proves that the Vakataka kingdom had already been annexed and was now ruled directly by the Gupta emperors",
   "It records the first-ever grant of land made to a Buddhist monastery by any ruler in India"],
  ["यह एक राजपरिवार की महिला को अपने अधिकार से भूमि दान करते दिखाता है, यद्यपि ग्रंथ महिलाओं से भूमि रखने की अपेक्षा नहीं करते थे",
   "यह उपमहाद्वीप में कहीं भी मिला सबसे पुराना अभिलेख है जिसके पाठ में ब्राह्मी लिपि प्रयुक्त है",
   "यह सिद्ध करता है कि वाकाटक राज्य का विलय हो चुका था और अब उस पर गुप्त सम्राट सीधे शासन करते थे",
   "यह भारत में किसी भी शासक द्वारा किसी बौद्ध विहार को दिए गए भूमि के पहले अनुदान को दर्ज करता है"],
  0,
  "According to the Dharmashastras, women were not supposed to have independent access to resources such as land; yet the grant shows that Prabhavati Gupta, who ruled the Vakataka kingdom as regent, had land and gave it away. "
  "Her case was probably exceptional because she was a queen -- a reminder that the normative texts do not always describe what actually happened. "
  "Brahmi inscriptions go back to Ashoka, the Vakatakas remained a separate kingdom allied to the Guptas by marriage, and grants to Buddhist monasteries are centuries older.",
  "धर्मशास्त्रों के अनुसार महिलाओं की भूमि जैसे संसाधनों तक स्वतंत्र पहुँच नहीं होनी चाहिए थी; फिर भी यह अनुदान दिखाता है कि वाकाटक राज्य पर संरक्षिका (regent) के रूप में शासन करने वाली प्रभावती गुप्त के पास भूमि थी और उन्होंने उसे दान किया। "
  "उनका मामला संभवतः असाधारण था क्योंकि वे रानी थीं -- यह याद दिलाता है कि मानक ग्रंथ हमेशा वह नहीं बताते जो वास्तव में होता था। "
  "ब्राह्मी अभिलेख अशोक तक जाते हैं, वाकाटक विवाह-संबंध से गुप्तों के सहयोगी एक अलग राज्य बने रहे, और बौद्ध विहारों को अनुदान सदियों पुराने हैं।",
  f"{TH1}, Chapter 2 (Kings, Farmers and Towns).",
  "l1-his-prabhavati-gupta-land-grant", craft="inference")

M(AN, "medium", "The Great Stupa at Sanchi survived in good condition while many other early stupas were destroyed. Which one of the following helped to preserve it?",
  "साँची का महान स्तूप अच्छी दशा में बचा रहा, जबकि कई अन्य प्रारंभिक स्तूप नष्ट हो गए। निम्नलिखित में से किसने इसे संरक्षित रखने में मदद की?",
  ["Funds from the Begums of Bhopal, Shahjehan Begum and Sultan Jehan Begum",
   "Its eastern gateway was taken to a museum in Paris, where it was kept safe",
   "It lay buried under the sand of the Thar desert until the twentieth century",
   "The Mughal emperors rebuilt it in red sandstone during the seventeenth century"],
  ["भोपाल की बेगमों, शाहजहाँ बेगम और सुल्तान जहाँ बेगम, से मिली धनराशि",
   "इसका पूर्वी तोरणद्वार पेरिस के एक संग्रहालय ले जाया गया, जहाँ वह सुरक्षित रहा",
   "यह बीसवीं सदी तक थार मरुस्थल की रेत के नीचे दबा रहा",
   "मुग़ल सम्राटों ने सत्रहवीं सदी में इसे लाल बलुआ पत्थर में फिर से बनवाया"],
  0,
  "The rulers of Bhopal, Shahjehan Begum and her successor Sultan Jehan Begum, gave money for its preservation; Sultan Jehan Begum also funded a museum and a guest house there, and John Marshall dedicated his volumes on Sanchi to her. "
  "The French sought permission to take the eastern gateway to France, and the English also wanted it, but both were content with plaster-cast copies, so the original stayed in place. Amaravati, by contrast, was dismantled and its sculptures carried away.",
  "भोपाल की शासिकाओं, शाहजहाँ बेगम और उनकी उत्तराधिकारी सुल्तान जहाँ बेगम, ने इसके संरक्षण के लिए धन दिया; सुल्तान जहाँ बेगम ने वहाँ एक संग्रहालय और अतिथिशाला के लिए भी धन दिया, और जॉन मार्शल ने साँची पर अपने ग्रंथ उन्हें समर्पित किए। "
  "फ़्रांसीसियों ने पूर्वी तोरणद्वार फ़्रांस ले जाने की अनुमति माँगी थी, और अंग्रेज़ भी उसे चाहते थे, पर दोनों प्लास्टर की प्रतिकृतियों से संतुष्ट हो गए, इसलिए मूल अपनी जगह रहा। इसके विपरीत अमरावती को तोड़ दिया गया और उसकी मूर्तियाँ ले जाई गईं।",
  f"{TH1}, Chapter 4 (Thinkers, Beliefs and Buildings).",
  "l1-his-sanchi-begums-preservation", craft="precision")

M(AN, "medium", "In early Buddhist texts, the term 'gahapati' usually refers to",
  "प्रारंभिक बौद्ध ग्रंथों में 'गहपति' शब्द प्रायः किसके लिए प्रयुक्त होता है?",
  ["the owner, master or head of a household",
   "a monk who has given up household life",
   "a royal official who collected the king's share",
   "a priest who performed sacrifices for kings"],
  ["किसी घर का स्वामी, मालिक या मुखिया",
   "वह भिक्षु जिसने गृहस्थ जीवन त्याग दिया हो",
   "राजा का हिस्सा वसूलने वाला राजकीय अधिकारी",
   "राजाओं के लिए यज्ञ करने वाला पुरोहित"],
  0,
  "A gahapati was the owner, master or head of a household, who exercised control over the women, children, slaves and workers who shared the residence, and over its resources -- land, animals and other things. "
  "The term was also used for the urban elite, including wealthy merchants.",
  "गहपति किसी घर का स्वामी, मालिक या मुखिया होता था, जो घर में रहने वाली महिलाओं, बच्चों, दासों और कामगारों पर, और उसके संसाधनों -- भूमि, पशु और अन्य वस्तुओं -- पर नियंत्रण रखता था। "
  "यह शब्द धनी व्यापारियों सहित नगरों के अभिजात वर्ग के लिए भी प्रयुक्त होता था।",
  f"{TH1}, Chapters 2 and 3.",
  "l1-his-gahapati-meaning", craft="precision")

M(AN, "medium", "Which one of the following made the Puranas, compiled from about the middle of the first millennium CE, different from the Vedic texts?",
  "निम्नलिखित में से किस बात ने पहली सहस्राब्दी ईस्वी के मध्य से संकलित पुराणों को वैदिक ग्रंथों से भिन्न बनाया?",
  ["They were in simple Sanskrit verse, meant to be heard by all, including women and shudras",
   "They were composed in Pali and preserved only in Buddhist monasteries",
   "They dealt only with rituals for the sacrificial fire, not with stories of gods",
   "They could be learnt only by brahmana men who had been formally initiated by a Vedic teacher"],
  ["वे सरल संस्कृत पद्य में थे, जिन्हें महिलाओं और शूद्रों सहित सब सुन सकते थे",
   "वे पालि में रचे गए थे और केवल बौद्ध विहारों में सुरक्षित रखे गए",
   "उनमें केवल यज्ञ की अग्नि के अनुष्ठान थे, देवताओं की कथाएँ नहीं",
   "उन्हें केवल वे ब्राह्मण पुरुष सीख सकते थे जिन्हें किसी वैदिक गुरु ने विधिवत दीक्षा दी हो"],
  0,
  "The Puranas contain stories about gods and goddesses such as Vishnu, Shiva, Durga or Parvati, with details on how they were to be worshipped, and accounts of the creation of the world and of kings. "
  "They were written in simple Sanskrit verse and meant to be heard by everybody -- including women and shudras, who were not allowed to study the Vedas -- and were often recited by priests in temples.",
  "पुराणों में विष्णु, शिव, दुर्गा या पार्वती जैसे देवी-देवताओं की कथाएँ, उनकी उपासना की विधियाँ, और संसार की सृष्टि तथा राजाओं के वृत्तांत हैं। "
  "वे सरल संस्कृत पद्य में लिखे गए और सबके सुनने के लिए थे -- महिलाओं और शूद्रों के लिए भी, जिन्हें वेद पढ़ने की अनुमति नहीं थी -- और प्रायः मंदिरों में पुरोहित उनका पाठ करते थे।",
  f"{OP1}, Chapter 12 (Buildings, Paintings and Books); {TH1}, Chapter 4.",
  "l1-his-puranas-audience", craft="inference")

write("his_l1_t2_a.sql")
