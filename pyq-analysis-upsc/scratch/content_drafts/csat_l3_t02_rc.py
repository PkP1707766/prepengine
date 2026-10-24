# -*- coding: utf-8 -*-
"""CSAT Level 3 · Test 2 -- Reading Comprehension: 10 original passages, 28 items (8 x 3, 2 x 2).

Level 3 passages carry a turn in the argument -- a claim, then its limit -- so that the items test where the author
stops as much as what the author says. Themes, none used in Level 2 Tests 1-7, Level 1 Minis 1-3 or Level 3 Test 1:
comparative advantage, sunk costs, placebo and nocebo effects, coral bleaching, the case for free speech, the journey
of place-value numerals from India, elected village councils and the few who capture them, automation bias, wolves
and the rivers they were said to change, and inflation as a tax on cash. Item types: main idea 7, best summary 3,
inference 9, assumption 5, tone 1, specific detail 3. Difficulty 2 easy / 14 medium / 12 hard. Options are named by
content in every explanation."""
from csat_common import passage, RQ

CRUX = "Which one of the following statements best reflects the crux of the passage?"
CRUX_HI = "निम्नलिखित में से कौन-सा कथन परिच्छेद के सार को सबसे अच्छी तरह व्यक्त करता है?"
MSG = "Which one of the following statements best reflects the most logical and rational message conveyed by the passage?"
MSG_HI = "निम्नलिखित में से कौन-सा कथन परिच्छेद द्वारा दिए गए सबसे तार्किक और विवेकपूर्ण संदेश को सबसे अच्छी तरह व्यक्त करता है?"
VALID = "On the basis of the passage, which of the following conclusions is/are valid?"
VALID_HI = "परिच्छेद के आधार पर निम्नलिखित में से कौन-सा/से निष्कर्ष वैध है/हैं?"
ASSUME = "Which of the following assumptions has/have been made in the passage?"
ASSUME_HI = "परिच्छेद में निम्नलिखित में से कौन-सी पूर्वधारणा/एँ बनाई गई है/हैं?"

# ------------------------------------------------------------------ P01 comparative advantage (3)
p = passage("p01",
  "It is tempting to think that a country should import only what it cannot make for itself. Yet a country that could produce both cloth and machines more cheaply than its neighbour may still gain by buying cloth from it. "
  "What matters is not who is better at a thing in absolute terms but what each must give up to produce it. If making a tonne of cloth costs one country many of the machines it could otherwise have built, while its neighbour gives up far fewer machines for the same cloth, "
  "both are better off when each specialises in what it sacrifices least to make and trades for the rest. The argument is about the size of the shared pie, not its division: some workers and firms in the industries that shrink will lose, sometimes badly, "
  "and the gains to the country as a whole do not reach them unless policy carries some of those gains across. Nor does the argument say anything about which industries a country should try to build for the future.",
  "यह सोचना लुभावना है कि किसी देश को केवल वही आयात करना चाहिए जो वह स्वयं नहीं बना सकता। फिर भी जो देश अपने पड़ोसी से कपड़ा और मशीनें दोनों सस्ते में बना सकता है, वह भी उससे कपड़ा ख़रीदकर लाभ उठा सकता है। "
  "मायने यह नहीं रखता कि किसी चीज़ में निरपेक्ष रूप से कौन बेहतर है, बल्कि यह कि उसे बनाने के लिए हर एक को क्या छोड़ना पड़ता है। यदि एक टन कपड़ा बनाने में एक देश को वे कई मशीनें छोड़नी पड़ें जो वह अन्यथा बना सकता था, जबकि उसका पड़ोसी उतने ही कपड़े के लिए कहीं कम मशीनें छोड़ता है, "
  "तो दोनों तब बेहतर स्थिति में होते हैं जब हर एक उस चीज़ में विशेषज्ञता ले जिसे बनाने में उसका त्याग सबसे कम है, और बाक़ी का व्यापार करे। यह तर्क साझे लाभ के आकार के बारे में है, उसके बँटवारे के बारे में नहीं: सिकुड़ने वाले उद्योगों के कुछ श्रमिक और कंपनियाँ हारेंगे, कभी-कभी बुरी तरह, "
  "और पूरे देश के लाभ उन तक तब तक नहीं पहुँचते जब तक नीति उन लाभों का कुछ भाग उन तक न ले जाए। न ही यह तर्क इस बारे में कुछ कहता है कि किसी देश को भविष्य के लिए कौन-से उद्योग खड़े करने का प्रयास करना चाहिए।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage argues that what counts is the sacrifice each country makes, so trade can pay even in a good that a country makes more cheaply, and then limits the claim: the gains are to the whole and do not reach those in shrinking industries unless policy carries them. "
   "It rejects the idea of importing only what one cannot make; it says that some workers lose, so not every worker gains; and it says that the argument is silent on which industries to build for the future.",
   "परिच्छेद तर्क देता है कि मायने हर देश के त्याग का है, इसलिए उस वस्तु में भी व्यापार लाभदायक हो सकता है जिसे कोई देश सस्ते में बनाता है, और फिर दावे को सीमित करता है: लाभ समग्र के हैं और सिकुड़ते उद्योगों वालों तक तब तक नहीं पहुँचते जब तक नीति न पहुँचाए। "
   "वह केवल वही आयात करने का विचार अस्वीकार करता है जो देश नहीं बना सकता; वह कहता है कि कुछ श्रमिक हारते हैं, इसलिए हर श्रमिक को लाभ नहीं होता; और वह कहता है कि तर्क भविष्य के उद्योगों के बारे में मौन है।",
   "crux",
   opts=["A country should import only those goods that it cannot produce for itself at any cost.",
         "Trade can pay even in goods a country makes more cheaply, though not everyone shares the gain.",
         "Free trade makes every worker in every industry of a country better off than before it began.",
         "A country should decide by trade alone which industries it ought to build for its future growth."],
   opts_hi=["किसी देश को केवल वही वस्तुएँ आयात करनी चाहिए जिन्हें वह किसी भी लागत पर स्वयं नहीं बना सकता।",
            "सस्ते में बनाई जा सकने वाली वस्तुओं में भी व्यापार लाभदायक हो सकता है, पर लाभ सबको नहीं मिलता।",
            "मुक्त व्यापार किसी देश के हर उद्योग के हर श्रमिक को उसके शुरू होने से पहले की तुलना में बेहतर बनाता है।",
            "किसी देश को केवल व्यापार के आधार पर तय करना चाहिए कि भविष्य की वृद्धि के लिए उसे कौन-से उद्योग खड़े करने हैं।"],
   ans=1, pos=1)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Only 1 is valid. The passage's example is a country that could make cloth more cheaply than its neighbour yet gains by buying cloth from it, because what decides is the sacrifice of other goods, not the absolute cost. "
   "2 is contradicted: the gains 'do not reach them unless policy carries some of those gains across', so compensation is not automatic.",
   "केवल 1 वैध है। परिच्छेद का उदाहरण ऐसा देश है जो अपने पड़ोसी से सस्ते में कपड़ा बना सकता है, फिर भी उससे कपड़ा ख़रीदकर लाभ पाता है, क्योंकि निर्णायक दूसरी वस्तुओं का त्याग है, निरपेक्ष लागत नहीं। "
   "2 का खंडन होता है: लाभ 'उन तक तब तक नहीं पहुँचते जब तक नीति उन लाभों का कुछ भाग उन तक न ले जाए', इसलिए क्षतिपूर्ति अपने-आप नहीं होती।",
   "conclusions",
   st=["A country can gain by importing a good even if it could itself produce that good with fewer resources than the exporter.",
       "Workers who lose their jobs when an industry shrinks are compensated automatically by the gains from trade."],
   st_hi=["कोई देश किसी वस्तु के आयात से लाभ पा सकता है, भले ही वह उसे निर्यातक से कम संसाधनों में स्वयं बना सकता हो।",
          "किसी उद्योग के सिकुड़ने पर नौकरी खोने वाले श्रमिकों की क्षतिपूर्ति व्यापार के लाभों से अपने-आप हो जाती है।"],
   key=0)
RQ(p, "Assumption", "hard", "s2", ASSUME, ASSUME_HI,
   "Only 2 is assumed. Specialising 'in what it sacrifices least to make' means moving workers, land and capital out of one industry and into another; the gain the passage describes exists only if such resources can be shifted, at least in part. "
   "1 is not assumed: the argument turns on what each country gives up, not on which is richer, and it would hold whichever of the two were poorer.",
   "केवल 2 पूर्वधारणा है। 'उस चीज़ में विशेषज्ञता' लेना 'जिसे बनाने में उसका त्याग सबसे कम है' का अर्थ है श्रमिकों, भूमि और पूँजी को एक उद्योग से दूसरे में ले जाना; परिच्छेद जिस लाभ का वर्णन करता है वह तभी है जब ऐसे संसाधनों को कम से कम आंशिक रूप से स्थानांतरित किया जा सके। "
   "1 पूर्वधारणा नहीं है: तर्क इस पर टिका है कि हर देश क्या छोड़ता है, इस पर नहीं कि कौन अधिक धनी है, और वह दोनों में से कोई भी ग़रीब हो तब भी सत्य रहेगा।",
   "assumptions",
   st=["The neighbouring country is poorer than the country that buys cloth from it.",
       "Workers and capital can be moved, at least in part, from one industry to another."],
   st_hi=["पड़ोसी देश उस देश से ग़रीब है जो उससे कपड़ा ख़रीदता है।",
          "श्रमिकों और पूँजी को, कम से कम आंशिक रूप से, एक उद्योग से दूसरे में ले जाया जा सकता है।"],
   key=1)

