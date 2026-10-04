# -*- coding: utf-8 -*-
"""Level 2 · Test 19 (Science & Technology 1) -- depth audit of 2026-10-05, part B: Chemistry & Materials and
Physics & Everyday Science, plus the tags for the 63 kept rows (Test 21's 5 are tagged already). Part A is
upg_l2_t19_st_a.py.

Part B rewrites 18 recall rows in place with the same concept id, type and difficulty:
  - cases: a solar street light's energy chain, a nitinol stent, a nail under oil in boiled water, a candle
    under a jar, lightning 3 seconds before thunder, a dentist's mirror, a spoon in hot tea, a ship, a
    control tower and a speed gun choosing radar, lidar or sonar, a phone in a woollen glove;
  - mechanisms: why milk of magnesia relieves acidity, why cakes rise, why leaked LPG hugs the floor, why
    aerogels insulate, why PTFE is non-stick, why gold stays bright, why MRI magnets are superconducting;
  - precision: a catalyst does not shift equilibrium, and sodium-ion cells store less energy per kilogram.
One kept row is retagged: bi-nobel-medicine-recent turns on the prize category the stem sets ('in this
category'; CRISPR won the Chemistry prize), so it is precision, not recall.
Leaks avoided while drafting:
  - graphite's free electrons (answer the diamond AR's statement I), so the allotropes row was left;
  - acids turning blue litmus red in the lemon row (the litmus row's statement 1);
  - an aluminium oxide layer among the PTFE options (the aluminium AR)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write_updates, CODE
from polity_common import C3, C4, T2

d.SUBJECT = "Science & Technology"
d.REQUIRE_CRAFT = True
CH = "Chemistry & Materials"
PH = "Physics & Everyday Science"
NC10 = "NCERT Class X Science"

# ================================================================ MCQs, chemistry (6)
M(CH, "easy", "Milk of magnesia relieves acidity in the stomach because it:",
  "मिल्क ऑफ़ मैग्नीशिया पेट की अम्लता से राहत देता है क्योंकि यह:",
  ["is a mild base that neutralises the excess acid",
   "is an acid that speeds up the digestion of food",
   "kills the bacteria that make acid in the stomach",
   "coats the stomach lining with a layer of oil"],
  ["एक हल्का क्षार है जो अतिरिक्त अम्ल को उदासीन करता है",
   "एक अम्ल है जो भोजन के पाचन को तेज़ करता है",
   "पेट में अम्ल बनाने वाले जीवाणुओं को मारता है",
   "पेट की भीतरी परत पर तेल की एक परत चढ़ा देता है"],
  0,
  "Milk of magnesia is a suspension of magnesium hydroxide, a mild base; it reacts with the excess hydrochloric acid in the stomach to form a salt and water, relieving the burning. Strong bases would harm the stomach, so only mild ones are used as antacids.",
  "मिल्क ऑफ़ मैग्नीशिया मैग्नीशियम हाइड्रॉक्साइड का निलंबन है, जो एक हल्का क्षार है; यह पेट के अतिरिक्त हाइड्रोक्लोरिक अम्ल से क्रिया करके लवण और पानी बनाता है, जिससे जलन शांत होती है। प्रबल क्षार पेट को हानि पहुँचाएँगे, इसलिए प्रति-अम्ल के रूप में केवल हल्के क्षार उपयोग किए जाते हैं।",
  NC10 + " (Acids, Bases and Salts).", "ch-antacid-easy", craft="linkage")

M(CH, "easy", "A cake rises when baked with baking soda or baking powder mainly because:",
  "बेकिंग सोडा या बेकिंग पाउडर के साथ पकाने पर केक इसलिए फूलता है क्योंकि मुख्यतः:",
  ["carbon dioxide is given off and forms bubbles in the dough",
   "oxygen is given off as the soda burns in the heat of the oven",
   "the soda absorbs water and makes the dough swell",
   "the heat turns the starch in the flour into air"],
  ["कार्बन डाइऑक्साइड निकलती है और गुँधे आटे में बुलबुले बनाती है",
   "ओवन की गर्मी में सोडा के जलने से ऑक्सीजन निकलती है",
   "सोडा पानी सोखकर आटे को फुला देता है",
   "गर्मी आटे के स्टार्च को हवा में बदल देती है"],
  0,
  "Sodium hydrogen carbonate gives off carbon dioxide when heated or when it meets an acid -- baking powder contains a mild acid such as tartaric acid for this -- and the gas, trapped as bubbles, puffs up the dough, which sets around them as it bakes. "
  "The same reaction makes vinegar and baking soda fizz, and is used in some fire extinguishers.",
  "सोडियम हाइड्रोजन कार्बोनेट गर्म करने पर या किसी अम्ल से मिलने पर कार्बन डाइऑक्साइड छोड़ता है, बेकिंग पाउडर में इसके लिए टार्टरिक अम्ल जैसा हल्का अम्ल होता है, और बुलबुलों के रूप में फँसी गैस आटे को फुला देती है, जो पकते समय उनके चारों ओर जम जाता है। "
  "यही अभिक्रिया सिरके और बेकिंग सोडा में झाग लाती है, और कुछ अग्निशामकों में प्रयुक्त होती है।",
  NC10 + " (Acids, Bases and Salts).", "ch-baking-soda-vinegar-easy", craft="linkage")

M(CH, "hard", "Polytetrafluoroethylene (PTFE), used as the non-stick coating on pans, is slippery and resists attack by almost all chemicals mainly because:",
  "पैन पर नॉन-स्टिक परत के रूप में प्रयुक्त पॉलीटेट्राफ़्लोरोएथिलीन (PTFE) फिसलन भरा है और लगभग सभी रसायनों से अप्रभावित रहता है, मुख्यतः इसलिए कि:",
  ["its carbon-fluorine bonds are among the strongest in chemistry",
   "it is made of silicon atoms linked to oxygen, just as glass is",
   "it is a metal that is coated with a thin film of oil in the factory",
   "its molecules are short, so they slide easily past one another"],
  ["इसके कार्बन-फ़्लोरीन बंध रसायन विज्ञान के सबसे प्रबल बंधों में हैं",
   "यह काँच की तरह ऑक्सीजन से जुड़े सिलिकॉन परमाणुओं से बना है",
   "यह एक धातु है जिस पर कारख़ाने में तेल की पतली परत चढ़ाई जाती है",
   "इसके अणु छोटे हैं, इसलिए वे एक-दूसरे पर आसानी से फिसलते हैं"],
  0,
  "In PTFE -- Teflon -- a backbone of carbon atoms is sheathed in fluorine atoms. Carbon-fluorine bonds are exceptionally strong and the fluorine sheath holds other molecules only weakly, so food does not stick and acids, alkalis and solvents leave it alone. PTFE's molecules are in fact very long chains. "
  "The same stability makes the wider family of fluorinated chemicals, PFAS, the 'forever chemicals' that persist in the environment; PFOA, once used to make PTFE, has been phased out.",
  "PTFE, यानी टेफ़्लॉन, में कार्बन परमाणुओं की एक रीढ़ फ़्लोरीन परमाणुओं से ढकी होती है। कार्बन-फ़्लोरीन बंध असाधारण रूप से प्रबल हैं और फ़्लोरीन का आवरण अन्य अणुओं को केवल दुर्बलता से पकड़ता है, इसलिए भोजन चिपकता नहीं और अम्ल, क्षार तथा विलायक उस पर असर नहीं करते। PTFE के अणु वास्तव में बहुत लंबी शृंखलाएँ हैं। "
  "यही स्थिरता फ़्लोरीनयुक्त रसायनों के बड़े परिवार PFAS को पर्यावरण में टिके रहने वाले 'चिरस्थायी रसायन' बनाती है; PTFE बनाने में कभी प्रयुक्त PFOA को चरणबद्ध रूप से हटा दिया गया है।",
  "NCERT Class XII Chemistry (Polymers); US Environmental Protection Agency -- PFAS.", "ch-non-stick-ptfe", craft="linkage")

M(CH, "medium", "Aerogels are used to insulate spacesuits and pipelines mainly because:",
  "एयरोजेल का उपयोग अंतरिक्ष सूट और पाइपलाइनों के ऊष्मारोधन में मुख्यतः इसलिए होता है क्योंकि:",
  ["gas trapped in their tiny pores makes them conduct very little heat",
   "they reflect almost all of the heat that falls on them, like a mirror",
   "they are made of metal, which spreads heat away evenly",
   "they absorb heat and release it slowly at night like a store"],
  ["उनके सूक्ष्म छिद्रों में फँसी गैस उन्हें बहुत कम ऊष्मा का चालक बनाती है",
   "वे दर्पण की तरह अपने पर पड़ने वाली लगभग सारी ऊष्मा परावर्तित कर देते हैं",
   "वे धातु के बने हैं, जो ऊष्मा को समान रूप से फैला देती है",
   "वे भंडार की तरह ऊष्मा सोखकर रात में धीरे-धीरे छोड़ते हैं"],
  0,
  "An aerogel is a gel whose liquid has been replaced by gas so gently that the solid network survives, leaving a material that can be over 95 per cent air. Heat must pass through a sparse, tangled solid and through pores too small for air to circulate, so conduction and convection are both tiny -- making aerogels among the best insulators known. "
  "Silica aerogels are glassy, not metallic, and were used on NASA's Stardust probe to catch comet dust.",
  "एयरोजेल वह जेल है जिसका द्रव इतनी सावधानी से गैस से बदला गया हो कि ठोस जाल बचा रहे, जिससे 95 प्रतिशत से अधिक हवा वाला पदार्थ बनता है। ऊष्मा को एक विरल, उलझे ठोस और इतने छोटे छिद्रों से गुज़रना पड़ता है कि उनमें हवा घूम न सके, इसलिए चालन और संवहन दोनों बहुत कम होते हैं; यही एयरोजेल को सबसे अच्छे ज्ञात ऊष्मारोधियों में रखता है। "
  "सिलिका एयरोजेल काँच जैसे हैं, धात्विक नहीं, और NASA के स्टारडस्ट यान पर धूमकेतु की धूल पकड़ने में इनका उपयोग हुआ।",
  "NASA -- aerogel research and the Stardust mission.", "ch-aerogels", craft="linkage")

M(CH, "medium", "Leaked LPG tends to collect near the floor of a closed kitchen rather than near the ceiling. This is because:",
  "रिसी हुई LPG बंद रसोई में छत के बजाय फ़र्श के पास जमा होती है। ऐसा इसलिए है क्योंकि:",
  ["LPG is heavier than air",
   "the odorant added to LPG is heavier than air, though the gas itself is lighter",
   "the floor is cooler, so the gas condenses back into a liquid there",
   "LPG reacts with the oxygen in the air to form a heavy gas"],
  ["LPG हवा से भारी है",
   "LPG में मिलाया गया गंधक-यौगिक हवा से भारी है, यद्यपि गैस स्वयं हल्की है",
   "फ़र्श ठंडा है, इसलिए गैस वहाँ फिर से द्रव में संघनित हो जाती है",
   "LPG हवा की ऑक्सीजन से क्रिया करके एक भारी गैस बनाती है"],
  0,
  "LPG is mainly propane and butane, both denser than air, so a leak spreads along the floor and can pool in low places -- which is why windows and doors should be opened and no switch or flame used. Piped natural gas, mostly methane, is lighter than air and rises instead. "
  "Both gases have almost no smell of their own, so a strong-smelling sulphur compound, ethyl mercaptan, is added in tiny amounts to warn of a leak.",
  "LPG मुख्यतः प्रोपेन और ब्यूटेन है, दोनों हवा से घनी, इसलिए रिसाव फ़र्श पर फैलता है और निचली जगहों में जमा हो सकता है; इसीलिए खिड़कियाँ-दरवाज़े खोलने चाहिए और कोई स्विच या लौ नहीं जलानी चाहिए। पाइप से आने वाली प्राकृतिक गैस, अधिकतर मीथेन, हवा से हल्की है और ऊपर उठती है। "
  "दोनों गैसों की अपनी लगभग कोई गंध नहीं होती, इसलिए रिसाव की चेतावनी के लिए तीखी गंध वाला गंधक-यौगिक एथिल मर्कैप्टन बहुत कम मात्रा में मिलाया जाता है।",
  "Petroleum and Natural Gas Regulatory Board; Ministry of Petroleum and Natural Gas -- LPG safety.", "ch-lpg-odorant", craft="linkage")

M(CH, "medium", "A stent made of nitinol is pushed into a blocked artery in a compressed form and then opens out inside it. The property of nitinol that allows this is that it:",
  "नाइटिनॉल से बना स्टेंट अवरुद्ध धमनी में दबे रूप में डाला जाता है और फिर उसके भीतर खुल जाता है। नाइटिनॉल का कौन-सा गुण इसे संभव बनाता है?",
  ["returns to a set shape when warmed to body temperature",
   "conducts electricity without any resistance in the body",
   "dissolves slowly in blood after it has opened the artery",
   "is strongly magnetic, so a magnet outside can open it"],
  ["शरीर के तापमान तक गर्म होने पर यह एक निर्धारित आकार में लौट आता है",
   "शरीर में बिना किसी प्रतिरोध के विद्युत का चालन करता है",
   "धमनी खोलने के बाद रक्त में धीरे-धीरे घुल जाता है",
   "यह प्रबल चुंबकीय है, इसलिए बाहर का चुंबक इसे खोल सकता है"],
  0,
  "Nitinol, an alloy of nickel and titanium, is a shape-memory alloy: it changes its crystal structure with temperature, so a piece deformed when cool 'remembers' and springs back to its set shape when warmed. Stents, orthodontic wires and spectacle frames use this, along with its springiness. "
  "It is not a superconductor, is designed not to dissolve, and is only weakly magnetic.",
  "निकल और टाइटेनियम की मिश्रधातु नाइटिनॉल एक आकार-स्मृति मिश्रधातु है: तापमान के साथ इसकी क्रिस्टल संरचना बदलती है, इसलिए ठंडे में मोड़ा गया टुकड़ा गर्म होने पर अपना निर्धारित आकार 'याद' करके लौट आता है। स्टेंट, दाँतों के तार और चश्मे के फ़्रेम इसका और इसके लचीलेपन का उपयोग करते हैं। "
  "यह अतिचालक नहीं है, घुलने के लिए नहीं बनाया जाता, और केवल दुर्बल रूप से चुंबकीय है।",
  "NCERT Class XII Physics (Magnetism and Matter); Indian Council of Medical Research -- medical devices.", "ch-shape-memory-alloys", craft="application")

# ================================================================ MCQ, physics (1)
M(PH, "easy", "A street light runs at night on a battery that is charged during the day by a solar panel. The energy changes taking place are:",
  "एक सड़क-बत्ती रात में एक बैटरी से चलती है जो दिन में सौर पैनल से चार्ज होती है। होने वाले ऊर्जा परिवर्तन हैं:",
  ["light to electrical to chemical by day; chemical to electrical to light at night",
   "heat to light to electrical by day; electrical to heat and then to light at night",
   "electrical to light by day; light to chemical to electrical at night",
   "chemical to light by day; light to electrical at night"],
  ["दिन में प्रकाश से विद्युत और विद्युत से रासायनिक; रात में रासायनिक से विद्युत और विद्युत से प्रकाश",
   "दिन में ऊष्मा से प्रकाश और प्रकाश से विद्युत; रात में विद्युत से ऊष्मा और फिर प्रकाश",
   "दिन में विद्युत से प्रकाश; रात में प्रकाश से रासायनिक और रासायनिक से विद्युत",
   "दिन में रासायनिक से प्रकाश; रात में प्रकाश से विद्युत"],
  0,
  "The solar panel turns sunlight directly into electricity through the photovoltaic effect in a semiconductor, and charging the battery stores that energy in chemical form. At night the battery's chemical energy is turned back into electricity, which the lamp converts into light.",
  "सौर पैनल अर्धचालक में प्रकाश-वोल्टीय प्रभाव से सूर्य के प्रकाश को सीधे विद्युत में बदलता है, और बैटरी चार्ज करने से वह ऊर्जा रासायनिक रूप में संचित होती है। रात में बैटरी की रासायनिक ऊर्जा फिर से विद्युत में बदलती है, जिसे लैंप प्रकाश में बदलता है।",
  NC10 + " (Sources of Energy).", "ph-solar-cell-easy", craft="application")

# ================================================================ two-statement rows, chemistry (3)
S(CH, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Gold keeps its shine for centuries because it hardly reacts with air or water.",
   "Lemon juice is basic."],
  ["सोना सदियों तक अपनी चमक बनाए रखता है क्योंकि वह हवा या पानी से लगभग क्रिया नहीं करता।",
   "नींबू का रस क्षारीय है।"],
  T2, 0,
  "Only statement 1 is correct. Gold is one of the least reactive metals, so it does not form an oxide or other dull coating, which is one reason it has been prized for jewellery, coins and electrical contacts. Statement 2 is wrong: lemon juice is acidic, because of citric acid.",
  "केवल कथन 1 सही है। सोना सबसे कम अभिक्रियाशील धातुओं में है, इसलिए उस पर ऑक्साइड या कोई और धुँधली परत नहीं बनती; यही एक कारण है कि आभूषणों, सिक्कों और विद्युत संपर्कों के लिए उसे मूल्यवान माना गया है। कथन 2 गलत है: साइट्रिक अम्ल के कारण नींबू का रस अम्लीय है।",
  NC10 + " (Metals and Non-metals).", "ch-lemon-gold-easy", craft="linkage")

S(CH, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["An iron nail kept in boiled water under a layer of oil will rust quickly, since water alone is enough for rusting.",
   "Common salt is sodium chloride."],
  ["उबले पानी में तेल की परत के नीचे रखी लोहे की कील जल्दी जंग खा जाएगी, क्योंकि जंग लगने के लिए केवल पानी पर्याप्त है।",
   "साधारण नमक सोडियम क्लोराइड है।"],
  T2, 1,
  "Only statement 2 is correct. Rusting needs both oxygen and water: boiling drives out the dissolved air and the oil stops more from dissolving, so the nail stays bright -- the classic textbook experiment. A nail in dry air with a drying agent stays bright too; only one exposed to both air and water rusts.",
  "केवल कथन 2 सही है। जंग लगने के लिए ऑक्सीजन और पानी दोनों चाहिए: उबालने से घुली हवा निकल जाती है और तेल और हवा को घुलने से रोकता है, इसलिए कील चमकती रहती है; यह पाठ्यपुस्तक का प्रसिद्ध प्रयोग है। शुष्कक के साथ शुष्क हवा में रखी कील भी चमकती रहती है; केवल हवा और पानी दोनों के संपर्क वाली कील पर जंग लगती है।",
  "NCERT Class VII Science (Physical and Chemical Changes).", "ch-rusting-salt-easy", craft="application")

S(CH, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Since passing electricity through water splits it into hydrogen and oxygen, water is a compound and not an element.",
   "A burning candle covered with a glass jar goes out after a while because the oxygen inside is used up."],
  ["चूँकि पानी में विद्युत प्रवाहित करने पर वह हाइड्रोजन और ऑक्सीजन में टूट जाता है, इसलिए पानी एक यौगिक है, तत्व नहीं।",
   "काँच के जार से ढकी जलती मोमबत्ती कुछ देर बाद बुझ जाती है क्योंकि भीतर की ऑक्सीजन ख़र्च हो जाती है।"],
  T2, 2,
  "Both statements are correct. An element cannot be broken into simpler substances by chemical means, but electrolysis splits water into two volumes of hydrogen for every volume of oxygen, so water is a compound of the two. Burning needs oxygen; once the candle has used up most of the oxygen in the jar, the flame dies.",
  "दोनों कथन सही हैं। तत्व को रासायनिक साधनों से सरल पदार्थों में नहीं तोड़ा जा सकता, पर विद्युत-अपघटन पानी को ऑक्सीजन के हर एक आयतन के लिए हाइड्रोजन के दो आयतनों में तोड़ देता है, इसलिए पानी इन दोनों का यौगिक है। जलने के लिए ऑक्सीजन चाहिए; जार की अधिकांश ऑक्सीजन ख़र्च होते ही लौ बुझ जाती है।",
  "NCERT Class VIII Science (Combustion and Flame); NCERT Class IX Science.", "ch-water-oxygen-easy", craft="inference")

# ================================================================ two-statement rows, physics (3)
S(PH, "easy", "During a storm, a flash of lightning is seen 3 seconds before its thunder is heard. Consider the following statements:",
  "आँधी के दौरान बिजली की चमक उसकी गड़गड़ाहट सुनाई देने से 3 सेकंड पहले दिखती है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The lightning struck about 3 km away.",
   "The flash is seen almost at once because light travels far faster than sound."],
  ["बिजली लगभग 3 किमी दूर गिरी।",
   "चमक लगभग तुरंत दिखती है क्योंकि प्रकाश ध्वनि से कहीं तेज़ चलता है।"],
  T2, 1,
  "Only statement 2 is correct. Light, at about 3 lakh km per second, arrives almost instantly, while sound travels at about 340 m per second in air; in 3 seconds sound covers about 1 km, so the strike was about a kilometre away -- roughly 3 seconds for every kilometre. Statement 1 is the slip of reading seconds as kilometres.",
  "केवल कथन 2 सही है। लगभग 3 लाख किमी प्रति सेकंड वाला प्रकाश लगभग तुरंत पहुँचता है, जबकि ध्वनि हवा में लगभग 340 मीटर प्रति सेकंड चलती है; 3 सेकंड में ध्वनि लगभग 1 किमी तय करती है, इसलिए बिजली लगभग एक किलोमीटर दूर गिरी, यानी हर किलोमीटर के लिए लगभग 3 सेकंड। कथन 1 सेकंडों को किलोमीटर पढ़ लेने की चूक है।",
  "NCERT Class IX Science (Sound).", "ph-sound-light-easy", craft="application")

S(PH, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["A dentist uses a convex mirror to see an enlarged image of a tooth.",
   "Mirrors form images by refracting light."],
  ["दंत चिकित्सक दाँत का बड़ा प्रतिबिंब देखने के लिए उत्तल दर्पण का उपयोग करता है।",
   "दर्पण प्रकाश का अपवर्तन करके प्रतिबिंब बनाते हैं।"],
  T2, 3,
  "Neither statement is correct. A concave mirror held close to an object gives an enlarged, upright image, which is why dentists and shaving mirrors use one; a convex mirror always gives a smaller image but a wider view, which suits the rear-view mirrors of vehicles. Statement 2 is wrong: mirrors form images by reflecting light; lenses work by refraction.",
  "दोनों में से कोई कथन सही नहीं है। वस्तु के पास रखा अवतल दर्पण बड़ा, सीधा प्रतिबिंब देता है, इसीलिए दंत चिकित्सक और दाढ़ी बनाने के दर्पण उसका उपयोग करते हैं; उत्तल दर्पण सदा छोटा प्रतिबिंब पर अधिक चौड़ा दृश्य देता है, जो वाहनों के पीछे देखने वाले दर्पणों के लिए उपयुक्त है। कथन 2 गलत है: दर्पण प्रकाश के परावर्तन से प्रतिबिंब बनाते हैं; लेंस अपवर्तन से काम करते हैं।",
  NC10 + " (Light: Reflection and Refraction).", "ph-lens-mirror-easy", craft="application")

S(PH, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["A steel spoon left in hot tea gets hot at the handle sooner than a wooden one, because metals conduct heat well.",
   "A refrigerator moves heat from its cold inside to the warmer room without using any energy."],
  ["गर्म चाय में छोड़ी गई स्टील की चम्मच का हत्था लकड़ी की चम्मच से पहले गर्म हो जाता है, क्योंकि धातुएँ ऊष्मा की अच्छी चालक हैं।",
   "रेफ़्रिजरेटर बिना कोई ऊर्जा लिए अपने ठंडे भीतरी भाग से ऊष्मा को अधिक गर्म कमरे में पहुँचाता है।"],
  T2, 0,
  "Only statement 1 is correct: metals carry heat quickly, which is why cooking pots are made of metal and their handles of wood or plastic. Statement 2 is wrong: heat flows by itself only from hot to cold; a refrigerator can move it the other way only by doing work, which is why it runs on electricity and its back grows warm.",
  "केवल कथन 1 सही है: धातुएँ ऊष्मा को जल्दी ले जाती हैं, इसीलिए खाना पकाने के बर्तन धातु के और उनके हत्थे लकड़ी या प्लास्टिक के बनते हैं। कथन 2 गलत है: ऊष्मा अपने आप केवल गर्म से ठंडे की ओर बहती है; रेफ़्रिजरेटर उसे उलटी दिशा में केवल कार्य करके ले जा सकता है, इसीलिए वह बिजली से चलता है और उसका पिछला भाग गर्म होता है।",
  "NCERT Class VII Science (Heat).", "ph-heat-flow-metals-easy", craft="application")

# ================================================================ three- and four-statement rows (5)
S(CH, "hard", "Consider the following statements about catalysts:",
  "उत्प्रेरकों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["A catalyst speeds up a reaction without being used up in it.",
   "In a reversible reaction, a catalyst increases the amount of product present once equilibrium is reached.",
   "Enzymes are catalysts made of carbohydrates."],
  ["उत्प्रेरक किसी अभिक्रिया को स्वयं ख़र्च हुए बिना तेज़ करता है।",
   "उत्क्रमणीय अभिक्रिया में उत्प्रेरक साम्यावस्था आने पर मौजूद उत्पाद की मात्रा बढ़ा देता है।",
   "एंज़ाइम कार्बोहाइड्रेट से बने उत्प्रेरक हैं।"],
  C3, 0,
  "Only statement 1 is correct: a catalyst offers a route with a lower energy barrier. Statement 2 is the near-miss: by speeding up the forward and backward reactions alike, a catalyst helps a reaction reach equilibrium sooner but does not shift it -- which is why the Haber process for ammonia relies on pressure and temperature, not on its iron catalyst, to set the yield. "
  "Statement 3 is wrong: almost all enzymes are proteins, which is why most stop working when heated well above body temperature.",
  "केवल कथन 1 सही है: उत्प्रेरक कम ऊर्जा-बाधा वाला मार्ग देता है। कथन 2 निकट-भ्रम है: अग्र और पश्च अभिक्रियाओं को समान रूप से तेज़ करके उत्प्रेरक अभिक्रिया को जल्दी साम्यावस्था तक पहुँचाता है पर उसे खिसकाता नहीं; इसीलिए अमोनिया की हेबर प्रक्रिया उपज तय करने के लिए अपने लौह उत्प्रेरक पर नहीं, दाब और तापमान पर निर्भर है। "
  "कथन 3 गलत है: लगभग सभी एंज़ाइम प्रोटीन हैं, इसीलिए अधिकांश शरीर के तापमान से काफ़ी अधिक गर्म करने पर काम करना बंद कर देते हैं।",
  "NCERT Class XI Chemistry (Equilibrium); NCERT Class XII Chemistry (Surface Chemistry).", "ch-catalysts-enzymes", craft="precision")

S(CH, "medium", "Consider the following statements about batteries:",
  "बैटरियों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["In a lithium-ion battery, lithium ions move between the electrodes as it charges and discharges.",
   "Sodium-ion batteries store more energy per kilogram than lithium-ion batteries.",
   "Solid-state batteries use a liquid electrolyte.",
   "Lithium-ion batteries can catch fire if damaged, because their electrolyte is flammable."],
  ["लिथियम-आयन बैटरी में चार्ज और डिस्चार्ज होते समय लिथियम आयन इलेक्ट्रोडों के बीच चलते हैं।",
   "सोडियम-आयन बैटरियाँ प्रति किलोग्राम लिथियम-आयन बैटरियों से अधिक ऊर्जा संचित करती हैं।",
   "ठोस-अवस्था बैटरियाँ द्रव विद्युत-अपघट्य का उपयोग करती हैं।",
   "क्षतिग्रस्त होने पर लिथियम-आयन बैटरियों में आग लग सकती है, क्योंकि उनका विद्युत-अपघट्य ज्वलनशील है।"],
  C4, 1,
  "Statements 1 and 4 are correct: the ions shuttle into the graphite anode on charging and back to the metal-oxide cathode in use, and the organic liquid electrolyte is why a punctured or overheated cell can burst into flame. "
  "Statement 2 is the near-miss: sodium is far more abundant and cheaper than lithium, but its ions are heavier and larger, so sodium-ion cells store less energy per kilogram -- they suit grid storage and low-cost vehicles rather than phones. Statement 3 is wrong: solid-state batteries replace the liquid with a solid electrolyte, which is safer and may store more energy.",
  "कथन 1 और 4 सही हैं: चार्ज होते समय आयन ग्रेफ़ाइट ऐनोड में और उपयोग के समय धातु-ऑक्साइड कैथोड में लौटते हैं, और जैविक द्रव विद्युत-अपघट्य ही कारण है कि छिदा या अधिक गर्म हुआ सेल आग पकड़ सकता है। "
  "कथन 2 निकट-भ्रम है: सोडियम लिथियम से कहीं अधिक प्रचुर और सस्ता है, पर उसके आयन भारी और बड़े हैं, इसलिए सोडियम-आयन सेल प्रति किलोग्राम कम ऊर्जा संचित करते हैं; वे फ़ोनों के बजाय ग्रिड भंडारण और कम लागत वाले वाहनों के लिए उपयुक्त हैं। कथन 3 गलत है: ठोस-अवस्था बैटरियाँ द्रव के स्थान पर ठोस विद्युत-अपघट्य का उपयोग करती हैं, जो अधिक सुरक्षित है और अधिक ऊर्जा संचित कर सकता है।",
  "NCERT Class XII Chemistry (Electrochemistry); Department of Science and Technology.", "ch-battery-chemistry", craft="precision")

S(PH, "hard", "Consider the following statements about superconductivity:",
  "अतिचालकता के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["MRI scanners use superconducting magnets because, with zero resistance, very large currents can flow in their coils without wasting energy as heat.",
   "A material that is superconducting at room temperature and ordinary pressure has been confirmed.",
   "Superconductors conduct well only at very high temperatures."],
  ["MRI स्कैनर अतिचालक चुंबकों का उपयोग करते हैं क्योंकि शून्य प्रतिरोध होने से उनकी कुंडलियों में बहुत बड़ी धाराएँ ऊष्मा के रूप में ऊर्जा व्यर्थ किए बिना बह सकती हैं।",
   "कमरे के तापमान और सामान्य दाब पर अतिचालक कोई पदार्थ पुष्ट हो चुका है।",
   "अतिचालक केवल बहुत ऊँचे तापमानों पर अच्छा चालन करते हैं।"],
  C3, 0,
  "Only statement 1 is correct. Below its critical temperature a superconductor carries current without loss, so the coils of an MRI magnet, cooled by liquid helium, can carry huge currents and make strong, steady fields; particle accelerators and some maglev trains use the same principle. "
  "Statement 2 is wrong: claims such as LK-99 in 2023 were not confirmed. Statement 3 is wrong: superconductivity appears only when a material is cooled below a critical temperature -- for most materials far below zero degrees Celsius.",
  "केवल कथन 1 सही है। अपने क्रांतिक तापमान से नीचे अतिचालक बिना हानि के धारा ले जाता है, इसलिए द्रव हीलियम से ठंडी की गई MRI चुंबक की कुंडलियाँ विशाल धाराएँ ले जाकर प्रबल, स्थिर क्षेत्र बना सकती हैं; कण त्वरक और कुछ मैग्लेव रेलें इसी सिद्धांत का उपयोग करती हैं। "
  "कथन 2 गलत है: 2023 में LK-99 जैसे दावे पुष्ट नहीं हुए। कथन 3 गलत है: अतिचालकता तभी प्रकट होती है जब पदार्थ को एक क्रांतिक तापमान से नीचे ठंडा किया जाए, अधिकांश पदार्थों के लिए शून्य डिग्री सेल्सियस से बहुत नीचे।",
  "NCERT Class XII Physics; Department of Science and Technology.", "ph-superconductivity", craft="linkage")

S(PH, "medium", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["A ship maps the depth of the sea floor with sonar, since sound travels well through water while radio waves and light are quickly absorbed.",
   "Air traffic control tracks aircraft hundreds of kilometres away with lidar.",
   "Traffic police measure the speeds of vehicles with sonar guns."],
  ["जहाज़ सोनार से समुद्र तल की गहराई का मानचित्र बनाता है, क्योंकि ध्वनि पानी में अच्छी तरह चलती है जबकि रेडियो तरंगें और प्रकाश जल्दी अवशोषित हो जाते हैं।",
   "वायु यातायात नियंत्रण सैकड़ों किलोमीटर दूर के विमानों को लिडार से ट्रैक करता है।",
   "यातायात पुलिस वाहनों की गति सोनार गन से मापती है।"],
  C3, 0,
  "Only statement 1 is correct. All three systems send out a signal and time its echo. Radio waves travel far through air, cloud and rain, so radar tracks aircraft and weather; laser light gives very precise distances over shorter ranges, so lidar maps terrain and helps self-driving cars see; and sound, which travels well in water, is used by sonar. "
  "Police speed guns use radar or laser (lidar), measuring the shift or timing of the reflected signal -- not sound.",
  "केवल कथन 1 सही है। तीनों प्रणालियाँ एक संकेत भेजकर उसकी प्रतिध्वनि का समय मापती हैं। रेडियो तरंगें हवा, बादल और वर्षा में दूर तक जाती हैं, इसलिए रडार विमानों और मौसम पर नज़र रखता है; लेज़र प्रकाश कम दूरी पर बहुत सटीक दूरी देता है, इसलिए लिडार भूभाग का मानचित्र बनाता है और स्वचालित कारों को देखने में मदद करता है; और पानी में अच्छी तरह चलने वाली ध्वनि का उपयोग सोनार करता है। "
  "पुलिस की गति-गन रडार या लेज़र (लिडार) का उपयोग करती हैं, जो परावर्तित संकेत का विचलन या समय मापती हैं, ध्वनि नहीं।",
  "NCERT Class IX Science (Sound); Indian Space Research Organisation; India Meteorological Department.", "ph-radar-lidar-sonar", craft="application")

S(PH, "medium", "Consider the following statements about a smartphone:",
  "स्मार्टफ़ोन के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Its capacitive touchscreen does not respond to a finger in an ordinary woollen glove, because the glove does not conduct electricity.",
   "When it is turned sideways, its accelerometer senses the change in the direction of gravity, so the screen rotates.",
   "Its compass app finds north from the GPS receiver even when the phone is held still."],
  ["इसकी धारितीय टचस्क्रीन साधारण ऊनी दस्ताने में ढकी उँगली पर प्रतिक्रिया नहीं देती, क्योंकि दस्ताना विद्युत का चालन नहीं करता।",
   "इसे तिरछा घुमाने पर इसका त्वरणमापी गुरुत्व की दिशा में बदलाव भाँप लेता है, इसलिए स्क्रीन घूम जाती है।",
   "इसका कंपास ऐप फ़ोन को स्थिर पकड़े रहने पर भी GPS रिसीवर से उत्तर दिशा ज्ञात करता है।"],
  C3, 1,
  "Statements 1 and 2 are correct. The body conducts electricity, so a bare finger disturbs the screen's electric field; wool does not, which is why special gloves have conductive fingertips. The accelerometer senses which way gravity pulls. "
  "Statement 3 is wrong: a stationary GPS receiver knows where it is but not which way it is facing; the compass uses a magnetometer, which senses the Earth's magnetic field.",
  "कथन 1 और 2 सही हैं। शरीर विद्युत का चालन करता है, इसलिए नंगी उँगली स्क्रीन के विद्युत क्षेत्र को बदल देती है; ऊन ऐसा नहीं करती, इसीलिए विशेष दस्तानों की उँगलियों के सिरे चालक होते हैं। त्वरणमापी भाँपता है कि गुरुत्व किस ओर खींच रहा है। "
  "कथन 3 गलत है: स्थिर GPS रिसीवर जानता है कि वह कहाँ है पर यह नहीं कि उसका मुख किस ओर है; कंपास एक चुंबकत्वमापी का उपयोग करता है, जो पृथ्वी का चुंबकीय क्षेत्र भाँपता है।",
  "Ministry of Electronics and Information Technology; NCERT Class XII Physics.", "ph-smartphone-sensors", craft="application")

# ================================================================ TAGS for the 63 kept rows (Test 21's 5 are tagged already)
TAGS = {
 "as-moon-phases-easy": "linkage", "as-iss-free-fall": "linkage", "as-moon-tidal-locking": "linkage",
 "as-red-planet-easy": "recall", "as-parsec-numerical": "application", "as-moon-earth-easy": "recall",
 "as-sun-jupiter-easy": "recall", "as-chandrasekhar-neutron-stars": "precision", "as-neutrinos-frbs": "recall",
 "as-sidereal-perihelion-seasons-none": "precision", "as-bharatfs-deep-ocean": "recall", "as-earth-rotation-moon-recession": "recall",
 "as-gravitational-waves": "recall", "as-magnetic-field-none": "precision", "as-planets-venus-mercury": "precision",
 "as-space-weather": "recall", "as-sun-life-cycle": "recall",
 "bi-amr-natural-selection": "linkage", "bi-heart-easy": "recall", "bi-herd-immunity-threshold": "application",
 "bi-universal-donor": "linkage", "bi-vaccines-malaria-easy": "recall", "bi-xenotransplant-organ-chip-prions": "recall",
 "bi-antimicrobial-resistance": "recall", "bi-crispr-car-t": "recall", "bi-genomics-none": "precision",
 "bi-monoclonal-antibodies": "recall", "bi-mrna-vaccines": "recall", "bi-nobel-medicine-recent": "precision",
 "ch-sea-rusting-easy": "linkage", "ch-stainless-steel-chromium": "linkage", "ch-aluminium-oxide-layer": "linkage",
 "ch-diamond-hard-insulator": "linkage", "ch-control-rods": "precision", "ch-litmus-vinegar-easy": "recall",
 "ch-isotopes-dating": "precision", "ch-perovskites-quantum-dots": "recall", "ch-ph-scale-none": "inference",
 "ch-bioplastics": "precision", "ch-bpa-phthalates": "recall", "ch-carbon-allotropes": "recall",
 "ch-carbon-materials": "recall", "ch-coal-gasification": "recall", "ch-common-chemicals": "precision",
 "ch-element-properties": "precision", "ch-food-chemistry-none": "precision", "ch-hard-water-none": "precision",
 "ch-hydrogels": "recall", "ch-metals-corrosion": "precision", "ch-nobel-chemistry-recent": "recall",
 "ph-aircraft-altitude": "linkage", "ph-lift-apparent-weight": "linkage", "ph-mass-weight-moon": "application",
 "ph-doppler-effect": "application", "ph-noise-cancelling": "linkage", "ph-twinkling-stars": "linkage",
 "ph-quantum-principles": "recall", "ph-boiling-pressure-cooker": "linkage", "ph-gps-clocks-none": "precision",
 "ph-heat-transfer-everyday": "linkage", "ph-led-sodium-lamps": "recall", "ph-microwave-induction": "linkage",
 "ph-nobel-physics-recent": "recall"}

if __name__ == "__main__":
    write_updates("upg_l2_t19_st_b.sql", statuses=("draft", "published"), tags=TAGS)
