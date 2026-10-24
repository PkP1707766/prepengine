# -*- coding: utf-8 -*-
"""Level 3 · Test 5 (GS Integrated Test 5) -- part D: Geography (10) (upsc_l3_cell_targets.mjs 5).
Same cell plan as Tests 1-4.
Every fact was searched in the whole UPSC bank (l3_tools/bank_find.py) and is one no row tests: Arunachal Pradesh's
hydropower potential; the language families of Khasi, Kurukh, Bodo and Bhili; El Nino Modoki; maquis, chaparral and
sclerophyllous shrubs; the IMD heat-wave criteria for hilly regions; the Main Central, Main Boundary and Himalayan
Frontal Thrusts, Joshimath and the Indus-Tsangpo suture; the Chagos treaty and Diego Garcia; Essequibo, Scarborough
Shoal and the Darien Gap; the Mahadayi and Vamsadhara rivers; soil-forming factors and horizons. MCQ keys are pinned."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Geography"
d.REQUIRE_CRAFT = True
FPG = "NCERT Class XI, Fundamentals of Physical Geography"
IPE = "NCERT Class XI, India: Physical Environment"
FHG = "NCERT Class XII, Fundamentals of Human Geography"
IPEc = "NCERT Class XII, India: People and Economy"

# ---------------------------------------------------------------- Resources (e-SI)
A("Resources: Minerals, Energy & Agriculture", "easy",
  "Arunachal Pradesh has the largest assessed hydropower potential among the States of India.",
  "भारत के राज्यों में अरुणाचल प्रदेश की आकलित जलविद्युत क्षमता सबसे अधिक है।",
  "Its rivers fall steeply from the Himalaya and carry very large flows during the monsoon.",
  "इसकी नदियाँ हिमालय से तीव्र ढाल पर उतरती हैं और मानसून में बहुत बड़ा प्रवाह लाती हैं।",
  0,
  "Both statements are correct and Statement II explains Statement I. Hydropower depends on the head -- the height through which water falls -- and on the volume of flow. The Siang, Subansiri, Lohit, Dibang and Kameng drop thousands of metres within short distances and are fed by some of the heaviest monsoon rainfall in the country, so the Central Electricity Authority's reassessment gives Arunachal Pradesh the largest share of India's potential, and the Brahmaputra basin as a whole the largest of any basin. "
  "Very little of it has been harnessed, because of remoteness, seismic risk, the cost of transmission and the opposition of downstream communities in Assam to large dams; the proposed Siang Upper Multipurpose Project, meant also as storage against sudden releases from upstream in Tibet, has met protests over displacement.",
  "दोनों कथन सही हैं और कथन II, कथन I की व्याख्या करता है। जलविद्युत शीर्ष -- वह ऊँचाई जिससे पानी गिरता है -- और प्रवाह की मात्रा पर निर्भर करती है। सियांग, सुबनसिरी, लोहित, दिबांग और कामेंग कम दूरी में हज़ारों मीटर उतरती हैं और देश की सबसे भारी मानसूनी वर्षा से पोषित होती हैं, इसलिए केंद्रीय विद्युत प्राधिकरण का पुनर्मूल्यांकन भारत की क्षमता का सबसे बड़ा हिस्सा अरुणाचल प्रदेश को और बेसिनों में सबसे बड़ा हिस्सा पूरे ब्रह्मपुत्र बेसिन को देता है। "
  "इसका बहुत कम भाग उपयोग में आया है, क्योंकि दूरस्थता, भूकंपीय जोखिम, पारेषण की लागत और असम के निचले क्षेत्र के समुदायों का बड़े बाँधों का विरोध बाधा है; प्रस्तावित सियांग अपर बहुउद्देशीय परियोजना, जो तिब्बत में ऊपरी क्षेत्र से अचानक छोड़े गए पानी के विरुद्ध भंडारण के लिए भी है, विस्थापन को लेकर विरोध झेल रही है।",
  IPEc + "; Central Electricity Authority, Reassessment of Hydro Power Potential.",
  "l3-t5-geo-arunachal-hydropower-potential", craft="linkage")

# ---------------------------------------------------------------- Transport, Ports & Human Geography (e-pairs)
P("Transport, Ports & Human Geography", "easy", "Consider the following pairs of languages and the language families to which they belong:",
  "भाषाओं और उनसे संबंधित भाषा-परिवारों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Khasi : Austro-Asiatic", "Kurukh : Dravidian", "Bodo : Tibeto-Burman", "Bhili : Indo-Aryan"],
  ["खासी : ऑस्ट्रो-एशियाटिक", "कुड़ुख : द्रविड़", "बोडो : तिब्बती-बर्मी", "भीली : भारतीय-आर्य"],
  3,
  "All four pairs are correct, and each is a common trap. Khasi, spoken in the hills of Meghalaya, belongs to the Austro-Asiatic family (the Mon-Khmer branch), not to the Tibeto-Burman languages of its neighbours; the Munda languages of the same family -- Santali, Mundari, Ho -- are spoken in Jharkhand, Odisha and West Bengal. Kurukh, the language of the Oraons of the Chota Nagpur plateau, is a northern Dravidian language, like Gondi in central India and Brahui in Balochistan, far from the Dravidian south. "
  "Bodo, of Assam's Brahmaputra valley, is Tibeto-Burman, as are the Naga, Mizo and Garo languages. Bhili, though spoken by a tribal people of western India, is an Indo-Aryan language. A people's language family therefore cannot be inferred from its region or from whether it is a Scheduled Tribe.",
  "चारों युग्म सही हैं, और प्रत्येक एक सामान्य भ्रम है। मेघालय की पहाड़ियों में बोली जाने वाली खासी ऑस्ट्रो-एशियाटिक परिवार (मोन-ख्मेर शाखा) की है, अपने पड़ोसियों की तिब्बती-बर्मी भाषाओं की नहीं; इसी परिवार की मुंडा भाषाएँ -- संथाली, मुंडारी, हो -- झारखंड, ओडिशा और पश्चिम बंगाल में बोली जाती हैं। छोटा नागपुर पठार के उराँवों की भाषा कुड़ुख उत्तरी द्रविड़ भाषा है, जैसे मध्य भारत की गोंडी और बलूचिस्तान की ब्राहुई, जो द्रविड़ दक्षिण से बहुत दूर हैं। "
  "असम की ब्रह्मपुत्र घाटी की बोडो तिब्बती-बर्मी है, जैसे नागा, मिज़ो और गारो भाषाएँ। भीली, यद्यपि पश्चिमी भारत के एक जनजातीय समुदाय द्वारा बोली जाती है, भारतीय-आर्य भाषा है। इसलिए किसी समुदाय का भाषा-परिवार उसके क्षेत्र से या उसके अनुसूचित जनजाति होने से नहीं निकाला जा सकता।",
  IPEc + ", 'Population: Distribution, Density, Growth and Composition'; Census of India, Language tables.",
  "l3-t5-geo-language-families-khasi-kurukh-bodo-bhili", craft="precision")

# ---------------------------------------------------------------- Climatology & Biomes (h-MCQ, m-stmt)
M("Climatology & Biomes", "hard",
  "An 'El Nino Modoki' differs from a conventional El Nino in that:",
  "‘एल नीनो मोडोकी’ पारंपरिक एल नीनो से किस प्रकार भिन्न है?",
  ["it warms the western Indian Ocean rather than the Pacific Ocean",
   "it is set off by a strengthening of the trade winds across the Pacific",
   "its warmest water lies in the central Pacific, with cooler water to the east and west",
   "it brings excess rainfall to India in every single monsoon season in which it happens to occur"],
  ["यह प्रशांत महासागर के बजाय पश्चिमी हिंद महासागर को गर्म करता है",
   "यह प्रशांत महासागर पर व्यापारिक पवनों के प्रबल होने से शुरू होता है",
   "इसमें सबसे गर्म पानी मध्य प्रशांत में होता है, पूर्व और पश्चिम में ठंडा पानी रहता है",
   "यह हर उस मानसून ऋतु में भारत में सामान्य से अधिक वर्षा लाता है जिसमें यह घटित होता है"],
  2,
  "In a conventional, or eastern-Pacific, El Nino the trade winds weaken and the warmest anomaly lies off the coast of Peru and Ecuador. In the pattern that the scientists Karumuri Ashok and Toshio Yamagata described in 2007 as El Nino Modoki -- Japanese for 'similar but different' -- the warm anomaly sits in the central equatorial Pacific, flanked by cooler water on both sides, a tripole that shifts rising air and rainfall to the middle of the ocean. "
  "Because the atmospheric response differs, so do the teleconnections: both types tend to weaken the Indian monsoon, but their effects on rainfall in Australia, East Asia and the Americas, and on Atlantic hurricanes, can differ. Forecasters therefore watch where the warming is centred, not just whether it occurs.",
  "पारंपरिक या पूर्वी-प्रशांत एल नीनो में व्यापारिक पवनें कमज़ोर पड़ती हैं और सबसे गर्म विसंगति पेरू और इक्वाडोर के तट के पास होती है। वैज्ञानिकों करुमुरी अशोक और तोशियो यामागाता ने 2007 में जिस प्रतिरूप को एल नीनो मोडोकी -- जापानी में ‘समान पर भिन्न’ -- बताया, उसमें गर्म विसंगति मध्य विषुवतीय प्रशांत में होती है, दोनों ओर ठंडे पानी से घिरी, एक त्रिध्रुवीय प्रतिरूप जो उठती हवा और वर्षा को महासागर के मध्य में ले जाता है। "
  "चूँकि वायुमंडलीय प्रतिक्रिया भिन्न होती है, दूरगामी प्रभाव (टेलीकनेक्शन) भी भिन्न होते हैं: दोनों प्रकार भारतीय मानसून को कमज़ोर करने की प्रवृत्ति रखते हैं, पर ऑस्ट्रेलिया, पूर्वी एशिया और अमेरिका में वर्षा पर तथा अटलांटिक हरिकेनों पर उनके प्रभाव भिन्न हो सकते हैं। इसलिए पूर्वानुमानकर्ता केवल यह नहीं देखते कि गर्मी हो रही है, बल्कि यह भी कि उसका केंद्र कहाँ है।",
  FPG + "; India Meteorological Department, ENSO bulletins; Ashok et al., Journal of Geophysical Research (2007).",
  "l3-t5-geo-el-nino-modoki", pos=2, craft="inference")

S("Climatology & Biomes", "medium", "With reference to the vegetation of regions with a Mediterranean-type climate, consider the following statements:",
  "भूमध्यसागरीय प्रकार की जलवायु वाले क्षेत्रों की वनस्पति के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["The evergreen shrublands of these regions are called maquis in southern Europe and chaparral in California.",
   "Their plants typically have small, hard, leathery leaves that limit water loss in the dry summer.",
   "Such shrublands are found only in the Northern Hemisphere."],
  ["इन क्षेत्रों की सदाबहार झाड़ियों को दक्षिणी यूरोप में माकी और कैलिफ़ोर्निया में चैपरल कहा जाता है।",
   "इनके पौधों में प्रायः छोटी, कठोर, चमड़े जैसी पत्तियाँ होती हैं जो शुष्क ग्रीष्म में जल-हानि सीमित करती हैं।",
   "ऐसी झाड़ियाँ केवल उत्तरी गोलार्ध में पाई जाती हैं।"],
  C3, 1,
  "Statements 1 and 2 are correct. With hot, dry summers and mild, wet winters, these regions favour sclerophyllous ('hard-leaved') evergreen shrubs and low trees -- such as the holm oak, cork oak, olive, myrtle and wild herbs -- whose thick-cuticled leaves cut transpiration; many are aromatic, and many regenerate quickly after the fires the dry summer brings. "
  "Statement 3 is wrong: the climate occurs on the western sides of continents between about 30 and 40 degrees in both hemispheres, and so do its shrublands -- the fynbos of the Cape in South Africa, the matorral of central Chile and the mallee and kwongan of south-western and southern Australia. The fynbos is so rich in endemic plants that the Cape is recognised as one of the world's floral kingdoms.",
  "कथन 1 और 2 सही हैं। गर्म, शुष्क ग्रीष्म और हल्की, नम सर्दियों वाले ये क्षेत्र दृढ़पर्णी (‘कठोर पत्ती वाली’) सदाबहार झाड़ियों और छोटे वृक्षों -- जैसे होम ओक, कॉर्क ओक, जैतून, मर्टल और जंगली जड़ी-बूटियाँ -- के अनुकूल हैं, जिनकी मोटी उपत्वचा वाली पत्तियाँ वाष्पोत्सर्जन घटाती हैं; अनेक सुगंधित हैं, और अनेक शुष्क ग्रीष्म में लगने वाली आग के बाद शीघ्र पुनर्जीवित होते हैं। "
  "कथन 3 ग़लत है: यह जलवायु दोनों गोलार्धों में लगभग 30 और 40 डिग्री के बीच महाद्वीपों के पश्चिमी भागों में मिलती है, और इसकी झाड़ियाँ भी -- दक्षिण अफ़्रीका के केप का फ़िनबॉस, मध्य चिली का माटोरल और दक्षिण-पश्चिमी तथा दक्षिणी ऑस्ट्रेलिया का मैली और क्वोंगन। फ़िनबॉस स्थानिक पौधों में इतना समृद्ध है कि केप को विश्व के पादप साम्राज्यों में से एक माना जाता है।",
  FPG + ", 'Biodiversity and Conservation' and 'World Climate'; " + FHG + ".", "l3-t5-geo-maquis-chaparral-sclerophyll", craft="precision")

# ---------------------------------------------------------------- Indian Physiography, Climate & Regions (h-SI, m-stmt)
A("Indian Physiography, Climate & Regions", "hard",
  "A hill station in the Himalaya can be declared to be under a heat wave even when its maximum temperature stays well below 40 deg C.",
  "हिमालय के किसी पर्वतीय स्थल को लू (हीट वेव) की स्थिति में घोषित किया जा सकता है, भले ही उसका अधिकतम तापमान 40 डिग्री सेल्सियस से काफ़ी नीचे रहे।",
  "The India Meteorological Department's heat-wave criteria for hilly regions begin at a maximum temperature of 30 deg C, combined with a departure above normal.",
  "पर्वतीय क्षेत्रों के लिए भारत मौसम विज्ञान विभाग के लू के मानदंड 30 डिग्री सेल्सियस के अधिकतम तापमान से शुरू होते हैं, साथ में सामान्य से ऊपर विचलन भी आवश्यक है।",
  0,
  "Both statements are correct and Statement II explains Statement I. Because a heat wave is defined by what is abnormal for a place, the IMD uses different thresholds: a station in the hills qualifies when its maximum is at least 30 deg C and well above its normal, a coastal station when its maximum is at least 37 deg C with such a departure, and the plains have a higher threshold of their own. Shimla or Srinagar can thus be under a heat wave at temperatures that would be ordinary in Delhi. "
  "Heat waves in the hills have become more frequent, drying forests and raising the risk of forest fires and of rapid snowmelt; the IMD and the National Disaster Management Authority use these alerts to trigger heat action plans, which many States and cities now prepare.",
  "दोनों कथन सही हैं और कथन II, कथन I की व्याख्या करता है। चूँकि लू की परिभाषा इस पर निर्भर है कि किसी स्थान के लिए क्या असामान्य है, आईएमडी अलग-अलग सीमाएँ प्रयोग करता है: पर्वतीय केंद्र तब योग्य होता है जब उसका अधिकतम तापमान कम से कम 30 डिग्री हो और सामान्य से काफ़ी ऊपर हो, तटीय केंद्र तब जब अधिकतम कम से कम 37 डिग्री हो और ऐसा ही विचलन हो, और मैदानों की अपनी ऊँची सीमा है। इस प्रकार शिमला या श्रीनगर ऐसे तापमान पर भी लू की स्थिति में हो सकते हैं जो दिल्ली में सामान्य होंगे। "
  "पहाड़ों में लू की घटनाएँ बढ़ी हैं, जिससे वन सूखते हैं और वनाग्नि तथा तीव्र हिम-पिघलन का जोखिम बढ़ता है; आईएमडी और राष्ट्रीय आपदा प्रबंधन प्राधिकरण इन चेतावनियों से ताप कार्य योजनाएँ सक्रिय करते हैं, जिन्हें अब अनेक राज्य और शहर तैयार करते हैं।",
  "India Meteorological Department, criteria for heat wave; National Disaster Management Authority, guidelines on heat waves.",
  "l3-t5-geo-heat-wave-criteria-hills", craft="inference")

S("Indian Physiography, Climate & Regions", "medium", "With reference to the structure of the Himalaya, consider the following statements:",
  "हिमालय की संरचना के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["From north to south, the Main Central Thrust, the Main Boundary Thrust and the Himalayan Frontal Thrust separate the Greater Himalaya, the Lesser Himalaya, the Siwaliks and the plains.",
   "Joshimath, which suffered severe land subsidence in 2023, stands on old landslide debris near the Main Central Thrust zone.",
   "The Indus-Tsangpo Suture Zone, where the Indian and Eurasian plates were joined, lies north of the Greater Himalaya."],
  ["उत्तर से दक्षिण, मेन सेंट्रल थ्रस्ट, मेन बाउंड्री थ्रस्ट और हिमालयन फ़्रंटल थ्रस्ट महान हिमालय, लघु हिमालय, शिवालिक और मैदानों को अलग करते हैं।",
   "2023 में गंभीर भू-धँसाव झेलने वाला जोशीमठ मेन सेंट्रल थ्रस्ट क्षेत्र के निकट पुराने भूस्खलन मलबे पर बसा है।",
   "सिंधु-सांगपो सीवन क्षेत्र, जहाँ भारतीय और यूरेशियाई प्लेटें जुड़ीं, महान हिमालय के उत्तर में स्थित है।"],
  C3, 2,
  "All three are correct. As the Indian plate has pushed under Asia, the crust has been sliced into slabs stacked along thrust faults that become younger towards the south: the Main Central Thrust carries the high-grade rocks of the Greater Himalaya over the Lesser Himalaya, the Main Boundary Thrust brings the Lesser Himalaya over the Siwaliks, and the Himalayan Frontal Thrust marks where the Siwaliks are being pushed onto the Indo-Gangetic plain. The great earthquakes of the region occur on this thrust system. "
  "The Mishra Committee warned in 1976 that Joshimath was built on unstable landslide material; heavy construction, blocked natural drainage and tunnelling nearby were blamed for the subsidence of 2023. Farther north, the Indus-Tsangpo Suture, followed by the upper Indus and the Yarlung Tsangpo, separates the Himalaya from the Trans-Himalayan ranges such as the Ladakh range.",
  "तीनों कथन सही हैं। जैसे-जैसे भारतीय प्लेट एशिया के नीचे धँसी है, भूपर्पटी थ्रस्ट भ्रंशों के साथ परतों में कटकर एक-दूसरे पर चढ़ी है, और ये भ्रंश दक्षिण की ओर नए होते जाते हैं: मेन सेंट्रल थ्रस्ट महान हिमालय की उच्च श्रेणी की चट्टानों को लघु हिमालय के ऊपर ले आता है, मेन बाउंड्री थ्रस्ट लघु हिमालय को शिवालिक के ऊपर लाता है, और हिमालयन फ़्रंटल थ्रस्ट वह रेखा है जहाँ शिवालिक को सिंधु-गंगा के मैदान पर धकेला जा रहा है। क्षेत्र के बड़े भूकंप इसी थ्रस्ट तंत्र पर आते हैं। "
  "मिश्रा समिति ने 1976 में चेतावनी दी थी कि जोशीमठ अस्थिर भूस्खलन सामग्री पर बना है; 2023 के धँसाव के लिए भारी निर्माण, प्राकृतिक जल-निकासी के अवरोध और पास की सुरंग खुदाई को दोषी ठहराया गया। और उत्तर में, सिंधु-सांगपो सीवन, जिसके साथ ऊपरी सिंधु और यारलुंग सांगपो बहती हैं, हिमालय को लद्दाख श्रेणी जैसी ट्रांस-हिमालयी श्रेणियों से अलग करता है।",
  IPE + ", 'Structure and Physiography'; Geological Survey of India; National Disaster Management Authority (Joshimath, 2023).",
  "l3-t5-geo-himalayan-thrusts-joshimath", craft="linkage")

# ---------------------------------------------------------------- World Regions, Water Bodies & Places (m-MCQ, m-stmt)
M("World Regions, Water Bodies & Places", "medium",
  "Under a treaty signed in 2025, the United Kingdom agreed to transfer sovereignty over the Chagos Archipelago to Mauritius, while keeping on a long lease the military base on:",
  "2025 में हस्ताक्षरित एक संधि के अंतर्गत यूनाइटेड किंगडम ने चागोस द्वीपसमूह की संप्रभुता मॉरीशस को सौंपने पर सहमति दी, पर किस द्वीप का सैन्य अड्डा लंबे पट्टे पर अपने पास रखा?",
  ["Ascension Island", "Rodrigues Island", "Socotra Island", "Diego Garcia"],
  ["असेंशन द्वीप", "रॉड्रिग्स द्वीप", "सोकोत्रा द्वीप", "डिएगो गार्सिया"],
  3,
  "Britain detached the Chagos islands from Mauritius in 1965, before Mauritian independence, to form the British Indian Ocean Territory, and moved out the islanders to make way for a joint UK-US base on Diego Garcia, the largest island. The International Court of Justice advised in 2019 that the separation was unlawful and the UN General Assembly called for the territory's return; the treaty signed in May 2025 recognises Mauritian sovereignty and leases Diego Garcia to the UK for 99 years. India, which has close ties with Mauritius, supported its claim. "
  "The other islands lie elsewhere: Ascension is a British territory in the South Atlantic, Rodrigues is part of Mauritius itself, and Socotra belongs to Yemen near the Gulf of Aden. Diego Garcia's position in the middle of the Indian Ocean is what makes it strategically valuable.",
  "ब्रिटेन ने 1965 में, मॉरीशस की स्वतंत्रता से पहले, चागोस द्वीपों को मॉरीशस से अलग कर ब्रिटिश हिंद महासागर क्षेत्र बनाया और सबसे बड़े द्वीप डिएगो गार्सिया पर संयुक्त ब्रिटेन-अमेरिका सैन्य अड्डे के लिए द्वीपवासियों को हटा दिया। अंतरराष्ट्रीय न्यायालय ने 2019 में सलाह दी कि यह अलगाव अवैध था और संयुक्त राष्ट्र महासभा ने क्षेत्र लौटाने को कहा; मई 2025 में हस्ताक्षरित संधि मॉरीशस की संप्रभुता को मान्यता देती है और डिएगो गार्सिया को 99 वर्ष के लिए ब्रिटेन को पट्टे पर देती है। मॉरीशस से घनिष्ठ संबंध रखने वाले भारत ने उसके दावे का समर्थन किया। "
  "अन्य द्वीप दूसरी जगह हैं: असेंशन दक्षिण अटलांटिक में ब्रिटिश क्षेत्र है, रॉड्रिग्स स्वयं मॉरीशस का भाग है, और सोकोत्रा अदन की खाड़ी के पास यमन का है। हिंद महासागर के मध्य में डिएगो गार्सिया की स्थिति ही उसे सामरिक रूप से मूल्यवान बनाती है।",
  "International Court of Justice, Advisory Opinion on the Chagos Archipelago (2019); Ministry of External Affairs, statements on the UK-Mauritius agreement (2025).",
  "l3-t5-geo-chagos-diego-garcia", pos=3, craft="application")

S("World Regions, Water Bodies & Places", "medium", "With reference to places that have been in the news, consider the following statements:",
  "समाचारों में रहे स्थानों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Essequibo region, administered by Guyana, is claimed by Venezuela.",
   "Scarborough Shoal in the South China Sea is the subject of a dispute between China and the Philippines.",
   "The Darien Gap is a roadless stretch of rainforest on the border of Colombia and Panama that interrupts the Pan-American Highway."],
  ["गयाना द्वारा प्रशासित एसेक्विबो क्षेत्र पर वेनेज़ुएला दावा करता है।",
   "दक्षिण चीन सागर में स्कारबोरो शोल चीन और फ़िलीपींस के बीच विवाद का विषय है।",
   "डेरियन गैप कोलंबिया और पनामा की सीमा पर वर्षावन का सड़क-विहीन हिस्सा है जो पैन-अमेरिकन राजमार्ग को तोड़ता है।"],
  C3, 2,
  "All three are correct. Essequibo, west of the Essequibo river, makes up about two-thirds of Guyana; Venezuela rejects the arbitral award of 1899 that gave it to British Guiana, held a referendum on the claim in 2023, and the case is before the International Court of Justice -- a dispute sharpened by the large offshore oil finds of recent years. "
  "China has controlled Scarborough Shoal, inside the Philippines' exclusive economic zone, since a stand-off in 2012; the arbitral tribunal of 2016 under UNCLOS held that the traditional fishing rights of both countries' fishermen there must be respected, a ruling China rejects. The Darien Gap, about 100 km of swamp and forest, is the only break in the highway from Alaska to Argentina and has become a dangerous route for migrants heading north to the United States.",
  "तीनों कथन सही हैं। एसेक्विबो नदी के पश्चिम का एसेक्विबो क्षेत्र गयाना का लगभग दो-तिहाई है; वेनेज़ुएला 1899 के उस पंचाट को अस्वीकार करता है जिसने इसे ब्रिटिश गयाना को दिया था, उसने 2023 में इस दावे पर जनमत संग्रह कराया, और मामला अंतरराष्ट्रीय न्यायालय के सामने है -- यह विवाद हाल के वर्षों की बड़ी अपतटीय तेल खोजों से और तीखा हुआ है। "
  "फ़िलीपींस के अनन्य आर्थिक क्षेत्र के भीतर स्थित स्कारबोरो शोल पर 2012 के एक गतिरोध के बाद से चीन का नियंत्रण है; यूएनक्लॉस के अंतर्गत 2016 के मध्यस्थ अधिकरण ने माना कि वहाँ दोनों देशों के मछुआरों के पारंपरिक मत्स्यन अधिकारों का सम्मान होना चाहिए, जिसे चीन अस्वीकार करता है। लगभग 100 किलोमीटर दलदल और वन वाला डेरियन गैप अलास्का से अर्जेंटीना तक के राजमार्ग का एकमात्र विराम है और उत्तर में संयुक्त राज्य अमेरिका जाने वाले प्रवासियों का ख़तरनाक मार्ग बन गया है।",
  "International Court of Justice, Guyana v. Venezuela; Permanent Court of Arbitration, South China Sea Arbitration (2016); " + FHG + ".",
  "l3-t5-geo-essequibo-scarborough-darien", craft="precision")

# ---------------------------------------------------------------- Indian Rivers, Lakes & Wetlands (m-stmt)
S("Indian Rivers, Lakes & Wetlands", "medium", "With reference to rivers that have been the subject of inter-State water disputes, consider the following statements:",
  "उन नदियों के संदर्भ में जो अंतरराज्यीय जल विवादों का विषय रही हैं, निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Mahadayi (Mhadei) rises in Karnataka and flows through Goa, where it is known as the Mandovi.",
   "Karnataka's plan to divert Mahadayi water through the Kalasa and Banduri canals would take it into the Malaprabha, part of the Krishna basin.",
   "The Vamsadhara water dispute is between Andhra Pradesh and Odisha.",
   "The Vamsadhara flows into the Bay of Bengal near Kalingapatnam."],
  ["महादयी (म्हादेई) कर्नाटक में निकलती है और गोवा से होकर बहती है, जहाँ इसे मांडवी कहा जाता है।",
   "कलसा और बंडूरी नहरों से महादयी का पानी मोड़ने की कर्नाटक की योजना इसे कृष्णा बेसिन की मलप्रभा में ले जाएगी।",
   "वंशधारा जल विवाद आंध्र प्रदेश और ओडिशा के बीच है।",
   "वंशधारा कलिंगपट्टनम के पास बंगाल की खाड़ी में गिरती है।"],
  C4, 3,
  "All four are correct. The Mahadayi rises in the Bhimgad forests of Belagavi district and reaches the Arabian Sea at Panaji as the Mandovi; Karnataka wants to divert some of its water east, across the Western Ghats, to meet drinking-water needs around Hubballi-Dharwad, which Goa opposes because of the river's ecology and its dependence on the flow. The Mahadayi Water Disputes Tribunal gave its award in 2018. "
  "The Vamsadhara rises in Odisha and flows through Srikakulam district of Andhra Pradesh to the sea at Kalingapatnam; the dispute, over Andhra Pradesh's Neradi barrage and a flood-flow canal, was decided by the Vamsadhara Water Disputes Tribunal in 2017. Both were set up under the Inter-State River Water Disputes Act, 1956, which Article 262 allows Parliament to make.",
  "चारों कथन सही हैं। महादयी बेलगावी ज़िले के भीमगढ़ वनों में निकलती है और मांडवी के रूप में पणजी में अरब सागर तक पहुँचती है; कर्नाटक हुब्बल्ली-धारवाड़ के आसपास पेयजल की ज़रूरतों के लिए इसका कुछ पानी पश्चिमी घाट के पार पूर्व की ओर मोड़ना चाहता है, जिसका गोवा नदी की पारिस्थितिकी और प्रवाह पर अपनी निर्भरता के कारण विरोध करता है। महादयी जल विवाद अधिकरण ने 2018 में अपना निर्णय दिया। "
  "वंशधारा ओडिशा में निकलती है और आंध्र प्रदेश के श्रीकाकुलम ज़िले से होकर कलिंगपट्टनम में समुद्र तक पहुँचती है; आंध्र प्रदेश के नेराडी बैराज और एक बाढ़-प्रवाह नहर से जुड़े इस विवाद का निर्णय वंशधारा जल विवाद अधिकरण ने 2017 में किया। दोनों अधिकरण अंतरराज्यीय नदी जल विवाद अधिनियम, 1956 के अंतर्गत बने, जिसे बनाने की अनुमति अनुच्छेद 262 संसद को देता है।",
  "Ministry of Jal Shakti, Inter-State River Water Disputes Tribunals (Mahadayi, Vamsadhara); " + IPE + ", 'Drainage System'.",
  "l3-t5-geo-mahadayi-vamsadhara", craft="precision")

# ---------------------------------------------------------------- Geomorphology & Earth's Interior (m-stmt)
S("Geomorphology & Earth's Interior", "medium", "With reference to the formation of soils, consider the following statements:",
  "मृदा निर्माण के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Climate and biological activity are counted among the active factors of soil formation, while parent material and topography are passive ones.",
   "In a soil profile, the B horizon is a zone in which material washed down from the layer above accumulates.",
   "Calcification, the build-up of calcium carbonate in the soil, is the dominant soil-forming process in hot, humid regions."],
  ["जलवायु और जैविक गतिविधि मृदा निर्माण के सक्रिय कारकों में गिने जाते हैं, जबकि मूल पदार्थ और स्थलाकृति निष्क्रिय कारक हैं।",
   "मृदा परिच्छेदिका में ‘बी’ संस्तर वह क्षेत्र है जिसमें ऊपरी परत से बहकर आया पदार्थ जमा होता है।",
   "कैल्सीकरण, अर्थात मृदा में कैल्शियम कार्बोनेट का जमाव, गर्म और आर्द्र क्षेत्रों में प्रमुख मृदा-निर्माण प्रक्रिया है।"],
  C3, 1,
  "Statements 1 and 2 are correct. Soil forms from weathered rock under five factors: parent material and topography, which control the process passively; climate, through moisture, temperature and the balance of rainfall and evaporation, and living organisms, which act on it actively; and time. Water moving down through the soil carries clay, iron, aluminium and humus out of the upper horizons (eluviation) and deposits them in the B horizon (illuviation), above the weathered parent material of the C horizon. "
  "Statement 3 is wrong: calcification occurs in dry and semi-arid regions, where evaporation exceeds rainfall and draws calcium carbonate upward or leaves it unleached, as in steppe and desert soils. In hot, humid regions heavy leaching removes the bases and silica, and laterisation is dominant; in cool, humid forests, podzolisation leaves an ash-grey leached layer.",
  "कथन 1 और 2 सही हैं। मृदा अपक्षयित चट्टान से पाँच कारकों के अधीन बनती है: मूल पदार्थ और स्थलाकृति, जो प्रक्रिया को निष्क्रिय रूप से नियंत्रित करते हैं; जलवायु, नमी, तापमान और वर्षा-वाष्पीकरण के संतुलन के माध्यम से, और जीव, जो इस पर सक्रिय रूप से कार्य करते हैं; और समय। मृदा में नीचे जाता पानी ऊपरी संस्तरों से मृत्तिका, लोहा, एल्युमिनियम और ह्यूमस बहा ले जाता है (अवक्षालन) और उन्हें ‘बी’ संस्तर में जमा करता है (संचयन), जो ‘सी’ संस्तर के अपक्षयित मूल पदार्थ के ऊपर होता है। "
  "कथन 3 ग़लत है: कैल्सीकरण शुष्क और अर्ध-शुष्क क्षेत्रों में होता है, जहाँ वाष्पीकरण वर्षा से अधिक होता है और कैल्शियम कार्बोनेट को ऊपर खींचता है या उसे बहने नहीं देता, जैसे स्टेपी और मरुस्थलीय मृदाओं में। गर्म, आर्द्र क्षेत्रों में भारी निक्षालन क्षारकों और सिलिका को हटा देता है और लैटेराइटीकरण प्रमुख होता है; ठंडे, आर्द्र वनों में पॉडज़ॉलीकरण राख-धूसर निक्षालित परत छोड़ता है।",
  FPG + ", 'Geomorphic Processes' (soil formation).", "l3-t5-geo-soil-factors-horizons-calcification", craft="precision")

write("gs_l3_t5_d.sql")
