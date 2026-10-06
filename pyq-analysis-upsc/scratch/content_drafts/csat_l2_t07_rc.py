# -*- coding: utf-8 -*-
"""CSAT Level 2 · Test 7 -- Reading Comprehension: 10 original passages, 28 items (8 x 3, 2 x 2).

Themes, none used in Tests 1-6: earthquake-resistant building and the code that goes unenforced, biometric
authentication in welfare schemes and the people it turns away, birdwatchers' lists as science, sand taken from
riverbeds, roads and girls' schooling, cheap fertiliser and tired soil, the costs of hosting mega-events,
village health workers and newborns, rooftop solar and the grid, and the overruns of large public projects.
Item types: main idea 7, inference 8, assumption 5, tone 1, specific detail 4 (one of them 'which is NOT
correct'), best summary 3. Options are named by content in every explanation."""
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
NOTCORRECT = "Which one of the following statements is NOT correct according to the passage?"
NOTCORRECT_HI = "परिच्छेद के अनुसार निम्नलिखित में से कौन-सा कथन सही नहीं है?"

# ------------------------------------------------------------------ P01 earthquake-resistant building (3)
p = passage("p01",
  "Earthquakes do not kill people; collapsing buildings do. Two towns struck by tremors of similar strength can suffer very different fates, depending on how their houses were built. "
  "India has had a detailed code for earthquake-resistant construction for decades, yet much of what is built, especially in small towns and villages, never meets it, because plans are rarely inspected and builders know that a fine, "
  "if it comes at all, comes years later. Teaching masons to tie the corners of a house, to lay bands of reinforcement and to keep walls from running too long has been shown to add only a small fraction to its cost. "
  "The difficulty is not in knowing what to do but in getting it done where nobody is watching.",
  "भूकंप लोगों को नहीं मारते; गिरती इमारतें मारती हैं। समान तीव्रता के झटकों से प्रभावित दो कस्बों का भाग्य बहुत अलग हो सकता है, यह इस पर निर्भर करता है कि उनके मकान कैसे बने थे। "
  "भारत में दशकों से भूकंप-रोधी निर्माण की विस्तृत संहिता है, फिर भी जो कुछ बनता है, विशेषकर छोटे कस्बों और गाँवों में, उसका बड़ा भाग उसे कभी पूरा नहीं करता, क्योंकि नक़्शों का निरीक्षण शायद ही होता है और निर्माता जानते हैं कि जुर्माना, "
  "यदि लगता भी है, तो वर्षों बाद लगता है। राजमिस्त्रियों को मकान के कोने बाँधना, सुदृढ़ीकरण की पट्टियाँ डालना और दीवारों को बहुत लंबी न होने देना सिखाने से लागत में केवल एक छोटा अंश जुड़ता है, यह दिखाया जा चुका है। "
  "कठिनाई यह जानने में नहीं कि क्या करना है, बल्कि वहाँ उसे करवाने में है जहाँ कोई देख नहीं रहा।")
RQ(p, "Main Idea", "easy", "mcq", CRUX, CRUX_HI,
   "The passage says that collapsing buildings, not tremors, kill; that the code exists but is not followed because nobody inspects plans and fines come late; and that building to the code adds only a small fraction to the cost. "
   "So what is lacking is enforcement, not money or knowledge. It does not say that the code is out of date, that small towns face stronger tremors, or that teaching masons is the only way to safety.",
   "परिच्छेद कहता है कि झटके नहीं, गिरती इमारतें जान लेती हैं; कि संहिता मौजूद है पर उसका पालन नहीं होता क्योंकि कोई नक़्शों का निरीक्षण नहीं करता और जुर्माना देर से लगता है; और कि संहिता के अनुसार निर्माण से लागत में केवल एक छोटा अंश जुड़ता है। "
   "अतः कमी लागू करने की है, धन या जानकारी की नहीं। वह यह नहीं कहता कि संहिता पुरानी है, कि छोटे कस्बों में तेज़ झटके आते हैं, या कि राजमिस्त्रियों को सिखाना सुरक्षा का एकमात्र रास्ता है।",
   "crux",
   opts=["Making houses safer costs little; what is missing is enforcement of a code that already exists.",
         "Many people die in earthquakes because India's code for earthquake-resistant building is out of date.",
         "Small towns and villages are struck by stronger earthquakes than cities are, so their houses need to be better.",
         "Teaching masons new methods of building is the only way of making the houses of small towns safe from earthquakes."],
   opts_hi=["मकानों को सुरक्षित बनाने में थोड़ा ख़र्च आता है; कमी उस संहिता को लागू करने की है जो पहले से मौजूद है।",
            "भूकंप में कई लोग इसलिए मरते हैं कि भारत की भूकंप-रोधी निर्माण संहिता पुरानी पड़ चुकी है।",
            "छोटे कस्बों और गाँवों में शहरों की तुलना में अधिक तीव्र भूकंप आते हैं, इसलिए उनके मकान बेहतर होने चाहिए।",
            "छोटे कस्बों के मकानों को भूकंप से सुरक्षित बनाने का एकमात्र तरीक़ा राजमिस्त्रियों को निर्माण की नई विधियाँ सिखाना है।"],
   ans=0, pos=2)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Only 2 is valid: the passage links the code's being ignored to plans being rarely inspected and to fines that come years late, which leaves builders little reason to follow it. "
   "1 goes beyond the passage, which speaks of tying corners, bands of reinforcement and shorter walls, and says nothing about steel frames.",
   "केवल 2 वैध है: परिच्छेद संहिता की अनदेखी को नक़्शों के शायद ही निरीक्षण और वर्षों देर से लगने वाले जुर्माने से जोड़ता है, जिससे निर्माताओं के पास उसे मानने का कारण कम रह जाता है। "
   "1 परिच्छेद से आगे चला जाता है, जो कोने बाँधने, सुदृढ़ीकरण की पट्टियों और छोटी दीवारों की बात करता है, और इस्पात के ढाँचों के बारे में कुछ नहीं कहता।",
   "conclusions",
   st=["Most of the deaths in earthquakes would be avoided if every house were built with a steel frame.",
       "Where plans are rarely inspected, builders have little reason to follow the code."],
   st_hi=["यदि हर मकान इस्पात के ढाँचे से बना हो, तो भूकंपों में अधिकांश मौतें टल जाएँगी।",
          "जहाँ नक़्शों का निरीक्षण शायद ही होता है, वहाँ निर्माताओं के पास संहिता को मानने का कारण कम है।"],
   key=1)
RQ(p, "Assumption", "hard", "s2", ASSUME, ASSUME_HI,
   "Only 1 is assumed. The passage puts the difficulty in getting the code followed where nobody is watching, not in knowing what to do; this sets cost aside as a barrier only if households can bear the small extra amount that building to the code adds. "
   "2 is not assumed: the passage says that teaching masons adds little to the cost and nowhere says that they refuse to learn.",
   "केवल 1 पूर्वधारणा है। परिच्छेद कठिनाई को यह जानने में नहीं, बल्कि वहाँ संहिता का पालन करवाने में रखता है जहाँ कोई देख नहीं रहा; यह लागत को बाधा के रूप में तभी किनारे करता है जब परिवार संहिता के अनुसार निर्माण से जुड़ने वाली छोटी अतिरिक्त राशि वहन कर सकें। "
   "2 पूर्वधारणा नहीं है: परिच्छेद कहता है कि राजमिस्त्रियों को सिखाने से लागत में थोड़ा ही जुड़ता है और कहीं नहीं कहता कि वे सीखने से मना करते हैं।",
   "assumptions",
   st=["Households in small towns can bear the small extra cost of building to the code.",
       "Masons in small towns are unwilling to learn safer ways of building."],
   st_hi=["छोटे कस्बों के परिवार संहिता के अनुसार निर्माण की छोटी अतिरिक्त लागत वहन कर सकते हैं।",
          "छोटे कस्बों के राजमिस्त्री निर्माण के सुरक्षित तरीक़े सीखने को तैयार नहीं हैं।"],
   key=0)

# ------------------------------------------------------------------ P02 biometric authentication in welfare schemes (3)
p = passage("p02",
  "When a welfare scheme moves to biometric authentication, leakage falls: ghost beneficiaries cannot be created, and the officials who once pocketed part of a payment have less room to do so. "
  "These gains are easy to count, and they are the ones that get quoted. The cost is harder to count, because it falls on people who appear in no report: a labourer whose fingerprints have worn away, an elderly woman whose hand trembles, "
  "a family in a village where the network is down on the day of distribution. Each is turned away not because they are ineligible but because a machine has failed to recognise them. "
  "A scheme that counts only the leakage it stops, and not the rightful claimants it shuts out, will look better than it is.",
  "जब कोई कल्याण योजना जैव-मापी प्रमाणीकरण पर चली जाती है, तो रिसाव घटता है: फ़र्ज़ी लाभार्थी नहीं बनाए जा सकते, और जो अधिकारी पहले भुगतान का कुछ हिस्सा हड़प लेते थे उनके पास ऐसा करने की गुंजाइश कम रह जाती है। "
  "इन लाभों को गिनना आसान है, और यही उद्धृत किए जाते हैं। क़ीमत को गिनना कठिन है, क्योंकि वह उन लोगों पर पड़ती है जो किसी रिपोर्ट में नहीं आते: ऐसा मज़दूर जिसकी उँगलियों के निशान घिस चुके हैं, ऐसी बुज़ुर्ग महिला जिसका हाथ काँपता है, "
  "ऐसा परिवार जिसके गाँव में वितरण के दिन नेटवर्क बंद है। इनमें से हर किसी को इसलिए नहीं लौटाया जाता कि वे अपात्र हैं, बल्कि इसलिए कि मशीन उन्हें पहचानने में विफल रही। "
  "जो योजना केवल उस रिसाव को गिनती है जिसे उसने रोका, और उन सही दावेदारों को नहीं जिन्हें उसने बाहर कर दिया, वह अपनी वास्तविकता से बेहतर दिखेगी।")
