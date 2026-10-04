# -*- coding: utf-8 -*-
"""Level 2 · Test 10 (Environment 2: Climate Change and Pollution) -- depth audit of 2026-10-04
(docs/upsc-question-design-standard.md §6).

All 106 rows were read and classified. Before: analytic 31, precision 38, recall 37 (5 rows are Test 21's,
already tagged). 13 recall rows are rewritten in place with the same concept id, type and difficulty:
  - MCQs that asked a name or a date now put a case: dryland fields lost to the desert (loss and damage), a
    panchayat's pond and trees (Green Credit Programme), a city whose PM2.5 sub-index alone is high (how the
    AQI is set), the remaining carbon budget at today's emissions, Earth Overshoot Day on 1 August, which
    project adds blue carbon, why N2 and O2 trap no heat, and why E. coli is the faecal indicator;
  - statement rows now reason: why one cold winter proves nothing and why land warms faster than the sea,
    how the waste hierarchy ranks a city's options, what fly ash in cement does to emissions, why boiling
    does not remove arsenic, and how microplastics carry toxins.
After: analytic 44, precision 38, recall 24. The other 88 rows keep their content and get their craft tag.
Keys were chosen up front: the 3-statement rewrites are Only one x2, Only two x2 and All three x1.
Leaks avoided while drafting:
  - the Paris 1.5-degree baseline in the climate-basics stem (supports the Paris-basics row);
  - 'the Arctic warms faster' as a false statement (the Arctic-amplification stem states it);
  - water vapour rising with temperature (the extreme-rainfall row's Statement-II);
  - a CCTS compliance-mechanism distractor (states the CCTS row's statement 4);
  - global warming of 1.1 degrees by 2011-2020, or a 1.5-degree budget still open in 2020 (either answers the
    AR6 row's statement 1);
  - an island losing land to the sea in the loss-and-damage case (supports the island-States row)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write_updates, CODE
from polity_common import C3, C4, T2

d.SUBJECT = "Environment & Ecology"
d.REQUIRE_CRAFT = True
AGR = "Climate Agreements & Carbon Markets"
SCI = "Climate Science & Mitigation"
POL = "Pollution, Waste & Resources"
AR6 = "IPCC Sixth Assessment Report, Working Group I (2021)."

# ================================================================ MCQs (8)
M(AGR, "hard", "Despite switching to drought-tolerant crops and digging new wells, a farming community in a dryland country permanently loses its fields to the advancing desert as rainfall declines. Under the UNFCCC, harm of this kind is addressed mainly through the arrangements for:",
  "सूखा-सहिष्णु फ़सलें अपनाने और नए कुएँ खोदने के बावजूद, एक शुष्क देश का कृषक समुदाय घटती वर्षा के साथ बढ़ते मरुस्थल के कारण अपने खेत स्थायी रूप से खो देता है। UNFCCC के अंतर्गत इस प्रकार की हानि को मुख्यतः किसके लिए बनी व्यवस्थाओं के माध्यम से संबोधित किया जाता है?",
  ["loss and damage, such as the Warsaw International Mechanism",
   "adaptation, such as the Adaptation Fund and national adaptation plans",
   "mitigation, such as nationally determined contributions",
   "forests, such as REDD+ payments for avoided deforestation"],
  ["हानि और क्षति, जैसे वारसॉ अंतरराष्ट्रीय तंत्र",
   "अनुकूलन, जैसे अनुकूलन कोष और राष्ट्रीय अनुकूलन योजनाएँ",
   "शमन, जैसे राष्ट्रीय स्तर पर निर्धारित योगदान",
   "वन, जैसे वनोन्मूलन टालने के लिए REDD+ भुगतान"],
  0,
  "Adaptation means preparing for climate impacts -- the drought-tolerant crops and new wells in the stem. Loss and damage is the harm that remains when adaptation is not enough or not possible: slow-onset losses such as land given up to the desert or the sea, and sudden ones such as lives and livelihoods destroyed by a disaster. "
  "The UNFCCC's first formal arrangement for it is the Warsaw International Mechanism, set up at COP19 in 2013; the Santiago Network later added technical help. Mitigation pledges and REDD+ deal with cutting emissions, not with harm that has already happened.",
  "अनुकूलन का अर्थ है जलवायु प्रभावों के लिए तैयारी, जैसे प्रश्न में सूखा-सहिष्णु फ़सलें और नए कुएँ। हानि और क्षति वह नुकसान है जो अनुकूलन के अपर्याप्त या असंभव होने पर बचा रहता है: धीरे होने वाली हानियाँ, जैसे मरुस्थल या समुद्र के हाथों गई भूमि, और अचानक होने वाली, जैसे किसी आपदा में नष्ट जीवन और आजीविकाएँ। "
  "इसके लिए UNFCCC की पहली औपचारिक व्यवस्था वारसॉ अंतरराष्ट्रीय तंत्र है, जो 2013 में COP19 में बनाया गया; बाद में सैंटियागो नेटवर्क ने तकनीकी सहायता जोड़ी। शमन के संकल्प और REDD+ उत्सर्जन घटाने से जुड़े हैं, उस हानि से नहीं जो हो चुकी है।",
  "UNFCCC -- Warsaw International Mechanism for Loss and Damage.", "env-warsaw-international-mechanism", craft="application")

M(AGR, "medium", "A gram panchayat restores a silted village pond and plants native trees on degraded common land. It wants this voluntary work to earn credits that can be traded. Which one of the following is designed for this?",
  "एक ग्राम पंचायत गाद से भरे गाँव के तालाब का जीर्णोद्धार करती है और क्षरित सामुदायिक भूमि पर देशी वृक्ष लगाती है। वह चाहती है कि इस स्वैच्छिक कार्य से ऐसे क्रेडिट मिलें जिनका व्यापार हो सके। निम्नलिखित में से कौन-सा इसके लिए बनाया गया है?",
  ["the Green Credit Programme",
   "the Perform, Achieve and Trade scheme",
   "the Compensatory Afforestation Fund",
   "the National Clean Air Programme"],
  ["हरित क्रेडिट कार्यक्रम",
   "परफ़ॉर्म, अचीव एंड ट्रेड (PAT) योजना",
   "प्रतिपूरक वनरोपण कोष",
   "राष्ट्रीय स्वच्छ वायु कार्यक्रम"],
  0,
  "The Green Credit Programme, notified in October 2023 under the Environment (Protection) Act, 1986, rewards voluntary environmental actions by individuals, communities, local bodies and companies -- tree plantation, water conservation and harvesting, sustainable agriculture, waste management and others -- with green credits that can be traded on a domestic platform; the Indian Council of Forestry Research and Education administers it. "
  "The PAT scheme issues tradeable energy-saving certificates, but only to designated energy-intensive industries; the Compensatory Afforestation Fund holds money paid when forest land is diverted to other uses; and the National Clean Air Programme sets cities targets for cutting particulate pollution.",
  "हरित क्रेडिट कार्यक्रम, जो अक्टूबर 2023 में पर्यावरण (संरक्षण) अधिनियम, 1986 के तहत अधिसूचित हुआ, व्यक्तियों, समुदायों, स्थानीय निकायों और कंपनियों के स्वैच्छिक पर्यावरणीय कार्यों, जैसे वृक्षारोपण, जल संरक्षण और संचयन, टिकाऊ कृषि, अपशिष्ट प्रबंधन आदि, को हरित क्रेडिट से पुरस्कृत करता है, जिनका एक घरेलू मंच पर व्यापार हो सकता है; भारतीय वानिकी अनुसंधान एवं शिक्षा परिषद इसका प्रशासक है। "
  "PAT योजना व्यापार-योग्य ऊर्जा-बचत प्रमाणपत्र देती है, पर केवल नामित ऊर्जा-गहन उद्योगों को; प्रतिपूरक वनरोपण कोष में वह धन रहता है जो वन भूमि को अन्य उपयोग में लगाने पर दिया जाता है; और राष्ट्रीय स्वच्छ वायु कार्यक्रम शहरों के लिए कण-प्रदूषण घटाने के लक्ष्य तय करता है।",
  "Ministry of Environment, Forest and Climate Change -- Green Credit Rules, 2023.", "env-green-credit-programme", craft="application")

M(SCI, "easy", "Nitrogen and oxygen together make up about 99 per cent of dry air, yet they add almost nothing to the greenhouse effect. This is mainly because:",
  "नाइट्रोजन और ऑक्सीजन मिलकर शुष्क वायु का लगभग 99 प्रतिशत बनाती हैं, फिर भी वे ग्रीनहाउस प्रभाव में लगभग कुछ नहीं जोड़तीं। इसका मुख्य कारण यह है कि:",
  ["each molecule has two identical atoms, so it barely absorbs infrared radiation",
   "they are found mostly in the upper atmosphere, far above the level where heat is trapped",
   "they are chemically inert and so cannot interact with any kind of radiation",
   "they are washed out of the air by rain too quickly to build up to high levels"],
  ["प्रत्येक अणु में दो समान परमाणु होते हैं, इसलिए वह अवरक्त विकिरण को लगभग अवशोषित नहीं करता",
   "वे अधिकतर ऊपरी वायुमंडल में पाई जाती हैं, उस स्तर से बहुत ऊपर जहाँ ऊष्मा रुकती है",
   "वे रासायनिक रूप से निष्क्रिय हैं, इसलिए किसी भी प्रकार के विकिरण से क्रिया नहीं कर सकतीं",
   "वर्षा उन्हें वायु से इतनी जल्दी धो देती है कि वे ऊँचे स्तर तक जमा नहीं हो पातीं"],
  0,
  "A gas traps heat when its molecules absorb the infrared radiation given off by the warm surface, and that needs a molecule whose vibrations shift its electric charge. Molecules made of two identical atoms, such as N2 and O2, have no such vibration, so infrared passes through them. "
  "Carbon dioxide, methane, nitrous oxide (N2O -- not to be confused with nitrogen, N2) and ozone all absorb it. Nitrogen and oxygen are well mixed through the lower atmosphere, they are not washed out by rain, and oxygen does absorb ultraviolet high in the atmosphere, so the other options are wrong.",
  "कोई गैस तब ऊष्मा रोकती है जब उसके अणु गर्म सतह से निकलने वाले अवरक्त विकिरण को अवशोषित करें, और इसके लिए ऐसा अणु चाहिए जिसके कंपन उसके विद्युत आवेश को खिसकाएँ। N2 और O2 जैसे दो समान परमाणुओं से बने अणुओं में ऐसा कंपन नहीं होता, इसलिए अवरक्त विकिरण उनसे होकर निकल जाता है। "
  "कार्बन डाइऑक्साइड, मीथेन, नाइट्रस ऑक्साइड (N2O, जिसे नाइट्रोजन N2 से न मिलाएँ) और ओज़ोन सभी इसे अवशोषित करती हैं। नाइट्रोजन और ऑक्सीजन निचले वायुमंडल में भली-भाँति मिली रहती हैं, वर्षा से नहीं धुलतीं, और ऑक्सीजन ऊँचे वायुमंडल में पराबैंगनी विकिरण को अवशोषित करती भी है, इसलिए अन्य विकल्प गलत हैं।",
  AR6, "env-not-a-greenhouse-gas", craft="linkage")

M(SCI, "medium", "Which one of the following projects would add to India's 'blue carbon' store?",
  "निम्नलिखित में से कौन-सी परियोजना भारत के 'ब्लू कार्बन' भंडार में वृद्धि करेगी?",
  ["Replanting mangroves on degraded tidal mudflats in the Sundarbans",
   "Planting deodar and oak on the bare hill slopes of Himachal Pradesh",
   "Encouraging plankton blooms far out in the open waters of the Indian Ocean",
   "Pumping captured carbon dioxide into depleted oil wells under the sea"],
  ["सुंदरबन के क्षरित ज्वारीय कीचड़-मैदानों पर फिर से मैंग्रोव लगाना",
   "हिमाचल प्रदेश की नंगी पहाड़ी ढलानों पर देवदार और बाँज लगाना",
   "हिंद महासागर के खुले जल में दूर तक प्लवक की बहुतायत को बढ़ावा देना",
   "पकड़ी गई कार्बन डाइऑक्साइड को समुद्र के नीचे खाली हुए तेल-कुओं में पंप करना"],
  0,
  "Blue carbon is the carbon captured by coastal vegetated ecosystems -- mangroves, seagrass meadows and tidal salt marshes -- and stored mostly in their waterlogged soils, where it can stay for centuries; per hectare they can hold several times as much carbon as many land forests. "
  "Hill forests store 'green' carbon; open-ocean plankton take up carbon, but little of it is stored reliably, so it is not counted as blue carbon; and injecting carbon dioxide into old oil wells is geological storage, wherever the wells lie.",
  "ब्लू कार्बन वह कार्बन है जिसे तटीय वनस्पति पारितंत्र, जैसे मैंग्रोव, समुद्री घास के मैदान और ज्वारीय लवण-दलदल, ग्रहण करते हैं और मुख्यतः अपनी जलभरी मिट्टी में संचित करते हैं, जहाँ वह सदियों तक रह सकता है; प्रति हेक्टेयर वे कई स्थलीय वनों से कई गुना अधिक कार्बन रख सकते हैं। "
  "पहाड़ी वन 'हरा' कार्बन संचित करते हैं; खुले महासागर के प्लवक कार्बन लेते हैं, पर उसका बहुत कम भाग भरोसे से संचित होता है, इसलिए उसे ब्लू कार्बन नहीं गिना जाता; और कार्बन डाइऑक्साइड को पुराने तेल-कुओं में डालना भूगर्भीय भंडारण है, कुएँ कहीं भी हों।",
  "IUCN -- Blue carbon.", "env-blue-carbon", craft="application")

M(SCI, "medium", "Suppose that, from the start of 2020, the world can emit a further 500 billion tonnes of carbon dioxide before a chosen limit on warming is crossed -- its remaining carbon budget. If the world keeps emitting about 40 billion tonnes of carbon dioxide a year, this budget will be used up around:",
  "मान लीजिए कि 2020 के आरंभ से संसार तापवृद्धि की किसी चुनी हुई सीमा के पार होने से पहले 500 अरब टन कार्बन डाइऑक्साइड और उत्सर्जित कर सकता है, जो उसका शेष कार्बन बजट है। यदि संसार प्रति वर्ष लगभग 40 अरब टन कार्बन डाइऑक्साइड उत्सर्जित करता रहे, तो यह बजट लगभग कब समाप्त हो जाएगा?",
  ["the early 2030s", "the late 2040s", "the 2070s", "the end of the century"],
  ["2030 के दशक के आरंभ में", "2040 के दशक के अंत में", "2070 के दशक में", "सदी के अंत में"],
  0,
  "500 divided by 40 is about 12.5 years, so from the start of 2020 the budget runs out in the early 2030s; 500 billion tonnes is roughly what the IPCC's Sixth Assessment Report gave for a 50 per cent chance of staying within 1.5 degrees Celsius. The idea of a budget rests on the near-linear relation between cumulative carbon dioxide emissions and warming: what decides the temperature is the total emitted, not the rate in any one year, so every year at today's level uses up a fixed share of what is left.",
  "500 को 40 से भाग देने पर लगभग 12.5 वर्ष आते हैं, इसलिए 2020 के आरंभ से गिनें तो बजट 2030 के दशक के आरंभ में समाप्त हो जाता है; 500 अरब टन लगभग वही है जो IPCC की छठी आकलन रिपोर्ट ने 1.5 डिग्री सेल्सियस के भीतर रहने की 50 प्रतिशत संभावना के लिए दिया। बजट का विचार संचयी कार्बन डाइऑक्साइड उत्सर्जन और तापवृद्धि के लगभग रैखिक संबंध पर टिका है: तापमान कुल उत्सर्जन से तय होता है, किसी एक वर्ष की दर से नहीं, इसलिए आज के स्तर पर हर वर्ष बचे हुए बजट का एक निश्चित भाग खर्च कर देता है।",
  AR6, "env-carbon-budget", craft="application")

M(POL, "easy", "On a winter day in a city, the sub-index for PM2.5 is 420, while the sub-indices of all the other pollutants measured are below 200. Under India's National Air Quality Index, the city's air quality that day is:",
  "किसी शहर में सर्दियों के एक दिन PM2.5 का उप-सूचकांक 420 है, जबकि मापे गए अन्य सभी प्रदूषकों के उप-सूचकांक 200 से कम हैं। भारत के राष्ट्रीय वायु गुणवत्ता सूचकांक के अनुसार उस दिन शहर की वायु गुणवत्ता है:",
  ["Severe, since the index takes the highest sub-index",
   "Moderately polluted, since the index averages the sub-indices",
   "Poor, since at least three pollutants must be high for a worse rating",
   "Not rated, since every pollutant must be measured above 200"],
  ["गंभीर, क्योंकि सूचकांक सबसे ऊँचा उप-सूचकांक लेता है",
   "मध्यम प्रदूषित, क्योंकि सूचकांक उप-सूचकांकों का औसत लेता है",
   "ख़राब, क्योंकि इससे बुरी श्रेणी के लिए कम से कम तीन प्रदूषक ऊँचे होने चाहिए",
   "श्रेणी नहीं दी जाएगी, क्योंकि हर प्रदूषक 200 से ऊपर मापा जाना चाहिए"],
  0,
  "The AQI is set by the worst pollutant: each pollutant's concentration is turned into a sub-index, and the highest sub-index becomes the AQI, so that one dangerous pollutant cannot be hidden in an average. A value of 401-500 falls in 'Severe', the worst of the six categories (Good, Satisfactory, Moderately Polluted, Poor, Very Poor and Severe). "
  "The index needs data for at least three pollutants, one of them PM2.5 or PM10, but only one of them has to be high.",
  "AQI सबसे बुरे प्रदूषक से तय होता है: हर प्रदूषक की सांद्रता को एक उप-सूचकांक में बदला जाता है, और सबसे ऊँचा उप-सूचकांक AQI बनता है, ताकि एक ख़तरनाक प्रदूषक औसत में छिप न सके। 401-500 का मान 'गंभीर' में आता है, जो छह श्रेणियों (अच्छा, संतोषजनक, मध्यम प्रदूषित, ख़राब, बहुत ख़राब और गंभीर) में सबसे बुरी है। "
  "सूचकांक के लिए कम से कम तीन प्रदूषकों के आँकड़े चाहिए, जिनमें एक PM2.5 या PM10 हो, पर ऊँचा केवल एक का होना पर्याप्त है।",
  "Central Pollution Control Board -- National Air Quality Index (2014).", "env-aqi-categories", craft="application")

M(POL, "hard", "Earth Overshoot Day marks the date by which humanity's demand on nature in a year exceeds what the Earth can regenerate in that year. If it falls on 1 August, humanity is using nature roughly:",
  "'अर्थ ओवरशूट डे' वह तिथि है जब किसी वर्ष में प्रकृति पर मानवता की माँग उस वर्ष में पृथ्वी द्वारा पुनः उत्पन्न की जा सकने वाली मात्रा से अधिक हो जाती है। यदि यह 1 अगस्त को पड़े, तो मानवता प्रकृति का उपयोग लगभग कर रही है:",
  ["1.7 times as fast as the Earth regenerates it",
   "1.2 times as fast as the Earth regenerates it",
   "2.5 times as fast as the Earth regenerates it",
   "only about half of what the Earth regenerates"],
  ["पृथ्वी के पुनर्जनन से 1.7 गुना तेज़ी से",
   "पृथ्वी के पुनर्जनन से 1.2 गुना तेज़ी से",
   "पृथ्वी के पुनर्जनन से 2.5 गुना तेज़ी से",
   "पृथ्वी के पुनर्जनन के केवल लगभग आधे के बराबर"],
  0,
  "1 August is the 213th day of the year, so a whole year's regeneration is used up in 213 days: 365 divided by 213 is about 1.7. That is the figure the Global Footprint Network, which calculates the day by comparing humanity's Ecological Footprint with the Earth's biocapacity, has reported for recent years, when the day has fallen in late July or early August. "
  "The later the day falls, the closer humanity is to living within what the Earth regenerates.",
  "1 अगस्त वर्ष का 213वाँ दिन है, इसलिए पूरे वर्ष का पुनर्जनन 213 दिनों में खप जाता है: 365 को 213 से भाग देने पर लगभग 1.7 आता है। ग्लोबल फ़ुटप्रिंट नेटवर्क, जो मानवता के पारिस्थितिक पदचिह्न की पृथ्वी की जैव-क्षमता से तुलना करके यह दिन निकालता है, हाल के वर्षों के लिए यही आँकड़ा बताता रहा है, जब यह दिन जुलाई के अंत या अगस्त के आरंभ में पड़ा। "
  "दिन जितनी देर से पड़े, मानवता उतनी ही पृथ्वी के पुनर्जनन की सीमा में जीने के निकट है।",
  "Global Footprint Network -- Earth Overshoot Day.", "env-earth-overshoot-day", craft="application")

M(POL, "medium", "Water-testing laboratories check drinking water for Escherichia coli as the indicator of faecal contamination. The main reason for choosing it is that it:",
  "जल-परीक्षण प्रयोगशालाएँ मल-संदूषण के सूचक के रूप में पेयजल में एशेरिकिया कोलाई की जाँच करती हैं। इसे चुनने का मुख्य कारण यह है कि यह:",
  ["lives in the gut of warm-blooded animals, so it signals faecal pollution",
   "is itself the deadliest of all the disease-causing organisms carried by water",
   "multiplies quickly in clean, treated water and so is easy to detect there",
   "survives chlorination, so it shows whether the water was disinfected at all"],
  ["उष्ण-रक्त वाले प्राणियों की आँत में रहता है, इसलिए हाल के मल-प्रदूषण का संकेत देता है",
   "स्वयं जल से फैलने वाले सभी रोगजनक जीवों में सबसे घातक है",
   "स्वच्छ, उपचारित जल में तेज़ी से बढ़ता है और इसलिए वहाँ आसानी से पकड़ में आता है",
   "क्लोरीनीकरण के बाद भी बचा रहता है, इसलिए दिखाता है कि जल का विसंक्रमण हुआ या नहीं"],
  0,
  "E. coli is abundant in the intestines and faeces of people and warm-blooded animals and does not usually multiply in clean water, so finding it shows that faecal matter has got in recently -- and with it, possibly the pathogens of cholera, typhoid or hepatitis, which are harder to test for one by one. Most strains are harmless; it is chosen as a marker, not because it is the most dangerous. "
  "It is killed by proper chlorination, so its presence after treatment shows that disinfection has failed. India's drinking-water standard, IS 10500, requires it to be absent in any 100 ml sample.",
  "ई. कोलाई मनुष्यों और उष्ण-रक्त वाले प्राणियों की आँतों और मल में प्रचुर होता है और प्रायः स्वच्छ जल में नहीं बढ़ता, इसलिए इसका मिलना दिखाता है कि हाल ही में मल पहुँचा है, और उसके साथ संभवतः हैज़ा, टाइफ़ाइड या हेपेटाइटिस के रोगजनक भी, जिनकी एक-एक करके जाँच कठिन है। इसके अधिकांश प्रकार हानिरहित हैं; इसे सूचक के रूप में चुना जाता है, सबसे ख़तरनाक होने के कारण नहीं। "
  "उचित क्लोरीनीकरण से यह मर जाता है, इसलिए उपचार के बाद इसकी उपस्थिति विसंक्रमण की विफलता दिखाती है। भारत का पेयजल मानक, IS 10500, किसी भी 100 मिली नमूने में इसकी अनुपस्थिति माँगता है।",
  "Bureau of Indian Standards -- IS 10500:2012, Drinking Water Specification.", "env-ecoli-indicator", craft="linkage")

# ================================================================ statements (5)
S(SCI, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Since climate is the average of weather over a long period, usually 30 years, one unusually cold winter does not by itself show that global warming has stopped.",
   "Because the oceans take up most of the extra heat trapped by greenhouse gases, the surface air warms less than it otherwise would.",
   "Land areas are warming faster than the oceans, partly because water needs more heat to warm up and loses heat through evaporation."],
  ["चूँकि जलवायु लंबी अवधि, प्रायः 30 वर्ष, के मौसम का औसत है, इसलिए एक असामान्य रूप से ठंडी सर्दी अपने आप में यह नहीं दिखाती कि वैश्विक तापवृद्धि रुक गई है।",
   "चूँकि ग्रीनहाउस गैसों द्वारा रोकी गई अतिरिक्त ऊष्मा का अधिकांश भाग महासागर ले लेते हैं, इसलिए सतह की वायु उतनी गर्म नहीं होती जितनी अन्यथा होती।",
   "स्थल भाग महासागरों से तेज़ी से गर्म हो रहे हैं, आंशिक रूप से इसलिए कि जल को गर्म होने के लिए अधिक ऊष्मा चाहिए और वह वाष्पीकरण से ऊष्मा खोता है।"],
  C3, 2,
  "All three are correct. Climate is described by 30-year averages, the 'climate normals' of the World Meteorological Organization, so a single cold season is weather, not a trend. More than 90 per cent of the extra heat trapped since the 1970s has gone into the oceans, which slows the rise in air temperature. "
  "Water has a much higher heat capacity than land and can lose heat by evaporation, so the land surface has warmed faster than the sea surface -- which is one reason why continents feel the heat sooner.",
  "तीनों कथन सही हैं। जलवायु का वर्णन 30 वर्षों के औसतों, विश्व मौसम विज्ञान संगठन के 'जलवायु मानकों', से होता है, इसलिए एक ठंडा मौसम मौसम ही है, प्रवृत्ति नहीं। 1970 के दशक से रोकी गई अतिरिक्त ऊष्मा का 90 प्रतिशत से अधिक भाग महासागरों में गया है, जो वायु के तापमान की वृद्धि को धीमा करता है। "
  "जल की ऊष्मा-धारिता स्थल से बहुत अधिक है और वह वाष्पीकरण से ऊष्मा खो सकता है, इसलिए स्थल की सतह समुद्र की सतह से तेज़ी से गर्म हुई है, जो एक कारण है कि महाद्वीप गर्मी जल्दी महसूस करते हैं।",
  AR6, "env-climate-basics-land-ocean", craft="linkage")

S(POL, "easy", "A city is choosing how to handle its waste. In the light of the waste hierarchy, consider the following statements:",
  "एक शहर तय कर रहा है कि अपने अपशिष्ट को कैसे सँभाले। अपशिष्ट पदानुक्रम के आलोक में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Setting up refill stations so that households reuse their detergent bottles ranks above collecting the bottles for recycling.",
   "Burning mixed waste to generate electricity ranks above composting the city's wet waste.",
   "Sending waste to a sanitary landfill is the least preferred of the options."],
  ["रिफ़िल केंद्र बनाना ताकि घर अपनी डिटर्जेंट की बोतलें फिर से उपयोग करें, बोतलों को पुनर्चक्रण के लिए इकट्ठा करने से ऊपर आता है।",
   "मिश्रित अपशिष्ट जलाकर बिजली बनाना शहर के गीले अपशिष्ट से कम्पोस्ट बनाने से ऊपर आता है।",
   "अपशिष्ट को स्वच्छ भराव-क्षेत्र (सैनिटरी लैंडफ़िल) में भेजना सबसे कम पसंदीदा विकल्प है।"],
  C3, 1,
  "Statements 1 and 3 are correct. The hierarchy ranks the options from most to least preferred: prevent or reduce, reuse, recycle (composting counts as recycling organic matter), recover energy, and dispose. Reuse keeps the bottle in service without the energy needed to reprocess it, so it ranks above recycling; landfilling is the last resort, because landfills take up land, leak leachate and give off methane. "
  "Statement 2 reverses two steps: composting returns nutrients and organic matter to the soil and ranks above energy recovery, while burning mixed, wet waste yields little energy and leaves ash and air pollution.",
  "कथन 1 और 3 सही हैं। पदानुक्रम विकल्पों को सबसे अधिक से सबसे कम पसंदीदा के क्रम में रखता है: रोकथाम या कमी, पुनः उपयोग, पुनर्चक्रण (कम्पोस्ट बनाना जैविक पदार्थ का पुनर्चक्रण गिना जाता है), ऊर्जा-प्राप्ति, और निपटान। पुनः उपयोग बोतल को बिना पुनर्प्रसंस्करण की ऊर्जा के काम में रखता है, इसलिए पुनर्चक्रण से ऊपर है; भराव-क्षेत्र अंतिम उपाय है, क्योंकि वह भूमि घेरता है, निक्षालित द्रव रिसाता है और मीथेन छोड़ता है। "
  "कथन 2 दो सीढ़ियों को उलट देता है: कम्पोस्ट मिट्टी को पोषक तत्व और जैविक पदार्थ लौटाता है और ऊर्जा-प्राप्ति से ऊपर है, जबकि मिश्रित, गीला अपशिष्ट जलाने से कम ऊर्जा मिलती है और राख तथा वायु प्रदूषण बचता है।",
  "United Nations Environment Programme -- Global Waste Management Outlook.", "env-waste-hierarchy", craft="application")

S(POL, "medium", "Consider the following statements about fly ash:",
  "फ़्लाई ऐश के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Because Indian coal has a high ash content, India's thermal power plants produce far more fly ash per unit of electricity than plants burning low-ash coal.",
   "Fly ash is classed as hazardous waste, so its use in bricks and road embankments is barred.",
   "Using fly ash in place of part of the clinker in cement increases the carbon dioxide emitted per tonne of cement."],
  ["चूँकि भारतीय कोयले में राख की मात्रा अधिक है, इसलिए भारत के ताप-विद्युत संयंत्र कम राख वाला कोयला जलाने वाले संयंत्रों की तुलना में प्रति इकाई बिजली कहीं अधिक फ़्लाई ऐश बनाते हैं।",
   "फ़्लाई ऐश ख़तरनाक अपशिष्ट की श्रेणी में है, इसलिए ईंटों और सड़क-तटबंधों में इसके उपयोग पर रोक है।",
   "सीमेंट में क्लिंकर के एक भाग के स्थान पर फ़्लाई ऐश के उपयोग से प्रति टन सीमेंट उत्सर्जित कार्बन डाइऑक्साइड बढ़ जाती है।"],
  C3, 0,
  "Only statement 1 is correct. Much Indian coal carries 30-45 per cent ash, far more than most imported coal, so the country's plants generate well over 200 million tonnes of fly ash a year. "
  "Statement 2 is wrong on both counts: fly ash is not listed as hazardous waste, and the Environment Ministry's notification of 2021 requires power plants to ensure that all their ash is used -- in bricks, cement, roads, embankments and mine filling -- with penalties for ash left unused. Statement 3 is the reverse: making clinker is the most carbon-intensive step in cement, so replacing part of it with fly ash, as in Portland pozzolana cement, cuts the carbon dioxide per tonne and saves limestone.",
  "केवल कथन 1 सही है। बहुत से भारतीय कोयले में 30-45 प्रतिशत राख होती है, जो अधिकांश आयातित कोयले से कहीं अधिक है, इसलिए देश के संयंत्र प्रति वर्ष 20 करोड़ टन से कहीं अधिक फ़्लाई ऐश बनाते हैं। "
  "कथन 2 दोनों दृष्टियों से गलत है: फ़्लाई ऐश ख़तरनाक अपशिष्ट में सूचीबद्ध नहीं है, और पर्यावरण मंत्रालय की 2021 की अधिसूचना बिजली संयंत्रों से अपेक्षा करती है कि उनकी सारी राख ईंटों, सीमेंट, सड़कों, तटबंधों और खदान-भराई में काम आए, और अप्रयुक्त राख पर दंड है। कथन 3 उलटा है: क्लिंकर बनाना सीमेंट का सबसे अधिक कार्बन-गहन चरण है, इसलिए उसके एक भाग के स्थान पर फ़्लाई ऐश, जैसे पोर्टलैंड पोज़ोलाना सीमेंट में, प्रति टन कार्बन डाइऑक्साइड घटाती है और चूना-पत्थर बचाती है।",
  "Ministry of Environment, Forest and Climate Change -- Fly ash utilisation notification, 2021.", "env-fly-ash", craft="inference")

S(POL, "medium", "Consider the following statements about groundwater contamination in India:",
  "भारत में भूजल संदूषण के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Arsenic in the groundwater of the Ganga-Brahmaputra plains is mainly of natural origin, released from the sediments of the aquifers themselves.",
   "Boiling arsenic-contaminated water at home makes it safe to drink.",
   "Uranium above the safe limit has been reported in groundwater in parts of Punjab."],
  ["गंगा-ब्रह्मपुत्र मैदानों के भूजल में आर्सेनिक मुख्यतः प्राकृतिक मूल का है, जो स्वयं जलभृतों के अवसादों से निकलता है।",
   "आर्सेनिक-दूषित जल को घर पर उबालने से वह पीने के लिए सुरक्षित हो जाता है।",
   "पंजाब के कुछ भागों के भूजल में सुरक्षित सीमा से अधिक यूरेनियम पाया गया है।"],
  C3, 1,
  "Statements 1 and 3 are correct. In the young alluvial aquifers of West Bengal, Bihar, Uttar Pradesh and Assam, arsenic is released naturally from iron-oxide coatings on sediment grains when the groundwater turns oxygen-poor; long-term drinking causes skin lesions and cancers. Surveys by the Central Ground Water Board have found uranium above the safe limit in parts of Punjab and several other States, where it too is largely geogenic. "
  "Statement 2 is wrong: boiling drives off water and leaves the arsenic behind, so it concentrates it; removal needs treatment such as adsorption or coagulation, or a safe source such as deeper aquifers or treated surface water.",
  "कथन 1 और 3 सही हैं। पश्चिम बंगाल, बिहार, उत्तर प्रदेश और असम के नए जलोढ़ जलभृतों में, जब भूजल में ऑक्सीजन घटती है, तो आर्सेनिक अवसाद-कणों पर लौह-ऑक्साइड की परतों से प्राकृतिक रूप से निकलता है; लंबे समय तक पीने से त्वचा के घाव और कैंसर होते हैं। केंद्रीय भूमि जल बोर्ड के सर्वेक्षणों ने पंजाब और कई अन्य राज्यों के कुछ भागों में सुरक्षित सीमा से अधिक यूरेनियम पाया है, जो वहाँ भी अधिकतर भूजनित है। "
  "कथन 2 गलत है: उबालने से पानी भाप बनकर उड़ता है और आर्सेनिक पीछे रह जाता है, इसलिए वह और सांद्र हो जाता है; उसे हटाने के लिए अधिशोषण या स्कंदन जैसा उपचार, या गहरे जलभृत अथवा उपचारित सतही जल जैसा सुरक्षित स्रोत चाहिए।",
  "Central Ground Water Board -- Ground Water Quality in Shallow Aquifers of India.", "env-groundwater-geogenic-contaminants", craft="inference")

S(POL, "medium", "Consider the following statements about microplastics:",
  "माइक्रोप्लास्टिक के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["They are generally defined as plastic particles smaller than 5 micrometres.",
   "Because toxic chemicals can stick to their surface, animals that swallow them may take in those chemicals too.",
   "Since sewage treatment plants remove all of them, treated effluent is not a source of microplastics."],
  ["इन्हें प्रायः 5 माइक्रोमीटर से छोटे प्लास्टिक कणों के रूप में परिभाषित किया जाता है।",
   "चूँकि विषैले रसायन इनकी सतह पर चिपक सकते हैं, इसलिए इन्हें निगलने वाले प्राणी उन रसायनों को भी ग्रहण कर सकते हैं।",
   "चूँकि सीवेज उपचार संयंत्र इन सभी को हटा देते हैं, इसलिए उपचारित बहिःस्राव माइक्रोप्लास्टिक का स्रोत नहीं है।"],
  C3, 0,
  "Only statement 2 is correct. Their small size and large surface area let microplastics pick up persistent pollutants such as PCBs from sea water, and plankton, fish and shellfish that swallow them can take up those chemicals, besides suffering blocked guts and reduced feeding; microplastics have been found in seafood, drinking water and human blood. "
  "Statement 1 gets the unit wrong: the usual definition is particles smaller than 5 millimetres. Statement 3 is wrong: treatment plants trap most microplastics in the sludge -- which may itself be spread on farmland -- but a share still leaves with the effluent, and fibres shed from synthetic clothes in the wash are a major source.",
  "केवल कथन 2 सही है। अपने छोटे आकार और बड़े सतही क्षेत्र के कारण माइक्रोप्लास्टिक समुद्री जल से PCB जैसे स्थायी प्रदूषक ग्रहण कर लेते हैं, और इन्हें निगलने वाले प्लवक, मछलियाँ और सीपदार जीव उन रसायनों को ले सकते हैं, साथ ही आँत अवरुद्ध होने और भोजन घटने की हानि भी झेलते हैं; माइक्रोप्लास्टिक समुद्री भोजन, पेयजल और मानव रक्त में पाए गए हैं। "
  "कथन 1 में इकाई गलत है: सामान्य परिभाषा 5 मिलीमीटर से छोटे कणों की है। कथन 3 गलत है: उपचार संयंत्र अधिकांश माइक्रोप्लास्टिक को गाद में रोक लेते हैं, जो स्वयं खेतों में फैलाई जा सकती है, पर एक भाग बहिःस्राव के साथ निकल जाता है, और धुलाई में कृत्रिम कपड़ों से झड़ने वाले रेशे एक बड़ा स्रोत हैं।",
  "United Nations Environment Programme -- Marine Litter and Microplastics.", "env-microplastics", craft="linkage")

# ================================================================ TAGS for the 88 kept rows (Test 21's 5 are tagged already)
TAGS = {
 "env-sids-one-point-five": "linkage", "env-paris-ndc-design": "linkage", "env-cop-outcomes-pairs": "recall",
 "env-climate-initiatives-pairs": "recall", "env-panchamrit-cop26": "recall", "env-btr-enhanced-transparency": "recall",
 "env-kyoto-basket-cfc": "precision", "env-cop-basics": "recall", "env-kyoto-protocol-targets": "precision",
 "env-paris-agreement-basics": "precision", "env-unfccc-bonn-cop8-delhi": "recall", "env-carbon-tax-vs-cap-and-trade": "inference",
 "env-global-stocktake": "precision", "env-kyoto-cdm-ji": "precision", "env-ncqg-cop29": "recall",
 "env-carbon-credit-trading-scheme": "precision", "env-eu-cbam": "precision", "env-gcf-adaptation-fund": "recall",
 "env-india-ndc-2035": "precision", "env-international-solar-alliance": "precision", "env-jetp": "recall",
 "env-loss-damage-fund": "precision", "env-paris-article6": "precision", "env-unfccc-annexes": "precision",
 "env-unfccc-basics": "precision",
 "env-himalayan-glacier-loss": "linkage", "env-warming-extreme-rainfall": "linkage", "env-coral-bleaching": "linkage",
 "env-sea-level-rise-causes": "inference", "env-climate-terms-pairs": "precision", "env-arctic-amplification": "linkage",
 "env-gwp-sf6-highest": "precision", "env-solar-radiation-modification": "precision", "env-co2-water-vapour": "recall",
 "env-india-clean-energy-schemes": "recall", "env-ipcc-role": "recall", "env-net-zero-meaning": "precision",
 "env-climate-sensitivity": "precision", "env-ipcc-ar6-findings": "precision", "env-keeling-curve": "precision",
 "env-short-lived-climate-pollutants": "multi", "env-aerosols-black-carbon": "linkage", "env-agricultural-methane": "linkage",
 "env-amoc": "inference", "env-ccus-dac-biochar": "precision", "env-gwp-methane-n2o": "inference",
 "env-heat-stress-wet-bulb": "inference", "env-hydrogen-colours": "precision", "env-milankovitch-cycles": "precision",
 "env-ocean-acidification": "linkage", "env-ozone-vs-warming-confusions": "precision", "env-permafrost": "linkage",
 "env-renewable-technologies": "linkage", "env-urban-heat-island": "linkage",
 "env-open-burning-plastic": "linkage", "env-deep-sea-mining": "inference", "env-delhi-winter-smog": "linkage",
 "env-ev-tailpipe-coal-grid": "inference", "env-pollutant-sources-pairs": "recall", "env-pollutant-diseases-pairs": "precision",
 "env-swachh-survekshan": "recall", "env-resin-identification-code": "recall", "env-pan-secondary-pollutant": "precision",
 "env-phytoremediation": "application", "env-so2-coal-power": "recall", "env-carbon-monoxide": "recall",
 "env-decibel-scale": "precision", "env-indoor-air-pollution": "recall", "env-leaded-petrol-lead": "recall",
 "env-thermal-pollution": "linkage", "env-naaqs-2009": "precision", "env-radioactive-pollutants": "precision",
 "env-rare-earth-elements": "precision", "env-virtual-water": "application", "env-who-aqg-ncap": "recall",
 "env-acid-rain": "precision", "env-air-pollution-control-devices": "precision", "env-biomagnification": "linkage",
 "env-bod-cod": "precision", "env-bs-vi-norms": "precision", "env-eutrophication": "precision",
 "env-ewaste-rules-2022": "recall", "env-ground-level-ozone": "linkage", "env-light-pollution": "precision",
 "env-noise-rules-2000": "recall", "env-plastic-waste-rules": "recall", "env-sewage-treatment-stages": "precision",
 "env-swm-rules-2026": "recall"}

if __name__ == "__main__":
    write_updates("upg_l2_t10_env.sql", statuses=("draft", "published"), tags=TAGS)
