# -*- coding: utf-8 -*-
"""CSAT Level 3 · Test 4 -- Reading Comprehension: 10 original passages, 28 items (8 x 3, 2 x 2).

Level 3 passages carry a turn in the argument -- a claim, then its limit -- so that the items test where the author
stops as much as what the author says. Themes, none used in Level 2 Tests 1-7, Level 1 Minis 1-3 or Level 3 Tests 1-3:
the rebound effect of efficiency, a fence whose purpose is unknown, El Niño and the monsoon, Gresham's law, moral luck,
lakes that switch state, the division of labour and its cost, the ozone treaty and climate change, positive results in
screening for a rare disease, and the rule of law. Item types: main idea 7, best summary 3, inference 11, assumption 3,
tone 1, specific detail 3. Difficulty 2 easy / 17 medium / 9 hard. Options are named by content in every explanation."""
from fractions import Fraction as F
from csat_common import passage, RQ

CRUX = "Which one of the following statements best reflects the crux of the passage?"
CRUX_HI = "निम्नलिखित में से कौन-सा कथन परिच्छेद के सार को सबसे अच्छी तरह व्यक्त करता है?"
MSG = "Which one of the following statements best reflects the most logical and rational message conveyed by the passage?"
MSG_HI = "निम्नलिखित में से कौन-सा कथन परिच्छेद द्वारा दिए गए सबसे तार्किक और विवेकपूर्ण संदेश को सबसे अच्छी तरह व्यक्त करता है?"
VALID = "On the basis of the passage, which of the following conclusions is/are valid?"
VALID_HI = "परिच्छेद के आधार पर निम्नलिखित में से कौन-सा/से निष्कर्ष वैध है/हैं?"
ASSUME = "Which of the following assumptions has/have been made in the passage?"
ASSUME_HI = "परिच्छेद में निम्नलिखित में से कौन-सी पूर्वधारणा/एँ बनाई गई है/हैं?"

# ------------------------------------------------------------------ P01 the rebound effect (3)
p = passage("p01",
  "When engines, lamps or cars become more efficient, it seems obvious that we will use less fuel. Yet in 1865 the economist William Stanley Jevons observed that Britain's use of coal had risen as steam engines grew more economical: cheaper power made it worth using in more places. Economists now call this the rebound effect. "
  "A more efficient air conditioner costs less to run, so a family may cool more rooms for longer; a car that goes further on a litre may be driven more often. Part of the energy saved is spent again. How large the rebound is depends on the case. "
  "Where a need is nearly met -- a family will not keep more food cold just because its refrigerator uses less power -- the rebound is small and most of the saving survives. Where demand responds strongly to price, the rebound can swallow much of the saving and, in rare cases, more than all of it. "
  "Efficiency is therefore worth pursuing, but it cannot be counted on by itself to cut total energy use; that may also need prices or rules that keep the savings from being spent again.",
  "जब इंजन, बत्तियाँ या गाड़ियाँ अधिक दक्ष हो जाती हैं, तो स्पष्ट लगता है कि हम कम ईंधन प्रयोग करेंगे। फिर भी 1865 में अर्थशास्त्री विलियम स्टैनली जेवन्स ने देखा कि भाप-इंजनों के अधिक किफ़ायती होने के साथ ब्रिटेन में कोयले का उपयोग बढ़ा था: सस्ती शक्ति के कारण उसे अधिक जगहों पर लगाना लाभदायक हो गया। अर्थशास्त्री अब इसे पलट-प्रभाव (रिबाउंड प्रभाव) कहते हैं। "
  "अधिक दक्ष एयर-कंडीशनर चलाने में कम ख़र्च होता है, इसलिए कोई परिवार अधिक कमरों को अधिक देर तक ठंडा रख सकता है; जो गाड़ी एक लीटर में अधिक दूर जाती है, वह अधिक बार चलाई जा सकती है। बचाई गई ऊर्जा का एक भाग फिर ख़र्च हो जाता है। पलट-प्रभाव कितना बड़ा है, यह स्थिति पर निर्भर है। "
  "जहाँ कोई आवश्यकता लगभग पूरी हो चुकी है -- कोई परिवार केवल इसलिए अधिक भोजन ठंडा नहीं रखेगा कि उसका रेफ़्रिजरेटर कम बिजली लेता है -- वहाँ पलट-प्रभाव छोटा होता है और अधिकांश बचत बनी रहती है। जहाँ माँग मूल्य के प्रति तीव्र प्रतिक्रिया करती है, वहाँ पलट-प्रभाव बचत का बड़ा भाग निगल सकता है और, विरले मामलों में, पूरी बचत से भी अधिक। "
  "इसलिए दक्षता प्रयास करने योग्य है, पर कुल ऊर्जा उपयोग घटाने के लिए अकेले उस पर भरोसा नहीं किया जा सकता; इसके लिए ऐसे मूल्यों या नियमों की भी आवश्यकता हो सकती है जो बचत को फिर ख़र्च होने से रोकें।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage grants that efficiency saves energy but shows that cheaper use invites more use, so that part of the saving -- small in some cases, large in others -- is spent again; hence efficiency alone cannot be relied on. "
   "It does not call efficiency pointless (it is 'worth pursuing') or say the saving is always used up; Jevons saw coal use rise as engines grew more economical, not less efficient; and higher prices are mentioned only as one possible aid, not as the passage's main point.",
   "परिच्छेद मानता है कि दक्षता ऊर्जा बचाती है, पर दिखाता है कि सस्ता उपयोग अधिक उपयोग को बुलाता है, जिससे बचत का एक भाग -- कहीं छोटा, कहीं बड़ा -- फिर ख़र्च हो जाता है; इसलिए अकेले दक्षता पर भरोसा नहीं किया जा सकता। "
   "वह दक्षता को व्यर्थ नहीं कहता (वह 'प्रयास करने योग्य' है) और न यह कहता है कि बचत हमेशा ख़र्च हो जाती है; जेवन्स ने इंजनों के अधिक किफ़ायती होने के साथ कोयले का उपयोग बढ़ते देखा, कम दक्ष होने के साथ नहीं; और ऊँचे मूल्यों का उल्लेख केवल एक संभावित सहायक के रूप में है, परिच्छेद के मुख्य बिंदु के रूप में नहीं।",
   "crux",
   opts=["Making machines more efficient is pointless, since the energy saved is always used up again in the end.",
         "Jevons showed that Britain used more coal because its steam engines had become less efficient over time.",
         "Efficiency gains are partly spent on extra use, so they cannot alone be relied on to cut energy use.",
         "Governments should raise fuel prices sharply so that families use their air conditioners much less."],
   opts_hi=["मशीनों को अधिक दक्ष बनाना व्यर्थ है, क्योंकि बचाई गई ऊर्जा अंततः हमेशा पूरी की पूरी फिर से ख़र्च हो जाती है।",
            "जेवन्स ने दिखाया कि ब्रिटेन ने अधिक कोयला इसलिए जलाया कि उसके भाप-इंजन समय के साथ कम दक्ष हो गए थे।",
            "दक्षता की बचत का कुछ भाग अधिक उपयोग में चला जाता है, इसलिए ऊर्जा घटाने के लिए अकेले उस पर भरोसा नहीं।",
            "सरकारों को ईंधन के मूल्य तेज़ी से बढ़ाने चाहिए ताकि परिवार अपने एयर-कंडीशनर पहले से बहुत कम चलाएँ।"],
   ans=2, pos=2)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Neither is valid. 1 turns a rare case into a rule: the passage says the rebound can exceed the saving only 'in rare cases', and usually only part of the saving is spent again, so a more efficient car need not raise total fuel use. "
   "2 overstates the other end: where a need is nearly met the rebound is 'small' and 'most of the saving survives' -- which means some energy is saved, not none.",
   "कोई भी वैध नहीं। 1 एक विरले मामले को नियम बना देता है: परिच्छेद कहता है कि पलट-प्रभाव बचत से अधिक केवल 'विरले मामलों में' हो सकता है, और प्रायः बचत का केवल एक भाग फिर ख़र्च होता है, इसलिए अधिक दक्ष गाड़ी से कुल ईंधन उपयोग बढ़ना आवश्यक नहीं। "
   "2 दूसरे छोर को बढ़ा-चढ़ाकर कहता है: जहाँ आवश्यकता लगभग पूरी हो चुकी है, वहाँ पलट-प्रभाव 'छोटा' है और 'अधिकांश बचत बनी रहती है' -- यानी कुछ ऊर्जा बचती है, शून्य नहीं।",
   "conclusions",
   st=["Making a car more fuel-efficient always increases the total amount of fuel used.",
       "Where a need is already nearly met, improving efficiency saves no energy at all."],
   st_hi=["किसी गाड़ी को ईंधन के मामले में अधिक दक्ष बनाने से कुल ईंधन उपयोग हमेशा बढ़ता है।",
          "जहाँ कोई आवश्यकता पहले से लगभग पूरी हो चुकी है, वहाँ दक्षता बढ़ाने से कोई ऊर्जा नहीं बचती।"],
   key=3)
RQ(p, "Specific Detail", "easy", "mcq",
   "According to the passage, why did Britain's use of coal rise as steam engines became more economical?",
   "परिच्छेद के अनुसार, भाप-इंजनों के अधिक किफ़ायती होने के साथ ब्रिटेन में कोयले का उपयोग क्यों बढ़ा?",
   "The passage says that 'cheaper power made it worth using in more places'. It mentions no scarcity of coal, no growth in population and nothing about the fuel an engine needs to start.",
   "परिच्छेद कहता है कि 'सस्ती शक्ति के कारण उसे अधिक जगहों पर लगाना लाभदायक हो गया'। वह न कोयले की कमी का उल्लेख करता है, न जनसंख्या की वृद्धि का, और न इंजन को चालू करने के लिए आवश्यक ईंधन का।",
   "why-coal-use-rose",
   opts=["Cheaper power made it worth using steam engines in more places.",
         "Coal grew scarcer, so more of it had to be burnt to get the same amount of power.",
         "Britain's population grew, and every household needed more coal for heating.",
         "The new engines needed more coal to start, though less to keep them running."],
   opts_hi=["सस्ती शक्ति के कारण भाप-इंजनों को अधिक जगहों पर लगाना लाभदायक हो गया।",
            "कोयला दुर्लभ होता गया, इसलिए उतनी ही शक्ति के लिए उसे अधिक मात्रा में जलाना पड़ा।",
            "ब्रिटेन की जनसंख्या बढ़ी, और हर घर को गर्मी के लिए अधिक कोयले की आवश्यकता हुई।",
            "नए इंजनों को चालू करने में अधिक कोयला लगता था, यद्यपि चलाए रखने में कम।"],
   ans=0, pos=0)

