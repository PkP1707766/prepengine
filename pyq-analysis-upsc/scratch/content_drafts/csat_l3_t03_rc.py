# -*- coding: utf-8 -*-
"""CSAT Level 3 · Test 3 -- Reading Comprehension: 10 original passages, 28 items (8 x 3, 2 x 2).

Level 3 passages carry a turn in the argument -- a claim, then its limit -- so that the items test where the author
stops as much as what the author says. Themes, none used in Level 2 Tests 1-7, Level 1 Minis 1-3 or Level 3 Tests 1-2:
the wisdom of crowds, restoring old monuments, vaccine hesitancy, desalination, merit and luck, knowledge that cannot
be written down, risk compensation, glaciers as water towers, a universal basic income, and the printing press.
Item types: main idea 7, best summary 3, inference 9, assumption 5, tone 1, specific detail 3. Difficulty 2 easy /
14 medium / 12 hard. Options are named by content in every explanation."""
from csat_common import passage, RQ

CRUX = "Which one of the following statements best reflects the crux of the passage?"
CRUX_HI = "निम्नलिखित में से कौन-सा कथन परिच्छेद के सार को सबसे अच्छी तरह व्यक्त करता है?"
MSG = "Which one of the following statements best reflects the most logical and rational message conveyed by the passage?"
MSG_HI = "निम्नलिखित में से कौन-सा कथन परिच्छेद द्वारा दिए गए सबसे तार्किक और विवेकपूर्ण संदेश को सबसे अच्छी तरह व्यक्त करता है?"
VALID = "On the basis of the passage, which of the following conclusions is/are valid?"
VALID_HI = "परिच्छेद के आधार पर निम्नलिखित में से कौन-सा/से निष्कर्ष वैध है/हैं?"
ASSUME = "Which of the following assumptions has/have been made in the passage?"
ASSUME_HI = "परिच्छेद में निम्नलिखित में से कौन-सी पूर्वधारणा/एँ बनाई गई है/हैं?"

# ------------------------------------------------------------------ P01 the wisdom of crowds (3)
p = passage("p01",
  "Ask a large number of people to guess the weight of an ox at a village fair, and the middle of their guesses is often remarkably close to the truth -- closer than most individual guesses, and sometimes closer than an expert's. The reason is not that crowds are wise but that their errors cancel: "
  "some guess too high and others too low, and the mistakes, if they are unrelated, wash out. That condition is easily broken. If people can hear one another's guesses, or all take their cue from the same confident voice, their errors move together instead of cancelling, "
  "and the crowd becomes no wiser than its loudest member. A crowd is useful as a measuring instrument only when its members think independently and bring different scraps of knowledge to the question.",
  "किसी ग्राम-मेले में बड़ी संख्या में लोगों से एक बैल का भार अनुमानित करने को कहिए, और उनके अनुमानों का मध्य प्रायः सच के उल्लेखनीय रूप से निकट होता है -- अधिकांश व्यक्तिगत अनुमानों से अधिक निकट, और कभी-कभी किसी विशेषज्ञ से भी अधिक। इसका कारण यह नहीं कि भीड़ बुद्धिमान होती है, बल्कि यह कि उनकी त्रुटियाँ एक-दूसरे को काट देती हैं: "
  "कुछ बहुत अधिक अनुमान लगाते हैं और कुछ बहुत कम, और यदि भूलें आपस में असंबद्ध हों तो वे धुल जाती हैं। यह शर्त आसानी से टूट जाती है। यदि लोग एक-दूसरे के अनुमान सुन सकें, या सब एक ही आत्मविश्वासी आवाज़ से संकेत लें, तो उनकी त्रुटियाँ कटने के बजाय एक साथ चलती हैं, "
  "और भीड़ अपने सबसे ऊँचे स्वर वाले सदस्य से अधिक बुद्धिमान नहीं रह जाती। भीड़ मापने के उपकरण के रूप में तभी उपयोगी है जब उसके सदस्य स्वतंत्र रूप से सोचें और प्रश्न पर ज्ञान के अलग-अलग टुकड़े लेकर आएँ।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage explains that a crowd's middle guess is accurate because unrelated errors cancel, and that this fails when people copy one another or follow one voice. The crux is the condition: independence and different knowledge. "
   "It says explicitly that the reason is 'not that crowds are wise'; it says the crowd is 'sometimes' closer than an expert, not always; and it does not reject crowd judgement, only crowds that are not independent.",
   "परिच्छेद बताता है कि भीड़ का मध्य अनुमान इसलिए सटीक होता है कि असंबद्ध त्रुटियाँ कट जाती हैं, और कि यह तब विफल होता है जब लोग एक-दूसरे की नक़ल करें या एक आवाज़ के पीछे चलें। सार यह शर्त है: स्वतंत्रता और अलग-अलग ज्ञान। "
   "वह स्पष्ट कहता है कि कारण 'यह नहीं कि भीड़ बुद्धिमान होती है'; वह कहता है कि भीड़ 'कभी-कभी' विशेषज्ञ से अधिक निकट होती है, हमेशा नहीं; और वह भीड़ के निर्णय को अस्वीकार नहीं करता, केवल उन भीड़ों को जो स्वतंत्र नहीं हैं।",
   "crux",
   opts=["Crowds are wiser than experts, and their judgement should be preferred on every question.",
         "A crowd judges well only when its members' errors are independent and so cancel out.",
         "The judgement of a crowd can never be relied on, because people tend to copy one another.",
         "Experts should always be consulted before a crowd is asked to guess any quantity at all."],
   opts_hi=["भीड़ विशेषज्ञों से अधिक बुद्धिमान होती है, और हर प्रश्न पर उसके निर्णय को प्राथमिकता देनी चाहिए।",
            "भीड़ तभी अच्छा आँकती है जब उसके सदस्यों की त्रुटियाँ स्वतंत्र हों और इसलिए कट जाएँ।",
            "भीड़ के निर्णय पर कभी भरोसा नहीं किया जा सकता, क्योंकि लोग एक-दूसरे की नक़ल करते हैं।",
            "भीड़ से किसी भी मात्रा का अनुमान पूछने से पहले हमेशा विशेषज्ञों से परामर्श लेना चाहिए।"],
   ans=1, pos=1)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Only 2 is valid. If everyone first hears an announcer's guess, their errors 'move together instead of cancelling', so the middle of the guesses tends to follow the announcer rather than the truth. "
   "1 goes beyond the passage: it says the middle guess is closer than 'most' individual guesses, not that it is closer than every single one; some individuals may well guess better.",
   "केवल 2 वैध है। यदि सब पहले उद्घोषक का अनुमान सुन लें, तो उनकी त्रुटियाँ 'कटने के बजाय एक साथ चलती हैं', इसलिए अनुमानों का मध्य सच के बजाय उद्घोषक के पीछे जाता है। "
   "1 परिच्छेद से आगे जाता है: वह कहता है कि मध्य अनुमान 'अधिकांश' व्यक्तिगत अनुमानों से अधिक निकट है, यह नहीं कि वह हर एक से अधिक निकट है; कुछ व्यक्ति बेहतर अनुमान लगा सकते हैं।",
   "conclusions",
   st=["The middle of a crowd's guesses is always closer to the truth than every individual guess.",
       "If every guesser first hears an announcer's estimate, the crowd's middle guess will tend to follow that estimate."],
   st_hi=["भीड़ के अनुमानों का मध्य हमेशा हर एक व्यक्तिगत अनुमान से सच के अधिक निकट होता है।",
          "यदि हर अनुमान लगाने वाला पहले किसी उद्घोषक का अनुमान सुन ले, तो भीड़ का मध्य अनुमान उसी अनुमान के पीछे जाएगा।"],
   key=1)
RQ(p, "Assumption", "hard", "s2", ASSUME, ASSUME_HI,
   "Only 1 is assumed. The cancelling of errors works only if, left to themselves, people's mistakes fall on both sides of the truth rather than mostly on one; a crowd that all guessed too low for the same reason would not cancel anything. "
   "2 is not assumed: the passage says the crowd is 'sometimes' closer than an expert, and its argument does not need experts to be generally unreliable.",
   "केवल 1 पूर्वधारणा है। त्रुटियों का कटना तभी चलता है जब, अपने भरोसे छोड़ दिए जाने पर, लोगों की भूलें सच के दोनों ओर पड़ें, अधिकतर एक ओर नहीं; जो भीड़ एक ही कारण से सब कम अनुमान लगाए, वह कुछ नहीं काटेगी। "
   "2 पूर्वधारणा नहीं है: परिच्छेद कहता है कि भीड़ 'कभी-कभी' विशेषज्ञ से अधिक निकट होती है, और उसके तर्क के लिए विशेषज्ञों का सामान्यतः अविश्वसनीय होना आवश्यक नहीं।",
   "assumptions",
   st=["People guessing independently are as likely to err on the high side as on the low side.",
       "Experts are generally unreliable when they estimate quantities."],
   st_hi=["स्वतंत्र रूप से अनुमान लगाने वाले लोगों की भूल ऊपर की ओर होने की संभावना उतनी ही है जितनी नीचे की ओर।",
          "मात्राओं का अनुमान लगाते समय विशेषज्ञ सामान्यतः अविश्वसनीय होते हैं।"],
   key=0)

