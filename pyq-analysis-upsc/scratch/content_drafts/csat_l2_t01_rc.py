# -*- coding: utf-8 -*-
"""CSAT Level 2 · Test 1 -- Reading Comprehension: 10 passages, 28 items (8 passages with three items, 2 with two).

The passages are original, written for this series in the op-ed register of UPSC's own passages (playbook K.3):
city heat, antibiotics, gig work, libraries, crop choice, misinformation, coasts, sport, schooling and trust
in science. Item types follow K.2: main idea 7, inference 8, assumption 5, tone 1, specific detail 4, best
summary 3. The distractors use UPSC's RC traps (K.4): true but beyond the passage, the stronger-worded
paraphrase, the half-true option, the reversed cause, the view the author reports but does not hold, and
the assumption wider than the argument needs."""
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

# ------------------------------------------------------------------ P01 city heat (3)
p = passage("p01",
  "Cities are warmer than the countryside around them, and the gap is widest on still summer nights. Concrete and asphalt soak up heat through the day and give it back after dark, "
  "while the cooling that trees provide -- by shading the ground and by evaporating water from their leaves -- is missing. The poorest neighbourhoods, with the least green cover and the most tin roofs, "
  "often run several degrees hotter than leafy ones a few kilometres away. Planting trees is the obvious remedy, but a sapling planted today will not shade a street for a decade, and many plantation drives "
  "count the saplings planted rather than the trees that survive. Cool roofs painted in reflective white, and shaded bus stops, can lower temperatures within a single season. "
  "A heat plan that relies on trees alone is a plan for the next decade, not for the next summer.",
  "शहर अपने आसपास के ग्रामीण क्षेत्रों से अधिक गर्म होते हैं, और यह अंतर गर्मियों की शांत रातों में सबसे अधिक होता है। कंक्रीट और डामर दिन भर गर्मी सोखते हैं और अँधेरा होने पर उसे लौटाते हैं, "
  "जबकि पेड़ों से मिलने वाली ठंडक -- ज़मीन पर छाया करके और पत्तियों से पानी का वाष्पन करके -- वहाँ नहीं होती। सबसे ग़रीब बस्तियाँ, जहाँ हरियाली सबसे कम और टिन की छतें सबसे अधिक हैं, "
  "प्रायः कुछ किलोमीटर दूर की हरी-भरी बस्तियों से कई डिग्री अधिक गर्म रहती हैं। पेड़ लगाना स्पष्ट उपाय है, पर आज लगाया गया पौधा एक दशक तक किसी सड़क को छाया नहीं देगा, और कई वृक्षारोपण अभियान "
  "बचे हुए पेड़ों के बजाय लगाए गए पौधों की गिनती करते हैं। चमकदार सफ़ेद रंग से रँगी ठंडी छतें और छायादार बस-स्टॉप एक ही मौसम में तापमान घटा सकते हैं। "
  "केवल पेड़ों पर टिकी गर्मी-योजना अगले दशक की योजना है, अगली गर्मी की नहीं।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage grants that trees are 'the obvious remedy' but shows that they work slowly, and ends by saying that a plan relying on trees alone will not help the next summer; quick measures such as cool roofs "
   "must sit alongside them. Saying that planting trees does little contradicts the passage, which calls trees the obvious remedy. Blaming tin roofs makes one cause the main one: the passage names both missing green cover and tin roofs. "
   "Counting surviving trees is a detail the passage mentions in passing, not its central point.",
   "परिच्छेद मानता है कि पेड़ 'स्पष्ट उपाय' हैं, पर दिखाता है कि वे धीरे काम करते हैं, और अंत में कहता है कि केवल पेड़ों पर टिकी योजना अगली गर्मी में सहायता नहीं करेगी; ठंडी छतों जैसे जल्दी असर वाले उपाय "
   "उनके साथ चलने चाहिए। यह कहना कि पेड़ लगाने से बहुत कम लाभ होता है, परिच्छेद का खंडन करता है, जो पेड़ों को स्पष्ट उपाय कहता है। टिन की छतों को मुख्य कारण बताना एक कारण को मुख्य बना देता है: परिच्छेद हरियाली की कमी और टिन की छतें दोनों बताता है। "
   "बचे हुए पेड़ गिनने की बात एक ब्योरा है जिसका उल्लेख परिच्छेद चलते-चलते करता है, उसका केंद्रीय विचार नहीं।",
   "crux",
   opts=["Tree planting must be paired with measures that cool cities quickly.",
         "Planting trees does little to reduce heat in cities.",
         "Poor neighbourhoods are hotter than others mainly because of their tin roofs.",
         "Plantation drives should count surviving trees, not saplings planted."],
   opts_hi=["पेड़ लगाने के साथ ऐसे उपाय भी होने चाहिए जो शहरों को जल्दी ठंडा करें।",
            "पेड़ लगाने से शहरों की गर्मी बहुत कम घटती है।",
            "ग़रीब बस्तियाँ मुख्यतः अपनी टिन की छतों के कारण दूसरी बस्तियों से अधिक गर्म हैं।",
            "वृक्षारोपण अभियानों को लगाए गए पौधों के बजाय बचे हुए पेड़ गिनने चाहिए।"],
   ans=0, pos=3)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Both are valid. The passage says drives count saplings planted rather than trees that survive, so a drive that reports only plantings can overstate what it achieves (1). "
   "It says a sapling will not shade a street for a decade, while cool roofs can lower temperatures 'within a single season', so cool roofs act sooner (2).",
   "दोनों वैध हैं। परिच्छेद कहता है कि अभियान बचे हुए पेड़ों के बजाय लगाए गए पौधे गिनते हैं, इसलिए केवल रोपण बताने वाला अभियान अपनी उपलब्धि को बढ़ा-चढ़ाकर दिखा सकता है (1)। "
   "वह कहता है कि पौधा एक दशक तक सड़क को छाया नहीं देगा, जबकि ठंडी छतें 'एक ही मौसम में' तापमान घटा सकती हैं, इसलिए ठंडी छतें जल्दी असर करती हैं (2)।",
   "conclusions",
   st=["A plantation drive that reports only the saplings it planted may overstate its effect on city heat.",
       "Cool roofs can bring down temperatures sooner than newly planted trees can."],
   st_hi=["केवल लगाए गए पौधों की संख्या बताने वाला वृक्षारोपण अभियान शहर की गर्मी पर अपने असर को बढ़ा-चढ़ाकर दिखा सकता है।",
          "ठंडी छतें नए लगाए गए पेड़ों की तुलना में जल्दी तापमान घटा सकती हैं।"],
   key=2)
RQ(p, "Assumption", "hard", "s2", ASSUME, ASSUME_HI,
   "Only 1 is an assumption. The author faults a plan that serves 'the next decade, not the next summer', which makes sense only if relief in the coming summer is itself worth planning for. "
   "2 goes further than the passage: it says drives count plantings rather than survivors, not that most saplings die; the argument does not need that claim -- the wider-than-needed assumption trap.",
   "केवल 1 पूर्वधारणा है। लेखक ऐसी योजना की आलोचना करता है जो 'अगले दशक की, अगली गर्मी की नहीं' है, जो तभी अर्थपूर्ण है जब आने वाली गर्मी में राहत स्वयं योजना के योग्य हो। "
   "2 परिच्छेद से आगे जाता है: वह कहता है कि अभियान बचे पेड़ों के बजाय रोपण गिनते हैं, यह नहीं कि अधिकांश पौधे मर जाते हैं; तर्क को उस दावे की ज़रूरत नहीं -- यह आवश्यकता से व्यापक पूर्वधारणा का जाल है।",
   "assumptions",
   st=["Bringing down heat in the coming summer is worth planning for, and not only over the next decade.",
       "Most of the saplings planted in cities die before they can grow into trees."],
   st_hi=["आने वाली गर्मी में तापमान घटाना योजना के योग्य है, केवल अगले दशक में नहीं।",
          "शहरों में लगाए गए अधिकांश पौधे पेड़ बनने से पहले मर जाते हैं।"],
   key=0)

