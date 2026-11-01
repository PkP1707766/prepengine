# -*- coding: utf-8 -*-
"""Current Affairs · Test 3 (July to September 2026) -- part G: Geography.

The quarter's places, framed on the map and the physical geography behind them: a new dam in the upper Yamuna, Central
Asia on the way to the SCO summit, a glacier-driven flood from Tibet into Nepal, the year's eruptions, the first World
Heritage listings of three African states and the neighbours of Saudi Arabia after the Mecca defence pact. No stem
carries a date (design doc, section 7). Every fact was searched in the whole UPSC bank and is one no row tests."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2
from ca_common import MX, finish
from ca_t3_format import FORMAT, POS

d.SUBJECT = "Geography"
d.REQUIRE_CRAFT = True
WR, GM, OC = "World Regions, Water Bodies & Places", "Geomorphology & Earth's Interior", "Oceanography & Hydrosphere"
IP = "Indian Physiography, Climate & Regions"

S(IP, "medium", "Six States have signed an agreement to build the Kishau Multipurpose Project in the upper Yamuna basin. Consider the following statements:",
  "छह राज्यों ने ऊपरी यमुना बेसिन में किशाऊ बहुउद्देशीय परियोजना बनाने के समझौते पर हस्ताक्षर किए हैं। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The dam is to be built on the Tons, a tributary of the Yamuna, on the border of Uttarakhand and Himachal Pradesh.",
   "The surface water of the Yamuna is shared among the basin States under an agreement of 1994.",
   "The Union Government will bear the entire cost of the project, including its power component."],
  ["बाँध यमुना की सहायक नदी टोंस पर, उत्तराखंड और हिमाचल प्रदेश की सीमा पर बनना है।",
   "यमुना का सतही जल बेसिन राज्यों के बीच 1994 के एक समझौते के अंतर्गत बाँटा जाता है।",
   "केंद्र सरकार परियोजना की पूरी लागत, उसके बिजली घटक सहित, वहन करेगी।"],
  C3, 1,
  "Statements 1 and 2 are correct. The Tons, which rises near the Bandarpunch massif, is the largest tributary of the Yamuna in its hill course; the 232.6-metre concrete gravity dam is to store monsoon flows for release in the lean season, for irrigation and drinking water downstream, especially Delhi, Haryana and Rajasthan, and to generate power. Under the memorandum of understanding of 1994, the basin States (Himachal Pradesh, Haryana, Uttar Pradesh with Uttarakhand, Rajasthan and Delhi) share the Yamuna's surface water, and the Upper Yamuna River Board oversees it; storage dams are needed because most of the flow comes in the four monsoon months. "
  "Statement 3 is wrong: the Centre bears 90 per cent of the cost of the irrigation and drinking-water component, and the power component is the host States' to fund. Kishau is the third such agreement in the upper Yamuna, after Renukaji on the Giri and Lakhwar on the Yamuna itself, signed in September 2026.",
  "कथन 1 और 2 सही हैं। बंदरपूँछ पर्वत-पुंज के पास से निकलने वाली टोंस अपने पहाड़ी मार्ग में यमुना की सबसे बड़ी सहायक नदी है; 232.6 मीटर का कंक्रीट गुरुत्व बाँध मानसून के प्रवाह को संचित कर कम पानी वाले मौसम में नीचे की ओर, विशेषतः दिल्ली, हरियाणा और राजस्थान में, सिंचाई और पेयजल के लिए छोड़ेगा, और बिजली बनाएगा। 1994 के समझौता ज्ञापन के अंतर्गत बेसिन राज्य (हिमाचल प्रदेश, हरियाणा, उत्तराखंड सहित उत्तर प्रदेश, राजस्थान और दिल्ली) यमुना का सतही जल बाँटते हैं, और ऊपरी यमुना नदी बोर्ड इसकी देखरेख करता है; भंडारण बाँध इसलिए आवश्यक हैं कि अधिकांश प्रवाह मानसून के चार महीनों में आता है। "
  "कथन 3 ग़लत है: सिंचाई और पेयजल घटक की लागत का 90 प्रतिशत केंद्र वहन करता है, और बिजली घटक का वित्तपोषण मेज़बान राज्यों का दायित्व है। किशाऊ ऊपरी यमुना में ऐसा तीसरा समझौता है, गिरि पर रेणुकाजी और स्वयं यमुना पर लखवाड़ के बाद, जिस पर सितंबर 2026 में हस्ताक्षर हुए।",
  "Ministry of Jal Shakti and PIB, agreement on the Kishau Multipurpose Project (15 September 2026); Memorandum of Understanding on the sharing of the surface flow of the Yamuna (12 May 1994); Upper Yamuna River Board.",
  "ca-t3-geo-kishau-tons-yamuna-1994-centre-90", craft="linkage")

S(WR, "medium", "India's Prime Minister visited Uzbekistan and then Kyrgyzstan, where the SCO summit was held at Bishkek. Consider the following statements:",
  "भारत के प्रधानमंत्री ने उज़्बेकिस्तान और फिर किर्गिज़स्तान की यात्रा की, जहाँ बिश्केक में एससीओ शिखर सम्मेलन हुआ। निम्नलिखित कथनों पर विचार कीजिए:",
  ["Kyrgyzstan shares a border with China.",
   "The Fergana Valley is shared by Uzbekistan, Kyrgyzstan and Tajikistan.",
   "Uzbekistan shares a border with Afghanistan along the Amu Darya."],
  ["किर्गिज़स्तान की सीमा चीन से लगती है।",
   "फ़रग़ना घाटी उज़्बेकिस्तान, किर्गिज़स्तान और ताजिकिस्तान में बँटी है।",
   "उज़्बेकिस्तान की सीमा अमू दरिया के साथ अफ़ग़ानिस्तान से लगती है।"],
  C3, 2,
  "All three statements are correct. Kyrgyzstan, a mountain country of the Tien Shan, borders Kazakhstan, Uzbekistan, Tajikistan and China's Xinjiang. The Fergana Valley, the most fertile and densely settled part of Central Asia, is divided among Uzbekistan, Kyrgyzstan and Tajikistan by borders drawn in the Soviet period, with enclaves that still cause disputes over water and land. Uzbekistan's short southern border with Afghanistan runs along the Amu Darya, crossed at Termez by the 'Friendship Bridge', a route for trade into Afghanistan. "
  "In August 2026 India and Uzbekistan raised their ties to a comprehensive strategic partnership and agreed a framework for long-term uranium supply; at Bishkek the SCO, marking 25 years, adopted English as an official language.",
  "तीनों कथन सही हैं। तियान शान का पर्वतीय देश किर्गिज़स्तान कज़ाख़स्तान, उज़्बेकिस्तान, ताजिकिस्तान और चीन के शिनजियांग से घिरा है। मध्य एशिया का सबसे उपजाऊ और घना बसा भाग, फ़रग़ना घाटी, सोवियत काल में खींची गई सीमाओं से उज़्बेकिस्तान, किर्गिज़स्तान और ताजिकिस्तान में बँटी है, जिनके अंतःक्षेत्र आज भी पानी और भूमि पर विवाद पैदा करते हैं। अफ़ग़ानिस्तान से उज़्बेकिस्तान की छोटी दक्षिणी सीमा अमू दरिया के साथ चलती है, जिसे तिरमिज़ में ‘मैत्री पुल’ पार करता है, जो अफ़ग़ानिस्तान में व्यापार का मार्ग है। "
  "अगस्त 2026 में भारत और उज़्बेकिस्तान ने अपने संबंधों को व्यापक रणनीतिक साझेदारी तक बढ़ाया और यूरेनियम की दीर्घकालिक आपूर्ति के ढाँचे पर सहमति की; बिश्केक में 25 वर्ष पूरे कर रहे एससीओ ने अंग्रेज़ी को आधिकारिक भाषा के रूप में अपनाया।",
  "Ministry of External Affairs, Prime Minister's visits to Uzbekistan and the Kyrgyz Republic and the 26th SCO Summit, Bishkek (August-September 2026); NCERT, Fundamentals of Human Geography and atlas.",
  "ca-t3-geo-kyrgyzstan-china-fergana-amu-darya", craft="precision")

S(GM, "hard", "A flood from Tibet devastated Nepal's Rasuwa district in 2026. Consider the following statements:",
  "2026 में तिब्बत से आई एक बाढ़ ने नेपाल के रसुवा ज़िले को तबाह कर दिया। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The flood travelled down the Bhote Koshi into the Trishuli, a river of the Gandaki system.",
   "It was set off by a large earthquake.",
   "Satellite images pointed to an avalanche of glacier ice and rock, rather than the breach of a moraine-dammed lake."],
  ["बाढ़ भोटे कोशी से होकर त्रिशूली में पहुँची, जो गंडकी तंत्र की नदी है।",
   "इसे एक बड़े भूकंप ने शुरू किया।",
   "उपग्रह चित्रों ने किसी हिमोढ़-बाँधित झील के टूटने के बजाय हिमनद की बर्फ़ और चट्टान के हिमस्खलन की ओर संकेत किया।"],
  C3, 1,
  "Statements 1 and 3 are correct. The flood began on the Lhende river in Tibet, crossed into Nepal near Rasuwagadhi as the Bhote Koshi and swept down the Trishuli, which joins the Kali Gandaki to form the Narayani, the river that enters India as the Gandak; water rose by up to nine metres in half an hour. Nepal's disaster authority called it a glacier-related flood caused by an ice-rock avalanche, after part of a glacier broke off at about 5,200 m and fell some 1,200 m onto the valley floor. "
  "Statement 2 is wrong: a small seismic signal was recorded, but the US Geological Survey and other experts read it as the effect of the collapse and debris flow, not its cause. The distinction matters for warning systems: a lake can be mapped and watched, while a glacier collapse gives little notice, and both are expected to grow more frequent as the Himalaya warms.",
  "कथन 1 और 3 सही हैं। बाढ़ तिब्बत में लेंडे नदी पर शुरू हुई, रसुवागढ़ी के पास भोटे कोशी के रूप में नेपाल में आई और त्रिशूली से होकर बही, जो काली गंडकी से मिलकर नारायणी बनाती है, वह नदी जो भारत में गंडक के रूप में प्रवेश करती है; आधे घंटे में पानी नौ मीटर तक चढ़ा। नेपाल के आपदा प्राधिकरण ने इसे बर्फ़-चट्टान हिमस्खलन से उत्पन्न हिमनद-संबंधी बाढ़ बताया, जब किसी हिमनद का एक भाग लगभग 5,200 मीटर पर टूटकर लगभग 1,200 मीटर नीचे घाटी के तल पर गिरा। "
  "कथन 2 ग़लत है: एक छोटा भूकंपीय संकेत दर्ज हुआ, पर अमेरिकी भूवैज्ञानिक सर्वेक्षण और अन्य विशेषज्ञों ने इसे टूटने और मलबा-प्रवाह का परिणाम माना, कारण नहीं। यह भेद चेतावनी प्रणालियों के लिए महत्त्वपूर्ण है: झील का मानचित्र बनाकर उस पर नज़र रखी जा सकती है, जबकि हिमनद का टूटना बहुत कम पूर्व-सूचना देता है, और हिमालय के गर्म होने के साथ दोनों के बढ़ने की आशंका है।",
  "Government of Nepal, National Disaster Risk Reduction and Management Authority, statements on the Rasuwa flood (August 2026); US Geological Survey; International Centre for Integrated Mountain Development.",
  "ca-t3-geo-rasuwa-flood-lhende-trishuli-ice-rock-avalanche", craft="inference")

M(GM, "easy",
  "Several volcanoes erupted in 2026. Which one of the following pairs of a volcano and the country where it lies is NOT correctly matched?",
  "2026 में कई ज्वालामुखी फूटे। ज्वालामुखी और उसके देश का निम्नलिखित में से कौन-सा युग्म सही सुमेलित नहीं है?",
  ["Sinabung : Philippines",
   "Etna : Italy",
   "Fuego : Guatemala",
   "Kilauea : United States"],
  ["सिनाबुंग : फ़िलीपींस",
   "एटना : इटली",
   "फ़्यूगो : ग्वाटेमाला",
   "किलाउआ : संयुक्त राज्य अमेरिका"],
  0,
  "Sinabung is in North Sumatra, Indonesia, on the Sunda arc, where the Indo-Australian plate dives beneath the Eurasian plate; it erupted at the end of August 2026. The other pairs are right: Etna, on Sicily, Italy, Europe's most active volcano, erupted in August 2026; Fuego, in Guatemala, on the volcanic arc above the subducting Cocos plate, began a new phase in August; and Kilauea, on the island of Hawaii in the United States, kept up its lava fountains through the year. "
  "The Philippines has its own volcanoes, such as Mayon and Taal, which is why it is a plausible distractor. All but Kilauea stand on plate boundaries; Kilauea is fed by a hotspot in the middle of the Pacific plate.",
  "सिनाबुंग इंडोनेशिया के उत्तरी सुमात्रा में सुंडा चाप पर है, जहाँ इंडो-ऑस्ट्रेलियाई प्लेट यूरेशियाई प्लेट के नीचे धँसती है; यह अगस्त 2026 के अंत में फूटा। शेष युग्म सही हैं: इटली के सिसिली पर स्थित एटना, यूरोप का सबसे सक्रिय ज्वालामुखी, अगस्त 2026 में फूटा; धँसती कोकोस प्लेट के ऊपर ज्वालामुखी चाप पर ग्वाटेमाला का फ़्यूगो अगस्त में नए चरण में आया; और संयुक्त राज्य अमेरिका के हवाई द्वीप पर किलाउआ वर्ष भर लावा फव्वारे छोड़ता रहा। "
  "फ़िलीपींस के अपने ज्वालामुखी हैं, जैसे मेयॉन और ताल, इसी कारण यह विश्वसनीय भ्रामक विकल्प है। किलाउआ को छोड़ सभी प्लेट सीमाओं पर हैं; किलाउआ प्रशांत प्लेट के मध्य एक हॉटस्पॉट से पोषित है।",
  "ASEAN Coordinating Centre for Humanitarian Assistance (AHA Centre), Sinabung eruption (31 August 2026); Copernicus Emergency Management Service, Fuego eruption (August 2026); Istituto Nazionale di Geofisica e Vulcanologia, Etna (August 2026); US Geological Survey, Hawaiian Volcano Observatory.",
  "ca-t3-geo-volcanoes-2026-sinabung-not-philippines", pos=POS.get("ca-t3-geo-volcanoes-2026-sinabung-not-philippines", 3), craft="precision")

S(WR, "easy", "Comoros, Sao Tome and Principe and South Sudan had their first sites inscribed on the World Heritage List in 2026. Consider the following statements:",
  "2026 में कोमोरोस, साओ टोमे और प्रिंसिपे तथा दक्षिण सूडान के पहले स्थल विश्व धरोहर सूची में अंकित हुए। निम्नलिखित कथनों पर विचार कीजिए:",
  ["Comoros is an island country in the Mozambique Channel.",
   "Sao Tome and Principe is an island country in the Gulf of Guinea.",
   "South Sudan is landlocked."],
  ["कोमोरोस मोज़ाम्बिक चैनल में एक द्वीपीय देश है।",
   "साओ टोमे और प्रिंसिपे गिनी की खाड़ी में एक द्वीपीय देश है।",
   "दक्षिण सूडान स्थलरुद्ध है।"],
  C3, 2,
  "All three statements are correct. The Comoros lie at the northern end of the Mozambique Channel, between Mozambique and Madagascar, in the western Indian Ocean; Sao Tome and Principe, two volcanic islands off Gabon, lie in the Gulf of Guinea almost on the Equator; and South Sudan, independent since 2011 and the newest member of the United Nations, has no coast, its trade routed through Sudan's Port Sudan or through Kenya. "
  "The 48th session of the World Heritage Committee, at Busan in July 2026, added 25 properties, bringing the total to 1,273 in 173 countries, and also inscribed Sarnath, India's 45th.",
  "तीनों कथन सही हैं। कोमोरोस पश्चिमी हिंद महासागर में मोज़ाम्बिक और मेडागास्कर के बीच मोज़ाम्बिक चैनल के उत्तरी छोर पर हैं; गैबॉन के पास दो ज्वालामुखीय द्वीप, साओ टोमे और प्रिंसिपे, लगभग भूमध्य रेखा पर गिनी की खाड़ी में हैं; और 2011 से स्वतंत्र तथा संयुक्त राष्ट्र का सबसे नया सदस्य दक्षिण सूडान तटहीन है, उसका व्यापार सूडान के पोर्ट सूडान या केन्या से होकर जाता है। "
  "जुलाई 2026 में बुसान में विश्व धरोहर समिति के 48वें सत्र ने 25 संपत्तियाँ जोड़ीं, जिससे कुल संख्या 173 देशों में 1,273 हुई, और भारत के 45वें, सारनाथ, को भी अंकित किया।",
  "UNESCO World Heritage Centre, decisions of the 48th session of the World Heritage Committee (July 2026); NCERT, atlas and Fundamentals of Physical Geography.",
  "ca-t3-geo-first-whs-comoros-sao-tome-south-sudan", craft="precision")

S(WR, "medium", "Saudi Arabia, Turkey and Pakistan have signed a joint defence agreement at Mecca. Consider the following countries:",
  "सऊदी अरब, तुर्किये और पाकिस्तान ने मक्का में एक संयुक्त रक्षा समझौते पर हस्ताक्षर किए हैं। निम्नलिखित देशों पर विचार कीजिए:",
  ["Jordan", "Iraq", "Oman", "Syria"],
  ["जॉर्डन", "इराक़", "ओमान", "सीरिया"],
  C4, 2,
  "Only three of them -- Jordan (1), Iraq (2) and Oman (3) -- share a land border with Saudi Arabia. The kingdom borders seven countries: Jordan, Iraq and Kuwait to the north, Qatar, the United Arab Emirates and Oman to the east and south-east, and Yemen to the south, from where the Houthis fired missiles at it in September 2026; Bahrain is joined to it only by a causeway. Syria does not touch Saudi Arabia: Jordan and Iraq lie between them. "
  "Under the pact signed on 7 August 2026, an attack on any of the three is to be treated as an attack on all; Saudi Arabia and Pakistan already had a mutual defence agreement of September 2025.",
  "इनमें से केवल तीन -- जॉर्डन (1), इराक़ (2) और ओमान (3) -- की स्थल सीमा सऊदी अरब से लगती है। राज्य की सीमा सात देशों से लगती है: उत्तर में जॉर्डन, इराक़ और कुवैत, पूर्व और दक्षिण-पूर्व में क़तर, संयुक्त अरब अमीरात और ओमान, और दक्षिण में यमन, जहाँ से हूती विद्रोहियों ने सितंबर 2026 में उस पर मिसाइलें दागीं; बहरीन उससे केवल एक सेतु से जुड़ा है। सीरिया सऊदी अरब को नहीं छूता: उनके बीच जॉर्डन और इराक़ हैं। "
  "7 अगस्त 2026 को हस्ताक्षरित समझौते के अंतर्गत तीनों में से किसी पर आक्रमण सब पर आक्रमण माना जाना है; सऊदी अरब और पाकिस्तान के बीच सितंबर 2025 का एक पारस्परिक रक्षा समझौता पहले से था।",
  "Kingdom of Saudi Arabia, Republic of Turkiye and Islamic Republic of Pakistan, Mecca Joint Defence Agreement (7 August 2026); NCERT, atlas.",
  "ca-t3-geo-saudi-neighbours-jordan-iraq-oman-not-syria",
  closing="How many of them share a land border with Saudi Arabia?", closing_hi="इनमें से कितने देशों की स्थल सीमा सऊदी अरब से लगती है?", craft="precision")

finish("ca_t3_g.sql", FORMAT, "2026-Q3", update="--update" in sys.argv)
