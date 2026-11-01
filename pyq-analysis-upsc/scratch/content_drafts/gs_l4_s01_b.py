# -*- coding: utf-8 -*-
"""Level 4 · Simulator 1 (GS Paper I full mock, Layout A: the 2023/24 shape) -- part B: History (11)
(upsc_l4_gs_cell_targets.mjs 1).
The bank is saturated on standard history, so this part draws on monuments, art and movements no row tests (a
whole-bank term sweep: l3_tools/_data/bank_dump.json): the Martand Sun Temple, Sirpur's Lakshmana temple, the
Vaikuntha Perumal temple, the Bamiyan Buddhas; Itmad-ud-Daulah, Bibi ka Maqbara, Ibrahim Rauza and Vimal Vasahi;
Mandu; the National Planning Committee of 1938; the Khudai Khidmatgars and Peshawar, 1930; Chhatrapati Shivaji
Terminus, Le Corbusier's Chandigarh and Lutyens's Delhi; the churches of Old Goa; and folk instruments (Kamaicha,
Gogona, Bhapang, Edakka). MCQ keys are pinned (pos)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "History"
d.REQUIRE_CRAFT = True

# ---------------------------------------------------------------- Ancient (MCQ, easy)
M("Ancient", "easy",
  "The Martand Sun Temple in Kashmir, now in ruins, was built by",
  "कश्मीर का मार्तंड सूर्य मंदिर, जो अब खंडहर है, किसने बनवाया था?",
  ["Lalitaditya Muktapida", "Zain-ul-Abidin of Kashmir", "Harshavardhana of Kannauj", "Kanishka of the Kushanas"],
  ["ललितादित्य मुक्तापीड", "कश्मीर के ज़ैनुल आबिदीन", "कन्नौज के हर्षवर्धन", "कुषाण वंश के कनिष्क"],
  0,
  "The temple at Martand, near Anantnag, was built in the eighth century by Lalitaditya Muktapida of the Karkota dynasty, the most powerful ruler of early medieval Kashmir, whose campaigns Kalhana's Rajatarangini celebrates. Its colonnaded courtyard, trefoil arches and gabled roofs combine Gandharan, Gupta and Greek-influenced elements in a distinctly Kashmiri style. The temple was wrecked in the fifteenth century. "
  "Zain-ul-Abidin, the fifteenth-century Sultan of Kashmir, is remembered for religious tolerance and the revival of crafts; Harsha ruled from Kannauj in the seventh century; Kanishka's empire, in the first and second centuries, centred on Gandhara and Mathura.",
  "अनंतनाग के पास मार्तंड का मंदिर आठवीं शताब्दी में कर्कोट वंश के ललितादित्य मुक्तापीड ने बनवाया, जो आरंभिक मध्यकालीन कश्मीर के सबसे शक्तिशाली शासक थे और जिनके अभियानों का गुणगान कल्हण की राजतरंगिणी करती है। इसका स्तंभयुक्त प्रांगण, त्रिपर्णी मेहराबें और ढलवाँ छतें गांधार, गुप्त और यूनानी-प्रभावित तत्वों को एक विशिष्ट कश्मीरी शैली में जोड़ती हैं। पंद्रहवीं शताब्दी में मंदिर नष्ट कर दिया गया। "
  "पंद्रहवीं शताब्दी के कश्मीर के सुल्तान ज़ैनुल आबिदीन धार्मिक सहिष्णुता और शिल्पों के पुनरुद्धार के लिए स्मरण किए जाते हैं; हर्ष ने सातवीं शताब्दी में कन्नौज से शासन किया; पहली और दूसरी शताब्दी में कनिष्क का साम्राज्य गांधार और मथुरा पर केंद्रित था।",
  "Archaeological Survey of India, Martand Sun Temple (Srinagar Circle); Kalhana, Rajatarangini, Book IV; NCERT, An Introduction to Indian Art (Class XI).",
  "l4-s01-his-martand-lalitaditya-karkota", pos=3, craft="recall")

# ---------------------------------------------------------------- Ancient (MCQ, medium)
M("Ancient", "medium",
  "The Lakshmana temple at Sirpur in Chhattisgarh is notable as",
  "छत्तीसगढ़ में सिरपुर का लक्ष्मण मंदिर किस रूप में उल्लेखनीय है?",
  ["one of the finest early temples of India built in brick",
   "a rock-cut cave temple of the Gupta period with painted walls",
   "a Jain temple built entirely of white marble by a merchant guild",
   "the earliest stepwell of central India, with a temple at its base"],
  ["भारत के ईंट से बने आरंभिक मंदिरों में सबसे उत्कृष्ट में से एक",
   "चित्रित दीवारों वाला गुप्त काल का एक शैलकृत गुफा मंदिर",
   "एक व्यापारी श्रेणी द्वारा पूर्णतः सफ़ेद संगमरमर से बना जैन मंदिर",
   "मध्य भारत की सबसे प्राचीन बावड़ी, जिसके तल में एक मंदिर है"],
  0,
  "Built in the seventh century, traditionally by Queen Vasata in memory of her husband, a ruler of the Panduvamshi dynasty of Dakshina Kosala, the Lakshmana temple at Sirpur on the Mahanadi is among the best-preserved early brick temples of India: its curvilinear tower and its door frame, carved in stone, show how moulded and cut bricks could reproduce the detail of stone temples. Sirpur was also a Buddhist centre, with monasteries excavated in the 2000s. "
  "Brick temples survive mainly where good stone was scarce -- Bhitargaon in Uttar Pradesh is another example -- which makes them rare evidence of an otherwise lost building tradition. The site is not a cave, not Jain and not a stepwell.",
  "सातवीं शताब्दी में, परंपरा के अनुसार दक्षिण कोसल के पांडुवंशी शासक की स्मृति में उनकी रानी वासटा द्वारा, बनवाया गया महानदी तट पर सिरपुर का लक्ष्मण मंदिर भारत के सबसे सुरक्षित आरंभिक ईंट-मंदिरों में है: इसका वक्ररेखीय शिखर और पत्थर में तराशा द्वार-चौखट दिखाते हैं कि ढाली और काटी गई ईंटें पत्थर के मंदिरों की बारीकियाँ कैसे दोहरा सकती थीं। सिरपुर एक बौद्ध केंद्र भी था, जहाँ 2000 के दशक में विहार उत्खनित हुए। "
  "ईंट के मंदिर मुख्यतः वहाँ बचे हैं जहाँ अच्छा पत्थर दुर्लभ था -- उत्तर प्रदेश का भीतरगाँव एक और उदाहरण है -- इसलिए वे एक अन्यथा लुप्त निर्माण परंपरा के दुर्लभ साक्ष्य हैं। यह स्थल न गुफा है, न जैन, न बावड़ी।",
  "Archaeological Survey of India, Lakshmana Temple, Sirpur (Raipur Circle); NCERT, An Introduction to Indian Art (Class XI), temple architecture.",
  "l4-s01-his-sirpur-lakshmana-brick-temple", pos=1, craft="precision")

# ---------------------------------------------------------------- Ancient (statement, easy)
S("Ancient", "easy", "With reference to the Vaikuntha Perumal temple at Kanchipuram, consider the following statements:",
  "कांचीपुरम के वैकुंठ पेरुमाल मंदिर के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["It was built by the Pallava king Nandivarman II.",
   "Sculptured panels on its walls narrate episodes from the history of the Pallava dynasty.",
   "It is a monolithic temple cut out of a single rock, like the rathas of Mamallapuram."],
  ["इसे पल्लव राजा नंदिवर्मन द्वितीय ने बनवाया था।",
   "इसकी दीवारों पर तराशे फलक पल्लव वंश के इतिहास के प्रसंग बताते हैं।",
   "यह मामल्लपुरम के रथों की तरह एक ही चट्टान से काटा गया एकाश्म मंदिर है।"],
  C3, 1,
  "Statements 1 and 2 are correct. The temple was built in the eighth century by Nandivarman II Pallavamalla, and its cloister walls carry a long sequence of relief panels with labels that depict Pallava history, including the choice of Nandivarman as king -- a rare case of a temple serving as a visual chronicle of its builders. "
  "Statement 3 is wrong: it is a structural temple of dressed stone, built up block by block, as is the Kailasanatha temple in the same city. Pallava architecture moved from rock-cut cave temples (Mahendravarman I) to monoliths such as the rathas (Narasimhavarman I) and then to structural temples (Rajasimha and his successors), the line that led to the great Chola temples.",
  "कथन 1 और 2 सही हैं। मंदिर आठवीं शताब्दी में नंदिवर्मन द्वितीय पल्लवमल्ल ने बनवाया, और इसकी प्रदक्षिणा-दीवारों पर लेखयुक्त उभरे फलकों की लंबी शृंखला पल्लव इतिहास दिखाती है, जिसमें नंदिवर्मन का राजा चुना जाना भी है -- यह दुर्लभ उदाहरण है जब मंदिर अपने निर्माताओं के चित्रात्मक इतिवृत्त का काम करता है। "
  "कथन 3 ग़लत है: यह तराशे पत्थर के खंडों को जोड़कर बना संरचनात्मक मंदिर है, जैसा इसी नगर का कैलासनाथ मंदिर है। पल्लव स्थापत्य शैलकृत गुफा मंदिरों (महेंद्रवर्मन प्रथम) से रथों जैसे एकाश्म मंदिरों (नरसिंहवर्मन प्रथम) और फिर संरचनात्मक मंदिरों (राजसिंह और उनके उत्तराधिकारी) तक बढ़ा, जिस धारा से महान चोल मंदिर निकले।",
  "Archaeological Survey of India, Vaikuntha Perumal Temple, Kanchipuram (Chennai Circle); NCERT, An Introduction to Indian Art (Class XI), Chapter 6.",
  "l4-s01-his-vaikuntha-perumal-nandivarman-ii-panels", craft="precision")

# ---------------------------------------------------------------- Ancient (statement, medium)
S("Ancient", "medium", "With reference to the giant Buddha figures of Bamiyan, consider the following statements:",
  "बामियान की विशाल बुद्ध आकृतियों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["They were carved into a cliff in a valley of the Hindu Kush that lay on routes linking Central Asia with India.",
   "They were destroyed in 2001.",
   "They were made in the Mathura style, from blocks of red sandstone brought from Mathura."],
  ["इन्हें हिंदूकुश की उस घाटी की चट्टान में तराशा गया था जो मध्य एशिया को भारत से जोड़ने वाले मार्गों पर थी।",
   "इन्हें 2001 में नष्ट कर दिया गया।",
   "इन्हें मथुरा शैली में, मथुरा से लाए गए लाल बलुआ पत्थर के खंडों से बनाया गया था।"],
  C3, 1,
  "Statements 1 and 2 are correct. The two standing Buddhas, about 55 and 38 metres high, were cut into the cliff of the Bamiyan valley in present-day Afghanistan around the sixth century, when the valley was a Buddhist centre on the trade routes through the Hindu Kush; the faces and robes were finished in mud and stucco and painted, in a style that carried Gandharan influence into Central Asia. Xuanzang described them in the seventh century. They were blown up by the Taliban in March 2001, and the valley's cultural landscape was then inscribed as a World Heritage site in danger. "
  "Statement 3 is wrong: they were carved in situ from the conglomerate rock of the cliff, not assembled from sandstone; red sandstone of Sikri is the material of the Mathura school's images.",
  "कथन 1 और 2 सही हैं। लगभग 55 और 38 मीटर ऊँची दो खड़ी बुद्ध आकृतियाँ लगभग छठी शताब्दी में आज के अफ़ग़ानिस्तान की बामियान घाटी की चट्टान में काटी गई थीं, जब यह घाटी हिंदूकुश से होकर जाने वाले व्यापार मार्गों पर एक बौद्ध केंद्र थी; चेहरों और वस्त्रों को मिट्टी और प्लास्टर से तैयार कर रंगा गया था, ऐसी शैली में जो गांधार प्रभाव को मध्य एशिया तक ले गई। सातवीं शताब्दी में ह्वेनसांग ने इनका वर्णन किया। मार्च 2001 में तालिबान ने इन्हें उड़ा दिया, और फिर घाटी का सांस्कृतिक भूदृश्य संकटग्रस्त विश्व धरोहर के रूप में अंकित किया गया। "
  "कथन 3 ग़लत है: इन्हें चट्टान की संगुटिका शिला से वहीं तराशा गया था, बलुआ पत्थर से जोड़ा नहीं गया था; सीकरी का लाल बलुआ पत्थर मथुरा शैली की मूर्तियों की सामग्री है।",
  "UNESCO World Heritage Centre, Cultural Landscape and Archaeological Remains of the Bamiyan Valley (2003); NCERT, An Introduction to Indian Art (Class XI).",
  "l4-s01-his-bamiyan-buddhas-cliff-2001-not-mathura", craft="linkage")

# ---------------------------------------------------------------- Medieval (pairs, medium)
P("Medieval", "medium", "Consider the following pairs of monuments and the persons who built or commissioned them:",
  "स्मारकों और उन्हें बनवाने या निर्मित करवाने वाले व्यक्तियों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Tomb of Itmad-ud-Daulah, Agra : Nur Jahan",
   "Bibi ka Maqbara, Aurangabad : Shah Jahan",
   "Ibrahim Rauza, Bijapur : Ibrahim Adil Shah II",
   "Vimal Vasahi temple, Mount Abu : Vimal Shah, minister of the Chaulukya king Bhima I"],
  ["एतमादुद्दौला का मक़बरा, आगरा : नूरजहाँ",
   "बीबी का मक़बरा, औरंगाबाद : शाहजहाँ",
   "इब्राहिम रौज़ा, बीजापुर : इब्राहिम आदिल शाह द्वितीय",
   "विमल वसही मंदिर, माउंट आबू : चौलुक्य राजा भीम प्रथम के मंत्री विमल शाह"],
  2,
  "Only three pairs are correct. Nur Jahan built the tomb of her father, Mirza Ghiyas Beg (Itmad-ud-Daulah), in the 1620s; its white marble inlaid with semi-precious stones (pietra dura) anticipates the Taj Mahal. Ibrahim Rauza, the tomb of Ibrahim Adil Shah II, is the finest monument of Bijapur and is said to have inspired the Taj's builders. Vimal Shah, a minister of the Chaulukya (Solanki) king Bhima I, built the Vimal Vasahi Jain temple at Dilwara in 1031, famous for its marble carving. "
  "Pair 2 is wrong: Bibi ka Maqbara, the 'Taj of the Deccan', was built in the 1660s in memory of Aurangzeb's wife Dilras Banu Begum, under Aurangzeb and their son Azam Shah -- not by Shah Jahan, though it consciously imitates his Taj Mahal.",
  "केवल तीन युग्म सही हैं। नूरजहाँ ने 1620 के दशक में अपने पिता मिर्ज़ा ग़ियास बेग (एतमादुद्दौला) का मक़बरा बनवाया; अर्ध-मूल्यवान पत्थरों की जड़ाई (पिएत्रा दूरा) वाला इसका सफ़ेद संगमरमर ताजमहल का पूर्वाभास देता है। इब्राहिम आदिल शाह द्वितीय का मक़बरा इब्राहिम रौज़ा बीजापुर का सबसे उत्कृष्ट स्मारक है और कहा जाता है कि इसने ताज के निर्माताओं को प्रेरित किया। चौलुक्य (सोलंकी) राजा भीम प्रथम के मंत्री विमल शाह ने 1031 में दिलवाड़ा में विमल वसही जैन मंदिर बनवाया, जो अपनी संगमरमर नक़्क़ाशी के लिए प्रसिद्ध है। "
  "युग्म 2 ग़लत है: ‘दक्कन का ताज’ बीबी का मक़बरा 1660 के दशक में औरंगज़ेब की पत्नी दिलरस बानो बेगम की स्मृति में औरंगज़ेब और उनके पुत्र आज़म शाह के अधीन बना -- शाहजहाँ ने नहीं, यद्यपि यह सचेत रूप से उनके ताजमहल की नक़ल करता है।",
  "Archaeological Survey of India: Itmad-ud-Daulah's Tomb (Agra Circle), Bibi ka Maqbara (Aurangabad Circle), Ibrahim Rauza (Dharwad Circle); Dilwara temples, Mount Abu.",
  "l4-s01-his-monuments-itmad-bibi-ibrahim-vimal-pairs", craft="precision")

# ---------------------------------------------------------------- Medieval (statement, medium)
S("Medieval", "medium", "With reference to Mandu, consider the following statements:",
  "मांडू के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["It was the capital of the Sultanate of Malwa.",
   "The Hindola Mahal there gets its name from its sloping side walls, which make it appear to sway.",
   "The pavilion named after Rupmati is linked with Baz Bahadur, the last independent ruler of Malwa, whom Akbar's forces defeated."],
  ["यह मालवा सल्तनत की राजधानी थी।",
   "वहाँ के हिंडोला महल का नाम उसकी ढलवाँ बग़ल की दीवारों से पड़ा, जिनसे वह झूलता-सा लगता है।",
   "रूपमती के नाम का मंडप बाज़ बहादुर से जुड़ा है, जो मालवा का अंतिम स्वतंत्र शासक था और जिसे अकबर की सेनाओं ने हराया।"],
  C3, 2,
  "All three statements are correct. Mandu, on a plateau of the Vindhyas in present-day Madhya Pradesh, was the capital of the Malwa Sultanate founded in the early fifteenth century, first under the Ghuri and then the Khalji dynasty; its monuments -- the Jami Masjid, Hoshang Shah's marble tomb, the Jahaz Mahal set between two lakes and the Hindola Mahal with its battered (inward-sloping) walls -- form one of the most complete groups of Sultanate architecture. "
  "Baz Bahadur, a musician-ruler, and the singer Rupmati became the subject of a celebrated romance; Akbar's general Adham Khan conquered Malwa in 1561, after which it became a Mughal province. Regional sultanates such as Malwa, Gujarat and Jaunpur developed styles of their own after the Delhi Sultanate weakened.",
  "तीनों कथन सही हैं। आज के मध्य प्रदेश में विंध्य के एक पठार पर स्थित मांडू पंद्रहवीं शताब्दी के आरंभ में स्थापित मालवा सल्तनत की राजधानी था, पहले ग़ोरी और फिर ख़लजी वंश के अधीन; इसके स्मारक -- जामी मस्जिद, होशंग शाह का संगमरमर का मक़बरा, दो झीलों के बीच बना जहाज़ महल और भीतर की ओर ढलती दीवारों वाला हिंडोला महल -- सल्तनतकालीन स्थापत्य के सबसे पूर्ण समूहों में हैं। "
  "संगीतज्ञ-शासक बाज़ बहादुर और गायिका रूपमती एक प्रसिद्ध प्रेमकथा के विषय बने; अकबर के सेनापति आदम ख़ाँ ने 1561 में मालवा जीता, जिसके बाद यह मुग़ल सूबा बना। दिल्ली सल्तनत के कमज़ोर होने के बाद मालवा, गुजरात और जौनपुर जैसी क्षेत्रीय सल्तनतों ने अपनी-अपनी शैलियाँ विकसित कीं।",
  "Archaeological Survey of India, Group of Monuments at Mandu (Bhopal Circle); NCERT, Themes in Indian History, Part II.",
  "l4-s01-his-mandu-malwa-hindola-rupmati-baz-bahadur", craft="linkage")

# ---------------------------------------------------------------- Modern (MCQ, medium)
M("Modern", "medium",
  "The National Planning Committee set up by the Indian National Congress in 1938 was chaired by",
  "1938 में भारतीय राष्ट्रीय कांग्रेस द्वारा गठित राष्ट्रीय योजना समिति के अध्यक्ष कौन थे?",
  ["Jawaharlal Nehru", "Subhas Chandra Bose", "M. Visvesvaraya", "K. T. Shah"],
  ["जवाहरलाल नेहरू", "सुभाष चंद्र बोस", "एम. विश्वेश्वरैया", "के. टी. शाह"],
  0,
  "The committee was set up in 1938 on the initiative of Subhas Chandra Bose, then Congress president, after a conference of the ministers of industries of the Congress-ruled provinces; Jawaharlal Nehru chaired it and the economist K. T. Shah was its general secretary. Its sub-committees, on subjects from industry and agriculture to women's role in the economy, prepared reports that shaped the idea of planned development and, after 1947, the Planning Commission. "
  "Bose set it up but did not chair it; M. Visvesvaraya had earlier argued for planning in 'Planned Economy for India' (1934); K. T. Shah, the committee's general secretary, edited its reports.",
  "समिति 1938 में तत्कालीन कांग्रेस अध्यक्ष सुभाष चंद्र बोस की पहल पर कांग्रेस-शासित प्रांतों के उद्योग मंत्रियों के एक सम्मेलन के बाद गठित हुई; जवाहरलाल नेहरू इसके अध्यक्ष और अर्थशास्त्री के. टी. शाह इसके महासचिव थे। उद्योग और कृषि से लेकर अर्थव्यवस्था में महिलाओं की भूमिका तक के विषयों पर इसकी उप-समितियों ने प्रतिवेदन तैयार किए, जिन्होंने नियोजित विकास के विचार को और 1947 के बाद योजना आयोग को आकार दिया। "
  "बोस ने इसे गठित किया पर अध्यक्षता नहीं की; एम. विश्वेश्वरैया ने पहले ‘प्लान्ड इकॉनमी फ़ॉर इंडिया’ (1934) में नियोजन की वकालत की थी; समिति के महासचिव के. टी. शाह ने इसके प्रतिवेदनों का संपादन किया।",
  "National Planning Committee, Reports (ed. K. T. Shah, 1946-49); NCERT, Themes in Indian History, Part III, and Politics in India since Independence, Chapter 3.",
  "l4-s01-his-national-planning-committee-1938-nehru", pos=2, craft="recall")

# ---------------------------------------------------------------- Modern (statement, easy)
S("Modern", "easy", "With reference to the Khudai Khidmatgar movement, consider the following statements:",
  "ख़ुदाई ख़िदमतगार आंदोलन के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["It was founded by Khan Abdul Ghaffar Khan in the North-West Frontier Province and was committed to non-violence.",
   "Many people were killed when troops fired on a crowd in the Qissa Khwani Bazaar of Peshawar during the Civil Disobedience Movement.",
   "At Peshawar, soldiers of the Garhwal Rifles refused orders to fire on the unarmed crowd."],
  ["इसकी स्थापना ख़ान अब्दुल ग़फ़्फ़ार ख़ान ने पश्चिमोत्तर सीमांत प्रांत में की थी और यह अहिंसा के प्रति प्रतिबद्ध था।",
   "सविनय अवज्ञा आंदोलन के दौरान पेशावर के क़िस्सा ख़्वानी बाज़ार में भीड़ पर सेना की गोलीबारी में अनेक लोग मारे गए।",
   "पेशावर में गढ़वाल राइफ़ल्स के सैनिकों ने निहत्थी भीड़ पर गोली चलाने के आदेश को मानने से इनकार किया।"],
  C3, 2,
  "All three statements are correct. Abdul Ghaffar Khan, the 'Frontier Gandhi', founded the Khudai Khidmatgars ('servants of God') in 1929 among the Pashtuns, a people with a strong martial tradition, and made non-violence their creed; from their dress they came to be called the 'Red Shirts', and they worked with the Congress. When he was arrested in April 1930, crowds gathered in Peshawar, and troops fired on them in the Qissa Khwani Bazaar. "
  "Two platoons of the Royal Garhwal Rifles under Chandra Singh Garhwali refused to fire on the unarmed Muslim crowd, and were court-martialled -- one of the clearest signs that the loyalty of Indian soldiers could no longer be taken for granted, and that the national movement cut across religious lines in the Frontier.",
  "तीनों कथन सही हैं। ‘सीमांत गांधी’ अब्दुल ग़फ़्फ़ार ख़ान ने 1929 में प्रबल योद्धा परंपरा वाले पश्तूनों में ख़ुदाई ख़िदमतगार (‘ईश्वर के सेवक’) की स्थापना की और अहिंसा को उनका धर्म बनाया; अपनी वेशभूषा के कारण वे ‘लाल कुर्ती’ कहलाए, और उन्होंने कांग्रेस के साथ काम किया। अप्रैल 1930 में उनकी गिरफ़्तारी पर पेशावर में भीड़ जुटी, और क़िस्सा ख़्वानी बाज़ार में सेना ने उस पर गोली चलाई। "
  "चंद्र सिंह गढ़वाली के अधीन रॉयल गढ़वाल राइफ़ल्स की दो प्लाटूनों ने निहत्थी मुस्लिम भीड़ पर गोली चलाने से इनकार किया, और उनका कोर्ट-मार्शल हुआ -- यह सबसे स्पष्ट संकेतों में था कि भारतीय सैनिकों की निष्ठा अब पक्की नहीं मानी जा सकती थी, और कि सीमांत में राष्ट्रीय आंदोलन धार्मिक सीमाओं के पार था।",
  "NCERT, Themes in Indian History, Part III, Chapter 13 (Mahatma Gandhi and the Nationalist Movement); NCERT, Our Pasts III (Class VIII).",
  "l4-s01-his-khudai-khidmatgar-qissa-khwani-garhwal-rifles", craft="recall")

# ---------------------------------------------------------------- Modern (statement, hard)
S("Modern", "hard", "With reference to colonial and modern architecture in India, consider the following statements:",
  "भारत में औपनिवेशिक और आधुनिक स्थापत्य के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Chhatrapati Shivaji Terminus in Mumbai, designed by Frederick William Stevens, blends Victorian Gothic forms with Indian elements.",
   "The Capitol Complex of Chandigarh, designed by Le Corbusier, is part of a World Heritage property that spans several countries.",
   "Rashtrapati Bhavan was designed by Herbert Baker, while Edwin Lutyens designed the North and South Blocks of the Secretariat."],
  ["मुंबई का छत्रपति शिवाजी टर्मिनस, जिसे फ़्रेडरिक विलियम स्टीवेंस ने अभिकल्पित किया, विक्टोरियन गोथिक रूपों को भारतीय तत्वों के साथ मिलाता है।",
   "ल कॉर्बूज़िए द्वारा अभिकल्पित चंडीगढ़ का कैपिटल कॉम्प्लेक्स एक ऐसी विश्व धरोहर संपत्ति का भाग है जो कई देशों में फैली है।",
   "राष्ट्रपति भवन हर्बर्ट बेकर ने अभिकल्पित किया, जबकि एडविन लुटियंस ने सचिवालय के नॉर्थ और साउथ ब्लॉक अभिकल्पित किए।"],
  C3, 1,
  "Statements 1 and 2 are correct. The terminus, completed in 1888 as Victoria Terminus, combines Gothic Revival arches, turrets and stained glass with Indian traditional features, carved by students of the Bombay school of art; it became a World Heritage site in 2004. Chandigarh's Capitol Complex -- the Assembly, the Secretariat and the High Court -- was inscribed in 2016 as one of 17 sites in seven countries that make up 'The Architectural Work of Le Corbusier', a modernist city planned for Punjab after Partition. "
  "Statement 3 reverses the roles: Edwin Lutyens designed the Viceroy's House (now Rashtrapati Bhavan), and Herbert Baker the two Secretariat blocks, when the capital moved from Calcutta to New Delhi after 1911. Their buildings drew on Mughal and Buddhist forms -- the chhatris and the dome inspired by the Sanchi stupa -- to present imperial rule as rooted in India.",
  "कथन 1 और 2 सही हैं। 1888 में विक्टोरिया टर्मिनस के रूप में पूर्ण यह टर्मिनस गोथिक पुनरुद्धार के मेहराबों, बुर्जों और रंगीन काँच को भारतीय पारंपरिक तत्वों से जोड़ता है, जिन्हें बॉम्बे कला विद्यालय के विद्यार्थियों ने तराशा; 2004 में यह विश्व धरोहर स्थल बना। चंडीगढ़ का कैपिटल कॉम्प्लेक्स -- विधानसभा, सचिवालय और उच्च न्यायालय -- 2016 में ‘ल कॉर्बूज़िए का स्थापत्य कार्य’ बनाने वाले सात देशों के 17 स्थलों में से एक के रूप में अंकित हुआ, जो विभाजन के बाद पंजाब के लिए नियोजित एक आधुनिकतावादी नगर है। "
  "कथन 3 भूमिकाएँ उलट देता है: एडविन लुटियंस ने वायसराय भवन (अब राष्ट्रपति भवन) और हर्बर्ट बेकर ने सचिवालय के दोनों ब्लॉक अभिकल्पित किए, जब 1911 के बाद राजधानी कलकत्ता से नई दिल्ली आई। उनकी इमारतों ने मुग़ल और बौद्ध रूपों -- छतरियों और साँची स्तूप से प्रेरित गुंबद -- का सहारा लिया, ताकि साम्राज्यिक शासन भारत में जड़ा हुआ दिखे।",
  "UNESCO World Heritage Centre: Chhatrapati Shivaji Terminus (2004) and The Architectural Work of Le Corbusier (2016); President's Secretariat, history of Rashtrapati Bhavan.",
  "l4-s01-his-cst-stevens-le-corbusier-lutyens-baker", craft="precision")

# ---------------------------------------------------------------- Modern (statement, medium)
S("Modern", "medium", "With reference to the churches of Old Goa, consider the following statements:",
  "पुराने गोवा के गिरजाघरों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Basilica of Bom Jesus holds the remains of St Francis Xavier.",
   "They were built in the nineteenth century, after the capital had moved to Panaji.",
   "The Se Cathedral was built by the Dutch after they captured Goa from the Portuguese."],
  ["बॉम जीसस बेसिलिका में संत फ़्रांसिस ज़ेवियर के अवशेष रखे हैं।",
   "इन्हें उन्नीसवीं शताब्दी में, राजधानी के पणजी चले जाने के बाद, बनाया गया।",
   "से कैथेड्रल डचों ने पुर्तगालियों से गोवा जीतने के बाद बनवाया।"],
  C3, 0,
  "Only statement 1 is correct. The Basilica of Bom Jesus, a Baroque church of the Jesuits consecrated in 1605, holds the remains of Francis Xavier, the Jesuit missionary who reached Goa in 1542, and the 'Churches and Convents of Goa' became a World Heritage site in 1986 for spreading Renaissance and Baroque forms across Asia. "
  "Statement 2 is wrong: the churches date from the sixteenth and seventeenth centuries, when Old Goa was the capital of Portuguese Asia; the city was later abandoned because of epidemics, and the capital moved to Panaji in the nineteenth century. Statement 3 is wrong: the Se Cathedral was built by the Portuguese, and the Dutch, though they blockaded Goa in the seventeenth century, never captured it; Goa stayed Portuguese until 1961.",
  "केवल कथन 1 सही है। 1605 में प्रतिष्ठित जेसुइट बरोक गिरजाघर बॉम जीसस बेसिलिका में 1542 में गोवा पहुँचे जेसुइट मिशनरी फ़्रांसिस ज़ेवियर के अवशेष हैं, और पुनर्जागरण तथा बरोक रूपों को एशिया भर में फैलाने के लिए ‘गोवा के गिरजाघर और कॉन्वेंट’ 1986 में विश्व धरोहर स्थल बने। "
  "कथन 2 ग़लत है: गिरजाघर सोलहवीं और सत्रहवीं शताब्दी के हैं, जब पुराना गोवा पुर्तगाली एशिया की राजधानी था; बाद में महामारियों के कारण नगर छोड़ दिया गया, और उन्नीसवीं शताब्दी में राजधानी पणजी चली गई। कथन 3 ग़लत है: से कैथेड्रल पुर्तगालियों ने बनवाया, और डचों ने सत्रहवीं शताब्दी में गोवा की नाकाबंदी तो की पर उसे कभी जीत नहीं पाए; गोवा 1961 तक पुर्तगाली रहा।",
  "UNESCO World Heritage Centre, Churches and Convents of Goa (1986); Archaeological Survey of India, Goa Circle.",
  "l4-s01-his-old-goa-bom-jesus-xavier-se-portuguese", craft="precision")

# ---------------------------------------------------------------- Music & Dance (pairs, hard)
P("Music & Dance", "hard", "Consider the following pairs of musical instruments and the traditions or regions they are associated with:",
  "वाद्ययंत्रों और उनसे जुड़ी परंपराओं या क्षेत्रों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Kamaicha : Bowed instrument of the Manganiyar musicians of western Rajasthan",
   "Gogona : Bamboo jaw harp played with Bihu songs in Assam",
   "Bhapang : One-stringed instrument associated with the Mewat region",
   "Edakka : Hourglass drum of the Kathak tradition of Lucknow"],
  ["कमायचा : पश्चिमी राजस्थान के मांगणियार संगीतकारों का गज़ से बजने वाला वाद्य",
   "गोगोना : असम में बिहू गीतों के साथ बजाया जाने वाला बाँस का मुखवीणा-वाद्य",
   "भपंग : मेवात क्षेत्र से जुड़ा एक-तारा वाद्य",
   "इडक्का : लखनऊ की कथक परंपरा का डमरू-आकार ढोल"],
  2,
  "Only three pairs are correct. The kamaicha, a bowed lute with a large round resonator, accompanies the hereditary Manganiyar musicians of the Thar; the gogona, a small bamboo jaw harp plucked against the mouth, is part of the Bihu ensemble in Assam; and the bhapang, a single string stretched through a drum that the player tightens and loosens to bend the pitch, is played by the Jogi musicians of Mewat on the Rajasthan-Haryana border. "
  "Pair 4 is wrong: the edakka is an hourglass drum of Kerala, played in temples and in Sopana Sangeetham, the music of the temple steps; its pitch changes as the player squeezes the laces. Kathak is accompanied mainly by the tabla and the pakhawaj. Folk instruments like these survive through hereditary communities and temple service, which is why their decline tracks the loss of patronage.",
  "केवल तीन युग्म सही हैं। बड़े गोल अनुनादक वाला गज़ से बजने वाला वाद्य कमायचा थार के वंशानुगत मांगणियार संगीतकारों की संगत करता है; मुँह के पास छेड़ा जाने वाला बाँस का छोटा मुखवीणा-वाद्य गोगोना असम के बिहू वादक-समूह का भाग है; और भपंग, जिसमें एक तार ढोल से होकर खिंचा रहता है और वादक उसे कसकर-ढीलाकर स्वर मोड़ता है, राजस्थान-हरियाणा सीमा पर मेवात के जोगी संगीतकार बजाते हैं। "
  "युग्म 4 ग़लत है: इडक्का केरल का डमरू-आकार ढोल है, जो मंदिरों में और मंदिर की सीढ़ियों के संगीत सोपान संगीतम् में बजाया जाता है; वादक डोरियाँ दबाकर इसका स्वर बदलता है। कथक की संगत मुख्यतः तबला और पखावज करते हैं। ऐसे लोक वाद्य वंशानुगत समुदायों और मंदिर-सेवा से बचे हैं, इसीलिए संरक्षण घटने के साथ उनका ह्रास होता है।",
  "Sangeet Natak Akademi, musical instruments collection; Centre for Cultural Resources and Training, folk instruments of India.",
  "l4-s01-his-instruments-kamaicha-gogona-bhapang-edakka", craft="precision")

write("gs_l4_s01_b.sql")
