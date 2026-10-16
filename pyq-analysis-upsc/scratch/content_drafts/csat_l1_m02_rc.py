# -*- coding: utf-8 -*-
"""CSAT Level 1 · Mini 2 -- Reading Comprehension: 5 original passages, 14 items (four with three items, the third
passage with two), at the foundation level: passages of about 140-155 words and 4 easy / 8 medium / 2 hard items.

Themes, none used in Level 2's 70 passages or in Mini 1: the certainty rather than the size of a penalty, testing
oneself against re-reading, a cooking-gas connection that is not refilled, oral epics and the archives that record
them, and what bystanders can do in the minutes after a heart stops. Item types: main idea 3, inference 4,
assumption 3, specific detail 2 (one of them 'NOT mentioned'), best summary 2. Options are named by content in every
explanation."""
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

# ------------------------------------------------------------------ P01 the certainty of a penalty (3)
p = passage("p01",
  "When a city wants drivers to stop jumping red lights, its first idea is often to raise the fine. Yet studies of deterrence have long suggested that what changes behaviour is less the size of a penalty than the chance of facing it. "
  "A driver who believes that a red light is watched by a camera, and that a ticket will arrive within days, slows down even if the fine is modest. "
  "A driver who knows that the light is rarely watched will take the risk even if the fine is heavy, because a large penalty that almost never falls weighs little in a quick decision at a crossing. "
  "Raising fines is cheap and makes a strong announcement; steady enforcement is costly and dull. That is why cities so often choose the first, and are surprised when little changes.",
  "जब कोई शहर चाहता है कि चालक लाल बत्ती पार करना बंद करें, तो उसका पहला विचार अक्सर जुर्माना बढ़ाने का होता है। फिर भी निवारण (deterrence) पर अध्ययन लंबे समय से संकेत देते रहे हैं कि व्यवहार दंड के आकार से कम और उसके मिलने की संभावना से अधिक बदलता है। "
  "जो चालक मानता है कि लाल बत्ती पर कैमरे की नज़र है, और चालान कुछ ही दिनों में आ जाएगा, वह जुर्माना मामूली होने पर भी धीमा हो जाता है। "
  "जो चालक जानता है कि बत्ती पर शायद ही नज़र रखी जाती है, वह जुर्माना भारी होने पर भी जोखिम उठाएगा, क्योंकि जो बड़ा दंड लगभग कभी नहीं लगता, उसका चौराहे पर लिए जाने वाले त्वरित निर्णय में बहुत कम वज़न होता है। "
  "जुर्माना बढ़ाना सस्ता है और एक ज़ोरदार घोषणा बनता है; लगातार प्रवर्तन महँगा और नीरस है। यही कारण है कि शहर अक्सर पहला रास्ता चुनते हैं, और जब बहुत कम बदलता है तो हैरान होते हैं।")
RQ(p, "Main Idea", "easy", "mcq", CRUX, CRUX_HI,
   "The passage argues that drivers respond to how likely they are to face a penalty more than to how large it is, and that cities nonetheless prefer raising fines because it is cheap and showy. "
   "It does not ask cities to stop fining drivers or to put cameras at every crossing; it does not say that drivers are unaware of the fines; and it does not claim that heavy fines never change behaviour -- only that a heavy fine that almost never falls weighs little.",
   "परिच्छेद का तर्क है कि चालक दंड के आकार से अधिक इस पर प्रतिक्रिया करते हैं कि उसके मिलने की कितनी संभावना है, और फिर भी शहर जुर्माना बढ़ाना पसंद करते हैं क्योंकि वह सस्ता और दिखावटी है। "
   "वह शहरों से जुर्माना बंद करने या हर चौराहे पर कैमरे लगाने को नहीं कहता; वह यह नहीं कहता कि चालक जुर्मानों से अनजान हैं; और वह यह दावा नहीं करता कि भारी जुर्माने व्यवहार को कभी नहीं बदलते -- केवल यह कि जो भारी जुर्माना लगभग कभी नहीं लगता उसका वज़न कम होता है।",
   "crux",
   opts=["Drivers are deterred more by the chance of being caught than by the size of the fine.",
         "Cities should stop fining drivers and spend the money on cameras at every single crossing.",
         "Most drivers who jump red lights do not know how large the fine for doing so is.",
         "Heavy fines never change how anyone behaves at a traffic light, however often they are imposed."],
   opts_hi=["चालक जुर्माने के आकार से अधिक पकड़े जाने की संभावना से रुकते हैं।",
            "शहरों को चालकों पर जुर्माना लगाना बंद करके वह धन हर एक चौराहे पर कैमरों पर ख़र्च करना चाहिए।",
            "लाल बत्ती पार करने वाले अधिकतर चालक नहीं जानते कि ऐसा करने का जुर्माना कितना है।",
            "भारी जुर्माने ट्रैफ़िक बत्ती पर किसी के व्यवहार को कभी नहीं बदलते, चाहे वे कितनी भी बार लगाए जाएँ।"],
   ans=0, pos=1)
