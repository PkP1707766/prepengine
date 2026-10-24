# -*- coding: utf-8 -*-
"""CSAT Level 4 · Simulator 1 -- Reading Comprehension: 9 original passages, 27 items (9 x 3), Layout A.

Passages in the voice of an op-ed or think-piece, each with a turn -- a claim, then its limit -- so that the items test
where the author stops. Themes, none used in Levels 1-3: compulsory licences for patented medicines, the idea of
swaraj in Hind Swaraj, minimum wages, language and attention, power lines and the great Indian bustard, the upkeep of
open-source software, the paradox of choice, dams and starving deltas, and green hydrogen. Item types: main idea 6,
best summary 3, inference 10, assumption 4, tone 1, specific detail 3. Difficulty 1 easy / 15 medium / 11 hard.
Options are named by content in every explanation."""
from csat_common import passage, RQ

CRUX = "Which one of the following statements best reflects the crux of the passage?"
CRUX_HI = "निम्नलिखित में से कौन-सा कथन परिच्छेद के सार को सबसे अच्छी तरह व्यक्त करता है?"
MSG = "Which one of the following statements best reflects the most logical and rational message conveyed by the passage?"
MSG_HI = "निम्नलिखित में से कौन-सा कथन परिच्छेद द्वारा दिए गए सबसे तार्किक और विवेकपूर्ण संदेश को सबसे अच्छी तरह व्यक्त करता है?"
VALID = "On the basis of the passage, which of the following conclusions is/are valid?"
VALID_HI = "परिच्छेद के आधार पर निम्नलिखित में से कौन-सा/से निष्कर्ष वैध है/हैं?"
ASSUME = "Which of the following assumptions has/have been made in the passage?"
ASSUME_HI = "परिच्छेद में निम्नलिखित में से कौन-सी पूर्वधारणा/एँ बनाई गई है/हैं?"

# ------------------------------------------------------------------ P01 compulsory licences for medicines (3)
p = passage("p01",
  "A patent gives the inventor of a new medicine the sole right to make and sell it for twenty years, and the high price this allows is meant to repay years of costly research, much of which fails. But a price that recovers research costs in rich countries can put a medicine out of reach of patients in poor ones. "
  "International trade rules therefore let a government issue a compulsory licence: permission for another firm to make a patented medicine without the patent holder's consent, in return for a royalty. In 2012 India issued its first such licence, allowing an Indian company to sell a patented cancer drug at a small fraction of the patent holder's price. "
  "Licences of this kind are a safety valve, not a business model. If governments issued them whenever a medicine seemed expensive, firms would have less reason to invest in research on diseases that mainly afflict poorer countries, and the patients the licences were meant to help would end up with fewer new medicines. "
  "Used sparingly, for medicines that are needed and priced far beyond reach, they correct the patent system without undoing it.",
  "पेटेंट किसी नई दवा के आविष्कारक को बीस वर्षों तक उसे बनाने और बेचने का एकमात्र अधिकार देता है, और इससे संभव ऊँचा मूल्य वर्षों के महँगे शोध की भरपाई के लिए है, जिसका बड़ा भाग विफल हो जाता है। पर जो मूल्य धनी देशों में शोध की लागत वसूल करता है, वह निर्धन देशों के रोगियों की पहुँच से दवा को बाहर कर सकता है। "
  "इसलिए अंतरराष्ट्रीय व्यापार नियम किसी सरकार को अनिवार्य लाइसेंस जारी करने देते हैं: किसी अन्य कंपनी को पेटेंट धारक की सहमति के बिना, रॉयल्टी के बदले, पेटेंट वाली दवा बनाने की अनुमति। 2012 में भारत ने ऐसा अपना पहला लाइसेंस जारी किया, जिससे एक भारतीय कंपनी कैंसर की एक पेटेंट वाली दवा पेटेंट धारक के मूल्य के एक छोटे-से अंश पर बेच सकी। "
  "इस प्रकार के लाइसेंस एक सुरक्षा-वाल्व हैं, व्यापार का ढंग नहीं। यदि सरकारें जब भी कोई दवा महँगी लगे तभी इन्हें जारी करने लगें, तो कंपनियों के पास उन रोगों पर शोध में निवेश का कम कारण रहेगा जो मुख्यतः निर्धन देशों को सताते हैं, और जिन रोगियों की सहायता के लिए लाइसेंस थे उन्हें अंततः कम नई दवाएँ मिलेंगी। "
  "संयम से, उन दवाओं के लिए प्रयोग किए जाएँ जो आवश्यक हैं और पहुँच से बहुत ऊपर के मूल्य पर हैं, तो वे पेटेंट व्यवस्था को मिटाए बिना उसे सुधारते हैं।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage defends compulsory licences as a way to bring needed medicines within reach, and in the same breath limits them: issued routinely, they would weaken the research that produces new medicines. The crux holds both halves. "
   "It does not want patents replaced -- the licences 'correct the patent system without undoing it'; it says one cancer drug was priced far beyond reach, not that patented medicines always are; and it argues that firms' research does respond to the rules, which contradicts the claim that they invest the same whatever the rules.",
   "परिच्छेद अनिवार्य लाइसेंसों का बचाव आवश्यक दवाओं को पहुँच में लाने के साधन के रूप में करता है, और साथ ही उन्हें सीमित करता है: नियमित रूप से जारी होने पर वे उस शोध को कमज़ोर करेंगे जिससे नई दवाएँ बनती हैं। सार दोनों हिस्सों को साथ रखता है। "
   "वह पेटेंटों को हटाना नहीं चाहता -- लाइसेंस 'पेटेंट व्यवस्था को मिटाए बिना उसे सुधारते हैं'; वह कहता है कि कैंसर की एक दवा का मूल्य पहुँच से बहुत ऊपर था, यह नहीं कि पेटेंट वाली दवाएँ हमेशा ऐसी होती हैं; और वह तर्क देता है कि कंपनियों का शोध नियमों से प्रभावित होता है, जो इस दावे का खंडन करता है कि वे नियम चाहे जो हों, उतना ही निवेश करती हैं।",
   "crux",
   opts=["Patents on medicines do more harm than good and should be replaced altogether by compulsory licences.",
         "Compulsory licences can widen access to medicines but must be rare, or they will deter research.",
         "India's first compulsory licence showed that patented medicines are always overpriced everywhere.",
         "Firms invest in research only on the diseases of rich countries, whatever the patent rules may be."],
   opts_hi=["दवाओं पर पेटेंट लाभ से अधिक हानि करते हैं और उन्हें पूरी तरह अनिवार्य लाइसेंसों से बदल देना चाहिए।",
            "अनिवार्य लाइसेंस दवाओं की पहुँच बढ़ा सकते हैं, पर वे विरले हों, वरना शोध को हतोत्साहित करेंगे।",
            "भारत के पहले अनिवार्य लाइसेंस ने दिखाया कि पेटेंट वाली दवाएँ हर जगह हमेशा ज़रूरत से ज़्यादा महँगी होती हैं।",
            "पेटेंट के नियम चाहे जो हों, कंपनियाँ केवल धनी देशों के रोगों पर ही शोध में निवेश करती हैं।"],
   ans=1, pos=1)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Neither is valid. 1 contradicts the passage: the other firm makes the medicine 'in return for a royalty', so the patent holder is paid. "
   "2 goes beyond the passage, which warns that routine licences would weaken research but makes no claim that the 2012 licence, a single and sparing use, reduced research on cancer medicines.",
   "कोई भी वैध नहीं। 1 परिच्छेद का खंडन करता है: दूसरी कंपनी दवा 'रॉयल्टी के बदले' बनाती है, इसलिए पेटेंट धारक को भुगतान मिलता है। "
   "2 परिच्छेद से आगे जाता है, जो चेताता है कि नियमित लाइसेंस शोध को कमज़ोर करेंगे, पर यह दावा नहीं करता कि 2012 के लाइसेंस ने, जो एक अकेला और संयमित प्रयोग था, कैंसर की दवाओं पर शोध घटाया।",
   "conclusions",
   st=["Under the rules described, a compulsory licence lets another firm make a patented medicine without paying the patent holder anything.",
       "The passage implies that India's licence of 2012 reduced the money spent on research into cancer medicines."],
   st_hi=["बताए गए नियमों के अंतर्गत अनिवार्य लाइसेंस किसी अन्य कंपनी को पेटेंट धारक को कुछ भी चुकाए बिना पेटेंट वाली दवा बनाने देता है।",
          "परिच्छेद का निहितार्थ है कि भारत के 2012 के लाइसेंस ने कैंसर की दवाओं पर शोध में ख़र्च होने वाला धन घटाया।"],
   key=3)
RQ(p, "Assumption", "medium", "s2", ASSUME, ASSUME_HI,
   "Only 1 is assumed. The warning that frequent licences would leave firms 'less reason to invest' in some diseases works only if the profits firms expect from patents shape where they spend on research. "
   "2 is not assumed: the passage speaks of research by firms and of patients in poor countries, but its argument does not depend on poor countries being unable to develop medicines of their own.",
   "केवल 1 पूर्वधारणा है। यह चेतावनी कि बार-बार के लाइसेंस कंपनियों के पास कुछ रोगों में 'निवेश का कम कारण' छोड़ेंगे, तभी चलती है जब पेटेंटों से अपेक्षित लाभ यह तय करें कि कंपनियाँ शोध पर कहाँ ख़र्च करती हैं। "
   "2 पूर्वधारणा नहीं है: परिच्छेद कंपनियों के शोध और निर्धन देशों के रोगियों की बात करता है, पर उसका तर्क इस पर निर्भर नहीं कि निर्धन देश अपनी दवाएँ विकसित नहीं कर सकते।",
   "assumptions",
   st=["The profits firms expect from patents influence how much they spend on research into particular diseases.",
       "Poor countries are unable to develop new medicines of their own."],
   st_hi=["पेटेंटों से अपेक्षित लाभ यह प्रभावित करते हैं कि कंपनियाँ किसी रोग विशेष के शोध पर कितना ख़र्च करती हैं।",
          "निर्धन देश अपनी नई दवाएँ विकसित करने में असमर्थ हैं।"],
   key=0)

