# -*- coding: utf-8 -*-
"""CSAT Level 4 · Simulator 5 -- Reading Comprehension: 10 passages, 29 items (9 x 3 and the 5th passage x 2), Layout B.

The 2025 shape. Each passage turns -- a claim, then its limit. Themes, none used in Levels 1-3 or Simulators 1-4: the
market for lemons, the coffee mugs that owners would not sell, Semmelweis and the washing of hands, the Directive
Principles, Moore's law, the paradox of water and diamonds, eyes on the street, the salt-and-sugar drink that saved
cholera patients, Blackstone's ratio, and lichens as a gauge of clean air. Item types: main idea 9, inference 17,
specific detail 3. Two-statement keys 2 / 3 / 2 / 2 (1 only / 2 only / Both / Neither). Difficulty 1 easy / 17 medium /
11 hard. Options are named by content in every explanation."""
from csat_common import passage, RQ

CRUX = "Which one of the following statements best reflects the crux of the passage?"
CRUX_HI = "निम्नलिखित में से कौन-सा कथन परिच्छेद के सार को सबसे अच्छी तरह व्यक्त करता है?"
MSG = "Which one of the following statements best reflects the most logical and rational message conveyed by the passage?"
MSG_HI = "निम्नलिखित में से कौन-सा कथन परिच्छेद द्वारा दिए गए सबसे तार्किक और विवेकपूर्ण संदेश को सबसे अच्छी तरह व्यक्त करता है?"
VALID = "On the basis of the passage, which of the following conclusions is/are valid?"
VALID_HI = "परिच्छेद के आधार पर निम्नलिखित में से कौन-सा/से निष्कर्ष वैध है/हैं?"
ASSUME = "Which of the following assumptions has/have been made in the passage?"
ASSUME_HI = "परिच्छेद में निम्नलिखित में से कौन-सी पूर्वधारणा/एँ बनाई गई है/हैं?"

# ------------------------------------------------------------------ P01 the market for lemons
p = passage("p01",
  "In 1970 the economist George Akerlof described a market for used cars in which every seller knows whether a car is sound or a 'lemon', but no buyer can tell. Unable to tell them apart, buyers will offer only a price suited to a car of average quality. The owners of good cars find that price too low and keep their cars off the market. The cars on offer are then worse on average, so buyers offer still less, and more good cars are withdrawn. In the extreme, only lemons are left for sale. "
  "The trouble is not that sellers lie, but that what they know cannot be shown to buyers. That is why such markets develop ways for the seller of a good car to prove it -- warranties, independent inspections, and dealers who have a reputation to protect.",
  "1970 में अर्थशास्त्री जॉर्ज एकरलॉफ़ ने पुरानी गाड़ियों के एक ऐसे बाज़ार का वर्णन किया जिसमें हर विक्रेता जानता है कि गाड़ी ठीक है या 'लेमन' (ख़राब), पर कोई ख़रीदार यह नहीं बता सकता। उन्हें अलग न कर पाने के कारण ख़रीदार केवल औसत गुणवत्ता की गाड़ी के लायक़ मूल्य देंगे। अच्छी गाड़ियों के मालिकों को वह मूल्य बहुत कम लगता है और वे अपनी गाड़ियाँ बाज़ार से दूर रखते हैं। तब बिक्री पर गाड़ियाँ औसतन और ख़राब होती हैं, इसलिए ख़रीदार और भी कम देते हैं, और और अच्छी गाड़ियाँ हट जाती हैं। चरम स्थिति में बिक्री के लिए केवल ख़राब गाड़ियाँ बचती हैं। "
  "कठिनाई यह नहीं कि विक्रेता झूठ बोलते हैं, बल्कि यह कि वे जो जानते हैं उसे ख़रीदारों को दिखाया नहीं जा सकता। इसीलिए ऐसे बाज़ारों में अच्छी गाड़ी के विक्रेता के लिए उसे सिद्ध करने के तरीक़े विकसित होते हैं -- वारंटी, स्वतंत्र निरीक्षण, और ऐसे डीलर जिनकी बचाने लायक़ साख हो।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage shows how buyers who cannot judge quality drive good cars out of the market, and ends with the remedies that let sellers prove quality. "
   "It says the trouble is 'not that sellers lie', so dishonesty is not its point; it does not say every used car is a lemon -- only that, in the extreme, lemons are what is left; and it presents warranties as a remedy, not a cause.",
   "परिच्छेद दिखाता है कि गुणवत्ता न आँक पाने वाले ख़रीदार अच्छी गाड़ियों को बाज़ार से कैसे बाहर कर देते हैं, और उन उपायों पर समाप्त होता है जिनसे विक्रेता गुणवत्ता सिद्ध कर सकें। "
   "वह कहता है कि कठिनाई 'यह नहीं कि विक्रेता झूठ बोलते हैं', इसलिए बेईमानी उसकी बात नहीं; वह यह नहीं कहता कि हर पुरानी गाड़ी ख़राब है -- केवल यह कि चरम स्थिति में ख़राब गाड़ियाँ ही बचती हैं; और वह वारंटी को उपाय बताता है, कारण नहीं।",
   "crux",
   opts=["When buyers cannot tell good goods from bad, good ones may be driven out unless quality can be shown.",
         "Most sellers of used cars are dishonest, and buyers should never trust what any seller says about a car.",
         "Every used car on sale is likely to be a lemon, so buying a new car is always the wiser choice.",
         "Warranties and inspections are the main reason why so many poor cars are offered on the used-car market."],
   opts_hi=["जब ख़रीदार अच्छे और ख़राब सामान को अलग न कर सकें, तो गुणवत्ता दिखाने के बिना अच्छा सामान बाहर हो सकता है।",
            "पुरानी गाड़ियों के अधिकांश विक्रेता बेईमान हैं, और ख़रीदारों को किसी विक्रेता की बात पर कभी भरोसा नहीं करना चाहिए।",
            "बिक्री पर हर पुरानी गाड़ी के ख़राब होने की संभावना है, इसलिए नई गाड़ी ख़रीदना हमेशा अधिक समझदारी है।",
            "वारंटी और निरीक्षण ही वह मुख्य कारण हैं जिससे पुरानी गाड़ियों के बाज़ार में इतनी ख़राब गाड़ियाँ आती हैं।"],
   ans=0, pos=0)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Only 1 is valid. A long warranty costs the seller of a lemon dearly, since it will break down and have to be repaired; the seller of a sound car can offer one cheaply. So, on the passage's reasoning, a warranty is a way for the seller of a good car to prove it. "
   "2 reverses the passage: buyers offer a price suited to average quality, which is too little for good cars -- that is why their owners withdraw them.",
   "केवल 1 वैध है। लंबी वारंटी ख़राब गाड़ी के विक्रेता को बहुत महँगी पड़ती है, क्योंकि गाड़ी ख़राब होगी और ठीक करनी पड़ेगी; ठीक गाड़ी का विक्रेता उसे सस्ते में दे सकता है। इसलिए, परिच्छेद के तर्क से, वारंटी अच्छी गाड़ी के विक्रेता के लिए उसे सिद्ध करने का एक तरीक़ा है। "
   "2 परिच्छेद को उलट देता है: ख़रीदार औसत गुणवत्ता के लायक़ मूल्य देते हैं, जो अच्छी गाड़ियों के लिए बहुत कम है -- इसीलिए उनके मालिक उन्हें हटा लेते हैं।",
   "conclusions",
   st=["A seller who offers a long warranty is, on the passage's reasoning, more likely to be selling a sound car.",
       "In the market described, buyers end up paying more than good cars are worth."],
   st_hi=["परिच्छेद के तर्क से, लंबी वारंटी देने वाले विक्रेता के ठीक गाड़ी बेचने की संभावना अधिक है।",
          "वर्णित बाज़ार में ख़रीदार अंततः अच्छी गाड़ियों के मूल्य से अधिक चुकाते हैं।"],
   key=0)
RQ(p, "Specific Detail", "medium", "mcq",
   "According to the passage, why do the owners of good cars keep them off the market?",
   "परिच्छेद के अनुसार, अच्छी गाड़ियों के मालिक उन्हें बाज़ार से दूर क्यों रखते हैं?",
   "Buyers who cannot tell good cars from bad offer a price suited to average quality, and the owners of good cars find that too low. "
   "The passage does not say that good cars are hard to sell for lack of buyers, that owners fear inspections, or that the law forbids their sale.",
   "जो ख़रीदार अच्छी और ख़राब गाड़ियों में भेद नहीं कर सकते, वे औसत गुणवत्ता के लायक़ मूल्य देते हैं, और अच्छी गाड़ियों के मालिकों को वह बहुत कम लगता है। "
   "परिच्छेद यह नहीं कहता कि ख़रीदारों की कमी से अच्छी गाड़ियाँ बेचना कठिन है, कि मालिक निरीक्षण से डरते हैं, या कि क़ानून उनकी बिक्री रोकता है।",
   "why-good-cars-are-withdrawn",
   opts=["There are too few buyers in such a market for anyone to sell a car quickly.",
         "The price buyers offer suits a car of average quality, which is too little for a good one.",
         "Their owners fear that an independent inspection would find hidden faults in the car.",
         "The law in such markets does not allow good cars to be sold at a higher price than poor ones."],
   opts_hi=["ऐसे बाज़ार में इतने कम ख़रीदार हैं कि कोई भी अपनी गाड़ी जल्दी नहीं बेच सकता।",
            "ख़रीदारों का दिया मूल्य औसत गाड़ी के लायक़ है, जो अच्छी गाड़ी के लिए बहुत कम है।",
            "उनके मालिकों को डर है कि स्वतंत्र निरीक्षण गाड़ी में छिपी ख़राबियाँ पकड़ लेगा।",
            "ऐसे बाज़ारों में क़ानून अच्छी गाड़ियों को ख़राब गाड़ियों से ऊँचे मूल्य पर बेचने नहीं देता।"],
   ans=1, pos=1)