RQ(p, "Best Summary", "medium", "mcq", MSG, MSG_HI,
   "The passage grants that leakage falls, then argues that the cost -- rightful claimants who are turned away -- goes uncounted, so a scheme that counts only the leakage it stops looks better than it is. The message is that both have to be counted. "
   "It does not ask for biometrics to be dropped, it does not call leakage a minor problem (it says that leakage falls), and it does not say that fingerprints are the only way of removing ghost beneficiaries.",
   "परिच्छेद मानता है कि रिसाव घटता है, फिर तर्क देता है कि क़ीमत -- लौटा दिए गए सही दावेदार -- गिनी नहीं जाती, इसलिए जो योजना केवल रोके गए रिसाव को गिनती है वह अपनी वास्तविकता से बेहतर दिखती है। संदेश यह है कि दोनों को गिनना होगा। "
   "वह जैव-मापी प्रणाली को हटाने को नहीं कहता, रिसाव को छोटी समस्या नहीं बताता (वह कहता है कि रिसाव घटता है), और यह नहीं कहता कि फ़र्ज़ी लाभार्थियों को हटाने का एकमात्र रास्ता उँगलियों के निशान हैं।",
   "message",
   opts=["A scheme should be judged by the rightful claimants it misses as well as by the leakage it stops.",
         "Biometric authentication should be dropped from welfare schemes because it does more harm than good.",
         "Leakage in welfare schemes is a minor problem, because few officials pocket any part of a payment.",
         "Ghost beneficiaries can be removed only if every beneficiary is made to prove identity by fingerprints."],
   opts_hi=["योजना को आँकते समय केवल रोके गए रिसाव को नहीं, छूटे हुए सही दावेदारों को भी गिनना चाहिए।",
            "जैव-मापी प्रमाणीकरण को कल्याण योजनाओं से हटा देना चाहिए, क्योंकि उससे लाभ से अधिक हानि होती है।",
            "कल्याण योजनाओं में रिसाव एक छोटी समस्या है, क्योंकि बहुत कम अधिकारी भुगतान का कोई हिस्सा हड़पते हैं।",
            "फ़र्ज़ी लाभार्थी तभी हटाए जा सकते हैं जब हर लाभार्थी से उँगलियों के निशान द्वारा पहचान प्रमाणित करवाई जाए।"],
   ans=0, pos=0)
RQ(p, "Inference", "hard", "sc", INFER, INFER_HI,
   "2 and 3 follow. The passage says that people are turned away although they are eligible because a machine fails to recognise them (2), and that a scheme that counts only the leakage it stops 'will look better than it is' (3). "
   "1 goes too far: the passage says that leakage falls, not that it disappears.",
   "2 और 3 निकलते हैं। परिच्छेद कहता है कि पात्र होते हुए भी लोग इसलिए लौटाए जाते हैं कि मशीन उन्हें पहचानने में विफल रहती है (2), और कि जो योजना केवल रोके गए रिसाव को गिनती है वह 'अपनी वास्तविकता से बेहतर दिखेगी' (3)। "
   "1 बहुत आगे चला जाता है: परिच्छेद कहता है कि रिसाव घटता है, यह नहीं कि वह समाप्त हो जाता है।",
   "conclusions",
   st=["Biometric authentication has removed leakage from welfare payments altogether.",
       "An eligible person can lose a benefit because a machine fails to recognise them.",
       "A scheme's reported success can be greater than its real success."],
   st_hi=["जैव-मापी प्रमाणीकरण ने कल्याण भुगतानों से रिसाव को पूरी तरह समाप्त कर दिया है।",
          "पात्र व्यक्ति इसलिए लाभ से वंचित हो सकता है कि मशीन उसे पहचानने में विफल रहती है।",
          "किसी योजना की बताई गई सफलता उसकी वास्तविक सफलता से अधिक हो सकती है।"],
   opts=["1 only", "1 and 2 only", "2 only", "2 and 3 only"], key=3)
RQ(p, "Specific Detail", "easy", "mcq",
   "According to the passage, why are some rightful claimants turned away?",
   "परिच्छेद के अनुसार कुछ सही दावेदार क्यों लौटा दिए जाते हैं?",
   "The passage says that each is turned away 'not because they are ineligible but because a machine has failed to recognise them'. The other options contradict this or give reasons that the passage does not: ineligibility on checking, "
   "a refusal by the officials who once pocketed payments, and being away from the village on the day of distribution.",
   "परिच्छेद कहता है कि हर किसी को 'इसलिए नहीं लौटाया जाता कि वे अपात्र हैं, बल्कि इसलिए कि मशीन उन्हें पहचानने में विफल रही'। बाक़ी विकल्प इसका खंडन करते हैं या ऐसे कारण देते हैं जो परिच्छेद नहीं देता: जाँच में अपात्रता, "
   "भुगतान हड़पने वाले अधिकारियों का इनकार, और वितरण के दिन गाँव से बाहर होना।",
   "detail",
   opts=["On checking, they are found to be ineligible for the benefit.",
         "The officials who once pocketed payments now refuse to pay them.",
         "They are away from the village on the day of distribution.",
         "The machine that checks identity fails to recognise them."],
   opts_hi=["जाँच करने पर वे लाभ के लिए अपात्र पाए जाते हैं।",
            "जो अधिकारी पहले भुगतान हड़पते थे वे अब उन्हें भुगतान करने से मना कर देते हैं।",
            "वितरण के दिन वे गाँव से बाहर होते हैं।",
            "पहचान जाँचने वाली मशीन उन्हें पहचानने में विफल रहती है।"],
   ans=3, pos=3)

# ------------------------------------------------------------------ P03 birdwatchers' lists as science (3)
p = passage("p03",
  "Every winter, thousands of volunteers across India note down the birds they see in an hour and upload their lists to a common database. Individually the lists are untidy: observers differ in skill, favour places that are easy to reach, "
  "and report the exciting species more often than the common ones. Yet when millions of such lists are combined, patterns appear that no scientist could have gathered alone: which species are retreating from their old range, "
  "which are arriving earlier each year, and which have vanished from places where they were once seen. The sheer scale makes up for the noise.",
  "हर सर्दी में भारत भर के हज़ारों स्वयंसेवक एक घंटे में देखे गए पक्षियों को लिख लेते हैं और अपनी सूचियाँ एक साझा डेटाबेस में अपलोड करते हैं। अलग-अलग देखने पर सूचियाँ अव्यवस्थित हैं: प्रेक्षकों का कौशल भिन्न है, "
  "वे आसानी से पहुँचने वाली जगहों को पसंद करते हैं, और रोमांचक प्रजातियों की रिपोर्ट आम प्रजातियों से अधिक बार करते हैं। फिर भी जब ऐसी लाखों सूचियाँ मिलाई जाती हैं, तो ऐसे रुझान उभरते हैं जिन्हें कोई वैज्ञानिक अकेले नहीं जुटा सकता: "
  "कौन-सी प्रजातियाँ अपने पुराने क्षेत्र से पीछे हट रही हैं, कौन हर वर्ष पहले पहुँच रही हैं, और कौन उन जगहों से लुप्त हो गई हैं जहाँ वे कभी दिखती थीं। केवल पैमाना ही शोर की भरपाई कर देता है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The point is that, although each list is untidy, a very large number of them combined shows patterns -- retreats, earlier arrivals, disappearances -- that no scientist could gather alone. "
   "The passage does not rank volunteers above scientists; it gives disappearances as one example of what the lists reveal, not as its main subject; and since the exciting species are already reported too often, it cannot be asking for only the exciting ones.",
   "बात यह है कि हर सूची अव्यवस्थित होने पर भी ऐसी बहुत-सी सूचियाँ मिलकर रुझान दिखाती हैं -- पीछे हटना, जल्दी पहुँचना, लुप्त होना -- जिन्हें कोई वैज्ञानिक अकेले नहीं जुटा सकता। "
   "परिच्छेद स्वयंसेवकों को वैज्ञानिकों से ऊपर नहीं रखता; वह लुप्त होने को सूचियों के उजागर करने वाली बातों के एक उदाहरण के रूप में देता है, मुख्य विषय के रूप में नहीं; और चूँकि रोमांचक प्रजातियों की रिपोर्ट पहले ही बहुत अधिक होती है, वह केवल रोमांचक प्रजातियों को दर्ज करने को नहीं कह रहा।",
   "crux",
   opts=["Volunteers are better than scientists at recording the birds that they see in a single hour of watching.",
         "Together, many imperfect volunteer lists show changes in bird life that no scientist could gather alone.",
         "Many species of birds in India are vanishing from the places where they were once seen in large numbers.",
         "Only the rare and exciting species should be entered in the common database of bird lists kept by volunteers."],
   opts_hi=["स्वयंसेवक एक घंटे की निगरानी में देखे गए पक्षियों को दर्ज करने में वैज्ञानिकों से बेहतर हैं।",
            "स्वयंसेवकों की अनेक अपूर्ण सूचियाँ मिलकर पक्षियों के ऐसे बदलाव दिखाती हैं जो वैज्ञानिक अकेले नहीं जुटा सकते।",
            "भारत में पक्षियों की अनेक प्रजातियाँ उन जगहों से लुप्त हो रही हैं जहाँ वे कभी बड़ी संख्या में दिखती थीं।",
            "स्वयंसेवकों द्वारा रखे गए पक्षी-सूचियों के साझा डेटाबेस में केवल दुर्लभ और रोमांचक प्रजातियाँ दर्ज होनी चाहिए।"],
   ans=1, pos=1)
