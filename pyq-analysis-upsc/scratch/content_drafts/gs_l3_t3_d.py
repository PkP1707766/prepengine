# -*- coding: utf-8 -*-
"""Level 3 · Test 3 (GS Integrated Test 3) -- part D: Geography (10) (upsc_l3_cell_targets.mjs 3).
Every fact was grepped against the Level-2 digests, all Level-1 drafts and Level 3 Tests 1-2, and is one none of them
tests: tin in Chhattisgarh; the Bhupen Hazarika, Atal, Anji Khad and Sudarshan bridges; the Siberian winter high;
why the Bay of Bengal breeds more cyclones; Lake Turkana; the North Atlantic Oscillation; the Mahakali and the Gandak;
Davis's cycle of erosion and Penck; the Arctic Council; Malnad and Maidan. MCQ keys are pinned (pos)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, T2

d.SUBJECT = "Geography"
d.REQUIRE_CRAFT = True
FPG = "NCERT Class XI, Fundamentals of Physical Geography"
IPE = "NCERT Class XI, India: Physical Environment"
FHG = "NCERT Class XII, Fundamentals of Human Geography"
IPEc = "NCERT Class XII, India: People and Economy"

# ---------------------------------------------------------------- Resources (e-SI)
A("Resources: Minerals, Energy & Agriculture", "easy",
  "Jharkhand is the only State in India that produces tin concentrates.",
  "झारखंड भारत का एकमात्र राज्य है जो टिन सांद्र का उत्पादन करता है।",
  "India's tin ore, cassiterite, is mined in the Bastar region of Chhattisgarh.",
  "भारत का टिन अयस्क, कैसिटेराइट, छत्तीसगढ़ के बस्तर क्षेत्र में खनित होता है।",
  3,
  "Statement-I is incorrect and Statement-II is correct. Chhattisgarh, not Jharkhand, is India's only producer of tin concentrates, from cassiterite in the Dantewada area of Bastar, much of it worked on a small scale. "
  "Domestic output is tiny, so India imports almost all the tin it uses -- chiefly for solder in electronics and for tin-plating steel for food cans -- which is why tin appears on lists of critical minerals.",
  "कथन-I ग़लत है और कथन-II सही है। झारखंड नहीं, बल्कि छत्तीसगढ़ टिन सांद्र का भारत का एकमात्र उत्पादक है, जो बस्तर के दंतेवाड़ा क्षेत्र के कैसिटेराइट से आता है, जिसका बहुत-सा भाग छोटे पैमाने पर निकाला जाता है। "
  "घरेलू उत्पादन बहुत कम है, इसलिए भारत अपने उपयोग का लगभग सारा टिन आयात करता है -- मुख्यतः इलेक्ट्रॉनिक्स में सोल्डर और खाद्य डिब्बों के लिए इस्पात पर टिन-चढ़ाने के लिए -- इसीलिए टिन महत्त्वपूर्ण खनिजों की सूचियों में आता है।",
  f"Indian Bureau of Mines (Indian Minerals Yearbook: Tin); {IPEc}.",
  "l3-t3-geo-tin-chhattisgarh", craft="precision")

# ---------------------------------------------------------------- Transport, Ports & Human Geography (e-pairs)
P("Transport, Ports & Human Geography", "easy", "Consider the following pairs of bridges and the States or Union Territories in which they are located:",
  "पुलों और उन राज्यों या केंद्रशासित प्रदेशों के निम्नलिखित युग्मों पर विचार कीजिए जिनमें वे स्थित हैं:",
  ["Bhupen Hazarika Setu (Dhola-Sadiya) : Assam",
   "Atal Setu (Mumbai Trans Harbour Link) : Maharashtra",
   "Anji Khad bridge : Jammu and Kashmir",
   "Sudarshan Setu : Gujarat"],
  ["भूपेन हज़ारिका सेतु (ढोला-सदिया) : असम",
   "अटल सेतु (मुंबई ट्रांस हार्बर लिंक) : महाराष्ट्र",
   "अंजी खड्ड पुल : जम्मू और कश्मीर",
   "सुदर्शन सेतु : गुजरात"],
  3,
  "All four pairs are correct. The Bhupen Hazarika Setu crosses the Lohit near Sadiya in eastern Assam and gives road access towards Arunachal Pradesh; the Atal Setu crosses Mumbai's harbour to Navi Mumbai and is India's longest sea bridge; the Anji Khad bridge, on the Udhampur-Srinagar-Baramulla rail link, is India's first cable-stayed railway bridge; and the cable-stayed Sudarshan Setu links Okha on the mainland with Beyt Dwarka island. "
  "Such bridges matter strategically as well as economically, especially in the north-east and in Jammu and Kashmir.",
  "चारों युग्म सही हैं। भूपेन हज़ारिका सेतु पूर्वी असम में सदिया के पास लोहित नदी को पार करता है और अरुणाचल प्रदेश की ओर सड़क मार्ग देता है; अटल सेतु मुंबई के बंदरगाह को पार कर नवी मुंबई तक जाता है और भारत का सबसे लंबा समुद्री पुल है; उधमपुर-श्रीनगर-बारामुला रेल लिंक पर अंजी खड्ड पुल भारत का पहला केबल-आधारित रेल पुल है; और केबल-आधारित सुदर्शन सेतु मुख्य भूमि पर ओखा को बेट द्वारका द्वीप से जोड़ता है। "
  "ऐसे पुल आर्थिक के साथ सामरिक रूप से भी महत्त्वपूर्ण हैं, विशेषकर पूर्वोत्तर और जम्मू-कश्मीर में।",
  f"Ministry of Road Transport and Highways; Ministry of Railways; {IPEc}.",
  "l3-t3-geo-bridges-dhola-atal-anji-sudarshan", craft="recall")

# ---------------------------------------------------------------- Climatology & Biomes (h-MCQ, m-stmt)
M("Climatology & Biomes", "hard",
  "The lowest temperatures recorded in permanently inhabited places, at Oymyakon and Verkhoyansk in north-eastern Siberia, are mainly due to:",
  "स्थायी रूप से बसे स्थानों में दर्ज सबसे कम तापमान, उत्तर-पूर्वी साइबेरिया के ओइम्याकोन और वर्खोयांस्क में, मुख्यतः किस कारण हैं?",
  ["the cold Labrador Current, which flows along the coast of north-eastern Siberia",
   "polar easterlies that bring air straight from the North Pole all through the winter months",
   "clear, calm winter skies under a strong high over a vast land mass far from the sea",
   "their great height above sea level, like that of the Tibetan plateau"],
  ["ठंडी लैब्राडोर धारा, जो उत्तर-पूर्वी साइबेरिया के तट के साथ बहती है",
   "ध्रुवीय पूर्वी पवनें जो सर्दियों के सभी महीनों में सीधे उत्तरी ध्रुव से हवा लाती हैं",
   "समुद्र से दूर विशाल भू-भाग पर प्रबल उच्च दाब के नीचे साफ़, शांत शीतकालीन आकाश",
   "समुद्र तल से उनकी बड़ी ऊँचाई, तिब्बत के पठार जैसी"],
  2,
  "In winter the interior of Asia loses heat rapidly and a vast, intense high-pressure system -- the Siberian High -- forms over it. Under its clear, dry, calm air the ground radiates heat away through the long polar night, and cold, dense air drains into and stagnates in the valleys where these towns stand, creating strong temperature inversions. "
  "Their distance from any moderating sea makes the annual range of temperature enormous: summers can be warm. The Labrador Current is in the north-west Atlantic, and the towns lie at low altitude.",
  "सर्दियों में एशिया का भीतरी भाग तेज़ी से ऊष्मा खोता है और उस पर एक विशाल, प्रबल उच्च दाब तंत्र -- साइबेरियाई उच्च -- बनता है। उसकी साफ़, शुष्क, शांत हवा के नीचे भूमि लंबी ध्रुवीय रात में ऊष्मा विकिरित कर देती है, और ठंडी, घनी हवा उन घाटियों में उतरकर ठहर जाती है जहाँ ये नगर हैं, जिससे प्रबल तापमान व्युत्क्रमण बनता है। "
  "किसी संतुलनकारी समुद्र से उनकी दूरी वार्षिक तापांतर को बहुत बड़ा बनाती है: गर्मियाँ गर्म हो सकती हैं। लैब्राडोर धारा उत्तर-पश्चिमी अटलांटिक में है, और ये नगर कम ऊँचाई पर हैं।",
  f"{FPG} (Atmospheric Circulation; World Climate).",
  "l3-t3-geo-siberian-high-oymyakon", pos=2, craft="inference")

S("Climatology & Biomes", "medium", "Consider the following statements about the North Atlantic Oscillation (NAO):",
  "उत्तरी अटलांटिक दोलन (NAO) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is a seesaw in air pressure between the Icelandic Low and the Azores High.",
   "In its positive phase, stronger westerlies bring mild, wet winters to northern Europe.",
   "It is a seesaw in pressure across the tropical Pacific, between Tahiti and Darwin."],
  ["यह आइसलैंडिक निम्न और एज़ोर्स उच्च के बीच वायुदाब का एक झूला (सी-सॉ) है।",
   "इसकी धनात्मक अवस्था में प्रबल पछुआ पवनें उत्तरी यूरोप में हल्की, नम सर्दियाँ लाती हैं।",
   "यह उष्णकटिबंधीय प्रशांत के पार, ताहिती और डार्विन के बीच, दाब का झूला है।"],
  C3, 1,
  "Statements 1 and 2 are correct. When the pressure difference between the Icelandic Low and the Azores High is large (the positive phase), the westerlies and the storm track are strong and shifted north, giving northern Europe mild, wet winters and southern Europe dry ones; in the negative phase the westerlies weaken and cold air can spill into Europe, bringing harsh winters. "
  "Statement 3 describes the Southern Oscillation, the atmospheric half of the El Niño-Southern Oscillation, which is measured by the pressure difference between Tahiti and Darwin.",
  "कथन 1 और 2 सही हैं। जब आइसलैंडिक निम्न और एज़ोर्स उच्च के बीच दाब का अंतर बड़ा होता है (धनात्मक अवस्था), पछुआ पवनें और तूफ़ान-पथ प्रबल और उत्तर की ओर खिसके होते हैं, जिससे उत्तरी यूरोप में हल्की, नम और दक्षिणी यूरोप में शुष्क सर्दियाँ होती हैं; ऋणात्मक अवस्था में पछुआ पवनें कमज़ोर पड़ती हैं और ठंडी हवा यूरोप में फैल सकती है, जिससे कठोर सर्दियाँ आती हैं। "
  "कथन 3 दक्षिणी दोलन का वर्णन करता है, जो एल नीनो-दक्षिणी दोलन का वायुमंडलीय भाग है और ताहिती तथा डार्विन के बीच दाब के अंतर से मापा जाता है।",
  f"{FPG} (Atmospheric Circulation and Weather Systems).",
  "l3-t3-geo-north-atlantic-oscillation", craft="precision")

# ---------------------------------------------------------------- Indian Physiography, Climate & Regions (h-SI, m-stmt)
A("Indian Physiography, Climate & Regions", "hard",
  "Far more tropical cyclones form over the Bay of Bengal than over the Arabian Sea.",
  "अरब सागर की तुलना में बंगाल की खाड़ी पर कहीं अधिक उष्णकटिबंधीय चक्रवात बनते हैं।",
  "The Bay of Bengal has warmer surface waters, a fresher upper layer from heavy river inflow that keeps heat near the surface, and receives the remnants of Pacific storms that cross South-east Asia.",
  "बंगाल की खाड़ी का सतही जल अधिक गर्म है, भारी नदी प्रवाह से बनी कम खारी ऊपरी परत ऊष्मा को सतह के पास रखती है, और उसे दक्षिण-पूर्व एशिया पार करने वाले प्रशांत तूफ़ानों के अवशेष मिलते हैं।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I. Roughly four cyclones form in the Bay for every one in the Arabian Sea. The Bay's surface stays warmer, its low-salinity surface layer, fed by the Ganga, Brahmaputra and other rivers, stops the cooler water below from mixing up, and low-pressure systems from the western Pacific often move across and redevelop over it; the Arabian Sea is cooler and its storms are often sheared apart. "
  "The balance is shifting, though: as the Arabian Sea has warmed, strong cyclones there have become more frequent in recent decades, putting the west coast at greater risk.",
  "दोनों कथन सही हैं, और कथन-II कथन-I की व्याख्या करता है। अरब सागर में बनने वाले हर एक चक्रवात पर खाड़ी में लगभग चार बनते हैं। खाड़ी की सतह अधिक गर्म रहती है, गंगा, ब्रह्मपुत्र और अन्य नदियों से भरी उसकी कम लवणता वाली सतही परत नीचे के ठंडे पानी को ऊपर मिलने से रोकती है, और पश्चिमी प्रशांत से निम्न दाब तंत्र प्रायः उस पर आकर फिर विकसित होते हैं; अरब सागर ठंडा है और उसके तूफ़ान प्रायः पवन-अपरूपण से बिखर जाते हैं। "
  "पर संतुलन बदल रहा है: अरब सागर के गर्म होने के साथ हाल के दशकों में वहाँ प्रबल चक्रवात अधिक बार आने लगे हैं, जिससे पश्चिमी तट पर ख़तरा बढ़ा है।",
  f"India Meteorological Department (cyclone climatology); {IPE} (Climate).",
  "l3-t3-geo-bay-of-bengal-cyclones", craft="linkage")

S("Indian Physiography, Climate & Regions", "medium", "Consider the following statements about the Karnataka plateau:",
  "कर्नाटक पठार के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is divided into the hilly, wet Malnad in the west and the rolling, drier Maidan to the east.",
   "The Malnad lies along the Western Ghats and is densely forested, with coffee and areca plantations.",
   "The Maidan receives more rainfall than the Malnad."],
  ["यह पश्चिम में पहाड़ी, नम मलनाड और पूर्व में लहरदार, अधिक शुष्क मैदान में बँटा है।",
   "मलनाड पश्चिमी घाट के साथ स्थित है और घने वनों वाला है, जहाँ कॉफ़ी और सुपारी के बाग़ान हैं।",
   "मैदान क्षेत्र मलनाड से अधिक वर्षा पाता है।"],
  C3, 1,
  "Statements 1 and 2 are correct. The Malnad ('hill country'), on the windward side of the Western Ghats in districts such as Shivamogga, Chikkamagaluru and Kodagu, gets heavy south-west monsoon rain and supports evergreen and moist deciduous forest, coffee estates and areca gardens. "
  "Statement 3 is wrong: the Maidan ('open plain') to the east lies in the rain shadow of the Ghats, so it is much drier, with millets, pulses and tank irrigation -- a sharp change in land use over a short distance that shows the Ghats' control on rainfall.",
  "कथन 1 और 2 सही हैं। शिवमोग्गा, चिक्कमगलुरु और कोडगु जैसे ज़िलों में पश्चिमी घाट की पवनाभिमुख ढलान पर स्थित मलनाड ('पहाड़ी प्रदेश') को दक्षिण-पश्चिमी मानसून की भारी वर्षा मिलती है और वहाँ सदाबहार और आर्द्र पर्णपाती वन, कॉफ़ी बाग़ान और सुपारी के बग़ीचे हैं। "
  "कथन 3 ग़लत है: पूर्व का मैदान ('खुला मैदान') घाटों की वृष्टि-छाया में है, इसलिए कहीं अधिक शुष्क है, जहाँ मोटे अनाज, दालें और तालाब सिंचाई है -- थोड़ी दूरी में भूमि उपयोग का यह तीखा बदलाव वर्षा पर घाटों का नियंत्रण दिखाता है।",
  f"{IPE} (Structure and Physiography; Climate).",
  "l3-t3-geo-malnad-maidan", craft="application")

# ---------------------------------------------------------------- World Regions, Water Bodies & Places (m-MCQ, m-stmt)
M("World Regions, Water Bodies & Places", "medium",
  "Lake Turkana, the world's largest permanent desert lake, which is fed mainly by the Omo river, lies mostly in:",
  "तुर्काना झील, विश्व की सबसे बड़ी स्थायी मरुस्थलीय झील, जिसे मुख्यतः ओमो नदी जल देती है, मुख्यतः कहाँ स्थित है?",
  ["Ethiopia", "Tanzania", "Uganda", "Kenya"],
  ["इथियोपिया", "तंज़ानिया", "युगांडा", "केन्या"],
  3,
  "Lake Turkana lies in the arid north of Kenya in the eastern branch of the Great Rift Valley, with only its northern tip in Ethiopia, where the Omo river, which supplies most of its water, rises. With no outlet, the lake is alkaline and slightly salty. "
  "Its shores have yielded some of the most important early human fossils, such as the 'Turkana Boy'. Dams and irrigation on the Omo in Ethiopia have raised fears of a falling lake and of harm to the pastoral and fishing peoples who depend on it.",
  "तुर्काना झील केन्या के शुष्क उत्तर में ग्रेट रिफ़्ट घाटी की पूर्वी शाखा में है, जिसका केवल उत्तरी सिरा इथियोपिया में है, जहाँ से उसका अधिकांश जल देने वाली ओमो नदी निकलती है। कोई निकास न होने के कारण झील क्षारीय और थोड़ी खारी है। "
  "इसके तटों से प्रारंभिक मानव के कुछ सबसे महत्त्वपूर्ण जीवाश्म, जैसे 'तुर्काना बालक', मिले हैं। इथियोपिया में ओमो पर बाँधों और सिंचाई ने झील के घटने और उस पर निर्भर पशुपालक तथा मछुआरे लोगों को हानि की आशंका बढ़ाई है।",
  f"{FPG}; UNESCO World Heritage List (Lake Turkana National Parks).",
  "l3-t3-geo-lake-turkana", pos=3, craft="recall")

S("World Regions, Water Bodies & Places", "medium", "Consider the following statements about the Arctic Council:",
  "आर्कटिक परिषद के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["India has been an observer in the Arctic Council since 2013.",
   "China is a full member of the Arctic Council."],
  ["भारत 2013 से आर्कटिक परिषद में पर्यवेक्षक है।",
   "चीन आर्कटिक परिषद का पूर्ण सदस्य है।"],
  T2, 0,
  "Only statement 1 is correct. The Council's eight members are the states with territory in the Arctic -- Canada, Denmark (for Greenland), Finland, Iceland, Norway, Russia, Sweden and the United States -- and organisations of indigenous Arctic peoples take part as permanent participants. "
  "Countries outside the region, such as India, China, Japan and South Korea, are observers without a vote. India, which runs the Himadri research station in Svalbard and published an Arctic Policy in 2022, follows the Arctic for its links with the monsoon, sea-level rise and new shipping routes.",
  "केवल कथन 1 सही है। परिषद के आठ सदस्य आर्कटिक में भूभाग रखने वाले राज्य हैं -- कनाडा, डेनमार्क (ग्रीनलैंड के लिए), फ़िनलैंड, आइसलैंड, नॉर्वे, रूस, स्वीडन और संयुक्त राज्य अमेरिका -- और आर्कटिक के मूल निवासी लोगों के संगठन स्थायी प्रतिभागी के रूप में भाग लेते हैं। "
  "क्षेत्र के बाहर के देश, जैसे भारत, चीन, जापान और दक्षिण कोरिया, बिना मताधिकार के पर्यवेक्षक हैं। स्वालबार्ड में हिमाद्रि अनुसंधान केंद्र चलाने वाला और 2022 में आर्कटिक नीति प्रकाशित करने वाला भारत मानसून, समुद्र-स्तर वृद्धि और नए जहाज़रानी मार्गों से इसके संबंधों के कारण आर्कटिक पर ध्यान रखता है।",
  "Ministry of Earth Sciences (India's Arctic Policy, 2022); Ministry of External Affairs.",
  "l3-t3-geo-arctic-council", craft="precision")

# ---------------------------------------------------------------- Indian Rivers, Lakes & Wetlands (m-stmt)
S("Indian Rivers, Lakes & Wetlands", "medium", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Mahakali (Sharda) forms part of the boundary between India and Nepal.",
   "The Mahakali Treaty of 1996 provides for the Pancheshwar multipurpose project.",
   "The Gandak, which rises in Nepal, joins the Ganga near Patna."],
  ["महाकाली (शारदा) भारत और नेपाल के बीच सीमा का भाग बनाती है।",
   "1996 की महाकाली संधि पंचेश्वर बहुउद्देशीय परियोजना का उपबंध करती है।",
   "नेपाल से निकलने वाली गंडक पटना के पास गंगा में मिलती है।"],
  C3, 2,
  "All three statements are correct. The Mahakali forms the western boundary between Nepal and Uttarakhand before entering the plains, where it is called the Sharda and joins the Ghaghara; the 1996 treaty covers the Sarada and Tanakpur barrages and the proposed Pancheshwar dam, which has been delayed for decades by disputes over costs and benefits. "
  "The Gandak, known as the Narayani in Nepal, enters Bihar near Valmikinagar and meets the Ganga at Hajipur, opposite Patna; the Gandak project at Valmikinagar is another India-Nepal arrangement. These Himalayan rivers make water-sharing and flood control central to India-Nepal relations.",
  "तीनों कथन सही हैं। महाकाली मैदानों में प्रवेश से पहले नेपाल और उत्तराखंड के बीच पश्चिमी सीमा बनाती है, जहाँ उसे शारदा कहते हैं और वह घाघरा से मिलती है; 1996 की संधि शारदा और टनकपुर बैराज तथा प्रस्तावित पंचेश्वर बाँध को शामिल करती है, जो लागत और लाभ पर विवादों के कारण दशकों से टल रहा है। "
  "नेपाल में नारायणी कहलाने वाली गंडक वाल्मीकिनगर के पास बिहार में प्रवेश करती है और पटना के सामने हाजीपुर में गंगा से मिलती है; वाल्मीकिनगर की गंडक परियोजना भारत-नेपाल की एक और व्यवस्था है। ये हिमालयी नदियाँ जल-बँटवारे और बाढ़ नियंत्रण को भारत-नेपाल संबंधों का केंद्र बनाती हैं।",
  f"{IPE} (Drainage System); Ministry of Jal Shakti.",
  "l3-t3-geo-mahakali-gandak", craft="linkage")

# ---------------------------------------------------------------- Geomorphology & Earth's Interior (m-stmt)
S("Geomorphology & Earth's Interior", "medium", "Consider the following statements about models of landscape evolution:",
  "भू-दृश्य विकास के मॉडलों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["In W.M. Davis's 'cycle of erosion', a landscape passes through stages of youth, maturity and old age.",
   "In Davis's scheme, the end of the cycle is a gently rolling, low surface called a peneplain, with occasional resistant hills called monadnocks.",
   "Walther Penck argued that landforms depend on the rate of uplift relative to the rate of erosion, rather than on time alone."],
  ["डब्ल्यू.एम. डेविस के 'अपरदन चक्र' में भू-दृश्य युवा, प्रौढ़ और वृद्ध अवस्थाओं से गुज़रता है।",
   "डेविस की योजना में चक्र का अंत एक हल्की लहरदार, निचली सतह है जिसे समप्राय मैदान (पेनीप्लेन) कहते हैं, जिस पर कहीं-कहीं प्रतिरोधी पहाड़ियाँ (मोनाडनॉक) होती हैं।",
   "वाल्टर पेंक का तर्क था कि भू-आकृतियाँ केवल समय पर नहीं, बल्कि अपरदन की दर की तुलना में उत्थान की दर पर निर्भर करती हैं।"],
  C3, 2,
  "All three statements are correct. Davis, writing around 1900, imagined a landmass uplifted quickly and then worn down: youthful landscapes have deep V-shaped valleys and waterfalls, mature ones the greatest relief and well-developed drainage, and old ones broad valleys, meandering rivers and finally a peneplain. "
  "Penck objected that uplift and erosion usually go on together, so slope forms reflect their relative rates, not a fixed sequence of stages. Both ideas are used to read landscapes such as the old, worn-down surfaces of the Peninsular plateau.",
  "तीनों कथन सही हैं। लगभग 1900 में लिखते हुए डेविस ने एक ऐसे भूभाग की कल्पना की जो तेज़ी से उठा और फिर घिसता गया: युवा भू-दृश्यों में गहरी V-आकार घाटियाँ और जलप्रपात होते हैं, प्रौढ़ में सबसे अधिक उच्चावच और विकसित अपवाह, और वृद्ध में चौड़ी घाटियाँ, विसर्पी नदियाँ और अंत में समप्राय मैदान। "
  "पेंक ने आपत्ति की कि उत्थान और अपरदन सामान्यतः साथ-साथ चलते हैं, इसलिए ढलान के रूप उनकी सापेक्ष दरों को दिखाते हैं, अवस्थाओं के किसी तय क्रम को नहीं। दोनों विचार प्रायद्वीपीय पठार की पुरानी, घिसी सतहों जैसे भू-दृश्यों को समझने में प्रयुक्त होते हैं।",
  f"{FPG} (Geomorphic Processes; Landforms and their Evolution).",
  "l3-t3-geo-davis-penck-erosion-cycle", craft="precision")

write("gs_l3_t3_d.sql")