# ------------------------------------------------------------------ P02 the coffee mugs that owners would not sell
p = passage("p02",
  "In an experiment published in 1990, the economists Daniel Kahneman, Jack Knetsch and Richard Thaler gave coffee mugs to half the students in a class, chosen at random, and let them trade with the others. Since the mugs had gone to students at random, about half should have ended up with those who valued them most, and many mugs should have changed hands. Few did. The owners' typical asking price was more than twice what the others were willing to pay. "
  "Owning the mug, even for a few minutes, seemed to make it worth more to its owner. A common explanation is that giving something up is felt as a loss, and losses weigh more heavily than gains of the same size. The effect is not universal, though: studies of experienced traders, who buy things in order to sell them, find it much weaker.",
  "1990 में प्रकाशित एक प्रयोग में अर्थशास्त्री डेनियल काह्नमन, जैक नेच और रिचर्ड थेलर ने एक कक्षा के आधे विद्यार्थियों को, यादृच्छिक रूप से चुनकर, कॉफ़ी के मग दिए और उन्हें बाक़ी के साथ लेन-देन करने दिया। चूँकि मग यादृच्छिक रूप से दिए गए थे, लगभग आधे उन तक पहुँचने चाहिए थे जो उन्हें सबसे अधिक महत्त्व देते, और बहुत-से मग हाथ बदलने चाहिए थे। बहुत कम बदले। मालिकों का सामान्य माँगा गया मूल्य उससे दोगुने से भी अधिक था जो बाक़ी देने को तैयार थे। "
  "मग का मालिक होना, कुछ मिनटों के लिए भी, उसे उसके मालिक के लिए अधिक मूल्यवान बनाता लगा। एक आम व्याख्या यह है कि कुछ छोड़ना हानि जैसा लगता है, और हानियाँ उतने ही बड़े लाभों से अधिक भारी पड़ती हैं। फिर भी यह प्रभाव सार्वभौमिक नहीं: अनुभवी व्यापारियों के अध्ययन, जो चीज़ें बेचने के लिए ही ख़रीदते हैं, इसे बहुत कमज़ोर पाते हैं।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage reports that owning a mug made its owner value it more, explains this by the weight of losses, and limits the claim: experienced traders show the effect much less. "
   "It says few mugs changed hands, not that students refused to trade at all; it treats the effect as weaker among traders, not as absent everywhere; and it gives no reason to think the mugs differed in quality.",
   "परिच्छेद बताता है कि मग का मालिक होना मालिक के लिए उसका मूल्य बढ़ा देता था, इसे हानियों के भार से समझाता है, और दावे को सीमित करता है: अनुभवी व्यापारियों में प्रभाव बहुत कम दिखता है। "
   "वह कहता है कि बहुत कम मग हाथ बदले, यह नहीं कि विद्यार्थियों ने लेन-देन से ही मना कर दिया; वह प्रभाव को व्यापारियों में कमज़ोर बताता है, हर जगह अनुपस्थित नहीं; और यह मानने का कोई कारण नहीं देता कि मग गुणवत्ता में अलग थे।",
   "crux",
   opts=["The students refused to trade at all, because they had been given the mugs as a gift.",
         "The mugs given to the owners were better than those the other students could buy elsewhere.",
         "People tend to value a thing more once they own it, though trading experience weakens this.",
         "Owning a thing makes everyone value it more, and no amount of experience can change this."],
   opts_hi=["विद्यार्थियों ने लेन-देन से ही पूरी तरह मना कर दिया, क्योंकि मग उन्हें उपहार में मिले थे।",
            "मालिकों को दिए गए मग उनसे बेहतर थे जो बाक़ी विद्यार्थी कहीं और ख़रीद सकते थे।",
            "लोग किसी चीज़ का मालिक बनने पर उसे अधिक महत्त्व देते हैं, यद्यपि व्यापार का अनुभव इसे कमज़ोर करता है।",
            "किसी चीज़ का मालिक होना हर व्यक्ति के लिए उसका मूल्य बढ़ा देता है, और कोई भी अनुभव इसे नहीं बदल सकता।"],
   ans=2, pos=2)
RQ(p, "Inference", "hard", "mcq",
   "Which one of the following is best explained by the effect the passage describes?",
   "परिच्छेद में वर्णित प्रभाव निम्नलिखित में से किसकी सबसे अच्छी व्याख्या करता है?",
   "The effect is that owning a thing raises the value its owner puts on it, because giving it up feels like a loss. A family that would not sell its old scooter for the price it would not pay for an identical one shows exactly that gap between selling and buying. "
   "A dealer who sells stock quickly is the experienced trader in whom the effect is weak; a buyer comparing prices is ordinary shopping; and a shop raising prices when demand rises is about the market, not about ownership.",
   "प्रभाव यह है कि किसी चीज़ का मालिक होना उस पर मालिक द्वारा लगाया गया मूल्य बढ़ा देता है, क्योंकि उसे छोड़ना हानि जैसा लगता है। जो परिवार अपना पुराना स्कूटर उस मूल्य पर नहीं बेचेगा जिस पर वह वैसा ही दूसरा स्कूटर ख़रीदेगा भी नहीं, वह बेचने और ख़रीदने के बीच ठीक वही अंतर दिखाता है। "
   "माल जल्दी बेचने वाला डीलर वही अनुभवी व्यापारी है जिसमें प्रभाव कमज़ोर है; दाम मिलाने वाला ख़रीदार सामान्य ख़रीदारी है; और माँग बढ़ने पर दाम बढ़ाने वाली दुकान बाज़ार के बारे में है, स्वामित्व के बारे में नहीं।",
   "what-the-effect-explains",
   opts=["A car dealer who sells most of the cars on the lot within a week of buying them",
         "A shopper who checks the price of a phone in three different shops before deciding to buy it",
         "A shop that raises the price of umbrellas on the first rainy day of the season",
         "A family that would not sell its scooter at a price it would not pay for the same model"],
   opts_hi=["ऐसा कार डीलर जो अहाते की अधिकांश गाड़ियाँ ख़रीदने के एक सप्ताह के भीतर बेच देता है",
            "ऐसा ख़रीदार जो फ़ोन ख़रीदने का निर्णय लेने से पहले तीन अलग-अलग दुकानों में उसका दाम देखता है",
            "ऐसी दुकान जो मौसम के पहले बरसाती दिन छातों के दाम बढ़ा देती है",
            "ऐसा परिवार जो अपना स्कूटर उस मूल्य पर नहीं बेचेगा जो वह वैसे ही मॉडल के लिए नहीं देगा"],
   ans=3, pos=3)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Only 2 is valid. The mugs went to students at random, so whether a student owned one had nothing to do with how much that student liked mugs; the gap between owners and others must come from owning itself. "
   "1 goes too far: the passage reports a weaker effect among experienced traders, not that people who trade often never value what they own more.",
   "केवल 2 वैध है। मग विद्यार्थियों को यादृच्छिक रूप से मिले थे, इसलिए किसी विद्यार्थी के पास मग होने का इससे कोई संबंध नहीं था कि उसे मग कितने पसंद थे; मालिकों और बाक़ी के बीच का अंतर स्वयं स्वामित्व से ही आया होगा। "
   "1 बहुत आगे जाता है: परिच्छेद अनुभवी व्यापारियों में कमज़ोर प्रभाव बताता है, यह नहीं कि बार-बार व्यापार करने वाले अपनी चीज़ को कभी अधिक महत्त्व नहीं देते।",
   "conclusions",
   st=["People who trade often never value the things they own more than other people do.",
       "Handing out the mugs at random was what allowed the gap in prices to be put down to owning them."],
   st_hi=["बार-बार व्यापार करने वाले लोग अपनी चीज़ों को कभी भी दूसरों से अधिक महत्त्व नहीं देते।",
          "मगों को यादृच्छिक रूप से बाँटने से ही दामों के अंतर का कारण स्वामित्व को माना जा सका।"],
   key=1)

