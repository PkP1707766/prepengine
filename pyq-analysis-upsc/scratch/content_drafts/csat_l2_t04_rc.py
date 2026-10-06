# -*- coding: utf-8 -*-
"""CSAT Level 2 · Test 4 -- Reading Comprehension: 10 original passages, 28 items (8 x 3, 2 x 2).

Themes, none used in Tests 1-3: women in paid work, curiosity-driven research, software and jobs, light at
night, migration and remittances, processed food and taxes, plantations counted as forest, cyclone warnings,
museum objects and their return, and dairy cooperatives. Item types: main idea 7, inference 8, assumption 5,
tone 1, specific detail 4, best summary 3. Options are named by content in every explanation."""
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

# ------------------------------------------------------------------ P01 women in paid work (3)
p = passage("p01",
  "For many years India's economy grew quickly while the share of women in paid work fell, and only recently has it begun to recover. Part of the explanation is welcome: more young women are in school and college "
  "rather than at work. But much of it is not. Where families grow richer, a woman's work outside the home can come to be seen as a sign that the household needs the money, and she withdraws from it. "
  "Jobs close to home are few, and the journey to distant ones is long and often unsafe. And the unpaid work of the household falls on her whatever she earns. Measures that make work possible -- "
  "safe transport, childcare, jobs within reach -- may do more than campaigns to change attitudes alone.",
  "कई वर्षों तक भारत की अर्थव्यवस्था तेज़ी से बढ़ी जबकि वेतन वाले काम में महिलाओं का हिस्सा घटता गया, और हाल में ही उसमें सुधार शुरू हुआ है। इसकी एक व्याख्या स्वागत योग्य है: अधिक युवतियाँ काम के बजाय विद्यालय और कॉलेज में हैं। "
  "पर अधिकांश व्याख्या ऐसी नहीं है। जहाँ परिवार अमीर होते हैं, वहाँ घर के बाहर महिला के काम को इस बात का संकेत माना जाने लगता है कि परिवार को पैसे की ज़रूरत है, और वह काम छोड़ देती है। "
  "घर के पास नौकरियाँ कम हैं, और दूर की नौकरियों तक का सफ़र लंबा और प्रायः असुरक्षित है। और घर का बिना वेतन वाला काम उस पर ही पड़ता है, वह चाहे जितना कमाए। जो उपाय काम को संभव बनाते हैं -- "
  "सुरक्षित परिवहन, बच्चों की देखभाल, पहुँच के भीतर नौकरियाँ -- वे केवल सोच बदलने के अभियानों से अधिक कर सकते हैं।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage grants one welcome cause, more women studying, names the unwelcome ones -- status, distance, unsafe travel, unpaid housework -- and ends by favouring measures that make work possible over attitude campaigns alone. "
   "It says education explains only 'part' of the fall; it says richer families 'can come to' see women's work as a sign of need, not that they always forbid it; and it says campaigns alone may do less, not that they are useless.",
   "परिच्छेद एक स्वागत योग्य कारण, अधिक महिलाओं का पढ़ना, मानता है, अस्वागत योग्य कारण गिनाता है -- प्रतिष्ठा, दूरी, असुरक्षित सफ़र, बिना वेतन का घरेलू काम -- और अंत में केवल सोच बदलने के अभियानों की तुलना में काम को संभव बनाने वाले उपायों को बेहतर बताता है। "
   "वह कहता है कि शिक्षा गिरावट का केवल 'एक भाग' समझाती है; वह कहता है कि अमीर परिवार महिला के काम को ज़रूरत का संकेत 'मानने लगते' हैं, यह नहीं कि वे सदा उसे रोकते हैं; और वह कहता है कि अकेले अभियान कम कर सकते हैं, यह नहीं कि वे बेकार हैं।",
   "crux",
   opts=["Making work practical for women may help more than attitude campaigns alone.",
         "Women have left paid work mainly because more of them are now studying in colleges.",
         "Families that grow richer always forbid women to work outside their homes for pay.",
         "Campaigns to change attitudes towards working women are of no use."],
   opts_hi=["महिलाओं के लिए काम को व्यावहारिक बनाना केवल अभियानों से अधिक मदद कर सकता है।",
            "महिलाओं ने वेतन वाला काम मुख्यतः इसलिए छोड़ा है क्योंकि उनमें से अधिक अब कॉलेजों में पढ़ रही हैं।",
            "जो परिवार अमीर होते हैं, वे महिलाओं को वेतन के लिए घर के बाहर काम करने से सदा रोकते हैं।",
            "कामकाजी महिलाओं के प्रति सोच बदलने के अभियान किसी काम के नहीं हैं।"],
   ans=0, pos=3)
RQ(p, "Inference", "hard", "sc", INFER, INFER_HI,
   "1 and 2 follow. Where families grow richer, women may withdraw from paid work, so higher household income does not by itself draw them in (1); distant jobs are hard to reach because the journey is long and unsafe, "
   "so safer transport could help (2). 3 contradicts the passage: the unpaid work of the household falls on a woman 'whatever she earns'.",
   "1 और 2 निकलते हैं। जहाँ परिवार अमीर होते हैं, वहाँ महिलाएँ वेतन वाला काम छोड़ सकती हैं, इसलिए परिवार की बढ़ी आय अपने-आप उन्हें काम में नहीं लाती (1); दूर की नौकरियों तक पहुँचना कठिन है क्योंकि सफ़र लंबा और असुरक्षित है, "
   "इसलिए सुरक्षित परिवहन मदद कर सकता है (2)। 3 परिच्छेद का खंडन करता है: घर का बिना वेतन वाला काम महिला पर ही पड़ता है, 'वह चाहे जितना कमाए'।",
   "inferences",
   st=["A rise in household income does not by itself bring more women into paid work.",
       "Safer transport could help some women take up jobs further from home.",
       "Women who earn wages are freed from the unpaid work of the household."],
   st_hi=["परिवार की आय बढ़ने भर से अधिक महिलाएँ वेतन वाले काम में नहीं आतीं।",
          "सुरक्षित परिवहन कुछ महिलाओं को घर से दूर की नौकरियाँ करने में मदद कर सकता है।",
          "वेतन कमाने वाली महिलाएँ घर के बिना वेतन वाले काम से मुक्त हो जाती हैं।"],
   opts=["1 only", "2 and 3 only", "1 and 2 only", "1, 2 and 3"], key=2)
RQ(p, "Assumption", "hard", "s2", ASSUME, ASSUME_HI,
   "Only 1 is assumed. Recommending safe transport, childcare and nearby jobs makes sense only if there are women who would take up paid work once such obstacles were removed. "
   "2 is neither needed nor suggested: the passage treats study as a welcome reason for young women to be out of the workforce, not as a lifelong bar.",
   "केवल 1 पूर्वधारणा है। सुरक्षित परिवहन, बच्चों की देखभाल और पास की नौकरियों की सिफ़ारिश तभी अर्थपूर्ण है जब ऐसी महिलाएँ हों जो ये बाधाएँ हटने पर वेतन वाला काम करेंगी। "
   "2 न आवश्यक है न सुझाया गया है: परिच्छेद पढ़ाई को युवतियों के कार्यबल से बाहर होने का स्वागत योग्य कारण मानता है, जीवन भर की रुकावट नहीं।",
   "assumptions",
   st=["Some women who are not in paid work would take it up if the practical obstacles were removed.",
       "Studying keeps women out of paid work for the rest of their lives."],
   st_hi=["वेतन वाले काम से बाहर कुछ महिलाएँ व्यावहारिक बाधाएँ हटने पर उसे अपना लेंगी।",
          "पढ़ाई महिलाओं को जीवन भर के लिए वेतन वाले काम से बाहर रखती है।"],
   key=0)