# ------------------------------------------------------------------ P02 the idea of swaraj in Hind Swaraj (3)
p = passage("p02",
  "In 1909, on a voyage from London to South Africa, Gandhi wrote Hind Swaraj, a short book in the form of a dialogue between an editor and an impatient reader. The reader wants the British driven out. "
  "Gandhi's editor asks what would be gained if Indians then ran the same courts, the same army and the same machinery of rule in the same spirit: the country would have changed its masters, not its condition. "
  "Swaraj, the book argues, means self-rule in a double sense -- a people governing its own affairs, and each person learning to govern his or her own desires. A nation of people who cannot rule themselves cannot be free merely because its rulers are its own. "
  "The book's wholesale rejection of railways, lawyers and modern medicine has struck many readers, then and since, as too sweeping. Its lasting point lies elsewhere: that freedom is a quality of conduct as much as a change of government, and that the means chosen to win it shape what is won.",
  "1909 में, लंदन से दक्षिण अफ़्रीका की एक समुद्री यात्रा में, गांधी ने 'हिंद स्वराज' लिखी, एक संपादक और एक अधीर पाठक के बीच संवाद के रूप में एक छोटी पुस्तक। पाठक चाहता है कि अंग्रेज़ों को निकाल दिया जाए। "
  "गांधी का संपादक पूछता है कि यदि भारतीय तब वही न्यायालय, वही सेना और शासन की वही मशीनरी उसी भावना से चलाएँ, तो क्या मिलेगा: देश ने अपने स्वामी बदले होंगे, अपनी दशा नहीं। "
  "पुस्तक का तर्क है कि स्वराज का अर्थ दोहरे अर्थ में स्व-शासन है -- एक जनता का अपने मामलों का शासन करना, और हर व्यक्ति का अपनी इच्छाओं पर शासन करना सीखना। जो राष्ट्र ऐसे लोगों का है जो स्वयं पर शासन नहीं कर सकते, वह केवल इसलिए स्वतंत्र नहीं हो सकता कि उसके शासक उसके अपने हैं। "
  "रेलवे, वकीलों और आधुनिक चिकित्सा को पुस्तक का थोक में अस्वीकार करना तब से अब तक अनेक पाठकों को बहुत व्यापक लगा है। उसका स्थायी बिंदु कहीं और है: कि स्वतंत्रता शासन के बदलाव जितनी ही आचरण का एक गुण है, और कि उसे पाने के लिए चुने गए साधन तय करते हैं कि क्या पाया जाता है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage presents the book's central idea: swaraj is self-rule both of the nation and of the person, so that replacing British rulers with Indian ones in the same spirit would not be freedom. "
   "The passage says the means 'shape what is won', so swaraj is not a matter of driving the British out by any means; it calls the rejection of machines and professions 'too sweeping' and places the lasting point elsewhere; and taking over the courts and army in the same spirit is exactly what the editor says would change only the masters.",
   "परिच्छेद पुस्तक के केंद्रीय विचार को प्रस्तुत करता है: स्वराज राष्ट्र और व्यक्ति दोनों का स्व-शासन है, इसलिए अंग्रेज़ शासकों की जगह उसी भावना से भारतीय शासक बिठाना स्वतंत्रता नहीं होगी। "
   "परिच्छेद कहता है कि साधन 'तय करते हैं कि क्या पाया जाता है', इसलिए स्वराज किसी भी साधन से अंग्रेज़ों को निकालने का मामला नहीं; वह मशीनों और पेशों के अस्वीकार को 'बहुत व्यापक' कहता है और स्थायी बिंदु को कहीं और रखता है; और न्यायालयों और सेना को उसी भावना से अपने हाथ में लेना ठीक वही है जिसके बारे में संपादक कहता है कि उससे केवल स्वामी बदलेंगे।",
   "crux",
   opts=["Gandhi wanted the British to leave India at once, whatever the means needed to make them go.",
         "Hind Swaraj argues that modern machines are the main obstacle standing in the way of India's freedom.",
         "For Gandhi, true swaraj required self-government of the person as well as of the nation.",
         "Indians would be free as soon as they took over the courts and the army from the British."],
   opts_hi=["गांधी चाहते थे कि अंग्रेज़ तुरंत भारत छोड़ें, उन्हें निकालने के लिए चाहे जो साधन लगें।",
            "'हिंद स्वराज' का तर्क है कि आधुनिक मशीनें भारत की स्वतंत्रता के रास्ते की मुख्य बाधा हैं।",
            "गांधी के लिए सच्चे स्वराज में राष्ट्र के साथ-साथ व्यक्ति का स्व-शासन भी आवश्यक था।",
            "भारतीय तभी स्वतंत्र हो जाते जब वे अंग्रेज़ों से न्यायालय और सेना अपने हाथ में ले लेते।"],
   ans=2, pos=2)
RQ(p, "Inference", "hard", "mcq",
   "Which one of the following would the editor in Hind Swaraj, as described in the passage, most likely regard as falling short of swaraj?",
   "परिच्छेद में वर्णित 'हिंद स्वराज' का संपादक निम्नलिखित में से किसे सबसे अधिक संभावना से स्वराज से कम मानेगा?",
   "The editor's objection is to Indians running 'the same machinery of rule in the same spirit': officials who carry on the inherited system as their predecessors did have changed the masters, not the condition. "
   "A village council settling its own disputes is a people governing its own affairs; a person giving up a habit she cannot control is learning to govern her desires; and a movement that refuses violence because of its means reflects the book's view that the means shape what is won.",
   "संपादक की आपत्ति भारतीयों के 'शासन की वही मशीनरी उसी भावना से' चलाने पर है: जो अधिकारी विरासत में मिली व्यवस्था को अपने पूर्ववर्तियों की तरह चलाते हैं, उन्होंने स्वामी बदले हैं, दशा नहीं। "
   "अपने विवाद ख़ुद निपटाने वाली ग्राम परिषद एक जनता का अपने मामलों का शासन है; जिस आदत पर नियंत्रण न हो उसे छोड़ने वाली व्यक्ति अपनी इच्छाओं पर शासन करना सीख रही है; और साधनों के कारण हिंसा से इनकार करने वाला आंदोलन पुस्तक के इस विचार को दर्शाता है कि साधन तय करते हैं कि क्या पाया जाता है।",
   "what-falls-short-of-swaraj",
   opts=["Indian officials running the inherited system of rule in the same spirit as their predecessors",
         "A village council that settles its own disputes without any appeal to officials far away from it",
         "A person who gives up a habit she cannot control, though no law of any kind requires her to",
         "A movement that refuses to use violence even where violence might bring success more quickly"],
   opts_hi=["विरासत में मिली शासन-व्यवस्था को अपने पूर्ववर्तियों की ही भावना से चलाने वाले भारतीय अधिकारी",
            "एक ग्राम परिषद जो दूर बैठे अधिकारियों से कोई अपील किए बिना अपने विवाद स्वयं निपटाती है",
            "एक व्यक्ति जो ऐसी आदत छोड़ देती है जिस पर उसका नियंत्रण नहीं, यद्यपि कोई क़ानून ऐसा नहीं कहता",
            "एक आंदोलन जो वहाँ भी हिंसा से इनकार करता है जहाँ हिंसा से सफलता अधिक जल्दी मिल सकती है"],
   ans=0, pos=0)
RQ(p, "Specific Detail", "easy", "mcq",
   "According to the passage, in what form is Hind Swaraj written?",
   "परिच्छेद के अनुसार, 'हिंद स्वराज' किस रूप में लिखी गई है?",
   "The passage calls it 'a short book in the form of a dialogue between an editor and an impatient reader'. It was written on a voyage, but it is not a diary of one, and the passage mentions no letters and no report to any organisation.",
   "परिच्छेद इसे 'एक संपादक और एक अधीर पाठक के बीच संवाद के रूप में एक छोटी पुस्तक' कहता है। यह एक यात्रा में लिखी गई, पर उस यात्रा की डायरी नहीं है, और परिच्छेद किसी पत्र या किसी संगठन को दी गई रिपोर्ट का उल्लेख नहीं करता।",
   "the-form-of-the-book",
   opts=["A collection of letters to his followers in India",
         "A diary of a sea voyage from London to South Africa",
         "A report written for the Indian National Congress",
         "A dialogue between an editor and a reader"],
   opts_hi=["भारत में उनके अनुयायियों को लिखे पत्रों का संग्रह",
            "लंदन से दक्षिण अफ़्रीका की समुद्री यात्रा की डायरी",
            "भारतीय राष्ट्रीय कांग्रेस के लिए लिखी गई एक रिपोर्ट",
            "एक संपादक और एक पाठक के बीच संवाद"],
   ans=3, pos=3)

