# -*- coding: utf-8 -*-
"""CSAT Level 2 · Test 3 -- Reading Comprehension: 10 original passages, 28 items (8 x 3, 2 x 2).

Themes, none used in Tests 1 or 2: stubble burning, remote work and cities, microfinance, space debris,
civil-service neutrality, food lost between farm and shop, Himalayan hill towns, nudges, elephants and forest
corridors, and GDP as a measure of wellbeing. Item types: main idea 7, inference 8, assumption 5, tone 1,
specific detail 4, best summary 3. Options are named by content in every explanation."""
from csat_common import passage, RQ

CRUX = "Which one of the following statements best reflects the crux of the passage?"
CRUX_HI = "निम्नलिखित में से कौन-सा कथन परिच्छेद के सार को सबसे अच्छी तरह व्यक्त करता है?"
MSG = "Which one of the following statements best reflects the most logical and rational message conveyed by the passage?"
MSG_HI = "निम्नलिखित में से कौन-सा कथन परिच्छेद द्वारा दिए गए सबसे तार्किक और विवेकपूर्ण संदेश को सबसे अच्छी तरह व्यक्त करता है?"
VALID = "On the basis of the passage, which of the following conclusions is/are valid?"
VALID_HI = "परिच्छेद के आधार पर निम्नलिखित में से कौन-सा/से निष्कर्ष वैध है/हैं?"
ASSUME = "Which of the following assumptions has/have been made in the passage?"
ASSUME_HI = "परिच्छेद में निम्नलिखित में से कौन-सी पूर्वधारणा/एँ बनाई गई है/हैं?"
INFER = "Which of the following inferences can be drawn from the passage?"
INFER_HI = "परिच्छेद से निम्नलिखित में से कौन-से अनुमान निकाले जा सकते हैं?"

# ------------------------------------------------------------------ P01 stubble burning (3)
p = passage("p01",
  "Every autumn, farmers in the north-west burn the straw left in their fields after the rice harvest, and the smoke adds to the haze that settles over the plains. Burning is not a habit that farmers cling to out of ignorance. "
  "The gap between harvesting rice and sowing wheat is barely three weeks, the straw is bulky and of little value as fodder, and removing it by machine costs money and time that a small farmer rarely has. "
  "Fines have done little, because a farmer who cannot sow on time loses far more than the fine. Where the problem has eased, it is because the alternatives became cheaper or quicker than the match: "
  "machines that sow wheat straight through the straw, supplied through cooperatives, and buyers who pay for straw as fuel or raw material.",
  "हर शरद ऋतु में उत्तर-पश्चिम के किसान धान की कटाई के बाद खेतों में बचा पुआल जला देते हैं, और उसका धुआँ मैदानों पर छाने वाली धुंध को और बढ़ा देता है। जलाना ऐसी आदत नहीं है जिससे किसान अज्ञानवश चिपके हों। "
  "धान की कटाई और गेहूँ की बुआई के बीच मुश्किल से तीन सप्ताह होते हैं, पुआल भारी-भरकम है और चारे के रूप में उसका मूल्य कम है, और मशीन से उसे हटाने में पैसा और समय लगता है जो छोटे किसान के पास शायद ही होता है। "
  "जुर्मानों से बहुत कम हुआ है, क्योंकि जो किसान समय पर बुआई नहीं कर पाता, उसका नुक़सान जुर्माने से कहीं अधिक होता है। जहाँ समस्या घटी है, वहाँ इसलिए घटी है कि विकल्प माचिस की तीली से सस्ते या तेज़ हो गए: "
  "पुआल के बीच से ही सीधे गेहूँ बोने वाली मशीनें, जो सहकारी समितियों के माध्यम से मिलीं, और ऐसे ख़रीदार जो पुआल का ईंधन या कच्चे माल के रूप में दाम देते हैं।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage rejects ignorance as the cause, explains burning by the time and cost of the alternatives, and ends by saying that the problem eased where the alternatives became cheaper or quicker. "
   "Ignorance is the very explanation the passage denies; fines are said to have done little; and giving up rice is never proposed.",
   "परिच्छेद अज्ञान को कारण मानने से इनकार करता है, जलाने की व्याख्या विकल्पों के समय और लागत से करता है, और अंत में कहता है कि समस्या वहाँ घटी जहाँ विकल्प सस्ते या तेज़ हो गए। "
   "अज्ञान ठीक वही व्याख्या है जिसे परिच्छेद नकारता है; जुर्मानों के बारे में कहा गया है कि उनसे बहुत कम हुआ; और धान छोड़ने का प्रस्ताव कहीं नहीं है।",
   "crux",
   opts=["Burning falls where the alternatives become cheaper or quicker for farmers than burning.",
         "Farmers burn their straw because they do not understand the harm that the smoke does.",
         "Heavier fines on farmers are the most effective way to put an end to stubble burning.",
         "Rice should no longer be grown in the north-west, so that there is no straw left to burn."],
   opts_hi=["जलाना वहाँ घटता है जहाँ किसानों के लिए विकल्प जलाने से सस्ते या तेज़ हो जाते हैं।",
            "किसान पुआल इसलिए जलाते हैं क्योंकि वे धुएँ से होने वाली हानि को नहीं समझते।",
            "किसानों पर भारी जुर्माने पुआल जलाना बंद कराने का सबसे प्रभावी तरीका हैं।",
            "उत्तर-पश्चिम में धान उगाना ही बंद कर देना चाहिए, ताकि जलाने के लिए कोई पुआल ही न बचे।"],
   ans=0, pos=1)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Neither is valid. 1 runs against the passage's own evidence: where cheaper or quicker alternatives appeared, burning eased. "
   "2 contradicts the passage directly: 'Burning is not a habit that farmers cling to out of ignorance.'",
   "कोई भी वैध नहीं है। 1 परिच्छेद के अपने प्रमाण के विरुद्ध जाता है: जहाँ सस्ते या तेज़ विकल्प आए, वहाँ जलाना घटा। "
   "2 परिच्छेद का सीधा खंडन करता है: 'जलाना ऐसी आदत नहीं है जिससे किसान अज्ञानवश चिपके हों।'",
   "conclusions",
   st=["Most farmers would go on burning straw even if a cheaper alternative were available.",
       "Farmers burn straw mainly because they are unaware of the harm the smoke does."],
   st_hi=["सस्ता विकल्प उपलब्ध होने पर भी अधिकांश किसान पुआल जलाते रहेंगे।",
          "किसान पुआल मुख्यतः इसलिए जलाते हैं क्योंकि वे धुएँ से होने वाली हानि से अनजान हैं।"],
   key=3)
RQ(p, "Assumption", "hard", "s2", ASSUME, ASSUME_HI,
   "Only 1 is assumed. The claim that fines fail 'because a farmer who cannot sow on time loses far more than the fine' makes sense only if farmers set the fine against what sowing late would cost them. "
   "2 is not needed: the passage explains burning by time and money, not by indifference to the smoke.",
   "केवल 1 पूर्वधारणा है। यह दावा कि जुर्माने इसलिए विफल हैं 'क्योंकि जो किसान समय पर बुआई नहीं कर पाता, उसका नुक़सान जुर्माने से कहीं अधिक होता है', तभी अर्थपूर्ण है जब किसान जुर्माने को देर से बुआई की लागत के सामने तौलते हों। "
   "2 की ज़रूरत नहीं: परिच्छेद जलाने की व्याख्या समय और पैसे से करता है, धुएँ के प्रति उदासीनता से नहीं।",
   "assumptions",
   st=["Farmers weigh the cost of a fine against what they would lose by sowing late.",
       "Farmers do not care about the smoke that burning produces."],
   st_hi=["किसान जुर्माने की लागत को उस नुक़सान के सामने तौलते हैं जो देर से बुआई करने पर होगा।",
          "किसानों को जलाने से उठने वाले धुएँ की परवाह नहीं है।"],
   key=0)

