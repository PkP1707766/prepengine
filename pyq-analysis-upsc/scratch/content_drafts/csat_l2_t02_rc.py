# -*- coding: utf-8 -*-
"""CSAT Level 2 · Test 2 -- Reading Comprehension: 10 original passages, 28 items (8 x 3, 2 x 2).

Themes, none repeated from Test 1: weather-index crop insurance, mother-tongue reading, urban water losses,
handloom, battery recycling, pollinators, court backlog and mediation, music teaching and recordings,
consent and privacy, and old-age care. Item types: main idea 7, inference 7, assumption 6, tone 1,
specific detail 4 (one of them 'which is NOT correct', as in the 2026 paper), best summary 3."""
import csat_common as c
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

# ------------------------------------------------------------------ P01 weather-index insurance (3)
p = passage("p01",
  "Crop insurance in India has long worked by measuring losses: after a drought, officials cut sample plots, weigh the grain and compare it with normal yields. The method is fair in principle but slow in practice, "
  "and farmers may wait months for money they needed in weeks. Insurance tied to a weather index pays out instead when the rainfall at a nearby station falls below an agreed level, whatever happened on any particular farm. "
  "Payment can then follow within days, and there is no field to inspect and no claim to dispute. The price of that speed is 'basis risk': a farmer whose crop failed may get nothing because the station recorded "
  "enough rain, while a neighbour with a good harvest is paid. The denser the network of weather stations, the smaller this gap becomes.",
  "भारत में फ़सल बीमा लंबे समय से हानि मापकर काम करता रहा है: सूखे के बाद अधिकारी नमूना खेतों की फ़सल काटते हैं, अनाज तौलते हैं और उसकी तुलना सामान्य उपज से करते हैं। यह तरीका सिद्धांत रूप में न्यायपूर्ण है पर व्यवहार में धीमा, "
  "और किसानों को वह पैसा पाने के लिए महीनों प्रतीक्षा करनी पड़ सकती है जिसकी उन्हें सप्ताहों में ज़रूरत थी। मौसम सूचकांक से जुड़ा बीमा इसके बजाय तब भुगतान करता है जब पास के किसी केंद्र पर वर्षा एक तय स्तर से नीचे रहे, चाहे किसी विशेष खेत पर कुछ भी हुआ हो। "
  "तब भुगतान कुछ ही दिनों में हो सकता है, और न कोई खेत जाँचना पड़ता है, न कोई दावा विवादित होता है। इस गति की क़ीमत 'आधार जोखिम' (basis risk) है: जिस किसान की फ़सल नष्ट हुई, उसे कुछ न मिले क्योंकि केंद्र ने पर्याप्त वर्षा दर्ज की, "
  "जबकि अच्छी फ़सल वाले पड़ोसी को भुगतान मिल जाए। मौसम केंद्रों का जाल जितना घना होगा, यह अंतर उतना ही छोटा होगा।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage weighs the speed of index insurance against its basis risk: it pays fast, but by the station's rainfall, not by each farm's loss. Calling the sample-plot method unfair misstates the passage, which calls it fair in principle but slow; "
   "saying index insurance has removed the need for yield-based cover overreaches, since the passage compares the two methods without saying one has replaced the other; paying farmers on their own harvests alone is never argued.",
   "परिच्छेद सूचकांक बीमा की गति को उसके आधार जोखिम के विरुद्ध तौलता है: यह जल्दी भुगतान करता है, पर केंद्र की वर्षा के आधार पर, हर खेत की हानि के आधार पर नहीं। नमूना खेतों वाले तरीके को अन्यायपूर्ण कहना परिच्छेद को ग़लत पढ़ना है, जो उसे सिद्धांत रूप में न्यायपूर्ण पर धीमा कहता है; "
   "यह कहना कि सूचकांक बीमा ने उपज-आधारित बीमा की आवश्यकता समाप्त कर दी, बहुत आगे जाना है, क्योंकि परिच्छेद दोनों तरीकों की तुलना करता है, यह नहीं कहता कि एक ने दूसरे की जगह ले ली; और केवल अपनी फ़सल के आधार पर भुगतान का तर्क कहीं नहीं दिया गया।",
   "crux",
   opts=["Index insurance pays fast, but its payouts may not match each farm's actual loss.",
         "Measuring crop losses by cutting sample plots is unfair to farmers and should be given up.",
         "Weather-index insurance has now removed the need for any crop insurance based on measured yields.",
         "Farmers should be paid on the basis of their own harvests alone."],
   opts_hi=["सूचकांक बीमा जल्दी भुगतान करता है, पर ज़रूरी नहीं कि वह हर खेत की हानि से मेल खाए।",
            "नमूना खेतों की फ़सल काटकर हानि मापना किसानों के साथ अन्याय है और इसे छोड़ देना चाहिए।",
            "मौसम सूचकांक बीमा ने अब मापी गई उपज पर आधारित किसी भी फ़सल बीमा की आवश्यकता समाप्त कर दी है।",
            "किसानों को केवल उनकी अपनी फ़सल के आधार पर भुगतान किया जाना चाहिए।"],
   ans=0, pos=3)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Only 1 is valid: the payout depends on a nearby station's rainfall 'whatever happened on any particular farm', so neighbours with very different harvests can be paid alike. "
   "2 misreads the last sentence: more stations shrink the gap between the index and each farm's loss, which makes payouts more accurate, not larger for everyone.",
   "केवल 1 वैध है: भुगतान पास के केंद्र की वर्षा पर निर्भर है, 'चाहे किसी विशेष खेत पर कुछ भी हुआ हो', इसलिए बहुत अलग फ़सल वाले पड़ोसियों को समान भुगतान मिल सकता है। "
   "2 अंतिम वाक्य को ग़लत पढ़ता है: अधिक केंद्र सूचकांक और हर खेत की हानि के बीच का अंतर घटाते हैं, जिससे भुगतान अधिक सटीक होता है, सबके लिए बड़ा नहीं।",
   "conclusions",
   st=["Under index insurance, two neighbouring farms with very different harvests may receive the same payout.",
       "Adding more weather stations would make index insurance pay more to every farmer."],
   st_hi=["सूचकांक बीमा में बहुत अलग फ़सल वाले दो पड़ोसी खेतों को समान भुगतान मिल सकता है।",
          "अधिक मौसम केंद्र जोड़ने से सूचकांक बीमा हर किसान को अधिक भुगतान करेगा।"],
   key=0)
RQ(p, "Specific Detail", "easy", "mcq",
   "As used in the passage, 'basis risk' refers to:",
   "परिच्छेद में प्रयुक्त 'आधार जोखिम' का अर्थ है:",
   "The passage defines basis risk as the mismatch by which a farmer whose crop failed may get nothing because the station recorded enough rain, while a neighbour with a good harvest is paid. "
   "The delay in payment belongs to the older, yield-based method; the insurer's finances and the chance of a poor monsoon are not what the term means here.",
   "परिच्छेद आधार जोखिम को उस बेमेल के रूप में परिभाषित करता है जिसमें नष्ट फ़सल वाले किसान को कुछ न मिले क्योंकि केंद्र ने पर्याप्त वर्षा दर्ज की, जबकि अच्छी फ़सल वाले पड़ोसी को भुगतान मिल जाए। "
   "भुगतान में देरी पुराने, उपज-आधारित तरीके की समस्या है; बीमाकर्ता की वित्तीय स्थिति और कमज़ोर मानसून की संभावना इस शब्द का अर्थ नहीं हैं।",
   "detail",
   opts=["the gap between what the station records and what a farm suffers",
         "the risk that the insurer will not have the money to pay claims",
         "the delay between a crop loss and the payment of the claim",
         "the chance that rainfall in a year will be below normal everywhere"],
   opts_hi=["केंद्र जो दर्ज करता है और खेत को जो हानि होती है, उनके बीच का अंतर",
            "यह जोखिम कि बीमाकर्ता के पास दावों का भुगतान करने के लिए पर्याप्त धन ही न हो",
            "फ़सल की हानि और दावे के भुगतान के बीच की देरी",
            "यह संभावना कि किसी वर्ष हर जगह वर्षा सामान्य से कम हो"],
   ans=0, pos=2)

