# -*- coding: utf-8 -*-
"""CSAT Level 4 · Simulator 3 -- Reading Comprehension: 10 short passages, 23 items (3 x 3, 7 x 2), Layout C.

The 2026 shape: more passages, shorter ones, fewer items each. Each passage still turns -- a claim, then its limit.
Themes, none used in Levels 1-3 or Simulators 1-2: the ring that makes its wearer invisible, the missing middle of
Indian firms, fire in forests, meat grown from cells, Sher Shah's road, the anti-defection law, India's own satellite
navigation, the black soils of the Deccan, rights and the arithmetic of lives, and a carbon tax at the border.
Item types: main idea 9, inference 9, assumption 1, specific detail 3, best summary 1. Difficulty 1 easy /
12 medium / 10 hard. Options are named by content in every explanation."""
from csat_common import passage, RQ

CRUX = "Which one of the following statements best reflects the crux of the passage?"
CRUX_HI = "निम्नलिखित में से कौन-सा कथन परिच्छेद के सार को सबसे अच्छी तरह व्यक्त करता है?"
MSG = "Which one of the following statements best reflects the most logical and rational message conveyed by the passage?"
MSG_HI = "निम्नलिखित में से कौन-सा कथन परिच्छेद द्वारा दिए गए सबसे तार्किक और विवेकपूर्ण संदेश को सबसे अच्छी तरह व्यक्त करता है?"
VALID = "On the basis of the passage, which of the following conclusions is/are valid?"
VALID_HI = "परिच्छेद के आधार पर निम्नलिखित में से कौन-सा/से निष्कर्ष वैध है/हैं?"
ASSUME = "Which of the following assumptions has/have been made in the passage?"
ASSUME_HI = "परिच्छेद में निम्नलिखित में से कौन-सी पूर्वधारणा/एँ बनाई गई है/हैं?"
IMPL = "Which one of the following statements best reflects the most logical and rational implication conveyed by the passage?"
IMPL_HI = "निम्नलिखित में से कौन-सा कथन परिच्छेद द्वारा दिए गए सबसे तार्किक और विवेकपूर्ण निहितार्थ को सबसे अच्छी तरह व्यक्त करता है?"

# ------------------------------------------------------------------ P01 the ring that makes its wearer invisible (2)
p = passage("p01",
  "In Plato's Republic a character tells of a shepherd who finds a ring that makes him invisible, and who uses it to do as he pleases without fear of being caught. The story poses a hard question: would anyone stay honest who could never be found out? "
  "If people are just only because they fear being seen, then honesty is merely prudence. Most of us hope that our integrity runs deeper than that, and much of public life depends on it, since no inspector can watch every official at every moment. "
  "Yet a sensible society does not stake everything on that hope. It also arranges things so that honesty is easier and dishonesty riskier -- open records, rotation of duties, decisions that leave a trace -- so that decent conduct does not require heroes.",
  "प्लेटो के 'रिपब्लिक' में एक पात्र ऐसे चरवाहे की कथा सुनाता है जिसे एक अँगूठी मिलती है जो उसे अदृश्य कर देती है, और जो उसका प्रयोग पकड़े जाने के डर के बिना मनमानी करने के लिए करता है। कथा एक कठिन प्रश्न उठाती है: क्या कोई ऐसा व्यक्ति ईमानदार रहेगा जिसे कभी पकड़ा न जा सके? "
  "यदि लोग केवल देखे जाने के डर से न्यायपूर्ण हैं, तो ईमानदारी केवल चतुराई है। हममें से अधिकांश आशा करते हैं कि हमारी सत्यनिष्ठा इससे गहरी है, और सार्वजनिक जीवन का बहुत कुछ इसी पर निर्भर है, क्योंकि कोई निरीक्षक हर अधिकारी को हर क्षण नहीं देख सकता। "
  "फिर भी एक समझदार समाज सब कुछ इसी आशा पर दाँव पर नहीं लगाता। वह ऐसी व्यवस्था भी करता है कि ईमानदारी आसान और बेईमानी जोखिम भरी हो -- खुले अभिलेख, कर्तव्यों का बारी-बारी से बदलना, ऐसे निर्णय जो निशान छोड़ें -- ताकि अच्छे आचरण के लिए नायकों की आवश्यकता न पड़े।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage values integrity that does not depend on being watched, since public life relies on it, but adds that a sensible society also makes honesty easier and dishonesty riskier rather than relying on that integrity alone. "
   "It does not say people are honest only out of fear -- it hopes integrity runs deeper; it does not want every official watched, which it calls impossible; and it treats the shepherd's story as a question, not as proof that honesty is impossible.",
   "परिच्छेद ऐसी सत्यनिष्ठा को महत्त्व देता है जो देखे जाने पर निर्भर न हो, क्योंकि सार्वजनिक जीवन उस पर टिका है, पर जोड़ता है कि समझदार समाज अकेले उस सत्यनिष्ठा पर निर्भर रहने के बजाय ईमानदारी को आसान और बेईमानी को जोखिम भरा भी बनाता है। "
   "वह यह नहीं कहता कि लोग केवल डर से ईमानदार हैं -- वह आशा करता है कि सत्यनिष्ठा गहरी है; वह हर अधिकारी पर नज़र रखना नहीं चाहता, जिसे वह असंभव कहता है; और वह चरवाहे की कथा को एक प्रश्न मानता है, इस बात का प्रमाण नहीं कि ईमानदारी असंभव है।",
   "crux",
   opts=["People are honest only because they fear being caught, as the story of the ring shows clearly.",
         "Integrity matters most when no one is watching, but society should not rely on it alone.",
         "Every public official should be watched at every moment so that no one can act unseen.",
         "The story of the ring proves that no one could remain honest if they could never be caught."],
   opts_hi=["लोग केवल इसलिए ईमानदार हैं कि उन्हें पकड़े जाने का डर है, जैसा अँगूठी की कथा स्पष्ट दिखाती है।",
            "सत्यनिष्ठा तब सबसे अधिक मायने रखती है जब कोई देख न रहा हो, पर समाज अकेले उस पर निर्भर न रहे।",
            "हर सार्वजनिक अधिकारी पर हर क्षण नज़र रखी जाए ताकि कोई भी बिना देखे काम न कर सके।",
            "अँगूठी की कथा सिद्ध करती है कि कोई भी ईमानदार नहीं रह सकता यदि उसे कभी पकड़ा न जा सके।"],
   ans=1, pos=1)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Neither is valid. 1 goes beyond the passage: it recommends open records and similar arrangements to make honesty easier, but it never says that they make personal integrity unnecessary -- it calls public life dependent on that integrity. "
   "2 also goes too far: the passage reports the story's question without saying that Plato concluded that people are honest only from fear; it hopes integrity runs deeper.",
   "कोई भी वैध नहीं। 1 परिच्छेद से आगे जाता है: वह ईमानदारी को आसान बनाने के लिए खुले अभिलेखों और ऐसी व्यवस्थाओं की सलाह देता है, पर कभी नहीं कहता कि वे निजी सत्यनिष्ठा को अनावश्यक बना देती हैं -- वह सार्वजनिक जीवन को उस सत्यनिष्ठा पर निर्भर बताता है। "
   "2 भी बहुत आगे जाता है: परिच्छेद कथा का प्रश्न बताता है, यह नहीं कहता कि प्लेटो ने निष्कर्ष निकाला कि लोग केवल डर से ईमानदार हैं; वह आशा करता है कि सत्यनिष्ठा गहरी है।",
   "conclusions",
   st=["Once records are open and decisions leave a trace, the personal integrity of officials no longer matters.",
       "According to the passage, Plato concluded that people are honest only because they fear being seen."],
   st_hi=["एक बार अभिलेख खुले हों और निर्णय निशान छोड़ें, तो अधिकारियों की निजी सत्यनिष्ठा का कोई महत्त्व नहीं रह जाता।",
          "परिच्छेद के अनुसार प्लेटो ने निष्कर्ष निकाला कि लोग केवल देखे जाने के डर से ईमानदार हैं।"],
   key=3)

