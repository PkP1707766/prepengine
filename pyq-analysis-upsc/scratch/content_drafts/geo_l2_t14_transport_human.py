# -*- coding: utf-8 -*-
"""Level 2 · Test 14 (Geography 3: Human & Economic Geography) -- Transport, Ports & Human Geography:
50 new bilingual rows against the live gap report: medium statement 17, medium MCQ 7, hard statement 5,
medium Statement-I/II 5, easy statement 4, hard MCQ 3, easy MCQ 2, easy Statement-I/II 2, hard
Statement-I/II 1 + I/II/III 1, medium pairs 2, hard pairs 1.
Age pyramids and the urban heat island are in the Environment tests, the Aspirational Districts and
NFSA in Polity, and the Suez and Panama canals in Test 12, so they are left alone. Census figures are
from 2011, the latest completed Census; the 2027 Census is tested only on decisions already notified."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Geography"
TH = "Transport, Ports & Human Geography"
NC10 = "NCERT Class X, Contemporary India II"
NC12I = "NCERT Class XII, India: People and Economy"
NC12F = "NCERT Class XII, Fundamentals of Human Geography"
CEN = "Census of India 2011"
MOPSW = "Ministry of Ports, Shipping and Waterways"

# ================================================================ MEDIUM STATEMENTS (17)
S(TH, "medium", "Consider the following statements about Indian Railways:",
  "भारतीय रेल के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The first passenger train in India ran between Bombay and Thane in 1853.",
   "Metre gauge is the widest of the track gauges used in India.",
   "Narrow gauge is now the most widely used gauge in India."],
  ["भारत में पहली यात्री रेलगाड़ी 1853 में बॉम्बे और ठाणे के बीच चली।",
   "मीटर गेज भारत में प्रयुक्त रेल पटरियों की चौड़ाइयों (गेज) में सबसे चौड़ी है।",
   "नैरो गेज अब भारत में सबसे अधिक प्रयुक्त गेज है।"],
  C3, 0,
  "Only statement 1 is correct: the first train covered about 34 km from Bori Bunder to Thane on 16 April 1853. "
  "Statement 2 is wrong: broad gauge, 1.676 m between the rails, is the widest; metre gauge is 1 m and narrow gauge 0.762 m or 0.610 m. "
  "Statement 3 is wrong: under Project Unigauge almost the whole network has been converted to broad gauge; narrow gauge survives mainly on heritage hill lines such as Darjeeling and Matheran.",
  "केवल कथन 1 सही है: पहली रेलगाड़ी ने 16 अप्रैल 1853 को बोरी बंदर से ठाणे तक लगभग 34 किमी की दूरी तय की। "
  "कथन 2 गलत है: पटरियों के बीच 1.676 मीटर वाली ब्रॉड गेज सबसे चौड़ी है; मीटर गेज 1 मीटर और नैरो गेज 0.762 मीटर या 0.610 मीटर होती है। "
  "कथन 3 गलत है: प्रोजेक्ट यूनिगेज के तहत लगभग पूरा नेटवर्क ब्रॉड गेज में बदल दिया गया है; नैरो गेज मुख्य रूप से दार्जिलिंग और माथेरान जैसी धरोहर पहाड़ी लाइनों पर बची है।",
  f"{NC12I} -- Transport and Communication; Ministry of Railways.",
  "tr-railways-1853-gauges")

S(TH, "medium", "Consider the following statements about the Dedicated Freight Corridors (DFCs):",
  "समर्पित माल गलियारों (DFC) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Eastern DFC runs from Ludhiana in Punjab to Sonnagar in Bihar.",
   "The Western DFC connects Kolkata with Mumbai.",
   "The DFCs are meant mainly for high-speed passenger trains."],
  ["पूर्वी DFC पंजाब के लुधियाना से बिहार के सोननगर तक जाता है।",
   "पश्चिमी DFC कोलकाता को मुंबई से जोड़ता है।",
   "DFC मुख्य रूप से तेज़ गति की यात्री रेलगाड़ियों के लिए हैं।"],
  C3, 0,
  "Only statement 1 is correct: the Eastern corridor, about 1,337 km long, carries coal and other bulk freight across the Indo-Gangetic plain. "
  "Statement 2 is wrong: the Western DFC runs about 1,500 km from Dadri near Delhi to the Jawaharlal Nehru Port near Mumbai, serving the ports of Gujarat and Maharashtra. "
  "Statement 3 is wrong: the DFCs are freight-only lines, meant to take slow goods trains off the crowded passenger routes and carry longer, heavier, double-stack container trains.",
  "केवल कथन 1 सही है: लगभग 1,337 किमी लंबा पूर्वी गलियारा सिंधु-गंगा मैदान के पार कोयला और अन्य थोक माल ले जाता है। "
  "कथन 2 गलत है: पश्चिमी DFC दिल्ली के पास दादरी से मुंबई के पास जवाहरलाल नेहरू बंदरगाह तक लगभग 1,500 किमी जाता है और गुजरात तथा महाराष्ट्र के बंदरगाहों को सेवा देता है। "
  "कथन 3 गलत है: DFC केवल माल के लिए बनी लाइनें हैं, जिनका उद्देश्य धीमी मालगाड़ियों को भीड़ भरे यात्री मार्गों से हटाना और अधिक लंबी, भारी, दो-मंज़िला कंटेनर गाड़ियाँ चलाना है।",
  "Ministry of Railways -- Dedicated Freight Corridor Corporation of India.",
  "tr-dedicated-freight-corridors")

S(TH, "medium", "Consider the following statements about some recent transport works:",
  "कुछ हाल के परिवहन निर्माणों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Chenab bridge on the Udhampur-Srinagar-Baramulla rail link is the world's highest railway arch bridge.",
   "The new Pamban bridge is India's first vertical-lift railway sea bridge.",
   "The Atal Tunnel connects Manali with the Lahaul-Spiti valley."],
  ["उधमपुर-श्रीनगर-बारामूला रेल लिंक पर चिनाब पुल विश्व का सबसे ऊँचा रेलवे आर्च (मेहराबदार) पुल है।",
   "नया पंबन पुल भारत का पहला वर्टिकल-लिफ़्ट रेलवे समुद्री पुल है।",
   "अटल सुरंग मनाली को लाहौल-स्पीति घाटी से जोड़ती है।"],
  C3, 2,
  "All three statements are correct. The Chenab bridge, about 359 m above the river in Reasi district, opened in June 2025 as part of the rail link that now joins the Kashmir valley to the national network. The new Pamban bridge, opened in April 2025, links Rameswaram island to the mainland and has a central span that lifts vertically to let ships pass. The Atal Tunnel under the Rohtang pass, opened in 2020, is about 9 km long and keeps Lahaul-Spiti reachable in winter.",
  "तीनों कथन सही हैं। रियासी ज़िले में नदी से लगभग 359 मीटर ऊँचा चिनाब पुल जून 2025 में उस रेल लिंक के भाग के रूप में खुला, जो अब कश्मीर घाटी को राष्ट्रीय नेटवर्क से जोड़ता है। अप्रैल 2025 में खुला नया पंबन पुल रामेश्वरम द्वीप को मुख्य भूमि से जोड़ता है, और इसका बीच का भाग जहाज़ों को निकलने देने के लिए सीधा ऊपर उठता है। 2020 में खुली, रोहतांग दर्रे के नीचे लगभग 9 किमी लंबी अटल सुरंग सर्दियों में भी लाहौल-स्पीति तक पहुँच बनाए रखती है।",
  "Ministry of Railways; Border Roads Organisation.",
  "tr-chenab-pamban-atal")

S(TH, "medium", "Consider the following statements about roads in India:",
  "भारत की सड़कों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The North-South and East-West corridors intersect at Jhansi.",
   "The Border Roads Organisation builds and maintains roads in the border areas.",
   "The North-South corridor runs from Srinagar to Chennai."],
  ["उत्तर-दक्षिण और पूर्व-पश्चिम गलियारे झाँसी पर एक-दूसरे को काटते हैं।",
   "सीमा सड़क संगठन सीमावर्ती क्षेत्रों में सड़कें बनाता है और उनका रखरखाव करता है।",
   "उत्तर-दक्षिण गलियारा श्रीनगर से चेन्नई तक जाता है।"],
  C3, 1,
  "Statements 1 and 2 are correct. The Border Roads Organisation, set up in 1960, builds strategic roads, bridges and tunnels in difficult terrain along the northern and north-eastern frontiers. "
  "Statement 3 is wrong: the North-South corridor links Srinagar with Kanyakumari; the East-West corridor links Silchar in Assam with Porbandar in Gujarat, and the two cross at Jhansi.",
  "कथन 1 और 2 सही हैं। 1960 में स्थापित सीमा सड़क संगठन उत्तरी और पूर्वोत्तर सीमाओं के साथ कठिन भू-भाग में सामरिक सड़कें, पुल और सुरंगें बनाता है। "
  "कथन 3 गलत है: उत्तर-दक्षिण गलियारा श्रीनगर को कन्याकुमारी से जोड़ता है; पूर्व-पश्चिम गलियारा असम के सिलचर को गुजरात के पोरबंदर से जोड़ता है, और दोनों झाँसी पर मिलते हैं।",
  f"{NC10} -- Lifelines of National Economy; Ministry of Road Transport and Highways.",
  "tr-road-corridors-bro")

S(TH, "medium", "Consider the following statements about National Waterways:",
  "राष्ट्रीय जलमार्गों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["National Waterway 1 is on the Ganga-Bhagirathi-Hooghly river system.",
   "National Waterway 2 is on the Brahmaputra from Dhubri to Sadiya.",
   "National Waterway 3 is the West Coast Canal in Kerala.",
   "The National Waterways Act, 2016 declared 25 National Waterways."],
  ["राष्ट्रीय जलमार्ग 1 गंगा-भागीरथी-हुगली नदी तंत्र पर है।",
   "राष्ट्रीय जलमार्ग 2 ब्रह्मपुत्र पर धुबरी से सदिया तक है।",
   "राष्ट्रीय जलमार्ग 3 केरल की पश्चिमी तट नहर है।",
   "राष्ट्रीय जलमार्ग अधिनियम, 2016 ने 25 राष्ट्रीय जलमार्ग घोषित किए।"],
  C4, 2,
  "Statements 1, 2 and 3 are correct. NW-1 runs about 1,620 km from Haldia to Prayagraj and is being upgraded under the Jal Marg Vikas project; NW-2 covers 891 km of the Brahmaputra; and NW-3 links Kottapuram and Kollam through the backwaters. "
  "Statement 4 is wrong: the 2016 Act raised the number of National Waterways to 111 -- the 5 existing ones and 106 new ones -- managed by the Inland Waterways Authority of India.",
  "कथन 1, 2 और 3 सही हैं। NW-1 हल्दिया से प्रयागराज तक लगभग 1,620 किमी जाता है और जल मार्ग विकास परियोजना के तहत उन्नत किया जा रहा है; NW-2 ब्रह्मपुत्र के 891 किमी भाग पर है; और NW-3 पश्चजल से होकर कोट्टापुरम और कोल्लम को जोड़ता है। "
  "कथन 4 गलत है: 2016 के अधिनियम ने राष्ट्रीय जलमार्गों की संख्या बढ़ाकर 111 कर दी, यानी 5 पुराने और 106 नए, जिनका प्रबंधन भारतीय अंतर्देशीय जलमार्ग प्राधिकरण करता है।",
  f"{MOPSW} -- Inland Waterways Authority of India.",
  "tr-national-waterways")

S(TH, "medium", "Consider the following statements about ports on the west coast:",
  "पश्चिमी तट के बंदरगाहों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Deendayal port (Kandla) is a tidal port.",
   "Jawaharlal Nehru Port is India's largest container port.",
   "Mormugao port in Goa is known mainly for exporting iron ore."],
  ["दीनदयाल बंदरगाह (कांडला) एक ज्वारीय (tidal) बंदरगाह है।",
   "जवाहरलाल नेहरू बंदरगाह भारत का सबसे बड़ा कंटेनर बंदरगाह है।",
   "गोवा का मोरमुगाओ बंदरगाह मुख्य रूप से लौह अयस्क के निर्यात के लिए जाना जाता है।"],
  C3, 2,
  "All three statements are correct. Deendayal, at the head of the Gulf of Kachchh, depends on the tides for its depth and is one of the busiest major ports by cargo volume, much of it petroleum. Jawaharlal Nehru Port (Nhava Sheva), built in the 1980s to relieve Mumbai, handles about half of the container traffic of the major ports. Mormugao has long shipped the iron ore of Goa's mines.",
  "तीनों कथन सही हैं। कच्छ की खाड़ी के शीर्ष पर स्थित दीनदयाल अपनी गहराई के लिए ज्वार पर निर्भर है और माल की मात्रा के अनुसार सबसे व्यस्त बड़े बंदरगाहों में से एक है, जिसमें बहुत-सा पेट्रोलियम है। मुंबई का बोझ घटाने के लिए 1980 के दशक में बना जवाहरलाल नेहरू बंदरगाह (न्हावा शेवा) बड़े बंदरगाहों के कंटेनर यातायात का लगभग आधा भाग संभालता है। मोरमुगाओ लंबे समय से गोवा की खदानों का लौह अयस्क भेजता रहा है।",
  f"{NC10} -- Lifelines of National Economy; {MOPSW}.",
  "tr-west-coast-ports")

S(TH, "medium", "Consider the following statements about ports on the east coast:",
  "पूर्वी तट के बंदरगाहों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Visakhapatnam is a deep, landlocked and well-protected port.",
   "Paradip port is in Andhra Pradesh.",
   "Kolkata port is a riverine port on the Hooghly."],
  ["विशाखापत्तनम एक गहरा, स्थल से घिरा और सुरक्षित बंदरगाह है।",
   "पारादीप बंदरगाह आंध्र प्रदेश में है।",
   "कोलकाता बंदरगाह हुगली पर स्थित एक नदी बंदरगाह है।"],
  C3, 1,
  "Statements 1 and 3 are correct. Visakhapatnam, the deepest landlocked port in the country, was developed to export iron ore; Kolkata (the Syama Prasad Mookerjee Port), about 128 km inland, has to be dredged constantly because the Hooghly brings down silt, and Haldia was developed downstream to relieve it. "
  "Statement 2 is wrong: Paradip, which specialises in iron ore and coal, is on the Odisha coast near the Mahanadi delta.",
  "कथन 1 और 3 सही हैं। देश का सबसे गहरा स्थल-रुद्ध बंदरगाह विशाखापत्तनम लौह अयस्क के निर्यात के लिए विकसित किया गया; समुद्र से लगभग 128 किमी भीतर स्थित कोलकाता (श्यामा प्रसाद मुखर्जी बंदरगाह) की लगातार तलकर्षण (dredging) करनी पड़ती है, क्योंकि हुगली गाद लाती है, और इसका बोझ घटाने के लिए नीचे की ओर हल्दिया विकसित किया गया। "
  "कथन 2 गलत है: लौह अयस्क और कोयले में विशेषज्ञता वाला पारादीप महानदी डेल्टा के पास ओडिशा तट पर है।",
  f"{NC10} -- Lifelines of National Economy; {MOPSW}.",
  "tr-east-coast-ports")

S(TH, "medium", "Consider the following statements about India's ports:",
  "भारत के बंदरगाहों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Vizhinjam in Kerala is India's first dedicated deep-water container transshipment port.",
   "Vadhavan in Maharashtra has been approved as a new major port.",
   "Kamarajar port at Ennore was India's first major port to be set up as a company."],
  ["केरल का विझिंजम भारत का पहला समर्पित गहरे जल का कंटेनर ट्रांसशिपमेंट बंदरगाह है।",
   "महाराष्ट्र के वाढवण को एक नए बड़े (major) बंदरगाह के रूप में मंज़ूरी दी गई है।",
   "एन्नोर का कामराजर बंदरगाह एक कंपनी के रूप में स्थापित भारत का पहला बड़ा बंदरगाह था।"],
  C3, 2,
  "All three statements are correct. Vizhinjam, near Thiruvananthapuram and close to the main east-west shipping route, was commissioned in 2025 so that containers need not be transshipped at Colombo or Singapore. The Union Cabinet approved the deep-draught Vadhavan port in Palghar district in 2024. Kamarajar (Ennore), near Chennai, began as India's first corporatised major port.",
  "तीनों कथन सही हैं। तिरुवनंतपुरम के पास और मुख्य पूर्व-पश्चिम जहाज़ी मार्ग के निकट स्थित विझिंजम 2025 में चालू हुआ, ताकि कंटेनरों को कोलंबो या सिंगापुर में ट्रांसशिप न करना पड़े। केंद्रीय मंत्रिमंडल ने 2024 में पालघर ज़िले में गहरे ड्राफ़्ट वाले वाढवण बंदरगाह को मंज़ूरी दी। चेन्नई के पास स्थित कामराजर (एन्नोर) भारत के पहले निगमीकृत बड़े बंदरगाह के रूप में शुरू हुआ।",
  f"{MOPSW}.",
  "tr-vizhinjam-vadhavan-kamarajar")

S(TH, "medium", "Consider the following statements about pipelines in India:",
  "भारत की पाइपलाइनों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Hazira-Vijaipur-Jagdishpur (HVJ) pipeline carries natural gas.",
   "India's first crude oil pipeline linked Naharkatiya in Assam with Guwahati and Barauni.",
   "The Motihari-Amlekhganj pipeline carries petroleum products from India to Bangladesh."],
  ["हज़ीरा-विजयपुर-जगदीशपुर (HVJ) पाइपलाइन प्राकृतिक गैस ले जाती है।",
   "भारत की पहली कच्चे तेल की पाइपलाइन ने असम के नहरकटिया को गुवाहाटी और बरौनी से जोड़ा।",
   "मोतिहारी-अमलेखगंज पाइपलाइन भारत से बांग्लादेश तक पेट्रोलियम उत्पाद ले जाती है।"],
  C3, 1,
  "Statements 1 and 2 are correct. The HVJ pipeline, built by GAIL, carries gas from the Gujarat coast to fertiliser and power plants in Madhya Pradesh and Uttar Pradesh; the Naharkatiya-Guwahati-Barauni line, completed in the early 1960s, took Assam crude to refineries in Assam and Bihar. "
  "Statement 3 is wrong: the Motihari-Amlekhganj pipeline, opened in 2019 as South Asia's first cross-border petroleum pipeline, runs from Bihar to Nepal; the India-Bangladesh Friendship Pipeline runs from Siliguri to Parbatipur.",
  "कथन 1 और 2 सही हैं। GAIL द्वारा बनाई गई HVJ पाइपलाइन गुजरात तट से मध्य प्रदेश और उत्तर प्रदेश के उर्वरक और बिजली संयंत्रों तक गैस ले जाती है; 1960 के दशक के आरंभ में पूरी हुई नहरकटिया-गुवाहाटी-बरौनी लाइन असम के कच्चे तेल को असम और बिहार की रिफ़ाइनरियों तक ले गई। "
  "कथन 3 गलत है: 2019 में दक्षिण एशिया की पहली सीमा-पार पेट्रोलियम पाइपलाइन के रूप में खुली मोतिहारी-अमलेखगंज पाइपलाइन बिहार से नेपाल तक जाती है; भारत-बांग्लादेश मैत्री पाइपलाइन सिलीगुड़ी से पार्बतीपुर तक जाती है।",
  f"{NC12I} -- Transport and Communication; Ministry of Petroleum and Natural Gas.",
  "tr-pipelines-hvj-naharkatiya-motihari")

S(TH, "medium", "Consider the following statements based on the Census of 2011:",
  "2011 की जनगणना पर आधारित निम्नलिखित कथनों पर विचार कीजिए:",
  ["Kerala had the highest sex ratio among the States.",
   "Arunachal Pradesh had the lowest population density among the States.",
   "Sikkim was the least populous State.",
   "Uttar Pradesh was the most populous State."],
  ["राज्यों में केरल का लिंगानुपात सबसे अधिक था।",
   "राज्यों में अरुणाचल प्रदेश का जनसंख्या घनत्व सबसे कम था।",
   "सिक्किम सबसे कम जनसंख्या वाला राज्य था।",
   "उत्तर प्रदेश सबसे अधिक जनसंख्या वाला राज्य था।"],
  C4, 3,
  "All four statements are correct. Kerala had 1,084 women per 1,000 men against a national 943; Arunachal Pradesh had only 17 persons per sq km against a national 382; Sikkim had about 6.1 lakh people; and Uttar Pradesh, with about 20 crore, had a sixth of India's population. "
  "A student who expects one false statement in four will lose marks here.",
  "चारों कथन सही हैं। केरल में राष्ट्रीय 943 के मुक़ाबले प्रति 1,000 पुरुषों पर 1,084 महिलाएँ थीं; अरुणाचल प्रदेश में राष्ट्रीय 382 के मुक़ाबले प्रति वर्ग किमी केवल 17 व्यक्ति थे; सिक्किम की जनसंख्या लगभग 6.1 लाख थी; और लगभग 20 करोड़ वाले उत्तर प्रदेश में भारत की जनसंख्या का छठा भाग था। "
  "जो विद्यार्थी मानकर चलता है कि चार में से एक कथन गलत होगा, वह यहाँ अंक गँवाएगा।",
  f"{CEN} -- Primary Census Abstract.",
  "hum-census-2011-state-facts")

S(TH, "medium", "Consider the following statements about the next Census of India:",
  "भारत की अगली जनगणना के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is to be the first Census in India conducted digitally.",
   "It will include the enumeration of castes.",
   "It will be conducted under the Registration of Births and Deaths Act, 1969."],
  ["यह भारत में डिजिटल रूप से की जाने वाली पहली जनगणना होगी।",
   "इसमें जातियों की गणना भी शामिल होगी।",
   "यह जन्म और मृत्यु रजिस्ट्रीकरण अधिनियम, 1969 के तहत की जाएगी।"],
  C3, 1,
  "Statements 1 and 2 are correct. The Census, delayed from 2021, was notified in June 2025 with 1 March 2027 as its reference date (1 October 2026 for the snow-bound areas of Ladakh, Jammu and Kashmir, Himachal Pradesh and Uttarakhand); data will be collected on mobile applications, with an option of self-enumeration, and castes will be counted for the first time since 1931 apart from Scheduled Castes and Tribes. "
  "Statement 3 is wrong: the Census is conducted under the Census Act, 1948; the 1969 Act governs the civil registration of births and deaths.",
  "कथन 1 और 2 सही हैं। 2021 से टली जनगणना जून 2025 में अधिसूचित की गई, जिसकी संदर्भ तिथि 1 मार्च 2027 है (लद्दाख, जम्मू-कश्मीर, हिमाचल प्रदेश और उत्तराखंड के हिमाच्छादित क्षेत्रों के लिए 1 अक्टूबर 2026); आँकड़े मोबाइल ऐप्लिकेशन पर एकत्र किए जाएँगे, स्व-गणना के विकल्प के साथ, और अनुसूचित जातियों और जनजातियों के अलावा 1931 के बाद पहली बार जातियों की गणना होगी। "
  "कथन 3 गलत है: जनगणना जनगणना अधिनियम, 1948 के तहत होती है; 1969 का अधिनियम जन्म और मृत्यु के नागरिक पंजीकरण को नियंत्रित करता है।",
  "Ministry of Home Affairs -- Office of the Registrar General and Census Commissioner, notification of June 2025.",
  "hum-census-2027")

S(TH, "medium", "Consider the following statements about migration in India:",
  "भारत में प्रवास के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Marriage is the most common reason for the migration of women.",
   "Rural-to-urban migration is the largest stream of internal migration.",
   "Most internal migrants move across State boundaries."],
  ["महिलाओं के प्रवास का सबसे आम कारण विवाह है।",
   "ग्रामीण से नगरीय प्रवास आंतरिक प्रवास की सबसे बड़ी धारा है।",
   "अधिकांश आंतरिक प्रवासी राज्य की सीमाओं के पार जाते हैं।"],
  C3, 0,
  "Only statement 1 is correct: because women usually move to the husband's home after marriage, most female migrants move for this reason, while work and employment are the main reason for men. "
  "Statement 2 is wrong: rural-to-rural migration, dominated by women moving on marriage, is the largest stream; rural-to-urban migration, mainly of men seeking work, is the most important for the economy. "
  "Statement 3 is wrong: most migrants move within their own State; inter-State migrants are a much smaller share.",
  "केवल कथन 1 सही है: चूँकि महिलाएँ प्रायः विवाह के बाद पति के घर जाती हैं, इसलिए अधिकांश महिला प्रवासी इसी कारण जाती हैं, जबकि पुरुषों के प्रवास का मुख्य कारण काम और रोज़गार है। "
  "कथन 2 गलत है: ग्रामीण से ग्रामीण प्रवास, जिसमें विवाह के कारण जाने वाली महिलाओं का वर्चस्व है, सबसे बड़ी धारा है; रोज़गार खोजने वाले मुख्यतः पुरुषों का ग्रामीण से नगरीय प्रवास अर्थव्यवस्था के लिए सबसे महत्त्वपूर्ण है। "
  "कथन 3 गलत है: अधिकांश प्रवासी अपने ही राज्य के भीतर जाते हैं; अंतर-राज्यीय प्रवासियों का हिस्सा कहीं कम है।",
  f"{NC12I} -- Migration: Types, Causes and Consequences.",
  "hum-migration-streams")

S(TH, "medium", "Consider the following statements about urban areas in India:",
  "भारत के नगरीय क्षेत्रों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["A place needs a population of at least 50,000 to be classified as a Census town.",
   "Kerala was the most urbanised State in 2011.",
   "An urban agglomeration can consist of a town and its adjoining outgrowths."],
  ["किसी स्थान को जनगणना नगर (Census town) माने जाने के लिए कम से कम 50,000 की जनसंख्या चाहिए।",
   "2011 में केरल सबसे अधिक नगरीकृत राज्य था।",
   "एक नगरीय संकुल (urban agglomeration) किसी नगर और उसके निकटवर्ती बाहरी विकास (outgrowths) से मिलकर बन सकता है।"],
  C3, 0,
  "Only statement 3 is correct: an urban agglomeration is a continuous urban spread made up of a town and its outgrowths, or two or more adjoining towns, such as Greater Mumbai or Delhi. "
  "Statement 1 is wrong: a Census town needs a population of at least 5,000, at least 75 per cent of male main workers in non-agricultural work, and a density of at least 400 persons per sq km. "
  "Statement 2 is wrong: Goa, with about 62 per cent of its people in towns, was the most urbanised State; Kerala came next.",
  "केवल कथन 3 सही है: नगरीय संकुल एक सतत नगरीय फैलाव है, जो किसी नगर और उसके बाहरी विकास से, या दो या अधिक सटे हुए नगरों से, बनता है, जैसे बृहन्मुंबई या दिल्ली। "
  "कथन 1 गलत है: जनगणना नगर के लिए कम से कम 5,000 जनसंख्या, कम से कम 75 प्रतिशत पुरुष मुख्य कामगारों का ग़ैर-कृषि कार्य में होना और प्रति वर्ग किमी कम से कम 400 व्यक्तियों का घनत्व चाहिए। "
  "कथन 2 गलत है: लगभग 62 प्रतिशत नगरीय जनसंख्या वाला गोवा सबसे अधिक नगरीकृत राज्य था; केरल उसके बाद था।",
  f"{CEN} -- Urban Agglomerations and Cities; {NC12I} -- Human Settlements.",
  "hum-census-town-urbanisation")

S(TH, "medium", "Consider the following statements about rural settlements in India:",
  "भारत की ग्रामीण बस्तियों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Clustered settlements are common in the fertile alluvial plains.",
   "Dispersed settlements are common in the hilly areas of Meghalaya, Uttarakhand and Himachal Pradesh.",
   "Semi-clustered settlements can result from the break-up of a large village along social lines."],
  ["गुच्छित (clustered) बस्तियाँ उपजाऊ जलोढ़ मैदानों में आम हैं।",
   "परिक्षिप्त (dispersed) बस्तियाँ मेघालय, उत्तराखंड और हिमाचल प्रदेश के पहाड़ी क्षेत्रों में आम हैं।",
   "अर्ध-गुच्छित बस्तियाँ किसी बड़े गाँव के सामाजिक आधार पर टूटने से बन सकती हैं।"],
  C3, 2,
  "All three statements are correct. In the plains, compact villages grow around fields, water and a common life; in the hills, where level land is scattered, homes stand apart as isolated huts or small hamlets. Semi-clustered settlements arise when a group within a large compact village settles a little way off, often along lines of caste, leaving the dominant group in the core.",
  "तीनों कथन सही हैं। मैदानों में सघन गाँव खेतों, जल और सामूहिक जीवन के आसपास बसते हैं; पहाड़ों में, जहाँ समतल भूमि बिखरी होती है, घर अलग-अलग झोंपड़ियों या छोटे पुरवों के रूप में दूर-दूर होते हैं। अर्ध-गुच्छित बस्तियाँ तब बनती हैं जब किसी बड़े सघन गाँव का कोई समूह, प्रायः जाति के आधार पर, कुछ दूरी पर बस जाता है और प्रभावशाली समूह केंद्र में रहता है।",
  f"{NC12I} -- Human Settlements.",
  "hum-rural-settlement-types")

S(TH, "medium", "Consider the following statements about the Human Development Index (HDI):",
  "मानव विकास सूचकांक (HDI) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It combines measures of health, education and per capita income.",
   "It is published by the United Nations Development Programme.",
   "The first Human Development Report was published in 1990."],
  ["यह स्वास्थ्य, शिक्षा और प्रति व्यक्ति आय के मापों को मिलाता है।",
   "इसे संयुक्त राष्ट्र विकास कार्यक्रम प्रकाशित करता है।",
   "पहली मानव विकास रिपोर्ट 1990 में प्रकाशित हुई।"],
  C3, 2,
  "All three statements are correct. The HDI uses life expectancy at birth, mean and expected years of schooling, and gross national income per head. The report was conceived by the Pakistani economist Mahbub ul Haq, with Amartya Sen among its architects, to judge development by people's choices and capabilities rather than income alone.",
  "तीनों कथन सही हैं। HDI जन्म के समय जीवन प्रत्याशा, स्कूली शिक्षा के औसत और अपेक्षित वर्ष, और प्रति व्यक्ति सकल राष्ट्रीय आय का उपयोग करता है। इस रिपोर्ट की कल्पना पाकिस्तानी अर्थशास्त्री महबूब-उल-हक़ ने की थी, जिनके साथ अमर्त्य सेन इसके निर्माताओं में थे, ताकि विकास को केवल आय से नहीं, बल्कि लोगों के विकल्पों और क्षमताओं से आँका जाए।",
  f"{NC12F} -- Human Development; United Nations Development Programme.",
  "hum-hdi-basics")

S(TH, "medium", "Consider the following statements about economic activities:",
  "आर्थिक क्रियाकलापों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Quaternary activities centre on research, information and knowledge.",
   "Quinary activities consist mainly of routine clerical work.",
   "Mining is a secondary activity."],
  ["चतुर्थक क्रियाकलाप अनुसंधान, सूचना और ज्ञान पर केंद्रित होते हैं।",
   "पंचम (quinary) क्रियाकलाप मुख्य रूप से नियमित लिपिकीय कार्य होते हैं।",
   "खनन एक द्वितीयक क्रियाकलाप है।"],
  C3, 0,
  "Only statement 1 is correct: quaternary activities include research and development, information technology, consulting and education. "
  "Statement 2 is wrong: quinary activities are the highest-level decision-making and policy roles -- senior executives, government officials, research scientists and advisers -- sometimes called 'gold collar' work. "
  "Statement 3 is wrong: mining, like farming, fishing and forestry, takes resources directly from nature and is a primary activity; turning the ore into metal is secondary.",
  "केवल कथन 1 सही है: चतुर्थक क्रियाकलापों में अनुसंधान और विकास, सूचना प्रौद्योगिकी, परामर्श और शिक्षा शामिल हैं। "
  "कथन 2 गलत है: पंचम क्रियाकलाप सर्वोच्च स्तर के निर्णय और नीति से जुड़े काम हैं, जैसे वरिष्ठ अधिकारी, सरकारी पदाधिकारी, अनुसंधान वैज्ञानिक और सलाहकार; इन्हें कभी-कभी 'गोल्ड कॉलर' काम कहा जाता है। "
  "कथन 3 गलत है: खेती, मछली पकड़ने और वानिकी की तरह खनन भी प्रकृति से सीधे संसाधन लेता है और प्राथमिक क्रियाकलाप है; अयस्क को धातु में बदलना द्वितीयक है।",
  f"{NC12F} -- Primary Activities; Tertiary and Quaternary Activities.",
  "hum-economic-activity-sectors")

S(TH, "medium", "Consider the following statements about world population:",
  "विश्व जनसंख्या के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["China was the most populous country in the world in 2024.",
   "Europe's population is growing faster than Africa's.",
   "Asia has less than half of the world's population."],
  ["2024 में चीन विश्व का सबसे अधिक जनसंख्या वाला देश था।",
   "यूरोप की जनसंख्या अफ़्रीका से अधिक तेज़ी से बढ़ रही है।",
   "विश्व की जनसंख्या का आधे से कम भाग एशिया में है।"],
  C3, 3,
  "None of the statements is correct. "
  "Statement 1 is wrong: according to the United Nations, India overtook China as the most populous country in 2023, and China's population has been falling since 2022. "
  "Statement 2 is wrong: Africa has the fastest-growing population of any continent, while Europe's is barely growing and is shrinking in several countries. "
  "Statement 3 is wrong: Asia holds nearly 60 per cent of the world's people.",
  "कोई भी कथन सही नहीं है। "
  "कथन 1 गलत है: संयुक्त राष्ट्र के अनुसार भारत 2023 में चीन से आगे निकलकर सबसे अधिक जनसंख्या वाला देश बन गया, और चीन की जनसंख्या 2022 से घट रही है। "
  "कथन 2 गलत है: अफ़्रीका की जनसंख्या किसी भी महाद्वीप से अधिक तेज़ी से बढ़ रही है, जबकि यूरोप की जनसंख्या मुश्किल से बढ़ रही है और कई देशों में घट रही है। "
  "कथन 3 गलत है: विश्व के लगभग 60 प्रतिशत लोग एशिया में रहते हैं।",
  f"United Nations -- World Population Prospects; {NC12F} -- The World Population.",
  "hum-world-population-facts")

# ================================================================ HARD STATEMENTS (5)
S(TH, "hard", "Consider the following statements about trans-continental railways:",
  "अंतर-महाद्वीपीय रेलमार्गों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Trans-Siberian railway runs from St Petersburg to Vladivostok.",
   "The Trans-Canadian railway runs from Halifax to Vancouver.",
   "The Australian trans-continental railway runs from Perth to Sydney.",
   "The Orient Express ran from Paris to Moscow."],
  ["ट्रांस-साइबेरियन रेलमार्ग सेंट पीटर्सबर्ग से व्लादिवोस्तोक तक जाता है।",
   "ट्रांस-कनाडियन रेलमार्ग हैलिफ़ैक्स से वैंकूवर तक जाता है।",
   "ऑस्ट्रेलियाई अंतर-महाद्वीपीय रेलमार्ग पर्थ से सिडनी तक जाता है।",
   "ओरिएंट एक्सप्रेस पेरिस से मॉस्को तक चलती थी।"],
  C4, 2,
  "Statements 1, 2 and 3 are correct. The Trans-Siberian, the longest railway in the world, crosses the Urals to reach the Pacific at Vladivostok; the Trans-Canadian links the Atlantic coast at Halifax with the Pacific at Vancouver; and the Australian line crosses the Nullarbor Plain on one of the longest straight stretches of track anywhere. "
  "Statement 4 is wrong: the Orient Express ran from Paris to Istanbul, through Vienna and Budapest, cutting the journey to Asia Minor.",
  "कथन 1, 2 और 3 सही हैं। विश्व का सबसे लंबा रेलमार्ग ट्रांस-साइबेरियन यूराल पार करके व्लादिवोस्तोक पर प्रशांत तक पहुँचता है; ट्रांस-कनाडियन हैलिफ़ैक्स के अटलांटिक तट को वैंकूवर के प्रशांत तट से जोड़ता है; और ऑस्ट्रेलियाई लाइन नलारबोर मैदान को कहीं की भी सबसे लंबी सीधी पटरियों में से एक पर पार करती है। "
  "कथन 4 गलत है: ओरिएंट एक्सप्रेस वियना और बुडापेस्ट होते हुए पेरिस से इस्तांबुल तक चलती थी, जिससे एशिया माइनर तक की यात्रा छोटी हुई।",
  f"{NC12F} -- Transport and Communication.",
  "tr-transcontinental-railways")

S(TH, "hard", "Consider the following statements about some major ports:",
  "कुछ बड़े बंदरगाहों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Kochi port lies at the mouth of the Vembanad backwaters.",
   "Kandla was developed soon after Independence to make up for the loss of Karachi.",
   "The New Mangalore port was developed mainly to export coal from the Chotanagpur plateau."],
  ["कोच्चि बंदरगाह वेम्बनाड पश्चजल के मुहाने पर स्थित है।",
   "कराची के छिन जाने की भरपाई के लिए स्वतंत्रता के तुरंत बाद कांडला विकसित किया गया।",
   "न्यू मंगलौर बंदरगाह मुख्य रूप से छोटानागपुर पठार का कोयला निर्यात करने के लिए विकसित किया गया।"],
  C3, 1,
  "Statements 1 and 2 are correct. Kochi, a natural harbour on Willingdon Island at the entrance to the Vembanad lagoon, is also the base of the Navy's Southern Command and India's first international transshipment terminal at Vallarpadam. Kandla was built in the 1950s because Partition left Karachi in Pakistan and Mumbai could not handle all the trade of north-western India. "
  "Statement 3 is wrong: New Mangalore was developed to export the iron ore of the Kudremukh mines in Karnataka; the coal of the Chotanagpur plateau is used mainly within India, and moves by rail.",
  "कथन 1 और 2 सही हैं। वेम्बनाड लैगून के प्रवेश पर विलिंगडन द्वीप पर स्थित प्राकृतिक बंदरगाह कोच्चि नौसेना की दक्षिणी कमान का केंद्र भी है, और वल्लारपाडम में भारत का पहला अंतरराष्ट्रीय ट्रांसशिपमेंट टर्मिनल यहीं है। कांडला 1950 के दशक में इसलिए बना कि विभाजन से कराची पाकिस्तान में चला गया और मुंबई उत्तर-पश्चिमी भारत का सारा व्यापार नहीं संभाल सकता था। "
  "कथन 3 गलत है: न्यू मंगलौर कर्नाटक की कुद्रेमुख खदानों का लौह अयस्क निर्यात करने के लिए विकसित हुआ; छोटानागपुर पठार का कोयला मुख्य रूप से देश के भीतर प्रयुक्त होता है और रेल से जाता है।",
  f"{NC10} -- Lifelines of National Economy; {MOPSW}.",
  "tr-ports-kochi-kandla-new-mangalore")

S(TH, "hard", "Consider the following statements about India's overseas connectivity projects:",
  "भारत की विदेशी संपर्क परियोजनाओं के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["India has signed a long-term agreement to operate a terminal at Chabahar port in Iran.",
   "Sittwe port in Myanmar is part of the Kaladan Multi-Modal Transit Transport Project.",
   "The International North-South Transport Corridor is meant to link India with Russia through Iran."],
  ["भारत ने ईरान के चाबहार बंदरगाह पर एक टर्मिनल चलाने के लिए दीर्घकालिक समझौता किया है।",
   "म्यांमार का सित्तवे बंदरगाह कालादान बहु-मॉडल पारगमन परिवहन परियोजना का भाग है।",
   "अंतरराष्ट्रीय उत्तर-दक्षिण परिवहन गलियारे का उद्देश्य ईरान के रास्ते भारत को रूस से जोड़ना है।"],
  C3, 2,
  "All three statements are correct. In May 2024 India Ports Global signed a ten-year contract to run the Shahid Beheshti terminal at Chabahar, India's gateway to Afghanistan and Central Asia that bypasses Pakistan. Sittwe, built by India, links Kolkata by sea to the Kaladan river and a road into Mizoram, giving the north-east a route that avoids the narrow Siliguri corridor. The INSTC combines sea, rail and road from Mumbai through Bandar Abbas and the Caspian region to Russia.",
  "तीनों कथन सही हैं। मई 2024 में इंडिया पोर्ट्स ग्लोबल ने चाबहार के शहीद बेहेश्ती टर्मिनल को चलाने के लिए दस वर्ष का अनुबंध किया; यह पाकिस्तान को बाईपास करते हुए अफ़ग़ानिस्तान और मध्य एशिया के लिए भारत का प्रवेश-द्वार है। भारत द्वारा बनाया गया सित्तवे कोलकाता को समुद्र के रास्ते कालादान नदी और मिज़ोरम तक जाने वाली सड़क से जोड़ता है, जिससे पूर्वोत्तर को संकरे सिलीगुड़ी गलियारे से बचकर जाने वाला मार्ग मिलता है। INSTC मुंबई से बंदर अब्बास और कैस्पियन क्षेत्र होते हुए रूस तक समुद्र, रेल और सड़क को जोड़ता है।",
  "Ministry of External Affairs; Ministry of Ports, Shipping and Waterways.",
  "tr-chabahar-sittwe-instc")

S(TH, "hard", "Consider the following statements about the demographic transition theory:",
  "जनांकिकीय संक्रमण सिद्धांत के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["In its first stage, both birth rates and death rates are high.",
   "In its second stage, birth rates fall faster than death rates.",
   "In its last stage, birth rates rise sharply again."],
  ["इसकी पहली अवस्था में जन्म दर और मृत्यु दर, दोनों ऊँची होती हैं।",
   "इसकी दूसरी अवस्था में जन्म दर मृत्यु दर से अधिक तेज़ी से घटती है।",
   "इसकी अंतिम अवस्था में जन्म दर फिर तेज़ी से बढ़ती है।"],
  C3, 0,
  "Only statement 1 is correct: in a pre-industrial society high birth and death rates keep population growth slow. "
  "Statement 2 is wrong: in the second stage death rates fall first, with better food, sanitation and health care, while birth rates stay high for a time -- so population grows rapidly, as it did in India after 1951. "
  "Statement 3 is wrong: in the last stage both birth and death rates are low, and the population is stable or grows very slowly, as in much of Europe and Japan.",
  "केवल कथन 1 सही है: पूर्व-औद्योगिक समाज में ऊँची जन्म और मृत्यु दरें जनसंख्या वृद्धि को धीमा रखती हैं। "
  "कथन 2 गलत है: दूसरी अवस्था में बेहतर भोजन, स्वच्छता और स्वास्थ्य सेवाओं से पहले मृत्यु दर घटती है, जबकि जन्म दर कुछ समय तक ऊँची रहती है; इसलिए जनसंख्या तेज़ी से बढ़ती है, जैसे 1951 के बाद भारत में। "
  "कथन 3 गलत है: अंतिम अवस्था में जन्म और मृत्यु दोनों दरें कम होती हैं, और जनसंख्या स्थिर रहती है या बहुत धीरे बढ़ती है, जैसे अधिकांश यूरोप और जापान में।",
  f"{NC12F} -- The World Population: Distribution, Density and Growth.",
  "hum-demographic-transition")

S(TH, "hard", "Consider the following statements about some tribal communities of India:",
  "भारत के कुछ जनजातीय समुदायों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Onge, the Jarawa and the Sentinelese live in the Andaman Islands.",
   "The Shompen live in Lakshadweep.",
   "The Bhotias live mainly in the Rann of Kachchh."],
  ["ओंगे, जारवा और सेंटिनली अंडमान द्वीपसमूह में रहते हैं।",
   "शोम्पेन लक्षद्वीप में रहते हैं।",
   "भोटिया मुख्य रूप से कच्छ के रण में रहते हैं।"],
  C3, 0,
  "Only statement 1 is correct: these are among the Particularly Vulnerable Tribal Groups of the Andamans; the Sentinelese of North Sentinel Island still avoid all outside contact. "
  "Statement 2 is wrong: the Shompen, a hunter-gatherer group, live in the forests of Great Nicobar -- the reason their future is a central concern in the island's development project. "
  "Statement 3 is wrong: the Bhotias live in the high valleys of Uttarakhand and other Himalayan borderlands, where they traditionally moved with their flocks and traded across the passes with Tibet.",
  "केवल कथन 1 सही है: ये अंडमान के विशेष रूप से कमज़ोर जनजातीय समूहों (PVTG) में से हैं; उत्तरी सेंटिनल द्वीप के सेंटिनली आज भी बाहरी संपर्क से पूरी तरह बचते हैं। "
  "कथन 2 गलत है: शिकारी-संग्राहक समूह शोम्पेन ग्रेट निकोबार के वनों में रहते हैं; इसीलिए उस द्वीप की विकास परियोजना में उनका भविष्य एक मुख्य चिंता है। "
  "कथन 3 गलत है: भोटिया उत्तराखंड और अन्य हिमालयी सीमावर्ती क्षेत्रों की ऊँची घाटियों में रहते हैं, जहाँ वे परंपरागत रूप से अपने पशुओं के साथ घूमते थे और दर्रों के पार तिब्बत से व्यापार करते थे।",
  "Ministry of Tribal Affairs -- Particularly Vulnerable Tribal Groups.",
  "hum-tribes-andaman-nicobar-bhotia")

# ================================================================ EASY STATEMENTS (4)
S(TH, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Roads are more economical than railways for short distances.",
   "Air transport is the cheapest way to carry passengers."],
  ["कम दूरी के लिए सड़कें रेलमार्गों से अधिक किफ़ायती हैं।",
   "यात्रियों को ले जाने का सबसे सस्ता तरीक़ा वायु परिवहन है।"],
  T2, 0,
  "Only statement 1 is correct: roads cost less to build, give door-to-door service and suit small loads over short distances. Statement 2 is wrong: air transport is the fastest but also the costliest mode, because aircraft, fuel and airports are expensive; for most passengers railways and buses are far cheaper.",
  "केवल कथन 1 सही है: सड़कें बनाने में कम ख़र्च होता है, ये घर-घर तक सेवा देती हैं और कम दूरी पर छोटे भार के लिए उपयुक्त हैं। कथन 2 गलत है: वायु परिवहन सबसे तेज़ पर सबसे महँगा साधन भी है, क्योंकि विमान, ईंधन और हवाई अड्डे महँगे होते हैं; अधिकांश यात्रियों के लिए रेल और बसें कहीं सस्ती हैं।",
  f"{NC10} -- Lifelines of National Economy.",
  "tr-roads-short-air-cost-easy")

S(TH, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Tamil is the mother tongue of most people in India.",
   "Hindi is the mother tongue of the largest number of people in India."],
  ["भारत के अधिकांश लोगों की मातृभाषा तमिल है।",
   "भारत में सबसे अधिक लोगों की मातृभाषा हिंदी है।"],
  T2, 1,
  "Only statement 2 is correct: in the 2011 Census about 44 per cent of Indians reported Hindi as their mother tongue, followed by Bengali and Marathi. Statement 1 is wrong: Tamil, one of the oldest living classical languages, is the mother tongue of about 6 per cent of the population.",
  "केवल कथन 2 सही है: 2011 की जनगणना में लगभग 44 प्रतिशत भारतीयों ने हिंदी को अपनी मातृभाषा बताया, जिसके बाद बांग्ला और मराठी आती हैं। कथन 1 गलत है: सबसे पुरानी जीवित शास्त्रीय भाषाओं में से एक, तमिल, लगभग 6 प्रतिशत जनसंख्या की मातृभाषा है।",
  f"{CEN} -- Language data.",
  "hum-mother-tongues-easy")

S(TH, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Indian Railways is owned and run by the Government of India.",
   "India's railway network is among the largest in the world."],
  ["भारतीय रेल का स्वामित्व और संचालन भारत सरकार के पास है।",
   "भारत का रेल नेटवर्क विश्व के सबसे बड़े नेटवर्कों में से एक है।"],
  T2, 2,
  "Both statements are correct. Indian Railways, a department of the Ministry of Railways, runs one of the four largest networks in the world, with more than 68,000 route-km, and is among the country's largest employers.",
  "दोनों कथन सही हैं। रेल मंत्रालय का एक विभाग, भारतीय रेल, 68,000 से अधिक रूट-किमी वाला, विश्व के चार सबसे बड़े नेटवर्कों में से एक चलाती है और देश के सबसे बड़े नियोक्ताओं में से है।",
  f"{NC10} -- Lifelines of National Economy; Ministry of Railways.",
  "tr-indian-railways-easy")

S(TH, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Census of India is held every five years.",
   "The 2011 Census was India's first Census."],
  ["भारत की जनगणना हर पाँच वर्ष में होती है।",
   "2011 की जनगणना भारत की पहली जनगणना थी।"],
  T2, 3,
  "Neither statement is correct. India's Census is normally held every ten years; the first synchronous Census was taken in 1881, and 2011 was the fifteenth in the unbroken series. The next one, delayed from 2021, is due in 2027.",
  "कोई भी कथन सही नहीं है। भारत की जनगणना सामान्यतः हर दस वर्ष में होती है; पहली समकालिक जनगणना 1881 में हुई थी, और 2011 की जनगणना इस अटूट श्रृंखला में पंद्रहवीं थी। 2021 से टली अगली जनगणना 2027 में होनी है।",
  f"{CEN}; Office of the Registrar General and Census Commissioner.",
  "hum-census-decennial-easy")

# ================================================================ MCQs (medium 7, hard 3, easy 2)
M(TH, "medium", "The Salaya-Mathura pipeline carries:",
  "सलाया-मथुरा पाइपलाइन क्या ले जाती है?",
  ["Crude oil", "Natural gas", "Liquefied petroleum gas", "Iron ore slurry"],
  ["कच्चा तेल", "प्राकृतिक गैस", "द्रवीकृत पेट्रोलियम गैस", "लौह अयस्क घोल (स्लरी)"],
  0,
  "The Salaya-Mathura pipeline of Indian Oil carries imported crude from the Gulf of Kachchh coast in Gujarat to refineries at Koyali, Panipat and Mathura. Natural gas moves through lines such as HVJ, and iron ore slurry is carried by dedicated pipelines, for example from Bailadila to Visakhapatnam.",
  "इंडियन ऑयल की सलाया-मथुरा पाइपलाइन गुजरात में कच्छ की खाड़ी के तट से आयातित कच्चे तेल को कोयली, पानीपत और मथुरा की रिफ़ाइनरियों तक ले जाती है। प्राकृतिक गैस HVJ जैसी लाइनों से जाती है, और लौह अयस्क का घोल समर्पित पाइपलाइनों से, जैसे बैलाडीला से विशाखापत्तनम तक, ले जाया जाता है।",
  f"{NC12I} -- Transport and Communication.",
  "tr-salaya-mathura-crude")

M(TH, "medium", "According to the 2011 Census, which one of the following States had the lowest sex ratio?",
  "2011 की जनगणना के अनुसार निम्नलिखित में से किस राज्य का लिंगानुपात सबसे कम था?",
  ["Haryana", "Punjab", "Rajasthan", "Uttar Pradesh"],
  ["हरियाणा", "पंजाब", "राजस्थान", "उत्तर प्रदेश"],
  0,
  "Haryana had 879 women per 1,000 men, the lowest among the States, and an even lower child sex ratio -- which is why the 'Beti Bachao Beti Padhao' campaign was launched from Panipat in 2015. Punjab (895), Uttar Pradesh (912) and Rajasthan (928) were also below the national 943.",
  "हरियाणा में प्रति 1,000 पुरुषों पर 879 महिलाएँ थीं, जो राज्यों में सबसे कम था, और बाल लिंगानुपात इससे भी कम था; इसीलिए 2015 में 'बेटी बचाओ बेटी पढ़ाओ' अभियान पानीपत से शुरू किया गया। पंजाब (895), उत्तर प्रदेश (912) और राजस्थान (928) भी राष्ट्रीय 943 से नीचे थे।",
  f"{CEN} -- Primary Census Abstract.",
  "hum-lowest-sex-ratio-haryana")

M(TH, "medium", "The Maasai, a pastoral people known for herding cattle, live mainly in:",
  "पशुपालन के लिए जाने जाने वाले चरवाहा लोग, मसाई, मुख्य रूप से कहाँ रहते हैं?",
  ["Kenya and Tanzania", "Nigeria and Niger", "Morocco and Algeria", "Namibia and Botswana"],
  ["केन्या और तंज़ानिया", "नाइजीरिया और नाइजर", "मोरक्को और अल्जीरिया", "नामीबिया और बोत्सवाना"],
  0,
  "The Maasai graze their cattle on the savannas of southern Kenya and northern Tanzania, around the Serengeti and the Rift Valley, measuring wealth in cattle. The San (Bushmen) of the Kalahari live in Namibia and Botswana, and the Tuareg and Berbers in the Sahara and the Atlas.",
  "मसाई दक्षिणी केन्या और उत्तरी तंज़ानिया के सवाना में, सेरेंगेटी और भ्रंश घाटी के आसपास, अपने मवेशी चराते हैं और धन को मवेशियों से मापते हैं। कालाहारी के सान (बुशमैन) नामीबिया और बोत्सवाना में, और तुआरेग तथा बर्बर सहारा और एटलस में रहते हैं।",
  f"{NC12F} -- Primary Activities.",
  "hum-maasai-kenya-tanzania")

M(TH, "medium", "The UDAN scheme of the Government of India is related to:",
  "भारत सरकार की 'उड़ान' (UDAN) योजना किससे संबंधित है?",
  ["regional air connectivity", "rural road connectivity", "inland water transport", "electrification of railway lines"],
  ["क्षेत्रीय हवाई संपर्क", "ग्रामीण सड़क संपर्क", "अंतर्देशीय जल परिवहन", "रेल लाइनों का विद्युतीकरण"],
  0,
  "UDAN -- 'Ude Desh ka Aam Nagrik', launched in 2016 -- links under-served airports, heliports and water aerodromes with capped fares, supported by viability gap funding, so that people in smaller towns can afford to fly. Rural roads are the subject of the Pradhan Mantri Gram Sadak Yojana.",
  "2016 में शुरू की गई 'उड़े देश का आम नागरिक' (उड़ान) योजना सीमित किराए के साथ कम सेवा वाले हवाई अड्डों, हेलीपोर्ट और जल-हवाई अड्डों को जोड़ती है, जिसमें व्यवहार्यता अंतर वित्तपोषण (viability gap funding) से सहायता मिलती है, ताकि छोटे शहरों के लोग भी हवाई यात्रा कर सकें। ग्रामीण सड़कें प्रधानमंत्री ग्राम सड़क योजना का विषय हैं।",
  "Ministry of Civil Aviation -- Regional Connectivity Scheme (UDAN).",
  "tr-udan-regional-air")

M(TH, "medium", "Which one of the following is the busiest airport in India by passenger traffic?",
  "यात्री यातायात के अनुसार निम्नलिखित में से कौन-सा भारत का सबसे व्यस्त हवाई अड्डा है?",
  ["Indira Gandhi International Airport, Delhi", "Chhatrapati Shivaji Maharaj International Airport, Mumbai",
   "Kempegowda International Airport, Bengaluru", "Rajiv Gandhi International Airport, Hyderabad"],
  ["इंदिरा गांधी अंतरराष्ट्रीय हवाई अड्डा, दिल्ली", "छत्रपति शिवाजी महाराज अंतरराष्ट्रीय हवाई अड्डा, मुंबई",
   "केम्पेगौड़ा अंतरराष्ट्रीय हवाई अड्डा, बेंगलुरु", "राजीव गांधी अंतरराष्ट्रीय हवाई अड्डा, हैदराबाद"],
  0,
  "Delhi's Indira Gandhi International Airport handles the most passengers in India -- more than 70 million a year -- and ranks among the busiest airports in the world; Mumbai is second, followed by Bengaluru and Hyderabad.",
  "दिल्ली का इंदिरा गांधी अंतरराष्ट्रीय हवाई अड्डा भारत में सबसे अधिक यात्रियों को संभालता है, वर्ष में 7 करोड़ से अधिक, और विश्व के सबसे व्यस्त हवाई अड्डों में गिना जाता है; मुंबई दूसरे स्थान पर है, जिसके बाद बेंगलुरु और हैदराबाद आते हैं।",
  "Airports Authority of India -- traffic statistics.",
  "tr-busiest-airport-delhi")

M(TH, "medium", "The Sagarmala programme is concerned with:",
  "सागरमाला कार्यक्रम किससे संबंधित है?",
  ["port-led development", "building national highways", "interlinking of rivers", "rural housing"],
  ["बंदरगाह-आधारित विकास", "राष्ट्रीय राजमार्गों का निर्माण", "नदियों को जोड़ना", "ग्रामीण आवास"],
  0,
  "Sagarmala, launched in 2015, aims at port-led development: modernising ports, linking them to the hinterland by road, rail and waterways, promoting coastal shipping and coastal economic zones, and developing coastal communities. National highways come under Bharatmala.",
  "2015 में शुरू किए गए सागरमाला का उद्देश्य बंदरगाह-आधारित विकास है: बंदरगाहों का आधुनिकीकरण, उन्हें सड़क, रेल और जलमार्गों से भीतरी भागों से जोड़ना, तटीय नौवहन और तटीय आर्थिक क्षेत्रों को बढ़ावा देना, और तटीय समुदायों का विकास। राष्ट्रीय राजमार्ग भारतमाला के अंतर्गत आते हैं।",
  f"{MOPSW} -- Sagarmala Programme.",
  "tr-sagarmala")

M(TH, "medium", "Which one of the following communities follows a matrilineal system of inheritance?",
  "निम्नलिखित में से कौन-सा समुदाय उत्तराधिकार की मातृवंशीय (matrilineal) व्यवस्था का पालन करता है?",
  ["Khasi", "Bhil", "Gond", "Santhal"],
  ["खासी", "भील", "गोंड", "संथाल"],
  0,
  "Among the Khasi, as among the Garo of Meghalaya, descent is traced through the mother, children take the mother's clan name and the youngest daughter (khadduh) traditionally inherits the family property. The Bhils, Gonds and Santhals, among India's largest tribes, are patrilineal.",
  "खासी में, मेघालय के गारो की तरह, वंश माता से गिना जाता है, बच्चे माँ के कुल का नाम लेते हैं और परंपरागत रूप से सबसे छोटी बेटी (खद्दुह) पारिवारिक संपत्ति की उत्तराधिकारी होती है। भारत की सबसे बड़ी जनजातियों में शामिल भील, गोंड और संथाल पितृवंशीय हैं।",
  "Ministry of Tribal Affairs; Government of Meghalaya.",
  "hum-khasi-matrilineal")

M(TH, "hard", "The eastern coast of India has fewer natural harbours than the western coast. Which one of the following best explains this?",
  "भारत के पूर्वी तट पर पश्चिमी तट की तुलना में कम प्राकृतिक बंदरगाह हैं। निम्नलिखित में से कौन-सा इसकी सबसे अच्छी व्याख्या करता है?",
  ["It is an emergent coast with a wide continental shelf that keeps deep water far out",
   "It receives far less rainfall than the west coast, so its rivers carry too little water for ports",
   "It is a submerged coast whose drowned valleys are too deep for ships to anchor",
   "It lies in the rain shadow of the Eastern Ghats and so has no harbour towns"],
  ["यह एक उभरा हुआ (emergent) तट है, जिसकी चौड़ी महाद्वीपीय मग्नतट गहरे जल को दूर रखती है",
   "यहाँ पश्चिमी तट से बहुत कम वर्षा होती है, इसलिए इसकी नदियों में बंदरगाहों के लिए बहुत कम जल होता है",
   "यह एक निमज्जित तट है, जिसकी डूबी घाटियाँ जहाज़ों के लंगर डालने के लिए बहुत गहरी हैं",
   "यह पूर्वी घाट के वृष्टि-छाया क्षेत्र में है, इसलिए यहाँ कोई बंदरगाह नगर नहीं है"],
  0,
  "The eastern coastal plain has emerged from the sea: its smooth, straight shore and a continental shelf up to about 500 km wide mean shallow water far offshore, so ports such as Chennai and Paradip had to be built with breakwaters and dredged channels. The western coast is the submerged one, whose indented shoreline gives natural harbours such as Mumbai and Mormugao. The 'submerged coast' option reverses the two coasts, and the east coast in fact gets heavy rain from the north-east monsoon and cyclones.",
  "पूर्वी तटीय मैदान समुद्र से उभरा है: इसकी चिकनी, सीधी तटरेखा और लगभग 500 किमी तक चौड़ी महाद्वीपीय मग्नतट का अर्थ है कि दूर तक जल उथला रहता है, इसलिए चेन्नई और पारादीप जैसे बंदरगाह तरंग-रोधकों (breakwaters) और तलकर्षित नहरों के साथ बनाने पड़े। निमज्जित तट पश्चिमी है, जिसकी कटी-फटी तटरेखा मुंबई और मोरमुगाओ जैसे प्राकृतिक बंदरगाह देती है। 'निमज्जित तट' वाला विकल्प दोनों तटों को उलट देता है, और पूर्वी तट पर वास्तव में उत्तर-पूर्वी मानसून और चक्रवातों से भारी वर्षा होती है।",
  "NCERT Class XI, India: Physical Environment -- Structure and Physiography; " + NC12I + " -- International Trade.",
  "tr-east-coast-fewer-harbours")

M(TH, "hard", "Building the Konkan Railway was an engineering challenge mainly because:",
  "कोंकण रेलवे का निर्माण मुख्य रूप से किस कारण एक इंजीनियरिंग चुनौती था?",
  ["it had to cross many rivers and cut through the steep, rocky slopes of the Western Ghats",
   "it runs through the Thar desert, where shifting sand dunes keep burying the track",
   "it passes over permafrost that thaws every summer and makes the ground collapse",
   "it crosses the main Himalayan thrust, the most earthquake-prone zone in the country, many times over"],
  ["इसे कई नदियाँ पार करनी थीं और पश्चिमी घाट की खड़ी, चट्टानी ढलानों को काटना था",
   "यह थार मरुस्थल से होकर जाती है, जहाँ खिसकते टीले पटरी को बार-बार दबा देते हैं",
   "यह ऐसे स्थायी तुषार (permafrost) पर से गुज़रती है जो हर गर्मी में पिघलकर ज़मीन धँसा देता है",
   "यह देश के सबसे अधिक भूकंप-प्रवण क्षेत्र, मुख्य हिमालयी भ्रंश, को कई बार पार करती है"],
  0,
  "The Konkan Railway, about 740 km from Roha in Maharashtra through Goa to Thokur near Mangaluru, opened in 1998. Running along the foot of the Western Ghats, it needed some 2,000 bridges and 91 tunnels, and parts of it still suffer landslides and boulder falls in the monsoon. It was built by a corporation jointly owned by the Railways and the States of Maharashtra, Goa, Karnataka and Kerala.",
  "महाराष्ट्र के रोहा से गोवा होते हुए मंगलुरु के पास ठोकुर तक लगभग 740 किमी लंबी कोंकण रेलवे 1998 में खुली। पश्चिमी घाट की तलहटी के साथ चलने वाली इस लाइन के लिए लगभग 2,000 पुल और 91 सुरंगें बनानी पड़ीं, और इसके कुछ भाग मानसून में आज भी भूस्खलनों और चट्टानें गिरने से प्रभावित होते हैं। इसे रेलवे तथा महाराष्ट्र, गोवा, कर्नाटक और केरल राज्यों के संयुक्त स्वामित्व वाले एक निगम ने बनाया।",
  f"{NC10} -- Lifelines of National Economy; Konkan Railway Corporation.",
  "tr-konkan-railway-challenge")

M(TH, "hard", "The term 'demographic dividend' refers to:",
  "'जनांकिकीय लाभांश' (demographic dividend) शब्द किसे दर्शाता है?",
  ["the economic boost possible when the working-age share of the population is large",
   "the extra revenue a government earns from conducting a population census",
   "the rise in birth rates that follows a long period of economic prosperity",
   "the incentive paid by the Centre to States that bring down their population growth"],
  ["वह आर्थिक उछाल जो जनसंख्या में कार्यशील आयु वर्ग का हिस्सा बड़ा होने पर संभव होता है",
   "जनगणना कराने से सरकार को होने वाली अतिरिक्त आय",
   "लंबी आर्थिक समृद्धि के बाद आने वाली जन्म दर में वृद्धि",
   "जनसंख्या वृद्धि घटाने वाले राज्यों को केंद्र द्वारा दिया जाने वाला प्रोत्साहन"],
  0,
  "When birth rates fall after death rates have already fallen, for some decades the share of people aged about 15-64 rises and the share of dependants falls; if these workers are educated, healthy and employed, output and savings can grow fast, as happened in East Asia. India's working-age share is expected to stay high until around the 2040s, so the dividend is an opportunity, not an automatic gain.",
  "जब मृत्यु दर पहले ही घट चुकी हो और फिर जन्म दर भी घटे, तो कुछ दशकों तक लगभग 15-64 आयु के लोगों का हिस्सा बढ़ता है और आश्रितों का हिस्सा घटता है; यदि ये कामगार शिक्षित, स्वस्थ और रोज़गार में हों, तो उत्पादन और बचत तेज़ी से बढ़ सकती है, जैसा पूर्वी एशिया में हुआ। भारत में कार्यशील आयु वर्ग का हिस्सा लगभग 2040 के दशक तक ऊँचा रहने की आशा है, इसलिए यह लाभांश एक अवसर है, अपने-आप मिलने वाला लाभ नहीं।",
  f"{NC12F} -- Population Composition; United Nations Population Fund.",
  "hum-demographic-dividend")

M(TH, "easy", "The Golden Quadrilateral is a network of:",
  "स्वर्णिम चतुर्भुज (Golden Quadrilateral) किसका नेटवर्क है?",
  ["highways", "railway lines", "gas pipelines", "inland waterways"],
  ["राजमार्ग", "रेल लाइनें", "गैस पाइपलाइनें", "अंतर्देशीय जलमार्ग"],
  0,
  "The Golden Quadrilateral, built by the National Highways Authority of India under the National Highways Development Project from 1999, is a network of four- and six-lane highways linking the four metropolitan cities of Delhi, Mumbai, Chennai and Kolkata.",
  "1999 से राष्ट्रीय राजमार्ग विकास परियोजना के तहत भारतीय राष्ट्रीय राजमार्ग प्राधिकरण द्वारा बनाया गया स्वर्णिम चतुर्भुज चार और छह लेन वाले राजमार्गों का नेटवर्क है, जो चार महानगरों, दिल्ली, मुंबई, चेन्नई और कोलकाता, को जोड़ता है।",
  f"{NC10} -- Lifelines of National Economy.",
  "tr-golden-quadrilateral-easy")

M(TH, "easy", "Which one of the following is generally the cheapest means of transporting heavy and bulky goods?",
  "भारी और भारी-भरकम माल ढोने का सामान्यतः सबसे सस्ता साधन निम्नलिखित में से कौन-सा है?",
  ["Waterways", "Airways", "Roadways", "Mountain ropeways"],
  ["जलमार्ग", "वायुमार्ग", "सड़क मार्ग", "पहाड़ी रज्जुमार्ग (रोपवे)"],
  0,
  "Ships and barges carry very large loads with little fuel per tonne-kilometre and need no track or road to be built on the water itself, so waterways are the cheapest means for heavy, bulky cargo such as coal, ore and containers; air transport is the costliest.",
  "जहाज़ और बजरे प्रति टन-किलोमीटर बहुत कम ईंधन में बहुत भारी माल ले जाते हैं, और जल पर कोई पटरी या सड़क नहीं बनानी पड़ती, इसलिए कोयला, अयस्क और कंटेनर जैसे भारी, भारी-भरकम माल के लिए जलमार्ग सबसे सस्ते हैं; वायु परिवहन सबसे महँगा है।",
  f"{NC10} -- Lifelines of National Economy.",
  "tr-waterways-cheapest-easy")

# ================================================================ STATEMENT-I/II (medium 5, easy 2, hard 1 + I/II/III 1)
A(TH, "medium",
  "Railway density is low in the Himalayan and north-eastern hill regions.",
  "हिमालयी और पूर्वोत्तर पहाड़ी क्षेत्रों में रेलमार्गों का घनत्व कम है।",
  "Rugged relief, sparse population and high construction costs make railways difficult to build there.",
  "ऊबड़-खाबड़ भू-भाग, विरल जनसंख्या और निर्माण की ऊँची लागत वहाँ रेलमार्ग बनाना कठिन बनाते हैं।",
  0,
  "Both statements are correct and Statement-II explains Statement-I. Railways need gentle gradients, so every mountain line needs tunnels, bridges and loops; with few people and little freight, the cost could rarely be recovered. Only recently have strategic lines -- to Kashmir, and to the capitals of the north-eastern States -- been pushed through.",
  "दोनों कथन सही हैं और कथन-II कथन-I की व्याख्या करता है। रेलमार्गों को हल्की ढलान चाहिए, इसलिए हर पहाड़ी लाइन के लिए सुरंगें, पुल और घुमाव बनाने पड़ते हैं; कम लोग और कम माल होने से यह लागत शायद ही वसूल हो पाती थी। हाल में ही सामरिक लाइनें, कश्मीर तक और पूर्वोत्तर राज्यों की राजधानियों तक, आगे बढ़ाई गई हैं।",
  f"{NC10} -- Lifelines of National Economy.",
  "tr-railway-density-hills")

A(TH, "medium",
  "Bihar had the lowest literacy rate among the States in the 2011 Census.",
  "2011 की जनगणना में राज्यों में बिहार की साक्षरता दर सबसे कम थी।",
  "Bihar had the highest population density among the States in the 2011 Census.",
  "2011 की जनगणना में राज्यों में बिहार का जनसंख्या घनत्व सबसे अधिक था।",
  1,
  "Both statements are correct, but Statement-II does not explain Statement-I. Bihar's literacy rate was about 62 per cent against a national 74, and its density about 1,106 persons per sq km. Density does not cause low literacy: Kerala, also densely peopled, had the highest literacy (about 94 per cent), so the causes lie in poverty, schooling and gender gaps.",
  "दोनों कथन सही हैं, पर कथन-II कथन-I की व्याख्या नहीं करता। राष्ट्रीय 74 प्रतिशत के मुक़ाबले बिहार की साक्षरता दर लगभग 62 प्रतिशत थी, और उसका घनत्व लगभग 1,106 व्यक्ति प्रति वर्ग किमी। घनत्व कम साक्षरता का कारण नहीं है: घनी आबादी वाले केरल की साक्षरता सबसे अधिक (लगभग 94 प्रतिशत) थी, इसलिए कारण ग़रीबी, स्कूली शिक्षा और लैंगिक अंतर में हैं।",
  f"{CEN} -- Primary Census Abstract.",
  "hum-bihar-literacy-density")

A(TH, "medium",
  "Pipelines are an efficient way to move oil and gas over long distances.",
  "लंबी दूरी तक तेल और गैस ले जाने का पाइपलाइन एक कुशल तरीक़ा है।",
  "Pipelines cannot be laid across rivers or under the sea.",
  "पाइपलाइनें नदियों के आर-पार या समुद्र के नीचे नहीं बिछाई जा सकतीं।",
  2,
  "Statement-I is correct but Statement-II is incorrect. Once laid, pipelines move fluids continuously with low running costs and little loss. They can be carried across rivers and laid on the sea bed -- the gas from Mumbai High reaches the mainland at Uran by undersea pipeline, and the Nord Stream lines ran under the Baltic.",
  "कथन-I सही है पर कथन-II गलत है। एक बार बिछ जाने पर पाइपलाइनें कम परिचालन लागत और कम हानि के साथ तरल पदार्थों को लगातार ले जाती हैं। इन्हें नदियों के आर-पार भी ले जाया जा सकता है और समुद्र तल पर भी बिछाया जा सकता है; मुंबई हाई की गैस समुद्र के नीचे की पाइपलाइन से उरण में मुख्य भूमि तक पहुँचती है, और नॉर्ड स्ट्रीम लाइनें बाल्टिक के नीचे से जाती थीं।",
  f"{NC12I} -- Transport and Communication.",
  "tr-pipelines-undersea")

A(TH, "medium",
  "Most of India's population lives in urban areas.",
  "भारत की अधिकांश जनसंख्या नगरीय क्षेत्रों में रहती है।",
  "The share of India's population living in urban areas has been rising over the decades.",
  "दशकों से भारत की नगरीय क्षेत्रों में रहने वाली जनसंख्या का हिस्सा बढ़ता रहा है।",
  3,
  "Statement-I is incorrect but Statement-II is correct. The urban share rose from about 17 per cent in 1951 to about 31 per cent in 2011 and has continued to rise, but most Indians still live in villages -- far below the urban share of China or Brazil.",
  "कथन-I गलत है पर कथन-II सही है। नगरीय हिस्सा 1951 के लगभग 17 प्रतिशत से बढ़कर 2011 में लगभग 31 प्रतिशत हो गया और आगे भी बढ़ता रहा है, पर अधिकांश भारतीय अब भी गाँवों में रहते हैं; यह चीन या ब्राज़ील के नगरीय हिस्से से बहुत कम है।",
  f"{CEN}; {NC12I} -- Population.",
  "hum-urban-share-rising")

A(TH, "medium",
  "Villages in the Thar desert are often compact, clustered around a source of water.",
  "थार मरुस्थल के गाँव प्रायः सघन होते हैं और किसी जल स्रोत के आसपास बसे होते हैं।",
  "Water is scarce in the Thar and available at only a few places.",
  "थार में जल दुर्लभ है और केवल कुछ ही स्थानों पर उपलब्ध है।",
  0,
  "Both statements are correct and Statement-II explains Statement-I. Settlements gather round wells, tanks and ponds -- the 'kunds' and 'tankas' of Rajasthan -- because a household cannot live far from the only water available, and pooling labour to maintain these sources adds to the pull.",
  "दोनों कथन सही हैं और कथन-II कथन-I की व्याख्या करता है। बस्तियाँ कुओं, तालाबों और जोहड़ों, यानी राजस्थान के 'कुंडों' और 'टाँकों', के आसपास बसती हैं, क्योंकि कोई परिवार उपलब्ध एकमात्र जल से दूर नहीं रह सकता, और इन स्रोतों के रखरखाव के लिए सामूहिक श्रम भी लोगों को पास लाता है।",
  f"{NC12I} -- Human Settlements.",
  "hum-thar-clustered-villages")

A(TH, "easy",
  "Air transport is very useful in the north-eastern States.",
  "पूर्वोत्तर राज्यों में वायु परिवहन बहुत उपयोगी है।",
  "Air transport in India was nationalised in 1953.",
  "भारत में वायु परिवहन का 1953 में राष्ट्रीयकरण किया गया।",
  1,
  "Both statements are correct, but Statement-II does not explain Statement-I. Air transport matters in the north-east because big rivers, dissected hills, dense forests, frequent floods and international frontiers make surface travel slow and difficult. The nationalisation of 1953 is a fact about ownership, not about why flying suits the region.",
  "दोनों कथन सही हैं, पर कथन-II कथन-I की व्याख्या नहीं करता। पूर्वोत्तर में वायु परिवहन इसलिए महत्त्वपूर्ण है कि बड़ी नदियाँ, कटी-फटी पहाड़ियाँ, घने वन, बार-बार बाढ़ और अंतरराष्ट्रीय सीमाएँ सतही यात्रा को धीमा और कठिन बनाती हैं। 1953 का राष्ट्रीयकरण स्वामित्व से जुड़ा तथ्य है, इस बात से नहीं कि हवाई यात्रा उस क्षेत्र के अनुकूल क्यों है।",
  f"{NC10} -- Lifelines of National Economy.",
  "tr-air-transport-north-east-easy")

A(TH, "easy",
  "Mumbai is a major port on the western coast of India.",
  "मुंबई भारत के पश्चिमी तट पर एक बड़ा बंदरगाह है।",
  "Mumbai lies on the Bay of Bengal.",
  "मुंबई बंगाल की खाड़ी पर स्थित है।",
  2,
  "Statement-I is correct but Statement-II is incorrect. Mumbai lies on the Arabian Sea; its spacious natural harbour made it the country's leading port for a century, and Jawaharlal Nehru Port was later built across the harbour to share the load.",
  "कथन-I सही है पर कथन-II गलत है। मुंबई अरब सागर पर है; इसके विशाल प्राकृतिक बंदरगाह ने इसे एक सदी तक देश का प्रमुख बंदरगाह बनाए रखा, और बाद में भार बाँटने के लिए बंदरगाह के उस पार जवाहरलाल नेहरू बंदरगाह बनाया गया।",
  f"{NC10} -- Lifelines of National Economy.",
  "tr-mumbai-port-easy")

A(TH, "hard",
  "The Gaddis of Himachal Pradesh practise transhumance.",
  "हिमाचल प्रदेश के गद्दी ऋतु-प्रवास (transhumance) करते हैं।",
  "Transhumance means the permanent migration of farming families to cities.",
  "ऋतु-प्रवास का अर्थ है किसान परिवारों का शहरों की ओर स्थायी प्रवास।",
  2,
  "Statement-I is correct but Statement-II is incorrect. Transhumance is the seasonal movement of herders and their flocks -- up to high alpine pastures in summer and down to the valleys and plains in winter. The Gaddis of the Dhauladhar, like the Gujjars and Bakarwals of Jammu and Kashmir and the Bhotias of Uttarakhand, have long followed this cycle.",
  "कथन-I सही है पर कथन-II गलत है। ऋतु-प्रवास चरवाहों और उनके झुंडों का मौसमी आवागमन है, यानी गर्मियों में ऊँचे अल्पाइन चरागाहों तक और सर्दियों में घाटियों और मैदानों तक। धौलाधार के गद्दी, जम्मू-कश्मीर के गुज्जरों और बकरवालों तथा उत्तराखंड के भोटियों की तरह, लंबे समय से इस चक्र का पालन करते आए हैं।",
  f"{NC12F} -- Primary Activities.",
  "hum-gaddi-transhumance")

A(TH, "hard",
  "Population density is very high in the Ganga plains.",
  "गंगा के मैदानों में जनसंख्या घनत्व बहुत अधिक है।",
  "The Ganga plains receive less rainfall than any other part of India.",
  "गंगा के मैदानों में भारत के किसी भी अन्य भाग से कम वर्षा होती है।",
  3,
  "Neither Statement II nor Statement III is correct. The plains are densely peopled because deep, fertile alluvium, level land, abundant surface and groundwater and a long history of settled farming have supported large populations for thousands of years. "
  "Statement II is wrong: the plains get moderate to heavy monsoon rain -- the driest parts of India are western Rajasthan and Ladakh. Statement III is wrong: the plains were cleared for farming over many centuries and are now among the least forested parts of India.",
  "कथन II और III में से कोई भी सही नहीं है। मैदान इसलिए घनी आबादी वाले हैं कि गहरी, उपजाऊ जलोढ़ मिट्टी, समतल भूमि, भरपूर सतही और भूजल तथा स्थायी खेती के लंबे इतिहास ने हज़ारों वर्षों से बड़ी जनसंख्या को सहारा दिया है। "
  "कथन II गलत है: मैदानों में मध्यम से भारी मानसूनी वर्षा होती है; भारत के सबसे शुष्क भाग पश्चिमी राजस्थान और लद्दाख हैं। कथन III गलत है: कई शताब्दियों में खेती के लिए मैदानों के वन साफ़ किए गए, और अब ये भारत के सबसे कम वन वाले भागों में से हैं।",
  f"{NC12I} -- Population: Distribution, Density, Growth and Composition.",
  "hum-ganga-plains-density",
  s3="Most of the Ganga plains are covered by dense natural forest.",
  s3_hi="गंगा के मैदानों का अधिकांश भाग घने प्राकृतिक वनों से ढका है।")

# ================================================================ PAIRS (medium 2, hard 1)
P(TH, "medium", "Consider the following pairs of tribal communities and the areas where they live:",
  "जनजातीय समुदायों और उनके निवास क्षेत्रों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Toda : Nilgiri hills", "Apatani : Ziro valley", "Chenchu : Nallamala hills", "Dongria Kondh : Western Ghats of Kerala"],
  ["टोडा : नीलगिरि पहाड़ियाँ", "अपातानी : ज़ीरो घाटी", "चेंचू : नल्लामला पहाड़ियाँ", "डोंगरिया कोंध : केरल के पश्चिमी घाट"],
  2,
  "Pairs 1, 2 and 3 are correct: the pastoral Todas keep buffaloes in the Nilgiris; the Apatani of Arunachal Pradesh are known for wet-rice cultivation combined with fish farming in the Ziro valley; and the Chenchus are forest-dwelling hunter-gatherers of the Nallamala hills of Andhra Pradesh and Telangana. "
  "Pair 4 is wrong: the Dongria Kondh live in the Niyamgiri hills of Odisha, where their gram sabhas rejected bauxite mining in 2013.",
  "युग्म 1, 2 और 3 सही हैं: चरवाहे टोडा नीलगिरि में भैंसें पालते हैं; अरुणाचल प्रदेश के अपातानी ज़ीरो घाटी में मछली पालन के साथ गीली धान की खेती के लिए जाने जाते हैं; और चेंचू आंध्र प्रदेश और तेलंगाना की नल्लामला पहाड़ियों के वनवासी शिकारी-संग्राहक हैं। "
  "युग्म 4 गलत है: डोंगरिया कोंध ओडिशा की नियमगिरि पहाड़ियों में रहते हैं, जहाँ उनकी ग्राम सभाओं ने 2013 में बॉक्साइट खनन को अस्वीकार कर दिया।",
  "Ministry of Tribal Affairs.",
  "hum-tribes-regions-pairs")

P(TH, "medium", "Consider the following pairs of ports and the States in which they are located:",
  "बंदरगाहों और उन राज्यों के निम्नलिखित युग्मों पर विचार कीजिए जिनमें वे स्थित हैं:",
  ["V.O. Chidambaranar (Thoothukudi) : Tamil Nadu", "New Mangalore : Karnataka", "Haldia : West Bengal", "Ennore : Andhra Pradesh"],
  ["वी.ओ. चिदंबरनार (थूथुकुडी) : तमिलनाडु", "न्यू मंगलौर : कर्नाटक", "हल्दिया : पश्चिम बंगाल", "एन्नोर : आंध्र प्रदेश"],
  2,
  "Pairs 1, 2 and 3 are correct: V.O. Chidambaranar port at Thoothukudi serves southern Tamil Nadu and trade with Sri Lanka; New Mangalore lies on the Karnataka coast; and Haldia, downstream on the Hooghly, is the dock system of Kolkata port. "
  "Pair 4 is wrong: Ennore (Kamarajar port) lies just north of Chennai in Tamil Nadu.",
  "युग्म 1, 2 और 3 सही हैं: थूथुकुडी का वी.ओ. चिदंबरनार बंदरगाह दक्षिणी तमिलनाडु और श्रीलंका के साथ व्यापार को सेवा देता है; न्यू मंगलौर कर्नाटक तट पर है; और हुगली पर नीचे की ओर स्थित हल्दिया कोलकाता बंदरगाह की गोदी प्रणाली है। "
  "युग्म 4 गलत है: एन्नोर (कामराजर बंदरगाह) तमिलनाडु में चेन्नई के ठीक उत्तर में है।",
  f"{MOPSW} -- Major ports.",
  "tr-ports-states-pairs")

P(TH, "hard", "Consider the following pairs of peoples and the regions where they traditionally live:",
  "लोगों (समुदायों) और उनके परंपरागत निवास क्षेत्रों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Inuit : Arctic lands of Canada and Greenland", "Pygmies : Congo basin", "Sami : Siberia", "Yanomami : Sahara"],
  ["इनुइट : कनाडा और ग्रीनलैंड के आर्कटिक क्षेत्र", "पिग्मी : कांगो बेसिन", "सामी : साइबेरिया", "यानोमामी : सहारा"],
  1,
  "Pairs 1 and 2 are correct: the Inuit have long lived by hunting seals, whales and caribou in the Arctic, and the forest-dwelling peoples called Pygmies hunt and gather in the rainforests of the Congo basin. "
  "Pair 3 is wrong: the Sami (Lapps), known for reindeer herding, live in the far north of Norway, Sweden and Finland and the Kola peninsula of Russia -- not Siberia. "
  "Pair 4 is wrong: the Yanomami live in the Amazon rainforest on the Brazil-Venezuela border; the peoples of the Sahara include the Tuareg and the Bedouin.",
  "युग्म 1 और 2 सही हैं: इनुइट लंबे समय से आर्कटिक में सील, व्हेल और कैरिबू का शिकार करके जीते आए हैं, और पिग्मी कहलाने वाले वनवासी लोग कांगो बेसिन के वर्षावनों में शिकार और संग्रह करते हैं। "
  "युग्म 3 गलत है: बारहसिंगा (रेनडियर) पालन के लिए जाने जाने वाले सामी (लैप्स) नॉर्वे, स्वीडन और फ़िनलैंड के सुदूर उत्तर तथा रूस के कोला प्रायद्वीप में रहते हैं, साइबेरिया में नहीं। "
  "युग्म 4 गलत है: यानोमामी ब्राज़ील-वेनेज़ुएला सीमा पर अमेज़न वर्षावन में रहते हैं; सहारा के लोगों में तुआरेग और बद्दू (बेदुइन) हैं।",
  f"{NC12F} -- Primary Activities.",
  "hum-world-peoples-pairs")

if __name__ == "__main__":
    write("geo_l2_t14_transport_human.sql")