RQ(p, "Assumption", "medium", "s2", ASSUME, ASSUME_HI,
   "Only 1 is assumed. The whole argument rests on drivers responding to how likely a ticket is -- slowing down when they believe the light is watched and taking the risk when they know it is not -- which takes for granted that they weigh, at least roughly, their chance of being caught. "
   "2 is not assumed: the passage says that steady enforcement is costly, but it nowhere compares the cost of cameras with the money that fines bring in.",
   "केवल 1 पूर्वधारणा है। पूरा तर्क इस पर टिका है कि चालक चालान की संभावना पर प्रतिक्रिया करते हैं -- यह मानने पर कि बत्ती पर नज़र है वे धीमे होते हैं और यह जानने पर कि नहीं है, जोखिम उठाते हैं -- जो यह मानकर चलता है कि वे कम से कम मोटे तौर पर पकड़े जाने की अपनी संभावना तौलते हैं। "
   "2 पूर्वधारणा नहीं है: परिच्छेद कहता है कि लगातार प्रवर्तन महँगा है, पर वह कहीं भी कैमरों की लागत की तुलना जुर्मानों से आने वाले धन से नहीं करता।",
   "assumptions",
   st=["Drivers at a crossing weigh, at least roughly, how likely they are to be caught.",
       "Cameras at crossings cost more to install and run than the fines they bring in."],
   st_hi=["चौराहे पर चालक कम से कम मोटे तौर पर यह तौलते हैं कि उनके पकड़े जाने की कितनी संभावना है।",
          "चौराहों पर कैमरे लगाने और चलाने की लागत उनसे आने वाले जुर्मानों से अधिक है।"],
   key=0)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Both are valid. 1: at a light that is rarely watched, a heavier fine is 'a large penalty that almost never falls', which the passage says weighs little -- so doubling it is unlikely to change much. "
   "2: the passage says that a driver who expects a ticket within days slows down 'even if the fine is modest', while a heavy fine that is rarely imposed does not stop the risk-taker.",
   "दोनों वैध हैं। 1: जिस बत्ती पर शायद ही नज़र रखी जाती है, वहाँ भारी जुर्माना 'ऐसा बड़ा दंड है जो लगभग कभी नहीं लगता', जिसका परिच्छेद के अनुसार वज़न कम होता है -- इसलिए उसे दुगुना करने से बहुत कुछ बदलने की संभावना नहीं। "
   "2: परिच्छेद कहता है कि जो चालक कुछ दिनों में चालान की अपेक्षा करता है, वह 'जुर्माना मामूली होने पर भी' धीमा हो जाता है, जबकि शायद ही लगने वाला भारी जुर्माना जोखिम उठाने वाले को नहीं रोकता।",
   "conclusions",
   st=["Doubling the fine at a crossing that is rarely watched is unlikely to change much.",
       "A modest fine that is imposed reliably can deter drivers better than a heavy fine that is rarely imposed."],
   st_hi=["जिस चौराहे पर शायद ही नज़र रखी जाती है, वहाँ जुर्माना दुगुना करने से बहुत कुछ बदलने की संभावना नहीं है।",
          "भरोसे से लगाया जाने वाला मामूली जुर्माना, शायद ही लगाए जाने वाले भारी जुर्माने से बेहतर ढंग से चालकों को रोक सकता है।"],
   key=2)

# ------------------------------------------------------------------ P02 testing oneself against re-reading (3)
p = passage("p02",
  "Students preparing for an examination often read their notes again and again, underlining as they go. The pages grow familiar, and familiarity feels like learning. "
  "But recognising a page is not the same as being able to recall what is on it without the page in front of you, which is what an examination demands. "
  "Experiments in classrooms have repeatedly found that students who spend part of their time testing themselves -- closing the book and trying to write down or explain what they have read -- remember more weeks later than students who spend the same time re-reading. "
  "Self-testing feels harder and less pleasant, and it exposes how much one does not yet know. That discomfort is not a sign that the method is failing; it is part of why it works.",
  "परीक्षा की तैयारी करने वाले विद्यार्थी अक्सर अपने नोट्स बार-बार पढ़ते हैं, साथ-साथ रेखांकन करते हुए। पन्ने परिचित होते जाते हैं, और परिचय सीखने जैसा लगता है। "
  "पर किसी पन्ने को पहचान लेना उस पर लिखी बात को पन्ना सामने न होने पर याद कर पाने के समान नहीं है, और परीक्षा यही माँगती है। "
  "कक्षाओं में किए गए प्रयोगों में बार-बार पाया गया है कि जो विद्यार्थी अपने समय का कुछ भाग स्वयं की परीक्षा लेने में लगाते हैं -- किताब बंद करके जो पढ़ा उसे लिखने या समझाने का प्रयास करते हुए -- वे सप्ताहों बाद उन विद्यार्थियों से अधिक याद रखते हैं जो उतना ही समय दोबारा पढ़ने में लगाते हैं। "
  "स्वयं की परीक्षा लेना कठिन और कम सुखद लगता है, और यह उजागर करता है कि अभी कितना नहीं आता। यह असुविधा इस बात का संकेत नहीं कि तरीक़ा विफल हो रहा है; यह इसका हिस्सा है कि वह क्यों काम करता है।")
