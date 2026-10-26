# -*- coding: utf-8 -*-
"""CSAT Level 4 · Simulator 6 -- Reading Comprehension: 10 short passages, 23 items (3 x 3, 7 x 2), Layout C.

The 2026 shape: more passages, shorter ones, fewer items each. Each passage still turns -- a claim, then its limit.
Themes, none used in Levels 1-3 or Simulators 1-5: why the least skilled overrate themselves, bystanders who wait for
others, rewards that spoil a pleasure, an ocean growing more acid, India's vultures and a cattle drug, the Salt March,
Engel's law, the case for protecting infant industries, languages that die, and the basic structure of the
Constitution. Difficulty 1 easy / 14 medium / 8 hard. Options are named by content in every explanation."""
from csat_common import passage, RQ

CRUX = "Which one of the following statements best reflects the crux of the passage?"
CRUX_HI = "निम्नलिखित में से कौन-सा कथन परिच्छेद के सार को सबसे अच्छी तरह व्यक्त करता है?"
VALID = "On the basis of the passage, which of the following conclusions is/are valid?"
VALID_HI = "परिच्छेद के आधार पर निम्नलिखित में से कौन-सा/से निष्कर्ष वैध है/हैं?"
ASSUME = "Which of the following assumptions has/have been made in the passage?"
ASSUME_HI = "परिच्छेद में निम्नलिखित में से कौन-सी पूर्वधारणा/एँ बनाई गई है/हैं?"

# ------------------------------------------------------------------ P01 why the least skilled overrate themselves (2)
p = passage("p01",
  "In a study published in 1999, the psychologists Justin Kruger and David Dunning tested students on grammar, logic and humour, and then asked each to guess how well they had done compared with the others. Those who scored lowest guessed, on average, that they had done better than most of their classmates. Kruger and Dunning suggested a reason: the skills needed to do a task well are often the same skills needed to judge how well it has been done, so the least skilled lack the means to see their own mistakes. "
  "Later researchers have added a caution. Almost everyone tends to rate themselves above average, and some of the gap between low scorers' guesses and their results comes from that general habit and from the noise in any test, not from a special blindness of the unskilled.",
  "1999 में प्रकाशित एक अध्ययन में मनोवैज्ञानिक जस्टिन क्रूगर और डेविड डनिंग ने विद्यार्थियों की व्याकरण, तर्क और हास्य में परीक्षा ली, और फिर हर एक से अनुमान लगवाया कि दूसरों की तुलना में उन्होंने कितना अच्छा किया। सबसे कम अंक पाने वालों ने औसतन अनुमान लगाया कि उन्होंने अपने अधिकांश सहपाठियों से अच्छा किया था। क्रूगर और डनिंग ने एक कारण सुझाया: किसी काम को अच्छी तरह करने के लिए जो कौशल चाहिए, वही प्रायः यह आँकने के लिए भी चाहिए कि वह कितनी अच्छी तरह हुआ, इसलिए सबसे कम कुशल लोगों के पास अपनी भूलें देखने का साधन नहीं होता। "
  "बाद के शोधकर्ताओं ने एक सावधानी जोड़ी है। लगभग हर व्यक्ति स्वयं को औसत से ऊपर आँकता है, और कम अंक पाने वालों के अनुमानों और उनके परिणामों के बीच का कुछ अंतर इसी सामान्य आदत और किसी भी परीक्षा के शोर से आता है, अकुशलों के किसी विशेष अंधेपन से नहीं।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage reports that the lowest scorers overrated themselves, gives Kruger and Dunning's explanation -- the skill to do a task is also the skill to judge it -- and adds that part of the effect comes from a general habit and test noise. "
   "It does not say skilled people underrate themselves, that the finding was disproved, or that tests cannot measure skill.",
   "परिच्छेद बताता है कि सबसे कम अंक पाने वालों ने स्वयं को बढ़ाकर आँका, क्रूगर और डनिंग की व्याख्या देता है -- काम करने का कौशल ही उसे आँकने का कौशल है -- और जोड़ता है कि प्रभाव का कुछ भाग एक सामान्य आदत और परीक्षा के शोर से आता है। "
   "वह यह नहीं कहता कि कुशल लोग स्वयं को घटाकर आँकते हैं, कि निष्कर्ष ग़लत सिद्ध हो गया, या कि परीक्षाएँ कौशल नहीं माप सकतीं।",
   "crux",
   opts=["The least skilled often overrate themselves, though part of this has more ordinary causes.",
         "The most skilled people always underrate themselves, as the 1999 study showed beyond doubt.",
         "Later research proved that the 1999 study's finding was false from beginning to end.",
         "Tests of grammar, logic and humour cannot measure anyone's real ability at all."],
   opts_hi=["सबसे कम कुशल प्रायः स्वयं को बढ़ाकर आँकते हैं, यद्यपि इसके कुछ कारण साधारण हैं।",
            "सबसे कुशल लोग हमेशा स्वयं को घटाकर आँकते हैं, जैसा 1999 के अध्ययन ने निःसंदेह दिखाया।",
            "बाद के शोध ने सिद्ध किया कि 1999 के अध्ययन का निष्कर्ष शुरू से अंत तक ग़लत था।",
            "व्याकरण, तर्क और हास्य की परीक्षाएँ किसी की वास्तविक क्षमता बिल्कुल नहीं माप सकतीं।"],
   ans=0, pos=0)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Only 2 is valid. If judging a task well uses the same skills as doing it, then improving those skills should also improve a person's judgement of their own work -- which is what Kruger and Dunning's reason implies. "
   "1 goes too far: the passage says part of the gap comes from a general habit and test noise, not that all of it does; the special blindness of the unskilled is qualified, not ruled out.",
   "केवल 2 वैध है। यदि किसी काम को अच्छी तरह आँकने में वही कौशल लगते हैं जो उसे करने में, तो उन कौशलों के सुधरने से व्यक्ति का अपने काम का आकलन भी सुधरना चाहिए -- यही क्रूगर और डनिंग का कारण संकेत करता है। "
   "1 बहुत आगे जाता है: परिच्छेद कहता है कि अंतर का कुछ भाग एक सामान्य आदत और परीक्षा के शोर से आता है, यह नहीं कि पूरा; अकुशलों के विशेष अंधेपन को सीमित किया गया है, ख़ारिज नहीं।",
   "conclusions",
   st=["The whole gap between low scorers' guesses and their results is explained by noise in the tests.",
       "On Kruger and Dunning's reasoning, training that improves a skill should also improve a person's judgement of their own work."],
   st_hi=["कम अंक पाने वालों के अनुमानों और परिणामों के बीच का पूरा अंतर परीक्षाओं के शोर से समझाया जाता है।",
          "क्रूगर और डनिंग के तर्क के अनुसार, किसी कौशल को सुधारने वाला प्रशिक्षण व्यक्ति के अपने काम के आकलन को भी सुधारना चाहिए।"],
   key=1)

