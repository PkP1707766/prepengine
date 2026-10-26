# -*- coding: utf-8 -*-
"""CSAT Level 4 · Simulator 7 -- Reading Comprehension: 9 passages, 27 items (3 each), Layout A.

The 2023/2024 shape again: nine passages of three items. Each passage turns -- a claim, then its limit. Themes, none
used in Levels 1-3 or Simulators 1-6: judging risk by what comes to mind, the lighthouse and the free rider, the
separation of powers, the Fundamental Duties, carbon dating, the bamboo that flowers once in fifty years, the last
case of polio in India, the ship of Theseus, and Occam's razor. Difficulty 1 easy / 15 medium / 11 hard. Options are
named by content in every explanation."""
from csat_common import passage, RQ

CRUX = "Which one of the following statements best reflects the crux of the passage?"
CRUX_HI = "निम्नलिखित में से कौन-सा कथन परिच्छेद के सार को सबसे अच्छी तरह व्यक्त करता है?"
VALID = "On the basis of the passage, which of the following conclusions is/are valid?"
VALID_HI = "परिच्छेद के आधार पर निम्नलिखित में से कौन-सा/से निष्कर्ष वैध है/हैं?"

# ------------------------------------------------------------------ P01 judging risk by what comes to mind
p = passage("p01",
  "In 1973 two psychologists, Amos Tversky and Daniel Kahneman, gave a name to a short cut that people use to judge how common something is: they ask themselves how easily examples come to mind. Usually this works, because things that happen often are easy to recall. But memory is swayed by more than frequency. Events that are vivid, recent or much reported come to mind more easily than dull, everyday ones of the same frequency. "
  "So after news of an air crash many people feel that flying is dangerous, though in most countries far more people die on the roads in a single week than in air crashes in a year. The short cut is not foolish; it fails in a predictable way, by giving too much weight to whatever is dramatic. Knowing this, a careful person checks a vivid impression against the numbers before acting on it.",
  "1973 में मनोवैज्ञानिक एमॉस त्वेर्स्की और डेनियल काह्नमन ने एक ऐसे शॉर्टकट का वर्णन किया जिससे लोग आँकते हैं कि कोई बात कितनी आम है: वे स्वयं से पूछते हैं कि उदाहरण कितनी आसानी से याद आते हैं। प्रायः यह काम करता है, क्योंकि जो बातें अक्सर होती हैं वे आसानी से याद आती हैं। पर स्मृति केवल बारंबारता से प्रभावित नहीं होती। जो घटनाएँ सजीव, हाल की या बहुत चर्चित हों, वे उतनी ही बार होने वाली नीरस, रोज़मर्रा की घटनाओं से अधिक आसानी से याद आती हैं। "
  "इसलिए किसी विमान दुर्घटना की ख़बर के बाद बहुत-से लोगों को लगता है कि उड़ना ख़तरनाक है, यद्यपि अधिकांश देशों में एक ही सप्ताह में सड़कों पर उससे कहीं अधिक लोग मरते हैं जितने एक वर्ष में विमान दुर्घटनाओं में। यह शॉर्टकट मूर्खतापूर्ण नहीं; यह एक अनुमानित ढंग से विफल होता है, जो कुछ भी नाटकीय हो उसे बहुत अधिक भार देकर। यह जानते हुए एक सावधान व्यक्ति किसी सजीव धारणा पर कुछ करने से पहले उसे आँकड़ों से जाँचता है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage describes judging frequency by ease of recall, says it usually works, and shows how it fails predictably by overweighting vivid events -- so impressions should be checked against numbers. "
   "It calls the short cut not foolish, so it does not reject it; it says it usually works, not that it is always wrong; and it does not say flying is more dangerous than driving.",
   "परिच्छेद याद आने की सरलता से बारंबारता आँकने का वर्णन करता है, कहता है कि यह प्रायः काम करता है, और दिखाता है कि यह सजीव घटनाओं को अधिक भार देकर अनुमानित ढंग से कैसे विफल होता है -- इसलिए धारणाओं को आँकड़ों से जाँचना चाहिए। "
   "वह शॉर्टकट को मूर्खतापूर्ण नहीं कहता, इसलिए उसे ख़ारिज नहीं करता; वह कहता है कि यह प्रायः काम करता है, यह नहीं कि यह हमेशा ग़लत है; और वह यह नहीं कहता कि उड़ना गाड़ी चलाने से अधिक ख़तरनाक है।",
   "crux",
   opts=["People should never rely on what they remember when they judge how likely something is.",
         "Flying is in truth more dangerous than travelling by road, as the news of crashes shows.",
         "Judging by what comes to mind mostly works but overrates the vivid; check the numbers.",
         "Memory records events in exact proportion to how often they really happen in the world."],
   opts_hi=["किसी बात की संभावना आँकते समय लोगों को कभी अपनी स्मृति पर निर्भर नहीं रहना चाहिए।",
            "उड़ना वास्तव में सड़क यात्रा से अधिक ख़तरनाक है, जैसा दुर्घटनाओं की ख़बरें दिखाती हैं।",
            "याद आने से आँकना प्रायः काम करता है पर सजीव घटनाओं को बढ़ा देता है, इसलिए आँकड़े जाँचिए।",
            "स्मृति घटनाओं को ठीक उसी अनुपात में दर्ज करती है जितनी बार वे दुनिया में सचमुच होती हैं।"],
   ans=2, pos=2)
RQ(p, "Inference", "hard", "mcq",
   "Which one of the following would the passage's reasoning most lead us to expect?",
   "परिच्छेद के तर्क के आधार पर निम्नलिखित में से किसकी सबसे अधिक अपेक्षा की जानी चाहिए?",
   "The short cut gives too much weight to what is vivid and much reported. After weeks of news about a few shark attacks, people would rate the risk of shark attacks higher than the facts justify, while dull and common risks, such as drowning in an ordinary pool, are underrated. "
   "The passage gives no reason to think people underrate dramatic risks, that news coverage makes judgements more accurate, or that common risks are the ones most often overrated.",
   "शॉर्टकट सजीव और बहुत चर्चित बातों को बहुत अधिक भार देता है। कुछ शार्क हमलों की हफ़्तों की ख़बरों के बाद लोग शार्क हमले के जोखिम को तथ्यों से अधिक आँकेंगे, जबकि नीरस और आम जोखिम, जैसे किसी साधारण तालाब में डूबना, कम आँके जाते हैं। "
   "परिच्छेद यह मानने का कोई कारण नहीं देता कि लोग नाटकीय जोखिमों को कम आँकते हैं, कि ख़बरों से निर्णय अधिक सटीक होते हैं, या कि आम जोखिम ही सबसे अधिक बढ़ाकर आँके जाते हैं।",
   "what-the-reasoning-predicts",
   opts=["After weeks of news about a few shark attacks, people overrate the risk of a shark attack.",
         "People who read a great deal of news judge the frequency of rare events more accurately than others.",
         "Dramatic risks are usually underrated, because people prefer not to think about frightening events.",
         "Ordinary, everyday risks are the ones that people most often overrate when they think about danger."],
   opts_hi=["कुछ शार्क हमलों की हफ़्तों की ख़बरों के बाद लोग शार्क के हमले के जोखिम को बढ़ाकर आँकते हैं।",
            "बहुत अधिक ख़बरें पढ़ने वाले लोग दुर्लभ घटनाओं की बारंबारता को दूसरों से अधिक सटीक आँकते हैं।",
            "नाटकीय जोखिम प्रायः कम आँके जाते हैं, क्योंकि लोग डरावनी घटनाओं के बारे में न सोचना पसंद करते हैं।",
            "साधारण, रोज़मर्रा के जोखिम ही वे हैं जिन्हें लोग ख़तरे के बारे में सोचते समय सबसे अधिक बढ़ाकर आँकते हैं।"],
   ans=0, pos=0)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Only 2 is valid. The passage says the short cut usually works because frequent things are easy to recall; it goes wrong when vividness, recency or reporting, rather than frequency, makes something easy to recall. "
   "1 contradicts the passage, which says the short cut 'usually' works and 'is not foolish'.",
   "केवल 2 वैध है। परिच्छेद कहता है कि शॉर्टकट प्रायः इसलिए काम करता है कि बार-बार होने वाली बातें आसानी से याद आती हैं; वह तब ग़लत होता है जब बारंबारता के बजाय सजीवता, हाल का होना या चर्चा किसी बात को आसानी से याद आने लायक़ बनाती है। "
   "1 परिच्छेद का खंडन करता है, जो कहता है कि शॉर्टकट 'प्रायः' काम करता है और 'मूर्खतापूर्ण नहीं' है।",
   "conclusions",
   st=["Judging how common something is by how easily examples come to mind is usually wrong.",
       "The short cut misleads mainly when something is easy to recall for reasons other than how often it happens."],
   st_hi=["उदाहरणों के आसानी से याद आने से किसी बात के आम होने का आकलन प्रायः ग़लत होता है।",
          "शॉर्टकट मुख्यतः तब भटकाता है जब कोई बात इसकी बारंबारता के अलावा अन्य कारणों से आसानी से याद आए।"],
   key=1)

