# -*- coding: utf-8 -*-
"""CSAT Level 4 · Simulator 4 -- Reading Comprehension: 9 passages, 27 items (3 each), Layout A.

The 2023/2024 shape again: nine passages of three items. Each passage turns -- a claim, then its limit. Themes, none
used in Levels 1-3 or Simulators 1-3: the broken window and the unseen cost, a number on a wheel that pulls an
estimate, Al-Biruni on the barriers to understanding India, Darwin's earthworms, the Amur falcons of Nagaland, the
veil of ignorance, the winter rain of western disturbances, India's railway gauges, and Ambedkar on constitutional
morality. Item types: main idea 7, best summary 1, inference 11, assumption 2, specific detail 6. Difficulty
1 easy / 16 medium / 10 hard. Options are named by content in every explanation."""
from csat_common import passage, RQ

CRUX = "Which one of the following statements best reflects the crux of the passage?"
CRUX_HI = "निम्नलिखित में से कौन-सा कथन परिच्छेद के सार को सबसे अच्छी तरह व्यक्त करता है?"
MSG = "Which one of the following statements best reflects the most logical and rational message conveyed by the passage?"
MSG_HI = "निम्नलिखित में से कौन-सा कथन परिच्छेद द्वारा दिए गए सबसे तार्किक और विवेकपूर्ण संदेश को सबसे अच्छी तरह व्यक्त करता है?"
VALID = "On the basis of the passage, which of the following conclusions is/are valid?"
VALID_HI = "परिच्छेद के आधार पर निम्नलिखित में से कौन-सा/से निष्कर्ष वैध है/हैं?"
ASSUME = "Which of the following assumptions has/have been made in the passage?"
ASSUME_HI = "परिच्छेद में निम्नलिखित में से कौन-सी पूर्वधारणा/एँ बनाई गई है/हैं?"

# ------------------------------------------------------------------ P01 the broken window and the unseen cost
p = passage("p01",
  "In 1850 the French economist Frédéric Bastiat told the story of a shopkeeper whose son breaks a pane of glass. The onlookers console him: at least the glazier will have work, and the glazier will spend what he earns, giving work to others in turn. So, they conclude, the broken window is good for trade. "
  "Bastiat called this the error of seeing only what is seen. The six francs paid to the glazier are visible. What is not visible is the pair of shoes or the book the shopkeeper would have bought with the same money, and the work that purchase would have given the shoemaker or the bookseller. The town has not gained a job; it has moved one, and lost a window. "
  "The lesson reaches beyond broken glass. Whenever an activity is praised for the work it creates -- rebuilding after a disaster, or a scheme that pays people to dig holes and fill them in again -- it is worth asking what the same resources would otherwise have done. This does not mean that spending is never useful, only that its benefits must be weighed against what is given up.",
  "1850 में फ़्रांसीसी अर्थशास्त्री फ़्रेडरिक बास्तियाँ ने एक दुकानदार की कथा सुनाई जिसका बेटा शीशे का एक पल्ला तोड़ देता है। देखने वाले उसे सांत्वना देते हैं: कम से कम शीशा लगाने वाले को काम मिलेगा, और वह अपनी कमाई ख़र्च करेगा, जिससे बदले में दूसरों को काम मिलेगा। इसलिए, वे निष्कर्ष निकालते हैं, टूटी खिड़की व्यापार के लिए अच्छी है। "
  "बास्तियाँ ने इसे केवल वही देखने की भूल कहा जो दिखाई देता है। शीशा लगाने वाले को दिए गए छह फ़्रैंक दिखाई देते हैं। जो दिखाई नहीं देता वह है जूतों की वह जोड़ी या वह पुस्तक जो दुकानदार उसी पैसे से ख़रीदता, और वह काम जो उस ख़रीद से मोची या पुस्तक-विक्रेता को मिलता। नगर ने कोई रोज़गार नहीं पाया; उसने एक रोज़गार को एक जगह से दूसरी जगह खिसकाया है, और एक खिड़की खो दी है। "
  "यह सीख टूटे शीशे से आगे तक जाती है। जब भी किसी गतिविधि की प्रशंसा उससे पैदा होने वाले काम के लिए की जाती है -- किसी आपदा के बाद पुनर्निर्माण, या कोई योजना जो लोगों को गड्ढे खोदने और फिर भरने के लिए पैसे देती है -- तो यह पूछना उचित है कि वही संसाधन अन्यथा क्या करते। इसका अर्थ यह नहीं कि ख़र्च कभी उपयोगी नहीं होता, केवल यह कि उसके लाभों को उस चीज़ के सामने तौला जाना चाहिए जिसे छोड़ा जाता है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage uses the broken window to show that the visible work an activity creates must be set against what the same money would otherwise have done, and it ends by saying that spending can be useful once that weighing is done. "
   "It rejects the claim that breaking things is good for trade; it says spending is not 'never useful', so it does not condemn all spending; and the care of windows is not its subject.",
   "परिच्छेद टूटी खिड़की के उदाहरण से दिखाता है कि किसी गतिविधि से पैदा होने वाले दिखाई देने वाले काम को इसके सामने रखना चाहिए कि वही पैसा अन्यथा क्या करता, और अंत में कहता है कि यह तौल कर लेने पर ख़र्च उपयोगी हो सकता है। "
   "वह इस दावे को ख़ारिज करता है कि चीज़ें तोड़ना व्यापार के लिए अच्छा है; वह कहता है कि ख़र्च 'कभी उपयोगी नहीं' ऐसा नहीं, इसलिए वह हर ख़र्च की निंदा नहीं करता; और खिड़कियों की देखभाल उसका विषय नहीं है।",
   "crux",
   opts=["The work an activity creates must be weighed against what the same resources would otherwise have done.",
         "Breaking and repairing things is good for an economy, because it creates work for those who repair them.",
         "Public spending never does any good, since it only moves jobs from one place in the economy to another.",
         "Shopkeepers should take more care of their windows, because repairing broken glass is very expensive."],
   opts_hi=["किसी गतिविधि से पैदा होने वाले काम को इसके सामने तौलना चाहिए कि वही संसाधन अन्यथा क्या करते।",
            "चीज़ें तोड़ना और उनकी मरम्मत करना अर्थव्यवस्था के लिए अच्छा है, क्योंकि इससे मरम्मत करने वालों को काम मिलता है।",
            "सार्वजनिक ख़र्च कभी कोई भलाई नहीं करता, क्योंकि वह केवल रोज़गार को अर्थव्यवस्था में एक जगह से दूसरी जगह खिसकाता है।",
            "दुकानदारों को अपनी खिड़कियों का अधिक ध्यान रखना चाहिए, क्योंकि टूटे शीशे की मरम्मत बहुत महँगी होती है।"],
   ans=0, pos=2)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Only 2 is valid. The case against the onlookers rests on the purchase the shopkeeper would otherwise have made: the glazier's job only replaces the shoemaker's or the bookseller's. If the money would have lain idle, nothing would have been displaced, and the claim that the town 'has not gained a job' would lose its force (though the town would still have lost a window). "
   "1 is the very error the passage describes: rebuilding after a disaster is praised for the work it creates while the loss itself and the uses the resources would otherwise have had are ignored.",
   "केवल 2 वैध है। देखने वालों के विरुद्ध तर्क उस ख़रीद पर टिका है जो दुकानदार अन्यथा करता: शीशा लगाने वाले का काम केवल मोची या पुस्तक-विक्रेता के काम की जगह लेता है। यदि पैसा अन्यथा बेकार पड़ा रहता, तो कुछ भी विस्थापित न होता, और यह दावा कि नगर ने 'कोई रोज़गार नहीं पाया' अपना बल खो देता (हालाँकि नगर फिर भी एक खिड़की खो चुका होता)। "
   "1 ठीक वही भूल है जिसका परिच्छेद वर्णन करता है: आपदा के बाद पुनर्निर्माण की प्रशंसा उससे पैदा होने वाले काम के लिए की जाती है, जबकि स्वयं हानि और संसाधनों के अन्य संभावित उपयोग अनदेखे रह जाते हैं।",
   "conclusions",
   st=["A town that is rebuilt after a disaster ends up better off than it was before the disaster struck.",
       "If the shopkeeper's money would otherwise have lain idle, the passage's case against the onlookers would be weaker."],
   st_hi=["आपदा के बाद फिर से बनाया गया नगर अंततः आपदा से पहले की तुलना में बेहतर स्थिति में होता है।",
          "यदि दुकानदार का पैसा अन्यथा बेकार पड़ा रहता, तो देखने वालों के विरुद्ध परिच्छेद का तर्क कमज़ोर होता।"],
   key=1)
RQ(p, "Inference", "medium", "mcq",
   "Which one of the following is an example of the error that the passage describes?",
   "निम्नलिखित में से कौन-सा उस भूल का उदाहरण है जिसका परिच्छेद वर्णन करता है?",
   "The error is to count the work an activity creates while ignoring what the same money would otherwise have paid for. Praising a road plan for its jobs without asking what else the money could have built does exactly that. "
   "Comparing three glaziers' prices is ordinary prudence; insisting that the person responsible pays is about who bears a cost, not about unseen alternatives; and counting both the cost of a project and its benefits is the weighing the passage recommends.",
   "भूल यह है कि किसी गतिविधि से पैदा होने वाले काम को गिना जाए और यह अनदेखा किया जाए कि वही पैसा अन्यथा किस चीज़ पर लगता। सड़क की किसी योजना की प्रशंसा उसके रोज़गारों के लिए करना, बिना यह पूछे कि उस पैसे से और क्या बन सकता था, ठीक यही करता है। "
   "तीन शीशा लगाने वालों के दाम मिलाना सामान्य समझदारी है; ज़िम्मेदार व्यक्ति से भुगतान पर ज़ोर देना इस बारे में है कि लागत कौन उठाए, अनदेखे विकल्पों के बारे में नहीं; और किसी परियोजना की लागत और उसके लाभ दोनों गिनना वही तौल है जिसकी परिच्छेद सलाह देता है।",
   "an-example-of-the-error",
   opts=["Praising a road-widening plan for the jobs it creates without asking what else the money could have built",
         "Choosing the cheapest of three glaziers after comparing the prices that each of them charges for the work",
         "Refusing to have a broken window repaired until the person who broke it has paid the full cost of the repair",
         "Counting both the money to be spent on a project and the benefits that the project is expected to bring"],
   opts_hi=["सड़क चौड़ी करने की योजना की उसके रोज़गारों के लिए प्रशंसा, बिना पूछे कि उस पैसे से और क्या बनता",
            "तीन शीशा लगाने वालों में से हर एक के दाम मिलाकर उनमें सबसे सस्ते को चुनना",
            "टूटी खिड़की की मरम्मत तब तक न करवाना जब तक उसे तोड़ने वाला व्यक्ति मरम्मत का पूरा ख़र्च स्वयं न चुका दे",
            "किसी परियोजना पर ख़र्च होने वाला पैसा और उससे मिलने वाले अपेक्षित लाभ, दोनों को गिनना"],
   ans=0, pos=0)

