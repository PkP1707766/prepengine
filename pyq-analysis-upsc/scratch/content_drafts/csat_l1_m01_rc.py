# -*- coding: utf-8 -*-
"""CSAT Level 1 · Mini 1 -- Reading Comprehension: 5 original passages, 14 items (four with three items, the third
passage with two), at the foundation level: shorter passages (about 125-170 words) and 4 easy / 8 medium / 2 hard items.

Themes, none used in Level 2's 70 passages: iodised salt and a remedy that asks little of people, village tanks and
the shared duty that kept them working, online star ratings and who writes them, what a '70 per cent chance of rain'
means, and the free play that crowded timetables leave out. Item types: main idea 4, inference 4, assumption 2,
tone 1, specific detail 2, best summary 1. Options are named by content in every explanation."""
from csat_common import passage, RQ

CRUX = "Which one of the following statements best reflects the crux of the passage?"
CRUX_HI = "निम्नलिखित में से कौन-सा कथन परिच्छेद के सार को सबसे अच्छी तरह व्यक्त करता है?"
VALID = "On the basis of the passage, which of the following conclusions is/are valid?"
VALID_HI = "परिच्छेद के आधार पर निम्नलिखित में से कौन-सा/से निष्कर्ष वैध है/हैं?"
ASSUME = "Which of the following assumptions has/have been made in the passage?"
ASSUME_HI = "परिच्छेद में निम्नलिखित में से कौन-सी पूर्वधारणा/एँ बनाई गई है/हैं?"
INFER = "Which of the following inferences can be drawn from the passage?"
INFER_HI = "परिच्छेद से निम्नलिखित में से कौन-से अनुमान निकाले जा सकते हैं?"
SUMMARY = "Which one of the following best sums up the passage?"
SUMMARY_HI = "निम्नलिखित में से कौन-सा परिच्छेद का सबसे अच्छा सारांश है?"
TONE = "Which one of the following best describes the author's approach in the passage?"
TONE_HI = "निम्नलिखित में से कौन-सा परिच्छेद में लेखक के दृष्टिकोण का सबसे अच्छा वर्णन करता है?"

# ------------------------------------------------------------------ P01 iodised salt (3)
p = passage("p01",
  "For much of the twentieth century, goitre -- a swelling of the neck caused by too little iodine in the diet -- was common in the hills of northern India, where centuries of rain and melting snow have washed much of the iodine out of the soil. "
  "The remedy chosen was remarkably simple. Instead of asking millions of families to change what they ate, the government asked salt makers to add a tiny amount of iodine to the salt that every family already bought. "
  "Nobody had to remember a tablet or visit a clinic; the dose came with every meal. Where iodised salt reached the shops and was kept away from damp and heat, which drive the iodine off, goitre became far less common within a generation. "
  "The lesson is not that every health problem has so easy an answer, but that a measure works best when it asks the least of the people it is meant to help.",
  "बीसवीं सदी के बड़े भाग में घेंघा (goitre) -- आहार में आयोडीन की कमी से होने वाली गले की सूजन -- उत्तर भारत की पहाड़ियों में आम था, जहाँ सदियों की वर्षा और पिघलती बर्फ़ ने मिट्टी से आयोडीन का बड़ा भाग बहा दिया है। "
  "इसका जो उपाय चुना गया वह उल्लेखनीय रूप से सरल था। लाखों परिवारों से अपना भोजन बदलने को कहने के बजाय, सरकार ने नमक बनाने वालों से कहा कि वे उस नमक में आयोडीन की बहुत थोड़ी मात्रा मिलाएँ जिसे हर परिवार पहले से ख़रीदता था। "
  "किसी को गोली याद रखने या दवाख़ाने जाने की ज़रूरत नहीं थी; ख़ुराक हर भोजन के साथ आ जाती थी। जहाँ आयोडीन युक्त नमक दुकानों तक पहुँचा और उसे नमी और गर्मी से बचाकर रखा गया, जो आयोडीन को उड़ा देती हैं, वहाँ एक पीढ़ी के भीतर घेंघा बहुत कम हो गया। "
  "सीख यह नहीं है कि हर स्वास्थ्य समस्या का इतना आसान उत्तर होता है, बल्कि यह कि कोई उपाय तब सबसे अच्छा काम करता है जब वह उन लोगों से सबसे कम माँगता है जिनकी सहायता के लिए वह बना है।")