# ------------------------------------------------------------------ P02 the lighthouse and the free rider
p = passage("p02",
  "Economists long used the lighthouse as the textbook case of a good that markets cannot supply. Once a light is shining, every passing ship can see it, and there is no way to charge a ship for looking; so each shipowner, the argument ran, would wait for someone else to pay, and no private lighthouse would ever be built. Only the state, through taxes, could provide one. "
  "In 1974 the economist Ronald Coase showed that the history did not fit the textbook. In Britain many lighthouses had been built and run privately, paid for by dues collected from ships when they called at nearby ports -- a place where payment could be enforced. The lesson is not that the state is never needed, but that a free-rider problem can sometimes be solved by tying the payment to something from which non-payers can be excluded.",
  "अर्थशास्त्री लंबे समय तक प्रकाशस्तंभ को ऐसी वस्तु के पाठ्यपुस्तकीय उदाहरण के रूप में लेते रहे जिसे बाज़ार नहीं दे सकता। एक बार प्रकाश जल जाए, तो पास से गुज़रने वाला हर जहाज़ उसे देख सकता है, और देखने के लिए जहाज़ से शुल्क लेने का कोई उपाय नहीं; इसलिए, तर्क था, हर जहाज़-मालिक किसी और के भुगतान की प्रतीक्षा करेगा, और कोई निजी प्रकाशस्तंभ कभी नहीं बनेगा। केवल राज्य, करों के माध्यम से, उसे दे सकता था। "
  "1974 में अर्थशास्त्री रोनाल्ड कोस ने दिखाया कि इतिहास पाठ्यपुस्तक से मेल नहीं खाता। ब्रिटेन में कई प्रकाशस्तंभ निजी रूप से बनाए और चलाए गए थे, जिनका ख़र्च जहाज़ों से तब वसूले गए शुल्कों से चलता था जब वे पास के बंदरगाहों पर रुकते -- एक ऐसी जगह जहाँ भुगतान लागू कराया जा सकता था। सीख यह नहीं कि राज्य की कभी आवश्यकता नहीं, बल्कि यह कि मुफ़्तख़ोरी की समस्या कभी-कभी भुगतान को किसी ऐसी चीज़ से जोड़कर हल की जा सकती है जिससे भुगतान न करने वालों को रोका जा सके।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage shows that the lighthouse, long cited as something only the state could provide, was in fact often provided privately by collecting dues at ports -- a way of tying payment to something from which non-payers could be excluded. "
   "It says the state is sometimes needed, so it does not say it never is; it does not say every public good can be sold privately; and it reports that private lighthouses existed, the opposite of none being built.",
   "परिच्छेद दिखाता है कि प्रकाशस्तंभ, जिसे लंबे समय तक ऐसी चीज़ बताया गया जो केवल राज्य दे सकता है, वास्तव में प्रायः बंदरगाहों पर शुल्क वसूलकर निजी रूप से दिया गया -- भुगतान को ऐसी चीज़ से जोड़ने का उपाय जिससे भुगतान न करने वालों को रोका जा सके। "
   "वह कहता है कि राज्य की कभी-कभी आवश्यकता है, इसलिए यह नहीं कहता कि कभी नहीं; वह यह नहीं कहता कि हर सार्वजनिक वस्तु निजी रूप से बेची जा सकती है; और वह बताता है कि निजी प्रकाशस्तंभ थे, जो किसी के न बनने का उलटा है।",
   "crux",
   opts=["The state is never needed to provide goods such as lighthouses, which markets supply well.",
         "Every good that is shared by all can be sold privately if the price is set high enough.",
         "No private lighthouse was ever built, exactly as the textbooks had always said.",
         "Free riding may be curbed by tying payment to something non-payers can be kept from."],
   opts_hi=["प्रकाशस्तंभ जैसी वस्तुएँ देने के लिए राज्य की कभी आवश्यकता नहीं, बाज़ार उन्हें अच्छी तरह देता है।",
            "सबके साझा उपयोग की हर वस्तु निजी रूप से बेची जा सकती है यदि मूल्य पर्याप्त ऊँचा रखा जाए।",
            "कोई निजी प्रकाशस्तंभ कभी नहीं बना, ठीक जैसा पाठ्यपुस्तकें हमेशा कहती थीं।",
            "मुफ़्तख़ोरी की समस्या भुगतान को उस चीज़ से जोड़कर हल हो सकती है जिससे न चुकाने वाले रोके जा सकें।"],
   ans=3, pos=3)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Neither is valid. 1 goes too far: Coase showed that the history did not fit the textbook, but the passage does not say that private lighthouses were better run or cheaper than state ones. "
   "2 reverses the passage's point: the dues worked precisely because they were collected at ports, where a ship could be made to pay; the light itself still could not be charged for.",
   "कोई भी वैध नहीं। 1 बहुत आगे जाता है: कोस ने दिखाया कि इतिहास पाठ्यपुस्तक से मेल नहीं खाता, पर परिच्छेद यह नहीं कहता कि निजी प्रकाशस्तंभ राज्य वालों से बेहतर चलाए गए या सस्ते थे। "
   "2 परिच्छेद की बात को उलट देता है: शुल्क ठीक इसलिए काम करते थे कि वे बंदरगाहों पर वसूले जाते थे, जहाँ जहाज़ से भुगतान कराया जा सकता था; स्वयं प्रकाश के लिए अब भी शुल्क नहीं लिया जा सकता था।",
   "conclusions",
   st=["Privately run lighthouses in Britain were cheaper and better than those run by the state.",
       "The private owners found a way to charge each ship for seeing the light while it was at sea."],
   st_hi=["ब्रिटेन में निजी रूप से चलाए गए प्रकाशस्तंभ राज्य द्वारा चलाए गए प्रकाशस्तंभों से सस्ते और बेहतर थे।",
          "निजी मालिकों ने हर जहाज़ से समुद्र में रहते हुए प्रकाश देखने का शुल्क लेने का उपाय खोज लिया।"],
   key=3)
RQ(p, "Inference", "medium", "mcq",
   "Which one of the following uses the same kind of solution as the port dues described in the passage?",
   "निम्नलिखित में से कौन-सा उसी प्रकार के हल का उपयोग करता है जैसा परिच्छेद में वर्णित बंदरगाह शुल्क?",
   "The port dues worked by collecting payment at a point where non-payers could be excluded. A town that pays for its street lights through a charge added to the fee for entering its market does the same: the lights cannot be charged for directly, but entry to the market can. "
   "Asking residents for voluntary donations invites free riding; a tax on all residents is the state solution the passage contrasts with; and switching the lights off removes the good rather than paying for it.",
   "बंदरगाह शुल्क ऐसे बिंदु पर भुगतान वसूलकर काम करते थे जहाँ भुगतान न करने वालों को रोका जा सके। जो नगर अपनी सड़क-बत्तियों का ख़र्च अपने बाज़ार में प्रवेश के शुल्क में जोड़े गए एक प्रभार से चलाए, वह यही करता है: बत्तियों के लिए सीधे शुल्क नहीं लिया जा सकता, पर बाज़ार में प्रवेश के लिए लिया जा सकता है। "
   "निवासियों से स्वैच्छिक दान माँगना मुफ़्तख़ोरी को न्योता देता है; सभी निवासियों पर कर वह राज्य वाला हल है जिससे परिच्छेद तुलना करता है; और बत्तियाँ बुझा देना वस्तु का ख़र्च चलाने के बजाय उसे ही हटा देता है।",
   "the-same-kind-of-solution",
   opts=["A town asks its residents to give whatever they wish, voluntarily, towards its street lights.",
         "A town pays for its street lights from a tax collected from every one of its residents.",
         "A market pays for the lights around it through a charge added to the fee for entering it.",
         "A town switches off its street lights at midnight to save the cost of running them."],
   opts_hi=["एक नगर अपने निवासियों से सड़क-बत्तियों के लिए स्वेच्छा से जो चाहें देने को कहता है।",
            "एक नगर अपनी सड़क-बत्तियों का ख़र्च अपने हर निवासी से वसूले गए कर से चलाता है।",
            "बाज़ार अपने आसपास की बत्तियों का ख़र्च प्रवेश-शुल्क में जोड़े प्रभार से चलाता है।",
            "एक नगर चलाने का ख़र्च बचाने के लिए आधी रात को अपनी सड़क-बत्तियाँ बुझा देता है।"],
   ans=2, pos=2)

