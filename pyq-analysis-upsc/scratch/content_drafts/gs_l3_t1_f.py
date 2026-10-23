# -*- coding: utf-8 -*-
"""Level 3 · Test 1 (GS Integrated Test 1) -- part F: Science & Technology (11) (upsc_l3_cell_targets.mjs 1).
S&T cells: Energy e-MCQ, m-stmt; IT e-MCQ, m-stmt; Chemistry h-MCQ, m-stmt; Space h-SI; Astronomy & Earth m-stmt;
Physics m-stmt; Biology m-stmt; Defence m-stmt.
Level 2 holds 211 S&T rows and Level 1 another 113, covering the usual batteries, storage, hydrogen, solar, nuclear,
missiles, NavIC, quantum, AI, vaccines and carbon materials. Every fact here was grepped against both and is one
neither tests: time-of-day electricity tariffs; what a VPN does (and CERT-In's 2022 record-keeping rule); the
piezoelectric effect; orbital decay, drag and the graveyard orbit; lab-grown diamonds; leap seconds; electrostatic
shielding in a car and a lift; antivenom and passive immunity; green ammonia as a hydrogen carrier; laser
directed-energy weapons; brain-computer interfaces. MCQ keys are pinned (pos), away from (d), and the statement keys
carry the paper's (d)s instead."""
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
  "The Electricity (Rights of Consumers) Amendment Rules, 2023 introduced time-of-day tariffs, under which electricity costs less during the solar hours of the day and more during the peak hours. What is the main purpose of such a tariff?",
  "विद्युत (उपभोक्ता अधिकार) संशोधन नियम, 2023 ने दिन के समय के अनुसार (टाइम-ऑफ़-डे) शुल्क शुरू किया, जिसके अंतर्गत दिन के सौर घंटों में बिजली सस्ती और व्यस्ततम (पीक) घंटों में महँगी होती है। ऐसे शुल्क का मुख्य उद्देश्य क्या है?",
  ["To shift demand into the hours when cheap solar power is plentiful and ease the evening peak",
   "To raise more revenue from farmers, who draw most of their power at night to run irrigation pumps",
   "To discourage households from installing rooftop solar by making grid power cheapest in daytime",
   "To keep the price of electricity the same for every consumer at every hour of the day"],
  ["माँग को उन घंटों में ले जाना जब सस्ती सौर बिजली प्रचुर हो, और शाम की पीक को कम करना",
   "किसानों से अधिक राजस्व जुटाना, जो सिंचाई पंप चलाने के लिए अपनी अधिकांश बिजली रात में लेते हैं",
   "दिन में ग्रिड बिजली सबसे सस्ती करके परिवारों को छत पर सौर पैनल लगाने से हतोत्साहित करना",
   "हर उपभोक्ता के लिए दिन के हर घंटे बिजली का दाम एक समान रखना"],
  0,
  "Solar plants fill the grid with power around midday, while demand peaks in the evening, after sunset, when the grid must lean on coal, gas and storage. Under the 2023 rules the tariff during the solar hours (eight hours a day, fixed by the State commission) is at least 10 to 20 per cent below the normal rate and the peak-hour tariff at least 10 to 20 per cent above it, so consumers with smart meters gain by moving flexible loads -- pumping water, charging vehicles, running machines -- into the day. "
  "The tariff applies to commercial and industrial consumers with a demand of 10 kW or more from April 2024 and to most other consumers from April 2025. Agricultural consumers are excluded, so the farmer option is wrong, and cheaper daytime power complements rooftop solar rather than discouraging it.",
  "सौर संयंत्र दोपहर के आसपास ग्रिड को बिजली से भर देते हैं, जबकि माँग शाम को, सूर्यास्त के बाद, चरम पर होती है, जब ग्रिड को कोयले, गैस और भंडारण पर निर्भर होना पड़ता है। 2023 के नियमों के अंतर्गत सौर घंटों (राज्य आयोग द्वारा तय, दिन के आठ घंटे) का शुल्क सामान्य दर से कम से कम 10 से 20 प्रतिशत कम और पीक घंटों का शुल्क उससे कम से कम 10 से 20 प्रतिशत अधिक होता है, इसलिए स्मार्ट मीटर वाले उपभोक्ता लचीले भार -- पानी चढ़ाना, वाहन चार्ज करना, मशीनें चलाना -- दिन में ले जाकर लाभ उठाते हैं। "
  "यह शुल्क 10 kW या अधिक माँग वाले वाणिज्यिक और औद्योगिक उपभोक्ताओं पर अप्रैल 2024 से और अधिकांश अन्य उपभोक्ताओं पर अप्रैल 2025 से लागू है। कृषि उपभोक्ता इससे बाहर हैं, इसलिए किसानों वाला विकल्प ग़लत है, और दिन की सस्ती बिजली छत के सौर पैनलों को हतोत्साहित नहीं करती बल्कि उनकी पूरक है।",
  "Ministry of Power, Electricity (Rights of Consumers) Amendment Rules, 2023.",
  "l3-t1-sci-time-of-day-tariff", pos=0, craft="application")

