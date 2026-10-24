# -*- coding: utf-8 -*-
"""Level 3 · Test 6 (GS Integrated Test 6) -- part D: Geography (10) (upsc_l3_cell_targets.mjs 6).
Same cell plan as Tests 1-5.
Every fact was searched in the whole UPSC bank (l3_tools/bank_find.py) and is one no row tests: India's dependence
on imported potash; the Samruddhi, Purvanchal, Bundelkhand and Ganga expressways; why hurricanes are rare in the
South Atlantic; the Saffir-Simpson scale, the IMD's cyclone classes and medicanes; Ladakh's diurnal range; the IMD's
cold-wave and cold-day criteria; the Suwalki Gap; Preah Vihear, the 2025 Cambodia-Thailand clashes, the Spratly and
Paracel Islands; Mullaperiyar, the Mahanadi tribunal and the Cauvery Water Management Authority; the Mohs scale.
MCQ keys are pinned."""
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
IMD = "India Meteorological Department"

# ---------------------------------------------------------------- Resources (e-SI)
A("Resources: Minerals, Energy & Agriculture", "easy",
  "India meets almost all its requirement of potash fertiliser through imports.",
  "भारत पोटाश उर्वरक की अपनी लगभग पूरी आवश्यकता आयात से पूरी करता है।",
  "India has no deposits of potash that are being mined commercially at present.",
  "भारत में इस समय पोटाश के ऐसे कोई निक्षेप नहीं हैं जिनका व्यावसायिक खनन हो रहा हो।",
  0,
  "Both statements are correct and Statement II explains Statement I. Potassium is one of the three main plant nutrients, and India's farms use several million tonnes of muriate of potash a year, all of it bought from countries such as Canada, Belarus, Russia, Israel and Jordan; this leaves fertiliser supply and subsidy costs exposed to world prices and to sanctions and freight shocks. "
  "Potash and polyhalite deposits identified in the Nagaur-Ganganagar basin of Rajasthan are now being explored and offered for mining, but none is yet in commercial production. Meanwhile, the long-standing subsidy bias in favour of urea has contributed to an imbalance in the use of nitrogen, phosphorus and potassium, which is why soil health cards recommend crop- and soil-specific doses.",
  "दोनों कथन सही हैं और कथन II, कथन I की व्याख्या करता है। पोटैशियम पौधों के तीन मुख्य पोषक तत्वों में से एक है, और भारत के खेत हर वर्ष कई लाख टन म्यूरिएट ऑफ़ पोटाश का उपयोग करते हैं, जो सारा कनाडा, बेलारूस, रूस, इज़राइल और जॉर्डन जैसे देशों से ख़रीदा जाता है; इससे उर्वरक आपूर्ति और सब्सिडी लागत विश्व क़ीमतों तथा प्रतिबंधों और भाड़े के झटकों के प्रति संवेदनशील रहती है। "
  "राजस्थान के नागौर-गंगानगर बेसिन में पहचाने गए पोटाश और पॉलीहैलाइट निक्षेपों का अब अन्वेषण हो रहा है और उन्हें खनन के लिए प्रस्तुत किया जा रहा है, पर कोई भी अभी व्यावसायिक उत्पादन में नहीं है। इस बीच, यूरिया के पक्ष में लंबे समय से चली आ रही सब्सिडी ने नाइट्रोजन, फ़ॉस्फ़ोरस और पोटैशियम के उपयोग में असंतुलन बढ़ाया है, इसीलिए मृदा स्वास्थ्य कार्ड फ़सल और मिट्टी के अनुसार मात्राएँ सुझाते हैं।",
  IPEc + "; Department of Fertilizers; Geological Survey of India.", "l3-t6-geo-potash-import-dependence", craft="linkage")