# ------------------------------------------------------------------ P02 mother-tongue reading (3)
p = passage("p02",
  "A child who starts school in a language she does not speak at home faces two tasks at once: learning to read, and learning the language in which reading is taught. Many manage, but many more fall behind in the "
  "first two years and never catch up. Studies across countries find that children taught to read first in their home language later read better even in a second language, because the skill of decoding -- linking "
  "written symbols to sounds and meanings -- carries over once it is learnt. The practical obstacles are real: a district may have pupils speaking a dozen languages, few textbooks exist in most of them, and parents "
  "often press for English from the first day, believing early exposure to be the surest route to good jobs. The evidence suggests that the surest route is early reading, in whatever language the child already speaks.",
  "जो बच्ची ऐसी भाषा में विद्यालय शुरू करती है जो वह घर पर नहीं बोलती, उसके सामने एक साथ दो काम होते हैं: पढ़ना सीखना, और वह भाषा सीखना जिसमें पढ़ना सिखाया जाता है। कई बच्चे सँभाल लेते हैं, पर उससे कहीं अधिक "
  "पहले दो वर्षों में पिछड़ जाते हैं और फिर कभी बराबरी नहीं कर पाते। अनेक देशों के अध्ययन पाते हैं कि जिन बच्चों को पहले उनकी घर की भाषा में पढ़ना सिखाया जाता है, वे बाद में दूसरी भाषा में भी बेहतर पढ़ते हैं, क्योंकि लिपि पढ़ने का कौशल -- लिखे संकेतों को "
  "ध्वनियों और अर्थों से जोड़ना -- एक बार सीख लेने पर दूसरी भाषा में भी काम आता है। व्यावहारिक बाधाएँ वास्तविक हैं: किसी ज़िले में दर्जन भर भाषाएँ बोलने वाले विद्यार्थी हो सकते हैं, उनमें से अधिकांश भाषाओं में पाठ्यपुस्तकें कम हैं, और माता-पिता "
  "प्रायः पहले दिन से अंग्रेज़ी पर ज़ोर देते हैं, यह मानकर कि जल्दी परिचय अच्छी नौकरी का सबसे पक्का रास्ता है। प्रमाण बताते हैं कि सबसे पक्का रास्ता जल्दी पढ़ना सीखना है, उसी भाषा में जो बच्चा पहले से बोलता है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage argues that reading learnt first in the home language transfers to later languages, so early reading in that language is the surest route. "
   "It never says English should not be taught; it reports parents' demand for English without calling it the main cause of poor reading; and the lack of textbooks is an obstacle it acknowledges, not its conclusion.",
   "परिच्छेद का तर्क है कि घर की भाषा में पहले सीखा गया पढ़ना बाद की भाषाओं में भी काम आता है, इसलिए उस भाषा में जल्दी पढ़ना सीखना सबसे पक्का रास्ता है। "
   "वह कहीं नहीं कहता कि अंग्रेज़ी नहीं पढ़ाई जानी चाहिए; वह माता-पिता की अंग्रेज़ी की माँग बताता है पर उसे कमज़ोर पढ़ाई का मुख्य कारण नहीं कहता; और पाठ्यपुस्तकों की कमी एक बाधा है जिसे वह स्वीकार करता है, उसका निष्कर्ष नहीं।",
   "crux",
   opts=["Children who learn to read first in their home language later read other languages better.",
         "Children should not be taught English at any stage of their schooling.",
         "Parents' demand for English from the first day is the main cause of poor reading among children.",
         "Schools cannot teach in home languages, because textbooks in most of those languages do not exist at all."],
   opts_hi=["जो बच्चे पहले घर की भाषा में पढ़ना सीखते हैं, वे बाद में दूसरी भाषाएँ बेहतर पढ़ते हैं।",
            "बच्चों को स्कूली शिक्षा के किसी भी चरण में अंग्रेज़ी नहीं पढ़ाई जानी चाहिए।",
            "पहले दिन से अंग्रेज़ी की माता-पिता की माँग ही बच्चों की कमज़ोर पढ़ाई का मुख्य कारण है।",
            "विद्यालय घर की भाषाओं में नहीं पढ़ा सकते, क्योंकि उनमें से अधिकांश भाषाओं में कोई पाठ्यपुस्तक है ही नहीं।"],
   ans=0, pos=1)
RQ(p, "Assumption", "hard", "sc", ASSUME, ASSUME_HI,
   "1 and 2 are assumed. The author answers parents who see early English as the 'surest route to good jobs' by saying that the surest route is early reading -- which takes for granted that reading well improves a child's later "
   "job prospects (1). The case for home-language reading also rests on the idea that decoding, once learnt, carries over to a new language (2). 3 is not assumed: the author calls the obstacles 'real' and argues for home-language reading despite them, without claiming they are easy to overcome.",
   "1 और 2 पूर्वधारणाएँ हैं। लेखक उन माता-पिता को, जो जल्दी अंग्रेज़ी को 'अच्छी नौकरी का सबसे पक्का रास्ता' मानते हैं, यह कहकर उत्तर देता है कि सबसे पक्का रास्ता जल्दी पढ़ना सीखना है -- जो यह मानकर चलता है कि अच्छी तरह पढ़ पाना "
   "बच्चे की बाद की नौकरी की संभावनाएँ बेहतर करता है (1)। घर की भाषा में पढ़ने का पक्ष इस विचार पर भी टिका है कि एक बार सीखा गया लिपि पढ़ने का कौशल नई भाषा में भी काम आता है (2)। 3 पूर्वधारणा नहीं है: लेखक बाधाओं को 'वास्तविक' कहता है और उनके बावजूद घर की भाषा में पढ़ाने का पक्ष लेता है, यह दावा किए बिना कि उन्हें आसानी से पार किया जा सकता है।",
   "assumptions",
   st=["Children who read well are better placed to get good jobs later.",
       "The ability to read can be carried over from one language to another.",
       "The practical obstacles to teaching in home languages can be easily overcome."],
   st_hi=["जो बच्चे अच्छी तरह पढ़ पाते हैं, वे बाद में अच्छी नौकरी पाने की बेहतर स्थिति में होते हैं।",
          "पढ़ने की क्षमता एक भाषा से दूसरी भाषा में ले जाई जा सकती है।",
          "घर की भाषाओं में पढ़ाने की व्यावहारिक बाधाएँ आसानी से पार की जा सकती हैं।"],
   opts=["1 only", "2 and 3 only", "1 and 2 only", "1, 2 and 3"], key=2)
RQ(p, "Author's Tone", "medium", "mcq",
   "The author's attitude towards parents who press for English from the first day of school is best described as:",
   "विद्यालय के पहले दिन से अंग्रेज़ी पर ज़ोर देने वाले माता-पिता के प्रति लेखक का दृष्टिकोण सबसे अच्छी तरह कैसा बताया जा सकता है?",
   "The author grants the parents' aim -- good jobs for their children -- and calls the obstacles 'real', but argues that the evidence points to a different route, early reading in the home language. "
   "That is sympathy for the goal combined with doubt about the method. Nothing in the passage is contemptuous of them, and it neither endorses their demand nor ignores it.",
   "लेखक माता-पिता के लक्ष्य -- बच्चों के लिए अच्छी नौकरी -- को मानता है और बाधाओं को 'वास्तविक' कहता है, पर तर्क देता है कि प्रमाण एक दूसरे रास्ते, घर की भाषा में जल्दी पढ़ने, की ओर इशारा करते हैं। "
   "यह लक्ष्य के प्रति सहानुभूति के साथ तरीके पर संदेह है। परिच्छेद में उनके प्रति कुछ भी तिरस्कारपूर्ण नहीं है, और वह न उनकी माँग का समर्थन करता है, न उसे अनदेखा करता है।",
   "tone",
   opts=["sympathetic to their aim but doubtful of their method",
         "contemptuous of the ambitions they hold for their children",
         "fully supportive of their demand for English from day one",
         "indifferent to the concerns that drive their demand"],
   opts_hi=["उनके लक्ष्य के प्रति सहानुभूतिपूर्ण पर तरीके को लेकर संशयी",
            "अपने बच्चों के लिए उनकी महत्त्वाकांक्षाओं के प्रति तिरस्कारपूर्ण",
            "पहले दिन से अंग्रेज़ी की उनकी माँग का पूरी तरह समर्थक",
            "उनकी माँग के पीछे की चिंताओं के प्रति उदासीन"],
   ans=0, pos=3)