# ------------------------------------------------------------------ P02 bystanders who wait for others (3)
p = passage("p02",
  "In an experiment reported in 1968, the psychologists John Darley and Bibb Latané had students talk over an intercom from separate rooms. During the talk one voice -- in fact a recording -- seemed to have a seizure. When a student believed no one else could hear, most went for help before the fit was over; when they believed four others were listening too, fewer than a third did. "
  "Darley and Latané called this a diffusion of responsibility: each person in a group feels less bound to act, assuming that someone else will. "
  "The effect is not a law of nature. Later studies found it weaker when the danger is obvious and serious, and weaker among people who know one another. Training also helps: a person who has been taught to pick out one bystander and say, 'You -- call an ambulance', turns a crowd back into individuals.",
  "1968 में प्रकाशित एक प्रयोग में मनोवैज्ञानिक जॉन डार्ली और बिब लाताने ने विद्यार्थियों से अलग-अलग कमरों से एक इंटरकॉम पर बात करवाई। बातचीत के दौरान एक आवाज़ को -- जो वास्तव में एक रिकॉर्डिंग थी -- दौरा पड़ता लगा। जब किसी विद्यार्थी को लगा कि कोई और नहीं सुन सकता, तो अधिकांश दौरा समाप्त होने से पहले सहायता लेने गए; जब उन्हें लगा कि चार और भी सुन रहे हैं, तो एक-तिहाई से कम गए। "
  "डार्ली और लाताने ने इसे उत्तरदायित्व का बिखराव कहा: समूह का हर व्यक्ति कुछ करने के लिए स्वयं को कम बँधा अनुभव करता है, यह मानकर कि कोई और करेगा। "
  "यह प्रभाव प्रकृति का नियम नहीं। बाद के अध्ययनों ने इसे तब कमज़ोर पाया जब ख़तरा स्पष्ट और गंभीर हो, और उन लोगों में भी कमज़ोर जो एक-दूसरे को जानते हों। प्रशिक्षण भी सहायक है: जिस व्यक्ति को सिखाया गया हो कि एक दर्शक को चुनकर कहे, 'आप -- एम्बुलेंस बुलाइए', वह भीड़ को फिर से व्यक्तियों में बदल देता है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage describes how people in a group help less because each assumes someone else will, then limits the claim -- the effect weakens when danger is plain, among people who know each other, and when someone is singled out. "
   "It calls the effect not a law of nature, so it does not say crowds never help; it does not blame the students' character; and it says nothing about ambulances being slow.",
   "परिच्छेद बताता है कि समूह में लोग कम सहायता क्यों करते हैं, क्योंकि हर एक मानता है कि कोई और करेगा, फिर दावे को सीमित करता है -- ख़तरा स्पष्ट होने पर, एक-दूसरे को जानने वालों में, और किसी को अलग से चुनने पर प्रभाव कमज़ोर पड़ता है। "
   "वह प्रभाव को प्रकृति का नियम नहीं कहता, इसलिए यह नहीं कहता कि भीड़ कभी सहायता नहीं करती; वह विद्यार्थियों के चरित्र को दोष नहीं देता; और एम्बुलेंस के धीमे होने के बारे में कुछ नहीं कहता।",
   "crux",
   opts=["People in a crowd never help a stranger in trouble, whatever the danger.",
         "The students in the experiment were selfish people who did not care for others.",
         "People help less when others are present, but this can be weakened or overcome.",
         "Ambulances reach emergencies too slowly to make bystanders' help worthwhile."],
   opts_hi=["भीड़ में लोग किसी संकट में पड़े अजनबी की कभी सहायता नहीं करते, ख़तरा चाहे जो हो।",
            "प्रयोग के विद्यार्थी स्वार्थी लोग थे जिन्हें दूसरों की परवाह नहीं थी।",
            "दूसरों के होने पर लोग कम सहायता करते हैं, पर इसे कमज़ोर किया या जीता जा सकता है।",
            "एम्बुलेंस आपात स्थितियों तक इतनी धीमी पहुँचती हैं कि दर्शकों की सहायता व्यर्थ है।"],
   ans=2, pos=2)
RQ(p, "Inference", "hard", "mcq",
   "According to the passage, why does picking out one bystander by name or by pointing work?",
   "परिच्छेद के अनुसार, किसी एक दर्शक को नाम लेकर या इशारा करके चुनना क्यों काम करता है?",
   "Diffusion of responsibility happens because each person assumes someone else will act. Naming one person removes that assumption for that person: the task is now plainly theirs and no one else's. "
   "It does not make the danger more serious, it does not rely on the bystander being a friend, and it is not a matter of the bystander's training.",
   "उत्तरदायित्व का बिखराव इसलिए होता है कि हर व्यक्ति मानता है कि कोई और करेगा। एक व्यक्ति का नाम लेना उस व्यक्ति के लिए यह मान्यता हटा देता है: काम अब स्पष्ट रूप से उसका है, किसी और का नहीं। "
   "यह ख़तरे को अधिक गंभीर नहीं बनाता, यह दर्शक के मित्र होने पर निर्भर नहीं, और यह दर्शक के प्रशिक्षण का प्रश्न नहीं।",
   "why-picking-out-one-bystander-works",
   opts=["It makes the danger seem far more serious than the bystander had thought it was.",
         "It leaves that person unable to assume that someone else will act.",
         "It works only when the person picked out is a friend of the one who is ill.",
         "It works because the bystander picked out has usually been trained in first aid."],
   opts_hi=["यह ख़तरे को उससे कहीं अधिक गंभीर दिखाता है जितना दर्शक ने सोचा था।",
            "यह उस व्यक्ति को यह मानने लायक़ नहीं छोड़ता कि कोई और करेगा।",
            "यह तभी काम करता है जब चुना गया व्यक्ति बीमार व्यक्ति का मित्र हो।",
            "यह इसलिए काम करता है कि चुना गया दर्शक प्रायः प्राथमिक चिकित्सा में प्रशिक्षित होता है।"],
   ans=1, pos=1)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Both are valid. The students who believed they were alone went for help far more often than those who believed four others were listening, so the mere belief that others are present reduced helping (1). "
   "And the passage says later studies found the effect weaker when the danger is obvious and serious, so a plain, serious emergency should see more help than an ambiguous one (2).",
   "दोनों वैध हैं। जिन विद्यार्थियों को लगा कि वे अकेले हैं, वे उनसे कहीं अधिक बार सहायता लेने गए जिन्हें लगा कि चार और सुन रहे हैं, इसलिए दूसरों के होने की केवल मान्यता ने सहायता घटाई (1)। "
   "और परिच्छेद कहता है कि बाद के अध्ययनों ने ख़तरा स्पष्ट और गंभीर होने पर प्रभाव को कमज़ोर पाया, इसलिए स्पष्ट, गंभीर आपात स्थिति में अस्पष्ट स्थिति से अधिक सहायता मिलनी चाहिए (2)।",
   "conclusions",
   st=["Believing that others are present, even without seeing them, can make a person less likely to help.",
       "A bystander is more likely to act when the danger is plainly serious than when it is unclear."],
   st_hi=["दूसरों के उपस्थित होने की मान्यता, उन्हें देखे बिना भी, व्यक्ति के सहायता करने की संभावना घटा सकती है।",
          "कोई दर्शक तब कुछ करने की अधिक संभावना रखता है जब ख़तरा स्पष्ट रूप से गंभीर हो, न कि जब वह अस्पष्ट हो।"],
   key=2)