RQ(p, "Best Summary", "medium", "mcq", SUMMARY, SUMMARY_HI,
   "The passage contrasts recognising familiar pages with recalling their content, notes that examinations demand recall, and reports that self-testing, though harder, leads to better recall than re-reading. "
   "It does not call re-reading useless or tell students to give up underlining; it says nothing about longer hours of study; and it says that examinations demand recall, not that they should test recognition.",
   "परिच्छेद परिचित पन्नों को पहचानने और उनकी सामग्री को याद कर पाने में अंतर करता है, बताता है कि परीक्षा याद करना माँगती है, और यह बताता है कि स्वयं की परीक्षा लेना कठिन होते हुए भी दोबारा पढ़ने से बेहतर याद दिलाता है। "
   "वह दोबारा पढ़ने को बेकार नहीं कहता और न विद्यार्थियों से रेखांकन छोड़ने को कहता है; वह अधिक घंटे पढ़ने के बारे में कुछ नहीं कहता; और वह कहता है कि परीक्षा याद करना माँगती है, यह नहीं कि उसे पहचान की जाँच करनी चाहिए।",
   "summary",
   opts=["Testing oneself is harder than re-reading but builds the recall that examinations demand.",
         "Re-reading notes is useless, and students should give up underlining and highlighting altogether.",
         "Students remember more when they study for longer hours, whatever method of study they use.",
         "Examinations should test whether students recognise material rather than whether they can recall it."],
   opts_hi=["स्वयं की परीक्षा लेना दोबारा पढ़ने से कठिन है पर वह याद करने की वह क्षमता बनाता है जो परीक्षा माँगती है।",
            "नोट्स दोबारा पढ़ना बेकार है, और विद्यार्थियों को रेखांकन और हाइलाइट करना पूरी तरह छोड़ देना चाहिए।",
            "विद्यार्थी अधिक घंटे पढ़ने पर अधिक याद रखते हैं, चाहे वे पढ़ने का कोई भी तरीक़ा अपनाएँ।",
            "परीक्षाओं को यह जाँचना चाहिए कि विद्यार्थी सामग्री पहचानते हैं या नहीं, न कि यह कि वे उसे याद कर सकते हैं या नहीं।"],
   ans=0, pos=3)
RQ(p, "Specific Detail", "easy", "mcq",
   "According to the passage, what did the experiments in classrooms find?",
   "परिच्छेद के अनुसार, कक्षाओं में किए गए प्रयोगों में क्या पाया गया?",
   "The passage says that students who spent part of their time testing themselves 'remember more weeks later than students who spend the same time re-reading'. "
   "It says the opposite of feeling less sure after re-reading -- re-reading feels familiar; it reports nothing about underlining; and the comparison was between students who spent the same time, not more hours.",
   "परिच्छेद कहता है कि जिन विद्यार्थियों ने अपने समय का कुछ भाग स्वयं की परीक्षा लेने में लगाया वे 'सप्ताहों बाद उन विद्यार्थियों से अधिक याद रखते हैं जो उतना ही समय दोबारा पढ़ने में लगाते हैं'। "
   "वह दोबारा पढ़ने के बाद कम आश्वस्त महसूस करने का उलटा कहता है -- दोबारा पढ़ना परिचित लगता है; रेखांकन के बारे में कुछ नहीं बताता; और तुलना उतना ही समय लगाने वाले विद्यार्थियों के बीच थी, अधिक घंटों की नहीं।",
   "detail",
   opts=["Students who tested themselves remembered more weeks later than those who re-read.",
         "Students who re-read their notes felt less sure of themselves than those who tested themselves.",
         "Students who underlined their notes remembered more than those who did not underline them.",
         "Students who tested themselves spent more hours studying than those who re-read their notes."],
   opts_hi=["स्वयं की परीक्षा लेने वालों ने सप्ताहों बाद दोबारा पढ़ने वालों से अधिक याद रखा।",
            "नोट्स दोबारा पढ़ने वाले विद्यार्थी स्वयं की परीक्षा लेने वालों से कम आश्वस्त महसूस करते थे।",
            "जिन विद्यार्थियों ने अपने नोट्स में रेखांकन किया उन्होंने रेखांकन न करने वालों से अधिक याद रखा।",
            "स्वयं की परीक्षा लेने वाले विद्यार्थियों ने दोबारा पढ़ने वालों से अधिक घंटे पढ़ाई की।"],
   ans=0, pos=2)
