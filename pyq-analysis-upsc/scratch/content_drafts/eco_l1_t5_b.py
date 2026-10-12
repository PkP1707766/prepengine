# -*- coding: utf-8 -*-
"""Level 1 · Test 5 (Economy, NCERT Foundation) -- part B: Money, Banking & Monetary Policy (11), Macro Concepts,
National Income & Inflation (5) and Taxation & Fiscal Federalism (5) (upsc_l1_cell_targets.mjs 5).
Money: easy MCQ 1, easy statement 2, easy Statement-I/II 1, medium MCQ 1, medium statement 4, medium Statement-I/II 1,
hard statement 1. Macro: easy statement 1, medium MCQ 1, medium statement 2, hard statement 1. Taxation: easy
statement 1, medium MCQ 1, medium statement 2, medium Statement-I/II 1.
The angle is NCERT Class X 'Money and Credit', Class XII Introductory Macroeconomics (money, banks, national income,
the Keynesian revolution) and the basic structure of Indian taxes. Level-2 facts are not repeated (RBI functions and
the one-rupee note, repo and the corridor, CRR/SLR, the money multiplier, money-supply measures, MPC, NBFCs, SHGs,
GDP aggregates, what counts in GDP, inflation indices, the State-taxes count, GST basics and compensation, income-tax
regimes). MCQ keys are pinned (pos)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Economy"
d.REQUIRE_CRAFT = True
MB = "Money, Banking & Monetary Policy"
MC = "Macro Concepts, National Income & Inflation"
TX = "Taxation & Fiscal Federalism"
EC10 = "NCERT Class X, Economics -- Understanding Economic Development"
MAC = "NCERT Class XII, Economics -- Introductory Macroeconomics"
RBI = "Reserve Bank of India"

# ================================================================ MONEY & BANKING (11)
# ---------------------------------------------------------------- easy MCQ (1)
M(MB, "easy", "In a barter economy, a shoe-maker who wants wheat must find a farmer who not only sells wheat but also wants shoes in exchange. This difficulty is called",
  "वस्तु-विनिमय अर्थव्यवस्था में गेहूँ चाहने वाले एक मोची को ऐसा किसान ढूँढना पड़ता है जो न केवल गेहूँ बेचता हो बल्कि बदले में जूते भी चाहता हो। यह कठिनाई क्या कहलाती है?",
  ["the double coincidence of wants", "moral hazard in lending", "a liquidity trap", "adverse selection in markets that are thin"],
  ["आवश्यकताओं का दोहरा संयोग", "ऋण में नैतिक संकट (moral hazard)", "तरलता जाल", "कम सौदों वाले बाज़ारों में प्रतिकूल चयन"],
  0,
  "Barter requires a double coincidence of wants: each party must want what the other has to offer. Money removes this difficulty by acting as a medium of exchange -- the shoe-maker sells shoes for money and uses the money to buy wheat from anyone. "
  "Money also solves barter's other problems, giving a common unit for valuing goods and a way to store purchasing power.",
  "वस्तु-विनिमय के लिए आवश्यकताओं का दोहरा संयोग चाहिए: हर पक्ष को वह चाहिए जो दूसरा दे सकता है। मुद्रा विनिमय के माध्यम का काम करके यह कठिनाई दूर करती है -- मोची जूते मुद्रा के बदले बेचता है और उस मुद्रा से किसी से भी गेहूँ ख़रीदता है। "
  "मुद्रा वस्तु-विनिमय की अन्य समस्याएँ भी हल करती है, वस्तुओं के मूल्यांकन की एक साझा इकाई और क्रय-शक्ति संचित करने का तरीक़ा देकर।",
  f"{EC10} (Money and Credit).",
  "l1-eco-double-coincidence-of-wants", pos=3, craft="recall")

# ---------------------------------------------------------------- easy statement (2)
S(MB, "easy", "Consider the following statements about the functions of money:",
  "मुद्रा के कार्यों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Money serves as a medium of exchange.",
   "Money serves as a unit of account, in which the values of all goods and services can be expressed.",
   "Money cannot act as a store of value, since holding it earns no return."],
  ["मुद्रा विनिमय के माध्यम का काम करती है।",
   "मुद्रा लेखे की इकाई का काम करती है, जिसमें सभी वस्तुओं और सेवाओं के मूल्य व्यक्त किए जा सकते हैं।",
   "मुद्रा मूल्य-संचय का काम नहीं कर सकती, क्योंकि उसे रखने पर कोई प्रतिफल नहीं मिलता।"],
  C3, 1,
  "Statements 1 and 2 are correct. Statement 3 is wrong: money is a store of value -- it lets people keep purchasing power for future use, and it is the most liquid of all assets, which is why people hold it even though it earns no interest. "
  "Its value as a store does fall when prices rise, which is one reason inflation hurts those who hold their savings as cash.",
  "कथन 1 और 2 सही हैं। कथन 3 गलत है: मुद्रा मूल्य-संचय का साधन है -- यह लोगों को भविष्य के लिए क्रय-शक्ति रखने देती है, और यह सभी परिसंपत्तियों में सबसे तरल है, इसीलिए ब्याज न मिलने पर भी लोग इसे रखते हैं। "
  "कीमतें बढ़ने पर संचय के रूप में इसका मूल्य घटता है, यह एक कारण है कि मुद्रास्फीति अपनी बचत नक़दी में रखने वालों को हानि पहुँचाती है।",
  f"{MAC} (Money and Banking).",
  "l1-eco-functions-of-money", craft="precision")

S(MB, "easy", "Consider the following statements about the currency of India:",
  "भारत की मुद्रा के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The rupee is legal tender in India: no one can legally refuse a payment made in rupee notes.",
   "Coins of any denomination must be accepted in settlement of a debt of any amount."],
  ["रुपया भारत में वैध मुद्रा (legal tender) है: कोई भी रुपये के नोटों में किए गए भुगतान को क़ानूनन अस्वीकार नहीं कर सकता।",
   "किसी भी मूल्यवर्ग के सिक्के किसी भी राशि के ऋण के निपटान में स्वीकार करने होंगे।"],
  T2, 0,
  "Only statement 1 is correct: modern currency has no value of its own, and it is accepted as money because the government authorises it -- the RBI issues notes on behalf of the Central Government, and the law makes them legal tender. "
  "Statement 2 is wrong: under the Coinage Act, 2011, coins of one rupee and above are legal tender only for sums up to one thousand rupees, and smaller coins for sums up to ten rupees.",
  "केवल कथन 1 सही है: आधुनिक मुद्रा का अपना कोई मूल्य नहीं है, और वह मुद्रा के रूप में इसलिए स्वीकार होती है कि सरकार उसे अधिकृत करती है -- RBI केंद्र सरकार की ओर से नोट जारी करता है, और क़ानून उन्हें वैध मुद्रा बनाता है। "
  "कथन 2 गलत है: सिक्का निर्माण अधिनियम, 2011 के अंतर्गत एक रुपये और उससे ऊपर के सिक्के केवल एक हज़ार रुपये तक की राशि के लिए, और छोटे सिक्के दस रुपये तक की राशि के लिए वैध मुद्रा हैं।",
  f"{EC10} (Money and Credit); the Coinage Act, 2011.",
  "l1-eco-legal-tender-coins-limit", craft="precision")

# ---------------------------------------------------------------- easy Statement-I/II (1)
A(MB, "easy",
  "Moneylenders in the informal sector often charge much higher rates of interest than banks.",
  "अनौपचारिक क्षेत्र के साहूकार प्रायः बैंकों से कहीं ऊँची ब्याज दरें लेते हैं।",
  "No organisation, such as the RBI, supervises the credit activities of lenders in the informal sector.",
  "अनौपचारिक क्षेत्र के ऋणदाताओं की ऋण गतिविधियों का पर्यवेक्षण RBI जैसा कोई संगठन नहीं करता।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I. Informal lenders -- moneylenders, traders, employers, relatives -- can lend at whatever interest rate they choose and use unfair means to recover their money, while the RBI supervises the lending of banks and cooperatives. "
  "High-cost credit can push a borrower into a debt trap, where repayments swallow most of the income, which is why NCERT stresses expanding cheap formal credit to the poor.",
  "दोनों कथन सही हैं, और कथन-II कथन-I की व्याख्या करता है। अनौपचारिक ऋणदाता -- साहूकार, व्यापारी, नियोक्ता, रिश्तेदार -- मनचाही ब्याज दर पर उधार दे सकते हैं और वसूली के लिए अनुचित तरीक़े अपना सकते हैं, जबकि RBI बैंकों और सहकारी समितियों के ऋण का पर्यवेक्षण करता है। "
  "ऊँची लागत का ऋण उधारकर्ता को ऋण-जाल में धकेल सकता है, जहाँ पुनर्भुगतान अधिकांश आय निगल लेता है, इसीलिए NCERT ग़रीबों तक सस्ते औपचारिक ऋण के विस्तार पर ज़ोर देता है।",
  f"{EC10} (Money and Credit).",
  "l1-eco-informal-credit-high-interest", craft="inference")

# ---------------------------------------------------------------- medium MCQ (1)
M(MB, "medium", "Under the Lead Bank Scheme, introduced in 1969, one bank is given the lead role in coordinating banking development and credit planning in each",
  "1969 में आरंभ अग्रणी बैंक योजना (Lead Bank Scheme) के अंतर्गत प्रत्येक किस इकाई में बैंकिंग विकास और ऋण योजना के समन्वय की अग्रणी भूमिका एक बैंक को दी जाती है?",
  ["district", "State", "development block", "gram panchayat"],
  ["ज़िला", "राज्य", "विकास खंड", "ग्राम पंचायत"],
  0,
  "Under the Lead Bank Scheme, a bank -- usually the one with the largest presence there -- is assigned to each district as its lead bank, to survey credit needs, draw up the district credit plan and coordinate the work of all banks and government agencies in that district. "
  "It was introduced in 1969, the year of bank nationalisation, as part of the push to take banking to rural and neglected areas.",
  "अग्रणी बैंक योजना के अंतर्गत एक बैंक -- सामान्यतः वहाँ सबसे बड़ी उपस्थिति वाला -- प्रत्येक ज़िले का अग्रणी बैंक बनाया जाता है, जो ऋण आवश्यकताओं का सर्वेक्षण करता है, ज़िला ऋण योजना बनाता है और ज़िले के सभी बैंकों तथा सरकारी एजेंसियों के कार्य का समन्वय करता है। "
  "यह 1969 में, बैंक राष्ट्रीयकरण के वर्ष, बैंकिंग को ग्रामीण और उपेक्षित क्षेत्रों तक ले जाने के प्रयास के रूप में आरंभ हुई।",
  f"{RBI} (Lead Bank Scheme).",
  "l1-eco-lead-bank-scheme-district", pos=3, craft="recall")

# ---------------------------------------------------------------- medium statement (4)
S(MB, "medium", "Consider the following statements about credit:",
  "ऋण (credit) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Banks and cooperatives are formal sources of credit.",
   "Richer households depend mainly on formal sources of credit, while poorer households depend largely on informal sources.",
   "Collateral is an asset that the borrower owns and uses as a guarantee to the lender until the loan is repaid.",
   "The terms of credit include the interest rate, collateral, documentation and the mode of repayment."],
  ["बैंक और सहकारी समितियाँ ऋण के औपचारिक स्रोत हैं।",
   "अमीर परिवार मुख्यतः ऋण के औपचारिक स्रोतों पर निर्भर रहते हैं, जबकि ग़रीब परिवार काफ़ी हद तक अनौपचारिक स्रोतों पर।",
   "समर्थक ऋणाधार (collateral) वह परिसंपत्ति है जिसका स्वामी उधारकर्ता होता है और जिसे वह ऋण चुकाए जाने तक ऋणदाता को गारंटी के रूप में देता है।",
   "ऋण की शर्तों में ब्याज दर, समर्थक ऋणाधार, आवश्यक काग़ज़ात और पुनर्भुगतान का तरीक़ा शामिल हैं।"],
  C4, 3,
  "All four statements are correct. Because banks usually ask for collateral and documents, poor borrowers who lack them are often excluded from formal credit and turn to moneylenders, which is one reason why the share of formal credit is much lower for poor households. "
  "If the borrower fails to repay, the lender has the right to sell the collateral -- land, a building, livestock or deposits -- to recover the money.",
  "चारों कथन सही हैं। चूँकि बैंक सामान्यतः समर्थक ऋणाधार और काग़ज़ात माँगते हैं, जिन ग़रीब उधारकर्ताओं के पास ये नहीं होते वे प्रायः औपचारिक ऋण से वंचित रहकर साहूकारों की ओर जाते हैं, यह एक कारण है कि ग़रीब परिवारों में औपचारिक ऋण का हिस्सा बहुत कम है। "
  "उधारकर्ता के न चुकाने पर ऋणदाता को धन वसूलने के लिए समर्थक ऋणाधार -- भूमि, भवन, पशु या जमा -- बेचने का अधिकार होता है।",
  f"{EC10} (Money and Credit).",
  "l1-eco-formal-credit-collateral-terms", craft="recall")

S(MB, "medium", "Consider the following statements about how banks create money:",
  "बैंक मुद्रा कैसे बनाते हैं, इस बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Banks keep only a small part of their deposits as cash reserves and lend out much of the rest.",
   "When a bank lends, the loan is credited to a borrower's account, so lending creates new deposits.",
   "If all depositors asked for their money at the same time, banks could repay it all at once out of their cash reserves."],
  ["बैंक अपनी जमाओं का केवल छोटा भाग नक़द आरक्षित के रूप में रखते हैं और शेष का बड़ा भाग उधार दे देते हैं।",
   "जब बैंक उधार देता है, तो ऋण उधारकर्ता के खाते में जमा होता है, इसलिए उधार देने से नई जमाएँ बनती हैं।",
   "यदि सभी जमाकर्ता एक साथ अपना पैसा माँगें, तो बैंक अपने नक़द आरक्षित से उसे तुरंत लौटा सकते हैं।"],
  C3, 1,
  "Statements 1 and 2 are correct: because the public rarely withdraws all its deposits together, banks need hold only a fraction as reserves; the loans they make return to the banking system as fresh deposits, which can be lent again, so the total of deposits becomes a multiple of the original reserves. "
  "Statement 3 is wrong: with only a fraction held in cash, banks cannot meet a run on all deposits at once -- which is why confidence, deposit insurance and the RBI as lender of last resort matter.",
  "कथन 1 और 2 सही हैं: चूँकि जनता शायद ही कभी सभी जमाएँ एक साथ निकालती है, बैंकों को आरक्षित के रूप में केवल एक अंश रखना पड़ता है; उनके दिए ऋण नई जमाओं के रूप में बैंकिंग प्रणाली में लौटते हैं, जिन्हें फिर उधार दिया जा सकता है, इसलिए कुल जमाएँ मूल आरक्षितों की कई गुना हो जाती हैं। "
  "कथन 3 गलत है: नक़दी में केवल एक अंश रखने के कारण बैंक सभी जमाओं की एक साथ माँग पूरी नहीं कर सकते -- इसीलिए विश्वास, जमा बीमा और अंतिम ऋणदाता के रूप में RBI का महत्त्व है।",
  f"{MAC} (Money and Banking).",
  "l1-eco-bank-money-creation", craft="inference")

S(MB, "medium", "Consider the following statements about real and nominal interest rates:",
  "वास्तविक और नाममात्र (nominal) ब्याज दरों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The real interest rate is roughly the nominal interest rate minus the rate of inflation.",
   "If inflation is higher than the nominal interest rate, the real interest rate is negative.",
   "Inflation that turns out higher than expected benefits borrowers at the expense of lenders."],
  ["वास्तविक ब्याज दर मोटे तौर पर नाममात्र ब्याज दर में से मुद्रास्फीति की दर घटाने पर मिलती है।",
   "यदि मुद्रास्फीति नाममात्र ब्याज दर से अधिक हो, तो वास्तविक ब्याज दर ऋणात्मक होती है।",
   "अपेक्षा से अधिक निकली मुद्रास्फीति ऋणदाताओं की कीमत पर उधारकर्ताओं को लाभ पहुँचाती है।"],
  C3, 2,
  "All three statements are correct. A deposit earning 6 per cent when prices rise by 8 per cent loses about 2 per cent of its purchasing power a year. "
  "When inflation exceeds what was expected when a loan was made, the borrower repays in money that buys less than the money borrowed, so purchasing power shifts from lenders to borrowers; unexpectedly low inflation does the reverse.",
  "तीनों कथन सही हैं। कीमतें 8 प्रतिशत बढ़ने पर 6 प्रतिशत कमाने वाली जमा वर्ष में अपनी क्रय-शक्ति का लगभग 2 प्रतिशत खो देती है। "
  "जब मुद्रास्फीति ऋण देते समय की अपेक्षा से अधिक हो, तो उधारकर्ता उस मुद्रा में चुकाता है जो उधार ली गई मुद्रा से कम ख़रीद पाती है, इसलिए क्रय-शक्ति ऋणदाताओं से उधारकर्ताओं की ओर खिसकती है; अप्रत्याशित रूप से कम मुद्रास्फीति इसका उल्टा करती है।",
  f"{MAC} (Money and Banking).",
  "l1-eco-real-nominal-interest", craft="application")

S(MB, "medium", "Consider the following statements about bank deposits:",
  "बैंक जमाओं के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Deposits in bank accounts that can be withdrawn on demand are called demand deposits.",
   "Banks keep all of their deposits as cash in their vaults.",
   "Banks pay no interest on deposits, since they provide safekeeping."],
  ["बैंक खातों की वे जमाएँ जो माँगने पर निकाली जा सकती हैं, माँग जमाएँ (demand deposits) कहलाती हैं।",
   "बैंक अपनी सारी जमाएँ अपनी तिजोरियों में नक़दी के रूप में रखते हैं।",
   "बैंक जमाओं पर कोई ब्याज नहीं देते, क्योंकि वे सुरक्षित रखने की सेवा देते हैं।"],
  C3, 0,
  "Only statement 1 is correct. Demand deposits, which can be paid out by cheque, share the essential features of money and are counted as money along with currency. "
  "Statement 2 is wrong: banks keep only a small share as cash and lend the rest, earning interest on the loans. Statement 3 is wrong: banks pay interest on deposits; the difference between what they charge borrowers and what they pay depositors is their main source of income.",
  "केवल कथन 1 सही है। माँग जमाएँ, जिनका भुगतान चेक से हो सकता है, मुद्रा की आवश्यक विशेषताएँ रखती हैं और करेंसी के साथ मुद्रा में गिनी जाती हैं। "
  "कथन 2 गलत है: बैंक केवल छोटा भाग नक़दी में रखते हैं और शेष उधार देकर ऋणों पर ब्याज कमाते हैं। कथन 3 गलत है: बैंक जमाओं पर ब्याज देते हैं; उधारकर्ताओं से वसूले और जमाकर्ताओं को दिए ब्याज का अंतर उनकी आय का मुख्य स्रोत है।",
  f"{EC10} (Money and Credit).",
  "l1-eco-demand-deposits-bank-interest", craft="recall")

# ---------------------------------------------------------------- medium Statement-I/II (1)
A(MB, "medium",
  "The Grameen Bank of Bangladesh lends mainly to poor rural women.",
  "बांग्लादेश का ग्रामीण बैंक मुख्यतः ग्रामीण निर्धन महिलाओं को उधार देता है।",
  "Its founder, Muhammad Yunus, and the bank jointly received the Nobel Peace Prize in 2006.",
  "इसके संस्थापक मुहम्मद यूनुस और बैंक को संयुक्त रूप से 2006 का नोबेल शांति पुरस्कार मिला।",
  1,
  "Both statements are correct, but Statement-II is not the correct explanation for Statement-I. The Grameen Bank, begun in the 1970s, lends small sums without collateral to members organised in groups, most of them women, who are jointly responsible and meet regularly; its high repayment rates showed that the poor are creditworthy. "
  "The prize recognised that work; it does not explain why the bank chose to lend to poor women.",
  "दोनों कथन सही हैं, पर कथन-II कथन-I की सही व्याख्या नहीं है। 1970 के दशक में आरंभ ग्रामीण बैंक समूहों में संगठित सदस्यों, जिनमें अधिकांश महिलाएँ हैं, को बिना समर्थक ऋणाधार के छोटी राशियाँ उधार देता है, जो संयुक्त रूप से उत्तरदायी होते हैं और नियमित मिलते हैं; उसकी ऊँची पुनर्भुगतान दरों ने दिखाया कि ग़रीब भी ऋण के योग्य हैं। "
  "पुरस्कार ने उस काम को मान्यता दी; यह नहीं बताता कि बैंक ने ग़रीब महिलाओं को उधार देना क्यों चुना।",
  f"{EC10} (Money and Credit).",
  "l1-eco-grameen-bank-yunus", craft="linkage")

# ---------------------------------------------------------------- hard statement (1)
S(MB, "hard", "Consider the following statements about the management of currency in India:",
  "भारत में मुद्रा के प्रबंधन के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Currency notes other than the one-rupee note are issued by the RBI.",
   "Coins are minted by the Government of India and put into circulation through the RBI.",
   "Under the minimum reserve system, the RBI must hold gold and foreign exchange worth at least ₹200 crore, of which gold must be worth at least ₹115 crore.",
   "Currency notes are printed at presses owned by the Government of India and by a subsidiary of the RBI."],
  ["एक रुपये के नोट को छोड़कर अन्य करेंसी नोट RBI जारी करता है।",
   "सिक्के भारत सरकार द्वारा ढाले जाते हैं और RBI के माध्यम से प्रचलन में लाए जाते हैं।",
   "न्यूनतम आरक्षित प्रणाली के अंतर्गत RBI को कम से कम ₹200 करोड़ का सोना और विदेशी मुद्रा रखनी होती है, जिसमें सोना कम से कम ₹115 करोड़ का होना चाहिए।",
   "करेंसी नोट भारत सरकार के स्वामित्व वाले और RBI की एक सहायक कंपनी के मुद्रणालयों में छापे जाते हैं।"],
  C4, 3,
  "All four statements are correct. Since 1957 India has followed the minimum reserve system, under which the note issue is backed by a small fixed holding of gold and foreign exchange together with government securities and other assets, rather than in proportion to the notes issued. "
  "The Security Printing and Minting Corporation of India runs the Government's presses and mints, while Bharatiya Reserve Bank Note Mudran Private Limited is the RBI's printing subsidiary.",
  "चारों कथन सही हैं। 1957 से भारत न्यूनतम आरक्षित प्रणाली अपनाता है, जिसमें नोट निर्गम के पीछे जारी नोटों के अनुपात में नहीं, बल्कि सोने और विदेशी मुद्रा की एक छोटी निश्चित राशि के साथ सरकारी प्रतिभूतियाँ और अन्य परिसंपत्तियाँ रहती हैं। "
  "सिक्योरिटी प्रिंटिंग एंड मिंटिंग कॉरपोरेशन ऑफ़ इंडिया सरकार के मुद्रणालय और टकसालें चलाता है, जबकि भारतीय रिज़र्व बैंक नोट मुद्रण प्राइवेट लिमिटेड RBI की मुद्रण सहायक कंपनी है।",
  f"{RBI} (currency management); the Reserve Bank of India Act, 1934.",
  "l1-eco-currency-management-minimum-reserve", craft="multi")

# ================================================================ MACRO (5)
# ---------------------------------------------------------------- easy statement (1)
S(MC, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["National income is a flow, measured over a period of time such as a year.",
   "The capital stock of an economy is measured at a point of time."],
  ["राष्ट्रीय आय एक प्रवाह (flow) है, जिसे किसी समयावधि, जैसे एक वर्ष, में मापा जाता है।",
   "किसी अर्थव्यवस्था का पूँजी स्टॉक एक समय-बिंदु पर मापा जाता है।"],
  T2, 2,
  "Both statements are correct. A flow has a time dimension -- income, output, investment and depreciation are measured per year -- while a stock, such as capital, wealth or the money supply, is a quantity existing at a particular moment. "
  "The two are linked: the flow of net investment during a year adds to the stock of capital at its end, as water flowing into a tank changes the level in it.",
  "दोनों कथन सही हैं। प्रवाह में समय का आयाम होता है -- आय, उत्पादन, निवेश और मूल्यह्रास प्रति वर्ष मापे जाते हैं -- जबकि स्टॉक, जैसे पूँजी, संपत्ति या मुद्रा की पूर्ति, किसी विशेष क्षण पर मौजूद मात्रा है। "
  "दोनों जुड़े हैं: वर्ष के दौरान शुद्ध निवेश का प्रवाह उसके अंत में पूँजी के स्टॉक में जुड़ता है, जैसे टंकी में बहता पानी उसका स्तर बदलता है।",
  f"{MAC} (National Income Accounting).",
  "l1-eco-stock-flow", craft="recall")

# ---------------------------------------------------------------- medium MCQ (1)
M(MC, "medium", "If all households in an economy try to save a larger share of their income, total output and income may fall, so that total saving does not rise and may even fall. This idea is known as",
  "यदि किसी अर्थव्यवस्था के सभी परिवार अपनी आय का बड़ा भाग बचाने का प्रयास करें, तो कुल उत्पादन और आय गिर सकते हैं, जिससे कुल बचत नहीं बढ़ती और घट भी सकती है। यह विचार क्या कहलाता है?",
  ["the paradox of thrift", "the liquidity trap", "Say's law of markets", "the crowding-out effect"],
  ["मितव्ययिता का विरोधाभास (paradox of thrift)", "तरलता जाल", "बाज़ार का से का नियम", "बहिर्गमन (crowding-out) प्रभाव"],
  0,
  "The paradox of thrift, from Keynes's analysis, arises because one person's spending is another's income: when everyone spends less, demand and output fall, incomes shrink, and the saving that was planned cannot be realised. "
  "What is wise for one household can harm the economy as a whole, which is why Keynesian policy supports demand in a slump. Say's law, the classical idea Keynes rejected, held that supply creates its own demand.",
  "मितव्ययिता का विरोधाभास, कीन्स के विश्लेषण से, इसलिए उत्पन्न होता है कि एक व्यक्ति का व्यय दूसरे की आय है: जब सब कम व्यय करते हैं, माँग और उत्पादन गिरते हैं, आय सिकुड़ती है, और नियोजित बचत साकार नहीं हो पाती। "
  "जो एक परिवार के लिए बुद्धिमानी है, वह पूरी अर्थव्यवस्था को हानि पहुँचा सकता है, इसीलिए कीन्सीय नीति मंदी में माँग को सहारा देती है। से का नियम, जिसे कीन्स ने अस्वीकार किया, मानता था कि आपूर्ति अपनी माँग स्वयं पैदा करती है।",
  f"{MAC} (Determination of Income and Employment).",
  "l1-eco-paradox-of-thrift", pos=2, craft="inference")

# ---------------------------------------------------------------- medium statement (2)
S(MC, "medium", "Consider the following statements about GDP as a measure of welfare:",
  "कल्याण के माप के रूप में GDP के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["GDP does not show how the income produced is distributed among the people.",
   "The harm done by pollution, a negative externality, is not deducted from GDP.",
   "A rise in GDP always means a rise in the welfare of the people."],
  ["GDP यह नहीं दिखाता कि उत्पन्न आय लोगों में कैसे बँटी है।",
   "प्रदूषण से होने वाली हानि, एक ऋणात्मक बाह्यता (externality), GDP में से नहीं घटाई जाती।",
   "GDP में वृद्धि का अर्थ सदा लोगों के कल्याण में वृद्धि होता है।"],
  C3, 1,
  "Statements 1 and 2 are correct. Statement 3 is wrong: GDP can rise while most people are no better off, if the gains go to a few; it leaves out externalities, such as the damage a factory's pollution does to a river and its fishermen; and it misses many non-monetary exchanges. "
  "So GDP is a measure of output, and only a rough guide to welfare.",
  "कथन 1 और 2 सही हैं। कथन 3 गलत है: यदि लाभ कुछ लोगों तक जाए, तो GDP बढ़ने पर भी अधिकांश लोग पहले से बेहतर नहीं होते; यह बाह्यताओं, जैसे किसी कारख़ाने के प्रदूषण से नदी और उसके मछुआरों को होने वाली क्षति, को छोड़ देता है; और यह कई ग़ैर-मौद्रिक विनिमयों को नहीं गिनता। "
  "इसलिए GDP उत्पादन का माप है, और कल्याण का केवल मोटा संकेतक।",
  f"{MAC} (National Income Accounting).",
  "l1-eco-gdp-welfare-limits", craft="inference")

S(MC, "medium", "Consider the following statements about measuring national product:",
  "राष्ट्रीय उत्पाद की माप के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The value added by a firm is the value of its output minus the value of the intermediate goods it uses.",
   "Adding up the values of all goods sold at every stage of production gives GDP without any double counting.",
   "Goods produced during a year but not sold are left out of that year's GDP."],
  ["किसी फ़र्म द्वारा जोड़ा गया मूल्य उसके उत्पादन के मूल्य में से उसके द्वारा प्रयुक्त मध्यवर्ती वस्तुओं का मूल्य घटाने पर मिलता है।",
   "उत्पादन की हर अवस्था पर बेची गई सभी वस्तुओं के मूल्य जोड़ने से बिना किसी दोहरी गणना के GDP मिलता है।",
   "वर्ष के दौरान उत्पादित पर न बिकी वस्तुएँ उस वर्ष के GDP से बाहर रहती हैं।"],
  C3, 0,
  "Only statement 1 is correct. Statement 2 is wrong: the value of wheat is counted again in the flour, and the flour in the bread, so adding all sales counts intermediate goods many times; summing values added, or counting only final goods, avoids this double counting. "
  "Statement 3 is wrong: unsold output is added to the firms' inventories, and the change in inventories is counted as part of investment, so it is included in that year's GDP.",
  "केवल कथन 1 सही है। कथन 2 गलत है: गेहूँ का मूल्य आटे में फिर गिना जाता है, और आटे का ब्रेड में, इसलिए सभी बिक्रियाँ जोड़ने से मध्यवर्ती वस्तुएँ कई बार गिन ली जाती हैं; जोड़े गए मूल्यों का योग, या केवल अंतिम वस्तुओं की गणना, इस दोहरी गणना से बचाती है। "
  "कथन 3 गलत है: न बिका उत्पादन फ़र्मों के माल-स्टॉक में जुड़ता है, और स्टॉक में परिवर्तन निवेश के भाग के रूप में गिना जाता है, इसलिए वह उस वर्ष के GDP में शामिल होता है।",
  f"{MAC} (National Income Accounting).",
  "l1-eco-value-added-inventories", craft="application")

# ---------------------------------------------------------------- hard statement (1)
S(MC, "hard", "Consider the following statements about the origins of macroeconomics:",
  "समष्टि अर्थशास्त्र (macroeconomics) की उत्पत्ति के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["During the Great Depression that began in 1929, unemployment in the USA rose from about 3 per cent to about 25 per cent.",
   "John Maynard Keynes's 'The General Theory of Employment, Interest and Money' was published in 1936.",
   "Keynes argued that a market economy left to itself always returns quickly to full employment."],
  ["1929 में आरंभ महामंदी के दौरान अमेरिका में बेरोज़गारी लगभग 3 प्रतिशत से बढ़कर लगभग 25 प्रतिशत हो गई।",
   "जॉन मेनार्ड कीन्स की 'द जनरल थ्योरी ऑफ़ एम्प्लॉयमेंट, इंटरेस्ट एंड मनी' 1936 में प्रकाशित हुई।",
   "कीन्स का तर्क था कि अपने हाल पर छोड़ी गई बाज़ार अर्थव्यवस्था सदा जल्दी ही पूर्ण रोज़गार पर लौट आती है।"],
  C3, 1,
  "Statements 1 and 2 are correct: the Depression, in which output fell and factories stood idle across Europe and North America, could not be explained by the classical view, and Keynes's book founded macroeconomics as a separate branch. "
  "Statement 3 is wrong: that was the classical belief Keynes challenged; he argued that output and employment depend on aggregate demand, which can stay too low for long periods, leaving workers unemployed unless the government steps in.",
  "कथन 1 और 2 सही हैं: महामंदी, जिसमें यूरोप और उत्तरी अमेरिका में उत्पादन गिरा और कारख़ाने बेकार पड़े रहे, शास्त्रीय दृष्टिकोण से नहीं समझाई जा सकी, और कीन्स की पुस्तक ने समष्टि अर्थशास्त्र को अलग शाखा के रूप में स्थापित किया। "
  "कथन 3 गलत है: यह वह शास्त्रीय विश्वास था जिसे कीन्स ने चुनौती दी; उनका तर्क था कि उत्पादन और रोज़गार समग्र माँग पर निर्भर करते हैं, जो लंबे समय तक बहुत कम रह सकती है, और सरकार के हस्तक्षेप के बिना श्रमिक बेरोज़गार रह जाते हैं।",
  f"{MAC} (Introduction).",
  "l1-eco-great-depression-keynes", craft="linkage")

# ================================================================ TAXATION (5)
# ---------------------------------------------------------------- easy statement (1)
S(TX, "easy", "Consider the following statements about the Goods and Services Tax (GST):",
  "वस्तु एवं सेवा कर (GST) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["GST is a destination-based tax on consumption, so the revenue goes to the State where the goods or services are consumed.",
   "Article 246A, inserted by the Constitution (One Hundred and First Amendment) Act, 2016, gives both Parliament and the State legislatures the power to make laws on GST."],
  ["GST उपभोग पर गंतव्य-आधारित कर है, इसलिए राजस्व उस राज्य को जाता है जहाँ वस्तुओं या सेवाओं का उपभोग होता है।",
   "संविधान (एक सौ एकवाँ संशोधन) अधिनियम, 2016 द्वारा जोड़ा गया अनुच्छेद 246A संसद और राज्य विधानमंडलों, दोनों को GST पर क़ानून बनाने की शक्ति देता है।"],
  T2, 2,
  "Both statements are correct. Under the old system, a producing State could tax goods sold to other States; under GST the tax follows the goods to where they are consumed, which benefits consuming States. "
  "Article 246A created a concurrent taxing power, but Parliament alone legislates on GST on inter-State supplies, collected as integrated GST and shared between the Centre and the destination State.",
  "दोनों कथन सही हैं। पुरानी व्यवस्था में उत्पादक राज्य दूसरे राज्यों को बेची गई वस्तुओं पर कर लगा सकता था; GST में कर वस्तुओं के पीछे-पीछे वहाँ जाता है जहाँ उनका उपभोग होता है, जिससे उपभोक्ता राज्यों को लाभ होता है। "
  "अनुच्छेद 246A ने समवर्ती कर-शक्ति बनाई, पर अंतर-राज्यीय आपूर्तियों पर GST का क़ानून केवल संसद बनाती है, जो एकीकृत GST के रूप में वसूलकर केंद्र और गंतव्य राज्य में बाँटा जाता है।",
  "Constitution of India (Article 246A, Article 269A); GST Council.",
  "l1-eco-gst-destination-246a", craft="recall")

# ---------------------------------------------------------------- medium MCQ (1)
M(TX, "medium", "Estate duty, a tax on property passing on the death of its owner, was abolished in India in",
  "स्वामी की मृत्यु पर हस्तांतरित संपत्ति पर लगने वाला कर, संपदा शुल्क (estate duty), भारत में कब समाप्त किया गया?",
  ["1985", "1991", "2005", "2015"],
  ["1985", "1991", "2005", "2015"],
  0,
  "Estate duty, introduced in 1953, was abolished in 1985 because it yielded little revenue, was costly to administer and encouraged evasion through early transfers and undervaluation. "
  "India has had no inheritance tax since then; wealth tax, a separate tax on net wealth, survived until its abolition from 2016-17.",
  "1953 में आरंभ संपदा शुल्क 1985 में समाप्त किया गया, क्योंकि इससे राजस्व कम मिलता था, इसका प्रशासन महँगा था और यह पहले ही हस्तांतरण तथा कम मूल्यांकन द्वारा कर-चोरी को बढ़ावा देता था। "
  "तब से भारत में कोई उत्तराधिकार कर नहीं है; शुद्ध संपत्ति पर अलग कर, संपत्ति कर (wealth tax), 2016-17 से समाप्त होने तक बना रहा।",
  "Ministry of Finance (Union Budget 1985-86).",
  "l1-eco-estate-duty-abolished-1985", pos=3, craft="recall")

# ---------------------------------------------------------------- medium statement (2)
S(TX, "medium", "Consider the following statements about Adam Smith's canons of taxation:",
  "एडम स्मिथ के कराधान के सिद्धांतों (canons) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The canon of equality requires every taxpayer to pay the same amount of tax.",
   "The canon of certainty requires the amount, time and manner of payment of a tax to be clear to the taxpayer.",
   "The canon of convenience requires a tax to be levied at the time and in the manner most convenient for the taxpayer to pay it.",
   "The canon of economy requires the cost of collecting a tax to be as small as possible."],
  ["समानता का सिद्धांत हर करदाता से समान राशि का कर चुकाने की अपेक्षा करता है।",
   "निश्चितता का सिद्धांत अपेक्षा करता है कि कर की राशि, भुगतान का समय और तरीक़ा करदाता को स्पष्ट हो।",
   "सुविधा का सिद्धांत अपेक्षा करता है कि कर ऐसे समय और तरीक़े से लगाया जाए जो करदाता के लिए चुकाने में सबसे सुविधाजनक हो।",
   "मितव्ययिता का सिद्धांत अपेक्षा करता है कि कर वसूलने की लागत यथासंभव कम हो।"],
  C4, 2,
  "Statements 2, 3 and 4 are correct. Statement 1 is wrong: in 'The Wealth of Nations' (1776), equality meant that people should contribute in proportion to their ability to pay, not the same amount -- the idea behind progressive income tax. "
  "Land revenue collected at harvest time and taxes deducted at source are classic examples of the canon of convenience.",
  "कथन 2, 3 और 4 सही हैं। कथन 1 गलत है: 'द वेल्थ ऑफ़ नेशंस' (1776) में समानता का अर्थ था कि लोग समान राशि नहीं, बल्कि अपनी भुगतान-क्षमता के अनुपात में योगदान दें -- प्रगतिशील आयकर के पीछे यही विचार है। "
  "फ़सल कटाई के समय वसूला जाने वाला भू-राजस्व और स्रोत पर काटे जाने वाले कर सुविधा के सिद्धांत के क्लासिक उदाहरण हैं।",
  "Adam Smith, 'An Inquiry into the Nature and Causes of the Wealth of Nations' (1776), Book V.",
  "l1-eco-canons-of-taxation", craft="precision")

S(TX, "medium", "Consider the following statements about the taxation of gifts under India's income tax law:",
  "भारत के आयकर क़ानून के अंतर्गत उपहारों पर कर के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Gifts of money worth more than ₹50,000 in a year from people who are not relatives are taxed as the income of the person who receives them.",
   "Gifts received from specified relatives are not taxed.",
   "Gifts received on the occasion of the recipient's marriage are not taxed.",
   "Property received under a will or by inheritance is not taxed as a gift."],
  ["ग़ैर-रिश्तेदारों से वर्ष में ₹50,000 से अधिक के धन के उपहार प्राप्त करने वाले व्यक्ति की आय मानकर कर-योग्य हैं।",
   "निर्दिष्ट रिश्तेदारों से मिले उपहारों पर कर नहीं लगता।",
   "प्राप्तकर्ता के विवाह के अवसर पर मिले उपहारों पर कर नहीं लगता।",
   "वसीयत या उत्तराधिकार से मिली संपत्ति पर उपहार के रूप में कर नहीं लगता।"],
  C4, 3,
  "All four statements are correct. A separate Gift-tax Act was abolished in 1998; since then, gifts have been brought into income tax in the hands of the recipient, so that gifts cannot be used to move income tax-free between unrelated people. "
  "The exemptions protect ordinary family transfers -- gifts between close relatives, at marriage, and on inheritance.",
  "चारों कथन सही हैं। अलग उपहार-कर अधिनियम 1998 में समाप्त हुआ; तब से उपहारों को प्राप्तकर्ता के हाथ में आयकर के दायरे में लाया गया है, ताकि उपहारों के ज़रिए असंबंधित लोगों के बीच आय कर-मुक्त न खिसकाई जा सके। "
  "छूटें सामान्य पारिवारिक हस्तांतरणों -- निकट संबंधियों के बीच, विवाह पर और उत्तराधिकार में मिले उपहारों -- की रक्षा करती हैं।",
  "Income-tax Department, Ministry of Finance (taxation of gifts).",
  "l1-eco-gift-taxation-income", craft="precision")

# ---------------------------------------------------------------- medium Statement-I/II (1)
A(TX, "medium",
  "Wealth tax was abolished with effect from 2016-17.",
  "संपत्ति कर (wealth tax) 2016-17 से समाप्त कर दिया गया।",
  "Its collections were small compared with the cost and effort of administering it.",
  "इसकी वसूली इसके प्रशासन की लागत और प्रयास की तुलना में बहुत कम थी।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I. Announcing the abolition in the Union Budget of 2015-16, the Government noted that wealth tax had yielded only about ₹1,000 crore a year while requiring taxpayers to file returns and value their assets; "
  "it replaced the revenue with an additional surcharge on the incomes of the very rich.",
  "दोनों कथन सही हैं, और कथन-II कथन-I की व्याख्या करता है। 2015-16 के केंद्रीय बजट में समाप्ति की घोषणा करते हुए सरकार ने कहा कि संपत्ति कर से वर्ष में केवल लगभग ₹1,000 करोड़ मिलते थे, जबकि करदाताओं को विवरणी भरनी और अपनी परिसंपत्तियों का मूल्यांकन करना पड़ता था; "
  "उसने इस राजस्व की भरपाई बहुत धनी लोगों की आय पर अतिरिक्त अधिभार से की।",
  "Ministry of Finance (Union Budget 2015-16, Budget Speech).",
  "l1-eco-wealth-tax-abolished", craft="inference")

write("eco_l1_t5_b.sql")