RQ(p, "Assumption", "hard", "sc", ASSUME, ASSUME_HI,
   "Only 1 is assumed. If every error leaned the same way -- say, all observers overlooked the same species -- scale could not cancel the noise; the passage says that it does, so it takes it that not all the errors lean the same way. "
   "2 contradicts the passage, which relies on such data; 3 is not needed, because the argument concerns what the lists already uploaded show.",
   "केवल 1 पूर्वधारणा है। यदि हर त्रुटि एक ही दिशा में झुकी हो -- मान लीजिए सभी प्रेक्षक एक ही प्रजाति को अनदेखा कर दें -- तो पैमाना शोर को काट नहीं सकता; परिच्छेद कहता है कि वह काटता है, इसलिए वह मानकर चलता है कि त्रुटियाँ सब की सब एक ही दिशा में नहीं झुकी हैं। "
   "2 परिच्छेद का खंडन करता है, जो ऐसे आँकड़ों पर ही निर्भर है; 3 की ज़रूरत नहीं, क्योंकि तर्क इस बारे में है कि पहले से अपलोड की गई सूचियाँ क्या दिखाती हैं।",
   "assumptions",
   st=["Not all the errors in the volunteers' lists lean in the same direction.",
       "Scientists have no use for data collected by people without training.",
       "Volunteers will keep uploading their lists every winter."],
   st_hi=["स्वयंसेवकों की सूचियों की त्रुटियाँ ऐसी नहीं हैं कि सब की सब एक ही दिशा में झुकी हों।",
          "प्रशिक्षण-रहित लोगों द्वारा जुटाए गए आँकड़ों का वैज्ञानिकों के लिए कोई उपयोग नहीं है।",
          "स्वयंसेवक हर सर्दी में अपनी सूचियाँ अपलोड करते रहेंगे।"],
   opts=["1 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"], key=0)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Both are valid. Observers 'report the exciting species more often than the common ones', so an exciting species can appear in the lists more often than its numbers justify (1). "
   "And the combined lists reveal species 'retreating from their old range' although each list is untidy (2).",
   "दोनों वैध हैं। प्रेक्षक 'रोमांचक प्रजातियों की रिपोर्ट आम प्रजातियों से अधिक बार करते हैं', इसलिए रोमांचक प्रजाति सूचियों में अपनी संख्या के अनुपात से अधिक बार आ सकती है (1)। "
   "और मिली हुई सूचियाँ 'अपने पुराने क्षेत्र से पीछे हटती' प्रजातियों को उजागर करती हैं, जबकि हर सूची अव्यवस्थित है (2)।",
   "conclusions",
   st=["A species that excites observers may appear in the lists more often than its numbers justify.",
       "A species' retreat from its old range can be detected even if each volunteer's list is imperfect."],
   st_hi=["जो प्रजाति प्रेक्षकों को रोमांचित करती है वह सूचियों में अपनी संख्या के अनुपात से अधिक बार दिख सकती है।",
          "किसी प्रजाति का अपने पुराने क्षेत्र से पीछे हटना तब भी पकड़ा जा सकता है जब हर स्वयंसेवक की सूची अपूर्ण हो।"],
   key=2)

# ------------------------------------------------------------------ P04 sand taken from riverbeds (2)
p = passage("p04",
  "Sand is the second most used natural resource after water, and the construction boom has made riverbeds its main source. Taking sand from a river is not like quarrying a hill, because the river keeps moving, "
  "and what is removed upstream is felt for kilometres downstream. Beds are lowered, banks collapse, bridges lose their footing, and the groundwater on which wells beside the river depend sinks. "
  "Licences limit how much may be taken, but the limits are often ignored, and the illegal trade is so profitable that those who try to stop it have been attacked. "
  "Substitutes exist, such as crushed rock and recycled demolition waste, but they are little used because river sand is cheaper.",
  "रेत पानी के बाद सबसे अधिक उपयोग किया जाने वाला प्राकृतिक संसाधन है, और निर्माण की तेज़ी ने नदी की तलहटी को उसका मुख्य स्रोत बना दिया है। नदी से रेत निकालना किसी पहाड़ी की खुदाई जैसा नहीं है, क्योंकि नदी चलती रहती है, "
  "और जो ऊपरी धारा में निकाला जाता है उसका असर किलोमीटरों नीचे तक महसूस होता है। तलहटी गहरी हो जाती है, किनारे ढह जाते हैं, पुल अपनी नींव खो देते हैं, और नदी के किनारे के कुएँ जिस भूजल पर निर्भर हैं वह नीचे चला जाता है। "
  "अनुज्ञप्तियाँ निकासी की मात्रा सीमित करती हैं, पर सीमाओं की अक्सर अनदेखी होती है, और अवैध व्यापार इतना लाभदायक है कि उसे रोकने वालों पर हमले हुए हैं। "
  "विकल्प मौजूद हैं, जैसे कुचला हुआ पत्थर और ध्वस्त निर्माण का पुनर्चक्रित मलबा, पर उनका उपयोग कम होता है क्योंकि नदी की रेत सस्ती है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage sets out the damage that sand mining does along the river, far beyond the site, and why it goes on: the limits are ignored, the illegal trade is profitable and the substitutes cost more. "
   "It says that sand is the second most used resource after water, not that it is used up faster, and it does not call for a ban. It says that substitutes exist but are little used because river sand is cheaper, so it does not say that no more sand need be mined. "
   "And it says that those who try to stop the illegal trade have been attacked, not that the officials who issue licences are.",
   "परिच्छेद नदी के साथ-साथ, स्थल से बहुत आगे तक, रेत-खनन से होने वाली हानि बताता है और यह भी कि वह क्यों चलता रहता है: सीमाओं की अनदेखी होती है, अवैध व्यापार लाभदायक है और विकल्प महँगे पड़ते हैं। "
   "वह कहता है कि रेत पानी के बाद दूसरा सबसे अधिक उपयोग होने वाला संसाधन है, यह नहीं कि वह पानी से तेज़ी से ख़त्म हो रही है, और वह प्रतिबंध की माँग नहीं करता। वह कहता है कि विकल्प हैं पर कम उपयोग होते हैं क्योंकि नदी की रेत सस्ती है, इसलिए वह यह नहीं कहता कि और रेत निकालने की ज़रूरत नहीं। "
   "और वह कहता है कि अवैध व्यापार रोकने की कोशिश करने वालों पर हमले हुए हैं, यह नहीं कि अनुज्ञप्ति जारी करने वाले अधिकारियों पर।",
   "crux",
   opts=["Sand is being used up faster than water is, so mining it from rivers ought to be banned at once.",
         "Crushed rock and recycled waste can take the place of river sand, so no more sand needs to be mined from rivers.",
         "Licences for taking sand from rivers have failed because the officials who issue them are attacked.",
         "Mining river sand harms the river far beyond the pit, yet goes on because it is cheap and poorly policed."],
   opts_hi=["रेत पानी से भी तेज़ी से ख़त्म हो रही है, इसलिए नदियों से उसका खनन तुरंत प्रतिबंधित होना चाहिए।",
            "कुचला पत्थर और पुनर्चक्रित मलबा नदी की रेत की जगह ले सकते हैं, इसलिए नदियों से और रेत निकालने की ज़रूरत नहीं।",
            "नदियों से रेत निकालने की अनुज्ञप्तियाँ इसलिए विफल हुई हैं कि उन्हें जारी करने वाले अधिकारियों पर हमले होते हैं।",
            "रेत का खनन नदी को गड्ढे से कहीं आगे तक हानि पहुँचाता है, फिर भी सस्ता और कम निगरानी वाला होने से चलता रहता है।"],
   ans=3, pos=3)