# ------------------------------------------------------------------ P02 restoring old monuments (3)
p = passage("p02",
  "When an old temple or fort has crumbled, it is tempting to rebuild it as it once was, so that visitors can see it whole. But a monument is valuable not only for its form but as evidence: its worn stones, its later repairs and even its scars record what happened to it over centuries. "
  "A reconstruction based on guesswork can erase that record and replace it with a modern idea of the past. For this reason conservators generally prefer to stabilise what survives, to repair with materials that can be told apart from the original, and to stop where firm evidence runs out. "
  "The rule is not absolute. Where a building is still in use, or where its form is fully documented, careful rebuilding may be justified. The danger lies in confusing a monument's appearance with its authenticity.",
  "जब कोई पुराना मंदिर या क़िला जर्जर हो जाता है, तो उसे वैसा ही फिर से बनाने का मन होता है जैसा वह कभी था, ताकि आगंतुक उसे पूरा देख सकें। पर कोई स्मारक केवल अपने रूप के लिए नहीं, साक्ष्य के रूप में भी मूल्यवान है: उसके घिसे पत्थर, उसकी बाद की मरम्मतें और यहाँ तक कि उसके घाव भी दर्ज करते हैं कि सदियों में उस पर क्या बीता। "
  "अनुमान पर आधारित पुनर्निर्माण उस अभिलेख को मिटाकर उसकी जगह अतीत का एक आधुनिक विचार रख सकता है। इसीलिए संरक्षक सामान्यतः जो बचा है उसे स्थिर करना, ऐसी सामग्री से मरम्मत करना जिसे मूल से अलग पहचाना जा सके, और वहाँ रुक जाना पसंद करते हैं जहाँ ठोस साक्ष्य समाप्त हो जाए। "
  "यह नियम निरपेक्ष नहीं है। जहाँ कोई भवन अब भी प्रयोग में है, या जहाँ उसका रूप पूरी तरह प्रलेखित है, वहाँ सावधानीपूर्ण पुनर्निर्माण उचित हो सकता है। ख़तरा किसी स्मारक के रूप को उसकी प्रामाणिकता समझ बैठने में है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage values a monument as evidence of its history, warns that guesswork reconstruction erases that evidence, prefers stabilising and distinguishable repair, and allows exceptions where the building is in use or fully documented. "
   "It does not forbid all rebuilding; it does not say repairs should match the original so closely that they cannot be told apart -- it says the opposite; and it does not reduce a monument's worth to how it looks.",
   "परिच्छेद स्मारक को उसके इतिहास के साक्ष्य के रूप में महत्व देता है, चेताता है कि अनुमान पर आधारित पुनर्निर्माण उस साक्ष्य को मिटा देता है, स्थिर करने और पहचानी जा सकने वाली मरम्मत को प्राथमिकता देता है, और अपवादों की अनुमति देता है जहाँ भवन प्रयोग में हो या पूरी तरह प्रलेखित हो। "
   "वह हर पुनर्निर्माण को वर्जित नहीं करता; वह यह नहीं कहता कि मरम्मत मूल से इतनी मिलती हो कि अलग न पहचानी जा सके -- वह इसका उलटा कहता है; और वह स्मारक के मूल्य को उसके दिखने तक सीमित नहीं करता।",
   "crux",
   opts=["No crumbling monument should ever be rebuilt, whatever is known about its original form.",
         "Repairs to a monument should match the original so closely that no one can tell them apart.",
         "A monument's chief value lies in how complete and impressive it looks to its visitors.",
         "A monument's worth as evidence argues for cautious repair over rebuilding from guesswork."],
   opts_hi=["किसी भी जर्जर स्मारक का कभी पुनर्निर्माण नहीं होना चाहिए, उसके मूल रूप के बारे में चाहे जो ज्ञात हो।",
            "किसी स्मारक की मरम्मत मूल से इतनी मिलनी चाहिए कि कोई उन्हें अलग न पहचान सके।",
            "किसी स्मारक का मुख्य मूल्य इसमें है कि वह आगंतुकों को कितना पूरा और प्रभावशाली दिखता है।",
            "साक्ष्य के रूप में स्मारक का मूल्य अनुमान से पुनर्निर्माण के बजाय सावधान मरम्मत का पक्ष लेता है।"],
   ans=3, pos=3)
RQ(p, "Author's Tone", "medium", "mcq",
   "The author's attitude towards rebuilding crumbled monuments is best described as one of:",
   "जर्जर स्मारकों के पुनर्निर्माण के प्रति लेखक के दृष्टिकोण का सबसे अच्छा वर्णन है:",
   "The author warns against rebuilding from guesswork and explains why conservators prefer restraint, but also says that 'the rule is not absolute' and that careful rebuilding may be justified in some cases. That is caution, not blanket opposition. "
   "The author is not enthusiastic about rebuilding, does not reject it in every case, and plainly cares about the question.",
   "लेखक अनुमान से पुनर्निर्माण के विरुद्ध चेताता है और बताता है कि संरक्षक संयम क्यों पसंद करते हैं, पर यह भी कहता है कि 'यह नियम निरपेक्ष नहीं है' और कुछ स्थितियों में सावधानीपूर्ण पुनर्निर्माण उचित हो सकता है। यह सावधानी है, पूर्ण विरोध नहीं। "
   "लेखक पुनर्निर्माण के प्रति उत्साही नहीं है, हर स्थिति में उसे अस्वीकार नहीं करता, और स्पष्ट रूप से इस प्रश्न की परवाह करता है।",
   "tone",
   opts=["enthusiastic support for rebuilding monuments in full",
         "cautious reserve",
         "outright opposition to rebuilding in every case",
         "indifference to how monuments are treated"],
   opts_hi=["स्मारकों के पूर्ण पुनर्निर्माण का उत्साहपूर्ण समर्थन",
            "सावधान संकोच",
            "हर स्थिति में पुनर्निर्माण का पूर्ण विरोध",
            "स्मारकों के साथ किए जाने वाले व्यवहार के प्रति उदासीनता"],
   ans=1, pos=1)
RQ(p, "Inference", "hard", "mcq",
   "On the basis of the passage, which one of the following would a careful conservator be most likely to approve?",
   "परिच्छेद के आधार पर, निम्नलिखित में से किसे एक सावधान संरक्षक सबसे अधिक स्वीकार करेगा?",
   "The passage allows careful rebuilding where a building's form is fully documented, and asks for repairs that can be told apart from the original. Rebuilding a fallen gateway exactly from detailed old drawings, in stone that can be distinguished from the old, meets both conditions. "
   "Adding a dome that may never have existed, smoothing away old repairs to make the walls look new, and filling gaps with matching stone so that the repair cannot be seen all do what the passage warns against.",
   "परिच्छेद वहाँ सावधानीपूर्ण पुनर्निर्माण की अनुमति देता है जहाँ भवन का रूप पूरी तरह प्रलेखित हो, और ऐसी मरम्मत माँगता है जो मूल से अलग पहचानी जा सके। विस्तृत पुराने चित्रों से गिरे प्रवेश-द्वार को ठीक वैसा ही, पुराने से अलग पहचाने जा सकने वाले पत्थर में, फिर बनाना दोनों शर्तें पूरी करता है। "
   "ऐसा गुंबद जोड़ना जो शायद कभी था ही नहीं, दीवारों को नया दिखाने के लिए पुरानी मरम्मतें घिसकर मिटाना, और दरारों को मेल खाते पत्थर से भरना ताकि मरम्मत दिखे ही नहीं -- ये सब वही करते हैं जिसके विरुद्ध परिच्छेद चेताता है।",
   "what-a-conservator-approves",
   opts=["Rebuilding a fallen gateway from detailed old drawings, in stone distinct from the original",
         "Adding a dome to a ruined temple because similar temples of that period often had domes on them",
         "Smoothing away the old repairs on a fort's walls so that the whole building looks new again",
         "Filling the gaps in a carved wall with matching stone so that no repair can be seen at all"],
   opts_hi=["विस्तृत पुराने चित्रों से गिरे प्रवेश-द्वार का पुनर्निर्माण, मूल से अलग दिखने वाले पत्थर में",
            "एक खंडहर मंदिर पर गुंबद जोड़ना, क्योंकि उस काल के ऐसे ही मंदिरों पर प्रायः गुंबद हुआ करते थे",
            "क़िले की दीवारों की पुरानी मरम्मतें घिसकर मिटाना ताकि पूरा भवन फिर से नया दिखे",
            "नक़्क़ाशीदार दीवार की दरारों को मेल खाते पत्थर से भरना ताकि कोई मरम्मत दिखाई ही न दे"],
   ans=0, pos=0)