# ------------------------------------------------------------------ P02 a number on a wheel that pulls an estimate
p = passage("p02",
  "In a well-known experiment reported in 1974, the psychologists Amos Tversky and Daniel Kahneman spun a wheel of fortune marked from 0 to 100 in front of their subjects; unknown to the subjects, it had been rigged to stop at either 10 or 65. The subjects were asked whether the percentage of African countries in the United Nations was higher or lower than the number on the wheel, and then to estimate that percentage. Those who had seen 10 gave a median estimate of 25 per cent; those who had seen 65 gave 45. A number they took to be pure chance had pulled their judgement towards it. "
  "Such anchoring appears well beyond the laboratory. An opening price in a bargain, a figure in a headline or the sum a lawyer demands in court can shift the final number, even among people who believe they are ignoring it. Since warning people about the effect does little to remove it, a careful negotiator may do better to name the first figure, or to think deliberately of reasons why the anchor might be wrong.",
  "1974 में प्रकाशित एक प्रसिद्ध प्रयोग में मनोवैज्ञानिक एमॉस त्वेर्स्की और डेनियल काह्नमन ने अपने प्रतिभागियों के सामने 0 से 100 तक अंकित भाग्य का एक पहिया घुमाया; प्रतिभागियों को पता नहीं था कि उसे केवल 10 या 65 पर रुकने के लिए बनाया गया था। प्रतिभागियों से पूछा गया कि संयुक्त राष्ट्र में अफ़्रीकी देशों का प्रतिशत पहिये की संख्या से अधिक है या कम, और फिर उस प्रतिशत का अनुमान लगाने को कहा गया। जिन्होंने 10 देखा था उनका माध्यिका अनुमान 25 प्रतिशत था; जिन्होंने 65 देखा था उनका 45। जिस संख्या को वे शुद्ध संयोग समझ रहे थे, उसने उनके निर्णय को अपनी ओर खींच लिया। "
  "ऐसी 'लंगर' प्रवृत्ति प्रयोगशाला से बहुत बाहर भी दिखती है। मोल-भाव में पहली क़ीमत, किसी शीर्षक में दी गई संख्या या अदालत में किसी वकील द्वारा माँगी गई राशि अंतिम संख्या को खिसका सकती है, उन लोगों में भी जो मानते हैं कि वे उसे अनदेखा कर रहे हैं। चूँकि लोगों को इस प्रभाव के बारे में चेतावनी देने से वह बहुत कम हटता है, एक सावधान वार्ताकार के लिए बेहतर हो सकता है कि वह स्वयं पहली संख्या रखे, या सोच-समझकर उन कारणों पर विचार करे जिनसे लंगर ग़लत हो सकता है।")
RQ(p, "Specific Detail", "easy", "mcq",
   "According to the passage, what was striking about the estimates in the experiment?",
   "परिच्छेद के अनुसार, प्रयोग में लगाए गए अनुमानों में क्या उल्लेखनीय था?",
   "The passage says that a number the subjects 'took to be pure chance had pulled their judgement towards it': those shown 10 guessed lower than those shown 65. "
   "It does not say the estimates were accurate or that subjects refused to guess; and the group that saw the higher number gave the higher estimate, not the lower one.",
   "परिच्छेद कहता है कि जिस संख्या को प्रतिभागी 'शुद्ध संयोग समझ रहे थे, उसने उनके निर्णय को अपनी ओर खींच लिया': 10 देखने वालों ने 65 देखने वालों से कम अनुमान लगाया। "
   "वह यह नहीं कहता कि अनुमान सटीक थे या प्रतिभागियों ने अनुमान लगाने से मना किया; और ऊँची संख्या देखने वाले समूह ने ऊँचा अनुमान दिया, नीचा नहीं।",
   "what-was-striking-about-the-estimates",
   opts=["They moved towards a number the subjects took to be pure chance.",
         "They were almost exactly right, whichever number the wheel had stopped at.",
         "Most subjects refused to guess once they realised the wheel had been rigged.",
         "The subjects who saw 65 gave lower estimates than those who saw only 10."],
   opts_hi=["वे उस संख्या की ओर खिसक गए जिसे प्रतिभागी शुद्ध संयोग से आई मान रहे थे।",
            "पहिया चाहे जिस संख्या पर रुका हो, वे लगभग बिल्कुल सही थे।",
            "पहिये के बनावटी होने का पता चलते ही अधिकांश प्रतिभागियों ने अनुमान लगाने से मना कर दिया।",
            "65 देखने वाले प्रतिभागियों ने केवल 10 देखने वालों से कम अनुमान दिए।"],
   ans=0, pos=3)
RQ(p, "Inference", "medium", "mcq",
   "Which one of the following would the passage lead us to expect?",
   "परिच्छेद के आधार पर निम्नलिखित में से किसकी अपेक्षा की जानी चाहिए?",
   "Anchoring says that a first figure pulls the final one towards it, so a buyer who first hears a high asking price is likely to settle higher than one who first hears a low price for the same item. "
   "The passage says warnings do little to remove the effect, so knowing about it is no shield; it says even people who believe they are ignoring a figure can be moved, so doubting the source is no shield either; and the experiment shows a random number distorting estimates, not leaving them unchanged.",
   "लंगर प्रवृत्ति कहती है कि पहली संख्या अंतिम संख्या को अपनी ओर खींचती है, इसलिए जो ख़रीदार पहले ऊँची माँगी गई क़ीमत सुनता है, उसके उसी वस्तु के लिए नीची क़ीमत पहले सुनने वाले से अधिक पर सौदा करने की संभावना है। "
   "परिच्छेद कहता है कि चेतावनी प्रभाव को बहुत कम हटाती है, इसलिए उसके बारे में जानना कोई कवच नहीं; वह कहता है कि जो लोग मानते हैं कि वे किसी संख्या को अनदेखा कर रहे हैं वे भी प्रभावित हो सकते हैं, इसलिए स्रोत पर संदेह भी कवच नहीं; और प्रयोग दिखाता है कि यादृच्छिक संख्या अनुमानों को बिगाड़ती है, उन्हें अपरिवर्तित नहीं छोड़ती।",
   "what-the-passage-leads-us-to-expect",
   opts=["A buyer who hears a high asking price first pays more than one who hears a low price first.",
         "A buyer who has read about anchoring is no longer influenced at all by a seller's opening price.",
         "A figure printed in a headline has no effect on readers who distrust the newspaper that printed it.",
         "Estimates made just after seeing a random number are as accurate as those made without seeing one."],
   opts_hi=["जो ख़रीदार पहले ऊँची माँगी गई क़ीमत सुनता है, वह उसी वस्तु के लिए पहले नीची क़ीमत सुनने वाले से अधिक चुकाता है।",
            "लंगर प्रवृत्ति के बारे में पढ़ चुका ख़रीदार विक्रेता की पहली क़ीमत से बिल्कुल भी प्रभावित नहीं होता।",
            "किसी शीर्षक में छपी संख्या का उन पाठकों पर कोई प्रभाव नहीं पड़ता जो उसे छापने वाले समाचारपत्र पर भरोसा नहीं करते।",
            "किसी यादृच्छिक संख्या को देखने के ठीक बाद लगाए गए अनुमान उतने ही सटीक होते हैं जितने उसे देखे बिना लगाए गए।"],
   ans=0, pos=2)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Only 1 is valid. The subjects took the wheel's number to be chance, and it still moved their estimates; so believing a number to be random did not protect them. "
   "2 cannot be concluded: the passage gives the two groups' median estimates but never the true percentage, so it does not say whether either group was too high or too low. It shows only that the two groups differed.",
   "केवल 1 वैध है। प्रतिभागी पहिये की संख्या को संयोग मान रहे थे, और फिर भी उसने उनके अनुमानों को खिसका दिया; इसलिए किसी संख्या को यादृच्छिक मानने ने उन्हें नहीं बचाया। "
   "2 का निष्कर्ष नहीं निकाला जा सकता: परिच्छेद दोनों समूहों के माध्यिका अनुमान देता है पर वास्तविक प्रतिशत कभी नहीं, इसलिए वह यह नहीं कहता कि कोई समूह बहुत ऊपर था या बहुत नीचे। वह केवल यह दिखाता है कि दोनों समूह अलग थे।",
   "conclusions",
   st=["Believing that a number has been produced by pure chance does not stop a person from being influenced by it.",
       "In the experiment, the subjects who saw 65 overestimated the true percentage, and those who saw 10 underestimated it."],
   st_hi=["किसी संख्या को शुद्ध संयोग से आई मानना किसी व्यक्ति को उससे प्रभावित होने से नहीं रोकता।",
          "प्रयोग में 65 देखने वाले प्रतिभागियों ने वास्तविक प्रतिशत को बढ़ाकर आँका, और 10 देखने वालों ने घटाकर।"],
   key=0)