# ------------------------------------------------------------------ P03 minimum wages (3)
p = passage("p03",
  "The textbook case against a minimum wage is simple: if the law sets pay above what the market would offer, employers will hire fewer workers, and the people it was meant to help will lose their jobs. The argument assumes, however, that employers must pay whatever the market rate is. "
  "In many towns a few large employers dominate hiring, and workers with nowhere else to go accept less than their work is worth to the firm. There, a moderate minimum wage can raise pay without reducing jobs, and may even draw more people into work. Studies of moderate increases in several countries have found little or no loss of employment. "
  "The word that matters is moderate. A minimum set far above what local businesses earn will close small firms or push work beyond the reach of the law -- a serious risk in India, where most workers are informal and enforcement is thin. "
  "A minimum wage is neither a free gift nor a sure destroyer of jobs; its effect depends on its level against local pay.",
  "न्यूनतम मज़दूरी के विरुद्ध पाठ्यपुस्तक का तर्क सरल है: यदि क़ानून वेतन को उससे ऊपर तय करे जो बाज़ार देता, तो नियोक्ता कम कामगार रखेंगे, और जिनकी सहायता के लिए यह था वे अपनी नौकरियाँ खो देंगे। पर यह तर्क मान लेता है कि नियोक्ताओं को बाज़ार की दर ही देनी पड़ती है, वह जो भी हो। "
  "कई नगरों में कुछ बड़े नियोक्ता भर्ती पर हावी होते हैं, और जिन कामगारों के पास और कहीं जाने को नहीं, वे अपने काम के फ़र्म के लिए मूल्य से कम स्वीकार कर लेते हैं। वहाँ एक संयत न्यूनतम मज़दूरी नौकरियाँ घटाए बिना वेतन बढ़ा सकती है, और अधिक लोगों को काम की ओर खींच भी सकती है। कई देशों में संयत वृद्धियों के अध्ययनों में रोज़गार की बहुत कम या कोई हानि नहीं पाई गई है। "
  "महत्त्व का शब्द 'संयत' है। स्थानीय व्यवसायों की कमाई से बहुत ऊपर तय की गई न्यूनतम मज़दूरी छोटी फ़र्मों को बंद कर देगी या काम को क़ानून की पहुँच से बाहर धकेल देगी -- भारत में यह गंभीर जोखिम है, जहाँ अधिकांश कामगार अनौपचारिक हैं और प्रवर्तन कमज़ोर है। "
  "न्यूनतम मज़दूरी न मुफ़्त का उपहार है न नौकरियों का निश्चित विनाशक; उसका प्रभाव स्थानीय वेतन की तुलना में उसके स्तर पर निर्भर है।")
RQ(p, "Best Summary", "medium", "mcq", MSG, MSG_HI,
   "The passage rejects both extremes and ends by saying that a minimum wage's effect 'depends on its level against local pay': moderate minimums need not cost jobs, high ones can. "
   "It does not say minimum wages always destroy jobs, nor that they can never harm workers -- it warns that a high one closes small firms; and breaking up large employers is not proposed anywhere.",
   "परिच्छेद दोनों अतियों को अस्वीकार करता है और अंत में कहता है कि न्यूनतम मज़दूरी का प्रभाव 'स्थानीय वेतन की तुलना में उसके स्तर पर निर्भर है': संयत न्यूनतम मज़दूरी से नौकरियाँ घटना आवश्यक नहीं, ऊँची से घट सकती हैं। "
   "वह यह नहीं कहता कि न्यूनतम मज़दूरी हमेशा नौकरियाँ नष्ट करती है, और न यह कि वह कामगारों को कभी हानि नहीं पहुँचा सकती -- वह चेताता है कि ऊँची मज़दूरी छोटी फ़र्मों को बंद कर देती है; और बड़े नियोक्ताओं को तोड़ने का प्रस्ताव कहीं नहीं है।",
   "message",
   opts=["Minimum wages always destroy jobs, and so the law should leave all pay to be set by the market.",
         "A minimum wage can never harm workers, and so it should be set as high as the law will allow.",
         "Large employers should be broken up, so that workers in every town have more choice of jobs.",
         "Whether a minimum wage costs jobs depends on how high it is set against local pay."],
   opts_hi=["न्यूनतम मज़दूरी हमेशा नौकरियाँ नष्ट करती है, इसलिए क़ानून को सारा वेतन बाज़ार पर छोड़ देना चाहिए।",
            "न्यूनतम मज़दूरी कामगारों को कभी हानि नहीं पहुँचा सकती, इसलिए उसे क़ानून की अनुमति जितना ऊँचा रखना चाहिए।",
            "बड़े नियोक्ताओं को तोड़ देना चाहिए, ताकि हर नगर के कामगारों के पास नौकरियों का अधिक विकल्प हो।",
            "न्यूनतम मज़दूरी से नौकरियाँ घटेंगी या नहीं, यह स्थानीय वेतन की तुलना में उसके स्तर पर निर्भर है।"],
   ans=3, pos=3)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Both are valid. 1: where a few employers dominate hiring, the passage says a moderate minimum 'can raise pay without reducing jobs' -- so in a one-employer town it need not reduce employment. "
   "2: the passage warns that where most workers are informal and enforcement is thin, a high minimum pushes work 'beyond the reach of the law'; so such a wage may help fewer people than its headline suggests.",
   "दोनों वैध हैं। 1: जहाँ कुछ नियोक्ता भर्ती पर हावी हैं, वहाँ परिच्छेद कहता है कि संयत न्यूनतम मज़दूरी 'नौकरियाँ घटाए बिना वेतन बढ़ा सकती है' -- इसलिए एक नियोक्ता वाले नगर में रोज़गार घटना आवश्यक नहीं। "
   "2: परिच्छेद चेताता है कि जहाँ अधिकांश कामगार अनौपचारिक हैं और प्रवर्तन कमज़ोर है, वहाँ ऊँची न्यूनतम मज़दूरी काम को 'क़ानून की पहुँच से बाहर' धकेलती है; इसलिए ऐसी मज़दूरी जितने लोगों की सहायता करती दिखती है उससे कम की कर सकती है।",
   "conclusions",
   st=["In a town where one large firm does nearly all the hiring, a moderate minimum wage need not reduce employment.",
       "Where most workers are informal and the law is weakly enforced, a high minimum wage may help fewer people than it appears to."],
   st_hi=["जिस नगर में लगभग सारी भर्ती एक बड़ी फ़र्म करती है, वहाँ संयत न्यूनतम मज़दूरी से रोज़गार घटना आवश्यक नहीं।",
          "जहाँ अधिकांश कामगार अनौपचारिक हैं और क़ानून का प्रवर्तन कमज़ोर है, वहाँ ऊँची न्यूनतम मज़दूरी जितने लोगों की सहायता करती दिखती है, उससे कम की कर सकती है।"],
   key=2)
RQ(p, "Assumption", "hard", "mcq",
   "According to the passage, the textbook argument against a minimum wage assumes that:",
   "परिच्छेद के अनुसार, न्यूनतम मज़दूरी के विरुद्ध पाठ्यपुस्तक का तर्क यह मान लेता है कि:",
   "The passage says so directly: the argument 'assumes ... that employers must pay whatever the market rate is' -- that is, they have no power to pay less. Its point is that this fails where a few employers dominate. "
   "Nothing in the textbook argument concerns a preference for informal work, the relative earnings of small and large firms, or whether workers would rather have higher pay than a job.",
   "परिच्छेद यह सीधे कहता है: तर्क 'मान लेता है ... कि नियोक्ताओं को बाज़ार की दर ही देनी पड़ती है' -- यानी उनके पास कम देने की कोई शक्ति नहीं। उसका बिंदु यह है कि जहाँ कुछ नियोक्ता हावी हों, वहाँ यह विफल होता है। "
   "पाठ्यपुस्तक के तर्क में अनौपचारिक काम के प्रति झुकाव, छोटी और बड़ी फ़र्मों की तुलनात्मक कमाई, या इस बात का कोई संबंध नहीं कि कामगार नौकरी से अधिक ऊँचा वेतन चाहेंगे।",
   "what-the-textbook-argument-assumes",
   opts=["most workers would rather do informal work than hold a formal job with a fixed wage",
         "employers have no power to pay less than the market rate",
         "small firms in most towns earn more than the large firms that dominate hiring there",
         "most workers would rather have higher pay than keep a job at a lower wage"],
   opts_hi=["अधिकांश कामगार निश्चित वेतन वाली औपचारिक नौकरी के बजाय अनौपचारिक काम करना पसंद करेंगे",
            "नियोक्ताओं के पास बाज़ार की दर से कम देने की कोई शक्ति नहीं है",
            "अधिकांश नगरों की छोटी फ़र्में वहाँ भर्ती पर हावी बड़ी फ़र्मों से अधिक कमाती हैं",
            "अधिकांश कामगार कम वेतन पर नौकरी बचाए रखने के बजाय ऊँचा वेतन चाहेंगे"],
   ans=1, pos=1)