# ------------------------------------------------------------------ P03 the separation of powers
p = passage("p03",
  "In The Spirit of the Laws, published in 1748, the French thinker Montesquieu argued that liberty is lost when the power to make laws, the power to carry them out and the power to judge are held by the same person or body; each must be able to check the others. "
  "Constitutions have applied the idea in different ways. The American Constitution keeps the President and the President's secretaries out of the legislature altogether. India's Constitution does not separate powers so sharply: under its parliamentary system, ministers are members of Parliament and remain in office only while they keep the support of the Lok Sabha. What India keeps is the idea of checks -- courts can strike down laws and executive acts that violate the Constitution, and Parliament can question and remove a government. The aim is not to keep the three powers apart for its own sake, but to ensure that none of them goes unchecked.",
  "1748 में प्रकाशित 'द स्पिरिट ऑफ़ द लॉज़' में फ़्रांसीसी विचारक मॉन्टेस्क्यू ने तर्क दिया कि स्वतंत्रता तब खो जाती है जब क़ानून बनाने, उन्हें लागू करने और न्याय करने की शक्तियाँ एक ही व्यक्ति या निकाय के पास हों; हर एक को दूसरों पर अंकुश रख पाना चाहिए। "
  "संविधानों ने इस विचार को अलग-अलग ढंग से लागू किया है। अमेरिकी संविधान राष्ट्रपति और राष्ट्रपति के सचिवों (मंत्रियों) को विधायिका से पूरी तरह बाहर रखता है। भारत का संविधान शक्तियों को इतनी कठोरता से अलग नहीं करता: उसकी संसदीय व्यवस्था में मंत्री संसद के सदस्य होते हैं और तभी तक पद पर रहते हैं जब तक उन्हें लोकसभा का समर्थन प्राप्त हो। भारत जो रखता है वह अंकुशों का विचार है -- न्यायालय संविधान का उल्लंघन करने वाले क़ानूनों और कार्यपालिका के कार्यों को रद्द कर सकते हैं, और संसद सरकार से प्रश्न पूछ सकती है और उसे हटा सकती है। उद्देश्य तीनों शक्तियों को केवल अलग रखना नहीं, बल्कि यह सुनिश्चित करना है कि कोई भी बिना अंकुश के न रहे।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage explains Montesquieu's idea that combining the three powers endangers liberty, and shows that India keeps not a strict separation but the checks that stop any power going unchecked. "
   "It says India does not separate powers sharply, so it is not identical to the American model; it does not say the courts control Parliament; and it presents checks, not separation for its own sake, as the aim.",
   "परिच्छेद मॉन्टेस्क्यू का यह विचार समझाता है कि तीनों शक्तियों को मिलाना स्वतंत्रता को ख़तरे में डालता है, और दिखाता है कि भारत कठोर पृथक्करण नहीं, बल्कि ऐसे अंकुश रखता है जो किसी शक्ति को बिना अंकुश के नहीं रहने देते। "
   "वह कहता है कि भारत शक्तियों को कठोरता से अलग नहीं करता, इसलिए वह अमेरिकी मॉडल जैसा नहीं; वह यह नहीं कहता कि न्यायालय संसद को नियंत्रित करते हैं; और वह पृथक्करण को अपने आप में नहीं, अंकुशों को उद्देश्य बताता है।",
   "crux",
   opts=["India's Constitution separates the three powers exactly as the American one does.",
         "No power should go unchecked, and India secures this without a strict separation.",
         "In India the courts control Parliament, and Parliament has no check on the courts.",
         "Montesquieu held that liberty is safest when one body holds all the powers of the state."],
   opts_hi=["भारत का संविधान तीनों शक्तियों को ठीक वैसे ही अलग करता है जैसे अमेरिकी संविधान।",
            "मायने यह रखता है कि कोई शक्ति बिना अंकुश के न रहे, जो भारत कठोर पृथक्करण के बिना सुनिश्चित करता है।",
            "भारत में न्यायालय संसद को नियंत्रित करते हैं, और संसद का न्यायालयों पर कोई अंकुश नहीं।",
            "मॉन्टेस्क्यू का मत था कि स्वतंत्रता तब सबसे सुरक्षित है जब एक ही निकाय के पास राज्य की सभी शक्तियाँ हों।"],
   ans=1, pos=1)
RQ(p, "Specific Detail", "easy", "mcq",
   "According to the passage, how long do ministers in India remain in office?",
   "परिच्छेद के अनुसार, भारत में मंत्री कितने समय तक पद पर रहते हैं?",
   "The passage says ministers 'remain in office only while they keep the support of the Lok Sabha'. "
   "It does not mention a fixed term, the President's pleasure alone, or the approval of the Supreme Court.",
   "परिच्छेद कहता है कि मंत्री 'तभी तक पद पर रहते हैं जब तक उन्हें लोकसभा का समर्थन प्राप्त हो'। "
   "वह किसी निश्चित अवधि, केवल राष्ट्रपति की इच्छा, या सर्वोच्च न्यायालय की स्वीकृति का उल्लेख नहीं करता।",
   "how-long-ministers-stay",
   opts=["For a fixed term of five years, whatever happens in Parliament",
         "For as long as the Supreme Court approves of their decisions",
         "Only while they keep the support of the Lok Sabha",
         "For as long as the President alone wishes, with no other check"],
   opts_hi=["संसद में चाहे जो हो, पाँच वर्ष की निश्चित अवधि तक",
            "जब तक सर्वोच्च न्यायालय उनके निर्णयों को स्वीकार करता है",
            "केवल तब तक जब तक उन्हें लोकसभा का समर्थन प्राप्त है",
            "जब तक अकेले राष्ट्रपति चाहें, बिना किसी अन्य अंकुश के"],
   ans=2, pos=2)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Both are valid. Montesquieu's concern was that the same person or body might hold all three powers; India's ministers belong to the legislature, yet the passage says India keeps checks on every power, so a system can join two powers and still guard liberty in his sense (1). "
   "And the passage says the aim is not to keep the powers apart 'for its own sake' but to ensure none goes unchecked, so a perfectly separate power with no check on it would defeat that aim (2).",
   "दोनों वैध हैं। मॉन्टेस्क्यू की चिंता यह थी कि एक ही व्यक्ति या निकाय के पास तीनों शक्तियाँ हों; भारत के मंत्री विधायिका के सदस्य हैं, फिर भी परिच्छेद कहता है कि भारत हर शक्ति पर अंकुश रखता है, इसलिए कोई व्यवस्था दो शक्तियों को जोड़कर भी उनके अर्थ में स्वतंत्रता की रक्षा कर सकती है (1)। "
   "और परिच्छेद कहता है कि उद्देश्य शक्तियों को 'केवल' अलग रखना नहीं, बल्कि यह सुनिश्चित करना है कि कोई बिना अंकुश के न रहे, इसलिए पूरी तरह अलग पर बिना किसी अंकुश वाली शक्ति उस उद्देश्य को विफल करेगी (2)।",
   "conclusions",
   st=["A system in which ministers sit in the legislature can still protect liberty if every power is checked.",
       "A branch of government kept wholly separate but answerable to no one would not meet the aim the passage describes."],
   st_hi=["जिस व्यवस्था में मंत्री विधायिका में बैठते हैं, वह भी स्वतंत्रता की रक्षा कर सकती है यदि हर शक्ति पर अंकुश हो।",
          "सरकार की कोई शाखा जो पूरी तरह अलग रखी गई हो पर किसी के प्रति उत्तरदायी न हो, परिच्छेद में वर्णित उद्देश्य पूरा नहीं करेगी।"],
   key=2)

# ------------------------------------------------------------------ P04 the Fundamental Duties
p = passage("p04",
  "The Constitution as adopted in 1950 listed citizens' rights but said little about their duties. In 1976, on the recommendation of the Swaran Singh Committee, the Forty-second Amendment added Part IV-A, with a list of Fundamental Duties: among them, to abide by the Constitution and respect the national flag and anthem, to promote harmony among all the people of India, to protect the natural environment and to develop a scientific temper. An eleventh, the duty of parents to provide opportunities for education to their children aged six to fourteen, was added in 2002. "
  "Like the Directive Principles, the duties cannot be enforced in a court. They have not been empty for that reason. Courts have drawn on them in reading laws -- on protecting forests, for instance -- and they set out what the Constitution expects of citizens, not only what it promises them.",
  "1950 में अपनाया गया संविधान नागरिकों के अधिकार बताता था पर उनके कर्तव्यों के बारे में कम कहता था। 1976 में स्वर्ण सिंह समिति की सिफ़ारिश पर बयालीसवें संशोधन ने भाग IV-क जोड़ा, जिसमें मौलिक कर्तव्यों की एक सूची थी: उनमें संविधान का पालन करना और राष्ट्रध्वज व राष्ट्रगान का सम्मान करना, भारत के सभी लोगों में सद्भाव बढ़ाना, प्राकृतिक पर्यावरण की रक्षा करना और वैज्ञानिक दृष्टिकोण विकसित करना शामिल हैं। ग्यारहवाँ, छह से चौदह वर्ष के बच्चों को शिक्षा के अवसर देने का माता-पिता का कर्तव्य, 2002 में जोड़ा गया। "
  "नीति निदेशक तत्त्वों की तरह, ये कर्तव्य न्यायालय में लागू नहीं कराए जा सकते। इस कारण वे खोखले नहीं रहे। न्यायालयों ने क़ानूनों की व्याख्या में उनका सहारा लिया है -- उदाहरण के लिए, वनों की रक्षा पर -- और वे बताते हैं कि संविधान नागरिकों से क्या अपेक्षा करता है, केवल यह नहीं कि वह उन्हें क्या वचन देता है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage explains when and why the Fundamental Duties were added and argues that, though not enforceable in court, they matter: courts draw on them, and they state what the Constitution expects of citizens. "
   "It says the duties cannot be enforced in court, so they are not penalties; it says they have not been empty, the opposite of meaningless; and it says they were added in 1976, not in 1950.",
   "परिच्छेद बताता है कि मौलिक कर्तव्य कब और क्यों जोड़े गए और तर्क देता है कि, न्यायालय में लागू न कराए जा सकने पर भी, वे मायने रखते हैं: न्यायालय उनका सहारा लेते हैं, और वे बताते हैं कि संविधान नागरिकों से क्या अपेक्षा करता है। "
   "वह कहता है कि कर्तव्य न्यायालय में लागू नहीं कराए जा सकते, इसलिए वे दंड नहीं; वह कहता है कि वे खोखले नहीं रहे, जो अर्थहीन होने का उलटा है; और वह कहता है कि वे 1976 में जोड़े गए, 1950 में नहीं।",
   "crux",
   opts=["Though unenforceable, the duties guide courts and say what is expected of citizens.",
         "Citizens who neglect a Fundamental Duty can be punished by any court in the country.",
         "The Fundamental Duties have no meaning at all, since no court can enforce them.",
         "The Fundamental Duties were part of the Constitution as it was adopted in 1950."],
   opts_hi=["अप्रवर्तनीय होकर भी कर्तव्य न्यायालयों को दिशा देते और नागरिकों से अपेक्षा बताते हैं।",
            "मौलिक कर्तव्य की उपेक्षा करने वाले नागरिकों को देश का कोई भी न्यायालय दंड दे सकता है।",
            "मौलिक कर्तव्यों का कोई अर्थ नहीं, क्योंकि कोई न्यायालय उन्हें लागू नहीं करा सकता।",
            "मौलिक कर्तव्य 1950 में अपनाए गए संविधान का भाग थे।"],
   ans=0, pos=0)