# ------------------------------------------------------------------ P02 a fence whose purpose is unknown (3)
p = passage("p02",
  "The writer G. K. Chesterton told of a reformer who finds a fence built across a road and, seeing no use for it, proposes to pull it down. The wiser course, he suggested, is first to find out why it was put up; once the reason is known, the fence may be removed with a clear conscience. "
  "The point applies to old rules and customs. A practice that looks pointless may be guarding against a danger that has not been seen for years precisely because the practice has kept it away: a rule against building on a dry riverbed looks absurd until the flood that comes once in thirty years. "
  "Yet the advice can be stretched too far. Some fences were built for reasons that no longer hold, and some were never meant to protect anyone but those who built them. Asking why a rule exists is a test it should pass before it is removed, not a reason to keep it for ever. "
  "A reformer who cannot find the reason after honest inquiry may fairly conclude that there is none worth keeping.",
  "लेखक जी. के. चेस्टरटन ने एक सुधारक की बात कही थी जो सड़क के आर-पार बनी एक बाड़ देखता है और, उसका कोई उपयोग न देखकर, उसे गिराने का प्रस्ताव करता है। उन्होंने सुझाया कि अधिक बुद्धिमानी का रास्ता पहले यह पता लगाना है कि वह क्यों लगाई गई थी; कारण ज्ञात हो जाने पर बाड़ को साफ़ अंतःकरण से हटाया जा सकता है। "
  "यह बात पुराने नियमों और रीतियों पर लागू होती है। जो प्रथा निरर्थक दिखती है, वह ऐसे ख़तरे से रक्षा कर रही हो सकती है जो वर्षों से इसीलिए नहीं दिखा कि प्रथा ने उसे दूर रखा: सूखी नदी के तल पर निर्माण के विरुद्ध नियम तब तक बेतुका लगता है जब तक तीस वर्षों में एक बार आने वाली बाढ़ नहीं आती। "
  "फिर भी इस सलाह को बहुत दूर तक खींचा जा सकता है। कुछ बाड़ें ऐसे कारणों से बनी थीं जो अब लागू नहीं होते, और कुछ का उद्देश्य कभी भी उन्हें बनाने वालों के अलावा किसी की रक्षा करना नहीं था। कोई नियम क्यों है, यह पूछना एक परीक्षा है जिसे हटाए जाने से पहले उसे पास करनी चाहिए, उसे हमेशा के लिए बनाए रखने का कारण नहीं। "
  "जो सुधारक ईमानदार जाँच के बाद भी कारण न पा सके, वह उचित ही यह निष्कर्ष निकाल सकता है कि बनाए रखने योग्य कोई कारण नहीं है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage asks that a rule be understood before it is removed, and in the same breath warns that this is 'a test it should pass before it is removed, not a reason to keep it for ever'. The crux holds both halves. "
   "Keeping rules because they are old is exactly what the passage rejects; it does not condemn reformers, only removal without inquiry; and rules that serve only their makers are mentioned as one kind of fence, not singled out for first removal.",
   "परिच्छेद कहता है कि किसी नियम को हटाने से पहले उसे समझा जाए, और साथ ही चेतावनी देता है कि यह 'एक परीक्षा है जिसे हटाए जाने से पहले उसे पास करनी चाहिए, उसे हमेशा के लिए बनाए रखने का कारण नहीं'। सार दोनों हिस्सों को साथ रखता है। "
   "नियमों को पुराना होने के कारण बनाए रखना ठीक वही है जिसे परिच्छेद अस्वीकार करता है; वह सुधारकों की निंदा नहीं करता, केवल बिना जाँच के हटाने की; और केवल बनाने वालों की सेवा करने वाले नियमों का उल्लेख एक प्रकार की बाड़ के रूप में है, सबसे पहले हटाने के लिए चुने जाने के रूप में नहीं।",
   "crux",
   opts=["Old rules and customs should always be kept, since they carry the tested wisdom of past generations.",
         "A rule that seems useless should be understood before removal, but not kept merely for its age.",
         "Reformers usually do more harm than good, since they cannot know why the rules were first made.",
         "Rules that protect only those who made them should be the first to be removed by any reformer."],
   opts_hi=["पुराने नियमों और रीतियों को बनाए रखना चाहिए, क्योंकि उनमें पिछली पीढ़ियों का परखा हुआ ज्ञान है।",
            "जो नियम व्यर्थ लगे उसे हटाने से पहले समझना चाहिए, पर केवल पुराना होने से उसे रखना नहीं चाहिए।",
            "सुधारक प्रायः लाभ से अधिक हानि करते हैं, क्योंकि वे जान नहीं सकते कि नियम पहले क्यों बनाए गए थे।",
            "जो नियम केवल अपने बनाने वालों की रक्षा करते हैं, उन्हें किसी भी सुधारक को सबसे पहले हटाना चाहिए।"],
   ans=1, pos=1)
RQ(p, "Assumption", "medium", "s2", ASSUME, ASSUME_HI,
   "Both are assumed. The advice to find out why a fence was put up, and the remark that a reformer who 'cannot find the reason after honest inquiry' may conclude there is none, take for granted that inquiry can usually find the reason (1). "
   "And the whole caution rests on the expectation that those who made a rule generally had some purpose, even if it is no longer obvious (2); otherwise there would be nothing to look for.",
   "दोनों पूर्वधारणाएँ हैं। यह सलाह कि पता लगाया जाए बाड़ क्यों लगाई गई, और यह टिप्पणी कि जो सुधारक 'ईमानदार जाँच के बाद भी कारण न पा सके' वह मान सकता है कि कोई कारण नहीं है, यह मानकर चलती हैं कि जाँच से प्रायः कारण मिल सकता है (1)। "
   "और पूरी सावधानी इस अपेक्षा पर टिकी है कि नियम बनाने वालों का सामान्यतः कोई उद्देश्य था, भले ही वह अब स्पष्ट न हो (2); अन्यथा खोजने को कुछ होता ही नहीं।",
   "assumptions",
   st=["The reason behind an old rule can usually be found by careful inquiry.",
       "Those who first made a rule generally had some purpose for it, even if it is no longer obvious."],
   st_hi=["किसी पुराने नियम के पीछे का कारण प्रायः सावधानीपूर्ण जाँच से पाया जा सकता है।",
          "जिन्होंने पहले कोई नियम बनाया, उनका सामान्यतः उसके लिए कोई उद्देश्य था, भले ही वह अब स्पष्ट न हो।"],
   key=2)
RQ(p, "Inference", "hard", "mcq",
   "Which one of the following actions is most in keeping with the advice of the passage?",
   "निम्नलिखित में से कौन-सा कार्य परिच्छेद की सलाह के सबसे अधिक अनुरूप है?",
   "The passage asks for the reason to be found first and allows removal once it is known not to hold. An office that checks why a form was introduced, finds the reason has lapsed and then withdraws it does exactly that. "
   "Keeping a ban only because it is a century old treats age as a reason, which the passage rejects; removing a channel because no one can see its purpose is the reformer's mistake that Chesterton warned against; and dropping rules because earlier heads made them involves no inquiry at all.",
   "परिच्छेद कहता है कि पहले कारण खोजा जाए, और यह ज्ञात होने पर कि वह अब लागू नहीं, हटाने की अनुमति देता है। जो कार्यालय जाँचता है कि कोई प्रपत्र क्यों शुरू हुआ, पाता है कि कारण समाप्त हो चुका, और फिर उसे वापस लेता है, वह ठीक यही करता है। "
   "किसी प्रतिबंध को केवल सौ वर्ष पुराना होने के कारण रखना आयु को कारण मानना है, जिसे परिच्छेद अस्वीकार करता है; किसी नाली को इसलिए हटाना कि कोई उसका उद्देश्य नहीं देख पाता, वही सुधारक वाली भूल है जिसके विरुद्ध चेस्टरटन ने चेताया; और नियम इसलिए छोड़ देना कि उन्हें पहले के प्रधानों ने बनाया था, उसमें कोई जाँच ही नहीं है।",
   "an-action-in-keeping-with-the-advice",
   opts=["An office checks why a form was introduced, finds the reason has lapsed, and withdraws it.",
         "A town keeps a ban on night-time loudspeakers simply because it has been in force for a century.",
         "A council fills in an old drainage channel at once because none of its members can see its purpose.",
         "A school drops a set of rules after its head decides that rules made by earlier heads need not bind him."],
   opts_hi=["एक कार्यालय जाँचता है कि कोई प्रपत्र क्यों शुरू हुआ, पाता है कि कारण समाप्त हो चुका, और उसे वापस लेता है।",
            "एक नगर रात में लाउडस्पीकरों पर प्रतिबंध केवल इसलिए बनाए रखता है कि वह सौ वर्षों से लागू है।",
            "एक परिषद एक पुरानी जल-निकासी नाली को तुरंत भर देती है क्योंकि उसका कोई सदस्य उसका उद्देश्य नहीं देख पाता।",
            "एक विद्यालय कुछ नियम छोड़ देता है, जब उसका प्रधान तय करता है कि पहले के प्रधानों के बनाए नियम उस पर लागू नहीं होते।"],
   ans=0, pos=3)

# ------------------------------------------------------------------ P03 El Niño and the monsoon (3)
p = passage("p03",
  "Every few years the surface waters of the central and eastern tropical Pacific grow unusually warm, an event called El Niño. Because it shifts where great currents of warm, moist air rise over the oceans, its effects reach far beyond the Pacific, and India watches for it closely: many of the years in which the summer monsoon failed badly have been El Niño years. "
  "Yet the link is a tendency, not a law. In 1997, during one of the strongest El Niño events of the twentieth century, India's monsoon rainfall was close to normal. Part of the explanation lies in India's own ocean. "
  "When the western Indian Ocean is warmer than its eastern part -- a pattern known as a positive Indian Ocean Dipole -- it can favour monsoon rain and offset the drying pull of El Niño. A forecast that looks at the Pacific alone therefore risks false alarms. "
  "The sounder approach treats El Niño as one weight on the scale, to be read alongside the Indian Ocean and other influences, and states its outlook as a probability rather than a promise.",
  "हर कुछ वर्षों में मध्य और पूर्वी उष्णकटिबंधीय प्रशांत महासागर का सतही जल असामान्य रूप से गर्म हो जाता है, एक घटना जिसे एल नीनो कहते हैं। चूँकि यह बदल देता है कि महासागरों के ऊपर गर्म, नम हवा की विशाल धाराएँ कहाँ उठती हैं, इसके प्रभाव प्रशांत से बहुत दूर तक पहुँचते हैं, और भारत इस पर बारीक़ नज़र रखता है: जिन वर्षों में ग्रीष्म मानसून बुरी तरह विफल हुआ, उनमें से कई एल नीनो वाले वर्ष रहे हैं। "
  "फिर भी यह संबंध एक प्रवृत्ति है, नियम नहीं। 1997 में, बीसवीं सदी की सबसे प्रबल एल नीनो घटनाओं में से एक के दौरान, भारत की मानसूनी वर्षा लगभग सामान्य रही। इसकी व्याख्या का एक भाग भारत के अपने महासागर में है। "
  "जब पश्चिमी हिंद महासागर उसके पूर्वी भाग से अधिक गर्म होता है -- एक पैटर्न जिसे धनात्मक हिंद महासागर द्विध्रुव कहते हैं -- तो वह मानसूनी वर्षा के अनुकूल हो सकता है और एल नीनो के सुखाने वाले खिंचाव को संतुलित कर सकता है। इसलिए जो पूर्वानुमान केवल प्रशांत को देखता है, उसमें झूठी चेतावनियों का जोखिम है। "
  "अधिक ठोस दृष्टिकोण एल नीनो को तराज़ू पर रखे एक बाट की तरह लेता है, जिसे हिंद महासागर और अन्य प्रभावों के साथ पढ़ा जाए, और अपना अनुमान वादे के बजाय संभावना के रूप में व्यक्त करता है।")
