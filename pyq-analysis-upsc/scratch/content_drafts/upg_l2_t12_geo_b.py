# -*- coding: utf-8 -*-
"""Level 2 · Test 12 (Geography 1) -- depth audit of 2026-10-04, part B: World Regions, Water Bodies & Places,
and the craft tags for the 79 kept rows (docs/upsc-question-design-standard.md §6). Part A is
upg_l2_t12_geo_a.py.

Part B rewrites 11 recall rows in place with the same concept id, type and difficulty:
  - place facts now carry their cause: why Iceland widens, what bounds the Sargasso Sea, why the Amazon
    runs to the Atlantic, why Patagonia is dry and the Gobi rainless, why the Blue Nile dam alarms Egypt,
    why the Congo's flow is steady, and why Baikal and Tanganyika are so deep;
  - two 5-item judgements (the Tropic of Cancer's countries; which Mediterranean islands are Italian), and a
    near-miss version of the European seas.
Test 12 after both parts: analytic 44, precision 31, recall 30.
Leaks avoided while drafting:
  - temperature falling with height, or elevation making a place cold (answers the mountains-colder AR);
  - subduction feeding volcanoes (states the Himalaya-no-volcanoes AR's Statement II);
  - India's collision with Asia raising Tibet (also part of that AR);
  - rivers lowering sea salinity (answers the salinity row's statement 3), so the Red Sea row was left;
  - the Bosporus as Azov's outlet (the straits pairs would answer it)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write_updates, CODE
from polity_common import C3, C4, T2

d.SUBJECT = "Geography"
d.REQUIRE_CRAFT = True
WR = "World Regions, Water Bodies & Places"
NC11 = "NCERT Class XI, Fundamentals of Physical Geography"
NC7 = "NCERT Class VII, Our Environment"
FIVE = ["Only two", "Only three", "Only four", "All five"]
FIVE_HI = ["केवल दो", "केवल तीन", "केवल चार", "सभी पाँच"]

# ================================================================ MCQs (2)
M(WR, "hard", "Iceland has many active volcanoes, and the island is slowly widening, its two halves moving apart by about 2 cm a year. This is mainly because Iceland lies:",
  "आइसलैंड में कई सक्रिय ज्वालामुखी हैं, और यह द्वीप धीरे-धीरे चौड़ा हो रहा है, इसके दोनों भाग प्रति वर्ष लगभग 2 सेमी दूर हो रहे हैं। इसका मुख्य कारण यह है कि आइसलैंड स्थित है:",
  ["on a mid-ocean ridge, where the North American and Eurasian plates are moving apart",
   "above a subduction zone, where the floor of the Atlantic Ocean is sinking beneath Europe",
   "on a transform fault, where two plates slide past each other without moving apart at all",
   "on an old fold-mountain belt that is still being pushed up by two plates colliding"],
  ["एक मध्य-महासागरीय कटक पर, जहाँ उत्तर अमेरिकी और यूरेशियाई प्लेटें एक-दूसरे से दूर जा रही हैं",
   "एक अधोगमन क्षेत्र के ऊपर, जहाँ अटलांटिक महासागर का तल यूरोप के नीचे धँस रहा है",
   "एक रूपांतर भ्रंश पर, जहाँ दो प्लेटें बिल्कुल दूर गए बिना एक-दूसरे के पास से खिसकती हैं",
   "एक पुरानी वलित पर्वत-पट्टी पर, जिसे दो प्लेटों की टक्कर अब भी ऊपर धकेल रही है"],
  0,
  "Iceland is the part of the Mid-Atlantic Ridge that stands above the sea: the North American and Eurasian plates pull apart along it, magma wells up to fill the gap, and a hotspot beneath the island adds extra magma, which is why it has so many volcanoes, fissure eruptions and geysers. At Thingvellir the rift valley between the plates can be walked across. "
  "Subduction zones, transform faults and fold belts are other settings; none of them would make the island widen.",
  "आइसलैंड मध्य-अटलांटिक कटक का वह भाग है जो समुद्र से ऊपर है: उत्तर अमेरिकी और यूरेशियाई प्लेटें उसके साथ-साथ दूर होती हैं, खाली जगह भरने के लिए मैग्मा ऊपर आता है, और द्वीप के नीचे का एक तप्त स्थल (हॉटस्पॉट) अतिरिक्त मैग्मा जोड़ता है, इसीलिए वहाँ इतने ज्वालामुखी, दरारी उद्गार और गीज़र हैं। थिंगवेलीर में प्लेटों के बीच की भ्रंश घाटी को पैदल पार किया जा सकता है। "
  "अधोगमन क्षेत्र, रूपांतर भ्रंश और वलित पट्टियाँ अन्य परिस्थितियाँ हैं; इनमें से कोई भी द्वीप को चौड़ा नहीं करेगी।",
  NC11, "geo-mid-atlantic-ridge-iceland", craft="inference")

M(WR, "hard", "The Sargasso Sea in the North Atlantic has no coastline, and its warm, clear and calm water is covered with mats of floating seaweed. Both features follow mainly from the fact that it:",
  "उत्तरी अटलांटिक के सारगैसो सागर की कोई तटरेखा नहीं है, और इसका गर्म, स्वच्छ और शांत जल तैरती समुद्री शैवाल की परतों से ढका रहता है। ये दोनों विशेषताएँ मुख्यतः इस तथ्य से निकलती हैं कि यह:",
  ["sits inside a ring of ocean currents that bound it and keep its water circling",
   "lies under the doldrums near the Equator, where the winds are calm for most of the year",
   "is fed by several large rivers whose nutrients feed the seaweed and keep the water warm",
   "is enclosed by a long chain of submerged volcanic islands that shut out the ocean waves"],
  ["महासागरीय धाराओं के एक घेरे के भीतर है जो इसकी सीमा बनाती हैं और इसके जल को घुमाती रहती हैं",
   "भूमध्यरेखा के पास डोलड्रम के नीचे है, जहाँ वर्ष के अधिकांश भाग में हवाएँ शांत रहती हैं",
   "कई बड़ी नदियों से जल पाता है, जिनके पोषक तत्व शैवाल को पोषण देते हैं और जल को गर्म रखते हैं",
   "डूबे हुए ज्वालामुखीय द्वीपों की एक लंबी शृंखला से घिरा है जो महासागर की लहरों को रोकती है"],
  0,
  "The Sargasso Sea lies at the centre of the North Atlantic gyre: the Gulf Stream on the west, the North Atlantic Drift on the north, the Canary Current on the east and the North Equatorial Current on the south circle it clockwise, and it is these currents, not land, that mark its limits. "
  "Water inside the gyre turns slowly, so floating Sargassum weed collects there and the sea stays calm; with few nutrients, plankton are scarce and the water is unusually clear and blue. It lies at roughly 20-35 degrees north, not at the Equator, and no rivers reach it.",
  "सारगैसो सागर उत्तरी अटलांटिक के गायर (वलय) के केंद्र में है: पश्चिम में गल्फ़ स्ट्रीम, उत्तर में उत्तरी अटलांटिक प्रवाह, पूर्व में कैनरी धारा और दक्षिण में उत्तरी भूमध्यरेखीय धारा इसे दक्षिणावर्त घेरती हैं, और ये धाराएँ ही, भूमि नहीं, इसकी सीमाएँ बनाती हैं। "
  "वलय के भीतर का जल धीरे घूमता है, इसलिए तैरती सारगैसम शैवाल वहाँ जमा होती है और सागर शांत रहता है; पोषक तत्व कम होने से प्लवक कम हैं और जल असाधारण रूप से स्वच्छ और नीला है। यह लगभग 20-35 डिग्री उत्तर में है, भूमध्यरेखा पर नहीं, और कोई नदी इस तक नहीं पहुँचती।",
  NC11, "geo-sargasso-sea-no-coast", craft="linkage")

# ================================================================ statements (9)
S(WR, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Pacific is the largest of the oceans.",
   "Although the Amazon rises in the Andes less than 200 km from the Pacific, it flows east to the Atlantic, because the Andes block the way west."],
  ["प्रशांत सबसे बड़ा महासागर है।",
   "यद्यपि अमेज़न प्रशांत से 200 किमी से भी कम दूरी पर एंडीज़ में निकलती है, फिर भी यह पूर्व की ओर अटलांटिक में बहती है, क्योंकि एंडीज़ पश्चिम का रास्ता रोकते हैं।"],
  T2, 2,
  "Both statements are correct. The Pacific covers about a third of the Earth's surface, more than all the land put together. The Andes, raised along the western edge of South America, form the continent's main divide: the short, steep rivers on their western side drop straight to the Pacific, while the Amazon and its tributaries gather the rain falling on the eastern slopes and flow some 6,400 km across the lowlands of Brazil to the Atlantic, carrying about a fifth of all the fresh water that rivers deliver to the oceans.",
  "दोनों कथन सही हैं। प्रशांत पृथ्वी की सतह का लगभग एक-तिहाई भाग घेरता है, जो पूरी भूमि से अधिक है। दक्षिण अमेरिका के पश्चिमी किनारे पर उठे एंडीज़ महाद्वीप के मुख्य जल-विभाजक हैं: उनके पश्चिमी ओर की छोटी, तीव्र ढाल वाली नदियाँ सीधे प्रशांत में उतरती हैं, जबकि अमेज़न और उसकी सहायक नदियाँ पूर्वी ढलानों पर गिरने वाली वर्षा को समेटकर ब्राज़ील के निचले मैदानों से लगभग 6,400 किमी बहकर अटलांटिक में जाती हैं, और नदियों द्वारा महासागरों में पहुँचाए जाने वाले कुल मीठे पानी का लगभग पाँचवाँ भाग ले जाती हैं।",
  NC7, "geo-pacific-amazon-easy", craft="linkage")

S(WR, "hard", "Consider the following statements about plateaus:",
  "पठारों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Tibetan Plateau is an intermontane plateau, enclosed by mountain ranges such as the Himalaya and the Kunlun.",
   "The Patagonian plateau of Argentina is dry because it lies in the rain shadow of the Andes, which block the moist westerlies from the Pacific.",
   "The Altiplano is shared mainly by Chile and Argentina."],
  ["तिब्बती पठार एक अंतरापर्वतीय पठार है, जो हिमालय और कुनलुन जैसी पर्वत-श्रेणियों से घिरा है।",
   "अर्जेंटीना का पैटागोनिया पठार इसलिए शुष्क है कि यह एंडीज़ की वृष्टि-छाया में है, जो प्रशांत से आने वाली नम पछुआ हवाओं को रोकते हैं।",
   "आल्टिप्लानो मुख्यतः चिली और अर्जेंटीना में बँटा है।"],
  C3, 1,
  "Statements 1 and 2 are correct. An intermontane plateau is one ringed by mountains: the Tibetan Plateau, averaging over 4,500 m, is the highest and largest, walled by the Himalaya to the south and the Kunlun to the north, and is the source of the Indus, the Brahmaputra, the Yangtze and the Mekong. In the southern latitudes the westerlies bring heavy rain to southern Chile, but by the time they cross the Andes into Patagonia they have lost their moisture, leaving a cold, dry, windswept steppe. "
  "Statement 3 is wrong: the Altiplano, at about 3,700 m and holding Lake Titicaca, lies mainly in Bolivia and Peru, reaching only into the edges of Chile and Argentina.",
  "कथन 1 और 2 सही हैं। अंतरापर्वतीय पठार वह है जो पर्वतों से घिरा हो: औसतन 4,500 मीटर से ऊँचा तिब्बती पठार सबसे ऊँचा और सबसे बड़ा है, जिसके दक्षिण में हिमालय और उत्तर में कुनलुन की दीवारें हैं, और यह सिंधु, ब्रह्मपुत्र, यांग्त्सी और मेकांग का स्रोत है। दक्षिणी अक्षांशों में पछुआ हवाएँ दक्षिणी चिली में भारी वर्षा लाती हैं, पर एंडीज़ पार करके पैटागोनिया पहुँचते-पहुँचते उनकी नमी ख़त्म हो जाती है, जिससे एक ठंडा, शुष्क, हवा से उजड़ा स्टेपी बचता है। "
  "कथन 3 गलत है: लगभग 3,700 मीटर ऊँचा और टिटिकाका झील वाला आल्टिप्लानो मुख्यतः बोलीविया और पेरू में है, और केवल चिली और अर्जेंटीना के किनारों तक पहुँचता है।",
  NC11, "geo-plateaus-tibet-patagonia-altiplano", craft="linkage")

S(WR, "hard", "Consider the following statements about dams:",
  "बाँधों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Egypt and Sudan fear the effect of the Grand Ethiopian Renaissance Dam because it stands on the Blue Nile, which supplies most of the Nile's water.",
   "The Three Gorges Dam is on the Yellow River (Huang He).",
   "The Kariba Dam is on the Limpopo."],
  ["मिस्र और सूडान ग्रैंड इथियोपियन रेनेसाँ बाँध के प्रभाव से इसलिए चिंतित हैं कि यह नीली नील पर है, जो नील के अधिकांश जल की आपूर्ति करती है।",
   "थ्री गॉर्जेस बाँध पीली नदी (ह्वांग हो) पर है।",
   "करीबा बाँध लिम्पोपो पर है।"],
  C3, 0,
  "Only statement 1 is correct. Rising in Lake Tana in the Ethiopian highlands, the Blue Nile carries Ethiopia's monsoon rains and provides well over half of the water of the main Nile, far more than the White Nile from Lake Victoria; so a dam on it, Africa's largest hydroelectric project, gives Ethiopia a say over the flow on which almost rainless Egypt depends. "
  "Statement 2 is wrong: the Three Gorges Dam, the world's largest power station by capacity, is on the Yangtze (Chang Jiang) in Hubei. Statement 3 is wrong: the Kariba Dam is on the Zambezi, on the border of Zambia and Zimbabwe.",
  "केवल कथन 1 सही है। इथियोपियाई उच्चभूमि की ताना झील से निकलने वाली नीली नील इथियोपिया की मानसूनी वर्षा को ले जाती है और मुख्य नील के आधे से कहीं अधिक जल की आपूर्ति करती है, जो विक्टोरिया झील से आने वाली श्वेत नील से बहुत अधिक है; इसलिए उस पर बना बाँध, अफ़्रीका की सबसे बड़ी जलविद्युत परियोजना, इथियोपिया को उस प्रवाह पर प्रभाव देता है जिस पर लगभग वर्षाहीन मिस्र निर्भर है। "
  "कथन 2 गलत है: क्षमता के आधार पर संसार का सबसे बड़ा बिजलीघर थ्री गॉर्जेस बाँध हुबेई में यांग्त्सी (चांग जियांग) पर है। कथन 3 गलत है: करीबा बाँध ज़ाम्बिया और ज़िम्बाब्वे की सीमा पर ज़ाम्बेज़ी पर है।",
  NC11, "geo-world-dams-gerd-three-gorges-kariba", craft="linkage")

S(WR, "medium", "Consider the following statements about rivers of Africa:",
  "अफ़्रीका की नदियों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Nile flows northwards into the Mediterranean Sea.",
   "Because the Congo crosses the Equator twice, some part of its basin is always in a rainy season, so its flow stays high all through the year.",
   "The Zambezi flows into the Indian Ocean, and the Victoria Falls lie on it."],
  ["नील उत्तर की ओर बहकर भूमध्य सागर में मिलती है।",
   "चूँकि कांगो भूमध्यरेखा को दो बार पार करती है, इसलिए इसके बेसिन का कोई न कोई भाग सदा वर्षा ऋतु में रहता है, और इसका प्रवाह साल भर ऊँचा रहता है।",
   "ज़ाम्बेज़ी हिंद महासागर में गिरती है, और विक्टोरिया जलप्रपात इसी पर है।"],
  C3, 2,
  "All three are correct. The Nile flows north through Sudan and Egypt to a delta on the Mediterranean. The Congo first flows north across the Equator, then curves west and south-west and crosses it again; since the rainy seasons north and south of the Equator fall at different times of the year, one part of its huge basin is always wet, which gives it the steadiest flow of any great river and the second-largest discharge in the world after the Amazon. "
  "The Zambezi flows east to the Indian Ocean in Mozambique, plunging over the Victoria Falls on the Zambia-Zimbabwe border on the way.",
  "तीनों कथन सही हैं। नील सूडान और मिस्र से होकर उत्तर की ओर बहती है और भूमध्य सागर पर डेल्टा बनाती है। कांगो पहले उत्तर की ओर भूमध्यरेखा पार करती है, फिर पश्चिम और दक्षिण-पश्चिम की ओर मुड़कर उसे फिर पार करती है; चूँकि भूमध्यरेखा के उत्तर और दक्षिण की वर्षा ऋतुएँ वर्ष के अलग-अलग समय पड़ती हैं, इसलिए इसके विशाल बेसिन का कोई भाग सदा गीला रहता है, जिससे इसका प्रवाह किसी भी बड़ी नदी से अधिक स्थिर है और इसका जल-प्रवाह अमेज़न के बाद संसार में दूसरा सबसे बड़ा है। "
  "ज़ाम्बेज़ी पूर्व की ओर बहकर मोज़ाम्बिक में हिंद महासागर में गिरती है, और रास्ते में ज़ाम्बिया-ज़िम्बाब्वे सीमा पर विक्टोरिया जलप्रपात से नीचे गिरती है।",
  NC7, "geo-africa-rivers-nile-congo-zambezi", craft="linkage")

S(WR, "medium", "Consider the following statements about deserts:",
  "मरुस्थलों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Gobi gets little rain largely because the Himalaya and the Tibetan Plateau block the moist winds from the Indian Ocean.",
   "The Kalahari Desert lies mainly in Kenya.",
   "The Karakum Desert lies mainly in Iran."],
  ["गोबी में कम वर्षा का बड़ा कारण यह है कि हिमालय और तिब्बती पठार हिंद महासागर से आने वाली नम हवाओं को रोक देते हैं।",
   "कालाहारी मरुस्थल मुख्यतः केन्या में है।",
   "काराकुम मरुस्थल मुख्यतः ईरान में है।"],
  C3, 0,
  "Only statement 1 is correct. The Gobi, on the Mongolian plateau and in northern China, lies deep inside Asia, and the Himalaya and the Tibetan Plateau to its south-west stop the monsoon's moisture from reaching it, making it a rain-shadow desert with bitter winters. "
  "Statement 2 is wrong: the Kalahari, a semi-desert of red sand, covers most of Botswana and reaches into Namibia and South Africa. Statement 3 is wrong: the Karakum ('black sand') covers most of Turkmenistan.",
  "केवल कथन 1 सही है। मंगोलियाई पठार और उत्तरी चीन में फैला गोबी एशिया के भीतरी भाग में है, और उसके दक्षिण-पश्चिम में हिमालय और तिब्बती पठार मानसून की नमी को उस तक पहुँचने से रोकते हैं, जिससे यह कड़ी सर्दियों वाला वृष्टि-छाया मरुस्थल है। "
  "कथन 2 गलत है: लाल रेत का अर्ध-मरुस्थल कालाहारी बोत्सवाना के अधिकांश भाग में फैला है और नामीबिया तथा दक्षिण अफ़्रीका तक पहुँचता है। कथन 3 गलत है: काराकुम ('काली रेत') तुर्कमेनिस्तान के अधिकांश भाग में फैला है।",
  NC7, "geo-deserts-gobi-kalahari-karakum", craft="linkage")

S(WR, "medium", "Consider the following statements about lakes of the world:",
  "संसार की झीलों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Lake Baikal is the deepest lake in the world because it fills a rift in the Earth's crust that is still slowly widening.",
   "Lake Victoria is the largest lake in Africa by area.",
   "Lake Tanganyika, another rift lake, is the second-deepest lake in the world."],
  ["बैकाल झील संसार की सबसे गहरी झील है क्योंकि यह पृथ्वी की भूपर्पटी की उस दरार को भरती है जो अब भी धीरे-धीरे चौड़ी हो रही है।",
   "क्षेत्रफल के आधार पर विक्टोरिया झील अफ़्रीका की सबसे बड़ी झील है।",
   "एक और भ्रंश-झील, टांगानिका झील, संसार की दूसरी सबसे गहरी झील है।"],
  C3, 2,
  "All three are correct. Baikal in Siberia fills a rift where the crust is being pulled apart by a few millimetres a year; more than 1,600 m deep, with kilometres of sediment below its floor, it holds about a fifth of the world's unfrozen surface fresh water. "
  "Victoria, shared by Uganda, Kenya and Tanzania, is Africa's largest lake and the largest tropical lake; it lies in a shallow basin between the two arms of the East African Rift rather than in the rift itself. Tanganyika, in the rift's western arm, is about 1,470 m deep, second only to Baikal.",
  "तीनों कथन सही हैं। साइबेरिया की बैकाल उस दरार को भरती है जहाँ भूपर्पटी प्रति वर्ष कुछ मिलीमीटर खिंच रही है; 1,600 मीटर से अधिक गहरी और तल के नीचे किलोमीटरों मोटे अवसाद वाली यह झील संसार के जमे हुए न रहने वाले सतही मीठे पानी का लगभग पाँचवाँ भाग रखती है। "
  "युगांडा, केन्या और तंज़ानिया में बँटी विक्टोरिया अफ़्रीका की सबसे बड़ी और सबसे बड़ी उष्णकटिबंधीय झील है; यह स्वयं भ्रंश में नहीं, बल्कि पूर्वी अफ़्रीकी भ्रंश की दो भुजाओं के बीच एक उथले बेसिन में है। भ्रंश की पश्चिमी भुजा में स्थित टांगानिका लगभग 1,470 मीटर गहरी है, केवल बैकाल से कम।",
  NC11, "geo-world-lakes-baikal-victoria-titicaca", craft="linkage")

S(WR, "medium", "Consider the following countries:",
  "निम्नलिखित देशों पर विचार कीजिए:",
  ["Iran", "Pakistan", "Nepal", "Oman", "Myanmar"],
  ["ईरान", "पाकिस्तान", "नेपाल", "ओमान", "म्यांमार"],
  None, 0,
  "Only two -- Oman and Myanmar. Across Africa and Asia the Tropic of Cancer (about 23.4 degrees north) runs through Mauritania, Mali, Algeria, Niger, Libya, Egypt, Saudi Arabia, the UAE and Oman, and then India, Bangladesh, Myanmar, China and Taiwan. "
  "Iran's southern coast lies at about 25 degrees north and Pakistan's southernmost tip, near Sir Creek, lies just north of the line, so it misses both; Nepal lies well to the north, beyond India's Gangetic plain.",
  "केवल दो -- ओमान और म्यांमार। अफ़्रीका और एशिया में कर्क रेखा (लगभग 23.4 डिग्री उत्तर) मॉरिटानिया, माली, अल्जीरिया, नाइजर, लीबिया, मिस्र, सऊदी अरब, संयुक्त अरब अमीरात और ओमान से, फिर भारत, बांग्लादेश, म्यांमार, चीन और ताइवान से होकर गुज़रती है। "
  "ईरान का दक्षिणी तट लगभग 25 डिग्री उत्तर पर है और पाकिस्तान का सबसे दक्षिणी सिरा, सर क्रीक के पास, रेखा से थोड़ा उत्तर में है, इसलिए यह दोनों से नहीं गुज़रती; नेपाल भारत के गंगा मैदान से परे, बहुत उत्तर में है।",
  NC7, "geo-tropic-of-cancer-countries", opts=FIVE, opts_hi=FIVE_HI,
  closing="Through how many of the above countries does the Tropic of Cancer pass?", closing_hi="कर्क रेखा उपर्युक्त में से कितने देशों से होकर गुज़रती है?", craft="multi")

S(WR, "hard", "Consider the following islands of the Mediterranean Sea:",
  "भूमध्य सागर के निम्नलिखित द्वीपों पर विचार कीजिए:",
  ["Sicily", "Sardinia", "Corsica", "Malta", "Elba"],
  ["सिसिली", "सार्डिनिया", "कोर्सिका", "माल्टा", "एल्बा"],
  None, 1,
  "Only three -- Sicily, Sardinia and Elba. Sicily and Sardinia, the two largest islands of the Mediterranean, are regions of Italy, and Elba, off the coast of Tuscany, belongs to Italy too; it is remembered as Napoleon's first island of exile. "
  "Corsica is the trap: it lies just north of Sardinia and close to Italy, and its people speak a language close to Italian, but it has belonged to France since 1768. Malta, south of Sicily, is an independent republic and a member of the European Union.",
  "केवल तीन -- सिसिली, सार्डिनिया और एल्बा। भूमध्य सागर के दो सबसे बड़े द्वीप सिसिली और सार्डिनिया इटली के क्षेत्र हैं, और टस्कनी के तट से दूर एल्बा भी इटली का है; इसे नेपोलियन के निर्वासन के पहले द्वीप के रूप में याद किया जाता है। "
  "कोर्सिका जाल है: यह सार्डिनिया के ठीक उत्तर में और इटली के पास है, और इसके लोग इतालवी से मिलती-जुलती भाषा बोलते हैं, पर यह 1768 से फ़्रांस का भाग है। सिसिली के दक्षिण में माल्टा एक स्वतंत्र गणराज्य और यूरोपीय संघ का सदस्य है।",
  NC7, "geo-mediterranean-islands", opts=FIVE, opts_hi=FIVE_HI,
  closing="How many of the above are part of Italy?", closing_hi="उपर्युक्त में से कितने इटली के भाग हैं?", craft="multi")

S(WR, "medium", "Consider the following statements about seas of Europe:",
  "यूरोप के सागरों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Adriatic Sea lies between Italy and the Iberian Peninsula.",
   "The Aegean Sea lies between Greece and Italy.",
   "The Sea of Azov is connected to the Caspian Sea by the Kerch Strait."],
  ["एड्रियाटिक सागर इटली और इबेरियाई प्रायद्वीप के बीच है।",
   "ईजियन सागर यूनान और इटली के बीच है।",
   "आज़ोव सागर केर्च जलडमरूमध्य द्वारा कैस्पियन सागर से जुड़ा है।"],
  C3, 3,
  "None is correct. Statement 1 is wrong: the Adriatic lies between Italy and the Balkan Peninsula -- Slovenia, Croatia, Montenegro and Albania; between Italy and Spain lie the Tyrrhenian Sea, the Balearic Sea and the open western Mediterranean. "
  "Statement 2 is wrong: the island-dotted Aegean lies between Greece and Turkey; the sea between Greece and southern Italy is the Ionian. Statement 3 is wrong: the shallow Sea of Azov opens through the Kerch Strait into the Black Sea; the Caspian has no outlet to the ocean.",
  "कोई भी कथन सही नहीं है। कथन 1 गलत है: एड्रियाटिक इटली और बाल्कन प्रायद्वीप, यानी स्लोवेनिया, क्रोएशिया, मॉन्टेनेग्रो और अल्बानिया, के बीच है; इटली और स्पेन के बीच टिरेनियन सागर, बेलियरिक सागर और खुला पश्चिमी भूमध्य सागर है। "
  "कथन 2 गलत है: द्वीपों से भरा ईजियन यूनान और तुर्की के बीच है; यूनान और दक्षिणी इटली के बीच का सागर आयोनियन है। कथन 3 गलत है: उथला आज़ोव सागर केर्च जलडमरूमध्य से काला सागर में खुलता है; कैस्पियन का महासागर तक कोई निकास नहीं है।",
  NC7, "geo-europe-seas-adriatic-aegean-azov", craft="precision")

# ================================================================ TAGS for the 79 kept rows (Test 21's 5 are tagged already)
TAGS = {
 "geo-rainforest-evergreen-easy": "linkage", "geo-mediterranean-winter-rain": "linkage", "geo-blue-sky-scattering": "linkage",
 "geo-mountains-colder-heated-below": "linkage", "geo-roaring-forties": "linkage", "geo-seasons-tilt-not-distance": "linkage",
 "geo-vegetation-trees-pairs": "precision", "geo-climate-types-regions-pairs": "precision", "geo-anemometer-easy": "recall",
 "geo-precipitation-fog-easy": "precision", "geo-hottest-deserts-not-equator": "linkage", "geo-air-mass-mt": "application",
 "geo-atmosphere-argon": "recall", "geo-horse-latitudes": "recall", "ugeo-taiga-annual-range": "inference",
 "geo-deserts-tundra-easy": "recall", "geo-pressure-altitude-isotherm-easy": "recall", "geo-weather-insolation-easy": "precision",
 "geo-fronts-types": "precision", "geo-heat-budget-albedo": "precision", "geo-temperature-inversion": "linkage",
 "geo-tricellular-circulation": "precision", "geo-atmosphere-layers-tropopause": "precision", "geo-biomes-soils-leaf-fall": "linkage",
 "geo-coriolis-force-properties": "precision", "geo-humidity-dew-point": "inference", "geo-jet-streams-season": "precision",
 "geo-planetary-winds-direction": "precision", "geo-pressure-belts-thermal-dynamic": "precision", "geo-temperate-vs-tropical-cyclones": "precision",
 "geo-tropical-cyclones-energy-eye": "precision", "ugeo-local-winds": "recall",
 "geo-marble-metamorphic-easy": "recall", "geo-himalaya-no-volcanoes": "linkage", "geo-ring-of-fire-intraplate": "linkage",
 "geo-s-waves-outer-core": "inference", "geo-thinnest-layer-easy": "recall", "geo-block-mountain-black-forest": "recall",
 "geo-cirque-glacial-erosion": "precision", "geo-mantle-volume": "recall", "geo-mariana-trench-boundary": "recall",
 "geo-crust-core-composition-easy": "recall", "geo-continental-drift-wegener": "precision", "geo-earthquake-scales-focus": "precision",
 "geo-karst-landforms": "precision", "geo-oxbow-barchan-mushroom": "precision", "geo-plate-boundaries-examples": "precision",
 "geo-seismic-waves-types": "precision",
 "geo-west-coast-deserts-cold-currents": "linkage", "geo-gulf-stream-origin": "recall", "geo-tides-spring-neap-easy": "precision",
 "geo-el-nino-la-nina": "precision", "geo-ocean-salinity-distribution": "precision",
 "geo-sahara-vegetation-hemisphere-easy": "linkage", "geo-aral-sea-shrinking": "linkage", "geo-dead-sea-lowest-rift": "precision",
 "geo-everest-mauna-kea-base": "precision", "geo-norway-fjords-oil": "linkage", "geo-panama-locks-suez": "linkage",
 "geo-lakes-countries-pairs": "recall", "geo-river-mouths-pairs": "recall", "geo-straits-pairs": "recall",
 "geo-africa-three-latitudes-easy": "recall", "geo-great-lakes-border-easy": "recall", "geo-kilimanjaro-tanzania": "recall",
 "geo-longest-river-europe-volga": "recall", "geo-red-sea-salinity": "recall", "geo-south-africa-two-oceans": "recall",
 "geo-strait-of-malacca": "recall", "geo-antarctica-mississippi-easy": "recall", "geo-continents-asia-australia-easy": "recall",
 "geo-polar-regions-treaty-svalbard": "recall", "geo-black-sea-coast-countries": "multi", "geo-europe-rivers-danube-rhine-tagus": "recall",
 "geo-equator-countries": "multi", "geo-landlocked-countries": "multi", "geo-mountain-ranges-andes-atlas-appalachians": "recall",
 "geo-regions-in-news-golan-donbas-karabakh": "recall", "ugeo-caspian-littoral-states": "multi"}

if __name__ == "__main__":
    write_updates("upg_l2_t12_geo_b.sql", statuses=("draft", "published"), tags=TAGS)