# ------------------------------------------------------------------ P03 rewards that spoil a pleasure (2)
p = passage("p03",
  "In a study published in 1973, the psychologists Mark Lepper, David Greene and Richard Nisbett picked out nursery-school children who liked drawing with felt-tip markers. Some were promised a certificate for drawing, some got the same certificate as a surprise afterwards, and some got nothing. In the following days, when markers were simply left out in the classroom, the children who had been promised the reward drew less than the others. "
  "Drawing had become, for them, something done for a prize rather than for its own sake. The lesson is not that rewards always backfire. Rewards for dull tasks, which no one would do for pleasure anyway, do little harm, and the surprise certificate did none. The risk lies in paying people for what they already enjoy.",
  "1973 में प्रकाशित एक अध्ययन में मनोवैज्ञानिक मार्क लेपर, डेविड ग्रीन और रिचर्ड निस्बेट ने ऐसे नर्सरी विद्यालय के बच्चे चुने जिन्हें फ़ेल्ट-टिप मार्करों से चित्र बनाना पसंद था। कुछ को चित्र बनाने के लिए प्रमाणपत्र का वचन दिया गया, कुछ को वही प्रमाणपत्र बाद में अचानक मिला, और कुछ को कुछ नहीं। अगले दिनों में, जब मार्कर बस कक्षा में रख दिए गए, तो जिन बच्चों को पुरस्कार का वचन मिला था उन्होंने बाक़ी से कम चित्र बनाए। "
  "उनके लिए चित्र बनाना अपने आनंद के लिए नहीं, बल्कि इनाम के लिए किया जाने वाला काम बन गया था। सीख यह नहीं कि पुरस्कार हमेशा उलटा असर करते हैं। नीरस कामों के लिए पुरस्कार, जिन्हें कोई वैसे भी आनंद के लिए नहीं करता, बहुत कम हानि करते हैं, और अचानक मिले प्रमाणपत्र ने कोई हानि नहीं की। जोखिम उन कामों के लिए भुगतान करने में है जिनका लोग पहले से आनंद लेते हैं।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage shows that a promised reward made children draw less once the reward was gone, and limits the lesson: rewards for dull tasks and surprise rewards do little or no harm; the risk is in rewarding what people already enjoy. "
   "It says rewards do not always backfire; it found the surprise reward harmless, not harmful; and it does not say children dislike drawing.",
   "परिच्छेद दिखाता है कि वचन दिए गए पुरस्कार से बच्चों ने पुरस्कार हटने के बाद कम चित्र बनाए, और सीख को सीमित करता है: नीरस कामों के लिए पुरस्कार और अचानक पुरस्कार बहुत कम या कोई हानि नहीं करते; जोखिम उसे पुरस्कृत करने में है जिसका लोग पहले से आनंद लेते हैं। "
   "वह कहता है कि पुरस्कार हमेशा उलटा असर नहीं करते; उसने अचानक पुरस्कार को हानिरहित पाया, हानिकारक नहीं; और वह यह नहीं कहता कि बच्चों को चित्र बनाना नापसंद है।",
   "crux",
   opts=["Rewards of every kind always make people less willing to do any task they are given.",
         "Surprise rewards spoil children's pleasure in drawing as much as promised ones.",
         "Most young children do not really enjoy drawing with felt-tip markers.",
         "Promised rewards for what people already enjoy can weaken their own wish to do it."],
   opts_hi=["हर प्रकार के पुरस्कार लोगों को किसी भी काम को करने के लिए हमेशा कम इच्छुक बनाते हैं।",
            "अचानक मिले पुरस्कार बच्चों का चित्र बनाने का आनंद उतना ही बिगाड़ते हैं जितना वचन दिए गए।",
            "अधिकांश छोटे बच्चे फ़ेल्ट-टिप मार्करों से चित्र बनाने का वास्तव में आनंद नहीं लेते।",
            "जिस काम में लोग पहले से आनंद लें, उसके लिए पुरस्कार का वचन उनकी अपनी इच्छा घटा सकता है।"],
   ans=3, pos=3)
RQ(p, "Inference", "hard", "mcq",
   "Which one of the following plans runs the risk that the passage describes?",
   "निम्नलिखित में से कौन-सी योजना उस जोखिम को उठाती है जिसका परिच्छेद वर्णन करता है?",
   "The risk is in rewarding, by promise, an activity people already do for pleasure. A library that starts paying children who already love reading for every book they finish does exactly that. "
   "Paying workers to sort old files rewards a dull task; praising a child unexpectedly after a match is like the surprise certificate; and a fine for late books is a penalty for a different behaviour, not a promised reward for an enjoyed one.",
   "जोखिम ऐसी गतिविधि को, वचन देकर, पुरस्कृत करने में है जिसे लोग पहले से आनंद के लिए करते हैं। जो पुस्तकालय पहले से पढ़ना पसंद करने वाले बच्चों को हर पूरी की गई पुस्तक के लिए भुगतान करने लगे, वह ठीक यही करता है। "
   "पुरानी फ़ाइलें छाँटने के लिए कर्मचारियों को भुगतान एक नीरस काम को पुरस्कृत करता है; मैच के बाद बच्चे की अचानक प्रशंसा अचानक मिले प्रमाणपत्र जैसी है; और देर से लौटाई पुस्तकों पर जुर्माना किसी और व्यवहार का दंड है, आनंददायक काम का वचन दिया पुरस्कार नहीं।",
   "a-plan-that-runs-the-risk",
   opts=["A library starts paying children who already love reading for each book they finish.",
         "An office pays its staff extra to sort out its old files, a task that nobody enjoys.",
         "A coach praises a young player, without warning, after a good match.",
         "A library charges a small fine for every day that a borrowed book is late."],
   opts_hi=["एक पुस्तकालय पहले से पढ़ना पसंद करने वाले बच्चों को हर पूरी की गई पुस्तक के लिए भुगतान करने लगता है।",
            "एक कार्यालय पुरानी फ़ाइलें छाँटने के लिए, जिसे कोई पसंद नहीं करता, कर्मचारियों को अतिरिक्त भुगतान करता है।",
            "एक प्रशिक्षक एक अच्छे मैच के बाद, बिना पहले बताए, एक युवा खिलाड़ी की प्रशंसा करता है।",
            "एक पुस्तकालय उधार ली गई पुस्तक के देर से लौटने के हर दिन पर छोटा जुर्माना लेता है।"],
   ans=0, pos=0)

# ------------------------------------------------------------------ P04 an ocean growing more acid (2)
p = passage("p04",
  "The oceans take up roughly a quarter of the carbon dioxide that human activity releases, which slows the warming of the air. But the gas does not simply vanish. Dissolved in sea water, it forms carbonic acid, and since the start of the industrial age the surface ocean has become about 30 per cent more acidic. "
  "Sea water is still alkaline; 'acidification' means only that it is moving towards acid. Even so, the change matters to creatures that build shells and skeletons of calcium carbonate -- corals, oysters, and tiny floating snails on which fish feed -- because more acidic water makes that building harder. A service the oceans perform for the climate thus carries a cost of its own.",
  "महासागर मानव गतिविधि से निकलने वाली कार्बन डाइऑक्साइड का लगभग एक-चौथाई सोख लेते हैं, जिससे वायु का गर्म होना धीमा होता है। पर यह गैस बस ग़ायब नहीं हो जाती। समुद्री जल में घुलकर वह कार्बोनिक अम्ल बनाती है, और औद्योगिक युग की शुरुआत से सतही महासागर लगभग 30 प्रतिशत अधिक अम्लीय हो गया है। "
  "समुद्री जल अब भी क्षारीय है; 'अम्लीकरण' का अर्थ केवल यह है कि वह अम्ल की ओर बढ़ रहा है। फिर भी यह परिवर्तन उन जीवों के लिए मायने रखता है जो कैल्शियम कार्बोनेट के खोल और कंकाल बनाते हैं -- प्रवाल, सीपियाँ, और छोटे तैरते घोंघे जिन पर मछलियाँ पलती हैं -- क्योंकि अधिक अम्लीय जल यह निर्माण कठिन बनाता है। इस प्रकार महासागर जलवायु के लिए जो सेवा करते हैं, उसकी अपनी एक क़ीमत है।")