# ------------------------------------------------------------------ P02 curiosity-driven research (3)
p = passage("p02",
  "Many of the technologies we now take for granted grew out of research that had no use in mind. The physics that explains how electrons move through solids was worked out long before anyone built a transistor; "
  "the study of bacteria living in hot springs gave biology a heat-resistant enzyme that made possible the standard test for copying DNA. Governments under pressure to show returns prefer to fund research aimed at a clear goal, "
  "and such research has its place. But a portfolio made up only of projects that promise results will mostly deliver what was expected. The discoveries that change a field tend to come from questions asked "
  "out of curiosity, and they keep to no timetable.",
  "आज हम जिन तकनीकों को सहज मान लेते हैं, उनमें से कई ऐसे शोध से निकलीं जिसके पीछे कोई उपयोग सोचा नहीं गया था। ठोस पदार्थों में इलेक्ट्रॉन कैसे चलते हैं, इसकी व्याख्या करने वाली भौतिकी ट्रांज़िस्टर बनने से बहुत पहले विकसित हो चुकी थी; "
  "गर्म झरनों में रहने वाले जीवाणुओं के अध्ययन ने जीवविज्ञान को एक ऊष्मा-सहिष्णु एंज़ाइम दिया जिसने DNA की प्रतियाँ बनाने का मानक परीक्षण संभव किया। परिणाम दिखाने के दबाव में सरकारें स्पष्ट लक्ष्य वाले शोध को धन देना पसंद करती हैं, "
  "और ऐसे शोध का अपना स्थान है। पर केवल परिणाम का वादा करने वाली परियोजनाओं से बना संग्रह अधिकतर वही देगा जिसकी अपेक्षा थी। किसी क्षेत्र को बदल देने वाली खोजें प्रायः जिज्ञासा से पूछे गए प्रश्नों से आती हैं, "
  "और वे किसी समय-सारणी के अनुसार नहीं आतीं।")
RQ(p, "Author's Tone", "hard", "mcq",
   "The author's attitude towards research aimed at a clear goal is best described as:",
   "स्पष्ट लक्ष्य वाले शोध के प्रति लेखक का दृष्टिकोण सबसे अच्छी तरह कैसा बताया जा सकता है?",
   "The author says that goal-directed research 'has its place' but warns that a portfolio made only of such projects 'will mostly deliver what was expected' -- acceptance with a caution. "
   "The passage never calls it a waste, does not present it as the route to discovery (curiosity is), and is plainly not indifferent to the choice.",
   "लेखक कहता है कि लक्ष्य वाले शोध का 'अपना स्थान है', पर चेताता है कि केवल ऐसी परियोजनाओं से बना संग्रह 'अधिकतर वही देगा जिसकी अपेक्षा थी' -- सावधानी के साथ स्वीकृति। "
   "परिच्छेद उसे कहीं व्यर्थ नहीं कहता, उसे खोज का रास्ता नहीं बताता (वह रास्ता जिज्ञासा है), और इस चुनाव के प्रति स्पष्ट रूप से उदासीन भी नहीं है।",
   "tone",
   opts=["accepting of it, but wary of funding nothing else",
         "dismissive of it as a waste of the public's money",
         "enthusiastic about it as the surest route to discovery",
         "quite indifferent to whether governments choose to fund it"],
   opts_hi=["उसे स्वीकार करने वाला, पर केवल उसी को धन देने के प्रति सावधान",
            "उसे जनता के पैसे की बर्बादी मानकर ख़ारिज करने वाला",
            "उसे खोज का सबसे पक्का रास्ता मानकर उत्साहित",
            "इस बात के प्रति पूरी तरह उदासीन कि सरकारें उसे धन दें या न दें"],
   ans=0, pos=1)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Only 1 is valid: the transistor and the DNA-copying enzyme both grew out of research 'that had no use in mind'. "
   "2 contradicts the passage, which says that research aimed at a clear goal 'has its place'.",
   "केवल 1 वैध है: ट्रांज़िस्टर और DNA की प्रतियाँ बनाने वाला एंज़ाइम, दोनों ऐसे शोध से निकले 'जिसके पीछे कोई उपयोग सोचा नहीं गया था'। "
   "2 परिच्छेद का खंडन करता है, जो कहता है कि स्पष्ट लक्ष्य वाले शोध का 'अपना स्थान है'।",
   "conclusions",
   st=["Research that seemed to have no use when it was done can later prove valuable.",
       "Governments should stop funding research that is aimed at specific goals."],
   st_hi=["जो शोध किए जाते समय बेकार लगा, वह बाद में मूल्यवान सिद्ध हो सकता है।",
          "सरकारों को विशिष्ट लक्ष्यों वाले शोध को धन देना बंद कर देना चाहिए।"],
   key=0)
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage's two examples show useful technology growing out of research with no aim in view, and it concludes that the discoveries that change a field come from curiosity and keep to no timetable, so such research needs room "
   "alongside goal-directed work. It does not say that most technologies were accidents; it grants that goal-directed research has its place; and electrons and bacteria are its examples, not a list of what to fund.",
   "परिच्छेद के दोनों उदाहरण दिखाते हैं कि उपयोगी तकनीक बिना किसी लक्ष्य वाले शोध से निकली, और वह निष्कर्ष निकालता है कि किसी क्षेत्र को बदलने वाली खोजें जिज्ञासा से आती हैं और किसी समय-सारणी के अनुसार नहीं आतीं, इसलिए ऐसे शोध को "
   "लक्ष्य वाले काम के साथ जगह मिलनी चाहिए। वह यह नहीं कहता कि अधिकांश तकनीकें संयोग थीं; वह मानता है कि लक्ष्य वाले शोध का अपना स्थान है; और इलेक्ट्रॉन और जीवाणु उसके उदाहरण हैं, धन देने की सूची नहीं।",
   "crux",
   opts=["Curiosity-driven research deserves support, since the biggest discoveries cannot be planned.",
         "Most of the technologies we use today were invented by accident rather than by careful design.",
         "Research aimed at clear goals never produces anything that turns out to be useful.",
         "Governments should fund only research on electrons and on bacteria."],
   opts_hi=["जिज्ञासा वाले शोध को समर्थन चाहिए, क्योंकि सबसे बड़ी खोजों की योजना नहीं बन सकती।",
            "आज हम जिन तकनीकों का उपयोग करते हैं, उनमें से अधिकांश सोची-समझी रचना के बजाय संयोग से बनीं।",
            "स्पष्ट लक्ष्य वाला शोध कभी कुछ ऐसा नहीं देता जो उपयोगी सिद्ध हो।",
            "सरकारों को केवल इलेक्ट्रॉन और जीवाणुओं पर शोध को धन देना चाहिए।"],
   ans=0, pos=2)

# ------------------------------------------------------------------ P03 software and jobs (3)
p = passage("p03",
  "Each wave of automation has brought fears of mass unemployment, and each time new kinds of work have appeared. Software that can write and summarise text differs in one respect: it reaches into tasks done by clerks, "
  "translators and junior professionals, work once thought safe because it called for judgement. Yet a task is not a job. Most jobs bundle many tasks, and when software takes over some of them, the people who do the rest "
  "may become more productive rather than redundant, as bank tellers did when cash machines arrived and they turned to advising customers. The risk is real for those whose work is a single routine task, and it falls "
  "hardest on those least able to retrain. Whether the gains are shared depends less on the technology than on how quickly skills, rules and safety nets adapt.",
  "स्वचालन की हर लहर ने बड़े पैमाने पर बेरोज़गारी का डर पैदा किया है, और हर बार नए प्रकार के काम सामने आए हैं। पाठ लिखने और सारांश बनाने वाला सॉफ़्टवेयर एक बात में अलग है: वह क्लर्कों, "
  "अनुवादकों और कनिष्ठ पेशेवरों के उन कामों तक पहुँचता है जिन्हें कभी सुरक्षित माना जाता था क्योंकि उनमें विवेक लगता था। फिर भी एक कार्य कोई नौकरी नहीं है। अधिकांश नौकरियों में कई कार्य होते हैं, और जब सॉफ़्टवेयर उनमें से कुछ ले लेता है, "
  "तो बाक़ी कार्य करने वाले लोग बेकार होने के बजाय अधिक उत्पादक हो सकते हैं, जैसे बैंक टेलर हुए जब नक़दी मशीनें आईं और वे ग्राहकों को सलाह देने लगे। जिनका काम एक ही नियमित कार्य है, उनके लिए ख़तरा वास्तविक है, और "
  "वह सबसे अधिक उन पर पड़ता है जो दोबारा प्रशिक्षण लेने में सबसे कम सक्षम हैं। लाभ सबमें बँटेंगे या नहीं, यह तकनीक से कम और इस बात पर अधिक निर्भर है कि कौशल, नियम और सुरक्षा-जाल कितनी जल्दी ढलते हैं।")