# ------------------------------------------------------------------ P02 sunk costs (3)
p = passage("p02",
  "A family that has paid for a holiday it cannot cancel may go even when one of them is ill, because 'otherwise the money is wasted'. But the money is gone whether they go or not; the only question left is whether the trip, from now on, is worth more than staying at home. "
  "Economists call such spending a sunk cost and advise ignoring it. People find this hard, and not only out of foolishness: abandoning a project feels like admitting a mistake, and those who started it are often judged by whether it is finished. "
  "Governments are especially prone to pressing on with schemes whose remaining costs exceed their remaining benefits, because the decision to stop is made by people who will be blamed for what was already spent. "
  "The sensible rule is to look forward -- what will further spending buy? -- while learning, separately, from what went wrong. Looking back is useful for learning, not for deciding.",
  "जिस परिवार ने ऐसी छुट्टी का भुगतान किया है जिसे रद्द नहीं किया जा सकता, वह एक सदस्य के बीमार होने पर भी जा सकता है, क्योंकि 'वरना पैसा बेकार जाएगा'। पर पैसा तो जा चुका, वे जाएँ या न जाएँ; अब केवल यह प्रश्न बचता है कि आगे से यात्रा घर रहने से अधिक मूल्यवान है या नहीं। "
  "अर्थशास्त्री ऐसे ख़र्च को डूबी लागत कहते हैं और उसे अनदेखा करने की सलाह देते हैं। लोगों को यह कठिन लगता है, और केवल मूर्खता के कारण नहीं: किसी परियोजना को छोड़ना ग़लती मानने जैसा लगता है, और जिन्होंने उसे शुरू किया उन्हें प्रायः इसी पर आँका जाता है कि वह पूरी हुई या नहीं। "
  "सरकारें विशेष रूप से ऐसी योजनाओं को आगे बढ़ाती रहती हैं जिनकी शेष लागत उनके शेष लाभ से अधिक हो, क्योंकि रोकने का निर्णय उन्हीं लोगों को लेना होता है जिन्हें पहले हुए ख़र्च के लिए दोषी ठहराया जाएगा। "
  "समझदारी का नियम आगे देखना है -- आगे का ख़र्च क्या दिलाएगा? -- और साथ ही, अलग से, जो ग़लत हुआ उससे सीखना। पीछे देखना सीखने के लिए उपयोगी है, निर्णय लेने के लिए नहीं।")
RQ(p, "Best Summary", "medium", "mcq", MSG, MSG_HI,
   "The passage's rule is to decide by what further spending will buy, setting aside what is already spent, while learning separately from past mistakes. "
   "Treating money already spent as wasted unless the project is finished is the very error the passage describes; it does not say that governments should never stop a scheme -- it criticises them for pressing on; and it says that people find sunk costs hard to ignore 'not only out of foolishness'.",
   "परिच्छेद का नियम यह है कि निर्णय इस पर लिया जाए कि आगे का ख़र्च क्या दिलाएगा, पहले हुए ख़र्च को अलग रखकर, और पिछली ग़लतियों से अलग से सीखा जाए। "
   "पहले ख़र्च हुए पैसे को परियोजना पूरी न होने पर बेकार मानना ठीक वही भूल है जिसका परिच्छेद वर्णन करता है; वह यह नहीं कहता कि सरकारों को कोई योजना कभी नहीं रोकनी चाहिए -- वह उनकी आगे बढ़ते रहने के लिए आलोचना करता है; और वह कहता है कि लोगों को डूबी लागत अनदेखा करना 'केवल मूर्खता के कारण नहीं' कठिन लगता है।",
   "message",
   opts=["Money already spent on a project is wasted unless the project is carried through to the end.",
         "Governments should never abandon schemes once they have been started and money has been spent.",
         "Decisions should weigh only what lies ahead; past spending matters for learning, not deciding.",
         "People who press on with failing projects do so simply because they do not understand costs."],
   opts_hi=["किसी परियोजना पर पहले ख़र्च हुआ पैसा बेकार है जब तक परियोजना अंत तक न पहुँचाई जाए।",
            "सरकारों को शुरू हो चुकी और पैसा लग चुकी योजनाओं को कभी नहीं छोड़ना चाहिए।",
            "निर्णयों में केवल आगे की बात तौलनी चाहिए; पिछला ख़र्च सीखने के लिए है, निर्णय के लिए नहीं।",
            "विफल परियोजनाओं को आगे बढ़ाते रहने वाले लोग केवल इसलिए ऐसा करते हैं कि वे लागत को नहीं समझते।"],
   ans=2, pos=2)
RQ(p, "Inference", "hard", "mcq",
   "Which one of the following decisions does the reasoning of the passage support?",
   "परिच्छेद का तर्क निम्नलिखित में से किस निर्णय का समर्थन करता है?",
   "On the passage's rule, only future costs and benefits count. A half-built road should be stopped if the cost of finishing it is greater than the benefit the finished road would bring, however much has been spent. "
   "Finishing the road because much has been spent, and going on a trip while ill so that the money is not wasted, are the sunk-cost error itself; refusing to study a failure throws away the learning that the passage says looking back is for.",
   "परिच्छेद के नियम के अनुसार केवल भविष्य की लागत और लाभ गिने जाते हैं। आधी बनी सड़क को रोक देना चाहिए यदि उसे पूरा करने की लागत पूरी सड़क से होने वाले लाभ से अधिक हो, चाहे जितना ख़र्च हो चुका हो। "
   "बहुत ख़र्च हो चुकने के कारण सड़क पूरी करना, और पैसा बेकार न जाए इसलिए बीमार होते हुए यात्रा पर जाना, स्वयं डूबी लागत की भूल हैं; किसी विफलता का अध्ययन न करना उस सीख को फेंक देता है जिसके लिए परिच्छेद के अनुसार पीछे देखा जाता है।",
   "which-decision",
   opts=["Stopping a half-built road whose remaining cost exceeds the benefit it would bring once finished",
         "Finishing a half-built road because very large sums of money have already been spent on building it",
         "Refusing to study why a project failed, since the money spent on it is already gone",
         "Going on a trip that cannot be cancelled while ill, so that the money paid is not wasted"],
   opts_hi=["ऐसी आधी बनी सड़क को रोकना जिसकी शेष लागत पूरी होने पर उससे मिलने वाले लाभ से अधिक हो",
            "आधी बनी सड़क को इसलिए पूरा करना कि उस पर पहले ही बहुत बड़ी राशि ख़र्च हो चुकी है",
            "यह अध्ययन करने से मना करना कि परियोजना क्यों विफल हुई, क्योंकि उस पर लगा पैसा तो जा चुका",
            "बीमार होते हुए भी रद्द न हो सकने वाली यात्रा पर जाना, ताकि चुकाया गया पैसा बेकार न जाए"],
   ans=0, pos=3)
RQ(p, "Specific Detail", "easy", "mcq",
   "According to the passage, why do people find it hard to ignore sunk costs?",
   "परिच्छेद के अनुसार, लोगों को डूबी लागत को अनदेखा करना कठिन क्यों लगता है?",
   "The passage gives two reasons: abandoning a project feels like admitting a mistake, and those who started it are often judged by whether it is finished. "
   "It says nothing of a law that requires projects to be completed, it says that the money is gone 'whether they go or not', and economists advise ignoring past spending, not weighing it.",
   "परिच्छेद दो कारण देता है: परियोजना छोड़ना ग़लती मानने जैसा लगता है, और उसे शुरू करने वालों को प्रायः इसी पर आँका जाता है कि वह पूरी हुई या नहीं। "
   "वह किसी ऐसे क़ानून का उल्लेख नहीं करता जो परियोजनाएँ पूरी करना अनिवार्य करे, वह कहता है कि पैसा 'जाएँ या न जाएँ' जा चुका है, और अर्थशास्त्री पिछले ख़र्च को अनदेखा करने की सलाह देते हैं, तौलने की नहीं।",
   "why-hard",
   opts=["Stopping feels like admitting error, and starters are judged by whether projects finish.",
         "The law requires every public project, once begun, to be completed in full, whatever it costs.",
         "Money spent on a project can usually be recovered if the project is finished.",
         "Economists advise people to give great weight to the money spent in the past."],
   opts_hi=["रोकना ग़लती मानने जैसा लगता है, और शुरू करने वालों को काम पूरा होने से आँका जाता है।",
            "क़ानून के अनुसार शुरू हुई हर सार्वजनिक परियोजना को पूरी तरह पूरा करना अनिवार्य है।",
            "परियोजना पूरी हो जाए तो उस पर ख़र्च हुआ पैसा प्रायः वसूल हो जाता है।",
            "अर्थशास्त्री लोगों को अतीत में ख़र्च हुए पैसे को बहुत अधिक महत्व देने की सलाह देते हैं।"],
   ans=0, pos=0)