# ------------------------------------------------------------------ P02 the missing middle of Indian firms (3)
p = passage("p02",
  "Most Indian enterprises are very small, many with fewer than ten workers, and a few are very large; comparatively few are of middling size. Economists call this the missing middle, and it matters because medium firms tend to be more productive than tiny ones and are where many better-paid jobs are created. "
  "Regulation is often blamed. For decades some labour rules began to bite only above a fixed number of workers -- permission to lay off workers, for instance, was needed by factories with a hundred or more -- and a firm near such a line had a reason to stay below it. "
  "Raising or removing such thresholds may help. But it would be a mistake to treat them as the whole story. Small firms also stay small because credit is hard to get, because their markets are local, and because their owners lack the managers needed to run something bigger.",
  "अधिकांश भारतीय उद्यम बहुत छोटे हैं, कई में दस से कम कामगार, और कुछ बहुत बड़े हैं; मध्यम आकार के अपेक्षाकृत कम हैं। अर्थशास्त्री इसे 'लुप्त मध्य' कहते हैं, और यह इसलिए मायने रखता है कि मध्यम फ़र्में प्रायः बहुत छोटी फ़र्मों से अधिक उत्पादक होती हैं और वहीं बेहतर वेतन वाली कई नौकरियाँ बनती हैं। "
  "प्रायः विनियमन को दोष दिया जाता है। दशकों तक कुछ श्रम नियम एक निश्चित संख्या से अधिक कामगारों पर ही लागू होते थे -- उदाहरण के लिए, सौ या अधिक कामगारों वाले कारख़ानों को छँटनी के लिए अनुमति चाहिए थी -- और ऐसी रेखा के पास की फ़र्म के पास उससे नीचे बने रहने का कारण था। "
  "ऐसी सीमाओं को बढ़ाना या हटाना सहायक हो सकता है। पर उन्हें पूरी कहानी मानना भूल होगी। छोटी फ़र्में इसलिए भी छोटी रहती हैं कि ऋण पाना कठिन है, उनके बाज़ार स्थानीय हैं, और उनके मालिकों के पास किसी बड़े उद्यम को चलाने के लिए आवश्यक प्रबंधक नहीं हैं।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage explains why the missing middle matters and why regulatory thresholds are blamed, then limits that explanation: thresholds are part of the story, alongside credit, local markets and managerial capacity. "
   "It says raising thresholds 'may help', so it does not call them irrelevant; it does not say large firms are the problem; and it says removing thresholds is not the whole story, the opposite of its being enough on its own.",
   "परिच्छेद बताता है कि लुप्त मध्य क्यों मायने रखता है और विनियामक सीमाओं को दोष क्यों दिया जाता है, फिर उस व्याख्या को सीमित करता है: सीमाएँ कहानी का एक भाग हैं, ऋण, स्थानीय बाज़ारों और प्रबंधकीय क्षमता के साथ। "
   "वह कहता है कि सीमाएँ बढ़ाना 'सहायक हो सकता है', इसलिए वह उन्हें अप्रासंगिक नहीं कहता; वह बड़ी फ़र्मों को समस्या नहीं बताता; और वह कहता है कि सीमाएँ हटाना पूरी कहानी नहीं, जो अकेले उसके पर्याप्त होने का उलटा है।",
   "crux",
   opts=["Rules that bite above a size help explain the missing middle, but are not its only cause.",
         "Labour rules have nothing to do with the small size of most Indian firms, whatever is often said.",
         "India's largest firms are the main reason why so few firms of middling size exist in the country.",
         "Removing the size thresholds in labour rules would on its own be enough to fill the missing middle."],
   opts_hi=["आकार-सीमा के ऊपर लगने वाले नियम लुप्त मध्य को कुछ हद तक समझाते हैं, पर वे एकमात्र कारण नहीं।",
            "प्रायः जो भी कहा जाए, अधिकांश भारतीय फ़र्मों के छोटे आकार से श्रम नियमों का कोई संबंध नहीं है।",
            "भारत की सबसे बड़ी फ़र्में ही वह मुख्य कारण हैं जिससे देश में मध्यम आकार की फ़र्में इतनी कम हैं।",
            "श्रम नियमों में आकार की सीमाएँ हटाना अपने आप में लुप्त मध्य को भरने के लिए पर्याप्त होगा।"],
   ans=0, pos=0)
RQ(p, "Inference", "hard", "mcq",
   "According to the reasoning of the passage, which one of the following firms is most likely to stay small even if every size threshold in labour rules were removed?",
   "परिच्छेद के तर्क के अनुसार, श्रम नियमों की हर आकार-सीमा हटा दिए जाने पर भी निम्नलिखित में से किस फ़र्म के छोटे बने रहने की सबसे अधिक संभावना है?",
   "Removing thresholds takes away only the regulatory reason to stay small. A firm whose owner cannot borrow, sells only in its own town and has no one to help manage a larger business still faces the other three obstacles the passage names. "
   "A firm held below a hundred workers by the lay-off rule, a firm whose only worry was the paperwork above a threshold, and a firm with ample credit and distant buyers would each be freed to grow once the thresholds went.",
   "सीमाएँ हटाने से केवल छोटे रहने का विनियामक कारण हटता है। जिस फ़र्म का मालिक ऋण नहीं ले सकता, केवल अपने नगर में बेचता है और जिसके पास बड़े व्यवसाय को सँभालने में मदद करने वाला कोई नहीं, वह परिच्छेद में बताई अन्य तीनों बाधाओं का सामना करती रहती है। "
   "छँटनी के नियम के कारण सौ से कम कामगारों पर रुकी फ़र्म, ऐसी फ़र्म जिसकी एकमात्र चिंता सीमा के ऊपर की काग़ज़ी कार्यवाही थी, और पर्याप्त ऋण व दूर के ख़रीदारों वाली फ़र्म -- सीमाएँ हटते ही हर एक बढ़ने के लिए स्वतंत्र हो जाती।",
   "who-stays-small-without-thresholds",
   opts=["A factory with 95 workers that has avoided hiring more only because of the lay-off rule",
         "A firm whose sole reason for staying small is the paperwork it would face above a threshold",
         "A workshop whose owner cannot borrow, sells only in his own town and has no managers",
         "A firm with easy access to credit and buyers in many States that fears only labour rules"],
   opts_hi=["95 कामगारों वाला कारख़ाना जिसने केवल छँटनी के नियम के कारण और भर्ती से परहेज़ किया है",
            "ऐसी फ़र्म जिसके छोटे बने रहने का एकमात्र कारण सीमा के ऊपर होने वाली काग़ज़ी कार्यवाही है",
            "ऐसी कार्यशाला जिसका मालिक ऋण नहीं ले सकता, केवल अपने नगर में बेचता है और जिसके पास प्रबंधक नहीं",
            "ऐसी फ़र्म जिसे ऋण आसानी से मिलता है और कई राज्यों में ख़रीदार हैं, और जिसे केवल श्रम नियमों का डर है"],
   ans=2, pos=2)
RQ(p, "Assumption", "medium", "s2", ASSUME, ASSUME_HI,
   "Only 2 is assumed. The claim that a firm near a threshold 'had a reason to stay below it' takes for granted that firms weigh the costs a rule would impose on them before deciding whether to grow. "
   "1 is not assumed: the passage says medium firms 'tend to be' more productive than tiny ones, not that every large firm is more productive than every small one.",
   "केवल 2 पूर्वधारणा है। यह दावा कि सीमा के पास की फ़र्म के पास 'उससे नीचे बने रहने का कारण था', यह मानकर चलता है कि फ़र्में बढ़ने का निर्णय लेने से पहले उस लागत को तौलती हैं जो कोई नियम उन पर डालेगा। "
   "1 पूर्वधारणा नहीं है: परिच्छेद कहता है कि मध्यम फ़र्में प्रायः बहुत छोटी फ़र्मों से 'अधिक उत्पादक होती हैं', यह नहीं कि हर बड़ी फ़र्म हर छोटी फ़र्म से अधिक उत्पादक है।",
   "assumptions",
   st=["Every large firm is more productive than every small one.",
       "Firms take into account the costs that a rule would impose on them when deciding whether to grow."],
   st_hi=["हर बड़ी फ़र्म हर छोटी फ़र्म से अधिक उत्पादक है।",
          "फ़र्में बढ़ने का निर्णय लेते समय उन लागतों का ध्यान रखती हैं जो कोई नियम उन पर डालेगा।"],
   key=1)

