# -*- coding: utf-8 -*-
"""Current Affairs · Test 1 (January to March 2026) -- part B: Economy.

Each question starts from an event of January-March 2026 (the Economic Survey 2025-26, the Union Budget 2026-27, the
Sixteenth Finance Commission's report, the new GDP and CPI series, the India–US trade framework, the LPG shortage of
March) or an anniversary in those months (the Regional Rural Banks Act, 1976; the Trade Unions Act, 1926), and asks
the static economics behind it. Every fact was searched in the whole UPSC bank and is one no row tests."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Economy"
d.REQUIRE_CRAFT = True
BD = "Budget, Deficits & Public Debt"
TF = "Taxation & Fiscal Federalism"
MC = "Macro Concepts, National Income & Inflation"
MB = "Money, Banking & Monetary Policy"
IN = "Industry, Infrastructure, Energy & Services"
GD = "Growth, Development, Poverty & Planning"
IG = "Inclusive Growth, Welfare & Demography"
EX = "External Sector & International Institutions"
AG = "Agriculture & Food Economy"

M(BD, "hard",
  "In the Union Budget 2026-27 the fiscal deficit is estimated at 4.3 per cent of GDP and the revenue deficit at 1.5 per cent of GDP. Which one of the following can be correctly inferred from these two figures?",
  "केंद्रीय बजट 2026-27 में राजकोषीय घाटा जीडीपी का 4.3 प्रतिशत और राजस्व घाटा जीडीपी का 1.5 प्रतिशत अनुमानित है। इन दो आँकड़ों से निम्नलिखित में से कौन-सा निष्कर्ष सही निकाला जा सकता है?",
  ["About two-thirds of the borrowing is budgeted for spending other than revenue expenditure, such as capital outlay",
   "The government is budgeted to run a primary surplus, since its interest payments are larger than the fiscal deficit",
   "The government's revenue receipts are budgeted to exceed its revenue expenditure in that year",
   "Interest payments are budgeted at 2.8 per cent of GDP, which is the difference between the two deficits"],
  ["लगभग दो-तिहाई उधारी राजस्व व्यय से भिन्न व्यय, जैसे पूँजीगत परिव्यय, के लिए बजट की गई है",
   "सरकार के प्राथमिक अधिशेष चलाने का बजट है, क्योंकि उसके ब्याज भुगतान राजकोषीय घाटे से अधिक हैं",
   "उस वर्ष सरकार की राजस्व प्राप्तियाँ उसके राजस्व व्यय से अधिक रहने का बजट है",
   "ब्याज भुगतान जीडीपी के 2.8 प्रतिशत पर बजट किए गए हैं, जो दोनों घाटों का अंतर है"],
  0,
  "The fiscal deficit is the government's total borrowing requirement; the revenue deficit is the part of it that pays for revenue (day-to-day) spending in excess of revenue receipts. The gap of 2.8 per cent of GDP is therefore borrowing used for capital outlay and net lending -- about 2.8/4.3, or two-thirds, of the total -- which is why a falling revenue deficit is read as an improvement in the quality of the deficit even when the fiscal deficit falls slowly. "
  "The other options misread the identities. A positive revenue deficit means revenue receipts fall short of revenue expenditure. The primary deficit is the fiscal deficit minus interest payments; the Centre's interest bill is smaller than its fiscal deficit, so the primary balance is still a deficit, not a surplus. And the difference between the fiscal and revenue deficits measures capital-side borrowing, not interest.",
  "राजकोषीय घाटा सरकार की कुल उधारी आवश्यकता है; राजस्व घाटा उसका वह भाग है जो राजस्व प्राप्तियों से अधिक राजस्व (दैनिक) व्यय को चुकाता है। इसलिए जीडीपी के 2.8 प्रतिशत का अंतर पूँजीगत परिव्यय और शुद्ध उधार के लिए ली गई उधारी है -- कुल का लगभग 2.8/4.3, यानी दो-तिहाई -- इसीलिए घटते राजस्व घाटे को घाटे की गुणवत्ता में सुधार माना जाता है, भले ही राजकोषीय घाटा धीरे घटे। "
  "अन्य विकल्प सर्वसमिकाओं को ग़लत पढ़ते हैं। धनात्मक राजस्व घाटे का अर्थ है कि राजस्व प्राप्तियाँ राजस्व व्यय से कम हैं। प्राथमिक घाटा राजकोषीय घाटे में से ब्याज भुगतान घटाकर निकलता है; केंद्र का ब्याज-बिल उसके राजकोषीय घाटे से छोटा है, इसलिए प्राथमिक संतुलन अब भी घाटा है, अधिशेष नहीं। और राजकोषीय और राजस्व घाटों का अंतर पूँजीगत पक्ष की उधारी मापता है, ब्याज नहीं।",
  "Union Budget 2026-27, Budget at a Glance and Budget Speech (1 February 2026); NCERT, Introductory Macroeconomics (Class XII), Chapter 5 (Government Budget and the Economy).",
  "ca-t1-eco-budget-fd-rd-quality-of-deficit", pos=0, craft="application")

S(TF, "hard", "With reference to the report of the Sixteenth Finance Commission, laid before Parliament on 1 February 2026, consider the following statements:",
  "1 फ़रवरी 2026 को संसद के समक्ष रखी गई सोलहवें वित्त आयोग की रिपोर्ट के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["It kept the States' share of the divisible pool of Central taxes at 41 per cent for 2026-31.",
   "It introduced a criterion based on each State's contribution to the national GDP and dropped the 'tax and fiscal effort' criterion.",
   "Among the criteria for sharing taxes among the States, it gave population the largest weight."],
  ["इसने 2026-31 के लिए केंद्रीय करों के विभाज्य पूल में राज्यों का हिस्सा 41 प्रतिशत बनाए रखा।",
   "इसने प्रत्येक राज्य के राष्ट्रीय जीडीपी में योगदान पर आधारित एक मानदंड जोड़ा और ‘कर और राजकोषीय प्रयास’ का मानदंड हटा दिया।",
   "राज्यों के बीच करों के बँटवारे के मानदंडों में इसने जनसंख्या को सबसे अधिक भार दिया।"],
  C3, 1,
  "Statements 1 and 2 are correct. The Commission, chaired by Arvind Panagariya, retained the vertical share at 41 per cent, as the Fifteenth had, and the Union accepted it. For the horizontal sharing it added 'contribution to GDP' with a weight of 10 per cent, worked out on a dampened (square-root) scale, and removed the 2.5 per cent 'tax and fiscal effort' criterion; the result raised the shares of several southern and western States. "
  "Statement 3 is wrong: income distance -- how far a State's per capita income lies below that of the richest States -- still carries the largest weight, 42.5 per cent (down from 45). Population (of 2011) carries 17.5 per cent, and area, forest and ecology, demographic performance and the new GDP criterion 10 per cent each.",
  "कथन 1 और 2 सही हैं। अरविंद पनगढ़िया की अध्यक्षता वाले आयोग ने पंद्रहवें की तरह ऊर्ध्वाधर हिस्सा 41 प्रतिशत रखा, और केंद्र ने इसे स्वीकार किया। क्षैतिज बँटवारे के लिए उसने ‘जीडीपी में योगदान’ को 10 प्रतिशत भार के साथ, एक मंद (वर्गमूल) पैमाने पर गणना करके, जोड़ा और 2.5 प्रतिशत वाला ‘कर और राजकोषीय प्रयास’ मानदंड हटाया; इससे कई दक्षिणी और पश्चिमी राज्यों के हिस्से बढ़े। "
  "कथन 3 ग़लत है: आय-दूरी -- किसी राज्य की प्रति व्यक्ति आय सबसे धनी राज्यों से कितनी नीचे है -- को अब भी सबसे अधिक भार, 42.5 प्रतिशत (45 से घटाकर), मिला है। जनसंख्या (2011 की) को 17.5 प्रतिशत, और क्षेत्रफल, वन और पारिस्थितिकी, जनसांख्यिकीय प्रदर्शन तथा नए जीडीपी मानदंड को 10-10 प्रतिशत भार मिला है।",
  "Report of the Sixteenth Finance Commission (2026-27 to 2030-31) and the Explanatory Memorandum on the Action Taken (February 2026); Constitution of India, Article 280.",
  "ca-t1-eco-sixteenth-fc-criteria-gdp-contribution", craft="precision")

A(TF, "hard",
  "The share of the Union's gross tax revenue that actually reaches the States is well below the share of the divisible pool that the Finance Commission recommends for them.",
  "केंद्र के सकल कर राजस्व का जो हिस्सा वास्तव में राज्यों तक पहुँचता है, वह वित्त आयोग द्वारा उनके लिए अनुशंसित विभाज्य पूल के हिस्से से काफ़ी कम है।",
  "Cesses and surcharges levied by the Union are excluded from the divisible pool of taxes shared with the States.",
  "केंद्र द्वारा लगाए गए उपकर और अधिभार राज्यों के साथ बाँटे जाने वाले करों के विभाज्य पूल से बाहर रखे जाते हैं।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I. Under Article 270, the taxes on the Union List are shared with the States, but clause (1) excludes surcharges (Article 271) and cesses levied for specific purposes, and the net proceeds are also reduced by the cost of collection. The 41 per cent applies only to what remains -- the divisible pool. "
  "Because the Union has raised a growing share of its revenue through cesses and surcharges, the divisible pool is a smaller part of gross tax revenue, so the States' effective share of gross collections has been in the low-to-mid thirties. This '41 per cent illusion' was a central complaint of the States before the Sixteenth Finance Commission.",
  "दोनों कथन सही हैं, और कथन-II कथन-I की सही व्याख्या है। अनुच्छेद 270 के अंतर्गत संघ सूची के कर राज्यों के साथ बाँटे जाते हैं, पर उसका खंड (1) अधिभारों (अनुच्छेद 271) और विशिष्ट प्रयोजनों के लिए लगाए गए उपकरों को बाहर रखता है, और शुद्ध आगम से संग्रहण की लागत भी घटाई जाती है। 41 प्रतिशत केवल शेष पर -- विभाज्य पूल पर -- लागू होता है। "
  "चूँकि केंद्र ने अपने राजस्व का बढ़ता हिस्सा उपकरों और अधिभारों से जुटाया है, विभाज्य पूल सकल कर राजस्व का छोटा भाग रह गया है, इसलिए सकल संग्रह में राज्यों का प्रभावी हिस्सा तीस के निचले से मध्य प्रतिशत के बीच रहा है। यह ‘41 प्रतिशत का भ्रम’ सोलहवें वित्त आयोग के समक्ष राज्यों की प्रमुख शिकायत थी।",
  "Constitution of India, Articles 270, 271 and 279; Report of the Sixteenth Finance Commission (2026).",
  "ca-t1-eco-cess-surcharge-outside-divisible-pool", craft="inference")

S(MC, "medium", "On 27 February 2026 the National Statistics Office released a new series of national accounts. Consider the following statements:",
  "27 फ़रवरी 2026 को राष्ट्रीय सांख्यिकी कार्यालय ने राष्ट्रीय लेखों की एक नई शृंखला जारी की। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The new series uses 2022-23 as its base year, replacing 2011-12.",
   "It draws on newer administrative data sources such as GST returns.",
   "A change of base year can change the growth rates already published for earlier years."],
  ["नई शृंखला 2011-12 के स्थान पर 2022-23 को आधार वर्ष मानती है।",
   "यह जीएसटी विवरणियों जैसे नए प्रशासनिक आँकड़ों के स्रोतों का उपयोग करती है।",
   "आधार वर्ष बदलने से पहले के वर्षों की पहले से प्रकाशित वृद्धि दरें बदल सकती हैं।"],
  C3, 2,
  "All three statements are correct. The base year is revised so that the weights of sectors, the basket of goods and the data sources reflect the current economy; the previous revision, in 2015, had moved the base from 2004-05 to 2011-12. The 2022-23 series uses GST returns, corporate filings and other digital records to capture parts of the economy, especially the informal and services sectors, that older surveys measured poorly. "
  "Because the whole back series is recomputed on the new weights and sources, the growth rates of earlier years change too: the new series lowered the estimate for 2023-24 and raised later years, and it showed a larger farm sector -- which is why such revisions are always followed by debate over comparability.",
  "तीनों कथन सही हैं। आधार वर्ष इसलिए बदला जाता है कि क्षेत्रों के भार, वस्तुओं की टोकरी और आँकड़ों के स्रोत वर्तमान अर्थव्यवस्था को दर्शाएँ; पिछला संशोधन, 2015 में, आधार को 2004-05 से 2011-12 पर लाया था। 2022-23 की शृंखला जीएसटी विवरणियों, कंपनी दाख़िलों और अन्य डिजिटल अभिलेखों का उपयोग अर्थव्यवस्था के उन भागों, विशेषकर अनौपचारिक और सेवा क्षेत्रों, को पकड़ने के लिए करती है जिन्हें पुराने सर्वेक्षण ठीक से नहीं माप पाते थे। "
  "चूँकि पूरी पिछली शृंखला नए भारों और स्रोतों पर फिर से गणना की जाती है, पहले के वर्षों की वृद्धि दरें भी बदलती हैं: नई शृंखला ने 2023-24 का अनुमान घटाया और बाद के वर्षों का बढ़ाया, और एक बड़ा कृषि क्षेत्र दिखाया -- इसीलिए ऐसे संशोधनों के बाद तुलनीयता पर बहस होती ही है।",
  "Ministry of Statistics and Programme Implementation, National Statistics Office, release of the new series of National Accounts with base year 2022-23 (27 February 2026).",
  "ca-t1-eco-gdp-new-series-2022-23", craft="inference")

S(MC, "hard", "In February 2026 the National Statistics Office replaced the Consumer Price Index series of 2012 with a new series. Consider the following statements about the new series:",
  "फ़रवरी 2026 में राष्ट्रीय सांख्यिकी कार्यालय ने 2012 की उपभोक्ता मूल्य सूचकांक शृंखला के स्थान पर एक नई शृंखला लागू की। नई शृंखला के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Its base year is 2024.",
   "Food and beverages carry a smaller weight in it than in the 2012 series.",
   "Its weights are drawn from the Household Consumption Expenditure Survey of 2023-24.",
   "Grain that households receive free under the PM Garib Kalyan Anna Yojana is given no weight in it."],
  ["इसका आधार वर्ष 2024 है।",
   "इसमें खाद्य और पेय पदार्थों का भार 2012 की शृंखला से कम है।",
   "इसके भार 2023-24 के घरेलू उपभोग व्यय सर्वेक्षण से लिए गए हैं।",
   "पीएम ग़रीब कल्याण अन्न योजना के अंतर्गत परिवारों को मुफ़्त मिलने वाले अनाज को इसमें कोई भार नहीं दिया गया है।"],
  C4, 3,
  "All four statements are correct. The new CPI (2024 = 100), whose first reading -- 2.75 per cent for January 2026 -- came out on 12 February, takes its weights from the 2023-24 consumption survey. The weight of food and beverages fell from about 46 per cent to about 37 per cent, because households now spend a smaller share on food, while housing, transport and communication gained; the basket grew from 299 to 358 items, adding services such as streaming, and prices are now also collected from online markets. "
  "Free grain carries no price and households spend nothing on it, so it is given no weight. These changes matter beyond statistics: CPI inflation is the target of the RBI's monetary policy, so a smaller food weight makes the headline rate less sensitive to vegetable and pulse prices.",
  "चारों कथन सही हैं। नया सीपीआई (2024 = 100), जिसकी पहली रीडिंग -- जनवरी 2026 के लिए 2.75 प्रतिशत -- 12 फ़रवरी को आई, अपने भार 2023-24 के उपभोग सर्वेक्षण से लेता है। खाद्य और पेय का भार लगभग 46 प्रतिशत से घटकर लगभग 37 प्रतिशत रह गया, क्योंकि परिवार अब भोजन पर कम हिस्सा ख़र्च करते हैं, जबकि आवास, परिवहन और संचार का भार बढ़ा; टोकरी 299 से बढ़कर 358 वस्तुओं की हो गई, जिसमें स्ट्रीमिंग जैसी सेवाएँ जुड़ीं, और क़ीमतें अब ऑनलाइन बाज़ारों से भी ली जाती हैं। "
  "मुफ़्त अनाज की कोई क़ीमत नहीं होती और परिवार उस पर कुछ ख़र्च नहीं करते, इसलिए उसे कोई भार नहीं दिया गया। ये बदलाव आँकड़ों से आगे भी मायने रखते हैं: सीपीआई मुद्रास्फीति रिज़र्व बैंक की मौद्रिक नीति का लक्ष्य है, इसलिए खाद्य का छोटा भार मुख्य दर को सब्ज़ियों और दालों की क़ीमतों के प्रति कम संवेदनशील बनाता है।",
  "Ministry of Statistics and Programme Implementation, release of the Consumer Price Index (base 2024 = 100) and its methodology note (12 February 2026).",
  "ca-t1-eco-cpi-2024-series-weights", craft="multi")

S(MB, "medium", "February 2026 marked fifty years of the Regional Rural Banks Act, 1976. Consider the following statements about Regional Rural Banks:",
  "फ़रवरी 2026 में क्षेत्रीय ग्रामीण बैंक अधिनियम, 1976 के पचास वर्ष पूरे हुए। क्षेत्रीय ग्रामीण बैंकों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The first Regional Rural Banks were set up in 1975, under an ordinance later replaced by the Act of 1976.",
   "Like commercial banks, they need lend only 40 per cent of their adjusted net bank credit to the priority sectors.",
   "Under the 'One State, One RRB' policy, all of them have been merged into a single national rural bank."],
  ["पहले क्षेत्रीय ग्रामीण बैंक 1975 में एक अध्यादेश के अंतर्गत बने, जिसका स्थान बाद में 1976 के अधिनियम ने लिया।",
   "वाणिज्यिक बैंकों की तरह, उन्हें अपने समायोजित शुद्ध बैंक ऋण का केवल 40 प्रतिशत प्राथमिकता क्षेत्रों को देना होता है।",
   "‘एक राज्य, एक आरआरबी’ नीति के अंतर्गत उन सभी का विलय एक राष्ट्रीय ग्रामीण बैंक में कर दिया गया है।"],
  C3, 0,
  "Only statement 1 is correct. On the recommendation of the Narasimham working group, the first RRBs -- among them Prathama Bank at Moradabad -- opened on 2 October 1975 under an ordinance, which the Regional Rural Banks Act replaced in February 1976. They were meant to combine the local feel of cooperatives with the business methods of commercial banks for small farmers, labourers and artisans; they are owned by the Union (50 per cent), a sponsor bank (35 per cent) and the State (15 per cent), regulated by the RBI and supervised by NABARD. "
  "Statement 2 is wrong: RRBs carry a much higher priority-sector target, 75 per cent of adjusted net bank credit. Statement 3 is wrong: the 'One State, One RRB' amalgamation of May 2025 merged the banks within each State, cutting their number to 28, not into one national bank.",
  "केवल कथन 1 सही है। नरसिंहम कार्य-समूह की सिफ़ारिश पर पहले आरआरबी -- जिनमें मुरादाबाद का प्रथमा बैंक था -- 2 अक्टूबर 1975 को एक अध्यादेश के अंतर्गत खुले, जिसका स्थान फ़रवरी 1976 में क्षेत्रीय ग्रामीण बैंक अधिनियम ने लिया। इनका उद्देश्य छोटे किसानों, मज़दूरों और कारीगरों के लिए सहकारी संस्थाओं की स्थानीय समझ को वाणिज्यिक बैंकों की कार्यप्रणाली से जोड़ना था; इनका स्वामित्व केंद्र (50 प्रतिशत), प्रायोजक बैंक (35 प्रतिशत) और राज्य (15 प्रतिशत) के पास है, विनियमन रिज़र्व बैंक करता है और पर्यवेक्षण नाबार्ड। "
  "कथन 2 ग़लत है: आरआरबी पर कहीं ऊँचा प्राथमिकता-क्षेत्र लक्ष्य है, समायोजित शुद्ध बैंक ऋण का 75 प्रतिशत। कथन 3 ग़लत है: मई 2025 के ‘एक राज्य, एक आरआरबी’ समामेलन ने हर राज्य के भीतर के बैंकों का विलय किया, जिससे उनकी संख्या 28 रह गई, न कि उन्हें एक राष्ट्रीय बैंक में मिलाया।",
  "Regional Rural Banks Act, 1976; Reserve Bank of India, Master Directions on Priority Sector Lending; Department of Financial Services, notification on the amalgamation of RRBs (April 2025).",
  "ca-t1-eco-rrb-fifty-years-75-percent-psl", craft="precision")

M(IN, "medium",
  "The Union Budget 2026-27 announced Rare Earth Corridors in Odisha, Kerala, Andhra Pradesh and Tamil Nadu. What these States have in common that makes them suitable is:",
  "केंद्रीय बजट 2026-27 ने ओडिशा, केरल, आंध्र प्रदेश और तमिलनाडु में दुर्लभ मृदा गलियारों की घोषणा की। इन राज्यों में ऐसा क्या समान है जो इन्हें उपयुक्त बनाता है?",
  ["beach-sand deposits on their coasts that contain monazite, a source of rare earth elements",
   "large bauxite deposits in the Eastern Ghats that yield rare earths as a by-product of alumina",
   "the country's main reserves of lithium, found in pegmatite belts close to their coasts",
   "deep-water ports through which most of India's imports of rare earth magnets arrive"],
  ["उनके तटों पर मोनाज़ाइट युक्त समुद्र-तटीय बालू के भंडार, जो दुर्लभ मृदा तत्वों का स्रोत है",
   "पूर्वी घाट में बॉक्साइट के बड़े भंडार, जो एल्युमिना के उप-उत्पाद के रूप में दुर्लभ मृदा देते हैं",
   "देश के लिथियम के मुख्य भंडार, जो उनके तटों के पास पेग्मेटाइट पट्टियों में मिलते हैं",
   "गहरे जल वाले बंदरगाह, जिनसे दुर्लभ मृदा चुंबकों का भारत का अधिकांश आयात आता है"],
  0,
  "The heavy-mineral sands of the coasts of Kerala, Tamil Nadu, Odisha and Andhra Pradesh contain monazite, a phosphate mineral that carries rare earth elements such as neodymium along with thorium; IREL (India) Limited mines and processes these sands. The corridors are meant to link mining, separation, research and the making of products such as permanent magnets in the same belt, cutting dependence on imports from China, and complement the rare-earth permanent magnet scheme of November 2025. "
  "The other options do not fit all four States. Bauxite lies in the Eastern Ghats of Odisha and Andhra Pradesh but not on the Kerala coast; India's lithium finds, such as the one in Jammu and Kashmir, are not in these coastal States; and imports, not deposits, are no reason to site mining and processing corridors.",
  "केरल, तमिलनाडु, ओडिशा और आंध्र प्रदेश के तटों की भारी-खनिज बालू में मोनाज़ाइट है, एक फ़ॉस्फ़ेट खनिज जो थोरियम के साथ नियोडिमियम जैसे दुर्लभ मृदा तत्व रखता है; आईआरईएल (इंडिया) लिमिटेड इन बालुओं का खनन और प्रसंस्करण करती है। गलियारों का उद्देश्य एक ही पट्टी में खनन, पृथक्करण, अनुसंधान और स्थायी चुंबकों जैसे उत्पादों के निर्माण को जोड़कर चीन से आयात पर निर्भरता घटाना है, और ये नवंबर 2025 की दुर्लभ मृदा स्थायी चुंबक योजना के पूरक हैं। "
  "अन्य विकल्प चारों राज्यों पर लागू नहीं होते। बॉक्साइट ओडिशा और आंध्र प्रदेश के पूर्वी घाट में है पर केरल के तट पर नहीं; भारत की लिथियम खोजें, जैसे जम्मू और कश्मीर वाली, इन तटीय राज्यों में नहीं हैं; और आयात, भंडार नहीं, खनन और प्रसंस्करण गलियारे बसाने का कारण नहीं होते।",
  "Union Budget 2026-27, Budget Speech (1 February 2026); Ministry of Mines and Department of Atomic Energy (IREL (India) Limited); NCERT, India: People and Economy (Class XII), Chapter 7.",
  "ca-t1-eco-rare-earth-corridors-monazite", pos=2, craft="inference")

S(IN, "medium", "The Union Budget 2026-27 announced the India Semiconductor Mission 2.0. Consider the following statements:",
  "केंद्रीय बजट 2026-27 ने इंडिया सेमीकंडक्टर मिशन 2.0 की घोषणा की। निम्नलिखित कथनों पर विचार कीजिए:",
  ["Most of the world's capacity to make the most advanced chips is concentrated in Taiwan.",
   "The second phase of the Mission aims to go beyond fabs and assembly units to semiconductor equipment, materials and Indian chip-design IP.",
   "The fab being built at Dholera is designed to make chips at the 3-nanometre node, the most advanced in commercial production."],
  ["विश्व की सबसे उन्नत चिप बनाने की अधिकांश क्षमता ताइवान में केंद्रित है।",
   "मिशन का दूसरा चरण फ़ैब और असेंबली इकाइयों से आगे सेमीकंडक्टर उपकरण, सामग्री और भारतीय चिप-डिज़ाइन बौद्धिक संपदा तक जाना चाहता है।",
   "धोलेरा में बन रहा फ़ैब 3-नैनोमीटर नोड पर चिप बनाने के लिए बनाया गया है, जो वाणिज्यिक उत्पादन में सबसे उन्नत है।"],
  C3, 1,
  "Statements 1 and 2 are correct. The leading-edge nodes are made almost entirely by a handful of firms, above all TSMC in Taiwan -- the concentration that turned chips into a strategic issue and lies behind supply-chain groupings such as Pax Silica. The first phase of the Mission funded fabs and assembly-and-test units; the second phase, announced on 1 February 2026, moves to the parts of the supply chain India lacks, such as equipment, specialty chemicals and gases, and design IP, alongside a doubled outlay for electronics components. "
  "Statement 3 is wrong: the Tata Electronics–PSMC fab at Dholera is planned for mature nodes, roughly 28 nm and above, which go into cars, power electronics, telecom and consumer devices; India's strategy is to enter through these high-volume nodes rather than the most advanced ones.",
  "कथन 1 और 2 सही हैं। अग्रणी नोड लगभग पूरी तरह कुछ फ़र्मों, सबसे बढ़कर ताइवान की टीएसएमसी, द्वारा बनाए जाते हैं -- इसी केंद्रीकरण ने चिप को सामरिक मुद्दा बनाया और पैक्स सिलिका जैसे आपूर्ति-शृंखला समूहों के पीछे यही है। मिशन के पहले चरण ने फ़ैब और असेंबली-और-परीक्षण इकाइयों को धन दिया; 1 फ़रवरी 2026 को घोषित दूसरा चरण आपूर्ति शृंखला के उन भागों की ओर जाता है जो भारत में नहीं हैं, जैसे उपकरण, विशेष रसायन और गैसें, और डिज़ाइन बौद्धिक संपदा, साथ ही इलेक्ट्रॉनिक्स घटकों के लिए दोगुना परिव्यय। "
  "कथन 3 ग़लत है: धोलेरा में टाटा इलेक्ट्रॉनिक्स–पीएसएमसी फ़ैब परिपक्व नोडों, मोटे तौर पर 28 नैनोमीटर और उससे ऊपर, के लिए नियोजित है, जो कारों, पावर इलेक्ट्रॉनिक्स, दूरसंचार और उपभोक्ता उपकरणों में लगते हैं; भारत की रणनीति सबसे उन्नत नोडों के बजाय इन्हीं अधिक मात्रा वाले नोडों से प्रवेश की है।",
  "Union Budget 2026-27, Budget Speech; Ministry of Electronics and Information Technology, India Semiconductor Mission, approved projects.",
  "ca-t1-eco-ism-2-fab-osat-dholera", craft="precision")

S(IN, "medium", "The Union Budget 2026-27 announced 'Biopharma SHAKTI', a programme for biologics and biosimilars. Consider the following statements:",
  "केंद्रीय बजट 2026-27 ने जैविक औषधियों और बायोसिमिलर के लिए ‘बायोफ़ार्मा शक्ति’ कार्यक्रम की घोषणा की। निम्नलिखित कथनों पर विचार कीजिए:",
  ["Biologics, such as monoclonal antibodies and insulin, are medicines produced in or from living cells.",
   "A biosimilar is an exact chemical copy of an off-patent biologic, made and approved in the same way as a generic chemical drug."],
  ["जैविक औषधियाँ, जैसे मोनोक्लोनल एंटीबॉडी और इंसुलिन, जीवित कोशिकाओं में या उनसे बनाई जाने वाली दवाएँ हैं।",
   "बायोसिमिलर पेटेंट-मुक्त जैविक औषधि की हूबहू रासायनिक प्रति है, जो सामान्य रासायनिक दवा की जेनेरिक की तरह ही बनाई और अनुमोदित की जाती है।"],
  T2, 0,
  "Only statement 1 is correct. Biologics are large, complex molecules -- antibodies, hormones such as insulin, vaccines -- made by engineered living cells, and their manufacture is far harder to control than chemical synthesis. Biopharma SHAKTI, with an outlay of about ₹10,000 crore over five years, aims to make India a hub for them through new and upgraded NIPERs, a network of accredited clinical-trial sites and a stronger drug regulator. "
  "Statement 2 is wrong: because a living process cannot reproduce a large protein identically, a biosimilar is only 'highly similar' to the reference product, with no clinically meaningful difference; it is approved on comparative analytical and clinical data, a heavier process than the bioequivalence test for a generic copy of a small chemical molecule.",
  "केवल कथन 1 सही है। जैविक औषधियाँ बड़े, जटिल अणु हैं -- एंटीबॉडी, इंसुलिन जैसे हार्मोन, टीके -- जो अभियांत्रिक जीवित कोशिकाओं द्वारा बनते हैं, और इनके निर्माण को नियंत्रित करना रासायनिक संश्लेषण से कहीं कठिन है। लगभग ₹10,000 करोड़ के पाँच-वर्षीय परिव्यय वाला बायोफ़ार्मा शक्ति नए और उन्नत नाइपर, मान्यता-प्राप्त नैदानिक परीक्षण स्थलों के जाल और मज़बूत औषधि नियामक के माध्यम से भारत को इनका केंद्र बनाना चाहता है। "
  "कथन 2 ग़लत है: चूँकि जीवित प्रक्रिया किसी बड़े प्रोटीन को हूबहू नहीं दोहरा सकती, बायोसिमिलर संदर्भ उत्पाद से केवल ‘अत्यधिक समान’ होता है, बिना किसी नैदानिक रूप से सार्थक अंतर के; उसका अनुमोदन तुलनात्मक विश्लेषणात्मक और नैदानिक आँकड़ों पर होता है, जो छोटे रासायनिक अणु की जेनेरिक प्रति की जैव-समतुल्यता जाँच से भारी प्रक्रिया है।",
  "Union Budget 2026-27, Budget Speech; Central Drugs Standard Control Organisation and Department of Biotechnology, Guidelines on Similar Biologics (2016).",
  "ca-t1-eco-biopharma-shakti-biosimilars", craft="precision")

S(GD, "hard", "With reference to the Economic Survey 2025-26, tabled on 29 January 2026, consider the following statements:",
  "29 जनवरी 2026 को प्रस्तुत आर्थिक समीक्षा 2025-26 के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["It put India's medium-term potential growth rate at about 7 per cent.",
   "It found that business enterprises account for a larger share of research and development spending in India than in China."],
  ["इसने भारत की मध्यम-अवधि की संभावित वृद्धि दर लगभग 7 प्रतिशत आँकी।",
   "इसने पाया कि अनुसंधान और विकास व्यय में व्यावसायिक उद्यमों का हिस्सा भारत में चीन से अधिक है।"],
  T2, 0,
  "Only statement 1 is correct. The Survey, prepared under the Chief Economic Adviser, raised its estimate of India's medium-term growth potential to about 7 per cent, estimated growth of 7.4 per cent for 2025-26 and projected 6.8 to 7.2 per cent for 2026-27, driven mainly by domestic demand. "
  "Statement 2 reverses the finding: India spends only about 0.64 per cent of GDP on R&D, and business enterprises account for about 41 per cent of it, against about 77 per cent in China. The Survey used this gap to argue for far more private R&D, and recommended that India pursue application-led AI that builds on its human capital rather than racing to build frontier models.",
  "केवल कथन 1 सही है। मुख्य आर्थिक सलाहकार के अधीन तैयार समीक्षा ने भारत की मध्यम-अवधि की संभावित वृद्धि का अनुमान बढ़ाकर लगभग 7 प्रतिशत किया, 2025-26 के लिए 7.4 प्रतिशत वृद्धि आँकी और 2026-27 के लिए 6.8 से 7.2 प्रतिशत का अनुमान लगाया, जो मुख्यतः घरेलू माँग से प्रेरित है। "
  "कथन 2 निष्कर्ष को उलट देता है: भारत अनुसंधान और विकास पर जीडीपी का केवल लगभग 0.64 प्रतिशत ख़र्च करता है, और उसमें व्यावसायिक उद्यमों का हिस्सा लगभग 41 प्रतिशत है, जबकि चीन में लगभग 77 प्रतिशत। समीक्षा ने इस अंतर से कहीं अधिक निजी अनुसंधान का तर्क दिया, और सिफ़ारिश की कि भारत अग्रणी मॉडल बनाने की दौड़ के बजाय अपनी मानव पूँजी पर आधारित, अनुप्रयोग-आधारित एआई अपनाए।",
  "Ministry of Finance, Economic Survey 2025-26 (29 January 2026), Volume I, chapters on the state of the economy, industry and AI.",
  "ca-t1-eco-survey-2025-26-potential-growth-rnd", craft="precision")

S(IG, "hard", "March 2026 marked a hundred years since the Indian Trade Unions Act was passed. Consider the following statements:",
  "मार्च 2026 में भारतीय ट्रेड यूनियन अधिनियम पारित होने के सौ वर्ष पूरे हुए। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Trade Unions Act, 1926 provided for the registration of trade unions and gave registered unions protection from certain civil and criminal liability.",
   "That Act has been subsumed in the Industrial Relations Code, 2020, which came into force in November 2025.",
   "Under the Industrial Relations Code, prior government permission for lay-off, retrenchment or closure is needed in establishments employing 100 or more workers."],
  ["ट्रेड यूनियन अधिनियम, 1926 ने ट्रेड यूनियनों के पंजीकरण का प्रावधान किया और पंजीकृत यूनियनों को कुछ सिविल और आपराधिक दायित्वों से संरक्षण दिया।",
   "वह अधिनियम औद्योगिक संबंध संहिता, 2020 में समाहित हो गया है, जो नवंबर 2025 में लागू हुई।",
   "औद्योगिक संबंध संहिता के अंतर्गत 100 या अधिक कर्मकार वाले प्रतिष्ठानों में ले-ऑफ़, छँटनी या बंदी के लिए सरकार की पूर्व अनुमति आवश्यक है।"],
  C3, 1,
  "Statements 1 and 2 are correct. The Trade Unions Act, passed in March 1926 after the growth of the labour movement and the founding of the All India Trade Union Congress in 1920, let unions register and protected registered unions from prosecution for criminal conspiracy and from civil suits over acts in furtherance of a trade dispute. It was one of three laws merged into the Industrial Relations Code, with the Industrial Disputes Act, 1947 and the Industrial Employment (Standing Orders) Act, 1946; the four labour codes came into force on 21 November 2025. "
  "Statement 3 is wrong: the Code raised the threshold for prior permission from 100 workers under the Industrial Disputes Act to 300, letting more establishments adjust their workforce without approval -- one of its most debated changes.",
  "कथन 1 और 2 सही हैं। श्रमिक आंदोलन के बढ़ने और 1920 में अखिल भारतीय ट्रेड यूनियन कांग्रेस की स्थापना के बाद मार्च 1926 में पारित ट्रेड यूनियन अधिनियम ने यूनियनों को पंजीकरण की सुविधा दी और पंजीकृत यूनियनों को व्यापार-विवाद को आगे बढ़ाने में किए गए कार्यों के लिए आपराधिक षड्यंत्र के अभियोजन और सिविल वादों से संरक्षण दिया। यह औद्योगिक संबंध संहिता में मिलाए गए तीन क़ानूनों में था, साथ में औद्योगिक विवाद अधिनियम, 1947 और औद्योगिक नियोजन (स्थायी आदेश) अधिनियम, 1946; चारों श्रम संहिताएँ 21 नवंबर 2025 को लागू हुईं। "
  "कथन 3 ग़लत है: संहिता ने पूर्व अनुमति की सीमा औद्योगिक विवाद अधिनियम के 100 कर्मकारों से बढ़ाकर 300 कर दी, जिससे अधिक प्रतिष्ठान बिना अनुमोदन अपने कार्यबल में बदलाव कर सकते हैं -- यह इसके सबसे विवादित बदलावों में है।",
  "Trade Unions Act, 1926, sections 13, 17 and 18; Industrial Relations Code, 2020, sections 77 and 104; Ministry of Labour and Employment, notification bringing the labour codes into force (21 November 2025).",
  "ca-t1-eco-trade-unions-act-centenary-ir-code", craft="linkage")

S(EX, "medium", "In February 2026 India and the United States announced a framework for an interim trade agreement. Consider the following statements:",
  "फ़रवरी 2026 में भारत और संयुक्त राज्य अमेरिका ने एक अंतरिम व्यापार समझौते के ढाँचे की घोषणा की। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The United States lowered the tariff on most Indian goods to 18 per cent.",
   "India agreed to remove its import duties on wheat, rice and dairy products.",
   "The framework is the final, comprehensive bilateral trade agreement between the two countries."],
  ["संयुक्त राज्य अमेरिका ने अधिकांश भारतीय वस्तुओं पर टैरिफ़ घटाकर 18 प्रतिशत किया।",
   "भारत ने गेहूँ, चावल और दुग्ध उत्पादों पर अपने आयात शुल्क हटाने पर सहमति दी।",
   "यह ढाँचा दोनों देशों के बीच अंतिम, व्यापक द्विपक्षीय व्यापार समझौता है।"],
  C3, 0,
  "Only statement 1 is correct. Under the framework announced in early February 2026, the United States cut the tariff on most Indian goods -- textiles, leather and footwear, chemicals and others -- to 18 per cent and removed the extra 25 per cent duty it had imposed over India's purchases of Russian oil; India agreed to cut duties on US industrial goods and on some farm items such as tree nuts, fruit and animal feed. "
  "Statement 2 is wrong: India kept protection for sensitive farm products, among them wheat, rice, maize, soya, poultry and dairy, which matter to the livelihoods of small farmers. Statement 3 is wrong: it is a framework for an interim deal, with the broader bilateral trade agreement still to be negotiated.",
  "केवल कथन 1 सही है। फ़रवरी 2026 के आरंभ में घोषित ढाँचे के अंतर्गत संयुक्त राज्य अमेरिका ने अधिकांश भारतीय वस्तुओं -- वस्त्र, चमड़ा और जूते, रसायन आदि -- पर टैरिफ़ घटाकर 18 प्रतिशत किया और भारत की रूसी तेल ख़रीद के कारण लगाया गया अतिरिक्त 25 प्रतिशत शुल्क हटाया; भारत ने अमेरिकी औद्योगिक वस्तुओं और मेवे, फल और पशु-आहार जैसी कुछ कृषि वस्तुओं पर शुल्क घटाने पर सहमति दी। "
  "कथन 2 ग़लत है: भारत ने संवेदनशील कृषि उत्पादों, जिनमें गेहूँ, चावल, मक्का, सोया, मुर्गी-पालन और दुग्ध हैं, के लिए संरक्षण बनाए रखा, जो छोटे किसानों की आजीविका से जुड़े हैं। कथन 3 ग़लत है: यह एक अंतरिम समझौते का ढाँचा है, और व्यापक द्विपक्षीय व्यापार समझौते पर वार्ता अभी बाक़ी है।",
  "India–United States joint statement on the framework for an interim trade agreement (February 2026); Ministry of Commerce and Industry statements.",
  "ca-t1-eco-india-us-interim-framework-18-percent", craft="precision")

S(IG, "medium", "The Economic Survey 2025-26 projected a sharp rise in gig and platform work. In this context, consider the following statements:",
  "आर्थिक समीक्षा 2025-26 ने गिग और प्लेटफ़ॉर्म कार्य में तेज़ वृद्धि का अनुमान लगाया। इस संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Under the Code on Social Security, 2020, aggregators can be required to contribute 1 to 2 per cent of their annual turnover, capped at 5 per cent of what they pay gig and platform workers, towards those workers' social security.",
   "The Survey projected the share of gig workers in India's workforce to rise to about 6.7 per cent by 2029-30."],
  ["सामाजिक सुरक्षा संहिता, 2020 के अंतर्गत एग्रीगेटरों से उनके वार्षिक कारोबार का 1 से 2 प्रतिशत, गिग और प्लेटफ़ॉर्म कर्मकारों को किए गए भुगतान के 5 प्रतिशत की सीमा तक, उन कर्मकारों की सामाजिक सुरक्षा के लिए अंशदान माँगा जा सकता है।",
   "समीक्षा ने अनुमान लगाया कि भारत के कार्यबल में गिग कर्मकारों का हिस्सा 2029-30 तक बढ़कर लगभग 6.7 प्रतिशत हो जाएगा।"],
  T2, 2,
  "Both statements are correct. The Code on Social Security, in force with the other labour codes from November 2025, is the first central law to define gig workers and platform workers, and section 114 lets the government notify schemes for them funded partly by aggregators -- 1 to 2 per cent of annual turnover, but not more than 5 per cent of the amount paid or payable to such workers. "
  "The Survey put gig workers at about 2 per cent of the workforce now and projected about 6.7 per cent by 2029-30, while noting that around 40 per cent of them earn less than ₹15,000 a month -- the reason it called for social security to keep pace with the growth of platform work.",
  "दोनों कथन सही हैं। नवंबर 2025 से अन्य श्रम संहिताओं के साथ लागू सामाजिक सुरक्षा संहिता गिग कर्मकारों और प्लेटफ़ॉर्म कर्मकारों को परिभाषित करने वाला पहला केंद्रीय क़ानून है, और उसकी धारा 114 सरकार को उनके लिए ऐसी योजनाएँ अधिसूचित करने देती है जिनका धन आंशिक रूप से एग्रीगेटर दें -- वार्षिक कारोबार का 1 से 2 प्रतिशत, पर ऐसे कर्मकारों को दी गई या देय राशि के 5 प्रतिशत से अधिक नहीं। "
  "समीक्षा ने गिग कर्मकारों को अभी कार्यबल का लगभग 2 प्रतिशत आँका और 2029-30 तक लगभग 6.7 प्रतिशत का अनुमान लगाया, यह भी बताते हुए कि उनमें से लगभग 40 प्रतिशत ₹15,000 प्रति माह से कम कमाते हैं -- इसीलिए उसने कहा कि सामाजिक सुरक्षा को प्लेटफ़ॉर्म कार्य की वृद्धि के साथ चलना चाहिए।",
  "Code on Social Security, 2020, sections 2(35), 2(61) and 114; Ministry of Finance, Economic Survey 2025-26, chapter on employment.",
  "ca-t1-eco-gig-aggregator-levy-survey", craft="linkage")

S(AG, "medium", "During the LPG shortage of March 2026 the government invoked the Essential Commodities Act. Consider the following statements about the Act:",
  "मार्च 2026 की एलपीजी कमी के दौरान सरकार ने आवश्यक वस्तु अधिनियम का प्रयोग किया। इस अधिनियम के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Essential Commodities Act, 1955 lets the Central Government control the production, supply and distribution of commodities it declares essential.",
   "The amendment made to the Act in 2020 was repealed in 2021 along with the other farm laws.",
   "Petroleum and its products cannot be declared essential commodities under the Act."],
  ["आवश्यक वस्तु अधिनियम, 1955 केंद्र सरकार को उन वस्तुओं के उत्पादन, आपूर्ति और वितरण को नियंत्रित करने देता है जिन्हें वह आवश्यक घोषित करे।",
   "2020 में अधिनियम में किया गया संशोधन 2021 में अन्य कृषि क़ानूनों के साथ निरस्त कर दिया गया।",
   "अधिनियम के अंतर्गत पेट्रोलियम और उसके उत्पादों को आवश्यक वस्तु घोषित नहीं किया जा सकता।"],
  C3, 1,
  "Statements 1 and 2 are correct. Section 3 of the 1955 Act lets the Centre regulate production, supply, distribution, prices and stocks of essential commodities, and the States act through delegated orders; it is the legal basis for stock limits and supply orders in shortages. The Essential Commodities (Amendment) Act, 2020, which allowed stock limits on farm produce only in extraordinary price rises, was one of the three farm laws, and the Farm Laws Repeal Act, 2021 repealed it. "
  "Statement 3 is wrong: the Schedule to the Act lists petroleum and petroleum products, so the government could issue orders to prioritise LPG for households and regulate its distribution when supplies through the Strait of Hormuz were disrupted.",
  "कथन 1 और 2 सही हैं। 1955 के अधिनियम की धारा 3 केंद्र को आवश्यक वस्तुओं के उत्पादन, आपूर्ति, वितरण, क़ीमत और भंडार को विनियमित करने देती है, और राज्य प्रत्यायोजित आदेशों से कार्य करते हैं; कमी के समय भंडार-सीमा और आपूर्ति आदेशों का यही विधिक आधार है। आवश्यक वस्तु (संशोधन) अधिनियम, 2020, जो कृषि उपज पर भंडार-सीमा केवल असाधारण मूल्य-वृद्धि में अनुमत करता था, तीन कृषि क़ानूनों में से एक था, और कृषि क़ानून निरसन अधिनियम, 2021 ने उसे निरस्त कर दिया। "
  "कथन 3 ग़लत है: अधिनियम की अनुसूची में पेट्रोलियम और पेट्रोलियम उत्पाद सूचीबद्ध हैं, इसलिए होर्मुज़ जलडमरूमध्य से आपूर्ति बाधित होने पर सरकार परिवारों के लिए एलपीजी को प्राथमिकता देने और उसके वितरण को विनियमित करने के आदेश जारी कर सकी।",
  "Essential Commodities Act, 1955, section 3 and Schedule; Farm Laws Repeal Act, 2021; Ministry of Petroleum and Natural Gas, orders on LPG supply (March 2026).",
  "ca-t1-eco-essential-commodities-act-lpg", craft="linkage")

S(IN, "medium", "In February 2026 the Supreme Court heard appeals in the Competition Commission of India's case against Meta and WhatsApp. Consider the following statements:",
  "फ़रवरी 2026 में सर्वोच्च न्यायालय ने मेटा और व्हाट्सऐप के विरुद्ध भारतीय प्रतिस्पर्धा आयोग के मामले में अपीलें सुनीं। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Competition Commission of India is a constitutional body.",
   "Appeals against the Commission's orders lie directly with the Supreme Court.",
   "The Commission can impose penalties only with reference to a company's turnover in India."],
  ["भारतीय प्रतिस्पर्धा आयोग एक संवैधानिक निकाय है।",
   "आयोग के आदेशों के विरुद्ध अपीलें सीधे सर्वोच्च न्यायालय में होती हैं।",
   "आयोग किसी कंपनी के भारत में कारोबार के संदर्भ में ही दंड लगा सकता है।"],
  C3, 3,
  "None of the statements is correct. The Competition Commission is a statutory body set up under the Competition Act, 2002 to check anti-competitive agreements, abuse of dominance and harmful mergers. Since 2017 appeals against its orders go to the National Company Law Appellate Tribunal, and only from there to the Supreme Court -- the route the WhatsApp privacy-policy case took after the Commission's penalty of 2024 and the Tribunal's ruling of 2025. "
  "The Competition (Amendment) Act, 2023 allows penalties to be calculated on a firm's global turnover, so that large digital companies earning abroad cannot escape with small fines on their Indian revenue alone.",
  "कोई भी कथन सही नहीं है। प्रतिस्पर्धा आयोग प्रतिस्पर्धा अधिनियम, 2002 के अंतर्गत बना एक सांविधिक निकाय है, जो प्रतिस्पर्धा-विरोधी करारों, प्रभुत्व के दुरुपयोग और हानिकारक विलयों पर रोक लगाता है। 2017 से उसके आदेशों के विरुद्ध अपीलें राष्ट्रीय कंपनी विधि अपीलीय अधिकरण में जाती हैं, और वहीं से सर्वोच्च न्यायालय -- व्हाट्सऐप निजता-नीति मामला 2024 के आयोग के दंड और 2025 के अधिकरण के निर्णय के बाद इसी मार्ग से आया। "
  "प्रतिस्पर्धा (संशोधन) अधिनियम, 2023 दंड की गणना किसी फ़र्म के वैश्विक कारोबार पर करने की अनुमति देता है, ताकि विदेश में कमाने वाली बड़ी डिजिटल कंपनियाँ केवल भारतीय राजस्व पर छोटे जुर्मानों से न छूट जाएँ।",
  "Competition Act, 2002, sections 7, 27 and 53A, as amended by the Finance Act, 2017 and the Competition (Amendment) Act, 2023.",
  "ca-t1-eco-cci-statutory-nclat-global-turnover", craft="precision")

S(IN, "medium", "In March 2026 Bihar made transit passes compulsory for moving minor minerals such as sand. Consider the following statements:",
  "मार्च 2026 में बिहार ने बालू जैसे गौण खनिजों के परिवहन के लिए पारगमन पास अनिवार्य किए। निम्नलिखित कथनों पर विचार कीजिए:",
  ["Under the Mines and Minerals (Development and Regulation) Act, 1957, the State Governments make the rules for granting concessions for minor minerals.",
   "The Central Government has the power to declare any mineral to be a minor mineral.",
   "The royalty on minor minerals is collected by the Central Government."],
  ["खान और खनिज (विकास और विनियमन) अधिनियम, 1957 के अंतर्गत गौण खनिजों के लिए रियायतें देने के नियम राज्य सरकारें बनाती हैं।",
   "केंद्र सरकार को किसी भी खनिज को गौण खनिज घोषित करने की शक्ति है।",
   "गौण खनिजों पर रॉयल्टी केंद्र सरकार वसूलती है।"],
  C3, 1,
  "Statements 1 and 2 are correct. Section 3(e) of the MMDR Act defines minor minerals as building stones, gravel, ordinary clay, ordinary sand (other than sand used for prescribed purposes) and any other mineral the Central Government notifies as minor; section 15 hands the regulation of minor minerals entirely to the States, which frame their own concession rules and enforce transit passes against illegal mining. "
  "Statement 3 is wrong: the royalty, and the rates, on minor minerals are fixed and collected by the States -- an important source of their own non-tax revenue -- whereas the royalty rates for major minerals are set by the Centre in the Second Schedule, though collected by the States too.",
  "कथन 1 और 2 सही हैं। एमएमडीआर अधिनियम की धारा 3(ङ) गौण खनिजों को इमारती पत्थर, बजरी, साधारण मिट्टी, साधारण बालू (निर्धारित प्रयोजनों वाली बालू को छोड़कर) और ऐसा कोई अन्य खनिज बताती है जिसे केंद्र सरकार गौण अधिसूचित करे; धारा 15 गौण खनिजों का विनियमन पूरी तरह राज्यों को सौंपती है, जो अपने रियायत नियम बनाते हैं और अवैध खनन के विरुद्ध पारगमन पास लागू करते हैं। "
  "कथन 3 ग़लत है: गौण खनिजों पर रॉयल्टी, और उसकी दरें, राज्य तय करते और वसूलते हैं -- यह उनके अपने ग़ैर-कर राजस्व का महत्त्वपूर्ण स्रोत है -- जबकि प्रमुख खनिजों की रॉयल्टी दरें केंद्र दूसरी अनुसूची में तय करता है, यद्यपि वसूलते उन्हें भी राज्य ही हैं।",
  "Mines and Minerals (Development and Regulation) Act, 1957, sections 3(e), 9 and 15.",
  "ca-t1-eco-minor-minerals-state-rules-royalty", craft="precision")

for r in d.ROWS:
    r["question_data"]["ca_window"] = "2026-Q1"
write("ca_t1_b.sql")