# ------------------------------------------------------------------ P03 Al-Biruni on the barriers to understanding
p = passage("p03",
  "Al-Biruni was born in 973 in Khwarizm, in Central Asia. Taken to Ghazni by Sultan Mahmud in 1017, he later spent years among Brahmana scholars in the Punjab, learning Sanskrit, and wrote in Arabic a long account of India, the Kitab-ul-Hind. "
  "He was unusually aware of how hard it is to understand a society from outside, and he named three barriers. The first was language: Sanskrit differed so much from Arabic and Persian that ideas could not easily be carried from one to the other. The second was the difference in religious beliefs and practices. The third was the self-absorption of the local people, which he felt made them unwilling to share what they knew with outsiders. "
  "To overcome these, he relied heavily on Sanskrit texts, and he looked for parallels in societies his readers knew, noting, for instance, that ancient Persia too had recognised four social categories. His account is valuable not because it is free of bias -- built on texts that laid down how society ought to be ordered, it often presents that ideal rather than everyday practice -- but because he named his difficulties openly.",
  "अल-बिरूनी का जन्म 973 में मध्य एशिया के ख़्वारिज़्म में हुआ था। 1017 में सुल्तान महमूद द्वारा ग़ज़नी ले जाए जाने के बाद उसने वर्षों तक पंजाब में ब्राह्मण विद्वानों के बीच रहकर संस्कृत सीखी, और अरबी में भारत का एक लंबा विवरण, किताब-उल-हिंद, लिखा। "
  "वह असाधारण रूप से जानता था कि किसी समाज को बाहर से समझना कितना कठिन है, और उसने तीन बाधाएँ बताईं। पहली भाषा थी: संस्कृत अरबी और फ़ारसी से इतनी भिन्न थी कि विचारों को एक से दूसरी में आसानी से नहीं ले जाया जा सकता था। दूसरी धार्मिक विश्वासों और प्रथाओं का अंतर थी। तीसरी स्थानीय लोगों का आत्म-केंद्रित होना थी, जिसके कारण, उसे लगा, वे जो जानते थे उसे बाहरी लोगों के साथ बाँटना नहीं चाहते थे। "
  "इन पर पार पाने के लिए वह संस्कृत ग्रंथों पर बहुत निर्भर रहा, और उसने अपने पाठकों के परिचित समाजों में समानताएँ खोजीं, उदाहरण के लिए यह बताते हुए कि प्राचीन फ़ारस में भी चार सामाजिक वर्ग माने गए थे। उसका विवरण इसलिए मूल्यवान नहीं कि वह पूर्वाग्रह से मुक्त है -- उन ग्रंथों पर आधारित होने के कारण जो बताते थे कि समाज को कैसे व्यवस्थित होना चाहिए, वह प्रायः रोज़मर्रा के व्यवहार के बजाय उस आदर्श को प्रस्तुत करता है -- बल्कि इसलिए कि उसने अपनी कठिनाइयों को खुलकर बताया।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage presents Al-Biruni as a careful outsider who named the barriers to understanding India, and it values his account for that frankness while warning that his reliance on prescriptive texts shaped what he described. "
   "It says outright that the account is not free of bias; he learnt Sanskrit, so he did not fail for want of the language; and nothing suggests that he wrote to praise Mahmud's campaigns.",
   "परिच्छेद अल-बिरूनी को एक सावधान बाहरी व्यक्ति के रूप में प्रस्तुत करता है जिसने भारत को समझने की बाधाएँ बताईं, और उसके विवरण को इसी स्पष्टवादिता के लिए मूल्यवान मानता है, यह चेतावनी देते हुए कि नियम बताने वाले ग्रंथों पर उसकी निर्भरता ने उसके वर्णन को आकार दिया। "
   "वह साफ़ कहता है कि विवरण पूर्वाग्रह से मुक्त नहीं है; उसने संस्कृत सीखी, इसलिए वह भाषा के अभाव में विफल नहीं हुआ; और कुछ भी यह नहीं बताता कि उसने महमूद के अभियानों की प्रशंसा के लिए लिखा।",
   "crux",
   opts=["Al-Biruni's account is valuable partly because he was frank about what made India hard to understand.",
         "Al-Biruni's account gives an unbiased picture of how ordinary people in India actually lived and worked.",
         "Al-Biruni could not understand India at all, because he never learnt any of the languages spoken there.",
         "Al-Biruni wrote his account of India mainly in order to praise the military campaigns of Sultan Mahmud."],
   opts_hi=["अल-बिरूनी का विवरण कुछ हद तक इसलिए मूल्यवान है कि उसने खुलकर बताया कि भारत को समझना किन कारणों से कठिन था।",
            "अल-बिरूनी का विवरण इस बात की पूर्वाग्रह-रहित तस्वीर देता है कि भारत के सामान्य लोग वास्तव में कैसे रहते और काम करते थे।",
            "अल-बिरूनी भारत को बिल्कुल नहीं समझ सका, क्योंकि उसने वहाँ बोली जाने वाली कोई भी भाषा कभी नहीं सीखी।",
            "अल-बिरूनी ने भारत का अपना विवरण मुख्यतः सुल्तान महमूद के सैन्य अभियानों की प्रशंसा के लिए लिखा।"],
   ans=0, pos=0)
RQ(p, "Specific Detail", "medium", "mcq",
   "Which one of the following was NOT among the barriers that, according to the passage, Al-Biruni named?",
   "परिच्छेद के अनुसार, निम्नलिखित में से कौन-सी उन बाधाओं में से नहीं थी जो अल-बिरूनी ने बताईं?",
   "The three barriers were language, differences of religious belief and practice, and the local people's unwillingness to share knowledge with outsiders. A lack of written sources was not one of them: he relied heavily on Sanskrit texts. "
   "The other three options restate the barriers he named.",
   "तीन बाधाएँ थीं भाषा, धार्मिक विश्वास और प्रथा के अंतर, और स्थानीय लोगों की बाहरी लोगों से ज्ञान बाँटने की अनिच्छा। लिखित स्रोतों का अभाव उनमें से नहीं था: वह संस्कृत ग्रंथों पर बहुत निर्भर रहा। "
   "अन्य तीन विकल्प उसकी बताई बाधाओं को ही दोहराते हैं।",
   "a-barrier-he-did-not-name",
   opts=["A shortage of written works about Indian society",
         "How far Sanskrit differed from Arabic and Persian",
         "Differences in religious beliefs and practices",
         "The reluctance of local people to share what they knew"],
   opts_hi=["भारतीय समाज के बारे में लिखित ग्रंथों की कमी",
            "संस्कृत का अरबी और फ़ारसी से इतना अधिक भिन्न होना",
            "धार्मिक विश्वासों और प्रथाओं में अंतर",
            "स्थानीय लोगों का अपना ज्ञान बाँटने में संकोच"],
   ans=0, pos=3)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Both are valid. The passage says Al-Biruni's account, built on texts about how society ought to be ordered, often presents that ideal rather than everyday practice -- so a historian would do well to check what it says about daily life against other evidence (1). "
   "And it says he looked for parallels in societies his readers knew, such as ancient Persia's four categories: a way of making the unfamiliar easier for them to grasp (2).",
   "दोनों वैध हैं। परिच्छेद कहता है कि अल-बिरूनी का विवरण, इस बारे में ग्रंथों पर आधारित होने के कारण कि समाज को कैसे व्यवस्थित होना चाहिए, प्रायः रोज़मर्रा के व्यवहार के बजाय उस आदर्श को प्रस्तुत करता है -- इसलिए इतिहासकार के लिए अच्छा होगा कि वह दैनिक जीवन के बारे में उसकी बातों को अन्य साक्ष्यों से मिलाए (1)। "
   "और वह कहता है कि उसने अपने पाठकों के परिचित समाजों में समानताएँ खोजीं, जैसे प्राचीन फ़ारस के चार वर्ग: अपरिचित को उनके लिए समझना आसान बनाने का एक तरीक़ा (2)।",
   "conclusions",
   st=["A historian using Al-Biruni's account should check what it says about everyday life against other kinds of evidence.",
       "Al-Biruni drew comparisons with societies familiar to his readers to help them understand what was unfamiliar."],
   st_hi=["अल-बिरूनी के विवरण का उपयोग करने वाले इतिहासकार को रोज़मर्रा के जीवन के बारे में उसकी बातों को अन्य प्रकार के साक्ष्यों से मिलाना चाहिए।",
          "अल-बिरूनी ने अपने पाठकों के परिचित समाजों से तुलना की, ताकि उन्हें अपरिचित बातें समझने में सहायता मिले।"],
   key=2)

# ------------------------------------------------------------------ P04 Darwin's earthworms
p = passage("p04",
  "Charles Darwin's last book, published in 1881, the year before his death, was about earthworms. Over some forty years he had watched them in his garden and fields, measured the soil they brought up, and even tested whether they responded to sound by having music played to them; they responded to vibration, not to sound. "
  "He found that worms swallow soil, pass it through their bodies and leave it on the surface as fine castings, so that over the years stones and the remains of old buildings sink slowly beneath a layer of new earth. Each worm moves very little, but there are so many of them, working year after year, that the whole of a field's topsoil passes through their bodies again and again over the centuries. "
  "The book sold well, and it showed a way of thinking that ran through all of Darwin's work: that small causes, repeated over long periods, can produce large effects. It is a habit of mind easily lost whenever we judge a force by how dramatic it looks rather than by how long it acts.",
  "चार्ल्स डार्विन की अंतिम पुस्तक, जो 1881 में, उनकी मृत्यु से एक वर्ष पहले, प्रकाशित हुई, केंचुओं के बारे में थी। लगभग चालीस वर्षों तक उन्होंने अपने बग़ीचे और खेतों में उन्हें देखा था, उनके द्वारा ऊपर लाई गई मिट्टी नापी थी, और यह भी परखा था कि क्या वे ध्वनि पर प्रतिक्रिया करते हैं, उनके लिए संगीत बजवाकर; वे कंपन पर प्रतिक्रिया करते थे, ध्वनि पर नहीं। "
  "उन्होंने पाया कि केंचुए मिट्टी निगलते हैं, उसे अपने शरीर से गुज़ारते हैं और सतह पर महीन विष्ठा के रूप में छोड़ देते हैं, जिससे वर्षों में पत्थर और पुरानी इमारतों के अवशेष धीरे-धीरे नई मिट्टी की परत के नीचे धँसते जाते हैं। हर केंचुआ बहुत कम चलता है, पर वे इतने अधिक हैं, और वर्ष-दर-वर्ष काम करते हैं, कि सदियों में किसी खेत की पूरी ऊपरी मिट्टी बार-बार उनके शरीर से होकर गुज़रती है। "
  "पुस्तक ख़ूब बिकी, और उसने सोचने का वह ढंग दिखाया जो डार्विन के पूरे काम में चलता है: कि छोटे कारण, लंबे समय तक दोहराए जाने पर, बड़े प्रभाव पैदा कर सकते हैं। सोचने की यह आदत तब आसानी से छूट जाती है जब भी हम किसी शक्ति को इससे आँकते हैं कि वह कितनी नाटकीय दिखती है, इससे नहीं कि वह कितने समय तक काम करती है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage uses Darwin's study of worms to make a general point: tiny effects repeated over a long time can reshape the land, and we underrate such forces when we look only for the dramatic. "
   "It does not rank worms above all other animals; it says the book 'sold well', not that it outsold his other books; and it warns against judging forces by how dramatic they look, the opposite of saying dramatic forces always matter more.",
   "परिच्छेद डार्विन के केंचुओं के अध्ययन से एक सामान्य बात कहता है: लंबे समय तक दोहराए गए बहुत छोटे प्रभाव भूमि को नया रूप दे सकते हैं, और जब हम केवल नाटकीय चीज़ें खोजते हैं तो ऐसी शक्तियों को कम आँकते हैं। "
   "वह केंचुओं को अन्य सभी जीवों से ऊपर नहीं रखता; वह कहता है कि पुस्तक 'ख़ूब बिकी', यह नहीं कि वह उनकी अन्य पुस्तकों से अधिक बिकी; और वह शक्तियों को उनके नाटकीय दिखने से आँकने के विरुद्ध चेतावनी देता है, जो यह कहने का उलटा है कि नाटकीय शक्तियाँ हमेशा अधिक मायने रखती हैं।",
   "crux",
   opts=["Earthworms are the most important of all the animals for the health of the soil in a farmer's field.",
         "Small effects repeated over a long time can add up to large changes, as Darwin's worms show.",
         "Darwin's book on earthworms was more popular with readers than any other book that he ever wrote.",
         "Forces that look dramatic always do more to shape the surface of the Earth than gradual ones can do."],
   opts_hi=["किसी किसान के खेत की मिट्टी के स्वास्थ्य के लिए केंचुए धरती के सभी जीवों में सबसे अधिक महत्त्वपूर्ण हैं।",
            "लंबे समय तक दोहराए गए छोटे प्रभाव मिलकर बड़े परिवर्तन ला सकते हैं, जैसा डार्विन के केंचुए दिखाते हैं।",
            "केंचुओं पर डार्विन की पुस्तक पाठकों में उनकी लिखी किसी भी अन्य पुस्तक से अधिक लोकप्रिय थी।",
            "नाटकीय दिखने वाली शक्तियाँ पृथ्वी की सतह को आकार देने में हमेशा धीमी शक्तियों से अधिक काम करती हैं।"],
   ans=1, pos=1)
