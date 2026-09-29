# -*- coding: utf-8 -*-
"""Level 2 · Test 16 (Economy 2: Growth, Development & External Sector) -- External Sector, part 1 (38):
balance of payments, reserves, exchange rates, convertibility, foreign investment, FEMA and LRS, and
trade policy and remedies. Cells: medium statement 14, easy statement 5, hard statement 5, medium MCQ 5,
medium Statement-I/II 4, easy MCQ 1, hard MCQ 1, easy Statement-I/II 1, hard I/II/III 1, hard pairs 1.
International institutions, WTO rules and trade agreements are in econ_l2_t16_institutions_growth.py.
Test 15 already tests masala bonds, the RBI's sterilisation and FPI registration, so they are left out."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Economy"
EX = "External Sector & International Institutions"
NCM = "NCERT Class XII, Introductory Macroeconomics -- Open Economy Macroeconomics"
RBI = "Reserve Bank of India"
DGFT = "Ministry of Commerce and Industry -- Directorate General of Foreign Trade"

# ================================================================ MEDIUM STATEMENTS (14)
S(EX, "medium", "Consider the following statements about the balance of payments:",
  "भुगतान संतुलन के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Remittances sent home by Indians working abroad are recorded in the current account.",
   "Foreign direct investment inflows are recorded in the current account.",
   "Once errors and omissions are included, the balance of payments as a whole always balances."],
  ["विदेश में काम करने वाले भारतीयों द्वारा घर भेजा गया धन चालू खाते में दर्ज होता है।",
   "प्रत्यक्ष विदेशी निवेश के अंतर्वाह चालू खाते में दर्ज होते हैं।",
   "त्रुटियों और चूकों को शामिल करने के बाद भुगतान संतुलन समग्र रूप से सदा संतुलित रहता है।"],
  C3, 1,
  "Statements 1 and 3 are correct. Remittances are transfers, recorded as secondary income in the current account alongside trade in goods and services and investment income. The balance of payments is double-entry: a current account deficit is matched by net capital inflows or a fall in reserves, with 'errors and omissions' covering gaps in the data. "
  "Statement 2 is wrong: FDI, portfolio investment, external loans and NRI deposits are flows of capital, recorded in the capital (financial) account.",
  "कथन 1 और 3 सही हैं। धन-प्रेषण हस्तांतरण हैं, जिन्हें वस्तुओं और सेवाओं के व्यापार तथा निवेश आय के साथ चालू खाते में द्वितीयक आय के रूप में दर्ज किया जाता है। भुगतान संतुलन दोहरी प्रविष्टि वाला होता है: चालू खाते के घाटे की भरपाई शुद्ध पूँजी अंतर्वाह या भंडार में कमी से होती है, और आँकड़ों की कमियों को 'त्रुटियाँ और चूकें' पूरा करती हैं। "
  "कथन 2 गलत है: FDI, पोर्टफ़ोलियो निवेश, बाहरी ऋण और NRI जमाएँ पूँजी के प्रवाह हैं, जो पूँजी (वित्तीय) खाते में दर्ज होते हैं।",
  f"{NCM}; {RBI} -- Balance of Payments statistics.",
  "ex-bop-accounts")

S(EX, "medium", "Consider the following statements about India's current account:",
  "भारत के चालू खाते के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["India usually runs a deficit in merchandise trade.",
   "India runs a surplus in its trade in services.",
   "India is the world's largest recipient of remittances.",
   "India's current account has been in surplus in most years since 2000."],
  ["भारत प्रायः वस्तु व्यापार में घाटा उठाता है।",
   "सेवाओं के व्यापार में भारत अधिशेष में रहता है।",
   "भारत विश्व में धन-प्रेषण पाने वाला सबसे बड़ा देश है।",
   "2000 के बाद से अधिकांश वर्षों में भारत का चालू खाता अधिशेष में रहा है।"],
  C4, 2,
  "Statements 1, 2 and 3 are correct. Heavy imports of crude oil, gold, electronics and coal leave a large goods deficit, which is partly offset by surpluses in software and business services and by remittances of well over 100 billion dollars a year. "
  "Statement 4 is wrong: India has run a current account deficit in most years; surpluses were seen only in a few years, such as the early 2000s and 2020-21, when the pandemic cut imports.",
  "कथन 1, 2 और 3 सही हैं। कच्चे तेल, सोने, इलेक्ट्रॉनिक्स और कोयले के भारी आयात से वस्तुओं में बड़ा घाटा रहता है, जिसकी आंशिक भरपाई सॉफ़्टवेयर और व्यावसायिक सेवाओं के अधिशेष और हर वर्ष 100 अरब डॉलर से काफ़ी अधिक के धन-प्रेषण से होती है। "
  "कथन 4 गलत है: भारत अधिकांश वर्षों में चालू खाते के घाटे में रहा है; अधिशेष केवल कुछ वर्षों में दिखा, जैसे 2000 के दशक के आरंभ में और 2020-21 में, जब महामारी ने आयात घटा दिए।",
  f"{RBI} -- Balance of Payments; World Bank -- Migration and Development Brief.",
  "ex-india-current-account")

S(EX, "medium", "Consider the following statements about India's foreign exchange reserves:",
  "भारत के विदेशी मुद्रा भंडार के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["India holds some of the largest foreign exchange reserves in the world.",
   "Foreign currency assets form the largest part of the reserves.",
   "The RBI is the custodian of the country's foreign exchange reserves."],
  ["भारत के पास विश्व के सबसे बड़े विदेशी मुद्रा भंडारों में से एक है।",
   "विदेशी मुद्रा परिसंपत्तियाँ भंडार का सबसे बड़ा भाग हैं।",
   "RBI देश के विदेशी मुद्रा भंडार का संरक्षक (custodian) है।"],
  C3, 2,
  "All three statements are correct. India's reserves, among the four or five largest in the world, give a cushion of many months of imports. Foreign currency assets -- mostly securities of other governments and deposits with central banks and the BIS -- dominate, and the RBI manages them for safety and liquidity first, and only then for return.",
  "तीनों कथन सही हैं। विश्व के चार-पाँच सबसे बड़े भंडारों में शामिल भारत का भंडार कई महीनों के आयात का सहारा देता है। विदेशी मुद्रा परिसंपत्तियाँ, जो अधिकतर दूसरी सरकारों की प्रतिभूतियाँ और केंद्रीय बैंकों तथा BIS में जमाएँ हैं, इसमें प्रमुख हैं, और RBI इनका प्रबंधन पहले सुरक्षा और तरलता के लिए, और उसके बाद ही प्रतिफल के लिए करता है।",
  f"{RBI} -- Half-yearly Report on Management of Foreign Exchange Reserves.",
  "ex-forex-reserves-basics")

S(EX, "medium", "Consider the following statements about the rupee's exchange rate:",
  "रुपये की विनिमय दर के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["India follows a fixed exchange rate pegged to the US dollar.",
   "The RBI intervenes in the foreign exchange market mainly to curb excessive volatility, not to defend a particular level.",
   "The rupee's exchange rate is fixed each day by the Ministry of Finance."],
  ["भारत अमेरिकी डॉलर से जुड़ी स्थिर विनिमय दर अपनाता है।",
   "RBI विदेशी मुद्रा बाज़ार में मुख्य रूप से अत्यधिक उतार-चढ़ाव रोकने के लिए हस्तक्षेप करता है, किसी विशेष स्तर की रक्षा के लिए नहीं।",
   "रुपये की विनिमय दर हर दिन वित्त मंत्रालय तय करता है।"],
  C3, 0,
  "Only statement 2 is correct: the rupee has been market-determined since 1993 -- a managed float -- with the RBI buying or selling dollars to smooth sharp swings. "
  "Statement 1 is wrong: India left the fixed and basket-linked systems behind with the Liberalised Exchange Rate Management System of 1992 and the unified market rate of 1993. "
  "Statement 3 is wrong: no authority fixes the rate; it is set by demand and supply in the interbank market, although the RBI publishes a reference rate.",
  "केवल कथन 2 सही है: 1993 से रुपया बाज़ार द्वारा निर्धारित है, यानी प्रबंधित अस्थिर (managed float), और RBI तेज़ उतार-चढ़ाव को शांत करने के लिए डॉलर ख़रीदता या बेचता है। "
  "कथन 1 गलत है: 1992 की उदारीकृत विनिमय दर प्रबंधन प्रणाली (LERMS) और 1993 की एकीकृत बाज़ार दर के साथ भारत ने स्थिर और टोकरी-आधारित प्रणालियाँ छोड़ दीं। "
  "कथन 3 गलत है: कोई प्राधिकरण दर तय नहीं करता; यह अंतर-बैंक बाज़ार में माँग और आपूर्ति से तय होती है, यद्यपि RBI एक संदर्भ दर प्रकाशित करता है।",
  f"{RBI} -- Foreign exchange market operations; {NCM}.",
  "ex-rupee-managed-float")

S(EX, "medium", "Consider the following statements about a depreciation of the rupee:",
  "रुपये के मूल्यह्रास (depreciation) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It makes Indian exports cheaper for foreign buyers.",
   "It makes imported crude oil costlier in rupee terms.",
   "It reduces the rupee value of India's external debt."],
  ["यह विदेशी ख़रीदारों के लिए भारतीय निर्यात को सस्ता बनाता है।",
   "यह रुपये के रूप में आयातित कच्चे तेल को महँगा बनाता है।",
   "यह भारत के बाहरी ऋण के रुपया मूल्य को घटाता है।"],
  C3, 1,
  "Statements 1 and 2 are correct: a weaker rupee helps exporters and hurts importers, and because India imports most of its oil, it also feeds inflation. "
  "Statement 3 is wrong: external debt is owed mostly in dollars, so when the rupee falls, more rupees are needed to repay it -- the rupee value of the debt rises, which is why firms with unhedged foreign loans suffer.",
  "कथन 1 और 2 सही हैं: कमज़ोर रुपया निर्यातकों की मदद करता है और आयातकों को हानि पहुँचाता है, और चूँकि भारत अपना अधिकांश तेल आयात करता है, यह मुद्रास्फीति भी बढ़ाता है। "
  "कथन 3 गलत है: बाहरी ऋण अधिकतर डॉलर में होता है, इसलिए रुपया गिरने पर उसे चुकाने के लिए अधिक रुपये चाहिए; ऋण का रुपया मूल्य बढ़ता है, इसीलिए बिना हेज किए विदेशी ऋण वाली कंपनियों को हानि होती है।",
  f"{NCM}.",
  "ex-depreciation-effects")

S(EX, "medium", "Consider the following statements about the convertibility of the rupee:",
  "रुपये की परिवर्तनीयता के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The rupee has been convertible on the current account since 1994.",
   "India has full capital account convertibility.",
   "Current account convertibility means that residents may buy foreign assets freely without any limit."],
  ["1994 से रुपया चालू खाते पर परिवर्तनीय है।",
   "भारत में पूर्ण पूँजी खाता परिवर्तनीयता है।",
   "चालू खाता परिवर्तनीयता का अर्थ है कि निवासी बिना किसी सीमा के स्वतंत्र रूप से विदेशी परिसंपत्तियाँ ख़रीद सकते हैं।"],
  C3, 0,
  "Only statement 1 is correct: in August 1994 India accepted the obligations of Article VIII of the IMF's Articles, so rupees can be freely converted for trade, travel, education and other current payments. "
  "Statement 2 is wrong: capital account convertibility is partial -- foreign investment, external borrowing and residents' investment abroad remain subject to limits. "
  "Statement 3 is wrong: that describes capital account convertibility; current account convertibility covers payments for goods, services and transfers, not the purchase of foreign assets.",
  "केवल कथन 1 सही है: अगस्त 1994 में भारत ने IMF के अनुच्छेदों के अनुच्छेद VIII के दायित्व स्वीकार किए, इसलिए व्यापार, यात्रा, शिक्षा और अन्य चालू भुगतानों के लिए रुपये स्वतंत्र रूप से बदले जा सकते हैं। "
  "कथन 2 गलत है: पूँजी खाता परिवर्तनीयता आंशिक है; विदेशी निवेश, बाहरी उधार और निवासियों का विदेश में निवेश सीमाओं के अधीन हैं। "
  "कथन 3 गलत है: यह पूँजी खाता परिवर्तनीयता का वर्णन है; चालू खाता परिवर्तनीयता वस्तुओं, सेवाओं और हस्तांतरणों के भुगतानों को शामिल करती है, विदेशी परिसंपत्तियों की ख़रीद को नहीं।",
  f"{RBI} -- Foreign Exchange Management; International Monetary Fund -- Article VIII.",
  "ex-rupee-convertibility")

S(EX, "medium", "Consider the following statements about India's foreign direct investment (FDI) policy:",
  "भारत की प्रत्यक्ष विदेशी निवेश (FDI) नीति के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Under the automatic route, no prior approval of the government is needed.",
   "FDI is prohibited in the lottery business and in gambling and betting.",
   "Investors from countries sharing a land border with India may invest under the automatic route in every sector."],
  ["स्वचालित मार्ग के तहत सरकार की पूर्व अनुमति की आवश्यकता नहीं होती।",
   "लॉटरी व्यवसाय और जुए तथा सट्टेबाज़ी में FDI निषिद्ध है।",
   "भारत से स्थलीय सीमा साझा करने वाले देशों के निवेशक हर क्षेत्र में स्वचालित मार्ग से निवेश कर सकते हैं।"],
  C3, 1,
  "Statements 1 and 2 are correct. Most sectors are open under the automatic route, where the investor informs the RBI after the investment; a short list, which also includes chit funds, Nidhi companies, real estate business and cigarettes, is closed. "
  "Statement 3 is wrong: under Press Note 3 of 2020, issued amid the pandemic to prevent opportunistic takeovers, any investment from a country sharing a land border with India -- including China -- needs government approval.",
  "कथन 1 और 2 सही हैं। अधिकांश क्षेत्र स्वचालित मार्ग के तहत खुले हैं, जहाँ निवेशक निवेश के बाद RBI को सूचित करता है; एक छोटी सूची बंद है, जिसमें चिट फ़ंड, निधि कंपनियाँ, रियल एस्टेट व्यवसाय और सिगरेट भी हैं। "
  "कथन 3 गलत है: महामारी के बीच अवसरवादी अधिग्रहण रोकने के लिए जारी 2020 के प्रेस नोट 3 के तहत, भारत से स्थलीय सीमा साझा करने वाले किसी भी देश, जिसमें चीन भी है, से आने वाले निवेश के लिए सरकार की अनुमति चाहिए।",
  "Department for Promotion of Industry and Internal Trade -- Consolidated FDI Policy; Press Note 3 (2020).",
  "ex-fdi-policy-routes")

S(EX, "medium", "Consider the following statements comparing foreign direct and portfolio investment:",
  "प्रत्यक्ष और पोर्टफ़ोलियो विदेशी निवेश की तुलना करने वाले निम्नलिखित कथनों पर विचार कीजिए:",
  ["A foreign investment of 10 per cent or more of the equity of a listed Indian company is treated as FDI.",
   "Foreign portfolio investment is generally more volatile than FDI.",
   "FDI usually brings management control and technology along with capital."],
  ["किसी सूचीबद्ध भारतीय कंपनी की इक्विटी के 10 प्रतिशत या अधिक का विदेशी निवेश FDI माना जाता है।",
   "विदेशी पोर्टफ़ोलियो निवेश सामान्यतः FDI से अधिक अस्थिर होता है।",
   "FDI प्रायः पूँजी के साथ प्रबंधन नियंत्रण और प्रौद्योगिकी भी लाता है।"],
  C3, 2,
  "All three statements are correct. Below the 10 per cent line a foreign holding in a listed company counts as portfolio investment. Portfolio money can leave a stock market within days when global conditions change, whereas a factory or a subsidiary cannot easily be sold off, so FDI is the steadier and more valued way to finance a current account deficit.",
  "तीनों कथन सही हैं। 10 प्रतिशत की सीमा से नीचे किसी सूचीबद्ध कंपनी में विदेशी हिस्सेदारी पोर्टफ़ोलियो निवेश मानी जाती है। वैश्विक परिस्थितियाँ बदलने पर पोर्टफ़ोलियो पैसा कुछ ही दिनों में शेयर बाज़ार से निकल सकता है, जबकि किसी कारख़ाने या सहायक कंपनी को आसानी से बेचा नहीं जा सकता; इसलिए चालू खाते के घाटे की भरपाई का FDI अधिक स्थिर और अधिक मूल्यवान तरीक़ा है।",
  "Department for Promotion of Industry and Internal Trade -- Consolidated FDI Policy; Ministry of Finance.",
  "ex-fdi-vs-fpi")

S(EX, "medium", "Consider the following statements about the Foreign Exchange Management Act (FEMA), 1999:",
  "विदेशी मुद्रा प्रबंधन अधिनियम (FEMA), 1999 के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It replaced the Foreign Exchange Regulation Act (FERA).",
   "Violations under FEMA are treated as civil offences.",
   "FEMA is enforced by the Central Bureau of Investigation."],
  ["इसने विदेशी मुद्रा विनियमन अधिनियम (FERA) का स्थान लिया।",
   "FEMA के तहत उल्लंघन सिविल अपराध माने जाते हैं।",
   "FEMA को केंद्रीय अन्वेषण ब्यूरो (CBI) लागू करता है।"],
  C3, 1,
  "Statements 1 and 2 are correct. FERA, a 1973 law made in an era of foreign-exchange scarcity, treated violations as criminal offences; FEMA, in force from June 2000, aims at 'facilitating external trade and payments' and orderly markets, with penalties rather than prosecution for most breaches. "
  "Statement 3 is wrong: FEMA is enforced by the Directorate of Enforcement under the Department of Revenue, while the RBI frames the regulations under it.",
  "कथन 1 और 2 सही हैं। विदेशी मुद्रा की कमी के दौर में बने 1973 के क़ानून FERA में उल्लंघन आपराधिक अपराध थे; जून 2000 से लागू FEMA का उद्देश्य 'बाहरी व्यापार और भुगतानों को सुगम बनाना' और व्यवस्थित बाज़ार है, जिसमें अधिकांश उल्लंघनों पर अभियोजन के बजाय जुर्माना है। "
  "कथन 3 गलत है: FEMA को राजस्व विभाग के तहत प्रवर्तन निदेशालय लागू करता है, जबकि इसके तहत विनियम RBI बनाता है।",
  "Foreign Exchange Management Act, 1999; Directorate of Enforcement.",
  "ex-fema")

S(EX, "medium", "Consider the following statements about the Liberalised Remittance Scheme (LRS):",
  "उदारीकृत धन-प्रेषण योजना (LRS) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Under the LRS, a resident individual may remit up to 250,000 US dollars in a financial year.",
   "Money sent under the LRS may be used to buy lottery tickets abroad.",
   "The LRS is available to companies and partnership firms."],
  ["LRS के तहत एक निवासी व्यक्ति एक वित्तीय वर्ष में 2,50,000 अमेरिकी डॉलर तक भेज सकता है।",
   "LRS के तहत भेजे गए पैसे से विदेश में लॉटरी टिकट ख़रीदे जा सकते हैं।",
   "LRS कंपनियों और साझेदारी फ़र्मों के लिए उपलब्ध है।"],
  C3, 0,
  "Only statement 1 is correct: resident individuals may send money abroad for education, travel, medical treatment, gifts and investment in shares or property, up to the annual limit, with tax collected at source above a threshold. "
  "Statement 2 is wrong: remittances for lottery tickets, sweepstakes, racing and banned magazines are prohibited. "
  "Statement 3 is wrong: the scheme is only for resident individuals, including minors through their guardians; companies invest abroad under the separate overseas investment rules.",
  "केवल कथन 1 सही है: निवासी व्यक्ति शिक्षा, यात्रा, चिकित्सा, उपहार और शेयरों या संपत्ति में निवेश के लिए वार्षिक सीमा तक विदेश पैसा भेज सकते हैं, और एक सीमा से ऊपर स्रोत पर कर एकत्र होता है। "
  "कथन 2 गलत है: लॉटरी टिकट, स्वीपस्टेक, घुड़दौड़ और प्रतिबंधित पत्रिकाओं के लिए धन-प्रेषण निषिद्ध है। "
  "कथन 3 गलत है: यह योजना केवल निवासी व्यक्तियों के लिए है, जिनमें अभिभावकों के ज़रिए नाबालिग भी शामिल हैं; कंपनियाँ अलग विदेशी निवेश नियमों के तहत विदेश में निवेश करती हैं।",
  f"{RBI} -- Master Direction on the Liberalised Remittance Scheme.",
  "ex-liberalised-remittance-scheme")

S(EX, "medium", "Consider the following statements about trade remedies in India:",
  "भारत में व्यापार उपचारों (trade remedies) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Anti-dumping duty may be imposed when goods are exported to India at less than their normal value and injure domestic industry.",
   "The Directorate General of Trade Remedies recommends such duties, and the Ministry of Finance imposes them.",
   "Countervailing duty is imposed to offset the effect of dumping."],
  ["जब वस्तुएँ अपने सामान्य मूल्य से कम पर भारत को निर्यात की जाएँ और घरेलू उद्योग को हानि पहुँचाएँ, तो पाटनरोधी (anti-dumping) शुल्क लगाया जा सकता है।",
   "व्यापार उपचार महानिदेशालय (DGTR) ऐसे शुल्कों की सिफ़ारिश करता है, और वित्त मंत्रालय उन्हें लगाता है।",
   "प्रतिकारी शुल्क (countervailing duty) पाटन के प्रभाव की भरपाई के लिए लगाया जाता है।"],
  C3, 1,
  "Statements 1 and 2 are correct. After an investigation by the DGTR, under the Commerce Ministry, the Finance Ministry notifies duties that are permitted under WTO rules; steel, chemicals and solar glass from China are frequent targets. "
  "Statement 3 is wrong: a countervailing duty offsets subsidies given by the exporting country's government; dumping is met with anti-dumping duty, and a sudden surge of imports with a safeguard duty.",
  "कथन 1 और 2 सही हैं। वाणिज्य मंत्रालय के अंतर्गत DGTR की जाँच के बाद वित्त मंत्रालय WTO नियमों के तहत अनुमत शुल्क अधिसूचित करता है; चीन से आने वाले इस्पात, रसायन और सौर काँच इसके प्रायः निशाने होते हैं। "
  "कथन 3 गलत है: प्रतिकारी शुल्क निर्यातक देश की सरकार द्वारा दी गई सब्सिडी की भरपाई करता है; पाटन का जवाब पाटनरोधी शुल्क से, और आयात में अचानक उछाल का जवाब रक्षोपाय (safeguard) शुल्क से दिया जाता है।",
  "Directorate General of Trade Remedies; Customs Tariff Act, 1975, sections 8B, 9 and 9A.",
  "ex-trade-remedies")

S(EX, "medium", "Consider the following statements about the Foreign Trade Policy, 2023:",
  "विदेश व्यापार नीति, 2023 के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is valid for a fixed period of five years.",
   "It is issued by the RBI.",
   "It sets a target of 5 trillion dollars of exports by 2030."],
  ["यह पाँच वर्ष की निश्चित अवधि के लिए मान्य है।",
   "इसे RBI जारी करता है।",
   "यह 2030 तक 5 ट्रिलियन डॉलर के निर्यात का लक्ष्य रखती है।"],
  C3, 3,
  "None of the statements is correct. Unlike earlier five-year policies, the Foreign Trade Policy that took effect on 1 April 2023 has no end date and is updated as needed; it is issued by the Directorate General of Foreign Trade in the Commerce Ministry. Its target is exports of goods and services worth 2 trillion dollars by 2030; 5 trillion dollars is the size the government has aimed for the whole economy.",
  "कोई भी कथन सही नहीं है। पहले की पंचवर्षीय नीतियों के विपरीत, 1 अप्रैल 2023 से लागू विदेश व्यापार नीति की कोई अंतिम तिथि नहीं है और आवश्यकता के अनुसार इसे अद्यतन किया जाता है; इसे वाणिज्य मंत्रालय का विदेश व्यापार महानिदेशालय जारी करता है। इसका लक्ष्य 2030 तक 2 ट्रिलियन डॉलर की वस्तुओं और सेवाओं का निर्यात है; 5 ट्रिलियन डॉलर वह आकार है जिसका लक्ष्य सरकार ने पूरी अर्थव्यवस्था के लिए रखा है।",
  f"{DGFT} -- Foreign Trade Policy, 2023.",
  "ex-foreign-trade-policy-2023")

S(EX, "medium", "Consider the following statements about Special Economic Zones (SEZs):",
  "विशेष आर्थिक क्षेत्रों (SEZ) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["SEZs in India are governed by the Special Economic Zones Act, 2005.",
   "Goods sent from an SEZ into the rest of India are treated as exports.",
   "Units in an SEZ must sell all their output within India."],
  ["भारत में SEZ विशेष आर्थिक क्षेत्र अधिनियम, 2005 से नियंत्रित होते हैं।",
   "SEZ से शेष भारत में भेजी गई वस्तुएँ निर्यात मानी जाती हैं।",
   "SEZ की इकाइयों को अपना पूरा उत्पादन भारत के भीतर ही बेचना होता है।"],
  C3, 0,
  "Only statement 1 is correct: SEZs are treated as foreign territory for customs purposes, so their units import inputs duty-free. "
  "Statement 2 is wrong: goods moving from an SEZ into the domestic tariff area are treated as imports and pay customs duty -- which is exactly why the zones are deemed to be outside India's customs territory. "
  "Statement 3 is wrong: SEZ units are export-oriented; they may sell in India only on payment of duty, and are expected to be net earners of foreign exchange.",
  "केवल कथन 1 सही है: सीमा शुल्क के प्रयोजन से SEZ को विदेशी क्षेत्र माना जाता है, इसलिए इनकी इकाइयाँ आदान शुल्क-मुक्त आयात करती हैं। "
  "कथन 2 गलत है: SEZ से घरेलू टैरिफ़ क्षेत्र में जाने वाली वस्तुएँ आयात मानी जाती हैं और उन पर सीमा शुल्क लगता है; ठीक इसी कारण इन क्षेत्रों को भारत के सीमा शुल्क क्षेत्र से बाहर माना जाता है। "
  "कथन 3 गलत है: SEZ इकाइयाँ निर्यात-उन्मुख हैं; वे केवल शुल्क चुकाकर भारत में बेच सकती हैं, और उनसे विदेशी मुद्रा की शुद्ध अर्जक होने की अपेक्षा है।",
  "Special Economic Zones Act, 2005; Ministry of Commerce and Industry.",
  "ex-special-economic-zones")

S(EX, "medium", "Consider the following statements about the international use of the rupee:",
  "रुपये के अंतरराष्ट्रीय उपयोग के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["In 2022 the RBI allowed Special Rupee Vostro Accounts so that trade could be invoiced and settled in rupees.",
   "UPI can now be used to make payments in some other countries, such as the UAE, Singapore and France.",
   "A fully internationalised currency is widely used to invoice trade and to hold as reserves."],
  ["2022 में RBI ने विशेष रुपया वोस्ट्रो खातों की अनुमति दी, ताकि व्यापार के बिल रुपये में बन सकें और निपटान रुपये में हो सके।",
   "अब UPI का उपयोग कुछ अन्य देशों, जैसे UAE, सिंगापुर और फ़्रांस, में भुगतान के लिए किया जा सकता है।",
   "पूरी तरह अंतरराष्ट्रीयकृत मुद्रा का व्यापार के बिलों और भंडार के रूप में व्यापक उपयोग होता है।"],
  C3, 2,
  "All three statements are correct. Vostro accounts -- rupee accounts that Indian banks hold for foreign partner banks -- let exporters and importers settle trade without converting through the dollar, which helped trade with countries such as Russia and the UAE. Wider rupee use would cut currency risk for Indian firms, but full internationalisation would require deeper, more open capital markets.",
  "तीनों कथन सही हैं। वोस्ट्रो खाते, यानी वे रुपया खाते जो भारतीय बैंक विदेशी साझेदार बैंकों के लिए रखते हैं, निर्यातकों और आयातकों को डॉलर के ज़रिए बदले बिना व्यापार का निपटान करने देते हैं, जिससे रूस और UAE जैसे देशों के साथ व्यापार में मदद मिली। रुपये का व्यापक उपयोग भारतीय कंपनियों का मुद्रा जोखिम घटाएगा, पर पूर्ण अंतरराष्ट्रीयकरण के लिए अधिक गहरे और खुले पूँजी बाज़ार चाहिए।",
  f"{RBI} -- International Trade Settlement in Indian Rupees (2022); Report of the Inter-Departmental Group on Internationalisation of INR (2023).",
  "ex-rupee-internationalisation")

# ================================================================ EASY STATEMENTS (5)
S(EX, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Exports bring foreign exchange into a country.",
   "Imports earn foreign exchange for a country."],
  ["निर्यात किसी देश में विदेशी मुद्रा लाते हैं।",
   "आयात किसी देश के लिए विदेशी मुद्रा अर्जित करते हैं।"],
  T2, 0,
  "Only statement 1 is correct. Statement 2 is wrong: imports have to be paid for, so they use up foreign exchange.",
  "केवल कथन 1 सही है। कथन 2 गलत है: आयात का भुगतान करना पड़ता है, इसलिए वे विदेशी मुद्रा ख़र्च करते हैं।",
  f"{NCM}.",
  "ex-exports-imports-forex-easy")

S(EX, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Indian currency notes are issued by the Ministry of Commerce.",
   "A trade deficit means that a country's imports exceed its exports."],
  ["भारतीय करेंसी नोट वाणिज्य मंत्रालय जारी करता है।",
   "व्यापार घाटे का अर्थ है कि किसी देश का आयात उसके निर्यात से अधिक है।"],
  T2, 1,
  "Only statement 2 is correct. Statement 1 is wrong: currency notes are issued by the Reserve Bank of India; the Commerce Ministry deals with trade policy.",
  "केवल कथन 2 सही है। कथन 1 गलत है: करेंसी नोट भारतीय रिज़र्व बैंक जारी करता है; वाणिज्य मंत्रालय व्यापार नीति देखता है।",
  f"{NCM}.",
  "ex-trade-deficit-easy")

S(EX, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Tariffs are taxes on imports.",
   "Quotas limit the quantity of a good that can be imported."],
  ["टैरिफ़ आयात पर लगने वाले कर हैं।",
   "कोटा किसी वस्तु की आयात की जा सकने वाली मात्रा को सीमित करता है।"],
  T2, 2,
  "Both statements are correct. Both protect domestic producers from foreign competition; a tariff raises the price of imports, while a quota caps their volume directly.",
  "दोनों कथन सही हैं। दोनों घरेलू उत्पादकों को विदेशी प्रतिस्पर्धा से बचाते हैं; टैरिफ़ आयात की क़ीमत बढ़ाता है, जबकि कोटा सीधे उनकी मात्रा सीमित करता है।",
  f"{NCM}.",
  "ex-tariffs-quotas-easy")

S(EX, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["When the rupee depreciates against the dollar, one dollar buys more rupees.",
   "A stronger rupee makes foreign travel costlier for Indians."],
  ["जब डॉलर के मुक़ाबले रुपये का मूल्यह्रास होता है, तो एक डॉलर से अधिक रुपये मिलते हैं।",
   "मज़बूत रुपया भारतीयों के लिए विदेश यात्रा को महँगा बनाता है।"],
  T2, 0,
  "Only statement 1 is correct. Statement 2 is wrong: when the rupee is stronger, each rupee buys more foreign currency, so hotels, fees and tickets abroad cost Indians less.",
  "केवल कथन 1 सही है। कथन 2 गलत है: जब रुपया मज़बूत होता है, तो हर रुपये से अधिक विदेशी मुद्रा मिलती है, इसलिए विदेश में होटल, शुल्क और टिकट भारतीयों को सस्ते पड़ते हैं।",
  f"{NCM}.",
  "ex-rupee-depreciation-easy")

S(EX, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The United States is the largest source of foreign direct investment into India.",
   "Gold is one of India's major imports."],
  ["संयुक्त राज्य अमेरिका भारत में प्रत्यक्ष विदेशी निवेश का सबसे बड़ा स्रोत है।",
   "सोना भारत के प्रमुख आयातों में से एक है।"],
  T2, 1,
  "Only statement 2 is correct: India is one of the world's largest buyers of gold, which, with crude oil and electronics, is among its biggest import items. Statement 1 is wrong: Singapore and Mauritius have been the largest sources of FDI into India, partly because many global investors route money through them; the United States comes after them.",
  "केवल कथन 2 सही है: भारत विश्व में सोने के सबसे बड़े ख़रीदारों में से है, और कच्चे तेल तथा इलेक्ट्रॉनिक्स के साथ सोना उसकी सबसे बड़ी आयात मदों में है। कथन 1 गलत है: भारत में FDI के सबसे बड़े स्रोत सिंगापुर और मॉरीशस रहे हैं, कुछ हद तक इसलिए कि कई वैश्विक निवेशक अपना पैसा इनके रास्ते भेजते हैं; संयुक्त राज्य अमेरिका इनके बाद आता है।",
  f"{NCM}.",
  "ex-fdi-source-gold-easy")

# ================================================================ HARD STATEMENTS (5)
S(EX, "hard", "Consider the following statements about the 'impossible trinity':",
  "'असंभव त्रयी' (impossible trinity) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["A country cannot at the same time have a fixed exchange rate, free movement of capital and an independent monetary policy.",
   "India's managed float with some capital controls is one way of keeping room for an independent monetary policy.",
   "The trilemma applies only to countries that have no central bank."],
  ["कोई देश एक साथ स्थिर विनिमय दर, पूँजी की स्वतंत्र आवाजाही और स्वतंत्र मौद्रिक नीति नहीं रख सकता।",
   "कुछ पूँजी नियंत्रणों के साथ भारत का प्रबंधित अस्थिर विनिमय दर स्वतंत्र मौद्रिक नीति की गुंजाइश बनाए रखने का एक तरीक़ा है।",
   "यह त्रिदुविधा (trilemma) केवल उन देशों पर लागू होती है जिनके पास केंद्रीय बैंक नहीं है।"],
  C3, 1,
  "Statements 1 and 2 are correct. With free capital flows, a central bank that tries to hold both an exchange-rate peg and its own interest rate will see money rush in or out until one of the two gives way; Hong Kong keeps the peg and gives up monetary independence, while India lets the rupee move within limits and keeps some controls. "
  "Statement 3 is wrong: the trilemma is precisely a constraint on central banks' choices; a country without one has no monetary policy to protect.",
  "कथन 1 और 2 सही हैं। पूँजी के स्वतंत्र प्रवाह के साथ, जो केंद्रीय बैंक विनिमय दर की स्थिरता और अपनी ब्याज दर, दोनों को थामे रखना चाहे, वहाँ पैसा तब तक आता-जाता रहेगा जब तक इनमें से कोई एक टूट न जाए; हांगकांग स्थिरता बनाए रखता है और मौद्रिक स्वतंत्रता छोड़ देता है, जबकि भारत रुपये को सीमाओं के भीतर चलने देता है और कुछ नियंत्रण रखता है। "
  "कथन 3 गलत है: यह त्रिदुविधा ठीक केंद्रीय बैंकों के विकल्पों पर एक बाध्यता है; जिस देश के पास केंद्रीय बैंक ही नहीं, उसके पास बचाने के लिए कोई मौद्रिक नीति नहीं है।",
  f"{RBI} -- Annual Report; {NCM}.",
  "ex-impossible-trinity")

S(EX, "hard", "Consider the following statements about exchange rates and the trade balance:",
  "विनिमय दरों और व्यापार संतुलन के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["After a depreciation, the trade balance may first worsen and only later improve.",
   "The Marshall-Lerner condition says that a depreciation improves the trade balance if the sum of the price elasticities of export and import demand is less than one.",
   "A country's terms of trade improve when its import prices rise faster than its export prices."],
  ["मूल्यह्रास के बाद व्यापार संतुलन पहले बिगड़ सकता है और बाद में ही सुधर सकता है।",
   "मार्शल-लर्नर शर्त कहती है कि यदि निर्यात और आयात माँग की मूल्य लोचों का योग एक से कम हो, तो मूल्यह्रास व्यापार संतुलन को सुधारता है।",
   "जब किसी देश की आयात क़ीमतें उसकी निर्यात क़ीमतों से तेज़ी से बढ़ती हैं, तो उसकी व्यापार की शर्तें (terms of trade) सुधरती हैं।"],
  C3, 0,
  "Only statement 1 is correct: this is the J-curve -- import and export volumes take time to adjust to new prices, so at first the country simply pays more for the same imports. "
  "Statement 2 is wrong: the condition requires the sum of the elasticities to be greater than one; if demand is inelastic, a cheaper currency brings in less foreign exchange, not more. "
  "Statement 3 is wrong: the terms of trade are export prices relative to import prices, so they worsen when import prices rise faster -- as for India when oil prices jump.",
  "केवल कथन 1 सही है: यह J-वक्र है; आयात और निर्यात की मात्राओं को नई क़ीमतों के अनुसार ढलने में समय लगता है, इसलिए शुरू में देश उन्हीं आयातों के लिए अधिक भुगतान करता है। "
  "कथन 2 गलत है: इस शर्त में लोचों का योग एक से अधिक होना चाहिए; यदि माँग बेलोच है, तो सस्ती मुद्रा अधिक नहीं, कम विदेशी मुद्रा लाती है। "
  "कथन 3 गलत है: व्यापार की शर्तें आयात क़ीमतों की तुलना में निर्यात क़ीमतें हैं, इसलिए आयात क़ीमतें तेज़ी से बढ़ने पर वे बिगड़ती हैं, जैसा तेल की क़ीमतें उछलने पर भारत के साथ होता है।",
  f"{NCM}.",
  "ex-j-curve-marshall-lerner-tot")

S(EX, "hard", "Consider the following statements about effective exchange rates:",
  "प्रभावी विनिमय दरों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The real effective exchange rate (REER) adjusts the nominal effective exchange rate for differences in inflation.",
   "A rise in the REER index indicates a real appreciation of the rupee.",
   "The nominal effective exchange rate (NEER) is calculated against the US dollar alone."],
  ["वास्तविक प्रभावी विनिमय दर (REER) नाममात्र प्रभावी विनिमय दर को मुद्रास्फीति के अंतरों के लिए समायोजित करती है।",
   "REER सूचकांक में वृद्धि रुपये के वास्तविक अधिमूल्यन (appreciation) को दर्शाती है।",
   "नाममात्र प्रभावी विनिमय दर (NEER) केवल अमेरिकी डॉलर के मुक़ाबले गणना की जाती है।"],
  C3, 1,
  "Statements 1 and 2 are correct. If Indian inflation runs above that of trading partners, the rupee can lose competitiveness even while its nominal rate is steady -- the REER captures this, and a REER well above 100 suggests the rupee is overvalued. "
  "Statement 3 is wrong: effective rates are trade-weighted averages against a basket of partner currencies -- the RBI publishes 40-currency and 6-currency indices -- not against one currency.",
  "कथन 1 और 2 सही हैं। यदि भारतीय मुद्रास्फीति व्यापारिक साझेदारों से ऊपर चलती है, तो नाममात्र दर स्थिर रहते हुए भी रुपया प्रतिस्पर्धा खो सकता है; REER इसे पकड़ती है, और 100 से काफ़ी ऊपर का REER संकेत देता है कि रुपया अधिमूल्यित है। "
  "कथन 3 गलत है: प्रभावी दरें साझेदार मुद्राओं की एक टोकरी के मुक़ाबले व्यापार-भारित औसत होती हैं; RBI 40-मुद्रा और 6-मुद्रा सूचकांक प्रकाशित करता है, किसी एक मुद्रा के मुक़ाबले नहीं।",
  f"{RBI} -- Indices of Nominal and Real Effective Exchange Rate.",
  "ex-neer-reer")

S(EX, "hard", "Consider the following statements about India's external debt:",
  "भारत के बाहरी ऋण के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Commercial borrowings are the largest component of India's external debt.",
   "Most of India's external debt is long-term.",
   "The US dollar is the largest currency of denomination of India's external debt."],
  ["वाणिज्यिक उधार भारत के बाहरी ऋण का सबसे बड़ा घटक है।",
   "भारत का अधिकांश बाहरी ऋण दीर्घकालिक है।",
   "भारत के बाहरी ऋण में अमेरिकी डॉलर सबसे बड़ी मूल्यवर्ग मुद्रा है।"],
  C3, 2,
  "All three statements are correct. Commercial borrowings, NRI deposits and short-term trade credit are the main components, and more than half of the debt is in dollars, with the rupee, yen, SDR and euro making up most of the rest; long-term debt is about four-fifths of the total. At under a fifth of GDP, the debt is moderate by international standards.",
  "तीनों कथन सही हैं। वाणिज्यिक उधार, NRI जमाएँ और अल्पकालिक व्यापार ऋण इसके मुख्य घटक हैं, और आधे से अधिक ऋण डॉलर में है, जबकि शेष का अधिकांश रुपया, येन, SDR और यूरो में है; दीर्घकालिक ऋण कुल का लगभग चार-पाँचवाँ भाग है। GDP के पाँचवें भाग से कम पर, यह ऋण अंतरराष्ट्रीय मानकों से मध्यम है।",
  "Ministry of Finance -- India's External Debt: A Status Report; RBI quarterly data.",
  "ex-external-debt-composition")

S(EX, "hard", "Consider the following statements about the current account deficit:",
  "चालू खाते के घाटे के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["A current account deficit means that domestic investment exceeds domestic saving.",
   "A current account deficit can be financed only by drawing down foreign exchange reserves.",
   "A country with a current account surplus must be a net debtor to the rest of the world."],
  ["चालू खाते के घाटे का अर्थ है कि घरेलू निवेश घरेलू बचत से अधिक है।",
   "चालू खाते के घाटे की भरपाई केवल विदेशी मुद्रा भंडार घटाकर ही की जा सकती है।",
   "चालू खाते में अधिशेष वाला देश अनिवार्य रूप से शेष विश्व का शुद्ध ऋणी होता है।"],
  C3, 0,
  "Only statement 1 is correct: from national accounts, the current account balance equals saving minus investment, so a deficit means the country is borrowing the rest of the world's saving to invest. "
  "Statement 2 is wrong: a deficit is normally financed by capital inflows -- FDI, portfolio investment, loans and NRI deposits -- and reserves are used only when these fall short. "
  "Statement 3 is wrong: a surplus country lends to or invests in the rest of the world and builds up claims on it -- China, Germany and Japan are large net creditors.",
  "केवल कथन 1 सही है: राष्ट्रीय लेखांकन से, चालू खाते का संतुलन बचत घटा निवेश के बराबर होता है, इसलिए घाटे का अर्थ है कि देश निवेश के लिए शेष विश्व की बचत उधार ले रहा है। "
  "कथन 2 गलत है: घाटे की भरपाई सामान्यतः पूँजी अंतर्वाह, यानी FDI, पोर्टफ़ोलियो निवेश, ऋण और NRI जमाओं, से होती है, और भंडार का उपयोग तभी होता है जब ये कम पड़ें। "
  "कथन 3 गलत है: अधिशेष वाला देश शेष विश्व को उधार देता है या उसमें निवेश करता है और उस पर दावे बनाता है; चीन, जर्मनी और जापान बड़े शुद्ध लेनदार हैं।",
  f"{NCM}.",
  "ex-cad-saving-investment")

# ================================================================ MCQs (medium 5, easy 1, hard 1)
M(EX, "medium", "Which one of the following is NOT a part of India's foreign exchange reserves?",
  "निम्नलिखित में से कौन-सा भारत के विदेशी मुद्रा भंडार का भाग नहीं है?",
  ["Deposits of non-resident Indians in Indian banks", "Gold held by the RBI", "Special Drawing Rights", "The reserve tranche position of India in the International Monetary Fund"],
  ["भारतीय बैंकों में अनिवासी भारतीयों की जमाएँ", "RBI के पास रखा सोना", "विशेष आहरण अधिकार (SDR)", "अंतरराष्ट्रीय मुद्रा कोष में भारत की आरक्षित किश्त (reserve tranche) स्थिति"],
  0,
  "The reserves are the external assets that the authorities control and can use at once: foreign currency assets, gold, SDRs and the reserve tranche in the IMF. NRI deposits are liabilities of Indian banks to non-residents -- part of the country's external debt, and a source of capital inflows, but not reserves.",
  "भंडार वे बाहरी परिसंपत्तियाँ हैं जिन पर अधिकारियों का नियंत्रण है और जिनका वे तुरंत उपयोग कर सकते हैं: विदेशी मुद्रा परिसंपत्तियाँ, सोना, SDR और IMF में आरक्षित किश्त। NRI जमाएँ अनिवासियों के प्रति भारतीय बैंकों की देयताएँ हैं; ये देश के बाहरी ऋण का भाग और पूँजी अंतर्वाह का स्रोत हैं, पर भंडार नहीं।",
  f"{RBI} -- Weekly Statistical Supplement (foreign exchange reserves).",
  "ex-reserves-not-nri-deposits")

M(EX, "medium", "In recent years, which one of the following has been the largest source of India's imports?",
  "हाल के वर्षों में निम्नलिखित में से कौन भारत के आयात का सबसे बड़ा स्रोत रहा है?",
  ["China", "The United States", "The United Arab Emirates", "Russia"],
  ["चीन", "संयुक्त राज्य अमेरिका", "संयुक्त अरब अमीरात", "रूस"],
  0,
  "China supplies more of India's imports than any other country -- electronics, machinery, chemicals and solar components -- and India runs its largest bilateral trade deficit with it. The United States is India's largest export market; Russia rose sharply as a supplier after 2022 because of discounted crude oil.",
  "चीन भारत को किसी भी अन्य देश से अधिक आयात देता है, जैसे इलेक्ट्रॉनिक्स, मशीनरी, रसायन और सौर पुर्ज़े, और भारत का सबसे बड़ा द्विपक्षीय व्यापार घाटा उसी के साथ है। संयुक्त राज्य अमेरिका भारत का सबसे बड़ा निर्यात बाज़ार है; 2022 के बाद रियायती कच्चे तेल के कारण रूस आपूर्तिकर्ता के रूप में तेज़ी से ऊपर आया।",
  "Ministry of Commerce and Industry -- Export Import Data Bank.",
  "ex-largest-import-source-china")

M(EX, "medium", "The RoDTEP scheme is meant to:",
  "RoDTEP योजना किसलिए है?",
  ["refund taxes and duties embedded in exported products that are not refunded otherwise", "give exporters loans at a fixed rate of interest",
   "set minimum prices for agricultural exports", "restrict the export of essential commodities such as onions and wheat during domestic shortages"],
  ["निर्यात किए गए उत्पादों में अंतर्निहित उन करों और शुल्कों की वापसी करना जो अन्यथा वापस नहीं होते", "निर्यातकों को स्थिर ब्याज दर पर ऋण देना",
   "कृषि निर्यात के लिए न्यूनतम मूल्य तय करना", "घरेलू कमी के समय प्याज़ और गेहूँ जैसी आवश्यक वस्तुओं के निर्यात पर रोक लगाना"],
  0,
  "The Remission of Duties and Taxes on Exported Products scheme, introduced in 2021, reimburses central, State and local levies -- such as duty on fuel used in transport or electricity duty -- that stay locked in the cost of exports. It replaced the MEIS, whose export subsidies had been ruled inconsistent with WTO rules, because refunding embedded taxes is permitted.",
  "2021 में शुरू की गई निर्यातित उत्पादों पर शुल्कों और करों में छूट (RoDTEP) योजना उन केंद्रीय, राज्य और स्थानीय करों, जैसे परिवहन में प्रयुक्त ईंधन पर शुल्क या बिजली शुल्क, की प्रतिपूर्ति करती है जो निर्यात की लागत में बंद रह जाते हैं। इसने MEIS का स्थान लिया, जिसकी निर्यात सब्सिडी को WTO नियमों के प्रतिकूल ठहराया गया था, क्योंकि अंतर्निहित करों की वापसी की अनुमति है।",
  f"{DGFT} -- RoDTEP scheme.",
  "ex-rodtep")

M(EX, "medium", "'Hot money' refers to:",
  "'हॉट मनी' किसे कहते हैं?",
  ["short-term capital that moves quickly between countries in search of higher returns", "money earned through the export of goods",
   "currency printed by a central bank to finance a deficit", "long-term foreign direct investment in manufacturing plants and infrastructure in India"],
  ["वह अल्पकालिक पूँजी जो अधिक प्रतिफल की तलाश में देशों के बीच तेज़ी से आती-जाती है", "वस्तुओं के निर्यात से अर्जित पैसा",
   "घाटे के वित्तपोषण के लिए केंद्रीय बैंक द्वारा छापी गई मुद्रा", "भारत में विनिर्माण संयंत्रों और अवसंरचना में दीर्घकालिक प्रत्यक्ष विदेशी निवेश"],
  0,
  "Hot money -- mostly portfolio flows into shares, bonds and short-term deposits -- chases interest-rate and exchange-rate gains and can reverse suddenly, as in the 2013 'taper tantrum', when it pulled the rupee down sharply. Long-term FDI is the opposite of hot money.",
  "हॉट मनी, जो अधिकतर शेयरों, बॉन्डों और अल्पकालिक जमाओं में पोर्टफ़ोलियो प्रवाह है, ब्याज दर और विनिमय दर के लाभों के पीछे भागती है और अचानक पलट सकती है, जैसा 2013 के 'टेपर टैंट्रम' में हुआ, जब इसने रुपये को तेज़ी से नीचे खींचा। दीर्घकालिक FDI हॉट मनी के ठीक उलट है।",
  f"{RBI} -- Annual Report 2013-14.",
  "ex-hot-money")

M(EX, "medium", "The term 'Dutch disease' refers to:",
  "'डच रोग' (Dutch disease) शब्द किसे दर्शाता है?",
  ["the decline of manufacturing after a natural-resource export boom pushes up the exchange rate", "a fall in farm output caused by floods in low-lying countries",
   "an outbreak of disease among dairy cattle that cuts a country's exports of milk and cheese for years", "the flight of capital from a country after its banks collapse"],
  ["प्राकृतिक संसाधन निर्यात में उछाल से विनिमय दर बढ़ने के बाद विनिर्माण का पतन", "निचले देशों में बाढ़ से कृषि उत्पादन में गिरावट",
   "दुधारू पशुओं में ऐसी बीमारी का प्रकोप जो वर्षों तक किसी देश के दूध और पनीर के निर्यात को घटा दे", "बैंकों के ढहने के बाद किसी देश से पूँजी का पलायन"],
  0,
  "The term was coined after the Netherlands' gas discoveries of the 1960s: large resource earnings strengthen the currency and draw labour and capital into the booming sector, making other exports, especially manufactures, uncompetitive. It is why resource-rich countries often struggle to industrialise.",
  "यह शब्द 1960 के दशक में नीदरलैंड की गैस खोजों के बाद बना: संसाधनों से भारी कमाई मुद्रा को मज़बूत करती है और श्रम तथा पूँजी को उछाल वाले क्षेत्र में खींच लेती है, जिससे अन्य निर्यात, विशेषकर विनिर्मित वस्तुएँ, प्रतिस्पर्धा खो देते हैं। इसीलिए संसाधन-समृद्ध देश प्रायः औद्योगीकरण में संघर्ष करते हैं।",
  "International Monetary Fund -- Finance and Development.",
  "ex-dutch-disease")

M(EX, "easy", "Which one of the following would be recorded in India's merchandise trade?",
  "निम्नलिखित में से कौन-सा भारत के वस्तु (merchandise) व्यापार में दर्ज होगा?",
  ["Export of rice", "Export of software services", "Money sent home by a nurse working abroad", "Spending by foreign tourists in India"],
  ["चावल का निर्यात", "सॉफ़्टवेयर सेवाओं का निर्यात", "विदेश में काम करने वाली नर्स द्वारा घर भेजा गया पैसा", "भारत में विदेशी पर्यटकों का ख़र्च"],
  0,
  "Merchandise trade covers physical goods such as rice, oil or machinery. Software services and tourism are trade in services, and remittances are transfers; all three are 'invisibles' in the current account.",
  "वस्तु व्यापार में चावल, तेल या मशीनरी जैसी भौतिक वस्तुएँ आती हैं। सॉफ़्टवेयर सेवाएँ और पर्यटन सेवाओं का व्यापार हैं, और धन-प्रेषण हस्तांतरण हैं; ये तीनों चालू खाते में 'अदृश्य मदें' (invisibles) हैं।",
  f"{NCM}.",
  "ex-merchandise-trade-easy")

M(EX, "hard", "If the exchange rate moves from 80 to 88 rupees per US dollar, the rupee has:",
  "यदि विनिमय दर 80 से 88 रुपये प्रति अमेरिकी डॉलर हो जाए, तो रुपये का क्या हुआ?",
  ["depreciated by about 9 per cent against the dollar", "depreciated by 10 per cent against the dollar",
   "appreciated by 10 per cent against the dollar", "appreciated by about 9 per cent against the dollar"],
  ["डॉलर के मुक़ाबले लगभग 9 प्रतिशत मूल्यह्रास हुआ", "डॉलर के मुक़ाबले 10 प्रतिशत मूल्यह्रास हुआ",
   "डॉलर के मुक़ाबले 10 प्रतिशत अधिमूल्यन हुआ", "डॉलर के मुक़ाबले लगभग 9 प्रतिशत अधिमूल्यन हुआ"],
  0,
  "More rupees per dollar means the rupee has weakened. Its value in dollars falls from 1/80 to 1/88, a change of 80/88 - 1, about -9.1 per cent. The 10 per cent figure is the dollar's appreciation against the rupee (88/80 - 1) -- the trap, since the two percentages are not the same.",
  "प्रति डॉलर अधिक रुपये का अर्थ है कि रुपया कमज़ोर हुआ है। डॉलर में इसका मूल्य 1/80 से घटकर 1/88 हो जाता है, यानी 80/88 - 1, लगभग -9.1 प्रतिशत का परिवर्तन। 10 प्रतिशत का आँकड़ा रुपये के मुक़ाबले डॉलर का अधिमूल्यन (88/80 - 1) है; यही जाल है, क्योंकि दोनों प्रतिशत समान नहीं हैं।",
  f"{NCM}.",
  "ex-depreciation-numerical")

# ================================================================ STATEMENT-I/II (medium 4, easy 1, hard I/II/III 1)
A(EX, "medium",
  "A sharp rise in world crude oil prices tends to worsen India's current account balance.",
  "विश्व में कच्चे तेल की क़ीमतों में तेज़ वृद्धि भारत के चालू खाता शेष को बिगाड़ने की प्रवृत्ति रखती है।",
  "India imports most of the crude oil it consumes.",
  "भारत अपनी खपत का अधिकांश कच्चा तेल आयात करता है।",
  0,
  "Both statements are correct and Statement-II explains Statement-I. With imports meeting more than 85 per cent of its crude needs, India's import bill rises almost one-for-one with oil prices, while demand for fuel changes little in the short run.",
  "दोनों कथन सही हैं और कथन-II कथन-I की व्याख्या करता है। अपनी कच्चे तेल की 85 प्रतिशत से अधिक आवश्यकता आयात से पूरी होने के कारण, भारत का आयात बिल तेल की क़ीमतों के साथ लगभग उसी अनुपात में बढ़ता है, जबकि अल्पकाल में ईंधन की माँग बहुत कम बदलती है।",
  "Ministry of Petroleum and Natural Gas -- Petroleum Planning and Analysis Cell; RBI Balance of Payments.",
  "ex-oil-prices-cad")

A(EX, "medium",
  "India's exports of services have grown faster than its merchandise exports over the past decade.",
  "पिछले एक दशक में भारत के सेवा निर्यात उसके वस्तु निर्यात से तेज़ी से बढ़े हैं।",
  "India's services exports are dominated by receipts from foreign tourists.",
  "भारत के सेवा निर्यात में विदेशी पर्यटकों से प्राप्तियों का प्रभुत्व है।",
  2,
  "Statement-I is correct but Statement-II is incorrect. Services exports more than doubled in the decade to 2024-25, to nearly 390 billion dollars, while merchandise exports grew far more slowly. Software, IT-enabled and other business services -- much of them delivered from global capability centres in India -- make up the bulk; travel receipts are a small share.",
  "कथन-I सही है पर कथन-II गलत है। 2024-25 तक के दशक में सेवा निर्यात दोगुने से अधिक होकर लगभग 390 अरब डॉलर हो गए, जबकि वस्तु निर्यात कहीं धीमे बढ़े। इनका बड़ा भाग सॉफ़्टवेयर, IT-सक्षम और अन्य व्यावसायिक सेवाओं का है, जिनमें से बहुत-सी भारत के वैश्विक क्षमता केंद्रों (GCC) से दी जाती हैं; पर्यटन से प्राप्तियाँ छोटा हिस्सा हैं।",
  f"{RBI} -- Balance of Payments; Ministry of Commerce and Industry.",
  "ex-services-exports-growth")

A(EX, "medium",
  "Under a floating exchange rate system, the central bank must defend a fixed parity.",
  "अस्थिर (floating) विनिमय दर प्रणाली में केंद्रीय बैंक को एक स्थिर समता (parity) की रक्षा करनी होती है।",
  "Under a floating exchange rate system, the value of the currency is set mainly by demand and supply in the market.",
  "अस्थिर विनिमय दर प्रणाली में मुद्रा का मूल्य मुख्य रूप से बाज़ार में माँग और आपूर्ति से तय होता है।",
  3,
  "Statement-I is incorrect but Statement-II is correct. Defending a parity is the obligation of a fixed-rate system, as under Bretton Woods; a floating currency moves with trade and capital flows, although central banks may still step in, as the RBI does, to limit volatility.",
  "कथन-I गलत है पर कथन-II सही है। किसी समता की रक्षा स्थिर दर प्रणाली का दायित्व है, जैसे ब्रेटन वुड्स के तहत था; अस्थिर मुद्रा व्यापार और पूँजी प्रवाह के साथ चलती है, यद्यपि केंद्रीय बैंक उतार-चढ़ाव सीमित करने के लिए अब भी हस्तक्षेप कर सकते हैं, जैसा RBI करता है।",
  f"{NCM}.",
  "ex-floating-rate-parity")

A(EX, "medium",
  "The rupee tends to weaken when the US Federal Reserve raises interest rates sharply.",
  "जब अमेरिकी फ़ेडरल रिज़र्व ब्याज दरें तेज़ी से बढ़ाता है, तो रुपया कमज़ोर होने लगता है।",
  "The US dollar is the main currency in which world trade is invoiced.",
  "अमेरिकी डॉलर वह मुख्य मुद्रा है जिसमें विश्व व्यापार के बिल बनते हैं।",
  1,
  "Both statements are correct, but Statement-II does not explain Statement-I. The rupee weakens because higher US yields draw portfolio money out of emerging markets such as India and strengthen the dollar generally; the dollar's role in invoicing trade is a long-standing fact that does not change when the Fed raises rates.",
  "दोनों कथन सही हैं, पर कथन-II कथन-I की व्याख्या नहीं करता। रुपया इसलिए कमज़ोर होता है कि अमेरिका के ऊँचे प्रतिफल भारत जैसे उभरते बाज़ारों से पोर्टफ़ोलियो पैसा खींच लेते हैं और डॉलर को सामान्य रूप से मज़बूत करते हैं; व्यापार के बिलों में डॉलर की भूमिका एक पुराना तथ्य है, जो फ़ेड के दरें बढ़ाने से नहीं बदलता।",
  f"{RBI} -- Financial Stability Report.",
  "ex-fed-hikes-rupee")

A(EX, "easy",
  "India imports large quantities of edible oil.",
  "भारत बड़ी मात्रा में खाद्य तेल आयात करता है।",
  "Domestic production of oilseeds falls short of the country's demand for edible oil.",
  "तिलहन का घरेलू उत्पादन देश की खाद्य तेल की माँग से कम पड़ता है।",
  0,
  "Both statements are correct and Statement-II explains Statement-I. India buys more than half of its edible oil abroad -- mainly palm oil from Indonesia and Malaysia and soybean and sunflower oil -- which is why the government has launched missions to raise domestic oilseed and oil-palm output.",
  "दोनों कथन सही हैं और कथन-II कथन-I की व्याख्या करता है। भारत अपना आधे से अधिक खाद्य तेल विदेश से ख़रीदता है, मुख्य रूप से इंडोनेशिया और मलेशिया से पाम तेल तथा सोयाबीन और सूरजमुखी तेल; इसीलिए सरकार ने घरेलू तिलहन और ऑयल पाम उत्पादन बढ़ाने के मिशन शुरू किए हैं।",
  "Ministry of Agriculture and Farmers Welfare -- National Mission on Edible Oils.",
  "ex-edible-oil-imports-easy")

A(EX, "hard",
  "India's foreign exchange reserves rose sharply in years of heavy capital inflows.",
  "भारी पूँजी अंतर्वाह वाले वर्षों में भारत का विदेशी मुद्रा भंडार तेज़ी से बढ़ा।",
  "The RBI bought dollars in those years to keep the rupee from appreciating too much.",
  "उन वर्षों में RBI ने रुपये को बहुत अधिक अधिमूल्यित होने से रोकने के लिए डॉलर ख़रीदे।",
  1,
  "Both Statements II and III are correct, but only Statement II explains Statement I. When inflows exceed what the current account deficit absorbs, the RBI buys the surplus dollars rather than let the rupee soar and hurt exporters, and those purchases add to the reserves. "
  "Statement III is true -- safety and liquidity guide where the reserves are placed -- but it describes how they are invested, not why they grew when capital poured in.",
  "कथन II और III दोनों सही हैं, पर केवल कथन II कथन I की व्याख्या करता है। जब अंतर्वाह चालू खाते के घाटे की ज़रूरत से अधिक होते हैं, तो RBI रुपये को ऊँचा उछलने देने और निर्यातकों को हानि पहुँचाने के बजाय अतिरिक्त डॉलर ख़रीद लेता है, और ये ख़रीदें भंडार में जुड़ती हैं। "
  "कथन III सही है, भंडार कहाँ रखे जाएँ यह सुरक्षा और तरलता से तय होता है, पर यह बताता है कि उनका निवेश कैसे होता है, यह नहीं कि पूँजी की भारी आवक होने पर वे क्यों बढ़े।",
  f"{RBI} -- Annual Report; Half-yearly Report on Management of Foreign Exchange Reserves.",
  "ex-reserves-capital-inflows",
  s3="The RBI invests its foreign currency assets mainly in the securities of other governments and with other central banks.",
  s3_hi="RBI अपनी विदेशी मुद्रा परिसंपत्तियों का निवेश मुख्य रूप से दूसरी सरकारों की प्रतिभूतियों में और दूसरे केंद्रीय बैंकों के पास करता है।")

# ================================================================ PAIRS (hard 1)
P(EX, "hard", "Consider the following pairs of committees and the subjects they examined:",
  "समितियों और उनके द्वारा जाँचे गए विषयों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Sodhani Committee : Foreign exchange market", "Narasimham Committee : Banking sector reforms",
   "Raja Chelliah Committee : Tax reforms", "Urjit Patel Committee : External debt management"],
  ["सोढानी समिति : विदेशी मुद्रा बाज़ार", "नरसिम्हम समिति : बैंकिंग क्षेत्र सुधार",
   "राजा चेलैया समिति : कर सुधार", "उर्जित पटेल समिति : बाहरी ऋण प्रबंधन"],
  2,
  "Pairs 1, 2 and 3 are correct: O.P. Sodhani's Expert Group (1995) recommended steps to widen and deepen the foreign exchange market; M. Narasimham's committees (1991 and 1998) shaped banking reform, including prudential norms; and Raja Chelliah's Tax Reforms Committee (1991-93) laid out the simplification of direct and indirect taxes. "
  "Pair 4 is wrong: the Urjit Patel Committee (2014) recommended the monetary policy framework -- CPI-based inflation targeting and a monetary policy committee.",
  "युग्म 1, 2 और 3 सही हैं: ओ.पी. सोढानी के विशेषज्ञ समूह (1995) ने विदेशी मुद्रा बाज़ार को व्यापक और गहरा बनाने के उपाय सुझाए; एम. नरसिम्हम की समितियों (1991 और 1998) ने विवेकपूर्ण मानदंडों सहित बैंकिंग सुधार को आकार दिया; और राजा चेलैया की कर सुधार समिति (1991-93) ने प्रत्यक्ष और अप्रत्यक्ष करों के सरलीकरण की रूपरेखा दी। "
  "युग्म 4 गलत है: उर्जित पटेल समिति (2014) ने मौद्रिक नीति ढाँचे, यानी CPI-आधारित मुद्रास्फीति लक्ष्यीकरण और एक मौद्रिक नीति समिति, की सिफ़ारिश की।",
  f"{RBI} -- Reports of committees; Ministry of Finance.",
  "ex-committees-pairs")

if __name__ == "__main__":
    write("econ_l2_t16_bop_trade.sql")
