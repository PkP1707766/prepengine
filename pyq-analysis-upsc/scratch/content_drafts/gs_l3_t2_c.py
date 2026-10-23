# -*- coding: utf-8 -*-
"""Level 3 · Test 2 (GS Integrated Test 2) -- part C: Environment & Ecology (15) (upsc_l3_cell_targets.mjs 2).
Environment cells: Flora e-MCQ, m-stmt; Fauna e-stmt, h-stmt, m-stmt; Pollution e-stmt, m-stmt; Conventions h-SI;
Laws & Bodies h-pairs; Climate Science m-MCQ, m-stmt; Protected Areas m-MCQ, m-stmt; Ecosystems m-stmt; Climate
Agreements m-stmt.
Every fact was grepped against the Level-2 digests, all Level-1 drafts and Level 3 Test 1, and is one none of them
tests: guchhi (morels); allelopathy; the black-necked crane; unihemispheric sleep; the Nicobar megapode; zero liquid
discharge and Tiruppur; the Comprehensive Environmental Pollution Index; trophic cascades (sea otters, Yellowstone);
the CO2 fertilisation effect; enhanced weathering, ocean iron fertilisation and LOHAFEX; Mission Innovation and the
Glasgow forests declaration; Barda as a second home for lions; the Veerangana Durgavati, Guru Ghasidas-Tamor Pingla
and Madhav tiger reserves; the Aarhus Convention; the Central Ground Water Authority, the Forest Advisory Committee,
the National Dam Safety Authority and the Central Empowered Committee. MCQ keys are pinned (pos)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, T2

d.SUBJECT = "Environment & Ecology"
d.REQUIRE_CRAFT = True
BIO12 = "NCERT Class XII, Biology (Organisms and Populations; Ecosystem; Biodiversity and Conservation)"
MOEF = "Ministry of Environment, Forest and Climate Change"
IUCN = "IUCN Red List of Threatened Species"
IPCC = "IPCC Sixth Assessment Report"
CPCB = "Central Pollution Control Board"

# ---------------------------------------------------------------- Flora, Fungi & Forests (e-MCQ, m-stmt)
M("Flora, Fungi & Forests", "easy",
  "Guchhi, among the costliest wild foods gathered in the forests of Jammu and Kashmir and Himachal Pradesh, is:",
  "जम्मू-कश्मीर और हिमाचल प्रदेश के वनों से इकट्ठा किए जाने वाले सबसे महँगे जंगली खाद्यों में से एक, गुच्छी, क्या है?",
  ["a morel, an edible fungus that comes up in spring",
   "a lichen that is dried and sold as the spice 'black stone flower'",
   "the young coiled frond of a fern, cooked as a vegetable",
   "a moss scraped from oak trunks and used in folk medicine"],
  ["एक मोरेल, वसंत में उगने वाला खाने योग्य कवक",
   "एक लाइकेन जिसे सुखाकर 'काला पत्थर फूल' मसाले के रूप में बेचा जाता है",
   "किसी फ़र्न की नई कुंडलित पत्ती, जो सब्ज़ी के रूप में पकाई जाती है",
   "बाँज के तनों से खुरचा गया एक मॉस, जो लोक औषधि में प्रयुक्त होता है"],
  0,
  "Guchhi is the morel (Morchella), a fungus with a honeycomb-like cap that appears for a few weeks in spring in moist conifer and mixed forests, often after the snow melts. It has resisted large-scale cultivation, so it is gathered by villagers and fetches a very high price when dried -- an example of how non-timber forest produce supports mountain incomes. "
  "The other options describe kalpasi (black stone flower, a lichen used in spice blends), lingad (the fiddlehead fern) and a moss.",
  "गुच्छी मोरेल (मोर्केला) है, मधुमक्खी के छत्ते जैसी टोपी वाला एक कवक जो वसंत में कुछ हफ़्तों के लिए नम शंकुधारी और मिश्रित वनों में, प्रायः बर्फ़ पिघलने के बाद, उगता है। इसकी बड़े पैमाने पर खेती नहीं हो पाई है, इसलिए इसे ग्रामीण इकट्ठा करते हैं और सूखने पर यह बहुत ऊँचे दाम पाता है -- यह इस बात का उदाहरण है कि ग़ैर-काष्ठ वन उपज पहाड़ी आय को कैसे सहारा देती है। "
  "बाक़ी विकल्प कल्पासी (काला पत्थर फूल, मसाला मिश्रणों में प्रयुक्त लाइकेन), लिंगड़ (फ़िडलहेड फ़र्न) और एक मॉस का वर्णन करते हैं।",
  "NCERT Class XI, Biology (Biological Classification: Kingdom Fungi); " + MOEF + ".",
  "l3-t2-env-guchhi-morel", pos=0, craft="recall")

S("Flora, Fungi & Forests", "medium", "Consider the following statements about allelopathy:",
  "ऐलीलोपैथी (परस्पर-विरोधी रासायनिक प्रभाव) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is the release by a plant of chemicals that hold back the germination or growth of other plants nearby.",
   "It is a form of parasitism in which a plant draws water and nutrients from the roots of its neighbours.",
   "The chemicals involved are released only through the roots, never from the leaves or fallen leaf litter."],
  ["यह किसी पौधे द्वारा ऐसे रसायन छोड़ना है जो आसपास के अन्य पौधों के अंकुरण या वृद्धि को रोकते हैं।",
   "यह परजीविता का एक रूप है जिसमें एक पौधा अपने पड़ोसियों की जड़ों से पानी और पोषक तत्व खींचता है।",
   "इसमें शामिल रसायन केवल जड़ों से छोड़े जाते हैं, पत्तियों या गिरी हुई पत्तियों के कूड़े से कभी नहीं।"],
  C3, 0,
  "Only statement 1 is correct. Allelopathic chemicals can be washed out of living leaves by rain, leached from leaf litter, given off as vapours or exuded by roots, so statement 3 is wrong. "
  "It is chemical competition, not parasitism -- a parasite such as Cuscuta taps its host, while an allelopathic plant merely suppresses its rivals. It helps explain why little grows under some eucalyptus plantations and why invasive weeds such as Parthenium spread so aggressively, and it is being studied as a natural means of weed control, for instance through crop residues and cover crops.",
  "केवल कथन 1 सही है। ऐलीलोपैथिक रसायन जीवित पत्तियों से वर्षा द्वारा धुल सकते हैं, पत्तियों के कूड़े से रिस सकते हैं, वाष्प के रूप में निकल सकते हैं या जड़ों से स्रावित हो सकते हैं, इसलिए कथन 3 ग़लत है। "
  "यह रासायनिक प्रतिस्पर्धा है, परजीविता नहीं -- अमरबेल जैसा परजीवी अपने परपोषी से पोषण लेता है, जबकि ऐलीलोपैथिक पौधा केवल अपने प्रतिद्वंद्वियों को दबाता है। इससे यह समझने में मदद मिलती है कि कुछ यूकेलिप्टस बाग़ानों के नीचे बहुत कम क्यों उगता है और पार्थेनियम जैसे आक्रामक खरपतवार इतनी तेज़ी से क्यों फैलते हैं, और फ़सल अवशेषों तथा आवरण फ़सलों के माध्यम से इसे खरपतवार नियंत्रण के प्राकृतिक साधन के रूप में परखा जा रहा है।",
  BIO12 + ".",
  "l3-t2-env-allelopathy", craft="precision")

# ---------------------------------------------------------------- Fauna & Animal Behaviour (e-stmt, h-stmt, m-stmt)
S("Fauna & Animal Behaviour", "easy", "Consider the following statements about the black-necked crane:",
  "काली गर्दन वाले सारस (ब्लैक-नेक्ड क्रेन) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It breeds on high-altitude wetlands of the Tibetan Plateau, including the Changthang region of Ladakh.",
   "It spends the winter in the mangrove forests of the Sundarbans."],
  ["यह तिब्बती पठार की, लद्दाख के चांगथांग क्षेत्र सहित, ऊँचाई वाली आर्द्रभूमियों में प्रजनन करता है।",
   "यह सर्दियाँ सुंदरबन के मैंग्रोव वनों में बिताता है।"],
  T2, 0,
  "Only statement 1 is correct. The black-necked crane, the only crane that lives at such heights, nests around the lakes and marshes of the Tibetan Plateau, and in India in the Changthang of Ladakh, which adopted it as its State bird in 2021. "
  "In winter it moves to lower, sheltered valleys -- in Bhutan, in Arunachal Pradesh (around Zemithang and Sangti) and in south-western China -- not to coastal mangroves. It is revered in Buddhist tradition and is now listed as Near Threatened.",
  "केवल कथन 1 सही है। इतनी ऊँचाई पर रहने वाला एकमात्र सारस, काली गर्दन वाला सारस, तिब्बती पठार की झीलों और दलदलों के आसपास, और भारत में लद्दाख के चांगथांग में घोंसले बनाता है, जिसने 2021 में इसे अपना राज्य पक्षी चुना। "
  "सर्दियों में यह निचली, सुरक्षित घाटियों में जाता है -- भूटान में, अरुणाचल प्रदेश में (ज़ेमिथांग और सांगती के आसपास) और दक्षिण-पश्चिमी चीन में -- तटीय मैंग्रोव में नहीं। बौद्ध परंपरा में यह पूजनीय है और अब निकट-संकटग्रस्त सूची में है।",
  f"{IUCN}; {MOEF}.",
  "l3-t2-env-black-necked-crane", craft="recall")

S("Fauna & Animal Behaviour", "hard", "Consider the following statements about sleep in animals:",
  "जंतुओं में नींद के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Some birds and marine mammals such as dolphins can sleep with one half of the brain while the other half stays awake.",
   "Such sleep has been recorded in frigatebirds in flight over the ocean, letting them rest during flights that last for weeks.",
   "In this kind of sleep, the eye that stays open is the one linked to the sleeping half of the brain."],
  ["कुछ पक्षी और डॉल्फ़िन जैसे समुद्री स्तनधारी मस्तिष्क के एक आधे भाग से सो सकते हैं जबकि दूसरा आधा जागता रहता है।",
   "ऐसी नींद समुद्र के ऊपर उड़ते फ़्रिगेटबर्ड में दर्ज की गई है, जिससे वे हफ़्तों चलने वाली उड़ानों के दौरान आराम कर पाते हैं।",
   "इस प्रकार की नींद में जो आँख खुली रहती है, वह मस्तिष्क के सोते हुए आधे भाग से जुड़ी होती है।"],
  C3, 1,
  "Statements 1 and 2 are correct. In unihemispheric sleep one cerebral hemisphere shows the slow waves of deep sleep while the other stays alert. Dolphins use it to keep surfacing to breathe and to watch for danger, and recordings of frigatebirds have shown them sleeping in short bursts, often one hemisphere at a time, while gliding for days over the sea. "
  "Statement 3 is wrong: the open eye is linked to the awake hemisphere, so that it can keep watch -- mallards at the end of a row of sleeping ducks keep their outward-facing eye open.",
  "कथन 1 और 2 सही हैं। एक-गोलार्ध नींद में मस्तिष्क का एक गोलार्ध गहरी नींद की धीमी तरंगें दिखाता है जबकि दूसरा सजग रहता है। डॉल्फ़िन इसका उपयोग साँस लेने के लिए बार-बार सतह पर आने और ख़तरे पर नज़र रखने के लिए करती हैं, और फ़्रिगेटबर्ड की रिकॉर्डिंग ने दिखाया है कि वे समुद्र के ऊपर दिनों तक सरकते हुए छोटे-छोटे अंतरालों में, प्रायः एक बार में एक गोलार्ध से, सोते हैं। "
  "कथन 3 ग़लत है: खुली आँख जागते हुए गोलार्ध से जुड़ी होती है, ताकि वह पहरा दे सके -- सोती बत्तखों की पंक्ति के सिरे पर बैठी मैलार्ड बत्तखें अपनी बाहर की ओर वाली आँख खुली रखती हैं।",
  BIO12 + "; NCERT Class XI, Biology (Neural Control and Coordination).",
  "l3-t2-env-unihemispheric-sleep", craft="inference")

S("Fauna & Animal Behaviour", "medium", "Consider the following statements about the Nicobar megapode:",
  "निकोबार मेगापोड के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It lays its eggs in large mounds of soil and leaf litter, where the heat of decomposition incubates them.",
   "In the wild it is found only in the Nicobar group of islands.",
   "The tsunami of 2004 destroyed many of its nesting mounds along the coast."],
  ["यह अपने अंडे मिट्टी और पत्तियों के कूड़े के बड़े टीलों में देता है, जहाँ अपघटन की ऊष्मा उन्हें सेती है।",
   "वन्य अवस्था में यह केवल निकोबार द्वीप-समूह में पाया जाता है।",
   "2004 की सुनामी ने तट के किनारे इसके कई घोंसला-टीले नष्ट कर दिए।"],
  C3, 2,
  "All three statements are correct. Megapodes ('big feet') do not sit on their eggs: the Nicobar megapode scrapes together mounds of sand, soil and rotting leaves near the shore, and the chicks hatch fully feathered and fend for themselves from the start. "
  "The bird is endemic to the Nicobar Islands, is listed as Vulnerable and is protected under Schedule I of the Wild Life (Protection) Act; because it nests in coastal forest, the tsunami hit it hard, and large projects on Great Nicobar have raised fresh concern for its habitat.",
  "तीनों कथन सही हैं। मेगापोड ('बड़े पैर') अपने अंडों पर नहीं बैठते: निकोबार मेगापोड तट के पास रेत, मिट्टी और सड़ती पत्तियों के टीले इकट्ठा करता है, और चूज़े पूरे पंखों के साथ निकलते हैं और शुरुआत से ही अपना ध्यान स्वयं रखते हैं। "
  "यह पक्षी निकोबार द्वीपों में स्थानिक है, सुभेद्य सूची में है और वन्यजीव (संरक्षण) अधिनियम की अनुसूची I में संरक्षित है; चूँकि यह तटीय वन में घोंसला बनाता है, सुनामी ने इसे भारी चोट पहुँचाई, और ग्रेट निकोबार पर बड़ी परियोजनाओं ने इसके आवास के लिए नई चिंता पैदा की है।",
  f"{IUCN}; Wild Life (Protection) Act, 1972, Schedule I; Zoological Survey of India.",
  "l3-t2-env-nicobar-megapode", craft="linkage")

# ---------------------------------------------------------------- Pollution, Waste & Resources (e-stmt, m-stmt)
S("Pollution, Waste & Resources", "easy", "Consider the following statements about zero liquid discharge (ZLD):",
  "शून्य तरल निर्वहन (ZLD) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It means that an industrial unit treats and recycles all its wastewater, so that no liquid effluent leaves its premises.",
   "Courts have required it of the textile dyeing and bleaching units of the Tiruppur cluster in Tamil Nadu."],
  ["इसका अर्थ है कि कोई औद्योगिक इकाई अपना सारा अपशिष्ट जल उपचारित और पुनर्चक्रित करती है, ताकि कोई तरल बहिःस्राव उसके परिसर से बाहर न जाए।",
   "न्यायालयों ने तमिलनाडु के तिरुप्पुर क्लस्टर की कपड़ा रँगाई और विरंजन इकाइयों से इसकी अपेक्षा की है।"],
  T2, 2,
  "Both statements are correct. A ZLD plant goes beyond ordinary effluent treatment: after treatment, reverse osmosis recovers most of the water for reuse, and evaporators and crystallisers turn the remaining brine into solid salts. "
  "Tiruppur's dyeing units had badly polluted the Noyyal river, and the Madras High Court's orders, including the closure of units in 2011, pushed the cluster to ZLD. The approach saves water but is costly and energy-hungry, and it leaves salt that must itself be managed; the CPCB has also pressed it on distilleries, tanneries and textile units in the Ganga basin.",
  "दोनों कथन सही हैं। ZLD संयंत्र सामान्य बहिःस्राव उपचार से आगे जाता है: उपचार के बाद रिवर्स ऑस्मोसिस अधिकांश पानी पुनः उपयोग के लिए निकाल लेता है, और वाष्पित्र तथा क्रिस्टलक बचे हुए खारे पानी को ठोस लवणों में बदल देते हैं। "
  "तिरुप्पुर की रँगाई इकाइयों ने नोय्यल नदी को बुरी तरह प्रदूषित किया था, और 2011 में इकाइयों को बंद करने सहित मद्रास उच्च न्यायालय के आदेशों ने क्लस्टर को ZLD की ओर धकेला। यह तरीक़ा पानी बचाता है पर महँगा और ऊर्जा-भूखा है, और ऐसा लवण छोड़ता है जिसका स्वयं प्रबंधन करना पड़ता है; CPCB ने गंगा बेसिन में आसवनियों, चर्मशोधनशालाओं और कपड़ा इकाइयों पर भी इसका दबाव डाला है।",
  f"{CPCB}; Madras High Court (Noyyal river cases).",
  "l3-t2-env-zero-liquid-discharge", craft="application")

S("Pollution, Waste & Resources", "medium", "Consider the following statements about the Comprehensive Environmental Pollution Index (CEPI):",
  "व्यापक पर्यावरणीय प्रदूषण सूचकांक (CEPI) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It considers only air quality around industrial clusters.",
   "Clusters that score below 70 on it are labelled 'critically polluted'.",
   "It was developed by NITI Aayog to rank States for central grants."],
  ["यह औद्योगिक क्लस्टरों के आसपास केवल वायु गुणवत्ता पर विचार करता है।",
   "इस पर 70 से कम अंक पाने वाले क्लस्टरों को 'गंभीर रूप से प्रदूषित' कहा जाता है।",
   "इसे नीति आयोग ने केंद्रीय अनुदानों के लिए राज्यों को श्रेणीबद्ध करने हेतु विकसित किया।"],
  C3, 3,
  "None of the statements is correct. The CEPI, developed by the Central Pollution Control Board with IIT Delhi in 2009, rates industrial clusters on the pollution of their air, water and land, taking into account the scale of pollution, the people exposed and the health effects. "
  "A score of 70 or more marks a cluster as 'critically polluted' (60 to 70 is 'severely polluted'); in the first assessment 43 of the 88 clusters studied, including Ankleshwar and Vapi in Gujarat, were critically polluted, and a moratorium on new projects in such clusters followed in 2010. It is a tool for regulating clusters, not for allocating grants among States.",
  "कोई भी कथन सही नहीं है। 2009 में केंद्रीय प्रदूषण नियंत्रण बोर्ड द्वारा IIT दिल्ली के साथ विकसित CEPI औद्योगिक क्लस्टरों को उनकी वायु, जल और भूमि के प्रदूषण पर आँकता है, जिसमें प्रदूषण का पैमाना, प्रभावित लोग और स्वास्थ्य प्रभाव ध्यान में रखे जाते हैं। "
  "70 या अधिक अंक क्लस्टर को 'गंभीर रूप से प्रदूषित' (60 से 70 'अत्यधिक प्रदूषित') चिह्नित करते हैं; पहले आकलन में अध्ययन किए गए 88 में से 43 क्लस्टर, जिनमें गुजरात के अंकलेश्वर और वापी शामिल थे, गंभीर रूप से प्रदूषित थे, और 2010 में ऐसे क्लस्टरों में नई परियोजनाओं पर रोक लगी। यह क्लस्टरों के विनियमन का साधन है, राज्यों में अनुदान बाँटने का नहीं।",
  f"{CPCB} (Comprehensive Environmental Pollution Index, 2009); {MOEF}.",
  "l3-t2-env-cepi-critically-polluted", craft="precision")

# ---------------------------------------------------------------- Ecosystems & Ecological Processes (m-stmt)
S("Ecosystems & Ecological Processes", "medium", "Consider the following statements about trophic cascades:",
  "पोषण सोपानी प्रभावों (ट्रॉफ़िक कैस्केड) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Where sea otters are present, they keep sea-urchin numbers down and so allow kelp forests to grow.",
   "The return of wolves to Yellowstone National Park in 1995 is widely cited as having helped streamside willows recover, as elk browsed them less.",
   "In a trophic cascade, effects travel only upwards from plants to predators, never downwards."],
  ["जहाँ समुद्री ऊदबिलाव मौजूद होते हैं, वे समुद्री अर्चिन की संख्या कम रखते हैं और इस प्रकार केल्प वनों को बढ़ने देते हैं।",
   "1995 में येलोस्टोन राष्ट्रीय उद्यान में भेड़ियों की वापसी को प्रायः इस रूप में उद्धृत किया जाता है कि इससे धाराओं के किनारे के विलो पेड़ फिर पनपे, क्योंकि एल्क उन्हें कम चरने लगे।",
   "ट्रॉफ़िक कैस्केड में प्रभाव केवल नीचे से ऊपर, पौधों से परभक्षियों की ओर जाते हैं, कभी ऊपर से नीचे नहीं।"],
  C3, 1,
  "Statements 1 and 2 are correct. A trophic cascade is an indirect effect of a predator on plants, two or more links down a food chain: otters eat urchins, urchins graze kelp, so losing the otters turns kelp forests into urchin 'barrens'; wolves reduce and unsettle elk, easing the browsing pressure on young trees (though how large the Yellowstone effect was is still debated). "
  "Statement 3 is wrong: the classic cascades are top-down, which is why the removal of top predators, such as tigers or wolves, can change the vegetation of an entire landscape and why such predators are often keystone species.",
  "कथन 1 और 2 सही हैं। ट्रॉफ़िक कैस्केड किसी परभक्षी का खाद्य शृंखला में दो या अधिक कड़ियाँ नीचे के पौधों पर अप्रत्यक्ष प्रभाव है: ऊदबिलाव अर्चिन खाते हैं, अर्चिन केल्प चरते हैं, इसलिए ऊदबिलावों के खोने से केल्प वन अर्चिन की 'बंजर भूमि' बन जाते हैं; भेड़िये एल्क की संख्या घटाते और उन्हें बेचैन रखते हैं, जिससे नए पेड़ों पर चराई का दबाव घटता है (यद्यपि येलोस्टोन प्रभाव कितना बड़ा था, इस पर अब भी बहस है)। "
  "कथन 3 ग़लत है: क्लासिक कैस्केड ऊपर से नीचे होते हैं, इसीलिए बाघ या भेड़िये जैसे शीर्ष परभक्षियों को हटाने से पूरे भू-दृश्य की वनस्पति बदल सकती है और इसीलिए ऐसे परभक्षी प्रायः कीस्टोन प्रजातियाँ होते हैं।",
  BIO12 + ".",
  "l3-t2-env-trophic-cascades", craft="inference")

# ---------------------------------------------------------------- Climate Science & Mitigation (m-MCQ, m-stmt)
M("Climate Science & Mitigation", "medium",
  "Climate scientists speak of a 'CO2 fertilisation effect'. It refers to:",
  "जलवायु वैज्ञानिक 'CO2 उर्वरीकरण प्रभाव' की बात करते हैं। यह किसे दर्शाता है?",
  ["farmers applying more nitrogen fertiliser, which releases more carbon dioxide",
   "the ocean giving off more carbon dioxide as it warms, which speeds further warming",
   "the use of captured carbon dioxide to make urea in fertiliser plants",
   "plants growing faster as CO2 rises, so that land vegetation absorbs more carbon"],
  ["किसानों द्वारा अधिक नाइट्रोजन उर्वरक डालना, जिससे अधिक कार्बन डाइऑक्साइड निकलती है",
   "गर्म होने पर महासागर का अधिक कार्बन डाइऑक्साइड छोड़ना, जिससे तापन और तेज़ होता है",
   "उर्वरक संयंत्रों में यूरिया बनाने के लिए पकड़ी गई कार्बन डाइऑक्साइड का उपयोग",
   "CO2 बढ़ने पर पौधों का तेज़ी से बढ़ना, जिससे स्थलीय वनस्पति अधिक कार्बन सोखती है"],
  3,
  "Higher CO2 speeds photosynthesis in C3 plants -- most trees, wheat and rice -- and lets them lose less water through their stomata. This is a main reason the land 'sink' has grown and absorbs roughly a quarter to a third of human CO2 emissions. "
  "The effect is limited by nitrogen, water and heat, is weaker in C4 crops such as maize and sugarcane, and can lower the protein and zinc content of grains -- so it slows warming but cannot be relied on to cancel emissions.",
  "अधिक CO2 C3 पौधों -- अधिकांश पेड़, गेहूँ और चावल -- में प्रकाश-संश्लेषण तेज़ करती है और उन्हें रंध्रों से कम पानी खोने देती है। यही एक मुख्य कारण है कि स्थलीय 'सिंक' बढ़ा है और मानव CO2 उत्सर्जन का लगभग एक-चौथाई से एक-तिहाई सोखता है। "
  "यह प्रभाव नाइट्रोजन, पानी और ताप से सीमित है, मक्का और गन्ने जैसी C4 फ़सलों में कमज़ोर है, और अनाज में प्रोटीन और ज़िंक की मात्रा घटा सकता है -- इसलिए यह तापन को धीमा करता है पर उत्सर्जन को रद्द करने के लिए इस पर भरोसा नहीं किया जा सकता।",
  f"{IPCC} (Working Group I, carbon cycle).",
  "l3-t2-env-co2-fertilisation-effect", pos=3, craft="precision")

S("Climate Science & Mitigation", "medium", "Consider the following statements about proposed ways of removing carbon dioxide from the atmosphere:",
  "वायुमंडल से कार्बन डाइऑक्साइड हटाने के प्रस्तावित तरीक़ों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Enhanced rock weathering spreads finely ground silicate rock such as basalt on farmland, to speed up the natural reactions that draw carbon dioxide out of the air.",
   "Ocean iron fertilisation seeks to trigger plankton blooms that take up carbon dioxide, in seas where iron is the nutrient in short supply.",
   "Ocean fertilisation other than legitimate scientific research is restricted under the London Convention and Protocol on dumping at sea."],
  ["संवर्धित शैल अपक्षय खेतों पर बेसाल्ट जैसी बारीक पिसी सिलिकेट चट्टान फैलाता है, ताकि हवा से कार्बन डाइऑक्साइड खींचने वाली प्राकृतिक अभिक्रियाएँ तेज़ हों।",
   "महासागरीय लौह उर्वरीकरण उन समुद्रों में प्लवक के प्रस्फुटन कराने का प्रयास करता है जहाँ लोहा ही कम उपलब्ध पोषक तत्व है, ताकि वे कार्बन डाइऑक्साइड सोखें।",
   "वैध वैज्ञानिक शोध के अलावा महासागरीय उर्वरीकरण समुद्र में डंपिंग पर लंदन अभिसमय और प्रोटोकॉल के अंतर्गत प्रतिबंधित है।"],
  C3, 2,
  "All three statements are correct. In enhanced weathering, rainwater carrying dissolved CO2 reacts with the crushed silicate minerals to form bicarbonates that are washed to the sea and stored for very long periods, with a side benefit of less acidic soil. "
  "Iron fertilisation targets 'high-nutrient, low-chlorophyll' waters such as the Southern Ocean; the Indo-German LOHAFEX experiment of 2009 showed that much of the carbon taken up by a bloom may not sink to the deep ocean, and the risks to marine ecosystems led the parties to the London Convention and Protocol to allow it only for legitimate research. "
  "Both methods, unlike planting trees, are still unproven at scale, which is why emission cuts remain the main route.",
  "तीनों कथन सही हैं। संवर्धित अपक्षय में घुली हुई CO2 वाला वर्षा जल पिसे सिलिकेट खनिजों से अभिक्रिया कर बाइकार्बोनेट बनाता है जो समुद्र में बहकर बहुत लंबे समय तक संचित रहते हैं, साथ में मिट्टी की अम्लता घटने का लाभ भी है। "
  "लौह उर्वरीकरण दक्षिणी महासागर जैसे 'उच्च-पोषक, निम्न-पर्णहरित' जल को लक्ष्य बनाता है; 2009 के भारत-जर्मन LOHAFEX प्रयोग ने दिखाया कि प्रस्फुटन द्वारा सोखा गया बहुत-सा कार्बन गहरे महासागर तक नहीं डूबता, और समुद्री पारितंत्रों के जोखिमों के कारण लंदन अभिसमय और प्रोटोकॉल के पक्षकारों ने इसे केवल वैध शोध के लिए अनुमति दी। "
  "पेड़ लगाने के विपरीत दोनों तरीक़े बड़े पैमाने पर अब भी अप्रमाणित हैं, इसीलिए उत्सर्जन में कटौती ही मुख्य रास्ता बनी हुई है।",
  f"{IPCC} (Working Group III, carbon dioxide removal); London Convention and Protocol (resolution on ocean fertilisation, 2008).",
  "l3-t2-env-weathering-iron-fertilisation", craft="linkage")

# ---------------------------------------------------------------- Climate Agreements & Carbon Markets (m-stmt)
S("Climate Agreements & Carbon Markets", "medium", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Mission Innovation was launched at the Glasgow climate summit of 2021 to accelerate public investment in clean-energy research.",
   "Under the Glasgow Leaders' Declaration on Forests and Land Use (2021), more than 140 countries committed to halt and reverse forest loss and land degradation by 2030.",
   "India signed the Glasgow Leaders' Declaration on Forests and Land Use."],
  ["मिशन इनोवेशन 2021 के ग्लासगो जलवायु शिखर सम्मेलन में स्वच्छ-ऊर्जा अनुसंधान में सार्वजनिक निवेश तेज़ करने के लिए शुरू किया गया।",
   "वनों और भूमि उपयोग पर ग्लासगो नेताओं की घोषणा (2021) के अंतर्गत 140 से अधिक देशों ने 2030 तक वन-हानि और भूमि-क्षरण को रोकने और पलटने की प्रतिबद्धता की।",
   "भारत ने वनों और भूमि उपयोग पर ग्लासगो नेताओं की घोषणा पर हस्ताक्षर किए।"],
  C3, 0,
  "Only statement 2 is correct. Statement 1 is wrong: Mission Innovation was launched alongside the Paris summit (COP21) in 2015, with India among its founding members, by governments that pledged to raise clean-energy research spending; its second phase from 2021 set 'missions' on themes such as clean hydrogen and green power. "
  "The Glasgow declaration, signed at COP26 by countries holding most of the world's forests, is a voluntary political pledge without binding targets. Statement 3 is wrong: India stayed out of it, reportedly over concerns that its language on trade and land use could restrict development and infrastructure.",
  "केवल कथन 2 सही है। कथन 1 ग़लत है: मिशन इनोवेशन 2015 में पेरिस शिखर सम्मेलन (COP21) के साथ उन सरकारों ने शुरू किया जिन्होंने स्वच्छ-ऊर्जा अनुसंधान पर व्यय बढ़ाने का संकल्प लिया, और भारत इसके संस्थापक सदस्यों में था; 2021 से इसके दूसरे चरण ने स्वच्छ हाइड्रोजन और हरित बिजली जैसे विषयों पर 'मिशन' तय किए। "
  "COP26 में विश्व के अधिकांश वनों वाले देशों द्वारा हस्ताक्षरित ग्लासगो घोषणा बिना बाध्यकारी लक्ष्यों वाली एक स्वैच्छिक राजनीतिक प्रतिज्ञा है। कथन 3 ग़लत है: भारत इससे बाहर रहा, कथित रूप से इस चिंता के कारण कि व्यापार और भूमि उपयोग पर इसकी भाषा विकास और अवसंरचना को सीमित कर सकती है।",
  f"Mission Innovation; UN Climate Change Conference COP26 (Glasgow Leaders' Declaration on Forests and Land Use, 2021); {MOEF}.",
  "l3-t2-env-mission-innovation-glasgow-forests", craft="precision")

# ---------------------------------------------------------------- Protected Areas & Wildlife Protection (m-MCQ, m-stmt)
M("Protected Areas & Wildlife Protection", "medium",
  "Barda Wildlife Sanctuary in Gujarat, where animals have begun to settle on their own in recent years, is being developed as a second home for which species?",
  "गुजरात का बरडा वन्यजीव अभयारण्य, जहाँ हाल के वर्षों में जानवर स्वयं बसने लगे हैं, किस प्रजाति के दूसरे घर के रूप में विकसित किया जा रहा है?",
  ["The great Indian bustard", "The Indian wild ass", "The Asiatic lion", "The cheetah"],
  ["सोन चिरैया (ग्रेट इंडियन बस्टर्ड)", "भारतीय जंगली गधा", "एशियाई सिंह", "चीता"],
  2,
  "Asiatic lions survive in the wild only in the Saurashtra region of Gujarat, centred on Gir, and keeping a single population in one landscape exposes it to an epidemic or disaster. As their numbers have grown, lions have spread across Saurashtra and some have reached Barda, near Porbandar, on their own; Gujarat is preparing it as a second home under Project Lion. "
  "Kuno in Madhya Pradesh, once chosen for lions, has instead received cheetahs; the great Indian bustard and the wild ass are associated with Kutch and the Rann.",
  "एशियाई सिंह वन्य अवस्था में केवल गुजरात के सौराष्ट्र क्षेत्र में, गिर के आसपास, बचे हैं, और एक ही भू-दृश्य में एकमात्र आबादी रखना उसे महामारी या आपदा के जोखिम में डालता है। संख्या बढ़ने के साथ सिंह सौराष्ट्र में फैल गए हैं और कुछ स्वयं पोरबंदर के पास बरडा तक पहुँच गए हैं; गुजरात प्रोजेक्ट लायन के अंतर्गत इसे दूसरे घर के रूप में तैयार कर रहा है। "
  "मध्य प्रदेश का कूनो, जो कभी सिंहों के लिए चुना गया था, अब चीतों का घर है; सोन चिरैया और जंगली गधा कच्छ और रण से जुड़े हैं।",
  f"{MOEF} (Project Lion); Gujarat Forest Department.",
  "l3-t2-env-barda-second-lion-home", pos=2, craft="linkage")

S("Protected Areas & Wildlife Protection", "medium", "Consider the following statements about India's newer tiger reserves:",
  "भारत के नए बाघ अभयारण्यों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Veerangana Durgavati Tiger Reserve in Madhya Pradesh includes the Nauradehi Wildlife Sanctuary.",
   "Guru Ghasidas-Tamor Pingla Tiger Reserve lies in Odisha.",
   "Madhav National Park, notified as a tiger reserve in 2025, is in Rajasthan."],
  ["मध्य प्रदेश का वीरांगना दुर्गावती बाघ अभयारण्य नौरादेही वन्यजीव अभयारण्य को शामिल करता है।",
   "गुरु घासीदास-तमोर पिंगला बाघ अभयारण्य ओडिशा में है।",
   "2025 में बाघ अभयारण्य के रूप में अधिसूचित माधव राष्ट्रीय उद्यान राजस्थान में है।"],
  C3, 0,
  "Only statement 1 is correct. Veerangana Durgavati (2023) joins the Nauradehi and Durgavati sanctuaries in the Sagar-Damoh-Narsinghpur region; Nauradehi had earlier been considered for the reintroduction of cheetahs. "
  "Guru Ghasidas-Tamor Pingla (2024), formed from Guru Ghasidas National Park and Tamor Pingla Sanctuary in northern Chhattisgarh, is among the largest tiger reserves in the country and links forests towards Madhya Pradesh and Jharkhand. "
  "Madhav National Park is near Shivpuri in Madhya Pradesh, which now has more tiger reserves than any other State.",
  "केवल कथन 1 सही है। वीरांगना दुर्गावती (2023) सागर-दमोह-नरसिंहपुर क्षेत्र में नौरादेही और दुर्गावती अभयारण्यों को जोड़ता है; नौरादेही पर पहले चीतों के पुनर्वास के लिए विचार किया गया था। "
  "उत्तरी छत्तीसगढ़ में गुरु घासीदास राष्ट्रीय उद्यान और तमोर पिंगला अभयारण्य से बना गुरु घासीदास-तमोर पिंगला (2024) देश के सबसे बड़े बाघ अभयारण्यों में से है और मध्य प्रदेश तथा झारखंड की ओर वनों को जोड़ता है। "
  "माधव राष्ट्रीय उद्यान मध्य प्रदेश में शिवपुरी के पास है, जिसके पास अब किसी भी अन्य राज्य से अधिक बाघ अभयारण्य हैं।",
  f"National Tiger Conservation Authority; {MOEF}.",
  "l3-t2-env-new-tiger-reserves", craft="precision")

# ---------------------------------------------------------------- International Conventions & Organisations (h-SI)
A("International Conventions & Organisations", "hard",
  "The Aarhus Convention gives the public rights of access to environmental information, of participation in environmental decision-making and of access to justice in environmental matters.",
  "आरहूस अभिसमय जनता को पर्यावरणीय सूचना तक पहुँच, पर्यावरणीय निर्णय-निर्माण में भागीदारी और पर्यावरणीय मामलों में न्याय तक पहुँच के अधिकार देता है।",
  "The Aarhus Convention was negotiated under the United Nations Economic Commission for Europe.",
  "आरहूस अभिसमय पर संयुक्त राष्ट्र यूरोपीय आर्थिक आयोग के अंतर्गत वार्ता हुई थी।",
  1,
  "Both statements are correct, but Statement-II does not explain Statement-I. The Aarhus Convention (1998, in force 2001) rests on three pillars -- information, participation and justice -- and links environmental protection with democratic rights; where it was negotiated says nothing about why it grants these rights. "
  "Being a UNECE treaty, its parties are mainly in Europe and Central Asia, and India is not a party. Latin America's counterpart, the Escazú Agreement (2018, in force 2021), adds the first treaty provisions on protecting environmental human-rights defenders. In India, similar rights come through the Right to Information Act, public hearings under the EIA notification and the National Green Tribunal.",
  "दोनों कथन सही हैं, पर कथन-II कथन-I की व्याख्या नहीं करता। आरहूस अभिसमय (1998, 2001 से लागू) तीन स्तंभों -- सूचना, भागीदारी और न्याय -- पर टिका है और पर्यावरण संरक्षण को लोकतांत्रिक अधिकारों से जोड़ता है; इस पर वार्ता कहाँ हुई, यह इस बारे में कुछ नहीं कहता कि वह ये अधिकार क्यों देता है। "
  "UNECE संधि होने के कारण इसके पक्षकार मुख्यतः यूरोप और मध्य एशिया में हैं, और भारत इसका पक्षकार नहीं है। लैटिन अमेरिका का समकक्ष, एस्काज़ू समझौता (2018, 2021 से लागू), पर्यावरणीय मानवाधिकार रक्षकों की सुरक्षा पर पहले संधि-उपबंध जोड़ता है। भारत में ऐसे अधिकार सूचना का अधिकार अधिनियम, EIA अधिसूचना के अंतर्गत जन-सुनवाई और राष्ट्रीय हरित अधिकरण से मिलते हैं।",
  "UNECE Convention on Access to Information, Public Participation in Decision-making and Access to Justice in Environmental Matters (Aarhus, 1998); UN ECLAC (Escazú Agreement, 2018).",
  "l3-t2-env-aarhus-convention", craft="inference")

# ---------------------------------------------------------------- Indian Environmental Laws & Bodies (h-pairs)
P("Indian Environmental Laws & Bodies", "hard", "Consider the following pairs of bodies and the laws under which they were constituted:",
  "निकायों और उन क़ानूनों के निम्नलिखित युग्मों पर विचार कीजिए जिनके अंतर्गत उनका गठन हुआ:",
  ["Central Ground Water Authority : Environment (Protection) Act, 1986",
   "Forest Advisory Committee : Forest (Conservation) Act, 1980",
   "National Dam Safety Authority : Dam Safety Act, 2021",
   "Central Empowered Committee (as reconstituted in 2023) : Environment (Protection) Act, 1986"],
  ["केंद्रीय भूजल प्राधिकरण : पर्यावरण (संरक्षण) अधिनियम, 1986",
   "वन सलाहकार समिति : वन (संरक्षण) अधिनियम, 1980",
   "राष्ट्रीय बाँध सुरक्षा प्राधिकरण : बाँध सुरक्षा अधिनियम, 2021",
   "केंद्रीय अधिकार-प्राप्त समिति (2023 में पुनर्गठित रूप में) : पर्यावरण (संरक्षण) अधिनियम, 1986"],
  3,
  "All four pairs are correct. The Central Ground Water Authority was constituted in 1997 under section 3(3) of the Environment (Protection) Act, on the Supreme Court's direction, to regulate groundwater extraction; the Forest Advisory Committee advises the Union on proposals to divert forest land under section 3 of the Forest Conservation Act, renamed the Van (Sanrakshan Evam Samvardhan) Adhiniyam in 2023. "
  "The National Dam Safety Authority was set up under the Dam Safety Act, 2021 to oversee the safety of large dams. The Central Empowered Committee, first created by the Supreme Court in 2002 to monitor its forest and wildlife orders, was made a permanent body under section 3(3) of the Environment (Protection) Act in 2023 -- one more example of that Act serving as the umbrella under which new regulators are created.",
  "चारों युग्म सही हैं। केंद्रीय भूजल प्राधिकरण का गठन 1997 में सर्वोच्च न्यायालय के निर्देश पर, भूजल दोहन के विनियमन के लिए, पर्यावरण (संरक्षण) अधिनियम की धारा 3(3) के अंतर्गत हुआ; वन सलाहकार समिति वन संरक्षण अधिनियम, जिसका नाम 2023 में वन (संरक्षण एवं संवर्धन) अधिनियम हुआ, की धारा 3 के अंतर्गत वन भूमि के अपवर्तन के प्रस्तावों पर संघ को सलाह देती है। "
  "राष्ट्रीय बाँध सुरक्षा प्राधिकरण बड़े बाँधों की सुरक्षा की निगरानी के लिए बाँध सुरक्षा अधिनियम, 2021 के अंतर्गत बना। केंद्रीय अधिकार-प्राप्त समिति, जिसे पहली बार 2002 में सर्वोच्च न्यायालय ने अपने वन और वन्यजीव आदेशों की निगरानी के लिए बनाया था, 2023 में पर्यावरण (संरक्षण) अधिनियम की धारा 3(3) के अंतर्गत स्थायी निकाय बनाई गई -- यह इस बात का एक और उदाहरण है कि यह अधिनियम नए नियामक बनाने का छत्र कैसे बनता है।",
  f"{MOEF} (notifications under the Environment (Protection) Act, 1986, s.3(3), 1997 and 2023); Forest (Conservation) Act, 1980; Dam Safety Act, 2021.",
  "l3-t2-env-bodies-cgwa-fac-ndsa-cec", craft="precision")

write("gs_l3_t2_c.sql")
