# -*- coding: utf-8 -*-
"""Current Affairs · Test 4 (October to December 2026) -- part B: economy.

Each item names the policy or market and asks what it does and why: the cap on trade margins of cancer drugs (and the
law behind drug prices), the sale of IDBI Bank, why wholesale inflation ran at twice retail inflation, the new
fuel-efficiency norms for cars, forward guidance in the models that won the economics prize, and the free trade
agreement with New Zealand. Written month by month: October 2026 first. No stem carries a date (design doc, section 7)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2
from ca_common import MX, finish
from ca_t4_format import FORMAT, POS

d.SUBJECT = "Economy"
d.REQUIRE_CRAFT = True
PR, BK, IF, EN, MP, TR = "Prices & Regulation", "Banking", "Inflation", "Energy & Industry", "Monetary Policy", "External Sector"

# ---------------------------------------------------------------- October 2026

S(PR, "medium", "The National Pharmaceutical Pricing Authority capped the trade margins on 137 anti-cancer medicines at 30 per cent. Consider the following statements:",
  "राष्ट्रीय औषध मूल्य निर्धारण प्राधिकरण ने 137 कैंसर-रोधी दवाओं पर व्यापार मार्जिन 30 प्रतिशत पर सीमित कर दिया। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The cap covers medicines whose prices are not otherwise fixed under the Drugs (Prices Control) Order, 2013.",
   "The National Pharmaceutical Pricing Authority functions under the Ministry of Health and Family Welfare.",
   "The Drugs (Prices Control) Order is issued under the Essential Commodities Act, 1955."],
  ["यह सीमा उन दवाओं पर लागू है जिनकी क़ीमतें औषध (मूल्य नियंत्रण) आदेश, 2013 के अंतर्गत अन्यथा तय नहीं होतीं।",
   "राष्ट्रीय औषध मूल्य निर्धारण प्राधिकरण स्वास्थ्य और परिवार कल्याण मंत्रालय के अधीन कार्य करता है।",
   "औषध (मूल्य नियंत्रण) आदेश आवश्यक वस्तु अधिनियम, 1955 के अंतर्गत जारी किया जाता है।"],
  C3, 1,
  "Statements 1 and 3 are correct. The Drugs (Prices Control) Order fixes ceiling prices only for 'scheduled' formulations, those in the National List of Essential Medicines; for the rest, makers set their own prices and may raise them by up to 10 per cent a year. Using its power under paragraph 19 to act in the public interest in extraordinary circumstances, the Authority capped the trade margin -- the gap between the price to the distributor and the maximum retail price -- at 30 per cent for 137 non-scheduled cancer drugs, patented ones included, from November 2026; retail prices of some are expected to fall by up to 70 per cent. "
  "A 2019 pilot on 42 cancer drugs had cut prices of 526 brands by up to 90 per cent, showing that much of the price of such drugs was margin, not cost. The Order itself is issued by the Centre under the Essential Commodities Act. Statement 2 is wrong: the Authority, set up in 1997, is under the Department of Pharmaceuticals in the Ministry of Chemicals and Fertilizers; it is the drug regulator, the CDSCO, that is under the Health Ministry, a common confusion.",
  "कथन 1 और 3 सही हैं। औषध (मूल्य नियंत्रण) आदेश केवल ‘अनुसूचित’ फ़ॉर्मूलेशनों, यानी राष्ट्रीय आवश्यक दवा सूची वाली दवाओं, की अधिकतम क़ीमत तय करता है; शेष के लिए निर्माता अपनी क़ीमतें स्वयं तय करते हैं और उन्हें वर्ष में 10 प्रतिशत तक बढ़ा सकते हैं। असाधारण परिस्थितियों में लोकहित में कार्य करने की पैराग्राफ़ 19 की शक्ति का उपयोग करके प्राधिकरण ने नवंबर 2026 से 137 गैर-अनुसूचित कैंसर दवाओं, पेटेंट वाली सहित, के व्यापार मार्जिन -- वितरक को क़ीमत और अधिकतम खुदरा मूल्य के बीच का अंतर -- को 30 प्रतिशत पर सीमित किया; कुछ के खुदरा मूल्य 70 प्रतिशत तक घटने की आशा है। "
  "2019 में 42 कैंसर दवाओं पर एक प्रायोगिक क़दम ने 526 ब्रांडों की क़ीमतें 90 प्रतिशत तक घटाई थीं, जिससे दिखा कि ऐसी दवाओं की क़ीमत का बड़ा भाग लागत नहीं, मार्जिन था। आदेश स्वयं केंद्र आवश्यक वस्तु अधिनियम के अंतर्गत जारी करता है। कथन 2 ग़लत है: 1997 में स्थापित प्राधिकरण रसायन और उर्वरक मंत्रालय के औषध विभाग के अधीन है; स्वास्थ्य मंत्रालय के अधीन औषध नियामक सीडीएससीओ है, जिससे प्रायः भ्रम होता है।",
  "National Pharmaceutical Pricing Authority, notification under paragraph 19 of the DPCO, 2013 on trade margins of 137 anti-cancer drugs (October 2026); Drugs (Prices Control) Order, 2013; Essential Commodities Act, 1955.",
  "ca-t4-eco-nppa-trade-margin-cancer-non-scheduled-ec-act", craft="linkage")

S(BK, "medium", "The Cabinet approved the sale of a 60.72 per cent stake in IDBI Bank to Fairfax Financial Holdings. Consider the following statements:",
  "मंत्रिमंडल ने आईडीबीआई बैंक में 60.72 प्रतिशत हिस्सेदारी फ़ेयरफ़ैक्स फ़ाइनेंशियल होल्डिंग्स को बेचने की स्वीकृति दी। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The RBI has treated IDBI Bank as a private sector bank ever since the Life Insurance Corporation of India acquired a majority stake in it.",
   "The stake being sold was held entirely by the Government of India.",
   "After the sale, neither the Government nor the Life Insurance Corporation will hold any shares in the bank."],
  ["जब से भारतीय जीवन बीमा निगम ने आईडीबीआई बैंक में बहुमत हिस्सेदारी ली, आरबीआई उसे निजी क्षेत्र का बैंक मानता है।",
   "बेची जा रही हिस्सेदारी पूरी तरह भारत सरकार के पास थी।",
   "बिक्री के बाद न तो सरकार और न ही जीवन बीमा निगम के पास बैंक का कोई शेयर रहेगा।"],
  C3, 0,
  "Only statement 1 is correct. IDBI was set up in 1964 by an Act of Parliament as a subsidiary of the RBI, passed to the Government in 1976, became a bank in 2004 and was recategorised by the RBI as a private sector bank for regulatory purposes in January 2019, after the LIC acquired 51 per cent of it; together the Government and the LIC held about 95 per cent. "
  "Statement 2 is wrong: the 60.72 per cent comes from both owners -- 30.48 per cent from the Government and 30.24 per cent from the LIC -- in a strategic disinvestment run by the Department of Investment and Public Asset Management. Statement 3 is wrong: the two keep about 34 per cent between them. The buyer, a Canadian group, becomes the promoter subject to regulatory approvals; a sale of control, rather than of minority stakes, is what makes this a privatisation.",
  "केवल कथन 1 सही है। आईडीबीआई की स्थापना 1964 में संसद के अधिनियम से आरबीआई की सहायक संस्था के रूप में हुई, 1976 में यह सरकार को सौंपा गया, 2004 में बैंक बना और जनवरी 2019 में, एलआईसी द्वारा इसकी 51 प्रतिशत हिस्सेदारी लेने के बाद, आरबीआई ने विनियामक प्रयोजनों के लिए इसे निजी क्षेत्र के बैंक की श्रेणी में रखा; सरकार और एलआईसी के पास मिलाकर लगभग 95 प्रतिशत हिस्सा था। "
  "कथन 2 ग़लत है: 60.72 प्रतिशत दोनों स्वामियों से आता है -- 30.48 प्रतिशत सरकार से और 30.24 प्रतिशत एलआईसी से -- निवेश और लोक परिसंपत्ति प्रबंधन विभाग द्वारा चलाए गए रणनीतिक विनिवेश में। कथन 3 ग़लत है: दोनों के पास मिलाकर लगभग 34 प्रतिशत रहेगा। कनाडा का क्रेता समूह विनियामक अनुमोदनों के अधीन प्रवर्तक बनता है; अल्प हिस्सेदारी के बजाय नियंत्रण की बिक्री ही इसे निजीकरण बनाती है।",
  "Cabinet Committee on Economic Affairs and DIPAM, strategic disinvestment of IDBI Bank (October 2026); Reserve Bank of India, recategorisation of IDBI Bank as a private sector bank (March 2019).",
  "ca-t4-eco-idbi-sale-private-sector-lic-govt-34-residual", craft="precision")

A(IF, "hard",
  "In September 2026, inflation measured by the Wholesale Price Index was more than twice the inflation measured by the Consumer Price Index.",
  "सितंबर 2026 में थोक मूल्य सूचकांक से मापी गई मुद्रास्फीति उपभोक्ता मूल्य सूचकांक से मापी गई मुद्रास्फीति के दोगुने से अधिक थी।",
  "Prices in the fuel and power group, which carries about one-seventh of the weight in the new WPI, rose by about a quarter over the year.",
  "ईंधन और बिजली समूह, जिसका नए थोक मूल्य सूचकांक में भार लगभग सातवाँ भाग है, की क़ीमतें वर्ष भर में लगभग एक-चौथाई बढ़ीं।",
  1,
  "Both Statement II and Statement III are correct, but only Statement II explains Statement I. Provisional figures put wholesale inflation at 11.39 per cent and retail inflation at 5.54 per cent. The gap came mainly from energy: the fuel and power group, with a weight of 14.11 per cent in the 2022-23 series, rose 25.85 per cent, and costlier fuel also raises the prices of the manufactured intermediates that dominate the wholesale basket. The CPI gives fuel a smaller share and includes services, whose prices move slowly. "
  "Statement III is correct but says nothing about the gap: the new WPI series, with 957 items against 697, takes 2022-23 as its base and moved crude petroleum and natural gas into the fuel and power group. A wide gap matters because producers' costs tend to reach consumers with a lag, which is why wholesale inflation is watched as an early signal even though the RBI's target is set on the CPI.",
  "कथन II और कथन III दोनों सही हैं, पर केवल कथन II कथन I की व्याख्या करता है। अनंतिम आँकड़ों में थोक मुद्रास्फीति 11.39 प्रतिशत और खुदरा मुद्रास्फीति 5.54 प्रतिशत रही। अंतर मुख्यतः ऊर्जा से आया: 2022-23 शृंखला में 14.11 प्रतिशत भार वाला ईंधन और बिजली समूह 25.85 प्रतिशत बढ़ा, और महँगा ईंधन उन विनिर्मित मध्यवर्ती वस्तुओं की क़ीमतें भी बढ़ाता है जो थोक टोकरी में प्रमुख हैं। उपभोक्ता मूल्य सूचकांक ईंधन को कम हिस्सा देता है और उसमें सेवाएँ शामिल हैं, जिनकी क़ीमतें धीरे बदलती हैं। "
  "कथन III सही है पर अंतर के बारे में कुछ नहीं कहता: 697 के स्थान पर 957 वस्तुओं वाली थोक मूल्य सूचकांक की नई शृंखला 2022-23 को आधार लेती है और उसने कच्चे पेट्रोलियम तथा प्राकृतिक गैस को ईंधन और बिजली समूह में डाला। चौड़ा अंतर इसलिए मायने रखता है कि उत्पादकों की लागत कुछ अंतराल के बाद उपभोक्ताओं तक पहुँचती है, इसीलिए थोक मुद्रास्फीति को प्रारंभिक संकेत के रूप में देखा जाता है, यद्यपि आरबीआई का लक्ष्य उपभोक्ता मूल्य सूचकांक पर तय है।",
  "Office of the Economic Adviser, DPIIT, Index Numbers of Wholesale Price in India for September 2026 and the new series (base 2022-23); MoSPI, Consumer Price Index for September 2026.",
  "ca-t4-eco-wpi-twice-cpi-fuel-power-weight-si3",
  s3="The new series of the Wholesale Price Index uses 2022-23 as its base year.",
  s3_hi="थोक मूल्य सूचकांक की नई शृंखला 2022-23 को अपना आधार वर्ष मानती है।",
  craft="inference")

S(EN, "medium", "New Corporate Average Fuel Efficiency (CAFE) norms will apply to passenger cars from April 2027. Consider the following statements:",
  "नए कॉरपोरेट औसत ईंधन दक्षता (कैफ़े) मानदंड अप्रैल 2027 से यात्री कारों पर लागू होंगे। निम्नलिखित कथनों पर विचार कीजिए:",
  ["They are notified by the Ministry of Road Transport and Highways under the Motor Vehicles Act, 1988.",
   "Every model that a manufacturer sells must individually meet the prescribed fuel-efficiency target.",
   "Sales of electric cars help a manufacturer meet its target."],
  ["इन्हें मोटर वाहन अधिनियम, 1988 के अंतर्गत सड़क परिवहन और राजमार्ग मंत्रालय अधिसूचित करता है।",
   "निर्माता द्वारा बेचे जाने वाले प्रत्येक मॉडल को अलग-अलग निर्धारित ईंधन-दक्षता लक्ष्य पूरा करना होगा।",
   "इलेक्ट्रिक कारों की बिक्री निर्माता को अपना लक्ष्य पूरा करने में मदद करती है।"],
  C3, 0,
  "Only statement 3 is correct. The norms cap the average carbon dioxide emitted per kilometre -- equivalently, the fuel consumed -- across all the cars a maker sells in a year, weighted by sales. Electric, hybrid and other low-carbon cars pull that average down, which is the policy's lever towards cleaner vehicles. The third phase, for 2027-32, tightens the benchmark by about 16.7 per cent over five years. "
  "Statement 1 is wrong: CAFE norms are notified by the Ministry of Power under the Energy Conservation Act, 2001, with the Bureau of Energy Efficiency administering them; the transport ministry sets the Bharat Stage limits on tailpipe pollutants such as nitrogen oxides and particulates under the Central Motor Vehicles Rules -- a different goal, clean air, from CAFE's fuel economy. Statement 2 is wrong: the target applies to the fleet average, so a large, thirsty model can be offset by efficient ones.",
  "केवल कथन 3 सही है। ये मानदंड किसी निर्माता द्वारा वर्ष में बेची गई सभी कारों में, बिक्री से भारित, प्रति किलोमीटर उत्सर्जित औसत कार्बन डाइऑक्साइड -- यानी खपत होने वाले ईंधन -- को सीमित करते हैं। इलेक्ट्रिक, हाइब्रिड और अन्य कम-कार्बन कारें यह औसत नीचे लाती हैं, जो स्वच्छ वाहनों की ओर नीति का उत्तोलक है। 2027-32 का तीसरा चरण पाँच वर्षों में मानक को लगभग 16.7 प्रतिशत कड़ा करता है। "
  "कथन 1 ग़लत है: कैफ़े मानदंड ऊर्जा संरक्षण अधिनियम, 2001 के अंतर्गत विद्युत मंत्रालय अधिसूचित करता है और ऊर्जा दक्षता ब्यूरो उन्हें लागू करता है; परिवहन मंत्रालय केंद्रीय मोटर वाहन नियमों के अंतर्गत नाइट्रोजन ऑक्साइड और कणिकीय पदार्थ जैसे प्रदूषकों पर भारत स्टेज सीमाएँ तय करता है -- कैफ़े की ईंधन बचत से भिन्न लक्ष्य, स्वच्छ वायु। कथन 2 ग़लत है: लक्ष्य बेड़े के औसत पर लागू होता है, इसलिए बड़े, अधिक ईंधन खाने वाले मॉडल की भरपाई दक्ष मॉडलों से हो सकती है।",
  "Ministry of Power, Corporate Average Fuel Efficiency (CAFE-III) norms for passenger vehicles, 2027-32 (notified September 2026); Energy Conservation Act, 2001; Bureau of Energy Efficiency.",
  "ca-t4-eco-cafe-iii-power-ministry-fleet-average-ev", craft="application")

M(MP, "medium",
  "In the macroeconomic models that central banks now widely use, a credible announcement about the future path of interest rates ('forward guidance') can affect the economy even before rates change. This is mainly because",
  "केंद्रीय बैंकों द्वारा अब व्यापक रूप से प्रयुक्त समष्टि-आर्थिक मॉडलों में, ब्याज दरों के भावी मार्ग की विश्वसनीय घोषणा (‘फ़ॉरवर्ड गाइडेंस’) दरें बदलने से पहले ही अर्थव्यवस्था को प्रभावित कर सकती है। इसका मुख्य कारण है कि",
  ["households and firms look ahead, so the rates they expect shape their spending and price-setting today",
   "commercial banks are legally bound to change their lending rates as soon as such guidance is announced by the central bank",
   "the announcement by itself immediately increases the stock of money that is held by the public",
   "the guidance fixes the exchange rate of the currency against the major currencies for the period it covers"],
  ["परिवार और फ़र्में आगे देखती हैं, इसलिए अपेक्षित दरें आज ही उनके व्यय और मूल्य-निर्धारण को बदल देती हैं",
   "केंद्रीय बैंक द्वारा ऐसी घोषणा होते ही वाणिज्यिक बैंक अपनी ऋण दरें तुरंत बदलने के लिए विधिक रूप से बाध्य हो जाते हैं",
   "घोषणा स्वयं ही जनता के पास रखी मुद्रा की मात्रा को तुरंत बढ़ा देती है",
   "घोषणा अपनी अवधि के लिए मुद्रा की विनिमय दर को प्रमुख मुद्राओं के मुक़ाबले स्थिर कर देती है"],
  0,
  "Forward-looking behaviour is at the heart of the 'New Keynesian' models built on microeconomic foundations, the work for which Robert Hall and Michael Woodford received the 2026 prize in economic sciences. Households decide how much to save, and firms how to set prices, on the basis of the path of interest rates and inflation they expect; so a credible statement about future policy moves long-term interest rates, spending and price-setting today. This is why central banks now explain their stance -- the RBI's shift from 'neutral' to 'calibrated tightening' is itself a signal -- and why credibility is a central bank's main asset. "
  "Guidance binds no bank in law: lending rates follow through transmission, often with a lag. An announcement does not by itself change the money stock, which moves through the banks' lending and the central bank's operations. Nor does it fix the exchange rate, which under India's managed float is set in the market, with the RBI intervening to curb volatility.",
  "आगे देखने वाला व्यवहार सूक्ष्म-आर्थिक आधारों पर बने ‘न्यू कीन्सियन’ मॉडलों के केंद्र में है, वह कार्य जिसके लिए रॉबर्ट हॉल और माइकल वुडफ़र्ड को 2026 का आर्थिक विज्ञान पुरस्कार मिला। परिवार कितनी बचत करें और फ़र्में क़ीमतें कैसे तय करें, यह वे ब्याज दरों और मुद्रास्फीति के अपेक्षित मार्ग के आधार पर तय करते हैं; इसलिए भावी नीति के बारे में विश्वसनीय वक्तव्य आज ही दीर्घकालिक ब्याज दरों, व्यय और मूल्य-निर्धारण को बदल देता है। इसीलिए केंद्रीय बैंक अब अपना रुख़ समझाते हैं -- आरबीआई का ‘तटस्थ’ से ‘सधी हुई सख़्ती’ की ओर बदलाव स्वयं एक संकेत है -- और विश्वसनीयता केंद्रीय बैंक की मुख्य पूँजी है। "
  "घोषणा किसी बैंक को विधिक रूप से बाध्य नहीं करती: ऋण दरें संचरण से, प्रायः कुछ अंतराल के बाद, बदलती हैं। घोषणा स्वयं मुद्रा की मात्रा नहीं बदलती, जो बैंकों के ऋण और केंद्रीय बैंक की क्रियाओं से बदलती है। न ही यह विनिमय दर स्थिर करती है, जो भारत के प्रबंधित तिरते विनिमय में बाज़ार तय करता है और आरबीआई अस्थिरता रोकने के लिए हस्तक्षेप करता है।",
  "Royal Swedish Academy of Sciences, Prize in Economic Sciences 2026, popular and scientific background; Reserve Bank of India, Monetary Policy Statement (October 2026).",
  "ca-t4-eco-forward-guidance-forward-looking-agents", pos=POS.get("ca-t4-eco-forward-guidance-forward-looking-agents"), craft="inference")

S(TR, "medium", "The free trade agreement between India and New Zealand came into force in 2026. Consider the following statements:",
  "भारत और न्यूज़ीलैंड के बीच मुक्त व्यापार समझौता 2026 में प्रवृत्त हुआ। निम्नलिखित कथनों पर विचार कीजिए:",
  ["India removed customs duties on all its tariff lines for goods from New Zealand.",
   "Dairy products were kept out of India's tariff concessions.",
   "New Zealand committed itself to facilitating investment in India over a fifteen-year period."],
  ["भारत ने न्यूज़ीलैंड से आने वाली वस्तुओं के लिए अपनी सभी टैरिफ़ लाइनों पर सीमा शुल्क हटा दिया।",
   "डेयरी उत्पादों को भारत की टैरिफ़ रियायतों से बाहर रखा गया।",
   "न्यूज़ीलैंड ने पंद्रह वर्ष की अवधि में भारत में निवेश को सुगम बनाने की प्रतिबद्धता की।"],
  C3, 1,
  "Statements 2 and 3 are correct. India protected dairy, sugar and some sensitive farm products -- dairy was among India's main reasons for staying out of the Regional Comprehensive Economic Partnership in 2019, since New Zealand and Australia are among the world's largest dairy exporters and India's dairy sector rests on small producers. New Zealand committed itself to facilitating about US$ 20 billion of investment in India over fifteen years, with a mechanism for rebalancing if the investment falls short, a model India first used in its agreement with the EFTA countries. "
  "Statement 1 is wrong: it is New Zealand that removes duties on all its tariff lines for Indian goods from the day the agreement takes effect; India liberalised about 70 per cent of its lines, which still cover some 95 per cent of New Zealand's exports by value. Such asymmetry is common when a large, protected market opens to a small, open one.",
  "कथन 2 और 3 सही हैं। भारत ने डेयरी, चीनी और कुछ संवेदनशील कृषि उत्पादों को संरक्षित रखा -- 2019 में क्षेत्रीय व्यापक आर्थिक साझेदारी से बाहर रहने के भारत के मुख्य कारणों में डेयरी थी, क्योंकि न्यूज़ीलैंड और ऑस्ट्रेलिया विश्व के सबसे बड़े डेयरी निर्यातकों में हैं और भारत का डेयरी क्षेत्र छोटे उत्पादकों पर टिका है। न्यूज़ीलैंड ने पंद्रह वर्षों में भारत में लगभग 20 अरब अमेरिकी डॉलर के निवेश को सुगम बनाने की प्रतिबद्धता की, निवेश कम पड़ने पर पुनर्संतुलन की व्यवस्था के साथ, जो मॉडल भारत ने पहली बार ईएफ़टीए देशों के साथ अपने समझौते में अपनाया था। "
  "कथन 1 ग़लत है: समझौता प्रभावी होने के दिन से भारतीय वस्तुओं के लिए अपनी सभी टैरिफ़ लाइनों पर शुल्क न्यूज़ीलैंड हटाता है; भारत ने अपनी लगभग 70 प्रतिशत लाइनें उदार कीं, जो फिर भी मूल्य के हिसाब से न्यूज़ीलैंड के लगभग 95 प्रतिशत निर्यात को समेटती हैं। जब कोई बड़ा, संरक्षित बाज़ार किसी छोटे, खुले बाज़ार के लिए खुलता है तो ऐसी असमानता आम है।",
  "Ministry of Commerce and Industry, India-New Zealand Free Trade Agreement (signed April 2026, in force October 2026); New Zealand Ministry of Foreign Affairs and Trade, summary of the agreement.",
  "ca-t4-eco-india-nz-fta-asymmetric-dairy-investment-15-years", craft="linkage")

finish("ca_t4_b.sql", FORMAT, "2026-Q4", update="--update" in sys.argv)
