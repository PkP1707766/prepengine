# -*- coding: utf-8 -*-
"""Level 4 · Simulator 3 (GS Paper I full mock, Layout C: the 2026 shape) -- part E: Economy (19)
(upsc_l4_gs_cell_targets.mjs 3).
Layout C puts four List-I/List-II items in Economy. Every tested proposition was swept against the whole UPSC bank and no
row tests it: RKVY, Per Drop More Crop, Paramparagat Krishi Vikas Yojana and the National Livestock Mission; Operation
Barga; the Treasury Single Account, the MTEF Statement, debt switches and buybacks; TRIMs, the Special Safeguard Mechanism, duty drawback and
interest equalisation; the 1991 gold pledge; covered bonds, interest rate futures, corporate bond repo and angel funds;
debenture trustees; NIIF and sovereign wealth funds; the end of LIBOR and SOFR; ASM and GSM; the Gandhian, People's,
Sarvodaya and rolling plans; IHDI and GII; the MRTP Act's repeal; technical textiles; the ACC battery PLI and wind
repowering; NAIRU and the Big Mac index; EASE; DRTs, SARFAESI's farm-land exclusion and wilful defaulters;
reverse charge, e-way bills and the Direct Taxes Code. MCQ keys are pinned (pos)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, write
from polity_common import T2
from ca_common import combo, MX
from bilingual import combo_hi

d.SUBJECT = "Economy"
d.REQUIRE_CRAFT = True

def SC(topic, diff, body, body_hi, st, st_hi, truth, pos, expl, expl_hi, cite, cg, craft):
    opts = combo(truth, pos)
    S(topic, diff, body, body_hi, st, st_hi, None, pos, expl, expl_hi, cite, cg, opts=opts, opts_hi=[combo_hi(o) for o in opts], craft=craft)

# ---------------------------------------------------------------- Agriculture & Food Economy (List-I/List-II, hard)
MX("Agriculture & Food Economy", "hard", "Match List-I (scheme) with List-II (its main focus):",
   "सूची-I (योजना) को सूची-II (उसका मुख्य केंद्र) से सुमेलित कीजिए:",
   ["Rashtriya Krishi Vikas Yojana", "Per Drop More Crop", "Paramparagat Krishi Vikas Yojana", "National Livestock Mission"],
   ["राष्ट्रीय कृषि विकास योजना", "प्रति बूँद अधिक फ़सल", "परंपरागत कृषि विकास योजना", "राष्ट्रीय पशुधन मिशन"],
   ["Cluster-based organic farming with group certification",
    "Flexible funds for agriculture projects chosen by the States",
    "Entrepreneurship in poultry, small ruminants and fodder",
    "Drip and sprinkler irrigation"],
   ["समूह प्रमाणन के साथ क्लस्टर-आधारित जैविक खेती",
    "राज्यों द्वारा चुनी गई कृषि परियोजनाओं के लिए लचीली निधि",
    "मुर्गीपालन, छोटे जुगाली करने वाले पशुओं और चारे में उद्यमिता",
    "ड्रिप और स्प्रिंकलर सिंचाई"],
   [2, 4, 1, 3], 1,
   "The correct code is A-2, B-4, C-1, D-3. The Rashtriya Krishi Vikas Yojana (2007), later RKVY-RAFTAAR, gives States untied funds to plan and fund agriculture and allied projects according to their own priorities, in keeping with agriculture being a State subject. Per Drop More Crop, the micro-irrigation component of the Pradhan Mantri Krishi Sinchayee Yojana, subsidises drip and sprinkler systems that save water and fertiliser. "
   "The Paramparagat Krishi Vikas Yojana (2015) promotes organic farming in clusters of farmers, certified through the Participatory Guarantee System rather than costly third-party certification. The National Livestock Mission, revamped in 2021, supports entrepreneurship and breed improvement in poultry, sheep, goats and pigs, and the development of feed and fodder -- livestock now produces a larger share of agricultural output than crops in many States.",
   "सही कूट क-2, ख-4, ग-1, घ-3 है। राष्ट्रीय कृषि विकास योजना (2007), बाद में आरकेवीवाई-रफ़्तार, राज्यों को अपनी प्राथमिकताओं के अनुसार कृषि और संबद्ध परियोजनाओं की योजना बनाने और उन्हें धन देने के लिए बिना शर्त निधि देती है, क्योंकि कृषि राज्य का विषय है। प्रति बूँद अधिक फ़सल, प्रधानमंत्री कृषि सिंचाई योजना का सूक्ष्म सिंचाई घटक, ड्रिप और स्प्रिंकलर प्रणालियों पर अनुदान देता है जो जल और उर्वरक बचाती हैं। "
   "परंपरागत कृषि विकास योजना (2015) किसानों के क्लस्टरों में जैविक खेती को बढ़ावा देती है, जिनका प्रमाणन महँगे तृतीय-पक्ष प्रमाणन के बजाय सहभागी गारंटी प्रणाली से होता है। 2021 में पुनर्गठित राष्ट्रीय पशुधन मिशन मुर्गीपालन, भेड़, बकरी और सूअर पालन में उद्यमिता और नस्ल सुधार, तथा पशु आहार और चारे के विकास में सहायता देता है -- अनेक राज्यों में पशुधन अब फ़सलों से बड़ा कृषि उत्पादन देता है।",
   "Ministry of Agriculture and Farmers Welfare (RKVY, PMKSY-Per Drop More Crop, PKVY); Department of Animal Husbandry and Dairying (National Livestock Mission).",
   "l4-s03-eco-rkvy-pdmc-pkvy-nlm", "recall")

# ---------------------------------------------------------------- Agriculture & Food Economy (MCQ, hard)
M("Agriculture & Food Economy", "hard", "'Operation Barga', launched in West Bengal in 1978, sought mainly to",
  "1978 में पश्चिम बंगाल में आरंभ 'ऑपरेशन बर्गा' का मुख्य उद्देश्य था",
  ["record the names of sharecroppers so that they gained secure, heritable tenancy",
   "distribute surplus land taken under ceiling laws among landless labourers",
   "consolidate scattered holdings into compact blocks for each cultivating family",
   "set up co-operative farms on which the members would pool their land and labour"],
  ["बटाईदारों के नाम दर्ज करना ताकि उन्हें सुरक्षित, वंशानुगत काश्तकारी मिले",
   "सीलिंग क़ानूनों के अंतर्गत ली गई अधिशेष भूमि भूमिहीन मज़दूरों में बाँटना",
   "हर काश्तकार परिवार के बिखरे खेतों को सघन खंडों में चकबंदी करना",
   "ऐसे सहकारी फ़ार्म बनाना जिन पर सदस्य अपनी भूमि और श्रम मिलाएँ"],
  0,
  "Sharecroppers (bargadars) in Bengal had legal rights on paper but could be evicted at will, so few dared to claim them. Operation Barga, run by the Left Front government from 1978 with camps held in the villages, recorded the names of bargadars in the land records, which gave them heritable tenancy and a legal right to their share -- three-quarters of the crop where the owner supplied no inputs. Within a few years well over a million sharecroppers were recorded. "
  "Studies have linked it with higher farm productivity in the State, since secure tenants had more reason to invest. It was a tenancy reform, distinct from the redistribution of ceiling-surplus land, the consolidation of holdings or co-operative farming named in the other options.",
  "बंगाल में बटाईदारों (बर्गादारों) के अधिकार काग़ज़ पर थे, पर उन्हें मनमाने ढंग से बेदख़ल किया जा सकता था, इसलिए कम ही उनका दावा करने का साहस करते थे। 1978 से वाम मोर्चा सरकार द्वारा गाँवों में शिविर लगाकर चलाए गए ऑपरेशन बर्गा ने भूमि अभिलेखों में बर्गादारों के नाम दर्ज किए, जिससे उन्हें वंशानुगत काश्तकारी और अपने हिस्से का विधिक अधिकार मिला -- जहाँ मालिक कोई आदान न दे वहाँ फ़सल का तीन-चौथाई। कुछ ही वर्षों में दस लाख से कहीं अधिक बटाईदार दर्ज हुए। "
  "अध्ययनों ने इसे राज्य में खेती की अधिक उत्पादकता से जोड़ा है, क्योंकि सुरक्षित काश्तकारों के पास निवेश का अधिक कारण था। यह काश्तकारी सुधार था, जो अन्य विकल्पों में बताए सीलिंग-अधिशेष भूमि के पुनर्वितरण, चकबंदी या सहकारी खेती से अलग है।",
  "Government of West Bengal, Land and Land Reforms Department; Planning Commission, reports on land reforms.",
  "l4-s03-eco-operation-barga-bargadars-1978", pos=3, craft="precision")

# ---------------------------------------------------------------- Budget, Deficits & Public Debt (List-I/List-II, hard)
MX("Budget, Deficits & Public Debt", "hard", "Match List-I (tool of public finance) with List-II (what it is):",
   "सूची-I (लोक वित्त का साधन) को सूची-II (वह क्या है) से सुमेलित कीजिए:",
   ["Treasury Single Account", "Medium-Term Expenditure Framework Statement", "Debt switch", "Buyback of government securities"],
   ["ट्रेज़री एकल खाता", "मध्यम-अवधि व्यय ढाँचा विवरण", "ऋण अदला-बदली (डेट स्विच)", "सरकारी प्रतिभूतियों की पुनर्ख़रीद"],
   ["Exchanging securities that mature soon for longer-dated ones, to smooth future repayments",
    "Funds of autonomous bodies kept in the government's account with the RBI until they are actually spent",
    "Repurchasing securities before they mature, using surplus cash, to reduce outstanding debt",
    "Three-year rolling targets for expenditure indicators, laid before Parliament under the FRBM Act"],
   ["शीघ्र परिपक्व होने वाली प्रतिभूतियों को लंबी अवधि वाली प्रतिभूतियों से बदलना, ताकि भावी पुनर्भुगतान सुचारु हों",
    "स्वायत्त निकायों की निधि जो वास्तव में ख़र्च होने तक आरबीआई में सरकार के खाते में रखी जाती है",
    "अधिशेष नक़दी से प्रतिभूतियों को परिपक्वता से पहले वापस ख़रीदना, ताकि बकाया ऋण घटे",
    "व्यय संकेतकों के तीन-वर्षीय अनवरत लक्ष्य, जो एफ़आरबीएम अधिनियम के अंतर्गत संसद के समक्ष रखे जाते हैं"],
   [2, 4, 1, 3], 2,
   "The correct code is A-2, B-4, C-1, D-3. Under the Treasury Single Account system, brought in for autonomous bodies from 2021-22, grants are not parked in their bank accounts; the money stays in the government's account with the RBI and is released just in time, which cuts the Union's borrowing and interest costs. The Medium-Term Expenditure Framework Statement, required by the 2012 amendment of the FRBM Act and presented after the Budget, sets three-year rolling targets for expenditure, linking each year's Budget to a medium-term path. "
   "In a debt switch, carried out through the RBI, the government exchanges securities falling due in the next few years for longer ones, so that large repayments do not bunch up in a single year. A buyback, done when the government has surplus cash, retires securities early and so reduces both the debt outstanding and the pressure of future redemptions. These tools of debt management sit alongside the deficit targets that the FRBM framework sets.",
   "सही कूट क-2, ख-4, ग-1, घ-3 है। स्वायत्त निकायों के लिए 2021-22 से लाई गई ट्रेज़री एकल खाता प्रणाली में अनुदान उनके बैंक खातों में नहीं रखे जाते; धन आरबीआई में सरकार के खाते में रहता है और ठीक समय पर जारी होता है, जिससे संघ का उधार और ब्याज व्यय घटता है। एफ़आरबीएम अधिनियम के 2012 के संशोधन द्वारा अपेक्षित और बजट के बाद प्रस्तुत मध्यम-अवधि व्यय ढाँचा विवरण व्यय के तीन-वर्षीय अनवरत लक्ष्य तय करता है, और हर वर्ष के बजट को एक मध्यम-अवधि मार्ग से जोड़ता है। "
   "ऋण अदला-बदली में, जो आरबीआई के माध्यम से होती है, सरकार अगले कुछ वर्षों में देय प्रतिभूतियों को लंबी अवधि वाली प्रतिभूतियों से बदलती है, ताकि बड़े पुनर्भुगतान किसी एक वर्ष में इकट्ठे न हों। पुनर्ख़रीद, जो सरकार के पास अधिशेष नक़दी होने पर की जाती है, प्रतिभूतियों को जल्दी चुका देती है और इस प्रकार बकाया ऋण और भावी मोचन का दबाव दोनों घटाती है। ऋण प्रबंधन के ये साधन एफ़आरबीएम ढाँचे द्वारा तय घाटा लक्ष्यों के साथ चलते हैं।",
   "Ministry of Finance, Department of Expenditure (Treasury Single Account) and Medium-Term Expenditure Framework Statement; Fiscal Responsibility and Budget Management Act, 2003 (as amended in 2012); Reserve Bank of India, press releases on switch and buyback auctions of government securities.",
   "l4-s03-eco-tsa-mtef-debt-switch-buyback", "precision")

# ---------------------------------------------------------------- External Sector & International Institutions (List-I/List-II, hard)
MX("External Sector & International Institutions", "hard", "Match List-I (trade rule or instrument) with List-II (what it is):",
   "सूची-I (व्यापार नियम या साधन) को सूची-II (वह क्या है) से सुमेलित कीजिए:",
   ["TRIMs Agreement", "Special Safeguard Mechanism", "Duty drawback", "Interest Equalisation Scheme"],
   ["ट्रिम्स समझौता", "विशेष रक्षोपाय तंत्र", "शुल्क वापसी (ड्यूटी ड्रॉबैक)", "ब्याज समकरण योजना"],
   ["A refund of duties paid on inputs used in exported goods",
    "WTO rules against investment conditions that distort trade in goods, such as local-content requirements",
    "A subsidy that lowers the interest cost of rupee export credit",
    "A tool that developing countries seek at the WTO to raise farm tariffs during import surges"],
   ["निर्यात की गई वस्तुओं में प्रयुक्त आदानों पर दिए गए शुल्कों की वापसी",
    "वस्तु व्यापार को विकृत करने वाली निवेश शर्तों, जैसे स्थानीय-सामग्री अपेक्षाओं, के विरुद्ध डब्ल्यूटीओ के नियम",
    "रुपये में निर्यात ऋण की ब्याज लागत घटाने वाला अनुदान",
    "आयात में अचानक वृद्धि के समय कृषि शुल्क बढ़ाने के लिए विकासशील देशों द्वारा डब्ल्यूटीओ में माँगा जाने वाला साधन"],
   [2, 4, 1, 3], 0,
   "The correct code is A-2, B-4, C-1, D-3. The Agreement on Trade-Related Investment Measures bars conditions on investors that discriminate against imports or restrict exports, such as requiring a minimum share of local inputs or balancing imports with exports. The Special Safeguard Mechanism, long sought by India and the G33 in the agriculture negotiations, would let developing countries raise tariffs temporarily when imports surge or prices crash; it has not been agreed. "
   "Duty drawback refunds customs and excise duties paid on inputs used in exports, on the principle that taxes should not be exported. The Interest Equalisation Scheme gave exporters, especially MSMEs, a subvention on pre- and post-shipment rupee credit, so that Indian exporters could borrow nearer the rates their competitors paid.",
   "सही कूट क-2, ख-4, ग-1, घ-3 है। व्यापार-संबंधी निवेश उपायों पर समझौता निवेशकों पर ऐसी शर्तों पर रोक लगाता है जो आयात के साथ भेदभाव करें या निर्यात सीमित करें, जैसे स्थानीय आदानों का न्यूनतम अंश अपेक्षित करना या आयात को निर्यात से संतुलित करना। कृषि वार्ताओं में भारत और जी33 द्वारा लंबे समय से माँगा गया विशेष रक्षोपाय तंत्र विकासशील देशों को आयात में अचानक वृद्धि या कीमतों में गिरावट पर अस्थायी रूप से शुल्क बढ़ाने देगा; इस पर सहमति नहीं हुई है। "
   "शुल्क वापसी निर्यात में प्रयुक्त आदानों पर चुकाए गए सीमा और उत्पाद शुल्क लौटाती है, इस सिद्धांत पर कि करों का निर्यात नहीं होना चाहिए। ब्याज समकरण योजना ने निर्यातकों, विशेषकर एमएसएमई, को लदान-पूर्व और लदान-पश्चात रुपया ऋण पर अनुदान दिया, ताकि भारतीय निर्यातक अपने प्रतिस्पर्धियों की दरों के निकट उधार ले सकें।",
   "WTO, Agreement on Trade-Related Investment Measures and Agreement on Agriculture negotiations; Central Board of Indirect Taxes and Customs (duty drawback); Reserve Bank of India and DGFT (Interest Equalisation Scheme).",
   "l4-s03-eco-trims-ssm-duty-drawback-interest-equalisation", "precision")

# ---------------------------------------------------------------- External Sector & International Institutions (MCQ, hard)
M("External Sector & International Institutions", "hard", "To deal with the balance-of-payments crisis of 1991, the Government of India and the RBI",
  "1991 के भुगतान संतुलन संकट से निपटने के लिए भारत सरकार और आरबीआई ने",
  ["pledged gold with the Bank of England and the Bank of Japan to raise loans",
   "defaulted on external debt payments for a year and rescheduled them later",
   "sold all of India's gold reserves to the IMF in return for a standby credit",
   "fixed the rupee permanently to the US dollar under a currency board system"],
  ["ऋण जुटाने के लिए बैंक ऑफ़ इंग्लैंड और बैंक ऑफ़ जापान के पास सोना गिरवी रखा",
   "एक वर्ष तक बाहरी ऋण भुगतानों में चूक की और बाद में उनका पुनर्निर्धारण किया",
   "स्टैंडबाय ऋण के बदले भारत के सारे स्वर्ण भंडार आईएमएफ़ को बेच दिए",
   "मुद्रा बोर्ड व्यवस्था के अंतर्गत रुपये को स्थायी रूप से अमेरिकी डॉलर से जोड़ दिया"],
  0,
  "By mid-1991 India's foreign exchange reserves had fallen to little more than two weeks of imports, after the Gulf War oil shock, falling remittances and the flight of non-resident deposits. To avoid defaulting -- which India never did -- the Government first leased gold through the State Bank of India, and in July 1991 the RBI pledged about 47 tonnes of gold with the Bank of England and the Bank of Japan to raise loans; the gold was later redeemed. "
  "The crisis was met with a devaluation of the rupee in July 1991, IMF support and the start of the reforms that opened the economy. The rupee moved towards a market-determined rate through the Liberalised Exchange Rate Management System of 1992, not a fixed peg.",
  "1991 के मध्य तक खाड़ी युद्ध के तेल झटके, घटते प्रेषण और अनिवासी जमाओं के पलायन के बाद भारत का विदेशी मुद्रा भंडार लगभग दो सप्ताह के आयात तक गिर गया था। चूक से बचने के लिए -- जो भारत ने कभी नहीं की -- सरकार ने पहले भारतीय स्टेट बैंक के माध्यम से सोना पट्टे पर दिया, और जुलाई 1991 में आरबीआई ने ऋण जुटाने के लिए लगभग 47 टन सोना बैंक ऑफ़ इंग्लैंड और बैंक ऑफ़ जापान के पास गिरवी रखा; बाद में सोना छुड़ा लिया गया। "
  "संकट का सामना जुलाई 1991 में रुपये के अवमूल्यन, आईएमएफ़ की सहायता और अर्थव्यवस्था खोलने वाले सुधारों के आरंभ से किया गया। रुपया 1992 की उदारीकृत विनिमय दर प्रबंधन प्रणाली के माध्यम से बाज़ार-निर्धारित दर की ओर बढ़ा, किसी स्थिर जुड़ाव की ओर नहीं।",
  "Reserve Bank of India, History of the Reserve Bank of India (Vol. 4); Ministry of Finance, Economic Survey 1991-92.",
  "l4-s03-eco-1991-gold-pledge-bank-of-england-japan", pos=1, craft="precision")

# ---------------------------------------------------------------- Financial Markets, Instruments & Fintech (List-I/List-II, hard)
MX("Financial Markets, Instruments & Fintech", "hard", "Match List-I (financial instrument or vehicle) with List-II (its description):",
   "सूची-I (वित्तीय साधन या माध्यम) को सूची-II (उसका विवरण) से सुमेलित कीजिए:",
   ["Covered bond", "Interest rate futures", "Repo in corporate bonds", "Angel fund"],
   ["कवर्ड बॉन्ड", "ब्याज दर वायदा", "कॉर्पोरेट बॉन्ड में रेपो", "एंजेल फ़ंड"],
   ["Exchange-traded contracts on the future price of a government bond, used to hedge against changes in interest rates",
    "A kind of Category I alternative investment fund that invests in start-ups",
    "A bond backed by a dedicated pool of assets that stays on the issuer's balance sheet, with a claim on the issuer as well",
    "Short-term borrowing against corporate bonds as collateral, with an agreement to buy them back"],
   ["सरकारी बॉन्ड के भावी मूल्य पर एक्सचेंज में कारोबार वाले अनुबंध, जिनका उपयोग ब्याज दरों में बदलाव से बचाव के लिए होता है",
    "श्रेणी I वैकल्पिक निवेश कोष का एक प्रकार जो स्टार्ट-अप में निवेश करता है",
    "परिसंपत्तियों के एक समर्पित समूह पर आधारित बॉन्ड जो जारीकर्ता के तुलन-पत्र पर ही रहता है, और जारीकर्ता पर भी दावा देता है",
    "कॉर्पोरेट बॉन्डों को संपार्श्विक रखकर अल्पकालिक उधार, उन्हें वापस ख़रीदने के समझौते के साथ"],
   [3, 1, 4, 2], 3,
   "The correct code is A-3, B-1, C-4, D-2. A covered bond gives its holders a double claim -- on the issuer and on a ring-fenced cover pool of assets such as home loans -- which makes it safer and cheaper than unsecured debt; unlike in securitisation, the assets stay on the issuer's books. Interest rate futures, traded on Indian exchanges on government bonds and settled in cash, let banks and others lock in a rate and hedge the fall in bond prices that a rise in rates causes. "
   "The RBI permitted repo in corporate bonds to deepen the corporate debt market, which remains thin compared with bank lending; the lender takes the bonds as collateral for a short period. Angel funds, a sub-category of venture capital funds under SEBI's alternative investment fund rules, pool money from angel investors to back early-stage start-ups.",
   "सही कूट क-3, ख-1, ग-4, घ-2 है। कवर्ड बॉन्ड अपने धारकों को दोहरा दावा देता है -- जारीकर्ता पर और आवास ऋणों जैसी परिसंपत्तियों के अलग रखे गए कवर पूल पर -- जिससे यह असुरक्षित ऋण से अधिक सुरक्षित और सस्ता होता है; प्रतिभूतिकरण के विपरीत, परिसंपत्तियाँ जारीकर्ता के खातों में ही रहती हैं। भारतीय एक्सचेंजों पर सरकारी बॉन्डों पर कारोबार वाले और नक़द में निपटाए जाने वाले ब्याज दर वायदे बैंकों और अन्य को दर तय करने और दरें बढ़ने से बॉन्ड मूल्यों में आने वाली गिरावट से बचाव करने देते हैं। "
   "आरबीआई ने कॉर्पोरेट ऋण बाज़ार को गहरा करने के लिए कॉर्पोरेट बॉन्डों में रेपो की अनुमति दी, जो बैंक ऋण की तुलना में अब भी पतला है; ऋणदाता बॉन्डों को थोड़े समय के लिए संपार्श्विक के रूप में लेता है। सेबी के वैकल्पिक निवेश कोष नियमों के अंतर्गत उद्यम पूँजी कोषों की एक उप-श्रेणी, एंजेल फ़ंड, आरंभिक चरण के स्टार्ट-अप में निवेश के लिए एंजेल निवेशकों का धन एकत्र करते हैं।",
   "Reserve Bank of India, directions on repo in corporate debt securities and on interest rate derivatives; SEBI (Alternative Investment Funds) Regulations, 2012.",
   "l4-s03-eco-covered-bond-irf-corporate-repo-angel-fund", "precision")

# ---------------------------------------------------------------- Financial Markets, Instruments & Fintech (MCQ, medium)
M("Financial Markets, Instruments & Fintech", "medium",
  "In an issue of secured debentures, the entity appointed to protect the interests of the debenture holders and to enforce the security if the issuer defaults is the",
  "सुरक्षित डिबेंचरों के निर्गम में, डिबेंचर धारकों के हितों की रक्षा करने और जारीकर्ता के चूक करने पर प्रतिभूति लागू करने के लिए नियुक्त इकाई है",
  ["debenture trustee", "credit rating agency", "registrar to the issue", "lead merchant banker"],
  ["डिबेंचर न्यासी", "साख निर्धारण एजेंसी", "निर्गम का रजिस्ट्रार", "मुख्य मर्चेंट बैंकर"],
  0,
  "A debenture trustee, which must be registered with SEBI and is usually a bank, an insurer or a specialised trustee company, holds the security created for the debentures on behalf of their holders. It checks that the assets charged are adequate, monitors the issuer's compliance with the terms, and, if the issuer defaults, calls meetings of holders and acts to enforce the security, including through insolvency proceedings. "
  "A credit rating agency only grades the debt; the registrar handles applications, allotment and records; and the merchant banker manages the issue. The trustee's role grew after defaults on corporate debt, when SEBI tightened rules on how trustees must act for investors.",
  "सेबी में पंजीकृत होना आवश्यक, और प्रायः कोई बैंक, बीमाकर्ता या विशेष न्यासी कंपनी, डिबेंचर न्यासी डिबेंचरों के लिए बनाई गई प्रतिभूति उनके धारकों की ओर से रखता है। यह जाँचता है कि गिरवी परिसंपत्तियाँ पर्याप्त हैं, शर्तों के पालन पर नज़र रखता है, और जारीकर्ता के चूक करने पर धारकों की बैठकें बुलाकर प्रतिभूति लागू करने के लिए कार्य करता है, दिवाला कार्यवाहियों सहित। "
  "साख निर्धारण एजेंसी केवल ऋण की श्रेणी तय करती है; रजिस्ट्रार आवेदन, आबंटन और अभिलेख सँभालता है; और मर्चेंट बैंकर निर्गम का प्रबंधन करता है। कॉर्पोरेट ऋण पर चूकों के बाद न्यासी की भूमिका बढ़ी, जब सेबी ने कड़े किए कि न्यासियों को निवेशकों के लिए कैसे कार्य करना है।",
  "SEBI (Debenture Trustees) Regulations, 1993; Companies Act, 2013, section 71.",
  "l4-s03-eco-debenture-trustee-sebi-enforce-security", pos=2, craft="application")

# ---------------------------------------------------------------- Financial Markets, Instruments & Fintech (statement, hard)
SC("Financial Markets, Instruments & Fintech", "hard", "With reference to the National Investment and Infrastructure Fund (NIIF) and sovereign wealth funds, consider the following statements:",
   "राष्ट्रीय निवेश और अवसंरचना कोष (एनआईआईएफ़) और सॉवरेन वेल्थ फ़ंड के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
   ["The Government of India holds 49 per cent of the NIIF, the rest coming from domestic and international investors.",
    "Its investors include sovereign wealth funds such as the Abu Dhabi Investment Authority.",
    "The NIIF is a statutory body created by an Act of Parliament.",
    "Sovereign wealth funds invest a country's surplus wealth, often earned from commodity exports, as Norway's oil fund does."],
   ["एनआईआईएफ़ में भारत सरकार का 49 प्रतिशत अंश है, और शेष घरेलू तथा अंतरराष्ट्रीय निवेशकों से आता है।",
    "इसके निवेशकों में अबू धाबी इन्वेस्टमेंट अथॉरिटी जैसे सॉवरेन वेल्थ फ़ंड शामिल हैं।",
    "एनआईआईएफ़ संसद के एक अधिनियम द्वारा बनाया गया सांविधिक निकाय है।",
    "सॉवरेन वेल्थ फ़ंड किसी देश की अधिशेष संपत्ति का निवेश करते हैं, जो प्रायः वस्तु निर्यात से अर्जित होती है, जैसा नॉर्वे का तेल कोष करता है।"],
   (1, 1, 0, 1), 1,
   "Statements 1, 2 and 4 are correct. Set up in 2015, the NIIF is a collaborative investment platform for infrastructure and other long-term assets: the Government holds 49 per cent, so that it is not a government company, and partners such as the Abu Dhabi Investment Authority, Temasek and multilateral banks bring in long-term capital and co-invest alongside its funds, for example in ports, roads, renewable energy and green infrastructure. "
   "Statement 3 is wrong: the NIIF is not created by statute; its funds are registered with SEBI as Category II alternative investment funds and are run by a professional management company. Sovereign wealth funds, from Norway's pension fund built on oil revenues to the Gulf funds, invest abroad to save windfall income for future generations and to spread risk, which is why they are prized as patient investors in Indian infrastructure.",
   "केवल कथन 1, 2 और 4 सही हैं। 2015 में बना एनआईआईएफ़ अवसंरचना और अन्य दीर्घकालिक परिसंपत्तियों के लिए एक सहयोगी निवेश मंच है: सरकार के पास 49 प्रतिशत अंश है, ताकि यह सरकारी कंपनी न हो, और अबू धाबी इन्वेस्टमेंट अथॉरिटी, टेमासेक और बहुपक्षीय बैंकों जैसे साझेदार दीर्घकालिक पूँजी लाते हैं और इसके कोषों के साथ सह-निवेश करते हैं, उदाहरण के लिए बंदरगाहों, सड़कों, नवीकरणीय ऊर्जा और हरित अवसंरचना में। "
   "कथन 3 ग़लत है: एनआईआईएफ़ किसी क़ानून से नहीं बना; इसके कोष सेबी में श्रेणी II वैकल्पिक निवेश कोष के रूप में पंजीकृत हैं और एक पेशेवर प्रबंधन कंपनी द्वारा चलाए जाते हैं। तेल राजस्व पर बने नॉर्वे के पेंशन कोष से खाड़ी के कोषों तक, सॉवरेन वेल्थ फ़ंड अप्रत्याशित आय को भावी पीढ़ियों के लिए बचाने और जोखिम फैलाने के लिए विदेश में निवेश करते हैं, इसी कारण उन्हें भारतीय अवसंरचना में धैर्यवान निवेशकों के रूप में महत्त्व दिया जाता है।",
   "Ministry of Finance, Department of Economic Affairs (NIIF); National Investment and Infrastructure Fund Limited, annual reports.",
   "l4-s03-eco-niif-49-per-cent-adia-not-statutory-swf", "precision")

# ---------------------------------------------------------------- Financial Markets, Instruments & Fintech (statement, medium)
SC("Financial Markets, Instruments & Fintech", "medium", "With reference to interest rate benchmarks, consider the following statements:",
   "ब्याज दर बेंचमार्क के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
   ["LIBOR was phased out after cases of manipulation, and its main US dollar rates stopped being published in 2023.",
    "The Secured Overnight Financing Rate (SOFR) is based on overnight repo transactions backed by US Treasury securities.",
    "SOFR is set from a panel of banks' estimates of what they would pay to borrow."],
   ["हेरफेर के मामलों के बाद लाइबोर को समाप्त किया गया, और इसकी मुख्य अमेरिकी डॉलर दरों का प्रकाशन 2023 में बंद हो गया।",
    "सिक्योर्ड ओवरनाइट फ़ाइनेंसिंग रेट (एसओएफ़आर) अमेरिकी ट्रेज़री प्रतिभूतियों पर आधारित रातोंरात रेपो लेनदेनों पर आधारित है।",
    "एसओएफ़आर बैंकों के एक पैनल के उन अनुमानों से तय होता है कि उन्हें उधार लेने पर कितना देना होगा।"],
   (1, 1, 0), 3,
   "Only statements 1 and 2 are correct. The London Interbank Offered Rate was set each day from banks' submissions of what they thought they would pay to borrow, and after banks were found to have rigged it, regulators decided to replace it; the last main US dollar LIBOR settings were published in June 2023. SOFR, published by the Federal Reserve Bank of New York, is calculated from a very large volume of actual overnight repo trades secured by Treasuries, so it is hard to manipulate. "
   "Statement 3 is wrong: that panel-estimate method was exactly LIBOR's weakness. Indian banks and companies with foreign-currency loans and derivatives had to move their contracts to alternative rates, and in India the RBI has also been reviewing how the domestic overnight benchmark should be built from actual trades.",
   "केवल कथन 1 और 2 सही हैं। लंदन इंटरबैंक ऑफ़र्ड रेट हर दिन बैंकों के इस अनुमान से तय होता था कि उन्हें उधार लेने पर कितना देना होगा, और बैंकों द्वारा इसमें हेरफेर पाए जाने के बाद नियामकों ने इसे बदलने का निर्णय लिया; मुख्य अमेरिकी डॉलर लाइबोर की अंतिम दरें जून 2023 में प्रकाशित हुईं। फ़ेडरल रिज़र्व बैंक ऑफ़ न्यूयॉर्क द्वारा प्रकाशित एसओएफ़आर ट्रेज़री से सुरक्षित रातोंरात रेपो सौदों की बहुत बड़ी मात्रा से गणना किया जाता है, इसलिए इसमें हेरफेर कठिन है। "
   "कथन 3 ग़लत है: पैनल-अनुमान की यही पद्धति लाइबोर की कमज़ोरी थी। विदेशी मुद्रा ऋणों और व्युत्पन्नों वाले भारतीय बैंकों और कंपनियों को अपने अनुबंध वैकल्पिक दरों पर ले जाने पड़े, और भारत में आरबीआई भी इस पर विचार करता रहा है कि घरेलू रातोंरात बेंचमार्क को वास्तविक सौदों से कैसे बनाया जाए।",
   "Federal Reserve Bank of New York (SOFR); UK Financial Conduct Authority, LIBOR cessation announcements; Reserve Bank of India, circulars on transition from LIBOR.",
   "l4-s03-eco-libor-end-sofr-repo-based", "precision")

SC("Financial Markets, Instruments & Fintech", "medium", "With reference to surveillance measures in the Indian stock market, consider the following statements:",
   "भारतीय शेयर बाज़ार में निगरानी उपायों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
   ["Stocks placed under the Additional Surveillance Measure framework face steps such as higher margins.",
    "Being placed under the framework means that the company has been found guilty of fraud.",
    "The Graded Surveillance Measure targets securities whose price rise is not in line with the company's financial health."],
   ["अतिरिक्त निगरानी उपाय ढाँचे में रखे गए शेयरों पर अधिक मार्जिन जैसे क़दम लागू होते हैं।",
    "ढाँचे में रखे जाने का अर्थ है कि कंपनी को कपट का दोषी पाया गया है।",
    "श्रेणीबद्ध निगरानी उपाय उन प्रतिभूतियों को लक्ष्य करता है जिनकी कीमत में वृद्धि कंपनी के वित्तीय स्वास्थ्य के अनुरूप नहीं है।"],
   (1, 0, 1), 2,
   "Only statements 1 and 3 are correct. SEBI and the stock exchanges use the Additional Surveillance Measure (ASM) framework to cool down stocks that show unusual price movements, volatility or concentration of trading: such stocks may face higher margins, trading in a separate trade-for-trade segment or price bands, so that speculative excess is checked. The Graded Surveillance Measure (GSM) applies to securities, often of small companies, whose prices rise far out of line with their fundamentals, with stricter stages of restriction. "
   "Statement 2 is wrong: the exchanges state clearly that inclusion is purely a market-surveillance step, based on objective criteria, and is not an adverse comment on the company. The aim is to protect investors from pump-and-dump schemes and sudden collapses.",
   "केवल कथन 1 और 3 सही हैं। सेबी और स्टॉक एक्सचेंज असामान्य मूल्य गतिविधियाँ, अस्थिरता या कारोबार का संकेंद्रण दिखाने वाले शेयरों को ठंडा करने के लिए अतिरिक्त निगरानी उपाय (एएसएम) ढाँचे का उपयोग करते हैं: ऐसे शेयरों पर अधिक मार्जिन, अलग ट्रेड-फ़ॉर-ट्रेड खंड में कारोबार या मूल्य सीमाएँ लग सकती हैं, ताकि सट्टेबाज़ी की अति रुके। श्रेणीबद्ध निगरानी उपाय (जीएसएम) उन प्रतिभूतियों पर, प्रायः छोटी कंपनियों की, लागू होता है जिनकी कीमतें उनके मूल आधारों से बहुत बेमेल बढ़ती हैं, प्रतिबंध के अधिक कड़े चरणों के साथ। "
   "कथन 2 ग़लत है: एक्सचेंज स्पष्ट कहते हैं कि समावेश पूरी तरह वस्तुनिष्ठ मानदंडों पर आधारित बाज़ार-निगरानी का क़दम है, और कंपनी पर कोई प्रतिकूल टिप्पणी नहीं है। उद्देश्य निवेशकों को पंप-एंड-डंप योजनाओं और अचानक गिरावटों से बचाना है।",
   "SEBI and National Stock Exchange / BSE circulars on the Additional Surveillance Measure and Graded Surveillance Measure frameworks.",
   "l4-s03-eco-asm-gsm-surveillance-not-adverse", "precision")

# ---------------------------------------------------------------- Growth, Development, Poverty & Planning (statement, hard)
SC("Growth, Development, Poverty & Planning", "hard", "With reference to plans for India's economic development, consider the following statements:",
   "भारत के आर्थिक विकास की योजनाओं के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
   ["The Gandhian Plan of 1944 was drawn up by Shriman Narayan Agarwal.",
    "The People's Plan of 1945 was prepared by M. N. Roy.",
    "The idea of a 'rolling plan', revised every year, was adopted by the Janata Government for 1978-80.",
    "The Sarvodaya Plan of 1950 was drafted by M. N. Roy."],
   ["1944 की गांधीवादी योजना श्रीमन्नारायण अग्रवाल ने तैयार की।",
    "1945 की जन योजना एम. एन. राय ने तैयार की।",
    "हर वर्ष संशोधित होने वाली 'अनवरत योजना' (रोलिंग प्लान) का विचार जनता सरकार ने 1978-80 के लिए अपनाया।",
    "1950 की सर्वोदय योजना एम. एन. राय ने तैयार की।"],
   (1, 1, 1, 0), 1,
   "Statements 1, 2 and 3 are correct. Before and after independence several groups put forward plans: the Bombay Plan of leading industrialists (1944), the Gandhian Plan of Shriman Narayan Agarwal (1944), built around village industries and decentralisation, and the People's Plan of M. N. Roy's Radical Democratic Party (1945), which gave priority to agriculture and consumer goods. After the Janata Government came to power in 1977, it ended the Fifth Plan a year early and adopted a 'rolling plan' for 1978-80, revised every year, before the Sixth Plan began in 1980. "
   "Statement 4 is wrong: the Sarvodaya Plan of 1950 was drafted by Jayaprakash Narayan, drawing on Gandhian and Vinoba Bhave's ideas, and stressed land reform and small-scale industry. The variety of these plans shows the real debate behind the choice of the Nehru-Mahalanobis strategy of heavy industry.",
   "केवल कथन 1, 2 और 3 सही हैं। स्वतंत्रता से पहले और बाद में कई समूहों ने योजनाएँ रखीं: प्रमुख उद्योगपतियों की बंबई योजना (1944), ग्राम उद्योगों और विकेंद्रीकरण पर आधारित श्रीमन्नारायण अग्रवाल की गांधीवादी योजना (1944), और एम. एन. राय की रेडिकल डेमोक्रेटिक पार्टी की जन योजना (1945), जिसने कृषि और उपभोक्ता वस्तुओं को प्राथमिकता दी। 1977 में सत्ता में आने के बाद जनता सरकार ने पाँचवीं योजना एक वर्ष पहले समाप्त कर दी और 1980 में छठी योजना आरंभ होने से पहले 1978-80 के लिए हर वर्ष संशोधित होने वाली 'अनवरत योजना' अपनाई। "
   "कथन 4 ग़लत है: 1950 की सर्वोदय योजना जयप्रकाश नारायण ने गांधीवादी और विनोबा भावे के विचारों के आधार पर तैयार की, और भूमि सुधार तथा लघु उद्योगों पर बल दिया। इन योजनाओं की विविधता नेहरू-महालनोबिस की भारी उद्योग रणनीति के चुनाव के पीछे की वास्तविक बहस दिखाती है।",
   "Planning Commission, Five Year Plan documents; NCERT, Class XII, Politics in India since Independence, chapter on planned development.",
   "l4-s03-eco-gandhian-peoples-sarvodaya-rolling-plan", "precision")

# ---------------------------------------------------------------- Inclusive Growth, Welfare & Demography (statement, hard)
SC("Inclusive Growth, Welfare & Demography", "hard", "With reference to the indices published by the UNDP, consider the following statements:",
   "यूएनडीपी द्वारा प्रकाशित सूचकांकों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
   ["The Inequality-adjusted Human Development Index discounts each dimension of human development for the inequality in its distribution.",
    "The Gender Inequality Index covers reproductive health, empowerment and participation in the labour market.",
    "A higher value of the Gender Inequality Index means greater equality between women and men."],
   ["असमानता-समायोजित मानव विकास सूचकांक मानव विकास के प्रत्येक आयाम को उसके वितरण में असमानता के अनुसार घटाता है।",
    "लैंगिक असमानता सूचकांक प्रजनन स्वास्थ्य, सशक्तीकरण और श्रम बाज़ार में भागीदारी को समाहित करता है।",
    "लैंगिक असमानता सूचकांक का अधिक मान स्त्रियों और पुरुषों के बीच अधिक समानता का अर्थ है।"],
   (1, 1, 0), 0,
   "Only statements 1 and 2 are correct. The IHDI takes the HDI's three dimensions -- a long and healthy life, knowledge and a decent standard of living -- and lowers each according to how unequally it is shared, so the gap between a country's HDI and IHDI measures the loss from inequality; India's loss is large. The GII combines maternal mortality and adolescent births (reproductive health), women's share of parliamentary seats and secondary education (empowerment), and the gap in labour force participation. "
   "Statement 3 is wrong: the GII measures the loss in human development caused by gender inequality, so a higher value means more inequality; a value of zero would mean women and men fare equally. India's low female labour force participation weighs heavily in its score.",
   "केवल कथन 1 और 2 सही हैं। आईएचडीआई मानव विकास सूचकांक के तीन आयामों -- लंबा और स्वस्थ जीवन, ज्ञान और सभ्य जीवन-स्तर -- को लेता है और प्रत्येक को इस अनुसार घटाता है कि वह कितनी असमानता से बँटा है, इसलिए किसी देश के एचडीआई और आईएचडीआई का अंतर असमानता से हुई हानि मापता है; भारत की हानि बड़ी है। जीआईआई मातृ मृत्यु और किशोरावस्था में जन्म (प्रजनन स्वास्थ्य), संसद की सीटों और माध्यमिक शिक्षा में स्त्रियों का अंश (सशक्तीकरण), और श्रम बल भागीदारी के अंतर को जोड़ता है। "
   "कथन 3 ग़लत है: जीआईआई लैंगिक असमानता से मानव विकास में होने वाली हानि मापता है, इसलिए अधिक मान का अर्थ अधिक असमानता है; शून्य का मान इसका अर्थ होगा कि स्त्रियों और पुरुषों की स्थिति बराबर है। भारत की कम महिला श्रम बल भागीदारी उसके अंक पर भारी पड़ती है।",
   "UNDP, Human Development Report, technical notes on the IHDI and the GII.",
   "l4-s03-eco-ihdi-gii-undp-higher-means-worse", "precision")

# ---------------------------------------------------------------- Industry, Infrastructure, Energy & Services (statement, hard)
SC("Industry, Infrastructure, Energy & Services", "hard", "With reference to competition law in India, consider the following statements:",
   "भारत में प्रतिस्पर्धा विधि के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
   ["The MRTP Commission continues to work alongside the Competition Commission of India.",
    "The Monopolies and Restrictive Trade Practices Act, 1969 aimed mainly to prevent the concentration of economic power.",
    "The Competition Act, 2002 replaced it, shifting the focus from the size of firms to anti-competitive conduct."],
   ["एमआरटीपी आयोग भारतीय प्रतिस्पर्धा आयोग के साथ-साथ कार्य करता रहता है।",
    "एकाधिकार और अवरोधक व्यापार व्यवहार अधिनियम, 1969 का मुख्य उद्देश्य आर्थिक शक्ति के संकेंद्रण को रोकना था।",
    "प्रतिस्पर्धा अधिनियम, 2002 ने इसका स्थान लिया, और ध्यान फ़र्मों के आकार से हटाकर प्रतिस्पर्धा-विरोधी आचरण पर केंद्रित किया।"],
   (0, 1, 1), 3,
   "Only statements 2 and 3 are correct. The MRTP Act of 1969, a product of the era of planning and licensing, followed reports on the concentration of economic power and controlled the expansion and mergers of large business houses, besides checking monopolistic and restrictive practices. After the reforms of 1991, the Raghavan Committee recommended a modern competition law, and the Competition Act, 2002 judges firms by what they do -- anti-competitive agreements, abuse of a dominant position and combinations that harm competition -- rather than by their size. "
   "Statement 1 is wrong: the MRTP Act was repealed in 2009, when the Competition Commission's provisions were fully in force, and the MRTP Commission was wound up, its pending cases being transferred. Being large or dominant is not itself an offence under the new law.",
   "केवल कथन 2 और 3 सही हैं। योजना और लाइसेंस के युग की उपज, 1969 का एमआरटीपी अधिनियम आर्थिक शक्ति के संकेंद्रण पर प्रतिवेदनों के बाद आया और एकाधिकारी तथा अवरोधक व्यवहारों पर रोक के साथ बड़े व्यावसायिक घरानों के विस्तार और विलय को नियंत्रित करता था। 1991 के सुधारों के बाद राघवन समिति ने आधुनिक प्रतिस्पर्धा विधि की संस्तुति की, और प्रतिस्पर्धा अधिनियम, 2002 फ़र्मों को उनके आकार से नहीं, उनके आचरण से परखता है -- प्रतिस्पर्धा-विरोधी समझौते, प्रभुत्वशाली स्थिति का दुरुपयोग और प्रतिस्पर्धा को हानि पहुँचाने वाले संयोजन। "
   "कथन 1 ग़लत है: एमआरटीपी अधिनियम 2009 में निरस्त हुआ, जब प्रतिस्पर्धा आयोग के प्रावधान पूरी तरह लागू हो गए, और एमआरटीपी आयोग समाप्त कर दिया गया, उसके लंबित मामले स्थानांतरित किए गए। नई विधि में बड़ा या प्रभुत्वशाली होना अपने-आप में अपराध नहीं है।",
   "Monopolies and Restrictive Trade Practices Act, 1969; Competition Act, 2002, section 66; Report of the High Level Committee on Competition Policy and Law (Raghavan Committee, 2000).",
   "l4-s03-eco-mrtp-1969-repeal-competition-act-conduct", "linkage")

# ---------------------------------------------------------------- Industry, Infrastructure, Energy & Services (statement, medium)
SC("Industry, Infrastructure, Energy & Services", "medium", "With reference to technical textiles, consider the following statements:",
   "तकनीकी वस्त्रों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
   ["They are textiles made mainly for their functional properties, such as geotextiles for roads and protective clothing.",
    "They cannot be made from natural fibres such as jute.",
    "The National Technical Textiles Mission promotes research, market development and exports in the sector."],
   ["ये मुख्यतः अपने कार्यात्मक गुणों के लिए बने वस्त्र हैं, जैसे सड़कों के लिए भू-वस्त्र और सुरक्षात्मक वस्त्र।",
    "इन्हें जूट जैसे प्राकृतिक रेशों से नहीं बनाया जा सकता।",
    "राष्ट्रीय तकनीकी वस्त्र मिशन इस क्षेत्र में अनुसंधान, बाज़ार विकास और निर्यात को बढ़ावा देता है।"],
   (1, 0, 1), 1,
   "Only statements 1 and 3 are correct. Technical textiles are valued for what they do rather than how they look: geotextiles that strengthen roads and embankments, agro-textiles such as shade nets and mulch mats, medical textiles, protective clothing for soldiers and firefighters, and fabrics for vehicles and buildings. The National Technical Textiles Mission, launched in 2020, funds research and standards, skill development, market promotion and exports, as India's use of such textiles is still low compared with developed economies. "
   "Statement 2 is wrong: natural fibres are widely used -- jute geotextiles protect slopes and riverbanks from erosion and then decay harmlessly, which makes them attractive for eco-friendly engineering in India's jute-growing east.",
   "केवल कथन 1 और 3 सही हैं। तकनीकी वस्त्रों का मूल्य उनके दिखने से नहीं, उनके कार्य से है: सड़कों और तटबंधों को मज़बूत करने वाले भू-वस्त्र, शेड नेट और मल्च मैट जैसे कृषि-वस्त्र, चिकित्सा वस्त्र, सैनिकों और अग्निशामकों के लिए सुरक्षात्मक वस्त्र, और वाहनों तथा भवनों के लिए कपड़े। 2020 में आरंभ राष्ट्रीय तकनीकी वस्त्र मिशन अनुसंधान और मानकों, कौशल विकास, बाज़ार संवर्धन और निर्यात को धन देता है, क्योंकि विकसित अर्थव्यवस्थाओं की तुलना में भारत में ऐसे वस्त्रों का उपयोग अभी कम है। "
   "कथन 2 ग़लत है: प्राकृतिक रेशे व्यापक रूप से प्रयुक्त होते हैं -- जूट भू-वस्त्र ढलानों और नदी-तटों को कटाव से बचाते हैं और फिर हानिरहित रूप से गल जाते हैं, जो उन्हें भारत के जूट उगाने वाले पूर्वी भाग में पर्यावरण-अनुकूल अभियांत्रिकी के लिए आकर्षक बनाता है।",
   "Ministry of Textiles, National Technical Textiles Mission.",
   "l4-s03-eco-technical-textiles-nttm-jute-geotextiles", "application")

SC("Industry, Infrastructure, Energy & Services", "medium", "Consider the following statements about energy manufacturing and renewable energy in India:",
   "भारत में ऊर्जा विनिर्माण और नवीकरणीय ऊर्जा के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
   ["The production-linked incentive scheme for Advanced Chemistry Cell batteries aims at 50 GWh of domestic manufacturing capacity.",
    "Repowering old wind farms replaces small, old turbines with larger, more efficient ones at the same good wind sites.",
    "The incentive scheme for Advanced Chemistry Cells supports only lithium-ion batteries."],
   ["उन्नत रसायन सेल बैटरियों के लिए उत्पादन-आधारित प्रोत्साहन योजना का लक्ष्य 50 गीगावाट-घंटे की घरेलू विनिर्माण क्षमता है।",
    "पुराने पवन फ़ार्मों का पुनःशक्तिकरण उन्हीं अच्छे पवन स्थलों पर छोटी, पुरानी टर्बाइनों के स्थान पर बड़ी, अधिक कुशल टर्बाइनें लगाता है।",
    "उन्नत रसायन सेलों की प्रोत्साहन योजना केवल लिथियम-आयन बैटरियों को सहायता देती है।"],
   (1, 1, 0), 2,
   "Only statements 1 and 2 are correct. The PLI scheme for Advanced Chemistry Cell battery storage, approved in 2021 with an outlay of ₹18,100 crore, seeks 50 GWh of giga-scale cell manufacturing, linking incentives to value addition in India, because cells are the costliest part of electric vehicles and grid storage and are mostly imported. Many of India's best wind sites, in Tamil Nadu and Gujarat, were filled in the 1990s and 2000s with turbines of under a megawatt; replacing them with modern multi-megawatt machines can yield several times more power from the same land, which the repowering policy encourages. "
   "Statement 3 is wrong: the scheme is technology-agnostic, open to any advanced chemistry -- sodium-ion or others as well as lithium-ion -- that meets its performance standards.",
   "केवल कथन 1 और 2 सही हैं। 2021 में ₹18,100 करोड़ के परिव्यय से स्वीकृत उन्नत रसायन सेल बैटरी भंडारण की पीएलआई योजना 50 गीगावाट-घंटे के बड़े पैमाने के सेल विनिर्माण का लक्ष्य रखती है, और प्रोत्साहनों को भारत में मूल्य संवर्धन से जोड़ती है, क्योंकि सेल विद्युत वाहनों और ग्रिड भंडारण का सबसे महँगा भाग हैं और अधिकांशतः आयात होते हैं। तमिलनाडु और गुजरात में भारत के कई सबसे अच्छे पवन स्थल 1990 और 2000 के दशकों में एक मेगावाट से कम की टर्बाइनों से भर गए थे; उन्हें आधुनिक बहु-मेगावाट मशीनों से बदलने से उसी भूमि से कई गुना अधिक बिजली मिल सकती है, जिसे पुनःशक्तिकरण नीति बढ़ावा देती है। "
   "कथन 3 ग़लत है: योजना प्रौद्योगिकी-निरपेक्ष है, किसी भी ऐसे उन्नत रसायन -- लिथियम-आयन के साथ सोडियम-आयन या अन्य भी -- के लिए खुली है जो उसके प्रदर्शन मानक पूरे करे।",
   "Ministry of Heavy Industries, PLI scheme for National Programme on Advanced Chemistry Cell Battery Storage (2021); Ministry of New and Renewable Energy, policy for repowering and life extension of wind projects.",
   "l4-s03-eco-acc-pli-50-gwh-wind-repowering", "precision")

# ---------------------------------------------------------------- Macro Concepts, National Income & Inflation (statement, medium)
S("Macro Concepts, National Income & Inflation", "medium", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The NAIRU is the rate of unemployment below which inflation tends to rise.",
   "The Big Mac index compares the price of a burger in different countries to illustrate purchasing power parity."],
  ["एनएआईआरयू बेरोज़गारी की वह दर है जिससे नीचे मुद्रास्फीति बढ़ने लगती है।",
   "बिग मैक सूचकांक क्रय शक्ति समता को समझाने के लिए विभिन्न देशों में एक बर्गर की कीमत की तुलना करता है।"],
  T2, 2,
  "Both statements are correct. The NAIRU (non-accelerating inflation rate of unemployment) is the level of unemployment consistent with stable inflation: if demand pushes unemployment below it, workers and firms bid up wages and prices and inflation accelerates, an idea that grew out of the debates on the Phillips curve in the 1960s and 1970s. It cannot be observed directly and shifts over time, which is why central banks treat estimates of it with caution. "
  "The Big Mac index, started by The Economist in 1986, compares the dollar price of the same burger across countries: if it is cheaper in one country than the market exchange rate implies, that currency is undervalued in purchasing-power terms. It is a light-hearted way to show why GDP compared at purchasing power parity -- the measure on which India is the world's third-largest economy -- differs so much from GDP at market exchange rates.",
  "दोनों कथन सही हैं। एनएआईआरयू (मुद्रास्फीति को तेज़ न करने वाली बेरोज़गारी दर) स्थिर मुद्रास्फीति से संगत बेरोज़गारी का स्तर है: यदि माँग बेरोज़गारी को इससे नीचे धकेलती है, तो श्रमिक और फ़र्में मज़दूरी और कीमतें बढ़ाते हैं और मुद्रास्फीति तेज़ होती है, एक विचार जो 1960 और 1970 के दशकों में फ़िलिप्स वक्र की बहसों से उपजा। इसे सीधे देखा नहीं जा सकता और यह समय के साथ बदलता है, इसी कारण केंद्रीय बैंक इसके अनुमानों को सावधानी से लेते हैं। "
  "द इकोनॉमिस्ट द्वारा 1986 में आरंभ बिग मैक सूचकांक देशों में एक ही बर्गर की डॉलर कीमत की तुलना करता है: यदि किसी देश में यह बाज़ार विनिमय दर के अनुमान से सस्ता है, तो उस मुद्रा का क्रय-शक्ति के अर्थ में अवमूल्यन है। यह यह दिखाने का हल्का-फुल्का तरीक़ा है कि क्रय शक्ति समता पर तुलना किया गया जीडीपी -- वह माप जिस पर भारत विश्व की तीसरी सबसे बड़ी अर्थव्यवस्था है -- बाज़ार विनिमय दरों पर जीडीपी से इतना भिन्न क्यों होता है।",
  "NCERT, Class XII, Introductory Macroeconomics; Reserve Bank of India, Monetary Policy Reports; World Bank, International Comparison Program.",
  "l4-s03-eco-nairu-big-mac-ppp", craft="linkage")

# ---------------------------------------------------------------- Money, Banking & Monetary Policy (MCQ, medium)
M("Money, Banking & Monetary Policy", "medium", "The 'EASE' (Enhanced Access and Service Excellence) reform agenda, launched in 2018, applies to",
  "2018 में आरंभ 'ईज़' (एन्हांस्ड एक्सेस एंड सर्विस एक्सीलेंस) सुधार एजेंडा किन पर लागू होता है?",
  ["public sector banks", "regional rural banks only", "urban co-operative banks", "non-banking financial companies"],
  ["सार्वजनिक क्षेत्र के बैंक", "केवल क्षेत्रीय ग्रामीण बैंक", "शहरी सहकारी बैंक", "ग़ैर-बैंकिंग वित्तीय कंपनियाँ"],
  0,
  "After the Government recapitalised the public sector banks, it tied the support to reforms: the EASE agenda, framed by the Department of Financial Services with the Indian Banks' Association, sets common reforms for all public sector banks in areas such as prudent lending, customer service, digital banking, governance and the handling of bad loans. Each bank's progress is measured on an index and published every year, and the agenda has moved through successive versions towards technology and data-driven banking. "
  "The other options are regulated in other ways: regional rural banks are sponsored by public sector banks, co-operative banks are supervised by the RBI with the States, and NBFCs fall under the RBI's scale-based regulation.",
  "सरकार द्वारा सार्वजनिक क्षेत्र के बैंकों का पुनर्पूंजीकरण करने के बाद उसने इस सहायता को सुधारों से जोड़ा: वित्तीय सेवा विभाग द्वारा भारतीय बैंक संघ के साथ बनाया गया ईज़ एजेंडा सभी सार्वजनिक क्षेत्र के बैंकों के लिए विवेकपूर्ण ऋण, ग्राहक सेवा, डिजिटल बैंकिंग, शासन और डूबत ऋणों के प्रबंधन जैसे क्षेत्रों में साझा सुधार तय करता है। हर बैंक की प्रगति एक सूचकांक पर मापी और हर वर्ष प्रकाशित की जाती है, और एजेंडा क्रमिक संस्करणों से प्रौद्योगिकी और आँकड़ा-आधारित बैंकिंग की ओर बढ़ा है। "
  "अन्य विकल्प अन्य ढंग से विनियमित हैं: क्षेत्रीय ग्रामीण बैंक सार्वजनिक क्षेत्र के बैंकों द्वारा प्रायोजित हैं, सहकारी बैंकों का पर्यवेक्षण आरबीआई राज्यों के साथ करता है, और एनबीएफ़सी आरबीआई के पैमाना-आधारित विनियमन के अंतर्गत आती हैं।",
  "Ministry of Finance, Department of Financial Services; Indian Banks' Association, EASE reform reports.",
  "l4-s03-eco-ease-reforms-public-sector-banks", pos=0, craft="recall")

# ---------------------------------------------------------------- Money, Banking & Monetary Policy (statement, medium)
SC("Money, Banking & Monetary Policy", "medium", "With reference to the recovery of bad loans by banks in India, consider the following statements:",
   "भारत में बैंकों द्वारा डूबत ऋणों की वसूली के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
   ["Debt Recovery Tribunals decide claims of banks and financial institutions of ₹20 lakh and above.",
    "Appeals against the orders of Debt Recovery Tribunals lie to the Debt Recovery Appellate Tribunals.",
    "Under the SARFAESI Act, banks can take possession of agricultural land pledged as security without going to court.",
    "Under the RBI's directions of 2024, a borrower can be classified as a wilful defaulter for a wilful default of ₹25 lakh or more."],
   ["ऋण वसूली अधिकरण बैंकों और वित्तीय संस्थाओं के ₹20 लाख और अधिक के दावों का निर्णय करते हैं।",
    "ऋण वसूली अधिकरणों के आदेशों के विरुद्ध अपील ऋण वसूली अपीलीय अधिकरणों में होती है।",
    "सरफ़ेसी अधिनियम के अंतर्गत बैंक प्रतिभूति के रूप में गिरवी रखी कृषि भूमि पर न्यायालय गए बिना क़ब्ज़ा ले सकते हैं।",
    "आरबीआई के 2024 के निदेशों के अंतर्गत ₹25 लाख या अधिक की जान-बूझकर चूक पर किसी उधारकर्ता को जान-बूझकर चूककर्ता वर्गीकृत किया जा सकता है।"],
   (1, 1, 0, 1), 3,
   "Statements 1, 2 and 4 are correct. Debt Recovery Tribunals, set up under the Recovery of Debts Due to Banks and Financial Institutions Act, 1993, hear recovery claims of ₹20 lakh and above -- the limit was raised from ₹10 lakh in 2018 to reduce their backlog -- with appeals to the Debt Recovery Appellate Tribunals. The RBI's Master Directions on wilful defaulters (2024) set a threshold of ₹25 lakh and give the borrower a hearing before the tag is applied; wilful defaulters are barred from fresh credit and from restructuring. "
   "Statement 3 is wrong: section 31 of the SARFAESI Act, 2002 excludes agricultural land from its scope, so banks cannot use its powers of enforcement without the courts against farm land offered as security. This exclusion protects farmers but is one reason why lending against land in villages remains limited.",
   "केवल कथन 1, 2 और 4 सही हैं। बैंकों और वित्तीय संस्थाओं के देय ऋणों की वसूली अधिनियम, 1993 के अंतर्गत बने ऋण वसूली अधिकरण ₹20 लाख और अधिक के वसूली दावे सुनते हैं -- उनके लंबित मामले घटाने के लिए 2018 में सीमा ₹10 लाख से बढ़ाई गई -- और अपीलें ऋण वसूली अपीलीय अधिकरणों में जाती हैं। जान-बूझकर चूक करने वालों पर आरबीआई के मास्टर निदेश (2024) ₹25 लाख की सीमा तय करते हैं और ठप्पा लगाने से पहले उधारकर्ता को सुनवाई देते हैं; जान-बूझकर चूक करने वालों को नए ऋण और पुनर्गठन से वंचित किया जाता है। "
   "कथन 3 ग़लत है: सरफ़ेसी अधिनियम, 2002 की धारा 31 कृषि भूमि को इसके दायरे से बाहर रखती है, इसलिए बैंक प्रतिभूति के रूप में दी गई कृषि भूमि पर न्यायालयों के बिना इसकी प्रवर्तन शक्तियों का प्रयोग नहीं कर सकते। यह अपवर्जन किसानों की रक्षा करता है, पर यह एक कारण है कि गाँवों में भूमि के बदले ऋण सीमित रहता है।",
   "Recovery of Debts and Bankruptcy Act, 1993; SARFAESI Act, 2002, section 31; Reserve Bank of India, Master Directions on Treatment of Wilful Defaulters and Large Defaulters (2024).",
   "l4-s03-eco-drt-20-lakh-drat-sarfaesi-farm-land-wilful-25-lakh", "precision")

# ---------------------------------------------------------------- Taxation & Fiscal Federalism (statement, medium)
SC("Taxation & Fiscal Federalism", "medium", "With reference to taxation in India, consider the following statements:",
   "भारत में कराधान के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
   ["Under the reverse charge mechanism of GST, the recipient of a supply, rather than the supplier, pays the tax.",
    "An e-way bill is generally needed to move goods worth more than ₹50,000.",
    "The Direct Taxes Code of 2010 replaced the Income-tax Act, 1961."],
   ["जीएसटी की प्रतिलोम प्रभार व्यवस्था में आपूर्तिकर्ता के बजाय आपूर्ति का प्राप्तकर्ता कर चुकाता है।",
    "₹50,000 से अधिक मूल्य की वस्तुएँ ले जाने के लिए सामान्यतः ई-वे बिल आवश्यक है।",
    "2010 की प्रत्यक्ष कर संहिता ने आयकर अधिनियम, 1961 का स्थान लिया।"],
   (1, 1, 0), 0,
   "Only statements 1 and 2 are correct. Reverse charge applies to notified supplies, such as legal services from an advocate to a business or goods transport services, and to some purchases from unregistered suppliers, where collecting tax from the recipient is easier and less open to evasion. The e-way bill, generated electronically on the GST portal, tracks the movement of goods worth more than ₹50,000 and has replaced the old check-post system. "
   "Statement 3 is wrong: the Direct Taxes Code Bill of 2010 was never enacted and lapsed; it is the Income-tax Act, 2025, effective from 1 April 2026, that has replaced the 1961 Act, with simpler language and a single 'tax year'.",
   "केवल कथन 1 और 2 सही हैं। प्रतिलोम प्रभार अधिसूचित आपूर्तियों पर लागू होता है, जैसे किसी अधिवक्ता से किसी व्यवसाय को विधिक सेवाएँ या माल परिवहन सेवाएँ, और अपंजीकृत आपूर्तिकर्ताओं से कुछ ख़रीदों पर, जहाँ प्राप्तकर्ता से कर वसूलना आसान और चोरी के लिए कम खुला है। जीएसटी पोर्टल पर इलेक्ट्रॉनिक रूप से बनने वाला ई-वे बिल ₹50,000 से अधिक मूल्य की वस्तुओं की आवाजाही पर नज़र रखता है और उसने पुरानी जाँच-चौकी प्रणाली का स्थान लिया है। "
   "कथन 3 ग़लत है: 2010 का प्रत्यक्ष कर संहिता विधेयक कभी अधिनियमित नहीं हुआ और व्यपगत हो गया; 1 अप्रैल 2026 से प्रभावी आयकर अधिनियम, 2025 ने 1961 के अधिनियम का स्थान लिया है, सरल भाषा और एकल 'कर वर्ष' के साथ।",
   "Central Goods and Services Tax Act, 2017, section 9(3)-(4) and rule 138 of the CGST Rules; Income-tax Act, 2025; Direct Taxes Code Bill, 2010.",
   "l4-s03-eco-reverse-charge-e-way-bill-dtc-lapsed", "precision")

write("gs_l4_s03_e.sql")