RQ(p, "Specific Detail", "medium", "mcq",
   "According to the passage, which duty was added to the list in 2002?",
   "परिच्छेद के अनुसार, 2002 में सूची में कौन-सा कर्तव्य जोड़ा गया?",
   "The passage says the eleventh duty, added in 2002, is that of parents to provide opportunities for education to their children aged six to fourteen. "
   "Respecting the flag and anthem, protecting the environment and developing a scientific temper are among the duties added in 1976.",
   "परिच्छेद कहता है कि 2002 में जोड़ा गया ग्यारहवाँ कर्तव्य छह से चौदह वर्ष के बच्चों को शिक्षा के अवसर देने का माता-पिता का कर्तव्य है। "
   "ध्वज और राष्ट्रगान का सम्मान, पर्यावरण की रक्षा और वैज्ञानिक दृष्टिकोण का विकास 1976 में जोड़े गए कर्तव्यों में हैं।",
   "the-duty-added-in-2002",
   opts=["To respect the national flag and the national anthem",
         "To protect the natural environment, forests and wildlife",
         "To develop a scientific temper and the spirit of inquiry",
         "Parents' duty to see children aged 6 to 14 educated"],
   opts_hi=["राष्ट्रध्वज और राष्ट्रगान का सम्मान करना",
            "वनों और वन्यजीवों सहित प्राकृतिक पर्यावरण की रक्षा करना",
            "वैज्ञानिक दृष्टिकोण और खोज की भावना विकसित करना",
            "6-14 वर्ष के बच्चों की शिक्षा का माता-पिता का कर्तव्य"],
   ans=3, pos=3)
RQ(p, "Inference", "hard", "mcq",
   "Which one of the following best describes how, according to the passage, a court can give effect to a duty it cannot enforce?",
   "परिच्छेद के अनुसार, कोई न्यायालय ऐसे कर्तव्य को, जिसे वह लागू नहीं करा सकता, किस प्रकार प्रभावी बना सकता है?",
   "The passage says courts 'have drawn on them in reading laws'. A court cannot order a citizen to perform a duty, but when a law can be read in more than one way it may prefer the reading that fits a duty -- as in cases on protecting forests. "
   "The passage gives courts no power to fine citizens for neglecting a duty, to add duties to the Constitution, or to strike down laws merely because they fail to promote a duty.",
   "परिच्छेद कहता है कि न्यायालयों ने 'क़ानूनों की व्याख्या में उनका सहारा लिया है'। न्यायालय किसी नागरिक को कर्तव्य निभाने का आदेश नहीं दे सकता, पर जब किसी क़ानून को एक से अधिक तरह पढ़ा जा सके, तो वह उस अर्थ को वरीयता दे सकता है जो किसी कर्तव्य से मेल खाए -- जैसे वनों की रक्षा के मामलों में। "
   "परिच्छेद न्यायालयों को कर्तव्य की उपेक्षा पर नागरिकों पर जुर्माना लगाने, संविधान में कर्तव्य जोड़ने, या क़ानूनों को केवल इसलिए रद्द करने की शक्ति नहीं देता कि वे किसी कर्तव्य को बढ़ावा नहीं देते।",
   "how-a-court-uses-a-duty",
   opts=["By fining any citizen who is shown to have neglected one of the duties",
         "By adding new duties to the Constitution whenever it thinks them needed",
         "By preferring a reading of a law that fits the duty, where it can",
         "By striking down every law that does not actively promote one of the duties"],
   opts_hi=["किसी भी ऐसे नागरिक पर जुर्माना लगाकर जिसने कोई कर्तव्य निभाने में उपेक्षा की हो",
            "जब भी उसे आवश्यक लगे, संविधान में नए कर्तव्य जोड़कर",
            "जहाँ क़ानून अनुमति दे, उसके ऐसे अर्थ को वरीयता देकर जो कर्तव्य से मेल खाए",
            "हर उस क़ानून को रद्द करके जो किसी कर्तव्य को सक्रिय रूप से बढ़ावा नहीं देता"],
   ans=2, pos=2)

# ------------------------------------------------------------------ P05 carbon dating
p = passage("p05",
  "Every living plant and animal takes in carbon, and a tiny, steady share of that carbon is carbon-14, a radioactive form made in the upper air. When the organism dies, it stops taking in carbon, and its carbon-14 decays at a known rate: half of it is gone after about 5,730 years, half of what remains after another 5,730, and so on. Measuring how much is left therefore tells how long ago the organism died. The method, worked out by Willard Libby in the late 1940s, earned him a Nobel Prize. "
  "It has limits. It works only on what was once alive -- wood, bone, cloth, charcoal -- not on stone or pottery itself. After about 50,000 years too little carbon-14 is left to measure. And because the share of carbon-14 in the air has varied over time, dates must be corrected against records such as tree rings.",
  "हर जीवित पौधा और प्राणी कार्बन ग्रहण करता है, और उस कार्बन का एक बहुत छोटा, स्थिर अंश कार्बन-14 होता है, जो ऊपरी वायुमंडल में बनने वाला एक रेडियोधर्मी रूप है। जीव के मरने पर वह कार्बन ग्रहण करना बंद कर देता है, और उसका कार्बन-14 एक ज्ञात दर से क्षय होता है: लगभग 5,730 वर्षों में उसका आधा चला जाता है, अगले 5,730 वर्षों में बचे हुए का आधा, और इसी तरह। इसलिए कितना बचा है यह मापने से पता चलता है कि जीव कितने समय पहले मरा। विलार्ड लिबी द्वारा 1940 के दशक के अंत में विकसित इस पद्धति ने उन्हें नोबेल पुरस्कार दिलाया। "
  "इसकी सीमाएँ हैं। यह केवल उस पर काम करती है जो कभी जीवित था -- लकड़ी, हड्डी, कपड़ा, लकड़ी का कोयला -- स्वयं पत्थर या मिट्टी के बर्तन पर नहीं। लगभग 50,000 वर्षों के बाद मापने लायक़ कार्बन-14 बहुत कम बचता है। और चूँकि वायु में कार्बन-14 का अंश समय के साथ बदलता रहा है, तिथियों को वृक्ष-वलयों जैसे अभिलेखों से सुधारना पड़ता है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage explains how the steady decay of carbon-14 after death allows once-living remains to be dated, and sets out the method's limits -- only organic material, only up to about 50,000 years, and only with correction. "
   "It says the method does not work on stone, does not reach back millions of years, and needs correction rather than being exact on its own.",
   "परिच्छेद समझाता है कि मृत्यु के बाद कार्बन-14 का स्थिर क्षय कभी जीवित रहे अवशेषों का तिथि-निर्धारण कैसे संभव बनाता है, और पद्धति की सीमाएँ बताता है -- केवल जैविक पदार्थ, केवल लगभग 50,000 वर्ष तक, और केवल सुधार के साथ। "
   "वह कहता है कि पद्धति पत्थर पर काम नहीं करती, लाखों वर्ष पीछे तक नहीं पहुँचती, और अपने आप सटीक होने के बजाय उसे सुधार चाहिए।",
   "crux",
   opts=["Carbon dating can find the exact age of any object, whether stone, pottery or bone.",
         "Carbon-14's steady decay dates once-living remains, within limits.",
         "Carbon dating can measure ages of many millions of years without any correction.",
         "Living things stop taking in carbon long before they die, which spoils the method."],
   opts_hi=["कार्बन तिथि-निर्धारण किसी भी वस्तु, चाहे पत्थर, मिट्टी का बर्तन या हड्डी, की ठीक आयु बता सकता है।",
            "कार्बन-14 का स्थिर क्षय कभी जीवित रहे अवशेषों की तिथि बताता है, पदार्थ और आयु की सीमाओं के भीतर।",
            "कार्बन तिथि-निर्धारण बिना किसी सुधार के कई करोड़ वर्षों की आयु माप सकता है।",
            "जीव मरने से बहुत पहले कार्बन ग्रहण करना बंद कर देते हैं, जिससे पद्धति बिगड़ जाती है।"],
   ans=1, pos=1)