# ------------------------------------------------------------------ P03 fire in forests (2)
p = passage("p03",
  "Many forests are shaped by fire, and some depend on it. Where small fires once burned through the undergrowth every few years, the habit of putting out every fire at once lets dead leaves and branches pile up, so that when a fire finally escapes control it burns far hotter and wider. "
  "Land managers in several countries have therefore revived the practice of deliberately setting small, cool fires in the right season, as some Indigenous communities long did, to clear away fuel before it builds up. "
  "The lesson is not that fire is always good for forests. Planned burns can escape, their smoke harms people's lungs, and wet tropical forests that rarely burn are badly damaged by it. Fire is a tool to be used where an ecosystem has grown up with it, not a general cure.",
  "कई वन आग से आकार लेते हैं, और कुछ उस पर निर्भर भी हैं। जहाँ कभी हर कुछ वर्षों में छोटी आगें झाड़ियों में से गुज़र जाती थीं, वहाँ हर आग को तुरंत बुझा देने की आदत सूखी पत्तियों और टहनियों को जमा होने देती है, जिससे जब अंततः कोई आग नियंत्रण से बाहर निकलती है तो वह कहीं अधिक गर्म और व्यापक जलती है। "
  "इसलिए कई देशों में भूमि-प्रबंधकों ने सही मौसम में जान-बूझकर छोटी, कम तापमान वाली आगें लगाने की प्रथा फिर से शुरू की है, जैसा कुछ मूल निवासी समुदाय लंबे समय से करते थे, ताकि ईंधन जमा होने से पहले हट जाए। "
  "सीख यह नहीं कि आग हमेशा वनों के लिए अच्छी है। नियोजित आगें बेक़ाबू हो सकती हैं, उनका धुआँ लोगों के फेफड़ों को हानि पहुँचाता है, और नम उष्णकटिबंधीय वन, जो विरले ही जलते हैं, उससे बुरी तरह क्षतिग्रस्त होते हैं। आग उन जगहों के लिए उपकरण है जहाँ कोई पारितंत्र उसके साथ विकसित हुआ है, सामान्य उपचार नहीं।")
RQ(p, "Best Summary", "medium", "mcq", MSG, MSG_HI,
   "The passage argues that putting out every fire can make later fires worse, so planned small burns help where forests have grown up with fire -- but that fire is not good for every forest. "
   "It does not say every fire should be put out at once, which it says makes fires worse; nor that forests should be left to burn freely, since it recommends small, planned fires; nor that tropical forests benefit, which it says are badly damaged.",
   "परिच्छेद तर्क देता है कि हर आग बुझा देने से बाद की आगें और बुरी हो सकती हैं, इसलिए जहाँ वन आग के साथ विकसित हुए हैं वहाँ नियोजित छोटी आगें सहायक हैं -- पर आग हर वन के लिए अच्छी नहीं। "
   "वह यह नहीं कहता कि हर आग तुरंत बुझाई जाए, जिससे उसके अनुसार आगें और बुरी होती हैं; न यह कि वनों को खुलकर जलने दिया जाए, क्योंकि वह छोटी, नियोजित आगों की सलाह देता है; न यह कि उष्णकटिबंधीय वनों को लाभ होता है, जिन्हें वह बुरी तरह क्षतिग्रस्त बताता है।",
   "message",
   opts=["Every forest fire should be put out at once, however small it is, to protect the trees.",
         "Forests should be left to burn freely, since fire is natural and always good for them.",
         "Wet tropical forests benefit most from deliberate burning, since they burn so rarely.",
         "Planned burning can prevent worse fires where forests have grown up with fire."],
   opts_hi=["पेड़ों की रक्षा के लिए वन की हर आग तुरंत बुझाई जाए, वह चाहे कितनी भी छोटी हो।",
            "वनों को खुलकर जलने दिया जाए, क्योंकि आग प्राकृतिक है और उनके लिए हमेशा अच्छी है।",
            "नम उष्णकटिबंधीय वनों को जान-बूझकर जलाने से सबसे अधिक लाभ होता है, क्योंकि वे विरले जलते हैं।",
            "जहाँ वन आग के साथ विकसित हुए हैं, वहाँ नियोजित आग बदतर आगों को रोक सकती है।"],
   ans=3, pos=3)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Only 1 is valid. The passage says that putting out every fire lets fuel pile up so that an escaped fire 'burns far hotter and wider'; so a forest where small fires have long been prevented is at greater risk of a severe fire. "
   "2 contradicts it: wet tropical forests 'that rarely burn are badly damaged' by fire, so planned burning there would not help in the same way.",
   "केवल 1 वैध है। परिच्छेद कहता है कि हर आग बुझा देने से ईंधन जमा होता है जिससे बेक़ाबू आग 'कहीं अधिक गर्म और व्यापक जलती है'; इसलिए जिस वन में लंबे समय से छोटी आगें रोकी गई हैं, उसमें गंभीर आग का जोखिम अधिक है। "
   "2 उसका खंडन करता है: 'जो विरले ही जलते हैं' वे नम उष्णकटिबंधीय वन आग से 'बुरी तरह क्षतिग्रस्त होते हैं', इसलिए वहाँ नियोजित आग उसी तरह सहायक नहीं होगी।",
   "conclusions",
   st=["A forest in which every small fire has been put out for many decades may face a more severe fire than one in which small fires were allowed.",
       "Planned burning would protect wet tropical forests just as it protects forests that have grown up with fire."],
   st_hi=["जिस वन में दशकों से हर छोटी आग बुझाई गई है, उसमें ऐसी आग का सामना हो सकता है जो उस वन से अधिक गंभीर हो जिसमें छोटी आगें होने दी गईं।",
          "नियोजित आग नम उष्णकटिबंधीय वनों की रक्षा भी वैसे ही करेगी जैसे वह आग के साथ विकसित हुए वनों की करती है।"],
   key=0)

# ------------------------------------------------------------------ P04 meat grown from cells (2)
p = passage("p04",
  "Meat can now be grown from animal cells in steel tanks, without raising and slaughtering animals. Singapore approved such meat for sale in 2020 and the United States in 2023. Its supporters point to the land, water and suffering it could spare. "
  "The climate case is less certain than it sounds. The tanks must be kept sterile and warm and fed with purified nutrients, all of which take a great deal of energy; some studies suggest that if that energy comes from fossil fuels, cell-grown meat could cause more emissions than some kinds of farmed meat. "
  "Its environmental promise therefore depends heavily on clean power and on cheaper ways of feeding the cells -- conditions that do not yet exist at scale.",
  "अब मांस को जानवरों को पालने और मारने के बिना, स्टील की टंकियों में जानवरों की कोशिकाओं से उगाया जा सकता है। सिंगापुर ने ऐसे मांस को 2020 में बिक्री की स्वीकृति दी और संयुक्त राज्य अमेरिका ने 2023 में। इसके समर्थक उस भूमि, पानी और पीड़ा की ओर संकेत करते हैं जो इससे बच सकती है। "
  "जलवायु का तर्क उतना निश्चित नहीं जितना लगता है। टंकियों को रोगाणु-रहित और गर्म रखना और उन्हें शुद्ध पोषक तत्व देना पड़ता है, और इन सबमें बहुत ऊर्जा लगती है; कुछ अध्ययन संकेत देते हैं कि यदि वह ऊर्जा जीवाश्म ईंधनों से आए, तो कोशिकाओं से उगाया मांस कुछ प्रकार के पाले गए मांस से अधिक उत्सर्जन कर सकता है। "
  "इसलिए उसका पर्यावरणीय वादा बहुत हद तक स्वच्छ बिजली और कोशिकाओं को पोषण देने के सस्ते तरीक़ों पर निर्भर है -- ऐसी परिस्थितियाँ जो अभी बड़े पैमाने पर मौजूद नहीं हैं।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage grants the benefits of cell-grown meat in land, water and suffering, but says its climate benefit depends on clean power and cheaper feeding, which do not yet exist at scale. "
   "It does not say the meat is certain to cut emissions, or that it is worse for the climate in every case -- only that it could be if powered by fossil fuels; and it does not call for a ban.",
   "परिच्छेद भूमि, पानी और पीड़ा में कोशिकाओं से उगाए मांस के लाभ मानता है, पर कहता है कि उसका जलवायु लाभ स्वच्छ बिजली और सस्ते पोषण पर निर्भर है, जो अभी बड़े पैमाने पर मौजूद नहीं। "
   "वह यह नहीं कहता कि यह मांस निश्चित रूप से उत्सर्जन घटाएगा, या हर स्थिति में जलवायु के लिए बुरा है -- केवल यह कि जीवाश्म ईंधनों से चलने पर ऐसा हो सकता है; और वह प्रतिबंध की माँग नहीं करता।",
   "crux",
   opts=["Meat grown from cells is certain to cut greenhouse emissions wherever it replaces farmed meat.",
         "Meat grown from cells is worse for the climate than farmed meat in every possible case.",
         "Cell-grown meat spares animals and land, but its climate benefit depends on clean energy.",
         "Meat grown from cells should be banned until it can be shown to be as cheap as farmed meat."],
   opts_hi=["कोशिकाओं से उगाया मांस जहाँ भी पाले गए मांस की जगह लेगा, वहाँ ग्रीनहाउस उत्सर्जन निश्चित रूप से घटाएगा।",
            "कोशिकाओं से उगाया मांस हर संभव स्थिति में पाले गए मांस से जलवायु के लिए बुरा है।",
            "कोशिकाओं से उगाया मांस जानवर और भूमि बचाता है, पर उसका जलवायु लाभ स्वच्छ ऊर्जा पर निर्भर है।",
            "कोशिकाओं से उगाए मांस पर तब तक प्रतिबंध रहे जब तक यह न दिखाया जा सके कि वह पाले गए मांस जितना सस्ता है।"],
   ans=2, pos=2)