RQ(p, "Inference", "hard", "sc", INFER, INFER_HI,
   "1 can be drawn: familiarity 'feels like learning' while recognising a page is not the same as recalling it, so a student who feels well prepared may still recall little. "
   "2 cannot: the passage says that the discomfort of self-testing is 'not a sign that the method is failing' but part of why it works. "
   "3 cannot: the passage says only that examinations demand recall; it says nothing about how re-reading would fare on a test of recognition, so this goes beyond it. Only 1 can be drawn.",
   "1 निकाला जा सकता है: परिचय 'सीखने जैसा लगता है' जबकि पन्ना पहचानना उसे याद कर पाने के समान नहीं, इसलिए जो विद्यार्थी स्वयं को अच्छी तरह तैयार महसूस करता है वह भी कम याद कर सकता है। "
   "2 नहीं निकाला जा सकता: परिच्छेद कहता है कि स्वयं की परीक्षा लेने की असुविधा 'इस बात का संकेत नहीं कि तरीक़ा विफल हो रहा है', बल्कि इसका हिस्सा है कि वह क्यों काम करता है। "
   "3 नहीं निकाला जा सकता: परिच्छेद केवल इतना कहता है कि परीक्षा याद करना माँगती है; वह यह कुछ नहीं कहता कि पहचान की परीक्षा में दोबारा पढ़ना कैसा रहेगा, इसलिए यह उससे आगे चला जाता है। केवल 1 निकाला जा सकता है।",
   "inferences",
   st=["A student's feeling of being well prepared can be a poor guide to how much the student will recall in an examination.",
       "Students who find testing themselves unpleasant are probably doing it wrongly.",
       "Re-reading would work better than self-testing for an examination that asked students only to recognise material."],
   st_hi=["किसी विद्यार्थी का स्वयं को अच्छी तरह तैयार महसूस करना इस बात का कमज़ोर संकेत हो सकता है कि वह परीक्षा में कितना याद कर पाएगा।",
          "जिन विद्यार्थियों को स्वयं की परीक्षा लेना अप्रिय लगता है, वे शायद उसे ग़लत ढंग से कर रहे हैं।",
          "जिस परीक्षा में विद्यार्थियों से केवल सामग्री पहचानने को कहा जाए, उसके लिए दोबारा पढ़ना स्वयं की परीक्षा लेने से बेहतर काम करेगा।"],
   opts=["1 only", "1 and 2 only", "1 and 3 only", "1, 2 and 3"], key=0)

# ------------------------------------------------------------------ P03 a cooking-gas connection that is not refilled (2)
p = passage("p03",
  "Over the past decade, tens of millions of poor households in India have received a cooking-gas connection, often with help to pay for the stove and the first cylinder. "
  "Yet surveys have found that many of them still cook much of the time on wood, dung or crop waste, refilling their cylinders only a few times a year. The reasons are not hard to find. "
  "A refill costs cash that must be found all at once, while wood can be gathered a little at a time without money; the gas agency may be far away; and many families are used to the taste of food cooked on a wood fire. "
  "A connection is the start of a change, not the change itself. Counting connections tells us how far a scheme has reached; counting refills tells us how far it has worked.",
  "पिछले एक दशक में भारत के करोड़ों ग़रीब परिवारों को रसोई गैस का कनेक्शन मिला है, अक्सर चूल्हे और पहले सिलेंडर का भुगतान करने में सहायता के साथ। "
  "फिर भी सर्वेक्षणों में पाया गया है कि उनमें से बहुत से परिवार अब भी अधिकतर समय लकड़ी, गोबर या फ़सल के अवशेष पर खाना पकाते हैं, और वर्ष में केवल कुछ ही बार सिलेंडर भरवाते हैं। कारण खोजना कठिन नहीं है। "
  "सिलेंडर भरवाने के लिए एक साथ नक़द चाहिए, जबकि लकड़ी बिना पैसे के थोड़ी-थोड़ी इकट्ठी की जा सकती है; गैस एजेंसी दूर हो सकती है; और बहुत से परिवार लकड़ी की आग पर पके भोजन के स्वाद के आदी हैं। "
  "कनेक्शन बदलाव की शुरुआत है, स्वयं बदलाव नहीं। कनेक्शन गिनना बताता है कि कोई योजना कितनी दूर तक पहुँची है; सिलेंडर भरवाने की संख्या गिनना बताता है कि वह कितनी कारगर रही है।")