S(EN, "medium", "Consider the following statements about green ammonia:",
  "हरित अमोनिया के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is made by combining hydrogen produced by electrolysis using renewable electricity with nitrogen drawn from the air.",
   "It is easier to store and ship than hydrogen, since ammonia turns liquid at about −33 °C at normal atmospheric pressure.",
   "Burning ammonia releases no carbon dioxide, though it can produce oxides of nitrogen.",
   "In India, auctions held under the National Green Hydrogen Mission have sought green ammonia for fertiliser plants, which otherwise make ammonia from natural gas."],
  ["यह नवीकरणीय बिजली से विद्युत-अपघटन द्वारा बने हाइड्रोजन को हवा से ली गई नाइट्रोजन के साथ मिलाकर बनाई जाती है।",
   "इसे हाइड्रोजन की तुलना में भंडारित करना और जहाज़ से भेजना आसान है, क्योंकि अमोनिया सामान्य वायुमंडलीय दाब पर लगभग −33 °C पर द्रव बन जाती है।",
   "अमोनिया जलाने पर कार्बन डाइऑक्साइड नहीं निकलती, यद्यपि नाइट्रोजन के ऑक्साइड बन सकते हैं।",
   "भारत में राष्ट्रीय हरित हाइड्रोजन मिशन के अंतर्गत हुई नीलामियों में उर्वरक संयंत्रों के लिए हरित अमोनिया माँगी गई है, जो अन्यथा प्राकृतिक गैस से अमोनिया बनाते हैं।"],
  C4, 3,
  "All four statements are correct. Ammonia (NH3) is made by the Haber process, which joins nitrogen and hydrogen over an iron catalyst at high pressure; it is 'green' when the hydrogen comes from splitting water with renewable power rather than from natural gas, whose use releases carbon dioxide. "
  "Hydrogen has to be cooled to about −253 °C or squeezed to very high pressure, while ammonia liquefies easily and can use existing tankers and terminals, so it is a favoured way of carrying hydrogen; it can be burnt directly in ships' engines and power plants, or cracked back into hydrogen. Its drawbacks are its toxicity and the oxides of nitrogen formed when it burns. "
  "In 2025 the Solar Energy Corporation of India ran auctions under the Mission's SIGHT programme to supply green ammonia to fertiliser units, the largest users of ammonia in India.",
  "चारों कथन सही हैं। अमोनिया (NH3) हेबर प्रक्रम से बनती है, जो उच्च दाब पर लोहे के उत्प्रेरक की उपस्थिति में नाइट्रोजन और हाइड्रोजन को जोड़ता है; यह 'हरित' तब होती है जब हाइड्रोजन प्राकृतिक गैस से नहीं, जिसके उपयोग से कार्बन डाइऑक्साइड निकलती है, बल्कि नवीकरणीय बिजली से पानी के अपघटन से आए। "
  "हाइड्रोजन को लगभग −253 °C तक ठंडा करना या बहुत ऊँचे दाब पर दबाना पड़ता है, जबकि अमोनिया आसानी से द्रवित होती है और मौजूदा टैंकरों और टर्मिनलों का उपयोग कर सकती है, इसलिए यह हाइड्रोजन ढोने का एक पसंदीदा तरीक़ा है; इसे जहाज़ों के इंजनों और बिजलीघरों में सीधे जलाया जा सकता है, या वापस हाइड्रोजन में तोड़ा जा सकता है। इसकी कमियाँ इसकी विषाक्तता और जलने पर बनने वाले नाइट्रोजन के ऑक्साइड हैं। "
  "2025 में भारतीय सौर ऊर्जा निगम ने मिशन के SIGHT कार्यक्रम के अंतर्गत उर्वरक इकाइयों, जो भारत में अमोनिया की सबसे बड़ी उपयोगकर्ता हैं, को हरित अमोनिया की आपूर्ति के लिए नीलामियाँ कीं।",
  "Ministry of New and Renewable Energy (National Green Hydrogen Mission; SIGHT programme); NCERT Class XI, Chemistry (Equilibrium: the Haber process).",
  "l3-t1-sci-green-ammonia-carrier", craft="linkage")

