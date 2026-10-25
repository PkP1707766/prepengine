# -*- coding: utf-8 -*-
"""CSAT Level 4 · Simulator 2 -- Reading Comprehension: 10 original passages, 29 items (9 x 3, 1 x 2), Layout B.

Passages in the voice of an op-ed or think-piece, each with a turn -- a claim, then its limit. Themes, none used in
Levels 1-3 or Simulator 1: sanitation and children's growth, out-of-pocket spending on health, Tagore on nationalism,
editing the genes of embryos, falsifiability in science, digital payments and cash, census towns, the undeciphered
Indus script, taxing pollution, and Chennai's rainwater-harvesting rule. Item types: main idea 8, best summary 2,
inference 12 (one of them an implication item), assumption 3, tone 1, specific detail 3.
Difficulty 1 easy / 17 medium / 11 hard. Options are named by content in every explanation."""
from csat_common import passage, RQ

CRUX = "Which one of the following statements best reflects the crux of the passage?"
CRUX_HI = "निम्नलिखित में से कौन-सा कथन परिच्छेद के सार को सबसे अच्छी तरह व्यक्त करता है?"
MSG = "Which one of the following statements best reflects the most logical and rational message conveyed by the passage?"
MSG_HI = "निम्नलिखित में से कौन-सा कथन परिच्छेद द्वारा दिए गए सबसे तार्किक और विवेकपूर्ण संदेश को सबसे अच्छी तरह व्यक्त करता है?"
VALID = "On the basis of the passage, which of the following conclusions is/are valid?"
VALID_HI = "परिच्छेद के आधार पर निम्नलिखित में से कौन-सा/से निष्कर्ष वैध है/हैं?"
ASSUME = "Which of the following assumptions has/have been made in the passage?"
ASSUME_HI = "परिच्छेद में निम्नलिखित में से कौन-सी पूर्वधारणा/एँ बनाई गई है/हैं?"
IMPL = "Which one of the following statements best reflects the most logical and rational implication conveyed by the passage?"
IMPL_HI = "निम्नलिखित में से कौन-सा कथन परिच्छेद द्वारा दिए गए सबसे तार्किक और विवेकपूर्ण निहितार्थ को सबसे अच्छी तरह व्यक्त करता है?"

# ------------------------------------------------------------------ P01 sanitation and children's growth (3)
p = passage("p01",
  "About a third of India's young children are too short for their age, and food alone does not explain it: many stunted children come from households that are not short of food. "
  "One reason lies in the ground around them. Where people defecate in the open, small children who crawl and put things in their mouths swallow germs again and again. Their guts become inflamed and absorb nutrients poorly, so much of what they eat is lost to repeated infection rather than spent on growth. "
  "This makes sanitation a matter of nutrition, and it has an awkward feature: a child is harmed not only by her own family's habits but by her neighbours'. "
  "Trials that gave toilets to some households in villages where most people still went outside found little effect on children's height. A toilet helps a child most when nearly everyone around her uses one too. Building latrines house by house, and counting them, therefore measures the wrong thing; what counts is how many people in a place actually stop defecating in the open.",
  "भारत के लगभग एक-तिहाई छोटे बच्चे अपनी आयु के हिसाब से बहुत नाटे हैं, और अकेला भोजन इसकी व्याख्या नहीं करता: कई ठिगने बच्चे ऐसे घरों से आते हैं जिनमें भोजन की कमी नहीं है। "
  "एक कारण उनके आसपास की ज़मीन में है। जहाँ लोग खुले में शौच करते हैं, वहाँ घुटनों के बल चलने और चीज़ें मुँह में डालने वाले छोटे बच्चे बार-बार कीटाणु निगलते हैं। उनकी आँतों में सूजन आ जाती है और वे पोषक तत्व ठीक से नहीं सोख पातीं, इसलिए वे जो खाते हैं उसका बड़ा भाग वृद्धि में लगने के बजाय बार-बार के संक्रमण में खो जाता है। "
  "इससे स्वच्छता पोषण का विषय बन जाती है, और इसकी एक असुविधाजनक विशेषता है: बच्चे को केवल उसके अपने परिवार की आदतों से नहीं, बल्कि उसके पड़ोसियों की आदतों से भी हानि होती है। "
  "जिन परीक्षणों में ऐसे गाँवों के कुछ घरों को शौचालय दिए गए जहाँ अधिकांश लोग अब भी बाहर जाते थे, उनमें बच्चों की लंबाई पर बहुत कम प्रभाव मिला। शौचालय किसी बच्चे की सबसे अधिक सहायता तब करता है जब उसके आसपास लगभग सभी उसका प्रयोग करें। इसलिए घर-घर शौचालय बनाना और उन्हें गिनना ग़लत चीज़ को मापता है; मायने यह रखता है कि किसी स्थान पर कितने लोग वास्तव में खुले में शौच करना बंद करते हैं।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage links stunting to germs from open defecation, notes that a child is harmed by her neighbours' habits too, and concludes that what matters is how many people in a place stop defecating in the open, not how many toilets are built. "
   "It says food 'alone does not explain' stunting, not that food does not matter; it reports that scattered household toilets had little effect, the opposite of toilets in every home being enough; and it makes no claim that stunting is mainly inherited.",
   "परिच्छेद ठिगनेपन को खुले में शौच से फैलने वाले कीटाणुओं से जोड़ता है, बताता है कि बच्चे को पड़ोसियों की आदतों से भी हानि होती है, और निष्कर्ष निकालता है कि मायने यह रखता है कि किसी स्थान पर कितने लोग खुले में शौच करना बंद करते हैं, यह नहीं कि कितने शौचालय बने। "
   "वह कहता है कि अकेला भोजन ठिगनेपन की 'व्याख्या नहीं करता', यह नहीं कि भोजन का महत्त्व नहीं; वह बताता है कि बिखरे घरेलू शौचालयों का बहुत कम प्रभाव हुआ, जो हर घर में शौचालय के पर्याप्त होने का उलटा है; और वह यह दावा नहीं करता कि ठिगनापन मुख्यतः वंशानुगत है।",
   "crux",
   opts=["Children grow short because they do not get enough food, whatever the state of sanitation around them.",
         "Stunting is tied to sanitation, and what helps is a whole community giving up open defecation.",
         "A toilet in every home is enough on its own to end stunting among the children who live there.",
         "Stunting in India is mainly inherited and owes little to the conditions in which children grow up."],
   opts_hi=["बच्चे इसलिए नाटे रहते हैं कि उन्हें पर्याप्त भोजन नहीं मिलता, आसपास की स्वच्छता चाहे जैसी हो।",
            "ठिगनापन स्वच्छता से जुड़ा है, और सहायता तब मिलती है जब पूरा समुदाय खुले में शौच छोड़ दे।",
            "हर घर में एक शौचालय अपने आप में वहाँ रहने वाले बच्चों का ठिगनापन समाप्त करने के लिए पर्याप्त है।",
            "भारत में ठिगनापन मुख्यतः वंशानुगत है और उन परिस्थितियों का उसमें बहुत कम हाथ है जिनमें बच्चे बड़े होते हैं।"],
   ans=1, pos=1)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Both are valid. 1: because a child is harmed by her neighbours' habits as well as her family's, a toilet in a village where few others use one protects her little -- just what the trials found. "
   "2: the passage says many stunted children come from households 'not short of food', and that much of what they eat is lost to infection; so giving such a child more food may do less for her growth than its quantity suggests.",
   "दोनों वैध हैं। 1: चूँकि बच्चे को उसके परिवार के साथ-साथ पड़ोसियों की आदतों से भी हानि होती है, ऐसे गाँव में जहाँ कुछ ही लोग शौचालय का प्रयोग करते हैं, अपना शौचालय उसकी बहुत कम रक्षा करता है -- ठीक वही जो परीक्षणों में मिला। "
   "2: परिच्छेद कहता है कि कई ठिगने बच्चे ऐसे घरों से हैं जिनमें 'भोजन की कमी नहीं', और कि वे जो खाते हैं उसका बड़ा भाग संक्रमण में खो जाता है; इसलिए ऐसे बच्चे को अधिक भोजन देने से उसकी वृद्धि पर उतना असर नहीं होगा जितना उसकी मात्रा से लगता है।",
   "conclusions",
   st=["A family that builds a toilet in a village where few others use one may see little gain in its children's growth.",
       "For a child who is repeatedly infected, extra food may do less for growth than its quantity would suggest."],
   st_hi=["जो परिवार ऐसे गाँव में शौचालय बनाता है जहाँ कुछ ही लोग उसका प्रयोग करते हैं, उसे अपने बच्चों की वृद्धि में बहुत कम लाभ दिख सकता है।",
          "जो बच्चा बार-बार संक्रमित होता है, उसके लिए अतिरिक्त भोजन वृद्धि पर उतना असर नहीं करेगा जितना उसकी मात्रा से लगता है।"],
   key=2)
RQ(p, "Specific Detail", "easy", "mcq",
   "According to the passage, how does open defecation slow children's growth?",
   "परिच्छेद के अनुसार, खुले में शौच बच्चों की वृद्धि को कैसे धीमा करता है?",
   "The passage says that repeated infection inflames children's guts so that they 'absorb nutrients poorly', and much of what they eat goes on fighting infection rather than on growth. It says nothing of families eating less, of poisoned water or of sleep.",
   "परिच्छेद कहता है कि बार-बार के संक्रमण से बच्चों की आँतों में सूजन आ जाती है जिससे वे 'पोषक तत्व ठीक से नहीं सोख पातीं', और वे जो खाते हैं उसका बड़ा भाग वृद्धि के बजाय संक्रमण से लड़ने में जाता है। वह परिवारों के कम खाने, विषैले पानी या नींद के बारे में कुछ नहीं कहता।",
   "how-open-defecation-slows-growth",
   opts=["Repeated infection damages the gut, so that food is poorly absorbed",
         "Families that lack toilets spend more on medicines and less on food",
         "Germs in the soil poison the water that children drink at home",
         "Children who fall ill often sleep less and so grow more slowly"],
   opts_hi=["बार-बार का संक्रमण आँतों को क्षति पहुँचाता है, जिससे भोजन ठीक से सोखा नहीं जाता",
            "जिन परिवारों के पास शौचालय नहीं, वे दवाओं पर अधिक और भोजन पर कम ख़र्च करते हैं",
            "मिट्टी के कीटाणु उस पानी को विषैला कर देते हैं जो बच्चे घर पर पीते हैं",
            "जो बच्चे प्रायः बीमार पड़ते हैं वे रात में कम सोते हैं और इसलिए धीरे-धीरे बढ़ते हैं"],
   ans=0, pos=0)

