# -*- coding: utf-8 -*-
"""Level 4 · Simulator 2 (GS Paper I full mock, Layout B: the 2025 shape) -- part D: Geography (6)
(upsc_l4_gs_cell_targets.mjs 2).
Every tested proposition was swept against the whole UPSC bank and no row tests it: Antarctic Bottom Water and North
Atlantic Deep Water; Wadati-Benioff zones; Kalsubai, Saramati, the Satmala-Ajanta hills and the Utkal plains;
Hussain Sagar; kimberlite pipes; the Coral Sea, the Gulf of Carpentaria, Lake Eyre and the Sea of Okhotsk. MCQ keys
are pinned (pos)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Geography"
d.REQUIRE_CRAFT = True

# ---------------------------------------------------------------- Climatology & Biomes (statement, medium)
S("Climatology & Biomes", "medium", "With reference to the deep water masses of the oceans, consider the following statements:",
  "महासागरों की गहरी जलराशियों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Antarctic Bottom Water, the densest water mass in the open ocean, forms mainly in the Weddell and Ross Seas.",
   "When sea ice forms, it leaves salt behind in the water beneath, which makes that water denser.",
   "North Atlantic Deep Water is denser than Antarctic Bottom Water, and so lies beneath it."],
  ["खुले महासागर की सबसे सघन जलराशि, अंटार्कटिक तलीय जल, मुख्यतः वेडेल और रॉस सागरों में बनती है।",
   "समुद्री बर्फ़ बनने पर वह नीचे के जल में लवण छोड़ देती है, जिससे वह जल अधिक सघन हो जाता है।",
   "उत्तर अटलांटिक गहन जल अंटार्कटिक तलीय जल से अधिक सघन है, और इसलिए उसके नीचे रहता है।"],
  C3, 1,
  "Only statements 1 and 2 are correct. Around Antarctica, especially on the continental shelves of the Weddell and Ross Seas, intense cooling and the formation of sea ice -- which rejects most of the salt into the water below -- produce very cold, salty water that sinks down the continental slope and spreads along the ocean floor as Antarctic Bottom Water, reaching far into the Atlantic, Indian and Pacific basins. "
  "Statement 3 is wrong: North Atlantic Deep Water, formed in the Nordic and Labrador Seas, is slightly less dense, so it flows southward above the Antarctic Bottom Water. These sinking regions drive the thermohaline circulation that carries heat around the globe; meltwater from Antarctic ice and from Greenland, by freshening the surface, can weaken them, which is one reason scientists watch them as a climate tipping element.",
  "केवल कथन 1 और 2 सही हैं। अंटार्कटिका के चारों ओर, विशेषकर वेडेल और रॉस सागरों के महाद्वीपीय मग्नतटों पर, तीव्र शीतलन और समुद्री बर्फ़ का बनना -- जो अधिकांश लवण को नीचे के जल में छोड़ देता है -- बहुत ठंडा, लवणीय जल बनाते हैं जो महाद्वीपीय ढाल से नीचे उतरकर अंटार्कटिक तलीय जल के रूप में समुद्र तल पर फैलता है, और अटलांटिक, हिंद और प्रशांत द्रोणियों में दूर तक पहुँचता है। "
  "कथन 3 ग़लत है: नॉर्डिक और लैब्राडोर सागरों में बनने वाला उत्तर अटलांटिक गहन जल थोड़ा कम सघन है, इसलिए वह अंटार्कटिक तलीय जल के ऊपर दक्षिण की ओर बहता है। डूबने के ये क्षेत्र तापलवणीय परिसंचरण को चलाते हैं जो पृथ्वी भर में ऊष्मा पहुँचाता है; अंटार्कटिक बर्फ़ और ग्रीनलैंड का पिघला जल, सतह को कम लवणीय बनाकर, इन्हें कमज़ोर कर सकता है, इसी कारण वैज्ञानिक इन्हें जलवायु के एक निर्णायक तत्व के रूप में देखते हैं।",
  "NCERT, Class XI, Fundamentals of Physical Geography, chapters on ocean water; IPCC, Special Report on the Ocean and Cryosphere in a Changing Climate (2019).",
  "l4-s02-geo-antarctic-bottom-water-brine-nadw", craft="inference")

# ---------------------------------------------------------------- Geomorphology & Earth's Interior (MCQ, hard)
M("Geomorphology & Earth's Interior", "hard",
  "A Wadati-Benioff zone is",
  "वदाती-बेनिऑफ़ क्षेत्र क्या है?",
  ["an inclined zone of earthquake foci marking a plate sinking into the mantle",
   "a band of shallow earthquakes running along the crest of a mid-ocean ridge",
   "the boundary at which seismic waves speed up abruptly beneath the crust",
   "the region on the far side of the Earth where no direct seismic waves arrive"],
  ["मेंटल में धँसती प्लेट को दर्शाने वाला भूकंप-केंद्रों का झुका क्षेत्र",
   "मध्य-महासागरीय कटक के शिखर के साथ चलने वाली उथले भूकंपों की एक पट्टी",
   "वह सीमा जिस पर भूपर्पटी के नीचे भूकंपीय तरंगों की गति अचानक बढ़ जाती है",
   "पृथ्वी के दूसरी ओर का वह क्षेत्र जहाँ कोई प्रत्यक्ष भूकंपीय तरंगें नहीं पहुँचतीं"],
  0,
  "Where one plate dives beneath another at a convergent boundary, earthquakes occur within and along the sinking slab. Plotted in cross-section, their foci form a plane that dips from the ocean trench down into the mantle, reaching depths of about 700 kilometres -- the Wadati-Benioff zone, named after the seismologists Kiyoo Wadati and Hugo Benioff, who mapped it in Japan and around the Pacific. It is strong evidence that lithosphere is recycled into the mantle at subduction zones, as beneath Japan, the Andes and the Andaman-Sumatra arc. "
  "The other options describe other features: shallow ridge-crest earthquakes mark divergent boundaries; the sharp rise in seismic velocity beneath the crust is the Mohorovicic discontinuity; and the region without direct waves is the shadow zone, which reveals the liquid outer core.",
  "जहाँ अभिसारी सीमा पर एक प्लेट दूसरी के नीचे गोता लगाती है, वहाँ धँसते हुए खंड के भीतर और उसके साथ भूकंप आते हैं। अनुप्रस्थ काट में अंकित करने पर उनके केंद्र एक तल बनाते हैं जो महासागरीय गर्त से मेंटल में लगभग 700 किलोमीटर की गहराई तक झुकता जाता है -- यही वदाती-बेनिऑफ़ क्षेत्र है, जिसका नाम उन भूकंपविज्ञानियों कियू वदाती और ह्यूगो बेनिऑफ़ पर है जिन्होंने इसे जापान और प्रशांत के चारों ओर मानचित्रित किया। यह इस बात का पुष्ट प्रमाण है कि धँसाव क्षेत्रों में स्थलमंडल मेंटल में पुनर्चक्रित होता है, जैसे जापान, एंडीज़ और अंडमान-सुमात्रा चाप के नीचे। "
  "अन्य विकल्प अन्य लक्षण बताते हैं: कटक-शिखर के उथले भूकंप अपसारी सीमाओं को दर्शाते हैं; भूपर्पटी के नीचे भूकंपीय वेग में तीव्र वृद्धि मोहोरोविचिच असांतत्य है; और प्रत्यक्ष तरंगों से रहित क्षेत्र छाया क्षेत्र है, जो तरल बाह्य क्रोड को उजागर करता है।",
  "NCERT, Class XI, Fundamentals of Physical Geography, chapters on the interior of the Earth and on plate tectonics; Geological Survey of India.",
  "l4-s02-geo-wadati-benioff-zone-subduction", pos=3, craft="precision")

# ---------------------------------------------------------------- Indian Physiography, Climate & Regions (statement, medium)
S("Indian Physiography, Climate & Regions", "medium", "With reference to the physical features of India, consider the following statements:",
  "भारत की भौतिक विशेषताओं के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Kalsubai, in the Sahyadri, is the highest peak in Maharashtra.",
   "Saramati, on the border with Myanmar, is the highest peak in Nagaland.",
   "The Satmala-Ajanta hills lie between the Tapi valley and the Godavari basin.",
   "The Utkal plains form the coastal plain of Andhra Pradesh."],
  ["सह्याद्रि में कलसूबाई महाराष्ट्र की सबसे ऊँची चोटी है।",
   "म्यांमार की सीमा पर सारामती नागालैंड की सबसे ऊँची चोटी है।",
   "सतमाला-अजंता पहाड़ियाँ तापी घाटी और गोदावरी द्रोणी के बीच स्थित हैं।",
   "उत्कल मैदान आंध्र प्रदेश का तटीय मैदान बनाते हैं।"],
  C4, 2,
  "The first three statements are correct. Kalsubai, at about 1,646 metres on the border of Ahmednagar and Nashik districts, is the highest point of Maharashtra and of the northern Sahyadri. Saramati, at about 3,840 metres in Kiphire district, rises in the Naga Hills on the Myanmar border, part of the Purvanchal ranges. The Satmala and Ajanta hills run east from the Sahyadri and form the divide between the Tapi, flowing west to the Arabian Sea, and the Godavari, flowing east. "
  "Statement 4 is wrong: the Utkal plains are the coastal plains of Odisha, built by the deltas of the Mahanadi, Brahmani and Baitarani and including Chilika Lake; the coastal plain of Andhra Pradesh, with the Godavari and Krishna deltas, is known as the Northern Circars.",
  "पहले तीन कथन सही हैं। अहमदनगर और नाशिक ज़िलों की सीमा पर लगभग 1,646 मीटर ऊँची कलसूबाई महाराष्ट्र और उत्तरी सह्याद्रि का सबसे ऊँचा बिंदु है। किफ़िरे ज़िले में लगभग 3,840 मीटर ऊँची सारामती म्यांमार सीमा पर नागा पहाड़ियों में उठती है, जो पूर्वांचल श्रेणियों का भाग हैं। सतमाला और अजंता पहाड़ियाँ सह्याद्रि से पूर्व की ओर चलती हैं और पश्चिम में अरब सागर की ओर बहने वाली तापी तथा पूर्व की ओर बहने वाली गोदावरी के बीच जलविभाजक बनाती हैं। "
  "कथन 4 ग़लत है: उत्कल मैदान ओडिशा के तटीय मैदान हैं, जो महानदी, ब्राह्मणी और बैतरणी के डेल्टाओं से बने हैं और जिनमें चिल्का झील शामिल है; गोदावरी और कृष्णा डेल्टाओं वाला आंध्र प्रदेश का तटीय मैदान उत्तरी सरकार कहलाता है।",
  "NCERT, Class XI, India: Physical Environment, chapter on structure and physiography; Survey of India.",
  "l4-s02-geo-kalsubai-saramati-satmala-utkal", craft="precision")

# ---------------------------------------------------------------- Indian Rivers, Lakes & Wetlands (MCQ, medium)
M("Indian Rivers, Lakes & Wetlands", "medium",
  "Which one of the following is an artificial lake?",
  "निम्नलिखित में से कौन-सी एक कृत्रिम झील है?",
  ["Hussain Sagar, Telangana", "Pulicat, Andhra Pradesh and Tamil Nadu", "Tso Moriri, Ladakh", "Loktak, Manipur"],
  ["हुसैन सागर, तेलंगाना", "पुलिकट, आंध्र प्रदेश और तमिलनाडु", "त्सो मोरीरी, लद्दाख", "लोकटक, मणिपुर"],
  0,
  "Hussain Sagar was built in the 1560s, in the reign of the Qutb Shahi Sultan Ibrahim Quli Qutb Shah, by damming a tributary of the Musi to supply water to the city; it now separates Hyderabad from Secunderabad, and its monolithic statue of the Buddha stands on a rock in the middle. The others are natural: Pulicat is a coastal lagoon behind a barrier island, Tso Moriri a high-altitude lake in a basin of the Changthang plateau, and Loktak a freshwater lake famous for its floating mats of vegetation, the phumdis. "
  "Many 'lakes' in India's cities, such as those of Bengaluru, are in fact old tanks built to store rainwater, which is why their encroachment destroys a designed drainage system.",
  "हुसैन सागर का निर्माण 1560 के दशक में क़ुतुबशाही सुल्तान इब्राहिम क़ुली क़ुतुब शाह के शासनकाल में नगर को जल देने के लिए मूसी की एक सहायक नदी पर बाँध बनाकर किया गया; यह अब हैदराबाद को सिकंदराबाद से अलग करता है, और इसके बीच एक चट्टान पर बुद्ध की एकाश्म प्रतिमा खड़ी है। अन्य प्राकृतिक हैं: पुलिकट एक अवरोधक द्वीप के पीछे की तटीय लैगून है, त्सो मोरीरी चांगथांग पठार की एक द्रोणी में ऊँचाई वाली झील, और लोकटक अपनी तैरती वनस्पति-परतों, फुमदियों, के लिए प्रसिद्ध मीठे पानी की झील। "
  "भारत के नगरों की कई 'झीलें', जैसे बेंगलुरु की, वास्तव में वर्षाजल संग्रहीत करने के लिए बने पुराने तालाब हैं, इसी कारण उन पर अतिक्रमण एक नियोजित जल-निकास प्रणाली को नष्ट कर देता है।",
  "Government of Telangana, Hyderabad Metropolitan Development Authority; Wetlands International South Asia; Ministry of Environment, Forest and Climate Change, Ramsar site information sheets.",
  "l4-s02-geo-hussain-sagar-artificial-lake", pos=0, craft="application")

# ---------------------------------------------------------------- Resources: Minerals, Energy & Agriculture (AR, easy)
A("Resources: Minerals, Energy & Agriculture", "easy",
  "Diamonds are mined from kimberlite pipes, as at Majhgawan in Panna district of Madhya Pradesh.",
  "हीरों का खनन किंबरलाइट नलिकाओं से होता है, जैसे मध्य प्रदेश के पन्ना ज़िले में मझगवाँ में।",
  "Kimberlite is a volcanic rock that rises rapidly from great depths in the mantle, where carbon crystallises as diamond under very high pressure.",
  "किंबरलाइट एक ज्वालामुखीय शैल है जो मेंटल की बड़ी गहराइयों से तेज़ी से ऊपर उठती है, जहाँ कार्बन बहुत उच्च दाब में हीरे के रूप में क्रिस्टलीकृत होता है।",
  0,
  "Both statements are correct, and Statement II explains Statement I. Diamonds form only at depths of roughly 150 kilometres or more, where pressure is high enough for carbon to take the diamond structure. Kimberlite magma rises from there so fast that it carries the diamonds to the surface before they can change to graphite, forming carrot-shaped pipes; erosion of such pipes also leaves diamonds in river gravels, the source of the famous diamonds of Golconda along the Krishna. "
  "The Majhgawan mine in Panna, worked by NMDC, is India's only mechanised diamond mine from a kimberlite pipe, and people also search the gravels of the Panna area under leases from the State.",
  "दोनों कथन सही हैं, और कथन II कथन I की व्याख्या करता है। हीरे केवल लगभग 150 किलोमीटर या उससे अधिक की गहराई पर बनते हैं, जहाँ दाब इतना अधिक होता है कि कार्बन हीरे की संरचना ले सके। किंबरलाइट मैग्मा वहाँ से इतनी तेज़ी से उठता है कि हीरों को ग्रेफ़ाइट में बदलने से पहले ही सतह तक ले आता है, और गाजर के आकार की नलिकाएँ बनाता है; ऐसी नलिकाओं के अपरदन से नदी की बजरी में भी हीरे मिलते हैं, जो कृष्णा के किनारे गोलकुंडा के प्रसिद्ध हीरों का स्रोत था। "
  "पन्ना में एनएमडीसी द्वारा संचालित मझगवाँ खान किंबरलाइट नलिका से हीरा निकालने वाली भारत की एकमात्र यंत्रीकृत हीरा खान है, और लोग राज्य से पट्टे लेकर पन्ना क्षेत्र की बजरी में भी हीरे खोजते हैं।",
  "Indian Bureau of Mines, Indian Minerals Yearbook (Diamond); NMDC Limited; Geological Survey of India.",
  "l4-s02-geo-kimberlite-panna-majhgawan", craft="linkage")

# ---------------------------------------------------------------- World Regions, Water Bodies & Places (statement, medium)
S("World Regions, Water Bodies & Places", "medium", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Great Barrier Reef lies in the Coral Sea, off the coast of Queensland.",
   "The Gulf of Carpentaria indents the northern coast of Australia.",
   "Lake Eyre (Kati Thanda), a salt lake that fills only now and then, is the lowest point in Australia.",
   "The Sea of Okhotsk is bounded by the Kamchatka peninsula and the island of Sakhalin."],
  ["ग्रेट बैरियर रीफ़ क्वींसलैंड के तट से दूर कोरल सागर में स्थित है।",
   "कार्पेंटारिया की खाड़ी ऑस्ट्रेलिया के उत्तरी तट में धँसी हुई है।",
   "कभी-कभी ही भरने वाली लवणीय झील, आयर झील (काती थांडा), ऑस्ट्रेलिया का सबसे निचला बिंदु है।",
   "ओख़ोत्स्क सागर कामचटका प्रायद्वीप और सख़ालिन द्वीप से घिरा है।"],
  C4, 3,
  "All four statements are correct. The Great Barrier Reef, the largest coral reef system in the world and a World Heritage Site, stretches for more than 2,000 kilometres in the Coral Sea off Queensland, and has suffered repeated mass bleaching as the sea warms. The shallow Gulf of Carpentaria is the large bay between Cape York Peninsula and Arnhem Land on Australia's north coast. "
  "Lake Eyre, in the arid interior of South Australia, lies about 15 metres below sea level; it is usually a salt crust and fills only after heavy rains in its huge inland basin. The Sea of Okhotsk, a marginal sea of the north-west Pacific, lies between Kamchatka, the Kuril Islands, Hokkaido and Sakhalin, and freezes over in winter, the southernmost large area of seasonal sea ice in the northern hemisphere.",
  "चारों कथन सही हैं। विश्व की सबसे बड़ी प्रवाल भित्ति प्रणाली और विश्व धरोहर स्थल, ग्रेट बैरियर रीफ़, क्वींसलैंड के पास कोरल सागर में 2,000 किलोमीटर से अधिक फैली है, और समुद्र गर्म होने के साथ इसमें बार-बार व्यापक विरंजन हुआ है। उथली कार्पेंटारिया की खाड़ी ऑस्ट्रेलिया के उत्तरी तट पर केप यॉर्क प्रायद्वीप और आर्नहेम लैंड के बीच की बड़ी खाड़ी है। "
  "दक्षिण ऑस्ट्रेलिया के शुष्क भीतरी भाग में आयर झील समुद्र तल से लगभग 15 मीटर नीचे है; यह प्रायः लवण की परत होती है और अपनी विशाल आंतरिक द्रोणी में भारी वर्षा के बाद ही भरती है। उत्तर-पश्चिम प्रशांत का एक सीमांत सागर, ओख़ोत्स्क सागर, कामचटका, कुरील द्वीपों, होक्काइदो और सख़ालिन के बीच स्थित है, और सर्दियों में जम जाता है -- उत्तरी गोलार्ध में मौसमी समुद्री बर्फ़ का सबसे दक्षिणी बड़ा क्षेत्र।",
  "Geoscience Australia; UNESCO World Heritage Centre, Great Barrier Reef; NCERT, Class XI, Fundamentals of Physical Geography.",
  "l4-s02-geo-coral-sea-carpentaria-eyre-okhotsk", craft="precision")

write("gs_l4_s02_d.sql")