RQ(p, "Best Summary", "medium", "mcq", MSG, MSG_HI,
   "The passage keeps El Niño as a real influence -- many bad monsoon years were El Niño years -- but calls the link 'a tendency, not a law' and asks forecasters to weigh it with the Indian Ocean and other factors and to speak in probabilities. "
   "It does not make El Niño the main cause of drought or say forecasts should rest on the Pacific; it does not say El Niño hardly affects the monsoon; and it criticises forecasts that look at one ocean, not forecasting itself.",
   "परिच्छेद एल नीनो को एक वास्तविक प्रभाव मानता है -- मानसून के कई ख़राब वर्ष एल नीनो वाले वर्ष थे -- पर संबंध को 'एक प्रवृत्ति, नियम नहीं' कहता है और पूर्वानुमान लगाने वालों से कहता है कि वे इसे हिंद महासागर और अन्य कारकों के साथ तौलें और संभावनाओं में बात करें। "
   "वह एल नीनो को सूखे का मुख्य कारण नहीं बनाता और न यह कहता है कि पूर्वानुमान प्रशांत पर टिके हों; वह यह नहीं कहता कि एल नीनो का मानसून पर लगभग कोई प्रभाव नहीं; और वह केवल एक महासागर को देखने वाले पूर्वानुमानों की आलोचना करता है, पूर्वानुमान की नहीं।",
   "message",
   opts=["El Niño is the main cause of drought in India, so monsoon forecasts should be based on the Pacific.",
         "The Indian Ocean matters more to India than the Pacific, and El Niño hardly affects its monsoon.",
         "Since the monsoon can never be forecast with certainty, forecasts tend to do more harm than good.",
         "El Niño raises the risk of a weak monsoon, but forecasts must weigh it with other factors."],
   opts_hi=["एल नीनो भारत में सूखे का मुख्य कारण है, इसलिए मानसून के पूर्वानुमान प्रशांत पर आधारित होने चाहिए।",
            "भारत के लिए हिंद महासागर प्रशांत से अधिक महत्त्वपूर्ण है, और एल नीनो उसके मानसून पर लगभग असर नहीं डालता।",
            "चूँकि मानसून का पूर्वानुमान कभी निश्चित नहीं हो सकता, इसलिए पूर्वानुमान लाभ से अधिक हानि करते हैं।",
            "एल नीनो कमज़ोर मानसून का जोखिम बढ़ाता है, पर पूर्वानुमानों को उसे अन्य कारकों के साथ तौलना चाहिए।"],
   ans=3, pos=3)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Only 2 is valid. The passage treats El Niño as raising the chance of a weak monsoon while asking for outlooks stated as 'a probability rather than a promise', so a forecaster may give a below-normal season a higher chance without ruling out a normal one. "
   "1 turns the Indian Ocean Dipole into the only escape. The passage calls it 'part of the explanation' and also names 'other influences', so a monsoon in an El Niño year is not bound to fail whenever the dipole is not positive.",
   "केवल 2 वैध है। परिच्छेद एल नीनो को कमज़ोर मानसून की संभावना बढ़ाने वाला मानता है और चाहता है कि अनुमान 'वादे के बजाय संभावना' के रूप में दिए जाएँ, इसलिए पूर्वानुमानकर्ता सामान्य मौसम को नकारे बिना सामान्य से कम वर्षा वाले मौसम को अधिक संभावना दे सकता है। "
   "1 हिंद महासागर द्विध्रुव को एकमात्र बचाव बना देता है। परिच्छेद उसे 'व्याख्या का एक भाग' कहता है और 'अन्य प्रभावों' का भी उल्लेख करता है, इसलिए एल नीनो वाले वर्ष में द्विध्रुव धनात्मक न होने पर मानसून का विफल होना निश्चित नहीं।",
   "conclusions",
   st=["In any year in which El Niño develops, India's monsoon will be below normal unless the Indian Ocean Dipole is positive.",
       "A monsoon outlook issued in an El Niño year may reasonably give a below-normal season a higher chance without ruling out a normal one."],
   st_hi=["जिस भी वर्ष एल नीनो विकसित होता है, उसमें भारत का मानसून सामान्य से कम रहेगा, जब तक कि हिंद महासागर द्विध्रुव धनात्मक न हो।",
          "एल नीनो वाले वर्ष में जारी मानसूनी अनुमान सामान्य मौसम को नकारे बिना सामान्य से कम वर्षा वाले मौसम को उचित रूप से अधिक संभावना दे सकता है।"],
   key=1)
RQ(p, "Specific Detail", "medium", "mcq",
   "According to the passage, what is a positive Indian Ocean Dipole?",
   "परिच्छेद के अनुसार, धनात्मक हिंद महासागर द्विध्रुव क्या है?",
   "The passage defines it as the pattern in which 'the western Indian Ocean is warmer than its eastern part'. The warming of the central and eastern tropical Pacific is El Niño; the dipole is said to favour monsoon rain, not to weaken rainfall; and nothing in the passage says it always brings drought.",
   "परिच्छेद इसे उस पैटर्न के रूप में परिभाषित करता है जिसमें 'पश्चिमी हिंद महासागर उसके पूर्वी भाग से अधिक गर्म होता है'। मध्य और पूर्वी उष्णकटिबंधीय प्रशांत का गर्म होना एल नीनो है; द्विध्रुव को मानसूनी वर्षा के अनुकूल बताया गया है, वर्षा घटाने वाला नहीं; और परिच्छेद में कहीं नहीं कहा गया कि वह हमेशा सूखा लाता है।",
   "what-a-positive-dipole-is",
   opts=["A pattern in which the western Indian Ocean is warmer than its eastern part",
         "A warming of the surface waters of the central and eastern tropical Pacific",
         "A shift in the rising currents of air that weakens rainfall over the Indian Ocean",
         "A cooling of the eastern Indian Ocean that always brings drought to the Indian subcontinent"],
   opts_hi=["एक पैटर्न जिसमें पश्चिमी हिंद महासागर उसके पूर्वी भाग से अधिक गर्म होता है",
            "मध्य और पूर्वी उष्णकटिबंधीय प्रशांत महासागर के सतही जल का गर्म होना",
            "उठती हवा की धाराओं में ऐसा बदलाव जो हिंद महासागर के ऊपर वर्षा को कमज़ोर कर देता है",
            "पूर्वी हिंद महासागर का ठंडा होना, जो भारतीय उपमहाद्वीप में हमेशा सूखा लाता है"],
   ans=0, pos=0)

# ------------------------------------------------------------------ P04 Gresham's law (2)
p = passage("p04",
  "'Bad money drives out good' is known as Gresham's law, after an English financier of the sixteenth century, though the idea is far older. Suppose two coins pass at the same face value, but one contains more silver than the other. "
  "Anyone who has both will spend the light coin and keep the heavy one -- or melt it down, or send it abroad, where it is valued by its weight. Soon only the light coins are seen in the market. "
  "The law, however, holds only under a condition that is easy to miss: the two coins must be forced to pass at the same value, usually by a law that makes both acceptable for every payment. Where sellers are free to refuse poor coins, or to ask for more of them, the good coin commands a premium and people prefer to be paid in it. "
  "In those conditions it is the bad money that drops out of use. Gresham's law is thus less a law of human nature than a consequence of a fixed rate set by authority.",
  "'बुरी मुद्रा अच्छी मुद्रा को बाहर कर देती है' -- इसे ग्रेशम का नियम कहा जाता है, सोलहवीं सदी के एक अंग्रेज़ वित्तदाता के नाम पर, यद्यपि यह विचार कहीं पुराना है। मान लीजिए दो सिक्के एक ही अंकित मूल्य पर चलते हैं, पर एक में दूसरे से अधिक चाँदी है। "
  "जिसके पास दोनों हैं, वह हल्का सिक्का ख़र्च करेगा और भारी सिक्का रख लेगा -- या उसे गला देगा, या विदेश भेज देगा, जहाँ उसका मूल्य उसके भार से आँका जाता है। जल्दी ही बाज़ार में केवल हल्के सिक्के दिखते हैं। "
  "पर यह नियम केवल एक ऐसी शर्त पर लागू होता है जो आसानी से छूट जाती है: दोनों सिक्कों को एक ही मूल्य पर चलने के लिए बाध्य किया गया हो, प्रायः ऐसे क़ानून द्वारा जो दोनों को हर भुगतान के लिए स्वीकार्य बनाता है। जहाँ विक्रेता घटिया सिक्कों को अस्वीकार करने, या उनकी अधिक संख्या माँगने के लिए स्वतंत्र हैं, वहाँ अच्छे सिक्के का मूल्य अधिक लगता है और लोग उसी में भुगतान पाना पसंद करते हैं। "
  "उन परिस्थितियों में बुरी मुद्रा ही उपयोग से बाहर हो जाती है। इस प्रकार ग्रेशम का नियम मानव स्वभाव का नियम कम और सत्ता द्वारा तय एक स्थिर दर का परिणाम अधिक है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage explains the familiar law and then fixes its limit: bad money drives out good only when both must pass at the same value; where people may refuse or discount poor coins, the bad money is the one that disappears. "
   "A general preference for heavier coins is only part of the mechanism; banning debased coins is never proposed, and the passage denies that they 'always' drive good coins out; and it says the idea is 'far older' than Gresham.",
   "परिच्छेद जाने-माने नियम को समझाता है और फिर उसकी सीमा तय करता है: बुरी मुद्रा अच्छी को तभी बाहर करती है जब दोनों को एक ही मूल्य पर चलना हो; जहाँ लोग घटिया सिक्कों को अस्वीकार कर सकें या उन्हें कम आँक सकें, वहाँ बुरी मुद्रा ही ग़ायब होती है। "
   "भारी सिक्कों के प्रति सामान्य झुकाव इस प्रक्रिया का केवल एक भाग है; घटिया सिक्कों पर प्रतिबंध का कहीं प्रस्ताव नहीं, और परिच्छेद इससे इनकार करता है कि वे 'हमेशा' अच्छे सिक्कों को बाहर करते हैं; और वह कहता है कि यह विचार ग्रेशम से 'कहीं पुराना' है।",
   "crux",
   opts=["People always prefer to hold their wealth in coins that contain more of a precious metal.",
         "Debased coins should be banned, since they always drive good coins out of circulation.",
         "Bad money displaces good only when both are forced to pass at the same fixed value.",
         "Gresham was the first to notice that coins of the same face value may differ in their metal."],
   opts_hi=["लोग हमेशा अपना धन ऐसे सिक्कों में रखना पसंद करते हैं जिनमें बहुमूल्य धातु अधिक हो।",
            "घटिया सिक्कों पर प्रतिबंध लगना चाहिए, क्योंकि वे हमेशा अच्छे सिक्कों को चलन से बाहर कर देते हैं।",
            "बुरी मुद्रा अच्छी को तभी हटाती है जब दोनों को एक ही स्थिर मूल्य पर चलने के लिए बाध्य किया जाए।",
            "ग्रेशम ने ही सबसे पहले देखा कि एक ही अंकित मूल्य के सिक्कों की धातु में अंतर हो सकता है।"],
   ans=2, pos=2)