RQ(p, "Inference", "hard", "mcq",
   "Which one of the following shows the error that the passage warns against in its last sentence?",
   "निम्नलिखित में से कौन-सा उस भूल को दिखाता है जिसके विरुद्ध परिच्छेद अपने अंतिम वाक्य में चेतावनी देता है?",
   "The warning is against judging a force by how dramatic it looks rather than by how long it acts. Dismissing the steady loss of a hillside's topsoil because no single storm removes much of it is exactly that error: each storm is small, but the loss accumulates. "
   "Studying one earthquake closely is not a judgement about which forces matter; measuring castings over years is Darwin's own method; and testing worms' responses is part of his careful observation, not an error.",
   "चेतावनी किसी शक्ति को इससे आँकने के विरुद्ध है कि वह कितनी नाटकीय दिखती है, इससे नहीं कि वह कितने समय तक काम करती है। किसी पहाड़ी ढलान की ऊपरी मिट्टी के लगातार बहने को इसलिए नकारना कि कोई एक तूफ़ान उसका अधिक भाग नहीं बहाता, ठीक यही भूल है: हर तूफ़ान छोटा है, पर हानि जुड़ती जाती है। "
   "एक भूकंप का बारीकी से अध्ययन यह निर्णय नहीं कि कौन-सी शक्तियाँ मायने रखती हैं; वर्षों तक विष्ठा नापना डार्विन की अपनी पद्धति है; और केंचुओं की प्रतिक्रियाएँ परखना उनके सावधान अवलोकन का भाग है, भूल नहीं।",
   "the-error-in-the-last-sentence",
   opts=["Studying a single violent earthquake in great detail to learn exactly how the ground moved during it",
         "Measuring the soil that worms bring to the surface over several years to estimate their total effect",
         "Testing whether worms respond to music, to other sounds or to the vibration of the ground beneath them",
         "Ignoring the slow loss of a hillside's soil because no single rainstorm washes much of it away"],
   opts_hi=["किसी एक प्रचंड भूकंप का बहुत विस्तार से अध्ययन करना ताकि ठीक-ठीक पता चले कि उसमें ज़मीन कैसे हिली",
            "केंचुओं द्वारा कई वर्षों में सतह पर लाई गई मिट्टी नापकर उनके कुल प्रभाव का अनुमान लगाना",
            "यह परखना कि केंचुए संगीत, अन्य ध्वनियों या अपने नीचे की ज़मीन के कंपन पर प्रतिक्रिया करते हैं या नहीं",
            "किसी ढलान की मिट्टी के धीमे बहाव को इसलिए अनदेखा करना कि कोई एक वर्षा उसका अधिक भाग नहीं बहाती"],
   ans=3, pos=3)
RQ(p, "Specific Detail", "medium", "s2", VALID, VALID_HI,
   "Only 2 is valid. The passage says worms leave swallowed soil on the surface as castings, so that stones and old remains sink beneath a layer of new earth: objects are buried from above. "
   "1 reverses this: the worms bring soil up to the surface; they do not carry surface soil down to bury it.",
   "केवल 2 वैध है। परिच्छेद कहता है कि केंचुए निगली हुई मिट्टी को सतह पर विष्ठा के रूप में छोड़ते हैं, जिससे पत्थर और पुराने अवशेष नई मिट्टी की परत के नीचे धँस जाते हैं: वस्तुएँ ऊपर से दबती हैं। "
   "1 इसे उलट देता है: केंचुए मिट्टी को ऊपर सतह पर लाते हैं; वे सतह की मिट्टी को नीचे ले जाकर नहीं दबाते।",
   "conclusions",
   st=["According to the passage, worms carry soil down from the surface and bury it deep in the ground.",
       "Objects lying on the ground slowly become buried because worms deposit fresh soil on the surface around and above them."],
   st_hi=["परिच्छेद के अनुसार केंचुए सतह से मिट्टी नीचे ले जाते हैं और उसे ज़मीन में गहरे दबा देते हैं।",
          "ज़मीन पर पड़ी वस्तुएँ धीरे-धीरे इसलिए दब जाती हैं कि केंचुए उनके आसपास और ऊपर सतह पर ताज़ी मिट्टी जमा करते हैं।"],
   key=1)

# ------------------------------------------------------------------ P05 the Amur falcons of Nagaland
p = passage("p05",
  "Every autumn, tens of thousands of Amur falcons -- small birds of prey that breed in eastern Asia -- stop in Nagaland on their way to southern Africa, on one of the longest migrations of any bird of prey. In 2012, reports that villagers around the Doyang reservoir were trapping the birds in great numbers, for food and for sale, drew wide attention. "
  "What followed is often cited as a conservation success. Rather than relying only on bans and patrols, the forest department and conservation groups worked with village councils; some former hunters became guards and guides; schoolchildren formed eco-clubs; and villages such as Pangti came to see the falcons as a source of pride and of visitors. Within a few years the killing had largely stopped. "
  "The lesson is not that laws are useless -- hunting the falcons had been illegal throughout -- but that a law a community accepts does far more than one merely imposed on it. Protection lasts when the people who live beside a species gain more from its survival than from its loss.",
  "हर शरद ऋतु में दसियों हज़ार अमूर बाज़ -- शिकारी पक्षियों की एक छोटी जाति जो पूर्वी एशिया में प्रजनन करती है -- दक्षिणी अफ़्रीका की ओर जाते हुए नागालैंड में रुकते हैं, किसी भी शिकारी पक्षी के सबसे लंबे प्रवासों में से एक पर। 2012 में इन ख़बरों ने व्यापक ध्यान खींचा कि दोयांग जलाशय के आसपास के ग्रामीण इन पक्षियों को भोजन और बिक्री के लिए भारी संख्या में फँसा रहे थे। "
  "उसके बाद जो हुआ उसे प्रायः संरक्षण की एक सफलता के रूप में उद्धृत किया जाता है। केवल प्रतिबंधों और गश्त पर निर्भर रहने के बजाय वन विभाग और संरक्षण समूहों ने ग्राम परिषदों के साथ काम किया; कुछ पूर्व शिकारी रक्षक और मार्गदर्शक बन गए; स्कूली बच्चों ने इको-क्लब बनाए; और पांग्ती जैसे गाँव बाज़ों को गर्व और पर्यटकों का स्रोत मानने लगे। कुछ ही वर्षों में हत्याएँ लगभग रुक गईं। "
  "सीख यह नहीं कि क़ानून बेकार हैं -- बाज़ों का शिकार पूरे समय अवैध था -- बल्कि यह कि जिस क़ानून को समुदाय स्वीकार करता है वह केवल थोपे गए क़ानून से कहीं अधिक करता है। संरक्षण तब टिकता है जब किसी प्रजाति के पास रहने वाले लोगों को उसके नष्ट होने से अधिक उसके बचे रहने से लाभ हो।")