# ------------------------------------------------------------------ P03 Semmelweis and the washing of hands
p = passage("p03",
  "In the 1840s, in the maternity wards of Vienna's General Hospital, women delivered by doctors and medical students died of childbed fever far more often than women delivered by midwives in the neighbouring ward. The physician Ignaz Semmelweis noticed that the doctors often came to the ward straight from dissecting corpses. In 1847 he made them wash their hands in a solution of chlorinated lime before examining patients, and deaths in their ward fell sharply. "
  "Yet many senior doctors rejected his conclusion. Some were offended by the suggestion that they themselves carried disease, and Semmelweis could not explain how matter from corpses caused fever. His practice spread widely only decades later, after the work of Louis Pasteur and Joseph Lister had shown that germs cause infection. The evidence had been there; what was missing was an account of why it should be true.",
  "1840 के दशक में, वियना के जनरल अस्पताल के प्रसूति वार्डों में, डॉक्टरों और चिकित्सा विद्यार्थियों द्वारा प्रसव कराई गई महिलाएँ पड़ोसी वार्ड में दाइयों द्वारा प्रसव कराई गई महिलाओं की तुलना में प्रसूति ज्वर से कहीं अधिक मरती थीं। चिकित्सक इग्नाज़ सेमेलवाइस ने देखा कि डॉक्टर प्रायः शवों की चीर-फाड़ से सीधे वार्ड में आते थे। 1847 में उन्होंने उन्हें रोगियों की जाँच से पहले क्लोरीनयुक्त चूने के घोल में हाथ धोने को कहा, और उनके वार्ड में मौतें तेज़ी से घटीं। "
  "फिर भी कई वरिष्ठ डॉक्टरों ने उनके निष्कर्ष को ठुकरा दिया। कुछ इस सुझाव से आहत हुए कि वे स्वयं रोग ले जाते हैं, और सेमेलवाइस यह नहीं समझा सके कि शवों का पदार्थ ज्वर कैसे पैदा करता है। उनकी प्रथा दशकों बाद ही व्यापक रूप से फैली, जब लुई पाश्चर और जोसेफ़ लिस्टर के काम ने दिखाया कि कीटाणु संक्रमण पैदा करते हैं। प्रमाण मौजूद था; जो अनुपस्थित था वह इस बात की व्याख्या थी कि वह सत्य क्यों होना चाहिए।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage tells how clear evidence that handwashing saved lives was resisted -- partly from pride, partly because no one could yet explain it -- until germ theory supplied the explanation. "
   "It says deaths fell sharply, so the evidence was not weak; it does not say midwives were better trained; and it presents the rejection as a failure, not as sound caution that was later proved right.",
   "परिच्छेद बताता है कि हाथ धोने से जान बचने के स्पष्ट प्रमाण का विरोध हुआ -- कुछ अहं से, कुछ इसलिए कि तब कोई उसे समझा नहीं सकता था -- जब तक कीटाणु सिद्धांत ने व्याख्या नहीं दी। "
   "वह कहता है कि मौतें तेज़ी से घटीं, इसलिए प्रमाण कमज़ोर नहीं था; वह यह नहीं कहता कि दाइयाँ बेहतर प्रशिक्षित थीं; और वह अस्वीकृति को एक विफलता के रूप में रखता है, ऐसी समझदार सावधानी के रूप में नहीं जो बाद में सही सिद्ध हुई।",
   "crux",
   opts=["Midwives in Vienna were better trained than the doctors and medical students of the hospital.",
         "The doctors were right to reject Semmelweis's claim, since his evidence was too weak to trust.",
         "Strong evidence can be resisted for years when it wounds pride and no one can yet explain it.",
         "Washing hands in chlorinated lime is still the best protection against all infections in hospitals."],
   opts_hi=["वियना की दाइयाँ अस्पताल के डॉक्टरों और चिकित्सा विद्यार्थियों से बेहतर प्रशिक्षित थीं।",
            "डॉक्टरों का सेमेलवाइस के दावे को ठुकराना सही था, क्योंकि उनका प्रमाण भरोसे के लिए बहुत कमज़ोर था।",
            "मज़बूत प्रमाण का वर्षों तक विरोध हो सकता है जब वह अहं को चोट पहुँचाए और कोई उसे अभी समझा न सके।",
            "क्लोरीनयुक्त चूने से हाथ धोना आज भी अस्पतालों में सभी संक्रमणों से सबसे अच्छी सुरक्षा है।"],
   ans=2, pos=2)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Neither is valid. 1 goes beyond the passage: it says Semmelweis could not explain how matter from corpses caused fever, but nothing in it says he was wrong that hands carried it -- the fall in deaths and the later germ theory both support him. "
   "2 also goes too far: the passage says some doctors were offended, and that the explanation was missing, but not that they rejected the idea only out of pride; it names two reasons.",
   "कोई भी वैध नहीं। 1 परिच्छेद से आगे जाता है: वह कहता है कि सेमेलवाइस समझा नहीं सके कि शवों का पदार्थ ज्वर कैसे पैदा करता है, पर उसमें कुछ भी यह नहीं कहता कि हाथों के उसे ले जाने के बारे में वे ग़लत थे -- मौतों का घटना और बाद का कीटाणु सिद्धांत दोनों उनका समर्थन करते हैं। "
   "2 भी बहुत आगे जाता है: परिच्छेद कहता है कि कुछ डॉक्टर आहत हुए, और कि व्याख्या अनुपस्थित थी, पर यह नहीं कि उन्होंने विचार को केवल अहं के कारण ठुकराया; वह दो कारण बताता है।",
   "conclusions",
   st=["Semmelweis was wrong to think that the doctors' hands carried the cause of the fever.",
       "The senior doctors rejected Semmelweis's conclusion only because it hurt their pride."],
   st_hi=["सेमेलवाइस का यह सोचना ग़लत था कि डॉक्टरों के हाथ ज्वर का कारण ले जाते थे।",
          "वरिष्ठ डॉक्टरों ने सेमेलवाइस के निष्कर्ष को केवल इसलिए ठुकराया कि उससे उनके अहं को चोट पहुँची।"],
   key=3)
RQ(p, "Inference", "medium", "mcq",
   "Why does the passage mention that the women delivered by midwives died less often?",
   "परिच्छेद यह उल्लेख क्यों करता है कि दाइयों द्वारा प्रसव कराई गई महिलाएँ कम मरती थीं?",
   "The midwives' ward is the comparison that pointed to the cause: in the same hospital, women delivered by people who did not come from dissecting corpses died less often. That made the doctors' hands the thing to look at. "
   "The passage does not say midwives were more skilled, that the two wards had different rules about visitors, or that the comparison proved germ theory, which came decades later.",
   "दाइयों का वार्ड वह तुलना है जिसने कारण की ओर संकेत किया: उसी अस्पताल में, जिन महिलाओं का प्रसव शवों की चीर-फाड़ से न आने वाले लोगों ने कराया, वे कम मरीं। इससे डॉक्टरों के हाथ ही देखने लायक़ बात बने। "
   "परिच्छेद यह नहीं कहता कि दाइयाँ अधिक कुशल थीं, कि दोनों वार्डों में आगंतुकों के नियम अलग थे, या कि तुलना ने कीटाणु सिद्धांत सिद्ध किया, जो दशकों बाद आया।",
   "why-the-midwives-ward-matters",
   opts=["It is a comparison pointing to something the doctors did and the midwives did not.",
         "It shows that midwives were more skilful than doctors at delivering babies safely.",
         "It shows that the two wards had different rules about who could visit the mothers.",
         "It proves that germs cause infection, which Pasteur and Lister merely confirmed later."],
   opts_hi=["यह ऐसी तुलना देता है जिसने उस बात की ओर संकेत किया जो डॉक्टर करते थे और दाइयाँ नहीं।",
            "यह दिखाता है कि दाइयाँ सुरक्षित प्रसव कराने में डॉक्टरों से अधिक कुशल थीं।",
            "यह दिखाता है कि दोनों वार्डों में माताओं से मिलने के नियम अलग-अलग थे।",
            "यह सिद्ध करता है कि कीटाणु संक्रमण पैदा करते हैं, जिसकी पाश्चर और लिस्टर ने बाद में केवल पुष्टि की।"],
   ans=0, pos=0)

# ------------------------------------------------------------------ P04 the Directive Principles
p = passage("p04",
  "Part IV of the Constitution of India sets out the Directive Principles of State Policy: that the State should work towards adequate means of livelihood for all, equal pay for equal work, free and compulsory education for children, and much else. Article 37 says that these principles cannot be enforced by any court, and yet that they are fundamental in the governance of the country and that the State has a duty to apply them in making laws. "
  "The framers made them unenforceable not because they thought them unimportant, but because a poor new country could not promise to meet them all at once; they were goals to be reached as the State's means grew. Over time some have moved closer to enforceable rights. Free and compulsory education for children aged six to fourteen, once a directive, was made a fundamental right by an amendment in 2002. A directive, then, is less a promise broken than a promise deferred.",
  "भारत के संविधान का भाग IV राज्य के नीति निदेशक तत्त्व बताता है: कि राज्य सबके लिए आजीविका के पर्याप्त साधनों, समान कार्य के लिए समान वेतन, बच्चों के लिए निःशुल्क और अनिवार्य शिक्षा, और बहुत कुछ की दिशा में काम करे। अनुच्छेद 37 कहता है कि ये तत्त्व किसी न्यायालय द्वारा लागू नहीं कराए जा सकते, फिर भी वे देश के शासन में मूलभूत हैं और क़ानून बनाते समय उन्हें लागू करना राज्य का कर्तव्य है। "
  "संविधान निर्माताओं ने उन्हें इसलिए अप्रवर्तनीय नहीं बनाया कि वे उन्हें महत्त्वहीन मानते थे, बल्कि इसलिए कि एक निर्धन नया देश उन सबको एक साथ पूरा करने का वचन नहीं दे सकता था; वे लक्ष्य थे जिन तक राज्य के साधन बढ़ने के साथ पहुँचना था। समय के साथ कुछ प्रवर्तनीय अधिकारों के निकट आए हैं। छह से चौदह वर्ष के बच्चों के लिए निःशुल्क और अनिवार्य शिक्षा, जो कभी एक निदेशक तत्त्व थी, 2002 के एक संशोधन द्वारा मौलिक अधिकार बना दी गई। अतः निदेशक तत्त्व टूटा हुआ वचन कम और स्थगित वचन अधिक है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage explains that the Directive Principles were made unenforceable because they could not all be met at once, not because they were unimportant, and shows one of them later becoming a right: a promise deferred. "
   "Article 37 calls them fundamental in governance, so they are not mere decoration; the passage does not say courts may enforce them now; and it shows them shaping law, not being ignored.",
   "परिच्छेद बताता है कि नीति निदेशक तत्त्वों को इसलिए अप्रवर्तनीय बनाया गया कि वे सब एक साथ पूरे नहीं किए जा सकते थे, इसलिए नहीं कि वे महत्त्वहीन थे, और उनमें से एक को बाद में अधिकार बनते दिखाता है: एक स्थगित वचन। "
   "अनुच्छेद 37 उन्हें शासन में मूलभूत कहता है, इसलिए वे केवल सजावट नहीं; परिच्छेद यह नहीं कहता कि न्यायालय अब उन्हें लागू करा सकते हैं; और वह उन्हें क़ानून को आकार देते दिखाता है, अनदेखा होते नहीं।",
   "crux",
   opts=["The Directive Principles are words of good intention that have had no effect on any law.",
         "The Directives were goals a poor country could not yet enforce, to be met as means grew.",
         "Every Directive Principle can now be enforced in court like any fundamental right.",
         "The framers thought the Directives less important than the other parts of the Constitution."],
   opts_hi=["नीति निदेशक तत्त्व अच्छे इरादे के ऐसे शब्द हैं जिनका किसी क़ानून पर कोई प्रभाव नहीं पड़ा।",
            "निदेशक तत्त्व निर्धन देश के अप्रवर्तनीय लक्ष्य थे, जिन्हें साधन बढ़ने पर पूरा करना था।",
            "हर नीति निदेशक तत्त्व अब किसी भी मौलिक अधिकार की तरह न्यायालय में लागू कराया जा सकता है।",
            "संविधान निर्माता निदेशक तत्त्वों को संविधान के अन्य भागों से कम महत्त्वपूर्ण मानते थे।"],
   ans=1, pos=1)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Both are valid. The 2002 amendment that made children's education a fundamental right shows that a directive can later become an enforceable right (1). "
   "And the passage says the directives were goals 'to be reached as the State's means grew', so the framers expected the State's capacity to meet them to increase over time (2).",
   "दोनों वैध हैं। 2002 का संशोधन, जिसने बच्चों की शिक्षा को मौलिक अधिकार बनाया, दिखाता है कि कोई निदेशक तत्त्व बाद में प्रवर्तनीय अधिकार बन सकता है (1)। "
   "और परिच्छेद कहता है कि निदेशक तत्त्व ऐसे लक्ष्य थे 'जिन तक राज्य के साधन बढ़ने के साथ पहुँचना था', इसलिए निर्माताओं को आशा थी कि उन्हें पूरा करने की राज्य की क्षमता समय के साथ बढ़ेगी (2)।",
   "conclusions",
   st=["What begins as a Directive Principle can later be turned into a right that courts enforce.",
       "The framers expected the State's ability to meet the Directives to grow over time."],
   st_hi=["जो नीति निदेशक तत्त्व के रूप में शुरू होता है, उसे बाद में न्यायालयों द्वारा लागू कराए जाने वाले अधिकार में बदला जा सकता है।",
          "संविधान निर्माताओं को आशा थी कि निदेशक तत्त्वों को पूरा करने की राज्य की क्षमता समय के साथ बढ़ेगी।"],
   key=2)