# ------------------------------------------------------------------ P03 vaccine hesitancy (3)
p = passage("p03",
  "Vaccines are among the cheapest ways of saving lives, yet in many places a share of parents delay or refuse them. It is easy to blame ignorance, but studies of such hesitancy find a more mixed picture. Some parents distrust the health system because of past neglect or a bad experience; "
  "some see little risk in diseases that vaccination itself has made rare, and so feel little urgency; others intend to vaccinate but are put off by a clinic that is far away, opens at the wrong hours or keeps them waiting all day. Each of these calls for a different response. "
  "Distrust is answered by health workers whom people know and believe, not by louder advertising; low urgency by honest reminders of what the diseases do; and inconvenience by bringing the vaccine closer, at times that suit working parents. Treating every hesitant parent as misinformed is likely to persuade few of them.",
  "टीके जीवन बचाने के सबसे सस्ते तरीक़ों में हैं, फिर भी कई स्थानों पर कुछ अभिभावक उन्हें टालते या मना करते हैं। अज्ञान को दोष देना आसान है, पर ऐसी हिचक के अध्ययन एक मिली-जुली तस्वीर पाते हैं। कुछ अभिभावक पिछली उपेक्षा या किसी बुरे अनुभव के कारण स्वास्थ्य तंत्र पर अविश्वास करते हैं; "
  "कुछ उन रोगों में कम जोखिम देखते हैं जिन्हें स्वयं टीकाकरण ने दुर्लभ बना दिया है, और इसलिए कम तात्कालिकता अनुभव करते हैं; अन्य टीका लगवाना चाहते हैं पर दूर स्थित, ग़लत समय पर खुलने वाले या दिन भर प्रतीक्षा कराने वाले चिकित्सालय से हतोत्साहित हो जाते हैं। इनमें से हर एक अलग प्रतिक्रिया माँगता है। "
  "अविश्वास का उत्तर ऐसे स्वास्थ्य कार्यकर्ता हैं जिन्हें लोग जानते हैं और जिन पर विश्वास करते हैं, ऊँचे विज्ञापन नहीं; कम तात्कालिकता का उत्तर इन रोगों के प्रभावों की ईमानदार याद दिलाना है; और असुविधा का उत्तर टीके को निकट लाना है, ऐसे समय पर जो कामकाजी अभिभावकों के अनुकूल हो। हर हिचकिचाते अभिभावक को ग़लत जानकारी वाला मानना शायद ही उनमें से कुछ को मना पाए।")
RQ(p, "Best Summary", "medium", "mcq", MSG, MSG_HI,
   "The passage finds that hesitancy has several causes -- distrust, low urgency, inconvenience -- and argues that each needs its own remedy, so treating every hesitant parent as misinformed will fail. "
   "It rejects blaming ignorance alone; it says that distrust is answered by trusted health workers, 'not by louder advertising'; and it does not say vaccines are unsafe -- it calls them among the cheapest ways of saving lives.",
   "परिच्छेद पाता है कि हिचक के कई कारण हैं -- अविश्वास, कम तात्कालिकता, असुविधा -- और तर्क देता है कि हर एक को अपना उपचार चाहिए, इसलिए हर हिचकिचाते अभिभावक को ग़लत जानकारी वाला मानना विफल होगा। "
   "वह केवल अज्ञान को दोष देना अस्वीकार करता है; वह कहता है कि अविश्वास का उत्तर भरोसेमंद स्वास्थ्य कार्यकर्ता हैं, 'ऊँचे विज्ञापन नहीं'; और वह यह नहीं कहता कि टीके असुरक्षित हैं -- वह उन्हें जीवन बचाने के सबसे सस्ते तरीक़ों में गिनता है।",
   "message",
   opts=["Vaccine hesitancy is caused mainly by ignorance, and more information will end it everywhere.",
         "Louder advertising is the most effective way of winning back the trust of hesitant parents.",
         "Hesitancy has different causes, and each must be met in its own way to persuade parents.",
         "Parents who delay vaccines do so because they have good reason to doubt that vaccines are safe."],
   opts_hi=["टीकों के प्रति हिचक मुख्यतः अज्ञान से होती है, और अधिक जानकारी उसे हर जगह समाप्त कर देगी।",
            "हिचकिचाते अभिभावकों का विश्वास फिर से जीतने का सबसे प्रभावी तरीक़ा ऊँचे विज्ञापन हैं।",
            "हिचक के अलग-अलग कारण हैं, और अभिभावकों को मनाने के लिए हर एक से अपने ढंग से निपटना होगा।",
            "जो अभिभावक टीके टालते हैं, उनके पास टीकों की सुरक्षा पर संदेह करने का ठोस कारण होता है।"],
   ans=2, pos=2)
RQ(p, "Assumption", "hard", "s2", ASSUME, ASSUME_HI,
   "Both are assumed. The remedy for distrust -- health workers 'whom people know and believe' -- works only if people trust the familiar workers more than the system as a whole (1). "
   "And the remedy for inconvenience -- bringing the vaccine closer at suitable times -- presumes that some parents who mean to vaccinate would in fact do so once it is easier (2).",
   "दोनों पूर्वधारणाएँ हैं। अविश्वास का उपाय -- ऐसे स्वास्थ्य कार्यकर्ता 'जिन्हें लोग जानते हैं और जिन पर विश्वास करते हैं' -- तभी काम करता है जब लोग पूरे तंत्र से अधिक परिचित कार्यकर्ताओं पर भरोसा करें (1)। "
   "और असुविधा का उपाय -- उपयुक्त समय पर टीके को निकट लाना -- यह मानता है कि टीका लगवाना चाहने वाले कुछ अभिभावक इसे आसान होने पर सचमुच लगवाएँगे (2)।",
   "assumptions",
   st=["People trust a health worker they know more than they trust the health system in general.",
       "Some parents who intend to vaccinate their children would do so if it were more convenient."],
   st_hi=["लोग किसी परिचित स्वास्थ्य कार्यकर्ता पर सामान्य स्वास्थ्य तंत्र से अधिक भरोसा करते हैं।",
          "अपने बच्चों को टीका लगवाना चाहने वाले कुछ अभिभावक इसे अधिक सुविधाजनक होने पर लगवा लेंगे।"],
   key=2)
RQ(p, "Specific Detail", "easy", "mcq",
   "According to the passage, why do some parents feel little urgency about vaccination?",
   "परिच्छेद के अनुसार, कुछ अभिभावक टीकाकरण के बारे में कम तात्कालिकता क्यों अनुभव करते हैं?",
   "The passage says that some parents see little risk in diseases that vaccination itself has made rare. It does not say that the vaccines are costly, that they are given only in cities, or that they have been shown not to work.",
   "परिच्छेद कहता है कि कुछ अभिभावक उन रोगों में कम जोखिम देखते हैं जिन्हें स्वयं टीकाकरण ने दुर्लभ बना दिया है। वह यह नहीं कहता कि टीके महँगे हैं, केवल शहरों में लगते हैं, या अप्रभावी सिद्ध हुए हैं।",
   "why-little-urgency",
   opts=["The diseases have become rare, thanks to vaccination itself.",
         "The vaccines are too costly for most families to afford.",
         "The vaccines are offered only in the larger cities.",
         "Studies are said to have shown that the vaccines do not work."],
   opts_hi=["स्वयं टीकाकरण के कारण ये रोग दुर्लभ हो गए हैं।",
            "टीके अधिकांश परिवारों की पहुँच से बहुत महँगे हैं।",
            "टीके केवल बड़े शहरों में दिए जाते हैं।",
            "कहा जाता है कि अध्ययनों ने दिखाया है कि टीके काम नहीं करते।"],
   ans=0, pos=0)

# ------------------------------------------------------------------ P04 desalination (2)
p = passage("p04",
  "Turning seawater into drinking water was once a luxury of rich desert states. Its cost has fallen as membranes have improved, and several coastal cities, Chennai among them, now draw part of their supply from desalination plants. "
  "But the process still takes a great deal of energy, and it leaves behind a salty brine that can harm marine life if it is discharged carelessly. Nor does it help inland towns far from the coast, to which the water would have to be pumped uphill at further cost. "
  "Desalination can make a coastal city's supply more secure in a drought, but it is an expensive last resort, best used after cheaper steps such as repairing leaking pipes and reusing treated waste water.",
  "समुद्री पानी को पीने योग्य बनाना कभी धनी रेगिस्तानी राज्यों की विलासिता था। झिल्लियों में सुधार के साथ इसकी लागत घटी है, और चेन्नई सहित कई तटीय शहर अब अपनी आपूर्ति का एक भाग विलवणीकरण संयंत्रों से लेते हैं। "
  "पर इस प्रक्रिया में अब भी बहुत ऊर्जा लगती है, और यह एक खारा अवशेष (ब्राइन) छोड़ती है जो लापरवाही से छोड़े जाने पर समुद्री जीवन को हानि पहुँचा सकता है। न ही यह तट से दूर के भीतरी कस्बों की सहायता करता है, जहाँ तक पानी को अतिरिक्त लागत पर ऊपर की ओर पंप करके ले जाना पड़ेगा। "
  "विलवणीकरण सूखे में किसी तटीय शहर की आपूर्ति को अधिक सुरक्षित बना सकता है, पर यह एक महँगा अंतिम उपाय है, जिसका सबसे अच्छा प्रयोग रिसते पाइपों की मरम्मत और उपचारित अपशिष्ट जल के पुनः उपयोग जैसे सस्ते क़दमों के बाद होता है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage grants that desalination has become cheaper and can secure a coastal city's supply in a drought, then lists its costs -- energy, brine, little use inland -- and concludes that it is a last resort after cheaper steps. "
   "It does not call it the best answer for every town, it does not say the brine is harmless (it can harm marine life if discharged carelessly), and it does not say desalination is still limited to rich desert states.",
   "परिच्छेद मानता है कि विलवणीकरण सस्ता हुआ है और सूखे में तटीय शहर की आपूर्ति सुरक्षित कर सकता है, फिर उसकी लागतें गिनाता है -- ऊर्जा, ब्राइन, भीतरी क्षेत्रों में कम उपयोग -- और निष्कर्ष निकालता है कि यह सस्ते क़दमों के बाद का अंतिम उपाय है। "
   "वह इसे हर कस्बे के लिए सबसे अच्छा उत्तर नहीं कहता, ब्राइन को हानिरहित नहीं कहता (लापरवाही से छोड़े जाने पर वह समुद्री जीवन को हानि पहुँचा सकता है), और यह नहीं कहता कि विलवणीकरण अब भी धनी रेगिस्तानी राज्यों तक सीमित है।",
   "crux",
   opts=["Desalination is now the cheapest and best source of water for every town, inland or coastal.",
         "The brine left by desalination is harmless and can be released into the sea without any care.",
         "Desalination remains a luxury that only the rich desert states of the world can afford.",
         "Desalination can secure coastal supply, but it is a costly last resort after cheaper steps."],
   opts_hi=["विलवणीकरण अब हर कस्बे के लिए, भीतरी हो या तटीय, पानी का सबसे सस्ता और सबसे अच्छा स्रोत है।",
            "विलवणीकरण से बचा ब्राइन हानिरहित है और बिना किसी सावधानी के समुद्र में छोड़ा जा सकता है।",
            "विलवणीकरण अब भी एक विलासिता है जिसे दुनिया के केवल धनी रेगिस्तानी राज्य वहन कर सकते हैं।",
            "विलवणीकरण तटीय आपूर्ति सुरक्षित कर सकता है, पर सस्ते क़दमों के बाद यह महँगा अंतिम उपाय है।"],
   ans=3, pos=3)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Only 1 is valid. The passage says the water would have to be pumped uphill to inland towns 'at further cost', so for a town far from the sea and well above it, desalinated water would cost more than for a coastal city. "
   "2 is not valid: the passage advises using desalination after repairing leaks and reusing waste water, not instead of them; a city with leaking pipes should fix them first.",
   "केवल 1 वैध है। परिच्छेद कहता है कि भीतरी कस्बों तक पानी को 'अतिरिक्त लागत पर' ऊपर की ओर पंप करना पड़ेगा, इसलिए समुद्र से दूर और उससे काफ़ी ऊँचाई पर बसे कस्बे के लिए विलवणीकृत पानी किसी तटीय शहर से महँगा पड़ेगा। "
   "2 वैध नहीं है: परिच्छेद रिसाव की मरम्मत और अपशिष्ट जल के पुनः उपयोग के बाद विलवणीकरण की सलाह देता है, उनके बदले नहीं; रिसते पाइपों वाले शहर को पहले उन्हें ठीक करना चाहिए।",
   "conclusions",
   st=["Desalinated water would cost more for a town far inland and high above the sea than for a coastal city.",
       "A city whose pipes leak badly should build a desalination plant before repairing them."],
   st_hi=["समुद्र से काफ़ी ऊँचाई पर बसे दूर के भीतरी कस्बे के लिए विलवणीकृत पानी किसी तटीय शहर से महँगा पड़ेगा।",
          "जिस शहर के पाइप बुरी तरह रिसते हैं, उसे उनकी मरम्मत से पहले विलवणीकरण संयंत्र बनाना चाहिए।"],
   key=0)