# ---------------------------------------------------------------- Transport, Ports & Human Geography (e-pairs)
P("Transport, Ports & Human Geography", "easy", "Consider the following pairs of expressways and the places they connect:",
  "एक्सप्रेसवे और उनसे जुड़ने वाले स्थानों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Samruddhi Mahamarg : Mumbai and Nagpur", "Purvanchal Expressway : Lucknow and Ghazipur",
   "Bundelkhand Expressway : Chitrakoot and Etawah", "Ganga Expressway : Delhi and Kolkata"],
  ["समृद्धि महामार्ग : मुंबई और नागपुर", "पूर्वांचल एक्सप्रेसवे : लखनऊ और ग़ाज़ीपुर",
   "बुंदेलखंड एक्सप्रेसवे : चित्रकूट और इटावा", "गंगा एक्सप्रेसवे : दिल्ली और कोलकाता"],
  2,
  "The first three pairs are correct. Maharashtra's Samruddhi Mahamarg, about 700 km long, links the State capital with Nagpur through the drought-prone districts of Vidarbha and Marathwada, with industrial nodes planned along it. Uttar Pradesh's Purvanchal Expressway runs from Lucknow to Ghazipur in the east, and the Bundelkhand Expressway from Chitrakoot to the Agra-Lucknow Expressway near Etawah, both meant to draw investment into poorer regions of the State. "
  "The fourth pair is wrong: the Ganga Expressway runs within Uttar Pradesh, from Meerut to Prayagraj, roughly parallel to the river. Such access-controlled highways cut travel time sharply, but their benefits depend on the industrial corridors and logistics hubs built around them.",
  "पहले तीन युग्म सही हैं। लगभग 700 किलोमीटर लंबा महाराष्ट्र का समृद्धि महामार्ग राज्य की राजधानी को विदर्भ और मराठवाड़ा के सूखा-प्रवण ज़िलों से होकर नागपुर से जोड़ता है, जिसके साथ औद्योगिक केंद्र प्रस्तावित हैं। उत्तर प्रदेश का पूर्वांचल एक्सप्रेसवे लखनऊ से पूर्व में ग़ाज़ीपुर तक, और बुंदेलखंड एक्सप्रेसवे चित्रकूट से इटावा के पास आगरा-लखनऊ एक्सप्रेसवे तक जाता है; दोनों का उद्देश्य राज्य के पिछड़े क्षेत्रों में निवेश लाना है। "
  "चौथा युग्म ग़लत है: गंगा एक्सप्रेसवे उत्तर प्रदेश के भीतर, मेरठ से प्रयागराज तक, नदी के लगभग समांतर चलता है। ऐसे पहुँच-नियंत्रित राजमार्ग यात्रा-समय को बहुत घटाते हैं, पर उनका लाभ उनके चारों ओर बने औद्योगिक गलियारों और लॉजिस्टिक केंद्रों पर निर्भर करता है।",
  "Maharashtra State Road Development Corporation; Uttar Pradesh Expressways Industrial Development Authority; Ministry of Road Transport and Highways.",
  "l3-t6-geo-expressways-samruddhi-purvanchal-bundelkhand-ganga", craft="recall")