# ------------------------------------------------------------------ P02 antibiotics (3)
p = passage("p02",
  "In many Indian towns a person with a sore throat can walk into a chemist's shop and walk out with a course of antibiotics, no prescription asked. The habit is rarely reckless; "
  "it is often the cheapest and quickest way to get treatment where a visit to a doctor costs a day's wages. Yet every unneeded course gives the bacteria in the body another chance to evolve resistance, "
  "and resistant infections are slower and costlier to treat for everyone. Banning over-the-counter sales without making doctors easier to reach would simply push people towards unregulated sellers. "
  "The more lasting answer is to make the right choice the easy one: quick, cheap tests that tell a viral infection from a bacterial one, and primary clinics near enough that a prescription costs less "
  "than the antibiotic itself.",
  "भारत के कई कस्बों में गले में ख़राश वाला व्यक्ति किसी दवा की दुकान पर जाकर बिना पर्चे के एंटीबायोटिक दवाओं का पूरा कोर्स ले आता है। यह आदत शायद ही लापरवाही होती है; "
  "जहाँ डॉक्टर के पास जाने में एक दिन की मज़दूरी लगती है, वहाँ यह प्रायः इलाज का सबसे सस्ता और सबसे जल्दी मिलने वाला तरीका है। फिर भी हर अनावश्यक कोर्स शरीर के जीवाणुओं को प्रतिरोध विकसित करने का एक और अवसर देता है, "
  "और प्रतिरोधी संक्रमणों का इलाज सबके लिए धीमा और महँगा हो जाता है। डॉक्टरों तक पहुँच आसान बनाए बिना बिना-पर्चे की बिक्री पर रोक लगाने से लोग केवल अनियंत्रित विक्रेताओं की ओर धकेले जाएँगे। "
  "अधिक टिकाऊ उत्तर यह है कि सही विकल्प को आसान बनाया जाए: ऐसी जल्दी और सस्ती जाँचें जो वायरल संक्रमण को जीवाणु संक्रमण से अलग पहचान सकें, और इतने पास प्राथमिक क्लिनिक कि पर्चा स्वयं एंटीबायोटिक से सस्ता पड़े।")
RQ(p, "Best Summary", "medium", "mcq", MSG, MSG_HI,
   "The passage ends on its answer: make the right choice the easy one, through cheap tests and nearby clinics. The first distractor is the step the passage warns against, a ban without better access. "
   "The second contradicts the passage, which says the habit is 'rarely reckless'. The third reverses the passage's point that resistant infections are costlier 'for everyone', not only for those who misuse the drugs.",
   "परिच्छेद अपने उत्तर पर समाप्त होता है: सस्ती जाँचों और पास के क्लिनिकों से सही विकल्प को आसान बनाइए। पहला ग़लत विकल्प वही कदम है जिसके प्रति परिच्छेद चेताता है, बेहतर पहुँच के बिना रोक। "
   "दूसरा परिच्छेद का खंडन करता है, जो कहता है कि यह आदत 'शायद ही लापरवाही' है। तीसरा परिच्छेद की इस बात को उलट देता है कि प्रतिरोधी संक्रमण 'सबके लिए' महँगे हैं, केवल दुरुपयोग करने वालों के लिए नहीं।",
   "message",
   opts=["Antibiotic misuse will fall when proper diagnosis and care become easier to get.",
         "The sale of antibiotics without a prescription should be banned everywhere at once.",
         "People who buy antibiotics without a prescription are acting recklessly.",
         "Resistant infections mainly harm the people who misuse antibiotics themselves."],
   opts_hi=["सही जाँच और इलाज आसानी से मिलने लगें तो एंटीबायोटिक का दुरुपयोग घटेगा।",
            "बिना पर्चे के एंटीबायोटिक की बिक्री पर हर जगह तुरंत रोक लगा देनी चाहिए।",
            "बिना पर्चे के एंटीबायोटिक ख़रीदने वाले लोग लापरवाही से काम कर रहे हैं।",
            "प्रतिरोधी संक्रमण मुख्यतः उन्हीं लोगों को हानि पहुँचाते हैं जो एंटीबायोटिक का दुरुपयोग करते हैं।"],
   ans=0, pos=0)
RQ(p, "Inference", "hard", "sc", INFER, INFER_HI,
   "1 and 2 follow. The cost of a doctor's visit -- 'a day's wages' -- is given as the reason chemists are the cheapest route (1), and the passage says a ban without better access would push people towards "
   "unregulated sellers (2). 3 cannot be drawn: the passage wants tests that tell a viral infection from a bacterial one, which implies the opposite, that an antibiotic course for a viral infection is unneeded.",
   "1 और 2 निकलते हैं। डॉक्टर के पास जाने की लागत -- 'एक दिन की मज़दूरी' -- ही वह कारण बताया गया है जिससे दवा की दुकान सबसे सस्ता रास्ता है (1), और परिच्छेद कहता है कि बेहतर पहुँच के बिना रोक लोगों को "
   "अनियंत्रित विक्रेताओं की ओर धकेलेगी (2)। 3 नहीं निकाला जा सकता: परिच्छेद ऐसी जाँचें चाहता है जो वायरल संक्रमण को जीवाणु संक्रमण से अलग करें, जिसका अर्थ इसके उलट है, कि वायरल संक्रमण के लिए एंटीबायोटिक कोर्स अनावश्यक है।",
   "inferences",
   st=["The cost of seeing a doctor is one reason why people buy antibiotics directly from chemists.",
       "A ban on its own could shift sales to sellers who are even less regulated.",
       "Antibiotics are an effective treatment for viral infections."],
   st_hi=["डॉक्टर को दिखाने की लागत एक कारण है जिससे लोग सीधे दवा की दुकानों से एंटीबायोटिक ख़रीदते हैं।",
          "अकेली रोक बिक्री को ऐसे विक्रेताओं की ओर खिसका सकती है जिन पर और भी कम नियंत्रण है।",
          "एंटीबायोटिक वायरल संक्रमणों का प्रभावी इलाज हैं।"],
   opts=["1 only", "2 and 3 only", "1, 2 and 3", "1 and 2 only"], key=3)
RQ(p, "Author's Tone", "medium", "mcq",
   "The author's attitude towards people who buy antibiotics over the counter is best described as:",
   "बिना पर्चे के एंटीबायोटिक ख़रीदने वाले लोगों के प्रति लेखक का दृष्टिकोण सबसे अच्छी तरह कैसा बताया जा सकता है?",
   "The author explains the buyers' reasons -- cost and speed where a doctor's visit costs a day's wages -- and calls the habit 'rarely reckless', yet warns that every unneeded course breeds resistance. "
   "That is sympathy for the people combined with concern about the practice. 'Scornful' contradicts 'rarely reckless'; 'indifferent' ignores the warning about harm to everyone; 'approving' ignores the concern.",
   "लेखक ख़रीदारों के कारण समझाता है -- जहाँ डॉक्टर के पास जाने में एक दिन की मज़दूरी लगती है वहाँ लागत और गति -- और इस आदत को 'शायद ही लापरवाही' कहता है, फिर भी चेताता है कि हर अनावश्यक कोर्स प्रतिरोध पैदा करता है। "
   "यह लोगों के प्रति सहानुभूति के साथ इस प्रथा को लेकर चिंता है। 'तिरस्कारपूर्ण' 'शायद ही लापरवाही' का खंडन करता है; 'उदासीन' सबको होने वाली हानि की चेतावनी अनदेखी करता है; 'प्रशंसा' चिंता को अनदेखा करता है।",
   "tone",
   opts=["sympathetic to their reasons but worried about the practice",
         "scornful of their carelessness and their ignorance of medicine",
         "indifferent to the harm their choices may do to others",
         "approving of their thrift and their spirit of self-reliance"],
   opts_hi=["उनके कारणों के प्रति सहानुभूतिपूर्ण, पर इस प्रथा को लेकर चिंतित",
            "उनकी लापरवाही और चिकित्सा के बारे में उनके अज्ञान के प्रति तिरस्कारपूर्ण",
            "उनके विकल्पों से दूसरों को होने वाली हानि के प्रति उदासीन",
            "उनकी मितव्ययिता और आत्मनिर्भरता की भावना की प्रशंसा करने वाला"],
   ans=0, pos=2)