# ------------------------------------------------------------------ P04 language and attention (3)
p = passage("p04",
  "It is sometimes claimed that the language we speak sets the limits of what we can think: if a language has no word for a colour, its speakers cannot see it. Put so strongly, the claim fails. People notice differences their language does not name, and whatever can be said in one language can, with some effort, be said in another. "
  "A weaker version has better support. Russian has separate basic words for light blue and dark blue, and in experiments Russian speakers tell those two shades apart a little faster than English speakers do. "
  "Speakers of some Australian languages describe positions by compass directions rather than by left and right -- 'the cup is north of the plate' -- and they keep track of which way they are facing with remarkable accuracy. "
  "Language, on this evidence, does not imprison thought, but it trains attention: the distinctions a language obliges its speakers to make every day become the ones they make quickly and without effort.",
  "कभी-कभी दावा किया जाता है कि हम जो भाषा बोलते हैं वह हमारी सोच की सीमाएँ तय करती है: यदि किसी भाषा में किसी रंग के लिए शब्द नहीं है, तो उसके बोलने वाले उसे देख नहीं सकते। इतने प्रबल रूप में रखा जाए तो दावा विफल होता है। लोग ऐसे अंतर देखते हैं जिनका नाम उनकी भाषा में नहीं, और जो एक भाषा में कहा जा सकता है वह कुछ प्रयास से दूसरी में भी कहा जा सकता है। "
  "एक कमज़ोर रूप को बेहतर समर्थन है। रूसी भाषा में हल्के नीले और गहरे नीले के लिए अलग-अलग मूल शब्द हैं, और प्रयोगों में रूसी बोलने वाले उन दो रंगतों को अंग्रेज़ी बोलने वालों से थोड़ा जल्दी अलग पहचानते हैं। "
  "कुछ ऑस्ट्रेलियाई भाषाओं के बोलने वाले स्थितियों का वर्णन दाएँ-बाएँ के बजाय दिशाओं से करते हैं -- 'प्याला थाली के उत्तर में है' -- और वे उल्लेखनीय सटीकता से याद रखते हैं कि उनका मुँह किस दिशा में है। "
  "इस साक्ष्य के अनुसार भाषा सोच को क़ैद नहीं करती, पर ध्यान को प्रशिक्षित करती है: जो भेद कोई भाषा अपने बोलने वालों से हर दिन करवाती है, वही वे भेद बन जाते हैं जिन्हें वे जल्दी और बिना प्रयास के करते हैं।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage rejects the strong claim that language limits thought and accepts a weaker one: language 'trains attention', so that the distinctions it requires are made readily. "
   "That speakers cannot see unnamed colours is the strong claim the passage rejects; the Russian speakers were 'a little faster' at one distinction, not more accurate in every respect; and the passage compares no languages on how well they describe positions.",
   "परिच्छेद इस प्रबल दावे को अस्वीकार करता है कि भाषा सोच को सीमित करती है और एक कमज़ोर दावे को स्वीकार करता है: भाषा 'ध्यान को प्रशिक्षित करती है', जिससे वह जिन भेदों की माँग करती है वे सहजता से होते हैं। "
   "यह कि बोलने वाले बिना नाम के रंग नहीं देख सकते, वही प्रबल दावा है जिसे परिच्छेद अस्वीकार करता है; रूसी बोलने वाले एक भेद में 'थोड़ा जल्दी' थे, हर तरह से अधिक सटीक नहीं; और परिच्छेद स्थितियों के वर्णन में भाषाओं की कोई तुलना नहीं करता।",
   "crux",
   opts=["Language does not limit what we can think, but shapes what we notice readily.",
         "The speakers of a language cannot perceive any colour for which it has no name at all.",
         "Russian speakers see every colour more accurately than English speakers do.",
         "All the world's languages are equally good at describing positions in space."],
   opts_hi=["भाषा हमारी सोच को सीमित नहीं करती, पर तय करती है कि हम क्या जल्दी देखते हैं।",
            "किसी भाषा के बोलने वाले ऐसा कोई भी रंग नहीं देख सकते जिसका उस भाषा में कोई नाम नहीं है।",
            "रूसी बोलने वाले हर रंग को अंग्रेज़ी बोलने वालों से अधिक सटीकता से देखते हैं।",
            "दुनिया की सभी भाषाएँ स्थान में स्थितियों का वर्णन करने में समान रूप से अच्छी हैं।"],
   ans=0, pos=0)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Only 2 is valid. Speakers who describe positions by compass directions keep track of which way they face 'with remarkable accuracy', so they would probably notice a change in a room's orientation sooner than others. "
   "1 restates the strong claim the passage rejects: people 'notice differences their language does not name', so a missing word does not stop anyone learning to tell a shade apart.",
   "केवल 2 वैध है। दिशाओं से स्थितियों का वर्णन करने वाले बोलने वाले 'उल्लेखनीय सटीकता से' याद रखते हैं कि उनका मुँह किस ओर है, इसलिए वे किसी कमरे की दिशा में बदलाव को संभवतः दूसरों से जल्दी पहचानेंगे। "
   "1 वही प्रबल दावा दोहराता है जिसे परिच्छेद अस्वीकार करता है: लोग 'ऐसे अंतर देखते हैं जिनका नाम उनकी भाषा में नहीं', इसलिए किसी शब्द का न होना किसी को रंगत पहचानना सीखने से नहीं रोकता।",
   "conclusions",
   st=["A person whose language lacks a word for a shade cannot learn to tell that shade apart from others.",
       "Speakers of a language that uses compass directions would probably notice a change in a room's orientation sooner than others."],
   st_hi=["जिस व्यक्ति की भाषा में किसी रंगत के लिए शब्द नहीं, वह उस रंगत को दूसरों से अलग पहचानना नहीं सीख सकता।",
          "दिशाओं का प्रयोग करने वाली भाषा के बोलने वाले किसी कमरे की दिशा में बदलाव को संभवतः दूसरों से जल्दी पहचानेंगे।"],
   key=1)
RQ(p, "Author's Tone", "medium", "mcq",
   "The author's approach to the claim that language limits thought is best described as:",
   "इस दावे के प्रति कि भाषा सोच को सीमित करती है, लेखक का दृष्टिकोण सबसे अच्छी तरह इस प्रकार वर्णित है:",
   "The author rejects the claim 'put so strongly' but says that 'a weaker version has better support' and sets out the evidence for it -- a discriminating approach. "
   "It is not wholly dismissive, since part of the claim is accepted; not wholly accepting, since the strong form 'fails'; and not indifferent, since the author draws a conclusion from the evidence.",
   "लेखक 'इतने प्रबल रूप में रखे गए' दावे को अस्वीकार करता है, पर कहता है कि 'एक कमज़ोर रूप को बेहतर समर्थन है' और उसका साक्ष्य रखता है -- एक विवेकपूर्ण, भेद करने वाला दृष्टिकोण। "
   "यह पूरी तरह ख़ारिज करने वाला नहीं, क्योंकि दावे का एक भाग स्वीकार किया गया है; पूरी तरह स्वीकार करने वाला नहीं, क्योंकि प्रबल रूप 'विफल होता है'; और उदासीन नहीं, क्योंकि लेखक साक्ष्य से निष्कर्ष निकालता है।",
   "the-author-s-approach",
   opts=["Wholly dismissive: the passage finds no truth in any version of the claim.",
         "Wholly accepting: the passage defends the claim in its strongest form.",
         "Discriminating: it rejects the strong form but accepts a weaker one.",
         "Indifferent: the passage reports the evidence without judging the claim."],
   opts_hi=["पूरी तरह ख़ारिज करने वाला: परिच्छेद दावे के किसी भी रूप में कोई सत्य नहीं पाता।",
            "पूरी तरह स्वीकार करने वाला: परिच्छेद दावे का उसके प्रबलतम रूप में बचाव करता है।",
            "भेद करने वाला: वह प्रबल रूप अस्वीकार करता है पर कमज़ोर रूप स्वीकार करता है।",
            "उदासीन: परिच्छेद दावे का मूल्यांकन किए बिना साक्ष्य बताता है।"],
   ans=2, pos=2)

# ------------------------------------------------------------------ P05 power lines and the great Indian bustard (3)
p = passage("p05",
  "Clean energy is not free of costs to wildlife. Wind turbines kill birds and bats that fly into their blades, and the power lines that carry electricity from new solar and wind parks kill more. "
  "In the Thar desert, overhead lines have become a leading cause of death for the great Indian bustard, a critically endangered bird with poor forward vision that cannot easily see a wire in its path; fewer than two hundred are thought to survive. "
  "It does not follow that renewable energy should be abandoned: a warming climate threatens birds too, on a far larger scale. The harm depends mostly on where turbines and lines are placed. "
  "Keeping them out of the few areas where vulnerable birds breed and feed, burying lines or fitting them with markers where they cross such areas, and halting turbines during peak migration can cut deaths sharply at modest cost. The choice is not between clean power and birds, but between careless and careful siting.",
  "स्वच्छ ऊर्जा वन्यजीवों के लिए लागत से मुक्त नहीं है। पवन टर्बाइन उन पक्षियों और चमगादड़ों को मारते हैं जो उनके पंखों से टकराते हैं, और नए सौर और पवन पार्कों से बिजली ले जाने वाली बिजली की लाइनें और अधिक को मारती हैं। "
  "थार मरुस्थल में ऊपर से गुज़रती लाइनें गोडावण (ग्रेट इंडियन बस्टर्ड) की मृत्यु का एक प्रमुख कारण बन गई हैं, जो गंभीर रूप से संकटग्रस्त पक्षी है, जिसकी सामने देखने की क्षमता कमज़ोर है और जो अपने रास्ते में तार आसानी से नहीं देख पाता; माना जाता है कि दो सौ से भी कम बचे हैं। "
  "इससे यह नहीं निकलता कि नवीकरणीय ऊर्जा छोड़ दी जाए: गर्म होती जलवायु भी पक्षियों के लिए ख़तरा है, कहीं बड़े पैमाने पर। हानि मुख्यतः इस पर निर्भर है कि टर्बाइन और लाइनें कहाँ लगाई जाती हैं। "
  "उन्हें उन थोड़े-से क्षेत्रों से दूर रखना जहाँ संवेदनशील पक्षी प्रजनन करते और भोजन पाते हैं, ऐसे क्षेत्रों को पार करने वाली लाइनों को भूमिगत करना या उन पर चिह्नक लगाना, और प्रवास के चरम समय में टर्बाइन रोक देना, साधारण लागत पर मौतों को तेज़ी से घटा सकता है। चुनाव स्वच्छ बिजली और पक्षियों के बीच नहीं, बल्कि लापरवाह और सावधान स्थल-चयन के बीच है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage grants that clean energy harms birds and then argues that the harm 'depends mostly on where turbines and lines are placed', so careful siting can cut it sharply. "
   "It explicitly rejects abandoning renewable energy; it says climate change threatens birds 'on a far larger scale', the reverse of power lines being the greater danger; and it proposes siting and markers for the Thar, not a halt to every power project there.",
   "परिच्छेद स्वीकार करता है कि स्वच्छ ऊर्जा पक्षियों को हानि पहुँचाती है और फिर तर्क देता है कि हानि 'मुख्यतः इस पर निर्भर है कि टर्बाइन और लाइनें कहाँ लगाई जाती हैं', इसलिए सावधान स्थल-चयन उसे तेज़ी से घटा सकता है। "
   "वह नवीकरणीय ऊर्जा छोड़ने को स्पष्ट रूप से अस्वीकार करता है; वह कहता है कि जलवायु परिवर्तन पक्षियों के लिए 'कहीं बड़े पैमाने पर' ख़तरा है, जो लाइनों के अधिक बड़ा ख़तरा होने का उलटा है; और वह थार के लिए स्थल-चयन और चिह्नकों का प्रस्ताव करता है, वहाँ हर बिजली परियोजना रोकने का नहीं।",
   "crux",
   opts=["Renewable energy projects should be halted until they can be shown to cause no harm to wildlife.",
         "Power lines are a greater danger to birds than the warming of the climate is.",
         "The great Indian bustard can be saved only by stopping every power project in the Thar desert.",
         "The harm that clean energy does to birds can be greatly reduced by careful siting."],
   opts_hi=["नवीकरणीय ऊर्जा परियोजनाएँ तब तक रोकी जाएँ जब तक यह न दिखाया जा सके कि वे वन्यजीवों को कोई हानि नहीं पहुँचातीं।",
            "बिजली की लाइनें पक्षियों के लिए जलवायु के गर्म होने से भी बड़ा ख़तरा हैं।",
            "गोडावण को केवल थार मरुस्थल की हर बिजली परियोजना रोककर ही बचाया जा सकता है।",
            "स्वच्छ ऊर्जा से पक्षियों को होने वाली हानि सावधान स्थल-चयन से बहुत घटाई जा सकती है।"],
   ans=3, pos=3)