# ------------------------------------------------------------------ P02 out-of-pocket spending on health (3)
p = passage("p02",
  "A serious illness can undo years of a family's saving. In India much of the money spent on health still comes straight from patients' pockets, and every year such spending pushes millions of households below the poverty line. "
  "Health insurance for poorer families, such as the government scheme that pays for hospital treatment up to a fixed sum each year, protects against the largest and most sudden bills. That protection matters. "
  "But the bulk of what families pay out of pocket is not for stays in hospital. It goes on visits to doctors and, above all, on medicines and tests for illnesses that are treated at home -- costs that insurance for hospital care does not touch. "
  "A household with a member who has diabetes or high blood pressure may never be admitted to a hospital and still be drained, month after month, by the price of tablets and check-ups. "
  "Insurance against catastrophe is therefore only half a health policy; the other half is cheap or free primary care and medicines close to where people live.",
  "एक गंभीर बीमारी किसी परिवार की वर्षों की बचत मिटा सकती है। भारत में स्वास्थ्य पर ख़र्च होने वाला बहुत-सा धन अब भी सीधे रोगियों की जेब से आता है, और हर वर्ष ऐसा ख़र्च लाखों परिवारों को ग़रीबी रेखा के नीचे धकेल देता है। "
  "निर्धन परिवारों के लिए स्वास्थ्य बीमा, जैसे वह सरकारी योजना जो हर वर्ष एक निश्चित राशि तक अस्पताल के उपचार का भुगतान करती है, सबसे बड़े और सबसे अचानक आने वाले बिलों से रक्षा करता है। यह रक्षा महत्त्वपूर्ण है। "
  "पर परिवार अपनी जेब से जो चुकाते हैं उसका अधिकांश भाग अस्पताल में भर्ती रहने पर नहीं जाता। वह डॉक्टरों को दिखाने पर और, सबसे बढ़कर, घर पर इलाज होने वाली बीमारियों की दवाओं और जाँचों पर जाता है -- ऐसी लागतें जिन्हें अस्पताल उपचार का बीमा छूता तक नहीं। "
  "जिस परिवार के किसी सदस्य को मधुमेह या उच्च रक्तचाप है, वह कभी अस्पताल में भर्ती न होकर भी महीने-दर-महीने गोलियों और जाँचों के मूल्य से निचुड़ता रह सकता है। "
  "इसलिए आपदा के विरुद्ध बीमा स्वास्थ्य नीति का केवल आधा भाग है; दूसरा आधा भाग लोगों के रहने के पास सस्ती या मुफ़्त प्राथमिक चिकित्सा और दवाएँ हैं।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage values insurance against large hospital bills but points out that most out-of-pocket spending is on doctors' visits, medicines and tests, so cheap primary care and medicines are needed as the other half of policy. "
   "It says the insurance protection 'matters', so it does not call the scheme a waste; it nowhere calls for more hospitals in place of insurance; and it says chronic illness drains families even without admission, the opposite of hospital stays being the main burden.",
   "परिच्छेद बड़े अस्पताली बिलों के विरुद्ध बीमा को महत्त्व देता है पर बताता है कि जेब से होने वाला अधिकांश ख़र्च डॉक्टरों को दिखाने, दवाओं और जाँचों पर होता है, इसलिए नीति के दूसरे आधे भाग के रूप में सस्ती प्राथमिक चिकित्सा और दवाएँ चाहिए। "
   "वह कहता है कि बीमा की रक्षा 'महत्त्वपूर्ण है', इसलिए वह योजना को व्यर्थ नहीं कहता; वह कहीं बीमा की जगह अधिक अस्पतालों की माँग नहीं करता; और वह कहता है कि दीर्घकालिक बीमारी भर्ती के बिना भी परिवारों को निचोड़ती है, जो अस्पताल में भर्ती के मुख्य बोझ होने का उलटा है।",
   "crux",
   opts=["Health insurance for poor families is a waste of money and the scheme should be wound up.",
         "The government should build more hospitals instead of paying for insurance for the poor.",
         "Stays in hospital are the main reason families are pushed into poverty by spending on health.",
         "Insurance for hospital bills helps, but cheap primary care and medicines are needed as well."],
   opts_hi=["निर्धन परिवारों के लिए स्वास्थ्य बीमा धन की बर्बादी है और योजना को बंद कर देना चाहिए।",
            "सरकार को निर्धनों के बीमा का भुगतान करने के बजाय और अधिक अस्पताल बनाने चाहिए।",
            "अस्पताल में भर्ती रहना ही वह मुख्य कारण है जिससे स्वास्थ्य पर ख़र्च परिवारों को ग़रीबी में धकेलता है।",
            "अस्पताल के बिलों का बीमा सहायक है, पर सस्ती प्राथमिक चिकित्सा और दवाएँ भी आवश्यक हैं।"],
   ans=3, pos=3)
RQ(p, "Assumption", "medium", "s2", ASSUME, ASSUME_HI,
   "Only 1 is assumed. The call for cheap primary care and medicines 'close to where people live' rests on the idea that making such care cheaper and nearer would actually cut what families pay out of pocket. "
   "2 is not assumed: the passage says much spending comes from patients' pockets, but its argument does not need doctors to overcharge; high costs could arise from many causes.",
   "केवल 1 पूर्वधारणा है। लोगों के 'रहने के पास' सस्ती प्राथमिक चिकित्सा और दवाओं की माँग इस विचार पर टिकी है कि ऐसी चिकित्सा को सस्ता और पास लाने से परिवारों का जेब से ख़र्च वास्तव में घटेगा। "
   "2 पूर्वधारणा नहीं है: परिच्छेद कहता है कि बहुत-सा ख़र्च रोगियों की जेब से आता है, पर उसके तर्क के लिए यह आवश्यक नहीं कि डॉक्टर अधिक शुल्क लें; ऊँची लागतों के कई कारण हो सकते हैं।",
   "assumptions",
   st=["Cheaper and nearer primary care and medicines would reduce what families pay out of their own pockets.",
       "Most doctors in India charge their patients more than their services are worth."],
   st_hi=["सस्ती और पास की प्राथमिक चिकित्सा और दवाएँ परिवारों का अपनी जेब से होने वाला ख़र्च घटाएँगी।",
          "भारत के अधिकांश डॉक्टर अपनी सेवाओं के मूल्य से अधिक शुल्क रोगियों से लेते हैं।"],
   key=0)
RQ(p, "Inference", "hard", "mcq",
   "Which one of the following families would the passage expect to gain least from insurance that pays only for treatment in hospital?",
   "परिच्छेद के अनुसार, निम्नलिखित में से किस परिवार को केवल अस्पताल उपचार का भुगतान करने वाले बीमा से सबसे कम लाभ होगा?",
   "Insurance for hospital care 'does not touch' the costs of medicines and check-ups for illnesses treated at home. A family whose member has long-term high blood pressure, managed with daily tablets and regular tests, pays mostly for exactly those things. "
   "A child's appendix operation, a hip replacement after a fall and a stay in intensive care are all hospital treatment, which the insurance pays for.",
   "अस्पताल उपचार का बीमा घर पर इलाज होने वाली बीमारियों की दवाओं और जाँचों की लागतों को 'छूता तक नहीं'। जिस परिवार के सदस्य को लंबे समय से उच्च रक्तचाप है, जिसका प्रबंधन रोज़ की गोलियों और नियमित जाँचों से होता है, वह मुख्यतः इन्हीं के लिए भुगतान करता है। "
   "बच्चे के अपेंडिक्स का ऑपरेशन, गिरने के बाद कूल्हे का प्रत्यारोपण और गहन चिकित्सा कक्ष में भर्ती -- ये सब अस्पताल उपचार हैं, जिनका भुगतान बीमा करता है।",
   "who-gains-least-from-hospital-insurance",
   opts=["A family whose child needs an emergency operation to remove an inflamed appendix",
         "A family whose grandmother needs a hip replaced after a bad fall at home",
         "A family whose member has long-term high blood pressure managed with tablets",
         "A family whose father spends a week in intensive care after a road accident"],
   opts_hi=["ऐसा परिवार जिसके बच्चे को सूजे हुए अपेंडिक्स को निकालने के लिए आपात ऑपरेशन चाहिए",
            "ऐसा परिवार जिसकी दादी को घर पर बुरी तरह गिरने के बाद कूल्हा बदलवाना है",
            "ऐसा परिवार जिसके सदस्य का लंबे समय से उच्च रक्तचाप गोलियों से संभाला जाता है",
            "ऐसा परिवार जिसके पिता सड़क दुर्घटना के बाद एक सप्ताह गहन चिकित्सा कक्ष में रहते हैं"],
   ans=2, pos=2)