# ------------------------------------------------------------------ P03 gig work (3)
p = passage("p03",
  "A delivery rider who works for three apps in a day is, in law, an employee of none of them. The platforms call riders 'partners', which spares the platforms the cost of health cover, accident insurance and pensions, "
  "and leaves the riders free to log in and out as they please. Many riders value that freedom; few can afford to lose a week's earnings to an injury. The usual choice offered -- make riders employees, "
  "or leave them as free agents -- is a false one. A small levy on every order, pooled into a fund that pays for accidents and illness whichever app the rider was using, would protect the worker without "
  "tying him to one employer. The idea is less radical than it sounds: construction workers, who also move from one site to another, have long been covered by such a cess.",
  "एक दिन में तीन ऐप्स के लिए काम करने वाला डिलीवरी राइडर क़ानून की नज़र में इनमें से किसी का भी कर्मचारी नहीं है। प्लेटफ़ॉर्म राइडरों को 'साझेदार' कहते हैं, जिससे प्लेटफ़ॉर्म स्वास्थ्य सुरक्षा, दुर्घटना बीमा और पेंशन के ख़र्च से बच जाते हैं, "
  "और राइडर अपनी इच्छा से लॉग-इन और लॉग-आउट करने के लिए स्वतंत्र रहते हैं। कई राइडर इस स्वतंत्रता को महत्त्व देते हैं; पर बहुत कम राइडर चोट लगने पर एक सप्ताह की कमाई गँवाना सह सकते हैं। "
  "आम तौर पर दिया जाने वाला विकल्प -- राइडरों को कर्मचारी बनाओ, या उन्हें स्वतंत्र छोड़ दो -- एक झूठा विकल्प है। हर ऑर्डर पर एक छोटा उपकर, जो एक कोष में जमा हो और दुर्घटना तथा बीमारी में भुगतान करे, "
  "चाहे राइडर किसी भी ऐप पर काम कर रहा हो, कर्मचारी को किसी एक नियोक्ता से बाँधे बिना उसकी रक्षा करेगा। यह विचार जितना क्रांतिकारी लगता है उतना है नहीं: निर्माण मज़दूर, जो एक साइट से दूसरी साइट पर जाते रहते हैं, "
  "लंबे समय से ऐसे उपकर के दायरे में हैं।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage calls the choice between 'employees' and 'free agents' a false one and proposes a pooled levy that protects riders 'without tying' them to one employer. "
   "The first distractor is one side of the false choice the author rejects; the second overstates the passage, which says many riders value freedom but few can bear the loss of earnings; "
   "the third turns the closing example, offered only to show the idea is workable, into the main point.",
   "परिच्छेद 'कर्मचारी' और 'स्वतंत्र' के बीच के विकल्प को झूठा बताता है और एक साझा उपकर सुझाता है जो राइडरों को किसी एक नियोक्ता से 'बाँधे बिना' उनकी रक्षा करे। "
   "पहला ग़लत विकल्प उसी झूठे विकल्प का एक पक्ष है जिसे लेखक नकारता है; दूसरा परिच्छेद को बढ़ा-चढ़ाकर कहता है, जो कहता है कि कई राइडर स्वतंत्रता को महत्त्व देते हैं पर बहुत कम कमाई की हानि सह सकते हैं; "
   "तीसरा अंतिम उदाहरण को, जो केवल यह दिखाने के लिए है कि विचार व्यावहारिक है, मुख्य बात बना देता है।",
   "crux",
   opts=["Gig workers can be protected without being made employees of any one platform.",
         "Platforms should be made to treat all their delivery riders as regular employees.",
         "Most delivery riders value their freedom more than any social security.",
         "Construction workers are better protected today than delivery riders are."],
   opts_hi=["गिग श्रमिकों को किसी एक प्लेटफ़ॉर्म का कर्मचारी बनाए बिना सुरक्षा दी जा सकती है।",
            "प्लेटफ़ॉर्मों को अपने सभी डिलीवरी राइडरों को नियमित कर्मचारी मानने के लिए बाध्य किया जाना चाहिए।",
            "अधिकांश डिलीवरी राइडर किसी भी सामाजिक सुरक्षा से अधिक अपनी स्वतंत्रता को महत्त्व देते हैं।",
            "निर्माण मज़दूर आज डिलीवरी राइडरों से अधिक सुरक्षित हैं।"],
   ans=0, pos=1)
RQ(p, "Assumption", "hard", "s2", ASSUME, ASSUME_HI,
   "Only 1 is assumed. The proposal works only if a small levy per order can pay for real cover; if it could not, pooling it would protect no one. "
   "2 is not assumed and runs against the passage, which says many riders value the freedom of logging in and out -- the reason the author avoids making them employees.",
   "केवल 1 पूर्वधारणा है। प्रस्ताव तभी काम करता है जब प्रति ऑर्डर छोटा उपकर वास्तविक सुरक्षा का ख़र्च उठा सके; यदि ऐसा न हो, तो उसे जमा करने से किसी की रक्षा नहीं होगी। "
   "2 पूर्वधारणा नहीं है और परिच्छेद के विपरीत जाता है, जो कहता है कि कई राइडर लॉग-इन और लॉग-आउट की स्वतंत्रता को महत्त्व देते हैं -- इसी कारण लेखक उन्हें कर्मचारी बनाने से बचता है।",
   "assumptions",
   st=["A small levy on each order could raise enough money to give riders meaningful cover.",
       "Most riders would rather be employees of a single platform."],
   st_hi=["हर ऑर्डर पर छोटा उपकर इतना धन जुटा सकता है कि राइडरों को सार्थक सुरक्षा मिल सके।",
          "अधिकांश राइडर किसी एक प्लेटफ़ॉर्म का कर्मचारी बनना अधिक पसंद करेंगे।"],
   key=0)
RQ(p, "Specific Detail", "easy", "mcq",
   "According to the passage, calling riders 'partners' benefits the platforms because it:",
   "परिच्छेद के अनुसार राइडरों को 'साझेदार' कहना प्लेटफ़ॉर्मों के लिए लाभदायक है, क्योंकि यह:",
   "The passage says the label 'spares the platforms the cost of health cover, accident insurance and pensions'. It says nothing about profit-sharing, a legal requirement or loyalty; "
   "if anything, the label leaves riders free to work for several apps.",
   "परिच्छेद कहता है कि यह नाम 'प्लेटफ़ॉर्मों को स्वास्थ्य सुरक्षा, दुर्घटना बीमा और पेंशन के ख़र्च से बचाता है'। वह लाभ में हिस्सेदारी, क़ानूनी बाध्यता या निष्ठा के बारे में कुछ नहीं कहता; "
   "बल्कि यह नाम राइडरों को कई ऐप्स के लिए काम करने को स्वतंत्र छोड़ता है।",
   "detail",
   opts=["spares them the cost of health cover and insurance",
         "lets them pay the riders a share of their yearly profits",
         "is the term that the law requires them to use",
         "makes the riders more loyal to a single platform"],
   opts_hi=["उन्हें स्वास्थ्य सुरक्षा और बीमा के ख़र्च से बचाता है",
            "उन्हें राइडरों को अपने वार्षिक लाभ का हिस्सा देने देता है",
            "वह शब्द है जिसका प्रयोग क़ानून उनसे करवाता है",
            "राइडरों को किसी एक प्लेटफ़ॉर्म के प्रति अधिक निष्ठावान बनाता है"],
   ans=0, pos=3)

# ------------------------------------------------------------------ P04 libraries (2)
p = passage("p04",
  "The public library is one of the few places in an Indian town where a person can sit for hours without being asked to buy anything. That, more than its books, may be its real value today. "
  "A student whose family of five shares a single room needs a quiet table more than a new title; a retired clerk needs company as much as newspapers. Libraries that judge themselves by the number of books issued "
  "miss what their busiest users come for, and those that close at five in the evening shut their doors just when working people are free. A library that stayed open late, with good light, clean toilets "
  "and reliable internet, might be the cheapest public investment a town could make in its young people.",
  "सार्वजनिक पुस्तकालय किसी भारतीय कस्बे की उन गिनी-चुनी जगहों में से है जहाँ कोई व्यक्ति कुछ ख़रीदने को कहे बिना घंटों बैठ सकता है। आज उसकी असली क़ीमत शायद उसकी पुस्तकों से अधिक यही है। "
  "जिस विद्यार्थी का पाँच लोगों का परिवार एक ही कमरे में रहता है, उसे नई पुस्तक से अधिक एक शांत मेज़ की ज़रूरत है; किसी सेवानिवृत्त क्लर्क को अख़बारों जितनी ही संगत की ज़रूरत है। जो पुस्तकालय स्वयं को जारी की गई पुस्तकों की संख्या से आँकते हैं, "
  "वे यह नहीं समझ पाते कि उनके सबसे नियमित उपयोगकर्ता किस लिए आते हैं, और जो शाम पाँच बजे बंद हो जाते हैं, वे ठीक तभी दरवाज़े बंद कर देते हैं जब कामकाजी लोग ख़ाली होते हैं। "
  "देर तक खुला रहने वाला पुस्तकालय, अच्छी रोशनी, साफ़ शौचालयों और भरोसेमंद इंटरनेट के साथ, शायद वह सबसे सस्ता सार्वजनिक निवेश हो जो कोई कस्बा अपने युवाओं में कर सकता है।")
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Only 2 is valid: the student sharing one room 'needs a quiet table more than a new title'. 1 reverses the passage, which says libraries that judge themselves by books issued 'miss what their busiest users come for'.",
   "केवल 2 वैध है: एक कमरा साझा करने वाले विद्यार्थी को 'नई पुस्तक से अधिक एक शांत मेज़ की ज़रूरत है'। 1 परिच्छेद को उलट देता है, जो कहता है कि जारी पुस्तकों से स्वयं को आँकने वाले पुस्तकालय 'यह नहीं समझ पाते कि उनके सबसे नियमित उपयोगकर्ता किस लिए आते हैं'।",
   "conclusions",
   st=["A library that issues more books than another serves its town better.",
       "For some library users, a place to study matters more than the books on the shelves."],
   st_hi=["जो पुस्तकालय दूसरे से अधिक पुस्तकें जारी करता है, वह अपने कस्बे की बेहतर सेवा करता है।",
          "कुछ उपयोगकर्ताओं के लिए पढ़ने की जगह अलमारियों की पुस्तकों से अधिक महत्त्वपूर्ण है।"],
   key=1)
