# -*- coding: utf-8 -*-
"""Level 2 · Test 21 (GS Comprehensive Revision, full syllabus) -- Environment block (15 of the paper's 84 static rows).
  Fauna 3, Protected Areas 2, Flora 2, Pollution 2, Climate Science 2, Conventions 1, Laws 1, Climate Agreements 1,
  Ecosystems 1.
  Cells: medium statement 6, easy statement 2, hard statement 2, medium MCQ 2, easy MCQ 1, medium Statement-I/II 1,
    hard pairs 1.
Tests 9-11 hold the COP basics, NCQG, loss and damage, the global stocktake, Article 6, Kyoto/CDM, GCF/Adaptation Fund,
GEF, Kigali/Montreal, JETP, Glasgow and other climate initiatives, the Green Credit Programme, BBNJ, the natural WHS
list, hangul/Dachigam, hoolock, sangai, Silent Valley, Kaziranga, Ramsar basics, Chilika, sandalwood, seagrass,
mycorrhiza, insectivorous plants, Neelakurinji, decomposition and food chains, pyramids, niches, r/K selection,
urban heat islands, Arctic amplification, permafrost, radon and indoor air, so none of those is tested here.
Checked-clean facts used: the 2024 WHC session and Moidams, pygmy hog/golden langur/wild buffalo sites, whale shark,
fishing cat, Ratapani, Nal Sarovar/Sultanpur/Ranganathittu, the Public Liability Insurance Act, red sanders, Azolla
and Cordyceps, COP/CMA procedure, Happy Seeder and the Pusa decomposer, GRAP and CAQM, earthworms, atmospheric rivers,
derechos, the polar vortex and GLOFs."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Environment & Ecology"
IC = "International Conventions & Organisations"
FA = "Fauna & Animal Behaviour"
PA = "Protected Areas & Wildlife Protection"
LW = "Indian Environmental Laws & Bodies"
FL = "Flora, Fungi & Forests"
CA = "Climate Agreements & Carbon Markets"
PO = "Pollution, Waste & Resources"
EC = "Ecosystems & Ecological Processes"
CS = "Climate Science & Mitigation"
IUCN = "IUCN Red List of Threatened Species"
WPA = "Wild Life (Protection) Act, 1972, as amended in 2022"
MOEF = "Ministry of Environment, Forest and Climate Change"
NC12B = "NCERT Class XII, Biology -- Ecosystem"

# ================================================================ CONVENTIONS (1)
S(IC, "medium", "Consider the following statements about the session of the World Heritage Committee held in 2024:",
  "2024 में हुए विश्व धरोहर समिति के सत्र के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It was the first time that India hosted a session of the World Heritage Committee.",
   "The Moidams of Charaideo in Assam, royal burial mounds of the Ahom dynasty, were inscribed on the World Heritage List at that session.",
   "The World Heritage Convention is administered by the United Nations Environment Programme."],
  ["यह पहली बार था जब भारत ने विश्व धरोहर समिति के सत्र की मेज़बानी की।",
   "असम के चराईदेव के मोइदाम, यानी अहोम राजवंश के शाही समाधि-टीले, उसी सत्र में विश्व धरोहर सूची में शामिल किए गए।",
   "विश्व धरोहर अभिसमय का प्रशासन संयुक्त राष्ट्र पर्यावरण कार्यक्रम (UNEP) करता है।"],
  C3, 1,
  "Statements 1 and 2 are correct. The 46th session met in New Delhi in July 2024, India's first time as host. The Moidams -- earthen mounds raised over the vaults of Ahom kings and nobles at Charaideo -- became India's 43rd World Heritage Site and the first cultural site from the North-East. "
  "Statement 3 is wrong: the 1972 Convention concerning the Protection of the World Cultural and Natural Heritage is administered by UNESCO, advised by IUCN on natural sites and by ICOMOS and ICCROM on cultural ones.",
  "कथन 1 और 2 सही हैं। 46वाँ सत्र जुलाई 2024 में नई दिल्ली में हुआ, और भारत पहली बार मेज़बान बना। मोइदाम, यानी चराईदेव में अहोम राजाओं और सामंतों की समाधियों पर बने मिट्टी के टीले, भारत का 43वाँ विश्व धरोहर स्थल और पूर्वोत्तर का पहला सांस्कृतिक स्थल बने। "
  "कथन 3 गलत है: विश्व सांस्कृतिक और प्राकृतिक धरोहर के संरक्षण से जुड़े 1972 के अभिसमय का प्रशासन यूनेस्को करता है; प्राकृतिक स्थलों पर IUCN और सांस्कृतिक स्थलों पर ICOMOS तथा ICCROM उसे सलाह देते हैं।",
  "UNESCO World Heritage Centre -- 46th session of the World Heritage Committee (2024); Convention concerning the Protection of the World Cultural and Natural Heritage (1972).",
  "env-whc-2024-delhi-moidams")

# ================================================================ FAUNA (3)
P(FA, "hard", "Consider the following pairs of animals and the protected areas they are especially associated with:",
  "जीवों और उन संरक्षित क्षेत्रों के निम्नलिखित युग्मों पर विचार कीजिए जिनसे वे विशेष रूप से जुड़े हैं:",
  ["Pygmy hog : Manas National Park", "Golden langur : Chakrashila Wildlife Sanctuary",
   "Lion-tailed macaque : Dachigam National Park", "Wild water buffalo : Udanti-Sitanadi Tiger Reserve"],
  ["पिग्मी हॉग : मानस राष्ट्रीय उद्यान", "सुनहरा लंगूर : चक्रशिला वन्यजीव अभयारण्य",
   "शेर-पूँछ मकाक : दाचीगाम राष्ट्रीय उद्यान", "जंगली भैंसा : उदंती-सीतानदी टाइगर रिज़र्व"],
  2,
  "Only the third pair is wrong. The pygmy hog, the world's smallest and rarest wild pig, survived in the tall wet grasslands of Manas and has since been bred in captivity and released into other Assam grasslands. "
  "Chakrashila in western Assam was declared a sanctuary chiefly for the golden langur, which lives only in western Assam and neighbouring Bhutan. "
  "The lion-tailed macaque is endemic to the evergreen rainforests of the Western Ghats; Dachigam, near Srinagar, is known for the hangul. "
  "Udanti-Sitanadi in Chhattisgarh shelters one of the last pure populations of the wild water buffalo, the State animal of Chhattisgarh.",
  "केवल तीसरा युग्म गलत है। दुनिया का सबसे छोटा और दुर्लभतम जंगली सूअर, पिग्मी हॉग, मानस के ऊँचे नम घास के मैदानों में बचा रहा, और अब बंदी प्रजनन के बाद असम के अन्य घास के मैदानों में छोड़ा गया है। "
  "पश्चिमी असम का चक्रशिला मुख्य रूप से सुनहरे लंगूर के लिए अभयारण्य घोषित हुआ, जो केवल पश्चिमी असम और पड़ोसी भूटान में मिलता है। "
  "शेर-पूँछ मकाक पश्चिमी घाट के सदाबहार वर्षावनों का स्थानिक जीव है; श्रीनगर के पास दाचीगाम हंगुल के लिए प्रसिद्ध है। "
  "छत्तीसगढ़ का उदंती-सीतानदी जंगली भैंसे की अंतिम शुद्ध आबादियों में से एक का आश्रय है, जो छत्तीसगढ़ का राजकीय पशु है।",
  f"Wildlife Institute of India -- ENVIS Centre on Wildlife and Protected Areas; {IUCN}.",
  "env-fauna-protected-areas-pairs-t21")

S(FA, "medium", "Consider the following statements about the whale shark:",
  "व्हेल शार्क के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is the largest living fish.",
   "It feeds mainly by filtering plankton and small fish from the water.",
   "It was the first fish species to be placed in Schedule I of the Wild Life (Protection) Act, 1972."],
  ["यह सबसे बड़ी जीवित मछली है।",
   "यह मुख्य रूप से पानी से प्लवक (plankton) और छोटी मछलियाँ छानकर भोजन करती है।",
   "यह वन्यजीव (संरक्षण) अधिनियम, 1972 की अनुसूची I में रखी जाने वाली पहली मछली प्रजाति थी।"],
  C3, 2,
  "All three are correct. The whale shark, which can grow beyond 12 m, is a shark, not a whale; it swims with its huge mouth open to filter plankton, fish eggs and small fish. "
  "India placed it in Schedule I in 2001 -- the first fish to get the highest protection -- after large numbers were being killed off the Saurashtra coast of Gujarat; a campaign with fishers there has since led to hundreds of sharks caught in nets being cut free. "
  "It is listed as Endangered by the IUCN and in Appendix II of CITES.",
  "तीनों कथन सही हैं। 12 मीटर से भी लंबी हो सकने वाली व्हेल शार्क एक शार्क है, व्हेल नहीं; यह अपना विशाल मुँह खोलकर तैरती है और प्लवक, मछलियों के अंडे तथा छोटी मछलियाँ छान लेती है। "
  "गुजरात के सौराष्ट्र तट पर बड़ी संख्या में इनके मारे जाने के बाद भारत ने 2001 में इसे अनुसूची I में रखा; सर्वोच्च संरक्षण पाने वाली यह पहली मछली थी। वहाँ मछुआरों के साथ चले अभियान से अब जाल में फँसी सैकड़ों शार्क छोड़ी जा चुकी हैं। "
  "IUCN इसे संकटग्रस्त (Endangered) मानता है और यह CITES के परिशिष्ट II में है।",
  f"{WPA}; {IUCN}.",
  "env-whale-shark-schedule-i")

M(FA, "easy", "Which one of the following wild cats, with partly webbed feet, lives in wetlands and mangroves and is the State animal of West Bengal?",
  "निम्नलिखित में से कौन-सी जंगली बिल्ली, जिसके पैर आंशिक रूप से जालीदार होते हैं, आर्द्रभूमियों और मैंग्रोव में रहती है और पश्चिम बंगाल का राजकीय पशु है?",
  ["Fishing cat", "Caracal", "Clouded leopard", "Rusty-spotted cat"],
  ["फ़िशिंग कैट (मछुआरी बिल्ली)", "कैराकल (स्याहगोश)", "क्लाउडेड लेपर्ड (धूमिल तेंदुआ)", "रस्टी-स्पॉटेड कैट"],
  0,
  "The fishing cat dives for fish and scoops them out with its partly webbed paws; it lives in marshes, mangroves such as the Sundarbans and Coringa, and the wetlands of the Terai, and is listed as Vulnerable. The draining and conversion of wetlands, including for fish farms, is its main threat. "
  "The caracal is a cat of dry scrub and ravines, the clouded leopard a tree-climbing cat of the north-eastern forests, and the rusty-spotted cat, the world's smallest wild cat, lives in the dry forests of peninsular India.",
  "फ़िशिंग कैट पानी में गोता लगाकर मछली पकड़ती है और आंशिक जालीदार पंजों से उन्हें निकालती है; यह दलदलों, सुंदरबन और कोरिंगा जैसे मैंग्रोव तथा तराई की आर्द्रभूमियों में रहती है और संवेदनशील (Vulnerable) श्रेणी में है। मत्स्य पालन सहित अन्य कामों के लिए आर्द्रभूमियों को सुखाना और बदलना इसका मुख्य ख़तरा है। "
  "कैराकल शुष्क झाड़ियों और बीहड़ों की बिल्ली है, क्लाउडेड लेपर्ड पूर्वोत्तर के वनों में पेड़ों पर चढ़ने वाली बिल्ली है, और दुनिया की सबसे छोटी जंगली बिल्ली, रस्टी-स्पॉटेड कैट, प्रायद्वीपीय भारत के शुष्क वनों में रहती है।",
  f"{IUCN}; {MOEF}.",
  "env-fishing-cat-easy")

# ================================================================ PROTECTED AREAS (2)
M(PA, "medium", "The Ratapani Tiger Reserve, notified in 2024, contains within its landscape which one of the following World Heritage Sites?",
  "2024 में अधिसूचित रातापानी टाइगर रिज़र्व के भू-क्षेत्र में निम्नलिखित में से कौन-सा विश्व धरोहर स्थल स्थित है?",
  ["Rock Shelters of Bhimbetka", "Buddhist Monuments at Sanchi", "Khajuraho Group of Monuments", "Mahabodhi Temple, Bodh Gaya"],
  ["भीमबेटका के शैलाश्रय", "साँची के बौद्ध स्मारक", "खजुराहो स्मारक समूह", "महाबोधि मंदिर, बोधगया"],
  0,
  "Ratapani, in the Raisen and Sehore districts near Bhopal, became Madhya Pradesh's eighth tiger reserve in December 2024. The Bhimbetka rock shelters, with paintings from the Mesolithic onward, lie within its forest landscape, so the reserve joins natural and cultural heritage. "
  "Sanchi is also in Raisen district but outside the reserve; Khajuraho lies in the north of the State near Panna, and the Mahabodhi Temple is in Bihar.",
  "भोपाल के पास रायसेन और सीहोर ज़िलों में स्थित रातापानी दिसंबर 2024 में मध्य प्रदेश का आठवाँ टाइगर रिज़र्व बना। मध्यपाषाण काल से आगे के चित्रों वाले भीमबेटका शैलाश्रय इसी वन-क्षेत्र में हैं, इसलिए यह रिज़र्व प्राकृतिक और सांस्कृतिक धरोहर को जोड़ता है। "
  "साँची भी रायसेन ज़िले में है पर रिज़र्व से बाहर; खजुराहो राज्य के उत्तर में पन्ना के पास है, और महाबोधि मंदिर बिहार में है।",
  "National Tiger Conservation Authority -- list of tiger reserves; UNESCO World Heritage Centre -- Rock Shelters of Bhimbetka.",
  "env-ratapani-bhimbetka")

S(PA, "medium", "Consider the following statements about wetlands of India designated as Ramsar sites:",
  "रामसर स्थल घोषित भारत की आर्द्रभूमियों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Nal Sarovar is a coastal lagoon on the Odisha coast.",
   "Sultanpur National Park lies in Haryana.",
   "Ranganathittu Bird Sanctuary lies on the Kaveri in Tamil Nadu."],
  ["नल सरोवर ओडिशा तट पर स्थित एक तटीय लैगून है।",
   "सुल्तानपुर राष्ट्रीय उद्यान हरियाणा में है।",
   "रंगनथिट्टू पक्षी अभयारण्य तमिलनाडु में कावेरी पर स्थित है।"],
  C3, 0,
  "Only statement 2 is correct. Sultanpur, in Gurugram district of Haryana, is a small, shallow wetland that draws migratory waterbirds every winter. "
  "Statement 1 is wrong: Nal Sarovar is a large, shallow inland lake west of Ahmedabad in Gujarat, a halt for flamingos, pelicans and ducks on the Central Asian Flyway. "
  "Statement 3 is wrong: Ranganathittu, a cluster of islets on the Kaveri near Srirangapatna, is in Mandya district of Karnataka and was the State's first Ramsar site.",
  "केवल कथन 2 सही है। हरियाणा के गुरुग्राम ज़िले का सुल्तानपुर एक छोटी, उथली आर्द्रभूमि है जहाँ हर सर्दी में प्रवासी जल-पक्षी आते हैं। "
  "कथन 1 गलत है: नल सरोवर गुजरात में अहमदाबाद के पश्चिम में एक बड़ी, उथली अंतर्देशीय झील है, जो मध्य एशियाई फ़्लाईवे पर फ़्लेमिंगो, पेलिकन और बत्तखों का पड़ाव है। "
  "कथन 3 गलत है: श्रीरंगपटना के पास कावेरी के टापुओं का समूह रंगनथिट्टू कर्नाटक के मंड्या ज़िले में है और राज्य का पहला रामसर स्थल था।",
  f"Ramsar Sites Information Service; {MOEF} -- Ramsar sites of India.",
  "env-ramsar-nal-sultanpur-ranganathittu")

# ================================================================ LAWS (1)
S(LW, "hard", "Consider the following statements about the Public Liability Insurance Act, 1991:",
  "सार्वजनिक दायित्व बीमा अधिनियम, 1991 के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It was enacted in the wake of the Bhopal gas disaster.",
   "It requires owners handling hazardous substances to take insurance, so that victims of an accident get immediate relief on a no-fault basis.",
   "A victim who accepts relief under the Act loses the right to claim further compensation under any other law."],
  ["यह भोपाल गैस त्रासदी के बाद बनाया गया।",
   "यह ख़तरनाक पदार्थों का काम करने वाले स्वामियों से बीमा लेने की अपेक्षा करता है, ताकि दुर्घटना के पीड़ितों को बिना दोष सिद्ध किए (no-fault) तुरंत राहत मिले।",
   "अधिनियम के तहत राहत स्वीकार करने वाला पीड़ित किसी अन्य क़ानून के तहत आगे मुआवज़ा माँगने का अधिकार खो देता है।"],
  C3, 1,
  "Statements 1 and 2 are correct. The Act obliges every owner who handles notified hazardous substances to hold insurance and makes the owner liable to pay fixed relief for death, injury or damage to property without the victim having to prove negligence -- the 'no-fault' principle. An Environment Relief Fund, fed by contributions from owners, adds to the insurance money. "
  "Statement 3 is wrong: relief under the Act is interim; the victim may still seek full compensation under other laws, and the relief already paid is deducted from any later award.",
  "कथन 1 और 2 सही हैं। यह अधिनियम अधिसूचित ख़तरनाक पदार्थों का काम करने वाले हर स्वामी के लिए बीमा अनिवार्य करता है और उसे मृत्यु, चोट या संपत्ति की हानि पर निश्चित राहत देने के लिए उत्तरदायी बनाता है, बिना इसके कि पीड़ित को लापरवाही सिद्ध करनी पड़े; यही 'बिना दोष' (no-fault) सिद्धांत है। स्वामियों के अंशदान से बना पर्यावरण राहत कोष बीमा राशि में जुड़ता है। "
  "कथन 3 गलत है: अधिनियम के तहत राहत अंतरिम है; पीड़ित अन्य क़ानूनों के तहत पूरा मुआवज़ा माँग सकता है, और पहले दी गई राहत बाद के किसी भी मुआवज़े में से घटा दी जाती है।",
  f"Public Liability Insurance Act, 1991; {MOEF}.",
  "env-public-liability-insurance-act")

# ================================================================ FLORA (2)
S(FL, "medium", "Consider the following statements about red sanders (Pterocarpus santalinus):",
  "लाल चंदन (Pterocarpus santalinus) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is endemic to the southern Eastern Ghats, chiefly in Andhra Pradesh.",
   "International trade in it is regulated under Appendix II of CITES.",
   "Its dense, deep-red heartwood, rather than any fragrance, is what makes it valuable."],
  ["यह दक्षिणी पूर्वी घाट का स्थानिक वृक्ष है, मुख्यतः आंध्र प्रदेश में।",
   "इसके अंतरराष्ट्रीय व्यापार का विनियमन CITES के परिशिष्ट II के तहत होता है।",
   "इसे मूल्यवान बनाने वाली चीज़ इसकी सुगंध नहीं, बल्कि इसकी घनी, गहरी लाल अंतःकाष्ठ (heartwood) है।"],
  C3, 2,
  "All three are correct. Red sanders grows naturally only in the dry deciduous forests of the Seshachalam, Veliconda and nearby hills of Andhra Pradesh, with small extensions into Tamil Nadu and Karnataka. It is listed in CITES Appendix II, and India allows exports only of legally sourced wood. "
  "Unlike sandalwood, it has no fragrance; its heavy red timber is prized abroad for furniture, musical instruments and dye, which drives large-scale smuggling from the Seshachalam forests.",
  "तीनों कथन सही हैं। लाल चंदन प्राकृतिक रूप से केवल आंध्र प्रदेश की शेषाचलम, वेलिकोंडा और आसपास की पहाड़ियों के शुष्क पर्णपाती वनों में उगता है, जिसका थोड़ा विस्तार तमिलनाडु और कर्नाटक तक है। यह CITES के परिशिष्ट II में है, और भारत केवल वैध स्रोत की लकड़ी के निर्यात की अनुमति देता है। "
  "सफ़ेद चंदन के विपरीत इसमें कोई सुगंध नहीं होती; इसकी भारी लाल लकड़ी विदेशों में फ़र्नीचर, वाद्ययंत्रों और रंग के लिए बहुत मूल्यवान है, और इसी से शेषाचलम के वनों से बड़े पैमाने पर तस्करी होती है।",
  f"{IUCN}; CITES Appendices; {MOEF}.",
  "env-red-sanders")

S(FL, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Azolla is a small floating fern that is grown in paddy fields as a nitrogen-fixing biofertiliser.",
   "Cordyceps, collected from high Himalayan meadows for traditional medicine, is a flowering herb."],
  ["एज़ोला एक छोटा तैरने वाला फ़र्न है जिसे धान के खेतों में नाइट्रोजन स्थिर करने वाले जैव-उर्वरक के रूप में उगाया जाता है।",
   "पारंपरिक औषधि के लिए ऊँचे हिमालयी घास के मैदानों से इकट्ठा किया जाने वाला कॉर्डिसेप्स एक फूलदार जड़ी-बूटी है।"],
  T2, 0,
  "Only statement 1 is correct. Azolla carries the nitrogen-fixing cyanobacterium Anabaena inside its leaves, so a mat of it on flooded rice fields adds nitrogen to the soil; it is also fed to cattle and poultry. "
  "Statement 2 is wrong: Cordyceps (yartsa gunbu, or keeda jadi) is a fungus that infects and mummifies ghost-moth caterpillars in alpine meadows; its stalk-like fruiting body pokes out of the soil, fetches very high prices and draws thousands of collectors in Uttarakhand, Sikkim and Nepal.",
  "केवल कथन 1 सही है। एज़ोला की पत्तियों में नाइट्रोजन स्थिर करने वाला सायनोबैक्टीरियम एनाबीना रहता है, इसलिए पानी भरे धान के खेतों में इसकी परत मिट्टी में नाइट्रोजन जोड़ती है; इसे पशुओं और मुर्गियों को चारे के रूप में भी दिया जाता है। "
  "कथन 2 गलत है: कॉर्डिसेप्स (यार्सागुम्बा या कीड़ा जड़ी) एक कवक है जो ऊँचे घास के मैदानों में घोस्ट-मॉथ की इल्लियों को संक्रमित कर सुखा देता है; इसका डंठल जैसा फलन-काय मिट्टी से बाहर निकलता है, बहुत ऊँचे दाम पर बिकता है और उत्तराखंड, सिक्किम तथा नेपाल में हज़ारों लोगों को इसे इकट्ठा करने खींच लाता है।",
  f"Indian Council of Agricultural Research -- Azolla as biofertiliser; {MOEF}.",
  "env-azolla-cordyceps-easy")

# ================================================================ CLIMATE AGREEMENTS (1)
S(CA, "hard", "Consider the following statements about decision-making under the UN Framework Convention on Climate Change:",
  "संयुक्त राष्ट्र जलवायु परिवर्तन फ़्रेमवर्क अभिसमय (UNFCCC) के तहत निर्णय-प्रक्रिया के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Conference of the Parties (COP) is the supreme decision-making body of the Convention.",
   "The meeting of the Parties to the Paris Agreement (CMA) is held only once every five years, in the years of the global stocktake.",
   "Decisions at the COP are normally taken by a simple majority vote of the Parties."],
  ["पक्षकारों का सम्मेलन (COP) इस अभिसमय का सर्वोच्च निर्णयकारी निकाय है।",
   "पेरिस समझौते के पक्षकारों की बैठक (CMA) केवल हर पाँच वर्ष में एक बार, वैश्विक समीक्षा (global stocktake) के वर्षों में होती है।",
   "COP में निर्णय सामान्यतः पक्षकारों के साधारण बहुमत से मतदान द्वारा लिए जाते हैं।"],
  C3, 0,
  "Only statement 1 is correct. The COP meets every year, and the same session also serves as the CMA for the Paris Agreement and the CMP for the Kyoto Protocol, so the CMA meets annually, not only in stocktake years. Two subsidiary bodies -- SBSTA for scientific and technological advice and SBI for implementation -- prepare its work. "
  "Statement 3 is wrong: because the Parties have never agreed on the voting rule in the draft rules of procedure, decisions are in practice taken by consensus. That gives any determined group of countries a strong say, and explains the late-night bargaining at the end of each COP.",
  "केवल कथन 1 सही है। COP हर वर्ष बैठता है, और वही सत्र पेरिस समझौते के लिए CMA तथा क्योटो प्रोटोकॉल के लिए CMP का काम भी करता है; इसलिए CMA हर वर्ष बैठती है, केवल समीक्षा वाले वर्षों में नहीं। दो सहायक निकाय, वैज्ञानिक और तकनीकी सलाह के लिए SBSTA और कार्यान्वयन के लिए SBI, इसका काम तैयार करते हैं। "
  "कथन 3 गलत है: पक्षकार प्रक्रिया-नियमों के मसौदे में मतदान के नियम पर कभी सहमत नहीं हुए, इसलिए व्यवहार में निर्णय सर्वसम्मति से लिए जाते हैं। इससे किसी भी दृढ़ देश-समूह की बात का वज़न बढ़ जाता है, और यही हर COP के अंत में देर रात तक चलने वाली सौदेबाज़ी का कारण है।",
  "United Nations Framework Convention on Climate Change -- bodies and process; UNFCCC draft rules of procedure.",
  "env-unfccc-cop-cma-consensus")

# ================================================================ POLLUTION (2)
S(PO, "medium", "Consider the following statements about managing paddy stubble in north-west India:",
  "उत्तर-पश्चिम भारत में धान की पराली के प्रबंधन के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Happy Seeder sows wheat directly into fields holding paddy stubble, without burning or removing it.",
   "The Pusa decomposer is a microbial preparation that speeds up the breakdown of stubble in the field.",
   "Stubble burning in Punjab and Haryana peaks in the pre-monsoon months of April and May."],
  ["हैप्पी सीडर पराली वाले खेतों में, उसे जलाए या हटाए बिना, सीधे गेहूँ बोता है।",
   "पूसा डीकंपोज़र एक सूक्ष्मजीवी घोल है जो खेत में पराली के सड़ने की गति बढ़ाता है।",
   "पंजाब और हरियाणा में पराली जलाना मानसून-पूर्व के अप्रैल और मई महीनों में चरम पर होता है।"],
  C3, 1,
  "Statements 1 and 2 are correct. The tractor-mounted Happy Seeder cuts and lifts the straw, drills the wheat seed and lays the straw back as mulch; the Pusa decomposer, developed by the Indian Agricultural Research Institute, is a mix of fungal strains sprayed on the stubble so that it rots within a few weeks. "
  "Statement 3 is wrong: burning peaks in October and November, when farmers have a short window between the paddy harvest and wheat sowing; it coincides with calm winds and falling temperatures, which trap the smoke over the Indo-Gangetic plain. Some wheat residue is burnt in April-May, but on a far smaller scale.",
  "कथन 1 और 2 सही हैं। ट्रैक्टर से चलने वाला हैप्पी सीडर पराली को काटकर उठाता है, गेहूँ का बीज बोता है और पराली को वापस पलवार (mulch) की तरह बिछा देता है; भारतीय कृषि अनुसंधान संस्थान का बनाया पूसा डीकंपोज़र कवक प्रजातियों का मिश्रण है, जिसे पराली पर छिड़कने से वह कुछ ही हफ़्तों में सड़ जाती है। "
  "कथन 3 गलत है: पराली जलाना अक्टूबर और नवंबर में चरम पर होता है, जब किसानों के पास धान की कटाई और गेहूँ की बुवाई के बीच थोड़ा समय होता है; यही समय शांत हवाओं और गिरते तापमान का होता है, जो धुएँ को सिंधु-गंगा मैदान के ऊपर रोक लेते हैं। अप्रैल-मई में भी कुछ गेहूँ के अवशेष जलते हैं, पर बहुत कम पैमाने पर।",
  "Indian Agricultural Research Institute -- Pusa decomposer; Ministry of Agriculture and Farmers Welfare -- crop residue management.",
  "env-stubble-happy-seeder-pusa")

M(PO, "medium", "The Graded Response Action Plan (GRAP) for air pollution in the Delhi-NCR is now invoked and enforced by the",
  "दिल्ली-एनसीआर में वायु प्रदूषण के लिए श्रेणीबद्ध प्रतिक्रिया कार्य योजना (GRAP) को अब कौन लागू करता है?",
  ["Commission for Air Quality Management in NCR and Adjoining Areas",
   "Environment Pollution (Prevention and Control) Authority",
   "National Green Tribunal, through its principal bench",
   "Delhi Pollution Control Committee, under the Delhi Government's orders"],
  ["राष्ट्रीय राजधानी क्षेत्र और आसपास के क्षेत्रों में वायु गुणवत्ता प्रबंधन आयोग",
   "पर्यावरण प्रदूषण (रोकथाम और नियंत्रण) प्राधिकरण",
   "राष्ट्रीय हरित अधिकरण, अपनी प्रधान पीठ के माध्यम से",
   "दिल्ली सरकार के आदेशों के तहत दिल्ली प्रदूषण नियंत्रण समिति"],
  0,
  "GRAP is a set of emergency steps triggered stage by stage as air quality worsens -- from dust control and curbs on diesel generators to bans on construction and on older vehicles. It was first notified in 2017 and enforced by the Supreme Court-appointed Environment Pollution (Prevention and Control) Authority. "
  "That body was dissolved in 2020 when the Commission for Air Quality Management was set up; under the Commission's 2021 Act it now revises and invokes GRAP, and its directions prevail over those of other authorities in the region.",
  "GRAP आपात क़दमों का एक समूह है जो वायु गुणवत्ता बिगड़ने के साथ चरण-दर-चरण लागू होता है, जैसे धूल नियंत्रण और डीज़ल जनरेटर पर रोक से लेकर निर्माण और पुराने वाहनों पर प्रतिबंध तक। इसे पहली बार 2017 में अधिसूचित किया गया और सर्वोच्च न्यायालय द्वारा नियुक्त पर्यावरण प्रदूषण (रोकथाम और नियंत्रण) प्राधिकरण इसे लागू करता था। "
  "2020 में वायु गुणवत्ता प्रबंधन आयोग बनने पर वह प्राधिकरण भंग कर दिया गया; आयोग के 2021 के अधिनियम के तहत अब वही GRAP में संशोधन करता है और उसे लागू करता है, और उसके निर्देश क्षेत्र के अन्य प्राधिकरणों पर प्रभावी होते हैं।",
  "Commission for Air Quality Management in National Capital Region and Adjoining Areas Act, 2021; CAQM -- Graded Response Action Plan.",
  "env-grap-caqm")

# ================================================================ ECOSYSTEMS (1)
S(EC, "easy", "Consider the following statements about earthworms:",
  "केंचुओं के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["They feed on dead organic matter and are counted among detritivores.",
   "Their burrowing improves soil aeration and drainage."],
  ["वे मृत कार्बनिक पदार्थ खाते हैं और अपरदाहारी (detritivores) गिने जाते हैं।",
   "उनके बिल बनाने से मिट्टी में वायु-संचार और जल-निकास सुधरता है।"],
  T2, 2,
  "Both statements are correct. Earthworms swallow soil and decaying leaves, grind the material into fine particles and pass out casts rich in plant nutrients, which is why they are used to make vermicompost. "
  "Their burrows let air and water into the soil and help roots go deeper, so ecologists often call them 'ecosystem engineers'.",
  "दोनों कथन सही हैं। केंचुए मिट्टी और सड़ती पत्तियाँ निगलकर उन्हें महीन कणों में पीसते हैं और पौधों के पोषक तत्वों से भरपूर मल (casts) निकालते हैं; इसीलिए उनसे वर्मीकम्पोस्ट बनाया जाता है। "
  "उनके बिल मिट्टी में हवा और पानी पहुँचाते हैं और जड़ों को गहराई तक जाने में मदद करते हैं, इसलिए पारिस्थितिकीविद् उन्हें प्रायः 'पारितंत्र अभियंता' (ecosystem engineers) कहते हैं।",
  f"{NC12B}; NCERT Class XI, Biology -- Animal Kingdom.",
  "env-earthworms-easy")

# ================================================================ CLIMATE SCIENCE (2)
S(CS, "medium", "Consider the following statements about extreme-weather phenomena:",
  "चरम मौसमी घटनाओं के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["An atmospheric river is a long, narrow band of concentrated water vapour carried in the lower atmosphere.",
   "A derecho is a slow-moving tropical cyclone that stalls over a coastline for several days.",
   "The polar vortex is a belt of warm air that circles the Equator in the upper atmosphere."],
  ["वायुमंडलीय नदी (atmospheric river) निचले वायुमंडल में बहने वाली घनी जलवाष्प की एक लंबी, सँकरी पट्टी है।",
   "डेरेचो (derecho) एक धीमा उष्णकटिबंधीय चक्रवात है जो कई दिनों तक किसी तट पर ठहरा रहता है।",
   "ध्रुवीय भँवर (polar vortex) ऊपरी वायुमंडल में विषुवत रेखा के चारों ओर घूमने वाली गर्म वायु की पट्टी है।"],
  C3, 0,
  "Only statement 1 is correct. Atmospheric rivers carry moisture from the tropics toward higher latitudes; when they run into mountains they can drop torrential rain, as on the west coast of North America. "
  "Statement 2 is wrong: a derecho is a fast-moving, long-lived windstorm driven by a line of thunderstorms, which can flatten crops and forests along a path hundreds of kilometres long; it is not a cyclone. "
  "Statement 3 is wrong: the polar vortex is a large band of cold, low-pressure air circling each pole; when it weakens or splits, bitter cold can spill into the middle latitudes.",
  "केवल कथन 1 सही है। वायुमंडलीय नदियाँ उष्णकटिबंध से ऊँचे अक्षांशों की ओर नमी ले जाती हैं; पहाड़ों से टकराने पर वे मूसलाधार वर्षा कर सकती हैं, जैसे उत्तर अमेरिका के पश्चिमी तट पर। "
  "कथन 2 गलत है: डेरेचो तड़ित-झंझाओं की एक पंक्ति से उठने वाला तेज़, लंबे समय तक चलने वाला पवन-तूफ़ान है, जो सैकड़ों किलोमीटर लंबे रास्ते में फ़सलें और वन गिरा सकता है; यह चक्रवात नहीं है। "
  "कथन 3 गलत है: ध्रुवीय भँवर हर ध्रुव के चारों ओर घूमने वाली ठंडी, निम्न दाब वायु की बड़ी पट्टी है; इसके कमज़ोर पड़ने या टूटने पर कड़ाके की ठंड मध्य अक्षांशों तक फैल सकती है।",
  "World Meteorological Organization -- International Meteorological Vocabulary; India Meteorological Department.",
  "env-atmospheric-river-derecho-polar-vortex")

A(CS, "medium",
  "The risk of glacial lake outburst floods is rising in the Himalaya.",
  "हिमालय में हिमनद झील के फटने से आने वाली बाढ़ (GLOF) का ख़तरा बढ़ रहा है।",
  "As glaciers retreat, many lakes held back by loose moraine dams are growing larger.",
  "हिमनदों के पीछे हटने के साथ ढीले हिमोढ़ (moraine) बाँधों से रुकी अनेक झीलें बड़ी होती जा रही हैं।",
  0,
  "Both statements are correct and Statement-II explains Statement-I. Meltwater collects behind unstable ridges of rock and debris left by retreating glaciers; an avalanche, landslide, earthquake or heavy rain can breach the moraine and release the lake in a sudden flood. "
  "In October 2023 the outburst of South Lhonak lake in Sikkim swept down the Teesta and destroyed the Chungthang dam. The National Disaster Management Authority has since mapped high-risk lakes and is installing early-warning systems and lowering water levels at some of them.",
  "दोनों कथन सही हैं और कथन-II कथन-I की व्याख्या करता है। पीछे हटते हिमनदों द्वारा छोड़ी गई चट्टान और मलबे की अस्थिर मेड़ों के पीछे पिघला जल इकट्ठा होता है; हिमस्खलन, भूस्खलन, भूकंप या भारी वर्षा हिमोढ़ को तोड़कर झील को अचानक बाढ़ के रूप में बहा सकती है। "
  "अक्टूबर 2023 में सिक्किम की दक्षिण ल्होनक झील के फटने से बाढ़ तीस्ता में बहती हुई चुंगथांग बाँध को नष्ट कर गई। राष्ट्रीय आपदा प्रबंधन प्राधिकरण ने तब से अधिक ख़तरे वाली झीलों का मानचित्रण किया है और कुछ पर पूर्व-चेतावनी प्रणालियाँ लगा रहा है तथा उनका जल-स्तर घटा रहा है।",
  "National Disaster Management Authority -- Guidelines on Management of Glacial Lake Outburst Floods; IPCC AR6 WGII.",
  "env-glof-moraine-lakes")

if __name__ == "__main__":
    write("gs_l2_t21_environment.sql")
