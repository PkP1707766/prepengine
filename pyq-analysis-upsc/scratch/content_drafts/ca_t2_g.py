# -*- coding: utf-8 -*-
"""Current Affairs · Test 2 (April to June 2026) -- part G: Geography.

Places and weather in the news in April-June 2026 -- IMD's below-normal monsoon forecast, the India-New Zealand free trade agreement, the
flow of opium from Myanmar, the Israel-Lebanon ceasefire as UNIFIL nears its end, the Supreme Court's review of the
Aravalli definition, the BSF-BGB talks on the Bangladesh border, the External Affairs Minister's visit to Trinidad and
Tobago, and ties with Seychelles -- set against the static geography behind them. Every fact was searched in the
whole UPSC bank and is one no row tests."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, C, write
from polity_common import C3, C4, T2
from ca_common import MX, finish
from ca_t2_format import FORMAT, POS

d.SUBJECT = "Geography"
d.REQUIRE_CRAFT = True
WR, GM, OC = "World Regions, Water Bodies & Places", "Geomorphology & Earth's Interior", "Oceanography & Hydrosphere"
IP = "Indian Physiography, Climate & Regions"

S(IP, "medium", "On 13 April 2026 the India Meteorological Department forecast the south-west monsoon rainfall at 92 per cent of the Long Period Average (LPA). Consider the following statements:",
  "13 अप्रैल 2026 को भारत मौसम विज्ञान विभाग ने दक्षिण-पश्चिम मानसून की वर्षा दीर्घावधि औसत (एलपीए) का 92 प्रतिशत रहने का पूर्वानुमान दिया। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The LPA now in use is the average all-India rainfall of 1961-2010.",
   "A season with rainfall of 92 per cent of the LPA falls in IMD's 'deficient' category.",
   "A below-normal seasonal forecast implies that the monsoon will set in over Kerala later than usual."],
  ["अब प्रयुक्त एलपीए 1961-2010 की औसत अखिल भारतीय वर्षा है।",
   "एलपीए के 92 प्रतिशत वर्षा वाला मौसम आईएमडी की ‘कमी वाली’ श्रेणी में आता है।",
   "सामान्य से कम का मौसमी पूर्वानुमान यह दर्शाता है कि मानसून केरल पर सामान्य से देर से पहुँचेगा।"],
  C3, 3,
  "None of the statements is correct. IMD forecasts the June-September rainfall over the country as a percentage of the Long Period Average, now 87 cm (the 1971-2020 mean, which in 2022 replaced the 1961-2010 mean of 88 cm), and grades a season as deficient (below 90 per cent), below normal (90-95), normal (96-104), above normal (105-110) or excess (above 110); 92 per cent is thus below normal, not deficient. The April forecast of 92 per cent carried a model error of 5 per cent; IMD cited the expected development of El Niño during the season, and its update of 29 May lowered the figure to 90 per cent. "
  "Statement 3 is wrong: the seasonal total and the date of onset are separate forecasts. IMD issues a distinct forecast of the date on which the monsoon sets in over Kerala, normally around 1 June, and a timely or early onset says little about how much rain the season as a whole will bring.",
  "कोई भी कथन सही नहीं है। आईएमडी देश में जून-सितंबर की वर्षा का पूर्वानुमान दीर्घावधि औसत के प्रतिशत के रूप में देता है, जो अब 87 सेमी (1971-2020 का माध्य, जिसने 2022 में 1961-2010 के 88 सेमी के माध्य का स्थान लिया) है, और मौसम को कमी वाला (90 प्रतिशत से कम), सामान्य से कम (90-95), सामान्य (96-104), सामान्य से अधिक (105-110) या अधिक (110 से ऊपर) श्रेणी में रखता है; इस प्रकार 92 प्रतिशत सामान्य से कम है, कमी वाला नहीं। अप्रैल के 92 प्रतिशत के पूर्वानुमान में 5 प्रतिशत की मॉडल त्रुटि थी; आईएमडी ने मौसम के दौरान एल नीनो के विकसित होने की संभावना बताई, और 29 मई के अद्यतन में आँकड़ा घटाकर 90 प्रतिशत कर दिया। "
  "कथन 3 ग़लत है: मौसम की कुल वर्षा और आगमन की तिथि अलग-अलग पूर्वानुमान हैं। आईएमडी केरल पर मानसून के आगमन की तिथि का अलग पूर्वानुमान देता है, जो सामान्यतः 1 जून के आसपास होती है, और समय पर या जल्दी आगमन से यह पता नहीं चलता कि पूरे मौसम में कितनी वर्षा होगी।",
  "India Meteorological Department and Ministry of Earth Sciences, Long Range Forecast for the 2026 Southwest Monsoon Season Rainfall (13 April 2026) and its update (29 May 2026).",
  "ca-t2-geo-imd-lrf-92-lpa-categories-onset", craft="application")

S(GM, "medium", "On 27 April 2026 India and New Zealand signed a free trade agreement. Consider the following statements about New Zealand:",
  "27 अप्रैल 2026 को भारत और न्यूज़ीलैंड ने एक मुक्त व्यापार समझौते पर हस्ताक्षर किए। न्यूज़ीलैंड के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It lies across the boundary between the Pacific and the Australian plates.",
   "The Southern Alps of its South Island have been raised along a fault where the two plates slide past each other.",
   "Its North and South Islands are separated by the Cook Strait."],
  ["यह प्रशांत और ऑस्ट्रेलियाई प्लेटों की सीमा के आर-पार स्थित है।",
   "इसके दक्षिणी द्वीप के दक्षिणी आल्प्स एक ऐसे भ्रंश के साथ उठे हैं जहाँ दोनों प्लेटें एक-दूसरे के बगल से खिसकती हैं।",
   "इसके उत्तरी और दक्षिणी द्वीप कुक जलडमरूमध्य से अलग होते हैं।"],
  C3, 2,
  "All three statements are correct. New Zealand straddles the boundary of the Pacific and Australian plates. Off the North Island the Pacific plate sinks beneath the Australian, feeding the volcanoes of the Taupo zone, while along the South Island the two plates slide past each other on the Alpine Fault, whose movement, with some squeezing together, has raised the Southern Alps -- which is why the country is so prone to earthquakes. Its islands are the largest emergent part of Zealandia, a sheet of continental crust that lies mostly under the sea. "
  "The North and South Islands are separated by the Cook Strait (the Bass Strait, by contrast, lies between mainland Australia and Tasmania). Under the agreement all Indian exports get duty-free access to New Zealand, while India removes or reduces tariffs on 95 per cent of its imports from New Zealand.",
  "तीनों कथन सही हैं। न्यूज़ीलैंड प्रशांत और ऑस्ट्रेलियाई प्लेटों की सीमा पर फैला है। उत्तरी द्वीप के पास प्रशांत प्लेट ऑस्ट्रेलियाई प्लेट के नीचे धँसती है, जिससे ताउपो क्षेत्र के ज्वालामुखी बनते हैं, जबकि दक्षिणी द्वीप के साथ-साथ दोनों प्लेटें अल्पाइन भ्रंश पर एक-दूसरे के बगल से खिसकती हैं, जिसकी गति ने, कुछ दबाव के साथ, दक्षिणी आल्प्स को ऊपर उठाया है -- इसीलिए यह देश भूकंपों के प्रति इतना संवेदनशील है। इसके द्वीप ज़ीलैंडिया का सबसे बड़ा उभरा हुआ भाग हैं, जो महाद्वीपीय भूपर्पटी का अधिकांशतः समुद्र के नीचे स्थित भूखंड है। "
  "उत्तरी और दक्षिणी द्वीप कुक जलडमरूमध्य से अलग होते हैं (इसके विपरीत बास जलडमरूमध्य ऑस्ट्रेलिया की मुख्य भूमि और तस्मानिया के बीच है)। समझौते के अंतर्गत भारत के सभी निर्यातों को न्यूज़ीलैंड में शुल्क-मुक्त पहुँच मिलती है, जबकि भारत न्यूज़ीलैंड से अपने 95 प्रतिशत आयातों पर शुल्क हटाता या घटाता है।",
  "Ministry of Commerce and Industry and PIB, India-New Zealand Free Trade Agreement (27 April 2026); NCERT, Fundamentals of Physical Geography (Class XI), Chapter 4 (Distribution of Oceans and Continents).",
  "ca-t2-geo-new-zealand-plates-alpine-fault-cook-strait", craft="linkage")

S(WR, "hard", "In June 2026 the Narcotics Control Bureau reported that the flow of opium from Myanmar was affecting India's eastern borders. Consider the following statements:",
  "जून 2026 में स्वापक नियंत्रण ब्यूरो ने बताया कि म्यांमार से अफ़ीम का प्रवाह भारत की पूर्वी सीमाओं को प्रभावित कर रहा है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Golden Triangle is the area where the borders of Myanmar, Laos and Thailand meet.",
   "The Golden Crescent spans parts of Afghanistan, Iran and Pakistan.",
   "Myanmar overtook Afghanistan as the largest source of opium after the Taliban banned poppy cultivation in 2022.",
   "The Irrawaddy forms part of the boundary between Myanmar and Thailand."],
  ["स्वर्णिम त्रिभुज वह क्षेत्र है जहाँ म्यांमार, लाओस और थाईलैंड की सीमाएँ मिलती हैं।",
   "स्वर्णिम अर्धचंद्र अफ़ग़ानिस्तान, ईरान और पाकिस्तान के भागों में फैला है।",
   "तालिबान द्वारा 2022 में पोस्ता की खेती पर प्रतिबंध के बाद म्यांमार अफ़ीम के सबसे बड़े स्रोत के रूप में अफ़ग़ानिस्तान से आगे निकल गया।",
   "इरावदी म्यांमार और थाईलैंड के बीच की सीमा का एक भाग बनाती है।"],
  C4, 2,
  "Statements 1, 2 and 3 are correct. The Golden Triangle centres on the meeting of the Ruak and the Mekong, where Myanmar, Laos and Thailand meet; the Golden Crescent lies across the mountains of Afghanistan, Iran and Pakistan. India lies between the two, which is why both its north-western and its north-eastern frontiers are trafficking routes. After the Taliban banned poppy cultivation in April 2022, Afghanistan's output collapsed and, by the United Nations Office on Drugs and Crime's survey of 2023, Myanmar became the world's largest producer of opium; heroin and methamphetamine now enter India mainly through Manipur and Mizoram. "
  "Statement 4 is wrong: the Irrawaddy rises in the far north of Myanmar and flows south to the Andaman Sea entirely within the country. Stretches of the Myanmar-Thailand boundary follow the Moei and the Salween, and the Mekong forms Myanmar's border with Laos.",
  "कथन 1, 2 और 3 सही हैं। स्वर्णिम त्रिभुज रुआक और मेकांग के संगम पर केंद्रित है, जहाँ म्यांमार, लाओस और थाईलैंड मिलते हैं; स्वर्णिम अर्धचंद्र अफ़ग़ानिस्तान, ईरान और पाकिस्तान के पहाड़ों में फैला है। भारत दोनों के बीच है, इसीलिए उसकी उत्तर-पश्चिमी और उत्तर-पूर्वी, दोनों सीमाएँ तस्करी के मार्ग हैं। तालिबान द्वारा अप्रैल 2022 में पोस्ता की खेती पर प्रतिबंध के बाद अफ़ग़ानिस्तान का उत्पादन गिर गया और संयुक्त राष्ट्र मादक पदार्थ एवं अपराध कार्यालय के 2023 के सर्वेक्षण के अनुसार म्यांमार विश्व का सबसे बड़ा अफ़ीम उत्पादक बन गया; हेरोइन और मेथएम्फ़ेटामीन अब मुख्यतः मणिपुर और मिज़ोरम से भारत में आती हैं। "
  "कथन 4 ग़लत है: इरावदी म्यांमार के सुदूर उत्तर से निकलकर पूरी तरह देश के भीतर दक्षिण की ओर अंडमान सागर तक बहती है। म्यांमार-थाईलैंड सीमा के कुछ भाग मोई और सालवीन के साथ चलते हैं, और मेकांग लाओस के साथ म्यांमार की सीमा बनाती है।",
  "Narcotics Control Bureau, Annual Report (June 2026); United Nations Office on Drugs and Crime, Southeast Asia Opium Survey 2023.",
  "ca-t2-geo-golden-triangle-crescent-myanmar-opium", craft="linkage")

S(WR, "hard", "In April 2026 a ceasefire between Israel and Lebanon was extended, months before the UN peacekeeping force in southern Lebanon is due to end its operations. Consider the following statements:",
  "अप्रैल 2026 में इज़रायल और लेबनान के बीच युद्धविराम बढ़ाया गया, दक्षिणी लेबनान में संयुक्त राष्ट्र शांति सेना के अपना संचालन समाप्त करने से कुछ महीने पहले। निम्नलिखित कथनों पर विचार कीजिए:",
  ["Lebanon has land borders with only two countries, Syria and Israel.",
   "The Blue Line in southern Lebanon is the internationally agreed boundary between Lebanon and Israel.",
   "The Security Council has extended the mandate of the United Nations Interim Force in Lebanon (UNIFIL) for a final time, to the end of 2026.",
   "UNIFIL was first set up in 2000, after Israel withdrew from southern Lebanon."],
  ["लेबनान की स्थल सीमाएँ केवल दो देशों, सीरिया और इज़रायल, से लगती हैं।",
   "दक्षिणी लेबनान की ब्लू लाइन लेबनान और इज़रायल के बीच अंतरराष्ट्रीय रूप से सहमत सीमा है।",
   "सुरक्षा परिषद ने लेबनान में संयुक्त राष्ट्र अंतरिम बल (यूनिफ़िल) का अधिदेश अंतिम बार, 2026 के अंत तक, बढ़ाया है।",
   "यूनिफ़िल पहली बार 2000 में, दक्षिणी लेबनान से इज़रायल की वापसी के बाद, बनाया गया।"],
  C4, 1,
  "Statements 1 and 3 are correct. Lebanon, on the eastern Mediterranean, is bordered by Syria to the north and east and by Israel to the south. UNIFIL was created in March 1978 by Security Council resolutions 425 and 426, after Israel's first invasion of southern Lebanon, and was enlarged after the war of 2006 under resolution 1701, which called for an area free of armed groups between the Blue Line and the Litani river; India has long contributed an infantry battalion to it. In August 2025 resolution 2790 extended the mandate a final time, to 31 December 2026, to be followed by withdrawal within a year. "
  "Statement 2 is wrong: the Blue Line is a line of withdrawal drawn by the United Nations in 2000 to confirm that Israeli forces had left southern Lebanon -- not an agreed international border, whose course is still disputed at points such as the Shebaa Farms. Statement 4 is wrong: UNIFIL dates from 1978; 2000 is the year the Blue Line was drawn.",
  "कथन 1 और 3 सही हैं। पूर्वी भूमध्यसागर पर स्थित लेबनान की सीमा उत्तर और पूर्व में सीरिया से और दक्षिण में इज़रायल से लगती है। यूनिफ़िल मार्च 1978 में सुरक्षा परिषद के संकल्प 425 और 426 से, दक्षिणी लेबनान पर इज़रायल के पहले आक्रमण के बाद, बना और 2006 के युद्ध के बाद संकल्प 1701 के अंतर्गत बढ़ाया गया, जिसने ब्लू लाइन और लितानी नदी के बीच सशस्त्र समूहों से मुक्त क्षेत्र की माँग की; भारत लंबे समय से इसमें एक पैदल सेना बटालियन देता रहा है। अगस्त 2025 में संकल्प 2790 ने अधिदेश अंतिम बार 31 दिसंबर 2026 तक बढ़ाया, जिसके बाद एक वर्ष में वापसी होनी है। "
  "कथन 2 ग़लत है: ब्लू लाइन संयुक्त राष्ट्र द्वारा 2000 में यह पुष्टि करने के लिए खींची गई वापसी-रेखा है कि इज़रायली सेनाएँ दक्षिणी लेबनान छोड़ चुकी हैं -- यह कोई सहमत अंतरराष्ट्रीय सीमा नहीं है, जिसका मार्ग शेबा फ़ार्म्स जैसे बिंदुओं पर अब भी विवादित है। कथन 4 ग़लत है: यूनिफ़िल 1978 से है; 2000 वह वर्ष है जब ब्लू लाइन खींची गई।",
  "United Nations Security Council resolutions 425 and 426 (1978), 1701 (2006) and 2790 (2025); United Nations Interim Force in Lebanon, mandate and Blue Line; Ministry of External Affairs, India and UN peacekeeping.",
  "ca-t2-geo-lebanon-blue-line-unifil-final-mandate", craft="multi")

S(IP, "hard", "In June 2026 the Supreme Court set up an expert committee to examine afresh how the Aravalli hills should be defined. Consider the following statements:",
  "जून 2026 में सर्वोच्च न्यायालय ने अरावली पहाड़ियों की परिभाषा पर नए सिरे से विचार के लिए एक विशेषज्ञ समिति बनाई। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The definition the Court had accepted in November 2025 counted as an Aravalli hill only a landform rising at least 100 metres above its local relief.",
   "By the Forest Survey of India's mapping, most of the Aravalli hills would have met that 100-metre test.",
   "The Delhi Ridge is the northern extension of the Aravalli range.",
   "Pending the review, the Court has barred new mining leases in the Aravallis without its permission."],
  ["नवंबर 2025 में न्यायालय द्वारा स्वीकार की गई परिभाषा केवल उसी भू-आकृति को अरावली पहाड़ी मानती थी जो अपने स्थानीय उच्चावच से कम से कम 100 मीटर ऊँची उठे।",
   "भारतीय वन सर्वेक्षण के मानचित्रण के अनुसार अधिकांश अरावली पहाड़ियाँ उस 100 मीटर की कसौटी पर खरी उतरतीं।",
   "दिल्ली रिज अरावली पर्वतमाला का उत्तरी विस्तार है।",
   "समीक्षा पूरी होने तक न्यायालय ने उसकी अनुमति के बिना अरावली में नए खनन पट्टों पर रोक लगा दी है।"],
  C4, 2,
  "Statements 1, 3 and 4 are correct. In November 2025 the Court accepted a committee's definition: an 'Aravalli hill' is a landform 100 m or more above its local relief, and an 'Aravalli range' is two or more such hills within 500 m of each other. On 29 December 2025 it stayed its own order and barred new mining leases without its leave, and in June 2026 it set up a high-powered committee, headed by the Director General of the Indian Council of Forestry Research and Education, to report by 31 August 2026. The Aravallis, among the oldest fold mountains on Earth, run for about 700 km from Gujarat through Rajasthan and Haryana to Delhi, where the Ridge is their last outcrop; they check the eastward spread of the Thar and recharge the aquifers of the region. "
  "Statement 2 is wrong: of the 12,081 hills mapped by the Forest Survey of India, only 1,048 -- under 9 per cent -- rise 100 m above their local relief, which is why the test was attacked as leaving the rest of the range open to mining and construction.",
  "कथन 1, 3 और 4 सही हैं। नवंबर 2025 में न्यायालय ने एक समिति की परिभाषा स्वीकार की: ‘अरावली पहाड़ी’ वह भू-आकृति है जो अपने स्थानीय उच्चावच से 100 मीटर या अधिक ऊँची हो, और ‘अरावली पर्वतमाला’ ऐसी दो या अधिक पहाड़ियाँ हैं जो एक-दूसरे से 500 मीटर के भीतर हों। 29 दिसंबर 2025 को उसने अपने ही आदेश पर रोक लगाई और उसकी अनुमति के बिना नए खनन पट्टों पर रोक लगाई, और जून 2026 में भारतीय वानिकी अनुसंधान एवं शिक्षा परिषद के महानिदेशक की अध्यक्षता में एक उच्चाधिकार समिति बनाई, जिसे 31 अगस्त 2026 तक रिपोर्ट देनी है। पृथ्वी के सबसे पुराने वलित पर्वतों में गिनी जाने वाली अरावली गुजरात से राजस्थान और हरियाणा होते हुए दिल्ली तक लगभग 700 किमी फैली है, जहाँ रिज उसका अंतिम उभार है; यह थार के पूर्व की ओर फैलाव को रोकती है और क्षेत्र के जलभृतों को भरती है। "
  "कथन 2 ग़लत है: भारतीय वन सर्वेक्षण द्वारा मानचित्रित 12,081 पहाड़ियों में से केवल 1,048 -- 9 प्रतिशत से कम -- अपने स्थानीय उच्चावच से 100 मीटर ऊँची हैं, इसीलिए इस कसौटी की आलोचना हुई कि यह पर्वतमाला के शेष भाग को खनन और निर्माण के लिए खुला छोड़ देती है।",
  "Supreme Court of India, orders in the suo motu matter on the definition of the Aravalli hills (20 November 2025, 29 December 2025 and May-June 2026); Forest Survey of India, mapping of the Aravalli hills; NCERT, Contemporary India I (Class IX), Chapter 2 (Physical Features of India).",
  "ca-t2-geo-aravalli-definition-100m-review", craft="precision")

C(IP, "medium", "In June 2026 the Border Security Force and Border Guard Bangladesh held their 57th conference at the level of Directors-General. Arrange the following States in decreasing order of the length of their border with Bangladesh:",
  "जून 2026 में सीमा सुरक्षा बल और बॉर्डर गार्ड बांग्लादेश ने महानिदेशक स्तर का अपना 57वाँ सम्मेलन किया। बांग्लादेश के साथ अपनी सीमा की लंबाई के घटते क्रम में निम्नलिखित राज्यों को व्यवस्थित कीजिए:",
  ["Assam", "Meghalaya", "Tripura", "Mizoram"],
  ["असम", "मेघालय", "त्रिपुरा", "मिज़ोरम"],
  ["2-3-4-1", "3-2-1-4", "3-2-4-1", "2-3-1-4"], 2,
  "Of the 4,096.7 km India-Bangladesh border, India's longest land border, West Bengal has the longest stretch, 2,216.7 km. Of the four States here, Tripura -- bounded by Bangladesh on three sides -- has 856 km, Meghalaya 443 km, Mizoram 318 km and Assam 263 km, so the order is Tripura, Meghalaya, Mizoram, Assam (3-2-4-1). "
  "The border is guarded by the Border Security Force, which also guards the Pakistan border, while the Sashastra Seema Bal guards the borders with Nepal and Bhutan and the Assam Rifles the border with Myanmar; illegal crossings, smuggling and the fencing of the remaining stretches were on the agenda in June.",
  "4,096.7 किमी की भारत-बांग्लादेश सीमा, जो भारत की सबसे लंबी स्थल सीमा है, में सबसे लंबा भाग पश्चिम बंगाल का है, 2,216.7 किमी। यहाँ दिए चार राज्यों में त्रिपुरा -- जो तीन ओर से बांग्लादेश से घिरा है -- की सीमा 856 किमी, मेघालय की 443 किमी, मिज़ोरम की 318 किमी और असम की 263 किमी है, इसलिए क्रम त्रिपुरा, मेघालय, मिज़ोरम, असम (3-2-4-1) है। "
  "इस सीमा की रक्षा सीमा सुरक्षा बल करता है, जो पाकिस्तान सीमा की भी रक्षा करता है, जबकि सशस्त्र सीमा बल नेपाल और भूटान की सीमाओं और असम राइफ़ल्स म्यांमार की सीमा की रक्षा करते हैं; अवैध आवाजाही, तस्करी और शेष हिस्सों की बाड़बंदी जून की बैठक के विषय थे।",
  "Ministry of Home Affairs, Department of Border Management, lengths of India's land borders, and replies in Parliament; Border Security Force, 57th DG-level Border Coordination Conference (8-11 June 2026).",
  "ca-t2-geo-india-bangladesh-border-lengths-order")
d.ROWS[-1]["question_data"]["craft"] = "precision"

S(WR, "medium", "In May 2026 India's External Affairs Minister visited Trinidad and Tobago, where eight memorandums of understanding were signed. Consider the following statements:",
  "मई 2026 में भारत के विदेश मंत्री ने त्रिनिदाद और टोबैगो की यात्रा की, जहाँ आठ समझौता ज्ञापनों पर हस्ताक्षर हुए। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The country marks the arrival of the first ship of Indian indentured labourers, in 1838, as Indian Arrival Day.",
   "Trinidad lies off the coast of Brazil, near the mouth of the Amazon.",
   "Trinidad and Tobago is a member of the Organization of the Petroleum Exporting Countries (OPEC)."],
  ["यह देश 1838 में भारतीय गिरमिटिया श्रमिकों के पहले जहाज़ के आगमन को भारतीय आगमन दिवस के रूप में मनाता है।",
   "त्रिनिदाद ब्राज़ील के तट के पास, अमेज़न के मुहाने के निकट स्थित है।",
   "त्रिनिदाद और टोबैगो पेट्रोलियम निर्यातक देशों के संगठन (ओपेक) का सदस्य है।"],
  C3, 3,
  "None of the statements is correct. Statement 1 has the wrong year: on 30 May 1845 the Fatel Razack landed the first indentured labourers from India in the Gulf of Paria, and the day has been a public holiday since the 1990s; their descendants form about a third of the population, and several heads of government, including the present Prime Minister, have been of Indian origin; 1838 is when the first Indian indentured labourers reached British Guiana. Statement 2 is wrong: Trinidad, the larger island, lies just off the north-eastern coast of Venezuela across the Gulf of Paria, close to the Orinoco delta, and is geologically a continuation of the South American mainland. "
  "Statement 3 is wrong: although Trinidad and Tobago is the Caribbean's leading producer of oil and natural gas and a large exporter of liquefied natural gas and ammonia, it is not a member of OPEC.",
  "कोई भी कथन सही नहीं है। कथन 1 में वर्ष ग़लत है: 30 मई 1845 को फ़तेल रज़ाक जहाज़ ने भारत से पहले गिरमिटिया श्रमिकों को पारिया की खाड़ी में उतारा, और 1990 के दशक से यह दिन सार्वजनिक अवकाश है; उनके वंशज जनसंख्या का लगभग एक-तिहाई हैं, और वर्तमान प्रधानमंत्री सहित कई शासनाध्यक्ष भारतीय मूल के रहे हैं; 1838 में भारत से पहले गिरमिटिया श्रमिक ब्रिटिश गयाना पहुँचे थे। कथन 2 ग़लत है: बड़ा द्वीप त्रिनिदाद पारिया की खाड़ी के पार वेनेज़ुएला के उत्तर-पूर्वी तट के ठीक पास, ओरिनोको डेल्टा के निकट है, और भूवैज्ञानिक रूप से दक्षिण अमेरिकी मुख्य भूमि का ही विस्तार है। "
  "कथन 3 ग़लत है: यद्यपि त्रिनिदाद और टोबैगो कैरिबियन का प्रमुख तेल और प्राकृतिक गैस उत्पादक और द्रवीकृत प्राकृतिक गैस तथा अमोनिया का बड़ा निर्यातक है, वह ओपेक का सदस्य नहीं है।",
  "Ministry of External Affairs, visit of the External Affairs Minister to Trinidad and Tobago (May 2026) and India-Trinidad and Tobago bilateral brief; Organization of the Petroleum Exporting Countries, member countries.",
  "ca-t2-geo-trinidad-arrival-day-orinoco-not-opec", craft="linkage")

S(GM, "medium", "India's ties with Seychelles, where people of Indian origin form a notable community, were in the news in June 2026. Consider the following statements about Seychelles:",
  "जून 2026 में सेशेल्स के साथ भारत के संबंध, जहाँ भारतीय मूल के लोग एक उल्लेखनीय समुदाय हैं, चर्चा में रहे। सेशेल्स के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Its granite inner islands are a fragment of continental crust that was left behind when India drifted away about 65 million years ago.",
   "It was one of the founding members of the Colombo Security Conclave in 2011."],
  ["इसके ग्रेनाइट वाले भीतरी द्वीप महाद्वीपीय भूपर्पटी का वह टुकड़ा हैं जो लगभग 6.5 करोड़ वर्ष पहले भारत के दूर खिसकने पर पीछे छूट गया।",
   "यह 2011 में कोलंबो सुरक्षा सम्मेलन के संस्थापक सदस्यों में था।"],
  T2, 0,
  "Only statement 1 is correct. Unlike most islands of the open ocean, which are volcanic or coral, the inner islands of Seychelles, around Mahé, are granite: they are a sliver of the old Gondwana landmass left behind when India, having parted from Madagascar, broke away from the Seychelles block about 65 million years ago, at the time of the Deccan volcanism. The outer islands are coral, and one of them, Aldabra, is a UNESCO World Heritage Site home to about 100,000 giant tortoises. "
  "Statement 2 is wrong: the Colombo Security Conclave began in 2011 as a trilateral maritime grouping of India, Sri Lanka and the Maldives; Mauritius joined in 2022, and Bangladesh and Seychelles, earlier observers, have since moved to join it as members.",
  "केवल कथन 1 सही है। खुले महासागर के अधिकांश द्वीपों के विपरीत, जो ज्वालामुखीय या प्रवाल के होते हैं, माहे के आसपास के सेशेल्स के भीतरी द्वीप ग्रेनाइट के हैं: ये पुराने गोंडवाना भूभाग का वह टुकड़ा हैं जो मेडागास्कर से अलग हो चुके भारत के लगभग 6.5 करोड़ वर्ष पहले, दक्कन ज्वालामुखी के समय, सेशेल्स खंड से टूटकर दूर जाने पर पीछे छूट गया। बाहरी द्वीप प्रवाल के हैं, और उनमें से एक, अल्दाब्रा, यूनेस्को विश्व धरोहर स्थल है जहाँ लगभग 1,00,000 विशाल कछुए रहते हैं। "
  "कथन 2 ग़लत है: कोलंबो सुरक्षा सम्मेलन 2011 में भारत, श्रीलंका और मालदीव के त्रिपक्षीय समुद्री समूह के रूप में शुरू हुआ; मॉरीशस 2022 में जुड़ा, और पहले पर्यवेक्षक रहे बांग्लादेश और सेशेल्स तब से सदस्य के रूप में इसमें शामिल होने की ओर बढ़े हैं।",
  "Ministry of External Affairs, India-Seychelles bilateral brief and Colombo Security Conclave statements; UNESCO World Heritage List, Aldabra Atoll (1982); NCERT, Fundamentals of Physical Geography (Class XI), Chapter 4 (Distribution of Oceans and Continents).",
  "ca-t2-geo-seychelles-granitic-microcontinent-csc", craft="linkage")

finish("ca_t2_g.sql", FORMAT, "2026-Q2", update="--update" in sys.argv)