# ================================================================ IT, COMMUNICATION & EMERGING TECHNOLOGIES (e-MCQ, m-stmt)
M(IT, "easy",
  "When a person goes online through a virtual private network (VPN), what does the VPN mainly do?",
  "जब कोई व्यक्ति वर्चुअल प्राइवेट नेटवर्क (VPN) के माध्यम से इंटरनेट का उपयोग करता है, तो VPN मुख्य रूप से क्या करता है?",
  ["It encrypts the traffic between the device and the VPN server, hiding it from the local network",
   "It scans every file the person downloads and removes any virus or other malware found on the device",
   "It makes the person fully anonymous, even to the websites and apps into which the person has logged in",
   "It speeds up the connection by compressing all the data that the device sends and receives"],
  ["यह डिवाइस और VPN सर्वर के बीच के ट्रैफ़िक को एन्क्रिप्ट करके स्थानीय नेटवर्क से छिपा देता है",
   "यह व्यक्ति द्वारा डाउनलोड की गई हर फ़ाइल को जाँचता है और डिवाइस पर मिला हर वायरस या मैलवेयर हटा देता है",
   "यह व्यक्ति को पूरी तरह गुमनाम बना देता है, उन वेबसाइटों और ऐप्स के लिए भी जिनमें वह लॉग इन है",
   "यह डिवाइस द्वारा भेजे और प्राप्त किए जाने वाले सारे डेटा को संपीड़ित करके कनेक्शन तेज़ कर देता है"],
  0,
  "A VPN builds an encrypted 'tunnel' from the device to a server run by the VPN provider: the local Wi-Fi network or the internet service provider sees only scrambled data going to that server, and websites see the server's address instead of the user's. "
  "It does not remove malware, and it cannot hide a user from a service the user has logged into, which still knows the account; the extra encryption and the longer route usually slow the connection a little. "
  "The trust simply shifts to the VPN provider -- which is why CERT-In's directions of April 2022 require VPN service providers in India to keep accurate records of their subscribers for five years.",
  "VPN डिवाइस से VPN प्रदाता द्वारा चलाए जाने वाले सर्वर तक एक एन्क्रिप्टेड 'सुरंग' बनाता है: स्थानीय वाई-फ़ाई नेटवर्क या इंटरनेट सेवा प्रदाता को उस सर्वर तक जाता केवल उलझा हुआ डेटा दिखता है, और वेबसाइटों को उपयोगकर्ता के पते के बजाय सर्वर का पता दिखता है। "
  "यह मैलवेयर नहीं हटाता, और उपयोगकर्ता को उस सेवा से नहीं छिपा सकता जिसमें उपयोगकर्ता ने लॉग इन किया है, क्योंकि वह खाते को जानती है; अतिरिक्त एन्क्रिप्शन और लंबा मार्ग आम तौर पर कनेक्शन को थोड़ा धीमा करते हैं। "
  "भरोसा बस VPN प्रदाता पर चला जाता है -- इसीलिए CERT-In के अप्रैल 2022 के निर्देश भारत में VPN सेवा प्रदाताओं से अपने ग्राहकों के सटीक रिकॉर्ड पाँच वर्ष तक रखने की अपेक्षा करते हैं।",
  "CERT-In, Directions under section 70B(6) of the Information Technology Act, 2000 (April 2022); Ministry of Electronics and Information Technology.",
  "l3-t1-sci-vpn-encrypted-tunnel", pos=1, craft="precision")

S(IT, "medium", "With reference to brain-computer interfaces, consider the following statements:",
  "ब्रेन-कंप्यूटर इंटरफ़ेस के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["They pick up the electrical activity of the brain and translate it into commands, such as moving a cursor or a robotic arm.",
   "They can work only with electrodes implanted in the brain through surgery."],
  ["वे मस्तिष्क की विद्युत गतिविधि को ग्रहण करके उसे कर्सर या रोबोटिक भुजा चलाने जैसे आदेशों में बदलते हैं।",
   "वे केवल शल्यक्रिया द्वारा मस्तिष्क में प्रत्यारोपित इलेक्ट्रोडों के साथ ही काम कर सकते हैं।"],
  T2, 0,
  "Only statement 1 is correct. Nerve cells communicate by electrical impulses; a brain-computer interface records these signals and uses software, increasingly machine learning, to decode intended movements or words, letting paralysed people type, speak through a synthesiser or move a prosthetic limb. "
  "Implanted electrodes give the clearest signals, but non-invasive systems with electrodes on the scalp (EEG caps) also work, though the skull blurs and weakens what they pick up. "
  "Because such devices read neural data, they raise new questions of privacy; Chile amended its constitution in 2021 to protect mental integrity and brain activity.",
  "केवल कथन 1 सही है। तंत्रिका कोशिकाएँ विद्युत आवेगों से संवाद करती हैं; ब्रेन-कंप्यूटर इंटरफ़ेस इन संकेतों को रिकॉर्ड करता है और सॉफ़्टवेयर, जिसमें बढ़ते रूप में मशीन लर्निंग है, से इच्छित गतियों या शब्दों को पढ़ता है, जिससे लकवाग्रस्त लोग टाइप कर सकते हैं, सिंथेसाइज़र से बोल सकते हैं या कृत्रिम अंग चला सकते हैं। "
  "प्रत्यारोपित इलेक्ट्रोड सबसे स्पष्ट संकेत देते हैं, पर खोपड़ी की त्वचा पर लगे इलेक्ट्रोडों वाली अनाक्रामक प्रणालियाँ (EEG कैप) भी काम करती हैं, यद्यपि खोपड़ी उनके पकड़े संकेतों को धुँधला और कमज़ोर कर देती है। "
  "चूँकि ऐसे उपकरण तंत्रिका-डेटा पढ़ते हैं, वे निजता के नए प्रश्न उठाते हैं; चिली ने 2021 में मानसिक अखंडता और मस्तिष्क गतिविधि की रक्षा के लिए अपने संविधान में संशोधन किया।",
  "NCERT Class XI, Biology (Neural Control and Coordination).",
  "l3-t1-sci-brain-computer-interface", craft="precision")

