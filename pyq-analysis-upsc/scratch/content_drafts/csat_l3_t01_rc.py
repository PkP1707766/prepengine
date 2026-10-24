# -*- coding: utf-8 -*-
"""CSAT Level 3 · Test 1 -- Reading Comprehension: 10 original passages, 28 items (8 x 3, 2 x 2).

Level 3 passages carry a turn in the argument -- a claim, then its limit -- so that the items test where the author
stops as much as what the author says. Themes, none used in Level 2 Tests 1-7 or Level 1 Minis 1-3: a measure that
becomes a target, the paradox of thrift, the precautionary principle and gene drives, deposit insurance and the risks
banks take, village commons and the rules that keep them, findings that fail to repeat, carbon offsets that change
nothing, transfers from the Centre to poorer States, Ashoka's case for restraint in speech, and lending decided by
algorithms. Item types: main idea 7, best summary 3, inference 9, assumption 5, tone 1, specific detail 3 (one
'NOT mentioned'). Difficulty 3 easy / 13 medium / 12 hard. Options are named by content in every explanation."""
from csat_common import passage, RQ

CRUX = "Which one of the following statements best reflects the crux of the passage?"
CRUX_HI = "निम्नलिखित में से कौन-सा कथन परिच्छेद के सार को सबसे अच्छी तरह व्यक्त करता है?"
MSG = "Which one of the following statements best reflects the most logical and rational message conveyed by the passage?"
MSG_HI = "निम्नलिखित में से कौन-सा कथन परिच्छेद द्वारा दिए गए सबसे तार्किक और विवेकपूर्ण संदेश को सबसे अच्छी तरह व्यक्त करता है?"
VALID = "On the basis of the passage, which of the following conclusions is/are valid?"
VALID_HI = "परिच्छेद के आधार पर निम्नलिखित में से कौन-सा/से निष्कर्ष वैध है/हैं?"
ASSUME = "Which of the following assumptions has/have been made in the passage?"
ASSUME_HI = "परिच्छेद में निम्नलिखित में से कौन-सी पूर्वधारणा/एँ बनाई गई है/हैं?"
INFER1 = "Which one of the following can be inferred from the passage?"
INFER1_HI = "परिच्छेद से निम्नलिखित में से किसका अनुमान लगाया जा सकता है?"

# ------------------------------------------------------------------ P01 a measure that becomes a target (3)
p = passage("p01",
  "When a measure becomes a target, it tends to stop measuring what it once did. A hospital judged by how quickly it discharges patients may send some home too early; a school judged by its pass rate may steer weaker pupils away from the examination; "
  "a police station judged by recorded crime may find reasons not to record it. In each case the number improves while the thing it was meant to reflect stays the same or gets worse. None of this means that measurement is useless. "
  "A number for which nobody is rewarded or punished remains an honest signal, and it is often the only way to see a problem spread too thinly for anyone to notice. The difficulty begins when a single figure is made to carry the whole weight of judgement, "
  "so that those being judged learn to serve the figure rather than the purpose behind it. Using several measures together, and checking them against what people actually experience, makes such gaming harder, though never impossible.",
  "जब कोई माप लक्ष्य बन जाता है, तो वह प्रायः वह मापना बंद कर देता है जो वह पहले मापता था। जिस अस्पताल को इस पर आँका जाए कि वह मरीज़ों को कितनी जल्दी छुट्टी देता है, वह कुछ को बहुत जल्दी घर भेज सकता है; जिस विद्यालय को उसकी उत्तीर्णता दर पर आँका जाए, वह कमज़ोर विद्यार्थियों को परीक्षा से दूर कर सकता है; "
  "जिस थाने को दर्ज अपराधों पर आँका जाए, वह अपराध दर्ज न करने के कारण ढूँढ सकता है। हर मामले में संख्या सुधरती है जबकि वह चीज़ जिसे वह दर्शाने के लिए थी, वैसी ही रहती है या बिगड़ जाती है। इसका यह अर्थ नहीं कि मापना व्यर्थ है। "
  "जिस संख्या के लिए किसी को न पुरस्कार मिलता है न दंड, वह एक ईमानदार संकेत बनी रहती है, और प्रायः किसी ऐसी समस्या को देखने का एकमात्र तरीक़ा होती है जो इतनी बिखरी हो कि किसी का ध्यान न जाए। कठिनाई तब शुरू होती है जब निर्णय का पूरा भार एक ही आँकड़े पर डाल दिया जाता है, "
  "जिससे जिन्हें आँका जा रहा है वे उसके पीछे के उद्देश्य के बजाय आँकड़े की सेवा करना सीख जाते हैं। कई मापों को साथ प्रयोग करना, और उन्हें लोगों के वास्तविक अनुभव से जाँचना, ऐसी चालबाज़ी को कठिन बनाता है, यद्यपि कभी असंभव नहीं।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage shows numbers improving while the reality behind them does not, but then says that measurement is not useless; the trouble starts when one figure carries the whole weight of judgement. The crux joins both halves. "
   "It does not say that numbers are always manipulated or that they should not be used; it says that several measures make gaming harder, 'though never impossible', so it cannot be prevented completely; and it never ranks recorded crime against pass rates or discharge times.",
   "परिच्छेद संख्याओं को सुधरते हुए दिखाता है जबकि उनके पीछे की वास्तविकता नहीं सुधरती, पर फिर कहता है कि मापना व्यर्थ नहीं है; परेशानी तब शुरू होती है जब निर्णय का पूरा भार एक आँकड़े पर हो। सार दोनों हिस्सों को जोड़ता है। "
   "वह यह नहीं कहता कि संख्याओं से हमेशा छेड़छाड़ होती है या उनका प्रयोग नहीं होना चाहिए; वह कहता है कि कई माप चालबाज़ी को कठिन बनाते हैं, 'यद्यपि कभी असंभव नहीं', इसलिए उसे पूरी तरह रोका नहीं जा सकता; और वह दर्ज अपराधों की तुलना उत्तीर्णता दर या छुट्टी के समय से कहीं नहीं करता।",
   "crux",
   opts=["A measure loses its value once one figure becomes the target for judging people, though measuring stays useful.",
         "Numbers should not be used to judge hospitals, schools and police stations, because they are always manipulated.",
         "Gaming of targets can be prevented completely if several measures are used together and checked against experience.",
         "Recorded crime is a poorer measure of performance than either pass rates or the time taken to discharge patients."],
   opts_hi=["जब एक ही आँकड़ा लोगों को आँकने का लक्ष्य बन जाए, तो माप का मूल्य घट जाता है, यद्यपि मापना उपयोगी रहता है।",
            "अस्पतालों, विद्यालयों और थानों को आँकने के लिए संख्याओं का प्रयोग नहीं होना चाहिए, क्योंकि उनसे हमेशा छेड़छाड़ होती है।",
            "यदि कई मापों का साथ प्रयोग हो और उन्हें अनुभव से जाँचा जाए, तो लक्ष्यों की चालबाज़ी पूरी तरह रोकी जा सकती है।",
            "प्रदर्शन के माप के रूप में दर्ज अपराध, उत्तीर्णता दर या मरीज़ों को छुट्टी देने में लगे समय, दोनों से कमज़ोर है।"],
   ans=0, pos=1)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Only 2 is valid. The passage's three examples are cases in which the figure improves while the thing it was meant to reflect stays the same or gets worse, so an improved figure does not by itself show an improved situation. "
   "1 goes too far: the passage says that a measure tied to rewards 'tends to' stop measuring what it did, and that a number nobody is rewarded for stays honest; it does not say that every measure tied to rewards is less accurate than every other.",
   "केवल 2 वैध है। परिच्छेद के तीनों उदाहरण ऐसे हैं जिनमें आँकड़ा सुधरता है जबकि वह चीज़ जिसे उसे दर्शाना था, वैसी ही रहती है या बिगड़ती है, इसलिए सुधरा आँकड़ा अपने-आप सुधरी स्थिति नहीं दिखाता। "
   "1 बहुत आगे चला जाता है: परिच्छेद कहता है कि पुरस्कार से जुड़ा माप 'प्रायः' वह मापना बंद कर देता है जो वह मापता था, और जिस संख्या के लिए किसी को पुरस्कार नहीं मिलता वह ईमानदार रहती है; वह यह नहीं कहता कि पुरस्कार से जुड़ा हर माप हर दूसरे माप से कम सटीक है।",
   "conclusions",
   st=["Measures that are tied to rewards are always less accurate than measures that are not.",
       "A figure that has improved does not by itself show that the situation it describes has improved."],
   st_hi=["पुरस्कार से जुड़े माप हमेशा उन मापों से कम सटीक होते हैं जो पुरस्कार से नहीं जुड़े।",
          "सुधरा हुआ आँकड़ा अपने-आप यह नहीं दिखाता कि जिस स्थिति का वह वर्णन करता है वह सुधरी है।"],
   key=1)
RQ(p, "Assumption", "hard", "s2", ASSUME, ASSUME_HI,
   "Only 1 is assumed. The whole argument -- that a figure used as a target is distorted -- works only if those judged by it can change what they do in ways that move it: discharge earlier, steer pupils away, leave crimes unrecorded. "
   "2 is not assumed: the passage blames the use of a single figure, not the purposes behind targets, which it calls the thing people should be serving.",
   "केवल 1 पूर्वधारणा है। पूरा तर्क -- कि लक्ष्य के रूप में प्रयुक्त आँकड़ा विकृत हो जाता है -- तभी चलता है जब जिन्हें उससे आँका जाता है वे अपने काम को ऐसे बदल सकें कि आँकड़ा बदले: जल्दी छुट्टी देना, विद्यार्थियों को दूर करना, अपराध दर्ज न करना। "
   "2 पूर्वधारणा नहीं है: परिच्छेद एक ही आँकड़े के प्रयोग को दोष देता है, लक्ष्यों के पीछे के उद्देश्यों को नहीं, जिन्हें वह वह चीज़ कहता है जिसकी लोगों को सेवा करनी चाहिए।",
   "assumptions",
   st=["People who are judged by a number can change their conduct in ways that change the number.",
       "The purposes behind most targets set for public institutions are badly chosen."],
   st_hi=["जिन लोगों को किसी संख्या से आँका जाता है, वे अपने आचरण को ऐसे बदल सकते हैं जिससे संख्या बदल जाए।",
          "सार्वजनिक संस्थाओं के लिए तय अधिकांश लक्ष्यों के पीछे के उद्देश्य ग़लत चुने गए हैं।"],
   key=0)

