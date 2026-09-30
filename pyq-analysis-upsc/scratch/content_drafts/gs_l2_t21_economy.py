# -*- coding: utf-8 -*-
"""Level 2 · Test 21 (GS Comprehensive Revision, full syllabus) -- Economy block (17 of the paper's 84 static rows).
  Money & Banking 2, Macro 1, Taxation 1, Inclusive Growth 1, External Sector 2, Financial Markets 4, Agriculture 2,
  Budget 1, Industry & Services 3.
  Cells: medium statement 6, easy statement 2, hard statement 2, medium MCQ 2, easy MCQ 1, medium Statement-I/II 2,
    easy Statement-I/II 1, hard pairs 1.
Tests 15-18 hold the monetary-policy, banking, market, external, budget, tax, farm, industry and welfare facts listed
in their headers, and the bank also holds the deflator, Phillips curve, stagflation, Laffer curve, core inflation,
J-curve, Dutch disease, hot money, NEER/REER, Bretton Woods, the IPO terms (book building, anchor, greenshoe), QIP,
rights and bonus issues, Sensex/Nifty, tax expenditure, Ricardian equivalence, dependency ratio, Lakhpati Didi,
industrial delicensing and capacity utilisation -- so none of those is tested here. Checked-clean facts used: PCA,
D-SIBs, shrinkflation, Pigouvian tax, MMR/IMR/NMR, the Triffin dilemma, reserve adequacy, the Social Stock Exchange,
buyback/stock split/sweat equity/India VIX, Bima Sugam, municipal bonds, the 10,000-FPO scheme, WDRA e-NWRs,
crowding-out, Maharatna/Navratna, QCOs and HUID, and e-commerce FDI."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Economy"
MB = "Money, Banking & Monetary Policy"
MC = "Macro Concepts, National Income & Inflation"
FT = "Taxation & Fiscal Federalism"
IG = "Inclusive Growth, Welfare & Demography"
EX = "External Sector & International Institutions"
FM = "Financial Markets, Instruments & Fintech"
AG = "Agriculture & Food Economy"
FB = "Budget, Deficits & Public Debt"
IN = "Industry, Infrastructure, Energy & Services"
RBI = "Reserve Bank of India"
SEBI = "Securities and Exchange Board of India"
NCM = "NCERT Class XII, Introductory Macroeconomics"
IED = "NCERT Class XI, Indian Economic Development"
DPIIT = "Department for Promotion of Industry and Internal Trade"
MOA = "Ministry of Agriculture and Farmers Welfare"

# ================================================================ MONEY & BANKING (2)
S(MB, "medium", "Consider the following statements about the Reserve Bank of India's Prompt Corrective Action (PCA) framework for banks:",
  "बैंकों के लिए भारतीय रिज़र्व बैंक के त्वरित सुधारात्मक कार्रवाई (PCA) ढाँचे के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Under the framework revised in 2021, the indicators tracked are capital, asset quality and leverage.",
   "The framework does not apply to public sector banks.",
   "Payments banks and small finance banks are kept outside the framework."],
  ["2021 में संशोधित ढाँचे के तहत जिन संकेतकों पर नज़र रखी जाती है वे पूँजी, परिसंपत्ति गुणवत्ता और लीवरेज हैं।",
   "यह ढाँचा सार्वजनिक क्षेत्र के बैंकों पर लागू नहीं होता।",
   "पेमेंट्स बैंक और लघु वित्त बैंक इस ढाँचे से बाहर रखे गए हैं।"],
  C3, 1,
  "Statements 1 and 3 are correct. The revised framework, in force from January 2022, watches capital (CRAR and Common Equity Tier 1), asset quality (the net NPA ratio) and leverage (the Tier 1 leverage ratio); profitability, tracked earlier, was dropped. A bank that breaches the thresholds faces graded curbs, for example on dividends, branch expansion and fresh lending. "
  "Statement 2 is wrong: the framework covers all banks operating in India, public sector banks and foreign banks' branches included -- eleven public sector banks were under PCA in 2017-18. Payments banks and small finance banks were taken out of its scope in the 2021 revision, and a separate PCA framework now applies to NBFCs.",
  "कथन 1 और 3 सही हैं। जनवरी 2022 से लागू संशोधित ढाँचा पूँजी (CRAR और कॉमन इक्विटी टियर 1), परिसंपत्ति गुणवत्ता (शुद्ध NPA अनुपात) और लीवरेज (टियर 1 लीवरेज अनुपात) पर नज़र रखता है; पहले देखी जाने वाली लाभप्रदता हटा दी गई। सीमा पार करने वाले बैंक पर चरणबद्ध प्रतिबंध लगते हैं, जैसे लाभांश, शाखा विस्तार और नए ऋण पर। "
  "कथन 2 गलत है: यह ढाँचा भारत में कार्यरत सभी बैंकों पर, सार्वजनिक क्षेत्र के बैंकों और विदेशी बैंकों की शाखाओं सहित, लागू होता है; 2017-18 में सार्वजनिक क्षेत्र के ग्यारह बैंक PCA के अधीन थे। पेमेंट्स बैंक और लघु वित्त बैंक 2021 के संशोधन में इसके दायरे से बाहर किए गए, और NBFCs के लिए अब अलग PCA ढाँचा है।",
  f"{RBI} -- Prompt Corrective Action Framework for Scheduled Commercial Banks (2021).",
  "mb-pca-framework-banks")

A(MB, "medium",
  "The RBI requires SBI, HDFC Bank and ICICI Bank to hold Common Equity Tier 1 capital above the level required of other banks.",
  "RBI, SBI, HDFC बैंक और ICICI बैंक से अन्य बैंकों से अपेक्षित स्तर से अधिक कॉमन इक्विटी टियर 1 पूँजी रखने की अपेक्षा करता है।",
  "Banks classified as Domestic Systemically Important Banks receive an explicit government guarantee on all their deposits.",
  "घरेलू प्रणालीगत रूप से महत्वपूर्ण बैंक (D-SIB) घोषित बैंकों को उनकी सभी जमाओं पर सरकार की स्पष्ट गारंटी मिलती है।",
  2,
  "Statement-I is correct but Statement-II is incorrect. Under its 2014 framework the RBI names Domestic Systemically Important Banks (D-SIBs) each year on the basis of size, interconnectedness, substitutability and complexity, and places them in buckets that carry an additional CET1 requirement; SBI sits in the highest bucket of the three. "
  "The extra capital is meant to lower the chance and the cost of their failure, precisely because markets may treat them as 'too big to fail'. There is no explicit government guarantee on their deposits; deposit insurance treats every insured bank alike.",
  "कथन-I सही है पर कथन-II गलत है। अपने 2014 के ढाँचे के तहत RBI हर वर्ष आकार, परस्पर जुड़ाव, प्रतिस्थापन-क्षमता और जटिलता के आधार पर घरेलू प्रणालीगत रूप से महत्वपूर्ण बैंकों (D-SIBs) को चिह्नित करता है और उन्हें ऐसे वर्गों (buckets) में रखता है जिनके साथ अतिरिक्त CET1 की शर्त जुड़ी है; तीनों में SBI सबसे ऊँचे वर्ग में है। "
  "अतिरिक्त पूँजी का उद्देश्य उनके विफल होने की आशंका और लागत घटाना है, ठीक इसलिए कि बाज़ार उन्हें 'इतना बड़ा कि डूब न सके' मान सकता है। उनकी जमाओं पर सरकार की कोई स्पष्ट गारंटी नहीं है; जमा बीमा सभी बीमित बैंकों के लिए एक जैसा है।",
  f"{RBI} -- Framework for dealing with Domestic Systemically Important Banks (2014) and the annual D-SIB list.",
  "mb-dsib-additional-cet1")

# ================================================================ MACRO (1)
M(MC, "easy", "The term 'shrinkflation' refers to",
  "'श्रिंकफ़्लेशन' (shrinkflation) शब्द का अर्थ है",
  ["a cut in a product's size or quantity while its price stays the same",
   "a fall in the general price level accompanied by a fall in output",
   "a slowdown in the rate of inflation without any fall in prices",
   "a rise in prices caused mainly by a shrinking supply of money in the economy"],
  ["किसी उत्पाद का आकार या मात्रा घटाना, जबकि उसकी क़ीमत वही रहे",
   "सामान्य क़ीमत स्तर में गिरावट के साथ उत्पादन में भी गिरावट",
   "क़ीमतें घटे बिना मुद्रास्फीति की दर का धीमा होना",
   "मुख्य रूप से अर्थव्यवस्था में मुद्रा आपूर्ति घटने से होने वाली क़ीमत-वृद्धि"],
  0,
  "Shrinkflation is a hidden price rise: a packet of biscuits or chips keeps its price but holds fewer grams, so the price per unit goes up. It matters for measuring inflation, because price indices have to adjust for such changes in quantity. "
  "A slowing rate of inflation with prices still rising is disinflation, a falling price level is deflation, and a shrinking money supply tends to pull prices down, not up.",
  "श्रिंकफ़्लेशन एक छिपी हुई क़ीमत-वृद्धि है: बिस्कुट या चिप्स का पैकेट उसी क़ीमत पर मिलता है पर उसमें कम ग्राम होते हैं, इसलिए प्रति इकाई क़ीमत बढ़ जाती है। मुद्रास्फीति मापने में इसका महत्व है, क्योंकि क़ीमत सूचकांकों को मात्रा के ऐसे बदलावों के अनुसार समायोजन करना पड़ता है। "
  "क़ीमतें बढ़ते रहते हुए मुद्रास्फीति की दर का धीमा होना अवस्फीति (disinflation) है, क़ीमत स्तर का गिरना अपस्फीति (deflation) है, और मुद्रा आपूर्ति घटने से क़ीमतें प्रायः गिरती हैं, बढ़ती नहीं।",
  f"{NCM}; {RBI} -- inflation measurement.",
  "mc-shrinkflation-easy")

# ================================================================ TAXATION (1)
M(FT, "medium", "A 'Pigouvian tax' is best described as a tax that",
  "'पिगूवियन कर' (Pigouvian tax) का सबसे सही वर्णन है, ऐसा कर जो",
  ["makes a producer pay for the harm its activity causes to others",
   "takes a larger share of income from the poor than from the rich",
   "is levied at each stage of production only on the value added",
   "is collected on short-term currency trades to curb speculation"],
  ["उत्पादक से उस हानि की क़ीमत वसूलता है जो उसकी गतिविधि दूसरों को पहुँचाती है",
   "अमीरों की तुलना में ग़रीबों की आय का बड़ा हिस्सा लेता है",
   "उत्पादन के हर चरण पर केवल जोड़े गए मूल्य पर लगता है",
   "सट्टेबाज़ी रोकने के लिए अल्पकालिक मुद्रा सौदों पर लगाया जाता है"],
  0,
  "Named after the economist Arthur Pigou, such a tax is set roughly equal to the external cost of an activity -- pollution, congestion or the health cost of tobacco -- so that the producer or buyer weighs the full cost to society; changing behaviour matters more than the revenue. "
  "A tax that takes a larger share of a poor person's income is regressive, a value-added tax falls on the value added at each stage, and a small levy on currency trades is known as a Tobin tax.",
  "अर्थशास्त्री आर्थर पिगू के नाम पर बना यह कर किसी गतिविधि की बाहरी लागत, जैसे प्रदूषण, भीड़भाड़ या तंबाकू की स्वास्थ्य लागत, के लगभग बराबर रखा जाता है, ताकि उत्पादक या ख़रीदार समाज पर पड़ने वाली पूरी लागत को ध्यान में रखे; इसमें राजस्व से ज़्यादा महत्व व्यवहार बदलने का है। "
  "जो कर ग़रीब की आय का बड़ा हिस्सा ले वह प्रतिगामी (regressive) कर है, मूल्य वर्धित कर हर चरण पर जोड़े गए मूल्य पर लगता है, और मुद्रा सौदों पर छोटे शुल्क को टोबिन कर कहते हैं।",
  f"{NCM} -- Government Budget and the Economy; Economic Survey -- environmental taxation.",
  "ft-pigouvian-tax")

# ================================================================ INCLUSIVE GROWTH (1)
S(IG, "easy", "Consider the following statements about measures of mortality:",
  "मृत्यु-दर के मापों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The maternal mortality ratio is expressed per 1,00,000 live births.",
   "The infant mortality rate counts deaths of children under five years of age per 1,000 live births.",
   "Neonatal mortality covers deaths of babies within the first year of life."],
  ["मातृ मृत्यु अनुपात प्रति 1,00,000 जीवित जन्मों पर व्यक्त किया जाता है।",
   "शिशु मृत्यु दर प्रति 1,000 जीवित जन्मों पर पाँच वर्ष से कम आयु के बच्चों की मृत्यु गिनती है।",
   "नवजात मृत्यु दर जीवन के पहले वर्ष के भीतर शिशुओं की मृत्यु को शामिल करती है।"],
  C3, 0,
  "Only statement 1 is correct. The maternal mortality ratio (MMR) counts women who die from causes related to pregnancy or childbirth per 1,00,000 live births; for India it comes from the Sample Registration System. "
  "The infant mortality rate (IMR) counts deaths before the first birthday per 1,000 live births; deaths before the fifth birthday make up the under-five mortality rate. "
  "The neonatal mortality rate covers only the first 28 days, when most infant deaths now occur. The SDG targets for 2030 are an MMR below 70 and a neonatal mortality rate of 12 or less.",
  "केवल कथन 1 सही है। मातृ मृत्यु अनुपात (MMR) प्रति 1,00,000 जीवित जन्मों पर गर्भावस्था या प्रसव से जुड़े कारणों से मरने वाली महिलाओं की गिनती करता है; भारत के लिए यह नमूना पंजीकरण प्रणाली (SRS) से मिलता है। "
  "शिशु मृत्यु दर (IMR) प्रति 1,000 जीवित जन्मों पर पहले जन्मदिन से पहले होने वाली मृत्यु गिनती है; पाँचवें जन्मदिन से पहले की मृत्यु से पाँच वर्ष से कम आयु की मृत्यु दर बनती है। "
  "नवजात मृत्यु दर केवल पहले 28 दिनों को शामिल करती है, जिनमें अब अधिकांश शिशु मृत्यु होती हैं। 2030 के लिए SDG लक्ष्य हैं: MMR 70 से कम और नवजात मृत्यु दर 12 या उससे कम।",
  "Office of the Registrar General of India -- Sample Registration System; NITI Aayog -- SDG India targets.",
  "ig-mortality-measures-mmr-imr-nmr")

# ================================================================ EXTERNAL SECTOR (2)
S(EX, "hard", "Consider the following statements about the 'Triffin dilemma':",
  "'ट्रिफ़िन दुविधा' (Triffin dilemma) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It arises when a national currency serves as the world's main reserve currency, since supplying the world with reserves requires that country to run persistent external deficits that can erode confidence in the currency.",
   "It was first described in the context of the British pound under the classical gold standard of the nineteenth century.",
   "The Chinese renminbi is now the largest component of the world's official foreign-exchange reserves."],
  ["यह तब उत्पन्न होती है जब कोई राष्ट्रीय मुद्रा दुनिया की मुख्य आरक्षित मुद्रा बनती है, क्योंकि दुनिया को भंडार उपलब्ध कराने के लिए उस देश को लगातार बाह्य घाटा चलाना पड़ता है, जो उस मुद्रा में भरोसा घटा सकता है।",
   "इसका वर्णन पहली बार उन्नीसवीं सदी के शास्त्रीय स्वर्ण मानक के तहत ब्रिटिश पाउंड के संदर्भ में किया गया था।",
   "चीनी रेनमिनबी आज दुनिया के आधिकारिक विदेशी मुद्रा भंडार का सबसे बड़ा घटक है।"],
  C3, 0,
  "Only statement 1 is correct. The economist Robert Triffin warned in 1960 that under the Bretton Woods system the world needed ever more dollars as reserves, which the United States could supply only by running deficits -- yet mounting deficits would undermine faith in the dollar's convertibility into gold. The strain helped end that system in the early 1970s, and the dilemma is still debated for today's dollar-based system. "
  "Statement 3 is wrong: the US dollar still makes up well over half of the reserves reported to the IMF, followed by the euro; the renminbi's share is only a few per cent.",
  "केवल कथन 1 सही है। अर्थशास्त्री रॉबर्ट ट्रिफ़िन ने 1960 में चेताया कि ब्रेटन वुड्स व्यवस्था में दुनिया को भंडार के रूप में लगातार अधिक डॉलर चाहिए थे, जिन्हें अमेरिका केवल घाटा चलाकर ही दे सकता था, पर बढ़ता घाटा डॉलर की सोने में परिवर्तनीयता पर भरोसा कमज़ोर करता। इसी खिंचाव ने 1970 के दशक की शुरुआत में उस व्यवस्था के अंत में भूमिका निभाई, और आज की डॉलर-आधारित व्यवस्था के लिए भी इस दुविधा पर बहस होती है। "
  "कथन 3 गलत है: IMF को बताए गए भंडार में आज भी अमेरिकी डॉलर का हिस्सा आधे से काफ़ी अधिक है, उसके बाद यूरो आता है; रेनमिनबी का हिस्सा केवल कुछ प्रतिशत है।",
  "International Monetary Fund -- Currency Composition of Official Foreign Exchange Reserves (COFER); Robert Triffin, Gold and the Dollar Crisis (1960).",
  "ex-triffin-dilemma-reserve-currency")

S(EX, "medium", "Consider the following statements about the adequacy of foreign-exchange reserves:",
  "विदेशी मुद्रा भंडार की पर्याप्तता के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Import cover measures the number of months of imports that the reserves could pay for.",
   "The Greenspan-Guidotti rule suggests that reserves should at least equal the external debt falling due within a year.",
   "Import cover can fall even when the level of reserves stays unchanged."],
  ["आयात कवर यह मापता है कि भंडार कितने महीनों के आयात का भुगतान कर सकता है।",
   "ग्रीनस्पैन-गुइडोटी नियम सुझाता है कि भंडार कम से कम एक वर्ष के भीतर देय बाह्य ऋण के बराबर होना चाहिए।",
   "भंडार का स्तर अपरिवर्तित रहने पर भी आयात कवर घट सकता है।"],
  C3, 2,
  "All three are correct. Import cover is the simplest yardstick, and India's reserves have in recent years covered far more than the traditional comfort level of about three months of imports. "
  "The Greenspan-Guidotti rule looks at the capital account instead: a country should be able to repay all its short-term external debt for a year without fresh borrowing. "
  "Because import cover is reserves divided by monthly imports, it falls whenever imports grow faster than reserves, even if the stock of reserves does not change.",
  "तीनों कथन सही हैं। आयात कवर सबसे सरल पैमाना है, और हाल के वर्षों में भारत का भंडार लगभग तीन महीने के आयात के पारंपरिक सुरक्षित स्तर से कहीं अधिक रहा है। "
  "ग्रीनस्पैन-गुइडोटी नियम इसके बजाय पूँजी खाते को देखता है: किसी देश को बिना नए ऋण के एक वर्ष तक अपना सारा अल्पकालिक बाह्य ऋण चुकाने में सक्षम होना चाहिए। "
  "क्योंकि आयात कवर भंडार को मासिक आयात से भाग देकर निकलता है, इसलिए जब भी आयात भंडार से तेज़ बढ़ते हैं तो यह घटता है, भले ही भंडार की मात्रा न बदले।",
  f"{RBI} -- Annual Report and Monthly Bulletin, external sector indicators; International Monetary Fund -- reserve adequacy.",
  "ex-reserve-adequacy-import-cover")

# ================================================================ FINANCIAL MARKETS (4)
S(FM, "medium", "Consider the following statements about the Social Stock Exchange in India:",
  "भारत में सोशल स्टॉक एक्सचेंज के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is a separate segment of an existing stock exchange rather than a new, independent exchange.",
   "Registered not-for-profit organisations can raise money on it through Zero Coupon Zero Principal instruments.",
   "For-profit social enterprises can also raise funds through it."],
  ["यह कोई नया, स्वतंत्र एक्सचेंज नहीं बल्कि मौजूदा स्टॉक एक्सचेंज का एक अलग खंड है।",
   "पंजीकृत ग़ैर-लाभकारी संगठन इस पर ज़ीरो कूपन ज़ीरो प्रिंसिपल इंस्ट्रूमेंट के ज़रिए धन जुटा सकते हैं।",
   "लाभ के लिए काम करने वाले सामाजिक उद्यम भी इसके माध्यम से धन जुटा सकते हैं।"],
  C3, 2,
  "All three are correct. SEBI's framework (2022) set up the Social Stock Exchange as a segment of the NSE and the BSE. Not-for-profit organisations must first register; they can then issue Zero Coupon Zero Principal instruments, which give donors neither interest nor repayment -- only yearly reports on the social impact of their money -- or raise funds through other permitted routes. "
  "For-profit social enterprises can list equity or debt on it much as on the main board. Corporate foundations, political and religious bodies, and trade associations are not eligible.",
  "तीनों कथन सही हैं। SEBI के ढाँचे (2022) ने सोशल स्टॉक एक्सचेंज को NSE और BSE के एक खंड के रूप में बनाया। ग़ैर-लाभकारी संगठनों को पहले पंजीकरण कराना होता है; फिर वे ज़ीरो कूपन ज़ीरो प्रिंसिपल इंस्ट्रूमेंट जारी कर सकते हैं, जिनमें दानदाताओं को न ब्याज मिलता है न मूलधन वापस, केवल उनके धन के सामाजिक प्रभाव की वार्षिक रिपोर्ट, या अन्य अनुमत रास्तों से धन जुटा सकते हैं। "
  "लाभकारी सामाजिक उद्यम मुख्य बोर्ड की तरह इस पर इक्विटी या ऋण सूचीबद्ध कर सकते हैं। कॉरपोरेट फ़ाउंडेशन, राजनीतिक और धार्मिक संस्थाएँ तथा व्यापार संघ इसके पात्र नहीं हैं।",
  f"{SEBI} -- Framework on Social Stock Exchange (2022).",
  "fm-social-stock-exchange")

P(FM, "hard", "Consider the following pairs of stock-market terms and their meanings:",
  "शेयर बाज़ार के शब्दों और उनके अर्थों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Buyback : A company purchases its own shares from its shareholders",
   "Stock split : A company raises fresh capital by selling new shares to its existing shareholders",
   "Sweat equity : Free shares given to all shareholders out of the company's reserves",
   "India VIX : An index of the thirty largest companies listed on the National Stock Exchange"],
  ["बायबैक : कंपनी अपने ही शेयर अपने शेयरधारकों से ख़रीदती है",
   "स्टॉक स्प्लिट : कंपनी अपने मौजूदा शेयरधारकों को नए शेयर बेचकर नई पूँजी जुटाती है",
   "स्वेट इक्विटी : कंपनी के आरक्षित कोष से सभी शेयरधारकों को दिए गए मुफ़्त शेयर",
   "इंडिया VIX : नेशनल स्टॉक एक्सचेंज पर सूचीबद्ध तीस सबसे बड़ी कंपनियों का सूचकांक"],
  0,
  "Only the first pair is correct. In a buyback the company repurchases, and usually cancels, its own shares, returning cash to holders. "
  "A stock split only divides each share into more shares of a lower face value -- the share capital and each holder's stake stay the same; selling new shares to existing holders is a rights issue. "
  "Sweat equity is shares issued, often at a discount, to employees or directors for their know-how or for creating intellectual property; free shares out of reserves are a bonus issue. "
  "India VIX is the NSE's volatility index, worked out from Nifty 50 option prices to show how sharply the market expects prices to swing over the next 30 days -- hence its nickname, the 'fear gauge'.",
  "केवल पहला युग्म सही है। बायबैक में कंपनी अपने शेयर वापस ख़रीदकर प्रायः रद्द कर देती है और शेयरधारकों को नक़दी लौटाती है। "
  "स्टॉक स्प्लिट केवल हर शेयर को कम अंकित मूल्य वाले अधिक शेयरों में बाँटता है; शेयर पूँजी और हर शेयरधारक की हिस्सेदारी वही रहती है; मौजूदा शेयरधारकों को नए शेयर बेचना राइट्स इश्यू है। "
  "स्वेट इक्विटी वे शेयर हैं जो कर्मचारियों या निदेशकों को उनके ज्ञान या बौद्धिक संपदा बनाने के बदले, प्रायः छूट पर, दिए जाते हैं; आरक्षित कोष से मुफ़्त शेयर बोनस इश्यू हैं। "
  "इंडिया VIX, NSE का अस्थिरता सूचकांक है, जो निफ़्टी 50 के ऑप्शन मूल्यों से निकाला जाता है और दिखाता है कि बाज़ार अगले 30 दिनों में क़ीमतों में कितने उतार-चढ़ाव की अपेक्षा करता है; इसीलिए इसे 'भय का पैमाना' भी कहते हैं।",
  f"{SEBI} -- Buy-back of Securities Regulations, 2018 and Share Based Employee Benefits and Sweat Equity Regulations, 2021; National Stock Exchange -- India VIX.",
  "fm-market-terms-buyback-split-sweat-vix")

M(FM, "medium", "'Bima Sugam', an initiative in the insurance sector, is best described as",
  "बीमा क्षेत्र की पहल 'बीमा सुगम' का सबसे सही वर्णन है",
  ["an online marketplace where many insurers' policies can be bought, serviced and claimed",
   "a deposit insurance scheme that covers bank deposits above the present limit",
   "a scheme that gives gig workers free life cover and a monthly pension",
   "a reinsurance company set up jointly by public sector insurers to cover disaster losses"],
  ["एक ऑनलाइन बाज़ार जहाँ अनेक बीमा कंपनियों की पॉलिसियाँ ख़रीदी, सँभाली और क्लेम की जा सकें",
   "बैंक जमाओं को मौजूदा सीमा से ऊपर बीमा देने वाली जमा बीमा योजना",
   "गिग कामगारों को मुफ़्त जीवन बीमा और मासिक पेंशन देने वाली योजना",
   "आपदा से हुए नुक़सान को कवर करने के लिए सरकारी बीमा कंपनियों द्वारा मिलकर बनाई गई पुनर्बीमा कंपनी"],
  0,
  "Bima Sugam, driven by the Insurance Regulatory and Development Authority of India (IRDAI), is designed as a single digital platform -- run by a not-for-profit company owned by the insurers -- on which people can compare and buy life, health and general insurance from different companies, service their policies and settle claims. "
  "The aim is to cut distribution costs and raise India's low insurance penetration, much as a common platform did for digital payments. Deposit insurance is the business of the DICGC, not of the insurance regulator.",
  "बीमा सुगम, जिसे भारतीय बीमा विनियामक और विकास प्राधिकरण (IRDAI) आगे बढ़ा रहा है, एक एकल डिजिटल मंच के रूप में बनाया गया है, जिसे बीमा कंपनियों के स्वामित्व वाली एक ग़ैर-लाभकारी कंपनी चलाती है; इस पर लोग विभिन्न कंपनियों के जीवन, स्वास्थ्य और सामान्य बीमा की तुलना कर ख़रीद सकें, पॉलिसी से जुड़ी सेवाएँ ले सकें और क्लेम निपटा सकें। "
  "इसका उद्देश्य वितरण लागत घटाना और भारत में बीमा की कम पहुँच बढ़ाना है, जैसे एक साझा मंच ने डिजिटल भुगतान के लिए किया। जमा बीमा DICGC का काम है, बीमा नियामक का नहीं।",
  "Insurance Regulatory and Development Authority of India -- Bima Sugam.",
  "fm-bima-sugam")

S(FM, "easy", "Consider the following statements about municipal bonds in India:",
  "भारत में नगरपालिका बॉन्ड के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["They are debt instruments issued by urban local bodies to raise money for projects such as water supply or roads.",
   "They can be listed and traded on stock exchanges under SEBI's regulations."],
  ["ये नगरीय स्थानीय निकायों द्वारा जल आपूर्ति या सड़क जैसी परियोजनाओं के लिए धन जुटाने हेतु जारी ऋण-पत्र हैं।",
   "इन्हें SEBI के विनियमों के तहत स्टॉक एक्सचेंजों पर सूचीबद्ध कर उनका व्यापार किया जा सकता है।"],
  T2, 2,
  "Both statements are correct. Municipal bonds let city governments borrow directly from investors; Bengaluru and Ahmedabad were among the first issuers in the late 1990s, and issues picked up after SEBI framed regulations for the issue and listing of municipal debt securities (2015) and the Union government began offering incentives to cities that issue them. "
  "Only bodies with sound accounts and a good credit rating can tap the market, which is one reason few cities have done so.",
  "दोनों कथन सही हैं। नगरपालिका बॉन्ड से नगर सरकारें सीधे निवेशकों से उधार ले पाती हैं; 1990 के दशक के अंत में बेंगलुरु और अहमदाबाद पहले जारीकर्ताओं में थे, और SEBI द्वारा नगरपालिका ऋण प्रतिभूतियों के निर्गम और सूचीकरण के विनियम (2015) बनाने तथा केंद्र सरकार द्वारा बॉन्ड जारी करने वाले शहरों को प्रोत्साहन देने के बाद इनकी संख्या बढ़ी। "
  "केवल अच्छे लेखे-जोखे और अच्छी क्रेडिट रेटिंग वाले निकाय ही बाज़ार से धन ले सकते हैं, और यही एक कारण है कि कम शहरों ने ऐसा किया है।",
  f"{SEBI} -- Issue and Listing of Municipal Debt Securities Regulations (2015); Ministry of Housing and Urban Affairs.",
  "fm-municipal-bonds-easy")

# ================================================================ AGRICULTURE (2)
S(AG, "medium", "Consider the following statements about Farmer Producer Organisations (FPOs):",
  "किसान उत्पादक संगठनों (FPOs) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["A central scheme launched in 2020 set out to form and promote 10,000 new FPOs.",
   "An FPO can be registered either as a producer company under the Companies Act or as a cooperative society.",
   "FPOs are barred from selling their members' produce directly to buyers and must route all sales through APMC mandis."],
  ["2020 में शुरू हुई एक केंद्रीय योजना का लक्ष्य 10,000 नए FPO बनाना और उन्हें बढ़ावा देना था।",
   "किसी FPO को कंपनी अधिनियम के तहत उत्पादक कंपनी या सहकारी समिति के रूप में पंजीकृत कराया जा सकता है।",
   "FPOs अपने सदस्यों की उपज सीधे ख़रीदारों को नहीं बेच सकते और उन्हें सारी बिक्री APMC मंडियों से करनी होती है।"],
  C3, 1,
  "Statements 1 and 2 are correct. The Formation and Promotion of 10,000 FPOs scheme (2020) funds cluster-based farmer businesses -- management costs for five years, a matching equity grant and a credit guarantee -- with SFAC, NABARD and NCDC among the implementing agencies. FPOs register as producer companies (now under the Companies Act, 2013) or under cooperative laws. "
  "Statement 3 is wrong: pooling their produce lets FPOs bargain better, sell directly to processors, exporters and retail chains or on electronic platforms, and buy inputs in bulk -- that is their whole purpose.",
  "कथन 1 और 2 सही हैं। 10,000 FPOs के गठन और संवर्धन की योजना (2020) क्लस्टर-आधारित किसान व्यवसायों को धन देती है, जैसे पाँच वर्ष का प्रबंधन ख़र्च, बराबरी का इक्विटी अनुदान और ऋण गारंटी; SFAC, NABARD और NCDC इसकी कार्यान्वयन एजेंसियों में हैं। FPO उत्पादक कंपनी (अब कंपनी अधिनियम, 2013 के तहत) या सहकारी क़ानूनों के तहत पंजीकृत होते हैं। "
  "कथन 3 गलत है: उपज को एक साथ लाने से FPO बेहतर मोलभाव कर पाते हैं, प्रसंस्करणकर्ताओं, निर्यातकों और खुदरा शृंखलाओं को या इलेक्ट्रॉनिक मंचों पर सीधे बेचते हैं, और थोक में इनपुट ख़रीदते हैं; यही उनका पूरा उद्देश्य है।",
  f"{MOA} -- Formation and Promotion of 10,000 Farmer Producer Organisations (2020).",
  "ag-fpo-10000-scheme")

A(AG, "medium",
  "A farmer who stores grain in a warehouse registered with the Warehousing Development and Regulatory Authority can raise a bank loan against it without selling the crop.",
  "भंडारण विकास और विनियामक प्राधिकरण (WDRA) में पंजीकृत गोदाम में अनाज रखने वाला किसान फ़सल बेचे बिना उसके बदले बैंक ऋण ले सकता है।",
  "Electronic negotiable warehouse receipts issued by such warehouses can be pledged with banks as collateral.",
  "ऐसे गोदामों द्वारा जारी इलेक्ट्रॉनिक परक्राम्य भंडार रसीदें (e-NWR) बैंकों के पास ज़मानत के रूप में गिरवी रखी जा सकती हैं।",
  0,
  "Both statements are correct and Statement-II explains Statement-I. Under the Warehousing (Development and Regulation) Act, 2007, the WDRA registers warehouses and regulates negotiable warehouse receipts, which since 2017 have been issued in electronic form through repositories. "
  "Because the receipt is negotiable -- it can be transferred by endorsement -- banks accept it as security, so a farmer can borrow at harvest time and wait for better prices instead of selling into a glut.",
  "दोनों कथन सही हैं और कथन-II कथन-I की व्याख्या करता है। भंडारण (विकास और विनियमन) अधिनियम, 2007 के तहत WDRA गोदामों का पंजीकरण करता है और परक्राम्य भंडार रसीदों का विनियमन करता है, जो 2017 से रिपॉज़िटरी के माध्यम से इलेक्ट्रॉनिक रूप में जारी होती हैं। "
  "क्योंकि रसीद परक्राम्य है, यानी पृष्ठांकन से हस्तांतरित हो सकती है, बैंक इसे ज़मानत मानते हैं; इसलिए किसान कटाई के समय उधार लेकर बेहतर क़ीमत की प्रतीक्षा कर सकता है, भरमार के समय बेचने के बजाय।",
  "Warehousing (Development and Regulation) Act, 2007; Warehousing Development and Regulatory Authority -- e-NWR system.",
  "ag-wdra-enwr-pledge-loans")

# ================================================================ BUDGET (1)
A(FB, "easy",
  "Heavy borrowing by the government can push up interest rates for private borrowers.",
  "सरकार का भारी उधार निजी उधारकर्ताओं के लिए ब्याज दरें बढ़ा सकता है।",
  "Government borrowing increases the total supply of savings available to private borrowers.",
  "सरकारी उधार निजी उधारकर्ताओं के लिए उपलब्ध बचत की कुल आपूर्ति बढ़ाता है।",
  2,
  "Statement-I is correct but Statement-II is incorrect. When the government borrows heavily, it competes with private firms for the same pool of savings, and the higher interest rates that follow can squeeze out some private investment -- the 'crowding-out' effect. "
  "Statement-II has it backwards: government borrowing adds to the demand for loanable funds, not to their supply, which is exactly why rates tend to rise. The effect is weaker when the economy has spare capacity or when capital flows in from abroad.",
  "कथन-I सही है पर कथन-II गलत है। जब सरकार भारी उधार लेती है तो वह बचत के उसी भंडार के लिए निजी कंपनियों से होड़ करती है, और इससे बढ़ी ब्याज दरें कुछ निजी निवेश को बाहर धकेल सकती हैं; इसे 'क्राउडिंग-आउट' प्रभाव कहते हैं। "
  "कथन-II उल्टी बात कहता है: सरकारी उधार उधार-योग्य धन की माँग बढ़ाता है, आपूर्ति नहीं, और इसी कारण दरें बढ़ती हैं। जब अर्थव्यवस्था में क्षमता ख़ाली हो या विदेश से पूँजी आ रही हो, तब यह प्रभाव कमज़ोर होता है।",
  f"{NCM} -- Government Budget and the Economy.",
  "fb-crowding-out-easy")

# ================================================================ INDUSTRY & SERVICES (3)
S(IN, "hard", "Consider the following statements about the 'Ratna' status of central public sector enterprises (CPSEs):",
  "केंद्रीय सार्वजनिक क्षेत्र उद्यमों (CPSEs) के 'रत्न' दर्जे के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["A CPSE can be granted Maharatna status directly, without first having Navratna status.",
   "To become a Maharatna, a CPSE must be listed on an Indian stock exchange with the minimum prescribed public shareholding.",
   "The board of a Navratna CPSE can invest any amount in a single project without government approval."],
  ["किसी CPSE को पहले नवरत्न दर्जा पाए बिना सीधे महारत्न का दर्जा दिया जा सकता है।",
   "महारत्न बनने के लिए CPSE का न्यूनतम निर्धारित सार्वजनिक शेयरधारिता के साथ किसी भारतीय स्टॉक एक्सचेंज पर सूचीबद्ध होना आवश्यक है।",
   "नवरत्न CPSE का बोर्ड सरकार की मंज़ूरी के बिना किसी एक परियोजना में कितनी भी राशि निवेश कर सकता है।"],
  C3, 0,
  "Only statement 2 is correct. The Maharatna scheme (2010) is open only to CPSEs that already hold Navratna status, are listed with the minimum public shareholding under SEBI rules, and clear high thresholds of average turnover, net worth and net profit over three years. "
  "Statement 3 is wrong: a Navratna board may invest up to ₹1,000 crore, or 15 per cent of its net worth, in a single project without government approval; a Maharatna board's limit is higher, up to ₹5,000 crore. "
  "The status is conferred by the Department of Public Enterprises, now under the Ministry of Finance, and gives large CPSEs more freedom to compete and to expand abroad.",
  "केवल कथन 2 सही है। महारत्न योजना (2010) केवल उन CPSEs के लिए है जिनके पास पहले से नवरत्न दर्जा है, जो SEBI नियमों के अनुसार न्यूनतम सार्वजनिक शेयरधारिता के साथ सूचीबद्ध हैं, और जो तीन वर्षों के औसत कारोबार, निवल मूल्य और शुद्ध लाभ की ऊँची सीमाएँ पार करते हैं। "
  "कथन 3 गलत है: नवरत्न बोर्ड सरकार की मंज़ूरी के बिना किसी एक परियोजना में ₹1,000 करोड़ या अपने निवल मूल्य के 15 प्रतिशत तक निवेश कर सकता है; महारत्न बोर्ड की सीमा अधिक, ₹5,000 करोड़ तक, है। "
  "यह दर्जा सार्वजनिक उद्यम विभाग देता है, जो अब वित्त मंत्रालय के अधीन है, और इससे बड़े CPSEs को प्रतिस्पर्धा करने और विदेश में विस्तार की अधिक स्वतंत्रता मिलती है।",
  "Department of Public Enterprises -- Maharatna, Navratna and Miniratna schemes.",
  "in-maharatna-navratna-status")

S(IN, "medium", "Consider the following statements about product standards in India:",
  "भारत में उत्पाद मानकों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Quality Control Orders issued under the Bureau of Indian Standards Act, 2016 make it compulsory for the covered products to carry the BIS standard mark.",
   "Goods covered by a Quality Control Order are exempt from it when they are imported.",
   "Hallmarking of gold jewellery with a six-digit Hallmark Unique Identification (HUID) number has been made compulsory in notified districts."],
  ["भारतीय मानक ब्यूरो अधिनियम, 2016 के तहत जारी गुणवत्ता नियंत्रण आदेश (QCO) शामिल उत्पादों पर BIS मानक चिह्न लगाना अनिवार्य करते हैं।",
   "गुणवत्ता नियंत्रण आदेश के दायरे वाली वस्तुएँ आयात किए जाने पर उससे मुक्त रहती हैं।",
   "अधिसूचित ज़िलों में सोने के आभूषणों पर छह अंकों वाले हॉलमार्क यूनिक आइडेंटिफ़िकेशन (HUID) नंबर के साथ हॉलमार्किंग अनिवार्य कर दी गई है।"],
  C3, 1,
  "Statements 1 and 3 are correct. Ministries issue Quality Control Orders for products ranging from helmets and pressure cookers to steel and chemicals; once one is in force, no one may make, import, store or sell a covered product without BIS certification. "
  "Statement 2 is wrong: QCOs apply equally to imports -- which is why foreign makers must also obtain BIS licences, and why critics say some QCOs act as non-tariff barriers that raise input costs for Indian manufacturers. "
  "Compulsory hallmarking began in June 2021 in 256 districts and has since been widened; each piece carries a six-character alphanumeric HUID that lets buyers check its purity.",
  "कथन 1 और 3 सही हैं। मंत्रालय हेलमेट और प्रेशर कुकर से लेकर इस्पात और रसायनों तक के उत्पादों के लिए गुणवत्ता नियंत्रण आदेश जारी करते हैं; आदेश लागू होने पर कोई भी व्यक्ति BIS प्रमाणन के बिना शामिल उत्पाद न बना सकता है, न आयात, भंडारण या बिक्री कर सकता है। "
  "कथन 2 गलत है: QCO आयात पर भी समान रूप से लागू होते हैं; इसीलिए विदेशी निर्माताओं को भी BIS लाइसेंस लेना पड़ता है, और आलोचक कहते हैं कि कुछ QCO ग़ैर-शुल्क बाधा की तरह काम करते हैं जो भारतीय निर्माताओं की इनपुट लागत बढ़ाते हैं। "
  "अनिवार्य हॉलमार्किंग जून 2021 में 256 ज़िलों में शुरू हुई और तब से इसका विस्तार हुआ है; हर आभूषण पर छह अक्षरों-अंकों वाला HUID होता है जिससे ख़रीदार उसकी शुद्धता जाँच सकते हैं।",
  "Bureau of Indian Standards -- Quality Control Orders and hallmarking; Bureau of Indian Standards Act, 2016.",
  "in-qco-bis-hallmarking")

S(IN, "medium", "Consider the following statements about India's rules on foreign direct investment (FDI) in e-commerce:",
  "ई-कॉमर्स में प्रत्यक्ष विदेशी निवेश (FDI) पर भारत के नियमों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["FDI up to 100 per cent is allowed under the automatic route in the inventory-based model of e-commerce.",
   "An e-commerce marketplace with foreign investment may own the inventory of the goods sold on its platform.",
   "FDI in the marketplace model of e-commerce needs prior government approval."],
  ["ई-कॉमर्स के इन्वेंटरी-आधारित मॉडल में स्वचालित मार्ग से 100 प्रतिशत तक FDI की अनुमति है।",
   "विदेशी निवेश वाला ई-कॉमर्स मार्केटप्लेस अपने प्लेटफ़ॉर्म पर बिकने वाले सामान की इन्वेंटरी का स्वामी हो सकता है।",
   "ई-कॉमर्स के मार्केटप्लेस मॉडल में FDI के लिए सरकार की पूर्व मंज़ूरी आवश्यक है।"],
  C3, 3,
  "None is correct. Under the FDI policy, 100 per cent FDI is allowed through the automatic route only in the marketplace model, in which the company runs an online platform that brings buyers and sellers together. "
  "FDI is not allowed in the inventory-based model, in which the company owns the goods and sells them to consumers itself -- a line drawn to protect small retailers, since multi-brand retail remains restricted. "
  "The 2018 changes further barred marketplace entities from owning or controlling the inventory of vendors on their platforms, and barred vendors in which the marketplace holds equity from selling there.",
  "कोई भी कथन सही नहीं है। FDI नीति के तहत स्वचालित मार्ग से 100 प्रतिशत FDI की अनुमति केवल मार्केटप्लेस मॉडल में है, जिसमें कंपनी एक ऑनलाइन प्लेटफ़ॉर्म चलाती है जो ख़रीदारों और विक्रेताओं को जोड़ता है। "
  "इन्वेंटरी-आधारित मॉडल में, जिसमें कंपनी सामान की स्वामी होकर उसे ख़ुद उपभोक्ताओं को बेचती है, FDI की अनुमति नहीं है; यह रेखा छोटे खुदरा व्यापारियों की रक्षा के लिए खींची गई, क्योंकि बहु-ब्रांड खुदरा पर अब भी प्रतिबंध है। "
  "2018 के बदलावों ने आगे मार्केटप्लेस कंपनियों को अपने प्लेटफ़ॉर्म के विक्रेताओं की इन्वेंटरी पर स्वामित्व या नियंत्रण से रोका, और उन विक्रेताओं को भी वहाँ बेचने से रोका जिनमें मार्केटप्लेस की इक्विटी हिस्सेदारी हो।",
  f"{DPIIT} -- Consolidated FDI Policy and Press Note 2 (2018 Series) on e-commerce.",
  "in-ecommerce-fdi-marketplace-inventory")

if __name__ == "__main__":
    write("gs_l2_t21_economy.sql")
