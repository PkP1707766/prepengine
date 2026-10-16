# -*- coding: utf-8 -*-
"""CSAT Level 1 · Mini 3 -- Reading Comprehension: 5 original passages, 14 items (four with three items, the third
passage with two), at the foundation level: passages of about 140-150 words and 4 easy / 8 medium / 2 hard items.

Themes, none used in Level 2's 70 passages or in Minis 1-2: mobile phones and the price of fish on the Kerala coast,
the reporting of near misses in aviation, how the railways brought standard time, what people resent about queues,
and advertising aimed at young children. Item types: main idea 3, inference 4, assumption 2, tone 1, specific detail 2,
best summary 2. Options are named by content in every explanation."""
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
TONE = "Which one of the following best describes the author's approach in the passage?"
TONE_HI = "निम्नलिखित में से कौन-सा परिच्छेद में लेखक के दृष्टिकोण का सबसे अच्छा वर्णन करता है?"

# ------------------------------------------------------------------ P01 mobile phones and the price of fish (3)
p = passage("p01",
  "Along the coast of Kerala in the late 1990s, a fisherman returning with a catch had to choose a market before reaching land, without knowing what prices were on offer. "
  "Some days one market was flooded and prices collapsed, while at another a few kilometres away buyers waited with nothing to buy. Fish that could not be sold was thrown away. "
  "When mobile phone networks reached the coast, fishermen began calling markets from their boats and steering for the one that offered the best price. "
  "Within a few years, prices across the markets became far more even, very little fish was wasted, and both the fishermen's earnings and the buyers' supplies became more dependable. "
  "Nothing about the fish or the boats had changed; what had changed was that each seller could now see the whole market before choosing where to sell.",
  "1990 के दशक के अंतिम वर्षों में केरल के तट पर, मछली पकड़कर लौटने वाले मछुआरे को किनारे पहुँचने से पहले ही कोई बाज़ार चुनना पड़ता था, बिना यह जाने कि वहाँ क्या दाम मिल रहे हैं। "
  "कुछ दिनों एक बाज़ार में मछली की भरमार हो जाती और दाम गिर जाते, जबकि कुछ किलोमीटर दूर दूसरे बाज़ार में ख़रीदार ख़ाली हाथ इंतज़ार करते। जो मछली नहीं बिकती, वह फेंक दी जाती। "
  "जब मोबाइल फ़ोन नेटवर्क तट तक पहुँचे, तो मछुआरे अपनी नावों से बाज़ारों को फ़ोन करने लगे और उस बाज़ार की ओर जाने लगे जहाँ सबसे अच्छा दाम मिल रहा हो। "
  "कुछ ही वर्षों में बाज़ारों के बीच दाम कहीं अधिक एक-से हो गए, बहुत कम मछली बर्बाद हुई, और मछुआरों की कमाई और ख़रीदारों की आपूर्ति दोनों अधिक भरोसेमंद हो गईं। "
  "मछली या नावों में कुछ नहीं बदला था; बदला यह था कि अब हर विक्रेता कहाँ बेचना है यह चुनने से पहले पूरा बाज़ार देख सकता था।")