# ------------------------------------------------------------------ P03 urban water (3)
p = passage("p03",
  "In many Indian cities, as much as two-fifths of the water that leaves the treatment plant never earns any revenue. Some of it leaks from old pipes; some is drawn through illegal connections; some reaches homes whose "
  "meters are broken or missing and is billed at a flat rate. Utilities short of money put off repairs, losses grow, and the gap between what they spend and what they collect widens -- a cycle that leaves poor "
  "neighbourhoods dependent on tankers that cost far more per litre than piped water. Raising tariffs alone would mostly punish the households that already pay. The more promising sequence is the reverse: measure first, "
  "by metering and mapping where the water goes; fix the worst leaks; and only then ask users to pay rates that reflect the cost of a supply they can now rely on.",
  "भारत के कई शहरों में शोधन संयंत्र से निकलने वाले पानी का दो-पाँचवाँ भाग तक कोई राजस्व नहीं देता। उसका कुछ भाग पुरानी पाइपों से रिसता है; कुछ अवैध कनेक्शनों से खींचा जाता है; कुछ ऐसे घरों तक पहुँचता है जिनके मीटर ख़राब हैं या हैं ही नहीं, "
  "और उसका बिल एकमुश्त दर पर बनता है। धन की कमी से जूझती जल-संस्थाएँ मरम्मत टालती हैं, हानि बढ़ती है, और उनके ख़र्च और वसूली के बीच का अंतर चौड़ा होता जाता है -- एक ऐसा चक्र जो ग़रीब बस्तियों को उन टैंकरों पर निर्भर छोड़ देता है "
  "जिनका पानी प्रति लीटर पाइप के पानी से कहीं महँगा पड़ता है। केवल दरें बढ़ाना अधिकतर उन्हीं परिवारों को दंडित करेगा जो पहले से भुगतान करते हैं। अधिक आशाजनक क्रम इसका उलटा है: पहले मापिए, "
  "मीटर लगाकर और यह नक़्शा बनाकर कि पानी कहाँ जाता है; सबसे बड़े रिसाव ठीक कीजिए; और उसके बाद ही उपयोगकर्ताओं से ऐसी दरें माँगिए जो उस आपूर्ति की लागत दर्शाएँ जिस पर वे अब भरोसा कर सकें।")
RQ(p, "Best Summary", "medium", "mcq", MSG, MSG_HI,
   "The passage's 'more promising sequence' is measure, repair, then charge -- so cities should cut losses and measure use before raising tariffs. Raising tariffs first is the step it says would punish paying households; "
   "illegal connections are only one of three causes; and the passage regrets poor neighbourhoods' dependence on tankers rather than recommending it.",
   "परिच्छेद का 'अधिक आशाजनक क्रम' है मापना, मरम्मत, फिर शुल्क -- इसलिए शहरों को दरें बढ़ाने से पहले हानि घटानी और उपयोग मापना चाहिए। पहले दरें बढ़ाना वही कदम है जिसके बारे में वह कहता है कि वह भुगतान करने वाले परिवारों को दंडित करेगा; "
   "अवैध कनेक्शन तीन कारणों में से केवल एक है; और परिच्छेद ग़रीब बस्तियों की टैंकरों पर निर्भरता पर खेद जताता है, उसकी सिफ़ारिश नहीं करता।",
   "message",
   opts=["Cities should cut losses and measure water use before they raise tariffs.",
         "Water utilities should raise tariffs at once so that they can pay for repairs to old pipes.",
         "Illegal connections are the main reason why cities lose so much of their treated water.",
         "Poor neighbourhoods are best supplied by tankers rather than by pipes."],
   opts_hi=["शहरों को दरें बढ़ाने से पहले हानि घटानी चाहिए और पानी का उपयोग मापना चाहिए।",
            "जल-संस्थाओं को तुरंत दरें बढ़ानी चाहिए ताकि वे पुरानी पाइपों की मरम्मत का ख़र्च उठा सकें।",
            "अवैध कनेक्शन ही शहरों में शोधित पानी के इतने बड़े भाग की हानि का मुख्य कारण हैं।",
            "ग़रीब बस्तियों को पाइपों के बजाय टैंकरों से पानी देना सबसे अच्छा है।"],
   ans=0, pos=0)
RQ(p, "Inference", "medium", "sc", INFER, INFER_HI,
   "1 and 2 follow. Homes with broken or missing meters are 'billed at a flat rate', so they may pay the same whatever they use (1); and the passage says raising tariffs alone 'would mostly punish the households that already pay' (2). "
   "3 reverses the passage, which says tankers cost 'far more per litre than piped water'.",
   "1 और 2 निकलते हैं। ख़राब या बिना मीटर वाले घरों का बिल 'एकमुश्त दर पर' बनता है, इसलिए वे जितना भी उपयोग करें, समान भुगतान कर सकते हैं (1); और परिच्छेद कहता है कि केवल दरें बढ़ाना 'अधिकतर उन्हीं परिवारों को दंडित करेगा जो पहले से भुगतान करते हैं' (2)। "
   "3 परिच्छेद को उलट देता है, जो कहता है कि टैंकर का पानी 'प्रति लीटर पाइप के पानी से कहीं महँगा' है।",
   "inferences",
   st=["Households without working meters may pay the same however much water they use.",
       "A rise in tariffs before losses are cut would fall mainly on households that already pay.",
       "Water from tankers is cheaper per litre than piped water."],
   st_hi=["बिना चालू मीटर वाले परिवार जितना भी पानी उपयोग करें, समान भुगतान कर सकते हैं।",
          "हानि घटाए बिना दरें बढ़ाने का बोझ मुख्यतः उन परिवारों पर पड़ेगा जो पहले से भुगतान करते हैं।",
          "टैंकरों का पानी प्रति लीटर पाइप के पानी से सस्ता है।"],
   opts=["1 only", "2 and 3 only", "1, 2 and 3", "1 and 2 only"], key=3)
RQ(p, "Assumption", "hard", "s2", ASSUME, ASSUME_HI,
   "Only 1 is assumed. The plan to raise rates last, once the supply is reliable, makes sense only if users are more willing to pay for a supply they can depend on. "
   "2 runs against the passage, which treats fixing the worst leaks as a practical step.",
   "केवल 1 पूर्वधारणा है। दरें अंत में, आपूर्ति भरोसेमंद होने के बाद, बढ़ाने की योजना तभी अर्थपूर्ण है जब उपयोगकर्ता उस आपूर्ति के लिए अधिक भुगतान करने को तैयार हों जिस पर वे निर्भर रह सकें। "
   "2 परिच्छेद के विपरीत है, जो सबसे बड़े रिसावों को ठीक करना एक व्यावहारिक कदम मानता है।",
   "assumptions",
   st=["People are more willing to pay higher rates for a supply they can rely on.",
       "Most leaks in old city pipes cannot be repaired."],
   st_hi=["लोग भरोसेमंद आपूर्ति के लिए ऊँची दरें देने को अधिक तैयार होते हैं।",
          "शहर की पुरानी पाइपों के अधिकांश रिसाव ठीक नहीं किए जा सकते।"],
   key=0)

# ------------------------------------------------------------------ P04 handloom (2)
p = passage("p04",
  "A handloom sari woven over three weeks competes in the market with a powerloom copy produced in an afternoon and sold for a fraction of the price. Customers who cannot tell the two apart will not pay for the difference, "
  "and the weaver, unable to earn enough for the time spent, leaves the loom for construction work. Geographical indications and handloom marks were meant to let buyers trust what they are paying for, but a label is only as good as the "
  "checks behind it, and copies bearing borrowed labels are easy to find. What the weaver needs is less a subsidy than a buyer who knows: direct sales, credible certification and designs that a machine cannot easily copy.",
  "तीन सप्ताह में बुनी गई हथकरघा साड़ी बाज़ार में एक दोपहर में बनी और कहीं कम दाम पर बिकने वाली पावरलूम नक़ल से होड़ करती है। जो ग्राहक दोनों में अंतर नहीं पहचान सकते, वे उस अंतर के लिए भुगतान नहीं करेंगे, "
  "और अपने समय की लागत न निकाल पाने वाला बुनकर करघा छोड़कर निर्माण-कार्य में चला जाता है। भौगोलिक संकेत और हथकरघा चिह्न इसलिए बनाए गए थे कि ख़रीदार उस पर भरोसा कर सकें जिसके लिए वे भुगतान कर रहे हैं, पर कोई लेबल उतना ही अच्छा है जितनी उसके पीछे की जाँच, "
  "और उधार लिए लेबल वाली नक़लें आसानी से मिल जाती हैं। बुनकर को सब्सिडी से अधिक एक जानकार ख़रीदार चाहिए: सीधी बिक्री, विश्वसनीय प्रमाणन और ऐसे डिज़ाइन जिनकी नक़ल मशीन आसानी से न कर सके।")
RQ(p, "Assumption", "hard", "s2", ASSUME, ASSUME_HI,
   "Only 2 is assumed. The argument that weavers need 'a buyer who knows' takes for granted that buyers who could tell handloom from powerloom would pay more for it -- the passage's complaint is that customers 'who cannot tell the two apart will not pay for the difference'. "
   "1 contradicts the passage, which says copies with borrowed labels 'are easy to find'.",
   "केवल 2 पूर्वधारणा है। यह तर्क कि बुनकरों को 'एक जानकार ख़रीदार' चाहिए, मानकर चलता है कि जो ख़रीदार हथकरघा और पावरलूम में अंतर पहचान सकें, वे हथकरघा के लिए अधिक भुगतान करेंगे -- परिच्छेद की शिकायत यही है कि 'जो ग्राहक दोनों में अंतर नहीं पहचान सकते, वे उस अंतर के लिए भुगतान नहीं करेंगे'। "
   "1 परिच्छेद का खंडन करता है, जो कहता है कि उधार लिए लेबल वाली नक़लें 'आसानी से मिल जाती हैं'।",
   "assumptions",
   st=["Geographical indications have stopped the sale of powerloom copies of handloom saris.",
       "Buyers who could tell handloom from powerloom would pay more for handloom."],
   st_hi=["भौगोलिक संकेतों ने हथकरघा साड़ियों की पावरलूम नक़लों की बिक्री रोक दी है।",
          "जो ख़रीदार हथकरघा और पावरलूम में अंतर पहचान सकें, वे हथकरघा के लिए अधिक भुगतान करेंगे।"],
   key=1)