RQ(p, "Inference", "hard", "mcq",
   "Which one of the following can be inferred from the passage?",
   "परिच्छेद से निम्नलिखित में से क्या अनुमान लगाया जा सकता है?",
   "Since the harm depends on where lines are placed, and keeping them out of the areas where vulnerable birds breed and feed cuts deaths, a line that avoids a bustard's feeding grounds is likely to kill fewer bustards than one that crosses them. "
   "The passage blames turbines and power lines, not solar panels; it recommends burying lines only where they cross sensitive areas, which says nothing about burying them everywhere being cheapest; and it compares the danger to bats and birds nowhere.",
   "चूँकि हानि इस पर निर्भर है कि लाइनें कहाँ लगाई जाती हैं, और उन्हें संवेदनशील पक्षियों के प्रजनन और भोजन वाले क्षेत्रों से दूर रखने से मौतें घटती हैं, इसलिए गोडावण के भोजन-क्षेत्र से बचने वाली लाइन उसे पार करने वाली लाइन की तुलना में कम गोडावण मारेगी। "
   "परिच्छेद टर्बाइनों और बिजली की लाइनों को दोष देता है, सौर पैनलों को नहीं; वह लाइनों को केवल वहाँ भूमिगत करने की सलाह देता है जहाँ वे संवेदनशील क्षेत्रों को पार करती हैं, जिससे यह नहीं निकलता कि उन्हें हर जगह भूमिगत करना सबसे सस्ता है; और वह चमगादड़ों और पक्षियों के ख़तरे की तुलना कहीं नहीं करता।",
   "what-can-be-inferred-about-siting",
   opts=["Most of the birds killed by clean energy are killed by solar panels rather than by turbines or lines.",
         "Burying every power line in the country would be the cheapest way to protect its birds.",
         "A line that avoids a bustard's feeding grounds is likely to kill fewer of them than one crossing them.",
         "Bats are in greater danger from wind turbines than any of the birds that happen to live near them are."],
   opts_hi=["स्वच्छ ऊर्जा से मरने वाले अधिकांश पक्षी टर्बाइनों या लाइनों से नहीं, बल्कि सौर पैनलों से मरते हैं।",
            "देश की हर बिजली लाइन को भूमिगत करना उसके पक्षियों की रक्षा का सबसे सस्ता उपाय होगा।",
            "गोडावण के भोजन-क्षेत्र से बचने वाली लाइन उसे पार करने वाली लाइन से कम गोडावण मारेगी।",
            "चमगादड़ों को पवन टर्बाइनों से उनके पास रहने वाले किसी भी पक्षी से अधिक ख़तरा है।"],
   ans=2, pos=2)
RQ(p, "Assumption", "medium", "s2", ASSUME, ASSUME_HI,
   "Only 2 is assumed. Advice to keep turbines and lines out of 'the few areas where vulnerable birds breed and feed' can be followed only if those areas can be identified before the projects are built. "
   "1 is not assumed: the passage describes the bustard's plight in the Thar, but its argument does not need the bird to live nowhere else.",
   "केवल 2 पूर्वधारणा है। टर्बाइनों और लाइनों को 'उन थोड़े-से क्षेत्रों से दूर रखने' की सलाह, 'जहाँ संवेदनशील पक्षी प्रजनन करते और भोजन पाते हैं', तभी मानी जा सकती है जब परियोजनाएँ बनने से पहले उन क्षेत्रों की पहचान की जा सके। "
   "1 पूर्वधारणा नहीं है: परिच्छेद थार में गोडावण की दुर्दशा बताता है, पर उसके तर्क के लिए यह आवश्यक नहीं कि वह पक्षी और कहीं न रहता हो।",
   "assumptions",
   st=["The great Indian bustard is found nowhere except in the Thar desert.",
       "The places where vulnerable birds breed and feed can be identified before projects are built."],
   st_hi=["गोडावण थार मरुस्थल के अलावा और कहीं नहीं पाया जाता।",
          "जिन स्थानों पर संवेदनशील पक्षी प्रजनन करते और भोजन पाते हैं, उनकी पहचान परियोजनाएँ बनने से पहले की जा सकती है।"],
   key=1)

# ------------------------------------------------------------------ P06 the upkeep of open-source software (3)
p = passage("p06",
  "Much of the software that runs the internet -- in servers, phones, banks and government offices -- is open source: its code is published freely, and anyone may use, copy or change it. Such software is a kind of commons. Everyone can draw on it, but few pay for its upkeep, and many vital pieces are maintained by a handful of volunteers in their spare time. "
  "The risk became plain in 2014, when a serious flaw was found in a widely used program that protects data sent over the internet. The program secured a large share of the world's websites, yet it was looked after by very few people working on a tiny budget. "
  "Supporters of open source like to say that with enough eyes, every flaw is easy to find. Open code does allow anyone to inspect it, which closed code does not; but the eyes help only if someone actually looks. "
  "Since then, some of the companies that depend most on such software have begun to pay for its maintenance -- an admission that free to use is not the same as free to keep.",
  "इंटरनेट को चलाने वाला अधिकांश सॉफ़्टवेयर -- सर्वरों, फ़ोनों, बैंकों और सरकारी कार्यालयों में -- ओपन सोर्स है: उसका कोड मुक्त रूप से प्रकाशित होता है, और कोई भी उसका प्रयोग, नक़ल या बदलाव कर सकता है। ऐसा सॉफ़्टवेयर एक प्रकार का साझा संसाधन है। हर कोई उससे ले सकता है, पर उसके रख-रखाव का ख़र्च कम ही उठाते हैं, और कई महत्त्वपूर्ण भाग कुछ स्वयंसेवक अपने ख़ाली समय में सँभालते हैं। "
  "यह जोखिम 2014 में स्पष्ट हुआ, जब इंटरनेट पर भेजे जाने वाले डेटा की रक्षा करने वाले एक व्यापक रूप से प्रयुक्त प्रोग्राम में एक गंभीर त्रुटि पाई गई। वह प्रोग्राम दुनिया की वेबसाइटों के बड़े भाग को सुरक्षित करता था, फिर भी उसकी देखभाल बहुत कम लोग बहुत छोटे बजट पर करते थे। "
  "ओपन सोर्स के समर्थक कहना पसंद करते हैं कि पर्याप्त आँखें हों, तो हर त्रुटि आसानी से मिल जाती है। खुला कोड सचमुच किसी को भी उसे जाँचने देता है, जो बंद कोड नहीं देता; पर आँखें तभी मदद करती हैं जब कोई वास्तव में देखे। "
  "तब से, ऐसे सॉफ़्टवेयर पर सबसे अधिक निर्भर कुछ कंपनियों ने उसके रख-रखाव के लिए भुगतान शुरू किया है -- यह स्वीकारोक्ति कि प्रयोग के लिए मुफ़्त होना बनाए रखने के लिए मुफ़्त होना नहीं है।")
RQ(p, "Best Summary", "medium", "mcq", MSG, MSG_HI,
   "The passage ends with the lesson that 'free to use is not the same as free to keep': software that much depends on still needs someone to pay for its upkeep. "
   "It says open code allows inspection 'which closed code does not', so it does not call open source less secure; it makes no comparison of volunteers with paid programmers; and it doubts, rather than accepts, that publishing code ensures flaws are found.",
   "परिच्छेद इस सीख पर समाप्त होता है कि 'प्रयोग के लिए मुफ़्त होना बनाए रखने के लिए मुफ़्त होना नहीं है': जिस सॉफ़्टवेयर पर बहुत कुछ निर्भर है, उसके रख-रखाव का ख़र्च किसी को उठाना ही होगा। "
   "वह कहता है कि खुला कोड जाँच की अनुमति देता है 'जो बंद कोड नहीं देता', इसलिए वह ओपन सोर्स को कम सुरक्षित नहीं कहता; वह स्वयंसेवकों और वेतनभोगी प्रोग्रामरों की कोई तुलना नहीं करता; और वह इस पर संदेह करता है, उसे स्वीकार नहीं करता, कि कोड प्रकाशित करने से त्रुटियाँ मिलना सुनिश्चित होता है।",
   "message",
   opts=["Open-source software is less secure than closed software, and banks should stop using it.",
         "Freely available software that much depends on still needs someone to pay for its upkeep.",
         "Volunteers working in their spare time write better software than paid programmers do.",
         "Publishing a program's code ensures that every flaw in it will be found quickly by its users."],
   opts_hi=["ओपन सोर्स सॉफ़्टवेयर बंद सॉफ़्टवेयर से कम सुरक्षित है, और बैंकों को उसका प्रयोग बंद कर देना चाहिए।",
            "मुक्त रूप से उपलब्ध जिस सॉफ़्टवेयर पर बहुत कुछ निर्भर है, उसके रख-रखाव का ख़र्च फिर भी किसी को उठाना होगा।",
            "ख़ाली समय में काम करने वाले स्वयंसेवक वेतनभोगी प्रोग्रामरों से बेहतर सॉफ़्टवेयर लिखते हैं।",
            "किसी प्रोग्राम का कोड प्रकाशित करने से यह सुनिश्चित होता है कि उसकी हर त्रुटि उसके उपयोगकर्ता जल्दी खोज लेंगे।"],
   ans=1, pos=1)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Only 1 is valid. The passage says that open code 'does allow anyone to inspect it' but that 'the eyes help only if someone actually looks': being open to inspection does not ensure that anyone has inspected it. "
   "2 goes beyond the passage, which blames too few people and too little money for the 2014 flaw going unnoticed; it never says closed code would have avoided the flaw.",
   "केवल 1 वैध है। परिच्छेद कहता है कि खुला कोड 'किसी को भी उसे जाँचने देता है' पर 'आँखें तभी मदद करती हैं जब कोई वास्तव में देखे': जाँच के लिए खुला होना यह सुनिश्चित नहीं करता कि किसी ने उसे जाँचा है। "
   "2 परिच्छेद से आगे जाता है, जो 2014 की त्रुटि के अनदेखे रहने का दोष बहुत कम लोगों और बहुत कम धन को देता है; वह कहीं नहीं कहता कि बंद कोड से वह त्रुटि टल जाती।",
   "conclusions",
   st=["That a program's code can be inspected by anyone does not ensure that anyone has inspected it.",
       "The flaw found in 2014 would not have occurred if the program's code had been kept secret."],
   st_hi=["यह कि किसी प्रोग्राम का कोड कोई भी जाँच सकता है, यह सुनिश्चित नहीं करता कि किसी ने उसे जाँचा है।",
          "यदि प्रोग्राम का कोड गुप्त रखा जाता, तो 2014 में मिली त्रुटि होती ही नहीं।"],
   key=0)