# ---------------------------------------------------------------- Climatology & Biomes (h-MCQ, m-stmt)
M("Climatology & Biomes", "hard",
  "Tropical cyclones are rare in the South Atlantic Ocean, unlike the North Atlantic, mainly because:",
  "उत्तरी अटलांटिक के विपरीत दक्षिणी अटलांटिक महासागर में उष्णकटिबंधीय चक्रवात मुख्यतः क्यों दुर्लभ हैं?",
  ["the Coriolis force does not act on winds south of the equator",
   "the cold Benguela Current flows westward across the whole width of the ocean",
   "the ocean there is too deep for warm surface water to collect",
   "its waters are relatively cool and the vertical wind shear over it is strong"],
  ["भूमध्यरेखा के दक्षिण में पवनों पर कोरियोलिस बल कार्य नहीं करता",
   "ठंडी बेंगुएला धारा पूरे महासागर की चौड़ाई में पश्चिम की ओर बहती है",
   "वहाँ महासागर इतना गहरा है कि गर्म सतही जल जमा नहीं हो पाता",
   "उसका जल अपेक्षाकृत ठंडा और ऊपर पवन-अपरूपण प्रबल है"],
  3,
  "A tropical cyclone needs sea-surface temperatures of about 26-27 deg C or more over a deep layer, weak vertical wind shear so that the developing storm is not torn apart, and a pre-existing disturbance at least five degrees or so from the equator. Over most of the South Atlantic the water is cooler, the upper-level winds shear strongly, and the Inter-Tropical Convergence Zone rarely moves south of the equator there, so the seed disturbances are missing. "
  "The exception proves the rule: Cyclone Catarina struck southern Brazil in 2004, the first recorded hurricane in the basin. The Coriolis force acts in both hemispheres (it is zero only at the equator), the Benguela Current is confined to the African coast, and depth is not the limiting factor.",
  "उष्णकटिबंधीय चक्रवात को गहरी परत पर लगभग 26-27 डिग्री सेल्सियस या अधिक का समुद्री सतह तापमान, कमज़ोर ऊर्ध्वाधर पवन-अपरूपण ताकि बनता हुआ तूफ़ान बिखर न जाए, और भूमध्यरेखा से कम से कम लगभग पाँच डिग्री दूर एक पहले से मौजूद विक्षोभ चाहिए। दक्षिणी अटलांटिक के अधिकांश भाग पर जल ठंडा है, ऊपरी स्तर की पवनें प्रबल अपरूपण करती हैं, और अंतर-उष्णकटिबंधीय अभिसरण क्षेत्र वहाँ शायद ही भूमध्यरेखा के दक्षिण जाता है, इसलिए आरंभिक विक्षोभ नहीं बनते। "
  "अपवाद नियम की पुष्टि करता है: चक्रवात कैटरीना 2004 में दक्षिणी ब्राज़ील से टकराया, इस बेसिन में दर्ज पहला हरिकेन। कोरियोलिस बल दोनों गोलार्धों में कार्य करता है (यह केवल भूमध्यरेखा पर शून्य है), बेंगुएला धारा अफ़्रीकी तट तक सीमित है, और गहराई सीमित करने वाला कारक नहीं है।",
  FPG + ", 'Atmospheric Circulation and Weather Systems'; World Meteorological Organization.", "l3-t6-geo-south-atlantic-cyclones-rare", pos=3, craft="inference")

S("Climatology & Biomes", "medium", "With reference to the classification of cyclonic storms, consider the following statements:",
  "चक्रवाती तूफ़ानों के वर्गीकरण के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Saffir-Simpson scale grades hurricanes into five categories according to their maximum sustained wind speed.",
   "The highest class in the India Meteorological Department's classification is the 'super cyclonic storm'.",
   "Storm Daniel, which caused catastrophic floods in Libya in 2023, was a 'medicane', a cyclone with tropical characteristics over the Mediterranean."],
  ["सैफ़िर-सिम्पसन पैमाना हरिकेनों को उनकी अधिकतम निरंतर पवन गति के आधार पर पाँच श्रेणियों में बाँटता है।",
   "भारत मौसम विज्ञान विभाग के वर्गीकरण में सबसे ऊँचा वर्ग ‘सुपर चक्रवाती तूफ़ान’ है।",
   "2023 में लीबिया में विनाशकारी बाढ़ लाने वाला तूफ़ान डेनियल एक ‘मेडिकेन’ था, भूमध्यसागर पर उष्णकटिबंधीय विशेषताओं वाला चक्रवात।"],
  C3, 2,
  "All three are correct. The Saffir-Simpson scale runs from Category 1 to Category 5, the top category beginning at sustained winds of about 252 km/h, and is used for Atlantic and eastern Pacific hurricanes. The IMD, which is the regional centre for the north Indian Ocean, grades systems from depression and deep depression through cyclonic, severe, very severe and extremely severe cyclonic storms to the super cyclonic storm, with winds of 222 km/h or more -- the class reached by the Odisha cyclone of 1999 and by Amphan in 2020. "
  "Medicanes form over the warm Mediterranean in autumn and can develop an eye; Daniel's rain burst two dams above the city of Derna and killed thousands. Warmer seas are expected to make such storms more intense, which is why categories based on wind alone can understate the danger of flooding rain and storm surge.",
  "तीनों कथन सही हैं। सैफ़िर-सिम्पसन पैमाना श्रेणी 1 से श्रेणी 5 तक जाता है, सर्वोच्च श्रेणी लगभग 252 किमी/घंटा की निरंतर पवनों से शुरू होती है, और यह अटलांटिक तथा पूर्वी प्रशांत के हरिकेनों के लिए प्रयुक्त होता है। उत्तरी हिंद महासागर के क्षेत्रीय केंद्र आईएमडी प्रणालियों को अवदाब और गहन अवदाब से चक्रवाती, गंभीर, अति गंभीर और अत्यंत गंभीर चक्रवाती तूफ़ानों होते हुए 222 किमी/घंटा या अधिक पवनों वाले सुपर चक्रवाती तूफ़ान तक श्रेणीबद्ध करता है -- वह वर्ग जिस तक 1999 का ओडिशा चक्रवात और 2020 में अम्फान पहुँचे। "
  "मेडिकेन शरद ऋतु में गर्म भूमध्यसागर पर बनते हैं और उनमें आँख विकसित हो सकती है; डेनियल की वर्षा से डेर्ना नगर के ऊपर के दो बाँध टूट गए और हज़ारों लोग मारे गए। गर्म होते समुद्रों से ऐसे तूफ़ानों के अधिक तीव्र होने की अपेक्षा है, इसीलिए केवल पवन पर आधारित श्रेणियाँ बाढ़ लाने वाली वर्षा और तूफ़ानी लहरों के ख़तरे को कम करके आँक सकती हैं।",
  IMD + ", cyclone classification; World Meteorological Organization.", "l3-t6-geo-saffir-simpson-imd-medicane", craft="precision")