RQ(p, "Main Idea", "easy", "mcq", CRUX, CRUX_HI,
   "The passage traces the weaver's decline to buyers who cannot tell handloom from a copy, and ends by asking for buyers who know -- trust in what is being bought. "
   "It says the weaver needs 'less a subsidy' than such buyers; it proposes no ban; and it says customers will not pay for a difference they cannot see, not that they have stopped valuing hand-woven cloth.",
   "परिच्छेद बुनकर के पतन को उन ख़रीदारों से जोड़ता है जो हथकरघा और नक़ल में अंतर नहीं पहचान पाते, और अंत में जानकार ख़रीदारों की माँग करता है -- जो ख़रीदा जा रहा है उस पर भरोसा। "
   "वह कहता है कि बुनकर को ऐसे ख़रीदारों की तुलना में 'सब्सिडी की कम' ज़रूरत है; वह किसी प्रतिबंध का प्रस्ताव नहीं करता; और वह कहता है कि ग्राहक उस अंतर के लिए भुगतान नहीं करेंगे जो वे देख नहीं पाते, यह नहीं कि उन्होंने हाथ से बुने कपड़े को महत्त्व देना छोड़ दिया है।",
   "crux",
   opts=["Handloom can survive only if buyers can trust what they are buying.",
         "Handloom weavers need larger subsidies if they are to compete with powerlooms.",
         "The sale of powerloom copies of handloom saris should be banned to protect weavers.",
         "Customers no longer value cloth that has been woven by hand."],
   opts_hi=["हथकरघा तभी बच सकता है जब ख़रीदार उस पर भरोसा कर सकें जो वे ख़रीद रहे हैं।",
            "यदि हथकरघा बुनकरों को पावरलूम से होड़ करनी है, तो उन्हें कहीं बड़ी सब्सिडी चाहिए।",
            "बुनकरों की रक्षा के लिए हथकरघा साड़ियों की पावरलूम नक़लों की बिक्री पर रोक लगनी चाहिए।",
            "ग्राहक अब हाथ से बुने कपड़े को महत्त्व नहीं देते।"],
   ans=0, pos=0)

# ------------------------------------------------------------------ P05 battery recycling (3)
p = passage("p05",
  "An electric car's battery, its most costly part, holds lithium, nickel, cobalt and graphite. When the battery wears out after a decade or so, those metals do not wear out with it; recovered and refined, "
  "they can go into new batteries. Recycling is often presented as the answer to the scarcity of these minerals, but its arithmetic is slow. The cars that will retire in 2035 are the much smaller number sold around 2025, "
  "while demand by then will be many times higher. For the next two decades, recycled metal can meet only a modest share of the need, and new mines will still be required. Recycling's real value lies further ahead, "
  "once the stock of batteries in use is large and growing more slowly -- which is why the plants and the collection systems have to be built now, before the wave of old batteries arrives.",
  "किसी इलेक्ट्रिक कार की बैटरी में, जो उसका सबसे महँगा भाग है, लिथियम, निकल, कोबाल्ट और ग्रेफ़ाइट होते हैं। लगभग एक दशक बाद जब बैटरी घिस जाती है, तो ये धातुएँ उसके साथ नहीं घिसतीं; उन्हें निकालकर और शुद्ध करके "
  "नई बैटरियों में लगाया जा सकता है। पुनर्चक्रण को प्रायः इन खनिजों की कमी का उत्तर बताया जाता है, पर इसका गणित धीमा है। 2035 में सेवा से हटने वाली कारें वे होंगी जो लगभग 2025 में बिकी थीं, जिनकी संख्या कहीं कम है, "
  "जबकि तब तक माँग कई गुना अधिक होगी। अगले दो दशकों तक पुनर्चक्रित धातु ज़रूरत का केवल एक सीमित भाग पूरा कर सकती है, और नई खदानें फिर भी चाहिए होंगी। पुनर्चक्रण का असली मूल्य आगे है, "
  "जब उपयोग में बैटरियों का भंडार बड़ा हो और धीरे बढ़ रहा हो -- इसीलिए संयंत्र और संग्रह-व्यवस्थाएँ अभी बनानी होंगी, पुरानी बैटरियों की लहर आने से पहले।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage's turn is that recycling's 'arithmetic is slow' -- it can meet only a modest share of demand for two decades -- yet its plants must be built now for the later wave. "
   "It says new mines 'will still be required', so recycling will not end mining soon; it says the metals outlast the battery, not that batteries are useless; storing old batteries for better prices is never suggested.",
   "परिच्छेद का मोड़ यह है कि पुनर्चक्रण का 'गणित धीमा है' -- दो दशकों तक यह माँग का केवल सीमित भाग पूरा कर सकता है -- फिर भी बाद की लहर के लिए इसके संयंत्र अभी बनाने होंगे। "
   "वह कहता है कि नई खदानें 'फिर भी चाहिए होंगी', इसलिए पुनर्चक्रण जल्दी खनन समाप्त नहीं करेगा; वह कहता है कि धातुएँ बैटरी से अधिक टिकती हैं, यह नहीं कि बैटरियाँ बेकार हैं; बेहतर दाम के लिए पुरानी बैटरियाँ रखने का सुझाव कहीं नहीं है।",
   "crux",
   opts=["Recycling cannot meet demand soon, but its capacity must be built in advance.",
         "Recycling will soon end the need to open new mines for lithium, nickel and cobalt.",
         "Electric car batteries wear out too quickly to be worth making.",
         "Old batteries should be stored until the prices of the metals inside them have risen."],
   opts_hi=["पुनर्चक्रण जल्दी माँग पूरी नहीं कर सकता, पर उसकी क्षमता पहले से बनानी होगी।",
            "पुनर्चक्रण जल्दी ही लिथियम, निकल और कोबाल्ट के लिए नई खदानें खोलने की ज़रूरत समाप्त कर देगा।",
            "इलेक्ट्रिक कार की बैटरियाँ इतनी जल्दी घिस जाती हैं कि उन्हें बनाना व्यर्थ है।",
            "पुरानी बैटरियों को तब तक रखना चाहिए जब तक उनमें मौजूद धातुओं के दाम न बढ़ जाएँ।"],
   ans=0, pos=3)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Only 2 is valid. The cars retiring in 2035 are those sold around 2025, about a decade earlier, so the supply of recycled metal in a year tracks the batteries sold some ten years before. "
   "1 contradicts the passage, which says new mines 'will still be required' for the next two decades.",
   "केवल 2 वैध है। 2035 में हटने वाली कारें वे हैं जो लगभग 2025 में, यानी लगभग एक दशक पहले, बिकी थीं, इसलिए किसी वर्ष पुनर्चक्रित धातु की आपूर्ति लगभग दस वर्ष पहले बिकी बैटरियों पर निर्भर करती है। "
   "1 परिच्छेद का खंडन करता है, जो कहता है कि अगले दो दशकों तक नई खदानें 'फिर भी चाहिए होंगी'।",
   "conclusions",
   st=["Once recycling plants are built, mining for these minerals can stop.",
       "The amount of recycled battery metal available in a year depends on the number of batteries sold about a decade earlier."],
   st_hi=["पुनर्चक्रण संयंत्र बन जाने पर इन खनिजों का खनन बंद हो सकता है।",
          "किसी वर्ष उपलब्ध पुनर्चक्रित बैटरी धातु की मात्रा लगभग एक दशक पहले बिकी बैटरियों की संख्या पर निर्भर करती है।"],
   key=1)
