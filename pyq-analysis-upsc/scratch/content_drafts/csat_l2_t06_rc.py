# -*- coding: utf-8 -*-
"""CSAT Level 2 · Test 6 -- Reading Comprehension: 10 original passages, 28 items (8 x 3, 2 x 2).

Themes, none used in Tests 1-5: groundwater and free power for pumps, translated literature, plastic carried by
rivers, secrecy in political donations, crowds at heritage sites, the stigma of vocational courses, the closing of
local newspapers, sorting waste at home, wetlands and urban floods, and street vendors. Item types: main idea 7,
inference 8, assumption 5, tone 1, specific detail 4 (one of them 'which is NOT correct'), best summary 3.
Options are named by content in every explanation."""
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
NOTCORRECT = "Which one of the following statements is NOT correct according to the passage?"
NOTCORRECT_HI = "परिच्छेद के अनुसार निम्नलिखित में से कौन-सा कथन सही नहीं है?"

# ------------------------------------------------------------------ P01 groundwater and free power (3)
p = passage("p01",
  "India draws more groundwater than any other country, mostly to irrigate crops, and in some regions the water table is falling by a metre or more a year. Part of the reason lies not in the fields but in the price of electricity. "
  "When the power that runs a farmer's pump is free or heavily subsidised, pumping for one more hour costs nothing, and there is no reason to save water or to grow a less thirsty crop. Meters and higher tariffs meet fierce opposition, "
  "since farmers fear that the next step is a bill they cannot pay. Some States have therefore tried a different route: they give farmers a fixed number of hours of supply a day and pay them, in cash, for any electricity that they do not use. "
  "The water saved is real, and so is the sense of being rewarded rather than punished.",
  "भारत किसी भी अन्य देश से अधिक भूजल निकालता है, मुख्यतः फ़सलों की सिंचाई के लिए, और कुछ क्षेत्रों में जल-स्तर हर वर्ष एक मीटर या उससे अधिक गिर रहा है। इसका एक कारण खेतों में नहीं बल्कि बिजली की क़ीमत में है। "
  "जब किसान के पंप को चलाने वाली बिजली मुफ़्त या भारी रियायती हो, तो एक घंटा और पंप चलाने में कुछ ख़र्च नहीं होता, और पानी बचाने या कम पानी माँगने वाली फ़सल उगाने का कोई कारण नहीं रहता। मीटर और ऊँची दरों का कड़ा विरोध होता है, "
  "क्योंकि किसानों को डर है कि अगला क़दम ऐसा बिल होगा जो वे चुका नहीं सकते। इसलिए कुछ राज्यों ने एक अलग रास्ता आज़माया है: वे किसानों को प्रतिदिन आपूर्ति के निश्चित घंटे देते हैं और जो बिजली वे उपयोग नहीं करते, उसके लिए उन्हें नक़द भुगतान करते हैं। "
  "बचा हुआ पानी वास्तविक है, और वास्तविक है दंडित होने के बजाय पुरस्कृत होने का एहसास भी।")
RQ(p, "Main Idea", "easy", "mcq", CRUX, CRUX_HI,
   "The passage traces the fall of the water table partly to free power, which makes wasting water cost nothing, and ends with States that pay farmers for the electricity they save. "
   "It does not blame carelessness; it says that higher tariffs meet fierce opposition and so describes a different route, not full prices; and it never says that the rains have failed.",
   "परिच्छेद जल-स्तर के गिरने को आंशिक रूप से मुफ़्त बिजली से जोड़ता है, जिससे पानी बर्बाद करने में कुछ ख़र्च नहीं होता, और उन राज्यों पर समाप्त होता है जो किसानों को बचाई गई बिजली के लिए भुगतान करते हैं। "
   "वह लापरवाही को दोष नहीं देता; वह कहता है कि ऊँची दरों का कड़ा विरोध होता है, इसलिए पूरी क़ीमत नहीं बल्कि एक अलग रास्ता बताता है; और वह कहीं नहीं कहता कि वर्षा विफल रही है।",
   "crux",
   opts=["Free power makes farmers waste water, so paying them to use less power may save it.",
         "Indian farmers pump more groundwater than farmers elsewhere because they are careless with water.",
         "Farmers should be charged the full price of electricity so that they stop pumping groundwater.",
         "The water table is falling because the rains in India have failed over the years."],
   opts_hi=["मुफ़्त बिजली पानी की बर्बादी कराती है, इसलिए बिजली बचाने पर भुगतान देना पानी बचा सकता है।",
            "भारतीय किसान दूसरी जगह के किसानों से अधिक भूजल इसलिए निकालते हैं कि वे पानी के प्रति लापरवाह हैं।",
            "किसानों से बिजली की पूरी क़ीमत वसूली जानी चाहिए ताकि वे भूजल निकालना बंद कर दें।",
            "जल-स्तर इसलिए गिर रहा है कि भारत में वर्षों से वर्षा विफल होती रही है।"],
   ans=0, pos=0)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Only 2 is valid: paying farmers for the electricity they do not use gives them a reason to pump less. 1 overstates the passage, which says that farmers would resist meters and higher tariffs because they fear a bill they cannot pay, "
   "not that they would stop pumping if they had to pay.",
   "केवल 2 वैध है: जो बिजली किसान उपयोग नहीं करते उसके लिए भुगतान उन्हें कम पंप चलाने का कारण देता है। 1 परिच्छेद को बढ़ा-चढ़ाकर कहता है, जो कहता है कि किसान मीटर और ऊँची दरों का विरोध करेंगे क्योंकि उन्हें ऐसे बिल का डर है जो वे चुका नहीं सकते, "
   "यह नहीं कि बिजली के लिए भुगतान करना पड़े तो वे पंप चलाना बंद कर देंगे।",
   "conclusions",
   st=["Farmers would stop pumping groundwater altogether if they had to pay for the electricity.",
       "Paying farmers for the electricity they do not use gives them a reason to pump less."],
   st_hi=["बिजली के लिए भुगतान करना पड़े तो किसान भूजल निकालना पूरी तरह बंद कर देंगे।",
          "जो बिजली किसान उपयोग नहीं करते उसके लिए भुगतान उन्हें कम पंप चलाने का कारण देता है।"],
   key=1)
RQ(p, "Assumption", "hard", "s2", ASSUME, ASSUME_HI,
   "Only 1 is assumed. The scheme of paying farmers in cash for unused electricity can save water only if farmers do pump less when they are paid to. "
   "2 is not needed: the argument says nothing of other sources of water, and works just as well if farmers have them.",
   "केवल 1 पूर्वधारणा है। उपयोग न की गई बिजली के लिए किसानों को नक़द भुगतान की योजना पानी तभी बचा सकती है जब भुगतान मिलने पर किसान सचमुच कम पंप चलाएँ। "
   "2 की ज़रूरत नहीं: तर्क पानी के दूसरे स्रोतों के बारे में कुछ नहीं कहता, और किसानों के पास वे हों तब भी उतना ही ठीक चलता है।",
   "assumptions",
   st=["Farmers will pump less water when they are paid in cash for the electricity they save.",
       "Farmers have no other source of water for their crops."],
   st_hi=["बचाई गई बिजली के लिए नक़द भुगतान मिलने पर किसान कम पानी निकालेंगे।",
          "किसानों के पास अपनी फ़सलों के लिए पानी का कोई दूसरा स्रोत नहीं है।"],
   key=0)

# ------------------------------------------------------------------ P02 translated literature (3)
p = passage("p02",
  "A novel written in Odia or Malayalam is read by the people who speak that language; a translation into English can reach hundreds of millions more, and a translation into another Indian language reaches readers who would "
  "otherwise never have met it. Yet translation is poorly paid, publishers often treat it as a favour to the author, and the translator's name may not even appear on the cover. Good translation is not a mechanical exchange of words: "
  "it asks for a feeling for both languages, and a translator who knows one of them well and the other only from a dictionary will produce prose that no one wants to read. Readers who pick up a translated book usually credit the author "
  "for its beauty and blame the translator for its faults, a poor reward for the person who made the reading possible.",
  "ओड़िया या मलयालम में लिखा उपन्यास उस भाषा को बोलने वाले लोग पढ़ते हैं; अंग्रेज़ी में उसका अनुवाद करोड़ों और पाठकों तक पहुँच सकता है, और किसी दूसरी भारतीय भाषा में अनुवाद उन पाठकों तक पहुँचता है जो अन्यथा उससे कभी मिलते ही नहीं। "
  "फिर भी अनुवाद का पारिश्रमिक कम है, प्रकाशक उसे प्रायः लेखक पर एहसान की तरह देखते हैं, और अनुवादक का नाम आवरण पर आता तक नहीं। अच्छा अनुवाद शब्दों की यांत्रिक अदला-बदली नहीं है: "
  "उसके लिए दोनों भाषाओं की समझ चाहिए, और जो अनुवादक एक भाषा अच्छी तरह जानता हो और दूसरी केवल शब्दकोश से, वह ऐसा गद्य रचेगा जिसे कोई पढ़ना न चाहे। अनुवादित पुस्तक उठाने वाले पाठक प्रायः उसकी सुंदरता का श्रेय लेखक को देते हैं "
  "और उसकी कमियों का दोष अनुवादक को, जो पढ़ना संभव बनाने वाले व्यक्ति के लिए एक खोटा प्रतिफल है।")