# ================================================================ CHEMISTRY & MATERIALS (h-MCQ, m-stmt)
M(CH, "hard",
  "A quartz watch keeps time, a push-button gas lighter makes a spark without any battery, and an ultrasound probe sends sound pulses into the body and picks up their echoes. The property shared by the crystals or ceramics at the heart of all three devices is that they:",
  "क्वार्ट्ज़ घड़ी समय बताती है, बटन दबाने वाला गैस लाइटर बिना बैटरी के चिंगारी पैदा करता है, और अल्ट्रासाउंड प्रोब शरीर में ध्वनि स्पंद भेजता है और उनकी प्रतिध्वनियाँ पकड़ता है। तीनों उपकरणों के केंद्र में लगे क्रिस्टलों या सिरेमिकों का साझा गुण यह है कि वे:",
  ["develop a voltage when squeezed and flex slightly when a voltage is applied",
   "lose all electrical resistance when they are cooled below a critical temperature",
   "give out light of a colour that depends on the size of their tiny particles",
   "spring back to a remembered shape when they are warmed above a set temperature"],
  ["दबाए जाने पर वोल्टेज उत्पन्न करते हैं और वोल्टेज लगाने पर थोड़ा मुड़ते-फैलते हैं",
   "एक क्रांतिक तापमान से नीचे ठंडा किए जाने पर अपना सारा विद्युत प्रतिरोध खो देते हैं",
   "अपने सूक्ष्म कणों के आकार पर निर्भर रंग का प्रकाश उत्सर्जित करते हैं",
   "एक तय तापमान से ऊपर गर्म किए जाने पर अपने याद रखे गए आकार में लौट आते हैं"],
  0,
  "All three rely on the piezoelectric effect. Squeezing a piezoelectric crystal such as quartz, or a ceramic such as lead zirconate titanate, separates charge across it and produces a voltage; applying a voltage makes it change shape. "
  "The lighter uses the first: a spring-loaded hammer strikes the crystal and a voltage of several thousand volts jumps a gap as a spark. The watch uses the second: a voltage keeps a tiny quartz tuning fork vibrating 32,768 times a second, and the circuit counts the vibrations. The ultrasound probe uses both, vibrating to send pulses and turning the returning echoes into electrical signals. "
  "The other options describe superconductors, quantum dots and shape-memory alloys such as nitinol.",
  "तीनों दाब-विद्युत (पीज़ोइलेक्ट्रिक) प्रभाव पर निर्भर हैं। क्वार्ट्ज़ जैसे दाब-विद्युत क्रिस्टल, या लेड ज़िरकोनेट टाइटेनेट जैसे सिरेमिक, को दबाने पर उसके आर-पार आवेश अलग होता है और वोल्टेज उत्पन्न होता है; वोल्टेज लगाने पर उसका आकार बदलता है। "
  "लाइटर पहले का उपयोग करता है: स्प्रिंग वाला हथौड़ा क्रिस्टल पर चोट करता है और कई हज़ार वोल्ट का वोल्टेज एक अंतराल को चिंगारी के रूप में पार करता है। घड़ी दूसरे का उपयोग करती है: वोल्टेज एक छोटे क्वार्ट्ज़ ट्यूनिंग फ़ोर्क को प्रति सेकंड 32,768 बार कंपित रखता है, और परिपथ इन कंपनों को गिनता है। अल्ट्रासाउंड प्रोब दोनों का उपयोग करता है, स्पंद भेजने के लिए कंपित होता है और लौटती प्रतिध्वनियों को विद्युत संकेतों में बदलता है। "
  "बाक़ी विकल्प अतिचालकों, क्वांटम डॉट्स और नाइटिनॉल जैसी आकार-स्मृति मिश्रधातुओं का वर्णन करते हैं।",
  "NCERT Class IX, Science (Sound: uses of ultrasound); NCERT Class XII, Physics Part I (Electrostatic Potential and Capacitance: polarisation of dielectrics).",
  "l3-t1-sci-piezoelectric-devices", pos=2, craft="linkage")