RQ(p, "Best Summary", "medium", "mcq", MSG, MSG_HI,
   "The passage separates tasks from jobs, expects many jobs to change rather than vanish, names those most at risk, and makes shared gains depend on how fast skills, rules and safety nets adapt. "
   "It does not say clerks and translators will have no work; it says past fears of mass unemployment proved wrong; and it says the bank tellers turned to advising customers rather than losing their jobs.",
   "परिच्छेद कार्यों को नौकरियों से अलग करता है, उम्मीद करता है कि कई नौकरियाँ ख़त्म होने के बजाय बदलेंगी, सबसे अधिक ख़तरे वालों का नाम लेता है, और लाभों के बँटने को इस पर निर्भर बताता है कि कौशल, नियम और सुरक्षा-जाल कितनी जल्दी ढलते हैं। "
   "वह यह नहीं कहता कि क्लर्कों और अनुवादकों के पास कोई काम नहीं बचेगा; वह कहता है कि बेरोज़गारी के पिछले डर ग़लत निकले; और वह कहता है कि बैंक टेलर नौकरी खोने के बजाय ग्राहकों को सलाह देने लगे।",
   "message",
   opts=["AI is likelier to reshape jobs than end them, but sharing its gains needs skills and safety nets.",
         "Software that writes text will leave no work at all for clerks, translators and junior professionals.",
         "Fears that automation will cause mass unemployment have always turned out to be correct in the end.",
         "Cash machines put most bank tellers out of work, and software will do the same to clerks."],
   opts_hi=["AI नौकरियाँ ख़त्म करने से अधिक बदलेगा, पर लाभ बाँटने के लिए कौशल और सुरक्षा-जाल चाहिए।",
            "पाठ लिखने वाला सॉफ़्टवेयर क्लर्कों, अनुवादकों और कनिष्ठ पेशेवरों के लिए कोई भी काम नहीं छोड़ेगा।",
            "स्वचालन से बड़े पैमाने पर बेरोज़गारी के डर अंततः सदा सही सिद्ध हुए हैं।",
            "नक़दी मशीनों ने अधिकांश बैंक टेलरों की नौकरी छीन ली, और सॉफ़्टवेयर क्लर्कों के साथ भी यही करेगा।"],
   ans=0, pos=0)
RQ(p, "Specific Detail", "medium", "mcq",
   "According to the passage, what did bank tellers do when cash machines arrived?",
   "परिच्छेद के अनुसार, नक़दी मशीनें आने पर बैंक टेलरों ने क्या किया?",
   "The passage says that the tellers 'turned to advising customers' when cash machines took over the handling of cash, and so became more productive rather than redundant. "
   "Running the machines, leaving banking and opposing the machines are none of them mentioned.",
   "परिच्छेद कहता है कि जब नक़दी मशीनों ने नक़दी का काम सँभाल लिया तो टेलर 'ग्राहकों को सलाह देने लगे', और इस तरह बेकार होने के बजाय अधिक उत्पादक हो गए। "
   "मशीनें चलाना, बैंकिंग छोड़ना और मशीनों का विरोध करना -- इनमें से किसी का उल्लेख नहीं है।",
   "detail",
   opts=["They turned to advising customers.",
         "They operated the new machines.",
         "They moved to jobs outside banking.",
         "They opposed the use of the machines."],
   opts_hi=["वे ग्राहकों को सलाह देने लगे।",
            "वे नई मशीनें चलाने लगे।",
            "वे बैंकिंग के बाहर की नौकरियों में चले गए।",
            "उन्होंने मशीनों के उपयोग का विरोध किया।"],
   ans=0, pos=2)
RQ(p, "Assumption", "hard", "sc", ASSUME, ASSUME_HI,
   "1 and 2 are assumed. The author uses the bank tellers to show what may happen to other workers, which works only if their case is a fair guide (1); and the claim that the people who do the remaining tasks "
   "may become more productive assumes that they can move to those tasks (2). 3 is not assumed: the author says the risk to some workers is real.",
   "1 और 2 पूर्वधारणाएँ हैं। लेखक बैंक टेलरों का उदाहरण यह दिखाने के लिए देता है कि दूसरे कर्मचारियों के साथ क्या हो सकता है, जो तभी काम करता है जब उनका मामला एक उचित मार्गदर्शक हो (1); और यह दावा कि बाक़ी कार्य करने वाले लोग "
   "अधिक उत्पादक हो सकते हैं, मानकर चलता है कि वे उन कार्यों की ओर जा सकते हैं (2)। 3 पूर्वधारणा नहीं है: लेखक कहता है कि कुछ कर्मचारियों के लिए ख़तरा वास्तविक है।",
   "assumptions",
   st=["The experience of bank tellers is a fair guide to what may happen to other workers.",
       "Workers can shift to their remaining tasks when some of their tasks are automated.",
       "New technology always creates more jobs than it destroys."],
   st_hi=["बैंक टेलरों का अनुभव इस बात का उचित संकेत है कि दूसरे कर्मचारियों के साथ क्या हो सकता है।",
          "जब कर्मचारियों के कुछ कार्य स्वचालित हो जाते हैं, तो वे अपने बाक़ी कार्यों की ओर जा सकते हैं।",
          "नई तकनीक जितनी नौकरियाँ ख़त्म करती है, उससे सदा अधिक पैदा करती है।"],
   opts=["1 only", "2 and 3 only", "1, 2 and 3", "1 and 2 only"], key=3)

# ------------------------------------------------------------------ P04 light at night (2)
p = passage("p04",
  "For most of human history, a clear night revealed thousands of stars. Today more than a third of humanity lives where the night sky is too bright for the Milky Way to be seen. Artificial light at night does more than hide the stars. "
  "Migrating birds that steer by the stars are drawn off course by lit buildings; insects circle street lamps until they die; and in people, bright light late in the evening delays the release of the hormone "
  "that prepares the body for sleep. Unlike most pollution, this kind can be undone at once: a lamp that is shielded to point downwards, dimmed after midnight or simply switched off leaves nothing behind.",
  "मानव इतिहास के अधिकांश समय में साफ़ रात हज़ारों तारे दिखाती थी। आज मानवता का एक-तिहाई से अधिक भाग ऐसी जगहों पर रहता है जहाँ रात का आकाश इतना उजला है कि आकाशगंगा दिखाई नहीं देती। रात की कृत्रिम रोशनी तारों को छिपाने से अधिक करती है। "
  "तारों के सहारे दिशा तय करने वाले प्रवासी पक्षी रोशन इमारतों से भटक जाते हैं; कीड़े सड़क की बत्तियों के चारों ओर तब तक चक्कर लगाते हैं जब तक मर न जाएँ; और मनुष्यों में देर शाम की तेज़ रोशनी उस हॉर्मोन के निकलने में देरी करती है "
  "जो शरीर को नींद के लिए तैयार करता है। अधिकांश प्रदूषण के विपरीत, इसे तुरंत मिटाया जा सकता है: नीचे की ओर रोशनी डालने के लिए ढकी गई, आधी रात के बाद मद्धम की गई या बस बुझा दी गई बत्ती अपने पीछे कुछ नहीं छोड़ती।")
