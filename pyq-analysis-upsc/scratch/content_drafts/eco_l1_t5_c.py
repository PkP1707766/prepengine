# -*- coding: utf-8 -*-
"""Level 1 · Test 5 (Economy, NCERT Foundation) -- part C: Agriculture & Food Economy (13), Inclusive Growth, Welfare
& Demography (4) and Growth, Development, Poverty & Planning (3) (upsc_l1_cell_targets.mjs 5).
Agriculture: easy MCQ 1, easy statement 2, easy Statement-I/II 1, medium MCQ 2, medium statement 4, medium
Statement-I/II 1, hard statement 1, hard Statement-I/II 1. Inclusive: easy statement 1, easy pairs 1, medium
statement 1, hard pairs 1. Growth: easy statement 1, medium statement 1, hard pairs 1.
The angle is NCERT Class IX (The Story of Village Palampur, Food Security, Poverty as a Challenge), Class X
(Development) and Class XI Indian Economic Development (planning, land reforms, the Green Revolution, rural
marketing, organic farming, human capital, employment, poverty). Level-2 facts are not repeated (MSP and procurement,
FCI and PDS pricing, buffer norms, ONORC, PM-KISAN, PMFBY, KCC, eNAM, FPOs, irrigation and multiple cropping, the Green
Revolution's wheat bias, land leasing, poverty-line committees, dependency ratio, IMR/MMR, Jan Dhan, Mudra, PMAY, the
social-security pairs, Plans and the 1950-90 strategy; NFSA and Antyodaya in Level-2 Polity). MCQ keys are pinned."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Economy"
d.REQUIRE_CRAFT = True
AG = "Agriculture & Food Economy"
IG = "Inclusive Growth, Welfare & Demography"
GD = "Growth, Development, Poverty & Planning"
EC9 = "NCERT Class IX, Economics"
EC10 = "NCERT Class X, Economics -- Understanding Economic Development"
IED = "NCERT Class XI, Economics -- Indian Economic Development"

# ================================================================ AGRICULTURE (13)
# ---------------------------------------------------------------- easy MCQ (1)
M(AG, "easy", "In 'The Story of Village Palampur', tools, machines and buildings that can be used in production over many years are called",
  "'पालमपुर गाँव की कहानी' में उत्पादन में कई वर्षों तक प्रयुक्त होने वाले औज़ार, मशीनें और भवन क्या कहलाते हैं?",
  ["fixed capital", "working capital", "human capital", "natural capital"],
  ["स्थायी पूँजी", "कार्यशील पूँजी", "मानव पूँजी", "प्राकृतिक पूँजी"],
  0,
  "Production needs land, labour, physical capital and human capital (the knowledge and enterprise to put the others together). Physical capital is of two kinds: fixed capital -- tools, machines, buildings -- used over many years, "
  "and working capital -- raw materials such as seeds, fertiliser and yarn, and money in hand -- which is used up in a single round of production.",
  "उत्पादन के लिए भूमि, श्रम, भौतिक पूँजी और मानव पूँजी (अन्य को एक साथ लगाने का ज्ञान और उद्यम) चाहिए। भौतिक पूँजी दो प्रकार की है: स्थायी पूँजी -- औज़ार, मशीनें, भवन -- जो कई वर्षों तक प्रयुक्त होती है, "
  "और कार्यशील पूँजी -- बीज, उर्वरक और सूत जैसे कच्चे माल, और हाथ में नक़दी -- जो उत्पादन के एक ही चक्र में ख़र्च हो जाती है।",
  f"{EC9} (The Story of Village Palampur).",
  "l1-eco-palampur-fixed-capital", pos=3, craft="recall")

# ---------------------------------------------------------------- easy statement (2)
S(AG, "easy", "Consider the following statements about the dimensions of food security:",
  "खाद्य सुरक्षा के आयामों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Availability of food covers production within the country, imports and the previous years' stock in government granaries.",
   "Accessibility means that food is within reach of every person.",
   "Affordability means that a person has enough money to buy sufficient, safe and nutritious food to meet dietary needs."],
  ["खाद्य की उपलब्धता में देश के भीतर उत्पादन, आयात और सरकारी अन्न भंडारों में पिछले वर्षों का भंडार शामिल है।",
   "पहुँच (accessibility) का अर्थ है कि खाद्य हर व्यक्ति की पहुँच में हो।",
   "सामर्थ्य (affordability) का अर्थ है कि व्यक्ति के पास अपनी आहार संबंधी आवश्यकताएँ पूरी करने के लिए पर्याप्त, सुरक्षित और पौष्टिक भोजन ख़रीदने भर का धन हो।"],
  C3, 2,
  "All three statements are correct. A country is food-secure only when all three hold for all its people at all times, so plentiful granaries are not enough if food does not reach remote areas or the poor cannot pay for it. "
  "Food security is most at risk during disasters such as droughts and floods, when production falls and prices rise.",
  "तीनों कथन सही हैं। कोई देश तभी खाद्य-सुरक्षित है जब ये तीनों उसके सभी लोगों के लिए हर समय पूरे हों, इसलिए भरे हुए अन्न भंडार पर्याप्त नहीं, यदि भोजन दूर-दराज़ के क्षेत्रों तक न पहुँचे या ग़रीब उसे न ख़रीद सकें। "
  "सूखे और बाढ़ जैसी आपदाओं के दौरान, जब उत्पादन गिरता और कीमतें बढ़ती हैं, खाद्य सुरक्षा सबसे अधिक संकट में होती है।",
  f"{EC9} (Food Security in India).",
  "l1-eco-food-security-dimensions", craft="recall")

S(AG, "easy", "Consider the following statements about food insecurity in India:",
  "भारत में खाद्य असुरक्षा के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["In rural areas, the worst affected include landless people, traditional artisans, petty self-employed workers and destitutes.",
   "Food insecurity is spread evenly across all the States of India."],
  ["ग्रामीण क्षेत्रों में सबसे अधिक प्रभावितों में भूमिहीन लोग, परंपरागत दस्तकार, छोटे स्वरोज़गार वाले श्रमिक और निराश्रित शामिल हैं।",
   "खाद्य असुरक्षा भारत के सभी राज्यों में समान रूप से फैली है।"],
  T2, 0,
  "Only statement 1 is correct; in urban areas, the food-insecure are largely families whose working members are in ill-paid occupations and the casual labour market. Social composition matters too: scheduled castes, scheduled tribes and some backward castes with poor land are more prone to food insecurity. "
  "Statement 2 is wrong: the food-insecure are concentrated in economically backward States with high poverty, tribal and remote regions, and areas prone to natural disasters.",
  "केवल कथन 1 सही है; नगरीय क्षेत्रों में खाद्य-असुरक्षित अधिकतर वे परिवार हैं जिनके कमाने वाले सदस्य कम मज़दूरी वाले कामों और अनियत श्रम बाज़ार में हैं। सामाजिक संरचना भी मायने रखती है: अनुसूचित जातियाँ, अनुसूचित जनजातियाँ और कमज़ोर भूमि वाली कुछ पिछड़ी जातियाँ खाद्य असुरक्षा के प्रति अधिक संवेदनशील हैं। "
  "कथन 2 गलत है: खाद्य-असुरक्षित लोग ऊँची ग़रीबी वाले आर्थिक रूप से पिछड़े राज्यों, जनजातीय और दूरस्थ क्षेत्रों, और प्राकृतिक आपदा-प्रवण क्षेत्रों में केंद्रित हैं।",
  f"{EC9} (Food Security in India).",
  "l1-eco-who-are-food-insecure", craft="precision")

# ---------------------------------------------------------------- easy Statement-I/II (1)
A(AG, "easy",
  "Most small farmers in Palampur have to borrow money to arrange the working capital for cultivation.",
  "पालमपुर के अधिकांश छोटे किसानों को खेती की कार्यशील पूँजी जुटाने के लिए उधार लेना पड़ता है।",
  "They have little surplus left over from earlier harvests to pay for seeds, fertilisers and pesticides.",
  "बीज, उर्वरक और कीटनाशक का ख़र्च चुकाने के लिए उनके पास पिछली फ़सलों से बहुत कम अधिशेष बचता है।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I. Small farmers borrow from large farmers, village moneylenders or traders who supply inputs, often at high rates of interest and sometimes on the condition that the crop is sold to the lender at a low price; "
  "medium and large farmers, by contrast, sell their surplus and can save to finance the next season themselves.",
  "दोनों कथन सही हैं, और कथन-II कथन-I की व्याख्या करता है। छोटे किसान बड़े किसानों, गाँव के साहूकारों या आदान बेचने वाले व्यापारियों से, प्रायः ऊँचे ब्याज पर और कभी-कभी इस शर्त पर उधार लेते हैं कि फ़सल ऋणदाता को कम कीमत पर बेची जाएगी; "
  "इसके विपरीत, मध्यम और बड़े किसान अपना अधिशेष बेचते हैं और अगले मौसम का ख़र्च स्वयं जुटाने के लिए बचत कर सकते हैं।",
  f"{EC9} (The Story of Village Palampur).",
  "l1-eco-palampur-small-farmers-borrow", craft="inference")

# ---------------------------------------------------------------- medium MCQ (2)
M(AG, "medium", "The portion of agricultural produce that farmers sell in the market, after meeting their own needs, is called",
  "अपनी आवश्यकताएँ पूरी करने के बाद किसान कृषि उपज का जो भाग बाज़ार में बेचते हैं, वह क्या कहलाता है?",
  ["marketed surplus", "buffer stock", "procurement quota", "subsistence output"],
  ["विपणित अधिशेष (marketed surplus)", "बफ़र स्टॉक", "प्रापण कोटा", "निर्वाह उत्पादन"],
  0,
  "Marketed surplus is the part of the produce that reaches the market. The Green Revolution raised it substantially, because higher yields left farmers with more to sell, which let the government procure grain to build the stocks needed for food security. "
  "A larger marketed surplus also helped keep food prices in check as demand grew.",
  "विपणित अधिशेष उपज का वह भाग है जो बाज़ार तक पहुँचता है। हरित क्रांति ने इसे काफ़ी बढ़ाया, क्योंकि ऊँची उपज से किसानों के पास बेचने को अधिक रहा, जिससे सरकार खाद्य सुरक्षा के लिए आवश्यक भंडार बनाने हेतु अनाज ख़रीद सकी। "
  "बड़े विपणित अधिशेष ने माँग बढ़ने के साथ खाद्य कीमतों को नियंत्रण में रखने में भी मदद की।",
  f"{IED} (Indian Economy 1950-1990).",
  "l1-eco-marketed-surplus", pos=1, craft="recall")

M(AG, "medium", "A network of NGOs setting up grain banks in different regions of Maharashtra, as an example of community action for food security, was facilitated by",
  "खाद्य सुरक्षा के लिए सामुदायिक प्रयास के उदाहरण के रूप में, महाराष्ट्र के विभिन्न क्षेत्रों में अनाज बैंक स्थापित करने वाले गैर-सरकारी संगठनों का नेटवर्क किसने सुगम बनाया?",
  ["the Academy of Development Science", "the Food Corporation of India", "the National Dairy Development Board", "the Indian Council of Agricultural Research"],
  ["एकेडमी ऑफ़ डेवलपमेंट साइंस (ADS)", "भारतीय खाद्य निगम", "राष्ट्रीय डेयरी विकास बोर्ड", "भारतीय कृषि अनुसंधान परिषद"],
  0,
  "NCERT cites the Academy of Development Science (ADS), which helped NGOs set up grain banks and trained them in running them, and which worked to have the idea taken up in government policy. "
  "It sits beside other examples of cooperatives in food security, such as the cooperative ration shops of Tamil Nadu, Mother Dairy in Delhi and Amul in Gujarat.",
  "NCERT एकेडमी ऑफ़ डेवलपमेंट साइंस (ADS) का उल्लेख करता है, जिसने गैर-सरकारी संगठनों को अनाज बैंक स्थापित करने में मदद की और उन्हें चलाने का प्रशिक्षण दिया, और इस विचार को सरकारी नीति में अपनवाने का प्रयास किया। "
  "यह खाद्य सुरक्षा में सहकारी समितियों के अन्य उदाहरणों के साथ है, जैसे तमिलनाडु की सहकारी राशन दुकानें, दिल्ली में मदर डेयरी और गुजरात में अमूल।",
  f"{EC9} (Food Security in India).",
  "l1-eco-ads-grain-banks-maharashtra", pos=3, craft="precision")

# ---------------------------------------------------------------- medium statement (4)
S(AG, "medium", "Consider the following statements about the Green Revolution in India:",
  "भारत में हरित क्रांति के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["In its first phase, from about the mid-1960s to the mid-1970s, high-yielding seeds were used mainly in the more affluent States such as Punjab, Andhra Pradesh and Tamil Nadu.",
   "In its second phase, from about the mid-1970s to the mid-1980s, the technology spread to a larger number of States and to more crops.",
   "It raised output mainly by bringing more land under cultivation."],
  ["इसके पहले चरण में, लगभग 1960 के दशक के मध्य से 1970 के दशक के मध्य तक, अधिक उपज वाले बीजों का उपयोग मुख्यतः पंजाब, आंध्र प्रदेश और तमिलनाडु जैसे अधिक समृद्ध राज्यों में हुआ।",
   "इसके दूसरे चरण में, लगभग 1970 के दशक के मध्य से 1980 के दशक के मध्य तक, यह तकनीक अधिक राज्यों और अधिक फ़सलों तक फैली।",
   "इसने उत्पादन मुख्यतः अधिक भूमि को खेती के अंतर्गत लाकर बढ़ाया।"],
  C3, 1,
  "Statements 1 and 2 are correct. Statement 3 is wrong: the Green Revolution raised productivity -- output per hectare -- through high-yielding seeds used with fertilisers, pesticides and assured water. "
  "Because these inputs cost money, there were fears that only rich farmers would gain; the government limited this by giving small farmers loans at low interest and subsidising inputs, and research institutes helped control pests.",
  "कथन 1 और 2 सही हैं। कथन 3 गलत है: हरित क्रांति ने उर्वरकों, कीटनाशकों और सुनिश्चित जल के साथ प्रयुक्त अधिक उपज वाले बीजों से उत्पादकता -- प्रति हेक्टेयर उत्पादन -- बढ़ाई। "
  "चूँकि इन आदानों में धन लगता था, आशंका थी कि केवल अमीर किसानों को लाभ होगा; सरकार ने छोटे किसानों को कम ब्याज पर ऋण देकर और आदानों पर सब्सिडी देकर इसे सीमित किया, और अनुसंधान संस्थानों ने कीटों के नियंत्रण में मदद की।",
  f"{IED} (Indian Economy 1950-1990).",
  "l1-eco-green-revolution-two-phases", craft="precision")

S(AG, "medium", "Consider the following alternative channels through which farmers can sell directly to consumers, and the regions where they are found:",
  "उन वैकल्पिक माध्यमों पर विचार कीजिए जिनसे किसान सीधे उपभोक्ताओं को बेच सकते हैं, और जिन क्षेत्रों में वे मिलते हैं:",
  ["'Apni Mandi' in Punjab, Haryana and Rajasthan.",
   "'Hadaspar Mandi' in Pune.",
   "'Rythu Bazars', vegetable and fruit markets, in Andhra Pradesh and Telangana.",
   "'Uzhavar Sandhais', farmers' markets, in Tamil Nadu."],
  ["पंजाब, हरियाणा और राजस्थान में 'अपनी मंडी'।",
   "पुणे में 'हडपसर मंडी'।",
   "आंध्र प्रदेश और तेलंगाना में सब्ज़ियों और फलों के बाज़ार, 'रायतु बाज़ार'।",
   "तमिलनाडु में किसानों के बाज़ार, 'उझावर संधई'।"],
  C4, 3,
  "All four are correctly placed. By cutting out middlemen, such markets raise the farmer's share of the price the consumer pays. "
  "NCERT also notes that national and multinational fast-food chains increasingly contract with farmers to grow vegetables and fruit of the required quality, providing seeds and inputs and assuring purchase at pre-decided prices.",
  "चारों सही स्थान पर हैं। बिचौलियों को हटाकर ऐसे बाज़ार उपभोक्ता द्वारा चुकाई कीमत में किसान का हिस्सा बढ़ाते हैं। "
  "NCERT यह भी बताता है कि राष्ट्रीय और बहुराष्ट्रीय फ़ास्ट-फ़ूड शृंखलाएँ बढ़ती संख्या में किसानों से आवश्यक गुणवत्ता की सब्ज़ियाँ और फल उगाने के अनुबंध करती हैं, बीज और आदान देती हैं और पहले से तय कीमतों पर ख़रीद का आश्वासन देती हैं।",
  f"{IED} (Rural Development).",
  "l1-eco-alternative-marketing-channels", craft="recall")

S(AG, "medium", "Consider the following statements about hunger in India:",
  "भारत में भूख के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Chronic hunger results from diets that are persistently inadequate in quantity and/or quality.",
   "Seasonal hunger is found only in rural areas.",
   "The proportion of people facing chronic and seasonal hunger in India has risen since the 1980s."],
  ["दीर्घकालिक (chronic) भूख उन आहारों का परिणाम है जो मात्रा और/या गुणवत्ता में लगातार अपर्याप्त रहते हैं।",
   "मौसमी भूख केवल ग्रामीण क्षेत्रों में मिलती है।",
   "भारत में दीर्घकालिक और मौसमी भूख झेलने वालों का अनुपात 1980 के दशक से बढ़ा है।"],
  C3, 0,
  "Only statement 1 is correct. Statement 2 is wrong: seasonal hunger is linked to the cycles of growing and harvesting food, and so is common in rural areas, but it is also found in towns, where casual labourers have work only part of the year -- construction work, for instance, stops in the rainy season. "
  "Statement 3 is wrong: NCERT notes that both chronic and seasonal hunger have declined in India.",
  "केवल कथन 1 सही है। कथन 2 गलत है: मौसमी भूख भोजन उगाने और काटने के चक्रों से जुड़ी है, इसलिए ग्रामीण क्षेत्रों में आम है, पर यह नगरों में भी मिलती है, जहाँ अनियत श्रमिकों को वर्ष के केवल कुछ भाग में काम मिलता है -- जैसे वर्षा ऋतु में निर्माण कार्य रुक जाता है। "
  "कथन 3 गलत है: NCERT के अनुसार भारत में दीर्घकालिक और मौसमी, दोनों तरह की भूख घटी है।",
  f"{EC9} (Food Security in India).",
  "l1-eco-chronic-seasonal-hunger", craft="precision")

S(AG, "medium", "Consider the following statements about the evolution of the public distribution of food in India:",
  "भारत में खाद्य के सार्वजनिक वितरण के विकास के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Rationing in India dates back to the 1940s, against the backdrop of the Bengal famine.",
   "The rationing system was revived in the 1960s, during an acute food shortage before the Green Revolution.",
   "The Targeted Public Distribution System, adopted in 1997, was meant to follow the principle of targeting the poor in all areas."],
  ["भारत में राशनिंग 1940 के दशक में बंगाल के अकाल की पृष्ठभूमि में आरंभ हुई।",
   "राशन व्यवस्था 1960 के दशक में, हरित क्रांति से पहले की तीव्र खाद्य कमी के दौरान, फिर से शुरू की गई।",
   "1997 में अपनाई गई लक्षित सार्वजनिक वितरण प्रणाली का उद्देश्य सभी क्षेत्रों के ग़रीबों को लक्षित करने के सिद्धांत का पालन करना था।"],
  C3, 2,
  "All three statements are correct. The Bengal famine of 1943 is the most devastating famine India has known, killing about thirty lakh people. "
  "Until 1992 the PDS was universal; the Revamped PDS of 1992 focused on remote and backward blocks, and the targeted system of 1997 introduced different prices for poor and non-poor households.",
  "तीनों कथन सही हैं। 1943 का बंगाल का अकाल भारत का सबसे विनाशकारी अकाल था, जिसमें लगभग तीस लाख लोग मारे गए। "
  "1992 तक PDS सार्वभौमिक था; 1992 की पुनर्गठित PDS ने दूरस्थ और पिछड़े प्रखंडों पर ध्यान दिया, और 1997 की लक्षित प्रणाली ने ग़रीब और ग़ैर-ग़रीब परिवारों के लिए अलग कीमतें लागू कीं।",
  f"{EC9} (Food Security in India).",
  "l1-eco-pds-history-rationing", craft="linkage")

# ---------------------------------------------------------------- medium Statement-I/II (1)
A(AG, "medium",
  "Since the early 1970s, India has avoided famine even in years of adverse weather.",
  "1970 के दशक के आरंभ से, प्रतिकूल मौसम वाले वर्षों में भी भारत अकाल से बचा रहा है।",
  "India has not faced a severe drought since the early 1970s.",
  "1970 के दशक के आरंभ से भारत ने कोई गंभीर सूखा नहीं झेला है।",
  2,
  "Statement-I is correct but Statement-II is incorrect. India has faced severe droughts since then -- in 1987, 2002 and 2009, among others; famine was avoided because of self-sufficiency in food grains after the Green Revolution and a food security system of buffer stocks and public distribution that moves grain to where it is needed. "
  "Droughts reduce output, but famine -- widespread starvation and deaths -- results when food is not available or affordable to people over a large area.",
  "कथन-I सही है, पर कथन-II गलत है। भारत ने तब से गंभीर सूखे झेले हैं -- 1987, 2002 और 2009 सहित; अकाल से बचाव हरित क्रांति के बाद खाद्यान्न में आत्मनिर्भरता और बफ़र स्टॉक तथा सार्वजनिक वितरण की उस खाद्य सुरक्षा व्यवस्था से हुआ जो अनाज को ज़रूरत की जगह तक पहुँचाती है। "
  "सूखा उत्पादन घटाता है, पर अकाल -- व्यापक भुखमरी और मौतें -- तब होता है जब बड़े क्षेत्र में लोगों को भोजन उपलब्ध या सस्ता न हो।",
  f"{EC9} (Food Security in India).",
  "l1-eco-no-famine-despite-droughts", craft="inference")

# ---------------------------------------------------------------- hard statement (1)
S(AG, "hard", "Consider the following statements about land reforms in India after Independence:",
  "स्वतंत्रता के बाद भारत में भूमि सुधारों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The abolition of intermediaries brought about 200 lakh tenants into direct contact with the government.",
   "Many big landlords escaped land-ceiling laws by registering their land in the names of close relatives.",
   "The policy of 'land to the tiller' was carried out fully in most States."],
  ["बिचौलियों की समाप्ति से लगभग 200 लाख काश्तकार सरकार के सीधे संपर्क में आए।",
   "कई बड़े भूस्वामी अपनी भूमि निकट संबंधियों के नाम पंजीकृत कराकर भूमि-सीमा क़ानूनों से बच निकले।",
   "'जोतने वाले को भूमि' की नीति अधिकांश राज्यों में पूरी तरह लागू की गई।"],
  C3, 1,
  "Statements 1 and 2 are correct: zamindari abolition gave tenants ownership and incentive to invest, but some former zamindars kept large areas by claiming to be self-cultivators, and landlords delayed ceiling laws by challenging them in court. "
  "Statement 3 is wrong: only in Kerala and West Bengal, where the governments were committed to it, was land given to the tillers on a large scale; elsewhere tenants were often evicted or left insecure.",
  "कथन 1 और 2 सही हैं: ज़मींदारी उन्मूलन ने काश्तकारों को स्वामित्व और निवेश की प्रेरणा दी, पर कुछ पूर्व ज़मींदारों ने स्वयं खेती करने का दावा करके बड़े क्षेत्र अपने पास रखे, और भूस्वामियों ने अदालतों में चुनौती देकर भूमि-सीमा क़ानूनों को टाला। "
  "कथन 3 गलत है: केवल केरल और पश्चिम बंगाल में, जहाँ सरकारें इसके प्रति प्रतिबद्ध थीं, बड़े पैमाने पर जोतने वालों को भूमि मिली; अन्यत्र काश्तकार प्रायः बेदख़ल हुए या असुरक्षित रहे।",
  f"{IED} (Indian Economy 1950-1990).",
  "l1-eco-land-reforms-intermediaries-ceiling", craft="multi")

# ---------------------------------------------------------------- hard Statement-I/II (1)
A(AG, "hard",
  "Organically grown food is generally cheaper than conventionally grown food, since organic farming saves on chemical inputs.",
  "जैविक रूप से उगाया भोजन सामान्यतः परंपरागत रूप से उगाए भोजन से सस्ता होता है, क्योंकि जैविक खेती रासायनिक आदानों की बचत करती है।",
  "Organic farming uses farm manure and biological pest control in place of chemical fertilisers and pesticides.",
  "जैविक खेती रासायनिक उर्वरकों और कीटनाशकों के स्थान पर खेत की खाद और जैविक कीट-नियंत्रण का उपयोग करती है।",
  3,
  "Statement-I is incorrect but Statement-II is correct. Organic farming saves on purchased chemicals and restores the soil, and being labour-intensive it suits India, but its yields are lower in the initial years, it needs better marketing and certification, and its produce may have a shorter shelf life -- so organic food usually sells at a premium over conventional produce. "
  "The premium is part of its appeal to farmers, provided they can reach the buyers who will pay it.",
  "कथन-I गलत है, पर कथन-II सही है। जैविक खेती ख़रीदे जाने वाले रसायनों की बचत करती और मिट्टी को पुनर्स्थापित करती है, और श्रम-प्रधान होने के कारण भारत के अनुकूल है, पर आरंभिक वर्षों में इसकी उपज कम होती है, इसे बेहतर विपणन और प्रमाणन चाहिए, और इसकी उपज जल्दी ख़राब हो सकती है -- इसलिए जैविक भोजन प्रायः परंपरागत उपज से ऊँची कीमत पर बिकता है। "
  "यह ऊँची कीमत किसानों के लिए इसका आकर्षण है, बशर्ते वे उसे चुकाने वाले ख़रीदारों तक पहुँच सकें।",
  f"{IED} (Rural Development).",
  "l1-eco-organic-farming-premium", craft="inference")

# ================================================================ INCLUSIVE GROWTH (4)
# ---------------------------------------------------------------- easy pairs (1)
P(IG, "easy", "Consider the following pairs of indicators and what they measure:",
  "संकेतकों और उनके द्वारा मापी जाने वाली चीज़ों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Body Mass Index : weight in kilograms divided by the square of height in metres",
   "Net attendance ratio : children of a given age group attending school, as a percentage of all children in that age group",
   "Worker-population ratio : number of workers per hundred persons in the population",
   "Sex ratio in India : number of males per 1,000 females"],
  ["बॉडी मास इंडेक्स : किलोग्राम में भार को मीटर में ऊँचाई के वर्ग से भाग",
   "निवल उपस्थिति अनुपात : किसी आयु वर्ग के स्कूल जाने वाले बच्चे, उस आयु वर्ग के सभी बच्चों के प्रतिशत के रूप में",
   "श्रमिक-जनसंख्या अनुपात : जनसंख्या में प्रति सौ व्यक्तियों पर श्रमिकों की संख्या",
   "भारत में लिंगानुपात : प्रति 1,000 महिलाओं पर पुरुषों की संख्या"],
  2,
  "Pairs 1, 2 and 3 are correctly matched. NCERT uses the BMI to judge undernourishment -- an adult with a BMI below 18.5 is considered undernourished -- and the net attendance ratio to judge access to schooling; the worker-population ratio shows how much of the population is actively contributing to production. "
  "Pair 4 is wrong: in India the sex ratio is expressed as the number of females per 1,000 males.",
  "युग्म 1, 2 और 3 सही सुमेलित हैं। NCERT अल्पपोषण आँकने के लिए BMI का उपयोग करता है -- 18.5 से कम BMI वाला वयस्क अल्पपोषित माना जाता है -- और स्कूली शिक्षा तक पहुँच आँकने के लिए निवल उपस्थिति अनुपात का; श्रमिक-जनसंख्या अनुपात दिखाता है कि जनसंख्या का कितना भाग उत्पादन में सक्रिय योगदान दे रहा है। "
  "युग्म 4 गलत है: भारत में लिंगानुपात प्रति 1,000 पुरुषों पर महिलाओं की संख्या के रूप में व्यक्त होता है।",
  f"{EC10} (Development); {IED} (Employment).",
  "l1-eco-development-indicators-pairs", craft="precision")

# ---------------------------------------------------------------- easy statement (1)
S(IG, "easy", "Consider the following statements about employment in India:",
  "भारत में रोज़गार के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Workers include all those engaged in economic activities, whether they are self-employed or hired by others.",
   "Casual wage labourers form the largest category of India's workforce."],
  ["श्रमिकों में आर्थिक गतिविधियों में लगे सभी लोग शामिल हैं, चाहे वे स्वरोज़गार में हों या दूसरों द्वारा काम पर रखे गए हों।",
   "अनियत (casual) दिहाड़ी मज़दूर भारत के कार्यबल की सबसे बड़ी श्रेणी हैं।"],
  T2, 0,
  "Only statement 1 is correct: anyone engaged in an activity that contributes to the gross domestic product is a worker. "
  "Statement 2 is wrong: the self-employed -- farmers working their own land, shopkeepers, artisans and their unpaid family helpers -- form the largest category, well above half the workforce in the Periodic Labour Force Surveys, followed by casual and then regular wage or salaried workers.",
  "केवल कथन 1 सही है: सकल घरेलू उत्पाद में योगदान देने वाली किसी भी गतिविधि में लगा व्यक्ति श्रमिक है। "
  "कथन 2 गलत है: स्वरोज़गार वाले -- अपनी भूमि पर काम करने वाले किसान, दुकानदार, दस्तकार और उनके अवैतनिक पारिवारिक सहायक -- सबसे बड़ी श्रेणी हैं, आवधिक श्रम बल सर्वेक्षणों में कार्यबल के आधे से कहीं अधिक, उसके बाद अनियत और फिर नियमित वेतनभोगी श्रमिक आते हैं।",
  f"{IED} (Employment); Periodic Labour Force Survey, Ministry of Statistics and Programme Implementation.",
  "l1-eco-workers-self-employed-largest", craft="precision")

# ---------------------------------------------------------------- medium statement (1)
S(IG, "medium", "Consider the following statements comparing human capital with physical capital:",
  "मानव पूँजी की भौतिक पूँजी से तुलना करते हुए निम्नलिखित कथनों पर विचार कीजिए:",
  ["Physical capital is tangible and can be sold in the market, while human capital is intangible.",
   "Human capital is inseparable from its owner, while physical capital can be separated from its owner.",
   "Unlike physical capital, human capital does not depreciate over time."],
  ["भौतिक पूँजी मूर्त है और बाज़ार में बेची जा सकती है, जबकि मानव पूँजी अमूर्त है।",
   "मानव पूँजी अपने स्वामी से अविभाज्य है, जबकि भौतिक पूँजी अपने स्वामी से अलग की जा सकती है।",
   "भौतिक पूँजी के विपरीत, मानव पूँजी में समय के साथ ह्रास नहीं होता।"],
  C3, 1,
  "Statements 1 and 2 are correct: a machine can be bought, moved and sold, while the skills of a doctor live in the doctor, and only their services can be sold. "
  "Statement 3 is wrong: both forms of capital depreciate with time, but differently -- machines wear out with use and become obsolete with new technology, while human capital declines with ageing and can be maintained by continuous investment in education and health.",
  "कथन 1 और 2 सही हैं: मशीन ख़रीदी, ले जाई और बेची जा सकती है, जबकि डॉक्टर का कौशल डॉक्टर में ही रहता है, और केवल उसकी सेवाएँ बेची जा सकती हैं। "
  "कथन 3 गलत है: दोनों तरह की पूँजी में समय के साथ ह्रास होता है, पर अलग ढंग से -- मशीनें उपयोग से घिसती हैं और नई तकनीक से पुरानी पड़ जाती हैं, जबकि मानव पूँजी आयु बढ़ने से घटती है और शिक्षा तथा स्वास्थ्य में निरंतर निवेश से बनाए रखी जा सकती है।",
  f"{IED} (Human Capital Formation in India).",
  "l1-eco-human-vs-physical-capital", craft="precision")

# ---------------------------------------------------------------- hard pairs (1)
P(IG, "hard", "Consider the following pairs of schemes and what they provide:",
  "योजनाओं और उनके द्वारा दी जाने वाली सुविधाओं के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["PM SVANidhi : collateral-free working-capital loans to street vendors",
   "Mission Indradhanush : full immunisation of children and pregnant women",
   "Pradhan Mantri Kaushal Vikas Yojana : short-term skill training and certification of youth",
   "Samagra Shiksha : an integrated scheme for school education, from pre-school to Class XII"],
  ["पीएम स्वनिधि : पथ विक्रेताओं को बिना समर्थक ऋणाधार के कार्यशील पूँजी ऋण",
   "मिशन इंद्रधनुष : बच्चों और गर्भवती महिलाओं का पूर्ण टीकाकरण",
   "प्रधानमंत्री कौशल विकास योजना : युवाओं का अल्पकालिक कौशल प्रशिक्षण और प्रमाणन",
   "समग्र शिक्षा : पूर्व-प्राथमिक से कक्षा XII तक स्कूली शिक्षा की एकीकृत योजना"],
  3,
  "All four pairs are correctly matched. PM SVANidhi was launched in 2020 to help street vendors restart after the pandemic, with larger follow-on loans for timely repayment and incentives for digital payments; Mission Indradhanush, from 2014, targets children and pregnant women left out of routine immunisation. "
  "PMKVY runs under the Ministry of Skill Development and Entrepreneurship, and Samagra Shiksha (2018) merged the earlier school schemes -- Sarva Shiksha Abhiyan, Rashtriya Madhyamik Shiksha Abhiyan and Teacher Education.",
  "चारों युग्म सही सुमेलित हैं। पीएम स्वनिधि 2020 में महामारी के बाद पथ विक्रेताओं को फिर से काम शुरू करने में मदद के लिए आरंभ हुई, जिसमें समय पर चुकाने पर बड़े अगले ऋण और डिजिटल भुगतान के प्रोत्साहन हैं; 2014 से चल रहा मिशन इंद्रधनुष नियमित टीकाकरण से छूटे बच्चों और गर्भवती महिलाओं को लक्षित करता है। "
  "PMKVY कौशल विकास और उद्यमिता मंत्रालय के अंतर्गत चलती है, और समग्र शिक्षा (2018) ने पहले की स्कूली योजनाओं -- सर्व शिक्षा अभियान, राष्ट्रीय माध्यमिक शिक्षा अभियान और शिक्षक शिक्षा -- को मिला दिया।",
  "Ministry of Housing and Urban Affairs; Ministry of Health and Family Welfare; Ministry of Skill Development and Entrepreneurship; Ministry of Education.",
  "l1-eco-welfare-schemes-pairs", craft="precision")

# ================================================================ GROWTH & PLANNING (3)
# ---------------------------------------------------------------- easy statement (1)
S(GD, "easy", "Consider the following statements about the goals of planning in India:",
  "भारत में नियोजन के लक्ष्यों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The goals of the Five Year Plans included growth, modernisation, self-reliance and equity.",
   "Modernisation, as a goal of planning, referred only to adopting new technology, not to changes in social outlook."],
  ["पंचवर्षीय योजनाओं के लक्ष्यों में संवृद्धि, आधुनिकीकरण, आत्मनिर्भरता और समता शामिल थे।",
   "नियोजन के लक्ष्य के रूप में आधुनिकीकरण का अर्थ केवल नई तकनीक अपनाना था, सामाजिक दृष्टिकोण में परिवर्तन नहीं।"],
  T2, 0,
  "Only statement 1 is correct. Statement 2 is wrong: NCERT explains that modernisation meant not only adopting new technology but also changing social outlook, such as recognising that women should have the same rights as men. "
  "Growth meant raising the country's capacity to produce goods and services, self-reliance meant avoiding imports of goods, especially food, that could be produced in India, and equity meant that the benefits of growth should reach the poor.",
  "केवल कथन 1 सही है। कथन 2 गलत है: NCERT बताता है कि आधुनिकीकरण का अर्थ केवल नई तकनीक अपनाना नहीं, बल्कि सामाजिक दृष्टिकोण बदलना भी था, जैसे यह मानना कि महिलाओं को पुरुषों के समान अधिकार होने चाहिए। "
  "संवृद्धि का अर्थ था वस्तुएँ और सेवाएँ उत्पन्न करने की देश की क्षमता बढ़ाना, आत्मनिर्भरता का अर्थ था उन वस्तुओं, विशेषकर भोजन, के आयात से बचना जो भारत में बन सकती थीं, और समता का अर्थ था कि संवृद्धि के लाभ ग़रीबों तक पहुँचें।",
  f"{IED} (Indian Economy 1950-1990).",
  "l1-eco-planning-goals-modernisation", craft="precision")

# ---------------------------------------------------------------- medium statement (1)
S(GD, "medium", "Consider the following statements about the study of poverty:",
  "ग़रीबी के अध्ययन के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The concept of social exclusion sees poverty as being excluded from the facilities, benefits and opportunities that others enjoy.",
   "Vulnerability to poverty measures the greater probability of certain communities or individuals becoming, or remaining, poor in the coming years.",
   "Poverty in India has declined at the same rate in all the States."],
  ["सामाजिक अपवर्जन (social exclusion) की अवधारणा ग़रीबी को उन सुविधाओं, लाभों और अवसरों से वंचित रहने के रूप में देखती है जिनका दूसरे आनंद लेते हैं।",
   "ग़रीबी के प्रति असुरक्षा (vulnerability) यह मापती है कि कुछ समुदायों या व्यक्तियों के आने वाले वर्षों में ग़रीब होने या ग़रीब बने रहने की संभावना कितनी अधिक है।",
   "भारत में ग़रीबी सभी राज्यों में एक ही दर से घटी है।"],
  C3, 1,
  "Statements 1 and 2 are correct: both widen the view of poverty beyond income -- the caste system, for instance, has excluded people from opportunities others enjoy, and groups such as landless labourers face greater risks in times of drought or job loss. "
  "Statement 3 is wrong: the decline has been very uneven; Punjab and Haryana reduced it through high agricultural growth, Kerala through human resource development, West Bengal through land reform, and Andhra Pradesh and Tamil Nadu partly through the public distribution of food grains, while others lag behind.",
  "कथन 1 और 2 सही हैं: दोनों ग़रीबी को आय से आगे देखते हैं -- जैसे जाति व्यवस्था ने लोगों को दूसरों को मिलने वाले अवसरों से वंचित रखा है, और भूमिहीन श्रमिकों जैसे समूहों को सूखे या नौकरी जाने पर अधिक जोखिम होता है। "
  "कथन 3 गलत है: गिरावट बहुत असमान रही है; पंजाब और हरियाणा ने ऊँची कृषि संवृद्धि से, केरल ने मानव संसाधन विकास से, पश्चिम बंगाल ने भूमि सुधार से, और आंध्र प्रदेश तथा तमिलनाडु ने कुछ हद तक खाद्यान्न के सार्वजनिक वितरण से ग़रीबी घटाई, जबकि अन्य पीछे हैं।",
  f"{EC9} (Poverty as a Challenge).",
  "l1-eco-social-exclusion-vulnerability", craft="linkage")

# ---------------------------------------------------------------- hard pairs (1)
P(GD, "hard", "Consider the following pairs of categories of the poor and their descriptions:",
  "ग़रीबों की श्रेणियों और उनके विवरणों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Chronic poor : the always poor and the usually poor",
   "Churning poor : those who regularly move in and out of poverty, such as small farmers and seasonal workers",
   "Occasionally poor : those who are rich most of the time but may sometimes have a patch of bad luck",
   "Non-poor : those who fall below the poverty line only in years of drought"],
  ["दीर्घकालिक ग़रीब : सदा ग़रीब और प्रायः ग़रीब",
   "गतिशील (churning) ग़रीब : वे जो नियमित रूप से ग़रीबी में आते-जाते रहते हैं, जैसे छोटे किसान और मौसमी श्रमिक",
   "कभी-कभार ग़रीब : वे जो अधिकतर समय अमीर रहते हैं पर कभी-कभी दुर्भाग्य झेल सकते हैं",
   "ग़ैर-ग़रीब : वे जो केवल सूखे के वर्षों में ग़रीबी रेखा से नीचे जाते हैं"],
  2,
  "Pairs 1, 2 and 3 are correctly matched. NCERT groups the churning poor and the occasionally poor together as the transient poor, whose condition depends on the season, the harvest or chance events. "
  "Pair 4 is wrong: the non-poor are those who are never poor; anyone who falls below the line in drought years belongs among the transient poor. The distinction matters for policy, since the chronic poor need lasting support, the transient poor protection against shocks.",
  "युग्म 1, 2 और 3 सही सुमेलित हैं। NCERT गतिशील ग़रीबों और कभी-कभार ग़रीबों को साथ मिलाकर अस्थायी (transient) ग़रीब कहता है, जिनकी स्थिति ऋतु, फ़सल या आकस्मिक घटनाओं पर निर्भर करती है। "
  "युग्म 4 गलत है: ग़ैर-ग़रीब वे हैं जो कभी ग़रीब नहीं होते; सूखे के वर्षों में रेखा से नीचे जाने वाला कोई भी अस्थायी ग़रीबों में आता है। यह भेद नीति के लिए महत्त्वपूर्ण है, क्योंकि दीर्घकालिक ग़रीबों को स्थायी सहारा, और अस्थायी ग़रीबों को झटकों से सुरक्षा चाहिए।",
  f"{IED} (Poverty).",
  "l1-eco-categories-of-poor-pairs", craft="precision")

write("eco_l1_t5_c.sql")