RQ(p, "Best Summary", "medium", "mcq", MSG, MSG_HI,
   "The passage says that translation takes a novel to far more readers, that it is poorly paid and unrecognised, and that it needs real skill in both languages. "
   "It does not say translations are poorer than the originals, only that bad ones are possible; it does not ask for novels to be written in English; and it does not ask publishers to stop translating.",
   "परिच्छेद कहता है कि अनुवाद उपन्यास को कहीं अधिक पाठकों तक ले जाता है, कि उसका पारिश्रमिक कम है और उसे पहचान नहीं मिलती, और कि उसके लिए दोनों भाषाओं में वास्तविक कौशल चाहिए। "
   "वह यह नहीं कहता कि अनुवाद मूल से कमतर होते हैं, केवल यह कि बुरे अनुवाद संभव हैं; वह उपन्यास अंग्रेज़ी में लिखे जाने की माँग नहीं करता; और वह प्रकाशकों से अनुवाद बंद करने को नहीं कहता।",
   "message",
   opts=["Translation widens a book's readership but is undervalued, though it needs real skill in two languages.",
         "Translated books are poorer than the originals because translators do not know the original language well.",
         "Writers should write in English, so that readers in other languages need not rely on translators.",
         "Publishers should stop translating books until translators are paid as much as authors are."],
   opts_hi=["अनुवाद पुस्तक के पाठक बढ़ाता है पर उसे कम आँका जाता है, जबकि उसमें दो भाषाओं में कौशल चाहिए।",
            "अनुवादित पुस्तकें मूल से कमतर होती हैं क्योंकि अनुवादक मूल भाषा को अच्छी तरह नहीं जानते।",
            "लेखकों को अंग्रेज़ी में लिखना चाहिए ताकि दूसरी भाषाओं के पाठकों को अनुवादकों पर निर्भर न रहना पड़े।",
            "जब तक अनुवादकों को लेखकों जितना पारिश्रमिक न मिले, प्रकाशकों को पुस्तकों का अनुवाद बंद कर देना चाहिए।"],
   ans=0, pos=3)
RQ(p, "Inference", "medium", "sc", INFER, INFER_HI,
   "1 and 2 follow. Readers 'credit the author for its beauty and blame the translator for its faults', so a translated book that succeeds is likely to bring the praise to the author (1); and a reader who cannot read the original "
   "has only the translation to go by, so its quality depends on the translator (2). 3 contradicts the passage, which says that translation is poorly paid.",
   "1 और 2 निकलते हैं। पाठक 'सुंदरता का श्रेय लेखक को और कमियों का दोष अनुवादक को' देते हैं, इसलिए जो अनुवादित पुस्तक सफल होती है उसकी प्रशंसा लेखक को मिलने की संभावना है (1); और जो पाठक मूल नहीं पढ़ सकता उसके पास केवल अनुवाद है, "
   "इसलिए उसकी गुणवत्ता अनुवादक पर निर्भर करती है (2)। 3 परिच्छेद का खंडन करता है, जो कहता है कि अनुवाद का पारिश्रमिक कम है।",
   "inferences",
   st=["A translated book that succeeds is likely to bring praise to the author rather than to the translator.",
       "A reader who cannot read the original language depends on the translator for the quality of what he reads.",
       "Translators are paid more than authors are."],
   st_hi=["जो अनुवादित पुस्तक सफल होती है, उसकी प्रशंसा अनुवादक के बजाय लेखक को मिलने की संभावना है।",
          "जो पाठक मूल भाषा नहीं पढ़ सकता, वह जो पढ़ता है उसकी गुणवत्ता के लिए अनुवादक पर निर्भर है।",
          "अनुवादकों को लेखकों से अधिक पारिश्रमिक मिलता है।"],
   opts=["1 only", "2 and 3 only", "1 and 2 only", "1, 2 and 3"], key=2)
RQ(p, "Specific Detail", "easy", "mcq",
   "According to the passage, what do readers who pick up a translated book usually do?",
   "परिच्छेद के अनुसार, अनुवादित पुस्तक उठाने वाले पाठक प्रायः क्या करते हैं?",
   "The passage says that readers 'usually credit the author for its beauty and blame the translator for its faults'. The opposite -- crediting the translator and blaming the author -- is not what it reports; "
   "reading the original beside the translation and looking only for the translator's name are not mentioned at all.",
   "परिच्छेद कहता है कि पाठक 'प्रायः सुंदरता का श्रेय लेखक को देते हैं और कमियों का दोष अनुवादक को'। इसका उलटा -- अनुवादक को श्रेय और लेखक को दोष -- वह नहीं बताता; "
   "मूल को अनुवाद के साथ रखकर पढ़ना और केवल अनुवादक का नाम खोजना, इनका उल्लेख ही नहीं है।",
   "detail",
   opts=["They credit the translator for the book's beauty and blame the author for its faults.",
         "They credit the author for the book's beauty and blame the translator for its faults.",
         "They read the original and the translation together so as to compare the two of them.",
         "They ignore the author altogether and look only for the name of the translator."],
   opts_hi=["वे पुस्तक की सुंदरता का श्रेय अनुवादक को और उसकी कमियों का दोष लेखक को देते हैं।",
            "वे पुस्तक की सुंदरता का श्रेय लेखक को और उसकी कमियों का दोष अनुवादक को देते हैं।",
            "वे मूल और अनुवाद को साथ-साथ पढ़ते हैं ताकि दोनों की तुलना कर सकें।",
            "वे लेखक को पूरी तरह अनदेखा करते हैं और केवल अनुवादक का नाम खोजते हैं।"],
   ans=1, pos=1)