RQ(p, "Specific Detail", "medium", "mcq",
   "According to the passage, what does Article 37 say about the Directive Principles?",
   "परिच्छेद के अनुसार, अनुच्छेद 37 नीति निदेशक तत्त्वों के बारे में क्या कहता है?",
   "The passage says Article 37 makes the principles unenforceable in any court, yet fundamental in governance, with a duty on the State to apply them in making laws. "
   "It does not say they bind the courts, that they may be ignored when inconvenient, or that they apply only to the States and not to the Union.",
   "परिच्छेद कहता है कि अनुच्छेद 37 तत्त्वों को किसी न्यायालय में अप्रवर्तनीय, फिर भी शासन में मूलभूत बनाता है, और क़ानून बनाते समय उन्हें लागू करने का कर्तव्य राज्य पर डालता है। "
   "वह यह नहीं कहता कि वे न्यायालयों को बाँधते हैं, कि असुविधा होने पर उन्हें अनदेखा किया जा सकता है, या कि वे केवल राज्यों पर लागू होते हैं, संघ पर नहीं।",
   "what-article-37-says",
   opts=["Courts must enforce them whenever a citizen shows that the State has failed to apply one.",
         "The State may set them aside whenever applying them in a law would prove inconvenient.",
         "They bind only the governments of the States, and not the government of the Union.",
         "No court can enforce them, yet the State has a duty to apply them in making laws."],
   opts_hi=["जब भी कोई नागरिक दिखाए कि राज्य ने किसी को लागू नहीं किया, न्यायालयों को उन्हें लागू कराना होगा।",
            "जब भी किसी क़ानून में उन्हें लागू करना असुविधाजनक हो, राज्य उन्हें किनारे कर सकता है।",
            "वे केवल राज्यों की सरकारों को बाँधते हैं, संघ की सरकार को नहीं।",
            "न्यायालय उन्हें लागू नहीं करा सकते, पर क़ानून बनाने में उन्हें लागू करना राज्य का कर्तव्य है।"],
   ans=3, pos=3)

# ------------------------------------------------------------------ P05 Moore's law (2)
p = passage("p05",
  "In 1965 the engineer Gordon Moore, who later co-founded the chipmaker Intel, observed that the number of components that could be put on a single chip had been doubling every year, and predicted that it would go on doing so; in 1975 he revised the pace to a doubling every two years. For decades the industry kept close to his forecast. "
  "Part of the reason is that it stopped being only a forecast. Chipmakers and their suppliers planned research, factories and products around it, each expecting the others to keep pace, so the prediction helped to bring about what it predicted. Some forecasts describe the world; others, once believed, become plans that shape it.",
  "1965 में इंजीनियर गॉर्डन मूर ने, जिन्होंने बाद में चिप निर्माता इंटेल की सह-स्थापना की, देखा कि एक चिप पर रखे जा सकने वाले घटकों की संख्या हर वर्ष दोगुनी होती आई थी, और भविष्यवाणी की कि ऐसा होता रहेगा; 1975 में उन्होंने गति को हर दो वर्ष में दोगुना कर दिया। दशकों तक उद्योग उनके पूर्वानुमान के क़रीब बना रहा। "
  "इसका एक कारण यह है कि वह केवल पूर्वानुमान नहीं रहा। चिप निर्माताओं और उनके आपूर्तिकर्ताओं ने अनुसंधान, कारख़ानों और उत्पादों की योजना उसके इर्द-गिर्द बनाई, हर एक यह आशा करते हुए कि बाक़ी साथ चलेंगे, इसलिए भविष्यवाणी ने वही लाने में सहायता की जिसकी उसने भविष्यवाणी की थी। कुछ पूर्वानुमान दुनिया का वर्णन करते हैं; दूसरे, एक बार विश्वास कर लिए जाने पर, ऐसी योजनाएँ बन जाते हैं जो उसे आकार देती हैं।")
RQ(p, "Main Idea", "medium", "mcq", MSG, MSG_HI,
   "The passage's point is that Moore's forecast held partly because the industry planned around it: a forecast that is believed can become a plan that helps to make itself come true. "
   "It does not say that every forecast fulfils itself, that Moore's forecast was a law of physics, or that the industry fell behind it.",
   "परिच्छेद की बात यह है कि मूर का पूर्वानुमान आंशिक रूप से इसलिए सही रहा कि उद्योग ने उसके इर्द-गिर्द योजना बनाई: जिस पूर्वानुमान पर विश्वास किया जाए वह ऐसी योजना बन सकता है जो उसे सच करने में सहायता करे। "
   "वह यह नहीं कहता कि हर पूर्वानुमान स्वयं को पूरा करता है, कि मूर का पूर्वानुमान भौतिकी का नियम था, या कि उद्योग उससे पीछे रह गया।",
   "message",
   opts=["Every forecast about technology comes true once enough people have heard of it.",
         "Moore's forecast held because it was a law of physics that no one could break.",
         "A forecast that people believe and plan around can help to bring itself about.",
         "The chip industry fell far behind Moore's forecast within a few years of 1975."],
   opts_hi=["तकनीक के बारे में हर पूर्वानुमान पर्याप्त लोगों के सुन लेने के बाद सच हो जाता है।",
            "मूर का पूर्वानुमान इसलिए सही रहा कि वह भौतिकी का ऐसा नियम था जिसे कोई नहीं तोड़ सकता था।",
            "जिस पूर्वानुमान पर लोग विश्वास कर योजना बनाएँ, वह स्वयं को सच करने में सहायक हो सकता है।",
            "1975 के कुछ ही वर्षों में चिप उद्योग मूर के पूर्वानुमान से बहुत पीछे रह गया।"],
   ans=2, pos=2)
RQ(p, "Inference", "hard", "mcq",
   "Which one of the following is most like the way, according to the passage, Moore's forecast came true?",
   "परिच्छेद के अनुसार मूर का पूर्वानुमान जिस तरह सच हुआ, निम्नलिखित में से कौन-सा उससे सबसे अधिक मिलता है?",
   "Moore's forecast came true partly because everyone involved planned on it and expected the others to keep pace. Rumours of a bank's failure that make depositors withdraw their money until the bank does fail work the same way: belief in the forecast brings it about. "
   "A tide table describes the moon's pull, which no one's belief affects; a weather forecast does not change the weather; and a doctor's prediction based on an X-ray describes a condition already present.",
   "मूर का पूर्वानुमान आंशिक रूप से इसलिए सच हुआ कि सभी संबंधित पक्षों ने उस पर योजना बनाई और बाक़ी से साथ चलने की आशा की। किसी बैंक के डूबने की अफ़वाहें, जो जमाकर्ताओं से पैसा तब तक निकलवाती हैं जब तक बैंक सचमुच डूब न जाए, इसी तरह काम करती हैं: पूर्वानुमान पर विश्वास उसे घटित कर देता है। "
   "ज्वार-तालिका चंद्रमा के खिंचाव का वर्णन करती है, जिस पर किसी के विश्वास का प्रभाव नहीं; मौसम का पूर्वानुमान मौसम नहीं बदलता; और एक्स-रे पर आधारित डॉक्टर की भविष्यवाणी पहले से मौजूद स्थिति का वर्णन करती है।",
   "a-forecast-that-comes-true-the-same-way",
   opts=["Rumours that a sound bank will fail make so many withdraw their money that it does fail.",
         "A tide table printed a year in advance correctly gives the times of high water at a port.",
         "A weather office's forecast of heavy rain for the next day turns out to be correct.",
         "A doctor who has seen an X-ray predicts that a broken bone will take six weeks to heal."],
   opts_hi=["ठीक बैंक के डूबने की अफ़वाहें इतने लोगों से पैसा निकलवाती हैं कि वह सचमुच डूब जाता है।",
            "एक वर्ष पहले छपी ज्वार-तालिका किसी बंदरगाह पर ऊँचे ज्वार के समय सही बताती है।",
            "मौसम कार्यालय का अगले दिन भारी वर्षा का पूर्वानुमान सही निकलता है।",
            "एक्स-रे देख चुका डॉक्टर भविष्यवाणी करता है कि टूटी हुई हड्डी को जुड़ने में छह सप्ताह लगेंगे।"],
   ans=0, pos=0)