RQ(p, "Specific Detail", "medium", "mcq", NOTCORRECT, NOTCORRECT_HI,
   "The passage says that licences limit how much may be taken but that the limits 'are often ignored', so saying that they are generally respected is the statement that is not correct. "
   "The passage does say that what is removed upstream is felt for kilometres downstream, that banks collapse and bridges lose their footing, and that substitutes are little used because river sand is cheaper.",
   "परिच्छेद कहता है कि अनुज्ञप्तियाँ निकासी की मात्रा सीमित करती हैं पर सीमाओं की 'अक्सर अनदेखी होती है', इसलिए यह कहना कि उनका प्रायः पालन होता है वही कथन है जो सही नहीं है। "
   "परिच्छेद यह अवश्य कहता है कि जो ऊपरी धारा में निकाला जाता है उसका असर किलोमीटरों नीचे तक महसूस होता है, कि किनारे ढह जाते हैं और पुल अपनी नींव खो देते हैं, और कि विकल्प कम उपयोग होते हैं क्योंकि नदी की रेत सस्ती है।",
   "not-correct",
   opts=["Licences limit the quantity of sand that may be taken, and the limits are generally respected.",
         "What is removed from a river upstream is felt for kilometres downstream of the place where it is taken.",
         "Sand taken from the bed of a river can make its banks collapse and its bridges lose their footing.",
         "Substitutes for river sand, such as crushed rock, are little used because river sand is cheaper."],
   opts_hi=["अनुज्ञप्तियाँ निकाली जा सकने वाली रेत की मात्रा सीमित करती हैं, और सीमाओं का प्रायः पालन होता है।",
            "नदी से ऊपरी धारा में जो निकाला जाता है उसका असर निकासी के स्थान से किलोमीटरों नीचे तक महसूस होता है।",
            "नदी की तलहटी से रेत निकालने पर उसके किनारे ढह सकते हैं और उसके पुल अपनी नींव खो सकते हैं।",
            "कुचले पत्थर जैसे नदी की रेत के विकल्प कम उपयोग होते हैं क्योंकि नदी की रेत सस्ती है।"],
   ans=0, pos=0)

# ------------------------------------------------------------------ P05 roads and girls' schooling (3)
p = passage("p05",
  "When a new all-weather road reaches a village, the first change people notice is often not in trade but in the school. Enrolment of girls tends to rise faster than that of boys, because the main reason families keep daughters at home "
  "is not the cost of fees but the fear of the long walk: the dangers of an isolated path, the hours lost, the lack of a bus that a mother would trust. A road that shortens the journey, brings a bus or makes a safe cycle ride possible, "
  "and lets a teacher travel in, removes the reason and not merely the symptom. Where a road is built but nothing runs on it, the effect is small.",
  "जब किसी गाँव में नई, हर मौसम में चलने वाली सड़क पहुँचती है, तो लोगों को पहला बदलाव अक्सर व्यापार में नहीं, विद्यालय में दिखता है। लड़कियों का नामांकन प्रायः लड़कों के नामांकन से तेज़ी से बढ़ता है, क्योंकि परिवार बेटियों को घर पर इसलिए रखते हैं कि "
  "फ़ीस का ख़र्च नहीं, बल्कि लंबे पैदल रास्ते का डर है: सुनसान पगडंडी के ख़तरे, खोए हुए घंटे, ऐसी बस का अभाव जिस पर कोई माँ भरोसा कर सके। जो सड़क यात्रा को छोटा करती है, बस लाती है या साइकिल से सुरक्षित सफ़र संभव बनाती है, "
  "और शिक्षक को आने देती है, वह केवल लक्षण नहीं, कारण को दूर करती है। जहाँ सड़क बन जाती है पर उस पर कुछ चलता नहीं, वहाँ असर छोटा होता है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage says that the main reason families keep daughters at home is the fear of the long walk, and that a road that shortens and secures the journey removes that reason. "
   "It denies that fees are the main reason, says that girls' enrolment tends to rise faster than boys', and says that the effect is small where nothing runs on the road, so a road alone is not enough.",
   "परिच्छेद कहता है कि परिवारों के बेटियों को घर पर रखने का मुख्य कारण लंबे पैदल रास्ते का डर है, और जो सड़क यात्रा को छोटा और सुरक्षित बनाती है वह उस कारण को दूर करती है। "
   "वह फ़ीस को मुख्य कारण मानने का खंडन करता है, कहता है कि लड़कियों का नामांकन प्रायः लड़कों से तेज़ी से बढ़ता है, और कहता है कि जहाँ सड़क पर कुछ चलता नहीं वहाँ असर छोटा होता है, इसलिए अकेली सड़क पर्याप्त नहीं।",
   "crux",
   opts=["Families keep their daughters out of school mainly because of what the fees cost them every year.",
         "When a new road reaches a village, boys gain more than girls in school enrolment in the years after.",
         "A road raises girls' school enrolment mainly by making the journey to school shorter and safer.",
         "Building a road to a village is enough by itself to bring all of its girls to school."],
   opts_hi=["परिवार बेटियों को विद्यालय से मुख्यतः हर साल लगने वाली फ़ीस के ख़र्च के कारण दूर रखते हैं।",
            "किसी गाँव में नई सड़क पहुँचने पर आगे के वर्षों में विद्यालय-नामांकन में लड़कियों से अधिक लाभ लड़कों को होता है।",
            "सड़क लड़कियों का नामांकन मुख्यतः विद्यालय की यात्रा को छोटा और सुरक्षित बनाकर बढ़ाती है।",
            "किसी गाँव तक सड़क बना देना अपने आप में उसकी सभी लड़कियों को विद्यालय लाने के लिए पर्याप्त है।"],
   ans=2, pos=2)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Neither is valid. 1 overstates: the passage says that the effect is small where nothing runs on the road, not that there is none. "
   "2 gives families a motive that the passage does not give; it names the fear of the long walk as the main reason, which is quite compatible with valuing girls' education.",
   "कोई भी वैध नहीं है। 1 बढ़ा-चढ़ाकर कहता है: परिच्छेद कहता है कि जहाँ सड़क पर कुछ नहीं चलता वहाँ असर छोटा होता है, यह नहीं कि बिल्कुल नहीं होता। "
   "2 परिवारों को ऐसा उद्देश्य देता है जो परिच्छेद नहीं देता; वह लंबे पैदल रास्ते के डर को मुख्य कारण बताता है, जो लड़कियों की शिक्षा को महत्त्व देने से पूरी तरह मेल खाता है।",
   "conclusions",
   st=["A road on which no transport runs has no effect at all on school enrolment.",
       "Families that keep daughters at home do so because they do not value girls' education."],
   st_hi=["जिस सड़क पर कोई परिवहन नहीं चलता उसका विद्यालय-नामांकन पर बिल्कुल कोई प्रभाव नहीं पड़ता।",
          "जो परिवार बेटियों को घर पर रखते हैं वे ऐसा इसलिए करते हैं कि वे लड़कियों की शिक्षा को महत्त्व नहीं देते।"],
   key=3)
RQ(p, "Assumption", "hard", "s2", ASSUME, ASSUME_HI,
   "Only 2 is assumed. The passage explains why girls' enrolment rises faster than boys' by the fear of the long walk, which works only if families fear the journey more for a daughter than for a son. "
   "1 is not assumed: the passage speaks only of the journey to a school -- shorter, safer, with a bus or a teacher able to travel in -- and its argument nowhere needs a new school to be built.",
   "केवल 2 पूर्वधारणा है। परिच्छेद लड़कियों का नामांकन लड़कों से तेज़ी से बढ़ने को लंबे पैदल रास्ते के डर से समझाता है, जो तभी चलता है जब परिवार बेटे की तुलना में बेटी के लिए यात्रा से अधिक डरते हों। "
   "1 पूर्वधारणा नहीं है: परिच्छेद केवल विद्यालय तक की यात्रा की बात करता है -- छोटी, सुरक्षित, बस या शिक्षक के आ सकने वाली -- और उसके तर्क को कहीं भी किसी नए विद्यालय के बनने की आवश्यकता नहीं है।",
   "assumptions",
   st=["A village that receives a road also receives a new school.",
       "Families worry more about a daughter's journey to school than about a son's."],
   st_hi=["जिस गाँव को सड़क मिलती है उसे नया विद्यालय भी मिलता है।",
          "परिवार बेटे की तुलना में बेटी की विद्यालय-यात्रा को लेकर अधिक चिंतित रहते हैं।"],
   key=1)