RQ(p, "Inference", "hard", "mcq",
   "A piece of charcoal from an ancient hearth has one-quarter of the carbon-14 that a living tree would have. On the passage's reasoning, roughly how long ago did the wood stop growing?",
   "एक प्राचीन चूल्हे से मिले लकड़ी के कोयले के एक टुकड़े में उतना एक-चौथाई कार्बन-14 है जितना किसी जीवित पेड़ में होता। परिच्छेद के तर्क से, लकड़ी ने मोटे तौर पर कितने समय पहले बढ़ना बंद किया?",
   "Half the carbon-14 goes in about 5,730 years, leaving a half; half of that goes in the next 5,730 years, leaving a quarter. So a quarter left means about two half-lives, roughly 11,460 years. "
   "5,730 years would leave a half, not a quarter; about 17,190 years would leave an eighth; and 22,920 years is four half-lives, which would leave a sixteenth -- treating 'a quarter' as four steps rather than two.",
   "लगभग 5,730 वर्षों में आधा कार्बन-14 चला जाता है, आधा बचता है; अगले 5,730 वर्षों में उसका आधा चला जाता है, एक-चौथाई बचता है। इसलिए एक-चौथाई बचने का अर्थ है लगभग दो अर्ध-आयु, मोटे तौर पर 11,460 वर्ष। "
   "5,730 वर्ष आधा छोड़ते, एक-चौथाई नहीं; लगभग 17,190 वर्ष आठवाँ भाग छोड़ते; और 22,920 वर्ष चार अर्ध-आयु हैं, जो सोलहवाँ भाग छोड़ते -- 'एक-चौथाई' को दो के बजाय चार चरण मानकर।",
   "the-age-of-a-piece-of-charcoal",
   opts=["About 5,730 years", "About 22,920 years", "About 17,190 years", "About 11,460 years"],
   opts_hi=["लगभग 5,730 वर्ष", "लगभग 22,920 वर्ष", "लगभग 17,190 वर्ष", "लगभग 11,460 वर्ष"],
   ans=3, pos=3)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Only 1 is valid. The method works only on what was once alive, so a stone tool cannot be dated by it directly, though charcoal or bone found with it might be. "
   "2 is not supported: the passage says dates must be corrected against tree rings because the share of carbon-14 in the air has varied, not that the method is useless; correction is what makes it reliable.",
   "केवल 1 वैध है। पद्धति केवल उस पर काम करती है जो कभी जीवित था, इसलिए पत्थर के औज़ार की तिथि उससे सीधे नहीं निकाली जा सकती, यद्यपि उसके साथ मिले कोयले या हड्डी की निकाली जा सकती है। "
   "2 समर्थित नहीं है: परिच्छेद कहता है कि वायु में कार्बन-14 का अंश बदलता रहा है इसलिए तिथियों को वृक्ष-वलयों से सुधारना पड़ता है, यह नहीं कि पद्धति बेकार है; सुधार ही उसे विश्वसनीय बनाता है।",
   "conclusions",
   st=["A stone tool cannot itself be dated by measuring its carbon-14.",
       "Because the share of carbon-14 in the air has varied, carbon dates cannot be trusted at all."],
   st_hi=["पत्थर के किसी औज़ार की तिथि स्वयं उसके कार्बन-14 को मापकर नहीं निकाली जा सकती।",
          "चूँकि वायु में कार्बन-14 का अंश बदलता रहा है, कार्बन तिथियों पर बिल्कुल भरोसा नहीं किया जा सकता।"],
   key=0)

# ------------------------------------------------------------------ P06 the bamboo that flowers once in fifty years
p = passage("p06",
  "Across much of Mizoram grows a bamboo that flowers only once in about fifty years, and when it does, it flowers over huge areas at the same time and then dies. The flowering brings a flood of fruit, and the rats that feed on it multiply enormously. When the fruit is gone, the rats turn to the farmers' fields and granaries, and famine can follow. The flowering of the late 1950s was followed by a severe famine and lasting bitterness over how slowly help had come. "
  "When the bamboo flowered again in 2006-07, the cycle was known in advance. Farmers were encouraged to grow crops the rats like less, to store grain safely and to trap rats, and food stocks were built up. The flowering could not be stopped, but a disaster that comes on a known schedule need not take people by surprise.",
  "मिज़ोरम के बड़े भाग में एक ऐसा बाँस उगता है जो लगभग पचास वर्षों में केवल एक बार फूलता है, और जब फूलता है, तो विशाल क्षेत्रों में एक साथ फूलता है और फिर मर जाता है। फूलने से फलों की बाढ़ आती है, और उन्हें खाने वाले चूहे बहुत अधिक बढ़ जाते हैं। फल समाप्त होने पर चूहे किसानों के खेतों और अन्न-भंडारों की ओर मुड़ते हैं, और अकाल पड़ सकता है। 1950 के दशक के अंत के फूलने के बाद एक भयंकर अकाल पड़ा और इस बात पर स्थायी कड़वाहट रही कि सहायता कितनी धीरे आई। "
  "जब 2006-07 में बाँस फिर फूला, तो यह चक्र पहले से ज्ञात था। किसानों को ऐसी फ़सलें उगाने के लिए प्रोत्साहित किया गया जो चूहों को कम पसंद हों, अनाज सुरक्षित रखने और चूहे फँसाने के लिए, और खाद्य भंडार बनाए गए। फूलना रोका नहीं जा सका, पर जो आपदा ज्ञात समय-सारणी पर आती है, उसे लोगों को अचानक घेरने की आवश्यकता नहीं।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage traces how a rare, region-wide flowering of bamboo leads to rats and famine, and contrasts the famine of the 1950s with the preparation of 2006-07: a disaster that comes on a known schedule can be prepared for. "
   "It says the flowering could not be stopped, so it was not prevented; it does not blame the farmers; and it presents the rats as following the fruit, not as the bamboo's cause.",
   "परिच्छेद बताता है कि बाँस का एक दुर्लभ, क्षेत्र-व्यापी फूलना कैसे चूहों और अकाल तक ले जाता है, और 1950 के दशक के अकाल की तुलना 2006-07 की तैयारी से करता है: ज्ञात समय-सारणी पर आने वाली आपदा के लिए तैयारी की जा सकती है। "
   "वह कहता है कि फूलना रोका नहीं जा सका, इसलिए उसे टाला नहीं गया; वह किसानों को दोष नहीं देता; और वह चूहों को फलों के बाद आने वाला बताता है, बाँस का कारण नहीं।",
   "crux",
   opts=["In 2006-07 scientists found a way to stop the bamboo from flowering at all.",
         "The famine of the 1950s was caused by the carelessness of the farmers themselves.",
         "A disaster on a known cycle can be prepared for, even if it cannot be stopped.",
         "Rats cause the bamboo to flower, which is why the two always appear together."],
   opts_hi=["2006-07 में वैज्ञानिकों ने बाँस को फूलने से पूरी तरह रोकने का उपाय खोज लिया।",
            "1950 के दशक का अकाल स्वयं किसानों की लापरवाही से पड़ा था।",
            "ज्ञात चक्र वाली आपदा की तैयारी हो सकती है, भले उसे रोका न जा सके।",
            "चूहे बाँस को फुलाते हैं, इसीलिए दोनों हमेशा साथ दिखते हैं।"],
   ans=2, pos=2)
