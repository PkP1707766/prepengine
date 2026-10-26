# -*- coding: utf-8 -*-
"""CSAT Level 4 · Simulator 9 -- Reading Comprehension: 10 short passages, 23 items (3 x 3, 7 x 2), Layout C.

The 2026 shape: more passages, shorter ones, fewer items each. Each passage still turns -- a claim, then its limit.
Themes, none used in Levels 1-3 or Simulators 1-8: the Pygmalion effect in a classroom, Mill's harm principle, the
Permanent Settlement of 1793, Wegener and the drifting continents, Keynes's beauty contest, the stepwells of western
India, Project Tiger, the Right to Information Act, Florence Nightingale's diagrams, and the rise in test scores named
after James Flynn. Item types: main idea 10, inference 11, specific detail 2. Two-statement keys 1 / 1 / 2 / 2 (1 only /
2 only / Both / Neither). Difficulty 1 easy / 14 medium / 8 hard. Options are named by content in every explanation."""
from csat_common import passage, RQ

CRUX = "Which one of the following statements best reflects the crux of the passage?"
CRUX_HI = "निम्नलिखित में से कौन-सा कथन परिच्छेद के सार को सबसे अच्छी तरह व्यक्त करता है?"
VALID = "On the basis of the passage, which of the following conclusions is/are valid?"
VALID_HI = "परिच्छेद के आधार पर निम्नलिखित में से कौन-सा/से निष्कर्ष वैध है/हैं?"

# ------------------------------------------------------------------ P01 the Pygmalion effect (2)
p = passage("p01",
  "In a study published in 1968, the psychologist Robert Rosenthal and the school principal Lenore Jacobson tested the pupils of an American primary school and then told the teachers that certain children -- in fact chosen at random -- were about to 'bloom' intellectually. When the children were tested again some months later, those labelled bloomers had gained more than the others, especially in the youngest classes. The authors concluded that the teachers' expectations had shaped how the children learned, perhaps through the warmth, attention and challenge the teachers gave them. The finding became famous as the Pygmalion effect. "
  "Later attempts to repeat the study found the effect real but usually small, and largest when teachers formed their expectations before they had come to know the children.",
  "1968 में प्रकाशित एक अध्ययन में मनोवैज्ञानिक रॉबर्ट रोज़ेन्थल और विद्यालय की प्रधानाचार्य लेनोर जैकबसन ने एक अमेरिकी प्राथमिक विद्यालय के विद्यार्थियों की परीक्षा ली और फिर शिक्षकों को बताया कि कुछ बच्चे -- जो वास्तव में यादृच्छिक रूप से चुने गए थे -- बौद्धिक रूप से 'खिलने' वाले हैं। कुछ महीने बाद जब बच्चों की फिर परीक्षा हुई, तो 'खिलने वाले' कहे गए बच्चों ने बाक़ियों से अधिक प्रगति की थी, विशेषकर सबसे छोटी कक्षाओं में। लेखकों ने निष्कर्ष निकाला कि शिक्षकों की अपेक्षाओं ने बच्चों के सीखने को आकार दिया, शायद उस स्नेह, ध्यान और चुनौती के माध्यम से जो शिक्षकों ने उन्हें दी। यह निष्कर्ष पिग्मेलियन प्रभाव के नाम से प्रसिद्ध हुआ। "
  "अध्ययन को दोहराने के बाद के प्रयासों ने प्रभाव को वास्तविक पर प्रायः छोटा पाया, और सबसे बड़ा तब जब शिक्षकों ने बच्चों को जानने से पहले ही अपनी अपेक्षाएँ बना ली थीं।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage reports a famous finding that teachers' expectations shaped pupils' progress, and ends by noting that later studies found the effect real but usually small. "
   "It says the bloomers were chosen at random, so they were not truly abler; it does not say that intelligence tests are useless; and it finds the effect strongest when teachers did not yet know the children, not when they knew them well.",
   "परिच्छेद एक प्रसिद्ध निष्कर्ष बताता है कि शिक्षकों की अपेक्षाओं ने विद्यार्थियों की प्रगति को आकार दिया, और यह कहकर समाप्त होता है कि बाद के अध्ययनों ने प्रभाव को वास्तविक पर प्रायः छोटा पाया। "
   "वह कहता है कि 'खिलने वाले' यादृच्छिक रूप से चुने गए थे, इसलिए वे वास्तव में अधिक योग्य नहीं थे; वह यह नहीं कहता कि बुद्धि परीक्षाएँ बेकार हैं; और वह प्रभाव को तब सबसे बड़ा पाता है जब शिक्षक बच्चों को अभी जानते नहीं थे, तब नहीं जब अच्छी तरह जानते थे।",
   "crux",
   opts=["What teachers expect of pupils can shape their progress, though usually only modestly.",
         "The children labelled as bloomers were in fact abler than the others from the very start.",
         "Intelligence tests are of no use, since their results depend entirely on what teachers think.",
         "Teachers' expectations matter most once they have come to know their pupils very well."],
   opts_hi=["शिक्षकों की अपेक्षाएँ विद्यार्थियों की प्रगति को प्रभावित कर सकती हैं, यद्यपि प्रायः थोड़ा ही।",
            "'खिलने वाले' कहे गए बच्चे शुरू से ही वास्तव में बाक़ियों से अधिक योग्य थे।",
            "बुद्धि परीक्षाएँ किसी काम की नहीं, क्योंकि उनके परिणाम पूरी तरह इस पर निर्भर हैं कि शिक्षक क्या सोचते हैं।",
            "शिक्षकों की अपेक्षाएँ तब सबसे अधिक मायने रखती हैं जब वे अपने विद्यार्थियों को बहुत अच्छी तरह जान चुके हों।"],
   ans=0, pos=2)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Neither is valid. 1: the bloomers were chosen at random, so their larger gains cannot be put down to greater ability at the start -- that is the whole point of choosing them at random. "
   "2: the later studies found the effect real but small; that is not the same as finding that expectations make no difference.",
   "कोई भी वैध नहीं। 1: 'खिलने वाले' यादृच्छिक रूप से चुने गए थे, इसलिए उनकी अधिक प्रगति को शुरुआती अधिक योग्यता से नहीं जोड़ा जा सकता -- यादृच्छिक चुनाव का यही उद्देश्य है। "
   "2: बाद के अध्ययनों ने प्रभाव को वास्तविक पर छोटा पाया; यह इस निष्कर्ष के समान नहीं कि अपेक्षाओं से कोई अंतर नहीं पड़ता।",
   "conclusions",
   st=["The bloomers gained more because they were abler than their classmates to begin with.",
       "Later studies showed that teachers' expectations make no difference to how pupils learn."],
   st_hi=["'खिलने वालों' ने अधिक प्रगति इसलिए की कि वे शुरू से ही अपने सहपाठियों से अधिक योग्य थे।",
          "बाद के अध्ययनों ने दिखाया कि शिक्षकों की अपेक्षाओं से विद्यार्थियों के सीखने पर कोई अंतर नहीं पड़ता।"],
   key=3)

