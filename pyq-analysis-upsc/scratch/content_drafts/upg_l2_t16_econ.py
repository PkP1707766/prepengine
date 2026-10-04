# -*- coding: utf-8 -*-
"""Level 2 · Test 16 (Economy 2: External Sector, International Institutions, Growth and Planning) -- depth audit of
2026-10-04 (docs/upsc-question-design-standard.md §6).

All 102 rows were read and classified. Before: analytic 21, precision 39, recall 42 (2 rows are Test 21's,
already tagged). 15 recall rows are rewritten in place with the same concept id, type and difficulty:
  - cases: a firm's exports and imports, a goods deficit set against the current account, two countries
    choosing between the IMF and the World Bank, four borrowers matched to the arms of the World Bank
    Group, and a country put on the FATF grey list;
  - mechanisms: what tariffs and quotas do differently, why FDI comes through Singapore and Mauritius, why MEIS gave way to RoDTEP, why fishing subsidies are banned, why a
    strong dollar shrinks the reserves, why the plans paused in 1966, why farm output per worker is low,
    the Mahalanobis logic, Lewis's surplus labour, and the aims of industrial licensing.
After: analytic 36, precision 39, recall 27. The other 85 rows keep their content and get their craft tag.
Leaks avoided while drafting (several candidates were left as they were):
  - OPEC+ cuts worsening India's current account (states the oil-prices AR's Statement I);
  - depreciation raising the rupee burden of external debt (answers the depreciation row's statement 3);
  - large imports from China (supports the RCEP MCQ's key);
  - TEPA's partner in an EFTA stem (answers the trade-agreements row's statement 3);
  - a devaluation making exports cheaper (states the depreciation row's statement 1), so the 1991 row was left;
  - per capita income as a full measure of development (repeats the growth-vs-development row);
  - gold imports and the deficit (the oil-prices AR's Statement I gives the same logic)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write_updates, CODE
from polity_common import C3, C4, T2

d.SUBJECT = "Economy"
d.REQUIRE_CRAFT = True
EX = "External Sector & International Institutions"
GD = "Growth, Development, Poverty & Planning"
NCM = "NCERT Class XII, Introductory Macroeconomics"
NCI = "NCERT Class XI, Indian Economic Development"
RBI = "Reserve Bank of India."

# ================================================================ MCQs (3)
M(EX, "medium", "A country is placed on the Financial Action Task Force's list of 'jurisdictions under increased monitoring' (the grey list). The most likely consequence is that:",
  "किसी देश को फ़ाइनेंशियल एक्शन टास्क फ़ोर्स की 'बढ़ी हुई निगरानी वाले क्षेत्राधिकारों' की सूची (ग्रे सूची) में डाला जाता है। इसका सबसे संभावित परिणाम यह है कि:",
  ["foreign banks and investors apply extra checks to its transactions, deterring inflows",
   "the International Monetary Fund suspends its membership until it is taken off the list",
   "the World Trade Organization authorises other members to impose trade sanctions on it",
   "its currency is dropped from the basket used to value the IMF's Special Drawing Rights"],
  ["विदेशी बैंक और निवेशक उसके लेन-देन की अतिरिक्त जाँच करते हैं, जिससे पूँजी-प्रवाह हतोत्साहित होता है",
   "अंतरराष्ट्रीय मुद्रा कोष सूची से हटाए जाने तक उसकी सदस्यता निलंबित कर देता है",
   "विश्व व्यापार संगठन अन्य सदस्यों को उस पर व्यापार प्रतिबंध लगाने की अनुमति देता है",
   "उसकी मुद्रा IMF के विशेष आहरण अधिकारों का मूल्य तय करने वाली टोकरी से हटा दी जाती है"],
  0,
  "The FATF sets standards against money laundering and terror financing and reviews countries against them. The grey list names countries with strategic deficiencies that have agreed to fix them; it carries no legal sanction, but banks, investors and rating agencies everywhere treat it as a warning, so they carry out enhanced due diligence on payments and investments, which raises costs and deters capital, as Pakistan found while on the list from 2018 to 2022. "
  "The FATF has no power over IMF membership, WTO trade rules or the SDR basket.",
  "FATF धन-शोधन और आतंक-वित्तपोषण के विरुद्ध मानक तय करता है और देशों की उनके आधार पर समीक्षा करता है। ग्रे सूची उन देशों के नाम बताती है जिनमें गंभीर कमियाँ हैं और जिन्होंने उन्हें दूर करने का वचन दिया है; इसके साथ कोई क़ानूनी प्रतिबंध नहीं जुड़ा, पर सब जगह बैंक, निवेशक और रेटिंग एजेंसियाँ इसे चेतावनी मानते हैं, इसलिए भुगतानों और निवेशों की गहन जाँच करते हैं, जिससे लागत बढ़ती और पूँजी हतोत्साहित होती है, जैसा पाकिस्तान ने 2018 से 2022 तक सूची में रहते हुए पाया। "
  "FATF का IMF सदस्यता, WTO व्यापार नियमों या SDR टोकरी पर कोई अधिकार नहीं है।",
  "Financial Action Task Force -- Jurisdictions under increased monitoring.", "ex-fatf-role", craft="linkage")

M(EX, "medium", "In 2021 India replaced the Merchandise Exports from India Scheme (MEIS) with the RoDTEP scheme, which refunds taxes and duties locked in the cost of exported goods. The main reason for the change was that:",
  "2021 में भारत ने भारत से वस्तु निर्यात योजना (MEIS) के स्थान पर RoDTEP योजना लागू की, जो निर्यातित वस्तुओं की लागत में फँसे करों और शुल्कों की वापसी करती है। इस बदलाव का मुख्य कारण यह था कि:",
  ["a WTO panel ruled that the MEIS was a prohibited export subsidy",
   "the MEIS had been open only to exporters of farm goods, not manufactures",
   "the RBI had stopped funding the MEIS out of its foreign exchange reserves",
   "the GST Council had asked for all export incentives to be paid by the States"],
  ["WTO के एक पैनल ने निर्णय दिया कि MEIS एक निषिद्ध निर्यात सब्सिडी थी",
   "MEIS केवल कृषि वस्तुओं के निर्यातकों के लिए थी, विनिर्मित वस्तुओं के लिए नहीं",
   "RBI ने अपने विदेशी मुद्रा भंडार से MEIS का वित्तपोषण बंद कर दिया था",
   "GST परिषद ने कहा था कि सभी निर्यात प्रोत्साहन राज्य दें"],
  0,
  "The MEIS paid exporters reward credits as a percentage of the value of their exports, so the benefit depended on exporting -- the definition of a prohibited subsidy under the WTO's Agreement on Subsidies and Countervailing Measures. In 2019 a WTO panel, in a case brought by the United States, ruled against it and other Indian schemes. "
  "RoDTEP only refunds central, State and local taxes that stay embedded in the cost of exports, such as duty on fuel used in transport, and rebating taxes actually borne by exports is allowed under WTO rules.",
  "MEIS निर्यातकों को उनके निर्यात मूल्य के प्रतिशत के रूप में पुरस्कार क्रेडिट देती थी, इसलिए लाभ निर्यात पर निर्भर था, जो WTO के सब्सिडी और प्रतिकारी उपाय समझौते के तहत निषिद्ध सब्सिडी की परिभाषा है। 2019 में अमेरिका द्वारा लाए गए मामले में WTO के एक पैनल ने इसके और अन्य भारतीय योजनाओं के विरुद्ध निर्णय दिया। "
  "RoDTEP केवल उन केंद्रीय, राज्य और स्थानीय करों की वापसी करती है जो निर्यात की लागत में फँसे रहते हैं, जैसे परिवहन में प्रयुक्त ईंधन पर शुल्क, और निर्यात द्वारा वास्तव में वहन किए गए करों की वापसी WTO नियमों के तहत अनुमत है।",
  "Directorate General of Foreign Trade -- RoDTEP scheme.", "ex-rodtep", craft="linkage")

M(GD, "medium", "Between 1966 and 1969 India ran three annual plans instead of starting the Fourth Five Year Plan. The main reason for this 'plan holiday' was that:",
  "1966 और 1969 के बीच भारत ने चौथी पंचवर्षीय योजना शुरू करने के बजाय तीन वार्षिक योजनाएँ चलाईं। इस 'योजना अवकाश' का मुख्य कारण यह था कि:",
  ["wars in 1962 and 1965, two severe droughts and a devaluation had thrown the Third Plan off course",
   "the Planning Commission had been abolished and replaced by a new body, which needed time to start work",
   "the Second Plan had overshot all its targets, so the government decided to pause and consolidate them",
   "a new constitutional amendment required every plan to be approved by all State legislatures first"],
  ["1962 और 1965 के युद्धों, दो भीषण सूखों और अवमूल्यन ने तीसरी योजना को पटरी से उतार दिया था",
   "योजना आयोग समाप्त कर एक नई संस्था बनाई गई थी, जिसे काम शुरू करने में समय चाहिए था",
   "दूसरी योजना ने सभी लक्ष्य पार कर लिए थे, इसलिए सरकार ने रुककर उन्हें सुदृढ़ करने का निर्णय लिया",
   "एक नए संविधान संशोधन के अनुसार हर योजना को पहले सभी राज्य विधानमंडलों की स्वीकृति चाहिए थी"],
  0,
  "The Third Plan (1961-66) was knocked off course by the war with China in 1962 and with Pakistan in 1965, by severe droughts in 1965-66 that brought food shortages and imports of grain, and by the devaluation of the rupee in 1966. With resources strained and the outlook unclear, the Fourth Plan was postponed and three annual plans were run until it began in 1969. "
  "The Planning Commission continued until it was replaced by NITI Aayog in 2015, and plans needed no approval from State legislatures.",
  "तीसरी योजना (1961-66) 1962 में चीन और 1965 में पाकिस्तान के साथ युद्ध, 1965-66 के भीषण सूखों से, जिनसे खाद्य कमी हुई और अनाज आयात करना पड़ा, और 1966 के रुपये के अवमूल्यन से पटरी से उतर गई। संसाधनों पर दबाव और अनिश्चित परिदृश्य के कारण चौथी योजना स्थगित की गई और 1969 में उसके शुरू होने तक तीन वार्षिक योजनाएँ चलाई गईं। "
  "योजना आयोग 2015 में नीति आयोग द्वारा प्रतिस्थापित होने तक चलता रहा, और योजनाओं को राज्य विधानमंडलों की स्वीकृति की आवश्यकता नहीं थी।",
  NCI, "gd-plan-holiday", craft="linkage")

# ================================================================ two-statement rows (6)
S(EX, "easy", "In a year an Indian firm exports textiles worth 10 million dollars and imports machinery worth 6 million dollars. Consider the following statements:",
  "एक वर्ष में एक भारतीय फ़र्म 1 करोड़ डॉलर के वस्त्र निर्यात करती है और 60 लाख डॉलर की मशीनरी आयात करती है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["Its exports bring foreign exchange into the country.",
   "Its imports also earn foreign exchange, so together its trade brings in 16 million dollars."],
  ["इसके निर्यात देश में विदेशी मुद्रा लाते हैं।",
   "इसके आयात भी विदेशी मुद्रा कमाते हैं, इसलिए कुल मिलाकर इसका व्यापार 1.6 करोड़ डॉलर लाता है।"],
  T2, 0,
  "Only statement 1 is correct. Foreign buyers pay for the textiles in foreign currency, which the firm converts into rupees, so exports add to the country's foreign exchange. Statement 2 is wrong: imports have to be paid for, so the machinery uses up 6 million dollars; on balance the firm's trade adds 4 million dollars, not 16.",
  "केवल कथन 1 सही है। विदेशी ख़रीदार वस्त्रों का भुगतान विदेशी मुद्रा में करते हैं, जिसे फ़र्म रुपये में बदलती है, इसलिए निर्यात देश की विदेशी मुद्रा बढ़ाते हैं। कथन 2 गलत है: आयात का भुगतान करना पड़ता है, इसलिए मशीनरी 60 लाख डॉलर खर्च करती है; शुद्ध रूप से फ़र्म का व्यापार 40 लाख डॉलर जोड़ता है, 1.6 करोड़ नहीं।",
  NCM, "ex-exports-imports-forex-easy", craft="application")

S(EX, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["A tariff on imported steel raises its price for buyers in India and brings revenue to the government.",
   "A quota caps the quantity of steel that can be imported, without bringing in any tariff revenue for the government."],
  ["आयातित इस्पात पर प्रशुल्क भारत में ख़रीदारों के लिए उसका दाम बढ़ाता है और सरकार को राजस्व देता है।",
   "कोटा आयात किए जा सकने वाले इस्पात की मात्रा सीमित करता है, सरकार को कोई प्रशुल्क राजस्व दिए बिना।"],
  T2, 2,
  "Both statements are correct. Both protect domestic producers, but differently: a tariff works through price, and the extra paid by buyers goes to the government as duty; a quota works through quantity, and the scarcity it creates raises the price too, but the gain -- the 'quota rent' -- goes to whoever holds the import licences. That is one reason the WTO's rules prefer tariffs, and converted many quotas into tariffs.",
  "दोनों कथन सही हैं। दोनों घरेलू उत्पादकों की रक्षा करते हैं, पर अलग ढंग से: प्रशुल्क क़ीमत के माध्यम से काम करता है, और ख़रीदारों द्वारा दिया गया अतिरिक्त शुल्क के रूप में सरकार को जाता है; कोटा मात्रा के माध्यम से काम करता है, और उससे बनी कमी भी क़ीमत बढ़ाती है, पर लाभ, यानी 'कोटा किराया', आयात लाइसेंस रखने वालों को जाता है। यही एक कारण है कि WTO के नियम प्रशुल्कों को प्राथमिकता देते हैं, और कई कोटों को प्रशुल्कों में बदल दिया गया।",
  NCM, "ex-tariffs-quotas-easy", craft="linkage")

S(EX, "easy", "In a year a country's exports of goods are 400 billion dollars and its imports of goods are 550 billion dollars. Consider the following statements:",
  "एक वर्ष में किसी देश का वस्तु-निर्यात 400 अरब डॉलर और वस्तु-आयात 550 अरब डॉलर है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["It has a merchandise trade deficit of 150 billion dollars.",
   "Its current account deficit for that year must therefore also be 150 billion dollars."],
  ["उसका वस्तु व्यापार घाटा 150 अरब डॉलर है।",
   "इसलिए उस वर्ष उसका चालू खाता घाटा भी 150 अरब डॉलर ही होना चाहिए।"],
  T2, 0,
  "Only statement 1 is correct: a trade deficit means imports of goods exceed exports, here by 150 billion dollars. Statement 2 does not follow: the current account also includes trade in services, income on investments and transfers such as remittances, so a surplus in services or large remittances can offset much of a goods deficit -- or a deficit in them can widen it.",
  "केवल कथन 1 सही है: व्यापार घाटे का अर्थ है वस्तुओं का आयात निर्यात से अधिक है, यहाँ 150 अरब डॉलर से। कथन 2 निष्कर्ष नहीं बनता: चालू खाते में सेवाओं का व्यापार, निवेशों पर आय और प्रेषण जैसे अंतरण भी शामिल हैं, इसलिए सेवाओं में अधिशेष या बड़े प्रेषण वस्तु घाटे के बड़े भाग की भरपाई कर सकते हैं, या उनमें घाटा उसे बढ़ा सकता है।",
  NCM, "ex-trade-deficit-easy", craft="inference")

S(EX, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Singapore and Mauritius have been the largest sources of FDI into India, partly because of their tax treaties with India and their role as financial hubs.",
   "Most of the gold that India consumes is mined within the country."],
  ["सिंगापुर और मॉरीशस भारत में FDI के सबसे बड़े स्रोत रहे हैं, आंशिक रूप से भारत के साथ उनकी कर संधियों और वित्तीय केंद्रों के रूप में उनकी भूमिका के कारण।",
   "भारत जितना सोना उपभोग करता है उसका अधिकांश देश के भीतर ही खनन से आता है।"],
  T2, 0,
  "Only statement 1 is correct. Much investment from the United States, Europe and elsewhere is channelled through holding companies in Singapore and Mauritius, which offered favourable tax treaties -- the treaty with Mauritius was amended in 2016 to tax capital gains -- and deep financial services. "
  "Statement 2 is wrong: India mines very little gold, mainly at Hutti in Karnataka, and imports almost all it uses, which makes gold one of its largest import items; that is why the government has offered Sovereign Gold Bonds and the gold monetisation scheme to wean savers off physical gold.",
  "केवल कथन 1 सही है। अमेरिका, यूरोप और अन्य जगहों का बहुत-सा निवेश सिंगापुर और मॉरीशस की होल्डिंग कंपनियों के माध्यम से आता है, जो अनुकूल कर संधियाँ देते थे, मॉरीशस के साथ संधि 2016 में पूँजीगत लाभ पर कर लगाने के लिए संशोधित की गई, और गहरी वित्तीय सेवाएँ भी। "
  "कथन 2 गलत है: भारत बहुत कम सोना निकालता है, मुख्यतः कर्नाटक के हट्टी में, और लगभग सारा उपयोग होने वाला सोना आयात करता है, जिससे सोना उसके सबसे बड़े आयातों में है; इसीलिए सरकार ने बचतकर्ताओं को भौतिक सोने से हटाने के लिए सॉवरेन गोल्ड बॉन्ड और स्वर्ण मुद्रीकरण योजना पेश की।",
  "Department for Promotion of Industry and Internal Trade -- FDI statistics.", "ex-fdi-source-gold-easy", craft="linkage")

S(EX, "easy", "Country A has run short of foreign exchange to pay for its imports. Country B wants long-term loans to build rural roads and schools. Consider the following statements:",
  "देश A के पास अपने आयातों का भुगतान करने के लिए विदेशी मुद्रा कम पड़ गई है। देश B ग्रामीण सड़कें और विद्यालय बनाने के लिए दीर्घकालिक ऋण चाहता है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["Country A would normally turn to the International Monetary Fund.",
   "Country B would normally turn to the World Bank."],
  ["देश A सामान्यतः अंतरराष्ट्रीय मुद्रा कोष की ओर जाएगा।",
   "देश B सामान्यतः विश्व बैंक की ओर जाएगा।"],
  T2, 2,
  "Both statements are correct. The two Bretton Woods institutions divide the work: the IMF watches over the international monetary system and lends, usually with policy conditions, to countries short of foreign exchange for their balance of payments, as it did for India in 1991 and for Sri Lanka in 2023; the World Bank finances long-term development -- roads, schools, health and water.",
  "दोनों कथन सही हैं। ब्रेटन वुड्स की दोनों संस्थाएँ काम बाँटती हैं: IMF अंतरराष्ट्रीय मौद्रिक प्रणाली पर नज़र रखता है और भुगतान संतुलन के लिए विदेशी मुद्रा की कमी वाले देशों को, प्रायः नीतिगत शर्तों के साथ, ऋण देता है, जैसे 1991 में भारत और 2023 में श्रीलंका को; विश्व बैंक दीर्घकालिक विकास, यानी सड़कों, विद्यालयों, स्वास्थ्य और जल, का वित्तपोषण करता है।",
  NCM, "ex-imf-world-bank-roles-easy", craft="application")

S(GD, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The literacy rate and life expectancy are among the indicators used to judge development.",
   "Since agriculture employs a much larger share of India's workers than its share of GDP, output per worker in agriculture is lower than in the rest of the economy."],
  ["साक्षरता दर और जीवन-प्रत्याशा विकास को आँकने वाले सूचकों में से हैं।",
   "चूँकि कृषि में GDP के अपने हिस्से की तुलना में भारत के श्रमिकों का कहीं बड़ा हिस्सा काम करता है, इसलिए कृषि में प्रति श्रमिक उत्पादन शेष अर्थव्यवस्था से कम है।"],
  T2, 2,
  "Both statements are correct. Development is judged by people's well-being as well as income, so health and education measures such as life expectancy and literacy enter indices like the HDI. "
  "Agriculture employs about 45 per cent of India's workforce but produces less than a fifth of GDP, so each farm worker produces on average far less than a worker in industry or services -- a sign of disguised unemployment and the reason moving workers out of farming raises incomes.",
  "दोनों कथन सही हैं। विकास को आय के साथ-साथ लोगों के कल्याण से आँका जाता है, इसलिए जीवन-प्रत्याशा और साक्षरता जैसे स्वास्थ्य और शिक्षा के माप HDI जैसे सूचकांकों में आते हैं। "
  "कृषि भारत के लगभग 45 प्रतिशत श्रमबल को काम देती है पर GDP का पाँचवें भाग से कम पैदा करती है, इसलिए हर कृषि श्रमिक औसतन उद्योग या सेवाओं के श्रमिक से कहीं कम उत्पादन करता है, जो प्रच्छन्न बेरोज़गारी का संकेत है और यही कारण है कि श्रमिकों को खेती से बाहर ले जाने से आय बढ़ती है।",
  NCI, "gd-development-indicators-easy", craft="inference")

# ================================================================ three- and four-statement rows (6)
S(EX, "hard", "Consider the following statements about the WTO Agreement on Fisheries Subsidies:",
  "मत्स्य सब्सिडी पर WTO समझौते के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It prohibits subsidies to illegal, unreported and unregulated fishing.",
   "Such subsidies are targeted because they keep more boats at sea than the fish stocks can sustain, driving overfishing.",
   "It entered into force in 2025."],
  ["यह अवैध, अप्रतिवेदित और अविनियमित मत्स्यन को दी जाने वाली सब्सिडी पर रोक लगाता है।",
   "ऐसी सब्सिडी को इसलिए लक्षित किया गया है कि वे मछलियों के भंडार की सहन-क्षमता से अधिक नावों को समुद्र में बनाए रखती हैं, जिससे अति-मत्स्यन होता है।",
   "यह 2025 में लागू हुआ।"],
  C3, 2,
  "All three are correct. Fuel, vessel and other subsidies lower the cost of fishing, so fleets keep fishing even when catches fall, which depletes the stocks; the agreement therefore bans subsidies for illegal, unreported and unregulated fishing, for fishing overfished stocks and for fishing on the unregulated high seas. "
  "Adopted at the Twelfth Ministerial Conference in 2022, it came into force in September 2025, once two-thirds of members had accepted it; rules on subsidies that drive overcapacity are still being negotiated.",
  "तीनों कथन सही हैं। ईंधन, नौका और अन्य सब्सिडी मत्स्यन की लागत घटाती हैं, इसलिए पकड़ गिरने पर भी बेड़े मछली पकड़ते रहते हैं, जिससे भंडार घटते हैं; इसलिए समझौता अवैध, अप्रतिवेदित और अविनियमित मत्स्यन, अति-दोहित भंडारों के मत्स्यन और अविनियमित खुले समुद्र में मत्स्यन के लिए सब्सिडी पर रोक लगाता है। "
  "2022 के बारहवें मंत्रिस्तरीय सम्मेलन में अपनाया गया यह सितंबर 2025 में, दो-तिहाई सदस्यों के स्वीकार करने पर, लागू हुआ; अति-क्षमता बढ़ाने वाली सब्सिडी के नियमों पर अभी वार्ता चल रही है।",
  "World Trade Organization -- Agreement on Fisheries Subsidies.", "ex-wto-fisheries-subsidies", craft="linkage")

S(EX, "medium", "Consider the following statements about India's foreign exchange reserves:",
  "भारत के विदेशी मुद्रा भंडार के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["India's foreign exchange reserves are the largest in the world.",
   "Since foreign currency assets, the largest part of the reserves, include assets in euros, yen and pounds, a rise of the dollar against those currencies can lower the reserves' dollar value without any sale.",
   "The RBI is the custodian of the country's foreign exchange reserves."],
  ["भारत का विदेशी मुद्रा भंडार संसार में सबसे बड़ा है।",
   "चूँकि भंडार के सबसे बड़े भाग, विदेशी मुद्रा परिसंपत्तियों, में यूरो, येन और पाउंड की परिसंपत्तियाँ भी हैं, इसलिए उन मुद्राओं के मुक़ाबले डॉलर के मज़बूत होने से बिना किसी बिक्री के भंडार का डॉलर मूल्य घट सकता है।",
   "RBI देश के विदेशी मुद्रा भंडार का संरक्षक है।"],
  C3, 1,
  "Statements 2 and 3 are correct. The reserves are reported in dollars, so their non-dollar assets, and gold, are revalued every week; a stronger dollar or a fall in the gold price can shrink the total even when the RBI has sold nothing -- the 'valuation change' that often explains weekly swings. The RBI holds and manages the reserves under the RBI Act. "
  "Statement 1 is wrong: India's reserves are among the four or five largest in the world, but China's, Japan's and Switzerland's are larger.",
  "कथन 2 और 3 सही हैं। भंडार डॉलर में बताए जाते हैं, इसलिए उनकी ग़ैर-डॉलर परिसंपत्तियों और सोने का हर सप्ताह पुनर्मूल्यन होता है; मज़बूत डॉलर या सोने के दाम में गिरावट कुल राशि को घटा सकती है, भले RBI ने कुछ न बेचा हो, यही 'मूल्यांकन परिवर्तन' प्रायः साप्ताहिक उतार-चढ़ाव समझाता है। RBI अधिनियम के तहत RBI भंडार रखता और प्रबंधित करता है। "
  "कथन 1 गलत है: भारत का भंडार संसार के चार-पाँच सबसे बड़े भंडारों में है, पर चीन, जापान और स्विट्ज़रलैंड के भंडार बड़े हैं।",
  RBI, "ex-forex-reserves-basics", craft="linkage")

S(EX, "medium", "Consider the following statements about the World Bank Group:",
  "विश्व बैंक समूह के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["A low-income country seeking a loan at little or no interest would borrow from the International Development Association rather than the IBRD.",
   "A foreign company investing in a conflict-prone country could buy cover against political risks from the Multilateral Investment Guarantee Agency.",
   "The International Finance Corporation lends mainly to governments for public works.",
   "The IBRD lends mainly to middle-income and creditworthy lower-income countries."],
  ["कम या बिना ब्याज का ऋण चाहने वाला निम्न-आय देश IBRD के बजाय अंतरराष्ट्रीय विकास संघ से उधार लेगा।",
   "संघर्ष-प्रवण देश में निवेश करने वाली विदेशी कंपनी बहुपक्षीय निवेश गारंटी एजेंसी से राजनीतिक जोखिमों के विरुद्ध बीमा ले सकती है।",
   "अंतरराष्ट्रीय वित्त निगम मुख्यतः सरकारों को सार्वजनिक कार्यों के लिए ऋण देता है।",
   "IBRD मुख्यतः मध्यम-आय और ऋण-योग्य निम्न-आय देशों को ऋण देता है।"],
  C4, 2,
  "Statements 1, 2 and 4 are correct. The IDA gives the poorest countries grants and long-term credits at little or no interest; India, once its largest borrower, 'graduated' in 2014 and now borrows from the IBRD at market-linked rates. MIGA does not lend: it covers investors against risks such as expropriation, war and currency restrictions. "
  "Statement 3 is wrong: the IFC invests in and lends to private companies in developing countries; lending to governments is the work of the IBRD and the IDA.",
  "कथन 1, 2 और 4 सही हैं। IDA सबसे ग़रीब देशों को अनुदान और कम या बिना ब्याज के दीर्घकालिक ऋण देता है; कभी उसका सबसे बड़ा उधारकर्ता भारत 2014 में उससे 'स्नातक' हो गया और अब IBRD से बाज़ार-आधारित दरों पर उधार लेता है। MIGA ऋण नहीं देता: यह निवेशकों को अधिग्रहण, युद्ध और मुद्रा प्रतिबंधों जैसे जोखिमों के विरुद्ध सुरक्षा देता है। "
  "कथन 3 गलत है: IFC विकासशील देशों की निजी कंपनियों में निवेश करता और उन्हें ऋण देता है; सरकारों को ऋण देना IBRD और IDA का काम है।",
  "World Bank Group.", "ex-world-bank-group", craft="application")

S(GD, "medium", "Consider the following statements about India's Five Year Plans:",
  "भारत की पंचवर्षीय योजनाओं के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The First Five Year Plan gave priority to heavy industry.",
   "The Second Five Year Plan, based on the Mahalanobis model, stressed heavy industry, holding that building capital goods first would raise the economy's growth later.",
   "The Twelfth Five Year Plan ended in 2012."],
  ["पहली पंचवर्षीय योजना ने भारी उद्योग को प्राथमिकता दी।",
   "महालनोबिस मॉडल पर आधारित दूसरी पंचवर्षीय योजना ने भारी उद्योग पर बल दिया, यह मानते हुए कि पहले पूँजीगत वस्तुएँ बनाने से बाद में अर्थव्यवस्था की वृद्धि बढ़ेगी।",
   "बारहवीं पंचवर्षीय योजना 2012 में समाप्त हुई।"],
  C3, 0,
  "Only statement 2 is correct. P.C. Mahalanobis argued that investment in the industries that make machines and steel would expand the economy's capacity to invest, and so its future growth, even if it held back consumption at first -- hence the steel plants and heavy industry of the Second Plan (1956-61). "
  "Statement 1 is wrong: coming after Partition and food shortages, the First Plan (1951-56) gave priority to agriculture and irrigation. Statement 3 is wrong: the Twelfth Plan ran from 2012 to 2017 and was the last.",
  "केवल कथन 2 सही है। पी.सी. महालनोबिस का तर्क था कि मशीनें और इस्पात बनाने वाले उद्योगों में निवेश अर्थव्यवस्था की निवेश-क्षमता और इसलिए उसकी भावी वृद्धि बढ़ाएगा, भले आरंभ में उपभोग कम रहे, इसीलिए दूसरी योजना (1956-61) में इस्पात संयंत्र और भारी उद्योग आए। "
  "कथन 1 गलत है: विभाजन और खाद्य कमी के बाद आई पहली योजना (1951-56) ने कृषि और सिंचाई को प्राथमिकता दी। कथन 3 गलत है: बारहवीं योजना 2012 से 2017 तक चली और अंतिम थी।",
  NCI, "gd-five-year-plans", craft="linkage")

S(GD, "hard", "Consider the following statements about some ideas in development economics:",
  "विकास अर्थशास्त्र के कुछ विचारों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["In W. Arthur Lewis's dual-sector model, modern industry can expand for a long time without raising wages, because it draws on surplus labour from traditional agriculture.",
   "The 'big push' theory argues for large, coordinated investment across many sectors at once, because industries depend on one another's markets.",
   "The phrase 'Hindu rate of growth' referred to India's growth of about 7 per cent a year before the 1980s."],
  ["डब्ल्यू. आर्थर लुईस के द्वि-क्षेत्र मॉडल में आधुनिक उद्योग लंबे समय तक मज़दूरी बढ़ाए बिना फैल सकता है, क्योंकि वह पारंपरिक कृषि के अधिशेष श्रम पर निर्भर करता है।",
   "'बिग पुश' सिद्धांत कई क्षेत्रों में एक साथ बड़े, समन्वित निवेश का समर्थन करता है, क्योंकि उद्योग एक-दूसरे के बाज़ारों पर निर्भर हैं।",
   "'हिंदू विकास दर' शब्द 1980 के दशक से पहले भारत की लगभग 7 प्रतिशत वार्षिक वृद्धि के लिए प्रयुक्त होता था।"],
  C3, 1,
  "Statements 1 and 2 are correct. Lewis argued that where farms hold more workers than they need, industry can hire them at a wage just above rural earnings until the surplus is used up, keeping profits and investment high. Paul Rosenstein-Rodan's big push held that a single factory fails for lack of buyers, but many investments together create markets for one another. "
  "Statement 3 is wrong: Raj Krishna's phrase described India's slow growth of about 3.5 per cent a year from the 1950s to the 1970s.",
  "कथन 1 और 2 सही हैं। लुईस का तर्क था कि जहाँ खेतों में आवश्यकता से अधिक श्रमिक हों, वहाँ उद्योग उन्हें ग्रामीण आय से थोड़ी अधिक मज़दूरी पर तब तक रख सकता है जब तक अधिशेष ख़त्म न हो, जिससे लाभ और निवेश ऊँचे रहते हैं। पॉल रोज़ेनस्टाइन-रोडान के बिग पुश के अनुसार अकेला कारख़ाना ख़रीदारों के अभाव में विफल होता है, पर कई निवेश मिलकर एक-दूसरे के लिए बाज़ार बनाते हैं। "
  "कथन 3 गलत है: राज कृष्ण का यह शब्द 1950 से 1970 के दशक तक भारत की लगभग 3.5 प्रतिशत वार्षिक धीमी वृद्धि के लिए था।",
  NCI, "gd-lewis-big-push-hindu-rate", craft="linkage")

S(GD, "medium", "Consider the following statements about India's development strategy between 1950 and 1990:",
  "1950 और 1990 के बीच भारत की विकास रणनीति के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Import substitution was the main strategy of trade policy.",
   "The Industrial Policy Resolution of 1956 reserved a number of industries for the public sector.",
   "Industrial licensing was used both to steer new private industry towards backward regions and to prevent the concentration of economic power."],
  ["आयात प्रतिस्थापन व्यापार नीति की मुख्य रणनीति थी।",
   "1956 के औद्योगिक नीति प्रस्ताव ने कई उद्योग सार्वजनिक क्षेत्र के लिए आरक्षित किए।",
   "औद्योगिक लाइसेंसिंग का उपयोग नए निजी उद्योग को पिछड़े क्षेत्रों की ओर मोड़ने और आर्थिक शक्ति के केंद्रीकरण को रोकने, दोनों के लिए किया गया।"],
  C3, 2,
  "All three are correct. Planners sought self-reliance by producing at home what had been imported, behind tariffs and quotas; the 1956 Resolution put 17 industries, including arms, atomic energy, railways and heavy industry, in Schedule A for the state. "
  "A licence was needed to set up or expand a factory, and the government used it to direct units to backward areas, to protect small industry and to keep large business houses from growing too dominant -- aims that in practice also bred delay and the 'licence raj'.",
  "तीनों कथन सही हैं। योजनाकारों ने प्रशुल्कों और कोटों की आड़ में आयातित वस्तुएँ देश में बनाकर आत्मनिर्भरता चाही; 1956 के प्रस्ताव ने हथियार, परमाणु ऊर्जा, रेलवे और भारी उद्योग सहित 17 उद्योगों को राज्य के लिए अनुसूची A में रखा। "
  "कारख़ाना लगाने या बढ़ाने के लिए लाइसेंस चाहिए था, और सरकार ने उसका उपयोग इकाइयों को पिछड़े क्षेत्रों की ओर ले जाने, लघु उद्योग की रक्षा और बड़े व्यावसायिक घरानों को अत्यधिक प्रभावी होने से रोकने के लिए किया, ऐसे उद्देश्य जिनसे व्यवहार में देरी और 'लाइसेंस राज' भी पनपा।",
  NCI, "gd-1950-90-strategy", craft="linkage")

# ================================================================ TAGS for the 85 kept rows (Test 21's 2 are tagged already)
TAGS = {
 "ex-edible-oil-imports-easy": "linkage", "ex-wto-predictability-easy": "linkage", "ex-g20-secretariat-summits": "precision",
 "ex-reserves-capital-inflows": "linkage", "ex-fed-hikes-rupee": "linkage", "ex-floating-rate-parity": "precision",
 "ex-india-founding-bretton-woods": "recall", "ex-ndb-members": "precision", "ex-oil-prices-cad": "linkage",
 "ex-services-exports-growth": "precision", "ex-wto-appellate-body-crisis": "linkage", "ex-headquarters-pairs-easy": "recall",
 "ex-committees-pairs": "recall", "ex-wto-agreements-pairs": "recall", "ex-ibsa-easy": "precision",
 "ex-merchandise-trade-easy": "application", "ex-opec-easy": "recall", "ex-depreciation-numerical": "application",
 "ex-efta-members": "recall", "ex-rcep-india-opt-out": "linkage", "ex-brics-2024-expansion": "recall",
 "ex-dutch-disease": "precision", "ex-hot-money": "precision", "ex-largest-import-source-china": "recall",
 "ex-reserves-not-nri-deposits": "precision", "ex-world-investment-report": "recall", "ex-wto-mfn": "precision",
 "ex-g7-adb-membership-easy": "recall", "ex-imf-wto-headquarters-easy": "recall", "ex-rupee-depreciation-easy": "inference",
 "ex-saarc-asean-easy": "recall", "ex-cad-saving-investment": "inference", "ex-external-debt-composition": "recall",
 "ex-imf-lending-facilities": "precision", "ex-impossible-trinity": "inference", "ex-j-curve-marshall-lerner-tot": "precision",
 "ex-neer-reer": "precision", "ex-sdr": "precision", "ex-wto-sdt-self-declaration": "precision",
 "ex-aiib-adb": "recall", "ex-bis-oecd-fatf": "recall", "ex-bop-accounts": "precision",
 "ex-depreciation-effects": "linkage", "ex-doing-business-bready": "recall", "ex-fdi-policy-routes": "precision",
 "ex-fdi-vs-fpi": "precision", "ex-fema": "precision", "ex-foreign-trade-policy-2023": "recall",
 "ex-g20-au-eu-presidency": "recall", "ex-imf-basics": "precision", "ex-imf-reports-article-iv-none": "recall",
 "ex-india-current-account": "recall", "ex-india-trade-agreements": "precision", "ex-ipef-saarc-fund": "recall",
 "ex-liberalised-remittance-scheme": "precision", "ex-rupee-convertibility": "precision", "ex-rupee-internationalisation": "recall",
 "ex-rupee-managed-float": "precision", "ex-sovereign-debt-common-framework": "precision", "ex-special-economic-zones": "precision",
 "ex-trade-remedies": "precision", "ex-wto-basics": "precision", "ex-wto-dispute-rules": "precision",
 "ex-wto-peace-clause": "precision", "ex-wto-subsidy-boxes": "precision", "ex-wto-tfa-ita-gpa": "recall",
 "gd-education-productivity-easy": "linkage", "gd-mpi-fall-schemes": "linkage", "gd-informal-sector-eshram": "linkage",
 "gd-population-per-capita-income": "linkage", "gd-tertiary-sector-easy": "recall", "gd-rule-of-70": "application",
 "gd-jobless-growth": "precision", "gd-merit-goods": "application", "gd-gdp-meaning-easy": "precision",
 "gd-growth-vs-development-easy": "precision", "gd-growth-models-icor": "precision", "gd-international-poverty-line": "precision",
 "gd-1991-reforms": "recall", "gd-inequality-gini-lorenz-kuznets": "precision", "gd-national-mpi": "precision",
 "gd-plans-eighth-fifth-ndc": "recall", "gd-plfs": "recall", "gd-poverty-lines": "precision",
 "gd-unemployment-types": "precision"}

if __name__ == "__main__":
    write_updates("upg_l2_t16_econ.sql", statuses=("draft", "published"), tags=TAGS)