# ---------------------------------------------------------------- Indian Physiography, Climate & Regions (h-SI, m-stmt)
A("Indian Physiography, Climate & Regions", "hard",
  "Places in Ladakh, such as Leh, have a very large difference between day and night temperatures.",
  "लेह जैसे लद्दाख के स्थानों में दिन और रात के तापमान में बहुत बड़ा अंतर होता है।",
  "At high altitude the thin, dry air lets the ground heat up quickly under strong sunshine by day and lose its heat rapidly by radiation at night.",
  "अधिक ऊँचाई पर पतली, शुष्क हवा के कारण दिन में तेज़ धूप में भूमि जल्दी गर्म होती है और रात में विकिरण से तेज़ी से ऊष्मा खो देती है।",
  0,
  "Both statements are correct and Statement II explains Statement I. Water vapour and cloud are the atmosphere's blanket: they absorb incoming sunlight and, at night, trap the heat radiated by the ground. In the cold desert of Ladakh, at 3,000-4,000 metres and in the rain shadow of the Great Himalaya, the air is thin and dry and skies are usually clear, so the sun burns strongly by day while the ground cools fast after sunset -- a person can get sunburnt and frostbitten on the same day. "
  "The same principle explains why hot deserts such as the Thar also have large daily ranges, while humid coastal places such as Mumbai or Kochi have small ones, their moist air and the nearby sea moderating both heating and cooling.",
  "दोनों कथन सही हैं और कथन II, कथन I की व्याख्या करता है। जल-वाष्प और बादल वायुमंडल का कंबल हैं: वे आने वाली धूप को सोखते हैं और रात में भूमि द्वारा विकिरित ऊष्मा को रोकते हैं। 3,000-4,000 मीटर की ऊँचाई पर और महान हिमालय की वृष्टि-छाया में स्थित लद्दाख के शीत मरुस्थल में हवा पतली और शुष्क है और आकाश प्रायः साफ़ रहता है, इसलिए दिन में धूप तेज़ जलाती है जबकि सूर्यास्त के बाद भूमि जल्दी ठंडी होती है -- एक ही दिन में किसी को धूप से झुलसन और पाला-दंश दोनों हो सकते हैं। "
  "यही सिद्धांत बताता है कि थार जैसे गर्म मरुस्थलों में भी दैनिक तापांतर बड़ा क्यों होता है, जबकि मुंबई या कोच्चि जैसे आर्द्र तटीय स्थानों में छोटा, जहाँ नम हवा और पास का समुद्र गर्म होने और ठंडा होने दोनों को संयमित करते हैं।",
  IPE + ", 'Climate'; " + FPG + ".", "l3-t6-geo-ladakh-diurnal-range", craft="inference")