# ------------------------------------------------------------------ P02 Mill's harm principle (3)
p = passage("p02",
  "In On Liberty, published in 1859, John Stuart Mill argued that the only purpose for which power can rightfully be used over a member of a civilised community, against their will, is to prevent harm to others. A person's own good, physical or moral, was not in his view a sufficient reason: people may be argued with, persuaded or warned, but not compelled for their own sake. Mill defended this partly because individuals usually know their own interests best, and partly because a society that allows varied 'experiments of living' learns which ways of life are worth following. "
  "The principle is easier to state than to apply. Almost any act affects others in some way, so much depends on what counts as harm. Mill himself excluded children from the principle, and many laws today -- requiring seat belts, for instance -- protect people from themselves, which strict followers of Mill would reject.",
  "1859 में प्रकाशित ऑन लिबर्टी में जॉन स्टुअर्ट मिल ने तर्क दिया कि किसी सभ्य समाज के सदस्य पर, उसकी इच्छा के विरुद्ध, शक्ति के उचित प्रयोग का एकमात्र उद्देश्य दूसरों को हानि से बचाना है। उनके मत में व्यक्ति का अपना भला, शारीरिक या नैतिक, पर्याप्त कारण नहीं था: लोगों से बहस की जा सकती है, उन्हें समझाया या चेताया जा सकता है, पर उनके अपने भले के लिए उन पर दबाव नहीं डाला जा सकता। मिल ने इसका बचाव कुछ इसलिए किया कि व्यक्ति प्रायः अपने हित सबसे अच्छी तरह जानते हैं, और कुछ इसलिए कि जो समाज जीवन के विविध 'प्रयोगों' की अनुमति देता है, वह सीखता है कि जीने के कौन-से ढंग अपनाने योग्य हैं। "
  "सिद्धांत को कहना लागू करने से आसान है। लगभग हर काम किसी न किसी तरह दूसरों को प्रभावित करता है, इसलिए बहुत कुछ इस पर निर्भर है कि हानि किसे माना जाए। मिल ने स्वयं बच्चों को इस सिद्धांत से बाहर रखा, और आज के बहुत-से क़ानून -- जैसे सीट बेल्ट अनिवार्य करने वाले -- लोगों को स्वयं उनसे बचाते हैं, जिन्हें मिल के कट्टर अनुयायी अस्वीकार करेंगे।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage states Mill's principle -- compulsion only to prevent harm to others -- with his reasons for it, then shows the difficulty of applying it, since so much depends on what counts as harm. "
   "Mill allowed persuasion and warning, so he did not say people must never be advised; the passage does not claim that every modern law follows Mill -- it gives seat-belt laws as ones that do not; and Mill excluded children rather than putting them first.",
   "परिच्छेद मिल का सिद्धांत -- दबाव केवल दूसरों को हानि से बचाने के लिए -- उसके कारणों सहित रखता है, फिर उसे लागू करने की कठिनाई दिखाता है, क्योंकि बहुत कुछ इस पर निर्भर है कि हानि किसे माना जाए। "
   "मिल ने समझाने और चेताने की अनुमति दी, इसलिए उन्होंने यह नहीं कहा कि लोगों को कभी सलाह न दी जाए; परिच्छेद यह दावा नहीं करता कि आज का हर क़ानून मिल के अनुसार है -- वह सीट बेल्ट क़ानूनों को ऐसे क़ानूनों के रूप में देता है जो नहीं हैं; और मिल ने बच्चों को सिद्धांत से बाहर रखा, सबसे आगे नहीं।",
   "crux",
   opts=["Liberty may be limited only to prevent harm to others, a rule easier to state than apply.",
         "People should never be advised or warned about choices that affect only themselves.",
         "Modern laws, such as those on seat belts, are all based on the harm principle that Mill set out.",
         "Mill's principle was meant above all to protect children from the harm they might do to themselves."],
   opts_hi=["स्वतंत्रता केवल दूसरों की हानि रोकने हेतु सीमित हो सकती है; यह नियम कहना आसान, लागू करना कठिन है।",
            "जो चुनाव केवल स्वयं को प्रभावित करते हैं, उनके बारे में लोगों को कभी सलाह या चेतावनी नहीं दी जानी चाहिए।",
            "आज के क़ानून, जैसे सीट बेल्ट वाले, सभी मिल के बताए हानि-सिद्धांत पर आधारित हैं।",
            "मिल का सिद्धांत सबसे बढ़कर बच्चों को उस हानि से बचाने के लिए था जो वे स्वयं को पहुँचा सकते हैं।"],
   ans=0, pos=0)
RQ(p, "Inference", "hard", "mcq",
   "Which one of the following laws would Mill's principle most clearly allow?",
   "मिल का सिद्धांत निम्नलिखित में से किस क़ानून की सबसे स्पष्ट अनुमति देगा?",
   "Driving after drinking puts other road users at risk, so a law punishing it prevents harm to others -- the one ground Mill accepts. "
   "Banning adults from risky sports, from eating unhealthy food, or from spending their own savings as they please would compel people for their own good, which Mill rejects; at most they may be warned or persuaded.",
   "शराब पीकर गाड़ी चलाना सड़क के दूसरे लोगों को जोखिम में डालता है, इसलिए उस पर दंड देने वाला क़ानून दूसरों को हानि से बचाता है -- वही एकमात्र आधार जिसे मिल स्वीकार करते हैं। "
   "वयस्कों पर जोखिम भरे खेलों, अस्वास्थ्यकर भोजन, या अपनी बचत मनचाहे ढंग से ख़र्च करने पर रोक लोगों पर उनके अपने भले के लिए दबाव डालती, जिसे मिल अस्वीकार करते हैं; अधिक से अधिक उन्हें चेताया या समझाया जा सकता है।",
   "a-law-mill-would-allow",
   opts=["A law punishing people who drive after drinking alcohol",
         "A law forbidding adults to take part in dangerous sports such as mountaineering",
         "A law forbidding adults to eat food that is bad for their health",
         "A law forbidding adults to spend their own savings on whatever they please"],
   opts_hi=["शराब पीकर गाड़ी चलाने वालों को दंड देने वाला क़ानून",
            "वयस्कों को पर्वतारोहण जैसे ख़तरनाक खेलों में भाग लेने से रोकने वाला क़ानून",
            "वयस्कों को उनके स्वास्थ्य के लिए हानिकारक भोजन खाने से रोकने वाला क़ानून",
            "वयस्कों को अपनी बचत मनचाही चीज़ों पर ख़र्च करने से रोकने वाला क़ानून"],
   ans=0, pos=3)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Only 2 is valid. Mill says people may be argued with, persuaded or warned, though not compelled for their own sake, so warning someone against a harmful habit fits his view. "
   "1 runs against the principle: a law forbidding adults to eat unhealthy food compels them for their own good, and Mill does not accept a person's own good as a reason for compulsion.",
   "केवल 2 वैध है। मिल कहते हैं कि लोगों से बहस की जा सकती है, उन्हें समझाया या चेताया जा सकता है, यद्यपि उनके अपने भले के लिए दबाव नहीं डाला जा सकता, इसलिए किसी को हानिकारक आदत के विरुद्ध चेताना उनके मत के अनुकूल है। "
   "1 सिद्धांत के विरुद्ध जाता है: वयस्कों को अस्वास्थ्यकर भोजन से रोकने वाला क़ानून उन पर उनके अपने भले के लिए दबाव डालता है, और मिल व्यक्ति के अपने भले को दबाव का कारण नहीं मानते।",
   "conclusions",
   st=["Mill would accept a law forbidding adults to eat unhealthy food, since their poor health may burden others.",
       "On Mill's view, a person may be warned against a harmful habit even though they may not be forced to give it up."],
   st_hi=["मिल वयस्कों को अस्वास्थ्यकर भोजन से रोकने वाला क़ानून स्वीकार करेंगे, क्योंकि उनका ख़राब स्वास्थ्य दूसरों पर बोझ बन सकता है।",
          "मिल के मत में किसी व्यक्ति को हानिकारक आदत के विरुद्ध चेताया जा सकता है, यद्यपि उसे वह आदत छोड़ने के लिए मजबूर नहीं किया जा सकता।"],
   key=1)

