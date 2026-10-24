# -*- coding: utf-8 -*-
"""Level 3 · Test 6 (GS Integrated Test 6) -- part E: Economy (17) (upsc_l3_cell_targets.mjs 6).
Same cell plan as Tests 1-5.
Every fact was searched in the whole UPSC bank (l3_tools/bank_find.py) and is one no row tests: the Mission for
Cotton Productivity; the NSS Situation Assessment Survey of agricultural households; the 2025-26 customs-duty
rationalisation; gold imports and the current account; India's largest trading partners; electricity futures;
rupee non-deliverable forwards; clearing corporations and CCIL; the RBI's Financial Stability Report and the FSDC;
the Global Hunger Index, World Happiness Report, World Inequality Report and Global Peace Index; India as the
third-largest vehicle market; section 43B(h) and payments to MSEs; BSNL's indigenous 4G; real and nominal wages;
the RBI's buy/sell swaps; the Lakshmi Vilas Bank amalgamation; updated income-tax returns. MCQ keys are pinned."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Economy"
d.REQUIRE_CRAFT = True
FM = "Financial Markets, Instruments & Fintech"
MB = "Money, Banking & Monetary Policy"
IN = "Industry, Infrastructure, Energy & Services"
EX = "External Sector & International Institutions"
AG = "Agriculture & Food Economy"
RBI = "Reserve Bank of India"

# ---------------------------------------------------------------- Agriculture & Food Economy (m-MCQ, m-stmt)
M(AG, "medium",
  "The Mission for Cotton Productivity, announced in the Union Budget for 2025-26, lays special stress on:",
  "2025-26 के केंद्रीय बजट में घोषित कपास उत्पादकता मिशन किस पर विशेष बल देता है?",
  ["shifting cotton fields in water-scarce districts over to millets and pulses",
   "replacing Bt cotton entirely with organically grown cotton within five years",
   "allowing duty-free imports of all long-staple cotton for the textile industry",
   "raising yields and promoting extra-long staple cotton varieties"],
  ["जल-संकट वाले ज़िलों में कपास के खेतों को मोटे अनाजों और दालों की ओर मोड़ना",
   "पाँच वर्षों में बीटी कपास को पूरी तरह जैविक रूप से उगाए कपास से बदलना",
   "वस्त्र उद्योग के लिए सभी लंबे रेशे वाले कपास के शुल्क-मुक्त आयात की अनुमति देना",
   "उपज बढ़ाना और अतिरिक्त-लंबे रेशे वाली कपास किस्मों को बढ़ावा देना"],
  3,
  "India has the world's largest area under cotton but one of the lowest yields, and output has stagnated as pink bollworm developed resistance to Bt cotton and rain-fed farms struggled with erratic weather. The five-year mission, backed by research through ICAR, aims at higher productivity and sustainability and especially at extra-long staple (ELS) varieties, which fine textiles need and which India now largely imports. "
  "It is meant to support the textile sector's 'farm to fibre to factory to fashion to foreign' value chain. The approaches discussed include better seed, high-density planting systems, and integrated pest management; none of the other options is part of the mission.",
  "भारत में कपास का क्षेत्रफल विश्व में सबसे अधिक है पर उपज सबसे कम में से एक है, और उत्पादन ठहर गया है क्योंकि गुलाबी सुंडी ने बीटी कपास के प्रति प्रतिरोध विकसित किया और वर्षा-आधारित खेत अनिश्चित मौसम से जूझते रहे। आईसीएआर के अनुसंधान से समर्थित पाँच वर्षीय मिशन का लक्ष्य अधिक उत्पादकता और स्थिरता है, और विशेष रूप से अतिरिक्त-लंबे रेशे (ईएलएस) वाली किस्में, जो महीन वस्त्रों के लिए आवश्यक हैं और जिन्हें भारत अभी अधिकतर आयात करता है। "
  "इसका उद्देश्य वस्त्र क्षेत्र की ‘खेत से रेशा, कारख़ाना, फ़ैशन और विदेश’ मूल्य-शृंखला को सहारा देना है। चर्चित तरीक़ों में बेहतर बीज, सघन रोपण प्रणालियाँ और एकीकृत कीट प्रबंधन शामिल हैं; अन्य कोई विकल्प मिशन का भाग नहीं है।",
  "Union Budget 2025-26, Budget Speech; Ministry of Agriculture and Farmers Welfare; Ministry of Textiles.",
  "l3-t6-eco-cotton-productivity-mission", pos=2, craft="recall")

S(AG, "medium", "With reference to the Situation Assessment Survey of agricultural households conducted by the National Statistical Office for 2018-19, consider the following statements:",
  "राष्ट्रीय सांख्यिकी कार्यालय द्वारा 2018-19 के लिए किए गए कृषि परिवारों के स्थिति आकलन सर्वेक्षण के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Wages formed a larger share of the average agricultural household's income than net receipts from crop cultivation.",
   "Most of the outstanding loans of indebted agricultural households had been taken from moneylenders.",
   "The survey counts a household as agricultural only if it owns at least one hectare of land."],
  ["औसत कृषि परिवार की आय में मज़दूरी का हिस्सा फ़सल खेती से शुद्ध प्राप्तियों से अधिक था।",
   "ऋणग्रस्त कृषि परिवारों के अधिकांश बकाया ऋण साहूकारों से लिए गए थे।",
   "सर्वेक्षण किसी परिवार को तभी कृषि परिवार मानता है जब उसके पास कम से कम एक हेक्टेयर भूमि हो।"],
  C3, 0,
  "Only statement 1 is correct. The survey put the average monthly income of an agricultural household at a little over Rs 10,000, of which wages were the largest component, ahead of crop cultivation and then livestock -- evidence that most farm families depend on several sources of income because their holdings are small. "
  "Statement 2 is wrong: just over half of the households were indebted, the average outstanding loan being around Rs 74,000, but about seven-tenths of the outstanding amount was owed to institutional sources such as banks and cooperatives; moneylenders accounted for about a fifth -- still a sizeable informal share. Statement 3 is wrong: an agricultural household is defined by its activity -- one that received more than a threshold value of produce from agriculture during the year and had at least one member self-employed in farming -- not by land ownership, so tenants and households with very small plots are included. The findings are a caution against treating crop prices alone as the answer to farm distress.",
  "केवल कथन 1 सही है। सर्वेक्षण ने कृषि परिवार की औसत मासिक आय 10,000 रुपये से कुछ अधिक आँकी, जिसमें मज़दूरी सबसे बड़ा घटक थी, फ़सल खेती से आगे और उसके बाद पशुपालन -- यह प्रमाण कि अधिकांश किसान परिवार अनेक आय-स्रोतों पर निर्भर हैं क्योंकि उनकी जोतें छोटी हैं। "
  "कथन 2 ग़लत है: आधे से थोड़े अधिक परिवार ऋणग्रस्त थे, औसत बकाया ऋण लगभग 74,000 रुपये था, पर बकाया राशि का लगभग सात-दसवाँ भाग बैंकों और सहकारी समितियों जैसे संस्थागत स्रोतों का था; साहूकारों का हिस्सा लगभग पाँचवाँ था -- फिर भी उल्लेखनीय अनौपचारिक भाग। कथन 3 ग़लत है: कृषि परिवार उसकी गतिविधि से परिभाषित है -- वह परिवार जिसे वर्ष में कृषि से एक सीमा-मूल्य से अधिक उपज मिली हो और जिसका कम से कम एक सदस्य खेती में स्वनियोजित हो -- भूमि-स्वामित्व से नहीं, इसलिए काश्तकार और बहुत छोटे भूखंड वाले परिवार भी शामिल हैं। ये निष्कर्ष कृषि संकट का उत्तर केवल फ़सल-मूल्यों को मानने के विरुद्ध चेतावनी हैं।",
  "Ministry of Statistics and Programme Implementation, NSS 77th Round, Situation Assessment of Agricultural Households (2021).",
  "l3-t6-eco-situation-assessment-survey-2019", craft="inference")

# ---------------------------------------------------------------- Budget, Deficits & Public Debt (m-stmt)
S("Budget, Deficits & Public Debt", "medium", "With reference to the changes in customs duties announced in the Union Budget for 2025-26, consider the following statements:",
  "2025-26 के केंद्रीय बजट में घोषित सीमा शुल्क परिवर्तनों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["The number of rates of basic customs duty on industrial goods was reduced by removing seven of them.",
   "It was proposed that not more than one cess or surcharge would be applied on any tariff item."],
  ["औद्योगिक वस्तुओं पर मूल सीमा शुल्क की दरों में से सात हटाकर उनकी संख्या घटाई गई।",
   "प्रस्ताव किया गया कि किसी भी टैरिफ़ मद पर एक से अधिक उपकर या अधिभार नहीं लगाया जाएगा।"],
  T2, 2,
  "Both statements are correct. Customs tariffs had accumulated many rates, cesses and surcharges, which made the duty on a product hard to predict and created inversions where inputs bore more duty than finished goods. The 2025-26 Budget removed seven tariff rates, leaving eight including zero, and adjusted the duties and the Agriculture Infrastructure and Development Cess so that the overall incidence on most items stayed broadly the same, while committing to a single cess or surcharge on any item. "
  "Customs duties and the cesses on imports matter for the Budget in two ways: they are a sizeable source of revenue, and the cesses, unlike basic duty, are not shared with the States, which is one reason the States watch the growing share of cesses in the Centre's gross tax revenue.",
  "दोनों कथन सही हैं। सीमा शुल्क टैरिफ़ में अनेक दरें, उपकर और अधिभार जमा हो गए थे, जिससे किसी उत्पाद पर शुल्क का अनुमान कठिन था और ऐसे उलटाव बनते थे जहाँ निविष्टियों पर तैयार वस्तुओं से अधिक शुल्क था। 2025-26 के बजट ने सात टैरिफ़ दरें हटाईं, शून्य सहित आठ बचीं, और शुल्कों तथा कृषि अवसंरचना और विकास उपकर को इस तरह समायोजित किया कि अधिकांश वस्तुओं पर कुल भार मोटे तौर पर वही रहे, साथ ही किसी भी मद पर एक ही उपकर या अधिभार की प्रतिबद्धता की। "
  "सीमा शुल्क और आयात पर उपकर बजट के लिए दो तरह से महत्वपूर्ण हैं: वे राजस्व का उल्लेखनीय स्रोत हैं, और उपकर, मूल शुल्क के विपरीत, राज्यों के साथ साझा नहीं होते, यही एक कारण है कि राज्य केंद्र के सकल कर राजस्व में उपकरों के बढ़ते हिस्से पर नज़र रखते हैं।",
  "Union Budget 2025-26, Budget Speech, Part B; Central Board of Indirect Taxes and Customs.",
  "l3-t6-eco-customs-rationalisation-2025", craft="precision")

# ---------------------------------------------------------------- External Sector & International Institutions (e-SI, m-stmt)
A(EX, "easy",
  "A sharp rise in gold imports tends to widen India's current account deficit.",
  "सोने के आयात में तीव्र वृद्धि भारत के चालू खाते के घाटे को बढ़ाने की प्रवृत्ति रखती है।",
  "Gold imports are recorded as merchandise imports in the trade balance, which is a part of the current account.",
  "सोने का आयात व्यापार संतुलन में वस्तु आयात के रूप में दर्ज होता है, जो चालू खाते का भाग है।",
  0,
  "Both statements are correct and Statement II explains Statement I. India produces very little gold but is among the world's largest consumers, for jewellery and as a store of value, so gold is one of its biggest import items after crude oil and electronics; a spike in purchases -- often when prices are expected to rise or during the wedding season -- shows up directly as a wider merchandise trade deficit and so a wider current account deficit. "
  "This is why governments have tried to divert demand to financial forms of gold, through gold monetisation and gold-linked instruments, and have used import duties to restrain imports in years of pressure on the rupee. Gold bought by the RBI for its reserves is different: it is a reserve asset, not a current-account import.",
  "दोनों कथन सही हैं और कथन II, कथन I की व्याख्या करता है। भारत बहुत कम सोना उत्पादित करता है पर आभूषणों और मूल्य-संचय के लिए विश्व के सबसे बड़े उपभोक्ताओं में है, इसलिए कच्चे तेल और इलेक्ट्रॉनिक्स के बाद सोना उसके सबसे बड़े आयातों में है; ख़रीद में उछाल -- प्रायः जब क़ीमतों के बढ़ने की अपेक्षा हो या विवाहों के मौसम में -- सीधे बड़े वस्तु व्यापार घाटे और इसलिए बड़े चालू खाते के घाटे के रूप में दिखता है। "
  "इसीलिए सरकारों ने स्वर्ण मुद्रीकरण और सोने से जुड़े साधनों के माध्यम से माँग को सोने के वित्तीय रूपों की ओर मोड़ने का प्रयास किया है, और रुपये पर दबाव के वर्षों में आयात रोकने के लिए आयात शुल्क का उपयोग किया है। आरबीआई द्वारा अपने भंडार के लिए ख़रीदा गया सोना भिन्न है: वह आरक्षित परिसंपत्ति है, चालू खाते का आयात नहीं।",
  RBI + ", Balance of Payments statistics; NCERT Class XII, Introductory Macroeconomics ('Open Economy Macroeconomics').",
  "l3-t6-eco-gold-imports-current-account", craft="linkage")

S(EX, "medium", "With reference to India's merchandise trade in 2024-25, consider the following statements:",
  "2024-25 में भारत के वस्तु व्यापार के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["China was India's largest trading partner.",
   "India ran a trade deficit with the United States.",
   "India's trade deficit with China narrowed sharply compared with 2023-24."],
  ["चीन भारत का सबसे बड़ा व्यापारिक साझेदार था।",
   "संयुक्त राज्य अमेरिका के साथ भारत का व्यापार घाटा था।",
   "चीन के साथ भारत का व्यापार घाटा 2023-24 की तुलना में तेज़ी से घटा।"],
  C3, 3,
  "None of the statements is correct. Statement 1 is wrong: the United States was India's largest trading partner in 2024-25, with China a close second -- China had narrowly held the top place in 2023-24, which is why the ranking needs care. Statement 2 is wrong: India ran a sizeable surplus with the United States, exporting medicines, electronics such as smartphones, gems and jewellery, textiles and engineering goods. "
  "Statement 3 is wrong: the deficit with China widened, from about 85 billion dollars in 2023-24 to nearly a hundred billion, as imports of electronic components, machinery, chemicals, solar equipment and active pharmaceutical ingredients kept rising while exports to China fell. The gap reflects how deeply Indian assembly and manufacturing still depend on Chinese inputs -- the very dependence that the production-linked incentive schemes and the push for component making are meant to reduce.",
  "कोई भी कथन सही नहीं है। कथन 1 ग़लत है: 2024-25 में संयुक्त राज्य अमेरिका भारत का सबसे बड़ा व्यापारिक साझेदार था, चीन निकट दूसरे स्थान पर -- 2023-24 में चीन थोड़े अंतर से शीर्ष पर था, इसलिए इस क्रम में सावधानी आवश्यक है। कथन 2 ग़लत है: संयुक्त राज्य अमेरिका के साथ भारत का अच्छा-ख़ासा अधिशेष था, जो दवाएँ, स्मार्टफ़ोन जैसे इलेक्ट्रॉनिक्स, रत्न और आभूषण, वस्त्र और इंजीनियरिंग वस्तुएँ निर्यात करता है। "
  "कथन 3 ग़लत है: चीन के साथ घाटा बढ़ा, 2023-24 के लगभग 85 अरब डॉलर से लगभग सौ अरब डॉलर तक, क्योंकि इलेक्ट्रॉनिक पुर्ज़ों, मशीनरी, रसायनों, सौर उपकरणों और सक्रिय दवा घटकों का आयात बढ़ता रहा जबकि चीन को निर्यात घटा। यह अंतर दिखाता है कि भारतीय असेंबली और विनिर्माण अब भी चीनी निविष्टियों पर कितना निर्भर हैं -- ठीक वही निर्भरता जिसे उत्पादन-आधारित प्रोत्साहन योजनाएँ और पुर्ज़ा-निर्माण का प्रयास घटाने के लिए हैं।",
  "Ministry of Commerce and Industry, Department of Commerce, Export Import Data Bank (2024-25).",
  "l3-t6-eco-trade-partners-us-china-russia", craft="inference")

# ---------------------------------------------------------------- Financial Markets, Instruments & Fintech (e-stmt, h-stmt, m-stmt x2)
S(FM, "easy", "With reference to electricity futures in India, consider the following statements:",
  "भारत में बिजली वायदा (फ़्यूचर्स) के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Monthly electricity futures contracts began trading on Indian exchanges in 2025.",
   "These contracts are settled in cash, without any physical delivery of electricity."],
  ["मासिक बिजली वायदा अनुबंधों का भारतीय एक्सचेंजों पर 2025 में कारोबार शुरू हुआ।",
   "ये अनुबंध बिजली की किसी भौतिक आपूर्ति के बिना, नक़द में निपटाए जाते हैं।"],
  T2, 2,
  "Both statements are correct. After the securities and electricity regulators settled their long dispute over jurisdiction, SEBI approved electricity derivatives and the commodity exchanges launched monthly futures in 2025, settled against the prices discovered in the power exchanges' day-ahead market. Generators, distribution companies and large consumers can use them to lock in prices months ahead, which matters more as variable solar and wind power make spot prices swing. "
  "No power changes hands under these contracts: a buyer who has locked in a price still buys the electricity itself in the physical market, and the futures gain or loss offsets any change in its cost. The aim is a deeper electricity market in which hedging lowers risk for investors in generation and storage.",
  "दोनों कथन सही हैं। प्रतिभूति और विद्युत विनियामकों के बीच अधिकार-क्षेत्र पर लंबे विवाद के सुलझने के बाद, सेबी ने बिजली व्युत्पन्नों को स्वीकृति दी और कमोडिटी एक्सचेंजों ने 2025 में मासिक वायदा शुरू किए, जिनका निपटान पावर एक्सचेंजों के डे-अहेड बाज़ार में तय क़ीमतों के आधार पर होता है। उत्पादक, वितरण कंपनियाँ और बड़े उपभोक्ता इनका उपयोग महीनों पहले क़ीमतें तय करने के लिए कर सकते हैं, जो इसलिए अधिक महत्वपूर्ण है कि परिवर्ती सौर और पवन बिजली हाज़िर क़ीमतों को झुलाती है। "
  "इन अनुबंधों में कोई बिजली हाथ नहीं बदलती: जिस ख़रीदार ने क़ीमत तय कर ली है वह बिजली स्वयं भौतिक बाज़ार में ही ख़रीदता है, और वायदा का लाभ या हानि उसकी लागत में किसी भी परिवर्तन की भरपाई करता है। उद्देश्य एक गहरा विद्युत बाज़ार है जिसमें हेजिंग उत्पादन और भंडारण में निवेशकों का जोखिम घटाए।",
  "Securities and Exchange Board of India (2025); Central Electricity Regulatory Commission; Multi Commodity Exchange and National Stock Exchange (contract launches, 2025).",
  "l3-t6-eco-electricity-futures-2025", craft="recall")

S(FM, "hard", "With reference to non-deliverable forwards (NDFs) on the Indian rupee, consider the following statements:",
  "भारतीय रुपये पर नॉन-डिलीवरेबल फ़ॉरवर्ड (एनडीएफ़) के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["In an NDF, the parties settle only the difference between the contracted rate and the actual exchange rate, in a convertible currency such as the dollar.",
   "Since 2020, banks in India have been allowed to deal in rupee NDFs through their units in the International Financial Services Centre.",
   "A large offshore NDF market can put pressure on the onshore exchange rate, especially in periods of stress.",
   "Rupee NDFs are traded mainly on Indian stock exchanges."],
  ["एनडीएफ़ में पक्ष केवल अनुबंधित दर और वास्तविक विनिमय दर के अंतर का निपटान डॉलर जैसी परिवर्तनीय मुद्रा में करते हैं।",
   "2020 से भारत के बैंकों को अंतरराष्ट्रीय वित्तीय सेवा केंद्र में अपनी इकाइयों के माध्यम से रुपये के एनडीएफ़ में सौदे की अनुमति है।",
   "बड़ा अपतटीय एनडीएफ़ बाज़ार, विशेषकर दबाव के समय, घरेलू विनिमय दर पर दबाव डाल सकता है।",
   "रुपये के एनडीएफ़ का कारोबार मुख्यतः भारतीय स्टॉक एक्सचेंजों पर होता है।"],
  C4, 2,
  "Statements 1, 2 and 3 are correct. NDFs let foreign investors and companies hedge or bet on a currency that is not fully convertible without touching it: no rupees change hands, only the dollar difference at maturity. Because the rupee's capital account is not fully open, a sizeable offshore market grew in Singapore, Dubai, London and New York, often trading round the clock, and the RBI has watched how offshore moves spill over into onshore prices. "
  "To bring some of that activity home and improve price discovery, the RBI in 2020 let banks with IFSC Banking Units in GIFT City deal in rupee NDFs with non-residents and with each other. Statement 4 is wrong: NDFs are over-the-counter contracts, mostly between banks and their clients abroad; exchange-traded currency futures are a different onshore product, settled in rupees.",
  "कथन 1, 2 और 3 सही हैं। एनडीएफ़ विदेशी निवेशकों और कंपनियों को ऐसी मुद्रा पर हेज करने या दाँव लगाने देते हैं जो पूरी तरह परिवर्तनीय नहीं है, उसे छुए बिना: कोई रुपया हाथ नहीं बदलता, केवल परिपक्वता पर डॉलर में अंतर चुकाया जाता है। चूँकि रुपये का पूँजी खाता पूरी तरह खुला नहीं है, सिंगापुर, दुबई, लंदन और न्यूयॉर्क में एक बड़ा अपतटीय बाज़ार बना, जो प्रायः चौबीसों घंटे चलता है, और आरबीआई ने देखा है कि अपतटीय उतार-चढ़ाव घरेलू क़ीमतों में कैसे फैलते हैं। "
  "उस गतिविधि का कुछ भाग देश में लाने और मूल्य-निर्धारण सुधारने के लिए आरबीआई ने 2020 में गिफ़्ट सिटी में आईएफ़एससी बैंकिंग इकाइयों वाले बैंकों को अनिवासियों और आपस में रुपये के एनडीएफ़ में सौदे करने दिए। कथन 4 ग़लत है: एनडीएफ़ ओवर-द-काउंटर अनुबंध हैं, अधिकतर विदेश में बैंकों और उनके ग्राहकों के बीच; एक्सचेंज पर कारोबार वाले मुद्रा फ़्यूचर्स एक अलग घरेलू उत्पाद हैं, जिनका निपटान रुपये में होता है।",
  RBI + ", Report of the Task Force on Offshore Rupee Markets (2019) and press release on NDF dealing by IBUs (2020).",
  "l3-t6-eco-rupee-ndf-offshore", craft="inference")

S(FM, "medium", "With reference to clearing corporations in India's financial markets, consider the following statements:",
  "भारत के वित्तीय बाज़ारों में क्लियरिंग कॉर्पोरेशनों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["A clearing corporation becomes the buyer to every seller and the seller to every buyer in the trades it clears.",
   "It collects margins from its members to cover potential losses on their open positions.",
   "It maintains a settlement guarantee fund to meet the obligations of a member that defaults.",
   "The Clearing Corporation of India, which clears trades in government securities and foreign exchange, is regulated by the RBI rather than by SEBI."],
  ["क्लियरिंग कॉर्पोरेशन अपने द्वारा निपटाए जाने वाले सौदों में हर विक्रेता के लिए क्रेता और हर क्रेता के लिए विक्रेता बन जाता है।",
   "यह अपने सदस्यों से उनकी खुली स्थितियों पर संभावित हानियों को ढकने के लिए मार्जिन लेता है।",
   "यह चूक करने वाले सदस्य के दायित्व पूरे करने के लिए एक निपटान गारंटी कोष रखता है।",
   "सरकारी प्रतिभूतियों और विदेशी मुद्रा के सौदे निपटाने वाला क्लियरिंग कॉर्पोरेशन ऑफ़ इंडिया सेबी के बजाय आरबीआई द्वारा विनियमित है।"],
  C4, 3,
  "All four are correct. By stepping between the two sides of every trade -- a process called novation -- a clearing corporation becomes the central counterparty, so that a trader faces the risk of the clearing corporation's failure rather than that of an unknown counterparty. It protects itself by collecting initial and mark-to-market margins, setting position limits and keeping a core settlement guarantee fund built from members' contributions and its own capital. "
  "The clearing corporations attached to the stock and commodity exchanges are regulated by SEBI, while the Clearing Corporation of India, set up by banks in 2001 for the government securities, money and foreign exchange markets, is a payment system authorised by the RBI under the Payment and Settlement Systems Act. Because they concentrate risk, such central counterparties are treated as systemically important market infrastructure.",
  "चारों कथन सही हैं। हर सौदे के दोनों पक्षों के बीच आकर -- जिसे नवीकरण (नोवेशन) कहते हैं -- क्लियरिंग कॉर्पोरेशन केंद्रीय प्रतिपक्ष बन जाता है, ताकि व्यापारी को किसी अज्ञात प्रतिपक्ष के बजाय क्लियरिंग कॉर्पोरेशन के विफल होने का जोखिम ही रहे। वह आरंभिक और बाज़ार-भाव आधारित मार्जिन लेकर, स्थिति-सीमाएँ तय करके और सदस्यों के अंशदान तथा अपनी पूँजी से बना मुख्य निपटान गारंटी कोष रखकर अपनी रक्षा करता है। "
  "स्टॉक और कमोडिटी एक्सचेंजों से जुड़े क्लियरिंग कॉर्पोरेशन सेबी द्वारा विनियमित हैं, जबकि सरकारी प्रतिभूति, मुद्रा और विदेशी मुद्रा बाज़ारों के लिए 2001 में बैंकों द्वारा स्थापित क्लियरिंग कॉर्पोरेशन ऑफ़ इंडिया भुगतान और निपटान प्रणाली अधिनियम के अंतर्गत आरबीआई द्वारा अधिकृत भुगतान प्रणाली है। चूँकि ये जोखिम को केंद्रित करते हैं, ऐसे केंद्रीय प्रतिपक्ष प्रणालीगत रूप से महत्वपूर्ण बाज़ार अवसंरचना माने जाते हैं।",
  "SEBI, Securities Contracts (Regulation) (Stock Exchanges and Clearing Corporations) Regulations, 2018; " + RBI + ", Payment and Settlement Systems Act, 2007.",
  "l3-t6-eco-clearing-corporations-ccil", craft="precision")

S(FM, "medium", "With reference to the Financial Stability Report, consider the following statements:",
  "वित्तीय स्थिरता रिपोर्ट के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is published by the RBI twice a year.",
   "It reflects the collective assessment of a sub-committee of the Financial Stability and Development Council on risks to financial stability.",
   "It includes macro stress tests of the capital of banks under baseline and adverse scenarios.",
   "The Financial Stability and Development Council is chaired by the Union Finance Minister."],
  ["इसे आरबीआई वर्ष में दो बार प्रकाशित करता है।",
   "यह वित्तीय स्थिरता के जोखिमों पर वित्तीय स्थिरता और विकास परिषद की एक उप-समिति के सामूहिक आकलन को दर्शाती है।",
   "इसमें आधार और प्रतिकूल परिदृश्यों में बैंकों की पूँजी के समष्टि दबाव परीक्षण शामिल हैं।",
   "वित्तीय स्थिरता और विकास परिषद की अध्यक्षता केंद्रीय वित्त मंत्री करते हैं।"],
  C4, 3,
  "All four are correct. The report, published every June and December, surveys global and domestic risks, the health of banks, NBFCs, insurers and markets, and the links among them; its stress tests ask how far banks' capital ratios would fall if growth slowed sharply or bad loans rose, and whether any bank would fall below the regulatory minimum. "
  "The FSDC, set up in 2010 after the global financial crisis, brings together the heads of the financial regulators -- the RBI, SEBI, IRDAI and PFRDA -- under the Finance Minister to coordinate on systemic risk, while its sub-committee, chaired by the RBI Governor, does the detailed monitoring. Such reports matter as early warnings, not forecasts: in the mid-2010s they repeatedly flagged rising stressed assets before the bad-loan problem peaked.",
  "चारों कथन सही हैं। हर जून और दिसंबर में प्रकाशित यह रिपोर्ट वैश्विक और घरेलू जोखिमों, बैंकों, एनबीएफ़सी, बीमा कंपनियों और बाज़ारों के स्वास्थ्य, और उनके आपसी संबंधों का सर्वेक्षण करती है; इसके दबाव परीक्षण पूछते हैं कि यदि वृद्धि तेज़ी से धीमी हो या डूबत ऋण बढ़ें तो बैंकों के पूँजी अनुपात कितने गिरेंगे, और क्या कोई बैंक विनियामक न्यूनतम से नीचे जाएगा। "
  "वैश्विक वित्तीय संकट के बाद 2010 में बनी एफ़एसडीसी वित्त मंत्री के अधीन वित्तीय विनियामकों -- आरबीआई, सेबी, इरडाई और पीएफ़आरडीए -- के प्रमुखों को प्रणालीगत जोखिम पर समन्वय के लिए साथ लाती है, जबकि आरबीआई गवर्नर की अध्यक्षता वाली इसकी उप-समिति विस्तृत निगरानी करती है। ऐसी रिपोर्टें पूर्वानुमान नहीं, पूर्व-चेतावनी के रूप में महत्वपूर्ण हैं: 2010 के दशक के मध्य में उन्होंने डूबत ऋण समस्या के चरम पर पहुँचने से पहले बार-बार बढ़ती दबावग्रस्त परिसंपत्तियों की ओर ध्यान दिलाया।",
  RBI + ", Financial Stability Report; Ministry of Finance, Financial Stability and Development Council.",
  "l3-t6-eco-financial-stability-report-fsdc", craft="precision")

# ---------------------------------------------------------------- Inclusive Growth, Welfare & Demography (h-pairs)
P("Inclusive Growth, Welfare & Demography", "hard", "Consider the following pairs of reports and the bodies that publish them:",
  "रिपोर्टों और उन्हें प्रकाशित करने वाली संस्थाओं के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Global Hunger Index : Concern Worldwide and Welthungerhilfe",
   "World Happiness Report : The Wellbeing Research Centre at Oxford, with Gallup and the UN Sustainable Development Solutions Network",
   "World Inequality Report : The World Inequality Lab",
   "Global Peace Index : The Stockholm International Peace Research Institute"],
  ["वैश्विक भूख सूचकांक : कंसर्न वर्ल्डवाइड और वेल्टहुंगरहिल्फ़",
   "विश्व प्रसन्नता रिपोर्ट : ऑक्सफ़ोर्ड का वेलबीइंग रिसर्च सेंटर, गैलप और संयुक्त राष्ट्र सतत विकास समाधान नेटवर्क के साथ",
   "विश्व असमानता रिपोर्ट : वर्ल्ड इनइक्वलिटी लैब",
   "वैश्विक शांति सूचकांक : स्टॉकहोम अंतरराष्ट्रीय शांति अनुसंधान संस्थान"],
  2,
  "The first three pairs are correct. The Global Hunger Index, prepared by two European aid agencies, combines undernourishment, child stunting, child wasting and child mortality, and India has disputed its use of a small survey for undernourishment and of child indicators to describe hunger in the whole population. The World Happiness Report ranks countries mainly on Gallup World Poll answers to the 'life evaluation' question; the World Inequality Report, from the lab associated with Thomas Piketty and Lucas Chancel at the Paris School of Economics, uses tax and survey data to estimate the shares of top incomes and wealth. "
  "The fourth pair is wrong: the Global Peace Index is published by the Institute for Economics and Peace, a think tank based in Sydney, which ranks countries on societal safety and security, ongoing conflict and militarisation. SIPRI, in Stockholm, is known instead for its yearbook and its databases on military expenditure and arms transfers, which are widely cited for India's position as one of the world's largest arms importers. Knowing who prepares an index, and from what data, is the first step in judging what it actually measures.",
  "पहले तीन युग्म सही हैं। दो यूरोपीय सहायता संस्थाओं द्वारा तैयार वैश्विक भूख सूचकांक अल्पपोषण, बच्चों के बौनेपन, दुबलेपन और बाल मृत्यु को जोड़ता है, और भारत ने अल्पपोषण के लिए एक छोटे सर्वेक्षण और पूरी आबादी की भूख बताने के लिए बाल संकेतकों के उपयोग पर आपत्ति की है। विश्व प्रसन्नता रिपोर्ट देशों को मुख्यतः ‘जीवन मूल्यांकन’ प्रश्न पर गैलप वर्ल्ड पोल के उत्तरों के आधार पर क्रम देती है; पेरिस स्कूल ऑफ़ इकोनॉमिक्स में थॉमस पिकेटी और लुकास चांसेल से जुड़ी लैब की विश्व असमानता रिपोर्ट कर और सर्वेक्षण आँकड़ों से शीर्ष आय और संपत्ति के हिस्सों का अनुमान लगाती है। "
  "चौथा युग्म ग़लत है: वैश्विक शांति सूचकांक सिडनी स्थित थिंक टैंक इंस्टीट्यूट फ़ॉर इकोनॉमिक्स एंड पीस प्रकाशित करता है, जो देशों को सामाजिक सुरक्षा, चल रहे संघर्ष और सैन्यीकरण पर क्रम देता है। स्टॉकहोम का सिपरी इसके बजाय अपनी वार्षिकी और सैन्य व्यय तथा शस्त्र हस्तांतरण पर अपने डेटाबेस के लिए जाना जाता है, जिन्हें भारत के विश्व के सबसे बड़े शस्त्र आयातकों में होने के लिए व्यापक रूप से उद्धृत किया जाता है। कौन सूचकांक बनाता है और किन आँकड़ों से, यह जानना यह परखने का पहला क़दम है कि वह वास्तव में क्या मापता है।",
  "Concern Worldwide and Welthungerhilfe, Global Hunger Index; World Happiness Report; World Inequality Lab; Institute for Economics and Peace, Global Peace Index; Stockholm International Peace Research Institute; Ministry of Women and Child Development (statement on the GHI).",
  "l3-t6-eco-reports-ghi-whr-wir-gpi", craft="precision")

# ---------------------------------------------------------------- Industry, Infrastructure, Energy & Services (e-stmt, m-MCQ, m-stmt)
S(IN, "easy", "With reference to India's automobile industry, consider the following statements:",
  "भारत के ऑटोमोबाइल उद्योग के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["India overtook Japan in 2022 to become the world's third-largest market for vehicles by sales.",
   "India is the world's largest producer of passenger cars."],
  ["भारत 2022 में जापान को पीछे छोड़कर बिक्री के हिसाब से विश्व का तीसरा सबसे बड़ा वाहन बाज़ार बना।",
   "भारत विश्व में यात्री कारों का सबसे बड़ा उत्पादक है।"],
  T2, 0,
  "Only statement 1 is correct. Vehicle sales in India passed those of Japan in 2022, leaving India behind only China and the United States, and the industry contributes a large share of manufacturing output and employment, with deep links to steel, rubber, electronics and component makers. India is also one of the world's largest makers of two-wheelers and three-wheelers. "
  "Statement 2 is wrong: China is by far the largest producer of passenger cars -- and of electric vehicles -- and India's car output is a fraction of it. The industry's next challenge is the move to electric and other clean powertrains, which is why schemes support battery cells, electric two- and three-wheelers and charging, and why fuel-efficiency norms are being tightened.",
  "केवल कथन 1 सही है। 2022 में भारत में वाहनों की बिक्री जापान से आगे निकल गई, जिससे भारत केवल चीन और संयुक्त राज्य अमेरिका से पीछे रहा, और यह उद्योग विनिर्माण उत्पादन और रोज़गार में बड़ा हिस्सा देता है, इस्पात, रबर, इलेक्ट्रॉनिक्स और पुर्ज़ा निर्माताओं से गहरे संबंधों के साथ। भारत विश्व में दोपहिया और तिपहिया वाहनों के सबसे बड़े निर्माताओं में भी है। "
  "कथन 2 ग़लत है: यात्री कारों -- और विद्युत वाहनों -- का सबसे बड़ा उत्पादक कहीं आगे चीन है, और भारत का कार उत्पादन उसका एक अंश है। उद्योग की अगली चुनौती विद्युत और अन्य स्वच्छ पावरट्रेन की ओर बदलाव है, इसीलिए योजनाएँ बैटरी सेलों, विद्युत दोपहिया और तिपहिया वाहनों तथा चार्जिंग को सहायता देती हैं, और ईंधन-दक्षता मानदंड कड़े किए जा रहे हैं।",
  "Ministry of Heavy Industries; Society of Indian Automobile Manufacturers; International Organization of Motor Vehicle Manufacturers.",
  "l3-t6-eco-india-third-largest-vehicle-market", craft="recall")

M(IN, "medium",
  "Section 43B(h) of the Income-tax Act, applicable from 2023-24, encourages buyers to pay micro and small enterprises on time by:",
  "2023-24 से लागू आयकर अधिनियम की धारा 43B(h) सूक्ष्म और लघु उद्यमों को समय पर भुगतान के लिए ख़रीदारों को किस प्रकार प्रोत्साहित करती है?",
  ["levying a penalty of two per cent a month on every payment to an MSME that is overdue",
   "making all receivables of MSMEs eligible for an automatic refund of the GST paid on them",
   "giving MSME suppliers a priority claim over secured creditors if the buyer becomes insolvent",
   "allowing a late payment as a deductible expense only in the year it is actually paid"],
  ["एमएसएमई को अतिदेय हर भुगतान पर प्रति माह दो प्रतिशत दंड लगाकर",
   "एमएसएमई की सभी प्राप्य राशियों को उन पर चुकाए जीएसटी की स्वचालित वापसी के योग्य बनाकर",
   "ख़रीदार के दिवालिया होने पर एमएसएमई आपूर्तिकर्ताओं को सुरक्षित लेनदारों से पहले दावा देकर",
   "देर से हुए भुगतान को केवल उसी वर्ष कटौती-योग्य व्यय मानकर जिसमें वह वास्तव में चुकाया जाए"],
  3,
  "Under the MSMED Act, 2006, a buyer must pay a micro or small supplier within the agreed period, which cannot exceed 45 days, failing which compound interest at three times the bank rate is due. Section 43B(h), added by the Finance Act, 2023, adds a tax incentive: if a business pays such a supplier after the permitted period, it cannot claim the amount as an expense for that year, but only in the year it actually pays, which raises its taxable profit in the meantime. "
  "Delayed payments are one of the main causes of working-capital stress for small firms, which also have the MSME Samadhaan portal for complaints and the TReDS platforms to sell their invoices to financiers. The provision covers registered micro and small enterprises, not medium ones, and the other options are not part of the law.",
  "एमएसएमईडी अधिनियम, 2006 के अंतर्गत ख़रीदार को सूक्ष्म या लघु आपूर्तिकर्ता को सहमत अवधि में भुगतान करना होता है, जो 45 दिन से अधिक नहीं हो सकती, वरना बैंक दर के तीन गुने पर चक्रवृद्धि ब्याज देय होता है। वित्त अधिनियम, 2023 द्वारा जोड़ी गई धारा 43B(h) एक कर-प्रोत्साहन जोड़ती है: यदि कोई व्यवसाय ऐसे आपूर्तिकर्ता को अनुमत अवधि के बाद भुगतान करे, तो वह उस राशि को उस वर्ष का व्यय नहीं मान सकता, केवल उस वर्ष जिसमें वह वास्तव में भुगतान करे, जिससे इस बीच उसका कर-योग्य लाभ बढ़ता है। "
  "विलंबित भुगतान छोटी कंपनियों में कार्यशील पूँजी के दबाव का एक मुख्य कारण है, जिनके पास शिकायतों के लिए एमएसएमई समाधान पोर्टल और अपने बिल वित्तदाताओं को बेचने के लिए ट्रेड्स मंच भी हैं। यह उपबंध पंजीकृत सूक्ष्म और लघु उद्यमों पर लागू है, मध्यम पर नहीं, और अन्य विकल्प क़ानून का भाग नहीं हैं।",
  "Income-tax Act, 1961, section 43B(h) (inserted by the Finance Act, 2023); Micro, Small and Medium Enterprises Development Act, 2006, sections 15 and 16.",
  "l3-t6-eco-section-43bh-msme-payments", pos=3, craft="inference")

S(IN, "medium", "With reference to the 4G network rolled out by BSNL in 2025, consider the following statements:",
  "2025 में बीएसएनएल द्वारा शुरू किए गए 4जी नेटवर्क के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["It was built on an indigenously developed technology stack.",
   "Its core network was developed by C-DOT and its radio equipment by Tejas Networks, with TCS as the system integrator.",
   "With it, India became the first country in the world to build its own telecom network equipment."],
  ["इसे स्वदेश में विकसित प्रौद्योगिकी स्टैक पर बनाया गया।",
   "इसका कोर नेटवर्क सी-डॉट ने और रेडियो उपकरण तेजस नेटवर्क्स ने विकसित किए, जिसमें टीसीएस सिस्टम इंटीग्रेटर रही।",
   "इसके साथ भारत अपने दूरसंचार नेटवर्क उपकरण स्वयं बनाने वाला विश्व का पहला देश बना।"],
  C3, 1,
  "Statements 1 and 2 are correct. BSNL's long-delayed 4G service was launched across the country in 2025 on tens of thousands of new towers, using a core developed by the Centre for Development of Telematics, radio access equipment from Tejas Networks and integration by Tata Consultancy Services; the network is designed to be upgradable to 5G through software. "
  "Statement 3 is wrong: the government described India as joining a small group of countries -- Denmark, Sweden, South Korea and China -- that make their own telecom equipment, the big vendors being Ericsson, Nokia, Samsung, Huawei and ZTE. An indigenous stack matters for the security of critical networks and for an export industry, though it came years after private operators had moved to 4G and 5G.",
  "कथन 1 और 2 सही हैं। बीएसएनएल की लंबे समय से विलंबित 4जी सेवा 2025 में देश भर में हज़ारों नए टावरों पर शुरू हुई, जिसमें सेंटर फ़ॉर डेवलपमेंट ऑफ़ टेलीमैटिक्स द्वारा विकसित कोर, तेजस नेटवर्क्स के रेडियो एक्सेस उपकरण और टाटा कंसल्टेंसी सर्विसेज़ का एकीकरण है; नेटवर्क को सॉफ़्टवेयर के माध्यम से 5जी में उन्नत करने योग्य बनाया गया है। "
  "कथन 3 ग़लत है: सरकार ने भारत को उन कुछ देशों -- डेनमार्क, स्वीडन, दक्षिण कोरिया और चीन -- के समूह में शामिल होने वाला बताया जो अपने दूरसंचार उपकरण बनाते हैं, बड़े विक्रेता एरिक्सन, नोकिया, सैमसंग, हुआवेई और ज़ेडटीई हैं। स्वदेशी स्टैक महत्वपूर्ण नेटवर्कों की सुरक्षा और निर्यात उद्योग के लिए मायने रखता है, यद्यपि यह निजी कंपनियों के 4जी और 5जी पर जाने के वर्षों बाद आया।",
  "Department of Telecommunications (PIB, 2025); Centre for Development of Telematics; Bharat Sanchar Nigam Limited.",
  "l3-t6-eco-bsnl-indigenous-4g", craft="precision")

# ---------------------------------------------------------------- Macro Concepts, National Income & Inflation (e-SI)
A("Macro Concepts, National Income & Inflation", "easy",
  "Workers' real wages can fall even in a year in which their money wages rise.",
  "किसी वर्ष श्रमिकों की मौद्रिक मज़दूरी बढ़ने पर भी उनकी वास्तविक मज़दूरी गिर सकती है।",
  "Real wages fall when prices rise faster than money wages.",
  "जब क़ीमतें मौद्रिक मज़दूरी से तेज़ी से बढ़ती हैं, तब वास्तविक मज़दूरी गिरती है।",
  0,
  "Both statements are correct and Statement II explains Statement I. A real wage is the money wage adjusted for the price level -- what the wage can actually buy -- so a 6 per cent pay rise in a year of 8 per cent inflation leaves workers poorer. For rural workers, economists usually deflate wages by the Consumer Price Index for Agricultural or Rural Labourers, whose basket weights food heavily. "
  "This distinction is why rising nominal wages in a period of high food inflation can coexist with falling living standards, and why real-wage trends are watched as a sign of whether growth is reaching workers.",
  "दोनों कथन सही हैं और कथन II, कथन I की व्याख्या करता है। वास्तविक मज़दूरी मूल्य-स्तर के अनुसार समायोजित मौद्रिक मज़दूरी है -- मज़दूरी वास्तव में क्या ख़रीद सकती है -- इसलिए 8 प्रतिशत मुद्रास्फीति वाले वर्ष में 6 प्रतिशत वेतन-वृद्धि श्रमिकों को अधिक ग़रीब छोड़ती है। ग्रामीण श्रमिकों के लिए अर्थशास्त्री सामान्यतः मज़दूरी को कृषि या ग्रामीण श्रमिकों के उपभोक्ता मूल्य सूचकांक से समायोजित करते हैं, जिसकी टोकरी में भोजन का भार अधिक है। "
  "इसी अंतर के कारण ऊँची खाद्य मुद्रास्फीति के दौर में बढ़ती नाममात्र मज़दूरी गिरते जीवन-स्तर के साथ चल सकती है, और वास्तविक मज़दूरी के रुझानों पर इस संकेत के रूप में नज़र रखी जाती है कि वृद्धि श्रमिकों तक पहुँच रही है या नहीं।",
  "NCERT Class XII, Introductory Macroeconomics; Labour Bureau, Consumer Price Index for Agricultural and Rural Labourers.",
  "l3-t6-eco-real-vs-money-wages", craft="application")

# ---------------------------------------------------------------- Money, Banking & Monetary Policy (m-MCQ, m-stmt)
M(MB, "medium",
  "When the RBI conducts a dollar-rupee 'buy/sell' swap with banks, it:",
  "जब आरबीआई बैंकों के साथ डॉलर-रुपया ‘ख़रीद/बिक्री’ स्वैप करता है, तब वह:",
  ["buys dollars and injects rupees now, agreeing to sell the dollars back later",
   "sells dollars now to absorb surplus rupees, agreeing to buy the dollars back later",
   "lends dollars to the Government of India to repay its external debt early",
   "converts part of its foreign exchange reserves into gold held in India"],
  ["अभी डॉलर ख़रीदकर रुपये डालता है, और बाद में डॉलर वापस बेचने का अनुबंध करता है",
   "अभी डॉलर बेचकर अतिरिक्त रुपये सोखता है, और बाद में डॉलर वापस ख़रीदने का अनुबंध करता है",
   "भारत सरकार को उसका विदेशी ऋण जल्दी चुकाने के लिए डॉलर उधार देता है",
   "अपने विदेशी मुद्रा भंडार के एक भाग को भारत में रखे सोने में बदलता है"],
  0,
  "In a buy/sell swap the RBI buys dollars from banks today, paying in rupees, and simultaneously contracts to sell the same dollars back at a set date and rate. The rupees released add to banking-system liquidity for the life of the swap -- six months or three years in the large swaps of early 2025 -- while the RBI's reserves are only temporarily enlarged. "
  "It was used in 2025 because heavy dollar sales to defend the rupee had drained rupee liquidity, pushing short-term rates above the policy rate. A sell/buy swap does the opposite and absorbs liquidity. Such swaps complement open market purchases of government bonds as a way of supplying durable liquidity.",
  "ख़रीद/बिक्री स्वैप में आरबीआई आज बैंकों से रुपये देकर डॉलर ख़रीदता है और साथ ही उन्हीं डॉलरों को एक निश्चित तिथि और दर पर वापस बेचने का अनुबंध करता है। जारी रुपये स्वैप की अवधि भर बैंकिंग प्रणाली की तरलता बढ़ाते हैं -- 2025 के आरंभ के बड़े स्वैपों में छह महीने या तीन वर्ष -- जबकि आरबीआई का भंडार केवल अस्थायी रूप से बढ़ता है। "
  "इसका उपयोग 2025 में इसलिए हुआ कि रुपये की रक्षा के लिए भारी डॉलर बिक्री ने रुपये की तरलता सोख ली थी, जिससे अल्पकालिक दरें नीतिगत दर से ऊपर चली गईं। बिक्री/ख़रीद स्वैप इसका उल्टा करता है और तरलता सोखता है। ऐसे स्वैप टिकाऊ तरलता देने के साधन के रूप में सरकारी बॉन्डों की खुले बाज़ार में ख़रीद के पूरक हैं।",
  RBI + ", press releases on USD/INR buy/sell swap auctions (2025); Monetary Policy Report.",
  "l3-t6-eco-rbi-buy-sell-swap", pos=0, craft="inference")

S(MB, "medium", "With reference to the resolution of the Lakshmi Vilas Bank in 2020, consider the following statements:",
  "2020 में लक्ष्मी विलास बैंक के समाधान के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["The bank was amalgamated with DBS Bank India, the Indian subsidiary of a Singapore bank.",
   "The resolution was carried out under the Insolvency and Bankruptcy Code.",
   "Depositors of the bank lost the part of their deposits that exceeded the insured limit of Rs 5 lakh."],
  ["बैंक का विलय सिंगापुर के एक बैंक की भारतीय सहायक कंपनी डीबीएस बैंक इंडिया में किया गया।",
   "समाधान दिवाला और शोधन अक्षमता संहिता के अंतर्गत किया गया।",
   "बैंक के जमाकर्ताओं ने अपनी जमा का वह भाग खो दिया जो 5 लाख रुपये की बीमित सीमा से अधिक था।"],
  C3, 0,
  "Only statement 1 is correct. After years of losses and failed merger talks, the RBI placed the Chennai-based private bank under a moratorium in November 2020 and, within days, the Union government approved a scheme to merge it with DBS Bank India -- the first time a foreign bank's Indian arm was used to rescue an Indian bank. "
  "Statement 2 is wrong: banks are outside the Insolvency and Bankruptcy Code; the scheme was framed under section 45 of the Banking Regulation Act, under which the RBI and the government handle a failing bank through a moratorium, reconstruction or amalgamation. Statement 3 is wrong: all deposits were transferred in full to DBS Bank India, so depositors lost nothing; the losses fell on shareholders, whose capital was written off, and on holders of the bank's Tier 2 bonds. Deposit insurance is the backstop when no such rescue is found.",
  "केवल कथन 1 सही है। वर्षों के घाटे और विफल विलय-वार्ताओं के बाद आरबीआई ने नवंबर 2020 में चेन्नई स्थित इस निजी बैंक पर अधिस्थगन लगाया और कुछ ही दिनों में केंद्र सरकार ने इसे डीबीएस बैंक इंडिया में मिलाने की योजना स्वीकृत की -- पहली बार किसी विदेशी बैंक की भारतीय शाखा का उपयोग किसी भारतीय बैंक को बचाने में हुआ। "
  "कथन 2 ग़लत है: बैंक दिवाला और शोधन अक्षमता संहिता के बाहर हैं; योजना बैंककारी विनियमन अधिनियम की धारा 45 के अंतर्गत बनी, जिसके तहत आरबीआई और सरकार विफल होते बैंक को अधिस्थगन, पुनर्निर्माण या विलय के माध्यम से सँभालते हैं। कथन 3 ग़लत है: सभी जमाएँ पूरी तरह डीबीएस बैंक इंडिया को हस्तांतरित हुईं, इसलिए जमाकर्ताओं ने कुछ नहीं खोया; हानि शेयरधारकों पर पड़ी, जिनकी पूँजी बट्टे खाते में गई, और बैंक के टियर 2 बॉन्डधारकों पर। जब ऐसा कोई बचाव न मिले, तब जमा बीमा अंतिम सहारा है।",
  RBI + ", press releases on Lakshmi Vilas Bank (November 2020); Banking Regulation Act, 1949, section 45.",
  "l3-t6-eco-lakshmi-vilas-dbs-amalgamation", craft="linkage")

# ---------------------------------------------------------------- Taxation & Fiscal Federalism (h-SI)
A("Taxation & Fiscal Federalism", "hard",
  "A taxpayer can now file an updated income-tax return up to four years after the end of the relevant assessment year.",
  "कोई करदाता अब संबंधित निर्धारण वर्ष की समाप्ति के चार वर्ष बाद तक अद्यतन आयकर रिटर्न दाखिल कर सकता है।",
  "An updated return cannot be used to claim a larger refund or to reduce tax liability; it is meant for declaring missed income on payment of additional tax.",
  "अद्यतन रिटर्न का उपयोग अधिक धनवापसी माँगने या कर-दायित्व घटाने के लिए नहीं हो सकता; यह अतिरिक्त कर चुकाकर छूटी आय घोषित करने के लिए है।",
  1,
  "Both statements are correct, but Statement II does not explain Statement I. The updated return, introduced in 2022 with a two-year window, was extended by the Budget for 2025-26 to forty-eight months; the later the return, the larger the additional tax -- rising from a quarter of the tax and interest due in the first year to as much as seventy per cent in the fourth -- so that early correction is cheaper than waiting to be caught. "
  "Statement II describes the purpose and the limits of the scheme: it is a voluntary-compliance route to bring undisclosed income into the net without the cost of litigation, and it cannot be filed to show a loss or claim a refund, or once a search or assessment has begun. The time limit in Statement I follows from the policy choice to widen that window, not from these restrictions.",
  "दोनों कथन सही हैं, पर कथन II, कथन I की व्याख्या नहीं करता। 2022 में दो वर्ष की अवधि के साथ लाया गया अद्यतन रिटर्न 2025-26 के बजट से अड़तालीस महीने तक बढ़ाया गया; रिटर्न जितना देर से हो, अतिरिक्त कर उतना अधिक -- पहले वर्ष में देय कर और ब्याज के एक-चौथाई से चौथे वर्ष में सत्तर प्रतिशत तक -- ताकि पकड़े जाने की प्रतीक्षा से जल्दी सुधार सस्ता रहे। "
  "कथन II योजना के उद्देश्य और सीमाओं का वर्णन करता है: यह मुक़दमे की लागत के बिना अघोषित आय को कर-जाल में लाने का स्वैच्छिक अनुपालन मार्ग है, और इसे हानि दिखाने या धनवापसी माँगने के लिए, या तलाशी या निर्धारण शुरू होने के बाद दाखिल नहीं किया जा सकता। कथन I की समय-सीमा उस अवधि को बढ़ाने के नीतिगत निर्णय से आती है, इन प्रतिबंधों से नहीं।",
  "Income-tax Act, 1961, section 139(8A) and section 140B; Union Budget 2025-26, Budget Speech; Central Board of Direct Taxes.",
  "l3-t6-eco-updated-return-48-months", craft="inference")

write("gs_l3_t6_e.sql")