RQ(p, "Main Idea", "easy", "mcq", CRUX, CRUX_HI,
   "The passage tells how goitre was reduced by putting iodine into the salt that every family already bought, so that nobody had to change anything, and draws the lesson that a measure works best when it asks the least of the people it is meant to help. "
   "It does not say that goitre is caused by badly stored salt (damp and heat only drive iodine out of iodised salt; goitre comes from too little iodine in the diet), it expressly denies that every health problem has so easy an answer, "
   "and it does not say that families refused to change their diets -- the government chose not to ask them.",
   "परिच्छेद बताता है कि घेंघा उस नमक में आयोडीन मिलाकर घटाया गया जिसे हर परिवार पहले से ख़रीदता था, ताकि किसी को कुछ बदलना न पड़े, और यह सीख निकालता है कि उपाय तब सबसे अच्छा काम करता है जब वह उन लोगों से सबसे कम माँगता है जिनकी सहायता के लिए वह बना है। "
   "वह यह नहीं कहता कि घेंघा ठीक से न रखे गए नमक से होता है (नमी और गर्मी केवल आयोडीन युक्त नमक से आयोडीन उड़ाती हैं; घेंघा आहार में आयोडीन की कमी से होता है), वह स्पष्ट रूप से नकारता है कि हर स्वास्थ्य समस्या का इतना आसान उत्तर होता है, "
   "और वह यह नहीं कहता कि परिवारों ने अपना भोजन बदलने से इनकार किया -- सरकार ने उनसे कहना ही नहीं चुना।",
   "crux",
   opts=["A health measure works best when it fits into what people already do, as iodised salt did.",
         "Goitre is caused mainly by salt that has been stored in damp and hot conditions.",
         "Most health problems in the hills could be solved by adding nutrients to common foods.",
         "Families in the hills refused to change their diets, so the government had to act through salt makers."],
   opts_hi=["स्वास्थ्य का कोई उपाय तब सबसे अच्छा चलता है जब वह लोगों की रोज़ की आदतों में घुल जाए, जैसे आयोडीन युक्त नमक।",
            "घेंघा मुख्यतः उस नमक से होता है जिसे नमी और गर्मी वाली जगहों पर रखा गया हो।",
            "पहाड़ियों की अधिकांश स्वास्थ्य समस्याएँ आम खाद्य पदार्थों में पोषक तत्व मिलाकर सुलझाई जा सकती हैं।",
            "पहाड़ियों के परिवारों ने अपना भोजन बदलने से इनकार कर दिया, इसलिए सरकार को नमक बनाने वालों के माध्यम से क़दम उठाना पड़ा।"],
   ans=0, pos=3)
RQ(p, "Specific Detail", "easy", "mcq",
   "According to the passage, why was there too little iodine in the diet of people in the hills of northern India?",
   "परिच्छेद के अनुसार, उत्तर भारत की पहाड़ियों के लोगों के आहार में आयोडीन की कमी क्यों थी?",
   "The passage says that in these hills 'centuries of rain and melting snow have washed much of the iodine out of the soil', so food grown there carried little iodine. "
   "Damp and heat are mentioned only as what drives iodine out of iodised salt in storage, not as the cause of the shortage; the passage says nothing about how much salt families in the hills ate, or about salt makers removing iodine.",
   "परिच्छेद कहता है कि इन पहाड़ियों में 'सदियों की वर्षा और पिघलती बर्फ़ ने मिट्टी से आयोडीन का बड़ा भाग बहा दिया है', इसलिए वहाँ उगे भोजन में आयोडीन कम था। "
   "नमी और गर्मी का उल्लेख केवल इस रूप में है कि वे रखे हुए आयोडीन युक्त नमक से आयोडीन उड़ा देती हैं, कमी के कारण के रूप में नहीं; परिच्छेद यह कुछ नहीं कहता कि पहाड़ियों के परिवार कितना नमक खाते थे, या कि नमक बनाने वाले आयोडीन निकाल देते थे।",
   "detail",
   opts=["Rain and melting snow had washed much of the iodine out of the soil.",
         "Families in the hills ate much less salt than families in the plains did.",
         "The salt sold in the hills was kept in damp and hot places, which drove the iodine off.",
         "Salt makers in the hills removed the iodine that was naturally present in the salt."],
   opts_hi=["वर्षा और पिघलती बर्फ़ ने मिट्टी से आयोडीन का बड़ा भाग बहा दिया था।",
            "पहाड़ियों के परिवार मैदानों के परिवारों की तुलना में बहुत कम नमक खाते थे।",
            "पहाड़ियों में बिकने वाला नमक नमी और गर्मी वाली जगहों पर रखा जाता था, जिससे आयोडीन उड़ जाता था।",
            "पहाड़ियों के नमक बनाने वाले नमक में प्राकृतिक रूप से मौजूद आयोडीन निकाल देते थे।"],
   ans=0, pos=0)
RQ(p, "Assumption", "medium", "s2", ASSUME, ASSUME_HI,
   "Only 2 is assumed. The passage's case for the remedy is that the dose 'came with every meal' without anyone changing what they ate; that holds only if families went on buying and using the salt once iodine had been added to it, which the passage takes for granted. "
   "1 is not assumed: the passage claims only that goitre became far less common, which is about fewer new cases, and says nothing about curing goitre that has lasted for years.",
   "केवल 2 पूर्वधारणा है। उपाय के पक्ष में परिच्छेद का तर्क यह है कि ख़ुराक बिना किसी के अपना भोजन बदले 'हर भोजन के साथ आ जाती थी'; यह तभी सही है जब परिवार आयोडीन मिलाए जाने के बाद भी वह नमक ख़रीदते और इस्तेमाल करते रहे, जिसे परिच्छेद मानकर चलता है। "
   "1 पूर्वधारणा नहीं है: परिच्छेद केवल यह कहता है कि घेंघा बहुत कम हो गया, जो नए मामलों के घटने की बात है, और वर्षों पुराने घेंघे के इलाज के बारे में कुछ नहीं कहता।",
   "assumptions",
   st=["Goitre that has lasted for many years can be cured completely by eating iodised salt.",
       "Families would go on buying and using the salt after iodine had been added to it."],
   st_hi=["वर्षों पुराना घेंघा आयोडीन युक्त नमक खाने से पूरी तरह ठीक हो सकता है।",
          "नमक में आयोडीन मिलाए जाने के बाद भी परिवार उसे ख़रीदते और इस्तेमाल करते रहेंगे।"],
   key=1)