RQ(p, "Inference", "hard", "mcq",
   "In which one of the following situations would the passage expect the heavy coins to stay in use while the light coins drop out?",
   "परिच्छेद के अनुसार, निम्नलिखित में से किस स्थिति में भारी सिक्के उपयोग में बने रहेंगे जबकि हल्के सिक्के बाहर हो जाएँगे?",
   "Good money survives where sellers are free to refuse poor coins or to ask for more of them: then the heavy coin commands a premium, people want to be paid in it, and the light coin falls out of use. "
   "A law making both coins acceptable at one value, with penalties for refusing either, is exactly the condition under which bad money drives out good; minting more light coins at the same face value only strengthens that; and a light coin of cheaper metal at a fixed value would still be the one people spend.",
   "अच्छी मुद्रा वहाँ बची रहती है जहाँ विक्रेता घटिया सिक्कों को अस्वीकार करने या उनकी अधिक संख्या माँगने के लिए स्वतंत्र हों: तब भारी सिक्के का मूल्य अधिक लगता है, लोग उसी में भुगतान चाहते हैं, और हल्का सिक्का उपयोग से बाहर हो जाता है। "
   "दोनों सिक्कों को एक मूल्य पर स्वीकार्य बनाने वाला क़ानून, किसी को भी अस्वीकार करने पर दंड के साथ, ठीक वही शर्त है जिसमें बुरी मुद्रा अच्छी को बाहर करती है; एक ही अंकित मूल्य पर अधिक हल्के सिक्के ढालना इसे और मज़बूत करता है; और स्थिर मूल्य पर सस्ती धातु का हल्का सिक्का फिर भी वही होगा जिसे लोग ख़र्च करेंगे।",
   "where-good-coins-survive",
   opts=["The government makes both coins legal for every payment at the same value and punishes anyone who refuses either.",
         "Traders are free to take coins by weight, and many ask for more light coins than heavy ones for the same goods.",
         "The mint issues far more light coins than heavy ones, while the law fixes the same face value for both.",
         "The light coins are made of a cheaper metal than silver, though the law sets the same value for both kinds."],
   opts_hi=["सरकार दोनों सिक्कों को एक ही मूल्य पर हर भुगतान के लिए वैध बनाती है और किसी को भी अस्वीकार करने वाले को दंड देती है।",
            "व्यापारी सिक्कों को भार से लेने को स्वतंत्र हैं, और कई उसी माल के लिए भारी की तुलना में अधिक हल्के सिक्के माँगते हैं।",
            "टकसाल भारी की तुलना में कहीं अधिक हल्के सिक्के जारी करती है, जबकि क़ानून दोनों सिक्कों का एक ही अंकित मूल्य तय करता है।",
            "हल्के सिक्के चाँदी से सस्ती धातु के बने हैं, यद्यपि क़ानून दोनों प्रकार के सिक्कों का एक ही मूल्य तय करता है।"],
   ans=1, pos=1)

# ------------------------------------------------------------------ P05 moral luck (3)
p = passage("p05",
  "Two drivers set out after an evening of drinking, equally careless and equally over the limit. One reaches home without incident; on the other's route a child runs into the road and is killed. Most of us judge the second driver far more harshly, and the law punishes him far more severely. "
  "Yet the two did exactly the same thing; the difference between them lay in circumstances that neither controlled. Philosophers call this moral luck, and it is puzzling, because we also hold that people should be judged only for what is in their control. "
  "The puzzle does not mean that outcomes should be ignored. Outcomes matter to victims, to compensation and to how much a person has to answer for, and a legal system that punished intentions alone would have to read minds. "
  "But it does suggest that the first driver should not mistake his luck for innocence. The blame he escaped was not something he earned; he took the same gamble with other people's lives, and it happened to come off.",
  "दो चालक शाम को शराब पीने के बाद निकलते हैं, दोनों बराबर लापरवाह और दोनों सीमा से बराबर ऊपर। एक बिना किसी घटना के घर पहुँच जाता है; दूसरे के रास्ते में एक बच्चा सड़क पर दौड़ आता है और मारा जाता है। हममें से अधिकांश दूसरे चालक को कहीं अधिक कठोरता से आँकते हैं, और क़ानून उसे कहीं अधिक कड़ा दंड देता है। "
  "फिर भी दोनों ने ठीक एक-सा काम किया; उनके बीच का अंतर ऐसी परिस्थितियों में था जिन पर किसी का नियंत्रण नहीं था। दार्शनिक इसे नैतिक भाग्य कहते हैं, और यह उलझन में डालता है, क्योंकि हम यह भी मानते हैं कि लोगों को केवल उसी के लिए आँका जाना चाहिए जो उनके नियंत्रण में है। "
  "इस उलझन का अर्थ यह नहीं कि परिणामों की अनदेखी की जाए। परिणाम पीड़ितों के लिए, क्षतिपूर्ति के लिए और इसके लिए मायने रखते हैं कि किसी व्यक्ति को कितना उत्तर देना है, और जो विधि-व्यवस्था केवल इरादों को दंडित करे उसे मन पढ़ने पड़ेंगे। "
  "पर इससे यह संकेत अवश्य मिलता है कि पहले चालक को अपने भाग्य को अपनी निर्दोषता नहीं समझ लेना चाहिए। जिस दोष से वह बचा, वह उसने कमाया नहीं था; उसने भी दूसरों के जीवन के साथ वही जुआ खेला, और वह संयोग से सफल हो गया।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage holds that the lucky driver did the same wrong as the unlucky one, so luck in the outcome does not reduce his blame, while still granting that outcomes matter for victims, compensation and the law. "
   "It does not ask the law to punish the two equally -- it defends the law's attention to outcomes; it does not endorse the harsher judgement of the second driver as fully right; and it rejects judging intentions alone as unworkable.",
   "परिच्छेद मानता है कि भाग्यशाली चालक ने वही ग़लती की जो अभागे ने, इसलिए परिणाम का भाग्य उसका दोष कम नहीं करता, फिर भी यह स्वीकार करता है कि परिणाम पीड़ितों, क्षतिपूर्ति और क़ानून के लिए मायने रखते हैं। "
   "वह क़ानून से दोनों को बराबर दंड देने को नहीं कहता -- वह परिणामों पर क़ानून के ध्यान का बचाव करता है; वह दूसरे चालक के कठोर आकलन को पूरी तरह सही नहीं ठहराता; और केवल इरादों को आँकने को अव्यावहारिक मानकर अस्वीकार करता है।",
   "crux",
   opts=["Escaping harm by luck does not make a careless act less blameworthy, though outcomes still matter.",
         "The law should punish the two drivers equally, since they did exactly the same thing on the road that night.",
         "We are right to judge the driver who killed a child far more harshly than the driver who reached home safely.",
         "People can fairly be blamed only for their intentions, since the outcomes of their acts are beyond their control."],
   opts_hi=["संयोग से हानि टल जाने पर लापरवाह कार्य कम दोषपूर्ण नहीं हो जाता, यद्यपि परिणाम फिर भी मायने रखते हैं।",
            "क़ानून को दोनों चालकों को बराबर दंड देना चाहिए, क्योंकि उस रात सड़क पर दोनों ने ठीक एक-सा काम किया।",
            "बच्चे को मारने वाले चालक को सुरक्षित घर पहुँचे चालक की तुलना में कहीं अधिक कठोरता से आँकना हमारा सही है।",
            "लोगों को उचित रूप से केवल उनके इरादों के लिए दोष दिया जा सकता है, क्योंकि उनके कार्यों के परिणाम उनके नियंत्रण से बाहर हैं।"],
   ans=0, pos=0)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Both are valid. The passage says the two drivers 'did exactly the same thing' and that the first took 'the same gamble', so on its view he acted as wrongly as the second (1). "
   "It also says that a legal system punishing intentions alone 'would have to read minds', which is to say it would be unworkable in practice (2).",
   "दोनों वैध हैं। परिच्छेद कहता है कि दोनों चालकों ने 'ठीक एक-सा काम किया' और पहले ने 'वही जुआ' खेला, इसलिए उसके मत में पहले ने भी उतना ही ग़लत किया जितना दूसरे ने (1)। "
   "वह यह भी कहता है कि केवल इरादों को दंडित करने वाली विधि-व्यवस्था को 'मन पढ़ने पड़ेंगे', यानी वह व्यवहार में चल नहीं सकती (2)।",
   "conclusions",
   st=["On the passage's view, the driver who reached home safely acted as wrongly as the one whose car killed the child.",
       "The passage suggests that a legal system punishing intentions alone would be unworkable in practice."],
   st_hi=["परिच्छेद के मत में, सुरक्षित घर पहुँचे चालक ने उतना ही ग़लत किया जितना उस चालक ने जिसकी गाड़ी से बच्चा मारा गया।",
          "परिच्छेद संकेत देता है कि केवल इरादों को दंडित करने वाली विधि-व्यवस्था व्यवहार में चल नहीं सकती।"],
   key=2)