# ------------------------------------------------------------------ P02 the paradox of thrift (3)
p = passage("p02",
  "What is prudent for a single household can be harmful when every household does it at once. A family that cuts its spending in hard times protects itself: it builds up savings against the loss of a job. But one family's spending is another's income. "
  "If all families cut back together, shops sell less, firms reduce their orders and lay off workers, and incomes fall -- so that, in the end, the families may find that they have not managed to save more at all, because their incomes have shrunk along with their spending. "
  "This is why governments in a slump are often urged to spend more just when their own revenues are falling and the instinct is to tighten the belt. The argument has limits. It applies when workers and machines lie idle for want of demand; "
  "when an economy is already running at full stretch, more spending tends to push up prices rather than output, and thrift frees resources for investment.",
  "जो एक परिवार के लिए विवेकपूर्ण है, वह हानिकारक हो सकता है जब हर परिवार उसे एक साथ करे। कठिन समय में अपना ख़र्च घटाने वाला परिवार अपनी रक्षा करता है: वह नौकरी छूटने के डर से बचत जमा करता है। पर एक परिवार का ख़र्च दूसरे की आय है। "
  "यदि सभी परिवार एक साथ ख़र्च घटाएँ, तो दुकानों की बिक्री घटती है, कंपनियाँ अपने ऑर्डर घटाती हैं और श्रमिकों को निकालती हैं, और आय गिरती है -- जिससे अंत में परिवार पा सकते हैं कि वे बिलकुल भी अधिक नहीं बचा पाए, क्योंकि उनकी आय भी उनके ख़र्च के साथ सिकुड़ गई। "
  "इसीलिए मंदी में सरकारों से प्रायः अधिक ख़र्च करने को कहा जाता है, ठीक तब जब उनका अपना राजस्व गिर रहा होता है और स्वाभाविक इच्छा कमर कसने की होती है। इस तर्क की सीमाएँ हैं। यह तब लागू होता है जब माँग के अभाव में श्रमिक और मशीनें बेकार पड़े हों; "
  "जब कोई अर्थव्यवस्था पहले से पूरी क्षमता पर चल रही हो, तो अधिक ख़र्च उत्पादन के बजाय क़ीमतें बढ़ाता है, और मितव्ययिता निवेश के लिए संसाधन मुक्त करती है।")
RQ(p, "Best Summary", "easy", "mcq", MSG, MSG_HI,
   "The passage argues that saving, wise for one household, can defeat itself when all households do it together in a slump, because spending is income for someone else; it then limits the argument to times of idle capacity. "
   "It does not say that households should never save in hard times or that saving always reduces incomes; it does not ask governments to spend whenever revenues fall, only in a slump with idle resources; and it says that at full stretch thrift helps investment, so thrift is not harmful at all times.",
   "परिच्छेद तर्क देता है कि बचत, जो एक परिवार के लिए समझदारी है, मंदी में सब परिवारों के एक साथ करने पर अपने ही उद्देश्य को विफल कर सकती है, क्योंकि ख़र्च किसी और की आय है; फिर वह इस तर्क को बेकार पड़ी क्षमता वाले समय तक सीमित करता है। "
   "वह यह नहीं कहता कि कठिन समय में परिवारों को कभी नहीं बचाना चाहिए या कि बचत हमेशा आय घटाती है; वह सरकारों से हर बार राजस्व गिरने पर ख़र्च करने को नहीं कहता, केवल बेकार संसाधनों वाली मंदी में; और वह कहता है कि पूरी क्षमता पर मितव्ययिता निवेश में सहायक है, इसलिए वह हर समय हानिकारक नहीं।",
   "message",
   opts=["Households should not save in hard times, because saving always reduces their incomes.",
         "Governments should increase their spending whenever their revenues are falling.",
         "Saving that is wise for one household can defeat itself when all save together in a slump.",
         "Thrift harms an economy at all times, whether or not its workers and machines are lying idle."],
   opts_hi=["कठिन समय में परिवारों को बचत नहीं करनी चाहिए, क्योंकि बचत हमेशा उनकी आय घटाती है।",
            "जब भी सरकारों का राजस्व गिर रहा हो, उन्हें अपना ख़र्च बढ़ाना चाहिए।",
            "एक परिवार के लिए समझदारी भरी बचत मंदी में सबके एक साथ बचाने पर अपना उद्देश्य विफल कर सकती है।",
            "मितव्ययिता अर्थव्यवस्था को हर समय हानि पहुँचाती है, चाहे उसके श्रमिक और मशीनें बेकार हों या नहीं।"],
   ans=2, pos=2)
RQ(p, "Inference", "hard", "mcq",
   "To which one of the following situations would the passage's case for more government spending apply LEAST?",
   "परिच्छेद का अधिक सरकारी ख़र्च वाला तर्क निम्नलिखित में से किस स्थिति पर सबसे कम लागू होगा?",
   "The passage limits its argument to times when workers and machines lie idle for want of demand; when an economy is already at full stretch, more spending pushes up prices rather than output. A fully used economy with fast-rising prices is exactly where the case applies least. "
   "The other three -- lost jobs and unsold stock, households cutting spending after a fall in income, firms cancelling orders as sales fall -- are the slump the passage describes, where the case applies most.",
   "परिच्छेद अपने तर्क को उस समय तक सीमित करता है जब माँग के अभाव में श्रमिक और मशीनें बेकार पड़े हों; जब अर्थव्यवस्था पहले से पूरी क्षमता पर हो, तो अधिक ख़र्च उत्पादन के बजाय क़ीमतें बढ़ाता है। तेज़ी से बढ़ती क़ीमतों वाली पूरी तरह प्रयुक्त अर्थव्यवस्था ठीक वही है जहाँ तर्क सबसे कम लागू होता है। "
   "अन्य तीन -- छूटी नौकरियाँ और बिना बिका माल, आय गिरने के बाद ख़र्च घटाते परिवार, बिक्री गिरने पर ऑर्डर रद्द करती कंपनियाँ -- वही मंदी हैं जिसका परिच्छेद वर्णन करता है, जहाँ तर्क सबसे अधिक लागू होता है।",
   "least-applicable",
   opts=["An economy in which factories are working at full capacity and prices are rising fast",
         "An economy in which many workers have lost their jobs and shops hold unsold stock",
         "An economy in which households have cut their spending sharply after a fall in incomes",
         "An economy in which firms have cancelled orders because their sales have been falling"],
   opts_hi=["ऐसी अर्थव्यवस्था जिसमें कारख़ाने पूरी क्षमता पर चल रहे हों और क़ीमतें तेज़ी से बढ़ रही हों",
            "ऐसी अर्थव्यवस्था जिसमें कई श्रमिकों की नौकरी छूट गई हो और दुकानों में माल बिना बिका पड़ा हो",
            "ऐसी अर्थव्यवस्था जिसमें आय गिरने के बाद परिवारों ने अपना ख़र्च तेज़ी से घटा दिया हो",
            "ऐसी अर्थव्यवस्था जिसमें बिक्री गिरने के कारण कंपनियों ने ऑर्डर रद्द कर दिए हों"],
   ans=0, pos=3)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Both are valid. 1: when all families cut back together their incomes shrink with their spending, so 'they may find that they have not managed to save more at all'. "
   "2: the passage says that governments are urged to spend more in a slump 'just when their own revenues are falling', which tells us that revenues tend to fall in a slump.",
   "दोनों वैध हैं। 1: जब सब परिवार एक साथ ख़र्च घटाते हैं तो उनकी आय उनके ख़र्च के साथ सिकुड़ती है, इसलिए 'वे पा सकते हैं कि वे बिलकुल भी अधिक नहीं बचा पाए'। "
   "2: परिच्छेद कहता है कि मंदी में सरकारों से अधिक ख़र्च करने को कहा जाता है 'ठीक तब जब उनका अपना राजस्व गिर रहा होता है', जिससे पता चलता है कि मंदी में राजस्व गिरने की प्रवृत्ति होती है।",
   "conclusions",
   st=["When all households cut their spending together, their total savings may fail to rise.",
       "In a slump, a government's revenues tend to fall."],
   st_hi=["जब सभी परिवार एक साथ अपना ख़र्च घटाते हैं, तो उनकी कुल बचत बढ़ने में विफल हो सकती है।",
          "मंदी में सरकार का राजस्व गिरने की प्रवृत्ति रखता है।"],
   key=2)