RQ(p, "Specific Detail", "easy", "mcq",
   "According to the passage, why does growing meat from cells take so much energy?",
   "परिच्छेद के अनुसार, कोशिकाओं से मांस उगाने में इतनी ऊर्जा क्यों लगती है?",
   "The passage says the tanks 'must be kept sterile and warm and fed with purified nutrients, all of which take a great deal of energy'. It says nothing about cooling the meat, transporting it by air, or lighting the tanks.",
   "परिच्छेद कहता है कि टंकियों को 'रोगाणु-रहित और गर्म रखना और उन्हें शुद्ध पोषक तत्व देना पड़ता है, और इन सबमें बहुत ऊर्जा लगती है'। वह मांस को ठंडा करने, हवाई जहाज़ से ले जाने या टंकियों में रोशनी करने के बारे में कुछ नहीं कहता।",
   "why-it-takes-energy",
   opts=["The tanks must be kept sterile and warm, and fed with purified nutrients",
         "The finished meat must be frozen at once and kept frozen until it is sold",
         "The meat has to be flown to distant markets soon after it has been made",
         "The cells need bright light, day and night, in order to grow at all"],
   opts_hi=["टंकियों को रोगाणु-रहित और गर्म रखना और उन्हें शुद्ध पोषक तत्व देना पड़ता है",
            "तैयार मांस को तुरंत जमाना और बिकने तक जमाए रखना पड़ता है",
            "मांस बनने के तुरंत बाद उसे हवाई जहाज़ से दूर के बाज़ारों तक ले जाना पड़ता है",
            "कोशिकाओं को बढ़ने के लिए दिन-रात तेज़ रोशनी की आवश्यकता होती है"],
   ans=0, pos=0)

# ------------------------------------------------------------------ P05 Sher Shah's road (3)
p = passage("p05",
  "In the five years of his rule, from 1540 to 1545, Sher Shah Suri rebuilt and extended the great road that ran from Bengal across the plains to the north-west. Along it he set up sarais, rest houses for travellers at regular stages, dug wells and planted shade trees; the sarais also served as stations for a mounted postal service that carried news and orders quickly across the kingdom. "
  "He is remembered too for issuing a silver coin, the rupiya, whose name survives in the rupee. "
  "It is easy to credit the road to one ruler. In fact a highway along much the same route already linked the cities of the plains in Mauryan times, and the Mughals and later the British, who named it the Grand Trunk Road, kept rebuilding it. What Sher Shah added was a system of upkeep and services that made the road work as an instrument of government.",
  "1540 से 1545 तक के अपने पाँच वर्षों के शासन में शेरशाह सूरी ने उस महान सड़क का पुनर्निर्माण और विस्तार किया जो बंगाल से मैदानों को पार करती हुई उत्तर-पश्चिम तक जाती थी। उसके किनारे उन्होंने सरायें बनवाईं, यात्रियों के लिए नियमित पड़ावों पर विश्राम-गृह, कुएँ खुदवाए और छायादार पेड़ लगवाए; सरायें घुड़सवार डाक-सेवा के ठिकानों का भी काम करती थीं, जो समाचार और आदेश राज्य भर में तेज़ी से पहुँचाती थी। "
  "उन्हें चाँदी का एक सिक्का, रुपया, जारी करने के लिए भी याद किया जाता है, जिसका नाम 'रुपये' में आज भी जीवित है। "
  "सड़क का श्रेय एक शासक को दे देना आसान है। वास्तव में लगभग इसी मार्ग पर एक राजमार्ग मौर्य काल में ही मैदानों के नगरों को जोड़ता था, और मुग़ल और बाद में अंग्रेज़, जिन्होंने उसे ग्रैंड ट्रंक रोड नाम दिया, उसका पुनर्निर्माण करते रहे। शेरशाह ने जो जोड़ा वह रख-रखाव और सेवाओं की एक व्यवस्था थी जिसने सड़क को शासन के एक साधन के रूप में काम करने योग्य बनाया।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage describes what Sher Shah did for the road and then corrects a common simplification: the route is far older and was rebuilt by many, and his real contribution was the system of upkeep and services. "
   "It says a highway already ran along the route in Mauryan times, so he did not build it from nothing; the British named the road but did not first build it; and the coin is mentioned in passing, not as his chief achievement.",
   "परिच्छेद बताता है कि शेरशाह ने सड़क के लिए क्या किया और फिर एक आम सरलीकरण को सुधारता है: मार्ग कहीं पुराना है और अनेक ने उसका पुनर्निर्माण किया, और उनका वास्तविक योगदान रख-रखाव और सेवाओं की व्यवस्था थी। "
   "वह कहता है कि मौर्य काल में ही इस मार्ग पर एक राजमार्ग था, इसलिए उन्होंने उसे शून्य से नहीं बनाया; अंग्रेज़ों ने सड़क का नाम रखा पर उसे पहले नहीं बनाया; और सिक्के का उल्लेख प्रसंगवश है, उनकी मुख्य उपलब्धि के रूप में नहीं।",
   "crux",
   opts=["Sher Shah built the first road ever to cross the northern plains from Bengal to the north-west.",
         "The British were the first to build a road along the route that they named the Grand Trunk Road.",
         "Sher Shah's most lasting achievement was the silver coin from which the rupee takes its name.",
         "An old route long predates Sher Shah; he made it work through a system of upkeep and services."],
   opts_hi=["शेरशाह ने बंगाल से उत्तर-पश्चिम तक उत्तरी मैदानों को पार करने वाली पहली सड़क बनाई।",
            "अंग्रेज़ों ने ही सबसे पहले उस मार्ग पर सड़क बनाई जिसे उन्होंने ग्रैंड ट्रंक रोड नाम दिया।",
            "शेरशाह की सबसे स्थायी उपलब्धि चाँदी का वह सिक्का था जिससे रुपये को उसका नाम मिला।",
            "पुराना मार्ग शेरशाह से बहुत पहले का है; उन्होंने रख-रखाव और सेवाओं से उसे काम का बनाया।"],
   ans=3, pos=3)
RQ(p, "Specific Detail", "medium", "mcq",
   "According to the passage, which one of the following was NOT a purpose served by the sarais along the road?",
   "परिच्छेद के अनुसार, निम्नलिखित में से कौन-सा उद्देश्य सड़क के किनारे की सरायों से पूरा नहीं होता था?",
   "The passage says the sarais were rest houses for travellers and also served as stations for the mounted postal service carrying news and orders. Minting the rupiya is mentioned separately, as something Sher Shah did, not as a use of the sarais.",
   "परिच्छेद कहता है कि सरायें यात्रियों के लिए विश्राम-गृह थीं और समाचार व आदेश ले जाने वाली घुड़सवार डाक-सेवा के ठिकानों का भी काम करती थीं। रुपया ढालने का उल्लेख अलग से है, शेरशाह के एक काम के रूप में, सरायों के उपयोग के रूप में नहीं।",
   "what-the-sarais-did-not-do",
   opts=["Giving travellers a place to rest at regular stages of the journey",
         "Minting the silver coins that Sher Shah issued",
         "Serving as stations for a mounted postal service",
         "Helping news and orders travel quickly across the kingdom"],
   opts_hi=["यात्रा के नियमित पड़ावों पर यात्रियों को विश्राम का स्थान देना",
            "शेरशाह द्वारा जारी चाँदी के सिक्के ढालना",
            "घुड़सवार डाक-सेवा के ठिकानों का काम करना",
            "समाचारों और आदेशों को राज्य भर में तेज़ी से पहुँचाने में सहायता करना"],
   ans=1, pos=1)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Both are valid. 1: the passage says the road was rebuilt by the Mughals and the British after Sher Shah and existed in Mauryan times before him; so the road we know is the work of many rulers over many centuries. "
   "2: it says the sarais served as stations for a postal service that carried news and orders quickly, and that his system made the road work 'as an instrument of government'; so the road helped a ruler govern a large kingdom from its centre.",
   "दोनों वैध हैं। 1: परिच्छेद कहता है कि शेरशाह के बाद मुग़लों और अंग्रेज़ों ने सड़क का पुनर्निर्माण किया और उनसे पहले मौर्य काल में वह मौजूद थी; इसलिए जिस सड़क को हम जानते हैं वह अनेक शताब्दियों में अनेक शासकों का काम है। "
   "2: वह कहता है कि सरायें ऐसी डाक-सेवा के ठिकाने थीं जो समाचार और आदेश तेज़ी से ले जाती थी, और कि उनकी व्यवस्था ने सड़क को 'शासन के एक साधन' के रूप में काम करने योग्य बनाया; इसलिए सड़क ने एक शासक को अपने केंद्र से बड़े राज्य पर शासन करने में सहायता की।",
   "conclusions",
   st=["The road known today as the Grand Trunk Road is the work of many rulers over many centuries.",
       "A fast postal service along the road helped a ruler govern a large kingdom from its centre."],
   st_hi=["आज ग्रैंड ट्रंक रोड के नाम से जानी जाने वाली सड़क अनेक शताब्दियों में अनेक शासकों का काम है।",
          "सड़क के किनारे तेज़ डाक-सेवा ने एक शासक को अपने केंद्र से बड़े राज्य पर शासन करने में सहायता की।"],
   key=2)