# ------------------------------------------------------------------ P02 village tanks (3)
p = passage("p02",
  "In many dry parts of southern India, villages once depended on tanks -- shallow reservoirs that caught the monsoon run-off and fed fields and wells through the dry months. "
  "Each year, after the harvest, the farmers who drew water from a tank removed the silt from its bed and repaired its banks together. The work was hard and unpaid, but every family that used the water took part, "
  "and a family that stayed away was shamed or denied water. As canals, borewells and government departments took over, the tank stopped being the village's only source of water, and its upkeep became somebody else's job. "
  "Silt built up, banks were breached, and the channels that fed the tanks were blocked by roads and houses. Many tanks that held water for centuries now hold it for only a few weeks after the rains. "
  "What was lost was not a structure, which can be rebuilt, but the shared duty that kept it working.",
  "दक्षिण भारत के कई सूखे भागों में गाँव कभी तालाबों पर निर्भर थे -- उथले जलाशय जो मानसून का बहता पानी रोक लेते थे और सूखे महीनों में खेतों और कुओं को पानी देते थे। "
  "हर वर्ष फ़सल कटने के बाद, किसी तालाब से पानी लेने वाले किसान मिलकर उसकी तली से गाद निकालते और उसकी मेड़ों की मरम्मत करते थे। यह काम कठिन और बिना मज़दूरी का था, पर पानी का उपयोग करने वाला हर परिवार इसमें भाग लेता था, "
  "और जो परिवार दूर रहता उसे लज्जित किया जाता या पानी नहीं दिया जाता था। जैसे-जैसे नहरों, नलकूपों और सरकारी विभागों ने जगह ली, तालाब गाँव के पानी का एकमात्र स्रोत नहीं रहा, और उसकी देखभाल किसी और का काम बन गई। "
  "गाद जमती गई, मेड़ें टूटती गईं, और तालाबों तक पानी लाने वाली नालियाँ सड़कों और मकानों से बंद हो गईं। जो कई तालाब सदियों तक पानी रोके रहे, वे अब वर्षा के बाद केवल कुछ सप्ताह पानी रोक पाते हैं। "
  "जो खोया, वह कोई ढाँचा नहीं था, जिसे फिर से बनाया जा सकता है, बल्कि वह साझा कर्तव्य था जो उसे चलाए रखता था।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage traces the tanks' decline to the moment they stopped being the village's only source of water and their upkeep 'became somebody else's job', and it ends by saying that what was lost was the shared duty, not the structure. "
   "It does not compare how much water borewells and canals give with what the tanks gave; it says that a structure can be rebuilt, so the tanks are not beyond repair; and the work had always been hard and unpaid, yet it was done -- that is not what changed.",
   "परिच्छेद तालाबों के पतन को उस समय से जोड़ता है जब वे गाँव के पानी का एकमात्र स्रोत नहीं रहे और उनकी देखभाल 'किसी और का काम बन गई', और अंत में कहता है कि जो खोया वह साझा कर्तव्य था, ढाँचा नहीं। "
   "वह नलकूपों और नहरों से मिलने वाले पानी की तुलना तालाबों के पानी से नहीं करता; वह कहता है कि ढाँचा फिर से बनाया जा सकता है, इसलिए तालाब मरम्मत से परे नहीं हैं; और काम सदा कठिन और बिना मज़दूरी का था, फिर भी होता था -- बदलाव वह नहीं था।",
   "crux",
   opts=["The tanks declined because shared upkeep faded once villages stopped depending on them alone.",
         "Borewells and canals give the dry villages of southern India less water than their old tanks once gave them.",
         "The old tanks can no longer be repaired, because their beds have filled up with silt.",
         "Villagers stopped repairing the tanks because the work was hard and nobody was paid for it."],
   opts_hi=["तालाबों का पतन इसलिए हुआ कि जब गाँव केवल उन पर निर्भर नहीं रहे, तो उनकी साझा देखभाल छूट गई।",
            "नलकूप और नहरें दक्षिण भारत के सूखे गाँवों को उतना पानी नहीं देतीं जितना उनके पुराने तालाब कभी देते थे।",
            "पुराने तालाबों की अब मरम्मत नहीं हो सकती, क्योंकि उनकी तली गाद से भर चुकी है।",
            "गाँव वालों ने तालाबों की मरम्मत बंद कर दी क्योंकि काम कठिन था और उसके लिए कोई मज़दूरी नहीं मिलती थी।"],
   ans=0, pos=2)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Neither is valid. 1: the passage says nothing about the quality of water from borewells or tanks; it says only that borewells, canals and departments took over. "
   "2: the passage says that the tanks' upkeep 'became somebody else's job' -- it describes neglect that followed when no one felt the duty, not a plan by the departments to let the tanks fall into ruin.",
   "कोई भी वैध नहीं है। 1: परिच्छेद नलकूपों या तालाबों के पानी की गुणवत्ता के बारे में कुछ नहीं कहता; वह केवल इतना कहता है कि नलकूपों, नहरों और विभागों ने जगह ले ली। "
   "2: परिच्छेद कहता है कि तालाबों की देखभाल 'किसी और का काम बन गई' -- यह उस उपेक्षा का वर्णन है जो किसी के कर्तव्य न समझने से आई, न कि विभागों की ऐसी योजना का जिससे तालाब नष्ट हो जाएँ।",
   "conclusions",
   st=["Villages turned to borewells because borewells give cleaner water than the tanks did.",
       "The government departments that took over the tanks set out to let them fall into ruin."],
   st_hi=["गाँवों ने नलकूपों का सहारा इसलिए लिया क्योंकि नलकूप तालाबों की तुलना में अधिक स्वच्छ पानी देते हैं।",
          "जिन सरकारी विभागों ने तालाबों का ज़िम्मा लिया, उन्होंने जान-बूझकर उन्हें नष्ट होने दिया।"],
   key=3)