# ------------------------------------------------------------------ P03 the precautionary principle and gene drives (3)
p = passage("p03",
  "The precautionary principle holds that when an activity threatens serious or irreversible harm, the lack of full scientific certainty should not be a reason for postponing measures to prevent it. Its appeal is plain in the case of gene drives, "
  "which can spread an edited gene through a wild population of mosquitoes within a few generations: if the drive goes wrong, there may be no recalling it. Yet the principle cuts both ways. The same mosquitoes carry malaria, which kills hundreds of thousands of people every year, most of them children. "
  "To delay a technology that might save them, because its risks cannot yet be ruled out, is also a choice with victims -- only they are harder to see, because they are the people who would have lived. "
  "A careful use of the principle therefore asks not 'is this risky?' but 'which course carries the graver and less reversible risk?', and it counts doing nothing as one of the courses.",
  "एहतियात का सिद्धांत कहता है कि जब किसी गतिविधि से गंभीर या अपरिवर्तनीय हानि का ख़तरा हो, तो पूर्ण वैज्ञानिक निश्चितता का अभाव उसे रोकने के उपायों को टालने का कारण नहीं होना चाहिए। इसका आकर्षण जीन ड्राइव के मामले में स्पष्ट है, "
  "जो किसी संपादित जीन को कुछ ही पीढ़ियों में मच्छरों की पूरी जंगली आबादी में फैला सकती है: यदि ड्राइव ग़लत हो जाए, तो उसे वापस बुलाने का शायद कोई रास्ता न हो। फिर भी यह सिद्धांत दोनों ओर काटता है। वही मच्छर मलेरिया फैलाते हैं, जो हर वर्ष लाखों लोगों की जान लेता है, जिनमें अधिकांश बच्चे हैं। "
  "किसी ऐसी प्रौद्योगिकी को टालना जो उन्हें बचा सकती हो, केवल इसलिए कि उसके जोखिम अभी नकारे नहीं जा सकते, भी पीड़ितों वाला चुनाव है -- बस वे कम दिखते हैं, क्योंकि वे वे लोग हैं जो जीवित रहते। "
  "इसलिए सिद्धांत का सावधान प्रयोग यह नहीं पूछता कि 'क्या यह जोखिम भरा है?', बल्कि यह कि 'कौन-सा रास्ता अधिक गंभीर और कम पलटने योग्य जोखिम रखता है?', और वह कुछ न करने को भी एक रास्ता गिनता है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage accepts the principle's concern about irreversible harm but argues that delay is also a choice with victims, so the question is which course carries the graver risk, doing nothing included. "
   "It does not ask for gene drives to be released at once; it does not want the principle abandoned, only used carefully; and it does not say that irreversible technologies must never be used -- it weighs irreversibility on both sides.",
   "परिच्छेद अपरिवर्तनीय हानि के बारे में सिद्धांत की चिंता को स्वीकार करता है, पर तर्क देता है कि टालना भी पीड़ितों वाला चुनाव है, इसलिए प्रश्न यह है कि कौन-सा रास्ता, कुछ न करने सहित, अधिक गंभीर जोखिम रखता है। "
   "वह जीन ड्राइव को तुरंत छोड़ने को नहीं कहता; वह सिद्धांत को त्यागना नहीं, केवल सावधानी से प्रयोग करना चाहता है; और वह यह नहीं कहता कि अपरिवर्तनीय प्रौद्योगिकियाँ कभी प्रयोग न हों -- वह अपरिवर्तनीयता को दोनों ओर तौलता है।",
   "crux",
   opts=["Gene drives should be released at once, because malaria kills so many children every year.",
         "The precautionary principle should be abandoned, because it blocks useful new technologies.",
         "Technologies whose effects cannot be reversed should never be used, however great the need for them.",
         "Precaution must weigh the harm of not acting against the harm of acting, for delay has victims too."],
   opts_hi=["जीन ड्राइव को तुरंत छोड़ा जाना चाहिए, क्योंकि मलेरिया हर वर्ष इतने बच्चों की जान लेता है।",
            "एहतियात के सिद्धांत को त्याग देना चाहिए, क्योंकि वह उपयोगी नई प्रौद्योगिकियों को रोकता है।",
            "जिन प्रौद्योगिकियों के प्रभाव पलटे नहीं जा सकते, उनका कभी प्रयोग नहीं होना चाहिए, आवश्यकता कितनी ही बड़ी हो।",
            "एहतियात को कुछ न करने की हानि को कुछ करने की हानि के सामने तौलना चाहिए, क्योंकि टालने के भी पीड़ित होते हैं।"],
   ans=3, pos=3)
RQ(p, "Author's Tone", "medium", "mcq",
   "The author's attitude towards the precautionary principle is best described as one of:",
   "एहतियात के सिद्धांत के प्रति लेखक के दृष्टिकोण का सबसे अच्छा वर्णन है:",
   "The author grants the principle's appeal ('its appeal is plain'), then shows that it 'cuts both ways' and proposes a careful use of it that counts inaction as a course. That is acceptance with a qualification. "
   "The author neither rejects the principle nor endorses it without question, and the close argument is the opposite of indifference.",
   "लेखक सिद्धांत के आकर्षण को स्वीकार करता है ('इसका आकर्षण स्पष्ट है'), फिर दिखाता है कि वह 'दोनों ओर काटता है' और उसके ऐसे सावधान प्रयोग का प्रस्ताव करता है जो कुछ न करने को भी एक रास्ता गिनता है। यह शर्त के साथ स्वीकृति है। "
   "लेखक न सिद्धांत को अस्वीकार करता है न बिना प्रश्न किए उसका समर्थन करता है, और बारीक तर्क उदासीनता का उलटा है।",
   "tone",
   opts=["outright rejection of the principle as harmful",
         "qualified acceptance of the principle",
         "complete support for the principle exactly as it stands",
         "indifference to the principle and its uses"],
   opts_hi=["सिद्धांत को हानिकारक मानकर पूरी तरह अस्वीकार करने का",
            "सिद्धांत को शर्त के साथ स्वीकार करने का",
            "सिद्धांत का, जैसा वह है ठीक वैसा ही, पूर्ण समर्थन करने का",
            "सिद्धांत और उसके प्रयोगों के प्रति उदासीनता का"],
   ans=1, pos=1)
RQ(p, "Assumption", "hard", "s2", ASSUME, ASSUME_HI,
   "Only 2 is assumed. The passage asks which course carries 'the graver and less reversible risk', counting inaction as a course: that question can be answered only if the risks of releasing and of not releasing can be set against each other. "
   "1 is not assumed: the passage says nothing about what most scientists think, and its case rests on weighing harms, not on expert opinion.",
   "केवल 2 पूर्वधारणा है। परिच्छेद पूछता है कि कौन-सा रास्ता 'अधिक गंभीर और कम पलटने योग्य जोखिम' रखता है, कुछ न करने को भी एक रास्ता गिनते हुए: इस प्रश्न का उत्तर तभी दिया जा सकता है जब छोड़ने और न छोड़ने के जोखिमों को एक-दूसरे के सामने रखा जा सके। "
   "1 पूर्वधारणा नहीं है: परिच्छेद इस बारे में कुछ नहीं कहता कि अधिकांश वैज्ञानिक क्या सोचते हैं, और उसका तर्क हानियों को तौलने पर टिका है, विशेषज्ञों की राय पर नहीं।",
   "assumptions",
   st=["Most scientists support the release of gene drives against malaria.",
       "The risks of releasing a gene drive and of not releasing it can be compared with each other."],
   st_hi=["अधिकांश वैज्ञानिक मलेरिया के विरुद्ध जीन ड्राइव छोड़ने का समर्थन करते हैं।",
          "जीन ड्राइव छोड़ने और न छोड़ने के जोखिमों की एक-दूसरे से तुलना की जा सकती है।"],
   key=1)

# ------------------------------------------------------------------ P04 deposit insurance and the risks banks take (2)
p = passage("p04",
  "Deposit insurance protects small savers: if a bank fails, their deposits up to a limit are repaid. It also prevents panics, since depositors who know they are safe have no reason to rush to withdraw their money at the first rumour. "
  "But protection changes behaviour. Depositors who are insured have little reason to ask how carefully their bank lends, and a bank that knows its depositors will not run may be tempted to take bigger risks in search of higher returns. "
  "The cost of failure then falls on the insurance fund, and in the end on the public. This is why deposit insurance is nearly always paired with close supervision of banks and with rules on how much of their own capital the owners must put at risk: "
  "the owners, not the depositors, are expected to do the worrying.",
  "जमा बीमा छोटे बचतकर्ताओं की रक्षा करता है: यदि कोई बैंक विफल हो जाए, तो एक सीमा तक उनकी जमा राशि लौटा दी जाती है। यह घबराहट को भी रोकता है, क्योंकि जो जमाकर्ता जानते हैं कि वे सुरक्षित हैं उनके पास पहली अफ़वाह पर अपना पैसा निकालने दौड़ पड़ने का कोई कारण नहीं होता। "
  "पर सुरक्षा व्यवहार बदल देती है। बीमित जमाकर्ताओं के पास यह पूछने का कम कारण होता है कि उनका बैंक कितनी सावधानी से ऋण देता है, और जो बैंक जानता है कि उसके जमाकर्ता पैसा निकालने नहीं दौड़ेंगे, वह अधिक प्रतिफल की खोज में बड़े जोखिम लेने को ललचा सकता है। "
  "तब विफलता की लागत बीमा कोष पर, और अंततः जनता पर पड़ती है। इसीलिए जमा बीमा को लगभग हमेशा बैंकों की कड़ी निगरानी और इन नियमों के साथ जोड़ा जाता है कि मालिकों को अपनी कितनी पूँजी जोखिम में डालनी होगी: "
  "चिंता करने का काम जमाकर्ताओं से नहीं, मालिकों से अपेक्षित है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage first lists what deposit insurance does well, then shows that it removes depositors' reason to watch their banks and tempts banks to take risks, which is why it comes with supervision and capital rules. The crux is that the insurance creates a need for other checks. "
   "It does not ask for deposit insurance to be withdrawn; it says nothing about large uninsured depositors causing panics; and it expects the owners, not small savers, to do the checking.",
   "परिच्छेद पहले बताता है कि जमा बीमा क्या अच्छा करता है, फिर दिखाता है कि वह जमाकर्ताओं से अपने बैंक पर नज़र रखने का कारण छीन लेता है और बैंकों को जोखिम लेने के लिए ललचाता है, इसीलिए वह निगरानी और पूँजी के नियमों के साथ आता है। सार यह है कि बीमा दूसरी जाँचों की आवश्यकता पैदा करता है। "
   "वह जमा बीमा को हटाने को नहीं कहता; वह बड़े बिना बीमे वाले जमाकर्ताओं के घबराहट फैलाने के बारे में कुछ नहीं कहता; और वह जाँच का काम छोटे बचतकर्ताओं से नहीं, मालिकों से अपेक्षित करता है।",
   "crux",
   opts=["Deposit insurance should be withdrawn, because it encourages banks to take bigger risks.",
         "Panics in banks are caused mainly by large depositors whose money is not insured.",
         "By removing depositors' reason to watch their banks, insurance creates a need for other checks.",
         "Small savers should find out how carefully a bank lends its money before they deposit money in it."],
   opts_hi=["जमा बीमा हटा देना चाहिए, क्योंकि वह बैंकों को बड़े जोखिम लेने के लिए प्रोत्साहित करता है।",
            "बैंकों में घबराहट मुख्यतः उन बड़े जमाकर्ताओं से फैलती है जिनका पैसा बीमित नहीं है।",
            "जमाकर्ताओं से बैंक पर नज़र रखने का कारण छीनकर बीमा दूसरी जाँचों की आवश्यकता पैदा करता है।",
            "छोटे बचतकर्ताओं को पैसा जमा करने से पहले पता करना चाहिए कि बैंक कितनी सावधानी से ऋण देता है।"],
   ans=2, pos=2)