# ------------------------------------------------------------------ P02 remote work and cities (3)
p = passage("p02",
  "When offices emptied during the pandemic, many predicted the end of the big city: if work could be done from anywhere, why pay city rents? The prediction has not come true, but something has shifted. "
  "Jobs that can be done at a screen are now less tied to a place, and some workers have moved to smaller towns, taking city salaries with them. Yet the work that most city residents do -- cooking, cleaning, building, "
  "caring, selling -- cannot be done remotely at all. And even screen workers gather in cities for what remote work handles badly: learning from colleagues, chance meetings, a variety of jobs to move between. "
  "Cities are unlikely to empty; what is likelier is that they will have to compete harder for the workers who could live anywhere.",
  "महामारी के दौरान जब दफ़्तर ख़ाली हुए, तो बहुतों ने बड़े शहर के अंत की भविष्यवाणी की: यदि काम कहीं से भी हो सकता है, तो शहर का किराया क्यों दें? यह भविष्यवाणी सच नहीं हुई, पर कुछ बदला ज़रूर है। "
  "जो काम स्क्रीन पर हो सकते हैं, वे अब किसी स्थान से कम बँधे हैं, और कुछ कर्मचारी शहर का वेतन साथ लेकर छोटे कस्बों में चले गए हैं। फिर भी शहर के अधिकांश निवासी जो काम करते हैं -- खाना बनाना, सफ़ाई, निर्माण, "
  "देखभाल, बिक्री -- वह दूर से हो ही नहीं सकता। और स्क्रीन पर काम करने वाले भी उन चीज़ों के लिए शहरों में जुटते हैं जिन्हें दूर से काम ठीक से नहीं सँभाल पाता: सहकर्मियों से सीखना, संयोग से होने वाली मुलाक़ातें, बदलने के लिए नौकरियों की विविधता। "
  "शहरों के ख़ाली होने की संभावना कम है; अधिक संभावना यह है कि उन्हें उन कर्मचारियों के लिए कड़ी होड़ करनी होगी जो कहीं भी रह सकते हैं।")
RQ(p, "Best Summary", "medium", "mcq", MSG, MSG_HI,
   "The passage says the predicted emptying of cities has not happened, that most city work cannot be done remotely, and that cities will have to compete for the workers who could live anywhere. "
   "Emptying cities is the prediction it rejects; most city residents cannot work from home at all; and the passage says workers took city salaries to the towns, not that towns pay more.",
   "परिच्छेद कहता है कि शहरों के ख़ाली होने की भविष्यवाणी सच नहीं हुई, कि शहर का अधिकांश काम दूर से नहीं हो सकता, और कि शहरों को उन कर्मचारियों के लिए होड़ करनी होगी जो कहीं भी रह सकते हैं। "
   "शहरों का ख़ाली होना वही भविष्यवाणी है जिसे वह नकारता है; शहर के अधिकांश निवासी घर से काम कर ही नहीं सकते; और परिच्छेद कहता है कि कर्मचारी शहर का वेतन कस्बों में ले गए, यह नहीं कि कस्बे अधिक वेतन देते हैं।",
   "message",
   opts=["Remote work frees some workers from cities, which will survive but must compete for them.",
         "Big cities will empty out as more and more work moves online and offices close down.",
         "Most people who live in cities now do their work from home instead of at an office.",
         "Small towns pay better salaries than big cities, which is why workers are moving to them."],
   opts_hi=["दूर से काम कुछ कर्मचारियों को शहरों से छुड़ाता है; शहर बचेंगे, पर उनके लिए होड़ करेंगे।",
            "जैसे-जैसे अधिक काम ऑनलाइन होगा और दफ़्तर बंद होंगे, बड़े शहर ख़ाली हो जाएँगे।",
            "शहरों में रहने वाले अधिकांश लोग अब दफ़्तर के बजाय घर से काम करते हैं।",
            "छोटे कस्बे बड़े शहरों की तुलना में अधिक वेतन देते हैं, और इसीलिए कर्मचारी उनकी ओर जा रहे हैं।"],
   ans=0, pos=0)
RQ(p, "Specific Detail", "easy", "mcq",
   "According to the passage, which one of the following does remote work handle badly?",
   "परिच्छेद के अनुसार, दूर से काम निम्नलिखित में से किसे ठीक से नहीं सँभाल पाता?",
   "The passage lists what remote work handles badly: learning from colleagues, chance meetings and a variety of jobs to move between. "
   "Earning a city salary is something remote work allows -- workers took city salaries with them to the towns; reaching the office on time and finding a cheaper home are not given as things remote work handles badly.",
   "परिच्छेद गिनाता है कि दूर से काम किसे ठीक से नहीं सँभाल पाता: सहकर्मियों से सीखना, संयोग से होने वाली मुलाक़ातें और बदलने के लिए नौकरियों की विविधता। "
   "शहर जैसा वेतन कमाना तो दूर से काम संभव बनाता है -- कर्मचारी शहर का वेतन कस्बों में साथ ले गए; समय पर दफ़्तर पहुँचना और सस्ता घर ढूँढना ऐसी बातों के रूप में नहीं दिए गए जिन्हें दूर से काम ठीक से नहीं सँभालता।",
   "detail",
   opts=["learning from colleagues", "earning a city salary", "reaching the office on time", "finding a cheaper home"],
   opts_hi=["सहकर्मियों से सीखना", "शहर जैसा वेतन कमाना", "समय पर दफ़्तर पहुँचना", "सस्ता घर ढूँढ पाना"],
   ans=0, pos=2)
RQ(p, "Inference", "hard", "sc", INFER, INFER_HI,
   "1 and 2 follow. The work most city residents do 'cannot be done remotely at all', so they could not keep their present jobs from a small town (1). Cities having to 'compete harder' for the workers who could live anywhere "
   "implies that what a city offers can draw such workers (2). 3 goes beyond the passage, which says nothing about rents falling.",
   "1 और 2 निकलते हैं। शहर के अधिकांश निवासी जो काम करते हैं वह 'दूर से हो ही नहीं सकता', इसलिए वे छोटे कस्बे से अपनी वर्तमान नौकरी नहीं रख सकते (1)। शहरों को उन कर्मचारियों के लिए 'कड़ी होड़' करनी होगी जो कहीं भी रह सकते हैं, "
   "जिसका अर्थ है कि शहर जो देता है वह ऐसे कर्मचारियों को खींच सकता है (2)। 3 परिच्छेद से आगे जाता है, जो किराये घटने के बारे में कुछ नहीं कहता।",
   "inferences",
   st=["Most city residents could not keep their present jobs if they moved to a small town.",
       "A city that offers a good life may draw workers who could live anywhere.",
       "Remote work has lowered rents in every big city."],
   st_hi=["शहर के अधिकांश निवासी छोटे कस्बे में चले जाने पर अपनी वर्तमान नौकरी नहीं रख सकते।",
          "जो शहर अच्छा जीवन देता है, वह उन कर्मचारियों को खींच सकता है जो कहीं भी रह सकते हैं।",
          "दूर से काम ने हर बड़े शहर में किराये घटा दिए हैं।"],
   opts=["1 only", "2 and 3 only", "1, 2 and 3", "1 and 2 only"], key=3)