# ------------------------------------------------------------------ P06 cheap fertiliser and tired soil (3)
p = passage("p06",
  "Fertiliser prices in India are held low by a subsidy, and urea, the nitrogen fertiliser, is the cheapest of all. Farmers respond as anyone would: they apply more of what is cheap, often far more than the crop can use, "
  "and too little of the phosphorus and potash that the soil also needs. The result is soil that is out of balance, crop yields that rise less with each extra bag, and rivers and wells that carry the surplus nitrogen away. "
  "The subsidy was meant to feed the country, and for years it did. It is harder now to say that it feeds the soil. Nobody argues for taking it away overnight; the argument is only that it is time to ask what it is buying.",
  "भारत में उर्वरकों की क़ीमतें अनुदान से नीची रखी जाती हैं, और नाइट्रोजन उर्वरक यूरिया सबसे सस्ता है। किसान वैसा ही करते हैं जैसा कोई भी करता: वे जो सस्ता है उसे अधिक डालते हैं, अक्सर फ़सल की ज़रूरत से कहीं अधिक, "
  "और फ़ॉस्फ़ोरस तथा पोटाश, जिनकी मिट्टी को भी ज़रूरत है, बहुत कम। नतीजा है असंतुलित मिट्टी, ऐसी पैदावार जो हर अतिरिक्त बोरी के साथ कम बढ़ती है, और ऐसी नदियाँ व कुएँ जो अतिरिक्त नाइट्रोजन को बहा ले जाते हैं। "
  "अनुदान का उद्देश्य देश का पेट भरना था, और वर्षों तक उसने यही किया। अब यह कहना कठिन है कि वह मिट्टी का पेट भरता है। कोई उसे रातोंरात हटाने की वकालत नहीं करता; तर्क केवल इतना है कि अब पूछने का समय है कि वह क्या ख़रीद रहा है।")
RQ(p, "Best Summary", "medium", "mcq", MSG, MSG_HI,
   "The passage says that the subsidy once fed the country, that its low price now leads farmers to overuse urea, to the harm of the soil and the water, and that nobody argues for removing it overnight, only for asking what it is buying. "
   "So the message is a fresh look, not withdrawal at once. It gives the low price, not ignorance, as the reason for overuse, and it does not say that yields will fall or that phosphorus and potash should be subsidised more.",
   "परिच्छेद कहता है कि अनुदान ने कभी देश का पेट भरा, कि उसकी नीची क़ीमत अब किसानों को यूरिया के अधिक उपयोग की ओर ले जाती है, जिससे मिट्टी और पानी को हानि होती है, और कि कोई उसे रातोंरात हटाने की वकालत नहीं करता, केवल यह पूछने की कि वह क्या ख़रीद रहा है। "
   "इसलिए संदेश नए सिरे से विचार का है, तुरंत वापसी का नहीं। वह अधिक उपयोग का कारण अज्ञान नहीं, नीची क़ीमत बताता है, और वह यह नहीं कहता कि पैदावार गिरेगी या कि फ़ॉस्फ़ोरस और पोटाश पर अधिक अनुदान दिया जाए।",
   "message",
   opts=["The subsidy on fertilisers should be withdrawn at once, as it has damaged the soil and the rivers.",
         "A subsidy that once helped feed the country now distorts fertiliser use, so its effects need a fresh look.",
         "Farmers use too much urea because they do not know what their soil needs or how much the crop can use.",
         "Crop yields in India will fall in the coming years unless phosphorus and potash are subsidised more than urea."],
   opts_hi=["उर्वरकों पर अनुदान तुरंत वापस ले लेना चाहिए, क्योंकि उसने मिट्टी और नदियों को हानि पहुँचाई है।",
            "जिस अनुदान ने कभी देश का पेट भरा वह अब उर्वरक के उपयोग को बिगाड़ रहा है; उसके प्रभावों पर नए सिरे से विचार हो।",
            "किसान यूरिया अधिक इसलिए डालते हैं कि उन्हें पता नहीं कि उनकी मिट्टी को क्या चाहिए और फ़सल कितना सोख सकती है।",
            "भारत में आने वाले वर्षों में पैदावार तब तक गिरेगी जब तक फ़ॉस्फ़ोरस और पोटाश पर यूरिया से अधिक अनुदान न दिया जाए।"],
   ans=1, pos=1)
RQ(p, "Inference", "medium", "sc", INFER, INFER_HI,
   "1 and 2 follow: farmers 'apply more of what is cheap', and yields 'rise less with each extra bag'. 3 does not follow: the surplus nitrogen is carried away by rivers and wells, so not all of it is taken up by the crop.",
   "1 और 2 निकलते हैं: किसान 'जो सस्ता है उसे अधिक डालते हैं', और पैदावार 'हर अतिरिक्त बोरी के साथ कम बढ़ती है'। 3 नहीं निकलता: अतिरिक्त नाइट्रोजन नदियों और कुओं में बह जाती है, इसलिए वह सब फ़सल नहीं सोखती।",
   "conclusions",
   st=["A farmer who pays less for urea has a reason to use more of it.",
       "The extra yield from each additional bag of fertiliser tends to be smaller.",
       "All the nitrogen that farmers apply is taken up by the crop."],
   st_hi=["जो किसान यूरिया के लिए कम देता है उसके पास उसे अधिक डालने का कारण है।",
          "उर्वरक की हर अतिरिक्त बोरी से मिलने वाली अतिरिक्त पैदावार प्रायः कम होती जाती है।",
          "किसान जो नाइट्रोजन डालते हैं वह सब फ़सल सोख लेती है।"],
   opts=["1 only", "2 and 3 only", "1 and 2 only", "1, 2 and 3"], key=2)
RQ(p, "Author's Tone", "medium", "mcq",
   "The author's attitude towards the fertiliser subsidy is best described as:",
   "उर्वरक अनुदान के प्रति लेखक का दृष्टिकोण सबसे अच्छी तरह कैसा बताया जा सकता है?",
   "The author says that the subsidy 'was meant to feed the country, and for years it did' -- appreciation of its past -- but that it is harder now to say that it feeds the soil, and asks what it is buying -- doubt about its present. "
   "The author is neither enthusiastic nor scornful, and the plea to ask what the subsidy buys shows that the author is not indifferent to whether it is kept.",
   "लेखक कहता है कि अनुदान 'का उद्देश्य देश का पेट भरना था, और वर्षों तक उसने यही किया' -- उसके अतीत की सराहना -- पर अब यह कहना कठिन है कि वह मिट्टी का पेट भरता है, और पूछता है कि वह क्या ख़रीद रहा है -- उसके वर्तमान पर संशय। "
   "लेखक न उत्साहित है, न तिरस्कारपूर्ण, और यह पूछने का आग्रह कि अनुदान क्या ख़रीदता है, दिखाता है कि लेखक इस बात के प्रति उदासीन नहीं कि वह रखा जाए या नहीं।",
   "tone",
   opts=["enthusiastic about the benefits that it continues to bring to farmers and to the country",
         "scornful of it as a policy that has always failed the farmers and the soil alike",
         "indifferent to whether it is kept in place or removed from the budget",
         "appreciative of what it did, but doubtful of what it now achieves"],
   opts_hi=["किसानों और देश को इसके निरंतर मिलते रहने वाले लाभों को लेकर उत्साहित",
            "इसे एक ऐसी नीति मानकर तिरस्कारपूर्ण जो किसानों और मिट्टी, दोनों के लिए सदा विफल रही",
            "इसके बजट में बने रहने या हटाए जाने के प्रति उदासीन",
            "इसने जो किया उसकी सराहना करने वाला, पर अब यह जो हासिल करता है उस पर संशयी"],
   ans=3, pos=3)

