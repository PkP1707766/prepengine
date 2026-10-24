# -*- coding: utf-8 -*-
"""Level 3 · Test 1 (GS Integrated Test 1) -- part C: Environment & Ecology (15) (upsc_l3_cell_targets.mjs 1).
Environment cells: Flora e-MCQ, m-stmt; Fauna e-stmt, h-stmt, m-stmt; Pollution e-stmt, m-stmt; Conventions h-SI;
Laws & Bodies h-pairs; Climate Science m-MCQ, m-stmt; Protected Areas m-MCQ, m-stmt; Ecosystems m-stmt; Climate
Agreements m-stmt.
Level 2 holds 318 Environment rows and Level 1 another 136; between them they cover nearly every species, rule,
convention and protected area in the standard lists, down to the koel, the Amur falcon, khejri and the SWM Rules 2026.
Every fact here was grepped against both and is one neither tests: seabuckthorn; the dhole and the chinkara; the
bio-medical waste colour codes; the lesser florican, the white-bellied heron and the binturong; the IUCN Green Status;
which Act the pollution and waste rules are made under; Arctic amplification; Desert National Park; agarwood, guggul
and kokum; the waggle dance, firefly light and imprinting; radiative forcing; the Recycling of Ships Act and the Hong
Kong Convention; hydrothermal-vent communities; the Santiago Network, the Global Goal on Adaptation and the Mitigation
Work Programme; the Nilgiri marten and the golden mahseer. MCQ keys are pinned (pos)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, T2

d.SUBJECT = "Environment & Ecology"
d.REQUIRE_CRAFT = True
BIO12 = "NCERT Class XII, Biology (Organisms and Populations; Ecosystem; Biodiversity and Conservation)"
SCI = "NCERT Science, Classes VII-X"
MOEF = "Ministry of Environment, Forest and Climate Change"
IUCN = "IUCN Red List of Threatened Species"
UNFCCC = "UNFCCC decisions (COP25-COP28)"
IPCC = "IPCC Sixth Assessment Report (AR6), Working Group I"

# ---------------------------------------------------------------- Flora, Fungi & Forests (e-MCQ, m-stmt)
M("Flora, Fungi & Forests", "easy",
  "Which shrub of the cold deserts of Ladakh and Lahaul-Spiti, valued for its vitamin-rich berries and planted to bind loose soil, also enriches the soil with nitrogen through its root nodules?",
  "लद्दाख और लाहौल-स्पीति के ठंडे मरुस्थलों की कौन-सी झाड़ी, जो अपनी विटामिन-युक्त बेरियों के लिए मूल्यवान है और ढीली मिट्टी को बाँधने के लिए लगाई जाती है, अपनी जड़-ग्रंथियों के माध्यम से मिट्टी को नाइट्रोजन से भी समृद्ध करती है?",
  ["Deodar, the tall Himalayan cedar of the outer ranges", "Chilgoza pine, valued for its edible seeds", "Brahma Kamal, the alpine flower of the high meadows", "Seabuckthorn"],
  ["देवदार, बाहरी श्रेणियों का ऊँचा हिमालयी वृक्ष", "चिलगोज़ा चीड़, जो अपने खाद्य बीजों के लिए मूल्यवान है", "ब्रह्म कमल, ऊँचे घास के मैदानों का अल्पाइन पुष्प", "सीबकथॉर्न"],
  3,
  "Seabuckthorn (Hippophae) grows in the cold deserts of the trans-Himalaya. Its berries are rich in vitamin C, and it is planted to stabilise slopes and riverbanks; like the alder, it carries nitrogen-fixing actinomycetes (Frankia) in its root nodules, so it can grow in poor soils and improve them. "
  "Deodar and chilgoza are conifers of the Himalayan ranges without such nodules, and Brahma Kamal is an alpine herb.",
  "सीबकथॉर्न (हिप्पोफ़े) ट्रांस-हिमालय के ठंडे मरुस्थलों में उगता है। उसकी बेरियाँ विटामिन C से भरपूर होती हैं, और उसे ढलानों और नदी-तटों को स्थिर करने के लिए लगाया जाता है; एल्डर की तरह उसकी जड़-ग्रंथियों में नाइट्रोजन-स्थिरीकारक एक्टिनोमाइसीट (फ़्रैंकिया) होते हैं, इसलिए वह ख़राब मिट्टी में उगकर उसे सुधार सकता है। "
  "देवदार और चिलगोज़ा हिमालयी श्रेणियों के शंकुधारी वृक्ष हैं जिनमें ऐसी ग्रंथियाँ नहीं होतीं, और ब्रह्म कमल एक अल्पाइन शाक है।",
  f"{MOEF}; Defence Institute of High Altitude Research (DRDO) on seabuckthorn; {BIO12}.",
  "l3-t1-env-seabuckthorn-cold-desert", pos=3, craft="recall")

S("Flora, Fungi & Forests", "medium", "Consider the following statements about some plant products of India:",
  "भारत के कुछ वनस्पति उत्पादों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The fragrant resin of agarwood forms in Aquilaria trees mainly after they are wounded or infected by fungi.",
   "Guggul, a resin used in Ayurveda, comes from Commiphora wightii, a shrub of the arid regions of Rajasthan and Gujarat.",
   "Kokum, whose dried fruit rind is used as a souring agent, grows wild in the Western Ghats."],
  ["अगरवुड की सुगंधित राल अक्विलारिया वृक्षों में मुख्यतः तब बनती है जब उन्हें चोट पहुँचती है या कवक का संक्रमण होता है।",
   "आयुर्वेद में प्रयुक्त राल, गुग्गुल, राजस्थान और गुजरात के शुष्क क्षेत्रों की झाड़ी कॉमिफ़ोरा वाइटी से मिलती है।",
   "कोकम, जिसके फल का सूखा छिलका खटास के लिए प्रयोग होता है, पश्चिमी घाट में जंगली रूप में उगता है।"],
  C3, 2,
  "All three are correct. Healthy Aquilaria wood is pale and scentless; the dark, resinous agarwood (oud) forms as a defence when the tree is wounded or infected, which is why wild trees of north-east India were felled in search of it and the genus is now regulated under CITES. "
  "Guggul resin is tapped from Commiphora wightii, a thorny shrub of dry rocky land that over-tapping has made Critically Endangered. Kokum (Garcinia indica) is a tree of the Western Ghats and the Konkan; its rind sours food and its seeds yield kokum butter.",
  "तीनों सही हैं। स्वस्थ अक्विलारिया की लकड़ी हल्के रंग की और गंधहीन होती है; गहरी, राल-युक्त अगरवुड (ऊद) तब बनती है जब वृक्ष चोट या संक्रमण से अपनी रक्षा करता है, इसीलिए पूर्वोत्तर भारत के जंगली वृक्ष उसकी खोज में काटे गए और यह वंश अब CITES के अंतर्गत नियंत्रित है। "
  "गुग्गुल राल शुष्क पथरीली भूमि की एक काँटेदार झाड़ी कॉमिफ़ोरा वाइटी से निकाली जाती है, जिसे अति-दोहन ने गंभीर रूप से संकटग्रस्त बना दिया है। कोकम (गार्सिनिया इंडिका) पश्चिमी घाट और कोंकण का वृक्ष है; उसका छिलका भोजन को खट्टा करता है और बीजों से कोकम बटर मिलता है।",
  f"{IUCN} (Commiphora wightii); CITES Appendix II (Aquilaria); Botanical Survey of India.",
  "l3-t1-env-agarwood-guggul-kokum", craft="linkage")

# ---------------------------------------------------------------- Fauna & Animal Behaviour (e-stmt, h-stmt, m-stmt)
S("Fauna & Animal Behaviour", "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The dhole, or Asiatic wild dog, lives and hunts in packs and is listed as Endangered by the IUCN.",
   "The chinkara, or Indian gazelle, is found mainly in the arid and semi-arid regions of north-western and central India."],
  ["ढोल, या एशियाई जंगली कुत्ता, झुंडों में रहता और शिकार करता है और IUCN द्वारा संकटग्रस्त (Endangered) सूचीबद्ध है।",
   "चिंकारा, या भारतीय गज़ेल, मुख्यतः उत्तर-पश्चिमी और मध्य भारत के शुष्क और अर्ध-शुष्क क्षेत्रों में पाया जाता है।"],
  T2, 2,
  "Both are correct. The dhole hunts cooperatively in packs that communicate with whistling calls, and has lost most of its former range; the IUCN lists it as Endangered. "
  "The chinkara is a small gazelle of dry grassland, scrub and desert, from Rajasthan and Gujarat into the Deccan; it can go long without drinking, getting water from plants and dew, and like the blackbuck it is protected by the Bishnoi communities of the Thar.",
  "दोनों सही हैं। ढोल सीटी जैसी आवाज़ों से संवाद करने वाले झुंडों में मिलकर शिकार करता है, और अपने पूर्व क्षेत्र का अधिकांश भाग खो चुका है; IUCN उसे संकटग्रस्त सूचीबद्ध करता है। "
  "चिंकारा शुष्क घास के मैदानों, झाड़ियों और मरुस्थल का एक छोटा गज़ेल है, राजस्थान और गुजरात से दक्कन तक; वह पौधों और ओस से पानी लेकर लंबे समय तक बिना पिए रह सकता है, और काले हिरण की तरह थार के बिश्नोई समुदाय उसकी रक्षा करते हैं।",
  f"{IUCN}; Zoological Survey of India.",
  "l3-t1-env-dhole-chinkara", craft="recall")

S("Fauna & Animal Behaviour", "hard", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["During the monsoon breeding season, the male lesser florican advertises itself by leaping repeatedly above the grass.",
   "The white-bellied heron, a Critically Endangered bird, is known in India mainly from the rivers of Arunachal Pradesh, such as those of Namdapha.",
   "The binturong of north-east India's forests is a primate, closely related to the slow loris."],
  ["मानसून के प्रजनन काल में नर लेसर फ़्लोरिकन (खरमोर) घास के ऊपर बार-बार उछलकर स्वयं को प्रदर्शित करता है।",
   "गंभीर रूप से संकटग्रस्त पक्षी, सफ़ेद पेट वाला बगुला (व्हाइट-बेलीड हेरॉन), भारत में मुख्यतः अरुणाचल प्रदेश की नदियों से, जैसे नामदफा की नदियों से, ज्ञात है।",
   "पूर्वोत्तर भारत के वनों का बिंटुरॉन्ग एक प्राइमेट है, जो स्लो लोरिस से निकट से संबंधित है।"],
  C3, 1,
  "Statements 1 and 2 are correct. The male lesser florican (kharmor) leaps up to two metres above the grass, again and again, to be seen by females -- which makes it dependent on undisturbed monsoon grasslands in Gujarat, Rajasthan and Madhya Pradesh; it is now Critically Endangered. "
  "The white-bellied heron survives along a few clear rivers of the eastern Himalaya, in India chiefly in and around Namdapha. "
  "Statement 3 is wrong: the binturong, or bearcat, is a viverrid -- a relative of the civets -- not a primate, though it is arboreal and has a prehensile tail.",
  "कथन 1 और 2 सही हैं। नर लेसर फ़्लोरिकन (खरमोर) मादाओं को दिखने के लिए बार-बार घास से दो मीटर तक ऊपर उछलता है -- जिससे वह गुजरात, राजस्थान और मध्य प्रदेश के अबाधित मानसूनी घास के मैदानों पर निर्भर है; वह अब गंभीर रूप से संकटग्रस्त है। "
  "सफ़ेद पेट वाला बगुला पूर्वी हिमालय की कुछ स्वच्छ नदियों के किनारे बचा है, भारत में मुख्यतः नामदफा और उसके आसपास। "
  "कथन 3 ग़लत है: बिंटुरॉन्ग, या बेयरकैट, एक विवेरिड है -- सिवेट (कस्तूरी बिलाव) का संबंधी -- प्राइमेट नहीं, यद्यपि वह वृक्षवासी है और उसकी पूँछ परिग्राही है।",
  f"{IUCN}; Wildlife Institute of India; BirdLife International.",
  "l3-t1-env-florican-heron-binturong", craft="precision")

S("Fauna & Animal Behaviour", "medium", "Consider the following statements about animal behaviour:",
  "पशु व्यवहार के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["A honeybee's waggle dance tells other bees the direction and the distance of a source of food.",
   "The light of a firefly is produced by a chemical reaction that gives out very little heat.",
   "Imprinting, by which a young bird learns to follow its parent, can happen at any time in the bird's life."],
  ["मधुमक्खी का 'वैगल नृत्य' दूसरी मधुमक्खियों को भोजन-स्रोत की दिशा और दूरी बताता है।",
   "जुगनू का प्रकाश एक रासायनिक अभिक्रिया से उत्पन्न होता है जिसमें बहुत कम ऊष्मा निकलती है।",
   "छाप-अधिगम (इम्प्रिंटिंग), जिसके द्वारा कोई बच्चा पक्षी अपने माता-पिता के पीछे चलना सीखता है, पक्षी के जीवन में किसी भी समय हो सकता है।"],
  C3, 1,
  "Statements 1 and 2 are correct. In the waggle dance, the angle of the waggle run to the vertical shows the direction of the food relative to the sun, and its duration the distance. "
  "A firefly's light comes from the oxidation of luciferin, catalysed by the enzyme luciferase; almost all the energy appears as light, so it is called 'cold light'. "
  "Statement 3 is wrong: imprinting happens only in a short sensitive period soon after hatching -- Konrad Lorenz's goslings followed him because he was the first moving object they saw.",
  "कथन 1 और 2 सही हैं। वैगल नृत्य में वैगल-दौड़ का ऊर्ध्वाधर से कोण सूर्य के सापेक्ष भोजन की दिशा बताता है, और उसकी अवधि दूरी। "
  "जुगनू का प्रकाश ल्यूसिफ़ेरिन के ऑक्सीकरण से आता है, जिसे ल्यूसिफ़ेरेज़ एंज़ाइम उत्प्रेरित करता है; लगभग सारी ऊर्जा प्रकाश के रूप में निकलती है, इसलिए इसे 'शीतल प्रकाश' कहते हैं। "
  "कथन 3 ग़लत है: छाप-अधिगम अंडे से निकलने के कुछ ही समय बाद की एक छोटी संवेदनशील अवधि में होता है -- कोनराड लॉरेंज़ के हंस-शावक उनके पीछे इसलिए चले क्योंकि वे पहली चलती वस्तु थे जो उन्होंने देखी।",
  f"{BIO12}; {SCI}.",
  "l3-t1-env-waggle-firefly-imprinting", craft="precision")

# ---------------------------------------------------------------- Pollution, Waste & Resources (e-stmt, m-stmt)
S("Pollution, Waste & Resources", "easy", "With reference to the Bio-Medical Waste Management Rules, 2016, consider the following statements:",
  "जैव-चिकित्सा अपशिष्ट प्रबंधन नियम, 2016 के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Needles and other sharps are collected in white, translucent, puncture-proof containers.",
   "Human anatomical waste is collected in red bags so that it can be recycled."],
  ["सुइयाँ और दूसरी नुकीली वस्तुएँ सफ़ेद, पारभासी, छेद-रोधी पात्रों में एकत्र की जाती हैं।",
   "मानव शारीरिक अपशिष्ट लाल थैलों में एकत्र किया जाता है ताकि उसका पुनर्चक्रण हो सके।"],
  T2, 0,
  "Only statement 1 is correct. The Rules sort waste by colour: white translucent puncture-proof containers for sharps; yellow bags for human and animal anatomical waste, soiled dressings and expired medicines, which go for incineration or deep burial; "
  "red bags for contaminated recyclable items such as tubing, bottles and gloves, which are disinfected and recycled; and blue containers for glassware and metallic implants. Anatomical waste is never recycled, so statement 2 is wrong.",
  "केवल कथन 1 सही है। नियम अपशिष्ट को रंग से छाँटते हैं: नुकीली वस्तुओं के लिए सफ़ेद पारभासी छेद-रोधी पात्र; मानव और पशु शारीरिक अपशिष्ट, गंदी पट्टियों और समाप्त-अवधि की दवाओं के लिए पीले थैले, जो भस्मीकरण या गहरे दफ़न के लिए जाते हैं; "
  "नलियों, बोतलों और दस्तानों जैसी संदूषित पुनर्चक्रण-योग्य वस्तुओं के लिए लाल थैले, जिन्हें विसंक्रमित करके पुनर्चक्रित किया जाता है; और काँच के सामान और धातु प्रत्यारोपणों के लिए नीले पात्र। शारीरिक अपशिष्ट का कभी पुनर्चक्रण नहीं होता, इसलिए कथन 2 ग़लत है।",
  "Bio-Medical Waste Management Rules, 2016 (Schedule I); Central Pollution Control Board.",
  "l3-t1-env-biomedical-waste-colour-codes", craft="application")

S("Pollution, Waste & Resources", "medium", "Consider the following statements about the recycling of ships:",
  "जहाज़ों के पुनर्चक्रण के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["India's Recycling of Ships Act, 2019 was enacted as India acceded to the Hong Kong International Convention for the Safe and Environmentally Sound Recycling of Ships.",
   "Under the Act, a ship-recycling facility must be authorised, and a ship sent for recycling must carry an inventory of the hazardous materials on board.",
   "The Hong Kong Convention has not yet entered into force internationally."],
  ["भारत का जहाज़ पुनर्चक्रण अधिनियम, 2019 तब बनाया गया जब भारत जहाज़ों के सुरक्षित और पर्यावरण की दृष्टि से सुदृढ़ पुनर्चक्रण के लिए हांगकांग अंतरराष्ट्रीय अभिसमय में शामिल हुआ।",
   "अधिनियम के अंतर्गत जहाज़ पुनर्चक्रण सुविधा को प्राधिकृत होना चाहिए, और पुनर्चक्रण के लिए भेजे गए जहाज़ के पास उस पर मौजूद ख़तरनाक पदार्थों की सूची होनी चाहिए।",
   "हांगकांग अभिसमय अभी अंतरराष्ट्रीय स्तर पर लागू नहीं हुआ है।"],
  C3, 1,
  "Statements 1 and 2 are correct. India passed the Act in 2019 and acceded to the Convention the same year; the Act requires every recycling facility to be authorised and every ship to carry an Inventory of Hazardous Materials (asbestos, PCBs, heavy metals and the like), with the Directorate General of Shipping as the national authority. "
  "Statement 3 is wrong: the Convention entered into force on 26 June 2025. India matters here because the yards at Alang-Sosiya in Gujarat recycle a large share of the world's ships; the rules aim to move the work off bare beaches and protect workers and the coast.",
  "कथन 1 और 2 सही हैं। भारत ने 2019 में अधिनियम पारित किया और उसी वर्ष अभिसमय में शामिल हुआ; अधिनियम हर पुनर्चक्रण सुविधा का प्राधिकरण और हर जहाज़ के पास ख़तरनाक पदार्थों (एस्बेस्टस, PCB, भारी धातुएँ आदि) की सूची अनिवार्य करता है, और नौवहन महानिदेशालय राष्ट्रीय प्राधिकरण है। "
  "कथन 3 ग़लत है: अभिसमय 26 जून 2025 को लागू हो गया। भारत यहाँ महत्त्वपूर्ण है क्योंकि गुजरात में अलंग-सोसिया के यार्ड दुनिया के जहाज़ों का बड़ा हिस्सा पुनर्चक्रित करते हैं; नियमों का उद्देश्य काम को खुले तटों से हटाना और श्रमिकों व तट की रक्षा करना है।",
  "Recycling of Ships Act, 2019; International Maritime Organization (Hong Kong Convention, 2009).",
  "l3-t1-env-ship-recycling-hong-kong-convention", craft="linkage")

# ---------------------------------------------------------------- International Conventions & Organisations (h-SI)
A("International Conventions & Organisations", "hard",
  "A species assessed as Least Concern on the IUCN Red List may still be classed as 'Largely Depleted' under the IUCN Green Status of Species.",
  "IUCN रेड लिस्ट में 'कम चिंताजनक' (Least Concern) आँकी गई प्रजाति को भी IUCN ग्रीन स्टेटस ऑफ़ स्पीशीज़ में 'काफ़ी हद तक क्षीण' (Largely Depleted) वर्गीकृत किया जा सकता है।",
  "The Green Status measures a species' recovery against its historical range and its ecological role there, whereas the Red List measures its risk of extinction.",
  "ग्रीन स्टेटस किसी प्रजाति की बहाली को उसके ऐतिहासिक विस्तार-क्षेत्र और वहाँ उसकी पारिस्थितिक भूमिका के सापेक्ष मापता है, जबकि रेड लिस्ट उसके विलुप्ति के जोखिम को मापती है।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I. The Green Status, launched by the IUCN in 2021, asks how close a species is to being present and ecologically functional across all the parts of its range it once occupied, and places it on a scale from Extinct in the Wild through Critically, Largely, Moderately and Slightly Depleted to Fully Recovered. "
  "Because this is a different question from the Red List's -- how likely is extinction -- a widespread species in no danger of extinction can still have vanished from much of its old range or lost its ecological role there.",
  "दोनों कथन सही हैं, और कथन-II कथन-I की व्याख्या करता है। IUCN द्वारा 2021 में शुरू किया गया ग्रीन स्टेटस यह पूछता है कि कोई प्रजाति अपने उन सभी क्षेत्रों में, जहाँ वह कभी थी, उपस्थित और पारिस्थितिक रूप से क्रियाशील होने के कितने निकट है, और उसे 'वन्य में विलुप्त' से लेकर गंभीर रूप से, काफ़ी हद तक, मध्यम रूप से और थोड़ा क्षीण होते हुए 'पूर्णतः बहाल' तक के पैमाने पर रखता है। "
  "चूँकि यह रेड लिस्ट के प्रश्न -- विलुप्ति कितनी संभावित है -- से अलग प्रश्न है, विलुप्ति के किसी ख़तरे में न होने वाली व्यापक प्रजाति भी अपने पुराने क्षेत्र के बड़े भाग से ग़ायब हो सकती है या वहाँ अपनी पारिस्थितिक भूमिका खो सकती है।",
  "IUCN Green Status of Species (2021); " + IUCN + ".",
  "l3-t1-env-iucn-green-status", craft="inference")

# ---------------------------------------------------------------- Indian Environmental Laws & Bodies (h-pairs)
P("Indian Environmental Laws & Bodies", "hard", "Consider the following pairs of Rules and the Acts under which they have been made:",
  "नियमों और उन अधिनियमों के निम्नलिखित युग्मों पर विचार कीजिए जिनके अंतर्गत वे बनाए गए हैं:",
  ["Noise Pollution (Regulation and Control) Rules, 2000 : Air (Prevention and Control of Pollution) Act, 1981",
   "Ozone Depleting Substances (Regulation and Control) Rules, 2000 : Environment (Protection) Act, 1986",
   "Bio-Medical Waste Management Rules, 2016 : Environment (Protection) Act, 1986",
   "Hazardous and Other Wastes (Management and Transboundary Movement) Rules, 2016 : Water (Prevention and Control of Pollution) Act, 1974"],
  ["ध्वनि प्रदूषण (विनियमन और नियंत्रण) नियम, 2000 : वायु (प्रदूषण निवारण एवं नियंत्रण) अधिनियम, 1981",
   "ओज़ोन क्षयकारी पदार्थ (विनियमन और नियंत्रण) नियम, 2000 : पर्यावरण (संरक्षण) अधिनियम, 1986",
   "जैव-चिकित्सा अपशिष्ट प्रबंधन नियम, 2016 : पर्यावरण (संरक्षण) अधिनियम, 1986",
   "ख़तरनाक और अन्य अपशिष्ट (प्रबंधन और सीमा-पार संचलन) नियम, 2016 : जल (प्रदूषण निवारण एवं नियंत्रण) अधिनियम, 1974"],
  1,
  "Only the second and third pairs are correct. All four sets of Rules were made under the Environment (Protection) Act, 1986, the umbrella law that lets the Union regulate any environmental pollutant. "
  "The trap in the first pair is that noise was added to the definition of 'air pollutant' in the Air Act in 1987 -- but the Noise Rules of 2000 were nonetheless framed under the 1986 Act; and the hazardous-waste rules have nothing to do with the Water Act.",
  "केवल दूसरा और तीसरा युग्म सही है। चारों नियम पर्यावरण (संरक्षण) अधिनियम, 1986 के अंतर्गत बनाए गए हैं, जो एक व्यापक क़ानून है और संघ को किसी भी पर्यावरणीय प्रदूषक का विनियमन करने देता है। "
  "पहले युग्म का जाल यह है कि 1987 में वायु अधिनियम में 'वायु प्रदूषक' की परिभाषा में शोर जोड़ा गया था -- फिर भी 2000 के ध्वनि नियम 1986 के अधिनियम के अंतर्गत बनाए गए; और ख़तरनाक अपशिष्ट नियमों का जल अधिनियम से कोई संबंध नहीं।",
  f"{MOEF}: notifications under the Environment (Protection) Act, 1986; Air (Prevention and Control of Pollution) Act, 1981, s.2(a).",
  "l3-t1-env-rules-and-parent-acts", craft="precision")

# ---------------------------------------------------------------- Climate Science & Mitigation (m-MCQ, m-stmt)
M("Climate Science & Mitigation", "medium",
  "Ice cores drilled from the Antarctic and Greenland ice sheets are especially valuable to climate scientists mainly because:",
  "अंटार्कटिक और ग्रीनलैंड की हिम-चादरों से निकाले गए बर्फ़ के कोर (आइस कोर) जलवायु वैज्ञानिकों के लिए विशेष रूप से मूल्यवान क्यों हैं?",
  ["they hold microbes from past ages whose decay rates are used to date volcanic eruptions on other continents",
   "they record the eleven-year sunspot cycle through changes in the thickness of each winter's snow layer",
   "bubbles in them preserve samples of past air, showing greenhouse-gas levels over many millennia",
   "their temperature at depth shows directly how warm the oceans were at each period of the past"],
  ["उनमें पिछले युगों के सूक्ष्मजीव होते हैं जिनकी क्षय-दर से दूसरे महाद्वीपों के ज्वालामुखी विस्फोटों की तिथि तय होती है",
   "वे हर सर्दी की हिम-परत की मोटाई में परिवर्तन के माध्यम से ग्यारह-वर्षीय सौर-कलंक चक्र को दर्ज करते हैं",
   "उनके बुलबुलों में पिछली हवा के नमूने बचे रहते हैं, जो हज़ारों वर्षों के ग्रीनहाउस-गैस स्तर दिखाते हैं",
   "गहराई पर उनका तापमान सीधे बताता है कि अतीत के हर काल में महासागर कितने गर्म थे"],
  2,
  "As snow piles up and is compressed into ice, it seals in small pockets of the atmosphere of the time, so analysing the bubbles gives carbon dioxide and methane levels going back about 800,000 years in Antarctic cores; the ratio of oxygen or hydrogen isotopes in the ice itself shows past temperatures, and layers of ash and dust mark eruptions and dry, windy periods. "
  "These records show that carbon dioxide and temperature rose and fell together through the ice-age cycles, and that today's level -- above 420 parts per million -- is far higher than anything in that span, which is why ice cores are central evidence in assessments of human-caused warming.",
  "जब बर्फ़ जमा होकर दबती हुई हिम बनती है, तो वह उस समय के वायुमंडल की छोटी जेबों को बंद कर लेती है, इसलिए बुलबुलों के विश्लेषण से अंटार्कटिक कोरों में लगभग 8,00,000 वर्ष पीछे तक के कार्बन डाइऑक्साइड और मीथेन स्तर मिलते हैं; स्वयं बर्फ़ में ऑक्सीजन या हाइड्रोजन समस्थानिकों का अनुपात पिछले तापमान बताता है, और राख तथा धूल की परतें विस्फोटों और शुष्क, आँधी वाले कालों को चिह्नित करती हैं। "
  "ये अभिलेख दिखाते हैं कि हिमयुग-चक्रों में कार्बन डाइऑक्साइड और तापमान साथ-साथ चढ़ते-उतरते रहे, और आज का स्तर -- 420 भाग प्रति दस लाख से ऊपर -- उस पूरी अवधि के किसी भी स्तर से कहीं ऊँचा है, इसीलिए मानव-जनित तापन के आकलनों में आइस कोर केंद्रीय साक्ष्य हैं।",
  IPCC + " (paleoclimate assessment); National Centre for Polar and Ocean Research.",
  "l3-t1-env-ice-cores-past-air", pos=2, craft="inference")

S("Climate Science & Mitigation", "medium", "Consider the following statements about radiative forcing:",
  "विकिरणी प्रणोदन (रेडिएटिव फ़ोर्सिंग) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is the change, caused by a factor such as a greenhouse gas or an aerosol, in the balance between the energy that reaches the Earth and the energy that leaves it.",
   "Among the gases emitted by human activity, methane today exerts a larger total radiative forcing than carbon dioxide."],
  ["यह किसी ग्रीनहाउस गैस या एरोसॉल जैसे कारक से पृथ्वी तक पहुँचने वाली और उससे निकलने वाली ऊर्जा के संतुलन में होने वाला परिवर्तन है।",
   "मानव गतिविधियों से उत्सर्जित गैसों में आज मीथेन का कुल विकिरणी प्रणोदन कार्बन डाइऑक्साइड से अधिक है।"],
  T2, 0,
  "Only statement 1 is correct. Radiative forcing, measured in watts per square metre, is the imbalance a factor creates in the Earth's energy budget: positive forcing (greenhouse gases) warms, negative forcing (such as sulphate aerosols, which reflect sunlight) cools. "
  "Statement 2 is wrong: methane is far more potent per molecule, but carbon dioxide, emitted in vastly larger amounts and lasting longer, accounts for the largest share of human-caused forcing; the IPCC puts methane's contribution at roughly a quarter of carbon dioxide's.",
  "केवल कथन 1 सही है। विकिरणी प्रणोदन, जो वाट प्रति वर्ग मीटर में मापा जाता है, वह असंतुलन है जो कोई कारक पृथ्वी के ऊर्जा बजट में पैदा करता है: धनात्मक प्रणोदन (ग्रीनहाउस गैसें) गर्म करता है, ऋणात्मक प्रणोदन (जैसे सल्फ़ेट एरोसॉल, जो धूप परावर्तित करते हैं) ठंडा करता है। "
  "कथन 2 ग़लत है: मीथेन प्रति अणु कहीं अधिक प्रबल है, पर कार्बन डाइऑक्साइड, जो कहीं अधिक मात्रा में उत्सर्जित होती है और अधिक समय तक रहती है, मानव-जनित प्रणोदन का सबसे बड़ा भाग है; IPCC मीथेन के योगदान को कार्बन डाइऑक्साइड के लगभग एक-चौथाई के बराबर आँकता है।",
  IPCC + " (Chapter 7, the Earth's energy budget).",
  "l3-t1-env-radiative-forcing", craft="precision")

# ---------------------------------------------------------------- Protected Areas & Wildlife Protection (m-MCQ, m-stmt)
M("Protected Areas & Wildlife Protection", "medium",
  "Desert National Park, which protects one of the last strongholds of the Great Indian Bustard, lies in which districts?",
  "डेज़र्ट नेशनल पार्क, जो ग्रेट इंडियन बस्टर्ड के अंतिम गढ़ों में से एक की रक्षा करता है, किन ज़िलों में स्थित है?",
  ["Bikaner and Churu in north-western Rajasthan", "Kachchh and Banaskantha in Gujarat", "Jodhpur and Nagaur in central Rajasthan", "Jaisalmer and Barmer in western Rajasthan"],
  ["उत्तर-पश्चिमी राजस्थान के बीकानेर और चूरू", "गुजरात के कच्छ और बनासकांठा", "मध्य राजस्थान के जोधपुर और नागौर", "पश्चिमी राजस्थान के जैसलमेर और बाड़मेर"],
  3,
  "Desert National Park spreads over about 3,160 sq km of the Thar in the Jaisalmer and Barmer districts of western Rajasthan, with sand dunes, rocky ground and grassland. "
  "Most of the world's remaining Great Indian Bustards live in and around it, which is why its grassland enclosures and the captive-breeding centres nearby matter so much.",
  "डेज़र्ट नेशनल पार्क पश्चिमी राजस्थान के जैसलमेर और बाड़मेर ज़िलों में थार के लगभग 3,160 वर्ग किमी में फैला है, जिसमें रेत के टीले, पथरीली भूमि और घास के मैदान हैं। "
  "विश्व के बचे हुए अधिकांश ग्रेट इंडियन बस्टर्ड इसके भीतर और आसपास रहते हैं, इसीलिए इसके घास के मैदानों वाले बाड़े और पास के बंदी-प्रजनन केंद्र इतने महत्त्वपूर्ण हैं।",
  f"{MOEF}; Rajasthan Forest Department; Wildlife Institute of India.",
  "l3-t1-env-desert-national-park", pos=3, craft="recall")

S("Protected Areas & Wildlife Protection", "medium", "With reference to the conservation of two Indian species, consider the following statements:",
  "दो भारतीय प्रजातियों के संरक्षण के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Nilgiri marten is found in the oak and conifer forests of the western Himalaya.",
   "The golden mahseer is a marine fish of the Arabian Sea coast, threatened mainly by trawling."],
  ["नीलगिरि मार्टन पश्चिमी हिमालय के बांज और शंकुधारी वनों में पाया जाता है।",
   "गोल्डन महसीर अरब सागर तट की एक समुद्री मछली है, जिसे मुख्यतः ट्रॉलिंग से ख़तरा है।"],
  T2, 3,
  "Neither statement is correct. The Nilgiri marten is the only marten of peninsular India and is endemic to the Western Ghats, living in their montane and evergreen forests far from the Himalaya. "
  "The golden mahseer (Tor putitora) is a large freshwater fish of Himalayan rivers and their foothills, listed as Endangered; dams that block its spawning migrations, overfishing and sand mining are its main threats, and temple pools and catch-and-release angling have helped to protect it.",
  "कोई भी कथन सही नहीं है। नीलगिरि मार्टन प्रायद्वीपीय भारत का एकमात्र मार्टन है और पश्चिमी घाट का स्थानिक है, जो हिमालय से दूर उनके पर्वतीय और सदाबहार वनों में रहता है। "
  "गोल्डन महसीर (टोर पुटिटोरा) हिमालयी नदियों और उनकी तलहटी की एक बड़ी मीठे पानी की मछली है, जो संकटग्रस्त सूचीबद्ध है; उसकी अंडे देने की प्रवास-यात्राएँ रोकने वाले बाँध, अति-मत्स्यन और रेत खनन उसके मुख्य ख़तरे हैं, और मंदिरों के तालाबों तथा पकड़कर छोड़ने वाले मत्स्य-आखेट ने उसकी रक्षा में सहायता की है।",
  f"{IUCN}; Zoological Survey of India.",
  "l3-t1-env-nilgiri-marten-golden-mahseer", craft="recall")

# ---------------------------------------------------------------- Ecosystems & Ecological Processes (m-stmt)
S("Ecosystems & Ecological Processes", "medium", "Consider the following statements about the communities around deep-sea hydrothermal vents:",
  "गहरे समुद्र के जलतापीय छिद्रों (हाइड्रोथर्मल वेंट) के आसपास के समुदायों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Their food webs rest on bacteria that make food by chemosynthesis, using energy from chemicals such as hydrogen sulphide rather than from sunlight.",
   "Giant tube worms living at some vents have no mouth or gut and depend on bacteria living inside their bodies."],
  ["उनके खाद्य-जाल ऐसे जीवाणुओं पर टिके हैं जो सूर्य के प्रकाश के बजाय हाइड्रोजन सल्फ़ाइड जैसे रसायनों की ऊर्जा से रसायनसंश्लेषण द्वारा भोजन बनाते हैं।",
   "कुछ छिद्रों पर रहने वाले विशाल ट्यूब वर्म्स का न मुँह होता है न आँत, और वे अपने शरीर के भीतर रहने वाले जीवाणुओं पर निर्भर रहते हैं।"],
  T2, 2,
  "Both are correct. In the dark of the deep sea, chemosynthetic bacteria oxidise hydrogen sulphide and other chemicals in the vent fluids to fix carbon, so these are among the few ecosystems whose primary producers do not depend on the Sun. "
  "The giant tube worm Riftia lacks a mouth and gut; its red plume takes up oxygen and hydrogen sulphide, which its blood carries to symbiotic bacteria packed in an organ called the trophosome. Such vents occur in all the major oceans, including the Indian Ocean.",
  "दोनों सही हैं। गहरे समुद्र के अँधेरे में रसायनसंश्लेषी जीवाणु छिद्र-द्रवों के हाइड्रोजन सल्फ़ाइड और अन्य रसायनों का ऑक्सीकरण करके कार्बन स्थिर करते हैं, इसलिए ये उन थोड़े पारितंत्रों में से हैं जिनके प्राथमिक उत्पादक सूर्य पर निर्भर नहीं। "
  "विशाल ट्यूब वर्म रिफ़्टिया का न मुँह होता है न आँत; उसका लाल गुच्छा ऑक्सीजन और हाइड्रोजन सल्फ़ाइड लेता है, जिन्हें उसका रक्त ट्रोफ़ोसोम नामक अंग में भरे सहजीवी जीवाणुओं तक ले जाता है। ऐसे छिद्र हिंद महासागर सहित सभी प्रमुख महासागरों में मिलते हैं।",
  f"{BIO12}; Ministry of Earth Sciences (Deep Ocean Mission).",
  "l3-t1-env-hydrothermal-vent-chemosynthesis", craft="inference")

# ---------------------------------------------------------------- Climate Agreements & Carbon Markets (m-stmt)
S("Climate Agreements & Carbon Markets", "medium", "Consider the following statements about arrangements under the UNFCCC and the Paris Agreement:",
  "UNFCCC और पेरिस समझौते के अंतर्गत व्यवस्थाओं के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Santiago Network connects developing countries with technical assistance to avert, minimise and address loss and damage.",
   "The UAE Framework for Global Climate Resilience, adopted at COP28, sets targets under the Global Goal on Adaptation established by the Paris Agreement.",
   "The Mitigation Work Programme is to be carried out in a non-prescriptive, non-punitive manner, without imposing new targets on countries."],
  ["सैंटियागो नेटवर्क विकासशील देशों को हानि और क्षति (लॉस एंड डैमेज) से बचने, उसे कम करने और उससे निपटने के लिए तकनीकी सहायता से जोड़ता है।",
   "COP28 में अपनाया गया वैश्विक जलवायु लचीलेपन के लिए UAE ढाँचा पेरिस समझौते द्वारा स्थापित अनुकूलन पर वैश्विक लक्ष्य के अंतर्गत लक्ष्य तय करता है।",
   "शमन कार्य कार्यक्रम (मिटिगेशन वर्क प्रोग्राम) देशों पर नए लक्ष्य थोपे बिना, ग़ैर-निर्देशात्मक और ग़ैर-दंडात्मक तरीक़े से चलाया जाना है।"],
  C3, 2,
  "All three are correct. The Santiago Network was set up in 2019 under the Warsaw International Mechanism to catalyse technical help on loss and damage, and its working arrangements were settled at COP27 and COP28. "
  "Article 7.1 of the Paris Agreement established the Global Goal on Adaptation; COP28 in Dubai gave it content through the UAE Framework, with targets on water, food, health, ecosystems, infrastructure and more. "
  "The Mitigation Work Programme, set up at COP26 and launched at COP27, is meant to scale up mitigation this decade through dialogues and exchange, and its mandate says expressly that it will not impose new targets or goals.",
  "तीनों सही हैं। सैंटियागो नेटवर्क 2019 में वारसॉ अंतरराष्ट्रीय तंत्र के अंतर्गत हानि और क्षति पर तकनीकी सहायता उपलब्ध कराने के लिए बनाया गया, और उसकी कार्य-व्यवस्था COP27 और COP28 में तय हुई। "
  "पेरिस समझौते के अनुच्छेद 7.1 ने अनुकूलन पर वैश्विक लक्ष्य स्थापित किया; दुबई में COP28 ने UAE ढाँचे के माध्यम से उसे ठोस रूप दिया, जिसमें जल, भोजन, स्वास्थ्य, पारितंत्र, अवसंरचना आदि पर लक्ष्य हैं। "
  "COP26 में बना और COP27 में आरंभ हुआ शमन कार्य कार्यक्रम संवादों और आदान-प्रदान के माध्यम से इस दशक में शमन बढ़ाने के लिए है, और उसका अधिदेश स्पष्ट कहता है कि वह नए लक्ष्य या उद्देश्य नहीं थोपेगा।",
  UNFCCC + "; Paris Agreement, Article 7.",
  "l3-t1-env-santiago-gga-mwp", craft="precision")

write("gs_l3_t1_c.sql")