# ------------------------------------------------------------------ P03 microfinance (3)
p = passage("p03",
  "Small loans to poor women, repaid in weekly instalments within groups, were once hailed as a way out of poverty. The record is more modest. Studies that compared villages with and without such lenders found that "
  "the loans helped households even out their spending, buy assets and cope with emergencies, but rarely transformed their incomes. The danger lies in success itself. Where many lenders crowd into the same area, "
  "a borrower can take a second loan to repay the first, and debts can grow faster than earnings; the weekly meetings that once built discipline then become a source of pressure. A loan is a tool, not a cure. "
  "Its value depends on what the borrower can do with it, and on lenders checking how much she already owes.",
  "ग़रीब महिलाओं को समूहों में दिए गए और साप्ताहिक किस्तों में चुकाए जाने वाले छोटे ऋणों को कभी ग़रीबी से निकलने का रास्ता कहा गया था। उनका रिकॉर्ड अधिक साधारण है। जिन अध्ययनों ने ऐसे ऋणदाताओं वाले और बिना ऋणदाताओं वाले गाँवों की तुलना की, उन्होंने पाया कि "
  "ऋणों ने परिवारों को अपना ख़र्च बराबर रखने, संपत्ति ख़रीदने और आपात स्थितियों से निपटने में मदद की, पर उनकी आय को शायद ही कभी बदला। ख़तरा सफलता में ही छिपा है। जहाँ एक ही क्षेत्र में बहुत-से ऋणदाता आ जुटते हैं, "
  "वहाँ उधार लेने वाली पहला ऋण चुकाने के लिए दूसरा ऋण ले सकती है, और कर्ज़ कमाई से तेज़ बढ़ सकता है; जो साप्ताहिक बैठकें कभी अनुशासन बनाती थीं, वे तब दबाव का स्रोत बन जाती हैं। ऋण एक औज़ार है, इलाज नहीं। "
  "उसका मूल्य इस पर निर्भर करता है कि उधार लेने वाली उससे क्या कर सकती है, और इस पर कि ऋणदाता जाँचें कि वह पहले से कितनी देनदार है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage scales down the claim that small loans end poverty -- they help households manage -- and warns that crowded, careless lending can trap borrowers in debt. "
   "It says the loans 'rarely transformed' incomes, so they did not lift most borrowers out of poverty; it never says the poor should not borrow; and it treats the weekly meetings as a source of pressure only where lending is crowded, not as the main cause of debt.",
   "परिच्छेद इस दावे को छोटा करता है कि छोटे ऋण ग़रीबी समाप्त करते हैं -- वे परिवारों को सँभलने में मदद करते हैं -- और चेताता है कि भीड़ भरा, लापरवाह ऋण उधार लेने वालों को कर्ज़ में फँसा सकता है। "
   "वह कहता है कि ऋणों ने आय को 'शायद ही कभी बदला', इसलिए उन्होंने अधिकांश उधार लेने वालों को ग़रीबी से नहीं निकाला; वह कहीं नहीं कहता कि ग़रीबों को उधार नहीं लेना चाहिए; और वह साप्ताहिक बैठकों को दबाव का स्रोत केवल वहाँ मानता है जहाँ ऋणदाताओं की भीड़ हो, कर्ज़ का मुख्य कारण नहीं।",
   "crux",
   opts=["Small loans help the poor manage money but can harm them when lenders are careless.",
         "Small loans have lifted most of the women who borrowed them out of poverty for good.",
         "Poor women should not be given loans at all, because they cannot repay them.",
         "The weekly meetings of borrowers are the main cause of debt in the villages."],
   opts_hi=["छोटे ऋण पैसा सँभालने में मदद करते हैं, पर लापरवाही से दिए जाएँ तो हानि कर सकते हैं।",
            "छोटे ऋणों ने उधार लेने वाली अधिकांश महिलाओं को सदा के लिए ग़रीबी से बाहर निकाल दिया है।",
            "ग़रीब महिलाओं को ऋण दिए ही नहीं जाने चाहिए, क्योंकि वे उन्हें चुका नहीं सकतीं।",
            "उधार लेने वालों की साप्ताहिक बैठकें ही गाँवों में कर्ज़ का मुख्य कारण हैं।"],
   ans=0, pos=3)
RQ(p, "Assumption", "hard", "s2", ASSUME, ASSUME_HI,
   "Only 2 is assumed. The remedy the passage proposes -- lenders checking how much a borrower already owes -- works only if lenders are able to find that out. "
   "1 is not assumed and runs against the passage, which says the loans rarely transformed incomes.",
   "केवल 2 पूर्वधारणा है। परिच्छेद जो उपाय सुझाता है -- ऋणदाता जाँचें कि उधार लेने वाली पहले से कितनी देनदार है -- वह तभी काम करता है जब ऋणदाता यह पता लगा सकें। "
   "1 पूर्वधारणा नहीं है और परिच्छेद के विरुद्ध जाता है, जो कहता है कि ऋणों ने आय को शायद ही कभी बदला।",
   "assumptions",
   st=["Borrowers always use their loans for purposes that raise their incomes.",
       "Lenders are able to find out how much a borrower already owes."],
   st_hi=["उधार लेने वाले अपने ऋणों का उपयोग सदा ऐसे कामों में करते हैं जिनसे उनकी आय बढ़े।",
          "ऋणदाता यह पता लगा सकते हैं कि उधार लेने वाला पहले से कितना देनदार है।"],
   key=1)
RQ(p, "Inference", "hard", "sc", INFER, INFER_HI,
   "1 and 2 follow. The loans helped households even out their spending and cope with emergencies but 'rarely transformed their incomes' (1). Where many lenders crowd into one area, borrowers take new loans to repay old ones "
   "and debts outgrow earnings (2). 3 contradicts the passage: the meetings 'once built discipline'.",
   "1 और 2 निकलते हैं। ऋणों ने परिवारों को ख़र्च बराबर रखने और आपात स्थितियों से निपटने में मदद की, पर 'उनकी आय को शायद ही कभी बदला' (1)। जहाँ एक क्षेत्र में बहुत-से ऋणदाता जुटते हैं, वहाँ उधार लेने वाले पुराने ऋण चुकाने के लिए नए ऋण लेते हैं "
   "और कर्ज़ कमाई से आगे निकल जाता है (2)। 3 परिच्छेद का खंडन करता है: बैठकें 'कभी अनुशासन बनाती थीं'।",
   "inferences",
   st=["Small loans have done more to help households manage money than to raise their incomes.",
       "Competition among lenders in one area can leave borrowers worse off.",
       "The weekly group meetings have never been of any use to borrowers."],
   st_hi=["छोटे ऋणों ने परिवारों की आय बढ़ाने से अधिक उन्हें पैसा सँभालने में मदद की है।",
          "एक क्षेत्र में ऋणदाताओं की होड़ उधार लेने वालों की स्थिति बिगाड़ सकती है।",
          "साप्ताहिक समूह बैठकें उधार लेने वालों के कभी किसी काम की नहीं रहीं।"],
   opts=["1 and 2 only", "2 only", "1 and 3 only", "1, 2 and 3"], key=0)

# ------------------------------------------------------------------ P04 space debris (2)
p = passage("p04",
  "More than ten thousand working satellites now circle the Earth, and with them millions of fragments -- spent rocket stages, dead satellites and the debris of collisions -- moving faster than a bullet. "
  "A fragment the size of a coin can disable a satellite, and each collision creates more fragments, so that in a crowded orbit the debris can multiply even if no one launches anything new. No single country can solve this, "
  "since debris respects no borders, and the low cost of launching today rewards whoever gets there first. Rules that require satellites to be steered down and burnt up at the end of their working lives exist, "
  "but in much of the world they are voluntary.",
  "अब दस हज़ार से अधिक कार्यरत उपग्रह पृथ्वी की परिक्रमा करते हैं, और उनके साथ दसियों लाख टुकड़े -- ख़र्च हो चुके रॉकेट चरण, निष्क्रिय उपग्रह और टक्करों का मलबा -- गोली से भी तेज़ चलते हैं। "
  "सिक्के के आकार का एक टुकड़ा किसी उपग्रह को बेकार कर सकता है, और हर टक्कर और टुकड़े बनाती है, जिससे भीड़ भरी कक्षा में मलबा तब भी बढ़ता जा सकता है जब कोई कुछ भी नया प्रक्षेपित न करे। कोई एक देश इसका समाधान नहीं कर सकता, "
  "क्योंकि मलबा कोई सीमा नहीं मानता, और आज प्रक्षेपण की कम लागत उसी को पुरस्कृत करती है जो पहले पहुँचे। ऐसे नियम मौजूद हैं जो अपेक्षा करते हैं कि उपग्रहों को उनके कार्यकाल के अंत में नीचे लाकर जला दिया जाए, "
  "पर दुनिया के बड़े भाग में वे स्वैच्छिक हैं।")
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Only 1 is valid. Because each collision creates more fragments, debris 'can multiply even if no one launches anything new', so stopping launches would not on its own make a crowded orbit safe. "
   "2 contradicts the passage: debris 'respects no borders'.",
   "केवल 1 वैध है। चूँकि हर टक्कर और टुकड़े बनाती है, मलबा 'तब भी बढ़ता जा सकता है जब कोई कुछ भी नया प्रक्षेपित न करे', इसलिए प्रक्षेपण रोक देने भर से भीड़ भरी कक्षा सुरक्षित नहीं हो जाएगी। "
   "2 परिच्छेद का खंडन करता है: मलबा 'कोई सीमा नहीं मानता'।",
   "conclusions",
   st=["Stopping all new launches would not by itself make a crowded orbit safe.",
       "Debris endangers only the satellites of the country that produced it."],
   st_hi=["सभी नए प्रक्षेपण रोक देने भर से भीड़ भरी कक्षा सुरक्षित नहीं हो जाएगी।",
          "मलबा केवल उसी देश के उपग्रहों के लिए ख़तरा है जिसने उसे पैदा किया।"],
   key=0)