# ------------------------------------------------------------------ P03 plastic carried by rivers (3)
p = passage("p03",
  "Much of the plastic in the oceans comes not from ships but from the land, and much of that is carried to the sea by rivers, which collect bags, bottles and packaging from the towns along their banks and wash them down in the monsoon. "
  "A small number of rivers, flowing past crowded cities that collect their waste poorly, carry most of the load. Cleaning beaches, or sweeping the sea, deals with the plastic after it has arrived, and is a little like mopping the floor "
  "while the tap is running. Collecting waste properly in the towns on a river's banks, and stopping the worst items from being made, costs less than hauling plastic out of the water, and it works at the source of the problem.",
  "समुद्रों में पड़े प्लास्टिक का बड़ा भाग जहाज़ों से नहीं बल्कि ज़मीन से आता है, और उसका अधिकांश नदियों द्वारा समुद्र तक पहुँचाया जाता है, जो अपने किनारे बसे कस्बों से थैले, बोतलें और पैकेजिंग बटोरकर उन्हें मानसून में बहा ले जाती हैं। "
  "कुछ ही नदियाँ, जो भीड़ भरे ऐसे शहरों के पास से बहती हैं जो अपना कचरा ठीक से इकट्ठा नहीं करते, अधिकांश बोझ ढोती हैं। समुद्र तटों की सफ़ाई, या समुद्र की झाड़ू, प्लास्टिक के आ जाने के बाद उससे निपटती है, और कुछ वैसी ही है जैसे नल चालू रहते "
  "फ़र्श पर पोंछा लगाना। नदी के किनारे के कस्बों में कचरा ठीक से इकट्ठा करना, और सबसे बुरी वस्तुओं का बनना रोकना, पानी से प्लास्टिक निकालने से सस्ता पड़ता है, और वह समस्या के स्रोत पर काम करता है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage argues that plastic should be stopped at its source, in the towns on the rivers, rather than cleared from beaches and seas after it has arrived. "
   "It does not say that beach clean-ups are the most effective way; it says the plastic comes from the land, not from ships; and it asks for better collection in river towns, not for rivers to be kept away from them.",
   "परिच्छेद तर्क देता है कि प्लास्टिक को उसके स्रोत पर, नदियों के किनारे के कस्बों में, रोकना चाहिए, उसके आ जाने के बाद तटों और समुद्र से साफ़ करने के बजाय। "
   "वह यह नहीं कहता कि तटों की सफ़ाई सबसे प्रभावी तरीका है; वह कहता है कि प्लास्टिक ज़मीन से आता है, जहाज़ों से नहीं; और वह नदी के कस्बों में बेहतर संग्रह माँगता है, नदियों को उनसे दूर रखना नहीं।",
   "crux",
   opts=["Beach clean-ups are the most effective way to keep plastic out of the oceans.",
         "Ships and fishing boats are the main source of the plastic that is found in the oceans today.",
         "Stopping plastic before it enters rivers does more good than clearing beaches and seas.",
         "Rivers must be kept away from towns so that no waste can reach them."],
   opts_hi=["तटों की सफ़ाई महासागरों को प्लास्टिक से मुक्त रखने का सबसे प्रभावी तरीका है।",
            "महासागरों में आज मिलने वाले प्लास्टिक का मुख्य स्रोत जहाज़ और मछली पकड़ने की नावें हैं।",
            "नदियों में पहुँचने से पहले प्लास्टिक रोकना, तटों और समुद्र की सफ़ाई से अधिक लाभकारी है।",
            "नदियों को कस्बों से दूर रखना चाहिए ताकि कोई कचरा उन तक न पहुँच सके।"],
   ans=2, pos=2)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Both are valid. Rivers carry the plastic of the towns along their banks down to the sea, so a town far from the coast can still add to what reaches it (1); and since the plastic comes from the towns, collecting their waste properly "
   "can reduce the load (2).",
   "दोनों वैध हैं। नदियाँ अपने किनारे के कस्बों का प्लास्टिक समुद्र तक बहा ले जाती हैं, इसलिए तट से दूर का कोई कस्बा भी उसमें योगदान दे सकता है (1); और चूँकि प्लास्टिक कस्बों से आता है, उनका कचरा ठीक से इकट्ठा करना "
   "बोझ घटा सकता है (2)।",
   "conclusions",
   st=["Plastic thrown away in a town far from the coast may end up in the sea.",
       "Better collection of waste in river towns can reduce the plastic that reaches the sea."],
   st_hi=["तट से दूर किसी कस्बे में फेंका गया प्लास्टिक समुद्र में पहुँच सकता है।",
          "नदी के कस्बों में कचरे का बेहतर संग्रह समुद्र तक पहुँचने वाले प्लास्टिक को घटा सकता है।"],
   key=2)
RQ(p, "Assumption", "hard", "sc", ASSUME, ASSUME_HI,
   "2 and 3 are assumed. Stopping 'the worst items from being made' takes for granted that they can be identified and their making stopped (2), and the plan to collect waste properly in river towns takes for granted that "
   "the poor collection there can be improved (3). 1 is not assumed: the passage says that cleaning deals with plastic 'after it has arrived', not that nothing can be done once plastic is in the sea.",
   "2 और 3 पूर्वधारणाएँ हैं। 'सबसे बुरी वस्तुओं का बनना रोकना' मानकर चलता है कि उन्हें पहचाना और उनका बनना रोका जा सकता है (2), और नदी के कस्बों में कचरा ठीक से इकट्ठा करने की योजना मानकर चलती है कि वहाँ का ख़राब संग्रह सुधारा जा सकता है (3)। "
   "1 पूर्वधारणा नहीं है: परिच्छेद कहता है कि सफ़ाई प्लास्टिक के 'आ जाने के बाद' उससे निपटती है, यह नहीं कि समुद्र में प्लास्टिक पहुँच जाने पर कुछ भी नहीं किया जा सकता।",
   "assumptions",
   st=["Plastic that has reached the sea cannot be removed at all.",
       "The worst plastic items can be identified and their making stopped.",
       "Poor collection of waste in river towns can be improved."],
   st_hi=["जो प्लास्टिक समुद्र तक पहुँच चुका है उसे बिल्कुल निकाला नहीं जा सकता।",
          "सबसे बुरी प्लास्टिक वस्तुओं को पहचाना जा सकता है और उनका बनना रोका जा सकता है।",
          "नदी के कस्बों में कचरे के ख़राब संग्रह को सुधारा जा सकता है।"],
   opts=["1 only", "1 and 2 only", "1 and 3 only", "2 and 3 only"], key=3)

# ------------------------------------------------------------------ P04 secrecy in political donations (2)
p = passage("p04",
  "Elections are expensive, and the money to fight them has to come from somewhere. When donors give large sums in secret, voters cannot know whom a party may owe a favour, and the donors, who know that no one will find out, "
  "have little to fear from asking for one. Supporters of secrecy argue that open donations expose donors to harassment by rivals in power, which is a real danger, and that some of the money is a harmless wish to support a cause. "
  "But the answer to harassment is protection against it, not darkness for all. A system that lets citizens see who pays for politics treats them as adults who can judge for themselves what such gifts may buy.",
  "चुनाव महँगे होते हैं, और उन्हें लड़ने का धन कहीं न कहीं से आना ही है। जब दानदाता बड़ी रक़में गुप्त रूप से देते हैं, तो मतदाता यह नहीं जान सकते कि किसी दल पर किसका एहसान हो सकता है, और दानदाता, जो जानते हैं कि किसी को पता नहीं चलेगा, "
  "उसे माँगने में कोई ख़तरा नहीं देखते। गोपनीयता के समर्थक तर्क देते हैं कि खुला दान दानदाताओं को सत्ता में बैठे विरोधियों के उत्पीड़न का शिकार बना देता है, जो वास्तविक ख़तरा है, और कि कुछ धन किसी उद्देश्य का समर्थन करने की निर्दोष इच्छा है। "
  "पर उत्पीड़न का उत्तर उससे सुरक्षा है, सबके लिए अँधेरा नहीं। जो व्यवस्था नागरिकों को यह देखने देती है कि राजनीति का ख़र्च कौन उठाता है, वह उन्हें ऐसे वयस्क मानती है जो स्वयं तय कर सकते हैं कि ऐसे उपहार क्या ख़रीद सकते हैं।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage argues that donations to parties should be open, because secrecy hides what donors may expect in return; the risk of harassment is met by protecting donors, not by hiding every gift. "
   "It does not say donors should give in secret, which is the view it answers; it never asks for the state to fund elections; and it speaks of what donors may expect, not of favours that are certain.",
   "परिच्छेद तर्क देता है कि दलों को दिए जाने वाले दान खुले होने चाहिए, क्योंकि गोपनीयता यह छिपा देती है कि दानदाता बदले में क्या अपेक्षा कर सकते हैं; उत्पीड़न का जोखिम दानदाताओं की सुरक्षा से सुलझता है, हर उपहार को छिपाने से नहीं। "
   "वह यह नहीं कहता कि दानदाता गुप्त रूप से दें, जो उस मत का उत्तर है जिसका वह उत्तर देता है; वह कहीं नहीं कहता कि राज्य चुनावों का ख़र्च उठाए; और वह इसकी बात करता है कि दानदाता क्या अपेक्षा कर सकते हैं, निश्चित एहसानों की नहीं।",
   "crux",
   opts=["Donors should be allowed to give in secret, because open giving exposes them to harassment.",
         "The state should pay for elections entirely, so that parties need no donors at all.",
         "Every party that takes a large donation is certain to do a favour for the donor.",
         "Donations to parties should be public, since secrecy hides what donors expect in return."],
   opts_hi=["दानदाताओं को गुप्त रूप से देने की अनुमति होनी चाहिए, क्योंकि खुले रूप से देने पर उनका उत्पीड़न हो सकता है।",
            "राज्य को चुनावों का पूरा ख़र्च उठाना चाहिए ताकि दलों को किसी दानदाता की ज़रूरत ही न रहे।",
            "बड़ा दान लेने वाला हर दल दानदाता का कोई एहसान चुकाएगा, यह निश्चित है।",
            "दलों को मिलने वाले दान सार्वजनिक हों, क्योंकि गोपनीयता यह छिपाती है कि दानदाता बदले में क्या चाहते हैं।"],
   ans=3, pos=3)