# ------------------------------------------------------------------ P06 the paradox of water and diamonds
p = passage("p06",
  "Adam Smith noticed a puzzle in 1776. Nothing is more useful than water, yet it will buy scarcely anything; a diamond has hardly any use, yet a great quantity of other goods can be had in exchange for it. Economists of the following century found the answer in the difference between the value of a whole supply and the value of one more unit of it. "
  "Price is set at the margin -- by how much people care about the next litre or the next stone. Water is usually so plentiful that one more litre matters little, though the whole supply is beyond price; diamonds are so scarce that one more is greatly prized. The answer also explains why the puzzle can vanish: to a traveller lost in a desert, the next litre of water is worth more than any diamond. "
  "Price, then, measures what a thing is worth at the margin, not how much it matters overall.",
  "एडम स्मिथ ने 1776 में एक पहेली देखी। पानी से अधिक उपयोगी कुछ नहीं, फिर भी उससे शायद ही कुछ ख़रीदा जा सकता है; हीरे का लगभग कोई उपयोग नहीं, फिर भी उसके बदले बहुत-सी अन्य वस्तुएँ मिल सकती हैं। अगली शताब्दी के अर्थशास्त्रियों ने इसका उत्तर पूरी आपूर्ति के मूल्य और उसकी एक और इकाई के मूल्य के अंतर में पाया। "
  "मूल्य सीमांत पर तय होता है -- इससे कि लोग अगले लीटर या अगले पत्थर की कितनी परवाह करते हैं। पानी प्रायः इतना प्रचुर होता है कि एक और लीटर का कम महत्त्व है, यद्यपि पूरी आपूर्ति अमूल्य है; हीरे इतने दुर्लभ हैं कि एक और का बहुत मूल्य है। यह उत्तर यह भी समझाता है कि पहेली ग़ायब क्यों हो सकती है: रेगिस्तान में भटके यात्री के लिए पानी का अगला लीटर किसी भी हीरे से अधिक मूल्यवान है। "
  "अतः मूल्य यह मापता है कि कोई वस्तु सीमांत पर कितनी मूल्यवान है, यह नहीं कि वह कुल मिलाकर कितनी मायने रखती है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage resolves Smith's puzzle: price reflects the value of one more unit, which depends on scarcity, not the value of the whole supply. "
   "It says water matters more overall, so it does not call water less useful; it does not say prices are unrelated to use, only that they track use at the margin; and it shows the gap reversing in a desert, so diamonds are not always dearer.",
   "परिच्छेद स्मिथ की पहेली सुलझाता है: मूल्य एक और इकाई का मूल्य दर्शाता है, जो दुर्लभता पर निर्भर है, पूरी आपूर्ति का मूल्य नहीं। "
   "वह कहता है कि पानी कुल मिलाकर अधिक मायने रखता है, इसलिए वह पानी को कम उपयोगी नहीं कहता; वह यह नहीं कहता कि मूल्यों का उपयोग से कोई संबंध नहीं, केवल यह कि वे सीमांत पर उपयोग का अनुसरण करते हैं; और वह रेगिस्तान में अंतर को उलटता दिखाता है, इसलिए हीरे हमेशा महँगे नहीं।",
   "crux",
   opts=["Water is in truth less useful than diamonds, which is why the market prices it so much lower.",
         "Prices have nothing to do with how useful things are, and are set by fashion and custom alone.",
         "Diamonds will always be worth more than water, wherever and whenever they are exchanged.",
         "A thing's price reflects the value of one more unit of it, which depends on how scarce it is."],
   opts_hi=["पानी वास्तव में हीरों से कम उपयोगी है, इसीलिए बाज़ार उसका मूल्य इतना कम आँकता है।",
            "मूल्यों का वस्तुओं की उपयोगिता से कोई संबंध नहीं, और वे केवल फ़ैशन और रिवाज से तय होते हैं।",
            "हीरे हमेशा पानी से अधिक मूल्यवान रहेंगे, चाहे जहाँ और जब भी उनका विनिमय हो।",
            "किसी वस्तु का मूल्य उसकी एक और इकाई का मूल्य दर्शाता है, जो उसकी दुर्लभता पर निर्भर है।"],
   ans=3, pos=3)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Only 2 is valid. The passage says that what sets a price is how much people care about the next unit; if a drought made water scarce, the next litre would matter much more and its price would rise, even though water had become no more useful in total. "
   "1 misreads the passage: it says the whole supply of water is 'beyond price', so a low price does not show that water matters little to people overall.",
   "केवल 2 वैध है। परिच्छेद कहता है कि मूल्य इससे तय होता है कि लोग अगली इकाई की कितनी परवाह करते हैं; यदि सूखा पानी को दुर्लभ कर दे, तो अगला लीटर कहीं अधिक मायने रखेगा और उसका मूल्य बढ़ेगा, यद्यपि कुल मिलाकर पानी अधिक उपयोगी नहीं हुआ। "
   "1 परिच्छेद को ग़लत पढ़ता है: वह कहता है कि पानी की पूरी आपूर्ति 'अमूल्य' है, इसलिए कम मूल्य यह नहीं दिखाता कि पानी लोगों के लिए कुल मिलाकर कम मायने रखता है।",
   "conclusions",
   st=["The low price of water shows that, taken as a whole, water matters little to people.",
       "A drought that made water scarce could raise its price without making water any more useful in total."],
   st_hi=["पानी का कम मूल्य दिखाता है कि कुल मिलाकर पानी लोगों के लिए कम मायने रखता है।",
          "पानी को दुर्लभ करने वाला सूखा पानी को कुल मिलाकर अधिक उपयोगी बनाए बिना उसका मूल्य बढ़ा सकता है।"],
   key=1)
RQ(p, "Inference", "medium", "mcq",
   "Which one of the following best fits the passage's explanation of prices?",
   "निम्नलिखित में से कौन-सा मूल्यों की परिच्छेद की व्याख्या पर सबसे अच्छा बैठता है?",
   "On the passage's account a price rises when the next unit becomes scarcer. A bottle of water that costs far more at the top of a mountain, where every bottle must be carried up, fits that exactly: the next bottle is scarce there. "
   "A price set by law, a fall in the price of a gem that has gone out of fashion and an equal price for unequal goods are explained by other things -- rules, taste and custom -- that the passage does not discuss.",
   "परिच्छेद के अनुसार मूल्य तब बढ़ता है जब अगली इकाई अधिक दुर्लभ हो जाती है। पहाड़ की चोटी पर, जहाँ हर बोतल ऊपर ढोनी पड़ती है, कहीं महँगी बिकने वाली पानी की बोतल इस पर ठीक बैठती है: वहाँ अगली बोतल दुर्लभ है। "
   "क़ानून द्वारा तय मूल्य, फ़ैशन से बाहर हुए रत्न के मूल्य में गिरावट और असमान वस्तुओं का समान मूल्य अन्य बातों -- नियमों, रुचि और रिवाज -- से समझाए जाते हैं, जिनकी परिच्छेद चर्चा नहीं करता।",
   "what-fits-the-explanation-of-prices",
   opts=["A government fixes the price of bread by law and keeps it the same for many years.",
         "Bottled water costs far more on a mountain top, where each bottle must be carried up.",
         "A gem falls in price after it goes out of fashion among the people who buy jewellery.",
         "A shop charges the same price for a large loaf and a small one, out of long custom."],
   opts_hi=["सरकार क़ानून द्वारा रोटी का मूल्य तय करती है और उसे कई वर्षों तक एक-सा रखती है।",
            "पानी की एक बोतल पहाड़ की चोटी पर कहीं महँगी है, जहाँ हर बोतल ऊपर ढोनी पड़ती है।",
            "आभूषणों के ख़रीदारों में फ़ैशन से बाहर होने के बाद किसी रत्न का मूल्य गिर जाता है।",
            "एक दुकान पुराने रिवाज से बड़ी और छोटी डबलरोटी का एक ही मूल्य लेती है।"],
   ans=1, pos=1)