RQ(p, "Specific Detail", "easy", "mcq",
   "According to the passage, what happens to the carbon dioxide that the oceans take up?",
   "परिच्छेद के अनुसार, महासागरों द्वारा सोखी गई कार्बन डाइऑक्साइड का क्या होता है?",
   "The passage says that, dissolved in sea water, the gas forms carbonic acid, making the surface ocean more acidic. "
   "It does not say the gas escapes back to the air, that it turns sea water into acid -- the water is still alkaline -- or that it is stored harmlessly in shells.",
   "परिच्छेद कहता है कि समुद्री जल में घुलकर गैस कार्बोनिक अम्ल बनाती है, जिससे सतही महासागर अधिक अम्लीय होता है। "
   "वह यह नहीं कहता कि गैस वापस वायु में निकल जाती है, कि वह समुद्री जल को अम्ल बना देती है -- जल अब भी क्षारीय है -- या कि वह खोलों में हानिरहित रूप से जमा हो जाती है।",
   "what-happens-to-the-gas",
   opts=["It escapes back into the air within a few years of being taken up.",
         "It dissolves and forms carbonic acid, making the water more acidic.",
         "It turns the water of the surface ocean into an acid like vinegar.",
         "It is stored harmlessly in the shells and skeletons of sea creatures."],
   opts_hi=["सोखे जाने के कुछ वर्षों के भीतर वह वापस वायु में निकल जाती है।",
            "वह घुलकर कार्बोनिक अम्ल बनाती है, जिससे जल अधिक अम्लीय होता है।",
            "वह सतही महासागर के जल को सिरके जैसे अम्ल में बदल देती है।",
            "वह समुद्री जीवों के खोलों और कंकालों में हानिरहित रूप से जमा हो जाती है।"],
   ans=1, pos=1)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Neither is valid. 1 misreads the passage: it says sea water is still alkaline and is only moving towards acid, so 30 per cent more acidic does not mean the oceans have become acid. "
   "2 also goes beyond it: the passage says the oceans' uptake slows warming and carries a cost, but it never says the uptake should be stopped or that the oceans would be better off taking up none of the gas.",
   "कोई भी वैध नहीं। 1 परिच्छेद को ग़लत पढ़ता है: वह कहता है कि समुद्री जल अब भी क्षारीय है और केवल अम्ल की ओर बढ़ रहा है, इसलिए 30 प्रतिशत अधिक अम्लीय का अर्थ यह नहीं कि महासागर अम्ल बन गए हैं। "
   "2 भी उससे आगे जाता है: परिच्छेद कहता है कि महासागरों का सोखना गर्म होना धीमा करता है और उसकी क़ीमत है, पर वह कभी नहीं कहता कि सोखना रोका जाना चाहिए या महासागर बिना गैस सोखे बेहतर होते।",
   "conclusions",
   st=["The surface ocean has now become an acid rather than an alkaline liquid.",
       "It would be better for the world if the oceans took up none of the carbon dioxide released."],
   st_hi=["सतही महासागर अब क्षारीय द्रव के बजाय एक अम्ल बन गया है।",
          "दुनिया के लिए बेहतर होता यदि महासागर निकली हुई कार्बन डाइऑक्साइड में से कुछ भी न सोखते।"],
   key=3)

# ------------------------------------------------------------------ P05 India's vultures and a cattle drug (3)
p = passage("p05",
  "In the early 1990s tens of millions of vultures lived in India, clearing the countryside of dead cattle. Within about fifteen years the numbers of the commonest species had fallen by more than 95 per cent. The cause, found in the early 2000s, was diclofenac, a painkiller given to sick cattle: vultures that fed on the carcasses of treated animals died of kidney failure, and even a small share of contaminated carcasses was enough to kill birds on a vast scale. "
  "India banned the drug for veterinary use in 2006, and a safe alternative was available. But the vultures' absence had costs of its own. Carcasses lay rotting for longer, and the number of stray dogs feeding on them rose, bringing with it more cases of rabies. A cheap medicine for one animal had passed, through a chain few had thought about, to a cost borne by people.",
  "1990 के दशक के आरंभ में भारत में करोड़ों गिद्ध रहते थे, जो ग्रामीण क्षेत्रों को मरे पशुओं से साफ़ करते थे। लगभग पंद्रह वर्षों में सबसे आम प्रजातियों की संख्या 95 प्रतिशत से अधिक घट गई थी। कारण, जो 2000 के दशक के आरंभ में पाया गया, डाइक्लोफ़ेनाक था, बीमार पशुओं को दी जाने वाली एक दर्दनिवारक दवा: उपचारित पशुओं के शवों को खाने वाले गिद्ध गुर्दे की विफलता से मर गए, और दूषित शवों का एक छोटा-सा अंश भी पक्षियों को बहुत बड़े पैमाने पर मारने के लिए पर्याप्त था। "
  "भारत ने 2006 में इस दवा के पशु-चिकित्सा उपयोग पर प्रतिबंध लगाया, और एक सुरक्षित विकल्प उपलब्ध था। पर गिद्धों की अनुपस्थिति की अपनी क़ीमतें थीं। शव अधिक समय तक सड़ते रहे, और उन्हें खाने वाले आवारा कुत्तों की संख्या बढ़ी, जिसके साथ रेबीज़ के मामले बढ़े। एक पशु की एक सस्ती दवा, ऐसी कड़ी के रास्ते जिसके बारे में कम लोगों ने सोचा था, लोगों द्वारा उठाई जाने वाली क़ीमत तक पहुँच गई थी।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage traces how a cattle painkiller killed most of India's vultures and how their loss then cost people, through rotting carcasses, more stray dogs and more rabies -- harm passed along a chain few had foreseen. "
   "It names a single cause, the drug, not many; it says a safe alternative existed, so the drug was not indispensable; and it does not say vultures spread rabies.",
   "परिच्छेद बताता है कि पशुओं की एक दर्दनिवारक दवा ने भारत के अधिकांश गिद्धों को कैसे मार डाला और फिर उनकी हानि ने लोगों को कैसे क़ीमत चुकवाई, सड़ते शवों, अधिक आवारा कुत्तों और अधिक रेबीज़ के रास्ते -- ऐसी कड़ी से पहुँची हानि जिसे कम लोगों ने देखा था। "
   "वह एक ही कारण, दवा, बताता है, अनेक नहीं; वह कहता है कि सुरक्षित विकल्प था, इसलिए दवा अपरिहार्य नहीं थी; और वह यह नहीं कहता कि गिद्ध रेबीज़ फैलाते हैं।",
   "crux",
   opts=["Vultures declined for many reasons at once, of which no one has proved the chief.",
         "Diclofenac was so necessary for cattle that banning it did more harm than good.",
         "Vultures spread rabies, so their decline was in the end good for public health.",
         "A cattle drug wiped out vultures, and their loss in turn brought costs to people."],
   opts_hi=["गिद्ध एक साथ अनेक कारणों से घटे, जिनमें से मुख्य कारण किसी ने सिद्ध नहीं किया।",
            "डाइक्लोफ़ेनाक पशुओं के लिए इतना आवश्यक था कि उस पर प्रतिबंध से लाभ से अधिक हानि हुई।",
            "गिद्ध रेबीज़ फैलाते हैं, इसलिए उनका घटना अंततः जन-स्वास्थ्य के लिए अच्छा था।",
            "पशुओं की एक दवा ने गिद्धों को मिटाया, और उनकी हानि ने लोगों पर क़ीमतें डालीं।"],
   ans=3, pos=3)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Only 2 is valid. The passage says even a small share of contaminated carcasses killed birds on a vast scale, so the poison did not have to be in most carcasses to do great harm. "
   "1 is not supported: the passage mentions the ban of 2006 and a safe alternative, but it never says that the vultures have since returned to their old numbers.",
   "केवल 2 वैध है। परिच्छेद कहता है कि दूषित शवों के एक छोटे-से अंश ने भी बहुत बड़े पैमाने पर पक्षियों को मारा, इसलिए भारी हानि के लिए विष का अधिकांश शवों में होना आवश्यक नहीं था। "
   "1 समर्थित नहीं: परिच्छेद 2006 के प्रतिबंध और सुरक्षित विकल्प का उल्लेख करता है, पर कभी नहीं कहता कि तब से गिद्ध अपनी पुरानी संख्या में लौट आए हैं।",
   "conclusions",
   st=["Since the ban of 2006, India's vultures have returned to the numbers of the early 1990s.",
       "A poison carried by only a small share of carcasses could still kill vultures in very large numbers."],
   st_hi=["2006 के प्रतिबंध के बाद से भारत के गिद्ध 1990 के दशक के आरंभ की संख्या में लौट आए हैं।",
          "केवल शवों के एक छोटे अंश में मौजूद विष भी गिद्धों को बहुत बड़ी संख्या में मार सकता था।"],
   key=1)