RQ(p, "Author's Tone", "hard", "mcq",
   "The author's attitude towards the first driver, who reached home safely, is best described as:",
   "सुरक्षित घर पहुँचे पहले चालक के प्रति लेखक का दृष्टिकोण सबसे अच्छी तरह इस प्रकार वर्णित है:",
   "The author says the first driver 'should not mistake his luck for innocence', that the blame he escaped 'was not something he earned', and that he 'took the same gamble with other people's lives'. That is criticism. "
   "Nothing in the passage admires him for getting home; the circumstances 'neither controlled' are the child's appearance on the road, not his decision to drive drunk, so they give no ground for sympathy with him; and the passage is not neutral, since it calls both drivers careless.",
   "लेखक कहता है कि पहले चालक को 'अपने भाग्य को अपनी निर्दोषता नहीं समझ लेना चाहिए', कि जिस दोष से वह बचा 'वह उसने कमाया नहीं था', और कि उसने 'दूसरों के जीवन के साथ वही जुआ खेला'। यह आलोचना है। "
   "परिच्छेद में घर पहुँचने के लिए उसकी कोई प्रशंसा नहीं; जिन परिस्थितियों पर 'किसी का नियंत्रण नहीं था' वे बच्चे का सड़क पर आना हैं, शराब पीकर गाड़ी चलाने का उसका निर्णय नहीं, इसलिए वे उसके प्रति सहानुभूति का आधार नहीं देतीं; और परिच्छेद तटस्थ नहीं है, क्योंकि वह दोनों चालकों को लापरवाह कहता है।",
   "attitude-to-the-lucky-driver",
   opts=["Critical: his escape from blame was luck, not innocence.",
         "Admiring: he reached home without harming anyone on the way.",
         "Sympathetic: he had no control over what happened on his route.",
         "Neutral: the passage does not judge the conduct of either driver."],
   opts_hi=["आलोचनात्मक: दोष से उसका बचना भाग्य था, निर्दोषता नहीं।",
            "प्रशंसात्मक: वह रास्ते में किसी को हानि पहुँचाए बिना घर पहुँच गया।",
            "सहानुभूतिपूर्ण: उसके रास्ते में जो हुआ उस पर उसका कोई नियंत्रण नहीं था।",
            "तटस्थ: परिच्छेद किसी भी चालक के आचरण पर कोई निर्णय नहीं देता।"],
   ans=0, pos=1)

# ------------------------------------------------------------------ P06 lakes that switch state (3)
p = passage("p06",
  "A shallow lake can stay clear for years while nutrients from farm fertiliser and sewage seep into it. Rooted plants on its bed hold the mud in place and take up nutrients, keeping the floating algae in check. Then, often within a single season, the lake turns green and murky. "
  "Nothing dramatic happened that year; the load had simply crossed a threshold. Once the water is turbid, the algae shade out the rooted plants, and without plants the wind stirs up the mud, which keeps the water cloudy. The new state maintains itself. "
  "This has an awkward consequence for anyone trying to restore the lake. Cutting the nutrient load back to the level at which the lake was last clear is often not enough; it may have to be cut much further before the water clears again, and even then managers sometimes have to help, for example by replanting the bed. "
  "A lake, in other words, does not always retrace its path. Early action is far cheaper than repair, but the warning signs before the switch are easy to miss.",
  "एक उथली झील वर्षों तक साफ़ रह सकती है, जबकि खेतों के उर्वरक और सीवेज से पोषक तत्व उसमें रिसते रहते हैं। उसके तल पर जड़ वाले पौधे कीचड़ को थामे रखते हैं और पोषक तत्व सोख लेते हैं, जिससे तैरते शैवाल नियंत्रण में रहते हैं। फिर, प्रायः एक ही मौसम के भीतर, झील हरी और गंदली हो जाती है। "
  "उस वर्ष कुछ नाटकीय नहीं हुआ; भार बस एक दहलीज़ पार कर गया था। एक बार पानी गंदला हो जाए, तो शैवाल जड़ वाले पौधों तक रोशनी नहीं पहुँचने देते, और पौधों के बिना हवा कीचड़ को उछाल देती है, जो पानी को धुँधला बनाए रखता है। नई अवस्था स्वयं को बनाए रखती है। "
  "झील को फिर से ठीक करने का प्रयास करने वाले के लिए इसका एक कठिन परिणाम है। पोषक भार को उस स्तर तक घटाना, जिस पर झील अंतिम बार साफ़ थी, प्रायः पर्याप्त नहीं होता; पानी फिर साफ़ होने से पहले उसे कहीं अधिक घटाना पड़ सकता है, और तब भी प्रबंधकों को कभी-कभी सहायता करनी पड़ती है, जैसे तल पर फिर से पौधे लगाकर। "
  "दूसरे शब्दों में, झील हमेशा अपने रास्ते पर वापस नहीं लौटती। जल्दी क़दम उठाना मरम्मत से कहीं सस्ता है, पर बदलाव से पहले के चेतावनी-संकेत आसानी से छूट जाते हैं।")
RQ(p, "Best Summary", "medium", "mcq", MSG, MSG_HI,
   "The passage describes a sudden switch to a murky state that sustains itself and is hard to reverse, and ends by saying that early action is far cheaper than repair. "
   "It does not call for removing algae wherever they appear; it says cutting the load back is 'often not enough', so restoration is not automatic; and the wind only helps keep an already murky lake cloudy -- it is not named as the chief cause of damage.",
   "परिच्छेद एक ऐसी गंदली अवस्था में अचानक बदलाव का वर्णन करता है जो स्वयं को बनाए रखती है और जिसे पलटना कठिन है, और अंत में कहता है कि जल्दी क़दम उठाना मरम्मत से कहीं सस्ता है। "
   "वह जहाँ भी शैवाल दिखें उन्हें हटाने की माँग नहीं करता; वह कहता है कि भार वापस घटाना 'प्रायः पर्याप्त नहीं', इसलिए सुधार अपने आप नहीं होता; और हवा केवल पहले से गंदली झील को धुँधला बनाए रखने में सहायक है -- उसे क्षति का मुख्य कारण नहीं बताया गया।",
   "message",
   opts=["Algae are the main threat to lakes and should be removed from the water wherever they appear.",
         "Lakes can switch suddenly to a murky state that sustains itself, so prevention beats repair.",
         "Cutting the nutrient load always returns a polluted lake to the clear state it was once in.",
         "Shallow lakes are damaged chiefly by the wind, which stirs up the mud lying on their beds."],
   opts_hi=["शैवाल झीलों के लिए मुख्य ख़तरा हैं और जहाँ भी दिखें उन्हें तुरंत ही पानी से हटा देना चाहिए।",
            "झीलें अचानक ऐसी गंदली अवस्था में जा सकती हैं जो स्वयं टिकी रहे, इसलिए बचाव मरम्मत से बेहतर है।",
            "पोषक भार घटाने से प्रदूषित झील हमेशा उसी साफ़ अवस्था में लौट आती है जिसमें वह पहले कभी थी।",
            "उथली झीलों को मुख्यतः हवा क्षति पहुँचाती है, जो उनके तल पर पड़े कीचड़ को बार-बार उछाल देती है।"],
   ans=1, pos=1)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Only 1 is valid. Because a turbid lake stays turbid even when the load falls back to a level at which it was once clear, the state of a lake depends on its history as well as on today's load; two lakes with the same load can therefore be one clear and one murky. "
   "2 contradicts the passage, which says 'nothing dramatic happened that year': the load had been building slowly and simply crossed a threshold.",
   "केवल 1 वैध है। चूँकि गंदली झील तब भी गंदली रहती है जब भार उस स्तर तक लौट आए जिस पर वह कभी साफ़ थी, झील की अवस्था आज के भार के साथ-साथ उसके इतिहास पर भी निर्भर है; इसलिए एक ही भार वाली दो झीलों में एक साफ़ और एक गंदली हो सकती है। "
   "2 परिच्छेद का खंडन करता है, जो कहता है कि 'उस वर्ष कुछ नाटकीय नहीं हुआ': भार धीरे-धीरे बढ़ रहा था और बस एक दहलीज़ पार कर गया।",
   "conclusions",
   st=["Two lakes receiving the same nutrient load today could be in different states, one clear and the other murky.",
       "A lake that turned murky within a single season must have received an unusually large load of nutrients that year."],
   st_hi=["आज एक ही पोषक भार पाने वाली दो झीलें अलग-अलग अवस्थाओं में हो सकती हैं, एक साफ़ और दूसरी गंदली।",
          "जो झील एक ही मौसम के भीतर गंदली हो गई, उसने उस वर्ष अवश्य ही पोषक तत्वों का असामान्य रूप से बड़ा भार पाया होगा।"],
   key=0)
RQ(p, "Specific Detail", "easy", "mcq",
   "According to the passage, how do rooted plants help to keep a shallow lake clear?",
   "परिच्छेद के अनुसार, जड़ वाले पौधे उथली झील को साफ़ रखने में कैसे सहायता करते हैं?",
   "The passage says the plants 'hold the mud in place and take up nutrients, keeping the floating algae in check'. It says nothing of chemicals or of slowing the wind, and the shading it describes runs the other way: in a murky lake the algae shade out the plants.",
   "परिच्छेद कहता है कि पौधे 'कीचड़ को थामे रखते हैं और पोषक तत्व सोख लेते हैं, जिससे तैरते शैवाल नियंत्रण में रहते हैं'। वह न रसायनों की बात करता है, न हवा को धीमा करने की, और जिस छाया का वह वर्णन करता है वह उलटी दिशा में है: गंदली झील में शैवाल पौधों तक रोशनी नहीं पहुँचने देते।",
   "how-plants-keep-a-lake-clear",
   opts=["By holding the mud in place and taking up nutrients",
         "By releasing chemicals that kill the floating algae",
         "By shading the water so that the algae cannot grow",
         "By slowing the wind that blows across the water"],
   opts_hi=["कीचड़ को थामे रखकर और पोषक तत्व सोखकर",
            "ऐसे रसायन छोड़कर जो तैरते शैवाल को मार देते हैं",
            "पानी पर छाया करके ताकि शैवाल उग न सकें",
            "पानी के ऊपर बहने वाली हवा को धीमा करके"],
   ans=0, pos=3)