RQ(p, "Main Idea", "easy", "mcq", CRUX, CRUX_HI,
   "The passage says that many households with a gas connection still cook mostly on wood, dung or crop waste, explains why, and ends that a connection is only the start of a change: refills show how far a scheme has worked. "
   "It does not say that poor households will never switch -- taste is only one of three reasons; it does not call the scheme a failure or say that most connections are never used ('many' still cook much of the time on other fuels); "
   "and it does not propose opening agencies in every village.",
   "परिच्छेद कहता है कि गैस कनेक्शन वाले बहुत से परिवार अब भी अधिकतर लकड़ी, गोबर या फ़सल के अवशेष पर खाना पकाते हैं, इसके कारण बताता है, और अंत में कहता है कि कनेक्शन बदलाव की केवल शुरुआत है: सिलेंडर भरवाना बताता है कि योजना कितनी कारगर रही। "
   "वह यह नहीं कहता कि ग़रीब परिवार कभी नहीं बदलेंगे -- स्वाद तीन में से केवल एक कारण है; वह योजना को विफल नहीं कहता और न यह कहता है कि अधिकतर कनेक्शन कभी इस्तेमाल नहीं होते ('बहुत से' परिवार अधिकतर समय दूसरे ईंधन पर पकाते हैं); "
   "और वह हर गाँव में एजेंसी खोलने का प्रस्ताव नहीं देता।",
   "crux",
   opts=["A gas connection alone does not change how a family cooks; regular refills show whether it has.",
         "Poor households prefer the taste of food cooked on wood and so will never switch to cooking gas.",
         "The cooking-gas scheme has failed, because most of the households that received connections never use them.",
         "Gas agencies should be opened in every village so that families do not have to travel to refill cylinders."],
   opts_hi=["केवल गैस कनेक्शन से पकाने का ढंग नहीं बदलता; नियमित रूप से सिलेंडर भरवाना बताता है कि बदला या नहीं।",
            "ग़रीब परिवार लकड़ी पर पके भोजन का स्वाद पसंद करते हैं और इसलिए कभी रसोई गैस नहीं अपनाएँगे।",
            "रसोई गैस योजना विफल रही है, क्योंकि कनेक्शन पाने वाले अधिकतर परिवार उनका कभी उपयोग नहीं करते।",
            "हर गाँव में गैस एजेंसियाँ खोली जानी चाहिए ताकि परिवारों को सिलेंडर भरवाने के लिए यात्रा न करनी पड़े।"],
   ans=0, pos=2)
RQ(p, "Assumption", "medium", "s2", ASSUME, ASSUME_HI,
   "Only 2 is assumed. The passage's last sentence treats the count of refills as the measure of how far the scheme has worked, which holds only if the refills a household buys reflect, at least roughly, how much it cooks with gas. "
   "1 is not assumed: the passage says that wood can be gathered without money, a cash difference, but it does not claim that wood, dung or crop waste is the cheapest way to cook once every cost is counted.",
   "केवल 2 पूर्वधारणा है। परिच्छेद का अंतिम वाक्य सिलेंडर भरवाने की संख्या को इस बात का माप मानता है कि योजना कितनी कारगर रही, जो तभी सही है जब किसी परिवार द्वारा भरवाए गए सिलेंडर कम से कम मोटे तौर पर यह दिखाएँ कि वह गैस पर कितना पकाता है। "
   "1 पूर्वधारणा नहीं है: परिच्छेद कहता है कि लकड़ी बिना पैसे के इकट्ठी की जा सकती है, जो नक़द का अंतर है, पर वह यह दावा नहीं करता कि हर लागत गिनने पर लकड़ी, गोबर या फ़सल के अवशेष पर पकाना सबसे सस्ता है।",
   "assumptions",
   st=["Cooking on wood, dung or crop waste is the cheapest way for a poor family to cook.",
       "The number of refills a household buys shows, at least roughly, how much it cooks with gas."],
   st_hi=["लकड़ी, गोबर या फ़सल के अवशेष पर खाना पकाना किसी ग़रीब परिवार के लिए सबसे सस्ता तरीक़ा है।",
          "कोई परिवार जितनी बार सिलेंडर भरवाता है, वह कम से कम मोटे तौर पर दिखाता है कि वह गैस पर कितना पकाता है।"],
   key=1)

# ------------------------------------------------------------------ P04 oral epics and the archives that record them (3)
p = passage("p04",
  "Across India, songs, stories and epics have been handed down for centuries not in books but from one singer to the next. Many of these traditions are now fading, as the young move to towns and the old singers die. "
  "Archives have rushed to record them, and a recording is far better than nothing. But a tradition is more than a set of texts. "
  "A singer performing an epic changes it to suit the audience of the evening: shortens a tale when children are listening, lengthens it on a festival night, and answers the listeners who call out. "
  "A recording captures one night's version and fixes it for ever. What keeps a tradition alive is not a store of recordings but people who still sing, and listeners who still want to hear them.",
  "पूरे भारत में गीत, कथाएँ और महाकाव्य सदियों से किताबों में नहीं, बल्कि एक गायक से अगले गायक तक सौंपे जाते रहे हैं। इनमें से कई परंपराएँ अब लुप्त हो रही हैं, क्योंकि युवा कस्बों में चले जाते हैं और पुराने गायक दुनिया छोड़ जाते हैं। "
  "अभिलेखागार उन्हें रिकॉर्ड करने में जुटे हैं, और रिकॉर्डिंग कुछ न होने से कहीं बेहतर है। पर परंपरा पाठों के एक संग्रह से कहीं अधिक है। "
  "महाकाव्य प्रस्तुत करने वाला गायक उसे उस शाम के श्रोताओं के अनुसार बदलता है: बच्चों के सुनते समय कथा छोटी कर देता है, उत्सव की रात उसे लंबा कर देता है, और आवाज़ लगाने वाले श्रोताओं को उत्तर देता है। "
  "रिकॉर्डिंग एक रात का रूप पकड़ लेती है और उसे सदा के लिए स्थिर कर देती है। किसी परंपरा को जीवित रखने वाला रिकॉर्डिंग का भंडार नहीं, बल्कि वे लोग हैं जो अब भी गाते हैं, और वे श्रोता जो अब भी उन्हें सुनना चाहते हैं।")