RQ(p, "Main Idea", "easy", "mcq", CRUX, CRUX_HI,
   "The passage describes a danger that no single country can solve, made worse by cheap launches that reward whoever comes first and by rules that are only voluntary. "
   "It does not call for an end to launches into low orbit; it says even a coin-sized fragment is dangerous; and it says launching is now cheap, not costly.",
   "परिच्छेद एक ऐसे ख़तरे का वर्णन करता है जिसे कोई एक देश हल नहीं कर सकता, और जिसे पहले पहुँचने वाले को पुरस्कृत करने वाले सस्ते प्रक्षेपण और केवल स्वैच्छिक नियम और बढ़ाते हैं। "
   "वह निचली कक्षा में प्रक्षेपण बंद करने की माँग नहीं करता; वह कहता है कि सिक्के जितना टुकड़ा भी ख़तरनाक है; और वह कहता है कि प्रक्षेपण अब सस्ता है, महँगा नहीं।",
   "crux",
   opts=["Debris is a shared danger that voluntary rules and a race to launch leave unchecked.",
         "Satellites should no longer be launched into the low orbits around the Earth at all.",
         "Only large pieces of debris, such as spent rocket stages, are a danger to satellites.",
         "Launching a satellite has become too costly for most of the countries of the world."],
   opts_hi=["मलबा साझा ख़तरा है, जिसे स्वैच्छिक नियम और प्रक्षेपण की होड़ बेरोक छोड़ देते हैं।",
            "पृथ्वी के चारों ओर की निचली कक्षाओं में अब उपग्रह भेजना पूरी तरह बंद कर देना चाहिए।",
            "केवल बड़े टुकड़े, जैसे ख़र्च हो चुके रॉकेट चरण, ही उपग्रहों के लिए ख़तरा हैं।",
            "उपग्रह प्रक्षेपित करना दुनिया के अधिकांश देशों के लिए बहुत महँगा हो गया है।"],
   ans=0, pos=3)

# ------------------------------------------------------------------ P05 civil-service neutrality (3)
p = passage("p05",
  "A civil servant in a democracy serves governments of every party in turn, and the system depends on her serving each of them with the same care. Neutrality does not mean having no views; it means giving honest advice "
  "in private and carrying out lawful decisions in public, even those she argued against. It also means knowing where the line lies. An order to bend a rule for a favoured contractor is not a decision to be loyally "
  "carried out but one to be refused, and the refusal recorded. Officials who confuse loyalty to the government of the day with loyalty to a minister's wishes serve neither the public nor the minister: "
  "a policy that no one dared to question is a policy that no one has tested.",
  "लोकतंत्र में एक सिविल सेवक बारी-बारी से हर दल की सरकारों की सेवा करती है, और व्यवस्था इस पर टिकी है कि वह हर एक की सेवा समान निष्ठा से करे। तटस्थता का अर्थ कोई राय न होना नहीं है; इसका अर्थ है निजी रूप से ईमानदार सलाह देना "
  "और सार्वजनिक रूप से वैध निर्णयों को लागू करना, उन निर्णयों को भी जिनके विरुद्ध उसने तर्क दिया था। इसका अर्थ यह जानना भी है कि रेखा कहाँ है। किसी चहेते ठेकेदार के लिए नियम मोड़ने का आदेश निष्ठा से लागू करने वाला निर्णय नहीं, "
  "बल्कि ठुकराने वाला आदेश है, और ठुकराने को लिखित में दर्ज किया जाना चाहिए। जो अधिकारी तत्कालीन सरकार के प्रति निष्ठा को किसी मंत्री की इच्छाओं के प्रति निष्ठा समझ बैठते हैं, वे न जनता का भला करते हैं न मंत्री का: "
  "जिस नीति पर किसी ने प्रश्न उठाने का साहस नहीं किया, उसे किसी ने परखा ही नहीं।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage defines neutrality by three duties: honest advice in private, faithful implementation of lawful decisions, and refusal of unlawful orders. It says neutrality 'does not mean having no views', so keeping quiet is wrong; "
   "it says some orders must be refused, so 'every order' is wrong; and it says nothing about ministers questioning their officials' advice.",
   "परिच्छेद तटस्थता को तीन कर्तव्यों से परिभाषित करता है: निजी रूप से ईमानदार सलाह, वैध निर्णयों को निष्ठा से लागू करना, और अवैध आदेशों को ठुकराना। वह कहता है कि तटस्थता का 'अर्थ कोई राय न होना नहीं है', इसलिए चुप रहना ग़लत है; "
   "वह कहता है कि कुछ आदेश ठुकराने होंगे, इसलिए 'हर आदेश' ग़लत है; और वह मंत्रियों द्वारा अधिकारियों की सलाह पर प्रश्न उठाने के बारे में कुछ नहीं कहता।",
   "crux",
   opts=["Neutrality means candid advice, loyal implementation and the refusal of unlawful orders.",
         "Civil servants should keep their views to themselves and never argue with a minister.",
         "Civil servants must carry out every order of the minister, since the minister is elected.",
         "Ministers should not question the advice that they receive from their civil servants."],
   opts_hi=["तटस्थता का अर्थ है खरी सलाह, निष्ठापूर्ण अमल और अवैध आदेशों को ठुकराना।",
            "सिविल सेवकों को अपनी राय अपने तक रखनी चाहिए और मंत्री से कभी बहस नहीं करनी चाहिए।",
            "सिविल सेवकों को मंत्री का हर आदेश लागू करना चाहिए, क्योंकि मंत्री निर्वाचित होता है।",
            "मंत्रियों को अपने सिविल सेवकों से मिलने वाली सलाह पर प्रश्न नहीं उठाना चाहिए।"],
   ans=0, pos=0)
RQ(p, "Author's Tone", "medium", "mcq",
   "The author's attitude towards officials who never question a minister's wishes is best described as:",
   "मंत्री की इच्छाओं पर कभी प्रश्न न उठाने वाले अधिकारियों के प्रति लेखक का दृष्टिकोण सबसे अच्छी तरह कैसा बताया जा सकता है?",
   "The author says such officials serve 'neither the public nor the minister', because a policy no one dared to question has never been tested -- a critical view. "
   "Nothing in the passage admires their deference, the author is plainly not indifferent, and the passage does not dwell on the pressure officials work under.",
   "लेखक कहता है कि ऐसे अधिकारी 'न जनता का भला करते हैं न मंत्री का', क्योंकि जिस नीति पर किसी ने प्रश्न उठाने का साहस नहीं किया, उसे परखा ही नहीं गया -- यह आलोचनात्मक दृष्टि है। "
   "परिच्छेद में उनकी आज्ञाकारिता की कोई प्रशंसा नहीं, लेखक स्पष्ट रूप से उदासीन नहीं है, और परिच्छेद अधिकारियों पर पड़ने वाले दबाव की चर्चा नहीं करता।",
   "tone",
   opts=["critical of them for leaving policies untested",
         "admiring of their loyalty to the government of the day",
         "indifferent to the way they choose to behave",
         "sympathetic to the pressure under which they work"],
   opts_hi=["नीतियों को बिना परखे छोड़ने के लिए उनका आलोचक",
            "तत्कालीन सरकार के प्रति उनकी निष्ठा का प्रशंसक",
            "उनके व्यवहार के ढंग के प्रति उदासीन",
            "जिस दबाव में वे काम करते हैं उसके प्रति सहानुभूतिपूर्ण"],
   ans=0, pos=2)