# ------------------------------------------------------------------ P07 the division of labour and its cost (3)
p = passage("p07",
  "Adam Smith opened The Wealth of Nations, in 1776, with a pin factory. A worker making pins alone, he wrote, could not make even twenty in a day; ten workers who divided the task into separate operations -- one drawing out the wire, another cutting it, another sharpening the point -- could make upwards of forty-eight thousand. "
  "Dividing labour made each worker more practised, saved the time lost in passing from one task to another, and made it easier to invent machines for simple, repeated motions. "
  "Less often remembered is that Smith returned to the subject later in the same book with a warning. A person who spends a whole working life repeating a few simple operations, he argued, has little occasion to use his judgement and risks losing the habit of thinking. "
  "Smith's remedy was not to abandon the division of labour, whose gains he never doubted, but to give the children of working people a basic schooling paid for partly by the public. The efficiency of a task, in his view, did not settle the question of what that task did to the person doing it.",
  "एडम स्मिथ ने 1776 में 'द वेल्थ ऑफ़ नेशन्स' की शुरुआत एक पिन कारख़ाने से की। उन्होंने लिखा कि अकेले पिन बनाने वाला कामगार एक दिन में बीस भी नहीं बना सकता; दस कामगार, जिन्होंने काम को अलग-अलग क्रियाओं में बाँट लिया -- एक तार खींचता, दूसरा उसे काटता, तीसरा नोक पैनी करता -- अड़तालीस हज़ार से भी अधिक बना सकते थे। "
  "श्रम-विभाजन ने हर कामगार को अधिक अभ्यस्त बनाया, एक काम से दूसरे पर जाने में खोने वाला समय बचाया, और सरल, दोहराई जाने वाली गतियों के लिए मशीनें ईजाद करना आसान बनाया। "
  "कम याद रखा जाता है कि स्मिथ उसी पुस्तक में आगे इस विषय पर एक चेतावनी के साथ लौटे। उन्होंने तर्क दिया कि जो व्यक्ति पूरा कामकाजी जीवन कुछ सरल क्रियाएँ दोहराने में बिताता है, उसे अपने विवेक का प्रयोग करने का कम अवसर मिलता है और उसके सोचने की आदत खो बैठने का जोखिम रहता है। "
  "स्मिथ का उपाय श्रम-विभाजन को छोड़ना नहीं था, जिसके लाभों पर उन्होंने कभी संदेह नहीं किया, बल्कि कामकाजी लोगों के बच्चों को ऐसी बुनियादी शिक्षा देना था जिसका ख़र्च आंशिक रूप से जनता उठाए। उनके विचार में किसी काम की दक्षता से यह प्रश्न तय नहीं हो जाता था कि वह काम करने वाले व्यक्ति पर क्या असर डालता है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage pairs Smith's praise of the division of labour with his later warning about its effect on workers' minds and his remedy of schooling. The crux keeps both. "
   "Smith did not want the division of labour limited -- his remedy was 'not to abandon' it; the pin factory credits divided work, with machines as one of its results, not as the true source of wealth; and the passage says he 'never doubted' the gains.",
   "परिच्छेद श्रम-विभाजन की स्मिथ की प्रशंसा को कामगारों के मन पर उसके प्रभाव के बारे में उनकी बाद की चेतावनी और शिक्षा के उनके उपाय के साथ रखता है। सार दोनों को साथ रखता है। "
   "स्मिथ श्रम-विभाजन को सीमित नहीं करना चाहते थे -- उनका उपाय उसे 'छोड़ना नहीं' था; पिन कारख़ाना बँटे हुए काम को श्रेय देता है, मशीनों को उसके एक परिणाम के रूप में, धन के वास्तविक स्रोत के रूप में नहीं; और परिच्छेद कहता है कि उन्होंने लाभों पर 'कभी संदेह नहीं किया'।",
   "crux",
   opts=["The division of labour does more harm than good and should be limited wherever it can be.",
         "The pin factory shows that machines, rather than workers, are the true source of a nation's wealth.",
         "Smith's warning shows that he came in the end to doubt the gains from dividing labour among workers.",
         "Smith valued dividing labour but saw its cost to workers' minds and proposed a remedy for it."],
   opts_hi=["श्रम-विभाजन लाभ से अधिक हानि करता है और जहाँ भी संभव हो उसे सीमित करना चाहिए।",
            "पिन कारख़ाना दिखाता है कि कामगार नहीं, बल्कि मशीनें किसी राष्ट्र के धन का वास्तविक स्रोत हैं।",
            "स्मिथ की चेतावनी दिखाती है कि अंत में उन्हें कामगारों में श्रम बाँटने के लाभों पर संदेह हो गया था।",
            "स्मिथ श्रम-विभाजन को महत्त्व देते थे, पर कामगारों के मन पर उसकी क़ीमत देखकर उन्होंने उपाय सुझाया।"],
   ans=3, pos=3)
RQ(p, "Assumption", "medium", "s2", ASSUME, ASSUME_HI,
   "Only 2 is assumed. Smith's remedy for minds dulled by repetitive work is schooling in childhood, which makes sense only if early schooling can help keep alive the habit of thinking that such work may weaken. "
   "1 is not assumed: the passage speaks of output, practice and time saved, and says nothing about the wages of workers who divide a task.",
   "केवल 2 पूर्वधारणा है। दोहराव वाले काम से कुंद हुए मन के लिए स्मिथ का उपाय बचपन में शिक्षा है, जिसका अर्थ तभी बनता है जब आरंभिक शिक्षा सोचने की उस आदत को जीवित रखने में सहायक हो सके जिसे ऐसा काम कमज़ोर कर सकता है। "
   "1 पूर्वधारणा नहीं है: परिच्छेद उत्पादन, अभ्यास और बचे समय की बात करता है, और काम बाँटने वाले कामगारों की मज़दूरी के बारे में कुछ नहीं कहता।",
   "assumptions",
   st=["Workers who divide a task among themselves earn higher wages than those who work alone.",
       "Schooling in childhood can help to keep alive the habit of thinking that repetitive work may weaken."],
   st_hi=["जो कामगार काम आपस में बाँट लेते हैं, वे अकेले काम करने वालों से अधिक मज़दूरी पाते हैं।",
          "बचपन की शिक्षा सोचने की उस आदत को जीवित रखने में सहायक हो सकती है जिसे दोहराव वाला काम कमज़ोर कर सकता है।"],
   key=1)
RQ(p, "Inference", "hard", "mcq",
   "Which one of the following can be inferred from the passage about Adam Smith's view?",
   "एडम स्मिथ के विचार के बारे में परिच्छेद से निम्नलिखित में से क्या अनुमान लगाया जा सकता है?",
   "The last sentence says that for Smith 'the efficiency of a task' did not settle 'what that task did to the person doing it': he judged work by its effect on the worker as well as by its output. "
   "He did not want every worker to learn every step -- that would undo the division he praised; he never thought the losses outweighed the gains in output; and his schooling was a remedy for the mind, not a way to raise output in repeated tasks.",
   "अंतिम वाक्य कहता है कि स्मिथ के लिए 'किसी काम की दक्षता' से यह तय नहीं हो जाता था कि 'वह काम करने वाले व्यक्ति पर क्या असर डालता है': वे काम को उसके उत्पादन के साथ-साथ कामगार पर उसके प्रभाव से भी आँकते थे। "
   "वे नहीं चाहते थे कि हर कामगार हर चरण सीखे -- इससे वह विभाजन ही मिट जाता जिसकी उन्होंने प्रशंसा की; उन्होंने कभी नहीं माना कि हानियाँ उत्पादन के लाभों से अधिक हैं; और उनकी शिक्षा मन का उपाय थी, दोहराए जाने वाले कामों में उत्पादन बढ़ाने का साधन नहीं।",
   "what-can-be-inferred-about-smith",
   opts=["He believed each worker in a pin factory should learn every step of making a pin.",
         "He thought the losses from repetitive work outweighed the gains in output it brought.",
         "He judged work by its effect on the worker as well as by what it produced.",
         "He held that schooling would make workers more productive in their repeated tasks."],
   opts_hi=["उनका मानना था कि पिन कारख़ाने के हर कामगार को पिन बनाने का हर चरण सीखना चाहिए।",
            "उनका विचार था कि दोहराव वाले काम की हानियाँ उससे मिलने वाले उत्पादन के लाभों से अधिक हैं।",
            "वे काम को उसके उत्पादन के साथ-साथ कामगार पर उसके प्रभाव से भी आँकते थे।",
            "उनका मत था कि शिक्षा कामगारों को उनके दोहराए जाने वाले कामों में अधिक उत्पादक बनाएगी।"],
   ans=2, pos=2)