RQ(p, "Best Summary", "medium", "mcq", SUMMARY, SUMMARY_HI,
   "The passage welcomes recordings as 'far better than nothing' but argues that an oral tradition is a living performance, shaped to each audience, and that it survives only through people who still sing and listeners who still want to hear. "
   "It does not call recording a waste of effort; it gives young people moving to towns and old singers dying, not the archives, as the reasons traditions fade; and fixing an epic in a single written text is the opposite of its point.",
   "परिच्छेद रिकॉर्डिंग को 'कुछ न होने से कहीं बेहतर' मानता है, पर तर्क देता है कि मौखिक परंपरा एक जीवित प्रस्तुति है, जो हर श्रोता-समूह के अनुसार ढलती है, और वह केवल उन लोगों से बचती है जो अब भी गाते हैं और उन श्रोताओं से जो अब भी सुनना चाहते हैं। "
   "वह रिकॉर्डिंग को प्रयास की बर्बादी नहीं कहता; परंपराओं के लुप्त होने के कारण युवाओं का कस्बों में जाना और पुराने गायकों का न रहना बताता है, अभिलेखागार नहीं; और किसी महाकाव्य को एक ही लिखित पाठ में स्थिर करना उसके मूल बिंदु का उलटा है।",
   "summary",
   opts=["Recordings help, but an oral tradition stays alive only through people who perform it and people who want it.",
         "Recording oral traditions is a waste of effort, because a recording captures only one night's version of an epic.",
         "Oral traditions are fading because archives have recorded them and young people no longer need to learn them.",
         "Every oral epic should be written down in a single fixed text so that no part of it is lost in the future."],
   opts_hi=["रिकॉर्डिंग सहायक हैं, पर मौखिक परंपरा केवल उसे प्रस्तुत करने वालों और उसे चाहने वालों से जीवित रहती है।",
            "मौखिक परंपराओं को रिकॉर्ड करना प्रयास की बर्बादी है, क्योंकि रिकॉर्डिंग किसी महाकाव्य का केवल एक रात का रूप पकड़ती है।",
            "मौखिक परंपराएँ इसलिए लुप्त हो रही हैं कि अभिलेखागारों ने उन्हें रिकॉर्ड कर लिया है और युवाओं को उन्हें सीखने की ज़रूरत नहीं रही।",
            "हर मौखिक महाकाव्य को एक ही स्थिर पाठ में लिख लेना चाहिए ताकि भविष्य में उसका कोई भाग खो न जाए।"],
   ans=0, pos=2)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Only 1 is valid: a singer changes an epic to suit each audience -- shortening it for children, lengthening it on a festival night -- so two performances by the same singer may well differ. "
   "2 is not: the passage says that what keeps a tradition alive is 'not a store of recordings' but people who still sing and listeners who still want to hear them.",
   "केवल 1 वैध है: गायक हर श्रोता-समूह के अनुसार महाकाव्य बदलता है -- बच्चों के लिए छोटा, उत्सव की रात लंबा -- इसलिए एक ही गायक की दो प्रस्तुतियाँ अलग हो सकती हैं। "
   "2 वैध नहीं है: परिच्छेद कहता है कि किसी परंपरा को जीवित रखने वाला 'रिकॉर्डिंग का भंडार नहीं', बल्कि वे लोग हैं जो अब भी गाते हैं और वे श्रोता जो अब भी सुनना चाहते हैं।",
   "conclusions",
   st=["Two performances of the same epic by the same singer may differ from each other.",
       "A complete archive of recordings would be enough to keep an oral tradition alive."],
   st_hi=["एक ही गायक द्वारा एक ही महाकाव्य की दो प्रस्तुतियाँ एक-दूसरे से अलग हो सकती हैं।",
          "रिकॉर्डिंग का एक पूरा संग्रह किसी मौखिक परंपरा को जीवित रखने के लिए पर्याप्त होगा।"],
   key=0)