RQ(p, "Specific Detail", "medium", "mcq",
   "Why does the passage call open-source software 'a kind of commons'?",
   "परिच्छेद ओपन सोर्स सॉफ़्टवेयर को 'एक प्रकार का साझा संसाधन' क्यों कहता है?",
   "The passage explains the word in the next sentence: 'Everyone can draw on it, but few pay for its upkeep.' It says nothing of joint ownership by governments or of a common programming language, and it says such software runs servers, banks and government offices, not that ordinary people use it more than companies.",
   "परिच्छेद अगले ही वाक्य में शब्द का अर्थ बताता है: 'हर कोई उससे ले सकता है, पर उसके रख-रखाव का ख़र्च कम ही उठाते हैं।' वह सरकारों के संयुक्त स्वामित्व या किसी साझी प्रोग्रामिंग भाषा की बात नहीं करता, और वह कहता है कि ऐसा सॉफ़्टवेयर सर्वरों, बैंकों और सरकारी कार्यालयों को चलाता है, यह नहीं कि साधारण लोग कंपनियों से अधिक उसका प्रयोग करते हैं।",
   "why-a-commons",
   opts=["Because it is owned and run jointly by all the governments that make use of it",
         "Because nearly all of it is written in one common programming language",
         "Because everyone can draw on it while few pay for its upkeep",
         "Because ordinary people use it far more than companies and offices do"],
   opts_hi=["क्योंकि उसका प्रयोग करने वाली सभी सरकारें उसकी संयुक्त स्वामी हैं और उसे मिलकर चलाती हैं",
            "क्योंकि उसका लगभग सारा भाग एक ही साझी प्रोग्रामिंग भाषा में लिखा गया है",
            "क्योंकि हर कोई उससे ले सकता है, जबकि उसके रख-रखाव का ख़र्च कम ही उठाते हैं",
            "क्योंकि साधारण लोग कंपनियों और कार्यालयों से कहीं अधिक उसका प्रयोग करते हैं"],
   ans=2, pos=2)

# ------------------------------------------------------------------ P07 the paradox of choice (3)
p = passage("p07",
  "In a well-known experiment, shoppers in a supermarket passed a stall offering free tastes of jam. On some days it displayed twenty-four flavours, on others six. The larger display drew more people to stop, but far fewer of those who stopped went on to buy a jar. "
  "The finding became the emblem of a broader claim: that beyond a point, more choice leaves people less able to decide and less satisfied with what they choose. The claim is less general than it sounds. Later attempts to repeat such experiments have produced mixed results, the effect sometimes large and sometimes absent. "
  "Choice seems to overwhelm when options are hard to compare, when people do not know what they want, and when a wrong pick is costly to undo; people with clear preferences, or with the knowledge to sort the options quickly, benefit from a wider range. "
  "The lesson for those who design menus, forms and public schemes is not to offer less, but to make what is offered easier to compare.",
  "एक प्रसिद्ध प्रयोग में एक सुपरमार्केट के ख़रीदार एक ऐसे स्टॉल के पास से गुज़रे जहाँ जैम मुफ़्त चखाया जा रहा था। कुछ दिन उस पर चौबीस स्वाद रखे गए, कुछ दिन छह। बड़े प्रदर्शन ने अधिक लोगों को रुकने के लिए खींचा, पर रुकने वालों में से कहीं कम लोगों ने आगे एक डिब्बा ख़रीदा। "
  "यह परिणाम एक व्यापक दावे का प्रतीक बन गया: कि एक सीमा के बाद अधिक विकल्प लोगों को निर्णय लेने में कम सक्षम और अपने चुनाव से कम संतुष्ट छोड़ते हैं। यह दावा जितना लगता है उतना सामान्य नहीं है। ऐसे प्रयोगों को दोहराने के बाद के प्रयासों के परिणाम मिले-जुले रहे हैं, प्रभाव कभी बड़ा तो कभी अनुपस्थित। "
  "विकल्प तब भारी पड़ते लगते हैं जब उनकी तुलना कठिन हो, जब लोग न जानते हों कि वे क्या चाहते हैं, और जब ग़लत चुनाव को पलटना महँगा हो; स्पष्ट पसंद वाले लोग, या विकल्पों को जल्दी छाँटने का ज्ञान रखने वाले, व्यापक दायरे से लाभ पाते हैं। "
  "मेनू, प्रपत्र और सार्वजनिक योजनाएँ बनाने वालों के लिए सीख कम विकल्प देने की नहीं, बल्कि जो दिया जाए उसकी तुलना आसान बनाने की है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage narrows a famous claim: more choice hinders decisions only under certain conditions, and so the remedy is to make options easier to compare, 'not to offer less'. "
   "It says the claim is 'less general than it sounds', so more choice does not always deter choosing; the jam study showed a difference in buying, not that six options are better in general; and its advice is the opposite of displaying as few products as possible.",
   "परिच्छेद एक प्रसिद्ध दावे को सीमित करता है: अधिक विकल्प केवल कुछ परिस्थितियों में निर्णय को बाधित करते हैं, इसलिए उपाय विकल्पों की तुलना आसान बनाना है, 'कम विकल्प देना नहीं'। "
   "वह कहता है कि दावा 'जितना लगता है उतना सामान्य नहीं', इसलिए अधिक विकल्प हमेशा चुनने से नहीं रोकते; जैम प्रयोग ने ख़रीद में अंतर दिखाया, यह नहीं कि सामान्यतः छह विकल्प बेहतर हैं; और उसकी सलाह जितने कम हो सकें उतने उत्पाद रखने का उलटा है।",
   "crux",
   opts=["Offering people more options always makes them less likely to choose anything at all.",
         "The jam experiment proved that six options are better than twenty-four in every kind of decision.",
         "More choice can hinder decisions in some conditions, so options should be made easy to compare.",
         "Shops should display as few products as they can manage in order to increase their sales."],
   opts_hi=["लोगों को अधिक विकल्प देने से वे हमेशा कुछ भी चुनने की कम संभावना रखते हैं।",
            "जैम प्रयोग ने सिद्ध किया कि हर प्रकार के निर्णय में छह विकल्प चौबीस से बेहतर हैं।",
            "कुछ परिस्थितियों में अधिक विकल्प निर्णय में बाधक हो सकते हैं, सो उनकी तुलना आसान हो।",
            "दुकानों को अपनी बिक्री बढ़ाने के लिए जितने कम हो सकें उतने उत्पाद प्रदर्शित करने चाहिए।"],
   ans=2, pos=2)
RQ(p, "Inference", "hard", "mcq",
   "In which one of the following situations would the passage expect a wide range of options to help rather than hinder?",
   "परिच्छेद के अनुसार, निम्नलिखित में से किस स्थिति में विकल्पों का व्यापक दायरा बाधा के बजाय सहायक होगा?",
   "The passage says that people 'with clear preferences, or with the knowledge to sort the options quickly, benefit from a wider range' -- a keen cook who knows exactly which spices a dish needs is such a person. "
   "A first-time buyer facing dozens of insurance plans meets options that are hard to compare; a pension that cannot be changed is a choice costly to undo; and a shopper with no idea what to buy does not know what she wants -- each is a condition in which choice overwhelms.",
   "परिच्छेद कहता है कि 'स्पष्ट पसंद वाले लोग, या विकल्पों को जल्दी छाँटने का ज्ञान रखने वाले, व्यापक दायरे से लाभ पाते हैं' -- एक उत्साही रसोइया जो ठीक जानता है कि किसी व्यंजन में कौन-से मसाले चाहिए, ऐसा ही व्यक्ति है। "
   "दर्जनों बीमा योजनाओं के सामने पहली बार ख़रीदने वाले के विकल्पों की तुलना कठिन है; जो पेंशन बदली न जा सके, उसका चुनाव पलटना महँगा है; और जिस ख़रीदार को कुछ पता न हो कि क्या ख़रीदे, वह नहीं जानती कि वह क्या चाहती है -- हर एक वह परिस्थिति है जिसमें विकल्प भारी पड़ते हैं।",
   "when-a-wide-range-helps",
   opts=["A first-time buyer choosing among dozens of insurance plans with quite different terms",
         "A person choosing a pension scheme that cannot be changed once it has been chosen",
         "A shopper with no idea at all what kind of gift to buy for someone she does not know",
         "A keen cook who knows exactly which spices a particular dish needs"],
   opts_hi=["पहली बार ख़रीदने वाला व्यक्ति जो काफ़ी अलग शर्तों वाली दर्जनों बीमा योजनाओं में से चुन रहा है",
            "एक व्यक्ति जो ऐसी पेंशन योजना चुन रहा है जिसे एक बार चुनने के बाद बदला नहीं जा सकता",
            "एक ख़रीदार जिसे बिल्कुल पता नहीं कि किसी अनजान व्यक्ति के लिए कैसा उपहार ख़रीदे",
            "एक उत्साही रसोइया जो ठीक-ठीक जानता है कि किसी व्यंजन में कौन-से मसाले चाहिए"],
   ans=3, pos=3)
