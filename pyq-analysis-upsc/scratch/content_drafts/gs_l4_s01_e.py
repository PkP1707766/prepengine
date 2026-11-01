# -*- coding: utf-8 -*-
"""Level 4 · Simulator 1 (GS Paper I full mock, Layout A: the 2023/24 shape) -- part E: Economy (15)
(upsc_l4_gs_cell_targets.mjs 1).
From a whole-bank sweep of concepts, instruments and schemes no row tests: the minimum export price; neem-coated
urea; Vivad se Vishwas; the US dollar index; the term premium; participatory notes; quantitative easing and
tightening and negative rates; retail algorithmic trading; export-oriented units; PMEGP; the Foreign Trade Policy
2023, Advance Authorisation and RoSCTL; Giffen goods; the velocity of money; bracket creep, presumptive taxation,
BEPS and fiscal drag; the Payments Infrastructure Development Fund. MCQ keys are pinned (pos)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Economy"
d.REQUIRE_CRAFT = True

# ---------------------------------------------------------------- Agriculture & Food Economy (MCQ, medium)
M("Agriculture & Food Economy", "medium",
  "When the Government sets a 'minimum export price' (MEP) on a farm commodity such as onions, it means that",
  "जब सरकार प्याज़ जैसी किसी कृषि वस्तु पर ‘न्यूनतम निर्यात मूल्य’ (एमईपी) तय करती है, तो इसका अर्थ है कि",
  ["the commodity cannot be exported at a price below that level",
   "the Government will buy any unsold stock from farmers at that price",
   "exporters receive a subsidy equal to the gap between that price and the market price",
   "domestic traders cannot sell the commodity in India below that price"],
  ["वस्तु का उस स्तर से कम मूल्य पर निर्यात नहीं किया जा सकता",
   "सरकार किसानों से कोई भी बिना बिका भंडार उस मूल्य पर ख़रीद लेगी",
   "निर्यातकों को उस मूल्य और बाज़ार मूल्य के अंतर के बराबर सब्सिडी मिलती है",
   "घरेलू व्यापारी देश में उस मूल्य से कम पर वस्तु नहीं बेच सकते"],
  0,
  "An MEP is a floor below which exports are not allowed, set by the Directorate General of Foreign Trade under the Foreign Trade Policy. It is a softer tool than an outright export ban: by making exports viable only at high prices, it keeps more of the crop at home when domestic prices are rising, as was done for onions and basmati rice. "
  "It is not a procurement price -- the minimum support price is the price at which the Government buys -- nor an export subsidy, and it does not control domestic prices. Because it can cut farmers' returns when world prices are high, its use is a running trade-off between consumers and growers.",
  "एमईपी वह न्यूनतम सीमा है जिसके नीचे निर्यात की अनुमति नहीं होती, जिसे विदेश व्यापार नीति के अंतर्गत विदेश व्यापार महानिदेशालय तय करता है। यह सीधे निर्यात-प्रतिबंध से नरम उपाय है: निर्यात को केवल ऊँचे मूल्यों पर लाभकारी बनाकर यह घरेलू क़ीमतें बढ़ने पर अधिक फ़सल देश में रखता है, जैसा प्याज़ और बासमती चावल के लिए किया गया। "
  "यह ख़रीद मूल्य नहीं है -- न्यूनतम समर्थन मूल्य वह क़ीमत है जिस पर सरकार ख़रीदती है -- न ही निर्यात सब्सिडी, और यह घरेलू क़ीमतों को नियंत्रित नहीं करता। चूँकि विश्व क़ीमतें ऊँची होने पर यह किसानों का प्रतिफल घटा सकता है, इसका उपयोग उपभोक्ताओं और उत्पादकों के बीच निरंतर संतुलन है।",
  "Directorate General of Foreign Trade, notifications on minimum export prices; Foreign Trade Policy 2023.",
  "l4-s01-eco-minimum-export-price-floor-not-procurement", pos=0, craft="application")

# ---------------------------------------------------------------- Agriculture & Food Economy (statement, medium)
S("Agriculture & Food Economy", "medium", "With reference to neem-coated urea, consider the following statements:",
  "नीम-लेपित यूरिया के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["All urea produced in India has been required to be neem-coated since 2015.",
   "Neem coating speeds up the release of nitrogen from urea in the soil.",
   "Neem coating raises the nitrogen content of urea above 46 per cent."],
  ["2015 से भारत में उत्पादित समस्त यूरिया का नीम-लेपित होना अनिवार्य है।",
   "नीम लेपन मिट्टी में यूरिया से नाइट्रोजन के निकलने को तेज़ करता है।",
   "नीम लेपन यूरिया में नाइट्रोजन की मात्रा को 46 प्रतिशत से ऊपर बढ़ा देता है।"],
  C3, 0,
  "Only statement 1 is correct. Since 2015 all domestically produced and imported urea has had to be neem-coated. "
  "Statement 2 reverses the effect: compounds in neem oil act as a mild nitrification inhibitor, slowing the conversion of urea's nitrogen so that less is lost by leaching and as gas and more is taken up by the crop. Statement 3 is wrong: the coating does not change urea's nitrogen content, which stays at about 46 per cent. A large part of the policy's purpose was also to stop the diversion of heavily subsidised farm urea to industries such as plywood and dyes, since the coated product is unsuited to them.",
  "केवल कथन 1 सही है। 2015 से देश में उत्पादित और आयातित समस्त यूरिया का नीम-लेपित होना अनिवार्य है। "
  "कथन 2 प्रभाव को उलट देता है: नीम तेल के यौगिक हल्के नाइट्रीकरण-अवरोधक का काम करते हैं, यूरिया के नाइट्रोजन के रूपांतरण को धीमा करते हैं, जिससे निक्षालन और गैस के रूप में कम हानि होती है और फ़सल अधिक ग्रहण करती है। कथन 3 ग़लत है: लेपन यूरिया की नाइट्रोजन मात्रा नहीं बदलता, जो लगभग 46 प्रतिशत बनी रहती है। नीति का बड़ा उद्देश्य भारी सब्सिडी वाले कृषि यूरिया के प्लाइवुड और रंजक जैसे उद्योगों की ओर अपवर्तन को रोकना भी था, क्योंकि लेपित उत्पाद उनके लिए अनुपयुक्त है।",
  "Department of Fertilizers, neem coating of urea (2015); Fertiliser (Control) Order, 1985.",
  "l4-s01-eco-neem-coated-urea-2015-slow-release-46", craft="precision")

# ---------------------------------------------------------------- Budget, Deficits & Public Debt (statement, medium)
S("Budget, Deficits & Public Debt", "medium", "With reference to the 'Vivad se Vishwas' schemes, consider the following statements:",
  "‘विवाद से विश्वास’ योजनाओं के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["They let taxpayers settle pending direct-tax disputes by paying the disputed tax, with interest and penalty waived wholly or in part.",
   "The 2024 scheme covered only disputes pending before the Supreme Court.",
   "They apply to disputes under the Goods and Services Tax as well."],
  ["ये करदाताओं को विवादित कर चुकाकर, ब्याज और जुर्माने की पूर्ण या आंशिक छूट के साथ, लंबित प्रत्यक्ष-कर विवाद निपटाने देती हैं।",
   "2024 की योजना केवल सर्वोच्च न्यायालय में लंबित विवादों पर लागू थी।",
   "ये वस्तु और सेवा कर के विवादों पर भी लागू होती हैं।"],
  C3, 0,
  "Only statement 1 is correct. Under the Direct Tax Vivad se Vishwas Act, 2020 and the Direct Tax Vivad se Vishwas Scheme, 2024, a taxpayer with an appeal pending can settle by paying the disputed tax (half of it if the department, not the taxpayer, had filed the appeal), and the interest and penalty are waived; the State gets revenue that is otherwise locked up for years and the courts are relieved of litigation. "
  "Statement 2 is wrong: the 2024 scheme covered appeals and petitions pending before the Commissioners (Appeals), the Income Tax Appellate Tribunal, the High Courts and the Supreme Court, as well as some objections and revision petitions. Statement 3 is wrong: they are confined to income tax; GST disputes were dealt with through a separate waiver of interest and penalty for older periods, under the GST law itself.",
  "केवल कथन 1 सही है। प्रत्यक्ष कर विवाद से विश्वास अधिनियम, 2020 और प्रत्यक्ष कर विवाद से विश्वास योजना, 2024 के अंतर्गत लंबित अपील वाला करदाता विवादित कर (यदि अपील करदाता ने नहीं, विभाग ने दायर की थी तो उसका आधा) चुकाकर निपटान कर सकता है, और ब्याज तथा जुर्माना माफ़ होते हैं; राज्य को वर्षों से फँसा राजस्व मिलता है और न्यायालयों का मुक़दमों का बोझ घटता है। "
  "कथन 2 ग़लत है: 2024 की योजना आयुक्त (अपील), आयकर अपील अधिकरण, उच्च न्यायालयों और सर्वोच्च न्यायालय में लंबित अपीलों और याचिकाओं, तथा कुछ आपत्तियों और पुनरीक्षण याचिकाओं पर लागू थी। कथन 3 ग़लत है: ये आयकर तक सीमित हैं; जीएसटी विवादों को स्वयं जीएसटी विधि के अंतर्गत पुरानी अवधियों के ब्याज और जुर्माने की अलग छूट से निपटाया गया।",
  "Direct Tax Vivad se Vishwas Act, 2020; Finance (No. 2) Act, 2024 (Direct Tax Vivad se Vishwas Scheme, 2024); Central Board of Direct Taxes.",
  "l4-s01-eco-vivad-se-vishwas-direct-tax-all-forums-not-gst", craft="precision")

# ---------------------------------------------------------------- External Sector & International Institutions (statement, medium)
S("External Sector & International Institutions", "medium", "With reference to the US dollar index, often cited in the news, consider the following statements:",
  "समाचारों में प्रायः उद्धृत अमेरिकी डॉलर सूचकांक के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["It measures the value of the US dollar against a basket of six major currencies.",
   "The euro carries the largest weight in the basket.",
   "The Chinese yuan is one of the currencies in the basket."],
  ["यह अमेरिकी डॉलर का मूल्य छह प्रमुख मुद्राओं की टोकरी के सापेक्ष मापता है।",
   "टोकरी में यूरो का भार सबसे अधिक है।",
   "चीनी युआन टोकरी की मुद्राओं में से एक है।"],
  C3, 1,
  "Statements 1 and 2 are correct. The index, set at 100 in March 1973 when the Bretton Woods system of fixed exchange rates ended, compares the dollar with the euro (about 58 per cent of the weight), the Japanese yen, the pound sterling, the Canadian dollar, the Swedish krona and the Swiss franc; a rising index means a stronger dollar. "
  "Statement 3 is wrong: the basket has not been changed since the euro replaced its member currencies in 1999, so it leaves out China and other large emerging economies -- one reason why the index is a gauge of the dollar against rich-country currencies rather than of its overall trade-weighted value. A strong dollar index usually means capital flowing out of emerging markets and pressure on currencies such as the rupee.",
  "कथन 1 और 2 सही हैं। मार्च 1973 में, जब ब्रेटन वुड्स की स्थिर विनिमय दर प्रणाली समाप्त हुई, 100 पर तय यह सूचकांक डॉलर की तुलना यूरो (भार का लगभग 58 प्रतिशत), जापानी येन, पाउंड स्टर्लिंग, कनाडाई डॉलर, स्वीडिश क्रोना और स्विस फ़्रैंक से करता है; बढ़ता सूचकांक मज़बूत डॉलर दर्शाता है। "
  "कथन 3 ग़लत है: 1999 में यूरो द्वारा अपनी सदस्य मुद्राओं का स्थान लेने के बाद से टोकरी नहीं बदली, इसलिए इसमें चीन और अन्य बड़ी उभरती अर्थव्यवस्थाएँ नहीं हैं -- इसी कारण यह सूचकांक डॉलर के समग्र व्यापार-भारित मूल्य के बजाय धनी देशों की मुद्राओं के सापेक्ष उसका मापक है। मज़बूत डॉलर सूचकांक का अर्थ प्रायः उभरते बाज़ारों से पूँजी का निकलना और रुपये जैसी मुद्राओं पर दबाव होता है।",
  "Intercontinental Exchange, US Dollar Index (DXY) methodology; Reserve Bank of India, Monetary Policy Reports (external sector).",
  "l4-s01-eco-dollar-index-six-currencies-euro-no-yuan", craft="precision")

# ---------------------------------------------------------------- Financial Markets, Instruments & Fintech (MCQ, medium)
M("Financial Markets, Instruments & Fintech", "medium",
  "The 'term premium' on a long-term government bond is best described as",
  "दीर्घकालिक सरकारी बॉन्ड पर ‘टर्म प्रीमियम’ का सबसे अच्छा वर्णन है",
  ["the fee that a government pays to banks for underwriting an issue of long-term bonds",
   "the extra yield demanded for holding a long bond rather than rolling over short ones",
   "the amount by which a bond's market price exceeds its face value",
   "the tax charged on interest earned from bonds held beyond a year"],
  ["वह शुल्क जो कोई सरकार अपने दीर्घकालिक बॉन्डों के निर्गम की हामीदारी के लिए बैंकों को चुकाती है",
   "छोटे बॉन्ड बार-बार नवीकृत करने के बजाय लंबा बॉन्ड रखने पर माँगा गया अतिरिक्त प्रतिफल",
   "वह राशि जिससे बॉन्ड का बाज़ार मूल्य उसके अंकित मूल्य से अधिक होता है",
   "एक वर्ष से अधिक रखे गए बॉन्डों पर अर्जित ब्याज पर लगने वाला कर"],
  1,
  "The yield on a long bond reflects two things: the path of short-term interest rates that investors expect over its life, and a premium for the risk of being locked in -- if inflation or rates turn out higher than expected, the bond's price falls. That second part is the term premium. It explains why long-term yields can rise even when the central bank is expected to cut its policy rate, for instance when government borrowing grows or inflation becomes more uncertain, and why central banks buying long bonds (quantitative easing) aims partly at compressing it. "
  "Underwriting fees, a bond trading above its face value (a premium to par) and taxes on interest are all different things.",
  "दीर्घकालिक बॉन्ड का प्रतिफल दो चीज़ें दर्शाता है: उसकी अवधि में अल्पकालिक ब्याज दरों का अपेक्षित मार्ग, और बँध जाने के जोखिम का प्रीमियम -- यदि मुद्रास्फीति या दरें अपेक्षा से ऊँची निकलें, तो बॉन्ड का मूल्य गिरता है। यही दूसरा भाग टर्म प्रीमियम है। यह बताता है कि केंद्रीय बैंक से नीतिगत दर घटाने की अपेक्षा होने पर भी दीर्घकालिक प्रतिफल क्यों बढ़ सकते हैं, जैसे जब सरकारी उधारी बढ़े या मुद्रास्फीति अधिक अनिश्चित हो जाए, और केंद्रीय बैंकों द्वारा लंबे बॉन्ड ख़रीदना (मात्रात्मक सहजता) अंशतः इसे दबाने के लिए क्यों होता है। "
  "हामीदारी शुल्क, अंकित मूल्य से ऊपर व्यापार होता बॉन्ड (सममूल्य से प्रीमियम) और ब्याज पर कर, सब अलग चीज़ें हैं।",
  "Reserve Bank of India, Financial Stability Report and Monetary Policy Report (yield curve); NCERT, Introductory Macroeconomics (Class XII), money and interest.",
  "l4-s01-eco-term-premium-long-bond-yield", pos=1, craft="inference")

# ---------------------------------------------------------------- Financial Markets, Instruments & Fintech (statement, easy)
S("Financial Markets, Instruments & Fintech", "easy", "With reference to participatory notes (P-notes), consider the following statements:",
  "पार्टिसिपेटरी नोट्स (पी-नोट्स) के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["They are issued abroad by registered foreign portfolio investors to investors who want exposure to Indian securities without registering in India.",
   "SEBI requires the issuers to know who the beneficial owners of the notes are.",
   "They are issued by the Reserve Bank of India to foreign central banks."],
  ["इन्हें पंजीकृत विदेशी पोर्टफ़ोलियो निवेशक विदेश में उन निवेशकों को जारी करते हैं जो भारत में पंजीकरण के बिना भारतीय प्रतिभूतियों में निवेश चाहते हैं।",
   "सेबी जारीकर्ताओं से अपेक्षा करता है कि वे नोटों के लाभार्थी स्वामियों को जानें।",
   "इन्हें भारतीय रिज़र्व बैंक विदेशी केंद्रीय बैंकों को जारी करता है।"],
  C3, 1,
  "Statements 1 and 2 are correct. P-notes are offshore derivative instruments: a registered foreign portfolio investor buys Indian shares or bonds and issues notes abroad whose value tracks them, so the holder gets the economic exposure without registering with SEBI. Because this anonymity was feared as a route for round-tripping -- Indian money returning disguised as foreign investment -- SEBI has tightened the rules: issuers must know the beneficial owners, report positions, and may not issue them to Indian residents or with derivatives as the underlying. "
  "Statement 3 is wrong: P-notes are private market instruments, issued by FPIs; the RBI issues no such notes.",
  "कथन 1 और 2 सही हैं। पी-नोट्स अपतटीय व्युत्पन्न उपकरण हैं: एक पंजीकृत विदेशी पोर्टफ़ोलियो निवेशक भारतीय शेयर या बॉन्ड ख़रीदता है और विदेश में ऐसे नोट जारी करता है जिनका मूल्य उनके साथ चलता है, जिससे धारक सेबी में पंजीकरण के बिना आर्थिक लाभ पाता है। चूँकि इस गुमनामी को राउंड-ट्रिपिंग -- विदेशी निवेश के वेश में भारतीय धन की वापसी -- का मार्ग माना गया, सेबी ने नियम कड़े किए: जारीकर्ताओं को लाभार्थी स्वामियों को जानना, स्थितियों की सूचना देना होता है, और वे इन्हें भारतीय निवासियों को या व्युत्पन्न को आधार बनाकर जारी नहीं कर सकते। "
  "कथन 3 ग़लत है: पी-नोट्स विदेशी पोर्टफ़ोलियो निवेशकों द्वारा जारी निजी बाज़ार उपकरण हैं; आरबीआई ऐसे कोई नोट जारी नहीं करता।",
  "Securities and Exchange Board of India (Foreign Portfolio Investors) Regulations, 2019, regulation 21 (offshore derivative instruments); SEBI circulars on ODIs.",
  "l4-s01-eco-p-notes-odi-fpi-beneficial-owner", craft="recall")

# ---------------------------------------------------------------- Financial Markets, Instruments & Fintech (statement, hard)
S("Financial Markets, Instruments & Fintech", "hard", "With reference to unconventional monetary policy, consider the following statements:",
  "अपरंपरागत मौद्रिक नीति के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Quantitative easing works mainly by lowering the short-term policy rate, which is its main target.",
   "Under quantitative tightening, a central bank always sells bonds outright in the market.",
   "The Bank of Japan has never set a negative policy interest rate."],
  ["मात्रात्मक सहजता मुख्यतः अल्पकालिक नीतिगत दर को घटाकर काम करती है, जो इसका मुख्य लक्ष्य है।",
   "मात्रात्मक कसाव में केंद्रीय बैंक सदा बाज़ार में बॉन्ड सीधे बेचता है।",
   "बैंक ऑफ़ जापान ने कभी ऋणात्मक नीतिगत ब्याज दर तय नहीं की।"],
  C3, 3,
  "None of the statements is correct. Statement 1 is wrong: quantitative easing is used precisely when the short-term rate is already near zero and cannot be cut much further; the central bank buys long-term government and other bonds with newly created reserves to push down long-term yields and term premiums and to ease financial conditions. Statement 2 is wrong: quantitative tightening shrinks the central bank's balance sheet mostly passively, by not reinvesting the proceeds of bonds as they mature, though some central banks have also sold bonds actively. "
  "Statement 3 is wrong: the Bank of Japan kept a slightly negative policy rate from 2016 to 2024, as did the European Central Bank from 2014 to 2022 and the Swiss and Danish central banks -- charging banks for holding reserves to push them to lend. India has never used these tools; its policy has worked through the repo rate and liquidity operations.",
  "कोई भी कथन सही नहीं है। कथन 1 ग़लत है: मात्रात्मक सहजता ठीक तभी अपनाई जाती है जब अल्पकालिक दर पहले से शून्य के निकट हो और उसे और नहीं घटाया जा सके; केंद्रीय बैंक नए सृजित आरक्षित धन से दीर्घकालिक सरकारी और अन्य बॉन्ड ख़रीदता है ताकि दीर्घकालिक प्रतिफल और टर्म प्रीमियम घटें और वित्तीय दशाएँ सहज हों। कथन 2 ग़लत है: मात्रात्मक कसाव केंद्रीय बैंक के तुलन-पत्र को मुख्यतः निष्क्रिय रूप से घटाता है, परिपक्व होते बॉन्डों की राशि पुनर्निवेश न करके, यद्यपि कुछ केंद्रीय बैंकों ने सक्रिय रूप से बॉन्ड बेचे भी हैं। "
  "कथन 3 ग़लत है: बैंक ऑफ़ जापान ने 2016 से 2024 तक थोड़ी ऋणात्मक नीतिगत दर रखी, जैसा यूरोपीय केंद्रीय बैंक ने 2014 से 2022 तक और स्विस तथा डेनिश केंद्रीय बैंकों ने किया -- बैंकों से आरक्षित धन रखने का शुल्क लेकर उन्हें ऋण देने को प्रेरित करना। भारत ने इन उपकरणों का कभी उपयोग नहीं किया; उसकी नीति रेपो दर और तरलता क्रियाओं से काम करती रही है।",
  "Bank of Japan, monetary policy statements (January 2016, March 2024); European Central Bank, deposit facility rate history; Reserve Bank of India, Monetary Policy Framework.",
  "l4-s01-eco-qe-qt-negative-rates-boj", craft="inference")

# ---------------------------------------------------------------- Financial Markets, Instruments & Fintech (statement, medium)
S("Financial Markets, Instruments & Fintech", "medium", "With reference to SEBI's framework for algorithmic trading by retail investors, consider the following statements:",
  "खुदरा निवेशकों द्वारा एल्गोरिदमिक ट्रेडिंग के लिए सेबी के ढाँचे के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Retail investors may use algorithms only through stock brokers, who act as principals for the algorithms they offer.",
   "Algorithm providers must be empanelled with a stock exchange.",
   "An algorithm that places orders above a set number per second must be registered with the exchange and carry a unique identifier."],
  ["खुदरा निवेशक एल्गोरिदम का उपयोग केवल स्टॉक ब्रोकरों के माध्यम से कर सकते हैं, जो अपने द्वारा प्रस्तुत एल्गोरिदम के लिए प्रधान के रूप में कार्य करते हैं।",
   "एल्गोरिदम प्रदाताओं का किसी स्टॉक एक्सचेंज में सूचीबद्ध (पैनल में) होना आवश्यक है।",
   "प्रति सेकंड एक तय संख्या से अधिक ऑर्डर देने वाले एल्गोरिदम का एक्सचेंज में पंजीकरण और विशिष्ट पहचानकर्ता होना आवश्यक है।"],
  C3, 2,
  "All three statements are correct. Until 2025, retail investors could use automated strategies through broker APIs in a grey zone, often sold by unregulated vendors promising easy profits. SEBI's framework of February 2025, in force from October 2025, brought them inside the regulated chain: the broker is the principal and answerable for every algorithm it allows, algorithm providers act as its agents and must be empanelled with the exchanges, and every algorithmic order is tagged so that it can be traced. "
  "Strategies placing more than a threshold of orders per second (ten, under the exchanges' rules) must be registered and given a unique ID, while slower ones carry a generic tag. The aim is to allow innovation while protecting retail investors and the market from runaway or manipulative algorithms.",
  "तीनों कथन सही हैं। 2025 तक खुदरा निवेशक ब्रोकर एपीआई के माध्यम से एक धूसर क्षेत्र में स्वचालित रणनीतियों का उपयोग कर सकते थे, जो प्रायः आसान लाभ का वादा करने वाले अविनियमित विक्रेता बेचते थे। फ़रवरी 2025 के और अक्टूबर 2025 से प्रवृत्त सेबी के ढाँचे ने उन्हें विनियमित शृंखला के भीतर ला दिया: ब्रोकर प्रधान है और अपने द्वारा अनुमत हर एल्गोरिदम के लिए उत्तरदायी है, एल्गोरिदम प्रदाता उसके अभिकर्ता हैं और उनका एक्सचेंजों में सूचीबद्ध होना आवश्यक है, और हर एल्गोरिदमिक ऑर्डर पर ऐसा चिह्न होता है जिससे उसका पता लगाया जा सके। "
  "प्रति सेकंड ऑर्डरों की एक सीमा (एक्सचेंजों के नियमों में दस) से अधिक ऑर्डर देने वाली रणनीतियों का पंजीकरण और विशिष्ट पहचान आवश्यक है, जबकि धीमी रणनीतियाँ सामान्य चिह्न रखती हैं। उद्देश्य नवाचार की अनुमति देते हुए खुदरा निवेशकों और बाज़ार को अनियंत्रित या हेरफेर करने वाले एल्गोरिदम से बचाना है।",
  "SEBI circular 'Safer participation of retail investors in algorithmic trading' (4 February 2025; timeline extended to 1 October 2025); National Stock Exchange circulars on empanelment of algo providers (2025).",
  "l4-s01-eco-retail-algo-broker-principal-empanelled-ops", craft="precision")

# ---------------------------------------------------------------- Industry, Infrastructure, Energy & Services (MCQ, medium)
M("Industry, Infrastructure, Energy & Services", "medium",
  "Under India's Foreign Trade Policy, an Export Oriented Unit (EOU) is required to",
  "भारत की विदेश व्यापार नीति के अंतर्गत निर्यातोन्मुख इकाई (ईओयू) के लिए आवश्यक है कि वह",
  ["export its entire production, with no sales in the domestic market",
   "be located inside a Special Economic Zone notified under the SEZ Act",
   "be a net earner of foreign exchange over a block of years",
   "be majority-owned by a foreign company or investor"],
  ["अपना समस्त उत्पादन निर्यात करे, घरेलू बाज़ार में कोई बिक्री न हो",
   "सेज़ अधिनियम के अंतर्गत अधिसूचित विशेष आर्थिक क्षेत्र के भीतर स्थित हो",
   "वर्षों की एक अवधि में विदेशी मुद्रा का शुद्ध अर्जक हो",
   "किसी विदेशी कंपनी या निवेशक के बहुमत स्वामित्व में हो"],
  2,
  "The EOU scheme, begun in 1981, lets a unit committed to exporting import and procure inputs duty-free, provided it achieves positive net foreign exchange earnings -- exports worth more than the foreign exchange it uses -- over a block of five years. The obligation is net, not total: an EOU may sell part of its output in the domestic tariff area on payment of duties, within limits. "
  "Unlike an SEZ unit, an EOU can be set up anywhere in the country, which suits units tied to raw materials, farms or skilled labour; ownership may be Indian or foreign. EOUs, SEZs and duty remission schemes all aim to let exporters compete at world prices without bearing domestic taxes on inputs.",
  "1981 में आरंभ ईओयू योजना निर्यात के प्रति प्रतिबद्ध इकाई को शुल्क-मुक्त आदान आयात और प्राप्त करने देती है, बशर्ते वह पाँच वर्षों की अवधि में सकारात्मक शुद्ध विदेशी मुद्रा अर्जन करे -- उपयोग की गई विदेशी मुद्रा से अधिक मूल्य का निर्यात। दायित्व शुद्ध है, कुल नहीं: ईओयू शुल्क चुकाकर अपने उत्पादन का कुछ भाग, सीमाओं के भीतर, घरेलू टैरिफ़ क्षेत्र में बेच सकती है। "
  "सेज़ इकाई के विपरीत ईओयू देश में कहीं भी स्थापित हो सकती है, जो कच्चे माल, खेतों या कुशल श्रम से जुड़ी इकाइयों के लिए उपयुक्त है; स्वामित्व भारतीय या विदेशी हो सकता है। ईओयू, सेज़ और शुल्क-छूट योजनाएँ, सबका उद्देश्य निर्यातकों को आदानों पर घरेलू करों का बोझ उठाए बिना विश्व क़ीमतों पर प्रतिस्पर्धा करने देना है।",
  "Directorate General of Foreign Trade, Foreign Trade Policy 2023, Chapter 6 (EOUs, EHTPs, STPs) and Handbook of Procedures.",
  "l4-s01-eco-eou-positive-nfe-dta-anywhere", pos=2, craft="application")

# ---------------------------------------------------------------- Industry, Infrastructure, Energy & Services (statement, easy)
S("Industry, Infrastructure, Energy & Services", "easy", "With reference to the Prime Minister's Employment Generation Programme (PMEGP), consider the following statements:",
  "प्रधानमंत्री रोज़गार सृजन कार्यक्रम (पीएमईजीपी) के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is a credit-linked subsidy programme for setting up new micro enterprises.",
   "NABARD is its nodal implementing agency at the national level.",
   "It supports manufacturing units only, not service enterprises."],
  ["यह नए सूक्ष्म उद्यम स्थापित करने के लिए ऋण-संबद्ध सब्सिडी कार्यक्रम है।",
   "नाबार्ड राष्ट्रीय स्तर पर इसकी नोडल क्रियान्वयन एजेंसी है।",
   "यह केवल विनिर्माण इकाइयों का समर्थन करता है, सेवा उद्यमों का नहीं।"],
  C3, 0,
  "Only statement 1 is correct. PMEGP, formed in 2008 by merging two older self-employment schemes, gives a margin-money subsidy of 15 to 35 per cent of the project cost -- higher in rural areas and for women, Scheduled Castes and Tribes and other special categories -- on bank loans for new micro enterprises, so that first-time entrepreneurs can start with limited capital. "
  "Statement 2 is wrong: the Khadi and Village Industries Commission, under the Ministry of MSME, is the nodal agency, working with State KVIBs and District Industries Centres. Statement 3 is wrong: both manufacturing and service units are eligible, with a higher project-cost ceiling for manufacturing.",
  "केवल कथन 1 सही है। 2008 में दो पुरानी स्वरोज़गार योजनाओं के विलय से बना पीएमईजीपी नए सूक्ष्म उद्यमों के बैंक ऋणों पर परियोजना लागत की 15 से 35 प्रतिशत मार्जिन-मनी सब्सिडी देता है -- ग्रामीण क्षेत्रों में और महिलाओं, अनुसूचित जातियों-जनजातियों तथा अन्य विशेष श्रेणियों के लिए अधिक -- ताकि पहली बार के उद्यमी सीमित पूँजी से आरंभ कर सकें। "
  "कथन 2 ग़लत है: सूक्ष्म, लघु और मध्यम उद्यम मंत्रालय के अधीन खादी और ग्रामोद्योग आयोग नोडल एजेंसी है, जो राज्य खादी बोर्डों और ज़िला उद्योग केंद्रों के साथ काम करता है। कथन 3 ग़लत है: विनिर्माण और सेवा, दोनों इकाइयाँ पात्र हैं, विनिर्माण के लिए परियोजना लागत की सीमा अधिक है।",
  "Ministry of MSME and KVIC, PMEGP guidelines.",
  "l4-s01-eco-pmegp-credit-linked-kvic-services-eligible", craft="recall")

# ---------------------------------------------------------------- Industry, Infrastructure, Energy & Services (statement, medium)
S("Industry, Infrastructure, Energy & Services", "medium", "With reference to India's export promotion schemes, consider the following statements:",
  "भारत की निर्यात संवर्धन योजनाओं के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Under Advance Authorisation, an exporter can import duty-free inputs only after it has completed its exports.",
   "The RoSCTL scheme refunds embedded taxes on exports of electronic goods.",
   "The 'Districts as Export Hubs' initiative is run by the Reserve Bank of India."],
  ["अग्रिम प्राधिकार के अंतर्गत निर्यातक अपने निर्यात पूरे करने के बाद ही शुल्क-मुक्त आदान आयात कर सकता है।",
   "आरओएससीटीएल योजना इलेक्ट्रॉनिक वस्तुओं के निर्यात पर अंतर्निहित करों की वापसी करती है।",
   "‘ज़िले निर्यात केंद्र के रूप में’ पहल भारतीय रिज़र्व बैंक चलाता है।"],
  C3, 3,
  "None of the statements is correct. Statement 1 is wrong: Advance Authorisation is issued in advance -- it lets an exporter import, without paying customs duty, the inputs that will be physically incorporated in the goods to be exported, against an obligation to export within a set period; the 'advance' is the point, since the exporter is spared from locking up working capital in duties that would later be refunded. "
  "Statement 2 is wrong: the Rebate of State and Central Taxes and Levies covers exports of apparel and made-ups, refunding taxes such as those on fuel and electricity used in production that are not credited anywhere else; other goods are covered by the RoDTEP scheme. Statement 3 is wrong: the initiative is run by the Directorate General of Foreign Trade and the Commerce Ministry with the States, each district identifying products with export potential and preparing an export action plan. All of these rest on the principle that goods, not taxes, should be exported.",
  "कोई भी कथन सही नहीं है। कथन 1 ग़लत है: अग्रिम प्राधिकार पहले ही जारी होता है -- यह निर्यातक को उन आदानों को सीमा शुल्क चुकाए बिना आयात करने देता है जो निर्यात की जाने वाली वस्तुओं में भौतिक रूप से समाहित होंगे, तय अवधि में निर्यात करने के दायित्व के बदले; ‘अग्रिम’ ही इसका सार है, क्योंकि निर्यातक बाद में वापस होने वाले शुल्कों में कार्यशील पूँजी फँसाने से बच जाता है। "
  "कथन 2 ग़लत है: राज्य और केंद्रीय करों और उद्ग्रहणों की छूट (आरओएससीटीएल) परिधानों और बने-बनाए वस्त्रों के निर्यात को कवर करती है, और उत्पादन में प्रयुक्त ईंधन तथा बिजली पर लगे ऐसे करों की वापसी करती है जिनका कहीं और क्रेडिट नहीं मिलता; अन्य वस्तुएँ आरओडीटीईपी योजना में आती हैं। कथन 3 ग़लत है: यह पहल विदेश व्यापार महानिदेशालय और वाणिज्य मंत्रालय राज्यों के साथ चलाते हैं, जिसमें हर ज़िला निर्यात क्षमता वाले उत्पाद पहचानता है और निर्यात कार्य-योजना बनाता है। ये सब इस सिद्धांत पर टिके हैं कि वस्तुएँ निर्यात हों, कर नहीं।",
  "Directorate General of Foreign Trade, Foreign Trade Policy 2023, Chapter 4 (Duty exemption schemes) and Chapter 3 (Districts as Export Hubs); notifications on RoSCTL and RoDTEP.",
  "l4-s01-eco-advance-authorisation-rosctl-district-export-hubs", craft="precision")

# ---------------------------------------------------------------- Macro Concepts, National Income & Inflation (AR, hard)
A("Macro Concepts, National Income & Inflation", "hard",
  "For very poor households, a rise in the price of their main staple food can increase the quantity of it that they buy.",
  "अत्यंत ग़रीब परिवारों के लिए उनके मुख्य खाद्यान्न की क़ीमत बढ़ने से उनके द्वारा ख़रीदी जाने वाली उसकी मात्रा बढ़ सकती है।",
  "When a staple takes up a large share of a household's budget, the fall in real income caused by its price rise can force the household to give up costlier foods and buy more of the staple.",
  "जब कोई मुख्य खाद्यान्न परिवार के बजट का बड़ा भाग लेता है, तो उसकी क़ीमत बढ़ने से वास्तविक आय में आई गिरावट परिवार को महँगे खाद्य छोड़कर मुख्य खाद्यान्न अधिक ख़रीदने को विवश कर सकती है।",
  0,
  "Both statements are correct, and Statement II explains Statement I. This is the case of a 'Giffen good'. A price rise has two effects: the substitution effect always pushes a buyer away from the dearer good, but the income effect -- the household is now poorer -- pushes it towards cheaper calories. For an inferior good that takes most of a very poor household's budget, the income effect can outweigh the substitution effect, so demand rises with price; a well-known field study found such behaviour for rice among poor households in China's Hunan province. "
  "A Veblen good, by contrast, is a luxury bought more when its price is higher because the price itself signals status. The point matters for food policy: price rises in staples hit the poorest hardest, which is one reason for subsidised grain under the food security law.",
  "दोनों कथन सही हैं, और कथन II कथन I की व्याख्या करता है। यह ‘गिफ़ेन वस्तु’ का उदाहरण है। क़ीमत बढ़ने के दो प्रभाव होते हैं: प्रतिस्थापन प्रभाव क्रेता को सदा महँगी वस्तु से दूर ले जाता है, पर आय प्रभाव -- परिवार अब ग़रीब हो गया -- उसे सस्ती कैलोरी की ओर ले जाता है। किसी घटिया वस्तु के लिए, जो अत्यंत ग़रीब परिवार के बजट का अधिकांश लेती है, आय प्रभाव प्रतिस्थापन प्रभाव से अधिक हो सकता है, इसलिए क़ीमत के साथ माँग बढ़ती है; एक प्रसिद्ध क्षेत्र-अध्ययन ने चीन के हुनान प्रांत के ग़रीब परिवारों में चावल के लिए ऐसा व्यवहार पाया। "
  "इसके विपरीत वेब्लेन वस्तु एक विलासिता है जो क़ीमत अधिक होने पर अधिक ख़रीदी जाती है क्योंकि क़ीमत स्वयं प्रतिष्ठा का संकेत है। यह बात खाद्य नीति के लिए महत्त्वपूर्ण है: मुख्य खाद्यान्नों की क़ीमतें बढ़ने का सबसे भारी असर सबसे ग़रीबों पर पड़ता है, जो खाद्य सुरक्षा क़ानून के अंतर्गत सब्सिडी वाले अनाज का एक कारण है।",
  "NCERT, Introductory Microeconomics (Class XII), Chapter 2 (Theory of Consumer Behaviour); Jensen, R. and Miller, N., 'Giffen Behavior and Subsistence Consumption', American Economic Review 98(4) (2008).",
  "l4-s01-eco-giffen-good-income-effect-staple", craft="inference")

# ---------------------------------------------------------------- Money, Banking & Monetary Policy (AR, easy)
A("Money, Banking & Monetary Policy", "easy",
  "A fall in the velocity of money makes a given increase in the money supply raise nominal GDP by more than before.",
  "मुद्रा के वेग में गिरावट मुद्रा आपूर्ति में दी गई वृद्धि से नाममात्र जीडीपी को पहले से अधिक बढ़ाती है।",
  "The velocity of money is the number of times a unit of money is spent on final goods and services in a period, so that the money stock multiplied by velocity equals nominal GDP.",
  "मुद्रा का वेग वह संख्या है जितनी बार किसी अवधि में मुद्रा की एक इकाई अंतिम वस्तुओं और सेवाओं पर ख़र्च होती है, जिससे मुद्रा भंडार गुणा वेग नाममात्र जीडीपी के बराबर होता है।",
  3,
  "Statement I is incorrect, but Statement II is correct. The identity MV = PY says that the money stock times its velocity equals nominal GDP (prices times real output). If velocity falls -- because people and firms hold on to money, as in uncertain times or when interest rates are low -- the same increase in money supports a smaller rise in nominal spending, not a larger one. That is why a money-supply target can mislead when velocity is unstable, and one reason why central banks, India's included, moved to targeting inflation directly. "
  "Velocity in India has also fallen over decades as the economy has become more monetised and financial deposits have grown.",
  "कथन I ग़लत है, पर कथन II सही है। तादात्म्य MV = PY कहता है कि मुद्रा भंडार गुणा उसका वेग नाममात्र जीडीपी (क़ीमतें गुणा वास्तविक उत्पादन) के बराबर है। यदि वेग घटता है -- क्योंकि लोग और फ़र्में मुद्रा रोककर रखते हैं, जैसे अनिश्चित समय में या ब्याज दरें कम होने पर -- तो मुद्रा में वही वृद्धि नाममात्र व्यय में कम वृद्धि को सहारा देती है, अधिक को नहीं। इसीलिए वेग अस्थिर होने पर मुद्रा-आपूर्ति का लक्ष्य भ्रामक हो सकता है, और यही एक कारण है कि भारत सहित केंद्रीय बैंक सीधे मुद्रास्फीति को लक्षित करने लगे। "
  "भारत में भी दशकों में वेग घटा है, क्योंकि अर्थव्यवस्था अधिक मौद्रीकृत हुई है और वित्तीय जमाएँ बढ़ी हैं।",
  "NCERT, Introductory Macroeconomics (Class XII), Chapter 3 (Money and Banking); Reserve Bank of India, Report of the Expert Committee to Revise and Strengthen the Monetary Policy Framework (2014).",
  "l4-s01-eco-velocity-of-money-mv-py-fall", craft="inference")

# ---------------------------------------------------------------- Money, Banking & Monetary Policy (statement, medium)
S("Money, Banking & Monetary Policy", "medium", "With reference to the Payments Infrastructure Development Fund (PIDF) of the RBI, consider the following statements:",
  "आरबीआई के भुगतान अवसंरचना विकास कोष (पीआईडीएफ़) के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["It subsidises the deployment of payment acceptance devices, such as point-of-sale terminals and QR codes, in smaller towns and the north-east.",
   "It is funded by the RBI together with card networks and card-issuing banks.",
   "It is meant mainly for metropolitan cities, where card use is highest."],
  ["यह छोटे नगरों और उत्तर-पूर्व में पॉइंट-ऑफ़-सेल टर्मिनल और क्यूआर कोड जैसे भुगतान स्वीकृति उपकरणों की स्थापना पर सब्सिडी देता है।",
   "इसका वित्तपोषण आरबीआई कार्ड नेटवर्कों और कार्ड जारी करने वाले बैंकों के साथ मिलकर करता है।",
   "यह मुख्यतः महानगरों के लिए है, जहाँ कार्ड का उपयोग सबसे अधिक है।"],
  C3, 1,
  "Statements 1 and 2 are correct. The fund, set up in 2021, subsidises acquiring banks and payment firms for installing physical and digital acceptance devices -- card machines and QR codes -- in tier-3 to tier-6 centres, the north-eastern States and Jammu and Kashmir and Ladakh, and was later extended to street vendors under PM SVANidhi. The RBI put in the initial contribution, with card networks and card-issuing banks contributing as well. "
  "Statement 3 is wrong: the fund exists because acceptance infrastructure was concentrated in the metros; a merchant in a small town has little reason to pay for devices when few customers use digital payments, and few customers use them when few merchants accept them -- a coordination problem the subsidy is meant to break.",
  "कथन 1 और 2 सही हैं। 2021 में बना यह कोष भौतिक और डिजिटल स्वीकृति उपकरण -- कार्ड मशीनें और क्यूआर कोड -- टियर-3 से टियर-6 केंद्रों, उत्तर-पूर्वी राज्यों और जम्मू-कश्मीर तथा लद्दाख में लगाने के लिए अधिग्रहणकर्ता बैंकों और भुगतान कंपनियों को सब्सिडी देता है, और बाद में इसे पीएम स्वनिधि के अंतर्गत रेहड़ी-पटरी विक्रेताओं तक बढ़ाया गया। आरबीआई ने प्रारंभिक योगदान दिया, और कार्ड नेटवर्कों तथा कार्ड जारी करने वाले बैंकों ने भी योगदान दिया। "
  "कथन 3 ग़लत है: कोष इसलिए है कि स्वीकृति अवसंरचना महानगरों में केंद्रित थी; छोटे नगर के व्यापारी के पास उपकरणों पर ख़र्च करने का कम कारण होता है जब कम ग्राहक डिजिटल भुगतान करते हैं, और कम ग्राहक उनका उपयोग करते हैं जब कम व्यापारी उन्हें स्वीकार करते हैं -- यही समन्वय की समस्या है जिसे सब्सिडी तोड़ना चाहती है।",
  "Reserve Bank of India, Payments Infrastructure Development Fund scheme (January 2021) and extensions.",
  "l4-s01-eco-pidf-acceptance-devices-tier-3-6-ne", craft="linkage")

# ---------------------------------------------------------------- Taxation & Fiscal Federalism (pairs, hard)
P("Taxation & Fiscal Federalism", "hard", "Consider the following pairs of terms used in taxation and their meaning:",
  "कराधान में प्रयुक्त शब्दों और उनके अर्थ के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Presumptive taxation : Taxing small businesses on a deemed share of their turnover instead of their computed profit",
   "Base erosion and profit shifting : The shifting of taxable profits by multinational firms to low-tax jurisdictions",
   "Tonnage tax : Taxing shipping companies on the net tonnage of their ships rather than on their actual profits",
   "Thin capitalisation rule : A limit on deducting interest paid on debt from associated enterprises abroad"],
  ["अनुमानित कराधान : छोटे व्यवसायों पर उनके गणना किए लाभ के बजाय उनके कारोबार के मान्य अंश पर कर लगाना",
   "आधार क्षरण और लाभ स्थानांतरण : बहुराष्ट्रीय कंपनियों द्वारा कर-योग्य लाभों को कम कर वाले क्षेत्रों में ले जाना",
   "टनभार कर : नौवहन कंपनियों पर उनके वास्तविक लाभ के बजाय उनके जहाज़ों के शुद्ध टनभार पर कर लगाना",
   "पतला पूँजीकरण नियम : विदेश के संबद्ध उद्यमों से लिए ऋण पर चुकाए ब्याज की कटौती पर सीमा"],
  3,
  "All four pairs are correct. Presumptive taxation, under sections 44AD and 44ADA of the Income-tax Act, lets small businesses and professionals declare income at a set percentage of turnover or receipts without keeping detailed accounts, cutting compliance costs and widening the base. Base erosion and profit shifting is the OECD/G20 term for multinationals' use of transfer pricing and tax havens; the response includes the 15 per cent global minimum tax. "
  "India's tonnage tax scheme (since 2004) lets shipping companies pay tax on a notional income worked out from the tonnage of their fleet, as most maritime countries do, so that Indian-flag ships are not at a disadvantage. The thin capitalisation rule (section 94B, from 2017) caps the deduction of interest paid to associated enterprises at 30 per cent of earnings before interest, tax, depreciation and amortisation, so that a multinational cannot load its Indian arm with debt to shift profits out as interest -- one of the BEPS recommendations put into law.",
  "चारों युग्म सही हैं। आयकर अधिनियम की धारा 44एडी और 44एडीए के अंतर्गत अनुमानित कराधान छोटे व्यवसायों और पेशेवरों को विस्तृत लेखा रखे बिना कारोबार या प्राप्तियों के तय प्रतिशत पर आय घोषित करने देता है, जिससे अनुपालन लागत घटती है और आधार बढ़ता है। आधार क्षरण और लाभ स्थानांतरण बहुराष्ट्रीय कंपनियों द्वारा अंतरण मूल्य-निर्धारण और कर-स्वर्गों के उपयोग के लिए ओईसीडी/जी20 का शब्द है; इसके उत्तर में 15 प्रतिशत का वैश्विक न्यूनतम कर है। "
  "भारत की टनभार कर योजना (2004 से) नौवहन कंपनियों को उनके बेड़े के टनभार से निकाली गई काल्पनिक आय पर कर चुकाने देती है, जैसा अधिकांश समुद्री देश करते हैं, ताकि भारतीय ध्वज वाले जहाज़ नुक़सान में न रहें। पतला पूँजीकरण नियम (धारा 94बी, 2017 से) संबद्ध उद्यमों को चुकाए ब्याज की कटौती को ब्याज, कर, मूल्यह्रास और परिशोधन से पहले की कमाई के 30 प्रतिशत तक सीमित करता है, ताकि कोई बहुराष्ट्रीय कंपनी अपनी भारतीय शाखा पर ऋण लादकर लाभ को ब्याज के रूप में बाहर न ले जा सके -- यह बीईपीएस की संस्तुतियों में से एक है जिसे विधि में लाया गया।",
  "Income-tax Act, 1961, sections 44AD, 44ADA, 94B and Chapter XII-G (tonnage tax); OECD/G20 Inclusive Framework on BEPS, Action 4.",
  "l4-s01-eco-presumptive-beps-tonnage-thin-cap", craft="precision")

write("gs_l4_s01_e.sql")
