# -*- coding: utf-8 -*-
"""CSAT Level 4 · Simulator 8 -- Reading Comprehension: 10 passages, 29 items (9 x 3 and the 5th passage x 2), Layout B.

The 2025 shape. Each passage turns -- a claim, then its limit. Themes, none used in Levels 1-3 or Simulators 1-7: the
Hawthorne studies, Hotelling's two sellers on a beach, James Lind's scurvy trial, Article 21 from Gopalan to Maneka
Gandhi, the paradox of the heap, a prophecy that failed, Dadabhai Naoroji and the drain of wealth, the olive ridleys of
Odisha, Eratosthenes measuring the Earth, and the Dutch disease. Item types: main idea 10, inference 16, specific detail
3. Two-statement keys 2 / 3 / 1 / 2 (1 only / 2 only / Both / Neither). Difficulty 1 easy / 17 medium / 11 hard.
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

# ------------------------------------------------------------------ P01 the Hawthorne studies
p = passage("p01",
  "Between 1924 and 1927, engineers at the Hawthorne Works, a factory of the Western Electric Company near Chicago, tried to find out how lighting affected the output of workers. They raised the light for one group and kept it steady for a comparison group. Output rose in both. When the light was later lowered for the test group, output held up until the workers could barely see. Studies in a separate test room at the same factory, which changed rest breaks and working hours, found output rising with almost every change. "
  "Decades afterwards the term 'Hawthorne effect' was coined for the idea that people change their behaviour simply because they know they are being studied, and the lesson usually drawn is that a study needs a comparison group that receives the same attention but not the treatment. Yet scholars who went back to the records found the original results weaker than the legend suggests. In the best-known test room, for instance, the workers were paid according to the output of their small group, and two of the five were replaced partway through.",
  "1924 से 1927 के बीच शिकागो के पास वेस्टर्न इलेक्ट्रिक कंपनी के एक कारख़ाने, हॉथॉर्न वर्क्स, में इंजीनियरों ने यह जानने का प्रयास किया कि रोशनी श्रमिकों के उत्पादन को कैसे प्रभावित करती है। उन्होंने एक समूह के लिए रोशनी बढ़ाई और एक तुलना-समूह के लिए उसे स्थिर रखा। दोनों में उत्पादन बढ़ा। जब बाद में परीक्षण-समूह की रोशनी घटाई गई, तो उत्पादन तब तक बना रहा जब तक श्रमिक मुश्किल से देख पाने लगे। उसी कारख़ाने के एक अलग परीक्षण-कक्ष के अध्ययनों में, जिनमें विश्राम के अंतराल और काम के घंटे बदले गए, लगभग हर बदलाव के साथ उत्पादन बढ़ता पाया गया। "
  "दशकों बाद इस विचार के लिए 'हॉथॉर्न प्रभाव' शब्द गढ़ा गया कि लोग केवल यह जानकर अपना व्यवहार बदल लेते हैं कि उनका अध्ययन हो रहा है, और इससे प्रायः यह सीख निकाली जाती है कि अध्ययन में ऐसा तुलना-समूह होना चाहिए जिसे उतना ही ध्यान मिले पर उपचार नहीं। फिर भी जिन विद्वानों ने अभिलेखों को दोबारा देखा, उन्होंने मूल परिणामों को किंवदंती से कमज़ोर पाया। उदाहरण के लिए, सबसे प्रसिद्ध परीक्षण-कक्ष में श्रमिकों को उनके छोटे समूह के उत्पादन के अनुसार भुगतान मिलता था, और पाँच में से दो को बीच में बदल दिया गया था।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage tells how the Hawthorne studies gave rise to a famous lesson about the effect of being studied, then shows that the records behind it are weaker than the legend. "
   "It reports that output rose even when the light was lowered, so better lighting is not its point; it says studies need comparison groups, not that studies of workers are worthless; and pay is mentioned as one thing that clouds the results, not as the main cause of output.",
   "परिच्छेद बताता है कि हॉथॉर्न अध्ययनों से अध्ययन किए जाने के प्रभाव के बारे में एक प्रसिद्ध सीख कैसे निकली, फिर दिखाता है कि उसके पीछे के अभिलेख किंवदंती से कमज़ोर हैं। "
   "वह बताता है कि रोशनी घटाने पर भी उत्पादन बढ़ा, इसलिए बेहतर रोशनी उसकी बात नहीं; वह कहता है कि अध्ययनों में तुलना-समूह चाहिए, यह नहीं कि श्रमिकों के अध्ययन बेकार हैं; और भुगतान का उल्लेख परिणामों को धुँधला करने वाली एक बात के रूप में है, उत्पादन के मुख्य कारण के रूप में नहीं।",
   "crux",
   opts=["A famous lesson about the effect of being studied rests on evidence weaker than its fame suggests.",
         "Better lighting in a factory raises the output of its workers, whatever else changes at the same time.",
         "Studies of workers are of no value, since people always behave differently when they are watched.",
         "How workers are paid matters more than lighting or rest breaks in deciding how much they produce."],
   opts_hi=["अध्ययन किए जाने के प्रभाव की प्रसिद्ध सीख उतने मज़बूत प्रमाण पर नहीं टिकी जितनी प्रसिद्ध है।",
            "कारख़ाने में बेहतर रोशनी श्रमिकों का उत्पादन बढ़ाती है, उसी समय और कुछ भी बदले।",
            "श्रमिकों के अध्ययनों का कोई मूल्य नहीं, क्योंकि देखे जाने पर लोग सदा अलग व्यवहार करते हैं।",
            "श्रमिक कितना उत्पादन करते हैं, यह तय करने में रोशनी या विश्राम से अधिक महत्त्व भुगतान के ढंग का है।"],
   ans=0, pos=3)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Only 1 is valid. The comparison group's lighting did not change, yet its output rose too, so the lighting cannot explain the rise and something else -- attention, pay, the changes in staff -- was at work. "
   "2 goes too far: the scholars found the original results weaker than the legend, not proof that being studied has no effect at all.",
   "केवल 1 वैध है। तुलना-समूह की रोशनी नहीं बदली, फिर भी उसका उत्पादन भी बढ़ा, इसलिए रोशनी उस बढ़त की व्याख्या नहीं कर सकती और कुछ और -- ध्यान, भुगतान, कर्मियों में बदलाव -- काम कर रहा था। "
   "2 बहुत आगे चला जाता है: विद्वानों ने मूल परिणामों को किंवदंती से कमज़ोर पाया, यह प्रमाण नहीं कि अध्ययन किए जाने का कोई प्रभाव होता ही नहीं।",
   "conclusions",
   st=["That output rose in the comparison group as well suggests that something other than the lighting was at work.",
       "The later look at the records showed that being studied has no effect on how people behave."],
   st_hi=["तुलना-समूह में भी उत्पादन बढ़ना संकेत देता है कि रोशनी के अलावा कुछ और काम कर रहा था।",
          "अभिलेखों की बाद की जाँच ने दिखाया कि अध्ययन किए जाने का लोगों के व्यवहार पर कोई प्रभाव नहीं पड़ता।"],
   key=0)
RQ(p, "Specific Detail", "medium", "mcq",
   "According to the passage, which of the following clouds the results of the best-known test room?",
   "परिच्छेद के अनुसार, निम्नलिखित में से कौन-सी बात सबसे प्रसिद्ध परीक्षण-कक्ष के परिणामों को धुँधला करती है?",
   "The passage names two things: the workers were paid by their small group's output, and two of the five were replaced partway through -- either could have changed output on its own. "
   "It does not say the lighting there was too dim to measure output, that the room had no comparison at all, or that the workers did not know they were being studied.",
   "परिच्छेद दो बातें बताता है: श्रमिकों को उनके छोटे समूह के उत्पादन से भुगतान मिलता था, और पाँच में से दो बीच में बदले गए -- इनमें से कोई भी अपने आप उत्पादन बदल सकती थी। "
   "वह यह नहीं कहता कि वहाँ रोशनी उत्पादन मापने के लिए बहुत मंद थी, कि कक्ष में कोई तुलना थी ही नहीं, या कि श्रमिकों को अध्ययन का पता नहीं था।",
   "what-clouds-the-best-known-test-room",
   opts=["Its workers were paid by their group's output, and two of them were replaced.",
         "Its lighting was kept so dim that the workers' output could not be measured.",
         "It was run without any group or period against which to compare its output.",
         "Its workers were never told that their output was being recorded and studied."],
   opts_hi=["उसके श्रमिकों को समूह के उत्पादन से भुगतान मिलता था, और उनमें से दो बदले गए।",
            "उसकी रोशनी इतनी मंद रखी गई कि श्रमिकों का उत्पादन मापा ही नहीं जा सका।",
            "वह बिना किसी ऐसे समूह या अवधि के चला जिससे उसके उत्पादन की तुलना की जा सके।",
            "उसके श्रमिकों को कभी नहीं बताया गया कि उनका उत्पादन दर्ज और अध्ययन किया जा रहा है।"],
   ans=0, pos=1)

# ------------------------------------------------------------------ P02 Hotelling's two sellers on a beach
p = passage("p02",
  "In 1929 the economist Harold Hotelling asked why competing sellers so often end up side by side. Picture a straight beach with bathers spread evenly along it and two ice-cream sellers, each free to set up anywhere. Bathers walk to the nearer seller. If the sellers stood at the quarter-points, each would serve half the beach and no bather would walk more than a quarter of its length. But either seller can win customers by edging towards the middle, taking bathers from the rival's side while keeping all of their own. So both drift to the centre and end up back to back, still sharing the beach equally, while bathers at the ends now walk twice as far. "
  "Economists later used the same reasoning for elections: two parties competing for votes may move towards the middle of opinion until their programmes look alike. The result depends on its assumptions, however. If bathers far from both sellers would rather go without than walk, or if a third seller arrives, the pull to the centre weakens or breaks down.",
  "1929 में अर्थशास्त्री हैरल्ड होटेलिंग ने पूछा कि प्रतिस्पर्धी विक्रेता इतनी बार अगल-बग़ल क्यों आ जाते हैं। एक सीधे समुद्र-तट की कल्पना करें जिस पर स्नान करने वाले समान रूप से फैले हैं, और आइसक्रीम के दो विक्रेता, जिनमें से हर एक कहीं भी दुकान लगा सकता है। स्नान करने वाले निकट वाले विक्रेता तक चलकर जाते हैं। यदि विक्रेता चौथाई-बिंदुओं पर खड़े हों, तो हर एक आधे तट को सेवा देगा और किसी को तट की लंबाई के चौथाई से अधिक नहीं चलना पड़ेगा। पर कोई भी विक्रेता बीच की ओर खिसककर ग्राहक जीत सकता है -- प्रतिद्वंद्वी की ओर के स्नान करने वालों को लेते हुए और अपने सभी को रखते हुए। इसलिए दोनों केंद्र की ओर खिसकते हैं और पीठ से पीठ सटाकर खड़े हो जाते हैं, अब भी तट को बराबर बाँटते हुए, जबकि छोरों पर के लोगों को अब दोगुना चलना पड़ता है। "
  "अर्थशास्त्रियों ने बाद में यही तर्क चुनावों पर लगाया: वोटों के लिए प्रतिस्पर्धा करते दो दल विचारों के मध्य की ओर तब तक खिसक सकते हैं जब तक उनके कार्यक्रम एक जैसे न दिखने लगें। पर यह परिणाम अपनी मान्यताओं पर निर्भर है। यदि दोनों विक्रेताओं से दूर के लोग चलने के बजाय बिना आइसक्रीम रहना पसंद करें, या कोई तीसरा विक्रेता आ जाए, तो केंद्र का खिंचाव कमज़ोर पड़ जाता है या टूट जाता है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage explains how competition for the same customers can pull two rivals to the same middle spot, applies this to elections, and ends by noting that the result rests on its assumptions. "
   "It says nothing about prices; it says parties 'may' move to the middle, not that all parties in every democracy end up identical; and it says bathers are served worse, not best, when the sellers stand at the middle.",
   "परिच्छेद समझाता है कि एक ही ग्राहकों के लिए प्रतिस्पर्धा दो प्रतिद्वंद्वियों को एक ही मध्य स्थान पर कैसे खींच सकती है, इसे चुनावों पर लगाता है, और यह कहकर समाप्त होता है कि परिणाम अपनी मान्यताओं पर टिका है। "
   "वह मूल्यों के बारे में कुछ नहीं कहता; वह कहता है कि दल मध्य की ओर 'खिसक सकते हैं', यह नहीं कि हर लोकतंत्र के सभी दल एक जैसे हो जाते हैं; और वह कहता है कि विक्रेताओं के मध्य में खड़े होने पर लोगों को ख़राब, न कि सबसे अच्छी, सेवा मिलती है।",
   "crux",
   opts=["Competition may pull rivals to the same middle spot, though this rests on certain assumptions.",
         "Sellers who stand side by side always charge higher prices than sellers who stand far apart.",
         "Political parties in every democracy end up offering exactly the same programmes to all their voters.",
         "Bathers on a beach are served best when both ice-cream sellers stand at its very middle."],
   opts_hi=["प्रतिस्पर्धा प्रतिद्वंद्वियों को एक ही मध्य स्थान पर खींच सकती है, पर यह कुछ मान्यताओं पर टिका है।",
            "अगल-बग़ल खड़े विक्रेता दूर-दूर खड़े विक्रेताओं से सदा ऊँचे मूल्य लेते हैं।",
            "हर लोकतंत्र के राजनीतिक दल अंततः मतदाताओं को बिल्कुल एक जैसे कार्यक्रम देते हैं।",
            "समुद्र-तट पर लोगों को तब सबसे अच्छी सेवा मिलती है जब आइसक्रीम के दोनों विक्रेता ठीक बीच में खड़े हों।"],
   ans=0, pos=0)
RQ(p, "Inference", "hard", "mcq",
   "Which one of the following would most weaken the pull of the two sellers towards the centre of the beach?",
   "निम्नलिखित में से कौन-सी बात दोनों विक्रेताओं के तट के केंद्र की ओर खिंचाव को सबसे अधिक कमज़ोर करेगी?",
   "A seller moves to the middle to win bathers without losing any. If bathers far from a seller would buy nothing rather than walk, then moving inwards loses the customers at the seller's own end, and the gain from crowding the rival shrinks -- the passage names this as a case where the pull weakens. "
   "Equal prices, bathers spread evenly and sellers free to move are the very conditions under which the passage says the sellers drift to the centre; they strengthen the pull, not weaken it.",
   "विक्रेता बीच की ओर इसलिए जाता है कि बिना किसी को खोए लोग जीते। यदि विक्रेता से दूर के लोग चलने के बजाय कुछ न ख़रीदें, तो भीतर की ओर जाने से विक्रेता अपने छोर के ग्राहक खो देता है, और प्रतिद्वंद्वी के पास सटने का लाभ घट जाता है -- परिच्छेद इसे ऐसी स्थिति बताता है जिसमें खिंचाव कमज़ोर पड़ता है। "
   "बराबर मूल्य, समान रूप से फैले लोग और खिसकने को स्वतंत्र विक्रेता वही परिस्थितियाँ हैं जिनमें परिच्छेद के अनुसार विक्रेता केंद्र की ओर जाते हैं; ये खिंचाव को मज़बूत करती हैं, कमज़ोर नहीं।",
   "what-weakens-the-pull-to-the-centre",
   opts=["Bathers at the far ends would buy no ice-cream at all rather than walk far.",
         "Both sellers charge exactly the same price for ice-cream of exactly the same quality.",
         "The bathers on the beach are spread evenly along the whole of its length every day.",
         "Each of the two sellers is free to move a stall along the beach at any time of day."],
   opts_hi=["तट के दूर छोरों पर के लोग दूर चलने के बजाय आइसक्रीम ख़रीदेंगे ही नहीं।",
            "दोनों विक्रेता बिल्कुल एक ही गुणवत्ता की आइसक्रीम का बिल्कुल एक ही मूल्य लेते हैं।",
            "तट पर के लोग हर दिन उसकी पूरी लंबाई में समान रूप से फैले रहते हैं।",
            "दोनों में से हर विक्रेता दिन में किसी भी समय तट पर अपनी दुकान खिसका सकता है।"],
   ans=0, pos=3)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Both are valid. 1: once the sellers stand back to back at the centre, a seller who moves away gives up bathers to the rival without gaining any, so neither has a reason to move. "
   "2: at the quarter-points no bather walks more than a quarter of the beach; at the centre those at the ends walk half of it, twice as far, and on average every bather walks farther. The passage notes the sellers still share the beach equally, so the bathers bear the whole cost.",
   "दोनों वैध हैं। 1: जब विक्रेता केंद्र पर पीठ से पीठ सटाकर खड़े हों, तो दूर खिसकने वाला विक्रेता बिना कुछ पाए प्रतिद्वंद्वी को लोग दे देता है, इसलिए किसी के पास खिसकने का कारण नहीं। "
   "2: चौथाई-बिंदुओं पर कोई व्यक्ति तट के चौथाई से अधिक नहीं चलता; केंद्र पर छोरों के लोग उसका आधा, यानी दोगुना, चलते हैं, और औसतन हर व्यक्ति अधिक चलता है। परिच्छेद बताता है कि विक्रेता तब भी तट बराबर बाँटते हैं, इसलिए पूरी लागत लोग उठाते हैं।",
   "conclusions",
   st=["Once both sellers stand at the centre, neither can gain customers by moving away.",
       "Taken together, the bathers walk farther when the sellers stand back to back than when they stand at the quarter-points."],
   st_hi=["जब दोनों विक्रेता केंद्र पर खड़े हों, तो कोई भी दूर खिसककर ग्राहक नहीं जीत सकता।",
          "कुल मिलाकर, विक्रेताओं के पीठ से पीठ सटाकर खड़े होने पर लोग चौथाई-बिंदुओं वाली स्थिति से अधिक चलते हैं।"],
   key=2)

# ------------------------------------------------------------------ P03 James Lind's scurvy trial
p = passage("p03",
  "In May 1747, on board the British naval ship Salisbury, the surgeon James Lind took twelve sailors who were ill with scurvy and divided them into six pairs. All twelve were given the same diet, but each pair also received a different remedy: cider, a dilute acid, vinegar, sea water, a medicinal paste, or two oranges and a lemon a day. Within about a week one of the sailors given the fruit was fit for duty, and the other was well enough to help nurse the rest. No other pair did nearly as well. "
  "Lind's trial is often called one of the first controlled experiments in medicine, because by treating similar patients alike in every way but one, he could see which remedy made the difference. Yet it changed little at first. Lind himself was not sure that the fruit was the cure, and later favoured a juice concentrated by boiling. The Royal Navy began issuing lemon juice to its sailors only in 1795, nearly fifty years after the trial.",
  "मई 1747 में ब्रिटिश नौसैनिक जहाज़ सैलिसबरी पर सर्जन जेम्स लिंड ने स्कर्वी से पीड़ित बारह नाविकों को लेकर छह जोड़ियों में बाँटा। सभी बारह को एक जैसा भोजन दिया गया, पर हर जोड़ी को एक अलग उपचार भी मिला: साइडर, एक तनु अम्ल, सिरका, समुद्री पानी, एक औषधीय लेप, या प्रतिदिन दो संतरे और एक नींबू। लगभग एक सप्ताह में फल पाने वाले नाविकों में से एक काम पर लौटने योग्य हो गया, और दूसरा इतना ठीक हो गया कि बाक़ियों की देखभाल में हाथ बँटा सके। कोई और जोड़ी इसके आसपास भी नहीं पहुँची। "
  "लिंड के परीक्षण को प्रायः चिकित्सा के पहले नियंत्रित प्रयोगों में गिना जाता है, क्योंकि एक जैसे रोगियों से एक बात छोड़कर हर तरह से एक जैसा व्यवहार करके वह देख सका कि अंतर किस उपचार से आया। फिर भी शुरू में इससे बहुत कम बदला। स्वयं लिंड को पक्का विश्वास नहीं था कि फल ही उपचार है, और बाद में उसने उबालकर गाढ़े किए गए रस को अधिक पसंद किया। ब्रिटिश नौसेना ने अपने नाविकों को नींबू का रस देना 1795 में ही शुरू किया, परीक्षण के लगभग पचास वर्ष बाद।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage describes a carefully designed comparison that pointed to a cure, then shows how slowly the finding was understood and acted upon -- even by Lind himself. "
   "The navy acted nearly fifty years later, not at once; the passage praises the design of the trial rather than calling it flawed; and it reports that no other pair did nearly as well as the pair given fruit.",
   "परिच्छेद एक सावधानी से बनाई गई तुलना का वर्णन करता है जिसने उपचार की ओर संकेत किया, फिर दिखाता है कि उस निष्कर्ष को समझने और उस पर अमल करने में कितनी देर लगी -- स्वयं लिंड को भी। "
   "नौसेना ने लगभग पचास वर्ष बाद क़दम उठाया, तुरंत नहीं; परिच्छेद परीक्षण की बनावट को दोषपूर्ण नहीं, सराहनीय बताता है; और वह बताता है कि कोई और जोड़ी फल पाने वाली जोड़ी के आसपास भी नहीं पहुँची।",
   "crux",
   opts=["A well-designed comparison pointed to a cure, yet the finding was slow to be acted upon.",
         "Scurvy was cured in 1747 by a remedy that the Royal Navy then adopted at once for all its sailors.",
         "Lind's trial was badly flawed, because it used far too few sailors to show anything at all.",
         "Sea water and vinegar were found to work against scurvy as well as oranges and lemons did."],
   opts_hi=["एक सुविचारित तुलना ने उपचार की ओर संकेत किया, फिर भी उस निष्कर्ष को समझने और अपनाने में देर लगी।",
            "स्कर्वी का 1747 में एक ऐसे उपचार से इलाज हुआ जिसे ब्रिटिश नौसेना ने तुरंत अपने सभी नाविकों के लिए अपना लिया।",
            "लिंड का परीक्षण बहुत दोषपूर्ण था, क्योंकि उसमें कुछ भी दिखाने के लिए बहुत कम नाविक थे।",
            "समुद्री पानी और सिरका स्कर्वी के विरुद्ध संतरों और नींबुओं जितने ही असरदार पाए गए।"],
   ans=0, pos=2)
RQ(p, "Inference", "medium", "mcq",
   "Why, on the passage's account, did Lind give all twelve sailors the same diet?",
   "परिच्छेद के अनुसार, लिंड ने सभी बारह नाविकों को एक जैसा भोजन क्यों दिया?",
   "The passage says that by treating similar patients alike in every way but one, Lind could see which remedy made the difference. A common diet keeps food from being a second difference between the pairs, so any difference in recovery can be put down to the remedies. "
   "The passage says nothing of the ship's stores or the navy's rules about food, and the sailors could hardly have been kept from knowing whether they were eating oranges or drinking sea water.",
   "परिच्छेद कहता है कि एक जैसे रोगियों से एक बात छोड़कर हर तरह से एक जैसा व्यवहार करके लिंड देख सका कि अंतर किस उपचार से आया। एक जैसा भोजन यह सुनिश्चित करता है कि जोड़ियों के बीच भोजन दूसरा अंतर न बने, ताकि ठीक होने में कोई भी अंतर उपचारों के कारण माना जा सके। "
   "परिच्छेद जहाज़ के भंडार या भोजन के बारे में नौसेना के नियमों पर कुछ नहीं कहता, और नाविकों से यह छिपाना शायद ही संभव था कि वे संतरे खा रहे हैं या समुद्री पानी पी रहे हैं।",
   "why-one-diet-for-all",
   opts=["So that any difference in recovery could be put down to the remedies alone.",
         "Because the ship carried enough stores for only a single kind of diet.",
         "So that none of the sailors would know which remedy they had been given.",
         "Because the navy's rules did not allow any change in a sailor's daily food."],
   opts_hi=["ताकि ठीक होने में कोई भी अंतर केवल उपचारों के कारण माना जा सके।",
            "क्योंकि जहाज़ पर केवल एक ही प्रकार के भोजन लायक़ भंडार था।",
            "ताकि किसी भी नाविक को पता न चले कि उसे कौन-सा उपचार मिला है।",
            "क्योंकि नौसेना के नियम नाविक के दैनिक भोजन में कोई बदलाव नहीं होने देते थे।"],
   ans=0, pos=0)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Only 2 is valid. The trial pointed clearly to the fruit, yet Lind was unsure, preferred a boiled juice, and the navy waited nearly fifty years: a clear result did not by itself ensure that it was acted upon. "
   "1 claims far more than the trial showed: two sailors took the fruit, one became fit for duty and the other improved -- that is not evidence that the fruit cures every patient.",
   "केवल 2 वैध है। परीक्षण ने स्पष्ट रूप से फल की ओर संकेत किया, फिर भी लिंड अनिश्चित रहा, उसने उबला रस पसंद किया, और नौसेना ने लगभग पचास वर्ष प्रतीक्षा की: स्पष्ट परिणाम अपने आप उस पर अमल सुनिश्चित नहीं करता। "
   "1 परीक्षण के दिखाए से कहीं अधिक दावा करता है: दो नाविकों ने फल लिया, एक काम योग्य हुआ और दूसरे में सुधार हुआ -- यह इसका प्रमाण नहीं कि फल हर रोगी को ठीक कर देता है।",
   "conclusions",
   st=["The trial shows that oranges and lemons cure scurvy in every patient who takes them.",
       "A clear result from a well-designed trial does not by itself ensure that the result is acted upon."],
   st_hi=["परीक्षण दिखाता है कि संतरे और नींबू उन्हें लेने वाले हर रोगी की स्कर्वी ठीक कर देते हैं।",
          "सुविचारित परीक्षण का स्पष्ट परिणाम अपने आप यह सुनिश्चित नहीं करता कि उस पर अमल होगा।"],
   key=1)

# ------------------------------------------------------------------ P04 Article 21 from Gopalan to Maneka Gandhi
p = passage("p04",
  "Article 21 of the Constitution says that no person shall be deprived of life or personal liberty 'except according to procedure established by law'. The Constituent Assembly chose these words, taken from the Constitution of Japan, in place of the American phrase 'due process of law', partly to keep judges from striking down laws merely because they thought them unwise. In the Gopalan case of 1950 the Supreme Court read the article in that spirit: if a law laid down a procedure and the procedure was followed, Article 21 was satisfied, and each fundamental right was to be read on its own. "
  "In 1978, in the Maneka Gandhi case, in which a passport had been impounded without reasons being given or a hearing held, the Court changed course. It held that the procedure must itself be fair, just and reasonable, not arbitrary, and that Articles 14, 19 and 21 must be read together. Supporters see this as giving life to rights that a legislature could otherwise take away by any procedure it chose. Critics reply that the Court thereby brought back, through interpretation, much of the due process that the Assembly had deliberately left out.",
  "संविधान का अनुच्छेद 21 कहता है कि किसी व्यक्ति को उसके प्राण या दैहिक स्वतंत्रता से 'विधि द्वारा स्थापित प्रक्रिया के अनुसार ही' वंचित किया जाएगा, अन्यथा नहीं। संविधान सभा ने ये शब्द, जो जापान के संविधान से लिए गए, अमेरिकी पद 'विधि की सम्यक प्रक्रिया' (ड्यू प्रोसेस) के स्थान पर चुने, आंशिक रूप से इसलिए कि न्यायाधीश क़ानूनों को केवल इस कारण रद्द न करें कि वे उन्हें अविवेकपूर्ण लगते हैं। 1950 के गोपालन मामले में सर्वोच्च न्यायालय ने अनुच्छेद को इसी भावना से पढ़ा: यदि किसी क़ानून ने प्रक्रिया निर्धारित की और उसका पालन हुआ, तो अनुच्छेद 21 संतुष्ट था, और हर मौलिक अधिकार को अलग से पढ़ा जाना था। "
  "1978 में मेनका गांधी मामले में, जिसमें बिना कारण बताए या सुनवाई किए एक पासपोर्ट ज़ब्त कर लिया गया था, न्यायालय ने अपनी दिशा बदली। उसने माना कि प्रक्रिया स्वयं उचित, न्यायपूर्ण और युक्तियुक्त होनी चाहिए, मनमानी नहीं, और अनुच्छेद 14, 19 और 21 को साथ पढ़ा जाना चाहिए। समर्थक इसे उन अधिकारों में जान डालने वाला मानते हैं जिन्हें अन्यथा विधायिका अपनी चुनी किसी भी प्रक्रिया से छीन सकती थी। आलोचक उत्तर देते हैं कि इस तरह न्यायालय ने व्याख्या के रास्ते उस सम्यक प्रक्रिया का बड़ा भाग वापस ला दिया जिसे सभा ने जान-बूझकर छोड़ा था।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage traces how the Supreme Court moved from a narrow reading of Article 21 to one that tests whether a procedure is fair, and sets out the case for and against that change. "
   "It says only the phrase in Article 21 came from Japan, not the fundamental rights as a whole; it says nothing about Parliament being unable to restrict liberty -- a fair procedure can still do so; and it reports both views without declaring either judgment wrong.",
   "परिच्छेद बताता है कि सर्वोच्च न्यायालय अनुच्छेद 21 की संकीर्ण व्याख्या से ऐसी व्याख्या तक कैसे पहुँचा जो जाँचती है कि प्रक्रिया उचित है या नहीं, और उस बदलाव के पक्ष और विपक्ष के तर्क रखता है। "
   "वह कहता है कि केवल अनुच्छेद 21 का पद जापान से आया, पूरे मौलिक अधिकार नहीं; वह यह नहीं कहता कि संसद स्वतंत्रता पर कोई रोक नहीं लगा सकती -- उचित प्रक्रिया से अब भी लगा सकती है; और वह दोनों मत रखता है, किसी निर्णय को ग़लत घोषित किए बिना।",
   "crux",
   opts=["The Court read Article 21 more widely than its words, which some welcome and others question.",
         "India's fundamental rights were copied, almost word for word, from the Constitution of Japan.",
         "Since 1978 Parliament has been unable to make any law at all that restricts personal liberty.",
         "The Gopalan case was rightly decided, and the Maneka Gandhi case was decided wrongly."],
   opts_hi=["न्यायालय ने अनुच्छेद 21 को उसके शब्दों से व्यापक पढ़ा, जिस पर मत बँटे हुए हैं।",
            "भारत के मौलिक अधिकार लगभग शब्दशः जापान के संविधान से लिए गए थे।",
            "1978 से संसद दैहिक स्वतंत्रता पर किसी भी प्रकार की रोक लगाने वाला कोई क़ानून नहीं बना सकी है।",
            "गोपालन मामले का निर्णय सही था, और मेनका गांधी मामले का निर्णय ग़लत।"],
   ans=0, pos=3)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Only 1 is valid. Under the Gopalan reading, Article 21 asked only whether a law laid down a procedure and whether it was followed; whether the procedure was fair did not enter into it, so an unfair procedure set by law could still satisfy the article. "
   "2 reverses the critics' complaint: they say the Court took on more power than the framers intended, not that the judgment protects too little liberty.",
   "केवल 1 वैध है। गोपालन व्याख्या में अनुच्छेद 21 केवल यह पूछता था कि क्या किसी क़ानून ने प्रक्रिया निर्धारित की और क्या उसका पालन हुआ; प्रक्रिया उचित है या नहीं, यह प्रश्न ही नहीं था, इसलिए क़ानून द्वारा निर्धारित अनुचित प्रक्रिया भी अनुच्छेद को संतुष्ट कर सकती थी। "
   "2 आलोचकों की शिकायत को उलट देता है: वे कहते हैं कि न्यायालय ने निर्माताओं के इरादे से अधिक शक्ति ले ली, यह नहीं कि निर्णय बहुत कम स्वतंत्रता की रक्षा करता है।",
   "conclusions",
   st=["Under the Gopalan reading, a law that laid down an unfair procedure could still satisfy Article 21.",
       "The critics' objection is that the Maneka Gandhi judgment protects too little personal liberty."],
   st_hi=["गोपालन व्याख्या में, अनुचित प्रक्रिया निर्धारित करने वाला क़ानून भी अनुच्छेद 21 को संतुष्ट कर सकता था।",
          "आलोचकों की आपत्ति यह है कि मेनका गांधी निर्णय दैहिक स्वतंत्रता की बहुत कम रक्षा करता है।"],
   key=0)
RQ(p, "Specific Detail", "easy", "mcq",
   "According to the passage, what had happened in the Maneka Gandhi case?",
   "परिच्छेद के अनुसार, मेनका गांधी मामले में क्या हुआ था?",
   "The passage says that a passport had been impounded without reasons being given or a hearing held. "
   "It mentions no arrest, no election and no taking of property.",
   "परिच्छेद कहता है कि बिना कारण बताए या सुनवाई किए एक पासपोर्ट ज़ब्त कर लिया गया था। "
   "वह किसी गिरफ़्तारी, चुनाव या संपत्ति लिए जाने का उल्लेख नहीं करता।",
   "what-happened-in-the-case",
   opts=["A passport was impounded with no reasons given and no hearing held.",
         "A person was arrested under a law passed soon after the Gopalan case.",
         "A candidate was barred from contesting an election to Parliament.",
         "Private property was taken over by the State without any compensation."],
   opts_hi=["बिना कारण बताए या सुनवाई किए एक पासपोर्ट ज़ब्त कर लिया गया।",
            "गोपालन मामले के तुरंत बाद बने एक क़ानून के तहत एक व्यक्ति को गिरफ़्तार किया गया।",
            "एक उम्मीदवार को संसद का चुनाव लड़ने से रोक दिया गया।",
            "राज्य ने बिना किसी मुआवज़े के निजी संपत्ति ले ली।"],
   ans=0, pos=1)

# ------------------------------------------------------------------ P05 the paradox of the heap (2)
p = passage("p05",
  "One grain of sand is not a heap, and adding a single grain to something that is not a heap never seems to turn it into one. Yet if that is so, then two grains are not a heap, nor three, nor any number at all -- and heaps plainly exist. This puzzle, first posed in ancient Greece, arises with many everyday words: tall, old, poor, crowded. No single step makes a difference, but many steps together make all the difference. "
  "The law cannot wait for philosophers to settle the matter. It draws sharp lines -- a voting age of 18, a poverty line, a speed limit -- knowing that a person one day short of 18 is no less mature than one a day past it. Such lines are arbitrary at the margin, but without them every case would have to be argued afresh.",
  "रेत का एक कण ढेर नहीं है, और जो ढेर नहीं है उसमें एक कण जोड़ने से वह कभी ढेर बनता नहीं दिखता। पर यदि ऐसा है, तो दो कण ढेर नहीं, न तीन, न कोई भी संख्या -- और ढेर तो स्पष्ट रूप से होते हैं। यह पहेली, जो पहली बार प्राचीन यूनान में उठाई गई, रोज़ के बहुत-से शब्दों के साथ उठती है: लंबा, बूढ़ा, ग़रीब, भीड़भरा। कोई एक क़दम अंतर नहीं लाता, पर बहुत-से क़दम मिलकर पूरा अंतर ला देते हैं। "
  "क़ानून दार्शनिकों के इसे सुलझाने की प्रतीक्षा नहीं कर सकता। वह तीखी रेखाएँ खींचता है -- 18 वर्ष की मतदान आयु, ग़रीबी रेखा, गति सीमा -- यह जानते हुए कि 18 से एक दिन कम का व्यक्ति एक दिन अधिक वाले से कम परिपक्व नहीं। ऐसी रेखाएँ सीमा पर मनमानी हैं, पर उनके बिना हर मामले पर नए सिरे से बहस करनी पड़ती।")
RQ(p, "Main Idea", "medium", "mcq", MSG, MSG_HI,
   "The passage grants that sharp legal lines are arbitrary at the margin, since the words they stand for are vague, and defends them as necessary: without them every case would be argued afresh. "
   "It does not ask the law to stop using vague words -- it shows how the law copes with them; it says a person a day short of 18 is no less mature, but defends the line rather than proposing to move it; and it says heaps 'plainly exist'.",
   "परिच्छेद मानता है कि क़ानून की तीखी रेखाएँ सीमा पर मनमानी हैं, क्योंकि जिन शब्दों के लिए वे हैं वे अस्पष्ट हैं, और उन्हें आवश्यक बताकर उनका बचाव करता है: उनके बिना हर मामले पर नए सिरे से बहस होती। "
   "वह क़ानून से अस्पष्ट शब्द छोड़ने को नहीं कहता -- वह दिखाता है कि क़ानून उनसे कैसे निपटता है; वह कहता है कि 18 से एक दिन कम वाला कम परिपक्व नहीं, पर रेखा खिसकाने का प्रस्ताव नहीं, उसका बचाव करता है; और वह कहता है कि ढेर 'स्पष्ट रूप से होते हैं'।",
   "message",
   opts=["Sharp lines in law are arbitrary at the edges, but they are needed where words are vague.",
         "Since vague words lead to paradox, laws should stop using words such as 'poor' or 'old'.",
         "A person one day short of 18 ought to be allowed to vote, being no less mature than an adult.",
         "Heaps do not really exist, since no single grain of sand can ever turn a pile into one."],
   opts_hi=["क़ानून की तीखी रेखाएँ किनारों पर मनमानी हैं, पर जहाँ शब्द अस्पष्ट हों वहाँ वे आवश्यक हैं।",
            "चूँकि अस्पष्ट शब्द विरोधाभास पैदा करते हैं, क़ानूनों को 'ग़रीब' या 'बूढ़ा' जैसे शब्द छोड़ देने चाहिए।",
            "18 से एक दिन कम वाले व्यक्ति को मतदान करने देना चाहिए, क्योंकि वह किसी वयस्क से कम परिपक्व नहीं।",
            "ढेर वास्तव में होते ही नहीं, क्योंकि रेत का कोई एक कण किसी अंबार को कभी ढेर नहीं बना सकता।"],
   ans=0, pos=2)
RQ(p, "Inference", "hard", "mcq",
   "Which one of the following is a case of the same puzzle as the one the passage describes?",
   "निम्नलिखित में से कौन-सी स्थिति उसी पहेली का उदाहरण है जिसका परिच्छेद वर्णन करता है?",
   "The puzzle arises when no single small step makes a difference, yet many steps together clearly do. Losing one hair never makes a person bald, yet many people are bald: the same structure. "
   "A run of ten heads is about chance, not about a vague word; a rule unfair to some citizens is about fairness; and two witnesses using different words is about description. None involves a long series of steps that each seem to change nothing.",
   "पहेली तब उठती है जब कोई एक छोटा क़दम अंतर नहीं लाता, फिर भी बहुत-से क़दम मिलकर स्पष्ट अंतर लाते हैं। एक बाल झड़ने से कोई गंजा नहीं होता, फिर भी बहुत-से लोग गंजे हैं: वही बनावट। "
   "लगातार दस बार चित आना संयोग के बारे में है, किसी अस्पष्ट शब्द के बारे में नहीं; कुछ नागरिकों के लिए अनुचित नियम निष्पक्षता के बारे में है; और दो गवाहों के अलग शब्द वर्णन के बारे में हैं। इनमें से किसी में ऐसे क़दमों की लंबी कड़ी नहीं जिनमें से हर एक कुछ न बदलता दिखे।",
   "the-same-puzzle-elsewhere",
   opts=["Losing one hair never makes a person bald, yet many people are bald.",
         "A coin tossed many times may come up heads ten times in a row.",
         "A rule that applies to every citizen may still be unfair to some of them.",
         "Two honest witnesses may describe the same event in different words."],
   opts_hi=["एक बाल झड़ने से कोई गंजा नहीं होता, फिर भी बहुत-से लोग गंजे हैं।",
            "कई बार उछाला गया सिक्का लगातार दस बार चित आ सकता है।",
            "हर नागरिक पर लागू होने वाला नियम भी उनमें से कुछ के लिए अनुचित हो सकता है।",
            "दो ईमानदार गवाह एक ही घटना का अलग-अलग शब्दों में वर्णन कर सकते हैं।"],
   ans=0, pos=3)

# ------------------------------------------------------------------ P06 a prophecy that failed
p = passage("p06",
  "In 1954 a small group in the United States came to believe, on the strength of messages its leader claimed to receive from beings in outer space, that a great flood would destroy much of the world before dawn on a set day in December, and that the faithful would be rescued by a flying saucer. Some members gave up their jobs and their possessions. The psychologist Leon Festinger and two colleagues joined the group without revealing who they were, to see what would happen when the prophecy failed. "
  "Dawn came, with no flood and no saucer. Yet the core members did not give up their belief. They announced that their faith had saved the world and began, for the first time, to seek publicity and new converts. Festinger explained this by what he called cognitive dissonance: holding beliefs that clash with each other, or with what one has done, is uncomfortable, and people often ease the discomfort by reinterpreting the evidence rather than abandoning a belief in which they have invested a great deal. Members who had waited for the end alone, away from the group, were far more likely to give the belief up.",
  "1954 में संयुक्त राज्य अमेरिका में एक छोटे समूह ने, उन संदेशों के बल पर जिनके बारे में उसके नेता का दावा था कि वे बाहरी अंतरिक्ष के प्राणियों से मिलते हैं, यह मान लिया कि दिसंबर के एक निश्चित दिन भोर से पहले एक भीषण बाढ़ दुनिया के बड़े भाग को नष्ट कर देगी, और आस्थावानों को एक उड़नतश्तरी बचा लेगी। कुछ सदस्यों ने अपनी नौकरियाँ और अपनी संपत्ति छोड़ दी। मनोवैज्ञानिक लियोन फ़ेस्टिंगर और उनके दो सहयोगी अपनी पहचान बताए बिना समूह में शामिल हो गए, यह देखने के लिए कि भविष्यवाणी विफल होने पर क्या होगा। "
  "भोर हुई, न बाढ़ आई न उड़नतश्तरी। फिर भी मुख्य सदस्यों ने अपना विश्वास नहीं छोड़ा। उन्होंने घोषणा की कि उनकी आस्था ने दुनिया को बचा लिया है और पहली बार प्रचार और नए अनुयायी जुटाने लगे। फ़ेस्टिंगर ने इसकी व्याख्या उस बात से की जिसे उन्होंने संज्ञानात्मक असंगति कहा: ऐसे विश्वास रखना जो आपस में, या अपने किए से, टकराते हों, असहज होता है, और लोग प्रायः यह असहजता उस विश्वास को छोड़कर नहीं, जिसमें उन्होंने बहुत कुछ लगाया हो, बल्कि प्रमाण की नई व्याख्या करके दूर करते हैं। जिन सदस्यों ने समूह से दूर, अकेले अंत की प्रतीक्षा की थी, उनके विश्वास छोड़ने की संभावना कहीं अधिक थी।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage shows believers holding on more firmly after their prophecy failed, explains this as a way of easing an uncomfortable clash, and ends by noting that those who faced the failure alone were more likely to let go. "
   "It describes one group that did not disband, so it cannot say such groups always do; it reports Festinger's method without judging it; and it makes no claim that people who give up jobs for a belief are more honest.",
   "परिच्छेद दिखाता है कि भविष्यवाणी विफल होने के बाद विश्वासी और दृढ़ता से टिके रहे, इसे एक असहज टकराव को कम करने का ढंग बताता है, और यह कहकर समाप्त होता है कि विफलता का अकेले सामना करने वालों के विश्वास छोड़ने की संभावना अधिक थी। "
   "वह एक ऐसे समूह का वर्णन करता है जो बिखरा नहीं, इसलिए यह नहीं कह सकता कि ऐसे समूह सदा बिखर जाते हैं; वह फ़ेस्टिंगर की पद्धति को आँके बिना बताता है; और वह यह दावा नहीं करता कि विश्वास के लिए नौकरी छोड़ने वाले अधिक ईमानदार होते हैं।",
   "crux",
   opts=["A refuted belief may be held more tightly, especially when others share it.",
         "Groups that predict the end of the world always break up once the date has passed.",
         "Psychologists should never study a group of people without first telling its members.",
         "People who give up their jobs for a belief are more honest than those who do not."],
   opts_hi=["खंडित विश्वास को लोग और कसकर पकड़ सकते हैं, विशेषकर जब दूसरे भी उसे मानें।",
            "दुनिया के अंत की भविष्यवाणी करने वाले समूह तारीख़ बीतते ही सदा बिखर जाते हैं।",
            "मनोवैज्ञानिकों को किसी समूह के सदस्यों को पहले बताए बिना उसका अध्ययन कभी नहीं करना चाहिए।",
            "जो लोग किसी विश्वास के लिए नौकरी छोड़ देते हैं, वे बाक़ियों से अधिक ईमानदार होते हैं।"],
   ans=0, pos=0)
RQ(p, "Inference", "hard", "mcq",
   "What does the passage suggest about the part played by fellow believers?",
   "परिच्छेद साथी विश्वासियों की भूमिका के बारे में क्या संकेत देता है?",
   "Those who waited with the group mostly kept the belief; those who waited alone were far more likely to give it up. So the company of fellow believers helped people hold on to a belief the evidence had refuted. "
   "The members with the group were the ones who sought converts, not the ones made less willing; being with others made it easier to keep the belief, not to accept that it was false; and the passage gives no comparison showing that what members had given up mattered more than the group.",
   "जिन्होंने समूह के साथ प्रतीक्षा की, उन्होंने अधिकतर विश्वास बनाए रखा; जिन्होंने अकेले प्रतीक्षा की, उनके उसे छोड़ने की संभावना कहीं अधिक थी। इसलिए साथी विश्वासियों के साथ ने लोगों को उस विश्वास पर टिके रहने में मदद की जिसका प्रमाण ने खंडन कर दिया था। "
   "समूह के साथ वाले सदस्यों ने ही अनुयायी जुटाए, वे कम इच्छुक नहीं हुए; दूसरों के साथ होने ने विश्वास बनाए रखना आसान किया, उसे झूठा मानना नहीं; और परिच्छेद ऐसी कोई तुलना नहीं देता जो दिखाए कि सदस्यों का त्याग समूह से अधिक मायने रखता था।",
   "what-fellow-believers-did",
   opts=["Their company helped people keep a belief that the evidence had refuted.",
         "Their company made the members less willing to look for new converts.",
         "Their company made it easier to accept that the prophecy had been false.",
         "They mattered less than how much each member had given up for the belief."],
   opts_hi=["उनके साथ ने प्रमाण से खंडित विश्वास बनाए रखने में मदद की।",
            "उनके साथ ने सदस्यों को नए अनुयायी खोजने के लिए कम इच्छुक बना दिया।",
            "उनके साथ ने यह मानना आसान कर दिया कि भविष्यवाणी झूठी थी।",
            "विश्वास के लिए हर सदस्य के त्याग की तुलना में उनका महत्त्व कम था।"],
   ans=0, pos=1)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Only 2 is valid. The passage explains the new search for publicity and converts by cognitive dissonance: winning others to the belief eased the discomfort of a failed prophecy. "
   "1 reverses Festinger's account: on it, the more a member had invested in the belief, the harder it was to abandon, so those who had given up the least would cling least, not hardest.",
   "केवल 2 वैध है। परिच्छेद प्रचार और अनुयायियों की नई खोज की व्याख्या संज्ञानात्मक असंगति से करता है: दूसरों को विश्वास में लाने से विफल भविष्यवाणी की असहजता कम हुई। "
   "1 फ़ेस्टिंगर की व्याख्या को उलट देता है: उसके अनुसार सदस्य ने विश्वास में जितना अधिक लगाया था, उसे छोड़ना उतना कठिन था, इसलिए सबसे कम त्याग करने वाले सबसे कम चिपकते, सबसे अधिक नहीं।",
   "conclusions",
   st=["On Festinger's account, the members who had given up the least for the belief would cling to it hardest.",
       "Seeking new converts after the failure was a way of easing the discomfort that the failure caused."],
   st_hi=["फ़ेस्टिंगर की व्याख्या के अनुसार, विश्वास के लिए सबसे कम त्याग करने वाले सदस्य उससे सबसे अधिक चिपके रहते।",
          "विफलता के बाद नए अनुयायी खोजना उस असहजता को कम करने का ढंग था जो विफलता से पैदा हुई।"],
   key=1)

# ------------------------------------------------------------------ P07 Dadabhai Naoroji and the drain of wealth
p = passage("p07",
  "In the late nineteenth century Dadabhai Naoroji set out to measure the poverty of India. Working from official figures, he estimated that income per head was only about 20 rupees a year -- too little, he argued, to keep a labourer in the barest health. His explanation became known as the drain of wealth. Every year a large part of India's revenue left the country for Britain without any return: as the salaries and pensions of British officials, as interest on public debt, and as the 'home charges' of the government of India in London. A country that sends abroad each year a share of what it produces, he argued, cannot build up the capital it needs to grow. "
  "His book, Poverty and Un-British Rule in India, was published in 1901. Its title made his point: he did not reject the British ideals of justice and fair dealing, but accused British rule in India of betraying them. Later historians have disputed his figures, but the idea of the drain gave the national movement an economic charge against colonial rule that did not rest on sentiment alone.",
  "उन्नीसवीं सदी के उत्तरार्ध में दादाभाई नौरोजी ने भारत की ग़रीबी मापने का प्रयास किया। सरकारी आँकड़ों के आधार पर उन्होंने अनुमान लगाया कि प्रति व्यक्ति आय केवल लगभग 20 रुपये वार्षिक थी -- उनके तर्क में, एक मज़दूर को न्यूनतम स्वस्थ रखने के लिए भी बहुत कम। उनकी व्याख्या धन के निकास (ड्रेन ऑफ़ वेल्थ) के नाम से जानी गई। हर वर्ष भारत के राजस्व का एक बड़ा भाग बिना किसी प्रतिफल के देश से ब्रिटेन चला जाता था: ब्रिटिश अधिकारियों के वेतन और पेंशन के रूप में, सार्वजनिक ऋण पर ब्याज के रूप में, और लंदन में भारत सरकार के 'होम चार्जेज़' के रूप में। उनका तर्क था कि जो देश हर वर्ष अपने उत्पादन का एक भाग विदेश भेजता है, वह बढ़ने के लिए आवश्यक पूँजी नहीं जुटा सकता। "
  "उनकी पुस्तक, पॉवर्टी एंड अन-ब्रिटिश रूल इन इंडिया, 1901 में प्रकाशित हुई। उसका शीर्षक ही उनकी बात कहता था: वे न्याय और निष्पक्ष व्यवहार के ब्रिटिश आदर्शों को अस्वीकार नहीं करते थे, बल्कि भारत में ब्रिटिश शासन पर उन आदर्शों से विश्वासघात का आरोप लगाते थे। बाद के इतिहासकारों ने उनके आँकड़ों पर विवाद किया है, पर निकास के विचार ने राष्ट्रीय आंदोलन को औपनिवेशिक शासन के विरुद्ध एक ऐसा आर्थिक आरोप दिया जो केवल भावना पर नहीं टिका था।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage presents Naoroji's case that a yearly outflow of wealth without return kept India poor, and ends with its significance: whatever the disputes over his figures, it gave the national movement an economic case against colonial rule. "
   "His figures are said to be disputed, not proved beyond dispute; he appealed to British ideals rather than rejecting them; and the drain was made up of official payments, not of Indians choosing to send their savings abroad.",
   "परिच्छेद नौरोजी का यह तर्क रखता है कि बिना प्रतिफल के धन के वार्षिक बहिर्गमन ने भारत को ग़रीब रखा, और उसके महत्त्व पर समाप्त होता है: उनके आँकड़ों पर विवाद जो भी हो, इसने राष्ट्रीय आंदोलन को औपनिवेशिक शासन के विरुद्ध आर्थिक तर्क दिया। "
   "उनके आँकड़ों को विवादित कहा गया है, निर्विवाद रूप से सिद्ध नहीं; उन्होंने ब्रिटिश आदर्शों को अस्वीकार नहीं किया, उनकी दुहाई दी; और निकास सरकारी भुगतानों से बना था, भारतीयों द्वारा अपनी इच्छा से बचत विदेश भेजने से नहीं।",
   "crux",
   opts=["Naoroji blamed India's poverty on a yearly drain of wealth, giving nationalists an economic case.",
         "Naoroji proved beyond all dispute that India's income per head was exactly 20 rupees a year.",
         "Naoroji rejected British ideas of justice and fair dealing as being unsuited to India.",
         "India was poor mainly because its own people chose to send their savings abroad of their own free will."],
   opts_hi=["नौरोजी ने ग़रीबी को धन के वार्षिक निकास से जोड़ा, जिससे राष्ट्रवादियों को आर्थिक तर्क मिला।",
            "नौरोजी ने निर्विवाद रूप से सिद्ध किया कि भारत की प्रति व्यक्ति आय ठीक 20 रुपये वार्षिक थी।",
            "नौरोजी ने न्याय और निष्पक्ष व्यवहार के ब्रिटिश विचारों को भारत के लिए अनुपयुक्त बताकर अस्वीकार किया।",
            "भारत मुख्यतः इसलिए ग़रीब था कि उसके लोग अपनी इच्छा से अपनी बचत विदेश भेजते थे।"],
   ans=0, pos=3)
RQ(p, "Inference", "hard", "mcq",
   "Which one of the following can be inferred about the way Naoroji argued his case?",
   "नौरोजी ने अपना पक्ष जिस ढंग से रखा, उसके बारे में निम्नलिखित में से कौन-सा निष्कर्ष निकाला जा सकता है?",
   "The title 'Un-British Rule' and the passage's gloss on it show that Naoroji measured British rule in India against ideals the British themselves professed -- justice and fair dealing -- and found it wanting. "
   "He did not reject British ideals, so a call to cut every tie at once does not follow; he worked from official figures, and the passage says his case did not rest on sentiment alone; and he blamed the drain, not the size of the population.",
   "शीर्षक 'अन-ब्रिटिश रूल' और परिच्छेद में उसकी व्याख्या दिखाती है कि नौरोजी ने भारत में ब्रिटिश शासन को उन आदर्शों -- न्याय और निष्पक्ष व्यवहार -- की कसौटी पर परखा जिनका दावा स्वयं ब्रिटिश करते थे, और उसे खरा नहीं पाया। "
   "उन्होंने ब्रिटिश आदर्शों को अस्वीकार नहीं किया, इसलिए हर संबंध तुरंत तोड़ने की माँग का निष्कर्ष नहीं निकलता; उन्होंने सरकारी आँकड़ों से काम किया, और परिच्छेद कहता है कि उनका तर्क केवल भावना पर नहीं टिका था; और उन्होंने दोष निकास को दिया, जनसंख्या के आकार को नहीं।",
   "how-naoroji-argued",
   opts=["He judged British rule by the standards that its own rulers claimed to uphold.",
         "He held that India should cut every one of its ties with Britain at once.",
         "He relied on feeling far more than on figures to make his case against the rule.",
         "He blamed India's poverty mainly on the great size of its growing population."],
   opts_hi=["उन्होंने ब्रिटिश शासन को उसके शासकों के अपने घोषित मानकों पर परखा।",
            "उनका मत था कि भारत को ब्रिटेन से अपना हर संबंध तुरंत तोड़ लेना चाहिए।",
            "शासन के विरुद्ध अपना पक्ष रखने में वे आँकड़ों से कहीं अधिक भावना पर निर्भर रहे।",
            "उन्होंने भारत की ग़रीबी का मुख्य दोष उसकी बढ़ती जनसंख्या के बड़े आकार को दिया।"],
   ans=0, pos=2)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Neither is valid. 1: the drain the passage describes was made up of official payments -- salaries, pensions, interest and home charges -- not of spending on imported goods. "
   "2: the passage says later historians have disputed Naoroji's figures, which is the opposite of saying they have been confirmed.",
   "कोई भी वैध नहीं। 1: परिच्छेद में वर्णित निकास सरकारी भुगतानों -- वेतन, पेंशन, ब्याज और होम चार्जेज़ -- से बना था, आयातित वस्तुओं पर ख़र्च से नहीं। "
   "2: परिच्छेद कहता है कि बाद के इतिहासकारों ने नौरोजी के आँकड़ों पर विवाद किया है, जो उनकी पुष्टि होने के ठीक उलट है।",
   "conclusions",
   st=["Naoroji held that the drain arose because Indians spent too much on goods imported from Britain.",
       "The passage shows that Naoroji's estimate of income per head has since been confirmed by historians."],
   st_hi=["नौरोजी का मत था कि निकास इसलिए हुआ कि भारतीय ब्रिटेन से आयातित वस्तुओं पर बहुत ख़र्च करते थे।",
          "परिच्छेद दिखाता है कि नौरोजी के प्रति व्यक्ति आय के अनुमान की इतिहासकारों ने बाद में पुष्टि की है।"],
   key=3)

# ------------------------------------------------------------------ P08 the olive ridleys of Odisha
p = passage("p08",
  "Every winter olive ridley turtles gather off the coast of Odisha, and on a few nights hundreds of thousands of females come ashore together to nest -- an event known by the Spanish word arribada, 'arrival'. The beaches at Gahirmatha and at the mouth of the Rushikulya river are among the largest such nesting sites in the world. Each female digs a pit, lays about a hundred eggs and returns to the sea; the hatchlings emerge some weeks later and make for the water on their own. "
  "The turtles' greatest danger lies not on the beaches but offshore. Turtles must come up to breathe, and those caught in trawl nets drown. Odisha therefore bans fishing close to the main nesting beaches during the season, and requires trawlers to fit turtle excluder devices -- grids that let a turtle escape through a flap while keeping most of the catch. Many fishers resent both rules, which cost them income, and enforcing them along a long coast is difficult. The sand matters too: eggs that incubate in warmer sand produce more females.",
  "हर सर्दी में ओलिव रिडले कछुए ओडिशा के तट के पास इकट्ठा होते हैं, और कुछ रातों में लाखों मादाएँ एक साथ अंडे देने तट पर आती हैं -- एक घटना जिसे स्पेनिश शब्द अरिबाडा, यानी 'आगमन', से जाना जाता है। गहिरमाथा के और रुशिकुल्या नदी के मुहाने के तट दुनिया के ऐसे सबसे बड़े घोंसला-स्थलों में हैं। हर मादा एक गड्ढा खोदती है, लगभग सौ अंडे देती है और समुद्र में लौट जाती है; कुछ सप्ताह बाद बच्चे निकलते हैं और अपने आप पानी की ओर बढ़ते हैं। "
  "कछुओं के लिए सबसे बड़ा ख़तरा तटों पर नहीं, समुद्र में है। कछुओं को साँस लेने के लिए ऊपर आना पड़ता है, और ट्रॉल जालों में फँसे कछुए डूब जाते हैं। इसलिए ओडिशा मौसम के दौरान मुख्य घोंसला-तटों के निकट मछली पकड़ने पर रोक लगाता है, और ट्रॉलरों के लिए टर्टल एक्सक्लूडर डिवाइस लगाना अनिवार्य करता है -- ऐसी जालियाँ जो पकड़ का अधिकांश भाग रखते हुए कछुए को एक फ़्लैप से निकल जाने देती हैं। बहुत-से मछुआरे इन दोनों नियमों से नाराज़ हैं, जिनसे उनकी आय घटती है, और लंबे तट पर इन्हें लागू करना कठिन है। रेत भी मायने रखती है: गर्म रेत में सेए गए अंडों से अधिक मादाएँ निकलती हैं।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "After describing the mass nesting, the passage turns to the real danger, drowning in trawl nets offshore, and to the rules meant to prevent it, which carry costs for fishers and are hard to enforce. "
   "It says the Odisha beaches are among the largest sites, not the only ones; it describes a ban near the nesting beaches in season, not a call for a year-round ban on the whole coast; and it says the greatest danger is offshore, not on the beaches.",
   "सामूहिक घोंसला-निर्माण का वर्णन करने के बाद परिच्छेद असली ख़तरे, यानी समुद्र में ट्रॉल जालों में डूबने, और उसे रोकने के नियमों की ओर मुड़ता है, जिनकी मछुआरों पर लागत है और जिन्हें लागू करना कठिन है। "
   "वह कहता है कि ओडिशा के तट सबसे बड़े स्थलों में हैं, एकमात्र नहीं; वह मौसम में घोंसला-तटों के निकट रोक का वर्णन करता है, पूरे तट पर साल भर रोक की माँग नहीं करता; और वह कहता है कि सबसे बड़ा ख़तरा समुद्र में है, तटों पर नहीं।",
   "crux",
   opts=["Saving the turtles depends on rules at sea, and those rules carry real costs.",
         "Olive ridley turtles come ashore to nest only on the beaches of the coast of Odisha.",
         "Fishing should be banned along the whole of India's coastline for the entire year.",
         "Most olive ridleys are killed on the beaches where they come ashore to lay eggs."],
   opts_hi=["कछुओं को बचाना समुद्र के नियमों पर निर्भर है, जिनकी वास्तविक लागत है।",
            "ओलिव रिडले कछुए अंडे देने केवल ओडिशा के तट पर ही आते हैं।",
            "भारत के पूरे समुद्र-तट पर पूरे वर्ष मछली पकड़ने पर रोक होनी चाहिए।",
            "अधिकांश ओलिव रिडले उन तटों पर मारे जाते हैं जहाँ वे अंडे देने आते हैं।"],
   ans=0, pos=1)
RQ(p, "Specific Detail", "medium", "mcq",
   "According to the passage, how does a turtle excluder device protect turtles?",
   "परिच्छेद के अनुसार, टर्टल एक्सक्लूडर डिवाइस कछुओं की रक्षा कैसे करता है?",
   "The passage describes the devices as grids fitted to trawl nets that let a turtle escape through a flap while keeping most of the catch. "
   "It says nothing about frightening turtles away before a net is lowered, marking the beaches, or warming the sand -- warm sand is mentioned only as something that affects the share of females.",
   "परिच्छेद इन उपकरणों को ट्रॉल जालों में लगी ऐसी जालियाँ बताता है जो पकड़ का अधिकांश भाग रखते हुए कछुए को एक फ़्लैप से निकल जाने देती हैं। "
   "वह जाल डालने से पहले कछुओं को डराकर भगाने, तटों को चिह्नित करने या रेत गर्म करने के बारे में कुछ नहीं कहता -- गर्म रेत का उल्लेख केवल मादाओं के अनुपात को प्रभावित करने वाली बात के रूप में है।",
   "how-the-device-works",
   opts=["As a grid in the net, it lets a turtle escape through a flap.",
         "It scares turtles away from a trawler before its nets are lowered into the sea.",
         "It marks the nesting beaches so that fishing boats know to keep well away from them.",
         "It warms the sand of the nesting beaches so that more of the eggs hatch safely."],
   opts_hi=["जाल में लगी जाली के रूप में, यह कछुए को एक फ़्लैप से निकल जाने देता है।",
            "यह ट्रॉलर के जाल समुद्र में डालने से पहले कछुओं को डराकर दूर भगा देता है।",
            "यह घोंसला-तटों को चिह्नित करता है ताकि मछली पकड़ने वाली नावें उनसे दूर रहें।",
            "यह घोंसला-तटों की रेत गर्म करता है ताकि अधिक अंडों से सुरक्षित बच्चे निकलें।"],
   ans=0, pos=3)
RQ(p, "Inference", "hard", "mcq",
   "Which one of the following long-term risks does the passage's last sentence point to?",
   "परिच्छेद का अंतिम वाक्य निम्नलिखित में से किस दीर्घकालिक जोखिम की ओर संकेत करता है?",
   "If warmer sand yields more females, then sand that keeps growing warmer could tilt the hatchlings so far towards females that too few males are born to keep the population healthy. "
   "The sentence is about the sex of the hatchlings, not about how many females come ashore, where the eggs are laid, or how many turtles drown in nets.",
   "यदि गर्म रेत से अधिक मादाएँ निकलती हैं, तो लगातार गर्म होती रेत बच्चों को मादाओं की ओर इतना झुका सकती है कि आबादी को स्वस्थ रखने लायक़ नर पैदा न हों। "
   "वाक्य बच्चों के लिंग के बारे में है, इस बारे में नहीं कि कितनी मादाएँ तट पर आती हैं, अंडे कहाँ दिए जाते हैं, या कितने कछुए जालों में डूबते हैं।",
   "what-warmer-sand-could-mean",
   opts=["Steadily warmer sand could leave too few males among the hatchlings.",
         "Warmer sand could stop the females from coming ashore to nest at all.",
         "Warmer sand could make the turtles lay their eggs out at sea instead.",
         "Warmer sand could drive more of the young turtles into trawl nets."],
   opts_hi=["लगातार गर्म होती रेत से बच्चों में नर बहुत कम रह सकते हैं।",
            "गर्म रेत मादाओं को अंडे देने तट पर आने से ही रोक सकती है।",
            "गर्म रेत से कछुए अपने अंडे समुद्र में ही देने लग सकते हैं।",
            "गर्म रेत अधिक छोटे कछुओं को ट्रॉल जालों की ओर धकेल सकती है।"],
   ans=0, pos=2)

# ------------------------------------------------------------------ P09 Eratosthenes measures the Earth
p = passage("p09",
  "Around 240 BCE the scholar Eratosthenes, who ran the great library at Alexandria, worked out the size of the Earth without leaving Egypt. He had learned that at Syene, to the south, the Sun stood directly overhead at noon on the longest day of the year, so that it shone straight down a deep well. At noon on that day at Alexandria, a vertical stick cast a short shadow, showing that the Sun there was about one-fiftieth of a full circle away from overhead. If the Earth is round, the distance from Syene to Alexandria must then be one-fiftieth of the way round it. Taking that distance as 5,000 stadia, he put the Earth's circumference at about 250,000 stadia. "
  "His method was sound, but it rested on several assumptions: that the Earth is a sphere, that the Sun is so far away that its rays reach both cities in parallel lines, and that Syene lies due south of Alexandria -- which it does only roughly. How close his answer came to the true figure is still debated, because no one is sure how long his stadion was.",
  "लगभग 240 ईसा पूर्व में विद्वान एराटोस्थनीज़ ने, जो अलेक्ज़ेंड्रिया के महान पुस्तकालय के प्रमुख थे, मिस्र छोड़े बिना पृथ्वी का आकार निकाला। उन्हें पता चला था कि दक्षिण में स्थित साइईन में वर्ष के सबसे लंबे दिन दोपहर को सूर्य ठीक सिर के ऊपर होता है, जिससे वह एक गहरे कुएँ में सीधा नीचे तक चमकता है। उसी दिन दोपहर को अलेक्ज़ेंड्रिया में एक खड़ी छड़ी छोटी छाया डालती थी, जिससे पता चलता था कि वहाँ सूर्य सिर के ऊपर से पूरे वृत्त के लगभग पचासवें भाग जितना हटा है। यदि पृथ्वी गोल है, तो साइईन से अलेक्ज़ेंड्रिया की दूरी उसके घेरे का पचासवाँ भाग होनी चाहिए। उस दूरी को 5,000 स्टेडिया मानकर उन्होंने पृथ्वी की परिधि लगभग 2,50,000 स्टेडिया आँकी। "
  "उनकी पद्धति ठोस थी, पर वह कई मान्यताओं पर टिकी थी: कि पृथ्वी एक गोला है, कि सूर्य इतना दूर है कि उसकी किरणें दोनों नगरों तक समानांतर रेखाओं में पहुँचती हैं, और कि साइईन अलेक्ज़ेंड्रिया के ठीक दक्षिण में है -- जो वह केवल मोटे तौर पर है। उनका उत्तर सही संख्या के कितना निकट था, इस पर आज भी बहस है, क्योंकि कोई निश्चित नहीं कि उनका स्टेडियन कितना लंबा था।")
RQ(p, "Inference", "hard", "s2", ASSUME, ASSUME_HI,
   "Only 2 has been made. The passage states that the method assumed the Sun's rays reach both cities in parallel lines; only then does the angle of the shadow at Alexandria measure the arc of the Earth between the two cities. "
   "1 is the opposite of what the method needs. Parallel rays meet a curved Earth at different angles in different places -- straight down at Syene, one-fiftieth of a circle off at Alexandria -- and it is exactly that difference which reveals the Earth's size. If the angle were the same everywhere, there would be nothing to measure.",
   "केवल 2 बनाई गई है। परिच्छेद कहता है कि पद्धति ने माना कि सूर्य की किरणें दोनों नगरों तक समानांतर रेखाओं में पहुँचती हैं; तभी अलेक्ज़ेंड्रिया की छाया का कोण दोनों नगरों के बीच पृथ्वी के चाप को मापता है। "
   "1 पद्धति की आवश्यकता के ठीक उलट है। समानांतर किरणें वक्र पृथ्वी से अलग-अलग स्थानों पर अलग-अलग कोण बनाती हैं -- साइईन में सीधी नीचे, अलेक्ज़ेंड्रिया में वृत्त के पचासवें भाग जितनी हटकर -- और ठीक यही अंतर पृथ्वी का आकार बताता है। यदि कोण हर जगह एक जैसा होता, तो मापने को कुछ न होता।",
   "assumptions",
   st=["At noon on the longest day, the Sun's rays strike the ground at the same angle in every city.",
       "The Sun's rays reach Syene and Alexandria in parallel lines."],
   st_hi=["सबसे लंबे दिन की दोपहर को सूर्य की किरणें हर नगर में भूमि पर एक ही कोण से पड़ती हैं।",
          "सूर्य की किरणें साइईन और अलेक्ज़ेंड्रिया तक समानांतर रेखाओं में पहुँचती हैं।"],
   key=1)
RQ(p, "Inference", "medium", "mcq",
   "If Eratosthenes had found the Sun at Alexandria to be one-twenty-fifth of a full circle away from overhead, with the distance still 5,000 stadia, what would his method have given for the Earth's circumference?",
   "यदि एराटोस्थनीज़ ने अलेक्ज़ेंड्रिया में सूर्य को सिर के ऊपर से पूरे वृत्त का पच्चीसवाँ भाग हटा पाया होता, और दूरी फिर भी 5,000 स्टेडिया होती, तो उनकी पद्धति से पृथ्वी की परिधि क्या निकलती?",
   "On the passage's reasoning, the distance between the cities is the same fraction of the circumference as the Sun's angle is of a full circle. If 5,000 stadia were one-twenty-fifth of the way round, the circumference would be 25 × 5,000 = 125,000 stadia -- half his figure, since the angle is twice as large. "
   "250,000 keeps the old answer; 500,000 doubles it instead of halving it; 200,000 has no basis.",
   "परिच्छेद के तर्क में नगरों के बीच की दूरी परिधि का वही भाग है जो सूर्य का कोण पूरे वृत्त का है। यदि 5,000 स्टेडिया घेरे का पच्चीसवाँ भाग होते, तो परिधि 25 × 5,000 = 1,25,000 स्टेडिया होती -- उनकी संख्या का आधा, क्योंकि कोण दोगुना है। "
   "2,50,000 पुराना उत्तर रखता है; 5,00,000 उसे आधा करने के बजाय दोगुना करता है; 2,00,000 का कोई आधार नहीं।",
   "the-answer-for-a-larger-angle",
   opts=["1,25,000 stadia", "2,00,000 stadia", "2,50,000 stadia", "5,00,000 stadia"],
   opts_hi=["1,25,000 स्टेडिया", "2,00,000 स्टेडिया", "2,50,000 स्टेडिया", "5,00,000 स्टेडिया"],
   ans=0, pos=0)
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage shows how Eratosthenes turned a shadow and a distance into the size of the Earth, then notes the assumptions the method rested on and why its accuracy is still uncertain. "
   "It calls the method sound, not exact; it says Syene lies due south only roughly, not that the method failed; and it is the stadion, not the angle, whose size is unknown today.",
   "परिच्छेद दिखाता है कि एराटोस्थनीज़ ने एक छाया और एक दूरी से पृथ्वी का आकार कैसे निकाला, फिर उन मान्यताओं को बताता है जिन पर पद्धति टिकी थी और यह कि उसकी सटीकता आज भी अनिश्चित क्यों है। "
   "वह पद्धति को ठोस कहता है, सटीक नहीं; वह कहता है कि साइईन केवल मोटे तौर पर दक्षिण में है, यह नहीं कि पद्धति विफल रही; और आज अज्ञात स्टेडियन की लंबाई है, कोण नहीं।",
   "crux",
   opts=["A sound method measured the Earth, though it rested on assumptions and its accuracy is unsure.",
         "Eratosthenes found the exact size of the Earth, a figure that later measurements have only confirmed.",
         "Eratosthenes' method failed because Syene does not lie exactly due south of Alexandria.",
         "No one today can tell what angle the shadow at Alexandria made with the vertical stick."],
   opts_hi=["एक ठोस पद्धति ने पृथ्वी को मापा, पर वह मान्यताओं पर टिकी थी और उसकी सटीकता अनिश्चित है।",
            "एराटोस्थनीज़ ने पृथ्वी का ठीक आकार निकाला, जिसकी बाद के मापों ने केवल पुष्टि ही की है।",
            "एराटोस्थनीज़ की पद्धति विफल रही क्योंकि साइईन अलेक्ज़ेंड्रिया के ठीक दक्षिण में नहीं है।",
            "आज कोई नहीं बता सकता कि अलेक्ज़ेंड्रिया की छाया ने खड़ी छड़ी के साथ कौन-सा कोण बनाया था।"],
   ans=0, pos=2)

# ------------------------------------------------------------------ P10 the Dutch disease
p = passage("p10",
  "In 1959 a vast field of natural gas was discovered at Groningen in the Netherlands. Gas exports brought in a flood of foreign earnings, but in the years that followed the country's factories struggled. In 1977 the magazine The Economist gave the problem a name: the Dutch disease. When a country suddenly earns a great deal from selling a natural resource abroad, its currency tends to rise in value and wages are bid up, so its other exports become dearer for foreigners to buy. Manufacturing shrinks, and when the resource runs out or its price falls, the country may find it has lost industries that are hard to rebuild. "
  "The disease is not inevitable. Norway, which found oil in the North Sea a decade later, puts much of its oil revenue into a fund invested abroad and spends only a small part of it each year, so that the money does not flood the home economy all at once. Botswana, rich in diamonds, has also been praised for saving its windfalls. What matters, it seems, is less the resource than how the earnings from it are managed.",
  "1959 में नीदरलैंड्स के ग्रोनिंगन में प्राकृतिक गैस का एक विशाल भंडार मिला। गैस के निर्यात से विदेशी आय की बाढ़ आई, पर आगे के वर्षों में देश के कारख़ाने संघर्ष करने लगे। 1977 में पत्रिका द इकोनॉमिस्ट ने इस समस्या को एक नाम दिया: डच रोग। जब कोई देश अचानक विदेश में कोई प्राकृतिक संसाधन बेचकर बहुत कमाने लगता है, तो उसकी मुद्रा का मूल्य बढ़ने लगता है और मज़दूरी चढ़ जाती है, इसलिए उसके दूसरे निर्यात विदेशियों के लिए महँगे हो जाते हैं। विनिर्माण सिकुड़ता है, और जब संसाधन ख़त्म हो जाए या उसका मूल्य गिर जाए, तो देश पा सकता है कि उसने ऐसे उद्योग खो दिए हैं जिन्हें फिर से खड़ा करना कठिन है। "
  "यह रोग अपरिहार्य नहीं है। नॉर्वे, जिसे एक दशक बाद उत्तरी सागर में तेल मिला, अपने तेल-राजस्व का बड़ा भाग विदेश में निवेश करने वाले एक कोष में डालता है और हर वर्ष उसका केवल छोटा भाग ख़र्च करता है, ताकि धन घरेलू अर्थव्यवस्था में एक साथ न उमड़ पड़े। हीरों से समृद्ध बोत्सवाना की भी अपनी अप्रत्याशित आय बचाने के लिए प्रशंसा हुई है। ऐसा लगता है कि मायने संसाधन से अधिक इस बात के हैं कि उससे होने वाली आय का प्रबंधन कैसे होता है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage explains how a resource boom can harm a country's other industries, then shows through Norway and Botswana that careful management of the earnings can prevent it. "
   "It says the disease is not inevitable, so resource-rich countries do not always grow more slowly; it does not say the Dutch should have kept their gas; and a rising currency is presented as part of the problem, not as the source of prosperity.",
   "परिच्छेद समझाता है कि संसाधन से आई तेज़ी किसी देश के दूसरे उद्योगों को कैसे नुक़सान पहुँचा सकती है, फिर नॉर्वे और बोत्सवाना के माध्यम से दिखाता है कि आय का सावधान प्रबंधन इसे रोक सकता है। "
   "वह कहता है कि रोग अपरिहार्य नहीं, इसलिए संसाधन-समृद्ध देश सदा धीमे नहीं बढ़ते; वह यह नहीं कहता कि डचों को अपनी गैस रख लेनी चाहिए थी; और बढ़ती मुद्रा को समस्या का भाग बताया गया है, समृद्धि का स्रोत नहीं।",
   "crux",
   opts=["A resource boom can harm other industries, but managing the earnings well can prevent it.",
         "Countries that discover natural resources always grow more slowly than countries that do not.",
         "The Netherlands should never have sold any of the natural gas it found at Groningen abroad.",
         "A strong and rising currency is the main source of the prosperity of any trading nation."],
   opts_hi=["संसाधन की तेज़ी दूसरे उद्योगों को हानि पहुँचा सकती है, पर सही प्रबंधन इसे रोकता है।",
            "जिन देशों को प्राकृतिक संसाधन मिलते हैं, वे बाक़ी देशों से सदा धीमे बढ़ते हैं।",
            "नीदरलैंड्स को ग्रोनिंगन में मिली गैस का कोई भी भाग कभी विदेश में नहीं बेचना चाहिए था।",
            "मज़बूत और बढ़ती मुद्रा किसी भी व्यापारी राष्ट्र की समृद्धि का मुख्य स्रोत है।"],
   ans=0, pos=0)
RQ(p, "Inference", "hard", "mcq",
   "On the passage's reasoning, why does it help Norway to invest its oil revenue abroad and spend only a little of it each year?",
   "परिच्छेद के तर्क के अनुसार, नॉर्वे को अपना तेल-राजस्व विदेश में निवेश करने और हर वर्ष उसका थोड़ा भाग ही ख़र्च करने से क्या लाभ होता है?",
   "The disease works through the earnings pushing up the currency and wages at home, which makes other exports dear. Keeping most of the money abroad and releasing it slowly stops it from flooding the home economy at once, so those pressures stay small. "
   "The passage says nothing about foreign returns being higher, makes no link between the fund and how fast the oil runs out, and mentions no law against spending on citizens.",
   "रोग इस तरह काम करता है कि आय देश में मुद्रा और मज़दूरी को ऊपर धकेलती है, जिससे दूसरे निर्यात महँगे होते हैं। धन का अधिकांश भाग विदेश में रखकर उसे धीरे-धीरे निकालने से वह घरेलू अर्थव्यवस्था में एक साथ नहीं उमड़ता, इसलिए वे दबाव कम रहते हैं। "
   "परिच्छेद विदेशी प्रतिफल के अधिक होने के बारे में कुछ नहीं कहता, कोष और तेल के ख़त्म होने की गति में कोई संबंध नहीं जोड़ता, और नागरिकों पर ख़र्च के विरुद्ध किसी क़ानून का उल्लेख नहीं करता।",
   "why-norway-invests-abroad",
   opts=["It stops the earnings pushing up the currency and wages at home at once.",
         "Foreign investments always pay a higher return than any investment at home.",
         "It slows the rate at which Norway's oil fields in the North Sea run dry.",
         "Norway's laws do not allow oil money to be spent on its own citizens."],
   opts_hi=["यह आय को देश में मुद्रा और मज़दूरी को एक साथ ऊपर धकेलने से रोकता है।",
            "विदेशी निवेश सदा देश के किसी भी निवेश से अधिक प्रतिफल देते हैं।",
            "यह उस गति को धीमा करता है जिससे उत्तरी सागर में नॉर्वे के तेल-क्षेत्र ख़ाली होते हैं।",
            "नॉर्वे के क़ानून तेल का धन अपने ही नागरिकों पर ख़र्च करने नहीं देते।"],
   ans=0, pos=3)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Neither is valid. 1: the passage puts the Dutch factories' troubles down to the gas boom -- a dearer currency and higher wages -- not to bad management by their owners. "
   "2: the passage says plainly that the disease is not inevitable, and gives Norway and Botswana as countries rich in a resource that avoided it.",
   "कोई भी वैध नहीं। 1: परिच्छेद डच कारख़ानों की कठिनाई का कारण गैस की तेज़ी -- महँगी मुद्रा और ऊँची मज़दूरी -- को बताता है, उनके मालिकों के ख़राब प्रबंधन को नहीं। "
   "2: परिच्छेद स्पष्ट कहता है कि रोग अपरिहार्य नहीं, और नॉर्वे तथा बोत्सवाना को ऐसे संसाधन-समृद्ध देशों के रूप में देता है जो इससे बचे।",
   "conclusions",
   st=["The passage shows that the Dutch factories struggled because their owners managed them badly.",
       "On the passage's account, any country rich in a natural resource is bound to suffer the Dutch disease."],
   st_hi=["परिच्छेद दिखाता है कि डच कारख़ाने इसलिए संघर्ष करने लगे कि उनके मालिकों ने उनका प्रबंधन ख़राब किया।",
          "परिच्छेद के अनुसार, प्राकृतिक संसाधन से समृद्ध हर देश को डच रोग होना तय है।"],
   key=3)