RQ(p, "Inference", "hard", "sc", INFER, INFER_HI,
   "1 can be drawn: nobody in the passage sets out to harm the tanks, yet they decline once their upkeep becomes 'somebody else's job'. 3 can be drawn: a family that stayed away from the yearly work 'was shamed or denied water', "
   "so social pressure helped to keep the users at the work. 2 cannot: silt in the bed and channels blocked by roads and houses would remain, and the passage's point is that a rebuilt structure fails without the shared duty that kept it working. "
   "The inferences that can be drawn are 1 and 3.",
   "1 निकाला जा सकता है: परिच्छेद में कोई तालाबों को हानि पहुँचाने का इरादा नहीं करता, फिर भी उनकी देखभाल 'किसी और का काम' बनते ही उनका पतन होता है। 3 निकाला जा सकता है: वार्षिक काम से दूर रहने वाले परिवार को 'लज्जित किया जाता या पानी नहीं दिया जाता था', "
   "इसलिए सामाजिक दबाव उपयोग करने वालों को काम में लगाए रखता था। 2 नहीं निकाला जा सकता: तली की गाद और सड़कों व मकानों से बंद नालियाँ बनी रहेंगी, और परिच्छेद का मूल बिंदु यही है कि उस साझा कर्तव्य के बिना, जो ढाँचे को चलाए रखता था, फिर से बना ढाँचा भी विफल होता है। "
   "जो अनुमान निकाले जा सकते हैं वे 1 और 3 हैं।",
   "inferences",
   st=["A shared resource can decline even when nobody sets out to damage it.",
       "Rebuilding the banks of a neglected tank would by itself restore its old capacity to hold water.",
       "Social pressure once helped to make sure that the families who used a tank also kept it in repair."],
   st_hi=["कोई साझा संसाधन तब भी नष्ट हो सकता है जब कोई उसे हानि पहुँचाने का इरादा न करे।",
          "उपेक्षित तालाब की मेड़ों को फिर से बना देना अपने-आप उसकी पानी रोकने की पुरानी क्षमता लौटा देगा।",
          "कभी सामाजिक दबाव यह सुनिश्चित करने में सहायक था कि जो परिवार किसी तालाब का उपयोग करते थे, वे उसकी मरम्मत भी करते रहें।"],
   opts=["1 only", "1 and 3 only", "2 and 3 only", "1, 2 and 3"], key=1)

# ------------------------------------------------------------------ P03 online star ratings (2)
p = passage("p03",
  "Before buying a book, booking a hotel or choosing a doctor, many of us now look first at the stars that other customers have given. The average rating feels like the verdict of the crowd, but it is less than that. "
  "Most customers never write a review; those who do tend to be the delighted and the furious, while the many who were merely satisfied stay silent. A product with a few hundred ratings may therefore be judged by a small and unusual group. "
  "Sellers know this, and some ask their happiest buyers to post a review, or pay for praise. None of this makes ratings useless. But a reader who treats an average of stars as a measurement, rather than as a clue, is likely to be misled.",
  "कोई किताब ख़रीदने, होटल बुक करने या डॉक्टर चुनने से पहले, हममें से बहुत से लोग अब सबसे पहले वे सितारे देखते हैं जो दूसरे ग्राहकों ने दिए हैं। औसत रेटिंग भीड़ के फ़ैसले जैसी लगती है, पर वह उससे कम है। "
  "अधिकतर ग्राहक कभी समीक्षा नहीं लिखते; जो लिखते हैं वे प्रायः बहुत प्रसन्न या बहुत नाराज़ लोग होते हैं, जबकि केवल संतुष्ट रहे अनेक लोग चुप रहते हैं। इसलिए कुछ सौ रेटिंग वाले किसी उत्पाद का आकलन एक छोटा और असामान्य समूह कर रहा हो सकता है। "
  "विक्रेता यह जानते हैं, और कुछ अपने सबसे प्रसन्न ख़रीदारों से समीक्षा लिखने को कहते हैं, या प्रशंसा के लिए पैसे देते हैं। इससे रेटिंग बेकार नहीं हो जातीं। पर जो पाठक सितारों के औसत को एक संकेत के बजाय एक माप मान लेता है, उसके भटकने की संभावना है।")