# ------------------------------------------------------------------ P03 the Permanent Settlement of 1793 (2)
p = passage("p03",
  "In 1793 Lord Cornwallis introduced the Permanent Settlement in Bengal. The zamindars were recognised as owners of the land, and the revenue each had to pay to the East India Company was fixed for ever. The Company hoped for a steady income it could count on, and expected that landlords secure in their property, and sure that any increase in output would be theirs, would invest in improving the land. "
  "Things turned out differently. The revenue was set so high that many zamindars failed to pay in the early years, and their estates were auctioned. Later, as cultivation spread and prices rose, the fixed demand became light, but the gains went largely to zamindars and a chain of intermediaries below them, while the cultivators, with weak rights, were squeezed. The Company, for its part, could not raise its revenue as the land grew more productive.",
  "1793 में लॉर्ड कॉर्नवालिस ने बंगाल में स्थायी बंदोबस्त लागू किया। ज़मींदारों को भूमि का स्वामी माना गया, और हर एक को ईस्ट इंडिया कंपनी को जो राजस्व देना था, वह सदा के लिए तय कर दिया गया। कंपनी को एक स्थिर आय की आशा थी जिस पर वह भरोसा कर सके, और उसकी अपेक्षा थी कि अपनी संपत्ति के प्रति आश्वस्त, और यह जानते हुए कि उत्पादन की कोई भी वृद्धि उनकी अपनी होगी, ज़मींदार भूमि सुधारने में निवेश करेंगे। "
  "परिणाम अलग निकले। राजस्व इतना ऊँचा तय किया गया कि शुरुआती वर्षों में बहुत-से ज़मींदार भुगतान नहीं कर सके, और उनकी ज़मींदारियाँ नीलाम हुईं। बाद में, जैसे-जैसे खेती फैली और मूल्य बढ़े, तय माँग हल्की हो गई, पर लाभ अधिकतर ज़मींदारों और उनके नीचे बिचौलियों की एक कड़ी को गया, जबकि कमज़ोर अधिकारों वाले काश्तकार पिसते रहे। कंपनी, अपनी ओर से, भूमि के अधिक उपजाऊ होने के साथ अपना राजस्व नहीं बढ़ा सकी।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage sets out what the Permanent Settlement was meant to achieve -- a steady income and improving landlords -- and shows how it turned out: auctions at first, then gains captured by zamindars and intermediaries, squeezed cultivators, and a Company unable to share in rising output. "
   "It says the early demand was too high, not too low; the zamindars were recognised as owners, not stripped of their land; and the gains went to zamindars and intermediaries, not to the cultivators.",
   "परिच्छेद बताता है कि स्थायी बंदोबस्त से क्या पाने की आशा थी -- स्थिर आय और सुधार करने वाले ज़मींदार -- और दिखाता है कि परिणाम क्या रहा: पहले नीलामियाँ, फिर ज़मींदारों और बिचौलियों द्वारा हथियाए गए लाभ, पिसते काश्तकार, और बढ़ते उत्पादन में हिस्सा न पा सकने वाली कंपनी। "
   "वह कहता है कि शुरुआती माँग बहुत ऊँची थी, नीची नहीं; ज़मींदारों को स्वामी माना गया, उनसे भूमि छीनी नहीं गई; और लाभ ज़मींदारों और बिचौलियों को गया, काश्तकारों को नहीं।",
   "crux",
   opts=["The fixed revenue failed its aims, and its gains went to those above the cultivators.",
         "The revenue demand was set so low that the Company soon ran short of the income it needed to govern.",
         "The Settlement took the land away from the zamindars and gave it to the Company.",
         "The cultivators of Bengal were the chief gainers when prices and output rose."],
   opts_hi=["तय राजस्व अपने उद्देश्यों में विफल रहा, और उसके लाभ काश्तकारों के ऊपर वालों को गए।",
            "राजस्व की माँग इतनी कम रखी गई कि कंपनी को शासन चलाने के लिए आवश्यक आय की जल्दी ही कमी पड़ गई।",
            "बंदोबस्त ने ज़मींदारों से भूमि लेकर कंपनी को दे दी।",
            "मूल्य और उत्पादन बढ़ने पर बंगाल के काश्तकार ही मुख्य लाभार्थी रहे।"],
   ans=0, pos=1)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Both are valid. 1: the passage says that as prices rose the fixed demand 'became light' -- a sum fixed in money is worth less as prices climb. "
   "2: many zamindars failed to pay in the early years and lost their estates at auction, which shows the demand was at first too heavy for them.",
   "दोनों वैध हैं। 1: परिच्छेद कहता है कि मूल्य बढ़ने पर तय माँग 'हल्की हो गई' -- पैसे में तय राशि का मूल्य मूल्यों के चढ़ने के साथ घटता है। "
   "2: शुरुआती वर्षों में बहुत-से ज़मींदार भुगतान नहीं कर सके और नीलामी में अपनी ज़मींदारियाँ खो बैठे, जो दिखाता है कि माँग शुरू में उनके लिए बहुत भारी थी।",
   "conclusions",
   st=["A revenue demand fixed in money grows lighter as prices rise.",
       "The early auctions of estates suggest that the revenue demand was at first too heavy."],
   st_hi=["पैसे में तय राजस्व-माँग मूल्य बढ़ने के साथ हल्की होती जाती है।",
          "ज़मींदारियों की शुरुआती नीलामियाँ संकेत देती हैं कि राजस्व-माँग शुरू में बहुत भारी थी।"],
   key=2)

# ------------------------------------------------------------------ P04 Wegener and the drifting continents (2)
p = passage("p04",
  "In 1912 the German scientist Alfred Wegener proposed that the continents had once been joined in a single landmass, which he later called Pangaea, and had since drifted apart. He pointed to the way the coasts of South America and Africa fit together, to matching rocks and fossils of the same land plants and animals on continents now separated by oceans, and to traces of ancient glaciers in regions that are now tropical. "
  "Most geologists rejected the idea for decades. The evidence was striking, but Wegener could not explain what force could push continents through the solid ocean floor, and the forces he suggested were far too weak. Only in the 1960s, when studies of the sea floor showed it spreading outwards from ridges in the middle of the oceans, did a mechanism emerge, and continental drift became part of the theory of plate tectonics.",
  "1912 में जर्मन वैज्ञानिक आल्फ़्रेड वेगनर ने प्रस्ताव रखा कि महाद्वीप कभी एक ही भूखंड में जुड़े थे, जिसे उन्होंने बाद में पैंजिया कहा, और तब से अलग-अलग खिसक गए हैं। उन्होंने दक्षिण अमेरिका और अफ़्रीका के तटों के आपस में बैठने, आज महासागरों से अलग महाद्वीपों पर मिलती-जुलती चट्टानों और एक ही स्थलीय पौधों और जीवों के जीवाश्मों, और आज उष्णकटिबंधीय क्षेत्रों में प्राचीन हिमनदों के चिह्नों की ओर संकेत किया। "
  "अधिकांश भूवैज्ञानिकों ने दशकों तक यह विचार अस्वीकार किया। प्रमाण प्रभावशाली थे, पर वेगनर यह नहीं समझा सके कि कौन-सा बल महाद्वीपों को ठोस महासागरीय तल के बीच से धकेल सकता है, और उनके सुझाए बल बहुत ही कमज़ोर थे। केवल 1960 के दशक में, जब समुद्र-तल के अध्ययनों ने दिखाया कि वह महासागरों के बीच की कटकों से बाहर की ओर फैल रहा है, एक तंत्र सामने आया, और महाद्वीपीय विस्थापन प्लेट विवर्तनिकी के सिद्धांत का भाग बन गया।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "Wegener's evidence was strong, but his idea was rejected for decades because he had no convincing mechanism; it was accepted once sea-floor spreading supplied one. "
   "The passage calls his evidence striking, not weak; it says the idea was rejected, not quickly accepted; and it says the forces he proposed were far too weak, not that he found the right one.",
   "वेगनर के प्रमाण मज़बूत थे, पर उनका विचार दशकों तक अस्वीकार रहा क्योंकि उनके पास कोई विश्वसनीय तंत्र नहीं था; समुद्र-तल के फैलाव ने जब तंत्र दिया, तब उसे स्वीकार किया गया। "
   "परिच्छेद उनके प्रमाणों को प्रभावशाली कहता है, कमज़ोर नहीं; वह कहता है कि विचार अस्वीकार हुआ, जल्दी स्वीकार नहीं; और वह कहता है कि उनके सुझाए बल बहुत कमज़ोर थे, यह नहीं कि उन्होंने सही बल खोज लिया।",
   "crux",
   opts=["Drift was doubted for want of a mechanism, not evidence, until sea-floor studies gave one.",
         "Wegener's evidence for drifting continents was so weak that geologists were right to ignore it.",
         "Geologists accepted Wegener's idea at once because the coasts of two continents fit together.",
         "Wegener correctly identified the force that moves the continents across the surface of the Earth."],
   opts_hi=["विस्थापन प्रमाण की नहीं, तंत्र की कमी से संदिग्ध रहा, जब तक समुद्र-तल ने तंत्र नहीं दिया।",
            "खिसकते महाद्वीपों के लिए वेगनर के प्रमाण इतने कमज़ोर थे कि भूवैज्ञानिकों का उन्हें अनदेखा करना ठीक था।",
            "भूवैज्ञानिकों ने वेगनर का विचार तुरंत स्वीकार कर लिया क्योंकि दो महाद्वीपों के तट आपस में बैठते थे।",
            "वेगनर ने वह बल सही-सही पहचाना जो पृथ्वी की सतह पर महाद्वीपों को खिसकाता है।"],
   ans=0, pos=3)