# ------------------------------------------------------------------ P03 Tagore on nationalism (3)
p = passage("p03",
  "Rabindranath Tagore loved his country deeply: he wrote songs now sung as anthems, and in 1919 he gave up his knighthood in protest against the killings at Jallianwala Bagh. Yet in lectures he gave abroad during the First World War he warned against the very idea of the Nation as the West had built it. "
  "A society, in his view, is the living web of relations through which a people cooperates and expresses itself. The modern nation-state is something else: an organisation of a whole people for power and commerce, efficient, mechanical and ready to treat other peoples as competitors or prey. "
  "He feared that a colonised country, in learning to resist such power, might come to copy it. "
  "Many of his contemporaries thought this a luxury for a people still seeking freedom, and his warnings did not stop the nationalist movement, nor were they meant to. What he asked was that love of one's country should not become the final measure of right and wrong, and that freedom from foreign rule should not be bought by adopting the worst habits of the rulers.",
  "रवींद्रनाथ टैगोर अपने देश से गहरा प्रेम करते थे: उन्होंने ऐसे गीत लिखे जो आज राष्ट्रगान के रूप में गाए जाते हैं, और 1919 में जलियाँवाला बाग़ की हत्याओं के विरोध में उन्होंने अपनी नाइटहुड की उपाधि लौटा दी। फिर भी प्रथम विश्वयुद्ध के दौरान विदेश में दिए अपने व्याख्यानों में उन्होंने पश्चिम द्वारा गढ़े गए राष्ट्र के विचार के ही विरुद्ध चेताया। "
  "उनके विचार में समाज संबंधों का वह जीवित ताना-बाना है जिसके द्वारा कोई जनता सहयोग करती और स्वयं को अभिव्यक्त करती है। आधुनिक राष्ट्र-राज्य कुछ और है: शक्ति और व्यापार के लिए पूरी जनता का एक संगठन, कुशल, यांत्रिक और दूसरी जनताओं को प्रतिस्पर्धी या शिकार मानने को तैयार। "
  "उन्हें डर था कि एक उपनिवेशित देश, ऐसी शक्ति का प्रतिरोध करना सीखते हुए, उसी की नक़ल करने लग सकता है। "
  "उनके अनेक समकालीनों को यह स्वतंत्रता की खोज में लगी जनता के लिए एक विलासिता लगी, और उनकी चेतावनियों ने राष्ट्रीय आंदोलन को नहीं रोका, न उनका यह उद्देश्य था। उनकी माँग यह थी कि देश-प्रेम सही और ग़लत का अंतिम माप न बन जाए, और विदेशी शासन से मुक्ति शासकों की सबसे बुरी आदतें अपनाकर न ख़रीदी जाए।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage presents Tagore as a patriot who nonetheless warned that the power-seeking nation-state should not be copied and that love of country should not become the final measure of right. "
   "It says he loved his country and that his warnings were not meant to stop the nationalist movement, so he did not oppose India's freedom; it reports that contemporaries found his view a luxury, not that they agreed; and it says he warned against the Western idea of the nation, not that India should model itself on it.",
   "परिच्छेद टैगोर को ऐसे देशभक्त के रूप में प्रस्तुत करता है जिन्होंने फिर भी चेताया कि शक्ति चाहने वाले राष्ट्र-राज्य की नक़ल न की जाए और देश-प्रेम सही का अंतिम माप न बन जाए। "
   "वह कहता है कि वे अपने देश से प्रेम करते थे और उनकी चेतावनियों का उद्देश्य राष्ट्रीय आंदोलन को रोकना नहीं था, इसलिए उन्होंने भारत की स्वतंत्रता का विरोध नहीं किया; वह बताता है कि समकालीनों को उनका विचार एक विलासिता लगा, यह नहीं कि वे सहमत थे; और वह कहता है कि उन्होंने राष्ट्र के पश्चिमी विचार के विरुद्ध चेताया, यह नहीं कि भारत उसे अपना आदर्श बनाए।",
   "crux",
   opts=["Tagore, though a patriot, warned against copying the power-seeking nation-state.",
         "Tagore opposed India's freedom from British rule because he distrusted all nationalism.",
         "Tagore's contemporaries all agreed that the Western nation-state should not be copied.",
         "Tagore urged India to model itself on the efficient nation-states of the West."],
   opts_hi=["टैगोर ने देशभक्त होते हुए भी शक्ति चाहने वाले राष्ट्र-राज्य की नक़ल के विरुद्ध चेताया।",
            "टैगोर ने ब्रिटिश शासन से भारत की मुक्ति का विरोध किया क्योंकि उन्हें हर राष्ट्रवाद पर संदेह था।",
            "टैगोर के सभी समकालीन सहमत थे कि पश्चिमी राष्ट्र-राज्य की नक़ल नहीं करनी चाहिए।",
            "टैगोर ने भारत से पश्चिम के कुशल राष्ट्र-राज्यों को अपना आदर्श बनाने का आग्रह किया।"],
   ans=0, pos=0)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Neither is valid. 1 contradicts the passage, which presents him as a deep patriot -- he wrote national songs and gave up his knighthood in protest -- who criticised a particular idea of the nation, not love of country. "
   "2 goes beyond it: the passage reports that many contemporaries thought his view a luxury and that it did not stop the movement, but it does not say his warnings were proved wrong by later events.",
   "कोई भी वैध नहीं। 1 परिच्छेद का खंडन करता है, जो उन्हें गहरे देशभक्त के रूप में प्रस्तुत करता है -- उन्होंने राष्ट्रीय गीत लिखे और विरोध में अपनी उपाधि लौटाई -- जिन्होंने राष्ट्र के एक विशेष विचार की आलोचना की, देश-प्रेम की नहीं। "
   "2 उससे आगे जाता है: परिच्छेद बताता है कि अनेक समकालीनों को उनका विचार विलासिता लगा और उसने आंदोलन को नहीं रोका, पर यह नहीं कहता कि बाद की घटनाओं ने उनकी चेतावनियों को ग़लत सिद्ध कर दिया।",
   "conclusions",
   st=["Tagore regarded love of one's country as a danger in itself.",
       "Later events proved Tagore's warnings about the nation-state to be mistaken."],
   st_hi=["टैगोर देश-प्रेम को अपने आप में एक ख़तरा मानते थे।",
          "बाद की घटनाओं ने राष्ट्र-राज्य के बारे में टैगोर की चेतावनियों को ग़लत सिद्ध कर दिया।"],
   key=3)
RQ(p, "Author's Tone", "medium", "mcq",
   "The author's attitude towards Tagore's views is best described as:",
   "टैगोर के विचारों के प्रति लेखक का दृष्टिकोण सबसे अच्छी तरह इस प्रकार वर्णित है:",
   "The author sets out Tagore's argument fairly, records the contemporary objection that it was 'a luxury', and then states what Tagore was actually asking -- a sympathetic but balanced account. "
   "There is no scorn for the ideas; the author does not hold them up as beyond question, since the objection is reported; and the account is not indifferent, since it explains what Tagore meant and why it mattered to him.",
   "लेखक टैगोर के तर्क को निष्पक्ष रूप से रखता है, समकालीनों की यह आपत्ति दर्ज करता है कि वह 'एक विलासिता' था, और फिर बताता है कि टैगोर वास्तव में क्या माँग रहे थे -- एक सहानुभूतिपूर्ण पर संतुलित वृत्तांत। "
   "विचारों के प्रति कोई तिरस्कार नहीं; लेखक उन्हें प्रश्नों से परे नहीं रखता, क्योंकि आपत्ति दर्ज की गई है; और वृत्तांत उदासीन नहीं, क्योंकि वह बताता है कि टैगोर का क्या आशय था और वह उनके लिए क्यों महत्त्वपूर्ण था।",
   "attitude-to-tagore-s-views",
   opts=["Scornful: the views are dismissed as unworldly.",
         "Sympathetic but balanced: the objection is fairly noted.",
         "Reverent: the views are presented as beyond all question.",
         "Indifferent: the views are listed without any comment."],
   opts_hi=["तिरस्कारपूर्ण: विचारों को अव्यावहारिक कहकर ख़ारिज किया गया है।",
            "सहानुभूतिपूर्ण पर संतुलित: आपत्ति निष्पक्ष रूप से दर्ज है।",
            "श्रद्धापूर्ण: विचारों को हर प्रश्न से परे प्रस्तुत किया गया है।",
            "उदासीन: विचारों को बिना किसी टिप्पणी के सूचीबद्ध किया गया है।"],
   ans=1, pos=1)

# ------------------------------------------------------------------ P04 editing the genes of embryos (3)
p = passage("p04",
  "Gene editing tools such as CRISPR can cut and change DNA at a chosen place, and they have begun to cure disease. The first such treatment, approved in 2023 for sickle cell disease and a related blood disorder, edits a patient's own blood-forming cells. Changes of this kind stay in the patient and die with the patient. "
  "Editing an embryo, an egg or a sperm is a different matter. The change would be copied into every cell of the person who grows from it, and passed on to that person's children. "
  "In 2018 a scientist in China announced the birth of twin girls whose genes he had edited as embryos. The work was condemned around the world and he was sent to prison: the girls could not consent, the risks of unintended changes were unknown, and the edit served no pressing medical need. "
  "Some scientists argue that a day may come when editing embryos could spare families a severe inherited disease safely. Even they accept that the step cannot be taken by one laboratory alone, because its effects would be inherited by people who never had a say.",
  "CRISPR जैसे जीन-संपादन उपकरण किसी चुने हुए स्थान पर DNA को काट और बदल सकते हैं, और वे रोगों का उपचार करने लगे हैं। ऐसा पहला उपचार, जिसे 2023 में सिकल सेल रोग और उससे जुड़े एक रक्त विकार के लिए स्वीकृति मिली, रोगी की अपनी रक्त बनाने वाली कोशिकाओं का संपादन करता है। इस प्रकार के बदलाव रोगी में रहते हैं और रोगी के साथ ही समाप्त हो जाते हैं। "
  "किसी भ्रूण, अंडाणु या शुक्राणु का संपादन अलग बात है। बदलाव उससे विकसित होने वाले व्यक्ति की हर कोशिका में नक़ल हो जाएगा, और उस व्यक्ति के बच्चों तक पहुँचेगा। "
  "2018 में चीन के एक वैज्ञानिक ने जुड़वाँ बच्चियों के जन्म की घोषणा की जिनके जीनों का संपादन उसने भ्रूण अवस्था में किया था। इस काम की दुनिया भर में निंदा हुई और उसे जेल भेजा गया: बच्चियाँ सहमति नहीं दे सकती थीं, अनचाहे बदलावों के जोखिम अज्ञात थे, और संपादन किसी गंभीर चिकित्सीय आवश्यकता को पूरा नहीं करता था। "
  "कुछ वैज्ञानिकों का तर्क है कि एक दिन ऐसा आ सकता है जब भ्रूणों का संपादन परिवारों को किसी गंभीर वंशानुगत रोग से सुरक्षित रूप से बचा सके। वे भी मानते हैं कि यह क़दम कोई एक प्रयोगशाला अकेले नहीं उठा सकती, क्योंकि उसके प्रभाव ऐसे लोगों तक पहुँचेंगे जिनकी कभी कोई राय नहीं ली गई।")