RQ(p, "Best Summary", "medium", "mcq", "Which one of the following best sums up the passage?",
   "निम्नलिखित में से कौन-सा कथन परिच्छेद का सबसे अच्छा सारांश है?",
   "The passage argues that a library's value today lies in its space -- a quiet table, company, long hours -- and that it should be run around what its users need. "
   "Spending more on books is the measure the passage questions; 'working people have no time' misreads the point that libraries close just when such people are free; "
   "the internet appears in the passage as something a library should offer, not as its replacement.",
   "परिच्छेद का तर्क है कि आज पुस्तकालय की क़ीमत उसकी जगह में है -- एक शांत मेज़, संगत, देर तक खुले रहना -- और उसे उपयोगकर्ताओं की ज़रूरतों के अनुसार चलाया जाना चाहिए। "
   "पुस्तकों पर अधिक ख़र्च वही पैमाना है जिस पर परिच्छेद प्रश्न उठाता है; 'कामकाजी लोगों के पास समय नहीं' इस बात को ग़लत पढ़ता है कि पुस्तकालय ठीक तभी बंद होते हैं जब ऐसे लोग ख़ाली होते हैं; "
   "इंटरनेट परिच्छेद में ऐसी चीज़ के रूप में आता है जो पुस्तकालय को देनी चाहिए, उसके विकल्प के रूप में नहीं।",
   "summary",
   opts=["Libraries matter as public spaces and should be run around their users' needs.",
         "Libraries should spend more of their money on new books and newspapers.",
         "Working people have no time to use the public libraries in their towns.",
         "The internet has now made the public library unnecessary for most young people."],
   opts_hi=["पुस्तकालय सार्वजनिक स्थानों के रूप में महत्त्वपूर्ण हैं और उन्हें उपयोगकर्ताओं की ज़रूरतों के अनुसार चलाया जाना चाहिए।",
            "पुस्तकालयों को अपना अधिक धन नई पुस्तकों और अख़बारों पर ख़र्च करना चाहिए।",
            "कामकाजी लोगों के पास अपने कस्बों के सार्वजनिक पुस्तकालयों का उपयोग करने का समय नहीं है।",
            "इंटरनेट ने अब अधिकांश युवाओं के लिए सार्वजनिक पुस्तकालय को अनावश्यक बना दिया है।"],
   ans=0, pos=2)

# ------------------------------------------------------------------ P05 crop choice (3)
p = passage("p05",
  "Farmers in the north-west grow rice in summer not because the climate suits it -- the region is semi-arid -- but because the government buys the crop at an assured price. Every kilogram of rice takes thousands "
  "of litres of water, much of it pumped from aquifers that fall year after year. Appeals to switch to pulses or millets have had little effect, for a simple reason: a farmer who switches gives up a certain income "
  "for an uncertain one. Diversification will come only when the other crops carry the same certainty -- a buyer, a price and a way to store the harvest -- that rice already enjoys. Until then, asking farmers "
  "to save water is asking them to bear a risk that the state has been unwilling to share.",
  "उत्तर-पश्चिम के किसान गर्मियों में धान इसलिए नहीं उगाते कि वहाँ की जलवायु उसके अनुकूल है -- यह क्षेत्र अर्ध-शुष्क है -- बल्कि इसलिए कि सरकार यह फ़सल सुनिश्चित मूल्य पर ख़रीदती है। हर किलोग्राम चावल में हज़ारों लीटर पानी लगता है, "
  "जिसका बड़ा भाग उन भूजल भंडारों से खींचा जाता है जिनका स्तर साल-दर-साल गिर रहा है। दालों या मोटे अनाजों की ओर जाने की अपीलों का बहुत कम असर हुआ है, और इसका कारण सीधा है: फ़सल बदलने वाला किसान एक निश्चित आय छोड़कर "
  "एक अनिश्चित आय चुनता है। विविधीकरण तभी आएगा जब दूसरी फ़सलों के साथ भी वही निश्चितता हो -- एक ख़रीदार, एक मूल्य और फ़सल रखने की व्यवस्था -- जो धान को पहले से प्राप्त है। "
  "तब तक किसानों से पानी बचाने को कहना उनसे वह जोखिम उठाने को कहना है जिसे राज्य बाँटने को तैयार नहीं रहा है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage traces rice-growing to the certainty of an assured purchase and says diversification will come 'only when the other crops carry the same certainty'. "
   "The first distractor is a stronger claim than the passage makes; the second blames farmers, while the passage blames the incentives they face; the third reverses the passage, which implies the alternatives save water.",
   "परिच्छेद धान की खेती को सुनिश्चित ख़रीद की निश्चितता से जोड़ता है और कहता है कि विविधीकरण 'तभी आएगा जब दूसरी फ़सलों के साथ भी वही निश्चितता हो'। "
   "पहला ग़लत विकल्प परिच्छेद से बड़ा दावा है; दूसरा किसानों को दोष देता है, जबकि परिच्छेद उनके सामने के प्रोत्साहनों को दोष देता है; तीसरा परिच्छेद को उलट देता है, जिसका आशय है कि विकल्प पानी बचाते हैं।",
   "crux",
   opts=["Farmers will move away from rice only when other crops offer the same certainty.",
         "Rice should not be grown at all in the semi-arid regions of the country.",
         "The fall in groundwater in the north-west is due mainly to the carelessness of farmers.",
         "Pulses and millets use more water than rice and so offer no real saving."],
   opts_hi=["किसान धान से तभी हटेंगे जब दूसरी फ़सलें भी वैसी ही निश्चितता दें।",
            "देश के अर्ध-शुष्क क्षेत्रों में धान बिल्कुल नहीं उगाया जाना चाहिए।",
            "उत्तर-पश्चिम में भूजल का गिरना मुख्यतः किसानों की लापरवाही के कारण है।",
            "दालें और मोटे अनाज धान से अधिक पानी लेते हैं, इसलिए उनसे कोई वास्तविक बचत नहीं होती।"],
   ans=0, pos=0)
RQ(p, "Assumption", "hard", "sc", ASSUME, ASSUME_HI,
   "1 and 2 are assumed. The whole argument treats crop choice as a response to risk -- a farmer will not trade a certain income for an uncertain one (1). And faulting the state for being 'unwilling' to share the risk, "
   "and asking it to give other crops a buyer, a price and storage, assumes that it can do so (2). 3 is not needed: the passage says rice is grown because its price is assured, not that it is the most profitable crop anywhere.",
   "1 और 2 पूर्वधारणाएँ हैं। पूरा तर्क फ़सल के चुनाव को जोखिम की प्रतिक्रिया मानता है -- किसान निश्चित आय को अनिश्चित आय से नहीं बदलेगा (1)। और राज्य को जोखिम बाँटने के लिए 'तैयार नहीं' होने का दोष देना, "
   "तथा उससे दूसरी फ़सलों को ख़रीदार, मूल्य और भंडारण देने को कहना, यह मानकर चलता है कि वह ऐसा कर सकता है (2)। 3 की ज़रूरत नहीं: परिच्छेद कहता है कि धान इसलिए उगाया जाता है कि उसका मूल्य सुनिश्चित है, यह नहीं कि वह हर जगह सबसे लाभदायक फ़सल है।",
   "assumptions",
   st=["Farmers' choice of crops responds to the risks they face.",
       "The state is able to offer assured purchase for crops other than rice.",
       "Rice is the most profitable crop that can be grown anywhere in India."],
   st_hi=["किसानों का फ़सल-चुनाव उनके सामने के जोखिमों के अनुसार होता है।",
          "राज्य धान के अलावा दूसरी फ़सलों की भी सुनिश्चित ख़रीद कर सकता है।",
          "धान भारत में कहीं भी उगाई जा सकने वाली सबसे लाभदायक फ़सल है।"],
   opts=["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"], key=0)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Both are valid. Appeals to switch 'have had little effect' because switching means giving up a certain income, so campaigns that only urge water-saving are unlikely to change what farmers grow (1). "
   "By buying rice at an assured price, the state already gives that crop the certainty the passage describes, that is, it bears part of the farmer's risk for rice; the complaint is that it will not do the same for other crops (2).",
   "दोनों वैध हैं। फ़सल बदलने की अपीलों का 'बहुत कम असर' हुआ है, क्योंकि बदलने का अर्थ निश्चित आय छोड़ना है, इसलिए केवल पानी बचाने का आग्रह करने वाले अभियान किसानों की फ़सल नहीं बदल पाएँगे (1)। "
   "धान को सुनिश्चित मूल्य पर ख़रीदकर राज्य उस फ़सल को पहले से वह निश्चितता देता है जिसका परिच्छेद वर्णन करता है, यानी धान के लिए वह किसान के जोखिम का एक भाग उठाता है; शिकायत यह है कि वह दूसरी फ़सलों के लिए ऐसा नहीं करता (2)।",
   "conclusions",
   st=["Campaigns that only urge farmers to save water are unlikely to change what they grow.",
       "In assuring the price of rice, the state already takes on part of the farmer's risk for that crop."],
   st_hi=["केवल पानी बचाने का आग्रह करने वाले अभियानों से किसानों की फ़सल बदलने की संभावना कम है।",
          "धान का मूल्य सुनिश्चित करके राज्य उस फ़सल के लिए किसान के जोखिम का एक भाग पहले से उठाता है।"],
   key=2)

