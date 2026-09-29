# -*- coding: utf-8 -*-
"""Level 2 · Test 18 (Economy 4: Sectors of the Economy & Inclusive Growth) -- Agriculture & Food Economy (38).
  medium statement 14, easy statement 5, hard statement 5, medium MCQ 5, medium Statement-I/II 3, easy MCQ 2,
  easy Statement-I/II 1, hard Statement-I/II 1, hard MCQ 1, medium pairs 1.
The National Food Security Act's entitlements, cooperatives' constitutional status, NRLM and DBT are Polity facts;
crops, producing States, world ranks, Operation Flood and the 'revolutions' are Geography Test 14; the WTO boxes
and peace clause are Test 16 and the food subsidy's place in the Budget Test 17. This file stays on farm prices,
procurement, markets, inputs, credit, insurance and the structure of Indian agriculture."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Economy"
AG = "Agriculture & Food Economy"
IED = "NCERT Class XI, Indian Economic Development"
MOA = "Ministry of Agriculture and Farmers Welfare"
DFPD = "Department of Food and Public Distribution"
ES = "Economic Survey 2024-25 -- chapter on agriculture"

# ================================================================ MEDIUM STATEMENTS (14)
S(AG, "medium", "Consider the following statements about minimum support prices (MSP):",
  "न्यूनतम समर्थन मूल्य (MSP) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["MSPs are announced for both kharif and rabi crops.",
   "MSPs are announced for 22 mandated crops.",
   "For sugarcane, the Centre fixes a Fair and Remunerative Price instead of an MSP.",
   "MSP has statutory backing, so traders are legally bound to pay it."],
  ["MSP ख़रीफ़ और रबी, दोनों मौसमों की फ़सलों के लिए घोषित किए जाते हैं।",
   "MSP 22 अधिदेशित फ़सलों के लिए घोषित किया जाता है।",
   "गन्ने के लिए केंद्र MSP के बजाय उचित और लाभकारी मूल्य (FRP) तय करता है।",
   "MSP को वैधानिक आधार प्राप्त है, इसलिए व्यापारी इसे चुकाने के लिए क़ानूनन बाध्य हैं।"],
  C4, 2,
  "Statements 1, 2 and 3 are correct. Prices are announced ahead of each sowing season on the recommendation of the Commission for Agricultural Costs and Prices; the 22 crops are 14 kharif crops, 6 rabi crops, and jute and copra; sugar mills must pay at least the FRP for cane. "
  "Statement 4 is wrong: MSP is an administrative announcement, not a legal entitlement -- it is effective only where the government actually procures, which is why farmers' groups have demanded a legal guarantee.",
  "कथन 1, 2 और 3 सही हैं। क़ीमतें हर बुआई मौसम से पहले कृषि लागत और मूल्य आयोग की सिफ़ारिश पर घोषित होती हैं; 22 फ़सलें 14 ख़रीफ़, 6 रबी, और जूट तथा खोपरा हैं; चीनी मिलों को गन्ने के लिए कम से कम FRP चुकाना होता है। "
  "कथन 4 गलत है: MSP एक प्रशासनिक घोषणा है, क़ानूनी अधिकार नहीं; यह वहीं प्रभावी है जहाँ सरकार वास्तव में ख़रीद करती है, इसीलिए किसान संगठनों ने इसकी क़ानूनी गारंटी की माँग की है।",
  f"{MOA} -- Commission for Agricultural Costs and Prices.",
  "ag-msp-cacp-crops",
  closing="How many of the above statements are correct?",
  closing_hi="उपर्युक्त में से कितने कथन सही हैं?")

S(AG, "medium", "Consider the following statements about the procurement of foodgrains:",
  "खाद्यान्न की ख़रीद के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Under decentralised procurement, the Food Corporation of India procures in every State and the State Governments have no role.",
   "The Food Corporation of India also runs the fair price shops that sell grain to ration card holders.",
   "The Food Corporation of India was set up in 1991 as part of the economic reforms."],
  ["विकेंद्रीकृत ख़रीद (decentralised procurement) में भारतीय खाद्य निगम हर राज्य में ख़रीद करता है और राज्य सरकारों की कोई भूमिका नहीं होती।",
   "भारतीय खाद्य निगम राशन कार्ड धारकों को अनाज बेचने वाली उचित मूल्य की दुकानें भी चलाता है।",
   "भारतीय खाद्य निगम की स्थापना 1991 में आर्थिक सुधारों के भाग के रूप में हुई।"],
  C3, 3,
  "None of the statements is correct. Statement 1 is wrong: under decentralised procurement, begun in 1997-98, the State Governments themselves procure, store and distribute grain, and the Centre reimburses them. "
  "Statement 2 is wrong: the FCI moves grain up to State depots; fair price shops are licensed and supervised by the State Governments, which run the distribution end of the system. "
  "Statement 3 is wrong: the FCI was set up in 1965 under the Food Corporations Act, 1964, at a time of acute shortage.",
  "कोई भी कथन सही नहीं है। कथन 1 गलत है: 1997-98 में शुरू हुई विकेंद्रीकृत ख़रीद में राज्य सरकारें स्वयं अनाज ख़रीदती, भंडारित करती और वितरित करती हैं, और केंद्र उन्हें प्रतिपूर्ति करता है। "
  "कथन 2 गलत है: FCI अनाज को राज्य डिपो तक पहुँचाता है; उचित मूल्य की दुकानों को राज्य सरकारें लाइसेंस देती और उनकी निगरानी करती हैं, जो व्यवस्था का वितरण वाला सिरा चलाती हैं। "
  "कथन 3 गलत है: FCI की स्थापना 1965 में, भारी कमी के दौर में, खाद्य निगम अधिनियम, 1964 के तहत हुई।",
  f"{DFPD} -- Decentralised Procurement Scheme; Food Corporation of India.",
  "ag-procurement-none")

S(AG, "medium", "Consider the following statements about the central pool of foodgrains:",
  "खाद्यान्न के केंद्रीय पूल के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Under the Open Market Sale Scheme, the FCI sells surplus grain in the open market to check prices.",
   "Buffer stock norms are fixed for the start of each quarter of the year.",
   "Stocks in the central pool are usually below the buffer norms."],
  ["खुला बाज़ार बिक्री योजना (OMSS) के तहत FCI क़ीमतों पर लगाम लगाने के लिए अतिरिक्त अनाज खुले बाज़ार में बेचता है।",
   "बफ़र स्टॉक के मानदंड वर्ष की हर तिमाही की शुरुआत के लिए तय किए जाते हैं।",
   "केंद्रीय पूल में भंडार प्रायः बफ़र मानदंडों से कम रहता है।"],
  C3, 1,
  "Statements 1 and 2 are correct: norms are set for 1 April, 1 July, 1 October and 1 January, since stocks swing with the rabi and kharif harvests; OMSS sales of wheat to flour mills and traders have been used repeatedly to cool atta prices. "
  "Statement 3 is wrong: stocks, especially of rice, have usually been well above the norms, which raises storage costs and the risk of wastage.",
  "कथन 1 और 2 सही हैं: मानदंड 1 अप्रैल, 1 जुलाई, 1 अक्टूबर और 1 जनवरी के लिए तय होते हैं, क्योंकि भंडार रबी और ख़रीफ़ की फ़सलों के साथ घटता-बढ़ता है; आटे की क़ीमतें ठंडी करने के लिए आटा मिलों और व्यापारियों को OMSS के तहत गेहूँ की बिक्री बार-बार की गई है। "
  "कथन 3 गलत है: भंडार, विशेषकर चावल का, प्रायः मानदंडों से काफ़ी ऊपर रहा है, जिससे भंडारण की लागत और बर्बादी का जोखिम बढ़ता है।",
  f"{DFPD} -- Buffer norms for the central pool; Open Market Sale Scheme (Domestic).",
  "ag-buffer-omss")

S(AG, "medium", "Consider the following statements about agricultural marketing:",
  "कृषि विपणन के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Agricultural Produce Market Committee (APMC) Acts are State laws.",
   "The National Agriculture Market (e-NAM) was launched in 2016.",
   "e-NAM links existing APMC markets on a common online trading platform."],
  ["कृषि उपज मंडी समिति (APMC) अधिनियम राज्य क़ानून हैं।",
   "राष्ट्रीय कृषि बाज़ार (e-NAM) 2016 में शुरू किया गया।",
   "e-NAM मौजूदा APMC मंडियों को एक साझा ऑनलाइन व्यापार मंच पर जोड़ता है।"],
  C3, 2,
  "All three statements are correct. Agriculture and markets are State subjects, so each State regulates its own mandis. e-NAM, run by the Small Farmers' Agribusiness Consortium, now covers more than 1,400 mandis; its aim is price discovery across markets, although most trade on it is still within a single mandi.",
  "तीनों कथन सही हैं। कृषि और बाज़ार राज्य के विषय हैं, इसलिए हर राज्य अपनी मंडियों को स्वयं नियंत्रित करता है। लघु कृषक कृषि-व्यापार संघ (SFAC) द्वारा चलाया जाने वाला e-NAM अब 1,400 से अधिक मंडियों को शामिल करता है; इसका लक्ष्य बाज़ारों के बीच मूल्य खोज है, यद्यपि इस पर अधिकांश व्यापार अब भी एक ही मंडी के भीतर होता है।",
  f"{MOA} -- National Agriculture Market (e-NAM).",
  "ag-apmc-enam")

S(AG, "medium", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Model Agricultural Produce and Livestock Marketing Act, 2017 was enacted by Parliament.",
   "One of the three farm laws of 2020 dealt with contract farming.",
   "The three farm laws of 2020 were repealed in 2021."],
  ["आदर्श कृषि उपज और पशुधन विपणन अधिनियम, 2017 संसद ने अधिनियमित किया।",
   "2020 के तीन कृषि क़ानूनों में से एक अनुबंध खेती (contract farming) से संबंधित था।",
   "2020 के तीनों कृषि क़ानून 2021 में निरस्त कर दिए गए।"],
  C3, 1,
  "Statements 2 and 3 are correct: the Farmers (Empowerment and Protection) Agreement on Price Assurance and Farm Services Act dealt with contract farming, and the laws were withdrawn after a year of farmers' protests. "
  "Statement 1 is wrong: the 2017 Act is a 'model' drafted by the Centre for the States to adopt, since agricultural markets are a State subject; the Centre issued a Model Contract Farming Act in 2018 on the same basis.",
  "कथन 2 और 3 सही हैं: कृषक (सशक्तिकरण और संरक्षण) क़ीमत आश्वासन और कृषि सेवा पर करार अधिनियम अनुबंध खेती से संबंधित था, और किसानों के एक वर्ष के आंदोलन के बाद क़ानून वापस लिए गए। "
  "कथन 1 गलत है: 2017 का अधिनियम एक 'आदर्श' (model) क़ानून है जिसे केंद्र ने राज्यों द्वारा अपनाने के लिए तैयार किया, क्योंकि कृषि बाज़ार राज्य का विषय है; इसी आधार पर केंद्र ने 2018 में एक आदर्श अनुबंध खेती अधिनियम जारी किया।",
  f"{MOA} -- Model APLM Act, 2017; Model Contract Farming Act, 2018; Farm Laws Repeal Act, 2021.",
  "ag-model-acts-farm-laws")

S(AG, "medium", "Consider the following statements about the Pradhan Mantri Fasal Bima Yojana (PMFBY):",
  "प्रधानमंत्री फ़सल बीमा योजना (PMFBY) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It was launched in 2016.",
   "Farmers pay a premium of 2 per cent for kharif crops, 1.5 per cent for rabi crops and 5 per cent for commercial and horticultural crops.",
   "Enrolment is compulsory for all farmers who have taken crop loans."],
  ["इसे 2016 में शुरू किया गया।",
   "किसान ख़रीफ़ फ़सलों के लिए 2 प्रतिशत, रबी फ़सलों के लिए 1.5 प्रतिशत और वाणिज्यिक तथा बाग़वानी फ़सलों के लिए 5 प्रतिशत प्रीमियम देते हैं।",
   "फ़सल ऋण लेने वाले सभी किसानों के लिए नामांकन अनिवार्य है।"],
  C3, 1,
  "Statements 1 and 2 are correct: the rest of the actuarial premium is shared by the Centre and the States, equally in most States and 90:10 in the North-East and Himalayan States. "
  "Statement 3 is wrong: enrolment was made voluntary for all farmers, including those with loans, from kharif 2020, after complaints that premiums were being deducted without farmers' consent.",
  "कथन 1 और 2 सही हैं: बीमांकिक प्रीमियम का शेष भाग केंद्र और राज्य बाँटते हैं, अधिकांश राज्यों में बराबर-बराबर और पूर्वोत्तर तथा हिमालयी राज्यों में 90:10 में। "
  "कथन 3 गलत है: ऐसी शिकायतों के बाद कि किसानों की सहमति के बिना प्रीमियम काटा जा रहा है, ख़रीफ़ 2020 से ऋण लेने वालों सहित सभी किसानों के लिए नामांकन स्वैच्छिक कर दिया गया।",
  f"{MOA} -- PMFBY operational guidelines.",
  "ag-pmfby")

S(AG, "medium", "Consider the following statements about farm credit:",
  "कृषि ऋण के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Kisan Credit Card scheme was introduced in 1998.",
   "Under the interest subvention scheme, farmers who repay promptly pay an effective interest rate of 4 per cent on short-term crop loans.",
   "Kisan Credit Cards have been extended to farmers in animal husbandry and fisheries."],
  ["किसान क्रेडिट कार्ड योजना 1998 में शुरू की गई।",
   "ब्याज अनुदान (interest subvention) योजना के तहत समय पर चुकाने वाले किसान अल्पकालिक फ़सल ऋण पर 4 प्रतिशत की प्रभावी ब्याज दर देते हैं।",
   "किसान क्रेडिट कार्ड पशुपालन और मत्स्य पालन करने वाले किसानों तक बढ़ाए गए हैं।"],
  C3, 2,
  "All three statements are correct. Banks lend at 7 per cent, with a subvention from the Centre, and a further 3 per cent incentive for prompt repayment brings the cost down to 4 per cent; the Budget 2025-26 raised the loan limit under the scheme from ₹3 lakh to ₹5 lakh. The extension to livestock and fisheries came in 2018-19.",
  "तीनों कथन सही हैं। बैंक केंद्र के अनुदान के साथ 7 प्रतिशत पर ऋण देते हैं, और समय पर चुकाने पर 3 प्रतिशत का अतिरिक्त प्रोत्साहन लागत को 4 प्रतिशत तक ले आता है; बजट 2025-26 ने योजना के तहत ऋण सीमा ₹3 लाख से बढ़ाकर ₹5 लाख की। पशुधन और मत्स्य पालन तक विस्तार 2018-19 में हुआ।",
  f"{MOA} -- Modified Interest Subvention Scheme; Union Budget 2025-26.",
  "ag-kcc-interest-subvention")

S(AG, "medium", "Consider the following statements about PM-KISAN:",
  "PM-KISAN के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It gives eligible farmer families ₹6,000 a year in three instalments.",
   "It was launched in 2016.",
   "It is meant mainly for tenant farmers and landless labourers."],
  ["यह पात्र किसान परिवारों को तीन किस्तों में ₹6,000 प्रति वर्ष देती है।",
   "इसे 2016 में शुरू किया गया।",
   "यह मुख्य रूप से बटाईदार (tenant) किसानों और भूमिहीन मज़दूरों के लिए है।"],
  C3, 0,
  "Only statement 1 is correct: the money goes directly into bank accounts. "
  "Statement 2 is wrong: the scheme was announced in the interim Budget of February 2019, with effect from December 2018. "
  "Statement 3 is wrong: it is for landholding farmer families, identified from land records -- so tenants and landless labourers, often the poorest cultivators, are left out, a common criticism of the scheme.",
  "केवल कथन 1 सही है: धन सीधे बैंक खातों में जाता है। "
  "कथन 2 गलत है: योजना की घोषणा फ़रवरी 2019 के अंतरिम बजट में, दिसंबर 2018 से प्रभावी रूप में, हुई। "
  "कथन 3 गलत है: यह भूमिधारक किसान परिवारों के लिए है, जिनकी पहचान भूमि अभिलेखों से होती है; इसलिए बटाईदार और भूमिहीन मज़दूर, जो प्रायः सबसे ग़रीब खेतिहर होते हैं, छूट जाते हैं; यह योजना की एक आम आलोचना है।",
  f"{MOA} -- PM-KISAN operational guidelines.",
  "ag-pm-kisan")

S(AG, "medium", "Consider the following statements about fertilisers:",
  "उर्वरकों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Nutrient Based Subsidy scheme for phosphatic and potassic fertilisers began in 2010.",
   "Urea is covered under the Nutrient Based Subsidy scheme.",
   "India is self-sufficient in potash."],
  ["फ़ॉस्फ़ेटिक और पोटाशिक उर्वरकों के लिए पोषक-तत्व आधारित सब्सिडी (NBS) योजना 2010 में शुरू हुई।",
   "यूरिया पोषक-तत्व आधारित सब्सिडी योजना के अंतर्गत आता है।",
   "भारत पोटाश में आत्मनिर्भर है।"],
  C3, 0,
  "Only statement 1 is correct: under NBS a fixed subsidy per kilogram of nitrogen, phosphorus, potash and sulphur is paid, and companies set retail prices. "
  "Statement 2 is wrong: urea is outside NBS; its retail price is fixed by the government and the subsidy covers the rest of the cost, which has made urea far cheaper than other fertilisers and encouraged its overuse. "
  "Statement 3 is wrong: India has no commercially mined potash and imports all of it.",
  "केवल कथन 1 सही है: NBS में नाइट्रोजन, फ़ॉस्फ़ोरस, पोटाश और सल्फ़र के प्रति किलोग्राम एक निश्चित सब्सिडी दी जाती है, और कंपनियाँ खुदरा क़ीमतें तय करती हैं। "
  "कथन 2 गलत है: यूरिया NBS से बाहर है; इसकी खुदरा क़ीमत सरकार तय करती है और शेष लागत सब्सिडी से पूरी होती है; इससे यूरिया अन्य उर्वरकों से कहीं सस्ता हो गया और इसके अति-उपयोग को बढ़ावा मिला। "
  "कथन 3 गलत है: भारत में वाणिज्यिक रूप से पोटाश का खनन नहीं होता और वह इसका पूरा आयात करता है।",
  "Department of Fertilizers -- Nutrient Based Subsidy policy; Economic Survey.",
  "ag-fertiliser-nbs-urea")

S(AG, "medium", "Consider the following statements based on the Agriculture Census 2015-16:",
  "कृषि गणना 2015-16 के आधार पर निम्नलिखित कथनों पर विचार कीजिए:",
  ["Marginal holdings, of less than one hectare, made up about two-thirds of all operational holdings.",
   "The average size of holdings had been rising since 1970-71.",
   "Large holdings, of 10 hectares or more, accounted for over a fifth of the operated area."],
  ["एक हेक्टेयर से कम की सीमांत जोतें सभी परिचालन जोतों का लगभग दो-तिहाई थीं।",
   "जोतों का औसत आकार 1970-71 से बढ़ता रहा था।",
   "10 हेक्टेयर या अधिक की बड़ी जोतों के पास परिचालित क्षेत्र का पाँचवें भाग से अधिक था।"],
  C3, 0,
  "Only statement 1 is correct: about 68 per cent of holdings were marginal, and with small holdings over 86 per cent were below two hectares. "
  "Statement 2 is wrong: the average holding shrank from 2.28 hectares in 1970-71 to 1.08 hectares, as land was divided among heirs. "
  "Statement 3 is wrong: large holdings were under 1 per cent of the total and covered only about 9 per cent of the area.",
  "केवल कथन 1 सही है: लगभग 68 प्रतिशत जोतें सीमांत थीं, और छोटी जोतों को मिलाकर 86 प्रतिशत से अधिक दो हेक्टेयर से कम थीं। "
  "कथन 2 गलत है: उत्तराधिकारियों में भूमि बँटने से औसत जोत 1970-71 के 2.28 हेक्टेयर से घटकर 1.08 हेक्टेयर रह गई। "
  "कथन 3 गलत है: बड़ी जोतें कुल का 1 प्रतिशत से कम थीं और केवल लगभग 9 प्रतिशत क्षेत्र पर थीं।",
  f"{MOA} -- Agriculture Census 2015-16.",
  "ag-land-holdings-census")

S(AG, "medium", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["India is a net exporter of agricultural and allied products.",
   "Marine products are India's largest agricultural export item by value.",
   "Rice exports are handled mainly by the Food Corporation of India.",
   "The Agricultural and Processed Food Products Export Development Authority (APEDA) regulates the import of foodgrains into India."],
  ["भारत कृषि और संबद्ध उत्पादों का शुद्ध निर्यातक है।",
   "समुद्री उत्पाद मूल्य के हिसाब से भारत की सबसे बड़ी कृषि निर्यात मद हैं।",
   "चावल का निर्यात मुख्य रूप से भारतीय खाद्य निगम करता है।",
   "कृषि और प्रसंस्कृत खाद्य उत्पाद निर्यात विकास प्राधिकरण (APEDA) भारत में खाद्यान्न के आयात को नियंत्रित करता है।"],
  C4, 0,
  "Only statement 1 is correct: farm exports of about 50 billion dollars a year exceed imports, which are dominated by vegetable oils and pulses. "
  "Statement 2 is wrong: rice -- basmati and non-basmati -- is the largest item, well ahead of marine products. "
  "Statement 3 is wrong: rice is exported by private traders; the FCI's grain goes mainly to the public distribution system. "
  "Statement 4 is wrong: APEDA promotes and develops exports of scheduled products such as fruits, vegetables, meat and basmati rice.",
  "केवल कथन 1 सही है: लगभग 50 अरब डॉलर प्रति वर्ष के कृषि निर्यात आयात से अधिक हैं, जिनमें वनस्पति तेलों और दालों का प्रभुत्व है। "
  "कथन 2 गलत है: चावल, बासमती और गैर-बासमती, सबसे बड़ी मद है, जो समुद्री उत्पादों से काफ़ी आगे है। "
  "कथन 3 गलत है: चावल का निर्यात निजी व्यापारी करते हैं; FCI का अनाज मुख्य रूप से सार्वजनिक वितरण प्रणाली में जाता है। "
  "कथन 4 गलत है: APEDA फल, सब्ज़ियाँ, मांस और बासमती चावल जैसे अनुसूचित उत्पादों के निर्यात को बढ़ावा देता और विकसित करता है।",
  "Department of Commerce -- Agricultural trade data; APEDA.",
  "ag-farm-trade",
  closing="How many of the above statements are correct?",
  closing_hi="उपर्युक्त में से कितने कथन सही हैं?")

S(AG, "medium", "Consider the following statements about Indian agriculture:",
  "भारतीय कृषि के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Agriculture and allied sectors account for about 18 per cent of India's gross value added.",
   "Over the past decade, livestock and fisheries have grown faster than crop agriculture.",
   "Livestock contributes more to agricultural gross value added than fisheries."],
  ["कृषि और संबद्ध क्षेत्र भारत के सकल मूल्य वर्धन (GVA) का लगभग 18 प्रतिशत हैं।",
   "पिछले एक दशक में पशुधन और मत्स्य पालन फ़सल खेती से तेज़ी से बढ़े हैं।",
   "कृषि सकल मूल्य वर्धन में पशुधन का योगदान मत्स्य पालन से अधिक है।"],
  C3, 2,
  "All three statements are correct. Livestock has grown at roughly 13 per cent a year and fisheries at about 9 per cent, against around 2 per cent for crops, so allied activities now make up well over a third of agricultural output -- livestock alone about 30 per cent. They matter most for small and landless households, whose incomes depend less on land.",
  "तीनों कथन सही हैं। पशुधन लगभग 13 प्रतिशत और मत्स्य पालन लगभग 9 प्रतिशत प्रति वर्ष बढ़े हैं, जबकि फ़सलें लगभग 2 प्रतिशत, इसलिए संबद्ध गतिविधियाँ अब कृषि उत्पादन का एक-तिहाई से काफ़ी अधिक हैं; अकेले पशुधन लगभग 30 प्रतिशत। ये छोटे और भूमिहीन परिवारों के लिए सबसे महत्त्वपूर्ण हैं, जिनकी आय भूमि पर कम निर्भर है।",
  f"{ES}; MoSPI -- National Accounts Statistics.",
  "ag-structure-allied-growth")

S(AG, "medium", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Food processing industries come under the Ministry of Agriculture and Farmers Welfare.",
   "The PM Kisan SAMPADA Yojana is a crop insurance scheme.",
   "Operation Greens was launched to stabilise the prices of wheat and rice."],
  ["खाद्य प्रसंस्करण उद्योग कृषि और किसान कल्याण मंत्रालय के अंतर्गत आते हैं।",
   "PM किसान संपदा योजना एक फ़सल बीमा योजना है।",
   "ऑपरेशन ग्रीन्स गेहूँ और चावल की क़ीमतें स्थिर करने के लिए शुरू किया गया।"],
  C3, 3,
  "None of the statements is correct. Statement 1 is wrong: there is a separate Ministry of Food Processing Industries. "
  "Statement 2 is wrong: PM Kisan SAMPADA is that ministry's umbrella scheme for food processing -- mega food parks, cold chains and processing units. "
  "Statement 3 is wrong: Operation Greens (2018) targeted tomato, onion and potato, whose prices swing wildly, and was later widened to other perishables; wheat and rice are supported through MSP and procurement.",
  "कोई भी कथन सही नहीं है। कथन 1 गलत है: खाद्य प्रसंस्करण उद्योग का एक अलग मंत्रालय है। "
  "कथन 2 गलत है: PM किसान संपदा उस मंत्रालय की खाद्य प्रसंस्करण के लिए छत्र योजना है, जिसमें मेगा फ़ूड पार्क, कोल्ड चेन और प्रसंस्करण इकाइयाँ हैं। "
  "कथन 3 गलत है: ऑपरेशन ग्रीन्स (2018) का लक्ष्य टमाटर, प्याज़ और आलू थे, जिनकी क़ीमतें बहुत उतार-चढ़ाव वाली होती हैं, और बाद में इसे अन्य जल्दी ख़राब होने वाली वस्तुओं तक बढ़ाया गया; गेहूँ और चावल को MSP और ख़रीद से समर्थन मिलता है।",
  "Ministry of Food Processing Industries -- PM Kisan SAMPADA Yojana; Operation Greens.",
  "ag-food-processing-none")

S(AG, "medium", "Consider the following statements about irrigation in India:",
  "भारत में सिंचाई के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["More than half of the net sown area is irrigated.",
   "Groundwater is the largest source of irrigation.",
   "Drip and sprinkler irrigation cover most of the irrigated area."],
  ["शुद्ध बोए गए क्षेत्र का आधे से अधिक भाग सिंचित है।",
   "भूजल सिंचाई का सबसे बड़ा स्रोत है।",
   "टपक (drip) और बौछारी (sprinkler) सिंचाई अधिकांश सिंचित क्षेत्र पर होती है।"],
  C3, 1,
  "Statements 1 and 2 are correct: about 55 per cent of the net sown area is irrigated, and tube wells and other wells supply over 60 per cent of it -- which is why cheap or free farm power has driven down water tables in Punjab, Haryana and Rajasthan. "
  "Statement 3 is wrong: micro-irrigation, though it saves water and is subsidised under PM Krishi Sinchayee Yojana, covers only a small share of irrigated land; flood irrigation still dominates.",
  "कथन 1 और 2 सही हैं: शुद्ध बोए गए क्षेत्र का लगभग 55 प्रतिशत सिंचित है, और नलकूप तथा अन्य कुएँ इसका 60 प्रतिशत से अधिक पानी देते हैं; इसीलिए सस्ती या मुफ़्त कृषि बिजली ने पंजाब, हरियाणा और राजस्थान में जल-स्तर नीचे गिराया है। "
  "कथन 3 गलत है: सूक्ष्म सिंचाई, यद्यपि यह पानी बचाती है और PM कृषि सिंचाई योजना के तहत इस पर सब्सिडी मिलती है, सिंचित भूमि के छोटे हिस्से पर ही है; बाढ़ (flood) सिंचाई अब भी प्रमुख है।",
  f"{MOA} -- Land Use Statistics; Central Ground Water Board.",
  "ag-irrigation-sources")

# ================================================================ EASY STATEMENTS (5)
S(AG, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The minimum support price for a crop is announced before its sowing season.",
   "The minimum support price is the price at which the government sells grain in ration shops."],
  ["किसी फ़सल का न्यूनतम समर्थन मूल्य उसके बुआई के मौसम से पहले घोषित किया जाता है।",
   "न्यूनतम समर्थन मूल्य वह क़ीमत है जिस पर सरकार राशन की दुकानों में अनाज बेचती है।"],
  T2, 0,
  "Only statement 1 is correct: announcing the price in advance helps farmers decide what to sow. Statement 2 is wrong: MSP is the price the government pays farmers; ration shops sell grain at a much lower issue price -- now free for most beneficiaries.",
  "केवल कथन 1 सही है: पहले से क़ीमत घोषित करने से किसानों को यह तय करने में मदद मिलती है कि क्या बोएँ। कथन 2 गलत है: MSP वह क़ीमत है जो सरकार किसानों को देती है; राशन की दुकानें बहुत कम निर्गम मूल्य पर अनाज बेचती हैं, जो अब अधिकांश लाभार्थियों के लिए मुफ़्त है।",
  f"{IED}.",
  "ag-msp-basics-easy")

S(AG, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Kisan Credit Cards give farmers short-term credit for their crop needs.",
   "Crop insurance protects farmers against losses caused by natural calamities."],
  ["किसान क्रेडिट कार्ड किसानों को उनकी फ़सल की आवश्यकताओं के लिए अल्पकालिक ऋण देते हैं।",
   "फ़सल बीमा किसानों को प्राकृतिक आपदाओं से होने वाले नुक़सान से बचाता है।"],
  T2, 2,
  "Both statements are correct. Credit lets farmers buy seeds and fertilisers before the harvest brings in money, and insurance pays out when drought, flood or pests destroy the crop.",
  "दोनों कथन सही हैं। ऋण से किसान फ़सल से पैसा आने से पहले बीज और उर्वरक ख़रीद पाते हैं, और सूखा, बाढ़ या कीट फ़सल नष्ट करें तो बीमा भुगतान करता है।",
  f"{IED}.",
  "ag-credit-insurance-easy")

S(AG, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Food Corporation of India stores foodgrains procured from farmers.",
   "The public distribution system sells grain at prices above the market price."],
  ["भारतीय खाद्य निगम किसानों से ख़रीदे गए खाद्यान्न का भंडारण करता है।",
   "सार्वजनिक वितरण प्रणाली बाज़ार भाव से ऊँची क़ीमतों पर अनाज बेचती है।"],
  T2, 0,
  "Only statement 1 is correct. Statement 2 is wrong: the PDS sells grain far below market prices -- and now free to most beneficiaries -- which is the whole point of the system.",
  "केवल कथन 1 सही है। कथन 2 गलत है: PDS बाज़ार भाव से कहीं कम क़ीमत पर, और अब अधिकांश लाभार्थियों को मुफ़्त, अनाज देती है; व्यवस्था का उद्देश्य ही यही है।",
  f"{DFPD}.",
  "ag-fci-pds-price-easy")

S(AG, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Agriculture contributes more than half of India's GDP.",
   "India imports most of the rice it consumes."],
  ["कृषि भारत के GDP में आधे से अधिक का योगदान करती है।",
   "भारत अपनी खपत का अधिकांश चावल आयात करता है।"],
  T2, 3,
  "Neither statement is correct. Agriculture's share of output has fallen to under a fifth, although it still employs a much larger share of workers. India grows far more rice than it eats and is the world's largest exporter of it.",
  "कोई भी कथन सही नहीं है। उत्पादन में कृषि का हिस्सा घटकर पाँचवें भाग से कम रह गया है, यद्यपि यह अब भी श्रमिकों के कहीं बड़े हिस्से को रोज़गार देती है। भारत अपनी खपत से कहीं अधिक चावल उगाता है और विश्व में इसका सबसे बड़ा निर्यातक है।",
  f"{IED}; Department of Commerce.",
  "ag-share-rice-easy")

S(AG, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Green Revolution mainly involved the spread of traditional seed varieties.",
   "Tractors and harvesters are examples of farm mechanisation."],
  ["हरित क्रांति में मुख्य रूप से पारंपरिक बीज किस्मों का प्रसार हुआ।",
   "ट्रैक्टर और हार्वेस्टर कृषि मशीनीकरण के उदाहरण हैं।"],
  T2, 1,
  "Only statement 2 is correct. Statement 1 is wrong: the Green Revolution rested on high-yielding varieties, together with irrigation, chemical fertilisers and assured prices.",
  "केवल कथन 2 सही है। कथन 1 गलत है: हरित क्रांति उच्च उपज वाली किस्मों (HYV) पर टिकी थी, साथ में सिंचाई, रासायनिक उर्वरक और सुनिश्चित क़ीमतें।",
  f"{IED}.",
  "ag-green-revolution-mechanisation-easy")

# ================================================================ HARD STATEMENTS (5)
S(AG, "hard", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["India banned exports of non-basmati white rice in 2023.",
   "Stock limits on traders can be imposed under the Essential Commodities Act.",
   "The Essential Commodities Act was repealed in 2020."],
  ["भारत ने 2023 में गैर-बासमती सफ़ेद चावल के निर्यात पर प्रतिबंध लगाया।",
   "आवश्यक वस्तु अधिनियम के तहत व्यापारियों पर भंडार सीमा (stock limits) लगाई जा सकती है।",
   "आवश्यक वस्तु अधिनियम 2020 में निरस्त कर दिया गया।"],
  C3, 1,
  "Statements 1 and 2 are correct: the ban of July 2023, lifted in 2024, and stock limits on wheat and pulses show how the government trades off farmers' prices against consumers' prices when inflation rises. "
  "Statement 3 is wrong: the Essential Commodities Act, 1955 is still in force. The 2020 amendment that would have removed most foodstuffs from regular stock limits was one of the three farm laws, and it was itself repealed in 2021.",
  "कथन 1 और 2 सही हैं: जुलाई 2023 का प्रतिबंध, जो 2024 में हटा, और गेहूँ तथा दालों पर भंडार सीमा दिखाती हैं कि मुद्रास्फीति बढ़ने पर सरकार किसानों की क़ीमतों और उपभोक्ताओं की क़ीमतों के बीच कैसे संतुलन बैठाती है। "
  "कथन 3 गलत है: आवश्यक वस्तु अधिनियम, 1955 अब भी लागू है। 2020 का संशोधन, जो अधिकांश खाद्य वस्तुओं को नियमित भंडार सीमा से बाहर कर देता, तीन कृषि क़ानूनों में से एक था, और वह स्वयं 2021 में निरस्त हो गया।",
  "Directorate General of Foreign Trade -- Notifications on rice exports (2023, 2024); Essential Commodities Act, 1955.",
  "ag-export-ban-eca")

S(AG, "hard", "Consider the following statements about PM-AASHA:",
  "PM-AASHA के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It brings together a Price Support Scheme, a Price Deficiency Payment Scheme and pilots of private procurement.",
   "Under price deficiency payment, farmers are paid the gap between the MSP and the market price without the government buying the crop.",
   "Under the Price Support Scheme, central agencies such as NAFED procure pulses, oilseeds and copra."],
  ["यह मूल्य समर्थन योजना, मूल्य न्यूनता भुगतान योजना और निजी ख़रीद के प्रायोगिक कार्यक्रमों को एक साथ लाती है।",
   "मूल्य न्यूनता भुगतान (price deficiency payment) में सरकार फ़सल ख़रीदे बिना किसानों को MSP और बाज़ार मूल्य के अंतर का भुगतान करती है।",
   "मूल्य समर्थन योजना के तहत NAFED जैसी केंद्रीय एजेंसियाँ दालें, तिलहन और खोपरा ख़रीदती हैं।"],
  C3, 2,
  "All three statements are correct. PM-AASHA (2018) was meant to extend price support beyond wheat and rice. Deficiency payments avoid the costs of storing grain, but they can push market prices down if traders expect the government to make up the gap -- a problem seen with Madhya Pradesh's Bhavantar scheme.",
  "तीनों कथन सही हैं। PM-AASHA (2018) का उद्देश्य गेहूँ और चावल से आगे मूल्य समर्थन का विस्तार करना था। न्यूनता भुगतान अनाज के भंडारण की लागत से बचाते हैं, पर यदि व्यापारी मानें कि अंतर सरकार भर देगी, तो वे बाज़ार भाव नीचे धकेल सकते हैं; मध्य प्रदेश की भावांतर योजना में यह समस्या दिखी।",
  f"{MOA} -- Pradhan Mantri Annadata Aay SanraksHan Abhiyan (PM-AASHA).",
  "ag-pm-aasha")

S(AG, "hard", "Consider the following statements about farm prices:",
  "कृषि क़ीमतों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The cobweb model explains cycles in farm prices that arise because farmers decide this season's output on the basis of last season's prices.",
   "Engel's law says that the share of food in household spending falls as income rises.",
   "The supply of most farm products is highly price-elastic in the short run."],
  ["मकड़जाल मॉडल (cobweb model) कृषि क़ीमतों के उन चक्रों को समझाता है जो इसलिए बनते हैं कि किसान इस मौसम का उत्पादन पिछले मौसम की क़ीमतों के आधार पर तय करते हैं।",
   "एंगेल का नियम कहता है कि आय बढ़ने के साथ घरेलू व्यय में भोजन का हिस्सा घटता है।",
   "अधिकांश कृषि उत्पादों की आपूर्ति अल्पकाल में क़ीमत के प्रति अत्यधिक लोचदार होती है।"],
  C3, 1,
  "Statements 1 and 2 are correct: a high onion price this year leads many farmers to plant onions, a glut follows and prices crash, and the cycle repeats. Engel's law is why farm incomes lag as economies grow: demand for food rises more slowly than income. "
  "Statement 3 is wrong: once a crop is sown, output cannot respond to price until the next season, so short-run supply is inelastic -- which is why small shocks cause large price swings.",
  "कथन 1 और 2 सही हैं: इस वर्ष प्याज़ की ऊँची क़ीमत से कई किसान प्याज़ बोते हैं, फिर भरमार होती है और क़ीमतें गिर जाती हैं, और चक्र दोहराता है। एंगेल का नियम ही कारण है कि अर्थव्यवस्था बढ़ने पर कृषि आय पीछे रह जाती है: भोजन की माँग आय से धीमी बढ़ती है। "
  "कथन 3 गलत है: फ़सल बोने के बाद उत्पादन अगले मौसम तक क़ीमत पर प्रतिक्रिया नहीं दे सकता, इसलिए अल्पकालिक आपूर्ति बेलोचदार होती है; इसीलिए छोटे झटके भी क़ीमतों में बड़े उतार-चढ़ाव लाते हैं।",
  f"{IED}; {ES}.",
  "ag-cobweb-engel")

S(AG, "hard", "Consider the following statements about agricultural credit:",
  "कृषि ऋण के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Cooperatives now provide the largest share of institutional credit to agriculture.",
   "Regional Rural Banks were set up on the recommendation of the Narasimham Working Group in the 1970s.",
   "NABARD's main business is lending directly to individual farmers."],
  ["सहकारी संस्थाएँ अब कृषि को संस्थागत ऋण का सबसे बड़ा हिस्सा देती हैं।",
   "क्षेत्रीय ग्रामीण बैंक 1970 के दशक में नरसिम्हम कार्य समूह की सिफ़ारिश पर स्थापित किए गए।",
   "NABARD का मुख्य काम व्यक्तिगत किसानों को सीधे ऋण देना है।"],
  C3, 0,
  "Only statement 2 is correct: RRBs date from 1975, to combine a cooperative's local feel with a commercial bank's resources. "
  "Statement 1 is wrong: cooperatives dominated farm credit in the early decades, but commercial banks now give roughly three-quarters of it, with cooperatives and RRBs sharing the rest. "
  "Statement 3 is wrong: NABARD is mainly a refinancing and development institution -- it lends to banks and cooperatives, which lend to farmers.",
  "केवल कथन 2 सही है: RRB 1975 से हैं, जो सहकारी संस्था की स्थानीय समझ को वाणिज्यिक बैंक के संसाधनों से जोड़ने के लिए बने। "
  "कथन 1 गलत है: शुरुआती दशकों में कृषि ऋण पर सहकारी संस्थाओं का प्रभुत्व था, पर अब वाणिज्यिक बैंक इसका लगभग तीन-चौथाई देते हैं, और शेष सहकारी संस्थाएँ और RRB बाँटते हैं। "
  "कथन 3 गलत है: NABARD मुख्य रूप से पुनर्वित्त और विकास संस्था है; यह बैंकों और सहकारी संस्थाओं को ऋण देता है, जो किसानों को ऋण देते हैं।",
  "Reserve Bank of India -- Report of the Internal Working Group to Review Agricultural Credit (2019); NABARD.",
  "ag-farm-credit-structure")

S(AG, "hard", "Consider the following statements about the leasing of farmland:",
  "कृषि भूमि को पट्टे पर देने के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Model Agricultural Land Leasing Act, 2016 was enacted by Parliament.",
   "Kerala and Jammu and Kashmir have been among the most liberal States in allowing tenancy.",
   "Most leasing of farmland in India is formally recorded in land records."],
  ["आदर्श कृषि भूमि पट्टा अधिनियम, 2016 संसद ने अधिनियमित किया।",
   "केरल और जम्मू-कश्मीर बटाईदारी (tenancy) की अनुमति देने में सबसे उदार राज्यों में रहे हैं।",
   "भारत में कृषि भूमि को पट्टे पर देने का अधिकांश भाग भूमि अभिलेखों में औपचारिक रूप से दर्ज होता है।"],
  C3, 3,
  "None of the statements is correct. Statement 1 is wrong: the 2016 Act is a model prepared by NITI Aayog for States to adopt, since land is a State subject. "
  "Statement 2 is wrong: Kerala and Jammu and Kashmir have banned leasing altogether, a legacy of land reforms meant to end absentee landlordism. "
  "Statement 3 is wrong: because many States ban or restrict leasing, most of it is oral and informal, so tenants cannot easily get crop loans, insurance or compensation for crop losses.",
  "कोई भी कथन सही नहीं है। कथन 1 गलत है: 2016 का अधिनियम NITI आयोग द्वारा राज्यों के अपनाने के लिए तैयार किया गया एक आदर्श क़ानून है, क्योंकि भूमि राज्य का विषय है। "
  "कथन 2 गलत है: केरल और जम्मू-कश्मीर ने पट्टेदारी पर पूरी तरह रोक लगाई है, जो अनुपस्थित ज़मींदारी समाप्त करने वाले भूमि सुधारों की विरासत है। "
  "कथन 3 गलत है: चूँकि कई राज्य पट्टेदारी पर रोक या प्रतिबंध लगाते हैं, इसका अधिकांश भाग मौखिक और अनौपचारिक है, इसलिए बटाईदार आसानी से फ़सल ऋण, बीमा या फ़सल हानि का मुआवज़ा नहीं पा सकते।",
  "NITI Aayog -- Model Agricultural Land Leasing Act, 2016 and report of the Expert Committee (T. Haque).",
  "ag-land-leasing-none")

# ================================================================ MEDIUM MCQs (5)
M(AG, "medium", "Which one of the following crops is NOT covered by the minimum support prices announced by the Centre?",
  "निम्नलिखित में से कौन-सी फ़सल केंद्र द्वारा घोषित न्यूनतम समर्थन मूल्यों में शामिल नहीं है?",
  ["Potato", "Copra", "Jute", "Niger seed"],
  ["आलू", "खोपरा", "जूट", "रामतिल (niger seed)"],
  0,
  "MSP covers cereals, pulses and oilseeds -- niger seed among them -- and the commercial crops jute and copra. Perishables such as potato and onion are not covered; their prices are handled through tools such as Operation Greens and market intervention schemes.",
  "MSP में अनाज, दालें और तिलहन, जिनमें रामतिल भी है, और वाणिज्यिक फ़सलें जूट और खोपरा शामिल हैं। आलू और प्याज़ जैसी जल्दी ख़राब होने वाली वस्तुएँ शामिल नहीं हैं; इनकी क़ीमतों को ऑपरेशन ग्रीन्स और बाज़ार हस्तक्षेप योजनाओं जैसे उपायों से संभाला जाता है।",
  f"{MOA} -- Commission for Agricultural Costs and Prices, Price Policy reports.",
  "ag-msp-not-covered")

M(AG, "medium", "'AGMARK' is a certification mark for:",
  "'एगमार्क' (AGMARK) किसका प्रमाणन चिह्न है?",
  ["grading of agricultural produce", "quality of electrical appliances such as fans and irons",
   "organically grown food exported to the European Union", "handloom products woven by registered weavers"],
  ["कृषि उपज की ग्रेडिंग", "पंखे और इस्त्री जैसे बिजली के उपकरणों की गुणवत्ता",
   "यूरोपीय संघ को निर्यात किया जाने वाला जैविक रूप से उगाया गया भोजन", "पंजीकृत बुनकरों द्वारा बुने गए हथकरघा उत्पाद"],
  0,
  "AGMARK, under the Agricultural Produce (Grading and Marking) Act, 1937, certifies the grade of products such as pulses, spices, ghee and honey, and is run by the Directorate of Marketing and Inspection. Electrical goods carry the BIS (ISI) mark, organic food the India Organic or Jaivik Bharat logo, and handloom goods the Handloom Mark.",
  "एगमार्क, कृषि उपज (श्रेणीकरण और चिह्नांकन) अधिनियम, 1937 के तहत, दालों, मसालों, घी और शहद जैसे उत्पादों की श्रेणी प्रमाणित करता है, और इसे विपणन और निरीक्षण निदेशालय चलाता है। बिजली के सामान पर BIS (ISI) चिह्न, जैविक भोजन पर इंडिया ऑर्गेनिक या जैविक भारत लोगो, और हथकरघा वस्तुओं पर हैंडलूम मार्क होता है।",
  f"{MOA} -- Directorate of Marketing and Inspection.",
  "ag-agmark")

M(AG, "medium", "The main aim of the 'One Nation One Ration Card' scheme is to:",
  "'एक राष्ट्र एक राशन कार्ड' योजना का मुख्य उद्देश्य है:",
  ["let ration card holders draw their grain from any fair price shop in India", "issue a separate ration card to every member of a household instead of one card per family",
   "replace ration cards with cash transfers for food in all the States of India", "fix a single price for foodgrains sold in open markets across the country"],
  ["राशन कार्ड धारकों को भारत की किसी भी उचित मूल्य की दुकान से अपना अनाज लेने देना", "प्रति परिवार एक कार्ड के बजाय परिवार के हर सदस्य को अलग राशन कार्ड जारी करना",
   "भारत के सभी राज्यों में राशन कार्डों के स्थान पर भोजन के लिए नकद हस्तांतरण लाना", "देश भर के खुले बाज़ारों में बिकने वाले खाद्यान्न के लिए एक ही क़ीमत तय करना"],
  0,
  "Portability, made possible by Aadhaar-seeded ration cards and electronic point-of-sale devices in shops, matters most for migrant workers, who can now collect grain where they work while their families draw the rest at home.",
  "सुवाह्यता (portability), जो आधार से जुड़े राशन कार्डों और दुकानों में इलेक्ट्रॉनिक पॉइंट-ऑफ़-सेल उपकरणों से संभव हुई, प्रवासी मज़दूरों के लिए सबसे महत्त्वपूर्ण है, जो अब काम की जगह पर अनाज ले सकते हैं जबकि उनके परिवार शेष घर पर लेते हैं।",
  f"{DFPD} -- One Nation One Ration Card.",
  "ag-onorc")

M(AG, "medium", "The Soil Health Card scheme gives farmers:",
  "मृदा स्वास्थ्य कार्ड योजना किसानों को क्या देती है?",
  ["information on the nutrients in their soil and the fertiliser it needs", "a loan against their land that can be used to buy seeds and fertilisers",
   "insurance that pays for crop losses caused by poor soil quality", "a certificate that allows them to sell their produce as organic"],
  ["उनकी मिट्टी में पोषक तत्वों और उसे आवश्यक उर्वरक की जानकारी", "उनकी भूमि पर ऋण, जिसका उपयोग बीज और उर्वरक ख़रीदने में हो सके",
   "ख़राब मिट्टी की गुणवत्ता से होने वाली फ़सल हानि के लिए बीमा", "एक प्रमाणपत्र, जो उन्हें अपनी उपज जैविक के रूप में बेचने देता है"],
  0,
  "Launched in 2015, the cards report a dozen parameters -- nitrogen, phosphorus, potassium, sulphur, micronutrients, pH and others -- and recommend balanced fertiliser use, to correct the overuse of urea that cheap prices encourage.",
  "2015 में शुरू हुए कार्ड लगभग एक दर्जन मानक, जैसे नाइट्रोजन, फ़ॉस्फ़ोरस, पोटैशियम, सल्फ़र, सूक्ष्म पोषक तत्व और pH, बताते हैं और संतुलित उर्वरक उपयोग की सिफ़ारिश करते हैं, ताकि सस्ती क़ीमतों से बढ़े यूरिया के अति-उपयोग को ठीक किया जा सके।",
  f"{MOA} -- Soil Health Card scheme.",
  "ag-soil-health-card")

M(AG, "medium", "Which one of the following is the largest of the Centre's major subsidies?",
  "निम्नलिखित में से कौन-सी केंद्र की प्रमुख सब्सिडियों में सबसे बड़ी है?",
  ["Food subsidy", "Fertiliser subsidy", "Petroleum subsidy", "Interest subsidy on crop loans"],
  ["खाद्य सब्सिडी", "उर्वरक सब्सिडी", "पेट्रोलियम सब्सिडी", "फ़सल ऋणों पर ब्याज सब्सिडी"],
  0,
  "The food subsidy -- the cost of buying, storing and moving grain and giving it free to over 80 crore people -- is about ₹2 lakh crore a year, ahead of the fertiliser subsidy. The petroleum subsidy, mostly for LPG for poor households, has become small since petrol and diesel prices were freed.",
  "खाद्य सब्सिडी, यानी अनाज ख़रीदने, भंडारित करने, ढोने और 80 करोड़ से अधिक लोगों को मुफ़्त देने की लागत, लगभग ₹2 लाख करोड़ प्रति वर्ष है, जो उर्वरक सब्सिडी से आगे है। पेट्रोलियम सब्सिडी, जो अधिकतर ग़रीब परिवारों के LPG के लिए है, पेट्रोल और डीज़ल की क़ीमतें मुक्त होने के बाद छोटी हो गई है।",
  "Ministry of Finance -- Union Budget 2025-26, Expenditure Budget.",
  "ag-largest-subsidy")

# ================================================================ EASY MCQs (2)
M(AG, "easy", "The Green Revolution in India first brought large gains in the output of:",
  "भारत में हरित क्रांति से सबसे पहले किसके उत्पादन में बड़ी वृद्धि हुई?",
  ["Wheat", "Pulses", "Oilseeds", "Cotton"],
  ["गेहूँ", "दालें", "तिलहन", "कपास"],
  0,
  "High-yielding dwarf wheat, spread in Punjab, Haryana and western Uttar Pradesh from the mid-1960s, transformed wheat output first; rice followed. Pulses and oilseeds largely missed out.",
  "1960 के दशक के मध्य से पंजाब, हरियाणा और पश्चिमी उत्तर प्रदेश में फैली उच्च उपज वाली बौनी गेहूँ किस्मों ने सबसे पहले गेहूँ उत्पादन को बदला; चावल बाद में आया। दालें और तिलहन बड़े पैमाने पर पीछे रह गए।",
  f"{IED}.",
  "ag-green-revolution-wheat-easy")

M(AG, "easy", "Which one of the following is an activity allied to agriculture?",
  "निम्नलिखित में से कौन-सी गतिविधि कृषि से संबद्ध है?",
  ["Dairy farming", "Textile weaving", "Software development", "Steel making"],
  ["डेयरी फ़ार्मिंग", "वस्त्र बुनाई", "सॉफ़्टवेयर विकास", "इस्पात निर्माण"],
  0,
  "Livestock, including dairying, along with fisheries and forestry, is counted with agriculture as an allied activity. Weaving and steel making are manufacturing, and software is a service.",
  "पशुधन, जिसमें डेयरी भी है, मत्स्य पालन और वानिकी के साथ कृषि की संबद्ध गतिविधि के रूप में गिना जाता है। बुनाई और इस्पात निर्माण विनिर्माण हैं, और सॉफ़्टवेयर एक सेवा है।",
  f"{IED}.",
  "ag-allied-activity-easy")

# ================================================================ HARD MCQ (1)
M(AG, "hard", "For a crop, the paid-out cost (A2) is ₹1,200 per quintal and the imputed value of family labour is ₹300 per quintal. Under the rule followed since 2018-19 of fixing MSP at least one-and-a-half times the cost of production, the MSP must be at least:",
  "किसी फ़सल के लिए भुगतान की गई लागत (A2) ₹1,200 प्रति क्विंटल और पारिवारिक श्रम का आरोपित मूल्य ₹300 प्रति क्विंटल है। 2018-19 से MSP को उत्पादन लागत के कम से कम डेढ़ गुना पर तय करने के नियम के तहत MSP कम से कम कितना होना चाहिए?",
  ["₹2,250", "₹1,800", "₹1,950", "₹3,000"],
  ["₹2,250", "₹1,800", "₹1,950", "₹3,000"],
  0,
  "The cost used is A2+FL -- paid-out costs plus the imputed value of family labour -- so 1.5 x (1,200 + 300) = ₹2,250. Using A2 alone gives ₹1,800, and doubling gives ₹3,000. Farm groups argue that the base should instead be C2, which also counts rent on owned land and interest on owned capital, as the National Commission on Farmers recommended.",
  "प्रयुक्त लागत A2+FL है, यानी भुगतान की गई लागत और पारिवारिक श्रम का आरोपित मूल्य, इसलिए 1.5 x (1,200 + 300) = ₹2,250। केवल A2 लेने पर ₹1,800 और दोगुना करने पर ₹3,000 आता है। किसान संगठनों का तर्क है कि आधार C2 होना चाहिए, जिसमें अपनी भूमि का किराया और अपनी पूँजी पर ब्याज भी शामिल है, जैसी राष्ट्रीय किसान आयोग ने सिफ़ारिश की थी।",
  f"{MOA} -- Commission for Agricultural Costs and Prices; Union Budget 2018-19.",
  "ag-msp-numerical")

# ================================================================ STATEMENT-I/II (medium 3, easy 1, hard 1)
A(AG, "medium",
  "Farmers in Punjab and Haryana grow mostly wheat and paddy.",
  "पंजाब और हरियाणा के किसान मुख्य रूप से गेहूँ और धान उगाते हैं।",
  "Open-ended procurement at MSP makes wheat and paddy less risky than other crops in these States.",
  "MSP पर खुली (open-ended) ख़रीद इन राज्यों में गेहूँ और धान को अन्य फ़सलों से कम जोखिम वाला बनाती है।",
  0,
  "Both statements are correct and Statement-II explains Statement-I. Assured purchase at a known price, along with free power and canal water, removes most of the price risk from wheat and paddy, so farmers have little reason to switch -- even as paddy drains the region's groundwater.",
  "दोनों कथन सही हैं और कथन-II कथन-I की व्याख्या करता है। ज्ञात क़ीमत पर सुनिश्चित ख़रीद, मुफ़्त बिजली और नहर के पानी के साथ, गेहूँ और धान से मूल्य जोखिम का अधिकांश भाग हटा देती है, इसलिए किसानों के पास फ़सल बदलने का कम कारण रहता है, भले ही धान क्षेत्र के भूजल को सुखा रहा हो।",
  f"{ES}; Commission for Agricultural Costs and Prices.",
  "ag-procurement-cropping-pattern")

A(AG, "medium",
  "India is the world's largest producer of milk.",
  "भारत विश्व का सबसे बड़ा दुग्ध उत्पादक है।",
  "Milk is not covered by the minimum support price system.",
  "दूध न्यूनतम समर्थन मूल्य प्रणाली में शामिल नहीं है।",
  1,
  "Both statements are correct, but Statement-II does not explain Statement-I. India produces about a quarter of the world's milk, from millions of small herds linked to cooperatives and private dairies that pay farmers on the basis of fat and quality. The absence of MSP for milk is a separate fact and says nothing about why output is so large.",
  "दोनों कथन सही हैं, पर कथन-II कथन-I की व्याख्या नहीं करता। भारत विश्व के लगभग एक-चौथाई दूध का उत्पादन करता है, जो सहकारी संस्थाओं और निजी डेयरियों से जुड़े लाखों छोटे झुंडों से आता है, जो वसा और गुणवत्ता के आधार पर किसानों को भुगतान करती हैं। दूध के लिए MSP न होना एक अलग तथ्य है और यह नहीं बताता कि उत्पादन इतना बड़ा क्यों है।",
  "Department of Animal Husbandry and Dairying -- Basic Animal Husbandry Statistics; FAO.",
  "ag-milk-largest-no-msp")

A(AG, "medium",
  "Shifting part of the paddy area to pulses and oilseeds can help conserve groundwater in north-west India.",
  "धान के क्षेत्र का एक भाग दालों और तिलहन की ओर मोड़ना उत्तर-पश्चिम भारत में भूजल बचाने में मदद कर सकता है।",
  "Pulses need more water than paddy.",
  "दालों को धान से अधिक पानी की आवश्यकता होती है।",
  2,
  "Statement-I is correct but Statement-II is incorrect. Paddy is among the thirstiest crops -- a kilogram of rice can take several thousand litres of water -- while pulses and most oilseeds need far less, and pulses also fix nitrogen in the soil. That is why crop diversification is part of the answer to falling water tables.",
  "कथन-I सही है पर कथन-II गलत है। धान सबसे अधिक पानी लेने वाली फ़सलों में है; एक किलोग्राम चावल में कई हज़ार लीटर पानी लग सकता है, जबकि दालों और अधिकांश तिलहनों को कहीं कम पानी चाहिए, और दालें मिट्टी में नाइट्रोजन भी स्थिर करती हैं। इसीलिए गिरते जल-स्तर का एक उत्तर फ़सल विविधीकरण है।",
  f"{ES}; Central Ground Water Board.",
  "ag-diversification-water")

A(AG, "easy",
  "Irrigation allows farmers to grow more than one crop a year.",
  "सिंचाई किसानों को एक वर्ष में एक से अधिक फ़सल उगाने देती है।",
  "It supplies water to fields in seasons when there is little rain.",
  "यह उन मौसमों में खेतों को पानी देती है जब बहुत कम वर्षा होती है।",
  0,
  "Both statements are correct and Statement-II explains Statement-I: with water available outside the monsoon, a second or even third crop becomes possible.",
  "दोनों कथन सही हैं और कथन-II कथन-I की व्याख्या करता है: मानसून के बाहर पानी उपलब्ध होने से दूसरी या तीसरी फ़सल भी संभव हो जाती है।",
  f"{IED}.",
  "ag-irrigation-multiple-cropping-easy")

A(AG, "hard",
  "Higher minimum support prices for wheat and rice have no effect on food inflation.",
  "गेहूँ और चावल के ऊँचे न्यूनतम समर्थन मूल्यों का खाद्य मुद्रास्फीति पर कोई प्रभाव नहीं पड़ता।",
  "The Commission for Agricultural Costs and Prices also considers the terms of trade between agriculture and the rest of the economy when it recommends MSPs.",
  "MSP की सिफ़ारिश करते समय कृषि लागत और मूल्य आयोग कृषि और शेष अर्थव्यवस्था के बीच व्यापार की शर्तों पर भी विचार करता है।",
  3,
  "Statement-I is incorrect but Statement-II is correct. MSP sets a floor for market prices of wheat and rice, and cereals carry a large weight in the consumer price index, so large MSP increases feed into food inflation -- one reason the RBI watches them. The CACP weighs costs, demand and supply, world prices, inter-crop parity and the terms of trade for agriculture.",
  "कथन-I गलत है पर कथन-II सही है। MSP गेहूँ और चावल के बाज़ार भाव की न्यूनतम सीमा तय करता है, और उपभोक्ता मूल्य सूचकांक में अनाज का भार बड़ा है, इसलिए MSP में बड़ी वृद्धि खाद्य मुद्रास्फीति में जुड़ती है; यह एक कारण है कि RBI इन पर नज़र रखता है। CACP लागत, माँग और आपूर्ति, विश्व क़ीमतों, फ़सलों के बीच समता और कृषि के लिए व्यापार की शर्तों पर विचार करता है।",
  f"Commission for Agricultural Costs and Prices -- terms of reference; Reserve Bank of India -- Monetary Policy Report.",
  "ag-msp-inflation-tot")

# ================================================================ PAIRS (medium 1)
P(AG, "medium", "Consider the following pairs of schemes and their purposes:",
  "योजनाओं और उनके उद्देश्यों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["PM Krishi Sinchayee Yojana : Expanding irrigation and water-use efficiency", "PM-PRANAM : Reducing the use of chemical fertilisers",
   "Agriculture Infrastructure Fund : Credit for post-harvest and farm-gate infrastructure", "PM Kisan Maandhan Yojana : Interest-free loans for buying tractors"],
  ["PM कृषि सिंचाई योजना : सिंचाई और जल-उपयोग दक्षता का विस्तार", "PM-PRANAM : रासायनिक उर्वरकों का उपयोग घटाना",
   "कृषि अवसंरचना कोष : फ़सल-कटाई के बाद और खेत-स्तरीय अवसंरचना के लिए ऋण", "PM किसान मानधन योजना : ट्रैक्टर ख़रीदने के लिए ब्याज-मुक्त ऋण"],
  2,
  "Pairs 1, 2 and 3 are correct: PMKSY's motto is 'Har Khet Ko Pani' and 'More Crop per Drop'; PM-PRANAM (2023) rewards States that cut chemical fertiliser use with a share of the subsidy saved; and the ₹1 lakh crore Agriculture Infrastructure Fund (2020) gives interest subvention on loans for warehouses, cold storage and processing. "
  "Pair 4 is wrong: PM Kisan Maandhan is a voluntary, contributory pension scheme giving small and marginal farmers ₹3,000 a month after the age of 60.",
  "युग्म 1, 2 और 3 सही हैं: PMKSY का ध्येय 'हर खेत को पानी' और 'प्रति बूँद अधिक फ़सल' है; PM-PRANAM (2023) रासायनिक उर्वरक का उपयोग घटाने वाले राज्यों को बची सब्सिडी का एक हिस्सा देकर पुरस्कृत करता है; और ₹1 लाख करोड़ का कृषि अवसंरचना कोष (2020) गोदामों, शीत भंडारों और प्रसंस्करण के लिए ऋणों पर ब्याज अनुदान देता है। "
  "युग्म 4 गलत है: PM किसान मानधन एक स्वैच्छिक, अंशदायी पेंशन योजना है जो छोटे और सीमांत किसानों को 60 वर्ष की आयु के बाद ₹3,000 प्रति माह देती है।",
  f"{MOA}; Department of Fertilizers -- PM-PRANAM.",
  "ag-schemes-pairs")

if __name__ == "__main__":
    write("econ_l2_t18_agriculture.sql")