RQ(p, "Best Summary", "medium", "mcq", MSG, MSG_HI,
   "The passage separates editing a patient's own cells, already curing disease and confined to that patient, from editing embryos, whose changes are inherited; it explains why the 2018 case was condemned and why even supporters want the step decided beyond one laboratory. "
   "It reports an approved treatment, so it does not call for banning all gene editing; it does not say embryo editing is already safe -- it says that day 'may come'; and it does not say one country's rules should settle the matter.",
   "परिच्छेद रोगी की अपनी कोशिकाओं के संपादन को, जो पहले से रोगों का उपचार कर रहा है और उसी रोगी तक सीमित है, भ्रूणों के संपादन से अलग करता है, जिसके बदलाव आगे पीढ़ियों तक जाते हैं; वह बताता है कि 2018 के मामले की निंदा क्यों हुई और समर्थक भी क्यों चाहते हैं कि यह क़दम एक प्रयोगशाला से परे तय हो। "
   "वह एक स्वीकृत उपचार की बात करता है, इसलिए वह सभी जीन-संपादन पर प्रतिबंध की माँग नहीं करता; वह यह नहीं कहता कि भ्रूण-संपादन पहले से सुरक्षित है -- वह कहता है कि वह दिन 'आ सकता है'; और वह यह नहीं कहता कि किसी एक देश के नियम इस विषय को तय करें।",
   "message",
   opts=["All gene editing should be banned, since its long-term effects on people cannot be known.",
         "Editing embryos is already safe enough to be offered to families at risk of inherited disease.",
         "Editing a patient's own cells is one thing; inheritable embryo edits need a wider decision.",
         "Each country should decide for itself, by its own rules alone, whether embryos may be edited."],
   opts_hi=["सभी जीन-संपादन पर प्रतिबंध लगना चाहिए, क्योंकि लोगों पर उसके दीर्घकालिक प्रभाव जाने नहीं जा सकते।",
            "भ्रूणों का संपादन पहले से इतना सुरक्षित है कि उसे वंशानुगत रोग के जोखिम वाले परिवारों को दिया जा सके।",
            "रोगी की अपनी कोशिकाओं का संपादन एक बात है; वंशानुगत भ्रूण-संपादन के लिए व्यापक निर्णय चाहिए।",
            "हर देश को केवल अपने नियमों से स्वयं तय करना चाहिए कि भ्रूणों का संपादन किया जा सकता है या नहीं।"],
   ans=2, pos=2)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Only 2 is valid. The passage says that changes to a patient's blood-forming cells 'stay in the patient and die with the patient', so a person cured of sickle cell disease this way can still pass on the faulty gene to children. "
   "1 goes too far: the 2018 work was condemned on several grounds -- consent, unknown risks and no pressing need -- and the passage reports scientists who think embryo editing might one day be justified; it does not say that any embryo edit is wrong in every case.",
   "केवल 2 वैध है। परिच्छेद कहता है कि रोगी की रक्त बनाने वाली कोशिकाओं के बदलाव 'रोगी में रहते हैं और रोगी के साथ ही समाप्त हो जाते हैं', इसलिए इस तरह सिकल सेल रोग से ठीक हुआ व्यक्ति भी दोषपूर्ण जीन अपने बच्चों तक पहुँचा सकता है। "
   "1 बहुत आगे जाता है: 2018 के काम की निंदा कई आधारों पर हुई -- सहमति, अज्ञात जोखिम और कोई गंभीर आवश्यकता न होना -- और परिच्छेद ऐसे वैज्ञानिकों का उल्लेख करता है जो मानते हैं कि भ्रूण-संपादन एक दिन उचित हो सकता है; वह यह नहीं कहता कि हर भ्रूण-संपादन हर स्थिति में ग़लत है।",
   "conclusions",
   st=["According to the passage, editing an embryo is wrong in every possible case.",
       "A patient cured of sickle cell disease by editing his own blood-forming cells could still pass the faulty gene to his children."],
   st_hi=["परिच्छेद के अनुसार भ्रूण का संपादन हर संभव स्थिति में ग़लत है।",
          "जो रोगी अपनी रक्त बनाने वाली कोशिकाओं के संपादन से सिकल सेल रोग से ठीक हुआ, वह भी दोषपूर्ण जीन अपने बच्चों तक पहुँचा सकता है।"],
   key=1)
RQ(p, "Specific Detail", "medium", "mcq",
   "Which one of the following is NOT given in the passage as a reason why the work announced in 2018 was condemned?",
   "निम्नलिखित में से कौन-सा कारण परिच्छेद में 2018 में घोषित काम की निंदा के कारण के रूप में नहीं दिया गया है?",
   "The passage gives three reasons: the girls could not consent, the risks of unintended changes were unknown, and the edit served no pressing medical need. It says nothing about the cost of the work being too high.",
   "परिच्छेद तीन कारण देता है: बच्चियाँ सहमति नहीं दे सकती थीं, अनचाहे बदलावों के जोखिम अज्ञात थे, और संपादन किसी गंभीर चिकित्सीय आवश्यकता को पूरा नहीं करता था। वह काम की लागत के बहुत अधिक होने के बारे में कुछ नहीं कहता।",
   "a-reason-not-given",
   opts=["The girls whose genes were edited could not give their consent",
         "The risks of unintended changes to their genes were not known",
         "The edit served no pressing medical need of the two girls",
         "The cost of the work was far too high"],
   opts_hi=["जिन बच्चियों के जीनों का संपादन हुआ वे अपनी सहमति नहीं दे सकती थीं",
            "उनके जीनों में अनचाहे बदलावों के जोखिम ज्ञात नहीं थे",
            "संपादन दोनों बच्चियों की किसी गंभीर चिकित्सीय आवश्यकता को पूरा नहीं करता था",
            "काम की लागत बहुत अधिक थी"],
   ans=3, pos=3)

# ------------------------------------------------------------------ P05 falsifiability (2)
p = passage("p05",
  "The philosopher Karl Popper proposed a test for telling science from other kinds of belief: a scientific theory must forbid something. It must make claims that some possible observation could show to be false. A theory that can explain every outcome, whatever happens, is not thereby strong; it has simply stopped saying anything about the world. "
  "The test is useful but, applied rigidly, misleading. By the 1840s the planet Uranus was known to stray from the orbit that Newton's laws predicted. Astronomers did not abandon the laws; they supposed that an unseen planet was pulling on Uranus, worked out where it should be, and found Neptune there. "
  "Scientists rightly hold on to a successful theory when one prediction fails, and look first for a hidden cause. A theory earns the name of science not by never being doubted, but by being exposed to tests it could fail, and by being given up when the failures pile up.",
  "दार्शनिक कार्ल पॉपर ने विज्ञान को अन्य प्रकार के विश्वासों से अलग करने की एक कसौटी सुझाई: वैज्ञानिक सिद्धांत को किसी बात का निषेध करना चाहिए। उसे ऐसे दावे करने चाहिए जिन्हें कोई संभावित अवलोकन ग़लत सिद्ध कर सके। जो सिद्धांत हर परिणाम की व्याख्या कर सकता है, चाहे जो हो, वह इससे प्रबल नहीं हो जाता; उसने बस दुनिया के बारे में कुछ भी कहना बंद कर दिया है। "
  "कसौटी उपयोगी है, पर कठोरता से लागू करने पर भ्रामक। 1840 के दशक तक यह ज्ञात हो चुका था कि यूरेनस ग्रह न्यूटन के नियमों द्वारा बताई गई कक्षा से भटकता है। खगोलविदों ने नियमों को नहीं छोड़ा; उन्होंने माना कि कोई अदृश्य ग्रह यूरेनस को खींच रहा है, गणना की कि वह कहाँ होना चाहिए, और वहाँ नेपच्यून को पाया। "
  "जब कोई एक भविष्यवाणी विफल होती है, तो वैज्ञानिक उचित ही किसी सफल सिद्धांत को थामे रखते हैं और पहले किसी छिपे कारण की खोज करते हैं। कोई सिद्धांत विज्ञान का नाम कभी संदेह न किए जाने से नहीं, बल्कि ऐसी परीक्षाओं के सामने रखे जाने से पाता है जिनमें वह विफल हो सकता हो, और विफलताएँ जमा होने पर छोड़ दिए जाने से।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage accepts Popper's test -- a scientific theory must be open to being shown false -- and then limits it: scientists reasonably keep a successful theory after one failed prediction, so a theory is scientific if it faces tests it could fail and is given up when failures pile up. "
   "The passage calls a theory that explains everything empty, not strong; it praises the astronomers for keeping Newton's laws, the opposite of dropping a theory at the first failure; and it says science is marked by facing possible failure, not by never being doubted.",
   "परिच्छेद पॉपर की कसौटी को स्वीकार करता है -- वैज्ञानिक सिद्धांत को ग़लत सिद्ध किए जाने के लिए खुला होना चाहिए -- और फिर उसे सीमित करता है: वैज्ञानिक एक विफल भविष्यवाणी के बाद भी उचित ही किसी सफल सिद्धांत को रखते हैं, इसलिए कोई सिद्धांत वैज्ञानिक है यदि वह ऐसी परीक्षाओं का सामना करे जिनमें वह विफल हो सकता हो और विफलताएँ जमा होने पर छोड़ दिया जाए। "
   "परिच्छेद हर बात समझाने वाले सिद्धांत को खोखला कहता है, प्रबल नहीं; वह नियमों को थामे रखने के लिए खगोलविदों की प्रशंसा करता है, जो पहली विफलता पर सिद्धांत छोड़ने का उलटा है; और वह कहता है कि विज्ञान की पहचान संभावित विफलता का सामना करना है, कभी संदेह न होना नहीं।",
   "crux",
   opts=["The best scientific theories are the ones that can explain every possible outcome of an experiment.",
         "A scientist should abandon a theory as soon as a single one of its predictions has failed.",
         "Science is the body of beliefs that no one has ever had any good reason to doubt.",
         "A theory is scientific if it risks failing tests, though one failure need not sink it."],
   opts_hi=["सबसे अच्छे वैज्ञानिक सिद्धांत वे हैं जो किसी प्रयोग के हर संभव परिणाम की व्याख्या कर सकें।",
            "वैज्ञानिक को कोई सिद्धांत उसकी किसी एक भविष्यवाणी के विफल होते ही छोड़ देना चाहिए।",
            "विज्ञान उन विश्वासों का समूह है जिन पर संदेह करने का किसी के पास कभी कोई भी अच्छा कारण नहीं रहा।",
            "सिद्धांत वैज्ञानिक है यदि वह परीक्षा में विफलता का जोखिम उठाए, पर एक विफलता से वह डूबता नहीं।"],
   ans=3, pos=3)
RQ(p, "Inference", "hard", "mcq",
   "Which one of the following would the passage regard as the clearest sign that a theory has stopped being scientific?",
   "निम्नलिखित में से किसे परिच्छेद इस बात का सबसे स्पष्ट संकेत मानेगा कि कोई सिद्धांत वैज्ञानिक नहीं रहा?",
   "A theory whose followers can explain both a result and its opposite after the event 'has simply stopped saying anything about the world' -- it forbids nothing. "
   "Proposing a hidden cause for one failed prediction is what the astronomers rightly did with Uranus; a theory that has passed many tests is the kind the passage values; and giving up a theory after repeated failures is how the passage says science should work.",
   "जिस सिद्धांत के अनुयायी घटना के बाद किसी परिणाम और उसके उलटे, दोनों की व्याख्या कर सकें, उसने 'दुनिया के बारे में कुछ भी कहना बंद कर दिया है' -- वह किसी बात का निषेध नहीं करता। "
   "एक विफल भविष्यवाणी के लिए किसी छिपे कारण का प्रस्ताव वही है जो खगोलविदों ने यूरेनस के मामले में उचित ही किया; कई परीक्षाओं में सफल सिद्धांत वैसा है जिसे परिच्छेद महत्त्व देता है; और बार-बार की विफलताओं के बाद सिद्धांत छोड़ना वही है जैसा परिच्छेद के अनुसार विज्ञान को चलना चाहिए।",
   "a-sign-of-a-theory-that-is-not-science",
   opts=["Its followers explain both a result and its opposite as confirming it, after the event.",
         "Its followers suggest a hidden cause when one of its predictions turns out to be wrong.",
         "It has passed many demanding tests over many years without a single serious failure.",
         "Its followers give it up after its predictions have failed again and again in many tests."],
   opts_hi=["उसके अनुयायी घटना के बाद किसी परिणाम और उसके उलटे, दोनों को उसकी पुष्टि बता देते हैं।",
            "उसकी कोई भविष्यवाणी ग़लत निकलने पर उसके अनुयायी किसी छिपे कारण का सुझाव देते हैं।",
            "वह वर्षों तक अनेक कठिन परीक्षाओं में बिना किसी गंभीर विफलता के सफल रहा है।",
            "कई परीक्षाओं में उसकी भविष्यवाणियाँ बार-बार विफल होने के बाद उसके अनुयायी उसे छोड़ देते हैं।"],
   ans=0, pos=0)