# ------------------------------------------------------------------ P05 merit and luck (3)
p = passage("p05",
  "It is comforting to believe that people get what they deserve: that those who rise do so by talent and effort, and those who fall short simply did not try hard enough. Talent and effort matter. But so does a great deal that nobody earns -- the family one is born into, the schools nearby, good health, "
  "and the accidents of timing that open or close a door. Even the capacity for sustained effort is shaped early by circumstances a child does not choose. None of this means that success is mere luck, or that rewarding effort is wrong. "
  "It means that those who have done well have reason for some humility, and that a society which treats its rewards as wholly deserved will find it easy to ignore those whom luck has passed by.",
  "यह मानना सुखद है कि लोगों को वही मिलता है जिसके वे योग्य हैं: कि जो ऊपर उठते हैं वे प्रतिभा और प्रयास से उठते हैं, और जो पीछे रह जाते हैं उन्होंने बस पर्याप्त प्रयास नहीं किया। प्रतिभा और प्रयास मायने रखते हैं। पर बहुत कुछ ऐसा भी मायने रखता है जो कोई कमाता नहीं -- जिस परिवार में कोई जन्म लेता है, पास के विद्यालय, अच्छा स्वास्थ्य, "
  "और समय के वे संयोग जो कोई द्वार खोलते या बंद करते हैं। निरंतर प्रयास की क्षमता भी जल्दी ही उन परिस्थितियों से आकार लेती है जिन्हें कोई बच्चा नहीं चुनता। इसका अर्थ यह नहीं कि सफलता केवल भाग्य है, या कि प्रयास को पुरस्कृत करना ग़लत है। "
  "इसका अर्थ यह है कि जिन्होंने अच्छा किया है उनके पास कुछ विनम्रता का कारण है, और कि जो समाज अपने पुरस्कारों को पूरी तरह योग्यता का फल मानता है, उसके लिए उन लोगों की अनदेखी करना आसान होगा जिन्हें भाग्य ने छोड़ दिया।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage accepts that talent and effort matter but adds that much that is unearned shapes success, even the capacity for effort; it concludes that the successful should have some humility and that treating rewards as wholly deserved makes it easy to ignore the unlucky. "
   "It says that this does not mean success is 'mere luck' or that rewarding effort is wrong, and it does not say effort has no effect.",
   "परिच्छेद मानता है कि प्रतिभा और प्रयास मायने रखते हैं, पर जोड़ता है कि बहुत कुछ अनर्जित सफलता को आकार देता है, प्रयास की क्षमता को भी; वह निष्कर्ष निकालता है कि सफल लोगों में कुछ विनम्रता होनी चाहिए और कि पुरस्कारों को पूरी तरह योग्यता का फल मानने से भाग्यहीनों की अनदेखी आसान हो जाती है। "
   "वह कहता है कि इसका अर्थ यह नहीं कि सफलता 'केवल भाग्य' है या प्रयास को पुरस्कृत करना ग़लत है, और वह यह नहीं कहता कि प्रयास का कोई प्रभाव नहीं।",
   "crux",
   opts=["Success depends entirely on luck, so effort deserves no reward at all from society.",
         "People who fall short in life have simply not tried as hard as those who succeed.",
         "Since luck shapes success, the fortunate owe some humility and concern for others.",
         "Talent and effort have no real effect on how well a person does in the course of a life."],
   opts_hi=["सफलता पूरी तरह भाग्य पर निर्भर है, इसलिए प्रयास समाज से किसी पुरस्कार का पात्र नहीं।",
            "जीवन में पीछे रह जाने वाले लोगों ने बस सफल होने वालों जितना प्रयास नहीं किया।",
            "भाग्य सफलता गढ़ता है, इसलिए भाग्यशालियों में विनम्रता और दूसरों की चिंता होनी चाहिए।",
            "किसी व्यक्ति के जीवन में उसके अच्छा करने पर प्रतिभा और प्रयास का कोई वास्तविक प्रभाव नहीं।"],
   ans=2, pos=2)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Neither is valid. 1 is contradicted: the passage says that even the capacity for sustained effort 'is shaped early by circumstances a child does not choose', so it is not wholly a matter of personal choice. "
   "2 is also contradicted: the passage says that none of this means 'rewarding effort is wrong'; it argues for humility, not for ending rewards.",
   "कोई भी वैध नहीं है। 1 का खंडन होता है: परिच्छेद कहता है कि निरंतर प्रयास की क्षमता भी 'जल्दी ही उन परिस्थितियों से आकार लेती है जिन्हें कोई बच्चा नहीं चुनता', इसलिए वह पूरी तरह व्यक्तिगत चुनाव का विषय नहीं है। "
   "2 का भी खंडन होता है: परिच्छेद कहता है कि इसका अर्थ यह नहीं कि 'प्रयास को पुरस्कृत करना ग़लत है'; वह विनम्रता का तर्क देता है, पुरस्कार समाप्त करने का नहीं।",
   "conclusions",
   st=["How much effort a person can sustain is wholly a matter of personal choice.",
       "Since luck shapes success, a society should stop rewarding effort altogether."],
   st_hi=["कोई व्यक्ति कितना प्रयास निरंतर कर सकता है, यह पूरी तरह व्यक्तिगत चुनाव का विषय है।",
          "चूँकि भाग्य सफलता को आकार देता है, समाज को प्रयास को पुरस्कृत करना पूरी तरह बंद कर देना चाहिए।"],
   key=3)
RQ(p, "Assumption", "medium", "s2", ASSUME, ASSUME_HI,
   "Only 2 is assumed. The passage warns that a society treating its rewards as wholly deserved 'will find it easy to ignore' the unlucky; that warning presumes that what people believe about desert affects how they treat others. "
   "1 is not assumed: the passage says that success is not 'mere luck', and it nowhere claims that the poor have had worse luck than the rich in every case.",
   "केवल 2 पूर्वधारणा है। परिच्छेद चेताता है कि अपने पुरस्कारों को पूरी तरह योग्यता का फल मानने वाले समाज के लिए भाग्यहीनों की 'अनदेखी करना आसान होगा'; यह चेतावनी मानती है कि योग्यता के बारे में लोगों का विश्वास इस पर असर डालता है कि वे दूसरों से कैसा व्यवहार करते हैं। "
   "1 पूर्वधारणा नहीं है: परिच्छेद कहता है कि सफलता 'केवल भाग्य' नहीं है, और कहीं दावा नहीं करता कि हर मामले में ग़रीबों का भाग्य अमीरों से बुरा रहा है।",
   "assumptions",
   st=["In every case, those who are poor have had worse luck than those who are rich.",
       "What people believe about whether success is deserved affects how they treat those who are less successful."],
   st_hi=["हर मामले में ग़रीबों का भाग्य अमीरों से बुरा रहा है।",
          "सफलता योग्यता का फल है या नहीं, इस बारे में लोगों का विश्वास इस पर असर डालता है कि वे कम सफल लोगों से कैसा व्यवहार करते हैं।"],
   key=1)