# ------------------------------------------------------------------ P07 eyes on the street
p = passage("p07",
  "In The Death and Life of Great American Cities, published in 1961, the writer Jane Jacobs argued that city streets are kept safe less by the police than by the people who use them: shopkeepers, residents at their windows and passers-by, the 'eyes on the street'. Such eyes, she said, need a mix of uses -- homes, shops, workplaces and places to eat side by side -- so that people are about at different hours of the day and night. "
  "Planners of her time often did the opposite, separating offices from homes and shops into zones of their own, and the streets of a zone emptied whenever its one use ended for the day. "
  "Her critics point out that she drew mostly on dense old neighbourhoods, and that a mix of uses cannot by itself make a street safe if the people on it do not care what happens there. Even so, her basic point -- that busy streets watch themselves -- has shaped city planning ever since.",
  "1961 में प्रकाशित 'द डेथ एंड लाइफ़ ऑफ़ ग्रेट अमेरिकन सिटीज़' में लेखिका जेन जेकब्स ने तर्क दिया कि शहर की सड़कें पुलिस से कम और उनका उपयोग करने वाले लोगों से अधिक सुरक्षित रहती हैं: दुकानदार, अपनी खिड़कियों पर निवासी और राहगीर, 'सड़क पर आँखें'। उन्होंने कहा कि ऐसी आँखों के लिए उपयोगों का मिश्रण चाहिए -- घर, दुकानें, कार्यस्थल और खाने की जगहें साथ-साथ -- ताकि दिन और रात के अलग-अलग समय पर लोग आसपास रहें। "
  "उनके समय के योजनाकार प्रायः उलटा करते थे, दफ़्तरों को घरों और दुकानों से अलग अपने-अपने क्षेत्रों में बाँटकर, और किसी क्षेत्र की सड़कें तब ख़ाली हो जातीं जब उसका एकमात्र उपयोग दिन भर के लिए समाप्त हो जाता। "
  "उनके आलोचक बताते हैं कि उन्होंने अधिकतर घनी पुरानी बस्तियों से उदाहरण लिए, और कि उपयोगों का मिश्रण अकेले किसी सड़क को सुरक्षित नहीं बना सकता यदि उस पर के लोगों को परवाह न हो कि वहाँ क्या होता है। फिर भी उनकी मूल बात -- कि भीड़-भरी सड़कें स्वयं अपनी निगरानी करती हैं -- ने तब से शहरी योजना को आकार दिया है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage presents Jacobs's claim that streets with a mix of uses stay safe because people are always about to watch them, notes its limits, and credits its lasting influence. "
   "It says safety comes less from the police than from people, not that police are useless; the critics say a mix is not enough by itself, not that it is harmful; and the planners' zoning is what Jacobs criticised, not what she recommended.",
   "परिच्छेद जेकब्स का यह दावा रखता है कि उपयोगों के मिश्रण वाली सड़कें इसलिए सुरक्षित रहती हैं कि उन पर नज़र रखने को लोग हमेशा आसपास होते हैं, उसकी सीमाएँ बताता है, और उसके स्थायी प्रभाव का श्रेय देता है। "
   "वह कहता है कि सुरक्षा पुलिस से कम और लोगों से अधिक आती है, यह नहीं कि पुलिस बेकार है; आलोचक कहते हैं कि मिश्रण अकेले पर्याप्त नहीं, यह नहीं कि वह हानिकारक है; और योजनाकारों का क्षेत्र-विभाजन वह है जिसकी जेकब्स ने आलोचना की, सलाह नहीं दी।",
   "crux",
   opts=["Streets with a mix of uses keep people about at all hours, and their watching makes them safer.",
         "Cities should do away with their police forces, since busy streets can always look after themselves.",
         "Mixing homes, shops and offices on the same street makes it more dangerous for those who live there.",
         "Planners were right to separate offices from homes and shops, so that each zone has a single use."],
   opts_hi=["मिश्रित उपयोग वाली सड़कें हर समय लोगों को आसपास रखती हैं, और उनकी निगरानी सड़कों को सुरक्षित बनाती है।",
            "शहरों को अपनी पुलिस समाप्त कर देनी चाहिए, क्योंकि भीड़-भरी सड़कें हमेशा अपनी देखभाल स्वयं कर सकती हैं।",
            "एक ही सड़क पर घर, दुकानें और दफ़्तर मिलाने से वह वहाँ रहने वालों के लिए अधिक ख़तरनाक हो जाती है।",
            "योजनाकारों का दफ़्तरों को घरों और दुकानों से अलग करना सही था, ताकि हर क्षेत्र का एक ही उपयोग हो।"],
   ans=0, pos=0)
RQ(p, "Inference", "hard", "mcq",
   "On Jacobs's reasoning, which one of the following streets is likely to be the least safe late in the evening?",
   "जेकब्स के तर्क के अनुसार, देर शाम को निम्नलिखित में से कौन-सी सड़क सबसे कम सुरक्षित होने की संभावना है?",
   "Jacobs's argument is that safety comes from people being about at different hours. A street of office towers with nothing else on it empties once the offices close, so in the evening it has no eyes at all. "
   "A street with homes above shops, one with a cinema and late cafes, and a market street with families living behind the stalls all keep people about after dark.",
   "जेकब्स का तर्क है कि सुरक्षा अलग-अलग समय पर लोगों के आसपास होने से आती है। केवल दफ़्तर भवनों वाली सड़क, जिस पर और कुछ नहीं, दफ़्तर बंद होते ही ख़ाली हो जाती है, इसलिए शाम को उस पर कोई आँखें नहीं होतीं। "
   "दुकानों के ऊपर घरों वाली सड़क, सिनेमा और देर तक खुले कैफ़े वाली सड़क, और दुकानों के पीछे रहने वाले परिवारों वाली बाज़ार की सड़क, सब अँधेरा होने के बाद भी लोगों को आसपास रखती हैं।",
   "the-least-safe-street-in-the-evening",
   opts=["A street of small shops with families living in the flats above them",
         "A street with a cinema, two late-night cafes and some homes nearby",
         "A street lined only with office towers that close at six in the evening",
         "A market street where the stallholders' families live behind their stalls"],
   opts_hi=["छोटी दुकानों वाली सड़क, जिनके ऊपर के फ़्लैटों में परिवार रहते हैं",
            "एक सिनेमा, देर रात तक खुले दो कैफ़े और पास में कुछ घरों वाली सड़क",
            "केवल ऐसे दफ़्तर भवनों वाली सड़क जो शाम छह बजे बंद हो जाते हैं",
            "बाज़ार की ऐसी सड़क जहाँ दुकानदारों के परिवार अपनी दुकानों के पीछे रहते हैं"],
   ans=2, pos=2)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Both are valid. The critics say a mix of uses cannot by itself make a street safe if the people on it do not care what happens there, so people's willingness to notice and act matters too (1). "
   "And the passage says that a zone's streets emptied whenever its one use ended for the day, so separating uses into zones could leave streets deserted for part of the day (2).",
   "दोनों वैध हैं। आलोचक कहते हैं कि उपयोगों का मिश्रण अकेले सड़क को सुरक्षित नहीं बना सकता यदि उस पर के लोगों को परवाह न हो कि वहाँ क्या होता है, इसलिए लोगों की ध्यान देने और कुछ करने की इच्छा भी मायने रखती है (1)। "
   "और परिच्छेद कहता है कि किसी क्षेत्र की सड़कें तब ख़ाली हो जातीं जब उसका एकमात्र उपयोग दिन भर के लिए समाप्त होता, इसलिए उपयोगों को क्षेत्रों में बाँटना दिन के कुछ भाग में सड़कों को सुनसान छोड़ सकता था (2)।",
   "conclusions",
   st=["For a street to be safe, the people on it must also care about what happens there.",
       "Separating uses into zones could leave streets deserted for part of each day."],
   st_hi=["किसी सड़क के सुरक्षित होने के लिए उस पर के लोगों को यह परवाह भी होनी चाहिए कि वहाँ क्या होता है।",
          "उपयोगों को क्षेत्रों में बाँटना हर दिन के कुछ भाग में सड़कों को सुनसान छोड़ सकता था।"],
   key=2)

# ------------------------------------------------------------------ P08 the salt-and-sugar drink
p = passage("p08",
  "Cholera and other diarrhoeal diseases kill mainly by draining the body of water and salts. For long the standard treatment was to replace them through a vein, which needs trained staff, sterile equipment and large stocks of fluid. In the 1960s researchers found that glucose helps the gut to absorb salt and water, so that a simple solution of salt and sugar in clean water, taken by mouth, could replace much of what was lost. "
  "In 1971, during the war that led to the birth of Bangladesh, the Indian doctor Dilip Mahalanabis used such a solution in refugee camps near the border, where fluid for drips was running out, and deaths among the cholera patients fell far below the usual rate. A few years later the medical journal The Lancet called the discovery potentially the most important medical advance of the century. "
  "The drink does not cure the infection; it keeps the patient alive while the body fights it. Its power lies in being cheap, simple and safe enough for a mother to give at home.",
  "हैज़ा और दस्त के अन्य रोग मुख्यतः शरीर से पानी और लवणों को निकालकर मारते हैं। लंबे समय तक सामान्य उपचार उन्हें नस के माध्यम से वापस देना था, जिसके लिए प्रशिक्षित कर्मचारी, कीटाणुरहित उपकरण और तरल के बड़े भंडार चाहिए। 1960 के दशक में शोधकर्ताओं ने पाया कि ग्लूकोज़ आँत को लवण और पानी सोखने में सहायता करता है, इसलिए साफ़ पानी में नमक और चीनी का एक साधारण घोल, मुँह से लिया जाकर, खोए हुए का बड़ा भाग वापस दे सकता है। "
  "1971 में, बांग्लादेश के जन्म तक ले जाने वाले युद्ध के दौरान, भारतीय डॉक्टर दिलीप महालनबीस ने सीमा के पास के शरणार्थी शिविरों में, जहाँ ड्रिप का तरल समाप्त हो रहा था, ऐसे घोल का उपयोग किया, और हैज़े के रोगियों में मौतें सामान्य दर से बहुत नीचे आ गईं। कुछ वर्ष बाद चिकित्सा पत्रिका 'द लैंसेट' ने इस खोज को संभवतः शताब्दी की सबसे महत्त्वपूर्ण चिकित्सा उपलब्धि कहा। "
  "यह पेय संक्रमण का इलाज नहीं करता; यह रोगी को तब तक जीवित रखता है जब तक शरीर संक्रमण से लड़ता है। इसकी शक्ति इसके सस्ते, सरल और इतना सुरक्षित होने में है कि एक माँ इसे घर पर दे सके।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage shows that a cheap drink of salt and sugar, which replaces lost water and salts while the body fights the infection, saved lives where drips could not reach -- its value lies in being simple and safe. "
   "It says the drink does not cure the infection; it does not say drips are useless, only that they need staff and supplies; and it does not credit any single discovery made in 1971.",
   "परिच्छेद दिखाता है कि नमक और चीनी का एक सस्ता पेय, जो शरीर के संक्रमण से लड़ते समय खोया पानी और लवण वापस देता है, उन जगहों पर जीवन बचाता था जहाँ ड्रिप नहीं पहुँच सकती थी -- उसका मूल्य उसके सरल और सुरक्षित होने में है। "
   "वह कहता है कि पेय संक्रमण का इलाज नहीं करता; वह यह नहीं कहता कि ड्रिप बेकार है, केवल यह कि उसके लिए कर्मचारी और सामग्री चाहिए; और वह 1971 में हुई किसी एक खोज को श्रेय नहीं देता।",
   "crux",
   opts=["The salt-and-sugar drink cures cholera by killing the germs that cause the disease.",
         "Treatment through a vein is useless and should no longer be given to any cholera patient.",
         "Dilip Mahalanabis discovered in 1971 that glucose helps the gut to absorb salt and water.",
         "A cheap drink that keeps patients alive can save lives where elaborate care is lacking."],
   opts_hi=["नमक-चीनी का पेय रोग पैदा करने वाले कीटाणुओं को मारकर हैज़े का इलाज करता है।",
            "नस के माध्यम से उपचार बेकार है और अब किसी भी हैज़ा रोगी को नहीं दिया जाना चाहिए।",
            "दिलीप महालनबीस ने 1971 में खोजा कि ग्लूकोज़ आँत को लवण और पानी सोखने में सहायता करता है।",
            "रोगियों को जीवित रखने वाला सस्ता पेय वहाँ जीवन बचा सकता है जहाँ विस्तृत देखभाल न हो।"],
   ans=3, pos=3)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Only 2 is valid. The drink works by replacing water and salts while the body fights the infection, so it would save a patient only if the patient could be kept alive long enough for the body to win; it is not a remedy for the germ itself. "
   "1 misreads the history: the passage says researchers found the effect of glucose in the 1960s; Mahalanabis used the solution in 1971 -- he did not discover it.",
   "केवल 2 वैध है। पेय शरीर के संक्रमण से लड़ते समय पानी और लवण वापस देकर काम करता है, इसलिए वह रोगी को तभी बचाएगा जब रोगी को इतने समय तक जीवित रखा जा सके कि शरीर जीत जाए; वह स्वयं कीटाणु का उपचार नहीं है। "
   "1 इतिहास को ग़लत पढ़ता है: परिच्छेद कहता है कि शोधकर्ताओं ने ग्लूकोज़ का प्रभाव 1960 के दशक में पाया; महालनबीस ने 1971 में घोल का उपयोग किया -- उन्होंने उसकी खोज नहीं की।",
   "conclusions",
   st=["The effect of glucose on the gut was first discovered in the refugee camps of 1971.",
       "The drink saves a patient by buying time for the body to fight off the infection, not by attacking the germ."],
   st_hi=["आँत पर ग्लूकोज़ का प्रभाव पहली बार 1971 के शरणार्थी शिविरों में खोजा गया।",
          "पेय रोगी को कीटाणु पर हमला करके नहीं, बल्कि शरीर को संक्रमण से लड़ने का समय देकर बचाता है।"],
   key=1)