# ------------------------------------------------------------------ P06 the anti-defection law (2)
p = passage("p06",
  "Before 1985, legislators in India often changed parties for office or money, and governments fell overnight. The Tenth Schedule, added to the Constitution that year, ended the trade: a member who gives up his party, or votes against its instructions in the House, can be disqualified, with an exception when two-thirds of a party's legislators merge with another. "
  "Governments became steadier. But the remedy has a cost. Because the party's instruction, the whip, can be issued on almost any vote, a member who disagrees on a bill must choose between conscience and seat, and debate in the House matters less when every vote is decided in advance. "
  "Some have suggested confining the whip to votes that could bring down a government, such as confidence motions and budgets, leaving members free on other bills.",
  "1985 से पहले भारत में विधायक प्रायः पद या धन के लिए दल बदल लेते थे, और सरकारें रातोंरात गिर जाती थीं। उस वर्ष संविधान में जोड़ी गई दसवीं अनुसूची ने यह व्यापार समाप्त किया: जो सदस्य अपना दल छोड़ देता है, या सदन में उसके निर्देशों के विरुद्ध मत देता है, उसे अयोग्य ठहराया जा सकता है, इस अपवाद के साथ कि जब किसी दल के दो-तिहाई विधायक किसी दूसरे दल में विलय कर लें। "
  "सरकारें अधिक स्थिर हुईं। पर इस उपाय की एक क़ीमत है। चूँकि दल का निर्देश, व्हिप, लगभग किसी भी मतदान पर जारी किया जा सकता है, किसी विधेयक पर असहमत सदस्य को अंतरात्मा और सीट में से एक चुनना पड़ता है, और जब हर मत पहले से तय हो तो सदन की बहस का महत्त्व घट जाता है। "
  "कुछ लोगों ने सुझाया है कि व्हिप को उन मतदानों तक सीमित किया जाए जो सरकार गिरा सकते हैं, जैसे विश्वास प्रस्ताव और बजट, और अन्य विधेयकों पर सदस्यों को स्वतंत्र छोड़ा जाए।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage credits the anti-defection law with steadier governments, then names its cost -- members bound on nearly every vote, debate weakened -- and reports a proposal to limit the whip to votes that could bring a government down. "
   "It does not call for repealing the law, whose benefit it records; it does not say the law has failed to reduce defections; and it reports the merger exception without saying it should be widened.",
   "परिच्छेद दल-बदल विरोधी क़ानून को अधिक स्थिर सरकारों का श्रेय देता है, फिर उसकी क़ीमत बताता है -- लगभग हर मतदान पर बँधे सदस्य, कमज़ोर बहस -- और व्हिप को उन मतदानों तक सीमित करने का प्रस्ताव बताता है जो सरकार गिरा सकते हैं। "
   "वह क़ानून को रद्द करने की माँग नहीं करता, जिसका लाभ वह दर्ज करता है; वह यह नहीं कहता कि क़ानून दल-बदल घटाने में विफल रहा; और वह विलय के अपवाद का उल्लेख करता है, उसे बढ़ाने की बात कहे बिना।",
   "crux",
   opts=["The law steadied governments but limits members' freedom, which a narrower whip might ease.",
         "The anti-defection law has done more harm than good and should be repealed as soon as possible.",
         "The anti-defection law has failed to make any difference to how often legislators change parties.",
         "The exception for mergers should be widened so that smaller groups of legislators may also merge."],
   opts_hi=["क़ानून ने सरकारें स्थिर कीं पर सदस्यों की स्वतंत्रता सीमित की, जिसे सीमित व्हिप घटा सकता है।",
            "दल-बदल विरोधी क़ानून ने लाभ से अधिक हानि की है और उसे जितनी जल्दी हो सके रद्द कर देना चाहिए।",
            "दल-बदल विरोधी क़ानून से इस पर कोई अंतर नहीं पड़ा कि विधायक कितनी बार दल बदलते हैं।",
            "विलय के अपवाद को बढ़ाया जाए ताकि विधायकों के छोटे समूह भी विलय कर सकें।"],
   ans=0, pos=0)
RQ(p, "Inference", "hard", "mcq",
   "If the whip were confined to confidence motions and budgets, as some have suggested, which one of the following would the passage expect?",
   "यदि व्हिप को, जैसा कुछ लोगों ने सुझाया है, विश्वास प्रस्तावों और बजट तक सीमित कर दिया जाए, तो परिच्छेद के अनुसार निम्नलिखित में से क्या होगा?",
   "The proposal leaves members free on other bills while keeping the whip on the votes that could bring a government down. So a member could vote against the party on an ordinary bill without being disqualified, while governments stayed protected on confidence and budget votes. "
   "Governments falling overnight again ignores that the whip would still bind on confidence motions; no member could switch parties freely, since giving up one's party still disqualifies; and the merger rule is untouched by the proposal.",
   "प्रस्ताव अन्य विधेयकों पर सदस्यों को स्वतंत्र छोड़ता है और व्हिप को उन मतदानों पर बनाए रखता है जो सरकार गिरा सकते हैं। इसलिए कोई सदस्य किसी साधारण विधेयक पर अयोग्य हुए बिना दल के विरुद्ध मत दे सकता, जबकि विश्वास और बजट के मतदानों पर सरकारें सुरक्षित रहतीं। "
   "सरकारों का फिर रातोंरात गिरना इसकी अनदेखी करता है कि विश्वास प्रस्तावों पर व्हिप तब भी बाँधता; कोई सदस्य खुलकर दल नहीं बदल सकता, क्योंकि अपना दल छोड़ना तब भी अयोग्य बनाता; और प्रस्ताव विलय के नियम को छूता नहीं।",
   "what-a-narrower-whip-would-do",
   opts=["Governments would again be liable to fall overnight whenever a few members changed their minds.",
         "Any member could switch to another party at any time without risk of losing the seat.",
         "Mergers between parties would need fewer than two-thirds of a party's legislators.",
         "A member could vote against the party on an ordinary bill without being disqualified."],
   opts_hi=["कुछ सदस्यों के मन बदलते ही सरकारें फिर रातोंरात गिरने की आशंका में आ जातीं।",
            "कोई भी सदस्य किसी भी समय सीट खोने के जोखिम के बिना दूसरे दल में जा सकता।",
            "दलों के बीच विलय के लिए किसी दल के दो-तिहाई से कम विधायक पर्याप्त होते।",
            "कोई सदस्य किसी साधारण विधेयक पर अयोग्य हुए बिना दल के विरुद्ध मत दे सकता।"],
   ans=3, pos=3)