S("Indian Physiography, Climate & Regions", "medium", "With reference to cold waves in India, consider the following statements:",
  "भारत में शीत लहर के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["In the plains, the India Meteorological Department can declare a cold wave when the minimum temperature falls to 4 deg C or below, even without a large departure from normal.",
   "A 'cold day' is defined with reference to the daytime maximum temperature, which stays well below normal, and not only the night minimum.",
   "Cold waves over north India are caused mainly by moist easterly winds from the Bay of Bengal."],
  ["मैदानों में, न्यूनतम तापमान 4 डिग्री सेल्सियस या उससे नीचे जाने पर भारत मौसम विज्ञान विभाग शीत लहर घोषित कर सकता है, भले ही सामान्य से बड़ा विचलन न हो।",
   "‘ठंडा दिन’ दिन के अधिकतम तापमान के संदर्भ में परिभाषित है, जो सामान्य से काफ़ी नीचे रहता है, केवल रात के न्यूनतम तापमान से नहीं।",
   "उत्तर भारत में शीत लहरें मुख्यतः बंगाल की खाड़ी से आने वाली नम पूर्वी पवनों के कारण होती हैं।"],
  C3, 1,
  "Statements 1 and 2 are correct. The IMD's criteria combine an absolute and a relative test: in the plains a cold wave is declared when the minimum is 10 deg C or less and 4.5 deg C or more below normal, or when the minimum itself falls to 4 deg C or lower, with 'severe' grades below that. A cold day is one when the minimum is 10 deg C or less and the maximum is at least 4.5 deg C below normal -- typical of long spells of fog or low cloud over the Indo-Gangetic plain, when the sun barely warms the ground. "
  "Statement 3 is wrong: north Indian cold waves usually follow the passage of western disturbances, when cold, dry north-westerly winds blow in from the snow-covered Himalaya and Central Asia, and clear skies allow strong night-time cooling; they are a serious health risk for the elderly and the homeless and damage crops such as mustard and vegetables through frost.",
  "कथन 1 और 2 सही हैं। आईएमडी के मानदंड निरपेक्ष और सापेक्ष दोनों परख जोड़ते हैं: मैदानों में शीत लहर तब घोषित होती है जब न्यूनतम तापमान 10 डिग्री या कम हो और सामान्य से 4.5 डिग्री या अधिक नीचे हो, या जब न्यूनतम स्वयं 4 डिग्री या उससे नीचे गिर जाए, और इससे नीचे ‘गंभीर’ श्रेणियाँ हैं। ठंडा दिन वह है जब न्यूनतम 10 डिग्री या कम हो और अधिकतम सामान्य से कम से कम 4.5 डिग्री नीचे हो -- सिंधु-गंगा मैदान पर कोहरे या नीचे बादलों के लंबे दौर में आम, जब धूप भूमि को मुश्किल से गर्म करती है। "
  "कथन 3 ग़लत है: उत्तर भारत की शीत लहरें प्रायः पश्चिमी विक्षोभों के गुज़रने के बाद आती हैं, जब हिमाच्छादित हिमालय और मध्य एशिया से ठंडी, शुष्क उत्तर-पश्चिमी पवनें आती हैं और साफ़ आकाश रात में तीव्र शीतलन होने देता है; ये बुज़ुर्गों और बेघर लोगों के लिए गंभीर स्वास्थ्य जोखिम हैं और पाले से सरसों और सब्ज़ियों जैसी फ़सलों को हानि पहुँचाती हैं।",
  IMD + ", criteria for cold wave and cold day; National Disaster Management Authority, cold wave guidelines.",
  "l3-t6-geo-cold-wave-cold-day-criteria", craft="precision")