RQ(p, "Assumption", "hard", "sc", ASSUME, ASSUME_HI,
   "Only 1 is assumed. Urging that the plants and collection systems 'have to be built now, before the wave of old batteries arrives' makes sense only if they take years to set up. "
   "2 would undercut the passage's own case, which assumes today's metals will still be wanted; 3 is never stated or needed -- the argument is about how much metal recycling can supply, not its price.",
   "केवल 1 पूर्वधारणा है। यह आग्रह कि संयंत्र और संग्रह-व्यवस्थाएँ 'अभी बनानी होंगी, पुरानी बैटरियों की लहर आने से पहले', तभी अर्थपूर्ण है जब उन्हें खड़ा करने में वर्षों लगें। "
   "2 परिच्छेद के अपने तर्क को कमज़ोर करेगा, जो मानता है कि आज की धातुओं की ज़रूरत बनी रहेगी; 3 न कहीं कहा गया है न आवश्यक है -- तर्क इस बारे में है कि पुनर्चक्रण कितनी धातु दे सकता है, उसके दाम के बारे में नहीं।",
   "assumptions",
   st=["Recycling plants and battery collection systems take years to set up.",
       "Battery designs will change so much that today's metals will no longer be needed.",
       "Recycled metal is cheaper than newly mined metal."],
   st_hi=["पुनर्चक्रण संयंत्र और बैटरी संग्रह-व्यवस्थाएँ खड़ी करने में वर्षों लगते हैं।",
          "बैटरियों की बनावट इतनी बदलेगी कि आज की धातुओं की ज़रूरत नहीं रहेगी।",
          "पुनर्चक्रित धातु नई खोदी गई धातु से सस्ती है।"],
   opts=["1 only", "1 and 3 only", "2 and 3 only", "1, 2 and 3"], key=0)

# ------------------------------------------------------------------ P06 pollinators (3)
p = passage("p06",
  "About three-quarters of the world's leading food crops depend to some degree on animal pollinators, mostly bees. Their decline -- from habitat loss, pesticides and disease -- is often described as a coming collapse "
  "of the food supply, but the reality is more uneven. Staple cereals such as wheat, rice and maize are pollinated by the wind or by their own flowers, and would be little affected. What is at risk is the variety and nutrition of diets: fruits, "
  "vegetables, nuts and oilseeds, which supply much of our vitamins and minerals, depend heavily on pollinators. Farmers can rent hives, and in some places workers now pollinate fruit trees by hand, but such substitutes "
  "are costly and slow. Hedgerows, flowering strips and careful use of pesticides keep wild pollinators on the farm at a fraction of the price.",
  "दुनिया की प्रमुख खाद्य फ़सलों में से लगभग तीन-चौथाई किसी न किसी हद तक जंतु परागणकर्ताओं, अधिकतर मधुमक्खियों, पर निर्भर हैं। उनकी कमी -- आवास के नष्ट होने, कीटनाशकों और रोगों से -- को प्रायः खाद्य आपूर्ति के आने वाले "
  "पतन के रूप में बताया जाता है, पर वास्तविकता अधिक असमान है। गेहूँ, चावल और मक्का जैसे मुख्य अनाज हवा से या अपने ही फूलों से परागित होते हैं, और उन पर बहुत कम असर पड़ेगा। ख़तरे में भोजन की विविधता और पोषण है: फल, "
  "सब्ज़ियाँ, मेवे और तिलहन, जो हमारे विटामिनों और खनिजों का बड़ा भाग देते हैं, परागणकर्ताओं पर बहुत निर्भर हैं। किसान छत्ते किराये पर ले सकते हैं, और कुछ जगहों पर अब मज़दूर हाथ से फलों के पेड़ों का परागण करते हैं, पर ऐसे विकल्प "
  "महँगे और धीमे हैं। झाड़ियों की बाड़ें, फूलों की पट्टियाँ और कीटनाशकों का सावधान उपयोग जंगली परागणकर्ताओं को खेत पर बहुत कम लागत में बनाए रखते हैं।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage corrects the 'collapse' story: staple grains do not need animal pollinators, so the real risk is to the variety and nutrition of diets. "
   "The 'collapse' option repeats the very view the passage disputes; renting hives reverses its advice, which favours keeping wild pollinators over costly substitutes; and saying that wheat, rice and maize need pollinators contradicts its statement that they are pollinated by the wind or by their own flowers.",
   "परिच्छेद 'पतन' वाली कहानी को सुधारता है: मुख्य अनाजों को जंतु परागणकर्ताओं की ज़रूरत नहीं, इसलिए असली ख़तरा भोजन की विविधता और पोषण को है। "
   "आपूर्ति ढहने वाली बात वही दृष्टिकोण दोहराती है जिस पर परिच्छेद आपत्ति करता है; छत्ते किराये पर लेने की बात उसकी सलाह को उलट देती है, जो महँगे विकल्पों के बजाय जंगली परागणकर्ताओं को बनाए रखने के पक्ष में है; और यह कहना कि गेहूँ, चावल और मक्का को परागणकर्ता चाहिए, उसके इस कथन का खंडन करता है कि वे हवा से या अपने ही फूलों से परागित होते हैं।",
   "crux",
   opts=["Pollinator loss threatens the quality of diets more than the supply of staples.",
         "The decline of pollinators will soon cause a collapse of the world's supply of food grains.",
         "Farmers should rent hives of bees instead of relying on wild pollinators near their fields.",
         "Wheat, rice and maize need animal pollinators in order to produce grain."],
   opts_hi=["परागणकर्ताओं की कमी मुख्य अनाजों की आपूर्ति से अधिक भोजन की गुणवत्ता के लिए ख़तरा है।",
            "परागणकर्ताओं की कमी से जल्दी ही दुनिया की खाद्यान्न आपूर्ति ढह जाएगी।",
            "किसानों को अपने खेतों के पास के जंगली परागणकर्ताओं पर निर्भर रहने के बजाय मधुमक्खियों के छत्ते किराये पर लेने चाहिए।",
            "गेहूँ, चावल और मक्का को अनाज पैदा करने के लिए जंतु परागणकर्ताओं की ज़रूरत है।"],
   ans=0, pos=1)
RQ(p, "Specific Detail", "medium", "mcq",
   "Which one of the following statements is NOT correct according to the passage?",
   "परिच्छेद के अनुसार निम्नलिखित में से कौन-सा कथन सही नहीं है?",
   "The passage says hand pollination and rented hives are substitutes that are 'costly and slow', so calling hand pollination cheap is the statement it does not support. "
   "It does name habitat loss, pesticides and disease as causes of decline, say that wheat, rice and maize would be little affected because they do not need animals, and say that fruits, vegetables, nuts and oilseeds supply much of our vitamins and minerals.",
   "परिच्छेद कहता है कि हाथ से परागण और किराये के छत्ते 'महँगे और धीमे' विकल्प हैं, इसलिए हाथ से परागण को सस्ता बताना वह कथन है जिसका वह समर्थन नहीं करता। "
   "वह आवास का नष्ट होना, कीटनाशक और रोग कमी के कारण बताता है, कहता है कि गेहूँ, चावल और मक्का को जंतुओं की ज़रूरत नहीं, इसलिए उन पर बहुत कम असर पड़ेगा, और कहता है कि फल, सब्ज़ियाँ, मेवे और तिलहन हमारे विटामिनों और खनिजों का बड़ा भाग देते हैं।",
   "not-correct",
   opts=["Hand pollination is a cheap substitute for bees.",
         "Habitat loss, pesticides and disease have contributed to the decline of pollinators.",
         "Wheat, rice and maize do not depend on animal pollinators.",
         "Fruits, vegetables, nuts and oilseeds supply much of our vitamins and minerals."],
   opts_hi=["हाथ से परागण मधुमक्खियों का एक सस्ता विकल्प है।",
            "आवास के नष्ट होने, कीटनाशकों और रोगों ने परागणकर्ताओं की कमी में योगदान दिया है।",
            "गेहूँ, चावल और मक्का जंतु परागणकर्ताओं पर निर्भर नहीं हैं।",
            "फल, सब्ज़ियाँ, मेवे और तिलहन हमारे विटामिनों और खनिजों का बड़ा भाग देते हैं।"],
   ans=0, pos=2)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Both are valid. Hedgerows, flowering strips and careful pesticide use keep wild pollinators 'at a fraction of the price' of rented hives and hand pollination (1). "
   "Since fruits, vegetables, nuts and oilseeds supply much of our vitamins and minerals and depend heavily on pollinators, fewer pollinators can mean less of those nutrients in diets (2).",
   "दोनों वैध हैं। झाड़ियों की बाड़ें, फूलों की पट्टियाँ और कीटनाशकों का सावधान उपयोग जंगली परागणकर्ताओं को किराये के छत्तों और हाथ से परागण की 'बहुत कम लागत में' बनाए रखते हैं (1)। "
   "चूँकि फल, सब्ज़ियाँ, मेवे और तिलहन हमारे विटामिनों और खनिजों का बड़ा भाग देते हैं और परागणकर्ताओं पर बहुत निर्भर हैं, कम परागणकर्ताओं का अर्थ भोजन में इन पोषक तत्वों की कमी हो सकता है (2)।",
   "conclusions",
   st=["Keeping wild pollinators on farms can cost less than paying for substitutes.",
       "A fall in pollinators could reduce the supply of vitamins and minerals in people's diets."],
   st_hi=["जंगली परागणकर्ताओं को खेतों पर बनाए रखना विकल्पों पर ख़र्च करने से सस्ता पड़ सकता है।",
          "परागणकर्ताओं की कमी से लोगों के भोजन में विटामिनों और खनिजों की आपूर्ति घट सकती है।"],
   key=2)