RQ(p, "Main Idea", "easy", "mcq", CRUX, CRUX_HI,
   "The passage says that an average rating is 'less than' the verdict of the crowd, because reviews come mostly from the delighted and the furious and can be pushed by sellers, but it adds that 'none of this makes ratings useless': they are a clue, not a measurement. "
   "It does not call ratings useless, it does not ask for satisfied customers to be made to write reviews, and it says nothing about products with thousands of ratings being better.",
   "परिच्छेद कहता है कि औसत रेटिंग भीड़ के फ़ैसले से 'कम' है, क्योंकि समीक्षाएँ अधिकतर बहुत प्रसन्न और बहुत नाराज़ लोगों से आती हैं और विक्रेता उन्हें प्रभावित कर सकते हैं, पर वह यह भी जोड़ता है कि 'इससे रेटिंग बेकार नहीं हो जातीं': वे संकेत हैं, माप नहीं। "
   "वह रेटिंग को बेकार नहीं कहता, संतुष्ट ग्राहकों से ज़बरदस्ती समीक्षा लिखवाने को नहीं कहता, और हज़ारों रेटिंग वाले उत्पादों के बेहतर होने के बारे में कुछ नहीं कहता।",
   "crux",
   opts=["Online ratings are a useful clue, but they come from a small and unusual group of customers.",
         "Online ratings are useless, because many sellers pay customers to write praise for their products.",
         "Customers who were merely satisfied with a product should be required to write a review of it.",
         "A product with a few hundred ratings is usually worse than one that has many thousands of ratings."],
   opts_hi=["ऑनलाइन रेटिंग एक उपयोगी संकेत हैं, पर वे ग्राहकों के एक छोटे और असामान्य समूह से आती हैं।",
            "ऑनलाइन रेटिंग बेकार हैं, क्योंकि कई विक्रेता अपने उत्पादों की प्रशंसा लिखवाने के लिए ग्राहकों को पैसे देते हैं।",
            "किसी उत्पाद से केवल संतुष्ट रहे ग्राहकों के लिए उसकी समीक्षा लिखना अनिवार्य किया जाना चाहिए।",
            "कुछ सौ रेटिंग वाला उत्पाद प्रायः उस उत्पाद से ख़राब होता है जिसकी हज़ारों रेटिंग हों।"],
   ans=0, pos=3)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Both are valid. 1: since the many merely satisfied buyers stay silent and the reviewers are mostly the delighted and the furious, the average of the reviews can differ from what most buyers thought. "
   "2: the passage says that those who write reviews 'tend to be the delighted and the furious, while the many who were merely satisfied stay silent', so a furious buyer is more likely to rate the product than a merely satisfied one.",
   "दोनों वैध हैं। 1: चूँकि केवल संतुष्ट रहे अनेक ख़रीदार चुप रहते हैं और समीक्षा लिखने वाले अधिकतर बहुत प्रसन्न या बहुत नाराज़ लोग होते हैं, इसलिए समीक्षाओं का औसत अधिकतर ख़रीदारों की राय से अलग हो सकता है। "
   "2: परिच्छेद कहता है कि समीक्षा लिखने वाले 'प्रायः बहुत प्रसन्न या बहुत नाराज़ लोग होते हैं, जबकि केवल संतुष्ट रहे अनेक लोग चुप रहते हैं', इसलिए नाराज़ ख़रीदार के रेटिंग देने की संभावना केवल संतुष्ट ख़रीदार से अधिक है।",
   "conclusions",
   st=["The average rating of a product may differ from what most of its buyers thought of it.",
       "Buyers who were furious with a product are more likely to rate it than buyers who were merely satisfied."],
   st_hi=["किसी उत्पाद की औसत रेटिंग उसके अधिकतर ख़रीदारों की राय से अलग हो सकती है।",
          "किसी उत्पाद से नाराज़ ख़रीदारों के उसे रेटिंग देने की संभावना केवल संतुष्ट ख़रीदारों से अधिक है।"],
   key=2)

# ------------------------------------------------------------------ P04 a 70 per cent chance of rain (3)
p = passage("p04",
  "When a weather office announces a 70 per cent chance of rain for tomorrow, many listeners hear a promise that it will rain, and complain when the day stays dry. But the forecast was not wrong. "
  "It meant that on days like tomorrow, rain falls about seven times in ten; on the other three, it does not. A forecast of this kind can be judged only over many days: if it rains on roughly seven of every ten days that were given a 70 per cent chance, "
  "the forecaster is doing well. Farmers who understand this can use the numbers to decide whether to sow, spray or harvest, weighing the cost of acting against the cost of waiting. "
  "A farmer who expects certainty, on the other hand, may stop listening after a dry day or two, and lose the help that the forecast could have given.",
  "जब कोई मौसम कार्यालय कल के लिए वर्षा की 70 प्रतिशत संभावना बताता है, तो बहुत से सुनने वाले इसे वर्षा होने का वादा समझ लेते हैं, और दिन सूखा रहने पर शिकायत करते हैं। पर पूर्वानुमान ग़लत नहीं था। "
  "उसका अर्थ यह था कि कल जैसे दिनों में दस में से लगभग सात बार वर्षा होती है; बाक़ी तीन में नहीं होती। इस प्रकार के पूर्वानुमान को केवल अनेक दिनों के आधार पर परखा जा सकता है: यदि जिन दिनों के लिए 70 प्रतिशत संभावना बताई गई उनमें से हर दस में से लगभग सात दिन वर्षा होती है, "
  "तो पूर्वानुमानकर्ता अच्छा काम कर रहा है। जो किसान यह समझते हैं, वे इन संख्याओं से यह तय कर सकते हैं कि बुआई करें, छिड़काव करें या कटाई, कुछ करने की लागत को प्रतीक्षा की लागत से तौलते हुए। "
  "दूसरी ओर, जो किसान निश्चितता की अपेक्षा करता है, वह एक-दो सूखे दिनों के बाद सुनना बंद कर सकता है, और वह सहायता खो सकता है जो पूर्वानुमान दे सकता था।")