# ------------------------------------------------------------------ P06 misinformation (3)
p = passage("p06",
  "Fact-checkers can correct a false story only after it has spread, and by then the correction reaches a fraction of the people who saw the original. Research on misinformation points to another approach: "
  "teaching people, before they meet a falsehood, the tricks that make it persuasive -- the doctored photograph, the fake expert, the appeal to outrage. People who have seen these tricks explained are better "
  "at spotting them later, much as a vaccine prepares the body for a virus it has not yet met. The method has limits. It works better against techniques than against particular claims, and its effect fades "
  "unless it is refreshed. But it does not depend on anyone deciding what is true, which makes it harder to dismiss as censorship.",
  "तथ्य-जाँचकर्ता किसी झूठी ख़बर को उसके फैल जाने के बाद ही सुधार सकते हैं, और तब तक सुधार उन लोगों के एक छोटे भाग तक ही पहुँचता है जिन्होंने मूल ख़बर देखी थी। ग़लत सूचना पर हुए शोध एक दूसरे तरीके की ओर इशारा करते हैं: "
  "लोगों को किसी झूठ से सामना होने से पहले ही वे तरकीबें सिखाना जो उसे विश्वसनीय बनाती हैं -- छेड़छाड़ की गई तस्वीर, नकली विशेषज्ञ, आक्रोश भड़काने वाली अपील। जिन लोगों को ये तरकीबें समझाई गई हैं, वे बाद में इन्हें बेहतर पहचान पाते हैं, "
  "ठीक वैसे ही जैसे टीका शरीर को किसी ऐसे वायरस के लिए तैयार करता है जिससे उसका अभी सामना नहीं हुआ। इस तरीके की सीमाएँ हैं। यह किसी विशेष दावे के बजाय तरकीबों के विरुद्ध बेहतर काम करता है, और दोहराया न जाए तो इसका असर घटता जाता है। "
  "पर यह इस पर निर्भर नहीं कि कोई यह तय करे कि सच क्या है, इसलिए इसे सेंसरशिप कहकर ख़ारिज करना कठिन है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage sets correction after the fact against preparing people in advance, and argues for the second despite its limits. "
   "The first distractor overreaches: the passage notes the limits of fact-checking but never says it should be given up. The second turns one example, the doctored photograph, into a general claim. "
   "The third is the opposite of the passage, which values the method because it does not depend on anyone deciding what is true.",
   "परिच्छेद बाद में किए जाने वाले सुधार की तुलना पहले से तैयार करने से करता है, और सीमाओं के बावजूद दूसरे के पक्ष में तर्क देता है। "
   "पहला ग़लत विकल्प बहुत आगे जाता है: परिच्छेद तथ्य-जाँच की सीमाएँ बताता है, पर कहीं नहीं कहता कि उसे छोड़ देना चाहिए। दूसरा एक उदाहरण, छेड़छाड़ की गई तस्वीर, को सामान्य दावा बना देता है। "
   "तीसरा परिच्छेद के उलट है, जो इस तरीके को इसलिए महत्त्व देता है कि यह किसी के सच तय करने पर निर्भर नहीं।",
   "crux",
   opts=["Teaching people to spot persuasion tricks can beat correcting each falsehood later.",
         "Fact-checking should be given up, because its corrections always arrive far too late.",
         "Most misinformation spreads through photographs that have been doctored.",
         "Governments should decide which stories are true and remove all the others."],
   opts_hi=["लोगों को राज़ी करने की तरकीबें पहचानना सिखाना हर झूठ को बाद में सुधारने से बेहतर हो सकता है।",
            "तथ्य-जाँच छोड़ देनी चाहिए, क्योंकि उसके सुधार सदा बहुत देर से आते हैं।",
            "अधिकांश ग़लत सूचना छेड़छाड़ की गई तस्वीरों से फैलती है।",
            "सरकारों को तय करना चाहिए कि कौन-सी ख़बरें सच हैं और बाक़ी सब हटा देनी चाहिए।"],
   ans=0, pos=2)
RQ(p, "Inference", "hard", "sc", INFER, INFER_HI,
   "1 and 2 follow. A correction 'reaches a fraction of the people who saw the original' (1). The training works 'better against techniques than against particular claims' and, like a vaccine, prepares people for what they "
   "'have not yet met', so it can help against false claims not yet seen (2). 3 contradicts the passage: the effect 'fades unless it is refreshed'.",
   "1 और 2 निकलते हैं। सुधार 'उन लोगों के एक छोटे भाग तक ही पहुँचता है जिन्होंने मूल ख़बर देखी थी' (1)। प्रशिक्षण 'किसी विशेष दावे के बजाय तरकीबों के विरुद्ध बेहतर काम करता है' और, टीके की तरह, लोगों को उसके लिए तैयार करता है "
   "'जिससे अभी सामना नहीं हुआ', इसलिए यह न देखे गए झूठे दावों के विरुद्ध भी सहायता कर सकता है (2)। 3 परिच्छेद का खंडन करता है: असर 'दोहराया न जाए तो घटता जाता है'।",
   "inferences",
   st=["A correction usually reaches fewer people than the false story it corrects.",
       "Training against a technique of deception can help people resist false claims they have not yet seen.",
       "Once given, such training protects a person for life."],
   st_hi=["सुधार प्रायः उस झूठी ख़बर से कम लोगों तक पहुँचता है जिसे वह सुधारता है।",
          "धोखे की किसी तरकीब के विरुद्ध प्रशिक्षण लोगों को उन झूठे दावों से भी बचा सकता है जिन्हें उन्होंने अभी देखा नहीं।",
          "एक बार दिया गया ऐसा प्रशिक्षण व्यक्ति की जीवन भर रक्षा करता है।"],
   opts=["1 only", "1, 2 and 3", "2 and 3 only", "1 and 2 only"], key=3)
RQ(p, "Specific Detail", "easy", "mcq",
   "The passage compares the approach it describes to a vaccine because the approach:",
   "परिच्छेद अपने बताए तरीके की तुलना टीके से इसलिए करता है क्योंकि यह तरीका:",
   "Like a vaccine, which prepares the body for a virus it has not yet met, the training prepares people for a falsehood before they meet it. "
   "The passage says nothing about the method spreading like an infection or about how many people it has been tested on, and it says the method works better against techniques than against particular claims.",
   "जैसे टीका शरीर को उस वायरस के लिए तैयार करता है जिससे अभी सामना नहीं हुआ, वैसे ही यह प्रशिक्षण लोगों को किसी झूठ से सामना होने से पहले तैयार करता है। "
   "परिच्छेद इस तरीके के संक्रमण की तरह फैलने या कितने लोगों पर इसके परीक्षण के बारे में कुछ नहीं कहता, और कहता है कि यह विशेष दावों के बजाय तरकीबों के विरुद्ध बेहतर काम करता है।",
   "detail",
   opts=["prepares people for a falsehood before they meet it",
         "spreads from one person to another like an infection",
         "works only against one particular false claim at a time",
         "has been tested on very large numbers of people"],
   opts_hi=["लोगों को किसी झूठ से सामना होने से पहले तैयार करता है",
            "किसी संक्रमण की तरह एक व्यक्ति से दूसरे तक फैलता है",
            "एक समय में केवल एक विशेष झूठे दावे के विरुद्ध काम करता है",
            "बहुत बड़ी संख्या में लोगों पर परखा गया है"],
   ans=0, pos=1)