RQ(p, "Assumption", "hard", "sc", ASSUME, ASSUME_HI,
   "1 and 2 are assumed. The closing line -- an unquestioned policy is an untested one -- takes for granted that frank advice can improve policy (1). The duty to refuse an order to bend a rule assumes that an unlawful order "
   "stays unlawful even when a minister gives it (2). 3 contradicts the passage: neutrality 'does not mean having no views'.",
   "1 और 2 पूर्वधारणाएँ हैं। अंतिम पंक्ति -- जिस नीति पर प्रश्न नहीं उठा, वह परखी नहीं गई -- मानकर चलती है कि खरी सलाह नीति को बेहतर बना सकती है (1)। नियम मोड़ने के आदेश को ठुकराने का कर्तव्य मानता है कि अवैध आदेश "
   "मंत्री के देने पर भी अवैध ही रहता है (2)। 3 परिच्छेद का खंडन करता है: तटस्थता का 'अर्थ कोई राय न होना नहीं है'।",
   "assumptions",
   st=["Frank advice from officials can improve the quality of policy.",
       "An unlawful order does not become lawful because a minister gives it.",
       "Civil servants have no political views of their own."],
   st_hi=["अधिकारियों की खरी सलाह नीति की गुणवत्ता सुधार सकती है।",
          "कोई अवैध आदेश केवल इसलिए वैध नहीं हो जाता कि उसे मंत्री ने दिया है।",
          "सिविल सेवकों के अपने कोई राजनीतिक विचार नहीं होते।"],
   opts=["1 only", "1 and 3 only", "2 and 3 only", "1 and 2 only"], key=3)

# ------------------------------------------------------------------ P06 food lost between farm and shop (3)
p = passage("p06",
  "India grows more fruit and vegetables than almost any other country, yet a sizeable share spoils between the farm and the plate. Much of the loss happens before the food reaches a shop: produce picked in the heat waits "
  "for a truck, travels without cooling, and is sold at whatever price the market will bear before it rots. Cold storage exists, but much of it is built for potatoes, lies far from the farms and is of little use for a tomato "
  "that must be cooled within hours of picking. What would make the most difference is less glamorous than large warehouses: small cooling units near the farms, run on solar power where the grid is weak, "
  "and trucks that keep the cold chain unbroken.",
  "भारत लगभग किसी भी अन्य देश से अधिक फल और सब्ज़ियाँ उगाता है, फिर भी उनका एक बड़ा भाग खेत और थाली के बीच ख़राब हो जाता है। अधिकांश हानि भोजन के दुकान तक पहुँचने से पहले होती है: गर्मी में तोड़ी गई उपज ट्रक की प्रतीक्षा करती है, "
  "बिना ठंडक के यात्रा करती है, और सड़ने से पहले बाज़ार जो भी दाम दे, उस पर बिक जाती है। शीत भंडार मौजूद हैं, पर उनका बड़ा भाग आलू के लिए बना है, खेतों से दूर है, और ऐसे टमाटर के लिए किसी काम का नहीं "
  "जिसे तोड़ने के कुछ ही घंटों के भीतर ठंडा करना ज़रूरी है। सबसे बड़ा अंतर बड़े गोदामों से कम आकर्षक चीज़ों से आएगा: खेतों के पास छोटी शीतलन इकाइयाँ, जो बिजली ग्रिड कमज़ोर होने पर सौर ऊर्जा से चलें, "
  "और ऐसे ट्रक जो शीत शृंखला को टूटने न दें।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage places most of the loss between picking and the shop, finds the existing stores built for potatoes and far away, and ends by calling for small cooling units near farms and an unbroken cold chain. "
   "It says nothing of India growing too much; it places the loss before food reaches a shop, not in homes and shops; and it does not ask for the potato stores to be closed.",
   "परिच्छेद अधिकांश हानि तोड़ने और दुकान के बीच बताता है, पाता है कि मौजूदा भंडार आलू के लिए बने और दूर हैं, और अंत में खेतों के पास छोटी शीतलन इकाइयों और न टूटने वाली शीत शृंखला की माँग करता है। "
   "वह भारत के बहुत अधिक उगाने की कोई बात नहीं करता; वह हानि को भोजन के दुकान पहुँचने से पहले रखता है, घरों और दुकानों में नहीं; और वह आलू के भंडार बंद करने को नहीं कहता।",
   "crux",
   opts=["Cutting food loss needs cooling close to the farms more than distant cold stores.",
         "India grows far more fruit and vegetables than its people are able to eat.",
         "Most of India's food is wasted in homes and shops rather than on the way to them.",
         "The cold stores that are now used for potatoes should be closed down."],
   opts_hi=["भोजन की हानि घटाने के लिए दूर के शीत भंडारों से अधिक खेतों के पास ठंडक चाहिए।",
            "भारत अपने लोगों के खा सकने से कहीं अधिक फल और सब्ज़ियाँ उगाता है।",
            "भारत का अधिकांश भोजन वहाँ तक पहुँचने के रास्ते में नहीं, घरों और दुकानों में बर्बाद होता है।",
            "जो शीत भंडार अभी आलू के लिए उपयोग होते हैं, उन्हें बंद कर देना चाहिए।"],
   ans=0, pos=3)
RQ(p, "Specific Detail", "easy", "mcq",
   "According to the passage, why is much of the existing cold storage of little use for tomatoes?",
   "परिच्छेद के अनुसार, मौजूदा शीत भंडारों का बड़ा भाग टमाटरों के लिए किसी काम का क्यों नहीं है?",
   "The passage says that much of the cold storage 'is built for potatoes, lies far from the farms' and so is of little use for a tomato that must be cooled within hours. "
   "Solar power appears only in the new units the passage proposes; the passage implies that tomatoes do gain from quick cooling; and storage charges are not mentioned.",
   "परिच्छेद कहता है कि शीत भंडारों का बड़ा भाग 'आलू के लिए बना है, खेतों से दूर है' और इसलिए ऐसे टमाटर के किसी काम का नहीं जिसे कुछ ही घंटों में ठंडा करना ज़रूरी है। "
   "सौर ऊर्जा केवल उन नई इकाइयों में आती है जिनका परिच्छेद प्रस्ताव करता है; परिच्छेद से स्पष्ट है कि टमाटरों को जल्दी ठंडा करने से लाभ होता है; और भंडारण शुल्क का कोई उल्लेख नहीं।",
   "detail",
   opts=["It is built for potatoes and lies far from the farms.",
         "It runs on solar power, which fails when the weather is cloudy.",
         "Tomatoes spoil just as quickly whether they are cooled or not.",
         "Traders find the charges for storing tomatoes there too high."],
   opts_hi=["उनका बड़ा भाग आलू के लिए बना है और खेतों से दूर है।",
            "वे सौर ऊर्जा से चलते हैं, जो बादल होने पर काम नहीं करती।",
            "टमाटर ठंडे किए जाएँ या नहीं, उतनी ही जल्दी ख़राब होते हैं।",
            "व्यापारियों को वहाँ टमाटर रखने का शुल्क बहुत अधिक लगता है।"],
   ans=0, pos=1)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Both are valid. A tomato 'must be cooled within hours of picking', and produce that travels without cooling rots, so cooling soon after picking helps produce keep (1). "
   "The passage proposes cooling units near the farms 'run on solar power where the grid is weak' (2).",
   "दोनों वैध हैं। टमाटर को 'तोड़ने के कुछ ही घंटों के भीतर ठंडा करना ज़रूरी है', और बिना ठंडक के यात्रा करने वाली उपज सड़ जाती है, इसलिए तोड़ने के तुरंत बाद ठंडा करने से उपज टिकती है (1)। "
   "परिच्छेद खेतों के पास ऐसी शीतलन इकाइयों का प्रस्ताव करता है 'जो बिजली ग्रिड कमज़ोर होने पर सौर ऊर्जा से चलें' (2)।",
   "conclusions",
   st=["Produce that is cooled soon after it is picked is likely to keep longer.",
       "Where the electricity grid is weak, solar power can help keep produce cool near the farms."],
   st_hi=["तोड़ने के तुरंत बाद ठंडी की गई उपज के अधिक समय तक टिकने की संभावना है।",
          "जहाँ बिजली ग्रिड कमज़ोर है, वहाँ सौर ऊर्जा खेतों के पास उपज को ठंडा रखने में मदद कर सकती है।"],
   key=2)