RQ(p, "Inference", "medium", "mcq",
   "On the passage's account, which one of the following would most likely have won geologists over to Wegener's idea much earlier?",
   "परिच्छेद के अनुसार, निम्नलिखित में से क्या भूवैज्ञानिकों को बहुत पहले वेगनर के विचार की ओर ला सकता था?",
   "The passage says the idea was rejected because Wegener could not explain what force could move continents, and that it was accepted once sea-floor spreading supplied a mechanism. A convincing mechanism, found earlier, is therefore what would most likely have changed minds. "
   "More fossils, more glacier traces or a closer fit of coastlines would add to evidence the passage already calls striking -- evidence that, by itself, did not persuade.",
   "परिच्छेद कहता है कि विचार इसलिए अस्वीकार हुआ कि वेगनर नहीं समझा सके कि कौन-सा बल महाद्वीपों को खिसका सकता है, और कि समुद्र-तल के फैलाव ने जब तंत्र दिया तब उसे स्वीकार किया गया। इसलिए पहले मिला एक विश्वसनीय तंत्र ही सबसे संभवतः मत बदलता। "
   "अधिक जीवाश्म, हिमनदों के अधिक चिह्न या तटों का और सटीक मेल उन प्रमाणों में जुड़ते जिन्हें परिच्छेद पहले ही प्रभावशाली कहता है -- ऐसे प्रमाण जो अपने आप में राज़ी नहीं कर सके।",
   "what-would-have-persuaded-sooner",
   opts=["A force, shown to exist, strong enough to move whole continents",
         "More fossils of the same animal found on two separate continents",
         "Fresh traces of ancient glaciers found in other tropical regions",
         "A still closer match between the coastlines of two continents"],
   opts_hi=["पूरे महाद्वीपों को खिसका सकने वाला एक सिद्ध बल",
            "दो अलग महाद्वीपों पर एक ही जीव के और जीवाश्म",
            "दूसरे उष्णकटिबंधीय क्षेत्रों में प्राचीन हिमनदों के नए चिह्न",
            "दो महाद्वीपों के तटों के बीच और भी सटीक मेल"],
   ans=0, pos=0)

# ------------------------------------------------------------------ P05 Keynes's beauty contest (3)
p = passage("p05",
  "In 1936 the economist John Maynard Keynes compared professional investment to a newspaper competition in which readers had to pick the six prettiest faces from a hundred photographs, the prize going to the reader whose choice came nearest to the average choice of all the competitors. To win, a reader should not pick the faces they personally found prettiest, nor even those they thought most people would find prettiest, but those they expected the others to expect to be most popular. "
  "In the same way, Keynes argued, investors buying shares for a quick profit try to guess not what a company is truly worth but what other investors will soon think it worth. Prices can then drift far from any sober estimate of value, driven by shifts of mood. The comparison does not mean that every investor behaves so: those who buy to hold for many years can ignore the crowd -- though, as Keynes noted, they may look foolish while they wait.",
  "1936 में अर्थशास्त्री जॉन मेनार्ड कीन्स ने पेशेवर निवेश की तुलना एक अख़बार की प्रतियोगिता से की, जिसमें पाठकों को सौ तस्वीरों में से छह सबसे सुंदर चेहरे चुनने थे, और पुरस्कार उस पाठक को मिलना था जिसका चुनाव सभी प्रतियोगियों के औसत चुनाव के सबसे निकट हो। जीतने के लिए पाठक को वे चेहरे नहीं चुनने चाहिए जो उसे स्वयं सबसे सुंदर लगें, न वे भी जिन्हें वह सोचता है कि अधिकांश लोग सबसे सुंदर पाएँगे, बल्कि वे जिनके बारे में उसका अनुमान हो कि दूसरे उन्हें सबसे लोकप्रिय मानेंगे। "
  "कीन्स का तर्क था कि इसी तरह जल्दी लाभ के लिए शेयर ख़रीदने वाले निवेशक यह अनुमान लगाने का प्रयास करते हैं कि कोई कंपनी वास्तव में कितने की है, यह नहीं, बल्कि यह कि दूसरे निवेशक जल्दी ही उसे कितने का मानेंगे। तब मूल्य किसी भी संयत आकलन से बहुत दूर बह सकते हैं, मनोदशा के बदलावों से प्रेरित होकर। इस तुलना का अर्थ यह नहीं कि हर निवेशक ऐसा ही करता है: जो बरसों तक रखने के लिए ख़रीदते हैं वे भीड़ की अनदेखी कर सकते हैं -- यद्यपि, जैसा कीन्स ने कहा, प्रतीक्षा करते समय वे मूर्ख दिख सकते हैं।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "Keynes's point is that short-term investors, like the contest's players, guess what others will think rather than what something is worth, so prices can stray from value; the passage adds that long-term investors can stand apart. "
   "It says prices can drift far from value, so it does not claim they always match it; it says not every investor behaves so; and it is about markets, not about judging beauty.",
   "कीन्स की बात यह है कि अल्पकालिक निवेशक, प्रतियोगिता के खिलाड़ियों की तरह, यह अनुमान लगाते हैं कि दूसरे क्या सोचेंगे, यह नहीं कि किसी चीज़ का मूल्य क्या है, इसलिए मूल्य वास्तविक मूल्य से भटक सकते हैं; परिच्छेद जोड़ता है कि दीर्घकालिक निवेशक अलग रह सकते हैं। "
   "वह कहता है कि मूल्य वास्तविक मूल्य से बहुत दूर बह सकते हैं, इसलिए वह यह दावा नहीं करता कि वे सदा मेल खाते हैं; वह कहता है कि हर निवेशक ऐसा नहीं करता; और वह बाज़ारों के बारे में है, सुंदरता आँकने के बारे में नहीं।",
   "crux",
   opts=["Short-term investors guess others' views, not true worth, so prices can stray from value.",
         "Share prices always settle at what companies are truly worth, whatever investors happen to feel.",
         "Every investor, short-term or long-term, is bound to follow the mood of the crowd.",
         "The best way to judge a face is to pick the one that most other people will like."],
   opts_hi=["अल्पकालिक निवेशक मूल्य नहीं, दूसरों की सोच भाँपते हैं, इसलिए क़ीमतें मूल्य से भटक सकती हैं।",
            "निवेशक जो भी महसूस करें, शेयरों के दाम सदा उसी पर टिकते हैं जितनी कंपनियाँ वास्तव में मूल्यवान हैं।",
            "हर निवेशक, अल्पकालिक हो या दीर्घकालिक, भीड़ की मनोदशा का अनुसरण करने को बाध्य है।",
            "किसी चेहरे को आँकने का सबसे अच्छा ढंग वह चुनना है जो अधिकांश दूसरे लोगों को पसंद आए।"],
   ans=0, pos=2)