RQ(p, "Specific Detail", "easy", "mcq",
   "According to the passage, what did fishermen do once mobile phone networks reached the coast?",
   "परिच्छेद के अनुसार, मोबाइल फ़ोन नेटवर्क तट तक पहुँचने के बाद मछुआरों ने क्या किया?",
   "The passage says that fishermen 'began calling markets from their boats and steering for the one that offered the best price'. "
   "It does not say that they stayed ashore on some days or sold their whole catch in advance, and it says that nothing about the boats had changed, so they did not carry larger catches.",
   "परिच्छेद कहता है कि मछुआरे 'अपनी नावों से बाज़ारों को फ़ोन करने लगे और उस बाज़ार की ओर जाने लगे जहाँ सबसे अच्छा दाम मिल रहा हो'। "
   "वह यह नहीं कहता कि वे कुछ दिन किनारे पर रहे या पहले से पूरी पकड़ बेच दी, और वह कहता है कि नावों में कुछ नहीं बदला था, इसलिए वे बड़ी पकड़ नहीं ले जा रहे थे।",
   "detail",
   opts=["They called markets from their boats and went to the one offering the best price.",
         "They stopped going out to sea on the days when the markets were flooded with fish.",
         "They sold their whole catch to a single buyer before setting out each morning.",
         "They threw back less fish, because their boats could now carry and keep larger catches."],
   opts_hi=["वे नावों से बाज़ारों को फ़ोन करके सबसे अच्छा दाम देने वाले बाज़ार में गए।",
            "जिन दिनों बाज़ारों में मछली की भरमार होती, उन दिनों उन्होंने समुद्र में जाना बंद कर दिया।",
            "वे हर सुबह निकलने से पहले अपनी पूरी पकड़ एक ही ख़रीदार को बेच देते थे।",
            "उन्होंने कम मछली फेंकी, क्योंकि अब उनकी नावें बड़ी पकड़ ले जा और रख सकती थीं।"],
   ans=0, pos=2)
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage shows that once fishermen could learn prices before choosing a market, prices evened out and waste fell -- and it ends by saying that the only change was that sellers 'could now see the whole market'. "
   "It says nothing about faster boats or bigger catches; it reports more even and dependable prices, not a sharp rise; and it proposes no merging of markets.",
   "परिच्छेद दिखाता है कि जब मछुआरे बाज़ार चुनने से पहले दाम जान सकने लगे, तो दाम एक-से हो गए और बर्बादी घटी -- और अंत में कहता है कि एकमात्र बदलाव यह था कि विक्रेता 'अब पूरा बाज़ार देख सकते थे'। "
   "वह तेज़ नावों या बड़ी पकड़ के बारे में कुछ नहीं कहता; वह अधिक एक-से और भरोसेमंद दामों की बात करता है, तेज़ वृद्धि की नहीं; और वह बाज़ारों को मिलाने का कोई प्रस्ताव नहीं देता।",
   "crux",
   opts=["Better information let sellers choose where to sell, making prices steadier and cutting waste.",
         "Mobile phones made fishing boats faster and allowed fishermen to catch more fish than before.",
         "Fishermen in Kerala earned more because the price of fish rose sharply once phones arrived.",
         "Markets a few kilometres apart should be merged so that buyers and sellers can meet in one place."],
   opts_hi=["बेहतर जानकारी से विक्रेता चुन सके कि कहाँ बेचें, जिससे दाम स्थिर हुए और बर्बादी घटी।",
            "मोबाइल फ़ोन ने मछली पकड़ने वाली नावों को तेज़ बनाया और मछुआरे पहले से अधिक मछली पकड़ने लगे।",
            "केरल के मछुआरों ने अधिक कमाया क्योंकि फ़ोन आने के बाद मछली के दाम तेज़ी से बढ़ गए।",
            "कुछ किलोमीटर दूर के बाज़ारों को मिला देना चाहिए ताकि ख़रीदार और विक्रेता एक ही जगह मिल सकें।"],
   ans=0, pos=3)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Only 1 is valid: before phones, a fisherman chose a market without knowing its prices, and some days one market was flooded while another had no fish, so what he received depended partly on how that choice happened to turn out. "
   "2 is not: the passage says that 'nothing about the fish or the boats had changed'; it reports less waste and steadier prices, not a larger catch.",
   "केवल 1 वैध है: फ़ोन से पहले मछुआरा बिना दाम जाने बाज़ार चुनता था, और कुछ दिनों एक बाज़ार में भरमार होती जबकि दूसरे में मछली ही नहीं होती, इसलिए उसे जो मिलता वह कुछ हद तक इस पर निर्भर था कि उसका चुनाव संयोग से कैसा निकला। "
   "2 वैध नहीं है: परिच्छेद कहता है कि 'मछली या नावों में कुछ नहीं बदला था'; वह कम बर्बादी और स्थिर दामों की बात करता है, बड़ी पकड़ की नहीं।",
   "conclusions",
   st=["Before phones, the price a fisherman received depended partly on luck in choosing a market.",
       "The spread of phones increased the total amount of fish caught along the coast."],
   st_hi=["फ़ोन से पहले, मछुआरे को मिलने वाला दाम कुछ हद तक बाज़ार चुनने में भाग्य पर निर्भर था।",
          "फ़ोन के फैलने से तट पर पकड़ी जाने वाली मछली की कुल मात्रा बढ़ गई।"],
   key=0)