RQ(p, "Author's Tone", "medium", "mcq",
   "The author's attitude towards the argument for secret donations is best described as:",
   "गुप्त दान के पक्ष में दिए गए तर्क के प्रति लेखक का दृष्टिकोण सबसे अच्छी तरह कैसा बताया जा सकता है?",
   "The author grants that the danger of harassment is 'real', but answers that protection, not secrecy, is the remedy: respect for the concern, with no agreement with the remedy. "
   "The passage is not scornful of the argument, does not accept it, and is plainly not unconcerned about whether donations are secret.",
   "लेखक मानता है कि उत्पीड़न का ख़तरा 'वास्तविक' है, पर उत्तर देता है कि उपाय गोपनीयता नहीं, सुरक्षा है: चिंता के प्रति आदर, पर उपाय से असहमति। "
   "परिच्छेद उस तर्क के प्रति तिरस्कारपूर्ण नहीं है, उसे स्वीकार भी नहीं करता, और इस बात के प्रति स्पष्ट रूप से उदासीन नहीं है कि दान गुप्त हैं या नहीं।",
   "tone",
   opts=["respectful of its concern but unconvinced by the remedy",
         "scornful of it as a mere cover for corruption",
         "wholly persuaded by the case that it makes",
         "unconcerned about whether donations are kept secret or made open"],
   opts_hi=["उसकी चिंता के प्रति आदरपूर्ण पर उपाय से असंतुष्ट",
            "उसे भ्रष्टाचार का महज़ पर्दा मानकर तिरस्कारपूर्ण",
            "उसके द्वारा प्रस्तुत पक्ष से पूरी तरह सहमत",
            "इस बात के प्रति उदासीन कि दान गुप्त रखे जाएँ या खुले किए जाएँ"],
   ans=0, pos=0)

# ------------------------------------------------------------------ P05 crowds at heritage sites (3)
p = passage("p05",
  "A medieval fort that once saw a few hundred visitors a year may now receive that many in an hour. The money they bring is welcome, but the monument pays a price: carved stone is worn by hands and feet, walls are scratched with names, "
  "and the humidity of thousands of breaths speeds the decay of old paint. Restricting the numbers is unpopular with the local traders whose livelihoods depend on visitors. Some sites have found a middle path: timed tickets that spread "
  "visitors through the day, a limit on the numbers in the most fragile rooms, and higher prices for those who come at the busiest hours. These measures cost visitors a little, and they cost the monument nothing.",
  "कोई मध्यकालीन क़िला, जहाँ कभी साल भर में कुछ सौ पर्यटक आते थे, अब उतने एक घंटे में पा सकता है। उनका लाया धन स्वागत योग्य है, पर स्मारक को क़ीमत चुकानी पड़ती है: उकेरा हुआ पत्थर हाथों और पैरों से घिसता है, दीवारों पर नाम खरोंचे जाते हैं, "
  "और हज़ारों साँसों की नमी पुराने रंग के क्षय को तेज़ करती है। संख्या सीमित करना उन स्थानीय व्यापारियों में अलोकप्रिय है जिनकी आजीविका पर्यटकों पर निर्भर है। कुछ स्थलों ने बीच का रास्ता खोजा है: समयबद्ध टिकट जो पर्यटकों को "
  "दिन भर में फैलाते हैं, सबसे नाज़ुक कक्षों में संख्या की सीमा, और सबसे व्यस्त घंटों में आने वालों के लिए ऊँचे दाम। इन उपायों से पर्यटकों को थोड़ा ख़र्च उठाना पड़ता है, और स्मारक को कुछ नहीं।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage describes the damage that crowds do to a monument and the middle path of timed tickets, limits in fragile rooms and higher prices at peak hours, which protects the monument without shutting visitors out. "
   "It does not ask for sites to be closed; it does not say that traders gain more than the monuments lose; and humidity is one of three kinds of damage it names, not the main cause.",
   "परिच्छेद भीड़ से स्मारक को होने वाली हानि और समयबद्ध टिकटों, नाज़ुक कक्षों में सीमा और व्यस्त घंटों में ऊँचे दामों के बीच के रास्ते का वर्णन करता है, जो पर्यटकों को बाहर किए बिना स्मारक की रक्षा करता है। "
   "वह स्थलों को बंद करने की माँग नहीं करता; वह यह नहीं कहता कि व्यापारियों का लाभ स्मारकों की हानि से अधिक है; और नमी उन तीन प्रकार की हानियों में से एक है जिनका वह नाम लेता है, मुख्य कारण नहीं।",
   "crux",
   opts=["Heritage sites should be closed to visitors until their monuments have been repaired.",
         "Limits and timed entry can protect monuments from damage without closing them.",
         "Local traders gain more from the visitors than the monuments lose through them.",
         "The damp breath of visitors is the main cause of the decay of old monuments."],
   opts_hi=["विरासत स्थलों को पर्यटकों के लिए तब तक बंद रखना चाहिए जब तक उनके स्मारकों की मरम्मत न हो जाए।",
            "सीमाएँ और समयबद्ध प्रवेश पर्यटकों को बाहर किए बिना स्मारकों को क्षति से बचा सकते हैं।",
            "स्थानीय व्यापारियों को पर्यटकों से जितना लाभ होता है वह स्मारकों की उनसे होने वाली हानि से अधिक है।",
            "पर्यटकों की साँसों की नमी पुराने स्मारकों के क्षय का मुख्य कारण है।"],
   ans=1, pos=1)
RQ(p, "Specific Detail", "medium", "mcq", NOTCORRECT, NOTCORRECT_HI,
   "The passage says that higher prices are charged only 'for those who come at the busiest hours', while timed tickets work by spreading visitors through the day, so saying that they charge every visitor a higher price is the statement it does not support. "
   "It does say that carved stone is worn by hands and feet, that limits on numbers are unpopular with local traders, and that the humidity of breaths speeds the decay of old paint.",
   "परिच्छेद कहता है कि ऊँचे दाम केवल 'सबसे व्यस्त घंटों में आने वालों' से लिए जाते हैं, जबकि समयबद्ध टिकट पर्यटकों को दिन भर में फैलाकर काम करते हैं, इसलिए यह कहना कि वे हर पर्यटक से ऊँचा दाम लेते हैं वह कथन है जिसका वह समर्थन नहीं करता। "
   "वह यह अवश्य कहता है कि उकेरा हुआ पत्थर हाथों और पैरों से घिसता है, कि संख्या पर सीमाएँ स्थानीय व्यापारियों में अलोकप्रिय हैं, और कि साँसों की नमी पुराने रंग के क्षय को तेज़ करती है।",
   "not-correct",
   opts=["Carved stone is worn down by the hands and feet of visitors.",
         "Limits on the number of visitors are unpopular with local traders.",
         "Timed tickets work by charging every visitor a higher price.",
         "The humidity of visitors' breath can hasten the decay of old paint."],
   opts_hi=["उकेरा हुआ पत्थर पर्यटकों के हाथों और पैरों से घिसता है।",
            "पर्यटकों की संख्या पर सीमाएँ स्थानीय व्यापारियों में अलोकप्रिय हैं।",
            "समयबद्ध टिकट हर पर्यटक से ऊँचा दाम लेकर काम करते हैं।",
            "पर्यटकों की साँसों की नमी पुराने रंग के क्षय को तेज़ कर सकती है।"],
   ans=2, pos=2)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Neither is valid. 1 contradicts the passage, which says that carved stone is worn by hands and feet. 2 puts the damage to old paint down to the touch of hands, whereas the passage gives the humidity of thousands of breaths as the cause.",
   "कोई भी वैध नहीं है। 1 परिच्छेद का खंडन करता है, जो कहता है कि उकेरा हुआ पत्थर हाथों और पैरों से घिसता है। 2 पुराने रंग की हानि का कारण हाथों का स्पर्श बताता है, जबकि परिच्छेद उसका कारण हज़ारों साँसों की नमी बताता है।",
   "conclusions",
   st=["Stone monuments are not harmed by large numbers of visitors.",
       "Old paint on a monument is damaged mainly by the touch of visitors' hands."],
   st_hi=["पत्थर के स्मारकों को बड़ी संख्या में आने वाले पर्यटकों से कोई हानि नहीं होती।",
          "किसी स्मारक का पुराना रंग मुख्यतः पर्यटकों के हाथों के स्पर्श से ख़राब होता है।"],
   key=3)

