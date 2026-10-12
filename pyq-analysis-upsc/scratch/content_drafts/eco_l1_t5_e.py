# -*- coding: utf-8 -*-
"""Level 1 · Test 5 (Economy, NCERT Foundation) -- part E: External Sector & International Institutions (9) and
Budget, Deficits & Public Debt (6) (upsc_l1_cell_targets.mjs 5).
External: easy MCQ 1, easy statement 2, medium MCQ 1, medium statement 3, medium Statement-I/II 1, hard statement 1.
Budget: easy statement 1, medium MCQ 1, medium statement 2, medium Statement-I/II 1, hard statement 1.
The angle is NCERT Class X 'Globalisation and the Indian Economy' (MNCs, the forces behind globalisation, its uneven
effects, fair globalisation) and Class XII Introductory Macroeconomics (the foreign exchange market, autonomous and
accommodating transactions, the objectives of the budget, public goods, multipliers, public debt), with the Asian
Clearing Union and gender budgeting. Level-2 facts are not repeated (WTO, IMF and World Bank, Bretton Woods, BoP
accounts and remittances, trade agreements, SEZs, rupee convertibility and float, FDI/FPI, deficits and the FRBM,
crowding out, Ricardian equivalence, budgeting practices, receipts and spending). MCQ keys are pinned."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Economy"
d.REQUIRE_CRAFT = True
EX = "External Sector & International Institutions"
BD = "Budget, Deficits & Public Debt"
EC10 = "NCERT Class X, Economics -- Understanding Economic Development"
MAC = "NCERT Class XII, Economics -- Introductory Macroeconomics"

# ================================================================ EXTERNAL (9)
# ---------------------------------------------------------------- easy MCQ (1)
M(EX, "easy", "A company that owns or controls production in more than one nation is called",
  "एक से अधिक देशों में उत्पादन का स्वामित्व या नियंत्रण रखने वाली कंपनी क्या कहलाती है?",
  ["a multinational corporation", "a public sector undertaking", "a cooperative society", "a special purpose vehicle"],
  ["बहुराष्ट्रीय निगम", "सार्वजनिक क्षेत्र का उपक्रम", "सहकारी समिति", "विशेष प्रयोजन वाहन (SPV)"],
  0,
  "A multinational corporation (MNC) sets up offices and factories where it can get cheap labour and other resources, close to markets, so as to lower costs and earn greater profits. "
  "Production by MNCs is increasingly spread across countries -- a product may be designed in one country, its parts made in several others and assembled in yet another -- which is what links markets and producers in different countries.",
  "बहुराष्ट्रीय निगम (MNC) वहाँ कार्यालय और कारख़ाने लगाता है जहाँ उसे सस्ता श्रम और अन्य संसाधन मिलें, बाज़ारों के निकट, ताकि लागत घटे और अधिक लाभ हो। "
  "MNCs का उत्पादन बढ़ती मात्रा में अनेक देशों में फैला है -- कोई उत्पाद एक देश में डिज़ाइन होता है, उसके पुर्ज़े कई अन्य देशों में बनते हैं और किसी और देश में जोड़े जाते हैं -- यही विभिन्न देशों के बाज़ारों और उत्पादकों को जोड़ता है।",
  f"{EC10} (Globalisation and the Indian Economy).",
  "l1-eco-mnc-definition", pos=3, craft="recall")

# ---------------------------------------------------------------- easy statement (2)
S(EX, "easy", "Consider the following statements about how multinational corporations spread their production:",
  "बहुराष्ट्रीय निगम अपना उत्पादन कैसे फैलाते हैं, इस बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["MNCs sometimes buy up local companies to expand production, as Cargill Foods bought Parakh Foods in India.",
   "MNCs never place orders with small local producers."],
  ["MNCs कभी-कभी उत्पादन बढ़ाने के लिए स्थानीय कंपनियाँ ख़रीद लेते हैं, जैसे भारत में कारगिल फ़ूड्स ने पारख फ़ूड्स को ख़रीदा।",
   "MNCs कभी भी छोटे स्थानीय उत्पादकों को ऑर्डर नहीं देते।"],
  T2, 0,
  "Only statement 1 is correct: MNCs also set up production jointly with local companies, bringing money for new machines and the latest technology. "
  "Statement 2 is wrong: large MNCs in developed countries place orders with small producers for garments, footwear and sports items, and sell the products under their own brand names -- so they control production without owning the factories, and decide the price, quality and delivery terms.",
  "केवल कथन 1 सही है: MNCs स्थानीय कंपनियों के साथ मिलकर भी उत्पादन करते हैं, जिसमें वे नई मशीनों के लिए धन और नवीनतम तकनीक लाते हैं। "
  "कथन 2 गलत है: विकसित देशों के बड़े MNCs वस्त्र, जूते और खेल के सामान के लिए छोटे उत्पादकों को ऑर्डर देते हैं और उत्पादों को अपने ब्रांड नाम से बेचते हैं -- इस तरह वे कारख़ानों के स्वामी हुए बिना उत्पादन पर नियंत्रण रखते हैं और कीमत, गुणवत्ता तथा आपूर्ति की शर्तें तय करते हैं।",
  f"{EC10} (Globalisation and the Indian Economy).",
  "l1-eco-mnc-ways-of-spreading", craft="precision")

S(EX, "easy", "Consider the following statements about the factors that have enabled globalisation:",
  "वैश्वीकरण को संभव बनाने वाले कारकों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Improvements in transport technology, such as the use of containers, have cut the cost of moving goods over long distances.",
   "Information and communication technology allows services such as call centres to be provided from distant locations.",
   "Liberalisation means placing more barriers on foreign trade and investment."],
  ["परिवहन तकनीक में सुधार, जैसे कंटेनरों का उपयोग, ने लंबी दूरी तक माल ले जाने की लागत घटाई है।",
   "सूचना और संचार तकनीक कॉल सेंटर जैसी सेवाओं को दूर के स्थानों से देना संभव बनाती है।",
   "उदारीकरण का अर्थ है विदेशी व्यापार और निवेश पर अधिक अवरोध लगाना।"],
  C3, 1,
  "Statements 1 and 2 are correct: faster, cheaper transport and instant communication made it possible to spread production across countries and to deliver services far from the customer. "
  "Statement 3 is wrong: liberalisation means removing barriers or restrictions set by the government; India began removing many barriers on foreign trade and investment from around 1991, and the WTO pushed for further removal.",
  "कथन 1 और 2 सही हैं: तेज़, सस्ते परिवहन और तत्काल संचार ने उत्पादन को अनेक देशों में फैलाना और सेवाओं को ग्राहक से दूर से देना संभव बनाया। "
  "कथन 3 गलत है: उदारीकरण का अर्थ है सरकार द्वारा लगाए अवरोधों या प्रतिबंधों को हटाना; भारत ने लगभग 1991 से विदेशी व्यापार और निवेश पर से कई अवरोध हटाने शुरू किए, और WTO ने और अधिक हटाने पर ज़ोर दिया।",
  f"{EC10} (Globalisation and the Indian Economy).",
  "l1-eco-globalisation-enabling-factors", craft="recall")

# ---------------------------------------------------------------- medium MCQ (1)
M(EX, "medium", "The Asian Clearing Union, through which the central banks of India and several neighbouring countries settle payments for trade among them, has its headquarters in",
  "एशियाई समाशोधन संघ (Asian Clearing Union), जिसके माध्यम से भारत और कई पड़ोसी देशों के केंद्रीय बैंक आपसी व्यापार के भुगतान निपटाते हैं, का मुख्यालय कहाँ है?",
  ["Tehran", "Kathmandu", "Colombo", "New Delhi"],
  ["तेहरान", "काठमांडू", "कोलंबो", "नई दिल्ली"],
  0,
  "The Asian Clearing Union was set up in 1974 at the initiative of the UN Economic and Social Commission for Asia and the Pacific, with its headquarters in Tehran. Its members' central banks -- of Bangladesh, Bhutan, India, Iran, the Maldives, Myanmar, Nepal, Pakistan and Sri Lanka -- settle their trade payments on a net, multilateral basis at intervals, "
  "which saves foreign exchange and the costs of settling each transaction separately.",
  "एशियाई समाशोधन संघ 1974 में एशिया और प्रशांत के लिए संयुक्त राष्ट्र आर्थिक एवं सामाजिक आयोग की पहल पर बना, जिसका मुख्यालय तेहरान में है। इसके सदस्यों के केंद्रीय बैंक -- बांग्लादेश, भूटान, भारत, ईरान, मालदीव, म्यांमार, नेपाल, पाकिस्तान और श्रीलंका -- अपने व्यापार भुगतान अंतराल पर शुद्ध, बहुपक्षीय आधार पर निपटाते हैं, "
  "जिससे विदेशी मुद्रा और हर लेन-देन को अलग से निपटाने की लागत बचती है।",
  "Reserve Bank of India (Asian Clearing Union).",
  "l1-eco-asian-clearing-union", pos=3, craft="recall")

# ---------------------------------------------------------------- medium statement (3)
S(EX, "medium", "Consider the following statements about the impact of globalisation on India:",
  "भारत पर वैश्वीकरण के प्रभाव के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It has given consumers, particularly the well-off in urban areas, greater choice, better quality and lower prices.",
   "MNCs have increased their investments in India in industries such as cell phones, automobiles, electronics, soft drinks and fast food.",
   "Some large Indian companies have themselves emerged as multinationals."],
  ["इसने उपभोक्ताओं, विशेषकर नगरीय क्षेत्रों के संपन्न लोगों, को अधिक विकल्प, बेहतर गुणवत्ता और कम कीमतें दी हैं।",
   "MNCs ने भारत में मोबाइल फ़ोन, वाहन, इलेक्ट्रॉनिक्स, शीतल पेय और फ़ास्ट फ़ूड जैसे उद्योगों में अपना निवेश बढ़ाया है।",
   "कुछ बड़ी भारतीय कंपनियाँ स्वयं बहुराष्ट्रीय बनकर उभरी हैं।"],
  C3, 2,
  "All three statements are correct. Top Indian companies gained from the competition by investing in new technology and raising standards, and some have spread their operations worldwide; new jobs have also been created in services, especially information technology. "
  "NCERT stresses, however, that the benefits have not been shared evenly among producers and workers.",
  "तीनों कथन सही हैं। शीर्ष भारतीय कंपनियों ने नई तकनीक में निवेश करके और मानक ऊँचे करके प्रतिस्पर्धा से लाभ उठाया, और कुछ ने अपने काम विश्व भर में फैलाए; सेवाओं, विशेषकर सूचना तकनीक, में नए रोज़गार भी पैदा हुए हैं। "
  "फिर भी NCERT ज़ोर देता है कि लाभ उत्पादकों और श्रमिकों में बराबर नहीं बँटे हैं।",
  f"{EC10} (Globalisation and the Indian Economy).",
  "l1-eco-globalisation-impact-india", craft="recall")

S(EX, "medium", "Consider the following statements about the foreign exchange market:",
  "विदेशी विनिमय बाज़ार के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The demand for foreign exchange arises from imports of goods and services, purchases of assets abroad and travel abroad.",
   "The supply of foreign exchange comes from exports, foreign tourists visiting the country and inflows of foreign investment.",
   "A rise in the number of foreign tourists visiting India reduces the supply of foreign exchange."],
  ["विदेशी मुद्रा की माँग वस्तुओं और सेवाओं के आयात, विदेश में परिसंपत्तियों की ख़रीद और विदेश यात्रा से उत्पन्न होती है।",
   "विदेशी मुद्रा की आपूर्ति निर्यात, देश में आने वाले विदेशी पर्यटकों और विदेशी निवेश के अंतर्वाह से आती है।",
   "भारत आने वाले विदेशी पर्यटकों की संख्या बढ़ने से विदेशी मुद्रा की आपूर्ति घटती है।"],
  C3, 1,
  "Statements 1 and 2 are correct: the exchange rate is the price at which the demand for and supply of foreign exchange are equal in the market. "
  "Statement 3 is wrong: foreign tourists bring foreign currency to spend in India, so more tourists raise the supply of foreign exchange; other things equal, this tends to make the rupee appreciate.",
  "कथन 1 और 2 सही हैं: विनिमय दर वह कीमत है जिस पर बाज़ार में विदेशी मुद्रा की माँग और आपूर्ति बराबर होती है। "
  "कथन 3 गलत है: विदेशी पर्यटक भारत में ख़र्च करने के लिए विदेशी मुद्रा लाते हैं, इसलिए अधिक पर्यटक विदेशी मुद्रा की आपूर्ति बढ़ाते हैं; अन्य बातें समान रहने पर इससे रुपये का अधिमूल्यन होता है।",
  f"{MAC} (Open Economy Macroeconomics).",
  "l1-eco-forex-demand-supply-sources", craft="application")

S(EX, "medium", "According to NCERT, a government seeking 'fair globalisation' can:",
  "NCERT के अनुसार, 'न्यायसंगत वैश्वीकरण' चाहने वाली सरकार क्या कर सकती है?",
  ["ensure that labour laws are properly implemented and workers get their rights.",
   "support small producers to improve their performance until they become strong enough to compete.",
   "use trade and investment barriers if necessary.",
   "negotiate at the WTO for fairer rules, aligning with developing countries that share its interests."],
  ["यह सुनिश्चित करना कि श्रम क़ानूनों का ठीक से पालन हो और श्रमिकों को उनके अधिकार मिलें।",
   "छोटे उत्पादकों को तब तक प्रदर्शन सुधारने में सहायता देना जब तक वे प्रतिस्पर्धा के लायक़ मज़बूत न हो जाएँ।",
   "आवश्यकता हो तो व्यापार और निवेश अवरोधों का उपयोग करना।",
   "समान हितों वाले विकासशील देशों के साथ मिलकर WTO में अधिक न्यायसंगत नियमों के लिए वार्ता करना।"],
  C4, 3,
  "All four are means NCERT lists. Fair globalisation would create opportunities for all and ensure that its benefits are better shared; the government can see that this happens, and people's organisations and campaigns have also influenced decisions on trade and investment at the WTO. "
  "The emphasis on support until producers can compete reflects the experience of small industries hurt by sudden competition.",
  "चारों वे उपाय हैं जो NCERT गिनाता है। न्यायसंगत वैश्वीकरण सबके लिए अवसर पैदा करेगा और उसके लाभों का बेहतर बँटवारा सुनिश्चित करेगा; सरकार यह होते देख सकती है, और जन संगठनों तथा अभियानों ने भी WTO में व्यापार और निवेश के निर्णयों को प्रभावित किया है। "
  "प्रतिस्पर्धा लायक़ होने तक सहायता पर ज़ोर अचानक प्रतिस्पर्धा से आहत लघु उद्योगों के अनुभव को दर्शाता है।",
  f"{EC10} (Globalisation and the Indian Economy).",
  "l1-eco-fair-globalisation-measures", craft="recall")

# ---------------------------------------------------------------- medium Statement-I/II (1)
A(EX, "medium",
  "Many small manufacturers in India, of goods such as batteries, capacitors, plastics and toys, were hit hard after globalisation.",
  "वैश्वीकरण के बाद भारत में बैटरी, संधारित्र, प्लास्टिक और खिलौनों जैसी वस्तुओं के कई छोटे उत्पादकों पर भारी चोट पड़ी।",
  "Once trade barriers were lowered, they faced severe competition from cheaper imports.",
  "व्यापार अवरोध घटने के बाद उन्हें सस्ते आयातों से कड़ी प्रतिस्पर्धा का सामना करना पड़ा।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I. Several such units shut down, leaving workers jobless, which matters because small industries are the largest employers in the country after agriculture. "
  "Competition also led many employers to hire workers 'flexibly', on temporary terms, so that more jobs became insecure even where firms survived.",
  "दोनों कथन सही हैं, और कथन-II कथन-I की व्याख्या करता है। ऐसी कई इकाइयाँ बंद हो गईं और श्रमिक बेरोज़गार हो गए, जो महत्त्वपूर्ण है क्योंकि कृषि के बाद लघु उद्योग देश के सबसे बड़े नियोक्ता हैं। "
  "प्रतिस्पर्धा के कारण कई नियोक्ताओं ने श्रमिकों को 'लचीले' ढंग से, अस्थायी शर्तों पर रखना शुरू किया, जिससे फ़र्में बचने पर भी अधिक नौकरियाँ असुरक्षित हो गईं।",
  f"{EC10} (Globalisation and the Indian Economy).",
  "l1-eco-small-producers-hit-imports", craft="inference")

# ---------------------------------------------------------------- hard statement (1)
S(EX, "hard", "Consider the following statements about transactions in the balance of payments:",
  "भुगतान संतुलन के लेन-देनों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Autonomous transactions are undertaken for their own sake, such as for profit, independently of the state of the balance of payments.",
   "Accommodating transactions are determined by the net result of the autonomous ones, and cover the gap between them.",
   "Official reserve transactions, in which the central bank draws down or adds to its reserves, are regarded as accommodating."],
  ["स्वायत्त लेन-देन अपने लिए, जैसे लाभ के लिए, भुगतान संतुलन की स्थिति से स्वतंत्र रूप से किए जाते हैं।",
   "समायोजक (accommodating) लेन-देन स्वायत्त लेन-देनों के शुद्ध परिणाम से तय होते हैं, और उनके बीच के अंतर को पूरा करते हैं।",
   "आधिकारिक आरक्षित लेन-देन, जिनमें केंद्रीय बैंक अपने भंडार घटाता या बढ़ाता है, समायोजक माने जाते हैं।"],
  C3, 2,
  "All three statements are correct. A balance of payments surplus or deficit is the excess or shortfall of autonomous receipts over autonomous payments -- the items 'above the line' -- and it is financed by accommodating items 'below the line'. "
  "If foreigners' autonomous demand for rupees falls short, the RBI sells foreign exchange from its reserves to fill the gap; a fall in reserves thus signals a deficit, and a rise a surplus.",
  "तीनों कथन सही हैं। भुगतान संतुलन का अधिशेष या घाटा स्वायत्त प्राप्तियों का स्वायत्त भुगतानों से अधिक या कम होना है -- 'रेखा के ऊपर' की मदें -- और इसका वित्तपोषण 'रेखा के नीचे' की समायोजक मदों से होता है। "
  "यदि विदेशियों की रुपयों के लिए स्वायत्त माँग कम पड़े, तो RBI अंतर भरने के लिए अपने भंडार से विदेशी मुद्रा बेचता है; इस प्रकार भंडार में गिरावट घाटे का, और वृद्धि अधिशेष का संकेत है।",
  f"{MAC} (Open Economy Macroeconomics).",
  "l1-eco-bop-autonomous-accommodating", craft="linkage")

# ================================================================ BUDGET (6)
# ---------------------------------------------------------------- easy statement (1)
S(BD, "easy", "Consider the following statements about the objectives of a government budget:",
  "सरकारी बजट के उद्देश्यों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Through its allocation function, the government provides public goods, such as national defence and roads, that the market will not supply in adequate measure.",
   "Through its redistribution function, the government uses taxes and transfers to bring about a fairer distribution of income.",
   "Through its stabilisation function, the government seeks to reduce fluctuations in income and employment."],
  ["आवंटन कार्य द्वारा सरकार राष्ट्रीय रक्षा और सड़कों जैसी सार्वजनिक वस्तुएँ उपलब्ध कराती है, जिन्हें बाज़ार पर्याप्त मात्रा में नहीं देगा।",
   "पुनर्वितरण कार्य द्वारा सरकार करों और अंतरणों से आय का अधिक न्यायसंगत वितरण लाती है।",
   "स्थिरीकरण कार्य द्वारा सरकार आय और रोज़गार में उतार-चढ़ाव घटाने का प्रयास करती है।"],
  C3, 2,
  "All three statements are correct. The budget is the government's annual statement of estimated receipts and expenditure, and these three functions are why it matters beyond the accounts. "
  "For stabilisation, the government raises spending or cuts taxes when demand is too low, and does the reverse when demand is so high that it causes inflation.",
  "तीनों कथन सही हैं। बजट सरकार की अनुमानित प्राप्तियों और व्यय का वार्षिक विवरण है, और ये तीन कार्य ही बताते हैं कि यह हिसाब-किताब से आगे क्यों महत्त्वपूर्ण है। "
  "स्थिरीकरण के लिए सरकार माँग बहुत कम होने पर व्यय बढ़ाती या कर घटाती है, और माँग इतनी अधिक होने पर कि मुद्रास्फीति हो, इसका उल्टा करती है।",
  f"{MAC} (Government Budget and the Economy).",
  "l1-eco-budget-objectives", craft="recall")

# ---------------------------------------------------------------- medium MCQ (1)
M(BD, "medium", "A Gender Budget Statement, showing allocations for schemes meant wholly or partly for women, was first presented with the Union Budget of",
  "महिलाओं के लिए पूर्णतः या आंशिक रूप से बनी योजनाओं के आवंटन दिखाने वाला जेंडर बजट विवरण पहली बार किस वर्ष के केंद्रीय बजट के साथ प्रस्तुत किया गया?",
  ["2005-06", "1991-92", "2014-15", "2000-01"],
  ["2005-06", "1991-92", "2014-15", "2000-01"],
  0,
  "The Gender Budget Statement has been part of the Union Budget documents since 2005-06; its Part A lists schemes in which the entire allocation is for women, and Part B those in which a substantial part is. "
  "Gender budgeting does not mean a separate budget for women: it examines the whole budget to see how spending and revenue measures affect women and men differently.",
  "जेंडर बजट विवरण 2005-06 से केंद्रीय बजट दस्तावेज़ों का भाग है; इसका भाग क उन योजनाओं की सूची देता है जिनका पूरा आवंटन महिलाओं के लिए है, और भाग ख उनकी जिनका बड़ा भाग महिलाओं के लिए है। "
  "जेंडर बजटिंग का अर्थ महिलाओं के लिए अलग बजट नहीं है: यह पूरे बजट को यह देखने के लिए जाँचता है कि व्यय और राजस्व के उपाय महिलाओं और पुरुषों को अलग-अलग कैसे प्रभावित करते हैं।",
  "Ministry of Finance (Union Budget, Statement 13: Gender Budget); Ministry of Women and Child Development.",
  "l1-eco-gender-budget-2005", pos=0, craft="recall")

# ---------------------------------------------------------------- medium statement (2)
S(BD, "medium", "Consider the following statements about public goods:",
  "सार्वजनिक वस्तुओं के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["They are non-rivalrous: one person's use does not reduce the amount available to others.",
   "They are non-excludable: there is no feasible way of keeping anyone from enjoying their benefits.",
   "Because everyone benefits from them, private firms find it easy to collect payment for pure public goods."],
  ["वे ग़ैर-प्रतिद्वंद्वी हैं: एक व्यक्ति का उपयोग दूसरों के लिए उपलब्ध मात्रा नहीं घटाता।",
   "वे ग़ैर-अपवर्जनीय हैं: किसी को उनके लाभ से वंचित रखने का कोई व्यावहारिक तरीक़ा नहीं है।",
   "चूँकि सभी को उनसे लाभ होता है, निजी फ़र्मों के लिए शुद्ध सार्वजनिक वस्तुओं का भुगतान वसूलना आसान होता है।"],
  C3, 1,
  "Statements 1 and 2 are correct: national defence, roads, government administration and street lighting benefit everyone together, unlike private goods such as clothes or cars, which go only to those who pay. "
  "Statement 3 is wrong: since no one can be excluded, people have little reason to pay voluntarily -- the free-rider problem -- so private firms cannot easily collect payment, and the government provides such goods out of taxes.",
  "कथन 1 और 2 सही हैं: राष्ट्रीय रक्षा, सड़कें, सरकारी प्रशासन और सड़कों की रोशनी सबको एक साथ लाभ देते हैं, जबकि कपड़े या कारें जैसी निजी वस्तुएँ केवल भुगतान करने वालों को मिलती हैं। "
  "कथन 3 गलत है: चूँकि किसी को वंचित नहीं किया जा सकता, लोगों के पास स्वेच्छा से भुगतान का बहुत कम कारण होता है -- मुफ़्तख़ोर (free-rider) समस्या -- इसलिए निजी फ़र्में आसानी से भुगतान नहीं वसूल सकतीं, और सरकार ऐसी वस्तुएँ करों से उपलब्ध कराती है।",
  f"{MAC} (Government Budget and the Economy).",
  "l1-eco-public-goods-free-rider", craft="inference")

S(BD, "medium", "Consider the following statements about the debate on public debt:",
  "सार्वजनिक ऋण पर बहस के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["One view holds that government borrowing passes a burden to future generations, who must pay higher taxes to repay the debt.",
   "If the debt is held by a country's own citizens, interest payments on it are a transfer from taxpayers to bondholders within the economy."],
  ["एक मत यह है कि सरकारी उधार भावी पीढ़ियों पर बोझ डालता है, जिन्हें ऋण चुकाने के लिए अधिक कर देने होंगे।",
   "यदि ऋण किसी देश के अपने नागरिकों के पास हो, तो उस पर ब्याज भुगतान अर्थव्यवस्था के भीतर करदाताओं से बॉन्डधारकों को अंतरण है।"],
  T2, 2,
  "Both statements are correct, and NCERT presents them as the two sides of the debate. Because internally held debt is in a sense owed by the nation to itself, some argue it is less of a burden than it seems; "
  "but servicing it still needs taxes, which can discourage work and investment, and what matters most is whether the borrowed money is used for productive investment that raises future income.",
  "दोनों कथन सही हैं, और NCERT इन्हें बहस के दो पक्षों के रूप में प्रस्तुत करता है। चूँकि आंतरिक रूप से धारित ऋण एक तरह से राष्ट्र का स्वयं के प्रति ऋण है, कुछ का तर्क है कि यह उतना बोझ नहीं जितना दिखता है; "
  "पर इसकी सेवा के लिए फिर भी कर चाहिए, जो काम और निवेश को हतोत्साहित कर सकते हैं, और सबसे महत्त्वपूर्ण यह है कि उधार लिया धन भावी आय बढ़ाने वाले उत्पादक निवेश में लगता है या नहीं।",
  f"{MAC} (Government Budget and the Economy).",
  "l1-eco-public-debt-burden-debate", craft="linkage")

# ---------------------------------------------------------------- medium Statement-I/II (1)
A(BD, "medium",
  "A rise in government spending financed by an equal rise in lump-sum taxes still raises national income.",
  "एकमुश्त करों में समान वृद्धि से वित्तपोषित सरकारी व्यय में वृद्धि भी राष्ट्रीय आय बढ़ाती है।",
  "The balanced budget multiplier is equal to one.",
  "संतुलित बजट गुणक एक के बराबर होता है।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I. Extra government spending raises income by the full multiplier, while the equal tax reduces consumption only by the marginal propensity to consume times the tax, so its contractionary effect is smaller; "
  "the two together raise income by exactly the amount of the extra spending -- a multiplier of one.",
  "दोनों कथन सही हैं, और कथन-II कथन-I की व्याख्या करता है। अतिरिक्त सरकारी व्यय आय को पूरे गुणक से बढ़ाता है, जबकि बराबर का कर उपभोग को केवल सीमांत उपभोग प्रवृत्ति गुणा कर जितना घटाता है, इसलिए उसका संकुचनकारी प्रभाव छोटा है; "
  "दोनों मिलकर आय को ठीक अतिरिक्त व्यय की राशि जितना बढ़ाते हैं -- एक का गुणक।",
  f"{MAC} (Government Budget and the Economy).",
  "l1-eco-balanced-budget-multiplier", craft="inference")

# ---------------------------------------------------------------- hard statement (1)
S(BD, "hard", "In a simple economy, the marginal propensity to consume is 0.75. Consider the following statements:",
  "एक सरल अर्थव्यवस्था में सीमांत उपभोग प्रवृत्ति 0.75 है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The government expenditure multiplier is 4.",
   "A cut in lump-sum taxes of ₹100 crore raises equilibrium income by ₹300 crore.",
   "If the marginal propensity to consume rises to 0.8, the government expenditure multiplier falls to 3."],
  ["सरकारी व्यय गुणक 4 है।",
   "एकमुश्त करों में ₹100 करोड़ की कटौती संतुलन आय को ₹300 करोड़ बढ़ाती है।",
   "यदि सीमांत उपभोग प्रवृत्ति बढ़कर 0.8 हो जाए, तो सरकारी व्यय गुणक घटकर 3 हो जाता है।"],
  C3, 1,
  "Statements 1 and 2 are correct: the expenditure multiplier is 1/(1 - MPC) = 1/0.25 = 4, and the tax multiplier is MPC/(1 - MPC) = 0.75/0.25 = 3 in absolute value, since a tax cut first raises disposable income and only the part spent starts the multiplier process -- so ₹100 crore of tax cut adds ₹300 crore. "
  "Statement 3 is wrong: a higher MPC means more of each round of income is spent, so the multiplier rises -- to 1/0.2 = 5.",
  "कथन 1 और 2 सही हैं: व्यय गुणक 1/(1 - MPC) = 1/0.25 = 4 है, और कर गुणक निरपेक्ष मान में MPC/(1 - MPC) = 0.75/0.25 = 3 है, क्योंकि कर कटौती पहले प्रयोज्य आय बढ़ाती है और केवल व्यय किया गया भाग गुणक प्रक्रिया शुरू करता है -- इसलिए ₹100 करोड़ की कर कटौती ₹300 करोड़ जोड़ती है। "
  "कथन 3 गलत है: ऊँची MPC का अर्थ है आय के हर दौर का अधिक भाग व्यय होना, इसलिए गुणक बढ़ता है -- 1/0.2 = 5 तक।",
  f"{MAC} (Determination of Income and Employment; Government Budget and the Economy).",
  "l1-eco-fiscal-multipliers-mpc", craft="application")

write("eco_l1_t5_e.sql")