# ------------------------------------------------------------------ P06 knowledge that cannot be written down (3)
p = passage("p06",
  "A master potter can tell from the feel of the clay whether it is ready, and a good nurse can sense that a patient is worsening before the instruments show it. Much of what skilled people know cannot be fully written down: they know more than they can say. "
  "Such knowledge passes from person to person by watching, trying, being corrected and trying again -- which is why crafts have long been learned through years of apprenticeship rather than from books. Manuals and videos help, and they can spread the explicit part of a skill to thousands at once. "
  "But a workplace that replaces its experienced hands with written procedures, believing that everything worth knowing has been recorded, may find that it has kept the instructions and lost the skill.",
  "एक कुशल कुम्हार मिट्टी को छूकर बता सकता है कि वह तैयार है या नहीं, और एक अच्छी नर्स उपकरणों के दिखाने से पहले भाँप सकती है कि मरीज़ की हालत बिगड़ रही है। कुशल लोग जो जानते हैं उसका बहुत-सा भाग पूरी तरह लिखा नहीं जा सकता: वे जितना कह सकते हैं उससे अधिक जानते हैं। "
  "ऐसा ज्ञान देखकर, करके, सुधारे जाकर और फिर करके एक व्यक्ति से दूसरे तक पहुँचता है -- इसीलिए शिल्प लंबे समय से पुस्तकों के बजाय वर्षों की शागिर्दी से सीखे जाते रहे हैं। पुस्तिकाएँ और वीडियो सहायता करते हैं, और वे किसी कौशल के स्पष्ट भाग को एक साथ हज़ारों तक पहुँचा सकते हैं। "
  "पर जो कार्यस्थल अपने अनुभवी हाथों की जगह लिखित प्रक्रियाएँ रख देता है, यह मानकर कि जानने योग्य सब कुछ दर्ज हो चुका है, वह पा सकता है कि उसने निर्देश तो रख लिए पर कौशल खो दिया।")
RQ(p, "Best Summary", "medium", "mcq", MSG, MSG_HI,
   "The passage says that much skilled knowledge cannot be written down and passes through practice and correction; written material spreads the explicit part, but replacing experienced people with procedures can lose the skill. "
   "It does not call manuals useless (they 'help'); it does not say a skill can be fully learned from books; and it says nothing about technology making crafts obsolete.",
   "परिच्छेद कहता है कि कुशल लोगों का बहुत-सा ज्ञान लिखा नहीं जा सकता और अभ्यास तथा सुधार से आगे बढ़ता है; लिखित सामग्री स्पष्ट भाग फैलाती है, पर अनुभवी लोगों की जगह प्रक्रियाएँ रखने से कौशल खो सकता है। "
   "वह पुस्तिकाओं को व्यर्थ नहीं कहता (वे 'सहायता करती हैं'); वह यह नहीं कहता कि कोई कौशल पूरी तरह पुस्तकों से सीखा जा सकता है; और वह तकनीक द्वारा शिल्पों को अप्रचलित करने के बारे में कुछ नहीं कहता।",
   "message",
   opts=["Manuals and videos are useless for teaching any skill, and should be given up altogether.",
         "Any skill, however fine, can be learned in full from a well-written book or a good video.",
         "Modern technology will soon make crafts such as pottery and their old skills obsolete.",
         "Much skill lives in practice and cannot all be written down, so experience must be kept."],
   opts_hi=["पुस्तिकाएँ और वीडियो किसी भी कौशल को सिखाने में व्यर्थ हैं, और उन्हें पूरी तरह छोड़ देना चाहिए।",
            "कोई भी कौशल, चाहे कितना ही बारीक हो, किसी अच्छी लिखी पुस्तक या अच्छे वीडियो से पूरा सीखा जा सकता है।",
            "आधुनिक तकनीक जल्दी ही कुम्हारी जैसे शिल्पों और उनके पुराने कौशलों को अप्रचलित कर देगी।",
            "बहुत-सा कौशल अभ्यास में बसता है और पूरा लिखा नहीं जा सकता, इसलिए अनुभव को बनाए रखना होगा।"],
   ans=3, pos=3)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Both are valid. 1: the passage says that manuals and videos 'can spread the explicit part of a skill to thousands at once', which an apprenticeship with one master cannot do. "
   "2: the nurse 'can sense that a patient is worsening before the instruments show it', so some of what an experienced nurse notices is not yet captured by the instruments.",
   "दोनों वैध हैं। 1: परिच्छेद कहता है कि पुस्तिकाएँ और वीडियो 'किसी कौशल के स्पष्ट भाग को एक साथ हज़ारों तक पहुँचा सकते हैं', जो किसी एक उस्ताद के साथ शागिर्दी नहीं कर सकती। "
   "2: नर्स 'उपकरणों के दिखाने से पहले भाँप सकती है कि मरीज़ की हालत बिगड़ रही है', इसलिए अनुभवी नर्स जो देखती है उसका कुछ भाग अभी उपकरण नहीं पकड़ते।",
   "conclusions",
   st=["Written material can reach far more learners at once than an apprenticeship can.",
       "Some of what an experienced nurse notices is not yet picked up by the instruments."],
   st_hi=["लिखित सामग्री एक साथ शागिर्दी की तुलना में कहीं अधिक सीखने वालों तक पहुँच सकती है।",
          "अनुभवी नर्स जो देखती है उसका कुछ भाग अभी उपकरण नहीं पकड़ते।"],
   key=2)
RQ(p, "Specific Detail", "easy", "mcq",
   "According to the passage, why have crafts long been learned through apprenticeship?",
   "परिच्छेद के अनुसार, शिल्प लंबे समय से शागिर्दी से क्यों सीखे जाते रहे हैं?",
   "The passage says that such knowledge passes from person to person by watching, trying, being corrected and trying again, which is why crafts have long been learned through apprenticeship. It does not mention books being scarce, the law, or the cost of materials.",
   "परिच्छेद कहता है कि ऐसा ज्ञान देखकर, करके, सुधारे जाकर और फिर करके एक व्यक्ति से दूसरे तक पहुँचता है, इसीलिए शिल्प लंबे समय से शागिर्दी से सीखे जाते रहे हैं। वह पुस्तकों की कमी, क़ानून या सामग्री की लागत का उल्लेख नहीं करता।",
   "why-apprenticeship",
   opts=["Their knowledge passes by watching, trying and being corrected.",
         "Books on the crafts were too rare and far too costly to buy at the time.",
         "The law required every craftsman to train an apprentice.",
         "The materials were too costly to let beginners use alone."],
   opts_hi=["उनका ज्ञान देखने, करने और सुधारे जाने से आगे बढ़ता है।",
            "उस समय शिल्पों पर पुस्तकें बहुत दुर्लभ थीं और ख़रीदने में बहुत महँगी थीं।",
            "क़ानून हर कारीगर से एक शागिर्द को प्रशिक्षित करवाता था।",
            "सामग्री इतनी महँगी थी कि शुरुआती लोगों को अकेले प्रयोग नहीं करने दी जाती थी।"],
   ans=0, pos=0)