# ------------------------------------------------------------------ P06 the stigma of vocational courses (3)
p = passage("p06",
  "Many young people in India would rather take an undistinguished degree than a skilled course. The reason is not that skilled work pays badly: a good electrician or technician can earn more than a graduate clerk. It is that vocational "
  "courses carry a stigma, as the route chosen by those who could not get into college. Families also doubt that the courses are worth it, with good reason, since many are outdated and teach on machines that no workplace uses. "
  "Employers who take on trainees, pay them while they learn and promise a certificate that others will accept make the course a first step into a career and not a last resort. Where this has been done, the stigma has begun to fade.",
  "भारत के कई युवा किसी कौशल पाठ्यक्रम के बजाय कोई साधारण डिग्री लेना पसंद करेंगे। कारण यह नहीं कि कुशल काम में पैसा कम मिलता है: एक अच्छा बिजली मिस्त्री या तकनीशियन किसी स्नातक क्लर्क से अधिक कमा सकता है। कारण यह है कि व्यावसायिक "
  "पाठ्यक्रमों पर कलंक लगा है, कि वे उन लोगों का चुना रास्ता हैं जिन्हें कॉलेज में प्रवेश नहीं मिला। परिवार भी संदेह करते हैं कि पाठ्यक्रम इस योग्य हैं, और ठोस कारण से, क्योंकि कई पुराने पड़ चुके हैं और ऐसी मशीनों पर सिखाते हैं जिन्हें कोई कार्यस्थल उपयोग नहीं करता। "
  "जो नियोक्ता प्रशिक्षुओं को लेते हैं, उन्हें सीखते समय वेतन देते हैं और ऐसे प्रमाणपत्र का वादा करते हैं जिसे दूसरे स्वीकार करें, वे पाठ्यक्रम को अंतिम सहारा नहीं बल्कि करियर की पहली सीढ़ी बना देते हैं। जहाँ ऐसा किया गया है, वहाँ कलंक फीका पड़ने लगा है।")
RQ(p, "Best Summary", "medium", "mcq", MSG, MSG_HI,
   "The passage traces young people's avoidance of skilled courses to stigma and to doubts about the courses' quality, and says that employers who train, pay and certify can turn them into a first step in a career. "
   "It denies that skilled work pays badly; it asks nothing of degree courses; and it speaks of trainees paid while they learn, not of permanent jobs for all of them.",
   "परिच्छेद युवाओं के कौशल पाठ्यक्रमों से बचने को कलंक और पाठ्यक्रमों की गुणवत्ता पर संदेह से जोड़ता है, और कहता है कि जो नियोक्ता प्रशिक्षण देते, वेतन देते और प्रमाणपत्र देते हैं वे उन्हें करियर की पहली सीढ़ी बना सकते हैं। "
   "वह इससे इनकार करता है कि कुशल काम में पैसा कम मिलता है; वह डिग्री पाठ्यक्रमों से कुछ नहीं माँगता; और वह सीखते समय वेतन पाने वाले प्रशिक्षुओं की बात करता है, सबको स्थायी नौकरी की नहीं।",
   "message",
   opts=["Young people avoid skilled courses because skilled workers are generally paid less than graduates.",
         "Degree courses should be closed to young people who could do skilled work instead.",
         "Employers should be made to hire every vocational trainee as a permanent employee.",
         "Vocational courses will draw students when employers back them and they lead to careers."],
   opts_hi=["युवा कौशल पाठ्यक्रमों से इसलिए बचते हैं कि कुशल कामगार स्नातकों से कम कमाते हैं।",
            "जो युवा कौशल का काम कर सकते हैं उनके लिए डिग्री पाठ्यक्रम बंद कर देने चाहिए।",
            "नियोक्ताओं को हर व्यावसायिक प्रशिक्षु को स्थायी कर्मचारी के रूप में रखने के लिए बाध्य करना चाहिए।",
            "व्यावसायिक पाठ्यक्रम तब छात्रों को खींचेंगे जब नियोक्ता उनका साथ दें और वे करियर तक पहुँचाएँ।"],
   ans=3, pos=3)
RQ(p, "Inference", "hard", "sc", INFER, INFER_HI,
   "1 and 3 follow. A good electrician or technician 'can earn more than a graduate clerk', so a skilled worker can earn more than some graduates (1); and a certificate 'that others will accept' is part of what makes a course 'a first step into a career', "
   "so such a certificate can raise its standing (3). 2 contradicts the passage, which says that many courses are outdated.",
   "1 और 3 निकलते हैं। एक अच्छा बिजली मिस्त्री या तकनीशियन 'किसी स्नातक क्लर्क से अधिक कमा सकता है', इसलिए कुशल कामगार कुछ स्नातकों से अधिक कमा सकता है (1); और 'दूसरों द्वारा स्वीकार किया जाने वाला' प्रमाणपत्र उसका भाग है जो पाठ्यक्रम को 'करियर की पहली सीढ़ी' बनाता है, "
   "इसलिए ऐसा प्रमाणपत्र पाठ्यक्रम की प्रतिष्ठा बढ़ा सकता है (3)। 2 परिच्छेद का खंडन करता है, जो कहता है कि कई पाठ्यक्रम पुराने पड़ चुके हैं।",
   "inferences",
   st=["A skilled worker can earn more than some graduates.",
       "Most vocational courses in India are of a high standard.",
       "A certificate that employers accept can raise the standing of a course."],
   st_hi=["कोई कुशल कामगार कुछ स्नातकों से अधिक कमा सकता है।",
          "भारत के अधिकांश व्यावसायिक पाठ्यक्रम उच्च स्तर के हैं।",
          "नियोक्ताओं द्वारा स्वीकार किया जाने वाला प्रमाणपत्र किसी पाठ्यक्रम की प्रतिष्ठा बढ़ा सकता है।"],
   opts=["1 and 3 only", "2 only", "1 and 2 only", "2 and 3 only"], key=0)
RQ(p, "Assumption", "hard", "s2", ASSUME, ASSUME_HI,
   "Both are assumed. The claim that employers make a course 'a first step into a career' by training, paying and certifying takes for granted that families will prefer a course that leads to a job (1), "
   "and the closing remark that the stigma has begun to fade where this has been done takes for granted that it can fade when a course is seen to lead to a career (2).",
   "दोनों पूर्वधारणाएँ हैं। यह दावा कि नियोक्ता प्रशिक्षण, वेतन और प्रमाणपत्र देकर पाठ्यक्रम को 'करियर की पहली सीढ़ी' बनाते हैं, मानकर चलता है कि परिवार नौकरी तक ले जाने वाला पाठ्यक्रम पसंद करेंगे (1), "
   "और अंतिम टिप्पणी कि जहाँ ऐसा किया गया वहाँ कलंक फीका पड़ने लगा है, मानकर चलती है कि जब पाठ्यक्रम को करियर तक ले जाता देखा जाए तो कलंक फीका पड़ सकता है (2)।",
   "assumptions",
   st=["A family is more likely to choose a course that leads to a job than one that does not.",
       "The stigma attached to a course can fade when the course is seen to lead to a career."],
   st_hi=["कोई परिवार नौकरी तक ले जाने वाले पाठ्यक्रम को, ऐसा न करने वाले पाठ्यक्रम की तुलना में, चुनने की अधिक संभावना रखता है।",
          "किसी पाठ्यक्रम पर लगा कलंक तब फीका पड़ सकता है जब पाठ्यक्रम को करियर तक ले जाता देखा जाए।"],
   key=2)