RQ(p, "Assumption", "hard", "s2", ASSUME, ASSUME_HI,
   "Both are assumed. 1: the passage says that insured depositors 'have little reason to ask how carefully their bank lends'; the point has force only if depositors without that protection do pay some such attention. "
   "2: requiring owners to put their own capital at risk is offered as the answer, so that 'the owners ... are expected to do the worrying'; this works only if owners with more at stake are more careful.",
   "दोनों पूर्वधारणाएँ हैं। 1: परिच्छेद कहता है कि बीमित जमाकर्ताओं के पास 'यह पूछने का कम कारण होता है कि उनका बैंक कितनी सावधानी से ऋण देता है'; इस बात में बल तभी है जब बिना उस सुरक्षा वाले जमाकर्ता ऐसा कुछ ध्यान देते हों। "
   "2: मालिकों से अपनी पूँजी जोखिम में डलवाना समाधान के रूप में दिया गया है, ताकि 'चिंता करने का काम ... मालिकों से अपेक्षित' हो; यह तभी काम करता है जब अधिक दाँव वाले मालिक अधिक सावधान हों।",
   "assumptions",
   st=["Depositors who are not insured pay some attention to how safely their bank is run.",
       "Owners who have more of their own capital at risk in a bank will run it more carefully."],
   st_hi=["जो जमाकर्ता बीमित नहीं हैं, वे इस पर कुछ ध्यान देते हैं कि उनका बैंक कितनी सुरक्षा से चलाया जाता है।",
          "जिन मालिकों की अपनी अधिक पूँजी बैंक में जोखिम पर है, वे उसे अधिक सावधानी से चलाएँगे।"],
   key=2)

# ------------------------------------------------------------------ P05 village commons and the rules that keep them (3)
p = passage("p05",
  "It is often said that a resource owned by everyone is cared for by no one: each herder gains the whole benefit of adding one more animal to a common pasture but bears only a small share of the damage, so the pasture is overgrazed. "
  "Yet many villages have managed common pastures, forests and tanks for generations without ruining them. Studies of such cases find that success rarely rests on goodwill alone. It rests on clear boundaries, so that outsiders can be kept out; "
  "on rules that the users themselves have a hand in making; on someone who watches whether the rules are kept; and on penalties that start small and grow for repeated offences. "
  "Where these conditions wear away -- when the State takes over the land but cannot police it, or when a new road brings outside buyers for whatever the commons produce -- the old arrangements can collapse quickly. "
  "The tragedy of the commons, in other words, is not a law of nature but a description of what happens when the institutions that govern a commons are missing.",
  "प्रायः कहा जाता है कि जिस संसाधन का स्वामी हर कोई है उसकी देखभाल कोई नहीं करता: हर चरवाहे को साझा चरागाह में एक और पशु जोड़ने का पूरा लाभ मिलता है पर हानि का केवल छोटा हिस्सा उठाना पड़ता है, इसलिए चरागाह में अति-चराई हो जाती है। "
  "फिर भी अनेक गाँवों ने साझा चरागाहों, जंगलों और तालाबों को पीढ़ियों तक बिना नष्ट किए सँभाला है। ऐसे मामलों के अध्ययन पाते हैं कि सफलता शायद ही केवल सद्भावना पर टिकी होती है। वह टिकी होती है स्पष्ट सीमाओं पर, ताकि बाहरी लोगों को बाहर रखा जा सके; "
  "ऐसे नियमों पर जिन्हें बनाने में स्वयं उपयोगकर्ताओं का हाथ हो; ऐसे व्यक्ति पर जो देखे कि नियमों का पालन हो रहा है या नहीं; और ऐसे दंडों पर जो छोटे से शुरू हों और बार-बार के अपराध पर बढ़ें। "
  "जहाँ ये शर्तें घिस जाती हैं -- जब राज्य भूमि अपने हाथ में ले लेता है पर उसकी निगरानी नहीं कर पाता, या जब कोई नई सड़क साझा संसाधनों की उपज के लिए बाहरी ख़रीदार ले आती है -- वहाँ पुरानी व्यवस्थाएँ जल्दी ढह सकती हैं। "
  "दूसरे शब्दों में, साझा संसाधनों की त्रासदी प्रकृति का नियम नहीं, बल्कि इसका वर्णन है कि जब किसी साझा संसाधन को चलाने वाली संस्थाएँ न हों तब क्या होता है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage states the claim that common resources are bound to be ruined, then answers it with villages that kept their commons for generations, and closes: the tragedy is 'not a law of nature' but what happens when governing institutions are missing. "
   "It never proposes private ownership; it says that success 'rarely rests on goodwill alone', so care for one another is not the explanation; and it gives the State's takeover without policing as a cause of collapse, not a cure.",
   "परिच्छेद यह दावा रखता है कि साझा संसाधनों का नष्ट होना तय है, फिर उसका उत्तर उन गाँवों से देता है जिन्होंने पीढ़ियों तक अपने साझा संसाधन सँभाले, और अंत में कहता है: त्रासदी 'प्रकृति का नियम नहीं', बल्कि वह है जो चलाने वाली संस्थाओं के न होने पर होता है। "
   "वह कहीं निजी स्वामित्व का प्रस्ताव नहीं करता; वह कहता है कि सफलता 'शायद ही केवल सद्भावना पर टिकी होती है', इसलिए आपसी परवाह व्याख्या नहीं है; और वह राज्य के बिना निगरानी के भूमि लेने को ढहने का कारण बताता है, उपचार नहीं।",
   "crux",
   opts=["Common lands should be handed to private owners, who alone can prevent overgrazing.",
         "Villages manage their commons well because their members care for one another.",
         "A commons is ruined not inevitably but when the rules and institutions governing it break down.",
         "The State should take over common pastures and forests in order to protect them from ruin by overuse."],
   opts_hi=["साझा भूमि निजी स्वामियों को सौंप देनी चाहिए, क्योंकि केवल वही अति-चराई रोक सकते हैं।",
            "गाँव अपने साझा संसाधनों को अच्छी तरह इसलिए सँभालते हैं कि उनके सदस्य एक-दूसरे की परवाह करते हैं।",
            "साझा संसाधन अनिवार्य रूप से नहीं, बल्कि तब नष्ट होता है जब उसे चलाने वाले नियम और संस्थाएँ टूट जाते हैं।",
            "राज्य को साझा चरागाहों और जंगलों को अति-उपयोग से नष्ट होने से बचाने के लिए उन्हें अपने हाथ में ले लेना चाहिए।"],
   ans=2, pos=2)
RQ(p, "Inference", "hard", "mcq",
   "On the basis of the passage, which one of the following would be most likely to weaken a village's management of its common forest?",
   "परिच्छेद के आधार पर, निम्नलिखित में से कौन-सा किसी गाँव के साझा जंगल के प्रबंधन को कमज़ोर करने की सबसे अधिक संभावना रखता है?",
   "The passage names a new road that brings outside buyers for what the commons produce as one way in which the old arrangements collapse: outsiders with ready cash weaken boundaries and the users' control. "
   "A committee elected by the villagers to revise the rules, fines that rise for a second offence, and a village-paid watchman on the boundary are the very conditions -- rules made by users, graduated penalties, monitoring, boundaries -- that the passage says sustain a commons.",
   "परिच्छेद साझा संसाधनों की उपज के लिए बाहरी ख़रीदार लाने वाली नई सड़क को उन तरीक़ों में गिनाता है जिनसे पुरानी व्यवस्थाएँ ढहती हैं: नक़द लिए बाहरी लोग सीमाओं और उपयोगकर्ताओं के नियंत्रण को कमज़ोर करते हैं। "
   "ग्रामीणों द्वारा चुनी गई नियम संशोधित करने वाली समिति, दूसरे अपराध पर बढ़ता जुर्माना, और सीमा पर गाँव द्वारा वेतन पाने वाला चौकीदार ठीक वही शर्तें हैं -- उपयोगकर्ताओं के बनाए नियम, क्रमिक दंड, निगरानी, सीमाएँ -- जिन्हें परिच्छेद साझा संसाधन को टिकाने वाली बताता है।",
   "what-weakens",
   opts=["A new highway lets traders from the cities buy the forest's timber and fruit in bulk.",
         "The villagers elect a committee that revises the rules on gathering firewood.",
         "The fine for cutting a green tree is raised for anyone caught doing so a second time.",
         "A watchman paid by the village begins to patrol the boundary of the forest."],
   opts_hi=["एक नया राजमार्ग शहरों के व्यापारियों को जंगल की लकड़ी और फल थोक में ख़रीदने देता है।",
            "ग्रामीण एक समिति चुनते हैं जो जलाऊ लकड़ी इकट्ठा करने के नियम संशोधित करती है।",
            "हरा पेड़ काटने का जुर्माना दूसरी बार पकड़े जाने वाले किसी भी व्यक्ति के लिए बढ़ा दिया जाता है।",
            "गाँव द्वारा वेतन पाने वाला एक चौकीदार जंगल की सीमा पर गश्त करने लगता है।"],
   ans=0, pos=3)
RQ(p, "Specific Detail", "medium", "mcq",
   "Which one of the following is NOT mentioned in the passage as a condition on which the successful management of a commons rests?",
   "निम्नलिखित में से किसे परिच्छेद में उस शर्त के रूप में नहीं बताया गया है जिस पर किसी साझा संसाधन का सफल प्रबंधन टिका है?",
   "The passage lists clear boundaries, rules that the users help to make, someone who watches whether the rules are kept, and penalties that start small and grow. Ownership by a government agency is not among them -- the passage mentions the State's taking over the land only as a way in which arrangements collapse.",
   "परिच्छेद स्पष्ट सीमाएँ, उपयोगकर्ताओं की सहायता से बने नियम, नियमों के पालन पर नज़र रखने वाला व्यक्ति, और छोटे से शुरू होकर बढ़ने वाले दंड गिनाता है। किसी सरकारी एजेंसी का स्वामित्व इनमें नहीं है -- परिच्छेद राज्य के भूमि अपने हाथ में लेने का उल्लेख केवल उस तरीक़े के रूप में करता है जिससे व्यवस्थाएँ ढहती हैं।",
   "not-mentioned",
   opts=["A government agency that owns the land and enforces the rules",
         "Clear boundaries that allow outsiders to be kept out of the commons",
         "Rules that the users themselves have a hand in making",
         "Penalties that start small and grow for repeated offences"],
   opts_hi=["एक सरकारी एजेंसी जो भूमि की स्वामी हो और नियम लागू करे",
            "स्पष्ट सीमाएँ जिनसे बाहरी लोगों को साझा संसाधन से बाहर रखा जा सके",
            "ऐसे नियम जिन्हें बनाने में स्वयं उपयोगकर्ताओं का हाथ हो",
            "ऐसे दंड जो छोटे से शुरू हों और बार-बार के अपराध पर बढ़ें"],
   ans=0, pos=0)