RQ(p, "Inference", "medium", "mcq",
   "Why, according to the passage, did the drink work so well in the refugee camps of 1971?",
   "परिच्छेद के अनुसार, 1971 के शरणार्थी शिविरों में पेय ने इतना अच्छा काम क्यों किया?",
   "The camps were running out of fluid for drips, which also need trained staff and sterile equipment; a drink of salt and sugar needed none of these and could be given to many patients at once. "
   "The passage does not say the camps had more doctors, that the cholera there was milder, or that the drink killed the germs.",
   "शिविरों में ड्रिप का तरल समाप्त हो रहा था, जिसके लिए प्रशिक्षित कर्मचारी और कीटाणुरहित उपकरण भी चाहिए; नमक और चीनी के पेय को इनमें से किसी की आवश्यकता नहीं थी और उसे एक साथ कई रोगियों को दिया जा सकता था। "
   "परिच्छेद यह नहीं कहता कि शिविरों में अधिक डॉक्टर थे, कि वहाँ हैज़ा हल्का था, या कि पेय कीटाणुओं को मारता था।",
   "why-the-drink-worked-in-the-camps",
   opts=["The camps had far more doctors and nurses than the hospitals of the region.",
         "It needed no drips, sterile equipment or trained staff, which the camps lacked.",
         "The cholera that broke out in the camps was a much milder form of the disease.",
         "It killed the germs in the water that the refugees in the camps had been drinking."],
   opts_hi=["शिविरों में उस क्षेत्र के सभी अस्पतालों को मिलाकर भी उनसे कहीं अधिक डॉक्टर और नर्सें थीं।",
            "उसे ड्रिप, कीटाणुरहित उपकरण या प्रशिक्षित कर्मचारी नहीं चाहिए थे, जो शिविरों में कम थे।",
            "शिविरों में फैला हैज़ा रोग का कहीं अधिक हल्का रूप था।",
            "उसने उस पानी के कीटाणु मार दिए जो शिविरों के शरणार्थी पी रहे थे।"],
   ans=1, pos=1)

# ------------------------------------------------------------------ P09 Blackstone's ratio
p = passage("p09",
  "In the 1760s the English jurist William Blackstone wrote that it is better for ten guilty persons to escape than for one innocent person to suffer. The maxim is really a judgement about mistakes. Every system of trial makes two kinds of error -- convicting the innocent and acquitting the guilty -- and the rules of evidence that make one rarer tend to make the other more common. "
  "Demanding proof beyond reasonable doubt is a choice to accept more wrongful acquittals in order to have fewer wrongful convictions. Blackstone's ten is not a figure found by measurement; it states which error a society fears more and by how much. Others have named different numbers, and a society that lowered the standard of proof would be choosing, whether it said so or not, a different ratio.",
  "1760 के दशक में अंग्रेज़ विधिवेत्ता विलियम ब्लैकस्टोन ने लिखा कि दस अपराधियों का बच निकलना एक निर्दोष के कष्ट पाने से बेहतर है। यह सूक्ति वास्तव में भूलों के बारे में एक निर्णय है। हर मुक़दमा-व्यवस्था दो प्रकार की भूल करती है -- निर्दोष को दोषी ठहराना और दोषी को बरी करना -- और साक्ष्य के जो नियम एक को कम करते हैं वे प्रायः दूसरे को बढ़ाते हैं। "
  "उचित संदेह से परे प्रमाण माँगना कम ग़लत दोषसिद्धियों के लिए अधिक ग़लत बरियों को स्वीकार करने का चुनाव है। ब्लैकस्टोन का दस कोई मापकर निकाला गया आँकड़ा नहीं; वह बताता है कि कोई समाज किस भूल से अधिक डरता है और कितना। दूसरों ने अलग संख्याएँ बताई हैं, और जो समाज प्रमाण का मानक घटाए वह, कहे या न कहे, एक अलग अनुपात चुन रहा होगा।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage reads Blackstone's maxim as a choice between two kinds of error, which trade off against each other: the standard of proof expresses how much more a society fears convicting the innocent. "
   "It calls the ten a judgement, not a measured fact; it says lowering the standard changes the ratio, not that it removes errors; and it does not say that guilty people rarely escape.",
   "परिच्छेद ब्लैकस्टोन की सूक्ति को दो प्रकार की भूलों के बीच एक चुनाव के रूप में पढ़ता है, जो एक-दूसरे के बदले घटती-बढ़ती हैं: प्रमाण का मानक बताता है कि कोई समाज निर्दोष को दोषी ठहराने से कितना अधिक डरता है। "
   "वह दस को एक निर्णय कहता है, मापा गया तथ्य नहीं; वह कहता है कि मानक घटाने से अनुपात बदलता है, यह नहीं कि भूलें मिट जाती हैं; और वह यह नहीं कहता कि अपराधी शायद ही बचते हैं।",
   "crux",
   opts=["Blackstone measured that exactly ten guilty people go free for every innocent one convicted.",
         "Lowering the standard of proof would remove both kinds of error from a system of trial.",
         "A standard of proof is a choice about which of two unavoidable errors a society fears more.",
         "Under proof beyond reasonable doubt, guilty people almost never escape conviction."],
   opts_hi=["ब्लैकस्टोन ने मापा कि दोषी ठहराए गए हर निर्दोष के बदले ठीक दस अपराधी छूट जाते हैं।",
            "प्रमाण का मानक घटाने से मुक़दमा-व्यवस्था से दोनों प्रकार की भूलें मिट जाएँगी।",
            "प्रमाण का मानक यह चुनाव है कि समाज दो अपरिहार्य भूलों में से किससे अधिक डरता है।",
            "उचित संदेह से परे प्रमाण के अंतर्गत अपराधी लगभग कभी दोषसिद्धि से नहीं बचते।"],
   ans=2, pos=2)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Neither is valid. 1 goes beyond the passage: it says the rules that make one error rarer tend to make the other more common, not that a perfect system with neither error could be designed -- if anything, it implies the opposite. "
   "2 also goes too far: the passage says a society that lowered the standard of proof would be choosing a different ratio, not that it would therefore convict more guilty people without convicting any more innocent ones.",
   "कोई भी वैध नहीं। 1 परिच्छेद से आगे जाता है: वह कहता है कि जो नियम एक भूल को कम करते हैं वे प्रायः दूसरी को बढ़ाते हैं, यह नहीं कि बिना किसी भूल वाली पूर्ण व्यवस्था बनाई जा सकती है -- बल्कि वह उलटा संकेत करता है। "
   "2 भी बहुत आगे जाता है: परिच्छेद कहता है कि प्रमाण का मानक घटाने वाला समाज एक अलग अनुपात चुन रहा होगा, यह नहीं कि वह इसलिए अधिक निर्दोषों को दोषी ठहराए बिना अधिक अपराधियों को दोषी ठहराएगा।",
   "conclusions",
   st=["With careful enough rules of evidence, a system of trial could avoid both kinds of error.",
       "Lowering the standard of proof would convict more of the guilty without convicting any more of the innocent."],
   st_hi=["पर्याप्त सावधान साक्ष्य-नियमों से कोई मुक़दमा-व्यवस्था दोनों प्रकार की भूलों से बच सकती है।",
          "प्रमाण का मानक घटाने से अधिक निर्दोषों को दोषी ठहराए बिना अधिक अपराधी दोषी ठहराए जाएँगे।"],
   key=3)
