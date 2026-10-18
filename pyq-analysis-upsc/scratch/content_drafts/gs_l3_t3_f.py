# -*- coding: utf-8 -*-
"""Level 3 · Test 3 (GS Integrated Test 3) -- part F: Science & Technology (11) (upsc_l3_cell_targets.mjs 3).
Every fact was grepped against the Level-2 digests, all Level-1 drafts and Level 3 Tests 1-2, and is one none of them
tests: vehicle-to-grid; eSIMs; enzymatic browning; NavIC's inclined geosynchronous satellites; electrochromic glass;
the heliosphere and the Voyagers' crossing; resonance; tuberculosis, BPaLM and BCG; coal bed methane; air-independent
propulsion; 5G network slicing. MCQ keys are pinned (pos)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, T2

d.SUBJECT = "Science & Technology"
d.REQUIRE_CRAFT = True
EN = "Energy & Environmental Technology"
IT = "IT, Communication & Emerging Technologies"
CH = "Chemistry & Materials"

# ================================================================ ENERGY & ENVIRONMENTAL TECHNOLOGY (e-MCQ, m-stmt)
M(EN, "easy",
  "In 'vehicle-to-grid' (V2G) technology, an electric vehicle:",
  "'व्हीकल-टू-ग्रिड' (V2G) तकनीक में एक विद्युत वाहन:",
  ["can send electricity stored in its battery back to the grid when it is needed",
   "is charged only at night, when the grid supplies power at no cost to its owner",
   "runs on hydrogen piped to filling stations through the city gas grid",
   "charges itself wirelessly from coils laid under special roads as it moves"],
  ["ज़रूरत पड़ने पर अपनी बैटरी में संचित बिजली ग्रिड को वापस भेज सकता है",
   "केवल रात में चार्ज होता है, जब ग्रिड उसके स्वामी को बिना शुल्क बिजली देता है",
   "शहर गैस ग्रिड से भरण-केंद्रों तक पाइप से पहुँचे हाइड्रोजन पर चलता है",
   "चलते समय विशेष सड़कों के नीचे बिछी कुंडलियों से बिना तार के चार्ज होता है"],
  0,
  "V2G uses bidirectional chargers so that parked electric vehicles can act as a scattered battery bank: they charge when power is cheap and plentiful, such as at midday when solar output peaks, and feed some back during the evening peak or to steady the grid's frequency. "
  "With millions of vehicles parked most of the day, the stored energy could help absorb variable solar and wind power, though owners worry about extra battery wear and need fair payment; pilots are under discussion in India. The last option describes dynamic wireless charging, a different idea.",
  "V2G द्विदिशी चार्जरों का उपयोग करता है ताकि खड़े विद्युत वाहन बिखरे हुए बैटरी भंडार का काम करें: वे तब चार्ज होते हैं जब बिजली सस्ती और प्रचुर हो, जैसे दोपहर में जब सौर उत्पादन चरम पर हो, और शाम की पीक में या ग्रिड की आवृत्ति स्थिर रखने के लिए कुछ बिजली लौटाते हैं। "
  "दिन के अधिकांश समय खड़े लाखों वाहनों के कारण संचित ऊर्जा परिवर्ती सौर और पवन बिजली को समायोजित करने में मदद कर सकती है, यद्यपि स्वामी अतिरिक्त बैटरी घिसाव से चिंतित रहते हैं और उन्हें उचित भुगतान चाहिए; भारत में पायलटों पर चर्चा चल रही है। अंतिम विकल्प गतिशील बेतार चार्जिंग का वर्णन करता है, जो अलग विचार है।",
  "Ministry of Power; Central Electricity Authority (electric vehicle charging infrastructure).",
  "l3-t3-sci-vehicle-to-grid", pos=0, craft="application")

S(EN, "medium", "Consider the following statements about coal bed methane:",
  "कोल बेड मीथेन के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is produced by burning coal underground and collecting the gas that results.",
   "It is a renewable source of energy."],
  ["यह भूमिगत कोयले को जलाकर और उससे बनी गैस को एकत्र करके उत्पन्न होती है।",
   "यह ऊर्जा का नवीकरणीय स्रोत है।"],
  T2, 3,
  "Neither statement is correct. Coal bed methane is natural gas -- mostly methane -- that formed with the coal and stays held on the coal's surfaces by the pressure of water in the seam; it is produced by drilling wells and pumping out the water, which lowers the pressure and lets the gas flow, with no burning involved. Burning coal underground to make gas is a different process, underground coal gasification. "
  "Like coal itself, CBM is a fossil fuel and not renewable. India has CBM blocks in coalfields of Jharkhand, West Bengal and Madhya Pradesh; producing it also cuts the methane that would otherwise escape during mining, a safety and climate benefit.",
  "कोई भी कथन सही नहीं है। कोल बेड मीथेन प्राकृतिक गैस -- मुख्यतः मीथेन -- है जो कोयले के साथ बनी और परत में पानी के दाब से कोयले की सतहों पर रुकी रहती है; इसे कुएँ खोदकर और पानी बाहर निकालकर उत्पन्न किया जाता है, जिससे दाब घटता है और गैस बहने लगती है, जलाने की कोई आवश्यकता नहीं होती। भूमिगत कोयला जलाकर गैस बनाना एक अलग प्रक्रिया, भूमिगत कोयला गैसीकरण, है। "
  "कोयले की तरह CBM भी जीवाश्म ईंधन है और नवीकरणीय नहीं। भारत में झारखंड, पश्चिम बंगाल और मध्य प्रदेश के कोयला क्षेत्रों में CBM ब्लॉक हैं; इसका उत्पादन खनन के दौरान अन्यथा निकल जाने वाली मीथेन को भी घटाता है, जो सुरक्षा और जलवायु दोनों के लिए लाभ है।",
  "Ministry of Petroleum and Natural Gas; Directorate General of Hydrocarbons (coal bed methane).",
  "l3-t3-sci-coal-bed-methane", craft="precision")

# ================================================================ IT, COMMUNICATION & EMERGING TECHNOLOGIES (e-MCQ, m-stmt)
M(IT, "easy",
  "An eSIM is:",
  "eSIM क्या है?",
  ["a SIM card that works only for emergency calls whenever the mobile network is down",
   "a SIM that stores the user's photos and messages on the operator's cloud",
   "a SIM card made of biodegradable plastic to cut electronic waste",
   "a SIM built into the phone, loaded with an operator profile without a card"],
  ["ऐसा SIM कार्ड जो केवल मोबाइल नेटवर्क बंद होने पर आपातकालीन कॉल के लिए काम करता है",
   "ऐसा SIM जो उपयोगकर्ता की तस्वीरें और संदेश ऑपरेटर के क्लाउड पर रखता है",
   "इलेक्ट्रॉनिक कचरा घटाने के लिए जैव-निम्नीकरणीय प्लास्टिक से बना SIM कार्ड",
   "फ़ोन में ही लगा SIM, जिसमें बिना कार्ड के ऑपरेटर प्रोफ़ाइल डाली जाती है"],
  3,
  "An embedded SIM is a small chip soldered into the device; instead of inserting a plastic card, the user downloads an operator's profile, and can switch operators or hold several profiles without handling a card. "
  "Because there is no slot, eSIMs suit smartwatches, cars that must call for help automatically after a crash, and Internet-of-Things devices such as smart meters. In India, operators must complete the same customer verification (KYC) before activating an eSIM as for a physical SIM, to prevent fraud.",
  "एम्बेडेड SIM उपकरण में जड़ी एक छोटी चिप है; प्लास्टिक कार्ड डालने के बजाय उपयोगकर्ता ऑपरेटर की प्रोफ़ाइल डाउनलोड करता है, और कार्ड छुए बिना ऑपरेटर बदल सकता है या कई प्रोफ़ाइल रख सकता है। "
  "स्लॉट न होने के कारण eSIM स्मार्टवॉच, दुर्घटना के बाद अपने आप मदद बुलाने वाली कारों और स्मार्ट मीटर जैसे इंटरनेट-ऑफ़-थिंग्स उपकरणों के अनुकूल हैं। भारत में धोखाधड़ी रोकने के लिए ऑपरेटरों को eSIM चालू करने से पहले भौतिक SIM जैसा ही ग्राहक सत्यापन (KYC) करना होता है।",
  "Department of Telecommunications; Telecom Regulatory Authority of India.",
  "l3-t3-sci-esim", pos=3, craft="precision")

S(IT, "medium", "With reference to 'network slicing' in 5G networks, consider the following statements:",
  "5G नेटवर्क में 'नेटवर्क स्लाइसिंग' के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["It lets an operator run several virtual networks, each with its own speed, latency and reliability, on the same physical infrastructure.",
   "It requires building a separate set of physical towers for each slice."],
  ["यह ऑपरेटर को एक ही भौतिक अवसंरचना पर कई आभासी नेटवर्क चलाने देता है, जिनमें से हर एक की अपनी गति, विलंबता और विश्वसनीयता होती है।",
   "इसके लिए हर स्लाइस के लिए भौतिक टावरों का अलग समूह बनाना पड़ता है।"],
  T2, 0,
  "Only statement 1 is correct. Because 5G's core network is largely software-defined, an operator can carve it into logical 'slices': one tuned for very low latency and high reliability, for factory robots or remote surgery; another for huge numbers of low-power sensors; another for ordinary mobile broadband. "
  "Statement 2 is wrong: the slices share the same towers, spectrum and fibre, which is what makes the idea economical. Slicing raises policy questions too, such as how it fits with net neutrality, since it lets operators offer different quality to different users.",
  "केवल कथन 1 सही है। चूँकि 5G का कोर नेटवर्क अधिकतर सॉफ़्टवेयर-परिभाषित है, ऑपरेटर उसे तार्किक 'स्लाइसों' में बाँट सकता है: एक कारख़ाने के रोबोट या दूरस्थ शल्यक्रिया के लिए बहुत कम विलंबता और उच्च विश्वसनीयता वाला; दूसरा बहुत बड़ी संख्या में कम-ऊर्जा संवेदकों के लिए; तीसरा सामान्य मोबाइल ब्रॉडबैंड के लिए। "
  "कथन 2 ग़लत है: स्लाइस एक ही टावर, स्पेक्ट्रम और फ़ाइबर साझा करते हैं, यही इस विचार को किफ़ायती बनाता है। स्लाइसिंग नीतिगत प्रश्न भी उठाती है, जैसे यह नेट तटस्थता से कैसे मेल खाती है, क्योंकि यह ऑपरेटरों को अलग-अलग उपयोगकर्ताओं को अलग गुणवत्ता देने देती है।",
  "Department of Telecommunications; Telecom Regulatory Authority of India.",
  "l3-t3-sci-5g-network-slicing", craft="precision")

# ================================================================ CHEMISTRY & MATERIALS (h-MCQ, m-stmt)
M(CH, "hard",
  "A cut apple turns brown within minutes. The main reason is that:",
  "कटा हुआ सेब कुछ ही मिनटों में भूरा हो जाता है। इसका मुख्य कारण यह है कि:",
  ["iron in the fruit's tissue rusts as soon as it meets the oxygen of the air",
   "the fruit's sugars caramelise at room temperature once the skin is removed",
   "bacteria carried on the knife multiply over the cut surface within minutes",
   "an enzyme oxidises phenolic compounds once the cut cells meet the air"],
  ["फल के ऊतक का लोहा हवा की ऑक्सीजन से मिलते ही जंग खा जाता है",
   "छिलका हटने पर फल की शर्कराएँ कमरे के सामान्य ताप पर ही कैरामेल बन जाती हैं",
   "चाकू पर लगे जीवाणु कुछ ही मिनटों में कटी सतह पर बढ़ जाते हैं",
   "कोशिकाएँ हवा से मिलते ही एंज़ाइम फ़ीनॉलिक यौगिकों को ऑक्सीकृत करता है"],
  3,
  "Cutting breaks the cells and brings the enzyme polyphenol oxidase into contact with phenolic compounds and oxygen; the enzyme turns them into quinones, which link up into brown, melanin-like pigments. "
  "That is why lemon juice slows browning -- its acid lowers the pH at which the enzyme works best, and its vitamin C, an antioxidant, converts quinones back -- and why chilling and blanching help. The same reaction darkens tea leaves during processing, and apples genetically modified to make less of the enzyme stay white when cut.",
  "काटने से कोशिकाएँ टूटती हैं और एंज़ाइम पॉलीफ़ीनॉल ऑक्सीडेज़ फ़ीनॉलिक यौगिकों और ऑक्सीजन के संपर्क में आता है; एंज़ाइम उन्हें क्विनोन में बदलता है, जो जुड़कर भूरे, मेलानिन-जैसे वर्णक बनाते हैं। "
  "इसीलिए नींबू का रस भूरापन धीमा करता है -- उसका अम्ल उस pH को घटाता है जिस पर एंज़ाइम सबसे अच्छा काम करता है, और उसका विटामिन C, एक प्रतिऑक्सीकारक, क्विनोन को वापस बदलता है -- और इसीलिए ठंडा करना और उबालना मदद करते हैं। यही अभिक्रिया प्रसंस्करण के दौरान चाय की पत्तियों को काला करती है, और कम एंज़ाइम बनाने के लिए आनुवंशिक रूप से संशोधित सेब काटने पर सफ़ेद रहते हैं।",
  "NCERT Class XI, Biology (Biomolecules: enzymes); NCERT Class X, Science (Chemical Reactions: oxidation).",
  "l3-t3-sci-enzymatic-browning", pos=3, craft="application")

S(CH, "medium", "Consider the following statements about electrochromic 'smart glass':",
  "विद्युत-वर्णी (इलेक्ट्रोक्रोमिक) 'स्मार्ट ग्लास' के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It changes its tint when a small electric voltage is applied across it.",
   "It can cut the cooling load of buildings by blocking sunlight when needed.",
   "It works by heating the glass so that it partly melts and turns opaque."],
  ["इस पर हल्का विद्युत वोल्टेज लगाने पर इसका रंग गहरा-हल्का होता है।",
   "यह आवश्यकता पड़ने पर धूप रोककर इमारतों का शीतलन भार घटा सकता है।",
   "यह काँच को गर्म करके काम करता है जिससे वह आंशिक रूप से पिघलकर अपारदर्शी हो जाता है।"],
  C3, 1,
  "Statements 1 and 2 are correct. Electrochromic glass carries thin layers, often of tungsten oxide, through which a small voltage drives ions in or out; this changes how much light and heat the coating absorbs, and the glass darkens or clears over minutes, using power only while switching. "
  "Tinting windows on sunny afternoons reduces glare and air-conditioning demand, which is why such glass appears in energy-efficient buildings, aircraft windows and car sunroofs. Statement 3 is wrong: the effect is electrochemical, at room temperature; nothing melts.",
  "कथन 1 और 2 सही हैं। विद्युत-वर्णी काँच पर प्रायः टंगस्टन ऑक्साइड की पतली परतें होती हैं, जिनमें हल्का वोल्टेज आयनों को भीतर-बाहर ले जाता है; इससे परत द्वारा सोखे जाने वाले प्रकाश और ऊष्मा की मात्रा बदलती है, और काँच कुछ मिनटों में गहरा या साफ़ होता है, केवल बदलते समय बिजली लेते हुए। "
  "धूप वाली दोपहर में खिड़कियाँ गहरी करने से चकाचौंध और वातानुकूलन की माँग घटती है, इसीलिए ऐसा काँच ऊर्जा-कुशल इमारतों, विमान की खिड़कियों और कार की सनरूफ़ में दिखता है। कथन 3 ग़लत है: प्रभाव कमरे के ताप पर विद्युत-रासायनिक है; कुछ नहीं पिघलता।",
  "NCERT Class XII, Chemistry (Electrochemistry); Bureau of Energy Efficiency (Energy Conservation Building Code).",
  "l3-t3-sci-electrochromic-smart-glass", craft="application")

# ================================================================ SPACE TECHNOLOGY & MISSIONS (h-SI)
A("Space Technology & Missions", "hard",
  "Statement-I: Seen from the ground, some NavIC satellites trace a figure-of-eight path in the sky over India once a day.",
  "कथन-I: ज़मीन से देखने पर कुछ NavIC उपग्रह दिन में एक बार भारत के ऊपर आकाश में अंक आठ जैसा पथ बनाते हैं।",
  "Statement-II: These satellites are in geosynchronous orbits inclined to the equator, so they match the Earth's rotation period but swing north and south of the equator each day.",
  "कथन-II: ये उपग्रह भूमध्यरेखा से झुकी हुई भू-तुल्यकालिक कक्षाओं में हैं, इसलिए वे पृथ्वी के घूर्णन काल से मेल खाते हैं पर हर दिन भूमध्यरेखा के उत्तर और दक्षिण झूलते हैं।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I. A satellite with a 24-hour period stays over the same longitudes, but if its orbit is tilted to the equator it spends half the day north of the equator and half south, and the combination with slight variations in speed makes its ground track a figure of eight. "
  "NavIC mixes satellites in geostationary orbit with satellites in inclined geosynchronous orbit, so that all of them remain in view over India and its surroundings at all times, with good geometry for accurate fixes -- unlike GPS, whose satellites in medium Earth orbit circle the whole globe.",
  "दोनों कथन सही हैं, और कथन-II कथन-I की व्याख्या करता है। 24 घंटे की अवधि वाला उपग्रह उन्हीं देशांतरों के ऊपर रहता है, पर यदि उसकी कक्षा भूमध्यरेखा से झुकी हो तो वह आधा दिन भूमध्यरेखा के उत्तर और आधा दक्षिण बिताता है, और गति में हल्के बदलावों के साथ मिलकर उसका भू-पथ अंक आठ जैसा बनता है। "
  "NavIC भूस्थिर कक्षा के उपग्रहों को झुकी भू-तुल्यकालिक कक्षा के उपग्रहों से मिलाता है, ताकि सभी हर समय भारत और आसपास के क्षेत्र के ऊपर दिखते रहें, सटीक स्थिति-निर्धारण के लिए अच्छी ज्यामिति के साथ -- GPS के विपरीत, जिसके मध्यम भू-कक्षा के उपग्रह पूरे ग्लोब का चक्कर लगाते हैं।",
  "ISRO (NavIC); NCERT Class XI, Physics (Gravitation: Earth satellites).",
  "l3-t3-sci-navic-igso-figure-eight", craft="inference")

# ================================================================ ASTRONOMY & EARTH SCIENCE (m-stmt)
S("Astronomy & Earth Science", "medium", "Consider the following statements about the heliosphere:",
  "हीलियोस्फ़ीयर के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is the vast bubble carved out in space by the solar wind, the stream of charged particles flowing from the Sun.",
   "Voyager 1 crossed its outer boundary, the heliopause, into interstellar space in 2012.",
   "It shields the solar system from part of the galactic cosmic rays coming from beyond it."],
  ["यह सौर पवन, सूर्य से बहने वाली आवेशित कणों की धारा, द्वारा अंतरिक्ष में बनाया गया विशाल बुलबुला है।",
   "वॉयजर 1 ने 2012 में इसकी बाहरी सीमा, हीलियोपॉज़, पार कर अंतरतारकीय अंतरिक्ष में प्रवेश किया।",
   "यह सौरमंडल को बाहर से आने वाली मंदाकिनीय कॉस्मिक किरणों के एक भाग से बचाता है।"],
  C3, 2,
  "All three statements are correct. The solar wind pushes outward until its pressure balances that of the thin gas between the stars; the heliopause, where the two meet, lies more than 120 times the Earth's distance from the Sun. "
  "Voyager 1 crossed it in 2012 and Voyager 2 in 2018, recording a sharp rise in galactic cosmic rays and a fall in solar particles -- direct evidence that the heliosphere screens out part of the cosmic radiation, which matters for life on Earth and for astronauts on long missions.",
  "तीनों कथन सही हैं। सौर पवन तब तक बाहर धकेलती है जब तक उसका दाब तारों के बीच की विरल गैस के दाब के बराबर न हो जाए; जहाँ दोनों मिलते हैं, वह हीलियोपॉज़ सूर्य से पृथ्वी की दूरी के 120 गुना से अधिक दूर है। "
  "वॉयजर 1 ने इसे 2012 में और वॉयजर 2 ने 2018 में पार किया, मंदाकिनीय कॉस्मिक किरणों में तेज़ वृद्धि और सौर कणों में कमी दर्ज करते हुए -- यह प्रत्यक्ष प्रमाण कि हीलियोस्फ़ीयर कॉस्मिक विकिरण के एक भाग को रोकता है, जो पृथ्वी पर जीवन और लंबे अभियानों पर अंतरिक्ष यात्रियों के लिए महत्त्वपूर्ण है।",
  "NASA (Voyager interstellar mission); NCERT Class VIII, Science (Stars and the Solar System).",
  "l3-t3-sci-heliosphere-heliopause", craft="recall")

# ================================================================ PHYSICS & EVERYDAY SCIENCE (m-stmt)
S("Physics & Everyday Science", "medium", "Consider the following statements about resonance:",
  "अनुनाद के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Resonance occurs when a periodic force acts at an object's natural frequency, building up large vibrations.",
   "Soldiers are told to break step on a bridge so that their rhythmic marching does not set it vibrating strongly.",
   "Tuning a radio to a station works by adjusting a circuit so that it resonates at that station's frequency."],
  ["अनुनाद तब होता है जब कोई आवर्ती बल किसी वस्तु की प्राकृतिक आवृत्ति पर कार्य करता है, जिससे बड़े कंपन बनते हैं।",
   "सैनिकों को पुल पर क़दम-ताल तोड़ने को कहा जाता है ताकि उनका लयबद्ध मार्च उसे ज़ोर से कंपित न करे।",
   "रेडियो को किसी स्टेशन पर मिलाना एक परिपथ को इस प्रकार समायोजित करके होता है कि वह उस स्टेशन की आवृत्ति पर अनुनादित हो।"],
  C3, 2,
  "All three statements are correct. Every structure or circuit has natural frequencies; a small push repeated at one of them adds energy each cycle, so the amplitude grows -- as with a child's swing pushed in time. "
  "A column of soldiers marching in step could drive a bridge near its natural frequency, so they break step; engineers add dampers to tall buildings and bridges for the same reason. In a radio, turning the dial changes a capacitor in an inductor-capacitor circuit so that it resonates at the wanted station's frequency and picks it out from all the others.",
  "तीनों कथन सही हैं। हर संरचना या परिपथ की प्राकृतिक आवृत्तियाँ होती हैं; उनमें से किसी पर दोहराया गया छोटा धक्का हर चक्र में ऊर्जा जोड़ता है, इसलिए आयाम बढ़ता जाता है -- जैसे समय पर धकेला गया बच्चे का झूला। "
  "क़दम मिलाकर चलती सैनिकों की टुकड़ी किसी पुल को उसकी प्राकृतिक आवृत्ति के निकट कंपित कर सकती है, इसलिए वे क़दम-ताल तोड़ते हैं; इसी कारण इंजीनियर ऊँची इमारतों और पुलों में अवमंदक लगाते हैं। रेडियो में डायल घुमाने से प्रेरक-संधारित्र परिपथ में संधारित्र बदलता है ताकि वह वांछित स्टेशन की आवृत्ति पर अनुनादित होकर उसे बाक़ी सबसे अलग चुन ले।",
  "NCERT Class XI, Physics Part II (Oscillations); NCERT Class XII, Physics Part I (Alternating Current: resonance).",
  "l3-t3-sci-resonance", craft="application")

# ================================================================ BIOLOGY, HEALTH & BIOTECHNOLOGY (m-stmt)
S("Biology, Health & Biotechnology", "medium", "Consider the following statements about tuberculosis (TB):",
  "क्षयरोग (TB) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is caused by a bacterium and spreads mainly through the air when a person with lung TB coughs.",
   "The BPaLM regimen, approved in India in 2024, treats drug-resistant TB in about six months.",
   "The BCG vaccine gives adults lifelong protection against TB of the lungs."],
  ["यह एक जीवाणु से होता है और मुख्यतः तब हवा से फैलता है जब फेफड़ों के TB वाला व्यक्ति खाँसता है।",
   "भारत में 2024 में स्वीकृत BPaLM उपचार-पद्धति दवा-प्रतिरोधी TB का लगभग छह महीनों में इलाज करती है।",
   "BCG टीका वयस्कों को फेफड़ों के TB से जीवन भर सुरक्षा देता है।"],
  C3, 1,
  "Statements 1 and 2 are correct. TB, caused by Mycobacterium tuberculosis, kills more people worldwide than any other single infectious agent, and India carries the largest share of cases. Drug-resistant TB used to need 18 months or more of toxic treatment; BPaLM -- bedaquiline, pretomanid, linezolid and moxifloxacin -- cuts this to about six months with better cure rates. "
  "Statement 3 is wrong: BCG, given at birth, protects young children well against severe forms such as TB meningitis but offers limited and variable protection against lung TB in adults, which is why new vaccines are being tested under India's TB elimination programme.",
  "कथन 1 और 2 सही हैं। माइकोबैक्टीरियम ट्यूबरकुलोसिस से होने वाला TB विश्व भर में किसी भी अन्य एकल संक्रामक कारक से अधिक लोगों की जान लेता है, और मामलों का सबसे बड़ा हिस्सा भारत में है। दवा-प्रतिरोधी TB के लिए पहले 18 महीने या अधिक का विषैला उपचार चाहिए था; BPaLM -- बेडाक्विलिन, प्रीटोमैनिड, लाइनज़ोलिड और मॉक्सीफ़्लॉक्सासिन -- इसे बेहतर उपचार दर के साथ लगभग छह महीने कर देता है। "
  "कथन 3 ग़लत है: जन्म पर दिया जाने वाला BCG छोटे बच्चों को TB मेनिनजाइटिस जैसे गंभीर रूपों से अच्छी सुरक्षा देता है पर वयस्कों में फेफड़ों के TB से सीमित और परिवर्ती सुरक्षा देता है, इसीलिए भारत के TB उन्मूलन कार्यक्रम के अंतर्गत नए टीकों का परीक्षण हो रहा है।",
  "Ministry of Health and Family Welfare (National TB Elimination Programme); World Health Organization (Global TB Report).",
  "l3-t3-sci-tuberculosis-bpalm-bcg", craft="linkage")

# ================================================================ DEFENCE, AEROSPACE & SECURITY TECHNOLOGY (m-stmt)
S("Defence, Aerospace & Security Technology", "medium", "Consider the following statements about air-independent propulsion (AIP) for submarines:",
  "पनडुब्बियों के लिए वायु-स्वतंत्र प्रणोदन (AIP) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It lets a non-nuclear submarine stay submerged much longer without surfacing or snorkelling to run its diesel engines.",
   "DRDO has developed a fuel-cell-based AIP system for India's Kalvari-class submarines.",
   "Nuclear-powered submarines also need AIP in order to stay underwater for long periods."],
  ["यह किसी ग़ैर-नाभिकीय पनडुब्बी को अपने डीज़ल इंजन चलाने के लिए सतह पर आए या स्नॉर्कल किए बिना कहीं अधिक समय तक जलमग्न रहने देता है।",
   "DRDO ने भारत की कलवरी-श्रेणी की पनडुब्बियों के लिए ईंधन-सेल आधारित AIP प्रणाली विकसित की है।",
   "नाभिकीय-शक्ति वाली पनडुब्बियों को भी लंबे समय तक पानी के नीचे रहने के लिए AIP चाहिए।"],
  C3, 1,
  "Statements 1 and 2 are correct. A conventional submarine runs on batteries underwater and must come near the surface every few days to run its diesel engines, when it is easiest to detect; AIP systems -- fuel cells, Stirling engines or closed-cycle turbines -- generate power without outside air, extending submerged endurance from days to weeks. "
  "DRDO's system uses fuel cells, with hydrogen generated on board, and is to be fitted to the Kalvari class during refits. Statement 3 is wrong: a nuclear reactor needs no air at all, so nuclear submarines can stay submerged for months, limited mainly by food and crew endurance.",
  "कथन 1 और 2 सही हैं। पारंपरिक पनडुब्बी पानी के नीचे बैटरियों से चलती है और डीज़ल इंजन चलाने के लिए हर कुछ दिनों में सतह के पास आनी चाहिए, जब उसे पकड़ना सबसे आसान होता है; AIP प्रणालियाँ -- ईंधन सेल, स्टर्लिंग इंजन या बंद-चक्र टर्बाइन -- बाहरी हवा के बिना शक्ति बनाती हैं, जिससे जलमग्न रहने की क्षमता दिनों से हफ़्तों तक बढ़ जाती है। "
  "DRDO की प्रणाली जहाज़ पर ही बनाए गए हाइड्रोजन वाले ईंधन सेलों का उपयोग करती है, और इसे मरम्मत के दौरान कलवरी श्रेणी में लगाया जाना है। कथन 3 ग़लत है: नाभिकीय रिएक्टर को हवा की बिल्कुल आवश्यकता नहीं होती, इसलिए नाभिकीय पनडुब्बियाँ महीनों जलमग्न रह सकती हैं, मुख्यतः भोजन और चालक दल की सहनशक्ति से सीमित।",
  "Defence Research and Development Organisation (Naval Materials Research Laboratory: fuel-cell AIP); Ministry of Defence.",
  "l3-t3-sci-air-independent-propulsion", craft="inference")

write("gs_l3_t3_f.sql")