# ------------------------------------------------------------------ P06 findings that fail to repeat (3)
p = passage("p06",
  "A single striking result in science is a beginning, not an ending. Before it can be trusted, other researchers must be able to repeat the experiment and find the same effect. In several fields, from psychology to cancer biology, "
  "organised attempts to repeat well-known studies have succeeded far less often than expected. The reasons are rarely fraud. More often they lie in small samples, in the freedom to choose among many ways of analysing the same data until one gives an impressive answer, "
  "and in journals that prefer exciting positive findings to careful negative ones. Each choice may look innocent, but together they fill the literature with effects that are larger and surer than the truth. "
  "The remedies are known: registering a study's plan before the data are collected, sharing data and code, and rewarding replications as real contributions. They cost little except a certain kind of speed -- the speed of being first rather than of being right.",
  "विज्ञान में एक अकेला चौंकाने वाला परिणाम शुरुआत है, अंत नहीं। उस पर भरोसा करने से पहले दूसरे शोधकर्ताओं को प्रयोग दोहराकर वही प्रभाव पाने में समर्थ होना चाहिए। मनोविज्ञान से लेकर कैंसर जीवविज्ञान तक कई क्षेत्रों में, "
  "प्रसिद्ध अध्ययनों को दोहराने के संगठित प्रयास अपेक्षा से कहीं कम सफल हुए हैं। कारण शायद ही धोखाधड़ी होते हैं। प्रायः वे छोटे नमूनों में, एक ही आँकड़ों के विश्लेषण के अनेक तरीक़ों में से तब तक चुनते रहने की छूट में जब तक कोई प्रभावशाली उत्तर न दे दे, "
  "और उन पत्रिकाओं में होते हैं जो सावधान नकारात्मक निष्कर्षों की तुलना में रोमांचक सकारात्मक निष्कर्ष छापना पसंद करती हैं। हर चुनाव निर्दोष लग सकता है, पर मिलकर वे साहित्य को ऐसे प्रभावों से भर देते हैं जो सच से बड़े और अधिक निश्चित दिखते हैं। "
  "उपाय ज्ञात हैं: आँकड़े इकट्ठा करने से पहले अध्ययन की योजना दर्ज करना, आँकड़े और कोड साझा करना, और दोहराव के अध्ययनों को वास्तविक योगदान मानकर पुरस्कृत करना। इनकी लागत एक ख़ास तरह की गति के सिवा बहुत कम है -- सही होने की नहीं, पहले होने की गति।")
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Only 1 is valid. Registering the plan before the data are collected fixes the analysis in advance, which removes 'the freedom to choose among many ways of analysing the same data until one gives an impressive answer'. "
   "2 overreaches: small samples are one reason among several; a large study can still fail through a flexible analysis or a journal's taste for exciting results, so large samples do not guarantee that a study will repeat.",
   "केवल 1 वैध है। आँकड़े इकट्ठा करने से पहले योजना दर्ज करना विश्लेषण को पहले से तय कर देता है, जिससे 'एक ही आँकड़ों के विश्लेषण के अनेक तरीक़ों में से तब तक चुनते रहने की छूट जब तक कोई प्रभावशाली उत्तर न दे दे' समाप्त होती है। "
   "2 बहुत आगे जाता है: छोटे नमूने कई कारणों में से एक हैं; बड़ा अध्ययन भी लचीले विश्लेषण या रोमांचक परिणामों के प्रति पत्रिका की पसंद से विफल हो सकता है, इसलिए बड़े नमूने यह गारंटी नहीं देते कि अध्ययन दोहराया जा सकेगा।",
   "conclusions",
   st=["A study whose plan is registered before its data are collected leaves less room for choosing the most impressive analysis.",
       "Studies with large samples can always be repeated successfully."],
   st_hi=["जिस अध्ययन की योजना उसके आँकड़े इकट्ठा करने से पहले दर्ज हो, उसमें सबसे प्रभावशाली विश्लेषण चुनने की गुंजाइश कम रहती है।",
          "बड़े नमूनों वाले अध्ययन हमेशा सफलतापूर्वक दोहराए जा सकते हैं।"],
   key=0)
RQ(p, "Best Summary", "medium", "mcq", MSG, MSG_HI,
   "The passage says that many well-known findings fail to repeat, puts the cause in ordinary practices rather than fraud, and names cheap remedies. The summary keeps all three. "
   "It says that the reasons are 'rarely fraud'; it does not compare psychology and cancer biology with other sciences; and it asks journals to value negative findings and replications, not to stop publishing positive ones.",
   "परिच्छेद कहता है कि अनेक प्रसिद्ध निष्कर्ष दोहराए नहीं जा पाते, कारण धोखाधड़ी में नहीं बल्कि सामान्य तौर-तरीक़ों में बताता है, और सस्ते उपाय गिनाता है। सारांश तीनों को रखता है। "
   "वह कहता है कि कारण 'शायद ही धोखाधड़ी' होते हैं; वह मनोविज्ञान और कैंसर जीवविज्ञान की तुलना दूसरे विज्ञानों से नहीं करता; और वह पत्रिकाओं से नकारात्मक निष्कर्षों और दोहराव को महत्व देने को कहता है, सकारात्मक निष्कर्ष छापना बंद करने को नहीं।",
   "message",
   opts=["Most scientific findings that cannot be repeated are the result of deliberate fraud by researchers.",
         "Psychology and cancer biology are less reliable than the other branches of science.",
         "Journals should stop publishing positive findings until they have been repeated.",
         "Many findings fail to hold up because of everyday research habits that known reforms can fix."],
   opts_hi=["जो वैज्ञानिक निष्कर्ष दोहराए नहीं जा सकते, उनमें से अधिकांश जानबूझकर की गई धोखाधड़ी का परिणाम हैं।",
            "मनोविज्ञान और कैंसर जीवविज्ञान विज्ञान की दूसरी शाखाओं से कम विश्वसनीय हैं।",
            "पत्रिकाओं को सकारात्मक निष्कर्ष तब तक छापना बंद कर देना चाहिए जब तक वे दोहराए न जाएँ।",
            "अनेक निष्कर्ष शोध की रोज़ की आदतों के कारण टिक नहीं पाते, जिन्हें ज्ञात सुधार ठीक कर सकते हैं।"],
   ans=3, pos=3)
RQ(p, "Assumption", "hard", "s2", ASSUME, ASSUME_HI,
   "Only 1 is assumed. Among the remedies is 'rewarding replications as real contributions', and the passage blames journals' preferences for the flood of inflated effects; both make sense only if researchers respond to what is rewarded. "
   "2 is not assumed: the passage says that each choice 'may look innocent', and it nowhere suggests that those who use small samples are careless people.",
   "केवल 1 पूर्वधारणा है। उपायों में 'दोहराव के अध्ययनों को वास्तविक योगदान मानकर पुरस्कृत करना' है, और परिच्छेद बढ़ा-चढ़ाकर दिखे प्रभावों की बाढ़ के लिए पत्रिकाओं की पसंद को दोष देता है; दोनों तभी सार्थक हैं जब शोधकर्ता उस पर प्रतिक्रिया करें जो पुरस्कृत होता है। "
   "2 पूर्वधारणा नहीं है: परिच्छेद कहता है कि हर चुनाव 'निर्दोष लग सकता है', और कहीं नहीं सुझाता कि छोटे नमूने लेने वाले लापरवाह लोग हैं।",
   "assumptions",
   st=["Researchers respond to the rewards that journals and institutions offer for different kinds of work.",
       "Studies with small samples are usually designed by careless researchers."],
   st_hi=["शोधकर्ता उन पुरस्कारों पर प्रतिक्रिया करते हैं जो पत्रिकाएँ और संस्थाएँ अलग-अलग तरह के काम के लिए देती हैं।",
          "छोटे नमूनों वाले अध्ययन प्रायः लापरवाह शोधकर्ताओं द्वारा बनाए जाते हैं।"],
   key=0)