# ------------------------------------------------------------------ P08 the ozone treaty and climate change (2)
p = passage("p08",
  "The treaty that protects the ozone layer is often held up as proof that the world can act together. Signed in 1987 and since accepted by every country, the Montreal Protocol phased out most of the chemicals that were thinning the ozone layer, and the layer is now expected to recover over the coming decades. "
  "It is tempting to conclude that climate change can be solved the same way. But the conditions were unusually kind. The ozone-destroying chemicals were made by a fairly small number of firms, used in a limited range of products such as refrigerators and aerosol cans, and could be replaced at modest cost; richer countries also paid to help poorer ones switch. "
  "Carbon dioxide, by contrast, is released by almost every power station, vehicle, factory and farm, and replacing the activities that produce it touches the whole economy. "
  "The ozone treaty shows that cooperation is possible; it does not show that it is easy when the costs are spread across everything a society does.",
  "ओज़ोन परत की रक्षा करने वाली संधि को प्रायः इस बात के प्रमाण के रूप में प्रस्तुत किया जाता है कि दुनिया मिलकर काम कर सकती है। 1987 में हस्ताक्षरित और तब से हर देश द्वारा स्वीकार किए गए मॉन्ट्रियल प्रोटोकॉल ने ओज़ोन परत को पतला कर रहे अधिकांश रसायनों को चरणबद्ध ढंग से समाप्त किया, और अब आने वाले दशकों में परत के ठीक होने की आशा है। "
  "यह निष्कर्ष निकालने का मन होता है कि जलवायु परिवर्तन को भी इसी तरह सुलझाया जा सकता है। पर परिस्थितियाँ असामान्य रूप से अनुकूल थीं। ओज़ोन नष्ट करने वाले रसायन अपेक्षाकृत कम कंपनियाँ बनाती थीं, वे रेफ़्रिजरेटर और एरोसोल डिब्बों जैसे सीमित उत्पादों में प्रयुक्त होते थे, और उन्हें साधारण लागत पर बदला जा सकता था; धनी देशों ने निर्धन देशों को बदलाव में सहायता के लिए धन भी दिया। "
  "इसके विपरीत, कार्बन डाइऑक्साइड लगभग हर बिजलीघर, वाहन, कारख़ाने और खेत से निकलती है, और उसे पैदा करने वाली गतिविधियों को बदलना पूरी अर्थव्यवस्था को छूता है। "
  "ओज़ोन संधि दिखाती है कि सहयोग संभव है; यह नहीं दिखाती कि वह तब आसान है जब लागत समाज के हर कार्य में फैली हो।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage grants the ozone treaty's success and then explains it by conditions -- few producers, limited uses, cheap substitutes, aid to poorer countries -- that carbon dioxide does not share. "
   "It warns against concluding that climate change can be solved 'the same way'; it says cooperation is 'possible', so it does not dismiss treaties; and aid from richer countries is one of the favourable conditions, not the passage's recommendation.",
   "परिच्छेद ओज़ोन संधि की सफलता को स्वीकार करता है और फिर उसे ऐसी परिस्थितियों से समझाता है -- कम उत्पादक, सीमित उपयोग, सस्ते विकल्प, निर्धन देशों को सहायता -- जो कार्बन डाइऑक्साइड के साथ नहीं हैं। "
   "वह यह निष्कर्ष निकालने के विरुद्ध चेताता है कि जलवायु परिवर्तन को 'इसी तरह' सुलझाया जा सकता है; वह सहयोग को 'संभव' कहता है, इसलिए संधियों को ख़ारिज नहीं करता; और धनी देशों की सहायता अनुकूल परिस्थितियों में से एक है, परिच्छेद की सिफ़ारिश नहीं।",
   "crux",
   opts=["The ozone treaty owed its success to conditions that the problem of climate change does not share.",
         "The ozone treaty shows that climate change can be tackled by the same means and just as quickly.",
         "International treaties rarely work, since countries will not bear costs for the common good of all.",
         "Richer countries should pay poorer ones to help them cut their own emissions of carbon dioxide."],
   opts_hi=["ओज़ोन संधि की सफलता ऐसी परिस्थितियों के कारण थी जो जलवायु परिवर्तन की समस्या के साथ नहीं हैं।",
            "ओज़ोन संधि दिखाती है कि जलवायु परिवर्तन से उन्हीं साधनों से और उतनी ही जल्दी निपटा जा सकता है।",
            "अंतरराष्ट्रीय संधियाँ विरले ही सफल होती हैं, क्योंकि देश सबके साझा हित के लिए लागत नहीं उठाते।",
            "धनी देशों को निर्धन देशों को उनके कार्बन डाइऑक्साइड उत्सर्जन घटाने में सहायता के लिए धन देना चाहिए।"],
   ans=0, pos=0)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Neither is valid. 1 contradicts the passage's last sentence, which says cooperation is 'possible' and only denies that it is easy; a treaty on climate change is harder, not ruled out. "
   "2 goes too far: cheap substitutes were one of several favourable conditions, alongside few producers, limited uses and aid to poorer countries, and the passage gives no ground for saying that without that one condition the treaty would 'certainly' have failed.",
   "कोई भी वैध नहीं। 1 परिच्छेद के अंतिम वाक्य का खंडन करता है, जो सहयोग को 'संभव' कहता है और केवल उसके आसान होने से इनकार करता है; जलवायु परिवर्तन पर संधि कठिन है, असंभव नहीं। "
   "2 बहुत आगे जाता है: सस्ते विकल्प कई अनुकूल परिस्थितियों में से एक थे, कम उत्पादकों, सीमित उपयोगों और निर्धन देशों को सहायता के साथ, और परिच्छेद यह कहने का कोई आधार नहीं देता कि उस एक परिस्थिति के बिना संधि 'निश्चित रूप से' विफल हो जाती।",
   "conclusions",
   st=["The passage implies that no treaty on climate change can succeed.",
       "Had substitutes for the ozone-destroying chemicals been costly, the Montreal Protocol would certainly have failed."],
   st_hi=["परिच्छेद का निहितार्थ है कि जलवायु परिवर्तन पर कोई भी संधि सफल नहीं हो सकती।",
          "यदि ओज़ोन नष्ट करने वाले रसायनों के विकल्प महँगे होते, तो मॉन्ट्रियल प्रोटोकॉल निश्चित रूप से विफल हो जाता।"],
   key=3)

# ------------------------------------------------------------------ P09 a positive result in screening for a rare disease (3)
_ill, _healthy = 100, 99900
assert round(_ill * F(99, 100)) == 99 and _healthy * F(2, 100) == F(1998)
assert F(99, 99 + 1998) < F(1, 20)
_sym_ill, _sym_healthy = 100, 900                          # one in ten of 1,000 people with symptoms
_share = (_sym_ill * F(99, 100)) / (_sym_ill * F(99, 100) + _sym_healthy * F(2, 100))
assert abs(_share - F(5, 6)) < F(1, 50)                    # 99 of 117, about 85 per cent
p = passage("p09",
  "A screening test sounds reliable if it catches 99 per cent of the people who have a disease. Suppose, however, that the disease affects only one person in a thousand, and that the test also wrongly flags 2 per cent of healthy people. "
  "Screen 100,000 people and it will correctly flag about 99 of the 100 who are ill -- but also about 2,000 of the 99,900 who are not. Of everyone told that the result is positive, fewer than one in twenty actually has the disease. "
  "The test has not become worse; the result follows from how rare the disease is. This is why doctors treat a positive screening result as a reason for a second, more exact test rather than as a diagnosis, and why screening a whole population for a rare condition can cause much needless worry and treatment. "
  "The same test is far more informative when used on people who already show symptoms, among whom the disease is common. How much a positive result means depends not only on the test but on who is being tested.",
  "कोई जाँच भरोसेमंद लगती है यदि वह किसी रोग से ग्रस्त 99 प्रतिशत लोगों को पकड़ लेती है। पर मान लीजिए कि रोग हज़ार में केवल एक व्यक्ति को होता है, और जाँच 2 प्रतिशत स्वस्थ लोगों को भी ग़लती से चिह्नित कर देती है। "
  "1,00,000 लोगों की जाँच कीजिए, तो वह 100 रोगियों में से लगभग 99 को सही चिह्नित करेगी -- पर 99,900 स्वस्थ लोगों में से भी लगभग 2,000 को। जिन सबको परिणाम धनात्मक बताया जाता है, उनमें से बीस में एक से भी कम को वास्तव में रोग होता है। "
  "जाँच बदतर नहीं हुई; यह परिणाम रोग के दुर्लभ होने से निकलता है। इसीलिए डॉक्टर धनात्मक जाँच-परिणाम को निदान नहीं, बल्कि दूसरी, अधिक सटीक जाँच का कारण मानते हैं, और इसीलिए किसी दुर्लभ रोग के लिए पूरी आबादी की जाँच बहुत-सी अनावश्यक चिंता और उपचार का कारण बन सकती है। "
  "वही जाँच उन लोगों पर कहीं अधिक जानकारी देती है जिनमें पहले से लक्षण हैं, जिनमें रोग आम है। किसी धनात्मक परिणाम का कितना अर्थ है, यह केवल जाँच पर नहीं, इस पर भी निर्भर है कि किसकी जाँच की जा रही है।")
RQ(p, "Best Summary", "medium", "mcq", MSG, MSG_HI,
   "The passage shows that the same test means very different things in a population where the disease is rare and in one where it is common, and ends: 'How much a positive result means depends not only on the test but on who is being tested.' "
   "It does not reject screening, only reading a screening result as a diagnosis; the claim that a test catching 99 per cent of cases is right about 99 per cent of positives is the very error the passage exposes; and it never says that people without symptoms cannot have the disease.",
   "परिच्छेद दिखाता है कि एक ही जाँच का अर्थ उस आबादी में, जहाँ रोग दुर्लभ है, और उसमें, जहाँ वह आम है, बहुत अलग होता है, और अंत में कहता है: 'किसी धनात्मक परिणाम का कितना अर्थ है, यह केवल जाँच पर नहीं, इस पर भी निर्भर है कि किसकी जाँच की जा रही है।' "
   "वह जाँच को अस्वीकार नहीं करता, केवल जाँच-परिणाम को निदान मान लेने को; यह दावा कि 99 प्रतिशत मामलों को पकड़ने वाली जाँच 99 प्रतिशत धनात्मक परिणामों में सही होती है, ठीक वही भूल है जिसे परिच्छेद उजागर करता है; और वह कभी नहीं कहता कि बिना लक्षण वाले लोगों को रोग नहीं हो सकता।",
   "message",
   opts=["Screening tests are unreliable and should not be used to look for rare diseases in anyone.",
         "What a positive result means depends on how common the disease is among those tested.",
         "A test that catches 99 per cent of cases will be right about 99 per cent of its positive results.",
         "Doctors should test only people with symptoms, since people without them never have the disease."],
   opts_hi=["जाँचें अविश्वसनीय हैं और किसी में भी दुर्लभ रोगों को खोजने के लिए उनका प्रयोग नहीं होना चाहिए।",
            "धनात्मक परिणाम का अर्थ इस पर निर्भर है कि जिनकी जाँच हो रही है उनमें रोग कितना आम है।",
            "99 प्रतिशत मामलों को पकड़ने वाली जाँच अपने 99 प्रतिशत धनात्मक परिणामों में सही होगी।",
            "डॉक्टरों को केवल लक्षण वाले लोगों की जाँच करनी चाहिए, क्योंकि बिना लक्षण वालों को रोग कभी नहीं होता।"],
   ans=1, pos=1)
RQ(p, "Inference", "hard", "mcq",
   "Suppose the same test is used only on people who show symptoms, one in ten of whom has the disease. Going by the figures in the passage, roughly what share of those who test positive will actually have the disease?",
   "मान लीजिए वही जाँच केवल उन लोगों पर प्रयोग की जाती है जिनमें लक्षण हैं, और उनमें से दस में एक को रोग है। परिच्छेद के आँकड़ों के आधार पर, धनात्मक पाए गए लोगों में से लगभग कितने भाग को वास्तव में रोग होगा?",
   "Take 1,000 such people: 100 are ill and the test flags about 99 of them; 900 are healthy and it wrongly flags 2 per cent of them, 18. Of the 117 positives, 99 are ill -- about 85 per cent, roughly five in six. "
   "About 1 in 20 is the figure for the general population, where the disease is rare; 1 in 10 is simply the share of the ill among those tested; and 99 in 100 confuses the share of the ill that the test catches with the share of positives that are ill.",
   "ऐसे 1,000 लोग लीजिए: 100 रोगी हैं और जाँच उनमें से लगभग 99 को चिह्नित करती है; 900 स्वस्थ हैं और वह उनमें से 2 प्रतिशत, यानी 18 को ग़लती से चिह्नित करती है। 117 धनात्मक परिणामों में से 99 रोगी हैं -- लगभग 85 प्रतिशत, यानी मोटे तौर पर छह में पाँच। "
   "बीस में लगभग एक सामान्य आबादी का आँकड़ा है, जहाँ रोग दुर्लभ है; दस में एक केवल जाँचे गए लोगों में रोगियों का भाग है; और 100 में 99, जाँच द्वारा पकड़े गए रोगियों के भाग को रोगी निकले धनात्मक परिणामों के भाग से मिला देता है।",
   "the-share-of-true-positives-among-the-ill",
   opts=["About 1 in 20", "About 1 in 10", "About 5 in 6", "About 99 in 100"],
   opts_hi=["लगभग 20 में 1", "लगभग 10 में 1", "लगभग 6 में 5", "लगभग 100 में 99"],
   ans=2, pos=2)