# ------------------------------------------------------------------ P03 placebo and nocebo (3)
p = passage("p03",
  "In many trials of new medicines, patients given a dummy pill report real relief: their pain eases, their sleep improves. This placebo effect is not simply imagination; expecting to feel better can change the body's own responses, at least for symptoms such as pain and nausea that the brain helps to regulate. "
  "It has an unwelcome twin. Patients warned at length about a drug's possible side effects report more of them, even when they have been given the dummy pill -- the nocebo effect. This puts doctors in a bind: they must tell patients about real risks, yet the way they do so can itself cause harm. "
  "The answer is not to hide risks but to frame them honestly -- to say how common a side effect really is, and that most people taking the drug do not experience it, rather than reading out a long list that suggests each one is likely. "
  "Nor do placebo effects make the dummy pill a cure: they ease how an illness is felt far more than they change its course.",
  "नई दवाओं के कई परीक्षणों में जिन मरीज़ों को नक़ली गोली दी जाती है, वे वास्तविक राहत बताते हैं: उनका दर्द घटता है, उनकी नींद सुधरती है। यह प्लेसीबो प्रभाव केवल कल्पना नहीं है; बेहतर महसूस करने की अपेक्षा शरीर की अपनी प्रतिक्रियाओं को बदल सकती है, कम से कम दर्द और मतली जैसे उन लक्षणों में जिनके नियमन में मस्तिष्क की भूमिका है। "
  "इसका एक अनचाहा जुड़वाँ है। जिन मरीज़ों को किसी दवा के संभावित दुष्प्रभावों के बारे में विस्तार से चेताया जाता है, वे उनमें से अधिक बताते हैं, तब भी जब उन्हें नक़ली गोली दी गई हो -- यह नोसीबो प्रभाव है। इससे डॉक्टर दुविधा में पड़ते हैं: उन्हें मरीज़ों को वास्तविक जोखिम बताने ही हैं, फिर भी बताने का ढंग स्वयं हानि पहुँचा सकता है। "
  "उत्तर जोखिम छिपाना नहीं, बल्कि उन्हें ईमानदारी से प्रस्तुत करना है -- यह बताना कि कोई दुष्प्रभाव वास्तव में कितना आम है, और कि दवा लेने वाले अधिकांश लोगों को वह नहीं होता, न कि ऐसी लंबी सूची पढ़ देना जो हर एक को संभावित दिखाए। "
  "न ही प्लेसीबो प्रभाव नक़ली गोली को इलाज बना देते हैं: वे इस बात को कहीं अधिक हल्का करते हैं कि बीमारी कैसी महसूस होती है, बजाय उसके क्रम को बदलने के।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage shows that expectations change what patients feel -- relief from a dummy pill, side effects from warnings -- and concludes that risks must be told honestly but in proportion, not hidden. "
   "It rejects hiding side effects; it says that placebo effects do not make the dummy pill a cure; and it says that the placebo effect 'is not simply imagination', so pain is not shown to be imaginary.",
   "परिच्छेद दिखाता है कि अपेक्षाएँ मरीज़ों के अनुभव को बदलती हैं -- नक़ली गोली से राहत, चेतावनियों से दुष्प्रभाव -- और निष्कर्ष निकालता है कि जोखिम छिपाए नहीं, बल्कि ईमानदारी से और उचित अनुपात में बताए जाने चाहिए। "
   "वह दुष्प्रभाव छिपाने को अस्वीकार करता है; वह कहता है कि प्लेसीबो प्रभाव नक़ली गोली को इलाज नहीं बनाते; और वह कहता है कि प्लेसीबो प्रभाव 'केवल कल्पना नहीं' है, इसलिए यह नहीं दिखता कि दर्द काल्पनिक है।",
   "crux",
   opts=["Doctors should stop telling patients about the side effects of the medicines they prescribe.",
         "Dummy pills can cure most illnesses, so long as the patients taking them believe in them.",
         "The placebo effect shows that most of the pain that patients report is in fact imaginary.",
         "Expectations shape what patients feel, so risks must be told honestly but in proportion."],
   opts_hi=["डॉक्टरों को मरीज़ों को अपनी लिखी दवाओं के दुष्प्रभावों के बारे में बताना बंद कर देना चाहिए।",
            "नक़ली गोलियाँ अधिकांश बीमारियाँ ठीक कर सकती हैं, बशर्ते उन्हें लेने वाले मरीज़ उन पर विश्वास करें।",
            "प्लेसीबो प्रभाव दिखाता है कि मरीज़ों द्वारा बताया गया अधिकांश दर्द वास्तव में काल्पनिक है।",
            "अपेक्षाएँ मरीज़ों के अनुभव को आकार देती हैं, इसलिए जोखिम ईमानदारी से पर उचित अनुपात में बताए जाएँ।"],
   ans=3, pos=3)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Only 2 is valid: patients warned at length about side effects report more of them even on a dummy pill, so what they report depends partly on what they were told. "
   "1 is contradicted: the passage begins with patients on dummy pills who report real relief.",
   "केवल 2 वैध है: जिन मरीज़ों को दुष्प्रभावों के बारे में विस्तार से चेताया जाता है वे नक़ली गोली पर भी उनमें से अधिक बताते हैं, इसलिए वे जो बताते हैं वह आंशिक रूप से इस पर निर्भर है कि उन्हें क्या बताया गया था। "
   "1 का खंडन होता है: परिच्छेद नक़ली गोली लेने वाले उन मरीज़ों से शुरू होता है जो वास्तविक राहत बताते हैं।",
   "conclusions",
   st=["In trials, patients given dummy pills report no change at all in their symptoms.",
       "The side effects patients report can depend partly on what they were told beforehand."],
   st_hi=["परीक्षणों में नक़ली गोलियाँ पाने वाले मरीज़ अपने लक्षणों में कोई भी बदलाव नहीं बताते।",
          "मरीज़ जो दुष्प्रभाव बताते हैं वे आंशिक रूप से इस पर निर्भर हो सकते हैं कि उन्हें पहले क्या बताया गया था।"],
   key=1)
RQ(p, "Assumption", "hard", "s2", ASSUME, ASSUME_HI,
   "Only 1 is assumed. The remedy the passage proposes -- telling patients how common a side effect really is and that most people do not get it -- can reduce the nocebo effect only if patients take in such information about frequency. "
   "2 is not assumed: the passage says that warnings increase reported side effects, not that most of the side effects reported in trials are nocebo effects.",
   "केवल 1 पूर्वधारणा है। परिच्छेद का उपाय -- मरीज़ों को बताना कि कोई दुष्प्रभाव वास्तव में कितना आम है और अधिकांश लोगों को वह नहीं होता -- नोसीबो प्रभाव को तभी घटा सकता है जब मरीज़ आवृत्ति की ऐसी जानकारी समझ सकें। "
   "2 पूर्वधारणा नहीं है: परिच्छेद कहता है कि चेतावनियाँ बताए गए दुष्प्रभाव बढ़ाती हैं, यह नहीं कि परीक्षणों में बताए गए अधिकांश दुष्प्रभाव नोसीबो प्रभाव हैं।",
   "assumptions",
   st=["Patients can understand and take reassurance from information about how common a side effect is.",
       "Most of the side effects reported in drug trials are caused by the nocebo effect."],
   st_hi=["मरीज़ यह जानकारी समझ सकते हैं, और उससे आश्वस्त हो सकते हैं, कि कोई दुष्प्रभाव कितना आम है।",
          "दवा परीक्षणों में बताए गए अधिकांश दुष्प्रभाव नोसीबो प्रभाव के कारण होते हैं।"],
   key=0)