# ------------------------------------------------------------------ P07 carbon offsets that change nothing (3)
p = passage("p07",
  "A company that cannot yet cut its own emissions may buy carbon offsets instead: it pays for a project elsewhere -- a forest protected, cleaner cookstoves handed out -- that is said to keep an equal amount of carbon dioxide out of the air. "
  "The idea is sound only if the reduction would not have happened anyway. If the forest was never under threat, paying to 'protect' it changes nothing, and the company's claim to have balanced its emissions is false, however honest its intentions. "
  "The reduction must also last: carbon stored in trees returns to the air if they burn a decade later, while the emissions it was meant to cancel stay in the atmosphere for centuries. "
  "Checking all this requires knowing what would have happened without the project, which can never be observed, only estimated. That is why offsets are best treated as a supplement to cutting one's own emissions, not a substitute for it.",
  "जो कंपनी अभी अपना उत्सर्जन नहीं घटा सकती, वह इसके बजाय कार्बन ऑफ़सेट ख़रीद सकती है: वह कहीं और की किसी परियोजना का भुगतान करती है -- किसी जंगल का संरक्षण, स्वच्छ चूल्हों का वितरण -- जिसके बारे में कहा जाता है कि वह उतनी ही कार्बन डाइऑक्साइड को हवा में जाने से रोकती है। "
  "यह विचार तभी ठीक है जब वह कमी अन्यथा न होती। यदि जंगल को कभी ख़तरा था ही नहीं, तो उसके 'संरक्षण' के लिए भुगतान कुछ नहीं बदलता, और कंपनी का अपना उत्सर्जन संतुलित करने का दावा झूठा है, उसकी नीयत कितनी ही ईमानदार हो। "
  "कमी को टिकना भी चाहिए: पेड़ों में संचित कार्बन हवा में लौट आता है यदि वे एक दशक बाद जल जाएँ, जबकि जिन उत्सर्जनों को उसे काटना था वे सदियों तक वायुमंडल में रहते हैं। "
  "यह सब जाँचने के लिए यह जानना ज़रूरी है कि परियोजना के बिना क्या होता, जिसे कभी देखा नहीं जा सकता, केवल अनुमान लगाया जा सकता है। इसीलिए ऑफ़सेट को अपना उत्सर्जन घटाने का पूरक मानना सबसे अच्छा है, विकल्प नहीं।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage sets two tests for an offset -- the reduction must be one that would not have happened anyway, and it must last -- and adds that the first can only be estimated, which is why offsets should supplement, not replace, a company's own cuts. "
   "It allows that a company may be honest ('however honest its intentions'); it does not call forest protection a poor way of storing carbon in general, only one whose storage may not last; and it does not ask for offsets to be banned.",
   "परिच्छेद ऑफ़सेट के लिए दो कसौटियाँ रखता है -- कमी ऐसी हो जो अन्यथा न होती, और वह टिके -- और जोड़ता है कि पहली का केवल अनुमान लगाया जा सकता है, इसीलिए ऑफ़सेट को कंपनी की अपनी कटौती का पूरक होना चाहिए, विकल्प नहीं। "
   "वह मानता है कि कंपनी ईमानदार हो सकती है ('उसकी नीयत कितनी ही ईमानदार हो'); वह जंगल संरक्षण को सामान्यतः कार्बन संचय का ख़राब तरीक़ा नहीं कहता, केवल ऐसा जिसका संचय शायद न टिके; और वह ऑफ़सेट पर प्रतिबंध नहीं माँगता।",
   "crux",
   opts=["Companies that buy carbon offsets are usually dishonest about the real level of their emissions.",
         "An offset counts only if its cut is lasting and would not otherwise occur, which is hard to check.",
         "Protecting forests is a poor way of keeping carbon dioxide out of the atmosphere.",
         "Offsets should be banned altogether, since what would have happened without them can never be observed."],
   opts_hi=["कार्बन ऑफ़सेट ख़रीदने वाली कंपनियाँ प्रायः अपने वास्तविक उत्सर्जन के बारे में बेईमान होती हैं।",
            "ऑफ़सेट तभी गिना जाता है जब वह ऐसी टिकाऊ कमी लाए जो अन्यथा न होती, और इसे जाँचना कठिन है।",
            "जंगलों का संरक्षण कार्बन डाइऑक्साइड को वायुमंडल से बाहर रखने का एक ख़राब तरीक़ा है।",
            "ऑफ़सेट पर प्रतिबंध लगना चाहिए, क्योंकि उनके बिना क्या होता यह देखा नहीं जा सकता।"],
   ans=1, pos=1)
RQ(p, "Inference", "hard", "mcq",
   "On the basis of the passage, which one of the following offsets is most open to doubt?",
   "परिच्छेद के आधार पर, निम्नलिखित में से कौन-सा ऑफ़सेट सबसे अधिक संदेह के घेरे में है?",
   "The passage's first test is that the reduction would not have happened anyway; paying to protect a forest that nobody had any plan or reason to cut fails it outright, since nothing changes. "
   "Cookstoves in villages that would otherwise burn more wood, stopping a planned clearing, and capturing methane that was escaping all change what would otherwise have happened, so they pass that test (whether their cuts last is a separate question).",
   "परिच्छेद की पहली कसौटी यह है कि कमी अन्यथा न होती; ऐसे जंगल के संरक्षण का भुगतान जिसे काटने की किसी की न योजना थी न कारण, इस कसौटी पर सीधे विफल होता है, क्योंकि कुछ नहीं बदलता। "
   "उन गाँवों में चूल्हे जो अन्यथा अधिक लकड़ी जलाते, नियोजित कटाई रोकना, और बाहर निकल रही मीथेन को पकड़ना, सभी वह बदलते हैं जो अन्यथा होता, इसलिए वे इस कसौटी पर खरे उतरते हैं (उनकी कमी टिकेगी या नहीं, यह अलग प्रश्न है)।",
   "most-doubtful",
   opts=["Paying for efficient cookstoves in villages that would otherwise have burned more wood",
         "Paying to stop a clearing of forest that was planned for a new plantation",
         "Paying to protect a remote forest that no one had any plan or reason to cut",
         "Paying to capture methane at a landfill that was releasing it into the air"],
   opts_hi=["उन गाँवों में कुशल चूल्हों के लिए भुगतान जो अन्यथा कहीं अधिक लकड़ी जलाते रहते",
            "किसी नए बाग़ान के लिए नियोजित जंगल की कटाई रोकने के लिए भुगतान",
            "ऐसे दूरस्थ जंगल के संरक्षण का भुगतान जिसे काटने की किसी की न योजना थी न कारण",
            "उस कचरा-भराव स्थल पर मीथेन पकड़ने के लिए भुगतान जो उसे लगातार हवा में छोड़ रहा था"],
   ans=2, pos=3)
RQ(p, "Specific Detail", "easy", "mcq",
   "According to the passage, why can carbon stored in trees make an unreliable offset?",
   "परिच्छेद के अनुसार, पेड़ों में संचित कार्बन एक अविश्वसनीय ऑफ़सेट क्यों हो सकता है?",
   "The passage says that carbon stored in trees returns to the air if they burn a decade later, while the emissions it was meant to cancel stay in the atmosphere for centuries: the storage may not last as long as the harm. "
   "It says nothing about trees absorbing too slowly, about measuring forests from the air, or about trees giving out more carbon dioxide at night than they take in by day.",
   "परिच्छेद कहता है कि पेड़ों में संचित कार्बन हवा में लौट आता है यदि वे एक दशक बाद जल जाएँ, जबकि जिन उत्सर्जनों को उसे काटना था वे सदियों तक वायुमंडल में रहते हैं: संचय शायद उतना न टिके जितनी हानि टिकती है। "
   "वह पेड़ों के बहुत धीरे सोखने, जंगलों को हवा से मापने, या पेड़ों के दिन में सोखने से अधिक रात में कार्बन डाइऑक्साइड छोड़ने के बारे में कुछ नहीं कहता।",
   "why-trees",
   opts=["Trees take in carbon dioxide far too slowly to make any real difference to the climate.",
         "Forests are difficult to measure accurately from the air or from satellites.",
         "The trees may burn and release it, while the emissions it offsets last for centuries.",
         "Trees give out more carbon dioxide at night than they take in during the day."],
   opts_hi=["पेड़ कार्बन डाइऑक्साइड इतनी धीरे सोखते हैं कि जलवायु पर कोई अंतर नहीं पड़ता।",
            "जंगलों को हवा से या उपग्रहों से सटीक रूप से मापना कठिन है।",
            "पेड़ जलकर उसे छोड़ सकते हैं, जबकि जिन उत्सर्जनों की वह भरपाई करता है वे सदियों तक रहते हैं।",
            "पेड़ दिन में जितनी कार्बन डाइऑक्साइड सोखते हैं, उससे कहीं अधिक वे रात में वापस छोड़ देते हैं।"],
   ans=2, pos=2)

# ------------------------------------------------------------------ P08 transfers from the Centre to poorer States (2)
p = passage("p08",
  "In a federation the richer States usually raise far more revenue per person than the poorer ones, while the cost of running a school or a clinic is not much lower in a poor State. If every State had to live on its own revenue, a child's chances would depend heavily on the State in which the child happened to be born. "
  "Transfers from the Centre, shared out by a formula, are meant to narrow these gaps, so that every State can provide broadly comparable services at broadly comparable rates of tax. "
  "Such transfers are often resented by the States that contribute more than they receive, which see their own effort subsidising others. The resentment is understandable but rests partly on a misreading: "
  "the taxes that fund the transfers are paid by citizens and firms, not by States as such, and the market and currency shared across the country help the richer regions earn much of what they earn.",
  "किसी संघ में अमीर राज्य प्रायः ग़रीब राज्यों की तुलना में प्रति व्यक्ति कहीं अधिक राजस्व जुटाते हैं, जबकि किसी ग़रीब राज्य में विद्यालय या चिकित्सालय चलाने की लागत बहुत कम नहीं होती। यदि हर राज्य को अपने ही राजस्व पर चलना पड़े, तो किसी बच्चे के अवसर बहुत हद तक इस पर निर्भर करेंगे कि वह संयोग से किस राज्य में जन्मा। "
  "केंद्र से एक सूत्र के अनुसार बाँटे जाने वाले हस्तांतरण इन अंतरों को घटाने के लिए हैं, ताकि हर राज्य मोटे तौर पर तुलनीय कर दरों पर मोटे तौर पर तुलनीय सेवाएँ दे सके। "
  "जो राज्य पाने से अधिक योगदान देते हैं वे प्रायः ऐसे हस्तांतरणों से नाराज़ रहते हैं, क्योंकि उन्हें लगता है कि उनका अपना प्रयास दूसरों को सहायता दे रहा है। यह नाराज़गी समझ में आती है, पर आंशिक रूप से एक ग़लत समझ पर टिकी है: "
  "हस्तांतरणों के लिए धन देने वाले कर नागरिक और कंपनियाँ चुकाते हैं, राज्य स्वयं नहीं, और पूरे देश में साझा बाज़ार और मुद्रा अमीर क्षेत्रों को उनकी कमाई का बड़ा भाग कमाने में सहायता करते हैं।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage explains why transfers exist -- so that every State can offer broadly comparable services at comparable tax rates -- and then argues that the richer States' resentment partly misreads who pays and how their wealth arises. "
   "It does not want richer States to keep all their revenue; it says that the cost of a school is 'not much lower' in a poor State, not that it is the same everywhere; and it does not say that poorer States tax their people less heavily.",
   "परिच्छेद बताता है कि हस्तांतरण क्यों हैं -- ताकि हर राज्य तुलनीय कर दरों पर मोटे तौर पर तुलनीय सेवाएँ दे सके -- और फिर तर्क देता है कि अमीर राज्यों की नाराज़गी आंशिक रूप से यह ग़लत समझती है कि भुगतान कौन करता है और उनकी समृद्धि कैसे आती है। "
   "वह नहीं चाहता कि अमीर राज्य अपना सारा राजस्व रखें; वह कहता है कि ग़रीब राज्य में विद्यालय की लागत 'बहुत कम नहीं' होती, यह नहीं कि वह हर जगह समान है; और वह यह नहीं कहता कि ग़रीब राज्य अपने लोगों पर कम कर लगाते हैं।",
   "crux",
   opts=["Richer States should be allowed to keep all of the revenue that they raise.",
         "Transfers aim at comparable services in all States, and richer States' resentment is partly misplaced.",
         "The cost of running schools and clinics is exactly the same in every State of a federation, rich or poor.",
         "Poorer States raise less revenue because they tax their citizens much less heavily."],
   opts_hi=["अमीर राज्यों को अपना जुटाया हुआ सारा राजस्व रखने दिया जाना चाहिए।",
            "हस्तांतरणों का उद्देश्य सब राज्यों में तुलनीय सेवाएँ हैं; अमीर राज्यों की नाराज़गी आंशिक रूप से अनुचित है।",
            "संघ के हर राज्य में, चाहे वह अमीर हो या ग़रीब, विद्यालय और चिकित्सालय चलाने की लागत बिलकुल समान है।",
            "ग़रीब राज्य कम राजस्व मुख्यतः इसलिए जुटाते हैं कि वे अपने नागरिकों पर अमीर राज्यों से बहुत कम कर लगाते हैं।"],
   ans=1, pos=1)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Only 1 is valid: the passage says that if every State lived on its own revenue, a child's chances would depend heavily on the State of birth, which is the same as saying that without transfers public services would depend more on where one lives. "
   "2 is not valid: the passage aims at 'broadly comparable services at broadly comparable rates of tax', not at equal revenue per person; and it explains the richer States' revenue by their larger tax base and the shared national market, not by better government.",
   "केवल 1 वैध है: परिच्छेद कहता है कि यदि हर राज्य अपने ही राजस्व पर चले, तो बच्चे के अवसर बहुत हद तक जन्म के राज्य पर निर्भर करेंगे, जो यह कहने के समान है कि हस्तांतरणों के बिना सार्वजनिक सेवाएँ इस पर अधिक निर्भर होंगी कि कोई कहाँ रहता है। "
   "2 वैध नहीं है: परिच्छेद 'मोटे तौर पर तुलनीय कर दरों पर मोटे तौर पर तुलनीय सेवाओं' का लक्ष्य रखता है, प्रति व्यक्ति समान राजस्व का नहीं; और वह अमीर राज्यों के राजस्व को उनके बड़े कर-आधार और साझा राष्ट्रीय बाज़ार से समझाता है, बेहतर शासन से नहीं।",
   "conclusions",
   st=["Without transfers, the public services a citizen received would depend more on the State in which the citizen lived.",
       "Richer States raise more revenue per person mainly because their governments are more efficient."],
   st_hi=["हस्तांतरणों के बिना, किसी नागरिक को मिलने वाली सार्वजनिक सेवाएँ इस पर अधिक निर्भर होतीं कि वह किस राज्य में रहता है।",
          "अमीर राज्य प्रति व्यक्ति अधिक राजस्व मुख्यतः इसलिए जुटाते हैं कि उनकी सरकारें अधिक कुशल हैं।"],
   key=0)