RQ(p, "Inference", "hard", "mcq",
   "Which one of the following best explains why the passage says the chain was one 'few had thought about'?",
   "निम्नलिखित में से कौन-सा सबसे अच्छी तरह समझाता है कि परिच्छेद उस कड़ी को ऐसी क्यों कहता है 'जिसके बारे में कम लोगों ने सोचा था'?",
   "The drug was given to cattle, for the cattle's sake; its effect on vultures came only after the animals died, and its effect on people only through rotting carcasses, dogs and rabies. Each link was far from the original use, which is why few foresaw the harm. "
   "The passage gives no sign that the drug was secret, that its makers knew of the danger, or that vets were careless with the dose.",
   "दवा पशुओं को, पशुओं के लिए, दी गई थी; गिद्धों पर उसका प्रभाव पशुओं के मरने के बाद ही आया, और लोगों पर उसका प्रभाव केवल सड़ते शवों, कुत्तों और रेबीज़ के रास्ते। हर कड़ी मूल उपयोग से दूर थी, इसीलिए कम लोगों ने हानि का पूर्वानुमान किया। "
   "परिच्छेद में कोई संकेत नहीं कि दवा गुप्त थी, कि उसके निर्माता ख़तरे को जानते थे, या कि पशु-चिकित्सक मात्रा में लापरवाह थे।",
   "why-few-had-thought-about-the-chain",
   opts=["The harm reached vultures, then people, only through steps far from treating cattle.",
         "The drug was sold secretly, so no one outside the trade knew it was being used.",
         "The makers of the drug knew about the danger to vultures but chose to hide it.",
         "Vets gave cattle many times the safe dose, which no one at all had expected them to do."],
   opts_hi=["हानि गिद्धों और फिर लोगों तक केवल ऐसे चरणों से पहुँची जो पशुओं के उपचार से बहुत दूर थे।",
            "दवा गुप्त रूप से बेची गई, इसलिए व्यापार के बाहर किसी को पता नहीं था कि उसका उपयोग हो रहा है।",
            "दवा के निर्माता गिद्धों को होने वाले ख़तरे को जानते थे पर उन्होंने उसे छिपाना चुना।",
            "पशु-चिकित्सकों ने पशुओं को सुरक्षित मात्रा से कई गुना दी, जिसकी किसी ने अपेक्षा नहीं की थी।"],
   ans=0, pos=0)

# ------------------------------------------------------------------ P06 the Salt March (2)
p = passage("p06",
  "On 12 March 1930 Gandhi set out from his ashram at Sabarmati with a band of followers and walked for more than three weeks to the coast at Dandi, where he picked up a handful of salt and so broke the law that made the making of salt a government monopoly. "
  "To many observers the choice seemed odd at first. Why salt, when there were weightier grievances? But the salt tax touched everyone, rich and poor, and it fell hardest on the poor, for whom salt was a large share of a small budget. A protest about salt was one that every Indian could understand and join, and breaking that law needed nothing more than sea water and the sun. The genius of the choice lay in its smallness.",
  "12 मार्च 1930 को गांधीजी अनुयायियों के एक दल के साथ साबरमती के अपने आश्रम से निकले और तीन सप्ताह से अधिक चलकर दांडी के समुद्र तट पर पहुँचे, जहाँ उन्होंने मुट्ठी भर नमक उठाया और इस प्रकार उस क़ानून को तोड़ा जिसने नमक बनाने को सरकार का एकाधिकार बना रखा था। "
  "बहुत-से प्रेक्षकों को यह चुनाव पहले अजीब लगा। नमक ही क्यों, जब कहीं भारी शिकायतें थीं? पर नमक कर हर किसी को छूता था, धनी और निर्धन दोनों को, और सबसे अधिक निर्धनों पर पड़ता था, जिनके छोटे बजट का नमक एक बड़ा भाग था। नमक पर विरोध ऐसा था जिसे हर भारतीय समझ सकता और जिसमें शामिल हो सकता था, और उस क़ानून को तोड़ने के लिए समुद्री जल और धूप से अधिक कुछ नहीं चाहिए था। इस चुनाव की प्रतिभा उसकी लघुता में थी।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage argues that salt, though it seemed a small issue, was a shrewd choice: the tax touched everyone, hurt the poor most, and could be defied by anyone with sea water and sun. "
   "It says the choice seemed odd only at first; it does not rank salt as the weightiest grievance; and it says nothing about how long the march took compared with other protests.",
   "परिच्छेद तर्क देता है कि नमक, यद्यपि छोटा मुद्दा लगता था, एक चतुर चुनाव था: कर हर किसी को छूता था, निर्धनों को सबसे अधिक चोट पहुँचाता था, और समुद्री जल व धूप वाला कोई भी उसकी अवज्ञा कर सकता था। "
   "वह कहता है कि चुनाव केवल पहले अजीब लगा; वह नमक को सबसे भारी शिकायत नहीं बताता; और वह यह नहीं कहता कि यात्रा अन्य विरोधों की तुलना में कितनी लंबी थी।",
   "crux",
   opts=["Salt was the weightiest of all the grievances that Indians held against the government.",
         "Salt, a seemingly small issue, made a protest that everyone could understand and join.",
         "The march to Dandi failed because most observers thought the choice of salt odd.",
         "Making salt from sea water was a skill that only a few people living on the coast had."],
   opts_hi=["नमक उन सभी शिकायतों में सबसे भारी था जो भारतीयों को सरकार से थीं।",
            "छोटा लगने वाला नमक ऐसा विरोध बना जिसे हर कोई समझ और अपना सके।",
            "दांडी यात्रा विफल रही क्योंकि अधिकांश प्रेक्षकों को नमक का चुनाव अजीब लगा।",
            "समुद्री जल से नमक बनाना एक ऐसा कौशल था जो केवल तट पर रहने वाले कुछ लोगों के पास था।"],
   ans=1, pos=1)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Only 1 is valid. The passage says the salt tax fell hardest on the poor, for whom salt was a large share of a small budget: the same tax took a bigger share of a poor family's income than of a rich one's. "
   "2 is not supported: the passage praises the choice of salt for its reach, but it does not say that the march ended the salt tax at once.",
   "केवल 1 वैध है। परिच्छेद कहता है कि नमक कर सबसे अधिक निर्धनों पर पड़ता था, जिनके छोटे बजट का नमक एक बड़ा भाग था: वही कर एक निर्धन परिवार की आय का धनी परिवार से बड़ा भाग लेता था। "
   "2 समर्थित नहीं: परिच्छेद नमक के चुनाव की उसकी पहुँच के लिए प्रशंसा करता है, पर यह नहीं कहता कि यात्रा ने नमक कर तुरंत समाप्त कर दिया।",
   "conclusions",
   st=["The salt tax took a larger share of a poor family's spending than of a rich family's.",
       "The march to Dandi brought the salt tax to an end as soon as Gandhi picked up the salt."],
   st_hi=["नमक कर एक निर्धन परिवार के ख़र्च का धनी परिवार से बड़ा भाग लेता था।",
          "गांधीजी के नमक उठाते ही दांडी यात्रा ने नमक कर समाप्त कर दिया।"],
   key=0)