RQ(p, "Main Idea", "medium", "mcq", MSG, MSG_HI,
   "The passage credits the turnaround to working with the community -- councils, former hunters, schools, villages that gained from the birds -- and concludes that protection lasts when local people gain from a species' survival. "
   "It says the lesson is 'not that laws are useless'; it calls the falcons' journey one of the longest of any bird of prey, not the longest of any bird; and it says nothing about fishing.",
   "परिच्छेद इस बदलाव का श्रेय समुदाय के साथ काम करने को देता है -- परिषदें, पूर्व शिकारी, स्कूल, वे गाँव जिन्हें पक्षियों से लाभ हुआ -- और निष्कर्ष निकालता है कि संरक्षण तब टिकता है जब स्थानीय लोगों को किसी प्रजाति के बचे रहने से लाभ हो। "
   "वह कहता है कि सीख 'यह नहीं कि क़ानून बेकार हैं'; वह बाज़ों की यात्रा को किसी भी शिकारी पक्षी की सबसे लंबी यात्राओं में से एक कहता है, किसी भी पक्षी की सबसे लंबी नहीं; और वह मछली पकड़ने के बारे में कुछ नहीं कहता।",
   "message",
   opts=["Laws against hunting are useless and ought to be replaced everywhere by campaigns of awareness.",
         "The Amur falcon makes the longest migration of any bird in the world, from eastern Asia to Africa.",
         "Conservation works best when the people who live beside a species gain from protecting it.",
         "Birds that pass through a region cannot be protected there unless all fishing in it is stopped."],
   opts_hi=["शिकार के विरुद्ध क़ानून बेकार हैं और उन्हें हर जगह जागरूकता अभियानों से बदल दिया जाना चाहिए।",
            "अमूर बाज़ पूर्वी एशिया से अफ़्रीका तक दुनिया के किसी भी पक्षी का सबसे लंबा प्रवास करता है।",
            "संरक्षण सबसे अच्छा तब काम करता है जब किसी प्रजाति के पास रहने वालों को उसकी रक्षा से लाभ हो।",
            "किसी क्षेत्र से गुज़रने वाले पक्षियों की वहाँ रक्षा तब तक नहीं हो सकती जब तक वहाँ हर तरह की मछली पकड़ना बंद न हो।"],
   ans=2, pos=2)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Only 1 is valid. Hunting the falcons was illegal throughout, yet in 2012 villagers were trapping them in great numbers: a law can exist without being obeyed. "
   "2 goes too far. The passage says the forest department relied 'not only' on bans and patrols, which means they were still used alongside the work with villages; nothing suggests that enforcement can be dropped wherever a community values a species.",
   "केवल 1 वैध है। बाज़ों का शिकार पूरे समय अवैध था, फिर भी 2012 में ग्रामीण उन्हें भारी संख्या में फँसा रहे थे: क़ानून हो सकता है और उसका पालन न हो। "
   "2 बहुत आगे जाता है। परिच्छेद कहता है कि वन विभाग 'केवल' प्रतिबंधों और गश्त पर निर्भर नहीं रहा, जिसका अर्थ है कि गाँवों के साथ काम के साथ-साथ उनका भी उपयोग होता रहा; कुछ भी यह नहीं बताता कि जहाँ भी कोई समुदाय किसी प्रजाति को महत्त्व दे वहाँ प्रवर्तन छोड़ा जा सकता है।",
   "conclusions",
   st=["The killing reported in 2012 shows that a law can be in force without being obeyed.",
       "Once a community values a species, patrols and penalties are no longer needed to protect it anywhere."],
   st_hi=["2012 में बताई गई हत्याएँ दिखाती हैं कि कोई क़ानून लागू रहते हुए भी माना न जाए, ऐसा हो सकता है।",
          "जब कोई समुदाय किसी प्रजाति को महत्त्व देने लगे, तो उसकी रक्षा के लिए कहीं भी गश्त और दंड की आवश्यकता नहीं रहती।"],
   key=0)
RQ(p, "Inference", "medium", "mcq",
   "Which one of the following, if true, would most strengthen the passage's explanation of why the killing stopped?",
   "निम्नलिखित में से कौन-सा, यदि सत्य हो, हत्याएँ रुकने की परिच्छेद की व्याख्या को सबसे अधिक मज़बूत करेगा?",
   "The passage explains the change by what villages came to gain from the living birds. If villages that earned from falcon-watching visitors stopped hunting sooner than others, the timing would match that explanation. "
   "A sharp rise in patrols would point instead to enforcement; a new route avoiding Nagaland would mean there were simply fewer birds to kill; and a rise in the price of trapped falcons would, if anything, make hunting more tempting.",
   "परिच्छेद बदलाव को इस बात से समझाता है कि गाँवों को जीवित पक्षियों से क्या लाभ होने लगा। यदि बाज़ देखने आने वाले पर्यटकों से कमाने वाले गाँवों ने अन्य गाँवों से पहले शिकार बंद किया, तो समय उस व्याख्या से मेल खाएगा। "
   "गश्त में तेज़ वृद्धि इसके बजाय प्रवर्तन की ओर संकेत करेगी; नागालैंड से बचने वाला नया मार्ग यह अर्थ देगा कि मारने के लिए पक्षी ही कम थे; और फँसाए गए बाज़ों के दाम में वृद्धि, यदि कुछ करती, तो शिकार को और लुभावना बनाती।",
   "what-strengthens-the-explanation",
   opts=["Villages that earned from falcon-watching visitors stopped hunting sooner than those that did not.",
         "The number of forest patrols around the reservoir was increased sharply in the year after the reports.",
         "Most Amur falcons now fly a shorter route to Africa that avoids Nagaland and the Doyang reservoir.",
         "The price paid for trapped falcons in the local markets rose steadily in the years after 2012."],
   opts_hi=["बाज़ देखने आने वाले पर्यटकों से कमाने वाले गाँवों ने बाक़ी गाँवों से पहले शिकार बंद किया।",
            "ख़बरों के बाद के वर्ष में जलाशय के आसपास वन विभाग की गश्त की संख्या तेज़ी से बढ़ा दी गई।",
            "अधिकांश अमूर बाज़ अब अफ़्रीका तक एक छोटे मार्ग से उड़ते हैं जो नागालैंड और दोयांग जलाशय से बचता है।",
            "2012 के बाद के वर्षों में स्थानीय बाज़ारों में फँसाए गए बाज़ों का दाम लगातार बढ़ता गया।"],
   ans=0, pos=0)

# ------------------------------------------------------------------ P06 the veil of ignorance
p = passage("p06",
  "How should the basic rules of a society be chosen? In A Theory of Justice, published in 1971, the philosopher John Rawls proposed a thought experiment. Imagine choosing the rules from behind a 'veil of ignorance': you do not know whether you will be born rich or poor, healthy or disabled, into the majority or a minority, or what talents you will have. Unable to tilt the rules in your own favour, you would have to choose rules you could accept whatever your place turned out to be. "
  "Rawls argued that people in this position would insist on equal basic liberties for all, and would allow inequalities of income and wealth only if they worked to the benefit of the least advantaged -- for instance, by rewarding effort and skill that make everyone better off. "
  "Critics reply that people might instead gamble on being among the lucky, and that the veil strips away the very loyalties and commitments that make us who we are. Yet even many critics grant the idea's use as a test of fairness: a rule we would reject if we did not know who we were is hard to defend once we do.",
  "किसी समाज के मूल नियम कैसे चुने जाने चाहिए? 1971 में प्रकाशित 'ए थ्योरी ऑफ़ जस्टिस' में दार्शनिक जॉन रॉल्स ने एक विचार-प्रयोग प्रस्तावित किया। कल्पना कीजिए कि आप नियम 'अज्ञान के पर्दे' के पीछे से चुन रहे हैं: आप नहीं जानते कि आप धनी पैदा होंगे या निर्धन, स्वस्थ या दिव्यांग, बहुसंख्यक में या किसी अल्पसंख्यक में, या आपमें कौन-सी प्रतिभाएँ होंगी। नियमों को अपने पक्ष में झुकाने में असमर्थ होकर आपको ऐसे नियम चुनने होंगे जिन्हें आप स्वीकार कर सकें, चाहे आपका स्थान जो भी निकले। "
  "रॉल्स का तर्क था कि इस स्थिति में लोग सबके लिए समान मूल स्वतंत्रताओं पर ज़ोर देंगे, और आय और संपत्ति की असमानताओं की अनुमति केवल तभी देंगे जब वे सबसे वंचित लोगों के लाभ के लिए काम करें -- उदाहरण के लिए, उस प्रयास और कौशल को पुरस्कृत करके जो सबकी स्थिति बेहतर बनाते हैं। "
  "आलोचक उत्तर देते हैं कि लोग इसके बजाय भाग्यशाली लोगों में होने का दाँव लगा सकते हैं, और यह पर्दा उन्हीं निष्ठाओं और प्रतिबद्धताओं को हटा देता है जो हमें वह बनाती हैं जो हम हैं। फिर भी कई आलोचक भी इस विचार को निष्पक्षता की कसौटी के रूप में उपयोगी मानते हैं: जिस नियम को हम यह न जानते हुए ठुकरा देते कि हम कौन हैं, उसका बचाव यह जान लेने के बाद कठिन है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage sets out Rawls's thought experiment and his conclusions, notes two criticisms, and ends on what survives them: imagining that one does not know one's own place is a useful test of whether a rule is fair. "
   "Rawls allows inequalities that benefit the least advantaged, so he does not call all inequality unjust; the critics' gamble is offered as an objection, not as something shown; and rewarding the most talented for its own sake is not what the passage describes.",
   "परिच्छेद रॉल्स का विचार-प्रयोग और उनके निष्कर्ष बताता है, दो आलोचनाओं का उल्लेख करता है, और उस पर समाप्त होता है जो उनके बाद भी बचता है: यह कल्पना करना कि हम अपना स्थान नहीं जानते, यह परखने की उपयोगी कसौटी है कि कोई नियम निष्पक्ष है या नहीं। "
   "रॉल्स उन असमानताओं की अनुमति देते हैं जो सबसे वंचितों को लाभ पहुँचाएँ, इसलिए वे हर असमानता को अन्यायपूर्ण नहीं कहते; आलोचकों का दाँव एक आपत्ति के रूप में रखा गया है, सिद्ध की गई बात के रूप में नहीं; और सबसे प्रतिभाशाली को केवल इसलिए पुरस्कृत करना वह नहीं जो परिच्छेद बताता है।",
   "crux",
   opts=["All inequalities of income and wealth are unjust and should be removed by the rules of a fair society.",
         "People choosing behind a veil of ignorance would gamble on being lucky, as Rawls's critics have shown.",
         "A just society is one whose rules give the largest rewards to those who have the greatest talents.",
         "Asking which rules we would accept without knowing our place in society is a useful test of fairness."],
   opts_hi=["आय और संपत्ति की सभी असमानताएँ अन्यायपूर्ण हैं और किसी निष्पक्ष समाज के नियमों द्वारा हटाई जानी चाहिए।",
            "अज्ञान के पर्दे के पीछे चुनने वाले लोग भाग्यशाली होने का दाँव लगाएँगे, जैसा रॉल्स के आलोचकों ने सिद्ध किया है।",
            "न्यायपूर्ण समाज वह है जिसके नियम सबसे बड़ी प्रतिभा वालों को सबसे बड़े पुरस्कार देते हैं।",
            "यह पूछना कि समाज में अपना स्थान जाने बिना हम कौन-से नियम स्वीकार करेंगे, निष्पक्षता की एक उपयोगी कसौटी है।"],
   ans=3, pos=3)
