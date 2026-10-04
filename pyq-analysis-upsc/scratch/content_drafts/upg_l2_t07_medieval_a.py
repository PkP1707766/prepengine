# -*- coding: utf-8 -*-
"""Level 2 · Test 7 (History 3: Medieval India) -- depth audit of 2026-10-04, part A: pairs and MCQs
(docs/upsc-question-design-standard.md §6). Part B (upg_l2_t07_medieval_b.py) has the statement rows and
the tags for the kept rows.

Before the audit the test had analytic 0, precision 21, recall 82. Part A rewrites 18 rows in place with
the same concept id, type and difficulty:
  - the Sufi terms pairs row now asks what each term shows about Sufi practice;
  - 16 MCQs now ask why something happened or what a source shows: the Chola economy, the Humayun-nama,
    Mirabai, Razia's fall, Tulsidas's Awadhi, the Futuhat, Hughli, the Tuhfat-ul-Mujahidin, Barani,
    Firuz's pillars, the langar, a hundi, Malik Ambar, Nadir Shah, the Persian translations, Siri;
  - the saint-poets pairs row stays recall but drops Tulsidas, whom the Awadhi MCQ's stem names with his
    work.
Leaks avoided while drafting:
  - the iqta paid 'instead of cash' (answers the iqta MCQ) and Daulatabad as a capital (answers the
    Muhammad bin Tughlaq row);
  - Barani as a theorist of kingship (answers the chronicles pairs row);
  - Jesuits at Akbar's court (answers the Ibadat Khana row);
  - the year of Nadir Shah's invasion (answers the eighteenth-century row)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write_updates, CODE
from polity_common import C3, C4, T2

d.SUBJECT = "History"
d.REQUIRE_CRAFT = True
MED = "Medieval"
SC_ = "Satish Chandra, History of Medieval India (Orient BlackSwan)"
NC7 = "NCERT Class VII, Our Pasts II"
NCM = "NCERT Class XII, Themes in Indian History"

# ================================================================ PAIRS (2)
P(MED, "medium", "Consider the following pairs of Sufi terms and what they show about Sufi practice:",
  "निम्नलिखित सूफ़ी शब्दों और उनसे सूफ़ी आचरण के बारे में मिलने वाली जानकारी के युग्मों पर विचार कीजिए:",
  ["Sama, the audition of music and poetry : The Chishtis' use of music as a path to spiritual ecstasy",
   "Urs, the death anniversary of a saint : A celebration of the saint's union with God",
   "Silsila, a chain of masters and disciples : A line of spiritual descent going back to the founder of the order",
   "Tariqa, the 'path' : The body of law that the Sultan's courts applied"],
  ["समा, संगीत और काव्य का श्रवण : आध्यात्मिक आनंद के मार्ग के रूप में चिश्तियों द्वारा संगीत का उपयोग",
   "उर्स, किसी संत की पुण्यतिथि : ईश्वर से संत के मिलन का उत्सव",
   "सिलसिला, गुरुओं और शिष्यों की कड़ी : संप्रदाय के संस्थापक तक जाने वाली आध्यात्मिक वंश-परंपरा",
   "तरीक़ा, 'मार्ग' : वह क़ानून जिसे सुल्तान की अदालतें लागू करती थीं"],
  2,
  "Three pairs are correct. The Chishtis held sama gatherings, where music and verse were meant to stir love of God; the qawwali grew out of them. The urs (literally 'wedding') marks the day the saint's soul was united with God, which is why it is celebrated rather than mourned. Each Sufi order traced its silsila, from master to disciple, back to its founder and beyond. "
  "Pair 4 is wrong: the tariqa is the Sufi's inner path, and the word also came to mean an order; the law applied by the qazis was the sharia.",
  "तीन युग्म सही हैं। चिश्ती समा की महफ़िलें करते थे, जिनमें संगीत और काव्य ईश्वर-प्रेम जगाने के लिए थे; क़व्वाली इन्हीं से निकली। उर्स (शाब्दिक अर्थ 'विवाह') उस दिन को मनाता है जब संत की आत्मा ईश्वर से मिली, इसीलिए इसमें शोक नहीं, उत्सव होता है। हर सूफ़ी संप्रदाय अपना सिलसिला गुरु से शिष्य तक, अपने संस्थापक और उससे आगे तक जोड़ता था। "
  "युग्म 4 गलत है: तरीक़ा सूफ़ी का आंतरिक मार्ग है, और यह शब्द संप्रदाय के अर्थ में भी आने लगा; क़ाज़ियों द्वारा लागू क़ानून शरिया था।",
  NCM, "medieval-sufi-terms-pairs", craft="linkage")

P(MED, "medium", "Consider the following pairs of saint-poets and their works:",
  "निम्नलिखित संत-कवियों और उनकी रचनाओं के युग्मों पर विचार कीजिए:",
  ["Kabir : Bijak",
   "Malik Muhammad Jayasi : Padmavat",
   "Surdas : Sursagar",
   "Raskhan : Kitab-i-Nauras"],
  ["कबीर : बीजक",
   "मलिक मुहम्मद जायसी : पद्मावत",
   "सूरदास : सूरसागर",
   "रसखान : किताब-ए-नौरस"],
  2,
  "Three pairs are correct. The Bijak is the Kabirpanthi collection of Kabir's verses; the Padmavat (1540), by the Sufi poet Malik Muhammad Jayasi, tells the story of Ratansen and Padmavati as an allegory of the soul's search for God; and Surdas's Sursagar sings of Krishna's childhood in Braj Bhasha. "
  "Pair 4 is wrong: Raskhan, a Muslim devotee of Krishna, wrote verses in Braj such as the Sujan Raskhan. The Kitab-i-Nauras, a book of songs in Dakhni, is by Ibrahim Adil Shah II of Bijapur.",
  "तीन युग्म सही हैं। बीजक कबीर के पदों का कबीरपंथी संग्रह है; सूफ़ी कवि मलिक मुहम्मद जायसी का पद्मावत (1540) रत्नसेन और पद्मावती की कथा को ईश्वर की खोज में आत्मा के रूपक के रूप में कहता है; और सूरदास का सूरसागर ब्रजभाषा में कृष्ण के बचपन का गान करता है। "
  "युग्म 4 गलत है: कृष्ण के मुसलमान भक्त रसखान ने सुजान रसखान जैसी ब्रज रचनाएँ लिखीं। दक्खिनी गीतों की पुस्तक किताब-ए-नौरस बीजापुर के इब्राहीम आदिल शाह द्वितीय की है।",
  SC_, "medieval-saint-poets-works-pairs", craft="recall")

# ================================================================ MCQs (16)
M(MED, "easy", "The Chola kingdom's power rested above all on:",
  "चोल राज्य की शक्ति सबसे अधिक किस पर टिकी थी?",
  ["the irrigated rice fields of the Kaveri delta, which fed many people, temples and armies",
   "the gold mines of the Kolar region, which paid for a large army of mercenaries from abroad",
   "control of the overland trade routes to Central Asia through the north-west",
   "the tribute paid to it by the Rashtrakutas, whom it had made its vassals early on"],
  ["कावेरी डेल्टा के सिंचित धान के खेतों पर, जो बहुत लोगों, मंदिरों और सेनाओं का पेट भरते थे",
   "कोलार क्षेत्र की सोने की खानों पर, जिनसे विदेशी भाड़े के सैनिकों की बड़ी सेना का ख़र्च चलता था",
   "उत्तर-पश्चिम से होकर मध्य एशिया जाने वाले स्थल व्यापार मार्गों के नियंत्रण पर",
   "राष्ट्रकूटों द्वारा दिए जाने वाले कर पर, जिन्हें उसने आरंभ में ही अपना सामंत बना लिया था"],
  0,
  "The Cholas rose from the fertile Kaveri delta around Uraiyur and later Thanjavur. Canals, tanks and the Grand Anicut on the Kaveri, attributed to the early Chola Karikala, supported intensive rice farming, and the surplus maintained a dense population, great temples that were also centres of economic life, and the armies and navy of Rajaraja I and Rajendra I. "
  "The Cholas were never vassals collecting tribute from the Rashtrakutas; the Rashtrakuta Krishna III in fact defeated them at Takkolam in 949.",
  "चोल उपजाऊ कावेरी डेल्टा में उरैयूर और बाद में तंजावुर के आसपास से उभरे। नहरों, तालाबों और कावेरी पर प्रारंभिक चोल करिकाल को श्रेय दिए जाने वाले ग्रैंड एनीकट ने गहन धान-खेती को सहारा दिया, और अधिशेष से घनी आबादी, आर्थिक जीवन के केंद्र भी रहे बड़े मंदिर, और राजराज प्रथम तथा राजेंद्र प्रथम की सेनाएँ और नौसेना चलती थीं। "
  "चोल कभी राष्ट्रकूटों से कर वसूलने वाले नहीं थे; वास्तव में राष्ट्रकूट कृष्ण तृतीय ने 949 में तक्कोलम में उन्हें हराया।",
  SC_, "medieval-chola-kaveri-delta", craft="linkage")

M(MED, "easy", "The Humayun-nama, written by Babur's daughter Gulbadan Begum at Akbar's request, is valued by historians mainly because it:",
  "अकबर के आग्रह पर बाबर की पुत्री गुलबदन बेगम द्वारा लिखा गया हुमायूँनामा इतिहासकारों के लिए मुख्यतः इसलिए मूल्यवान है कि यह:",
  ["gives a rare view of Mughal family life in years of struggle, from a woman of the household",
   "is the official chronicle of Humayun's reign, compiled by court historians from state records",
   "records the debates held in Akbar's Ibadat Khana in great detail",
   "describes the Mughal conquest of the Deccan sultanates under Aurangzeb in great detail"],
  ["संघर्ष के वर्षों में मुग़ल पारिवारिक जीवन की दुर्लभ झलक घर की एक महिला की नज़र से देता है",
   "हुमायूँ के शासन का आधिकारिक इतिहास है, जिसे दरबारी इतिहासकारों ने राजकीय अभिलेखों से संकलित किया",
   "अकबर के इबादतख़ाने की बहसों का विस्तार से विवरण देता है",
   "औरंगज़ेब के समय दक्कन सल्तनतों की मुग़ल विजय का विस्तार से वर्णन करता है"],
  0,
  "Gulbadan, Humayun's half-sister, wrote from memory about the family's life through Humayun's defeats, flight and exile -- marriages, quarrels among the brothers, journeys and the women of the haram -- in a plain Persian quite unlike the official histories. That makes it a rare source on the Mughal household and on women's lives at court. "
  "The official history of Akbar's reign is Abul Fazl's Akbarnama, and the Humayun-nama ends long before Aurangzeb.",
  "हुमायूँ की सौतेली बहन गुलबदन ने हुमायूँ की पराजयों, पलायन और निर्वासन के दौरान परिवार के जीवन के बारे में स्मृति से लिखा, जैसे विवाह, भाइयों के झगड़े, यात्राएँ और हरम की स्त्रियाँ, और वह भी आधिकारिक इतिहासों से बिल्कुल अलग सरल फ़ारसी में। इसीलिए यह मुग़ल घराने और दरबार में स्त्रियों के जीवन पर दुर्लभ स्रोत है। "
  "अकबर के शासन का आधिकारिक इतिहास अबुल फ़ज़ल का अकबरनामा है, और हुमायूँनामा औरंगज़ेब से बहुत पहले समाप्त हो जाता है।",
  NCM, "medieval-humayun-nama-gulbadan", craft="linkage")

M(MED, "easy", "Mirabai, a Rajput princess married into the royal family of Mewar, defied her in-laws to devote herself to Krishna. Her life is often read as showing that bhakti:",
  "मेवाड़ के राजपरिवार में ब्याही राजपूत राजकुमारी मीराबाई ने अपने ससुराल वालों की अवहेलना कर स्वयं को कृष्ण को समर्पित किया। उनके जीवन को प्रायः इस रूप में पढ़ा जाता है कि भक्ति:",
  ["gave some women a way to assert their own choices against family and caste",
   "was open only to the Brahmana men who controlled the temples and the scriptures",
   "required its followers to give up family life altogether and live in monasteries",
   "was promoted by the Rajput courts as a state religion that all subjects had to follow"],
  ["ने कुछ स्त्रियों को परिवार और जाति के विरुद्ध अपनी पसंद जताने का रास्ता दिया",
   "केवल उन ब्राह्मण पुरुषों के लिए खुली थी जो मंदिरों और शास्त्रों पर नियंत्रण रखते थे",
   "अपने अनुयायियों से पारिवारिक जीवन पूरी तरह छोड़कर मठों में रहने की अपेक्षा करती थी",
   "को राजपूत दरबारों ने राजधर्म के रूप में बढ़ावा दिया जिसका पालन सभी प्रजा को करना था"],
  0,
  "Mirabai regarded Krishna as her true husband, refused the restraints placed on a royal widow, and is said to have taken a teacher from a caste thought to be low; her songs, in Rajasthani and Braj, were carried by ordinary people rather than by the court. "
  "Bhakti did not require renunciation -- most saints were householders or wandering singers -- and it spread among people of every caste in their own languages, often against the wishes of courts and priests.",
  "मीराबाई कृष्ण को अपना सच्चा पति मानती थीं, उन्होंने राजघराने की विधवा पर लगाई गई बंदिशें नहीं मानीं, और कहा जाता है कि उन्होंने निम्न मानी जाने वाली जाति के गुरु को अपनाया; राजस्थानी और ब्रज में उनके गीत दरबार ने नहीं, आम लोगों ने आगे बढ़ाए। "
  "भक्ति में संन्यास आवश्यक नहीं था, अधिकांश संत गृहस्थ या घूमते गायक थे, और यह हर जाति के लोगों में उनकी अपनी भाषाओं में, प्रायः दरबारों और पुरोहितों की इच्छा के विरुद्ध, फैली।",
  NC7, "medieval-mirabai-krishna", craft="inference")

M(MED, "easy", "Razia, daughter of Iltutmish, was deposed in 1240, within four years of coming to the throne. Which one of the following best explains her fall?",
  "इल्तुतमिश की पुत्री रज़िया को सिंहासन पर बैठने के चार वर्ष के भीतर 1240 में हटा दिया गया। निम्नलिखित में से कौन-सा उनके पतन की सबसे अच्छी व्याख्या करता है?",
  ["The Turkish nobles resented a woman ruling on her own and her favour to outsiders like Yaqut",
   "She was defeated by a Mongol army that captured and sacked Delhi",
   "She was defeated by the Rajputs of Ranthambhor and lost her whole treasury and most of her army",
   "The ulema declared that the throne must pass to Balban, who was then the senior noble at court"],
  ["तुर्क सामंतों को एक स्त्री का स्वतंत्र शासन और याक़ूत जैसे बाहरी लोगों को उसका आगे बढ़ाना अखरता था",
   "उसे एक मंगोल सेना ने हराया जिसने दिल्ली पर क़ब्ज़ा कर उसे लूटा",
   "उसे रणथंभौर के राजपूतों ने हराया और उसका पूरा ख़ज़ाना तथा अधिकांश सेना छिन गई",
   "उलेमा ने घोषणा की कि सिंहासन बलबन को मिलना चाहिए, जो तब दरबार का वरिष्ठ सामंत था"],
  0,
  "Iltutmish had named Razia his heir over his sons, but the Turkish slave-officers who had grown powerful under him wanted a ruler they could control. Razia discarded the veil, held court in public, led her armies on an elephant and promoted men outside their circle, notably the Abyssinian Yaqut; the nobles rose against her, and she was deposed and killed in 1240. "
  "No Mongol army took Delhi then, and Balban came to the throne only in 1266.",
  "इल्तुतमिश ने अपने पुत्रों के ऊपर रज़िया को उत्तराधिकारी चुना था, पर उसके समय शक्तिशाली हुए तुर्क दास-अधिकारी ऐसा शासक चाहते थे जिसे वे नियंत्रित कर सकें। रज़िया ने पर्दा छोड़ा, खुले दरबार लगाए, हाथी पर बैठकर सेना का नेतृत्व किया और उनके घेरे से बाहर के लोगों, विशेषकर हब्शी याक़ूत, को आगे बढ़ाया; सामंतों ने उसके विरुद्ध विद्रोह किया, और 1240 में उसे हटाकर मार दिया गया। "
  "तब किसी मंगोल सेना ने दिल्ली नहीं ली, और बलबन 1266 में ही सिंहासन पर आया।",
  SC_, "medieval-razia-sultan", craft="inference")

M(MED, "easy", "Tulsidas wrote the Ramcharitmanas in Awadhi rather than in Sanskrit. This choice mainly helped to:",
  "तुलसीदास ने रामचरितमानस संस्कृत के बजाय अवधी में लिखा। इस चुनाव ने मुख्यतः किसमें सहायता की?",
  ["carry the story of Rama to ordinary people across north India",
   "win the patronage of the Mughal court, where Awadhi was the official language",
   "make the text acceptable to the Sikh Gurus of the Punjab",
   "restrict the text to the Brahmana scholars of Banaras"],
  ["राम की कथा को पूरे उत्तर भारत के आम लोगों तक पहुँचाने में",
   "मुग़ल दरबार का संरक्षण पाने में, जहाँ अवधी राजभाषा थी",
   "पाठ को पंजाब के सिख गुरुओं के लिए स्वीकार्य बनाने में",
   "पाठ को बनारस के ब्राह्मण विद्वानों तक सीमित रखने में"],
  0,
  "Composed from 1574, the Ramcharitmanas retold the Rama story in Awadhi, the speech of the Ayodhya region, so that people who knew no Sanskrit could hear, sing and stage it; the Ramlila performances of north India still draw on it. "
  "This was the bhakti saints' general method -- composing in the languages of the people. The Mughal court's language was Persian, and Tulsidas worked outside the patronage of courts.",
  "1574 से रचे गए रामचरितमानस ने राम-कथा को अयोध्या क्षेत्र की बोली अवधी में फिर कहा, ताकि संस्कृत न जानने वाले लोग उसे सुन, गा और मंचित कर सकें; उत्तर भारत की रामलीलाएँ आज भी उसी पर आधारित हैं। "
  "यह भक्त संतों का सामान्य तरीक़ा था, यानी लोगों की भाषाओं में रचना करना। मुग़ल दरबार की भाषा फ़ारसी थी, और तुलसीदास दरबारी संरक्षण से बाहर रहकर काम करते थे।",
  NC7, "medieval-tulsidas-awadhi", craft="linkage")

M(MED, "hard", "The Futuhat-i-Firozshahi was written by Firuz Shah Tughlaq himself and lists his measures as acts of piety. Historians therefore treat it mainly as:",
  "फ़ुतूहात-ए-फ़ीरोज़शाही स्वयं फ़ीरोज़ शाह तुग़लक़ ने लिखी और इसमें उसके कार्यों को धर्मपरायणता के कार्यों के रूप में गिनाया गया है। इसलिए इतिहासकार इसे मुख्यतः किस रूप में देखते हैं?",
  ["a statement of how the Sultan wished to be seen, to be checked against other accounts",
   "an impartial record compiled by the court historians from the archives of the Sultanate",
   "a Persian translation of an earlier Sanskrit chronicle of the Delhi Sultans",
   "a Sufi text that the Sultan copied out from the sayings of Nizamuddin Auliya"],
  ["सुल्तान स्वयं को किस रूप में दिखाना चाहता था, इसके कथन के रूप में, जिसे अन्य विवरणों से जाँचना होगा",
   "दरबारी इतिहासकारों द्वारा सल्तनत के अभिलेखागार से संकलित निष्पक्ष विवरण के रूप में",
   "दिल्ली सुल्तानों के किसी पुराने संस्कृत इतिहास के फ़ारसी अनुवाद के रूप में",
   "निज़ामुद्दीन औलिया के कथनों से सुल्तान द्वारा उतारे गए सूफ़ी ग्रंथ के रूप में"],
  0,
  "In this short work, inscribed on a building at Firozabad, Firuz lists the taxes he abolished as not sanctioned by the sharia, the cruel punishments he ended, the buildings he repaired and the towns he founded -- and also, in his own words, measures against new temples. It shows the image of a pious, lawful ruler that he wanted to leave. "
  "Historians weigh it against other accounts, such as those of Barani and Shams-i-Siraj Afif, to see how his policies worked in practice.",
  "फ़ीरोज़ाबाद की एक इमारत पर उत्कीर्ण इस छोटी कृति में फ़ीरोज़ उन करों की सूची देता है जिन्हें उसने शरिया-सम्मत न मानकर हटाया, जिन क्रूर दंडों को समाप्त किया, जिन इमारतों की मरम्मत की और जिन नगरों की स्थापना की, और अपने शब्दों में नए मंदिरों के विरुद्ध कार्रवाई भी। यह एक धर्मपरायण और विधिसम्मत शासक की वह छवि दिखाती है जो वह छोड़ना चाहता था। "
  "इतिहासकार यह देखने के लिए कि उसकी नीतियाँ व्यवहार में कैसे चलीं, इसे बरनी और शम्स-ए-सिराज अफ़ीफ़ जैसे अन्य विवरणों से तौलते हैं।",
  SC_, "medieval-futuhat-i-firozshahi", craft="inference")

M(MED, "hard", "In 1632 Shah Jahan's forces besieged and took the Portuguese settlement of Hughli, after complaints that the Portuguese were raiding for slaves and evading duties. The episode best shows that the Mughals:",
  "1632 में शाहजहाँ की सेना ने हुगली की पुर्तगाली बस्ती को घेरकर ले लिया, इन शिकायतों के बाद कि पुर्तगाली दास बनाने के लिए छापे मार रहे थे और शुल्क से बच रहे थे। यह प्रसंग सबसे अच्छी तरह दिखाता है कि मुग़ल:",
  ["could act decisively against Europeans on land, though they had no navy to match them at sea",
   "had by then made the Portuguese their main allies in the war against the Dutch",
   "expelled all the European trading companies from Bengal for the rest of the seventeenth century",
   "had begun to build a large navy in order to drive the Portuguese out of Goa"],
  ["स्थल पर यूरोपीयों के विरुद्ध निर्णायक कार्रवाई कर सकते थे, यद्यपि समुद्र में उनसे टक्कर लेने वाली नौसेना उनके पास नहीं थी",
   "तब तक पुर्तगालियों को डचों के विरुद्ध युद्ध में अपना मुख्य सहयोगी बना चुके थे",
   "ने सत्रहवीं सदी के शेष भाग के लिए बंगाल से सभी यूरोपीय व्यापारियों को निकाल दिया",
   "ने पुर्तगालियों को गोवा से निकालने के लिए एक बड़ी नौसेना बनानी शुरू कर दी थी"],
  0,
  "The Portuguese at Hughli had built up a trading town in Bengal but were accused of kidnapping people for the slave trade, forcing conversions and avoiding customs. Shah Jahan's governor besieged the town and took it in 1632, and thousands of captives were sent to Agra. "
  "On land the empire was overwhelmingly strong, but at sea the Portuguese -- and later the Dutch and English -- held the advantage, and Mughal pilgrim ships from Surat sailed under Portuguese passes. Other European companies kept trading in Bengal, and the Mughals never built a navy to attack Goa.",
  "हुगली के पुर्तगालियों ने बंगाल में एक व्यापारिक नगर बसाया था, पर उन पर दास-व्यापार के लिए लोगों के अपहरण, जबरन धर्मांतरण और सीमा शुल्क से बचने के आरोप थे। शाहजहाँ के सूबेदार ने नगर को घेरकर 1632 में ले लिया, और हज़ारों बंदी आगरा भेजे गए। "
  "स्थल पर साम्राज्य बहुत शक्तिशाली था, पर समुद्र में पुर्तगालियों, और बाद में डचों तथा अंग्रेज़ों, का पलड़ा भारी था, और सूरत से जाने वाले मुग़ल हज-जहाज़ पुर्तगाली पास लेकर चलते थे। अन्य यूरोपीय कंपनियाँ बंगाल में व्यापार करती रहीं, और मुग़लों ने गोवा पर हमले के लिए कभी नौसेना नहीं बनाई।",
  SC_, "medieval-hughli-portuguese-1632", craft="inference")

M(MED, "hard", "The Tuhfat-ul-Mujahidin, written in Arabic by Zainuddin Makhdum of Ponnani in the late sixteenth century, is valued by historians mainly because it:",
  "सोलहवीं सदी के उत्तरार्ध में पोन्नानी के ज़ैनुद्दीन मख़दूम द्वारा अरबी में लिखी गई तुहफ़त-उल-मुजाहिदीन इतिहासकारों के लिए मुख्यतः इसलिए मूल्यवान है कि यह:",
  ["gives a Malabar Muslim view of the Portuguese attacks on the region's trade and of the resistance to them",
   "is the official chronicle of the Vijayanagara court, compiled by its poets at the command of Krishnadevaraya",
   "records the conquest of Kerala by the Mughal armies sent south by Aurangzeb late in his reign",
   "describes the voyages of Vasco da Gama from the Portuguese side, drawing on the logbooks of his ships"],
  ["पुर्तगालियों द्वारा क्षेत्र के व्यापार पर हमलों और उनके प्रतिरोध पर मालाबार के एक मुसलमान का दृष्टिकोण देती है",
   "कृष्णदेवराय के आदेश से उसके कवियों द्वारा संकलित विजयनगर दरबार का आधिकारिक इतिहास है",
   "औरंगज़ेब द्वारा अपने शासन के अंत में दक्षिण भेजी गई मुग़ल सेनाओं की केरल विजय का वर्णन करती है",
   "जहाज़ों के लॉग-बुक के आधार पर पुर्तगाली पक्ष से वास्को द गामा की यात्राओं का वर्णन करती है"],
  0,
  "Zainuddin Makhdum described how the Portuguese, from the early sixteenth century, sought to control the spice trade of Malabar by force -- burning ships, attacking ports and demanding passes -- and how the Zamorin of Calicut and his naval commanders, the Kunjali Marakkars, resisted them. It is one of the few accounts from the side of the people who suffered the attacks, and it also calls for resistance. "
  "Malabar was never conquered by the Mughals, and Vijayanagara's records are in other languages.",
  "ज़ैनुद्दीन मख़दूम ने बताया कि कैसे सोलहवीं सदी के आरंभ से पुर्तगालियों ने जहाज़ जलाकर, बंदरगाहों पर हमले कर और पास माँगकर बलपूर्वक मालाबार के मसाला व्यापार पर नियंत्रण करना चाहा, और कैसे कालीकट के ज़मोरिन तथा उसके नौसैनिक सेनापतियों, कुंजाली मरक्कारों, ने उनका प्रतिरोध किया। यह हमले झेलने वाले लोगों के पक्ष के गिने-चुने विवरणों में से एक है, और यह प्रतिरोध का आह्वान भी करती है। "
  "मालाबार को मुग़लों ने कभी नहीं जीता, और विजयनगर के अभिलेख अन्य भाषाओं में हैं।",
  SC_, "medieval-tuhfat-ul-mujahidin", craft="linkage")

M(MED, "medium", "Ziauddin Barani's Tarikh-i-Firoz Shahi is a key source for Alauddin Khalji's market controls and Muhammad bin Tughlaq's schemes. Historians nevertheless read it with care mainly because:",
  "ज़ियाउद्दीन बरनी की तारीख़-ए-फ़ीरोज़शाही अलाउद्दीन ख़लजी के बाज़ार नियंत्रण और मुहम्मद बिन तुग़लक़ की योजनाओं का प्रमुख स्रोत है। फिर भी इतिहासकार इसे सावधानी से मुख्यतः इसलिए पढ़ते हैं कि:",
  ["Barani wrote with strong likes and dislikes, and composed much of it long after the events",
   "it was written in Arabic, a language that few of the later scholars of the Sultanate could read",
   "it was compiled at the Mughal court two centuries after the events it describes",
   "Barani was a Mongol captive who never visited Delhi and wrote from hearsay alone"],
  ["बरनी गहरी पसंद-नापसंद के साथ लिखता था, और उसने इसका बड़ा भाग घटनाओं के बहुत बाद रचा",
   "यह अरबी में लिखी गई, जिसे सल्तनत के बाद के कम ही विद्वान पढ़ पाते थे",
   "इसे वर्णित घटनाओं के दो सदी बाद मुग़ल दरबार में संकलित किया गया",
   "बरनी एक मंगोल बंदी था जो कभी दिल्ली नहीं आया और केवल सुनी-सुनाई बातों पर लिखा"],
  0,
  "Barani, a noble who served at Muhammad bin Tughlaq's court and later fell from favour, wrote his history in Persian under Firuz Shah, decades after Alauddin's reign. He gives the fullest account of the price controls and of Muhammad's experiments, but he praised or blamed rulers by whether they upheld the old nobility and religious law as he saw them. "
  "So historians check him against other sources -- Isami, Ibn Battuta, inscriptions and coins -- before accepting his judgements.",
  "बरनी, जो मुहम्मद बिन तुग़लक़ के दरबार में सेवा कर चुका एक सामंत था और बाद में कृपा खो बैठा, ने अलाउद्दीन के शासन के दशकों बाद फ़ीरोज़ शाह के समय फ़ारसी में अपना इतिहास लिखा। वह मूल्य नियंत्रण और मुहम्मद के प्रयोगों का सबसे पूरा विवरण देता है, पर उसने शासकों की प्रशंसा या निंदा इस आधार पर की कि वे उसकी समझ के अनुसार पुराने अभिजात वर्ग और धार्मिक क़ानून को बनाए रखते थे या नहीं। "
  "इसलिए इतिहासकार उसके निर्णय मानने से पहले उसे इसामी, इब्न बतूता, अभिलेखों और सिक्कों जैसे अन्य स्रोतों से जाँचते हैं।",
  SC_, "medieval-barani-tarikh-i-firoz-shahi", craft="inference")

M(MED, "medium", "Firuz Shah Tughlaq had two Ashokan pillars, from Topra and Meerut, carried to Delhi, though no one at his court could read their inscriptions. This suggests that he:",
  "फ़ीरोज़ शाह तुग़लक़ ने टोपरा और मेरठ से अशोक के दो स्तंभ दिल्ली मँगवाए, यद्यपि उसके दरबार में कोई उनके अभिलेख नहीं पढ़ सकता था। इससे संकेत मिलता है कि वह:",
  ["valued them as impressive monuments that added to the glory of his new city",
   "wished to spread Buddhism among his subjects by displaying Ashoka's teachings",
   "believed they recorded the victories of the earlier Sultans of Delhi",
   "wanted their inscriptions read out to settle disputes over land revenue"],
  ["उन्हें ऐसे प्रभावशाली स्मारक मानता था जो उसके नए नगर की शोभा बढ़ाते",
   "अशोक के उपदेश दिखाकर अपनी प्रजा में बौद्ध धर्म फैलाना चाहता था",
   "मानता था कि उनमें दिल्ली के पहले के सुल्तानों की विजयें दर्ज हैं",
   "भू-राजस्व के विवाद सुलझाने के लिए उनके अभिलेख पढ़वाना चाहता था"],
  0,
  "Firuz, a great builder, had the pillars wrapped and moved on specially made carts and boats; one was raised on his palace-citadel, the Firoz Shah Kotla, and the other on the ridge. His chronicler records that no one at court could read the inscriptions, so their value to him lay in their size, antiquity and the prestige of setting them up. "
  "The Brahmi script was deciphered only in 1837, by James Prinsep.",
  "महान निर्माता फ़ीरोज़ ने स्तंभों को लपेटकर विशेष रूप से बनाई गाड़ियों और नावों पर ढुलवाया; एक उसके महल-दुर्ग फ़ीरोज़ शाह कोटला पर और दूसरा रिज पर खड़ा किया गया। उसका इतिहासकार लिखता है कि दरबार में कोई अभिलेख नहीं पढ़ सका, इसलिए उसके लिए उनका मूल्य उनके आकार, प्राचीनता और उन्हें खड़ा करने की प्रतिष्ठा में था। "
  "ब्राह्मी लिपि 1837 में ही जेम्स प्रिंसेप ने पढ़ी।",
  SC_, "medieval-firuz-ashokan-pillars", craft="inference")

M(MED, "medium", "Guru Amar Das insisted that everyone who came to see him, high or low, first eat together in the langar. This practice was meant mainly to:",
  "गुरु अमरदास ने आग्रह किया कि उनसे मिलने आने वाला हर व्यक्ति, ऊँचा हो या नीचा, पहले लंगर में साथ भोजन करे। इस प्रथा का मुख्य उद्देश्य था:",
  ["break down distinctions of caste and status among his followers",
   "raise funds for building the Harmandir Sahib at Amritsar",
   "prepare the Sikhs for military service against the Mughals",
   "honour the Mughal emperor Akbar, who had granted land to the Gurus"],
  ["अपने अनुयायियों में जाति और प्रतिष्ठा के भेद मिटाना",
   "अमृतसर में हरमंदिर साहिब के निर्माण के लिए धन जुटाना",
   "सिखों को मुग़लों के विरुद्ध सैन्य सेवा के लिए तैयार करना",
   "गुरुओं को भूमि देने वाले मुग़ल सम्राट अकबर का सम्मान करना"],
  0,
  "Eating together, seated in rows on the floor, struck at the rules of purity that kept castes from sharing food; by making it a condition of meeting him, Guru Amar Das, the third Guru, turned the langar into a mark of Sikh equality -- tradition holds that Akbar himself ate there. He also organised the followers into 22 manjis under trusted Sikhs and spoke against purdah and sati. "
  "Military organisation came later, under Guru Hargobind.",
  "फ़र्श पर पंक्तियों में बैठकर साथ भोजन करना उन शुद्धता के नियमों पर प्रहार था जो जातियों को साथ खाने से रोकते थे; इसे अपने से मिलने की शर्त बनाकर तीसरे गुरु अमरदास ने लंगर को सिख समानता का चिह्न बना दिया, परंपरा के अनुसार स्वयं अकबर ने वहाँ भोजन किया। उन्होंने अनुयायियों को विश्वसनीय सिखों के अधीन 22 मंजियों में भी संगठित किया और पर्दा तथा सती के विरुद्ध बोले। "
  "सैन्य संगठन बाद में गुरु हरगोबिंद के समय आया।",
  SC_, "medieval-guru-amar-das-manji", craft="linkage")

M(MED, "medium", "A merchant in Surat wanted to pay a supplier in Agra without sending coins along the road. He would most likely have used:",
  "सूरत का एक व्यापारी आगरा के एक आपूर्तिकर्ता को सड़क पर सिक्के भेजे बिना भुगतान करना चाहता था। वह सबसे अधिक संभावना से किसका उपयोग करता?",
  ["a hundi bought from a sarraf, payable at Agra",
   "a dastak issued by the English East India Company",
   "a jagir assigned to him by the Mughal emperor",
   "a farman exempting him from the inland customs duties"],
  ["किसी सर्राफ़ से ली गई हुंडी का, जो आगरा में देय हो",
   "अंग्रेज़ ईस्ट इंडिया कंपनी द्वारा जारी दस्तक का",
   "मुग़ल सम्राट द्वारा उसे दी गई जागीर का",
   "आंतरिक सीमा शुल्क से छूट देने वाले फ़रमान का"],
  0,
  "A hundi was a written order by which a banker (sarraf or shroff) in one city promised payment by his agent or correspondent in another, after a set time; it could be bought, sold, discounted and passed on, much like a bill of exchange, and it spared merchants the risk of carrying cash across the country. European travellers such as Tavernier admired the system. "
  "A dastak was a trade permit, a jagir an assignment of revenue to an officer, and a farman a royal order.",
  "हुंडी एक लिखित आदेश था जिससे एक नगर का साहूकार (सर्राफ़ या श्रॉफ़) तय समय बाद दूसरे नगर में अपने एजेंट या प्रतिनिधि द्वारा भुगतान का वचन देता था; इसे ख़रीदा, बेचा, भुनाया और आगे सौंपा जा सकता था, लगभग विनिमय-पत्र की तरह, और इससे व्यापारी देश भर में नक़दी ढोने के जोखिम से बचते थे। टैवर्नियर जैसे यूरोपीय यात्रियों ने इस व्यवस्था की प्रशंसा की। "
  "दस्तक व्यापार का अनुमति-पत्र, जागीर किसी अधिकारी को राजस्व का आवंटन, और फ़रमान शाही आदेश था।",
  SC_, "medieval-hundi", craft="application")

M(MED, "medium", "Malik Ambar, regent of Ahmadnagar, held off the Mughals for about two decades in the early seventeenth century. This was largely because he:",
  "अहमदनगर के संरक्षक मलिक अंबर ने सत्रहवीं सदी के आरंभ में लगभग दो दशक तक मुग़लों को रोके रखा। यह मुख्यतः इसलिए संभव हुआ कि उसने:",
  ["used Maratha light cavalry for guerrilla war and won the peasants with a fair revenue system",
   "had the support of a Portuguese fleet that cut off the supplies of the Mughal armies by sea",
   "made an alliance with the Safavid Shah of Persia, who sent an army to help him in the Deccan",
   "built a chain of forts manned by European gunners across the Deccan"],
  ["मराठा हल्की घुड़सवार सेना से छापामार युद्ध किया और न्यायसंगत राजस्व व्यवस्था से किसानों को अपने साथ रखा",
   "पुर्तगाली बेड़े का समर्थन पाया जिसने समुद्र से मुग़ल सेनाओं की रसद काट दी",
   "फ़ारस के सफ़वी शाह से गठबंधन किया, जिसने दक्कन में सेना भेजी",
   "पूरे दक्कन में यूरोपीय तोपचियों वाले क़िलों की शृंखला बनाई"],
  0,
  "Malik Ambar, an Ethiopian brought to India as a slave, rose to lead the Nizam Shahi state and fought Jahangir's armies with Maratha horsemen who struck at their supply lines and avoided pitched battles -- the bargi-giri that the Marathas later perfected. His revenue settlement, based on a survey of the land and fixed in cash, won the cultivators' confidence and was later adapted by the Mughals in the Deccan. "
  "He founded Khirki, later renamed Aurangabad.",
  "दास के रूप में भारत लाए गए इथियोपियाई मलिक अंबर निज़ामशाही राज्य का नेतृत्व करने लगे और जहाँगीर की सेनाओं से ऐसे मराठा घुड़सवारों के साथ लड़े जो उनकी रसद-लाइनों पर वार करते और आमने-सामने की लड़ाई से बचते थे, यानी वही बर्गी-गीरी जिसे बाद में मराठों ने निखारा। भूमि-सर्वेक्षण पर आधारित और नक़द में तय उसके राजस्व बंदोबस्त ने किसानों का विश्वास जीता, और बाद में मुग़लों ने दक्कन में उसे अपनाया। "
  "उसने खिड़की बसाया, जिसका नाम बाद में औरंगाबाद रखा गया।",
  SC_, "medieval-malik-ambar-ahmadnagar", craft="linkage")

M(MED, "medium", "Nadir Shah of Persia defeated the Mughal army at Karnal and sacked Delhi, carrying off the Peacock Throne. The invasion mattered mainly because it:",
  "फ़ारस के नादिर शाह ने करनाल में मुग़ल सेना को हराया और दिल्ली को लूटकर तख़्त-ए-ताऊस ले गया। यह आक्रमण मुख्यतः इसलिए महत्वपूर्ण था कि इसने:",
  ["exposed the military weakness of the Mughal empire and emptied its treasury",
   "brought the Punjab under Persian rule for the rest of the eighteenth century",
   "ended the Mughal dynasty and placed a Persian prince on the throne of Delhi",
   "led straight to a Maratha occupation of Delhi in the same year"],
  ["मुग़ल साम्राज्य की सैन्य दुर्बलता उजागर कर दी और उसका ख़ज़ाना ख़ाली कर दिया",
   "पंजाब को अठारहवीं सदी के शेष भाग के लिए फ़ारसी शासन में ला दिया",
   "मुग़ल वंश समाप्त कर दिल्ली के सिंहासन पर एक फ़ारसी राजकुमार को बैठा दिया",
   "उसी वर्ष सीधे दिल्ली पर मराठा क़ब्ज़ा करवा दिया"],
  0,
  "After Karnal, Nadir Shah's troops massacred thousands in Delhi, and he left with an enormous treasure, including the Peacock Throne and the Koh-i-Noor. The Mughal emperor Muhammad Shah was left on the throne, but the empire's prestige and finances never recovered, and the governors of the provinces grew still more independent. "
  "Nadir Shah went home and was assassinated in 1747; it was his successor in Afghanistan, Ahmad Shah Abdali, who repeatedly invaded the Punjab.",
  "करनाल के बाद नादिर शाह की सेना ने दिल्ली में हज़ारों लोगों का क़त्लेआम किया, और वह तख़्त-ए-ताऊस और कोहिनूर सहित भारी ख़ज़ाना लेकर गया। मुग़ल सम्राट मुहम्मद शाह सिंहासन पर बना रहा, पर साम्राज्य की प्रतिष्ठा और वित्त कभी नहीं सँभले, और प्रांतों के सूबेदार और भी स्वतंत्र हो गए। "
  "नादिर शाह स्वदेश लौट गया और 1747 में मारा गया; अफ़ग़ानिस्तान में उसका उत्तराधिकारी अहमद शाह अब्दाली था, जिसने बार-बार पंजाब पर आक्रमण किया।",
  SC_, "medieval-peacock-throne-nadir-shah", craft="inference")

M(MED, "medium", "At Akbar's court the Mahabharata, the Ramayana and other Sanskrit works were translated into Persian. This was mainly meant to:",
  "अकबर के दरबार में महाभारत, रामायण और अन्य संस्कृत ग्रंथों का फ़ारसी में अनुवाद किया गया। इसका मुख्य उद्देश्य था:",
  ["make Indian traditions known to Persian-reading nobles and bring his varied subjects closer",
   "replace Persian with Sanskrit as the language of the Mughal court and of its administration",
   "prepare preachers who could convert Hindus to Islam by quoting from their own sacred texts",
   "please the Safavid Shah, who had asked for copies of the Indian epics"],
  ["फ़ारसी पढ़ने वाले अभिजात वर्ग को भारतीय परंपराओं से परिचित कराना और अपनी विविध प्रजा को निकट लाना",
   "मुग़ल दरबार और प्रशासन की भाषा के रूप में फ़ारसी की जगह संस्कृत लाना",
   "ऐसे उपदेशक तैयार करना जो हिंदुओं के अपने ग्रंथ उद्धृत कर उन्हें इस्लाम में ला सकें",
   "सफ़वी शाह को प्रसन्न करना, जिसने भारतीय महाकाव्यों की प्रतियाँ माँगी थीं"],
  0,
  "Akbar set up a translation bureau (maktab khana) at Fatehpur Sikri, where scholars such as Badauni and Faizi, working with Brahmana pandits, produced the illustrated Razmnama ('Book of War') from the Mahabharata, a Persian Ramayana and versions of other works. Abul Fazl's preface explains the aim: to make Indian learning known to the nobility and to remove prejudice. "
  "Persian remained the language of the court, and copies were given to nobles to read.",
  "अकबर ने फ़तेहपुर सीकरी में एक अनुवाद-विभाग (मक़तबख़ाना) बनाया, जहाँ बदायूँनी और फ़ैज़ी जैसे विद्वानों ने ब्राह्मण पंडितों के साथ काम करते हुए महाभारत से सचित्र रज़्मनामा ('युद्ध की पुस्तक'), फ़ारसी रामायण और अन्य ग्रंथों के रूपांतर तैयार किए। अबुल फ़ज़ल की भूमिका उद्देश्य बताती है: अभिजात वर्ग को भारतीय विद्या से परिचित कराना और पूर्वाग्रह दूर करना। "
  "फ़ारसी दरबार की भाषा बनी रही, और प्रतियाँ पढ़ने के लिए सामंतों को दी गईं।",
  SC_, "medieval-razmnama-akbar", craft="linkage")

M(MED, "medium", "Alauddin Khalji built Siri, the second city of Delhi, as a fortified garrison city around 1303. This was mainly to:",
  "अलाउद्दीन ख़लजी ने लगभग 1303 में दिल्ली के दूसरे नगर सीरी को एक क़िलेबंद छावनी-नगर के रूप में बनवाया। इसका मुख्य उद्देश्य था:",
  ["guard the capital against the Mongol raids that reached its outskirts",
   "house the Sufi saints whom he had invited to Delhi from Persia and Central Asia",
   "store the treasure brought back from the south by his generals",
   "replace the old city, which an earthquake had just destroyed"],
  ["राजधानी को उन मंगोल आक्रमणों से बचाना जो उसकी सीमा तक पहुँच जाते थे",
   "फ़ारस और मध्य एशिया से दिल्ली बुलाए गए सूफ़ी संतों को बसाना",
   "उसके सेनापतियों द्वारा दक्षिण से लाए गए ख़ज़ाने को रखना",
   "पुराने नगर की जगह लेना, जिसे अभी-अभी भूकंप ने नष्ट कर दिया था"],
  0,
  "In 1303 a Mongol army camped near Delhi and besieged the Sultan, who was saved only when it withdrew. Alauddin then built Siri as a walled camp for his army, repaired the forts on the route of the invaders and raised a large standing force -- the context in which Barani places his price controls. "
  "Siri was begun before the great southern campaigns brought their treasure, and the older city at Mehrauli remained in use alongside it.",
  "1303 में एक मंगोल सेना ने दिल्ली के पास डेरा डालकर सुल्तान को घेर लिया, जो उसके लौट जाने पर ही बच पाया। तब अलाउद्दीन ने अपनी सेना के लिए दीवारों वाले शिविर के रूप में सीरी बनवाया, आक्रमणकारियों के मार्ग के क़िलों की मरम्मत कराई और एक बड़ी स्थायी सेना खड़ी की; बरनी उसके मूल्य नियंत्रण को इसी संदर्भ में रखता है। "
  "सीरी बड़े दक्षिणी अभियानों के ख़ज़ाना लाने से पहले शुरू हुआ था, और महरौली का पुराना नगर उसके साथ उपयोग में बना रहा।",
  SC_, "medieval-siri-alauddin", craft="linkage")

if __name__ == "__main__":
    write_updates("upg_l2_t07_medieval_a.sql", statuses=("draft", "published"))