# ------------------------------------------------------------------ P04 coral bleaching (2)
p = passage("p04",
  "Corals owe their colour, and most of their food, to tiny algae that live inside their tissues. When the water stays unusually warm for weeks, the partnership breaks down: the coral expels the algae and turns white. A bleached coral is not yet dead. "
  "If temperatures fall soon enough, the algae can return and the coral recover; if the heat lasts, the coral starves. Reefs have survived bleaching before, but recovery takes years, and as warm spells become more frequent, "
  "the gaps between them may grow too short for reefs to recover fully. Local care -- curbing pollution and overfishing -- can help a reef bounce back, but it cannot by itself prevent bleaching driven by warming seas.",
  "मूँगे अपना रंग, और अपना अधिकांश भोजन, उन सूक्ष्म शैवालों से पाते हैं जो उनके ऊतकों के भीतर रहते हैं। जब पानी हफ़्तों तक असामान्य रूप से गर्म रहता है, तो यह साझेदारी टूट जाती है: मूँगा शैवालों को बाहर निकाल देता है और सफ़ेद पड़ जाता है। विरंजित मूँगा अभी मरा नहीं होता। "
  "यदि तापमान जल्दी गिर जाए, तो शैवाल लौट सकते हैं और मूँगा ठीक हो सकता है; यदि गर्मी बनी रहे, तो मूँगा भूखा मर जाता है। भित्तियाँ पहले भी विरंजन झेल चुकी हैं, पर ठीक होने में वर्षों लगते हैं, और जैसे-जैसे गर्म दौर अधिक बार आते हैं, "
  "उनके बीच के अंतराल भित्तियों के पूरी तरह ठीक होने के लिए बहुत छोटे पड़ सकते हैं। स्थानीय देखभाल -- प्रदूषण और अति-मत्स्यन पर रोक -- किसी भित्ति को फिर से उभरने में सहायता कर सकती है, पर वह अकेले गर्म होते समुद्रों से होने वाले विरंजन को रोक नहीं सकती।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage says that a bleached coral can recover if the heat passes soon, and that the danger lies in warm spells coming so often that reefs lack time to recover. "
   "It says outright that a bleached coral 'is not yet dead'; local care helps a reef recover but 'cannot by itself prevent' bleaching; and corals get most of their food from the algae inside them, not by filtering the water.",
   "परिच्छेद कहता है कि गर्मी जल्दी बीत जाए तो विरंजित मूँगा ठीक हो सकता है, और ख़तरा इसमें है कि गर्म दौर इतनी बार आएँ कि भित्तियों को ठीक होने का समय न मिले। "
   "वह स्पष्ट कहता है कि विरंजित मूँगा 'अभी मरा नहीं होता'; स्थानीय देखभाल भित्ति को ठीक होने में सहायता करती है पर विरंजन को 'अकेले रोक नहीं सकती'; और मूँगे अपना अधिकांश भोजन अपने भीतर के शैवालों से पाते हैं, पानी छानकर नहीं।",
   "crux",
   opts=["A bleached coral is already dead, and a reef that has bleached cannot recover from it.",
         "Curbing pollution and overfishing can on its own prevent corals from bleaching in warm seas.",
         "Bleaching need not kill a reef, but frequent heat may leave too little time to recover.",
         "Corals obtain most of their food by filtering small particles out of the surrounding water."],
   opts_hi=["विरंजित मूँगा पहले ही मर चुका होता है, और विरंजित हुई भित्ति उससे ठीक नहीं हो सकती।",
            "प्रदूषण और अति-मत्स्यन पर रोक अकेले ही गर्म समुद्रों में मूँगों का विरंजन रोक सकती है।",
            "विरंजन से भित्ति का मरना ज़रूरी नहीं, पर बार-बार की गर्मी उबरने का समय घटा सकती है।",
            "मूँगे अपना अधिकांश भोजन आसपास के समुद्री पानी से छोटे-छोटे कण छानकर प्राप्त करते हैं।"],
   ans=2, pos=2)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Both are valid. 1: recovery takes years, so two warm spells close together can strike a reef before it has recovered from the first, while the same two years apart leave time to recover. "
   "2: local care 'can help a reef bounce back' even though it cannot prevent bleaching, so it is of some use.",
   "दोनों वैध हैं। 1: ठीक होने में वर्षों लगते हैं, इसलिए एक-दूसरे के निकट के दो गर्म दौर भित्ति पर पहले से ठीक होने से पहले ही चोट कर सकते हैं, जबकि वही दो दौर वर्षों के अंतर पर ठीक होने का समय छोड़ते हैं। "
   "2: स्थानीय देखभाल 'भित्ति को फिर से उभरने में सहायता कर सकती है', भले ही वह विरंजन रोक न सके, इसलिए उसका कुछ उपयोग है।",
   "conclusions",
   st=["Two warm spells in quick succession may harm a reef more than the same two spells years apart.",
       "Measures against local pollution are of some use even though they cannot stop bleaching."],
   st_hi=["एक के बाद एक जल्दी आने वाले दो गर्म दौर किसी भित्ति को उससे अधिक हानि पहुँचा सकते हैं जितनी वर्षों के अंतर पर आने वाले वही दो दौर।",
          "स्थानीय प्रदूषण के विरुद्ध उपाय कुछ उपयोगी हैं, भले ही वे विरंजन रोक न सकें।"],
   key=2)

# ------------------------------------------------------------------ P05 the case for free speech (3)
p = passage("p05",
  "The case for free speech is often put as a marketplace: let every idea compete, and the true ones will win. The image is attractive but too hopeful. Markets reward what sells, and a false claim that flatters or frightens can travel faster than a careful correction. "
  "A better defence does not depend on truth winning quickly. It rests on two points: no authority can be trusted to decide in advance which opinions are false, and a person who has never heard the case against his views holds them as a prejudice rather than as a reasoned belief. "
  "On this view, protecting unpopular speech is not a bet that it will persuade anyone; it is a safeguard against the errors of those who would silence it. The defence has limits that even its strongest supporters accept, such as incitement to immediate violence -- "
  "but those limits are narrow, and the burden lies on those who would widen them.",
  "अभिव्यक्ति की स्वतंत्रता का पक्ष प्रायः एक बाज़ार के रूप में रखा जाता है: हर विचार को होड़ करने दो, और सच्चे विचार जीतेंगे। यह छवि आकर्षक है पर अत्यधिक आशावादी। बाज़ार उसे पुरस्कृत करता है जो बिकता है, और चापलूसी करने वाला या डराने वाला कोई झूठा दावा सावधानी से किए गए सुधार से तेज़ फैल सकता है। "
  "एक बेहतर बचाव सत्य के जल्दी जीतने पर निर्भर नहीं करता। वह दो बातों पर टिका है: किसी भी सत्ता पर भरोसा नहीं किया जा सकता कि वह पहले से तय करे कि कौन-सी राय झूठी है, और जिस व्यक्ति ने अपने विचारों के विरुद्ध पक्ष कभी नहीं सुना, वह उन्हें तर्कपूर्ण विश्वास नहीं, पूर्वाग्रह के रूप में रखता है। "
  "इस दृष्टि से अलोकप्रिय अभिव्यक्ति की रक्षा यह दाँव नहीं कि वह किसी को मना लेगी; यह उन लोगों की भूलों से बचाव है जो उसे चुप कराना चाहेंगे। इस बचाव की कुछ सीमाएँ हैं जिन्हें इसके सबसे प्रबल समर्थक भी मानते हैं, जैसे तत्काल हिंसा के लिए उकसाना -- "
  "पर वे सीमाएँ संकीर्ण हैं, और उन्हें चौड़ा करना चाहने वालों पर ही औचित्य सिद्ध करने का भार है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage sets aside the hope that truth wins in an open market and rests the case on distrust of any authority that would decide in advance which views are false, together with the value of hearing the other side. "
   "It calls the idea that true ideas always win 'too hopeful'; it accepts limits such as incitement to immediate violence; and it uses the speed of false claims to reject the market image, not to call for wider regulation, whose burden it puts on those who would widen the limits.",
   "परिच्छेद इस आशा को किनारे करता है कि खुले बाज़ार में सत्य जीतता है, और पक्ष को किसी भी ऐसी सत्ता के प्रति अविश्वास पर टिकाता है जो पहले से तय करे कि कौन-से विचार झूठे हैं, साथ ही दूसरा पक्ष सुनने के मूल्य पर। "
   "वह इस विचार को कि सच्चे विचार हमेशा जीतते हैं 'अत्यधिक आशावादी' कहता है; वह तत्काल हिंसा के लिए उकसाने जैसी सीमाएँ स्वीकार करता है; और वह झूठे दावों की गति का प्रयोग बाज़ार की छवि को अस्वीकार करने के लिए करता है, व्यापक नियमन माँगने के लिए नहीं, जिसका भार वह सीमाएँ चौड़ी करना चाहने वालों पर रखता है।",
   "crux",
   opts=["Free speech should be protected because true ideas always defeat false ones in open debate.",
         "All speech must be protected without exception, including incitement to immediate violence.",
         "Since false claims spread faster than corrections, speech ought to be regulated far more widely.",
         "Free speech rests less on truth winning than on distrust of any power that would judge views."],
   opts_hi=["अभिव्यक्ति की स्वतंत्रता की रक्षा होनी चाहिए क्योंकि खुली बहस में सच्चे विचार हमेशा झूठे विचारों को हराते हैं।",
            "हर अभिव्यक्ति की रक्षा बिना किसी अपवाद के होनी चाहिए, तत्काल हिंसा के लिए उकसाने सहित।",
            "चूँकि झूठे दावे सुधारों से तेज़ फैलते हैं, अभिव्यक्ति का कहीं अधिक व्यापक नियमन होना चाहिए।",
            "अभिव्यक्ति की स्वतंत्रता सत्य के जीतने पर कम, विचारों को परखने वाली सत्ता पर अविश्वास पर अधिक टिकी है।"],
   ans=3, pos=3)
RQ(p, "Author's Tone", "medium", "mcq",
   "The author's attitude towards the 'marketplace' picture of free speech is best described as one of:",
   "अभिव्यक्ति की स्वतंत्रता की 'बाज़ार' वाली छवि के प्रति लेखक के दृष्टिकोण का सबसे अच्छा वर्णन है:",
   "The author calls the image 'attractive but too hopeful', explains why it fails, and replaces it with a better defence of the same freedom. That is sympathy for its aim joined to scepticism about its optimism. "
   "The author does not reject free speech itself, does not accept the image without reservation, and is plainly not indifferent.",
   "लेखक छवि को 'आकर्षक पर अत्यधिक आशावादी' कहता है, बताता है कि वह क्यों विफल होती है, और उसकी जगह उसी स्वतंत्रता का बेहतर बचाव रखता है। यह उसके उद्देश्य के प्रति सहानुभूति के साथ उसकी आशावादिता पर संदेह है। "
   "लेखक न स्वयं अभिव्यक्ति की स्वतंत्रता को अस्वीकार करता है, न छवि को बिना किसी आपत्ति के स्वीकार करता है, और स्पष्ट रूप से उदासीन भी नहीं है।",
   "tone",
   opts=["rejection of free speech itself as harmful",
         "sympathetic scepticism",
         "acceptance of it without any reservation",
         "complete indifference to the question"],
   opts_hi=["स्वयं अभिव्यक्ति की स्वतंत्रता को हानिकारक मानकर अस्वीकार करने का",
            "सहानुभूतिपूर्ण संदेह का",
            "उसे बिना किसी आपत्ति के स्वीकार करने का",
            "इस प्रश्न के प्रति पूर्ण उदासीनता का"],
   ans=1, pos=1)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Both are valid. 1: the defence does not depend on truth winning, and protecting unpopular speech is 'not a bet that it will persuade'; since no authority can be trusted to decide in advance which opinions are false, an opinion may be protected whether or not it is true. "
   "2: the passage says that the limits are narrow 'and the burden lies on those who would widen them' -- those who want to restrict more speech must make the case.",
   "दोनों वैध हैं। 1: बचाव सत्य के जीतने पर निर्भर नहीं, और अलोकप्रिय अभिव्यक्ति की रक्षा 'यह दाँव नहीं कि वह मना लेगी'; चूँकि किसी सत्ता पर भरोसा नहीं किया जा सकता कि वह पहले से तय करे कि कौन-सी राय झूठी है, किसी राय की रक्षा हो सकती है चाहे वह सत्य हो या नहीं। "
   "2: परिच्छेद कहता है कि सीमाएँ संकीर्ण हैं 'और उन्हें चौड़ा करना चाहने वालों पर ही औचित्य सिद्ध करने का भार है' -- जो और अधिक अभिव्यक्ति पर रोक चाहते हैं उन्हें अपना पक्ष सिद्ध करना होगा।",
   "conclusions",
   st=["On the passage's view, an opinion may deserve protection even if it is false.",
       "Those who wish to place further limits on speech must justify doing so."],
   st_hi=["परिच्छेद की दृष्टि में किसी राय की रक्षा उचित हो सकती है, भले ही वह झूठी हो।",
          "जो अभिव्यक्ति पर और सीमाएँ लगाना चाहते हैं, उन्हें ऐसा करने का औचित्य सिद्ध करना होगा।"],
   key=2)