# ---------------------------------------------------------------- World Regions, Water Bodies & Places (m-MCQ, m-stmt)
M("World Regions, Water Bodies & Places", "medium",
  "The Suwalki Gap, a short stretch of the border between Poland and Lithuania often described as a weak point in NATO's defences, separates Belarus from:",
  "पोलैंड और लिथुआनिया की सीमा का छोटा हिस्सा सुवाल्की गैप, जिसे प्रायः नाटो की रक्षा का कमज़ोर बिंदु कहा जाता है, बेलारूस को किससे अलग करता है?",
  ["Transnistria", "Crimea", "Moldova", "Kaliningrad"],
  ["ट्रांसनिस्ट्रिया", "क्रीमिया", "मोल्दोवा", "कालिनिनग्राद"],
  3,
  "Kaliningrad is a Russian exclave on the Baltic Sea, cut off from the rest of Russia since the Soviet Union broke up, wedged between Poland and Lithuania. The roughly 65-100 km of Polish-Lithuanian border between it and Belarus, Russia's close ally, is the only land link between the Baltic States and the rest of NATO and the EU; military planners worry that seizing it could cut off Estonia, Latvia and Lithuania, which is why NATO has stationed forces in the region since 2014 and especially since 2022. "
  "The other options lie to the south: Transnistria is a Russian-backed breakaway strip of Moldova on the Dniester, and Crimea is the Black Sea peninsula annexed by Russia in 2014.",
  "कालिनिनग्राद बाल्टिक सागर पर एक रूसी अंतःक्षेत्र है, जो सोवियत संघ के विघटन के बाद से शेष रूस से कटा हुआ, पोलैंड और लिथुआनिया के बीच दबा है। इसके और रूस के घनिष्ठ सहयोगी बेलारूस के बीच पोलैंड-लिथुआनिया सीमा का लगभग 65-100 किलोमीटर हिस्सा बाल्टिक देशों और शेष नाटो तथा यूरोपीय संघ के बीच एकमात्र स्थल संपर्क है; सैन्य योजनाकारों को चिंता है कि इस पर कब्ज़ा एस्टोनिया, लातविया और लिथुआनिया को काट सकता है, इसीलिए नाटो ने 2014 से और विशेषकर 2022 से क्षेत्र में सेनाएँ तैनात की हैं। "
  "अन्य विकल्प दक्षिण में हैं: ट्रांसनिस्ट्रिया डनिस्टर नदी पर मोल्दोवा की रूस-समर्थित अलग हुई पट्टी है, और क्रीमिया 2014 में रूस द्वारा मिलाया गया काला सागर का प्रायद्वीप है।",
  FHG + "; Ministry of External Affairs, briefings on Europe.", "l3-t6-geo-suwalki-gap-kaliningrad", pos=3, craft="application")

S("World Regions, Water Bodies & Places", "medium", "With reference to territorial disputes in South-East Asia, consider the following statements:",
  "दक्षिण-पूर्व एशिया के क्षेत्रीय विवादों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["The International Court of Justice held in 1962 that the temple of Preah Vihear lies in territory under the sovereignty of Cambodia.",
   "Cambodia and Thailand fought armed clashes along their border in 2025.",
   "The Spratly Islands are claimed wholly or in part by China, Vietnam, the Philippines, Malaysia and Brunei.",
   "The Paracel Islands are held by China and claimed by Vietnam."],
  ["अंतरराष्ट्रीय न्यायालय ने 1962 में माना कि प्रेह विहेयर मंदिर कंबोडिया की संप्रभुता वाले क्षेत्र में है।",
   "कंबोडिया और थाईलैंड के बीच 2025 में उनकी सीमा पर सशस्त्र झड़पें हुईं।",
   "स्प्रैटली द्वीपों पर पूर्ण या आंशिक रूप से चीन, वियतनाम, फ़िलीपींस, मलेशिया और ब्रुनेई दावा करते हैं।",
   "पैरासेल द्वीप चीन के कब्ज़े में हैं और उन पर वियतनाम दावा करता है।"],
  C4, 3,
  "All four are correct. The eleventh-century Khmer temple of Preah Vihear stands on a cliff of the Dangrek range; the ICJ awarded it to Cambodia in 1962 on the basis of a French colonial map that Thailand had long accepted, and in 2013 it clarified that the whole promontory belongs to Cambodia. Its listing as a World Heritage Site in 2008 revived tension, and in July 2025 the two countries fought their deadliest clashes in years before a ceasefire mediated with Malaysia's help. "
  "In the South China Sea, the Spratlys -- scores of reefs and islets, several turned into bases by land reclamation -- are claimed by China and Taiwan in full and by Vietnam, the Philippines, Malaysia and Brunei in part, while China has held the Paracels since seizing them from South Vietnam in 1974. The disputes matter to India because about half its trade passes through these waters and because Indian companies explore for oil off Vietnam.",
  "चारों कथन सही हैं। ग्यारहवीं शताब्दी का ख़्मेर मंदिर प्रेह विहेयर डांगरेक श्रेणी की एक चट्टान पर है; अंतरराष्ट्रीय न्यायालय ने 1962 में इसे एक फ़्रांसीसी औपनिवेशिक मानचित्र के आधार पर कंबोडिया को दिया, जिसे थाईलैंड ने लंबे समय तक स्वीकार किया था, और 2013 में स्पष्ट किया कि पूरा अग्रभाग कंबोडिया का है। 2008 में विश्व धरोहर स्थल बनने से तनाव फिर उभरा, और जुलाई 2025 में दोनों देशों के बीच वर्षों की सबसे घातक झड़पें हुईं, जिसके बाद मलेशिया की सहायता से युद्धविराम हुआ। "
  "दक्षिण चीन सागर में स्प्रैटली -- दर्जनों प्रवाल-भित्तियाँ और छोटे द्वीप, जिनमें से कई भूमि-उद्धार से अड्डे बना दिए गए हैं -- पर चीन और ताइवान पूर्ण रूप से तथा वियतनाम, फ़िलीपींस, मलेशिया और ब्रुनेई आंशिक रूप से दावा करते हैं, जबकि चीन 1974 में दक्षिण वियतनाम से छीनने के बाद से पैरासेल पर काबिज़ है। ये विवाद भारत के लिए महत्वपूर्ण हैं क्योंकि उसके व्यापार का लगभग आधा इन्हीं जलक्षेत्रों से गुज़रता है और भारतीय कंपनियाँ वियतनाम के पास तेल की खोज करती हैं।",
  "International Court of Justice, Temple of Preah Vihear (Cambodia v. Thailand), 1962 and 2013; " + FHG + ".",
  "l3-t6-geo-preah-vihear-spratly-paracel", craft="precision")

