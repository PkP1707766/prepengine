# -*- coding: utf-8 -*-
"""Level 1 · Test 5 (Economy, NCERT Foundation) -- part A: Financial Markets, Instruments & Fintech (26)
(upsc_l1_cell_targets.mjs 5): easy MCQ 2, easy statement 5, easy Statement-I/II 1, medium MCQ 3, medium statement 9,
medium Statement-I/II 2, hard MCQ 1, hard statement 2, hard Statement-I/II 1.
The angle is NCERT Business Studies (sources of business finance, financial markets, banking and insurance services)
with the RBI, SEBI, NPCI and Ministry of Finance rules an investor meets first: depositories, cheques, payment
systems, digital lending, credit information, mutual-fund plans and small savings.
Level-2 facts are not repeated (BSE/NSE history, demat basics, IPO and QIP, T-bills, CP/CD/call money, bonds and
yields, derivatives, insurance basics and IRDAI, UPI, card networks, e-rupee, REITs, NPS, mutual-fund types, the
instruments-markets pairs). MCQ keys are pinned (pos)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Economy"
d.REQUIRE_CRAFT = True
FM = "Financial Markets, Instruments & Fintech"
BS11 = "NCERT Class XI, Business Studies"
BS12 = "NCERT Class XII, Business Studies, Part II"
RBI = "Reserve Bank of India"

# ---------------------------------------------------------------- easy MCQ (2)
M(FM, "easy", "A company keeps part of its net profit and reinvests it in the business instead of paying it out as dividend. This source of finance is called",
  "एक कंपनी अपने शुद्ध लाभ का एक भाग लाभांश के रूप में बाँटने के बजाय रोककर व्यवसाय में फिर से लगाती है। वित्त का यह स्रोत क्या कहलाता है?",
  ["retained earnings", "commercial paper", "factoring of receivables", "public deposits"],
  ["प्रतिधारित आय (retained earnings)", "वाणिज्यिक पत्र", "प्राप्य राशियों का फ़ैक्टरिंग", "सार्वजनिक जमा"],
  0,
  "Retained earnings, also called the 'ploughing back of profit', are an internal source of finance: no flotation cost is incurred, no ownership is diluted and the money is available whenever the business needs it. "
  "Their drawback is that the amount is uncertain, since it depends on profits, and too much retention can annoy shareholders who expect dividends.",
  "प्रतिधारित आय, जिसे 'लाभ का पुनर्निवेश' (ploughing back of profit) भी कहते हैं, वित्त का आंतरिक स्रोत है: इसमें निर्गमन लागत नहीं लगती, स्वामित्व नहीं बँटता और व्यवसाय को जब ज़रूरत हो, धन उपलब्ध रहता है। "
  "इसकी कमी यह है कि राशि अनिश्चित रहती है, क्योंकि यह लाभ पर निर्भर है, और बहुत अधिक रोकने से लाभांश की आशा रखने वाले अंशधारक असंतुष्ट हो सकते हैं।",
  f"{BS11} (Sources of Business Finance).",
  "l1-eco-retained-earnings-ploughing-back", pos=0, craft="recall")

M(FM, "easy", "Which type of bank account allows any number of deposits and withdrawals, pays little or no interest, and usually comes with an overdraft facility, making it suited to business firms?",
  "किस प्रकार का बैंक खाता असीमित जमा और निकासी की अनुमति देता है, जिस पर बहुत कम या कोई ब्याज नहीं मिलता, और जिसके साथ सामान्यतः ओवरड्राफ़्ट की सुविधा होती है, जिससे यह व्यावसायिक फ़र्मों के अनुकूल है?",
  ["current account", "savings account", "recurring deposit account", "fixed deposit account"],
  ["चालू खाता", "बचत खाता", "आवर्ती जमा खाता", "सावधि जमा खाता"],
  0,
  "A current account is meant for people and firms that make frequent payments: there is no limit on the number of transactions, little or no interest is paid on the balance, and the bank may allow the holder to overdraw up to an agreed limit. "
  "A savings account encourages saving and pays interest, while recurring and fixed deposits lock money in for a period in return for higher interest.",
  "चालू खाता उन लोगों और फ़र्मों के लिए है जो बार-बार भुगतान करते हैं: लेन-देन की संख्या पर कोई सीमा नहीं होती, शेष राशि पर बहुत कम या कोई ब्याज नहीं मिलता, और बैंक धारक को एक तय सीमा तक अधिक राशि निकालने दे सकता है। "
  "बचत खाता बचत को प्रोत्साहित करता है और ब्याज देता है, जबकि आवर्ती और सावधि जमा ऊँचे ब्याज के बदले धन को एक अवधि के लिए बाँध देते हैं।",
  f"{BS11} (Business Services).",
  "l1-eco-current-account-features", pos=3, craft="application")

# ---------------------------------------------------------------- easy statement (5)
S(FM, "easy", "Consider the following statements about equity and preference shares:",
  "इक्विटी और अधिमान (preference) शेयरों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Preference shareholders receive dividend at a fixed rate before any dividend is paid to equity shareholders.",
   "Equity shareholders are the owners of the company and have voting rights.",
   "When a company is wound up, preference capital is repaid only after the equity capital."],
  ["अधिमान अंशधारकों को इक्विटी अंशधारकों को कोई लाभांश दिए जाने से पहले निश्चित दर पर लाभांश मिलता है।",
   "इक्विटी अंशधारक कंपनी के स्वामी होते हैं और उन्हें मतदान का अधिकार होता है।",
   "कंपनी के समापन पर अधिमान पूँजी इक्विटी पूँजी के बाद ही लौटाई जाती है।"],
  C3, 1,
  "Statements 1 and 2 are correct: equity shareholders carry the risk of the business, receive what is left after all other claims and control the company through their votes, while preference shareholders enjoy a preference over them in dividend. "
  "Statement 3 is wrong: preference shareholders are also paid back their capital before the equity shareholders when the company is wound up; that is the second half of their 'preference'.",
  "कथन 1 और 2 सही हैं: इक्विटी अंशधारक व्यवसाय का जोखिम उठाते हैं, अन्य सभी दावों के बाद जो बचे वह पाते हैं और अपने मतों द्वारा कंपनी को नियंत्रित करते हैं, जबकि अधिमान अंशधारकों को लाभांश में उन पर वरीयता मिलती है। "
  "कथन 3 गलत है: कंपनी के समापन पर अधिमान अंशधारकों की पूँजी भी इक्विटी अंशधारकों से पहले लौटाई जाती है; यही उनकी 'वरीयता' का दूसरा भाग है।",
  f"{BS11} (Sources of Business Finance).",
  "l1-eco-equity-preference-shares", craft="precision")

S(FM, "easy", "Consider the following statements about sources of business finance:",
  "व्यावसायिक वित्त के स्रोतों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Trade credit is credit extended by one trader to another on the purchase of goods, and appears in the buyer's books as sundry creditors or accounts payable.",
   "In lease financing, the lessee pays rentals for the right to use an asset that remains owned by the lessor."],
  ["व्यापार साख वह साख है जो माल ख़रीदने पर एक व्यापारी दूसरे को देता है, और जो ख़रीदार की बहियों में विविध लेनदारों या देय खातों के रूप में दिखती है।",
   "पट्टा वित्त (lease financing) में पट्टेदार (lessee) उस संपत्ति के उपयोग के अधिकार के लिए किराया देता है जिसका स्वामित्व पट्टाकर्ता (lessor) के पास रहता है।"],
  T2, 2,
  "Both statements are correct. Trade credit is a common short-term source of finance that needs no charge on the firm's assets, though it can tempt a firm to over-trade. "
  "Leasing lets a firm use costly equipment without a large initial outlay: the lessor receives the lease rentals and, at the end of the lease, the asset reverts to the lessor.",
  "दोनों कथन सही हैं। व्यापार साख अल्पकालिक वित्त का एक सामान्य स्रोत है, जिसके लिए फ़र्म की संपत्तियों पर कोई भार नहीं रखना पड़ता, यद्यपि यह फ़र्म को आवश्यकता से अधिक व्यापार के लिए ललचा सकती है। "
  "पट्टा फ़र्म को बड़ी आरंभिक लागत के बिना महँगे उपकरण उपयोग करने देता है: पट्टाकर्ता को पट्टे का किराया मिलता है और पट्टे के अंत में संपत्ति पट्टाकर्ता के पास लौट जाती है।",
  f"{BS11} (Sources of Business Finance).",
  "l1-eco-trade-credit-lease-financing", craft="recall")

S(FM, "easy", "Consider the following statements about the capital market:",
  "पूँजी बाज़ार के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The primary market deals in new securities issued by companies for the first time.",
   "Each time a company's shares change hands in the secondary market, the company receives money from the transaction."],
  ["प्राथमिक बाज़ार कंपनियों द्वारा पहली बार जारी नई प्रतिभूतियों का बाज़ार है।",
   "द्वितीयक बाज़ार में जब भी किसी कंपनी के शेयर हाथ बदलते हैं, तब उस लेन-देन से कंपनी को धन मिलता है।"],
  T2, 0,
  "Only statement 1 is correct: in the primary (new issues) market, savings flow directly from investors to the issuing company, which uses the money for new projects or expansion. "
  "Statement 2 is wrong: the secondary market, the stock exchange, deals in securities already issued; when shares are traded there, money passes from one investor to another and the company receives nothing -- but the market gives the shares liquidity, which makes investors willing to buy new issues in the first place.",
  "केवल कथन 1 सही है: प्राथमिक (नए निर्गम) बाज़ार में बचत निवेशकों से सीधे निर्गमकर्ता कंपनी तक जाती है, जो उसका उपयोग नई परियोजनाओं या विस्तार के लिए करती है। "
  "कथन 2 गलत है: द्वितीयक बाज़ार, यानी शेयर बाज़ार, पहले से जारी प्रतिभूतियों का बाज़ार है; वहाँ शेयरों के व्यापार में धन एक निवेशक से दूसरे निवेशक को जाता है और कंपनी को कुछ नहीं मिलता -- पर यह बाज़ार शेयरों को तरलता देता है, जिससे निवेशक नए निर्गम ख़रीदने को तैयार होते हैं।",
  f"{BS12} (Financial Markets).",
  "l1-eco-primary-secondary-market", craft="inference")

S(FM, "easy", "Consider the following statements about cheques in India:",
  "भारत में चेक के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["A crossed cheque cannot be encashed over the counter; its amount must be credited to a bank account.",
   "A bearer cheque can be encashed by whoever presents it at the bank.",
   "A cheque is valid for three months from the date written on it."],
  ["रेखांकित (crossed) चेक का भुगतान काउंटर पर नक़द नहीं हो सकता; उसकी राशि किसी बैंक खाते में जमा होनी चाहिए।",
   "वाहक (bearer) चेक का भुगतान उसे बैंक में प्रस्तुत करने वाले किसी भी व्यक्ति को हो सकता है।",
   "चेक उस पर लिखी तारीख़ से तीन महीने तक वैध रहता है।"],
  C3, 2,
  "All three statements are correct. Crossing -- two parallel lines across the face of the cheque -- makes it safer, since the money can be traced to an account; a bearer cheque is as risky as cash if lost, and an 'order' cheque is payable only to the named person or to whomever he endorses it. "
  "The RBI cut the validity of cheques, drafts and pay orders from six months to three months from 1 April 2012.",
  "तीनों कथन सही हैं। रेखांकन -- चेक के मुख पर दो समानांतर रेखाएँ -- उसे सुरक्षित बनाता है, क्योंकि धन का पता किसी खाते तक लगाया जा सकता है; खो जाने पर वाहक चेक नक़दी जितना जोखिम भरा है, और 'आदेश' (order) चेक का भुगतान केवल नामित व्यक्ति को या जिसके पक्ष में वह उसका पृष्ठांकन करे, उसे होता है। "
  "RBI ने 1 अप्रैल 2012 से चेक, ड्राफ़्ट और पे ऑर्डर की वैधता छह महीने से घटाकर तीन महीने कर दी।",
  f"{BS11} (Business Services); {RBI}.",
  "l1-eco-cheques-crossed-bearer-validity", craft="recall")

S(FM, "easy", "Consider the following statements about the functions of financial markets:",
  "वित्तीय बाज़ारों के कार्यों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Financial markets mobilise savings and channel them into the most productive uses.",
   "Financial markets raise the cost of transactions, because they add intermediaries between savers and borrowers."],
  ["वित्तीय बाज़ार बचतों को जुटाकर उन्हें सबसे उत्पादक उपयोगों की ओर ले जाते हैं।",
   "वित्तीय बाज़ार लेन-देन की लागत बढ़ाते हैं, क्योंकि वे बचतकर्ताओं और उधारकर्ताओं के बीच बिचौलिए जोड़ते हैं।"],
  T2, 0,
  "Only statement 1 is correct. Statement 2 is wrong: by bringing buyers and sellers together and providing information about securities, financial markets reduce the time, effort and money spent on transactions. "
  "Their other functions are price discovery -- prices emerge from the interaction of the demand and supply of funds -- and providing liquidity, since financial assets can be turned into cash readily.",
  "केवल कथन 1 सही है। कथन 2 गलत है: क्रेताओं और विक्रेताओं को एक साथ लाकर और प्रतिभूतियों की जानकारी देकर वित्तीय बाज़ार लेन-देन में लगने वाला समय, प्रयास और धन घटाते हैं। "
  "उनके अन्य कार्य हैं मूल्य-निर्धारण (price discovery) -- कीमतें धन की माँग और आपूर्ति की पारस्परिक क्रिया से तय होती हैं -- और तरलता देना, क्योंकि वित्तीय परिसंपत्तियों को आसानी से नक़दी में बदला जा सकता है।",
  f"{BS12} (Financial Markets).",
  "l1-eco-financial-market-functions", craft="inference")

# ---------------------------------------------------------------- easy Statement-I/II (1)
A(FM, "easy",
  "A seller is safer accepting a bank draft than a personal cheque.",
  "विक्रेता के लिए निजी चेक की बजाय बैंक ड्राफ़्ट स्वीकार करना अधिक सुरक्षित है।",
  "The amount of a draft is paid to the bank in advance, so it cannot be dishonoured for want of funds.",
  "ड्राफ़्ट की राशि बैंक को पहले ही चुका दी जाती है, इसलिए धन की कमी के कारण उसका अनादर नहीं हो सकता।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I. A bank draft is an order by a bank to pay a sum to the named payee, issued after the buyer has paid that sum (with a small commission) to the bank; a cheque, in contrast, is only as good as the balance in the drawer's account. "
  "That is why drafts are used for fees, deposits and payments to strangers, where the payee cannot judge the drawer's credit.",
  "दोनों कथन सही हैं, और कथन-II कथन-I की व्याख्या करता है। बैंक ड्राफ़्ट नामित प्राप्तकर्ता को एक राशि देने का बैंक का आदेश है, जो ख़रीदार द्वारा वह राशि (थोड़े कमीशन के साथ) बैंक को चुकाने के बाद जारी होता है; इसके विपरीत, चेक उतना ही विश्वसनीय है जितना आहर्ता के खाते में शेष। "
  "इसीलिए शुल्क, जमानत और अपरिचितों को भुगतान में ड्राफ़्ट का उपयोग होता है, जहाँ प्राप्तकर्ता आहर्ता की साख नहीं परख सकता।",
  f"{BS11} (Business Services).",
  "l1-eco-bank-draft-prepaid", craft="inference")

# ---------------------------------------------------------------- medium MCQ (3)
M(FM, "medium", "A building is insured with two insurers for ₹30 lakh and ₹20 lakh. After a fire causes a loss of ₹10 lakh, the two insurers pay ₹6 lakh and ₹4 lakh respectively. The principle applied is",
  "एक भवन दो बीमाकर्ताओं के पास ₹30 लाख और ₹20 लाख के लिए बीमित है। आग से ₹10 लाख की हानि होने पर दोनों बीमाकर्ता क्रमशः ₹6 लाख और ₹4 लाख चुकाते हैं। यहाँ कौन-सा सिद्धांत लागू हुआ?",
  ["contribution", "mitigation of loss", "risk pooling", "reinsurance"],
  ["अंशदान (contribution)", "हानि का न्यूनीकरण", "जोखिम का सामूहीकरण (risk pooling)", "पुनर्बीमा"],
  0,
  "Under the principle of contribution, when the same property is insured with more than one insurer, the insurers share the loss in proportion to the amounts they have insured -- here 3:2 -- and the insured, who can recover no more than the actual loss, cannot claim the full loss from each. "
  "Mitigation of loss obliges the insured to take reasonable steps to limit the damage, while reinsurance is an insurer itself insuring part of its risk with another insurer.",
  "अंशदान के सिद्धांत के अंतर्गत, जब एक ही संपत्ति एक से अधिक बीमाकर्ताओं के पास बीमित हो, तो बीमाकर्ता हानि को अपनी बीमित राशियों के अनुपात में -- यहाँ 3:2 -- बाँटते हैं, और बीमित व्यक्ति, जो वास्तविक हानि से अधिक वसूल नहीं कर सकता, हर एक से पूरी हानि का दावा नहीं कर सकता। "
  "हानि के न्यूनीकरण का सिद्धांत बीमित व्यक्ति पर क्षति सीमित करने के उचित उपाय करने का दायित्व डालता है, जबकि पुनर्बीमा में बीमाकर्ता स्वयं अपने जोखिम का एक भाग किसी अन्य बीमाकर्ता के पास बीमित कराता है।",
  f"{BS11} (Business Services).",
  "l1-eco-insurance-contribution-principle", pos=1, craft="application")

M(FM, "medium", "A seller draws a bill of exchange on the buyer for goods sold on credit; the buyer accepts it, and the seller gets it discounted with a bank to raise cash before the due date. Such an instrument is a",
  "एक विक्रेता उधार बेचे गए माल के लिए ख़रीदार पर विनिमय-पत्र लिखता है; ख़रीदार उसे स्वीकार करता है, और विक्रेता नियत तिथि से पहले नक़दी पाने के लिए उसे बैंक से भुनवा लेता है। ऐसा साधन क्या है?",
  ["commercial bill", "commercial paper", "certificate of deposit", "treasury bill"],
  ["वाणिज्यिक बिल", "वाणिज्यिक पत्र", "जमा प्रमाण-पत्र", "ट्रेज़री बिल"],
  0,
  "A commercial bill is a bill of exchange used to finance the working capital of business firms: once accepted by the buyer it becomes a marketable instrument, and the seller can discount it with a bank, receiving the amount less a discount, while the bank collects the full sum from the buyer on maturity. "
  "Commercial paper is an unsecured promissory note issued by a large company, a certificate of deposit is a negotiable time deposit issued by a bank, and a treasury bill is short-term borrowing by the Government of India.",
  "वाणिज्यिक बिल व्यावसायिक फ़र्मों की कार्यशील पूँजी के वित्तपोषण में प्रयुक्त विनिमय-पत्र है: ख़रीदार द्वारा स्वीकार होते ही यह विपणन योग्य साधन बन जाता है, और विक्रेता उसे बैंक से भुनवाकर बट्टा घटाकर राशि पा सकता है, जबकि परिपक्वता पर बैंक ख़रीदार से पूरी राशि वसूलता है। "
  "वाणिज्यिक पत्र किसी बड़ी कंपनी द्वारा जारी असुरक्षित वचन-पत्र है, जमा प्रमाण-पत्र किसी बैंक द्वारा जारी परक्राम्य सावधि जमा है, और ट्रेज़री बिल भारत सरकार का अल्पकालिक उधार है।",
  f"{BS12} (Financial Markets).",
  "l1-eco-commercial-bill-discounting", pos=2, craft="precision")

M(FM, "medium", "Investing a fixed amount in a mutual fund scheme at regular intervals, so that more units are bought when prices are low and fewer when they are high, is called",
  "किसी म्यूचुअल फ़ंड योजना में नियमित अंतराल पर एक निश्चित राशि लगाना, जिससे कीमतें कम होने पर अधिक और अधिक होने पर कम यूनिट ख़रीदी जाती हैं, क्या कहलाता है?",
  ["a systematic investment plan", "a systematic withdrawal plan", "a dividend reinvestment plan", "a lump-sum investment"],
  ["व्यवस्थित निवेश योजना (SIP)", "व्यवस्थित निकासी योजना (SWP)", "लाभांश पुनर्निवेश योजना", "एकमुश्त निवेश"],
  0,
  "A systematic investment plan (SIP) averages out the purchase price over time -- often called rupee-cost averaging -- and builds the habit of regular saving without having to time the market; it does not, however, guarantee returns or protect against a long fall in prices. "
  "A systematic withdrawal plan works the other way, paying out a fixed sum from the investment at regular intervals.",
  "व्यवस्थित निवेश योजना (SIP) समय के साथ ख़रीद मूल्य का औसत निकाल देती है -- जिसे प्रायः रुपया-लागत औसत कहते हैं -- और बाज़ार का सही समय पकड़ने की चिंता के बिना नियमित बचत की आदत बनाती है; पर यह न लाभ की गारंटी देती है न कीमतों की लंबी गिरावट से बचाती है। "
  "व्यवस्थित निकासी योजना उल्टी दिशा में काम करती है, जो निवेश से नियमित अंतराल पर एक निश्चित राशि देती है।",
  "Securities and Exchange Board of India (investor education); Association of Mutual Funds in India.",
  "l1-eco-sip-rupee-cost-averaging", pos=3, craft="recall")

# ---------------------------------------------------------------- medium statement (9)
S(FM, "medium", "Consider the following statements about methods of floating new issues of securities:",
  "प्रतिभूतियों के नए निर्गम जारी करने की विधियों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["In an 'offer for sale', the company sells the securities in bulk to intermediaries such as issuing houses or brokers, who resell them to the public.",
   "In a 'rights issue', existing shareholders get the first right to subscribe to new shares, in proportion to their holdings.",
   "In a 'private placement', securities are allotted to institutional investors and some selected individuals.",
   "In an 'e-IPO', the company issues its securities to the public through the online system of a stock exchange."],
  ["'बिक्री के लिए प्रस्ताव' (offer for sale) में कंपनी प्रतिभूतियाँ थोक में निर्गम गृहों या दलालों जैसे मध्यस्थों को बेचती है, जो उन्हें जनता को फिर से बेचते हैं।",
   "'अधिकार निर्गम' (rights issue) में मौजूदा अंशधारकों को अपनी धारिता के अनुपात में नए शेयरों के लिए आवेदन करने का पहला अधिकार मिलता है।",
   "'निजी नियोजन' (private placement) में प्रतिभूतियाँ संस्थागत निवेशकों और कुछ चुने हुए व्यक्तियों को आवंटित की जाती हैं।",
   "'ई-आईपीओ' में कंपनी अपनी प्रतिभूतियाँ शेयर बाज़ार की ऑनलाइन प्रणाली से जनता को जारी करती है।"],
  C4, 3,
  "All four statements are correct. An offer through a prospectus invites the public directly, while an offer for sale saves the company the work of selling to the public itself; a rights issue lets existing owners keep their share of the company, and private placement is cheaper and quicker because it avoids a public issue. "
  "For an e-IPO, the company enters into an agreement with the stock exchange and appoints registered brokers to accept applications.",
  "चारों कथन सही हैं। विवरण-पत्रिका द्वारा प्रस्ताव जनता को सीधे आमंत्रित करता है, जबकि बिक्री के लिए प्रस्ताव कंपनी को स्वयं जनता को बेचने के काम से बचाता है; अधिकार निर्गम मौजूदा स्वामियों को कंपनी में अपना हिस्सा बनाए रखने देता है, और निजी नियोजन सस्ता और तेज़ है क्योंकि इसमें सार्वजनिक निर्गम नहीं करना पड़ता। "
  "ई-आईपीओ के लिए कंपनी शेयर बाज़ार से समझौता करती है और आवेदन स्वीकार करने के लिए पंजीकृत दलाल नियुक्त करती है।",
  f"{BS12} (Financial Markets).",
  "l1-eco-floatation-methods", craft="precision")

S(FM, "medium", "Consider the following statements about depositories:",
  "निक्षेपागारों (depositories) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["A depository holds securities in electronic form and transfers them by book entry.",
   "India has two depositories, the National Securities Depository Limited (NSDL) and the Central Depository Services (India) Limited (CDSL).",
   "An investor deals with a depository directly, without any intermediary."],
  ["निक्षेपागार प्रतिभूतियों को इलेक्ट्रॉनिक रूप में रखता है और बही-प्रविष्टि द्वारा उनका अंतरण करता है।",
   "भारत में दो निक्षेपागार हैं, नेशनल सिक्योरिटीज़ डिपॉज़िटरी लिमिटेड (NSDL) और सेंट्रल डिपॉज़िटरी सर्विसेज़ (इंडिया) लिमिटेड (CDSL)।",
   "निवेशक बिना किसी मध्यस्थ के सीधे निक्षेपागार से व्यवहार करता है।"],
  C3, 1,
  "Statements 1 and 2 are correct: a depository works like a bank for securities, and dematerialisation -- converting share certificates into electronic holdings -- removes the risks of loss, theft, forgery and delays in transfer. "
  "Statement 3 is wrong: the investor opens a demat account with a depository participant (DP), such as a bank or a broker registered with SEBI, which acts as the depository's agent and the investor's point of contact.",
  "कथन 1 और 2 सही हैं: निक्षेपागार प्रतिभूतियों के लिए बैंक की तरह काम करता है, और अभौतिकीकरण -- शेयर प्रमाण-पत्रों को इलेक्ट्रॉनिक धारिता में बदलना -- खोने, चोरी, जालसाज़ी और अंतरण में देरी के जोखिम मिटाता है। "
  "कथन 3 गलत है: निवेशक किसी निक्षेपागार सहभागी (DP), जैसे SEBI में पंजीकृत बैंक या दलाल, के पास डीमैट खाता खोलता है, जो निक्षेपागार का एजेंट और निवेशक का संपर्क-बिंदु होता है।",
  f"{BS12} (Financial Markets).",
  "l1-eco-depositories-nsdl-cdsl-dp", craft="precision")

S(FM, "medium", "Consider the following statements about the principles of insurance:",
  "बीमा के सिद्धांतों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Under 'utmost good faith', both parties to the contract must disclose all material facts to each other.",
   "Under 'insurable interest', the insured must stand to suffer a financial loss if the insured event happens.",
   "Under 'subrogation', after settling a claim the insurer takes over the insured's right to recover the loss from a third party.",
   "Under 'proximate cause', a loss is covered only if its nearest cause is a peril insured against."],
  ["'परम सद्भाव' (utmost good faith) के अंतर्गत अनुबंध के दोनों पक्षों को एक-दूसरे को सभी महत्त्वपूर्ण तथ्य बताने होते हैं।",
   "'बीमायोग्य हित' (insurable interest) के अंतर्गत, बीमित घटना होने पर बीमित व्यक्ति को वित्तीय हानि होने की स्थिति होनी चाहिए।",
   "'प्रत्यासन' (subrogation) के अंतर्गत दावा चुकाने के बाद बीमाकर्ता किसी तीसरे पक्ष से हानि वसूलने का बीमित व्यक्ति का अधिकार ले लेता है।",
   "'निकटतम कारण' (proximate cause) के अंतर्गत हानि तभी कवर होती है जब उसका निकटतम कारण कोई बीमित जोखिम हो।"],
  C4, 3,
  "All four statements are correct. These principles keep insurance a protection against loss rather than a wager: concealment of a material fact makes the contract voidable, a person cannot insure what he has no stake in, and subrogation stops the insured from collecting twice for the same loss. "
  "The other principles NCERT lists are indemnity, contribution and mitigation of loss.",
  "चारों कथन सही हैं। ये सिद्धांत बीमा को दाँव के बजाय हानि से सुरक्षा बनाए रखते हैं: किसी महत्त्वपूर्ण तथ्य को छिपाने से अनुबंध शून्यकरणीय हो जाता है, कोई व्यक्ति उस चीज़ का बीमा नहीं करा सकता जिसमें उसका कोई हित न हो, और प्रत्यासन बीमित व्यक्ति को एक ही हानि के लिए दो बार वसूली से रोकता है। "
  "NCERT द्वारा गिनाए गए अन्य सिद्धांत हैं क्षतिपूर्ति, अंशदान और हानि का न्यूनीकरण।",
  f"{BS11} (Business Services).",
  "l1-eco-insurance-principles", craft="precision")

S(FM, "medium", "Consider the following statements about short-term bank credit to businesses:",
  "व्यवसायों को बैंकों के अल्पकालिक ऋण के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["An overdraft lets an account holder withdraw more than the balance in the account, up to an agreed limit, paying interest only on the amount overdrawn.",
   "Cash credit is usually given against the security of goods, such as stocks of raw material or finished goods, pledged or hypothecated to the bank.",
   "Under cash credit, interest is charged on the full sanctioned limit, whether it is used or not."],
  ["ओवरड्राफ़्ट खाताधारक को एक तय सीमा तक खाते में शेष से अधिक राशि निकालने देता है, जिसमें ब्याज केवल अधिक निकाली गई राशि पर लगता है।",
   "नक़द साख (cash credit) सामान्यतः माल, जैसे कच्चे माल या तैयार माल के भंडार, को बैंक के पास गिरवी या दृष्टिबंधक रखकर दी जाती है।",
   "नक़द साख में ब्याज पूरी स्वीकृत सीमा पर लगता है, चाहे उसका उपयोग हो या न हो।"],
  C3, 1,
  "Statements 1 and 2 are correct: both facilities meet a firm's working capital needs, which rise and fall with its business. "
  "Statement 3 is wrong: under cash credit the borrower draws money as required within the limit, and interest is charged only on the amount actually used -- which makes it cheaper than a term loan of the full amount.",
  "कथन 1 और 2 सही हैं: दोनों सुविधाएँ फ़र्म की कार्यशील पूँजी की ज़रूरतें पूरी करती हैं, जो उसके व्यवसाय के साथ घटती-बढ़ती हैं। "
  "कथन 3 गलत है: नक़द साख में उधारकर्ता सीमा के भीतर आवश्यकता अनुसार धन निकालता है, और ब्याज केवल वास्तव में उपयोग की गई राशि पर लगता है -- जिससे यह पूरी राशि के सावधि ऋण से सस्ती पड़ती है।",
  f"{BS11} (Business Services).",
  "l1-eco-overdraft-cash-credit", craft="precision")

S(FM, "medium", "Consider the following statements about payment systems run by the National Payments Corporation of India (NPCI):",
  "भारतीय राष्ट्रीय भुगतान निगम (NPCI) द्वारा चलाई जाने वाली भुगतान प्रणालियों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Aadhaar-enabled Payment System (AePS) lets a customer withdraw cash or check the balance through a business correspondent, using Aadhaar authentication.",
   "The Bharat Bill Payment System (BBPS) offers interoperable payment of bills such as electricity, water and telephone through many channels.",
   "Immediate Payment Service (IMPS) transfers are available only during banking hours on working days."],
  ["आधार-सक्षम भुगतान प्रणाली (AePS) ग्राहक को आधार प्रमाणीकरण से किसी व्यवसाय प्रतिनिधि (business correspondent) के माध्यम से नक़द निकालने या शेष देखने देती है।",
   "भारत बिल भुगतान प्रणाली (BBPS) बिजली, पानी और टेलीफ़ोन जैसे बिलों का अनेक माध्यमों से अंतर-प्रचालनीय भुगतान देती है।",
   "तत्काल भुगतान सेवा (IMPS) से अंतरण केवल कार्य-दिवसों पर बैंकिंग समय में उपलब्ध है।"],
  C3, 1,
  "Statements 1 and 2 are correct: AePS, using only an Aadhaar number and a fingerprint at a micro-ATM, has carried basic banking to villages without branches, and BBPS lets a bill be paid at any agent, bank or app. "
  "Statement 3 is wrong: IMPS, launched in 2010, provides instant interbank transfers round the clock, all days of the year, including holidays.",
  "कथन 1 और 2 सही हैं: केवल आधार संख्या और माइक्रो-एटीएम पर उँगली की छाप से चलने वाली AePS ने बिना शाखा वाले गाँवों तक बुनियादी बैंकिंग पहुँचाई है, और BBPS किसी भी एजेंट, बैंक या ऐप पर बिल चुकाने देती है। "
  "कथन 3 गलत है: 2010 में आरंभ IMPS छुट्टियों सहित वर्ष के सभी दिन, चौबीसों घंटे, तत्काल अंतर-बैंक अंतरण देती है।",
  "National Payments Corporation of India; Reserve Bank of India.",
  "l1-eco-aeps-bbps-imps", craft="precision")

S(FM, "medium", "Consider the following statements about the RBI's rules on digital lending:",
  "डिजिटल ऋण पर RBI के नियमों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["A digital loan must be disbursed directly into the borrower's bank account, and not routed through a pool account of a lending service provider.",
   "Before the contract, the borrower must be given a Key Fact Statement, which shows the all-in cost of the loan as an annual percentage rate.",
   "The borrower gets a cooling-off period during which he can exit the loan by repaying the principal and the proportionate cost, without any penalty."],
  ["डिजिटल ऋण सीधे उधारकर्ता के बैंक खाते में दिया जाना चाहिए, न कि किसी ऋण सेवा प्रदाता के पूल खाते से होकर।",
   "अनुबंध से पहले उधारकर्ता को एक मुख्य तथ्य विवरण (Key Fact Statement) देना होता है, जो ऋण की पूरी लागत को वार्षिक प्रतिशत दर के रूप में दिखाता है।",
   "उधारकर्ता को एक 'कूलिंग-ऑफ़' अवधि मिलती है जिसमें वह मूलधन और आनुपातिक लागत चुकाकर बिना किसी दंड के ऋण से बाहर निकल सकता है।"],
  C3, 2,
  "All three statements are correct. The rules, framed after complaints of hidden charges, unauthorised apps and coercive recovery, hold the regulated lender -- a bank or NBFC -- responsible for the conduct of any app or agent acting for it. "
  "Repayments too must go directly from the borrower's account to the lender's, and fees not shown in the Key Fact Statement cannot be charged.",
  "तीनों कथन सही हैं। छिपे शुल्कों, अनधिकृत ऐप्स और दबावपूर्ण वसूली की शिकायतों के बाद बने ये नियम विनियमित ऋणदाता -- बैंक या NBFC -- को उसकी ओर से काम करने वाले किसी भी ऐप या एजेंट के आचरण के लिए उत्तरदायी ठहराते हैं। "
  "पुनर्भुगतान भी सीधे उधारकर्ता के खाते से ऋणदाता के खाते में जाना चाहिए, और मुख्य तथ्य विवरण में न दिखाए गए शुल्क नहीं वसूले जा सकते।",
  f"{RBI} (Digital Lending Directions).",
  "l1-eco-digital-lending-kfs-cooling-off", craft="recall")

S(FM, "medium", "Consider the following statements about investing in mutual funds:",
  "म्यूचुअल फ़ंड में निवेश के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The direct plan of a scheme has a lower expense ratio than its regular plan, since no distributor's commission is paid out of it.",
   "Every scheme carries a SEBI 'riskometer', which grades its risk on a scale from Low to Very High.",
   "An equity-linked savings scheme (ELSS) is a debt scheme with no lock-in period."],
  ["किसी योजना के प्रत्यक्ष (direct) प्लान का व्यय अनुपात उसके नियमित (regular) प्लान से कम होता है, क्योंकि उसमें से वितरक का कमीशन नहीं दिया जाता।",
   "हर योजना पर SEBI का 'रिस्कोमीटर' होता है, जो उसके जोखिम को 'निम्न' से 'बहुत उच्च' तक के पैमाने पर आँकता है।",
   "इक्विटी-लिंक्ड बचत योजना (ELSS) बिना लॉक-इन अवधि वाली एक ऋण (debt) योजना है।"],
  C3, 1,
  "Statements 1 and 2 are correct: the same portfolio is offered in both plans, so the lower costs of a direct plan show up as a higher net asset value over time, and the riskometer must be shown in all advertisements and updated as the portfolio changes. "
  "Statement 3 is wrong: an ELSS is an equity scheme that invests mainly in shares and carries a lock-in period of three years.",
  "कथन 1 और 2 सही हैं: दोनों प्लानों में एक ही पोर्टफ़ोलियो होता है, इसलिए प्रत्यक्ष प्लान की कम लागत समय के साथ ऊँचे शुद्ध परिसंपत्ति मूल्य के रूप में दिखती है, और रिस्कोमीटर को सभी विज्ञापनों में दिखाना और पोर्टफ़ोलियो बदलने पर अद्यतन करना होता है। "
  "कथन 3 गलत है: ELSS मुख्यतः शेयरों में निवेश करने वाली इक्विटी योजना है, जिसकी लॉक-इन अवधि तीन वर्ष है।",
  "Securities and Exchange Board of India (mutual fund regulations and circulars).",
  "l1-eco-mutual-fund-direct-plan-riskometer", craft="precision")

S(FM, "medium", "Consider the following statements about small savings schemes:",
  "लघु बचत योजनाओं के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["A Public Provident Fund (PPF) account matures after 15 years.",
   "A Sukanya Samriddhi account can be opened for a girl child up to the age of 18 years.",
   "Interest rates on small savings schemes are fixed once a year by the RBI."],
  ["सार्वजनिक भविष्य निधि (PPF) खाता 15 वर्ष बाद परिपक्व होता है।",
   "सुकन्या समृद्धि खाता 18 वर्ष तक की आयु की बालिका के लिए खोला जा सकता है।",
   "लघु बचत योजनाओं की ब्याज दरें RBI द्वारा वर्ष में एक बार तय की जाती हैं।"],
  C3, 0,
  "Only statement 1 is correct: the PPF runs for 15 years and can be extended in blocks of five years. "
  "Statement 2 is wrong: a Sukanya Samriddhi account can be opened only for a girl child below the age of 10. Statement 3 is wrong: the rates are notified every quarter by the Ministry of Finance, linked broadly to the yields on government securities; the money collected goes into the National Small Savings Fund and is lent to the Centre and the States.",
  "केवल कथन 1 सही है: PPF 15 वर्ष चलता है और पाँच-पाँच वर्ष के खंडों में बढ़ाया जा सकता है। "
  "कथन 2 गलत है: सुकन्या समृद्धि खाता केवल 10 वर्ष से कम आयु की बालिका के लिए खोला जा सकता है। कथन 3 गलत है: दरें हर तिमाही वित्त मंत्रालय द्वारा अधिसूचित होती हैं, जो मोटे तौर पर सरकारी प्रतिभूतियों के प्रतिफल से जुड़ी हैं; जुटाया गया धन राष्ट्रीय लघु बचत कोष में जाता है और केंद्र तथा राज्यों को उधार दिया जाता है।",
  "Ministry of Finance, Department of Economic Affairs (small savings schemes).",
  "l1-eco-small-savings-ppf-ssy-rates", craft="multi")

S(FM, "medium", "Consider the following statements about raising funds from abroad by Indian companies:",
  "भारतीय कंपनियों द्वारा विदेश से धन जुटाने के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Holders of Global Depository Receipts (GDRs) do not carry voting rights in the company.",
   "American Depository Receipts (ADRs) are issued to American investors and listed and traded on a stock exchange of the USA.",
   "Foreign Currency Convertible Bonds (FCCBs) are equity-linked debt securities that can be converted into shares after a specified period."],
  ["वैश्विक निक्षेपागार रसीदों (GDRs) के धारकों को कंपनी में मतदान का अधिकार नहीं होता।",
   "अमेरिकी निक्षेपागार रसीदें (ADRs) अमेरिकी निवेशकों को जारी की जाती हैं और अमेरिका के किसी शेयर बाज़ार में सूचीबद्ध होकर उनका व्यापार होता है।",
   "विदेशी मुद्रा परिवर्तनीय बॉन्ड (FCCBs) इक्विटी से जुड़ी ऋण प्रतिभूतियाँ हैं, जिन्हें एक तय अवधि के बाद शेयरों में बदला जा सकता है।"],
  C3, 2,
  "All three statements are correct. A depository receipt is a negotiable certificate, denominated in a foreign currency, that represents a company's shares held by a custodian in India; GDRs trade on exchanges outside the USA, such as Luxembourg and London. "
  "An FCCB carries a fixed interest rate, lower than a plain bond, because holders also get the option of conversion into equity.",
  "तीनों कथन सही हैं। निक्षेपागार रसीद विदेशी मुद्रा में अंकित एक परक्राम्य प्रमाण-पत्र है, जो भारत में किसी अभिरक्षक के पास रखे कंपनी के शेयरों का प्रतिनिधित्व करता है; GDRs का व्यापार अमेरिका के बाहर, जैसे लक्ज़मबर्ग और लंदन के बाज़ारों में होता है। "
  "FCCB पर साधारण बॉन्ड से कम, निश्चित ब्याज दर होती है, क्योंकि धारकों को इक्विटी में बदलने का विकल्प भी मिलता है।",
  f"{BS11} (Sources of Business Finance).",
  "l1-eco-gdr-adr-fccb", craft="precision")

# ---------------------------------------------------------------- medium Statement-I/II (2)
A(FM, "medium",
  "A company must pay interest on its debentures even in a year in which it makes no profit.",
  "कंपनी को अपने ऋणपत्रों (debentures) पर उस वर्ष भी ब्याज चुकाना होता है जिसमें उसे कोई लाभ नहीं होता।",
  "Debenture holders are creditors of the company, whereas shareholders are its owners.",
  "ऋणपत्रधारक कंपनी के लेनदार होते हैं, जबकि अंशधारक उसके स्वामी होते हैं।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I. As lenders, debenture holders are entitled to interest at a fixed rate and to repayment on schedule, whatever the company's results, while dividend on shares is paid only out of profits and at the board's discretion. "
  "For the same reason debenture holders generally have no voting rights, and interest on debentures is a charge on profit, deductible for tax purposes.",
  "दोनों कथन सही हैं, और कथन-II कथन-I की व्याख्या करता है। लेनदार होने के नाते ऋणपत्रधारक कंपनी के परिणाम चाहे जो हों, निश्चित दर पर ब्याज और समय पर पुनर्भुगतान के हक़दार हैं, जबकि शेयरों पर लाभांश केवल लाभ से और निदेशक मंडल के विवेक पर दिया जाता है। "
  "इसी कारण ऋणपत्रधारकों को सामान्यतः मतदान का अधिकार नहीं होता, और ऋणपत्रों का ब्याज लाभ पर भार है, जो कर के लिए घटाने योग्य है।",
  f"{BS11} (Sources of Business Finance).",
  "l1-eco-debenture-interest-creditors", craft="inference")

A(FM, "medium",
  "SEBI prohibits insider trading in securities.",
  "SEBI प्रतिभूतियों में भेदिया व्यापार (insider trading) पर रोक लगाता है।",
  "SEBI was set up as a statutory body under an Act of Parliament in 1988.",
  "SEBI को 1988 में संसद के एक अधिनियम के अंतर्गत सांविधिक निकाय के रूप में स्थापित किया गया था।",
  2,
  "Statement-I is correct but Statement-II is incorrect. Prohibiting insider trading -- dealing on the basis of unpublished price-sensitive information -- is one of SEBI's protective functions, along with curbing fraudulent and unfair trade practices and educating investors. "
  "SEBI was set up in April 1988 as an interim administrative body; it got statutory status on 30 January 1992 through an ordinance, later replaced by the SEBI Act, 1992.",
  "कथन-I सही है, पर कथन-II गलत है। भेदिया व्यापार -- अप्रकाशित, मूल्य-संवेदी जानकारी के आधार पर सौदा करना -- पर रोक SEBI के संरक्षणात्मक कार्यों में है, साथ ही धोखाधड़ी और अनुचित व्यापार प्रथाओं पर अंकुश और निवेशकों को शिक्षित करना भी। "
  "SEBI अप्रैल 1988 में एक अंतरिम प्रशासनिक निकाय के रूप में बना; उसे 30 जनवरी 1992 को एक अध्यादेश से सांविधिक दर्जा मिला, जिसका स्थान बाद में SEBI अधिनियम, 1992 ने लिया।",
  f"{BS12} (Financial Markets).",
  "l1-eco-sebi-insider-trading-1992", craft="precision")

# ---------------------------------------------------------------- hard MCQ (1)
M(FM, "hard", "A mutual fund scheme holds securities worth ₹245 crore and cash of ₹10 crore, has liabilities of ₹5 crore, and has 20 crore units outstanding. Its net asset value (NAV) per unit is",
  "एक म्यूचुअल फ़ंड योजना के पास ₹245 करोड़ की प्रतिभूतियाँ और ₹10 करोड़ नक़द है, उसकी देनदारियाँ ₹5 करोड़ हैं, और उसकी 20 करोड़ यूनिट बकाया हैं। उसका प्रति यूनिट शुद्ध परिसंपत्ति मूल्य (NAV) है",
  ["₹12.50", "₹12.75", "₹12.25", "₹13.00"],
  ["₹12.50", "₹12.75", "₹12.25", "₹13.00"],
  0,
  "NAV per unit = (market value of assets - liabilities) / units outstanding = (245 + 10 - 5) / 20 = 250 / 20 = ₹12.50. "
  "Cash is part of the assets; omitting it gives ₹12.00, and omitting the liabilities gives ₹12.75. The NAV is worked out at the end of every business day, and investors buy and redeem units of open-ended schemes at that day's NAV.",
  "प्रति यूनिट NAV = (परिसंपत्तियों का बाज़ार मूल्य - देनदारियाँ) / बकाया यूनिट = (245 + 10 - 5) / 20 = 250 / 20 = ₹12.50। "
  "नक़दी परिसंपत्तियों का भाग है; उसे छोड़ने पर ₹12.00 और देनदारियाँ छोड़ने पर ₹12.75 आता है। NAV हर कार्य-दिवस के अंत में निकाला जाता है, और निवेशक खुली योजनाओं की यूनिट उसी दिन के NAV पर ख़रीदते और भुनाते हैं।",
  "Securities and Exchange Board of India (Mutual Funds) Regulations; Association of Mutual Funds in India.",
  "l1-eco-nav-calculation", pos=3, craft="application")

# ---------------------------------------------------------------- hard statement (2)
S(FM, "hard", "Consider the following statements about factoring:",
  "फ़ैक्टरिंग के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["In factoring 'with recourse', the client firm bears the loss if a customer fails to pay.",
   "In factoring 'without recourse', the factor bears the risk of bad debts.",
   "Factoring is a source of long-term finance for buying fixed assets."],
  ["'सहारे सहित' (with recourse) फ़ैक्टरिंग में ग्राहक के भुगतान न करने पर हानि ग्राहक फ़र्म उठाती है।",
   "'सहारे रहित' (without recourse) फ़ैक्टरिंग में डूबत ऋणों का जोखिम फ़ैक्टर उठाता है।",
   "फ़ैक्टरिंग स्थायी संपत्तियाँ ख़रीदने के लिए दीर्घकालिक वित्त का स्रोत है।"],
  C3, 1,
  "Statements 1 and 2 are correct: a factor buys or collects a firm's receivables, advancing cash against them at a discount, and may also keep its sales ledger and check the credit standing of its customers; since the factor carries more risk without recourse, it charges more for that service. "
  "Statement 3 is wrong: factoring turns receivables into cash, and so is a source of short-term finance for working capital.",
  "कथन 1 और 2 सही हैं: फ़ैक्टर किसी फ़र्म की प्राप्य राशियाँ ख़रीदता या वसूलता है, उनके बदले बट्टे पर नक़द अग्रिम देता है, और उसकी बिक्री बही रखने तथा उसके ग्राहकों की साख जाँचने का काम भी कर सकता है; सहारे रहित में अधिक जोखिम उठाने के कारण फ़ैक्टर उस सेवा का अधिक शुल्क लेता है। "
  "कथन 3 गलत है: फ़ैक्टरिंग प्राप्य राशियों को नक़दी में बदलती है, इसलिए यह कार्यशील पूँजी के लिए अल्पकालिक वित्त का स्रोत है।",
  f"{BS11} (Sources of Business Finance).",
  "l1-eco-factoring-recourse", craft="precision")

S(FM, "hard", "Consider the following statements about credit information companies (CICs) in India:",
  "भारत में साख सूचना कंपनियों (CICs) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["They are regulated by the RBI under the Credit Information Companies (Regulation) Act, 2005.",
   "Banks and other lenders regulated by the RBI must be members of all CICs and report the credit information of their borrowers to them.",
   "A person is entitled to one free full credit report, including the credit score, every year from each CIC."],
  ["इनका विनियमन RBI द्वारा साख सूचना कंपनी (विनियमन) अधिनियम, 2005 के अंतर्गत होता है।",
   "RBI द्वारा विनियमित बैंकों और अन्य ऋणदाताओं को सभी CICs का सदस्य होना और अपने उधारकर्ताओं की साख संबंधी जानकारी उन्हें देनी होती है।",
   "किसी व्यक्ति को हर CIC से प्रति वर्ष, साख अंक (credit score) सहित, एक निःशुल्क पूर्ण साख रिपोर्ट पाने का अधिकार है।"],
  C3, 2,
  "All three statements are correct. India has four CICs -- TransUnion CIBIL, Equifax, Experian and CRIF High Mark -- which compile repayment histories into credit reports and scores that lenders use to price and decide loans. "
  "Because a wrong entry can deny someone credit, the RBI also requires lenders to correct errors quickly, and CICs to compensate the customer for delays in resolving complaints.",
  "तीनों कथन सही हैं। भारत में चार CICs हैं -- ट्रांसयूनियन सिबिल, इक्विफ़ैक्स, एक्सपीरियन और क्रिफ़ हाई मार्क -- जो पुनर्भुगतान के इतिहास को साख रिपोर्टों और अंकों में बदलती हैं, जिनसे ऋणदाता ऋण देने और उसकी दर तय करते हैं। "
  "चूँकि एक गलत प्रविष्टि किसी को ऋण से वंचित कर सकती है, RBI ऋणदाताओं से त्रुटियाँ शीघ्र सुधारने, और CICs से शिकायतों के निपटान में देरी पर ग्राहक को क्षतिपूर्ति देने की भी अपेक्षा करता है।",
  f"{RBI} (Credit Information Companies directions).",
  "l1-eco-credit-information-companies", craft="recall")

# ---------------------------------------------------------------- hard Statement-I/II (1)
A(FM, "hard",
  "Life insurance is a contract of indemnity.",
  "जीवन बीमा क्षतिपूर्ति (indemnity) का अनुबंध है।",
  "Under a contract of indemnity, the insured is compensated only for the actual loss suffered, and cannot make a profit out of the loss.",
  "क्षतिपूर्ति के अनुबंध में बीमित व्यक्ति को केवल वास्तविक हानि की भरपाई मिलती है, और वह हानि से लाभ नहीं कमा सकता।",
  3,
  "Statement-I is incorrect but Statement-II is correct. Fire, marine and most general insurance are contracts of indemnity, which is why the claim is limited to the loss actually proved. "
  "Life insurance is not: the loss of a human life cannot be valued in money, so the insurer promises to pay a fixed sum on death or on maturity of the policy, whatever the 'loss' -- it is a contract of assurance rather than indemnity.",
  "कथन-I गलत है, पर कथन-II सही है। अग्नि, समुद्री और अधिकांश सामान्य बीमा क्षतिपूर्ति के अनुबंध हैं, इसीलिए दावा वास्तव में सिद्ध हानि तक सीमित रहता है। "
  "जीवन बीमा ऐसा नहीं है: मानव जीवन की हानि को धन में नहीं आँका जा सकता, इसलिए बीमाकर्ता मृत्यु या पॉलिसी की परिपक्वता पर, 'हानि' चाहे जो हो, एक निश्चित राशि देने का वचन देता है -- यह क्षतिपूर्ति का नहीं, आश्वासन का अनुबंध है।",
  f"{BS11} (Business Services).",
  "l1-eco-life-insurance-not-indemnity", craft="inference")

write("eco_l1_t5_a.sql")