RQ(p, "Main Idea", "easy", "mcq", CRUX, CRUX_HI,
   "The passage lists the harms of light at night -- to birds, insects and human sleep -- and ends on its distinctive feature: it can be undone at once. "
   "It asks for shielded, dimmed or switched-off lamps, not for their removal everywhere; it shows harms well beyond star-gazing; and it compares light with other pollution only in how quickly it can be reversed.",
   "परिच्छेद रात की रोशनी की हानियाँ गिनाता है -- पक्षियों, कीड़ों और मनुष्य की नींद को -- और उसकी विशेष बात पर समाप्त होता है: उसे तुरंत मिटाया जा सकता है। "
   "वह ढकी, मद्धम या बुझाई गई बत्तियाँ माँगता है, उन्हें हर जगह से हटाना नहीं; वह तारे देखने से कहीं आगे की हानियाँ दिखाता है; और वह रोशनी की तुलना दूसरे प्रदूषण से केवल इस बात में करता है कि उसे कितनी जल्दी पलटा जा सकता है।",
   "crux",
   opts=["Night lighting harms wildlife and sleep, yet unlike most pollution it is easily undone.",
         "Street lamps should be removed from all towns and cities so that people can see the stars again.",
         "Light pollution matters only to people who like to look at the stars.",
         "Birds and insects suffer more from light than from any other kind of pollution."],
   opts_hi=["रात की रोशनी जीवों और नींद को हानि देती है, पर दूसरे प्रदूषण के उलट जल्दी मिटती है।",
            "सभी कस्बों और शहरों से सड़क की बत्तियाँ हटा देनी चाहिए ताकि लोग फिर से तारे देख सकें।",
            "प्रकाश प्रदूषण केवल उन लोगों के लिए मायने रखता है जिन्हें तारे देखना पसंद है।",
            "पक्षी और कीड़े किसी भी अन्य प्रदूषण से अधिक रोशनी से पीड़ित होते हैं।"],
   ans=0, pos=3)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Both are valid. A lamp shielded to point downwards 'leaves nothing behind', so shielding cuts the pollution without lasting effects (1). "
   "Bright light late in the evening delays the hormone that prepares the body for sleep, so it can make falling asleep harder (2).",
   "दोनों वैध हैं। नीचे की ओर रोशनी डालने के लिए ढकी बत्ती 'अपने पीछे कुछ नहीं छोड़ती', इसलिए ढकना बिना स्थायी प्रभाव के प्रदूषण घटाता है (1)। "
   "देर शाम की तेज़ रोशनी शरीर को नींद के लिए तैयार करने वाले हॉर्मोन में देरी करती है, इसलिए वह नींद आने को कठिन बना सकती है (2)।",
   "conclusions",
   st=["Shielding lamps to point downwards can reduce light pollution without lasting side effects.",
       "Bright light late in the evening can make it harder for people to fall asleep."],
   st_hi=["बत्तियों को नीचे की ओर रोशनी डालने के लिए ढकना बिना स्थायी दुष्प्रभाव के प्रकाश प्रदूषण घटा सकता है।",
          "देर शाम की तेज़ रोशनी लोगों के लिए सो पाना कठिन बना सकती है।"],
   key=2)

# ------------------------------------------------------------------ P05 migration and remittances (3)
p = passage("p05",
  "Millions of Indians work away from home, in other States or abroad, and the money they send back pays for school fees, houses and medical bills. Remittances arrive even when a village's harvest fails, which makes them "
  "a kind of insurance as well as income. Yet they come at a price paid by those left behind: children who see a parent once a year, old people who manage farms alone, and women who carry the work of two adults. "
  "Migrants themselves often live in crowded rooms, without the support they would have at home, because many of the welfare schemes they are entitled to remain tied to the place where they are registered. "
  "Making entitlements portable, so that they follow the worker, would ease the cost of a movement on which the economy depends.",
  "करोड़ों भारतीय घर से दूर, दूसरे राज्यों में या विदेश में, काम करते हैं, और जो पैसा वे वापस भेजते हैं उससे स्कूल की फ़ीस, मकान और इलाज के बिल चुकते हैं। घर भेजी जाने वाली यह रक़म तब भी आती है जब गाँव की फ़सल नष्ट हो जाए, जिससे वह "
  "आय के साथ-साथ एक तरह का बीमा भी है। फिर भी इसकी क़ीमत पीछे रह गए लोग चुकाते हैं: बच्चे जो साल में एक बार माता या पिता को देखते हैं, बुज़ुर्ग जो अकेले खेती सँभालते हैं, और महिलाएँ जो दो वयस्कों का काम ढोती हैं। "
  "प्रवासी स्वयं प्रायः भीड़ भरे कमरों में रहते हैं, उस सहारे के बिना जो उन्हें घर पर मिलता, क्योंकि जिन कल्याण योजनाओं के वे हक़दार हैं उनमें से कई अब भी उसी स्थान से बँधी हैं जहाँ वे पंजीकृत हैं। "
  "हक़ों को साथ ले जाने योग्य बनाना, ताकि वे कर्मचारी के पीछे-पीछे चलें, उस आवाजाही की लागत घटाएगा जिस पर अर्थव्यवस्था निर्भर है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage values remittances as income and insurance, sets out the costs borne by migrants and their families, and proposes portable entitlements to ease them. "
   "It never argues against migration -- the economy depends on it; it says the money pays for school fees, houses and medical bills; and it does not compare migrants' well-being with that of those left behind.",
   "परिच्छेद घर भेजी गई रक़म को आय और बीमा दोनों के रूप में महत्त्व देता है, प्रवासियों और उनके परिवारों की लागतें बताता है, और उन्हें घटाने के लिए साथ ले जाने योग्य हक़ों का प्रस्ताव करता है। "
   "वह प्रवास के विरुद्ध कहीं तर्क नहीं देता -- अर्थव्यवस्था उस पर निर्भर है; वह कहता है कि यह पैसा स्कूल फ़ीस, मकान और इलाज पर लगता है; और वह प्रवासियों की भलाई की तुलना पीछे रह गए लोगों से नहीं करता।",
   "crux",
   opts=["Remittances help families, but portable entitlements could ease migration's costs.",
         "Migration should be discouraged, because it keeps parents away from their children.",
         "Families spend most of the money they receive from migrants on things they do not need.",
         "Migrants who work far from home are better off than the families they leave behind."],
   opts_hi=["घर भेजी गई रक़म परिवारों की मदद करती है, पर साथ ले जाने योग्य हक़ प्रवास की लागत घटा सकते हैं।",
            "प्रवास को हतोत्साहित करना चाहिए, क्योंकि वह माता-पिता को उनके बच्चों से दूर रखता है।",
            "परिवार प्रवासियों से मिले पैसे का अधिकांश भाग उन चीज़ों पर ख़र्च करते हैं जिनकी उन्हें ज़रूरत नहीं।",
            "घर से दूर काम करने वाले प्रवासी पीछे छोड़े गए अपने परिवारों से बेहतर स्थिति में हैं।"],
   ans=0, pos=0)
RQ(p, "Inference", "hard", "sc", INFER, INFER_HI,
   "1 and 3 follow. Remittances 'arrive even when a village's harvest fails' (1), and many welfare schemes 'remain tied to the place where they are registered', so migrants working elsewhere may be unable to use them (3). "
   "2 contradicts the passage, which names school fees, houses and medical bills.",
   "1 और 3 निकलते हैं। रक़म 'तब भी आती है जब गाँव की फ़सल नष्ट हो जाए' (1), और कई कल्याण योजनाएँ 'उसी स्थान से बँधी हैं जहाँ वे पंजीकृत हैं', इसलिए कहीं और काम करने वाले प्रवासी उनका उपयोग न कर पाएँ, ऐसा हो सकता है (3)। "
   "2 परिच्छेद का खंडन करता है, जो स्कूल फ़ीस, मकान और इलाज के बिलों का नाम लेता है।",
   "inferences",
   st=["Remittances can help a family get through a year in which its crops fail.",
       "Remittances are spent mostly on goods that do not last.",
       "Some migrants cannot use the benefits they are entitled to while they work away from home."],
   st_hi=["घर भेजी गई रक़म किसी परिवार को उस वर्ष से निकलने में मदद कर सकती है जिसमें उसकी फ़सल नष्ट हो जाए।",
          "घर भेजी गई रक़म अधिकतर ऐसी चीज़ों पर ख़र्च होती है जो टिकती नहीं।",
          "कुछ प्रवासी घर से दूर काम करते समय उन लाभों का उपयोग नहीं कर पाते जिनके वे हक़दार हैं।"],
   opts=["1 only", "1 and 3 only", "2 and 3 only", "1, 2 and 3"], key=1)