# ------------------------------------------------------------------ P02 reporting near misses (3)
p = passage("p02",
  "In aviation, a near miss -- two aircraft passing closer than they should, a wrong switch caught just in time -- is treated not as luck to be forgotten but as a lesson to be studied. "
  "Pilots and controllers are encouraged to report their own mistakes, and the reports are used to find the weak points in procedures before they cause a crash. "
  "This works because those who report are, as a rule, not punished for honest errors; a person who expects to be blamed will stay silent, and the weakness stays hidden. "
  "Hospitals, railways and factories have tried to copy the idea, with mixed results. Where a mistake still leads to suspension or a court case, the forms are filled in but say little. "
  "A reporting system is only as good as the trust that people place in it.",
  "विमानन में बाल-बाल बची दुर्घटना -- दो विमानों का तय दूरी से अधिक पास से गुज़रना, ग़लत स्विच का ठीक समय पर पकड़ में आ जाना -- भूल जाने वाला संयोग नहीं, बल्कि अध्ययन करने योग्य सबक़ मानी जाती है। "
  "पायलटों और नियंत्रकों को अपनी ग़लतियाँ स्वयं बताने के लिए प्रोत्साहित किया जाता है, और इन रिपोर्टों से प्रक्रियाओं की कमज़ोरियाँ दुर्घटना होने से पहले ही खोजी जाती हैं। "
  "यह इसलिए चलता है कि रिपोर्ट करने वालों को सामान्यतः ईमानदार भूल के लिए दंड नहीं दिया जाता; जो व्यक्ति दोष दिए जाने की अपेक्षा करता है वह चुप रहेगा, और कमज़ोरी छिपी रहेगी। "
  "अस्पतालों, रेलवे और कारख़ानों ने इस विचार को अपनाने का प्रयास किया है, मिले-जुले परिणामों के साथ। जहाँ ग़लती पर अब भी निलंबन या मुक़दमा होता है, वहाँ फ़ॉर्म भरे तो जाते हैं पर उनमें कुछ ख़ास नहीं होता। "
  "कोई रिपोर्टिंग व्यवस्था उतनी ही अच्छी होती है जितना लोग उस पर भरोसा करते हैं।")
RQ(p, "Best Summary", "medium", "mcq", SUMMARY, SUMMARY_HI,
   "The passage explains that aviation learns from near misses because people report their own mistakes without fear of punishment, and that copies elsewhere work poorly where mistakes are still punished: a reporting system is only as good as the trust placed in it. "
   "It does not compare how careful pilots and doctors are; it argues against, not for, strict inquiries to find someone to blame; and it treats near misses as lessons, not as matters of luck.",
   "परिच्छेद समझाता है कि विमानन बाल-बाल बची दुर्घटनाओं से इसलिए सीखता है कि लोग बिना दंड के डर के अपनी ग़लतियाँ बताते हैं, और कि दूसरी जगहों पर इसकी नक़ल वहाँ ठीक नहीं चलती जहाँ ग़लतियों पर अब भी दंड मिलता है: रिपोर्टिंग व्यवस्था उतनी ही अच्छी है जितना उस पर भरोसा। "
   "वह पायलटों और डॉक्टरों की सावधानी की तुलना नहीं करता; वह दोषी ढूँढ़ने के लिए कड़ी जाँच के विरुद्ध तर्क देता है, पक्ष में नहीं; और वह बाल-बाल बची दुर्घटनाओं को सबक़ मानता है, संयोग नहीं।",
   "summary",
   opts=["Reporting mistakes improves safety only where people trust that honest errors go unpunished.",
         "Aviation is safer than medicine because pilots are more careful than doctors and nurses are.",
         "Every mistake at work should lead to a strict inquiry so that the person responsible is found.",
         "Near misses in aviation are matters of luck, and studying them has done little to prevent crashes."],
   opts_hi=["ग़लतियाँ बताने से सुरक्षा तभी बढ़ती है जब लोगों को भरोसा हो कि ईमानदार भूल पर दंड नहीं मिलेगा।",
            "विमानन चिकित्सा से अधिक सुरक्षित है क्योंकि पायलट डॉक्टरों और नर्सों से अधिक सावधान होते हैं।",
            "काम पर हर ग़लती की कड़ी जाँच होनी चाहिए ताकि उसके लिए ज़िम्मेदार व्यक्ति का पता चले।",
            "विमानन में बाल-बाल बची दुर्घटनाएँ संयोग हैं, और उनके अध्ययन से दुर्घटनाएँ रोकने में बहुत कम मदद मिली है।"],
   ans=0, pos=3)
RQ(p, "Assumption", "medium", "s2", ASSUME, ASSUME_HI,
   "Only 2 is assumed. The passage relies on people reporting their own mistakes to find the weak points in procedures, and says that if they stay silent 'the weakness stays hidden' -- which takes for granted that many such weaknesses come to light only through those who make the mistakes. "
   "1 is not assumed: the passage compares how well reporting systems work in different fields, not how often pilots and other workers make mistakes.",
   "केवल 2 पूर्वधारणा है। परिच्छेद प्रक्रियाओं की कमज़ोरियाँ खोजने के लिए लोगों द्वारा अपनी ग़लतियाँ बताने पर निर्भर है, और कहता है कि यदि वे चुप रहें तो 'कमज़ोरी छिपी रहेगी' -- जो यह मानकर चलता है कि ऐसी कई कमज़ोरियाँ केवल ग़लती करने वालों के माध्यम से ही सामने आती हैं। "
   "1 पूर्वधारणा नहीं है: परिच्छेद अलग-अलग क्षेत्रों में रिपोर्टिंग व्यवस्थाओं के चलने की तुलना करता है, इसकी नहीं कि पायलट और दूसरे कर्मचारी कितनी बार ग़लती करते हैं।",
   "assumptions",
   st=["Pilots make fewer mistakes than people who work in hospitals and factories.",
       "Many weaknesses in procedures become known only through the people who make mistakes."],
   st_hi=["पायलट अस्पतालों और कारख़ानों में काम करने वालों से कम ग़लतियाँ करते हैं।",
          "प्रक्रियाओं की कई कमज़ोरियाँ केवल ग़लती करने वाले लोगों के माध्यम से ही पता चलती हैं।"],
   key=1)