RQ(p, "Assumption", "medium", "s2", ASSUME, ASSUME_HI,
   "Only 1 is assumed. The claim that the same test is 'far more informative' among people with symptoms holds only if it does not wrongly flag healthy people with symptoms much more often than other healthy people; if it did, the gain from a commoner disease could be lost. "
   "2 is not assumed: the passage says doctors treat a positive result as a reason for a second test, and nothing in it depends on patients refusing one.",
   "केवल 1 पूर्वधारणा है। यह दावा कि वही जाँच लक्षण वाले लोगों में 'कहीं अधिक जानकारी देती है', तभी टिकता है जब वह लक्षण वाले स्वस्थ लोगों को अन्य स्वस्थ लोगों की तुलना में बहुत अधिक बार ग़लती से चिह्नित न करे; यदि करती, तो अधिक आम रोग से मिलने वाला लाभ खो सकता था। "
   "2 पूर्वधारणा नहीं है: परिच्छेद कहता है कि डॉक्टर धनात्मक परिणाम को दूसरी जाँच का कारण मानते हैं, और उसमें कुछ भी मरीज़ों के उसे अस्वीकार करने पर निर्भर नहीं।",
   "assumptions",
   st=["The test wrongly flags healthy people with symptoms about as often as other healthy people.",
       "Most people told that a screening result is positive will refuse a second test."],
   st_hi=["जाँच लक्षण वाले स्वस्थ लोगों को लगभग उतनी ही बार ग़लती से चिह्नित करती है जितनी अन्य स्वस्थ लोगों को।",
          "जिन अधिकांश लोगों को जाँच-परिणाम धनात्मक बताया जाता है, वे दूसरी जाँच से इनकार कर देंगे।"],
   key=0)

# ------------------------------------------------------------------ P10 the rule of law (3)
p = passage("p10",
  "A country can have a great many laws and still lack the rule of law. Under what is sometimes called rule by law, the government uses laws as instruments: it writes them, applies them to its opponents and sets them aside when they stand in its own way. "
  "The rule of law asks for more. Laws must be public and reasonably clear, so that people can know in advance what is required of them; they must apply to those who govern as much as to the governed; and disputes about them must be settled by courts that do not take orders from either party. "
  "None of these conditions guarantees that the laws themselves are good -- a clear, evenly applied law can still be harsh. That is why the rule of law is best seen as a necessary protection rather than the whole of justice. "
  "But its absence is felt at once by anyone who has had to deal with an official whose decision depends on who is asking, and it is the first thing lost when power is allowed to judge its own case.",
  "कोई देश बहुत-से क़ानून रखते हुए भी विधि के शासन से वंचित हो सकता है। जिसे कभी-कभी विधि द्वारा शासन कहा जाता है, उसमें सरकार क़ानूनों को औज़ार की तरह प्रयोग करती है: वह उन्हें लिखती है, अपने विरोधियों पर लागू करती है, और जब वे उसके अपने रास्ते में आते हैं तो उन्हें किनारे कर देती है। "
  "विधि का शासन इससे अधिक माँगता है। क़ानून सार्वजनिक और यथोचित रूप से स्पष्ट होने चाहिए, ताकि लोग पहले से जान सकें कि उनसे क्या अपेक्षित है; वे शासन करने वालों पर उतने ही लागू होने चाहिए जितने शासितों पर; और उनसे जुड़े विवाद ऐसे न्यायालयों द्वारा निपटाए जाने चाहिए जो किसी भी पक्ष के आदेश नहीं लेते। "
  "इनमें से कोई भी शर्त यह सुनिश्चित नहीं करती कि क़ानून स्वयं अच्छे हों -- एक स्पष्ट, समान रूप से लागू क़ानून भी कठोर हो सकता है। इसीलिए विधि के शासन को न्याय की संपूर्णता के बजाय एक आवश्यक सुरक्षा के रूप में देखना सबसे उचित है। "
  "पर उसका अभाव तुरंत उस हर व्यक्ति को महसूस होता है जिसे किसी ऐसे अधिकारी से निपटना पड़ा हो जिसका निर्णय इस पर निर्भर हो कि माँगने वाला कौन है, और जब सत्ता को अपने ही मामले का न्याय करने दिया जाता है तो सबसे पहले वही खोता है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage sets out what the rule of law requires -- public, clear laws that bind rulers too, and independent courts -- and then limits its claim: these conditions do not make laws good, so the rule of law is 'a necessary protection rather than the whole of justice'. "
   "Having many laws is exactly what the opening sentence says is not enough; the passage says a clear, evenly applied law 'can still be harsh', so clarity does not make a law just; and it gives courts the task of settling disputes, not of judging whether laws are good.",
   "परिच्छेद बताता है कि विधि का शासन क्या माँगता है -- सार्वजनिक, स्पष्ट क़ानून जो शासकों पर भी लागू हों, और स्वतंत्र न्यायालय -- और फिर अपने दावे को सीमित करता है: ये शर्तें क़ानूनों को अच्छा नहीं बनातीं, इसलिए विधि का शासन 'न्याय की संपूर्णता के बजाय एक आवश्यक सुरक्षा' है। "
   "बहुत-से क़ानून होना ठीक वही है जिसे पहला वाक्य पर्याप्त नहीं बताता; परिच्छेद कहता है कि स्पष्ट, समान रूप से लागू क़ानून 'भी कठोर हो सकता है', इसलिए स्पष्टता क़ानून को न्यायपूर्ण नहीं बनाती; और वह न्यायालयों को विवाद निपटाने का काम देता है, यह आँकने का नहीं कि क़ानून अच्छे हैं या नहीं।",
   "crux",
   opts=["A country that has a great many laws can safely be taken to observe the rule of law.",
         "The rule of law binds rulers as well as the ruled, but it is not the whole of justice.",
         "Laws that are clear and are applied evenly to everyone are, for that very reason, just.",
         "Courts should decide whether laws are good or harsh before those laws are applied to anyone."],
   opts_hi=["जिस देश में बहुत-से क़ानून हैं, उसके बारे में सुरक्षित रूप से माना जा सकता है कि वहाँ विधि का शासन है।",
            "विधि का शासन शासितों के साथ शासकों को भी बाँधता है, पर वह न्याय की संपूर्णता नहीं है।",
            "जो क़ानून स्पष्ट हैं और सब पर समान रूप से लागू होते हैं, वे इसी कारण न्यायपूर्ण हैं।",
            "क़ानूनों को किसी पर लागू करने से पहले न्यायालयों को तय करना चाहिए कि वे अच्छे हैं या कठोर।"],
   ans=1, pos=1)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Both are valid. The passage says that none of the conditions of the rule of law guarantees good laws and that a clear, evenly applied law 'can still be harsh', so a law can meet those conditions and still be unjust (1). "
   "It also requires that laws apply 'to those who govern as much as to the governed', and describes rule by law as a government setting laws aside when they stand in its way; where officials may exempt themselves, that requirement fails (2).",
   "दोनों वैध हैं। परिच्छेद कहता है कि विधि के शासन की कोई भी शर्त अच्छे क़ानूनों की गारंटी नहीं देती और कि स्पष्ट, समान रूप से लागू क़ानून 'भी कठोर हो सकता है', इसलिए कोई क़ानून उन शर्तों को पूरा करते हुए भी अन्यायपूर्ण हो सकता है (1)। "
   "वह यह भी माँगता है कि क़ानून 'शासन करने वालों पर उतने ही लागू हों जितने शासितों पर', और विधि द्वारा शासन को ऐसी सरकार बताता है जो क़ानूनों को अपने रास्ते में आने पर किनारे कर देती है; जहाँ अधिकारी स्वयं को छूट दे सकें, वहाँ वह शर्त विफल हो जाती है (2)।",
   "conclusions",
   st=["A law can satisfy every condition of the rule of law and still be unjust.",
       "Where officials may exempt themselves from the laws they apply to others, the rule of law is absent."],
   st_hi=["कोई क़ानून विधि के शासन की हर शर्त पूरी करते हुए भी अन्यायपूर्ण हो सकता है।",
          "जहाँ अधिकारी दूसरों पर लागू किए जाने वाले क़ानूनों से स्वयं को छूट दे सकते हैं, वहाँ विधि का शासन नहीं है।"],
   key=2)
RQ(p, "Inference", "medium", "mcq",
   "Which one of the following would the passage regard as a breach of the rule of law, rather than merely a harsh law?",
   "निम्नलिखित में से किसे परिच्छेद केवल एक कठोर क़ानून नहीं, बल्कि विधि के शासन का उल्लंघन मानेगा?",
   "A rule letting a minister decide whom a law shall apply to makes the law's reach depend on who is concerned -- the very mark of rule by law, and a breach of the requirement that laws bind everyone, including those who govern. "
   "A high tax applied to every citizen alike, a strict littering law published well in advance, and a heavy fine imposed equally on officials and citizens may all be harsh, but each is public, clear and even, as the rule of law asks.",
   "किसी मंत्री को यह तय करने देने वाला नियम कि कोई क़ानून किस पर लागू होगा, क़ानून की पहुँच को इस पर निर्भर बना देता है कि मामला किसका है -- यही विधि द्वारा शासन की पहचान है, और इस शर्त का उल्लंघन कि क़ानून शासन करने वालों सहित सब पर लागू हों। "
   "हर नागरिक पर समान रूप से लगा ऊँचा कर, पहले से प्रकाशित कूड़ा फैलाने के विरुद्ध कड़ा क़ानून, और अधिकारियों और नागरिकों पर समान रूप से लगाया गया भारी जुर्माना -- ये सब कठोर हो सकते हैं, पर हर एक सार्वजनिक, स्पष्ट और समान है, जैसा विधि का शासन माँगता है।",
   "a-breach-rather-than-a-harsh-law",
   opts=["A rule that lets a minister decide which citizens a law shall apply to",
         "A clearly worded tax law that applies a high rate to every citizen alike",
         "A strict law against littering that is published well before it takes effect",
         "A heavy fine for a minor offence, imposed equally on officials and on citizens"],
   opts_hi=["ऐसा नियम जो किसी मंत्री को यह तय करने दे कि कोई क़ानून किन नागरिकों पर लागू होगा",
            "स्पष्ट शब्दों वाला कर क़ानून जो हर नागरिक पर समान रूप से ऊँची दर लागू करता है",
            "कूड़ा फैलाने के विरुद्ध एक कड़ा क़ानून जो लागू होने से काफ़ी पहले प्रकाशित किया गया है",
            "एक छोटे अपराध के लिए भारी जुर्माना, जो अधिकारियों और नागरिकों पर समान रूप से लगाया जाता है"],
   ans=0, pos=3)