RQ(p, "Inference", "hard", "mcq",
   "Which one of the following arrangements would Rawls's principles, as the passage describes them, allow?",
   "परिच्छेद में वर्णित रॉल्स के सिद्धांत निम्नलिखित में से किस व्यवस्था की अनुमति देंगे?",
   "Rawls allows an inequality of income only if it works to the benefit of the least advantaged, and never at the cost of equal basic liberties. Higher pay for doctors that draws more people into medicine and so improves the care the poorest receive meets that test. "
   "Higher pay for a group because it is the majority benefits the majority, not the least advantaged; a property qualification for voting takes away an equal basic liberty, whatever it does to average wealth; and lower wages for a minority to raise the majority's average harms those who are already worse off.",
   "रॉल्स आय की असमानता की अनुमति केवल तभी देते हैं जब वह सबसे वंचितों के लाभ के लिए काम करे, और समान मूल स्वतंत्रताओं की क़ीमत पर कभी नहीं। डॉक्टरों का ऊँचा वेतन जो अधिक लोगों को चिकित्सा की ओर खींचे और इस तरह सबसे निर्धनों को मिलने वाली देखभाल सुधारे, इस कसौटी पर खरा उतरता है। "
   "किसी समूह को बहुसंख्यक होने के कारण ऊँचा वेतन बहुसंख्यकों को लाभ देता है, सबसे वंचितों को नहीं; मतदान के लिए संपत्ति की शर्त एक समान मूल स्वतंत्रता छीन लेती है, औसत संपत्ति पर उसका प्रभाव जो भी हो; और बहुसंख्यकों का औसत बढ़ाने के लिए किसी अल्पसंख्यक की कम मज़दूरी उन्हें हानि पहुँचाती है जो पहले से ही बदतर स्थिति में हैं।",
   "an-inequality-rawls-would-allow",
   opts=["Paying one group more than others simply because that group makes up the majority of the population",
         "Higher pay for doctors, if it draws more people into medicine and so improves care for the poorest",
         "Letting only owners of property vote, if doing so would make the country richer on average",
         "Paying a minority lower wages, if doing so raised the average income of everyone else in the country"],
   opts_hi=["किसी समूह को दूसरों से अधिक वेतन केवल इसलिए देना कि वह समूह जनसंख्या का बहुमत है",
            "डॉक्टरों को ऊँचा वेतन, यदि वह अधिक लोगों को चिकित्सा में लाए और निर्धनतम की देखभाल सुधारे",
            "केवल संपत्ति के स्वामियों को मतदान का अधिकार देना, यदि ऐसा करने से पूरा देश औसतन अधिक धनी हो जाए",
            "किसी अल्पसंख्यक को कम मज़दूरी देना, यदि ऐसा करने से देश के बाक़ी सब लोगों की औसत आय बढ़ जाए"],
   ans=1, pos=1)
RQ(p, "Specific Detail", "medium", "s2", VALID, VALID_HI,
   "Neither is valid. 1 misstates Rawls: he would allow inequalities only if they benefit the least advantaged, not any inequality that raises the average. "
   "2 reverses the critics' point: they say people might gamble on being among the lucky -- that the veil would not make them as cautious as Rawls supposed -- not that it makes them too cautious to gamble.",
   "कोई भी वैध नहीं। 1 रॉल्स को ग़लत ढंग से बताता है: वे असमानताओं की अनुमति केवल तभी देंगे जब वे सबसे वंचितों को लाभ पहुँचाएँ, औसत बढ़ाने वाली किसी भी असमानता की नहीं। "
   "2 आलोचकों की बात को उलट देता है: वे कहते हैं कि लोग भाग्यशाली लोगों में होने का दाँव लगा सकते हैं -- कि पर्दा उन्हें उतना सतर्क नहीं बनाएगा जितना रॉल्स ने माना -- यह नहीं कि वह उन्हें दाँव लगाने के लिए बहुत सतर्क बना देता है।",
   "conclusions",
   st=["Rawls held that people behind the veil would accept any inequality that raised the average income of the society.",
       "The critics mentioned in the passage object that the veil would make people too cautious to take any gamble."],
   st_hi=["रॉल्स का मत था कि पर्दे के पीछे के लोग समाज की औसत आय बढ़ाने वाली किसी भी असमानता को स्वीकार कर लेंगे।",
          "परिच्छेद में उल्लिखित आलोचक आपत्ति करते हैं कि पर्दा लोगों को कोई भी दाँव लगाने के लिए बहुत सतर्क बना देगा।"],
   key=3)

# ------------------------------------------------------------------ P07 the winter rain of western disturbances
p = passage("p07",
  "Most of India's rain falls in the summer monsoon, but the north-west also receives a little rain in winter, and it matters out of all proportion to its amount. It is brought by western disturbances -- low-pressure systems that form over the Mediterranean region and are carried eastward across Iran and Afghanistan by the westerly winds of the upper air. "
  "When they reach India they bring light rain to the plains of Punjab, Haryana and western Uttar Pradesh, and snow to the western Himalaya. The rain falls while the wheat sown in November is growing, and can save farmers an irrigation or two; the snow feeds the rivers that flow through the following spring and summer. "
  "Yet the same systems can do harm. A disturbance that arrives late, in March or April, when the wheat is ripening, may bring hail and strong winds that flatten the crop. Whether a western disturbance proves a blessing or a loss depends less on its strength than on its timing.",
  "भारत की अधिकांश वर्षा ग्रीष्मकालीन मानसून में होती है, पर उत्तर-पश्चिम में सर्दियों में भी थोड़ी वर्षा होती है, और उसका महत्त्व उसकी मात्रा से कहीं अधिक है। यह पश्चिमी विक्षोभों से आती है -- निम्न दाब की प्रणालियाँ जो भूमध्यसागरीय क्षेत्र के ऊपर बनती हैं और ऊपरी वायुमंडल की पछुआ हवाओं द्वारा ईरान और अफ़ग़ानिस्तान के पार पूर्व की ओर ले जाई जाती हैं। "
  "भारत पहुँचने पर वे पंजाब, हरियाणा और पश्चिमी उत्तर प्रदेश के मैदानों में हल्की वर्षा, और पश्चिमी हिमालय में हिमपात लाते हैं। वर्षा तब होती है जब नवंबर में बोया गया गेहूँ बढ़ रहा होता है, और किसानों की एक-दो सिंचाई बचा सकती है; हिम उन नदियों को पोषित करता है जो अगले वसंत और ग्रीष्म में बहती हैं। "
  "फिर भी यही प्रणालियाँ हानि भी कर सकती हैं। देर से, मार्च या अप्रैल में, जब गेहूँ पक रहा होता है, आने वाला विक्षोभ ओले और तेज़ हवाएँ ला सकता है जो फ़सल को बिछा देती हैं। कोई पश्चिमी विक्षोभ वरदान सिद्ध होगा या हानि, यह उसकी तीव्रता से कम और उसके समय से अधिक तय होता है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage explains that the small winter rain of western disturbances helps the wheat and feeds the rivers, then turns to the harm late disturbances can do, ending on timing as the deciding factor. "
   "It says the winter rain matters 'out of all proportion to its amount', not that it matters more than the monsoon; it says late disturbances 'may' harm the crop, not that all of them do; and it places their origin over the Mediterranean, not the Indian Ocean.",
   "परिच्छेद बताता है कि पश्चिमी विक्षोभों की थोड़ी-सी शीतकालीन वर्षा गेहूँ की सहायता करती है और नदियों को पोषित करती है, फिर देर से आने वाले विक्षोभों से होने वाली हानि की ओर मुड़ता है, और समय को निर्णायक कारक बताकर समाप्त होता है। "
   "वह कहता है कि शीतकालीन वर्षा का महत्त्व 'उसकी मात्रा से कहीं अधिक' है, यह नहीं कि वह मानसून से अधिक मायने रखती है; वह कहता है कि देर से आने वाले विक्षोभ फ़सल को हानि पहुँचा 'सकते' हैं, यह नहीं कि सभी पहुँचाते हैं; और वह उनका उद्गम भूमध्यसागर के ऊपर बताता है, हिंद महासागर नहीं।",
   "crux",
   opts=["Winter rain from western disturbances helps the rabi crop, but its effect depends on when it comes.",
         "The winter rain of the north-west matters more to Indian farming than the rain of the summer monsoon.",
         "Western disturbances always harm the wheat crop, since they bring hail and strong winds to the plains.",
         "Western disturbances form over the Indian Ocean and move north-west across the Indian subcontinent."],
   opts_hi=["पश्चिमी विक्षोभों की शीतकालीन वर्षा रबी फ़सल की सहायता करती है, पर उसका प्रभाव आने के समय पर निर्भर है।",
            "उत्तर-पश्चिम की शीतकालीन वर्षा भारतीय खेती के लिए ग्रीष्मकालीन मानसून की वर्षा से अधिक मायने रखती है।",
            "पश्चिमी विक्षोभ हमेशा गेहूँ की फ़सल को हानि पहुँचाते हैं, क्योंकि वे मैदानों में ओले और तेज़ हवाएँ लाते हैं।",
            "पश्चिमी विक्षोभ हिंद महासागर के ऊपर बनते हैं और भारतीय उपमहाद्वीप के पार उत्तर-पश्चिम की ओर बढ़ते हैं।"],
   ans=0, pos=0)