# ---------------------------------------------------------------- Indian Rivers, Lakes & Wetlands (m-stmt)
S("Indian Rivers, Lakes & Wetlands", "medium", "With reference to inter-State river issues in India, consider the following statements:",
  "भारत में अंतरराज्यीय नदी विषयों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Mullaperiyar dam, completed in 1895 on the Periyar in Kerala, is operated by Tamil Nadu and diverts water eastward to the Vaigai basin.",
   "The dispute between Odisha and Chhattisgarh over the waters of the Mahanadi was referred to a tribunal in 2018.",
   "The Cauvery Water Management Authority was set up by the Cauvery Water Disputes Tribunal when it was constituted in 1990."],
  ["1895 में केरल में पेरियार पर पूरा हुआ मुल्लापेरियार बाँध तमिलनाडु द्वारा संचालित है और पानी को पूर्व की ओर वैगई बेसिन में मोड़ता है।",
   "महानदी के जल पर ओडिशा और छत्तीसगढ़ के बीच का विवाद 2018 में एक अधिकरण को सौंपा गया।",
   "कावेरी जल प्रबंधन प्राधिकरण का गठन कावेरी जल विवाद अधिकरण ने 1990 में अपने गठन के समय किया था।"],
  C3, 1,
  "Statements 1 and 2 are correct. Mullaperiyar was built under an 1886 lease between the princely state of Travancore and the Madras Presidency; it lies in Kerala's Idukki district but feeds irrigation and drinking water in southern Tamil Nadu through a tunnel across the Western Ghats, and Kerala's fears about the safety of the old masonry dam have led to repeated litigation over the permitted water level. Odisha complained that upstream barrages in Chhattisgarh reduced flows into Hirakud, and the Mahanadi Water Disputes Tribunal was constituted in 2018. "
  "Statement 3 is wrong: the tribunal set up in 1990 gave its final award in 2007, and it was the Supreme Court's judgment of 2018, modifying the shares, that led the Union to frame the scheme creating the Cauvery Water Management Authority and its regulation committee to implement the allocations.",
  "कथन 1 और 2 सही हैं। मुल्लापेरियार त्रावणकोर रियासत और मद्रास प्रेसीडेंसी के बीच 1886 के पट्टे के अंतर्गत बना; यह केरल के इडुक्की ज़िले में है पर पश्चिमी घाट के पार एक सुरंग से दक्षिणी तमिलनाडु में सिंचाई और पेयजल देता है, और पुराने चिनाई वाले बाँध की सुरक्षा को लेकर केरल की आशंकाओं से अनुमत जल-स्तर पर बार-बार मुक़दमे हुए हैं। ओडिशा ने शिकायत की कि छत्तीसगढ़ में ऊपरी बैराजों ने हीराकुद में प्रवाह घटाया, और 2018 में महानदी जल विवाद अधिकरण का गठन हुआ। "
  "कथन 3 ग़लत है: 1990 में गठित अधिकरण ने 2007 में अपना अंतिम निर्णय दिया, और हिस्सों में संशोधन करने वाले सर्वोच्च न्यायालय के 2018 के निर्णय के बाद संघ ने वह योजना बनाई जिससे आवंटन लागू करने के लिए कावेरी जल प्रबंधन प्राधिकरण और उसकी विनियमन समिति बनी।",
  "Ministry of Jal Shakti, Inter-State River Water Disputes Tribunals; Supreme Court of India: State of Karnataka v. State of Tamil Nadu (2018); " + IPE + ".",
  "l3-t6-geo-mullaperiyar-mahanadi-cwma", craft="linkage")