RQ(p, "Assumption", "hard", "s2", ASSUME, ASSUME_HI,
   "Neither is assumed. The case for portable entitlements needs nothing about whether migrants prefer working far from home (1), and nothing in the argument depends on remittances being a family's only income (2) -- "
   "the passage calls them insurance precisely because the farm's income can fail.",
   "कोई भी पूर्वधारणा नहीं है। साथ ले जाने योग्य हक़ों के पक्ष को इस बात की ज़रूरत नहीं कि प्रवासी घर से दूर काम करना पसंद करते हैं या नहीं (1), और तर्क की कोई बात इस पर निर्भर नहीं कि घर भेजी गई रक़म परिवार की एकमात्र आय है (2) -- "
   "परिच्छेद उसे बीमा ही इसलिए कहता है कि खेती की आय नष्ट हो सकती है।",
   "assumptions",
   st=["Most migrants would rather work far from home than near it.",
       "Remittances are the only income of the families left behind."],
   st_hi=["अधिकांश प्रवासी घर के पास के बजाय घर से दूर काम करना पसंद करेंगे।",
          "घर भेजी गई रक़म पीछे रह गए परिवारों की एकमात्र आय है।"],
   key=3)

# ------------------------------------------------------------------ P06 processed food and taxes (3)
p = passage("p06",
  "Diets in India are changing fast. Packaged snacks, sugary drinks and instant meals, once found mainly in cities, are now sold in village shops, and with them have come rising rates of diabetes and obesity, sometimes in the very "
  "households where children are still undernourished. Some countries have taxed sugary drinks and found that people bought fewer of them, and that manufacturers cut the sugar in their recipes to escape the tax. "
  "A tax alone, though, falls hardest on poorer buyers and does nothing about the foods it leaves out. Clear labels on the front of packs, limits on advertising to children and healthy school meals work alongside a tax, "
  "each closing a gap that the others leave open.",
  "भारत में खान-पान तेज़ी से बदल रहा है। पैकेट वाले नाश्ते, मीठे पेय और तुरंत बनने वाले भोजन, जो कभी मुख्यतः शहरों में मिलते थे, अब गाँव की दुकानों में बिकते हैं, और उनके साथ मधुमेह और मोटापे की दरें बढ़ी हैं, कभी-कभी ठीक उन्हीं "
  "घरों में जहाँ बच्चे अब भी कुपोषित हैं। कुछ देशों ने मीठे पेयों पर कर लगाया और पाया कि लोगों ने उन्हें कम ख़रीदा, और निर्माताओं ने कर से बचने के लिए अपनी विधियों में चीनी घटा दी। "
  "पर अकेला कर सबसे अधिक ग़रीब ख़रीदारों पर पड़ता है और उन खाद्य पदार्थों के बारे में कुछ नहीं करता जिन्हें वह छोड़ देता है। पैकेट के सामने स्पष्ट लेबल, बच्चों को लक्ष्य करने वाले विज्ञापनों पर सीमाएँ और विद्यालयों में स्वस्थ भोजन कर के साथ काम करते हैं, "
  "और हर एक वह कमी पूरी करता है जो बाक़ी छोड़ देते हैं।")
RQ(p, "Best Summary", "medium", "mcq", MSG, MSG_HI,
   "The passage credits sugar taxes with real effects but notes two limits -- they fall hardest on poorer buyers and miss the foods they leave out -- and says that labels, limits on advertising and school meals close those gaps. "
   "It reports that the taxes worked where they were tried; it proposes no ban on packaged food; and it says children in some households are still undernourished.",
   "परिच्छेद चीनी पर कर के वास्तविक प्रभाव मानता है पर दो सीमाएँ बताता है -- वह सबसे अधिक ग़रीब ख़रीदारों पर पड़ता है और छोड़े गए खाद्य पदार्थों को नहीं छूता -- और कहता है कि लेबल, विज्ञापन पर सीमाएँ और विद्यालयी भोजन ये कमियाँ पूरी करते हैं। "
   "वह बताता है कि जहाँ ये कर लगाए गए वहाँ उन्होंने काम किया; वह पैकेट वाले भोजन पर प्रतिबंध का प्रस्ताव नहीं करता; और वह कहता है कि कुछ घरों में बच्चे अब भी कुपोषित हैं।",
   "message",
   opts=["A tax on unhealthy food helps most as one part of a wider set of measures.",
         "Taxes on sugary drinks have failed in every one of the countries that have tried them.",
         "Packaged food should no longer be sold in village shops at all.",
         "Undernourishment has now disappeared from most Indian households."],
   opts_hi=["अस्वास्थ्यकर भोजन पर कर दूसरे उपायों के साथ मिलकर सबसे अधिक मदद करता है।",
            "मीठे पेयों पर लगाए गए कर उन सभी देशों में विफल रहे हैं जिन्होंने उन्हें आज़माकर देखा।",
            "गाँव की दुकानों में पैकेट वाला भोजन बेचना पूरी तरह बंद कर देना चाहिए।",
            "अधिकांश भारतीय घरों से कुपोषण अब समाप्त हो चुका है।"],
   ans=0, pos=2)
RQ(p, "Specific Detail", "easy", "mcq",
   "According to the passage, how did manufacturers respond to taxes on sugary drinks?",
   "परिच्छेद के अनुसार, मीठे पेयों पर कर लगने पर निर्माताओं ने क्या किया?",
   "The passage says that manufacturers 'cut the sugar in their recipes to escape the tax'. The other responses are not mentioned; advertising to children appears only as something to be limited.",
   "परिच्छेद कहता है कि निर्माताओं ने 'कर से बचने के लिए अपनी विधियों में चीनी घटा दी'। बाक़ी प्रतिक्रियाओं का उल्लेख नहीं है; बच्चों को लक्ष्य करने वाले विज्ञापन केवल सीमित की जाने वाली चीज़ के रूप में आते हैं।",
   "detail",
   opts=["They cut the sugar in their recipes.",
         "They stopped selling drinks in villages.",
         "They spent more on advertising to children.",
         "They moved their factories to other countries."],
   opts_hi=["उन्होंने अपनी विधियों में चीनी घटा दी।",
            "उन्होंने गाँवों में पेय बेचना बंद कर दिया।",
            "उन्होंने बच्चों को लक्ष्य करने वाले विज्ञापनों पर अधिक ख़र्च किया।",
            "उन्होंने अपने कारख़ाने दूसरे देशों में ले जाए।"],
   ans=0, pos=1)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Only 2 is valid: rising obesity and diabetes appear 'sometimes in the very households where children are still undernourished'. 1 reverses the passage, which says a tax 'falls hardest on poorer buyers'.",
   "केवल 2 वैध है: मोटापे और मधुमेह की बढ़ती दरें 'कभी-कभी ठीक उन्हीं घरों में' दिखती हैं 'जहाँ बच्चे अब भी कुपोषित हैं'। 1 परिच्छेद को उलट देता है, जो कहता है कि कर 'सबसे अधिक ग़रीब ख़रीदारों पर पड़ता है'।",
   "conclusions",
   st=["A tax on sugary drinks leaves poorer buyers better off than richer ones.",
       "Obesity and undernutrition can be found in the same household."],
   st_hi=["मीठे पेयों पर कर ग़रीब ख़रीदारों को अमीरों से बेहतर स्थिति में छोड़ता है।",
          "मोटापा और कुपोषण एक ही घर में पाए जा सकते हैं।"],
   key=1)

