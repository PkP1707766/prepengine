# -*- coding: utf-8 -*-
"""Level 3 · Test 6 (GS Integrated Test 6) -- part F: Science & Technology (11) (upsc_l3_cell_targets.mjs 6).
Same cell plan as Tests 1-5.
Every fact was searched in the whole UPSC bank (l3_tools/bank_find.py) and is one no row tests: the 'duck curve' of
solar-heavy grids; vanadium redox flow batteries; agentic AI; neuromorphic chips; thermal runaway in lithium-ion
cells; the structure and composition of glass; the 2029 flyby of the asteroid Apophis; human metapneumovirus; GNSS
jamming and spoofing; Cherenkov radiation; ISRO's semi-cryogenic engine. MCQ keys are pinned."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Science & Technology"
d.REQUIRE_CRAFT = True
EN = "Energy & Environmental Technology"
IT = "IT, Communication & Emerging Technologies"
CH = "Chemistry & Materials"

# ================================================================ ENERGY & ENVIRONMENTAL TECHNOLOGY (e-MCQ, m-stmt)
M(EN, "easy",
  "In a grid with a large share of solar power, the demand that other plants must meet falls sharply around noon and then climbs steeply after sunset -- a pattern called the 'duck curve'. This pattern mainly increases the need for:",
  "सौर ऊर्जा के बड़े हिस्से वाले ग्रिड में, अन्य संयंत्रों को जो माँग पूरी करनी होती है वह दोपहर के आसपास तेज़ी से गिरती है और सूर्यास्त के बाद तेज़ी से चढ़ती है -- इस पैटर्न को ‘डक कर्व’ कहते हैं। यह पैटर्न मुख्यतः किसकी आवश्यकता बढ़ाता है?",
  ["more coal plants that run at a constant full output throughout the day",
   "flexible sources, such as storage and hydro, that can ramp up quickly",
   "higher transmission voltages to cut line losses during the noon hours",
   "bigger cooling towers at nuclear power plants during the summer months"],
  ["अधिक कोयला संयंत्रों की जो पूरे दिन स्थिर पूर्ण उत्पादन पर चलें",
   "भंडारण और जलविद्युत जैसे लचीले स्रोतों की जो जल्दी उत्पादन बढ़ाएँ",
   "दोपहर के घंटों में लाइन हानि घटाने के लिए और ऊँचे पारेषण वोल्टेज की",
   "गर्मी के महीनों में परमाणु बिजलीघरों पर बड़े शीतलन टावरों की"],
  1,
  "The 'net load' -- demand minus solar and wind output -- traced through a day looks like a duck: a sagging belly at midday when solar output peaks, and a steep neck in the evening when solar fades just as household demand rises. The grid then needs resources that can cut back at noon and ramp up by tens of gigawatts within a few hours: batteries and pumped storage that charge on cheap midday power, hydro, flexible gas plants, and demand response encouraged by time-of-day tariffs. "
  "Coal plants running flat out are the least suited to this, since they ramp slowly and cannot go far below their minimum load without trouble. India is already seeing the pattern: its tightest hours are increasingly the evening 'non-solar hours', when solar output has gone but demand stays high, which is why the government is pushing battery storage and pumped hydro alongside new solar capacity.",
  "दिन भर का ‘शुद्ध भार’ -- माँग में से सौर और पवन उत्पादन घटाकर -- बत्तख जैसा दिखता है: दोपहर में जब सौर उत्पादन चरम पर होता है तब झुका हुआ पेट, और शाम को खड़ी गर्दन जब सौर उत्पादन घटता है ठीक तभी घरेलू माँग बढ़ती है। तब ग्रिड को ऐसे संसाधन चाहिए जो दोपहर में उत्पादन घटा सकें और कुछ ही घंटों में दसियों गीगावाट बढ़ा सकें: बैटरियाँ और पंप भंडारण जो दोपहर की सस्ती बिजली से चार्ज हों, जलविद्युत, लचीले गैस संयंत्र, और दिन के समय के अनुसार शुल्क से प्रोत्साहित माँग-प्रतिक्रिया। "
  "पूरी क्षमता पर चलते कोयला संयंत्र इसके लिए सबसे कम उपयुक्त हैं, क्योंकि वे धीरे-धीरे उत्पादन बदलते हैं और अपने न्यूनतम भार से बहुत नीचे बिना कठिनाई के नहीं जा सकते। भारत में यह पैटर्न दिखने लगा है: उसके सबसे कठिन घंटे बढ़ते रूप में शाम के ‘ग़ैर-सौर घंटे’ हैं, जब सौर उत्पादन समाप्त हो जाता है पर माँग ऊँची बनी रहती है, इसीलिए सरकार नई सौर क्षमता के साथ बैटरी भंडारण और पंप जलविद्युत को बढ़ावा दे रही है।",
  "Ministry of Power and Central Electricity Authority (energy storage and resource adequacy); Grid Controller of India.",
  "l3-t6-sci-duck-curve-flexibility", pos=1, craft="application")

S(EN, "medium", "With reference to vanadium redox flow batteries, consider the following statements:",
  "वैनेडियम रेडॉक्स फ़्लो बैटरियों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Their energy is stored in liquid electrolytes kept in external tanks, so the storage capacity can be raised by enlarging the tanks.",
   "Their high energy density makes them well suited to powering electric cars.",
   "They lose capacity quickly and typically last only a few hundred charge cycles."],
  ["इनकी ऊर्जा बाहरी टंकियों में रखे द्रव विद्युत-अपघट्यों में संग्रहीत होती है, इसलिए टंकियाँ बड़ी करके भंडारण क्षमता बढ़ाई जा सकती है।",
   "इनका ऊँचा ऊर्जा घनत्व इन्हें विद्युत कारों को चलाने के लिए बहुत उपयुक्त बनाता है।",
   "इनकी क्षमता जल्दी घटती है और ये सामान्यतः केवल कुछ सौ चार्ज-चक्र चलती हैं।"],
  C3, 0,
  "Only statement 1 is correct. In a flow battery, two solutions -- here of vanadium ions in different oxidation states -- are pumped from tanks through a cell stack, where they exchange electrons across a membrane; the power rating depends on the size of the stack and the energy stored on the volume of electrolyte, so the two can be scaled separately. That makes them attractive for long-duration grid storage of four hours or more. "
  "Statement 2 is wrong: their energy density is several times lower than that of lithium-ion cells, so they are bulky and suited to stationary use, not vehicles. Statement 3 is wrong: because the same element is used on both sides and the electrodes do not undergo the structural wear of lithium-ion electrodes, they can run for many thousands of cycles over two decades or more, and their water-based electrolyte does not catch fire. Their drawbacks are a high upfront cost and dependence on vanadium supplies.",
  "केवल कथन 1 सही है। फ़्लो बैटरी में दो विलयन -- यहाँ विभिन्न ऑक्सीकरण अवस्थाओं वाले वैनेडियम आयनों के -- टंकियों से एक सेल-स्टैक में पंप किए जाते हैं, जहाँ वे एक झिल्ली के आर-पार इलेक्ट्रॉनों का आदान-प्रदान करते हैं; शक्ति क्षमता स्टैक के आकार पर और संग्रहीत ऊर्जा विद्युत-अपघट्य की मात्रा पर निर्भर है, इसलिए दोनों को अलग-अलग बढ़ाया जा सकता है। इससे वे चार घंटे या अधिक के दीर्घ-अवधि ग्रिड भंडारण के लिए आकर्षक हैं। "
  "कथन 2 ग़लत है: इनका ऊर्जा घनत्व लिथियम-आयन सेलों से कई गुना कम है, इसलिए वे भारी-भरकम हैं और स्थिर उपयोग के लिए उपयुक्त हैं, वाहनों के लिए नहीं। कथन 3 ग़लत है: चूँकि दोनों ओर एक ही तत्व प्रयुक्त होता है और इलेक्ट्रोडों में लिथियम-आयन इलेक्ट्रोडों जैसी संरचनात्मक घिसावट नहीं होती, वे दो दशक या अधिक में कई हज़ार चक्र चल सकती हैं, और उनका जल-आधारित विद्युत-अपघट्य आग नहीं पकड़ता। इनकी कमियाँ ऊँची आरंभिक लागत और वैनेडियम आपूर्ति पर निर्भरता हैं।",
  "NCERT Class XII, Chemistry ('Electrochemistry'); Ministry of Power, National Framework for Promoting Energy Storage Systems (2023).",
  "l3-t6-sci-vanadium-flow-battery", craft="precision")

# ================================================================ IT, COMMUNICATION & EMERGING TECHNOLOGIES (e-MCQ, m-stmt)
M(IT, "easy",
  "A software assistant is given the goal 'book the cheapest train ticket to Patna for Friday'. On its own it searches several websites, compares fares, fills in the booking form and asks the user only to confirm the payment. Such a system is best described as:",
  "एक सॉफ़्टवेयर सहायक को लक्ष्य दिया जाता है ‘शुक्रवार के लिए पटना का सबसे सस्ता रेल टिकट बुक करो’। वह स्वयं कई वेबसाइटें खोजता है, किराए की तुलना करता है, बुकिंग फ़ॉर्म भरता है और उपयोगकर्ता से केवल भुगतान की पुष्टि माँगता है। ऐसी प्रणाली का सबसे अच्छा वर्णन है:",
  ["a rule-based expert system that can follow only fixed if-then rules",
   "agentic AI, which plans and carries out multi-step tasks with tools",
   "a generative adversarial network trained to produce realistic images",
   "an optical character recognition program that reads printed text"],
  ["एक नियम-आधारित विशेषज्ञ प्रणाली जो केवल निश्चित यदि-तो नियमों का पालन कर सकती है",
   "एजेंटिक एआई, जो उपकरणों से बहु-चरणीय कार्यों की योजना बनाकर उन्हें पूरा करता है",
   "छवियाँ बनाने के लिए प्रशिक्षित एक जनरेटिव एडवर्सेरियल नेटवर्क",
   "छपे हुए पाठ को पढ़ने वाला एक ऑप्टिकल कैरेक्टर रिकग्निशन प्रोग्राम"],
  1,
  "An AI agent goes beyond answering a question: built usually on a large language model, it breaks a goal into steps, decides which tools to use -- a browser, a search engine, a form, a calculator or other software -- acts, checks the result and continues, with only limited human direction. A rule-based expert system, by contrast, can only apply rules written in advance for a narrow domain, while GANs and OCR are specialised tools for generating images and reading text. "
  "The autonomy that makes agents useful also raises new risks: errors can compound over many steps, a malicious web page can try to hijack the agent's instructions, and it is unclear who is accountable for a wrong purchase or a leaked document. That is why sensitive steps such as payments are usually kept for the human to confirm, as in the example.",
  "एआई एजेंट प्रश्न का उत्तर देने से आगे जाता है: सामान्यतः किसी बड़े भाषा मॉडल पर बना, वह लक्ष्य को चरणों में बाँटता है, तय करता है कि कौन-से उपकरण -- ब्राउज़र, सर्च इंजन, फ़ॉर्म, कैलकुलेटर या अन्य सॉफ़्टवेयर -- प्रयोग करने हैं, कार्य करता है, परिणाम जाँचता है और आगे बढ़ता है, केवल सीमित मानवीय निर्देशन के साथ। इसके विपरीत, नियम-आधारित विशेषज्ञ प्रणाली किसी संकीर्ण क्षेत्र के लिए पहले से लिखे नियम ही लागू कर सकती है, जबकि जीएएन और ओसीआर छवियाँ बनाने और पाठ पढ़ने के विशिष्ट उपकरण हैं। "
  "जो स्वायत्तता एजेंटों को उपयोगी बनाती है वही नए जोखिम भी लाती है: अनेक चरणों में त्रुटियाँ बढ़ सकती हैं, कोई दुर्भावनापूर्ण वेब पेज एजेंट के निर्देशों पर क़ब्ज़ा करने का प्रयास कर सकता है, और यह अस्पष्ट है कि ग़लत ख़रीद या लीक हुए दस्तावेज़ के लिए कौन उत्तरदायी है। इसीलिए भुगतान जैसे संवेदनशील चरण सामान्यतः मनुष्य की पुष्टि के लिए रखे जाते हैं, जैसा उदाहरण में है।",
  "Ministry of Electronics and Information Technology, IndiaAI Mission; NITI Aayog, National Strategy for Artificial Intelligence.",
  "l3-t6-sci-agentic-ai", pos=1, craft="application")

S(IT, "medium", "With reference to neuromorphic computing, consider the following statements:",
  "न्यूरोमॉर्फ़िक कंप्यूटिंग के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Neuromorphic chips work like conventional processors, moving data back and forth between a separate memory unit and a processing unit at every clock cycle.",
   "Because they imitate the brain, neuromorphic chips need far more electrical power than conventional processors for the same task."],
  ["न्यूरोमॉर्फ़िक चिप पारंपरिक प्रोसेसरों की तरह काम करते हैं, हर क्लॉक-चक्र में एक अलग मेमोरी इकाई और प्रसंस्करण इकाई के बीच डेटा आगे-पीछे ले जाते हुए।",
   "मस्तिष्क की नक़ल करने के कारण न्यूरोमॉर्फ़िक चिपों को उसी कार्य के लिए पारंपरिक प्रोसेसरों से कहीं अधिक बिजली चाहिए।"],
  T2, 3,
  "Neither statement is correct. Conventional computers follow the von Neumann design, in which data shuttle constantly between memory and processor -- a bottleneck that consumes much of the energy in modern AI workloads. Neuromorphic chips instead imitate networks of neurons and synapses: memory and computation sit together, and artificial neurons 'fire' spikes only when their input changes, so most of the chip is idle most of the time. "
  "The result is very low power consumption, which suits always-on sensors, drones, robots and other edge devices that must process signals in real time on a small battery. Research chips include Intel's Loihi and IBM's TrueNorth, and Indian institutions such as the Indian Institute of Science are developing new materials for brain-like circuits.",
  "कोई भी कथन सही नहीं है। पारंपरिक कंप्यूटर वॉन न्यूमैन रूपरेखा पर चलते हैं, जिसमें डेटा लगातार मेमोरी और प्रोसेसर के बीच आता-जाता है -- एक अवरोध जो आधुनिक एआई कार्यभार की बहुत-सी ऊर्जा खा जाता है। न्यूरोमॉर्फ़िक चिप इसके बजाय न्यूरॉनों और सिनैप्सों के जाल की नक़ल करते हैं: मेमोरी और गणना साथ रहते हैं, और कृत्रिम न्यूरॉन तभी स्पाइक ‘दागते’ हैं जब उनका इनपुट बदले, इसलिए चिप का अधिकांश भाग अधिकांश समय निष्क्रिय रहता है। "
  "परिणाम बहुत कम बिजली की खपत है, जो हमेशा चालू रहने वाले सेंसरों, ड्रोनों, रोबोटों और अन्य एज उपकरणों के लिए उपयुक्त है जिन्हें छोटी बैटरी पर वास्तविक समय में संकेतों को संसाधित करना होता है। अनुसंधान चिपों में इंटेल का लोइही और आईबीएम का ट्रूनॉर्थ शामिल हैं, और भारतीय विज्ञान संस्थान जैसी भारतीय संस्थाएँ मस्तिष्क-जैसे परिपथों के लिए नई सामग्रियाँ विकसित कर रही हैं।",
  "Department of Science and Technology; Ministry of Electronics and Information Technology (India Semiconductor Mission).",
  "l3-t6-sci-neuromorphic-computing", craft="inference")

# ================================================================ CHEMISTRY & MATERIALS (h-MCQ, m-stmt)
M(CH, "hard",
  "Fires in the lithium-ion batteries of electric scooters and phones are notoriously hard to put out. The main reason is that:",
  "इलेक्ट्रिक स्कूटरों और फ़ोनों की लिथियम-आयन बैटरियों में लगी आग बुझाना कुख्यात रूप से कठिन है। इसका मुख्य कारण यह है कि:",
  ["the cells hold a large mass of metallic lithium, which bursts into flame as soon as it meets air",
   "the batteries store compressed hydrogen gas, which leaks out when the outer casing is damaged",
   "an overheating cell sets off a self-heating chain reaction that spreads to neighbouring cells",
   "water reacts violently with every battery material, so no water-based extinguisher may ever be used"],
  ["सेलों में धात्विक लिथियम की बड़ी मात्रा होती है, जो हवा के संपर्क में आते ही जल उठती है",
   "बैटरियाँ संपीडित हाइड्रोजन गैस रखती हैं, जो बाहरी आवरण क्षतिग्रस्त होने पर रिसती है",
   "ज़्यादा गर्म हुआ सेल स्व-तापन की शृंखला-अभिक्रिया शुरू करता है जो पड़ोसी सेलों तक फैलती है",
   "पानी हर बैटरी सामग्री से तीव्र अभिक्रिया करता है, इसलिए जल-आधारित अग्निशामक कभी प्रयोग नहीं हो सकता"],
  2,
  "This is thermal runaway. Damage, overcharging or a manufacturing defect can cause an internal short circuit; the heat melts the separator between the electrodes, the flammable organic electrolyte breaks down into combustible gases, and some cathode materials release oxygen as they decompose, so the fire can sustain itself even when smothered. Each failing cell heats its neighbours, and a pack can reignite hours after the flames seem to be out. "
  "The other options rest on misconceptions: a lithium-ion cell holds lithium as ions within electrode compounds, not as a block of metal; it stores no hydrogen; and firefighters in fact use large volumes of water to cool burning packs. After a series of electric-scooter fires in 2022, India tightened its battery safety standard for electric vehicles (AIS-156), adding requirements on cell testing, thermal propagation and the battery management system.",
  "यह थर्मल रनअवे है। क्षति, अति-चार्जिंग या निर्माण-दोष से आंतरिक लघु-परिपथ हो सकता है; ऊष्मा इलेक्ट्रोडों के बीच के पृथक्कारक को पिघला देती है, ज्वलनशील कार्बनिक विद्युत-अपघट्य टूटकर दहनशील गैसें बनाता है, और कुछ कैथोड पदार्थ विघटित होते हुए ऑक्सीजन छोड़ते हैं, इसलिए ढक देने पर भी आग स्वयं चलती रह सकती है। हर विफल होता सेल अपने पड़ोसियों को गर्म करता है, और लपटें बुझी लगने के घंटों बाद भी पैक फिर जल सकता है। "
  "अन्य विकल्प भ्रांतियों पर टिके हैं: लिथियम-आयन सेल लिथियम को धातु के खंड के रूप में नहीं, इलेक्ट्रोड यौगिकों में आयनों के रूप में रखता है; वह हाइड्रोजन संग्रहीत नहीं करता; और अग्निशामक वास्तव में जलते पैकों को ठंडा करने के लिए भारी मात्रा में पानी प्रयोग करते हैं। 2022 में इलेक्ट्रिक स्कूटरों में आग की कई घटनाओं के बाद भारत ने विद्युत वाहनों के लिए अपना बैटरी सुरक्षा मानक (एआईएस-156) कड़ा किया, जिसमें सेल परीक्षण, ऊष्मा-प्रसार और बैटरी प्रबंधन प्रणाली की आवश्यकताएँ जोड़ी गईं।",
  "NCERT Class XII, Chemistry ('Electrochemistry'); Ministry of Road Transport and Highways, AIS-156 amendments (2022).",
  "l3-t6-sci-lithium-ion-thermal-runaway", pos=2, craft="inference")

S(CH, "medium", "With reference to glass, consider the following statements:",
  "काँच के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Glass is a crystalline solid in which the atoms are arranged in a regular, repeating pattern.",
   "Like ice, glass has a sharp melting point at which the whole solid turns into a liquid at once.",
   "Ordinary window glass is made mainly by melting alumina (aluminium oxide) with charcoal."],
  ["काँच एक क्रिस्टलीय ठोस है जिसमें परमाणु नियमित, दोहराए जाने वाले क्रम में व्यवस्थित होते हैं।",
   "बर्फ़ की तरह काँच का एक तीक्ष्ण गलनांक होता है जिस पर पूरा ठोस एक साथ द्रव में बदल जाता है।",
   "साधारण खिड़की का काँच मुख्यतः एल्यूमिना (एल्युमिनियम ऑक्साइड) को कोयले के साथ पिघलाकर बनाया जाता है।"],
  C3, 3,
  "None of the statements is correct. Statement 1 is wrong: glass is an amorphous solid -- its atoms have only short-range order, like a frozen liquid -- unlike crystalline quartz, which is also silica but has its atoms in a regular lattice. Statement 2 is wrong, and follows from the first: because there is no long-range order, there is no single temperature at which the whole structure gives way, so glass softens gradually over a range of temperatures; that is what lets glassblowers draw and shape it, whereas a crystalline solid such as ice melts sharply at a fixed point. "
  "Statement 3 is wrong: common soda-lime glass is made by melting silica sand with soda ash (sodium carbonate) and limestone; the soda lowers the melting temperature and the lime makes the glass durable. Small amounts of metal oxides colour glass -- cobalt oxide gives blue, for example -- while lead oxide gives the brilliance of crystal glass.",
  "कोई भी कथन सही नहीं है। कथन 1 ग़लत है: काँच एक अक्रिस्टलीय ठोस है -- उसके परमाणुओं में केवल लघु-परास क्रम होता है, जमे हुए द्रव की तरह -- क्रिस्टलीय क्वार्ट्ज़ के विपरीत, जो भी सिलिका है पर जिसके परमाणु नियमित जालक में होते हैं। कथन 2 ग़लत है, और पहले से ही निकलता है: दीर्घ-परास क्रम न होने से कोई एक ताप नहीं होता जिस पर पूरी संरचना टूट जाए, इसलिए काँच तापों के एक परास में धीरे-धीरे नरम होता है; इसी से काँच फूँकने वाले उसे खींचकर आकार दे पाते हैं, जबकि बर्फ़ जैसा क्रिस्टलीय ठोस एक निश्चित बिंदु पर तीक्ष्णता से पिघलता है। "
  "कथन 3 ग़लत है: सामान्य सोडा-लाइम काँच सिलिका रेत को सोडा ऐश (सोडियम कार्बोनेट) और चूना-पत्थर के साथ पिघलाकर बनता है; सोडा गलन-ताप घटाता है और चूना काँच को टिकाऊ बनाता है। धातु ऑक्साइडों की थोड़ी मात्रा काँच को रंग देती है -- उदाहरण के लिए कोबाल्ट ऑक्साइड नीला रंग -- जबकि लेड ऑक्साइड क्रिस्टल काँच को चमक देता है।",
  "NCERT Class XII, Chemistry ('The Solid State', earlier editions); NCERT Class XI, Chemistry ('The p-Block Elements').",
  "l3-t6-sci-glass-amorphous-soda-lime", craft="precision")

# ================================================================ ASTRONOMY & EARTH SCIENCE (m-stmt)
S("Astronomy & Earth Science", "medium", "With reference to the asteroid Apophis, which will make a close approach to the Earth in April 2029, consider the following statements:",
  "क्षुद्रग्रह एपोफ़िस के संदर्भ में, जो अप्रैल 2029 में पृथ्वी के निकट से गुज़रेगा, निम्नलिखित कथनों पर विचार कीजिए:",
  ["It will pass closer to the Earth than the satellites in geostationary orbit.",
   "It will be visible to the naked eye from parts of the Earth during the close approach.",
   "Current estimates give it about a one-in-a-hundred chance of striking the Earth in 2029."],
  ["यह भूस्थिर कक्षा के उपग्रहों से भी अधिक पृथ्वी के निकट से गुज़रेगा।",
   "निकट आगमन के दौरान यह पृथ्वी के कुछ भागों से नंगी आँखों से दिखाई देगा।",
   "वर्तमान अनुमान इसे 2029 में पृथ्वी से टकराने की लगभग सौ में एक संभावना देते हैं।"],
  C3, 1,
  "Statements 1 and 2 are correct. Apophis, a rocky asteroid roughly 340 metres across, will pass about 32,000 km above the Earth's surface on 13 April 2029 -- inside the ring of geostationary satellites at about 36,000 km -- and will appear as a moving point of light visible without a telescope from Europe, Africa and parts of Asia. Such a close pass by an object this large is expected only about once in a thousand years, and the Earth's gravity is expected to alter its orbit and spin. "
  "Statement 3 is wrong: soon after its discovery in 2004 Apophis briefly appeared to pose a real risk, but radar and optical observations have since ruled out any impact in 2029 and for at least the next hundred years. Space agencies plan to study the encounter closely: NASA's OSIRIS-APEX spacecraft is to accompany the asteroid after the flyby, and the European Space Agency has proposed a mission to reach it ahead of the flyby.",
  "कथन 1 और 2 सही हैं। लगभग 340 मीटर चौड़ा चट्टानी क्षुद्रग्रह एपोफ़िस 13 अप्रैल 2029 को पृथ्वी की सतह से लगभग 32,000 किमी ऊपर से गुज़रेगा -- लगभग 36,000 किमी पर स्थित भूस्थिर उपग्रहों के घेरे के भीतर -- और यूरोप, अफ़्रीका और एशिया के कुछ भागों से दूरबीन के बिना चलते हुए प्रकाश-बिंदु के रूप में दिखेगा। इतने बड़े पिंड का इतना निकट से गुज़रना लगभग हज़ार वर्षों में एक बार ही अपेक्षित है, और पृथ्वी का गुरुत्व उसकी कक्षा और घूर्णन को बदल सकता है। "
  "कथन 3 ग़लत है: 2004 में खोज के तुरंत बाद एपोफ़िस कुछ समय के लिए वास्तविक ख़तरा लगा था, पर रडार और प्रकाशीय प्रेक्षणों ने तब से 2029 में और कम से कम अगले सौ वर्षों तक किसी टक्कर की संभावना समाप्त कर दी है। अंतरिक्ष एजेंसियाँ इस भेंट का बारीकी से अध्ययन करने की योजना बना रही हैं: नासा का ओसिरिस-एपेक्स अंतरिक्ष यान गुज़रने के बाद क्षुद्रग्रह के साथ चलेगा, और यूरोपीय अंतरिक्ष एजेंसी ने उसके गुज़रने से पहले उस तक पहुँचने का मिशन प्रस्तावित किया है।",
  "NASA, Center for Near-Earth Object Studies and Planetary Defense Coordination Office; European Space Agency, Planetary Defence Office.",
  "l3-t6-sci-apophis-2029-flyby", craft="precision")

# ================================================================ BIOLOGY, HEALTH & BIOTECHNOLOGY (m-stmt)
S("Biology, Health & Biotechnology", "medium", "With reference to human metapneumovirus (HMPV), consider the following statements:",
  "ह्यूमन मेटान्यूमोवायरस (एचएमपीवी) के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["It was first identified in 2001, in the Netherlands.",
   "It belongs to the same family of viruses as the respiratory syncytial virus (RSV).",
   "Infants, older people and those with weakened immunity face the highest risk of severe disease.",
   "As of 2025, there was no specific antiviral drug or approved vaccine against it, and treatment was supportive."],
  ["इसकी पहचान पहली बार 2001 में नीदरलैंड में हुई।",
   "यह रेस्पिरेटरी सिंसिशियल वायरस (आरएसवी) वाले विषाणु-कुल से संबंधित है।",
   "शिशुओं, वृद्धों और कमज़ोर प्रतिरक्षा वाले लोगों को गंभीर रोग का सबसे अधिक जोखिम है।",
   "2025 तक इसके विरुद्ध कोई विशिष्ट विषाणुरोधी दवा या स्वीकृत टीका नहीं था, और उपचार सहायक था।"],
  C4, 3,
  "All four are correct. HMPV was identified by Dutch researchers in children with respiratory illness in 2001, though stored samples show it had been circulating for decades. Like RSV it belongs to the family Pneumoviridae; it spreads through droplets and contact, mostly in winter and spring, and causes symptoms from a common cold to bronchiolitis and pneumonia in the vulnerable. "
  "In January 2025, after reports of a rise in respiratory infections in China, cases detected in India drew wide attention; the Union Health Ministry and the ICMR explained that the virus was not new, was already circulating in India, and that surveillance showed no unusual increase. With no specific drug or vaccine, care consists of fluids, oxygen and treatment of complications, and prevention relies on hygiene. The episode is an example of how genomic and respiratory surveillance helps tell a known seasonal virus from a new threat.",
  "चारों कथन सही हैं। एचएमपीवी की पहचान डच शोधकर्ताओं ने 2001 में श्वसन रोग वाले बच्चों में की, यद्यपि संग्रहीत नमूने दिखाते हैं कि यह दशकों से फैल रहा था। आरएसवी की तरह यह न्यूमोविरिडी कुल का है; यह बूँदों और संपर्क से फैलता है, अधिकतर सर्दी और वसंत में, और कमज़ोर लोगों में सामान्य सर्दी से लेकर ब्रोंकियोलाइटिस और निमोनिया तक के लक्षण पैदा करता है। "
  "जनवरी 2025 में, चीन में श्वसन संक्रमणों में वृद्धि की ख़बरों के बाद, भारत में पाए गए मामलों ने व्यापक ध्यान खींचा; केंद्रीय स्वास्थ्य मंत्रालय और आईसीएमआर ने स्पष्ट किया कि वायरस नया नहीं है, भारत में पहले से फैल रहा है, और निगरानी में कोई असामान्य वृद्धि नहीं दिखी। कोई विशिष्ट दवा या टीका न होने से देखभाल में तरल, ऑक्सीजन और जटिलताओं का उपचार शामिल है, और बचाव स्वच्छता पर निर्भर है। यह प्रसंग दिखाता है कि जीनोमिक और श्वसन निगरानी किसी ज्ञात मौसमी वायरस को नए ख़तरे से अलग पहचानने में कैसे सहायक है।",
  "Ministry of Health and Family Welfare (PIB, January 2025); Indian Council of Medical Research; World Health Organization.",
  "l3-t6-sci-hmpv-2025", craft="recall")

# ================================================================ DEFENCE, AEROSPACE & SECURITY TECHNOLOGY (m-stmt)
S("Defence, Aerospace & Security Technology", "medium", "With reference to interference with satellite navigation (GNSS) signals, consider the following statements:",
  "उपग्रह नौवहन (जीएनएसएस) संकेतों में हस्तक्षेप के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Spoofing broadcasts counterfeit satellite-like signals so that a receiver computes a false position or time.",
   "Jamming is harder to detect than spoofing, because a jammed receiver continues to show a believable position.",
   "Civil aircraft flying near India's western border have not been affected by such interference, because civil GPS signals are encrypted."],
  ["स्पूफ़िंग नक़ली उपग्रह-जैसे संकेत प्रसारित करती है ताकि रिसीवर ग़लत स्थिति या समय की गणना करे।",
   "जैमिंग का पता लगाना स्पूफ़िंग से कठिन है, क्योंकि जैम किया गया रिसीवर विश्वसनीय स्थिति दिखाता रहता है।",
   "भारत की पश्चिमी सीमा के निकट उड़ते नागरिक विमान ऐसे हस्तक्षेप से प्रभावित नहीं हुए हैं, क्योंकि नागरिक जीपीएस संकेत कूटबद्ध होते हैं।"],
  C3, 0,
  "Only statement 1 is correct. Navigation satellites transmit very weak signals from about 20,000 km away, so a ground transmitter can easily overpower them. Jamming simply drowns them in noise, and the receiver loses its fix -- an obvious failure. Spoofing is subtler and more dangerous: by imitating genuine signals it can drag a receiver's position or clock away step by step without raising an alarm, so statement 2 has the two reversed. "
  "Statement 3 is wrong: the open civil signals of GPS are not encrypted, which is what makes spoofing possible, and the civil aviation regulator issued an advisory in 2023 after pilots reported interference; the government has since told Parliament of hundreds of such incidents in the Amritsar and Jammu region. Defences include receivers that use several constellations, encrypted military or restricted services such as NavIC's restricted service, antennas that reject interference, and inertial navigation as a backup.",
  "केवल कथन 1 सही है। नौवहन उपग्रह लगभग 20,000 किमी दूर से बहुत क्षीण संकेत भेजते हैं, इसलिए धरती का कोई ट्रांसमीटर उन्हें आसानी से दबा सकता है। जैमिंग उन्हें शोर में डुबो देती है, और रिसीवर अपनी स्थिति खो देता है -- एक स्पष्ट विफलता। स्पूफ़िंग अधिक सूक्ष्म और ख़तरनाक है: असली संकेतों की नक़ल करके वह बिना चेतावनी दिए रिसीवर की स्थिति या घड़ी को धीरे-धीरे भटका सकती है, इसलिए कथन 2 में दोनों उलट दिए गए हैं। "
  "कथन 3 ग़लत है: जीपीएस के खुले नागरिक संकेत कूटबद्ध नहीं होते, इसी से स्पूफ़िंग संभव होती है, और पायलटों द्वारा हस्तक्षेप की सूचना के बाद नागर विमानन विनियामक ने 2023 में परामर्श जारी किया; सरकार ने तब से संसद को अमृतसर और जम्मू क्षेत्र में ऐसी सैकड़ों घटनाओं की जानकारी दी है। बचाव में कई तारामंडलों का उपयोग करने वाले रिसीवर, नाविक की प्रतिबंधित सेवा जैसी कूटबद्ध सैन्य या प्रतिबंधित सेवाएँ, हस्तक्षेप को अस्वीकार करने वाले एंटीना, और विकल्प के रूप में जड़त्वीय नौवहन शामिल हैं।",
  "Directorate General of Civil Aviation, advisory circular on GNSS interference (2023); Ministry of Civil Aviation (replies in Parliament); Indian Space Research Organisation (NavIC).",
  "l3-t6-sci-gnss-jamming-spoofing", craft="inference")

# ================================================================ PHYSICS & EVERYDAY SCIENCE (m-stmt)
S("Physics & Everyday Science", "medium", "With reference to Cherenkov radiation, consider the following statements:",
  "चेरेनकोव विकिरण के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["The blue glow seen in the water around the core of a pool-type research reactor is produced by charged particles travelling faster than light travels in water.",
   "It shows that particles can travel faster than light does in a vacuum."],
  ["पूल-प्रकार के अनुसंधान रिएक्टर के कोर के चारों ओर पानी में दिखने वाली नीली चमक उन आवेशित कणों से उत्पन्न होती है जो पानी में प्रकाश की चाल से तेज़ चलते हैं।",
   "यह दिखाता है कि कण निर्वात में प्रकाश की चाल से भी तेज़ चल सकते हैं।"],
  T2, 0,
  "Only statement 1 is correct. Light slows down in a medium: in water, whose refractive index is about 1.33, it travels at roughly three-quarters of its speed in a vacuum. High-energy electrons emitted by fission products can move faster than that, and as they do they disturb the water's molecules so that the emitted light piles up into a cone -- an optical counterpart of the sonic boom of a supersonic aircraft. The light is mostly blue because the emission is strongest at short wavelengths. "
  "Statement 2 is wrong: nothing with mass reaches, let alone exceeds, the speed of light in a vacuum; the particles only outrun light in the medium. The effect, discovered by Pavel Cherenkov and explained by Ilya Frank and Igor Tamm, who shared the 1958 Nobel Prize, is put to use in giant water and ice detectors that catch the faint flashes from neutrinos and cosmic rays.",
  "केवल कथन 1 सही है। माध्यम में प्रकाश धीमा हो जाता है: पानी में, जिसका अपवर्तनांक लगभग 1.33 है, वह निर्वात की अपनी चाल के लगभग तीन-चौथाई से चलता है। विखंडन उत्पादों से निकले उच्च-ऊर्जा इलेक्ट्रॉन इससे तेज़ चल सकते हैं, और ऐसा करते हुए वे पानी के अणुओं को इस तरह विचलित करते हैं कि उत्सर्जित प्रकाश एक शंकु में जमा होता है -- पराध्वनिक विमान के ध्वनि-बूम का प्रकाशीय समकक्ष। प्रकाश अधिकतर नीला होता है क्योंकि उत्सर्जन लघु तरंगदैर्घ्यों पर सबसे प्रबल होता है। "
  "कथन 2 ग़लत है: द्रव्यमान वाली कोई वस्तु निर्वात में प्रकाश की चाल तक नहीं पहुँचती, उससे आगे निकलना तो दूर; कण केवल माध्यम में प्रकाश से आगे निकलते हैं। पावेल चेरेनकोव द्वारा खोजा गया और इल्या फ़्रैंक तथा इगोर टैम द्वारा समझाया गया यह प्रभाव, जिसके लिए तीनों को 1958 का नोबेल पुरस्कार मिला, पानी और बर्फ़ के विशाल संसूचकों में प्रयुक्त होता है जो न्यूट्रिनो और कॉस्मिक किरणों की क्षीण चमक पकड़ते हैं।",
  "NCERT Class XII, Physics ('Ray Optics and Optical Instruments' and 'Nuclei'); Bhabha Atomic Research Centre.",
  "l3-t6-sci-cherenkov-radiation", craft="inference")

# ================================================================ SPACE TECHNOLOGY & MISSIONS (h-SI)
A("Space Technology & Missions", "hard",
  "The semi-cryogenic engine that ISRO is developing for the LVM3 will burn liquid hydrogen with liquid oxygen.",
  "इसरो द्वारा एलवीएम3 के लिए विकसित किया जा रहा अर्ध-क्रायोजेनिक इंजन द्रव हाइड्रोजन को द्रव ऑक्सीजन के साथ जलाएगा।",
  "In a semi-cryogenic engine only the oxidiser is a cryogenic liquid; the fuel can be stored at ordinary temperatures.",
  "अर्ध-क्रायोजेनिक इंजन में केवल ऑक्सीकारक क्रायोजेनिक द्रव होता है; ईंधन सामान्य तापों पर संग्रहीत किया जा सकता है।",
  3,
  "Statement I is incorrect but Statement II is correct. ISRO's semi-cryogenic engine, of about 2,000 kN thrust, burns a highly refined kerosene with liquid oxygen; it is meant to power a new core stage that will replace the LVM3's liquid stage, which uses storable but toxic hypergolic propellants, and so raise the rocket's payload capacity. Liquid hydrogen, which must be kept at about -253 °C, is the fuel of a fully cryogenic engine such as the one in the LVM3's upper stage. "
  "Kerosene is far denser than liquid hydrogen, so its tanks are smaller and the engine produces high thrust -- well suited to a lower stage -- while being cheaper and safer to handle than hypergolic fuels; only the liquid oxygen, at about -183 °C, needs cryogenic handling. The engine's components have been tested at the ISRO Propulsion Complex at Mahendragiri.",
  "कथन I ग़लत है पर कथन II सही है। लगभग 2,000 किलोन्यूटन प्रणोद वाला इसरो का अर्ध-क्रायोजेनिक इंजन अत्यंत परिष्कृत केरोसिन को द्रव ऑक्सीजन के साथ जलाता है; इसका उद्देश्य एक नए कोर चरण को शक्ति देना है जो एलवीएम3 के उस द्रव चरण का स्थान लेगा जिसमें संग्रहणीय पर विषैले हाइपरगोलिक प्रणोदक प्रयुक्त होते हैं, और इस प्रकार रॉकेट की नीतभार क्षमता बढ़ाना है। लगभग -253 °C पर रखा जाने वाला द्रव हाइड्रोजन पूर्ण क्रायोजेनिक इंजन का ईंधन है, जैसे एलवीएम3 के ऊपरी चरण का इंजन। "
  "केरोसिन द्रव हाइड्रोजन से कहीं अधिक घना है, इसलिए उसकी टंकियाँ छोटी होती हैं और इंजन अधिक प्रणोद देता है -- निचले चरण के लिए उपयुक्त -- और वह हाइपरगोलिक ईंधनों से सस्ता और सँभालने में सुरक्षित है; केवल लगभग -183 °C वाली द्रव ऑक्सीजन को क्रायोजेनिक सँभाल की आवश्यकता होती है। इंजन के घटकों का परीक्षण महेंद्रगिरि स्थित इसरो प्रणोदन परिसर में हुआ है।",
  "Indian Space Research Organisation, semi-cryogenic engine development updates; Department of Space, Annual Report.",
  "l3-t6-sci-semi-cryogenic-engine", craft="precision")

write("gs_l3_t6_f.sql")