S(CH, "medium", "With reference to lab-grown diamonds, consider the following statements:",
  "प्रयोगशाला में उगाए गए हीरों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["They are made of silicon carbide, which is why they cost much less than mined diamonds.",
   "Being softer than natural diamonds, they can be told apart from them by a simple scratch test."],
  ["वे सिलिकॉन कार्बाइड से बने होते हैं, इसीलिए वे खनन से निकले हीरों से बहुत सस्ते होते हैं।",
   "प्राकृतिक हीरों से नरम होने के कारण उन्हें एक साधारण खरोंच परीक्षण से उनसे अलग पहचाना जा सकता है।"],
  T2, 3,
  "Neither statement is correct. A lab-grown diamond is real diamond: pure carbon in the same crystal lattice, with the same hardness, brilliance and chemical behaviour as a mined stone. It is grown either by subjecting carbon to high pressure and high temperature (HPHT) or by chemical vapour deposition (CVD), in which carbon from a gas such as methane settles layer by layer on a small diamond 'seed'. Silicon carbide is moissanite, a different stone sometimes sold as a diamond look-alike. "
  "Lab-grown and mined diamonds can be told apart only with laboratory instruments that read growth patterns, trace impurities and fluorescence, which is why disclosure and labelling matter. India, the world's main centre for cutting and polishing diamonds, has become a large producer of CVD diamonds, and the Union Budget 2023-24 provided a research grant to an IIT to develop the seeds and machines at home.",
  "कोई भी कथन सही नहीं है। प्रयोगशाला में उगाया गया हीरा असली हीरा है: उसी क्रिस्टल जालक में शुद्ध कार्बन, जिसकी कठोरता, चमक और रासायनिक व्यवहार खनन से निकले पत्थर जैसे ही हैं। इसे या तो कार्बन पर उच्च दाब और उच्च ताप (HPHT) डालकर या रासायनिक वाष्प निक्षेपण (CVD) से उगाया जाता है, जिसमें मीथेन जैसी गैस का कार्बन एक छोटे हीरे के 'बीज' पर परत-दर-परत जमता है। सिलिकॉन कार्बाइड मोइसानाइट है, एक अलग पत्थर जो कभी-कभी हीरे जैसे दिखने वाले पत्थर के रूप में बेचा जाता है। "
  "प्रयोगशाला में उगाए और खनन से निकले हीरों को केवल उन प्रयोगशाला उपकरणों से अलग पहचाना जा सकता है जो वृद्धि के पैटर्न, सूक्ष्म अशुद्धियाँ और प्रतिदीप्ति पढ़ते हैं, इसीलिए प्रकटीकरण और लेबलिंग महत्त्वपूर्ण हैं। हीरों की कटाई और पॉलिश का विश्व का मुख्य केंद्र भारत CVD हीरों का भी बड़ा उत्पादक बन गया है, और केंद्रीय बजट 2023-24 ने बीज और मशीनें देश में विकसित करने के लिए एक IIT को शोध अनुदान दिया।",
  "NCERT Class X, Science (Carbon and its Compounds); Union Budget 2023-24 (Ministry of Finance).",
  "l3-t1-sci-lab-grown-diamonds", craft="precision")

# ================================================================ SPACE TECHNOLOGY & MISSIONS (h-SI)
A("Space Technology & Missions", "hard",
  "A dead satellite left at a height of about 400 km falls back into the atmosphere within a few years, whereas one left in geostationary orbit can stay up for a very long time.",
  "लगभग 400 km की ऊँचाई पर छोड़ा गया निष्क्रिय उपग्रह कुछ वर्षों के भीतर वायुमंडल में वापस गिर जाता है, जबकि भूस्थिर कक्षा में छोड़ा गया उपग्रह बहुत लंबे समय तक ऊपर बना रह सकता है।",
  "At the height of the geostationary orbit, the Earth's gravitational pull is too weak to bring a satellite down.",
  "भूस्थिर कक्षा की ऊँचाई पर पृथ्वी का गुरुत्वाकर्षण खिंचाव किसी उपग्रह को नीचे लाने के लिए बहुत कमज़ोर होता है।",
  2,
  "Statement-I is correct and Statement-II is incorrect. What brings low satellites down is drag: a few hundred kilometres up there is still a trace of atmosphere, which steadily saps a satellite's speed so that its orbit sinks -- the International Space Station has to be boosted regularly for this reason. At about 36,000 km there is practically no air, so nothing lowers the orbit. "
  "Gravity there is still a little over 2 per cent of its strength at the surface, and it is this very pull that bends the satellite's path into a 24-hour circle: every satellite is falling all the time, but moving sideways fast enough to keep missing the Earth. "
  "That is why operators push retiring geostationary satellites a few hundred kilometres higher, into a 'graveyard' orbit, to keep the valuable slots clear, and why ISRO has set itself the goal of debris-free space missions by 2030.",
  "कथन-I सही है और कथन-II ग़लत है। निचले उपग्रहों को नीचे लाने वाला कारण कर्षण (ड्रैग) है: कुछ सौ किलोमीटर ऊपर अब भी वायुमंडल का अंश है, जो उपग्रह की गति लगातार घटाता है जिससे उसकी कक्षा नीचे आती है -- इसी कारण अंतरराष्ट्रीय अंतरिक्ष स्टेशन को नियमित रूप से ऊपर धकेलना पड़ता है। लगभग 36,000 km पर व्यावहारिक रूप से हवा नहीं है, इसलिए कक्षा को कोई नीचे नहीं लाता। "
  "वहाँ गुरुत्व अब भी सतह की अपनी शक्ति का 2 प्रतिशत से कुछ अधिक है, और यही खिंचाव उपग्रह के पथ को 24 घंटे के वृत्त में मोड़ता है: हर उपग्रह लगातार गिर रहा है, पर इतनी तेज़ी से बगल की ओर चल रहा है कि पृथ्वी से चूकता रहता है। "
  "इसीलिए संचालक सेवानिवृत्त हो रहे भूस्थिर उपग्रहों को कुछ सौ किलोमीटर ऊपर एक 'कब्रगाह' कक्षा में धकेल देते हैं, ताकि मूल्यवान स्थान ख़ाली रहें, और इसीलिए ISRO ने 2030 तक मलबा-मुक्त अंतरिक्ष मिशनों का लक्ष्य रखा है।",
  "ISRO (Indian Space Situational Assessment Report; Debris-Free Space Missions); NCERT Class XI, Physics (Gravitation: Earth satellites).",
  "l3-t1-sci-orbital-decay-graveyard", craft="inference")