# ------------------------------------------------------------------ P07 coasts (3)
p = passage("p07",
  "When planners in coastal cities think about rising seas, they think first of walls. A sea wall is visible, easy to cost and quick to inaugurate, and it can protect a stretch of shore for decades. "
  "It also moves the problem elsewhere: waves that strike a hard wall scour the beach in front of it and wear away the shore at its ends. Mangroves offer a different kind of defence. Their tangled roots slow "
  "the waves and trap sediment, so a healthy mangrove belt can build up the land behind it as the sea rises, and it shelters fish nurseries too. But mangroves need room to move inland, and that room is usually "
  "taken by roads, ports and housing. A city that wants nature to defend it must first be willing to give nature space.",
  "जब तटीय शहरों के योजनाकार बढ़ते समुद्र के बारे में सोचते हैं, तो सबसे पहले दीवारों के बारे में सोचते हैं। समुद्री दीवार दिखाई देती है, उसकी लागत आँकना आसान है और उसका उद्घाटन जल्दी हो जाता है, और वह तट के किसी हिस्से की दशकों तक रक्षा कर सकती है। "
  "साथ ही वह समस्या को कहीं और खिसका देती है: कठोर दीवार से टकराने वाली लहरें उसके सामने के समुद्र-तट को खुरच ले जाती हैं और उसके सिरों पर तट को काटती हैं। मैंग्रोव एक अलग तरह की रक्षा देते हैं। उनकी उलझी जड़ें लहरों को धीमा करती हैं "
  "और तलछट रोकती हैं, इसलिए एक स्वस्थ मैंग्रोव पट्टी समुद्र के बढ़ने के साथ अपने पीछे की ज़मीन को ऊँचा कर सकती है, और वह मछलियों की नर्सरी को आश्रय भी देती है। पर मैंग्रोव को भीतर की ओर खिसकने के लिए जगह चाहिए, और वह जगह "
  "प्रायः सड़कों, बंदरगाहों और आवासों ने ले रखी होती है। जो शहर चाहता है कि प्रकृति उसकी रक्षा करे, उसे पहले प्रकृति को जगह देने के लिए तैयार होना होगा।")
RQ(p, "Best Summary", "medium", "mcq", MSG, MSG_HI,
   "The passage weighs walls against mangroves and ends on its condition: mangroves can defend a coast only if the city gives them room. "
   "Replacing every wall goes beyond the passage, which credits walls with decades of protection; the claim that walls beat any natural defence reverses its argument; fish nurseries are a side benefit, not the point.",
   "परिच्छेद दीवारों और मैंग्रोव की तुलना करता है और अपनी शर्त पर समाप्त होता है: मैंग्रोव तट की रक्षा तभी कर सकते हैं जब शहर उन्हें जगह दे। "
   "हर दीवार हटाना परिच्छेद से आगे जाता है, जो दीवारों को दशकों की सुरक्षा का श्रेय देता है; यह दावा कि दीवारें हर प्राकृतिक रक्षा से बेहतर हैं उसके तर्क को उलट देता है; मछलियों की नर्सरी एक अतिरिक्त लाभ है, मुख्य बात नहीं।",
   "message",
   opts=["Mangroves can defend a coast, but only if a city leaves them room to grow.",
         "Every coastal city should now replace its sea walls with belts of mangroves.",
         "Sea walls protect a coast better than any natural defence can.",
         "Mangroves matter mainly because they shelter the nurseries of fish."],
   opts_hi=["मैंग्रोव तट की रक्षा कर सकते हैं, पर तभी जब शहर उन्हें बढ़ने की जगह दे।",
            "हर तटीय शहर को अब अपनी समुद्री दीवारों की जगह मैंग्रोव की पट्टियाँ लगानी चाहिए।",
            "समुद्री दीवारें किसी भी प्राकृतिक रक्षा से बेहतर तट की रक्षा करती हैं।",
            "मैंग्रोव मुख्यतः इसलिए महत्त्वपूर्ण हैं कि वे मछलियों की नर्सरी को आश्रय देते हैं।"],
   ans=0, pos=3)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Neither is valid. 1 contradicts the passage, which says a sea wall 'can protect a stretch of shore for decades'. 2 contradicts its warning that 'mangroves need room to move inland'. "
   "Both read like summaries of the passage but each turns a stated condition upside down.",
   "कोई भी वैध नहीं है। 1 परिच्छेद का खंडन करता है, जो कहता है कि समुद्री दीवार 'तट के किसी हिस्से की दशकों तक रक्षा कर सकती है'। 2 उसकी इस चेतावनी का खंडन करता है कि 'मैंग्रोव को भीतर की ओर खिसकने के लिए जगह चाहिए'। "
   "दोनों परिच्छेद के सारांश जैसे लगते हैं, पर हर एक बताई गई शर्त को उलट देता है।",
   "conclusions",
   st=["Sea walls can protect a coast for only a few years.",
       "Mangroves can protect a coast without any land behind them to move into."],
   st_hi=["समुद्री दीवारें केवल कुछ वर्षों तक ही तट की रक्षा कर सकती हैं।",
          "मैंग्रोव अपने पीछे खिसकने के लिए कोई ज़मीन न होने पर भी तट की रक्षा कर सकते हैं।"],
   key=3)
RQ(p, "Assumption", "hard", "s2", ASSUME, ASSUME_HI,
   "Only 2 is assumed. The whole discussion -- walls against mangroves, land building up 'as the sea rises' -- takes for granted that coastal cities face higher seas ahead. "
   "1 is not needed: the passage compares the two defences and never says they cannot be used together on one coast.",
   "केवल 2 पूर्वधारणा है। पूरी चर्चा -- दीवारें बनाम मैंग्रोव, 'समुद्र के बढ़ने के साथ' ज़मीन का ऊँचा होना -- यह मानकर चलती है कि तटीय शहरों के सामने ऊँचे समुद्र आने वाले हैं। "
   "1 की ज़रूरत नहीं: परिच्छेद दोनों प्रकार की रक्षा की तुलना करता है और कहीं नहीं कहता कि एक ही तट पर दोनों का साथ-साथ उपयोग नहीं हो सकता।",
   "assumptions",
   st=["A sea wall and a mangrove belt can never be used along the same coast.",
       "Coastal cities will face higher seas in the years ahead."],
   st_hi=["एक ही तट पर समुद्री दीवार और मैंग्रोव पट्टी का उपयोग कभी नहीं किया जा सकता।",
          "आने वाले वर्षों में तटीय शहरों को ऊँचे समुद्र का सामना करना होगा।"],
   key=1)

# ------------------------------------------------------------------ P08 sport (2)
p = passage("p08",
  "Talent scouts in cricket and football talk of the 'relative age effect'. In any group of children sorted by year of birth, those born in the first months of the year are older, bigger and stronger than those born "
  "in its last months. Coaches mistake that head start for talent, pick the older children for the best teams and give them the best coaching, and the gap widens. Years later, professional squads are crowded with "
  "players born early in the selection year. Some clubs now compare each child only with others born in the same quarter of the year, or put off selection until growth evens out. The lesson goes beyond sport: "
  "a judgement made too early can create the very difference it claims to discover.",
  "क्रिकेट और फ़ुटबॉल में प्रतिभा खोजने वाले 'सापेक्ष आयु प्रभाव' की बात करते हैं। जन्म-वर्ष के अनुसार बाँटे गए बच्चों के किसी भी समूह में, वर्ष के पहले महीनों में जन्मे बच्चे उसके अंतिम महीनों में जन्मे बच्चों से बड़े, "
  "लंबे और अधिक मज़बूत होते हैं। कोच इस आरंभिक बढ़त को प्रतिभा समझ लेते हैं, बड़े बच्चों को सबसे अच्छी टीमों के लिए चुनते हैं और उन्हें सबसे अच्छा प्रशिक्षण देते हैं, और अंतर बढ़ता जाता है। "
  "वर्षों बाद पेशेवर टीमें चयन-वर्ष के आरंभ में जन्मे खिलाड़ियों से भरी होती हैं। कुछ क्लब अब हर बच्चे की तुलना केवल वर्ष की उसी तिमाही में जन्मे बच्चों से करते हैं, या चयन को तब तक टालते हैं जब तक विकास बराबर न हो जाए। "
  "यह सबक खेल से आगे जाता है: बहुत जल्दी किया गया निर्णय वही अंतर पैदा कर सकता है जिसे खोजने का वह दावा करता है।")