# ------------------------------------------------------------------ P07 risk compensation (3)
p = passage("p07",
  "Safety measures do not always deliver all the safety they promise, because people adjust to them. Drivers whose cars have better brakes may follow the car in front more closely; walkers who feel protected by a new crossing may look less carefully before stepping out. "
  "Economists call this risk compensation: some of the benefit of a safer environment is taken back as riskier behaviour. The size of the effect is disputed, and for many measures it is small; seat belts, for instance, have clearly saved many lives despite it. "
  "The lesson is not that safety measures are pointless but that their effect should be judged by what happens on the road, not by what they would achieve if behaviour stayed the same. Measures that work even when people do not change their behaviour, such as barriers that physically separate traffic, are the least likely to be undone in this way.",
  "सुरक्षा उपाय हमेशा वह पूरी सुरक्षा नहीं देते जिसका वे वादा करते हैं, क्योंकि लोग उनके अनुसार अपने को ढाल लेते हैं। जिन चालकों की गाड़ियों में बेहतर ब्रेक हैं, वे आगे वाली गाड़ी के अधिक पास चल सकते हैं; जो पैदल यात्री किसी नए पारपथ से सुरक्षित महसूस करते हैं, वे सड़क पर उतरने से पहले कम ध्यान से देख सकते हैं। "
  "अर्थशास्त्री इसे जोखिम क्षतिपूर्ति कहते हैं: अधिक सुरक्षित वातावरण का कुछ लाभ अधिक जोखिम भरे व्यवहार के रूप में वापस ले लिया जाता है। इस प्रभाव का आकार विवादित है, और कई उपायों के लिए यह छोटा है; उदाहरण के लिए, सीट बेल्ट ने इसके बावजूद स्पष्ट रूप से अनेक जानें बचाई हैं। "
  "सीख यह नहीं कि सुरक्षा उपाय व्यर्थ हैं, बल्कि यह कि उनके प्रभाव को सड़क पर वास्तव में जो होता है उससे आँका जाना चाहिए, न कि इससे कि व्यवहार वैसा ही रहता तो वे क्या करते। ऐसे उपाय जो लोगों के व्यवहार न बदलने पर भी काम करते हैं, जैसे यातायात को भौतिक रूप से अलग करने वाले अवरोधक, इस तरह निष्फल होने की सबसे कम संभावना रखते हैं।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage describes how people can take back part of a safety measure's benefit through riskier behaviour, notes that the effect is disputed and often small, and concludes that measures should be judged by actual outcomes, favouring those that work regardless of behaviour. "
   "It says outright that safety measures are not pointless; it says that seat belts have clearly saved many lives; and it calls the effect's size disputed, not always large enough to cancel the benefit.",
   "परिच्छेद बताता है कि लोग अधिक जोखिम भरे व्यवहार से किसी सुरक्षा उपाय के लाभ का कुछ भाग वापस ले सकते हैं, दर्ज करता है कि यह प्रभाव विवादित और प्रायः छोटा है, और निष्कर्ष निकालता है कि उपायों को वास्तविक परिणामों से आँका जाए, उन उपायों को प्राथमिकता देते हुए जो व्यवहार से निरपेक्ष काम करते हैं। "
   "वह स्पष्ट कहता है कि सुरक्षा उपाय व्यर्थ नहीं हैं; वह कहता है कि सीट बेल्ट ने स्पष्ट रूप से अनेक जानें बचाई हैं; और वह प्रभाव के आकार को विवादित कहता है, न कि हमेशा इतना बड़ा कि लाभ को समाप्त कर दे।",
   "crux",
   opts=["Safety measures are pointless, because people always become reckless enough to cancel them out.",
         "Seat belts have made roads more dangerous by encouraging drivers to drive faster than before.",
         "Risk compensation always outweighs the benefit of any new safety measure on the roads.",
         "People may offset safety gains by taking risks, so measures should be judged by real outcomes."],
   opts_hi=["सुरक्षा उपाय व्यर्थ हैं, क्योंकि लोग हमेशा इतने लापरवाह हो जाते हैं कि उन्हें निष्फल कर दें।",
            "सीट बेल्ट ने चालकों को पहले से तेज़ चलाने के लिए प्रोत्साहित करके सड़कों को अधिक ख़तरनाक बना दिया है।",
            "जोखिम क्षतिपूर्ति हमेशा सड़कों पर किसी भी नए सुरक्षा उपाय के लाभ से अधिक होती है।",
            "लोग जोखिम लेकर सुरक्षा के लाभ की भरपाई कर सकते हैं, इसलिए उपायों को वास्तविक परिणामों से आँकें।"],
   ans=3, pos=3)
RQ(p, "Inference", "hard", "mcq",
   "On the basis of the passage, which one of the following road-safety measures is least likely to have its benefit reduced by risk compensation?",
   "परिच्छेद के आधार पर, निम्नलिखित में से किस सड़क-सुरक्षा उपाय का लाभ जोखिम क्षतिपूर्ति से घटने की सबसे कम संभावना है?",
   "The passage says that measures which work even when people do not change their behaviour, such as barriers that physically separate traffic, are the least likely to be undone. A concrete divider between oncoming lanes prevents head-on collisions however people drive. "
   "Better brakes and a better-lit crossing are exactly the kind of measures that invite people to take more risk (following closely, looking less), and a smoother, wider road may tempt drivers to go faster.",
   "परिच्छेद कहता है कि जो उपाय लोगों के व्यवहार न बदलने पर भी काम करते हैं, जैसे यातायात को भौतिक रूप से अलग करने वाले अवरोधक, उनके निष्फल होने की सबसे कम संभावना है। आमने-सामने की लेनों के बीच कंक्रीट का विभाजक आमने-सामने की टक्कर रोकता है, लोग चाहे जैसे चलाएँ। "
   "बेहतर ब्रेक और अधिक रोशनी वाला पारपथ ठीक वही उपाय हैं जो लोगों को अधिक जोखिम लेने के लिए प्रेरित करते हैं (पास चलना, कम देखना), और चिकनी, चौड़ी सड़क चालकों को तेज़ चलाने के लिए ललचा सकती है।",
   "least-undone",
   opts=["Fitting all new cars with brakes that bring them to a stop in a shorter distance",
         "A concrete divider that physically separates the two directions of traffic",
         "Brighter lights and fresh paint at a busy pedestrian crossing",
         "Widening and smoothing a winding road so that it feels easier to drive"],
   opts_hi=["सभी नई गाड़ियों में ऐसे ब्रेक लगाना जो उन्हें पहले से कम दूरी में रोक दें",
            "यातायात की दोनों दिशाओं को भौतिक रूप से अलग करने वाला कंक्रीट का विभाजक",
            "किसी व्यस्त पैदल पारपथ पर अधिक तेज़ रोशनी और नया रंग",
            "किसी घुमावदार सड़क को चौड़ा और चिकना करना ताकि उस पर चलाना आसान लगे"],
   ans=1, pos=1)
RQ(p, "Assumption", "hard", "s2", ASSUME, ASSUME_HI,
   "Only 1 is assumed. Risk compensation, as the passage describes it, works only if people can perceive that their surroundings have become safer -- the driver must know the brakes are better, the walker must feel protected -- and adjust to that perception. "
   "2 is not assumed: the passage says the effect is disputed and often small, and that seat belts have clearly saved lives; it does not assume that every driver offsets every gain.",
   "केवल 1 पूर्वधारणा है। परिच्छेद में वर्णित जोखिम क्षतिपूर्ति तभी चलती है जब लोग समझ सकें कि उनका परिवेश अधिक सुरक्षित हो गया है -- चालक को पता हो कि ब्रेक बेहतर हैं, पैदल यात्री सुरक्षित महसूस करे -- और उस धारणा के अनुसार अपने को ढालें। "
   "2 पूर्वधारणा नहीं है: परिच्छेद कहता है कि प्रभाव विवादित और प्रायः छोटा है, और सीट बेल्ट ने स्पष्ट रूप से जानें बचाई हैं; वह यह नहीं मानता कि हर चालक हर लाभ की भरपाई कर देता है।",
   "assumptions",
   st=["People notice when their surroundings have been made safer and adjust their behaviour to it.",
       "Every driver fully offsets every safety improvement by driving more dangerously."],
   st_hi=["लोग ध्यान देते हैं कि उनका परिवेश अधिक सुरक्षित बनाया गया है और उसके अनुसार अपना व्यवहार ढालते हैं।",
          "हर चालक अधिक ख़तरनाक ढंग से चलाकर हर सुरक्षा सुधार की पूरी भरपाई कर देता है।"],
   key=0)

# ------------------------------------------------------------------ P08 glaciers as water towers (2)
p = passage("p08",
  "The glaciers of the Himalaya are often called water towers, but their importance differs from river to river. In basins that get most of their water from monsoon rain, meltwater from glaciers is a small share of the yearly flow; in drier basins to the west, it is a much larger share, "
  "and it matters most in the hot, dry weeks before the monsoon, when rivers would otherwise run low. As glaciers shrink in a warming climate, their melt at first increases, swelling the rivers for a time. That extra water is not a gift that lasts: "
  "once the glaciers have shrunk enough, their melt will begin to decline, and the rivers that depend on it most will lose flow just when it is most needed.",
  "हिमालय के हिमनदों को प्रायः जल-मीनार कहा जाता है, पर उनका महत्व हर नदी के लिए अलग है। जिन बेसिनों को अपना अधिकांश पानी मानसूनी वर्षा से मिलता है, उनमें हिमनदों का पिघला पानी वार्षिक प्रवाह का छोटा भाग है; पश्चिम के अधिक शुष्क बेसिनों में यह कहीं बड़ा भाग है, "
  "और सबसे अधिक मायने मानसून से पहले के गर्म, सूखे हफ़्तों में रखता है, जब नदियाँ अन्यथा कम बहतीं। गर्म होती जलवायु में जैसे-जैसे हिमनद सिकुड़ते हैं, उनका पिघलना पहले बढ़ता है, जिससे कुछ समय के लिए नदियाँ फूल जाती हैं। वह अतिरिक्त पानी कोई टिकाऊ उपहार नहीं है: "
  "एक बार हिमनद पर्याप्त सिकुड़ जाएँ, तो उनका पिघलना घटने लगेगा, और उस पर सबसे अधिक निर्भर नदियाँ ठीक तब प्रवाह खोएँगी जब उसकी सबसे अधिक आवश्यकता होती है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage shows that glaciers matter more to some rivers than others -- most to drier basins in the pre-monsoon weeks -- and warns that shrinking glaciers raise melt only for a while before it declines. "
   "It says that meltwater is a small share in monsoon-fed basins, so not all rivers depend on it mainly; it calls the extra melt a passing effect, not a lasting gain; and it does not say glaciers are growing.",
   "परिच्छेद दिखाता है कि हिमनद कुछ नदियों के लिए दूसरों से अधिक मायने रखते हैं -- सबसे अधिक शुष्क बेसिनों के लिए मानसून-पूर्व हफ़्तों में -- और चेताता है कि सिकुड़ते हिमनद पिघलन को केवल कुछ समय बढ़ाते हैं, फिर वह घटती है। "
   "वह कहता है कि मानसून-पोषित बेसिनों में पिघला पानी छोटा भाग है, इसलिए सभी नदियाँ मुख्यतः उस पर निर्भर नहीं; वह अतिरिक्त पिघलन को अस्थायी प्रभाव कहता है, टिकाऊ लाभ नहीं; और वह यह नहीं कहता कि हिमनद बढ़ रहे हैं।",
   "crux",
   opts=["All Himalayan rivers get most of their yearly water from the melting of glaciers.",
         "The faster melting of shrinking glaciers will give the rivers more water for ever.",
         "Melt matters most to some rivers, and its rise as glaciers shrink will not last.",
         "Himalayan glaciers are growing in size as the monsoon brings more snow each year."],
   opts_hi=["हिमालय की सभी नदियाँ अपना अधिकांश वार्षिक पानी हिमनदों के पिघलने से पाती हैं।",
            "सिकुड़ते हिमनदों का तेज़ पिघलना नदियों को हमेशा के लिए पहले से कहीं अधिक पानी देता रहेगा।",
            "पिघलन कुछ नदियों के लिए अधिक मायने रखती है, और हिमनद सिकुड़ने पर उसकी वृद्धि टिकेगी नहीं।",
            "मानसून हर वर्ष अधिक बर्फ़ लाता है, इसलिए हिमालय के हिमनद आकार में बढ़ रहे हैं।"],
   ans=2, pos=2)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Only 2 is valid: meltwater 'matters most in the hot, dry weeks before the monsoon, when rivers would otherwise run low', so for a basin that relies on it, a decline in melt would show most clearly in those weeks. "
   "1 is not valid: the passage says the extra flow from faster melting 'is not a gift that lasts' -- a rise in river flow now does not show that the glaciers are healthy, and may be a sign of their shrinking.",
   "केवल 2 वैध है: पिघला पानी 'मानसून से पहले के गर्म, सूखे हफ़्तों में सबसे अधिक मायने रखता है, जब नदियाँ अन्यथा कम बहतीं', इसलिए उस पर निर्भर बेसिन में पिघलन की कमी उन्हीं हफ़्तों में सबसे स्पष्ट दिखेगी। "
   "1 वैध नहीं है: परिच्छेद कहता है कि तेज़ पिघलन से अतिरिक्त प्रवाह 'कोई टिकाऊ उपहार नहीं है' -- अभी नदी के प्रवाह में वृद्धि यह नहीं दिखाती कि हिमनद स्वस्थ हैं, और उनके सिकुड़ने का संकेत हो सकती है।",
   "conclusions",
   st=["A rise in a glacier-fed river's flow over recent years shows that its glaciers are in good health.",
       "In a basin that relies on meltwater, a decline in melt would be felt most in the weeks before the monsoon."],
   st_hi=["हाल के वर्षों में हिमनद-पोषित किसी नदी के प्रवाह में वृद्धि दिखाती है कि उसके हिमनद अच्छी स्थिति में हैं।",
          "पिघले पानी पर निर्भर किसी बेसिन में पिघलन की कमी सबसे अधिक मानसून से पहले के हफ़्तों में महसूस होगी।"],
   key=1)

