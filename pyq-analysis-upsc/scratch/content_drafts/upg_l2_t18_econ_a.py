# -*- coding: utf-8 -*-
"""Level 2 · Test 18 (Economy 4: Agriculture, Industry, Infrastructure and Welfare) -- depth audit of 2026-10-05,
part A: Agriculture & Food Economy and Inclusive Growth, Welfare & Demography (docs/upsc-question-design-standard.md
§6). Part B (upg_l2_t18_econ_b.py) has Industry, Infrastructure, Energy & Services and the tags for the kept rows.

Before the audit the test had analytic 21, precision 26, recall 59. Part A rewrites 16 recall rows in place
with the same concept id, type and difficulty:
  - cases: a migrant worker drawing rations in Surat, a hail-hit farmer insured under the PMFBY, and a
    town's dependency ratio worked out from its age groups;
  - mechanisms: why the Green Revolution began with wheat and favoured larger farmers, what the Soil
    Health Card corrects, how the food subsidy arises, what an export ban does to farm prices, why
    PM-KISAN leaves out tenants, why the MSP is announced before sowing, why a falling farm share does
    not mean falling rice output, why Jan Dhan carries transfers, and why houses are put in women's names;
  - precision: near-miss versions of the farm schemes, e-NAM and the interest subvention.
Leaks fixed after the cue check: "short-term crop loans" in the KCC row (answered the easy KCC statement) and
"APMC Acts are State laws" in the e-NAM row (answered the two model-Act rows, as the old row also did).
The bank-wide search caught three repeats. Test 16's gd-development-indicators-easy already asks why output per
worker is low in agriculture, so the share-rice row tests share against level instead; Test 14's
hum-demographic-dividend already defines the dividend, so the dependency row is a calculation; and Test 3's
NFSA case already tests free grain, so the food-subsidy statement rests on the economic cost alone.
One fact was corrected on the way: the Essential Commodities (Amendment) Act, 2020 was one of the three farm
laws repealed in 2021, so no statement now rests on its price triggers.
Leaks avoided while drafting:
  - free or cheap farm power (answers the discom AR's statement II), so the irrigation-sources row was left;
  - paddy as a thirsty crop (the diversification AR), India as a rice exporter (the old share-rice row);
  - free grain in ration shops against an MSP-is-the-ration-price statement (the old msp-basics row);
  - 'Maan-dhan' as a pension (the social-security pairs), cheap urea (the NBS row's statement 2), and
    insurance being optional for loanee farmers (the PMFBY row's statement 3);
  - an old-age dependency ratio (the TFR row's statement 3) and Engel's law (the cobweb-Engel row)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write_updates, CODE
from polity_common import C3, C4, T2

d.SUBJECT = "Economy"
d.REQUIRE_CRAFT = True
AG = "Agriculture & Food Economy"
IG = "Inclusive Growth, Welfare & Demography"
NCI = "NCERT Class XI, Indian Economic Development"
MOA = "Ministry of Agriculture and Farmers Welfare."

# ================================================================ MCQs (4)
M(AG, "easy", "The Green Revolution of the mid-1960s first transformed the output of wheat rather than rice. The main reason is that:",
  "1960 के दशक के मध्य की हरित क्रांति ने पहले धान के बजाय गेहूँ के उत्पादन को बदला। इसका मुख्य कारण यह है कि:",
  ["the first high-yielding seeds were of wheat and did best where canals and tube wells existed",
   "wheat is a kharif crop that depends entirely on monsoon rain, so it needed no new irrigation at all",
   "rice is grown only in hill areas, where the new seeds and fertilisers could not be used by farmers",
   "the Third Plan had given priority to pulses over rice, so rice research was stopped for a decade"],
  ["पहले अधिक उपज वाले बीज गेहूँ के थे और वे वहाँ सबसे अच्छे चले जहाँ नहरें और नलकूप थे",
   "गेहूँ ख़रीफ़ फ़सल है जो पूरी तरह मानसूनी वर्षा पर निर्भर है, इसलिए उसे नई सिंचाई की आवश्यकता ही नहीं थी",
   "धान केवल पहाड़ी क्षेत्रों में उगता है, जहाँ किसान नए बीज और उर्वरक उपयोग नहीं कर सकते थे",
   "तीसरी योजना ने धान के बजाय दालों को प्राथमिकता दी थी, इसलिए धान का शोध एक दशक तक रुका रहा"],
  0,
  "The dwarf, high-yielding wheat varieties bred in Mexico gave large yields only with assured water and heavy doses of fertiliser, so they spread first in the irrigated plains of Punjab, Haryana and western Uttar Pradesh, where canals and tube wells already existed and farms were larger. "
  "Rice varieties such as IR8 came a little later and spread more slowly in the rain-fed east. Wheat is a rabi crop grown with irrigation in winter, and rice is grown across the plains, deltas and coasts.",
  "मेक्सिको में विकसित बौनी, अधिक उपज वाली गेहूँ की क़िस्में केवल सुनिश्चित पानी और उर्वरकों की भारी मात्रा के साथ बड़ी उपज देती थीं, इसलिए वे पहले पंजाब, हरियाणा और पश्चिमी उत्तर प्रदेश के सिंचित मैदानों में फैलीं, जहाँ नहरें और नलकूप पहले से थे और खेत बड़े थे। "
  "IR8 जैसी धान की क़िस्में थोड़ी बाद में आईं और वर्षा-आधारित पूर्व में धीरे फैलीं। गेहूँ सर्दियों में सिंचाई से उगाई जाने वाली रबी फ़सल है, और धान मैदानों, डेल्टाओं और तटों पर उगता है।",
  NCI, "ag-green-revolution-wheat-easy", craft="linkage")

M(AG, "medium", "A migrant worker from a village in Bihar works in Surat, while his family stays in the village. Under 'One Nation One Ration Card':",
  "बिहार के एक गाँव का प्रवासी मज़दूर सूरत में काम करता है, जबकि उसका परिवार गाँव में रहता है। 'वन नेशन वन राशन कार्ड' के तहत:",
  ["he can draw part of the household's grain in Surat while his family draws the rest in the village",
   "he must first transfer the household's ration card from Bihar to Gujarat before drawing any grain",
   "only the family can draw grain, since rations are tied to the shop where the card was first issued",
   "he receives cash in place of grain whenever he buys food outside his home State of Bihar"],
  ["वह परिवार के अनाज का एक भाग सूरत में ले सकता है जबकि उसका परिवार शेष गाँव में लेता है",
   "उसे कोई भी अनाज लेने से पहले परिवार का राशन कार्ड बिहार से गुजरात स्थानांतरित कराना होगा",
   "केवल परिवार अनाज ले सकता है, क्योंकि राशन उसी दुकान से जुड़ा है जहाँ कार्ड पहली बार जारी हुआ",
   "जब भी वह बिहार से बाहर भोजन ख़रीदता है, उसे अनाज के बदले नक़द मिलता है"],
  0,
  "One Nation One Ration Card makes the entitlement portable: because ration cards are seeded with Aadhaar and fair price shops use electronic point-of-sale devices, a beneficiary can authenticate at any shop in the country, and the system records how much of the household's monthly quota has been drawn. "
  "So the worker can take his share where he works while his family draws the rest at home, without transferring the card; the scheme moves grain, not cash.",
  "वन नेशन वन राशन कार्ड हक़ को सुवाह्य बनाता है: चूँकि राशन कार्ड आधार से जुड़े हैं और उचित मूल्य दुकानें इलेक्ट्रॉनिक पॉइंट-ऑफ़-सेल उपकरणों का उपयोग करती हैं, लाभार्थी देश की किसी भी दुकान पर प्रमाणीकरण कर सकता है, और प्रणाली दर्ज करती है कि परिवार के मासिक कोटे का कितना भाग लिया जा चुका है। "
  "इसलिए मज़दूर जहाँ काम करता है वहाँ अपना हिस्सा ले सकता है जबकि परिवार शेष घर पर लेता है, कार्ड स्थानांतरित किए बिना; योजना अनाज देती है, नक़द नहीं।",
  "Department of Food and Public Distribution -- One Nation One Ration Card.", "ag-onorc", craft="application")

M(AG, "medium", "The Soil Health Card scheme, launched in 2015, reports the nutrients in a farmer's soil and recommends the fertiliser it needs. The main problem it is meant to correct is:",
  "2015 में शुरू की गई मृदा स्वास्थ्य कार्ड योजना किसान की मिट्टी के पोषक तत्व बताती है और आवश्यक उर्वरक की सिफ़ारिश करती है। यह मुख्यतः किस समस्या को सुधारने के लिए है?",
  ["unbalanced fertiliser use, with too much nitrogen and too little of other nutrients",
   "a shortage of land records that keeps farmers from getting bank loans for their crops",
   "the lack of an organic certificate needed to export farm produce to Europe",
   "losses from floods, for which farmers have had no form of crop insurance"],
  ["असंतुलित उर्वरक उपयोग, जिसमें नाइट्रोजन बहुत अधिक और अन्य पोषक तत्व बहुत कम होते हैं",
   "भूमि अभिलेखों की कमी, जिससे किसानों को फ़सलों के लिए बैंक ऋण नहीं मिल पाता",
   "यूरोप को कृषि उपज निर्यात करने के लिए आवश्यक जैविक प्रमाणपत्र का अभाव",
   "बाढ़ से होने वाली हानियाँ, जिनके लिए किसानों के पास कोई फ़सल बीमा नहीं रहा"],
  0,
  "Many farmers apply too much nitrogen, mostly as urea, and too little phosphorus, potash, sulphur and micronutrients, so yields stall and soils degrade. "
  "The card reports a dozen parameters -- nitrogen, phosphorus, potassium, sulphur, micronutrients, pH and others -- and recommends a balanced dose for the crop, so that the farmer applies what the soil actually lacks.",
  "बहुत-से किसान बहुत अधिक नाइट्रोजन, अधिकतर यूरिया के रूप में, और बहुत कम फ़ॉस्फ़ोरस, पोटाश, गंधक और सूक्ष्म पोषक तत्व डालते हैं, जिससे उपज ठहर जाती है और मिट्टी बिगड़ती है। "
  "कार्ड लगभग एक दर्जन मानदंड बताता है, जैसे नाइट्रोजन, फ़ॉस्फ़ोरस, पोटैशियम, गंधक, सूक्ष्म पोषक तत्व, pH आदि, और फ़सल के लिए संतुलित मात्रा की सिफ़ारिश करता है, ताकि किसान वही डाले जिसकी मिट्टी में वास्तव में कमी है।",
  MOA, "ag-soil-health-card", craft="linkage")

M(IG, "easy", "In a town, 3,000 people are aged under 15, 1,000 are over 64 and 6,000 are aged 15 to 64. Its dependency ratio, per 100 people of working age, is about:",
  "एक कस्बे में 3,000 लोग 15 वर्ष से कम, 1,000 लोग 64 वर्ष से अधिक और 6,000 लोग 15 से 64 वर्ष के हैं। कार्यशील आयु के प्रति 100 लोगों पर उसका निर्भरता अनुपात लगभग है:",
  ["67", "40", "50", "150"],
  ["67", "40", "50", "150"],
  0,
  "The dependency ratio relates those usually too young or too old to work to those of working age: (3,000 + 1,000) / 6,000 x 100 = about 67. "
  "Taking dependants as a share of the whole population gives 40; counting children alone gives the child dependency ratio, 50; and 150 turns the ratio upside down. A falling ratio means each worker supports fewer dependants -- the basis of the 'demographic dividend' -- though in India the old-age part of the ratio has begun to rise even as the child part falls.",
  "निर्भरता अनुपात सामान्यतः काम करने के लिए बहुत छोटे या बहुत बूढ़े लोगों को कार्यशील आयु के लोगों से जोड़ता है: (3,000 + 1,000) / 6,000 x 100 = लगभग 67। "
  "आश्रितों को पूरी जनसंख्या के अंश के रूप में लेने पर 40 आता है; केवल बच्चों को गिनने पर बाल निर्भरता अनुपात 50 आता है; और 150 अनुपात को उलट देता है। घटते अनुपात का अर्थ है कि हर श्रमिक कम आश्रितों को सहारा देता है, यही 'जनसांख्यिकीय लाभांश' का आधार है, हालाँकि भारत में बाल भाग घटने के साथ-साथ अनुपात का वृद्धावस्था भाग बढ़ने लगा है।",
  NCI, "ig-dependency-ratio-easy", craft="application")

# ================================================================ pairs (1)
P(AG, "medium", "Consider the following pairs of schemes and their purposes:",
  "योजनाओं और उनके उद्देश्यों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["PM-PRANAM : Reducing the use of chemical fertilisers", "Rashtriya Gokul Mission : Development of indigenous cattle breeds",
   "Agriculture Infrastructure Fund : Insurance for crops stored in warehouses", "PM Krishi Sinchayee Yojana : Expanding irrigation and water-use efficiency"],
  ["PM-PRANAM : रासायनिक उर्वरकों का उपयोग घटाना", "राष्ट्रीय गोकुल मिशन : देशी गोवंश नस्लों का विकास",
   "कृषि अवसंरचना कोष : गोदामों में रखी फ़सलों का बीमा", "प्रधानमंत्री कृषि सिंचाई योजना : सिंचाई और जल-उपयोग दक्षता का विस्तार"],
  2,
  "Three pairs are correct. PM-PRANAM, announced in the Budget 2023-24, is meant to reward States that cut chemical fertiliser use with a share of the subsidy saved; the Rashtriya Gokul Mission (2014) works to conserve and improve indigenous bovine breeds such as Gir and Sahiwal; and PM Krishi Sinchayee Yojana (2015) runs on the mottos 'Har Khet Ko Pani' and 'More Crop per Drop'. "
  "Pair 3 is the near-miss: the ₹1 lakh crore Agriculture Infrastructure Fund (2020) is a financing facility, giving interest subvention and credit guarantees on loans for warehouses, cold storage and processing units -- it insures neither the crops nor the buildings.",
  "तीन युग्म सही हैं। बजट 2023-24 में घोषित PM-PRANAM का उद्देश्य रासायनिक उर्वरक का उपयोग घटाने वाले राज्यों को बचाई गई सब्सिडी का एक भाग देकर पुरस्कृत करना है; राष्ट्रीय गोकुल मिशन (2014) गिर और साहीवाल जैसी देशी गोवंश नस्लों के संरक्षण और सुधार के लिए काम करता है; और प्रधानमंत्री कृषि सिंचाई योजना (2015) 'हर खेत को पानी' और 'प्रति बूँद अधिक फ़सल' के ध्येय पर चलती है। "
  "युग्म 3 निकट-भ्रम है: ₹1 लाख करोड़ का कृषि अवसंरचना कोष (2020) एक वित्तपोषण सुविधा है, जो गोदामों, शीत भंडारों और प्रसंस्करण इकाइयों के ऋणों पर ब्याज छूट और ऋण गारंटी देता है; यह न फ़सलों का बीमा करता है, न भवनों का।",
  MOA, "ag-schemes-pairs", craft="precision")

# ================================================================ two-statement rows (5)
S(AG, "easy", "A farmer who has a Kisan Credit Card insures her kharif crop under the Pradhan Mantri Fasal Bima Yojana. A hailstorm then destroys her standing crop, though the fields around hers escape damage. Consider the following statements:",
  "किसान क्रेडिट कार्ड रखने वाली एक किसान अपनी ख़रीफ़ फ़सल का प्रधानमंत्री फ़सल बीमा योजना के तहत बीमा कराती है। फिर ओलावृष्टि उसकी खड़ी फ़सल नष्ट कर देती है, जबकि उसके आसपास के खेत बच जाते हैं। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Kisan Credit Card gives farmers long-term loans for buying land.",
   "She can be compensated for her loss even though the neighbouring fields were not damaged."],
  ["किसान क्रेडिट कार्ड किसानों को भूमि ख़रीदने के लिए दीर्घकालिक ऋण देता है।",
   "पड़ोसी खेतों को नुक़सान न होने के बावजूद उसे अपनी हानि की भरपाई मिल सकती है।"],
  T2, 1,
  "Only statement 2 is correct. Under the PMFBY, hailstorms, like landslides and inundation, are 'localised calamities': losses are assessed for the individual insured farm rather than for the whole area, so a farmer whose field alone is hit can still be paid. "
  "Statement 1 is wrong: the Kisan Credit Card gives short-term credit for crop needs -- seed, fertiliser, labour -- and working capital for allied activities, repaid after the harvest; it is not a loan to buy land.",
  "केवल कथन 2 सही है। PMFBY के तहत ओलावृष्टि, भूस्खलन और जलभराव की तरह, 'स्थानीय आपदा' है: हानि का आकलन पूरे क्षेत्र के बजाय अलग-अलग बीमित खेत के लिए होता है, इसलिए जिस किसान का केवल अपना खेत प्रभावित हुआ हो, उसे भी भुगतान मिल सकता है। "
  "कथन 1 गलत है: किसान क्रेडिट कार्ड फ़सल की ज़रूरतों, यानी बीज, उर्वरक, मज़दूरी, के लिए और संबद्ध गतिविधियों की कार्यशील पूँजी के लिए अल्पकालिक ऋण देता है, जो फ़सल के बाद चुकाया जाता है; यह भूमि ख़रीदने का ऋण नहीं है।",
  MOA, "ag-credit-insurance-easy", craft="application")

S(AG, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Food Corporation of India stores foodgrains procured from farmers.",
   "Since the public distribution system issues grain far below what it costs to buy, store and move, the Centre has to meet the gap through the food subsidy."],
  ["भारतीय खाद्य निगम किसानों से ख़रीदे गए अनाज का भंडारण करता है।",
   "चूँकि सार्वजनिक वितरण प्रणाली अनाज उसकी ख़रीद, भंडारण और परिवहन की लागत से बहुत कम पर जारी करती है, इसलिए केंद्र को यह अंतर खाद्य सब्सिडी से पूरा करना पड़ता है।"],
  T2, 2,
  "Both statements are correct. The FCI buys wheat and rice at the minimum support price, stores and moves them, and hands them to the States for distribution. Its 'economic cost' -- the MSP plus the cost of procuring, storing, moving and financing the grain -- is far above the price at which the grain is issued, which since 2023 has been zero for over 80 crore people; the Centre pays the difference as the food subsidy.",
  "दोनों कथन सही हैं। FCI गेहूँ और चावल न्यूनतम समर्थन मूल्य पर ख़रीदता है, उनका भंडारण और परिवहन करता है, और वितरण के लिए राज्यों को देता है। उसकी 'आर्थिक लागत', यानी MSP के साथ अनाज की ख़रीद, भंडारण, परिवहन और वित्तपोषण की लागत, उस मूल्य से कहीं अधिक है जिस पर अनाज जारी होता है, जो 2023 से 80 करोड़ से अधिक लोगों के लिए शून्य है; केंद्र यह अंतर खाद्य सब्सिडी के रूप में चुकाता है।",
  "Department of Food and Public Distribution.", "ag-fci-pds-price-easy", craft="linkage")

S(AG, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The early gains of the Green Revolution went mostly to larger farmers, since the new seeds, fertilisers and pesticides cost money that small farmers often lacked.",
   "Tractors and harvesters are examples of farm mechanisation."],
  ["हरित क्रांति के आरंभिक लाभ अधिकतर बड़े किसानों को मिले, क्योंकि नए बीजों, उर्वरकों और कीटनाशकों पर पैसा लगता था जो छोटे किसानों के पास प्रायः नहीं होता था।",
   "ट्रैक्टर और हार्वेस्टर कृषि यंत्रीकरण के उदाहरण हैं।"],
  T2, 2,
  "Both statements are correct. The high-yielding varieties needed a package of purchased inputs, so at first only farmers who could afford them gained -- one reason the Green Revolution widened gaps between large and small farmers. "
  "As the government extended cheap credit and subsidised inputs, small farmers too adopted the new seeds and their yields rose. Mechanisation, with tractors, threshers and combine harvesters, spread alongside it.",
  "दोनों कथन सही हैं। अधिक उपज वाली क़िस्मों के लिए ख़रीदे गए आदानों का एक पूरा पैकेज चाहिए था, इसलिए शुरू में केवल वही किसान लाभ में रहे जो उन्हें ख़रीद सकते थे; यही एक कारण है कि हरित क्रांति ने बड़े और छोटे किसानों के बीच अंतर बढ़ाया। "
  "जब सरकार ने सस्ता ऋण और सब्सिडी वाले आदान उपलब्ध कराए, तब छोटे किसानों ने भी नए बीज अपनाए और उनकी उपज बढ़ी। ट्रैक्टर, थ्रेशर और कंबाइन हार्वेस्टर के साथ यंत्रीकरण भी साथ-साथ फैला।",
  NCI, "ag-green-revolution-mechanisation-easy", craft="linkage")

S(AG, "easy", "Consider the following statements about the minimum support price (MSP):",
  "न्यूनतम समर्थन मूल्य (MSP) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Announcing the MSP before the sowing season helps farmers decide which crop to grow.",
   "Once the MSP for a crop is announced, farmers must sell their entire output of it to the government."],
  ["बुवाई के मौसम से पहले MSP घोषित करने से किसानों को यह तय करने में मदद मिलती है कि कौन-सी फ़सल उगाएँ।",
   "किसी फ़सल का MSP घोषित होने के बाद किसानों को उसकी पूरी उपज सरकार को बेचनी होती है।"],
  T2, 0,
  "Only statement 1 is correct. Knowing the floor price in advance lets a farmer compare the likely returns from different crops before committing land, seed and fertiliser. "
  "Statement 2 is wrong: the MSP is a floor, not an obligation. Farmers may sell to private traders at any price; the government buys only what is offered at its procurement centres, and in practice it buys in large quantities mainly wheat and rice in a few States.",
  "केवल कथन 1 सही है। न्यूनतम मूल्य पहले से जानने पर किसान भूमि, बीज और उर्वरक लगाने से पहले अलग-अलग फ़सलों के संभावित लाभ की तुलना कर सकता है। "
  "कथन 2 गलत है: MSP एक न्यूनतम सीमा है, बाध्यता नहीं। किसान निजी व्यापारियों को किसी भी मूल्य पर बेच सकते हैं; सरकार केवल वही ख़रीदती है जो उसके क्रय केंद्रों पर लाया जाता है, और व्यवहार में बड़ी मात्रा में मुख्यतः कुछ राज्यों में गेहूँ और धान ही ख़रीदती है।",
  "Commission for Agricultural Costs and Prices.", "ag-msp-basics-easy", craft="linkage")

S(AG, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Agriculture's share of India's GDP has fallen over the past three decades.",
   "This means that India now grows less rice than it did in 1990-91."],
  ["पिछले तीन दशकों में भारत के GDP में कृषि का हिस्सा घटा है।",
   "इसका अर्थ है कि भारत अब 1990-91 की तुलना में कम चावल उगाता है।"],
  T2, 0,
  "Only statement 1 is correct: agriculture and allied activities have fallen from close to a third of GDP around 1990 to under a fifth today. "
  "Statement 2 is wrong because a share is a ratio, not a level. Rice output has roughly doubled, from about 74 million tonnes in 1990-91 to about 150 million tonnes in 2024-25, and India has become the world's largest exporter of rice; agriculture's share fell because industry and services grew much faster than farming did.",
  "केवल कथन 1 सही है: कृषि और संबद्ध गतिविधियाँ 1990 के आसपास GDP के लगभग एक-तिहाई से घटकर आज पाँचवें भाग से कम रह गई हैं। "
  "कथन 2 गलत है क्योंकि हिस्सा एक अनुपात है, स्तर नहीं। चावल उत्पादन लगभग दोगुना हुआ है, 1990-91 के लगभग 7.4 करोड़ टन से 2024-25 में लगभग 15 करोड़ टन, और भारत विश्व का सबसे बड़ा चावल निर्यातक बन गया है; कृषि का हिस्सा इसलिए घटा क्योंकि उद्योग और सेवाएँ खेती की तुलना में कहीं तेज़ी से बढ़ीं।",
  "NCERT Class XI, Indian Economic Development; Ministry of Agriculture and Farmers Welfare -- Agricultural Statistics at a Glance.", "ag-share-rice-easy", craft="inference")

# ================================================================ three-statement rows (6)
S(AG, "hard", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["India banned exports of non-basmati white rice in 2023 to keep domestic prices in check.",
   "An export ban on a crop usually raises the price that farmers growing it receive at home.",
   "Stock limits on traders can be imposed under the Essential Commodities Act, 1955."],
  ["भारत ने घरेलू क़ीमतें नियंत्रण में रखने के लिए 2023 में ग़ैर-बासमती सफ़ेद चावल के निर्यात पर रोक लगाई।",
   "किसी फ़सल के निर्यात पर रोक सामान्यतः उसे उगाने वाले किसानों को देश में मिलने वाली क़ीमत बढ़ा देती है।",
   "आवश्यक वस्तु अधिनियम, 1955 के तहत व्यापारियों पर भंडार सीमाएँ लगाई जा सकती हैं।"],
  C3, 1,
  "Statements 1 and 3 are correct. A ban keeps grain that would have been sold abroad in the home market, so domestic supply rises and prices fall -- good for consumers when food inflation is high, but it cuts the price farmers receive, which is why statement 2 is wrong. The ban of July 2023 was lifted in 2024 once stocks were comfortable. "
  "Stock limits, imposed on wheat and pulses in recent years, cap how much traders may hold so as to stop hoarding. The 1955 Act remains in force: the Essential Commodities (Amendment) Act, 2020, one of the three farm laws, was repealed in 2021.",
  "कथन 1 और 3 सही हैं। रोक उस अनाज को देश के बाज़ार में रखती है जो विदेश में बिकता, इसलिए घरेलू आपूर्ति बढ़ती है और क़ीमतें गिरती हैं; खाद्य मुद्रास्फीति ऊँची होने पर यह उपभोक्ताओं के लिए अच्छा है, पर किसानों को मिलने वाली क़ीमत घटती है, इसीलिए कथन 2 गलत है। जुलाई 2023 की रोक 2024 में भंडार पर्याप्त होने पर हटाई गई। "
  "हाल के वर्षों में गेहूँ और दालों पर लगाई गई भंडार सीमाएँ तय करती हैं कि व्यापारी कितना रख सकते हैं, ताकि जमाख़ोरी रुके। 1955 का अधिनियम लागू है: आवश्यक वस्तु (संशोधन) अधिनियम, 2020, जो तीन कृषि क़ानूनों में से एक था, 2021 में निरस्त कर दिया गया।",
  "Department of Consumer Affairs; Directorate General of Foreign Trade.", "ag-export-ban-eca", craft="inference")

S(AG, "medium", "Consider the following statements about agricultural marketing:",
  "कृषि विपणन के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The National Agriculture Market (e-NAM) platform is run by the Small Farmers' Agribusiness Consortium.",
   "The National Agriculture Market (e-NAM) was launched in 2020.",
   "e-NAM has replaced the APMC mandis with a single national market."],
  ["राष्ट्रीय कृषि बाज़ार (e-NAM) मंच लघु कृषक कृषि-व्यापार संघ (SFAC) द्वारा चलाया जाता है।",
   "राष्ट्रीय कृषि बाज़ार (e-NAM) 2020 में शुरू किया गया।",
   "e-NAM ने APMC मंडियों के स्थान पर एक एकल राष्ट्रीय बाज़ार बना दिया है।"],
  C3, 0,
  "Only statement 1 is correct: the Small Farmers' Agribusiness Consortium, under the agriculture ministry, runs the platform. Statement 2 is wrong: e-NAM was launched in 2016. Statement 3 is the near-miss: since agricultural markets are a State subject, the mandis remain under State APMC laws, and e-NAM does not replace them -- it links existing APMC markets, now more than 1,400 of them, on a common online platform so that buyers elsewhere can bid; trade across mandis and States has grown only slowly.",
  "केवल कथन 1 सही है: कृषि मंत्रालय के अधीन लघु कृषक कृषि-व्यापार संघ यह मंच चलाता है। कथन 2 गलत है: e-NAM 2016 में शुरू हुआ। कथन 3 निकट-भ्रम है: चूँकि कृषि बाज़ार राज्य विषय है, मंडियाँ राज्यों के APMC क़ानूनों के अधीन रहती हैं, और e-NAM उनका स्थान नहीं लेता, बल्कि मौजूदा APMC बाज़ारों, अब 1,400 से अधिक, को एक साझा ऑनलाइन मंच पर जोड़ता है ताकि अन्य जगहों के ख़रीदार बोली लगा सकें; मंडियों और राज्यों के पार व्यापार धीरे ही बढ़ा है।",
  MOA, "ag-apmc-enam", craft="precision")

S(AG, "medium", "Consider the following statements about farm credit:",
  "कृषि ऋण के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Kisan Credit Card scheme was introduced in 2008.",
   "Farmers who repay their crop loans late also pay the effective interest rate of 4 per cent.",
   "The interest subvention on crop loans applies to loans of any size."],
  ["किसान क्रेडिट कार्ड योजना 2008 में शुरू की गई।",
   "जो किसान अपने फ़सल ऋण देर से चुकाते हैं, वे भी 4 प्रतिशत की प्रभावी ब्याज दर देते हैं।",
   "फ़सल ऋणों पर ब्याज छूट किसी भी आकार के ऋण पर लागू होती है।"],
  C3, 3,
  "None is correct; each misses an exact condition. Statement 1 is wrong: the KCC scheme dates from 1998. Statement 2 is wrong: banks lend at 7 per cent with a subvention from the Centre, and only farmers who repay promptly get a further 3 per cent incentive that brings the cost down to 4 per cent. "
  "Statement 3 is wrong: the subvention covers short-term loans only up to a limit -- ₹3 lakh, which the Budget 2025-26 announced would be raised to ₹5 lakh for loans through the KCC.",
  "कोई भी कथन सही नहीं है; हर कथन एक सटीक शर्त चूकता है। कथन 1 गलत है: KCC योजना 1998 से है। कथन 2 गलत है: बैंक केंद्र की छूट के साथ 7 प्रतिशत पर ऋण देते हैं, और केवल समय पर चुकाने वाले किसानों को 3 प्रतिशत का अतिरिक्त प्रोत्साहन मिलता है जो लागत 4 प्रतिशत तक लाता है। "
  "कथन 3 गलत है: छूट केवल एक सीमा तक के अल्पकालिक ऋणों पर है, यानी ₹3 लाख, जिसे बजट 2025-26 ने KCC के माध्यम से ऋणों के लिए ₹5 लाख करने की घोषणा की।",
  MOA, "ag-kcc-interest-subvention", craft="precision")

S(AG, "medium", "Consider the following statements about PM-KISAN:",
  "PM-KISAN के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It gives eligible farmer families ₹6,000 a year in three instalments.",
   "It was launched in 2016.",
   "Since the benefit goes to landholding families, tenant farmers who cultivate land they do not own are generally left out."],
  ["यह पात्र किसान परिवारों को तीन किस्तों में ₹6,000 प्रति वर्ष देती है।",
   "यह 2016 में शुरू की गई।",
   "चूँकि लाभ भूमिधारी परिवारों को मिलता है, इसलिए दूसरों की भूमि जोतने वाले काश्तकार किसान सामान्यतः बाहर रह जाते हैं।"],
  C3, 1,
  "Statements 1 and 3 are correct. The money goes directly into the bank accounts of landholding farmer families, identified by the States, so tenants and sharecroppers -- who bear the costs of cultivation but do not own the land -- usually miss out. "
  "Statement 2 is wrong: the scheme was announced in the interim Budget of February 2019, with effect from December 2018.",
  "कथन 1 और 3 सही हैं। पैसा सीधे भूमिधारी किसान परिवारों के बैंक खातों में जाता है, जिनकी पहचान राज्य करते हैं, इसलिए काश्तकार और बटाईदार, जो खेती की लागत उठाते हैं पर भूमि के स्वामी नहीं होते, प्रायः छूट जाते हैं। "
  "कथन 2 गलत है: योजना की घोषणा फ़रवरी 2019 के अंतरिम बजट में, दिसंबर 2018 से प्रभावी रूप में, की गई।",
  MOA, "ag-pm-kisan", craft="inference")

S(IG, "medium", "Consider the following statements about the Pradhan Mantri Jan Dhan Yojana:",
  "प्रधानमंत्री जन धन योजना के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Jan Dhan accounts are basic savings accounts that need no minimum balance.",
   "More than 55 crore accounts have been opened under it.",
   "Because most poor households now have a bank account, cash support can be sent directly to them, cutting out middlemen and leakage."],
  ["जन धन खाते बुनियादी बचत खाते हैं जिनमें न्यूनतम शेष की आवश्यकता नहीं होती।",
   "इसके तहत 55 करोड़ से अधिक खाते खोले गए हैं।",
   "चूँकि अधिकांश ग़रीब परिवारों के पास अब बैंक खाता है, इसलिए नक़द सहायता सीधे उन्हें भेजी जा सकती है, जिससे बिचौलिए और रिसाव कम होते हैं।"],
  C3, 2,
  "All three are correct. Launched in 2014, the scheme brought most unbanked households into the banking system with zero-balance accounts, RuPay debit cards and accident cover; more than half the accounts are held by women. "
  "Linked with Aadhaar and mobile numbers -- the 'JAM trinity' -- the accounts became the channel for direct benefit transfers such as PM-KISAN payments and pandemic cash support, so money reaches the beneficiary without passing through intermediaries who could take a cut.",
  "तीनों कथन सही हैं। 2014 में शुरू हुई योजना ने शून्य-शेष खातों, RuPay डेबिट कार्ड और दुर्घटना सुरक्षा के साथ अधिकांश बैंक-रहित परिवारों को बैंकिंग प्रणाली में लाया; आधे से अधिक खाते महिलाओं के हैं। "
  "आधार और मोबाइल नंबरों से जुड़कर, यानी 'JAM त्रयी', ये खाते PM-KISAN भुगतानों और महामारी की नक़द सहायता जैसे प्रत्यक्ष लाभ अंतरण का माध्यम बने, जिससे पैसा उन बिचौलियों से गुज़रे बिना लाभार्थी तक पहुँचता है जो हिस्सा काट सकते थे।",
  "Department of Financial Services -- PMJDY.", "ig-jan-dhan", craft="linkage")

S(IG, "medium", "Consider the following statements about housing schemes:",
  "आवास योजनाओं के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["PMAY-Urban 2.0, approved in 2024, aims to build one crore houses for the urban poor and middle class.",
   "PMAY-Gramin was extended in 2024 to build two crore more rural houses by 2029.",
   "Houses under PMAY are to be registered in the name of a woman of the household, alone or jointly, so that women own an asset in their own right."],
  ["2024 में स्वीकृत PMAY-शहरी 2.0 का लक्ष्य शहरी ग़रीबों और मध्यम वर्ग के लिए एक करोड़ मकान बनाना है।",
   "PMAY-ग्रामीण को 2024 में 2029 तक दो करोड़ और ग्रामीण मकान बनाने के लिए बढ़ाया गया।",
   "PMAY के तहत मकान परिवार की किसी महिला के नाम, अकेले या संयुक्त रूप से, पंजीकृत किए जाने हैं, ताकि महिलाओं के पास अपनी एक संपत्ति हो।"],
  C3, 2,
  "All three are correct. The condition on women's ownership, where the household has a woman member, is meant to give women a valuable asset and a stronger voice in the household, and some security in case of desertion or widowhood. "
  "Together, the two phases aim to close the remaining housing gap by the end of the decade.",
  "तीनों कथन सही हैं। महिलाओं के स्वामित्व की शर्त, जहाँ परिवार में कोई महिला सदस्य हो, महिलाओं को एक मूल्यवान संपत्ति और परिवार में अधिक मज़बूत आवाज़ देने के लिए है, और परित्याग या वैधव्य की स्थिति में कुछ सुरक्षा भी। "
  "दोनों चरण मिलकर दशक के अंत तक शेष आवास कमी दूर करने का लक्ष्य रखते हैं।",
  "Ministry of Housing and Urban Affairs; Ministry of Rural Development.", "ig-pmay", craft="linkage")

if __name__ == "__main__":
    write_updates("upg_l2_t18_econ_a.sql", statuses=("draft", "published"))