RQ(p, "Inference", "hard", "mcq",
   "A society moves from Blackstone's ten to a ratio of a hundred guilty escaping for every innocent person convicted. According to the passage's reasoning, what would that change most likely involve?",
   "एक समाज ब्लैकस्टोन के दस से ऐसे अनुपात पर जाता है जिसमें दोषी ठहराए गए हर निर्दोष के बदले सौ अपराधी छूटें। परिच्छेद के तर्क के अनुसार, इस बदलाव में सबसे अधिक संभावना किसकी है?",
   "A higher ratio means fearing wrongful conviction even more, which calls for a still stricter standard of proof -- and, because the two errors trade off, more of the guilty going free. "
   "A lower standard of proof would move the ratio the other way; fewer acquittals of the guilty is the opposite of what a stricter standard brings; and nothing in the passage ties the ratio to the number of judges.",
   "ऊँचे अनुपात का अर्थ है ग़लत दोषसिद्धि से और भी अधिक डरना, जिसके लिए प्रमाण का और कड़ा मानक चाहिए -- और, चूँकि दोनों भूलें एक-दूसरे के बदले घटती-बढ़ती हैं, अधिक अपराधियों का छूटना। "
   "प्रमाण का निचला मानक अनुपात को उलटी ओर ले जाएगा; अपराधियों की कम बरियाँ वह नहीं जो कड़ा मानक लाता है; और परिच्छेद में कुछ भी अनुपात को न्यायाधीशों की संख्या से नहीं जोड़ता।",
   "what-a-higher-ratio-involves",
   opts=["A stricter standard of proof, with more of the guilty going free",
         "A lower standard of proof, so that fewer of the guilty go free",
         "Fewer acquittals of the guilty, with no other change to the trials",
         "Many more judges, so that every case can be heard more quickly"],
   opts_hi=["प्रमाण का अधिक कड़ा मानक, जिसमें अधिक अपराधी छूटें",
            "प्रमाण का निचला मानक, ताकि कम अपराधी छूटें",
            "अपराधियों की कम बरियाँ, मुक़दमों में कोई और बदलाव किए बिना",
            "कहीं अधिक न्यायाधीश, ताकि हर मामले की सुनवाई जल्दी हो सके"],
   ans=0, pos=0)

# ------------------------------------------------------------------ P10 lichens as a gauge of clean air
p = passage("p10",
  "Lichens -- partnerships of a fungus with an alga -- grow as crusts and tufts on bark and stone. They have no roots, and they take most of their water and nourishment straight from rain and the air. Lacking the protective outer layer of a leaf, they absorb whatever the air carries, and many kinds are harmed by sulphur dioxide, a gas given off when coal and oil are burnt. "
  "That makes them useful as indicators of pollution: where the air is heavy with sulphur dioxide, sensitive lichens die out, and in some cities they have returned to the trees only as the air has been cleaned. "
  "Lichens are a cheap gauge that anyone can read. But they are a rough one. Their absence says that something is wrong with the air without saying exactly what or how much, and a lichen may also be missing for reasons that have nothing to do with pollution, such as dry weather or the wrong kind of bark.",
  "लाइकेन -- किसी कवक और शैवाल की साझेदारियाँ -- छाल और पत्थर पर पपड़ी और गुच्छों के रूप में उगते हैं। उनकी जड़ें नहीं होतीं, और वे अपना अधिकांश पानी और पोषण सीधे वर्षा और वायु से लेते हैं। पत्ती जैसी सुरक्षात्मक बाहरी परत न होने के कारण वे वायु में जो कुछ भी हो उसे सोख लेते हैं, और कई प्रकार सल्फ़र डाइऑक्साइड से हानि पाते हैं, जो कोयला और तेल जलाने पर निकलने वाली गैस है। "
  "इससे वे प्रदूषण के सूचक के रूप में उपयोगी होते हैं: जहाँ वायु में सल्फ़र डाइऑक्साइड अधिक है, संवेदनशील लाइकेन समाप्त हो जाते हैं, और कुछ शहरों में वे पेड़ों पर तभी लौटे जब वायु साफ़ की गई। "
  "लाइकेन एक सस्ता मापक हैं जिसे कोई भी पढ़ सकता है। पर वे एक मोटा मापक हैं। उनकी अनुपस्थिति बताती है कि वायु में कुछ गड़बड़ है, यह बताए बिना कि ठीक-ठीक क्या या कितना, और कोई लाइकेन ऐसे कारणों से भी अनुपस्थित हो सकता है जिनका प्रदूषण से कोई संबंध नहीं, जैसे सूखा मौसम या ग़लत प्रकार की छाल।")
RQ(p, "Specific Detail", "easy", "mcq",
   "According to the passage, why are lichens so easily harmed by what the air carries?",
   "परिच्छेद के अनुसार, लाइकेन वायु में मौजूद चीज़ों से इतनी आसानी से हानि क्यों पाते हैं?",
   "The passage says lichens take their water and nourishment straight from rain and air and, lacking a leaf's protective outer layer, absorb whatever the air carries. "
   "It does not say they grow only in cities, that they need sulphur dioxide, or that their roots draw pollution from the soil -- they have no roots.",
   "परिच्छेद कहता है कि लाइकेन अपना पानी और पोषण सीधे वर्षा और वायु से लेते हैं और, पत्ती की सुरक्षात्मक बाहरी परत न होने से, वायु में जो कुछ भी हो उसे सोख लेते हैं। "
   "वह यह नहीं कहता कि वे केवल शहरों में उगते हैं, कि उन्हें सल्फ़र डाइऑक्साइड चाहिए, या कि उनकी जड़ें मिट्टी से प्रदूषण खींचती हैं -- उनकी जड़ें नहीं होतीं।",
   "why-lichens-are-easily-harmed",
   opts=["Their roots draw polluted water up from the soil into the rest of the plant.",
         "They take in water and food straight from the air, with no protective outer layer.",
         "They grow only in cities, where the air is always heavy with smoke and gases.",
         "They need sulphur dioxide to grow, and are harmed when the air has too much of it."],
   opts_hi=["उनकी जड़ें मिट्टी से प्रदूषित पानी पौधे के बाक़ी भाग तक खींचती हैं।",
            "वे पानी और भोजन सीधे वायु से लेते हैं, किसी सुरक्षात्मक बाहरी परत के बिना।",
            "वे केवल शहरों में उगते हैं, जहाँ वायु हमेशा धुएँ और गैसों से भरी रहती है।",
            "उन्हें उगने के लिए सल्फ़र डाइऑक्साइड चाहिए, और वायु में उसके बहुत अधिक होने पर वे हानि पाते हैं।"],
   ans=1, pos=1)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Only 1 is valid. The passage says lichens returned to the trees of some cities only as the air was cleaned, so their return is a sign that sulphur dioxide has fallen. "
   "2 goes too far: the passage warns that a lichen may be missing for reasons that have nothing to do with pollution, such as dry weather or the wrong bark, so a single tree without lichens proves nothing on its own.",
   "केवल 1 वैध है। परिच्छेद कहता है कि कुछ शहरों के पेड़ों पर लाइकेन तभी लौटे जब वायु साफ़ की गई, इसलिए उनकी वापसी इस बात का संकेत है कि सल्फ़र डाइऑक्साइड घटी है। "
   "2 बहुत आगे जाता है: परिच्छेद चेताता है कि कोई लाइकेन ऐसे कारणों से भी अनुपस्थित हो सकता है जिनका प्रदूषण से कोई संबंध नहीं, जैसे सूखा मौसम या ग़लत छाल, इसलिए लाइकेन रहित एक पेड़ अकेले कुछ सिद्ध नहीं करता।",
   "conclusions",
   st=["The return of sensitive lichens to a city's trees is a sign that its air has become cleaner.",
       "A single tree without lichens proves that the air around it is polluted with sulphur dioxide."],
   st_hi=["किसी शहर के पेड़ों पर संवेदनशील लाइकेनों की वापसी इस बात का संकेत है कि उसकी वायु साफ़ हुई है।",
          "लाइकेन रहित एक पेड़ सिद्ध करता है कि उसके आसपास की वायु सल्फ़र डाइऑक्साइड से प्रदूषित है।"],
   key=0)
RQ(p, "Inference", "hard", "mcq",
   "A town wants to know whether a new power station has changed its air. Which one of the following uses lichens in the way the passage suggests?",
   "एक नगर जानना चाहता है कि एक नए बिजलीघर ने उसकी वायु को बदला है या नहीं। निम्नलिखित में से कौन-सा लाइकेनों का उस तरह उपयोग करता है जैसा परिच्छेद सुझाता है?",
   "Lichens are a cheap but rough gauge, and their absence can have other causes. Comparing the same trees, of the same kind, before and after the station opened -- and then measuring the air directly if the lichens decline -- uses them as an early warning while guarding against the other causes. "
   "Counting lichens on one dry wall mixes in the effect of dry weather; reading the exact amount of gas from them asks more than they can tell; and ignoring them because they are cheap throws away a useful signal.",
   "लाइकेन सस्ते पर मोटे मापक हैं, और उनकी अनुपस्थिति के अन्य कारण हो सकते हैं। बिजलीघर खुलने से पहले और बाद में उसी प्रकार के उन्हीं पेड़ों की तुलना करना -- और लाइकेन घटें तो वायु को सीधे मापना -- उन्हें अन्य कारणों से बचाव करते हुए पूर्व चेतावनी के रूप में उपयोग करता है। "
   "एक सूखी दीवार पर लाइकेन गिनना सूखे मौसम का प्रभाव मिला देता है; उनसे गैस की ठीक मात्रा पढ़ना उनसे अधिक माँगना है जितना वे बता सकते हैं; और सस्ते होने के कारण उन्हें अनदेखा करना एक उपयोगी संकेत फेंक देना है।",
   "using-lichens-to-watch-a-power-station",
   opts=["Count the lichens on a single dry wall near the station, once, after it opens",
         "Use the number of lichens on a tree to state exactly how much gas is in the air",
         "Ignore the lichens, since anything so cheap to observe cannot tell anything useful",
         "Compare the same trees' lichens before and after, and test the air if they decline"],
   opts_hi=["बिजलीघर खुलने के बाद एक बार उसके पास की एक सूखी दीवार पर लाइकेन गिनना",
            "किसी पेड़ पर लाइकेनों की संख्या से यह बताना कि वायु में ठीक कितनी गैस है",
            "लाइकेनों को अनदेखा करना, क्योंकि इतनी सस्ती देखी जाने वाली चीज़ कुछ उपयोगी नहीं बता सकती",
            "उन्हीं पेड़ों पर पहले और बाद के लाइकेनों की तुलना करना, और घटें तो वायु मापना"],
   ans=3, pos=3)
