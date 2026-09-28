# -*- coding: utf-8 -*-
"""Level 2 · Test 7 (History 3: Medieval India), part B -- 34 MCQ and pairs rows against the
live gap report: medium MCQ 13, easy MCQ 8, hard MCQ 3, medium pairs 5, easy pairs 3, hard
pairs 2. Planned MCQs on Hemu, the founder of the Lodis and the Kakatiya capital were dropped
because each would have given away a statement in part A (the Humayun, Sultanate-dynasties and
Malik Kafur rows); the Peacock Throne stem does not name Shah Jahan (the Mughal-rulers pairs
row tests it)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import M, P, write

d.SUBJECT = "History"
MD = "Medieval"
SC1 = "Satish Chandra, Medieval India: From Sultanat to the Mughals, Part One (Har-Anand)"
SC2 = "Satish Chandra, Medieval India: From Sultanat to the Mughals, Part Two (Har-Anand)"
NC7 = "NCERT Class VII, Our Pasts II"
NC12 = "NCERT Class XII, Themes in Indian History II"

# ---------------------------------------------------------------- medium MCQs (13)
M(MD, "medium", "The city of Siri, the second city of Delhi, was built by:",
  "दिल्ली का दूसरा नगर सीरी किसने बसाया?",
  ["Alauddin Khalji", "Iltutmish", "Balban", "Firuz Shah Tughlaq"],
  ["अलाउद्दीन ख़िलजी", "इल्तुतमिश", "बलबन", "फ़िरोज़ शाह तुग़लक़"],
  0,
  "Alauddin Khalji built Siri around 1303 as a fortified garrison city to guard against the Mongols, whose raids reached the outskirts of Delhi. The 'seven cities of Delhi' run from Lal Kot and Qila Rai Pithora through Siri, Tughlaqabad, Jahanpanah and Firozabad to Shahjahanabad.",
  "अलाउद्दीन ख़िलजी ने मंगोलों से, जिनके हमले दिल्ली के बाहरी इलाक़ों तक पहुँचते थे, रक्षा के लिए लगभग 1303 में क़िलेबंद छावनी-नगर के रूप में सीरी बसाया। 'दिल्ली के सात नगर' लाल कोट और क़िला राय पिथौरा से सीरी, तुग़लक़ाबाद, जहाँपनाह और फ़िरोज़ाबाद होते हुए शाहजहानाबाद तक जाते हैं।",
  f"{SC1}, chapter 5.",
  "medieval-siri-alauddin")

M(MD, "medium", "The 'Tarikh-i-Firoz Shahi', a history of the Delhi Sultans down to the early years of Firuz Shah Tughlaq, was written by:",
  "फ़िरोज़ शाह तुग़लक़ के आरंभिक वर्षों तक दिल्ली सुल्तानों का इतिहास 'तारीख़-ए-फ़िरोज़शाही' किसने लिखा?",
  ["Ziauddin Barani", "Minhaj-us-Siraj", "Amir Khusrau", "Abdul Malik Isami"],
  ["ज़ियाउद्दीन बरनी", "मिनहाज-उस-सिराज", "अमीर ख़ुसरो", "अब्दुल मलिक इसामी"],
  0,
  "Ziauddin Barani's Tarikh-i-Firoz Shahi covers the Sultanate from Balban to Firuz and is a key, if opinionated, source for Alauddin's market reforms and Muhammad bin Tughlaq's schemes. "
  "A different chronicler, Shams-i-Siraj Afif, wrote another 'Tarikh-i-Firoz Shahi' about Firuz's own reign -- one reason this is a trap-prone title; Minhaj wrote the earlier Tabaqat-i-Nasiri and Isami the verse Futuh-us-Salatin.",
  "ज़ियाउद्दीन बरनी की तारीख़-ए-फ़िरोज़शाही बलबन से फ़िरोज़ तक सल्तनत का इतिहास है और अलाउद्दीन के बाज़ार-सुधारों तथा मुहम्मद बिन तुग़लक़ की योजनाओं का, भले ही मत-प्रधान, मुख्य स्रोत है। "
  "एक दूसरे इतिहासकार, शम्स-ए-सिराज अफ़ीफ़, ने फ़िरोज़ के अपने शासन पर एक और 'तारीख़-ए-फ़िरोज़शाही' लिखी; इसीलिए यह शीर्षक जाल बनाता है; मिनहाज ने पहले की तबक़ात-ए-नासिरी और इसामी ने पद्य में फ़ुतूह-उस-सलातीन लिखी।",
  f"{SC1}, introduction on sources.",
  "medieval-barani-tarikh-i-firoz-shahi")

M(MD, "medium", "The Mughal 'Peacock Throne' was carried off from Delhi by:",
  "मुग़ल 'मयूर सिंहासन' को दिल्ली से कौन ले गया?",
  ["Nadir Shah", "Ahmad Shah Abdali", "Timur", "Mahmud of Ghazni"],
  ["नादिर शाह", "अहमद शाह अब्दाली", "तैमूर", "महमूद ग़ज़नवी"],
  0,
  "After defeating the Mughal army at Karnal, Nadir Shah of Persia occupied Delhi, ordered a massacre and carried away enormous wealth, including the jewelled Peacock Throne and the Koh-i-Noor diamond. His invasion exposed the weakness of the later Mughals. Ahmad Shah Abdali, once Nadir's officer, raided repeatedly afterwards.",
  "करनाल में मुग़ल सेना को हराने के बाद फ़ारस के नादिर शाह ने दिल्ली पर कब्ज़ा किया, क़त्लेआम का आदेश दिया और जड़ाऊ मयूर सिंहासन तथा कोहिनूर हीरे सहित अपार संपत्ति ले गया। उसके आक्रमण ने बाद के मुग़लों की कमज़ोरी उजागर कर दी। कभी नादिर का अधिकारी रहा अहमद शाह अब्दाली उसके बाद बार-बार आक्रमण करता रहा।",
  f"{SC2}, chapter on the later Mughals.",
  "medieval-peacock-throne-nadir-shah")

M(MD, "medium", "Which one of the following was the principal port of the Chola kingdom?",
  "निम्नलिखित में से कौन-सा चोल राज्य का प्रमुख बंदरगाह था?",
  ["Nagapattinam", "Muziris", "Barygaza (Bharuch)", "Tamralipti"],
  ["नागपट्टिनम", "मुज़िरिस", "भड़ौच (बैरीगाज़ा)", "ताम्रलिप्ति"],
  0,
  "Nagapattinam, on the Coromandel coast near the Kaveri delta, was the Chola kingdom's main outlet for trade with South-East Asia and China; a king of Srivijaya even built a Buddhist monastery there with Rajaraja I's permission. "
  "The distractors are famous ports of other regions and ages: Muziris on the Malabar coast (Chera), Barygaza (Bharuch) at the Narmada's mouth and Tamralipti in Bengal.",
  "कावेरी डेल्टा के पास कोरोमंडल तट पर नागपट्टिनम दक्षिण-पूर्व एशिया और चीन के साथ व्यापार के लिए चोल राज्य का मुख्य द्वार था; श्रीविजय के एक राजा ने राजराज प्रथम की अनुमति से वहाँ एक बौद्ध विहार भी बनवाया। "
  "गलत विकल्प दूसरे क्षेत्रों और युगों के प्रसिद्ध बंदरगाह हैं: मालाबार तट पर मुज़िरिस (चेर), नर्मदा के मुहाने पर भड़ौच और बंगाल में ताम्रलिप्ति।",
  f"{NC7} -- New Kings and Kingdoms; Upinder Singh, A History of Ancient and Early Medieval India, chapter 11.",
  "medieval-chola-port-nagapattinam")

M(MD, "medium", "The city of Ahmedabad was founded in 1411 by:",
  "अहमदाबाद नगर की स्थापना 1411 में किसने की?",
  ["Ahmad Shah I", "Bahadur Shah", "Muzaffar Shah I", "Qutb-ud-din Ahmad Shah"],
  ["अहमद शाह प्रथम", "बहादुर शाह", "मुज़फ़्फ़र शाह प्रथम", "क़ुतुबुद्दीन अहमद शाह"],
  0,
  "Ahmad Shah I, grandson of Muzaffar Shah I (who had declared Gujarat independent of Delhi), founded Ahmedabad on the Sabarmati as his new capital; its mosques, with their fusion of Islamic plans and Gujarati temple carving, are now part of a World Heritage city. All four options are Sultans of Gujarat, which is the trap.",
  "मुज़फ़्फ़र शाह प्रथम (जिन्होंने गुजरात को दिल्ली से स्वतंत्र घोषित किया था) के पौत्र अहमद शाह प्रथम ने साबरमती के किनारे अपनी नई राजधानी के रूप में अहमदाबाद बसाया; इस्लामी योजना और गुजराती मंदिर-नक्काशी के मेल वाली इसकी मस्जिदें आज एक विश्व धरोहर नगर का भाग हैं। चारों विकल्प गुजरात के सुल्तान हैं, और यही जाल है।",
  f"{SC1}, chapter on regional kingdoms; UNESCO -- Historic City of Ahmadabad.",
  "medieval-ahmedabad-ahmad-shah")

M(MD, "medium", "The administration of the Ahom kingdom rested largely on:",
  "अहोम राज्य का प्रशासन मुख्य रूप से किस पर आधारित था?",
  ["The paik system of compulsory service", "The iqta system", "The mansabdari system", "The ryotwari system of direct settlement with each cultivator"],
  ["अनिवार्य सेवा की पाइक व्यवस्था", "इक़्ता व्यवस्था", "मनसबदारी व्यवस्था", "हर कृषक के साथ सीधे बंदोबस्त की रैयतवाड़ी व्यवस्था"],
  0,
  "Under the Ahom paik system, every adult male (paik) owed the state labour and military service for part of the year, in return for a plot of land; paiks were grouped into khels under officers. It gave the kingdom the manpower for its armies and public works, and its breakdown in the 18th century weakened the state. The other options belong to the Sultanate, the Mughals and the British.",
  "अहोम पाइक व्यवस्था में हर वयस्क पुरुष (पाइक) भूमि के एक टुकड़े के बदले वर्ष के कुछ भाग में राज्य को श्रम और सैन्य सेवा देता था; पाइकों को अधिकारियों के अधीन खेलों में संगठित किया जाता था। इससे राज्य को सेना और सार्वजनिक कार्यों के लिए जनशक्ति मिलती थी, और 18वीं सदी में इसके टूटने से राज्य कमज़ोर हुआ। दूसरे विकल्प सल्तनत, मुग़लों और अंग्रेज़ों के हैं।",
  f"{NC7} -- Tribes, Nomads and Settled Communities.",
  "medieval-ahom-paik-system")

M(MD, "medium", "Which Delhi Sultan had two Ashokan pillars, from Topra and Meerut, brought to Delhi?",
  "किस दिल्ली सुल्तान ने टोपरा और मेरठ से दो अशोक-स्तंभ दिल्ली मँगवाए?",
  ["Firuz Shah Tughlaq", "Alauddin Khalji", "Ghiyasuddin Tughlaq", "Sikandar Lodi"],
  ["फ़िरोज़ शाह तुग़लक़", "अलाउद्दीन ख़िलजी", "ग़यासुद्दीन तुग़लक़", "सिकंदर लोदी"],
  0,
  "Firuz Shah, who took a great interest in buildings and antiquities, had the pillars moved on specially built carts and boats; the Topra pillar was set up on his palace-citadel, the Firoz Shah Kotla, where no one could then read its Brahmi script -- it was deciphered only in 1837. He also repaired older monuments such as the Qutb Minar.",
  "इमारतों और प्राचीन वस्तुओं में बड़ी रुचि रखने वाले फ़िरोज़ शाह ने विशेष रूप से बनाई गाड़ियों और नावों से स्तंभों को ले जाया गया; टोपरा स्तंभ उनके महल-क़िले, फ़िरोज़ शाह कोटला, पर खड़ा किया गया, जहाँ तब कोई इसकी ब्राह्मी लिपि नहीं पढ़ सकता था; यह केवल 1837 में पढ़ी गई। उन्होंने क़ुतुब मीनार जैसे पुराने स्मारकों की मरम्मत भी करवाई।",
  f"{SC1}, chapter 7.",
  "medieval-firuz-ashokan-pillars")

M(MD, "medium", "Which Sikh Guru organised the community into 'manjis' (districts) and strengthened the institution of the langar?",
  "किस सिख गुरु ने समुदाय को 'मंजियों' (क्षेत्रों) में संगठित किया और लंगर की संस्था को मज़बूत किया?",
  ["Guru Amar Das", "Guru Angad", "Guru Ram Das", "Guru Har Krishan"],
  ["गुरु अमरदास", "गुरु अंगद", "गुरु रामदास", "गुरु हर कृष्ण"],
  0,
  "Guru Amar Das, the third Guru, set up 22 manjis, each under a devoted follower, to spread the teaching and collect offerings, and insisted that all visitors eat together in the langar before meeting him -- Akbar is said to have done so. He also opposed purdah and sati. Guru Ram Das, his son-in-law, founded Ramdaspur (Amritsar).",
  "तीसरे गुरु, गुरु अमरदास, ने शिक्षा फैलाने और भेंट इकट्ठा करने के लिए 22 मंजियाँ बनाईं, हर एक एक समर्पित अनुयायी के अधीन, और आग्रह किया कि उनसे मिलने से पहले सभी आगंतुक लंगर में साथ भोजन करें; कहा जाता है कि अकबर ने भी ऐसा किया। उन्होंने पर्दा और सती का भी विरोध किया। उनके दामाद गुरु रामदास ने रामदासपुर (अमृतसर) बसाया।",
  f"{SC2}, chapter on the Sikhs.",
  "medieval-guru-amar-das-manji")

M(MD, "medium", "The 'Razmnama', a Persian translation of the Mahabharata, was produced at the court of:",
  "महाभारत का फ़ारसी अनुवाद 'रज़्मनामा' किसके दरबार में तैयार हुआ?",
  ["Akbar", "Humayun", "Jahangir", "Dara Shikoh"],
  ["अकबर", "हुमायूँ", "जहाँगीर", "दारा शिकोह"],
  0,
  "Akbar set up a translation bureau (maktab khana) at Fatehpur Sikri, where scholars including Badauni and Faizi translated the Mahabharata (as the illustrated Razmnama, 'Book of War'), the Ramayana, the Atharva Veda and other works into Persian, to make Indian learning available to the Persian-reading nobility. Dara Shikoh's translations of the Upanishads came later.",
  "अकबर ने फ़तेहपुर सीकरी में एक अनुवाद-विभाग (मक़तब ख़ाना) बनाया, जहाँ बदायूनी और फ़ैज़ी सहित विद्वानों ने महाभारत (सचित्र रज़्मनामा, 'युद्ध की पुस्तक' के रूप में), रामायण, अथर्ववेद और दूसरी रचनाओं का फ़ारसी में अनुवाद किया, ताकि फ़ारसी पढ़ने वाला अभिजात वर्ग भारतीय ज्ञान तक पहुँच सके। दारा शिकोह के उपनिषद-अनुवाद बाद में आए।",
  f"{NC12} -- Kings and Chronicles; {SC2}.",
  "medieval-razmnama-akbar")

M(MD, "medium", "The Treaty of Purandar (1665) was signed between Shivaji and:",
  "पुरंदर की संधि (1665) शिवाजी और किसके बीच हुई?",
  ["Raja Jai Singh of Amber", "Shaista Khan", "The Adil Shahi general Afzal Khan", "Aurangzeb in person"],
  ["आमेर के राजा जय सिंह", "शाइस्ता ख़ाँ", "आदिलशाही सेनापति अफ़ज़ल ख़ाँ", "स्वयं औरंगज़ेब"],
  0,
  "Aurangzeb sent Raja Jai Singh of Amber, who besieged Purandar and forced Shivaji to give up 23 forts and agree to serve the Mughals; Shivaji's visit to Agra in 1666 ended in his famous escape. "
  "Shaista Khan had earlier been surprised by Shivaji's night raid at Pune (1663), and Afzal Khan of Bijapur was killed by Shivaji at Pratapgarh (1659).",
  "औरंगज़ेब ने आमेर के राजा जय सिंह को भेजा, जिन्होंने पुरंदर को घेरकर शिवाजी को 23 क़िले छोड़ने और मुग़लों की सेवा स्वीकार करने पर विवश किया; 1666 में शिवाजी की आगरा यात्रा उनके प्रसिद्ध पलायन पर समाप्त हुई। "
  "शाइस्ता ख़ाँ पहले पुणे में शिवाजी के रात्रि-हमले (1663) से चकित हो चुका था, और बीजापुर के अफ़ज़ल ख़ाँ को शिवाजी ने प्रतापगढ़ (1659) में मार दिया था।",
  f"{SC2}, chapter on the Marathas.",
  "medieval-treaty-of-purandar")

M(MD, "medium", "Malik Ambar, the Abyssinian minister known for his land revenue settlement and guerrilla warfare against the Mughals, served the kingdom of:",
  "मुग़लों के विरुद्ध अपनी भू-राजस्व व्यवस्था और छापामार युद्ध के लिए प्रसिद्ध हब्शी मंत्री मलिक अंबर किस राज्य की सेवा में थे?",
  ["Ahmadnagar", "Golconda", "Bijapur", "Berar (Ellichpur)"],
  ["अहमदनगर", "गोलकोंडा", "बीजापुर", "बरार (एलिचपुर)"],
  0,
  "Malik Ambar, brought to India as a slave from Ethiopia, became the regent of the Nizam Shahi kingdom of Ahmadnagar and held off the Mughals under Jahangir for two decades, using Maratha light cavalry; he founded the town of Khirki, later Aurangabad. His revenue settlement, modelled on Todar Mal's, influenced later Maratha practice.",
  "इथियोपिया से दास के रूप में भारत लाए गए मलिक अंबर अहमदनगर के निज़ामशाही राज्य के संरक्षक बने और मराठा हल्के घुड़सवारों का उपयोग करके दो दशकों तक जहाँगीर के अधीन मुग़लों को रोके रखा; उन्होंने खिड़की नगर बसाया, जो बाद में औरंगाबाद बना। टोडरमल के नमूने पर बनी उनकी राजस्व व्यवस्था ने बाद की मराठा प्रथा को प्रभावित किया।",
  f"{SC2}, chapter on the Deccan.",
  "medieval-malik-ambar-ahmadnagar")

M(MD, "medium", "The 'Gita Govinda', a Sanskrit poem on the love of Radha and Krishna, was composed by:",
  "राधा और कृष्ण के प्रेम पर संस्कृत काव्य 'गीतगोविंद' की रचना किसने की?",
  ["Jayadeva", "Vidyapati", "Chandidas", "Kalidasa"],
  ["जयदेव", "विद्यापति", "चंडीदास", "कालिदास"],
  0,
  "Jayadeva, a 12th-century poet associated with the court of the Sena king Lakshmana Sena of Bengal (and, by Odia tradition, with Puri), wrote the Gita Govinda, whose songs are still sung in the Jagannath temple and inspired centuries of painting and dance. Vidyapati (Maithili) and Chandidas (Bengali) wrote later songs on the same theme -- the natural trap.",
  "12वीं सदी के कवि जयदेव, जिन्हें बंगाल के सेन राजा लक्ष्मण सेन के दरबार से (और ओड़िया परंपरा के अनुसार पुरी से) जोड़ा जाता है, ने गीतगोविंद लिखा, जिसके गीत आज भी जगन्नाथ मंदिर में गाए जाते हैं और जिसने सदियों तक चित्रकला और नृत्य को प्रेरित किया। विद्यापति (मैथिली) और चंडीदास (बांग्ला) ने बाद में इसी विषय पर गीत लिखे; यही स्वाभाविक जाल है।",
  f"{NC7} -- Devotional Paths to the Divine; {SC1}.",
  "medieval-gita-govinda-jayadeva")

M(MD, "medium", "In medieval Indian trade, a 'hundi' was:",
  "मध्यकालीन भारतीय व्यापार में 'हुंडी' क्या थी?",
  ["A bill of exchange used by merchants", "A tax collected on goods carried across a river by boat", "A unit of land measurement", "A Sufi hospice"],
  ["व्यापारियों द्वारा उपयोग किया जाने वाला विनिमय-पत्र", "नाव से नदी पार ले जाए गए माल पर लगने वाला कर", "भूमि मापने की एक इकाई", "एक सूफ़ी ख़ानक़ाह"],
  0,
  "A hundi was a written order to pay a sum of money at another place or after a period; merchants and sarrafs (bankers) used it to move money across long distances without carrying cash, and it could be discounted or passed on, much like a bill of exchange. Bernier and other travellers noted how widely it was used in Mughal India.",
  "हुंडी किसी दूसरे स्थान पर या एक अवधि के बाद कोई राशि चुकाने का लिखित आदेश थी; व्यापारी और सर्राफ़ (साहूकार) इसका उपयोग नकद ले जाए बिना लंबी दूरी तक धन भेजने के लिए करते थे, और इसे विनिमय-पत्र की तरह भुनाया या आगे बढ़ाया जा सकता था। बर्नियर और दूसरे यात्रियों ने लिखा है कि मुग़ल भारत में इसका कितना व्यापक उपयोग था।",
  f"{NC12} -- Peasants, Zamindars and the State; {SC2}, chapter on economy.",
  "medieval-hundi")

# ---------------------------------------------------------------- easy MCQs (8)
M(MD, "easy", "Who was the only woman to rule as Sultan of Delhi?",
  "दिल्ली की सुल्तान के रूप में शासन करने वाली एकमात्र महिला कौन थीं?",
  ["Razia Sultan", "Chand Bibi", "Nur Jahan", "Rani Durgavati"],
  ["रज़िया सुल्तान", "चाँद बीबी", "नूरजहाँ", "रानी दुर्गावती"],
  0,
  "Razia, daughter of Iltutmish, ruled from 1236 to 1240. She discarded the veil, held court in public and rode on an elephant, but the Turkish nobles resented her independence and her promotion of an Abyssinian, Yaqut, and she was deposed and killed. Chand Bibi, Nur Jahan and Durgavati wielded power elsewhere or as queens and regents.",
  "इल्तुतमिश की पुत्री रज़िया ने 1236 से 1240 तक शासन किया। उन्होंने पर्दा छोड़ा, खुले दरबार में बैठीं और हाथी की सवारी की, पर तुर्क सरदार उनकी स्वतंत्रता और एक हब्शी, याक़ूत, को ऊँचा पद देने से नाराज़ थे, और उन्हें गद्दी से हटाकर मार दिया गया। चाँद बीबी, नूरजहाँ और दुर्गावती ने दूसरी जगहों पर या रानी और संरक्षिका के रूप में सत्ता चलाई।",
  f"{NC7} -- The Delhi Sultans.",
  "medieval-razia-sultan")

M(MD, "easy", "The Red Fort at Delhi was built by:",
  "दिल्ली का लाल क़िला किसने बनवाया?",
  ["Shah Jahan", "Akbar", "Aurangzeb", "Sher Shah Suri"],
  ["शाहजहाँ", "अकबर", "औरंगज़ेब", "शेरशाह सूरी"],
  0,
  "Shah Jahan built the Red Fort (Qila-i-Mubarak) as the citadel of his new capital, Shahjahanabad, completed in 1648; it contains the Diwan-i-Aam and Diwan-i-Khas. Akbar built the Agra Fort, whose red sandstone is often the source of confusion, and Aurangzeb added the Moti Masjid inside the Red Fort.",
  "शाहजहाँ ने अपनी नई राजधानी शाहजहानाबाद के क़िले के रूप में लाल क़िला (क़िला-ए-मुबारक) बनवाया, जो 1648 में पूरा हुआ; इसमें दीवान-ए-आम और दीवान-ए-ख़ास हैं। अकबर ने आगरा का क़िला बनवाया, जिसका लाल बलुआ पत्थर प्रायः भ्रम का कारण बनता है, और औरंगज़ेब ने लाल क़िले के भीतर मोती मस्जिद जोड़ी।",
  f"{NC7} -- Rulers and Buildings; UNESCO -- Red Fort Complex.",
  "medieval-red-fort-shah-jahan")

M(MD, "easy", "The 'Humayun-nama' was written by:",
  "'हुमायूँनामा' किसने लिखा?",
  ["Gulbadan Begum", "Nur Jahan", "Jahanara Begum", "Zeb-un-Nissa"],
  ["गुलबदन बेगम", "नूरजहाँ", "जहाँआरा बेगम", "ज़ेबुन्निसा"],
  0,
  "Gulbadan Begum, Babur's daughter and Humayun's half-sister, wrote the Humayun-nama at Akbar's request, giving a rare view of family life in the Mughal household during the years of struggle and exile. Jahanara (Shah Jahan's daughter) wrote on Sufism, and Zeb-un-Nissa (Aurangzeb's daughter) was a poet.",
  "बाबर की पुत्री और हुमायूँ की सौतेली बहन गुलबदन बेगम ने अकबर के अनुरोध पर हुमायूँनामा लिखा, जो संघर्ष और निर्वासन के वर्षों में मुग़ल परिवार के पारिवारिक जीवन की दुर्लभ झलक देता है। जहाँआरा (शाहजहाँ की पुत्री) ने सूफ़ीवाद पर लिखा, और ज़ेबुन्निसा (औरंगज़ेब की पुत्री) कवयित्री थीं।",
  f"{NC12} -- Kings and Chronicles.",
  "medieval-humayun-nama-gulbadan")

M(MD, "easy", "The heartland of the Chola kingdom lay in the delta of the:",
  "चोल राज्य का केंद्र-क्षेत्र किस नदी के डेल्टा में था?",
  ["Kaveri", "Krishna", "Godavari", "Mahanadi"],
  ["कावेरी", "कृष्णा", "गोदावरी", "महानदी"],
  0,
  "The Cholas rose from the fertile Kaveri delta around Uraiyur and later Thanjavur, where irrigated rice cultivation supported a dense population, temples and a strong state; the Grand Anicut on the Kaveri, attributed to the early Chola Karikala, is among the oldest water-diversion works in use.",
  "चोल उरैयूर और बाद में तंजावुर के आसपास उपजाऊ कावेरी डेल्टा से उभरे, जहाँ सिंचित धान की खेती ने घनी आबादी, मंदिरों और सशक्त राज्य को आधार दिया; कावेरी पर ग्रैंड एनीकट, जिसे आरंभिक चोल करिकाल का माना जाता है, उपयोग में आने वाले सबसे पुराने जल-मोड़ कार्यों में है।",
  f"{NC7} -- New Kings and Kingdoms.",
  "medieval-chola-kaveri-delta")

M(MD, "easy", "Mirabai was a devotee of:",
  "मीराबाई किसकी भक्त थीं?",
  ["Krishna", "Rama", "Shiva", "Vithoba"],
  ["कृष्ण", "राम", "शिव", "विठोबा"],
  0,
  "Mirabai, a Rajput princess married into the royal family of Mewar in the 16th century, devoted herself to Krishna, whom she regarded as her true husband, defying the norms of her in-laws; her bhajans in Rajasthani and Braj are still widely sung.",
  "16वीं सदी में मेवाड़ के राजपरिवार में ब्याही गई राजपूत राजकुमारी मीराबाई ने अपने ससुराल के नियमों को चुनौती देते हुए स्वयं को कृष्ण को समर्पित किया, जिन्हें वे अपना सच्चा पति मानती थीं; राजस्थानी और ब्रज में उनके भजन आज भी व्यापक रूप से गाए जाते हैं।",
  f"{NC7} -- Devotional Paths to the Divine.",
  "medieval-mirabai-krishna")

M(MD, "easy", "The tomb of Sher Shah Suri stands at:",
  "शेरशाह सूरी का मक़बरा कहाँ है?",
  ["Sasaram", "Agra", "Delhi", "Jaunpur"],
  ["सासाराम", "आगरा", "दिल्ली", "जौनपुर"],
  0,
  "Sher Shah's tomb at Sasaram in Bihar, his family's home, stands in the middle of an artificial lake; the octagonal building with its broad dome is one of the finest examples of Afghan (Sur) architecture and a step towards the Mughal style.",
  "बिहार के सासाराम में, जो उनके परिवार का घर था, शेरशाह का मक़बरा एक कृत्रिम झील के बीच खड़ा है; चौड़े गुंबद वाली यह अष्टकोणीय इमारत अफ़ग़ान (सूर) वास्तुकला के सबसे सुंदर उदाहरणों में से एक है और मुग़ल शैली की ओर एक क़दम है।",
  "Archaeological Survey of India -- Sher Shah Suri's Tomb, Sasaram.",
  "medieval-sher-shah-tomb-sasaram")

M(MD, "easy", "Tulsidas wrote the 'Ramcharitmanas' in:",
  "तुलसीदास ने 'रामचरितमानस' किस भाषा में लिखा?",
  ["Awadhi", "Braj Bhasha", "Maithili", "Bhojpuri"],
  ["अवधी", "ब्रजभाषा", "मैथिली", "भोजपुरी"],
  0,
  "Tulsidas composed the Ramcharitmanas (1574 onwards) in Awadhi, the language of the Ayodhya region, which carried the Rama story to ordinary people across north India. Surdas, his contemporary, sang of Krishna in Braj Bhasha -- the trap -- and Vidyapati wrote in Maithili.",
  "तुलसीदास ने रामचरितमानस (1574 से) अवधी में रचा, जो अयोध्या क्षेत्र की भाषा है, और इसने राम-कथा को पूरे उत्तर भारत के आम लोगों तक पहुँचाया। उनके समकालीन सूरदास ने ब्रजभाषा में कृष्ण के गीत गाए, जो जाल है, और विद्यापति ने मैथिली में लिखा।",
  f"{NC7} -- Devotional Paths to the Divine.",
  "medieval-tulsidas-awadhi")

M(MD, "easy", "Who was the first Mughal emperor to be born in India?",
  "भारत में जन्म लेने वाले पहले मुग़ल बादशाह कौन थे?",
  ["Akbar", "Humayun", "Jahangir", "Shah Jahan"],
  ["अकबर", "हुमायूँ", "जहाँगीर", "शाहजहाँ"],
  0,
  "Akbar was born in 1542 at Amarkot in Sindh, while his father Humayun was fleeing after his defeats by Sher Shah; Babur and Humayun were born in Central Asia (Humayun at Kabul). Jahangir, born at Fatehpur Sikri, came later.",
  "अकबर का जन्म 1542 में सिंध के अमरकोट में हुआ, जब उनके पिता हुमायूँ शेरशाह से पराजयों के बाद भाग रहे थे; बाबर और हुमायूँ का जन्म मध्य एशिया में (हुमायूँ का काबुल में) हुआ। फ़तेहपुर सीकरी में जन्मे जहाँगीर बाद में आए।",
  f"{SC2}, chapter on Akbar.",
  "medieval-akbar-born-in-india")

# ---------------------------------------------------------------- hard MCQs (3)
M(MD, "hard", "The 'Futuhat-i-Firozshahi', an account of the policies of Firuz Shah Tughlaq, was written by:",
  "फ़िरोज़ शाह तुग़लक़ की नीतियों का विवरण 'फ़ुतूहात-ए-फ़िरोज़शाही' किसने लिखा?",
  ["Firuz Shah Tughlaq himself", "Ziauddin Barani", "Shams-i-Siraj Afif", "Amir Khusrau, the court poet"],
  ["स्वयं फ़िरोज़ शाह तुग़लक़", "ज़ियाउद्दीन बरनी", "शम्स-ए-सिराज अफ़ीफ़", "दरबारी कवि अमीर ख़ुसरो"],
  0,
  "Firuz Shah wrote the Futuhat himself, a short work listing his measures -- the abolition of certain taxes and punishments, the repair of buildings, the founding of towns -- and presenting them as acts of piety; it was inscribed on a building at Firozabad. "
  "Barani and Afif both wrote histories titled Tarikh-i-Firoz Shahi, which is why they are the tempting answers; Khusrau had died before Firuz came to the throne.",
  "फ़िरोज़ शाह ने फ़ुतूहात स्वयं लिखी, एक छोटी रचना जो उनके उपायों, जैसे कुछ करों और दंडों की समाप्ति, इमारतों की मरम्मत, नगरों की स्थापना, को गिनाती है और उन्हें धार्मिक पुण्य के काम बताती है; इसे फ़िरोज़ाबाद की एक इमारत पर उकेरा गया था। "
  "बरनी और अफ़ीफ़, दोनों ने तारीख़-ए-फ़िरोज़शाही नाम के इतिहास लिखे, इसीलिए वे आकर्षक उत्तर हैं; फ़िरोज़ के गद्दी पर बैठने से पहले ख़ुसरो की मृत्यु हो चुकी थी।",
  f"{SC1}, chapter 7 and introduction on sources.",
  "medieval-futuhat-i-firozshahi")

M(MD, "hard", "The Portuguese were expelled from Hughli in Bengal in 1632 during the reign of:",
  "1632 में बंगाल के हुगली से पुर्तगालियों को किसके शासनकाल में निकाला गया?",
  ["Shah Jahan", "Jahangir", "Aurangzeb", "Farrukhsiyar"],
  ["शाहजहाँ", "जहाँगीर", "औरंगज़ेब", "फ़र्रुख़सियर"],
  0,
  "Shah Jahan ordered the siege of Hughli after complaints that the Portuguese were raiding for slaves, forcing conversions and evading duties; the town fell in 1632 and thousands of Portuguese were taken as captives to Agra. The episode shows the Mughals' readiness to act against a European power on land, even though they had no navy to match it at sea.",
  "शाहजहाँ ने शिकायतों के बाद हुगली की घेराबंदी का आदेश दिया कि पुर्तगाली दासों के लिए छापे मार रहे हैं, ज़बरन धर्म-परिवर्तन करा रहे हैं और शुल्क से बच रहे हैं; 1632 में नगर गिरा और हज़ारों पुर्तगालियों को बंदी बनाकर आगरा ले जाया गया। यह प्रसंग दिखाता है कि मुग़ल ज़मीन पर एक यूरोपीय शक्ति के विरुद्ध कार्रवाई को तैयार थे, भले ही समुद्र में उसकी बराबरी वाली नौसेना उनके पास नहीं थी।",
  f"{SC2}, chapter on Shah Jahan.",
  "medieval-hughli-portuguese-1632")

M(MD, "hard", "The 'Tuhfat-ul-Mujahidin', an account of the resistance to the Portuguese in Malabar, was written by:",
  "मालाबार में पुर्तगालियों के प्रतिरोध का विवरण 'तुहफ़त-उल-मुजाहिदीन' किसने लिखा?",
  ["Zainuddin Makhdum", "Muhammad Qasim Ferishta", "Abdur Razzaq", "Ibn Battuta"],
  ["ज़ैनुद्दीन मख़दूम", "मुहम्मद क़ासिम फ़रिश्ता", "अब्दुर्रज़्ज़ाक़", "इब्न बतूता"],
  0,
  "Shaikh Zainuddin Makhdum of Ponnani wrote the Tuhfat-ul-Mujahidin in Arabic in the late 16th century, describing the Portuguese attacks on Malabar's trade and the resistance of the Zamorin's forces and the Kunjali Marakkars, the Zamorin's naval commanders; it is among the earliest histories of Kerala. Ferishta wrote a general history of India, and the other two were travellers of earlier centuries.",
  "पोन्नानी के शेख़ ज़ैनुद्दीन मख़दूम ने 16वीं सदी के अंत में अरबी में तुहफ़त-उल-मुजाहिदीन लिखी, जिसमें मालाबार के व्यापार पर पुर्तगाली हमलों और ज़मोरिन की सेनाओं तथा उसके नौसेनापतियों, कुंजाली मरक्कारों, के प्रतिरोध का वर्णन है; यह केरल के सबसे आरंभिक इतिहासों में है। फ़रिश्ता ने भारत का सामान्य इतिहास लिखा, और बाकी दो पहले की सदियों के यात्री थे।",
  f"{SC2}, chapter on the Europeans.",
  "medieval-tuhfat-ul-mujahidin")

# ---------------------------------------------------------------- medium pairs (5)
P(MD, "medium", "Consider the following pairs of dynasties and their capitals:",
  "राजवंशों और उनकी राजधानियों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Paramaras : Dhar", "Gurjara-Pratiharas : Kanauj", "Hoysalas : Dwarasamudra", "Yadavas : Warangal"],
  ["परमार : धार", "गुर्जर-प्रतिहार : कन्नौज", "होयसल : द्वारसमुद्र", "यादव : वारंगल"],
  2,
  "Three pairs are correct. The Paramaras ruled Malwa from Dhar, the Pratiharas made Kanauj their capital, and the Hoysalas ruled from Dwarasamudra (Halebidu) in Karnataka, famous for its temples. "
  "Pair 4 is wrong: the Yadavas ruled from Devagiri; Warangal was the Kakatiya capital. All four kingdoms were attacked by the Khaljis, which is why they are often confused.",
  "तीन युग्म सही हैं। परमारों ने धार से मालवा पर शासन किया, प्रतिहारों ने कन्नौज को राजधानी बनाया, और होयसलों ने कर्नाटक के द्वारसमुद्र (हलेबीडु) से शासन किया, जो अपने मंदिरों के लिए प्रसिद्ध है। "
  "युग्म 4 गलत है: यादवों ने देवगिरि से शासन किया; वारंगल काकतीयों की राजधानी थी। चारों राज्यों पर ख़िलजियों ने आक्रमण किए, इसीलिए इन्हें प्रायः गड्डमड्ड कर दिया जाता है।",
  f"{SC1}, chapters 1 and 5.",
  "medieval-dynasties-capitals-pairs")

P(MD, "medium", "Consider the following pairs of Bhakti saints and the regions of their activity:",
  "भक्ति संतों और उनके कार्य-क्षेत्रों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Namdev : Maharashtra", "Purandaradasa : Karnataka", "Narsinh Mehta : Rajasthan", "Lalla (Lal Ded) : Kashmir"],
  ["नामदेव : महाराष्ट्र", "पुरंदरदास : कर्नाटक", "नरसिंह मेहता : राजस्थान", "लल्ला (लल देद) : कश्मीर"],
  2,
  "Three pairs are correct. Namdev was a Varkari saint of Maharashtra; Purandaradasa, a Haridasa of Vijayanagara times, is called the father of Carnatic music; and Lalla (14th century) composed mystical verses (vakhs) in Kashmiri that are revered by Hindus and Muslims alike. "
  "Pair 3 is wrong: Narsinh Mehta (15th century) was a poet-saint of Gujarat, whose 'Vaishnav Jan To' was a favourite of Gandhi.",
  "तीन युग्म सही हैं। नामदेव महाराष्ट्र के वारकरी संत थे; विजयनगर काल के हरिदास पुरंदरदास को कर्नाटक संगीत का जनक कहा जाता है; और लल्ला (14वीं सदी) ने कश्मीरी में रहस्यवादी पद (वाख) रचे, जिन्हें हिंदू और मुसलमान समान रूप से पूजते हैं। "
  "युग्म 3 गलत है: नरसिंह मेहता (15वीं सदी) गुजरात के कवि-संत थे, जिनका 'वैष्णव जन तो' गांधी का प्रिय भजन था।",
  f"{NC7} -- Devotional Paths to the Divine.",
  "medieval-bhakti-saints-regions-pairs")

P(MD, "medium", "Consider the following pairs of chronicles and their authors:",
  "इतिवृत्तों और उनके लेखकों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Muntakhab-ul-Lubab : Abdur Razzaq", "Tabaqat-i-Akbari : Nizamuddin Ahmad", "Padshahnama : Abdul Hamid Lahori", "Alamgirnama : Abul Fazl"],
  ["मुंतख़ब-उल-लुबाब : अब्दुर्रज़्ज़ाक़", "तबक़ात-ए-अकबरी : निज़ामुद्दीन अहमद", "पादशाहनामा : अब्दुल हमीद लाहौरी", "आलमगीरनामा : अबुल फ़ज़ल"],
  1,
  "Only pairs 2 and 3 are correct. Nizamuddin Ahmad's Tabaqat-i-Akbari is a general history ending in Akbar's reign, and Abdul Hamid Lahori wrote the official Padshahnama of Shah Jahan's reign, famous for its illustrated manuscript. "
  "Pair 1 is wrong: the Muntakhab-ul-Lubab, a history of the Mughals down to the early 18th century, was written by Khafi Khan; Abdur Razzaq was a 15th-century Timurid envoy and chronicler. Pair 4 is wrong: the Alamgirnama, on the first ten years of Aurangzeb's reign, is by Mirza Muhammad Kazim; Abul Fazl, author of the Akbarnama, had died in 1602.",
  "केवल युग्म 2 और 3 सही हैं। निज़ामुद्दीन अहमद की तबक़ात-ए-अकबरी अकबर के शासन तक का सामान्य इतिहास है, और अब्दुल हमीद लाहौरी ने शाहजहाँ के शासन का आधिकारिक पादशाहनामा लिखा, जो अपनी सचित्र पांडुलिपि के लिए प्रसिद्ध है। "
  "युग्म 1 गलत है: 18वीं सदी के आरंभ तक मुग़लों का इतिहास मुंतख़ब-उल-लुबाब ख़ाफ़ी ख़ाँ ने लिखा; अब्दुर्रज़्ज़ाक़ 15वीं सदी के तैमूरी दूत और इतिहासकार थे। युग्म 4 गलत है: औरंगज़ेब के शासन के पहले दस वर्षों पर आलमगीरनामा मिर्ज़ा मुहम्मद काज़िम का है; अकबरनामा के लेखक अबुल फ़ज़ल की 1602 में मृत्यु हो चुकी थी।",
  f"{NC12} -- Kings and Chronicles; {SC2}, introduction on sources.",
  "medieval-mughal-chronicles-authors-pairs")

P(MD, "medium", "Consider the following pairs of Sufi terms and their meanings:",
  "सूफ़ी शब्दों और उनके अर्थों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Pir : A spiritual guide", "Murid : A disciple", "Sama : Fasting during Ramzan", "Silsila : The tomb of a Sufi saint"],
  ["पीर : आध्यात्मिक मार्गदर्शक", "मुरीद : शिष्य", "समा : रमज़ान में रोज़ा", "सिलसिला : किसी सूफ़ी संत की क़ब्र"],
  1,
  "Only pairs 1 and 2 are correct: the bond between pir (or shaikh) and murid was the heart of Sufi life. "
  "Pair 3 is wrong: sama is the audition of mystical music and poetry, which the Chishtis used to reach spiritual ecstasy and which gave rise to the qawwali. Pair 4 is wrong: a silsila is the chain of spiritual succession linking a Sufi through his teachers back to the Prophet; a saint's tomb is a dargah, where the anniversary of his death (urs) is celebrated.",
  "केवल युग्म 1 और 2 सही हैं: पीर (या शेख़) और मुरीद का बंधन सूफ़ी जीवन का केंद्र था। "
  "युग्म 3 गलत है: समा रहस्यवादी संगीत और काव्य का श्रवण है, जिसका उपयोग चिश्ती आध्यात्मिक आनंद तक पहुँचने के लिए करते थे और जिससे क़व्वाली विकसित हुई। युग्म 4 गलत है: सिलसिला आध्यात्मिक उत्तराधिकार की वह शृंखला है जो किसी सूफ़ी को उसके गुरुओं के ज़रिए पैग़ंबर तक जोड़ती है; किसी संत की क़ब्र दरगाह है, जहाँ उसकी पुण्यतिथि (उर्स) मनाई जाती है।",
  f"{NC12} -- Bhakti-Sufi Traditions.",
  "medieval-sufi-terms-pairs")

P(MD, "medium", "Consider the following pairs of ports of Mughal India and their regions:",
  "मुग़ल भारत के बंदरगाहों और उनके क्षेत्रों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Surat : Gujarat", "Masulipatnam : Coromandel coast", "Hughli : Bengal", "Calicut : Malabar"],
  ["सूरत : गुजरात", "मसूलीपट्टनम : कोरोमंडल तट", "हुगली : बंगाल", "कालीकट : मालाबार"],
  3,
  "All four pairs are correct. Surat was the main Mughal port and the gateway for pilgrims to Mecca; Masulipatnam, the port of Golconda, exported the famous painted and printed cottons; Hughli handled Bengal's silk, sugar and rice; and Calicut, under the Zamorin, was the pepper port where Vasco da Gama arrived. "
  "A student who expects one mismatch will fall for 'Only three pairs'.",
  "चारों युग्म सही हैं। सूरत मुख्य मुग़ल बंदरगाह और मक्का जाने वाले तीर्थयात्रियों का द्वार था; गोलकोंडा का बंदरगाह मसूलीपट्टनम प्रसिद्ध चित्रित और छापे वाले सूती कपड़े निर्यात करता था; हुगली बंगाल के रेशम, चीनी और चावल का व्यापार संभालता था; और ज़मोरिन के अधीन कालीकट काली मिर्च का बंदरगाह था, जहाँ वास्को द गामा पहुँचा। "
  "जो विद्यार्थी एक बेमेल की अपेक्षा करता है, वह 'केवल तीन युग्म' के जाल में फँसेगा।",
  f"{SC2}, chapter on trade; {NC12}.",
  "medieval-mughal-ports-regions-pairs")

# ---------------------------------------------------------------- easy pairs (3)
P(MD, "easy", "Consider the following pairs of regional dynasties and the regions they ruled:",
  "क्षेत्रीय राजवंशों और उनके शासित क्षेत्रों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Sharqi : Jaunpur", "Faruqi : Khandesh", "Hussain Shahi : Bengal", "Imad Shahi : Kashmir"],
  ["शर्क़ी : जौनपुर", "फ़ारूक़ी : ख़ानदेश", "हुसैनशाही : बंगाल", "इमादशाही : कश्मीर"],
  2,
  "Three pairs are correct. The Sharqis made Jaunpur a centre of learning and architecture in the 15th century; the Faruqis ruled Khandesh from Burhanpur; and Alauddin Hussain Shah's dynasty patronised Bengali literature, including translations of the epics. "
  "Pair 4 is wrong: the Imad Shahis ruled Berar, one of the five successor states of the Bahmani kingdom; Kashmir was ruled by the Shah Mir dynasty.",
  "तीन युग्म सही हैं। शर्क़ियों ने 15वीं सदी में जौनपुर को विद्या और वास्तुकला का केंद्र बनाया; फ़ारूक़ियों ने बुरहानपुर से ख़ानदेश पर शासन किया; और अलाउद्दीन हुसैन शाह के वंश ने बांग्ला साहित्य को, महाकाव्यों के अनुवादों सहित, संरक्षण दिया। "
  "युग्म 4 गलत है: इमादशाहियों ने बरार पर शासन किया, जो बहमनी राज्य के पाँच उत्तराधिकारी राज्यों में से एक था; कश्मीर पर शाहमीर वंश का शासन था।",
  f"{SC1}, chapter on regional kingdoms.",
  "medieval-regional-dynasties-pairs")

P(MD, "easy", "Consider the following pairs of titles and the rulers who bore them:",
  "उपाधियों और उन्हें धारण करने वाले शासकों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Lakh Bakhsh : Qutb-ud-din Aibak", "Andhra Bhoja : Krishnadevaraya", "Jagadguru : Ibrahim Adil Shah II", "Sikandar-i-Sani : Alauddin Khalji"],
  ["लाख बख़्श : क़ुतुबुद्दीन ऐबक", "आंध्र भोज : कृष्णदेवराय", "जगद्गुरु : इब्राहिम आदिल शाह द्वितीय", "सिकंदर-ए-सानी : अलाउद्दीन ख़िलजी"],
  3,
  "All four pairs are correct. Aibak was called 'Lakh Bakhsh', the giver of lakhs, for his generosity; Krishnadevaraya, poet and patron, was 'Andhra Bhoja'; Ibrahim Adil Shah II of Bijapur, a patron of music who wrote the Kitab-i-Nauras, was called 'Jagadguru' for his tolerance; and Alauddin Khalji called himself 'Sikandar-i-Sani', the second Alexander, on his coins. "
  "A student who expects one mismatch will fall for 'Only three pairs'.",
  "चारों युग्म सही हैं। ऐबक को उदारता के लिए 'लाख बख़्श', यानी लाखों देने वाला, कहा जाता था; कवि और संरक्षक कृष्णदेवराय 'आंध्र भोज' थे; किताब-ए-नौरस लिखने वाले और संगीत के संरक्षक बीजापुर के इब्राहिम आदिल शाह द्वितीय को सहिष्णुता के लिए 'जगद्गुरु' कहा गया; और अलाउद्दीन ख़िलजी ने अपने सिक्कों पर स्वयं को 'सिकंदर-ए-सानी', यानी दूसरा सिकंदर, कहा। "
  "जो विद्यार्थी एक बेमेल की अपेक्षा करता है, वह 'केवल तीन युग्म' के जाल में फँसेगा।",
  f"{SC1}; {SC2}.",
  "medieval-rulers-titles-pairs")

P(MD, "easy", "Consider the following pairs of women rulers and the kingdoms they defended or governed:",
  "महिला शासकों और उनके द्वारा रक्षित या शासित राज्यों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Rani Durgavati : Garha-Katanga (Gond kingdom)", "Rani Karnavati : Mewar", "Tarabai : Mysore", "Rani Abbakka : Gujarat"],
  ["रानी दुर्गावती : गढ़ा-कटंगा (गोंड राज्य)", "रानी कर्णावती : मेवाड़", "ताराबाई : मैसूर", "रानी अब्बक्का : गुजरात"],
  1,
  "Only pairs 1 and 2 are correct. Rani Durgavati of the Gond kingdom of Garha-Katanga died fighting Akbar's general Asaf Khan in 1564, and Rani Karnavati, widow of Rana Sanga, defended Chittor against Bahadur Shah of Gujarat in 1535. "
  "Pair 3 is wrong: Tarabai, widow of Rajaram, led the Maratha resistance to Aurangzeb after 1700 and founded the Kolhapur line. Pair 4 is wrong: Rani Abbakka Chowta ruled Ullal on the Tulu coast of Karnataka and resisted the Portuguese in the 16th century.",
  "केवल युग्म 1 और 2 सही हैं। गढ़ा-कटंगा के गोंड राज्य की रानी दुर्गावती 1564 में अकबर के सेनापति आसफ़ ख़ाँ से लड़ते हुए शहीद हुईं, और राणा सांगा की विधवा रानी कर्णावती ने 1535 में गुजरात के बहादुर शाह से चित्तौड़ की रक्षा की। "
  "युग्म 3 गलत है: राजाराम की विधवा ताराबाई ने 1700 के बाद औरंगज़ेब के विरुद्ध मराठा प्रतिरोध का नेतृत्व किया और कोल्हापुर शाखा की स्थापना की। युग्म 4 गलत है: रानी अब्बक्का चौटा ने कर्नाटक के तुलु तट पर उल्लाल पर शासन किया और 16वीं सदी में पुर्तगालियों का प्रतिरोध किया।",
  f"{SC2}; {NC7}.",
  "medieval-women-rulers-pairs")

# ---------------------------------------------------------------- hard pairs (2)
P(MD, "hard", "Consider the following pairs of rulers and their dynasties:",
  "शासकों और उनके राजवंशों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Mihira Bhoja : Gurjara-Pratihara", "Dharmapala : Pala", "Govinda III : Rashtrakuta", "Vikramaditya VI : Pala"],
  ["मिहिर भोज : गुर्जर-प्रतिहार", "धर्मपाल : पाल", "गोविंद तृतीय : राष्ट्रकूट", "विक्रमादित्य षष्ठ : पाल"],
  2,
  "Three pairs are correct. Mihira Bhoja was the greatest Pratihara king; Dharmapala raised the Palas to their height and briefly placed his nominee on the throne of Kanauj; and Govinda III led Rashtrakuta armies as far as the Ganga-Yamuna doab. "
  "Pair 4 is wrong: Vikramaditya VI (1076-1126) was the greatest king of the Western (Kalyani) Chalukyas, patron of the poet Bilhana, whose Vikramankadevacharita celebrates him, and of the jurist Vijnaneshvara, author of the Mitakshara.",
  "तीन युग्म सही हैं। मिहिर भोज सबसे महान प्रतिहार राजा थे; धर्मपाल ने पालों को उनके चरम तक पहुँचाया और कुछ समय के लिए कन्नौज की गद्दी पर अपना समर्थित व्यक्ति बैठाया; और गोविंद तृतीय राष्ट्रकूट सेनाओं को गंगा-यमुना दोआब तक ले गए। "
  "युग्म 4 गलत है: विक्रमादित्य षष्ठ (1076-1126) पश्चिमी (कल्याणी) चालुक्यों के सबसे महान राजा थे, कवि बिल्हण के संरक्षक, जिनका विक्रमांकदेवचरित उनकी प्रशंसा करता है, और मिताक्षरा के लेखक विधिवेत्ता विज्ञानेश्वर के भी।",
  f"{SC1}, chapter 1; Upinder Singh, A History of Ancient and Early Medieval India, chapter 11.",
  "medieval-early-medieval-rulers-pairs")

P(MD, "hard", "Consider the following pairs of Sufi saints and the places of their dargahs:",
  "सूफ़ी संतों और उनकी दरगाहों के स्थानों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Nizamuddin Auliya : Delhi", "Shaikh Salim Chishti : Fatehpur Sikri", "Baba Farid (Fariduddin Ganj-i-Shakar) : Bidar", "Khwaja Bandanawaz Gesu Daraz : Lahore"],
  ["निज़ामुद्दीन औलिया : दिल्ली", "शेख़ सलीम चिश्ती : फ़तेहपुर सीकरी", "बाबा फ़रीद (फ़रीदुद्दीन गंज-ए-शकर) : बीदर", "ख़्वाजा बंदानवाज़ गेसू दराज़ : लाहौर"],
  1,
  "Only pairs 1 and 2 are correct. Nizamuddin Auliya's dargah is in Delhi, near the tombs of Amir Khusrau and Jahanara, and Shaikh Salim Chishti's white marble tomb stands in the courtyard of the Jama Masjid at Fatehpur Sikri -- Akbar, whose son Salim was born after the saint's blessing, built the city there. "
  "Pair 3 is wrong: Baba Farid's dargah is at Pakpattan in Pakistani Punjab; his verses are included in the Guru Granth Sahib. Pair 4 is wrong: Gesu Daraz, who took the Chishti order to the Deccan, is buried at Gulbarga.",
  "केवल युग्म 1 और 2 सही हैं। निज़ामुद्दीन औलिया की दरगाह दिल्ली में अमीर ख़ुसरो और जहाँआरा की क़ब्रों के पास है, और शेख़ सलीम चिश्ती का सफ़ेद संगमरमर का मक़बरा फ़तेहपुर सीकरी की जामा मस्जिद के आँगन में है; अकबर ने, जिनके पुत्र सलीम का जन्म संत के आशीर्वाद के बाद हुआ, वहीं नगर बसाया। "
  "युग्म 3 गलत है: बाबा फ़रीद की दरगाह पाकिस्तानी पंजाब के पाकपट्टन में है; उनकी वाणी गुरु ग्रंथ साहिब में शामिल है। युग्म 4 गलत है: चिश्ती सिलसिले को दक्कन ले जाने वाले गेसू दराज़ गुलबर्गा में दफ़न हैं।",
  f"{NC12} -- Bhakti-Sufi Traditions.",
  "medieval-sufi-dargahs-pairs")

if __name__ == "__main__":
    write("hist_l2_t7_medieval_b.sql")