# ------------------------------------------------------------------ P07 Himalayan hill towns (3)
p = passage("p07",
  "Hill towns in the Himalaya were built for a few thousand residents and now receive that many visitors in a single day in the season. Roads are widened to bring them in, hotels rise on slopes that were never surveyed "
  "for such loads, and the streams that once carried away a town's waste now carry far more. Each new road brings more cars, and each wider road invites more hotels; the town's appeal, its quiet and its views, "
  "is the first thing to go. Some places have begun to limit the number of vehicles or visitors on a given day. Such limits are unpopular with those who earn from tourism, but they may be what keeps the trade alive.",
  "हिमालय के पहाड़ी कस्बे कुछ हज़ार निवासियों के लिए बसे थे और अब मौसम में एक ही दिन में उतने पर्यटक आ जाते हैं। उन्हें लाने के लिए सड़कें चौड़ी की जाती हैं, ऐसी ढलानों पर होटल उठते हैं जिनका इतने भार के लिए कभी सर्वेक्षण नहीं हुआ, "
  "और जो नाले कभी कस्बे का कचरा बहा ले जाते थे, वे अब कहीं अधिक ढोते हैं। हर नई सड़क अधिक गाड़ियाँ लाती है, और हर चौड़ी सड़क अधिक होटलों को न्योता देती है; कस्बे का आकर्षण, उसकी शांति और उसके दृश्य, "
  "सबसे पहले जाते हैं। कुछ स्थानों ने किसी एक दिन में गाड़ियों या पर्यटकों की संख्या सीमित करना शुरू किया है। ऐसी सीमाएँ पर्यटन से कमाने वालों में अलोकप्रिय हैं, पर हो सकता है कि यही उस व्यापार को जीवित रखें।")
RQ(p, "Best Summary", "medium", "mcq", MSG, MSG_HI,
   "The passage traces how the roads and hotels built for visitors destroy the quiet and views that draw them, and suggests that daily limits, though unpopular, may keep tourism alive. "
   "It proposes limits, not a ban; it presents wider roads as part of the problem; and it says the limits are unpopular with those who earn from tourism.",
   "परिच्छेद दिखाता है कि पर्यटकों के लिए बनी सड़कें और होटल उस शांति और उन दृश्यों को नष्ट करते हैं जो उन्हें खींचते हैं, और सुझाता है कि दैनिक सीमाएँ, अलोकप्रिय होने पर भी, पर्यटन को जीवित रख सकती हैं। "
   "वह सीमाओं का प्रस्ताव करता है, प्रतिबंध का नहीं; वह चौड़ी सड़कों को समस्या का भाग बताता है; और वह कहता है कि सीमाएँ पर्यटन से कमाने वालों में अलोकप्रिय हैं।",
   "message",
   opts=["Unchecked tourism wears away what draws visitors, so limits may save the trade.",
         "Tourism should be banned in Himalayan towns to protect their streams and slopes.",
         "Wider roads are the best way for hill towns to cope with the crowds of tourists.",
         "People who earn their living from tourism have welcomed the limits on visitors."],
   opts_hi=["बेरोक पर्यटन वही घिसता है जो पर्यटकों को खींचता है; सीमाएँ व्यापार बचा सकती हैं।",
            "हिमालयी कस्बों के नालों और ढलानों की रक्षा के लिए वहाँ पर्यटन पर प्रतिबंध लगना चाहिए।",
            "पहाड़ी कस्बों के लिए पर्यटकों की भीड़ से निपटने का सबसे अच्छा तरीका चौड़ी सड़कें हैं।",
            "पर्यटन से जीविका कमाने वालों ने पर्यटकों पर लगी सीमाओं का स्वागत किया है।"],
   ans=0, pos=0)
RQ(p, "Assumption", "hard", "s2", ASSUME, ASSUME_HI,
   "Only 2 is assumed. The claim that limits 'may be what keeps the trade alive' rests on the idea that a town's quiet and views draw its visitors -- lose them and the visitors go. "
   "1 is not needed: the passage speaks of limiting 'vehicles or visitors', and nothing depends on every visitor coming by car.",
   "केवल 2 पूर्वधारणा है। यह दावा कि सीमाएँ 'हो सकता है उस व्यापार को जीवित रखें', इस विचार पर टिका है कि कस्बे की शांति और उसके दृश्य पर्यटकों को खींचते हैं -- वे गए तो पर्यटक भी जाएँगे। "
   "1 की ज़रूरत नहीं: परिच्छेद 'गाड़ियों या पर्यटकों' को सीमित करने की बात करता है, और कुछ भी इस पर निर्भर नहीं कि हर पर्यटक कार से आए।",
   "assumptions",
   st=["All visitors to hill towns arrive by car.",
       "A town's quiet and its views are part of what draws visitors to it."],
   st_hi=["पहाड़ी कस्बों में सभी पर्यटक कार से आते हैं।",
          "किसी कस्बे की शांति और उसके दृश्य उन कारणों में हैं जो पर्यटकों को वहाँ खींचते हैं।"],
   key=1)
RQ(p, "Inference", "hard", "sc", INFER, INFER_HI,
   "1 and 2 follow. 'Each new road brings more cars, and each wider road invites more hotels', so widening the roads into a hill town can add to its traffic (1); the hotels rise 'on slopes that were never surveyed for such loads' (2). "
   "3 contradicts the passage, which says the limits are unpopular with those who earn from tourism.",
   "1 और 2 निकलते हैं। 'हर नई सड़क अधिक गाड़ियाँ लाती है, और हर चौड़ी सड़क अधिक होटलों को न्योता देती है', इसलिए पहाड़ी कस्बे की सड़कें चौड़ी करने से उसका यातायात बढ़ सकता है (1); होटल 'ऐसी ढलानों पर उठते हैं जिनका इतने भार के लिए कभी सर्वेक्षण नहीं हुआ' (2)। "
   "3 परिच्छेद का खंडन करता है, जो कहता है कि सीमाएँ पर्यटन से कमाने वालों में अलोकप्रिय हैं।",
   "inferences",
   st=["Widening the roads into a hill town can bring more traffic rather than less.",
       "Some hotels may stand on slopes that were never checked for the load they carry.",
       "Limits on visitors are welcomed by everyone who earns from tourism."],
   st_hi=["पहाड़ी कस्बे की सड़कें चौड़ी करने से यातायात घटने के बजाय बढ़ सकता है।",
          "कुछ होटल ऐसी ढलानों पर हो सकते हैं जिनकी उस भार के लिए कभी जाँच नहीं हुई जो वे ढोती हैं।",
          "पर्यटन से कमाने वाले सभी लोग पर्यटकों पर सीमाओं का स्वागत करते हैं।"],
   opts=["1 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"], key=1)