# ------------------------------------------------------------------ P07 courts and mediation (3)
p = passage("p07",
  "Courts in India carry a backlog of tens of millions of cases, and the usual remedy proposed is more judges. Judges matter, but the backlog is not only a question of numbers. A large share of pending cases are disputes "
  "that need not have reached a courtroom: cheques that bounced, quarrels over small debts, family disagreements that hardened into litigation. Mediation, in which a neutral person helps the parties reach their own settlement, "
  "can resolve many of these in weeks, and settlements that the parties have agreed to are complied with more often than orders imposed on them. Yet mediation is still treated as an optional detour rather than the normal "
  "first step. Making it the default for suitable disputes, with courts kept for those that genuinely need a judge, would do more for the backlog than any realistic increase in the number of judges.",
  "भारत की अदालतों पर करोड़ों मामलों का बोझ है, और प्रायः सुझाया जाने वाला उपाय अधिक न्यायाधीश हैं। न्यायाधीश महत्त्वपूर्ण हैं, पर लंबित मामले केवल संख्या का प्रश्न नहीं हैं। लंबित मामलों का बड़ा भाग ऐसे विवादों का है "
  "जिन्हें अदालत तक पहुँचना ही नहीं चाहिए था: बाउंस हुए चेक, छोटे कर्ज़ों के झगड़े, पारिवारिक मतभेद जो मुक़दमेबाज़ी में बदल गए। मध्यस्थता, जिसमें एक तटस्थ व्यक्ति पक्षों को अपना समझौता करने में मदद करता है, "
  "इनमें से कई को सप्ताहों में सुलझा सकती है, और पक्षों द्वारा स्वीकार किए गए समझौतों का पालन उन पर थोपे गए आदेशों से अधिक बार होता है। फिर भी मध्यस्थता को अब भी सामान्य पहले कदम के बजाय एक वैकल्पिक मोड़ माना जाता है। "
  "उपयुक्त विवादों के लिए इसे सामान्य नियम बनाना, और अदालतों को उन मामलों के लिए रखना जिन्हें सचमुच न्यायाधीश चाहिए, लंबित मामलों के लिए न्यायाधीशों की संख्या में किसी भी व्यावहारिक वृद्धि से अधिक करेगा।")
RQ(p, "Best Summary", "medium", "mcq", MSG, MSG_HI,
   "The passage concludes that making mediation the default for suitable disputes 'would do more for the backlog than any realistic increase in the number of judges'. "
   "More judges is the usual remedy it questions; it limits mediation to 'suitable disputes', keeping courts for the rest; and family quarrels are only one of its examples, not most of the backlog.",
   "परिच्छेद का निष्कर्ष है कि उपयुक्त विवादों के लिए मध्यस्थता को सामान्य नियम बनाना 'लंबित मामलों के लिए न्यायाधीशों की संख्या में किसी भी व्यावहारिक वृद्धि से अधिक करेगा'। "
   "अधिक न्यायाधीश वही सामान्य उपाय है जिस पर वह प्रश्न उठाता है; वह मध्यस्थता को 'उपयुक्त विवादों' तक सीमित रखता है और बाक़ी के लिए अदालतें रखता है; और पारिवारिक झगड़े उसके उदाहरणों में से केवल एक हैं, लंबित मामलों का अधिकांश नहीं।",
   "message",
   opts=["Default mediation for suitable disputes would ease the backlog more than extra judges.",
         "India needs many more judges, since only judges can clear a backlog of tens of millions of cases.",
         "Mediation should replace the courts for every kind of dispute, large or small, civil or criminal.",
         "Most of the cases in Indian courts concern quarrels within families."],
   opts_hi=["उपयुक्त विवादों में मध्यस्थता को सामान्य नियम बनाना अधिक न्यायाधीशों से ज़्यादा कारगर होगा।",
            "भारत को कहीं अधिक न्यायाधीश चाहिए, क्योंकि केवल न्यायाधीश ही करोड़ों लंबित मामले निपटा सकते हैं।",
            "छोटे-बड़े, दीवानी या फ़ौजदारी, हर प्रकार के विवाद के लिए मध्यस्थता को अदालतों की जगह लेनी चाहिए।",
            "भारतीय अदालतों के अधिकांश मामले परिवारों के भीतर के झगड़ों के हैं।"],
   ans=0, pos=3)
RQ(p, "Assumption", "hard", "s2", ASSUME, ASSUME_HI,
   "Only 1 is assumed. Making mediation the default can cut the backlog only if many disputants would actually take part, and settle, when it is the normal first step. "
   "2 is the opposite of the passage, which keeps courts for disputes 'that genuinely need a judge'.",
   "केवल 1 पूर्वधारणा है। मध्यस्थता को सामान्य नियम बनाना लंबित मामले तभी घटा सकता है जब बहुत-से पक्ष, उसके सामान्य पहला कदम होने पर, वास्तव में उसमें भाग लें और समझौता करें। "
   "2 परिच्छेद के उलट है, जो अदालतों को उन विवादों के लिए रखता है 'जिन्हें सचमुच न्यायाधीश चाहिए'।",
   "assumptions",
   st=["Many disputants would take part in mediation if it were the normal first step.",
       "Judges are not needed for any kind of dispute."],
   st_hi=["यदि मध्यस्थता सामान्य पहला कदम हो तो बहुत-से पक्ष उसमें भाग लेंगे।",
          "किसी भी प्रकार के विवाद के लिए न्यायाधीशों की ज़रूरत नहीं है।"],
   key=0)
RQ(p, "Inference", "medium", "sc", INFER, INFER_HI,
   "1 and 3 follow: the passage calls many pending cases disputes 'that need not have reached a courtroom' (1), and says mediation can resolve many of them 'in weeks' (3). "
   "2 contradicts its point that the backlog 'is not only a question of numbers'.",
   "1 और 3 निकलते हैं: परिच्छेद बहुत-से लंबित मामलों को ऐसे विवाद बताता है 'जिन्हें अदालत तक पहुँचना ही नहीं चाहिए था' (1), और कहता है कि मध्यस्थता उनमें से कई को 'सप्ताहों में' सुलझा सकती है (3)। "
   "2 उसकी इस बात का खंडन करता है कि लंबित मामले 'केवल संख्या का प्रश्न नहीं हैं'।",
   "inferences",
   st=["Some of the pending cases could have been settled without a judge.",
       "Adding judges would by itself clear the backlog.",
       "Mediation can settle suitable disputes faster than a trial in court."],
   st_hi=["कुछ लंबित मामले न्यायाधीश के बिना निपटाए जा सकते थे।",
          "न्यायाधीश बढ़ाने भर से लंबित मामले निपट जाएँगे।",
          "मध्यस्थता उपयुक्त विवादों को अदालत में सुनवाई से जल्दी निपटा सकती है।"],
   opts=["2 only", "1 and 3 only", "1 and 2 only", "1, 2 and 3"], key=1)

# ------------------------------------------------------------------ P08 music teaching (2)
p = passage("p08",
  "For centuries Indian classical music passed from teacher to student by imitation and repetition, the student living close to the teacher and absorbing not only the notes but the manner of their delivery. "
  "Recordings and online lessons have opened that knowledge to anyone with a phone, and many musicians now learn their first steps from a screen. Teachers worry that something is lost: a recording can show what a master sang, "
  "but it cannot correct what the student sings back. The worry is reasonable, but it may be overstated. The old system admitted only those who could afford years beside a master; recordings have widened the circle of "
  "listeners and learners, and the best students still seek a teacher once the screen has taken them as far as it can.",
  "सदियों तक भारतीय शास्त्रीय संगीत अनुकरण और अभ्यास से गुरु से शिष्य तक पहुँचा, जिसमें शिष्य गुरु के पास रहकर केवल स्वर ही नहीं, उन्हें गाने का ढंग भी आत्मसात करता था। "
  "रिकॉर्डिंग और ऑनलाइन पाठों ने यह ज्ञान फ़ोन रखने वाले हर व्यक्ति के लिए खोल दिया है, और अब बहुत-से संगीतकार अपने पहले कदम स्क्रीन से सीखते हैं। गुरुओं को चिंता है कि कुछ खो रहा है: रिकॉर्डिंग दिखा सकती है कि किसी उस्ताद ने क्या गाया, "
  "पर वह यह नहीं सुधार सकती कि शिष्य बदले में क्या गाता है। यह चिंता उचित है, पर शायद बढ़ा-चढ़ाकर कही गई है। पुरानी व्यवस्था में केवल वही आ पाते थे जो किसी उस्ताद के पास वर्षों बिताने का ख़र्च उठा सकें; रिकॉर्डिंग ने "
  "सुनने और सीखने वालों का दायरा बढ़ाया है, और सबसे अच्छे शिष्य, स्क्रीन उन्हें जहाँ तक ले जा सकती है वहाँ तक पहुँचकर, फिर भी गुरु खोजते हैं।")