# ------------------------------------------------------------------ P06 digital payments and cash (3)
p = passage("p06",
  "Since its launch in 2016, the Unified Payments Interface has made paying by phone in India almost as easy as handing over a note; the street vendor with a printed code is now a familiar sight, and monthly transactions run into the billions. It is tempting to conclude that cash is on its way out. "
  "The figures do not bear this out. The value of currency in circulation has kept rising, and many people who pay by phone for small purchases still keep and use cash -- for privacy, as a buffer when networks fail, or because the person they are paying does not take digital payments. "
  "The two are less rivals than partners: digital payments have grown alongside cash rather than in place of it. "
  "This has a practical consequence. A policy that treats cash as a relic, or that makes services available only to those who can pay digitally, will fall hardest on the people least able to switch -- the elderly, those without smartphones and those in places with poor connections.",
  "2016 में शुरू होने के बाद से यूनिफ़ाइड पेमेंट्स इंटरफ़ेस ने भारत में फ़ोन से भुगतान को लगभग नोट थमाने जितना आसान बना दिया है; छपे हुए कोड वाला रेहड़ी वाला अब एक जाना-पहचाना दृश्य है, और मासिक लेन-देन अरबों में पहुँचते हैं। यह निष्कर्ष निकालने का मन होता है कि नक़दी जाने वाली है। "
  "आँकड़े इसकी पुष्टि नहीं करते। चलन में मुद्रा का मूल्य बढ़ता ही रहा है, और कई लोग जो छोटी ख़रीद के लिए फ़ोन से भुगतान करते हैं, वे अब भी नक़दी रखते और प्रयोग करते हैं -- गोपनीयता के लिए, नेटवर्क विफल होने पर सहारे के रूप में, या इसलिए कि जिसे वे भुगतान कर रहे हैं वह डिजिटल भुगतान नहीं लेता। "
  "दोनों प्रतिद्वंद्वी कम और साझेदार अधिक हैं: डिजिटल भुगतान नक़दी की जगह लेने के बजाय उसके साथ-साथ बढ़े हैं। "
  "इसका एक व्यावहारिक परिणाम है। जो नीति नक़दी को बीते युग का अवशेष मानती है, या सेवाओं को केवल डिजिटल भुगतान कर सकने वालों के लिए उपलब्ध करती है, उसका सबसे भारी बोझ उन लोगों पर पड़ेगा जो बदलने में सबसे कम सक्षम हैं -- बुज़ुर्ग, बिना स्मार्टफ़ोन वाले और कमज़ोर नेटवर्क वाले स्थानों के लोग।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage argues that digital payments have grown 'alongside cash rather than in place of it', and draws the consequence that policies should not treat cash as a relic, lest they hurt those least able to switch. "
   "It says the figures do not show cash on its way out; it praises the ease of digital payments rather than calling them a failure; and it warns against making services digital-only, the opposite of urging that cash be withdrawn.",
   "परिच्छेद तर्क देता है कि डिजिटल भुगतान 'नक़दी की जगह लेने के बजाय उसके साथ-साथ बढ़े हैं', और यह परिणाम निकालता है कि नीतियाँ नक़दी को अवशेष न मानें, कहीं वे बदलने में सबसे कम सक्षम लोगों को हानि न पहुँचाएँ। "
   "वह कहता है कि आँकड़े नक़दी के जाने को नहीं दिखाते; वह डिजिटल भुगतान की सुगमता की प्रशंसा करता है, उसे विफल नहीं कहता; और वह सेवाओं को केवल डिजिटल बनाने के विरुद्ध चेताता है, जो नक़दी वापस लेने के आग्रह का उलटा है।",
   "crux",
   opts=["Cash will soon disappear from India because paying by phone has become so easy for everyone.",
         "Digital payments have grown beside cash, so policy should not treat cash as obsolete.",
         "Paying by phone has largely failed in India, since most people still prefer to use cash.",
         "The government should withdraw cash quickly so that every purchase is made digitally."],
   opts_hi=["भारत से नक़दी जल्दी ही ग़ायब हो जाएगी क्योंकि फ़ोन से भुगतान सबके लिए बहुत आसान हो गया है।",
            "डिजिटल भुगतान नक़दी के साथ बढ़े हैं, इसलिए नीति को नक़दी को अप्रचलित नहीं मानना चाहिए।",
            "भारत में फ़ोन से भुगतान बड़े पैमाने पर विफल रहा है, क्योंकि अधिकांश लोग अब भी नक़दी पसंद करते हैं।",
            "सरकार को नक़दी जल्दी वापस ले लेनी चाहिए ताकि हर ख़रीद डिजिटल रूप से हो।"],
   ans=1, pos=1)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Only 1 is valid. The passage says that the value of currency in circulation 'has kept rising' while monthly digital transactions run into the billions, so a rapid rise in digital payments has gone together with a rise in cash. "
   "2 goes beyond the passage: it says people keep cash for privacy, as a buffer and because some payees do not take digital payments, but it nowhere says that most people distrust digital payments.",
   "केवल 1 वैध है। परिच्छेद कहता है कि चलन में मुद्रा का मूल्य 'बढ़ता ही रहा है' जबकि मासिक डिजिटल लेन-देन अरबों में पहुँचते हैं, इसलिए डिजिटल भुगतान में तेज़ वृद्धि नक़दी में वृद्धि के साथ-साथ हुई है। "
   "2 परिच्छेद से आगे जाता है: वह कहता है कि लोग गोपनीयता के लिए, सहारे के रूप में और इसलिए नक़दी रखते हैं कि कुछ प्राप्तकर्ता डिजिटल भुगतान नहीं लेते, पर कहीं नहीं कहता कि अधिकांश लोग डिजिटल भुगतान पर अविश्वास करते हैं।",
   "conclusions",
   st=["In India a rapid rise in digital payments has gone together with a rise in the value of cash in circulation.",
       "Most people in India who keep cash do so because they distrust digital payments."],
   st_hi=["भारत में डिजिटल भुगतान में तेज़ वृद्धि चलन में नक़दी के मूल्य में वृद्धि के साथ-साथ हुई है।",
          "भारत में नक़दी रखने वाले अधिकांश लोग ऐसा इसलिए करते हैं कि वे डिजिटल भुगतान पर अविश्वास करते हैं।"],
   key=0)
RQ(p, "Assumption", "hard", "mcq",
   "The warning in the last paragraph rests on which one of the following assumptions?",
   "अंतिम अनुच्छेद की चेतावनी निम्नलिखित में से किस पूर्वधारणा पर टिकी है?",
   "The warning is that a digital-only policy 'will fall hardest' on the elderly, those without smartphones and those with poor connections. That holds only if some people cannot easily switch to paying digitally -- otherwise they would simply switch. "
   "The warning does not depend on digital payments being less safe, on vendors preferring cash, or on cash being cheaper to print; none of these is needed for the harm to fall on those who cannot switch.",
   "चेतावनी यह है कि केवल डिजिटल नीति का 'सबसे भारी बोझ' बुज़ुर्गों, बिना स्मार्टफ़ोन वालों और कमज़ोर नेटवर्क वालों पर पड़ेगा। यह तभी टिकता है जब कुछ लोग आसानी से डिजिटल भुगतान की ओर न बदल सकें -- अन्यथा वे बस बदल जाते। "
   "चेतावनी इस पर निर्भर नहीं कि डिजिटल भुगतान कम सुरक्षित है, रेहड़ी वाले नक़दी पसंद करते हैं, या नक़दी छापना सस्ता है; बदल न सकने वालों पर हानि पड़ने के लिए इनमें से किसी की आवश्यकता नहीं।",
   "what-the-warning-assumes",
   opts=["Digital payments are, on the whole, less safe from fraud than payments made in cash.",
         "Most street vendors would rather be paid in cash than through a printed code.",
         "Printing and handling currency notes costs the country less than running digital systems.",
         "Some people cannot easily switch to paying digitally, whatever the policy may require."],
   opts_hi=["कुल मिलाकर डिजिटल भुगतान नक़द भुगतान की तुलना में धोखाधड़ी से कम सुरक्षित हैं।",
            "अधिकांश रेहड़ी वाले छपे कोड के बजाय नक़दी में भुगतान पाना पसंद करेंगे।",
            "नोट छापना और सँभालना देश के लिए डिजिटल व्यवस्था चलाने से सस्ता पड़ता है।",
            "कुछ लोग आसानी से डिजिटल भुगतान की ओर नहीं बदल सकते, नीति चाहे जो माँगे।"],
   ans=3, pos=3)

# ------------------------------------------------------------------ P07 census towns (3)
p = passage("p07",
  "Officially, a little under a third of India's people lived in towns and cities at the last census in 2011. The figure depends on a definition. Some urban areas are towns because a state government has notified them as such and given them a municipality. "
  "Others, called census towns, are recognised only by the census: places of at least 5,000 people, densely settled, where at least three-quarters of the working men earn their living outside farming. Between 2001 and 2011 the number of census towns almost trebled, to nearly 3,900, and they accounted for a large part of the growth in the urban population. "
  "Yet a census town is still governed as a village. It has a panchayat, not a municipality, and lacks the planning, drainage and services that its size and density require. "
  "Converting such places into towns is not simple: residents may fear higher taxes and the loss of rural schemes. But a country that undercounts its towns will under-plan them, and the consequences arrive as overflowing drains and unplanned growth.",
  "आधिकारिक रूप से, 2011 की पिछली जनगणना में भारत के एक-तिहाई से कुछ कम लोग नगरों और शहरों में रहते थे। यह आँकड़ा एक परिभाषा पर निर्भर है। कुछ शहरी क्षेत्र इसलिए नगर हैं कि किसी राज्य सरकार ने उन्हें ऐसा अधिसूचित किया है और उन्हें नगरपालिका दी है। "
  "अन्य, जिन्हें जनगणना नगर कहा जाता है, केवल जनगणना द्वारा मान्य हैं: कम से कम 5,000 लोगों वाले, घनी बसावट वाले स्थान, जहाँ कम से कम तीन-चौथाई कामकाजी पुरुष खेती से बाहर अपनी जीविका कमाते हैं। 2001 और 2011 के बीच जनगणना नगरों की संख्या लगभग तिगुनी होकर लगभग 3,900 हो गई, और शहरी जनसंख्या की वृद्धि का बड़ा भाग उन्हीं का था। "
  "फिर भी जनगणना नगर का शासन अब भी गाँव की तरह चलता है। उसके पास नगरपालिका नहीं, पंचायत है, और उसमें वह नियोजन, जल-निकासी और सेवाएँ नहीं हैं जो उसके आकार और घनत्व के लिए आवश्यक हैं। "
  "ऐसे स्थानों को नगरों में बदलना सरल नहीं: निवासियों को ऊँचे करों और ग्रामीण योजनाओं के छिन जाने का डर हो सकता है। पर जो देश अपने नगरों को कम गिनता है, वह उनकी कम योजना बनाएगा, और इसके परिणाम उफनती नालियों और अनियोजित विकास के रूप में आते हैं।")