# ------------------------------------------------------------------ P07 plantations counted as forest (3)
p = passage("p07",
  "Measured from space, India's forest cover has grown. But the measure counts any area of a hectare or more where tree canopy covers more than a tenth of the ground, so a plantation of a single fast-growing species, an orchard "
  "or a palm grove can count as forest just as an old jungle does. The difference matters. A natural forest holds many species, layers of undergrowth and soil built up over centuries; it stores water and carbon and shelters "
  "animals in ways that a plantation cannot. Rows of eucalyptus or acacia grown for timber or pulp can draw down groundwater and offer little to wildlife. Planting trees is not wrong, but a target measured in hectares "
  "of canopy can be met while the forests that matter most go on shrinking.",
  "अंतरिक्ष से मापने पर भारत का वनावरण बढ़ा है। पर यह माप एक हेक्टेयर या उससे बड़े हर उस क्षेत्र को गिनता है जहाँ पेड़ों का छत्र ज़मीन के दसवें भाग से अधिक को ढकता है, इसलिए एक ही तेज़ बढ़ने वाली प्रजाति का बागान, कोई फलोद्यान "
  "या ताड़ का झुरमुट भी उसी तरह वन गिना जा सकता है जैसे कोई पुराना जंगल। यह अंतर मायने रखता है। प्राकृतिक वन में अनेक प्रजातियाँ, झाड़ियों की परतें और सदियों में बनी मिट्टी होती है; वह पानी और कार्बन सहेजता है और "
  "जानवरों को ऐसा आश्रय देता है जो बागान नहीं दे सकता। लकड़ी या लुगदी के लिए उगाई गई यूकेलिप्टस या बबूल की क़तारें भूजल खींच सकती हैं और वन्यजीवों को बहुत कम देती हैं। पेड़ लगाना ग़लत नहीं है, पर छत्र के हेक्टेयरों में मापा गया लक्ष्य "
  "तब भी पूरा हो सकता है जब सबसे महत्त्वपूर्ण वन सिकुड़ते जाएँ।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage shows that the forest-cover measure counts plantations, orchards and palm groves alongside old forest, explains why the two differ, and warns that a canopy target can be met while natural forests shrink. "
   "It says planting trees 'is not wrong'; it raises no doubt about the measurement from space, only about what it counts; and it says eucalyptus 'can draw down groundwater', not that it is the main cause of falling water tables.",
   "परिच्छेद दिखाता है कि वनावरण का माप पुराने वन के साथ बागानों, फलोद्यानों और ताड़ के झुरमुटों को भी गिनता है, बताता है कि दोनों में अंतर क्यों है, और चेताता है कि छत्र का लक्ष्य तब भी पूरा हो सकता है जब प्राकृतिक वन सिकुड़ें। "
   "वह कहता है कि पेड़ लगाना 'ग़लत नहीं है'; वह अंतरिक्ष से माप पर नहीं, केवल इस पर संदेह उठाता है कि वह क्या गिनता है; और वह कहता है कि यूकेलिप्टस 'भूजल खींच सकता है', यह नहीं कि वह गिरते जल-स्तर का मुख्य कारण है।",
   "crux",
   opts=["Forest-cover figures can mask the loss of natural forest behind new plantations.",
         "India should stop planting trees, since plantations harm the land.",
         "Satellites cannot measure the canopy of trees accurately from space.",
         "Eucalyptus plantations are the main reason why groundwater is falling across India."],
   opts_hi=["वनावरण के आँकड़े प्राकृतिक वन की हानि को नए बागानों के पीछे छिपा सकते हैं।",
            "भारत को पेड़ लगाना बंद कर देना चाहिए, क्योंकि बागान ज़मीन को हानि पहुँचाते हैं।",
            "उपग्रह अंतरिक्ष से पेड़ों के छत्र को सही-सही नहीं माप सकते।",
            "यूकेलिप्टस के बागान ही पूरे भारत में भूजल गिरने का मुख्य कारण हैं।"],
   ans=0, pos=0)
RQ(p, "Assumption", "hard", "s2", ASSUME, ASSUME_HI,
   "Only 1 is assumed: calling natural forests 'the forests that matter most', and objecting that plantations count the same, takes for granted that a hectare of the one is worth more than a hectare of the other. "
   "2 is not needed: the argument holds whether plantations replaced old forest or were planted on bare land.",
   "केवल 1 पूर्वधारणा है: प्राकृतिक वनों को 'सबसे महत्त्वपूर्ण वन' कहना, और इस पर आपत्ति करना कि बागान उतने ही गिने जाते हैं, मानकर चलता है कि एक का हेक्टेयर दूसरे के हेक्टेयर से अधिक मूल्यवान है। "
   "2 की ज़रूरत नहीं: तर्क तब भी टिका रहता है चाहे बागानों ने पुराने वन की जगह ली हो या ख़ाली ज़मीन पर लगाए गए हों।",
   "assumptions",
   st=["A hectare of natural forest is worth more than a hectare of plantation.",
       "Every plantation has been planted on land that was once natural forest."],
   st_hi=["प्राकृतिक वन का एक हेक्टेयर बागान के एक हेक्टेयर से अधिक मूल्यवान है।",
          "हर बागान ऐसी ज़मीन पर लगाया गया है जो कभी प्राकृतिक वन थी।"],
   key=0)
RQ(p, "Inference", "hard", "sc", INFER, INFER_HI,
   "1 and 2 follow. Because any land with more than a tenth under canopy counts, new plantations can lift the figure while old forest is lost (1), and an orchard is named as land that can count as forest (2). "
   "3 reverses the passage: plantations can draw down groundwater, while natural forests store water.",
   "1 और 2 निकलते हैं। चूँकि दसवें भाग से अधिक छत्र वाली हर ज़मीन गिनी जाती है, नए बागान आँकड़ा बढ़ा सकते हैं जबकि पुराना वन खोता जाए (1), और फलोद्यान का नाम उस ज़मीन के रूप में लिया गया है जो वन गिनी जा सकती है (2)। "
   "3 परिच्छेद को उलट देता है: बागान भूजल खींच सकते हैं, जबकि प्राकृतिक वन पानी सहेजते हैं।",
   "inferences",
   st=["Forest cover can rise even while natural forest is shrinking.",
       "An orchard can be counted as forest in the forest-cover figures.",
       "Plantations store more water than natural forests do."],
   st_hi=["प्राकृतिक वन सिकुड़ते हुए भी वनावरण बढ़ सकता है।",
          "वनावरण के आँकड़ों में फलोद्यान को वन गिना जा सकता है।",
          "बागान प्राकृतिक वनों से अधिक पानी सहेजते हैं।"],
   opts=["2 only", "1 and 3 only", "2 and 3 only", "1 and 2 only"], key=3)

# ------------------------------------------------------------------ P08 cyclone warnings (2)
p = passage("p08",
  "Cyclones that once killed thousands on India's eastern coast now kill far fewer, though they are no weaker. Better forecasts are part of the reason, but a forecast saves no one by itself. What changed was the last mile: "
  "warnings passed on in local languages by radio, telephone and village volunteers; shelters built on high ground within walking distance; and drills held often enough that people knew where to go and trusted "
  "the order to leave. The hardest part is persuading families to leave their homes and animals behind, and that trust is built in the calm years, not in the hours before the storm reaches land.",
  "जो चक्रवात कभी भारत के पूर्वी तट पर हज़ारों की जान लेते थे, वे अब कहीं कम लोगों की जान लेते हैं, यद्यपि वे कमज़ोर नहीं हुए हैं। बेहतर पूर्वानुमान इसका एक कारण हैं, पर कोई पूर्वानुमान अपने-आप किसी को नहीं बचाता। जो बदला वह अंतिम कड़ी थी: "
  "रेडियो, टेलीफ़ोन और गाँव के स्वयंसेवकों द्वारा स्थानीय भाषाओं में पहुँचाई गई चेतावनियाँ; पैदल दूरी पर ऊँची ज़मीन पर बने आश्रय; और इतनी बार होने वाले अभ्यास कि लोग जानते थे कि कहाँ जाना है और "
  "घर छोड़ने के आदेश पर भरोसा करते थे। सबसे कठिन काम परिवारों को अपने घर और पशु पीछे छोड़ने के लिए राज़ी करना है, और वह भरोसा शांत वर्षों में बनता है, तूफ़ान के तट से टकराने से पहले के घंटों में नहीं।")