# ------------------------------------------------------------------ P06 the journey of place-value numerals (3)
p = passage("p06",
  "The way we write numbers -- ten digits, including a sign for zero, whose value depends on their place -- took shape in India by the middle of the first millennium CE. Its power lay less in any single digit than in the system: with place value and a zero to mark an empty place, "
  "any number could be written with the same ten symbols, and sums could be worked on paper by simple rules. Scholars writing in Arabic learned the system and explained it in the ninth century, and from their works it reached Europe, where for a long time it was known as 'Arabic numerals'. "
  "It spread slowly. Merchants and clerks used to the counting board and to Roman numerals were in no hurry to change, and at least one city for a time barred the new numerals from official accounts, fearing that they were easier to alter. "
  "What finally carried the day was usefulness: the new method put calculation within reach of anyone who could hold a pen.",
  "संख्याएँ लिखने का हमारा तरीक़ा -- दस अंक, शून्य के एक चिह्न सहित, जिनका मान उनके स्थान पर निर्भर करता है -- प्रथम सहस्राब्दी ईस्वी के मध्य तक भारत में आकार ले चुका था। इसकी शक्ति किसी एक अंक में कम और पूरी प्रणाली में अधिक थी: स्थानीय मान और ख़ाली स्थान दर्शाने वाले शून्य के साथ, "
  "कोई भी संख्या उन्हीं दस चिह्नों से लिखी जा सकती थी, और सरल नियमों से काग़ज़ पर हिसाब लगाया जा सकता था। अरबी में लिखने वाले विद्वानों ने यह प्रणाली सीखी और नौवीं शताब्दी में उसकी व्याख्या की, और उनकी कृतियों से वह यूरोप पहुँची, जहाँ लंबे समय तक उसे 'अरबी अंक' कहा जाता रहा। "
  "वह धीरे-धीरे फैली। गिनती-पट्ट और रोमन अंकों के अभ्यस्त व्यापारी और लिपिक बदलने की जल्दी में नहीं थे, और कम से कम एक नगर ने कुछ समय के लिए नए अंकों को आधिकारिक हिसाब-किताब से वर्जित कर दिया, इस डर से कि उनमें छेड़छाड़ करना आसान है। "
  "अंततः उपयोगिता की जीत हुई: नई विधि ने हिसाब लगाने को हर उस व्यक्ति की पहुँच में ला दिया जो क़लम पकड़ सकता था।")
RQ(p, "Best Summary", "medium", "mcq", MSG, MSG_HI,
   "The passage traces the place-value system with zero from India, through scholars writing in Arabic, to Europe, and explains that it won slowly, through usefulness. "
   "It says the system took shape in India and only later came to be called 'Arabic' in Europe; it says that Europe was slow to adopt it and that one city barred it as easier to alter, not harder to forge; and it places the system's worth in the whole method, not in the shapes of the digits.",
   "परिच्छेद शून्य वाली स्थानीय मान प्रणाली की यात्रा भारत से, अरबी में लिखने वाले विद्वानों के माध्यम से, यूरोप तक दिखाता है, और बताता है कि वह धीरे-धीरे, अपनी उपयोगिता से जीती। "
   "वह कहता है कि प्रणाली भारत में बनी और बाद में यूरोप में 'अरबी' कहलाई; वह कहता है कि यूरोप ने उसे अपनाने में देर की और एक नगर ने उसे छेड़छाड़ में आसान मानकर वर्जित किया, न कि जालसाज़ी में कठिन मानकर; और वह प्रणाली का मूल्य पूरी विधि में रखता है, अंकों की आकृतियों में नहीं।",
   "message",
   opts=["Today's numerals were invented in Arabia and were later taken up by mathematicians in India.",
         "Europe adopted the new numerals at once, because they were so much harder to forge than the old ones.",
         "The worth of the Indian numerals lay chiefly in the elegant shapes of the individual digits.",
         "Place value with zero spread from India via Arabic scholars to Europe, winning slowly by usefulness."],
   opts_hi=["आज के अंक अरब में आविष्कृत हुए और बाद में भारत के गणितज्ञों ने उन्हें अपनाया।",
            "यूरोप ने नए अंक तुरंत अपना लिए, क्योंकि उनमें पुराने अंकों की तुलना में जालसाज़ी करना कहीं कठिन था।",
            "भारतीय अंकों का मूल्य मुख्यतः अलग-अलग अंकों की सुंदर आकृतियों में था।",
            "शून्य सहित स्थानीय मान भारत से अरबी विद्वानों द्वारा यूरोप पहुँचा और उपयोगिता से धीरे-धीरे जीता।"],
   ans=3, pos=3)
RQ(p, "Specific Detail", "easy", "mcq",
   "According to the passage, why did a city for a time bar the new numerals from official accounts?",
   "परिच्छेद के अनुसार, एक नगर ने कुछ समय के लिए नए अंकों को आधिकारिक हिसाब-किताब से वर्जित क्यों किया?",
   "The passage says that the city feared that the new numerals were easier to alter. It says nothing about their being unable to express large numbers, being harder to read, or having been brought in by foreign traders.",
   "परिच्छेद कहता है कि नगर को डर था कि नए अंकों में छेड़छाड़ करना आसान है। वह इस बारे में कुछ नहीं कहता कि वे बड़ी संख्याएँ व्यक्त नहीं कर सकते थे, पढ़ने में कठिन थे, या विदेशी व्यापारियों द्वारा लाए गए थे।",
   "why-barred",
   opts=["It was feared that entries in them were easier to alter.",
         "They could not be used to write numbers above a thousand.",
         "Merchants found them harder to read than Roman numerals.",
         "They had been brought into the city by foreign traders."],
   opts_hi=["डर था कि उनमें लिखी प्रविष्टियाँ बदलना आसान है।",
            "उनसे एक हज़ार से बड़ी संख्याएँ नहीं लिखी जा सकती थीं।",
            "व्यापारियों को वे रोमन अंकों से पढ़ने में कठिन लगते थे।",
            "उन्हें विदेशी व्यापारी नगर में लेकर आए थे।"],
   ans=0, pos=0)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Both are valid. 1: the passage credits the zero with marking an empty place; without such a sign, 25 and 205 would both be written with a 2 followed by a 5. "
   "2: the system spread slowly, and merchants and clerks used to the counting board and to Roman numerals 'were in no hurry to change', so the older methods stayed in use alongside the new for a time.",
   "दोनों वैध हैं। 1: परिच्छेद शून्य को ख़ाली स्थान दर्शाने का श्रेय देता है; ऐसे चिह्न के बिना 25 और 205 दोनों 2 के बाद 5 लिखकर ही व्यक्त होते। "
   "2: प्रणाली धीरे-धीरे फैली, और गिनती-पट्ट तथा रोमन अंकों के अभ्यस्त व्यापारी और लिपिक 'बदलने की जल्दी में नहीं थे', इसलिए पुरानी विधियाँ कुछ समय तक नई के साथ-साथ चलती रहीं।",
   "conclusions",
   st=["Without a sign for an empty place, a place-value system could not tell 25 from 205 in writing.",
       "For a time the new numerals were used alongside older ways of counting and recording."],
   st_hi=["ख़ाली स्थान के चिह्न के बिना स्थानीय मान प्रणाली लिखित रूप में 25 और 205 में अंतर नहीं कर सकती।",
          "कुछ समय तक नए अंक गिनने और दर्ज करने के पुराने तरीक़ों के साथ-साथ प्रयोग होते रहे।"],
   key=2)