RQ(p, "Assumption", "hard", "s2", ASSUME, ASSUME_HI,
   "Both are assumed. The closing advice -- to make what is offered 'easier to compare' -- makes sense only if the ease of comparison depends partly on how options are presented, which designers can change (1). "
   "And the jam experiment is used as evidence that more choice leaves people 'less able to decide', which treats whether someone who stopped went on to buy as a sign of how easily he or she could decide (2).",
   "दोनों पूर्वधारणाएँ हैं। अंतिम सलाह -- जो दिया जाए उसकी 'तुलना आसान' बनाना -- तभी अर्थपूर्ण है जब तुलना की सुगमता आंशिक रूप से इस पर निर्भर हो कि विकल्प कैसे प्रस्तुत किए जाते हैं, जिसे बनाने वाले बदल सकते हैं (1)। "
   "और जैम प्रयोग को इस बात के साक्ष्य के रूप में प्रयोग किया गया है कि अधिक विकल्प लोगों को 'निर्णय लेने में कम सक्षम' छोड़ते हैं, जो यह मानता है कि रुकने वाले ने आगे ख़रीदा या नहीं, यह इस बात का संकेत है कि वह कितनी आसानी से निर्णय ले सका (2)।",
   "assumptions",
   st=["How easily options can be compared depends partly on how they are presented.",
       "Whether a shopper who stops at a stall goes on to buy says something about how easily he or she could decide."],
   st_hi=["विकल्पों की तुलना कितनी आसानी से हो सकती है, यह आंशिक रूप से इस पर निर्भर है कि उन्हें कैसे प्रस्तुत किया जाता है।",
          "स्टॉल पर रुकने वाला ख़रीदार आगे ख़रीदता है या नहीं, इससे कुछ पता चलता है कि वह कितनी आसानी से निर्णय ले सका।"],
   key=2)

# ------------------------------------------------------------------ P08 dams and starving deltas (3)
p = passage("p08",
  "A delta is built by its river. Over thousands of years the silt carried down from the mountains settles where the river meets the sea, raising land faster than the waves can wear it away and the soft ground can sink. Dams interrupt this work. "
  "Their reservoirs are still water, and most of the silt that enters them settles behind the wall. Downstream, the river reaches the sea carrying less sediment and often less water, and the balance tips: the coast retreats, salt water pushes inland, and fields that once flooded with fertile silt need costly fertiliser. "
  "The deltas of the Nile and the Indus have both lost land in this way since large dams and barrages were built upstream. None of this means that dams should not be built; they store water for dry seasons and generate power. "
  "But a dam's costs are paid partly by people far downstream who had no say in it, and designs that let some sediment pass -- through tunnels, gates or periodic flushing -- can reduce the bill.",
  "डेल्टा को उसकी नदी बनाती है। हज़ारों वर्षों में पहाड़ों से बहकर आई गाद वहाँ जमती है जहाँ नदी समुद्र से मिलती है, जिससे भूमि उससे तेज़ी से ऊपर उठती है जितनी तेज़ी से लहरें उसे घिस सकें और नरम ज़मीन धँस सके। बाँध इस काम में बाधा डालते हैं। "
  "उनके जलाशय ठहरा हुआ पानी हैं, और उनमें आने वाली अधिकांश गाद दीवार के पीछे बैठ जाती है। नीचे की ओर नदी समुद्र तक कम गाद और प्रायः कम पानी लेकर पहुँचती है, और संतुलन बिगड़ जाता है: तट पीछे हटता है, खारा पानी भीतर घुसता है, और जो खेत कभी उपजाऊ गाद से भर जाते थे उन्हें महँगे उर्वरक चाहिए। "
  "नील और सिंधु दोनों के डेल्टा ऊपर की ओर बड़े बाँध और बैराज बनने के बाद से इसी तरह भूमि खो चुके हैं। इसका अर्थ यह नहीं कि बाँध न बनाए जाएँ; वे सूखे मौसमों के लिए पानी जमा करते हैं और बिजली बनाते हैं। "
  "पर बाँध की लागत का एक भाग बहुत नीचे रहने वाले वे लोग चुकाते हैं जिनकी उसमें कोई राय नहीं थी, और ऐसी रचनाएँ जो कुछ गाद को आगे जाने दें -- सुरंगों, फाटकों या समय-समय पर बहाव के द्वारा -- यह बोझ घटा सकती हैं।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage explains how dams starve deltas of silt, refuses to conclude that dams should not be built, and stresses that the cost falls on people downstream and can be reduced by designs that pass sediment. "
   "It says 'none of this means that dams should not be built', so removing them is not its point; it says the Nile and Indus deltas 'lost land', not that the deltas are gone; and it explains sinking and erosion by the loss of silt, not by a rising sea.",
   "परिच्छेद बताता है कि बाँध कैसे डेल्टाओं को गाद से वंचित करते हैं, यह निष्कर्ष निकालने से इनकार करता है कि बाँध न बनें, और ज़ोर देता है कि लागत नीचे रहने वाले लोगों पर पड़ती है और गाद को आगे जाने देने वाली रचनाओं से घटाई जा सकती है। "
   "वह कहता है 'इसका अर्थ यह नहीं कि बाँध न बनाए जाएँ', इसलिए उन्हें हटाना उसका बिंदु नहीं; वह कहता है कि नील और सिंधु के डेल्टा 'भूमि खो चुके हैं', यह नहीं कि डेल्टा मिट गए; और वह धँसाव और कटाव को गाद की कमी से समझाता है, बढ़ते समुद्र से नहीं।",
   "crux",
   opts=["Dams starve deltas of silt; designs can reduce this cost, which falls on people downstream.",
         "Dams do more harm than good, and the largest of them should be taken down as soon as possible.",
         "The Nile and the Indus have lost their deltas entirely because of the dams built upstream of them.",
         "Deltas sink mainly because the level of the sea has risen faster than rivers can build up land."],
   opts_hi=["बाँध डेल्टाओं को गाद से वंचित करते हैं; रचना से यह लागत घट सकती है, जो नीचे के लोगों पर पड़ती है।",
            "बाँध लाभ से अधिक हानि करते हैं, और उनमें से सबसे बड़े बाँधों को जितनी जल्दी हो सके हटा देना चाहिए।",
            "नील और सिंधु ऊपर बने बाँधों के कारण अपने डेल्टा पूरी तरह खो चुकी हैं।",
            "डेल्टा मुख्यतः इसलिए धँसते हैं कि समुद्र का स्तर उससे तेज़ी से बढ़ा है जितनी तेज़ी से नदियाँ भूमि बना सकें।"],
   ans=0, pos=0)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Neither is valid. 1: the passage describes a balance between land built by silt and land lost to waves and sinking; dams tip it, but nothing says a delta without a dam can never lose land. "
   "2 reverses the passage, which says that fields that once flooded with fertile silt 'need costly fertiliser' once a dam holds the silt back -- a loss to farmers, not a gain.",
   "कोई भी वैध नहीं। 1: परिच्छेद गाद से बनी भूमि और लहरों व धँसाव से खोई भूमि के बीच संतुलन का वर्णन करता है; बाँध उसे बिगाड़ते हैं, पर कहीं नहीं कहा गया कि बिना बाँध का डेल्टा कभी भूमि नहीं खो सकता। "
   "2 परिच्छेद का उलटा कहता है, जिसके अनुसार बाँध के गाद रोक लेने पर जो खेत कभी उपजाऊ गाद से भर जाते थे उन्हें 'महँगे उर्वरक चाहिए' -- किसानों की हानि, लाभ नहीं।",
   "conclusions",
   st=["A delta that has no dam upstream can never lose land to the sea.",
       "Farmers in a delta gain from a dam upstream, because their fields no longer need to be cleared of silt."],
   st_hi=["जिस डेल्टा के ऊपर की ओर कोई बाँध नहीं, वह समुद्र के हाथों कभी भूमि नहीं खो सकता।",
          "डेल्टा के किसानों को ऊपर के बाँध से लाभ होता है, क्योंकि उनके खेतों से अब गाद हटानी नहीं पड़ती।"],
   key=3)
RQ(p, "Inference", "hard", "mcq",
   "Which one of the following is the most logical implication of the passage for those planning a new dam?",
   "नया बाँध बनाने की योजना बनाने वालों के लिए परिच्छेद का निम्नलिखित में से कौन-सा सबसे तार्किक निहितार्थ है?",
   "The passage says a dam's costs are 'paid partly by people far downstream who had no say in it' and that designs letting sediment pass 'can reduce the bill': planners should count those losses and plan for passing sediment. "
   "Building only where no one lives downstream is not suggested and would rule out most rivers; a reservoir deep enough to hold all the silt for centuries would starve the delta even more; and the passage blames dams and barrages alike, so preferring barrages is no remedy.",
   "परिच्छेद कहता है कि बाँध की लागत 'बहुत नीचे रहने वाले वे लोग चुकाते हैं जिनकी उसमें कोई राय नहीं थी' और कि गाद को आगे जाने देने वाली रचनाएँ 'यह बोझ घटा सकती हैं': योजनाकारों को वे हानियाँ गिननी चाहिए और गाद को आगे भेजने की योजना बनानी चाहिए। "
   "केवल वहाँ बनाना जहाँ नीचे कोई न रहता हो, सुझाया नहीं गया और इससे अधिकांश नदियाँ बाहर हो जातीं; सदियों तक सारी गाद रोकने लायक़ गहरा जलाशय डेल्टा को और भी वंचित करेगा; और परिच्छेद बाँधों और बैराजों दोनों को दोष देता है, इसलिए बैराज को प्राथमिकता देना कोई उपाय नहीं।",
   "an-implication-for-planners",
   opts=["They should build only on rivers along which no one at all lives downstream of the site.",
         "They should count losses to people downstream among its costs and plan to let sediment pass.",
         "They should make the reservoir deep enough to hold back all the incoming silt for centuries.",
         "They should prefer a barrage to a dam, since barrages hold back no sediment at all."],
   opts_hi=["उन्हें केवल उन नदियों पर बनाना चाहिए जिनके किनारे स्थल से नीचे की ओर कोई भी न रहता हो।",
            "उन्हें नीचे के लोगों की हानि लागत में गिननी और गाद आगे जाने देने की योजना बनानी चाहिए।",
            "उन्हें जलाशय इतना गहरा बनाना चाहिए कि वह आने वाली सारी की सारी गाद को सदियों तक रोक सके।",
            "उन्हें बाँध के बजाय बैराज को प्राथमिकता देनी चाहिए, क्योंकि बैराज कोई गाद नहीं रोकते।"],
   ans=1, pos=1)

