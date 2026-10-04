# -*- coding: utf-8 -*-
"""Level 2 · Test 17 (Economy 3: Budget, Deficits, Public Debt, Taxation and Fiscal Federalism) -- depth audit of
2026-10-04 (docs/upsc-question-design-standard.md §6).

All 102 rows were read and classified. Before: analytic 28, precision 43, recall 31 (2 rows are Test 21's,
already tagged). 9 recall rows are rewritten in place with the same concept id, type and difficulty:
  - cases: a government's fiscal and primary deficits from its accounts, a ministry asked to justify every item afresh, one
    scheme's cost shared differently in Assam, Bihar and Ladakh, and a salary of 12.5 lakh under the new
    regime;
  - mechanisms: what 24 paise of borrowing in the Budget rupee reflects, why the Centre's mostly domestic
    debt is safer, why cities lean on State transfers, what 'income distance' does to the tax shares, and
    what faceless assessment is for.
After: analytic 37, precision 43, recall 22. The other 91 rows keep their content and get their craft tag.
Leaks avoided while drafting (two candidates were left as they were):
  - 'no asset, so revenue expenditure' (answers the scholarships row), and subsidies as the largest item
    (the interest AR's Statement II), so the spending-composition row was left;
  - interest-free 50-year loans counted as capital expenditure (states the capex row's statement 3), so
    the SASCI row was left;
  - drawing down cash balances to cover a deficit (states the financing row's statement 3);
  - the 4.4 per cent deficit target for 2025-26 (answers the fiscal-path row's statement 1)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write_updates, CODE
from polity_common import C3, C4, T2

d.SUBJECT = "Economy"
d.REQUIRE_CRAFT = True
FB = "Budget, Deficits & Public Debt"
FT = "Taxation & Fiscal Federalism"
NCM = "NCERT Class XII, Introductory Macroeconomics"
MOF = "Ministry of Finance -- Union Budget documents."

# ================================================================ MCQs (3)
M(FB, "medium", "In the Union Budget 2025-26, 'borrowings and other liabilities' supplied about 24 paise of every rupee that the Centre expected to receive. This share mainly reflects:",
  "केंद्रीय बजट 2025-26 में 'उधार और अन्य देयताएँ' केंद्र की अपेक्षित प्राप्तियों के हर रुपये में से लगभग 24 पैसे देती थीं। यह हिस्सा मुख्यतः क्या दर्शाता है?",
  ["how large the fiscal deficit is relative to the Centre's total outgo",
   "the share of the Centre's total spending that goes on interest payments alone",
   "the share of the Centre's gross tax revenue that is passed on to the States",
   "the share of the country's GDP that the Centre spends on capital projects"],
  ["केंद्र के कुल व्यय की तुलना में राजकोषीय घाटा कितना बड़ा है",
   "केंद्र के कुल व्यय का वह हिस्सा जो केवल ब्याज भुगतान पर जाता है",
   "केंद्र के सकल कर राजस्व का वह हिस्सा जो राज्यों को दिया जाता है",
   "देश के GDP का वह हिस्सा जिसे केंद्र पूँजीगत परियोजनाओं पर खर्च करता है"],
  0,
  "Every rupee the Centre pays out has to come from somewhere; whatever taxes and other non-debt receipts do not cover is borrowed, and that gap is the fiscal deficit. So the 'borrowings and other liabilities' slice of the Budget rupee is the deficit seen as a share of the whole outgo -- the larger the slice, the more of the Centre's spending rests on debt. "
  "The 'rupee' in these charts counts gross receipts, including the States' share of taxes, which appears on the other side as money going to the States; interest and capital spending are items of where the rupee goes, not of where it comes from.",
  "केंद्र जो हर रुपया खर्च करता है, उसे कहीं से आना होता है; जो भाग कर और अन्य ग़ैर-ऋण प्राप्तियाँ नहीं ढक पातीं, वह उधार लिया जाता है, और यही अंतर राजकोषीय घाटा है। इसलिए बजट रुपये का 'उधार और अन्य देयताएँ' वाला भाग पूरे व्यय के हिस्से के रूप में घाटा है; यह भाग जितना बड़ा, केंद्र का उतना अधिक व्यय ऋण पर टिका है। "
  "इन चार्टों में 'रुपया' सकल प्राप्तियाँ गिनता है, जिनमें करों में राज्यों का हिस्सा भी है, जो दूसरी ओर राज्यों को जाने वाले धन के रूप में दिखता है; ब्याज और पूँजीगत व्यय इस बात के मद हैं कि रुपया कहाँ जाता है, इस बात के नहीं कि कहाँ से आता है।",
  MOF, "fb-rupee-comes-from", craft="inference")

M(FT, "hard", "The Fifteenth Finance Commission gave 'income distance' -- each State's distance from the State with the highest per capita income -- the largest weight, 45 per cent, in sharing Central taxes among the States. The effect of this criterion is that:",
  "पंद्रहवें वित्त आयोग ने राज्यों में केंद्रीय करों के बँटवारे में 'आय दूरी', यानी सबसे अधिक प्रति व्यक्ति आय वाले राज्य से प्रत्येक राज्य की दूरी, को सबसे अधिक, 45 प्रतिशत, भार दिया। इस मानदंड का प्रभाव यह है कि:",
  ["poorer States receive a larger share than their population alone would give them",
   "States that raise more taxes of their own receive a correspondingly larger share",
   "every State receives exactly the same amount per head of its population in 2011",
   "States with more dense forest cover receive a larger share, as a reward for conservation"],
  ["ग़रीब राज्यों को केवल उनकी जनसंख्या से मिलने वाले हिस्से से अधिक हिस्सा मिलता है",
   "जो राज्य अपने अधिक कर जुटाते हैं, उन्हें उसी अनुपात में अधिक हिस्सा मिलता है",
   "हर राज्य को उसकी 2011 की जनसंख्या के प्रति व्यक्ति बिल्कुल बराबर राशि मिलती है",
   "अधिक सघन वन आवरण वाले राज्यों को संरक्षण के पुरस्कार के रूप में अधिक हिस्सा मिलता है"],
  0,
  "Income distance is an equalising criterion: the further a State's per capita income is below the highest, the larger its weight, so States such as Bihar and Uttar Pradesh, with low incomes and large populations, get the biggest shares, helping them provide services close to the national level. "
  "The Commission's other weights were population (2011) 15 per cent, area 15, forest and ecology 10, demographic performance 12.5, and tax and fiscal effort only 2.5 -- so own tax effort and forests count, but far less than income distance.",
  "आय दूरी एक समकारी मानदंड है: किसी राज्य की प्रति व्यक्ति आय सबसे ऊँची से जितनी नीचे, उसका भार उतना अधिक, इसलिए कम आय और बड़ी जनसंख्या वाले बिहार और उत्तर प्रदेश जैसे राज्यों को सबसे बड़े हिस्से मिलते हैं, जिससे वे राष्ट्रीय स्तर के निकट सेवाएँ दे सकें। "
  "आयोग के अन्य भार थे जनसंख्या (2011) 15 प्रतिशत, क्षेत्रफल 15, वन और पारिस्थितिकी 10, जनसांख्यिकीय प्रदर्शन 12.5, और कर तथा राजकोषीय प्रयास केवल 2.5; इसलिए अपने कर प्रयास और वन गिने जाते हैं, पर आय दूरी से बहुत कम।",
  "Report of the Fifteenth Finance Commission (2021-26).", "ft-15th-fc-criteria", craft="linkage")

M(FT, "medium", "In 2020 India introduced 'faceless assessment' of income tax, under which cases are allotted by computer to officers anywhere in the country and all communication is online. Its main purpose is to:",
  "2020 में भारत ने आयकर का 'फ़ेसलेस मूल्यांकन' शुरू किया, जिसके तहत मामले कंप्यूटर द्वारा देश में कहीं के भी अधिकारियों को सौंपे जाते हैं और सारा संवाद ऑनलाइन होता है। इसका मुख्य उद्देश्य है:",
  ["reduce the discretion and scope for harassment and corruption that come with personal contact",
   "let each taxpayer choose for himself the particular tax officer who will assess his return",
   "exempt all small taxpayers below a set income from having to file any income tax return at all",
   "allow the tax department to raise tax demands without ever informing the taxpayer concerned"],
  ["व्यक्तिगत संपर्क से आने वाले विवेकाधिकार और उत्पीड़न तथा भ्रष्टाचार की गुंजाइश को घटाना",
   "हर करदाता को अपना रिटर्न आँकने वाले अधिकारी को स्वयं चुनने देना",
   "एक तय आय से नीचे के सभी छोटे करदाताओं को कोई भी आयकर रिटर्न भरने से छूट देना",
   "कर विभाग को संबंधित करदाता को बताए बिना कर माँग उठाने देना"],
  0,
  "When the same local officer meets a taxpayer face to face, there is room for discretion, delay and rent-seeking. The faceless scheme breaks that link: a computer picks the officer, the taxpayer does not know who it is, the draft order is reviewed by another team, and notices, replies and hearings, by video, all go through the portal. "
  "Taxpayers still file returns and are informed of every demand; they simply do not choose or meet the assessing officer.",
  "जब वही स्थानीय अधिकारी करदाता से आमने-सामने मिलता है, तो विवेकाधिकार, देरी और अनुचित लाभ की गुंजाइश रहती है। फ़ेसलेस योजना यह संबंध तोड़ती है: कंप्यूटर अधिकारी चुनता है, करदाता नहीं जानता कि वह कौन है, मसौदा आदेश की समीक्षा दूसरी टीम करती है, और नोटिस, उत्तर और वीडियो से सुनवाई, सब पोर्टल से होते हैं। "
  "करदाता अब भी रिटर्न भरते हैं और हर माँग की सूचना पाते हैं; वे बस मूल्यांकन अधिकारी को न चुनते हैं न उससे मिलते हैं।",
  "Central Board of Direct Taxes -- Faceless Assessment Scheme.", "ft-faceless-assessment", craft="linkage")

# ================================================================ two-statement rows (2)
S(FB, "easy", "A government expects to spend 120 crore rupees in a year and to receive 100 crore rupees from taxes and other non-debt sources. Consider the following statements:",
  "एक सरकार वर्ष में 120 करोड़ रुपये खर्च करने और करों तथा अन्य ग़ैर-ऋण स्रोतों से 100 करोड़ रुपये प्राप्त करने की अपेक्षा रखती है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["It has a deficit of 20 crore rupees.",
   "If 15 crore rupees of its spending is interest on past debt, its primary deficit is 5 crore rupees."],
  ["उसका घाटा 20 करोड़ रुपये है।",
   "यदि उसके व्यय में 15 करोड़ रुपये पिछले ऋण पर ब्याज है, तो उसका प्राथमिक घाटा 5 करोड़ रुपये है।"],
  T2, 2,
  "Both statements are correct. The fiscal deficit is total expenditure minus total receipts other than borrowing: 120 - 100 = 20 crore rupees. The primary deficit takes interest on past debt out of the fiscal deficit: 20 - 15 = 5 crore rupees. It shows how much of this year's borrowing is due to this year's own spending decisions, rather than to the cost of servicing old debt.",
  "दोनों कथन सही हैं। राजकोषीय घाटा कुल व्यय में से उधार के अलावा कुल प्राप्तियाँ घटाने पर आता है: 120 - 100 = 20 करोड़ रुपये। प्राथमिक घाटा राजकोषीय घाटे में से पिछले ऋण पर ब्याज निकाल देता है: 20 - 15 = 5 करोड़ रुपये। यह दिखाता है कि इस वर्ष के उधार का कितना भाग इस वर्ष के अपने व्यय निर्णयों के कारण है, न कि पुराने ऋण की सेवा की लागत के कारण।",
  NCM, "fb-deficit-borrowing-easy", craft="application")

S(FT, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Property tax on houses in cities is collected by the State Government.",
   "Because property tax is often levied on outdated values and poorly collected, many Indian cities depend heavily on transfers from their State Governments."],
  ["शहरों में मकानों पर संपत्ति कर राज्य सरकार वसूलती है।",
   "चूँकि संपत्ति कर प्रायः पुराने मूल्यांकनों पर लगता है और ठीक से वसूला नहीं जाता, इसलिए कई भारतीय शहर अपनी राज्य सरकारों के अंतरणों पर बहुत निर्भर हैं।"],
  T2, 1,
  "Only statement 2 is correct. Property tax is levied and collected by municipal bodies and is their main source of their own revenue, but in India it brings in only a small fraction of a per cent of GDP, far less than in many other countries, because valuations are rarely revised and coverage is patchy. "
  "So cities rely on grants and shared taxes from their States, and the Fifteenth Finance Commission made part of its grants to urban local bodies depend on States notifying floor rates for property tax. Statement 1 is wrong for that reason: it is a municipal, not a State, tax.",
  "केवल कथन 2 सही है। संपत्ति कर नगर निकाय लगाते और वसूलते हैं और यह उनकी अपनी आय का मुख्य स्रोत है, पर भारत में यह GDP का एक प्रतिशत का बहुत छोटा अंश ही लाता है, कई अन्य देशों से बहुत कम, क्योंकि मूल्यांकन शायद ही संशोधित होते हैं और दायरा अधूरा है। "
  "इसलिए शहर अपने राज्यों के अनुदानों और साझा करों पर निर्भर रहते हैं, और पंद्रहवें वित्त आयोग ने नगरीय निकायों को अपने अनुदानों का एक भाग राज्यों द्वारा संपत्ति कर की न्यूनतम दरें अधिसूचित करने पर निर्भर किया। इसी कारण कथन 1 गलत है: यह नगर निकाय का कर है, राज्य का नहीं।",
  "Report of the Fifteenth Finance Commission (2021-26).", "ft-property-tax-gst-easy", craft="linkage")

# ================================================================ three-statement rows (4)
S(FB, "medium", "Consider the following statements about the debt of the Central Government:",
  "केंद्र सरकार के ऋण के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Most of it is owed to domestic lenders, which largely shields the Centre from shocks to the exchange rate.",
   "Dated government securities form the largest part of its internal debt.",
   "Commercial banks hold large amounts of Central Government securities, partly because they must keep a set share of their deposits in such securities."],
  ["इसका अधिकांश भाग घरेलू ऋणदाताओं का है, जो केंद्र को विनिमय दर के झटकों से काफ़ी हद तक बचाता है।",
   "दिनांकित सरकारी प्रतिभूतियाँ इसके आंतरिक ऋण का सबसे बड़ा भाग हैं।",
   "वाणिज्यिक बैंक केंद्र सरकार की प्रतिभूतियों की बड़ी मात्रा रखते हैं, आंशिक रूप से इसलिए कि उन्हें अपनी जमाओं का एक तय हिस्सा ऐसी प्रतिभूतियों में रखना होता है।"],
  C3, 2,
  "All three are correct. External debt is only about 5 per cent of the Centre's liabilities, and most of it is long-term and concessional, so a fall in the rupee does little to the Centre's debt burden -- unlike countries that borrow heavily in foreign currency. "
  "Dated securities, sold through RBI auctions, make up the bulk of internal debt. Banks must hold a share of their deposits in approved securities under the Statutory Liquidity Ratio, which gives the Centre a large, steady set of buyers, along with insurers, provident funds and the RBI.",
  "तीनों कथन सही हैं। विदेशी ऋण केंद्र की देयताओं का केवल लगभग 5 प्रतिशत है, और उसका अधिकांश दीर्घकालिक और रियायती है, इसलिए रुपये के गिरने से केंद्र के ऋण भार पर बहुत कम असर पड़ता है, उन देशों के विपरीत जो विदेशी मुद्रा में भारी उधार लेते हैं। "
  "RBI नीलामियों से बेची गई दिनांकित प्रतिभूतियाँ आंतरिक ऋण का बड़ा भाग हैं। सांविधिक तरलता अनुपात के तहत बैंकों को अपनी जमाओं का एक हिस्सा अनुमोदित प्रतिभूतियों में रखना होता है, जिससे बीमाकर्ताओं, भविष्य निधियों और RBI के साथ केंद्र को ख़रीदारों का बड़ा, स्थिर समूह मिलता है।",
  "Ministry of Finance -- Status Paper on Government Debt.", "fb-central-debt-composition", craft="linkage")

S(FB, "medium", "A ministry is asked to justify every item of next year's spending from scratch, instead of adding a percentage to this year's allocation. Consider the following statements:",
  "एक मंत्रालय से कहा जाता है कि वह इस वर्ष के आवंटन में प्रतिशत जोड़ने के बजाय अगले वर्ष के व्यय की हर मद को नए सिरे से उचित ठहराए। निम्नलिखित कथनों पर विचार कीजिए:",
  ["This is zero-based budgeting.",
   "This approach makes it easier to cut schemes that have outlived their purpose.",
   "The Outcome Budget, too, sets each allocation on the basis of the previous year's spending."],
  ["यह शून्य-आधारित बजटन है।",
   "यह तरीक़ा उन योजनाओं में कटौती आसान बनाता है जिनका उद्देश्य पूरा हो चुका है।",
   "परिणाम बजट भी हर आवंटन पिछले वर्ष के व्यय के आधार पर तय करता है।"],
  C3, 1,
  "Statements 1 and 2 are correct. Under incremental budgeting, last year's figure is taken as given and only the increase is debated, so old schemes roll on; zero-based budgeting starts each head from nothing, so every scheme has to prove its worth again and weak ones can be dropped, at the cost of much more work each year. "
  "Statement 3 is wrong: the Outcome Budget, introduced in 2005 and now an Output-Outcome Monitoring Framework, ties allocations to measurable outputs and outcomes, not to last year's spending.",
  "कथन 1 और 2 सही हैं। वृद्धिशील बजटन में पिछले वर्ष का आँकड़ा दिया हुआ मान लिया जाता है और केवल वृद्धि पर बहस होती है, इसलिए पुरानी योजनाएँ चलती रहती हैं; शून्य-आधारित बजटन हर मद को शून्य से शुरू करता है, इसलिए हर योजना को अपनी उपयोगिता फिर साबित करनी पड़ती है और कमज़ोर योजनाएँ हटाई जा सकती हैं, यद्यपि हर वर्ष काम बहुत बढ़ जाता है। "
  "कथन 3 गलत है: 2005 में शुरू हुआ और अब आउटपुट-आउटकम निगरानी ढाँचा बना परिणाम बजट आवंटनों को मापने योग्य आउटपुट और परिणामों से जोड़ता है, पिछले वर्ष के व्यय से नहीं।",
  MOF, "fb-budgeting-practices", craft="application")

S(FT, "medium", "A centrally sponsored 'core' scheme is to spend 100 crore rupees each in Assam, in Bihar and in the Union Territory of Ladakh, which has no legislature. Consider the following statements:",
  "एक केंद्र प्रायोजित 'मूल' योजना को असम, बिहार और विधानमंडल-रहित केंद्रशासित प्रदेश लद्दाख, प्रत्येक में 100 करोड़ रुपये खर्च करने हैं। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Centre's share in Assam is 90 crore rupees.",
   "The Centre's share in Bihar is 60 crore rupees.",
   "The Centre bears the full 100 crore rupees in Ladakh."],
  ["असम में केंद्र का हिस्सा 90 करोड़ रुपये है।",
   "बिहार में केंद्र का हिस्सा 60 करोड़ रुपये है।",
   "लद्दाख में केंद्र पूरे 100 करोड़ रुपये वहन करता है।"],
  C3, 2,
  "All three are correct. For most core centrally sponsored schemes the Centre and a State share the cost 60:40, but the North-Eastern and Himalayan States, Assam among them, pay only 10 per cent, and Union Territories without a legislature, such as Ladakh, are funded fully by the Centre. "
  "Because a State must put up its matching share to draw the Centre's money, these schemes shape how States spend their own budgets -- a frequent point of friction in fiscal federalism.",
  "तीनों कथन सही हैं। अधिकांश मूल केंद्र प्रायोजित योजनाओं में केंद्र और राज्य लागत 60:40 में बाँटते हैं, पर असम सहित उत्तर-पूर्वी और हिमालयी राज्य केवल 10 प्रतिशत देते हैं, और लद्दाख जैसे विधानमंडल-रहित केंद्रशासित प्रदेशों का पूरा वित्तपोषण केंद्र करता है। "
  "चूँकि केंद्र का धन पाने के लिए राज्य को अपना मिलान हिस्सा देना पड़ता है, ये योजनाएँ तय करती हैं कि राज्य अपने बजट कैसे खर्च करें, जो राजकोषीय संघवाद में टकराव का बार-बार आने वाला बिंदु है।",
  "Ministry of Finance -- Department of Expenditure, Rationalisation of Centrally Sponsored Schemes.", "ft-css-funding-pattern", craft="application")

S(FT, "medium", "A resident salaried employee has a salary of ₹12.5 lakh in 2025-26, no other income, and stays in the new tax regime. Consider the following statements:",
  "एक निवासी वेतनभोगी कर्मचारी का 2025-26 में वेतन ₹12.5 लाख है, कोई अन्य आय नहीं है, और वह नई कर व्यवस्था में रहती है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["Her taxable income is the full ₹12.5 lakh, because no standard deduction is allowed under the new regime.",
   "She pays no income tax, because of the rebate.",
   "Had her salary been ₹13 lakh, she would still have paid no income tax."],
  ["उसकी कर-योग्य आय पूरे ₹12.5 लाख है, क्योंकि नई व्यवस्था में कोई मानक कटौती नहीं मिलती।",
   "छूट (रिबेट) के कारण वह कोई आयकर नहीं देती।",
   "यदि उसका वेतन ₹13 लाख होता, तो भी वह कोई आयकर नहीं देती।"],
  C3, 0,
  "Only statement 2 is correct. Salaried taxpayers in the new regime get a standard deduction of ₹75,000, so her taxable income is ₹11.75 lakh; the rebate makes the tax nil on taxable income up to ₹12 lakh, that is, on a salary of up to ₹12.75 lakh. "
  "Statement 1 is wrong for that reason. Statement 3 is wrong: on a salary of ₹13 lakh the taxable income, ₹12.25 lakh, crosses ₹12 lakh, so the rebate no longer applies; marginal relief limits the tax to the income above ₹12 lakh -- about ₹25,000 plus cess -- but some tax is due.",
  "केवल कथन 2 सही है। नई व्यवस्था में वेतनभोगी करदाताओं को ₹75,000 की मानक कटौती मिलती है, इसलिए उसकी कर-योग्य आय ₹11.75 लाख है; छूट ₹12 लाख तक की कर-योग्य आय, यानी ₹12.75 लाख तक के वेतन, पर कर शून्य कर देती है। "
  "इसी कारण कथन 1 गलत है। कथन 3 गलत है: ₹13 लाख के वेतन पर कर-योग्य आय, ₹12.25 लाख, ₹12 लाख से ऊपर चली जाती है, इसलिए छूट लागू नहीं होती; सीमांत राहत कर को ₹12 लाख से ऊपर की आय, लगभग ₹25,000 और उपकर, तक सीमित करती है, पर कुछ कर देय है।",
  "Ministry of Finance -- Union Budget 2025-26, Finance Act, 2025.", "ft-new-regime-2025-26", craft="application")

# ================================================================ TAGS for the 91 kept rows (Test 21's 2 are tagged already)
TAGS = {
 "fb-economic-survey-role-easy": "recall", "fb-roads-capex-easy": "linkage", "fb-monetisation-frbm": "inference",
 "fb-pandemic-deficit": "linkage", "fb-consolidation-not-capex-cut": "precision", "fb-crowding-out": "linkage",
 "fb-interest-committed": "linkage", "fb-interest-rising-largest": "linkage", "fb-revenue-deficit-two-budgets": "precision",
 "fb-receipt-classification-pairs-easy": "application", "fb-fiscal-committees-pairs": "recall", "fb-financial-year-easy": "recall",
 "fb-surplus-easy": "recall", "fb-debt-ratio-numerical": "application", "fb-effective-capex": "precision",
 "fb-disinvestment-fd-not-rd": "inference", "fb-fiscal-consolidation-meaning": "precision", "fb-fiscal-space": "precision",
 "fb-golden-rule": "precision", "fb-iebr-example": "application", "fb-interest-rd-not-pd": "inference",
 "fb-borrowing-debt-easy": "precision", "fb-budget-basics-easy": "recall", "fb-defence-spending-easy": "recall",
 "fb-deficit-debt-grants-easy": "precision", "fb-revenue-capital-spending-easy": "application", "fb-revenue-receipts-easy": "precision",
 "fb-accrual-cash-gasab": "precision", "fb-capex-composition": "recall", "fb-debt-dynamics-r-g": "inference",
 "fb-deficits-numerical": "application", "fb-fiscal-dominance-drag-twin": "precision", "fb-gfce-national-accounts": "precision",
 "fb-market-borrowing-none": "precision", "fb-ricardian-multipliers": "inference", "fb-adhoc-bills-wma": "precision",
 "fb-automatic-stabilisers": "linkage", "fb-budget-date-division-none": "recall", "fb-budget-terms-none": "precision",
 "fb-capital-receipts-count": "multi", "fb-deficit-measures-concepts": "linkage", "fb-disinvestment-dipam": "recall",
 "fb-economic-survey": "precision", "fb-erd-primary-deficit": "precision", "fb-financing-fiscal-deficit": "recall",
 "fb-fiscal-path-debt-anchor": "precision", "fb-frbm-act": "precision", "fb-general-debt-ratings": "recall",
 "fb-guarantees-contingent": "precision", "fb-nk-singh-frbm-review": "precision", "fb-off-budget-fci-nssf": "linkage",
 "fb-revenue-expenditure-count": "multi", "fb-sasci-loans": "recall", "fb-spending-composition": "recall",
 "ft-sin-tax-easy": "linkage", "ft-e-invoicing": "precision", "ft-agricultural-income-slabs": "precision",
 "ft-customs-protection-centre": "precision", "ft-gst-cascading-itc": "linkage", "ft-new-regime-deductions-efiling": "linkage",
 "ft-tax-authorities-pairs": "recall", "ft-direct-tax-easy": "precision", "ft-gst-launch-easy": "recall",
 "ft-input-tax-credit-numerical": "application", "ft-gst-subsumed-customs": "precision", "ft-revenue-neutral-rate": "precision",
 "ft-securities-transaction-tax": "precision", "ft-specific-ad-valorem": "precision", "ft-customs-excise-easy": "recall",
 "ft-gst-income-tax-sharing-easy": "recall", "ft-progressive-cigarette-easy": "precision", "ft-tax-basics-easy": "recall",
 "ft-gst-registration-inverted-duty": "precision", "ft-international-tax-none": "precision", "ft-tax-administration": "precision",
 "ft-tax-gdp-ratio": "recall", "ft-tax-incidence-elasticity": "inference", "ft-buoyancy-elasticity-none": "precision",
 "ft-capital-gains-2024": "precision", "ft-corporate-tax-2019": "recall", "ft-direct-tax-trends": "recall",
 "ft-equalisation-levy-angel-tax": "recall", "ft-gst-compensation": "precision", "ft-gst-rate-rationalisation-2025": "precision",
 "ft-gst-scope-none": "precision", "ft-incidence-direct-indirect": "precision", "ft-income-tax-act-2025": "precision",
 "ft-oecd-two-pillars": "precision", "ft-state-taxes-count": "multi", "ft-tax-expenditure": "precision",
 "ft-vertical-horizontal-imbalance": "precision"}

if __name__ == "__main__":
    write_updates("upg_l2_t17_econ.sql", statuses=("draft", "published"), tags=TAGS)