# ------------------------------------------------------------------ P07 elected village councils and the few who capture them (3)
p = passage("p07",
  "Handing power and money to elected village councils is meant to bring decisions closer to the people they affect. Local officials know local needs, and villagers can see -- and question -- how money is spent. But closeness cuts both ways. "
  "In a village where land, credit and status are held by a few families, those families may also hold the council, and the funds meant for everyone can be steered towards their own fields and lanes. "
  "Reserving council seats for women and for disadvantaged groups has changed who sits at the table in many places, and studies have found that such councils often spend more on what their members' communities need, such as drinking water. "
  "Yet a seat is not the same as a voice: where a reserved member is a front for a powerful relative, little changes. Decentralisation works best where village assemblies meet regularly and accounts are read out in public, so that the many can watch the few.",
  "निर्वाचित ग्राम परिषदों को शक्ति और धन सौंपने का उद्देश्य निर्णयों को उन लोगों के निकट लाना है जिन पर उनका असर पड़ता है। स्थानीय अधिकारी स्थानीय आवश्यकताएँ जानते हैं, और ग्रामीण देख सकते हैं -- और प्रश्न कर सकते हैं -- कि पैसा कैसे ख़र्च होता है। पर निकटता दोनों ओर काटती है। "
  "जिस गाँव में भूमि, ऋण और प्रतिष्ठा कुछ परिवारों के हाथ में हो, वहाँ परिषद भी उन्हीं परिवारों के हाथ में हो सकती है, और सबके लिए बने धन को उनके अपने खेतों और गलियों की ओर मोड़ा जा सकता है। "
  "परिषद की सीटें महिलाओं और वंचित समूहों के लिए आरक्षित करने से कई स्थानों पर यह बदला है कि मेज़ पर कौन बैठता है, और अध्ययनों ने पाया है कि ऐसी परिषदें प्रायः उन चीज़ों पर अधिक ख़र्च करती हैं जिनकी उनके सदस्यों के समुदायों को आवश्यकता है, जैसे पीने का पानी। "
  "फिर भी सीट और आवाज़ एक नहीं हैं: जहाँ आरक्षित सदस्य किसी प्रभावशाली रिश्तेदार का मुखौटा हो, वहाँ थोड़ा ही बदलता है। विकेंद्रीकरण वहाँ सबसे अच्छा चलता है जहाँ ग्राम सभाएँ नियमित रूप से मिलती हैं और हिसाब सार्वजनिक रूप से पढ़कर सुनाया जाता है, ताकि बहुत-से लोग कुछ लोगों पर नज़र रख सकें।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage grants that elected councils bring decisions closer to people, warns that a few families can capture them, and concludes that decentralisation works best with regular assemblies and public accounts. "
   "It does not call for abolishing councils; it says that a reserved seat is 'not the same as a voice'; and it values local knowledge, so it does not prefer distant officials.",
   "परिच्छेद मानता है कि निर्वाचित परिषदें निर्णयों को लोगों के निकट लाती हैं, चेताता है कि कुछ परिवार उन पर क़ब्ज़ा कर सकते हैं, और निष्कर्ष निकालता है कि नियमित सभाओं और सार्वजनिक हिसाब के साथ विकेंद्रीकरण सबसे अच्छा चलता है। "
   "वह परिषदें समाप्त करने को नहीं कहता; वह कहता है कि आरक्षित सीट 'आवाज़ के समान नहीं' है; और वह स्थानीय जानकारी को महत्व देता है, इसलिए दूर के अधिकारियों को पसंद नहीं करता।",
   "crux",
   opts=["Village councils should be abolished, because a few powerful families control most of them.",
         "Reserving seats for women always gives them a real voice in the decisions of the council.",
         "Village funds are better handled by distant officials who are free of local pressures.",
         "Elected councils bring decisions closer to people but need open scrutiny to resist capture."],
   opts_hi=["ग्राम परिषदें समाप्त कर देनी चाहिए, क्योंकि उनमें से अधिकांश पर कुछ प्रभावशाली परिवारों का नियंत्रण है।",
            "महिलाओं के लिए सीटें आरक्षित करने से उन्हें परिषद के निर्णयों में हमेशा वास्तविक आवाज़ मिलती है।",
            "ग्राम निधि को स्थानीय दबावों से मुक्त दूर के अधिकारी बेहतर ढंग से सँभालते हैं।",
            "निर्वाचित परिषदें निर्णय लोगों के निकट लाती हैं, पर क़ब्ज़े से बचने के लिए उन्हें खुली निगरानी चाहिए।"],
   ans=3, pos=3)
RQ(p, "Inference", "hard", "mcq",
   "On the basis of the passage, which one of the following would do most to reduce the capture of a village council by a few families?",
   "परिच्छेद के आधार पर, निम्नलिखित में से कौन-सा कुछ परिवारों द्वारा ग्राम परिषद पर क़ब्ज़े को घटाने में सबसे अधिक सहायक होगा?",
   "The passage says that decentralisation works best where village assemblies meet regularly and accounts are read out in public, 'so that the many can watch the few'. "
   "Larger grants give a captured council more to steer; longer terms make its members harder to remove; and fewer meetings reduce the very scrutiny that the passage relies on.",
   "परिच्छेद कहता है कि विकेंद्रीकरण वहाँ सबसे अच्छा चलता है जहाँ ग्राम सभाएँ नियमित रूप से मिलें और हिसाब सार्वजनिक रूप से पढ़ा जाए, 'ताकि बहुत-से लोग कुछ लोगों पर नज़र रख सकें'। "
   "बड़े अनुदान क़ब्ज़े वाली परिषद को मोड़ने के लिए अधिक धन देते हैं; लंबे कार्यकाल उसके सदस्यों को हटाना कठिन बनाते हैं; और कम बैठकें उसी निगरानी को घटाती हैं जिस पर परिच्छेद टिका है।",
   "what-reduces-capture",
   opts=["Larger grants given to the council each year for roads, drains and other local works",
         "Regular village assemblies at which the council's accounts are read out",
         "Longer terms of office for the members of the council",
         "Fewer council meetings, so that decisions can be taken faster"],
   opts_hi=["सड़कों, नालियों और अन्य स्थानीय कार्यों के लिए परिषद को हर वर्ष दिए जाने वाले बड़े अनुदान",
            "नियमित ग्राम सभाएँ जिनमें परिषद का हिसाब पढ़कर सुनाया जाए",
            "परिषद के सदस्यों के लिए लंबा कार्यकाल",
            "परिषद की कम बैठकें, ताकि निर्णय तेज़ी से लिए जा सकें"],
   ans=1, pos=1)
RQ(p, "Assumption", "medium", "s2", ASSUME, ASSUME_HI,
   "Only 2 is assumed. The remedy of public assemblies and accounts read aloud works only if villagers who learn that funds are being misused can bring some pressure to bear; otherwise watching would change nothing. "
   "1 is not assumed: the passage compares councils with and without public scrutiny, not elected officials with appointed ones, and it makes no claim about which are more honest.",
   "केवल 2 पूर्वधारणा है। सार्वजनिक सभाओं और ज़ोर से पढ़े जाने वाले हिसाब का उपाय तभी काम करता है जब धन के दुरुपयोग का पता चलने पर ग्रामीण कुछ दबाव डाल सकें; अन्यथा नज़र रखने से कुछ नहीं बदलेगा। "
   "1 पूर्वधारणा नहीं है: परिच्छेद सार्वजनिक निगरानी वाली और बिना निगरानी वाली परिषदों की तुलना करता है, निर्वाचित और नियुक्त अधिकारियों की नहीं, और यह कोई दावा नहीं करता कि कौन अधिक ईमानदार है।",
   "assumptions",
   st=["Elected officials are, on the whole, more honest than officials who are appointed.",
       "Villagers who learn that funds are being misused can bring some pressure to bear on the council."],
   st_hi=["निर्वाचित अधिकारी कुल मिलाकर नियुक्त अधिकारियों से अधिक ईमानदार होते हैं।",
          "जिन ग्रामीणों को धन के दुरुपयोग का पता चलता है, वे परिषद पर कुछ दबाव डाल सकते हैं।"],
   key=1)

# ------------------------------------------------------------------ P08 automation bias (2)
p = passage("p08",
  "When a navigation app tells a driver to turn into a flooded road, some drivers turn. Pilots and doctors show a similar tendency, called automation bias: once a machine is usually right, people stop checking it, and they miss the rare occasions when it is wrong. "
  "The cause is not laziness so much as the way attention works; watching for an error that almost never comes is tiring, and the mind drifts. The remedy is not to distrust machines in general -- they are often more reliable than people -- "
  "but to design work so that people stay engaged: asking them to make their own judgement before they see the machine's, or showing how confident the machine is in each answer.",
  "जब कोई नेविगेशन ऐप चालक को पानी भरी सड़क में मुड़ने को कहता है, तो कुछ चालक मुड़ जाते हैं। पायलट और डॉक्टर भी ऐसी ही प्रवृत्ति दिखाते हैं, जिसे स्वचालन-पूर्वाग्रह कहते हैं: जब कोई मशीन प्रायः सही होती है, तो लोग उसे जाँचना बंद कर देते हैं, और उन दुर्लभ अवसरों को चूक जाते हैं जब वह ग़लत होती है। "
  "कारण आलस्य उतना नहीं जितना ध्यान के काम करने का ढंग है; ऐसी त्रुटि की प्रतीक्षा करना जो लगभग कभी नहीं आती, थका देता है, और मन भटक जाता है। उपाय मशीनों पर सामान्य रूप से अविश्वास करना नहीं है -- वे प्रायः लोगों से अधिक विश्वसनीय होती हैं -- "
  "बल्कि काम को ऐसे रचना है कि लोग जुड़े रहें: उनसे मशीन का निर्णय देखने से पहले अपना निर्णय लेने को कहना, या यह दिखाना कि मशीन अपने हर उत्तर के बारे में कितनी आश्वस्त है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage describes how people stop checking machines that are usually right, traces this to the way attention works, and proposes designing work so that people stay engaged. "
   "It says that machines are often more reliable than people, so it does not call for distrusting them; it says that the cause is 'not laziness so much as' attention; and the flooded road is an example, not a case against navigation apps.",
   "परिच्छेद बताता है कि लोग प्रायः सही रहने वाली मशीनों को जाँचना बंद कर देते हैं, इसे ध्यान के काम करने के ढंग से जोड़ता है, और काम को ऐसे रचने का प्रस्ताव करता है कि लोग जुड़े रहें। "
   "वह कहता है कि मशीनें प्रायः लोगों से अधिक विश्वसनीय हैं, इसलिए उन पर अविश्वास करने को नहीं कहता; वह कहता है कि कारण 'आलस्य उतना नहीं' जितना ध्यान है; और पानी भरी सड़क एक उदाहरण है, नेविगेशन ऐप के विरुद्ध कोई तर्क नहीं।",
   "crux",
   opts=["Machines are less reliable than people and should not be trusted with important decisions.",
         "Automation bias arises chiefly because people grow lazy once machines do part of their work.",
         "People stop checking machines that are usually right, so work should keep them engaged.",
         "Navigation apps should not be relied on by drivers when roads may be flooded by heavy rain."],
   opts_hi=["मशीनें लोगों से कम विश्वसनीय हैं और महत्वपूर्ण निर्णयों में उन पर भरोसा नहीं करना चाहिए।",
            "स्वचालन-पूर्वाग्रह मुख्यतः इसलिए होता है कि मशीनों के काम सँभालने पर लोग आलसी हो जाते हैं।",
            "लोग प्रायः सही रहने वाली मशीनों को जाँचना छोड़ देते हैं, इसलिए काम उन्हें जोड़े रखे।",
            "जब भारी वर्षा से सड़कों पर पानी भर सकता हो, तब चालकों को नेविगेशन ऐप पर निर्भर नहीं रहना चाहिए।"],
   ans=2, pos=2)