# ================================================================ ASTRONOMY & EARTH SCIENCE (m-stmt)
S("Astronomy & Earth Science", "medium", "Consider the following statements about leap seconds:",
  "लीप सेकंड के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["They are added to Coordinated Universal Time (UTC) to keep it close to the time measured by the Earth's rotation, which does not keep perfectly steady time.",
   "A leap second is added every four years, along with the extra day in February.",
   "Under a decision taken in 2022, leap seconds are to be added more often from 2035."],
  ["इन्हें समन्वित सार्वभौमिक समय (UTC) में इसलिए जोड़ा जाता है ताकि वह पृथ्वी के घूर्णन से मापे गए समय के निकट रहे, जो पूरी तरह स्थिर समय नहीं रखता।",
   "हर चार वर्ष में, फ़रवरी के अतिरिक्त दिन के साथ, एक लीप सेकंड जोड़ा जाता है।",
   "2022 में लिए गए एक निर्णय के अंतर्गत 2035 से लीप सेकंड अधिक बार जोड़े जाने हैं।"],
  C3, 0,
  "Only statement 1 is correct. UTC is kept by atomic clocks, while the length of the day varies slightly with the tides, movements in the Earth's core and shifts of ice and water; leap seconds were inserted to keep UTC within 0.9 second of the time given by the Earth's rotation. "
  "They come irregularly, announced about six months ahead by the International Earth Rotation and Reference Systems Service -- 27 were added between 1972 and 2016, none since -- and have nothing to do with leap years. "
  "Because the sudden jumps disrupt computer networks and satellite navigation, the General Conference on Weights and Measures decided in 2022 to let the gap grow much larger in or before 2035, in effect ending leap seconds. In India, CSIR-National Physical Laboratory keeps Indian Standard Time and applies them.",
  "केवल कथन 1 सही है। UTC परमाणु घड़ियों से रखा जाता है, जबकि दिन की लंबाई ज्वार, पृथ्वी के क्रोड में हलचल और बर्फ़ व पानी के खिसकने से थोड़ी बदलती रहती है; लीप सेकंड इसलिए जोड़े गए ताकि UTC पृथ्वी के घूर्णन से मिलने वाले समय से 0.9 सेकंड के भीतर रहे। "
  "वे अनियमित रूप से आते हैं, जिनकी घोषणा अंतरराष्ट्रीय पृथ्वी घूर्णन और संदर्भ प्रणाली सेवा लगभग छह महीने पहले करती है -- 1972 से 2016 के बीच 27 जोड़े गए, उसके बाद कोई नहीं -- और उनका लीप वर्ष से कोई संबंध नहीं है। "
  "चूँकि अचानक की ये छलाँगें कंप्यूटर नेटवर्कों और उपग्रह नेविगेशन को बाधित करती हैं, माप-तौल महासम्मेलन ने 2022 में निर्णय लिया कि 2035 तक या उससे पहले इस अंतर को बहुत बड़ा होने दिया जाए, जिससे वस्तुतः लीप सेकंड समाप्त हो जाते हैं। भारत में CSIR-राष्ट्रीय भौतिक प्रयोगशाला भारतीय मानक समय रखती है और उन्हें लागू करती है।",
  "International Earth Rotation and Reference Systems Service (Bulletin C); General Conference on Weights and Measures, Resolution 4 (2022); CSIR-National Physical Laboratory.",
  "l3-t1-sci-leap-seconds", craft="precision")