RQ(p, "Specific Detail", "medium", "mcq",
   "According to the passage, how does the winter snow that western disturbances bring to the western Himalaya help?",
   "परिच्छेद के अनुसार, पश्चिमी विक्षोभों द्वारा पश्चिमी हिमालय में लाया गया शीतकालीन हिम कैसे सहायता करता है?",
   "The passage says that the snow 'feeds the rivers that flow through the following spring and summer'. "
   "Saving an irrigation is what the rain on the plains does for the wheat; the passage does not say that snow prevents hail or cools the westerly winds.",
   "परिच्छेद कहता है कि हिम 'उन नदियों को पोषित करता है जो अगले वसंत और ग्रीष्म में बहती हैं'। "
   "सिंचाई बचाना वह काम है जो मैदानों की वर्षा गेहूँ के लिए करती है; परिच्छेद यह नहीं कहता कि हिम ओलों को रोकता है या पछुआ हवाओं को ठंडा करता है।",
   "what-the-winter-snow-does",
   opts=["It saves farmers on the plains an irrigation or two for the wheat sown in November.",
         "It stops hail from falling on the plains when the wheat is ripening in March and April.",
         "It feeds the rivers that flow through the following spring and summer.",
         "It cools the westerly winds of the upper air that carry the disturbances eastward."],
   opts_hi=["यह मैदानों के किसानों की नवंबर में बोए गए गेहूँ के लिए एक-दो सिंचाई बचाता है।",
            "यह मार्च और अप्रैल में गेहूँ पकने के समय मैदानों में ओले गिरने से रोकता है।",
            "यह उन नदियों को पोषित करता है जो अगले वसंत और ग्रीष्म में बहती हैं।",
            "यह ऊपरी वायुमंडल की उन पछुआ हवाओं को ठंडा करता है जो विक्षोभों को पूर्व की ओर ले जाती हैं।"],
   ans=2, pos=2)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Both are valid. The passage ends by saying that a disturbance's effect depends less on its strength than on its timing, so two of equal strength, one arriving while the wheat grows and one while it ripens, could help in one case and harm in the other (1). "
   "And since a disturbance in the growing season brings useful rain while one in March or April may bring hail, one in December or January is the more likely to help (2).",
   "दोनों वैध हैं। परिच्छेद यह कहकर समाप्त होता है कि किसी विक्षोभ का प्रभाव उसकी तीव्रता से कम और उसके समय पर अधिक निर्भर है, इसलिए समान तीव्रता के दो विक्षोभ, एक गेहूँ के बढ़ते समय और एक पकते समय आने वाला, एक स्थिति में सहायता और दूसरी में हानि कर सकते हैं (1)। "
   "और चूँकि बढ़वार के मौसम का विक्षोभ उपयोगी वर्षा लाता है जबकि मार्च या अप्रैल का विक्षोभ ओले ला सकता है, दिसंबर या जनवरी के विक्षोभ के सहायक होने की संभावना अधिक है (2)।",
   "conclusions",
   st=["Two western disturbances of the same strength could have opposite effects on the wheat harvest.",
       "A western disturbance in December or January is more likely to help the wheat crop than one in April."],
   st_hi=["समान तीव्रता के दो पश्चिमी विक्षोभों का गेहूँ की फ़सल पर विपरीत प्रभाव हो सकता है।",
          "दिसंबर या जनवरी के पश्चिमी विक्षोभ के गेहूँ की फ़सल के लिए अप्रैल वाले विक्षोभ से अधिक सहायक होने की संभावना है।"],
   key=2)

# ------------------------------------------------------------------ P08 India's railway gauges
p = passage("p08",
  "When railways were first built in India in the nineteenth century, the main lines were laid to a broad gauge -- the distance between the rails -- of 1,676 mm. From the 1870s, to save money, many new lines were built to a metre gauge, and some hill and branch lines to narrower gauges still. "
  "Each choice made sense at the time, but together they left a network in which goods moving between lines of different gauges had to be unloaded and reloaded by hand, a slow and costly business. Once thousands of kilometres of track, and the engines and wagons to run on it, had been built to a gauge, changing it was hugely expensive, so the mixed network lasted for more than a century. Only in 1992 did Indian Railways begin Project Unigauge, a long programme of converting metre and narrow gauge lines to broad gauge. "
  "Economists call such cases path dependence: a choice that suits its moment can, by attracting investments built around it, lock in a pattern that later generations would never have chosen.",
  "जब उन्नीसवीं शताब्दी में भारत में पहली बार रेलें बनीं, तो मुख्य लाइनें 1,676 मिमी की बड़ी लाइन (ब्रॉड गेज) -- पटरियों के बीच की दूरी -- पर बिछाई गईं। 1870 के दशक से पैसा बचाने के लिए कई नई लाइनें मीटर गेज पर बनाई गईं, और कुछ पहाड़ी और शाखा लाइनें उससे भी संकरी गेजों पर। "
  "हर चुनाव अपने समय में उचित था, पर मिलकर उन्होंने ऐसा जाल छोड़ा जिसमें अलग-अलग गेज की लाइनों के बीच जाने वाले माल को हाथ से उतारना और फिर लादना पड़ता था, जो धीमा और महँगा काम था। एक बार किसी गेज पर हज़ारों किलोमीटर पटरी, और उस पर चलने वाले इंजन और डिब्बे बन जाने पर उसे बदलना बेहद महँगा था, इसलिए मिश्रित जाल एक शताब्दी से भी अधिक समय तक बना रहा। केवल 1992 में भारतीय रेल ने प्रोजेक्ट यूनीगेज शुरू किया, मीटर और नैरो गेज लाइनों को बड़ी लाइन में बदलने का एक लंबा कार्यक्रम। "
  "अर्थशास्त्री ऐसे मामलों को पथ-निर्भरता कहते हैं: अपने समय के अनुकूल कोई चुनाव, अपने इर्द-गिर्द बने निवेशों को आकर्षित करके, एक ऐसा ढर्रा जमा सकता है जिसे बाद की पीढ़ियाँ कभी न चुनतीं।")
RQ(p, "Best Summary", "medium", "mcq",
   "Which one of the following best summarises the passage?",
   "निम्नलिखित में से कौन-सा परिच्छेद का सबसे अच्छा सारांश है?",
   "The passage tells how sensible choices of gauge, each made to suit its time, became costly to undo once track and rolling stock had been built around them, and names this path dependence. "
   "It says the metre gauge was chosen to save money, the opposite of choosing without thought for cost; it never claims that a single gauge was cheaper from the very start; and it calls Project Unigauge a long programme begun in 1992, without saying that every line has been converted.",
   "परिच्छेद बताता है कि गेज के समझदारी भरे चुनाव, जो हर एक अपने समय के अनुकूल किया गया था, पटरियों और डिब्बों के उनके इर्द-गिर्द बन जाने के बाद बदलने में महँगे हो गए, और इसे पथ-निर्भरता कहता है। "
   "वह कहता है कि मीटर गेज पैसा बचाने के लिए चुनी गई, जो लागत का विचार किए बिना चुनने का उलटा है; वह कभी दावा नहीं करता कि एक ही गेज शुरू से सस्ती थी; और वह प्रोजेक्ट यूनीगेज को 1992 में शुरू हुआ एक लंबा कार्यक्रम कहता है, यह कहे बिना कि हर लाइन बदल दी गई है।",
   "summary",
   opts=["India's early railway builders chose the metre gauge without giving any thought to what it would cost.",
         "A single gauge for a whole railway network is always cheaper than a mix of gauges, right from the start.",
         "Project Unigauge has now converted every railway line in India from metre or narrow gauge to broad gauge.",
         "Choices made for good reasons in their time can become costly to undo once investment grows around them."],
   opts_hi=["भारत के आरंभिक रेल निर्माताओं ने मीटर गेज को उसकी लागत का कोई विचार किए बिना चुना।",
            "पूरे रेल जाल के लिए एक ही गेज शुरू से ही गेजों के मिश्रण से हमेशा सस्ती होती है।",
            "प्रोजेक्ट यूनीगेज ने अब भारत की हर रेल लाइन को मीटर या नैरो गेज से बड़ी लाइन में बदल दिया है।",
            "अपने समय में उचित चुनाव, उनके इर्द-गिर्द निवेश बढ़ने के बाद, बदलने में महँगे हो सकते हैं।"],
   ans=3, pos=3)
RQ(p, "Inference", "hard", "mcq",
   "Which one of the following is also an example of path dependence as the passage describes it?",
   "निम्नलिखित में से कौन-सा भी परिच्छेद में वर्णित पथ-निर्भरता का एक उदाहरण है?",
   "Path dependence, in the passage, is an early choice that suited its moment and then became locked in because investments were built around it. A city's narrow lanes, laid out for carts and now lined with buildings that make widening hugely expensive, fit that pattern. "
   "Switching to a better seed as soon as it is proven shows no lock-in; a timetable changed every year is the opposite of being locked in; and buying stock by last month's sales is ordinary adjustment to recent information.",
   "परिच्छेद में पथ-निर्भरता एक आरंभिक चुनाव है जो अपने समय के अनुकूल था और फिर इसलिए जम गया कि उसके इर्द-गिर्द निवेश हो गए। किसी शहर की संकरी गलियाँ, जो गाड़ियों के लिए बनी थीं और जिनके किनारे अब ऐसी इमारतें हैं कि उन्हें चौड़ा करना बेहद महँगा है, इस ढर्रे पर ठीक बैठती हैं। "
   "सिद्ध होते ही बेहतर बीज अपना लेना कोई जमाव नहीं दिखाता; हर वर्ष बदली जाने वाली समय-सारणी जमाव का उलटा है; और पिछले महीने की बिक्री के आधार पर माल ख़रीदना हाल की जानकारी के अनुसार सामान्य समायोजन है।",
   "another-example-of-path-dependence",
   opts=["A farmer who switches to a new variety of seed as soon as trials show that it gives higher yields",
         "A railway that rewrites its timetable every year to keep pace with changes in demand",
         "A city whose lanes, laid out for carts, are too costly to widen now that buildings line them",
         "A shopkeeper who decides what to stock by checking which goods sold best in the month before"],
   opts_hi=["ऐसा किसान जो परीक्षणों में किसी नए बीज के अधिक उपज देने का प्रमाण मिलते ही उसे तुरंत अपना लेता है",
            "ऐसी रेल जो माँग में बदलावों के साथ चलने के लिए हर वर्ष अपनी समय-सारणी फिर से लिखती है",
            "ऐसा शहर जिसकी गाड़ियों के लिए बनी गलियाँ किनारे इमारतें बन जाने से चौड़ी करने में बहुत महँगी हैं",
            "ऐसा दुकानदार जो यह देखकर तय करता है कि क्या रखे कि पिछले महीने कौन-सा सामान सबसे अधिक बिका"],
   ans=2, pos=2)