# ------------------------------------------------------------------ P08 nudges (2)
p = passage("p08",
  "Governments have long changed behaviour with laws and taxes. A newer approach changes instead the way choices are presented. When employees are enrolled in a pension plan unless they choose to opt out, far more of them "
  "save than when they must opt in, though the choice is the same. Putting fruit at eye level in a canteen sells more fruit than a poster about healthy eating. Such 'nudges' are cheap and leave people free to choose, "
  "which makes them attractive. But they work best where people already want the outcome and only inertia stands in the way. They do little when the problem is not inattention but poverty: a nudge to save means little "
  "to a family that has nothing left at the end of the month.",
  "सरकारें लंबे समय से क़ानूनों और करों से व्यवहार बदलती रही हैं। एक नया तरीका इसके बजाय विकल्पों को प्रस्तुत करने का ढंग बदलता है। जब कर्मचारियों को पेंशन योजना में तब तक शामिल माना जाता है जब तक वे स्वयं बाहर निकलना न चुनें, "
  "तो उनमें से कहीं अधिक बचत करते हैं, बनिस्बत उस स्थिति के जब उन्हें स्वयं शामिल होना पड़ता है, यद्यपि विकल्प वही है। कैंटीन में फल आँखों की ऊँचाई पर रखने से स्वस्थ भोजन के पोस्टर की तुलना में अधिक फल बिकते हैं। "
  "ऐसे 'नज' (हल्के प्रेरक संकेत) सस्ते हैं और लोगों को चुनने की स्वतंत्रता देते हैं, जिससे वे आकर्षक लगते हैं। पर वे वहाँ सबसे अच्छा काम करते हैं जहाँ लोग पहले से वही परिणाम चाहते हैं और केवल जड़ता रास्ते में है। "
  "जब समस्या असावधानी नहीं बल्कि ग़रीबी हो, तब वे बहुत कम कर पाते हैं: बचत का नज उस परिवार के लिए कुछ ख़ास मायने नहीं रखता जिसके पास महीने के अंत में कुछ बचता ही नहीं।")
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Both are valid. Employees enrolled unless they opt out save far more, 'though the choice is the same', so a default can raise saving while leaving everyone free to opt out (1). "
   "Nudges 'do little when the problem is not inattention but poverty', and a nudge to save means little to a family with nothing left over (2).",
   "दोनों वैध हैं। जब तक बाहर न निकलें तब तक शामिल माने गए कर्मचारी कहीं अधिक बचत करते हैं, 'यद्यपि विकल्प वही है', इसलिए डिफ़ॉल्ट विकल्प हर किसी को बाहर निकलने की स्वतंत्रता देते हुए बचत बढ़ा सकता है (1)। "
   "नज 'तब बहुत कम कर पाते हैं जब समस्या असावधानी नहीं बल्कि ग़रीबी हो', और बचत का नज उस परिवार के लिए कुछ मायने नहीं रखता जिसके पास कुछ बचता ही नहीं (2)।",
   "conclusions",
   st=["Making saving the default can raise saving without forcing anyone to save.",
       "A nudge to save is unlikely to help a family that has no money left over."],
   st_hi=["बचत को डिफ़ॉल्ट विकल्प बनाना किसी को बचत के लिए विवश किए बिना बचत बढ़ा सकता है।",
          "बचत का नज उस परिवार की मदद करे, इसकी संभावना कम है जिसके पास कोई पैसा बचता ही नहीं।"],
   key=2)
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage presents nudges as cheap and freedom-preserving, effective where only inertia stands in the way, and of little use where poverty is the problem. "
   "It does not say that laws and taxes have stopped working; it says fruit at eye level sells more than a poster does; and employees enrolled by default can still opt out, so they are not forced to save.",
   "परिच्छेद नज को सस्ता और स्वतंत्रता बनाए रखने वाला बताता है, जो वहाँ प्रभावी है जहाँ केवल जड़ता रास्ते में हो, और वहाँ कम उपयोगी जहाँ समस्या ग़रीबी हो। "
   "वह नहीं कहता कि क़ानूनों और करों ने काम करना बंद कर दिया है; वह कहता है कि आँखों की ऊँचाई पर रखे फल पोस्टर से अधिक बिकते हैं; और डिफ़ॉल्ट रूप से शामिल कर्मचारी अब भी बाहर निकल सकते हैं, इसलिए वे बचत के लिए विवश नहीं हैं।",
   "crux",
   opts=["Nudges cheaply help people do what they already want but cannot make up for poverty.",
         "Laws and taxes no longer change people's behaviour, so governments must turn to nudges.",
         "Posters about healthy eating work better than changing how food is displayed in a canteen.",
         "Employees who are enrolled in pension plans automatically are forced to save their money."],
   opts_hi=["नज सस्ते में वह करवाते हैं जो लोग पहले से चाहते हैं, पर ग़रीबी की भरपाई नहीं कर सकते।",
            "क़ानून और कर अब लोगों का व्यवहार नहीं बदलते, इसलिए सरकारों को नज अपनाने होंगे।",
            "स्वस्थ भोजन के पोस्टर कैंटीन में भोजन रखने का ढंग बदलने से बेहतर काम करते हैं।",
            "पेंशन योजनाओं में अपने-आप शामिल किए गए कर्मचारी अपना पैसा बचाने के लिए पूरी तरह विवश हैं।"],
   ans=0, pos=3)

# ------------------------------------------------------------------ P09 elephants and forest corridors (3)
p = passage("p09",
  "As forests are cut into fragments by roads, canals and farms, elephants that once moved between them along old routes find their way blocked, and they walk instead through villages and fields. "
  "Each year crops are lost, homes damaged and people killed, and every death hardens attitudes towards the animals. Fences and trenches push elephants from one village to the next without reducing the conflict overall. "
  "The approach that has worked better treats the problem as one of movement: keeping open the corridors between forests, warning villages when a herd is near, and paying compensation quickly enough that farmers "
  "do not take matters into their own hands.",
  "जैसे-जैसे सड़कें, नहरें और खेत जंगलों को टुकड़ों में बाँटते हैं, वे हाथी जो कभी पुराने रास्तों से एक जंगल से दूसरे तक जाते थे, अपना रास्ता बंद पाते हैं, और इसके बजाय गाँवों और खेतों से होकर गुज़रते हैं। "
  "हर वर्ष फ़सलें नष्ट होती हैं, घर टूटते हैं और लोग मारे जाते हैं, और हर मौत इन जानवरों के प्रति रवैये को और कठोर बना देती है। बाड़ और खाइयाँ हाथियों को एक गाँव से अगले गाँव की ओर धकेल देती हैं, पर कुल मिलाकर संघर्ष नहीं घटातीं। "
  "जिस तरीके ने बेहतर काम किया है, वह समस्या को आवाजाही की समस्या मानता है: जंगलों के बीच के गलियारों को खुला रखना, झुंड पास होने पर गाँवों को चेतावनी देना, और मुआवज़ा इतनी जल्दी देना कि किसान "
  "मामला अपने हाथ में न लें।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage traces the conflict to blocked routes between fragmented forests, and says the approach that has worked better treats it as a problem of movement -- open corridors, warnings and quick compensation. "
   "It never calls elephants aggressive by nature; it says fences and trenches only move the problem on; and it does not propose moving farmers out.",
   "परिच्छेद संघर्ष को टुकड़ों में बँटे जंगलों के बीच बंद रास्तों से जोड़ता है, और कहता है कि जिस तरीके ने बेहतर काम किया वह इसे आवाजाही की समस्या मानता है -- खुले गलियारे, चेतावनियाँ और जल्दी मुआवज़ा। "
   "वह हाथियों को स्वभाव से आक्रामक कभी नहीं कहता; वह कहता है कि बाड़ और खाइयाँ समस्या को केवल आगे सरका देती हैं; और वह किसानों को हटाने का प्रस्ताव नहीं करता।",
   "crux",
   opts=["Conflict with elephants eases when their routes between forests are kept open.",
         "Elephants are by nature aggressive towards the people who live near the forests.",
         "Fences and trenches are the best way to keep elephants out of villages and fields.",
         "Farmers whose fields lie near forests should be moved out to protect the elephants."],
   opts_hi=["जंगलों के बीच हाथियों के रास्ते खुले रखने पर उनसे संघर्ष घटता है।",
            "हाथी स्वभाव से ही जंगलों के पास रहने वाले लोगों के प्रति आक्रामक होते हैं।",
            "हाथियों को गाँवों और खेतों से बाहर रखने का सबसे अच्छा तरीका बाड़ और खाइयाँ हैं।",
            "जिन किसानों के खेत जंगलों के पास हैं, उन्हें हाथियों की रक्षा के लिए वहाँ से हटा देना चाहिए।"],
   ans=0, pos=1)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Only 2 is valid. Compensation must be paid 'quickly enough that farmers do not take matters into their own hands', which implies that slow payment makes them likelier to act against the animals (2). "
   "1 contradicts the passage: fences and trenches move elephants on 'without reducing the conflict overall'.",
   "केवल 2 वैध है। मुआवज़ा 'इतनी जल्दी देना कि किसान मामला अपने हाथ में न लें', इसका अर्थ है कि भुगतान में देरी उन्हें जानवरों के विरुद्ध कदम उठाने की ओर अधिक ले जाती है (2)। "
   "1 परिच्छेद का खंडन करता है: बाड़ और खाइयाँ हाथियों को आगे धकेलती हैं, 'पर कुल मिलाकर संघर्ष नहीं घटातीं'।",
   "conclusions",
   st=["Fences and trenches have reduced the conflict between people and elephants overall.",
       "Slow payment of compensation can make farmers more likely to harm elephants."],
   st_hi=["बाड़ और खाइयों ने कुल मिलाकर लोगों और हाथियों के बीच संघर्ष घटाया है।",
          "मुआवज़े के भुगतान में देरी किसानों द्वारा हाथियों को हानि पहुँचाने की संभावना बढ़ा सकती है।"],
   key=1)
