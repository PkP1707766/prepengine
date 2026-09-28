# -*- coding: utf-8 -*-
"""Level 2 · Test 10 (Environment 2: Climate Change & Pollution) -- Pollution, Waste &
Resources, 22 new bilingual rows against the live gap report: medium statement 8, easy
statement 3, hard statement 3, medium MCQ 2, easy MCQ 1, hard MCQ 1, medium Statement-I/II 1,
easy Statement-I/II 1, hard Statement-I/II/III 1, easy pairs 1. Concepts already in the bank
(control devices, AQI categories, biomagnification, BS-VI, carbon monoxide, Delhi winter smog,
overshoot day, E. coli indicator, eutrophication, e-waste rules, ground-level ozone, indoor
air, NAAQS, noise rules, PAN, pollutant-disease pairs, radioactive pollutants, SWM Rules 2026,
thermal pollution) are not repeated."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Environment & Ecology"
W = "Pollution, Waste & Resources"
MICRO12 = "NCERT Class XII, Biology -- Microbes in Human Welfare (sewage treatment)"
CHEM11 = "NCERT Class XI, Chemistry -- Environmental Chemistry"

# ---------------------------------------------------------------- medium statements (8)
S(W, "medium", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Biochemical oxygen demand (BOD) is the amount of oxygen that microorganisms need to break down the organic matter in a sample of water.",
   "A higher BOD indicates cleaner water.",
   "For the same sample, the chemical oxygen demand (COD) is usually lower than the BOD."],
  ["जैव-रासायनिक ऑक्सीजन माँग (BOD) वह ऑक्सीजन की मात्रा है जिसकी सूक्ष्मजीवों को पानी के किसी नमूने में जैविक पदार्थ तोड़ने के लिए ज़रूरत होती है।",
   "अधिक BOD स्वच्छ पानी का संकेत है।",
   "एक ही नमूने के लिए रासायनिक ऑक्सीजन माँग (COD) सामान्यतः BOD से कम होती है।"],
  C3, 0,
  "Only statement 1 is correct. BOD, usually measured over five days at 20 degrees Celsius, is a measure of how much biodegradable organic matter the water carries. COD uses a strong chemical oxidant, which oxidises nearly all organic matter -- including matter that microbes cannot break down -- so COD is normally higher than BOD -- the reverse of statement 3 -- and the ratio between them tells an engineer how biodegradable a waste is. "
  "Statement 2 is also reversed: a high BOD means a heavy load of organic pollution, such as sewage, which will use up the dissolved oxygen that fish need. The CPCB's criterion for bathing water is a BOD of 3 mg per litre or less.",
  "केवल कथन 1 सही है। सामान्यतः 20 डिग्री सेल्सियस पर पाँच दिनों में मापी जाने वाली BOD इस बात का माप है कि पानी में कितना जैव-निम्नीकरणीय (biodegradable) जैविक पदार्थ है। COD में एक प्रबल रासायनिक ऑक्सीकारक का उपयोग होता है, जो लगभग सारे जैविक पदार्थ को ऑक्सीकृत कर देता है, उस पदार्थ सहित जिसे सूक्ष्मजीव नहीं तोड़ सकते; इसलिए COD सामान्यतः BOD से अधिक होती है, जो कथन 3 का उलटा है, और दोनों का अनुपात इंजीनियर को बताता है कि कोई अपशिष्ट कितना जैव-निम्नीकरणीय है। "
  "कथन 2 भी उलटा है: अधिक BOD का अर्थ है जैविक प्रदूषण, जैसे सीवेज, का भारी बोझ, जो मछलियों के लिए ज़रूरी घुली ऑक्सीजन को खत्म कर देगा। स्नान योग्य जल के लिए CPCB का मानदंड 3 मिलीग्राम प्रति लीटर या उससे कम BOD है।",
  f"{MICRO12}; Central Pollution Control Board -- primary water quality criteria for bathing water.",
  "env-bod-cod")

S(W, "medium", "Consider the following statements about the rules on plastic waste in India:",
  "भारत में प्लास्टिक अपशिष्ट से संबंधित नियमों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Identified single-use plastic items have been banned since 1 July 2022.",
   "Plastic carry bags thinner than 120 microns have been banned since 31 December 2022.",
   "Producers, importers and brand owners must meet Extended Producer Responsibility obligations for plastic packaging.",
   "The ban on single-use plastic also covers PET bottles used for drinking water."],
  ["चिह्नित एकल-उपयोग प्लास्टिक (single-use plastic) वस्तुओं पर 1 जुलाई 2022 से प्रतिबंध है।",
   "120 माइक्रोन से पतली प्लास्टिक कैरी बैग पर 31 दिसंबर 2022 से प्रतिबंध है।",
   "उत्पादकों, आयातकों और ब्रांड मालिकों को प्लास्टिक पैकेजिंग के लिए विस्तारित उत्पादक उत्तरदायित्व (EPR) के दायित्व पूरे करने होते हैं।",
   "एकल-उपयोग प्लास्टिक पर प्रतिबंध पीने के पानी की PET बोतलों पर भी लागू है।"],
  C4, 2,
  "Statements 1, 2 and 3 are correct. The Plastic Waste Management (Amendment) Rules, 2021 banned the manufacture, sale and use of a list of low-utility, high-litter items -- plastic-stick earbuds, cutlery, straws, stirrers, thin wrapping film for sweet boxes, and the like -- from 1 July 2022, and raised the minimum thickness of carry bags to 75 microns and then to 120 microns from 31 December 2022. The EPR guidelines of 2022 make producers, importers and brand owners collect and recycle set shares of the plastic packaging they put on the market. "
  "Statement 4 is wrong: PET bottles are not on the banned list; they are packaging covered by EPR, with targets for collection, recycling and the use of recycled content.",
  "कथन 1, 2 और 3 सही हैं। प्लास्टिक अपशिष्ट प्रबंधन (संशोधन) नियम, 2021 ने कम उपयोगिता और अधिक कूड़ा फैलाने वाली वस्तुओं की एक सूची, जैसे प्लास्टिक डंडी वाले ईयरबड, कटलरी, स्ट्रॉ, स्टिरर, मिठाई के डिब्बों पर लपेटी जाने वाली पतली फ़िल्म आदि, के निर्माण, बिक्री और उपयोग पर 1 जुलाई 2022 से रोक लगाई, और कैरी बैग की न्यूनतम मोटाई पहले 75 माइक्रोन और फिर 31 दिसंबर 2022 से 120 माइक्रोन कर दी। 2022 के EPR दिशानिर्देश उत्पादकों, आयातकों और ब्रांड मालिकों को बाज़ार में उतारी गई प्लास्टिक पैकेजिंग के निर्धारित हिस्से को एकत्र करने और पुनर्चक्रित करने के लिए बाध्य करते हैं। "
  "कथन 4 गलत है: PET बोतलें प्रतिबंधित सूची में नहीं हैं; वे EPR के तहत आने वाली पैकेजिंग हैं, जिनके लिए संग्रह, पुनर्चक्रण और पुनर्चक्रित सामग्री के उपयोग के लक्ष्य हैं।",
  "Ministry of Environment, Forest and Climate Change -- Plastic Waste Management (Amendment) Rules, 2021 and Guidelines on Extended Producer Responsibility for Plastic Packaging (2022).",
  "env-plastic-waste-rules")

S(W, "medium", "Consider the following statements about groundwater contamination in India:",
  "भारत में भूजल संदूषण के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Arsenic contamination of groundwater affects parts of the Ganga-Brahmaputra plains, including West Bengal and Bihar.",
   "Excess fluoride in drinking water causes dental and skeletal fluorosis.",
   "Uranium above the safe limit has been reported in groundwater in parts of Punjab."],
  ["भूजल का आर्सेनिक संदूषण गंगा-ब्रह्मपुत्र मैदानों के कुछ भागों, जिनमें पश्चिम बंगाल और बिहार शामिल हैं, को प्रभावित करता है।",
   "पीने के पानी में अधिक फ़्लोराइड से दाँतों और हड्डियों का फ़्लोरोसिस होता है।",
   "पंजाब के कुछ भागों के भूजल में सुरक्षित सीमा से अधिक यूरेनियम पाया गया है।"],
  C3, 2,
  "All three statements are correct. Arsenic in the young alluvial aquifers of the Ganga-Brahmaputra plains is natural in origin, released from sediments into groundwater, and long-term drinking causes skin lesions and cancers. Fluoride above 1.5 mg per litre causes mottled teeth and, over years, crippling bone deformities; it is widespread in Rajasthan, Telangana, Andhra Pradesh, Gujarat and other States with hard-rock aquifers. "
  "The Central Ground Water Board's groundwater quality reports have found uranium above the 30 micrograms per litre limit in many wells, notably in Punjab and Haryana. All three are 'geogenic' contaminants, made worse by heavy pumping -- the problem is not only sewage and industry.",
  "तीनों कथन सही हैं। गंगा-ब्रह्मपुत्र मैदानों के नए जलोढ़ जलभृतों में आर्सेनिक प्राकृतिक मूल का है, जो तलछट से भूजल में घुलता है, और लंबे समय तक पीने से त्वचा पर घाव और कैंसर होते हैं। 1.5 मिलीग्राम प्रति लीटर से अधिक फ़्लोराइड से दाँतों पर धब्बे और वर्षों में हड्डियों की अपंग करने वाली विकृतियाँ होती हैं; यह राजस्थान, तेलंगाना, आंध्र प्रदेश, गुजरात और कठोर चट्टानी जलभृतों वाले दूसरे राज्यों में व्यापक है। "
  "केंद्रीय भूजल बोर्ड की भूजल गुणवत्ता रिपोर्टों में कई कुओं में 30 माइक्रोग्राम प्रति लीटर की सीमा से अधिक यूरेनियम मिला है, विशेषकर पंजाब और हरियाणा में। तीनों 'भूजनित' (geogenic) संदूषक हैं, जिन्हें अत्यधिक दोहन और बढ़ा देता है; समस्या केवल सीवेज और उद्योग की नहीं है।",
  "Central Ground Water Board -- Annual Groundwater Quality Report; Bureau of Indian Standards, IS 10500:2012 (drinking water specification).",
  "env-groundwater-geogenic-contaminants")

S(W, "medium", "Consider the following statements about microplastics:",
  "माइक्रोप्लास्टिक के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["They are generally defined as plastic particles smaller than 5 millimetres.",
   "Microbeads added to cosmetics and toothpastes are an example of primary microplastics.",
   "Microplastics have been detected in human blood."],
  ["इन्हें सामान्यतः 5 मिलीमीटर से छोटे प्लास्टिक कणों के रूप में परिभाषित किया जाता है।",
   "सौंदर्य-प्रसाधनों और टूथपेस्ट में मिलाए जाने वाले माइक्रोबीड प्राथमिक माइक्रोप्लास्टिक का उदाहरण हैं।",
   "मानव रक्त में माइक्रोप्लास्टिक पाए गए हैं।"],
  C3, 2,
  "All three statements are correct. Primary microplastics are made small on purpose (microbeads, pellets used as raw material); secondary microplastics come from the breakdown of larger items -- bottles, bags, fishing nets -- and from synthetic textiles shedding fibres in the wash and tyres wearing on roads, which together are the largest sources. "
  "A 2022 study found plastic particles in the blood of most of the healthy volunteers tested, and they have since been reported in placenta and other tissues; their long-term health effects are still being studied. The Bureau of Indian Standards has classed plastic microbeads as unsafe for use in rinse-off cosmetics.",
  "तीनों कथन सही हैं। प्राथमिक माइक्रोप्लास्टिक जान-बूझकर छोटे बनाए जाते हैं (माइक्रोबीड, कच्चे माल के रूप में उपयोग होने वाले दाने); द्वितीयक माइक्रोप्लास्टिक बोतलों, थैलियों, मछली पकड़ने के जालों जैसी बड़ी वस्तुओं के टूटने से, और धुलाई में रेशे छोड़ते कृत्रिम वस्त्रों तथा सड़कों पर घिसते टायरों से आते हैं, जो मिलकर सबसे बड़े स्रोत हैं। "
  "2022 के एक अध्ययन में जाँचे गए अधिकांश स्वस्थ स्वयंसेवकों के रक्त में प्लास्टिक कण मिले, और तब से ये अपरा (placenta) और दूसरे ऊतकों में भी पाए गए हैं; इनके दीर्घकालिक स्वास्थ्य-प्रभावों पर अभी अध्ययन जारी है। भारतीय मानक ब्यूरो ने धोकर हटाए जाने वाले सौंदर्य-प्रसाधनों में प्लास्टिक माइक्रोबीड को असुरक्षित श्रेणी में रखा है।",
  "UNEP -- microplastics; H.A. Leslie et al., Environment International 163 (2022); Bureau of Indian Standards -- microbeads in cosmetic products (IS 4707, Part 2).",
  "env-microplastics")

S(W, "medium", "Consider the following statements about fly ash:",
  "फ़्लाई ऐश के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is produced mainly by coal-based thermal power plants.",
   "It is listed as a hazardous waste under India's hazardous waste rules.",
   "It consists mainly of unburnt organic carbon."],
  ["यह मुख्य रूप से कोयला-आधारित तापीय विद्युत संयंत्रों से बनती है।",
   "यह भारत के खतरनाक अपशिष्ट नियमों के तहत एक खतरनाक अपशिष्ट के रूप में सूचीबद्ध है।",
   "यह मुख्य रूप से बिना जले जैविक कार्बन से बनी होती है।"],
  C3, 0,
  "Only statement 1 is correct: Indian coal has a high ash content, and power plants generate well over 200 million tonnes of fly ash a year, which is dumped in ash ponds unless it is used. "
  "Statement 2 is wrong: fly ash is not listed as hazardous waste; its disposal and use are governed by a separate fly ash utilisation notification, which since 2021 requires power plants to achieve full utilisation within set cycles, with penalties on the unused ash. "
  "Statement 3 is wrong: fly ash consists mainly of silica, alumina and oxides of iron and calcium, which is why it can replace part of the cement in concrete and is used to make bricks and to build roads and embankments.",
  "केवल कथन 1 सही है: भारतीय कोयले में राख की मात्रा अधिक होती है, और बिजली संयंत्र हर वर्ष 20 करोड़ टन से कहीं अधिक फ़्लाई ऐश बनाते हैं, जिसका उपयोग न हो तो वह राख-तालाबों में डाल दी जाती है। "
  "कथन 2 गलत है: फ़्लाई ऐश खतरनाक अपशिष्ट के रूप में सूचीबद्ध नहीं है; इसका निपटान और उपयोग एक अलग फ़्लाई ऐश उपयोग अधिसूचना से नियंत्रित होता है, जो 2021 से बिजली संयंत्रों से निर्धारित चक्रों में पूरे उपयोग की अपेक्षा करती है और बची राख पर दंड लगाती है। "
  "कथन 3 गलत है: फ़्लाई ऐश मुख्य रूप से सिलिका, एल्युमिना और लोहे तथा कैल्शियम के ऑक्साइडों से बनी होती है; इसीलिए यह कंक्रीट में सीमेंट के एक हिस्से की जगह ले सकती है और ईंटें बनाने तथा सड़कें और तटबंध बनाने में उपयोग होती है।",
  "Ministry of Environment, Forest and Climate Change -- Fly Ash Utilisation Notification (31 December 2021); Central Electricity Authority -- report on fly ash generation and utilisation.",
  "env-fly-ash")

S(W, "medium", "Consider the following statements about acid rain:",
  "अम्लीय वर्षा के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Any rain with a pH below 7 is classified as acid rain.",
   "Acid rain is caused mainly by oxides of sulphur and nitrogen.",
   "The marble of the Taj Mahal is vulnerable to damage by acid rain."],
  ["pH 7 से कम वाली कोई भी वर्षा अम्लीय वर्षा मानी जाती है।",
   "अम्लीय वर्षा मुख्य रूप से सल्फ़र और नाइट्रोजन के ऑक्साइडों के कारण होती है।",
   "ताजमहल का संगमरमर अम्लीय वर्षा से होने वाली क्षति के प्रति संवेदनशील है।"],
  C3, 1,
  "Statements 2 and 3 are correct. Sulphur dioxide from burning coal and oil, and nitrogen oxides from vehicles and power plants, form sulphuric and nitric acids in the atmosphere. These react with the calcium carbonate of marble -- the 'marble cancer' feared for the Taj Mahal from the Mathura refinery and Agra's industries, which led to the Taj Trapezium Zone. "
  "Statement 1 is the trap: even unpolluted rain is slightly acidic, with a pH of about 5.6, because carbon dioxide dissolves in it to form weak carbonic acid. Only rain with a pH below about 5.6 is called acid rain.",
  "कथन 2 और 3 सही हैं। कोयला और तेल जलाने से निकलने वाली सल्फ़र डाइऑक्साइड, और वाहनों तथा बिजली संयंत्रों से निकलने वाले नाइट्रोजन ऑक्साइड वायुमंडल में सल्फ़्यूरिक और नाइट्रिक अम्ल बनाते हैं। ये संगमरमर के कैल्शियम कार्बोनेट से प्रतिक्रिया करते हैं; मथुरा रिफ़ाइनरी और आगरा के उद्योगों से ताजमहल के लिए इसी 'संगमरमर कैंसर' का डर था, जिससे ताज ट्रेपेज़ियम ज़ोन बना। "
  "कथन 1 जाल है: प्रदूषण-रहित वर्षा भी थोड़ी अम्लीय होती है, जिसका pH लगभग 5.6 होता है, क्योंकि कार्बन डाइऑक्साइड उसमें घुलकर दुर्बल कार्बोनिक अम्ल बनाती है। केवल लगभग 5.6 से कम pH वाली वर्षा को अम्लीय वर्षा कहा जाता है।",
  f"{CHEM11} (acid rain); Supreme Court, M.C. Mehta v. Union of India (Taj Trapezium case, 1996).",
  "env-acid-rain")

S(W, "medium", "Consider the following statements about light pollution:",
  "प्रकाश प्रदूषण के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Hanle in Ladakh was declared India's first Dark Sky Reserve in 2022.",
   "Artificial lights near beaches can lead sea turtle hatchlings away from the sea.",
   "Blue-rich white LED street lighting causes less skyglow than older sodium lamps of the same brightness."],
  ["लद्दाख के हानले को 2022 में भारत का पहला डार्क स्काई रिज़र्व घोषित किया गया।",
   "समुद्र तटों के पास की कृत्रिम रोशनी समुद्री कछुओं के बच्चों को समुद्र से दूर भटका सकती है।",
   "नीले प्रकाश से भरपूर सफ़ेद LED सड़क-प्रकाश उतनी ही चमक वाले पुराने सोडियम लैंपों की तुलना में कम आकाश-दीप्ति (skyglow) पैदा करता है।"],
  C3, 1,
  "Statements 1 and 2 are correct. The Hanle Dark Sky Reserve, around the Indian Astronomical Observatory in the Changthang, was set up in 2022 to keep the night sky dark through lighting controls and astro-tourism. Turtle hatchlings find the sea by moving towards the brighter horizon over the water, so lights on the shore draw them inland, where they die -- one reason for lighting rules near nesting beaches. "
  "Statement 3 is reversed: blue light is scattered much more strongly by the atmosphere, so blue-rich white LEDs brighten the sky more than the orange sodium lamps they replaced, unless they are warm-toned, shielded and dimmed.",
  "कथन 1 और 2 सही हैं। चांगथांग में भारतीय खगोलीय वेधशाला के आसपास हानले डार्क स्काई रिज़र्व 2022 में बनाया गया, ताकि प्रकाश-नियंत्रण और खगोल-पर्यटन के ज़रिए रात का आकाश अँधेरा बना रहे। कछुओं के बच्चे पानी के ऊपर के अधिक चमकीले क्षितिज की ओर बढ़कर समुद्र ढूँढ़ते हैं, इसलिए तट की रोशनियाँ उन्हें ज़मीन की ओर खींच लेती हैं, जहाँ वे मर जाते हैं; घोंसलों वाले तटों के पास प्रकाश-नियमों का यह एक कारण है। "
  "कथन 3 उलटा है: वायुमंडल नीले प्रकाश को कहीं अधिक प्रकीर्णित करता है, इसलिए नीले से भरपूर सफ़ेद LED उन नारंगी सोडियम लैंपों से अधिक आकाश को चमकाते हैं जिनकी जगह उन्होंने ली, जब तक कि वे गर्म रंगत वाले, ढके हुए और मंद न हों।",
  "Department of Science and Technology / Indian Institute of Astrophysics -- Hanle Dark Sky Reserve (2022); International Dark-Sky Association -- lighting and wildlife.",
  "env-light-pollution")

S(W, "medium", "Consider the following statements about the treatment of sewage:",
  "सीवेज के उपचार के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Primary treatment of sewage is a biological process that relies on microbes.",
   "Secondary treatment raises the BOD of the effluent.",
   "The biogas produced in anaerobic sludge digesters is mainly hydrogen."],
  ["सीवेज का प्राथमिक उपचार सूक्ष्मजीवों पर आधारित एक जैविक प्रक्रिया है।",
   "द्वितीयक उपचार बहिःस्राव (effluent) की BOD बढ़ा देता है।",
   "अवायवीय आपंक पाचकों (anaerobic sludge digesters) में बनने वाली बायोगैस मुख्य रूप से हाइड्रोजन होती है।"],
  C3, 3,
  "None of the statements is correct. Primary treatment is physical: screening, filtration and settling remove floating debris, grit and settleable solids. "
  "Secondary treatment is the biological step: in aeration tanks, aerobic microbes form flocs that consume the organic matter, which greatly reduces the BOD of the effluent; part of the settled 'activated sludge' is returned to the tanks as inoculum. "
  "The rest of the sludge goes to anaerobic digesters, where other bacteria break it down and produce biogas made mostly of methane, with hydrogen sulphide and carbon dioxide.",
  "कोई भी कथन सही नहीं है। प्राथमिक उपचार भौतिक है: छनाई, निस्यंदन और तलछटीकरण से तैरता कचरा, रेत-कंकड़ और बैठने योग्य ठोस हटाए जाते हैं। "
  "द्वितीयक उपचार जैविक चरण है: वातन टैंकों में वायवीय सूक्ष्मजीव फ़्लॉक बनाते हैं, जो जैविक पदार्थ को खा जाते हैं, जिससे बहिःस्राव की BOD बहुत घट जाती है; नीचे बैठे 'सक्रियित आपंक' (activated sludge) का एक भाग संवर्धक के रूप में टैंकों में लौटा दिया जाता है। "
  "बाकी आपंक अवायवीय पाचकों में जाता है, जहाँ दूसरे जीवाणु उसे तोड़कर बायोगैस बनाते हैं, जो मुख्यतः मीथेन होती है, साथ में हाइड्रोजन सल्फ़ाइड और कार्बन डाइऑक्साइड।",
  f"{MICRO12}.",
  "env-sewage-treatment-stages")

# ---------------------------------------------------------------- easy statements (3)
S(W, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The loudness of sound is measured in decibels (dB).",
   "The decibel scale is linear, so a sound of 80 dB is twice as intense as one of 40 dB."],
  ["ध्वनि की प्रबलता डेसिबल (dB) में मापी जाती है।",
   "डेसिबल पैमाना रैखिक है, इसलिए 80 dB की ध्वनि 40 dB की ध्वनि से दोगुनी तीव्र होती है।"],
  T2, 0,
  "Only statement 1 is correct. The decibel scale is logarithmic: every rise of 10 dB means ten times the sound intensity, so 80 dB is 10,000 times as intense as 40 dB, not twice. That is why the gap between a residential night-time limit (45 dB(A)) and busy traffic (around 80 to 90 dB) is so large in terms of energy, and why prolonged exposure above about 85 dB can damage hearing.",
  "केवल कथन 1 सही है। डेसिबल पैमाना लघुगणकीय (logarithmic) है: हर 10 dB की वृद्धि का अर्थ है ध्वनि की तीव्रता का दस गुना होना, इसलिए 80 dB, 40 dB से दोगुना नहीं, 10,000 गुना तीव्र है। इसीलिए आवासीय क्षेत्र की रात की सीमा (45 dB(A)) और भारी यातायात (लगभग 80 से 90 dB) का अंतर ऊर्जा के हिसाब से इतना बड़ा है, और लगभग 85 dB से ऊपर लंबे समय तक रहने से सुनने की क्षमता को नुकसान हो सकता है।",
  "NCERT Class IX, Science -- Sound; Noise Pollution (Regulation and Control) Rules, 2000, Schedule.",
  "env-decibel-scale")

S(W, "easy", "Consider the following statements about managing waste:",
  "अपशिष्ट प्रबंधन के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["In the waste hierarchy, reducing and reusing waste rank above recycling.",
   "Recovering energy from waste ranks above disposal in a landfill.",
   "Composting wet waste reduces the amount of waste sent to landfills."],
  ["अपशिष्ट पदानुक्रम (waste hierarchy) में अपशिष्ट घटाना और पुनः उपयोग करना पुनर्चक्रण से ऊपर आते हैं।",
   "अपशिष्ट से ऊर्जा प्राप्त करना भराव-क्षेत्र (landfill) में निपटान से ऊपर आता है।",
   "गीले कचरे की खाद बनाने से भराव-क्षेत्रों में भेजे जाने वाले कचरे की मात्रा घटती है।"],
  C3, 2,
  "All three statements are correct. The waste hierarchy runs from the most to the least preferred: prevent or reduce, reuse, recycle (including composting), recover energy, and only last dispose of in a landfill. "
  "Landfilling is the last resort, because landfills take up land, leak leachate into groundwater and give off methane from rotting organic waste -- which is also why composting the wet half of Indian household waste matters so much.",
  "तीनों कथन सही हैं। अपशिष्ट पदानुक्रम सबसे अधिक से सबसे कम पसंदीदा तक चलता है: रोकना या घटाना, पुनः उपयोग, पुनर्चक्रण (खाद बनाने सहित), ऊर्जा की प्राप्ति, और सबसे अंत में भराव-क्षेत्र में निपटान। "
  "भराव-क्षेत्र अंतिम उपाय है, क्योंकि वह भूमि घेरता है, भूजल में निक्षालित द्रव (leachate) रिसाता है और सड़ते जैविक कचरे से मीथेन छोड़ता है; इसीलिए भारतीय घरेलू कचरे के गीले आधे भाग की खाद बनाना इतना महत्त्वपूर्ण है।",
  "UNEP -- Global Waste Management Outlook; Ministry of Housing and Urban Affairs -- Swachh Bharat Mission (Urban) 2.0 (garbage-free cities).",
  "env-waste-hierarchy")

S(W, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["India phased out leaded petrol nationwide in 2000.",
   "Lead mainly damages the nervous system, and children are especially vulnerable to it."],
  ["भारत ने 2000 में पूरे देश में सीसायुक्त (leaded) पेट्रोल को समाप्त कर दिया।",
   "सीसा मुख्य रूप से तंत्रिका तंत्र को नुकसान पहुँचाता है, और बच्चे इसके प्रति विशेष रूप से संवेदनशील होते हैं।"],
  T2, 2,
  "Both statements are correct. India moved to unleaded petrol in stages from the metros in the mid-1990s and completed the switch nationwide in 2000; worldwide, the last leaded petrol was sold in 2021. "
  "Lead has no safe level in the body; in children even low exposure lowers IQ and affects behaviour, and it also raises blood pressure in adults. With petrol gone, the main sources today are lead-acid battery recycling, some paints, spices and cookware.",
  "दोनों कथन सही हैं। भारत 1990 के दशक के मध्य में महानगरों से शुरू करके चरणों में सीसा-रहित पेट्रोल की ओर बढ़ा और 2000 में पूरे देश में यह बदलाव पूरा किया; विश्व में अंतिम सीसायुक्त पेट्रोल 2021 में बिका। "
  "शरीर में सीसे का कोई सुरक्षित स्तर नहीं है; बच्चों में कम संपर्क भी IQ घटाता है और व्यवहार को प्रभावित करता है, और वयस्कों में यह रक्तचाप बढ़ाता है। पेट्रोल से हटने के बाद आज इसके मुख्य स्रोत लेड-एसिड बैटरी का पुनर्चक्रण, कुछ पेंट, मसाले और बर्तन हैं।",
  "UNEP -- Partnership for Clean Fuels and Vehicles (end of leaded petrol, 2021); WHO -- lead poisoning fact sheet.",
  "env-leaded-petrol-lead")

# ---------------------------------------------------------------- hard statements (3)
S(W, "hard", "Consider the following statements about rare earth elements:",
  "दुर्लभ मृदा तत्वों (rare earth elements) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["They are not actually rare in the Earth's crust; what is rare is finding them in concentrated deposits that are economical to mine.",
   "India has the world's largest reserves of rare earth elements.",
   "In India, rare earths are obtained mainly from monazite in the Deccan basalts."],
  ["ये पृथ्वी की पर्पटी में वास्तव में दुर्लभ नहीं हैं; दुर्लभ है इन्हें ऐसे सांद्र निक्षेपों में पाना जिनका खनन किफ़ायती हो।",
   "भारत के पास दुर्लभ मृदा तत्वों का विश्व का सबसे बड़ा भंडार है।",
   "भारत में दुर्लभ मृदा मुख्य रूप से दक्कन के बेसाल्ट में मिलने वाले मोनाज़ाइट से प्राप्त होते हैं।"],
  C3, 0,
  "Only statement 1 is correct: cerium, for instance, is about as common in the crust as copper, but rare earths are dispersed and chemically alike, so separating them is difficult and polluting -- which is why China, which built that processing capacity, dominates supply. "
  "Statement 2 is wrong: China has by far the largest reserves; India's are among the larger ones but well behind. "
  "Statement 3 is wrong: India's rare earths come from monazite in the beach and coastal placer sands of Kerala, Tamil Nadu, Odisha and Andhra Pradesh; monazite also contains thorium, so it is handled by the Department of Atomic Energy through IREL (India) Limited. These elements are vital for the permanent magnets of electric motors and wind turbines.",
  "केवल कथन 1 सही है: उदाहरण के लिए, सीरियम पर्पटी में लगभग ताँबे जितना आम है, पर दुर्लभ मृदा तत्व बिखरे हुए और रासायनिक रूप से एक-जैसे होते हैं, इसलिए इन्हें अलग करना कठिन और प्रदूषणकारी है; इसीलिए यह प्रसंस्करण क्षमता बनाने वाला चीन आपूर्ति पर हावी है। "
  "कथन 2 गलत है: सबसे बड़ा भंडार कहीं आगे चीन के पास है; भारत का भंडार बड़े भंडारों में है, पर काफ़ी पीछे। "
  "कथन 3 गलत है: भारत के दुर्लभ मृदा तत्व केरल, तमिलनाडु, ओडिशा और आंध्र प्रदेश की समुद्र-तट और तटीय प्लेसर रेत के मोनाज़ाइट से आते हैं; मोनाज़ाइट में थोरियम भी होता है, इसलिए इसे परमाणु ऊर्जा विभाग IREL (इंडिया) लिमिटेड के ज़रिए संभालता है। ये तत्व विद्युत मोटरों और पवन टर्बाइनों के स्थायी चुंबकों के लिए बहुत ज़रूरी हैं।",
  "US Geological Survey -- Mineral Commodity Summaries (rare earths); Department of Atomic Energy -- IREL (India) Limited; Ministry of Mines -- National Critical Mineral Mission (2025).",
  "env-rare-earth-elements")

S(W, "hard", "Consider the following statements about air quality standards and targets:",
  "वायु गुणवत्ता के मानकों और लक्ष्यों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The WHO Air Quality Guidelines of 2021 set the annual guideline value for PM2.5 at 5 micrograms per cubic metre.",
   "The WHO guidelines also set interim targets for countries whose pollution is far above the guideline values.",
   "The annual PM2.5 guideline of 2021 is stricter than the one WHO set in 2005.",
   "Under the National Clean Air Programme, the target is a reduction of up to 40 per cent in PM10 levels by 2025-26 over 2017-18, or meeting the national standard."],
  ["WHO के 2021 के वायु गुणवत्ता दिशानिर्देशों ने PM2.5 के लिए वार्षिक दिशानिर्देश मान 5 माइक्रोग्राम प्रति घन मीटर तय किया।",
   "WHO दिशानिर्देश उन देशों के लिए अंतरिम लक्ष्य भी तय करते हैं जिनका प्रदूषण दिशानिर्देश मानों से बहुत ऊपर है।",
   "2021 का वार्षिक PM2.5 दिशानिर्देश WHO द्वारा 2005 में तय किए गए दिशानिर्देश से अधिक कठोर है।",
   "राष्ट्रीय स्वच्छ वायु कार्यक्रम (NCAP) के तहत लक्ष्य 2017-18 की तुलना में 2025-26 तक PM10 के स्तर में 40 प्रतिशत तक की कमी, या राष्ट्रीय मानक प्राप्त करना है।"],
  C4, 3,
  "All four statements are correct. The 2021 update halved the annual PM2.5 guideline from 10 to 5 micrograms per cubic metre, because new evidence showed harm at levels once thought safe; India's national standard is 40. NCAP, launched in 2019 for about 130 non-attainment and million-plus cities, began with a 20 to 30 per cent goal and was revised to up to 40 per cent reduction in PM10, or reaching the national standard of 60, by 2025-26, with funds tied to each city's performance. "
  "The guidelines are recommendations, not law: for PM2.5 they give four interim targets (35, 25, 15 and 10) as steps for countries far above 5, while binding limits are set by each country, as India does through its National Ambient Air Quality Standards. A student expecting one statement to be false will pick 'Only three'.",
  "चारों कथन सही हैं। 2021 के अद्यतन ने वार्षिक PM2.5 दिशानिर्देश को 10 से आधा करके 5 माइक्रोग्राम प्रति घन मीटर कर दिया, क्योंकि नए साक्ष्यों ने उन स्तरों पर भी हानि दिखाई जिन्हें कभी सुरक्षित माना जाता था; भारत का राष्ट्रीय मानक 40 है। लगभग 130 गैर-प्राप्ति (non-attainment) और दस लाख से अधिक आबादी वाले शहरों के लिए 2019 में शुरू हुआ NCAP 20 से 30 प्रतिशत के लक्ष्य से शुरू हुआ और फिर 2025-26 तक PM10 में 40 प्रतिशत तक की कमी, या 60 के राष्ट्रीय मानक तक पहुँचने, के लक्ष्य में बदला गया, और धन हर शहर के प्रदर्शन से जोड़ा गया। "
  "दिशानिर्देश सिफ़ारिशें हैं, कानून नहीं: PM2.5 के लिए ये 5 से बहुत ऊपर वाले देशों के लिए चरणों के रूप में चार अंतरिम लक्ष्य (35, 25, 15 और 10) देते हैं, जबकि बाध्यकारी सीमाएँ हर देश स्वयं तय करता है, जैसे भारत अपने राष्ट्रीय परिवेशी वायु गुणवत्ता मानकों (NAAQS) से करता है। जो विद्यार्थी मानता है कि एक कथन गलत होगा ही, वह 'केवल तीन' चुन लेगा।",
  "WHO Global Air Quality Guidelines (2021); Ministry of Environment, Forest and Climate Change -- National Clean Air Programme (2019) and revised targets (PIB, 2024).",
  "env-who-aqg-ncap")

S(W, "hard", "Consider the following statements about 'virtual water':",
  "'आभासी जल' (virtual water) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Virtual water is the water used to produce a good or a crop.",
   "When India exports rice, it is in effect exporting large amounts of water.",
   "Producing a kilogram of rice generally takes less water than producing a kilogram of wheat."],
  ["आभासी जल किसी वस्तु या फ़सल के उत्पादन में उपयोग हुआ जल है।",
   "जब भारत चावल निर्यात करता है, तो वह वास्तव में बड़ी मात्रा में पानी निर्यात कर रहा होता है।",
   "एक किलोग्राम चावल के उत्पादन में सामान्यतः एक किलोग्राम गेहूँ से कम पानी लगता है।"],
  C3, 1,
  "Statements 1 and 2 are correct. The idea, developed by J.A. Allan, counts the water 'embedded' in traded goods. As the world's largest rice exporter, India ships out a great deal of virtual water, much of it pumped from the falling aquifers of Punjab and Haryana -- which is why the concept appears in debates on crop diversification. "
  "Statement 3 is reversed: rice, grown in standing water, generally needs more water per kilogram than wheat -- global average water footprints are roughly 2,500 litres per kilogram for rice against about 1,800 for wheat, and much more for irrigated rice in dry regions.",
  "कथन 1 और 2 सही हैं। जे.ए. एलन द्वारा विकसित यह विचार व्यापार की जाने वाली वस्तुओं में 'समाए' पानी को गिनता है। विश्व के सबसे बड़े चावल निर्यातक के रूप में भारत बहुत-सा आभासी जल बाहर भेजता है, जिसका अधिकांश भाग पंजाब और हरियाणा के गिरते जलभृतों से पंप किया जाता है; इसीलिए यह अवधारणा फ़सल-विविधीकरण की बहसों में आती है। "
  "कथन 3 उलटा है: खड़े पानी में उगाए जाने वाले चावल को सामान्यतः प्रति किलोग्राम गेहूँ से अधिक पानी चाहिए; वैश्विक औसत जल-पदचिह्न चावल के लिए लगभग 2,500 लीटर प्रति किलोग्राम और गेहूँ के लिए लगभग 1,800 लीटर है, और शुष्क क्षेत्रों में सिंचित चावल के लिए कहीं अधिक।",
  "Water Footprint Network -- M.M. Mekonnen and A.Y. Hoekstra, The green, blue and grey water footprint of crops (2011); J.A. Allan, Virtual Water (2011).",
  "env-virtual-water")

# ---------------------------------------------------------------- MCQs (4)
M(W, "medium", "Which one of the following is an example of phytoremediation?",
  "निम्नलिखित में से कौन-सा पादप-उपचार (phytoremediation) का एक उदाहरण है?",
  ["Growing Indian mustard to take up heavy metals from soil", "Spraying oil-eating bacteria over an oil spill in the open sea",
   "Adding lime to neutralise the acidity of a lake", "Burning municipal waste to generate electricity"],
  ["मिट्टी से भारी धातुएँ सोखने के लिए भारतीय सरसों उगाना", "खुले समुद्र में तेल-रिसाव पर तेल खाने वाले जीवाणुओं का छिड़काव",
   "किसी झील की अम्लता को उदासीन करने के लिए उसमें चूना डालना", "बिजली बनाने के लिए नगरपालिका कचरे को जलाना"],
  0,
  "Phytoremediation uses plants to remove, break down or lock up pollutants. Indian mustard (Brassica juncea) takes up lead, cadmium and other metals into its shoots, which can then be harvested; wetland plants in constructed wetlands clean sewage in a similar way. "
  "Spraying microbes on an oil spill is bioremediation, but with microbes, not plants -- the closest distractor. Liming is chemical treatment, and burning waste is energy recovery.",
  "पादप-उपचार प्रदूषकों को हटाने, तोड़ने या बाँधकर रखने के लिए पौधों का उपयोग करता है। भारतीय सरसों (Brassica juncea) सीसा, कैडमियम और दूसरी धातुओं को अपने तनों-पत्तियों में सोख लेती है, जिन्हें फिर काटकर हटाया जा सकता है; निर्मित आर्द्रभूमियों में जलीय पौधे इसी तरह सीवेज को साफ़ करते हैं। "
  "तेल-रिसाव पर सूक्ष्मजीवों का छिड़काव जैव-उपचार (bioremediation) है, पर पौधों से नहीं, सूक्ष्मजीवों से; यही सबसे निकट का गलत विकल्प है। चूना डालना रासायनिक उपचार है, और कचरा जलाना ऊर्जा की प्राप्ति है।",
  "UNEP -- Phytoremediation: an environmentally sound technology for pollution prevention, control and remediation; NCERT Class XII, Biology -- Microbes in Human Welfare.",
  "env-phytoremediation")

M(W, "medium", "In India, the largest source of sulphur dioxide emissions is:",
  "भारत में सल्फ़र डाइऑक्साइड उत्सर्जन का सबसे बड़ा स्रोत है:",
  ["Coal-based power plants", "Petrol-driven passenger cars", "Burning of paddy stubble", "Brick kilns of the Indo-Gangetic plain"],
  ["कोयला-आधारित बिजली संयंत्र", "पेट्रोल से चलने वाली यात्री कारें", "धान की पराली जलाना", "सिंधु-गंगा मैदान के ईंट-भट्ठे"],
  0,
  "Indian coal contains sulphur, and burning it in thermal power plants produces most of the country's sulphur dioxide, which has made India the world's largest emitter of the gas in recent years. The fix is flue-gas desulphurisation (FGD), which the 2015 emission norms required; the deadlines were extended several times, and in 2025 the requirement was narrowed mainly to plants near large cities and polluted areas. "
  "Petrol has very little sulphur since BS-VI fuel; stubble burning is a major source of particulate matter, carbon monoxide and other gases, but not of much sulphur dioxide; brick kilns contribute, but far less than power plants.",
  "भारतीय कोयले में सल्फ़र होता है, और तापीय बिजली संयंत्रों में इसे जलाने से देश की अधिकांश सल्फ़र डाइऑक्साइड बनती है, जिसने हाल के वर्षों में भारत को इस गैस का विश्व का सबसे बड़ा उत्सर्जक बना दिया है। इसका उपाय फ़्लू-गैस डीसल्फ़्यूराइज़ेशन (FGD) है, जिसे 2015 के उत्सर्जन मानकों ने अनिवार्य किया था; समय-सीमाएँ कई बार बढ़ाई गईं, और 2025 में यह अपेक्षा मुख्यतः बड़े शहरों और प्रदूषित क्षेत्रों के पास के संयंत्रों तक सीमित कर दी गई। "
  "BS-VI ईंधन के बाद पेट्रोल में बहुत कम सल्फ़र है; पराली जलाना कणिकीय पदार्थ, कार्बन मोनोऑक्साइड और दूसरी गैसों का बड़ा स्रोत है, पर अधिक सल्फ़र डाइऑक्साइड का नहीं; ईंट-भट्ठे योगदान देते हैं, पर बिजली संयंत्रों से बहुत कम।",
  "Ministry of Environment, Forest and Climate Change -- Environment (Protection) Amendment Rules, 2015 (emission standards for thermal power plants); Centre for Science and Environment -- sulphur dioxide from thermal power.",
  "env-so2-coal-power")

M(W, "easy", "The 'Swachh Survekshan' is an annual survey that ranks:",
  "'स्वच्छ सर्वेक्षण' एक वार्षिक सर्वेक्षण है, जो किसकी रैंकिंग करता है?",
  ["Cleanliness of cities and towns", "Air quality in rural areas", "Quality of water in rivers and lakes", "Forest cover of the States"],
  ["शहरों और कस्बों की स्वच्छता", "ग्रामीण क्षेत्रों की वायु गुणवत्ता", "नदियों और झीलों के पानी की गुणवत्ता", "राज्यों का वन आवरण"],
  0,
  "Swachh Survekshan, run by the Ministry of Housing and Urban Affairs since 2016 under the Swachh Bharat Mission (Urban), ranks cities and towns on sanitation and solid waste management, including segregation and processing of waste, citizen feedback and on-the-ground checks. "
  "Air quality is tracked by the CPCB's AQI and the 'Swachh Vayu Survekshan' under NCAP, river quality by the CPCB, and forest cover by the Forest Survey of India's biennial report.",
  "स्वच्छ सर्वेक्षण, जिसे आवास और शहरी कार्य मंत्रालय 2016 से स्वच्छ भारत मिशन (शहरी) के तहत चलाता है, शहरों और कस्बों को स्वच्छता और ठोस अपशिष्ट प्रबंधन पर रैंक करता है, जिसमें कचरे का पृथक्करण और प्रसंस्करण, नागरिकों की प्रतिक्रिया और ज़मीनी जाँच शामिल हैं। "
  "वायु गुणवत्ता पर CPCB का AQI और NCAP के तहत 'स्वच्छ वायु सर्वेक्षण' नज़र रखते हैं, नदियों की गुणवत्ता पर CPCB, और वन आवरण पर भारतीय वन सर्वेक्षण की द्विवार्षिक रिपोर्ट।",
  "Ministry of Housing and Urban Affairs -- Swachh Survekshan; Swachh Bharat Mission (Urban) 2.0.",
  "env-swachh-survekshan")

M(W, "hard", "In the resin identification code printed on plastic items, the number '1' inside the triangle of arrows stands for:",
  "प्लास्टिक की वस्तुओं पर छपे रेज़िन पहचान कोड (resin identification code) में तीरों के त्रिकोण के भीतर अंक '1' किसे दर्शाता है?",
  ["PET (polyethylene terephthalate)", "HDPE (high-density polyethylene)", "PVC (polyvinyl chloride)", "PP (polypropylene)"],
  ["PET (पॉलीएथिलीन टेरेफ़्थेलेट)", "HDPE (उच्च घनत्व पॉलीएथिलीन)", "PVC (पॉलीविनाइल क्लोराइड)", "PP (पॉलीप्रोपिलीन)"],
  0,
  "Code 1 is PET, the plastic of water and soft-drink bottles, which is widely recycled into fibre and new bottles; 2 is HDPE, 3 is PVC, 4 is LDPE, 5 is PP, 6 is polystyrene, and 7 is 'other'. "
  "The chasing-arrows triangle is often misread as a promise that the item is recyclable -- it only identifies the resin, and codes 3, 6 and 7 are rarely recycled in practice. India's plastic rules require such marking so that waste can be sorted by resin.",
  "कोड 1 PET है, पानी और शीतल पेय की बोतलों का प्लास्टिक, जिसे बड़े पैमाने पर रेशे और नई बोतलों में पुनर्चक्रित किया जाता है; 2 HDPE, 3 PVC, 4 LDPE, 5 PP, 6 पॉलीस्टाइरीन और 7 'अन्य' है। "
  "पीछा करते तीरों वाले त्रिकोण को प्रायः गलती से इस बात का वादा समझ लिया जाता है कि वस्तु पुनर्चक्रण योग्य है; यह केवल रेज़िन की पहचान बताता है, और कोड 3, 6 और 7 का व्यवहार में शायद ही पुनर्चक्रण होता है। भारत के प्लास्टिक नियम ऐसे चिह्नांकन को अनिवार्य करते हैं, ताकि कचरे को रेज़िन के अनुसार छाँटा जा सके।",
  "Bureau of Indian Standards, IS 14534 (guidelines for recycling of plastics, marking codes); Plastic Waste Management Rules, 2016 (marking and labelling).",
  "env-resin-identification-code")

# ---------------------------------------------------------------- Statement-I/II (medium, easy) and I/II/III (hard)
A(W, "medium",
  "Battery electric vehicles have no tailpipe emissions.",
  "बैटरी से चलने वाले विद्युत वाहनों से कोई टेलपाइप (धुआँ-नली) उत्सर्जन नहीं होता।",
  "Most of India's electricity is still generated from coal.",
  "भारत की अधिकांश बिजली अब भी कोयले से बनती है।",
  1,
  "Both statements are correct, but Statement-II does not explain Statement-I. An electric vehicle has no engine burning fuel, so it gives off no exhaust at the point of use -- which is why it cleans city air -- whatever the source of the electricity. "
  "Statement-II matters for a different question: how much an EV cuts emissions over its whole life. Although more than half of India's installed capacity is now non-fossil, coal still generates roughly three-quarters of the electricity actually produced, because solar and wind run for fewer hours; as the grid gets cleaner, so do EVs. The trap is to treat 'capacity' and 'generation' as the same.",
  "दोनों कथन सही हैं, पर कथन-II कथन-I की व्याख्या नहीं करता। विद्युत वाहन में ईंधन जलाने वाला इंजन नहीं होता, इसलिए उपयोग के स्थान पर उससे कोई धुआँ नहीं निकलता, बिजली का स्रोत चाहे जो हो; इसीलिए यह शहर की हवा साफ़ करता है। "
  "कथन-II एक अलग प्रश्न के लिए महत्त्वपूर्ण है: EV अपने पूरे जीवनकाल में उत्सर्जन कितना घटाता है। यद्यपि भारत की आधी से अधिक स्थापित क्षमता अब गैर-जीवाश्म है, वास्तव में बनने वाली बिजली का लगभग तीन-चौथाई भाग अब भी कोयले से आता है, क्योंकि सौर और पवन कम घंटे चलते हैं; ग्रिड जितना स्वच्छ होगा, EV उतने ही स्वच्छ होंगे। जाल 'क्षमता' और 'उत्पादन' को एक ही मान लेना है।",
  "Central Electricity Authority -- installed capacity and generation reports; International Energy Agency -- Global EV Outlook.",
  "env-ev-tailpipe-coal-grid")

A(W, "easy",
  "Open burning of plastic waste is harmful to health.",
  "प्लास्टिक कचरे को खुले में जलाना स्वास्थ्य के लिए हानिकारक है।",
  "It releases toxic substances such as dioxins and furans.",
  "इससे डाइऑक्सिन और फ़्यूरान जैसे विषैले पदार्थ निकलते हैं।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I. Burning plastics at low temperatures -- especially PVC and other chlorine-containing plastics -- produces dioxins and furans, persistent pollutants linked to cancer and to damage of the immune and hormone systems, along with fine particles and black carbon. That is why open burning of waste is prohibited under India's solid waste rules and penalised by the National Green Tribunal.",
  "दोनों कथन सही हैं, और कथन-II कथन-I की व्याख्या करता है। कम तापमान पर प्लास्टिक, विशेषकर PVC और क्लोरीन वाले दूसरे प्लास्टिक, जलाने से डाइऑक्सिन और फ़्यूरान बनते हैं, जो कैंसर और प्रतिरक्षा तथा हॉर्मोन तंत्र की क्षति से जुड़े स्थायी प्रदूषक हैं, साथ में सूक्ष्म कण और ब्लैक कार्बन भी निकलते हैं। इसीलिए भारत के ठोस अपशिष्ट नियमों के तहत कचरे को खुले में जलाना प्रतिबंधित है और राष्ट्रीय हरित अधिकरण इस पर दंड लगाता है।",
  "WHO -- dioxins and their effects on human health; Solid Waste Management Rules (prohibition of open burning); National Green Tribunal orders on open burning of waste.",
  "env-open-burning-plastic")

A(W, "hard",
  "Deep-sea mining of polymetallic nodules is highly controversial.",
  "बहुधात्विक पिंडों (polymetallic nodules) का गहरे समुद्र में खनन अत्यधिक विवादास्पद है।",
  "The nodules contain nickel, cobalt and manganese, which are in demand for batteries.",
  "इन पिंडों में निकल, कोबाल्ट और मैंगनीज़ होते हैं, जिनकी बैटरियों के लिए माँग है।",
  1,
  "Both Statement II and Statement III are correct, but only Statement III explains Statement I. The metals in the nodules explain why companies and governments want to mine the seabed; they do not explain why it is contested. "
  "The controversy comes from the risk to ecosystems: the nodules grow a few millimetres in a million years, the animals living on them are largely unknown to science, and sediment plumes could spread damage far beyond the mined area. Several countries have called for a moratorium while the International Seabed Authority drafts its mining code; India holds an ISA exploration contract for nodules in the Central Indian Ocean Basin and pursues it under its Deep Ocean Mission.",
  "कथन-II और कथन-III दोनों सही हैं, पर केवल कथन-III कथन-I की व्याख्या करता है। पिंडों में मौजूद धातुएँ बताती हैं कि कंपनियाँ और सरकारें समुद्र-तल का खनन क्यों करना चाहती हैं; वे यह नहीं बतातीं कि यह विवादित क्यों है। "
  "विवाद पारितंत्रों के जोखिम से आता है: ये पिंड दस लाख वर्षों में कुछ मिलीमीटर बढ़ते हैं, उन पर रहने वाले जीव विज्ञान के लिए लगभग अज्ञात हैं, और तलछट के बादल खनन क्षेत्र से बहुत दूर तक नुकसान फैला सकते हैं। अंतरराष्ट्रीय समुद्र-तल प्राधिकरण (ISA) जब तक अपना खनन कोड तैयार कर रहा है, कई देशों ने रोक (moratorium) की माँग की है; भारत के पास मध्य हिंद महासागर बेसिन में पिंडों के लिए ISA का अन्वेषण अनुबंध है, जिस पर वह अपने गहरे महासागर मिशन के तहत काम करता है।",
  "International Seabed Authority -- exploration contracts and draft exploitation regulations; Ministry of Earth Sciences -- Deep Ocean Mission (2021).",
  "env-deep-sea-mining",
  s3="Mining could destroy slow-recovering seabed ecosystems about which very little is known.",
  s3_hi="खनन धीरे-धीरे उबरने वाले उन समुद्र-तलीय पारितंत्रों को नष्ट कर सकता है, जिनके बारे में बहुत कम जानकारी है।")

# ---------------------------------------------------------------- pairs (1, easy)
P(W, "easy", "Consider the following pairs of air pollutants and their main sources:",
  "वायु प्रदूषकों और उनके मुख्य स्रोतों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Sulphur dioxide : Burning of coal", "Nitrogen oxides : High-temperature combustion in vehicle engines",
   "Carbon monoxide : Incomplete combustion of fuels", "Chlorofluorocarbons : Volcanic eruptions"],
  ["सल्फ़र डाइऑक्साइड : कोयले का दहन", "नाइट्रोजन ऑक्साइड : वाहनों के इंजनों में उच्च तापमान पर दहन",
   "कार्बन मोनोऑक्साइड : ईंधनों का अपूर्ण दहन", "क्लोरोफ़्लोरोकार्बन : ज्वालामुखी विस्फोट"],
  2,
  "Three pairs are correct. Sulphur in coal becomes sulphur dioxide when it burns; at the high temperatures inside engines, nitrogen and oxygen of the air combine into nitrogen oxides; and carbon monoxide forms when fuel burns with too little oxygen. "
  "Pair 4 is wrong: CFCs are entirely man-made, used in the past as refrigerants, aerosol propellants and foam-blowing agents -- volcanoes emit sulphur dioxide and ash, not CFCs.",
  "तीन युग्म सही हैं। कोयले का सल्फ़र जलने पर सल्फ़र डाइऑक्साइड बन जाता है; इंजनों के भीतर के उच्च तापमान पर हवा की नाइट्रोजन और ऑक्सीजन मिलकर नाइट्रोजन ऑक्साइड बनाती हैं; और कार्बन मोनोऑक्साइड तब बनती है जब ईंधन बहुत कम ऑक्सीजन में जलता है। "
  "युग्म 4 गलत है: CFC पूरी तरह मानव-निर्मित हैं, जिनका उपयोग पहले प्रशीतक, एरोसोल प्रणोदक और फ़ोम बनाने में होता था; ज्वालामुखी सल्फ़र डाइऑक्साइड और राख छोड़ते हैं, CFC नहीं।",
  f"{CHEM11} (air pollution: gaseous pollutants).",
  "env-pollutant-sources-pairs")

if __name__ == "__main__":
    write("env_l2_t10_pollution.sql")