# ------------------------------------------------------------------ P09 Ashoka's case for restraint in speech (3)
p = passage("p09",
  "In his inscriptions the emperor Ashoka asked his subjects to respect the beliefs of others. One edict warns that a person who praises his own sect and condemns the sects of others, out of devotion to his own, in fact does it great harm. "
  "What is striking is not only the plea for tolerance but its reasoning. Ashoka did not argue that all beliefs are equally true, nor did he ask people to give up their own. "
  "He argued that restraint in speech -- not praising one's own faith and running down others' without cause -- served everyone, the faithful included, because a community known for contempt makes enemies and loses the respect it seeks. "
  "Tolerance, on this view, is not indifference to truth but a discipline of conduct, and it was to be taught and encouraged: Ashoka appointed officials to promote dhamma among all communities. "
  "Whether a ruler should take on such a role is a fair question; that he thought tolerance needed cultivating, rather than simply assuming it, is perhaps his most modern insight.",
  "अपने अभिलेखों में सम्राट अशोक ने अपनी प्रजा से दूसरों की मान्यताओं का सम्मान करने को कहा। एक अभिलेख चेताता है कि जो व्यक्ति अपने संप्रदाय के प्रति भक्ति के कारण अपने संप्रदाय की प्रशंसा और दूसरों के संप्रदायों की निंदा करता है, वह वास्तव में अपने संप्रदाय को बड़ी हानि पहुँचाता है। "
  "ध्यान खींचने वाली बात केवल सहिष्णुता की अपील नहीं, बल्कि उसका तर्क है। अशोक ने यह तर्क नहीं दिया कि सभी मान्यताएँ समान रूप से सत्य हैं, न ही उन्होंने लोगों से अपनी मान्यताएँ छोड़ने को कहा। "
  "उनका तर्क था कि वाणी में संयम -- बिना कारण अपने धर्म की प्रशंसा और दूसरों के धर्म की निंदा न करना -- सबके हित में है, धर्मनिष्ठों के भी, क्योंकि तिरस्कार के लिए जाना जाने वाला समुदाय शत्रु बनाता है और वह सम्मान खो देता है जो वह चाहता है। "
  "इस दृष्टि से सहिष्णुता सत्य के प्रति उदासीनता नहीं, बल्कि आचरण का अनुशासन है, और उसे सिखाया और प्रोत्साहित किया जाना था: अशोक ने सभी समुदायों में धम्म को बढ़ावा देने के लिए अधिकारी नियुक्त किए। "
  "किसी शासक को ऐसी भूमिका लेनी चाहिए या नहीं, यह एक उचित प्रश्न है; पर यह कि उन्होंने सहिष्णुता को केवल मान लेने के बजाय पोषित करने योग्य समझा, शायद उनकी सबसे आधुनिक अंतर्दृष्टि है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage stresses the reasoning behind Ashoka's plea: tolerance as a discipline of conduct that serves everyone, the faithful included, and something to be cultivated rather than assumed. "
   "It says that Ashoka did not argue that all beliefs are equally true and did not ask people to give up their own sects; and it treats a ruler's appointing officials for dhamma as 'a fair question', not as a recommendation.",
   "परिच्छेद अशोक की अपील के पीछे के तर्क पर बल देता है: सहिष्णुता आचरण के एक ऐसे अनुशासन के रूप में जो धर्मनिष्ठों सहित सबके हित में है, और जिसे मान लेने के बजाय पोषित करना होता है। "
   "वह कहता है कि अशोक ने यह तर्क नहीं दिया कि सभी मान्यताएँ समान रूप से सत्य हैं और लोगों से अपने संप्रदाय छोड़ने को नहीं कहा; और वह शासक द्वारा धम्म के लिए अधिकारी नियुक्त करने को 'एक उचित प्रश्न' मानता है, सिफ़ारिश नहीं।",
   "crux",
   opts=["Ashoka taught that all religious beliefs are equally true and deserve equal praise.",
         "Rulers ought to appoint officials to supervise the religious life of their subjects.",
         "Ashoka asked his subjects to give up their own sects for the sake of peace and harmony in his empire.",
         "Ashoka saw tolerance as a discipline that serves all, one's own faith included, and must be nurtured."],
   opts_hi=["अशोक ने सिखाया कि सभी धार्मिक मान्यताएँ समान रूप से सत्य हैं और समान प्रशंसा की पात्र हैं।",
            "शासकों को अपनी प्रजा के धार्मिक जीवन की देखरेख के लिए अधिकारी नियुक्त करने चाहिए।",
            "अशोक ने अपनी प्रजा से अपने साम्राज्य में शांति और सद्भाव बनाए रखने के लिए अपने-अपने संप्रदाय छोड़ देने को कहा।",
            "अशोक सहिष्णुता को ऐसा अनुशासन मानते थे जो अपने धर्म सहित सबके हित में है और जिसे पोषित करना होता है।"],
   ans=3, pos=3)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Only 2 is valid. Ashoka did not ask people to give up their own beliefs; he asked for restraint in speaking of others', and argued that this served the faithful themselves. So on his reasoning a person can hold firmly to his own faith and still be tolerant. "
   "1 is the opposite of what the passage says: Ashoka thought that tolerance 'needed cultivating, rather than simply assuming it', and appointed officials to promote it.",
   "केवल 2 वैध है। अशोक ने लोगों से अपनी मान्यताएँ छोड़ने को नहीं कहा; उन्होंने दूसरों की मान्यताओं के बारे में बोलने में संयम माँगा, और तर्क दिया कि यह स्वयं धर्मनिष्ठों के हित में है। इसलिए उनके तर्क के अनुसार कोई व्यक्ति अपने धर्म को दृढ़ता से मानते हुए भी सहिष्णु हो सकता है। "
   "1 परिच्छेद के कथन का उलटा है: अशोक सहिष्णुता को 'केवल मान लेने के बजाय पोषित करने योग्य' समझते थे, और उसे बढ़ावा देने के लिए अधिकारी नियुक्त किए।",
   "conclusions",
   st=["Ashoka believed that tolerance comes naturally to people and needs no teaching.",
       "On Ashoka's reasoning, a person could hold firmly to his own faith and still practise tolerance."],
   st_hi=["अशोक मानते थे कि सहिष्णुता लोगों में स्वाभाविक रूप से आती है और उसे सिखाने की आवश्यकता नहीं।",
          "अशोक के तर्क के अनुसार, कोई व्यक्ति अपने धर्म को दृढ़ता से मानते हुए भी सहिष्णुता का पालन कर सकता है।"],
   key=1)