RQ(p, "Specific Detail", "easy", "mcq",
   "Which one of the following is NOT mentioned in the passage as a way in which a singer changes an epic to suit the audience?",
   "निम्नलिखित में से किसका उल्लेख परिच्छेद में उस तरीक़े के रूप में नहीं है जिससे गायक श्रोताओं के अनुसार महाकाव्य को बदलता है?",
   "The passage lists three ways in which a singer suits an epic to the audience: shortening a tale when children are listening, lengthening it on a festival night, and answering listeners who call out. "
   "Translating it into the language of the listeners is not mentioned.",
   "परिच्छेद तीन तरीक़े गिनाता है जिनसे गायक महाकाव्य को श्रोताओं के अनुसार ढालता है: बच्चों के सुनते समय कथा छोटी करना, उत्सव की रात उसे लंबा करना, और आवाज़ लगाने वाले श्रोताओं को उत्तर देना। "
   "उसे श्रोताओं की भाषा में अनुवाद करने का उल्लेख नहीं है।",
   "detail",
   opts=["Translating it into the language of the listeners",
         "Shortening a tale when children are listening",
         "Lengthening it on the night of a festival",
         "Answering the listeners who call out during the performance"],
   opts_hi=["उसे श्रोताओं की भाषा में अनुवाद करना",
            "बच्चों के सुनते समय कथा को छोटा करना",
            "किसी उत्सव की रात उसे लंबा करना",
            "प्रस्तुति के दौरान आवाज़ लगाने वाले श्रोताओं को उत्तर देना"],
   ans=0, pos=3)

# ------------------------------------------------------------------ P05 the minutes after a heart stops (3)
p = passage("p05",
  "When a person's heart suddenly stops, every minute without help sharply lowers the chance of survival, and an ambulance in a crowded city rarely arrives within the first few minutes. What happens before it arrives therefore decides most outcomes. "
  "A bystander who knows how to press hard and fast on the centre of the chest can keep blood flowing to the brain until trained help comes. "
  "Yet in many places only a small share of the people who collapse in public receive such help, partly because few people have been taught it and partly because those who have are afraid of doing something wrong. "
  "Short, repeated training sessions in schools, offices and housing societies could change this. A skill that many people hold, even imperfectly, saves more lives than one held perfectly by a few.",
  "जब किसी व्यक्ति का हृदय अचानक रुक जाता है, तो बिना सहायता के बीतने वाला हर मिनट बचने की संभावना को तेज़ी से घटाता है, और भीड़भाड़ वाले शहर में एम्बुलेंस शायद ही पहले कुछ मिनटों में पहुँचती है। इसलिए उसके पहुँचने से पहले जो होता है, वही अधिकतर परिणाम तय करता है। "
  "जो पास खड़ा व्यक्ति छाती के बीच ज़ोर से और तेज़ी से दबाना जानता है, वह प्रशिक्षित सहायता आने तक मस्तिष्क तक रक्त का प्रवाह बनाए रख सकता है। "
  "फिर भी कई जगहों पर सार्वजनिक स्थानों पर गिरने वाले लोगों में से केवल थोड़ों को ही ऐसी सहायता मिलती है, कुछ इसलिए कि बहुत कम लोगों को यह सिखाया गया है और कुछ इसलिए कि जिन्हें सिखाया गया है वे कुछ ग़लत कर बैठने से डरते हैं। "
  "विद्यालयों, कार्यालयों और आवासीय सोसाइटियों में छोटे, बार-बार होने वाले प्रशिक्षण सत्र इसे बदल सकते हैं। जो कौशल बहुत से लोगों के पास हो, भले ही अधूरा, वह उस कौशल से अधिक जानें बचाता है जो कुछ लोगों के पास पूर्ण रूप से हो।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage says that the minutes before an ambulance arrives decide most outcomes, that a bystander pressing on the chest can keep blood flowing to the brain, and that short, repeated training for many people would save more lives than perfect skill in a few. "
   "It does not call for more ambulances -- it says that in a crowded city they rarely arrive in the first minutes; it does not say that only doctors and nurses should act, which is the opposite of its point; "
   "and it puts the lack of help down to too little training and fear of doing wrong, not to unwillingness to help strangers.",
   "परिच्छेद कहता है कि एम्बुलेंस आने से पहले के मिनट अधिकतर परिणाम तय करते हैं, कि छाती पर दबाने वाला पास खड़ा व्यक्ति मस्तिष्क तक रक्त का प्रवाह बनाए रख सकता है, और कि बहुत से लोगों का छोटा, बार-बार प्रशिक्षण कुछ लोगों के पूर्ण कौशल से अधिक जानें बचाएगा। "
   "वह अधिक एम्बुलेंस की माँग नहीं करता -- वह कहता है कि भीड़भाड़ वाले शहर में वे शायद ही पहले मिनटों में पहुँचती हैं; वह यह नहीं कहता कि केवल डॉक्टर और नर्स ही कुछ करें, जो उसके मूल बिंदु का उलटा है; "
   "और वह सहायता की कमी का कारण बहुत कम प्रशिक्षण और ग़लती के डर को बताता है, अजनबियों की सहायता न करने की इच्छा को नहीं।",
   "crux",
   opts=["Because the first minutes matter most, teaching many people chest compressions could save many lives.",
         "Cities should buy many more ambulances so that help reaches every person who collapses within a few minutes.",
         "Only trained doctors and nurses should attempt chest compressions, as untrained people may do harm.",
         "Most people who collapse in public die because bystanders are unwilling to help strangers in need."],
   opts_hi=["क्योंकि पहले मिनट सबसे अधिक मायने रखते हैं, बहुत से लोगों को छाती दबाना सिखाने से बहुत-सी जानें बच सकती हैं।",
            "शहरों को बहुत अधिक एम्बुलेंस ख़रीदनी चाहिए ताकि सहायता गिरने वाले हर व्यक्ति तक कुछ ही मिनटों में पहुँचे।",
            "छाती दबाने का प्रयास केवल प्रशिक्षित डॉक्टरों और नर्सों को करना चाहिए, क्योंकि अप्रशिक्षित लोग हानि पहुँचा सकते हैं।",
            "सार्वजनिक स्थानों पर गिरने वाले अधिकतर लोग इसलिए मरते हैं कि पास खड़े लोग ज़रूरतमंद अजनबियों की सहायता नहीं करना चाहते।"],
   ans=0, pos=0)