# ------------------------------------------------------------------ P07 the costs of hosting mega-events (3)
p = passage("p07",
  "Cities bid to host the Olympic Games or a football World Cup in the belief that the event will pay for itself in tourists, jobs and global attention. Looking back over many such events, economists find that the promised gains "
  "are usually smaller than the costs, which run over budget with remarkable regularity. Stadiums built for a fortnight sit half-empty for decades. The cities that gain most are those that use the event to build what they would have needed anyway, "
  "such as transport and housing, and that plan from the start for what the new buildings will be used for afterwards. For the rest, the Games leave behind a bill.",
  "शहर ओलंपिक खेलों या फ़ुटबॉल विश्व कप की मेज़बानी के लिए इस विश्वास से बोली लगाते हैं कि आयोजन पर्यटकों, रोज़गार और वैश्विक ध्यान से अपना ख़र्च ख़ुद निकाल लेगा। ऐसे अनेक आयोजनों को पीछे मुड़कर देखने पर अर्थशास्त्री पाते हैं कि वादा किए गए लाभ "
  "प्रायः लागत से कम होते हैं, और लागत उल्लेखनीय नियमितता से बजट से बढ़ जाती है। जो स्टेडियम पखवाड़े भर के लिए बने, वे दशकों तक आधे ख़ाली पड़े रहते हैं। सबसे अधिक लाभ उन शहरों को होता है जो आयोजन का उपयोग वह बनाने में करते हैं जिसकी उन्हें वैसे भी ज़रूरत होती, "
  "जैसे परिवहन और आवास, और जो शुरू से ही योजना बनाते हैं कि नई इमारतें बाद में किस काम आएँगी। बाक़ी के लिए, खेल अपने पीछे एक बिल छोड़ जाते हैं।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage says that the gains are usually smaller than the costs, but that the cities that gain most are those that use the event to build what they would have needed anyway and plan for the later use of the buildings. "
   "So lasting gain depends on these two conditions. It does not say that no event ever brings a gain, that tourists repay the costs (it says that the gains are smaller than the costs), or that stadiums should never be built.",
   "परिच्छेद कहता है कि लाभ प्रायः लागत से कम होते हैं, पर सबसे अधिक लाभ उन शहरों को होता है जो आयोजन का उपयोग वह बनाने में करते हैं जिसकी उन्हें वैसे भी ज़रूरत होती और इमारतों के बाद के उपयोग की योजना बनाते हैं। "
   "इसलिए स्थायी लाभ इन दो शर्तों पर निर्भर है। वह यह नहीं कहता कि कोई आयोजन कभी लाभ नहीं देता, कि पर्यटक लागत चुका देते हैं (वह कहता है कि लाभ लागत से कम होते हैं), या कि स्टेडियम कभी नहीं बनने चाहिए।",
   "crux",
   opts=["Cities should stop bidding for sporting events, since such events never bring a city any gain at all.",
         "The costs of hosting a mega-event are repaid by the tourists whom the event attracts to the city and its shops.",
         "A mega-event brings lasting gain only if it builds what the city needs anyway and plans for later use.",
         "Stadiums built for a sporting event are rarely used again, so no city should ever build them."],
   opts_hi=["शहरों को खेल आयोजनों की बोली लगाना बंद कर देना चाहिए, क्योंकि ऐसे आयोजन किसी शहर को कभी कोई भी लाभ नहीं देते।",
            "किसी विशाल आयोजन की मेज़बानी की लागत उन पर्यटकों से चुक जाती है जिन्हें आयोजन शहर और उसकी दुकानों में खींचता है।",
            "विशाल आयोजन से शहर को स्थायी लाभ तभी मिलता है जब वह वही बनाए जो उसे वैसे भी चाहिए और बाद के उपयोग की योजना रखे।",
            "खेल आयोजन के लिए बने स्टेडियम शायद ही दोबारा उपयोग होते हैं, इसलिए किसी शहर को उन्हें कभी नहीं बनाना चाहिए।"],
   ans=2, pos=2)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Only 1 is valid: stadiums built for a fortnight sit half-empty for decades, while the cities that gain are those that build what they would have needed anyway. "
   "2 is not valid: the passage ties the gain to what is built and planned for later use, not to how little is spent.",
   "केवल 1 वैध है: पखवाड़े भर के लिए बने स्टेडियम दशकों तक आधे ख़ाली पड़े रहते हैं, जबकि लाभ उन शहरों को होता है जो वह बनाते हैं जिसकी उन्हें वैसे भी ज़रूरत होती। "
   "2 वैध नहीं है: परिच्छेद लाभ को इससे जोड़ता है कि क्या बना और बाद के उपयोग की क्या योजना थी, इससे नहीं कि कितना कम ख़र्च हुआ।",
   "conclusions",
   st=["A city that builds only what the event itself requires is likely to be left with buildings that stand idle.",
       "A city that spends less on an event is sure to gain more from it."],
   st_hi=["जो शहर केवल वही बनाता है जो आयोजन को स्वयं चाहिए, उसके पास ऐसी इमारतें रह जाने की संभावना है जो ख़ाली पड़ी रहें।",
          "जो शहर आयोजन पर कम ख़र्च करता है उसे उससे अधिक लाभ होना निश्चित है।"],
   key=0)
RQ(p, "Assumption", "hard", "sc", ASSUME, ASSUME_HI,
   "1 and 3 are assumed. The passage turns a record of past events into a warning for a city that is now thinking of bidding, which takes it that the record is a fair guide (1); "
   "and it asks cities to plan from the start for the later use of new buildings, which takes it that a city can foresee that use (3). "
   "2 is not assumed: costs run over budget 'with remarkable regularity', which is not the same as always, and nothing in the argument needs every host city to overspend.",
   "1 और 3 पूर्वधारणाएँ हैं। परिच्छेद पिछले आयोजनों के रिकॉर्ड को अब बोली पर विचार करने वाले शहर के लिए चेतावनी बना देता है, जो मानकर चलता है कि वह रिकॉर्ड उचित मार्गदर्शक है (1); "
   "और वह शहरों से शुरू से ही नई इमारतों के बाद के उपयोग की योजना बनाने को कहता है, जो मानकर चलता है कि शहर उस उपयोग का पूर्वानुमान लगा सकता है (3)। "
   "2 पूर्वधारणा नहीं है: लागत 'उल्लेखनीय नियमितता से' बजट से आगे निकलती है, जिसका अर्थ 'हमेशा' नहीं है, और तर्क को यह आवश्यकता नहीं कि हर मेज़बान शहर अधिक ख़र्च करे।",
   "assumptions",
   st=["The findings of economists about past events are a fair guide to what a city now thinking of bidding can expect.",
       "No city can host a mega-event without running over budget.",
       "A city can foresee, before the event, what its new buildings will be used for afterwards."],
   st_hi=["पिछले आयोजनों के बारे में अर्थशास्त्रियों के निष्कर्ष इसका उचित मार्गदर्शन करते हैं कि अब बोली पर विचार करने वाला शहर क्या अपेक्षा कर सकता है।",
          "कोई शहर बजट से आगे गए बिना किसी विशाल आयोजन की मेज़बानी नहीं कर सकता।",
          "शहर आयोजन से पहले अनुमान लगा सकता है कि उसकी नई इमारतें बाद में किस काम आएँगी।"],
   opts=["1 only", "1 and 3 only", "2 and 3 only", "1, 2 and 3"], key=1)

# ------------------------------------------------------------------ P08 village health workers and newborns (2)
p = passage("p08",
  "A woman who lives in the village, has been trained for a few weeks and visits each new mother in the first days after the birth can do something that a doctor in a distant hospital cannot: she can notice early what is going wrong. "
  "She weighs the baby, checks that it is feeding, and sends a mother with a fever to the health centre before the fever becomes dangerous. Such community health workers are paid little and asked to do a great deal, "
  "and they are often the only link between a household and the health system. Where they are trusted and backed with supplies and supervision, newborn deaths fall; where they are left to manage alone, the effect fades.",
  "गाँव में रहने वाली, कुछ सप्ताह प्रशिक्षित और प्रसव के बाद के पहले दिनों में हर नई माँ से मिलने वाली एक महिला वह कर सकती है जो दूर के अस्पताल का डॉक्टर नहीं कर सकता: वह जल्दी भाँप सकती है कि क्या गड़बड़ हो रहा है। "
  "वह शिशु का वज़न लेती है, देखती है कि वह दूध पी रहा है या नहीं, और बुख़ार वाली माँ को बुख़ार ख़तरनाक होने से पहले स्वास्थ्य केंद्र भेज देती है। ऐसे सामुदायिक स्वास्थ्य कार्यकर्ताओं को कम मानदेय मिलता है और उनसे बहुत कुछ करने को कहा जाता है, "
  "और वे अक्सर परिवार और स्वास्थ्य व्यवस्था के बीच की एकमात्र कड़ी होती हैं। जहाँ उन पर भरोसा किया जाता है और आपूर्ति तथा पर्यवेक्षण का सहारा दिया जाता है, वहाँ नवजात मृत्यु घटती है; जहाँ उन्हें अकेले निपटने को छोड़ दिया जाता है, वहाँ असर मद्धम पड़ जाता है।")
RQ(p, "Main Idea", "easy", "mcq", CRUX, CRUX_HI,
   "The passage says that a trained village woman can notice early what is going wrong, that newborn deaths fall where such workers are trusted and backed with supplies and supervision, and that the effect fades where they are left alone. "
   "The main idea is that lives are saved on condition that the system supports them. The passage notes the low pay but does not ask for more; it says what a village woman can do that a distant doctor cannot, not that the doctor can do less; and it does not say that a few weeks of training suit anyone.",
   "परिच्छेद कहता है कि प्रशिक्षित ग्रामीण महिला जल्दी भाँप सकती है कि क्या गड़बड़ हो रहा है, कि जहाँ ऐसे कार्यकर्ताओं पर भरोसा किया जाता है और आपूर्ति व पर्यवेक्षण का सहारा दिया जाता है वहाँ नवजात मृत्यु घटती है, और कि जहाँ उन्हें अकेला छोड़ा जाता है वहाँ असर मद्धम पड़ जाता है। "
   "मुख्य विचार यह है कि जान तभी बचती है जब व्यवस्था उनका साथ दे। परिच्छेद कम मानदेय का उल्लेख करता है पर अधिक की माँग नहीं करता; वह बताता है कि गाँव की महिला वह कर सकती है जो दूर का डॉक्टर नहीं कर सकता, यह नहीं कि डॉक्टर कम कर सकता है; और वह यह नहीं कहता कि कुछ सप्ताह का प्रशिक्षण किसी के भी लिए पर्याप्त है।",
   "crux",
   opts=["Trained village health workers can save newborn lives, but only where the health system backs them.",
         "Doctors in distant hospitals can do less for newborn babies than village women can do for them.",
         "Community health workers are paid too little for what they are asked to do and should be given higher wages.",
         "A few weeks of training are enough to enable anyone to treat a sick newborn baby."],
   opts_hi=["प्रशिक्षित ग्रामीण स्वास्थ्य कार्यकर्ता नवजात शिशुओं की जान बचा सकती हैं, पर केवल वहाँ जहाँ स्वास्थ्य व्यवस्था उनका साथ दे।",
            "दूर के अस्पतालों के डॉक्टर नवजात शिशुओं के लिए उससे कम कर सकते हैं जितना गाँव की महिलाएँ उनके लिए कर सकती हैं।",
            "सामुदायिक स्वास्थ्य कार्यकर्ताओं को जो कुछ करने को कहा जाता है उसके लिए बहुत कम मानदेय मिलता है और उन्हें अधिक वेतन दिया जाना चाहिए।",
            "कुछ सप्ताह का प्रशिक्षण किसी को भी बीमार नवजात शिशु का इलाज करने में सक्षम बनाने के लिए पर्याप्त है।"],
   ans=0, pos=0)