RQ(p, "Main Idea", "easy", "mcq", CRUX, CRUX_HI,
   "The passage explains that a 70 per cent chance of rain is not a promise, that such forecasts can be judged only over many days, and that farmers who understand them can weigh the cost of acting against the cost of waiting. "
   "It does not ask weather offices to stop giving percentages -- it asks listeners to read them correctly; it says the opposite of 'wrong whenever the day stays dry'; and it sets no rule that farmers should sow only above 70 per cent.",
   "परिच्छेद समझाता है कि वर्षा की 70 प्रतिशत संभावना कोई वादा नहीं है, कि ऐसे पूर्वानुमान केवल अनेक दिनों के आधार पर परखे जा सकते हैं, और कि जो किसान उन्हें समझते हैं वे कुछ करने की लागत को प्रतीक्षा की लागत से तौल सकते हैं। "
   "वह मौसम कार्यालयों से प्रतिशत बताना बंद करने को नहीं कहता -- वह सुनने वालों से उन्हें सही पढ़ने को कहता है; वह 'दिन सूखा रहने पर हर बार ग़लत' का उलटा कहता है; और कोई नियम नहीं बनाता कि किसान केवल 70 प्रतिशत से ऊपर बुआई करें।",
   "crux",
   opts=["A chance-of-rain forecast should be judged over many days and used to weigh choices, not taken as a promise.",
         "Weather offices should stop giving their forecasts in percentages, because farmers find such numbers confusing.",
         "A forecast of a 70 per cent chance of rain has turned out to be wrong whenever the day stays dry.",
         "Farmers should sow their crops only on days for which the chance of rain is above 70 per cent."],
   opts_hi=["वर्षा की संभावना वाले पूर्वानुमान को अनेक दिनों पर परखना और निर्णय तौलने में बरतना चाहिए, उसे वादा नहीं मानना चाहिए।",
            "मौसम कार्यालयों को अपने पूर्वानुमान प्रतिशत में देना बंद कर देना चाहिए, क्योंकि किसानों को ऐसी संख्याएँ भ्रमित करती हैं।",
            "जब भी दिन सूखा रहता है, वर्षा की 70 प्रतिशत संभावना वाला पूर्वानुमान ग़लत साबित होता है।",
            "किसानों को अपनी फ़सलें केवल उन दिनों बोनी चाहिए जिनके लिए वर्षा की संभावना 70 प्रतिशत से अधिक हो।"],
   ans=0, pos=0)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Only 1 is valid: such a forecast 'can be judged only over many days', and on three days in ten like it rain is expected not to fall, so one dry day proves nothing. "
   "2 is not: by the passage's own test, a forecaster does well if it rains on roughly seven of every ten days given a 70 per cent chance. Rain on every one of them would mean that the 70 per cent understated the chance -- the forecasts would be off, not as good as possible.",
   "केवल 1 वैध है: ऐसे पूर्वानुमान को 'केवल अनेक दिनों के आधार पर परखा जा सकता है', और ऐसे हर दस में से तीन दिनों में वर्षा न होना अपेक्षित है, इसलिए एक सूखा दिन कुछ सिद्ध नहीं करता। "
   "2 वैध नहीं है: परिच्छेद की अपनी कसौटी पर पूर्वानुमानकर्ता तब अच्छा काम करता है जब 70 प्रतिशत संभावना वाले हर दस में से लगभग सात दिन वर्षा हो। ऐसे हर दिन वर्षा होने का अर्थ होगा कि 70 प्रतिशत ने संभावना को कम आँका -- पूर्वानुमान चूक रहे होंगे, सबसे अच्छे नहीं।",
   "conclusions",
   st=["A single dry day after a forecast of a 70 per cent chance of rain does not show that the forecast was poor.",
       "A forecaster whose 70 per cent forecasts were followed by rain on every such day would be doing as well as possible."],
   st_hi=["वर्षा की 70 प्रतिशत संभावना के पूर्वानुमान के बाद एक सूखा दिन यह नहीं दिखाता कि पूर्वानुमान ख़राब था।",
          "जिस पूर्वानुमानकर्ता के 70 प्रतिशत वाले पूर्वानुमानों के बाद हर ऐसे दिन वर्षा हुई हो, वह यथासंभव सबसे अच्छा काम कर रहा होगा।"],
   key=0)