# ================================================================ PHYSICS & EVERYDAY SCIENCE (m-stmt)
S("Physics & Everyday Science", "medium", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["A person sitting in a closed metal-bodied car is fairly safe from lightning, mainly because the current flows through the metal shell around the occupants.",
   "The rubber tyres, by insulating the car from the ground, are the main reason for this safety.",
   "A mobile phone gets a stronger signal inside a closed metal lift, because the metal walls gather and focus the radio waves."],
  ["बंद धातु-ढाँचे वाली कार में बैठा व्यक्ति आकाशीय बिजली से काफ़ी सुरक्षित रहता है, मुख्यतः इसलिए कि धारा सवारों के चारों ओर धातु के खोल से होकर बहती है।",
   "रबर के टायर, कार को ज़मीन से विद्युतरोधी बनाकर, इस सुरक्षा का मुख्य कारण हैं।",
   "बंद धातु की लिफ़्ट के भीतर मोबाइल फ़ोन को अधिक मज़बूत सिग्नल मिलता है, क्योंकि धातु की दीवारें रेडियो तरंगों को इकट्ठा और केंद्रित करती हैं।"],
  C3, 0,
  "Only statement 1 is correct. A closed conducting shell keeps electric fields out of the space inside it -- the electrostatic shielding of NCERT's Class XII Physics. Lightning striking a car runs over the metal body and on to the ground, and the occupants are safe as long as they do not touch the metal. "
  "The tyres do not explain it: a bolt that has crossed kilometres of air easily crosses a few centimetres of rubber, and a soft-top or fibreglass car gives little protection. "
  "The same shielding works on radio waves, which is why a phone loses its signal inside a metal lift: the lift acts as a Faraday cage, not a collector.",
  "केवल कथन 1 सही है। बंद चालक खोल अपने भीतर के स्थान से विद्युत क्षेत्रों को बाहर रखता है -- NCERT की कक्षा XII भौतिकी का स्थिरवैद्युत परिरक्षण। कार पर गिरने वाली आकाशीय बिजली धातु के ढाँचे पर से होकर ज़मीन तक चली जाती है, और सवार तब तक सुरक्षित रहते हैं जब तक वे धातु को न छुएँ। "
  "टायर इसकी व्याख्या नहीं करते: किलोमीटरों तक हवा पार कर चुकी बिजली कुछ सेंटीमीटर रबर आसानी से पार कर लेती है, और कपड़े की छत या फ़ाइबरग्लास वाली कार कम सुरक्षा देती है। "
  "यही परिरक्षण रेडियो तरंगों पर भी काम करता है, इसीलिए धातु की लिफ़्ट के भीतर फ़ोन का सिग्नल चला जाता है: लिफ़्ट संग्राहक नहीं, फ़ैराडे पिंजरे का काम करती है।",
  "NCERT Class XII, Physics Part I (Electrostatic Potential and Capacitance: electrostatic shielding).",
  "l3-t1-sci-faraday-cage-car-lift", craft="application")

# ================================================================ BIOLOGY, HEALTH & BIOTECHNOLOGY (m-stmt)
S("Biology, Health & Biotechnology", "medium", "Consider the following statements about the antivenom used to treat snakebite in India:",
  "भारत में सर्पदंश के उपचार में प्रयुक्त प्रतिविष (एंटीवेनम) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is made from the blood of human volunteers who have been given small, safe doses of venom.",
   "Like a vaccine, it works by training the patient's own immune system to produce antibodies against the venom.",
   "Since the venom of a snake species is the same wherever it lives, an antivenom made from snakes caught in one region works equally well across the country."],
  ["यह उन मानव स्वयंसेवकों के रक्त से बनाया जाता है जिन्हें विष की छोटी, सुरक्षित ख़ुराकें दी गई हों।",
   "टीके की तरह, यह रोगी की अपनी प्रतिरक्षा प्रणाली को विष के विरुद्ध प्रतिरक्षी (एंटीबॉडी) बनाना सिखाकर काम करता है।",
   "चूँकि किसी साँप प्रजाति का विष हर जगह एक-सा होता है, इसलिए एक क्षेत्र में पकड़े गए साँपों से बना प्रतिविष पूरे देश में समान रूप से कारगर होता है।"],
  C3, 3,
  "None of the statements is correct. Antivenom is made by giving horses gradually rising doses of venom and purifying the antibodies from their blood; in India most of the venom comes from snakes caught by the Irula cooperative in Tamil Nadu, and the standard polyvalent product covers the 'big four' species. "
  "It gives passive immunity: the ready-made antibodies neutralise venom already in the body but do not train the patient's immune system, so the protection soon fades -- NCERT's own example of passive immunisation is the injection given after a snakebite. "
  "Venom varies between populations of the same species, so antivenom made from southern snakes works less well against some northern and north-eastern ones, and not at all against species it was not raised against; region-specific antivenoms are being developed for this reason. The National Action Plan for Prevention and Control of Snakebite Envenoming (2024) aims to halve snakebite deaths by 2030.",
  "कोई भी कथन सही नहीं है। प्रतिविष घोड़ों को विष की धीरे-धीरे बढ़ती ख़ुराकें देकर और उनके रक्त से प्रतिरक्षी शुद्ध करके बनाया जाता है; भारत में अधिकांश विष तमिलनाडु की इरुला सहकारी समिति द्वारा पकड़े गए साँपों से आता है, और मानक बहुसंयोजी उत्पाद 'बड़े चार' प्रजातियों को शामिल करता है। "
  "यह निष्क्रिय प्रतिरक्षा देता है: बने-बनाए प्रतिरक्षी शरीर में पहले से मौजूद विष को निष्क्रिय करते हैं पर रोगी की प्रतिरक्षा प्रणाली को प्रशिक्षित नहीं करते, इसलिए सुरक्षा जल्दी समाप्त हो जाती है -- NCERT का निष्क्रिय प्रतिरक्षीकरण का अपना उदाहरण सर्पदंश के बाद दिया जाने वाला इंजेक्शन है। "
  "एक ही प्रजाति की अलग-अलग आबादियों का विष भिन्न होता है, इसलिए दक्षिणी साँपों से बना प्रतिविष कुछ उत्तरी और पूर्वोत्तर साँपों के विरुद्ध कम कारगर होता है, और उन प्रजातियों के विरुद्ध बिल्कुल नहीं जिनके लिए वह बनाया ही नहीं गया; इसी कारण क्षेत्र-विशिष्ट प्रतिविष विकसित किए जा रहे हैं। सर्पदंश विषाक्तता की रोकथाम और नियंत्रण हेतु राष्ट्रीय कार्य योजना (2024) का लक्ष्य 2030 तक सर्पदंश से होने वाली मौतें आधी करना है।",
  "NCERT Class XII, Biology (Human Health and Disease: active and passive immunity); Ministry of Health and Family Welfare (National Action Plan for Prevention and Control of Snakebite Envenoming, 2024).",
  "l3-t1-sci-antivenom-passive-immunity", craft="linkage")