RQ(p, "Assumption", "hard", "s2", ASSUME, ASSUME_HI,
   "Both are assumed. 1: the passage holds that a skill held by many 'even imperfectly' saves more lives than one held perfectly by a few, which takes for granted that imperfect compressions by a bystander do more good than harm on the whole. "
   "2: the passage names fear of doing something wrong as one reason trained people do not help, and still claims that short, repeated training could change this; that works only if those who are trained would be willing to use the skill.",
   "दोनों पूर्वधारणाएँ हैं। 1: परिच्छेद मानता है कि बहुत से लोगों के पास 'भले ही अधूरा' कौशल, कुछ लोगों के पूर्ण कौशल से अधिक जानें बचाता है, जो यह मानकर चलता है कि पास खड़े व्यक्ति का अधूरा दबाव कुल मिलाकर हानि से अधिक लाभ करता है। "
   "2: परिच्छेद कुछ ग़लत कर बैठने के डर को एक कारण बताता है कि प्रशिक्षित लोग सहायता नहीं करते, और फिर भी दावा करता है कि छोटा, बार-बार प्रशिक्षण इसे बदल सकता है; यह तभी चलता है जब प्रशिक्षित लोग उस कौशल का उपयोग करने को तैयार हों।",
   "assumptions",
   st=["Chest compressions given by a bystander who is not perfectly trained do more good than harm on the whole.",
       "People given short, repeated training would be willing to use it when someone collapses in front of them."],
   st_hi=["जो पास खड़ा व्यक्ति पूरी तरह प्रशिक्षित न हो, उसके द्वारा छाती पर दिया गया दबाव कुल मिलाकर हानि से अधिक लाभ करता है।",
          "जिन लोगों को छोटा, बार-बार प्रशिक्षण मिला हो, वे किसी के सामने गिरने पर उसका उपयोग करने को तैयार होंगे।"],
   key=2)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Only 1 is valid: since the minutes before an ambulance arrives decide most outcomes, and only some bystanders know what to do, whether a person survives depends partly on who happens to be nearby. "
   "2 is not: the passage says that many who have been taught are 'afraid of doing something wrong', which is a reason they do not always help.",
   "केवल 1 वैध है: चूँकि एम्बुलेंस आने से पहले के मिनट अधिकतर परिणाम तय करते हैं, और केवल कुछ ही पास खड़े लोग जानते हैं कि क्या करना है, इसलिए कोई व्यक्ति बचेगा या नहीं यह कुछ हद तक इस पर निर्भर है कि संयोग से पास कौन है। "
   "2 वैध नहीं है: परिच्छेद कहता है कि जिन्हें सिखाया गया है उनमें से बहुत से 'कुछ ग़लत कर बैठने से डरते हैं', जो इसका एक कारण है कि वे हमेशा सहायता नहीं करते।",
   "conclusions",
   st=["Whether a person whose heart stops in public survives depends partly on who happens to be nearby.",
       "Most people who have been trained in chest compressions use the skill whenever someone collapses near them."],
   st_hi=["सार्वजनिक स्थान पर जिस व्यक्ति का हृदय रुक जाए, वह बचेगा या नहीं, यह कुछ हद तक इस पर निर्भर है कि संयोग से पास कौन है।",
          "छाती दबाने का प्रशिक्षण पाए अधिकतर लोग पास में किसी के गिरने पर हर बार उस कौशल का उपयोग करते हैं।"],
   key=0)