RQ(p, "Specific Detail", "medium", "mcq",
   "According to the passage, what does a forecast of a 70 per cent chance of rain mean?",
   "परिच्छेद के अनुसार, वर्षा की 70 प्रतिशत संभावना वाले पूर्वानुमान का क्या अर्थ है?",
   "The passage says that the forecast 'meant that on days like tomorrow, rain falls about seven times in ten'. It is not about the share of the area that gets rain, the share of the day's hours that are wet, "
   "or how many forecasters expect rain -- these are common misreadings that the passage does not support.",
   "परिच्छेद कहता है कि पूर्वानुमान का 'अर्थ यह था कि कल जैसे दिनों में दस में से लगभग सात बार वर्षा होती है'। यह न तो क्षेत्र के उस हिस्से के बारे में है जहाँ वर्षा होगी, न दिन के उन घंटों के हिस्से के बारे में जिनमें वर्षा होगी, "
   "और न इस बारे में कि कितने पूर्वानुमानकर्ता वर्षा की अपेक्षा करते हैं -- ये आम ग़लत अर्थ हैं जिनका परिच्छेद समर्थन नहीं करता।",
   "detail",
   opts=["On days like the one forecast, rain falls about seven times in every ten.",
         "Rain will fall over about 70 per cent of the area that the forecast covers.",
         "Rain will fall for about 70 per cent of the hours of the day that is forecast.",
         "Seven out of every ten forecasters at the weather office expect rain on that day."],
   opts_hi=["पूर्वानुमान वाले दिन जैसे दिनों में दस में से लगभग सात बार वर्षा होती है।",
            "पूर्वानुमान वाले क्षेत्र के लगभग 70 प्रतिशत भाग पर वर्षा होगी।",
            "पूर्वानुमान वाले दिन के लगभग 70 प्रतिशत घंटों में वर्षा होगी।",
            "मौसम कार्यालय के हर दस में से सात पूर्वानुमानकर्ता उस दिन वर्षा की अपेक्षा करते हैं।"],
   ans=0, pos=3)

# ------------------------------------------------------------------ P05 free play (3)
p = passage("p05",
  "Parents who fill every hour of a child's day with classes -- music on Monday, coding on Tuesday, tuition every evening -- usually do so out of love and worry. Yet something is lost when no time is left over. "
  "In free play, with no adult in charge, children invent games, quarrel over the rules and settle the quarrels themselves; they take small risks, fail and try again. "
  "These are the beginnings of skills that no class teaches directly: planning, bargaining and bearing disappointment. A child who is always instructed may learn a great deal and still find it hard to decide what to do when nobody is giving instructions. "
  "None of this argues against classes. It argues for leaving some hours empty, and for trusting children to fill them.",
  "जो माता-पिता बच्चे के दिन का हर घंटा कक्षाओं से भर देते हैं -- सोमवार को संगीत, मंगलवार को कोडिंग, हर शाम ट्यूशन -- वे प्रायः प्रेम और चिंता के कारण ऐसा करते हैं। फिर भी जब कोई समय ख़ाली नहीं बचता, तो कुछ खो जाता है। "
  "मुक्त खेल में, जब कोई वयस्क देखरेख नहीं कर रहा होता, बच्चे खेल गढ़ते हैं, नियमों पर झगड़ते हैं और झगड़े स्वयं सुलझाते हैं; वे छोटे जोखिम उठाते हैं, असफल होते हैं और फिर प्रयास करते हैं। "
  "ये उन कौशलों की शुरुआत है जिन्हें कोई कक्षा सीधे नहीं सिखाती: योजना बनाना, मोलभाव करना और निराशा सहना। जिस बच्चे को सदा निर्देश मिलते रहे हों, वह बहुत कुछ सीखकर भी यह तय करने में कठिनाई महसूस कर सकता है कि जब कोई निर्देश न दे रहा हो तब क्या करे। "
  "इनमें से कुछ भी कक्षाओं के विरुद्ध तर्क नहीं है। यह कुछ घंटे ख़ाली छोड़ने, और उन्हें भरने के लिए बच्चों पर भरोसा करने के पक्ष में तर्क है।")
RQ(p, "Best Summary", "medium", "mcq", SUMMARY, SUMMARY_HI,
   "The passage argues that free play, with no adult in charge, builds skills that 'no class teaches directly', and that this is a reason to leave some hours empty -- while saying that 'none of this argues against classes'. "
   "It does not tell parents to stop sending children to classes; it explains crowded timetables by 'love and worry', not by parents lacking time; and it says the opposite of 'only when adults teach them directly'.",
   "परिच्छेद का तर्क है कि मुक्त खेल, जिसमें कोई वयस्क देखरेख नहीं करता, वे कौशल बनाता है जिन्हें 'कोई कक्षा सीधे नहीं सिखाती', और यह कुछ घंटे ख़ाली छोड़ने का कारण है -- साथ ही वह कहता है कि 'इनमें से कुछ भी कक्षाओं के विरुद्ध तर्क नहीं है'। "
   "वह माता-पिता से बच्चों को कक्षाओं में भेजना बंद करने को नहीं कहता; भरे हुए दिनों का कारण 'प्रेम और चिंता' बताता है, माता-पिता के पास समय की कमी नहीं; और 'केवल तब जब वयस्क सीधे सिखाएँ' का उलटा कहता है।",
   "summary",
   opts=["Free play builds skills that classes do not teach, so children's days should keep some hours free of instruction.",
         "Classes in music and coding do children more harm than good, and parents should stop sending them to such classes.",
         "Parents fill their children's days with classes because they do not have the time to play with the children themselves.",
         "Children learn to plan and to bear disappointment only when adults teach them these skills directly and patiently."],
   opts_hi=["मुक्त खेल वे कौशल बनाता है जो कक्षाएँ नहीं सिखातीं, इसलिए बच्चों के दिन में कुछ घंटे निर्देश से मुक्त रहने चाहिए।",
            "संगीत और कोडिंग की कक्षाएँ बच्चों को लाभ से अधिक हानि पहुँचाती हैं, और माता-पिता को उन्हें ऐसी कक्षाओं में भेजना बंद कर देना चाहिए।",
            "माता-पिता बच्चों के दिन कक्षाओं से इसलिए भर देते हैं क्योंकि उनके पास स्वयं बच्चों के साथ खेलने का समय नहीं होता।",
            "बच्चे योजना बनाना और निराशा सहना तभी सीखते हैं जब वयस्क उन्हें ये कौशल सीधे और धैर्य से सिखाएँ।"],
   ans=0, pos=2)