# ------------------------------------------------------------------ P09 a universal basic income (3)
p = passage("p09",
  "A universal basic income would pay every adult a fixed sum, without conditions. Its supporters value its simplicity: no one would be wrongly left out because of a missing document or a mistaken list, and no official would have to decide who deserves help. "
  "Critics raise two objections. A sum large enough to matter, paid to everyone, would cost a great deal, and the money would have to come from higher taxes or from cutting other programmes -- some of which, such as subsidised food or rural jobs, may serve the poor better. "
  "The second objection, that people would stop working, finds less support: small trials, including some in Indian villages, have found little sign of it, and some recipients worked more, using the money to buy tools or seed. "
  "The real question is less whether people can be trusted with cash than what would have to give way to pay for it.",
  "सार्वभौमिक बुनियादी आय हर वयस्क को बिना किसी शर्त के एक निश्चित राशि देगी। इसके समर्थक इसकी सरलता को महत्व देते हैं: किसी ग़ायब दस्तावेज़ या ग़लत सूची के कारण कोई ग़लती से बाहर नहीं छूटेगा, और किसी अधिकारी को यह तय नहीं करना होगा कि सहायता का पात्र कौन है। "
  "आलोचक दो आपत्तियाँ उठाते हैं। सबको दी जाने वाली ऐसी राशि जो वास्तव में मायने रखे, बहुत महँगी होगी, और पैसा ऊँचे करों से या दूसरे कार्यक्रमों में कटौती से आना होगा -- जिनमें से कुछ, जैसे सस्ता अनाज या ग्रामीण रोज़गार, ग़रीबों की बेहतर सेवा कर सकते हैं। "
  "दूसरी आपत्ति, कि लोग काम करना छोड़ देंगे, को कम समर्थन मिलता है: छोटे परीक्षणों में, भारतीय गाँवों के कुछ परीक्षणों सहित, इसके बहुत कम संकेत मिले हैं, और कुछ प्राप्तकर्ताओं ने पैसे से औज़ार या बीज ख़रीदकर अधिक काम किया। "
  "वास्तविक प्रश्न यह कम है कि लोगों पर नक़द के मामले में भरोसा किया जा सकता है या नहीं, और अधिक यह कि इसका भुगतान करने के लिए किसे जगह छोड़नी होगी।")
RQ(p, "Best Summary", "medium", "mcq", MSG, MSG_HI,
   "The passage weighs a basic income's simplicity against its cost, finds little support for the fear that people would stop working, and concludes that the real issue is what would have to be cut or taxed to pay for it. "
   "It does not say trials prove people stop working (they found 'little sign of it'); it does not call the scheme cheap; and it does not say it should replace every other programme -- it warns that some may serve the poor better.",
   "परिच्छेद बुनियादी आय की सरलता को उसकी लागत के सामने तौलता है, इस डर को कम समर्थन पाता है कि लोग काम छोड़ देंगे, और निष्कर्ष निकालता है कि वास्तविक मुद्दा यह है कि उसका भुगतान करने के लिए किसमें कटौती या किस पर कर लगाना होगा। "
   "वह यह नहीं कहता कि परीक्षण सिद्ध करते हैं कि लोग काम छोड़ देते हैं (उन्हें 'इसके बहुत कम संकेत मिले'); वह योजना को सस्ता नहीं कहता; और वह यह नहीं कहता कि इसे हर दूसरे कार्यक्रम की जगह लेनी चाहिए -- वह चेताता है कि कुछ ग़रीबों की बेहतर सेवा कर सकते हैं।",
   "message",
   opts=["Trials show that a basic income makes people stop working, so the idea should be dropped at once.",
         "A basic income would be cheap, since it needs no officials to decide who deserves help.",
         "A basic income should replace every other welfare programme, including subsidised food.",
         "The key question is less about work than about what must give way to fund a basic income."],
   opts_hi=["परीक्षण दिखाते हैं कि बुनियादी आय से लोग काम छोड़ देते हैं, इसलिए यह विचार छोड़ देना चाहिए।",
            "बुनियादी आय सस्ती होगी, क्योंकि इसमें यह तय करने के लिए अधिकारियों की आवश्यकता नहीं कि सहायता का पात्र कौन है।",
            "बुनियादी आय को सस्ते अनाज सहित हर दूसरे कल्याण कार्यक्रम की जगह लेनी चाहिए।",
            "बुनियादी आय के बारे में मुख्य प्रश्न काम से कम, और इससे अधिक है कि उसके लिए किसे जगह छोड़नी होगी।"],
   ans=3, pos=3)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Both are valid. 1: the passage says the money would have to come from higher taxes or from cutting other programmes, some of which 'may serve the poor better' -- so funding the income by cutting such a programme could leave some poor families worse off. "
   "2: supporters value that 'no one would be wrongly left out because of a missing document or a mistaken list', which implies that programmes with conditions do sometimes leave out people who should be included.",
   "दोनों वैध हैं। 1: परिच्छेद कहता है कि पैसा ऊँचे करों से या दूसरे कार्यक्रमों में कटौती से आना होगा, जिनमें से कुछ 'ग़रीबों की बेहतर सेवा कर सकते हैं' -- इसलिए ऐसे कार्यक्रम में कटौती से आय का भुगतान कुछ ग़रीब परिवारों को पहले से बुरी स्थिति में छोड़ सकता है। "
   "2: समर्थक इसे महत्व देते हैं कि 'किसी ग़ायब दस्तावेज़ या ग़लत सूची के कारण कोई ग़लती से बाहर नहीं छूटेगा', जिसका अर्थ है कि शर्तों वाले कार्यक्रम कभी-कभी उन लोगों को छोड़ देते हैं जिन्हें शामिल होना चाहिए।",
   "conclusions",
   st=["If a basic income were paid for by cutting a programme that serves the poor well, some poor families could end up worse off.",
       "Programmes that set conditions for help sometimes leave out people who ought to be included."],
   st_hi=["यदि बुनियादी आय का भुगतान ग़रीबों की अच्छी सेवा करने वाले किसी कार्यक्रम में कटौती से किया जाए, तो कुछ ग़रीब परिवार पहले से बुरी स्थिति में पहुँच सकते हैं।",
          "सहायता के लिए शर्तें रखने वाले कार्यक्रम कभी-कभी उन लोगों को छोड़ देते हैं जिन्हें शामिल होना चाहिए।"],
   key=2)