# ---------------------------------------------------------------- Geomorphology & Earth's Interior (m-stmt)
S("Geomorphology & Earth's Interior", "medium", "With reference to the Mohs scale of mineral hardness, consider the following statements:",
  "खनिज कठोरता के मोह्स पैमाने के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["On the scale, talc is the softest mineral (1) and diamond the hardest (10).",
   "The scale is relative: diamond is many times harder than corundum (9), not just slightly harder.",
   "Quartz (7) can easily be scratched with a steel knife."],
  ["इस पैमाने पर टैल्क सबसे नरम खनिज (1) और हीरा सबसे कठोर (10) है।",
   "यह पैमाना सापेक्ष है: हीरा कोरंडम (9) से थोड़ा नहीं, कई गुना अधिक कठोर है।",
   "क्वार्ट्ज़ (7) को स्टील के चाकू से आसानी से खरोंचा जा सकता है।"],
  C3, 1,
  "Statements 1 and 2 are correct. Friedrich Mohs ranked ten reference minerals by which can scratch which -- talc, gypsum, calcite, fluorite, apatite, orthoclase feldspar, quartz, topaz, corundum and diamond -- so each number says only that a mineral scratches those below it. The steps are uneven: measured by indentation, diamond is about four times as hard as corundum, while the gap between talc and gypsum is tiny. "
  "Statement 3 is wrong: a steel knife has a hardness of about 5.5, so it cannot scratch quartz; instead quartz scratches steel and glass, which is one of the simplest field tests geologists use. Hardness, along with lustre, streak, cleavage and specific gravity, helps identify minerals, and it explains why quartz-rich sand survives as the main mineral of beaches and deserts.",
  "कथन 1 और 2 सही हैं। फ़्रेडरिक मोह्स ने दस संदर्भ खनिजों को इस आधार पर क्रम दिया कि कौन किसे खरोंच सकता है -- टैल्क, जिप्सम, कैल्साइट, फ़्लोराइट, एपेटाइट, ऑर्थोक्लेज़ फ़ेल्डस्पार, क्वार्ट्ज़, टोपाज़, कोरंडम और हीरा -- इसलिए हर अंक केवल यह बताता है कि कोई खनिज अपने से नीचे वालों को खरोंचता है। अंतराल असमान हैं: धँसाव से मापने पर हीरा कोरंडम से लगभग चार गुना कठोर है, जबकि टैल्क और जिप्सम का अंतर बहुत छोटा है। "
  "कथन 3 ग़लत है: स्टील के चाकू की कठोरता लगभग 5.5 है, इसलिए वह क्वार्ट्ज़ को नहीं खरोंच सकता; बल्कि क्वार्ट्ज़ स्टील और काँच को खरोंचता है, जो भूवैज्ञानिकों की सबसे सरल क्षेत्रीय परखों में से एक है। चमक, धारी, विदलन और विशिष्ट गुरुत्व के साथ कठोरता खनिजों की पहचान में मदद करती है, और बताती है कि क्वार्ट्ज़-प्रधान रेत तटों और मरुस्थलों के मुख्य खनिज के रूप में क्यों बची रहती है।",
  FPG + ", 'Minerals and Rocks'.", "l3-t6-geo-mohs-scale-hardness", craft="precision")

write("gs_l3_t6_d.sql")