RQ(p, "Inference", "hard", "sc", INFER, INFER_HI,
   "1 can be drawn: where mistakes are still punished, 'the forms are filled in but say little', so a system can appear to be in use while it reveals almost nothing. "
   "3 can be drawn: the reports are used 'to find the weak points in procedures before they cause a crash'. "
   "2 cannot: the passage says that hospitals copied the idea 'with mixed results', which gives no ground for saying that they have become as safe as aviation. The inferences that can be drawn are 1 and 3.",
   "1 निकाला जा सकता है: जहाँ ग़लतियों पर अब भी दंड मिलता है, वहाँ 'फ़ॉर्म भरे तो जाते हैं पर उनमें कुछ ख़ास नहीं होता', इसलिए कोई व्यवस्था चलती हुई दिख सकती है जबकि वह लगभग कुछ भी सामने नहीं लाती। "
   "3 निकाला जा सकता है: रिपोर्टों से 'प्रक्रियाओं की कमज़ोरियाँ दुर्घटना होने से पहले ही खोजी जाती हैं'। "
   "2 नहीं निकाला जा सकता: परिच्छेद कहता है कि अस्पतालों ने यह विचार 'मिले-जुले परिणामों के साथ' अपनाया, जो यह कहने का कोई आधार नहीं देता कि वे विमानन जितने सुरक्षित हो गए हैं। जो अनुमान निकाले जा सकते हैं वे 1 और 3 हैं।",
   "inferences",
   st=["Fear of punishment can make a reporting system look as if it is working when it is not.",
       "Hospitals that adopted reporting systems have become as safe as aviation.",
       "A weakness in a procedure can be found before it has caused any crash."],
   st_hi=["दंड का डर किसी रिपोर्टिंग व्यवस्था को ऐसा दिखा सकता है मानो वह काम कर रही हो, जबकि वह नहीं कर रही।",
          "जिन अस्पतालों ने रिपोर्टिंग व्यवस्थाएँ अपनाईं, वे विमानन जितने सुरक्षित हो गए हैं।",
          "किसी प्रक्रिया की कमज़ोरी किसी दुर्घटना का कारण बनने से पहले ही खोजी जा सकती है।"],
   opts=["1 only", "1 and 2 only", "1 and 3 only", "1, 2 and 3"], key=2)

# ------------------------------------------------------------------ P03 the railways and standard time (2)
p = passage("p03",
  "Until the middle of the nineteenth century, every town set its clocks by the sun: noon was the moment the sun stood highest, which came a few minutes later in each town lying further west. "
  "This mattered little while people travelled on horseback. The railways changed that. A timetable that listed a dozen local times was a recipe for missed trains and, on lines with a single track, for collisions. "
  "So the railway companies adopted one standard time for all their stations, and in country after country governments later made such a time the official one. "
  "People who had always lived by the sun now lived by the timetable. A change made for the convenience of one industry reshaped the way whole nations told the time.",
  "उन्नीसवीं सदी के मध्य तक हर कस्बा अपनी घड़ियाँ सूर्य के अनुसार मिलाता था: दोपहर वह क्षण था जब सूर्य सबसे ऊँचा होता, और यह क्षण पश्चिम की ओर स्थित हर कस्बे में कुछ मिनट बाद आता था। "
  "जब तक लोग घोड़ों पर यात्रा करते थे, इससे बहुत अंतर नहीं पड़ता था। रेलवे ने यह बदल दिया। एक दर्जन स्थानीय समय दिखाने वाली समय-सारणी ट्रेनें छूटने का और एकल पटरी वाली लाइनों पर टक्करों का कारण बन सकती थी। "
  "इसलिए रेल कंपनियों ने अपने सभी स्टेशनों के लिए एक मानक समय अपनाया, और एक के बाद एक देशों में सरकारों ने बाद में ऐसे समय को आधिकारिक बना दिया। "
  "जो लोग सदा सूर्य के अनुसार जीते आए थे, वे अब समय-सारणी के अनुसार जीने लगे। एक उद्योग की सुविधा के लिए किए गए बदलाव ने पूरे राष्ट्रों के समय बताने का ढंग बदल दिया।")
