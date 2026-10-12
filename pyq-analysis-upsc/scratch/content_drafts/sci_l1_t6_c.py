# -*- coding: utf-8 -*-
"""Level 1 · Test 6 (Science & Technology, NCERT Foundation) -- part C: Biology, Health & Biotechnology (8) and
Energy & Environmental Technology (18) (upsc_l1_cell_targets.mjs 6).
Biology: easy MCQ 1, easy statement 2, medium MCQ 1, medium statement 3, hard statement 1. Energy: easy MCQ 1, easy
statement 4, medium MCQ 2, medium statement 7, medium Statement-I/II 1, hard MCQ 1, hard statement 2.
The angle is NCERT Science VIII-X (microbes and food preservation, life processes, control and coordination,
heredity; work and energy, power and its units, fuels, sources of energy) and Physics XI-XII energy ideas, with the
Ministry of Power and MNRE classifications that apply them. Level-2 S&T, Environment and Geography facts are not
repeated (vaccines, AMR, blood groups, insulin, deficiency diseases, protozoan diseases; ethanol, hydrogen, storage,
batteries, solar technologies and water heaters, wind limits, hydro head, LED/UJALA, efficiency labels, fuel
cells, SMRs, control rods, fusion, LPG behaviour, fly ash, BS-VI, ESPs, CCUS, nuclear plant locations, the three
stages); nor are Level-1 Environment's calorific values, biogas, OTEC, geothermal, CNG or the solar cooker."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Science & Technology"
d.REQUIRE_CRAFT = True
BI = "Biology, Health & Biotechnology"
EN = "Energy & Environmental Technology"
SC8 = "NCERT Class VIII, Science"
SC9 = "NCERT Class IX, Science"
SC10 = "NCERT Class X, Science"
MOP = "Ministry of Power"
MNRE = "Ministry of New and Renewable Energy"

# ================================================================ BIOLOGY (8)
# ---------------------------------------------------------------- easy MCQ (1)
M(BI, "easy", "Which one of the following diseases is caused by a bacterium?",
  "निम्नलिखित में से कौन-सा रोग जीवाणु से होता है?",
  ["typhoid", "measles", "chickenpox", "polio"],
  ["टाइफ़ाइड (मियादी बुख़ार)", "खसरा", "छोटी माता (चिकनपॉक्स)", "पोलियो"],
  0,
  "Typhoid is caused by the bacterium Salmonella Typhi, spread through contaminated food and water, and is treated with antibiotics; tuberculosis and cholera are other bacterial diseases. "
  "Measles, chickenpox and polio are caused by viruses, which antibiotics cannot kill -- they are prevented chiefly by vaccination.",
  "टाइफ़ाइड साल्मोनेला टाइफ़ी जीवाणु से होता है, दूषित भोजन और जल से फैलता है, और प्रतिजैविकों से इसका उपचार होता है; क्षयरोग और हैज़ा अन्य जीवाणुजनित रोग हैं। "
  "खसरा, छोटी माता और पोलियो विषाणुओं से होते हैं, जिन्हें प्रतिजैविक नहीं मार सकते -- इनकी रोकथाम मुख्यतः टीकाकरण से होती है।",
  f"{SC8} (Microorganisms: Friend and Foe); {SC9} (Why Do We Fall Ill?).",
  "l1-sci-typhoid-bacterial", pos=3, craft="recall")

# ---------------------------------------------------------------- easy statement (2)
S(BI, "easy", "Consider the following statements about preserving food:",
  "भोजन के परिरक्षण के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["In pasteurisation, milk is heated to about 70 degrees Celsius for 15 to 30 seconds and then suddenly chilled.",
   "Salt and sugar preserve food such as pickles and jams by checking the growth of microbes."],
  ["पाश्चरीकरण में दूध को लगभग 70 डिग्री सेल्सियस पर 15 से 30 सेकंड तक गर्म करके अचानक ठंडा किया जाता है।",
   "नमक और चीनी अचार और जैम जैसे खाद्य पदार्थों को सूक्ष्मजीवों की वृद्धि रोककर परिरक्षित करते हैं।"],
  T2, 2,
  "Both statements are correct. Pasteurisation, named after Louis Pasteur, kills most harmful microbes without boiling the milk, so its taste and nutrients are little changed. "
  "Salt and sugar draw water out of microbial cells and lower the water available for their growth, which is why salted fish and sugary jams keep for months; oil and vinegar, and chemicals such as sodium benzoate, are other preservatives.",
  "दोनों कथन सही हैं। लुई पाश्चर के नाम पर पाश्चरीकरण दूध को उबाले बिना अधिकांश हानिकारक सूक्ष्मजीवों को मार देता है, इसलिए उसका स्वाद और पोषक तत्व बहुत कम बदलते हैं। "
  "नमक और चीनी सूक्ष्मजीवी कोशिकाओं से पानी खींच लेते हैं और उनकी वृद्धि के लिए उपलब्ध पानी घटाते हैं, इसीलिए नमकीन मछली और मीठे जैम महीनों टिकते हैं; तेल और सिरका, और सोडियम बेंज़ोएट जैसे रसायन अन्य परिरक्षक हैं।",
  f"{SC8} (Microorganisms: Friend and Foe).",
  "l1-sci-pasteurisation-salt-sugar", craft="recall")

S(BI, "easy", "Consider the following statements about human digestion:",
  "मानव पाचन के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The digestion of starch begins in the mouth, where saliva contains an enzyme that acts on it.",
   "Bile, made in the liver and stored in the gall bladder, breaks fats into small globules, though it contains no digestive enzymes.",
   "The small intestine is the main site of the complete digestion and absorption of food, and its villi greatly increase the surface for absorption."],
  ["मंड (starch) का पाचन मुँह में आरंभ होता है, जहाँ लार में उस पर क्रिया करने वाला एक एंज़ाइम होता है।",
   "यकृत में बना और पित्ताशय में संचित पित्त वसा को छोटी गोलिकाओं में तोड़ता है, यद्यपि उसमें कोई पाचक एंज़ाइम नहीं होता।",
   "छोटी आँत भोजन के पूर्ण पाचन और अवशोषण का मुख्य स्थान है, और उसके रसांकुर (villi) अवशोषण की सतह को बहुत बढ़ा देते हैं।"],
  C3, 2,
  "All three statements are correct. Salivary amylase begins breaking starch into sugar, which is why a piece of bread chewed for long starts to taste sweet; protein digestion begins in the stomach, with pepsin working in an acid medium. "
  "By emulsifying fats, bile gives the fat-digesting enzymes of the pancreas a much larger surface to act on.",
  "तीनों कथन सही हैं। लार का एमाइलेज़ मंड को शर्करा में तोड़ना शुरू करता है, इसीलिए देर तक चबाई गई रोटी मीठी लगने लगती है; प्रोटीन का पाचन आमाशय में, अम्लीय माध्यम में काम करने वाले पेप्सिन से आरंभ होता है। "
  "वसा का पायसीकरण करके पित्त अग्न्याशय के वसा-पाचक एंज़ाइमों को काम करने के लिए कहीं बड़ी सतह देता है।",
  f"{SC10} (Life Processes).",
  "l1-sci-digestion-saliva-bile-villi", craft="recall")

# ---------------------------------------------------------------- medium MCQ (1)
M(BI, "medium", "A person who suddenly faces danger feels the heart race and breathing quicken, as the body prepares to fight or run. The hormone mainly responsible is",
  "अचानक ख़तरे का सामना करने वाले व्यक्ति का दिल तेज़ धड़कता और साँस तेज़ हो जाती है, क्योंकि शरीर लड़ने या भागने की तैयारी करता है। इसके लिए मुख्यतः कौन-सा हार्मोन उत्तरदायी है?",
  ["adrenaline", "insulin", "thyroxine", "growth hormone"],
  ["एड्रीनलीन", "इंसुलिन", "थायरॉक्सिन", "वृद्धि हार्मोन"],
  0,
  "Adrenaline, secreted by the adrenal glands directly into the blood, speeds up the heartbeat to supply more oxygen to the muscles, diverts blood from the digestive system and skin, and raises the breathing rate -- preparing the body for 'fight or flight'. "
  "Insulin, from the pancreas, regulates blood sugar; thyroxine, which needs iodine, regulates metabolism; and growth hormone, from the pituitary, regulates growth.",
  "अधिवृक्क (adrenal) ग्रंथियों द्वारा सीधे रक्त में स्रावित एड्रीनलीन मांसपेशियों को अधिक ऑक्सीजन देने के लिए हृदय गति बढ़ाता है, पाचन तंत्र और त्वचा से रक्त हटाता है और साँस की दर बढ़ाता है -- शरीर को 'लड़ो या भागो' के लिए तैयार करता है। "
  "अग्न्याशय का इंसुलिन रक्त शर्करा नियंत्रित करता है; आयोडीन चाहने वाला थायरॉक्सिन उपापचय नियंत्रित करता है; और पीयूष ग्रंथि का वृद्धि हार्मोन वृद्धि नियंत्रित करता है।",
  f"{SC10} (Control and Coordination).",
  "l1-sci-adrenaline-fight-or-flight", pos=0, craft="application")

# ---------------------------------------------------------------- medium statement (3)
S(BI, "medium", "Consider the following statements about plant hormones:",
  "पादप हार्मोनों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Auxin makes a shoot bend towards light, because it collects on the shaded side and makes the cells there grow longer.",
   "Abscisic acid inhibits growth, and its effects include the wilting of leaves.",
   "Cytokinins promote cell division and are present in high concentration in fruits and seeds."],
  ["ऑक्सिन प्ररोह को प्रकाश की ओर मोड़ता है, क्योंकि वह छायादार भाग में एकत्र होकर वहाँ की कोशिकाओं को लंबा बढ़ाता है।",
   "ऐब्सिसिक अम्ल वृद्धि को रोकता है, और इसके प्रभावों में पत्तियों का मुरझाना शामिल है।",
   "साइटोकाइनिन कोशिका विभाजन को बढ़ावा देते हैं और फलों तथा बीजों में अधिक सांद्रता में होते हैं।"],
  C3, 2,
  "All three statements are correct. Plants have no nervous system; they coordinate growth through hormones, and the bending of a shoot towards light (phototropism) is the result of unequal growth on its two sides. "
  "Gibberellins, another group, promote the growth of the stem; abscisic acid, in contrast, helps a plant cope with stress such as drought.",
  "तीनों कथन सही हैं। पौधों में तंत्रिका तंत्र नहीं होता; वे हार्मोनों द्वारा वृद्धि का समन्वय करते हैं, और प्ररोह का प्रकाश की ओर मुड़ना (प्रकाशानुवर्तन) उसके दोनों भागों में असमान वृद्धि का परिणाम है। "
  "जिबरेलिन, एक अन्य समूह, तने की वृद्धि बढ़ाते हैं; इसके विपरीत, ऐब्सिसिक अम्ल सूखे जैसे तनाव से निपटने में पौधे की सहायता करता है।",
  f"{SC10} (Control and Coordination).",
  "l1-sci-plant-hormones-auxin-aba", craft="inference")

S(BI, "medium", "Consider the following statements about the circulation of blood:",
  "रक्त परिसंचरण के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The pulmonary artery carries deoxygenated blood from the heart to the lungs.",
   "The pulmonary veins carry oxygenated blood from the lungs to the left atrium.",
   "In fishes, the heart has two chambers, and blood passes through it only once in each complete circuit.",
   "In humans, blood passes through the heart twice in each complete circuit."],
  ["फुफ्फुसीय धमनी हृदय से फेफड़ों तक विऑक्सीजनित रक्त ले जाती है।",
   "फुफ्फुसीय शिराएँ फेफड़ों से बाएँ अलिंद तक ऑक्सीजनित रक्त लाती हैं।",
   "मछलियों में हृदय के दो कक्ष होते हैं, और हर पूर्ण चक्र में रक्त उससे केवल एक बार गुज़रता है।",
   "मनुष्यों में हर पूर्ण चक्र में रक्त हृदय से दो बार गुज़रता है।"],
  C4, 3,
  "All four statements are correct. Arteries are defined by carrying blood away from the heart and veins by carrying it towards the heart, not by how much oxygen the blood holds -- hence the pulmonary exceptions. "
  "The double circulation of birds and mammals keeps oxygenated and deoxygenated blood fully separate, giving the efficient oxygen supply that animals which keep a constant body temperature need.",
  "चारों कथन सही हैं। धमनियाँ हृदय से दूर और शिराएँ हृदय की ओर रक्त ले जाने से परिभाषित होती हैं, रक्त में ऑक्सीजन की मात्रा से नहीं -- इसीलिए फुफ्फुसीय अपवाद हैं। "
  "पक्षियों और स्तनधारियों का दोहरा परिसंचरण ऑक्सीजनित और विऑक्सीजनित रक्त को पूरी तरह अलग रखता है, जिससे वह कुशल ऑक्सीजन आपूर्ति मिलती है जिसकी शरीर का स्थिर तापमान रखने वाले जंतुओं को आवश्यकता होती है।",
  f"{SC10} (Life Processes).",
  "l1-sci-pulmonary-double-circulation", craft="precision")

S(BI, "medium", "Consider the following statements about respiration:",
  "श्वसन के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Muscle cramps during hard exercise are caused by the build-up of lactic acid when the muscle cells run short of oxygen.",
   "Anaerobic respiration releases more energy from a molecule of glucose than aerobic respiration does.",
   "Plants respire only at night."],
  ["कड़े व्यायाम के दौरान मांसपेशियों में ऐंठन तब होती है जब ऑक्सीजन की कमी होने पर मांसपेशी कोशिकाओं में लैक्टिक अम्ल जमा हो जाता है।",
   "अवायवीय श्वसन ग्लूकोज़ के एक अणु से वायवीय श्वसन की तुलना में अधिक ऊर्जा मुक्त करता है।",
   "पौधे केवल रात में श्वसन करते हैं।"],
  C3, 0,
  "Only statement 1 is correct: in a sprint, muscles use oxygen faster than the blood can supply it and switch to breaking glucose down without oxygen, into lactic acid. "
  "Statement 2 is wrong: aerobic respiration, completed in the mitochondria, releases far more energy. Statement 3 is wrong: plants respire all the time; by day their photosynthesis simply exceeds respiration, so they give out more oxygen than they take in.",
  "केवल कथन 1 सही है: तेज़ दौड़ में मांसपेशियाँ ऑक्सीजन का उपयोग रक्त की आपूर्ति से तेज़ करती हैं और ग्लूकोज़ को बिना ऑक्सीजन के लैक्टिक अम्ल में तोड़ने लगती हैं। "
  "कथन 2 गलत है: माइटोकॉन्ड्रिया में पूरा होने वाला वायवीय श्वसन कहीं अधिक ऊर्जा मुक्त करता है। कथन 3 गलत है: पौधे हर समय श्वसन करते हैं; दिन में उनका प्रकाश-संश्लेषण बस श्वसन से अधिक होता है, इसलिए वे जितनी ऑक्सीजन लेते हैं उससे अधिक छोड़ते हैं।",
  f"{SC10} (Life Processes).",
  "l1-sci-respiration-lactic-acid", craft="inference")

# ---------------------------------------------------------------- hard statement (1)
S(BI, "hard", "Consider the following statements about sex determination:",
  "लिंग निर्धारण के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["In humans, the sex of a child is determined by whether the father's sperm carries an X or a Y chromosome.",
   "In some reptiles, the temperature at which the fertilised eggs are kept decides the sex of the young.",
   "A child who inherits an X chromosome from the father will be a boy."],
  ["मनुष्यों में बच्चे का लिंग इस पर निर्भर करता है कि पिता के शुक्राणु में X गुणसूत्र है या Y।",
   "कुछ सरीसृपों में निषेचित अंडों को जिस तापमान पर रखा जाता है, वह संतान का लिंग तय करता है।",
   "पिता से X गुणसूत्र पाने वाला बच्चा लड़का होगा।"],
  C3, 1,
  "Statements 1 and 2 are correct. A woman has two X chromosomes and passes one X to every child; a man has one X and one Y, so a child receiving his Y becomes a boy and one receiving his X a girl -- which also shows that blaming mothers for the sex of a child has no basis. "
  "Statement 3 is wrong for that reason: an X from the father, with the mother's X, makes a girl. In turtles and many crocodiles, the warmth of the nest decides the sex instead.",
  "कथन 1 और 2 सही हैं। स्त्री में दो X गुणसूत्र होते हैं और वह हर बच्चे को एक X देती है; पुरुष में एक X और एक Y होता है, इसलिए उसका Y पाने वाला बच्चा लड़का और X पाने वाला लड़की होता है -- इससे यह भी दिखता है कि बच्चे के लिंग के लिए माताओं को दोष देने का कोई आधार नहीं। "
  "इसी कारण कथन 3 गलत है: पिता का X, माता के X के साथ, लड़की बनाता है। कछुओं और कई मगरमच्छों में इसके बजाय घोंसले की गर्मी लिंग तय करती है।",
  f"{SC10} (Heredity).",
  "l1-sci-sex-determination-xy-temperature", craft="inference")

# ================================================================ ENERGY (18)
# ---------------------------------------------------------------- easy MCQ (1)
M(EN, "easy", "Liquefied petroleum gas (LPG), used as a cooking fuel, consists mainly of",
  "रसोई ईंधन के रूप में प्रयुक्त द्रवित पेट्रोलियम गैस (LPG) मुख्यतः किससे बनी होती है?",
  ["butane", "methane", "hydrogen", "ethylene"],
  ["ब्यूटेन", "मेथेन", "हाइड्रोजन", "एथिलीन"],
  0,
  "LPG is mainly butane, with some propane, gases that turn to liquid under moderate pressure, so a large amount can be stored in a small cylinder; it is obtained from refining petroleum and processing natural gas. "
  "Compressed natural gas (CNG), used in vehicles, is mainly methane, which must be stored under much higher pressure.",
  "LPG मुख्यतः ब्यूटेन है, जिसमें कुछ प्रोपेन होती है -- ये गैसें मध्यम दाब पर द्रव बन जाती हैं, इसलिए छोटे सिलेंडर में बड़ी मात्रा रखी जा सकती है; यह पेट्रोलियम के शोधन और प्राकृतिक गैस के प्रसंस्करण से मिलती है। "
  "वाहनों में प्रयुक्त संपीडित प्राकृतिक गैस (CNG) मुख्यतः मेथेन है, जिसे कहीं अधिक दाब पर रखना पड़ता है।",
  f"{SC8} (Coal and Petroleum); {SC10} (Carbon and its Compounds).",
  "l1-sci-lpg-butane", pos=3, craft="recall")

# ---------------------------------------------------------------- easy statement (4)
S(EN, "easy", "Consider the following statements about work and energy:",
  "कार्य और ऊर्जा के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Energy can neither be created nor destroyed; it only changes from one form to another.",
   "As a ball falls, its potential energy is converted into kinetic energy.",
   "A person holding a heavy suitcase still for an hour does work on it, in the scientific sense."],
  ["ऊर्जा न तो बनाई जा सकती है न नष्ट की जा सकती है; वह केवल एक रूप से दूसरे रूप में बदलती है।",
   "गिरती हुई गेंद की स्थितिज ऊर्जा गतिज ऊर्जा में बदलती है।",
   "एक घंटे तक भारी सूटकेस को स्थिर पकड़े रहने वाला व्यक्ति वैज्ञानिक अर्थ में उस पर कार्य करता है।"],
  C3, 1,
  "Statements 1 and 2 are correct. Statement 3 is wrong: in science, work is done only when a force moves its point of application -- work equals force times the displacement in the direction of the force -- so holding a load without moving it does no work, however tiring it is. "
  "The tiredness comes from the energy the muscles use to stay tense, not from work done on the suitcase.",
  "कथन 1 और 2 सही हैं। कथन 3 गलत है: विज्ञान में कार्य तभी होता है जब बल अपने लगने के बिंदु को खिसकाए -- कार्य बल और बल की दिशा में विस्थापन का गुणनफल है -- इसलिए भार को बिना खिसकाए पकड़े रहना, चाहे कितना भी थकाने वाला हो, कोई कार्य नहीं है। "
  "थकान मांसपेशियों के तने रहने में ख़र्च ऊर्जा से आती है, सूटकेस पर किए गए कार्य से नहीं।",
  f"{SC9} (Work and Energy).",
  "l1-sci-work-energy-conservation", craft="application")

S(EN, "easy", "Consider the following statements about charcoal:",
  "लकड़ी के कोयले (चारकोल) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Charcoal is made by heating wood in a limited supply of air.",
   "Charcoal burns with a large, smoky flame."],
  ["चारकोल लकड़ी को सीमित वायु में गर्म करके बनाया जाता है।",
   "चारकोल बड़ी, धुएँ भरी लौ के साथ जलता है।"],
  T2, 0,
  "Only statement 1 is correct: heating wood without enough air to burn it drives off water and volatile substances, leaving mostly carbon. "
  "Statement 2 is wrong: because those volatile substances are gone, charcoal does not vaporise and burns with a glow and very little flame or smoke, giving more heat for its weight than wood -- which is why it has long been used by blacksmiths and in sigris and barbecues.",
  "केवल कथन 1 सही है: जलने लायक़ वायु के बिना लकड़ी को गर्म करने से पानी और वाष्पशील पदार्थ निकल जाते हैं, और अधिकतर कार्बन बचता है। "
  "कथन 2 गलत है: वाष्पशील पदार्थ निकल जाने के कारण चारकोल वाष्पित नहीं होता और बहुत कम लौ या धुएँ के साथ दहकता है, और भार के अनुपात में लकड़ी से अधिक ऊष्मा देता है -- इसीलिए लोहार और सिगड़ियाँ लंबे समय से इसका उपयोग करते रहे हैं।",
  f"{SC8} (Combustion and Flame); {SC10} (Sources of Energy, earlier editions).",
  "l1-sci-charcoal-flameless", craft="precision")

S(EN, "easy", "Consider the following statements about power and its units:",
  "शक्ति और उसकी इकाइयों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Power is the rate of doing work, and its unit is the watt.",
   "One horsepower is about 746 watts.",
   "The kilowatt-hour is a unit of power."],
  ["शक्ति कार्य करने की दर है, और इसकी इकाई वाट है।",
   "एक अश्वशक्ति लगभग 746 वाट है।",
   "किलोवाट-घंटा शक्ति की इकाई है।"],
  C3, 1,
  "Statements 1 and 2 are correct: one watt is one joule of work done each second. "
  "Statement 3 is wrong: the kilowatt-hour is a unit of energy -- the energy used by a 1,000-watt appliance in one hour -- and it is the 'unit' on an electricity bill; power tells how fast energy is used, energy how much.",
  "कथन 1 और 2 सही हैं: एक वाट प्रति सेकंड किया गया एक जूल कार्य है। "
  "कथन 3 गलत है: किलोवाट-घंटा ऊर्जा की इकाई है -- 1,000 वाट का उपकरण एक घंटे में जितनी ऊर्जा लेता है -- और यही बिजली के बिल की 'यूनिट' है; शक्ति बताती है कि ऊर्जा कितनी तेज़ी से ख़र्च होती है, ऊर्जा बताती है कितनी।",
  f"{SC9} (Work and Energy).",
  "l1-sci-power-watt-horsepower-kwh", craft="precision")

S(EN, "easy", "Consider the following statements about fixed solar panels installed in India:",
  "भारत में लगाए गए स्थिर सौर पैनलों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["They are usually made to face south.",
   "They are usually tilted at an angle roughly equal to the latitude of the place, to get the most energy over the year."],
  ["इन्हें सामान्यतः दक्षिण की ओर मुख करके लगाया जाता है।",
   "वर्ष भर में अधिकतम ऊर्जा पाने के लिए इन्हें सामान्यतः स्थान के अक्षांश के लगभग बराबर कोण पर झुकाया जाता है।"],
  T2, 2,
  "Both statements are correct. India lies north of the Equator, so the Sun is in the southern half of the sky for most of the year; a south-facing panel catches its rays most directly. "
  "Tilting it at about the latitude angle makes the panel face the Sun squarely around the equinoxes and balances the high summer Sun against the low winter Sun -- a panel in Chennai is tilted less than one in Delhi.",
  "दोनों कथन सही हैं। भारत विषुवत रेखा के उत्तर में है, इसलिए वर्ष के अधिकांश भाग में सूर्य आकाश के दक्षिणी अर्धभाग में रहता है; दक्षिणमुखी पैनल उसकी किरणों को सबसे सीधा पकड़ता है। "
  "पैनल को अक्षांश के लगभग बराबर कोण पर झुकाने से वह विषुवों के आसपास सूर्य के ठीक सामने रहता है और गर्मियों के ऊँचे तथा सर्दियों के नीचे सूर्य के बीच संतुलन बनता है -- चेन्नई में पैनल दिल्ली से कम झुकाया जाता है।",
  f"{MNRE} (rooftop solar guidelines); NCERT Class VI-XI, Geography (latitude and the Sun's path).",
  "l1-sci-solar-panel-south-latitude-tilt", craft="application")

# ---------------------------------------------------------------- medium MCQ (2)
M(EN, "medium", "The power that a wind turbine can draw from the wind varies roughly as the cube of the wind speed. If the wind speed doubles, the power available increases about",
  "पवन टरबाइन पवन से जितनी शक्ति ले सकती है, वह मोटे तौर पर पवन की गति के घन के अनुसार बदलती है। यदि पवन की गति दोगुनी हो जाए, तो उपलब्ध शक्ति लगभग कितनी बढ़ती है?",
  ["eight times", "twice", "four times", "sixteen times"],
  ["आठ गुना", "दोगुनी", "चार गुना", "सोलह गुना"],
  0,
  "Power varies as the cube of the speed: 2 x 2 x 2 = 8. The kinetic energy of each kilogram of air rises with the square of its speed, and twice as much air passes through the blades each second, giving the extra factor. "
  "This is why sites with only slightly stronger winds, such as coasts, passes and offshore areas, are so much more valuable, and why turbines are mounted on tall towers where the wind is faster.",
  "शक्ति गति के घन के अनुसार बदलती है: 2 x 2 x 2 = 8। हर किलोग्राम वायु की गतिज ऊर्जा उसकी गति के वर्ग के साथ बढ़ती है, और हर सेकंड पंखुड़ियों से दोगुनी वायु गुज़रती है, जिससे अतिरिक्त गुणक आता है। "
  "इसीलिए थोड़ी-सी तेज़ पवन वाले स्थल, जैसे तट, दर्रे और अपतटीय क्षेत्र, कहीं अधिक मूल्यवान हैं, और टरबाइनें ऊँचे टावरों पर लगाई जाती हैं जहाँ पवन तेज़ होती है।",
  f"{MNRE} (wind energy); NCERT Class XI, Physics (Work, Energy and Power).",
  "l1-sci-wind-power-cube-law", pos=3, craft="application")

M(EN, "medium", "In a hydroelectric power station, the main energy changes, in order, are from",
  "जलविद्युत केंद्र में मुख्य ऊर्जा परिवर्तन, क्रम से, किस प्रकार होते हैं?",
  ["potential, to kinetic, to electrical energy", "kinetic, to potential, to electrical energy",
   "chemical, to heat, to electrical energy", "heat, to kinetic, to electrical energy"],
  ["स्थितिज से गतिज, फिर विद्युत ऊर्जा", "गतिज से स्थितिज, फिर विद्युत ऊर्जा",
   "रासायनिक से ऊष्मा, फिर विद्युत ऊर्जा", "ऊष्मा से गतिज, फिर विद्युत ऊर्जा"],
  0,
  "Water held high behind a dam has potential energy; as it falls through the penstock it gains kinetic energy, which turns the turbine, and the generator coupled to the turbine converts that mechanical energy into electrical energy. "
  "A thermal power station, in contrast, goes from the chemical energy of the fuel to heat, then to the kinetic energy of steam and the turbine, and finally to electricity.",
  "बाँध के पीछे ऊँचाई पर रोके गए पानी में स्थितिज ऊर्जा होती है; पेनस्टॉक से गिरते हुए वह गतिज ऊर्जा पाता है, जो टरबाइन घुमाती है, और टरबाइन से जुड़ा जनित्र उस यांत्रिक ऊर्जा को विद्युत ऊर्जा में बदलता है। "
  "इसके विपरीत, ताप विद्युत केंद्र ईंधन की रासायनिक ऊर्जा से ऊष्मा, फिर भाप और टरबाइन की गतिज ऊर्जा, और अंत में बिजली तक जाता है।",
  f"{SC9} (Work and Energy); {SC10} (Sources of Energy, earlier editions).",
  "l1-sci-hydro-energy-conversion-chain", pos=0, craft="application")

# ---------------------------------------------------------------- medium statement (7)
S(EN, "medium", "Consider the following statements about grid-connected rooftop solar systems:",
  "ग्रिड से जुड़ी छत पर लगी सौर प्रणालियों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Under net metering, surplus solar power that a household sends to the grid is set off against the power it draws from the grid.",
   "A grid-connected rooftop system without batteries stops supplying power during a grid outage, for the safety of line workers.",
   "Rooftop solar panels produce most of their power at night."],
  ["नेट मीटरिंग के अंतर्गत किसी परिवार द्वारा ग्रिड को भेजी गई अतिरिक्त सौर बिजली ग्रिड से ली गई बिजली में समायोजित होती है।",
   "बिना बैटरी वाली ग्रिड से जुड़ी छत की प्रणाली ग्रिड बंद होने पर, लाइन पर काम करने वालों की सुरक्षा के लिए, बिजली देना बंद कर देती है।",
   "छत के सौर पैनल अपनी अधिकांश बिजली रात में उत्पन्न करते हैं।"],
  C3, 1,
  "Statements 1 and 2 are correct: net metering lets the grid act like a store, since solar output peaks at midday while household use peaks in the evening; and the inverter is designed to switch off when the grid fails, so that it does not send power into lines that workers believe are dead. "
  "Statement 3 is wrong: panels produce power only in daylight, most around noon on clear days.",
  "कथन 1 और 2 सही हैं: नेट मीटरिंग ग्रिड को भंडार की तरह काम करने देती है, क्योंकि सौर उत्पादन दोपहर में और घरेलू उपयोग शाम को सबसे अधिक होता है; और इन्वर्टर ग्रिड बंद होने पर बंद होने के लिए बना है, ताकि वह उन लाइनों में बिजली न भेजे जिन्हें कर्मी बिजली-रहित मान रहे हों। "
  "कथन 3 गलत है: पैनल केवल दिन के प्रकाश में, साफ़ दिनों में दोपहर के आसपास सबसे अधिक, बिजली बनाते हैं।",
  f"{MNRE} (grid-connected rooftop solar programme); Central Electricity Authority (connectivity standards).",
  "l1-sci-net-metering-anti-islanding", craft="inference")

S(EN, "medium", "Consider the following statements about bagasse-based cogeneration in sugar mills:",
  "चीनी मिलों में खोई (bagasse) आधारित सह-उत्पादन (cogeneration) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Bagasse is the fibrous residue left after the juice is extracted from sugarcane.",
   "Sugar mills burn bagasse to raise steam for their own processes and also to generate electricity.",
   "Many mills sell the surplus electricity to the grid."],
  ["खोई गन्ने से रस निकालने के बाद बचा रेशेदार अवशेष है।",
   "चीनी मिलें अपनी प्रक्रियाओं के लिए भाप बनाने और बिजली उत्पन्न करने के लिए खोई जलाती हैं।",
   "कई मिलें अतिरिक्त बिजली ग्रिड को बेचती हैं।"],
  C3, 2,
  "All three statements are correct. Cogeneration means producing heat and power from the same fuel, which uses far more of the fuel's energy than generating electricity alone; bagasse cogeneration is counted as a renewable, biomass-based source of power. "
  "It turns a waste product into income for the mills during the crushing season, when the bagasse is available.",
  "तीनों कथन सही हैं। सह-उत्पादन का अर्थ है एक ही ईंधन से ऊष्मा और बिजली दोनों बनाना, जो केवल बिजली बनाने की तुलना में ईंधन की कहीं अधिक ऊर्जा का उपयोग करता है; खोई सह-उत्पादन बिजली का नवीकरणीय, जैव-भार आधारित स्रोत माना जाता है। "
  "यह पेराई के मौसम में, जब खोई उपलब्ध होती है, एक अपशिष्ट उत्पाद को मिलों की आय में बदल देता है।",
  f"{MNRE} (bagasse cogeneration programme).",
  "l1-sci-bagasse-cogeneration", craft="linkage")

S(EN, "medium", "Consider the following statements about hydropower in India:",
  "भारत में जलविद्युत के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Hydro projects of up to 25 MW are classified as 'small hydro' and are looked after by the Ministry of New and Renewable Energy.",
   "In 2019, large hydro projects, above 25 MW, were also declared a renewable source of energy.",
   "Distribution companies have been given hydropower purchase obligations, as part of their renewable purchase obligations.",
   "Run-of-river projects store little water and depend largely on the river's natural flow."],
  ["25 मेगावाट तक की जलविद्युत परियोजनाएँ 'लघु जलविद्युत' मानी जाती हैं और नवीन एवं नवीकरणीय ऊर्जा मंत्रालय उनकी देखरेख करता है।",
   "2019 में 25 मेगावाट से बड़ी जलविद्युत परियोजनाओं को भी ऊर्जा का नवीकरणीय स्रोत घोषित किया गया।",
   "वितरण कंपनियों को उनके नवीकरणीय क्रय दायित्वों के भाग के रूप में जलविद्युत क्रय दायित्व दिए गए हैं।",
   "नदी-प्रवाह (run-of-river) परियोजनाएँ बहुत कम पानी संचित करती हैं और मुख्यतः नदी के प्राकृतिक प्रवाह पर निर्भर रहती हैं।"],
  C4, 3,
  "All four statements are correct. Until 2019 only small hydro counted towards India's renewable targets; declaring large hydro renewable, with purchase obligations and tariff support, was meant to revive investment in a clean source that can also be ramped up and down to balance solar and wind. "
  "Run-of-river designs submerge less land, but their output falls with the river in the lean season.",
  "चारों कथन सही हैं। 2019 तक केवल लघु जलविद्युत भारत के नवीकरणीय लक्ष्यों में गिनी जाती थी; बड़ी जलविद्युत को क्रय दायित्वों और शुल्क समर्थन के साथ नवीकरणीय घोषित करने का उद्देश्य उस स्वच्छ स्रोत में निवेश को फिर से जगाना था, जिसे सौर और पवन के संतुलन के लिए घटाया-बढ़ाया भी जा सकता है। "
  "नदी-प्रवाह डिज़ाइन कम भूमि डुबोते हैं, पर कम प्रवाह के मौसम में नदी के साथ उनका उत्पादन भी घटता है।",
  f"{MOP} (hydropower policy measures, 2019); {MNRE} (small hydro).",
  "l1-sci-small-large-hydro-renewable", craft="recall")

S(EN, "medium", "Consider the following statements about tidal energy:",
  "ज्वारीय ऊर्जा के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["A tidal power station traps sea water behind a barrage at high tide and releases it through turbines.",
   "Tides, and so tidal power, are caused mainly by the heating of the oceans by the Sun.",
   "India has a large commercial tidal power station operating in the Gulf of Kachchh."],
  ["ज्वारीय विद्युत केंद्र ज्वार के समय समुद्री जल को बैराज के पीछे रोककर टरबाइनों से छोड़ता है।",
   "ज्वार, और इसलिए ज्वारीय ऊर्जा, मुख्यतः सूर्य द्वारा महासागरों के गर्म होने से उत्पन्न होते हैं।",
   "कच्छ की खाड़ी में भारत का एक बड़ा व्यावसायिक ज्वारीय विद्युत केंद्र चल रहा है।"],
  C3, 0,
  "Only statement 1 is correct. Statement 2 is wrong: tides are caused mainly by the gravitational pull of the Moon, with the Sun's pull adding to it at spring tides, which makes tidal power highly predictable. "
  "Statement 3 is wrong: the Gulfs of Kachchh and Khambhat and the Sundarbans have the tidal ranges such projects need, but the high cost of barrages and their effect on coastal ecosystems have so far kept India from building a commercial tidal station.",
  "केवल कथन 1 सही है। कथन 2 गलत है: ज्वार मुख्यतः चंद्रमा के गुरुत्वाकर्षण से आते हैं, जिसमें बृहत् ज्वार के समय सूर्य का आकर्षण भी जुड़ता है, इसीलिए ज्वारीय ऊर्जा का पूर्वानुमान बहुत सटीक होता है। "
  "कथन 3 गलत है: कच्छ और खंभात की खाड़ियों तथा सुंदरवन में ऐसी परियोजनाओं के लायक़ ज्वारीय परास है, पर बैराजों की ऊँची लागत और तटीय पारितंत्रों पर उनके प्रभाव ने अब तक भारत को व्यावसायिक ज्वारीय केंद्र बनाने से रोका है।",
  f"{SC10} (Sources of Energy, earlier editions); {MNRE} (ocean energy).",
  "l1-sci-tidal-energy-barrage-moon", craft="precision")

S(EN, "medium", "Consider the following statements about co-firing biomass in thermal power plants:",
  "ताप विद्युत संयंत्रों में जैव-भार के सह-दहन (co-firing) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Coal-based thermal power plants are required to co-fire a small share, about 5 per cent, of biomass pellets with coal.",
   "The pellets are made mainly from agricultural residue such as paddy straw.",
   "Using crop residue this way gives farmers an alternative to burning it in the fields.",
   "SAMARTH is the national mission on the use of biomass in thermal power plants."],
  ["कोयला आधारित ताप विद्युत संयंत्रों को कोयले के साथ जैव-भार गोलियों (pellets) का एक छोटा भाग, लगभग 5 प्रतिशत, जलाना आवश्यक है।",
   "ये गोलियाँ मुख्यतः धान की पराली जैसे कृषि अवशेषों से बनती हैं।",
   "फ़सल अवशेष का ऐसा उपयोग किसानों को उसे खेतों में जलाने का विकल्प देता है।",
   "SAMARTH ताप विद्युत संयंत्रों में जैव-भार के उपयोग का राष्ट्रीय मिशन है।"],
  C4, 3,
  "All four statements are correct. The policy, issued by the Ministry of Power in 2021, replaces a little coal with a renewable fuel without building new plants, and creates a market for straw that would otherwise be burnt in north-west India after the paddy harvest, worsening winter air pollution. "
  "Collecting, storing and pelletising bulky straw cheaply enough remains the main practical challenge.",
  "चारों कथन सही हैं। विद्युत मंत्रालय की 2021 की नीति नए संयंत्र बनाए बिना थोड़े कोयले की जगह नवीकरणीय ईंधन लाती है, और उस पराली के लिए बाज़ार बनाती है जो अन्यथा धान की कटाई के बाद उत्तर-पश्चिम भारत में जलाई जाती और सर्दियों का वायु प्रदूषण बढ़ाती। "
  "भारी पराली को पर्याप्त सस्ते में इकट्ठा करना, रखना और गोलियाँ बनाना मुख्य व्यावहारिक चुनौती बनी हुई है।",
  f"{MOP} (policy on biomass co-firing, 2021; SAMARTH mission).",
  "l1-sci-biomass-cofiring-samarth", craft="linkage")

S(EN, "medium", "Consider the following statements about kinetic energy and road safety:",
  "गतिज ऊर्जा और सड़क सुरक्षा के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The kinetic energy of a moving vehicle is proportional to the square of its speed.",
   "For the same braking force, doubling a vehicle's speed roughly quadruples the distance it needs to stop.",
   "Halving a vehicle's speed halves its kinetic energy."],
  ["चलते वाहन की गतिज ऊर्जा उसकी गति के वर्ग के अनुपाती होती है।",
   "समान ब्रेकिंग बल पर, वाहन की गति दोगुनी करने से रुकने के लिए आवश्यक दूरी मोटे तौर पर चार गुना हो जाती है।",
   "वाहन की गति आधी करने से उसकी गतिज ऊर्जा आधी हो जाती है।"],
  C3, 1,
  "Statements 1 and 2 are correct: kinetic energy is half the mass times the speed squared, and the brakes must remove all of it, doing work equal to force times distance -- so four times the energy needs four times the distance. "
  "Statement 3 is wrong: halving the speed cuts the kinetic energy to one-fourth, which is why lower speed limits near schools and in crowded streets reduce the damage in a collision so sharply.",
  "कथन 1 और 2 सही हैं: गतिज ऊर्जा द्रव्यमान और गति के वर्ग के गुणनफल की आधी है, और ब्रेकों को यह सारी ऊर्जा हटानी होती है, बल और दूरी के गुणनफल के बराबर कार्य करके -- इसलिए चार गुनी ऊर्जा के लिए चार गुनी दूरी चाहिए। "
  "कथन 3 गलत है: गति आधी करने से गतिज ऊर्जा एक-चौथाई रह जाती है, इसीलिए स्कूलों के पास और भीड़ भरी सड़कों पर कम गति-सीमा टक्कर में क्षति को इतना अधिक घटाती है।",
  f"{SC9} (Work and Energy).",
  "l1-sci-kinetic-energy-braking-distance", craft="application")

S(EN, "medium", "Consider the following statements about thermal power stations:",
  "ताप विद्युत केंद्रों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Thermal power stations need large quantities of water to cool and condense the steam, so they are built near rivers, reservoirs or the sea.",
   "In a thermal power station, high-pressure steam turns a turbine, which drives the generator.",
   "The white plumes rising from the cooling towers of a power station are smoke from burning coal."],
  ["ताप विद्युत केंद्रों को भाप को ठंडा और संघनित करने के लिए बहुत पानी चाहिए, इसलिए वे नदियों, जलाशयों या समुद्र के पास बनाए जाते हैं।",
   "ताप विद्युत केंद्र में उच्च दाब की भाप टरबाइन घुमाती है, जो जनित्र चलाती है।",
   "विद्युत केंद्र की शीतलन मीनारों (cooling towers) से उठने वाले सफ़ेद गुबार कोयला जलने का धुआँ हैं।"],
  C3, 1,
  "Statements 1 and 2 are correct. Statement 3 is wrong: the plumes from cooling towers are water vapour condensing into droplets as the warm, moist air rises -- the smoke from burning coal leaves through the tall chimney after passing through dust-removal equipment. "
  "Water scarcity during droughts has forced some Indian coal plants to shut down for days, which is why plants increasingly use treated sewage water and dry cooling.",
  "कथन 1 और 2 सही हैं। कथन 3 गलत है: शीतलन मीनारों से उठने वाले गुबार जलवाष्प हैं, जो ऊपर उठती गर्म, नम वायु के साथ बूँदों में संघनित होती है -- कोयला जलने का धुआँ धूल हटाने वाले उपकरणों से गुज़रकर ऊँची चिमनी से निकलता है। "
  "सूखे के समय पानी की कमी ने कुछ भारतीय कोयला संयंत्रों को कई दिनों तक बंद करवाया है, इसीलिए संयंत्र बढ़ती मात्रा में उपचारित सीवेज जल और शुष्क शीतलन का उपयोग करते हैं।",
  f"{SC10} (Sources of Energy, earlier editions); {MOP}.",
  "l1-sci-thermal-plant-cooling-towers", craft="inference")

# ---------------------------------------------------------------- medium Statement-I/II (1)
A(EN, "medium",
  "Electricity is transmitted over long distances at very high voltages.",
  "बिजली को लंबी दूरियों तक बहुत ऊँचे वोल्टेज पर संचरित किया जाता है।",
  "For the same power, a higher voltage means a smaller current, and the heat lost in the wires depends on the square of the current.",
  "समान शक्ति के लिए ऊँचे वोल्टेज का अर्थ है कम धारा, और तारों में नष्ट होने वाली ऊष्मा धारा के वर्ग पर निर्भर करती है।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I. Since power equals voltage times current, raising the voltage ten times cuts the current to a tenth and the heating loss in the line to a hundredth; transformers step the voltage up at the power station and down again near consumers. "
  "This is a main reason alternating current won out for public supply: its voltage is easily changed with transformers.",
  "दोनों कथन सही हैं, और कथन-II कथन-I की व्याख्या करता है। चूँकि शक्ति वोल्टेज और धारा का गुणनफल है, वोल्टेज दस गुना बढ़ाने से धारा दसवाँ भाग और लाइन में ताप हानि सौवाँ भाग रह जाती है; ट्रांसफ़ॉर्मर विद्युत केंद्र पर वोल्टेज बढ़ाते और उपभोक्ताओं के पास फिर घटाते हैं। "
  "सार्वजनिक आपूर्ति के लिए प्रत्यावर्ती धारा के अपनाए जाने का यह एक मुख्य कारण है: ट्रांसफ़ॉर्मरों से इसका वोल्टेज आसानी से बदला जा सकता है।",
  f"NCERT Class XII, Physics (Alternating Current); {SC10} (Electricity).",
  "l1-sci-high-voltage-transmission", craft="inference")

# ---------------------------------------------------------------- hard MCQ (1)
M(EN, "hard", "A litre of diesel releases about 36 megajoules of energy when burnt. A diesel generator converts 35 per cent of this into electricity. Since 1 kWh equals 3.6 megajoules, one litre gives about",
  "एक लीटर डीज़ल जलने पर लगभग 36 मेगाजूल ऊर्जा देता है। एक डीज़ल जनित्र इसका 35 प्रतिशत बिजली में बदलता है। चूँकि 1 kWh 3.6 मेगाजूल के बराबर है, एक लीटर से लगभग कितनी बिजली मिलती है?",
  ["3.5 kWh", "12.6 kWh", "10 kWh", "1.26 kWh"],
  ["3.5 kWh", "12.6 kWh", "10 kWh", "1.26 kWh"],
  0,
  "Useful energy = 36 x 0.35 = 12.6 megajoules; dividing by 3.6 megajoules per kWh gives 3.5 kWh. Forgetting to convert gives 12.6, and ignoring the efficiency gives 10 kWh. "
  "The other 65 per cent leaves as heat in the exhaust and the cooling system -- a reminder that converting fuel into electricity is inherently wasteful, which is why the efficiency of power plants and engines matters so much.",
  "उपयोगी ऊर्जा = 36 x 0.35 = 12.6 मेगाजूल; इसे 3.6 मेगाजूल प्रति kWh से भाग देने पर 3.5 kWh मिलता है। इकाई न बदलने पर 12.6, और दक्षता छोड़ देने पर 10 kWh आता है। "
  "शेष 65 प्रतिशत निकास और शीतलन प्रणाली में ऊष्मा के रूप में निकल जाता है -- यह याद दिलाता है कि ईंधन को बिजली में बदलना स्वभावतः अपव्ययी है, इसीलिए विद्युत संयंत्रों और इंजनों की दक्षता इतनी महत्त्वपूर्ण है।",
  f"{SC9} (Work and Energy); NCERT Class XI, Physics (Thermodynamics).",
  "l1-sci-diesel-generator-kwh", pos=3, craft="application")

# ---------------------------------------------------------------- hard statement (2)
S(EN, "hard", "Consider the following statements about nuclear reactors in India:",
  "भारत में नाभिकीय रिएक्टरों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["India's pressurised heavy water reactors use natural uranium as fuel and heavy water as both moderator and coolant.",
   "The reactors at Kudankulam are Russian-designed VVERs, which use enriched uranium and ordinary water.",
   "The job of a moderator is to absorb neutrons so that the chain reaction stops."],
  ["भारत के दाबित भारी जल रिएक्टर ईंधन के रूप में प्राकृतिक यूरेनियम और मंदक तथा शीतलक, दोनों के रूप में भारी जल का उपयोग करते हैं।",
   "कुडनकुलम के रिएक्टर रूसी डिज़ाइन के VVER हैं, जो संवर्धित यूरेनियम और साधारण जल का उपयोग करते हैं।",
   "मंदक का कार्य न्यूट्रॉनों को अवशोषित करना है ताकि शृंखला अभिक्रिया रुक जाए।"],
  C3, 1,
  "Statements 1 and 2 are correct: heavy water absorbs so few neutrons that a reactor using it can run on natural uranium, which suited India, as it lacked enrichment capacity when its programme began; ordinary water absorbs more neutrons, so light-water reactors need enriched fuel. "
  "Statement 3 is wrong: a moderator slows the fast neutrons released in fission so that they can cause further fission and keep the reaction going; it is the control rods that absorb neutrons to regulate or stop it.",
  "कथन 1 और 2 सही हैं: भारी जल इतने कम न्यूट्रॉन अवशोषित करता है कि उसका उपयोग करने वाला रिएक्टर प्राकृतिक यूरेनियम पर चल सकता है, जो भारत के अनुकूल था, क्योंकि कार्यक्रम आरंभ होने पर उसके पास संवर्धन की क्षमता नहीं थी; साधारण जल अधिक न्यूट्रॉन अवशोषित करता है, इसलिए हल्के जल वाले रिएक्टरों को संवर्धित ईंधन चाहिए। "
  "कथन 3 गलत है: मंदक विखंडन में निकले तेज़ न्यूट्रॉनों को धीमा करता है ताकि वे आगे विखंडन करके अभिक्रिया जारी रख सकें; न्यूट्रॉनों को अवशोषित करके उसे नियंत्रित करने या रोकने का काम नियंत्रक छड़ें करती हैं।",
  "Department of Atomic Energy; Nuclear Power Corporation of India Limited.",
  "l1-sci-phwr-vver-moderator", craft="precision")

S(EN, "hard", "Consider the following statements about the efficiency of thermal power generation:",
  "ताप विद्युत उत्पादन की दक्षता के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["A typical coal-fired power station converts only about a third of the energy in its fuel into electricity.",
   "Combined-cycle gas power stations reach higher efficiency by using the hot exhaust of a gas turbine to raise steam for a second turbine.",
   "Supercritical coal units improve efficiency by running at higher steam temperatures and pressures."],
  ["एक सामान्य कोयला आधारित विद्युत केंद्र अपने ईंधन की ऊर्जा का केवल लगभग एक-तिहाई भाग ही बिजली में बदलता है।",
   "संयुक्त-चक्र (combined-cycle) गैस विद्युत केंद्र गैस टरबाइन के गर्म निकास से दूसरी टरबाइन के लिए भाप बनाकर अधिक दक्षता पाते हैं।",
   "अति-क्रांतिक (supercritical) कोयला इकाइयाँ ऊँचे भाप तापमान और दाब पर चलकर दक्षता सुधारती हैं।"],
  C3, 2,
  "All three statements are correct. Most of the energy lost in a thermal station leaves as heat in the condenser cooling water and the flue gases; the hotter the steam entering the turbine, the larger the share that can be turned into work. "
  "Higher efficiency means less coal burnt and less carbon dioxide emitted for each unit of electricity, which is why India's newer coal units are supercritical or ultra-supercritical.",
  "तीनों कथन सही हैं। ताप केंद्र में नष्ट होने वाली अधिकांश ऊर्जा संघनित्र के शीतलन जल और फ़्लू गैसों में ऊष्मा के रूप में निकलती है; टरबाइन में जाने वाली भाप जितनी अधिक गर्म हो, उतना बड़ा भाग कार्य में बदला जा सकता है। "
  "अधिक दक्षता का अर्थ है बिजली की हर यूनिट के लिए कम कोयला जलाना और कम कार्बन डाइऑक्साइड उत्सर्जित करना, इसीलिए भारत की नई कोयला इकाइयाँ अति-क्रांतिक या अत्यधिक अति-क्रांतिक हैं।",
  f"{MOP}; Central Electricity Authority; NCERT Class XI, Physics (Thermodynamics).",
  "l1-sci-thermal-efficiency-supercritical", craft="linkage")

write("sci_l1_t6_c.sql")