# ------------------------------------------------------------------ P07 Engel's law (2)
p = passage("p07",
  "In 1857 the German statistician Ernst Engel, studying the budgets of working families, noticed that the poorer a household was, the larger the share of its spending that went on food. As incomes rise, families spend more on food in money terms, but the share falls, because there is only so much that anyone can eat; the extra goes on housing, schooling, travel and the like. "
  "The pattern has held so widely that the share of food in household budgets is still used as a rough gauge of how well off people are. It is a rough gauge only: a sharp rise in food prices can raise the share even when families are no poorer in other ways, and families who eat out more may count more of their spending as food.",
  "1857 में जर्मन सांख्यिकीविद् अर्न्स्ट एंगेल ने श्रमिक परिवारों के बजट का अध्ययन करते हुए देखा कि कोई परिवार जितना निर्धन होता, उसके ख़र्च का उतना ही बड़ा भाग भोजन पर जाता। आय बढ़ने के साथ परिवार भोजन पर पैसे के रूप में अधिक ख़र्च करते हैं, पर भाग घटता है, क्योंकि कोई कितना ही खा सकता है; अतिरिक्त आय आवास, पढ़ाई, यात्रा आदि पर जाती है। "
  "यह ढर्रा इतने व्यापक रूप से सही रहा है कि परिवारों के बजट में भोजन का भाग आज भी इस बात का मोटा मापक माना जाता है कि लोग कितने संपन्न हैं। यह केवल मोटा मापक है: भोजन के दामों में तेज़ वृद्धि भाग को तब भी बढ़ा सकती है जब परिवार अन्य तरीक़ों से अधिक निर्धन न हुए हों, और बाहर अधिक खाने वाले परिवार अपने ख़र्च का अधिक भाग भोजन में गिन सकते हैं।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage states Engel's finding -- the share of spending on food falls as income rises -- explains why, and adds that the share is only a rough measure of well-being, since food prices and eating out can move it. "
   "It says richer families spend more on food in money terms, not less; it calls the share a useful gauge, though rough; and it does not say Engel studied only rich families.",
   "परिच्छेद एंगेल की खोज बताता है -- आय बढ़ने पर भोजन पर ख़र्च का भाग घटता है -- समझाता है क्यों, और जोड़ता है कि यह भाग संपन्नता का केवल मोटा माप है, क्योंकि भोजन के दाम और बाहर खाना उसे बदल सकते हैं। "
   "वह कहता है कि धनी परिवार पैसे के रूप में भोजन पर अधिक ख़र्च करते हैं, कम नहीं; वह भाग को उपयोगी, यद्यपि मोटा, मापक कहता है; और वह यह नहीं कहता कि एंगेल ने केवल धनी परिवारों का अध्ययन किया।",
   "crux",
   opts=["Richer families spend less money on food than poorer families do.",
         "The share of food in a budget tells us nothing at all about how well off people are.",
         "The share spent on food falls as incomes rise, a rough sign of well-being.",
         "Engel studied only the budgets of the richest families of his day."],
   opts_hi=["धनी परिवार निर्धन परिवारों से भोजन पर कम पैसा ख़र्च करते हैं।",
            "बजट में भोजन का भाग इस बारे में कुछ भी नहीं बताता कि लोग वास्तव में कितने संपन्न हैं।",
            "आय बढ़ने पर भोजन पर ख़र्च का भाग घटता है, जिससे वह संपन्नता का मोटा संकेत बनता है।",
            "एंगेल ने केवल अपने समय के सबसे धनी परिवारों के बजट का अध्ययन किया।"],
   ans=2, pos=2)
RQ(p, "Inference", "hard", "mcq",
   "In a town, the share of household spending that goes on food rose from 40 to 45 per cent in a year in which food prices jumped sharply. On the passage's reasoning, what can be concluded?",
   "एक नगर में, जिस वर्ष भोजन के दाम तेज़ी से उछले, उस वर्ष परिवारों के ख़र्च में भोजन का भाग 40 से बढ़कर 45 प्रतिशत हो गया। परिच्छेद के तर्क से क्या निष्कर्ष निकाला जा सकता है?",
   "The passage warns that a sharp rise in food prices can raise the food share even when families are no poorer in other ways. So the rise from 40 to 45 per cent does not by itself show that the town's families became poorer. "
   "Concluding that they became poorer, or richer, ignores that warning; and the passage gives no reason to think families began eating less.",
   "परिच्छेद चेताता है कि भोजन के दामों में तेज़ वृद्धि भोजन का भाग तब भी बढ़ा सकती है जब परिवार अन्य तरीक़ों से अधिक निर्धन न हुए हों। इसलिए 40 से 45 प्रतिशत की वृद्धि अपने आप यह नहीं दिखाती कि नगर के परिवार अधिक निर्धन हो गए। "
   "यह निष्कर्ष कि वे अधिक निर्धन, या अधिक धनी, हुए, उस चेतावनी को अनदेखा करता है; और परिच्छेद यह मानने का कोई कारण नहीं देता कि परिवारों ने कम खाना शुरू किया।",
   "a-food-share-that-rose-with-prices",
   opts=["The town's families have certainly become poorer over the year.",
         "The town's families have certainly become richer over the year.",
         "The families of the town have begun to eat less food than before.",
         "The rise alone does not show that the families became poorer."],
   opts_hi=["नगर के परिवार वर्ष भर में निश्चित रूप से अधिक निर्धन हो गए हैं।",
            "नगर के परिवार वर्ष भर में निश्चित रूप से अधिक धनी हो गए हैं।",
            "नगर के परिवारों ने पहले से कम भोजन करना शुरू कर दिया है।",
            "केवल यह वृद्धि नहीं दिखाती कि नगर के परिवार अधिक निर्धन हो गए।"],
   ans=3, pos=3)

# ------------------------------------------------------------------ P08 the case for protecting infant industries (3)
p = passage("p08",
  "A young industry in a poor country may be unable to compete with long-established firms abroad, not because it could never be efficient, but because it has not yet had time to learn -- to train its workers, find its suppliers and bring its costs down. Writers such as Alexander Hamilton in the United States and Friedrich List in Germany argued that such 'infant industries' deserve protection from imports for a while, until they can stand on their own. "
  "The argument is sound in principle but hard to apply. Protection is easier to grant than to withdraw: the firms it shelters have every reason to say they are not ready yet, and the longer they are shielded, the less they may need to improve. An infant industry that never grows up costs consumers dearly for as long as the shelter lasts. Protection works best when it is limited in time and tied to clear tests of progress.",
  "किसी निर्धन देश का एक नया उद्योग विदेश की लंबे समय से स्थापित फ़र्मों से प्रतिस्पर्धा करने में असमर्थ हो सकता है, इसलिए नहीं कि वह कभी कुशल नहीं हो सकता, बल्कि इसलिए कि उसे अभी सीखने का समय नहीं मिला -- अपने कामगारों को प्रशिक्षित करने, अपने आपूर्तिकर्ता खोजने और अपनी लागत घटाने का। संयुक्त राज्य में अलेक्ज़ेंडर हैमिल्टन और जर्मनी में फ़्रीड्रिख़ लिस्ट जैसे लेखकों ने तर्क दिया कि ऐसे 'शिशु उद्योग' कुछ समय के लिए आयात से संरक्षण के पात्र हैं, जब तक वे अपने पैरों पर खड़े न हो सकें। "
  "यह तर्क सिद्धांत में ठीक है पर लागू करना कठिन। संरक्षण देना वापस लेने से आसान है: जिन फ़र्मों को वह आश्रय देता है उनके पास यह कहने का हर कारण है कि वे अभी तैयार नहीं, और जितना अधिक समय वे बचाई जाती हैं, उतनी ही कम उन्हें सुधरने की आवश्यकता पड़ सकती है। जो शिशु उद्योग कभी बड़ा नहीं होता, वह आश्रय जितने समय तक रहे उतने समय उपभोक्ताओं को महँगा पड़ता है। संरक्षण सबसे अच्छा तब काम करता है जब वह समय में सीमित हो और प्रगति की स्पष्ट कसौटियों से जुड़ा हो।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage accepts the case for protecting young industries while they learn, but warns that protection is hard to withdraw and can stop firms improving, so it should be limited in time and tied to tests of progress. "
   "It calls the argument sound in principle, so it does not reject all protection; it does not say young industries can never become efficient; and it does not recommend permanent protection.",
   "परिच्छेद नए उद्योगों को सीखने के समय संरक्षण देने के पक्ष को स्वीकार करता है, पर चेताता है कि संरक्षण वापस लेना कठिन है और फ़र्मों को सुधरने से रोक सकता है, इसलिए उसे समय में सीमित और प्रगति की कसौटियों से जुड़ा होना चाहिए। "
   "वह तर्क को सिद्धांत में ठीक कहता है, इसलिए हर संरक्षण को ख़ारिज नहीं करता; वह यह नहीं कहता कि नए उद्योग कभी कुशल नहीं बन सकते; और वह स्थायी संरक्षण की सलाह नहीं देता।",
   "crux",
   opts=["A young industry may deserve protection, but only for a time and with tests of progress.",
         "Every form of protection from imports does more harm than good and should be given up.",
         "Young industries in poor countries can never become as efficient as firms abroad.",
         "Once granted, protection for a young industry should be kept for as long as its firms ask."],
   opts_hi=["नए उद्योग को संरक्षण उचित हो सकता है, पर केवल कुछ समय और प्रगति की कसौटियों पर।",
            "आयात से संरक्षण का हर रूप लाभ से अधिक हानि करता है और इसलिए छोड़ दिया जाना चाहिए।",
            "निर्धन देशों के नए उद्योग कभी विदेश की फ़र्मों जितने कुशल नहीं बन सकते।",
            "एक बार दिया गया संरक्षण तब तक बनाए रखा जाए जब तक उसकी फ़र्में माँगें।"],
   ans=0, pos=0)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Neither is valid. 1 goes beyond the passage: it argues that a young industry may be inefficient because it has not yet had time to learn, not that every protected industry will in time become efficient -- it warns that some never grow up. "
   "2 also goes too far: the passage says an infant industry that never grows up costs consumers dearly while protected, but it does not say consumers gain nothing from protection that works.",
   "कोई भी वैध नहीं। 1 परिच्छेद से आगे जाता है: वह तर्क देता है कि कोई नया उद्योग इसलिए अकुशल हो सकता है कि उसे अभी सीखने का समय नहीं मिला, यह नहीं कि हर संरक्षित उद्योग समय के साथ कुशल हो जाएगा -- वह चेताता है कि कुछ कभी बड़े नहीं होते। "
   "2 भी बहुत आगे जाता है: परिच्छेद कहता है कि कभी बड़ा न होने वाला शिशु उद्योग संरक्षण के दौरान उपभोक्ताओं को महँगा पड़ता है, पर यह नहीं कहता कि सफल संरक्षण से उपभोक्ताओं को कुछ नहीं मिलता।",
   "conclusions",
   st=["Any industry that is protected from imports will, given enough time, become efficient.",
       "Consumers gain nothing at all from protection, even when the protected industry does grow up."],
   st_hi=["आयात से संरक्षित कोई भी उद्योग पर्याप्त समय मिलने पर कुशल हो जाएगा।",
          "उपभोक्ताओं को संरक्षण से कुछ भी नहीं मिलता, तब भी जब संरक्षित उद्योग सचमुच बड़ा हो जाए।"],
   key=3)
