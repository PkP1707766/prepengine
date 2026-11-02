# -*- coding: utf-8 -*-
"""Level 4 · Simulator 2 (GS Paper I full mock, Layout B: the 2025 shape) -- part E: Economy (16)
(upsc_l4_gs_cell_targets.mjs 2).
The Economy bank is the most saturated (L1-L3 and CA cover most schemes, taxes and instruments), so every proposition
was swept in several spellings and kept only where no row tests it: rice fortification; the Bharat brand; Kisan
Vikas Patra, oil bonds and recapitalisation bonds; IMF quotas, the Sixteenth General Review and the BRICS CRA's
IMF-linked portion; front-running; pre-packaged insolvency for MSMEs; co-lending; securitisation of
standard assets; PM-VBRY, PM CARES for Children, AVYAY and PM-USHA; the RDI scheme; the Late Payment Surcharge
Rules and market coupling; the vehicle scrapping policy; seigniorage; currency chests; the countercyclical capital
buffer; post-devolution revenue deficit grants. MCQ keys are pinned (pos)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Economy"
d.REQUIRE_CRAFT = True

# ---------------------------------------------------------------- Agriculture & Food Economy (AR with Statement III, hard)
A("Agriculture & Food Economy", "hard",
  "Rice distributed under the public distribution system and other central food schemes is fortified with micronutrients.",
  "सार्वजनिक वितरण प्रणाली और अन्य केंद्रीय खाद्य योजनाओं के अंतर्गत बाँटा जाने वाला चावल सूक्ष्म पोषक तत्वों से प्रबलीकृत है।",
  "Fortified rice kernels, made from rice flour mixed with iron, folic acid and vitamin B12, are blended with ordinary rice in a ratio of about 1:100.",
  "चावल के आटे में लोहा, फ़ोलिक अम्ल और विटामिन बी12 मिलाकर बनाए गए प्रबलीकृत चावल दाने सामान्य चावल में लगभग 1:100 के अनुपात में मिलाए जाते हैं।",
  1,
  "Both Statement II and Statement III are correct, but only Statement III explains Statement I. The Government made fortified rice universal across the public distribution system, the PM POSHAN mid-day meal and the anganwadi services by March 2024, and in 2024 decided to continue it, fully funded by the Union, until December 2028, alongside the free foodgrains of PM-GKAY. The reason is the one in Statement III: anaemia remains very common among women and children, and adding iron, folic acid and vitamin B12 to a staple that poor households already eat is a cheap way to reach them. "
  "Statement II describes how it is done rather than why: the kernels are made by extruding rice flour with a premix of the micronutrients, shaped like grains, and mixed at about 10 grams per kilogram of rice, following the standards of the Food Safety and Standards Authority of India. Mills, the Food Corporation of India and State agencies blend them before the rice reaches ration shops.",
  "कथन II और कथन III दोनों सही हैं, पर केवल कथन III कथन I की व्याख्या करता है। सरकार ने मार्च 2024 तक सार्वजनिक वितरण प्रणाली, पीएम पोषण मध्याह्न भोजन और आँगनवाड़ी सेवाओं में प्रबलीकृत चावल को सार्वभौम बना दिया, और 2024 में तय किया कि पीएम-जीकेएवाई के निःशुल्क अनाज के साथ इसे दिसंबर 2028 तक, पूरी तरह संघ के व्यय पर, जारी रखा जाएगा। कारण वही है जो कथन III में है: स्त्रियों और बच्चों में रक्ताल्पता अब भी बहुत आम है, और जिस मुख्य भोजन को निर्धन परिवार पहले से खाते हैं उसमें लोहा, फ़ोलिक अम्ल और विटामिन बी12 मिलाना उन तक पहुँचने का सस्ता तरीक़ा है। "
  "कथन II बताता है कि यह कैसे होता है, क्यों नहीं: दाने चावल के आटे को सूक्ष्म पोषक तत्वों के प्रीमिक्स के साथ बाहर निकालकर (एक्सट्रूज़न) दानों के आकार में बनाए जाते हैं, और भारतीय खाद्य सुरक्षा और मानक प्राधिकरण के मानकों के अनुसार लगभग 10 ग्राम प्रति किलोग्राम चावल में मिलाए जाते हैं। मिलें, भारतीय खाद्य निगम और राज्य एजेंसियाँ राशन की दुकानों तक चावल पहुँचने से पहले इन्हें मिलाती हैं।",
  "Department of Food and Public Distribution, Government of India; Cabinet decision on continuation of fortified rice supply (2024); FSSAI, Food Safety and Standards (Fortification of Foods) Regulations.",
  "l4-s02-eco-rice-fortification-pds-frk-anaemia",
  s3="Fortification aims to address the wide prevalence of anaemia and micronutrient deficiencies.",
  s3_hi="प्रबलीकरण का उद्देश्य रक्ताल्पता और सूक्ष्म पोषक तत्वों की कमी के व्यापक प्रसार से निपटना है।",
  craft="linkage")

# ---------------------------------------------------------------- Agriculture & Food Economy (MCQ, hard)
M("Agriculture & Food Economy", "hard",
  "The 'Bharat' brand, under which atta, rice and chana dal have been sold since 2023-24, is best described as",
  "'भारत' ब्रांड, जिसके अंतर्गत 2023-24 से आटा, चावल और चना दाल बेचे जा रहे हैं, का सबसे उपयुक्त वर्णन है",
  ["staples sold below market price via NAFED, NCCF and Kendriya Bhandar to cool inflation",
   "an export label under which GI-tagged Indian rice and pulses are sold abroad under one name",
   "a certification mark for cereals grown organically by farmer producer organisations in India",
   "free grain given every month to priority households under the National Food Security Act"],
  ["महँगाई घटाने हेतु नाफ़ेड, एनसीसीएफ़ और केंद्रीय भंडार से बाज़ार से कम दाम पर बिकने वाले मुख्य खाद्यान्न",
   "एक निर्यात लेबल जिसके अंतर्गत जीआई-टैग वाले भारतीय चावल और दालें एक ही नाम से विदेश में बेचे जाते हैं",
   "भारत में किसान उत्पादक संगठनों द्वारा जैविक रूप से उगाए गए अनाज के लिए एक प्रमाणन चिह्न",
   "राष्ट्रीय खाद्य सुरक्षा अधिनियम के अंतर्गत प्राथमिकता वाले परिवारों को हर माह दिया जाने वाला निःशुल्क अनाज"],
  0,
  "When cereal and pulse prices rose in 2023, the Department of Consumer Affairs launched Bharat chana dal, then Bharat atta and Bharat rice, sold at fixed prices well below the market through outlets and mobile vans of the cooperatives NAFED and NCCF and of Kendriya Bhandar, and on e-commerce platforms. The atta and rice came from Food Corporation of India stocks offered under the open market sale scheme, and the dal from the buffer of chana held under the Price Stabilisation Fund. "
  "It is a consumer-side price intervention, unlike free grain under the National Food Security Act and PM-GKAY, which goes only to entitled households through ration shops; a second phase began in November 2024.",
  "2023 में अनाज और दालों के दाम बढ़ने पर उपभोक्ता मामले विभाग ने भारत चना दाल, फिर भारत आटा और भारत चावल आरंभ किए, जिन्हें सहकारी संस्थाओं नाफ़ेड और एनसीसीएफ़ तथा केंद्रीय भंडार की दुकानों और चलती गाड़ियों से, और ई-कॉमर्स मंचों पर, बाज़ार से काफ़ी कम तय दामों पर बेचा गया। आटा और चावल खुले बाज़ार बिक्री योजना के अंतर्गत दिए गए भारतीय खाद्य निगम के भंडार से आए, और दाल मूल्य स्थिरीकरण कोष के अंतर्गत रखे चने के बफ़र से। "
  "यह उपभोक्ता की ओर से मूल्य हस्तक्षेप है, राष्ट्रीय खाद्य सुरक्षा अधिनियम और पीएम-जीकेएवाई के निःशुल्क अनाज से अलग, जो राशन की दुकानों के माध्यम से केवल पात्र परिवारों को जाता है; इसका दूसरा चरण नवंबर 2024 में आरंभ हुआ।",
  "Department of Consumer Affairs, Government of India; Department of Food and Public Distribution, Open Market Sale Scheme (Domestic); Price Stabilisation Fund.",
  "l4-s02-eco-bharat-brand-atta-rice-dal-nafed-nccf", pos=1, craft="application")

# ---------------------------------------------------------------- Budget, Deficits & Public Debt (pairs, hard)
P("Budget, Deficits & Public Debt", "hard", "Consider the following pairs of instruments of government finance and their descriptions:",
  "सरकारी वित्त के साधनों और उनके विवरणों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Kisan Vikas Patra : A small savings certificate that doubles the amount invested over a fixed period",
   "Treasury Bills : Dated securities with maturities of five to forty years",
   "Oil bonds : Special securities issued to oil marketing companies instead of a cash subsidy",
   "Recapitalisation bonds : Special securities issued to raise the capital of public sector banks"],
  ["किसान विकास पत्र : एक लघु बचत प्रमाणपत्र जो निवेश की गई राशि को एक निश्चित अवधि में दोगुना करता है",
   "ट्रेज़री बिल : पाँच से चालीस वर्ष की परिपक्वता वाली दिनांकित प्रतिभूतियाँ",
   "तेल बॉन्ड : नक़द सब्सिडी के बदले तेल विपणन कंपनियों को जारी विशेष प्रतिभूतियाँ",
   "पुनर्पूंजीकरण बॉन्ड : सार्वजनिक क्षेत्र के बैंकों की पूँजी बढ़ाने के लिए जारी विशेष प्रतिभूतियाँ"],
  2,
  "Pairs 1, 3 and 4 are correct. Kisan Vikas Patra, sold at post offices, doubles the money invested over a period that depends on the notified interest rate; like other small savings, its collections go into the National Small Savings Fund in the Public Account, which lends them to the Union and so helps finance the fiscal deficit. Between 2005 and 2010 the Union issued oil bonds to the oil marketing companies to make up their losses on selling fuel below cost, which kept the subsidy out of the deficit of those years but left interest and repayments to later budgets. "
  "Recapitalisation bonds were issued from 2017 to public sector banks, which subscribed to them with the same money the Government put in as equity, strengthening their capital without immediate cash outgo; some later issues were non-interest-bearing special securities. Pair 2 is wrong: Treasury Bills are short-term money-market instruments of 91, 182 and 364 days, issued at a discount; dated securities run from about five to forty years and more.",
  "युग्म 1, 3 और 4 सही हैं। डाकघरों में बिकने वाला किसान विकास पत्र निवेश की गई राशि को अधिसूचित ब्याज दर पर निर्भर अवधि में दोगुना करता है; अन्य लघु बचतों की तरह इसका संग्रह लोक लेखा के राष्ट्रीय लघु बचत कोष में जाता है, जो इसे संघ को उधार देता है और इस प्रकार राजकोषीय घाटे के वित्तपोषण में सहायक होता है। 2005 और 2010 के बीच संघ ने तेल विपणन कंपनियों को लागत से कम पर ईंधन बेचने से हुई हानि की भरपाई के लिए तेल बॉन्ड जारी किए, जिससे उन वर्षों की सब्सिडी घाटे से बाहर रही, पर ब्याज और पुनर्भुगतान बाद के बजटों पर आ गए। "
  "पुनर्पूंजीकरण बॉन्ड 2017 से सार्वजनिक क्षेत्र के बैंकों को जारी किए गए, जिन्होंने उन्हें उसी धन से ख़रीदा जो सरकार ने इक्विटी के रूप में डाला, जिससे तुरंत नक़द व्यय के बिना उनकी पूँजी मज़बूत हुई; बाद के कुछ निर्गम ब्याज-रहित विशेष प्रतिभूतियाँ थे। युग्म 2 ग़लत है: ट्रेज़री बिल 91, 182 और 364 दिनों के अल्पकालिक मुद्रा-बाज़ार साधन हैं, जो बट्टे पर जारी होते हैं; दिनांकित प्रतिभूतियाँ लगभग पाँच से चालीस वर्ष और उससे अधिक की होती हैं।",
  "Ministry of Finance, Department of Economic Affairs, small savings schemes and National Small Savings Fund; Reserve Bank of India, Government Securities Market handbook; Union Budget documents, Statement of Liabilities.",
  "l4-s02-eco-kvp-tbills-oil-bonds-recap-bonds-pairs", craft="precision")

# ---------------------------------------------------------------- External Sector & International Institutions (statement, hard)
S("External Sector & International Institutions", "hard", "With reference to IMF quotas and the BRICS Contingent Reserve Arrangement, consider the following statements:",
  "आईएमएफ़ कोटा और ब्रिक्स आकस्मिक आरक्षित व्यवस्था के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["A member's quota largely determines its subscription to the IMF, its voting power and how much it can borrow.",
   "India's share of IMF quotas is smaller than its share of world GDP measured at purchasing power parity.",
   "Under the BRICS Contingent Reserve Arrangement, a member can draw beyond a limited share of its access only if it has an arrangement with the IMF.",
   "The Sixteenth General Review of Quotas raised quotas by 50 per cent in equal proportion, without realigning members' shares."],
  ["किसी सदस्य का कोटा मुख्यतः आईएमएफ़ में उसका अंशदान, उसकी मतदान शक्ति और वह कितना उधार ले सकता है, तय करता है।",
   "आईएमएफ़ कोटा में भारत का अंश क्रय शक्ति समता पर मापे गए विश्व जीडीपी में उसके अंश से कम है।",
   "ब्रिक्स आकस्मिक आरक्षित व्यवस्था के अंतर्गत कोई सदस्य अपनी पहुँच के एक सीमित अंश से अधिक तभी ले सकता है जब आईएमएफ़ के साथ उसकी कोई व्यवस्था हो।",
   "कोटा की सोलहवीं सामान्य समीक्षा ने सदस्यों के अंशों का पुनर्संयोजन किए बिना कोटा को समान अनुपात में 50 प्रतिशत बढ़ाया।"],
  C4, 3,
  "All four statements are correct. A quota, expressed in SDRs, sets a member's subscription, most of its votes (alongside basic votes) and its normal access to IMF lending, and guides its share of SDR allocations. India's quota share is about 2.75 per cent and its vote share about 2.6 per cent, well below its share of world GDP at purchasing power parity -- one reason why India and other emerging economies press for realignment. "
  "The Sixteenth General Review, concluded in December 2023, agreed on a 50 per cent increase in quotas in equal proportion, leaving any realignment of shares to later reviews. The BRICS Contingent Reserve Arrangement of 2014, a pool of 100 billion dollars of commitments (India's 18 billion), lets members draw on one another's reserves through currency swaps in a balance-of-payments squeeze, but only a 'de-linked' portion -- 30 per cent of a member's maximum access -- is available without an IMF programme, so it complements the IMF rather than replacing it.",
  "चारों कथन सही हैं। एसडीआर में व्यक्त कोटा किसी सदस्य का अंशदान, उसके अधिकांश मत (मूल मतों के साथ) और आईएमएफ़ ऋण तक उसकी सामान्य पहुँच तय करता है, और एसडीआर आवंटन में उसके अंश का आधार बनता है। भारत का कोटा अंश लगभग 2.75 प्रतिशत और मत अंश लगभग 2.6 प्रतिशत है, जो क्रय शक्ति समता पर विश्व जीडीपी में उसके अंश से काफ़ी कम है -- एक कारण कि भारत और अन्य उभरती अर्थव्यवस्थाएँ पुनर्संयोजन पर ज़ोर देती हैं। "
  "दिसंबर 2023 में पूरी हुई सोलहवीं सामान्य समीक्षा ने कोटा में समान अनुपात में 50 प्रतिशत वृद्धि पर सहमति दी, और अंशों के किसी पुनर्संयोजन को बाद की समीक्षाओं पर छोड़ दिया। 2014 की ब्रिक्स आकस्मिक आरक्षित व्यवस्था, 100 अरब डॉलर की प्रतिबद्धताओं का एक कोष (भारत की 18 अरब), सदस्यों को भुगतान-संतुलन संकट में मुद्रा-विनिमय के माध्यम से एक-दूसरे के भंडार का उपयोग करने देती है, पर केवल 'असंबद्ध' अंश -- किसी सदस्य की अधिकतम पहुँच का 30 प्रतिशत -- आईएमएफ़ कार्यक्रम के बिना उपलब्ध है, इसलिए यह आईएमएफ़ का स्थान नहीं लेती, उसकी पूरक है।",
  "IMF, Quotas factsheet and Board of Governors resolution on the Sixteenth General Review of Quotas (2023); Treaty for the Establishment of a BRICS Contingent Reserve Arrangement (2014).",
  "l4-s02-eco-imf-quota-16th-review-brics-cra-delinked", craft="multi")

# ---------------------------------------------------------------- Financial Markets, Instruments & Fintech (statement, hard)
S("Financial Markets, Instruments & Fintech", "hard", "With reference to front-running in the securities market, consider the following statements:",
  "प्रतिभूति बाज़ार में फ़्रंट-रनिंग के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["It means trading ahead of a large pending order, using knowledge of that order, to profit from the price move the order will cause.",
   "SEBI treats it as a fraudulent and unfair trade practice.",
   "SEBI requires asset management companies to set up an institutional mechanism to identify and deter market abuse such as front-running.",
   "It is an offence only when the trader is an employee of a stock exchange."],
  ["इसका अर्थ है किसी बड़े लंबित आदेश की जानकारी का उपयोग करके उससे पहले सौदा करना, ताकि उस आदेश से होने वाले मूल्य परिवर्तन से लाभ कमाया जा सके।",
   "सेबी इसे एक कपटपूर्ण और अनुचित व्यापार व्यवहार मानता है।",
   "सेबी परिसंपत्ति प्रबंधन कंपनियों से फ़्रंट-रनिंग जैसे बाज़ार दुरुपयोग की पहचान करने और उसे रोकने के लिए एक संस्थागत तंत्र बनाने की अपेक्षा करता है।",
   "यह तभी अपराध है जब सौदा करने वाला किसी स्टॉक एक्सचेंज का कर्मचारी हो।"],
  C4, 2,
  "The first three statements are correct. A dealer or fund manager who knows that a client or a mutual fund is about to place a large buy order can buy first, let the order push the price up, and sell at a profit -- a breach of the duty owed to the client and of fair dealing with the market. SEBI's Prohibition of Fraudulent and Unfair Trade Practices (PFUTP) Regulations, 2003 name trading in advance of a substantial client order as an unfair practice, and SEBI can bar the persons involved, impound the gains and prosecute. "
  "After front-running cases in mutual funds came to light, SEBI amended its Mutual Fund Regulations in 2024 to make asset management companies responsible for an institutional mechanism -- surveillance of trades and communications, escalation and whistle-blower channels -- to identify and deter such abuse. Statement 4 is wrong: the prohibition applies to anyone who trades on such knowledge, whether a broker's dealer, a fund manager or a relative who is tipped off; it is related to, but distinct from, insider trading, which uses unpublished price-sensitive information about a company.",
  "पहले तीन कथन सही हैं। जिस डीलर या कोष प्रबंधक को पता हो कि कोई ग्राहक या म्यूचुअल फ़ंड बड़ा ख़रीद आदेश देने वाला है, वह पहले ख़रीद सकता है, आदेश से मूल्य बढ़ने दे सकता है, और लाभ पर बेच सकता है -- यह ग्राहक के प्रति कर्तव्य और बाज़ार के साथ निष्पक्ष व्यवहार दोनों का उल्लंघन है। सेबी के कपटपूर्ण और अनुचित व्यापार व्यवहार निषेध (पीएफ़यूटीपी) विनियम, 2003 किसी बड़े ग्राहक आदेश से पहले सौदा करने को अनुचित व्यवहार बताते हैं, और सेबी संबंधित व्यक्तियों पर रोक लगा सकता है, लाभ ज़ब्त कर सकता है और अभियोजन कर सकता है। "
  "म्यूचुअल फ़ंडों में फ़्रंट-रनिंग के मामले सामने आने के बाद सेबी ने 2024 में अपने म्यूचुअल फ़ंड विनियमों में संशोधन कर परिसंपत्ति प्रबंधन कंपनियों को एक संस्थागत तंत्र -- सौदों और संचार की निगरानी, सूचना आगे बढ़ाने और व्हिसल-ब्लोअर माध्यम -- के लिए उत्तरदायी बनाया, ताकि ऐसे दुरुपयोग की पहचान हो और उसे रोका जा सके। कथन 4 ग़लत है: निषेध हर उस व्यक्ति पर लागू होता है जो ऐसी जानकारी पर सौदा करता है, चाहे ब्रोकर का डीलर हो, कोष प्रबंधक हो या कोई संबंधी जिसे सूचना दी गई हो; यह भेदिया व्यापार (इनसाइडर ट्रेडिंग) से जुड़ा पर उससे अलग है, जो किसी कंपनी के बारे में अप्रकाशित मूल्य-संवेदी जानकारी का उपयोग करता है।",
  "SEBI (Prohibition of Fraudulent and Unfair Trade Practices relating to Securities Market) Regulations, 2003, regulation 4(2); SEBI (Mutual Funds) (Amendment) Regulations, 2024.",
  "l4-s02-eco-front-running-pfutp-amc-institutional-mechanism", craft="precision")

S("Financial Markets, Instruments & Fintech", "hard", "With reference to the pre-packaged insolvency resolution process under the Insolvency and Bankruptcy Code, consider the following statements:",
  "दिवाला और शोधन अक्षमता संहिता के अंतर्गत पूर्व-नियोजित (प्री-पैकेज्ड) दिवाला समाधान प्रक्रिया के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is available to any corporate debtor, whatever its size.",
   "It can be started on the application of an operational creditor.",
   "The existing management is replaced by a resolution professional as soon as the process begins."],
  ["यह किसी भी कॉर्पोरेट देनदार के लिए, उसके आकार की परवाह किए बिना, उपलब्ध है।",
   "इसे किसी परिचालन लेनदार के आवेदन पर आरंभ किया जा सकता है।",
   "प्रक्रिया आरंभ होते ही वर्तमान प्रबंधन का स्थान एक समाधान पेशेवर ले लेता है।"],
  C3, 3,
  "None of the statements is correct. The pre-packaged process, added to the Code in 2021 as Chapter III-A, is open only to corporate debtors that are micro, small or medium enterprises, for defaults of at least ₹10 lakh. Only the corporate debtor itself can apply, and only after financial creditors not related to it, holding at least 66 per cent of its financial debt, have approved the proposal and the base resolution plan it brings. "
  "Unlike the regular corporate insolvency process, in which a resolution professional takes over the management, it is 'debtor-in-possession': the promoters keep running the business under the oversight of the resolution professional, unless the committee of creditors shows fraud or gross mismanagement. It must be completed within 120 days, and a plan that does not pay operational creditors in full can be exposed to competing plans (a Swiss challenge). It was designed to be faster and less disruptive for small firms hit by the pandemic.",
  "कोई भी कथन सही नहीं है। 2021 में संहिता में अध्याय III-क के रूप में जोड़ी गई पूर्व-नियोजित प्रक्रिया केवल उन कॉर्पोरेट देनदारों के लिए है जो सूक्ष्म, लघु या मध्यम उद्यम हैं, और कम से कम ₹10 लाख की चूक के लिए। केवल कॉर्पोरेट देनदार स्वयं आवेदन कर सकता है, और तभी जब उससे असंबद्ध, उसके वित्तीय ऋण का कम से कम 66 प्रतिशत रखने वाले वित्तीय लेनदारों ने प्रस्ताव और उसके साथ लाई गई आधार समाधान योजना को अनुमोदित कर दिया हो। "
  "सामान्य कॉर्पोरेट दिवाला प्रक्रिया के विपरीत, जिसमें समाधान पेशेवर प्रबंधन सँभाल लेता है, यह 'देनदार-के-क़ब्ज़े' वाली है: प्रवर्तक समाधान पेशेवर की देखरेख में व्यवसाय चलाते रहते हैं, जब तक लेनदारों की समिति कपट या घोर कुप्रबंधन न दिखाए। इसे 120 दिनों में पूरा होना होता है, और जो योजना परिचालन लेनदारों को पूरा भुगतान नहीं करती उसे प्रतिस्पर्धी योजनाओं (स्विस चैलेंज) के सामने रखा जा सकता है। इसे महामारी से प्रभावित छोटी फ़र्मों के लिए अधिक तेज़ और कम बाधक बनाने के लिए रचा गया।",
  "Insolvency and Bankruptcy Code, 2016, Chapter III-A (inserted by the Insolvency and Bankruptcy Code (Amendment) Act, 2021); Insolvency and Bankruptcy Board of India.",
  "l4-s02-eco-ibc-pre-pack-msme-debtor-in-possession", craft="precision")

# ---------------------------------------------------------------- Financial Markets, Instruments & Fintech (statement, medium)
S("Financial Markets, Instruments & Fintech", "medium", "With reference to co-lending by banks and non-banking financial companies, consider the following statements:",
  "बैंकों और ग़ैर-बैंकिंग वित्तीय कंपनियों द्वारा सह-ऋण के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["A bank and an NBFC jointly fund the loans, and the NBFC that originates them keeps a minimum share on its own books.",
   "Under the RBI's framework of 2020, the NBFC partner need not retain any share of the loans."],
  ["एक बैंक और एक एनबीएफ़सी मिलकर ऋण देते हैं, और उन्हें आरंभ करने वाली एनबीएफ़सी उनका एक न्यूनतम अंश अपने खातों में रखती है।",
   "आरबीआई के 2020 के ढाँचे के अंतर्गत एनबीएफ़सी साझेदार को ऋणों का कोई अंश रखने की आवश्यकता नहीं है।"],
  T2, 0,
  "Only statement 1 is correct. Co-lending joins the low cost of funds of banks to the reach of NBFCs, which source and service borrowers in places banks find hard to serve; the borrower sees a single interface and a blended interest rate. Statement 2 is wrong: the RBI's Co-Lending Model of 2020, which allowed banks to co-lend with NBFCs for priority sector loans, required the NBFC to retain at least 20 per cent of each loan on its own books, so that the originator shares the risk and keeps an incentive to choose borrowers carefully. "
  "The bank may take its share under a prior agreement or after due diligence on each loan, and its share counts towards its priority sector target. Retaining part of the risk is the same safeguard that rules on securitisation and default loss guarantees use against lenders who pass loans on without caring how they perform.",
  "केवल कथन 1 सही है। सह-ऋण बैंकों की कम लागत वाली निधियों को एनबीएफ़सी की पहुँच से जोड़ता है, जो ऐसे स्थानों पर उधारकर्ताओं को खोजती और सेवा देती हैं जहाँ बैंकों के लिए कठिन है; उधारकर्ता को एक ही इंटरफ़ेस और मिश्रित ब्याज दर दिखती है। कथन 2 ग़लत है: आरबीआई के 2020 के सह-ऋण मॉडल ने, जिसने बैंकों को प्राथमिकता क्षेत्र के ऋणों के लिए एनबीएफ़सी के साथ सह-ऋण की अनुमति दी, एनबीएफ़सी से प्रत्येक ऋण का कम से कम 20 प्रतिशत अपने खातों में रखने की अपेक्षा की, ताकि ऋण आरंभ करने वाला जोखिम में भागीदार रहे और उधारकर्ता सावधानी से चुनने का प्रोत्साहन बना रहे। "
  "बैंक अपना अंश पूर्व समझौते के अंतर्गत या प्रत्येक ऋण की समुचित जाँच के बाद ले सकता है, और उसका अंश उसके प्राथमिकता क्षेत्र लक्ष्य में गिना जाता है। जोखिम का अंश रखना वही सुरक्षा-उपाय है जिसका प्रयोग प्रतिभूतिकरण और चूक हानि गारंटी के नियम उन ऋणदाताओं के विरुद्ध करते हैं जो ऋणों के प्रदर्शन की चिंता किए बिना उन्हें आगे बढ़ा देते हैं।",
  "Reserve Bank of India, Co-Lending by Banks and NBFCs to Priority Sector (circular, November 2020).",
  "l4-s02-eco-co-lending-model-2020-nbfc-20-per-cent", craft="precision")

S("Financial Markets, Instruments & Fintech", "medium", "With reference to the securitisation of loans in India, consider the following statements:",
  "भारत में ऋणों के प्रतिभूतिकरण के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["A lender pools loans and transfers them to a special purpose entity, which issues securities backed by the repayments.",
   "Pass-through certificates pass the borrowers' repayments on to the investors who hold them.",
   "The RBI requires the lender that originated the loans to retain a minimum share of their risk.",
   "Non-banking financial companies, including housing finance companies, may securitise standard assets."],
  ["कोई ऋणदाता ऋणों को एकत्र कर एक विशेष प्रयोजन इकाई को हस्तांतरित करता है, जो पुनर्भुगतानों पर आधारित प्रतिभूतियाँ जारी करती है।",
   "पास-थ्रू प्रमाणपत्र उधारकर्ताओं के पुनर्भुगतान उन्हें धारण करने वाले निवेशकों तक पहुँचाते हैं।",
   "आरबीआई ऋण आरंभ करने वाले ऋणदाता से उनके जोखिम का एक न्यूनतम अंश रखने की अपेक्षा करता है।",
   "आवास वित्त कंपनियों सहित ग़ैर-बैंकिंग वित्तीय कंपनियाँ मानक आस्तियों का प्रतिभूतिकरण कर सकती हैं।"],
  C4, 3,
  "All four statements are correct. Securitisation turns illiquid loans into tradable securities: the originator sells a pool of loans to a bankruptcy-remote special purpose entity, which pays for it by issuing securities, such as pass-through certificates, whose investors receive the principal and interest as borrowers repay. It frees capital for fresh lending and spreads risk to investors who want it. "
  "The RBI's Master Direction on Securitisation of Standard Assets (2021), which applies to banks, NBFCs including housing finance companies and all-India financial institutions, sets a minimum retention requirement -- usually 5 or 10 per cent depending on the maturity of the loans -- and a minimum holding period before loans can be sold, so that originators keep 'skin in the game'. Loose securitisation of mortgages without such safeguards was at the heart of the global financial crisis of 2008.",
  "चारों कथन सही हैं। प्रतिभूतिकरण अतरल ऋणों को व्यापार-योग्य प्रतिभूतियों में बदलता है: ऋण आरंभ करने वाला ऋणों का एक समूह दिवालियापन से सुरक्षित विशेष प्रयोजन इकाई को बेचता है, जो पास-थ्रू प्रमाणपत्रों जैसी प्रतिभूतियाँ जारी करके उसका भुगतान करती है, जिनके निवेशकों को उधारकर्ताओं के चुकाने पर मूलधन और ब्याज मिलता है। यह नए ऋण के लिए पूँजी मुक्त करता है और जोखिम उसे चाहने वाले निवेशकों तक फैलाता है। "
  "मानक आस्तियों के प्रतिभूतिकरण पर आरबीआई का मास्टर निदेश (2021), जो बैंकों, आवास वित्त कंपनियों सहित एनबीएफ़सी और अखिल भारतीय वित्तीय संस्थाओं पर लागू होता है, न्यूनतम प्रतिधारण अपेक्षा -- प्रायः ऋणों की परिपक्वता के अनुसार 5 या 10 प्रतिशत -- और ऋण बेचने से पहले न्यूनतम धारण अवधि तय करता है, ताकि ऋण आरंभ करने वालों का अपना दाँव बना रहे। ऐसे सुरक्षा-उपायों के बिना बंधक ऋणों का ढीला प्रतिभूतिकरण 2008 के वैश्विक वित्तीय संकट के केंद्र में था।",
  "Reserve Bank of India, Master Direction -- Reserve Bank of India (Securitisation of Standard Assets) Directions, 2021.",
  "l4-s02-eco-securitisation-ptc-mrr-nbfc-hfc", craft="linkage")

# ---------------------------------------------------------------- Inclusive Growth, Welfare & Demography (pairs, hard)
P("Inclusive Growth, Welfare & Demography", "hard", "Consider the following pairs of schemes and what they provide:",
  "योजनाओं और उनके द्वारा दी जाने वाली सुविधाओं के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Pradhan Mantri Viksit Bharat Rozgar Yojana : Incentives for new jobs, paid through the EPFO to employers and first-time employees",
   "PM CARES for Children : Support for children who lost their parents to COVID-19",
   "Atal Vayo Abhyuday Yojana : An umbrella scheme for the welfare of senior citizens",
   "PM-USHA : Upgrading government primary schools into model schools"],
  ["प्रधानमंत्री विकसित भारत रोज़गार योजना : नए रोज़गार के लिए प्रोत्साहन, ईपीएफ़ओ के माध्यम से नियोक्ताओं और पहली बार नौकरी पाने वालों को",
   "पीएम केयर्स फ़ॉर चिल्ड्रन : कोविड-19 में माता-पिता खोने वाले बच्चों को सहायता",
   "अटल वयो अभ्युदय योजना : वरिष्ठ नागरिकों के कल्याण के लिए एक व्यापक (अंब्रेला) योजना",
   "पीएम-उषा : सरकारी प्राथमिक विद्यालयों को आदर्श विद्यालयों में उन्नत करना"],
  2,
  "Pairs 1, 2 and 3 are correct. The Employment Linked Incentive scheme approved in 2025, renamed the Pradhan Mantri Viksit Bharat Rozgar Yojana, pays first-time employees registered with the EPFO an incentive of up to one month's wage, and pays employers a monthly amount for each additional worker they hire, for two years -- four in manufacturing -- for jobs created between August 2025 and July 2027. PM CARES for Children (2021) supports children who lost both parents, a surviving parent or a guardian to COVID-19, with a corpus that matures when they turn 23, free schooling and health cover. "
  "The Atal Vayo Abhyuday Yojana of the Ministry of Social Justice brings together programmes for older persons, such as homes and day-care centres, aids and assistive devices under the Rashtriya Vayoshri Yojana, and the Elderline helpline. Pair 4 is wrong: PM-USHA (Pradhan Mantri Uchchatar Shiksha Abhiyan), the successor to RUSA, funds State universities and colleges to improve access, equity and quality in higher education; upgrading existing schools into exemplar schools under NEP 2020 is the aim of PM SHRI.",
  "युग्म 1, 2 और 3 सही हैं। 2025 में स्वीकृत रोज़गार-आधारित प्रोत्साहन योजना, जिसका नाम प्रधानमंत्री विकसित भारत रोज़गार योजना रखा गया, ईपीएफ़ओ में पंजीकृत पहली बार नौकरी पाने वालों को एक माह के वेतन तक का प्रोत्साहन देती है, और नियोक्ताओं को हर अतिरिक्त कर्मचारी के लिए दो वर्ष -- विनिर्माण में चार वर्ष -- तक मासिक राशि देती है, अगस्त 2025 से जुलाई 2027 के बीच बने रोज़गारों के लिए। पीएम केयर्स फ़ॉर चिल्ड्रन (2021) उन बच्चों की सहायता करती है जिन्होंने कोविड-19 में माता-पिता दोनों, जीवित माता या पिता या अभिभावक को खो दिया, ऐसे कोष के साथ जो 23 वर्ष की आयु पर परिपक्व होता है, निःशुल्क शिक्षा और स्वास्थ्य बीमा के साथ। "
  "सामाजिक न्याय मंत्रालय की अटल वयो अभ्युदय योजना वृद्धजनों के कार्यक्रमों -- जैसे आश्रय गृह और दिवा देखभाल केंद्र, राष्ट्रीय वयोश्री योजना के अंतर्गत सहायक उपकरण, और एल्डरलाइन हेल्पलाइन -- को एक साथ लाती है। युग्म 4 ग़लत है: रूसा की उत्तराधिकारी पीएम-उषा (प्रधानमंत्री उच्चतर शिक्षा अभियान) उच्च शिक्षा में पहुँच, समता और गुणवत्ता बढ़ाने के लिए राज्य विश्वविद्यालयों और महाविद्यालयों को धन देती है; राष्ट्रीय शिक्षा नीति 2020 के अंतर्गत मौजूदा विद्यालयों को आदर्श विद्यालयों में उन्नत करना पीएम श्री का उद्देश्य है।",
  "Ministry of Labour and Employment (ELI scheme / PM-VBRY, 2025); Ministry of Women and Child Development (PM CARES for Children); Ministry of Social Justice and Empowerment (AVYAY); Ministry of Education (PM-USHA, PM SHRI).",
  "l4-s02-eco-pm-vbry-pm-cares-children-avyay-pm-usha-pairs", craft="precision")

# ---------------------------------------------------------------- Industry, Infrastructure, Energy & Services (MCQ, medium)
M("Industry, Infrastructure, Energy & Services", "medium",
  "The Research, Development and Innovation (RDI) Scheme approved by the Union Cabinet in 2025 is meant mainly to",
  "2025 में केंद्रीय मंत्रिमंडल द्वारा स्वीकृत अनुसंधान, विकास और नवाचार (आरडीआई) योजना का मुख्य उद्देश्य है",
  ["lend long-term at low or nil interest for private research in sunrise sectors",
   "fund new research universities run jointly by the Union and the States in every region",
   "give a 200 per cent tax deduction on research spending by companies in all sectors",
   "pay monthly fellowships to doctoral students who study science in public universities"],
  ["उभरते क्षेत्रों में निजी क्षेत्र के अनुसंधान के लिए कम या शून्य ब्याज पर दीर्घकालिक वित्त देना",
   "हर क्षेत्र में संघ और राज्यों द्वारा मिलकर चलाए जाने वाले नए अनुसंधान विश्वविद्यालयों को धन देना",
   "सभी क्षेत्रों में कंपनियों के अनुसंधान व्यय पर 200 प्रतिशत कर कटौती देना",
   "सार्वजनिक विश्वविद्यालयों में विज्ञान पढ़ने वाले शोध छात्रों को मासिक फ़ेलोशिप देना"],
  0,
  "Announced in the interim Budget of 2024 and approved in July 2025, the scheme has a corpus of ₹1 lakh crore to spur private investment in research, development and innovation, where India's spending is low and comes mostly from the government. A Special Purpose Fund within the Anusandhan National Research Foundation holds the corpus and passes money to second-level fund managers, which lend to companies, mainly as long-term loans at low or nil interest, with equity possible for start-ups, in strategic and sunrise areas such as energy, semiconductors, artificial intelligence, quantum technology and biotechnology. "
  "It finances late-stage, higher-risk projects that banks shy away from, rather than giving grants, tax breaks or fellowships -- the tools named in the other options.",
  "2024 के अंतरिम बजट में घोषित और जुलाई 2025 में स्वीकृत इस योजना का कोष ₹1 लाख करोड़ है, ताकि अनुसंधान, विकास और नवाचार में निजी निवेश बढ़े, जहाँ भारत का व्यय कम है और अधिकांशतः सरकार से आता है। अनुसंधान नेशनल रिसर्च फ़ाउंडेशन के भीतर एक विशेष प्रयोजन कोष यह राशि रखता है और दूसरे स्तर के कोष प्रबंधकों को देता है, जो कंपनियों को, मुख्यतः कम या शून्य ब्याज पर दीर्घकालिक ऋणों के रूप में और स्टार्ट-अप के लिए इक्विटी के रूप में भी, ऊर्जा, सेमीकंडक्टर, कृत्रिम बुद्धिमत्ता, क्वांटम प्रौद्योगिकी और जैव प्रौद्योगिकी जैसे सामरिक और उभरते क्षेत्रों में देते हैं। "
  "यह बाद के चरण की, अधिक जोखिम वाली उन परियोजनाओं को वित्त देती है जिनसे बैंक कतराते हैं, अनुदान, कर छूट या फ़ेलोशिप -- अन्य विकल्पों में बताए साधन -- देने के बजाय।",
  "Cabinet decision on the Research, Development and Innovation Scheme (1 July 2025); Department of Science and Technology; Anusandhan National Research Foundation.",
  "l4-s02-eco-rdi-scheme-anrf-spf-long-term-loans", pos=2, craft="precision")

# ---------------------------------------------------------------- Industry, Infrastructure, Energy & Services (statement, medium)
S("Industry, Infrastructure, Energy & Services", "medium", "With reference to the electricity sector in India, consider the following statements:",
  "भारत में विद्युत क्षेत्र के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Under the Late Payment Surcharge Rules, 2022, a distribution company that does not clear its dues to generators in time can be cut off from buying power on the power exchanges.",
   "Under market coupling, the bids received on all the power exchanges are pooled to discover a single market-clearing price.",
   "Electricity is a subject in the Union List of the Constitution."],
  ["विलंब भुगतान अधिभार नियम, 2022 के अंतर्गत, जो वितरण कंपनी समय पर उत्पादकों का बकाया नहीं चुकाती, उसे पावर एक्सचेंजों पर बिजली ख़रीदने से रोका जा सकता है।",
   "मार्केट कपलिंग के अंतर्गत सभी पावर एक्सचेंजों पर प्राप्त बोलियों को मिलाकर एक ही बाज़ार-समाशोधन मूल्य निकाला जाता है।",
   "विद्युत संविधान की संघ सूची का विषय है।"],
  C3, 1,
  "Only statements 1 and 2 are correct. The Electricity (Late Payment Surcharge and Related Matters) Rules, 2022 gave distribution companies a way to clear old dues in instalments, but provide that a company that defaults beyond the permitted period loses access to short-term power purchase through the exchanges, and its long-term access is cut in steps, until it pays -- a lever that sharply reduced overdue payments to generators. "
  "In market coupling, a single operator collects the buy and sell bids from all exchanges and clears them together, so that the whole country gets one price instead of slightly different prices on each exchange; the Central Electricity Regulatory Commission has decided to introduce it in phases, starting with the day-ahead market. Statement 3 is wrong: electricity is Entry 38 of the Concurrent List, which is why both the Union's Electricity Act, 2003 and State regulatory commissions shape the sector.",
  "केवल कथन 1 और 2 सही हैं। विद्युत (विलंब भुगतान अधिभार और संबंधित मामले) नियम, 2022 ने वितरण कंपनियों को पुराने बकाये किस्तों में चुकाने का रास्ता दिया, पर यह प्रावधान भी किया कि अनुमत अवधि से अधिक चूक करने वाली कंपनी एक्सचेंजों के माध्यम से अल्पकालिक बिजली ख़रीद की पहुँच खो देती है, और भुगतान करने तक उसकी दीर्घकालिक पहुँच चरणों में घटाई जाती है -- एक ऐसा साधन जिसने उत्पादकों के अतिदेय भुगतानों को तेज़ी से घटाया। "
  "मार्केट कपलिंग में एक ही संचालक सभी एक्सचेंजों से ख़रीद और बिक्री की बोलियाँ एकत्र करके उन्हें साथ में समाशोधित करता है, ताकि हर एक्सचेंज पर थोड़े अलग मूल्यों के बजाय पूरे देश को एक मूल्य मिले; केंद्रीय विद्युत विनियामक आयोग ने इसे चरणों में, डे-अहेड बाज़ार से आरंभ करते हुए, लागू करने का निर्णय लिया है। कथन 3 ग़लत है: विद्युत समवर्ती सूची की प्रविष्टि 38 है, इसी कारण संघ का विद्युत अधिनियम, 2003 और राज्य विनियामक आयोग दोनों इस क्षेत्र को आकार देते हैं।",
  "Ministry of Power, Electricity (Late Payment Surcharge and Related Matters) Rules, 2022; Central Electricity Regulatory Commission, orders on market coupling; Constitution of India, Seventh Schedule, List III, Entry 38.",
  "l4-s02-eco-lps-rules-market-coupling-concurrent", craft="multi")

S("Industry, Infrastructure, Energy & Services", "medium", "With reference to the Vehicle Scrapping Policy launched in 2021, consider the following statements:",
  "2021 में आरंभ वाहन स्क्रैपिंग नीति के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["An owner who scraps a vehicle at a registered facility gets a certificate of deposit that brings concessions on buying a new vehicle.",
   "The policy bans every private vehicle older than fifteen years from Indian roads."],
  ["किसी पंजीकृत सुविधा पर वाहन स्क्रैप कराने वाले स्वामी को एक जमा प्रमाणपत्र मिलता है, जिससे नया वाहन ख़रीदने पर रियायतें मिलती हैं।",
   "नीति पंद्रह वर्ष से पुराने हर निजी वाहन को भारतीय सड़कों से प्रतिबंधित करती है।"],
  T2, 0,
  "Only statement 1 is correct. The policy sets up Registered Vehicle Scrapping Facilities and Automated Testing Stations. An owner who scraps an old vehicle gets a certificate of deposit, which can be used to get a waiver of registration fees and a concession in motor vehicle tax from the States -- up to 25 per cent for private vehicles and 15 per cent for commercial ones -- on a new vehicle. "
  "Statement 2 is wrong: the policy is based on fitness rather than age. Private vehicles need re-registration after fifteen years and commercial vehicles regular fitness certificates after eight, and only those that fail the tests must be deregistered; government vehicles older than fifteen years are being scrapped from April 2023. The age limits for diesel and petrol vehicles in Delhi-NCR come from orders of the National Green Tribunal and the Supreme Court, not from this policy. Scrapping also yields steel scrap for a less carbon-intensive way of making steel.",
  "केवल कथन 1 सही है। नीति पंजीकृत वाहन स्क्रैपिंग सुविधाएँ और स्वचालित परीक्षण केंद्र स्थापित करती है। पुराना वाहन स्क्रैप कराने वाले स्वामी को एक जमा प्रमाणपत्र मिलता है, जिससे नए वाहन पर पंजीकरण शुल्क में छूट और राज्यों से मोटर वाहन कर में रियायत -- निजी वाहनों के लिए 25 प्रतिशत और व्यावसायिक वाहनों के लिए 15 प्रतिशत तक -- मिल सकती है। "
  "कथन 2 ग़लत है: नीति आयु के बजाय फ़िटनेस पर आधारित है। निजी वाहनों को पंद्रह वर्ष के बाद पुनः पंजीकरण और व्यावसायिक वाहनों को आठ वर्ष के बाद नियमित फ़िटनेस प्रमाणपत्र चाहिए, और केवल परीक्षण में विफल वाहनों का पंजीकरण रद्द करना होता है; पंद्रह वर्ष से पुराने सरकारी वाहन अप्रैल 2023 से स्क्रैप किए जा रहे हैं। दिल्ली-एनसीआर में डीज़ल और पेट्रोल वाहनों की आयु सीमाएँ राष्ट्रीय हरित अधिकरण और सर्वोच्च न्यायालय के आदेशों से आती हैं, इस नीति से नहीं। स्क्रैपिंग से इस्पात बनाने के कम कार्बन वाले तरीक़े के लिए इस्पात स्क्रैप भी मिलता है।",
  "Ministry of Road Transport and Highways, Motor Vehicles (Registration and Functions of Vehicle Scrapping Facility) Rules, 2021 and related notifications.",
  "l4-s02-eco-vehicle-scrapping-certificate-of-deposit-fitness", craft="application")

# ---------------------------------------------------------------- Macro Concepts, National Income & Inflation (AR, easy)
A("Macro Concepts, National Income & Inflation", "easy",
  "Issuing currency is a source of income for the Reserve Bank of India.",
  "मुद्रा जारी करना भारतीय रिज़र्व बैंक के लिए आय का एक स्रोत है।",
  "The RBI holds interest-earning assets against the currency it issues, while it pays no interest on the currency itself.",
  "आरबीआई अपने द्वारा जारी मुद्रा के बदले ब्याज कमाने वाली आस्तियाँ रखता है, जबकि स्वयं मुद्रा पर वह कोई ब्याज नहीं देता।",
  0,
  "Both statements are correct, and Statement II explains Statement I. Currency is a liability of the RBI on which it pays nothing, while the assets it acquires when it puts currency into circulation -- government securities and foreign assets -- earn interest. The difference, less the cost of printing and distributing notes, is seigniorage, a major part of the RBI's income. "
  "After making provisions, the RBI transfers its surplus to the Government, and these transfers have become an important non-tax revenue for the Union Budget. The same logic explains why a non-interest-bearing digital rupee also earns seigniorage, and why high inflation is called an 'inflation tax' when governments lean on currency issue.",
  "दोनों कथन सही हैं, और कथन II कथन I की व्याख्या करता है। मुद्रा आरबीआई की देयता है जिस पर वह कुछ नहीं देता, जबकि मुद्रा को प्रचलन में लाते समय वह जो आस्तियाँ प्राप्त करता है -- सरकारी प्रतिभूतियाँ और विदेशी आस्तियाँ -- उन पर ब्याज मिलता है। नोट छापने और बाँटने की लागत घटाने के बाद यही अंतर सिन्योरेज (मुद्रा-निर्गम लाभ) है, जो आरबीआई की आय का बड़ा भाग है। "
  "प्रावधान करने के बाद आरबीआई अपना अधिशेष सरकार को हस्तांतरित करता है, और ये हस्तांतरण संघीय बजट के लिए महत्त्वपूर्ण ग़ैर-कर राजस्व बन गए हैं। यही तर्क बताता है कि ब्याज-रहित डिजिटल रुपया भी सिन्योरेज क्यों कमाता है, और जब सरकारें मुद्रा जारी करने पर निर्भर होती हैं तो ऊँची मुद्रास्फीति को 'मुद्रास्फीति कर' क्यों कहा जाता है।",
  "Reserve Bank of India, Annual Report (income and surplus transfer); NCERT, Class XII, Introductory Macroeconomics, chapter on money and banking.",
  "l4-s02-eco-seigniorage-rbi-income-surplus", craft="inference")

# ---------------------------------------------------------------- Money, Banking & Monetary Policy (MCQ, medium)
M("Money, Banking & Monetary Policy", "medium",
  "A 'currency chest' is",
  "'करेंसी चेस्ट' क्या है?",
  ["a store of notes and coins that a bank holds on the RBI's behalf",
   "the reserve of gold and foreign assets that legally backs the notes issued by the RBI",
   "a fund in the Public Account into which the profits of the RBI are first credited",
   "a vault at a Security Printing Press where newly printed notes are counted and sealed"],
  ["नोटों और सिक्कों का भंडार जिसे कोई बैंक आरबीआई की ओर से रखता है",
   "सोने और विदेशी आस्तियों का वह भंडार जो आरबीआई द्वारा जारी नोटों का विधिक आधार है",
   "लोक लेखा में वह कोष जिसमें आरबीआई का लाभ पहले जमा किया जाता है",
   "किसी प्रतिभूति मुद्रणालय की वह तिजोरी जहाँ नए छपे नोट गिनकर सील किए जाते हैं"],
  0,
  "To distribute notes and coins across a large country, the RBI authorises banks to run currency chests, of which there are a few thousand. The notes in a chest belong to the RBI, not to the bank: when a bank moves cash from its own counters into the chest, its current account with the RBI is credited, and when it draws cash out, the account is debited. Chests receive fresh notes from the RBI, supply branches in their area and send back soiled notes for destruction. "
  "The reserve that backs the note issue is a different thing: under section 33 of the RBI Act, the Bank must hold gold and foreign assets of at least ₹200 crore, of which at least ₹115 crore in gold -- the minimum reserve system.",
  "इतने बड़े देश में नोट और सिक्के बाँटने के लिए आरबीआई बैंकों को करेंसी चेस्ट चलाने के लिए अधिकृत करता है, जिनकी संख्या कुछ हज़ार है। चेस्ट के नोट आरबीआई के होते हैं, बैंक के नहीं: जब कोई बैंक अपने काउंटरों से नक़दी चेस्ट में डालता है, तो आरबीआई में उसके चालू खाते में जमा होता है, और जब वह नक़दी निकालता है, तो खाता नामे होता है। चेस्ट आरबीआई से नए नोट पाते हैं, अपने क्षेत्र की शाखाओं को देते हैं और गंदे नोट नष्ट करने के लिए वापस भेजते हैं। "
  "नोट जारी करने का आधार बनने वाला भंडार अलग चीज़ है: आरबीआई अधिनियम की धारा 33 के अंतर्गत बैंक को कम से कम ₹200 करोड़ का सोना और विदेशी आस्तियाँ रखनी होती हैं, जिनमें कम से कम ₹115 करोड़ सोने में -- न्यूनतम आरक्षित प्रणाली।",
  "Reserve Bank of India, Master Direction on currency distribution and exchange scheme for bank branches including currency chests; Reserve Bank of India Act, 1934, section 33.",
  "l4-s02-eco-currency-chest-rbi-property-minimum-reserve", pos=1, craft="precision")

# ---------------------------------------------------------------- Money, Banking & Monetary Policy (statement, medium)
S("Money, Banking & Monetary Policy", "medium", "With reference to the countercyclical capital buffer for banks, consider the following statements:",
  "बैंकों के लिए प्रतिचक्रीय पूँजी बफ़र के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["It requires banks to build up extra capital when credit is growing fast, which can be released in a downturn.",
   "The RBI's framework uses the gap between the credit-to-GDP ratio and its long-term trend as the main indicator.",
   "It is the same as the capital conservation buffer that every bank must hold at all times."],
  ["यह बैंकों से ऋण तेज़ी से बढ़ने के समय अतिरिक्त पूँजी जमा करने की अपेक्षा करता है, जिसे मंदी में मुक्त किया जा सकता है।",
   "आरबीआई का ढाँचा ऋण-जीडीपी अनुपात और उसकी दीर्घकालिक प्रवृत्ति के बीच के अंतर को मुख्य संकेतक के रूप में प्रयोग करता है।",
   "यह वही पूँजी संरक्षण बफ़र है जिसे हर बैंक को हर समय रखना होता है।"],
  C3, 1,
  "Only statements 1 and 2 are correct. Under Basel III, the countercyclical capital buffer (CCyB) can range from zero to 2.5 per cent of risk-weighted assets: it is raised when credit growth runs ahead of the economy and systemic risk builds up, and released in bad times so that banks can absorb losses without cutting lending sharply. The RBI's framework of 2015 uses the credit-to-GDP gap as the main indicator, read together with others such as the growth of gross non-performing assets, and the RBI has so far judged that the buffer need not be activated. "
  "Statement 3 is wrong: the capital conservation buffer of 2.5 per cent is a fixed layer that banks must hold above the minimum at all times, and drawing on it restricts dividends; systemically important banks hold a further surcharge on top. The CCyB is the only one of these that moves with the credit cycle.",
  "केवल कथन 1 और 2 सही हैं। बेसल III के अंतर्गत प्रतिचक्रीय पूँजी बफ़र (सीसीवाईबी) जोखिम-भारित आस्तियों के शून्य से 2.5 प्रतिशत तक हो सकता है: जब ऋण वृद्धि अर्थव्यवस्था से आगे निकल जाती है और प्रणालीगत जोखिम बढ़ता है तो इसे बढ़ाया जाता है, और बुरे समय में मुक्त किया जाता है ताकि बैंक ऋण में तेज़ कटौती किए बिना हानियाँ झेल सकें। आरबीआई का 2015 का ढाँचा ऋण-जीडीपी अंतर को मुख्य संकेतक के रूप में, सकल अनर्जक आस्तियों की वृद्धि जैसे अन्य संकेतकों के साथ पढ़ते हुए, प्रयोग करता है, और आरबीआई ने अब तक माना है कि बफ़र को सक्रिय करने की आवश्यकता नहीं है। "
  "कथन 3 ग़लत है: 2.5 प्रतिशत का पूँजी संरक्षण बफ़र एक स्थिर परत है जिसे बैंकों को न्यूनतम से ऊपर हर समय रखना होता है, और इसका उपयोग लाभांश को सीमित करता है; प्रणालीगत रूप से महत्त्वपूर्ण बैंक इसके ऊपर एक और अधिभार रखते हैं। इनमें से केवल सीसीवाईबी ही ऋण चक्र के साथ बदलता है।",
  "Reserve Bank of India, Guidelines on Implementation of Countercyclical Capital Buffer (2015); Basel Committee on Banking Supervision, Basel III framework.",
  "l4-s02-eco-countercyclical-capital-buffer-credit-gdp-gap", craft="precision")

# ---------------------------------------------------------------- Taxation & Fiscal Federalism (AR with Statement III, hard)
A("Taxation & Fiscal Federalism", "hard",
  "The Fifteenth Finance Commission recommended post-devolution revenue deficit grants for only some of the States.",
  "पंद्रहवें वित्त आयोग ने केवल कुछ राज्यों के लिए हस्तांतरण-पश्चात राजस्व घाटा अनुदान की संस्तुति की।",
  "These grants cover the gap that remains in a State's revenue account after its share of Union taxes has been taken into account.",
  "ये अनुदान किसी राज्य के राजस्व खाते में संघीय करों में उसके हिस्से को गिनने के बाद बचे अंतर को पूरा करते हैं।",
  2,
  "Statement II is correct and explains Statement I; Statement III is incorrect. The Finance Commission first estimates each State's revenue and expenditure and its share in the divisible pool; States whose revenue account still shows a deficit after devolution receive grants under Article 275 to close it. Because tax devolution already favours poorer States, only some States -- seventeen in 2021-22 under the Fifteenth Commission, fewer in later years as the grants tapered -- qualified, many of them hill and north-eastern States with a small tax base. "
  "Statement III is wrong: Article 275(1) lets Parliament provide grants-in-aid to any State that it determines to be in need of assistance; its provisos add specific grants for the welfare of Scheduled Tribes and the administration of Scheduled Areas, and for Assam's tribal areas, but they do not limit the Article to such States. Critics argue that revenue deficit grants can reward States that do not raise their own revenue, which is why Commissions taper them.",
  "कथन II सही है और कथन I की व्याख्या करता है; कथन III ग़लत है। वित्त आयोग पहले प्रत्येक राज्य के राजस्व, व्यय और विभाज्य पूल में उसके हिस्से का अनुमान लगाता है; जिन राज्यों के राजस्व खाते में हस्तांतरण के बाद भी घाटा रहता है, उन्हें उसे पूरा करने के लिए अनुच्छेद 275 के अंतर्गत अनुदान मिलते हैं। क्योंकि कर हस्तांतरण पहले से ही निर्धन राज्यों के पक्ष में है, इसलिए केवल कुछ राज्य -- पंद्रहवें आयोग के अंतर्गत 2021-22 में सत्रह, अनुदानों के घटने के साथ बाद के वर्षों में कम -- पात्र हुए, जिनमें से कई छोटे कर आधार वाले पहाड़ी और पूर्वोत्तर राज्य हैं। "
  "कथन III ग़लत है: अनुच्छेद 275(1) संसद को किसी भी ऐसे राज्य को सहायता अनुदान देने देता है जिसे वह सहायता की आवश्यकता वाला माने; इसके परंतुक अनुसूचित जनजातियों के कल्याण और अनुसूचित क्षेत्रों के प्रशासन के लिए, और असम के जनजातीय क्षेत्रों के लिए, विशिष्ट अनुदान जोड़ते हैं, पर अनुच्छेद को ऐसे राज्यों तक सीमित नहीं करते। आलोचकों का तर्क है कि राजस्व घाटा अनुदान उन राज्यों को पुरस्कृत कर सकते हैं जो अपना राजस्व नहीं बढ़ाते, इसी कारण आयोग इन्हें क्रमशः घटाते हैं।",
  "Constitution of India, Article 275; Report of the Fifteenth Finance Commission for 2021-26.",
  "l4-s02-eco-revenue-deficit-grants-15th-fc-art275",
  s3="Grants-in-aid under Article 275 can be given only to States that have Scheduled Areas.",
  s3_hi="अनुच्छेद 275 के अंतर्गत सहायता अनुदान केवल उन्हीं राज्यों को दिए जा सकते हैं जिनमें अनुसूचित क्षेत्र हैं।",
  craft="linkage")

write("gs_l4_s02_e.sql")
