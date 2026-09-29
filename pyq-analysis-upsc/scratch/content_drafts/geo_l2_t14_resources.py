# -*- coding: utf-8 -*-
"""Level 2 · Test 14 (Geography 3: Human & Economic Geography) -- Resources: Minerals, Energy & Agriculture:
50 new bilingual rows against the live gap report: medium statement 15, medium MCQ 7, easy statement 5,
hard statement 5, medium Statement-I/II 5, hard MCQ 3, easy MCQ 2, easy Statement-I/II 2, hard
Statement-I/II 1 + I/II/III 1, medium pairs 2, easy pairs 1, hard pairs 1.
The Environment tests already hold the International Solar Alliance, PM Surya Ghar, PM-KUSUM, green and
other 'colours' of hydrogen, fly ash, rare earths, rice-paddy methane and virtual water, so those are
left alone; Test 13 holds soils and the Tehri, Bhakra and Nagarjuna Sagar dams."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Geography"
RS = "Resources: Minerals, Energy & Agriculture"
NC10 = "NCERT Class X, Contemporary India II"
NC12I = "NCERT Class XII, India: People and Economy"
NC12F = "NCERT Class XII, Fundamentals of Human Geography"

# ================================================================ MEDIUM STATEMENTS (15)
S(RS, "medium", "Consider the following statements about coal in India:",
  "भारत में कोयले के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Most of India's coal reserves are of Gondwana age.",
   "Tertiary coal is found mainly in the north-eastern States.",
   "Anthracite is the most abundant type of coal in India."],
  ["भारत के अधिकांश कोयला भंडार गोंडवाना युग के हैं।",
   "टर्शियरी कोयला मुख्य रूप से पूर्वोत्तर राज्यों में पाया जाता है।",
   "एन्थ्रेसाइट भारत में सबसे प्रचुर प्रकार का कोयला है।"],
  C3, 1,
  "Statements 1 and 2 are correct. About 98 per cent of India's coal lies in Gondwana formations, a little over 200 million years old, in the valleys of the Damodar, the Mahanadi, the Godavari and the Son; younger tertiary coal occurs in Assam, Meghalaya, Arunachal Pradesh and Nagaland. "
  "Statement 3 is wrong: most Indian coal is bituminous, the grade used for power and, when of coking quality, for steel; anthracite, the highest grade, is found only in small quantities in Jammu and Kashmir.",
  "कथन 1 और 2 सही हैं। भारत का लगभग 98 प्रतिशत कोयला दामोदर, महानदी, गोदावरी और सोन की घाटियों में 20 करोड़ वर्ष से कुछ अधिक पुरानी गोंडवाना संरचनाओं में है; अपेक्षाकृत नया टर्शियरी कोयला असम, मेघालय, अरुणाचल प्रदेश और नागालैंड में मिलता है। "
  "कथन 3 गलत है: अधिकांश भारतीय कोयला बिटुमिनस है, जो बिजली के लिए और कोकिंग गुणवत्ता का होने पर इस्पात के लिए प्रयुक्त होता है; सबसे उच्च श्रेणी का एन्थ्रेसाइट केवल थोड़ी मात्रा में जम्मू-कश्मीर में मिलता है।",
  f"{NC12I} -- Mineral and Energy Resources; {NC10} -- Minerals and Energy Resources.",
  "res-coal-gondwana-tertiary")

S(RS, "medium", "Consider the following statements about iron ore in India:",
  "भारत में लौह अयस्क के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Bailadila in Chhattisgarh is known for high-grade haematite.",
   "Odisha is the largest producer of iron ore.",
   "Magnetite has a higher iron content than haematite."],
  ["छत्तीसगढ़ का बैलाडीला उच्च श्रेणी के हेमेटाइट के लिए जाना जाता है।",
   "ओडिशा लौह अयस्क का सबसे बड़ा उत्पादक है।",
   "मैग्नेटाइट में हेमेटाइट की तुलना में लोहे की मात्रा अधिक होती है।"],
  C3, 2,
  "All three statements are correct. The Bailadila hills of Dantewada, named for their hump-like shape, yield some of the finest haematite in the world, much of it exported through Visakhapatnam. Odisha, with the Keonjhar, Sundargarh and Mayurbhanj deposits, produces more than half of India's iron ore. Magnetite can contain up to about 70 per cent iron, but haematite is the ore used in the largest quantities.",
  "तीनों कथन सही हैं। दंतेवाड़ा की बैलाडीला पहाड़ियाँ, जिनका नाम बैल के कूबड़ जैसे आकार से पड़ा, विश्व का कुछ सबसे उत्तम हेमेटाइट देती हैं, जिसका बहुत-सा भाग विशाखापत्तनम से निर्यात होता है। क्योंझर, सुंदरगढ़ और मयूरभंज के भंडारों वाला ओडिशा भारत के आधे से अधिक लौह अयस्क का उत्पादन करता है। मैग्नेटाइट में लगभग 70 प्रतिशत तक लोहा हो सकता है, पर सबसे अधिक मात्रा में प्रयुक्त होने वाला अयस्क हेमेटाइट है।",
  f"{NC10} -- Minerals and Energy Resources; Indian Bureau of Mines -- Indian Minerals Yearbook.",
  "res-iron-ore-bailadila-odisha")

S(RS, "medium", "Consider the following statements about minerals and their uses:",
  "खनिजों और उनके उपयोगों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Bauxite is the ore from which aluminium is obtained.",
   "Manganese is used mainly in the aluminium industry.",
   "Limestone is the basic raw material of the cement industry."],
  ["बॉक्साइट वह अयस्क है जिससे ऐलुमिनियम प्राप्त होता है।",
   "मैंगनीज़ मुख्य रूप से ऐलुमिनियम उद्योग में प्रयुक्त होता है।",
   "चूना पत्थर सीमेंट उद्योग का मूल कच्चा माल है।"],
  C3, 1,
  "Statements 1 and 3 are correct. Bauxite, a clay-like material rich in aluminium oxides formed by the decomposition of rocks, is refined into alumina and then smelted into aluminium; limestone, with clay and gypsum, is the main raw material of cement. "
  "Statement 2 is wrong: manganese is used mainly in making steel and ferro-manganese alloys -- nearly 10 kg of it goes into a tonne of steel -- and also in bleaching powder, insecticides and paints.",
  "कथन 1 और 3 सही हैं। चट्टानों के विघटन से बना, ऐलुमिनियम ऑक्साइडों से भरपूर मिट्टी जैसा पदार्थ बॉक्साइट पहले ऐलुमिना में शोधित होता है और फिर प्रगलन से ऐलुमिनियम बनता है; मिट्टी और जिप्सम के साथ चूना पत्थर सीमेंट का मुख्य कच्चा माल है। "
  "कथन 2 गलत है: मैंगनीज़ मुख्य रूप से इस्पात और फ़ेरो-मैंगनीज़ मिश्रधातु बनाने में प्रयुक्त होता है, एक टन इस्पात में लगभग 10 किलो मैंगनीज़ लगता है, और यह ब्लीचिंग पाउडर, कीटनाशकों और पेंट में भी काम आता है।",
  f"{NC10} -- Minerals and Energy Resources.",
  "res-bauxite-manganese-limestone")

S(RS, "medium", "Consider the following statements about oil fields in India:",
  "भारत के तेल क्षेत्रों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Digboi in Assam is the oldest oil-producing area in India.",
   "Mumbai High is an offshore oil field.",
   "The Barmer basin in Rajasthan is an important onshore oil-producing area.",
   "The Ankleshwar oil field lies in Rajasthan."],
  ["असम का डिगबोई भारत का सबसे पुराना तेल उत्पादक क्षेत्र है।",
   "मुंबई हाई एक अपतटीय (offshore) तेल क्षेत्र है।",
   "राजस्थान का बाड़मेर बेसिन एक महत्त्वपूर्ण स्थलीय (onshore) तेल उत्पादक क्षेत्र है।",
   "अंकलेश्वर तेल क्षेत्र राजस्थान में है।"],
  C4, 2,
  "Statements 1, 2 and 3 are correct. Oil was struck at Digboi in the 1880s and its refinery, started in 1901, is one of the oldest still working in the world; Mumbai High, about 160 km off the Mumbai coast, has been India's largest producing field since the 1970s; and the Mangala and other fields of the Barmer basin made Rajasthan a leading onshore producer after 2009. "
  "Statement 4 is wrong: Ankleshwar lies in Gujarat, in the Cambay (Khambhat) basin, and was one of the first fields developed after Independence.",
  "कथन 1, 2 और 3 सही हैं। डिगबोई में 1880 के दशक में तेल मिला और 1901 में शुरू हुई इसकी रिफ़ाइनरी विश्व की अब भी चल रही सबसे पुरानी रिफ़ाइनरियों में से एक है; मुंबई तट से लगभग 160 किमी दूर स्थित मुंबई हाई 1970 के दशक से भारत का सबसे बड़ा उत्पादक क्षेत्र है; और बाड़मेर बेसिन के मंगला तथा अन्य क्षेत्रों ने 2009 के बाद राजस्थान को एक प्रमुख स्थलीय उत्पादक बना दिया। "
  "कथन 4 गलत है: अंकलेश्वर गुजरात में, कैम्बे (खंभात) बेसिन में है, और स्वतंत्रता के बाद विकसित पहले क्षेत्रों में से एक था।",
  f"{NC12I} -- Mineral and Energy Resources; Ministry of Petroleum and Natural Gas.",
  "res-oil-fields-digboi-bombay-high-barmer")

S(RS, "medium", "Consider the following statements about India's electricity sector:",
  "भारत के विद्युत क्षेत्र के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["In 2025, non-fossil sources came to account for half of India's installed electricity capacity.",
   "Nuclear power provides more than a quarter of India's electricity generation.",
   "Solar power has the largest share of India's installed renewable energy capacity."],
  ["2025 में भारत की स्थापित विद्युत क्षमता में गैर-जीवाश्म स्रोतों का हिस्सा आधा हो गया।",
   "परमाणु ऊर्जा भारत के विद्युत उत्पादन का एक-चौथाई से अधिक भाग देती है।",
   "भारत की स्थापित नवीकरणीय ऊर्जा क्षमता में सौर ऊर्जा का हिस्सा सबसे बड़ा है।"],
  C3, 1,
  "Statements 1 and 3 are correct. By mid-2025 non-fossil sources -- solar, wind, hydro, biomass and nuclear -- made up about half of installed capacity, five years ahead of the 2030 target in India's climate pledge, and solar had grown to be the largest renewable source, well ahead of wind and large hydro. "
  "Statement 2 is wrong: nuclear plants generate only about 3 per cent of India's electricity; coal still produces most of it, because installed capacity and actual generation are different things -- coal plants run far more hours a year than solar panels.",
  "कथन 1 और 3 सही हैं। 2025 के मध्य तक गैर-जीवाश्म स्रोत, यानी सौर, पवन, जल, बायोमास और परमाणु, स्थापित क्षमता का लगभग आधा भाग हो गए, जो भारत के जलवायु संकल्प में 2030 के लक्ष्य से पाँच वर्ष पहले है, और सौर ऊर्जा पवन तथा बड़ी जलविद्युत से कहीं आगे सबसे बड़ा नवीकरणीय स्रोत बन गई। "
  "कथन 2 गलत है: परमाणु संयंत्र भारत की केवल लगभग 3 प्रतिशत बिजली बनाते हैं; अधिकांश बिजली अब भी कोयले से बनती है, क्योंकि स्थापित क्षमता और वास्तविक उत्पादन अलग-अलग बातें हैं; कोयला संयंत्र सौर पैनलों से वर्ष में कहीं अधिक घंटे चलते हैं।",
  "Ministry of Power; Ministry of New and Renewable Energy; Central Electricity Authority.",
  "res-electricity-capacity-mix")

S(RS, "medium", "Consider the following statements about cropping seasons in India:",
  "भारत में फ़सल ऋतुओं के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Kharif crops are sown with the onset of the monsoon and harvested in September-October.",
   "Mustard and gram are rabi crops.",
   "In Assam, West Bengal and Odisha, three crops of paddy -- aus, aman and boro -- are grown in a year."],
  ["खरीफ़ फ़सलें मानसून के आगमन के साथ बोई जाती हैं और सितंबर-अक्टूबर में काटी जाती हैं।",
   "सरसों और चना रबी की फ़सलें हैं।",
   "असम, पश्चिम बंगाल और ओडिशा में वर्ष में धान की तीन फ़सलें, औस, अमन और बोरो, उगाई जाती हैं।"],
  C3, 2,
  "All three statements are correct. Rabi crops are sown in October-December and harvested in April-June, helped by winter rain from western disturbances in the north-west; between the two seasons comes the short zaid season. The eastern States' three paddy crops use the pre-monsoon, monsoon and winter seasons.",
  "तीनों कथन सही हैं। रबी की फ़सलें अक्टूबर-दिसंबर में बोई जाती हैं और अप्रैल-जून में काटी जाती हैं, जिनमें उत्तर-पश्चिम में पश्चिमी विक्षोभों की शीतकालीन वर्षा सहायक होती है; दोनों ऋतुओं के बीच छोटी ज़ायद ऋतु आती है। पूर्वी राज्यों में धान की तीन फ़सलें मानसून-पूर्व, मानसून और शीत ऋतु का उपयोग करती हैं।",
  f"{NC10} -- Agriculture.",
  "res-cropping-seasons-aus-aman-boro")

S(RS, "medium", "Consider the following statements about the climatic needs of rice and wheat:",
  "चावल और गेहूँ की जलवायु संबंधी आवश्यकताओं के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Rice needs high temperature, high humidity and more than about 100 cm of rain.",
   "Wheat needs a cool growing season and bright sunshine at the time of ripening.",
   "Rice can be grown in areas of low rainfall with the help of irrigation."],
  ["चावल को ऊँचा तापमान, अधिक आर्द्रता और लगभग 100 सेमी से अधिक वर्षा चाहिए।",
   "गेहूँ को ठंडी उगने की ऋतु और पकने के समय तेज़ धूप चाहिए।",
   "सिंचाई की सहायता से चावल कम वर्षा वाले क्षेत्रों में भी उगाया जा सकता है।"],
  C3, 2,
  "All three statements are correct. Rice grows best above about 25 °C with plenty of water, which is why it dominates the wet east and the coasts; wheat needs 50-75 cm of rain spread over the growing season. With canals and tube-wells, Punjab and Haryana have become major rice growers despite modest rainfall -- at a heavy cost to groundwater.",
  "तीनों कथन सही हैं। चावल लगभग 25 °C से अधिक तापमान और भरपूर जल में सबसे अच्छा उगता है, इसीलिए यह नम पूर्व और तटों पर प्रमुख है; गेहूँ को उगने की ऋतु में फैली 50-75 सेमी वर्षा चाहिए। नहरों और नलकूपों के सहारे पंजाब और हरियाणा कम वर्षा के बावजूद प्रमुख चावल उत्पादक बन गए हैं, पर भूजल की भारी क़ीमत पर।",
  f"{NC10} -- Agriculture.",
  "res-rice-wheat-climate")

S(RS, "medium", "Consider the following statements about some cash crops:",
  "कुछ नक़दी फ़सलों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Cotton needs at least 210 frost-free days and bright sunshine.",
   "Groundnut is mainly a rabi crop.",
   "Sugarcane needs a cool, dry climate with little rainfall."],
  ["कपास को कम से कम 210 पाला-रहित दिन और तेज़ धूप चाहिए।",
   "मूँगफली मुख्य रूप से रबी की फ़सल है।",
   "गन्ने को कम वर्षा वाली ठंडी, शुष्क जलवायु चाहिए।"],
  C3, 0,
  "Only statement 1 is correct: cotton, a kharif crop of the Deccan and the north-west, takes six to eight months to mature and is harmed by frost and by rain at picking time. "
  "Statement 2 is wrong: groundnut is mainly a kharif crop, although some is grown in the rabi season in the south. "
  "Statement 3 is wrong: sugarcane is a tropical and subtropical crop that needs a hot, humid climate, 21-27 °C, and 75-100 cm of rain, or irrigation where rainfall is low.",
  "केवल कथन 1 सही है: दक्कन और उत्तर-पश्चिम की खरीफ़ फ़सल कपास को पकने में छह से आठ महीने लगते हैं और इसे पाले से तथा चुनाई के समय वर्षा से हानि होती है। "
  "कथन 2 गलत है: मूँगफली मुख्य रूप से खरीफ़ की फ़सल है, यद्यपि दक्षिण में कुछ रबी में भी उगाई जाती है। "
  "कथन 3 गलत है: गन्ना उष्णकटिबंधीय और उपोष्णकटिबंधीय फ़सल है, जिसे 21-27 °C की गर्म, नम जलवायु और 75-100 सेमी वर्षा चाहिए, या कम वर्षा वाले क्षेत्रों में सिंचाई।",
  f"{NC10} -- Agriculture.",
  "res-cotton-groundnut-sugarcane")

S(RS, "medium", "Consider the following statements about plantation crops in India:",
  "भारत में बागानी फ़सलों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Arabica coffee grown in India was first brought from Yemen.",
   "Kerala is the largest producer of coffee.",
   "Natural rubber is grown mainly in Assam and West Bengal."],
  ["भारत में उगाई जाने वाली अरेबिका कॉफ़ी सबसे पहले यमन से लाई गई थी।",
   "केरल कॉफ़ी का सबसे बड़ा उत्पादक है।",
   "प्राकृतिक रबर मुख्य रूप से असम और पश्चिम बंगाल में उगाया जाता है।"],
  C3, 0,
  "Only statement 1 is correct: by tradition, coffee first came to the Baba Budan hills of Karnataka with seeds brought from Yemen in the seventeenth century, and Indian Arabica is prized for its quality. "
  "Statement 2 is wrong: Karnataka grows about 70 per cent of India's coffee, mainly in Kodagu, Chikkamagaluru and Hassan; Kerala and Tamil Nadu follow. "
  "Statement 3 is wrong: Kerala produces most of India's natural rubber, and Tripura has become the second-largest producer.",
  "केवल कथन 1 सही है: परंपरा के अनुसार कॉफ़ी सत्रहवीं शताब्दी में यमन से लाए गए बीजों के साथ सबसे पहले कर्नाटक की बाबा बुदन पहाड़ियों में आई, और भारतीय अरेबिका अपनी गुणवत्ता के लिए प्रसिद्ध है। "
  "कथन 2 गलत है: भारत की लगभग 70 प्रतिशत कॉफ़ी कर्नाटक में, मुख्य रूप से कोडगु, चिक्कमगलुरु और हासन में, उगती है; इसके बाद केरल और तमिलनाडु आते हैं। "
  "कथन 3 गलत है: भारत का अधिकांश प्राकृतिक रबर केरल में होता है, और त्रिपुरा दूसरा सबसे बड़ा उत्पादक बन गया है।",
  f"{NC10} -- Agriculture; Coffee Board of India; Rubber Board.",
  "res-plantation-coffee-rubber")

S(RS, "medium", "Consider the following statements about millets:",
  "मोटे अनाजों (मिलेट्स) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Jowar, bajra and ragi are millets.",
   "Karnataka is the largest producer of ragi.",
   "Rajasthan is the largest producer of bajra."],
  ["ज्वार, बाजरा और रागी मोटे अनाज (मिलेट्स) हैं।",
   "कर्नाटक रागी का सबसे बड़ा उत्पादक है।",
   "राजस्थान बाजरे का सबसे बड़ा उत्पादक है।"],
  C3, 2,
  "All three statements are correct. Millets -- promoted as 'Shree Anna' after India led the International Year of Millets in 2023 -- grow on poorer soils with little water and are rich in fibre, iron and calcium. Ragi thrives in the red soils of dry Karnataka, and bajra on the sandy soils of Rajasthan, which grows a large share of the country's crop.",
  "तीनों कथन सही हैं। मोटे अनाज, जिन्हें 2023 के अंतरराष्ट्रीय मिलेट्स वर्ष की अगुवाई भारत द्वारा किए जाने के बाद 'श्री अन्न' के रूप में बढ़ावा दिया गया, कम जल वाली अपेक्षाकृत कमज़ोर मिट्टियों में उगते हैं और रेशे, लोहे तथा कैल्शियम से भरपूर होते हैं। रागी शुष्क कर्नाटक की लाल मिट्टियों में और बाजरा राजस्थान की रेतीली मिट्टियों में खूब उगता है, जहाँ देश की फ़सल का बड़ा भाग होता है।",
  f"{NC10} -- Agriculture; Ministry of Agriculture and Farmers Welfare.",
  "res-millets-ragi-bajra")

S(RS, "medium", "Consider the following statements about India's place in world agriculture:",
  "विश्व कृषि में भारत के स्थान के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["India is the largest producer of bananas in the world.",
   "India is the largest producer of pulses in the world.",
   "India is the largest producer of jute in the world.",
   "India is the second-largest producer of fruits and vegetables in the world."],
  ["भारत विश्व में केले का सबसे बड़ा उत्पादक है।",
   "भारत विश्व में दालों का सबसे बड़ा उत्पादक है।",
   "भारत विश्व में जूट का सबसे बड़ा उत्पादक है।",
   "भारत विश्व में फलों और सब्ज़ियों का दूसरा सबसे बड़ा उत्पादक है।"],
  C4, 3,
  "All four statements are correct. India leads the world in bananas, pulses and jute, and is second only to China in fruits and vegetables taken together. Even so, India also imports pulses in years of shortfall, because its consumption is the highest in the world. "
  "A student who expects one false statement in four will lose marks here.",
  "चारों कथन सही हैं। केले, दालों और जूट में भारत विश्व में प्रथम है, और फलों तथा सब्ज़ियों को मिलाकर केवल चीन से पीछे है। फिर भी कमी वाले वर्षों में भारत दालें आयात भी करता है, क्योंकि उसकी खपत विश्व में सबसे अधिक है। "
  "जो विद्यार्थी मानकर चलता है कि चार में से एक कथन गलत होगा, वह यहाँ अंक गँवाएगा।",
  "Ministry of Agriculture and Farmers Welfare; Food and Agriculture Organization (FAOSTAT).",
  "res-india-world-rank-crops")

S(RS, "medium", "Consider the following statements about the Indira Gandhi Canal:",
  "इंदिरा गांधी नहर के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It draws water from the Harike barrage, near the confluence of the Satluj and the Beas.",
   "It has helped to spread cultivation in the Thar desert of Rajasthan.",
   "It runs mainly through Gujarat."],
  ["यह सतलुज और ब्यास के संगम के पास हरिके बैराज से जल लेती है।",
   "इसने राजस्थान के थार मरुस्थल में खेती के प्रसार में मदद की है।",
   "यह मुख्य रूप से गुजरात से होकर बहती है।"],
  C3, 1,
  "Statements 1 and 2 are correct. One of the largest canal systems in the world, it starts at Harike in Punjab and runs parallel to the Pakistan border through western Rajasthan, bringing wheat, cotton, groundnut and rice to districts such as Sri Ganganagar, Bikaner and Jaisalmer. Waterlogging and soil salinity have followed in parts of its command area. "
  "Statement 3 is wrong: the canal runs almost wholly through Rajasthan; Gujarat's arid north is served instead by the Sardar Sarovar (Narmada) canal.",
  "कथन 1 और 2 सही हैं। विश्व की सबसे बड़ी नहर प्रणालियों में से एक यह नहर पंजाब के हरिके से शुरू होकर पाकिस्तान सीमा के समानांतर पश्चिमी राजस्थान से होकर जाती है और श्रीगंगानगर, बीकानेर और जैसलमेर जैसे ज़िलों में गेहूँ, कपास, मूँगफली और धान ले आई है। इसके कमान क्षेत्र के कुछ भागों में जलभराव और मिट्टी की लवणता भी आई है। "
  "कथन 3 गलत है: यह नहर लगभग पूरी तरह राजस्थान से होकर बहती है; गुजरात के शुष्क उत्तर को सरदार सरोवर (नर्मदा) नहर सेवा देती है।",
  f"{NC12I} -- Planning and Sustainable Development in Indian Context (Indira Gandhi Canal Command Area).",
  "res-indira-gandhi-canal")

S(RS, "medium", "Consider the following statements about irrigation in India:",
  "भारत में सिंचाई के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Canals irrigate the largest share of India's net irrigated area.",
   "Tank irrigation is important mainly in Punjab and Haryana.",
   "Drip irrigation increases the loss of water by evaporation compared with flood irrigation."],
  ["भारत के शुद्ध सिंचित क्षेत्र के सबसे बड़े भाग की सिंचाई नहरों से होती है।",
   "तालाब (टैंक) सिंचाई मुख्य रूप से पंजाब और हरियाणा में महत्त्वपूर्ण है।",
   "बाढ़ (flood) सिंचाई की तुलना में टपक (drip) सिंचाई से वाष्पीकरण द्वारा जल की हानि बढ़ती है।"],
  C3, 3,
  "None of the statements is correct. "
  "Statement 1 is wrong: wells and tube-wells, drawing on groundwater, irrigate well over half of the net irrigated area; canals come second. "
  "Statement 2 is wrong: tanks -- small reservoirs that store monsoon run-off -- are important in the hard-rock Peninsula, in Tamil Nadu, Telangana, Karnataka and Andhra Pradesh; Punjab and Haryana rely on tube-wells and canals. "
  "Statement 3 is wrong: drip irrigation delivers water drop by drop at the roots, cutting evaporation and run-off and saving a large share of the water used by flooding fields.",
  "कोई भी कथन सही नहीं है। "
  "कथन 1 गलत है: भूजल पर आधारित कुएँ और नलकूप शुद्ध सिंचित क्षेत्र के आधे से काफ़ी अधिक भाग की सिंचाई करते हैं; नहरें दूसरे स्थान पर हैं। "
  "कथन 2 गलत है: मानसूनी बहाव को संचित करने वाले छोटे जलाशय, यानी तालाब, कठोर चट्टानों वाले प्रायद्वीप में, तमिलनाडु, तेलंगाना, कर्नाटक और आंध्र प्रदेश में महत्त्वपूर्ण हैं; पंजाब और हरियाणा नलकूपों और नहरों पर निर्भर हैं। "
  "कथन 3 गलत है: टपक सिंचाई जड़ों पर बूँद-बूँद जल पहुँचाती है, जिससे वाष्पीकरण और बहाव घटता है और खेतों में पानी भरने की तुलना में बहुत-सा जल बचता है।",
  f"{NC12I} -- Water Resources; Ministry of Agriculture and Farmers Welfare -- Land Use Statistics.",
  "res-irrigation-sources")

S(RS, "medium", "Consider the following statements about types of farming:",
  "खेती के प्रकारों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Primitive subsistence farming depends on the monsoon and the natural fertility of the soil.",
   "Commercial farming uses mainly traditional inputs and little capital.",
   "Intensive subsistence farming is practised where the pressure of population on land is low."],
  ["आदिम निर्वाह खेती मानसून और मिट्टी की प्राकृतिक उर्वरता पर निर्भर होती है।",
   "वाणिज्यिक खेती में मुख्य रूप से परंपरागत आदान और कम पूँजी लगती है।",
   "गहन निर्वाह खेती वहाँ की जाती है जहाँ भूमि पर जनसंख्या का दबाव कम होता है।"],
  C3, 0,
  "Only statement 1 is correct: practised on small patches with digging sticks and hoes, as in slash-and-burn cultivation, it gives low yields. "
  "Statement 2 is wrong: commercial farming uses high doses of modern inputs -- high-yielding seeds, fertilisers, pesticides and machinery -- to produce for sale. "
  "Statement 3 is wrong: intensive subsistence farming, with heavy labour and inputs on small holdings, is practised where the pressure of population on land is high, as in the Ganga plains.",
  "केवल कथन 1 सही है: खुदाई की छड़ियों और कुदालों से छोटे भूखंडों पर, जैसे कर्तन-दहन (slash-and-burn) खेती में, की जाने वाली यह खेती कम उपज देती है। "
  "कथन 2 गलत है: वाणिज्यिक खेती बिक्री के लिए उत्पादन हेतु आधुनिक आदानों, यानी अधिक उपज वाले बीज, उर्वरक, कीटनाशक और मशीनें, का भारी उपयोग करती है। "
  "कथन 3 गलत है: छोटी जोतों पर भारी श्रम और आदानों वाली गहन निर्वाह खेती वहाँ होती है जहाँ भूमि पर जनसंख्या का दबाव अधिक होता है, जैसे गंगा के मैदानों में।",
  f"{NC10} -- Agriculture.",
  "res-farming-types")

S(RS, "medium", "Consider the following statements about the iron and steel industry:",
  "लोहा और इस्पात उद्योग के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Bhilai steel plant was set up with the help of the Soviet Union.",
   "The Rourkela steel plant was set up with the help of the United Kingdom.",
   "The Tata steel plant at Jamshedpur began in 1907."],
  ["भिलाई इस्पात संयंत्र सोवियत संघ की सहायता से स्थापित किया गया।",
   "राउरकेला इस्पात संयंत्र यूनाइटेड किंगडम की सहायता से स्थापित किया गया।",
   "जमशेदपुर का टाटा इस्पात संयंत्र 1907 में शुरू हुआ।"],
  C3, 1,
  "Statements 1 and 3 are correct. In the Second Five Year Plan three public-sector plants were built with foreign help: Bhilai (Chhattisgarh) with the Soviet Union, Rourkela (Odisha) with West Germany and Durgapur (West Bengal) with the United Kingdom; Bokaro later came up with Soviet help. The Tata Iron and Steel Company was set up at Sakchi, now Jamshedpur, in 1907. "
  "Statement 2 is wrong: Rourkela was built with West German collaboration; the British helped with Durgapur.",
  "कथन 1 और 3 सही हैं। दूसरी पंचवर्षीय योजना में विदेशी सहायता से सार्वजनिक क्षेत्र के तीन संयंत्र बने: सोवियत संघ के साथ भिलाई (छत्तीसगढ़), पश्चिम जर्मनी के साथ राउरकेला (ओडिशा) और यूनाइटेड किंगडम के साथ दुर्गापुर (पश्चिम बंगाल); बाद में सोवियत सहायता से बोकारो बना। टाटा आयरन एंड स्टील कंपनी 1907 में साकची, अब जमशेदपुर, में स्थापित हुई। "
  "कथन 2 गलत है: राउरकेला पश्चिम जर्मनी के सहयोग से बना; अंग्रेज़ों ने दुर्गापुर में सहायता की।",
  f"{NC12I} -- Manufacturing Industries; {NC10} -- Manufacturing Industries.",
  "res-steel-plants-foreign-help")

# ================================================================ HARD STATEMENTS (5)
S(RS, "hard", "Consider the following statements about atomic minerals and nuclear energy in India:",
  "भारत में परमाणु खनिजों और परमाणु ऊर्जा के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The monazite sands of the Kerala coast are a source of thorium.",
   "Jaduguda in Jharkhand has uranium mines.",
   "The Tummalapalle uranium deposit lies in Karnataka.",
   "India's three-stage nuclear power programme aims ultimately at using thorium."],
  ["केरल तट की मोनाज़ाइट रेत थोरियम का स्रोत है।",
   "झारखंड के जादूगोड़ा में यूरेनियम की खदानें हैं।",
   "तुम्मलपल्ले यूरेनियम भंडार कर्नाटक में है।",
   "भारत के तीन-चरणीय परमाणु ऊर्जा कार्यक्रम का अंतिम लक्ष्य थोरियम का उपयोग है।"],
  C4, 2,
  "Statements 1, 2 and 4 are correct. India has some of the world's largest thorium reserves, in the monazite beach sands of Kerala, Tamil Nadu and Odisha, but only modest uranium; Jaduguda in the Singhbhum belt has been mined since 1967. Hence Homi Bhabha's plan: pressurised heavy-water reactors burn natural uranium, fast breeder reactors use the plutonium they produce, and the third stage is to run on thorium. "
  "Statement 3 is wrong: Tummalapalle, one of the largest uranium deposits in the country, is in the Kadapa district of Andhra Pradesh.",
  "कथन 1, 2 और 4 सही हैं। केरल, तमिलनाडु और ओडिशा की मोनाज़ाइट तटीय रेत में भारत के पास विश्व के सबसे बड़े थोरियम भंडारों में से कुछ हैं, पर यूरेनियम सीमित है; सिंहभूम पट्टी के जादूगोड़ा में 1967 से खनन हो रहा है। इसीलिए होमी भाभा की योजना बनी: दाबित भारी जल रिएक्टर प्राकृतिक यूरेनियम जलाते हैं, फ़ास्ट ब्रीडर रिएक्टर उनसे बने प्लूटोनियम का उपयोग करते हैं, और तीसरा चरण थोरियम पर चलना है। "
  "कथन 3 गलत है: देश के सबसे बड़े यूरेनियम भंडारों में से एक, तुम्मलपल्ले, आंध्र प्रदेश के कडप्पा ज़िले में है।",
  f"{NC12I} -- Mineral and Energy Resources; Department of Atomic Energy.",
  "res-atomic-minerals-three-stage")

S(RS, "hard", "Consider the following statements about the distribution of minerals in India:",
  "भारत में खनिजों के वितरण के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Most metallic minerals occur in the old crystalline rocks of the Peninsular plateau.",
   "Petroleum occurs mainly in sedimentary basins.",
   "Mineral fuels are found mainly in igneous rocks."],
  ["अधिकांश धात्विक खनिज प्रायद्वीपीय पठार की पुरानी रवेदार चट्टानों में पाए जाते हैं।",
   "पेट्रोलियम मुख्य रूप से अवसादी बेसिनों में पाया जाता है।",
   "खनिज ईंधन मुख्य रूप से आग्नेय चट्टानों में पाए जाते हैं।"],
  C3, 1,
  "Statements 1 and 2 are correct. The ancient igneous and metamorphic rocks of the Peninsula -- above all the belt from the Chotanagpur plateau through Odisha to Chhattisgarh -- hold iron ore, manganese, bauxite, copper and mica. "
  "Statement 3 is wrong: coal, oil and natural gas are formed from buried plant and animal matter and so occur in sedimentary rocks -- the Gondwana basins for coal and the offshore and delta basins, Assam, Gujarat and Rajasthan for oil and gas.",
  "कथन 1 और 2 सही हैं। प्रायद्वीप की प्राचीन आग्नेय और कायांतरित चट्टानों में, सबसे बढ़कर छोटानागपुर पठार से ओडिशा होते हुए छत्तीसगढ़ तक की पट्टी में, लौह अयस्क, मैंगनीज़, बॉक्साइट, तांबा और अभ्रक मिलते हैं। "
  "कथन 3 गलत है: कोयला, तेल और प्राकृतिक गैस दबे हुए पौधों और जंतुओं के अवशेषों से बनते हैं, इसलिए अवसादी चट्टानों में मिलते हैं; कोयले के लिए गोंडवाना बेसिन, और तेल तथा गैस के लिए अपतटीय और डेल्टा बेसिन, असम, गुजरात और राजस्थान।",
  f"{NC12I} -- Mineral and Energy Resources.",
  "res-mineral-distribution-rocks")

S(RS, "hard", "Consider the following statements about hydroelectric projects:",
  "जलविद्युत परियोजनाओं के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Subansiri Lower project lies on the border of Assam and Arunachal Pradesh.",
   "The Salal project is on the Jhelum.",
   "The Koyna project is in Kerala."],
  ["सुबनसिरी लोअर परियोजना असम और अरुणाचल प्रदेश की सीमा पर है।",
   "सलाल परियोजना झेलम पर है।",
   "कोयना परियोजना केरल में है।"],
  C3, 0,
  "Only statement 1 is correct: the 2,000 MW Subansiri Lower project of NHPC, one of the largest hydroelectric projects in the country, stands at Gerukamukh on the Assam-Arunachal border and is being commissioned unit by unit. "
  "Statement 2 is wrong: the Salal project is on the Chenab in Jammu and Kashmir's Reasi district. "
  "Statement 3 is wrong: the Koyna project, on a tributary of the Krishna, is in the Satara district of Maharashtra.",
  "केवल कथन 1 सही है: NHPC की 2,000 मेगावाट की सुबनसिरी लोअर परियोजना, देश की सबसे बड़ी जलविद्युत परियोजनाओं में से एक, असम-अरुणाचल सीमा पर गेरुकामुख में है और इसकी इकाइयाँ एक-एक करके चालू की जा रही हैं। "
  "कथन 2 गलत है: सलाल परियोजना जम्मू-कश्मीर के रियासी ज़िले में चिनाब पर है। "
  "कथन 3 गलत है: कृष्णा की एक सहायक नदी पर स्थित कोयना परियोजना महाराष्ट्र के सातारा ज़िले में है।",
  "Ministry of Power -- NHPC Limited; Central Electricity Authority.",
  "res-hydro-subansiri-salal-koyna")

S(RS, "hard", "Consider the following statements about the conditions needed by plantation crops:",
  "बागानी फ़सलों के लिए आवश्यक दशाओं के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Black pepper and cardamom are grown mainly in the Western Ghats region of Kerala and Karnataka.",
   "Coffee in India is usually grown under the shade of trees.",
   "Rubber needs high temperatures and heavy rainfall spread over the year."],
  ["काली मिर्च और इलायची मुख्य रूप से केरल और कर्नाटक के पश्चिमी घाट क्षेत्र में उगाई जाती हैं।",
   "भारत में कॉफ़ी प्रायः पेड़ों की छाया में उगाई जाती है।",
   "रबर को ऊँचा तापमान और पूरे वर्ष फैली भारी वर्षा चाहिए।"],
  C3, 2,
  "All three statements are correct. Pepper and cardamom need the heavy rain, humidity and shade of the Western Ghats forests -- the Cardamom hills take their name from the spice; coffee in Karnataka, Kerala and Tamil Nadu is grown under a canopy of shade trees, often mixed with pepper and cardamom, which protects the plants from strong sun; and rubber, an equatorial crop, needs more than about 200 cm of rain and temperatures above about 25 °C.",
  "तीनों कथन सही हैं। काली मिर्च और इलायची को पश्चिमी घाट के वनों की भारी वर्षा, आर्द्रता और छाया चाहिए; इलायची पहाड़ियों का नाम इसी मसाले से पड़ा है; कर्नाटक, केरल और तमिलनाडु में कॉफ़ी छायादार पेड़ों की छतरी के नीचे, प्रायः काली मिर्च और इलायची के साथ, उगाई जाती है, जो पौधों को तेज़ धूप से बचाती है; और भूमध्यरेखीय फ़सल रबर को लगभग 200 सेमी से अधिक वर्षा और लगभग 25 °C से अधिक तापमान चाहिए।",
  f"{NC10} -- Agriculture.",
  "res-plantation-spices-coffee-rubber-conditions")

S(RS, "hard", "Consider the following statements about cropping intensity:",
  "फ़सल गहनता (cropping intensity) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Cropping intensity is the gross cropped area expressed as a percentage of the net sown area.",
   "A cropping intensity of 100 per cent means that the land is cropped twice a year.",
   "Areas without assured irrigation generally have higher cropping intensity than irrigated areas."],
  ["फ़सल गहनता सकल फ़सल क्षेत्र को शुद्ध बोए गए क्षेत्र के प्रतिशत के रूप में व्यक्त करती है।",
   "100 प्रतिशत फ़सल गहनता का अर्थ है कि भूमि पर वर्ष में दो बार फ़सल ली जाती है।",
   "सुनिश्चित सिंचाई से रहित क्षेत्रों में सामान्यतः सिंचित क्षेत्रों से अधिक फ़सल गहनता होती है।"],
  C3, 0,
  "Only statement 1 is correct: if the same field is sown twice in a year, it is counted twice in the gross cropped area but once in the net sown area. "
  "Statement 2 is wrong: 100 per cent means every sown field bears only one crop a year; 200 per cent would mean two crops on all of it. "
  "Statement 3 is wrong: assured irrigation is what makes a second or third crop possible, which is why irrigated Punjab and Haryana have some of the highest cropping intensities in the country.",
  "केवल कथन 1 सही है: यदि एक ही खेत में वर्ष में दो बार बुआई होती है, तो वह सकल फ़सल क्षेत्र में दो बार पर शुद्ध बोए गए क्षेत्र में एक बार गिना जाता है। "
  "कथन 2 गलत है: 100 प्रतिशत का अर्थ है कि हर बोए गए खेत में वर्ष में केवल एक फ़सल होती है; 200 प्रतिशत का अर्थ होगा कि पूरे क्षेत्र में दो फ़सलें होती हैं। "
  "कथन 3 गलत है: सुनिश्चित सिंचाई से ही दूसरी या तीसरी फ़सल संभव होती है, इसीलिए सिंचित पंजाब और हरियाणा में देश की सबसे ऊँची फ़सल गहनताओं में से कुछ हैं।",
  f"{NC12I} -- Land Resources and Agriculture.",
  "res-cropping-intensity")

# ================================================================ EASY STATEMENTS (5)
S(RS, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Solar energy is a non-renewable resource.",
   "Coal is a fossil fuel."],
  ["सौर ऊर्जा एक अनवीकरणीय संसाधन है।",
   "कोयला एक जीवाश्म ईंधन है।"],
  T2, 1,
  "Only statement 2 is correct: coal formed over millions of years from plant material buried and compressed in swamps. Statement 1 is wrong: sunlight is renewed every day and will not run out on any human timescale, so solar energy is renewable.",
  "केवल कथन 2 सही है: कोयला दलदलों में दबे और संपीडित पौधों के पदार्थ से लाखों वर्षों में बना। कथन 1 गलत है: सूर्य का प्रकाश हर दिन नवीनीकृत होता है और किसी भी मानवीय समय-सीमा में समाप्त नहीं होगा, इसलिए सौर ऊर्जा नवीकरणीय है।",
  f"{NC10} -- Resources and Development; Minerals and Energy Resources.",
  "res-solar-coal-easy")

S(RS, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Mustard is an oilseed crop.",
   "Wheat is a kharif crop."],
  ["सरसों एक तिलहन फ़सल है।",
   "गेहूँ खरीफ़ की फ़सल है।"],
  T2, 0,
  "Only statement 1 is correct. Statement 2 is wrong: wheat is the main rabi crop, sown in winter and harvested in spring.",
  "केवल कथन 1 सही है। कथन 2 गलत है: गेहूँ रबी की मुख्य फ़सल है, जो शीत ऋतु में बोई जाती है और वसंत में काटी जाती है।",
  f"{NC10} -- Agriculture.",
  "res-mustard-wheat-easy")

S(RS, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Rice is a food crop.",
   "Cotton is a fibre crop."],
  ["चावल एक खाद्य फ़सल है।",
   "कपास एक रेशेदार (fibre) फ़सल है।"],
  T2, 2,
  "Both statements are correct. Rice is the staple food of most of India; cotton, jute, hemp and natural silk are the main fibres the country produces.",
  "दोनों कथन सही हैं। चावल भारत के अधिकांश भाग का मुख्य भोजन है; कपास, जूट, सन और प्राकृतिक रेशम देश में उत्पादित मुख्य रेशे हैं।",
  f"{NC10} -- Agriculture.",
  "res-rice-cotton-easy")

S(RS, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Petroleum is also called mineral oil.",
   "Uranium is used as a fuel in nuclear power plants."],
  ["पेट्रोलियम को खनिज तेल भी कहते हैं।",
   "परमाणु बिजलीघरों में यूरेनियम का उपयोग ईंधन के रूप में होता है।"],
  T2, 2,
  "Both statements are correct. Petroleum is refined into fuels such as petrol, diesel and kerosene; uranium atoms release heat when they split, which turns water into steam to drive turbines.",
  "दोनों कथन सही हैं। पेट्रोलियम को शोधित करके पेट्रोल, डीज़ल और मिट्टी का तेल जैसे ईंधन बनते हैं; यूरेनियम के परमाणु टूटने पर ऊष्मा छोड़ते हैं, जो पानी को भाप में बदलकर टर्बाइन चलाती है।",
  f"{NC10} -- Minerals and Energy Resources.",
  "res-petroleum-uranium-easy")

S(RS, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Biogas is produced mainly from coal.",
   "Geothermal energy comes from the heat of the Sun."],
  ["बायोगैस मुख्य रूप से कोयले से बनती है।",
   "भूतापीय (geothermal) ऊर्जा सूर्य की ऊष्मा से मिलती है।"],
  T2, 3,
  "Neither statement is correct. Biogas is produced by the decomposition of cattle dung, crop waste and other organic matter without air; geothermal energy is heat from the Earth's interior, as tapped experimentally at Manikaran in Himachal Pradesh and the Puga valley in Ladakh.",
  "कोई भी कथन सही नहीं है। बायोगैस गोबर, फ़सल अवशेषों और अन्य जैविक पदार्थों के हवा के बिना सड़ने से बनती है; भूतापीय ऊर्जा पृथ्वी के आंतरिक भाग की ऊष्मा है, जिसका प्रायोगिक उपयोग हिमाचल प्रदेश के मणिकरण और लद्दाख की पूगा घाटी में किया गया है।",
  f"{NC10} -- Minerals and Energy Resources.",
  "res-biogas-geothermal-easy")

# ================================================================ MCQs (medium 7, hard 3, easy 2)
M(RS, "medium", "The Neyveli lignite field is located in:",
  "नेवेली लिग्नाइट क्षेत्र कहाँ स्थित है?",
  ["Tamil Nadu", "Rajasthan", "West Bengal", "Jharkhand"],
  ["तमिलनाडु", "राजस्थान", "पश्चिम बंगाल", "झारखंड"],
  0,
  "Neyveli, in Cuddalore district of Tamil Nadu, holds the country's largest lignite (brown coal) deposits, which feed the power stations of NLC India. Rajasthan (Barsingsar, Bikaner, Barmer) and Gujarat (Kachchh) also have lignite, which is why Rajasthan tempts; the coal of West Bengal and Jharkhand is bituminous.",
  "तमिलनाडु के कडलूर ज़िले में स्थित नेवेली में देश के सबसे बड़े लिग्नाइट (भूरे कोयले) भंडार हैं, जो NLC इंडिया के बिजलीघरों को ईंधन देते हैं। राजस्थान (बरसिंगसर, बीकानेर, बाड़मेर) और गुजरात (कच्छ) में भी लिग्नाइट है, इसीलिए राजस्थान आकर्षक लगता है; पश्चिम बंगाल और झारखंड का कोयला बिटुमिनस है।",
  f"{NC10} -- Minerals and Energy Resources.",
  "res-neyveli-lignite")

M(RS, "medium", "Which one of the following States is the largest producer of tea in India?",
  "निम्नलिखित में से कौन-सा राज्य भारत में चाय का सबसे बड़ा उत्पादक है?",
  ["Assam", "West Bengal", "Kerala", "Tamil Nadu"],
  ["असम", "पश्चिम बंगाल", "केरल", "तमिलनाडु"],
  0,
  "Assam, with its gardens in the Brahmaputra and Barak valleys, produces about half of India's tea. West Bengal is the usual trap -- Darjeeling tea is famous, but its output is small; the State's larger share comes from the Dooars and Terai. Tamil Nadu and Kerala grow tea in the Nilgiris and nearby hills.",
  "ब्रह्मपुत्र और बराक घाटियों के बागानों वाला असम भारत की लगभग आधी चाय पैदा करता है। पश्चिम बंगाल सामान्य जाल है; दार्जिलिंग चाय प्रसिद्ध है, पर उसका उत्पादन कम है, और राज्य का बड़ा भाग डुआर्स और तराई से आता है। तमिलनाडु और केरल नीलगिरि और आसपास की पहाड़ियों में चाय उगाते हैं।",
  f"{NC10} -- Agriculture; Tea Board of India.",
  "res-tea-assam")

M(RS, "medium", "The Khetri mines in Rajasthan are known for:",
  "राजस्थान की खेतड़ी खदानें किसके लिए जानी जाती हैं?",
  ["Copper", "Gold", "Iron ore", "Mica"],
  ["तांबा", "सोना", "लौह अयस्क", "अभ्रक"],
  0,
  "The Khetri belt in Jhunjhunu district is one of India's main copper-producing areas, worked by Hindustan Copper; the others are the Singhbhum belt of Jharkhand and Malanjkhand in Madhya Pradesh, the largest. Rajasthan's Aravallis also yield lead and zinc (Zawar) and marble; India's gold comes mainly from Hutti in Karnataka.",
  "झुंझुनू ज़िले की खेतड़ी पट्टी भारत के मुख्य तांबा उत्पादक क्षेत्रों में से एक है, जहाँ हिंदुस्तान कॉपर खनन करती है; अन्य हैं झारखंड की सिंहभूम पट्टी और मध्य प्रदेश का मलाजखंड, जो सबसे बड़ा है। राजस्थान की अरावली से सीसा और जस्ता (ज़ावर) और संगमरमर भी मिलते हैं; भारत का सोना मुख्य रूप से कर्नाटक के हट्टी से आता है।",
  f"{NC10} -- Minerals and Energy Resources; Indian Bureau of Mines.",
  "res-khetri-copper")

M(RS, "medium", "Which one of the following crops is grown in the zaid season?",
  "निम्नलिखित में से कौन-सी फ़सल ज़ायद ऋतु में उगाई जाती है?",
  ["Watermelon", "Wheat", "Paddy", "Pigeon pea (arhar)"],
  ["तरबूज़", "गेहूँ", "धान", "अरहर (तूर)"],
  0,
  "The zaid season is the short summer gap between the rabi harvest and the kharif sowing, roughly March to June; watermelon, muskmelon, cucumber, vegetables and fodder crops are grown then, usually with irrigation. Wheat is rabi; paddy and arhar are kharif.",
  "ज़ायद ऋतु रबी की कटाई और खरीफ़ की बुआई के बीच की छोटी ग्रीष्मकालीन अवधि है, मोटे तौर पर मार्च से जून; इसमें प्रायः सिंचाई से तरबूज़, खरबूज़, खीरा, सब्ज़ियाँ और चारे की फ़सलें उगाई जाती हैं। गेहूँ रबी की और धान तथा अरहर खरीफ़ की फ़सलें हैं।",
  f"{NC10} -- Agriculture.",
  "res-zaid-watermelon")

M(RS, "medium", "The Jharia coalfield, known for fires that have burned underground for more than a century, is in:",
  "एक सदी से अधिक समय से भूमिगत जल रही आग के लिए प्रसिद्ध झरिया कोयला क्षेत्र कहाँ है?",
  ["Jharkhand", "West Bengal", "Odisha", "Chhattisgarh"],
  ["झारखंड", "पश्चिम बंगाल", "ओडिशा", "छत्तीसगढ़"],
  0,
  "Jharia, near Dhanbad in the Damodar valley, is the country's main source of coking coal for steel; its mine fires, first noticed in 1916, have forced families to be resettled. Raniganj in West Bengal, the other great Damodar field and India's first coalfield to be worked, is the usual trap; Talcher (Odisha) and Korba (Chhattisgarh) are large sources of power-grade coal.",
  "दामोदर घाटी में धनबाद के पास स्थित झरिया इस्पात के लिए कोकिंग कोयले का देश का मुख्य स्रोत है; 1916 में पहली बार देखी गई इसकी खदानों की आग के कारण परिवारों को पुनर्वासित करना पड़ा है। दामोदर का दूसरा बड़ा क्षेत्र और भारत में सबसे पहले खनन किया गया कोयला क्षेत्र, पश्चिम बंगाल का रानीगंज, सामान्य जाल है; तालचेर (ओडिशा) और कोरबा (छत्तीसगढ़) बिजली-श्रेणी के कोयले के बड़े स्रोत हैं।",
  f"{NC12I} -- Mineral and Energy Resources; Ministry of Coal -- Jharia Master Plan.",
  "res-jharia-coalfield")

M(RS, "medium", "'Operation Flood' is associated with the development of:",
  "'ऑपरेशन फ़्लड' किसके विकास से जुड़ा है?",
  ["Dairying", "Fisheries", "Oilseeds", "Flood control"],
  ["डेयरी (दुग्ध उत्पादन)", "मत्स्य पालन", "तिलहन", "बाढ़ नियंत्रण"],
  0,
  "Operation Flood, launched in 1970 by the National Dairy Development Board under Verghese Kurien, linked village milk co-operatives on the Anand (Amul) model with urban markets through a national milk grid -- the 'White Revolution' that made India the world's largest milk producer. The name refers to a flood of milk, which is why 'flood control' is the trap.",
  "1970 में वर्गीज़ कुरियन के नेतृत्व में राष्ट्रीय डेयरी विकास बोर्ड द्वारा शुरू किए गए ऑपरेशन फ़्लड ने आणंद (अमूल) मॉडल पर बनी गाँवों की दुग्ध सहकारी समितियों को एक राष्ट्रीय दुग्ध ग्रिड से शहरी बाज़ारों से जोड़ा; यही 'श्वेत क्रांति' थी जिसने भारत को विश्व का सबसे बड़ा दुग्ध उत्पादक बनाया। नाम दूध की बाढ़ की ओर संकेत करता है, इसीलिए 'बाढ़ नियंत्रण' जाल है।",
  "National Dairy Development Board; Department of Animal Husbandry and Dairying.",
  "res-operation-flood-milk")

M(RS, "medium", "Which one of the following States is the largest producer of groundnut in India?",
  "निम्नलिखित में से कौन-सा राज्य भारत में मूँगफली का सबसे बड़ा उत्पादक है?",
  ["Gujarat", "Tamil Nadu", "Andhra Pradesh", "Punjab"],
  ["गुजरात", "तमिलनाडु", "आंध्र प्रदेश", "पंजाब"],
  0,
  "Gujarat, especially the Saurashtra region, grows about 40 per cent of India's groundnut, followed by Rajasthan. Tamil Nadu and Andhra Pradesh, once the leaders, are the usual traps; Punjab grows little.",
  "गुजरात, विशेषकर सौराष्ट्र क्षेत्र, भारत की लगभग 40 प्रतिशत मूँगफली उगाता है, जिसके बाद राजस्थान आता है। कभी अग्रणी रहे तमिलनाडु और आंध्र प्रदेश सामान्य जाल हैं; पंजाब बहुत कम मूँगफली उगाता है।",
  "Ministry of Agriculture and Farmers Welfare -- Agricultural Statistics at a Glance.",
  "res-groundnut-gujarat")

M(RS, "hard", "In recent decades, sugar mills have tended to shift from north India to the southern and western States, especially Maharashtra. Which one of the following best explains this?",
  "हाल के दशकों में चीनी मिलें उत्तर भारत से दक्षिणी और पश्चिमी राज्यों, विशेषकर महाराष्ट्र, की ओर खिसकने लगी हैं। निम्नलिखित में से कौन-सा इसकी सबसे अच्छी व्याख्या करता है?",
  ["Cane there has a higher sucrose content and the crushing season lasts longer",
   "The southern and western States have the largest area under sugarcane in India",
   "The northern plains have stopped growing sugarcane because of falling groundwater",
   "Sugar can be exported only through the ports on the western coast of India"],
  ["वहाँ के गन्ने में सुक्रोज़ की मात्रा अधिक होती है और पेराई की ऋतु अधिक लंबी चलती है",
   "भारत में गन्ने का सबसे बड़ा क्षेत्र दक्षिणी और पश्चिमी राज्यों में है",
   "गिरते भूजल के कारण उत्तरी मैदानों ने गन्ना उगाना बंद कर दिया है",
   "चीनी का निर्यात केवल भारत के पश्चिमी तट के बंदरगाहों से ही हो सकता है"],
  0,
  "The tropical cane of the Peninsula yields more sugar per tonne, and the milder climate allows a longer crushing season; the success of co-operative sugar factories in Maharashtra added to the pull. Uttar Pradesh still has the largest area under sugarcane and remains a major producer, so the options about area and groundwater are false, and sugar can be shipped from any port.",
  "प्रायद्वीप का उष्णकटिबंधीय गन्ना प्रति टन अधिक चीनी देता है, और अपेक्षाकृत समशीतोष्ण जलवायु में पेराई की ऋतु लंबी चलती है; महाराष्ट्र में सहकारी चीनी कारख़ानों की सफलता ने इस खिंचाव को और बढ़ाया। गन्ने का सबसे बड़ा क्षेत्र अब भी उत्तर प्रदेश में है और वह प्रमुख उत्पादक बना हुआ है, इसलिए क्षेत्र और भूजल वाले विकल्प गलत हैं, और चीनी किसी भी बंदरगाह से भेजी जा सकती है।",
  f"{NC10} -- Manufacturing Industries.",
  "res-sugar-mills-shift-south")

M(RS, "hard", "The jute mills of India are concentrated along the banks of the Hooghly. Which one of the following best explains this?",
  "भारत की जूट मिलें हुगली के किनारों पर केंद्रित हैं। निम्नलिखित में से कौन-सा इसकी सबसे अच्छी व्याख्या करता है?",
  ["Nearness to jute-growing areas, cheap water transport and plenty of water for processing",
   "Jute is too light and bulky to be carried by road or rail, so the mills must be built on riverbanks",
   "The Hooghly's water is saline, which is needed to bleach the jute fibre white",
   "Jute can be grown only on islands in the Hooghly, so the mills are built beside them"],
  ["जूट उत्पादक क्षेत्रों की निकटता, सस्ता जल परिवहन और प्रसंस्करण के लिए भरपूर जल",
   "जूट सड़क या रेल से ले जाने के लिए बहुत हल्का और भारी-भरकम है, इसलिए मिलें नदी किनारों पर बनानी पड़ती हैं",
   "हुगली का जल खारा है, जो जूट के रेशे को सफ़ेद करने के लिए आवश्यक है",
   "जूट केवल हुगली के द्वीपों पर ही उग सकता है, इसलिए मिलें उनके पास बनती हैं"],
  0,
  "The mills grew up in a narrow belt about 100 km long on both banks of the Hooghly because the delta grows most of India's jute, the river offered cheap transport and water for retting and washing, labour came from West Bengal and neighbouring States, and Kolkata provided banking, insurance and a port. None of the other options is true.",
  "मिलें हुगली के दोनों किनारों पर लगभग 100 किमी लंबी संकरी पट्टी में इसलिए विकसित हुईं कि डेल्टा में भारत का अधिकांश जूट उगता है, नदी ने सस्ता परिवहन और जूट सड़ाने (retting) तथा धोने के लिए जल दिया, श्रमिक पश्चिम बंगाल और पड़ोसी राज्यों से मिले, और कोलकाता ने बैंकिंग, बीमा और बंदरगाह की सुविधा दी। अन्य कोई विकल्प सही नहीं है।",
  f"{NC10} -- Manufacturing Industries.",
  "res-jute-mills-hooghly")

M(RS, "hard", "Aluminium smelters are usually located close to sources of cheap and plentiful electricity. This is mainly because:",
  "ऐलुमिनियम प्रगलन संयंत्र प्रायः सस्ती और प्रचुर बिजली के स्रोतों के पास स्थापित किए जाते हैं। इसका मुख्य कारण क्या है?",
  ["turning alumina into aluminium by electrolysis uses very large amounts of power",
   "bauxite is found only in the reservoirs behind hydroelectric dams",
   "aluminium cannot be carried over long distances because it rusts quickly in moist air",
   "electricity is needed to mine bauxite from deep underground shafts"],
  ["ऐलुमिना को विद्युत-अपघटन से ऐलुमिनियम में बदलने में बहुत अधिक बिजली लगती है",
   "बॉक्साइट केवल जलविद्युत बाँधों के पीछे के जलाशयों में मिलता है",
   "नम हवा में जल्दी जंग लगने के कारण ऐलुमिनियम को लंबी दूरी तक नहीं ले जाया जा सकता",
   "गहरी भूमिगत खदानों से बॉक्साइट निकालने के लिए बिजली चाहिए"],
  0,
  "Smelting aluminium is one of the most power-hungry industrial processes -- electricity can be a third or more of its cost -- so smelters such as NALCO at Angul and Hindalco at Renukoot sit near coalfields, pit-head power plants or hydroelectric stations. Bauxite is mined from open-cast pits near the surface, and aluminium does not rust.",
  "ऐलुमिनियम का प्रगलन सबसे अधिक बिजली खाने वाली औद्योगिक प्रक्रियाओं में से एक है, इसकी लागत का एक-तिहाई या अधिक भाग बिजली हो सकता है, इसलिए अंगुल में NALCO और रेणुकूट में हिंडाल्को जैसे प्रगलक कोयला क्षेत्रों, खदान-मुख (pit-head) बिजलीघरों या जलविद्युत केंद्रों के पास हैं। बॉक्साइट सतह के पास खुली खदानों से निकाला जाता है, और ऐलुमिनियम में जंग नहीं लगता।",
  f"{NC10} -- Manufacturing Industries.",
  "res-aluminium-smelter-power")

M(RS, "easy", "Which one of the following is known as the 'golden fibre'?",
  "निम्नलिखित में से किसे 'सुनहरा रेशा' (golden fibre) कहा जाता है?",
  ["Jute", "Cotton", "Coir", "Silk"],
  ["जूट", "कपास", "नारियल रेशा (कॉयर)", "रेशम"],
  0,
  "Jute is called the golden fibre for its golden-brown colour and its value as a cash crop; it is used for gunny bags, mats, ropes and carpets, and is in demand again as a biodegradable substitute for plastic packaging.",
  "जूट को उसके सुनहरे-भूरे रंग और नक़दी फ़सल के रूप में उसके मूल्य के कारण सुनहरा रेशा कहा जाता है; इससे बोरे, चटाइयाँ, रस्सियाँ और कालीन बनते हैं, और प्लास्टिक पैकेजिंग के जैव-अपघटनीय विकल्प के रूप में इसकी माँग फिर बढ़ी है।",
  f"{NC10} -- Agriculture.",
  "res-golden-fibre-jute-easy")

M(RS, "easy", "Which one of the following is a fossil fuel?",
  "निम्नलिखित में से कौन-सा जीवाश्म ईंधन है?",
  ["Natural gas", "Uranium", "Wind energy", "Biogas"],
  ["प्राकृतिक गैस", "यूरेनियम", "पवन ऊर्जा", "बायोगैस"],
  0,
  "Natural gas, like coal and petroleum, formed over millions of years from buried organic matter, so it is a fossil fuel and cannot be replaced once used. Uranium is a mineral used for nuclear energy, wind is renewable, and biogas is made from fresh organic waste.",
  "कोयले और पेट्रोलियम की तरह प्राकृतिक गैस भी दबे हुए जैविक पदार्थ से लाखों वर्षों में बनी, इसलिए यह जीवाश्म ईंधन है और एक बार उपयोग के बाद इसकी पूर्ति नहीं हो सकती। यूरेनियम परमाणु ऊर्जा के लिए प्रयुक्त खनिज है, पवन नवीकरणीय है, और बायोगैस ताज़े जैविक अपशिष्ट से बनती है।",
  f"{NC10} -- Minerals and Energy Resources.",
  "res-fossil-fuel-natural-gas-easy")

# ================================================================ STATEMENT-I/II (medium 5, easy 2, hard 1 + I/II/III 1)
A(RS, "medium",
  "Tea gardens in India are located mainly on hill slopes.",
  "भारत में चाय के बागान मुख्य रूप से पहाड़ी ढलानों पर स्थित हैं।",
  "Tea bushes need plenty of rain but cannot tolerate water standing at their roots.",
  "चाय की झाड़ियों को भरपूर वर्षा चाहिए, पर वे अपनी जड़ों में पानी का ठहराव सहन नहीं कर सकतीं।",
  0,
  "Both statements are correct and Statement-II explains Statement-I. On slopes the heavy rain drains away quickly through deep, fertile, humus-rich soil, which is why tea is grown in the hills of Assam, Darjeeling and the Nilgiris; in flat areas the gardens need careful drainage channels.",
  "दोनों कथन सही हैं और कथन-II कथन-I की व्याख्या करता है। ढलानों पर भारी वर्षा का जल गहरी, उपजाऊ, ह्यूमस-युक्त मिट्टी से होकर जल्दी बह जाता है, इसीलिए चाय असम, दार्जिलिंग और नीलगिरि की पहाड़ियों में उगाई जाती है; समतल क्षेत्रों में बागानों को सावधानी से बनाई गई जल-निकास नालियाँ चाहिए।",
  f"{NC10} -- Agriculture.",
  "res-tea-slopes-drainage")

A(RS, "medium",
  "India imports most of the crude oil it uses.",
  "भारत अपने द्वारा उपयोग किए जाने वाले कच्चे तेल का अधिकांश भाग आयात करता है।",
  "Crude oil is refined into products such as petrol, diesel and LPG.",
  "कच्चे तेल को शोधित करके पेट्रोल, डीज़ल और एलपीजी जैसे उत्पाद बनाए जाते हैं।",
  1,
  "Both statements are correct, but Statement-II does not explain Statement-I. India imports more than 85 per cent of its crude oil because domestic production has stagnated while demand keeps growing. That crude is refined into many products explains why refineries exist -- India is in fact a large exporter of refined products -- not why it must import the crude.",
  "दोनों कथन सही हैं, पर कथन-II कथन-I की व्याख्या नहीं करता। भारत अपने कच्चे तेल का 85 प्रतिशत से अधिक भाग इसलिए आयात करता है कि घरेलू उत्पादन स्थिर है जबकि माँग बढ़ती जा रही है। कच्चे तेल से कई उत्पाद बनना यह बताता है कि रिफ़ाइनरियाँ क्यों हैं, वास्तव में भारत शोधित उत्पादों का बड़ा निर्यातक है, यह नहीं कि उसे कच्चा तेल आयात क्यों करना पड़ता है।",
  "Ministry of Petroleum and Natural Gas -- Petroleum Planning and Analysis Cell.",
  "res-crude-imports-refining")

A(RS, "medium",
  "Mica is widely used in the electrical and electronics industries.",
  "अभ्रक (mica) का विद्युत और इलेक्ट्रॉनिक उद्योगों में व्यापक उपयोग होता है।",
  "Mica is a good conductor of electricity.",
  "अभ्रक विद्युत का सुचालक है।",
  2,
  "Statement-I is correct but Statement-II is incorrect. Mica is prized for exactly the opposite property: it is an excellent insulator, splits into thin, transparent, heat-resistant sheets and has high dielectric strength, so it is used in capacitors, heaters and electrical appliances. The Koderma-Gaya-Hazaribagh belt of Jharkhand and Nellore in Andhra Pradesh are known for it.",
  "कथन-I सही है पर कथन-II गलत है। अभ्रक ठीक उलटे गुण के लिए मूल्यवान है: यह उत्कृष्ट विद्युत-रोधी है, पतली, पारदर्शी, ऊष्मा-प्रतिरोधी परतों में बँटता है और इसकी परावैद्युत सामर्थ्य अधिक है, इसलिए इसका उपयोग संधारित्रों, हीटरों और बिजली के उपकरणों में होता है। झारखंड की कोडरमा-गया-हज़ारीबाग पट्टी और आंध्र प्रदेश का नेल्लोर इसके लिए जाने जाते हैं।",
  f"{NC10} -- Minerals and Energy Resources.",
  "res-mica-insulator")

A(RS, "medium",
  "Jute is grown mainly in the dry regions of western India.",
  "जूट मुख्य रूप से पश्चिमी भारत के शुष्क क्षेत्रों में उगाया जाता है।",
  "Jute needs high temperatures, heavy rainfall and fertile alluvial soils that are renewed by floods.",
  "जूट को ऊँचा तापमान, भारी वर्षा और बाढ़ से नवीनीकृत होने वाली उपजाऊ जलोढ़ मिट्टी चाहिए।",
  3,
  "Statement-I is incorrect but Statement-II is correct. Because of these needs, jute is grown on the flood plains of the Ganga-Brahmaputra delta -- West Bengal, Bihar, Assam, Odisha and Meghalaya -- with West Bengal producing most of India's crop.",
  "कथन-I गलत है पर कथन-II सही है। इन्हीं आवश्यकताओं के कारण जूट गंगा-ब्रह्मपुत्र डेल्टा के बाढ़ के मैदानों में, यानी पश्चिम बंगाल, बिहार, असम, ओडिशा और मेघालय में, उगाया जाता है, और भारत की अधिकांश फ़सल पश्चिम बंगाल में होती है।",
  f"{NC10} -- Agriculture.",
  "res-jute-growing-conditions")

A(RS, "medium",
  "Many thermal power stations in India are located close to coalfields.",
  "भारत के कई ताप बिजलीघर कोयला क्षेत्रों के पास स्थित हैं।",
  "Coal is bulky and loses much of its weight when burnt, so it is cheaper to generate power near the mines and carry electricity by transmission lines.",
  "कोयला भारी-भरकम होता है और जलने पर उसका बहुत-सा भार घट जाता है, इसलिए खदानों के पास बिजली बनाकर उसे पारेषण लाइनों से ले जाना सस्ता पड़ता है।",
  0,
  "Both statements are correct and Statement-II explains Statement-I. Coal is a weight-losing raw material with a high ash content in India, so 'pit-head' plants have grown up at Singrauli, Korba, Talcher and in the Damodar valley, while plants far from the mines depend on long rail hauls or on imported coal at coastal sites.",
  "दोनों कथन सही हैं और कथन-II कथन-I की व्याख्या करता है। भारत में कोयला अधिक राख वाला, भार घटाने वाला कच्चा माल है, इसलिए सिंगरौली, कोरबा, तालचेर और दामोदर घाटी में 'खदान-मुख' संयंत्र विकसित हुए हैं, जबकि खदानों से दूर के संयंत्र लंबी रेल ढुलाई या तटीय स्थलों पर आयातित कोयले पर निर्भर हैं।",
  f"{NC12I} -- Mineral and Energy Resources; Manufacturing Industries.",
  "res-thermal-plants-pit-head")

A(RS, "easy",
  "Terrace farming is practised on hill slopes.",
  "सीढ़ीदार (terrace) खेती पहाड़ी ढलानों पर की जाती है।",
  "Terraces slow down the water flowing down a slope and check soil erosion.",
  "सीढ़ीदार खेत ढलान से नीचे बहते जल की गति धीमी करते हैं और मृदा अपरदन को रोकते हैं।",
  0,
  "Both statements are correct and Statement-II explains Statement-I. Cutting a slope into flat steps creates level fields that hold water and soil, which is why terraces are common in the western and central Himalaya and in the north-eastern hills.",
  "दोनों कथन सही हैं और कथन-II कथन-I की व्याख्या करता है। ढलान को समतल सीढ़ियों में काटने से ऐसे समतल खेत बनते हैं जो जल और मिट्टी को रोके रखते हैं, इसीलिए पश्चिमी और मध्य हिमालय तथा पूर्वोत्तर की पहाड़ियों में सीढ़ीदार खेत आम हैं।",
  f"{NC10} -- Resources and Development.",
  "res-terrace-farming-easy")

A(RS, "easy",
  "Solar energy has great potential in India.",
  "भारत में सौर ऊर्जा की बहुत अधिक संभावना है।",
  "India gets fewer sunny days in a year than most European countries.",
  "भारत में वर्ष में अधिकांश यूरोपीय देशों की तुलना में कम धूप वाले दिन होते हैं।",
  2,
  "Statement-I is correct but Statement-II is incorrect. Lying largely in the tropics, India gets about 300 clear, sunny days a year in most parts, far more than most of Europe -- which is why large solar parks have come up in Rajasthan, Gujarat, Karnataka and elsewhere.",
  "कथन-I सही है पर कथन-II गलत है। अधिकांशतः उष्णकटिबंध में स्थित भारत के अधिकांश भागों में वर्ष में लगभग 300 साफ़, धूप वाले दिन होते हैं, जो अधिकांश यूरोप से कहीं अधिक हैं; इसीलिए राजस्थान, गुजरात, कर्नाटक और अन्य स्थानों पर बड़े सौर पार्क बने हैं।",
  "Ministry of New and Renewable Energy.",
  "res-solar-potential-easy")

A(RS, "hard",
  "India is self-sufficient in natural gas.",
  "भारत प्राकृतिक गैस में आत्मनिर्भर है।",
  "India imports liquefied natural gas (LNG) through terminals such as Dahej in Gujarat.",
  "भारत गुजरात के दाहेज जैसे टर्मिनलों से द्रवीकृत प्राकृतिक गैस (LNG) आयात करता है।",
  3,
  "Statement-I is incorrect but Statement-II is correct. Roughly half of the natural gas India uses is imported as LNG, shipped mainly from Qatar and elsewhere and regasified at terminals such as Dahej and Hazira in Gujarat, Dabhol in Maharashtra and Kochi in Kerala; domestic gas comes from the Krishna-Godavari basin, Mumbai High and Assam.",
  "कथन-I गलत है पर कथन-II सही है। भारत द्वारा उपयोग की जाने वाली प्राकृतिक गैस का लगभग आधा भाग LNG के रूप में आयात होता है, जो मुख्य रूप से क़तर और अन्य देशों से जहाज़ों द्वारा आता है और गुजरात के दाहेज और हज़ीरा, महाराष्ट्र के दाभोल और केरल के कोच्चि जैसे टर्मिनलों पर फिर गैस में बदला जाता है; घरेलू गैस कृष्णा-गोदावरी बेसिन, मुंबई हाई और असम से आती है।",
  "Ministry of Petroleum and Natural Gas -- Petroleum Planning and Analysis Cell.",
  "res-natural-gas-lng-imports")

A(RS, "hard",
  "Several large iron and steel plants are concentrated in the Chotanagpur plateau region.",
  "छोटानागपुर पठार क्षेत्र में कई बड़े लोहा और इस्पात संयंत्र केंद्रित हैं।",
  "Coal and iron ore, the main raw materials of the industry, are found close to each other in this region.",
  "इस उद्योग के मुख्य कच्चे माल, कोयला और लौह अयस्क, इस क्षेत्र में एक-दूसरे के पास पाए जाते हैं।",
  1,
  "Both Statements II and III are correct, but only Statement II explains Statement I. Jamshedpur, Bokaro, Durgapur, Burnpur and Rourkela lie close to the coking coal of the Damodar valley and the iron ore of Singhbhum and Keonjhar, with limestone and manganese nearby -- the region has the country's cheapest assembly of raw materials, along with cheap labour and a large home market. "
  "Statement III is true -- Bokaro, Durgapur, Burnpur and Rourkela belong to the Steel Authority of India -- but who owns the plants does not explain why they are in this region.",
  "कथन II और III दोनों सही हैं, पर केवल कथन II कथन I की व्याख्या करता है। जमशेदपुर, बोकारो, दुर्गापुर, बर्नपुर और राउरकेला दामोदर घाटी के कोकिंग कोयले और सिंहभूम तथा क्योंझर के लौह अयस्क के पास हैं, और चूना पत्थर तथा मैंगनीज़ भी पास में हैं; सस्ते श्रम और बड़े घरेलू बाज़ार के साथ यह क्षेत्र देश में कच्चे माल को सबसे सस्ते में एकत्र करने की सुविधा देता है। "
  "कथन III सही है, बोकारो, दुर्गापुर, बर्नपुर और राउरकेला स्टील अथॉरिटी ऑफ़ इंडिया के हैं, पर संयंत्रों का स्वामित्व यह नहीं बताता कि वे इस क्षेत्र में क्यों हैं।",
  f"{NC12I} -- Manufacturing Industries.",
  "res-chotanagpur-steel-location",
  s3="Several of these plants are run by the Steel Authority of India Limited.",
  s3_hi="इनमें से कई संयंत्र स्टील अथॉरिटी ऑफ़ इंडिया लिमिटेड द्वारा चलाए जाते हैं।")

# ================================================================ PAIRS (medium 2, easy 1, hard 1)
P(RS, "easy", "Consider the following pairs of 'revolutions' and the fields they relate to:",
  "'क्रांतियों' और उनसे संबंधित क्षेत्रों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Yellow Revolution : Oilseeds", "Blue Revolution : Fisheries", "Silver Revolution : Eggs and poultry", "Grey Revolution : Milk"],
  ["पीली क्रांति : तिलहन", "नीली क्रांति : मत्स्य पालन", "रजत क्रांति : अंडे और मुर्गीपालन", "धूसर क्रांति : दूध"],
  2,
  "Pairs 1, 2 and 3 are correct. The Yellow Revolution raised oilseed output through the Technology Mission on Oilseeds from 1986; the Blue Revolution boosted fisheries and aquaculture; the Silver Revolution relates to eggs and poultry. "
  "Pair 4 is wrong: milk is the White Revolution (Operation Flood); the Grey Revolution refers to fertilisers.",
  "युग्म 1, 2 और 3 सही हैं। पीली क्रांति ने 1986 से तिलहन पर प्रौद्योगिकी मिशन के ज़रिए तिलहन उत्पादन बढ़ाया; नीली क्रांति ने मत्स्य पालन और जलीय कृषि को बढ़ावा दिया; रजत क्रांति अंडों और मुर्गीपालन से जुड़ी है। "
  "युग्म 4 गलत है: दूध श्वेत क्रांति (ऑपरेशन फ़्लड) है; धूसर क्रांति उर्वरकों से जुड़ी है।",
  "Ministry of Agriculture and Farmers Welfare; Department of Fisheries.",
  "res-revolutions-pairs-easy")

P(RS, "medium", "Consider the following pairs of nuclear power stations and the States in which they are located:",
  "परमाणु बिजलीघरों और उन राज्यों के निम्नलिखित युग्मों पर विचार कीजिए जिनमें वे स्थित हैं:",
  ["Tarapur : Maharashtra", "Kudankulam : Tamil Nadu", "Kaiga : Karnataka", "Narora : Uttar Pradesh"],
  ["तारापुर : महाराष्ट्र", "कुडनकुलम : तमिलनाडु", "कैगा : कर्नाटक", "नरोरा : उत्तर प्रदेश"],
  3,
  "All four pairs are correct. Tarapur (1969) was India's first nuclear power station; Kudankulam, built with Russian collaboration, has the largest reactors in the country; Kaiga lies in Uttara Kannada; and Narora stands on the Ganga in Bulandshahr district. The others include Rawatbhata (Rajasthan), Kakrapar (Gujarat) and Kalpakkam (Tamil Nadu). "
  "A student who expects one mismatch will fall for 'Only three pairs'.",
  "चारों युग्म सही हैं। तारापुर (1969) भारत का पहला परमाणु बिजलीघर था; रूसी सहयोग से बने कुडनकुलम में देश के सबसे बड़े रिएक्टर हैं; कैगा उत्तर कन्नड़ में है; और नरोरा बुलंदशहर ज़िले में गंगा के किनारे है। अन्य में रावतभाटा (राजस्थान), काकरापार (गुजरात) और कलपक्कम (तमिलनाडु) हैं। "
  "जो विद्यार्थी एक बेमेल की अपेक्षा करता है, वह 'केवल तीन युग्म' के जाल में फँसेगा।",
  f"{NC12I} -- Mineral and Energy Resources; Nuclear Power Corporation of India.",
  "res-nuclear-plants-pairs")

P(RS, "medium", "Consider the following pairs of local names for shifting cultivation and the regions where they are used:",
  "स्थानांतरी खेती के स्थानीय नामों और उन क्षेत्रों के निम्नलिखित युग्मों पर विचार कीजिए जहाँ वे प्रचलित हैं:",
  ["Jhum : North-eastern India", "Milpa : Mexico and Central America", "Ladang : Indonesia and Malaysia", "Roca : Venezuela"],
  ["झूम : पूर्वोत्तर भारत", "मिल्पा : मेक्सिको और मध्य अमेरिका", "लदांग : इंडोनेशिया और मलेशिया", "रोका : वेनेज़ुएला"],
  2,
  "Pairs 1, 2 and 3 are correct: slash-and-burn cultivation has many local names -- jhum in the north-east, milpa in Mexico and Central America, ladang in Indonesia and Malaysia, and ray in Vietnam. "
  "Pair 4 is wrong: roca is the name used in Brazil; in Venezuela it is called conuco.",
  "युग्म 1, 2 और 3 सही हैं: कर्तन-दहन खेती के कई स्थानीय नाम हैं, जैसे पूर्वोत्तर में झूम, मेक्सिको और मध्य अमेरिका में मिल्पा, इंडोनेशिया और मलेशिया में लदांग, और वियतनाम में रे। "
  "युग्म 4 गलत है: रोका ब्राज़ील में प्रयुक्त नाम है; वेनेज़ुएला में इसे कोनुको कहते हैं।",
  f"{NC10} -- Agriculture; {NC12F} -- Primary Activities.",
  "res-shifting-cultivation-names-pairs")

P(RS, "hard", "Consider the following pairs of large solar parks and the States in which they are located:",
  "बड़े सौर पार्कों और उन राज्यों के निम्नलिखित युग्मों पर विचार कीजिए जिनमें वे स्थित हैं:",
  ["Bhadla : Rajasthan", "Pavagada : Karnataka", "Rewa : Chhattisgarh", "Kurnool : Telangana"],
  ["भड़ला : राजस्थान", "पावगढ़ : कर्नाटक", "रीवा : छत्तीसगढ़", "कुरनूल : तेलंगाना"],
  1,
  "Pairs 1 and 2 are correct: Bhadla in Jodhpur district and Pavagada in Tumakuru district are among the largest solar parks in the world. "
  "Pair 3 is wrong: the Rewa Ultra Mega Solar park, which supplies power to the Delhi Metro, is in Madhya Pradesh. "
  "Pair 4 is wrong: the Kurnool Ultra Mega Solar Park is in Andhra Pradesh.",
  "युग्म 1 और 2 सही हैं: जोधपुर ज़िले का भड़ला और तुमकुरु ज़िले का पावगढ़ विश्व के सबसे बड़े सौर पार्कों में से हैं। "
  "युग्म 3 गलत है: दिल्ली मेट्रो को बिजली देने वाला रीवा अल्ट्रा मेगा सौर पार्क मध्य प्रदेश में है। "
  "युग्म 4 गलत है: कुरनूल अल्ट्रा मेगा सौर पार्क आंध्र प्रदेश में है।",
  "Ministry of New and Renewable Energy -- Solar Park Scheme.",
  "res-solar-parks-pairs")

if __name__ == "__main__":
    write("geo_l2_t14_resources.sql")