RQ(p, "Inference", "medium", "mcq",
   "Why, according to the passage, is protection 'easier to grant than to withdraw'?",
   "परिच्छेद के अनुसार, संरक्षण 'देना वापस लेने से आसान' क्यों है?",
   "The passage says the firms that protection shelters have every reason to say they are not ready yet: those who gain from it press to keep it. "
   "It does not say imports stop entirely, that foreign firms demand protection, or that consumers lobby to keep it.",
   "परिच्छेद कहता है कि जिन फ़र्मों को संरक्षण आश्रय देता है उनके पास यह कहने का हर कारण है कि वे अभी तैयार नहीं: जिन्हें उससे लाभ है वे उसे बनाए रखने का दबाव डालते हैं। "
   "वह यह नहीं कहता कि आयात पूरी तरह रुक जाता है, कि विदेशी फ़र्में संरक्षण माँगती हैं, या कि उपभोक्ता उसे बनाए रखने की पैरवी करते हैं।",
   "why-protection-is-hard-to-withdraw",
   opts=["Foreign firms ask the government to keep the protection in place for them.",
         "The firms it shelters have every reason to claim they are not ready yet.",
         "Consumers press the government to keep protection because prices then fall.",
         "Once protection begins, no imports at all can ever enter the country again."],
   opts_hi=["विदेशी फ़र्में सरकार से अपने लिए संरक्षण बनाए रखने को कहती हैं।",
            "आश्रित फ़र्मों के पास यह कहने का हर कारण है कि वे अभी तैयार नहीं।",
            "उपभोक्ता सरकार पर संरक्षण बनाए रखने का दबाव डालते हैं क्योंकि तब दाम घटते हैं।",
            "संरक्षण शुरू होने के बाद देश में फिर कभी कोई आयात प्रवेश नहीं कर सकता।"],
   ans=1, pos=1)

# ------------------------------------------------------------------ P09 languages that die (2)
p = passage("p09",
  "Of the roughly 7,000 languages spoken in the world, a large share are counted as endangered, many of them by only a few thousand speakers. A language rarely dies because its speakers are killed; more often its speakers' children stop learning it, because another language seems more useful for school and work. A language can then die even while thousands of adults still speak it, once none of them passes it on. "
  "That is why the number of speakers says less about a language's future than whether children are learning it at home. Decline can be reversed. Hebrew, for centuries a language of prayer and study, became again the everyday tongue of millions, and Welsh has gained young speakers through schools that teach in it.",
  "दुनिया में बोली जाने वाली लगभग 7,000 भाषाओं में से एक बड़ा भाग संकटग्रस्त माना जाता है, उनमें से कई को केवल कुछ हज़ार लोग बोलते हैं। कोई भाषा शायद ही इसलिए मरती है कि उसके बोलने वाले मारे जाते हैं; प्रायः उसके बोलने वालों के बच्चे उसे सीखना छोड़ देते हैं, क्योंकि पढ़ाई और काम के लिए कोई दूसरी भाषा अधिक उपयोगी लगती है। तब कोई भाषा तब भी मर सकती है जब हज़ारों वयस्क उसे बोलते हों, जैसे ही उनमें से कोई उसे आगे न सौंपे। "
  "इसीलिए बोलने वालों की संख्या किसी भाषा के भविष्य के बारे में इससे कम बताती है कि बच्चे उसे घर पर सीख रहे हैं या नहीं। गिरावट उलटी जा सकती है। हिब्रू, जो सदियों तक प्रार्थना और अध्ययन की भाषा रही, फिर से लाखों लोगों की रोज़मर्रा की भाषा बनी, और वेल्श ने उसमें पढ़ाने वाले विद्यालयों के माध्यम से युवा बोलने वाले पाए हैं।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage argues that a language's survival depends above all on whether children learn it at home, not on how many adults speak it, and that decline can be reversed, as Hebrew and Welsh show. "
   "It says languages rarely die because speakers are killed; it presents revival as possible, not hopeless; and it does not say large languages are safe whatever children do.",
   "परिच्छेद तर्क देता है कि किसी भाषा का बचना सबसे अधिक इस पर निर्भर है कि बच्चे उसे घर पर सीखते हैं या नहीं, इस पर नहीं कि कितने वयस्क उसे बोलते हैं, और कि गिरावट उलटी जा सकती है, जैसा हिब्रू और वेल्श दिखाते हैं। "
   "वह कहता है कि भाषाएँ शायद ही बोलने वालों के मारे जाने से मरती हैं; वह पुनरुद्धार को संभव बताता है, निराशाजनक नहीं; और वह यह नहीं कहता कि बड़ी भाषाएँ बच्चे चाहे जो करें, सुरक्षित हैं।",
   "crux",
   opts=["Most languages die because the people who speak them are killed in wars.",
         "Once a language starts to decline, nothing can ever be done to bring it back.",
         "A language spoken by thousands of adults is safe, whatever its children do.",
         "A language lives on mainly if children learn it, and decline can be reversed."],
   opts_hi=["अधिकांश भाषाएँ इसलिए मरती हैं कि उन्हें बोलने वाले युद्धों में मारे जाते हैं।",
            "एक बार किसी भाषा की गिरावट शुरू हो जाए, तो उसे वापस लाने के लिए कभी कुछ नहीं किया जा सकता।",
            "हज़ारों वयस्कों द्वारा बोली जाने वाली भाषा सुरक्षित है, उसके बच्चे चाहे जो करें।",
            "कोई भाषा मुख्यतः तब जीवित रहती है जब बच्चे उसे सीखें, और उसकी गिरावट उलटी जा सकती है।"],
   ans=3, pos=3)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Both are valid. The passage says a language can die even while thousands of adults speak it, once none passes it on, so a smaller language that children still learn may have the better future (1). "
   "And it says children stop learning a language when another seems more useful for school and work, so making a language useful in school -- as Welsh-medium schools did -- can help it survive (2).",
   "दोनों वैध हैं। परिच्छेद कहता है कि कोई भाषा तब भी मर सकती है जब हज़ारों वयस्क उसे बोलते हों, जैसे ही कोई उसे आगे न सौंपे, इसलिए एक छोटी भाषा जिसे बच्चे अब भी सीखते हैं, बेहतर भविष्य रख सकती है (1)। "
   "और वह कहता है कि बच्चे किसी भाषा को तब सीखना छोड़ते हैं जब कोई दूसरी पढ़ाई और काम के लिए अधिक उपयोगी लगे, इसलिए किसी भाषा को विद्यालय में उपयोगी बनाना -- जैसा वेल्श माध्यम के विद्यालयों ने किया -- उसके बचने में सहायता कर सकता है (2)।",
   "conclusions",
   st=["A language with fewer speakers can have a safer future than a larger one that children no longer learn.",
       "Using a language for teaching in schools can help it to survive."],
   st_hi=["कम बोलने वालों वाली भाषा का भविष्य उस बड़ी भाषा से अधिक सुरक्षित हो सकता है जिसे बच्चे अब नहीं सीखते।",
          "विद्यालयों में पढ़ाने के लिए किसी भाषा का उपयोग उसे बचाए रखने में सहायता कर सकता है।"],
   key=2)