RQ(p, "Main Idea", "hard", "mcq", CRUX, CRUX_HI,
   "The passage shows how an early age advantage, mistaken for talent, is widened by selection and coaching until it becomes a real gap -- 'a judgement made too early can create the very difference it claims to discover'. "
   "The first distractor repeats the coaches' error that the passage exposes; the second invents a fixed age the passage never names; the third is a sweeping claim the passage does not make, since some clubs are already correcting for the effect.",
   "परिच्छेद दिखाता है कि आयु की आरंभिक बढ़त, जिसे प्रतिभा समझ लिया जाता है, चयन और प्रशिक्षण से तब तक बढ़ती है जब तक वह वास्तविक अंतर न बन जाए -- 'बहुत जल्दी किया गया निर्णय वही अंतर पैदा कर सकता है जिसे खोजने का वह दावा करता है'। "
   "पहला ग़लत विकल्प कोचों की वही भूल दोहराता है जिसे परिच्छेद उजागर करता है; दूसरा एक निश्चित आयु गढ़ता है जिसका परिच्छेद में उल्लेख नहीं; तीसरा एक व्यापक दावा है जो परिच्छेद नहीं करता, क्योंकि कुछ क्लब पहले से इस प्रभाव को सुधार रहे हैं।",
   "crux",
   opts=["Selecting too early can turn a passing advantage of age into a lasting gap in skill.",
         "Children born early in the year are by nature more talented at sport than other children.",
         "Coaches should not select any player before the age of eighteen.",
         "Professional sport is unfair to all players born late in the year."],
   opts_hi=["बहुत जल्दी किया गया चयन आयु की अस्थायी बढ़त को कौशल के स्थायी अंतर में बदल सकता है।",
            "वर्ष के आरंभ में जन्मे बच्चे स्वभाव से ही खेल में दूसरे बच्चों से अधिक प्रतिभाशाली होते हैं।",
            "कोचों को अठारह वर्ष की आयु से पहले किसी खिलाड़ी का चयन नहीं करना चाहिए।",
            "पेशेवर खेल वर्ष के अंत में जन्मे सभी खिलाड़ियों के साथ अन्याय करता है।"],
   ans=0, pos=0)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Only 2 is valid. The head start comes from being born early in the selection year, so moving the cut-off date would move the advantage to a different group of children. "
   "1 is not valid: cricket and football are the passage's examples, and it says the lesson 'goes beyond sport', not that the effect is confined to these two games.",
   "केवल 2 वैध है। बढ़त चयन-वर्ष के आरंभ में जन्म लेने से आती है, इसलिए कट-ऑफ़ तिथि बदलने से बढ़त बच्चों के दूसरे समूह को मिलेगी। "
   "1 वैध नहीं है: क्रिकेट और फ़ुटबॉल परिच्छेद के उदाहरण हैं, और वह कहता है कि सबक 'खेल से आगे जाता है', यह नहीं कि यह प्रभाव इन्हीं दो खेलों तक सीमित है।",
   "conclusions",
   st=["The relative age effect is found only in cricket and football.",
       "If the cut-off date for selection were changed, a different group of children would gain the head start."],
   st_hi=["सापेक्ष आयु प्रभाव केवल क्रिकेट और फ़ुटबॉल में पाया जाता है।",
          "यदि चयन की कट-ऑफ़ तिथि बदल दी जाए, तो आरंभिक बढ़त बच्चों के किसी दूसरे समूह को मिलेगी।"],
   key=1)

# ------------------------------------------------------------------ P09 schooling (3)
p = passage("p09",
  "For two decades India measured progress in schooling by enrolment, and by that measure it succeeded: almost every child of primary-school age is now on a school's rolls. Surveys that test children directly "
  "tell a less cheerful story. Large numbers of children in the upper primary classes cannot read a text meant for a much younger class, or do a simple division. The trouble is not that these children never learnt; "
  "it is that the curriculum moved on before they did, and teachers, bound to finish the syllabus, taught to the front rows. Programmes that group children by what they can actually do, rather than by their age, "
  "and teach from that level, have raised reading scores quickly and cheaply. The difficulty is that such teaching looks, to an inspector with a syllabus in hand, like falling behind.",
  "दो दशकों तक भारत ने स्कूली शिक्षा में प्रगति को नामांकन से मापा, और उस पैमाने पर वह सफल रहा: प्राथमिक विद्यालय की आयु का लगभग हर बच्चा अब किसी विद्यालय के रजिस्टर में है। बच्चों की सीधे परीक्षा लेने वाले सर्वेक्षण "
  "कम उत्साहजनक तस्वीर दिखाते हैं। उच्च प्राथमिक कक्षाओं के बहुत-से बच्चे अपने से कहीं छोटी कक्षा के लिए लिखा गया पाठ नहीं पढ़ पाते, या एक साधारण भाग नहीं कर पाते। समस्या यह नहीं कि इन बच्चों ने कभी सीखा ही नहीं; "
  "समस्या यह है कि पाठ्यक्रम उनसे पहले आगे बढ़ गया, और पाठ्यक्रम पूरा करने के लिए बँधे शिक्षकों ने आगे की पंक्तियों को ही पढ़ाया। जो कार्यक्रम बच्चों को उनकी आयु के बजाय वे वास्तव में जो कर सकते हैं उसके अनुसार समूहों में बाँटते हैं, "
  "और उसी स्तर से पढ़ाते हैं, उन्होंने पढ़ने के अंक जल्दी और कम ख़र्च में बढ़ाए हैं। कठिनाई यह है कि हाथ में पाठ्यक्रम लिए किसी निरीक्षक को ऐसा शिक्षण पिछड़ने जैसा दिखता है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage moves from enrolment to learning, finds the cause in a curriculum that 'moved on before they did', and praises teaching from the level children have reached. "
   "The first distractor contradicts the passage, which says enrolment succeeded; the second names a cause the passage does not give; the third draws a conclusion about inspectors that the passage does not draw.",
   "परिच्छेद नामांकन से सीखने की ओर बढ़ता है, कारण उस पाठ्यक्रम में पाता है जो 'उनसे पहले आगे बढ़ गया', और बच्चों के पहुँचे हुए स्तर से पढ़ाने की प्रशंसा करता है। "
   "पहला ग़लत विकल्प परिच्छेद का खंडन करता है, जो कहता है कि नामांकन सफल रहा; दूसरा ऐसा कारण बताता है जो परिच्छेद नहीं देता; तीसरा निरीक्षकों के बारे में ऐसा निष्कर्ष निकालता है जो परिच्छेद नहीं निकालता।",
   "crux",
   opts=["Teaching must start from what children can do, not from their class syllabus.",
         "India has not yet managed to bring most of its children into school.",
         "Most of India's teachers have never been properly trained to teach children to read.",
         "School inspectors should stop visiting schools to check on their teachers."],
   opts_hi=["पढ़ाई बच्चों की कक्षा के पाठ्यक्रम से नहीं, बल्कि वे जो कर सकते हैं वहाँ से शुरू होनी चाहिए।",
            "भारत अभी तक अपने अधिकांश बच्चों को विद्यालय तक नहीं ला पाया है।",
            "भारत के अधिकांश शिक्षकों को बच्चों को पढ़ना सिखाने का ठीक से प्रशिक्षण कभी नहीं मिला।",
            "विद्यालय निरीक्षकों को शिक्षकों की जाँच के लिए विद्यालय जाना बंद कर देना चाहिए।"],
   ans=0, pos=2)
RQ(p, "Specific Detail", "easy", "mcq",
   "According to the passage, many children have fallen behind because:",
   "परिच्छेद के अनुसार बहुत-से बच्चे पीछे इसलिए रह गए हैं क्योंकि:",
   "The passage says the trouble is 'that the curriculum moved on before they did' while teachers taught to the front rows. It mentions no problem of attendance or class size, "
   "and the text meant for a younger class is the passage's test of reading level, not a description of the children's textbooks.",
   "परिच्छेद कहता है कि समस्या यह है कि 'पाठ्यक्रम उनसे पहले आगे बढ़ गया', जबकि शिक्षकों ने आगे की पंक्तियों को पढ़ाया। वह उपस्थिति या कक्षा के आकार की किसी समस्या का उल्लेख नहीं करता, "
   "और छोटी कक्षा के लिए लिखा पाठ परिच्छेद में पढ़ने के स्तर की कसौटी है, बच्चों की पाठ्यपुस्तकों का वर्णन नहीं।",
   "detail",
   opts=["the curriculum moved ahead before they had learnt",
         "they did not attend school regularly enough to keep up",
         "their classes were far too large for any teacher to manage",
         "their textbooks were written for children much older than them"],
   opts_hi=["पाठ्यक्रम उनके सीखने से पहले आगे बढ़ गया",
            "वे साथ बने रहने लायक नियमित रूप से विद्यालय नहीं गए",
            "उनकी कक्षाएँ किसी भी शिक्षक के सँभालने के लिए बहुत बड़ी थीं",
            "उनकी पाठ्यपुस्तकें उनसे कहीं बड़े बच्चों के लिए लिखी गई थीं"],
   ans=0, pos=3)
