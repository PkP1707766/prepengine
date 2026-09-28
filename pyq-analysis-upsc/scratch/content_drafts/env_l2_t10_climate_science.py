# -*- coding: utf-8 -*-
"""Level 2 · Test 10 (Environment 2: Climate Change & Pollution) -- Climate Science &
Mitigation, 17 new bilingual rows against the live gap report: medium statement 7, easy
statement 3, hard statement 2, medium MCQ 1, easy MCQ 1, medium Statement-I/II 1, hard
Statement-I/II/III 1, medium pairs 1. Concepts already in the bank (aerosols/black carbon,
Arctic amplification, blue carbon, carbon budget, CO2/water vapour, GWP of methane and N2O,
Himalayan glaciers, hydrogen colours, IPCC AR6 and role, Keeling curve, ocean acidification,
permafrost, sea-level rise, solar radiation modification, urban heat island) are not repeated."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Environment & Ecology"
K = "Climate Science & Mitigation"
AR6 = "IPCC Sixth Assessment Report (AR6), Working Group I, Summary for Policymakers (2021)"
AR6_3 = "IPCC AR6, Working Group III -- Mitigation of Climate Change (2022)"

# ---------------------------------------------------------------- medium statements (7)
S(K, "medium", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Depletion of the stratospheric ozone layer is the main cause of global warming.",
   "Carbon dioxide is one of the main ozone-depleting substances.",
   "Hydrofluorocarbons (HFCs), which replaced CFCs in many uses, damage the ozone layer about as much as CFCs do."],
  ["समतापमंडलीय ओज़ोन परत का क्षरण वैश्विक तापन का मुख्य कारण है।",
   "कार्बन डाइऑक्साइड मुख्य ओज़ोन-क्षयकारी पदार्थों में से एक है।",
   "कई उपयोगों में CFC की जगह लेने वाले हाइड्रोफ़्लोरोकार्बन (HFC) ओज़ोन परत को लगभग उतना ही नुकसान पहुँचाते हैं जितना CFC।"],
  C3, 3,
  "None of the statements is correct; all three mix up two different problems. The ozone hole is caused by chlorine and bromine released from substances such as CFCs and halons, and it lets more ultraviolet radiation reach the surface. Global warming is caused by greenhouse gases trapping outgoing infrared radiation, above all carbon dioxide; ozone loss is not its main driver. "
  "Carbon dioxide does not destroy ozone. HFCs contain no chlorine, so they have practically zero ozone-depleting potential -- but many are powerful greenhouse gases, which is why the 2016 Kigali Amendment to the Montreal Protocol set a schedule to phase them down.",
  "कोई भी कथन सही नहीं है; तीनों दो अलग-अलग समस्याओं को आपस में मिला देते हैं। ओज़ोन छिद्र CFC और हैलॉन जैसे पदार्थों से निकलने वाले क्लोरीन और ब्रोमीन से बनता है, और इससे अधिक पराबैंगनी विकिरण सतह तक पहुँचता है। वैश्विक तापन ग्रीनहाउस गैसों, सबसे बढ़कर कार्बन डाइऑक्साइड, द्वारा बाहर जाते अवरक्त विकिरण को रोकने से होता है; ओज़ोन क्षरण इसका मुख्य कारण नहीं है। "
  "कार्बन डाइऑक्साइड ओज़ोन को नष्ट नहीं करती। HFC में क्लोरीन नहीं होता, इसलिए उनकी ओज़ोन-क्षयकारी क्षमता लगभग शून्य है; पर इनमें से कई शक्तिशाली ग्रीनहाउस गैसें हैं, इसीलिए मॉन्ट्रियल प्रोटोकॉल के 2016 के किगाली संशोधन ने इन्हें चरणबद्ध रूप से घटाने की समय-सारिणी तय की।",
  "UNEP Ozone Secretariat -- Montreal Protocol and Kigali Amendment (2016); WMO/UNEP Scientific Assessment of Ozone Depletion (2022).",
  "env-ozone-vs-warming-confusions")

S(K, "medium", "Consider the following statements about heat stress:",
  "ऊष्मा-तनाव (heat stress) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Wet-bulb temperature combines the effect of heat and humidity.",
   "At the same air temperature, dry heat is more dangerous to the human body than humid heat.",
   "The India Meteorological Department declares a heatwave in the plains only when the maximum temperature crosses 50 degrees Celsius."],
  ["आर्द्र-बल्ब तापमान (wet-bulb temperature) गर्मी और आर्द्रता, दोनों के प्रभाव को जोड़ता है।",
   "समान वायु तापमान पर शुष्क गर्मी मानव शरीर के लिए आर्द्र गर्मी से अधिक खतरनाक होती है।",
   "भारत मौसम विज्ञान विभाग मैदानी क्षेत्रों में लू (heatwave) तभी घोषित करता है जब अधिकतम तापमान 50 डिग्री सेल्सियस पार कर जाए।"],
  C3, 0,
  "Only statement 1 is correct: wet-bulb temperature is the lowest temperature to which air can be cooled by evaporating water into it, so it captures how well sweat can cool the body. A sustained wet-bulb temperature of about 35 degrees Celsius is taken as the theoretical limit of human survival. "
  "Statement 2 is reversed: in humid heat sweat evaporates poorly, so the body cannot shed heat -- which is why coastal and Indo-Gangetic heat with high humidity is so deadly. "
  "Statement 3 is wrong: for the plains, the IMD declares a heatwave when the maximum temperature is at least 40 degrees Celsius and 4.5 to 6.4 degrees above normal, or when it reaches 45 degrees or more regardless of the normal.",
  "केवल कथन 1 सही है: आर्द्र-बल्ब तापमान वह न्यूनतम तापमान है जिस तक हवा को उसमें पानी वाष्पित करके ठंडा किया जा सकता है, इसलिए यह दिखाता है कि पसीना शरीर को कितना ठंडा कर सकता है। लगभग 35 डिग्री सेल्सियस का लगातार आर्द्र-बल्ब तापमान मानव जीवन की सैद्धांतिक सीमा माना जाता है। "
  "कथन 2 उलटा है: आर्द्र गर्मी में पसीना ठीक से वाष्पित नहीं होता, इसलिए शरीर गर्मी बाहर नहीं निकाल पाता; इसीलिए उच्च आर्द्रता वाली तटीय और सिंधु-गंगा मैदान की गर्मी इतनी घातक होती है। "
  "कथन 3 गलत है: मैदानी क्षेत्रों के लिए IMD तब लू घोषित करता है जब अधिकतम तापमान कम से कम 40 डिग्री सेल्सियस हो और सामान्य से 4.5 से 6.4 डिग्री अधिक हो, या जब वह सामान्य की परवाह किए बिना 45 डिग्री या उससे अधिक पहुँच जाए।",
  "India Meteorological Department -- criteria for heatwave; NDMA -- National Guidelines on Heat Wave; S.C. Sherwood and M. Huber, PNAS 107 (2010).",
  "env-heat-stress-wet-bulb")

S(K, "medium", "Consider the following statements about removing carbon dioxide from the atmosphere or from emission sources:",
  "वायुमंडल या उत्सर्जन स्रोतों से कार्बन डाइऑक्साइड हटाने के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Carbon capture, utilisation and storage (CCUS) captures carbon dioxide from large point sources such as power and cement plants.",
   "Direct air capture removes carbon dioxide from the ambient air.",
   "Biochar is made by burning biomass in a plentiful supply of oxygen.",
   "Biochar added to soil can keep its carbon locked away for centuries."],
  ["कार्बन अभिग्रहण, उपयोग और भंडारण (CCUS) बिजली और सीमेंट संयंत्रों जैसे बड़े बिंदु-स्रोतों से कार्बन डाइऑक्साइड पकड़ता है।",
   "प्रत्यक्ष वायु अभिग्रहण (direct air capture) आसपास की हवा से कार्बन डाइऑक्साइड हटाता है।",
   "बायोचार जैव-भार को ऑक्सीजन की भरपूर आपूर्ति में जलाकर बनाया जाता है।",
   "मिट्टी में मिलाया गया बायोचार अपने कार्बन को सदियों तक बंद रख सकता है।"],
  C4, 2,
  "Statements 1, 2 and 4 are correct. CCUS captures carbon dioxide at the chimney of an industrial plant and either stores it deep underground or uses it; it cuts new emissions but does not by itself remove old ones. Direct air capture pulls carbon dioxide out of ordinary air, which is far more dilute, so it takes much more energy per tonne. "
  "Statement 3 is the trap: burning biomass in plenty of oxygen simply turns its carbon back into carbon dioxide. Biochar is made by pyrolysis -- heating biomass with little or no oxygen -- which leaves a stable, charcoal-like solid; in soil it resists decay for centuries and can also improve water and nutrient retention.",
  "कथन 1, 2 और 4 सही हैं। CCUS किसी औद्योगिक संयंत्र की चिमनी पर कार्बन डाइऑक्साइड पकड़कर उसे ज़मीन में गहराई पर संग्रहीत करता है या उसका उपयोग करता है; यह नए उत्सर्जन घटाता है, पर अपने-आप पुराने उत्सर्जन नहीं हटाता। प्रत्यक्ष वायु अभिग्रहण साधारण हवा से, जिसमें कार्बन डाइऑक्साइड बहुत विरल होती है, उसे खींचता है, इसलिए प्रति टन कहीं अधिक ऊर्जा लगती है। "
  "कथन 3 जाल है: जैव-भार को भरपूर ऑक्सीजन में जलाने से उसका कार्बन फिर से कार्बन डाइऑक्साइड बन जाता है। बायोचार तापीय अपघटन (pyrolysis) से बनता है, यानी जैव-भार को बहुत कम या बिना ऑक्सीजन के गर्म करके, जिससे कोयले जैसा स्थिर ठोस बचता है; मिट्टी में यह सदियों तक सड़ता नहीं और पानी तथा पोषक तत्व रोकने की क्षमता भी बढ़ा सकता है।",
  f"{AR6_3} (carbon dioxide removal, CCS); NITI Aayog -- Carbon Capture, Utilisation and Storage: Policy Framework and its Deployment Mechanism in India (2022).",
  "env-ccus-dac-biochar")

S(K, "medium", "Consider the following statements about the Atlantic Meridional Overturning Circulation (AMOC):",
  "अटलांटिक मेरिडियनल ओवरटर्निंग सर्कुलेशन (AMOC) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It carries warm surface water northwards in the Atlantic Ocean.",
   "Fresh water from the melting Greenland ice sheet can weaken it.",
   "A collapse of the AMOC would make north-western Europe markedly warmer."],
  ["यह अटलांटिक महासागर में गर्म सतही जल को उत्तर की ओर ले जाता है।",
   "पिघलती ग्रीनलैंड हिम-चादर का मीठा पानी इसे कमज़ोर कर सकता है।",
   "AMOC के ढहने से उत्तर-पश्चिमी यूरोप काफ़ी अधिक गर्म हो जाएगा।"],
  C3, 1,
  "Statements 1 and 2 are correct. In the AMOC, warm, salty surface water (including the Gulf Stream) flows north, gives up its heat, becomes cold and dense in the North Atlantic, sinks and returns south at depth. Fresh meltwater from Greenland makes the surface water lighter, so less of it sinks, which weakens the overturning; the IPCC judges a weakening this century very likely. "
  "Statement 3 is the reverse: the northward flow of heat is what keeps north-western Europe mild for its latitude, so a collapse would make it much colder. It would also shift the tropical rain belt southwards, which could disturb the West African and Indian monsoons -- one of the 'tipping points' of the climate system.",
  "कथन 1 और 2 सही हैं। AMOC में गर्म, खारा सतही जल (गल्फ़ स्ट्रीम सहित) उत्तर की ओर बहता है, अपनी गर्मी छोड़ता है, उत्तरी अटलांटिक में ठंडा और घना होकर नीचे बैठता है और गहराई में दक्षिण की ओर लौटता है। ग्रीनलैंड का मीठा पिघला पानी सतही जल को हल्का कर देता है, जिससे कम जल नीचे बैठता है और यह परिसंचरण कमज़ोर होता है; IPCC इस सदी में इसके कमज़ोर होने को बहुत संभावित मानता है। "
  "कथन 3 उलटा है: गर्मी का यही उत्तरमुखी प्रवाह उत्तर-पश्चिमी यूरोप को उसके अक्षांश की तुलना में सौम्य रखता है, इसलिए इसके ढहने से वह बहुत ठंडा हो जाएगा। इससे उष्णकटिबंधीय वर्षा-पट्टी भी दक्षिण की ओर खिसकेगी, जो पश्चिम अफ़्रीकी और भारतीय मानसून को बिगाड़ सकती है; यह जलवायु तंत्र के 'टिपिंग पॉइंट' में से एक है।",
  f"{AR6}; IPCC Special Report on the Ocean and Cryosphere in a Changing Climate (2019).",
  "env-amoc")

S(K, "medium", "Consider the following statements about renewable energy technologies:",
  "नवीकरणीय ऊर्जा प्रौद्योगिकियों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Solar photovoltaic cells convert sunlight directly into electricity.",
   "Offshore wind turbines generally produce more electricity than onshore turbines of the same size, because winds at sea are stronger and steadier.",
   "Floating solar plants on reservoirs can reduce the loss of water by evaporation."],
  ["सौर फ़ोटोवोल्टिक सेल सूर्य के प्रकाश को सीधे बिजली में बदलते हैं।",
   "समान आकार की तटवर्ती (onshore) टर्बाइनों की तुलना में अपतटीय (offshore) पवन टर्बाइनें सामान्यतः अधिक बिजली बनाती हैं, क्योंकि समुद्र पर हवाएँ अधिक तेज़ और स्थिर होती हैं।",
   "जलाशयों पर तैरते सौर संयंत्र वाष्पीकरण से होने वाली पानी की हानि घटा सकते हैं।"],
  C3, 2,
  "All three statements are correct. Photovoltaic cells, made mostly of silicon, generate a current when light falls on them -- unlike concentrated solar power, which uses mirrors to make heat. "
  "Wind power rises with the cube of wind speed, so the stronger, steadier winds over the sea give offshore turbines a much higher capacity factor, though they cost more to build; India has identified sites off Gujarat and Tamil Nadu. "
  "Floating panels shade the water and so cut evaporation, while the water cools the panels and raises their efficiency, and no land has to be acquired.",
  "तीनों कथन सही हैं। मुख्यतः सिलिकॉन से बने फ़ोटोवोल्टिक सेल पर प्रकाश पड़ने से धारा बनती है; यह संकेंद्रित सौर ऊर्जा से अलग है, जो दर्पणों से ऊष्मा बनाती है। "
  "पवन ऊर्जा हवा की गति के घन के अनुपात में बढ़ती है, इसलिए समुद्र की तेज़, स्थिर हवाएँ अपतटीय टर्बाइनों को कहीं अधिक क्षमता-उपयोग (capacity factor) देती हैं, हालाँकि इन्हें लगाने की लागत अधिक है; भारत ने गुजरात और तमिलनाडु के तट के पास ऐसे स्थल चिह्नित किए हैं। "
  "तैरते पैनल पानी पर छाया करके वाष्पीकरण घटाते हैं, पानी पैनलों को ठंडा रखकर उनकी दक्षता बढ़ाता है, और किसी भूमि का अधिग्रहण नहीं करना पड़ता।",
  "Ministry of New and Renewable Energy -- solar, offshore wind and floating solar; National Institute of Wind Energy -- offshore wind assessment.",
  "env-renewable-technologies")

S(K, "medium", "Consider the following statements about Milankovitch cycles:",
  "मिलनकोविच चक्रों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["They are slow changes in the shape of the Earth's orbit and in the tilt and wobble of its axis, which alter how sunlight is distributed over the Earth.",
   "They are the main cause of the global warming observed since 1850.",
   "They are thought to pace the cycle of ice ages and warmer interglacial periods of the last million years."],
  ["ये पृथ्वी की कक्षा के आकार और उसके अक्ष के झुकाव तथा डगमगाहट में होने वाले धीमे परिवर्तन हैं, जो पृथ्वी पर सूर्य के प्रकाश के वितरण को बदलते हैं।",
   "ये 1850 से देखे गए वैश्विक तापन का मुख्य कारण हैं।",
   "माना जाता है कि ये पिछले दस लाख वर्षों के हिमयुगों और गर्म अंतर-हिमनदीय कालों के चक्र की गति तय करते हैं।"],
  C3, 1,
  "Statements 1 and 3 are correct. The eccentricity of the orbit, the tilt (obliquity) and the precession of the axis change over periods of roughly 100,000, 41,000 and 23,000 years; the resulting changes in summer sunshine at high northern latitudes are thought to set the rhythm of the ice ages, amplified by feedbacks from carbon dioxide and ice. "
  "Statement 2 is wrong because the timescales do not match: these cycles act over tens of thousands of years and would, if anything, now be leading very slowly towards cooling. The rapid warming since 1850 is, in the IPCC's words, unequivocally caused by human influence.",
  "कथन 1 और 3 सही हैं। कक्षा की उत्केंद्रता, अक्ष का झुकाव और अक्ष का पुरस्सरण (precession) लगभग 1,00,000, 41,000 और 23,000 वर्षों की अवधियों में बदलते हैं; उच्च उत्तरी अक्षांशों पर गर्मियों की धूप में इनसे होने वाले बदलाव, कार्बन डाइऑक्साइड और बर्फ़ की प्रतिपुष्टियों से बढ़कर, हिमयुगों की लय तय करते माने जाते हैं। "
  "कथन 2 इसलिए गलत है कि समय-मापक्रम मेल नहीं खाते: ये चक्र हज़ारों वर्षों में काम करते हैं और अभी तो, यदि कुछ, बहुत धीरे-धीरे ठंडक की ओर ले जाते। 1850 से हुआ तेज़ तापन, IPCC के शब्दों में, निर्विवाद रूप से मानवीय प्रभाव से हुआ है।",
  f"{AR6}; IPCC AR6 WG I, Chapter 2 (paleoclimate and orbital forcing).",
  "env-milankovitch-cycles")

S(K, "medium", "Consider the following statements about methane emissions from agriculture:",
  "कृषि से होने वाले मीथेन उत्सर्जन के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Flooded rice fields emit methane because organic matter decomposes there without oxygen.",
   "Enteric fermentation in the stomachs of cattle and buffaloes is a major source of methane.",
   "Alternate wetting and drying of rice fields, instead of keeping them flooded all the time, reduces methane emissions."],
  ["जलमग्न धान के खेत मीथेन उत्सर्जित करते हैं, क्योंकि वहाँ जैविक पदार्थ ऑक्सीजन के बिना अपघटित होता है।",
   "गाय और भैंस के पेट में होने वाला आंत्रिक किण्वन (enteric fermentation) मीथेन का एक प्रमुख स्रोत है।",
   "धान के खेतों को हर समय भरा रखने के बजाय बारी-बारी से भिगोने और सुखाने (alternate wetting and drying) से मीथेन उत्सर्जन घटता है।"],
  C3, 2,
  "All three statements are correct. Methane-producing microbes (methanogens) thrive in waterlogged, oxygen-free paddy soil, and in the rumen of cattle and buffaloes, which belch the gas out; livestock and rice together make agriculture India's largest source of methane. "
  "Letting the field dry out for a few days between irrigations lets oxygen into the soil and cuts methane sharply while saving water, often without loss of yield -- though it can raise nitrous oxide a little. Methane matters because it is far more potent than carbon dioxide over the short term.",
  "तीनों कथन सही हैं। मीथेन बनाने वाले सूक्ष्मजीव (मेथैनोजेन) जलभराव वाली, ऑक्सीजन-रहित धान की मिट्टी में और गाय-भैंस के रूमेन (प्रथम आमाशय) में पनपते हैं, जहाँ से यह गैस डकार के साथ निकलती है; पशुधन और धान मिलकर कृषि को भारत में मीथेन का सबसे बड़ा स्रोत बनाते हैं। "
  "सिंचाइयों के बीच कुछ दिन खेत को सूखने देने से मिट्टी में ऑक्सीजन पहुँचती है और पानी बचाते हुए मीथेन तेज़ी से घटती है, प्रायः उपज घटाए बिना; हालाँकि इससे नाइट्रस ऑक्साइड थोड़ी बढ़ सकती है। मीथेन इसलिए महत्त्वपूर्ण है कि अल्पावधि में यह कार्बन डाइऑक्साइड से कहीं अधिक शक्तिशाली है।",
  "ICAR -- climate-resilient rice cultivation (alternate wetting and drying); India's Biennial Update Reports to the UNFCCC (agriculture sector emissions).",
  "env-agricultural-methane")

# ---------------------------------------------------------------- easy statements (3)
S(K, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["A country that reaches 'net zero' emits no greenhouse gases at all.",
   "Under net zero, any remaining emissions are balanced by an equal amount of removals from the atmosphere."],
  ["'नेट ज़ीरो' पर पहुँचने वाला देश कोई भी ग्रीनहाउस गैस उत्सर्जित नहीं करता।",
   "नेट ज़ीरो में बचे हुए उत्सर्जन को वायुमंडल से उतनी ही मात्रा के निष्कासन से संतुलित किया जाता है।"],
  T2, 1,
  "Only statement 2 is correct. Net zero does not mean zero emissions: some emissions, for instance from agriculture or cement, may remain, but they are balanced by removals -- through forests and soils or technologies such as direct air capture -- so that the net addition to the atmosphere is zero. That is why India's net-zero target for 2070 goes together with its goal of a larger forest carbon sink.",
  "केवल कथन 2 सही है। नेट ज़ीरो का अर्थ शून्य उत्सर्जन नहीं है: कुछ उत्सर्जन, जैसे कृषि या सीमेंट से, बचे रह सकते हैं, पर उन्हें वनों और मिट्टी या प्रत्यक्ष वायु अभिग्रहण जैसी तकनीकों से होने वाले निष्कासन से संतुलित किया जाता है, ताकि वायुमंडल में शुद्ध वृद्धि शून्य रहे। इसीलिए भारत का 2070 का नेट-ज़ीरो लक्ष्य बड़े वन कार्बन-सिंक के लक्ष्य के साथ चलता है।",
  "IPCC AR6 Glossary (net zero emissions); India's Long-Term Low-Carbon Development Strategy, submitted to the UNFCCC (2022).",
  "env-net-zero-meaning")

S(K, "easy", "Consider the following statements about India's clean-energy programmes:",
  "भारत के स्वच्छ-ऊर्जा कार्यक्रमों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["PM Surya Ghar: Muft Bijli Yojana supports rooftop solar for households.",
   "PM-KUSUM supports solar pumps and solar power plants for farmers.",
   "The National Green Hydrogen Mission aims at a production capacity of at least 5 million tonnes of green hydrogen a year by 2030."],
  ["पीएम सूर्य घर: मुफ़्त बिजली योजना घरों के लिए छत पर सौर ऊर्जा (rooftop solar) को सहायता देती है।",
   "पीएम-कुसुम किसानों के लिए सौर पंप और सौर ऊर्जा संयंत्रों को सहायता देती है।",
   "राष्ट्रीय हरित हाइड्रोजन मिशन का लक्ष्य 2030 तक प्रति वर्ष कम से कम 50 लाख टन हरित हाइड्रोजन की उत्पादन क्षमता है।"],
  C3, 2,
  "All three statements are correct. PM Surya Ghar (2024) aims to put rooftop solar on one crore homes, with a central subsidy and free electricity up to a limit. PM-KUSUM (2019) helps farmers install standalone solar pumps, solarise grid-connected pumps and set up small solar plants on their land. "
  "The National Green Hydrogen Mission (2023) targets at least 5 million tonnes a year of green hydrogen capacity by 2030, with about 125 GW of associated renewable capacity, to cut the use of fossil fuels in refineries, fertilisers and steel.",
  "तीनों कथन सही हैं। पीएम सूर्य घर (2024) का लक्ष्य केंद्रीय सब्सिडी और एक सीमा तक मुफ़्त बिजली के साथ एक करोड़ घरों पर छत पर सौर ऊर्जा लगाना है। पीएम-कुसुम (2019) किसानों को स्वतंत्र सौर पंप लगाने, ग्रिड से जुड़े पंपों को सौर बनाने और अपनी भूमि पर छोटे सौर संयंत्र लगाने में मदद करती है। "
  "राष्ट्रीय हरित हाइड्रोजन मिशन (2023) का लक्ष्य 2030 तक प्रति वर्ष कम से कम 50 लाख टन हरित हाइड्रोजन क्षमता है, साथ में लगभग 125 गीगावाट नवीकरणीय क्षमता, ताकि रिफ़ाइनरी, उर्वरक और इस्पात में जीवाश्म ईंधन का उपयोग घटे।",
  "Ministry of New and Renewable Energy -- PM Surya Ghar: Muft Bijli Yojana (2024), PM-KUSUM (2019), National Green Hydrogen Mission (2023).",
  "env-india-clean-energy-schemes")

S(K, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Climate is the average weather of a place over a long period, usually taken as 30 years.",
   "The 1.5 degrees Celsius goal of the Paris Agreement refers to warming above pre-industrial levels.",
   "Land areas of the Earth are warming more slowly than the oceans."],
  ["जलवायु किसी स्थान का लंबी अवधि, सामान्यतः 30 वर्ष, का औसत मौसम है।",
   "पेरिस समझौते का 1.5 डिग्री सेल्सियस का लक्ष्य पूर्व-औद्योगिक स्तर से ऊपर के तापन को दर्शाता है।",
   "पृथ्वी के स्थलीय भाग महासागरों की तुलना में धीरे गर्म हो रहे हैं।"],
  C3, 1,
  "Statements 1 and 2 are correct. The World Meteorological Organization uses 30-year 'climate normals'; weather is what happens on a given day. The Paris temperature goals are measured against the 1850-1900 average, used as the pre-industrial baseline. "
  "Statement 3 is reversed: land warms faster than the ocean, because the ocean has a far larger capacity to store heat and loses heat by evaporation. By the IPCC's assessment, in 2011-2020 land had warmed by about 1.6 degrees Celsius and the ocean surface by about 0.9 degrees, against about 1.1 degrees for the globe as a whole.",
  "कथन 1 और 2 सही हैं। विश्व मौसम विज्ञान संगठन 30 वर्ष के 'जलवायु मानक' (climate normals) का उपयोग करता है; मौसम वह है जो किसी दिन विशेष पर होता है। पेरिस के तापमान लक्ष्य 1850-1900 के औसत से मापे जाते हैं, जिसे पूर्व-औद्योगिक आधार माना जाता है। "
  "कथन 3 उलटा है: स्थल महासागर से तेज़ गर्म होता है, क्योंकि महासागर की ऊष्मा संचित करने की क्षमता कहीं अधिक है और वह वाष्पीकरण से गर्मी खोता है। IPCC के आकलन के अनुसार 2011-2020 में पूरे विश्व के लगभग 1.1 डिग्री की तुलना में स्थल लगभग 1.6 डिग्री सेल्सियस और महासागर की सतह लगभग 0.9 डिग्री गर्म हो चुकी थी।",
  f"{AR6}; World Meteorological Organization -- climate normals; Paris Agreement, Article 2.",
  "env-climate-basics-land-ocean")

# ---------------------------------------------------------------- hard statements (2)
S(K, "hard", "Consider the following statements about climate sensitivity:",
  "जलवायु संवेदनशीलता (climate sensitivity) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Equilibrium climate sensitivity is the long-term global warming expected from a doubling of the atmospheric concentration of carbon dioxide.",
   "The IPCC's Sixth Assessment Report widened the likely range of its value, compared with earlier reports, to 1.5 to 4.5 degrees Celsius.",
   "When the concentration of carbon dioxide doubles, the full warming it causes is reached almost immediately."],
  ["संतुलन जलवायु संवेदनशीलता (equilibrium climate sensitivity) वायुमंडल में कार्बन डाइऑक्साइड की सांद्रता दोगुनी होने से अपेक्षित दीर्घकालिक वैश्विक तापन है।",
   "IPCC की छठी आकलन रिपोर्ट ने पिछली रिपोर्टों की तुलना में इसकी संभावित सीमा को चौड़ा करके 1.5 से 4.5 डिग्री सेल्सियस कर दिया।",
   "कार्बन डाइऑक्साइड की सांद्रता दोगुनी होते ही उससे होने वाला पूरा तापन लगभग तुरंत हो जाता है।"],
  C3, 0,
  "Only statement 1 is correct. Statement 2 reverses what AR6 did: the likely range of 1.5 to 4.5 degrees Celsius had stood, with small changes, since 1979 and was repeated in AR5; AR6, using several lines of evidence, narrowed it to 2.5 to 4 degrees, with a best estimate of 3 degrees. "
  "Statement 3 is wrong: the oceans absorb most of the extra heat and warm slowly, so the climate takes many decades to centuries to reach the new equilibrium. The warming at the time of doubling -- the 'transient climate response', about 1.8 degrees -- is lower, and some further warming is 'in the pipeline' even after concentrations stop rising.",
  "केवल कथन 1 सही है। कथन 2 AR6 के काम को उलट देता है: 1.5 से 4.5 डिग्री सेल्सियस की संभावित सीमा, छोटे-मोटे बदलावों के साथ, 1979 से चली आ रही थी और AR5 में भी दोहराई गई थी; AR6 ने कई प्रकार के साक्ष्यों के आधार पर इसे संकरा करके 2.5 से 4 डिग्री कर दिया, जिसका सर्वोत्तम अनुमान 3 डिग्री है। "
  "कथन 3 गलत है: अतिरिक्त गर्मी का अधिकांश भाग महासागर सोख लेते हैं और धीरे-धीरे गर्म होते हैं, इसलिए जलवायु को नए संतुलन तक पहुँचने में कई दशक से सदियाँ लगती हैं। दोगुनी होने के समय का तापन, यानी 'क्षणिक जलवायु प्रतिक्रिया' (transient climate response), लगभग 1.8 डिग्री, कम होता है, और सांद्रता का बढ़ना रुकने के बाद भी कुछ और तापन 'रास्ते में' रहता है।",
  f"{AR6} (section A.4 and Table SPM.1 context); IPCC AR6 WG I, Chapter 7.",
  "env-climate-sensitivity")

S(K, "hard", "Consider the following:",
  "निम्नलिखित पर विचार कीजिए:",
  ["Methane", "Tropospheric ozone", "Sulphur hexafluoride", "Nitrous oxide"],
  ["मीथेन", "क्षोभमंडलीय ओज़ोन", "सल्फ़र हेक्साफ़्लोराइड", "नाइट्रस ऑक्साइड"],
  C4, 1,
  "Two of them are: methane (atmospheric lifetime about 12 years) and tropospheric ozone (days to weeks); the Climate and Clean Air Coalition's list also includes black carbon and many hydrofluorocarbons. Because they leave the air quickly, cutting them slows warming within a decade or two, and since most also harm health and crops, such cuts bring quick co-benefits. "
  "Nitrous oxide is not one: it stays in the atmosphere for more than a century (about 110 to 120 years). Sulphur hexafluoride is the extreme case -- a lifetime of over 3,000 years -- so, like carbon dioxide, the warming of both accumulates. Potency (GWP) and lifetime are different things: a gas can be very powerful and long-lived, or powerful and short-lived.",
  "इनमें से दो हैं: मीथेन (वायुमंडलीय आयु लगभग 12 वर्ष) और क्षोभमंडलीय ओज़ोन (कुछ दिन से कुछ सप्ताह); जलवायु और स्वच्छ वायु गठबंधन (Climate and Clean Air Coalition) की सूची में ब्लैक कार्बन और कई हाइड्रोफ़्लोरोकार्बन भी हैं। चूँकि ये हवा से जल्दी हट जाते हैं, इन्हें घटाने से एक-दो दशक में ही तापन धीमा होता है, और चूँकि इनमें से अधिकांश स्वास्थ्य और फ़सलों को भी नुकसान पहुँचाते हैं, ऐसी कटौती से जल्दी सह-लाभ मिलते हैं। "
  "नाइट्रस ऑक्साइड इनमें नहीं है: यह वायुमंडल में सौ वर्ष से अधिक (लगभग 110 से 120 वर्ष) रहती है। सल्फ़र हेक्साफ़्लोराइड चरम उदाहरण है, जिसकी आयु 3,000 वर्ष से अधिक है; इसलिए कार्बन डाइऑक्साइड की तरह दोनों का तापन-प्रभाव जमा होता जाता है। क्षमता (GWP) और आयु अलग-अलग बातें हैं: कोई गैस बहुत शक्तिशाली और दीर्घजीवी हो सकती है, या शक्तिशाली और अल्पजीवी।",
  "UNEP -- Climate and Clean Air Coalition (short-lived climate pollutants); IPCC AR6 WG I, Chapter 6 and Table 7.15.",
  "env-short-lived-climate-pollutants",
  closing="How many of the above are generally classed as short-lived climate pollutants?",
  closing_hi="उपर्युक्त में से कितने सामान्यतः अल्पजीवी जलवायु प्रदूषक (short-lived climate pollutants) की श्रेणी में आते हैं?")

# ---------------------------------------------------------------- MCQs (2)
M(K, "medium", "Which one of the following gases has the highest global warming potential over a 100-year period?",
  "100 वर्ष की अवधि में निम्नलिखित में से किस गैस की वैश्विक तापन क्षमता (GWP) सबसे अधिक है?",
  ["Sulphur hexafluoride", "Nitrogen trifluoride", "Nitrous oxide", "Methane"],
  ["सल्फ़र हेक्साफ़्लोराइड", "नाइट्रोजन ट्राइफ़्लोराइड", "नाइट्रस ऑक्साइड", "मीथेन"],
  0,
  "Sulphur hexafluoride, used as an insulating gas in high-voltage electrical switchgear, has a 100-year GWP of about 24,300 in the IPCC's Sixth Assessment Report and lasts for thousands of years in the atmosphere, which is why it is one of the Kyoto gases despite its small emissions. "
  "Nitrogen trifluoride, used in making electronics and solar panels, is the close runner-up at about 17,400; nitrous oxide is about 273 and methane about 27 to 30.",
  "उच्च-वोल्टेज विद्युत स्विचगियर में विद्युत-रोधी गैस के रूप में उपयोग होने वाली सल्फ़र हेक्साफ़्लोराइड की 100 वर्ष की GWP IPCC की छठी आकलन रिपोर्ट में लगभग 24,300 है और यह वायुमंडल में हज़ारों वर्ष रहती है; इसीलिए कम उत्सर्जन के बावजूद यह क्योटो गैसों में से एक है। "
  "इलेक्ट्रॉनिक्स और सौर पैनल बनाने में उपयोग होने वाली नाइट्रोजन ट्राइफ़्लोराइड लगभग 17,400 के साथ निकट दूसरे स्थान पर है; नाइट्रस ऑक्साइड लगभग 273 और मीथेन लगभग 27 से 30 है।",
  "IPCC AR6 WG I, Chapter 7, Table 7.15 (global warming potentials); UNFCCC -- Kyoto Protocol basket of gases.",
  "env-gwp-sf6-highest")

M(K, "easy", "Which one of the following is NOT a greenhouse gas?",
  "निम्नलिखित में से कौन-सी एक ग्रीनहाउस गैस नहीं है?",
  ["Nitrogen", "Methane", "Nitrous oxide", "Ozone"],
  ["नाइट्रोजन", "मीथेन", "नाइट्रस ऑक्साइड", "ओज़ोन"],
  0,
  "Nitrogen (N2), which makes up about 78 per cent of the air, is not a greenhouse gas: molecules made of two identical atoms do not absorb infrared radiation. Methane, nitrous oxide and ozone all do. "
  "The trap is the similar names: nitrous oxide (N2O), a compound of nitrogen and oxygen released mainly from fertilised soils, is a powerful greenhouse gas and also depletes the ozone layer.",
  "हवा का लगभग 78 प्रतिशत भाग बनाने वाली नाइट्रोजन (N2) ग्रीनहाउस गैस नहीं है: दो समान परमाणुओं से बने अणु अवरक्त विकिरण नहीं सोखते। मीथेन, नाइट्रस ऑक्साइड और ओज़ोन, तीनों सोखते हैं। "
  "जाल मिलते-जुलते नामों में है: नाइट्रस ऑक्साइड (N2O), जो नाइट्रोजन और ऑक्सीजन का यौगिक है और मुख्यतः उर्वरक डाली गई मिट्टी से निकलता है, एक शक्तिशाली ग्रीनहाउस गैस है और ओज़ोन परत का क्षरण भी करता है।",
  "NCERT Class XI, Chemistry -- Environmental Chemistry (global warming and greenhouse effect); IPCC AR6 WG I, Chapter 7.",
  "env-not-a-greenhouse-gas")

# ---------------------------------------------------------------- Statement-I/II (medium), I/II/III (hard)
A(K, "medium",
  "Mass coral bleaching events have become more frequent in recent decades.",
  "हाल के दशकों में बड़े पैमाने पर प्रवाल विरंजन (coral bleaching) की घटनाएँ अधिक बार होने लगी हैं।",
  "When sea water stays unusually warm for weeks, corals expel the symbiotic algae (zooxanthellae) living in their tissues.",
  "जब समुद्री जल कई सप्ताह तक असामान्य रूप से गर्म रहता है, तो प्रवाल अपने ऊतकों में रहने वाले सहजीवी शैवाल (ज़ूज़ैंथेली) को बाहर निकाल देते हैं।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I. Corals get their colour and most of their food from zooxanthellae; under prolonged heat stress the partnership breaks down, the algae are expelled and the white skeleton shows through. Bleached corals can recover if the water cools soon enough, but repeated events leave too little time. "
  "As ocean temperatures have risen, marine heatwaves have become more frequent, and the world saw global bleaching events in 1998, 2010, 2014-17 and again from 2023, the most extensive yet, affecting reefs in the Gulf of Mannar and Lakshadweep as well.",
  "दोनों कथन सही हैं, और कथन-II कथन-I की व्याख्या करता है। प्रवालों को उनका रंग और अधिकांश भोजन ज़ूज़ैंथेली से मिलता है; लंबे ऊष्मा-तनाव में यह साझेदारी टूट जाती है, शैवाल बाहर निकाल दिए जाते हैं और सफ़ेद कंकाल दिखने लगता है। पानी समय रहते ठंडा हो जाए तो विरंजित प्रवाल उबर सकते हैं, पर बार-बार की घटनाएँ बहुत कम समय छोड़ती हैं। "
  "महासागरों का तापमान बढ़ने के साथ समुद्री ऊष्मा-लहरें बढ़ी हैं, और विश्व ने 1998, 2010, 2014-17 और फिर 2023 से वैश्विक विरंजन घटनाएँ देखीं, जिनमें अंतिम अब तक की सबसे व्यापक है और जिसने मन्नार की खाड़ी और लक्षद्वीप की भित्तियों को भी प्रभावित किया।",
  "NOAA Coral Reef Watch -- fourth global coral bleaching event (confirmed 2024); IPCC Special Report on the Ocean and Cryosphere (2019).",
  "env-coral-bleaching")

A(K, "hard",
  "Global warming is expected to make extreme rainfall events more intense.",
  "वैश्विक तापन से अत्यधिक वर्षा की घटनाओं के अधिक तीव्र होने की आशंका है।",
  "A warmer atmosphere can hold more water vapour -- about 7 per cent more for every 1 degree Celsius of warming.",
  "गर्म वायुमंडल अधिक जलवाष्प धारण कर सकता है: तापन के हर 1 डिग्री सेल्सियस पर लगभग 7 प्रतिशत अधिक।",
  2,
  "Only Statement II is correct, and it explains Statement I. By the Clausius-Clapeyron relation, the air's capacity to hold moisture rises by about 7 per cent per degree of warming, so when it rains heavily there is more water to fall; the IPCC finds that heavy rainfall has already intensified over most land areas, and India's cloudbursts and extreme monsoon spells fit that pattern. "
  "Statement III is wrong: warming increases evaporation from the oceans, which is part of why the hydrological cycle intensifies -- wetter extremes in some places and faster drying of soils in others.",
  "केवल कथन-II सही है, और यह कथन-I की व्याख्या करता है। क्लॉज़ियस-क्लैपेरॉन संबंध के अनुसार तापन के हर डिग्री पर हवा की नमी धारण करने की क्षमता लगभग 7 प्रतिशत बढ़ती है, इसलिए भारी वर्षा होने पर गिरने के लिए अधिक पानी होता है; IPCC के अनुसार अधिकांश स्थलीय क्षेत्रों में भारी वर्षा पहले ही तीव्र हो चुकी है, और भारत के बादल फटने तथा अत्यधिक मानसूनी दौर इसी पैटर्न में आते हैं। "
  "कथन-III गलत है: तापन महासागरों से वाष्पीकरण बढ़ाता है, और यही जल-चक्र के तीव्र होने का एक कारण है: कहीं अधिक गीली चरम घटनाएँ और कहीं मिट्टी का तेज़ी से सूखना।",
  f"{AR6} (heavy precipitation, section A.3 and B.3); IPCC AR6 WG I, Chapter 8 (water cycle changes).",
  "env-warming-extreme-rainfall",
  s3="Warming reduces evaporation from the oceans.",
  s3_hi="तापन महासागरों से वाष्पीकरण घटाता है।")

# ---------------------------------------------------------------- pairs (1, medium)
P(K, "medium", "Consider the following pairs of terms and their meanings:",
  "शब्दों और उनके अर्थों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Carbon sequestration : Long-term storage of carbon in plants, soils, oceans or rock",
   "Climate adaptation : Cutting greenhouse gas emissions to limit warming",
   "Carbon intensity : Total greenhouse gas emissions of a country in a year",
   "Carbon leakage : Shift of emissions to countries with weaker climate rules"],
  ["कार्बन प्रच्छादन (sequestration) : पौधों, मिट्टी, महासागरों या चट्टानों में कार्बन का दीर्घकालिक भंडारण",
   "जलवायु अनुकूलन (adaptation) : तापन सीमित करने के लिए ग्रीनहाउस गैस उत्सर्जन घटाना",
   "कार्बन तीव्रता (carbon intensity) : किसी देश का एक वर्ष का कुल ग्रीनहाउस गैस उत्सर्जन",
   "कार्बन रिसाव (carbon leakage) : कमज़ोर जलवायु नियमों वाले देशों की ओर उत्सर्जन का खिसकना"],
  1,
  "Only pairs 1 and 4 are correct. Carbon leakage is the worry that if one country prices carbon heavily, production and its emissions move to countries with weaker rules -- the stated reason for the EU's carbon border adjustment. "
  "Pair 2 describes mitigation; adaptation means adjusting to the effects of climate change, such as heat-tolerant crop varieties, early-warning systems or higher embankments. Pair 3 describes total emissions; carbon (emissions) intensity is emissions per unit of GDP, the measure in which India states its NDC target, so a country's intensity can fall while its total emissions still rise.",
  "केवल युग्म 1 और 4 सही हैं। कार्बन रिसाव वह चिंता है कि यदि एक देश कार्बन पर भारी कीमत लगाए, तो उत्पादन और उसके उत्सर्जन कमज़ोर नियमों वाले देशों में चले जाएँ; यूरोपीय संघ के कार्बन सीमा समायोजन का घोषित कारण यही है। "
  "युग्म 2 शमन (mitigation) का वर्णन है; अनुकूलन का अर्थ जलवायु परिवर्तन के प्रभावों के साथ तालमेल बिठाना है, जैसे गर्मी सहने वाली फ़सल-किस्में, पूर्व-चेतावनी प्रणालियाँ या ऊँचे तटबंध। युग्म 3 कुल उत्सर्जन का वर्णन है; कार्बन (उत्सर्जन) तीव्रता प्रति इकाई GDP उत्सर्जन है, वही माप जिसमें भारत अपना NDC लक्ष्य बताता है, इसलिए किसी देश की तीव्रता घटते हुए भी उसका कुल उत्सर्जन बढ़ सकता है।",
  "IPCC AR6 Glossary (adaptation, mitigation, sequestration, carbon leakage); India's Nationally Determined Contribution (2031-2035).",
  "env-climate-terms-pairs")

if __name__ == "__main__":
    write("env_l2_t10_climate_science.sql")