RQ(p, "Inference", "hard", "mcq",
   "According to the passage, why do the rats turn to the farmers' fields?",
   "परिच्छेद के अनुसार, चूहे किसानों के खेतों की ओर क्यों मुड़ते हैं?",
   "The bamboo's fruit lets the rats multiply enormously; when the fruit is gone, a far larger rat population than usual is left with nothing to eat in the forest, so it turns to the fields and granaries. "
   "The passage does not say the rats prefer crops to fruit, that the dying bamboo poisons them, or that farmers lure them in.",
   "बाँस के फल चूहों को बहुत अधिक बढ़ने देते हैं; फल समाप्त होने पर सामान्य से कहीं बड़ी चूहों की आबादी के पास जंगल में खाने को कुछ नहीं रहता, इसलिए वह खेतों और अन्न-भंडारों की ओर मुड़ती है। "
   "परिच्छेद यह नहीं कहता कि चूहे फलों से अधिक फ़सलें पसंद करते हैं, कि मरता बाँस उन्हें विष देता है, या कि किसान उन्हें लुभाते हैं।",
   "why-the-rats-turn-to-the-fields",
   opts=["Rats swollen in number by the fruit have nothing to eat once it is gone.",
         "Rats always prefer ripe crops to bamboo fruit, whenever both are on offer to them.",
         "The dying bamboo releases a poison that drives the rats out of the forest at once.",
         "Farmers leave grain in the forest to keep the rats away from their villages."],
   opts_hi=["फलों से बढ़ी चूहों की आबादी के पास फल ख़त्म होने पर खाने को कुछ नहीं रहता।",
            "जब भी दोनों उपलब्ध हों, चूहे हमेशा बाँस के फलों से अधिक पकी फ़सलें पसंद करते हैं।",
            "मरता हुआ बाँस एक विष छोड़ता है जो चूहों को तुरंत जंगल से बाहर भगा देता है।",
            "किसान चूहों को अपने गाँवों से दूर रखने के लिए जंगल में अनाज छोड़ देते हैं।"],
   ans=0, pos=0)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Only 2 is valid. The passage says that in 2006-07 the cycle was known in advance and farmers and the government prepared, which shows that knowing when a hazard will come allows its effects to be reduced. "
   "1 goes beyond the passage: it says help came slowly after the 1950s flowering and that preparations were made in 2006-07, but it does not say that no hardship at all followed the second flowering.",
   "केवल 2 वैध है। परिच्छेद कहता है कि 2006-07 में चक्र पहले से ज्ञात था और किसानों तथा सरकार ने तैयारी की, जो दिखाता है कि किसी संकट के आने का समय जानने से उसके प्रभाव घटाए जा सकते हैं। "
   "1 परिच्छेद से आगे जाता है: वह कहता है कि 1950 के दशक के फूलने के बाद सहायता धीरे आई और 2006-07 में तैयारी की गई, पर यह नहीं कहता कि दूसरे फूलने के बाद कोई कठिनाई ही नहीं हुई।",
   "conclusions",
   st=["The flowering of 2006-07 caused no hardship of any kind to the people of Mizoram.",
       "Knowing in advance when a natural hazard will come can help to reduce the harm it does."],
   st_hi=["2006-07 के फूलने से मिज़ोरम के लोगों को किसी भी प्रकार की कठिनाई नहीं हुई।",
          "किसी प्राकृतिक संकट के आने का समय पहले से जानना उसकी हानि घटाने में सहायक हो सकता है।"],
   key=1)

# ------------------------------------------------------------------ P07 the last case of polio in India
p = passage("p07",
  "As late as 2009 India reported more cases of polio than any other country, and many experts doubted that it could be rid of the disease. The last case was recorded in January 2011, in a girl in Howrah, and in 2014 the World Health Organization's South-East Asia region, which includes India, was certified free of polio. "
  "The vaccine had long been available; what made the difference was reaching every child. On national polio days volunteers gave drops to children under five in homes, at railway stations and bus stands, and on moving trains; families who moved for work were tracked; and in crowded districts of Uttar Pradesh and Bihar, where poor sanitation made the vaccine work less well, children were given many more doses. The last stage of ending a disease is often the hardest, because the cases that remain are among the people who are hardest to reach.",
  "2009 तक भारत में किसी भी अन्य देश से अधिक पोलियो के मामले दर्ज होते थे, और कई विशेषज्ञों को संदेह था कि देश इस रोग से मुक्त हो पाएगा। अंतिम मामला जनवरी 2011 में हावड़ा में एक बच्ची में दर्ज हुआ, और 2014 में विश्व स्वास्थ्य संगठन के दक्षिण-पूर्व एशिया क्षेत्र को, जिसमें भारत शामिल है, पोलियो-मुक्त प्रमाणित किया गया। "
  "टीका बहुत पहले से उपलब्ध था; अंतर हर बच्चे तक पहुँचने से आया। राष्ट्रीय पोलियो दिवसों पर स्वयंसेवकों ने पाँच वर्ष से कम आयु के बच्चों को घरों में, रेलवे स्टेशनों और बस अड्डों पर, और चलती रेलगाड़ियों में बूँदें पिलाईं; काम के लिए जगह बदलने वाले परिवारों का पता रखा गया; और उत्तर प्रदेश व बिहार के भीड़-भरे ज़िलों में, जहाँ ख़राब स्वच्छता के कारण टीका कम असर करता था, बच्चों को कहीं अधिक ख़ुराकें दी गईं। किसी रोग को समाप्त करने का अंतिम चरण प्रायः सबसे कठिन होता है, क्योंकि बचे हुए मामले उन लोगों में होते हैं जिन तक पहुँचना सबसे कठिन होता है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage explains that India ended polio not through a new vaccine but by reaching every child -- on trains, among migrant families, with extra doses where the vaccine worked less well -- and notes that the last stage is hardest because the remaining cases are among the hardest to reach. "
   "It says the vaccine had long been available; it does not say India still reports cases; and it does not credit a single dose given to each child.",
   "परिच्छेद बताता है कि भारत ने पोलियो को किसी नए टीके से नहीं, बल्कि हर बच्चे तक पहुँचकर समाप्त किया -- रेलगाड़ियों में, प्रवासी परिवारों में, जहाँ टीका कम असर करता था वहाँ अतिरिक्त ख़ुराकें देकर -- और कहता है कि अंतिम चरण सबसे कठिन होता है क्योंकि बचे मामले सबसे कठिनाई से पहुँचे जाने वालों में होते हैं। "
   "वह कहता है कि टीका बहुत पहले से उपलब्ध था; वह यह नहीं कहता कि भारत में अब भी मामले दर्ज होते हैं; और वह हर बच्चे को दी गई एक ही ख़ुराक को श्रेय नहीं देता।",
   "crux",
   opts=["India ended polio once a new and far better vaccine was finally invented in 2010.",
         "India still reports more cases of polio than any other country in the world.",
         "A single dose given to every child was enough to end polio across the country.",
         "Polio was ended by reaching every child, the last few being the hardest."],
   opts_hi=["2010 में अंततः एक नया और कहीं बेहतर टीका बनने पर भारत ने पोलियो समाप्त किया।",
            "भारत में अब भी दुनिया के किसी भी अन्य देश से अधिक पोलियो के मामले दर्ज होते हैं।",
            "हर बच्चे को दी गई एक ही ख़ुराक देश भर में पोलियो समाप्त करने के लिए पर्याप्त थी।",
            "पोलियो हर बच्चे तक पहुँचकर समाप्त हुआ, सबसे कठिन भाग अंतिम कुछ तक पहुँचना था।"],
   ans=3, pos=3)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Neither is valid. 1 goes too far: the passage says the region was certified free of polio in 2014, not that the vaccine is no longer given; nothing in it says vaccination stopped. "
   "2 misreads the passage: it says the vaccine worked less well where sanitation was poor, and children there were given more doses -- not that the vaccine did not work at all in those districts.",
   "कोई भी वैध नहीं। 1 बहुत आगे जाता है: परिच्छेद कहता है कि क्षेत्र 2014 में पोलियो-मुक्त प्रमाणित हुआ, यह नहीं कि टीका अब नहीं दिया जाता; उसमें कुछ भी यह नहीं कहता कि टीकाकरण रुक गया। "
   "2 परिच्छेद को ग़लत पढ़ता है: वह कहता है कि जहाँ स्वच्छता ख़राब थी वहाँ टीका कम असर करता था, और वहाँ बच्चों को अधिक ख़ुराकें दी गईं -- यह नहीं कि उन ज़िलों में टीका बिल्कुल काम नहीं करता था।",
   "conclusions",
   st=["Since 2014 children in India have no longer been given the polio vaccine.",
       "In the crowded districts of Uttar Pradesh and Bihar the vaccine did not work at all."],
   st_hi=["2014 के बाद से भारत में बच्चों को पोलियो का टीका नहीं दिया जाता।",
          "उत्तर प्रदेश और बिहार के भीड़-भरे ज़िलों में टीका बिल्कुल काम नहीं करता था।"],
   key=3)