RQ(p, "Main Idea", "easy", "mcq", CRUX, CRUX_HI,
   "The passage traces standard time from the railways' need for a single time on their timetables to governments making such a time official, and ends that a change made for one industry reshaped how whole nations told the time. "
   "It does not say that railway clocks were more accurate; it does not call solar time wrong -- it served well while travel was slow; and it says nothing about replacing single-track lines.",
   "परिच्छेद मानक समय को रेलवे की अपनी समय-सारणियों के लिए एक समय की आवश्यकता से लेकर सरकारों द्वारा ऐसे समय को आधिकारिक बनाने तक ले जाता है, और अंत में कहता है कि एक उद्योग के लिए किए गए बदलाव ने पूरे राष्ट्रों के समय बताने का ढंग बदल दिया। "
   "वह यह नहीं कहता कि रेलवे की घड़ियाँ अधिक सटीक थीं; वह सूर्य के समय को ग़लत नहीं कहता -- धीमी यात्रा के समय वह ठीक काम करता था; और वह एकल पटरी वाली लाइनों को बदलने के बारे में कुछ नहीं कहता।",
   "crux",
   opts=["Standard time began as a railway convenience and went on to change how whole nations kept time.",
         "Railways were the first to measure time accurately, because their clocks were better than those of the towns.",
         "Setting clocks by the sun was a mistake, and towns should never have kept their own local times.",
         "Single-track railway lines were dangerous, so governments replaced them with double-track lines."],
   opts_hi=["मानक समय रेलवे की सुविधा से शुरू हुआ और फिर पूरे राष्ट्रों के समय रखने का ढंग बदल गया।",
            "रेलवे ने सबसे पहले समय सटीक रूप से मापा, क्योंकि उनकी घड़ियाँ कस्बों की घड़ियों से बेहतर थीं।",
            "घड़ियाँ सूर्य के अनुसार मिलाना एक भूल थी, और कस्बों को कभी अपना स्थानीय समय नहीं रखना चाहिए था।",
            "एकल पटरी वाली रेल लाइनें ख़तरनाक थीं, इसलिए सरकारों ने उन्हें दोहरी पटरी वाली लाइनों से बदल दिया।"],
   ans=0, pos=2)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Only 1 is valid: each town's noon came a few minutes later the further west it lay, so two towns on the same line could show different times at the same moment -- which is why a timetable listed 'a dozen local times'. "
   "2 is not: the passage says that the railway companies adopted standard time first and that governments made it official 'later'.",
   "केवल 1 वैध है: हर कस्बे की दोपहर जितना वह पश्चिम में हो उतने कुछ मिनट बाद आती थी, इसलिए एक ही लाइन के दो कस्बे एक ही क्षण में अलग-अलग समय दिखा सकते थे -- इसी कारण समय-सारणी में 'एक दर्जन स्थानीय समय' होते थे। "
   "2 वैध नहीं है: परिच्छेद कहता है कि मानक समय पहले रेल कंपनियों ने अपनाया और सरकारों ने उसे 'बाद में' आधिकारिक बनाया।",
   "conclusions",
   st=["Before standard time, two towns on the same railway line might show different times at the same moment.",
       "Governments adopted a standard time before the railway companies did."],
   st_hi=["मानक समय से पहले, एक ही रेल लाइन पर स्थित दो कस्बे एक ही क्षण में अलग-अलग समय दिखा सकते थे।",
          "सरकारों ने रेल कंपनियों से पहले मानक समय अपनाया।"],
   key=0)

# ------------------------------------------------------------------ P04 what people resent about queues (3)
p = passage("p04",
  "People will wait a long time in a queue without complaint, yet lose their temper over a short wait that seems unfair. A customer who has waited ten minutes and sees a latecomer served first is angrier than one who has waited twenty minutes in strict order. "
  "Waits also feel longer when nothing is happening and when nobody says how long they will last: a sign saying 'about fifteen minutes from here' can make the same wait easier to bear. "
  "Banks and hospitals that have taken such findings seriously have often cut complaints without cutting waiting times at all, by using a single line, a token system and a screen that shows the queue moving. "
  "Waiting is a cost, but much of what people resent is not the minutes; it is the sense of being ignored or cheated.",
  "लोग बिना शिकायत के क़तार में देर तक प्रतीक्षा कर लेते हैं, फिर भी किसी ऐसी छोटी प्रतीक्षा पर आपा खो देते हैं जो अनुचित लगे। जिस ग्राहक ने दस मिनट प्रतीक्षा की और देखा कि बाद में आए व्यक्ति को पहले सेवा मिली, वह उससे अधिक नाराज़ होता है जिसने सख़्त क्रम में बीस मिनट प्रतीक्षा की। "
  "प्रतीक्षा तब भी लंबी लगती है जब कुछ हो नहीं रहा होता और जब कोई नहीं बताता कि वह कितनी देर चलेगी: 'यहाँ से लगभग पंद्रह मिनट' लिखा एक बोर्ड उसी प्रतीक्षा को सहना आसान बना सकता है। "
  "जिन बैंकों और अस्पतालों ने ऐसे निष्कर्षों को गंभीरता से लिया है, उन्होंने अक्सर प्रतीक्षा का समय बिल्कुल घटाए बिना शिकायतें घटा दी हैं, एक ही क़तार, टोकन व्यवस्था और क़तार को आगे बढ़ता दिखाने वाली स्क्रीन के सहारे। "
  "प्रतीक्षा एक क़ीमत है, पर लोगों को जो बुरा लगता है उसका बड़ा भाग मिनट नहीं होते; वह अनदेखा किए जाने या ठगे जाने का भाव होता है।")
