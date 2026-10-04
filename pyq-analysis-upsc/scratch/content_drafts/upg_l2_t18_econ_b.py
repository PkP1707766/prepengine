# -*- coding: utf-8 -*-
"""Level 2 · Test 18 (Economy 4) -- depth audit of 2026-10-05, part B: Industry, Infrastructure, Energy & Services,
plus the Lakhpati Didi row, and the tags for the 69 kept rows (Test 21's 6 are tagged already). Part A is
upg_l2_t18_econ_a.py.

Part B rewrites 15 rows in place with the same concept id, type and difficulty:
  - cases: idle factory capacity, a textile mill buying solar power across States, a US toy maker adding
    an Indian supplier base, a core-index month in which refinery output falls, a PLI incentive worked out
    on incremental sales, and a majority government shareholding;
  - mechanisms: what AT&C losses count and why prepaid meters cut them;
  - precision: the form of viability gap funding, who counts as a Lakhpati Didi, the IIP's sectors against
    its use-based groups, Micron's ATMP unit against a fab, the reserve caverns' days of cover against the
    90-day norm, PM-WANI's licence-free data offices, and the logistics-cost estimate.
One kept row was reworded for accuracy: smartphones have become one of India's largest single export items,
so the electronics row now compares electronics with engineering goods rather than petroleum products.
The oil row also drops the claim about Russia as the largest supplier, which sanctions have made unstable.
Leaks avoided while drafting:
  - steel or cement in the core-index case (the core-industries count row lists them), and 'monthly' in
    its stem (the core-index row's statement 3);
  - cross-subsidy surcharges in the open-access options (the cross-subsidy row's statement 3);
  - a start-up's age or turnover limit in the easy row (the start-ups row's statement 2);
  - incremental sales anywhere but the PLI case, which tests them;
  - a Rajasthan seller for the Tamil Nadu mill (linked regional grids answer the electricity-none row's
    statement 2), so both States are in the southern region."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write_updates, CODE
from polity_common import C3, C4, T2

d.SUBJECT = "Economy"
d.REQUIRE_CRAFT = True
IN = "Industry, Infrastructure, Energy & Services"
IG = "Inclusive Growth, Welfare & Demography"

# ================================================================ MCQs (6)
M(IN, "medium", "An RBI survey finds that manufacturers are using only about two-thirds of their installed capacity, and their order books have stopped growing. Which one of the following is the most likely to follow?",
  "RBI के एक सर्वेक्षण में पाया जाता है कि विनिर्माता अपनी स्थापित क्षमता का केवल लगभग दो-तिहाई उपयोग कर रहे हैं, और उनके ऑर्डर बढ़ना रुक गए हैं। निम्नलिखित में से किसके होने की सबसे अधिक संभावना है?",
  ["Firms will put off building new plants until demand picks up",
   "Firms will rush to build new plants, since a third of their capacity stands idle",
   "Prices of manufactured goods will rise sharply because supply cannot keep up with demand",
   "Factories will have to stop production until they can run at full capacity"],
  ["माँग बढ़ने तक फ़र्में नए संयंत्र लगाने का काम टाल देंगी",
   "फ़र्में तेज़ी से नए संयंत्र लगाएँगी, क्योंकि उनकी एक-तिहाई क्षमता बेकार पड़ी है",
   "विनिर्मित वस्तुओं की क़ीमतें तेज़ी से बढ़ेंगी क्योंकि आपूर्ति माँग के साथ नहीं चल पा रही",
   "कारख़ानों को तब तक उत्पादन रोकना पड़ेगा जब तक वे पूरी क्षमता पर न चल सकें"],
  0,
  "Capacity utilisation is actual output as a share of what installed capacity allows; the RBI tracks it in its quarterly OBICUS survey. With a third of capacity idle and orders flat, firms can meet any extra demand from existing plants, so they have little reason to invest in new ones -- which is why utilisation rising into the mid-70s per cent is read as a lead signal of a revival in private investment. "
  "Idle capacity also means supply is not the constraint, so it does not push prices up; and factories routinely run below full capacity.",
  "क्षमता उपयोग वास्तविक उत्पादन और स्थापित क्षमता से संभव उत्पादन का अनुपात है; RBI इसे अपने त्रैमासिक OBICUS सर्वेक्षण में देखता है। एक-तिहाई क्षमता खाली और ऑर्डर स्थिर होने पर फ़र्में अतिरिक्त माँग मौजूदा संयंत्रों से ही पूरी कर सकती हैं, इसलिए उनके पास नए संयंत्रों में निवेश का कम कारण होता है; इसीलिए उपयोग का 75 प्रतिशत के आसपास पहुँचना निजी निवेश में सुधार का अग्रिम संकेत माना जाता है। "
  "खाली क्षमता का अर्थ यह भी है कि आपूर्ति बाधा नहीं है, इसलिए यह क़ीमतें नहीं बढ़ाती; और कारख़ाने सामान्यतः पूरी क्षमता से कम पर चलते हैं।",
  "Reserve Bank of India -- Order Books, Inventories and Capacity Utilisation Survey (OBICUS).", "in-capacity-utilisation", craft="inference")

M(IN, "medium", "A large textile mill in Tamil Nadu wants to buy cheaper solar power directly from a developer's plant in Karnataka. Under the Electricity Act, 2003, the mill can do so:",
  "तमिलनाडु की एक बड़ी कपड़ा मिल कर्नाटक में एक डेवलपर के संयंत्र से सीधे सस्ती सौर बिजली ख़रीदना चाहती है। विद्युत अधिनियम, 2003 के तहत मिल ऐसा कर सकती है:",
  ["through open access, using the transmission and distribution networks for a charge",
   "only by first setting up a captive solar plant of its own on its premises in Tamil Nadu",
   "only after the State distribution company agrees to buy the power and resell it to the mill",
   "only if the Central Electricity Authority first registers the mill as an inter-State power trader"],
  ["ओपन एक्सेस के माध्यम से, शुल्क देकर पारेषण और वितरण नेटवर्क का उपयोग करते हुए",
   "केवल पहले तमिलनाडु में अपने परिसर पर अपना एक कैप्टिव सौर संयंत्र लगाकर",
   "केवल तब जब राज्य की वितरण कंपनी बिजली ख़रीदकर मिल को दोबारा बेचने को राज़ी हो",
   "केवल तब जब केंद्रीय विद्युत प्राधिकरण पहले मिल को अंतर-राज्यीय बिजली व्यापारी के रूप में पंजीकृत करे"],
  0,
  "Open access, introduced by the Electricity Act, 2003, lets consumers above a size limit -- normally 1 MW, and 100 kW under the green energy open access rules of 2022 -- buy power from a generator of their choice, even in another State. "
  "The power still flows over the inter-State transmission system and the local distribution network, so the mill pays transmission and wheeling charges, and usually surcharges that compensate the local distributor for the customer it loses. It need not own a plant, route the purchase through the distributor, or become a trader.",
  "विद्युत अधिनियम, 2003 द्वारा शुरू किया गया ओपन एक्सेस एक आकार-सीमा से ऊपर के उपभोक्ताओं को, सामान्यतः 1 MW और 2022 के हरित ऊर्जा ओपन एक्सेस नियमों के तहत 100 kW, अपनी पसंद के उत्पादक से, दूसरे राज्य में भी, बिजली ख़रीदने देता है। "
  "बिजली फिर भी अंतर-राज्यीय पारेषण प्रणाली और स्थानीय वितरण नेटवर्क से होकर आती है, इसलिए मिल पारेषण और व्हीलिंग शुल्क देती है, और प्रायः ऐसे अधिभार भी जो स्थानीय वितरक को खोए ग्राहक की भरपाई करते हैं। उसे न अपना संयंत्र चाहिए, न वितरक के माध्यम से ख़रीद, न व्यापारी बनना।",
  "Ministry of Power -- Electricity Act, 2003; Green Energy Open Access Rules, 2022.", "in-open-access", craft="application")

M(IN, "medium", "A toy company based in the United States, which has made all its toys in China, opens a second supplier base in India but keeps its Chinese factories running. This is an example of:",
  "संयुक्त राज्य अमेरिका की एक खिलौना कंपनी, जो अपने सारे खिलौने चीन में बनवाती रही है, भारत में आपूर्तिकर्ताओं का एक दूसरा आधार खोलती है पर अपने चीनी कारख़ाने चालू रखती है। यह किसका उदाहरण है?",
  ["the 'China plus one' strategy", "reshoring production to the home country",
   "decoupling completely from China", "import substitution by India"],
  ["'चाइना प्लस वन' रणनीति", "उत्पादन को स्वदेश वापस लाना (रीशोरिंग)",
   "चीन से पूर्ण अलगाव (डीकपलिंग)", "भारत द्वारा आयात प्रतिस्थापन"],
  0,
  "'China plus one' means adding production in at least one other country while keeping the Chinese base, to spread the risk that trade tensions and pandemic shutdowns exposed. "
  "Reshoring would bring production back to the United States; decoupling would cut the Chinese link altogether, which the firm has not done; and import substitution is producing at home what a country used to import -- here India is making goods for export, not replacing its own imports. India's PLI schemes and trade deals aim to attract such shifts, in competition with Vietnam, Mexico and others.",
  "'चाइना प्लस वन' का अर्थ है चीनी आधार बनाए रखते हुए कम से कम एक अन्य देश में उत्पादन जोड़ना, ताकि व्यापार तनाव और महामारी के बंद से उजागर हुआ जोखिम बँट जाए। "
  "रीशोरिंग उत्पादन को अमेरिका वापस ले जाती; डीकपलिंग चीनी संबंध पूरी तरह तोड़ देती, जो फ़र्म ने नहीं किया; और आयात प्रतिस्थापन का अर्थ है देश में वह बनाना जो पहले आयात होता था, जबकि यहाँ भारत निर्यात के लिए माल बना रहा है, अपने आयात की जगह नहीं। भारत की PLI योजनाएँ और व्यापार समझौते वियतनाम, मेक्सिको आदि से प्रतिस्पर्धा में ऐसे बदलावों को आकर्षित करना चाहते हैं।",
  "Economic Survey 2023-24 (Ministry of Finance).", "in-china-plus-one", craft="application")

M(IN, "hard", "Compared with a year earlier, output of coal and of natural gas rose by 5 per cent each, output of refinery products fell by 8 per cent, and the other core industries were unchanged. The Index of Eight Core Industries fell. This is best explained by the fact that:",
  "एक वर्ष पहले की तुलना में कोयले और प्राकृतिक गैस, दोनों का उत्पादन 5-5 प्रतिशत बढ़ा, रिफ़ाइनरी उत्पादों का उत्पादन 8 प्रतिशत घटा, और अन्य मूल उद्योग अपरिवर्तित रहे। आठ मूल उद्योगों का सूचकांक गिरा। इसकी सबसे अच्छी व्याख्या यह तथ्य करता है कि:",
  ["refinery products carry more weight in the index than coal and natural gas together",
   "the eight industries carry equal weights in the index, whatever their size",
   "the index tracks the prices of these products rather than output, and fuel prices fell",
   "coal and natural gas are part of the IIP but are not counted in the core index"],
  ["सूचकांक में रिफ़ाइनरी उत्पादों का भार कोयले और प्राकृतिक गैस के कुल भार से अधिक है",
   "सूचकांक में आठों उद्योगों का भार बराबर है, चाहे उनका आकार कुछ भी हो",
   "सूचकांक उत्पादन के बजाय इन उत्पादों की क़ीमतें मापता है, और ईंधन की क़ीमतें गिरीं",
   "कोयला और प्राकृतिक गैस IIP में शामिल हैं पर मूल उद्योग सूचकांक में नहीं गिने जाते"],
  0,
  "In the 2011-12 series, refinery products carry about 28 per cent of the weight, against about 10 for coal and 7 for natural gas. So the 8 per cent fall subtracts about 2.2 percentage points while the two rises add only about 0.9, and the index falls. "
  "With equal weights the two rises would have outweighed the single fall; the index measures the volume of output, not prices; and coal and natural gas are two of the eight core industries. Electricity (about 20) and steel (about 18) are the next heaviest, and fertilisers the lightest, at under 3.",
  "2011-12 श्रृंखला में रिफ़ाइनरी उत्पादों का भार लगभग 28 प्रतिशत है, जबकि कोयले का लगभग 10 और प्राकृतिक गैस का 7। इसलिए 8 प्रतिशत की गिरावट लगभग 2.2 प्रतिशत अंक घटाती है जबकि दोनों वृद्धियाँ केवल लगभग 0.9 जोड़ती हैं, और सूचकांक गिरता है। "
  "बराबर भार होने पर दोनों वृद्धियाँ अकेली गिरावट पर भारी पड़तीं; सूचकांक उत्पादन की मात्रा मापता है, क़ीमतें नहीं; और कोयला तथा प्राकृतिक गैस आठ मूल उद्योगों में से दो हैं। बिजली (लगभग 20) और इस्पात (लगभग 18) अगले सबसे भारी हैं, और उर्वरक सबसे हल्के, 3 से कम।",
  "Office of the Economic Adviser, DPIIT -- Index of Eight Core Industries.", "in-core-industries-weights", craft="application")

M(IN, "medium", "Under the Centre's Viability Gap Funding scheme for public-private partnership projects, support is given as:",
  "सार्वजनिक-निजी भागीदारी परियोजनाओं के लिए केंद्र की व्यवहार्यता अंतर वित्तपोषण (VGF) योजना के तहत सहायता किस रूप में दी जाती है?",
  ["a grant towards the capital cost, capped at a share of the project cost",
   "an annual subsidy paid for the project's whole life to cover its operating losses",
   "a guarantee that the government will make good any shortfall in traffic or tolls",
   "an interest-free loan to the developer, to be repaid out of the project's user charges"],
  ["पूँजी लागत के लिए अनुदान, जिसकी सीमा परियोजना लागत का एक अंश है",
   "परियोजना के पूरे जीवनकाल तक उसके परिचालन घाटे को पूरा करने के लिए वार्षिक सब्सिडी",
   "यह गारंटी कि यातायात या टोल में कोई भी कमी सरकार पूरी करेगी",
   "डेवलपर को ब्याज-मुक्त ऋण, जो परियोजना के उपयोगकर्ता शुल्क से चुकाया जाएगा"],
  0,
  "Some projects -- rural roads, water supply, hospitals -- bring large benefits to society but cannot charge users enough to repay private capital. VGF closes that gap with a grant, released during construction after the developer has put in its equity: up to 20 per cent of the total project cost from the Centre, with the sponsoring ministry or State able to add up to another 20 per cent. "
  "For social-sector pilot projects the limits are higher and some operating support is allowed in the first five years. The grant is not repaid, is not a lifelong subsidy and does not guarantee traffic; the bidder seeking the least VGF usually wins. The same term is used more loosely under the UDAN regional air scheme, where the Centre and States pay airlines a per-seat subsidy on regional routes for a few years.",
  "कुछ परियोजनाएँ, जैसे ग्रामीण सड़कें, जल आपूर्ति, अस्पताल, समाज को बड़े लाभ देती हैं पर उपयोगकर्ताओं से इतना शुल्क नहीं ले सकतीं कि निजी पूँजी चुकाई जा सके। VGF यह अंतर एक अनुदान से पाटता है, जो डेवलपर के अपनी इक्विटी लगाने के बाद निर्माण के दौरान दिया जाता है: कुल परियोजना लागत का 20 प्रतिशत तक केंद्र से, और प्रायोजक मंत्रालय या राज्य 20 प्रतिशत तक और जोड़ सकते हैं। "
  "सामाजिक क्षेत्र की पायलट परियोजनाओं के लिए सीमाएँ अधिक हैं और पहले पाँच वर्षों में कुछ परिचालन सहायता भी मिल सकती है। अनुदान लौटाया नहीं जाता, यह आजीवन सब्सिडी नहीं है और यातायात की गारंटी नहीं देता; सबसे कम VGF माँगने वाला बोलीदाता प्रायः जीतता है। उड़ान क्षेत्रीय हवाई योजना में यही शब्द अधिक ढीले अर्थ में प्रयुक्त होता है, जहाँ केंद्र और राज्य क्षेत्रीय मार्गों पर कुछ वर्षों तक एयरलाइनों को प्रति-सीट सब्सिडी देते हैं।",
  "Department of Economic Affairs -- Scheme for Financial Support to PPPs in Infrastructure (VGF Scheme).", "in-viability-gap-funding", craft="precision")

M(IG, "medium", "Under the 'Lakhpati Didi' initiative, a member of a self-help group is counted as a 'Lakhpati Didi' when:",
  "'लखपति दीदी' पहल के तहत स्वयं सहायता समूह की किसी सदस्य को 'लखपति दीदी' कब गिना जाता है?",
  ["her household earns at least ₹1 lakh a year, sustained over several seasons",
   "she receives a one-time grant of ₹1 lakh from the rural livelihoods mission",
   "her self-help group as a whole reaches an annual turnover of at least ₹1 lakh",
   "she takes a collateral-free loan of at least ₹1 lakh through her self-help group"],
  ["उसके परिवार की आय कम से कम ₹1 लाख प्रति वर्ष हो, जो कई मौसमों तक बनी रहे",
   "उसे ग्रामीण आजीविका मिशन से ₹1 लाख का एकमुश्त अनुदान मिले",
   "उसके स्वयं सहायता समूह का कुल वार्षिक कारोबार कम से कम ₹1 लाख हो जाए",
   "वह अपने स्वयं सहायता समूह के माध्यम से कम से कम ₹1 लाख का बिना गारंटी ऋण ले"],
  0,
  "A Lakhpati Didi is an SHG member whose annual household income is ₹1 lakh or more, measured over at least four agricultural seasons or business cycles with an average monthly income above ₹10,000, so that the gain is sustained rather than a one-off. The test is income -- not a grant, a loan or the group's turnover. "
  "Working through the Deendayal Antyodaya Yojana-National Rural Livelihoods Mission, the initiative aims at three crore such women, through farm and non-farm enterprises, skills and market links.",
  "लखपति दीदी वह स्वयं सहायता समूह सदस्य है जिसकी वार्षिक पारिवारिक आय ₹1 लाख या अधिक हो, जिसे कम से कम चार कृषि मौसमों या व्यावसायिक चक्रों में ₹10,000 से अधिक की औसत मासिक आय के साथ मापा जाता है, ताकि लाभ एक बार का न होकर टिकाऊ हो। कसौटी आय है, न कि अनुदान, ऋण या समूह का कारोबार। "
  "दीनदयाल अंत्योदय योजना-राष्ट्रीय ग्रामीण आजीविका मिशन के माध्यम से यह पहल कृषि और ग़ैर-कृषि उद्यमों, कौशल और बाज़ार संपर्कों द्वारा तीन करोड़ ऐसी महिलाओं का लक्ष्य रखती है।",
  "Ministry of Rural Development -- DAY-NRLM, Lakhpati Didi.", "ig-lakhpati-didi", craft="precision")

# ================================================================ two-statement row (1)
S(IN, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["A start-up is a newly established business.",
   "A company in which the government holds 51 per cent of the shares is in the public sector, even though private investors own the rest."],
  ["स्टार्ट-अप एक नया स्थापित व्यवसाय है।",
   "जिस कंपनी के 51 प्रतिशत शेयर सरकार के पास हों वह सार्वजनिक क्षेत्र में है, भले ही शेष शेयर निजी निवेशकों के पास हों।"],
  T2, 2,
  "Both statements are correct. What decides the sector is who owns and controls the enterprise: with a majority of the shares, the government controls the board, and the firm is a government company even when a minority of its shares are traded on the stock market. Many listed public sector enterprises have private shareholders in this way.",
  "दोनों कथन सही हैं। क्षेत्र इससे तय होता है कि उद्यम का स्वामित्व और नियंत्रण किसके पास है: अधिकांश शेयर होने पर बोर्ड पर सरकार का नियंत्रण होता है, और फ़र्म एक सरकारी कंपनी है भले ही उसके कुछ अल्प शेयर शेयर बाज़ार में बिकते हों। बहुत-से सूचीबद्ध सार्वजनिक उपक्रमों में इसी तरह निजी शेयरधारक हैं।",
  "NCERT Class X, Understanding Economic Development; Companies Act, 2013.", "in-startup-public-sector-easy", craft="application")

# ================================================================ three- and four-statement rows (8)
S(IN, "hard", "Consider the following statements about electronics manufacturing:",
  "इलेक्ट्रॉनिक्स विनिर्माण के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The PLI scheme helped India become a net exporter of mobile phones.",
   "Apple's iPhones are assembled in India through contract manufacturers.",
   "Electronics goods have overtaken engineering goods as India's largest export group."],
  ["PLI योजना ने भारत को मोबाइल फ़ोन का शुद्ध निर्यातक बनने में मदद की।",
   "एप्पल के iPhone भारत में अनुबंध निर्माताओं के ज़रिए असेंबल किए जाते हैं।",
   "इलेक्ट्रॉनिक वस्तुएँ इंजीनियरिंग वस्तुओं को पीछे छोड़कर भारत का सबसे बड़ा निर्यात समूह बन गई हैं।"],
  C3, 1,
  "Statements 1 and 2 are correct: from importing most of its phones a decade ago, India now exports well over 20 billion dollars' worth a year, largely iPhones assembled by firms such as Foxconn and Tata Electronics, and smartphones have become one of the country's largest single export items. "
  "Statement 3 is wrong: electronics goods, at about 39 billion dollars in 2024-25, remain far behind engineering goods, India's largest export group at over 110 billion dollars, and behind petroleum products too.",
  "कथन 1 और 2 सही हैं: एक दशक पहले अपने अधिकांश फ़ोन आयात करने वाला भारत अब हर वर्ष 20 अरब डॉलर से कहीं अधिक के फ़ोन निर्यात करता है, जिनमें अधिकतर फ़ॉक्सकॉन और टाटा इलेक्ट्रॉनिक्स जैसी फ़र्मों द्वारा असेंबल किए गए iPhone हैं, और स्मार्टफ़ोन देश की सबसे बड़ी एकल निर्यात मदों में से एक बन गए हैं। "
  "कथन 3 गलत है: 2024-25 में लगभग 39 अरब डॉलर की इलेक्ट्रॉनिक वस्तुएँ 110 अरब डॉलर से अधिक वाले भारत के सबसे बड़े निर्यात समूह, इंजीनियरिंग वस्तुओं, से बहुत पीछे हैं, और पेट्रोलियम उत्पादों से भी।",
  "Ministry of Commerce and Industry; Ministry of Electronics and Information Technology.", "in-electronics-pli-exports", craft="recall")

S(IN, "medium", "A firm approved under the PLI scheme for mobile phones sold phones made in India worth ₹1,000 crore in the base year. This year it sells phones made in India worth ₹1,500 crore, and also resells imported phones worth ₹200 crore. Assume an incentive rate of 4 per cent. Consider the following statements:",
  "मोबाइल फ़ोन के लिए PLI योजना के तहत स्वीकृत एक फ़र्म ने आधार वर्ष में भारत में बने ₹1,000 करोड़ के फ़ोन बेचे। इस वर्ष वह भारत में बने ₹1,500 करोड़ के फ़ोन बेचती है, और ₹200 करोड़ के आयातित फ़ोन भी दोबारा बेचती है। प्रोत्साहन दर 4 प्रतिशत मान लीजिए। निम्नलिखित कथनों पर विचार कीजिए:",
  ["Its incentive for this year is ₹20 crore.",
   "The imported phones it resells also add to its incentive.",
   "If its sales of phones made in India fell back to ₹1,000 crore, it would still earn ₹40 crore."],
  ["इस वर्ष उसका प्रोत्साहन ₹20 करोड़ है।",
   "वह जो आयातित फ़ोन दोबारा बेचती है, वे भी उसका प्रोत्साहन बढ़ाते हैं।",
   "यदि भारत में बने फ़ोनों की उसकी बिक्री वापस ₹1,000 करोड़ पर आ जाए, तो भी उसे ₹40 करोड़ मिलेंगे।"],
  C3, 0,
  "Only statement 1 is correct. PLI incentives are paid on incremental sales of goods made in India over a base year: 4 per cent of (1,500 - 1,000) = ₹20 crore. Imported phones are not made in India, so they earn nothing (statement 2); and if sales fall back to the base-year level there is no increment, so the incentive is zero, not 4 per cent of the whole ₹1,000 crore (statement 3). Firms must also meet thresholds of incremental investment. "
  "Launched in 2020 with mobile phones and electronics, the PLI schemes now cover 14 sectors with an outlay of about ₹1.97 lakh crore; tying the reward to added output pushes firms to scale up.",
  "केवल कथन 1 सही है। PLI प्रोत्साहन आधार वर्ष की तुलना में भारत में बनी वस्तुओं की वृद्धिशील बिक्री पर दिया जाता है: (1,500 - 1,000) का 4 प्रतिशत = ₹20 करोड़। आयातित फ़ोन भारत में नहीं बने, इसलिए उन पर कुछ नहीं मिलता (कथन 2); और बिक्री आधार वर्ष के स्तर पर लौट आए तो कोई वृद्धि नहीं है, इसलिए प्रोत्साहन शून्य है, पूरे ₹1,000 करोड़ का 4 प्रतिशत नहीं (कथन 3)। फ़र्मों को वृद्धिशील निवेश की सीमाएँ भी पूरी करनी होती हैं। "
  "2020 में मोबाइल फ़ोन और इलेक्ट्रॉनिक्स से शुरू हुई PLI योजनाएँ अब लगभग ₹1.97 लाख करोड़ के परिव्यय के साथ 14 क्षेत्रों में हैं; पुरस्कार को अतिरिक्त उत्पादन से जोड़ना फ़र्मों को पैमाना बढ़ाने के लिए प्रेरित करता है।",
  "Ministry of Electronics and Information Technology -- PLI Scheme for Large Scale Electronics Manufacturing.", "in-pli", craft="application")

S(IN, "medium", "Consider the following statements about electricity distribution:",
  "बिजली वितरण के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Aggregate technical and commercial (AT&C) losses include power that is billed but never paid for, not only power lost in the wires.",
   "Smart prepaid meters, funded under the Revamped Distribution Sector Scheme, cut the commercial part of these losses because consumers pay before they use power.",
   "Private distribution companies serve most of India's electricity consumers."],
  ["समग्र तकनीकी और वाणिज्यिक (AT&C) हानियों में वह बिजली भी शामिल है जिसका बिल बनता है पर भुगतान नहीं होता, केवल तारों में नष्ट हुई बिजली नहीं।",
   "संशोधित वितरण क्षेत्र योजना के तहत वित्तपोषित स्मार्ट प्रीपेड मीटर इन हानियों के वाणिज्यिक भाग को घटाते हैं, क्योंकि उपभोक्ता बिजली उपयोग करने से पहले भुगतान करते हैं।",
   "निजी वितरण कंपनियाँ भारत के अधिकांश बिजली उपभोक्ताओं को सेवा देती हैं।"],
  C3, 1,
  "Statements 1 and 2 are correct. AT&C losses combine technical losses in lines and transformers with commercial losses -- theft, unbilled supply and bills that are not collected -- which is why they fell from over 22 per cent in 2020-21 to about 16 per cent in 2023-24 as billing and collection improved. "
  "A prepaid meter removes the collection problem altogether, and smart meters also show where power is being stolen; the RDSS (2021) ties its funds to such metering and to loss-reduction targets. Statement 3 is wrong: most consumers are served by State-owned distribution companies; private distribution is limited to a few areas such as Delhi, Mumbai, Kolkata, Ahmedabad, Surat and Odisha.",
  "कथन 1 और 2 सही हैं। AT&C हानियाँ लाइनों और ट्रांसफ़ॉर्मरों की तकनीकी हानियों को वाणिज्यिक हानियों, यानी चोरी, बिना बिल की आपूर्ति और वसूल न हुए बिलों, के साथ जोड़ती हैं; इसीलिए बिलिंग और वसूली सुधरने से वे 2020-21 के 22 प्रतिशत से अधिक से घटकर 2023-24 में लगभग 16 प्रतिशत रह गईं। "
  "प्रीपेड मीटर वसूली की समस्या पूरी तरह हटा देता है, और स्मार्ट मीटर यह भी दिखाते हैं कि बिजली कहाँ चोरी हो रही है; RDSS (2021) अपना धन ऐसी मीटरिंग और हानि घटाने के लक्ष्यों से जोड़ती है। कथन 3 गलत है: अधिकांश उपभोक्ताओं को राज्य-स्वामित्व वाली वितरण कंपनियाँ सेवा देती हैं; निजी वितरण दिल्ली, मुंबई, कोलकाता, अहमदाबाद, सूरत और ओडिशा जैसे कुछ क्षेत्रों तक सीमित है।",
  "Ministry of Power -- Revamped Distribution Sector Scheme; Power Finance Corporation, Report on Performance of Power Utilities.", "in-discoms-atc", craft="linkage")

S(IN, "medium", "Consider the following statements about the Index of Industrial Production (IIP):",
  "औद्योगिक उत्पादन सूचकांक (IIP) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It measures changes in the volume of industrial output, not its value.",
   "Construction is one of the three sectors that the IIP covers.",
   "Under the IIP's use-based classification, infrastructure and construction goods form one of the groups."],
  ["यह औद्योगिक उत्पादन की मात्रा में बदलाव मापता है, उसके मूल्य में नहीं।",
   "निर्माण (कंस्ट्रक्शन) उन तीन क्षेत्रों में से एक है जिन्हें IIP शामिल करता है।",
   "IIP के उपयोग-आधारित वर्गीकरण में अवसंरचना और निर्माण वस्तुएँ एक समूह हैं।"],
  C3, 1,
  "Statements 1 and 3 are correct. The IIP, released monthly by the National Statistics Office, covers three sectors -- mining, manufacturing and electricity -- with manufacturing carrying over three-quarters of the weight. Construction activity itself is not one of them, which is the near-miss in statement 2. "
  "The use-based classification regroups the same output into primary, capital, intermediate, infrastructure/construction, consumer durable and consumer non-durable goods, so products such as cement and structural steel appear under 'infrastructure/construction goods'.",
  "कथन 1 और 3 सही हैं। राष्ट्रीय सांख्यिकी कार्यालय द्वारा हर महीने जारी IIP तीन क्षेत्रों, खनन, विनिर्माण और बिजली, को शामिल करता है, जिनमें विनिर्माण का भार तीन-चौथाई से अधिक है। स्वयं निर्माण गतिविधि उनमें से एक नहीं है, यही कथन 2 का निकट-भ्रम है। "
  "उपयोग-आधारित वर्गीकरण उसी उत्पादन को प्राथमिक, पूँजीगत, मध्यवर्ती, अवसंरचना/निर्माण, टिकाऊ उपभोक्ता और ग़ैर-टिकाऊ उपभोक्ता वस्तुओं में फिर से बाँटता है, इसलिए सीमेंट और संरचनात्मक इस्पात जैसे उत्पाद 'अवसंरचना/निर्माण वस्तुओं' में आते हैं।",
  "Ministry of Statistics and Programme Implementation -- Index of Industrial Production.", "in-iip", craft="precision")

S(IN, "medium", "Consider the following statements about semiconductors in India:",
  "भारत में सेमीकंडक्टर के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Under the India Semiconductor Mission, the Centre offers fiscal support of up to half the project cost for chip fabrication plants.",
   "Micron's facility at Sanand in Gujarat assembles, tests and packages chips rather than making wafers.",
   "The first chip fabrication plant approved under the mission is being built at Dholera in Gujarat by Tata Electronics with Taiwan's PSMC."],
  ["भारत सेमीकंडक्टर मिशन के तहत केंद्र चिप निर्माण (फ़ैब) संयंत्रों के लिए परियोजना लागत के आधे तक की वित्तीय सहायता देता है।",
   "गुजरात के साणंद में माइक्रोन की इकाई वेफ़र बनाने के बजाय चिप्स को असेंबल, परीक्षण और पैकेज करती है।",
   "मिशन के तहत स्वीकृत पहला चिप निर्माण संयंत्र गुजरात के धोलेरा में टाटा इलेक्ट्रॉनिक्स ताइवान की PSMC के साथ बना रही है।"],
  C3, 2,
  "All three are correct. The mission (2021), under the Ministry of Electronics and IT, offers support of up to 50 per cent of project cost on a pari-passu basis for fabs and for assembly, testing, marking and packaging (ATMP/OSAT) units, and States add their own incentives. "
  "Micron's Sanand plant, approved in 2023, is an ATMP unit that turns imported wafers into finished memory chips -- the trap is to call it a fab. The Tata-PSMC fab at Dholera, approved in 2024, is the first commercial fab; several packaging units have also been approved in Assam, Gujarat and elsewhere.",
  "तीनों कथन सही हैं। इलेक्ट्रॉनिकी और सूचना प्रौद्योगिकी मंत्रालय के अधीन मिशन (2021) फ़ैब और असेंबली, परीक्षण, मार्किंग और पैकेजिंग (ATMP/OSAT) इकाइयों के लिए समान-अनुपात आधार पर परियोजना लागत के 50 प्रतिशत तक की सहायता देता है, और राज्य अपने प्रोत्साहन जोड़ते हैं। "
  "2023 में स्वीकृत माइक्रोन का साणंद संयंत्र एक ATMP इकाई है जो आयातित वेफ़रों को तैयार मेमोरी चिप्स में बदलती है; उसे फ़ैब कहना ही जाल है। 2024 में स्वीकृत धोलेरा का टाटा-PSMC फ़ैब पहला व्यावसायिक फ़ैब है; असम, गुजरात और अन्य जगहों पर कई पैकेजिंग इकाइयाँ भी स्वीकृत हुई हैं।",
  "Ministry of Electronics and Information Technology -- India Semiconductor Mission.", "in-semiconductors", craft="precision")

S(IN, "medium", "Consider the following statements about oil:",
  "तेल के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["India's strategic petroleum reserves are built and managed by Indian Strategic Petroleum Reserves Limited, a special purpose vehicle under the Oil Industry Development Board.",
   "The crude stored in the reserve caverns at Visakhapatnam, Mangaluru and Padur can meet India's needs for about three months.",
   "India's domestic crude oil production has been rising steadily over the past decade."],
  ["भारत के सामरिक पेट्रोलियम भंडार तेल उद्योग विकास बोर्ड के अंतर्गत एक विशेष प्रयोजन वाहन, इंडियन स्ट्रैटेजिक पेट्रोलियम रिज़र्व्स लिमिटेड, बनाती और प्रबंधित करती है।",
   "विशाखापत्तनम, मंगलुरु और पादुर की भंडार गुफाओं में रखा कच्चा तेल भारत की लगभग तीन महीने की ज़रूरत पूरी कर सकता है।",
   "पिछले एक दशक में भारत का घरेलू कच्चे तेल का उत्पादन लगातार बढ़ा है।"],
  C3, 0,
  "Only statement 1 is correct. The three underground caverns hold about 5.33 million tonnes of crude -- roughly nine to ten days of the country's requirement, not three months; counting the stocks held by oil companies, India has cover for about two and a half months. The 90-day figure is the import cover that members of the International Energy Agency must hold -- the near-miss here. "
  "Statement 3 is wrong: domestic output has been flat or falling for over a decade, at under 30 million tonnes a year, so India imports more than 85 per cent of its crude -- which is why the reserves matter and more caverns are planned at Chandikhol and Padur.",
  "केवल कथन 1 सही है। तीनों भूमिगत गुफाएँ लगभग 53.3 लाख टन कच्चा तेल रखती हैं, यानी देश की लगभग नौ से दस दिन की ज़रूरत, तीन महीने नहीं; तेल कंपनियों के भंडार जोड़ने पर भारत के पास लगभग ढाई महीने का भंडार है। 90 दिन का आँकड़ा वह आयात भंडार है जो अंतरराष्ट्रीय ऊर्जा एजेंसी के सदस्यों को रखना होता है; यही यहाँ निकट-भ्रम है। "
  "कथन 3 गलत है: घरेलू उत्पादन एक दशक से अधिक समय से स्थिर या घटता रहा है, 3 करोड़ टन प्रति वर्ष से कम, इसलिए भारत अपने कच्चे तेल का 85 प्रतिशत से अधिक आयात करता है; इसीलिए भंडार महत्त्वपूर्ण हैं और चंडीखोल तथा पादुर में और गुफाओं की योजना है।",
  "Ministry of Petroleum and Natural Gas; Petroleum Planning and Analysis Cell.", "in-oil-spr-imports", craft="precision")

S(IN, "medium", "Consider the following statements about digital infrastructure:",
  "डिजिटल अवसंरचना के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["BharatNet aims to connect all gram panchayats with optical fibre broadband.",
   "5G mobile services were launched in India in 2020.",
   "Most of India's telecom subscribers use fixed-line connections.",
   "Under PM-WANI, a small shop can offer public Wi-Fi as a Public Data Office without a telecom licence."],
  ["भारतनेट का लक्ष्य सभी ग्राम पंचायतों को ऑप्टिकल फ़ाइबर ब्रॉडबैंड से जोड़ना है।",
   "भारत में 5G मोबाइल सेवाएँ 2020 में शुरू की गईं।",
   "भारत के अधिकांश दूरसंचार ग्राहक फ़िक्स्ड-लाइन कनेक्शन उपयोग करते हैं।",
   "PM-WANI के तहत कोई छोटी दुकान बिना दूरसंचार लाइसेंस के पब्लिक डेटा ऑफ़िस के रूप में सार्वजनिक वाई-फ़ाई दे सकती है।"],
  C4, 1,
  "Statements 1 and 4 are correct. Under PM-WANI (2020), Public Data Offices -- tea stalls, kirana shops and the like -- need no licence, registration or fee to sell Wi-Fi access; only the aggregators that link them and the app providers register with the Department of Telecommunications. BharatNet, now being upgraded under the amended scheme, carries fibre to the panchayats on which such hotspots can draw. "
  "Statement 2 is wrong: 5G was launched in October 2022, after the spectrum auction of that year. Statement 3 is wrong: over 95 per cent of connections are wireless.",
  "कथन 1 और 4 सही हैं। PM-WANI (2020) के तहत पब्लिक डेटा ऑफ़िस, जैसे चाय की दुकानें, किराना दुकानें आदि, को वाई-फ़ाई सुविधा बेचने के लिए न लाइसेंस, न पंजीकरण, न शुल्क चाहिए; केवल उन्हें जोड़ने वाले एग्रीगेटर और ऐप प्रदाता दूरसंचार विभाग में पंजीकरण कराते हैं। अब संशोधित योजना के तहत उन्नत किया जा रहा भारतनेट पंचायतों तक फ़ाइबर पहुँचाता है, जिसका उपयोग ऐसे हॉटस्पॉट कर सकते हैं। "
  "कथन 2 गलत है: 5G उस वर्ष की स्पेक्ट्रम नीलामी के बाद अक्टूबर 2022 में शुरू हुआ। कथन 3 गलत है: 95 प्रतिशत से अधिक कनेक्शन वायरलेस हैं।",
  "Department of Telecommunications -- PM-WANI framework, 2020; BharatNet.", "in-digital-infrastructure", craft="precision")

S(IN, "medium", "Consider the following statements about logistics in India:",
  "भारत में लॉजिस्टिक्स के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["India adopted a National Logistics Policy in 2022.",
   "India was ranked 38th of 139 countries in the World Bank's Logistics Performance Index 2023, up from 44th in 2018.",
   "A study commissioned by the government estimated India's logistics costs at under 10 per cent of GDP, well below the 13-14 per cent often quoted."],
  ["भारत ने 2022 में राष्ट्रीय लॉजिस्टिक्स नीति अपनाई।",
   "विश्व बैंक के लॉजिस्टिक्स प्रदर्शन सूचकांक 2023 में भारत 139 देशों में 38वें स्थान पर रहा, जो 2018 के 44वें स्थान से बेहतर है।",
   "सरकार द्वारा कराए गए एक अध्ययन ने भारत की लॉजिस्टिक्स लागत GDP के 10 प्रतिशत से कम आँकी, जो प्रायः उद्धृत 13-14 प्रतिशत से काफ़ी कम है।"],
  C3, 2,
  "All three are correct. The National Logistics Policy (September 2022) aims to bring logistics costs down to global benchmarks and lift India into the top 25 of the LPI by 2030, working with PM Gati Shakti's GIS-based master plan for roads, railways, ports and pipelines. India's rise to 38th in 2023 owed much to faster port turnaround. "
  "The DPIIT-NCAER study of 2023 put logistics costs at about 7.8-8.9 per cent of GDP for 2021-22, far below the 13-14 per cent figure often cited earlier.",
  "तीनों कथन सही हैं। राष्ट्रीय लॉजिस्टिक्स नीति (सितंबर 2022) लॉजिस्टिक्स लागत को वैश्विक मानकों तक लाने और 2030 तक भारत को LPI के शीर्ष 25 में पहुँचाने का लक्ष्य रखती है, और सड़कों, रेल, बंदरगाहों और पाइपलाइनों के लिए PM गति शक्ति की GIS-आधारित मास्टर योजना के साथ काम करती है। 2023 में भारत के 38वें स्थान तक पहुँचने में बंदरगाहों पर तेज़ निपटान का बड़ा योगदान था। "
  "2023 के DPIIT-NCAER अध्ययन ने 2021-22 के लिए लॉजिस्टिक्स लागत GDP का लगभग 7.8-8.9 प्रतिशत आँकी, जो पहले प्रायः उद्धृत 13-14 प्रतिशत से बहुत कम है।",
  "Department for Promotion of Industry and Internal Trade -- National Logistics Policy, 2022; World Bank, Logistics Performance Index 2023.", "in-logistics", craft="precision")

# ================================================================ TAGS for the 69 kept rows (Test 21's 6 are tagged already)
TAGS = {
 "ag-irrigation-multiple-cropping-easy": "linkage", "ag-msp-inflation-tot": "linkage", "ag-diversification-water": "linkage",
 "ag-milk-largest-no-msp": "linkage", "ag-procurement-cropping-pattern": "linkage", "ag-allied-activity-easy": "recall",
 "ag-msp-numerical": "application", "ag-agmark": "recall", "ag-largest-subsidy": "recall",
 "ag-msp-not-covered": "precision", "ag-cobweb-engel": "inference", "ag-farm-credit-structure": "recall",
 "ag-land-leasing-none": "precision", "ag-pm-aasha": "precision", "ag-buffer-omss": "precision",
 "ag-farm-trade": "recall", "ag-fertiliser-nbs-urea": "precision", "ag-food-processing-none": "recall",
 "ag-irrigation-sources": "recall", "ag-land-holdings-census": "recall", "ag-model-acts-farm-laws": "precision",
 "ag-msp-cacp-crops": "precision", "ag-pmfby": "precision", "ag-procurement-none": "recall",
 "ag-structure-allied-growth": "recall",
 "ig-clean-cooking-health": "linkage", "ig-social-security-pairs": "precision", "ig-social-security-easy": "recall",
 "ig-female-lfpr": "recall", "ig-hces-2023-24": "recall", "ig-demography-tfr": "recall",
 "ig-mudra-standup-vishwakarma": "precision",
 "in-electricity-factories-easy": "linkage", "in-tourism-exports-easy": "linkage", "in-manufacturing-share-flat": "linkage",
 "in-solar-evening-storage": "linkage", "in-discom-losses-farm-tariffs": "linkage", "in-infrastructure-exports": "linkage",
 "in-manufacturing-jobs": "linkage", "in-mobile-phones-chips": "linkage", "in-public-sector-share": "linkage",
 "in-regulators-pairs": "precision", "in-infrastructure-easy": "recall", "in-non-renewable-easy": "recall",
 "in-services-gva-composition": "recall", "in-brownfield": "precision", "in-industry-4-0": "recall",
 "in-fishing-it-easy": "recall", "in-hydro-petrol-easy": "recall", "in-msme-steel-easy": "recall",
 "in-railways-roads-easy": "recall", "in-sectors-easy": "recall", "in-asi-asuse": "precision",
 "in-infra-finance-tools": "precision", "in-petroleum-pricing-none": "precision", "in-power-market-cross-subsidy": "precision",
 "in-premature-deindustrialisation": "precision", "in-coal": "recall", "in-core-industries-count": "multi",
 "in-core-industries-index": "recall", "in-electricity-none": "precision", "in-infra-finance-none": "precision",
 "in-manufacturing-policy": "recall", "in-msme-classification": "precision", "in-pmi": "precision",
 "in-ppp-ham-bot": "precision", "in-roads-nh-fastag": "recall", "in-services-share": "recall",
 "in-startups": "precision"}

if __name__ == "__main__":
    write_updates("upg_l2_t18_econ_b.sql", statuses=("draft", "published"), tags=TAGS)