RQ(p, "Inference", "hard", "mcq",
   "Why does the passage say the last stage of ending a disease is often the hardest?",
   "परिच्छेद यह क्यों कहता है कि किसी रोग को समाप्त करने का अंतिम चरण प्रायः सबसे कठिन होता है?",
   "The passage says the cases that remain are among the people who are hardest to reach. Easy-to-reach children are protected first; what is left is concentrated among those who move, live in crowded or poorly served places, or respond less well to the vaccine. "
   "The passage does not say the vaccine loses its power over time, that volunteers lose interest, or that the disease becomes more deadly near the end.",
   "परिच्छेद कहता है कि बचे हुए मामले उन लोगों में होते हैं जिन तक पहुँचना सबसे कठिन है। आसानी से पहुँचे जाने वाले बच्चे पहले सुरक्षित होते हैं; जो बचता है वह उन लोगों में केंद्रित होता है जो जगह बदलते हैं, भीड़-भरी या कम सुविधा वाली जगहों में रहते हैं, या टीके पर कम प्रतिक्रिया करते हैं। "
   "परिच्छेद यह नहीं कहता कि टीका समय के साथ शक्ति खो देता है, कि स्वयंसेवकों की रुचि घट जाती है, या कि अंत के निकट रोग अधिक घातक हो जाता है।",
   "why-the-last-stage-is-hardest",
   opts=["The vaccine slowly loses its power after it has been used for many years.",
         "The cases that remain are among the people who are hardest to reach.",
         "Volunteers lose interest once most of the cases have already disappeared.",
         "The disease becomes far more deadly as the number of cases falls."],
   opts_hi=["कई वर्षों तक उपयोग के बाद टीका धीरे-धीरे अपनी शक्ति खो देता है।",
            "बचे मामले उन लोगों में होते हैं जिन तक पहुँचना सबसे कठिन है।",
            "अधिकांश मामले समाप्त हो जाने पर स्वयंसेवकों की रुचि घट जाती है।",
            "मामलों की संख्या घटने के साथ रोग कहीं अधिक घातक हो जाता है।"],
   ans=1, pos=1)

# ------------------------------------------------------------------ P08 the ship of Theseus
p = passage("p08",
  "The Greek writer Plutarch tells of the ship in which the hero Theseus sailed, kept by the people of Athens for centuries. As its planks rotted they were replaced one by one, until in time no original plank was left. Philosophers argued over whether it was still the same ship. The English philosopher Thomas Hobbes later sharpened the puzzle: suppose someone had kept every discarded plank and built them into a second ship. Which of the two would then be the ship of Theseus? "
  "The puzzle is not only about ships. The cells of a human body are replaced over the years, and an institution may keep its name long after every member has changed. Perhaps what makes a thing the same over time is not its material but the continuity of its form and its use -- though Hobbes's second ship shows that even this answer is not free of difficulty.",
  "यूनानी लेखक प्लूटार्क उस जहाज़ की कथा कहते हैं जिसमें नायक थीसियस ने यात्रा की थी, और जिसे एथेंस के लोगों ने सदियों तक सँभाले रखा। जैसे-जैसे उसके तख़्ते सड़ते गए, उन्हें एक-एक करके बदला गया, जब तक समय के साथ कोई मूल तख़्ता नहीं बचा। दार्शनिकों ने बहस की कि क्या वह अब भी वही जहाज़ था। अंग्रेज़ दार्शनिक थॉमस हॉब्स ने बाद में पहेली को और पैना किया: मान लीजिए किसी ने हर फेंका गया तख़्ता सँभाल रखा हो और उनसे एक दूसरा जहाज़ बना दिया हो। तब दोनों में से थीसियस का जहाज़ कौन-सा होगा? "
  "यह पहेली केवल जहाज़ों के बारे में नहीं। मानव शरीर की कोशिकाएँ वर्षों में बदल जाती हैं, और कोई संस्था अपने हर सदस्य के बदल जाने के बहुत बाद तक अपना नाम रख सकती है। हो सकता है कि किसी चीज़ को समय के साथ वही बनाने वाली बात उसका पदार्थ नहीं, बल्कि उसके रूप और उपयोग की निरंतरता हो -- यद्यपि हॉब्स का दूसरा जहाज़ दिखाता है कि यह उत्तर भी कठिनाई से मुक्त नहीं।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage uses the ship of Theseus to raise the question of what keeps a thing the same over time, suggests continuity of form and use rather than material, and admits that Hobbes's second ship makes even that answer difficult. "
   "It does not settle the puzzle in favour of the rebuilt ship, does not say the question is only about ships, and does not call it meaningless.",
   "परिच्छेद थीसियस के जहाज़ से यह प्रश्न उठाता है कि किसी चीज़ को समय के साथ वही क्या बनाए रखता है, पदार्थ के बजाय रूप और उपयोग की निरंतरता का सुझाव देता है, और मानता है कि हॉब्स का दूसरा जहाज़ उस उत्तर को भी कठिन बना देता है। "
   "वह पहेली को दोबारा बने जहाज़ के पक्ष में हल नहीं करता, यह नहीं कहता कि प्रश्न केवल जहाज़ों के बारे में है, और उसे अर्थहीन नहीं कहता।",
   "crux",
   opts=["What keeps a thing the same over time is a hard question that no answer fully settles.",
         "The ship rebuilt from the old planks is plainly the true ship of Theseus, as Hobbes proved.",
         "The puzzle concerns ships alone and has nothing to say about people or institutions.",
         "Questions about whether a thing stays the same are meaningless and should not be asked."],
   opts_hi=["चीज़ को समय के साथ वही क्या बनाए रखता है, यह कठिन प्रश्न है जिसे कोई उत्तर पूरा हल नहीं करता।",
            "पुराने तख़्तों से फिर से बना जहाज़ स्पष्ट रूप से थीसियस का असली जहाज़ है, जैसा हॉब्स ने सिद्ध किया।",
            "यह पहेली केवल जहाज़ों से संबंधित है और लोगों या संस्थाओं के बारे में कुछ नहीं कहती।",
            "कोई चीज़ वही रहती है या नहीं, ऐसे प्रश्न अर्थहीन हैं और पूछे नहीं जाने चाहिए।"],
   ans=0, pos=0)
RQ(p, "Inference", "hard", "mcq",
   "Why, in the passage's terms, does Hobbes's second ship make the 'continuity of form and use' answer difficult?",
   "परिच्छेद के शब्दों में, हॉब्स का दूसरा जहाज़ 'रूप और उपयोग की निरंतरता' वाले उत्तर को कठिन क्यों बनाता है?",
   "The continuity answer would make the repaired ship, which kept its form and stayed in use, the ship of Theseus. But the second ship is made of all the original material, which seems an equally strong claim to be the same ship -- so there are now two rival candidates, and continuity alone does not obviously win. "
   "The passage does not say the second ship sank, that it could never be built, or that it had a different shape.",
   "निरंतरता वाला उत्तर मरम्मत किए गए जहाज़ को, जिसने अपना रूप रखा और उपयोग में रहा, थीसियस का जहाज़ बनाएगा। पर दूसरा जहाज़ पूरी मूल सामग्री से बना है, जो उसी जहाज़ होने का उतना ही मज़बूत दावा लगता है -- इसलिए अब दो प्रतिद्वंद्वी दावेदार हैं, और अकेली निरंतरता स्पष्ट रूप से नहीं जीतती। "
   "परिच्छेद यह नहीं कहता कि दूसरा जहाज़ डूब गया, कि वह कभी बन नहीं सकता था, या कि उसका आकार अलग था।",
   "why-the-second-ship-makes-it-hard",
   opts=["The second ship would have sunk at once, being built of rotten planks.",
         "No one could ever have kept all the old planks, so the question cannot arise.",
         "The second ship, made of all the old planks, has a rival claim to be the ship.",
         "The second ship would have had a different shape from the ship that Theseus sailed."],
   opts_hi=["दूसरा जहाज़, सड़े तख़्तों से बना होने के कारण, तुरंत डूब जाता।",
            "कोई भी कभी सभी पुराने तख़्ते सँभाल नहीं सकता था, इसलिए प्रश्न उठ ही नहीं सकता।",
            "सभी पुराने तख़्तों से बने दूसरे जहाज़ का भी प्रतिद्वंद्वी दावा है।",
            "दूसरे जहाज़ का आकार उस जहाज़ से अलग होता जिसमें थीसियस ने यात्रा की।"],
   ans=2, pos=2)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Both are valid. The passage applies the puzzle to institutions that keep their name after every member has changed, so it treats a body's identity as not simply a matter of who belongs to it at a given time (1). "
   "And it says that, on the view it suggests, sameness lies in continuity of form and use rather than material -- so a body whose cells have all been replaced could still count as the same body (2).",
   "दोनों वैध हैं। परिच्छेद पहेली को उन संस्थाओं पर लागू करता है जो हर सदस्य के बदल जाने के बाद भी अपना नाम रखती हैं, इसलिए वह किसी संस्था की पहचान को केवल इस बात का प्रश्न नहीं मानता कि किसी समय उसमें कौन है (1)। "
   "और वह कहता है कि उसके सुझाए विचार में समानता पदार्थ के बजाय रूप और उपयोग की निरंतरता में है -- इसलिए जिस शरीर की सभी कोशिकाएँ बदल गई हों, वह भी वही शरीर माना जा सकता है (2)।",
   "conclusions",
   st=["On the passage's view, an institution need not lose its identity just because all its members have changed.",
       "On the view the passage suggests, a body whose cells have all been replaced could still be the same body."],
   st_hi=["परिच्छेद के विचार में, कोई संस्था केवल इसलिए अपनी पहचान नहीं खोती कि उसके सभी सदस्य बदल गए हों।",
          "परिच्छेद के सुझाए विचार में, जिस शरीर की सभी कोशिकाएँ बदल गई हों, वह फिर भी वही शरीर हो सकता है।"],
   key=2)