RQ(p, "Best Summary", "easy", "mcq", SUMMARY, SUMMARY_HI,
   "The passage says that people mind waits that seem unfair or uncertain more than long ones, and that banks and hospitals have cut complaints 'without cutting waiting times at all' by making queues fair and visible. "
   "It does not ask for more staff, and it says that the main resentment is not about the minutes; nor does it claim that token systems make queues move faster -- only that complaints fell.",
   "परिच्छेद कहता है कि लोग लंबी प्रतीक्षा से अधिक उस प्रतीक्षा को बुरा मानते हैं जो अनुचित या अनिश्चित लगे, और कि बैंकों और अस्पतालों ने क़तारों को उचित और दिखाई देने वाला बनाकर 'प्रतीक्षा का समय बिल्कुल घटाए बिना' शिकायतें घटाई हैं। "
   "वह अधिक कर्मचारियों की माँग नहीं करता, और कहता है कि मुख्य नाराज़गी मिनटों की नहीं होती; न ही वह दावा करता है कि टोकन व्यवस्था क़तार को तेज़ चलाती है -- केवल यह कि शिकायतें घटीं।",
   "summary",
   opts=["Banks and hospitals should hire many more staff, since long queues are the main cause of their customers' complaints.",
         "Much of what people resent in waiting is unfairness and uncertainty, which can be eased without shortening waits.",
         "People complain mainly about the number of minutes they spend waiting in a queue for service.",
         "Token systems and screens make every queue move faster than a single line ever could."],
   opts_hi=["बैंकों और अस्पतालों को बहुत अधिक कर्मचारी रखने चाहिए, क्योंकि लंबी क़तारें ही उनके ग्राहकों की शिकायतों का मुख्य कारण हैं।",
            "प्रतीक्षा में लोगों को जो बुरा लगता है वह अधिकतर अनुचितता और अनिश्चितता है, जिसे प्रतीक्षा घटाए बिना कम किया जा सकता है।",
            "लोग मुख्य रूप से उन मिनटों की शिकायत करते हैं जो वे सेवा के लिए क़तार में प्रतीक्षा करते हुए बिताते हैं।",
            "टोकन व्यवस्था और स्क्रीनें हर क़तार को उससे तेज़ चलाती हैं जितना एक अकेली क़तार कभी चल सकती है।"],
   ans=1, pos=1)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Neither is valid. 1: the passage says that banks and hospitals cut complaints 'without cutting waiting times at all', so it gives no ground for saying that a single line moves faster. "
   "2: the passage says only that being told how long a wait will last can make it 'easier to bear', not that people stop minding the wait altogether.",
   "कोई भी वैध नहीं है। 1: परिच्छेद कहता है कि बैंकों और अस्पतालों ने 'प्रतीक्षा का समय बिल्कुल घटाए बिना' शिकायतें घटाईं, इसलिए यह कहने का कोई आधार नहीं कि एक अकेली क़तार तेज़ चलती है। "
   "2: परिच्छेद केवल इतना कहता है कि प्रतीक्षा की अवधि बताए जाने से वह 'सहना आसान' हो सकती है, यह नहीं कि लोग प्रतीक्षा का बुरा मानना ही छोड़ देते हैं।",
   "conclusions",
   st=["A single line served in strict order always moves faster than several separate lines do.",
       "Customers who are told how long a wait will last no longer mind waiting at all."],
   st_hi=["सख़्त क्रम में चलने वाली एक अकेली क़तार सदा कई अलग-अलग क़तारों से तेज़ चलती है।",
          "जिन ग्राहकों को बताया जाता है कि प्रतीक्षा कितनी देर चलेगी, वे प्रतीक्षा का बिल्कुल भी बुरा नहीं मानते।"],
   key=3)