RQ(p, "Inference", "hard", "mcq",
   "A reader in the competition personally finds face 12 the prettiest, but expects that most competitors will expect face 40 to be the popular choice. On the passage's reasoning, which of the two faces should the reader prefer, in order to win?",
   "प्रतियोगिता में एक पाठक को स्वयं चेहरा 12 सबसे सुंदर लगता है, पर उसका अनुमान है कि अधिकांश प्रतियोगी चेहरा 40 को लोकप्रिय चुनाव मानेंगे। परिच्छेद के तर्क के अनुसार, जीतने के लिए पाठक को दोनों में से किस चेहरे को प्राथमिकता देनी चाहिए?",
   "The prize goes to whoever comes nearest the average choice, and the passage says a winning reader picks what they expect the others to expect to be popular -- here face 40. "
   "Face 12 is the reader's own taste, which the passage says a winner should set aside; a face that nobody is likely to choose cannot be near the average; and the two views do not cancel out -- the prize rewards matching the crowd's expectations, not the reader's taste.",
   "पुरस्कार उसे मिलता है जो औसत चुनाव के सबसे निकट हो, और परिच्छेद कहता है कि जीतने वाला पाठक वह चुनता है जिसके बारे में उसका अनुमान हो कि दूसरे उसे लोकप्रिय मानेंगे -- यहाँ चेहरा 40। "
   "चेहरा 12 पाठक की अपनी रुचि है, जिसे परिच्छेद के अनुसार विजेता को अलग रखना चाहिए; जिस चेहरे को किसी के चुनने की संभावना न हो, वह औसत के निकट नहीं हो सकता; और दोनों मत एक-दूसरे को काटते नहीं -- पुरस्कार भीड़ की अपेक्षाओं से मेल खाने का है, पाठक की रुचि का नहीं।",
   "which-face-to-pick",
   opts=["Face 40, which the reader expects the others to expect to be popular",
         "Face 12, which the reader personally finds the prettiest of all",
         "A face that neither the reader nor the others are likely to choose",
         "Neither, since the reader's own taste and the crowd's expectation cancel each other out"],
   opts_hi=["चेहरा 40, जिसके बारे में पाठक का अनुमान है कि दूसरे उसे लोकप्रिय मानेंगे",
            "चेहरा 12, जो पाठक को स्वयं सबसे सुंदर लगता है",
            "ऐसा चेहरा जिसे न पाठक चुनेगा न दूसरे चुनेंगे",
            "कोई नहीं, क्योंकि पाठक की अपनी रुचि और भीड़ की अपेक्षा एक-दूसरे को काट देती हैं"],
   ans=0, pos=1)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Only 1 is valid. In the contest the prize goes to whoever comes nearest the average choice, so a reader's own sense of beauty counts for little; the passage says the winner should not pick the faces they personally find prettiest. "
   "2 reverses Keynes: he argued that prices can drift far from any sober estimate of what companies are worth.",
   "केवल 1 वैध है। प्रतियोगिता में पुरस्कार उसे मिलता है जो औसत चुनाव के सबसे निकट हो, इसलिए पाठक की अपनी सौंदर्य-दृष्टि का बहुत कम महत्त्व है; परिच्छेद कहता है कि विजेता को वे चेहरे नहीं चुनने चाहिए जो उसे स्वयं सबसे सुंदर लगें। "
   "2 कीन्स को उलट देता है: उन्होंने तर्क दिया कि मूल्य कंपनियों के वास्तविक मूल्य के किसी भी संयत आकलन से बहुत दूर बह सकते हैं।",
   "conclusions",
   st=["In the competition, a reader's own taste is of little help in winning the prize.",
       "Keynes held that share prices always reflect what companies are truly worth."],
   st_hi=["प्रतियोगिता में पुरस्कार जीतने के लिए पाठक की अपनी रुचि बहुत कम सहायक है।",
          "कीन्स का मत था कि शेयरों के दाम सदा यह दर्शाते हैं कि कंपनियाँ वास्तव में कितनी मूल्यवान हैं।"],
   key=0)

# ------------------------------------------------------------------ P06 the stepwells of western India (2)
p = passage("p06",
  "For more than a thousand years, people in the dry regions of western India built stepwells: deep shafts that reach down to the water below the ground, lined with long flights of steps so that people could reach the water however far it had sunk in the dry months. The finest, such as the Rani ki Vav at Patan in Gujarat, built in the eleventh century, are richly carved, with galleries where travellers could rest in the cool. Stepwells were also places where people met, and their upkeep was often a shared duty. "
  "Under colonial rule, piped water and hand pumps came to be preferred, many stepwells were judged unhygienic, and many were filled in or left to decay. Some are now being cleaned and revived, as falling groundwater makes their old purpose -- holding water and reaching it through the dry season -- valuable again.",
  "एक हज़ार से अधिक वर्षों तक पश्चिमी भारत के शुष्क क्षेत्रों में लोगों ने बावड़ियाँ बनाईं: भूमि के नीचे के पानी तक पहुँचने वाले गहरे कुएँ, जिनमें सीढ़ियों की लंबी कतारें होती थीं ताकि सूखे महीनों में पानी कितना भी नीचे चला जाए, लोग उस तक पहुँच सकें। सबसे भव्य बावड़ियाँ, जैसे गुजरात के पाटन की ग्यारहवीं सदी में बनी रानी की वाव, बारीक नक़्क़ाशी वाली हैं, जिनमें ऐसे गलियारे हैं जहाँ यात्री ठंडक में विश्राम कर सकते थे। बावड़ियाँ लोगों के मिलने की जगहें भी थीं, और उनकी देखभाल प्रायः एक साझा कर्तव्य होती थी। "
  "औपनिवेशिक शासन में नल के पानी और हैंडपंपों को प्राथमिकता मिली, बहुत-सी बावड़ियों को अस्वच्छ माना गया, और बहुत-सी पाट दी गईं या जर्जर होने को छोड़ दी गईं। कुछ को अब साफ़ करके फिर से जीवित किया जा रहा है, क्योंकि गिरता भूजल उनके पुराने उद्देश्य -- सूखे मौसम भर पानी रखना और उस तक पहुँचना -- को फिर मूल्यवान बना रहा है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage describes stepwells as practical, social and beautiful structures, tells how they fell out of use under colonial rule, and ends with their revival as groundwater falls. "
   "It does not say every stepwell is now in use again -- only some are being revived; it gives falling groundwater, not tourism, as the reason; and it presents piped water as what replaced them, not as something to be abandoned.",
   "परिच्छेद बावड़ियों को उपयोगी, सामाजिक और सुंदर संरचनाओं के रूप में वर्णित करता है, बताता है कि औपनिवेशिक शासन में उनका उपयोग कैसे छूटा, और भूजल गिरने पर उनके पुनरुद्धार पर समाप्त होता है। "
   "वह यह नहीं कहता कि हर बावड़ी फिर उपयोग में है -- केवल कुछ का पुनरुद्धार हो रहा है; वह कारण गिरता भूजल बताता है, पर्यटन नहीं; और वह नल के पानी को उन्हें बदलने वाली चीज़ बताता है, छोड़ने योग्य चीज़ नहीं।",
   "crux",
   opts=["Neglected stepwells are regaining value as stores of scarce water.",
         "Every stepwell in western India is now back in daily use for drinking water.",
         "Stepwells are being revived mainly so that they can attract more tourists.",
         "Piped water should be given up in dry regions in favour of the old stepwells."],
   opts_hi=["उपेक्षित बावड़ियाँ दुर्लभ पानी के भंडार के रूप में फिर मूल्यवान हो रही हैं।",
            "पश्चिमी भारत की हर बावड़ी अब पीने के पानी के लिए फिर से रोज़ उपयोग में है।",
            "बावड़ियों का पुनरुद्धार मुख्यतः इसलिए हो रहा है कि वे और पर्यटक आकर्षित कर सकें।",
            "शुष्क क्षेत्रों में पुरानी बावड़ियों के पक्ष में नल का पानी छोड़ देना चाहिए।"],
   ans=0, pos=0)
RQ(p, "Specific Detail", "easy", "mcq",
   "According to the passage, why were stepwells built with long flights of steps?",
   "परिच्छेद के अनुसार, बावड़ियाँ सीढ़ियों की लंबी कतारों के साथ क्यों बनाई गईं?",
   "The passage says the steps let people reach the water however far it had sunk in the dry months. "
   "It mentions carving and galleries, but not that the steps were for decoration; it says nothing of steps for storing grain or for keeping animals away.",
   "परिच्छेद कहता है कि सीढ़ियों से लोग सूखे महीनों में पानी तक पहुँच सकते थे, वह कितना भी नीचे चला गया हो। "
   "वह नक़्क़ाशी और गलियारों का उल्लेख करता है, पर यह नहीं कहता कि सीढ़ियाँ सजावट के लिए थीं; वह अनाज रखने या पशुओं को दूर रखने के लिए सीढ़ियों के बारे में कुछ नहीं कहता।",
   "why-the-steps",
   opts=["To reach the water however low it fell in the dry months",
         "So that the carvings on the walls could be seen from close up",
         "So that grain could be stored on the steps above the water",
         "So that animals could not come down to drink from the water"],
   opts_hi=["सूखे महीनों में नीचे गए पानी तक पहुँचने के लिए",
            "ताकि दीवारों की नक़्क़ाशी पास से देखी जा सके",
            "ताकि पानी के ऊपर की सीढ़ियों पर अनाज रखा जा सके",
            "ताकि पशु पानी पीने नीचे न आ सकें"],
   ans=0, pos=2)