# ------------------------------------------------------------------ P07 the closing of local newspapers (3)
p = passage("p07",
  "When a town's newspaper closes, the news does not move elsewhere; it simply stops. Nobody reports on the council's budget, the school's failing results or the contractor's delayed road, and studies from several countries suggest that "
  "where local reporting fades, officials spend more, borrow more and are re-elected more easily. National papers and social media cover national politics, not the drains of a particular ward. Local news is hard to pay for: advertisers have "
  "moved online and readers are used to getting news free. Some places support it through public funds, through donations, or through a small tax on the online platforms that carry local stories. Whichever route is chosen, "
  "the choice is between paying for local news and paying later for the mistakes that it would have caught.",
  "जब किसी कस्बे का अख़बार बंद होता है, तो ख़बर कहीं और नहीं चली जाती; वह बस रुक जाती है। परिषद के बजट, विद्यालय के ख़राब परिणामों या ठेकेदार की अटकी सड़क के बारे में कोई नहीं लिखता, और कई देशों के अध्ययन संकेत देते हैं कि "
  "जहाँ स्थानीय रिपोर्टिंग मद्धम पड़ती है, वहाँ अधिकारी अधिक ख़र्च करते हैं, अधिक उधार लेते हैं और अधिक आसानी से दोबारा चुन लिए जाते हैं। राष्ट्रीय अख़बार और सोशल मीडिया राष्ट्रीय राजनीति को कवर करते हैं, किसी विशेष वार्ड की नालियों को नहीं। स्थानीय समाचार का ख़र्च जुटाना कठिन है: विज्ञापनदाता "
  "ऑनलाइन चले गए हैं और पाठकों को ख़बर मुफ़्त पाने की आदत है। कुछ स्थान उसे सार्वजनिक धन, दान, या स्थानीय कहानियाँ चलाने वाले ऑनलाइन मंचों पर एक छोटे कर के माध्यम से सहारा देते हैं। जो भी रास्ता चुना जाए, "
  "चुनाव स्थानीय समाचार का ख़र्च उठाने और बाद में उन ग़लतियों की क़ीमत चुकाने के बीच है जिन्हें वह पकड़ लेता।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage says that local news keeps officials watched, that it is hard to pay for, and that the choice is between paying for it and paying later for the mistakes it would have caught. "
   "It says national papers and social media cover national politics and not the drains of a ward, so the claim that they report local affairs just as well contradicts it; it does not ask readers to pay for news they get free; "
   "and it says that spending and borrowing rise where reporting fades, not that the papers caused them.",
   "परिच्छेद कहता है कि स्थानीय समाचार अधिकारियों पर नज़र बनाए रखता है, कि उसका ख़र्च जुटाना कठिन है, और कि चुनाव उसका ख़र्च उठाने और बाद में उन ग़लतियों की क़ीमत चुकाने के बीच है जिन्हें वह पकड़ लेता। "
   "वह कहता है कि राष्ट्रीय अख़बार और सोशल मीडिया राष्ट्रीय राजनीति को कवर करते हैं, किसी वार्ड की नालियों को नहीं, इसलिए यह दावा कि वे स्थानीय मामलों की रिपोर्टिंग उतनी ही अच्छी तरह करते हैं, उसका खंडन करता है; वह पाठकों से मुफ़्त मिलने वाली ख़बर का भुगतान करने को नहीं कहता; "
   "और वह कहता है कि जहाँ रिपोर्टिंग मद्धम पड़ती है वहाँ ख़र्च और उधार बढ़ते हैं, यह नहीं कि अख़बारों ने उन्हें पैदा किया।",
   "crux",
   opts=["Local news holds officials to account, and paying for it is cheaper than doing without it.",
         "National newspapers and social media can report local affairs as well as local papers can.",
         "Readers should be made to pay for the news that they now receive free online.",
         "Officials spend more and borrow more because local papers have exaggerated their failings."],
   opts_hi=["स्थानीय समाचार अधिकारियों को जवाबदेह बनाता है, और उसका ख़र्च उठाना उसके बिना रहने से सस्ता है।",
            "राष्ट्रीय अख़बार और सोशल मीडिया स्थानीय मामलों की रिपोर्टिंग उतनी ही अच्छी तरह कर सकते हैं जितनी स्थानीय अख़बार।",
            "पाठकों को उस ख़बर का भुगतान करने के लिए बाध्य किया जाना चाहिए जो उन्हें अब ऑनलाइन मुफ़्त मिलती है।",
            "अधिकारी इसलिए अधिक ख़र्च और उधार करते हैं कि स्थानीय अख़बारों ने उनकी विफलताएँ बढ़ा-चढ़ाकर बताईं।"],
   ans=0, pos=0)
RQ(p, "Specific Detail", "easy", "mcq",
   "According to the passage, why is local news hard to pay for?",
   "परिच्छेद के अनुसार, स्थानीय समाचार का ख़र्च जुटाना कठिन क्यों है?",
   "The passage says 'advertisers have moved online and readers are used to getting news free'. It does not say that local reporters are paid more than national ones, that officials stop papers from reporting, "
   "or that readers have lost interest in their own towns.",
   "परिच्छेद कहता है कि 'विज्ञापनदाता ऑनलाइन चले गए हैं और पाठकों को ख़बर मुफ़्त पाने की आदत है'। वह यह नहीं कहता कि स्थानीय संवाददाताओं को राष्ट्रीय संवाददाताओं से अधिक वेतन मिलता है, कि अधिकारी अख़बारों को रिपोर्ट करने से रोकते हैं, "
   "या कि पाठकों की अपने कस्बों के मामलों में रुचि समाप्त हो गई है।",
   "detail",
   opts=["Local reporters demand higher pay than national reporters do.",
         "Officials stop local papers from reporting on the council's budget.",
         "Readers have lost interest in the affairs of their own towns.",
         "Advertisers have moved online and readers expect news to be free."],
   opts_hi=["स्थानीय संवाददाता राष्ट्रीय संवाददाताओं से अधिक वेतन माँगते हैं।",
            "अधिकारी स्थानीय अख़बारों को परिषद के बजट पर रिपोर्ट करने से रोकते हैं।",
            "पाठकों की अपने कस्बों के मामलों में रुचि समाप्त हो गई है।",
            "विज्ञापनदाता ऑनलाइन चले गए और पाठक मुफ़्त ख़बर की अपेक्षा रखते हैं।"],
   ans=3, pos=3)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Only 1 is valid: where local reporting fades, officials spend more, borrow more and are re-elected more easily, so a town whose paper has closed may find its officials less closely watched. "
   "2 reverses the passage, which says that national papers and social media cover national politics, not the drains of a particular ward.",
   "केवल 1 वैध है: जहाँ स्थानीय रिपोर्टिंग मद्धम पड़ती है, वहाँ अधिकारी अधिक ख़र्च करते, अधिक उधार लेते और अधिक आसानी से दोबारा चुने जाते हैं, इसलिए जिस कस्बे का अख़बार बंद हो गया हो वहाँ अधिकारियों पर कम नज़र रखी जा सकती है। "
   "2 परिच्छेद को उलट देता है, जो कहता है कि राष्ट्रीय अख़बार और सोशल मीडिया राष्ट्रीय राजनीति को कवर करते हैं, किसी विशेष वार्ड की नालियों को नहीं।",
   "conclusions",
   st=["A town whose newspaper has closed may find its officials less closely watched.",
       "Social media covers the drains of a ward better than a local newspaper does."],
   st_hi=["जिस कस्बे का अख़बार बंद हो गया हो, वहाँ उसके अधिकारियों पर कम नज़र रखी जा सकती है।",
          "सोशल मीडिया किसी वार्ड की नालियों को स्थानीय अख़बार से बेहतर कवर करता है।"],
   key=0)

# ------------------------------------------------------------------ P08 sorting waste at home (2)
p = passage("p08",
  "A city can collect all its household waste in one cart, or it can ask people to sort it at home into wet waste, dry waste and hazardous items. Mixed waste is the easy habit but a costly one: food scraps soak the paper and plastic, "
  "making them hard to sell for recycling, and what cannot be sold goes to a dump, where it rots and burns. Separated at the source, wet waste can become compost, dry waste finds buyers, and the dump receives far less. Sorting at home asks "
  "something of every household, which is why the cities that have succeeded have paired it with daily collection in separate bins, and with fines that are used rarely and explained first.",
  "कोई शहर अपने घरों का पूरा कचरा एक ही गाड़ी में इकट्ठा कर सकता है, या वह लोगों से कह सकता है कि वे उसे घर पर ही गीले कचरे, सूखे कचरे और ख़तरनाक वस्तुओं में छाँट दें। मिला हुआ कचरा आसान आदत है पर महँगी: खाने के टुकड़े काग़ज़ और प्लास्टिक को भिगो देते हैं, "
  "जिससे उन्हें पुनर्चक्रण के लिए बेचना कठिन हो जाता है, और जो बिक नहीं पाता वह कचराघर में जाता है, जहाँ वह सड़ता और जलता है। स्रोत पर अलग किए जाने पर गीला कचरा खाद बन सकता है, सूखे कचरे को ख़रीदार मिलते हैं, और कचराघर में बहुत कम पहुँचता है। घर पर छाँटना "
  "हर परिवार से कुछ माँगता है, इसीलिए जिन शहरों को सफलता मिली है उन्होंने उसे अलग-अलग डिब्बों में दैनिक संग्रह और ऐसे जुर्मानों के साथ जोड़ा है जो कम ही लगाए जाते हैं और जिन्हें पहले समझाया जाता है।")