RQ(p, "Specific Detail", "medium", "s2", VALID, VALID_HI,
   "Only 2 is valid. The passage says goods moving between gauges had to be unloaded and reloaded by hand, 'a slow and costly business'. "
   "1 is not supported: the passage says the metre gauge was adopted to save money, and nothing suggests that the government expected the lines to be replaced soon -- the mixed network in fact lasted more than a century.",
   "केवल 2 वैध है। परिच्छेद कहता है कि अलग-अलग गेज के बीच जाने वाले माल को हाथ से उतारना और फिर लादना पड़ता था, 'जो धीमा और महँगा काम था'। "
   "1 समर्थित नहीं है: परिच्छेद कहता है कि मीटर गेज पैसा बचाने के लिए अपनाई गई, और कुछ भी यह नहीं बताता कि सरकार को लाइनों के जल्द बदले जाने की आशा थी -- वास्तव में मिश्रित जाल एक शताब्दी से अधिक चला।",
   "conclusions",
   st=["The metre gauge lines were built because the government expected them to be replaced by broad gauge soon.",
       "Moving goods between lines of different gauges added both time and cost to their journey."],
   st_hi=["मीटर गेज लाइनें इसलिए बनाई गईं कि सरकार को आशा थी कि उन्हें जल्द ही बड़ी लाइन से बदल दिया जाएगा।",
          "अलग-अलग गेज की लाइनों के बीच माल ले जाने से उसकी यात्रा में समय और लागत दोनों बढ़ते थे।"],
   key=1)

# ------------------------------------------------------------------ P09 Ambedkar on constitutional morality
p = passage("p09",
  "Moving the draft Constitution in the Constituent Assembly in November 1948, B. R. Ambedkar borrowed a phrase from the historian George Grote: constitutional morality. By it he meant a deep respect for the forms of the constitution -- a habit of working through its procedures and accepting their limits, even when one is strong enough to brush them aside. "
  "Such a habit, he warned, is not a natural sentiment; it has to be cultivated, and he doubted that it was yet widespread in India. That doubt explains a feature of the document that is often criticised: its length. Ambedkar defended including details of administration, which other constitutions leave to ordinary law, on the ground that where constitutional morality is weak it is possible to pervert a constitution without changing its form, simply by changing the way it is administered. "
  "Writing more into the text narrows the room for such perversion. But no text can close it entirely. A constitution can lay down procedures; whether they are honoured depends on those who work them.",
  "नवंबर 1948 में संविधान सभा में संविधान का प्रारूप प्रस्तुत करते हुए बी. आर. आंबेडकर ने इतिहासकार जॉर्ज ग्रोट से एक पद उधार लिया: संवैधानिक नैतिकता। इससे उनका आशय संविधान के रूपों के प्रति गहरे सम्मान से था -- उसकी प्रक्रियाओं के माध्यम से काम करने और उनकी सीमाओं को स्वीकार करने की आदत, तब भी जब कोई उन्हें किनारे कर देने लायक़ शक्तिशाली हो। "
  "उन्होंने चेताया कि ऐसी आदत कोई स्वाभाविक भावना नहीं है; उसे विकसित करना पड़ता है, और उन्हें संदेह था कि वह भारत में अभी व्यापक है। यही संदेह इस दस्तावेज़ की एक ऐसी विशेषता को समझाता है जिसकी प्रायः आलोचना होती है: उसकी लंबाई। आंबेडकर ने प्रशासन के उन विवरणों को शामिल करने का बचाव किया जिन्हें अन्य संविधान साधारण क़ानून पर छोड़ देते हैं, इस आधार पर कि जहाँ संवैधानिक नैतिकता कमज़ोर हो वहाँ संविधान का रूप बदले बिना, केवल उसके प्रशासन का ढंग बदलकर, उसे विकृत करना संभव है। "
  "पाठ में अधिक लिखना ऐसी विकृति की गुंजाइश को कम करता है। पर कोई भी पाठ उसे पूरी तरह बंद नहीं कर सकता। संविधान प्रक्रियाएँ निर्धारित कर सकता है; उनका सम्मान होगा या नहीं, यह उन पर निर्भर है जो उन्हें चलाते हैं।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage explains that Ambedkar wrote administrative detail into the Constitution because respect for its forms was not yet widespread, and it adds that such detail narrows, but cannot close, the room for abuse. "
   "It ends by saying that no text can close that room and that everything depends on those who work the procedures, so detail does not make constitutional morality unnecessary; Ambedkar called that morality something to be cultivated, not natural; and he defended the length rather than calling for it to be cut.",
   "परिच्छेद बताता है कि आंबेडकर ने संविधान में प्रशासनिक विवरण इसलिए लिखे कि उसके रूपों के प्रति सम्मान अभी व्यापक नहीं था, और जोड़ता है कि ऐसे विवरण दुरुपयोग की गुंजाइश को कम करते हैं, पर बंद नहीं कर सकते। "
   "वह यह कहकर समाप्त होता है कि कोई पाठ उस गुंजाइश को बंद नहीं कर सकता और सब कुछ प्रक्रियाएँ चलाने वालों पर निर्भर है, इसलिए विवरण संवैधानिक नैतिकता को अनावश्यक नहीं बनाते; आंबेडकर ने उस नैतिकता को विकसित की जाने वाली चीज़ कहा, स्वाभाविक नहीं; और उन्होंने लंबाई का बचाव किया, उसे घटाने की माँग नहीं की।",
   "crux",
   opts=["A long and detailed constitution makes the habit of constitutional morality unnecessary.",
         "Ambedkar wrote administrative detail into the Constitution because respect for its forms was not yet secure.",
         "Constitutional morality comes naturally to any people that adopts a democratic constitution.",
         "Ambedkar thought the draft Constitution too long and wanted its administrative details left to ordinary law."],
   opts_hi=["एक लंबा और विस्तृत संविधान संवैधानिक नैतिकता की आदत को अनावश्यक बना देता है।",
            "आंबेडकर ने संविधान में प्रशासनिक विवरण इसलिए लिखे कि उसके रूपों के प्रति सम्मान अभी सुरक्षित नहीं था।",
            "संवैधानिक नैतिकता लोकतांत्रिक संविधान अपनाने वाले किसी भी समाज में स्वाभाविक रूप से आ जाती है।",
            "आंबेडकर प्रारूप संविधान को बहुत लंबा मानते थे और चाहते थे कि उसके प्रशासनिक विवरण साधारण क़ानून पर छोड़ दिए जाएँ।"],
   ans=1, pos=1)
RQ(p, "Inference", "hard", "mcq",
   "Which one of the following would be an example of perverting a constitution 'without changing its form', in the sense the passage uses?",
   "निम्नलिखित में से कौन-सा, परिच्छेद में प्रयुक्त अर्थ में, संविधान को 'उसका रूप बदले बिना' विकृत करने का उदाहरण होगा?",
   "Perverting a constitution without changing its form means leaving every procedure in place on paper while administering it against its spirit. A government that keeps the forms but fills the bodies meant to check it with its own loyalists does exactly that. "
   "Amending the constitution by its own procedure after open debate is working through its forms, not perverting them; a court striking down an unconstitutional law is a check doing its job; and abolishing the legislature by decree changes the form itself.",
   "संविधान को उसका रूप बदले बिना विकृत करने का अर्थ है काग़ज़ पर हर प्रक्रिया को बनाए रखते हुए उसे उसकी भावना के विरुद्ध चलाना। ऐसी सरकार जो रूपों को बनाए रखती है पर उस पर अंकुश रखने वाले निकायों को अपने निष्ठावानों से भर देती है, ठीक यही करती है। "
   "खुली बहस के बाद संविधान को उसकी अपनी प्रक्रिया से संशोधित करना उसके रूपों के माध्यम से काम करना है, उन्हें विकृत करना नहीं; असंवैधानिक क़ानून को रद्द करने वाला न्यायालय एक अंकुश है जो अपना काम कर रहा है; और आदेश द्वारा विधायिका को समाप्त करना स्वयं रूप को बदलता है।",
   "perverting-without-changing-the-form",
   opts=["A government that keeps all procedures on paper but fills the bodies that check it with loyalists",
         "Amending the constitution by the very procedure that it lays down, after an open debate in the legislature",
         "A court striking down a law because it conflicts with a provision of the constitution",
         "Abolishing the legislature by decree and governing without it until further notice"],
   opts_hi=["ऐसी सरकार जो काग़ज़ पर सब प्रक्रियाएँ रखती है पर अंकुश वाले निकायों में निष्ठावान भर देती है",
            "विधायिका में खुली बहस के बाद संविधान को उसी की निर्धारित की गई प्रक्रिया के अनुसार संशोधित करना",
            "किसी न्यायालय द्वारा किसी क़ानून को इसलिए रद्द करना कि वह संविधान के किसी प्रावधान के विरुद्ध है",
            "एक आदेश द्वारा विधायिका को समाप्त कर देना और अगली सूचना तक उसके बिना ही शासन चलाना"],
   ans=0, pos=0)
RQ(p, "Assumption", "hard", "s2", ASSUME, ASSUME_HI,
   "Only 1 is assumed. The claim that writing more into the text 'narrows the room' for perversion takes for granted that rules placed in the constitution are harder to change or ignore than rules left to ordinary law. "
   "2 is not assumed; the passage denies it, saying no text can close the room entirely and that whether procedures are honoured depends on those who work them.",
   "केवल 1 पूर्वधारणा है। यह दावा कि पाठ में अधिक लिखना विकृति की 'गुंजाइश को कम करता है', यह मानकर चलता है कि संविधान में रखे गए नियमों को साधारण क़ानून पर छोड़े गए नियमों की तुलना में बदलना या अनदेखा करना कठिन है। "
   "2 पूर्वधारणा नहीं है; परिच्छेद उसका खंडन करता है, यह कहते हुए कि कोई पाठ गुंजाइश को पूरी तरह बंद नहीं कर सकता और प्रक्रियाओं का सम्मान उन्हें चलाने वालों पर निर्भर है।",
   "assumptions",
   st=["Rules written into a constitution are harder to change or ignore than rules left to ordinary law.",
       "A constitution that includes enough administrative detail will be honoured by whoever comes to work it."],
   st_hi=["संविधान में लिखे गए नियमों को साधारण क़ानून पर छोड़े गए नियमों की तुलना में बदलना या अनदेखा करना कठिन है।",
          "पर्याप्त प्रशासनिक विवरण वाले संविधान का सम्मान वह हर व्यक्ति करेगा जो उसे चलाने आए।"],
   key=0)