# ------------------------------------------------------------------ P09 green hydrogen (3)
p = passage("p09",
  "Hydrogen burns without releasing carbon dioxide, which has made it a favourite of plans to cut emissions. Most hydrogen today, however, is made from natural gas or coal, in processes that release a good deal of carbon dioxide. "
  "Hydrogen made by splitting water with electricity from wind or solar power -- green hydrogen -- avoids this, but it still costs more, and turning electricity into hydrogen and back into electricity wastes much of the energy along the way. That is why, for cars and home heating, using electricity directly, through batteries and heat pumps, is usually more efficient. "
  "Green hydrogen earns its place where electricity cannot easily do the job: in making fertiliser and refining fuels, which already use large amounts of hydrogen made from gas; in making steel without coal; and perhaps in fuels for ships and aircraft. "
  "India's National Green Hydrogen Mission, approved in 2023, aims at an output of five million tonnes a year by 2030. Whether such plans succeed will depend on cheap renewable power and on aiming the hydrogen at the uses where nothing else will serve.",
  "हाइड्रोजन कार्बन डाइऑक्साइड छोड़े बिना जलती है, जिसने उसे उत्सर्जन घटाने की योजनाओं का प्रिय बना दिया है। पर आज अधिकांश हाइड्रोजन प्राकृतिक गैस या कोयले से ऐसी प्रक्रियाओं में बनती है जो काफ़ी कार्बन डाइऑक्साइड छोड़ती हैं। "
  "पवन या सौर बिजली से पानी को तोड़कर बनी हाइड्रोजन -- हरित हाइड्रोजन -- इससे बचती है, पर वह अब भी महँगी है, और बिजली को हाइड्रोजन में और फिर वापस बिजली में बदलने में रास्ते में बहुत-सी ऊर्जा व्यर्थ जाती है। इसीलिए गाड़ियों और घरों को गर्म करने के लिए बैटरियों और हीट पंपों द्वारा बिजली का सीधा प्रयोग प्रायः अधिक दक्ष है। "
  "हरित हाइड्रोजन का स्थान वहाँ है जहाँ बिजली आसानी से काम नहीं कर सकती: उर्वरक बनाने और ईंधन शोधन में, जो पहले से गैस से बनी बड़ी मात्रा में हाइड्रोजन प्रयोग करते हैं; कोयले के बिना इस्पात बनाने में; और संभवतः जहाज़ों और विमानों के ईंधन में। "
  "2023 में स्वीकृत भारत का राष्ट्रीय हरित हाइड्रोजन मिशन 2030 तक प्रति वर्ष पचास लाख टन उत्पादन का लक्ष्य रखता है। ऐसी योजनाएँ सफल होंगी या नहीं, यह सस्ती नवीकरणीय बिजली पर और हाइड्रोजन को उन उपयोगों की ओर मोड़ने पर निर्भर करेगा जहाँ और कुछ काम नहीं आएगा।")
RQ(p, "Best Summary", "medium", "mcq", MSG, MSG_HI,
   "The passage's message is that green hydrogen 'earns its place where electricity cannot easily do the job', and that plans should aim it at such uses. "
   "It says batteries are usually more efficient for cars, so hydrogen should not replace them there; it says most hydrogen today is made from gas or coal with large emissions; and it says green hydrogen 'still costs more', which a target does not change.",
   "परिच्छेद का संदेश यह है कि हरित हाइड्रोजन का 'स्थान वहाँ है जहाँ बिजली आसानी से काम नहीं कर सकती', और योजनाएँ उसे ऐसे उपयोगों की ओर मोड़ें। "
   "वह कहता है कि गाड़ियों के लिए बैटरियाँ प्रायः अधिक दक्ष हैं, इसलिए वहाँ हाइड्रोजन उनकी जगह न ले; वह कहता है कि आज अधिकांश हाइड्रोजन बड़े उत्सर्जन के साथ गैस या कोयले से बनती है; और वह कहता है कि हरित हाइड्रोजन 'अब भी महँगी है', जिसे कोई लक्ष्य नहीं बदलता।",
   "message",
   opts=["Green hydrogen is most useful where electricity cannot be used directly.",
         "Hydrogen should replace batteries in cars, since burning it releases no carbon dioxide.",
         "All the hydrogen produced in the world today is already free of carbon emissions.",
         "India's target shows that green hydrogen is already cheaper than hydrogen made from gas."],
   opts_hi=["हरित हाइड्रोजन वहाँ सबसे उपयोगी है जहाँ बिजली का सीधा प्रयोग नहीं हो सकता।",
            "गाड़ियों में बैटरियों की जगह हाइड्रोजन लेनी चाहिए, क्योंकि उसे जलाने से कार्बन डाइऑक्साइड नहीं निकलती।",
            "आज दुनिया में बनने वाली सारी हाइड्रोजन पहले से ही कार्बन उत्सर्जन से मुक्त है।",
            "भारत का लक्ष्य दिखाता है कि हरित हाइड्रोजन पहले से ही गैस से बनी हाइड्रोजन से सस्ती है।"],
   ans=0, pos=0)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Only 2 is valid. Fertiliser plants already use large amounts of hydrogen made from gas, so making that hydrogen green would cut emissions without any new use for hydrogen having to be found. "
   "1 ignores where hydrogen comes from: burning it releases no carbon dioxide either way, but making it from natural gas releases 'a good deal', so the two do not cut emissions equally.",
   "केवल 2 वैध है। उर्वरक संयंत्र पहले से गैस से बनी बड़ी मात्रा में हाइड्रोजन प्रयोग करते हैं, इसलिए उस हाइड्रोजन को हरित बनाने से हाइड्रोजन का कोई नया उपयोग खोजे बिना उत्सर्जन घटेगा। "
   "1 इसकी अनदेखी करता है कि हाइड्रोजन कहाँ से आती है: जलाने पर दोनों ही स्थितियों में कार्बन डाइऑक्साइड नहीं निकलती, पर उसे प्राकृतिक गैस से बनाने में 'काफ़ी' निकलती है, इसलिए दोनों उत्सर्जन बराबर नहीं घटातीं।",
   "conclusions",
   st=["Using hydrogen made from natural gas cuts emissions as much as using green hydrogen does.",
       "Replacing the gas-made hydrogen already used in fertiliser plants with green hydrogen would cut emissions without needing any new use for hydrogen."],
   st_hi=["प्राकृतिक गैस से बनी हाइड्रोजन का प्रयोग उत्सर्जन को उतना ही घटाता है जितना हरित हाइड्रोजन का प्रयोग।",
          "उर्वरक संयंत्रों में पहले से प्रयुक्त गैस से बनी हाइड्रोजन की जगह हरित हाइड्रोजन लाने से हाइड्रोजन के किसी नए उपयोग के बिना उत्सर्जन घटेगा।"],
   key=1)
RQ(p, "Specific Detail", "medium", "mcq",
   "According to the passage, why is using electricity directly usually better than using hydrogen for cars?",
   "परिच्छेद के अनुसार, गाड़ियों के लिए हाइड्रोजन के बजाय बिजली का सीधा प्रयोग प्रायः बेहतर क्यों है?",
   "The passage gives one reason: 'turning electricity into hydrogen and back into electricity wastes much of the energy along the way', which is why using electricity directly 'is usually more efficient'. "
   "It says hydrogen burns without releasing carbon dioxide, so a hydrogen car emits none from its exhaust; it never says hydrogen cannot be stored in a vehicle; and it compares no costs of batteries and tanks.",
   "परिच्छेद एक कारण देता है: 'बिजली को हाइड्रोजन में और फिर वापस बिजली में बदलने में रास्ते में बहुत-सी ऊर्जा व्यर्थ जाती है', इसीलिए बिजली का सीधा प्रयोग 'प्रायः अधिक दक्ष है'। "
   "वह कहता है कि हाइड्रोजन कार्बन डाइऑक्साइड छोड़े बिना जलती है, इसलिए हाइड्रोजन गाड़ी के धुएँ से कुछ नहीं निकलता; वह कभी नहीं कहता कि गाड़ी में हाइड्रोजन रखी नहीं जा सकती; और वह बैटरियों और टंकियों की लागत की कोई तुलना नहीं करता।",
   "why-batteries-for-cars",
   opts=["Cars that run on hydrogen release carbon dioxide from their exhausts as they are driven.",
         "Hydrogen cannot be stored safely in a vehicle in the quantities a journey would need.",
         "Batteries cost far less to manufacture than the tanks that are needed to hold hydrogen.",
         "Converting electricity to hydrogen and back wastes much of the energy."],
   opts_hi=["हाइड्रोजन से चलने वाली गाड़ियाँ चलते समय अपने धुएँ से कार्बन डाइऑक्साइड छोड़ती हैं।",
            "किसी यात्रा के लिए आवश्यक मात्रा में हाइड्रोजन गाड़ी में सुरक्षित रूप से रखी नहीं जा सकती।",
            "बैटरियाँ बनाने में हाइड्रोजन रखने के लिए आवश्यक टंकियों से कहीं कम लागत आती है।",
            "बिजली को हाइड्रोजन में और वापस बदलने में बहुत-सी ऊर्जा व्यर्थ जाती है।"],
   ans=3, pos=3)