# ------------------------------------------------------------------ P07 Project Tiger (2)
p = passage("p07",
  "When India launched Project Tiger in 1973, tigers had been hunted and their forests cleared for decades. The project set aside reserves in which a core area was kept free of human use, with a buffer zone around it. Tiger numbers recovered in many reserves, and national estimates based on camera traps have risen in recent surveys. "
  "The approach has had costs, however. Creating some reserves meant moving villages out of the forest, not always with fair compensation; and as tiger numbers grow, more tigers wander out of small, isolated reserves into farmland, where conflict with people follows. Many conservationists now argue that the future lies less in more fencing than in keeping corridors of forest open between reserves, and in giving the people who live beside tigers a stake in their survival.",
  "जब भारत ने 1973 में प्रोजेक्ट टाइगर शुरू किया, तब तक दशकों से बाघों का शिकार हो रहा था और उनके जंगल कट रहे थे। परियोजना ने ऐसे अभयारण्य बनाए जिनमें एक कोर क्षेत्र को मानव उपयोग से मुक्त रखा गया, और उसके चारों ओर एक बफ़र क्षेत्र। बहुत-से अभयारण्यों में बाघों की संख्या फिर बढ़ी, और कैमरा ट्रैप पर आधारित राष्ट्रीय अनुमान हाल के सर्वेक्षणों में बढ़े हैं। "
  "पर इस तरीक़े की कुछ लागतें भी रही हैं। कुछ अभयारण्य बनाने के लिए गाँवों को जंगल से बाहर बसाना पड़ा, सदा उचित मुआवज़े के साथ नहीं; और जैसे-जैसे बाघों की संख्या बढ़ती है, अधिक बाघ छोटे, अलग-थलग अभयारण्यों से निकलकर खेतों में आ जाते हैं, जहाँ लोगों से टकराव होता है। बहुत-से संरक्षणवादी अब तर्क देते हैं कि भविष्य और बाड़ लगाने में कम, और अभयारण्यों के बीच जंगल के गलियारे खुले रखने तथा बाघों के पास रहने वाले लोगों को उनके बचे रहने में हिस्सेदार बनाने में अधिक है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage credits Project Tiger with a recovery in tiger numbers, sets out its costs to people, and ends with the argument that the next step is corridors and a stake for local people rather than more fencing. "
   "It reports a recovery, so it does not say the project failed; it argues against more fencing, not for it; and it says villages were moved, sometimes unfairly -- it does not call for moving all of them.",
   "परिच्छेद बाघों की संख्या में सुधार का श्रेय प्रोजेक्ट टाइगर को देता है, लोगों पर उसकी लागतें बताता है, और इस तर्क पर समाप्त होता है कि अगला क़दम और बाड़ नहीं, बल्कि गलियारे और स्थानीय लोगों की हिस्सेदारी है। "
   "वह सुधार की बात करता है, इसलिए यह नहीं कहता कि परियोजना विफल रही; वह और बाड़ के पक्ष में नहीं, उसके विरुद्ध तर्क देता है; और वह कहता है कि गाँव बसाए गए, कभी-कभी अनुचित ढंग से -- वह सबको हटाने की माँग नहीं करता।",
   "crux",
   opts=["Tigers recovered, but lasting success needs corridors and local goodwill.",
         "Project Tiger has failed, since tiger numbers have kept falling in every reserve.",
         "The best way to protect tigers in future is to fence every reserve more strongly.",
         "All villages near tiger reserves should be moved out so that conflict ends."],
   opts_hi=["बाघ बढ़े, पर स्थायी सफलता के लिए गलियारे और स्थानीय सहयोग चाहिए।",
            "प्रोजेक्ट टाइगर विफल रहा है, क्योंकि हर अभयारण्य में बाघों की संख्या घटती रही है।",
            "भविष्य में बाघों की रक्षा का सबसे अच्छा ढंग हर अभयारण्य की और मज़बूत बाड़बंदी है।",
            "बाघ अभयारण्यों के पास के सभी गाँवों को हटा देना चाहिए ताकि टकराव समाप्त हो।"],
   ans=0, pos=3)
RQ(p, "Inference", "hard", "mcq",
   "Which one of the following does the passage present as, in part, a result of the project's own success?",
   "परिच्छेद निम्नलिखित में से किसे आंशिक रूप से परियोजना की अपनी सफलता का परिणाम बताता है?",
   "The passage says that as tiger numbers grow, more tigers wander out of small, isolated reserves into farmland, where conflict follows -- a problem that the recovery itself helps to create. "
   "The hunting and forest clearing came before the project; moving villages was a cost of creating reserves, not of rising numbers; and camera-trap surveys are how numbers are counted, not a result of the recovery.",
   "परिच्छेद कहता है कि जैसे-जैसे बाघों की संख्या बढ़ती है, अधिक बाघ छोटे, अलग-थलग अभयारण्यों से निकलकर खेतों में आते हैं, जहाँ टकराव होता है -- एक समस्या जिसे स्वयं सुधार ही पैदा करने में भूमिका निभाता है। "
   "शिकार और जंगल कटना परियोजना से पहले के थे; गाँवों को हटाना अभयारण्य बनाने की लागत थी, बढ़ती संख्या की नहीं; और कैमरा ट्रैप सर्वेक्षण संख्या गिनने का ढंग है, सुधार का परिणाम नहीं।",
   "a-problem-that-success-creates",
   opts=["More tigers straying from small reserves into farmland",
         "The hunting of tigers and the clearing of their forests",
         "The moving of villages out of the forest to create reserves",
         "The use of camera traps to estimate the number of tigers"],
   opts_hi=["छोटे अभयारण्यों से अधिक बाघों का खेतों में भटक आना",
            "बाघों का शिकार और उनके जंगलों का कटना",
            "अभयारण्य बनाने के लिए गाँवों को जंगल से बाहर बसाना",
            "बाघों की संख्या का अनुमान लगाने के लिए कैमरा ट्रैप का उपयोग"],
   ans=0, pos=0)

# ------------------------------------------------------------------ P08 the Right to Information Act (3)
p = passage("p08",
  "The Right to Information Act, 2005 lets any citizen of India ask a public authority for information it holds, and requires a reply within thirty days, or within forty-eight hours where a person's life or liberty is at stake. Officials who refuse without good reason can be fined, and appeals go to information commissions. Before the Act, official information was largely secret unless there was a reason to release it; after it, disclosure became the rule and secrecy the exception that has to be justified. Citizens have used the Act to trace ration cards, pensions and the spending of village funds, and to expose wrongdoing at high levels. "
  "The Act has limits. Information whose release would harm national security, or would invade privacy without any public interest, can be withheld; many requests go unanswered or are answered late; commissions face long backlogs; and some of those who have used the Act to expose wrongdoing have been threatened or attacked.",
  "सूचना का अधिकार अधिनियम, 2005 भारत के किसी भी नागरिक को किसी लोक प्राधिकरण से उसके पास उपलब्ध सूचना माँगने देता है, और तीस दिनों के भीतर, या जहाँ किसी व्यक्ति के जीवन या स्वतंत्रता का प्रश्न हो वहाँ अड़तालीस घंटों के भीतर, उत्तर देना अनिवार्य करता है। बिना उचित कारण इनकार करने वाले अधिकारियों पर जुर्माना लग सकता है, और अपीलें सूचना आयोगों में जाती हैं। अधिनियम से पहले सरकारी सूचना प्रायः तब तक गोपनीय रहती थी जब तक उसे जारी करने का कोई कारण न हो; उसके बाद प्रकटीकरण नियम बन गया और गोपनीयता ऐसा अपवाद जिसका औचित्य बताना पड़ता है। नागरिकों ने अधिनियम का उपयोग राशन कार्डों, पेंशनों और ग्राम निधियों के ख़र्च का पता लगाने, और ऊँचे स्तरों पर अनियमितताएँ उजागर करने में किया है। "
  "अधिनियम की सीमाएँ हैं। जिस सूचना के जारी होने से राष्ट्रीय सुरक्षा को हानि हो, या जो बिना किसी जनहित के निजता में दख़ल दे, उसे रोका जा सकता है; बहुत-से अनुरोधों का उत्तर नहीं आता या देर से आता है; आयोगों में लंबित मामलों का अंबार है; और अनियमितताएँ उजागर करने के लिए अधिनियम का उपयोग करने वाले कुछ लोगों को धमकाया गया है या उन पर हमले हुए हैं।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage shows how the Act reversed the default from secrecy to disclosure and has been put to real use, and then sets out its limits in exemptions, delays, backlogs and danger to users. "
   "It says some information can be withheld, so not all information must be released; it describes real gains, so it does not call the Act useless; and it says requests are often answered late, not always on time.",
   "परिच्छेद दिखाता है कि अधिनियम ने डिफ़ॉल्ट को गोपनीयता से प्रकटीकरण में कैसे बदला और उसका वास्तविक उपयोग हुआ है, फिर छूटों, देरी, लंबित मामलों और उपयोगकर्ताओं के ख़तरे के रूप में उसकी सीमाएँ बताता है। "
   "वह कहता है कि कुछ सूचना रोकी जा सकती है, इसलिए सारी सूचना जारी करना अनिवार्य नहीं; वह वास्तविक उपलब्धियाँ बताता है, इसलिए अधिनियम को बेकार नहीं कहता; और वह कहता है कि अनुरोधों का उत्तर प्रायः देर से आता है, सदा समय पर नहीं।",
   "crux",
   opts=["The Act made openness the rule and served citizens, though practice weakens it.",
         "Under the Act every piece of official information must be released to anyone who asks for it.",
         "The Act has proved useless, since requests are usually ignored by public officials.",
         "Requests under the Act are now always answered within thirty days, as the law requires."],
   opts_hi=["अधिनियम ने खुलेपन को नियम बनाया और काम आया, यद्यपि व्यवहार में कमज़ोर है।",
            "अधिनियम के तहत हर सरकारी सूचना माँगने वाले किसी भी व्यक्ति को जारी करनी होगी।",
            "अधिनियम बेकार सिद्ध हुआ है, क्योंकि सरकारी अधिकारी प्रायः अनुरोधों की अनदेखी करते हैं।",
            "अधिनियम के तहत अनुरोधों का उत्तर अब सदा तीस दिनों के भीतर आता है, जैसा क़ानून कहता है।"],
   ans=0, pos=2)
