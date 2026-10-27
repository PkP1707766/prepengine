# -*- coding: utf-8 -*-
"""Current Affairs · Test 1 (January to March 2026) -- part G: Geography.

Places in the news in January-March 2026 -- Venezuela, Greenland, the Strait of Hormuz and the islands and ports of
the Gulf during the West Asian war, the Shaksgam Valley -- and the twenty-fifth anniversary of the Bhuj earthquake
(26 January 2001), set against the static geography and law behind them. Every fact was searched in the whole UPSC
bank and is one no row tests."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Geography"
d.REQUIRE_CRAFT = True
WR, GM, OC = "World Regions, Water Bodies & Places", "Geomorphology & Earth's Interior", "Oceanography & Hydrosphere"
IP = "Indian Physiography, Climate & Regions"

S(WR, "medium", "The US operation of January 2026 in which Venezuela's President was captured drew attention to the country's geography. Consider the following statements:",
  "जनवरी 2026 के जिस अमेरिकी अभियान में वेनेज़ुएला के राष्ट्रपति को पकड़ा गया, उसने देश के भूगोल की ओर ध्यान खींचा। निम्नलिखित कथनों पर विचार कीजिए:",
  ["Venezuela has the largest proven reserves of crude oil of any country.",
   "The Orinoco belt holds very large deposits of extra-heavy crude oil.",
   "Lake Maracaibo is a freshwater lake with no connection to the sea.",
   "Venezuela's coastline lies on the Pacific Ocean."],
  ["वेनेज़ुएला के पास किसी भी देश से अधिक प्रमाणित कच्चे तेल के भंडार हैं।",
   "ओरिनोको पट्टी में अति-भारी कच्चे तेल के बहुत बड़े भंडार हैं।",
   "माराकाइबो झील एक मीठे पानी की झील है जिसका समुद्र से कोई संबंध नहीं है।",
   "वेनेज़ुएला का समुद्र-तट प्रशांत महासागर पर है।"],
  C4, 1,
  "Statements 1 and 2 are correct. Venezuela's proven reserves, at about 300 billion barrels, are the largest in the world, ahead of Saudi Arabia's, but most of them lie in the Orinoco belt north of the Orinoco river as extra-heavy crude that is costly to extract, upgrade and refine -- one reason its output collapsed under sanctions and mismanagement, and why Indian refiners built to process heavy crude have been among its buyers. "
  "Statement 3 is wrong: Lake Maracaibo, in the north-west, is a large brackish lagoon joined to the Gulf of Venezuela and the Caribbean by a narrow strait, and is one of the oldest oil-producing areas of the country. Statement 4 is wrong: Venezuela faces the Caribbean Sea and the Atlantic; it has no Pacific coast, which its neighbour Colombia has.",
  "कथन 1 और 2 सही हैं। लगभग 300 अरब बैरल के साथ वेनेज़ुएला के प्रमाणित भंडार सऊदी अरब से भी आगे, विश्व में सबसे बड़े हैं, पर उनमें से अधिकांश ओरिनोको नदी के उत्तर की ओरिनोको पट्टी में अति-भारी कच्चे तेल के रूप में हैं जिसे निकालना, उन्नत करना और परिष्कृत करना महँगा है -- यही प्रतिबंधों और कुप्रबंधन में उसका उत्पादन ढहने का एक कारण है, और इसीलिए भारी कच्चे तेल के लिए बनी भारतीय रिफ़ाइनरियाँ उसकी ख़रीदार रही हैं। "
  "कथन 3 ग़लत है: उत्तर-पश्चिम में माराकाइबो झील एक बड़ा खारा लैगून है जो एक संकरे जलडमरूमध्य से वेनेज़ुएला की खाड़ी और कैरिबियन से जुड़ा है, और देश के सबसे पुराने तेल-उत्पादक क्षेत्रों में है। कथन 4 ग़लत है: वेनेज़ुएला कैरिबियन सागर और अटलांटिक की ओर है; उसका कोई प्रशांत तट नहीं है, जो उसके पड़ोसी कोलंबिया के पास है।",
  "OPEC, Annual Statistical Bulletin (proven crude oil reserves by country); NCERT, Fundamentals of Human Geography (Class XII), on mineral and energy resources; Oxford School Atlas.",
  "ca-t1-geo-venezuela-orinoco-maracaibo", craft="multi")

S(WR, "easy", "In January 2026 US pressure to acquire Greenland strained relations between the United States and Europe. Consider the following statements about Greenland:",
  "जनवरी 2026 में ग्रीनलैंड को हासिल करने के अमेरिकी दबाव ने संयुक्त राज्य अमेरिका और यूरोप के संबंधों पर तनाव डाला। ग्रीनलैंड के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is a self-governing part of the Kingdom of Denmark.",
   "It left the European Economic Community in 1985, although Denmark remains in the European Union.",
   "Most of its area lies north of the Arctic Circle."],
  ["यह डेनमार्क राज्य का एक स्वशासित भाग है।",
   "इसने 1985 में यूरोपीय आर्थिक समुदाय छोड़ दिया, यद्यपि डेनमार्क यूरोपीय संघ में बना हुआ है।",
   "इसका अधिकांश क्षेत्र आर्कटिक वृत्त के उत्तर में है।"],
  C3, 2,
  "All three statements are correct. Greenland, the world's largest island, gained home rule in 1979 and wider self-government under a 2009 Act that recognises the Greenlandic people's right to independence; Denmark still handles its foreign and defence policy. It joined the EEC with Denmark in 1973 but voted in 1982 to leave, mainly over control of its fisheries, and left in 1985, keeping links as an overseas country and territory -- the best-known exit before Brexit. "
  "Some four-fifths of it is covered by an ice sheet second only to Antarctica's, and nearly all of it lies north of the Arctic Circle. Its position on the shortest air and missile routes between North America and Eurasia, the US Pituffik Space Base, the waters of the GIUK gap and its rare earths explain the strategic interest.",
  "तीनों कथन सही हैं। विश्व का सबसे बड़ा द्वीप ग्रीनलैंड 1979 में गृह-शासन और 2009 के एक अधिनियम से व्यापक स्वशासन पा गया, जो ग्रीनलैंडवासियों का स्वतंत्रता का अधिकार मानता है; उसकी विदेश और रक्षा नीति अब भी डेनमार्क संभालता है। यह 1973 में डेनमार्क के साथ ईईसी में शामिल हुआ पर 1982 में मुख्यतः अपने मत्स्य-क्षेत्र पर नियंत्रण के प्रश्न पर अलग होने के पक्ष में मत दिया, और 1985 में अलग होकर एक समुद्रपार देश और क्षेत्र के रूप में संबंध रखे -- ब्रेग्ज़िट से पहले का सबसे चर्चित निकास। "
  "इसका लगभग चार-पाँचवाँ भाग अंटार्कटिका के बाद सबसे बड़ी हिम-चादर से ढका है, और लगभग पूरा आर्कटिक वृत्त के उत्तर में है। उत्तरी अमेरिका और यूरेशिया के बीच सबसे छोटे वायु और मिसाइल मार्गों पर इसकी स्थिति, अमेरिकी पिटुफ़िक अंतरिक्ष अड्डा, जीआईयूके अंतराल के जल और इसके दुर्लभ मृदा तत्व सामरिक रुचि की व्याख्या करते हैं।",
  "Act on Greenland Self-Government (Denmark, 2009); Treaty amending the European Communities with regard to Greenland (1984); Oxford School Atlas.",
  "ca-t1-geo-greenland-self-rule-eec-exit", craft="recall")

M(WR, "hard",
  "After the strikes on Iran that began in February 2026, shipping through the Strait of Hormuz was disrupted. Which one of the following ports can ships reach and leave without passing through the Strait?",
  "फ़रवरी 2026 में ईरान पर शुरू हुए हमलों के बाद होर्मुज़ जलडमरूमध्य से नौवहन बाधित हुआ। निम्नलिखित में से किस बंदरगाह तक जहाज़ जलडमरूमध्य से गुज़रे बिना पहुँच और वहाँ से निकल सकते हैं?",
  ["Chabahar in Iran", "Ras Laffan in Qatar", "Ras Tanura in Saudi Arabia", "Jebel Ali in the United Arab Emirates"],
  ["ईरान का चाबहार", "क़तर का रास लफ़ान", "सऊदी अरब का रास तनूरा", "संयुक्त अरब अमीरात का जेबेल अली"],
  0,
  "Chabahar lies on the Gulf of Oman coast of Iran's Sistan-Baluchestan province, outside the Strait, which is why India developed its Shahid Beheshti terminal as a route to Afghanistan and Central Asia that avoids both Pakistan and the Gulf chokepoint (though the Budget of 2026-27 made no allocation for it after the US withdrew its sanctions waiver). "
  "The other three lie inside the Persian Gulf: Ras Laffan is Qatar's LNG hub, the source of much of India's imported gas, which came under attack in March 2026; Ras Tanura is Saudi Arabia's main crude-export terminal; and Jebel Ali at Dubai is the region's busiest container port. Ships to and from all three must use the Strait -- the reason Saudi Arabia and the UAE have pipelines to Yanbu on the Red Sea and Fujairah on the Gulf of Oman to bypass it.",
  "चाबहार ईरान के सिस्तान-बलूचिस्तान प्रांत के ओमान की खाड़ी वाले तट पर, जलडमरूमध्य के बाहर है, इसीलिए भारत ने इसके शहीद बेहेश्ती टर्मिनल को अफ़ग़ानिस्तान और मध्य एशिया के ऐसे मार्ग के रूप में विकसित किया जो पाकिस्तान और खाड़ी के अवरोध-बिंदु दोनों से बचे (यद्यपि अमेरिका द्वारा प्रतिबंध-छूट वापस लेने के बाद 2026-27 के बजट में इसके लिए कोई आवंटन नहीं हुआ)। "
  "अन्य तीनों फ़ारस की खाड़ी के भीतर हैं: रास लफ़ान क़तर का एलएनजी केंद्र है, भारत की आयातित गैस के बड़े भाग का स्रोत, जिस पर मार्च 2026 में हमला हुआ; रास तनूरा सऊदी अरब का मुख्य कच्चा-तेल निर्यात टर्मिनल है; और दुबई का जेबेल अली क्षेत्र का सबसे व्यस्त कंटेनर बंदरगाह है। तीनों तक आने-जाने वाले जहाज़ों को जलडमरूमध्य से गुज़रना पड़ता है -- इसीलिए सऊदी अरब और यूएई ने उससे बचने के लिए लाल सागर पर यानबू और ओमान की खाड़ी पर फ़ुजैरा तक पाइपलाइनें बनाई हैं।",
  "Oxford School Atlas (West Asia); Ministry of Ports, Shipping and Waterways, Chabahar (Shahid Beheshti) port project; Ministry of Petroleum and Natural Gas, statements on supply security (March 2026).",
  "ca-t1-geo-hormuz-ports-chabahar-outside", pos=3, craft="application")

P(OC, "hard", "During the West Asian conflict of 2026, several islands were in the news. Consider the following pairs of islands and the waters in which they lie:",
  "2026 के पश्चिम एशियाई संघर्ष के दौरान कई द्वीप चर्चा में रहे। द्वीपों और उन जलक्षेत्रों के निम्नलिखित युग्मों पर विचार कीजिए जिनमें वे स्थित हैं:",
  ["Kharg Island : Persian Gulf",
   "Qeshm Island : Strait of Hormuz",
   "Socotra : Arabian Sea",
   "Abu Musa : Persian Gulf"],
  ["ख़ार्ग द्वीप : फ़ारस की खाड़ी",
   "क़ेश्म द्वीप : होर्मुज़ जलडमरूमध्य",
   "सोकोत्रा : अरब सागर",
   "अबू मूसा : फ़ारस की खाड़ी"],
  3,
  "All four pairs are correct. Kharg, a small island off Iran's coast in the northern Persian Gulf, handles most of Iran's crude exports. Qeshm, the largest island of the region, lies in the Strait of Hormuz itself, opposite Bandar Abbas, and was among the places struck in March 2026. Socotra, which belongs to Yemen, lies in the Arabian Sea off the Horn of Africa, near the mouth of the Gulf of Aden. "
  "Abu Musa, near the western approach to the Strait, is held by Iran and claimed by the United Arab Emirates, as are the Greater and Lesser Tunbs -- islands whose control matters because the deep-water shipping lanes pass close to them.",
  "चारों युग्म सही हैं। ईरान के तट के पास उत्तरी फ़ारस की खाड़ी का छोटा द्वीप ख़ार्ग ईरान के अधिकांश कच्चे तेल के निर्यात को संभालता है। क्षेत्र का सबसे बड़ा द्वीप क़ेश्म स्वयं होर्मुज़ जलडमरूमध्य में, बंदर अब्बास के सामने है, और मार्च 2026 में जिन स्थानों पर हमले हुए उनमें था। यमन का सोकोत्रा हॉर्न ऑफ़ अफ़्रीका के पास, अदन की खाड़ी के मुहाने के निकट अरब सागर में है। "
  "जलडमरूमध्य के पश्चिमी प्रवेश के पास अबू मूसा ईरान के नियंत्रण में है और संयुक्त अरब अमीरात उस पर दावा करता है, जैसे बड़े और छोटे टुंब पर -- ऐसे द्वीप जिनका नियंत्रण इसलिए मायने रखता है कि गहरे पानी के नौवहन मार्ग उनके पास से गुज़रते हैं।",
  "Oxford School Atlas (West Asia and the Arabian Sea); NCERT, Fundamentals of Physical Geography (Class XI), on oceans and seas.",
  "ca-t1-geo-gulf-islands-kharg-qeshm-socotra", craft="precision")

S(GM, "hard", "January 2026 marked twenty-five years since the Bhuj earthquake of 26 January 2001. Consider the following statements:",
  "जनवरी 2026 में 26 जनवरी 2001 के भुज भूकंप के पच्चीस वर्ष पूरे हुए। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Bhuj earthquake occurred on the boundary between the Indian and Eurasian plates.",
   "The revised seismic code of 2025, which added a new highest-hazard Zone VI, is in force across India.",
   "Under India's seismic zoning, the whole of Gujarat lies in Zone V."],
  ["भुज भूकंप भारतीय और यूरेशियाई प्लेटों की सीमा पर आया था।",
   "नई उच्चतम-जोखिम वाली ज़ोन VI जोड़ने वाली 2025 की संशोधित भूकंपीय संहिता पूरे भारत में लागू है।",
   "भारत के भूकंपीय क्षेत्रीकरण में पूरा गुजरात ज़ोन V में आता है।"],
  C3, 3,
  "None of the statements is correct. The Bhuj earthquake was an intraplate event, on old faults of the Kachchh rift basin far from any plate boundary -- a reminder that stable peninsular India can also produce large earthquakes; the disaster led to Gujarat's State Disaster Management Act of 2003 and fed into the national Disaster Management Act, 2005. "
  "The Bureau of Indian Standards issued a revised code in 2025 based on probabilistic hazard assessment, placing the whole Himalayan arc in a new Zone VI, but withdrew it in March 2026 after concerns over costs and consultation, restoring the 2016 code. Under that code only Kachchh is in Zone V; most of the rest of Gujarat is in Zones III and IV.",
  "कोई भी कथन सही नहीं है। भुज भूकंप प्लेट के भीतर की घटना था, किसी प्लेट-सीमा से दूर कच्छ रिफ़्ट बेसिन के पुराने भ्रंशों पर -- यह याद दिलाता है कि स्थिर प्रायद्वीपीय भारत में भी बड़े भूकंप आ सकते हैं; इस आपदा से 2003 का गुजरात राज्य आपदा प्रबंधन अधिनियम बना और यह राष्ट्रीय आपदा प्रबंधन अधिनियम, 2005 का आधार बनी। "
  "भारतीय मानक ब्यूरो ने 2025 में संभाव्य जोखिम आकलन पर आधारित एक संशोधित संहिता जारी की, जिसने पूरे हिमालयी चाप को नई ज़ोन VI में रखा, पर लागत और परामर्श की चिंताओं के बाद मार्च 2026 में उसे वापस ले लिया और 2016 की संहिता बहाल की। उस संहिता में केवल कच्छ ज़ोन V में है; गुजरात का अधिकांश शेष भाग ज़ोन III और IV में है।",
  "Bureau of Indian Standards, IS 1893 (Part 1): 2016 and the withdrawal of IS 1893: 2025 (March 2026); NCERT, India: Physical Environment (Class XI), Chapter 7 (Natural Hazards and Disasters); Disaster Management Act, 2005.",
  "ca-t1-geo-bhuj-25-years-intraplate-zone-code", craft="multi")

S(IP, "hard", "In January 2026 Chinese construction in the Shaksgam Valley drew a protest from India. Consider the following statements:",
  "जनवरी 2026 में शक्सगाम घाटी में चीनी निर्माण पर भारत ने विरोध दर्ज कराया। निम्नलिखित कथनों पर विचार कीजिए:",
  ["Pakistan ceded the Shaksgam Valley to China under their boundary agreement of 1963.",
   "India accepted that agreement as part of its 1993 agreement with China on peace along the Line of Actual Control.",
   "The Shaksgam Valley lies in the Aksai Chin area of eastern Ladakh."],
  ["पाकिस्तान ने 1963 के अपने सीमा समझौते के अंतर्गत शक्सगाम घाटी चीन को सौंप दी।",
   "भारत ने वास्तविक नियंत्रण रेखा पर शांति के लिए चीन के साथ अपने 1993 के समझौते के अंग के रूप में उस समझौते को स्वीकार किया।",
   "शक्सगाम घाटी पूर्वी लद्दाख के अक्साई चिन क्षेत्र में है।"],
  C3, 0,
  "Only statement 1 is correct. The Shaksgam or Trans-Karakoram Tract, about 5,000 sq km north of the main Karakoram ridge and the Siachen glacier, drained by the Shaksgam river towards the Yarkand, was part of the former State of Jammu and Kashmir in the region under Pakistan's control; under the 1963 agreement Pakistan handed it to China, though the agreement itself calls the arrangement provisional pending a settlement of Kashmir. "
  "Statement 2 is wrong: India has never recognised the 1963 agreement and regards the tract as part of its territory; the 1993 agreement on the LAC does not touch it. Statement 3 is wrong: Aksai Chin is a different area, in eastern Ladakh, held by China since the 1950s, through which it built its Xinjiang–Tibet highway. Together they show how China holds territory claimed by India on both sides of the Karakoram.",
  "केवल कथन 1 सही है। शक्सगाम या ट्रांस-काराकोरम ट्रैक्ट, मुख्य काराकोरम श्रेणी और सियाचिन हिमनद के उत्तर में लगभग 5,000 वर्ग किमी का क्षेत्र, जिसे शक्सगाम नदी यारकंद की ओर अपवाहित करती है, पूर्व जम्मू और कश्मीर राज्य के पाकिस्तान-नियंत्रित क्षेत्र का भाग था; 1963 के समझौते के अंतर्गत पाकिस्तान ने इसे चीन को सौंप दिया, यद्यपि समझौता स्वयं इस व्यवस्था को कश्मीर के समाधान तक अस्थायी बताता है। "
  "कथन 2 ग़लत है: भारत ने 1963 के समझौते को कभी मान्यता नहीं दी और इस क्षेत्र को अपना भाग मानता है; वास्तविक नियंत्रण रेखा पर 1993 का समझौता इसे नहीं छूता। कथन 3 ग़लत है: अक्साई चिन एक अलग क्षेत्र है, पूर्वी लद्दाख में, जो 1950 के दशक से चीन के पास है और जिससे होकर उसने अपना शिनजियांग–तिब्बत राजमार्ग बनाया। दोनों मिलकर दिखाते हैं कि चीन काराकोरम के दोनों ओर भारत द्वारा दावा किए गए क्षेत्र पर क़ाबिज़ है।",
  "Ministry of External Affairs, statements on the Shaksgam Valley (January 2026); Survey of India, political map of India; China–Pakistan Boundary Agreement (1963), Article 6.",
  "ca-t1-geo-shaksgam-1963-cession-not-aksai-chin", craft="precision")

S(OC, "hard", "In March 2026 Sri Lanka allowed an Iranian naval ship in distress to dock, and the law of the sea in wartime came under discussion. With reference to the UN Convention on the Law of the Sea, consider the following statements:",
  "मार्च 2026 में श्रीलंका ने संकटग्रस्त एक ईरानी नौसैनिक पोत को लंगर डालने दिया, और युद्धकाल में समुद्री विधि पर चर्चा हुई। समुद्री विधि पर संयुक्त राष्ट्र अभिसमय के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["A coastal State's territorial sea may extend up to 12 nautical miles from its baselines.",
   "Ships of all States enjoy the right of innocent passage through the territorial sea.",
   "In straits used for international navigation, ships and aircraft enjoy the right of transit passage, which the States bordering the strait may not suspend."],
  ["किसी तटीय राज्य का प्रादेशिक समुद्र उसकी आधार-रेखाओं से 12 समुद्री मील तक हो सकता है।",
   "सभी राज्यों के जहाज़ों को प्रादेशिक समुद्र से निर्दोष मार्ग का अधिकार है।",
   "अंतरराष्ट्रीय नौवहन में प्रयुक्त जलडमरूमध्यों में जहाज़ों और विमानों को पारगमन मार्ग का अधिकार है, जिसे जलडमरूमध्य से लगे राज्य निलंबित नहीं कर सकते।"],
  C3, 2,
  "All three statements are correct. UNCLOS lets a State claim a territorial sea of up to 12 nautical miles (Article 3), in which foreign ships enjoy innocent passage so long as it is not prejudicial to the coastal State's peace, good order or security (Articles 17-19); the coastal State may temporarily suspend innocent passage in specified areas for security. "
  "Straits used for international navigation have a stronger regime: transit passage, the freedom of continuous and expeditious transit for ships and aircraft, which cannot be suspended (Articles 38 and 44). Whether this applies at Hormuz is itself disputed -- Iran has signed but not ratified UNCLOS and argues that non-parties cannot claim transit passage -- which is why the closure of the Strait raised legal as well as economic questions. India ratified the Convention in 1995.",
  "तीनों कथन सही हैं। यूएनक्लॉस किसी राज्य को अधिकतम 12 समुद्री मील के प्रादेशिक समुद्र का दावा करने देता है (अनुच्छेद 3), जिसमें विदेशी जहाज़ों को निर्दोष मार्ग का अधिकार है बशर्ते वह तटीय राज्य की शांति, सुव्यवस्था या सुरक्षा के प्रतिकूल न हो (अनुच्छेद 17-19); तटीय राज्य सुरक्षा के लिए विनिर्दिष्ट क्षेत्रों में निर्दोष मार्ग को अस्थायी रूप से निलंबित कर सकता है। "
  "अंतरराष्ट्रीय नौवहन में प्रयुक्त जलडमरूमध्यों के लिए सशक्त व्यवस्था है: पारगमन मार्ग, यानी जहाज़ों और विमानों के निरंतर और शीघ्र पारगमन की स्वतंत्रता, जिसे निलंबित नहीं किया जा सकता (अनुच्छेद 38 और 44)। होर्मुज़ पर यह लागू होता है या नहीं, यह स्वयं विवादित है -- ईरान ने यूएनक्लॉस पर हस्ताक्षर किए हैं पर अनुसमर्थन नहीं, और उसका तर्क है कि ग़ैर-पक्षकार पारगमन मार्ग का दावा नहीं कर सकते -- इसीलिए जलडमरूमध्य बंद होने ने आर्थिक के साथ विधिक प्रश्न भी उठाए। भारत ने 1995 में अभिसमय का अनुसमर्थन किया।",
  "United Nations Convention on the Law of the Sea (1982), Articles 3, 17-19, 25, 38 and 44.",
  "ca-t1-geo-unclos-innocent-vs-transit-passage", craft="linkage")

M(WR, "easy",
  "The Musandam Peninsula, which forms the southern shore of the Strait of Hormuz at its narrowest, belongs to:",
  "होर्मुज़ जलडमरूमध्य के सबसे संकरे भाग का दक्षिणी तट बनाने वाला मुसंदम प्रायद्वीप किस देश का है?",
  ["Oman", "the United Arab Emirates", "Iran", "Saudi Arabia"],
  ["ओमान", "संयुक्त अरब अमीरात", "ईरान", "सऊदी अरब"],
  0,
  "The Musandam Peninsula is an exclave of Oman, separated from the rest of the country by territory of the United Arab Emirates; its rugged, fjord-like coast faces Iran's Bandar Abbas and Qeshm across the Strait. Because the shipping lanes through the narrowest part run through Omani waters under a traffic separation scheme, Oman is a key party in keeping the Strait open, and Muscat has often been a channel for talks with Iran. "
  "The UAE lies further south-west along the Gulf coast, Iran holds the northern shore, and Saudi Arabia does not reach the Strait at all.",
  "मुसंदम प्रायद्वीप ओमान का एक बहिःक्षेत्र है, जो देश के शेष भाग से संयुक्त अरब अमीरात के क्षेत्र द्वारा अलग है; इसका ऊबड़-खाबड़, फ़्योर्ड जैसा तट जलडमरूमध्य के पार ईरान के बंदर अब्बास और क़ेश्म के सामने है। चूँकि सबसे संकरे भाग के नौवहन मार्ग एक यातायात पृथक्करण योजना के अंतर्गत ओमानी जल से गुज़रते हैं, जलडमरूमध्य खुला रखने में ओमान प्रमुख पक्ष है, और मस्कट प्रायः ईरान से वार्ता का माध्यम रहा है। "
  "यूएई खाड़ी के तट पर और दक्षिण-पश्चिम में है, उत्तरी तट ईरान के पास है, और सऊदी अरब जलडमरूमध्य तक पहुँचता ही नहीं।",
  "Oxford School Atlas (West Asia); International Maritime Organization, traffic separation scheme in the Strait of Hormuz.",
  "ca-t1-geo-musandam-oman-exclave-hormuz", pos=0, craft="recall")

for r in d.ROWS:
    r["question_data"]["ca_window"] = "2026-Q1"
write("ca_t1_g.sql")