RQ(p, "Specific Detail", "medium", "mcq",
   "According to the passage, what did small trials of cash payments find about work?",
   "परिच्छेद के अनुसार, नक़द भुगतान के छोटे परीक्षणों ने काम के बारे में क्या पाया?",
   "The passage says the trials found little sign that people stopped working, and that some recipients worked more, using the money to buy tools or seed. "
   "It does not say that most recipients stopped work, that the trials were stopped, or that the trials measured only spending on food.",
   "परिच्छेद कहता है कि परीक्षणों में इसके बहुत कम संकेत मिले कि लोगों ने काम छोड़ा, और कुछ प्राप्तकर्ताओं ने पैसे से औज़ार या बीज ख़रीदकर अधिक काम किया। "
   "वह यह नहीं कहता कि अधिकांश प्राप्तकर्ताओं ने काम छोड़ दिया, कि परीक्षण रोक दिए गए, या कि परीक्षणों ने केवल भोजन पर ख़र्च मापा।",
   "what-trials-found",
   opts=["Most recipients stopped working once the payments began to arrive.",
         "Little sign of people stopping work; some used the money to work more.",
         "The trials were stopped early because the payments proved far too costly.",
         "The trials measured only how much the recipients spent on their food."],
   opts_hi=["भुगतान आने लगते ही अधिकांश प्राप्तकर्ताओं ने काम करना छोड़ दिया।",
            "काम छोड़ने के बहुत कम संकेत; कुछ ने पैसे से अधिक काम किया।",
            "भुगतान बहुत महँगे सिद्ध होने के कारण परीक्षण जल्दी रोक दिए गए।",
            "परीक्षणों ने केवल यह मापा कि प्राप्तकर्ताओं ने भोजन पर कितना ख़र्च किया।"],
   ans=1, pos=1)

# ------------------------------------------------------------------ P10 the printing press (3)
p = passage("p10",
  "When printing with movable type spread through Europe in the late fifteenth century, it made books far cheaper and faster to produce than copying by hand. Ideas that had once circulated among a few scholars could now reach thousands, and religious and political pamphlets travelled faster than any authority could suppress them. "
  "Printing also made it possible to compare texts and correct errors, since many readers could check the same edition. Yet the same machines printed falsehoods as readily as truths: sensational accounts of monsters and lurid manuals for hunting witches sold well, "
  "and some of the age's worst persecutions were fuelled by printed material. A new way of spreading words amplifies whatever is put into it; whether it improves understanding depends on the habits of checking and argument that grow up around it.",
  "जब पंद्रहवीं शताब्दी के अंत में चल टाइप से छपाई यूरोप में फैली, तो उसने पुस्तकों को हाथ से नक़ल करने की तुलना में कहीं सस्ता और तेज़ी से बनने योग्य बना दिया। जो विचार कभी कुछ विद्वानों में घूमते थे वे अब हज़ारों तक पहुँच सकते थे, और धार्मिक तथा राजनीतिक पर्चे किसी भी सत्ता के दबा पाने से तेज़ यात्रा करते थे। "
  "छपाई ने पाठों की तुलना करना और त्रुटियाँ सुधारना भी संभव बनाया, क्योंकि अनेक पाठक एक ही संस्करण की जाँच कर सकते थे। फिर भी वही मशीनें सत्य जितनी ही सहजता से झूठ भी छापती थीं: राक्षसों के सनसनीख़ेज़ वृत्तांत और डायनों का शिकार करने की भड़काऊ पुस्तिकाएँ ख़ूब बिकती थीं, "
  "और उस युग के कुछ सबसे बुरे उत्पीड़नों को छपी सामग्री से हवा मिली। शब्दों को फैलाने का कोई नया तरीक़ा उसमें डाली गई हर चीज़ को बढ़ा देता है; वह समझ को बेहतर बनाता है या नहीं, यह उसके चारों ओर पनपने वाली जाँच और तर्क की आदतों पर निर्भर करता है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage credits printing with spreading ideas widely and making texts easier to check, then shows that it spread falsehoods as readily, and concludes that a new medium amplifies whatever goes into it, its value depending on habits of checking and argument. "
   "It does not say printing spread only the truth or that it did more harm than good; and it treats the authorities' failure to suppress pamphlets as a fact, not as a lesson that printing should have been controlled.",
   "परिच्छेद छपाई को विचारों को व्यापक रूप से फैलाने और पाठों की जाँच आसान बनाने का श्रेय देता है, फिर दिखाता है कि उसने झूठ भी उतनी ही सहजता से फैलाया, और निष्कर्ष निकालता है कि नया माध्यम उसमें डाली गई हर चीज़ को बढ़ा देता है, उसका मूल्य जाँच और तर्क की आदतों पर निर्भर करता है। "
   "वह यह नहीं कहता कि छपाई ने केवल सत्य फैलाया या कि उसने भलाई से अधिक हानि की; और वह सत्ता के पर्चे न दबा पाने को एक तथ्य मानता है, इस सीख के रूप में नहीं कि छपाई को नियंत्रित करना चाहिए था।",
   "crux",
   opts=["Printing spread only true and useful ideas, and so it greatly improved understanding at once.",
         "Printing did more harm than good, because it fuelled some of the worst persecutions of the age.",
         "A new medium amplifies whatever is put into it, and its value depends on habits of checking.",
         "Authorities should have controlled printing, since pamphlets spread faster than they could act."],
   opts_hi=["छपाई ने केवल सच्चे और उपयोगी विचार फैलाए, और इसलिए उसने समझ को तुरंत बहुत बेहतर बना दिया।",
            "छपाई ने भलाई से अधिक हानि की, क्योंकि उसने उस युग के कुछ सबसे बुरे उत्पीड़नों को हवा दी।",
            "नया माध्यम उसमें डाली हर चीज़ बढ़ा देता है, और उसका मूल्य जाँच की आदतों पर निर्भर है।",
            "सत्ता को छपाई पर नियंत्रण रखना चाहिए था, क्योंकि पर्चे उसकी कार्रवाई से तेज़ फैलते थे।"],
   ans=2, pos=2)
RQ(p, "Inference", "hard", "mcq",
   "Which one of the following can be inferred from the passage?",
   "परिच्छेद से निम्नलिखित में से किसका अनुमान लगाया जा सकता है?",
   "The passage says that printing let many readers check the same edition, which made it possible to compare texts and correct errors. Copies made by hand differ from one another, so a mistake found in one copy could not be corrected in the same way across all of them; a single printed edition could be checked, and its errors fixed, by many readers at once. "
   "The passage does not say that handwritten books were free of errors, that authorities welcomed pamphlets, or that sensational books sold poorly -- it says they sold well.",
   "परिच्छेद कहता है कि छपाई ने अनेक पाठकों को एक ही संस्करण की जाँच करने दी, जिससे पाठों की तुलना और त्रुटियों का सुधार संभव हुआ। हाथ से बनी प्रतियाँ एक-दूसरे से भिन्न होती हैं, इसलिए किसी एक प्रति में पाई गई भूल को सब प्रतियों में उसी तरह नहीं सुधारा जा सकता था; एक ही छपे संस्करण को अनेक पाठक एक साथ जाँच सकते थे और उसकी त्रुटियाँ ठीक हो सकती थीं। "
   "परिच्छेद यह नहीं कहता कि हाथ से लिखी पुस्तकें त्रुटिहीन थीं, कि सत्ता ने पर्चों का स्वागत किया, या कि सनसनीख़ेज़ पुस्तकें कम बिकीं -- वह कहता है कि वे ख़ूब बिकीं।",
   "what-can-be-inferred",
   opts=["Many readers checking one identical edition helped errors to be found and corrected.",
         "Books copied by hand contained no errors at all before printing came into use.",
         "The authorities of the time welcomed the spread of religious and political pamphlets.",
         "Sensational accounts of monsters found few buyers once printing made books cheap."],
   opts_hi=["एक ही संस्करण को अनेक पाठकों के जाँचने से त्रुटियाँ खोजने और सुधारने में सहायता मिली।",
            "छपाई के प्रयोग में आने से पहले हाथ से नक़ल की गई पुस्तकों में कोई त्रुटि नहीं होती थी।",
            "उस समय की सत्ता ने धार्मिक और राजनीतिक पर्चों के तेज़ प्रसार का खुलकर स्वागत किया।",
            "छपाई से पुस्तकें सस्ती होने पर राक्षसों के सनसनीख़ेज़ वृत्तांतों के ख़रीदार कम मिले।"],
   ans=0, pos=0)
RQ(p, "Assumption", "hard", "s2", ASSUME, ASSUME_HI,
   "Only 2 is assumed. The closing claim -- that whether a medium improves understanding 'depends on the habits of checking and argument that grow up around it' -- takes it for granted that such habits can develop, and that they are not fixed once and for all by the medium itself. "
   "1 is not assumed: the passage says that printing amplified both truths and falsehoods; it makes no claim that most printed books of the time were false.",
   "केवल 2 पूर्वधारणा है। अंतिम दावा -- कि कोई माध्यम समझ को बेहतर बनाता है या नहीं, यह 'उसके चारों ओर पनपने वाली जाँच और तर्क की आदतों पर निर्भर करता है' -- मान लेता है कि ऐसी आदतें विकसित हो सकती हैं, और वे माध्यम द्वारा ही सदा के लिए तय नहीं हो जातीं। "
   "1 पूर्वधारणा नहीं है: परिच्छेद कहता है कि छपाई ने सत्य और झूठ दोनों को बढ़ाया; वह यह कोई दावा नहीं करता कि उस समय की अधिकांश छपी पुस्तकें झूठी थीं।",
   "assumptions",
   st=["Most of the books printed in that age contained falsehoods.",
       "Habits of checking and argument can grow up around a new medium over time."],
   st_hi=["उस युग में छपी अधिकांश पुस्तकों में झूठ भरा था।",
          "किसी नए माध्यम के चारों ओर समय के साथ जाँच और तर्क की आदतें विकसित हो सकती हैं।"],
   key=1)