# ------------------------------------------------------------------ P09 Occam's razor
p = passage("p09",
  "A rule of thinking named after William of Ockham, a fourteenth-century English philosopher, advises that when two explanations fit the facts equally well, the one that assumes less should be preferred. It is called Occam's razor because it shaves away needless assumptions. Doctors put it in their own way: when you hear hoofbeats, think of horses, not zebras -- a common illness is a likelier cause of a symptom than a rare one. "
  "The razor is a guide to where to look first, not a proof. The simpler explanation is not always the true one; zebras do exist, and a doctor who never considers a rare disease will sometimes miss it. The razor tells us how to choose between explanations that the evidence cannot yet separate. It does not tell us to ignore evidence that favours the more complicated one.",
  "चौदहवीं शताब्दी के अंग्रेज़ दार्शनिक विलियम ऑफ़ ओखम के नाम पर रखा गया सोचने का एक नियम सलाह देता है कि जब दो व्याख्याएँ तथ्यों पर समान रूप से ठीक बैठें, तो कम मान्यताएँ लेने वाली को वरीयता दी जाए। इसे ओखम का उस्तरा कहते हैं क्योंकि यह अनावश्यक मान्यताओं को छील देता है। डॉक्टर इसे अपने ढंग से कहते हैं: जब खुरों की आवाज़ सुनो, तो घोड़ों के बारे में सोचो, ज़ेबरा के नहीं -- किसी लक्षण का कारण दुर्लभ रोग की तुलना में आम रोग होने की अधिक संभावना है। "
  "उस्तरा यह बताने वाला मार्गदर्शक है कि पहले कहाँ देखें, कोई प्रमाण नहीं। सरल व्याख्या हमेशा सत्य नहीं होती; ज़ेबरा भी होते हैं, और जो डॉक्टर कभी दुर्लभ रोग पर विचार नहीं करता, वह कभी-कभी उसे चूक जाएगा। उस्तरा बताता है कि उन व्याख्याओं में कैसे चुनें जिन्हें प्रमाण अभी अलग नहीं कर सकते। वह हमें अधिक जटिल व्याख्या के पक्ष वाले प्रमाण को अनदेखा करने को नहीं कहता।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage presents Occam's razor as a guide for choosing, among explanations the evidence cannot yet separate, the one that assumes less -- and warns that it is not proof and must give way to evidence for the more complicated explanation. "
   "It says the simpler explanation is not always true; it says rare diseases do occur; and it says the razor does not tell us to ignore evidence.",
   "परिच्छेद ओखम के उस्तरे को उन व्याख्याओं में से, जिन्हें प्रमाण अभी अलग नहीं कर सकते, कम मान्यता लेने वाली को चुनने का मार्गदर्शक बताता है -- और चेताता है कि यह प्रमाण नहीं है और अधिक जटिल व्याख्या के पक्ष वाले प्रमाण के आगे झुकना चाहिए। "
   "वह कहता है कि सरल व्याख्या हमेशा सत्य नहीं होती; वह कहता है कि दुर्लभ रोग होते हैं; और वह कहता है कि उस्तरा हमें प्रमाण अनदेखा करने को नहीं कहता।",
   "crux",
   opts=["The simplest explanation of anything is always the true one, as Ockham proved.",
         "Prefer the leaner explanation when evidence cannot choose; follow evidence when it can.",
         "Doctors should never think of rare diseases, since common ones are far more likely.",
         "When evidence favours a complicated explanation, it should be set aside for a simpler one."],
   opts_hi=["किसी भी बात की सबसे सरल व्याख्या हमेशा सत्य होती है, जैसा ओखम ने सिद्ध किया।",
            "जब प्रमाण न चुन सके तो कम मानने वाली व्याख्या चुनिए, पर जब चुन सके तो प्रमाण के साथ चलिए।",
            "डॉक्टरों को कभी दुर्लभ रोगों के बारे में नहीं सोचना चाहिए, क्योंकि आम रोग कहीं अधिक संभावित हैं।",
            "जब प्रमाण किसी जटिल व्याख्या के पक्ष में हो, तो उसे किसी सरल व्याख्या के लिए अलग रख देना चाहिए।"],
   ans=1, pos=1)
RQ(p, "Inference", "hard", "mcq",
   "A doctor sees a patient with a fever and first tests for a common infection. The test is negative, and further tests point clearly to a rare disease. On the passage's reasoning, what should the doctor do?",
   "एक डॉक्टर बुख़ार वाले रोगी को देखता है और पहले एक आम संक्रमण की जाँच करता है। जाँच नकारात्मक आती है, और आगे की जाँचें स्पष्ट रूप से एक दुर्लभ रोग की ओर संकेत करती हैं। परिच्छेद के तर्क से डॉक्टर को क्या करना चाहिए?",
   "The razor told the doctor where to look first, and testing for the common infection was right. Once the evidence clearly favours the rare disease, the razor no longer applies -- it chooses only between explanations the evidence cannot separate -- so the doctor should treat the rare disease. "
   "Sticking with the common infection ignores the evidence; repeating the first test indefinitely puts the razor above the evidence; and calling the case unexplained refuses the explanation the evidence supports.",
   "उस्तरे ने डॉक्टर को बताया कि पहले कहाँ देखें, और आम संक्रमण की जाँच करना सही था। जब प्रमाण स्पष्ट रूप से दुर्लभ रोग के पक्ष में हो, तो उस्तरा लागू नहीं होता -- वह केवल उन व्याख्याओं में चुनता है जिन्हें प्रमाण अलग नहीं कर सकते -- इसलिए डॉक्टर को दुर्लभ रोग का उपचार करना चाहिए। "
   "आम संक्रमण पर टिके रहना प्रमाण को अनदेखा करता है; पहली जाँच को अनिश्चित काल तक दोहराना उस्तरे को प्रमाण से ऊपर रखता है; और मामले को अव्याख्यात कहना उस व्याख्या को ठुकराता है जिसका प्रमाण समर्थन करता है।",
   "what-the-doctor-should-do",
   opts=["Keep treating the common infection, since common illnesses are always more likely.",
         "Repeat the test for the common infection until it finally comes back positive.",
         "Declare the fever unexplained, since a rare disease cannot be the simplest answer.",
         "Treat the rare disease, now that the evidence clearly separates the explanations."],
   opts_hi=["आम संक्रमण का उपचार जारी रखना, क्योंकि आम रोग हमेशा अधिक संभावित होते हैं।",
            "आम संक्रमण की जाँच तब तक दोहराना जब तक वह अंततः सकारात्मक न आ जाए।",
            "बुख़ार को अव्याख्यात घोषित करना, क्योंकि दुर्लभ रोग सबसे सरल उत्तर नहीं हो सकता।",
            "दुर्लभ रोग का उपचार करना, अब जब प्रमाण व्याख्याओं को स्पष्ट अलग करता है।"],
   ans=3, pos=3)
RQ(p, "Inference", "medium", "mcq",
   "Which one of the following situations is the kind the razor is meant for?",
   "निम्नलिखित में से कौन-सी स्थिति उस प्रकार की है जिसके लिए उस्तरा बना है?",
   "The razor is for choosing between explanations that fit the facts equally well. A missing key that could equally have been mislaid by its owner or stolen by a burglar who took nothing else, with no other sign of a break-in, is such a case: mislaying it assumes less. "
   "A case settled by a clear photograph, one with only a single explanation, and one where the evidence plainly favours the more complicated story are not cases the razor is needed for.",
   "उस्तरा उन व्याख्याओं में चुनने के लिए है जो तथ्यों पर समान रूप से ठीक बैठें। खोई चाबी, जिसे उतनी ही संभावना से मालिक ने कहीं रख दिया हो या किसी ऐसे चोर ने चुराया हो जिसने और कुछ नहीं लिया, जबकि सेंध का कोई और संकेत न हो, ऐसी ही स्थिति है: कहीं रख देना कम मानता है। "
   "स्पष्ट फ़ोटो से तय हुआ मामला, केवल एक व्याख्या वाला मामला, और ऐसा मामला जहाँ प्रमाण स्पष्ट रूप से अधिक जटिल कहानी के पक्ष में हो, वे मामले नहीं जिनके लिए उस्तरे की आवश्यकता है।",
   "a-case-for-the-razor",
   opts=["A key is missing; with no sign of a break-in, it may be mislaid or stolen.",
         "A clear photograph shows exactly who took the missing key from the office drawer.",
         "Only one explanation of the event has been offered, and nothing contradicts it.",
         "The evidence plainly favours the more complicated of two accounts of an event."],
   opts_hi=["चाबी ग़ायब है; सेंध का संकेत नहीं, वह कहीं रखी गई या चुराई गई हो सकती है।",
            "एक स्पष्ट फ़ोटो ठीक दिखाता है कि कार्यालय की दराज़ से खोई चाबी किसने ली।",
            "घटना की केवल एक व्याख्या दी गई है, और कुछ भी उसका खंडन नहीं करता।",
            "प्रमाण किसी घटना के दो विवरणों में से अधिक जटिल वाले के पक्ष में स्पष्ट है।"],
   ans=0, pos=0)