# ------------------------------------------------------------------ P07 India's own satellite navigation (2)
p = passage("p07",
  "Phones, ships, aircraft and power grids rely on signals from navigation satellites, and for decades most users in India relied on the American system. A country that depends on a service run by another government accepts that the service could be degraded or withheld when that government chooses. "
  "India therefore built its own regional system, now called NavIC, whose satellites cover the country and a band of about 1,500 km around it. "
  "Owning the system is not the same as using it. Few phones were made to receive its signals in its early years, and some of its first satellites lost the atomic clocks on which accurate positions depend, so that replacements had to be launched. "
  "Strategic independence is achieved only when the system is maintained and actually built into the devices people use.",
  "फ़ोन, जहाज़, विमान और बिजली ग्रिड नेविगेशन उपग्रहों के संकेतों पर निर्भर हैं, और दशकों तक भारत में अधिकांश उपयोगकर्ता अमेरिकी प्रणाली पर निर्भर रहे। जो देश किसी दूसरी सरकार द्वारा चलाई जाने वाली सेवा पर निर्भर है, वह यह स्वीकार करता है कि वह सरकार जब चाहे सेवा को कमज़ोर कर सकती है या रोक सकती है। "
  "इसलिए भारत ने अपनी क्षेत्रीय प्रणाली बनाई, जिसे अब NavIC कहते हैं, जिसके उपग्रह देश और उसके चारों ओर लगभग 1,500 किमी की पट्टी को कवर करते हैं। "
  "प्रणाली का स्वामी होना उसका प्रयोग करने जैसा नहीं है। आरंभिक वर्षों में कम ही फ़ोन उसके संकेत ग्रहण करने के लिए बनाए गए, और उसके कुछ पहले उपग्रहों की वे परमाणु घड़ियाँ ख़राब हो गईं जिन पर सटीक स्थिति निर्भर करती है, जिससे बदले में उपग्रह छोड़ने पड़े। "
  "सामरिक स्वतंत्रता तभी मिलती है जब प्रणाली का रख-रखाव हो और वह वास्तव में उन उपकरणों में लगी हो जिनका लोग प्रयोग करते हैं।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage explains why a country builds its own navigation system and then warns that owning it is not enough: independence comes only when the system is maintained and built into everyday devices. "
   "It does not say the American system should be abandoned; it says NavIC covers India and a band around it, not the whole world; and it reports the clock failures as a problem that required replacements, not as a reason to give the system up.",
   "परिच्छेद बताता है कि कोई देश अपनी नेविगेशन प्रणाली क्यों बनाता है और फिर चेताता है कि उसका स्वामी होना पर्याप्त नहीं: स्वतंत्रता तभी आती है जब प्रणाली का रख-रखाव हो और वह रोज़मर्रा के उपकरणों में लगी हो। "
   "वह यह नहीं कहता कि अमेरिकी प्रणाली छोड़ दी जाए; वह कहता है कि NavIC भारत और उसके चारों ओर की एक पट्टी को कवर करता है, पूरी दुनिया को नहीं; और वह घड़ियों की ख़राबी को ऐसी समस्या के रूप में बताता है जिसके लिए बदले में उपग्रह चाहिए थे, प्रणाली छोड़ने के कारण के रूप में नहीं।",
   "crux",
   opts=["India should stop using the American system altogether now that it has a system of its own.",
         "Owning a system gives independence only if it is kept working and used in devices.",
         "NavIC can guide users anywhere in the world as accurately as any other system can.",
         "The failure of some atomic clocks shows that India should give up running its own system."],
   opts_hi=["भारत को अब अपनी प्रणाली होने के कारण अमेरिकी प्रणाली का प्रयोग पूरी तरह बंद कर देना चाहिए।",
            "अपनी प्रणाली स्वतंत्रता तभी देती है जब वह चालू रहे और उपकरणों में प्रयुक्त हो।",
            "NavIC उपयोगकर्ताओं को दुनिया में कहीं भी किसी अन्य प्रणाली जितनी सटीकता से मार्ग दिखा सकता है।",
            "कुछ परमाणु घड़ियों की ख़राबी दिखाती है कि भारत को अपनी प्रणाली चलाना छोड़ देना चाहिए।"],
   ans=1, pos=1)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Neither is valid. 1 goes too far: the passage says few phones received NavIC signals in the early years, but not that no phone can now receive them, nor that this will always be so. "
   "2 contradicts the passage's logic: a system whose satellites cover India and 1,500 km around it would not by itself serve an Indian ship far out in another ocean, so it cannot replace every foreign system everywhere.",
   "कोई भी वैध नहीं। 1 बहुत आगे जाता है: परिच्छेद कहता है कि आरंभिक वर्षों में कम ही फ़ोन NavIC के संकेत ग्रहण करते थे, यह नहीं कि अब कोई फ़ोन उन्हें ग्रहण नहीं कर सकता, और न यह कि ऐसा हमेशा रहेगा। "
   "2 परिच्छेद के तर्क का खंडन करता है: जिस प्रणाली के उपग्रह भारत और उसके चारों ओर 1,500 किमी को कवर करते हैं, वह अपने आप किसी दूर के महासागर में स्थित भारतीय जहाज़ की सेवा नहीं करेगी, इसलिए वह हर जगह हर विदेशी प्रणाली की जगह नहीं ले सकती।",
   "conclusions",
   st=["No phone can receive NavIC signals, and none ever will.",
       "With NavIC, an Indian ship anywhere in the world no longer needs any foreign navigation system."],
   st_hi=["कोई भी फ़ोन NavIC के संकेत ग्रहण नहीं कर सकता, और कभी नहीं करेगा।",
          "NavIC के होते हुए दुनिया में कहीं भी किसी भारतीय जहाज़ को किसी विदेशी नेविगेशन प्रणाली की आवश्यकता नहीं रहती।"],
   key=3)

# ------------------------------------------------------------------ P08 the black soils of the Deccan (3)
p = passage("p08",
  "Across much of the Deccan, the soil is black. It formed as the vast sheets of lava that once spread over the plateau weathered into fine clay, and it is often called black cotton soil because it suits that crop so well. "
  "Its clay holds water for a long time, a gift in a region of uncertain rain, and it is rich in lime, magnesium and potash, though usually poor in phosphorus. "
  "The same clay makes it awkward. It swells and turns sticky when wet, so that it is hard to plough after heavy rain, and it shrinks and cracks deeply when dry -- cracks that let air into the soil but also crack the walls and roads built on it. "
  "Black soil is neither simply fertile nor simply difficult; what it offers depends on how well its users work with its habits of swelling and shrinking.",
  "दक्कन के बड़े भाग में मिट्टी काली है। यह तब बनी जब कभी पठार पर फैली लावा की विशाल परतें अपक्षयित होकर बारीक चिकनी मिट्टी में बदल गईं, और इसे प्रायः काली कपास मिट्टी कहा जाता है क्योंकि यह उस फ़सल के लिए बहुत उपयुक्त है। "
  "इसकी चिकनी मिट्टी लंबे समय तक पानी रोके रखती है, जो अनिश्चित वर्षा वाले क्षेत्र में एक वरदान है, और यह चूना, मैग्नीशियम और पोटाश से समृद्ध है, यद्यपि प्रायः फ़ॉस्फ़ोरस में कमज़ोर। "
  "यही चिकनी मिट्टी इसे कठिन भी बनाती है। गीली होने पर यह फूलती है और चिपचिपी हो जाती है, जिससे भारी वर्षा के बाद इसे जोतना कठिन होता है, और सूखने पर यह सिकुड़ती है और गहरी दरारें बनाती है -- दरारें जो मिट्टी में हवा पहुँचाती हैं पर उस पर बनी दीवारों और सड़कों में भी दरार डाल देती हैं। "
  "काली मिट्टी न केवल उपजाऊ है न केवल कठिन; वह क्या देती है, यह इस पर निर्भर है कि उसका प्रयोग करने वाले उसके फूलने और सिकुड़ने के स्वभाव के साथ कितनी अच्छी तरह काम करते हैं।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage presents both sides of black soil -- it holds water and suits cotton, but swells, sticks and cracks -- and concludes that what it offers depends on working with those habits. "
   "It does not call it the most fertile soil in India; it says the soil is usually poor in phosphorus, not rich in every nutrient; and it notes cracks in walls and roads without saying nothing can be built on it.",
   "परिच्छेद काली मिट्टी के दोनों पक्ष रखता है -- वह पानी रोकती है और कपास के लिए उपयुक्त है, पर फूलती, चिपकती और दरकती है -- और निष्कर्ष निकालता है कि वह क्या देती है, यह उन स्वभावों के साथ काम करने पर निर्भर है। "
   "वह उसे भारत की सबसे उपजाऊ मिट्टी नहीं कहता; वह कहता है कि मिट्टी प्रायः फ़ॉस्फ़ोरस में कमज़ोर है, हर पोषक तत्व में समृद्ध नहीं; और वह दीवारों और सड़कों में दरारों का उल्लेख करता है, यह कहे बिना कि उस पर कुछ बनाया ही नहीं जा सकता।",
   "crux",
   opts=["Black soil is the most fertile soil in India and can grow any crop well without any special care.",
         "Black soil is rich in every nutrient that crops need, phosphorus included, and needs no fertiliser.",
         "Black soil has real gifts and real drawbacks, both coming from the way its clay behaves.",
         "Nothing can safely be built on black soil, because its deep cracks bring down walls and roads."],
   opts_hi=["काली मिट्टी भारत की सबसे उपजाऊ मिट्टी है और किसी विशेष देखभाल के बिना कोई भी फ़सल अच्छी उगा सकती है।",
            "काली मिट्टी फ़ॉस्फ़ोरस सहित हर उस पोषक तत्व से समृद्ध है जो फ़सलों को चाहिए, और उसे कोई उर्वरक नहीं चाहिए।",
            "काली मिट्टी में वास्तविक गुण और वास्तविक कमियाँ हैं, दोनों उसकी चिकनी मिट्टी के व्यवहार से आती हैं।",
            "काली मिट्टी पर सुरक्षित रूप से कुछ भी नहीं बनाया जा सकता, क्योंकि उसकी गहरी दरारें दीवारें और सड़कें गिरा देती हैं।"],
   ans=2, pos=2)