RQ(p, "Specific Detail", "easy", "mcq",
   "According to the passage, which one of the following is the hardest part of saving lives from cyclones?",
   "परिच्छेद के अनुसार, चक्रवातों से जान बचाने में निम्नलिखित में से सबसे कठिन काम कौन-सा है?",
   "The passage says, 'The hardest part is persuading families to leave their homes and animals behind'. Forecasts, shelters and warnings in local languages are all part of what changed, but none of them is called the hardest part.",
   "परिच्छेद कहता है, 'सबसे कठिन काम परिवारों को अपने घर और पशु पीछे छोड़ने के लिए राज़ी करना है'। पूर्वानुमान, आश्रय और स्थानीय भाषाओं में चेतावनियाँ, सब उस बदलाव का भाग हैं, पर उनमें से किसी को सबसे कठिन काम नहीं कहा गया।",
   "detail",
   opts=["persuading families to leave their homes and animals",
         "making the forecasts of each cyclone's path more accurate",
         "building enough shelters on high ground near the villages",
         "translating the warnings into every local language"],
   opts_hi=["परिवारों को अपने घर और पशु छोड़ने के लिए राज़ी करना",
            "हर चक्रवात के रास्ते के पूर्वानुमान को अधिक सटीक बनाना",
            "गाँवों के पास ऊँची ज़मीन पर पर्याप्त आश्रय बनाना",
            "चेतावनियों का हर स्थानीय भाषा में अनुवाद करना"],
   ans=0, pos=3)
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage says that cyclones are no weaker and that a forecast 'saves no one by itself'; what changed was the last mile -- warnings people received and trusted, shelters within reach, and drills. "
   "It says the storms are no weaker; it says forecasts are only part of the reason; and it speaks of persuasion and trust, not of force.",
   "परिच्छेद कहता है कि चक्रवात कमज़ोर नहीं हुए और कि कोई पूर्वानुमान 'अपने-आप किसी को नहीं बचाता'; जो बदला वह अंतिम कड़ी थी -- चेतावनियाँ जो लोगों तक पहुँचीं और जिन पर उन्होंने भरोसा किया, पहुँच में आश्रय, और अभ्यास। "
   "वह कहता है कि तूफ़ान कमज़ोर नहीं हुए; वह कहता है कि पूर्वानुमान केवल एक कारण हैं; और वह राज़ी करने और भरोसे की बात करता है, बल प्रयोग की नहीं।",
   "crux",
   opts=["Deaths fell as warnings reached people who trusted them, not through forecasts alone.",
         "Cyclones on India's eastern coast have become much weaker than they were in the past.",
         "Better forecasts are by themselves enough to explain why cyclones now kill fewer people.",
         "Families should be forced by law to leave their homes before every cyclone arrives."],
   opts_hi=["मौतें इसलिए घटीं कि चेतावनियाँ भरोसा करने वालों तक पहुँचीं, केवल पूर्वानुमानों से नहीं।",
            "भारत के पूर्वी तट के चक्रवात पहले की तुलना में बहुत कमज़ोर हो गए हैं।",
            "चक्रवातों से अब कम लोगों के मरने की व्याख्या के लिए बेहतर पूर्वानुमान अपने-आप पर्याप्त हैं।",
            "हर चक्रवात से पहले परिवारों को क़ानूनन अपना घर छोड़ने के लिए बाध्य करना चाहिए।"],
   ans=0, pos=1)

# ------------------------------------------------------------------ P09 museum objects and their return (3)
p = passage("p09",
  "Museums in Europe and North America hold many objects taken from other countries during colonial rule -- some bought, some given and some simply carried off. Countries of origin increasingly ask for their return, "
  "and some museums have begun to agree. Opponents warn that returning every object would empty the great collections, which let millions of people see the art of many cultures side by side. Their case is weakest "
  "where an object was plainly looted, and strongest, perhaps, where it was bought openly and has been cared for over a century. Each claim deserves to be judged on its history. But a rule that keeps everything "
  "because some cases are hard is not a judgement; it is a refusal to make one.",
  "यूरोप और उत्तर अमेरिका के संग्रहालयों में औपनिवेशिक शासन के दौरान दूसरे देशों से ली गई अनेक वस्तुएँ हैं -- कुछ ख़रीदी गईं, कुछ उपहार में मिलीं और कुछ यों ही उठा ली गईं। मूल देश बढ़ती संख्या में उनकी वापसी माँग रहे हैं, "
  "और कुछ संग्रहालय सहमत होने लगे हैं। विरोधी चेताते हैं कि हर वस्तु लौटाने से वे महान संग्रह ख़ाली हो जाएँगे जो लाखों लोगों को अनेक संस्कृतियों की कला एक साथ देखने देते हैं। उनका पक्ष वहाँ सबसे कमज़ोर है "
  "जहाँ कोई वस्तु स्पष्ट रूप से लूटी गई थी, और शायद वहाँ सबसे मज़बूत जहाँ वह खुले रूप से ख़रीदी गई और एक सदी से सँभालकर रखी गई है। हर दावे को उसके इतिहास के आधार पर परखा जाना चाहिए। पर जो नियम सब कुछ इसलिए रख लेता है "
  "कि कुछ मामले कठिन हैं, वह कोई निर्णय नहीं; वह निर्णय करने से इनकार है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage grants the opponents' point about great collections, ranks the claims by how objects were acquired, and ends by rejecting a rule that keeps everything. "
   "It never asks for every object to be returned; it rejects keeping everything; and it calls the case for keeping an openly bought object 'strongest, perhaps', which is short of 'never return'.",
   "परिच्छेद महान संग्रहों के बारे में विरोधियों की बात मानता है, दावों को इस आधार पर आँकता है कि वस्तुएँ कैसे प्राप्त हुईं, और अंत में सब कुछ रख लेने वाले नियम को नकारता है। "
   "वह कहीं हर वस्तु लौटाने को नहीं कहता; वह सब कुछ रख लेने को नकारता है; और खुले रूप से ख़रीदी गई वस्तु को रखने के पक्ष को 'शायद सबसे मज़बूत' कहता है, जो 'कभी न लौटाओ' से कम है।",
   "crux",
   opts=["Each claim for return should be judged on its history, not refused wholesale.",
         "Every object in a foreign museum should be returned to its country of origin.",
         "Museums should keep all their objects so that their collections are not emptied.",
         "Objects that were bought openly should never be returned to their countries."],
   opts_hi=["वापसी के हर दावे को उसके इतिहास पर परखना चाहिए, सबको एक साथ ठुकराना नहीं।",
            "किसी विदेशी संग्रहालय की हर वस्तु उसके मूल देश को लौटा दी जानी चाहिए।",
            "संग्रहालयों को अपनी सभी वस्तुएँ रखनी चाहिए ताकि उनके संग्रह ख़ाली न हों।",
            "जो वस्तुएँ खुले रूप से ख़रीदी गईं, उन्हें उनके देशों को कभी नहीं लौटाना चाहिए।"],
   ans=0, pos=2)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Both are valid. The opponents' case is 'weakest where an object was plainly looted', so the case for return is strongest there (1); and the author calls a rule that keeps everything 'a refusal' to judge (2).",
   "दोनों वैध हैं। विरोधियों का पक्ष 'वहाँ सबसे कमज़ोर है जहाँ कोई वस्तु स्पष्ट रूप से लूटी गई थी', इसलिए वहाँ वापसी का पक्ष सबसे मज़बूत है (1); और लेखक सब कुछ रख लेने वाले नियम को निर्णय करने से 'इनकार' कहता है (2)।",
   "conclusions",
   st=["In the author's view, the case for returning a plainly looted object is strong.",
       "The author would not accept a policy of keeping every object in a collection."],
   st_hi=["लेखक की दृष्टि में स्पष्ट रूप से लूटी गई वस्तु को लौटाने का पक्ष मज़बूत है।",
          "लेखक किसी संग्रह की हर वस्तु रख लेने की नीति स्वीकार नहीं करेगा।"],
   key=2)
