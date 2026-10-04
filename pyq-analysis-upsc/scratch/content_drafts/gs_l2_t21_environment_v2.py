# -*- coding: utf-8 -*-
"""Level 2 · Test 21 -- Environment block, rewritten to the depth standard of October 2026
(docs/upsc-question-design-standard.md §6). It updates the 15 draft rows of gs_l2_t21_environment.py in place,
with the same blueprint cells.
  - Whale shark: a shark caught in a Saurashtra net, tested against the law and the release scheme.
  - Red sanders: what a CITES Appendix II listing does and does not mean.
  - Stubble: why farmers burn, and what burning costs the soil.
  - GRAP: which body acts when the AQI turns severe; the dissolved EPCA is the trap.
  - Weather systems: what a weakened polar vortex does to the middle latitudes.
The Conventions, Laws and Climate-agreement rows were already precision rows; the species and places that
Prelims asks as plain facts stay as recall. Every row is tagged.
Craft mix: recall 7, inference 3, precision 3, application 2."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write_updates, CODE
from polity_common import C3, C4, T2

d.SUBJECT = "Environment & Ecology"
d.REQUIRE_CRAFT = True
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
  "env-whc-2024-delhi-moidams", craft="recall")

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
  "env-fauna-protected-areas-pairs-t21", craft="recall")

S(FA, "medium", "A whale shark gets entangled in a fisherman's net off the Saurashtra coast of Gujarat. Consider the following statements:",
  "गुजरात के सौराष्ट्र तट के पास एक व्हेल शार्क एक मछुआरे के जाल में फँस जाती है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["Killing the shark or selling its meat would be an offence, since the species is listed in Schedule I of the Wild Life (Protection) Act, 1972.",
   "Cutting it free carries little danger to the fishermen, since it is a filter feeder that does not hunt large animals.",
   "A fisherman who cuts his net to release the shark can be compensated by the State Forest Department."],
  ["शार्क को मारना या उसका मांस बेचना अपराध होगा, क्योंकि यह प्रजाति वन्यजीव (संरक्षण) अधिनियम, 1972 की अनुसूची I में है।",
   "इसे जाल से छुड़ाने में मछुआरों को बहुत कम ख़तरा है, क्योंकि यह छानकर भोजन करने वाला जीव है जो बड़े जानवरों का शिकार नहीं करता।",
   "शार्क को छोड़ने के लिए अपना जाल काटने वाले मछुआरे को राज्य वन विभाग मुआवज़ा दे सकता है।"],
  C3, 2,
  "All three are correct. The whale shark, the largest living fish, was placed in Schedule I in 2001 -- the first fish to get the highest protection -- after large numbers were being slaughtered off Saurashtra, so killing or trading it is an offence. "
  "Despite its size it is harmless to people: it swims with its mouth open to filter plankton, fish eggs and small fish. "
  "Gujarat's Forest Department, working with conservation groups, compensates fishermen for nets cut to free entangled sharks, and hundreds have been released at sea this way. The species is Endangered on the IUCN Red List and is listed in CITES Appendix II.",
  "तीनों कथन सही हैं। सबसे बड़ी जीवित मछली, व्हेल शार्क, को 2001 में अनुसूची I में रखा गया, जब सौराष्ट्र तट पर इनका बड़े पैमाने पर वध हो रहा था; सर्वोच्च संरक्षण पाने वाली यह पहली मछली थी, इसलिए इसे मारना या इसका व्यापार करना अपराध है। "
  "अपने आकार के बावजूद यह मनुष्यों के लिए हानिरहित है: यह मुँह खोलकर तैरती है और प्लवक, मछलियों के अंडे तथा छोटी मछलियाँ छान लेती है। "
  "गुजरात का वन विभाग संरक्षण संस्थाओं के साथ मिलकर उन मछुआरों को मुआवज़ा देता है जो फँसी शार्क को छुड़ाने के लिए अपना जाल काटते हैं, और इस तरह सैकड़ों शार्क समुद्र में छोड़ी जा चुकी हैं। IUCN इसे संकटग्रस्त (Endangered) मानता है और यह CITES के परिशिष्ट II में है।",
  f"{WPA}; {IUCN}; Gujarat Forest Department -- whale shark conservation campaign.",
  "env-whale-shark-schedule-i", craft="application")

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
  "env-fishing-cat-easy", craft="recall")

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
  "env-ratapani-bhimbetka", craft="recall")

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
  "env-ramsar-nal-sultanpur-ranganathittu", craft="recall")

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
  "env-public-liability-insurance-act", craft="precision")

# ================================================================ FLORA (2)
S(FL, "medium", "Consider the following statements about red sanders (Pterocarpus santalinus):",
  "लाल चंदन (Pterocarpus santalinus) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is endemic to the southern Eastern Ghats, chiefly in Andhra Pradesh.",
   "Unlike sandalwood, it is valued for its dense red heartwood rather than for any fragrance.",
   "Because it is listed in Appendix II of CITES, all international trade in it is prohibited."],
  ["यह दक्षिणी पूर्वी घाट का स्थानिक वृक्ष है, मुख्यतः आंध्र प्रदेश में।",
   "सफ़ेद चंदन के विपरीत, यह किसी सुगंध के लिए नहीं बल्कि अपनी घनी लाल अंतःकाष्ठ (heartwood) के लिए मूल्यवान है।",
   "चूँकि यह CITES के परिशिष्ट II में है, इसलिए इसका सारा अंतरराष्ट्रीय व्यापार प्रतिबंधित है।"],
  C3, 1,
  "Statements 1 and 2 are correct. Red sanders grows naturally only in the dry deciduous forests of the Seshachalam, Veliconda and nearby hills of Andhra Pradesh, with small extensions into Tamil Nadu and Karnataka. It has no fragrance; its heavy red timber is prized abroad for furniture, musical instruments and dye, which drives large-scale smuggling. "
  "Statement 3 is wrong: Appendix II covers species that are not necessarily threatened with extinction but whose trade must be controlled. Trade is allowed under export permits issued when it will not harm the species' survival, and India permits exports only of legally sourced wood. It is Appendix I that bars commercial trade.",
  "कथन 1 और 2 सही हैं। लाल चंदन प्राकृतिक रूप से केवल आंध्र प्रदेश की शेषाचलम, वेलिकोंडा और आसपास की पहाड़ियों के शुष्क पर्णपाती वनों में उगता है, जिसका थोड़ा विस्तार तमिलनाडु और कर्नाटक तक है। इसमें कोई सुगंध नहीं होती; इसकी भारी लाल लकड़ी विदेशों में फ़र्नीचर, वाद्ययंत्रों और रंग के लिए बहुत मूल्यवान है, जिससे बड़े पैमाने पर तस्करी होती है। "
  "कथन 3 गलत है: परिशिष्ट II में वे प्रजातियाँ आती हैं जो आवश्यक रूप से विलुप्ति के कगार पर नहीं हैं, पर जिनके व्यापार पर नियंत्रण ज़रूरी है। प्रजाति के अस्तित्व को हानि न पहुँचने पर निर्यात परमिट के तहत व्यापार की अनुमति है, और भारत केवल वैध स्रोत की लकड़ी के निर्यात की अनुमति देता है। व्यावसायिक व्यापार पर रोक परिशिष्ट I लगाता है।",
  f"{IUCN}; CITES -- Appendices and Article IV; {MOEF}.",
  "env-red-sanders", craft="precision")

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
  "env-azolla-cordyceps-easy", craft="recall")

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
  "env-unfccc-cop-cma-consensus", craft="precision")

# ================================================================ POLLUTION (2)
S(PO, "medium", "Consider the following statements about the burning of paddy stubble in Punjab and Haryana:",
  "पंजाब और हरियाणा में धान की पराली जलाने के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The short gap between the paddy harvest and the sowing of wheat pushes farmers to clear their fields by fire.",
   "Machines such as the Happy Seeder let wheat be sown straight into the stubble, removing the need to burn it.",
   "Burning the straw returns all its nitrogen to the soil, so the farmer loses no nutrients."],
  ["धान की कटाई और गेहूँ की बुवाई के बीच का कम समय किसानों को आग से खेत साफ़ करने की ओर धकेलता है।",
   "हैप्पी सीडर जैसी मशीनें पराली के बीच ही सीधे गेहूँ बोने देती हैं, जिससे उसे जलाने की ज़रूरत नहीं रहती।",
   "पराली जलाने से उसकी सारी नाइट्रोजन मिट्टी में लौट आती है, इसलिए किसान को पोषक तत्वों का कोई नुक़सान नहीं होता।"],
  C3, 1,
  "Statements 1 and 2 are correct. Paddy is harvested in October, often by combine harvesters that leave tall stubble, and wheat must be sown by early November; with only two or three weeks to spare, fire is the cheapest way to clear the field. The Happy Seeder cuts and lifts the straw, drills the seed and lays the straw back as mulch, and the Pusa decomposer, a mix of fungi sprayed on the stubble, makes it rot in the field. "
  "Statement 3 is wrong: most of the straw's nitrogen and much of its sulphur go up as gases when it burns, along with its organic carbon, and the heat kills useful soil microbes. Burning therefore costs the soil nutrients as well as fouling the air.",
  "कथन 1 और 2 सही हैं। धान की कटाई अक्टूबर में, प्रायः कंबाइन हार्वेस्टर से होती है जो ऊँची पराली छोड़ देते हैं, और गेहूँ नवंबर की शुरुआत तक बोना होता है; केवल दो-तीन हफ़्तों के समय में आग खेत साफ़ करने का सबसे सस्ता तरीक़ा है। हैप्पी सीडर पराली को काटकर उठाता है, बीज बोता है और पराली को वापस पलवार (mulch) की तरह बिछा देता है, और पराली पर छिड़का जाने वाला कवकों का मिश्रण, पूसा डीकंपोज़र, उसे खेत में ही सड़ा देता है। "
  "कथन 3 गलत है: जलने पर पराली की अधिकांश नाइट्रोजन और काफ़ी गंधक, उसके जैविक कार्बन के साथ, गैस बनकर उड़ जाते हैं, और गर्मी मिट्टी के उपयोगी सूक्ष्मजीवों को मार देती है। इसलिए पराली जलाने से हवा तो दूषित होती ही है, मिट्टी के पोषक तत्व भी घटते हैं।",
  "Indian Agricultural Research Institute -- Pusa decomposer and crop residue management; Ministry of Agriculture and Farmers Welfare.",
  "env-stubble-happy-seeder-pusa", craft="inference")

M(PO, "medium", "On a November evening the air quality index in Delhi-NCR enters the 'severe' range, and the stage of the Graded Response Action Plan (GRAP) that halts most construction across the region has to be invoked. Which body invokes it?",
  "नवंबर की एक शाम दिल्ली-एनसीआर में वायु गुणवत्ता सूचकांक 'गंभीर' श्रेणी में पहुँच जाता है, और श्रेणीबद्ध प्रतिक्रिया कार्य योजना (GRAP) का वह चरण लागू करना है जो पूरे क्षेत्र में अधिकांश निर्माण कार्य रोकता है। इसे कौन लागू करता है?",
  ["Commission for Air Quality Management in NCR and Adjoining Areas",
   "Environment Pollution (Prevention and Control) Authority",
   "National Green Tribunal, through its principal bench",
   "Delhi Pollution Control Committee, under the Delhi Government's orders"],
  ["राष्ट्रीय राजधानी क्षेत्र और आसपास के क्षेत्रों में वायु गुणवत्ता प्रबंधन आयोग",
   "पर्यावरण प्रदूषण (रोकथाम और नियंत्रण) प्राधिकरण",
   "राष्ट्रीय हरित अधिकरण, अपनी प्रधान पीठ के माध्यम से",
   "दिल्ली सरकार के आदेशों के तहत दिल्ली प्रदूषण नियंत्रण समिति"],
  0,
  "Under the Commission for Air Quality Management in National Capital Region and Adjoining Areas Act, 2021, the Commission revises and invokes GRAP's stages as forecasts and readings worsen, and its directions prevail over those of other authorities in the region; a region-wide ban needs a body whose writ runs across Delhi, Haryana, Uttar Pradesh and Rajasthan. "
  "The trap is the Environment Pollution (Prevention and Control) Authority: appointed by the Supreme Court, it enforced GRAP when the plan was first notified in 2017, but it was dissolved in 2020 when the Commission was set up. The Delhi Pollution Control Committee's remit stops at Delhi's borders, and the National Green Tribunal decides cases rather than running the plan.",
  "राष्ट्रीय राजधानी क्षेत्र और आसपास के क्षेत्रों में वायु गुणवत्ता प्रबंधन आयोग अधिनियम, 2021 के तहत आयोग पूर्वानुमान और मापन बिगड़ने के साथ GRAP के चरणों में संशोधन करता है और उन्हें लागू करता है, और उसके निर्देश क्षेत्र के अन्य प्राधिकरणों पर प्रभावी होते हैं; पूरे क्षेत्र में प्रतिबंध के लिए ऐसा निकाय चाहिए जिसका अधिकार दिल्ली, हरियाणा, उत्तर प्रदेश और राजस्थान, सब पर चले। "
  "जाल पर्यावरण प्रदूषण (रोकथाम और नियंत्रण) प्राधिकरण है: सर्वोच्च न्यायालय द्वारा नियुक्त यह प्राधिकरण 2017 में योजना के पहली बार अधिसूचित होने पर GRAP लागू करता था, पर 2020 में आयोग बनने पर इसे भंग कर दिया गया। दिल्ली प्रदूषण नियंत्रण समिति का अधिकार दिल्ली की सीमा तक है, और राष्ट्रीय हरित अधिकरण मामलों का निर्णय करता है, योजना नहीं चलाता।",
  "Commission for Air Quality Management in National Capital Region and Adjoining Areas Act, 2021; CAQM -- Graded Response Action Plan.",
  "env-grap-caqm", craft="application")

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
  "env-earthworms-easy", craft="recall")

# ================================================================ CLIMATE SCIENCE (2)
S(CS, "medium", "Consider the following statements about weather systems:",
  "मौसम प्रणालियों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["An atmospheric river is a long, narrow band of concentrated water vapour carried in the lower atmosphere.",
   "A derecho is a slow-moving tropical cyclone that stalls over a coastline for several days.",
   "A weakening of the polar vortex keeps Arctic air locked near the pole, bringing unusually mild winters to the middle latitudes."],
  ["वायुमंडलीय नदी (atmospheric river) निचले वायुमंडल में बहने वाली घनी जलवाष्प की एक लंबी, सँकरी पट्टी है।",
   "डेरेचो (derecho) एक धीमा उष्णकटिबंधीय चक्रवात है जो कई दिनों तक किसी तट पर ठहरा रहता है।",
   "ध्रुवीय भँवर (polar vortex) के कमज़ोर पड़ने से आर्कटिक वायु ध्रुव के पास ही बँधी रहती है, जिससे मध्य अक्षांशों में असामान्य रूप से हल्की सर्दियाँ आती हैं।"],
  C3, 0,
  "Only statement 1 is correct. Atmospheric rivers carry moisture from the tropics toward higher latitudes and can drop torrential rain where they come ashore, as on the west coast of North America. "
  "Statement 2 is wrong: a derecho is a fast-moving, long-lived windstorm driven by a line of thunderstorms, which can flatten crops and forests along a path hundreds of kilometres long; it is not a cyclone. "
  "Statement 3 reverses the effect. The polar vortex is a band of strong westerly winds that holds cold air over the pole. When it weakens or splits, the cold air is no longer contained, and bitter cold spills south into North America, Europe or Asia -- the cause of several recent extreme cold spells.",
  "केवल कथन 1 सही है। वायुमंडलीय नदियाँ उष्णकटिबंध से ऊँचे अक्षांशों की ओर नमी ले जाती हैं और तट से टकराने पर मूसलाधार वर्षा कर सकती हैं, जैसे उत्तर अमेरिका के पश्चिमी तट पर। "
  "कथन 2 गलत है: डेरेचो तड़ित-झंझाओं की एक पंक्ति से उठने वाला तेज़, लंबे समय तक चलने वाला पवन-तूफ़ान है, जो सैकड़ों किलोमीटर लंबे रास्ते में फ़सलें और वन गिरा सकता है; यह चक्रवात नहीं है। "
  "कथन 3 प्रभाव को उलट देता है। ध्रुवीय भँवर प्रबल पछुआ पवनों की वह पट्टी है जो ठंडी वायु को ध्रुव के ऊपर थामे रखती है। इसके कमज़ोर पड़ने या टूटने पर ठंडी वायु बँधी नहीं रहती और कड़ाके की ठंड दक्षिण में उत्तर अमेरिका, यूरोप या एशिया तक फैल जाती है; हाल की कई चरम शीत लहरों का यही कारण रहा है।",
  "World Meteorological Organization -- International Meteorological Vocabulary; India Meteorological Department.",
  "env-atmospheric-river-derecho-polar-vortex", craft="inference")

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
  "env-glof-moraine-lakes", craft="inference")

if __name__ == "__main__":
    write_updates("gs_l2_t21_environment_v2.sql")