RQ(p, "Specific Detail", "medium", "mcq",
   "According to the passage, how soon must a reply be given when a person's life or liberty is at stake?",
   "परिच्छेद के अनुसार, जब किसी व्यक्ति के जीवन या स्वतंत्रता का प्रश्न हो, तो उत्तर कितनी जल्दी देना होता है?",
   "The passage says forty-eight hours where a person's life or liberty is at stake. "
   "Thirty days is the ordinary limit; the passage mentions no seven-day limit and no limit of twenty-four hours.",
   "परिच्छेद कहता है कि जहाँ किसी व्यक्ति के जीवन या स्वतंत्रता का प्रश्न हो, वहाँ अड़तालीस घंटे। "
   "तीस दिन सामान्य सीमा है; परिच्छेद सात दिन या चौबीस घंटे की किसी सीमा का उल्लेख नहीं करता।",
   "the-urgent-time-limit",
   opts=["Within 48 hours", "Within 24 hours", "Within 7 days", "Within 30 days"],
   opts_hi=["48 घंटों के भीतर", "24 घंटों के भीतर", "7 दिनों के भीतर", "30 दिनों के भीतर"],
   ans=0, pos=1)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Both are valid. 1: before the Act information was secret unless there was a reason to release it; after it, secrecy became 'the exception that has to be justified' -- so the burden of giving reasons moved from the person asking to the official refusing. "
   "2: the passage says many requests go unanswered or are answered late, so the Act's time limits do not by themselves ensure timely replies.",
   "दोनों वैध हैं। 1: अधिनियम से पहले सूचना तब तक गोपनीय थी जब तक उसे जारी करने का कोई कारण न हो; उसके बाद गोपनीयता 'ऐसा अपवाद जिसका औचित्य बताना पड़ता है' बन गई -- इसलिए कारण बताने का भार माँगने वाले से हटकर इनकार करने वाले अधिकारी पर आ गया। "
   "2: परिच्छेद कहता है कि बहुत-से अनुरोधों का उत्तर नहीं आता या देर से आता है, इसलिए अधिनियम की समय-सीमाएँ अपने आप समय पर उत्तर सुनिश्चित नहीं करतीं।",
   "conclusions",
   st=["The Act moved the burden of giving reasons from the person asking for information to the official refusing it.",
       "The time limits in the Act do not by themselves ensure that every request is answered on time."],
   st_hi=["अधिनियम ने कारण बताने का भार सूचना माँगने वाले से हटाकर उसे देने से इनकार करने वाले अधिकारी पर डाल दिया।",
          "अधिनियम की समय-सीमाएँ अपने आप यह सुनिश्चित नहीं करतीं कि हर अनुरोध का उत्तर समय पर आए।"],
   key=2)

# ------------------------------------------------------------------ P09 Florence Nightingale's diagrams (2)
p = passage("p09",
  "During the Crimean War, Florence Nightingale found that far more British soldiers in the army hospitals were dying of diseases such as typhus, typhoid and dysentery than of their wounds. Back in Britain she worked with the statistician William Farr to analyse the army's records, and in 1858 presented them in diagrams of her own design: wedge-shaped charts in which the area of each slice showed the deaths in a month from each cause. "
  "The charts made plain, even to readers who would never study a table of figures, that most of the deaths could have been prevented, and they helped persuade the government to improve sanitation in military hospitals and barracks. Nightingale was not, however, a lone genius who changed policy with a picture: her charts worked because she also had the data, powerful allies and years of persistence.",
  "क्रीमिया युद्ध के दौरान फ़्लोरेंस नाइटिंगेल ने पाया कि सेना के अस्पतालों में कहीं अधिक ब्रिटिश सैनिक अपने घावों से नहीं, बल्कि टाइफ़स, टाइफ़ाइड और पेचिश जैसे रोगों से मर रहे थे। ब्रिटेन लौटकर उन्होंने सांख्यिकीविद विलियम फ़ार के साथ सेना के अभिलेखों का विश्लेषण किया, और 1858 में उन्हें अपने बनाए आरेखों में प्रस्तुत किया: फाँक जैसे खंडों वाले चार्ट, जिनमें हर फाँक का क्षेत्रफल हर कारण से एक महीने में हुई मौतें दिखाता था। "
  "चार्टों ने उन पाठकों के सामने भी, जो आँकड़ों की तालिका कभी न पढ़ते, यह स्पष्ट कर दिया कि अधिकांश मौतें रोकी जा सकती थीं, और उन्होंने सरकार को सैन्य अस्पतालों और बैरकों में स्वच्छता सुधारने के लिए राज़ी करने में मदद की। पर नाइटिंगेल कोई अकेली प्रतिभा नहीं थीं जिन्होंने एक चित्र से नीति बदल दी: उनके चार्ट इसलिए असरदार रहे कि उनके पास आँकड़े, प्रभावशाली सहयोगी और वर्षों की लगन भी थी।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage shows how Nightingale's diagrams made the evidence of preventable deaths plain and helped win sanitary reform, while insisting that the charts worked alongside data, allies and persistence. "
   "It credits the charts with helping, so it does not call them useless; it explicitly denies that a picture alone changed policy; and it says most deaths were from disease, not wounds.",
   "परिच्छेद दिखाता है कि नाइटिंगेल के आरेखों ने रोकी जा सकने वाली मौतों के प्रमाण को कैसे स्पष्ट किया और स्वच्छता सुधार दिलाने में मदद की, साथ ही इस पर ज़ोर देता है कि चार्ट आँकड़ों, सहयोगियों और लगन के साथ मिलकर असरदार रहे। "
   "वह चार्टों को मदद का श्रेय देता है, इसलिए उन्हें बेकार नहीं कहता; वह स्पष्ट नकारता है कि केवल एक चित्र ने नीति बदली; और वह कहता है कि अधिकांश मौतें रोगों से हुईं, घावों से नहीं।",
   "crux",
   opts=["Clear diagrams helped turn evidence into reform, but only with data, allies and persistence.",
         "Nightingale's diagrams changed government policy on their own, without any other support.",
         "Charts are of little use, since officials make decisions only by studying tables of figures.",
         "Most British soldiers in the Crimean War died of their wounds rather than of disease."],
   opts_hi=["स्पष्ट आरेखों ने प्रमाण को सुधार में बदला, पर आँकड़ों, सहयोगियों और लगन के साथ।",
            "नाइटिंगेल के आरेखों ने अपने आप, बिना किसी और सहायता के, सरकार की नीति बदल दी।",
            "चार्ट बहुत कम उपयोगी हैं, क्योंकि अधिकारी केवल आँकड़ों की तालिकाएँ पढ़कर निर्णय लेते हैं।",
            "क्रीमिया युद्ध में अधिकांश ब्रिटिश सैनिक रोगों से नहीं, अपने घावों से मरे।"],
   ans=0, pos=0)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Neither is valid. 1: the last sentence denies exactly this -- the charts worked because Nightingale also had the data, powerful allies and years of persistence. "
   "2: the passage says the area of each slice showed the deaths, not its length.",
   "कोई भी वैध नहीं। 1: अंतिम वाक्य ठीक इसी को नकारता है -- चार्ट इसलिए असरदार रहे कि नाइटिंगेल के पास आँकड़े, प्रभावशाली सहयोगी और वर्षों की लगन भी थी। "
   "2: परिच्छेद कहता है कि हर फाँक का क्षेत्रफल मौतें दिखाता था, उसकी लंबाई नहीं।",
   "conclusions",
   st=["The passage shows that Nightingale's diagrams were by themselves enough to change government policy.",
       "In Nightingale's charts, the length of each slice showed the number of deaths."],
   st_hi=["परिच्छेद दिखाता है कि नाइटिंगेल के आरेख सरकार की नीति बदलने के लिए अपने आप में पर्याप्त थे।",
          "नाइटिंगेल के चार्टों में हर फाँक की लंबाई मौतों की संख्या दिखाती थी।"],
   key=3)