RQ(p, "Assumption", "hard", "s2", ASSUME, ASSUME_HI,
   "Only 2 is assumed: judging each claim 'on its history' is possible only if the history of at least some objects -- looted, bought or given -- can be established. "
   "1 contradicts the passage, which says that some objects were bought and some given.",
   "केवल 2 पूर्वधारणा है: हर दावे को 'उसके इतिहास के आधार पर' परखना तभी संभव है जब कम से कम कुछ वस्तुओं का इतिहास -- लूटी गईं, ख़रीदी गईं या उपहार में मिलीं -- स्थापित किया जा सके। "
   "1 परिच्छेद का खंडन करता है, जो कहता है कि कुछ वस्तुएँ ख़रीदी गईं और कुछ उपहार में मिलीं।",
   "assumptions",
   st=["Every object in the museums of Europe and North America was taken by force.",
       "How an object was acquired can be established for at least some of the claims."],
   st_hi=["यूरोप और उत्तर अमेरिका के संग्रहालयों की हर वस्तु बलपूर्वक ली गई थी।",
          "कम से कम कुछ दावों के लिए यह स्थापित किया जा सकता है कि वस्तु कैसे प्राप्त हुई।"],
   key=1)

# ------------------------------------------------------------------ P10 dairy cooperatives (3)
p = passage("p10",
  "India produces more milk than any other country, and much of it comes from small farmers who own two or three animals. What made this possible was not large farms but cooperatives: villagers who pooled their milk, "
  "sold it through a society they owned, and were paid according to its fat content, measured in front of them. The fair measurement mattered as much as the price, because it ended a long suspicion that traders cheated "
  "on quality. The cooperatives also brought cattle feed, veterinary care and better breeding to the village. Their weakness is the one common to bodies owned by their members: where elections are captured by a few "
  "and accounts are kept closed, the trust that built them drains away.",
  "भारत किसी भी अन्य देश से अधिक दूध पैदा करता है, और उसका बड़ा भाग उन छोटे किसानों से आता है जिनके पास दो-तीन पशु हैं। यह बड़े फ़ार्मों से नहीं बल्कि सहकारी समितियों से संभव हुआ: ग्रामीण जिन्होंने अपना दूध इकट्ठा किया, "
  "उसे अपनी ही समिति के माध्यम से बेचा, और उसकी वसा की मात्रा के अनुसार भुगतान पाया, जो उनके सामने मापी जाती थी। न्यायपूर्ण माप उतना ही महत्त्वपूर्ण था जितना दाम, क्योंकि उसने यह पुराना संदेह समाप्त किया कि व्यापारी गुणवत्ता में "
  "धोखा देते हैं। सहकारी समितियाँ गाँव तक पशु आहार, पशु चिकित्सा और बेहतर नस्ल सुधार भी लाईं। उनकी कमज़ोरी वही है जो सदस्यों के स्वामित्व वाली हर संस्था की होती है: जहाँ चुनाव कुछ लोगों के क़ब्ज़े में चले जाएँ "
  "और हिसाब बंद रखे जाएँ, वहाँ वह भरोसा रिसकर ख़त्म हो जाता है जिसने उन्हें खड़ा किया था।")
RQ(p, "Best Summary", "medium", "mcq", MSG, MSG_HI,
   "The passage credits the cooperatives -- pooled milk, member ownership, payment by fat content measured openly -- with the rise of small-farm dairying, and warns that captured elections and closed accounts drain the trust "
   "behind them. It says much of the milk comes from small farmers; it says fair measurement mattered as much as the price; and it proposes no replacement by traders.",
   "परिच्छेद छोटे किसानों के डेयरी उद्योग के उदय का श्रेय सहकारी समितियों को देता है -- इकट्ठा दूध, सदस्यों का स्वामित्व, खुले में मापी गई वसा के अनुसार भुगतान -- और चेताता है कि क़ब्ज़े में गए चुनाव और बंद हिसाब उनके पीछे के भरोसे को "
   "ख़त्म कर देते हैं। वह कहता है कि बड़ा भाग छोटे किसानों से आता है; वह कहता है कि न्यायपूर्ण माप उतना ही महत्त्वपूर्ण था जितना दाम; और वह व्यापारियों से उनकी जगह लेने का प्रस्ताव नहीं करता।",
   "message",
   opts=["Dairy cooperatives rose on fair dealing and shared ownership, which poor governance undoes.",
         "Most of India's milk comes from large commercial farms rather than from small farmers in villages.",
         "The price of milk matters more to farmers than whether it is measured honestly.",
         "Dairy cooperatives should be replaced by private traders who pay better prices."],
   opts_hi=["डेयरी सहकारी समितियाँ ईमानदारी और साझे स्वामित्व से बढ़ीं, जिसे कुशासन मिटा देता है।",
            "भारत का अधिकांश दूध गाँवों के छोटे किसानों के बजाय बड़े व्यावसायिक फ़ार्मों से आता है।",
            "किसानों के लिए दूध का दाम इस बात से अधिक मायने रखता है कि वह ईमानदारी से मापा जाए।",
            "डेयरी सहकारी समितियों की जगह बेहतर दाम देने वाले निजी व्यापारियों को लेनी चाहिए।"],
   ans=0, pos=0)
RQ(p, "Specific Detail", "easy", "mcq",
   "According to the passage, why did measuring the fat content in front of the farmers matter?",
   "परिच्छेद के अनुसार, किसानों के सामने वसा की मात्रा मापना क्यों महत्त्वपूर्ण था?",
   "The passage says that the fair measurement 'ended a long suspicion that traders cheated on quality'. It does not say that the measuring raised the fat content, let farmers fix prices, or was required by the government.",
   "परिच्छेद कहता है कि न्यायपूर्ण माप ने 'यह पुराना संदेह समाप्त किया कि व्यापारी गुणवत्ता में धोखा देते हैं'। वह यह नहीं कहता कि माप ने वसा की मात्रा बढ़ाई, किसानों को दाम तय करने दिया, या सरकार ने उसे अनिवार्य किया।",
   "detail",
   opts=["It ended a long suspicion that traders cheated on quality.",
         "It helped the farmers raise the fat content of their milk.",
         "It allowed the farmers to fix the price of their milk themselves.",
         "It was a condition laid down by the government for all buyers."],
   opts_hi=["उसने व्यापारियों के गुणवत्ता में धोखा देने का पुराना संदेह मिटाया।",
            "उससे किसानों को अपने दूध में वसा की मात्रा बढ़ाने में सहायता मिली।",
            "उसने किसानों को अपने दूध का दाम स्वयं तय करने दिया।",
            "वह सभी ख़रीदारों के लिए सरकार द्वारा तय की गई शर्त थी।"],
   ans=0, pos=3)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Only 1 is valid: where 'accounts are kept closed, the trust that built them drains away'. 2 contradicts the passage, whose whole story is of small farmers with two or three animals gaining through cooperatives.",
   "केवल 1 वैध है: जहाँ 'हिसाब बंद रखे जाएँ, वहाँ वह भरोसा रिसकर ख़त्म हो जाता है जिसने उन्हें खड़ा किया था'। 2 परिच्छेद का खंडन करता है, जिसकी पूरी कहानी दो-तीन पशुओं वाले छोटे किसानों के सहकारी समितियों से लाभ पाने की है।",
   "conclusions",
   st=["A cooperative whose accounts are kept closed may lose its members' trust.",
       "Farmers with only two or three animals cannot gain from selling milk."],
   st_hi=["जिस सहकारी समिति का हिसाब बंद रखा जाता है, वह अपने सदस्यों का भरोसा खो सकती है।",
          "केवल दो-तीन पशुओं वाले किसान दूध बेचकर लाभ नहीं कमा सकते।"],
   key=0)