RQ(p, "Assumption", "hard", "s2", ASSUME, ASSUME_HI,
   "Only 2 is assumed. The passage's case for empty hours rests on what children do in free play -- invent games, quarrel over rules and settle the quarrels -- and it asks parents to trust children to fill the hours; "
   "this works only if children given free time do, at least some of the time, play with other children rather than spend it all alone or idle. "
   "1 is not assumed: the passage says that a child who is always instructed 'may learn a great deal', so it does not take such children to learn less in all.",
   "केवल 2 पूर्वधारणा है। ख़ाली घंटों के पक्ष में परिच्छेद का तर्क इस पर टिका है कि बच्चे मुक्त खेल में क्या करते हैं -- खेल गढ़ते हैं, नियमों पर झगड़ते हैं और झगड़े सुलझाते हैं -- और वह माता-पिता से घंटे भरने के लिए बच्चों पर भरोसा करने को कहता है; "
   "यह तभी चलता है जब ख़ाली समय पाने वाले बच्चे कम से कम कुछ समय दूसरे बच्चों के साथ खेलें, न कि सारा समय अकेले या बेकार बिताएँ। "
   "1 पूर्वधारणा नहीं है: परिच्छेद कहता है कि सदा निर्देश पाने वाला बच्चा 'बहुत कुछ सीख' सकता है, इसलिए वह यह नहीं मानता कि ऐसे बच्चे कुल मिलाकर कम सीखते हैं।",
   "assumptions",
   st=["Children who attend many classes learn less in all than children who attend none.",
       "Children given free hours will use at least some of them to play with other children."],
   st_hi=["जो बच्चे अनेक कक्षाओं में जाते हैं वे कुल मिलाकर उन बच्चों से कम सीखते हैं जो किसी कक्षा में नहीं जाते।",
          "ख़ाली घंटे पाने वाले बच्चे उनमें से कम से कम कुछ घंटे दूसरे बच्चों के साथ खेलने में लगाएँगे।"],
   key=1)
RQ(p, "Author's Tone", "medium", "mcq", TONE, TONE_HI,
   "The author grants that parents act 'out of love and worry', which is sympathetic, and states that 'none of this argues against classes', yet holds firmly that some hours should be left empty. "
   "That rules out scorn for such parents, rules out neutrality (the author takes a side: leave some hours free), and rules out alarm that children no longer know how to play -- the passage describes children playing well when given the chance.",
   "लेखक मानता है कि माता-पिता 'प्रेम और चिंता के कारण' ऐसा करते हैं, जो सहानुभूतिपूर्ण है, और कहता है कि 'इनमें से कुछ भी कक्षाओं के विरुद्ध तर्क नहीं है', फिर भी दृढ़ता से मानता है कि कुछ घंटे ख़ाली छोड़े जाने चाहिए। "
   "इससे ऐसे माता-पिता के प्रति तिरस्कार का भाव ख़ारिज होता है, तटस्थता भी (लेखक एक पक्ष लेता है: कुछ घंटे ख़ाली रखें), और यह चिंता भी कि बच्चे अब खेलना ही नहीं जानते -- परिच्छेद अवसर मिलने पर बच्चों के अच्छी तरह खेलने का वर्णन करता है।",
   "tone",
   opts=["Sympathetic to worried parents, but firm that children need some free time",
         "Scornful of parents who send their children to many classes",
         "Neutral, listing the benefits of classes and of play without taking any side",
         "Alarmed that children today no longer know how to play with one another at all"],
   opts_hi=["चिंतित माता-पिता से सहानुभूति, पर दृढ़ कि बच्चों को कुछ ख़ाली समय चाहिए",
            "बच्चों को अनेक कक्षाओं में भेजने वाले माता-पिता के प्रति तिरस्कारपूर्ण",
            "तटस्थ, कक्षाओं और खेल दोनों के लाभ गिनाता हुआ, बिना कोई पक्ष लिए",
            "इस बात से घबराया हुआ कि आज के बच्चे एक-दूसरे के साथ खेलना बिल्कुल भी नहीं जानते"],
   ans=0, pos=3)
