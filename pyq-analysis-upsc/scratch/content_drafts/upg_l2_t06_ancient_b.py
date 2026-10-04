# -*- coding: utf-8 -*-
"""Level 2 · Test 6 (History 2: Ancient India) -- depth audit of 2026-10-04, part B: statement rows and the
tags for the kept rows (part A, upg_l2_t06_ancient_a.py, has the pairs and MCQs).

36 statement rows that asked a date, a place or an author are rewritten in place with the same concept id,
type and difficulty. They now ask what a find or a text shows, why something happened, or a four- or
five-item judgement: Harappan sites in present-day India, structural Gupta temples, astronomical works,
Neolithic sites, Pulakeshin II's rivals.
With part A: before, analytic 2, precision 24, recall 80; after, analytic 52, precision 24, recall 30.
The other 50 rows keep their content and get their craft tag here.
Leaks avoided while drafting:
  - Lumbini as the birth site (answers the Rummindei statement of the Dhamma row) and Jetavana (answers
    the Isipatana MCQ), so the Buddha's-life row asks about his clan and patrons instead;
  - 'Sandrocottus' (answers the Bindusara MCQ);
  - Bhadrabahu by name (answers the texts-and-religions pairs row);
  - the language of Ashoka's edicts and Pali for the canon (answer the Arthashastra and Tripitaka rows);
  - the debasement of Gupta coins and the Mehrauli pillar (duplicate the coinage and Mehrauli rows);
  - Jyotisha as the example of a Vedanga (answers the Vedanga MCQ)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write_updates, CODE
from polity_common import C3, C4, T2

d.SUBJECT = "History"
d.REQUIRE_CRAFT = True
ANC = "Ancient"
RS = "R.S. Sharma, India's Ancient Past (Oxford University Press)"
US = "Upinder Singh, A History of Ancient and Early Medieval India (Pearson)"
NCM = "NCERT Class XII, Themes in Indian History"
NC6 = "NCERT Class VI, Our Pasts I"
FIVE = ["Only two", "Only three", "Only four", "All five"]
FIVE_HI = ["केवल दो", "केवल तीन", "केवल चार", "सभी पाँच"]

# ---------------------------------------------------------------- easy (13)
S(ANC, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Alexander's invasion came while the Nandas ruled Magadha, and Chandragupta Maurya rose soon after, partly by driving out the Greek garrisons of the north-west.",
   "The invasion left a Greek kingdom in the Punjab that lasted into the reign of Ashoka."],
  ["सिकंदर का आक्रमण तब हुआ जब मगध पर नंदों का शासन था, और चंद्रगुप्त मौर्य उसके तुरंत बाद उभरे, आंशिक रूप से उत्तर-पश्चिम की यूनानी चौकियों को खदेड़कर।",
   "आक्रमण ने पंजाब में एक यूनानी राज्य छोड़ा जो अशोक के शासन तक बना रहा।"],
  T2, 0,
  "Only statement 1 is correct. Alexander crossed into the Punjab in 326 BCE, defeated Porus at the Hydaspes (Jhelum), and turned back at the Beas when his army refused to go on, so he never reached the Nanda heartland. "
  "Statement 2 is wrong: the garrisons he left soon collapsed, and within a few years Chandragupta held the north-west; after his war with Seleucus he also gained lands beyond the Indus. Greek rule in the north-west came back only with the Indo-Greeks, after the Mauryas.",
  "केवल कथन 1 सही है। सिकंदर 326 ई.पू. में पंजाब में घुसा, हाइडेस्पीज़ (झेलम) पर पोरस को हराया, और ब्यास पर सेना के आगे बढ़ने से मना करने पर लौट गया, इसलिए वह कभी नंदों के मुख्य क्षेत्र तक नहीं पहुँचा। "
  "कथन 2 गलत है: उसकी छोड़ी चौकियाँ जल्द ढह गईं, और कुछ ही वर्षों में उत्तर-पश्चिम चंद्रगुप्त के पास था; सेल्यूकस से युद्ध के बाद उन्हें सिंधु के पार की भूमि भी मिली। उत्तर-पश्चिम में यूनानी शासन मौर्यों के बाद, हिंद-यवनों के साथ ही लौटा।",
  RS, "ancient-alexander-invasion", craft="linkage")

S(ANC, "easy", "Consider the following statements about the Bhimbetka rock shelters in Madhya Pradesh:",
  "मध्य प्रदेश के भीमबेटका शैलाश्रयों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Their paintings of animals, hunting and dancing span several periods, from the Mesolithic onwards.",
   "The paintings show that the people who made the earliest of them were settled farmers using iron ploughs."],
  ["जानवरों, शिकार और नृत्य के उनके चित्र मध्यपाषाण काल से आगे के कई कालों के हैं।",
   "चित्र दिखाते हैं कि उनमें से सबसे पुराने बनाने वाले लोग लोहे के हल चलाने वाले स्थायी किसान थे।"],
  T2, 0,
  "Only statement 1 is correct. The shelters in the Vindhyan hills south of Bhopal, found by V.S. Wakankar in 1957 and a World Heritage Site since 2003, were used from the Palaeolithic onwards; their paintings, layered over one another, show wild animals, hunts, dances and later riders and warriors. "
  "Statement 2 is wrong: the earliest paintings are the work of hunter-gatherers. Settled farming came much later, and iron later still, in about the first millennium BCE.",
  "केवल कथन 1 सही है। भोपाल के दक्षिण में विंध्य की पहाड़ियों में स्थित, 1957 में वी.एस. वाकणकर द्वारा खोजे गए और 2003 से विश्व धरोहर स्थल ये शैलाश्रय पुरापाषाण काल से उपयोग में थे; एक-दूसरे पर बने उनके चित्र जंगली जानवर, शिकार, नृत्य और बाद में घुड़सवार तथा योद्धा दिखाते हैं। "
  "कथन 2 गलत है: सबसे पुराने चित्र शिकारी-संग्राहकों का काम हैं। स्थायी खेती बहुत बाद में आई, और लोहा उससे भी बाद, लगभग पहली सहस्राब्दी ई.पू. में।",
  NC6, "ancient-bhimbetka", craft="inference")

S(ANC, "easy", "Consider the following statements about the life of the Buddha:",
  "बुद्ध के जीवन के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["He was born into the Shakya clan, a gana whose capital was Kapilavastu, so he grew up in a polity governed by an assembly rather than a king.",
   "His order admitted no women.",
   "He attained mahaparinirvana at Rajagriha, the capital of Magadha."],
  ["उनका जन्म शाक्य कुल में हुआ, जो एक गण था जिसकी राजधानी कपिलवस्तु थी, इसलिए वे राजा के बजाय सभा द्वारा शासित राज्य में बड़े हुए।",
   "उनके संघ में स्त्रियों को प्रवेश नहीं दिया गया।",
   "उन्होंने मगध की राजधानी राजगृह में महापरिनिर्वाण प्राप्त किया।"],
  C3, 0,
  "Only statement 1 is correct. The Shakyas were a gana-sangha, in which the heads of leading families met in an assembly, and the Buddha's order, the Sangha, drew on this practice of discussion and consensus. "
  "Statement 2 is wrong: at the request of Ananda, the Buddha admitted women, beginning with his foster-mother Mahapajapati Gotami, and an order of nuns (bhikkhunis) grew up; the Therigatha preserves their verses. Statement 3 is wrong: he died at Kushinagar, in the territory of the Mallas, another gana. Rajagriha was where the First Buddhist Council was held soon after.",
  "केवल कथन 1 सही है। शाक्य एक गण-संघ थे, जिसमें प्रमुख परिवारों के मुखिया सभा में मिलते थे, और बुद्ध के संघ ने चर्चा और सहमति की इसी परंपरा को अपनाया। "
  "कथन 2 गलत है: आनंद के आग्रह पर बुद्ध ने स्त्रियों को प्रवेश दिया, जिसकी शुरुआत उनकी विमाता महाप्रजापति गौतमी से हुई, और भिक्षुणियों का संघ बना; थेरीगाथा में उनकी गाथाएँ सुरक्षित हैं। कथन 3 गलत है: उनका देहांत एक अन्य गण, मल्लों के क्षेत्र में कुशीनगर में हुआ। राजगृह वह स्थान था जहाँ उसके तुरंत बाद पहली बौद्ध संगीति हुई।",
  NCM, "ancient-buddha-life-places", craft="linkage")

S(ANC, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The civilisation is often called 'Harappan' because Harappa was the first of its sites to be excavated.",
   "The discoveries of the 1920s pushed the beginnings of urban life in the subcontinent back to the third millennium BCE."],
  ["इस सभ्यता को प्रायः 'हड़प्पा' सभ्यता इसलिए कहा जाता है कि हड़प्पा उसका पहला खोदा गया स्थल था।",
   "1920 के दशक की खोजों ने उपमहाद्वीप में नगरीय जीवन की शुरुआत को तीसरी सहस्राब्दी ई.पू. तक पीछे पहुँचा दिया।"],
  T2, 2,
  "Both statements are correct. Daya Ram Sahni began digging at Harappa in 1921 and R.D. Banerji at Mohenjodaro in 1922; in 1924 John Marshall, the Director-General of the Archaeological Survey, announced a new civilisation. Archaeologists name a culture after the first site where it was found, hence 'Harappan'. "
  "Before this, Indian history was thought to begin with the Vedic age; the finds showed planned cities more than a thousand years older, contemporary with Mesopotamia.",
  "दोनों कथन सही हैं। दयाराम साहनी ने 1921 में हड़प्पा में और आर.डी. बनर्जी ने 1922 में मोहनजोदड़ो में खुदाई शुरू की; 1924 में भारतीय पुरातत्व सर्वेक्षण के महानिदेशक जॉन मार्शल ने एक नई सभ्यता की घोषणा की। पुरातत्वविद किसी संस्कृति का नाम उसके पहले खोजे गए स्थल पर रखते हैं, इसीलिए 'हड़प्पा'। "
  "इससे पहले भारतीय इतिहास वैदिक युग से शुरू माना जाता था; खोजों ने हज़ार वर्ष से अधिक पुराने नियोजित नगर दिखाए, जो मेसोपोटामिया के समकालीन थे।",
  NCM, "ancient-harappa-mohenjodaro-excavation", craft="linkage")

S(ANC, "easy", "Consider the following statements about the Great Bath at Mohenjodaro:",
  "मोहनजोदड़ो के विशाल स्नानागार के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Its careful waterproofing, its place in the citadel and the absence of signs that it was a palace have led most archaeologists to see it as a place of ritual bathing.",
   "It shows that the Harappans worshipped in large temples like those of Mesopotamia."],
  ["इसकी सावधानीपूर्ण जलरोधी बनावट, दुर्ग में इसका स्थान और इसके महल होने के संकेतों का अभाव अधिकांश पुरातत्वविदों को इसे अनुष्ठानिक स्नान का स्थान मानने की ओर ले जाते हैं।",
   "यह दिखाता है कि हड़प्पावासी मेसोपोटामिया जैसे बड़े मंदिरों में पूजा करते थे।"],
  T2, 0,
  "Only statement 1 is correct. The tank was lined with fine burnt bricks set in gypsum mortar, with a layer of bitumen behind them, had steps at both ends and rooms around it, and stood on the raised citadel; such effort for bathing suggests a ritual purpose, perhaps linked to purity. "
  "Statement 2 is wrong: no building in the Harappan cities has been securely identified as a temple, which is one of the ways they differ from the temple-centred cities of Mesopotamia.",
  "केवल कथन 1 सही है। कुंड जिप्सम के गारे में लगी पकी ईंटों से बना था, जिनके पीछे बिटुमेन की परत थी, उसके दोनों सिरों पर सीढ़ियाँ और चारों ओर कमरे थे, और वह ऊँचे दुर्ग पर था; स्नान के लिए इतना श्रम किसी अनुष्ठानिक उद्देश्य, संभवतः शुद्धता से जुड़े, का संकेत देता है। "
  "कथन 2 गलत है: हड़प्पा के नगरों में किसी भवन की पहचान निश्चित रूप से मंदिर के रूप में नहीं हुई है, और यह मेसोपोटामिया के मंदिर-केंद्रित नगरों से उनका एक अंतर है।",
  NCM, "ancient-indus-great-bath", craft="inference")

S(ANC, "easy", "Most Harappan seals carry a short inscription along with an animal motif, and sealings -- clay impressions made with seals -- have been found at many sites. Consider the following statements:",
  "अधिकांश हड़प्पा मुहरों पर किसी पशु-आकृति के साथ एक छोटा अभिलेख है, और कई स्थलों पर मुद्रांकन, यानी मुहरों से बनी मिट्टी की छापें, मिली हैं। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The seals were probably used to mark goods or packages sent in trade.",
   "Since the script has not been deciphered, what the inscriptions say is not known.",
   "The script was written from left to right, like Brahmi."],
  ["मुहरों का उपयोग संभवतः व्यापार में भेजे जाने वाले माल या गठरियों को चिह्नित करने के लिए होता था।",
   "चूँकि लिपि पढ़ी नहीं जा सकी है, इसलिए अभिलेखों में क्या लिखा है यह ज्ञात नहीं है।",
   "लिपि ब्राह्मी की तरह बाएँ से दाएँ लिखी जाती थी।"],
  C3, 1,
  "Statements 1 and 2 are correct. A sealing pressed onto clay over a knot or a jar stopper showed who sent the goods and that they had not been tampered with, which is why sealings turn up where goods were received. The inscriptions are short, usually five signs or so, and remain undeciphered despite many attempts. "
  "Statement 3 is wrong: the way signs are crowded at the left edge of some seals suggests the script was usually written from right to left.",
  "कथन 1 और 2 सही हैं। किसी गाँठ या घड़े के ढक्कन पर लगी मिट्टी पर दबाई गई छाप बताती थी कि माल किसने भेजा और उससे छेड़छाड़ नहीं हुई, इसीलिए मुद्रांकन वहाँ मिलते हैं जहाँ माल पहुँचा। अभिलेख छोटे हैं, प्रायः लगभग पाँच चिह्नों के, और कई प्रयासों के बावजूद पढ़े नहीं जा सके हैं। "
  "कथन 3 गलत है: कुछ मुहरों के बाएँ किनारे पर चिह्नों के सिकुड़ने के ढंग से लगता है कि लिपि प्रायः दाएँ से बाएँ लिखी जाती थी।",
  NCM, "ancient-indus-seals-script", craft="inference")

S(ANC, "easy", "Consider the following statements about Jainism:",
  "जैन धर्म के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Jains hold that liberation comes through right faith, right knowledge and right conduct practised together.",
   "Because they believe that even plants, water and tiny creatures have souls, Jains carry ahimsa further than most traditions.",
   "Mahavira is regarded as the founder of Jainism, with no teachers before him."],
  ["जैन मानते हैं कि मोक्ष सम्यक् दर्शन, सम्यक् ज्ञान और सम्यक् चरित्र के एक साथ पालन से मिलता है।",
   "चूँकि वे मानते हैं कि पौधों, जल और सूक्ष्म जीवों में भी आत्मा है, इसलिए जैन अहिंसा को अधिकांश परंपराओं से आगे ले जाते हैं।",
   "महावीर को जैन धर्म का संस्थापक माना जाता है, जिनसे पहले कोई उपदेशक नहीं था।"],
  C3, 1,
  "Statements 1 and 2 are correct. The 'three jewels' must go together for the soul to shed the karma that binds it. Since souls are held to exist in all things, Jain monks sweep the path and cover their mouths to avoid harming even the smallest beings, and lay Jains have avoided occupations such as farming that involve killing, which is one reason many took to trade. "
  "Statement 3 is wrong: Jains regard Mahavira as the twenty-fourth and last Tirthankara of this age, after Rishabhadeva and others; many historians accept that Parshvanatha, the twenty-third, was a historical figure.",
  "कथन 1 और 2 सही हैं। आत्मा को बाँधने वाले कर्म से मुक्त होने के लिए 'त्रिरत्न' साथ-साथ होने चाहिए। चूँकि हर वस्तु में आत्मा मानी जाती है, जैन भिक्षु सबसे छोटे जीवों को भी हानि से बचाने के लिए रास्ता बुहारते और मुँह ढकते हैं, और गृहस्थ जैनों ने खेती जैसे हिंसा वाले व्यवसायों से परहेज़ किया, जो एक कारण है कि कई व्यापार की ओर गए। "
  "कथन 3 गलत है: जैन महावीर को इस युग के चौबीसवें और अंतिम तीर्थंकर मानते हैं, जो ऋषभदेव और अन्य के बाद आए; कई इतिहासकार मानते हैं कि तेईसवें तीर्थंकर पार्श्वनाथ एक ऐतिहासिक व्यक्ति थे।",
  RS, "ancient-jain-triratna-tirthankaras", craft="linkage")

S(ANC, "easy", "Consider the following statements about megaliths in India:",
  "भारत में महापाषाणों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Since the dead were buried with pots, tools and weapons, the megalith-builders probably believed in some form of life after death.",
   "Megaliths are found only in south India."],
  ["चूँकि मृतकों को बर्तनों, औज़ारों और हथियारों के साथ दफ़नाया जाता था, इसलिए महापाषाण बनाने वाले संभवतः किसी प्रकार के परलोक में विश्वास करते थे।",
   "महापाषाण केवल दक्षिण भारत में मिलते हैं।"],
  T2, 0,
  "Only statement 1 is correct. Megaliths are burials marked by large stones -- stone circles, cists and dolmens -- and the grave goods, including black-and-red ware and iron implements, suggest a belief that the dead would need them; the varying amounts of goods also hint at differences in status. "
  "Statement 2 is wrong: though most are in the Deccan and the south, from about 1000 BCE, megaliths are also found in Vidarbha, in Kashmir at Burzahom, in Baluchistan, and in the north-east, where some communities still raise memorial stones.",
  "केवल कथन 1 सही है। महापाषाण बड़े पत्थरों से चिह्नित समाधियाँ हैं, जैसे पत्थरों के घेरे, कोष्ठ और डोलमेन, और काले-लाल मृद्भांड तथा लोहे के उपकरणों सहित समाधि-सामग्री इस विश्वास का संकेत देती है कि मृतक को इनकी ज़रूरत होगी; सामग्री की अलग-अलग मात्रा प्रतिष्ठा के अंतर का भी संकेत देती है। "
  "कथन 2 गलत है: यद्यपि अधिकांश दक्कन और दक्षिण में, लगभग 1000 ई.पू. से, हैं, महापाषाण विदर्भ, कश्मीर के बुर्ज़होम, बलूचिस्तान और पूर्वोत्तर में भी मिलते हैं, जहाँ कुछ समुदाय आज भी स्मारक-पत्थर खड़े करते हैं।",
  NCM, "ancient-megaliths-iron", craft="inference")

S(ANC, "easy", "Consider the following Neolithic sites:",
  "निम्नलिखित नवपाषाण स्थलों पर विचार कीजिए:",
  ["Mehrgarh", "Burzahom", "Chirand", "Koldihwa", "Daojali Hading"],
  ["मेहरगढ़", "बुर्ज़होम", "चिरांद", "कोल्डिहवा", "दाओजली हाडिंग"],
  None, 2,
  "Four of them are in present-day India. Burzahom in Kashmir is known for pit dwellings; Chirand in Saran district of Bihar for bone tools; Koldihwa in the Belan valley of Uttar Pradesh for some of the early evidence of rice; and Daojali Hading in Assam for Neolithic tools of the north-east. "
  "Mehrgarh, at the foot of the Bolan pass in Baluchistan, Pakistan, has some of the earliest evidence of farming in the subcontinent, from about 7000 BCE.",
  "इनमें से चार वर्तमान भारत में हैं। कश्मीर का बुर्ज़होम गड्ढे वाले आवासों के लिए, बिहार के सारण ज़िले का चिरांद हड्डी के औज़ारों के लिए, उत्तर प्रदेश की बेलन घाटी का कोल्डिहवा चावल के कुछ प्रारंभिक साक्ष्यों के लिए, और असम का दाओजली हाडिंग पूर्वोत्तर के नवपाषाण औज़ारों के लिए जाना जाता है। "
  "पाकिस्तान के बलूचिस्तान में बोलन दर्रे के नीचे स्थित मेहरगढ़ में लगभग 7000 ई.पू. से उपमहाद्वीप में खेती के कुछ सबसे प्रारंभिक साक्ष्य हैं।",
  RS, "ancient-neolithic-sites", opts=FIVE, opts_hi=FIVE_HI,
  closing="How many of the above are in present-day India?", closing_hi="उपर्युक्त में से कितने वर्तमान भारत में हैं?", craft="multi")

S(ANC, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Patanjali's Mahabhashya is a commentary on Panini's grammar, which shows that the Ashtadhyayi had become a classic within a few centuries.",
   "Panini's grammar was composed in the Gupta period."],
  ["पतंजलि का महाभाष्य पाणिनि के व्याकरण पर टीका है, जो दिखाता है कि अष्टाध्यायी कुछ ही सदियों में एक क्लासिक बन चुकी थी।",
   "पाणिनि का व्याकरण गुप्त काल में रचा गया।"],
  T2, 0,
  "Only statement 1 is correct. Panini, from Gandhara, set out the rules of Sanskrit in nearly 4,000 compact sutras in about the fifth-fourth centuries BCE. By the second century BCE his work was authoritative enough for Katyayana to annotate it and Patanjali to write the 'great commentary' on both, and it later fixed the form of classical Sanskrit. "
  "Statement 2 is wrong: the Ashtadhyayi is centuries older than the Guptas, whose age saw classical Sanskrit literature flourish on the foundation it laid.",
  "केवल कथन 1 सही है। गांधार के पाणिनि ने लगभग पाँचवीं-चौथी सदी ई.पू. में लगभग 4,000 संक्षिप्त सूत्रों में संस्कृत के नियम दिए। दूसरी सदी ई.पू. तक उनका ग्रंथ इतना प्रामाणिक हो चुका था कि कात्यायन ने उस पर वार्तिक लिखे और पतंजलि ने दोनों पर 'महान टीका' लिखी, और बाद में इसी ने शास्त्रीय संस्कृत का रूप स्थिर किया। "
  "कथन 2 गलत है: अष्टाध्यायी गुप्तों से सदियों पुरानी है, जिनके युग में इसी नींव पर शास्त्रीय संस्कृत साहित्य फला-फूला।",
  RS, "ancient-panini-patanjali", craft="linkage")

S(ANC, "easy", "Consider the following statements about the Great Stupa at Sanchi:",
  "सांची के महान स्तूप के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The brick stupa begun under Ashoka was later enlarged and cased in stone, so the monument shows work of more than one period.",
   "The carvings on its gateways show the Buddha through symbols, such as the Bodhi tree and footprints, rather than in human form.",
   "Sanchi is in Uttar Pradesh."],
  ["अशोक के समय शुरू हुए ईंटों के स्तूप को बाद में बड़ा कर पत्थर से ढका गया, इसलिए स्मारक में एक से अधिक कालों का काम दिखता है।",
   "इसके तोरणों की नक़्क़ाशी बुद्ध को मानव रूप के बजाय बोधि वृक्ष और पदचिह्न जैसे प्रतीकों से दिखाती है।",
   "सांची उत्तर प्रदेश में है।"],
  C3, 1,
  "Statements 1 and 2 are correct. The stupa of Ashoka's time was enlarged and cased in stone in the Shunga period, and the four gateways, carved with Jataka tales and scenes from the Buddha's life, were added in about the first century BCE with gifts from many donors, including ivory carvers of Vidisha. In this early phase the Buddha is shown only through symbols -- the tree, the wheel, the empty seat, footprints. "
  "Statement 3 is wrong: Sanchi is near Vidisha in Madhya Pradesh.",
  "कथन 1 और 2 सही हैं। अशोक के समय के स्तूप को शुंग काल में बड़ा कर पत्थर से ढका गया, और जातक कथाओं तथा बुद्ध के जीवन के दृश्यों से सजे चारों तोरण लगभग पहली सदी ई.पू. में कई दानदाताओं, जिनमें विदिशा के हाथीदाँत के कारीगर भी थे, के दान से जोड़े गए। इस प्रारंभिक चरण में बुद्ध को केवल प्रतीकों से दिखाया गया है, जैसे वृक्ष, चक्र, ख़ाली आसन और पदचिह्न। "
  "कथन 3 गलत है: सांची मध्य प्रदेश में विदिशा के पास है।",
  NCM, "ancient-sanchi-stupa", craft="linkage")

S(ANC, "easy", "Consider the following works:",
  "निम्नलिखित ग्रंथों पर विचार कीजिए:",
  ["Aryabhatiya", "Brahmasphutasiddhanta", "Pancha Siddhantika", "Sushruta Samhita", "Charaka Samhita"],
  ["आर्यभटीय", "ब्रह्मस्फुटसिद्धांत", "पंचसिद्धांतिका", "सुश्रुत संहिता", "चरक संहिता"],
  None, 1,
  "Three of them deal mainly with astronomy and mathematics. Aryabhata's Aryabhatiya (499 CE) explained day and night by the Earth's rotation and gave a close value of pi; Brahmagupta's Brahmasphutasiddhanta (628 CE) set out rules for working with zero and negative numbers; and Varahamihira's Pancha Siddhantika summarised five systems of astronomy. "
  "The Sushruta Samhita and the Charaka Samhita are the classics of medicine -- the first known above all for surgery, the second for internal medicine.",
  "इनमें से तीन मुख्यतः खगोलशास्त्र और गणित से जुड़े हैं। आर्यभट के आर्यभटीय (499 ई.) ने दिन और रात की व्याख्या पृथ्वी के घूर्णन से की और पाई का निकट मान दिया; ब्रह्मगुप्त के ब्रह्मस्फुटसिद्धांत (628 ई.) ने शून्य और ऋणात्मक संख्याओं के साथ गणना के नियम दिए; और वराहमिहिर की पंचसिद्धांतिका ने खगोलशास्त्र की पाँच पद्धतियों का सार दिया। "
  "सुश्रुत संहिता और चरक संहिता चिकित्सा के क्लासिक ग्रंथ हैं; पहला मुख्यतः शल्य-चिकित्सा के लिए और दूसरा काय-चिकित्सा के लिए जाना जाता है।",
  RS, "ancient-scientists-texts", opts=FIVE, opts_hi=FIVE_HI,
  closing="How many of the above deal mainly with astronomy or mathematics?", closing_hi="उपर्युक्त में से कितने मुख्यतः खगोलशास्त्र या गणित से जुड़े हैं?", craft="multi")

# ---------------------------------------------------------------- hard (2)
S(ANC, "hard", "Consider the following statements about the rise of Mahayana Buddhism:",
  "महायान बौद्ध धर्म के उदय के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The worship of the Buddha in image form went together with the Mahayana's devotional turn.",
   "The Bodhisattva ideal shifted the goal from one's own liberation to helping all beings towards it.",
   "The Theravada school took the Bodhisattva, rather than the arhat, as its ideal."],
  ["बुद्ध की मूर्ति रूप में उपासना महायान के भक्तिपरक मोड़ के साथ चली।",
   "बोधिसत्व के आदर्श ने लक्ष्य को अपनी मुक्ति से हटाकर सभी प्राणियों को उसकी ओर ले जाने पर रखा।",
   "थेरवाद संप्रदाय ने अर्हत के बजाय बोधिसत्व को अपना आदर्श माना।"],
  C3, 1,
  "Statements 1 and 2 are correct. From around the beginning of the Common Era, the Mahayana ('great vehicle') treated the Buddha as a saviour to be worshipped, and images of him and of Bodhisattvas became central. A Bodhisattva is one who has earned liberation but delays it out of compassion to help others, which opened the path to lay devotees. "
  "Statement 3 reverses the two: the Theravada, whose canon is the Pali Tripitaka, holds up the arhat, who attains liberation through his own effort; the Mahayana called the older schools the 'Hinayana', or lesser vehicle.",
  "कथन 1 और 2 सही हैं। लगभग सामान्य संवत् के आरंभ से महायान ('महान यान') ने बुद्ध को पूजनीय उद्धारक माना, और उनकी तथा बोधिसत्वों की मूर्तियाँ केंद्रीय हो गईं। बोधिसत्व वह है जिसने मुक्ति अर्जित कर ली है पर करुणावश दूसरों की सहायता के लिए उसे टालता है, और इसने गृहस्थ भक्तों के लिए मार्ग खोला। "
  "कथन 3 दोनों को उलट देता है: थेरवाद, जिसका धर्मग्रंथ पालि त्रिपिटक है, अर्हत को आदर्श मानता है, जो अपने प्रयास से मुक्ति पाता है; महायान ने पुराने संप्रदायों को 'हीनयान', यानी छोटा यान, कहा।",
  US, "ancient-buddhist-schools", craft="linkage")

S(ANC, "hard", "Consider the following Harappan sites:",
  "निम्नलिखित हड़प्पा स्थलों पर विचार कीजिए:",
  ["Dholavira", "Rakhigarhi", "Banawali", "Kot Diji", "Ropar"],
  ["धोलावीरा", "राखीगढ़ी", "बनावली", "कोट दीजी", "रोपड़"],
  None, 2,
  "Four of them are in present-day India: Dholavira in the Kachchh district of Gujarat, Rakhigarhi in Hisar district and Banawali in Fatehabad district of Haryana, and Ropar (Rupnagar) on the Sutlej in Punjab, the first Harappan site excavated in independent India. "
  "Kot Diji, a fortified settlement with early Harappan levels, lies in Sindh in Pakistan, not far from Mohenjodaro. Since 1947 most new Harappan sites have been found in India, in Gujarat, Haryana, Rajasthan and Punjab.",
  "इनमें से चार वर्तमान भारत में हैं: गुजरात के कच्छ ज़िले में धोलावीरा, हरियाणा के हिसार ज़िले में राखीगढ़ी और फ़तेहाबाद ज़िले में बनावली, और पंजाब में सतलुज पर रोपड़ (रूपनगर), जो स्वतंत्र भारत में खोदा गया पहला हड़प्पा स्थल था। "
  "प्रारंभिक हड़प्पा स्तरों वाली किलेबंद बस्ती कोट दीजी पाकिस्तान के सिंध में, मोहनजोदड़ो से ज़्यादा दूर नहीं, स्थित है। 1947 के बाद अधिकांश नए हड़प्पा स्थल भारत में, गुजरात, हरियाणा, राजस्थान और पंजाब में, मिले हैं।",
  US, "ancient-harappan-sites-rivers", opts=FIVE, opts_hi=FIVE_HI,
  closing="How many of the above are in present-day India?", closing_hi="उपर्युक्त में से कितने वर्तमान भारत में हैं?", craft="multi")

# ---------------------------------------------------------------- medium (21)
S(ANC, "medium", "The Kailasa temple at Ellora was carved out of a single rock, from the top downwards. Consider the following statements:",
  "एलोरा का कैलास मंदिर एक ही चट्टान को ऊपर से नीचे की ओर काटकर बनाया गया। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The method left no room for error, since stone could only be cut away, not added back.",
   "The temple was made under the patronage of the Rashtrakuta ruler Krishna I.",
   "The Ajanta caves include Hindu and Jain shrines as well as Buddhist ones."],
  ["इस तरीक़े में भूल की कोई गुंजाइश नहीं थी, क्योंकि पत्थर केवल काटा जा सकता था, वापस जोड़ा नहीं।",
   "मंदिर राष्ट्रकूट शासक कृष्ण प्रथम के संरक्षण में बना।",
   "अजंता की गुफाओं में बौद्ध के साथ हिंदू और जैन देवालय भी हैं।"],
  C3, 1,
  "Statements 1 and 2 are correct. The builders cut trenches into the hillside and then carved the whole temple, with its shrine, halls, bridges and free-standing elephants, out of the rock left in the middle, so the full plan had to be fixed in advance. It dates from the eighth century, under Krishna I. "
  "Statement 3 is wrong: Ajanta's caves, from the second century BCE to the late fifth century CE, are all Buddhist chaityas and viharas. It is Ellora that has Buddhist, Hindu and Jain caves side by side.",
  "कथन 1 और 2 सही हैं। निर्माताओं ने पहाड़ी में खाइयाँ काटीं और फिर बीच में बची चट्टान से गर्भगृह, मंडपों, पुलों और स्वतंत्र हाथियों सहित पूरा मंदिर तराशा, इसलिए पूरी योजना पहले से तय करनी थी। यह आठवीं सदी का है, कृष्ण प्रथम के समय का। "
  "कथन 3 गलत है: दूसरी सदी ई.पू. से पाँचवीं सदी ई. के अंत तक की अजंता की सभी गुफाएँ बौद्ध चैत्य और विहार हैं। एलोरा में बौद्ध, हिंदू और जैन गुफाएँ साथ-साथ हैं।",
  US, "ancient-ajanta-ellora-caves", craft="inference")

S(ANC, "medium", "Consider the following statements about the heterodox schools of the sixth and fifth centuries BCE:",
  "छठी और पाँचवीं सदी ई.पू. के अवैदिक संप्रदायों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Ajivika teacher Makkhali Gosala held, in his doctrine of niyati, that human effort could not change one's destiny.",
   "Ashoka gave the Barabar caves to Jain monks.",
   "The Charvakas accepted rebirth and the law of karma."],
  ["आजीवक उपदेशक मक्खलि गोसाल ने अपने नियति के सिद्धांत में कहा कि मानवीय प्रयास भाग्य नहीं बदल सकता।",
   "अशोक ने बराबर गुफाएँ जैन भिक्षुओं को दीं।",
   "चार्वाकों ने पुनर्जन्म और कर्म के नियम को स्वीकार किया।"],
  C3, 0,
  "Only statement 1 is correct. Gosala, once a companion of Mahavira, taught a strict fatalism: every soul passes through a fixed course of births, whatever it does. "
  "Statement 2 is the near-miss: Ashoka, and later his grandson Dasharatha, had caves in the Barabar and Nagarjuni hills polished and given to the Ajivikas, not the Jains -- a sign of royal respect for sects other than Buddhism. "
  "Statement 3 is wrong: the Charvakas or Lokayatas were materialists who accepted only perception as a source of knowledge and rejected rebirth, karma, the soul and the authority of the Vedas.",
  "केवल कथन 1 सही है। कभी महावीर के साथी रहे गोसाल ने कठोर नियतिवाद सिखाया: हर आत्मा, चाहे जो करे, जन्मों के एक तय क्रम से गुज़रती है। "
  "कथन 2 निकट-भ्रम है: अशोक ने, और बाद में उनके पौत्र दशरथ ने, बराबर और नागार्जुनी पहाड़ियों की गुफाएँ चिकनी करवाकर जैनों को नहीं, आजीवकों को दीं, जो बौद्ध धर्म के अलावा अन्य संप्रदायों के प्रति राजकीय सम्मान का संकेत है। "
  "कथन 3 गलत है: चार्वाक या लोकायत भौतिकवादी थे, जो केवल प्रत्यक्ष को ज्ञान का स्रोत मानते थे और पुनर्जन्म, कर्म, आत्मा तथा वेदों के प्रामाण्य को अस्वीकार करते थे।",
  RS, "ancient-ajivikas-charvaka", craft="linkage")

S(ANC, "medium", "Consider the following rulers:",
  "निम्नलिखित शासकों पर विचार कीजिए:",
  ["Harshavardhana", "Narasimhavarman I", "Mahendravarman I", "Rajendra Chola I", "Dantidurga"],
  ["हर्षवर्धन", "नरसिंहवर्मन प्रथम", "महेंद्रवर्मन प्रथम", "राजेंद्र चोल प्रथम", "दंतिदुर्ग"],
  None, 1,
  "Three of them fought Pulakeshin II of Badami. His Aihole inscription (634 CE), by the poet Ravikirti, claims victory over Harsha, whose advance to the south was checked; he fought the Pallava Mahendravarman I; and the next Pallava, Narasimhavarman I, defeated and killed him and took Vatapi in about 642. "
  "Rajendra Chola I ruled in the eleventh century, and Dantidurga, the founder of the Rashtrakuta power, overthrew the Badami Chalukyas in the mid-eighth century, about a century after Pulakeshin.",
  "इनमें से तीन बादामी के पुलकेशिन द्वितीय से लड़े। कवि रविकीर्ति का उसका ऐहोल अभिलेख (634 ई.) हर्ष पर विजय का दावा करता है, जिसकी दक्षिण की ओर बढ़त रोकी गई; वह पल्लव महेंद्रवर्मन प्रथम से लड़ा; और अगले पल्लव, नरसिंहवर्मन प्रथम, ने लगभग 642 में उसे हराकर मार डाला और वातापी ले लिया। "
  "राजेंद्र चोल प्रथम ने ग्यारहवीं सदी में शासन किया, और राष्ट्रकूट शक्ति के संस्थापक दंतिदुर्ग ने पुलकेशिन के लगभग एक सदी बाद, आठवीं सदी के मध्य में बादामी चालुक्यों को उखाड़ा।",
  US, "ancient-badami-chalukyas", opts=FIVE, opts_hi=FIVE_HI,
  closing="How many of the above were rivals of Pulakeshin II?", closing_hi="उपर्युक्त में से कितने पुलकेशिन द्वितीय के प्रतिद्वंद्वी थे?", craft="multi")

S(ANC, "medium", "Consider the following statements about the Buddhist councils and what came out of them:",
  "बौद्ध संगीतियों और उनके परिणामों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The First Council at Rajagriha fixed the Buddha's teachings by recitation, soon after his death.",
   "The Second Council at Vaishali led to a split in the Sangha over questions of monastic discipline.",
   "The Third Council, under Ashoka at Pataliputra, was followed by missions to spread the teaching, including one to Sri Lanka."],
  ["राजगृह में पहली संगीति ने बुद्ध की मृत्यु के तुरंत बाद उनके उपदेशों को सस्वर पाठ द्वारा स्थिर किया।",
   "वैशाली में दूसरी संगीति के कारण भिक्षु-अनुशासन के प्रश्नों पर संघ में विभाजन हुआ।",
   "पाटलिपुत्र में अशोक के समय तीसरी संगीति के बाद धर्म प्रचार के लिए मिशन भेजे गए, जिनमें एक श्रीलंका भी गया।"],
  C3, 2,
  "All three are correct. Since nothing was written down, the First Council agreed the texts by having senior monks recite them: the rules of the order and the discourses. About a century later the Council at Vaishali divided the monks into the Sthaviravadins and the Mahasanghikas over relaxed rules of conduct. "
  "The Third Council, associated with Ashoka's reign, purged dissenters and was followed by missions abroad; Ashoka's son Mahinda (Mahendra) is said to have taken Buddhism to Sri Lanka. The Fourth Council, in Kashmir under Kanishka, is linked with the rise of the Mahayana.",
  "तीनों कथन सही हैं। चूँकि कुछ लिखा नहीं गया था, पहली संगीति ने वरिष्ठ भिक्षुओं से पाठ करवाकर ग्रंथों पर सहमति बनाई: संघ के नियम और प्रवचन। लगभग एक सदी बाद वैशाली की संगीति ने आचरण के ढीले नियमों पर भिक्षुओं को स्थविरवादियों और महासांघिकों में बाँट दिया। "
  "अशोक के शासन से जुड़ी तीसरी संगीति ने असहमतों को अलग किया और उसके बाद विदेशों में मिशन भेजे गए; कहा जाता है कि अशोक के पुत्र महिंद (महेंद्र) बौद्ध धर्म को श्रीलंका ले गए। कनिष्क के समय कश्मीर में हुई चौथी संगीति महायान के उदय से जुड़ी है।",
  US, "ancient-buddhist-councils", craft="linkage")

S(ANC, "medium", "At Inamgaon, a Chalcolithic settlement in Maharashtra, a large house with a granary stood near the centre of the village, and the dead were buried beneath the floors of houses with pots. Consider the following statements:",
  "महाराष्ट्र की ताम्रपाषाण बस्ती इनामगाँव में गाँव के बीच के पास अन्नभंडार वाला एक बड़ा घर था, और मृतकों को घरों के फ़र्श के नीचे बर्तनों के साथ दफ़नाया जाता था। निम्नलिखित कथनों पर विचार कीजिए:",
  ["Some households may have had more wealth or authority than others.",
   "The settlement was occupied only for a few weeks each year.",
   "The people were hunter-gatherers with no agriculture."],
  ["कुछ परिवारों के पास दूसरों से अधिक धन या अधिकार रहा होगा।",
   "बस्ती में हर वर्ष केवल कुछ सप्ताह लोग रहते थे।",
   "लोग खेती न करने वाले शिकारी-संग्राहक थे।"],
  C3, 0,
  "Only statement 1 follows. A bigger house with a granary at the centre, and differences in the goods buried with the dead, point to social ranking, perhaps a chief. "
  "Statements 2 and 3 do not fit the evidence: burials beneath houses, a granary and storage pits mean a permanent village of farmers. Inamgaon, a Jorwe-culture site on the Ghod river, grew wheat, barley and pulses and even had an irrigation channel, while its people used copper alongside stone tools.",
  "केवल कथन 1 निकलता है। बीच में अन्नभंडार वाला बड़ा घर, और मृतकों के साथ दफ़नाई गई वस्तुओं में अंतर, सामाजिक श्रेणीकरण, शायद किसी मुखिया, की ओर संकेत करते हैं। "
  "कथन 2 और 3 साक्ष्य से मेल नहीं खाते: घरों के नीचे दफ़न, अन्नभंडार और भंडारण गड्ढों का अर्थ किसानों का स्थायी गाँव है। घोड नदी पर स्थित जोरवे संस्कृति का स्थल इनामगाँव गेहूँ, जौ और दालें उगाता था और वहाँ एक सिंचाई नाली भी थी, जबकि उसके लोग पत्थर के औज़ारों के साथ ताँबे का उपयोग करते थे।",
  US, "ancient-chalcolithic-cultures", craft="inference")

S(ANC, "medium", "Chandragupta Maurya's career has to be pieced together from Greek, Jain and Brahmanical sources. Consider the following statements:",
  "चंद्रगुप्त मौर्य का जीवन यूनानी, जैन और ब्राह्मणवादी स्रोतों को जोड़कर समझना पड़ता है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["Greek accounts of his treaty with Seleucus give Indian chronology one of its few fixed dates.",
   "The Jain tradition that he ended his life at Shravanabelagola cannot be checked against the Greek sources.",
   "The Mudrarakshasa, a Gupta-period play, is a contemporary record of his reign."],
  ["सेल्यूकस से उनकी संधि के यूनानी विवरण भारतीय कालक्रम को उसकी कुछ निश्चित तिथियों में से एक देते हैं।",
   "उनके श्रवणबेलगोला में देह-त्याग की जैन परंपरा को यूनानी स्रोतों से जाँचा नहीं जा सकता।",
   "गुप्त काल का नाटक मुद्राराक्षस उनके शासन का समकालीन विवरण है।"],
  C3, 1,
  "Statements 1 and 2 are correct. Because the Greek writers date the wars of Alexander's successors, the identification of the Indian king they describe with Chandragupta, made by William Jones, anchors Mauryan dates; after their conflict of about 305-303 BCE, Seleucus ceded lands in the north-west and sent Megasthenes to his court. The Greek sources say nothing of his last years, so the Jain account of his abdication and death by fasting at Shravanabelagola rests on later tradition and inscriptions there. "
  "Statement 3 is wrong: the Mudrarakshasa, by Vishakhadatta, was written many centuries later and is a political drama, not a record.",
  "कथन 1 और 2 सही हैं। चूँकि यूनानी लेखक सिकंदर के उत्तराधिकारियों के युद्धों की तिथियाँ देते हैं, इसलिए विलियम जोन्स द्वारा उनके वर्णित भारतीय राजा की पहचान चंद्रगुप्त से करना मौर्य तिथियों का आधार बनता है; लगभग 305-303 ई.पू. के संघर्ष के बाद सेल्यूकस ने उत्तर-पश्चिम की भूमि दी और मेगस्थनीज़ को उनके दरबार भेजा। यूनानी स्रोत उनके अंतिम वर्षों पर कुछ नहीं कहते, इसलिए श्रवणबेलगोला में उनके सिंहासन-त्याग और उपवास से देह-त्याग का जैन विवरण बाद की परंपरा और वहाँ के अभिलेखों पर टिका है। "
  "कथन 3 गलत है: विशाखदत्त का मुद्राराक्षस कई सदी बाद लिखा गया एक राजनीतिक नाटक है, विवरण नहीं।",
  US, "ancient-chandragupta-maurya-sources", craft="inference")

S(ANC, "medium", "The Chinese pilgrim Fa-hien travelled in India in the reign of Chandragupta II but never names the king. Consider the following statements:",
  "चीनी यात्री फ़ाह्यान चंद्रगुप्त द्वितीय के शासन में भारत में घूमे, पर कभी राजा का नाम नहीं लेते। निम्नलिखित कथनों पर विचार कीजिए:",
  ["His account is valued as an outsider's view of society and of Buddhism rather than as a political record.",
   "His description of Chandalas living outside the towns, and striking a piece of wood to warn of their approach, suggests that untouchability was well established.",
   "He came mainly to collect Buddhist texts, especially those on the rules of monastic discipline."],
  ["उनके विवरण को राजनीतिक अभिलेख के बजाय समाज और बौद्ध धर्म पर एक बाहरी व्यक्ति की दृष्टि के रूप में महत्व दिया जाता है।",
   "नगरों के बाहर रहने वाले और अपने आने की चेतावनी लकड़ी बजाकर देने वाले चांडालों का उनका वर्णन बताता है कि अस्पृश्यता अच्छी तरह स्थापित हो चुकी थी।",
   "वे मुख्यतः बौद्ध ग्रंथ, विशेषकर भिक्षु-अनुशासन के नियमों वाले, एकत्र करने आए थे।"],
  C3, 2,
  "All three are correct. Fa-hien, who travelled between about 399 and 414 CE, was a monk interested in holy places and texts, so his account says much about monasteries, charity and daily life -- rest houses, hospitals, mild punishments -- and almost nothing about the court. "
  "His picture of the Chandalas, kept apart and obliged to announce themselves, is one of the earliest outside records of untouchability. His aim was to find complete copies of the Vinaya, the monastic rules, which he took back to China by sea by way of Sri Lanka.",
  "तीनों कथन सही हैं। लगभग 399 से 414 ई. के बीच घूमने वाले फ़ाह्यान पवित्र स्थलों और ग्रंथों में रुचि रखने वाले भिक्षु थे, इसलिए उनका विवरण विहारों, दान और दैनिक जीवन, जैसे धर्मशालाओं, चिकित्सालयों और हल्के दंडों, के बारे में बहुत कुछ कहता है और दरबार के बारे में लगभग कुछ नहीं। "
  "अलग रखे गए और अपने आने की सूचना देने को बाध्य चांडालों का उनका चित्र अस्पृश्यता के सबसे प्रारंभिक बाहरी विवरणों में से एक है। उनका उद्देश्य भिक्षु-नियमों, विनय, की पूरी प्रतियाँ खोजना था, जिन्हें वे समुद्री मार्ग से श्रीलंका होते हुए चीन ले गए।",
  US, "ancient-fa-hien-gupta-visit", craft="inference")

S(ANC, "medium", "Consider the following statements about the later Guptas:",
  "उत्तरवर्ती गुप्तों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Skandagupta's wars against the Hunas, recorded in his Bhitari pillar inscription, strained the empire's resources.",
   "The Gupta era, reckoned from 319-20 CE, is generally linked to the accession of Samudragupta.",
   "After Skandagupta's victory the Hunas never again troubled north India."],
  ["भितरी स्तंभ अभिलेख में दर्ज हूणों के विरुद्ध स्कंदगुप्त के युद्धों ने साम्राज्य के संसाधनों पर दबाव डाला।",
   "319-20 ई. से गिना जाने वाला गुप्त संवत् सामान्यतः समुद्रगुप्त के राज्यारोहण से जोड़ा जाता है।",
   "स्कंदगुप्त की विजय के बाद हूणों ने उत्तर भारत को फिर कभी परेशान नहीं किया।"],
  C3, 0,
  "Only statement 1 is correct. Skandagupta (about 455-467 CE) beat back the first Huna attacks, but the effort was costly, and the empire weakened under his successors. "
  "Statement 2 names the wrong king: the Gupta era is usually traced to Chandragupta I, Samudragupta's father and the first to take the title Maharajadhiraja. "
  "Statement 3 is wrong: in the early sixth century the Hunas returned under Toramana and Mihirakula and took over much of the north-west and central India, until Indian rulers checked them; their raids helped break up the Gupta empire.",
  "केवल कथन 1 सही है। स्कंदगुप्त (लगभग 455-467 ई.) ने हूणों के पहले आक्रमण रोके, पर यह प्रयास महँगा पड़ा, और उनके उत्तराधिकारियों के समय साम्राज्य कमज़ोर हुआ। "
  "कथन 2 ग़लत राजा बताता है: गुप्त संवत् प्रायः समुद्रगुप्त के पिता चंद्रगुप्त प्रथम से जोड़ा जाता है, जिन्होंने पहली बार महाराजाधिराज की उपाधि ली। "
  "कथन 3 गलत है: छठी सदी के आरंभ में हूण तोरमाण और मिहिरकुल के नेतृत्व में लौटे और उत्तर-पश्चिम तथा मध्य भारत के बड़े भाग पर छा गए, जब तक भारतीय शासकों ने उन्हें रोका नहीं; उनके आक्रमणों ने गुप्त साम्राज्य को तोड़ने में मदद दी।",
  RS, "ancient-gupta-rulers-iron-pillar", craft="linkage")

S(ANC, "medium", "Consider the following monuments of the Gupta and immediately following periods:",
  "गुप्त और उसके ठीक बाद के कालों के निम्नलिखित स्मारकों पर विचार कीजिए:",
  ["Dashavatara temple, Deogarh", "Brick temple, Bhitargaon", "Udayagiri caves near Vidisha", "Parvati temple, Nachna", "Elephanta caves"],
  ["दशावतार मंदिर, देवगढ़", "ईंटों का मंदिर, भीतरगाँव", "विदिशा के पास उदयगिरि गुफाएँ", "पार्वती मंदिर, नचना", "एलीफ़ेंटा गुफाएँ"],
  None, 1,
  "Three are structural temples, built up from stone or brick rather than cut into rock. The Dashavatara temple at Deogarh is a free-standing stone temple, among the earliest with a shikhara; the temple at Bhitargaon near Kanpur is built of brick, with terracotta panels; and the Parvati temple at Nachna is another early stone temple. "
  "The Udayagiri caves, with the great Varaha panel, and the Elephanta caves near Mumbai, with the Shiva Maheshamurti, are cut into the rock.",
  "तीन संरचनात्मक मंदिर हैं, जो चट्टान काटकर नहीं, पत्थर या ईंट से खड़े किए गए। देवगढ़ का दशावतार मंदिर स्वतंत्र खड़ा पत्थर का मंदिर है, शिखर वाले सबसे प्रारंभिक मंदिरों में से एक; कानपुर के पास भीतरगाँव का मंदिर टेराकोटा फलकों वाला ईंटों का बना है; और नचना का पार्वती मंदिर एक और प्रारंभिक पत्थर का मंदिर है। "
  "विशाल वराह फलक वाली उदयगिरि गुफाएँ और शिव महेशमूर्ति वाली मुंबई के पास की एलीफ़ेंटा गुफाएँ चट्टान में काटी गई हैं।",
  US, "ancient-gupta-temples-caves", opts=FIVE, opts_hi=FIVE_HI,
  closing="How many of the above are structural temples rather than rock-cut ones?", closing_hi="उपर्युक्त में से कितने शैलकृत के बजाय संरचनात्मक मंदिर हैं?", craft="multi")

S(ANC, "medium", "Consider the following statements about the Harappan civilisation:",
  "हड़प्पा सभ्यता के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The absence of the horse from the seals, and the scarcity of horse remains, is one argument for distinguishing the Harappans from the Rig Vedic people, for whom the horse mattered greatly.",
   "Houses usually opened onto side lanes rather than onto the main streets, which suggests a concern for privacy.",
   "Cotton was unknown to the Harappans, who wove only wool."],
  ["मुहरों पर घोड़े का अभाव और घोड़े के अवशेषों की कमी हड़प्पावासियों को उन ऋग्वैदिक लोगों से अलग मानने का एक तर्क है, जिनके लिए घोड़ा बहुत महत्वपूर्ण था।",
   "घर प्रायः मुख्य सड़कों के बजाय गलियों की ओर खुलते थे, जो निजता की चिंता का संकेत देता है।",
   "हड़प्पावासी कपास से अनजान थे और केवल ऊन बुनते थे।"],
  C3, 1,
  "Statements 1 and 2 are correct. The seals show the humped bull, the 'unicorn', the elephant, the tiger and the rhinoceros, but not the horse, while the Rig Veda is full of horses and chariots; this is one of the arguments, debated by scholars, for treating the two cultures as different. Doors and windows faced lanes, not the main roads, and courtyards lay within. "
  "Statement 3 is wrong: cotton fragments at Mohenjodaro, and cotton seeds at Mehrgarh, are among the earliest evidence of the crop anywhere; the Greeks later called it 'sindon'.",
  "कथन 1 और 2 सही हैं। मुहरें कूबड़ वाला बैल, 'एकशृंगी', हाथी, बाघ और गैंडा दिखाती हैं, पर घोड़ा नहीं, जबकि ऋग्वेद घोड़ों और रथों से भरा है; यह उन तर्कों में से एक है, जिन पर विद्वानों में बहस है, जिनके आधार पर दोनों संस्कृतियों को अलग माना जाता है। दरवाज़े और खिड़कियाँ मुख्य सड़कों के बजाय गलियों की ओर थीं, और आँगन भीतर थे। "
  "कथन 3 गलत है: मोहनजोदड़ो में कपास के टुकड़े और मेहरगढ़ में कपास के बीज कहीं भी इस फ़सल के सबसे प्रारंभिक साक्ष्यों में से हैं; बाद में यूनानियों ने इसे 'सिंडन' कहा।",
  NCM, "ancient-harappan-cotton-horse-houses", craft="inference")

S(ANC, "medium", "Consider the following statements about Harshavardhana's religious patronage:",
  "हर्षवर्धन के धार्मिक संरक्षण के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Hiuen Tsang describes an assembly at Kanauj, held in his honour, at which the Mahayana doctrine was expounded.",
   "At Prayaga, every five years, Harsha gave away his accumulated wealth in charity.",
   "Hiuen Tsang wrote his account of these assemblies in Sanskrit, for Harsha's court."],
  ["ह्वेनसांग कन्नौज की एक सभा का वर्णन करते हैं, जो उनके सम्मान में हुई और जिसमें महायान सिद्धांत की व्याख्या की गई।",
   "प्रयाग में हर पाँच वर्ष पर हर्ष अपना संचित धन दान में दे देता था।",
   "ह्वेनसांग ने इन सभाओं का अपना विवरण हर्ष के दरबार के लिए संस्कृत में लिखा।"],
  C3, 1,
  "Statements 1 and 2 are correct. Hiuen Tsang describes the Kanauj assembly of about 643 CE, and the great quinquennial gathering at the confluence at Prayaga, where Harsha distributed his treasure to monks, Brahmanas and the poor. "
  "Statement 3 is wrong: Hiuen Tsang wrote his account, the Si-yu-ki ('Records of the Western World'), in Chinese after returning home, at the request of the Tang emperor. It also says that at Prayaga images of the Buddha, the Sun and Shiva were worshipped on successive days -- Harsha's own inscriptions call him a devotee of Shiva.",
  "कथन 1 और 2 सही हैं। ह्वेनसांग लगभग 643 ई. की कन्नौज सभा का, और प्रयाग के संगम पर हर पाँच वर्ष होने वाले उस बड़े समागम का वर्णन करते हैं, जहाँ हर्ष ने भिक्षुओं, ब्राह्मणों और ग़रीबों में अपना ख़ज़ाना बाँटा। "
  "कथन 3 गलत है: ह्वेनसांग ने अपना विवरण, सि-यू-की ('पश्चिमी संसार के अभिलेख'), स्वदेश लौटकर तांग सम्राट के आग्रह पर चीनी भाषा में लिखा। उसमें यह भी है कि प्रयाग में लगातार दिनों पर बुद्ध, सूर्य और शिव की प्रतिमाओं की पूजा हुई; हर्ष के अपने अभिलेख उसे शिव का भक्त कहते हैं।",
  US, "ancient-harsha-assemblies-plays", craft="linkage")

S(ANC, "medium", "Harshavardhana of Thanesar took over the kingdom of Kanauj and made it his capital. Consider the following statements:",
  "थानेसर के हर्षवर्धन ने कन्नौज का राज्य सँभाला और उसे अपनी राजधानी बनाया। निम्नलिखित कथनों पर विचार कीजिए:",
  ["Kanauj's position in the Ganga valley made it the prize that later powers fought over for centuries.",
   "Harsha took over Kanauj after the Maukhari king, the husband of his sister Rajyashri, was killed.",
   "Harsha himself belonged to the Maukhari dynasty."],
  ["गंगा घाटी में कन्नौज की स्थिति ने इसे वह पुरस्कार बना दिया जिसके लिए बाद की शक्तियाँ सदियों तक लड़ीं।",
   "हर्ष ने कन्नौज तब सँभाला जब उनकी बहन राज्यश्री के पति, मौखरि राजा, मारे गए।",
   "हर्ष स्वयं मौखरि वंश के थे।"],
  C3, 1,
  "Statements 1 and 2 are correct. After the Maukhari king Grahavarman was killed and his brother Rajyavardhana died, Harsha, of the Pushyabhuti (Vardhana) family of Thanesar, joined the two kingdoms and ruled from Kanauj. The city's wealth and central place in the Gangetic plain made it the target of the 'tripartite struggle' among the Palas, the Gurjara-Pratiharas and the Rashtrakutas in the eighth to tenth centuries. "
  "Statement 3 is wrong: the Maukharis were his sister's in-laws, not his own dynasty.",
  "कथन 1 और 2 सही हैं। मौखरि राजा ग्रहवर्मन के मारे जाने और उनके भाई राज्यवर्धन की मृत्यु के बाद थानेसर के पुष्यभूति (वर्धन) परिवार के हर्ष ने दोनों राज्यों को मिलाया और कन्नौज से शासन किया। गंगा के मैदान में नगर की संपत्ति और केंद्रीय स्थिति ने इसे आठवीं से दसवीं सदी में पालों, गुर्जर-प्रतिहारों और राष्ट्रकूटों के 'त्रिपक्षीय संघर्ष' का लक्ष्य बना दिया। "
  "कथन 3 गलत है: मौखरि उनकी बहन के ससुराल वाले थे, उनका अपना वंश नहीं।",
  US, "ancient-harshavardhana", craft="linkage")

S(ANC, "medium", "Consider the following statements about the Indo-Greeks and their contacts:",
  "हिंद-यवनों और उनके संपर्कों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Heliodorus pillar at Besnagar, set up by a Greek envoy in honour of Vasudeva, shows that some Greeks took up Indian cults.",
   "The Milindapanha's dialogue between Menander and the monk Nagasena shows Greek interest in Buddhist thought.",
   "Indo-Greek coins, with portraits of kings and bilingual legends, are a major source for their history."],
  ["एक यूनानी दूत द्वारा वासुदेव के सम्मान में खड़ा किया गया बेसनगर का हेलियोडोरस स्तंभ दिखाता है कि कुछ यूनानियों ने भारतीय उपासना-पद्धतियाँ अपनाईं।",
   "मिलिंदपन्हो में मिनांडर और भिक्षु नागसेन का संवाद बौद्ध चिंतन में यूनानी रुचि दिखाता है।",
   "राजाओं के चित्रों और द्विभाषी लेखों वाले हिंद-यवन सिक्के उनके इतिहास का प्रमुख स्रोत हैं।"],
  C3, 2,
  "All three are correct. Heliodorus, envoy of the Indo-Greek king Antialcidas of Taxila to a king at Vidisha, called himself a 'Bhagavata' on the Garuda pillar he set up in about 113 BCE. The Pali Milindapanha records Menander's questions to Nagasena, and Buddhist tradition says he became a follower. "
  "So many Indo-Greek kings are known only from their coins, with realistic portraits and legends in Greek and Prakrit (in Kharoshthi), that the coins are the main basis for their history; they also set a model of portrait coinage that later rulers followed.",
  "तीनों कथन सही हैं। तक्षशिला के हिंद-यवन राजा एंटियालकिडस के विदिशा के एक राजा के पास भेजे गए दूत हेलियोडोरस ने लगभग 113 ई.पू. में अपने खड़े किए गरुड़ स्तंभ पर स्वयं को 'भागवत' कहा। पालि मिलिंदपन्हो नागसेन से मिनांडर के प्रश्न दर्ज करता है, और बौद्ध परंपरा कहती है कि वह अनुयायी बन गया। "
  "इतने हिंद-यवन राजा केवल अपने सिक्कों से ज्ञात हैं, जिन पर यथार्थ चित्र और यूनानी तथा प्राकृत (खरोष्ठी में) में लेख हैं, कि सिक्के ही उनके इतिहास का मुख्य आधार हैं; उन्होंने चित्र-युक्त सिक्कों का ऐसा आदर्श भी रखा जिसका बाद के शासकों ने अनुसरण किया।",
  US, "ancient-indo-greeks-contacts", craft="linkage")

S(ANC, "medium", "Mesopotamian texts of the late third millennium BCE speak of trade with a land called 'Meluhha'. Consider the following statements:",
  "तीसरी सहस्राब्दी ई.पू. के अंत के मेसोपोटामियाई ग्रंथ 'मेलुहा' नामक देश से व्यापार की बात करते हैं। निम्नलिखित कथनों पर विचार कीजिए:",
  ["Harappan seals and beads found in Mesopotamia support the identification of Meluhha with the Indus region.",
   "Harappan weights followed a purely decimal system, like the metric system.",
   "The Harappans paid for their imports in coined money."],
  ["मेसोपोटामिया में मिली हड़प्पा मुहरें और मनके मेलुहा की पहचान सिंधु क्षेत्र से करने का समर्थन करते हैं।",
   "हड़प्पा के बाट मीट्रिक प्रणाली की तरह पूरी तरह दशमलव पद्धति पर थे।",
   "हड़प्पावासी अपने आयात का मूल्य सिक्कों में चुकाते थे।"],
  C3, 0,
  "Only statement 1 is correct. Mesopotamian texts mention copper, carnelian, ivory and timber from Meluhha, and Harappan seals, etched carnelian beads and weights have been found at Mesopotamian sites, which is why most scholars identify Meluhha with the Indus region. "
  "Statement 2 is wrong: the cubical chert weights, found from Gujarat to the Punjab, doubled in the lower denominations (1, 2, 4, 8 ...) and rose in decimal steps only for the higher ones. Statement 3 is wrong: there were no coins in the Harappan world; exchange was by barter and measured goods. Coins appear in the subcontinent only with the punch-marked coins of the Mahajanapada period.",
  "केवल कथन 1 सही है। मेसोपोटामियाई ग्रंथ मेलुहा से ताँबा, कार्नेलियन, हाथीदाँत और लकड़ी आने का उल्लेख करते हैं, और मेसोपोटामियाई स्थलों पर हड़प्पा मुहरें, उकेरे गए कार्नेलियन मनके और बाट मिले हैं, इसीलिए अधिकांश विद्वान मेलुहा को सिंधु क्षेत्र मानते हैं। "
  "कथन 2 गलत है: गुजरात से पंजाब तक मिलने वाले चर्ट के घनाकार बाट छोटे मानों में दोगुने होते जाते थे (1, 2, 4, 8 ...) और केवल बड़े मानों में दशमलव क्रम में बढ़ते थे। कथन 3 गलत है: हड़प्पा जगत में सिक्के नहीं थे; विनिमय वस्तु-विनिमय और तौली गई वस्तुओं से होता था। उपमहाद्वीप में सिक्के महाजनपद काल के आहत सिक्कों के साथ ही आते हैं।",
  NCM, "ancient-indus-trade", craft="inference")

S(ANC, "medium", "Consider the following statements about the division of Jainism into the Svetambara and Digambara sects:",
  "जैन धर्म के श्वेतांबर और दिगंबर संप्रदायों में विभाजन के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Jain tradition links the division to a famine in Chandragupta Maurya's time, when one group of monks went south and another stayed in Magadha.",
   "The two sects differ over whether monks must give up all clothing.",
   "The Digambaras hold that women can attain liberation in their present birth."],
  ["जैन परंपरा इस विभाजन को चंद्रगुप्त मौर्य के समय के एक अकाल से जोड़ती है, जब भिक्षुओं का एक समूह दक्षिण गया और दूसरा मगध में रहा।",
   "दोनों संप्रदायों में मतभेद इस पर है कि क्या भिक्षुओं को सभी वस्त्र त्यागने होंगे।",
   "दिगंबर मानते हैं कि स्त्रियाँ इसी जन्म में मोक्ष पा सकती हैं।"],
  C3, 1,
  "Statements 1 and 2 are correct. By tradition, a twelve-year famine led part of the order to migrate to Karnataka while the rest stayed in the north under Sthulabhadra; when the groups met again they differed over practice and over the canon compiled at Pataliputra in the meantime. The Digambaras ('sky-clad') hold that monks must renounce clothing altogether, while the Svetambaras wear white. "
  "Statement 3 reverses the positions: it is the Svetambaras who accept that women can be liberated in their present birth; the Digambaras hold that a woman must first be reborn as a man.",
  "कथन 1 और 2 सही हैं। परंपरा के अनुसार बारह वर्ष के अकाल के कारण संघ का एक भाग कर्नाटक चला गया, जबकि शेष स्थूलभद्र के नेतृत्व में उत्तर में रहा; जब समूह फिर मिले तो आचरण पर और इस बीच पाटलिपुत्र में संकलित धर्मग्रंथ पर उनमें मतभेद थे। दिगंबर ('आकाश-वस्त्रधारी') मानते हैं कि भिक्षुओं को वस्त्र पूरी तरह त्यागने होंगे, जबकि श्वेतांबर सफ़ेद वस्त्र पहनते हैं। "
  "कथन 3 स्थितियों को उलट देता है: श्वेतांबर ही मानते हैं कि स्त्रियाँ इसी जन्म में मुक्त हो सकती हैं; दिगंबरों का मत है कि स्त्री को पहले पुरुष के रूप में जन्म लेना होगा।",
  RS, "ancient-jainism-councils-schism", craft="linkage")

S(ANC, "medium", "Kushana gold coins show Greek, Iranian and Indian deities, among them the Buddha and Shiva. Consider the following statements:",
  "कुषाण स्वर्ण सिक्कों पर यूनानी, ईरानी और भारतीय देवता दिखाई देते हैं, जिनमें बुद्ध और शिव भी हैं। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The rulers sought to appeal to the many peoples of an empire that stretched from Central Asia to the Gangetic plain.",
   "Roman gold coming in through trade may have supplied part of the metal for these coins.",
   "Some of their coins carry legends in Bactrian, an Iranian language written in the Greek script."],
  ["शासक मध्य एशिया से गंगा के मैदान तक फैले साम्राज्य के अनेक लोगों को आकर्षित करना चाहते थे।",
   "व्यापार से आने वाला रोमन सोना इन सिक्कों की धातु का एक भाग दे सकता था।",
   "उनके कुछ सिक्कों पर बैक्ट्रियाई, यानी यूनानी लिपि में लिखी एक ईरानी भाषा, में लेख हैं।"],
  C3, 2,
  "All three are correct. Kanishka's coins carry deities as different as the Iranian Mithra, the Greek Helios and the Buddha, and Wima Kadphises's carry Shiva with his bull -- a way of speaking to subjects of many faiths across an empire from the Oxus to the Ganga. The Kushanas minted gold on a large scale, and the flow of Roman gold into India through trade is often linked to it. "
  "The Kushanas were a branch of the Yuezhi, a Central Asian people, not Greeks; they used Greek on their early coins and then, from Kanishka's time, Bactrian in Greek letters, because those were current in Bactria.",
  "तीनों कथन सही हैं। कनिष्क के सिक्कों पर ईरानी मिथ्र, यूनानी हेलियोस और बुद्ध जैसे बहुत अलग देवता हैं, और विम कडफ़िसेस के सिक्कों पर अपने बैल के साथ शिव, जो ऑक्सस से गंगा तक फैले साम्राज्य में अनेक धर्मों की प्रजा से संवाद का तरीक़ा था। कुषाणों ने बड़े पैमाने पर स्वर्ण सिक्के ढाले, और व्यापार से भारत आने वाले रोमन सोने को प्रायः इससे जोड़ा जाता है। "
  "कुषाण यूनानी नहीं, मध्य एशिया के लोगों, यूएझी, की एक शाखा थे; वे अपने प्रारंभिक सिक्कों पर यूनानी और फिर कनिष्क के समय से यूनानी अक्षरों में बैक्ट्रियाई का उपयोग करते थे, क्योंकि ये बैक्ट्रिया में प्रचलित थीं।",
  US, "ancient-kushanas-empire-coins", craft="inference")

S(ANC, "medium", "Consider the following statements about why Magadha became the most powerful of the Mahajanapadas:",
  "मगध महाजनपदों में सबसे शक्तिशाली क्यों बना, इसके बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Rich iron ores in the region gave it better tools and weapons.",
   "Its position on the Ganga and its tributaries gave it fertile land and easy river routes.",
   "Elephants from the forests to the east strengthened its army."],
  ["क्षेत्र के समृद्ध लौह अयस्कों ने इसे बेहतर औज़ार और हथियार दिए।",
   "गंगा और उसकी सहायक नदियों पर इसकी स्थिति ने इसे उपजाऊ भूमि और आसान नदी मार्ग दिए।",
   "पूर्व के जंगलों के हाथियों ने इसकी सेना को मज़बूत किया।"],
  C3, 2,
  "All three are correct. The iron ores of the Rajgir hills and the Chota Nagpur region gave Magadha tools for clearing the forest and farming, and weapons for war. The alluvial soils of the middle Ganga plain yielded surplus grain, and the rivers carried trade and troops. Elephants from the eastern forests were a decisive arm in its wars. "
  "Able and ambitious rulers -- Bimbisara, Ajatashatru, Mahapadma Nanda -- used these advantages; and the city of Pataliputra, at the meeting of rivers, was easy to defend.",
  "तीनों कथन सही हैं। राजगीर की पहाड़ियों और छोटानागपुर क्षेत्र के लौह अयस्कों ने मगध को जंगल साफ़ करने और खेती के औज़ार तथा युद्ध के हथियार दिए। मध्य गंगा मैदान की जलोढ़ मिट्टी ने अधिशेष अनाज दिया, और नदियाँ व्यापार और सेना को ले जाती थीं। पूर्व के जंगलों के हाथी इसके युद्धों में निर्णायक अंग थे। "
  "बिंबिसार, अजातशत्रु और महापद्म नंद जैसे योग्य और महत्वाकांक्षी शासकों ने इन लाभों का उपयोग किया; और नदियों के संगम पर स्थित पाटलिपुत्र नगर की रक्षा आसान थी।",
  RS, "ancient-magadha-haryanka-nanda", craft="linkage")

S(ANC, "medium", "Consider the following statements about the Mahajanapadas:",
  "महाजनपदों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Vajji was ruled by a hereditary king, like Magadha.",
   "In the ganas, every adult, including women and slaves, had a voice in the assembly.",
   "Magadha's capital was moved from Pataliputra to Rajagriha under Udayin."],
  ["मगध की तरह वज्जि पर भी एक वंशानुगत राजा का शासन था।",
   "गणों में स्त्रियों और दासों सहित हर वयस्क की सभा में आवाज़ थी।",
   "उदयिन के समय मगध की राजधानी पाटलिपुत्र से राजगृह ले जाई गई।"],
  C3, 3,
  "None is correct. The Vajji confederacy, with its centre at Vaishali and the Lichchhavis as its leading clan, was a gana-sangha run by an assembly of rajas -- heads of Kshatriya families -- who met in the santhagara, not by a hereditary king. "
  "Statement 2 overstates its openness: women, slaves and labourers had no say, so these early examples of government by assembly were rule by a clan elite. Statement 3 reverses the move: the capital went from Rajagriha to Pataliputra, which Udayin is credited with founding at the confluence of the Ganga and the Son.",
  "कोई भी कथन सही नहीं है। वैशाली केंद्र वाला और लिच्छवियों को प्रमुख कुल मानने वाला वज्जि संघ एक गण-संघ था, जो किसी वंशानुगत राजा से नहीं, बल्कि संथागार में मिलने वाले राजाओं, यानी क्षत्रिय परिवारों के मुखियाओं, की सभा से चलता था। "
  "कथन 2 इसके खुलेपन को बढ़ा-चढ़ाकर बताता है: स्त्रियों, दासों और मज़दूरों की कोई भूमिका नहीं थी, इसलिए सभा द्वारा शासन के ये प्रारंभिक उदाहरण एक कुलीन वर्ग का शासन थे। कथन 3 स्थानांतरण को उलट देता है: राजधानी राजगृह से पाटलिपुत्र गई, जिसकी स्थापना का श्रेय गंगा और सोन के संगम पर उदयिन को दिया जाता है।",
  NCM, "ancient-mahajanapadas", craft="linkage")

S(ANC, "medium", "Consider the following statements about the Rig Vedic period:",
  "ऋग्वैदिक काल के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The 'Battle of the Ten Kings', fought on the Parushni (Ravi), was a conflict among the Vedic tribes themselves.",
   "The large number of hymns to Indra, a warrior god who breaks forts, reflects a society in which war and raiding mattered.",
   "The Rig Veda shows a fully developed caste system with untouchability."],
  ["परुष्णी (रावी) पर लड़ा गया 'दाशराज्ञ युद्ध' स्वयं वैदिक जनों के बीच का संघर्ष था।",
   "दुर्ग तोड़ने वाले योद्धा देवता इंद्र को समर्पित ऋचाओं की बड़ी संख्या ऐसे समाज को दर्शाती है जिसमें युद्ध और छापे महत्वपूर्ण थे।",
   "ऋग्वेद अस्पृश्यता सहित पूर्ण विकसित जाति व्यवस्था दिखाता है।"],
  C3, 1,
  "Statements 1 and 2 are correct. The Bharata chief Sudasa defeated a confederacy of ten tribes, Vedic and non-Vedic, on the Parushni, as the seventh mandala records -- conflict was as often among the Vedic tribes as against others. Indra receives about 250 hymns, more than any other god, in a society of tribal chiefs, cattle raids and battles. "
  "Statement 3 is wrong: Rig Vedic society was tribal and fairly fluid; the idea of four varnas appears in a late hymn, and birth-based caste with untouchability took shape much later.",
  "कथन 1 और 2 सही हैं। भरत मुखिया सुदास ने परुष्णी पर वैदिक और ग़ैर-वैदिक, दस जनों के संघ को हराया, जैसा सातवाँ मंडल बताता है; संघर्ष जितना दूसरों से था उतना ही वैदिक जनों के बीच भी। जनजातीय मुखियाओं, पशु-हरण और युद्धों वाले समाज में इंद्र को किसी भी अन्य देवता से अधिक, लगभग 250 ऋचाएँ मिलती हैं। "
  "कथन 3 गलत है: ऋग्वैदिक समाज जनजातीय और काफ़ी लचीला था; चार वर्णों का विचार एक बाद की ऋचा में आता है, और अस्पृश्यता सहित जन्म-आधारित जाति बहुत बाद में बनी।",
  RS, "ancient-rig-vedic-society", craft="linkage")

S(ANC, "medium", "Consider the following statements about the Sangam poems as a source:",
  "स्रोत के रूप में संगम कविताओं के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["They are a source for social life in the Tamil region because they describe ordinary people and landscapes as well as kings.",
   "They were composed over several centuries, so they cannot be read as describing a single moment.",
   "The Tolkappiyam, a work on grammar and poetics, sets out the conventions that many of the poems follow."],
  ["वे तमिल क्षेत्र के सामाजिक जीवन का स्रोत हैं क्योंकि वे राजाओं के साथ आम लोगों और भू-दृश्यों का भी वर्णन करती हैं।",
   "वे कई सदियों में रची गईं, इसलिए उन्हें किसी एक समय का वर्णन मानकर नहीं पढ़ा जा सकता।",
   "व्याकरण और काव्यशास्त्र का ग्रंथ तोलकाप्पियम वे परिपाटियाँ बताता है जिनका कई कविताएँ पालन करती हैं।"],
  C3, 2,
  "All three are correct. The poems speak of farmers, fishers, herders, merchants, bards and warriors in different landscapes, so they are read for social and economic history, not just for the deeds of the Chera, Chola and Pandya kings. Since they were composed over a long span, roughly the third century BCE to the third century CE, historians are careful about treating them as one picture. "
  "The Tolkappiyam is not an anthology but a treatise; its rules on akam (love) and puram (war and public life) and on the five landscapes help readers decode the poems' imagery.",
  "तीनों कथन सही हैं। कविताएँ अलग-अलग भू-दृश्यों के किसानों, मछुआरों, चरवाहों, व्यापारियों, भाटों और योद्धाओं की बात करती हैं, इसलिए उन्हें केवल चेर, चोल और पांड्य राजाओं के कार्यों के लिए नहीं, सामाजिक और आर्थिक इतिहास के लिए पढ़ा जाता है। चूँकि वे लगभग तीसरी सदी ई.पू. से तीसरी सदी ई. तक के लंबे समय में रची गईं, इसलिए इतिहासकार उन्हें एक ही चित्र मानने में सावधान रहते हैं। "
  "तोलकाप्पियम कोई संकलन नहीं, शास्त्र है; अकम (प्रेम) और पुरम (युद्ध और सार्वजनिक जीवन) तथा पाँच भू-दृश्यों पर उसके नियम पाठकों को कविताओं के बिंब समझने में मदद करते हैं।",
  NCM, "ancient-sangam-age-overview", craft="inference")

S(ANC, "medium", "Consider the following statements about the Satavahanas:",
  "सातवाहनों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Kings named after their mothers, such as Gautamiputra, show that the throne passed through the mother's line.",
   "Their grants of land to Brahmanas and Buddhist monks, with exemptions from royal interference, are among the earliest such records.",
   "Satavahana inscriptions are mostly in Sanskrit."],
  ["गौतमीपुत्र जैसे माताओं के नाम वाले राजा दिखाते हैं कि सिंहासन माता के वंश से चलता था।",
   "राजकीय हस्तक्षेप से छूट के साथ ब्राह्मणों और बौद्ध भिक्षुओं को उनके भूमि-दान ऐसे सबसे प्रारंभिक अभिलेखों में से हैं।",
   "सातवाहन अभिलेख अधिकांशतः संस्कृत में हैं।"],
  C3, 0,
  "Only statement 2 is correct. Statement 1 draws the wrong conclusion: metronymics such as Gautamiputra and Vasishthiputra point to the standing of royal mothers -- Gautami Balashri herself issued the Nashik inscription -- but succession still passed from father to son. Their grants freed the donated land from the entry of royal officers and soldiers, an early form of the land grants that later spread widely. "
  "Statement 3 is wrong: Satavahana inscriptions are in Prakrit, unlike the Sanskrit of the contemporary Junagadh inscription of the Shakas.",
  "केवल कथन 2 सही है। कथन 1 ग़लत निष्कर्ष निकालता है: गौतमीपुत्र और वासिष्ठीपुत्र जैसे मातृनाम राजमाताओं की प्रतिष्ठा की ओर संकेत करते हैं, स्वयं गौतमी बलश्री ने नासिक अभिलेख जारी किया, पर उत्तराधिकार फिर भी पिता से पुत्र को जाता था। उनके दानों ने दी गई भूमि को राजकीय अधिकारियों और सैनिकों के प्रवेश से मुक्त किया, जो उन भूमि-दानों का प्रारंभिक रूप था जो बाद में बहुत फैले। "
  "कथन 3 गलत है: सातवाहन अभिलेख प्राकृत में हैं, शकों के समकालीन जूनागढ़ अभिलेख की संस्कृत के विपरीत।",
  US, "ancient-satavahanas-matronymics-grants", craft="linkage")

S(ANC, "medium", "Consider the following statements about the Upanishads and the Vedangas:",
  "उपनिषदों और वेदांगों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Upanishads, called the Vedanta, turned from ritual to questions about the self and ultimate reality.",
   "Their teaching that the self (atman) is one with brahman made knowledge, rather than sacrifice, the path to liberation.",
   "The six Vedangas were auxiliary disciplines for reciting, understanding and performing the Vedas correctly."],
  ["वेदांत कहलाने वाले उपनिषद कर्मकांड से हटकर आत्म और परम सत्य के प्रश्नों की ओर मुड़े।",
   "आत्मा के ब्रह्म से एक होने की उनकी शिक्षा ने यज्ञ के बजाय ज्ञान को मोक्ष का मार्ग बनाया।",
   "छह वेदांग वेदों के सही पाठ, अर्थ और अनुष्ठान के लिए सहायक विद्याएँ थे।"],
  C3, 2,
  "All three are correct, and they show one shift in Vedic thought. The Upanishads, the last layer of the Vedic texts, asked what lies behind the world and the self, and answered that atman and brahman are one; liberation came from realising this, so knowledge outranked ritual -- a change that set the stage for later philosophy and for the questioning of sacrifice by the Buddha and Mahavira. "
  "The Vedangas, by contrast, served the ritual tradition: phonetics, metre and grammar for correct recitation, etymology for meaning, and ritual and astronomy for correct performance at the right time.",
  "तीनों कथन सही हैं, और वैदिक चिंतन के एक बदलाव को दिखाते हैं। वैदिक ग्रंथों की अंतिम परत, उपनिषदों, ने पूछा कि संसार और आत्म के पीछे क्या है, और उत्तर दिया कि आत्मा और ब्रह्म एक हैं; मोक्ष इसके बोध से आता था, इसलिए ज्ञान कर्मकांड से ऊपर हुआ, एक ऐसा बदलाव जिसने बाद के दर्शन और बुद्ध तथा महावीर द्वारा यज्ञ पर उठाए प्रश्नों की भूमिका बनाई। "
  "इसके विपरीत वेदांग कर्मकांडी परंपरा के सहायक थे: सही पाठ के लिए शिक्षा, छंद और व्याकरण, अर्थ के लिए निरुक्त, और सही समय पर सही अनुष्ठान के लिए कल्प और ज्योतिष।",
  RS, "ancient-upanishads-vedangas", craft="linkage")

# ================================================================ TAGS for the 50 kept rows (Test 21's 6 are tagged already)
TAGS = {
 "ancient-ancient-modern-names-pairs": "recall", "ancient-dynasties-regions-pairs": "recall", "ancient-vedas-contents-pairs": "recall",
 "ancient-buddhist-councils-presiding-pairs": "recall", "ancient-rulers-titles-pairs": "recall", "ancient-texts-authors-pairs": "recall",
 "ancient-dynasties-capitals-pairs": "recall", "ancient-learning-centres-states-pairs": "recall", "ancient-ports-regions-pairs": "recall",
 "ancient-texts-religions-pairs": "recall",
 "ancient-dhamek-stupa-sarnath": "recall", "ancient-taxila-gandhara": "recall", "ancient-tirthankara-meaning": "recall",
 "ancient-tirukkural-tamil-veda": "recall", "ancient-vedanga-jyotisha": "precision", "ancient-magadha-dynasties-chronology": "precision",
 "ancient-mauryan-officials-sannidhata": "precision", "ancient-sulba-sutras-geometry": "recall", "ancient-ashvaghosha-buddhacharita": "recall",
 "ancient-bindusara-mauryan-empire": "recall", "ancient-buddha-first-sermon-isipatana": "recall", "ancient-gautamiputra-satakarni-nahapana": "recall",
 "ancient-mehrauli-pillar-chandra": "recall", "ancient-nagarjuna-madhyamaka": "recall", "ancient-nalanda-university-founding": "recall",
 "ancient-navaratnas-tradition": "recall", "ancient-periplus-indo-roman-trade": "recall", "ancient-saka-era-kanishka": "recall",
 "ancient-silappadikaram-sangam-literature": "recall",
 "ancient-kalidasa-works": "recall", "ancient-tripitaka": "recall", "ancient-tamil-epics-sangam": "recall",
 "ancient-gandhara-mathura-amaravati-schools": "precision", "ancient-gupta-coinage-trade": "precision", "ancient-gupta-literature": "precision",
 "ancient-inscriptions-eran-maski-rabatak": "precision", "ancient-jain-philosophy": "precision", "ancient-kalinga-war-edicts": "precision",
 "ancient-mauryan-art-pillars": "precision", "ancient-mauryan-decline-shunga": "precision", "ancient-nbpw-pgw-punch-marked": "precision",
 "ancient-sangam-polity-economy": "precision", "ancient-arthashastra-mauryan-administration": "precision", "ancient-ashoka-dhamma": "precision",
 "ancient-ashokan-edicts-script": "precision", "ancient-gupta-administration": "precision", "ancient-later-vedic-economy-society": "precision",
 "ancient-pallava-chalukya-architecture": "precision", "ancient-rig-veda-structure": "precision", "ancient-sarnath-lion-capital": "precision"}

if __name__ == "__main__":
    write_updates("upg_l2_t06_ancient_b.sql", statuses=("draft", "published"), tags=TAGS)