RQ(p, "Assumption", "hard", "s2", ASSUME, ASSUME_HI,
   "Only 1 is assumed. Asking people to make their own judgement before they see the machine's is offered as a remedy; it can help only if committing to a judgement of one's own keeps attention up. "
   "2 is not assumed: the passage says that machines are 'often' more reliable than people, not that they are more reliable at every task.",
   "केवल 1 पूर्वधारणा है। लोगों से मशीन का निर्णय देखने से पहले अपना निर्णय लेने को कहना उपाय के रूप में दिया गया है; यह तभी सहायक है जब अपना निर्णय तय करना ध्यान बनाए रखे। "
   "2 पूर्वधारणा नहीं है: परिच्छेद कहता है कि मशीनें 'प्रायः' लोगों से अधिक विश्वसनीय हैं, यह नहीं कि वे हर काम में अधिक विश्वसनीय हैं।",
   "assumptions",
   st=["People stay more attentive when they must first commit to a judgement of their own.",
       "Machines are more reliable than people at every kind of task."],
   st_hi=["जब लोगों को पहले अपना निर्णय तय करना पड़ता है, तो वे अधिक सजग रहते हैं।",
          "मशीनें हर प्रकार के काम में लोगों से अधिक विश्वसनीय हैं।"],
   key=0)

# ------------------------------------------------------------------ P09 wolves and the rivers they were said to change (3)
p = passage("p09",
  "Removing a top predator can change a landscape in ways that seem to have nothing to do with it. Where wolves were wiped out, deer and elk multiplied and browsed the young trees along rivers so heavily that the trees could not grow; with fewer roots to hold them, banks eroded, and streams widened and warmed. "
  "When wolves were brought back to some such places, browsing near rivers fell -- partly because there were fewer elk, partly because the elk avoided spots where they could be ambushed -- and in places willows and aspens began to recover. Ecologists call such chains of effects trophic cascades. "
  "The popular story of wolves 'changing the course of rivers' has been simplified, however: in many valleys recovery has been slow or patchy, because decades of overgrazing and the loss of beavers had changed the streams in ways that the return of one predator could not quickly undo.",
  "किसी शीर्ष शिकारी को हटाने से भू-दृश्य ऐसे ढंग से बदल सकता है जिसका उससे कोई संबंध नहीं दिखता। जहाँ भेड़िये समाप्त कर दिए गए, वहाँ हिरण और एल्क बढ़ गए और उन्होंने नदियों के किनारे के छोटे पेड़ों को इतना चरा कि पेड़ बढ़ ही नहीं सके; उन्हें थामने वाली जड़ें कम होने से किनारे कटे, और धाराएँ चौड़ी और गर्म हो गईं। "
  "जब ऐसे कुछ स्थानों पर भेड़िये वापस लाए गए, तो नदियों के पास चराई घटी -- आंशिक रूप से इसलिए कि एल्क कम हो गए, आंशिक रूप से इसलिए कि एल्क उन जगहों से बचने लगे जहाँ उन पर घात लगाकर हमला हो सकता था -- और कहीं-कहीं विलो और एस्पेन फिर उगने लगे। पारिस्थितिकीविद ऐसे प्रभावों की शृंखला को पोषण-सोपानी प्रपात (ट्रॉफ़िक कैस्केड) कहते हैं। "
  "फिर भी भेड़ियों के 'नदियों का मार्ग बदल देने' की लोकप्रिय कहानी सरलीकृत है: कई घाटियों में सुधार धीमा या टुकड़ों में हुआ है, क्योंकि दशकों की अति-चराई और ऊदबिलावों (बीवर) के समाप्त होने ने धाराओं को ऐसे बदल दिया था जिसे एक शिकारी की वापसी जल्दी नहीं पलट सकती थी।")
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Neither is valid. 1 goes beyond the passage: it names the loss of beavers as one of the reasons the streams changed, but never says that their return alone would restore the streams. "
   "2 is contradicted: willows and aspens began to recover only 'in places', and recovery has been slow or patchy in many valleys.",
   "कोई भी वैध नहीं है। 1 परिच्छेद से आगे जाता है: वह ऊदबिलावों के समाप्त होने को धाराओं के बदलने के कारणों में गिनता है, पर कहीं नहीं कहता कि केवल उनकी वापसी धाराओं को ठीक कर देगी। "
   "2 का खंडन होता है: विलो और एस्पेन केवल 'कहीं-कहीं' फिर उगने लगे, और कई घाटियों में सुधार धीमा या टुकड़ों में रहा है।",
   "conclusions",
   st=["The return of beavers would by itself be enough to restore the streams of these valleys.",
       "Wherever wolves have returned, the willows and aspens along the rivers have recovered fully."],
   st_hi=["केवल ऊदबिलावों की वापसी इन घाटियों की धाराओं को ठीक करने के लिए पर्याप्त होगी।",
          "जहाँ भी भेड़िये लौटे हैं, वहाँ नदियों के किनारे के विलो और एस्पेन पूरी तरह फिर उग आए हैं।"],
   key=3)
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage shows how losing wolves set off a chain of effects down to the rivers, and then warns that bringing them back has not quickly reversed the damage everywhere. "
   "It says that recovery has been slow or patchy in many valleys, so not every valley has been restored; it blames the elk's browsing in these places, not everywhere; and it gives the elk's avoiding ambush spots as an effect beyond the number killed.",
   "परिच्छेद दिखाता है कि भेड़ियों के न रहने से प्रभावों की एक शृंखला नदियों तक कैसे पहुँची, और फिर चेताता है कि उन्हें वापस लाने से हर जगह क्षति जल्दी नहीं पलटी। "
   "वह कहता है कि कई घाटियों में सुधार धीमा या टुकड़ों में रहा, इसलिए हर घाटी ठीक नहीं हुई; वह इन स्थानों में एल्क की चराई को दोष देता है, हर जगह नहीं; और वह एल्क के घात वाली जगहों से बचने को मारे गए जानवरों की संख्या से परे का प्रभाव बताता है।",
   "crux",
   opts=["Bringing back wolves has restored every river valley into which they have been reintroduced.",
         "Elk and deer are the main cause of the erosion of river banks in all parts of the world.",
         "Top predators matter to an ecosystem only because of the number of animals that they hunt and kill.",
         "A top predator's loss can ripple through an ecosystem, and its return may not quickly undo that."],
   opts_hi=["भेड़ियों को वापस लाने से हर उस घाटी की नदियाँ ठीक हो गई हैं जिसमें उन्हें फिर से बसाया गया।",
            "दुनिया के सभी भागों में नदी किनारों के कटाव का मुख्य कारण एल्क और हिरण हैं।",
            "शीर्ष शिकारी किसी पारितंत्र के लिए केवल इसलिए महत्वपूर्ण हैं कि वे कितने जानवर मारते हैं।",
            "शीर्ष शिकारी का न रहना पूरे पारितंत्र में फैल सकता है, और उसकी वापसी इसे जल्दी नहीं पलटती।"],
   ans=3, pos=3)