RQ(p, "Assumption", "hard", "sc", ASSUME, ASSUME_HI,
   "1 and 2 are assumed. The passage uses reading scores both to show the problem and to show that teaching at level works, which assumes such tests fairly show whether teaching works (1). "
   "Its last sentence -- teaching at level looks 'like falling behind' to an inspector 'with a syllabus in hand' -- assumes inspectors judge teachers by how much of the syllabus they have covered (2). "
   "3 runs against the passage, which says the programmes raised scores 'quickly and cheaply'.",
   "1 और 2 पूर्वधारणाएँ हैं। परिच्छेद पढ़ने के अंकों का उपयोग समस्या दिखाने और यह दिखाने में करता है कि स्तर के अनुसार पढ़ाना काम करता है, जो मानकर चलता है कि ऐसी परीक्षाएँ ठीक से बताती हैं कि शिक्षण काम कर रहा है या नहीं (1)। "
   "उसका अंतिम वाक्य -- 'हाथ में पाठ्यक्रम लिए' निरीक्षक को स्तर के अनुसार पढ़ाना 'पिछड़ने जैसा' दिखता है -- मानता है कि निरीक्षक शिक्षकों को इस आधार पर आँकते हैं कि उन्होंने पाठ्यक्रम का कितना भाग पूरा किया (2)। "
   "3 परिच्छेद के विपरीत है, जो कहता है कि कार्यक्रमों ने अंक 'जल्दी और कम ख़र्च में' बढ़ाए।",
   "assumptions",
   st=["Tests of reading are a fair guide to whether teaching is working.",
       "Inspectors judge teachers by how much of the syllabus they have covered.",
       "Grouping children by level needs money that schools do not have."],
   st_hi=["पढ़ने की परीक्षाएँ इस बात की उचित कसौटी हैं कि शिक्षण काम कर रहा है या नहीं।",
          "निरीक्षक शिक्षकों को इस आधार पर आँकते हैं कि उन्होंने पाठ्यक्रम का कितना भाग पूरा किया है।",
          "बच्चों को स्तर के अनुसार समूहों में बाँटने के लिए ऐसा धन चाहिए जो विद्यालयों के पास नहीं है।"],
   opts=["1 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"], key=1)

# ------------------------------------------------------------------ P10 trust in science (3)
p = passage("p10",
  "Public trust in science is often discussed as though it were a fixed stock that experts either keep or squander. It behaves more like the trust people place in a doctor. People trust a doctor who explains what she knows "
  "and what she does not, who changes her advice when the evidence changes, and who does not pretend that a hard trade-off is a purely technical question. Scientists who, in a crisis, present every recommendation "
  "as certain may win obedience in the short run, but each later revision then looks like a broken promise. Admitting uncertainty feels risky to an expert facing an anxious public; in the long run, hiding it is riskier.",
  "विज्ञान में जनता के भरोसे की चर्चा प्रायः ऐसे की जाती है मानो वह कोई निश्चित भंडार हो जिसे विशेषज्ञ या तो बचाए रखते हैं या गँवा देते हैं। वह अधिकतर उस भरोसे की तरह व्यवहार करता है जो लोग किसी डॉक्टर पर करते हैं। "
  "लोग उस डॉक्टर पर भरोसा करते हैं जो बताती है कि वह क्या जानती है और क्या नहीं, जो प्रमाण बदलने पर अपनी सलाह बदलती है, और जो किसी कठिन संतुलन को पूरी तरह तकनीकी प्रश्न होने का दिखावा नहीं करती। "
  "जो वैज्ञानिक संकट के समय हर सिफ़ारिश को निश्चित बताकर पेश करते हैं, वे थोड़े समय के लिए आज्ञापालन पा सकते हैं, पर बाद में होने वाला हर संशोधन तब टूटे वादे जैसा लगता है। "
  "चिंतित जनता के सामने अनिश्चितता स्वीकार करना किसी विशेषज्ञ को जोखिम भरा लगता है; लंबे समय में उसे छिपाना अधिक जोखिम भरा है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage argues that trust is kept by candour -- saying what is not known and revising openly -- and that projecting certainty backfires when advice changes. "
   "Avoiding advice in a crisis is not suggested; the comparison with doctors is an analogy, not a ranking of whom people trust more; and the passage rejects the view of trust as a fixed stock that, once lost, can never be won back.",
   "परिच्छेद का तर्क है कि भरोसा स्पष्टता से बना रहता है -- यह बताना कि क्या ज्ञात नहीं और खुलकर संशोधन करना -- और यह कि सलाह बदलने पर निश्चितता का दिखावा उलटा पड़ता है। "
   "संकट में सलाह न देने का सुझाव नहीं दिया गया; डॉक्टरों से तुलना एक उपमा है, यह क्रम नहीं कि लोग किस पर अधिक भरोसा करते हैं; और परिच्छेद भरोसे को ऐसा निश्चित भंडार मानने वाले दृष्टिकोण को नकारता है जो एक बार खो जाने पर कभी वापस नहीं मिलता।",
   "crux",
   opts=["Experts keep public trust by being open about what they do not know.",
         "Scientists should avoid giving any advice at all in a time of crisis.",
         "People trust their doctors far more than they trust scientists.",
         "Once lost, public trust in science can never be won back again."],
   opts_hi=["विशेषज्ञ यह खुलकर बताकर जनता का भरोसा बनाए रखते हैं कि वे क्या नहीं जानते।",
            "वैज्ञानिकों को संकट के समय कोई भी सलाह देने से बचना चाहिए।",
            "लोग वैज्ञानिकों की तुलना में अपने डॉक्टरों पर कहीं अधिक भरोसा करते हैं।",
            "एक बार खोया हुआ विज्ञान पर जनता का भरोसा फिर कभी नहीं लौटता।"],
   ans=0, pos=1)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Both are valid. Advice first presented as certain makes 'each later revision' look 'like a broken promise', so a revision hurts more when certainty was claimed (1). "
   "The good doctor 'does not pretend that a hard trade-off is a purely technical question', which implies that some decisions involve values as well as facts (2).",
   "दोनों वैध हैं। पहले निश्चित बताकर दी गई सलाह 'बाद में होने वाले हर संशोधन' को 'टूटे वादे जैसा' बना देती है, इसलिए निश्चितता का दावा करने पर संशोधन अधिक चोट करता है (1)। "
   "अच्छा डॉक्टर 'किसी कठिन संतुलन को पूरी तरह तकनीकी प्रश्न होने का दिखावा नहीं करता', जिसका आशय है कि कुछ निर्णयों में तथ्यों के साथ मूल्य भी जुड़े होते हैं (2)।",
   "conclusions",
   st=["Advice that is later revised does more harm to trust if it was first presented as certain.",
       "Some decisions in a crisis involve choices of value as well as technical facts."],
   st_hi=["बाद में बदली जाने वाली सलाह भरोसे को अधिक हानि पहुँचाती है यदि उसे पहले निश्चित बताकर दिया गया हो।",
          "संकट के समय कुछ निर्णयों में तकनीकी तथ्यों के साथ मूल्यों के चुनाव भी शामिल होते हैं।"],
   key=2)
RQ(p, "Specific Detail", "easy", "mcq",
   "According to the passage, people trust a doctor who:",
   "परिच्छेद के अनुसार लोग उस डॉक्टर पर भरोसा करते हैं जो:",
   "The passage lists three marks of a trusted doctor, among them one 'who changes her advice when the evidence changes'. The other options invert the other two marks: she explains what she does not know, "
   "and does not pretend a hard trade-off is purely technical; always giving the same advice contradicts changing it with the evidence.",
   "परिच्छेद भरोसेमंद डॉक्टर के तीन लक्षण बताता है, जिनमें एक वह है 'जो प्रमाण बदलने पर अपनी सलाह बदलती है'। बाक़ी विकल्प दूसरे दो लक्षणों को उलट देते हैं: वह बताती है कि वह क्या नहीं जानती, "
   "और कठिन संतुलन को पूरी तरह तकनीकी होने का दिखावा नहीं करती; हमेशा एक ही सलाह देना प्रमाण के साथ सलाह बदलने का खंडन करता है।",
   "detail",
   opts=["changes her advice when the evidence changes",
         "never admits that there is anything she does not know",
         "treats every hard trade-off as a purely technical question",
         "always gives the same advice whatever the case may be"],
   opts_hi=["प्रमाण बदलने पर अपनी सलाह बदलती है",
            "कभी स्वीकार नहीं करती कि कुछ ऐसा है जो वह नहीं जानती",
            "हर कठिन संतुलन को पूरी तरह तकनीकी प्रश्न मानती है",
            "हर मामले में हमेशा एक ही सलाह देती है"],
   ans=0, pos=0)