RQ(p, "Best Summary", "medium", "mcq", MSG, MSG_HI,
   "The passage argues that sorting waste at home cuts what reaches the dump, and that it works where the city collects the sorted waste separately every day and uses fines sparingly. "
   "It does not ask for heavy fines; it says mixed waste is hard to sell, not that it can never be recycled; and sorting at the dump is the costly habit it argues against.",
   "परिच्छेद तर्क देता है कि घर पर कचरा छाँटने से कचराघर तक पहुँचने वाला कचरा घटता है, और कि यह वहाँ काम करता है जहाँ शहर छाँटे हुए कचरे को रोज़ अलग-अलग इकट्ठा करता है और जुर्माने कम लगाता है। "
   "वह भारी जुर्माने नहीं माँगता; वह कहता है कि मिला हुआ कचरा बेचना कठिन है, यह नहीं कि उसका पुनर्चक्रण कभी हो ही नहीं सकता; और कचराघर पर छँटाई वही महँगी आदत है जिसके विरुद्ध वह तर्क देता है।",
   "message",
   opts=["Households should be fined heavily whenever they mix wet waste with dry waste.",
         "Waste that has once been mixed with food scraps can never be recycled.",
         "Sorting waste at home cuts what reaches the dump, if the city collects it separately every day.",
         "A city can cut its waste by collecting everything in one cart and sorting it later at the dump."],
   opts_hi=["जब भी कोई परिवार गीले और सूखे कचरे को मिलाए, उस पर भारी जुर्माना लगना चाहिए।",
            "जो कचरा एक बार खाने के टुकड़ों के साथ मिल गया, उसका पुनर्चक्रण कभी नहीं हो सकता।",
            "घर पर कचरा छाँटने से कचराघर पहुँचने वाला कचरा घटता है, यदि शहर उसे रोज़ अलग इकट्ठा करे।",
            "कोई शहर सब कुछ एक गाड़ी में इकट्ठा करके उसे बाद में कचराघर पर छाँटकर अपना कचरा घटा सकता है।"],
   ans=2, pos=2)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Only 2 is valid: food scraps soak the paper and plastic, 'making them hard to sell for recycling'. 1 goes beyond the passage, which says that sorted dry waste 'finds buyers' and wet waste can become compost, "
   "not that every kind of waste that goes to a dump could be sold.",
   "केवल 2 वैध है: खाने के टुकड़े काग़ज़ और प्लास्टिक को भिगो देते हैं, 'जिससे उन्हें पुनर्चक्रण के लिए बेचना कठिन हो जाता है'। 1 परिच्छेद से आगे जाता है, जो कहता है कि छँटे हुए सूखे कचरे को ख़रीदार 'मिलते' हैं और गीला कचरा खाद बन सकता है, "
   "यह नहीं कि कचराघर में जाने वाला हर प्रकार का कचरा बेचा जा सकता है।",
   "conclusions",
   st=["All the waste that goes to a dump could be sold for recycling if it were sorted.",
       "Food scraps can make dry waste harder to sell for recycling."],
   st_hi=["कचराघर में जाने वाला सारा कचरा, यदि वह छँटा हुआ होता, पुनर्चक्रण के लिए बेचा जा सकता था।",
          "खाने के टुकड़े सूखे कचरे को पुनर्चक्रण के लिए बेचना और कठिन बना सकते हैं।"],
   key=1)

# ------------------------------------------------------------------ P09 wetlands and urban floods (3)
p = passage("p09",
  "Cities that fill their ponds, lakes and marshes with rubble to make land for buildings often find, a few monsoons later, that their streets flood in places that were never flooded before. Wetlands act like sponges: "
  "they soak up the rain that falls on a city and release it slowly, and when they are built over, the water has nowhere to go but the roads. Drains alone cannot take their place, for a drain carries water away at the speed of the storm "
  "and so pushes the flood downstream. Cities that have cleared old channels, protected a few wetlands and left open land for the water to spread have lowered the flood level without spending much. "
  "The land that is given up is a small price for the buildings it saves.",
  "जो शहर इमारतों के लिए ज़मीन बनाने हेतु अपने तालाबों, झीलों और दलदलों को मलबे से भर देते हैं, वे प्रायः कुछ मानसून बाद पाते हैं कि उनकी सड़कें ऐसी जगहों पर डूबने लगी हैं जहाँ पहले कभी नहीं डूबी थीं। आर्द्रभूमियाँ स्पंज की तरह काम करती हैं: "
  "वे शहर पर गिरने वाली वर्षा को सोख लेती हैं और उसे धीरे-धीरे छोड़ती हैं, और जब उन पर निर्माण हो जाता है, तो पानी के पास सड़कों के सिवा कहीं जाने को नहीं बचता। नालियाँ अकेले उनकी जगह नहीं ले सकतीं, क्योंकि नाली पानी को तूफ़ान की गति से बहा ले जाती है "
  "और इस तरह बाढ़ को निचले क्षेत्रों की ओर धकेल देती है। जिन शहरों ने पुराने मार्ग साफ़ किए, कुछ आर्द्रभूमियों को बचाया और पानी के फैलने के लिए खुली ज़मीन छोड़ी, उन्होंने बहुत ख़र्च किए बिना बाढ़ का स्तर घटाया है। "
  "जो ज़मीन छोड़ी जाती है वह उन इमारतों को बचाने की छोटी क़ीमत है जिन्हें वह बचाती है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage says that wetlands soak up a city's rain, that drains cannot replace them, and that cities which protect some wetlands and leave open land lower the flood level cheaply. "
   "It does not say that drains that are too small are the main cause -- it says drains push the flood downstream; it speaks of protecting a few wetlands, not of banning all building near water; "
   "and it presents filling wetlands as the cause of new floods, not as a cheap gain.",
   "परिच्छेद कहता है कि आर्द्रभूमियाँ शहर की वर्षा को सोख लेती हैं, कि नालियाँ उनकी जगह नहीं ले सकतीं, और कि जो शहर कुछ आर्द्रभूमियाँ बचाते और खुली ज़मीन छोड़ते हैं वे बाढ़ का स्तर सस्ते में घटा लेते हैं। "
   "वह यह नहीं कहता कि बहुत छोटी नालियाँ मुख्य कारण हैं -- वह कहता है कि नालियाँ बाढ़ को निचले क्षेत्रों की ओर धकेलती हैं; वह कुछ आर्द्रभूमियाँ बचाने की बात करता है, पानी के पास हर निर्माण पर रोक की नहीं; "
   "और वह आर्द्रभूमियों को भरने को नई बाढ़ों का कारण बताता है, सस्ता लाभ नहीं।",
   "crux",
   opts=["Wetlands protect a city from floods, so building over them invites flooding.",
         "Floods in cities are caused mainly by drains that are too small.",
         "Cities should build no new buildings near any pond, lake or marsh.",
         "Filling in wetlands is the cheapest way for a city to find land for buildings."],
   opts_hi=["आर्द्रभूमियाँ शहर को बाढ़ से बचाती हैं, इसलिए उन पर निर्माण बाढ़ बुलाता है।",
            "शहरों में बाढ़ मुख्यतः बहुत छोटी नालियों के कारण आती है।",
            "शहरों को किसी भी तालाब, झील या दलदल के पास कोई नई इमारत नहीं बनानी चाहिए।",
            "आर्द्रभूमियों को भरना शहर के लिए इमारतों हेतु ज़मीन पाने का सबसे सस्ता तरीका है।"],
   ans=0, pos=0)
RQ(p, "Assumption", "hard", "sc", ASSUME, ASSUME_HI,
   "1 and 3 are assumed. Leaving open land for water takes for granted that a city can afford to give up some land without halting its growth (1), and the argument that wetlands act like sponges takes for granted that a wetland "
   "which has not been built over keeps its power to soak up rain (3). 2 is not assumed and goes beyond the passage, which says only that building over wetlands brings floods in places never flooded before.",
   "1 और 3 पूर्वधारणाएँ हैं। पानी के लिए खुली ज़मीन छोड़ना मानकर चलता है कि शहर अपनी वृद्धि रोके बिना कुछ ज़मीन छोड़ सकता है (1), और यह तर्क कि आर्द्रभूमियाँ स्पंज की तरह काम करती हैं, मानकर चलता है कि जिस आर्द्रभूमि पर निर्माण नहीं हुआ "
   "वह वर्षा को सोखने की अपनी क्षमता बनाए रखती है (3)। 2 पूर्वधारणा नहीं है और परिच्छेद से आगे जाता है, जो केवल इतना कहता है कि आर्द्रभूमियों पर निर्माण से उन जगहों पर बाढ़ आती है जहाँ पहले कभी नहीं आई थी।",
   "assumptions",
   st=["A city can afford to leave some land open without halting its growth.",
       "Every flood in a city is caused by the loss of a wetland.",
       "A wetland that has not been built over keeps its power to soak up rain."],
   st_hi=["कोई शहर अपनी वृद्धि रोके बिना कुछ ज़मीन खुली छोड़ सकता है।",
          "शहर में आने वाली हर बाढ़ किसी आर्द्रभूमि के खो जाने से आती है।",
          "जिस आर्द्रभूमि पर निर्माण नहीं हुआ है वह वर्षा को सोखने की अपनी क्षमता बनाए रखती है।"],
   opts=["1 only", "2 and 3 only", "1, 2 and 3", "1 and 3 only"], key=3)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Both are valid. A drain 'pushes the flood downstream', so improving drains alone may only move a flood from one place to another (1); and cities that fill wetlands find their streets flooding 'in places that were never flooded before', "
   "so the risk of flooding can rise when wetlands are filled in (2).",
   "दोनों वैध हैं। नाली 'बाढ़ को निचले क्षेत्रों की ओर धकेल देती है', इसलिए केवल नालियाँ सुधारने से बाढ़ बस एक जगह से दूसरी जगह जा सकती है (1); और जो शहर आर्द्रभूमियाँ भरते हैं उनकी सड़कें 'ऐसी जगहों पर डूबती हैं जहाँ पहले कभी नहीं डूबी थीं', "
   "इसलिए आर्द्रभूमियाँ भरने पर बाढ़ का जोखिम बढ़ सकता है (2)।",
   "conclusions",
   st=["Improving the drains alone may only move a flood from one place to another.",
       "A city's risk of flooding can rise when its wetlands are filled in."],
   st_hi=["केवल नालियाँ सुधारने से बाढ़ बस एक जगह से दूसरी जगह जा सकती है।",
          "किसी शहर की आर्द्रभूमियाँ भरने पर उसके बाढ़ का जोखिम बढ़ सकता है।"],
   key=2)