RQ(p, "Author's Tone", "medium", "mcq", TONE, TONE_HI,
   "The author explains why people react to waiting as they do -- unfairness, idleness and uncertainty -- and reports what has worked, without blaming anyone. "
   "That is analytical. The author does not attack banks and hospitals, does not mock people who lose their temper (their anger is explained, not ridiculed), and is not resigned -- the passage shows waits being made easier to bear.",
   "लेखक समझाता है कि लोग प्रतीक्षा पर वैसी प्रतिक्रिया क्यों करते हैं -- अनुचितता, ख़ाली बैठना और अनिश्चितता -- और बताता है कि क्या कारगर रहा है, बिना किसी को दोष दिए। "
   "यह विश्लेषणात्मक है। लेखक बैंकों और अस्पतालों पर आक्रोश नहीं जताता, आपा खोने वालों का उपहास नहीं करता (उनके ग़ुस्से को समझाया गया है, उसकी हँसी नहीं उड़ाई गई), और न हताश है -- परिच्छेद प्रतीक्षा को सहने योग्य बनाए जाने के उदाहरण देता है।",
   "tone",
   opts=["Analytical, explaining why people feel as they do about waiting",
         "Indignant at banks and hospitals for keeping people waiting",
         "Mocking towards people who lose their temper in queues",
         "Resigned, accepting that long waits can never be made any easier to bear"],
   opts_hi=["विश्लेषणात्मक, यह समझाता हुआ कि लोग प्रतीक्षा के बारे में वैसा क्यों महसूस करते हैं",
            "लोगों को प्रतीक्षा कराने के लिए बैंकों और अस्पतालों पर आक्रोशित",
            "क़तारों में आपा खोने वाले लोगों का उपहास करता हुआ",
            "हताश, यह मानते हुए कि लंबी प्रतीक्षा को कभी भी किसी तरह सहने योग्य नहीं बनाया जा सकता"],
   ans=0, pos=0)

# ------------------------------------------------------------------ P05 advertising aimed at young children (3)
p = passage("p05",
  "Young children watch advertisements with the same trust they bring to the programmes around them. Studies suggest that until about the age of eight, many children cannot tell that an advertisement is trying to sell them something; "
  "they take it as one more piece of information, much as they would a cartoon or a lesson. An adult who sees an advertisement for a sugary drink knows that the seller is making a case; a five-year-old may simply believe that the drink makes children strong and happy. "
  "For this reason several countries limit or ban advertising aimed at young children. Critics say that parents, not governments, should decide what children watch. "
  "But a protection that depends on every parent watching every screen at every hour will, in practice, protect only some children.",
  "छोटे बच्चे विज्ञापनों को उसी भरोसे से देखते हैं जिस भरोसे से वे उनके आसपास के कार्यक्रम देखते हैं। अध्ययन संकेत देते हैं कि लगभग आठ वर्ष की आयु तक बहुत से बच्चे यह नहीं पहचान पाते कि कोई विज्ञापन उन्हें कुछ बेचने का प्रयास कर रहा है; "
  "वे उसे जानकारी का एक और टुकड़ा मान लेते हैं, लगभग वैसे ही जैसे कोई कार्टून या पाठ। मीठे पेय का विज्ञापन देखने वाला वयस्क जानता है कि विक्रेता अपना पक्ष रख रहा है; पाँच वर्ष का बच्चा सीधे मान सकता है कि वह पेय बच्चों को बलवान और ख़ुश बनाता है। "
  "इसी कारण कई देश छोटे बच्चों को लक्ष्य करने वाले विज्ञापनों को सीमित करते हैं या उन पर रोक लगाते हैं। आलोचक कहते हैं कि बच्चे क्या देखें, यह सरकारें नहीं, माता-पिता तय करें। "
  "पर जो सुरक्षा हर माता-पिता के हर समय हर स्क्रीन पर नज़र रखने पर निर्भर हो, वह व्यवहार में केवल कुछ ही बच्चों की रक्षा करेगी।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage says that young children take advertisements at face value, explains why several countries limit advertising aimed at them, and answers the critics: protection that depends on every parent watching every screen protects only some children. "
   "It does not call for banning sugary-drink advertisements for all viewers; it reports the view that parents should decide only in order to answer it; and it says nothing about children over eight being immune to advertisements.",
   "परिच्छेद कहता है कि छोटे बच्चे विज्ञापनों को ज्यों का त्यों मान लेते हैं, समझाता है कि कई देश उन्हें लक्ष्य करने वाले विज्ञापनों को क्यों सीमित करते हैं, और आलोचकों को उत्तर देता है: जो सुरक्षा हर माता-पिता के हर स्क्रीन पर नज़र रखने पर निर्भर हो, वह केवल कुछ बच्चों की रक्षा करती है। "
   "वह सभी दर्शकों के लिए मीठे पेयों के विज्ञापनों पर रोक की माँग नहीं करता; माता-पिता के तय करने वाले मत का उल्लेख केवल उसका उत्तर देने के लिए करता है; और आठ वर्ष से बड़े बच्चों के विज्ञापनों से अप्रभावित होने के बारे में कुछ नहीं कहता।",
   "crux",
   opts=["Advertisements for sugary drinks should be banned on every channel, for viewers of every age, children and adults alike.",
         "Since young children take ads at face value, limits on ads aimed at them protect better than parents alone.",
         "Parents, not governments, should decide what their young children are allowed to watch on screen.",
         "Children over the age of eight are no longer influenced by any advertisement that they watch."],
   opts_hi=["मीठे पेयों के विज्ञापनों पर हर चैनल पर, हर आयु के सभी दर्शकों के लिए, बच्चों और वयस्कों दोनों के लिए, रोक लगनी चाहिए।",
            "छोटे बच्चे विज्ञापनों को सच मान लेते हैं, इसलिए उन पर लक्षित विज्ञापनों की सीमा अकेले माता-पिता से बेहतर रक्षा है।",
            "छोटे बच्चे स्क्रीन पर क्या देखें, यह सरकारें नहीं, उनके माता-पिता तय करें।",
            "आठ वर्ष से बड़े बच्चे अपने देखे किसी भी विज्ञापन से प्रभावित नहीं होते।"],
   ans=1, pos=1)
