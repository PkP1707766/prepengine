# -*- coding: utf-8 -*-
"""Level 2 · Test 15 (Economy 1: Money, Banking, Financial Markets, Macro Concepts) -- depth audit of 2026-10-04
(docs/upsc-question-design-standard.md §6).

All 107 rows were read and classified. Before: analytic 25, precision 40, recall 42 (7 rows are Test 21's,
already tagged). 14 recall rows are rewritten in place with the same concept id, type and difficulty, mostly
as small cases:
  - a company splitting its profit, a first listing, a T-bill bought at a discount, a 10 per cent crash in
    the Nifty, a depositor in a cooperative bank under moratorium, a farmer who also mills his wheat, and the
    1970s mix of rising prices and stagnant output;
  - why fund returns float, who is paid first in a winding-up, why fixed deposits pay more, what a
    downgrade costs, how InvITs recycle capital, how TReDS prices an MSME's invoice, and what selling bad
    loans does for a bank.
After: analytic 39, precision 40, recall 28. The other 86 rows keep their content and get their craft tag.
Leaks avoided while drafting:
  - savings accounts earning a lower rate than fixed deposits (answers the savings-spread AR's Statement I);
  - bond prices falling as yields rise (states the borrowing-yields AR's Statement III);
  - an oil shock as the cause in the stagflation case (supports the inflation-types row's statement 2), and
    demand-pull or disinflation as its distractors (that row defines both)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write_updates, CODE
from polity_common import C3, C4, T2

d.SUBJECT = "Economy"
d.REQUIRE_CRAFT = True
FM = "Financial Markets, Instruments & Fintech"
MC = "Macro Concepts, National Income & Inflation"
MB = "Money, Banking & Monetary Policy"
SEBI = "Securities and Exchange Board of India."
RBI = "Reserve Bank of India."
NCM = "NCERT Class XII, Introductory Macroeconomics"
NC10E = "NCERT Class X, Understanding Economic Development"

# ================================================================ MCQs (3)
M(FM, "easy", "A company earns a profit of 100 crore rupees. Its board decides to pay 30 crore rupees of it to the shareholders and to keep the rest for expansion. The 30 crore rupees paid out is:",
  "एक कंपनी 100 करोड़ रुपये का लाभ कमाती है। उसका बोर्ड इसमें से 30 करोड़ रुपये शेयरधारकों को देने और बाक़ी विस्तार के लिए रखने का निर्णय लेता है। दिए गए 30 करोड़ रुपये हैं:",
  ["a dividend", "interest on the company's debt", "a bonus issue", "a buyback of shares"],
  ["लाभांश", "कंपनी के ऋण पर ब्याज", "बोनस निर्गम", "शेयरों की पुनर्ख़रीद"],
  0,
  "A dividend is the part of its profit that a company distributes to its shareholders; the board decides how much, if any, to pay, and the rest is kept as retained earnings for the business. "
  "Interest on debt is owed to lenders whether or not there is a profit, and is a cost met before profit is struck. A bonus issue gives shareholders extra shares out of reserves without paying any cash, and a buyback returns cash only to those holders who sell their shares back to the company.",
  "लाभांश लाभ का वह भाग है जो कंपनी अपने शेयरधारकों में बाँटती है; बोर्ड तय करता है कि कितना, यदि कुछ, देना है, और बाक़ी व्यवसाय के लिए प्रतिधारित आय के रूप में रखा जाता है। "
  "ऋण पर ब्याज ऋणदाताओं को देय होता है चाहे लाभ हो या न हो, और लाभ निकालने से पहले चुकाई जाने वाली लागत है। बोनस निर्गम शेयरधारकों को बिना नक़द दिए आरक्षित निधि से अतिरिक्त शेयर देता है, और पुनर्ख़रीद केवल उन धारकों को नक़द लौटाती है जो अपने शेयर कंपनी को वापस बेचते हैं।",
  SEBI, "fm-dividend-easy", craft="application")

M(FM, "easy", "A private company whose shares have never been traded offers its shares to the public for the first time and then lists them on a stock exchange. This is:",
  "एक निजी कंपनी, जिसके शेयरों का कभी व्यापार नहीं हुआ, पहली बार अपने शेयर जनता को देती है और फिर उन्हें स्टॉक एक्सचेंज पर सूचीबद्ध करती है। यह है:",
  ["an initial public offering", "a follow-on public offer", "a rights issue", "a qualified institutional placement"],
  ["प्रारंभिक सार्वजनिक निर्गम (IPO)", "अनुवर्ती सार्वजनिक निर्गम (FPO)", "अधिकार निर्गम", "अर्हता प्राप्त संस्थागत नियोजन (QIP)"],
  0,
  "An initial public offering is a company's first sale of shares to the public, after which the shares are listed and traded. A follow-on public offer is a later public issue by a company that is already listed; a rights issue offers new shares only to existing shareholders; and a qualified institutional placement sells shares to institutions such as mutual funds and insurers without a public issue.",
  "प्रारंभिक सार्वजनिक निर्गम किसी कंपनी की जनता को शेयरों की पहली बिक्री है, जिसके बाद शेयर सूचीबद्ध होकर व्यापार में आते हैं। अनुवर्ती सार्वजनिक निर्गम पहले से सूचीबद्ध कंपनी का बाद का सार्वजनिक निर्गम है; अधिकार निर्गम नए शेयर केवल मौजूदा शेयरधारकों को देता है; और अर्हता प्राप्त संस्थागत नियोजन बिना सार्वजनिक निर्गम के म्यूचुअल फ़ंड और बीमाकर्ताओं जैसी संस्थाओं को शेयर बेचता है।",
  SEBI, "fm-ipo-meaning-easy", craft="application")

M(MC, "medium", "In the mid-1970s many economies saw prices rising rapidly while output stagnated and unemployment rose. Which one of the following best describes this situation?",
  "1970 के दशक के मध्य में कई अर्थव्यवस्थाओं में क़ीमतें तेज़ी से बढ़ीं, जबकि उत्पादन ठहरा रहा और बेरोज़गारी बढ़ी। निम्नलिखित में से कौन-सा इस स्थिति का सबसे अच्छा वर्णन करता है?",
  ["Stagflation", "Hyperinflation", "Reflation", "Deflation"],
  ["मुद्रास्फीतिजनित मंदी (स्टैगफ़्लेशन)", "अति-मुद्रास्फीति (हाइपरइन्फ़्लेशन)", "पुनर्स्फीति (रिफ़्लेशन)", "अपस्फीति (डिफ़्लेशन)"],
  0,
  "Stagflation -- stagnation plus inflation -- pairs high inflation with high unemployment, the combination the simple Phillips curve said should not occur. Hyperinflation is a runaway rise in prices, often of hundreds of per cent a year, usually from printing money to pay for deficits; reflation is a deliberate policy push to lift prices and output back after a slump; and deflation is a fall in the price level. "
  "Stagflation is hard to treat, because tighter money to curb prices deepens the slump, while looser money to support output feeds the inflation.",
  "मुद्रास्फीतिजनित मंदी, यानी ठहराव और मुद्रास्फीति, ऊँची मुद्रास्फीति को ऊँची बेरोज़गारी से जोड़ती है, वह मेल जिसे सरल फ़िलिप्स वक्र के अनुसार नहीं होना चाहिए था। अति-मुद्रास्फीति क़ीमतों की बेलगाम वृद्धि है, प्रायः सैकड़ों प्रतिशत प्रति वर्ष, जो आम तौर पर घाटे पूरे करने के लिए नोट छापने से होती है; पुनर्स्फीति मंदी के बाद क़ीमतों और उत्पादन को फिर ऊपर लाने का जानबूझकर किया गया नीतिगत प्रयास है; और अपस्फीति क़ीमत-स्तर का गिरना है। "
  "मुद्रास्फीतिजनित मंदी का उपचार कठिन है, क्योंकि क़ीमतें रोकने के लिए सख़्त मौद्रिक नीति मंदी को गहरा करती है, जबकि उत्पादन को सहारा देने के लिए नरम नीति मुद्रास्फीति को बढ़ाती है।",
  NCM, "econ-stagflation", craft="application")

# ================================================================ two-statement rows (5)
S(FM, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The returns of a mutual fund are not guaranteed, because the value of its units moves with the market prices of the securities it holds.",
   "Mutual funds can invest only in government bonds."],
  ["म्यूचुअल फ़ंड के प्रतिफल की गारंटी नहीं होती, क्योंकि उसकी इकाइयों का मूल्य उसके द्वारा रखी प्रतिभूतियों के बाज़ार मूल्यों के साथ बदलता है।",
   "म्यूचुअल फ़ंड केवल सरकारी बॉन्डों में निवेश कर सकते हैं।"],
  T2, 0,
  "Only statement 1 is correct. A fund's net asset value is simply the market value of what it holds, divided among its units, so when share or bond prices fall the units lose value; SEBI regulates the funds, but neither SEBI nor anyone else guarantees their returns -- hence the warning that investments are subject to market risks. "
  "Statement 2 is wrong: funds invest in shares, corporate and government bonds, money market instruments and gold, according to each scheme's mandate.",
  "केवल कथन 1 सही है। फ़ंड का शुद्ध परिसंपत्ति मूल्य उसकी धारित परिसंपत्तियों का बाज़ार मूल्य है जो उसकी इकाइयों में बँटा है, इसलिए शेयरों या बॉन्डों के दाम गिरने पर इकाइयों का मूल्य घटता है; SEBI फ़ंडों को विनियमित करता है, पर न SEBI और न कोई और उनके प्रतिफल की गारंटी देता है, इसीलिए चेतावनी दी जाती है कि निवेश बाज़ार जोखिमों के अधीन हैं। "
  "कथन 2 गलत है: फ़ंड हर योजना के अधिदेश के अनुसार शेयरों, कंपनी और सरकारी बॉन्डों, मुद्रा बाज़ार साधनों और सोने में निवेश करते हैं।",
  SEBI, "fm-mutual-fund-risk-easy", craft="linkage")

S(FM, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Shares represent part ownership of a company.",
   "If a company is wound up, its bondholders are paid out of what is left before its shareholders get anything."],
  ["शेयर किसी कंपनी के आंशिक स्वामित्व को दर्शाते हैं।",
   "यदि कंपनी का समापन होता है, तो बची हुई राशि से उसके बॉन्डधारकों को शेयरधारकों से पहले भुगतान किया जाता है।"],
  T2, 2,
  "Both statements are correct. Shareholders own the company and share in its profits through dividends and rising share prices, but they are residual claimants: in a winding-up, lenders, including bondholders, are paid first, and shareholders get only what is left. That priority, along with a promised interest payment, is why bonds are generally less risky than shares, and why shares can earn more.",
  "दोनों कथन सही हैं। शेयरधारक कंपनी के स्वामी हैं और लाभांश तथा बढ़ते शेयर-मूल्य के रूप में उसके लाभ में भागीदार हैं, पर वे अवशिष्ट दावेदार हैं: समापन में बॉन्डधारकों सहित ऋणदाताओं को पहले भुगतान होता है, और शेयरधारकों को केवल बचा हुआ मिलता है। यही प्राथमिकता, और वचनबद्ध ब्याज भुगतान, कारण है कि बॉन्ड सामान्यतः शेयरों से कम जोखिम वाले हैं, और शेयर अधिक कमा सकते हैं।",
  SEBI, "fm-shares-bonds-easy", craft="linkage")

S(FM, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Money in a fixed deposit can be withdrawn at any time without any penalty.",
   "Banks pay more interest on fixed deposits than on deposits that can be withdrawn on demand, because money locked in for a set period can be lent out with more certainty."],
  ["सावधि जमा का पैसा बिना किसी दंड के कभी भी निकाला जा सकता है।",
   "बैंक माँग पर निकाली जा सकने वाली जमाओं की तुलना में सावधि जमा पर अधिक ब्याज देते हैं, क्योंकि निश्चित अवधि के लिए बँधा पैसा अधिक निश्चितता से उधार दिया जा सकता है।"],
  T2, 1,
  "Only statement 2 is correct. A fixed deposit is a time deposit: the bank knows it will hold the money for the agreed term, so it can lend it for longer and pays a higher rate for that certainty. "
  "Statement 1 is wrong: a fixed deposit can usually be broken before maturity, but the bank then pays a lower rate and often deducts a penalty -- the price of getting the money back early.",
  "केवल कथन 2 सही है। सावधि जमा एक समय-जमा है: बैंक जानता है कि वह तय अवधि तक पैसा रखेगा, इसलिए उसे लंबे समय के लिए उधार दे सकता है और उस निश्चितता के लिए अधिक दर देता है। "
  "कथन 1 गलत है: सावधि जमा प्रायः परिपक्वता से पहले तोड़ी जा सकती है, पर तब बैंक कम दर देता है और अक्सर दंड काटता है, जो पैसा जल्दी वापस पाने की क़ीमत है।",
  RBI, "fm-fixed-deposit-easy", craft="linkage")

S(MC, "easy", "A village has a farmer who grows wheat and a potter who makes pots from clay at home. Consider the following statements:",
  "एक गाँव में गेहूँ उगाने वाला एक किसान और घर पर मिट्टी से बर्तन बनाने वाला एक कुम्हार है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The potter's work belongs to the secondary sector, even though he works by hand at home.",
   "If the farmer also grinds his wheat into flour and sells it, the milling is a primary activity."],
  ["कुम्हार का काम द्वितीयक क्षेत्र में आता है, यद्यपि वह घर पर हाथ से काम करता है।",
   "यदि किसान अपना गेहूँ पीसकर आटा भी बेचता है, तो पिसाई एक प्राथमिक गतिविधि है।"],
  T2, 0,
  "Only statement 1 is correct. The sector depends on what an activity does, not on its size or where it is done: drawing a product straight from nature -- growing wheat, fishing, mining -- is primary; turning a raw material into a new good, whether clay into pots or wheat into flour, is secondary (manufacturing), even in a household unit. "
  "So statement 2 is wrong: once the farmer mills the wheat, he is doing a secondary activity alongside his primary one; selling the flour in the market is a service.",
  "केवल कथन 1 सही है। क्षेत्र इस पर निर्भर है कि गतिविधि क्या करती है, उसके आकार या स्थान पर नहीं: प्रकृति से सीधे उत्पाद लेना, जैसे गेहूँ उगाना, मछली पकड़ना, खनन, प्राथमिक है; कच्चे माल को नई वस्तु में बदलना, चाहे मिट्टी से बर्तन या गेहूँ से आटा, द्वितीयक (विनिर्माण) है, घरेलू इकाई में भी। "
  "इसलिए कथन 2 गलत है: गेहूँ पीसते ही किसान अपनी प्राथमिक गतिविधि के साथ एक द्वितीयक गतिविधि कर रहा है; बाज़ार में आटा बेचना एक सेवा है।",
  NC10E, "econ-sectors-banking-easy", craft="application")

# ================================================================ three-statement rows (6)
S(FM, "medium", "An investor buys a 91-day Treasury bill with a face value of 100 rupees for 98 rupees and holds it until it matures. Consider the following statements:",
  "एक निवेशक 100 रुपये अंकित मूल्य वाला 91-दिवसीय ट्रेज़री बिल 98 रुपये में ख़रीदता है और उसे परिपक्वता तक रखता है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The investor earns 2 rupees per bill.",
   "The bill pays interest every month until it matures.",
   "Treasury bills are issued by the Central Government, not by the State Governments."],
  ["निवेशक प्रति बिल 2 रुपये कमाता है।",
   "बिल परिपक्व होने तक हर महीने ब्याज देता है।",
   "ट्रेज़री बिल केंद्र सरकार जारी करती है, राज्य सरकारें नहीं।"],
  C3, 1,
  "Statements 1 and 3 are correct. A Treasury bill pays no coupon: it is sold at a discount and redeemed at face value, so the investor's return is the difference -- here 2 rupees on 98, a little over 8 per cent a year for a 91-day bill. "
  "The RBI auctions 91-day, 182-day and 364-day bills on behalf of the Centre to meet its short-term needs; the States borrow through State Development Loans instead.",
  "कथन 1 और 3 सही हैं। ट्रेज़री बिल कोई कूपन नहीं देता: यह छूट पर बेचा और अंकित मूल्य पर भुनाया जाता है, इसलिए निवेशक का प्रतिफल अंतर है, यहाँ 98 पर 2 रुपये, जो 91-दिवसीय बिल के लिए वार्षिक 8 प्रतिशत से कुछ अधिक है। "
  "RBI केंद्र की अल्पकालिक आवश्यकताओं के लिए उसकी ओर से 91, 182 और 364 दिनों के बिलों की नीलामी करता है; राज्य इसके बजाय राज्य विकास ऋणों के माध्यम से उधार लेते हैं।",
  RBI, "fm-bond-coupon-zero-tbills", craft="application")

S(FM, "medium", "On a trading day the Nifty 50 falls by 10 per cent within the first hour. Consider the following statements:",
  "एक कारोबारी दिन निफ़्टी 50 पहले घंटे के भीतर 10 प्रतिशत गिर जाता है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["Index-wide circuit breakers would halt trading for a while.",
   "A trader who had sold Nifty shares short before the fall would lose money.",
   "A market in which prices keep falling like this is called a bull market."],
  ["सूचकांक-व्यापी सर्किट ब्रेकर कुछ समय के लिए कारोबार रोक देंगे।",
   "गिरावट से पहले निफ़्टी के शेयर शॉर्ट बेचने वाले व्यापारी को नुक़सान होगा।",
   "इस तरह लगातार गिरते दामों वाले बाज़ार को बुल बाज़ार कहते हैं।"],
  C3, 0,
  "Only statement 1 is correct. Index-wide circuit breakers are set at falls of 10, 15 and 20 per cent; a 10 per cent fall early in the day halts trading across the market for 45 minutes, giving investors time to absorb the news instead of selling in panic. "
  "Statement 2 is the reverse: a short seller sells shares first and buys them back later, so a fall in prices is a gain for him. Statement 3 is wrong: a market of falling prices is a bear market; a bull market is one of rising prices.",
  "केवल कथन 1 सही है। सूचकांक-व्यापी सर्किट ब्रेकर 10, 15 और 20 प्रतिशत की गिरावट पर तय हैं; दिन में जल्दी 10 प्रतिशत गिरावट पूरे बाज़ार में 45 मिनट के लिए कारोबार रोक देती है, जिससे निवेशकों को घबराहट में बेचने के बजाय ख़बर समझने का समय मिलता है। "
  "कथन 2 उलटा है: शॉर्ट विक्रेता पहले शेयर बेचता है और बाद में वापस ख़रीदता है, इसलिए दाम गिरना उसके लिए लाभ है। कथन 3 गलत है: गिरते दामों वाला बाज़ार बियर बाज़ार है; बुल बाज़ार बढ़ते दामों वाला है।",
  SEBI, "fm-circuit-breakers-short-selling-bear", craft="application")

S(FM, "medium", "Consider the following statements about credit rating agencies:",
  "क्रेडिट रेटिंग एजेंसियों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Credit rating agencies in India are regulated by SEBI.",
   "When a company's credit rating is downgraded, it usually has to pay a higher rate of interest on its new borrowing.",
   "CRISIL was India's first credit rating agency."],
  ["भारत में क्रेडिट रेटिंग एजेंसियाँ SEBI द्वारा विनियमित हैं।",
   "जब किसी कंपनी की क्रेडिट रेटिंग घटाई जाती है, तो उसे प्रायः अपने नए ऋण पर अधिक ब्याज दर देनी पड़ती है।",
   "CRISIL भारत की पहली क्रेडिट रेटिंग एजेंसी थी।"],
  C3, 2,
  "All three are correct. A rating judges how likely a borrower is to repay on time; a downgrade tells investors the risk of default has risen, so they demand more interest as compensation, and some funds whose rules allow only highly rated paper must sell the company's bonds, pushing their yields up further. "
  "CRISIL, set up in 1987, was followed by ICRA, CARE and others, all registered with SEBI under its Credit Rating Agencies Regulations, 1999.",
  "तीनों कथन सही हैं। रेटिंग यह आँकती है कि कर्ज़दार के समय पर चुकाने की कितनी संभावना है; रेटिंग घटने से निवेशकों को पता चलता है कि चूक का जोखिम बढ़ा है, इसलिए वे क्षतिपूर्ति के रूप में अधिक ब्याज माँगते हैं, और जिन फ़ंडों के नियम केवल ऊँची रेटिंग वाले काग़ज़ की अनुमति देते हैं उन्हें कंपनी के बॉन्ड बेचने पड़ते हैं, जिससे उनका प्रतिफल और बढ़ता है। "
  "1987 में बनी CRISIL के बाद ICRA, CARE और अन्य आईं, जो सभी SEBI के क्रेडिट रेटिंग एजेंसी विनियम, 1999 के तहत पंजीकृत हैं।",
  SEBI, "fm-credit-rating-agencies", craft="inference")

S(FM, "medium", "Consider the following statements about REITs and InvITs:",
  "REIT और InvIT के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Real Estate Investment Trusts own income-generating property and must distribute most of their income to unit holders.",
   "Infrastructure Investment Trusts let the developers of roads and transmission lines recycle their capital by selling finished, income-earning assets to investors.",
   "REITs and InvITs are regulated by SEBI."],
  ["रियल एस्टेट इन्वेस्टमेंट ट्रस्ट आय देने वाली संपत्ति के स्वामी होते हैं और उन्हें अपनी अधिकांश आय इकाई-धारकों में बाँटनी होती है।",
   "इन्फ़्रास्ट्रक्चर इन्वेस्टमेंट ट्रस्ट सड़कों और पारेषण लाइनों के विकासकर्ताओं को तैयार, आय देने वाली परिसंपत्तियाँ निवेशकों को बेचकर अपनी पूँजी का पुनर्चक्रण करने देते हैं।",
   "REIT और InvIT SEBI द्वारा विनियमित हैं।"],
  C3, 2,
  "All three are correct. Both are trusts that let investors own units in finished, income-earning assets -- office parks and malls for REITs, toll roads, transmission lines and pipelines for InvITs -- and both must pass on at least 90 per cent of their distributable cash flows. "
  "Because the risky construction phase is over, such assets suit pension funds and insurers looking for steady income, while the developer gets back cash to build new projects. Both are governed by SEBI's REIT and InvIT Regulations of 2014.",
  "तीनों कथन सही हैं। दोनों ऐसे ट्रस्ट हैं जो निवेशकों को तैयार, आय देने वाली परिसंपत्तियों में इकाइयाँ रखने देते हैं, REIT के लिए ऑफ़िस पार्क और मॉल, InvIT के लिए टोल सड़कें, पारेषण लाइनें और पाइपलाइनें, और दोनों को अपने वितरण-योग्य नक़द प्रवाह का कम से कम 90 प्रतिशत बाँटना होता है। "
  "चूँकि जोखिम भरा निर्माण चरण समाप्त हो चुका होता है, ऐसी परिसंपत्तियाँ स्थिर आय चाहने वाले पेंशन फ़ंडों और बीमाकर्ताओं के अनुकूल हैं, जबकि विकासकर्ता नई परियोजनाएँ बनाने के लिए नक़द वापस पाता है। दोनों SEBI के 2014 के REIT और InvIT विनियमों के अधीन हैं।",
  SEBI, "fm-reits-invits", craft="linkage")

S(FM, "medium", "Consider the following statements about some digital platforms for commerce and credit:",
  "वाणिज्य और ऋण के कुछ डिजिटल मंचों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Open Network for Digital Commerce (ONDC) is an open network protocol, not an e-commerce marketplace of its own.",
   "On the Trade Receivables Discounting System (TReDS), an MSME's invoice on a large buyer can be financed at a rate based on the buyer's creditworthiness rather than the MSME's own.",
   "Peer-to-peer lending platforms are regulated by SEBI."],
  ["डिजिटल वाणिज्य के लिए खुला नेटवर्क (ONDC) एक खुला नेटवर्क प्रोटोकॉल है, अपना ई-कॉमर्स बाज़ार नहीं।",
   "व्यापार प्राप्य बट्टाकरण प्रणाली (TReDS) पर किसी बड़े ख़रीदार पर MSME के बीजक का वित्तपोषण MSME की अपनी साख के बजाय ख़रीदार की साख पर आधारित दर पर हो सकता है।",
   "पीयर-टू-पीयर ऋण मंच SEBI द्वारा विनियमित हैं।"],
  C3, 1,
  "Statements 1 and 2 are correct. ONDC, a Section 8 company promoted by the Department for Promotion of Industry and Internal Trade, lets any buyer app transact with any seller app, much as UPI did for payments. On TReDS platforms, financiers bid to discount an accepted invoice; since the large buyer, usually a big company or a public sector unit, is the one that will pay, the rate reflects its standing, so a small supplier gets its money early and cheaply. "
  "Statement 3 is wrong: peer-to-peer lending platforms are a class of NBFC registered with and regulated by the RBI.",
  "कथन 1 और 2 सही हैं। उद्योग और आंतरिक व्यापार संवर्धन विभाग द्वारा प्रवर्तित धारा 8 कंपनी ONDC किसी भी ख़रीदार ऐप को किसी भी विक्रेता ऐप से लेन-देन करने देती है, जैसे UPI ने भुगतानों के लिए किया। TReDS मंचों पर वित्तदाता स्वीकृत बीजक को भुनाने के लिए बोली लगाते हैं; चूँकि भुगतान बड़ा ख़रीदार, प्रायः बड़ी कंपनी या सार्वजनिक उपक्रम, करेगा, इसलिए दर उसकी साख दर्शाती है, और छोटे आपूर्तिकर्ता को पैसा जल्दी और सस्ते में मिलता है। "
  "कथन 3 गलत है: पीयर-टू-पीयर ऋण मंच RBI के पास पंजीकृत और उससे विनियमित NBFC की एक श्रेणी हैं।",
  RBI, "fm-ondc-treds-p2p", craft="linkage")

S(FM, "hard", "Consider the following statements about the resolution of bad loans:",
  "डूबे ऋणों के समाधान के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Asset reconstruction companies buy bad loans from banks at their full face value.",
   "Selling bad loans to an asset reconstruction company lets a bank clean up its balance sheet and free capital for fresh lending.",
   "Asset reconstruction companies are regulated by SEBI."],
  ["परिसंपत्ति पुनर्निर्माण कंपनियाँ बैंकों से डूबे ऋण उनके पूरे अंकित मूल्य पर ख़रीदती हैं।",
   "डूबे ऋण किसी परिसंपत्ति पुनर्निर्माण कंपनी को बेचने से बैंक अपना तुलन-पत्र साफ़ कर पाता है और नए ऋण के लिए पूँजी मुक्त कर पाता है।",
   "परिसंपत्ति पुनर्निर्माण कंपनियाँ SEBI द्वारा विनियमित हैं।"],
  C3, 0,
  "Only statement 2 is correct. A bad loan ties up a bank's capital in provisions and its staff in recovery; once it is sold, the bank books whatever loss remains, stops carrying the asset and can lend afresh, while the ARC, a specialist, pursues recovery or restructuring. "
  "Statement 1 is wrong: ARCs buy non-performing loans at a discount, paying partly in cash and partly in security receipts whose value depends on what is recovered. Statement 3 is wrong: ARCs are registered with and regulated by the RBI under the SARFAESI Act, 2002.",
  "केवल कथन 2 सही है। डूबा ऋण बैंक की पूँजी को प्रावधानों में और उसके कर्मचारियों को वसूली में फँसाता है; बेच देने पर बैंक बचा हुआ घाटा दर्ज करता है, परिसंपत्ति ढोना बंद करता है और नए सिरे से उधार दे पाता है, जबकि विशेषज्ञ ARC वसूली या पुनर्गठन करती है। "
  "कथन 1 गलत है: ARC अनर्जक ऋण छूट पर ख़रीदती हैं, कुछ नक़द और कुछ ऐसी प्रतिभूति रसीदों में भुगतान करके जिनका मूल्य वसूली पर निर्भर है। कथन 3 गलत है: SARFAESI अधिनियम, 2002 के तहत ARC RBI के पास पंजीकृत और उससे विनियमित हैं।",
  RBI, "fm-arcs-securitisation", craft="linkage")

S(MB, "medium", "A depositor has 7 lakh rupees in a savings account with an urban cooperative bank, which the RBI then places under a moratorium. Consider the following statements:",
  "एक जमाकर्ता के एक शहरी सहकारी बैंक के बचत खाते में 7 लाख रुपये हैं, जिसके बाद RBI उस बैंक पर अधिस्थगन (मोरेटोरियम) लगा देता है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The depositor is insured by the DICGC up to 5 lakh rupees.",
   "The insured amount is to be paid within about 90 days, even while the moratorium continues.",
   "The depositor will receive the full 7 lakh rupees from the DICGC."],
  ["जमाकर्ता DICGC द्वारा 5 लाख रुपये तक बीमित है।",
   "बीमित राशि का भुगतान लगभग 90 दिनों के भीतर किया जाना है, भले ही अधिस्थगन जारी रहे।",
   "जमाकर्ता को DICGC से पूरे 7 लाख रुपये मिलेंगे।"],
  C3, 1,
  "Statements 1 and 2 are correct. The deposit insurance cover, raised from 1 lakh to 5 lakh rupees per depositor per bank in 2020, applies to commercial banks, regional rural banks and cooperative banks; after depositors of the PMC Bank waited years for their money, the 2021 amendment to the DICGC Act required insured amounts to be paid within about 90 days even while a bank is under moratorium. "
  "Statement 3 is wrong: the DICGC pays only up to 5 lakh rupees; the remaining 2 lakh can come back only if the bank is revived or merged, or from what its assets fetch on liquidation.",
  "कथन 1 और 2 सही हैं। 2020 में प्रति जमाकर्ता प्रति बैंक 1 लाख से 5 लाख रुपये की गई जमा बीमा सुरक्षा वाणिज्यिक बैंकों, क्षेत्रीय ग्रामीण बैंकों और सहकारी बैंकों पर लागू है; PMC बैंक के जमाकर्ताओं के अपने पैसे के लिए वर्षों प्रतीक्षा करने के बाद DICGC अधिनियम के 2021 के संशोधन ने अपेक्षा की कि बीमित राशि लगभग 90 दिनों में दी जाए, भले ही बैंक अधिस्थगन में हो। "
  "कथन 3 गलत है: DICGC केवल 5 लाख रुपये तक देता है; बाक़ी 2 लाख तभी लौट सकते हैं जब बैंक पुनर्जीवित या विलयित हो, या परिसमापन पर उसकी परिसंपत्तियों से जो मिले।",
  "Deposit Insurance and Credit Guarantee Corporation (Amendment) Act, 2021.", "econ-dicgc-ibc-timeline", craft="application")

# ================================================================ TAGS for the 86 kept rows (Test 21's 7 are tagged already)
TAGS = {
 "fm-digital-payments-cash-easy": "linkage", "fm-stock-exchange-trading-easy": "recall", "fm-borrowing-bond-yields": "linkage",
 "fm-fpi-outflows-rupee": "linkage", "fm-card-payments-pss-act": "linkage", "fm-erupee-no-interest": "precision",
 "fm-gold-safe-haven": "linkage", "fm-insurance-penetration": "linkage", "fm-insurance-risk-pooling": "linkage",
 "fm-upi-settlement": "precision", "fm-bond-types-pairs": "precision", "fm-instruments-markets-pairs": "precision",
 "fm-call-option-numerical": "application", "fm-credit-default-swaps": "precision", "fm-current-yield-numerical": "application",
 "fm-e-rupi-voucher": "precision", "fm-free-float-market-cap": "precision", "fm-qip": "precision",
 "fm-regulatory-sandbox": "recall", "fm-scores-grievances": "recall", "fm-unified-lending-interface": "recall",
 "fm-upi-123pay": "recall", "fm-bse-nse-easy": "recall", "fm-cheque-demat-easy": "recall",
 "fm-exchange-regulator-easy": "recall", "fm-insurance-premium-easy": "recall", "fm-upi-debit-card-easy": "recall",
 "fm-at1-bonds": "precision", "fm-bancassurance-micro-ulip": "precision", "fm-beta-systematic-risk": "precision",
 "fm-margin-short-selling": "inference", "fm-tokenisation-blockchain": "precision", "fm-yield-curve-inversion": "linkage",
 "fm-account-aggregators": "precision", "fm-aif-regulation": "precision", "fm-derivatives-futures-options": "precision",
 "fm-erupee-pilots": "recall", "fm-gsecs-sdl-retail-direct": "recall", "fm-ifsca-gift-city": "recall",
 "fm-insurance-irdai-reinsurance-parametric": "precision", "fm-ipo-book-building-anchor-greenshoe": "precision", "fm-masala-green-bonds": "precision",
 "fm-money-market-cp-cd-call": "precision", "fm-mutual-funds-index-open-ended": "precision", "fm-nps-ups-apy": "recall",
 "fm-rtgs-neft": "precision", "fm-sebi-t-plus-one-commodities": "recall", "fm-sensex-nifty-compilers": "recall",
 "fm-upi-npci-interoperability": "recall", "fm-vda-taxation": "precision",
 "econ-investment-multiplier": "inference", "econ-final-good-easy": "application", "econ-personal-disposable-income": "precision",
 "econ-inflation-deflation-easy": "recall", "econ-base-effect-core-inflation": "inference", "econ-phillips-liquidity-trap-laffer": "precision",
 "econ-gdp-deflator": "inference", "econ-gdp-what-counts": "application", "econ-inflation-types-disinflation": "precision",
 "econ-national-income-aggregates": "precision", "econ-price-indices-wpi-cpi": "precision",
 "econ-savings-interest-spread-easy": "linkage", "econ-forex-intervention-sterilisation": "linkage", "econ-omo-government-securities": "precision",
 "econ-repo-transmission": "linkage", "econ-dfi-functions-pairs": "recall", "econ-lender-of-last-resort-easy": "recall",
 "econ-money-multiplier-currency-ratio": "inference", "econ-dicgc-rbi-subsidiary": "recall", "econ-qualitative-moral-suasion": "precision",
 "econ-reduce-liquidity-crr": "application", "econ-rbi-established-easy": "recall", "econ-rbi-vs-commercial-banks-easy": "recall",
 "econ-repo-rate-easy": "recall", "econ-basel-iii": "precision", "econ-loan-pricing-ebllr-mclr": "precision",
 "econ-priority-sector-pslc": "precision", "econ-coop-banks-fsib-rrbs": "recall", "econ-crr-slr": "precision",
 "econ-inflation-targeting-framework": "precision", "econ-money-supply-measures": "precision", "econ-mpc-composition": "precision",
 "econ-nbfc-vs-banks": "precision", "econ-payments-small-finance-banks": "precision", "econ-rbi-functions-debt-notes-tax": "recall",
 "econ-sdf-msf-corridor": "precision"}

if __name__ == "__main__":
    write_updates("upg_l2_t15_econ.sql", statuses=("draft", "published"), tags=TAGS)