# ------------------------------------------------------------------ P10 street vendors (3)
p = passage("p10",
  "Street vendors sell cheap food, vegetables and repairs to millions of city dwellers, and the cities that treat them as a nuisance lose a service that is hard to replace. Vendors are removed because they crowd the pavement, "
  "but removal is often followed by their return a week later, since they have no other livelihood and their customers have not gone anywhere. Cities that give vendors licences and a place to trade -- marked spots, fixed hours, "
  "a rule against blocking the way -- find that the pavement is kept clearer than it was under bans, and that the vendors, who now have something to lose, keep the rules. The aim is not to let vendors do as they please, "
  "but to plan for them as part of the city, as one plans for buses and drains.",
  "रेहड़ी-पटरी वाले लाखों शहरवासियों को सस्ता भोजन, सब्ज़ियाँ और मरम्मत की सेवाएँ देते हैं, और जो शहर उन्हें उपद्रव मानते हैं वे एक ऐसी सेवा खो देते हैं जिसकी जगह भरना कठिन है। विक्रेताओं को इसलिए हटाया जाता है कि वे पटरी पर भीड़ लगाते हैं, "
  "पर हटाने के बाद प्रायः एक सप्ताह में वे लौट आते हैं, क्योंकि उनके पास और कोई आजीविका नहीं और उनके ग्राहक कहीं गए नहीं। जो शहर विक्रेताओं को लाइसेंस और व्यापार की जगह देते हैं -- निशान लगे स्थान, तय घंटे, "
  "रास्ता न रोकने का नियम -- वे पाते हैं कि प्रतिबंधों के दौर से पटरी अधिक साफ़ रहती है, और कि विक्रेता, जिनके पास अब खोने को कुछ है, नियमों का पालन करते हैं। लक्ष्य विक्रेताओं को मनमानी करने देना नहीं, "
  "बल्कि उन्हें शहर के भाग के रूप में नियोजित करना है, जैसे बसों और नालियों की योजना बनाई जाती है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage argues that cities should plan for vendors -- licences, marked spots, fixed hours, a rule against blocking the way -- instead of trying to remove them, since removal fails and planning keeps the pavement clearer. "
   "It does not ask for a ban, which it says fails; it does not ask for vendors to trade wherever they like, since 'the aim is not to let vendors do as they please'; and licensed vendors keep rules, not none.",
   "परिच्छेद तर्क देता है कि शहरों को विक्रेताओं को हटाने की कोशिश के बजाय उनके लिए योजना बनानी चाहिए -- लाइसेंस, निशान लगे स्थान, तय घंटे, रास्ता न रोकने का नियम -- क्योंकि हटाना विफल रहता है और योजना पटरी को अधिक साफ़ रखती है। "
   "वह प्रतिबंध नहीं माँगता, जिसके बारे में वह कहता है कि वह विफल रहता है; वह विक्रेताओं को जहाँ चाहें वहाँ व्यापार करने की छूट नहीं माँगता, क्योंकि 'लक्ष्य विक्रेताओं को मनमानी करने देना नहीं है'; और लाइसेंस वाले विक्रेता नियम मानते हैं, बिना नियमों के नहीं चलते।",
   "crux",
   opts=["Street vendors should be banned from pavements because they block the way.",
         "Cities should plan for vendors with licences and fixed places, not try to remove them.",
         "Vendors should be free to trade wherever they like, so long as customers want them there.",
         "Vendors who hold licences need not follow any rules about where they sell."],
   opts_hi=["रेहड़ी-पटरी वालों को पटरियों से प्रतिबंधित कर देना चाहिए क्योंकि वे रास्ता रोकते हैं।",
            "शहरों को विक्रेताओं को हटाने के बजाय लाइसेंस और तय स्थानों के साथ उनके लिए योजना बनानी चाहिए।",
            "विक्रेताओं को जहाँ चाहें वहाँ व्यापार करने की छूट होनी चाहिए, जब तक ग्राहक उन्हें वहाँ चाहते हों।",
            "लाइसेंस रखने वाले विक्रेताओं को इस बारे में कोई नियम मानने की ज़रूरत नहीं कि वे कहाँ बेचें।"],
   ans=1, pos=1)
RQ(p, "Specific Detail", "easy", "mcq",
   "According to the passage, why do vendors who are removed from a pavement often return within a week?",
   "परिच्छेद के अनुसार, किसी पटरी से हटाए गए विक्रेता प्रायः एक सप्ताह के भीतर क्यों लौट आते हैं?",
   "The passage says they return 'since they have no other livelihood and their customers have not gone anywhere'. It does not say that the police are unable to remove them, that the city gives them licences as soon as they return, "
   "or that their customers force the city to withdraw the ban.",
   "परिच्छेद कहता है कि वे लौट आते हैं 'क्योंकि उनके पास और कोई आजीविका नहीं और उनके ग्राहक कहीं गए नहीं'। वह यह नहीं कहता कि पुलिस उन्हें हटा नहीं पाती, कि शहर उनके लौटते ही उन्हें लाइसेंस दे देता है, "
   "या कि उनके ग्राहक शहर को प्रतिबंध वापस लेने के लिए बाध्य करते हैं।",
   "detail",
   opts=["The police find it impossible to remove them from the pavement at all.",
         "The city gives them licences as soon as they have returned to the pavement.",
         "Their customers force the city to withdraw the ban within the week.",
         "They have no other livelihood, and their customers are still there."],
   opts_hi=["पुलिस के लिए उन्हें पटरी से बिल्कुल हटा पाना संभव ही नहीं होता।",
            "शहर उनके पटरी पर लौटते ही उन्हें लाइसेंस दे देता है।",
            "उनके ग्राहक एक सप्ताह के भीतर शहर को प्रतिबंध वापस लेने के लिए बाध्य कर देते हैं।",
            "उनके पास और कोई आजीविका नहीं है, और उनके ग्राहक अब भी वहीं हैं।"],
   ans=3, pos=3)
RQ(p, "Assumption", "hard", "s2", ASSUME, ASSUME_HI,
   "Only 2 is assumed. The claim that vendors who 'now have something to lose' keep the rules takes for granted that a vendor with a licensed spot has more to lose by breaking them. "
   "1 is the opposite of the passage, which says that vendors who are removed return a week later because they have no other livelihood.",
   "केवल 2 पूर्वधारणा है। यह दावा कि जिन विक्रेताओं के पास 'अब खोने को कुछ है' वे नियम मानते हैं, मानकर चलता है कि लाइसेंस वाली जगह रखने वाले विक्रेता के पास नियम तोड़ने पर खोने को अधिक है। "
   "1 परिच्छेद के उलट है, जो कहता है कि हटाए गए विक्रेता एक सप्ताह बाद इसलिए लौट आते हैं कि उनके पास और कोई आजीविका नहीं।",
   "assumptions",
   st=["Vendors who are banned from a pavement find other work within a week.",
       "Vendors who hold a licensed spot have more to lose by breaking the rules."],
   st_hi=["जिन विक्रेताओं को किसी पटरी से प्रतिबंधित किया जाता है वे एक सप्ताह के भीतर दूसरा काम खोज लेते हैं।",
          "लाइसेंस वाली जगह रखने वाले विक्रेताओं के पास नियम तोड़ने पर खोने को अधिक होता है।"],
   key=1)