# ------------------------------------------------------------------ P10 the basic structure of the Constitution (2)
p = passage("p10",
  "In the Kesavananda Bharati case of 1973, thirteen judges of the Supreme Court heard argument for months and decided, by seven to six, that Parliament may amend any part of the Constitution but may not destroy its basic structure. The judges did not list once and for all what the basic structure contains; features such as judicial review, free and fair elections and the federal character of the State have been named in later cases. "
  "Critics object that the doctrine appears nowhere in the text and gives unelected judges the last word. Its defenders reply that a constitution which a passing majority could rewrite entirely would protect nothing for long. The doctrine, in their view, does not stop change; it stops change that would unmake the Constitution while keeping its name.",
  "1973 के केशवानंद भारती मामले में सर्वोच्च न्यायालय के तेरह न्यायाधीशों ने महीनों तक बहस सुनी और सात के मुक़ाबले छह से निर्णय दिया कि संसद संविधान के किसी भी भाग में संशोधन कर सकती है पर उसकी मूल संरचना को नष्ट नहीं कर सकती। न्यायाधीशों ने यह एक बार में हमेशा के लिए नहीं बताया कि मूल संरचना में क्या-क्या है; न्यायिक पुनरावलोकन, स्वतंत्र और निष्पक्ष चुनाव और राज्य के संघीय स्वरूप जैसी विशेषताएँ बाद के मामलों में बताई गई हैं। "
  "आलोचक आपत्ति करते हैं कि यह सिद्धांत पाठ में कहीं नहीं है और अनिर्वाचित न्यायाधीशों को अंतिम शब्द देता है। इसके समर्थक उत्तर देते हैं कि जिस संविधान को कोई अस्थायी बहुमत पूरी तरह फिर से लिख सके, वह लंबे समय तक कुछ भी नहीं बचाएगा। उनके विचार में यह सिद्धांत परिवर्तन को नहीं रोकता; वह ऐसे परिवर्तन को रोकता है जो संविधान का नाम रखते हुए उसे मिटा दे।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage explains the basic structure doctrine -- Parliament may amend anything but not destroy the Constitution's basic structure -- and sets out both the objection to it and the reply. "
   "It says Parliament may amend any part, so the doctrine does not forbid amendment; the list of basic features was not fixed in 1973; and the passage presents both sides rather than declaring the doctrine wrong.",
   "परिच्छेद मूल संरचना सिद्धांत समझाता है -- संसद कुछ भी संशोधित कर सकती है पर संविधान की मूल संरचना नष्ट नहीं कर सकती -- और उस पर आपत्ति तथा उत्तर दोनों रखता है। "
   "वह कहता है कि संसद किसी भी भाग में संशोधन कर सकती है, इसलिए सिद्धांत संशोधन को वर्जित नहीं करता; मूल विशेषताओं की सूची 1973 में तय नहीं हुई; और परिच्छेद सिद्धांत को ग़लत घोषित करने के बजाय दोनों पक्ष रखता है।",
   "crux",
   opts=["Since 1973, Parliament has not been allowed to amend any part of the Constitution.",
         "Parliament may amend, but not destroy, the basic structure -- a contested limit.",
         "The Kesavananda Bharati judges listed every feature of the basic structure in full.",
         "The basic structure doctrine has been shown to be wrong because it is not in the text."],
   opts_hi=["1973 से संसद को संविधान के किसी भी भाग में संशोधन की अनुमति नहीं है।",
            "संसद संशोधन कर सकती है, पर मूल संरचना नष्ट नहीं -- एक विवादित सीमा।",
            "केशवानंद भारती मामले के न्यायाधीशों ने मूल संरचना की हर विशेषता पूरी तरह सूचीबद्ध की।",
            "मूल संरचना सिद्धांत ग़लत सिद्ध हो चुका है क्योंकि वह पाठ में नहीं है।"],
   ans=1, pos=1)
RQ(p, "Inference", "hard", "mcq",
   "According to the defenders of the doctrine as the passage presents them, which one of the following amendments would the doctrine forbid?",
   "परिच्छेद में प्रस्तुत सिद्धांत के समर्थकों के अनुसार, निम्नलिखित में से किस संशोधन को यह सिद्धांत वर्जित करेगा?",
   "The defenders say the doctrine stops change that would unmake the Constitution while keeping its name. An amendment that kept elections on paper but let the government postpone them indefinitely would destroy free and fair elections, a feature named as basic. "
   "Changing the number of judges, adding a new language to a schedule or raising the age of retirement changes the Constitution without unmaking it.",
   "समर्थक कहते हैं कि सिद्धांत ऐसे परिवर्तन को रोकता है जो संविधान का नाम रखते हुए उसे मिटा दे। जो संशोधन चुनावों को काग़ज़ पर रखे पर सरकार को उन्हें अनिश्चित काल तक टालने दे, वह स्वतंत्र और निष्पक्ष चुनावों को नष्ट करेगा, जिसे मूल विशेषता बताया गया है। "
   "न्यायाधीशों की संख्या बदलना, किसी अनुसूची में नई भाषा जोड़ना या सेवानिवृत्ति की आयु बढ़ाना संविधान को बदलता है, मिटाता नहीं।",
   "an-amendment-the-doctrine-forbids",
   opts=["An amendment that raises the number of judges of the Supreme Court",
         "An amendment that adds a new language to the list in a schedule",
         "An amendment that lets a government put off elections indefinitely",
         "An amendment that raises the age at which judges retire"],
   opts_hi=["सर्वोच्च न्यायालय के न्यायाधीशों की संख्या बढ़ाने वाला संशोधन",
            "किसी अनुसूची की सूची में नई भाषा जोड़ने वाला संशोधन",
            "सरकार को चुनाव अनिश्चित काल तक टालने देने वाला संशोधन",
            "न्यायाधीशों की सेवानिवृत्ति की आयु बढ़ाने वाला संशोधन"],
   ans=2, pos=2)