RQ(p, "Best Summary", "medium", "mcq", MSG, MSG_HI,
   "The passage shows that many urban places are counted only by the census and governed as villages, and concludes that undercounting towns leads to under-planning them. "
   "It reports the official figure without saying it is false, only that it depends on a definition; it notes that residents may resist conversion, so it does not say they want it; and it attributes poor services to village government, not to population growth alone.",
   "परिच्छेद दिखाता है कि कई शहरी स्थान केवल जनगणना द्वारा गिने जाते हैं और गाँवों की तरह शासित होते हैं, और निष्कर्ष निकालता है कि नगरों को कम गिनने से उनकी कम योजना बनती है। "
   "वह आधिकारिक आँकड़ा देता है पर उसे ग़लत नहीं कहता, केवल यह कि वह एक परिभाषा पर निर्भर है; वह बताता है कि निवासी बदलाव का विरोध कर सकते हैं, इसलिए यह नहीं कहता कि वे उसे चाहते हैं; और वह ख़राब सेवाओं का कारण ग्रामीण शासन को बताता है, अकेले जनसंख्या-वृद्धि को नहीं।",
   "message",
   opts=["Places that are urban in fact but run as villages need to be counted and planned as towns.",
         "The census figure for India's urban population is false and should be withdrawn at once.",
         "Residents of census towns are eager to be governed by municipalities rather than panchayats.",
         "Poor drainage in census towns is caused only by the speed at which their population has grown."],
   opts_hi=["वास्तव में शहरी पर गाँवों की तरह शासित स्थानों को नगर मानकर गिनना और नियोजित करना चाहिए।",
            "भारत की शहरी जनसंख्या का जनगणना आँकड़ा पूरी तरह ग़लत है और उसे तुरंत वापस ले लेना चाहिए।",
            "जनगणना नगरों के निवासी पंचायतों के बजाय नगरपालिकाओं द्वारा शासित होने के लिए उत्सुक हैं।",
            "जनगणना नगरों में ख़राब जल-निकासी का एकमात्र कारण उनकी जनसंख्या के बढ़ने की तेज़ गति है।"],
   ans=0, pos=0)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Both are valid. 1: a census town is recognised as urban by the census but has no municipality -- it is governed by a panchayat -- so being counted as urban does not by itself give a place urban government. "
   "2: the official urban share counts census towns as urban, and the passage says urban status 'depends on a definition'; so a stricter definition, counting only notified towns, would give a smaller urban share.",
   "दोनों वैध हैं। 1: जनगणना नगर को जनगणना शहरी मानती है पर उसके पास नगरपालिका नहीं -- उसका शासन पंचायत से होता है -- इसलिए शहरी गिने जाने से अपने आप किसी स्थान को शहरी शासन नहीं मिलता। "
   "2: आधिकारिक शहरी हिस्सा जनगणना नगरों को शहरी गिनता है, और परिच्छेद कहता है कि शहरी दर्जा 'एक परिभाषा पर निर्भर है'; इसलिए केवल अधिसूचित नगरों को गिनने वाली कड़ी परिभाषा से शहरी हिस्सा छोटा आएगा।",
   "conclusions",
   st=["Being counted as urban by the census does not by itself give a place a municipality.",
       "If only notified towns were counted as urban, India's official urban share would be smaller."],
   st_hi=["जनगणना द्वारा शहरी गिने जाने से अपने आप किसी स्थान को नगरपालिका नहीं मिल जाती।",
          "यदि केवल अधिसूचित नगरों को शहरी गिना जाए, तो भारत का आधिकारिक शहरी हिस्सा छोटा होगा।"],
   key=2)
RQ(p, "Specific Detail", "medium", "mcq",
   "Which one of the following is NOT one of the conditions a place must meet to be a census town, as the passage describes them?",
   "परिच्छेद में बताई गई शर्तों के अनुसार, निम्नलिखित में से कौन-सी उन शर्तों में से नहीं है जो किसी स्थान को जनगणना नगर बनने के लिए पूरी करनी होती हैं?",
   "The passage lists three conditions: at least 5,000 people, dense settlement, and at least three-quarters of working men earning their living outside farming. Having been notified by the state government is what makes a statutory town -- the very thing a census town lacks.",
   "परिच्छेद तीन शर्तें बताता है: कम से कम 5,000 लोग, घनी बसावट, और कम से कम तीन-चौथाई कामकाजी पुरुषों का खेती से बाहर जीविका कमाना। राज्य सरकार द्वारा अधिसूचित होना वह है जो किसी स्थान को वैधानिक नगर बनाता है -- ठीक वही जो जनगणना नगर के पास नहीं होता।",
   "a-condition-not-required",
   opts=["It must have at least 5,000 people living in it",
         "It must have been notified as a town by the state government",
         "It must be densely settled",
         "At least three-quarters of its working men must earn their living outside farming"],
   opts_hi=["उसमें कम से कम 5,000 लोग रहने चाहिए",
            "राज्य सरकार द्वारा उसे नगर के रूप में अधिसूचित किया गया होना चाहिए",
            "उसकी बसावट घनी होनी चाहिए",
            "उसके कम से कम तीन-चौथाई कामकाजी पुरुष खेती से बाहर जीविका कमाते हों"],
   ans=1, pos=1)

# ------------------------------------------------------------------ P08 the undeciphered Indus script (3)
p = passage("p08",
  "More than four thousand objects bearing signs of the Indus script have been found, most of them small seals, yet nobody can read it. The obstacles are well understood. The inscriptions are very short, most only four or five signs long, so they offer few patterns to work on. "
  "There is no bilingual text, no Indus Rosetta Stone setting the script beside a known one. And the language it recorded is unknown. Some scholars have even argued that the signs may not be full writing at all, but symbols for clans, offices or goods -- a view that others dispute strongly. "
  "Confident announcements of decipherment appear from time to time, and each tends to find in the signs the language its author expected to find. "
  "The silence of the script should not be mistaken for ignorance of the civilisation. From their cities, drains, weights, crafts and trade, archaeologists know a great deal about how these people lived. What remains closed to us is what they would have told us in their own words.",
  "सिंधु लिपि के चिह्नों वाली चार हज़ार से अधिक वस्तुएँ मिली हैं, उनमें से अधिकांश छोटी मुहरें, फिर भी उसे कोई पढ़ नहीं सकता। बाधाएँ भली-भाँति समझी गई हैं। अभिलेख बहुत छोटे हैं, अधिकांश केवल चार या पाँच चिह्नों के, इसलिए उनमें काम करने लायक़ कम पैटर्न मिलते हैं। "
  "कोई द्विभाषी पाठ नहीं है, लिपि को किसी ज्ञात लिपि के साथ रखने वाला सिंधु का कोई 'रोज़ेटा पत्थर' नहीं। और जिस भाषा को वह दर्ज करती थी, वह अज्ञात है। कुछ विद्वानों ने यह तक तर्क दिया है कि चिह्न पूरी लिपि हैं ही नहीं, बल्कि कुलों, पदों या वस्तुओं के प्रतीक हैं -- एक मत जिसका दूसरे दृढ़ता से विरोध करते हैं। "
  "समय-समय पर पढ़ लेने की आत्मविश्वासी घोषणाएँ होती रहती हैं, और हर एक चिह्नों में प्रायः वही भाषा पाती है जिसे उसका लेखक पाने की अपेक्षा रखता था। "
  "लिपि की चुप्पी को उस सभ्यता के बारे में अज्ञान नहीं समझना चाहिए। उनके नगरों, नालियों, बाटों, शिल्पों और व्यापार से पुरातत्वविद बहुत कुछ जानते हैं कि ये लोग कैसे रहते थे। जो हमारे लिए बंद है, वह है जो वे अपने शब्दों में हमें बताते।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage explains why the script resists decipherment -- short texts, no bilingual, an unknown language -- and adds that this does not leave the civilisation unknown, since archaeology tells much about how its people lived. "
   "It reports that some scholars doubt the signs are full writing and that others dispute this, so it does not settle the question; it treats confident decipherments with doubt; and it says a great deal is known about the civilisation.",
   "परिच्छेद बताता है कि लिपि को पढ़ना क्यों कठिन है -- छोटे पाठ, कोई द्विभाषी नहीं, अज्ञात भाषा -- और जोड़ता है कि इससे सभ्यता अज्ञात नहीं रह जाती, क्योंकि पुरातत्व बताता है कि उसके लोग कैसे रहते थे। "
   "वह बताता है कि कुछ विद्वानों को संदेह है कि चिह्न पूरी लिपि हैं और दूसरे इसका विरोध करते हैं, इसलिए वह प्रश्न तय नहीं करता; वह आत्मविश्वासी पढ़ने के दावों को संदेह से देखता है; और वह कहता है कि सभ्यता के बारे में बहुत कुछ ज्ञात है।",
   "crux",
   opts=["The Indus signs have now been shown not to be a true system of writing at all.",
         "The Indus script has recently been read with confidence by several scholars.",
         "The script resists reading for clear reasons, but much is known of the civilisation.",
         "Because its script cannot be read, almost nothing is known of the Indus civilisation."],
   opts_hi=["अब दिखा दिया गया है कि सिंधु चिह्न कोई वास्तविक लेखन-प्रणाली हैं ही नहीं।",
            "हाल में कई विद्वानों ने सिंधु लिपि को आत्मविश्वास के साथ पढ़ लिया है।",
            "लिपि स्पष्ट कारणों से पढ़ी नहीं जा पाती, पर सभ्यता के बारे में बहुत कुछ ज्ञात है।",
            "चूँकि उसकी लिपि पढ़ी नहीं जा सकती, सिंधु सभ्यता के बारे में लगभग कुछ भी ज्ञात नहीं।"],
   ans=2, pos=2)
