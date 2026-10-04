# -*- coding: utf-8 -*-
"""Level 2 · Test 12 (Geography 1: Physical and World) -- depth audit of 2026-10-04, part A: Climatology & Biomes,
Geomorphology & Earth's Interior and Oceanography & Hydrosphere (docs/upsc-question-design-standard.md §6).
Part B (upg_l2_t12_geo_b.py) has World Regions, Water Bodies & Places and the tags for the kept rows.

Before the audit the test had analytic 28, precision 26, recall 51. Part A rewrites 10 recall rows in place
with the same concept id, type and difficulty:
  - analytic: a climate described by its months to be coded in Koppen's scheme, why tornadoes cluster on
    the Great Plains, why fossils shun igneous rock, what lava chemistry does to a volcano's shape, why a
    tsunami grows near the shore, and what happens where warm and cold currents meet;
  - precision: near-miss versions of the grassland pairs, cloud types, landform agents and the
    discontinuities of the interior.
Leaks avoided while drafting:
  - the Gulf of Mexico as the source of warm, moist air (answers the air-mass MCQ);
  - descending air warming by compression (states the adiabatic row's statement 3);
  - cold currents off west coasts and upwelling off Peru (the west-coast-deserts AR and the El Nino row);
  - 'mushroom rock : glacier' (repeats the oxbow-barchan row's statement 3)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write_updates, CODE
from polity_common import C3, C4, T2

d.SUBJECT = "Geography"
d.REQUIRE_CRAFT = True
CL = "Climatology & Biomes"
GM = "Geomorphology & Earth's Interior"
OC = "Oceanography & Hydrosphere"
NC11 = "NCERT Class XI, Fundamentals of Physical Geography"
NC7 = "NCERT Class VII, Our Environment"

# ================================================================ CLIMATOLOGY (4)
M(CL, "hard", "At a lowland station, every month has a mean temperature above 18 °C. Heavy rain falls in the high-sun season and is followed by a dry season of four to five months in the low-sun period. In Köppen's scheme, the station's climate is:",
  "एक निचले भूभाग के केंद्र पर हर महीने का औसत तापमान 18 °C से ऊपर रहता है। उच्च-सूर्य ऋतु में भारी वर्षा होती है, जिसके बाद निम्न-सूर्य काल में चार से पाँच महीने का शुष्क मौसम आता है। कोपेन की योजना में इस केंद्र की जलवायु है:",
  ["Aw", "Af", "Am", "BSh"], ["Aw", "Af", "Am", "BSh"], 0,
  "'A' marks a tropical climate in which every month averages above 18 °C. The second letter describes the rainfall: 'f' means no dry season (the equatorial rainforest), 'm' means monsoon rain heavy enough to carry the forest through a short dry season, and 'w' means a distinct dry season in winter, the low-sun period -- the tropical wet-and-dry or savanna climate. "
  "A dry season of four or five months is too long for Am, and since the rain is still enough for the A group, the climate is not BSh, the hot semi-arid steppe of the dry B group.",
  "'A' उस उष्णकटिबंधीय जलवायु का चिह्न है जिसमें हर महीने का औसत 18 °C से ऊपर हो। दूसरा अक्षर वर्षा बताता है: 'f' का अर्थ है कोई शुष्क मौसम नहीं (भूमध्यरेखीय वर्षावन), 'm' का अर्थ है इतनी भारी मानसूनी वर्षा कि वन एक छोटे शुष्क मौसम को झेल ले, और 'w' का अर्थ है शीत ऋतु, यानी निम्न-सूर्य काल, में स्पष्ट शुष्क मौसम, जो उष्णकटिबंधीय आर्द्र-शुष्क या सवाना जलवायु है। "
  "चार-पाँच महीने का शुष्क मौसम Am के लिए बहुत लंबा है, और चूँकि वर्षा A समूह के लिए अब भी पर्याप्त है, इसलिए जलवायु शुष्क B समूह की गर्म अर्ध-शुष्क स्टेपी BSh नहीं है।",
  NC11, "geo-koppen-aw-savanna", craft="application")

M(CL, "medium", "Tornadoes are more frequent on the Great Plains of the United States than anywhere else on Earth. The main reason is that there:",
  "संयुक्त राज्य अमेरिका के 'ग्रेट प्लेन्स' में बवंडर (टॉर्नेडो) पृथ्वी पर कहीं और से अधिक आते हैं। इसका मुख्य कारण यह है कि वहाँ:",
  ["warm, moist air from the south meets cold, dry air from the north, with no range between",
   "warm sea water just offshore keeps feeding storms with heat and moisture throughout the year",
   "the plains lie at so great a height that thunderclouds form directly inside the jet stream above them",
   "an active fault line beneath the plains releases heat that sets off rising currents of air in spring"],
  ["दक्षिण की गर्म, नम वायु उत्तर की ठंडी, शुष्क वायु से मिलती है, और बीच में कोई पर्वत-श्रेणी नहीं है",
   "तट के पास का गर्म समुद्री जल साल भर तूफ़ानों को ऊष्मा और नमी देता रहता है",
   "मैदान इतनी ऊँचाई पर हैं कि गरज वाले बादल सीधे उनके ऊपर की जेट धारा के भीतर बनते हैं",
   "मैदानों के नीचे की एक सक्रिय भ्रंश-रेखा ऊष्मा छोड़ती है जो वसंत में वायु की ऊर्ध्व धाराएँ पैदा करती है"],
  0,
  "Tornadoes grow out of severe thunderstorms that need warm, moist air near the ground, dry air above it and winds that change direction and speed with height. On the Great Plains, moist tropical air flowing north and cold, dry air flowing south from Canada clash in spring and early summer, and because the Rockies and the Appalachians run north-south, nothing keeps them apart. "
  "The Great Plains lie deep inland, far from any sea, and faults play no part in tornadoes.",
  "बवंडर उन तीव्र गरज-तूफ़ानों से पनपते हैं जिन्हें धरातल के पास गर्म, नम वायु, उसके ऊपर शुष्क वायु और ऊँचाई के साथ दिशा व गति बदलने वाली हवाएँ चाहिए। ग्रेट प्लेन्स पर उत्तर की ओर बहती नम उष्णकटिबंधीय वायु और कनाडा से दक्षिण की ओर बहती ठंडी, शुष्क वायु वसंत और आरंभिक ग्रीष्म में टकराती हैं, और चूँकि रॉकी और अप्लेशियन उत्तर-दक्षिण फैले हैं, इसलिए उन्हें अलग रखने वाला कुछ नहीं है। "
  "ग्रेट प्लेन्स किसी भी समुद्र से दूर, भीतरी भाग में हैं, और भ्रंशों की बवंडरों में कोई भूमिका नहीं होती।",
  NC11, "geo-tornadoes-great-plains", craft="linkage")

P(CL, "easy", "Consider the following pairs of temperate grasslands and the regions where they are found:",
  "शीतोष्ण घास के मैदानों और उन क्षेत्रों के निम्नलिखित युग्मों पर विचार कीजिए जहाँ वे पाए जाते हैं:",
  ["Prairies : North America", "Pampas : Argentina", "Veld : Australia", "Downs : New Zealand"],
  ["प्रेयरी : उत्तरी अमेरिका", "पम्पास : अर्जेंटीना", "वेल्ड : ऑस्ट्रेलिया", "डाउन्स : न्यूज़ीलैंड"],
  1,
  "Only pairs 1 and 2 are correct. Pairs 3 and 4 swap the southern grasslands around: the Veld is the grassland of the South African plateau, the Downs are in south-eastern Australia (the Murray-Darling basin), and New Zealand's temperate grassland is the Canterbury plain. The Steppes of Eurasia complete the usual list.",
  "केवल युग्म 1 और 2 सही हैं। युग्म 3 और 4 दक्षिणी घास के मैदानों को आपस में बदल देते हैं: वेल्ड दक्षिण अफ़्रीकी पठार का घास का मैदान है, डाउन्स दक्षिण-पूर्वी ऑस्ट्रेलिया (मरे-डार्लिंग बेसिन) में हैं, और न्यूज़ीलैंड का शीतोष्ण घास का मैदान कैंटरबरी का मैदान है। यूरेशिया के स्टेपी इस सामान्य सूची को पूरा करते हैं।",
  NC7, "geo-temperate-grasslands-pairs-easy", craft="precision")

S(CL, "medium", "Consider the following statements about clouds:",
  "बादलों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Cirrus clouds form at high altitudes and are made mostly of ice crystals.",
   "Cumulonimbus clouds bring steady, continuous drizzle over a wide area for many hours.",
   "Nimbostratus clouds bring thunder, lightning and hail."],
  ["पक्षाभ (सिरस) बादल ऊँचाई पर बनते हैं और मुख्यतः हिम-कणों से बने होते हैं।",
   "कपासी-वर्षी (क्यूम्यलोनिम्बस) बादल कई घंटों तक विस्तृत क्षेत्र में स्थिर, लगातार फुहार लाते हैं।",
   "वर्षा-स्तरी (निम्बोस्ट्रेटस) बादल गरज, बिजली और ओले लाते हैं।"],
  C3, 0,
  "Only statement 1 is correct: cirrus are thin, feathery clouds at about 8-12 km, too cold for liquid water. Statements 2 and 3 swap the two rain clouds. Cumulonimbus are towering thunderclouds whose tops can reach the tropopause; they bring short, intense showers with lightning, thunder and often hail. "
  "Nimbostratus are thick, grey, layered clouds that bring the steady, continuous rain or snow that can last for hours over a wide area.",
  "केवल कथन 1 सही है: पक्षाभ लगभग 8-12 किमी की ऊँचाई पर पतले, पंख जैसे बादल हैं, जहाँ तरल जल के लिए बहुत ठंड है। कथन 2 और 3 दो वर्षा-बादलों को आपस में बदल देते हैं। कपासी-वर्षी ऊँचे गरज-बादल हैं जिनके शिखर क्षोभसीमा तक पहुँच सकते हैं; वे बिजली, गरज और प्रायः ओलों के साथ थोड़ी देर की तीव्र बौछारें लाते हैं। "
  "वर्षा-स्तरी मोटे, धूसर, परतदार बादल हैं जो विस्तृत क्षेत्र में घंटों चलने वाली स्थिर, लगातार वर्षा या हिमपात लाते हैं।",
  NC11, "geo-cloud-types", craft="precision")

# ================================================================ GEOMORPHOLOGY (4)
S(GM, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Fossils are common in igneous rocks, since lava buries and preserves the plants and animals it flows over.",
   "Fossils are found mostly in sedimentary rocks, which form as layers of sediment slowly bury remains and harden."],
  ["आग्नेय चट्टानों में जीवाश्म आम हैं, क्योंकि लावा जिन पौधों और जीवों पर बहता है उन्हें दबाकर सुरक्षित रखता है।",
   "जीवाश्म मुख्यतः अवसादी चट्टानों में मिलते हैं, जो तब बनती हैं जब अवसाद की परतें धीरे-धीरे अवशेषों को दबाकर कठोर हो जाती हैं।"],
  T2, 1,
  "Only statement 2 is correct. Sediment settling on a sea bed, lake floor or flood plain buries shells, bones and leaves gently, and as the layers are compacted and cemented into sandstone, shale or limestone, the remains or their imprints are preserved. "
  "Statement 1 is wrong: igneous rocks form from molten magma or lava at temperatures of roughly 700-1,200 °C, which burn or melt any organism, so fossils are almost never found in them; heat and pressure also destroy most fossils when rocks are metamorphosed.",
  "केवल कथन 2 सही है। समुद्र-तल, झील-तल या बाढ़ के मैदान पर जमता अवसाद सीपियों, हड्डियों और पत्तियों को धीरे से दबा देता है, और जब परतें दबकर और जुड़कर बलुआ पत्थर, शेल या चूना पत्थर बनती हैं, तो अवशेष या उनकी छाप सुरक्षित रह जाती है। "
  "कथन 1 गलत है: आग्नेय चट्टानें लगभग 700-1,200 °C के पिघले मैग्मा या लावा से बनती हैं, जो किसी भी जीव को जला या पिघला देता है, इसलिए उनमें जीवाश्म लगभग कभी नहीं मिलते; चट्टानों के कायांतरण में ताप और दबाव भी अधिकांश जीवाश्म नष्ट कर देते हैं।",
  NC11, "geo-igneous-fossils-easy", craft="linkage")

S(GM, "medium", "Consider the following statements about volcanoes:",
  "ज्वालामुखियों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Shield volcanoes have gentle slopes because their fluid basaltic lava flows a long way before it cools.",
   "Composite volcanoes tend to erupt explosively because their thicker, silica-rich magma traps gas.",
   "A caldera is a steep cone built up by repeated eruptions of ash."],
  ["ढाल ज्वालामुखियों की ढलानें मंद होती हैं क्योंकि उनका तरल बेसाल्टी लावा ठंडा होने से पहले दूर तक बहता है।",
   "मिश्रित ज्वालामुखी प्रायः विस्फोटक रूप से फटते हैं क्योंकि उनका गाढ़ा, सिलिका-समृद्ध मैग्मा गैस को रोक लेता है।",
   "काल्डेरा राख के बार-बार उद्गार से बना एक खड़ा शंकु है।"],
  C3, 1,
  "Statements 1 and 2 are correct. The shape of a volcano follows its lava: basaltic lava, low in silica, is runny and spreads in thin sheets, building broad, gently sloping shields such as Mauna Loa; silica-rich andesitic magma is viscous, so gas cannot escape until pressure blasts it out, and alternating lava and ash build steep composite cones such as Fuji or Vesuvius. "
  "Statement 3 is wrong: a caldera is a large depression formed when the summit collapses into the emptied magma chamber after a great eruption, as at Krakatoa or Crater Lake in Oregon.",
  "कथन 1 और 2 सही हैं। ज्वालामुखी का आकार उसके लावा पर निर्भर है: कम सिलिका वाला बेसाल्टी लावा पतला होता है और पतली परतों में फैलता है, जिससे मौना लोआ जैसे चौड़े, मंद ढाल वाले ज्वालामुखी बनते हैं; सिलिका-समृद्ध एंडेसाइटी मैग्मा गाढ़ा होता है, इसलिए गैस तब तक नहीं निकलती जब तक दबाव उसे विस्फोट से बाहर न फेंके, और लावा तथा राख की बारी-बारी परतें फ़ूजी या विसूवियस जैसे खड़े मिश्रित शंकु बनाती हैं। "
  "कथन 3 गलत है: काल्डेरा वह बड़ा गर्त है जो किसी बड़े उद्गार के बाद ख़ाली मैग्मा कक्ष में शिखर के धँसने से बनता है, जैसे क्राकाटोआ या ओरेगन की क्रेटर झील।",
  NC11, "geo-volcano-types-caldera", craft="linkage")

P(GM, "medium", "Consider the following pairs of landforms and the agents that mainly form them:",
  "भू-आकृतियों और उन्हें मुख्यतः बनाने वाले कारकों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Yardang : Wind", "Esker : Sea waves", "Levee : River", "Hanging valley : Glacier"],
  ["यारडांग : पवन", "एस्कर : समुद्री लहरें", "तटबंध (लेवी) : नदी", "निलंबी घाटी : हिमनद"],
  2,
  "Three pairs are correct. Yardangs are streamlined rock ridges cut by wind-blown sand in deserts; levees are raised banks built up by a river's floods; and hanging valleys are tributary valleys left high above a main valley that a glacier deepened. "
  "Pair 2 is wrong: an esker is a long, winding ridge of sand and gravel laid down by a stream flowing in a tunnel beneath a glacier, and exposed when the ice melts; sea waves build spits, bars and beaches.",
  "तीन युग्म सही हैं। यारडांग मरुस्थलों में पवन से उड़ती रेत द्वारा काटी गई सुव्यवस्थित चट्टानी कटकें हैं; तटबंध नदी की बाढ़ों से बने ऊँचे किनारे हैं; और निलंबी घाटियाँ वे सहायक घाटियाँ हैं जो हिमनद द्वारा गहरी की गई मुख्य घाटी से बहुत ऊपर रह जाती हैं। "
  "युग्म 2 गलत है: एस्कर रेत और बजरी की लंबी, घुमावदार कटक है जिसे हिमनद के नीचे सुरंग में बहने वाली धारा जमा करती है, और जो बर्फ़ पिघलने पर दिखती है; समुद्री लहरें स्पिट, रोधिकाएँ और पुलिन बनाती हैं।",
  NC11, "geo-landforms-agents-pairs", craft="precision")

S(GM, "medium", "Consider the following statements about the Earth's interior:",
  "पृथ्वी के आंतरिक भाग के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Mohorovičić discontinuity separates the crust from the mantle.",
   "The Gutenberg discontinuity separates the upper mantle from the lower mantle.",
   "The Lehmann discontinuity separates the outer core from the inner core."],
  ["मोहोरोविचिच असांतत्य भूपर्पटी को प्रावार (मेंटल) से अलग करता है।",
   "गुटेनबर्ग असांतत्य ऊपरी प्रावार को निचले प्रावार से अलग करता है।",
   "लेहमन असांतत्य बाह्य क्रोड को आंतरिक क्रोड से अलग करता है।"],
  C3, 1,
  "Statements 1 and 3 are correct. These boundaries were found from sudden changes in the speed of seismic waves: the 'Moho' lies about 5-10 km below the ocean floor and 30-70 km below the continents, and the Lehmann discontinuity lies at about 5,150 km, where the liquid outer core gives way to the solid inner core. "
  "Statement 2 is wrong: the Gutenberg discontinuity, at about 2,900 km, separates the mantle from the outer core, where S-waves stop; the boundary between the upper and lower mantle is called the Repetti discontinuity.",
  "कथन 1 और 3 सही हैं। ये सीमाएँ भूकंपीय तरंगों की गति में अचानक परिवर्तन से पहचानी गईं: 'मोहो' समुद्र-तल से लगभग 5-10 किमी और महाद्वीपों के नीचे 30-70 किमी गहराई पर है, और लेहमन असांतत्य लगभग 5,150 किमी पर है, जहाँ तरल बाह्य क्रोड ठोस आंतरिक क्रोड में बदलता है। "
  "कथन 2 गलत है: लगभग 2,900 किमी पर स्थित गुटेनबर्ग असांतत्य प्रावार को बाह्य क्रोड से अलग करता है, जहाँ S-तरंगें रुक जाती हैं; ऊपरी और निचले प्रावार की सीमा को रेपेटी असांतत्य कहते हैं।",
  NC11, "geo-earth-interior-discontinuities", craft="precision")

# ================================================================ OCEANOGRAPHY (2)
A(OC, "medium",
  "A tsunami can pass almost unnoticed beneath a ship in the open ocean, yet rise to a great height as it reaches the coast.",
  "सुनामी खुले महासागर में किसी जहाज़ के नीचे से लगभग बिना पता चले निकल सकती है, फिर भी तट पर पहुँचते-पहुँचते बहुत ऊँची उठ जाती है।",
  "As the wave enters shallow water it slows down, so its energy is squeezed into a shorter, taller wave.",
  "उथले जल में प्रवेश करते ही तरंग धीमी हो जाती है, इसलिए उसकी ऊर्जा एक छोटी, ऊँची तरंग में सिमट जाती है।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I. In the deep ocean a tsunami may be less than a metre high but hundreds of kilometres long, racing at 700-800 km/h; because the whole column of water moves, a ship hardly notices it. "
  "As the sea floor rises towards the coast the wave slows sharply, the waves behind catch up with those in front, and the same energy is packed into a much shorter length, so the water piles up -- sometimes to 10 m or more, as on the coasts around the Indian Ocean in December 2004.",
  "दोनों कथन सही हैं, और कथन-II कथन-I की व्याख्या करता है। गहरे महासागर में सुनामी एक मीटर से भी कम ऊँची पर सैकड़ों किलोमीटर लंबी हो सकती है, जो 700-800 किमी/घंटा से दौड़ती है; चूँकि जल का पूरा स्तंभ चलता है, जहाज़ उसे मुश्किल से महसूस करता है। "
  "तट की ओर समुद्र-तल उठने पर तरंग तेज़ी से धीमी होती है, पीछे की तरंगें आगे वालों को पकड़ लेती हैं, और वही ऊर्जा बहुत छोटी लंबाई में भर जाती है, इसलिए पानी ऊपर उठता जाता है, कभी-कभी 10 मीटर या उससे अधिक, जैसे दिसंबर 2004 में हिंद महासागर के तटों पर।",
  "India National Centre for Ocean Information Services -- Indian Tsunami Early Warning Centre.", "geo-tsunami-cause", craft="linkage")

S(OC, "medium", "Consider the following statements about ocean currents:",
  "महासागरीय धाराओं के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Where the warm Gulf Stream meets the cold Labrador Current off Newfoundland, the mixing of the waters produces thick fog and one of the world's richest fishing grounds.",
   "The Kuroshio is a cold current off the coast of Japan.",
   "The Oyashio is a warm current."],
  ["जहाँ गर्म गल्फ़ स्ट्रीम न्यूफ़ाउंडलैंड के पास ठंडी लैब्राडोर धारा से मिलती है, वहाँ जल के मिश्रण से घना कोहरा बनता है और संसार के सबसे समृद्ध मत्स्य-क्षेत्रों में से एक बनता है।",
   "कुरोशियो जापान के तट से दूर बहने वाली एक ठंडी धारा है।",
   "ओयाशियो एक गर्म धारा है।"],
  C3, 0,
  "Only statement 1 is correct. On the Grand Banks, warm, moist air over the Gulf Stream is chilled over the cold Labrador water, so fog is frequent, and the mixing of the two waters, over a shallow bank, stirs up nutrients that feed plankton and huge shoals of cod. "
  "Statements 2 and 3 swap the two currents of the north-western Pacific: the Kuroshio is warm, flowing north-east past Japan like the Gulf Stream in the Atlantic, while the Oyashio is cold, flowing south from the Arctic; where they meet off northern Japan lies another rich fishing ground.",
  "केवल कथन 1 सही है। ग्रैंड बैंक्स पर गल्फ़ स्ट्रीम के ऊपर की गर्म, नम वायु ठंडे लैब्राडोर जल के ऊपर ठंडी होती है, इसलिए कोहरा बार-बार होता है, और एक उथले बैंक के ऊपर दोनों जलों का मिश्रण पोषक तत्व ऊपर लाता है, जिनसे प्लवक और कॉड मछलियों के विशाल झुंड पलते हैं। "
  "कथन 2 और 3 उत्तर-पश्चिमी प्रशांत की दो धाराओं को आपस में बदल देते हैं: कुरोशियो गर्म है, जो अटलांटिक की गल्फ़ स्ट्रीम की तरह जापान के पास से उत्तर-पूर्व की ओर बहती है, जबकि ओयाशियो ठंडी है, जो आर्कटिक से दक्षिण की ओर बहती है; जहाँ वे उत्तरी जापान के पास मिलती हैं, वहाँ एक और समृद्ध मत्स्य-क्षेत्र है।",
  NC11, "geo-ocean-currents-warm-cold", craft="linkage")

if __name__ == "__main__":
    write_updates("upg_l2_t12_geo_a.sql", statuses=("draft", "published"))
