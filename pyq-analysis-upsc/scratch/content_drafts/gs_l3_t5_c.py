# -*- coding: utf-8 -*-
"""Level 3 · Test 5 (GS Integrated Test 5) -- part C: Environment & Ecology (15) (upsc_l3_cell_targets.mjs 5).
Same cell plan as Tests 1-4.
Every fact was searched in the whole UPSC bank (l3_tools/bank_find.py) and is one no row tests: Noctiluca and the
'blue tide'; the Champion and Seth forest types; the 2025 river-dolphin estimate; parthenogenesis, delayed implantation,
magnetic sensing in birds and honeybee drones; the 2025 DNA-based elephant estimate; the Construction and Demolition Waste
Management Rules, 2025; cloud seeding and Delhi's 2025 trials; the Tropical Forest Forever Facility; the National
Environment Tribunal and Appellate Authority Acts, the Water Cess Act and section 38 of the NGT Act; 2024 as the
first year above 1.5 deg C; the ocean's pumps, upwelling and stratification; Udhwa Lake; the Ramsar criteria; the
metapopulation and the rescue effect; the IMO Net-Zero Framework. MCQ keys are pinned (pos)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Environment & Ecology"
d.REQUIRE_CRAFT = True
BIO12 = "NCERT Class XII, Biology (Organisms and Populations; Ecosystem; Biodiversity and Conservation)"
MOEF = "Ministry of Environment, Forest and Climate Change"
WII = "Wildlife Institute of India"

# ---------------------------------------------------------------- Flora, Fungi & Forests (e-MCQ, m-stmt)
M("Flora, Fungi & Forests", "easy",
  "The glowing 'blue tide' seen at night on some beaches of India's west coast is caused mainly by:",
  "भारत के पश्चिमी तट के कुछ समुद्र तटों पर रात में दिखने वाला चमकता ‘नीला ज्वार’ मुख्यतः किसके कारण होता है?",
  ["bioluminescent dinoflagellates such as Noctiluca scintillans",
   "phosphorus-bearing minerals in beach sand that glow after absorbing sunlight",
   "swarms of jellyfish that light up when stranded by the receding tide",
   "moonlight reflected from the foam that waves whip up from decaying plankton"],
  ["नॉक्टिल्यूका सिंटिलान्स जैसे जैवदीप्त डाइनोफ़्लैजेलेट",
   "समुद्र तट की रेत में फ़ॉस्फ़ोरसयुक्त खनिज जो धूप सोखने के बाद चमकते हैं",
   "जेलीफ़िश के झुंड जो उतरते ज्वार में फँसने पर चमक उठते हैं",
   "सड़ते प्लवकों से लहरों द्वारा बने झाग से परावर्तित चाँदनी"],
  0,
  "The glow is bioluminescence: Noctiluca scintillans, the 'sea sparkle', is a single-celled dinoflagellate that flashes blue when the water around it is disturbed by waves, boats or swimmers, through a reaction in which the enzyme luciferase oxidises the pigment luciferin. Dense blooms off Goa, Karnataka, Kerala and Mumbai produce the effect. "
  "The blooms are not merely a spectacle. The green form of Noctiluca, which carries algal symbionts, has spread in the Arabian Sea in winter as the sea has warmed and its waters have become poorer in oxygen and richer in nutrients, displacing the diatoms at the base of the food web and affecting fisheries.",
  "यह चमक जैवदीप्ति है: ‘सी स्पार्कल’ कहलाने वाला नॉक्टिल्यूका सिंटिलान्स एककोशिकीय डाइनोफ़्लैजेलेट है जो लहरों, नावों या तैराकों से आसपास का पानी हिलने पर नीली चमक देता है; यह उस अभिक्रिया से होता है जिसमें एंज़ाइम ल्यूसिफ़ेरेज़ वर्णक ल्यूसिफ़ेरिन का ऑक्सीकरण करता है। गोवा, कर्नाटक, केरल और मुंबई के पास घने प्रस्फुटन यह प्रभाव पैदा करते हैं। "
  "ये प्रस्फुटन केवल दृश्य नहीं हैं। नॉक्टिल्यूका का हरा रूप, जिसमें शैवाल सहजीवी रहते हैं, अरब सागर में सर्दियों में फैला है, क्योंकि समुद्र गर्म हुआ है और उसके पानी में ऑक्सीजन घटी और पोषक तत्व बढ़े हैं; यह खाद्य जाल के आधार के डायटमों को हटाता है और मत्स्य पालन को प्रभावित करता है।",
  "Indian National Centre for Ocean Information Services; National Institute of Oceanography (studies of Noctiluca blooms in the Arabian Sea).",
  "l3-t5-env-noctiluca-blue-tide", pos=0, craft="inference")

S("Flora, Fungi & Forests", "medium", "With reference to the classification of the forests of India, consider the following statements:",
  "भारत के वनों के वर्गीकरण के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["The classification of Champion and Seth divides India's forests into sixteen type groups.",
   "Tropical dry deciduous forests cover the largest area among these groups.",
   "The classification was first prepared by the Forest Survey of India in 2001."],
  ["चैंपियन और सेठ का वर्गीकरण भारत के वनों को सोलह प्रकार-समूहों में बाँटता है।",
   "इन समूहों में उष्णकटिबंधीय शुष्क पर्णपाती वन सबसे अधिक क्षेत्र में फैले हैं।",
   "यह वर्गीकरण पहली बार 2001 में भारतीय वन सर्वेक्षण ने तैयार किया था।"],
  C3, 1,
  "Statements 1 and 2 are correct. The sixteen type groups -- from tropical wet evergreen, semi-evergreen, moist deciduous, littoral and swamp, dry deciduous, thorn and dry evergreen, through the subtropical and montane groups, to the sub-alpine and the moist and dry alpine scrub -- are divided into some two hundred forest types, based on climate, soil and the dominant vegetation. The Forest Survey of India's forest-type mapping shows tropical dry deciduous forests, of teak, sal and their associates in the drier parts of the peninsula and the plains, as the most extensive group, followed by tropical moist deciduous forests. "
  "Statement 3 is wrong: H. G. Champion published the first classification in 1936, and it was revised by Champion and S. K. Seth in 1968; the Forest Survey of India, set up in 1981, uses it as the basis of its mapping. The classification matters for policy because the type of forest decides what restoration, fire management and working plans are suitable.",
  "कथन 1 और 2 सही हैं। सोलह प्रकार-समूह -- उष्णकटिबंधीय आर्द्र सदाबहार, अर्ध-सदाबहार, आर्द्र पर्णपाती, तटीय और दलदली, शुष्क पर्णपाती, कँटीले और शुष्क सदाबहार से लेकर उपोष्ण और पर्वतीय समूहों और उप-अल्पाइन तथा आर्द्र और शुष्क अल्पाइन झाड़ियों तक -- जलवायु, मिट्टी और प्रमुख वनस्पति के आधार पर लगभग दो सौ वन प्रकारों में बँटे हैं। भारतीय वन सर्वेक्षण का वन-प्रकार मानचित्रण उष्णकटिबंधीय शुष्क पर्णपाती वनों को, जो प्रायद्वीप और मैदानों के शुष्क भागों में सागौन, साल और उनके सहचरों के हैं, सबसे विस्तृत समूह दिखाता है, उसके बाद उष्णकटिबंधीय आर्द्र पर्णपाती वन आते हैं। "
  "कथन 3 ग़लत है: एच. जी. चैंपियन ने पहला वर्गीकरण 1936 में प्रकाशित किया, और 1968 में चैंपियन और एस. के. सेठ ने इसे संशोधित किया; 1981 में स्थापित भारतीय वन सर्वेक्षण इसे अपने मानचित्रण का आधार बनाता है। यह वर्गीकरण नीति के लिए महत्वपूर्ण है क्योंकि वन का प्रकार तय करता है कि कौन-सा पुनर्स्थापन, अग्नि प्रबंधन और कार्य योजना उपयुक्त है।",
  "Forest Survey of India, India State of Forest Report and Atlas of Forest Types; Champion and Seth, A Revised Survey of the Forest Types of India (1968).",
  "l3-t5-env-champion-seth-forest-types", craft="precision")

# ---------------------------------------------------------------- Fauna & Animal Behaviour (e-stmt, h-stmt, m-stmt)
S("Fauna & Animal Behaviour", "easy", "With reference to the first range-wide count of river dolphins in India, consider the following statements:",
  "भारत में नदी डॉल्फ़िनों की पहली पूरे क्षेत्र की गणना के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["It was the first range-wide estimate of river dolphins in India and put their number at about 6,300.",
   "The count included the Irrawaddy dolphins of Chilika Lake.",
   "Assam, along the Brahmaputra, recorded the largest number among the States."],
  ["यह भारत में नदी डॉल्फ़िनों का पहला पूरे क्षेत्र का आकलन था और इसने उनकी संख्या लगभग 6,300 बताई।",
   "इस गणना में चिल्का झील की इरावदी डॉल्फ़िन भी शामिल थीं।",
   "राज्यों में सबसे अधिक संख्या ब्रह्मपुत्र के किनारे असम में दर्ज हुई।"],
  C3, 0,
  "Only statement 1 is correct. The survey under Project Dolphin, conducted by the Wildlife Institute of India with State forest departments over more than 8,000 km of the Ganga, its tributaries, the Brahmaputra and the Beas, estimated 6,327 river dolphins; it was released in March 2025. Almost all were Ganges river dolphins, the only others being a handful of Indus river dolphins in the Beas in Punjab. "
  "Statement 2 is wrong: the Irrawaddy dolphin is a coastal and estuarine species, counted separately in Chilika, and was not part of this river survey. Statement 3 is wrong: Uttar Pradesh recorded the most, followed by Bihar, West Bengal and Assam. Such a baseline lets future counts show whether barrages, dredging for waterways and bycatch in fishing nets are reducing numbers.",
  "केवल कथन 1 सही है। प्रोजेक्ट डॉल्फ़िन के अंतर्गत भारतीय वन्यजीव संस्थान ने राज्य वन विभागों के साथ गंगा, उसकी सहायक नदियों, ब्रह्मपुत्र और ब्यास के 8,000 किलोमीटर से अधिक हिस्से का सर्वेक्षण किया और 6,327 नदी डॉल्फ़िनों का अनुमान लगाया; इसे मार्च 2025 में जारी किया गया। लगभग सभी गंगा नदी डॉल्फ़िन थीं, अन्य केवल पंजाब में ब्यास की कुछ सिंधु नदी डॉल्फ़िन थीं। "
  "कथन 2 ग़लत है: इरावदी डॉल्फ़िन तटीय और ज्वारनदमुखी प्रजाति है, जिसकी गणना चिल्का में अलग से होती है, और वह इस नदी सर्वेक्षण का भाग नहीं थी। कथन 3 ग़लत है: सबसे अधिक संख्या उत्तर प्रदेश में दर्ज हुई, उसके बाद बिहार, पश्चिम बंगाल और असम में। ऐसी आधार-रेखा से भावी गणनाएँ दिखा सकेंगी कि बैराज, जलमार्गों के लिए तलकर्षण और मछली पकड़ने के जालों में फँसना संख्या घटा रहे हैं या नहीं।",
  f"{WII} and {MOEF}, Population Status of River Dolphins in India (2025).",
  "l3-t5-env-river-dolphin-estimate-2025", craft="precision")

S("Fauna & Animal Behaviour", "hard", "With reference to reproduction and navigation in animals, consider the following statements:",
  "जंतुओं में प्रजनन और दिशा-निर्धारण के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Some lizards and snakes, including the Komodo dragon, can produce young by parthenogenesis, without fertilisation by a male.",
   "In delayed implantation, seen in bears, the fertilised egg does not attach to the wall of the uterus at once, so that birth falls at a favourable time.",
   "Some migratory birds are thought to sense the Earth's magnetic field, possibly through light-sensitive proteins in their eyes, and use it to hold their course.",
   "In honeybees, drones develop from fertilised eggs and workers from unfertilised ones."],
  ["कोमोडो ड्रैगन सहित कुछ छिपकलियाँ और साँप नर द्वारा निषेचन के बिना, अनिषेकजनन द्वारा संतान उत्पन्न कर सकते हैं।",
   "भालुओं में दिखने वाले विलंबित आरोपण में निषेचित अंडा तुरंत गर्भाशय की भित्ति से नहीं जुड़ता, ताकि जन्म अनुकूल समय पर हो।",
   "माना जाता है कि कुछ प्रवासी पक्षी, संभवतः अपनी आँखों के प्रकाश-संवेदी प्रोटीनों के माध्यम से, पृथ्वी के चुंबकीय क्षेत्र को महसूस करते हैं और दिशा बनाए रखने में उसका उपयोग करते हैं।",
   "मधुमक्खियों में नर (ड्रोन) निषेचित अंडों से और श्रमिक अनिषेचित अंडों से विकसित होते हैं।"],
  C4, 2,
  "Statements 1, 2 and 3 are correct. Female Komodo dragons in British zoos produced young without any male in 2006, and the same has since been recorded in several snakes and sharks; in Komodo dragons such offspring are all male because of the reptile's sex-chromosome system. In bears the blastocyst floats free for months after the summer mating and implants only when the female enters her den, so cubs are born in mid-winter and emerge in spring. Experiments with European robins and other songbirds suggest a magnetic compass based on cryptochrome proteins in the retina, in which light triggers reactions sensitive to the direction of the field; birds also navigate by the Sun, the stars and landmarks. "
  "Statement 4 is the reverse of the truth: drones develop from unfertilised eggs and are haploid, while workers and queens develop from fertilised eggs and are diploid -- a form of parthenogenesis that links statements 1 and 4, and the reason workers are more closely related to their sisters than to their own young.",
  "कथन 1, 2 और 3 सही हैं। 2006 में ब्रिटिश चिड़ियाघरों में मादा कोमोडो ड्रैगनों ने बिना किसी नर के संतान उत्पन्न की, और तब से कई साँपों और शार्कों में भी यह दर्ज हुआ है; कोमोडो ड्रैगनों में ऐसी संतान सरीसृप के लिंग-गुणसूत्र तंत्र के कारण सब नर होती है। भालुओं में गर्मियों के संभोग के बाद कोरकपुटी (ब्लास्टोसिस्ट) महीनों तक मुक्त रहती है और तभी आरोपित होती है जब मादा अपनी माँद में जाती है, इसलिए शावक मध्य-शीत में जन्म लेते हैं और वसंत में बाहर आते हैं। यूरोपीय रॉबिन और अन्य गायक पक्षियों पर प्रयोग रेटिना के क्रिप्टोक्रोम प्रोटीनों पर आधारित एक चुंबकीय दिक्सूचक का संकेत देते हैं, जिसमें प्रकाश ऐसी अभिक्रियाएँ शुरू करता है जो क्षेत्र की दिशा के प्रति संवेदनशील होती हैं; पक्षी सूर्य, तारों और भू-चिह्नों से भी दिशा पाते हैं। "
  "कथन 4 सत्य का उल्टा है: ड्रोन अनिषेचित अंडों से विकसित होते हैं और अगुणित होते हैं, जबकि श्रमिक और रानियाँ निषेचित अंडों से विकसित होती हैं और द्विगुणित होती हैं -- यह अनिषेकजनन का एक रूप है जो कथन 1 और 4 को जोड़ता है, और यही कारण है कि श्रमिक अपनी संतान की तुलना में अपनी बहनों से अधिक निकट संबंधी होती हैं।",
  BIO12 + "; Zoological Survey of India.", "l3-t5-env-parthenogenesis-delayed-implantation-magnetic", craft="linkage")

S("Fauna & Animal Behaviour", "medium", "With reference to the all-India elephant estimate released in 2025, consider the following statements:",
  "2025 में जारी अखिल भारतीय हाथी आकलन के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["It was the first such estimate to identify individual elephants from the DNA in their dung.",
   "It placed the number of wild elephants at about 22,000, with Karnataka holding the largest number among the States.",
   "It found that the north-eastern hills and the Brahmaputra floodplains hold more than half of India's wild elephants."],
  ["यह पहला ऐसा आकलन था जिसने लीद के डीएनए से अलग-अलग हाथियों की पहचान की।",
   "इसने जंगली हाथियों की संख्या लगभग 22,000 बताई, जिसमें राज्यों में सबसे अधिक संख्या कर्नाटक में थी।",
   "इसने पाया कि उत्तर-पूर्वी पहाड़ियों और ब्रह्मपुत्र के बाढ़ के मैदानों में भारत के आधे से अधिक जंगली हाथी हैं।"],
  C3, 1,
  "Statements 1 and 2 are correct. The Synchronous All India Elephant Estimation of 2021-25, by the Wildlife Institute of India under Project Elephant, genotyped dung samples to tell individuals apart and combined them in a capture-recapture model; it estimated 22,446 elephants, with Karnataka first, followed by Assam, Tamil Nadu and Kerala. The method differs from the earlier direct and dung-decay counts, so the figure is a new baseline rather than proof of a fall from the 2017 count of about 27,000. "
  "Statement 3 is wrong: the Western Ghats hold more than half -- nearly 12,000 -- while the north-eastern hills and Brahmaputra plains hold about 6,500, the Shivalik hills and Gangetic plains about 2,000, and central India and the Eastern Ghats under 2,000. The report flags fragmented habitat and rising human-elephant conflict in central India, where herds have moved into new areas, as the main threats.",
  "कथन 1 और 2 सही हैं। प्रोजेक्ट एलिफ़ैंट के अंतर्गत भारतीय वन्यजीव संस्थान के 2021-25 के समकालिक अखिल भारतीय हाथी आकलन ने अलग-अलग हाथियों को पहचानने के लिए लीद के नमूनों का जीनोटाइपिंग किया और उन्हें कैप्चर-रिकैप्चर मॉडल में जोड़ा; इसने 22,446 हाथियों का अनुमान लगाया, जिसमें कर्नाटक पहले स्थान पर था, उसके बाद असम, तमिलनाडु और केरल। यह विधि पहले की प्रत्यक्ष और लीद-क्षय गणनाओं से भिन्न है, इसलिए यह आँकड़ा 2017 की लगभग 27,000 की गणना से गिरावट का प्रमाण होने के बजाय एक नई आधार-रेखा है। "
  "कथन 3 ग़लत है: पश्चिमी घाट में आधे से अधिक -- लगभग 12,000 -- हाथी हैं, जबकि उत्तर-पूर्वी पहाड़ियों और ब्रह्मपुत्र के मैदानों में लगभग 6,500, शिवालिक पहाड़ियों और गंगा के मैदानों में लगभग 2,000, और मध्य भारत तथा पूर्वी घाट में 2,000 से कम हैं। रिपोर्ट खंडित आवास और मध्य भारत में बढ़ते मानव-हाथी संघर्ष को, जहाँ झुंड नए क्षेत्रों में चले गए हैं, मुख्य ख़तरे बताती है।",
  f"{WII} and {MOEF} (Project Elephant), Status of Elephants in India: DNA-based Synchronous All India Population Estimation of Elephants, 2021-25.",
  "l3-t5-env-elephant-dna-estimate-2025", craft="inference")

# ---------------------------------------------------------------- Pollution, Waste & Resources (e-stmt, m-stmt)
S("Pollution, Waste & Resources", "easy", "With reference to the Environment (Construction and Demolition) Waste Management Rules, 2025, consider the following statements:",
  "पर्यावरण (निर्माण और विध्वंस) अपशिष्ट प्रबंधन नियम, 2025 के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["They make the producers of such waste -- builders and developers of large projects -- responsible for managing it.",
   "They introduce Extended Producer Responsibility, with targets for using recycled construction and demolition material in new construction."],
  ["ये ऐसे अपशिष्ट के उत्पादकों -- बड़ी परियोजनाओं के निर्माताओं और विकासकर्ताओं -- को उसके प्रबंधन के लिए उत्तरदायी बनाते हैं।",
   "ये विस्तारित उत्पादक उत्तरदायित्व लाते हैं, जिसमें नए निर्माण में पुनर्चक्रित निर्माण और विध्वंस सामग्री के उपयोग के लक्ष्य हैं।"],
  T2, 2,
  "Both statements are correct. The rules, notified under the Environment (Protection) Act, replace the Construction and Demolition Waste Management Rules of 2016 and take effect from April 2026. They shift responsibility to the producer: large builders must register on a central portal run by the Central Pollution Control Board, segregate and recycle the waste, and meet rising year-by-year targets for using recycled material, with environmental compensation for shortfalls. "
  "Construction and demolition debris is one of the largest waste streams in Indian cities and a major source of road dust and of illegal dumping in wetlands and floodplains, so the rules link waste policy to air quality and to the demand for sand and aggregates.",
  "दोनों कथन सही हैं। पर्यावरण (संरक्षण) अधिनियम के अंतर्गत अधिसूचित ये नियम 2016 के निर्माण और विध्वंस अपशिष्ट प्रबंधन नियमों का स्थान लेते हैं और अप्रैल 2026 से लागू होते हैं। ये उत्तरदायित्व उत्पादक पर डालते हैं: बड़े निर्माताओं को केंद्रीय प्रदूषण नियंत्रण बोर्ड द्वारा चलाए जाने वाले केंद्रीय पोर्टल पर पंजीकरण करना, अपशिष्ट को अलग करना और पुनर्चक्रित करना, और पुनर्चक्रित सामग्री के उपयोग के वर्ष-दर-वर्ष बढ़ते लक्ष्यों को पूरा करना होगा, कमी पर पर्यावरणीय क्षतिपूर्ति देनी होगी। "
  "निर्माण और विध्वंस का मलबा भारतीय शहरों के सबसे बड़े अपशिष्ट प्रवाहों में से एक है और सड़क की धूल तथा आर्द्रभूमियों और बाढ़ के मैदानों में अवैध डंपिंग का बड़ा स्रोत है, इसलिए ये नियम अपशिष्ट नीति को वायु गुणवत्ता और रेत तथा गिट्टी की माँग से जोड़ते हैं।",
  f"{MOEF}, Environment (Construction and Demolition) Waste Management Rules, 2025.",
  "l3-t5-env-construction-demolition-waste-rules-2025", craft="recall")

S("Pollution, Waste & Resources", "medium", "With reference to cloud seeding, which has been tried as a way of washing pollutants out of the air, consider the following statements:",
  "मेघ बीजन (क्लाउड सीडिंग) के संदर्भ में, जिसे हवा से प्रदूषकों को धोने के उपाय के रूप में आज़माया गया है, निम्नलिखित कथनों पर विचार कीजिए:",
  ["It usually disperses particles of silver iodide or salt into clouds, to act as nuclei on which droplets or ice crystals can grow.",
   "It can produce rain even from a clear sky, provided the air is dry and still.",
   "Delhi's trials in 2025 were carried out with aircraft under a project with IIT Kanpur."],
  ["इसमें सामान्यतः बादलों में सिल्वर आयोडाइड या नमक के कण बिखेरे जाते हैं, ताकि वे ऐसे नाभिक बनें जिन पर बूँदें या हिम-क्रिस्टल बढ़ सकें।",
   "यह साफ़ आकाश से भी वर्षा करा सकता है, बशर्ते हवा शुष्क और स्थिर हो।",
   "दिल्ली के 2025 के परीक्षण आईआईटी कानपुर के साथ एक परियोजना के अंतर्गत विमानों से किए गए।"],
  C3, 1,
  "Statements 1 and 3 are correct. Seeding works only on clouds that already hold enough moisture: silver iodide, whose crystal structure resembles ice, helps supercooled droplets freeze in cold clouds, while hygroscopic salts help droplets grow in warm clouds, so that more of the cloud's water falls as rain. Delhi's government and IIT Kanpur flew seeding sorties in October 2025, firing flares over parts of the city. "
  "Statement 2 is wrong: seeding cannot create clouds or rain from dry air -- which is why Delhi's winter trials produced little or no rain, as the clouds were thin and the humidity low. Even when it succeeds, any rain clears particulate matter only briefly, so the method is no substitute for cutting emissions from vehicles, industry, construction dust and crop-residue burning.",
  "कथन 1 और 3 सही हैं। बीजन केवल उन्हीं बादलों पर काम करता है जिनमें पहले से पर्याप्त नमी हो: सिल्वर आयोडाइड, जिसकी क्रिस्टल संरचना बर्फ़ जैसी है, ठंडे बादलों में अतिशीतित बूँदों को जमने में मदद करता है, जबकि आर्द्रताग्राही लवण गर्म बादलों में बूँदों को बढ़ने में मदद करते हैं, ताकि बादल का अधिक पानी वर्षा के रूप में गिरे। दिल्ली सरकार और आईआईटी कानपुर ने अक्टूबर 2025 में शहर के कुछ भागों पर फ़्लेयर दाग़कर बीजन उड़ानें भरीं। "
  "कथन 2 ग़लत है: बीजन शुष्क हवा से बादल या वर्षा नहीं बना सकता -- इसीलिए दिल्ली के शीतकालीन परीक्षणों से बहुत कम या कोई वर्षा नहीं हुई, क्योंकि बादल पतले और आर्द्रता कम थी। सफल होने पर भी वर्षा कणीय पदार्थ को थोड़े समय के लिए ही साफ़ करती है, इसलिए यह विधि वाहनों, उद्योग, निर्माण की धूल और फ़सल अवशेष जलाने से होने वाले उत्सर्जन को घटाने का विकल्प नहीं है।",
  "India Meteorological Department and Indian Institute of Tropical Meteorology (CAIPEEX cloud-seeding experiment); Government of NCT of Delhi and IIT Kanpur (2025 trials).",
  "l3-t5-env-cloud-seeding-delhi-2025", craft="application")

# ---------------------------------------------------------------- International Conventions & Organisations (h-SI)
A("International Conventions & Organisations", "hard",
  "The Tropical Forest Forever Facility, launched in Belem in November 2025, is meant to reward tropical forest countries for keeping their forests standing.",
  "नवंबर 2025 में बेलेम में शुरू की गई ट्रॉपिकल फ़ॉरेस्ट फ़ॉरएवर फ़ैसिलिटी का उद्देश्य उष्णकटिबंधीय वन वाले देशों को अपने वन खड़े रखने के लिए पुरस्कृत करना है।",
  "Its payments are calculated per hectare of forest retained, with deductions for every hectare that is deforested or degraded.",
  "इसके भुगतान बचाए गए वन के प्रति हेक्टेयर के आधार पर तय होते हैं, और कटे या क्षरित हर हेक्टेयर के लिए कटौती होती है।",
  0,
  "Both statements are correct and Statement II explains Statement I. Brazil proposed the facility and launched it at the leaders' summit held in Belem on the eve of COP30. Unlike REDD+, which pays for measured reductions in emissions against a baseline, it is designed as an investment fund: money from sponsor governments and private investors is to be invested, and the surplus returns paid each year to countries for every hectare of tropical forest kept standing, as verified by satellite. "
  "Large deductions for each hectare cleared or degraded make keeping forests more valuable than clearing them, and a fifth of the payments is to go to Indigenous peoples and local communities. The World Bank serves as trustee. Its success depends on raising enough capital and on investment returns, which is the main criticism of the design.",
  "दोनों कथन सही हैं और कथन II, कथन I की व्याख्या करता है। ब्राज़ील ने इस सुविधा का प्रस्ताव रखा और इसे कॉप30 की पूर्व संध्या पर बेलेम में हुए नेताओं के शिखर सम्मेलन में शुरू किया। रेड+ (REDD+) के विपरीत, जो आधार-रेखा की तुलना में उत्सर्जन में मापी गई कमी के लिए भुगतान करता है, इसे एक निवेश कोष के रूप में बनाया गया है: प्रायोजक सरकारों और निजी निवेशकों का धन निवेश किया जाना है, और अतिरिक्त प्रतिफल हर वर्ष देशों को उपग्रह से सत्यापित खड़े उष्णकटिबंधीय वन के हर हेक्टेयर के लिए दिया जाना है। "
  "कटे या क्षरित हर हेक्टेयर के लिए बड़ी कटौतियाँ वनों को काटने की तुलना में बचाए रखना अधिक मूल्यवान बनाती हैं, और भुगतान का पाँचवाँ हिस्सा मूलनिवासी लोगों और स्थानीय समुदायों को जाना है। विश्व बैंक न्यासी है। इसकी सफलता पर्याप्त पूँजी जुटाने और निवेश प्रतिफल पर निर्भर है, और यही इस रूपरेखा की मुख्य आलोचना है।",
  "UNFCCC COP30 (Belem, 2025), Tropical Forest Forever Facility concept note; World Bank (trustee).",
  "l3-t5-env-tropical-forest-forever-facility", craft="inference")

# ---------------------------------------------------------------- Indian Environmental Laws & Bodies (h-pairs)
P("Indian Environmental Laws & Bodies", "hard", "Consider the following pairs of laws and what they provided:",
  "क़ानूनों और उनमें किए गए उपबंधों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["National Environment Tribunal Act, 1995 : Strict liability for damage from accidents involving hazardous substances",
   "National Environment Appellate Authority Act, 1997 : Appeals against the grant of environmental clearance",
   "Water (Prevention and Control of Pollution) Cess Act, 1977 : A cess on water consumed by certain industries and local authorities",
   "National Green Tribunal Act, 2010 : Kept both the Tribunal of 1995 and the Authority of 1997 alongside the new Tribunal"],
  ["राष्ट्रीय पर्यावरण अधिकरण अधिनियम, 1995 : परिसंकटमय पदार्थों से जुड़ी दुर्घटनाओं से हुई क्षति के लिए कठोर दायित्व",
   "राष्ट्रीय पर्यावरण अपील प्राधिकरण अधिनियम, 1997 : पर्यावरणीय स्वीकृति दिए जाने के विरुद्ध अपीलें",
   "जल (प्रदूषण निवारण और नियंत्रण) उपकर अधिनियम, 1977 : कुछ उद्योगों और स्थानीय प्राधिकरणों द्वारा उपभोग किए गए जल पर उपकर",
   "राष्ट्रीय हरित अधिकरण अधिनियम, 2010 : 1995 के अधिकरण और 1997 के प्राधिकरण दोनों को नए अधिकरण के साथ बनाए रखा"],
  2,
  "The first three pairs are correct. The 1995 Act, passed after the Bhopal gas disaster, provided for strict liability -- compensation without proof of negligence -- and a tribunal to decide claims, though the tribunal was never set up. The 1997 Act created an authority to hear appeals against environmental clearances. The 1977 Cess Act levied a cess on water consumed by specified industries and local authorities to fund the pollution control boards; it was repealed in 2017 when the tax was folded into GST. "
  "The fourth pair is wrong: section 38 of the National Green Tribunal Act repealed both the 1995 and the 1997 Acts, and the Tribunal took over their work, deciding civil cases with a substantial question relating to the environment under the seven laws in its Schedule I and applying the principles of sustainable development, the precautionary principle and 'polluter pays'.",
  "पहले तीन युग्म सही हैं। भोपाल गैस त्रासदी के बाद पारित 1995 के अधिनियम ने कठोर दायित्व -- लापरवाही सिद्ध किए बिना क्षतिपूर्ति -- और दावों के निर्णय के लिए एक अधिकरण का उपबंध किया, हालाँकि अधिकरण कभी स्थापित नहीं हुआ। 1997 के अधिनियम ने पर्यावरणीय स्वीकृतियों के विरुद्ध अपीलें सुनने के लिए एक प्राधिकरण बनाया। 1977 के उपकर अधिनियम ने प्रदूषण नियंत्रण बोर्डों के वित्तपोषण के लिए विनिर्दिष्ट उद्योगों और स्थानीय प्राधिकरणों द्वारा उपभोग किए गए जल पर उपकर लगाया; 2017 में जब यह कर जीएसटी में मिला दिया गया, तब इसे निरसित कर दिया गया। "
  "चौथा युग्म ग़लत है: राष्ट्रीय हरित अधिकरण अधिनियम की धारा 38 ने 1995 और 1997 दोनों अधिनियमों को निरसित किया, और अधिकरण ने उनका काम सँभाला; यह अपनी अनुसूची I के सात क़ानूनों के अंतर्गत पर्यावरण से जुड़े सारवान प्रश्न वाले सिविल मामलों का निर्णय करता है और सतत विकास, एहतियाती सिद्धांत और ‘प्रदूषक भुगतान करे’ के सिद्धांत लागू करता है।",
  "National Environment Tribunal Act, 1995; National Environment Appellate Authority Act, 1997; Water (Prevention and Control of Pollution) Cess Act, 1977; National Green Tribunal Act, 2010, sections 14, 20 and 38.",
  "l3-t5-env-net-neaa-water-cess-ngt-repeal", craft="linkage")

# ---------------------------------------------------------------- Climate Science & Mitigation (m-MCQ, m-stmt)
M("Climate Science & Mitigation", "medium",
  "The World Meteorological Organization reported that 2024 was the first calendar year in which the global average temperature was more than 1.5 deg C above the pre-industrial level. Which one of the following statements about this finding is correct?",
  "विश्व मौसम विज्ञान संगठन ने बताया कि 2024 पहला कैलेंडर वर्ष था जिसमें वैश्विक औसत तापमान पूर्व-औद्योगिक स्तर से 1.5 डिग्री सेल्सियस से अधिक रहा। इस निष्कर्ष के बारे में निम्नलिखित में से कौन-सा कथन सही है?",
  ["The Paris Agreement's 1.5 deg C limit has been formally breached and the Agreement must now be renegotiated",
   "The record warmth was caused mainly by a strong La Nina event that released heat from the Pacific Ocean",
   "The figure compares 2024 with the average temperature of 1991-2020 rather than with pre-industrial times",
   "The goal refers to long-term average warming, so one year above 1.5 deg C does not by itself breach it"],
  ["पेरिस समझौते की 1.5 डिग्री सेल्सियस की सीमा औपचारिक रूप से टूट गई है और अब समझौते पर फिर से वार्ता करनी होगी",
   "यह रिकॉर्ड गर्मी मुख्यतः एक प्रबल ला नीना घटना से हुई जिसने प्रशांत महासागर से ऊष्मा मुक्त की",
   "यह आँकड़ा 2024 की तुलना पूर्व-औद्योगिक काल के बजाय 1991-2020 के औसत तापमान से करता है",
   "लक्ष्य दीर्घकालिक औसत तापवृद्धि से संबंधित है, इसलिए 1.5 डिग्री से ऊपर एक वर्ष अपने आप में इसे नहीं तोड़ता"],
  3,
  "The WMO's consolidated figure for 2024 was about 1.55 deg C above the 1850-1900 average, the warmest year on record, pushed up by the long-term trend and by the El Nino of 2023-24 (a La Nina usually cools the globe). The Paris goal of holding warming to 1.5 deg C refers to warming averaged over about twenty years, which the WMO put at about 1.3 to 1.4 deg C; one year above the line is therefore a warning, not a breach. "
  "The IPCC's assessment is that, at current emission rates, the long-term average is likely to cross 1.5 deg C around the early 2030s, which is why the size of the remaining carbon budget, now only a few years of present emissions, dominates the negotiations.",
  "डब्ल्यूएमओ के समेकित आँकड़े के अनुसार 2024 का तापमान 1850-1900 के औसत से लगभग 1.55 डिग्री सेल्सियस अधिक था, जो अब तक का सबसे गर्म वर्ष था; इसे दीर्घकालिक प्रवृत्ति और 2023-24 के एल नीनो ने ऊपर धकेला (ला नीना सामान्यतः पृथ्वी को ठंडा करती है)। तापवृद्धि को 1.5 डिग्री तक रोकने का पेरिस लक्ष्य लगभग बीस वर्षों के औसत से संबंधित है, जिसे डब्ल्यूएमओ ने लगभग 1.3 से 1.4 डिग्री आँका; इसलिए रेखा के ऊपर एक वर्ष चेतावनी है, उल्लंघन नहीं। "
  "आईपीसीसी का आकलन है कि वर्तमान उत्सर्जन दर पर दीर्घकालिक औसत 2030 के दशक के आरंभ के आसपास 1.5 डिग्री पार कर सकता है, इसीलिए शेष कार्बन बजट का आकार, जो अब वर्तमान उत्सर्जन के कुछ ही वर्षों के बराबर है, वार्ताओं में सबसे प्रमुख है।",
  "World Meteorological Organization, State of the Global Climate 2024; IPCC Sixth Assessment Report.",
  "l3-t5-env-2024-first-year-above-1-5", pos=3, craft="inference")

S("Climate Science & Mitigation", "medium", "With reference to the ocean's exchange of carbon dioxide with the atmosphere, consider the following statements:",
  "महासागर और वायुमंडल के बीच कार्बन डाइऑक्साइड के आदान-प्रदान के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Cold high-latitude waters take up more carbon dioxide, since gases dissolve better in cold water, and their sinking carries it to the deep ocean.",
   "The biological pump moves carbon to depth as organic matter from phytoplankton and other organisms sinks.",
   "In upwelling regions such as the eastern equatorial Pacific, deep water rich in carbon dioxide releases some of it to the atmosphere.",
   "Warming and stronger layering of the upper ocean are expected to weaken the ocean's uptake of carbon dioxide over time."],
  ["ठंडे उच्च-अक्षांशीय जल अधिक कार्बन डाइऑक्साइड सोखते हैं, क्योंकि गैसें ठंडे पानी में बेहतर घुलती हैं, और उनका डूबना इसे गहरे महासागर तक ले जाता है।",
   "जैविक पंप पादप-प्लवकों और अन्य जीवों के कार्बनिक पदार्थ के डूबने से कार्बन को गहराई तक ले जाता है।",
   "पूर्वी विषुवतीय प्रशांत जैसे उत्प्रवाह (अपवेलिंग) क्षेत्रों में कार्बन डाइऑक्साइड से समृद्ध गहरा जल उसका कुछ भाग वायुमंडल में छोड़ता है।",
   "तापवृद्धि और ऊपरी महासागर का अधिक स्तरीकरण समय के साथ महासागर द्वारा कार्बन डाइऑक्साइड के अवशोषण को कमज़ोर करेंगे, ऐसी अपेक्षा है।"],
  C4, 3,
  "All four are correct. The 'solubility pump' works because carbon dioxide is more soluble in cold water: dense, cold waters of the North Atlantic and the Southern Ocean absorb it and sink, locking it away for centuries. The 'biological pump' carries carbon fixed by phytoplankton downward as dead cells, faecal pellets and 'marine snow', a small fraction reaching the sea floor. The ocean is therefore a patchwork of sinks and sources: where upwelling brings old, carbon-rich deep water to the warm surface, as along the equatorial Pacific and off Peru, carbon dioxide escapes to the air. "
  "Warming reduces the solubility of the gas, and a more strongly layered ocean mixes less, slowing the transfer of carbon to depth and the return of nutrients that feed phytoplankton; models therefore project that the ocean will take up a smaller fraction of emissions as warming proceeds -- one reason carbon budgets cannot count on today's sinks lasting.",
  "चारों कथन सही हैं। ‘विलेयता पंप’ इसलिए काम करता है कि कार्बन डाइऑक्साइड ठंडे पानी में अधिक घुलनशील है: उत्तरी अटलांटिक और दक्षिणी महासागर का घना, ठंडा जल इसे सोखकर डूबता है और इसे सदियों के लिए बंद कर देता है। ‘जैविक पंप’ पादप-प्लवकों द्वारा स्थिर किए गए कार्बन को मृत कोशिकाओं, मल-गोलियों और ‘समुद्री हिम’ के रूप में नीचे ले जाता है, जिसका छोटा अंश समुद्र तल तक पहुँचता है। इसलिए महासागर सिंक और स्रोतों का मिश्रण है: जहाँ उत्प्रवाह पुराने, कार्बन-समृद्ध गहरे जल को गर्म सतह पर लाता है, जैसे विषुवतीय प्रशांत और पेरू के पास, वहाँ कार्बन डाइऑक्साइड हवा में निकलती है। "
  "तापवृद्धि गैस की विलेयता घटाती है, और अधिक स्तरित महासागर कम मिश्रित होता है, जिससे कार्बन का गहराई तक जाना और पादप-प्लवकों को पोषण देने वाले पोषक तत्वों का लौटना धीमा होता है; इसलिए मॉडल अनुमान लगाते हैं कि तापवृद्धि के साथ महासागर उत्सर्जन का छोटा अंश सोखेगा -- यह एक कारण है कि कार्बन बजट आज के सिंकों के बने रहने पर भरोसा नहीं कर सकते।",
  "IPCC Sixth Assessment Report, Working Group I, Chapter 5 (Global Carbon and other Biogeochemical Cycles); " + "Global Carbon Project, Global Carbon Budget.",
  "l3-t5-env-ocean-pumps-upwelling-stratification", craft="linkage")

# ---------------------------------------------------------------- Protected Areas & Wildlife Protection (m-MCQ, m-stmt)
M("Protected Areas & Wildlife Protection", "medium",
  "Which one of the following wetlands, all designated as Ramsar sites in 2025, is in Jharkhand?",
  "निम्नलिखित आर्द्रभूमियों में से, जो सभी 2025 में रामसर स्थल घोषित हुईं, कौन-सी झारखंड में है?",
  ["Khecheopalri Lake", "Menar", "Therthangal", "Udhwa Lake"],
  ["खेचियोपलरी झील", "मेनार", "तेर्थांगल", "उधवा झील"],
  3,
  "Udhwa Lake Bird Sanctuary, in Sahibganj district on the Ganga floodplain, became Jharkhand's first Ramsar site in 2025; its two connected lakes, Pataura and Berhale, draw large numbers of wintering waterbirds. "
  "The others are from different States: Khecheopalri, a lake sacred to Buddhists and Hindus, is in Sikkim; Menar, the 'bird village' near Udaipur where villagers protect the ponds, is in Rajasthan; and Therthangal, with Sakkarakottai, is a bird sanctuary in Ramanathapuram district of Tamil Nadu, the State with the largest number of Ramsar sites. The 2025 additions took India's total past ninety.",
  "साहिबगंज ज़िले में गंगा के बाढ़ के मैदान पर स्थित उधवा झील पक्षी विहार 2025 में झारखंड का पहला रामसर स्थल बना; इसकी दो जुड़ी झीलें, पतौड़ा और बरहले, बड़ी संख्या में शीतकालीन जलपक्षियों को आकर्षित करती हैं। "
  "अन्य दूसरे राज्यों की हैं: बौद्धों और हिंदुओं के लिए पवित्र खेचियोपलरी झील सिक्किम में है; उदयपुर के पास ‘पक्षी गाँव’ मेनार, जहाँ ग्रामीण तालाबों की रक्षा करते हैं, राजस्थान में है; और सक्करकोट्टई के साथ तेर्थांगल तमिलनाडु के रामनाथपुरम ज़िले का पक्षी विहार है, वह राज्य जिसमें सबसे अधिक रामसर स्थल हैं। 2025 के जुड़ावों से भारत की कुल संख्या नब्बे के पार चली गई।",
  f"{MOEF} (PIB releases on new Ramsar sites, 2025); Ramsar Sites Information Service.",
  "l3-t5-env-udhwa-lake-ramsar-jharkhand", pos=3, craft="recall")

S("Protected Areas & Wildlife Protection", "medium", "With reference to the criteria for designating a Wetland of International Importance under the Ramsar Convention, consider the following statements:",
  "रामसर अभिसमय के अंतर्गत अंतरराष्ट्रीय महत्व की आर्द्रभूमि घोषित करने के मानदंडों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["A wetland can qualify if it regularly supports 20,000 or more waterbirds.",
   "A wetland can qualify if it regularly supports one per cent of the individuals in a population of one species or subspecies of waterbird.",
   "A wetland must already be a protected area under national law before it can be designated."],
  ["कोई आर्द्रभूमि योग्य हो सकती है यदि वह नियमित रूप से 20,000 या अधिक जलपक्षियों को आश्रय देती हो।",
   "कोई आर्द्रभूमि योग्य हो सकती है यदि वह नियमित रूप से किसी जलपक्षी प्रजाति या उप-प्रजाति की एक आबादी के एक प्रतिशत सदस्यों को आश्रय देती हो।",
   "किसी आर्द्रभूमि को घोषित करने से पहले उसका राष्ट्रीय क़ानून के अंतर्गत संरक्षित क्षेत्र होना आवश्यक है।"],
  C3, 1,
  "Statements 1 and 2 are correct; they are Criteria 5 and 6 of the nine criteria. The others cover rare or unique wetland types (Criterion 1), threatened species and ecological communities (2), biodiversity of a region (3), critical stages of life cycles such as breeding or moulting (4), fish diversity and fish spawning, nursery or migration routes (7 and 8), and one per cent of a population of a wetland-dependent non-avian animal (9). A site needs to meet only one criterion. "
  "Statement 3 is wrong: the Convention does not require prior legal protection, and many Ramsar sites, including community-managed wetlands, are not national parks or sanctuaries. Designation commits the country to 'wise use' and to maintaining the site's ecological character; in India, wetlands are regulated under the Wetlands (Conservation and Management) Rules, 2017, whether or not they are protected areas.",
  "कथन 1 और 2 सही हैं; ये नौ मानदंडों में से मानदंड 5 और 6 हैं। अन्य मानदंड दुर्लभ या अनूठे आर्द्रभूमि प्रकारों (मानदंड 1), संकटग्रस्त प्रजातियों और पारिस्थितिक समुदायों (2), किसी क्षेत्र की जैव विविधता (3), प्रजनन या पंख झड़ने जैसे जीवन-चक्र के महत्वपूर्ण चरणों (4), मछलियों की विविधता और उनके अंडे देने, पालन या प्रवास मार्गों (7 और 8), और आर्द्रभूमि पर निर्भर किसी गैर-पक्षी जंतु की आबादी के एक प्रतिशत (9) से संबंधित हैं। किसी स्थल को केवल एक मानदंड पूरा करना होता है। "
  "कथन 3 ग़लत है: अभिसमय पहले से क़ानूनी संरक्षण की अपेक्षा नहीं करता, और समुदाय-प्रबंधित आर्द्रभूमियों सहित अनेक रामसर स्थल राष्ट्रीय उद्यान या अभयारण्य नहीं हैं। घोषणा देश को ‘विवेकपूर्ण उपयोग’ और स्थल के पारिस्थितिक स्वरूप को बनाए रखने के लिए प्रतिबद्ध करती है; भारत में आर्द्रभूमियाँ, संरक्षित क्षेत्र हों या न हों, आर्द्रभूमि (संरक्षण और प्रबंधन) नियम, 2017 के अंतर्गत विनियमित होती हैं।",
  "Ramsar Convention Secretariat, Criteria for Identifying Wetlands of International Importance; " + MOEF + ", Wetlands (Conservation and Management) Rules, 2017.",
  "l3-t5-env-ramsar-criteria", craft="precision")

# ---------------------------------------------------------------- Ecosystems & Ecological Processes (m-stmt)
S("Ecosystems & Ecological Processes", "medium", "With reference to metapopulations, consider the following statements:",
  "मेटापॉपुलेशन (उप-आबादियों के समूह) के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["A metapopulation is a set of spatially separate populations of a species, linked by the occasional movement of individuals between them.",
   "A local population that goes extinct within a metapopulation cannot be re-established without human help.",
   "The 'rescue effect' refers to the recovery of a population after a predator has been removed from its habitat."],
  ["मेटापॉपुलेशन किसी प्रजाति की स्थानिक रूप से अलग आबादियों का समूह है, जो उनके बीच सदस्यों के कभी-कभार आवागमन से जुड़ी होती हैं।",
   "मेटापॉपुलेशन के भीतर विलुप्त हुई कोई स्थानीय आबादी मानवीय सहायता के बिना फिर से स्थापित नहीं हो सकती।",
   "‘रेस्क्यू इफ़ेक्ट’ का अर्थ है किसी आवास से शिकारी हटाए जाने के बाद आबादी का पुनः बढ़ना।"],
  C3, 0,
  "Only statement 1 is correct. The idea, formalised by Richard Levins in 1969, treats a species in a fragmented landscape as a network of patches: local populations wink out and patches are recolonised by dispersers from occupied ones, so the species can persist regionally even though each local population is short-lived. Statement 2 is wrong for that very reason -- natural recolonisation is the defining process. "
  "Statement 3 is wrong: the rescue effect is the prevention of a local extinction by immigrants arriving from other patches, which bolster numbers and genetic diversity. The concept explains why conservationists insist on corridors between protected areas -- for tigers in central India, for instance -- since a reserve cut off from others loses both recolonisation and rescue, however well it is guarded.",
  "केवल कथन 1 सही है। 1969 में रिचर्ड लेविंस द्वारा औपचारिक रूप दिया गया यह विचार खंडित भूदृश्य में किसी प्रजाति को टुकड़ों के जाल के रूप में देखता है: स्थानीय आबादियाँ मिटती हैं और भरे हुए टुकड़ों से आए प्रवासी ख़ाली टुकड़ों को फिर बसाते हैं, इसलिए प्रजाति क्षेत्रीय स्तर पर बनी रह सकती है, भले ही हर स्थानीय आबादी अल्पकालिक हो। कथन 2 इसी कारण ग़लत है -- प्राकृतिक पुनर्वास ही इसकी पहचान है। "
  "कथन 3 ग़लत है: रेस्क्यू इफ़ेक्ट दूसरे टुकड़ों से आने वाले प्रवासियों द्वारा किसी स्थानीय विलोपन को रोकना है, जो संख्या और आनुवंशिक विविधता दोनों बढ़ाते हैं। यह अवधारणा बताती है कि संरक्षणवादी संरक्षित क्षेत्रों के बीच गलियारों पर क्यों ज़ोर देते हैं -- उदाहरण के लिए मध्य भारत में बाघों के लिए -- क्योंकि दूसरों से कटा कोई अभयारण्य, चाहे कितनी भी अच्छी तरह संरक्षित हो, पुनर्वास और बचाव दोनों खो देता है।",
  BIO12 + "; " + WII + ", connectivity and corridor studies.", "l3-t5-env-metapopulation-rescue-effect", craft="application")

# ---------------------------------------------------------------- Climate Agreements & Carbon Markets (m-stmt)
S("Climate Agreements & Carbon Markets", "medium", "With reference to the Net-Zero Framework of the International Maritime Organization (IMO), consider the following statements:",
  "अंतरराष्ट्रीय समुद्री संगठन (आईएमओ) के नेट-ज़ीरो फ़्रेमवर्क के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["It was formally adopted by the IMO's member States in October 2025.",
   "It would apply only to ships flying the flags of developed countries."],
  ["इसे आईएमओ के सदस्य देशों ने अक्टूबर 2025 में औपचारिक रूप से अपनाया।",
   "यह केवल विकसित देशों के ध्वज वाले जहाज़ों पर लागू होगा।"],
  T2, 3,
  "Neither statement is correct. The framework, approved in draft as amendments to Annex VI of MARPOL in April 2025, combines a global fuel standard -- a falling limit on the greenhouse-gas intensity of the fuel ships use -- with a global pricing mechanism under which ships that exceed the limits must buy remedial units, the money going to an IMO Net-Zero Fund. It would be the first mandatory emissions price applied across an entire industry worldwide. "
  "Statement 1 is wrong: at the extraordinary session called in October 2025 to adopt it, member States voted to adjourn for a year, after strong opposition from some States. Statement 2 is wrong: it would cover large ocean-going ships above 5,000 gross tonnage, which account for most of the sector's emissions, whatever flag they fly -- shipping, like aviation, is outside national targets under the Paris Agreement, which is why it needs a sectoral regime.",
  "कोई भी कथन सही नहीं है। अप्रैल 2025 में मारपोल के अनुलग्नक VI में संशोधनों के रूप में मसौदे में स्वीकृत यह फ़्रेमवर्क एक वैश्विक ईंधन मानक -- जहाज़ों द्वारा प्रयुक्त ईंधन की ग्रीनहाउस-गैस तीव्रता पर घटती सीमा -- को एक वैश्विक मूल्य-निर्धारण तंत्र से जोड़ता है, जिसके अंतर्गत सीमाएँ पार करने वाले जहाज़ों को उपचारात्मक इकाइयाँ ख़रीदनी होंगी और धन आईएमओ नेट-ज़ीरो फ़ंड में जाएगा। यह पूरे उद्योग पर विश्व स्तर पर लागू पहला अनिवार्य उत्सर्जन मूल्य होगा। "
  "कथन 1 ग़लत है: अक्टूबर 2025 में इसे अपनाने के लिए बुलाए गए विशेष सत्र में, कुछ देशों के कड़े विरोध के बाद, सदस्य देशों ने एक वर्ष के लिए स्थगन के पक्ष में मत दिया। कथन 2 ग़लत है: यह 5,000 सकल टन भार से बड़े समुद्री जहाज़ों पर लागू होगा, जो क्षेत्र के अधिकांश उत्सर्जन के लिए उत्तरदायी हैं, चाहे उनका ध्वज कोई भी हो -- विमानन की तरह जहाज़रानी भी पेरिस समझौते के अंतर्गत राष्ट्रीय लक्ष्यों से बाहर है, इसीलिए इसके लिए क्षेत्रीय व्यवस्था चाहिए।",
  "International Maritime Organization, MEPC 83 (April 2025) and the extraordinary session of October 2025; MARPOL Annex VI.",
  "l3-t5-env-imo-net-zero-framework", craft="precision")

write("gs_l3_t5_c.sql")