RQ(p, "Specific Detail", "easy", "s2",
   "According to the passage, which of the following is/are correct?",
   "परिच्छेद के अनुसार निम्नलिखित में से कौन-सा/से सही है/हैं?",
   "Only 2 is stated: a recording can show what a master sang 'but it cannot correct what the student sings back'. 1 reverses the passage's last sentence: the best students 'still seek a teacher' once the screen has taken them as far as it can.",
   "केवल 2 कहा गया है: रिकॉर्डिंग दिखा सकती है कि उस्ताद ने क्या गाया, 'पर वह यह नहीं सुधार सकती कि शिष्य बदले में क्या गाता है'। 1 परिच्छेद के अंतिम वाक्य को उलट देता है: सबसे अच्छे शिष्य, स्क्रीन जहाँ तक ले जाए वहाँ तक पहुँचकर, 'फिर भी गुरु खोजते हैं'।",
   "statements",
   st=["Recordings have made teachers unnecessary for serious students.",
       "A recording cannot correct the mistakes a student makes in singing."],
   st_hi=["रिकॉर्डिंग ने गंभीर शिष्यों के लिए गुरुओं को अनावश्यक बना दिया है।",
          "रिकॉर्डिंग शिष्य द्वारा गाने में की गई ग़लतियाँ नहीं सुधार सकती।"],
   key=1)
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage accepts the teachers' worry as reasonable but 'overstated': recordings have widened access, and serious students still go on to a teacher. "
   "It does not say online lessons destroyed the tradition, that only resident students can learn, or that teaching should move entirely to recordings.",
   "परिच्छेद गुरुओं की चिंता को उचित पर 'बढ़ा-चढ़ाकर कही गई' मानता है: रिकॉर्डिंग ने पहुँच बढ़ाई है, और गंभीर शिष्य आगे गुरु के पास जाते ही हैं। "
   "वह यह नहीं कहता कि ऑनलाइन पाठों ने परंपरा नष्ट कर दी, कि केवल गुरु के पास रहने वाले ही सीख सकते हैं, या कि शिक्षण पूरी तरह रिकॉर्डिंग पर चला जाना चाहिए।",
   "crux",
   opts=["Recordings widen access to classical music but leave a role for teachers.",
         "Online lessons and recordings have destroyed the traditional way of teaching classical music.",
         "Only those who live with a teacher for years can truly learn classical music.",
         "Classical music should now be taught only through recordings."],
   opts_hi=["रिकॉर्डिंग शास्त्रीय संगीत तक पहुँच बढ़ाती है, पर गुरुओं की भूमिका बनी रहती है।",
            "ऑनलाइन पाठों और रिकॉर्डिंग ने शास्त्रीय संगीत सिखाने का पारंपरिक तरीका नष्ट कर दिया है।",
            "केवल वही शास्त्रीय संगीत सचमुच सीख सकते हैं जो वर्षों गुरु के साथ रहें।",
            "शास्त्रीय संगीत अब केवल रिकॉर्डिंग से सिखाया जाना चाहिए।"],
   ans=0, pos=2)

# ------------------------------------------------------------------ P09 consent and privacy (3)
p = passage("p09",
  "Every app asks for consent, and almost everyone gives it. A user who installs ten apps in a month would need hours to read their privacy policies, written in language few lawyers enjoy, so she clicks 'agree' and moves on. "
  "Consent obtained this way protects the company more than the user: it turns the collection of data into something the user is said to have chosen. Some regulators have begun to shift the burden. Instead of asking users "
  "to police every request, they set limits that apply whatever the user clicks -- data may be collected only for a stated purpose, kept only as long as needed, and not sold on. Consent still matters for choices people "
  "can actually weigh, but it cannot carry the whole weight of protecting privacy.",
  "हर ऐप सहमति माँगता है, और लगभग हर व्यक्ति दे देता है। एक महीने में दस ऐप डालने वाली उपयोगकर्ता को उनकी निजता नीतियाँ पढ़ने में घंटों लगेंगे, जो ऐसी भाषा में लिखी हैं जिसे बहुत कम वकील पसंद करते हैं, इसलिए वह 'सहमत' दबाकर आगे बढ़ जाती है। "
  "इस तरह ली गई सहमति उपयोगकर्ता से अधिक कंपनी की रक्षा करती है: वह आँकड़ों के संग्रह को ऐसी चीज़ बना देती है जिसे उपयोगकर्ता ने कथित रूप से चुना। कुछ नियामकों ने यह भार बदलना शुरू किया है। उपयोगकर्ताओं से "
  "हर अनुरोध की निगरानी करने को कहने के बजाय वे ऐसी सीमाएँ तय करते हैं जो उपयोगकर्ता चाहे जो दबाए, लागू होती हैं -- आँकड़े केवल बताए गए उद्देश्य के लिए लिए जा सकते हैं, केवल आवश्यकता तक रखे जा सकते हैं, और आगे बेचे नहीं जा सकते। "
  "जिन विकल्पों को लोग सचमुच तौल सकें उनके लिए सहमति अब भी महत्त्वपूर्ण है, पर निजता की रक्षा का पूरा भार वह नहीं उठा सकती।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage argues that click-through consent cannot carry the load, and favours limits that apply 'whatever the user clicks', while keeping consent for choices people can weigh. "
   "Asking users to read every policy is the burden the passage wants lifted; it keeps a role for consent, so 'stop asking' overreaches; and it never says policies are written to confuse.",
   "परिच्छेद का तर्क है कि क्लिक करके दी गई सहमति यह भार नहीं उठा सकती, और ऐसी सीमाओं के पक्ष में है जो 'उपयोगकर्ता चाहे जो दबाए' लागू हों, जबकि सहमति को उन विकल्पों के लिए रखता है जिन्हें लोग तौल सकें। "
   "उपयोगकर्ताओं से हर नीति पढ़ने को कहना वही भार है जिसे परिच्छेद हटाना चाहता है; वह सहमति के लिए भूमिका रखता है, इसलिए 'माँगना बंद करो' बहुत आगे जाता है; और वह कहीं नहीं कहता कि नीतियाँ भ्रमित करने के लिए लिखी जाती हैं।",
   "crux",
   opts=["Privacy needs rules that apply whatever users agree to, not consent alone.",
         "Users should take the time to read every privacy policy before agreeing to it.",
         "Apps should stop asking their users for consent altogether.",
         "Privacy policies are deliberately written by lawyers to confuse the people who read them."],
   opts_hi=["निजता के लिए केवल सहमति नहीं, ऐसे नियम चाहिए जो सहमति कुछ भी हो, लागू हों।",
            "उपयोगकर्ताओं को सहमति देने से पहले समय निकालकर हर निजता नीति पूरी पढ़नी चाहिए।",
            "ऐप्स को अपने उपयोगकर्ताओं से सहमति माँगना पूरी तरह बंद कर देना चाहिए।",
            "निजता नीतियाँ वकील जान-बूझकर ऐसी लिखते हैं कि उन्हें पढ़ने वाले लोग भ्रमित हो जाएँ।"],
   ans=0, pos=1)
RQ(p, "Inference", "hard", "sc", INFER, INFER_HI,
   "1 and 2 follow. Policies that take 'hours' to read in difficult language lead users to click 'agree' and move on (1). A limit that data be kept 'only as long as needed' applies 'whatever the user clicks', so it protects even someone who never read the policy (2). "
   "3 contradicts the passage, which says consent 'still matters for choices people can actually weigh'.",
   "1 और 2 निकलते हैं। कठिन भाषा में लिखी और पढ़ने में 'घंटों' लेने वाली नीतियाँ उपयोगकर्ताओं को 'सहमत' दबाकर आगे बढ़ने पर विवश करती हैं (1)। आँकड़े 'केवल आवश्यकता तक' रखने की सीमा 'उपयोगकर्ता चाहे जो दबाए' लागू होती है, इसलिए यह उस व्यक्ति की भी रक्षा करती है जिसने नीति कभी नहीं पढ़ी (2)। "
   "3 परिच्छेद का खंडन करता है, जो कहता है कि सहमति 'जिन विकल्पों को लोग सचमुच तौल सकें उनके लिए अब भी महत्त्वपूर्ण है'।",
   "inferences",
   st=["The length and language of privacy policies discourage users from reading them.",
       "A limit on how long data may be kept protects users who never read the policy.",
       "Consent has no place at all in protecting privacy."],
   st_hi=["निजता नीतियों की लंबाई और भाषा उपयोगकर्ताओं को उन्हें पढ़ने से हतोत्साहित करती है।",
          "आँकड़े कितने समय तक रखे जा सकते हैं, इसकी सीमा उन उपयोगकर्ताओं की भी रक्षा करती है जिन्होंने नीति कभी नहीं पढ़ी।",
          "निजता की रक्षा में सहमति का कोई स्थान नहीं है।"],
   opts=["1 only", "1 and 3 only", "1 and 2 only", "1, 2 and 3"], key=2)