RQ(p, "Specific Detail", "easy", "mcq",
   "According to the passage, why did Ashoka hold that condemning other sects harms one's own?",
   "परिच्छेद के अनुसार, अशोक यह क्यों मानते थे कि दूसरे संप्रदायों की निंदा अपने संप्रदाय को हानि पहुँचाती है?",
   "The passage gives Ashoka's reason: a community known for contempt makes enemies and loses the respect it seeks. "
   "It says that he did not argue that all sects are equally true, so their teaching the same truths is not his reason; and it mentions no punishment by the State and no doubt that condemning others would raise about one's own faith.",
   "परिच्छेद अशोक का कारण बताता है: तिरस्कार के लिए जाना जाने वाला समुदाय शत्रु बनाता है और वह सम्मान खो देता है जो वह चाहता है। "
   "वह कहता है कि अशोक ने यह तर्क नहीं दिया कि सभी संप्रदाय समान रूप से सत्य हैं, इसलिए उनका एक ही सत्य सिखाना उनका कारण नहीं है; और वह न राज्य द्वारा किसी दंड का उल्लेख करता है न ऐसे संदेह का जो दूसरों की निंदा से अपने धर्म के बारे में उठे।",
   "why-harm",
   opts=["A community known for contempt makes enemies and loses the respect it seeks.",
         "All sects teach the same truths, so condemning one of them condemns them all.",
         "The State punished severely those who spoke against the sects of others.",
         "Condemning others makes a person begin to doubt the truth of his own faith."],
   opts_hi=["तिरस्कार के लिए जाना गया समुदाय शत्रु बनाता है और अपना चाहा हुआ सम्मान खो देता है।",
            "सभी संप्रदाय एक ही सत्य सिखाते हैं, इसलिए उनमें से एक की निंदा सबकी निंदा है।",
            "राज्य दूसरों के संप्रदायों के विरुद्ध बोलने वालों को कठोर दंड देता था।",
            "दूसरों की निंदा करने से व्यक्ति धीरे-धीरे अपने ही धर्म के सत्य पर संदेह करने लगता है।"],
   ans=0, pos=1)

# ------------------------------------------------------------------ P10 lending decided by algorithms (3)
p = passage("p10",
  "Lenders increasingly decide whom to lend to with the help of algorithms that look at far more than a credit history: how regularly a person pays mobile bills, how often an app is used, even the time of day at which a loan form is filled in. "
  "Supporters point out that this can bring credit to people with no formal record, who were once refused by default. Critics worry about two things. "
  "First, a model trained on past lending can learn the patterns of past exclusion and repeat them, without any instruction to discriminate, simply because some signals stand in for income, caste, gender or place. "
  "Second, a person refused by such a model may never learn why, and so cannot correct an error or change the behaviour that counted against them. "
  "Neither worry is a reason to go back to refusing everyone without a record. They are reasons to test models for unequal outcomes and to give applicants an account of the main factors behind a decision.",
  "ऋणदाता अब बढ़ते रूप में यह तय करते हैं कि किसे ऋण दें, ऐसे एल्गोरिद्म की सहायता से जो क्रेडिट इतिहास से कहीं अधिक देखते हैं: कोई व्यक्ति मोबाइल बिल कितनी नियमितता से चुकाता है, कोई ऐप कितनी बार प्रयोग होता है, यहाँ तक कि ऋण का फ़ॉर्म दिन के किस समय भरा गया। "
  "समर्थक बताते हैं कि इससे उन लोगों तक ऋण पहुँच सकता है जिनका कोई औपचारिक रिकॉर्ड नहीं है और जिन्हें पहले अपने-आप मना कर दिया जाता था। आलोचक दो बातों से चिंतित हैं। "
  "पहली, पुराने ऋणों पर प्रशिक्षित मॉडल पिछले बहिष्कार के पैटर्न सीखकर उन्हें दोहरा सकता है, भेदभाव के किसी निर्देश के बिना, केवल इसलिए कि कुछ संकेत आय, जाति, लिंग या स्थान का स्थान ले लेते हैं। "
  "दूसरी, ऐसे मॉडल द्वारा मना किया गया व्यक्ति शायद कभी न जान पाए कि क्यों, और इसलिए न किसी त्रुटि को सुधार सके न उस व्यवहार को बदल सके जो उसके विरुद्ध गया। "
  "इनमें से कोई चिंता बिना रिकॉर्ड वाले हर व्यक्ति को मना करने की ओर लौटने का कारण नहीं है। वे मॉडलों को असमान परिणामों के लिए जाँचने और आवेदकों को निर्णय के पीछे के मुख्य कारकों का विवरण देने के कारण हैं।")
RQ(p, "Inference", "hard", "mcq", INFER1, INFER1_HI,
   "The passage says that a model can repeat past exclusion 'without any instruction to discriminate, simply because some signals stand in for income, caste, gender or place'. So a model never shown those characteristics directly can still treat groups unequally through the signals that track them. "
   "The passage does not say that people without a record are poor risks, that models trained on past lending are more accurate, or that the time of day reveals a borrower's honesty -- it lists the time of day only as one of the signals used.",
   "परिच्छेद कहता है कि मॉडल पिछले बहिष्कार को 'भेदभाव के किसी निर्देश के बिना, केवल इसलिए कि कुछ संकेत आय, जाति, लिंग या स्थान का स्थान ले लेते हैं', दोहरा सकता है। इसलिए जिस मॉडल को ये विशेषताएँ सीधे कभी न दिखाई गई हों, वह भी उनसे जुड़े संकेतों के माध्यम से समूहों से असमान व्यवहार कर सकता है। "
   "परिच्छेद यह नहीं कहता कि बिना रिकॉर्ड वाले लोग जोखिम भरे उधारकर्ता हैं, कि पुराने ऋणों पर प्रशिक्षित मॉडल अधिक सटीक हैं, या कि दिन का समय उधारकर्ता की ईमानदारी बताता है -- वह दिन के समय को केवल प्रयुक्त संकेतों में से एक के रूप में गिनाता है।",
   "unequal-without-instruction",
   opts=["A lending model can treat groups unequally even if it is never given their caste, gender or income directly.",
         "People who have no formal credit record are usually poor risks for any lender.",
         "Models trained on past lending are more accurate than models that are not.",
         "The time of day at which a loan form is filled in is a reliable sign of how honest a borrower is likely to be."],
   opts_hi=["ऋण का कोई मॉडल समूहों से असमान व्यवहार कर सकता है, भले ही उसे उनकी जाति, लिंग या आय सीधे कभी न दी गई हो।",
            "जिन लोगों का कोई औपचारिक क्रेडिट रिकॉर्ड नहीं, वे किसी भी ऋणदाता के लिए प्रायः जोखिम भरे उधारकर्ता होते हैं।",
            "पुराने ऋणों पर प्रशिक्षित मॉडल उन मॉडलों से अधिक सटीक होते हैं जो ऐसे प्रशिक्षित नहीं हैं।",
            "ऋण का फ़ॉर्म दिन के किस समय भरा गया, यह उधारकर्ता की ईमानदारी विश्वसनीय रूप से दिखाता है।"],
   ans=0, pos=0)
RQ(p, "Best Summary", "medium", "mcq", MSG, MSG_HI,
   "The passage weighs a benefit (credit for people with no record) against two risks (repeating past exclusion, and refusals that cannot be understood) and concludes that the answer is testing and explanation, not a return to refusing by default. "
   "It does not reject algorithms in lending; it does not rank credit histories against mobile data; and it says that a model can discriminate 'without any instruction to discriminate', so it does not accuse lenders of deliberate exclusion.",
   "परिच्छेद एक लाभ (बिना रिकॉर्ड वालों के लिए ऋण) को दो जोखिमों (पिछले बहिष्कार को दोहराना, और ऐसे इनकार जो समझे न जा सकें) के सामने तौलता है और निष्कर्ष निकालता है कि उत्तर जाँच और व्याख्या है, अपने-आप मना करने की ओर लौटना नहीं। "
   "वह ऋण में एल्गोरिद्म को अस्वीकार नहीं करता; वह क्रेडिट इतिहास की तुलना मोबाइल आँकड़ों से नहीं करता; और वह कहता है कि मॉडल 'भेदभाव के किसी निर्देश के बिना' भेदभाव कर सकता है, इसलिए वह ऋणदाताओं पर जानबूझकर बहिष्कार का आरोप नहीं लगाता।",
   "message",
   opts=["Algorithms should not be used in lending at all, because they always work against the interests of the poor.",
         "Credit histories are less reliable than mobile-phone data for judging borrowers.",
         "Such lending can widen access to credit, but its models need testing for bias and must explain decisions.",
         "Lenders deliberately instruct their models to exclude borrowers from certain groups."],
   opts_hi=["ऋण देने में एल्गोरिद्म का प्रयोग नहीं होना चाहिए, क्योंकि वे हमेशा ग़रीबों के विरुद्ध काम करते हैं।",
            "उधारकर्ताओं को आँकने के लिए क्रेडिट इतिहास मोबाइल फ़ोन के आँकड़ों से कम विश्वसनीय है।",
            "ऐसा ऋण-वितरण पहुँच बढ़ा सकता है, पर उसके मॉडलों की पक्षपात के लिए जाँच हो और वे निर्णय समझाएँ।",
            "ऋणदाता जानबूझकर अपने मॉडलों को कुछ समूहों के उधारकर्ताओं को बाहर रखने का निर्देश देते हैं।"],
   ans=2, pos=2)
RQ(p, "Assumption", "medium", "s2", ASSUME, ASSUME_HI,
   "Neither is assumed. 1 goes beyond the passage: it says that such lending can bring credit to people with no record, not that most of them would repay on time, and its argument does not depend on their doing so. "
   "2 is not assumed either: the passage compares the algorithms with refusing everyone without a record, not with human loan officers, and says nothing about which is more accurate.",
   "कोई भी पूर्वधारणा नहीं है। 1 परिच्छेद से आगे जाता है: वह कहता है कि ऐसा ऋण-वितरण बिना रिकॉर्ड वालों तक ऋण पहुँचा सकता है, यह नहीं कि उनमें से अधिकांश समय पर चुकाएँगे, और उसका तर्क उनके ऐसा करने पर निर्भर नहीं। "
   "2 भी पूर्वधारणा नहीं है: परिच्छेद एल्गोरिद्म की तुलना बिना रिकॉर्ड वाले हर व्यक्ति को मना करने से करता है, मानवीय ऋण अधिकारियों से नहीं, और यह कुछ नहीं कहता कि कौन अधिक सटीक है।",
   "assumptions",
   st=["Most people without a formal credit record would repay their loans on time.",
       "Algorithms judge borrowers less accurately than human loan officers do."],
   st_hi=["औपचारिक क्रेडिट रिकॉर्ड के बिना अधिकांश लोग अपने ऋण समय पर चुका देंगे।",
          "एल्गोरिद्म उधारकर्ताओं को मानवीय ऋण अधिकारियों से कम सटीकता से आँकते हैं।"],
   key=3)