# ------------------------------------------------------------------ P10 the rise in test scores named after James Flynn (2)
p = passage("p10",
  "Through the twentieth century, average scores on intelligence tests rose steadily in country after country -- by roughly three points a decade, so that the tests had to be made harder every so often to keep the average at 100. The trend is named after the researcher James Flynn, who documented it in the 1980s. The rise was far too fast to be genetic. Better nutrition and health, more and longer schooling, smaller families and a world full of abstract symbols and categories have all been suggested as causes, and they may have worked together. "
  "Flynn himself argued that people had not become cleverer in every sense, but more practised at the kinds of abstract thinking the tests reward. In some rich countries the rise has slowed or even reversed since the 1990s, which suggests that whatever drove it has limits.",
  "बीसवीं सदी भर बुद्धि परीक्षाओं के औसत अंक एक के बाद एक देश में लगातार बढ़े -- मोटे तौर पर प्रति दशक तीन अंक, जिससे औसत को 100 पर रखने के लिए परीक्षाओं को समय-समय पर कठिन करना पड़ा। इस प्रवृत्ति का नाम शोधकर्ता जेम्स फ़्लिन के नाम पर है, जिन्होंने 1980 के दशक में इसे दर्ज किया। यह बढ़त आनुवंशिक होने के लिए बहुत तेज़ थी। बेहतर पोषण और स्वास्थ्य, अधिक और लंबी स्कूली शिक्षा, छोटे परिवार और अमूर्त प्रतीकों तथा श्रेणियों से भरी दुनिया -- सभी को कारण के रूप में सुझाया गया है, और हो सकता है इन्होंने मिलकर काम किया हो। "
  "फ़्लिन का अपना तर्क था कि लोग हर अर्थ में अधिक बुद्धिमान नहीं हुए, बल्कि उस प्रकार की अमूर्त सोच में अधिक अभ्यस्त हुए जिसे परीक्षाएँ पुरस्कृत करती हैं। कुछ धनी देशों में 1990 के दशक से यह बढ़त धीमी पड़ी है या उलट भी गई है, जो संकेत देता है कि जो भी इसे चला रहा था उसकी सीमाएँ हैं।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage describes a large rise in test scores, rules out genes, lists possible environmental causes, and adds Flynn's view that the rise reflects practice at abstract thinking rather than cleverness in every sense -- noting that it has stalled in some places. "
   "It says the rise was too fast to be genetic; it does not say people became cleverer in every way -- Flynn denied that; and it says the rise has slowed or reversed in some countries, so it has not continued everywhere.",
   "परिच्छेद परीक्षा-अंकों में बड़ी बढ़त का वर्णन करता है, आनुवंशिकता को अलग करता है, संभावित परिवेशी कारण गिनाता है, और फ़्लिन का मत जोड़ता है कि बढ़त हर अर्थ में बुद्धिमत्ता के बजाय अमूर्त सोच के अभ्यास को दर्शाती है -- यह भी कि कुछ जगहों पर यह रुक गई है। "
   "वह कहता है कि बढ़त आनुवंशिक होने के लिए बहुत तेज़ थी; वह यह नहीं कहता कि लोग हर तरह से अधिक बुद्धिमान हुए -- फ़्लिन ने इसे नकारा; और वह कहता है कि कुछ देशों में बढ़त धीमी पड़ी या उलटी, इसलिए वह हर जगह जारी नहीं रही।",
   "crux",
   opts=["Scores rose for reasons other than genes, reflecting practice more than cleverness.",
         "Test scores rose because the genes of whole populations changed within a few generations.",
         "People in the twentieth century became cleverer in every sense than their grandparents were.",
         "The rise in test scores has continued at the same pace in every country up to the present."],
   opts_hi=["अंक आनुवंशिकता के अलावा कारणों से बढ़े, जो बुद्धिमत्ता से अधिक अभ्यास दर्शाते हैं।",
            "परीक्षा-अंक इसलिए बढ़े कि कुछ ही पीढ़ियों के भीतर पूरी की पूरी आबादी के जीन बदल गए।",
            "बीसवीं सदी के लोग अपने दादा-दादी से हर अर्थ में अधिक बुद्धिमान हो गए।",
            "परीक्षा-अंकों की बढ़त आज तक हर देश में उसी गति से जारी है।"],
   ans=0, pos=3)
RQ(p, "Inference", "hard", "mcq",
   "Which one of the following findings would best fit Flynn's own explanation of the rise?",
   "निम्नलिखित में से कौन-सा निष्कर्ष बढ़त की फ़्लिन की अपनी व्याख्या से सबसे अच्छी तरह मेल खाएगा?",
   "Flynn argued that people had become more practised at the abstract thinking the tests reward, not cleverer in every sense. That predicts the largest gains on tests of abstract reasoning, with little change in skills such as vocabulary and arithmetic. "
   "Equal gains everywhere would suggest a general rise in cleverness; gains largest in arithmetic and vocabulary point away from abstract thinking; and a rise only among children of tall parents would suggest a genetic or physical cause, which the passage rules out.",
   "फ़्लिन का तर्क था कि लोग परीक्षाओं द्वारा पुरस्कृत अमूर्त सोच में अधिक अभ्यस्त हुए, हर अर्थ में अधिक बुद्धिमान नहीं। इससे यह अपेक्षा बनती है कि सबसे अधिक बढ़त अमूर्त तर्क की परीक्षाओं में हो, और शब्दावली तथा अंकगणित जैसे कौशलों में बहुत कम बदलाव हो। "
   "हर जगह बराबर बढ़त बुद्धिमत्ता में सामान्य वृद्धि का संकेत देती; अंकगणित और शब्दावली में सबसे अधिक बढ़त अमूर्त सोच से दूर ले जाती; और केवल लंबे माता-पिता के बच्चों में बढ़त किसी आनुवंशिक या शारीरिक कारण की ओर संकेत करती, जिसे परिच्छेद नकारता है।",
   "what-fits-flynn-s-view",
   opts=["Scores rose most on abstract-reasoning tests and least on vocabulary and arithmetic.",
         "Scores rose by exactly the same amount on every kind of test, in every subject.",
         "Scores rose most on tests of arithmetic and vocabulary, and least on abstract reasoning.",
         "Scores rose only among children whose parents were taller than average."],
   opts_hi=["अमूर्त तर्क में अंक सबसे अधिक और शब्दावली तथा अंकगणित में सबसे कम बढ़े।",
            "हर प्रकार की परीक्षा में, हर विषय में, अंक ठीक उतने ही बढ़े।",
            "अंकगणित और शब्दावली की परीक्षाओं में अंक सबसे अधिक और अमूर्त तर्क में सबसे कम बढ़े।",
            "अंक केवल उन बच्चों में बढ़े जिनके माता-पिता औसत से लंबे थे।"],
   ans=0, pos=2)
