# -*- coding: utf-8 -*-
"""CSAT Level 2 · Test 5 -- Reading Comprehension: 10 original passages, 28 items (8 x 3, 2 x 2).

Themes, none used in Tests 1-4: the silence around mental illness, old crop varieties and seed banks, electric
buses, lantana in the forests, timely official statistics, the right to repair, overfishing, city noise, giving
to charity well, and streets for people on foot. Item types: main idea 7, inference 8, assumption 5, tone 1,
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

# ------------------------------------------------------------------ P01 the silence around mental illness (3)
p = passage("p01",
  "Depression and anxiety are among the commonest causes of illness in India, yet most people who live with them never see anyone trained to help. Part of the reason is supply: there are few psychiatrists, "
  "and most of them work in cities. But part of it is silence. Families fear that a diagnosis will spoil a marriage or a career, and so a son's withdrawal is put down to laziness and a mother's exhaustion to her temperament. "
  "Programmes that train community health workers to recognise common disorders and to offer simple talking therapies have shown that care need not wait for specialists. Their reach, however, depends on whether people "
  "are willing to say that something is wrong.",
  "अवसाद और दुश्चिंता भारत में बीमारी के सबसे आम कारणों में हैं, फिर भी इनके साथ जीने वाले अधिकांश लोग कभी किसी प्रशिक्षित सहायक से नहीं मिलते। इसका एक कारण उपलब्धता है: मनोचिकित्सक कम हैं, "
  "और उनमें से अधिकांश शहरों में काम करते हैं। पर एक कारण चुप्पी भी है। परिवारों को डर होता है कि निदान से विवाह या करियर बिगड़ जाएगा, और इसलिए बेटे के अलग-थलग रहने को आलस्य और माँ की थकान को उसका स्वभाव मान लिया जाता है। "
  "जो कार्यक्रम सामुदायिक स्वास्थ्य कार्यकर्ताओं को आम विकार पहचानने और सरल बातचीत वाली चिकित्सा देने का प्रशिक्षण देते हैं, उन्होंने दिखाया है कि देखभाल को विशेषज्ञों की प्रतीक्षा करने की ज़रूरत नहीं। पर उनकी पहुँच इस पर निर्भर है कि लोग "
  "यह कहने को तैयार हैं या नहीं कि कुछ ठीक नहीं है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage names two barriers to care -- too few specialists and the silence of families -- shows that trained community workers can supply care, and ends by making their reach depend on people speaking up. "
   "It says care need not wait for more psychiatrists; it reports laziness and temperament as the excuses families give, not as causes; and it proposes community workers alongside specialists, not in place of them everywhere.",
   "परिच्छेद देखभाल की दो बाधाएँ बताता है -- विशेषज्ञों की कमी और परिवारों की चुप्पी -- दिखाता है कि प्रशिक्षित सामुदायिक कार्यकर्ता देखभाल दे सकते हैं, और अंत में उनकी पहुँच को लोगों के बोलने पर निर्भर बताता है। "
   "वह कहता है कि देखभाल को अधिक मनोचिकित्सकों की प्रतीक्षा नहीं करनी पड़ती; वह आलस्य और स्वभाव को परिवारों के बहाने बताता है, कारण नहीं; और वह सामुदायिक कार्यकर्ताओं को विशेषज्ञों के साथ रखता है, हर जगह उनकी जगह नहीं।",
   "crux",
   opts=["Treating mental illness needs trained helpers and less silence about it.",
         "India needs many more psychiatrists before mental illness can be treated at all.",
         "Depression is in most cases the result of laziness or of a person's temperament.",
         "Community health workers should take the place of psychiatrists everywhere."],
   opts_hi=["मानसिक बीमारी के इलाज के लिए प्रशिक्षित सहायक और कम चुप्पी, दोनों चाहिए।",
            "मानसिक बीमारी का कोई इलाज हो, उससे पहले भारत को कहीं अधिक मनोचिकित्सक चाहिए।",
            "अवसाद अधिकांश मामलों में आलस्य या व्यक्ति के स्वभाव का परिणाम होता है।",
            "सामुदायिक स्वास्थ्य कार्यकर्ताओं को हर जगह मनोचिकित्सकों की जगह लेनी चाहिए।"],
   ans=0, pos=3)
RQ(p, "Inference", "hard", "sc", INFER, INFER_HI,
   "1 and 2 follow. When a son's withdrawal is put down to laziness and a mother's exhaustion to temperament, the illness goes unrecognised by the family (1); and trained community workers offering simple therapies show that "
   "care need not wait for specialists (2). 3 is not supported: the passage says most psychiatrists work in cities, not that mental illness is commoner there.",
   "1 और 2 निकलते हैं। जब बेटे के अलग-थलग रहने को आलस्य और माँ की थकान को स्वभाव मान लिया जाता है, तो परिवार बीमारी को पहचान ही नहीं पाता (1); और सरल चिकित्सा देने वाले प्रशिक्षित सामुदायिक कार्यकर्ता दिखाते हैं कि "
   "देखभाल को विशेषज्ञों की प्रतीक्षा नहीं करनी पड़ती (2)। 3 का समर्थन नहीं है: परिच्छेद कहता है कि अधिकांश मनोचिकित्सक शहरों में काम करते हैं, यह नहीं कि मानसिक बीमारी वहाँ अधिक है।",
   "inferences",
   st=["Some people with depression may never be seen as ill by their own families.",
       "Care for common mental disorders can be given by people who are not specialists.",
       "Mental illness is commoner in cities than in villages."],
   st_hi=["अवसाद से ग्रस्त कुछ लोगों को उनके अपने परिवार कभी बीमार मानें ही नहीं, ऐसा हो सकता है।",
          "आम मानसिक विकारों की देखभाल ऐसे लोग भी कर सकते हैं जो विशेषज्ञ नहीं हैं।",
          "मानसिक बीमारी गाँवों की तुलना में शहरों में अधिक आम है।"],
   opts=["1 only", "2 and 3 only", "1 and 2 only", "1, 2 and 3"], key=2)
RQ(p, "Assumption", "hard", "s2", ASSUME, ASSUME_HI,
   "Only 1 is assumed. The passage blames silence on families' fear of what a diagnosis would do, and makes the programmes' reach depend on people being willing to speak, which takes for granted that less shame "
   "would make more people seek help. 2 is neither stated nor needed: the passage praises simple talking therapies for common disorders without ranking them against medicines.",
   "केवल 1 पूर्वधारणा है। परिच्छेद चुप्पी का कारण इस डर को बताता है कि निदान का क्या असर होगा, और कार्यक्रमों की पहुँच को लोगों के बोलने की तत्परता पर निर्भर बताता है, जो मानकर चलता है कि कम लज्जा "
   "से अधिक लोग सहायता माँगेंगे। 2 न कहा गया है न आवश्यक है: परिच्छेद आम विकारों के लिए सरल बातचीत वाली चिकित्सा की सराहना करता है, उसकी तुलना दवाओं से किए बिना।",
   "assumptions",
   st=["People are more likely to seek help when admitting to a mental illness carries less shame.",
       "Talking therapies work better than medicines for every kind of mental disorder."],
   st_hi=["जब मानसिक बीमारी स्वीकार करने में कम लज्जा हो, तो लोगों के सहायता माँगने की संभावना अधिक होती है।",
          "बातचीत वाली चिकित्सा हर प्रकार के मानसिक विकार में दवाओं से बेहतर काम करती है।"],
   key=0)

# ------------------------------------------------------------------ P02 old crop varieties and seed banks (3)
p = passage("p02",
  "For ten thousand years farmers saved seed from their best plants, and every valley came to grow its own varieties of rice, millet or beans, each suited to its soil and its weather. In a few decades, high-yielding varieties "
  "have replaced most of them. The gains in output were real, but something was lost: varieties that tolerate drought, salt or a particular pest, which may be needed as the climate changes. Seed banks keep samples frozen, "
  "but a seed in a freezer does not go on adapting. Farmers who keep growing old varieties in their fields preserve something a vault cannot -- a crop that changes as its surroundings change.",
  "दस हज़ार वर्षों तक किसान अपने सबसे अच्छे पौधों से बीज बचाते रहे, और हर घाटी में धान, बाजरे या दालों की अपनी किस्में उगने लगीं, हर एक अपनी मिट्टी और अपने मौसम के अनुकूल। कुछ ही दशकों में अधिक उपज वाली किस्मों ने "
  "उनमें से अधिकांश की जगह ले ली है। उपज में बढ़त वास्तविक थी, पर कुछ खो भी गया: ऐसी किस्में जो सूखा, खारापन या कोई विशेष कीट सह लेती हैं, और जिनकी जलवायु बदलने पर ज़रूरत पड़ सकती है। बीज बैंक नमूनों को जमाकर रखते हैं, "
  "पर फ़्रीज़र में रखा बीज ढलना जारी नहीं रखता। जो किसान अपने खेतों में पुरानी किस्में उगाते रहते हैं, वे कुछ ऐसा सहेजते हैं जो कोई तिजोरी नहीं सहेज सकती -- ऐसी फ़सल जो अपने परिवेश के साथ बदलती रहती है।")
RQ(p, "Author's Tone", "hard", "mcq",
   "The author's attitude towards high-yielding varieties is best described as:",
   "अधिक उपज वाली किस्मों के प्रति लेखक का दृष्टिकोण सबसे अच्छी तरह कैसा बताया जा सकता है?",
   "The author says 'the gains in output were real' and then that 'something was lost' -- appreciation of the gains, with awareness of the old varieties they displaced. "
   "The passage blames them for no other problem, does not treat them as an unmixed blessing, and is plainly not indifferent to the change.",
   "लेखक कहता है कि 'उपज में बढ़त वास्तविक थी' और फिर कि 'कुछ खो भी गया' -- बढ़त की सराहना, उन पुरानी किस्मों के प्रति सजगता के साथ जिनकी जगह उन्होंने ली। "
   "परिच्छेद उन्हें किसी और समस्या के लिए दोषी नहीं ठहराता, उन्हें शुद्ध वरदान नहीं मानता, और इस बदलाव के प्रति स्पष्ट रूप से उदासीन भी नहीं है।",
   "tone",
   opts=["appreciative of their gains, aware of what they displaced",
         "hostile to them as the cause of every problem in farming",
         "uncritical of them, seeing them as an unmixed blessing",
         "indifferent to the ways in which they have changed farming"],
   opts_hi=["उनकी बढ़त का सराहक, पर उनसे हटी किस्मों के प्रति सजग",
            "उन्हें खेती की हर समस्या का कारण मानकर उनका विरोधी",
            "उन्हें शुद्ध वरदान मानकर उनके प्रति आलोचनाहीन",
            "इस बात के प्रति उदासीन कि उन्होंने खेती को किस तरह बदला है"],
   ans=0, pos=1)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Only 1 is valid: varieties that tolerate drought, salt or a pest 'may be needed as the climate changes'. "
   "2 overstates the passage, which says seed banks keep samples but cannot keep them adapting -- a limit, not a lack of all value.",
   "केवल 1 वैध है: सूखा, खारापन या कीट सहने वाली किस्मों की 'जलवायु बदलने पर ज़रूरत पड़ सकती है'। "
   "2 परिच्छेद को बढ़ा-चढ़ाकर कहता है, जो कहता है कि बीज बैंक नमूने सहेजते हैं पर उन्हें ढलते नहीं रख सकते -- यह एक सीमा है, मूल्य का पूर्ण अभाव नहीं।",
   "conclusions",
   st=["Some traditional crop varieties may prove useful as the climate changes.",
       "Seed banks are of no value in preserving the diversity of crops."],
   st_hi=["कुछ पारंपरिक फ़सल किस्में जलवायु बदलने पर उपयोगी सिद्ध हो सकती हैं।",
          "फ़सलों की विविधता सहेजने में बीज बैंकों का कोई मूल्य नहीं है।"],
   key=0)
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage traces the loss of local varieties, grants the yield gains, and ends by valuing farmers who keep old varieties growing, because a crop in the field goes on adapting while a frozen seed does not. "
   "It says the gains in output were real; it asks for no ban on new varieties; and it presents freezing as a limited safeguard, not the safest one.",
   "परिच्छेद स्थानीय किस्मों के खोने का वर्णन करता है, उपज की बढ़त मानता है, और अंत में पुरानी किस्में उगाते रहने वाले किसानों को महत्त्व देता है, क्योंकि खेत की फ़सल ढलती रहती है जबकि जमाया गया बीज नहीं। "
   "वह कहता है कि उपज की बढ़त वास्तविक थी; वह नई किस्मों पर रोक नहीं माँगता; और वह जमाकर रखने को एक सीमित सुरक्षा बताता है, सबसे सुरक्षित नहीं।",
   "crux",
   opts=["Old varieties are best kept alive in fields, where they go on adapting.",
         "High-yielding varieties have not raised the output of India's farms at all.",
         "Every valley should grow only its own traditional varieties of crops.",
         "Freezing seeds in a seed bank is the safest way to protect the diversity of crops."],
   opts_hi=["पुरानी किस्में खेतों में ही सबसे अच्छी तरह बचती हैं, जहाँ वे ढलती रहती हैं।",
            "अधिक उपज वाली किस्मों ने भारत के खेतों की उपज बिल्कुल नहीं बढ़ाई है।",
            "हर घाटी को केवल अपनी पारंपरिक फ़सल किस्में उगानी चाहिए।",
            "बीजों को फ़्रीज़र में जमाकर रखना फ़सलों की विविधता बचाने का सबसे सुरक्षित तरीका है।"],
   ans=0, pos=2)

# ------------------------------------------------------------------ P03 electric buses (3)
p = passage("p03",
  "Cities that want cleaner air often begin by replacing diesel buses with electric ones. The new buses are quiet and emit nothing from the exhaust, and over their lifetime they can cost less to run, since electricity "
  "is cheaper than diesel and electric motors need little maintenance. Their price, however, is high, and so is the cost of the depots and chargers they need, which is why many cities lease them rather than buy them, "
  "paying a private operator for each kilometre run. The bigger question is not the engine but the service: a city whose buses come rarely and crawl through traffic will not draw people out of their cars, "
  "whatever powers those buses.",
  "स्वच्छ हवा चाहने वाले शहर प्रायः डीज़ल बसों की जगह इलेक्ट्रिक बसें लाकर शुरुआत करते हैं। नई बसें शांत होती हैं और उनके निकास से कुछ नहीं निकलता, और अपने पूरे जीवनकाल में उन्हें चलाना सस्ता पड़ सकता है, क्योंकि बिजली "
  "डीज़ल से सस्ती है और इलेक्ट्रिक मोटरों को बहुत कम रखरखाव चाहिए। पर उनका दाम ऊँचा है, और उनके लिए ज़रूरी डिपो और चार्जरों की लागत भी, इसीलिए कई शहर उन्हें ख़रीदने के बजाय पट्टे पर लेते हैं, "
  "और हर चले किलोमीटर के लिए किसी निजी संचालक को भुगतान करते हैं। बड़ा प्रश्न इंजन का नहीं बल्कि सेवा का है: जिस शहर की बसें कभी-कभार आती हैं और यातायात में रेंगती हैं, वह लोगों को उनकी कारों से बाहर नहीं निकाल पाएगा, "
  "चाहे वे बसें किसी भी ऊर्जा से चलें।")
RQ(p, "Best Summary", "medium", "mcq", MSG, MSG_HI,
   "The passage grants the advantages of electric buses and explains why cities lease them, but its closing point is that frequent, fast service, not the engine, decides whether people leave their cars. "
   "It says electric buses can cost less to run over their lifetime; it explains leasing without urging cities to buy; and it never claims that the buses alone will end air pollution.",
   "परिच्छेद इलेक्ट्रिक बसों के लाभ मानता है और बताता है कि शहर उन्हें पट्टे पर क्यों लेते हैं, पर उसकी अंतिम बात यह है कि बार-बार और तेज़ सेवा, इंजन नहीं, तय करती है कि लोग अपनी कारें छोड़ेंगे या नहीं। "
   "वह कहता है कि इलेक्ट्रिक बसें अपने जीवनकाल में चलाने में सस्ती पड़ सकती हैं; वह पट्टे की व्याख्या करता है, ख़रीदने का आग्रह नहीं; और वह कहीं दावा नहीं करता कि अकेली बसें वायु प्रदूषण समाप्त कर देंगी।",
   "message",
   opts=["Electric buses help, but frequent and fast service matters more for drawing people out of cars.",
         "Electric buses cost more to run than diesel buses over the whole of their working lives.",
         "Cities should buy their electric buses outright rather than leasing them from private operators.",
         "Electric buses will by themselves put an end to the air pollution in Indian cities."],
   opts_hi=["इलेक्ट्रिक बसें मदद करती हैं, पर लोग कारें तभी छोड़ेंगे जब सेवा तेज़ और लगातार हो।",
            "अपने पूरे कार्यकाल में इलेक्ट्रिक बसें चलाने में डीज़ल बसों से अधिक महँगी पड़ती हैं।",
            "शहरों को इलेक्ट्रिक बसें निजी संचालकों से पट्टे पर लेने के बजाय सीधे ख़रीदनी चाहिए।",
            "इलेक्ट्रिक बसें अपने-आप भारतीय शहरों का वायु प्रदूषण समाप्त कर देंगी।"],
   ans=0, pos=0)
RQ(p, "Specific Detail", "medium", "mcq",
   "According to the passage, why do many cities lease electric buses instead of buying them?",
   "परिच्छेद के अनुसार, कई शहर इलेक्ट्रिक बसें ख़रीदने के बजाय पट्टे पर क्यों लेते हैं?",
   "The passage says that the buses' price is high, 'and so is the cost of the depots and chargers they need, which is why many cities lease them'. "
   "It does not say that electric buses break down more often, that private operators drive more carefully, or that leasing has anything to do with noise.",
   "परिच्छेद कहता है कि बसों का दाम ऊँचा है, 'और उनके लिए ज़रूरी डिपो और चार्जरों की लागत भी, इसीलिए कई शहर उन्हें पट्टे पर लेते हैं'। "
   "वह यह नहीं कहता कि इलेक्ट्रिक बसें अधिक बार ख़राब होती हैं, कि निजी संचालक अधिक सावधानी से चलाते हैं, या कि पट्टे का शोर से कोई संबंध है।",
   "detail",
   opts=["The buses, depots and chargers cost a great deal.",
         "Electric buses break down more often than diesel buses do.",
         "Private operators are known to drive their buses more carefully.",
         "Leased buses make less noise than the buses a city owns."],
   opts_hi=["बसों, डिपो और चार्जरों की लागत बहुत अधिक है।",
            "इलेक्ट्रिक बसें डीज़ल बसों से अधिक बार ख़राब होती हैं।",
            "निजी संचालक अपनी बसें अधिक सावधानी से चलाने के लिए जाने जाते हैं।",
            "पट्टे पर ली गई बसें शहर की अपनी बसों से कम शोर करती हैं।"],
   ans=0, pos=2)
RQ(p, "Assumption", "hard", "sc", ASSUME, ASSUME_HI,
   "1 and 2 are assumed. Saying that rare, slow buses 'will not draw people out of their cars' takes for granted that people weigh how often and how fast buses run when choosing between bus and car (1), "
   "and that drawing people out of cars is one of the things better buses are meant to do (2). 3 contradicts the passage, which says the price of electric buses is high.",
   "1 और 2 पूर्वधारणाएँ हैं। यह कहना कि कभी-कभार आने वाली धीमी बसें 'लोगों को उनकी कारों से बाहर नहीं निकाल पाएँगी', मानकर चलता है कि बस और कार में चुनते समय लोग देखते हैं कि बसें कितनी बार और कितनी तेज़ चलती हैं (1), "
   "और कि लोगों को कारों से निकालना बेहतर बसों के उद्देश्यों में से एक है (2)। 3 परिच्छेद का खंडन करता है, जो कहता है कि इलेक्ट्रिक बसों का दाम ऊँचा है।",
   "assumptions",
   st=["People choose between bus and car partly on how often and how fast the buses run.",
       "Drawing people out of their cars is one of the aims of better buses.",
       "Electric buses are cheaper to buy than diesel buses."],
   st_hi=["लोग बस और कार में चुनाव कुछ हद तक इस आधार पर करते हैं कि बसें कितनी बार और कितनी तेज़ चलती हैं।",
          "लोगों को उनकी कारों से बाहर निकालना बेहतर बसों के उद्देश्यों में से एक है।",
          "इलेक्ट्रिक बसें ख़रीदने में डीज़ल बसों से सस्ती हैं।"],
   opts=["1 only", "2 and 3 only", "1, 2 and 3", "1 and 2 only"], key=3)

# ------------------------------------------------------------------ P04 lantana in the forests (2)
p = passage("p04",
  "Lantana, a flowering shrub brought to India as a garden plant in the nineteenth century, now covers large parts of the country's forests. It grows fast, shades out the seedlings of native trees and grasses, "
  "and is avoided by grazing animals, so that where it spreads, the food available to deer and elephants shrinks. Cutting it back does little, since it regrows from the roots; it has to be uprooted, and the cleared ground "
  "replanted with native species before the shrub returns. Some villages now turn the uprooted stems into furniture and baskets, which gives people a reason to keep clearing it.",
  "लैंटाना, एक फूलदार झाड़ी जिसे उन्नीसवीं सदी में बगीचे के पौधे के रूप में भारत लाया गया था, अब देश के वनों के बड़े भाग पर फैल चुकी है। यह तेज़ी से बढ़ती है, देशी पेड़ों और घासों के पौधों को छाया में दबा देती है, "
  "और चरने वाले पशु इससे दूर रहते हैं, इसलिए जहाँ यह फैलती है, वहाँ हिरणों और हाथियों के लिए भोजन घट जाता है। इसे ऊपर से काटने से बहुत कम होता है, क्योंकि यह जड़ों से फिर उग आती है; इसे जड़ से उखाड़ना होता है, और साफ़ की गई ज़मीन पर "
  "झाड़ी के लौटने से पहले देशी प्रजातियाँ लगानी होती हैं। कुछ गाँव अब उखाड़े गए तनों से फ़र्नीचर और टोकरियाँ बनाते हैं, जिससे लोगों को इसे साफ़ करते रहने का एक कारण मिलता है।")
RQ(p, "Main Idea", "easy", "mcq", CRUX, CRUX_HI,
   "The passage describes how lantana harms forests and wildlife, explains that it must be uprooted and the ground replanted, and ends with a local use that keeps the clearing going. "
   "It presents lantana's garden origin as the start of the problem, not a reason to plant it; it says cutting back does little; and it says grazing animals avoid lantana, not that they live on it.",
   "परिच्छेद बताता है कि लैंटाना वनों और वन्यजीवों को कैसे हानि पहुँचाती है, समझाता है कि उसे उखाड़कर ज़मीन पर फिर से पौधे लगाने होंगे, और एक स्थानीय उपयोग पर समाप्त होता है जो सफ़ाई को जारी रखता है। "
   "वह बगीचे से उसकी उत्पत्ति को समस्या की शुरुआत बताता है, उसे लगाने का कारण नहीं; वह कहता है कि ऊपर से काटने से बहुत कम होता है; और वह कहता है कि चरने वाले पशु लैंटाना से दूर रहते हैं, यह नहीं कि वे उस पर जीते हैं।",
   "crux",
   opts=["Lantana harms forests and must be uprooted and replaced, helped by local uses.",
         "Lantana should be planted widely in gardens because of its attractive flowers.",
         "Cutting lantana back to the ground is quite enough to stop it from spreading again.",
         "Deer and elephants feed mainly on lantana wherever the shrub has spread."],
   opts_hi=["लैंटाना वनों की हानि करती है; उसे उखाड़कर बदलना होगा, स्थानीय उपयोग सहायक हैं।",
            "लैंटाना को उसके सुंदर फूलों के कारण बगीचों में व्यापक रूप से लगाना चाहिए।",
            "लैंटाना को ज़मीन तक काट देना उसे फिर से फैलने से रोकने के लिए पूरी तरह पर्याप्त है।",
            "जहाँ भी यह झाड़ी फैली है, वहाँ हिरण और हाथी मुख्यतः लैंटाना खाते हैं।"],
   ans=0, pos=3)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Both are valid. The cleared ground must be replanted 'before the shrub returns', so clearing without replanting may let it back (1); and turning the stems into furniture and baskets 'gives people a reason to keep clearing it' (2).",
   "दोनों वैध हैं। साफ़ की गई ज़मीन पर 'झाड़ी के लौटने से पहले' पौधे लगाने होते हैं, इसलिए बिना पौधे लगाए सफ़ाई उसे लौटने दे सकती है (1); और तनों से फ़र्नीचर और टोकरियाँ बनाना 'लोगों को इसे साफ़ करते रहने का एक कारण' देता है (2)।",
   "conclusions",
   st=["Clearing lantana without replanting the ground may let the shrub return.",
       "A use for the uprooted stems can help to keep the clearing going."],
   st_hi=["ज़मीन पर फिर से पौधे लगाए बिना लैंटाना साफ़ करने से झाड़ी लौट सकती है।",
          "उखाड़े गए तनों का कोई उपयोग सफ़ाई को जारी रखने में मदद कर सकता है।"],
   key=2)

# ------------------------------------------------------------------ P05 timely official statistics (3)
p = passage("p05",
  "Good policy needs good numbers, and good numbers need to be timely. A survey of household spending that is published five years after the fieldwork describes an economy that no longer exists; a census delayed by "
  "several years leaves welfare schemes sharing out money on the basis of population figures that are out of date. Late data do more harm than missing data in one respect: they are used as if they were current. "
  "Statistical offices therefore face a hard trade-off between the care that makes figures reliable and the speed that makes them useful, and they serve the public best when they are open about it, publishing early "
  "estimates clearly marked as provisional and revising them as fuller data come in.",
  "अच्छी नीति के लिए अच्छे आँकड़े चाहिए, और अच्छे आँकड़ों का समय पर होना ज़रूरी है। घरेलू ख़र्च का जो सर्वेक्षण क्षेत्र-कार्य के पाँच वर्ष बाद प्रकाशित होता है, वह ऐसी अर्थव्यवस्था का वर्णन करता है जो अब है ही नहीं; कई वर्षों से टली "
  "जनगणना कल्याण योजनाओं को पुराने पड़ चुके जनसंख्या आँकड़ों के आधार पर धन बाँटने पर छोड़ देती है। एक मामले में देर से आए आँकड़े न आए आँकड़ों से अधिक हानि करते हैं: उनका उपयोग ऐसे किया जाता है मानो वे वर्तमान के हों। "
  "इसलिए सांख्यिकी कार्यालयों के सामने उस सावधानी, जो आँकड़ों को विश्वसनीय बनाती है, और उस गति, जो उन्हें उपयोगी बनाती है, के बीच कठिन चुनाव है, और वे जनता की सबसे अच्छी सेवा तब करते हैं जब इस बारे में खुले रहें, आरंभिक "
  "अनुमानों को स्पष्ट रूप से अनंतिम बताकर प्रकाशित करें और पूरे आँकड़े आने पर उन्हें संशोधित करें।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage argues that figures must be timely as well as reliable, notes the trade-off between the two, and recommends early estimates marked as provisional and revised later. "
   "It says late data are worse than missing data only 'in one respect', not always; it asks for revisions, not an end to them; and it questions the timing of surveys, not whether they are needed.",
   "परिच्छेद तर्क देता है कि आँकड़े विश्वसनीय होने के साथ समय पर भी होने चाहिए, दोनों के बीच के चुनाव को रेखांकित करता है, और अनंतिम बताकर प्रकाशित तथा बाद में संशोधित आरंभिक अनुमानों की सिफ़ारिश करता है। "
   "वह कहता है कि देर से आए आँकड़े न आए आँकड़ों से केवल 'एक मामले में' बदतर हैं, सदा नहीं; वह संशोधन माँगता है, उनका अंत नहीं; और वह सर्वेक्षणों के समय पर प्रश्न उठाता है, उनकी ज़रूरत पर नहीं।",
   "crux",
   opts=["Figures must be timely and reliable; early estimates should be marked provisional.",
         "Missing data always do more harm to policy than data that arrive late.",
         "Statistical offices should stop revising any figures that they have once published.",
         "Surveys of household spending are no longer needed for making good policy."],
   opts_hi=["आँकड़े विश्वसनीय और समय पर, दोनों होने चाहिए; आरंभिक अनुमान अनंतिम बताए जाएँ।",
            "न आए आँकड़े देर से आए आँकड़ों की तुलना में नीति को सदा अधिक हानि पहुँचाते हैं।",
            "सांख्यिकी कार्यालयों को पहले से प्रकाशित आँकड़ों में संशोधन करना बंद कर देना चाहिए।",
            "अच्छी नीति बनाने के लिए घरेलू ख़र्च के सर्वेक्षणों की अब ज़रूरत नहीं है।"],
   ans=0, pos=0)
RQ(p, "Inference", "hard", "sc", INFER, INFER_HI,
   "1 and 3 follow. A census delayed by years leaves welfare schemes using population figures 'that are out of date' (1), and the passage speaks of 'a hard trade-off' between the care that makes figures reliable and the speed "
   "that makes them useful (3). 2 contradicts the passage, which asks for early estimates to be revised as fuller data come in.",
   "1 और 3 निकलते हैं। वर्षों से टली जनगणना कल्याण योजनाओं को 'पुराने पड़ चुके' जनसंख्या आँकड़ों पर छोड़ देती है (1), और परिच्छेद आँकड़ों को विश्वसनीय बनाने वाली सावधानी और उपयोगी बनाने वाली गति के बीच "
   "'कठिन चुनाव' की बात करता है (3)। 2 परिच्छेद का खंडन करता है, जो पूरे आँकड़े आने पर आरंभिक अनुमानों को संशोधित करने को कहता है।",
   "inferences",
   st=["Population figures used by welfare schemes can be out of date.",
       "A provisional estimate should never be revised once it has been published.",
       "Speed and reliability in statistics can pull in opposite directions."],
   st_hi=["कल्याण योजनाओं में प्रयुक्त जनसंख्या आँकड़े पुराने पड़ चुके हो सकते हैं।",
          "किसी अनंतिम अनुमान को एक बार प्रकाशित होने के बाद कभी संशोधित नहीं करना चाहिए।",
          "आँकड़ों में गति और विश्वसनीयता एक-दूसरे के विपरीत दिशा में खींच सकती हैं।"],
   opts=["1 only", "1 and 3 only", "2 and 3 only", "1, 2 and 3"], key=1)
RQ(p, "Assumption", "hard", "s2", ASSUME, ASSUME_HI,
   "Neither is assumed. Marking early estimates as provisional is useful only if users do notice such markings, so the passage, if anything, assumes the opposite of 1. "
   "2 is not needed: the census is one example of late data, and nothing in the argument requires it to be the only basis for sharing out welfare money.",
   "कोई भी पूर्वधारणा नहीं है। आरंभिक अनुमानों को अनंतिम बताना तभी उपयोगी है जब उपयोगकर्ता ऐसे चिह्नों पर ध्यान दें, इसलिए परिच्छेद, यदि कुछ मानता है, तो 1 का उलटा मानता है। "
   "2 की ज़रूरत नहीं: जनगणना देर से आए आँकड़ों का एक उदाहरण है, और तर्क में कुछ भी उसके कल्याण धन बाँटने का एकमात्र आधार होने पर निर्भर नहीं।",
   "assumptions",
   st=["Users of statistics never notice whether figures are marked as provisional.",
       "Census figures are the only data used in sharing out welfare money."],
   st_hi=["आँकड़ों के उपयोगकर्ता कभी ध्यान नहीं देते कि आँकड़े अनंतिम बताए गए हैं या नहीं।",
          "कल्याण धन बाँटने में केवल जनगणना के आँकड़ों का उपयोग होता है।"],
   key=3)

# ------------------------------------------------------------------ P06 the right to repair (3)
p = passage("p06",
  "A phone that stops working after two years is often thrown away, not because it cannot be fixed but because fixing it has been made hard. Some manufacturers glue in batteries, refuse to sell spare parts to independent shops, "
  "or lock software so that a repaired device stops working properly. The 'right to repair' movement asks that spare parts, manuals and tools be made available at fair prices. Its supporters point to the waste of discarded "
  "electronics and to the livelihoods of small repair shops. Manufacturers reply that open access to their devices can threaten safety and security. Both concerns are real, but a phone that cannot be opened safely by anyone "
  "outside the factory is a design choice, not a law of nature.",
  "जो फ़ोन दो वर्ष बाद काम करना बंद कर देता है, वह प्रायः फेंक दिया जाता है, इसलिए नहीं कि उसे ठीक नहीं किया जा सकता बल्कि इसलिए कि उसे ठीक करना कठिन बना दिया गया है। कुछ निर्माता बैटरियाँ चिपका देते हैं, स्वतंत्र दुकानों को कलपुर्ज़े बेचने से मना करते हैं, "
  "या सॉफ़्टवेयर पर ऐसा ताला लगाते हैं कि मरम्मत किया गया उपकरण ठीक से काम करना बंद कर दे। 'मरम्मत का अधिकार' आंदोलन माँग करता है कि कलपुर्ज़े, निर्देश-पुस्तिकाएँ और औज़ार उचित दामों पर उपलब्ध हों। उसके समर्थक फेंके गए "
  "इलेक्ट्रॉनिक सामान की बर्बादी और छोटी मरम्मत दुकानों की आजीविका की ओर इशारा करते हैं। निर्माता उत्तर देते हैं कि उनके उपकरणों तक खुली पहुँच सुरक्षा और संरक्षा के लिए ख़तरा हो सकती है। दोनों चिंताएँ वास्तविक हैं, पर जिस फ़ोन को "
  "कारख़ाने के बाहर कोई सुरक्षित रूप से खोल ही न सके, वह एक डिज़ाइन का चुनाव है, प्रकृति का नियम नहीं।")
RQ(p, "Best Summary", "medium", "mcq", MSG, MSG_HI,
   "The passage describes how repair is made hard, sets out both sides, grants that both concerns are real, and closes by calling a phone that cannot be opened safely 'a design choice' -- so safety can be designed for. "
   "It does not want phones to last only two years; it does not call repair shops a danger; and it says manufacturers' concerns are real, not baseless.",
   "परिच्छेद बताता है कि मरम्मत को कैसे कठिन बनाया जाता है, दोनों पक्ष रखता है, मानता है कि दोनों चिंताएँ वास्तविक हैं, और अंत में सुरक्षित रूप से न खुल सकने वाले फ़ोन को 'डिज़ाइन का चुनाव' कहता है -- इसलिए सुरक्षा को डिज़ाइन में लाया जा सकता है। "
   "वह नहीं चाहता कि फ़ोन केवल दो वर्ष चलें; वह मरम्मत की दुकानों को ख़तरा नहीं कहता; और वह कहता है कि निर्माताओं की चिंताएँ वास्तविक हैं, निराधार नहीं।",
   "message",
   opts=["Easier repair would cut waste, and safety can be designed in, not used as an excuse.",
         "Phones should be built so that they last no more than two years before they are replaced.",
         "Independent repair shops are a threat to the safety of the phones that they open up.",
         "Manufacturers have no reason whatsoever to worry about the security of their devices."],
   opts_hi=["आसान मरम्मत से बर्बादी घटेगी; सुरक्षा बहाना नहीं, डिज़ाइन में शामिल हो सकती है।",
            "फ़ोन ऐसे बनाए जाने चाहिए कि वे बदले जाने से पहले दो वर्ष से अधिक न चलें।",
            "स्वतंत्र मरम्मत दुकानें जिन फ़ोनों को खोलती हैं, उनकी सुरक्षा के लिए ख़तरा हैं।",
            "निर्माताओं के पास अपने उपकरणों की संरक्षा की चिंता करने का कोई कारण नहीं है।"],
   ans=0, pos=2)
RQ(p, "Specific Detail", "easy", "mcq",
   "According to the passage, which one of the following do some manufacturers do?",
   "परिच्छेद के अनुसार, कुछ निर्माता निम्नलिखित में से क्या करते हैं?",
   "The passage says that some manufacturers 'refuse to sell spare parts to independent shops'. The other options are the opposite of what it describes: it speaks of batteries glued in, not easy to replace, "
   "and of manuals and tools that the movement wants made available, not ones given away.",
   "परिच्छेद कहता है कि कुछ निर्माता 'स्वतंत्र दुकानों को कलपुर्ज़े बेचने से मना करते हैं'। बाक़ी विकल्प उसके वर्णन के उलट हैं: वह चिपकाई गई बैटरियों की बात करता है, आसानी से बदलने वाली नहीं, "
   "और ऐसी निर्देश-पुस्तिकाओं और औज़ारों की जिन्हें उपलब्ध कराने की माँग आंदोलन करता है, मुफ़्त दिए जाने वालों की नहीं।",
   "detail",
   opts=["They refuse to sell spare parts to independent shops.",
         "They give free repair manuals to independent repair shops.",
         "They make the batteries in their phones easy to replace.",
         "They pay small shops to repair phones on their behalf."],
   opts_hi=["वे स्वतंत्र दुकानों को कलपुर्ज़े बेचने से मना करते हैं।",
            "वे स्वतंत्र मरम्मत दुकानों को मुफ़्त निर्देश-पुस्तिकाएँ देते हैं।",
            "वे अपने फ़ोनों की बैटरियाँ आसानी से बदलने योग्य बनाते हैं।",
            "वे अपनी ओर से फ़ोन ठीक करने के लिए छोटी दुकानों को भुगतान करते हैं।"],
   ans=0, pos=1)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Only 2 is valid: phones are 'often thrown away, not because [they] cannot be fixed but because fixing [them] has been made hard'. 1 contradicts the passage, which says 'both concerns are real'.",
   "केवल 2 वैध है: फ़ोन 'प्रायः फेंक दिए जाते हैं, इसलिए नहीं कि उन्हें ठीक नहीं किया जा सकता बल्कि इसलिए कि उन्हें ठीक करना कठिन बना दिया गया है'। 1 परिच्छेद का खंडन करता है, जो कहता है कि 'दोनों चिंताएँ वास्तविक हैं'।",
   "conclusions",
   st=["Manufacturers' concerns about safety and security are entirely unfounded.",
       "Some phones are thrown away even though they could have been repaired."],
   st_hi=["सुरक्षा और संरक्षा के बारे में निर्माताओं की चिंताएँ पूरी तरह निराधार हैं।",
          "कुछ फ़ोन ठीक किए जा सकने के बावजूद फेंक दिए जाते हैं।"],
   key=1)

# ------------------------------------------------------------------ P07 overfishing (3)
p = passage("p07",
  "Fish caught off India's coasts feed millions and employ millions more, but in several fisheries the catch has stopped growing even as boats and nets have multiplied. When too many boats chase the same stocks, each catches "
  "fewer fish, the young are taken before they can breed, and the stock shrinks further. Seasonal bans on fishing during the breeding months help, but only if they cover the whole coast and are enforced; otherwise boats "
  "simply move to waters where the ban does not apply. Giving fishing communities a say in managing their own waters has worked in some places, because those who depend on a fishery for the long term have the strongest "
  "reason to protect it.",
  "भारत के तटों से पकड़ी गई मछलियाँ करोड़ों का पेट भरती हैं और करोड़ों को रोज़गार देती हैं, पर कई मत्स्य क्षेत्रों में नावें और जाल बढ़ने के बावजूद पकड़ बढ़नी रुक गई है। जब बहुत-सी नावें एक ही भंडार का पीछा करती हैं, तो हर नाव "
  "कम मछलियाँ पकड़ती है, छोटी मछलियाँ प्रजनन से पहले ही पकड़ ली जाती हैं, और भंडार और सिकुड़ जाता है। प्रजनन के महीनों में मछली पकड़ने पर मौसमी रोक मदद करती है, पर तभी जब वह पूरे तट पर लागू हो और उसका पालन कराया जाए; अन्यथा नावें "
  "बस उन जलक्षेत्रों में चली जाती हैं जहाँ रोक लागू नहीं है। मछुआरा समुदायों को अपने जलक्षेत्रों के प्रबंधन में भागीदारी देना कुछ स्थानों पर सफल रहा है, क्योंकि जो लोग लंबे समय तक किसी मत्स्य क्षेत्र पर निर्भर रहते हैं, उनके पास उसकी "
  "रक्षा का सबसे प्रबल कारण होता है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage explains how too many boats shrink the stocks, says seasonal bans work only when they cover the whole coast and are enforced, and credits community management where those who depend on the fishery have a say. "
   "It says more boats have not raised the catch; it says bans help under conditions, not that they have failed; and it says the fish feed millions.",
   "परिच्छेद समझाता है कि बहुत अधिक नावें भंडार कैसे घटाती हैं, कहता है कि मौसमी रोक तभी काम करती है जब वह पूरे तट पर लागू हो और उसका पालन कराया जाए, और उस सामुदायिक प्रबंधन को श्रेय देता है जिसमें मत्स्य क्षेत्र पर निर्भर लोगों की भागीदारी हो। "
   "वह कहता है कि अधिक नावों से पकड़ नहीं बढ़ी; वह कहता है कि रोक शर्तों के साथ मदद करती है, यह नहीं कि वह विफल रही; और वह कहता है कि मछलियाँ करोड़ों का पेट भरती हैं।",
   "crux",
   opts=["Overfishing is checked by enforced limits and by giving communities a stake in their waters.",
         "Adding more boats and nets is the surest way to raise the catch of fish along India's coasts.",
         "Seasonal bans on fishing have failed in every place where they have been tried.",
         "Fish caught off India's coasts are no longer an important source of food."],
   opts_hi=["अति-मत्स्यन लागू सीमाओं और समुदायों को जलक्षेत्रों में हिस्सेदारी देने से रुकता है।",
            "अधिक नावें और जाल जोड़ना भारत के तटों पर मछलियों की पकड़ बढ़ाने का सबसे पक्का तरीका है।",
            "मछली पकड़ने पर मौसमी रोक हर उस स्थान पर विफल रही है जहाँ उसे आज़माया गया।",
            "भारत के तटों से पकड़ी गई मछलियाँ अब भोजन का महत्त्वपूर्ण स्रोत नहीं हैं।"],
   ans=0, pos=0)
RQ(p, "Assumption", "hard", "s2", ASSUME, ASSUME_HI,
   "Only 1 is assumed: explaining community management's success by the strong reason its members have to protect the fishery takes for granted that, given a say, they will act on that reason. "
   "2 is not assumed and runs against the passage, which offers community management as another way that has worked.",
   "केवल 1 पूर्वधारणा है: सामुदायिक प्रबंधन की सफलता को उसके सदस्यों के पास मत्स्य क्षेत्र की रक्षा के प्रबल कारण से समझाना मानकर चलता है कि भागीदारी मिलने पर वे उस कारण के अनुसार काम करेंगे। "
   "2 पूर्वधारणा नहीं है और परिच्छेद के विरुद्ध जाता है, जो सामुदायिक प्रबंधन को एक और सफल तरीके के रूप में प्रस्तुत करता है।",
   "assumptions",
   st=["People who depend on a fishery for the long term will act to protect it if given a say in managing it.",
       "Seasonal bans are the only way to protect fish stocks from overfishing."],
   st_hi=["जो लोग लंबे समय तक किसी मत्स्य क्षेत्र पर निर्भर हैं, वे उसके प्रबंधन में भागीदारी मिलने पर उसकी रक्षा के लिए कदम उठाएँगे।",
          "मौसमी रोक ही मछली भंडारों को अति-मत्स्यन से बचाने का एकमात्र तरीका है।"],
   key=0)
RQ(p, "Inference", "hard", "sc", INFER, INFER_HI,
   "1 and 2 follow. Where a ban does not cover the whole coast, boats 'simply move to waters where the ban does not apply' (1); and the catch has stopped growing 'even as boats and nets have multiplied' (2). "
   "3 contradicts the passage, which says the young are taken before they can breed.",
   "1 और 2 निकलते हैं। जहाँ रोक पूरे तट पर लागू नहीं होती, वहाँ नावें 'बस उन जलक्षेत्रों में चली जाती हैं जहाँ रोक लागू नहीं है' (1); और पकड़ 'नावें और जाल बढ़ने के बावजूद' बढ़नी रुक गई है (2)। "
   "3 परिच्छेद का खंडन करता है, जो कहता है कि छोटी मछलियाँ प्रजनन से पहले ही पकड़ ली जाती हैं।",
   "inferences",
   st=["A ban that covers only part of the coast may simply move the fishing elsewhere.",
       "More boats do not necessarily mean a bigger catch.",
       "Young fish are never caught in Indian waters."],
   st_hi=["तट के केवल एक भाग पर लागू रोक मछली पकड़ने को बस कहीं और खिसका सकती है।",
          "अधिक नावों का अर्थ ज़रूरी नहीं कि अधिक पकड़ हो।",
          "भारतीय जलक्षेत्रों में छोटी मछलियाँ कभी नहीं पकड़ी जातीं।"],
   opts=["2 only", "1 and 3 only", "2 and 3 only", "1 and 2 only"], key=3)

# ------------------------------------------------------------------ P08 city noise (2)
p = passage("p08",
  "Noise is the pollutant that cities notice least. Horns, construction and loudspeakers routinely push sound levels in Indian cities above the limits that the rules allow, yet complaints are few, because people have come "
  "to treat the din as part of city life. The harm is not only to hearing. Long exposure to traffic noise is linked to raised blood pressure and disturbed sleep, and children in noisy schools learn to read more slowly. "
  "Unlike smoke, noise leaves no trace once it stops, which makes it easy to ignore and, for the same reason, quick to cure where the rules are enforced.",
  "शोर वह प्रदूषक है जिस पर शहर सबसे कम ध्यान देते हैं। हॉर्न, निर्माण-कार्य और लाउडस्पीकर भारतीय शहरों में ध्वनि के स्तर को नियमित रूप से नियमों द्वारा अनुमत सीमाओं से ऊपर ले जाते हैं, फिर भी शिकायतें कम होती हैं, क्योंकि लोग "
  "इस कोलाहल को शहरी जीवन का भाग मानने लगे हैं। हानि केवल सुनने की क्षमता को नहीं है। यातायात के शोर में लंबे समय तक रहना बढ़े हुए रक्तचाप और बिगड़ी नींद से जुड़ा है, और शोर भरे विद्यालयों के बच्चे पढ़ना धीरे सीखते हैं। "
  "धुएँ के विपरीत, शोर रुकने के बाद कोई निशान नहीं छोड़ता, जिससे उसे अनदेखा करना आसान है और, इसी कारण, जहाँ नियमों का पालन कराया जाए वहाँ उसका जल्दी इलाज भी संभव है।")
RQ(p, "Specific Detail", "easy", "mcq",
   "According to the passage, why are there few complaints about noise in Indian cities?",
   "परिच्छेद के अनुसार, भारतीय शहरों में शोर की शिकायतें कम क्यों होती हैं?",
   "The passage says complaints are few 'because people have come to treat the din as part of city life'. It says noise levels are routinely above the legal limits, that the harm goes beyond hearing, "
   "and nothing about complaints being barred by the rules.",
   "परिच्छेद कहता है कि शिकायतें कम हैं 'क्योंकि लोग इस कोलाहल को शहरी जीवन का भाग मानने लगे हैं'। वह कहता है कि शोर का स्तर नियमित रूप से क़ानूनी सीमाओं से ऊपर है, कि हानि सुनने की क्षमता से आगे जाती है, "
   "और नियमों द्वारा शिकायतें रोके जाने के बारे में कुछ नहीं कहता।",
   "detail",
   opts=["People have come to accept the noise as part of city life.",
         "Noise in Indian cities stays within the limits set by the rules.",
         "Noise is known to harm nothing except people's hearing.",
         "The rules do not allow people to complain about noise at all."],
   opts_hi=["लोग शोर को शहरी जीवन का भाग मानकर स्वीकार करने लगे हैं।",
            "भारतीय शहरों में शोर नियमों द्वारा तय सीमाओं के भीतर रहता है।",
            "शोर सुनने की क्षमता के सिवा किसी चीज़ को हानि नहीं पहुँचाता।",
            "नियम लोगों को शोर की शिकायत करने की अनुमति ही नहीं देते।"],
   ans=0, pos=3)
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage says city noise exceeds the limits, harms health and learning, and is ignored because it leaves no trace -- the same feature that makes it quick to cure where the rules are enforced. "
   "It compares noise with smoke only in leaving no trace, not in overall harm; it says children in noisy schools learn to read more slowly, not that they cannot; and it asks for the rules to be enforced, not for loudspeakers to be banned.",
   "परिच्छेद कहता है कि शहरी शोर सीमाओं से ऊपर है, स्वास्थ्य और पढ़ाई को हानि पहुँचाता है, और इसलिए अनदेखा होता है कि कोई निशान नहीं छोड़ता -- वही विशेषता जो नियमों का पालन कराए जाने पर उसका जल्दी इलाज संभव बनाती है। "
   "वह शोर की तुलना धुएँ से केवल निशान न छोड़ने में करता है, कुल हानि में नहीं; वह कहता है कि शोर भरे विद्यालयों के बच्चे पढ़ना धीरे सीखते हैं, यह नहीं कि सीख ही नहीं पाते; और वह नियमों का पालन कराने को कहता है, लाउडस्पीकरों पर प्रतिबंध को नहीं।",
   "crux",
   opts=["City noise does real harm that is easy to ignore, but enforcing rules can cut it fast.",
         "Noise in Indian cities is more harmful than smoke in every respect that matters to health.",
         "Children who study in noisy schools are unable to learn to read at all.",
         "Loudspeakers should be banned from every Indian city to protect people's health."],
   opts_hi=["शहरी शोर की हानि अनदेखी रहती है, पर नियम लागू होने पर वह जल्दी घट सकता है।",
            "भारतीय शहरों में शोर हर महत्त्वपूर्ण मामले में धुएँ से अधिक हानिकारक है।",
            "शोर भरे विद्यालयों में पढ़ने वाले बच्चे पढ़ना सीख ही नहीं पाते।",
            "लोगों के स्वास्थ्य की रक्षा के लिए हर भारतीय शहर में लाउडस्पीकरों पर प्रतिबंध लगना चाहिए।"],
   ans=0, pos=1)

# ------------------------------------------------------------------ P09 giving to charity well (3)
p = passage("p09",
  "When people give to charity, they usually choose a cause that moves them and an organisation they have heard of. Few ask what each rupee achieves. Yet the difference between the most and the least effective ways of "
  "doing the same good can be very large: one programme may prevent a child's death for a fraction of what another spends on the same result. Measuring results is not always possible -- the value of a library or of a free "
  "legal clinic resists counting -- and a fixation on numbers can push donors towards what is easy to measure rather than what matters. But where results can be compared, a donor who never asks is choosing, without knowing it, "
  "to do less good.",
  "दान देते समय लोग प्रायः ऐसा उद्देश्य चुनते हैं जो उन्हें छूता हो और ऐसी संस्था जिसके बारे में उन्होंने सुना हो। कम लोग पूछते हैं कि हर रुपया क्या हासिल करता है। फिर भी एक ही भलाई करने के सबसे प्रभावी और सबसे कम प्रभावी तरीकों में "
  "अंतर बहुत बड़ा हो सकता है: एक कार्यक्रम किसी बच्चे की मृत्यु उसके एक अंश ख़र्च में रोक सकता है जितना दूसरा उसी परिणाम पर ख़र्च करता है। परिणाम मापना सदा संभव नहीं -- किसी पुस्तकालय या मुफ़्त क़ानूनी सहायता केंद्र का मूल्य "
  "गिनती में नहीं आता -- और आँकड़ों का जुनून दानदाताओं को उस ओर धकेल सकता है जो मापने में आसान है, बजाय उसके जो महत्त्वपूर्ण है। पर जहाँ परिणामों की तुलना हो सकती है, वहाँ कभी न पूछने वाला दानदाता अनजाने में "
  "कम भलाई करना चुन रहा है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage urges donors to ask what their money achieves, because effectiveness varies widely, while warning that some value cannot be counted -- so compare where you can. "
   "It questions giving only to causes that move us; it says some results cannot be measured, so not every programme can be ranked; and it values libraries and legal clinics, whose worth simply resists counting.",
   "परिच्छेद दानदाताओं से आग्रह करता है कि वे पूछें कि उनका पैसा क्या हासिल करता है, क्योंकि प्रभावशीलता में बहुत अंतर होता है, और साथ ही चेताता है कि कुछ मूल्य गिने नहीं जा सकते -- इसलिए जहाँ हो सके, तुलना कीजिए। "
   "वह केवल मन को छूने वाले उद्देश्यों को दान देने पर प्रश्न उठाता है; वह कहता है कि कुछ परिणाम मापे नहीं जा सकते, इसलिए हर कार्यक्रम को क्रम में नहीं रखा जा सकता; और वह पुस्तकालयों और क़ानूनी सहायता केंद्रों को महत्त्व देता है, जिनका मूल्य बस गिनती में नहीं आता।",
   "crux",
   opts=["Donors should compare results where they can, though not all value can be measured.",
         "People should give only to the causes that move them most strongly.",
         "Every charitable programme can be ranked fairly by the results that it is able to show.",
         "Libraries and free legal clinics are a waste of the money given by donors."],
   opts_hi=["दानदाता जहाँ संभव हो परिणामों की तुलना करें, यद्यपि हर मूल्य मापा नहीं जा सकता।",
            "लोगों को केवल उन्हीं उद्देश्यों को दान देना चाहिए जो उन्हें सबसे अधिक छूते हों।",
            "हर परोपकारी कार्यक्रम को उसके दिखाए जा सकने वाले परिणामों से क्रम में रखा जा सकता है।",
            "पुस्तकालय और मुफ़्त क़ानूनी सहायता केंद्र दानदाताओं के पैसे की बर्बादी हैं।"],
   ans=0, pos=2)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Both are valid. One programme may prevent a child's death 'for a fraction of what another spends on the same result' (1); and 'a fixation on numbers can push donors towards what is easy to measure rather than what matters' (2).",
   "दोनों वैध हैं। एक कार्यक्रम किसी बच्चे की मृत्यु 'उसके एक अंश ख़र्च में' रोक सकता है 'जितना दूसरा उसी परिणाम पर ख़र्च करता है' (1); और 'आँकड़ों का जुनून दानदाताओं को उस ओर धकेल सकता है जो मापने में आसान है, बजाय उसके जो महत्त्वपूर्ण है' (2)।",
   "conclusions",
   st=["Two programmes with the same aim can differ greatly in what they spend for each result.",
       "Relying only on what can be counted may lead donors away from some valuable work."],
   st_hi=["एक ही उद्देश्य वाले दो कार्यक्रम हर परिणाम पर होने वाले ख़र्च में बहुत भिन्न हो सकते हैं।",
          "केवल गिनी जा सकने वाली चीज़ों पर निर्भर रहना दानदाताओं को कुछ मूल्यवान कामों से दूर ले जा सकता है।"],
   key=2)
RQ(p, "Assumption", "hard", "s2", ASSUME, ASSUME_HI,
   "Only 2 is assumed: blaming the donor 'who never asks' for doing less good takes for granted that the results of at least some programmes can be found out and compared. "
   "1 is not assumed: the passage says donors give to causes that move them, not that they give for praise.",
   "केवल 2 पूर्वधारणा है: 'कभी न पूछने वाले' दानदाता को कम भलाई करने का दोषी ठहराना मानकर चलता है कि कम से कम कुछ कार्यक्रमों के परिणाम जाने और तुलना किए जा सकते हैं। "
   "1 पूर्वधारणा नहीं है: परिच्छेद कहता है कि दानदाता उन उद्देश्यों को दान देते हैं जो उन्हें छूते हैं, यह नहीं कि वे प्रशंसा के लिए देते हैं।",
   "assumptions",
   st=["Every donor gives to charity in order to be praised by others.",
       "Information on the results of at least some programmes can be obtained by donors."],
   st_hi=["हर दानदाता दूसरों से प्रशंसा पाने के लिए दान देता है।",
          "दानदाता कम से कम कुछ कार्यक्रमों के परिणामों की जानकारी प्राप्त कर सकते हैं।"],
   key=1)

# ------------------------------------------------------------------ P10 streets for people on foot (3)
p = passage("p10",
  "In many Indian cities more people travel on foot than by car, yet streets are designed as if the car were the main user. Footpaths are narrow, broken or taken over by parked vehicles and shops, so pedestrians walk "
  "in the road, among the traffic. Crossing a wide road can mean a long detour to a signal or a dash between vehicles. The people most affected are those with no other choice: children, the old, and workers who cannot "
  "afford a vehicle. Making streets walkable costs far less than building flyovers, and it serves the many who already walk rather than the few who drive.",
  "भारत के कई शहरों में कार से अधिक लोग पैदल चलते हैं, फिर भी सड़कें ऐसे बनाई जाती हैं मानो कार ही उनकी मुख्य उपयोगकर्ता हो। फ़ुटपाथ संकरे हैं, टूटे हैं या खड़ी गाड़ियों और दुकानों के क़ब्ज़े में हैं, इसलिए पैदल चलने वाले "
  "यातायात के बीच सड़क पर चलते हैं। चौड़ी सड़क पार करने का अर्थ सिग्नल तक लंबा चक्कर या गाड़ियों के बीच से दौड़ हो सकता है। सबसे अधिक प्रभावित वे हैं जिनके पास और कोई विकल्प नहीं: बच्चे, बुज़ुर्ग, और ऐसे कामगार जो "
  "वाहन नहीं ख़रीद सकते। सड़कों को पैदल चलने योग्य बनाना फ़्लाईओवर बनाने से कहीं सस्ता है, और यह उन बहुतों की सेवा करता है जो पहले से पैदल चलते हैं, न कि उन थोड़े लोगों की जो गाड़ी चलाते हैं।")
RQ(p, "Best Summary", "medium", "mcq", MSG, MSG_HI,
   "The passage contrasts how many walk with how streets are built, shows who suffers, and concludes that walkable streets cost less than flyovers and serve the majority. "
   "It says more people walk than drive; it treats flyovers as the costlier option, not the way to walkability; and it says people walk in the road because the footpaths are unusable, not by choice.",
   "परिच्छेद पैदल चलने वालों की संख्या की तुलना सड़कों की बनावट से करता है, दिखाता है कि कौन कष्ट उठाता है, और निष्कर्ष निकालता है कि पैदल चलने योग्य सड़कें फ़्लाईओवरों से सस्ती हैं और बहुमत की सेवा करती हैं। "
   "वह कहता है कि गाड़ी चलाने वालों से अधिक लोग पैदल चलते हैं; वह फ़्लाईओवरों को अधिक महँगा विकल्प मानता है, पैदल चलने योग्यता का रास्ता नहीं; और वह कहता है कि लोग सड़क पर इसलिए चलते हैं कि फ़ुटपाथ उपयोग योग्य नहीं, अपनी इच्छा से नहीं।",
   "message",
   opts=["Streets built for the many who walk are cheaper and fairer than streets built for cars.",
         "Most people in Indian cities make their daily journeys by car rather than on foot.",
         "Building more flyovers is the best way to make Indian cities easier to walk in.",
         "Pedestrians walk in the road because they find it more convenient than using the footpath."],
   opts_hi=["पैदल चलने वाले बहुतों के लिए बनी सड़कें कारों की सड़कों से सस्ती और न्यायपूर्ण हैं।",
            "भारतीय शहरों के अधिकांश लोग अपनी रोज़ की यात्राएँ पैदल के बजाय कार से करते हैं।",
            "अधिक फ़्लाईओवर बनाना भारतीय शहरों को पैदल चलने में आसान बनाने का सबसे अच्छा तरीका है।",
            "पैदल चलने वाले सड़क पर इसलिए चलते हैं कि उन्हें यह फ़ुटपाथ से अधिक सुविधाजनक लगता है।"],
   ans=0, pos=0)
RQ(p, "Specific Detail", "easy", "mcq",
   "According to the passage, who are the people most affected by streets that are hard to walk on?",
   "परिच्छेद के अनुसार, जिन सड़कों पर पैदल चलना कठिन है, उनसे सबसे अधिक प्रभावित लोग कौन हैं?",
   "The passage names them: 'those with no other choice: children, the old, and workers who cannot afford a vehicle'. Drivers, shopkeepers and people near flyovers are not the ones it says are most affected.",
   "परिच्छेद उनके नाम बताता है: 'जिनके पास और कोई विकल्प नहीं: बच्चे, बुज़ुर्ग, और ऐसे कामगार जो वाहन नहीं ख़रीद सकते'। गाड़ी चलाने वाले, दुकानदार और फ़्लाईओवरों के पास रहने वाले वे लोग नहीं हैं जिन्हें वह सबसे अधिक प्रभावित बताता है।",
   "detail",
   opts=["children, the old and workers without vehicles",
         "drivers who are stuck in the city's traffic every day",
         "shopkeepers whose goods are spread over the footpaths",
         "families who live close to the new flyovers in the city"],
   opts_hi=["बच्चे, बुज़ुर्ग और बिना वाहन वाले कामगार",
            "गाड़ी चलाने वाले जो रोज़ शहर के यातायात में फँसते हैं",
            "दुकानदार जिनका सामान फ़ुटपाथों पर फैला रहता है",
            "परिवार जो शहर के नए फ़्लाईओवरों के पास रहते हैं"],
   ans=0, pos=3)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Only 1 is valid: footpaths are 'narrow, broken or taken over by parked vehicles and shops, so pedestrians walk in the road'. 2 reverses the passage, which says walkable streets cost 'far less than building flyovers'.",
   "केवल 1 वैध है: फ़ुटपाथ 'संकरे हैं, टूटे हैं या खड़ी गाड़ियों और दुकानों के क़ब्ज़े में हैं, इसलिए पैदल चलने वाले ... सड़क पर चलते हैं'। 2 परिच्छेद को उलट देता है, जो कहता है कि पैदल चलने योग्य सड़कें 'फ़्लाईओवर बनाने से कहीं सस्ती' हैं।",
   "conclusions",
   st=["Pedestrians often walk in the road because the footpaths cannot be used.",
       "Building flyovers costs less than making streets fit for walking."],
   st_hi=["पैदल चलने वाले प्रायः सड़क पर इसलिए चलते हैं कि फ़ुटपाथ उपयोग योग्य नहीं होते।",
          "फ़्लाईओवर बनाना सड़कों को पैदल चलने योग्य बनाने से सस्ता है।"],
   key=0)