RQ(p, "Assumption", "hard", "s2", ASSUME, ASSUME_HI,
   "Both are assumed. 1: the case for limiting such advertisements -- a child may believe that a drink makes children strong and happy -- matters only if the advertisements can shape what young children want or ask for. "
   "2: the reply to the critics, that protection depending on every parent watching every screen 'will, in practice, protect only some children', rests on the premise that many parents cannot watch all that their young children see.",
   "दोनों पूर्वधारणाएँ हैं। 1: ऐसे विज्ञापनों को सीमित करने का पक्ष -- कि बच्चा मान सकता है कि कोई पेय बच्चों को बलवान और ख़ुश बनाता है -- तभी मायने रखता है जब विज्ञापन यह प्रभावित कर सकें कि छोटे बच्चे क्या चाहते या माँगते हैं। "
   "2: आलोचकों को दिया गया उत्तर, कि हर माता-पिता के हर स्क्रीन पर नज़र रखने पर निर्भर सुरक्षा 'व्यवहार में केवल कुछ ही बच्चों की रक्षा करेगी', इस आधार पर टिका है कि बहुत से माता-पिता वह सब नहीं देख सकते जो उनके छोटे बच्चे देखते हैं।",
   "assumptions",
   st=["Advertisements aimed at young children can influence what those children want or ask for.",
       "Many parents are not able to watch everything that their young children see on screens."],
   st_hi=["छोटे बच्चों को लक्ष्य करने वाले विज्ञापन इस पर प्रभाव डाल सकते हैं कि वे बच्चे क्या चाहते या माँगते हैं।",
          "बहुत से माता-पिता वह सब नहीं देख पाते जो उनके छोटे बच्चे स्क्रीन पर देखते हैं।"],
   key=2)
RQ(p, "Specific Detail", "easy", "mcq",
   "According to the passage, what do many children below about the age of eight fail to understand?",
   "परिच्छेद के अनुसार, लगभग आठ वर्ष से कम आयु के बहुत से बच्चे क्या नहीं समझ पाते?",
   "The passage says that until about the age of eight, many children 'cannot tell that an advertisement is trying to sell them something'. "
   "It does not say that they fail to understand that sugary drinks can harm them, that programmes are made by adults, or that parents decide what they watch.",
   "परिच्छेद कहता है कि लगभग आठ वर्ष की आयु तक बहुत से बच्चे 'यह नहीं पहचान पाते कि कोई विज्ञापन उन्हें कुछ बेचने का प्रयास कर रहा है'। "
   "वह यह नहीं कहता कि वे यह नहीं समझते कि मीठे पेय हानि कर सकते हैं, कि कार्यक्रम वयस्क बनाते हैं, या कि वे क्या देखें यह माता-पिता तय करते हैं।",
   "detail",
   opts=["That an advertisement is trying to sell them something",
         "That sugary drinks can do harm to their health and teeth",
         "That cartoons and lessons are made by adults",
         "That their parents decide what they may watch"],
   opts_hi=["कि कोई विज्ञापन उन्हें कुछ बेचने का प्रयास कर रहा है",
            "कि मीठे पेय उनके स्वास्थ्य और दाँतों को हानि पहुँचा सकते हैं",
            "कि कार्टून और पाठ वयस्क बनाते हैं",
            "कि वे क्या देखें यह उनके माता-पिता तय करते हैं"],
   ans=0, pos=0)