RQ(p, "Inference", "hard", "mcq",
   "Which one of the following would the passage most expect a farmer on black soil to find?",
   "परिच्छेद के अनुसार, काली मिट्टी पर खेती करने वाले किसान को निम्नलिखित में से क्या मिलने की सबसे अधिक अपेक्षा है?",
   "The soil 'holds water for a long time', so after the rains stop it keeps moisture longer than a soil that drains quickly -- a crop can draw on it into the dry weeks. "
   "Ploughing is hardest just after heavy rain, when the soil is sticky, not easiest; the soil is usually poor in phosphorus, so it may need that nutrient added; and the passage gives no ground for expecting it to suit no crop but cotton.",
   "मिट्टी 'लंबे समय तक पानी रोके रखती है', इसलिए वर्षा रुकने के बाद वह जल्दी पानी बहा देने वाली मिट्टी से अधिक देर तक नमी रखती है -- फ़सल सूखे सप्ताहों में भी उससे पानी ले सकती है। "
   "जुताई भारी वर्षा के ठीक बाद, जब मिट्टी चिपचिपी होती है, सबसे कठिन होती है, सबसे आसान नहीं; मिट्टी प्रायः फ़ॉस्फ़ोरस में कमज़ोर है, इसलिए उसमें यह पोषक तत्व मिलाना पड़ सकता है; और परिच्छेद यह मानने का कोई आधार नहीं देता कि वह कपास के अलावा किसी फ़सल के लिए उपयुक्त नहीं।",
   "what-a-farmer-on-black-soil-finds",
   opts=["Ploughing is easiest just after heavy rain, when the soil is soft and wet.",
         "The soil keeps moisture after the rains end longer than a quickly draining soil.",
         "The soil never needs phosphorus to be added, since it is rich in every nutrient.",
         "No crop other than cotton can be grown on the soil with any success at all."],
   opts_hi=["भारी वर्षा के ठीक बाद, जब मिट्टी नरम और गीली हो, जुताई सबसे आसान होती है।",
            "वर्षा समाप्त होने के बाद मिट्टी जल्दी पानी बहाने वाली मिट्टी से अधिक देर तक नमी रखती है।",
            "मिट्टी में कभी फ़ॉस्फ़ोरस मिलाने की आवश्यकता नहीं, क्योंकि वह हर पोषक तत्व से समृद्ध है।",
            "उस मिट्टी पर कपास के अलावा कोई भी फ़सल किसी भी सफलता के साथ नहीं उगाई जा सकती।"],
   ans=1, pos=1)
RQ(p, "Specific Detail", "medium", "mcq",
   "According to the passage, how was the black soil of the Deccan formed?",
   "परिच्छेद के अनुसार, दक्कन की काली मिट्टी कैसे बनी?",
   "The passage says it formed 'as the vast sheets of lava that once spread over the plateau weathered into fine clay'. It says nothing of silt from rivers, of fallen leaves or of wind-blown dust.",
   "परिच्छेद कहता है कि यह तब बनी 'जब कभी पठार पर फैली लावा की विशाल परतें अपक्षयित होकर बारीक चिकनी मिट्टी में बदल गईं'। वह नदियों की गाद, गिरी पत्तियों या हवा से उड़कर आई धूल के बारे में कुछ नहीं कहता।",
   "how-black-soil-formed",
   opts=["From the weathering of lava that once spread over the plateau",
         "From silt laid down by rivers flooding the plateau each year",
         "From leaves that have fallen and rotted in its forests for ages",
         "From fine dust carried onto the plateau by winds from the desert"],
   opts_hi=["उस लावा के अपक्षय से जो कभी पठार पर फैला था",
            "उस गाद से जो हर वर्ष पठार पर बाढ़ लाने वाली नदियाँ बिछाती हैं",
            "उन पत्तियों से जो युगों से उसके वनों में गिरकर सड़ती रही हैं",
            "उस बारीक धूल से जिसे मरुस्थल की हवाएँ पठार पर ले आती हैं"],
   ans=0, pos=0)

# ------------------------------------------------------------------ P09 rights and the arithmetic of lives (2)
p = passage("p09",
  "A surgeon has five patients who will die without transplants and one healthy visitor whose organs would save them all. If the right act is always the one that produces the most good, the surgeon should sacrifice the visitor: five lives outweigh one. Almost everyone recoils from this conclusion. "
  "The recoil suggests that people have rights that cannot simply be added up and traded -- that some things may not be done to a person even to save more lives. "
  "Yet it would be too quick to conclude that lives may never be weighed. Governments do it constantly: a speed limit, a hospital budget or a safety rule for factories trades some risk to life against cost and convenience. "
  "The difficulty is to say where weighing is legitimate and where it becomes a licence to use some people as means for others.",
  "एक शल्य-चिकित्सक के पाँच रोगी हैं जो प्रत्यारोपण के बिना मर जाएँगे, और एक स्वस्थ आगंतुक है जिसके अंग उन सबको बचा सकते हैं। यदि सही कार्य हमेशा वही है जो सबसे अधिक भला करे, तो चिकित्सक को आगंतुक की बलि दे देनी चाहिए: पाँच जीवन एक से भारी हैं। लगभग हर कोई इस निष्कर्ष से पीछे हटता है। "
  "यह पीछे हटना संकेत देता है कि लोगों के ऐसे अधिकार हैं जिन्हें बस जोड़कर और अदला-बदली करके नहीं निपटाया जा सकता -- कि किसी व्यक्ति के साथ कुछ बातें अधिक जीवन बचाने के लिए भी नहीं की जा सकतीं। "
  "फिर भी यह निष्कर्ष निकालना जल्दबाज़ी होगी कि जीवनों को कभी तौला ही नहीं जा सकता। सरकारें लगातार ऐसा करती हैं: गति-सीमा, अस्पताल का बजट या कारख़ानों के लिए सुरक्षा नियम -- हर एक जीवन के कुछ जोखिम को लागत और सुविधा के सामने तौलता है। "
  "कठिनाई यह बताने में है कि तौलना कहाँ वैध है और कहाँ वह कुछ लोगों को दूसरों के साधन के रूप में प्रयोग करने का अनुमति-पत्र बन जाता है।")
RQ(p, "Main Idea", "hard", "mcq", CRUX, CRUX_HI,
   "The passage uses the surgeon case to show that some rights resist being added up, then adds that public policy weighs lives all the time, and ends on the real difficulty: telling legitimate weighing apart from using some people as means for others. "
   "It rejects the surgeon's sum, so it does not say the most good should always be done; it says lives are weighed constantly, the opposite of 'never'; and it treats speed limits and budgets as ordinary weighing, not as wrongs like the surgeon's.",
   "परिच्छेद शल्य-चिकित्सक के मामले से दिखाता है कि कुछ अधिकार जोड़-घटाव का विरोध करते हैं, फिर जोड़ता है कि सार्वजनिक नीति हर समय जीवनों को तौलती है, और वास्तविक कठिनाई पर समाप्त होता है: वैध तौल को कुछ लोगों को दूसरों के साधन के रूप में प्रयोग करने से अलग करना। "
   "वह चिकित्सक के हिसाब को अस्वीकार करता है, इसलिए यह नहीं कहता कि हमेशा सबसे अधिक भला किया जाए; वह कहता है कि जीवन लगातार तौले जाते हैं, जो 'कभी नहीं' का उलटा है; और वह गति-सीमा और बजट को साधारण तौल मानता है, चिकित्सक जैसे अनुचित कार्य नहीं।",
   "crux",
   opts=["The right act is always the one that saves the greatest number of lives, whatever it requires.",
         "Lives must never be weighed against one another, in medicine or in any public policy.",
         "Speed limits and hospital budgets are as wrong as the surgeon's sacrifice of the visitor.",
         "Some rights resist being traded, yet lives are often weighed; the hard part is the line."],
   opts_hi=["सही कार्य हमेशा वही है जो सबसे अधिक जीवन बचाए, उसके लिए चाहे जो करना पड़े।",
            "चिकित्सा में या किसी भी सार्वजनिक नीति में जीवनों को कभी एक-दूसरे के सामने नहीं तौलना चाहिए।",
            "गति-सीमा और अस्पताल के बजट उतने ही अनुचित हैं जितनी चिकित्सक द्वारा आगंतुक की बलि।",
            "कुछ अधिकारों का सौदा नहीं होता, फिर भी जीवन प्रायः तौले जाते हैं; कठिन भाग रेखा खींचना है।"],
   ans=3, pos=3)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Both are valid. The passage reads the general recoil from the surgeon's choice as a sign that some things 'may not be done to a person even to save more lives' -- a limit that a bare count of lives saved cannot capture (1). "
   "It also says it 'would be too quick to conclude' that lives may never be weighed, and gives speed limits, hospital budgets and factory rules as cases where governments trade some risk to life against cost; it asks only where such weighing stops being legitimate (2).",
   "दोनों वैध हैं। परिच्छेद चिकित्सक के चुनाव से सामान्य रूप से पीछे हटने को इस बात का संकेत मानता है कि किसी व्यक्ति के साथ 'कुछ बातें अधिक जीवन बचाने के लिए भी नहीं की जा सकतीं' -- एक सीमा जिसे बचाए गए जीवनों की केवल गिनती नहीं पकड़ सकती (1)। "
   "वह यह भी कहता है कि यह निष्कर्ष निकालना 'जल्दबाज़ी होगी' कि जीवनों को कभी तौला ही नहीं जा सकता, और गति-सीमा, अस्पताल के बजट और कारख़ानों के नियमों को ऐसे उदाहरण बताता है जहाँ सरकारें लागत के सामने जीवन के कुछ जोखिम का सौदा करती हैं; वह केवल यह पूछता है कि ऐसा तौलना कहाँ वैध नहीं रहता (2)।",
   "conclusions",
   st=["On the passage's view, counting lives saved cannot by itself settle what may be done to a person.",
       "The passage treats it as sometimes legitimate for a government to accept some risk to life in return for lower cost."],
   st_hi=["परिच्छेद के मत में बचाए गए जीवनों की गिनती अकेले यह तय नहीं कर सकती कि किसी व्यक्ति के साथ क्या किया जा सकता है।",
          "परिच्छेद यह मानता है कि कभी-कभी सरकार के लिए कम लागत के बदले जीवन का कुछ जोखिम स्वीकार करना वैध है।"],
   key=2)