RQ(p, "Specific Detail", "easy", "mcq",
   "According to the passage, which of the following have cut the forests into fragments?",
   "परिच्छेद के अनुसार, निम्नलिखित में से किन्होंने जंगलों को टुकड़ों में बाँटा है?",
   "The passage says that forests are 'cut into fragments by roads, canals and farms'. Fences and trenches push elephants from village to village but are not said to fragment the forests; "
   "the herds are what the fragmenting blocks; and warnings to villages are part of the remedy.",
   "परिच्छेद कहता है कि जंगल 'सड़कों, नहरों और खेतों' से टुकड़ों में बँटते हैं। बाड़ और खाइयाँ हाथियों को गाँव-दर-गाँव धकेलती हैं, पर उनके बारे में यह नहीं कहा गया कि वे जंगलों को बाँटती हैं; "
   "झुंड वे हैं जिनका रास्ता यह बँटवारा रोकता है; और गाँवों को चेतावनी उपाय का भाग है।",
   "detail",
   opts=["roads, canals and farms",
         "fences and trenches put up around villages",
         "the herds of elephants that move between them",
         "warnings sent to villages when a herd is near"],
   opts_hi=["सड़कें, नहरें और खेत",
            "गाँवों के चारों ओर बनी बाड़ और खाइयाँ",
            "उनके बीच घूमने वाले हाथियों के झुंड",
            "झुंड पास होने पर गाँवों को भेजी गई चेतावनियाँ"],
   ans=0, pos=2)

# ------------------------------------------------------------------ P10 GDP and wellbeing (3)
p = passage("p10",
  "Gross domestic product measures the value of what an economy produces in a year, and it does this well. The trouble begins when it is taken for a measure of how well people live. GDP rises when a forest is felled "
  "and its timber sold, but does not fall to reflect the loss of the forest. It counts the cost of treating illness caused by polluted air as output. And it leaves out the unpaid work of caring for children and the old, "
  "which would be a large part of the economy if anyone were paid for it. None of this means GDP should be dropped; growth still pays for schools and hospitals. It means that a country which watches only GDP "
  "may grow richer on paper while some of what matters to its people declines.",
  "सकल घरेलू उत्पाद (GDP) किसी अर्थव्यवस्था द्वारा एक वर्ष में उत्पादित वस्तुओं और सेवाओं का मूल्य मापता है, और यह काम वह अच्छी तरह करता है। कठिनाई तब शुरू होती है जब उसे इस बात का माप मान लिया जाता है कि लोग कितनी अच्छी तरह जीते हैं। "
  "जब कोई जंगल काटा जाता है और उसकी लकड़ी बेची जाती है तो GDP बढ़ता है, पर जंगल की हानि दर्शाने के लिए घटता नहीं। प्रदूषित हवा से हुई बीमारी के इलाज की लागत को वह उत्पादन गिनता है। और वह बच्चों और बुज़ुर्गों की देखभाल के "
  "बिना वेतन वाले काम को छोड़ देता है, जो अर्थव्यवस्था का बड़ा भाग होता यदि किसी को उसके लिए वेतन मिलता। इसका अर्थ यह नहीं कि GDP को छोड़ दिया जाए; वृद्धि अब भी विद्यालयों और अस्पतालों का ख़र्च उठाती है। "
  "इसका अर्थ यह है कि जो देश केवल GDP पर नज़र रखता है, वह काग़ज़ पर अमीर होता जा सकता है जबकि उसके लोगों के लिए महत्त्वपूर्ण कुछ चीज़ें घटती जाएँ।")
RQ(p, "Best Summary", "medium", "mcq", MSG, MSG_HI,
   "The passage grants that GDP measures output well, shows three ways in which it misjudges wellbeing, and concludes that a country watching only GDP can grow richer on paper while losing what matters. "
   "It says GDP should not be dropped; it says growth still pays for schools and hospitals; and it says unpaid care is left out of GDP, not counted in it.",
   "परिच्छेद मानता है कि GDP उत्पादन को अच्छी तरह मापता है, तीन ऐसे तरीके दिखाता है जिनसे वह कल्याण को ग़लत आँकता है, और निष्कर्ष निकालता है कि केवल GDP पर नज़र रखने वाला देश काग़ज़ पर अमीर होते हुए भी महत्त्वपूर्ण चीज़ें खो सकता है। "
   "वह कहता है कि GDP को छोड़ा नहीं जाना चाहिए; वह कहता है कि वृद्धि अब भी विद्यालयों और अस्पतालों का ख़र्च उठाती है; और वह कहता है कि बिना वेतन की देखभाल GDP से बाहर है, उसमें गिनी नहीं जाती।",
   "message",
   opts=["GDP measures output well but misleads if it is taken alone as a measure of wellbeing.",
         "GDP should be dropped altogether and replaced by a measure of how happy people say they are.",
         "Economic growth does not pay for public services such as schools and hospitals.",
         "The unpaid work of caring for children and the old is already counted in GDP."],
   opts_hi=["GDP उत्पादन अच्छी तरह मापता है, पर अकेले कल्याण का माप मान लेने पर भ्रम पैदा करता है।",
            "GDP को पूरी तरह छोड़कर उसकी जगह इस बात का माप अपनाना चाहिए कि लोग स्वयं को कितना सुखी बताते हैं।",
            "आर्थिक वृद्धि विद्यालयों और अस्पतालों जैसी सार्वजनिक सेवाओं का ख़र्च नहीं उठाती।",
            "बच्चों और बुज़ुर्गों की देखभाल का बिना वेतन वाला काम पहले से GDP में गिना जाता है।"],
   ans=0, pos=0)
RQ(p, "Specific Detail", "medium", "mcq",
   "According to the passage, which one of the following does GDP leave out?",
   "परिच्छेद के अनुसार, GDP निम्नलिखित में से किसे छोड़ देता है?",
   "The passage says GDP 'leaves out the unpaid work of caring for children and the old'. The timber of a felled forest is counted -- GDP rises when it is sold; the cost of treating illness caused by polluted air "
   "is counted as output; and the passage says growth pays for schools and hospitals, not that GDP leaves that spending out.",
   "परिच्छेद कहता है कि GDP 'बच्चों और बुज़ुर्गों की देखभाल के बिना वेतन वाले काम को छोड़ देता है'। काटे गए जंगल की लकड़ी गिनी जाती है -- उसके बिकने पर GDP बढ़ता है; प्रदूषित हवा से हुई बीमारी के इलाज की लागत "
   "उत्पादन के रूप में गिनी जाती है; और परिच्छेद कहता है कि वृद्धि विद्यालयों और अस्पतालों का ख़र्च उठाती है, यह नहीं कि GDP उस ख़र्च को छोड़ देता है।",
   "detail",
   opts=["the unpaid work of caring for children and the old",
         "the value of timber from a forest that is felled",
         "the cost of treating illness caused by polluted air",
         "the money that growth provides for schools and hospitals"],
   opts_hi=["बच्चों और बुज़ुर्गों की देखभाल का बिना वेतन वाला काम",
            "काटे गए जंगल से मिली लकड़ी का मूल्य",
            "प्रदूषित हवा से हुई बीमारी के इलाज की लागत",
            "वृद्धि से विद्यालयों और अस्पतालों के लिए मिलने वाला धन"],
   ans=0, pos=3)
RQ(p, "Assumption", "hard", "s2", ASSUME, ASSUME_HI,
   "Both are assumed. The complaint that GDP is a poor measure of 'how well people live' takes for granted that wellbeing depends on more than output (1). "
   "Saying that GDP 'does not fall to reflect the loss of the forest' assumes that the standing forest had a value beyond the timber that was sold (2).",
   "दोनों पूर्वधारणाएँ हैं। यह शिकायत कि GDP इस बात का कमज़ोर माप है कि 'लोग कितनी अच्छी तरह जीते हैं', मानकर चलती है कि कल्याण उत्पादन से अधिक पर निर्भर है (1)। "
   "यह कहना कि GDP 'जंगल की हानि दर्शाने के लिए घटता नहीं', मानता है कि खड़े जंगल का मूल्य बेची गई लकड़ी से अधिक था (2)।",
   "assumptions",
   st=["How well people live depends on more than the value of what their economy produces.",
       "A forest has a value that is lost when it is felled, even if its timber is sold."],
   st_hi=["लोग कितनी अच्छी तरह जीते हैं, यह उनकी अर्थव्यवस्था के उत्पादन के मूल्य से अधिक बातों पर निर्भर करता है।",
          "जंगल का ऐसा मूल्य होता है जो उसके काटे जाने पर खो जाता है, भले उसकी लकड़ी बेच दी जाए।"],
   key=2)