# ================================================================ DEFENCE, AEROSPACE & SECURITY TECHNOLOGY (m-stmt)
S("Defence, Aerospace & Security Technology", "medium", "With reference to laser-based directed-energy weapons, consider the following statements:",
  "लेज़र-आधारित निर्देशित-ऊर्जा हथियारों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Since a laser beam travels in a straight line at the speed of light, such weapons work equally well in fog, dust and rain.",
   "Each shot costs far more than an air-defence missile, which limits their use to high-value targets such as aircraft."],
  ["चूँकि लेज़र किरण प्रकाश की गति से सीधी रेखा में चलती है, इसलिए ऐसे हथियार कोहरे, धूल और वर्षा में भी समान रूप से कारगर रहते हैं।",
   "हर शॉट की लागत किसी वायु-रक्षा मिसाइल से कहीं अधिक होती है, जिससे उनका उपयोग विमान जैसे उच्च-मूल्य लक्ष्यों तक सीमित रहता है।"],
  T2, 3,
  "Neither statement is correct. A laser weapon has to hold its beam on one spot for some seconds to burn through, and fog, dust, smoke and rain scatter and absorb the beam and cut its range, so these weapons work best at short range in clear air. "
  "Their great advantage is cost: each shot uses only electrical power, a tiny fraction of the price of an interceptor missile, and the 'magazine' lasts as long as the power supply. That suits them to cheap and numerous targets such as drones and drone swarms rather than to aircraft. "
  "In April 2025 DRDO demonstrated a 30-kW vehicle-mounted laser system, the Mk-II(A), which disabled drones at the National Open Air Range in Kurnool.",
  "कोई भी कथन सही नहीं है। लेज़र हथियार को लक्ष्य को जलाकर भेदने के लिए अपनी किरण कुछ सेकंड तक एक बिंदु पर टिकाए रखनी पड़ती है, और कोहरा, धूल, धुआँ और वर्षा किरण को बिखेरते और सोखते हैं तथा उसकी मारक दूरी घटाते हैं, इसलिए ये हथियार साफ़ हवा में कम दूरी पर सबसे अच्छा काम करते हैं। "
  "उनका बड़ा लाभ लागत है: हर शॉट में केवल बिजली लगती है, जो किसी इंटरसेप्टर मिसाइल के दाम का छोटा-सा अंश है, और 'मैगज़ीन' तब तक चलती है जब तक बिजली की आपूर्ति है। इससे वे विमानों के बजाय ड्रोन और ड्रोन झुंड जैसे सस्ते और असंख्य लक्ष्यों के लिए उपयुक्त हैं। "
  "अप्रैल 2025 में DRDO ने 30-kW की वाहन-आरूढ़ लेज़र प्रणाली, Mk-II(A), का प्रदर्शन किया, जिसने कुर्नूल के नेशनल ओपन एयर रेंज में ड्रोनों को निष्क्रिय किया।",
  "Defence Research and Development Organisation (laser directed-energy weapon trial, April 2025); Ministry of Defence.",
  "l3-t1-sci-laser-directed-energy", craft="inference")

write("gs_l3_t1_f.sql")