# ------------------------------------------------------------------ P10 a carbon tax at the border (2)
p = passage("p10",
  "From 2026 the European Union charges importers of goods such as steel, aluminium, cement and fertilisers for the carbon emitted in making them, at the price its own producers pay for their emissions. The aim is to stop European firms that pay for carbon from being undercut by imports from places where carbon is free, and to stop production simply moving abroad. "
  "Exporting countries, India among them, object that the charge is a trade barrier imposed by one side, and that it ignores the principle that richer countries, which emitted most in the past, should bear more of the burden. "
  "The charge has another effect, however. Importers may deduct any carbon price already paid in the country of origin, so a country that taxes carbon at home keeps that revenue instead of handing it to Europe's treasury.",
  "2026 से यूरोपीय संघ इस्पात, एल्युमिनियम, सीमेंट और उर्वरक जैसी वस्तुओं के आयातकों से उन्हें बनाने में निकले कार्बन का शुल्क लेता है, उसी मूल्य पर जो उसके अपने उत्पादक अपने उत्सर्जन के लिए चुकाते हैं। उद्देश्य यह है कि कार्बन के लिए भुगतान करने वाली यूरोपीय फ़र्में उन स्थानों से आने वाले आयातों से न पिछड़ें जहाँ कार्बन मुफ़्त है, और उत्पादन बस विदेश न चला जाए। "
  "भारत सहित निर्यातक देश आपत्ति करते हैं कि यह शुल्क एक पक्ष द्वारा थोपी गई व्यापार बाधा है, और कि यह इस सिद्धांत की अनदेखी करता है कि धनी देश, जिन्होंने अतीत में सबसे अधिक उत्सर्जन किया, बोझ का बड़ा भाग उठाएँ। "
  "पर इस शुल्क का एक और प्रभाव है। आयातक मूल देश में पहले से चुकाए गए किसी भी कार्बन मूल्य को घटा सकते हैं, इसलिए जो देश अपने यहाँ कार्बन पर कर लगाता है वह उस राजस्व को यूरोप के ख़ज़ाने को सौंपने के बजाय अपने पास रखता है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage explains the EU's border charge and its purpose, records the objections of exporting countries such as India, and points out that a carbon price paid at home is deducted, so such a country keeps the revenue. "
   "It does not say the charge applies to all imports -- it names carbon-intensive goods; it reports India's objection without saying India accepts the charge; and the deduction applies to any carbon price paid at home, not a reason for India to stop exporting.",
   "परिच्छेद यूरोपीय संघ के सीमा-शुल्क और उसके उद्देश्य को समझाता है, भारत जैसे निर्यातक देशों की आपत्तियाँ दर्ज करता है, और बताता है कि घर पर चुकाया कार्बन मूल्य घटाया जाता है, इसलिए ऐसा देश राजस्व अपने पास रखता है। "
   "वह यह नहीं कहता कि शुल्क सभी आयातों पर लगता है -- वह कार्बन-सघन वस्तुओं के नाम लेता है; वह भारत की आपत्ति बताता है, यह कहे बिना कि भारत शुल्क स्वीकार करता है; और कटौती घर पर चुकाए किसी भी कार्बन मूल्य पर लागू है, यह भारत के निर्यात बंद करने का कारण नहीं।",
   "crux",
   opts=["The EU now charges every single good imported into it for the carbon emitted in making it.",
         "The EU charge is disputed, but a country that prices carbon at home keeps the revenue.",
         "India has accepted the EU's border charge as fair and has raised no objection to it.",
         "India should stop exporting steel and cement to Europe so as to avoid paying the charge."],
   opts_hi=["यूरोपीय संघ अब उसमें आयात होने वाली हर वस्तु पर उसे बनाने में निकले कार्बन का शुल्क लेता है।",
            "यूरोपीय संघ का शुल्क विवादित है, पर घर पर कार्बन-मूल्य लगाने वाला देश राजस्व अपने पास रखता है।",
            "भारत ने यूरोपीय संघ के सीमा-शुल्क को उचित मानकर स्वीकार कर लिया है और उस पर कोई आपत्ति नहीं की है।",
            "भारत को शुल्क चुकाने से बचने के लिए यूरोप को इस्पात और सीमेंट का निर्यात बंद कर देना चाहिए।"],
   ans=1, pos=1)
RQ(p, "Inference", "hard", "mcq", IMPL, IMPL_HI,
   "Because importers may deduct a carbon price already paid at home, a charge collected by an exporting country's own treasury replaces part of what would otherwise go to Europe. Pricing carbon at home is therefore a way for an exporter to keep the revenue that the charge would otherwise send abroad. "
   "The passage does not say the charge will end trade, nor that it ignores where goods come from -- it depends on the carbon paid at origin; and it gives no ground for saying European producers pay nothing for carbon.",
   "चूँकि आयातक घर पर पहले से चुकाए कार्बन मूल्य को घटा सकते हैं, किसी निर्यातक देश के अपने ख़ज़ाने द्वारा वसूला गया शुल्क उस भाग की जगह ले लेता है जो अन्यथा यूरोप जाता। इसलिए घर पर कार्बन का मूल्य लगाना किसी निर्यातक के लिए उस राजस्व को अपने पास रखने का साधन है जिसे शुल्क अन्यथा विदेश भेज देता। "
   "परिच्छेद यह नहीं कहता कि शुल्क व्यापार समाप्त कर देगा, न यह कि वह वस्तुओं के मूल की अनदेखी करता है -- वह मूल देश में चुकाए कार्बन पर निर्भर है; और वह यह कहने का कोई आधार नहीं देता कि यूरोपीय उत्पादक कार्बन के लिए कुछ नहीं चुकाते।",
   "what-the-deduction-implies",
   opts=["The border charge will bring all trade in steel and cement with Europe to an end.",
         "The charge is the same for every exporter, whatever carbon price it already pays at home.",
         "An exporter that prices carbon at home can keep revenue otherwise bound for Europe.",
         "European producers of steel and cement pay nothing at all for the carbon they emit."],
   opts_hi=["सीमा-शुल्क यूरोप के साथ इस्पात और सीमेंट का सारा व्यापार समाप्त कर देगा।",
            "शुल्क हर निर्यातक के लिए समान है, वह घर पर पहले से कार्बन का चाहे जो मूल्य चुकाता हो।",
            "घर पर कार्बन-मूल्य लगाने वाला निर्यातक अन्यथा यूरोप जाने वाला राजस्व रख सकता है।",
            "इस्पात और सीमेंट के यूरोपीय उत्पादक अपने उत्सर्जित कार्बन के लिए कुछ भी नहीं चुकाते।"],
   ans=2, pos=0)