RQ(p, "Specific Detail", "medium", "mcq",
   "According to the passage, why did browsing near rivers fall when wolves were brought back?",
   "परिच्छेद के अनुसार, भेड़ियों को वापस लाने पर नदियों के पास चराई क्यों घटी?",
   "The passage gives both reasons: there were fewer elk, and the elk avoided spots where they could be ambushed -- a change in behaviour as well as in numbers. "
   "It does not say that the wolves ate the young trees' seedlings, that the rivers flooded the grazing land, or that the deer moved to other continents.",
   "परिच्छेद दोनों कारण देता है: एल्क कम हो गए, और एल्क उन जगहों से बचने लगे जहाँ उन पर घात लगाकर हमला हो सकता था -- संख्या के साथ-साथ व्यवहार में भी बदलाव। "
   "वह यह नहीं कहता कि भेड़िये छोटे पेड़ों के अंकुर खा गए, कि नदियों ने चरागाहों को डुबो दिया, या कि हिरण दूसरे महाद्वीपों में चले गए।",
   "why-browsing-fell",
   opts=["Fewer elk, and elk shunning spots where they could be ambushed",
         "The wolves themselves ate most of the young trees' seedlings",
         "The rivers flooded the meadows on which the elk used to graze",
         "The deer and elk left those valleys for other continents entirely"],
   opts_hi=["कम एल्क, और एल्क का उन जगहों से बचना जहाँ घात लग सकती थी",
            "भेड़िये स्वयं छोटे पेड़ों के अधिकांश अंकुर खा गए",
            "नदियों ने उन घास के मैदानों को डुबो दिया जहाँ एल्क चरते थे",
            "हिरण और एल्क उन घाटियों को छोड़कर पूरी तरह दूसरे महाद्वीपों में चले गए"],
   ans=0, pos=0)

# ------------------------------------------------------------------ P10 inflation as a tax on cash (3)
p = passage("p10",
  "Inflation is sometimes called a tax that nobody votes for. When prices rise, money held as cash or in accounts that pay little interest buys less, and the loss falls hardest on those who keep their savings in that form -- typically poorer households, who have no shares or property to rise in value along with prices. "
  "Wages and pensions fixed in money terms also lose ground until they are revised, and the revisions come late. Debtors, on the other hand, gain when inflation was not expected, because they repay loans in money that is worth less; "
  "and since governments are large debtors, a burst of unexpected inflation quietly lightens the public debt. None of this makes all inflation harmful: a low and steady rate that everyone expects does little damage, because contracts, wages and interest rates adjust to it in advance. "
  "The harm comes chiefly from inflation that is high, or that comes as a surprise.",
  "मुद्रास्फीति को कभी-कभी ऐसा कर कहा जाता है जिसके पक्ष में कोई मत नहीं देता। जब क़ीमतें बढ़ती हैं, तो नक़द या कम ब्याज देने वाले खातों में रखा पैसा कम ख़रीद पाता है, और हानि उन पर सबसे भारी पड़ती है जो अपनी बचत इसी रूप में रखते हैं -- प्रायः ग़रीब परिवार, जिनके पास ऐसे शेयर या संपत्ति नहीं जिनका मूल्य क़ीमतों के साथ बढ़े। "
  "पैसे के रूप में तय मज़दूरी और पेंशन भी संशोधित होने तक पिछड़ती रहती हैं, और संशोधन देर से आते हैं। दूसरी ओर, जब मुद्रास्फीति अपेक्षित नहीं थी तब ऋणी लाभ में रहते हैं, क्योंकि वे ऋण ऐसे पैसे से चुकाते हैं जिसका मूल्य कम हो गया है; "
  "और चूँकि सरकारें बड़ी ऋणी होती हैं, अचानक आई मुद्रास्फीति चुपचाप सार्वजनिक ऋण को हल्का कर देती है। इससे हर मुद्रास्फीति हानिकारक नहीं हो जाती: एक कम और स्थिर दर जिसकी सब अपेक्षा करते हैं, थोड़ी ही हानि करती है, क्योंकि अनुबंध, मज़दूरी और ब्याज दरें पहले से उसके अनुसार ढल जाती हैं। "
  "हानि मुख्यतः उस मुद्रास्फीति से होती है जो ऊँची हो, या अचानक आए।")
RQ(p, "Best Summary", "medium", "mcq", MSG, MSG_HI,
   "The passage shows who loses (holders of cash and of fixed wages and pensions) and who gains (debtors, governments included) when inflation is high or unexpected, and adds that a low, expected rate does little harm. "
   "It does not call all inflation harmful; it says that debtors gain only when inflation was not expected, not always; and it says that governments' debt is lightened 'quietly', not that they create inflation on purpose.",
   "परिच्छेद दिखाता है कि ऊँची या अचानक आई मुद्रास्फीति में कौन हारता है (नक़द और तय मज़दूरी तथा पेंशन वाले) और कौन लाभ पाता है (ऋणी, सरकारों सहित), और जोड़ता है कि कम, अपेक्षित दर थोड़ी ही हानि करती है। "
   "वह हर मुद्रास्फीति को हानिकारक नहीं कहता; वह कहता है कि ऋणी केवल तब लाभ पाते हैं जब मुद्रास्फीति अपेक्षित न हो, हमेशा नहीं; और वह कहता है कि सरकारों का ऋण 'चुपचाप' हल्का होता है, यह नहीं कि वे जानबूझकर मुद्रास्फीति पैदा करती हैं।",
   "message",
   opts=["Every kind of inflation, however low and steady it may be, harms the poor and ought to be brought to an end at once.",
         "Debtors always gain from inflation at the expense of savers, whether or not it was expected when their loans were made.",
         "High or surprise inflation shifts wealth from cash and fixed incomes to debtors; expected inflation does little harm.",
         "Governments deliberately create inflation from time to time so as to reduce the burden of the large debts that they owe."],
   opts_hi=["हर प्रकार की मुद्रास्फीति, चाहे वह कितनी ही कम और स्थिर हो, ग़रीबों को हानि पहुँचाती है और उसे तुरंत समाप्त कर देना चाहिए।",
            "ऋणी मुद्रास्फीति से बचतकर्ताओं की क़ीमत पर हमेशा लाभ पाते हैं, चाहे ऋण देते समय उसकी अपेक्षा रही हो या नहीं।",
            "ऊँची या अचानक मुद्रास्फीति धन को नक़द और तय आय से ऋणियों की ओर ले जाती है; कम, अपेक्षित मुद्रास्फीति थोड़ी हानि करती है।",
            "सरकारें अपने ऊपर के बड़े ऋणों का बोझ घटाने के लिए समय-समय पर जानबूझकर मुद्रास्फीति पैदा करती रहती हैं।"],
   ans=2, pos=2)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Only 1 is valid. Pensions fixed in money terms lose ground until they are revised, so a pension revised only every few years falls further behind in a year of high inflation than one revised every month. "
   "2 is not valid: when inflation is fully expected, interest rates 'adjust to it in advance', so the borrower does not gain at the lender's expense; the passage gives debtors a gain only when inflation was not expected.",
   "केवल 1 वैध है। पैसे के रूप में तय पेंशन संशोधित होने तक पिछड़ती रहती है, इसलिए हर कुछ वर्षों में एक बार संशोधित होने वाली पेंशन ऊँची मुद्रास्फीति के वर्ष में हर महीने संशोधित होने वाली पेंशन से अधिक पीछे रह जाती है। "
   "2 वैध नहीं है: जब मुद्रास्फीति पूरी तरह अपेक्षित हो, तो ब्याज दरें 'पहले से उसके अनुसार ढल जाती हैं', इसलिए उधारकर्ता ऋणदाता की क़ीमत पर लाभ नहीं पाता; परिच्छेद ऋणियों को लाभ केवल तब देता है जब मुद्रास्फीति अपेक्षित न हो।",
   "conclusions",
   st=["In a year of high inflation, a pensioner whose pension is revised only every few years loses more than one whose pension is revised every month.",
       "If inflation is fully expected when a loan is made, the borrower gains at the lender's expense."],
   st_hi=["ऊँची मुद्रास्फीति के वर्ष में जिस पेंशनभोगी की पेंशन केवल हर कुछ वर्षों में संशोधित होती है, वह हर महीने संशोधित पेंशन वाले से अधिक खोता है।",
          "यदि ऋण देते समय मुद्रास्फीति पूरी तरह अपेक्षित हो, तो उधारकर्ता ऋणदाता की क़ीमत पर लाभ पाता है।"],
   key=0)
RQ(p, "Assumption", "hard", "s2", ASSUME, ASSUME_HI,
   "Only 2 is assumed. The passage says that poorer households suffer more because they 'have no shares or property to rise in value along with prices'; that reasoning takes it for granted that shares and property do tend to rise in value with the price level. "
   "1 is not assumed: the passage says that unexpected inflation 'quietly lightens the public debt' as a side effect, and nowhere suggests that governments create inflation on purpose.",
   "केवल 2 पूर्वधारणा है। परिच्छेद कहता है कि ग़रीब परिवार अधिक हानि उठाते हैं क्योंकि उनके पास 'ऐसे शेयर या संपत्ति नहीं जिनका मूल्य क़ीमतों के साथ बढ़े'; यह तर्क मान लेता है कि शेयरों और संपत्ति का मूल्य सामान्य मूल्य-स्तर के साथ बढ़ने की प्रवृत्ति रखता है। "
   "1 पूर्वधारणा नहीं है: परिच्छेद कहता है कि अचानक मुद्रास्फीति एक दुष्प्रभाव के रूप में 'चुपचाप सार्वजनिक ऋण को हल्का कर देती है', और कहीं नहीं सुझाता कि सरकारें जानबूझकर मुद्रास्फीति पैदा करती हैं।",
   "assumptions",
   st=["Governments deliberately cause inflation in order to reduce what they owe.",
       "The prices of shares and property tend to rise along with the general level of prices."],
   st_hi=["सरकारें अपना ऋण घटाने के लिए जानबूझकर मुद्रास्फीति पैदा करती हैं।",
          "शेयरों और संपत्ति की क़ीमतें सामान्य मूल्य-स्तर के साथ बढ़ने की प्रवृत्ति रखती हैं।"],
   key=1)