RQ(p, "Assumption", "hard", "s2", ASSUME, ASSUME_HI,
   "Both are assumed. The worker's value lies in noticing early what is going wrong, which matters only if what is noticed early can be dealt with (1); and her sending a mother with a fever to the health centre helps only if the mother can be treated there (2).",
   "दोनों पूर्वधारणाएँ हैं। कार्यकर्ता का महत्त्व इसमें है कि वह जल्दी भाँप लेती है कि क्या गड़बड़ हो रहा है, जो तभी मायने रखता है जब जो जल्दी भाँपा जाए उससे निपटा जा सके (1); और बुख़ार वाली माँ को स्वास्थ्य केंद्र भेजना तभी काम आता है जब वहाँ माँ का इलाज हो सके (2)।",
   "assumptions",
   st=["Illnesses in newborn babies can often be dealt with if they are noticed early.",
       "A mother sent to the health centre with a fever can be treated there."],
   st_hi=["नवजात शिशुओं की बीमारियों से अक्सर निपटा जा सकता है यदि उन्हें जल्दी भाँप लिया जाए।",
          "बुख़ार के साथ स्वास्थ्य केंद्र भेजी गई माँ का वहाँ इलाज हो सकता है।"],
   key=2)

# ------------------------------------------------------------------ P09 rooftop solar and the grid (3)
p = passage("p09",
  "A household that puts solar panels on its roof and sells its surplus electricity back to the grid pays less for power and cuts the demand for coal. When a few houses do so, the grid barely notices. "
  "When thousands do, in the same afternoon, the grid must cope with a flood of power at midday and a sudden shortfall when the sun sets and everyone switches on lights and fans at once. "
  "Managing that swing needs batteries, flexible power stations and meters that can tell the grid what is happening. Some utilities respond by discouraging rooftop solar, because households that generate their own power pay less towards "
  "the fixed cost of the wires; the households reply that the wires would be needed in any case. The disagreement is as much about who pays as about technology.",
  "जो परिवार अपनी छत पर सौर पैनल लगाता है और अपनी अतिरिक्त बिजली ग्रिड को वापस बेचता है, वह बिजली के लिए कम चुकाता है और कोयले की माँग घटाता है। जब कुछ ही घर ऐसा करते हैं, तो ग्रिड को शायद ही पता चलता है। "
  "जब हज़ारों एक ही दोपहर में ऐसा करते हैं, तो ग्रिड को दोपहर में बिजली की बाढ़ और सूरज ढलने पर अचानक कमी से निपटना पड़ता है, जब सब एक साथ बत्तियाँ और पंखे चला देते हैं। "
  "उस उतार-चढ़ाव को सँभालने के लिए बैटरियाँ, लचीले बिजलीघर और ऐसे मीटर चाहिए जो ग्रिड को बता सकें कि क्या हो रहा है। कुछ बिजली कंपनियाँ छत के सौर को हतोत्साहित करके जवाब देती हैं, क्योंकि अपनी बिजली बनाने वाले परिवार "
  "तारों की स्थायी लागत में कम योगदान देते हैं; परिवार जवाब देते हैं कि तारों की ज़रूरत तो वैसे भी रहेगी। असहमति जितनी तकनीक के बारे में है उतनी ही इस बारे में भी कि भुगतान कौन करे।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage shows that rooftop solar helps a household and cuts the demand for coal, that it strains the grid once it spreads, and that utilities and households disagree about who should pay for the wires; the last sentence says that the dispute is as much about who pays as about technology. "
   "It does not say that the grid loses more than it saves, that batteries and flexible stations will solve the problems for good, or that the households pay nothing: they pay less towards the fixed cost.",
   "परिच्छेद दिखाता है कि छत का सौर परिवार की मदद करता है और कोयले की माँग घटाता है, कि फैलने पर वह ग्रिड पर दबाव डालता है, और कि बिजली कंपनियाँ और परिवार इस पर असहमत हैं कि तारों का भुगतान कौन करे; अंतिम वाक्य कहता है कि विवाद जितना तकनीक का है उतना ही इसका कि भुगतान कौन करे। "
   "वह यह नहीं कहता कि ग्रिड को बचत से अधिक हानि होती है, कि बैटरियाँ और लचीले बिजलीघर समस्याओं को हमेशा के लिए सुलझा देंगे, या कि परिवार कुछ नहीं चुकाते: वे स्थायी लागत में कम चुकाते हैं।",
   "crux",
   opts=["Rooftop solar should be discouraged, because it costs the grid more than it saves in coal.",
         "The spread of rooftop solar strains the grid and raises the question of who should bear the cost.",
         "Batteries and flexible power stations will solve the problems that rooftop solar causes for the grid for good.",
         "Households with rooftop panels pay nothing towards the grid although they depend on it."],
   opts_hi=["छत के सौर को हतोत्साहित करना चाहिए, क्योंकि वह ग्रिड को कोयले की बचत से अधिक महँगा पड़ता है।",
            "छत के सौर का प्रसार ग्रिड पर दबाव डालता है और यह प्रश्न उठाता है कि लागत कौन उठाए।",
            "बैटरियाँ और लचीले बिजलीघर छत के सौर से ग्रिड को होने वाली समस्याओं को हमेशा के लिए सुलझा देंगे।",
            "छत पर पैनल वाले परिवार ग्रिड पर निर्भर होने के बावजूद उसके लिए कुछ नहीं चुकाते।"],
   ans=1, pos=1)
RQ(p, "Specific Detail", "medium", "mcq",
   "According to the passage, why do some utilities discourage rooftop solar?",
   "परिच्छेद के अनुसार कुछ बिजली कंपनियाँ छत के सौर को हतोत्साहित क्यों करती हैं?",
   "The passage says that some utilities discourage rooftop solar 'because households that generate their own power pay less towards the fixed cost of the wires'. The other options are not given as reasons: "
   "at midday there is a flood of power, not a shortage; households sell their surplus back to the grid; and the passage says that rooftop solar cuts the demand for coal, not that it raises it.",
   "परिच्छेद कहता है कि कुछ बिजली कंपनियाँ छत के सौर को हतोत्साहित करती हैं 'क्योंकि अपनी बिजली बनाने वाले परिवार तारों की स्थायी लागत में कम योगदान देते हैं'। बाक़ी विकल्प कारण के रूप में नहीं दिए गए हैं: "
   "दोपहर में बिजली की बाढ़ होती है, कमी नहीं; परिवार अपनी अतिरिक्त बिजली ग्रिड को वापस बेचते हैं; और परिच्छेद कहता है कि छत का सौर कोयले की माँग घटाता है, यह नहीं कि बढ़ाता है।",
   "detail",
   opts=["Households that generate their own power pay less towards the fixed cost of the wires.",
         "Rooftop panels cannot produce enough power to meet the demand that the grid has at midday.",
         "The utilities are unable to buy back the surplus power that the households produce.",
         "Solar panels on roofs raise the demand for coal in the evening, when the sun has set."],
   opts_hi=["अपनी बिजली बनाने वाले परिवार तारों की स्थायी लागत में कम योगदान देते हैं।",
            "छत के पैनल उतनी बिजली नहीं बना सकते जितनी ग्रिड की दोपहर में माँग होती है।",
            "बिजली कंपनियाँ परिवारों की बनाई अतिरिक्त बिजली को वापस ख़रीदने में असमर्थ हैं।",
            "छत पर लगे सौर पैनल शाम को, जब सूरज ढल चुका होता है, कोयले की माँग बढ़ा देते हैं।"],
   ans=0, pos=0)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Only 2 is valid: the passage says that the swing between a flood of power at midday and a shortfall at sunset needs batteries, flexible power stations and meters. "
   "1 is contradicted: when a few houses use rooftop solar, the grid 'barely notices'.",
   "केवल 2 वैध है: परिच्छेद कहता है कि दोपहर की बिजली की बाढ़ और सूर्यास्त पर कमी के बीच के उतार-चढ़ाव को सँभालने के लिए बैटरियाँ, लचीले बिजलीघर और मीटर चाहिए। "
   "1 का खंडन होता है: जब कुछ ही घर छत का सौर उपयोग करते हैं, तो ग्रिड को 'शायद ही पता चलता है'।",
   "conclusions",
   st=["Rooftop solar causes difficulty for the grid even when only a few houses use it.",
       "A grid with many rooftop panels needs ways of balancing the supply between midday and the evening."],
   st_hi=["छत का सौर तब भी ग्रिड के लिए कठिनाई पैदा करता है जब केवल कुछ घर उसका उपयोग करते हैं।",
          "जिस ग्रिड में बहुत-से छत-पैनल हैं उसे दोपहर और शाम के बीच आपूर्ति को संतुलित करने के उपाय चाहिए।"],
   key=1)