RQ(p, "Inference", "hard", "s2", VALID, VALID_HI,
   "Neither is valid. 1 overstates the passage, which says a bilingual text is missing, but also names short inscriptions and an unknown language as obstacles; it does not say that a bilingual alone would certainly be enough. "
   "2 contradicts it: the view that the signs are not full writing is reported as one that 'others dispute strongly', not as the settled opinion of most scholars.",
   "कोई भी वैध नहीं। 1 परिच्छेद को बढ़ा-चढ़ाकर कहता है, जो कहता है कि द्विभाषी पाठ नहीं है, पर छोटे अभिलेखों और अज्ञात भाषा को भी बाधाएँ बताता है; वह यह नहीं कहता कि अकेला द्विभाषी पाठ निश्चित रूप से पर्याप्त होगा। "
   "2 उसका खंडन करता है: यह मत कि चिह्न पूरी लिपि नहीं हैं, ऐसे मत के रूप में बताया गया है जिसका 'दूसरे दृढ़ता से विरोध करते हैं', अधिकांश विद्वानों की तय राय के रूप में नहीं।",
   "conclusions",
   st=["If a bilingual inscription were found, the Indus script would certainly be deciphered.",
       "Most scholars now agree that the Indus signs are not a full system of writing."],
   st_hi=["यदि कोई द्विभाषी अभिलेख मिल जाए, तो सिंधु लिपि निश्चित रूप से पढ़ ली जाएगी।",
          "अधिकांश विद्वान अब सहमत हैं कि सिंधु चिह्न पूरी लेखन-प्रणाली नहीं हैं।"],
   key=3)
RQ(p, "Inference", "medium", "mcq",
   "What does the author suggest about the confident announcements of decipherment that appear from time to time?",
   "समय-समय पर होने वाली पढ़ लेने की आत्मविश्वासी घोषणाओं के बारे में लेखक क्या संकेत देता है?",
   "The author says each such announcement 'tends to find in the signs the language its author expected to find' -- a hint that the readings reflect their authors' expectations rather than evidence. "
   "The author does not call them proven, nor credit them to computers, nor say they agree with one another; finding different expected languages implies the opposite.",
   "लेखक कहता है कि ऐसी हर घोषणा 'चिह्नों में प्रायः वही भाषा पाती है जिसे उसका लेखक पाने की अपेक्षा रखता था' -- यह संकेत कि पढ़ाइयाँ प्रमाण के बजाय उनके लेखकों की अपेक्षाओं को दर्शाती हैं। "
   "लेखक उन्हें सिद्ध नहीं कहता, न उनका श्रेय कंप्यूटरों को देता है, न कहता है कि वे एक-दूसरे से सहमत हैं; अलग-अलग अपेक्षित भाषाएँ पाना इसका उलटा संकेत देता है।",
   "what-the-author-suggests-about-decipherments",
   opts=["They have been proved correct by the discovery of new and longer inscriptions.",
         "They tend to reflect what their authors expected more than the evidence.",
         "They mostly rely on computers, which can read scripts that people cannot.",
         "They broadly agree with one another about which language the script recorded."],
   opts_hi=["नए और लंबे अभिलेखों की खोज ने उन्हें सही सिद्ध कर दिया है।",
            "वे प्रमाण जो दिखाता है उससे अधिक अपने लेखकों की अपेक्षाओं को दर्शाती हैं।",
            "वे मुख्यतः कंप्यूटरों पर निर्भर हैं, जो ऐसी लिपियाँ पढ़ सकते हैं जिन्हें लोग नहीं पढ़ सकते।",
            "वे इस बारे में मोटे तौर पर एक-दूसरे से सहमत हैं कि लिपि किस भाषा को दर्ज करती थी।"],
   ans=1, pos=1)

# ------------------------------------------------------------------ P09 taxing pollution (3)
p = passage("p09",
  "When a factory pollutes a river, people downstream bear a cost that appears nowhere in the factory's accounts. A century ago the economist Arthur Pigou proposed a remedy: tax the polluter by an amount equal to the harm done, so that the cost the factory ignores becomes one it must pay. "
  "Faced with the tax, each polluter can choose the cheapest way to cut its pollution -- or pay -- and the cuts happen first where they cost least. Several countries now tax carbon emissions on this principle. "
  "The idea is elegant, and its difficulties are practical. The right rate depends on the harm, which is often uncertain and spread over decades. A tax on fuel can weigh heavily on poorer households, unless the money raised is returned to them. "
  "And where pollution is dangerous at any level, or harms a few people severely in one place, a tax that lets polluters pay and carry on may be the wrong tool; a firm limit may protect people better. A tax on pollution is a powerful instrument, not a universal one.",
  "जब कोई कारख़ाना किसी नदी को प्रदूषित करता है, तो नीचे की ओर रहने वाले लोग ऐसी लागत उठाते हैं जो कारख़ाने के हिसाब-किताब में कहीं नहीं दिखती। एक सदी पहले अर्थशास्त्री आर्थर पिगू ने एक उपाय सुझाया: प्रदूषक पर उतना कर लगाया जाए जितनी हानि होती है, ताकि जिस लागत की कारख़ाना अनदेखी करता है वह ऐसी लागत बन जाए जिसे उसे चुकाना पड़े। "
  "कर का सामना होने पर हर प्रदूषक अपना प्रदूषण घटाने का सबसे सस्ता तरीक़ा चुन सकता है -- या भुगतान कर सकता है -- और कटौतियाँ पहले वहाँ होती हैं जहाँ उनकी लागत सबसे कम हो। कई देश अब इसी सिद्धांत पर कार्बन उत्सर्जन पर कर लगाते हैं। "
  "विचार सुघड़ है, और उसकी कठिनाइयाँ व्यावहारिक हैं। सही दर हानि पर निर्भर है, जो प्रायः अनिश्चित और दशकों में फैली होती है। ईंधन पर कर निर्धन परिवारों पर भारी पड़ सकता है, जब तक कि जुटाया गया धन उन्हें लौटाया न जाए। "
  "और जहाँ प्रदूषण किसी भी स्तर पर ख़तरनाक हो, या किसी एक स्थान पर थोड़े लोगों को गंभीर हानि पहुँचाए, वहाँ ऐसा कर जो प्रदूषकों को भुगतान करके चलते रहने दे, ग़लत उपकरण हो सकता है; एक दृढ़ सीमा लोगों की बेहतर रक्षा कर सकती है। प्रदूषण पर कर एक शक्तिशाली साधन है, सार्वभौमिक नहीं।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage explains Pigou's tax and its strength -- polluters cut where it is cheapest -- and then its limits: an uncertain rate, the burden on the poor and pollution that a firm limit handles better. 'A powerful instrument, not a universal one.' "
   "It does not reject the tax as useless, or say it should replace all regulation; and it treats the burden on poorer households as a problem that can be eased by returning the money, not as a reason why it always fails.",
   "परिच्छेद पिगू के कर और उसकी शक्ति -- प्रदूषक वहाँ कटौती करते हैं जहाँ सबसे सस्ता हो -- को और फिर उसकी सीमाओं को समझाता है: अनिश्चित दर, निर्धनों पर बोझ और ऐसा प्रदूषण जिसे दृढ़ सीमा बेहतर संभालती है। 'एक शक्तिशाली साधन, सार्वभौमिक नहीं।' "
   "वह कर को व्यर्थ कहकर अस्वीकार नहीं करता, न यह कहता है कि वह सारे नियमन की जगह ले; और वह निर्धन परिवारों पर बोझ को ऐसी समस्या मानता है जिसे धन लौटाकर हल्का किया जा सकता है, इस बात का कारण नहीं कि वह हमेशा विफल होता है।",
   "crux",
   opts=["Taxing pollution is useless, because polluters will simply pay the tax and carry on as before.",
         "A tax on pollution should replace every other rule, since it always cuts pollution at least cost.",
         "Taxes on fuel always fail, because they fall heavily on the poorest households in the country.",
         "A pollution tax makes polluters bear the harm, though some cases need firm limits instead."],
   opts_hi=["प्रदूषण पर कर व्यर्थ है, क्योंकि प्रदूषक बस कर चुकाकर पहले की तरह चलते रहेंगे।",
            "प्रदूषण पर कर को हर दूसरे नियम की जगह ले लेनी चाहिए, क्योंकि वह हमेशा न्यूनतम लागत पर प्रदूषण घटाता है।",
            "ईंधन पर कर हमेशा विफल होते हैं, क्योंकि उनका बोझ देश के सबसे निर्धन परिवारों पर भारी पड़ता है।",
            "प्रदूषण कर प्रदूषकों से हानि की क़ीमत चुकवाता है, यद्यपि कुछ मामलों में इसके बजाय दृढ़ सीमाएँ चाहिए।"],
   ans=3, pos=3)
RQ(p, "Inference", "hard", "mcq",
   "In which one of the following cases would the passage most favour a firm limit over a tax?",
   "परिच्छेद निम्नलिखित में से किस मामले में कर की तुलना में दृढ़ सीमा को सबसे अधिक प्राथमिकता देगा?",
   "The passage prefers a firm limit 'where pollution is dangerous at any level, or harms a few people severely in one place'. A toxic metal released near a village school, dangerous even in small amounts, is exactly such a case. "
   "Carbon dioxide from many sources, a modest increase in smoke spread over a large region, and fuel burnt across the country are the diffuse, cost-sensitive cases where a tax works well.",
   "परिच्छेद दृढ़ सीमा को वहाँ प्राथमिकता देता है 'जहाँ प्रदूषण किसी भी स्तर पर ख़तरनाक हो, या किसी एक स्थान पर थोड़े लोगों को गंभीर हानि पहुँचाए'। किसी गाँव के विद्यालय के पास छोड़ी गई विषैली धातु, जो छोटी मात्रा में भी ख़तरनाक है, ठीक ऐसा ही मामला है। "
   "कई स्रोतों से निकलने वाली कार्बन डाइऑक्साइड, बड़े क्षेत्र में फैले धुएँ में साधारण वृद्धि, और देश भर में जलने वाला ईंधन -- ये वे बिखरे, लागत-संवेदी मामले हैं जिनमें कर अच्छा काम करता है।",
   "where-a-firm-limit-is-better",
   opts=["Carbon dioxide released by thousands of factories and power plants across a country",
         "A modest rise in smoke from many small sources spread over a large region",
         "A toxic metal released near a village school, harmful even in small amounts",
         "Petrol and diesel burnt by millions of vehicles on roads all over the country"],
   opts_hi=["किसी देश भर में फैले हज़ारों कारख़ानों और बिजलीघरों से निकलने वाली कार्बन डाइऑक्साइड",
            "बड़े क्षेत्र में फैले अनेक छोटे स्रोतों से धुएँ में साधारण वृद्धि",
            "गाँव के विद्यालय के पास छोड़ी गई विषैली धातु, जो छोटी मात्रा में भी हानिकारक है",
            "पूरे देश की सड़कों पर लाखों वाहनों द्वारा जलाया जाने वाला पेट्रोल और डीज़ल"],
   ans=2, pos=2)