RQ(p, "Assumption", "hard", "s2", ASSUME, ASSUME_HI,
   "Neither is assumed. 1 is the opposite of the passage's premise: users click 'agree' without reading policies that would take hours. "
   "2 is not needed either: the argument is that consent gathered this way protects the company, which would not matter if companies never misused data -- so the passage, if anything, assumes the reverse.",
   "कोई भी पूर्वधारणा नहीं है। 1 परिच्छेद के आधार-वाक्य के उलट है: उपयोगकर्ता घंटों में पढ़ी जाने वाली नीतियाँ पढ़े बिना 'सहमत' दबा देते हैं। "
   "2 की भी ज़रूरत नहीं: तर्क यह है कि इस तरह ली गई सहमति कंपनी की रक्षा करती है, जो तब मायने नहीं रखती यदि कंपनियाँ कभी आँकड़ों का दुरुपयोग न करतीं -- इसलिए परिच्छेद, यदि कुछ मानता है, तो इसका उलटा मानता है।",
   "assumptions",
   st=["Most users understand the privacy policies they agree to.",
       "Companies never misuse the data that users allow them to collect."],
   st_hi=["अधिकांश उपयोगकर्ता उन निजता नीतियों को समझते हैं जिन पर वे सहमति देते हैं।",
          "कंपनियाँ उपयोगकर्ताओं द्वारा अनुमत आँकड़ों का कभी दुरुपयोग नहीं करतीं।"],
   key=3)

# ------------------------------------------------------------------ P10 old-age care (3)
p = passage("p10",
  "India's population is still young on average, but the number of people over sixty is growing faster than any other age group and will roughly double in the next quarter-century. Much of their care is given today by "
  "women in the family, unpaid and uncounted. As families shrink, as more women take paid work and as children move to distant cities, that arrangement will strain. Paid care -- nurses, attendants, day-care centres for the old -- "
  "will have to grow, and it could become a large source of jobs, many of them for women. Whether those jobs are decent depends on choices made now: training and certifying care workers, setting standards for agencies, "
  "and counting care work in the statistics that guide policy.",
  "भारत की जनसंख्या औसतन अब भी युवा है, पर साठ वर्ष से अधिक आयु के लोगों की संख्या किसी भी अन्य आयु-वर्ग से तेज़ी से बढ़ रही है और अगले पच्चीस वर्षों में लगभग दोगुनी हो जाएगी। आज उनकी अधिकांश देखभाल परिवार की महिलाएँ करती हैं, "
  "बिना वेतन और बिना गिनती के। जैसे-जैसे परिवार छोटे होंगे, अधिक महिलाएँ वेतन वाला काम करेंगी और बच्चे दूर के शहरों में जाएँगे, यह व्यवस्था दबाव में आएगी। वेतन वाली देखभाल -- नर्सें, परिचारक, बुज़ुर्गों के लिए दिवा-देखभाल केंद्र -- "
  "को बढ़ना होगा, और यह रोज़गार का एक बड़ा स्रोत बन सकती है, जिनमें से कई महिलाओं के लिए होंगे। ये रोज़गार सम्मानजनक होंगे या नहीं, यह अभी किए गए चुनावों पर निर्भर है: देखभाल कर्मियों का प्रशिक्षण और प्रमाणन, एजेंसियों के लिए मानक तय करना, "
  "और नीति का मार्गदर्शन करने वाले आँकड़ों में देखभाल के काम की गिनती करना।")
RQ(p, "Best Summary", "medium", "mcq", MSG, MSG_HI,
   "The passage expects paid care to grow as family care strains, and says whether the new jobs are decent 'depends on choices made now' -- training, standards and counting care work. "
   "It does not ask women to keep caring at home or families to stay put; and it says the over-sixties are the fastest-growing group in India, not that India is ageing faster than every other country.",
   "परिच्छेद को उम्मीद है कि पारिवारिक देखभाल पर दबाव बढ़ने से वेतन वाली देखभाल बढ़ेगी, और कहता है कि नए रोज़गार सम्मानजनक होंगे या नहीं, यह 'अभी किए गए चुनावों पर निर्भर है' -- प्रशिक्षण, मानक और देखभाल के काम की गिनती। "
   "वह न महिलाओं से घर पर देखभाल जारी रखने को कहता है, न परिवारों से एक जगह टिके रहने को; और वह कहता है कि साठ से अधिक आयु वाले भारत में सबसे तेज़ी से बढ़ने वाला वर्ग हैं, यह नहीं कि भारत हर दूसरे देश से तेज़ी से बूढ़ा हो रहा है।",
   "message",
   opts=["Care for the old can become decent work if it is trained, regulated and counted.",
         "Women should go on caring for their elderly relatives at home, as they have always done.",
         "India's population is ageing faster than that of any other country in the world today.",
         "Families should be discouraged from moving to distant cities."],
   opts_hi=["बुज़ुर्गों की देखभाल सम्मानजनक रोज़गार बन सकती है, यदि उसका प्रशिक्षण, विनियमन और गिनती हो।",
            "महिलाओं को पहले की तरह घर पर ही अपने बुज़ुर्ग संबंधियों की देखभाल करते रहना चाहिए।",
            "भारत की जनसंख्या आज दुनिया के किसी भी अन्य देश की जनसंख्या की तुलना में तेज़ी से बूढ़ी हो रही है।",
            "परिवारों को दूर के शहरों में जाने से हतोत्साहित किया जाना चाहिए।"],
   ans=0, pos=2)
RQ(p, "Specific Detail", "easy", "mcq",
   "According to the passage, which of the following will put the present arrangement of care under strain?",
   "परिच्छेद के अनुसार निम्नलिखित में से क्या देखभाल की वर्तमान व्यवस्था पर दबाव डालेगा?",
   "The passage names three pressures: families shrinking, more women taking paid work, and children moving to distant cities. "
   "It says the number of people over sixty is rising, not falling; it does not mention the cost of nurses; and it does not speak of a rise in young people.",
   "परिच्छेद तीन दबाव बताता है: परिवारों का छोटा होना, अधिक महिलाओं का वेतन वाला काम करना, और बच्चों का दूर के शहरों में जाना। "
   "वह कहता है कि साठ से अधिक आयु वालों की संख्या बढ़ रही है, घट नहीं रही; वह नर्सों की लागत का उल्लेख नहीं करता; और वह युवाओं में वृद्धि की बात नहीं करता।",
   "detail",
   opts=["smaller families, women's paid work and children moving away",
         "a fall in the number of people who are over sixty years old",
         "the rising cost of hiring nurses and attendants in the cities",
         "a rise in the number of young people in the population"],
   opts_hi=["छोटे परिवार, महिलाओं का वेतन वाला काम और बच्चों का दूर जाना",
            "साठ वर्ष से अधिक आयु के लोगों की संख्या में कमी",
            "शहरों में नर्सों और परिचारकों को काम पर रखने की लगातार बढ़ती लागत",
            "जनसंख्या में युवाओं की संख्या में वृद्धि"],
   ans=0, pos=3)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Both are valid. Family care is described as 'unpaid and uncounted', and counting care work in 'the statistics that guide policy' is one of the choices proposed, so such work is not counted today (1). "
   "With the over-sixties doubling and family care under strain, the passage says paid care 'will have to grow' (2).",
   "दोनों वैध हैं। पारिवारिक देखभाल को 'बिना वेतन और बिना गिनती के' बताया गया है, और 'नीति का मार्गदर्शन करने वाले आँकड़ों' में देखभाल के काम की गिनती सुझाए गए चुनावों में से एक है, इसलिए आज ऐसे काम की गिनती नहीं होती (1)। "
   "साठ से अधिक आयु वालों के दोगुना होने और पारिवारिक देखभाल पर दबाव के साथ, परिच्छेद कहता है कि वेतन वाली देखभाल को 'बढ़ना होगा' (2)।",
   "conclusions",
   st=["Unpaid care work in families is not reflected in the statistics used to make policy.",
       "The demand for paid care is likely to grow."],
   st_hi=["परिवारों में बिना वेतन के देखभाल का काम नीति बनाने में प्रयुक्त आँकड़ों में नहीं दिखता।",
          "वेतन वाली देखभाल की माँग बढ़ने की संभावना है।"],
   key=2)
