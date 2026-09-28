# -*- coding: utf-8 -*-
"""Level 2 · Test 9 (Environment 1: Ecology & Biodiversity) -- Ecosystems & Ecological
Processes, 13 new bilingual rows against the live gap report: medium statement 4, easy
statement 2, hard statement 2, easy MCQ 2, medium MCQ 1, hard MCQ 1, medium pairs 1.
Concepts already in the bank (succession, seres, ecology-term pairs incl. niche, productivity,
ecotone/keystone, nutrient cycles, Gause, pyramids, rainforest soils, energy flow, blue carbon)
are not repeated."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, write
from polity_common import C3, C4, T2

d.SUBJECT = "Environment & Ecology"
E = "Ecosystems & Ecological Processes"
POP12 = "NCERT Class XII, Biology -- Organisms and Populations"
ECO12 = "NCERT Class XII, Biology -- Ecosystem"
BIOD12 = "NCERT Class XII, Biology -- Biodiversity and Conservation"

# ---------------------------------------------------------------- medium statements (4)
S(E, "medium", "Consider the following statements about the latitudinal gradient in species diversity:",
  "जाति-विविधता की अक्षांशीय प्रवणता (latitudinal gradient) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["In general, species diversity decreases from the equator towards the poles.",
   "One explanation offered is that the tropics have had a long, relatively undisturbed evolutionary history.",
   "Another explanation offered is that tropical environments are more seasonal than temperate ones."],
  ["सामान्यतः जाति-विविधता भूमध्य रेखा से ध्रुवों की ओर घटती है।",
   "इसकी एक व्याख्या यह दी जाती है कि उष्णकटिबंधीय क्षेत्रों का विकासीय इतिहास लंबा और अपेक्षाकृत अबाधित रहा है।",
   "दूसरी व्याख्या यह दी जाती है कि उष्णकटिबंधीय पर्यावरण शीतोष्ण पर्यावरण की तुलना में अधिक ऋतुनिष्ठ (seasonal) हैं।"],
  C3, 1,
  "Statements 1 and 2 are correct. Colombia, near the equator, has around 1,400 bird species against about 105 in New York and 56 in Greenland. "
  "Ecologists offer three main explanations: the tropics escaped the repeated glaciations of higher latitudes, giving species a long time to diversify; they receive more solar energy, so productivity is higher; and -- the opposite of statement 3 -- tropical environments are less seasonal, more constant and more predictable, which allows more species to specialise into narrow niches.",
  "कथन 1 और 2 सही हैं। भूमध्य रेखा के पास कोलंबिया में पक्षियों की लगभग 1,400 प्रजातियाँ हैं, जबकि न्यूयॉर्क में लगभग 105 और ग्रीनलैंड में 56। "
  "पारिस्थितिकीविद तीन मुख्य व्याख्याएँ देते हैं: उष्णकटिबंधीय क्षेत्र ऊँचे अक्षांशों के बार-बार के हिमनदन से बचे रहे, जिससे प्रजातियों को विविध होने के लिए लंबा समय मिला; उन्हें अधिक सौर ऊर्जा मिलती है, इसलिए उत्पादकता अधिक है; और, कथन 3 के ठीक उलट, उष्णकटिबंधीय पर्यावरण कम ऋतुनिष्ठ, अधिक स्थिर और अधिक पूर्वानुमेय हैं, जिससे अधिक प्रजातियाँ संकरे निकेतों में विशेषीकृत हो पाती हैं।",
  f"{BIOD12} (patterns of biodiversity: latitudinal gradients).",
  "env-latitudinal-diversity-gradient")

S(E, "medium", "Consider the following statements about age pyramids of populations:",
  "जनसंख्या के आयु पिरामिडों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["A pyramid with a broad base shows a population that is growing.",
   "A bell-shaped pyramid shows a population that is stable.",
   "An urn-shaped pyramid, narrower at the base than in the middle, shows a population that is declining."],
  ["चौड़े आधार वाला पिरामिड बढ़ती हुई जनसंख्या दर्शाता है।",
   "घंटी के आकार का पिरामिड स्थिर जनसंख्या दर्शाता है।",
   "कलश के आकार का पिरामिड, जिसका आधार बीच के भाग से संकरा होता है, घटती हुई जनसंख्या दर्शाता है।"],
  C3, 2,
  "All three statements are correct. An age pyramid shows the numbers in the pre-reproductive, reproductive and post-reproductive age groups. A broad base means many young individuals who will soon reproduce, so the population expands. "
  "In a bell shape the young are about as many as those in the reproductive group, so numbers hold steady; in an urn shape there are fewer young than adults, so the population will shrink -- the pattern of several ageing societies such as Japan.",
  "तीनों कथन सही हैं। आयु पिरामिड प्रजनन-पूर्व, प्रजननशील और प्रजनन-पश्च आयु वर्गों की संख्या दिखाता है। चौड़े आधार का अर्थ है बहुत से युवा, जो जल्दी ही प्रजनन करेंगे, इसलिए जनसंख्या फैलती है। "
  "घंटी के आकार में युवाओं की संख्या लगभग प्रजननशील वर्ग जितनी होती है, इसलिए संख्या स्थिर रहती है; कलश के आकार में युवा वयस्कों से कम होते हैं, इसलिए जनसंख्या घटेगी; यह जापान जैसे कई बूढ़े होते समाजों का पैटर्न है।",
  f"{POP12} (population attributes: age pyramids).",
  "env-age-pyramids")

S(E, "medium", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["According to Liebig's law of the minimum, the growth of a plant is controlled by the nutrient that is present in the largest amount.",
   "Stenohaline organisms can tolerate a wide range of salinity.",
   "Eurythermal organisms can live only within a narrow range of temperature."],
  ["लीबिग के न्यूनतम के नियम के अनुसार, पौधे की वृद्धि उस पोषक तत्व से नियंत्रित होती है जो सबसे अधिक मात्रा में उपस्थित हो।",
   "तनुलवणी (stenohaline) जीव लवणता की विस्तृत सीमा सह सकते हैं।",
   "पृथुतापी (eurythermal) जीव तापमान की केवल संकरी सीमा में ही रह सकते हैं।"],
  C3, 3,
  "None of the statements is correct; each reverses a basic definition. Liebig's law says growth is limited by the essential factor in shortest supply, not the most abundant one -- adding more nitrogen does nothing for a crop that is short of phosphorus. "
  "The prefix 'eury-' means wide and 'steno-' narrow: stenohaline organisms tolerate only a narrow range of salinity (most freshwater and most marine fish), while euryhaline ones, such as salmon and many estuarine species, tolerate a wide range; and eurythermal organisms tolerate a wide range of temperature, stenothermal ones a narrow range. Tolerance ranges help explain why most organisms are restricted to particular habitats.",
  "कोई भी कथन सही नहीं है; हर कथन एक मूल परिभाषा को उलट देता है। लीबिग का नियम कहता है कि वृद्धि उस आवश्यक कारक से सीमित होती है जिसकी आपूर्ति सबसे कम है, सबसे अधिक वाले से नहीं; फ़ॉस्फ़ोरस की कमी वाली फ़सल में अधिक नाइट्रोजन डालने से कुछ नहीं होता। "
  "उपसर्ग 'पृथु-' (eury-) का अर्थ है विस्तृत और 'तनु-' (steno-) का संकरा: तनुलवणी जीव लवणता की केवल संकरी सीमा सहते हैं (अधिकांश मीठे पानी की और अधिकांश समुद्री मछलियाँ), जबकि पृथुलवणी जीव, जैसे सैल्मन और कई ज्वारनदमुखी प्रजातियाँ, विस्तृत सीमा सहते हैं; और पृथुतापी जीव तापमान की विस्तृत सीमा सहते हैं, तनुतापी संकरी। सहनशीलता की सीमाएँ समझाती हैं कि अधिकांश जीव विशेष आवासों तक ही सीमित क्यों हैं।",
  f"{POP12} (abiotic factors: eurythermal and stenothermal, euryhaline and stenohaline); E.P. Odum, Fundamentals of Ecology (limiting factors).",
  "env-limiting-factors-tolerance")

S(E, "medium", "Consider the following statements about decomposition:",
  "अपघटन (decomposition) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Warm and moist conditions speed up decomposition.",
   "Detritus rich in lignin and chitin decomposes faster than detritus rich in nitrogen and sugars.",
   "Decomposition is largely an anaerobic process."],
  ["गर्म और नम परिस्थितियाँ अपघटन को तेज़ करती हैं।",
   "लिग्निन और काइटिन से भरपूर अपरद (detritus), नाइट्रोजन और शर्करा से भरपूर अपरद की तुलना में तेज़ी से अपघटित होता है।",
   "अपघटन मुख्य रूप से एक अवायवीय (anaerobic) प्रक्रिया है।"],
  C3, 0,
  "Only statement 1 is correct: warmth and moisture favour the microbes that break down dead matter, while low temperature and lack of oxygen slow them down. "
  "Statement 2 is reversed: tough lignin (in wood) and chitin (in insect skeletons and fungal walls) resist breakdown, while nitrogen-rich, sugary detritus disappears quickly. "
  "Statement 3 is wrong: decomposition is largely an oxygen-requiring process. That is why waterlogged, oxygen-poor places such as bogs and mangrove mud accumulate undecomposed organic matter as peat and store so much carbon.",
  "केवल कथन 1 सही है: गर्मी और नमी मृत पदार्थ को तोड़ने वाले सूक्ष्मजीवों के अनुकूल हैं, जबकि कम तापमान और ऑक्सीजन की कमी उन्हें धीमा कर देते हैं। "
  "कथन 2 उलटा है: कठोर लिग्निन (लकड़ी में) और काइटिन (कीटों के कंकाल और कवक-भित्तियों में) टूटने का प्रतिरोध करते हैं, जबकि नाइट्रोजन से भरपूर, शर्करायुक्त अपरद जल्दी समाप्त हो जाता है। "
  "कथन 3 गलत है: अपघटन मुख्य रूप से ऑक्सीजन की आवश्यकता वाली प्रक्रिया है। इसीलिए दलदल और मैंग्रोव की कीचड़ जैसे जलभराव वाले, ऑक्सीजन-रहित स्थानों पर बिना अपघटित जैविक पदार्थ पीट के रूप में जमा होता है और बहुत अधिक कार्बन संचित रहता है।",
  f"{ECO12} (decomposition).",
  "env-decomposition-factors")

# ---------------------------------------------------------------- easy statements (2)
S(E, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The tundra biome is dominated by tall coniferous trees.",
   "The savanna is a tropical grassland with scattered trees and a long dry season."],
  ["टुंड्रा बायोम में ऊँचे शंकुधारी पेड़ों का प्रभुत्व होता है।",
   "सवाना बिखरे हुए पेड़ों और लंबी शुष्क ऋतु वाला उष्णकटिबंधीय घास का मैदान है।"],
  T2, 1,
  "Only statement 2 is correct: savannas, as in East Africa, combine grass cover with scattered trees such as acacias, and their long dry season and frequent fires keep them from becoming forest. "
  "Statement 1 describes the taiga (boreal forest), which lies just south of the tundra. The tundra itself is treeless: its permanently frozen subsoil (permafrost), cold and short summer allow only mosses, lichens, sedges and dwarf shrubs.",
  "केवल कथन 2 सही है: पूर्वी अफ़्रीका जैसे सवाना में घास के साथ बबूल जैसे बिखरे पेड़ होते हैं, और लंबी शुष्क ऋतु तथा बार-बार की आग उन्हें वन बनने से रोकती है। "
  "कथन 1 टैगा (बोरियल वन) का वर्णन है, जो टुंड्रा के ठीक दक्षिण में है। टुंड्रा स्वयं वृक्षहीन है: इसकी स्थायी रूप से जमी उप-मृदा (permafrost), ठंड और छोटी गर्मी केवल मॉस, लाइकेन, सेज और बौनी झाड़ियों को ही पनपने देती हैं।",
  "NCERT Class XI, Fundamentals of Physical Geography -- Biodiversity and Conservation / world biomes; NCERT Class XII, Biology -- Organisms and Populations (major biomes).",
  "env-tundra-savanna-biomes")

S(E, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["A population is a group of individuals of the same species living in an area.",
   "A community consists of the populations of different species living together in an area.",
   "An ecosystem includes only the living organisms of an area."],
  ["जनसंख्या किसी क्षेत्र में रहने वाले एक ही प्रजाति के व्यक्तियों का समूह है।",
   "समुदाय किसी क्षेत्र में एक साथ रहने वाली विभिन्न प्रजातियों की जनसंख्याओं से बनता है।",
   "पारितंत्र में किसी क्षेत्र के केवल जीवित जीव शामिल होते हैं।"],
  C3, 1,
  "Statements 1 and 2 are correct; they are the two levels of organisation just above the individual organism. "
  "Statement 3 is wrong: an ecosystem is the community together with its non-living (abiotic) environment -- soil, water, air, sunlight and nutrients -- and the flows of energy and cycles of matter that link them. Leaving out the abiotic part turns an ecosystem back into a community.",
  "कथन 1 और 2 सही हैं; ये व्यक्तिगत जीव के ठीक ऊपर के संगठन के दो स्तर हैं। "
  "कथन 3 गलत है: पारितंत्र समुदाय और उसके निर्जीव (अजैविक) पर्यावरण, यानी मिट्टी, पानी, हवा, सूर्य के प्रकाश और पोषक तत्वों, तथा उन्हें जोड़ने वाले ऊर्जा-प्रवाह और पदार्थ-चक्रों से मिलकर बनता है। अजैविक भाग को हटा दें तो पारितंत्र फिर से केवल समुदाय रह जाता है।",
  f"{POP12}; {ECO12}.",
  "env-population-community-ecosystem")

# ---------------------------------------------------------------- hard statements (2)
S(E, "hard", "Consider the following statements about the estimate of the value of the world's ecosystem services made by Robert Costanza and colleagues:",
  "रॉबर्ट कॉस्टैन्ज़ा और उनके सहयोगियों द्वारा किए गए विश्व की पारितंत्र सेवाओं के मूल्य के आकलन के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["They put the average value of these services at about US$ 33 trillion a year.",
   "Soil formation accounted for about half of the total value.",
   "Recreation and nutrient cycling each accounted for less than 10 per cent of the total."],
  ["उन्होंने इन सेवाओं का औसत मूल्य लगभग 33 ट्रिलियन अमेरिकी डॉलर प्रति वर्ष आँका।",
   "कुल मूल्य का लगभग आधा भाग मृदा-निर्माण का था।",
   "मनोरंजन और पोषक-चक्रण, प्रत्येक का हिस्सा कुल के 10 प्रतिशत से कम था।"],
  C3, 2,
  "All three statements are correct, as reported in NCERT. The 1997 study tried to put a price on services that nature provides free -- purification of air and water, pollination, flood control, soil formation, climate regulation -- and arrived at about US$ 33 trillion a year, larger than the world's GDP at the time. "
  "Soil formation made up about 50 per cent; recreation and nutrient cycling were each below 10 per cent, and climate regulation and habitat for wildlife about 6 per cent each. The point of the exercise is that such services are not 'free' simply because no one pays for them.",
  "तीनों कथन सही हैं, जैसा NCERT में दिया गया है। 1997 के इस अध्ययन ने प्रकृति द्वारा मुफ़्त दी जाने वाली सेवाओं, जैसे हवा और पानी की शुद्धि, परागण, बाढ़ नियंत्रण, मृदा-निर्माण और जलवायु नियमन, की कीमत आँकने की कोशिश की और लगभग 33 ट्रिलियन अमेरिकी डॉलर प्रति वर्ष का आँकड़ा दिया, जो उस समय के विश्व GDP से अधिक था। "
  "मृदा-निर्माण का हिस्सा लगभग 50 प्रतिशत था; मनोरंजन और पोषक-चक्रण, प्रत्येक 10 प्रतिशत से कम, और जलवायु नियमन तथा वन्यजीवों के आवास, प्रत्येक लगभग 6 प्रतिशत थे। इस प्रयास का मुद्दा यह है कि ऐसी सेवाएँ केवल इसलिए 'मुफ़्त' नहीं हो जातीं कि उनके लिए कोई भुगतान नहीं करता।",
  f"{ECO12} (ecosystem services); R. Costanza et al., Nature 387 (1997).",
  "env-ecosystem-services-value")

S(E, "hard", "Consider the following statements about how organisms respond to their environment:",
  "जीव अपने पर्यावरण के प्रति कैसे प्रतिक्रिया करते हैं, इसके बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Nearly all plants and most animals cannot keep their internal environment constant, and are called conformers.",
   "Very small mammals such as shrews are rare in polar regions, because their large surface area relative to volume makes them lose body heat fast.",
   "At high altitude, the human body compensates for low oxygen partly by reducing the production of red blood cells.",
   "Many zooplankton species in lakes enter diapause, a stage of suspended development, when conditions are unfavourable."],
  ["लगभग सभी पौधे और अधिकांश जंतु अपने आंतरिक पर्यावरण को स्थिर नहीं रख सकते, और इन्हें अनुरूपक (conformers) कहा जाता है।",
   "छछूंदर (shrew) जैसे बहुत छोटे स्तनधारी ध्रुवीय क्षेत्रों में दुर्लभ हैं, क्योंकि आयतन की तुलना में उनकी सतह बड़ी होने से वे शरीर की गर्मी जल्दी खोते हैं।",
   "ऊँचाई पर मानव शरीर कम ऑक्सीजन की भरपाई आंशिक रूप से लाल रक्त कोशिकाओं का उत्पादन घटाकर करता है।",
   "झीलों की कई ज़ूप्लैंकटन प्रजातियाँ प्रतिकूल परिस्थितियों में डायपॉज़ (diapause), यानी निलंबित विकास की अवस्था, में चली जाती हैं।"],
  C4, 2,
  "Statements 1, 2 and 4 are correct. By NCERT's figure, about 99 per cent of animals and nearly all plants are conformers; keeping a constant body temperature (being a regulator) is costly, and small animals pay most, since heat is lost through the surface and gained through the volume -- hence no shrews or hummingbirds in the polar regions. "
  "Diapause in zooplankton is a way of 'suspending' through a bad season, as hibernation is for bears. "
  "Statement 3 reverses the response: at high altitude the body makes more red blood cells, lowers the binding affinity of haemoglobin and breathes faster, which is why climbers acclimatise over days before going higher.",
  "कथन 1, 2 और 4 सही हैं। NCERT के आँकड़े के अनुसार लगभग 99 प्रतिशत जंतु और लगभग सभी पौधे अनुरूपक हैं; शरीर का तापमान स्थिर रखना (नियामक होना) महँगा है, और छोटे जंतुओं को इसकी सबसे अधिक कीमत चुकानी पड़ती है, क्योंकि गर्मी सतह से खोती है और आयतन से बनती है; इसीलिए ध्रुवीय क्षेत्रों में छछूंदर या हमिंगबर्ड नहीं मिलते। "
  "ज़ूप्लैंकटन में डायपॉज़ खराब मौसम को 'स्थगित' होकर काटने का तरीका है, जैसे भालुओं के लिए शीतनिद्रा। "
  "कथन 3 प्रतिक्रिया को उलट देता है: ऊँचाई पर शरीर अधिक लाल रक्त कोशिकाएँ बनाता है, हीमोग्लोबिन की बंधन-क्षमता घटाता है और तेज़ साँस लेता है; इसीलिए पर्वतारोही और ऊपर जाने से पहले कुछ दिनों तक अनुकूलन (acclimatisation) करते हैं।",
  f"{POP12} (responses to abiotic factors: regulate, conform, migrate, suspend).",
  "env-regulators-conformers-responses")

# ---------------------------------------------------------------- MCQs (4)
M(E, "easy", "In the food chain grass → grasshopper → frog → snake → hawk, the frog is a:",
  "खाद्य शृंखला घास → टिड्डा → मेंढक → साँप → बाज़ में मेंढक क्या है?",
  ["Secondary consumer", "Primary consumer", "Tertiary (third-order) consumer", "Producer"],
  ["द्वितीयक उपभोक्ता", "प्राथमिक उपभोक्ता", "तृतीयक (तीसरे क्रम का) उपभोक्ता", "उत्पादक"],
  0,
  "Grass is the producer (first trophic level), the grasshopper eats it and is the primary consumer (second level), and the frog, which eats the grasshopper, is the secondary consumer at the third trophic level; the snake is a tertiary consumer and the hawk the top carnivore. "
  "The trap is the word 'third': the frog stands at the third trophic level but is only the second consumer in the chain.",
  "घास उत्पादक है (पहला पोषी स्तर), टिड्डा उसे खाता है और प्राथमिक उपभोक्ता है (दूसरा स्तर), और टिड्डे को खाने वाला मेंढक तीसरे पोषी स्तर पर द्वितीयक उपभोक्ता है; साँप तृतीयक उपभोक्ता है और बाज़ शीर्ष मांसाहारी। "
  "जाल 'तीसरे' शब्द में है: मेंढक तीसरे पोषी स्तर पर है, पर शृंखला में वह केवल दूसरा उपभोक्ता है।",
  f"{ECO12} (food chains and trophic levels).",
  "env-trophic-level-frog")

M(E, "easy", "The term 'ecosystem' was first used by:",
  "'पारितंत्र' (ecosystem) शब्द का पहली बार उपयोग किसने किया?",
  ["A.G. Tansley", "Ernst Haeckel", "Charles Elton", "Eugene Odum"],
  ["ए.जी. टैंसले", "अर्न्स्ट हेकेल", "चार्ल्स एल्टन", "यूजीन ओडम"],
  0,
  "The British ecologist A.G. Tansley introduced the term 'ecosystem' in 1935 for the community of organisms together with its physical environment. "
  "Ernst Haeckel, the tempting distractor, coined the word 'ecology' (1866); Charles Elton developed the ideas of food chains, the niche and the pyramid of numbers; and Eugene Odum's textbook made ecosystem ecology a core discipline.",
  "ब्रिटिश पारिस्थितिकीविद ए.जी. टैंसले ने 1935 में जीवों के समुदाय और उसके भौतिक पर्यावरण के लिए 'पारितंत्र' शब्द दिया। "
  "आकर्षक गलत विकल्प अर्न्स्ट हेकेल ने 'पारिस्थितिकी' (ecology) शब्द गढ़ा था (1866); चार्ल्स एल्टन ने खाद्य शृंखला, निकेत और संख्या-पिरामिड के विचार विकसित किए; और यूजीन ओडम की पाठ्यपुस्तक ने पारितंत्र पारिस्थितिकी को एक मुख्य विषय बनाया।",
  f"{ECO12}; A.G. Tansley, Ecology 16 (1935).",
  "env-ecosystem-term-tansley")

M(E, "medium", "Which one of the following is best described as a K-selected species?",
  "निम्नलिखित में से किसे K-चयनित (K-selected) प्रजाति के रूप में सबसे अच्छी तरह वर्णित किया जा सकता है?",
  ["Asian elephant", "Anopheles mosquito", "Common housefly", "Desert locust"],
  ["एशियाई हाथी", "एनोफ़िलीज़ मच्छर", "घरेलू मक्खी", "रेगिस्तानी टिड्डी"],
  0,
  "K-selected species live in fairly stable environments where the population stays near the carrying capacity (K); they grow slowly, mature late, have few offspring and invest heavily in each -- the elephant, with a pregnancy of about 22 months and years of care for each calf, is the classic case. "
  "Mosquitoes, houseflies and locusts are r-selected: they mature quickly, produce huge numbers of young with little care and can multiply explosively (r is the intrinsic rate of increase) when conditions allow -- which is why they swarm and why they recover so quickly from control measures.",
  "K-चयनित प्रजातियाँ अपेक्षाकृत स्थिर पर्यावरण में रहती हैं, जहाँ जनसंख्या वहन क्षमता (K) के पास बनी रहती है; वे धीरे बढ़ती हैं, देर से परिपक्व होती हैं, कम संतानें पैदा करती हैं और हर संतान पर बहुत निवेश करती हैं; लगभग 22 महीने के गर्भकाल और हर बच्चे की वर्षों तक देखभाल वाला हाथी इसका मानक उदाहरण है। "
  "मच्छर, घरेलू मक्खी और टिड्डी r-चयनित हैं: ये जल्दी परिपक्व होते हैं, कम देखभाल के साथ भारी संख्या में संतानें पैदा करते हैं और परिस्थितियाँ अनुकूल होने पर विस्फोटक रूप से बढ़ सकते हैं (r वृद्धि की अंतर्निहित दर है); इसीलिए ये झुंड बनाते हैं और नियंत्रण उपायों के बाद भी इतनी जल्दी लौट आते हैं।",
  f"{POP12} (population growth: exponential and logistic, carrying capacity); E.P. Odum, Fundamentals of Ecology.",
  "env-r-k-selection")

M(E, "hard", "According to the species-area relationship described by Alexander von Humboldt, when very large areas such as whole continents are compared, the slope (Z) of the line on a log-log plot:",
  "अलेक्ज़ेंडर वॉन हम्बोल्ट द्वारा वर्णित जाति-क्षेत्र संबंध के अनुसार, जब पूरे महाद्वीपों जैसे बहुत बड़े क्षेत्रों की तुलना की जाती है, तो लॉग-लॉग आलेख पर रेखा का ढलान (Z):",
  ["is much steeper, about 0.6 to 1.2", "stays at about 0.1 to 0.2, as for smaller areas", "falls to zero, as richness stops rising", "turns negative, as larger areas hold fewer species"],
  ["कहीं अधिक खड़ा होता है, लगभग 0.6 से 1.2", "छोटे क्षेत्रों की तरह लगभग 0.1 से 0.2 ही रहता है", "शून्य हो जाता है, क्योंकि समृद्धि बढ़ना बंद हो जाती है", "ऋणात्मक हो जाता है, क्योंकि बड़े क्षेत्रों में कम प्रजातियाँ होती हैं"],
  0,
  "Within a region, species richness rises with area, but at a diminishing rate; on a log-log plot the relationship becomes a straight line, log S = log C + Z log A. For most taxa and regions, Z lies between about 0.1 and 0.2 -- the distractor that most students remember. "
  "But when very large areas such as entire continents are compared, the line becomes much steeper, with Z of about 0.6 to 1.2 (for example, for frugivorous birds and mammals of the tropical forests of different continents), because different continents hold largely different sets of species.",
  "किसी क्षेत्र के भीतर जाति-समृद्धि क्षेत्रफल के साथ बढ़ती है, पर घटती दर से; लॉग-लॉग आलेख पर यह संबंध एक सीधी रेखा बन जाता है, log S = log C + Z log A। अधिकांश वर्गकों और क्षेत्रों के लिए Z लगभग 0.1 से 0.2 के बीच होता है, और यही वह गलत विकल्प है जो अधिकांश विद्यार्थियों को याद रहता है। "
  "पर जब पूरे महाद्वीपों जैसे बहुत बड़े क्षेत्रों की तुलना की जाती है, तो रेखा कहीं अधिक खड़ी हो जाती है और Z लगभग 0.6 से 1.2 होता है (जैसे, विभिन्न महाद्वीपों के उष्णकटिबंधीय वनों के फलाहारी पक्षियों और स्तनधारियों के लिए), क्योंकि अलग-अलग महाद्वीपों में प्रजातियों के समूह काफ़ी हद तक अलग होते हैं।",
  f"{BIOD12} (species-area relationships).",
  "env-species-area-relationship")

# ---------------------------------------------------------------- pairs (1, medium)
P(E, "medium", "Consider the following pairs of types of interaction between species and examples:",
  "प्रजातियों के बीच अंतःक्रिया के प्रकारों और उदाहरणों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Mutualism : Loranthus growing on a mango tree", "Commensalism : Cattle egret foraging near grazing cattle",
   "Competition : Barnacles growing on the back of a whale", "Amensalism : Penicillium mould inhibiting nearby bacteria"],
  ["सहोपकारिता (mutualism) : आम के पेड़ पर उगता लोरेंथस (बाँदा)", "सहभोजिता (commensalism) : चरते मवेशियों के पास भोजन खोजता मवेशी बगुला",
   "स्पर्धा (competition) : व्हेल की पीठ पर उगते बार्नेकल", "अंतरजातीय प्रतिजीविता (amensalism) : पास के जीवाणुओं को रोकती पेनिसिलियम फफूँद"],
  1,
  "Only pairs 2 and 4 are correct. The cattle egret eats insects stirred up by grazing cattle, and the cattle neither gain nor lose -- commensalism. Penicillium releases a substance that kills or checks bacteria around it without any benefit or harm to itself from them -- amensalism. "
  "Pair 1 is wrong: Loranthus (mistletoe, 'banda') is a partial parasite that sends suckers into the host's branches to draw water and minerals; it is not mutualism. Pair 3 is wrong: barnacles ride on a whale for a place to live and access to food while the whale is little affected, which is the textbook example of commensalism, not competition.",
  "केवल युग्म 2 और 4 सही हैं। मवेशी बगुला चरते मवेशियों द्वारा उड़ाए गए कीट खाता है, और मवेशियों को न लाभ होता है न हानि; यह सहभोजिता है। पेनिसिलियम ऐसा पदार्थ छोड़ता है जो आसपास के जीवाणुओं को मारता या रोकता है, और उनसे उसे न कोई लाभ होता है न हानि; यह अंतरजातीय प्रतिजीविता (amensalism) है। "
  "युग्म 1 गलत है: लोरेंथस (बाँदा) एक आंशिक परजीवी है, जो मेज़बान की शाखाओं में चूषक (haustoria) भेजकर पानी और खनिज खींचता है; यह सहोपकारिता नहीं है। युग्म 3 गलत है: बार्नेकल रहने की जगह और भोजन तक पहुँच के लिए व्हेल पर सवारी करते हैं जबकि व्हेल पर बहुत कम असर होता है; यह सहभोजिता का पाठ्यपुस्तकीय उदाहरण है, स्पर्धा का नहीं।",
  f"{POP12} (population interactions).",
  "env-species-interactions-pairs")

if __name__ == "__main__":
    write("env_l2_t9_ecosystems.sql")