# ------------------------------------------------------------------ P10 the overruns of large public projects (3)
p = passage("p10",
  "Large public projects, whether a metro line, a dam or a bridge, rarely finish on the budget or the date first announced. The usual explanations are bad luck and bad management, but studies of hundreds of projects point to something else: "
  "the people who plan them tend to imagine the project going as planned, and forget the delays that most such projects have met. Estimates are also shaped by the need to win approval, since a project that looks cheap is more likely to be sanctioned. "
  "A remedy that has worked in some countries is to ask how long and how much similar projects have actually taken and cost, and to start from that record rather than from the new project's own plan. "
  "It is a humbling method, because it treats the project as one of a kind of which the world has already seen many.",
  "बड़ी सार्वजनिक परियोजनाएँ, चाहे मेट्रो लाइन हो, बाँध हो या पुल, पहले घोषित बजट या तारीख़ पर शायद ही पूरी होती हैं। सामान्य व्याख्याएँ बुरी क़िस्मत और बुरा प्रबंधन हैं, पर सैकड़ों परियोजनाओं के अध्ययन कुछ और इशारा करते हैं: "
  "उन्हें बनाने वाले लोग परियोजना को योजना के अनुसार चलता हुआ कल्पित करते हैं, और उन देरियों को भूल जाते हैं जिनका सामना अधिकांश ऐसी परियोजनाओं ने किया है। अनुमान मंज़ूरी पाने की आवश्यकता से भी प्रभावित होते हैं, क्योंकि जो परियोजना सस्ती दिखती है उसके स्वीकृत होने की संभावना अधिक होती है। "
  "कुछ देशों में काम करने वाला एक उपाय यह पूछना है कि वैसी ही परियोजनाओं में वास्तव में कितना समय और कितना धन लगा, और नई परियोजना की अपनी योजना के बजाय उस रिकॉर्ड से शुरुआत करना। "
  "यह विनम्र बनाने वाली पद्धति है, क्योंकि वह परियोजना को ऐसी श्रेणी की एक इकाई मानती है जिसकी दुनिया पहले ही अनेक देख चुकी है।")
RQ(p, "Best Summary", "medium", "mcq", MSG, MSG_HI,
   "The passage sets aside bad luck and bad management as the usual explanation, says that planners imagine things going to plan and that the need for approval keeps estimates low, and recommends starting from the record of similar projects. "
   "So the message is to base estimates on what such projects have actually cost. It does not blame carelessness, it does not ask that the lowest estimate be sanctioned (low estimates are part of the problem), and it does not ask that projects wait for the world to see more of them.",
   "परिच्छेद सामान्य व्याख्या के रूप में बुरी क़िस्मत और बुरे प्रबंधन को किनारे रखता है, कहता है कि योजनाकार सब कुछ योजना के अनुसार चलता कल्पित करते हैं और मंज़ूरी की आवश्यकता अनुमानों को नीचा रखती है, और वैसी परियोजनाओं के रिकॉर्ड से शुरू करने की सिफ़ारिश करता है। "
   "इसलिए संदेश यह है कि अनुमान इस पर आधारित हों कि ऐसी परियोजनाओं में वास्तव में कितना लगा। वह लापरवाही को दोष नहीं देता, यह नहीं कहता कि सबसे कम अनुमान को मंज़ूरी दी जाए (कम अनुमान समस्या का हिस्सा हैं), और यह नहीं कहता कि परियोजनाएँ तब तक रुकी रहें जब तक दुनिया उनमें से और न देख ले।",
   "message",
   opts=["Public projects overrun their budgets because the people who plan and manage them are careless and unlucky.",
         "Projects should be sanctioned only when their estimated cost is the lowest of all those that are proposed.",
         "New projects should not be started until the world has seen enough projects of the same kind as theirs.",
         "Planners should base estimates on what similar projects actually cost, as their own plans are over-hopeful."],
   opts_hi=["सार्वजनिक परियोजनाएँ बजट से इसलिए अक्सर आगे निकलती हैं कि उन्हें बनाने और चलाने वाले लोग लापरवाह और बदक़िस्मत होते हैं।",
            "परियोजनाओं को तभी मंज़ूरी दी जानी चाहिए जब उनकी अनुमानित लागत प्रस्तावित की गई सभी परियोजनाओं में सबसे कम हो।",
            "नई परियोजनाएँ तब तक शुरू नहीं होनी चाहिए जब तक दुनिया उसी तरह की पर्याप्त परियोजनाएँ पहले न देख ले।",
            "योजनाकारों को अनुमान वैसी परियोजनाओं की वास्तविक लागत पर टिकाना चाहिए, क्योंकि उनकी अपनी योजनाएँ अति-आशावादी होती हैं।"],
   ans=3, pos=3)
RQ(p, "Specific Detail", "easy", "mcq",
   "According to the passage, what pressure tends to keep the estimates of a project's cost low?",
   "परिच्छेद के अनुसार कौन-सा दबाव किसी परियोजना की लागत के अनुमानों को नीचे रखता है?",
   "The passage says that estimates are shaped by the need to win approval, 'since a project that looks cheap is more likely to be sanctioned'. Forgetting the delays of earlier projects is a habit of mind that the passage gives separately, not a pressure, "
   "and it says that planners forget such delays, not that they are unable to count them. The cost of materials and attention to dates are not mentioned.",
   "परिच्छेद कहता है कि अनुमान मंज़ूरी पाने की आवश्यकता से प्रभावित होते हैं, 'क्योंकि जो परियोजना सस्ती दिखती है उसके स्वीकृत होने की संभावना अधिक होती है'। पहले की परियोजनाओं की देरियों को भूल जाना सोच की एक आदत है जिसे परिच्छेद अलग से बताता है, कोई दबाव नहीं, "
   "और वह कहता है कि योजनाकार ऐसी देरियों को भूल जाते हैं, यह नहीं कि वे उन्हें गिन नहीं पाते। सामग्री की लागत और तारीख़ों पर ध्यान का उल्लेख नहीं है।",
   "detail",
   opts=["Planners are unable to count the delays that earlier projects have met.",
         "The cost of materials falls as soon as a project has been announced.",
         "A project that looks cheap is more likely to be sanctioned.",
         "Governments pay more attention to the date of a project than to its cost."],
   opts_hi=["योजनाकार पहले की परियोजनाओं को मिली देरियों को गिन नहीं पाते।",
            "परियोजना की घोषणा होते ही सामग्री की लागत घट जाती है।",
            "जो परियोजना सस्ती दिखती है उसके स्वीकृत होने की संभावना अधिक होती है।",
            "सरकारें परियोजना की लागत की तुलना में उसकी तारीख़ पर अधिक ध्यान देती हैं।"],
   ans=2, pos=2)
RQ(p, "Inference", "hard", "sc", INFER, INFER_HI,
   "1 and 2 follow. Large projects 'rarely finish on the budget or the date first announced', so a project's own plan is usually a poor guide to its cost (1); and starting from what similar projects have actually cost is a remedy that is said to have worked (2). "
   "3 contradicts the passage, which sets bad luck aside as the usual explanation and points to how planners imagine the project going.",
   "1 और 2 निकलते हैं। बड़ी परियोजनाएँ 'पहले घोषित बजट या तारीख़ पर शायद ही पूरी होती हैं', इसलिए परियोजना की अपनी योजना उसकी लागत की प्रायः कमज़ोर मार्गदर्शक होती है (1); और वैसी परियोजनाओं की वास्तविक लागत से शुरू करना ऐसा उपाय है जिसके कारगर रहने की बात कही गई है (2)। "
   "3 परिच्छेद का खंडन करता है, जो सामान्य व्याख्या के रूप में बुरी क़िस्मत को किनारे रखता है और इस ओर इशारा करता है कि योजनाकार परियोजना को कैसे चलता हुआ कल्पित करते हैं।",
   "conclusions",
   st=["A project's own plan is usually a poor guide to what the project will cost.",
       "The record of similar projects can improve an estimate of cost.",
       "Most overruns are the result of bad luck rather than of how the projects were planned."],
   st_hi=["किसी परियोजना की अपनी योजना प्रायः उसकी लागत का ख़राब मार्गदर्शक होती है।",
          "वैसी परियोजनाओं का रिकॉर्ड लागत के अनुमान को बेहतर बना सकता है।",
          "अधिकांश अतिरिक्त ख़र्च परियोजनाओं की योजना के तरीक़े से नहीं, बल्कि बुरी क़िस्मत से होते हैं।"],
   opts=["1 only", "1 and 3 only", "2 and 3 only", "1 and 2 only"], key=3)