RQ(p, "Assumption", "hard", "s2", ASSUME, ASSUME_HI,
   "Only 2 is assumed. The claim that under the tax 'the cuts happen first where they cost least' rests on polluters responding to the tax by comparing what it would cost them to cut pollution with what they would pay. "
   "1 is not assumed: the passage says the harm is 'often uncertain', which is the opposite of assuming that it can always be measured exactly.",
   "केवल 2 पूर्वधारणा है। यह दावा कि कर के अंतर्गत 'कटौतियाँ पहले वहाँ होती हैं जहाँ उनकी लागत सबसे कम हो', इस पर टिका है कि प्रदूषक कर का उत्तर इस तुलना से देते हैं कि प्रदूषण घटाने में उन्हें कितना लगेगा और कर में कितना देना होगा। "
   "1 पूर्वधारणा नहीं है: परिच्छेद कहता है कि हानि 'प्रायः अनिश्चित' होती है, जो यह मानने का उलटा है कि उसे हमेशा ठीक-ठीक मापा जा सकता है।",
   "assumptions",
   st=["The harm caused by pollution can always be measured exactly.",
       "Polluters weigh the cost of cutting their pollution against the tax they would otherwise pay."],
   st_hi=["प्रदूषण से होने वाली हानि को हमेशा ठीक-ठीक मापा जा सकता है।",
          "प्रदूषक अपना प्रदूषण घटाने की लागत को उस कर से तौलते हैं जो उन्हें अन्यथा चुकाना पड़ता।"],
   key=1)

# ------------------------------------------------------------------ P10 Chennai's rainwater-harvesting rule (3)
p = passage("p10",
  "In 2003, after years of drought, Tamil Nadu made rainwater harvesting compulsory for buildings, and Chennai's householders dug pits and fitted pipes to send rain from their roofs into the ground. In the years that followed, groundwater levels in many parts of the city rose, and the rule was hailed as a model for other cities. "
  "In 2019, after a weak monsoon, the city's reservoirs ran almost dry and water had to be brought in by train. "
  "Part of the explanation is simple neglect: many structures built to satisfy the rule were never cleaned or repaired, and silted up. Part is larger. Rooftop harvesting can top up the ground beneath a house, but it cannot replace the lakes, tanks and wetlands that once caught and stored the region's rain, many of which have been built over. "
  "A rule that requires a pit is easier to make than a habit of maintaining it, and a city that harvests rain from roofs while paving over its lakes has kept the smaller part of the solution and lost the larger.",
  "2003 में, वर्षों के सूखे के बाद, तमिलनाडु ने भवनों के लिए वर्षा-जल संचयन अनिवार्य कर दिया, और चेन्नई के गृहस्वामियों ने अपनी छतों की वर्षा को ज़मीन में भेजने के लिए गड्ढे खोदे और पाइप लगाए। इसके बाद के वर्षों में शहर के कई भागों में भूजल स्तर ऊपर उठा, और इस नियम को दूसरे शहरों के लिए आदर्श बताया गया। "
  "2019 में, कमज़ोर मानसून के बाद, शहर के जलाशय लगभग सूख गए और पानी रेलगाड़ी से लाना पड़ा। "
  "व्याख्या का एक भाग साधारण उपेक्षा है: नियम पूरा करने के लिए बनी कई संरचनाएँ कभी साफ़ या ठीक नहीं की गईं, और गाद से भर गईं। एक भाग बड़ा है। छत से संचयन किसी घर के नीचे की ज़मीन को भर सकता है, पर वह उन झीलों, तालाबों और आर्द्रभूमियों की जगह नहीं ले सकता जो कभी क्षेत्र की वर्षा को पकड़ती और जमा करती थीं, जिनमें से कई पर निर्माण हो चुका है। "
  "गड्ढे की माँग करने वाला नियम बनाना उसके रख-रखाव की आदत बनाने से आसान है, और जो शहर अपनी झीलों को पाटते हुए छतों से वर्षा का संचयन करता है, उसने समाधान का छोटा भाग रखा है और बड़ा भाग खो दिया है।")
RQ(p, "Main Idea", "medium", "mcq", CRUX, CRUX_HI,
   "The passage credits the rule with rising groundwater, then explains the 2019 crisis by neglected structures and the loss of lakes and wetlands -- rooftop harvesting is 'the smaller part of the solution'. "
   "It does not call the rule a failure from the start, since groundwater rose; it blames neglect and lost lakes, not the monsoon alone; and it says harvesting cannot replace lakes and wetlands, the opposite of its making them unnecessary.",
   "परिच्छेद भूजल स्तर के उठने का श्रेय नियम को देता है, फिर 2019 के संकट को उपेक्षित संरचनाओं और झीलों व आर्द्रभूमियों के खोने से समझाता है -- छत से संचयन 'समाधान का छोटा भाग' है। "
   "वह नियम को आरंभ से विफल नहीं कहता, क्योंकि भूजल स्तर उठा; वह उपेक्षा और खोई झीलों को दोष देता है, अकेले मानसून को नहीं; और वह कहता है कि संचयन झीलों और आर्द्रभूमियों की जगह नहीं ले सकता, जो उनके अनावश्यक हो जाने का उलटा है।",
   "crux",
   opts=["Rooftop harvesting helps only if maintained, and cannot make up for lost lakes and wetlands.",
         "Chennai's rule on rainwater harvesting was a failure from the very first year it came into force.",
         "The water crisis of 2019 was caused by a weak monsoon alone, and no rule could have prevented it.",
         "Once every building harvests rain from its roof, a city no longer needs its lakes and wetlands."],
   opts_hi=["छत से संचयन तभी सहायक है जब उसका रख-रखाव हो, और वह खोई झीलों और आर्द्रभूमियों की भरपाई नहीं कर सकता।",
            "चेन्नई का वर्षा-जल संचयन नियम लागू होने के पहले ही वर्ष से विफल था।",
            "2019 का जल-संकट अकेले कमज़ोर मानसून से हुआ, और कोई नियम उसे रोक नहीं सकता था।",
            "एक बार हर भवन अपनी छत से वर्षा का संचयन करने लगे, तो शहर को अपनी झीलों और आर्द्रभूमियों की आवश्यकता नहीं रहती।"],
   ans=0, pos=0)
RQ(p, "Inference", "medium", "s2", VALID, VALID_HI,
   "Neither is valid. 1: the passage says groundwater rose in the years after the rule, so it worked for a time; it explains the later crisis by neglect and lost wetlands, not by the rule never having worked. "
   "2 goes too far: the passage says rooftop harvesting cannot replace the region's lakes and wetlands, but it does not say that restoring them would by itself have prevented any shortage in 2019.",
   "कोई भी वैध नहीं। 1: परिच्छेद कहता है कि नियम के बाद के वर्षों में भूजल स्तर उठा, इसलिए उसने कुछ समय काम किया; वह बाद के संकट को उपेक्षा और खोई आर्द्रभूमियों से समझाता है, नियम के कभी काम न करने से नहीं। "
   "2 बहुत आगे जाता है: परिच्छेद कहता है कि छत से संचयन क्षेत्र की झीलों और आर्द्रभूमियों की जगह नहीं ले सकता, पर यह नहीं कहता कि उन्हें फिर से जीवित करना अकेले 2019 की हर कमी रोक देता।",
   "conclusions",
   st=["The rainwater-harvesting rule never had any effect on Chennai's groundwater.",
       "Had Chennai restored its lakes and wetlands, it would certainly have faced no shortage of water in 2019."],
   st_hi=["वर्षा-जल संचयन नियम का चेन्नई के भूजल पर कभी कोई प्रभाव नहीं पड़ा।",
          "यदि चेन्नई अपनी झीलों और आर्द्रभूमियों को फिर से जीवित करता, तो 2019 में उसे निश्चित रूप से पानी की कोई कमी नहीं होती।"],
   key=3)
RQ(p, "Inference", "hard", "mcq", IMPL, IMPL_HI,
   "The passage's lesson is that a rule requiring structures does little without their upkeep, and that rooftop harvesting is only part of the answer while lakes and wetlands are lost. A city copying the rule should therefore plan for maintenance and protect its water bodies too. "
   "Requiring pits in every building and stopping there repeats the mistake; dropping harvesting altogether ignores that groundwater rose; and relying on water brought by train was an emergency measure, not a policy the passage commends.",
   "परिच्छेद की सीख यह है कि संरचनाओं की माँग करने वाला नियम उनके रख-रखाव के बिना बहुत कम करता है, और कि झीलें व आर्द्रभूमियाँ खोते हुए छत से संचयन उत्तर का केवल एक भाग है। इसलिए इस नियम की नक़ल करने वाले शहर को रख-रखाव की योजना बनानी चाहिए और अपने जलाशयों की रक्षा भी करनी चाहिए। "
   "हर भवन में गड्ढे अनिवार्य करके रुक जाना वही भूल दोहराना है; संचयन को पूरी तरह छोड़ देना इसकी अनदेखी करता है कि भूजल स्तर उठा; और रेलगाड़ी से लाए पानी पर निर्भर रहना आपात उपाय था, ऐसी नीति नहीं जिसकी परिच्छेद प्रशंसा करता है।",
   "an-implication-for-other-cities",
   opts=["Other cities should require harvesting pits in every building, and need do nothing more than that.",
         "Other cities should give up rooftop harvesting, since it did not save Chennai in 2019.",
         "A city adopting such a rule should also plan upkeep and protect its lakes and wetlands.",
         "Cities should plan to bring water in by train whenever their reservoirs run low."],
   opts_hi=["दूसरे शहरों को हर भवन में संचयन के गड्ढे अनिवार्य करने चाहिए, और इससे अधिक कुछ करने की आवश्यकता नहीं।",
            "दूसरे शहरों को छत से संचयन छोड़ देना चाहिए, क्योंकि उसने 2019 में चेन्नई को नहीं बचाया।",
            "ऐसा नियम अपनाने वाला शहर रख-रखाव की योजना भी बनाए और अपनी झीलों व आर्द्रभूमियों की रक्षा करे।",
            "शहरों को योजना बनानी चाहिए कि जब भी उनके जलाशय कम हों, पानी रेलगाड़ी से लाया जाए।"],
   ans=2, pos=2)
