# -*- coding: utf-8 -*-
"""Level 2 · Test 8 (History 4: Art & Culture) -- depth audit of 2026-10-04, part C: Music & Dance and the
tags for the kept rows (parts A and B have the other sub-topics).

Part C rewrites 21 rows in place with the same concept id, type and difficulty. They now ask why a form
looks or sounds the way it does (Dhrupad's austerity, the thumri and Kathak at Lucknow, Kathak's mixed
temple and court roots, the Sangita Ratnakara's standing in both systems), to place a piece or an
instrument from a description (the tillana; the Natya Shastra's four classes), and five-item judgements
(the Carnatic Trinity; the dances the Sangeet Natak Akademi recognises as classical).
With parts A and B: before, analytic 1, precision 12, recall 89; after, analytic 55, precision 17,
recall 30. The other 42 rows keep their content and get their craft tag here.
Leaks avoided while drafting:
  - a 'thaat' distractor in the Sangita Ratnakara MCQ (the new thaat row would knock it out);
  - Dhrupad's unaccompanied alap in the Tansen MCQ (would answer the Dhrupad row);
  - Birju Maharaj in the Kathak row and Kalyanikutty Amma in the Mohiniyattam row (answer the dancers
    pairs row);
  - the Sattriya's year of recognition (with the Akademi list row it would give away an item)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write_updates, CODE
from polity_common import C3, C4, T2

d.SUBJECT = "History"
d.REQUIRE_CRAFT = True
MUS = "Music & Dance"
NFA = "NCERT Class XI, An Introduction to Indian Art"
SNA = "Sangeet Natak Akademi -- classical and folk forms"
CCRT = "Centre for Cultural Resources and Training -- Indian music and dance"
FIVE = ["Only two", "Only three", "Only four", "All five"]
FIVE_HI = ["केवल दो", "केवल तीन", "केवल चार", "सभी पाँच"]

# ================================================================ pairs (1)
P(MUS, "hard", "Consider the following pairs of folk theatre forms and their character:",
  "निम्नलिखित लोक रंगमंच रूपों और उनकी प्रकृति के युग्मों पर विचार कीजिए:",
  ["Tamasha : Lavani songs, dance and comic sketches",
   "Bhavai : A travelling theatre of social satire",
   "Jatra : Open-air theatre that grew out of Vaishnava devotion",
   "Nautanki : Operatic folk theatre of the Hindi heartland"],
  ["तमाशा : लावणी गीत, नृत्य और हास्य दृश्य",
   "भवाई : सामाजिक व्यंग्य का घुमंतू रंगमंच",
   "जात्रा : वैष्णव भक्ति से उपजा खुला रंगमंच",
   "नौटंकी : हिंदी पट्टी का गीत-प्रधान लोक रंगमंच"],
  3,
  "All four pairs are correct. Tamasha of Maharashtra mixes Lavani songs, dance and comic interludes; Bhavai of Gujarat, performed by travelling troupes, mocks social evils through short playlets; Jatra, popular in Bengal and Odisha, grew from the kirtans and processions of Chaitanya's followers into open-air plays on mythological and later social themes; and Nautanki of Uttar Pradesh tells romances and legends through sung verse, to the beat of the nagara drum. "
  "All of them are performed in the open, close to their audiences, with music carrying much of the story.",
  "चारों युग्म सही हैं। महाराष्ट्र का तमाशा लावणी गीतों, नृत्य और हास्य प्रसंगों को मिलाता है; घुमंतू मंडलियों द्वारा प्रस्तुत गुजरात की भवाई छोटे नाटकों से सामाजिक बुराइयों का उपहास करती है; बंगाल और ओडिशा में लोकप्रिय जात्रा चैतन्य के अनुयायियों के कीर्तनों और शोभायात्राओं से पौराणिक और बाद में सामाजिक विषयों के खुले नाटकों में बदली; और उत्तर प्रदेश की नौटंकी नगाड़े की ताल पर गाए जाने वाले पदों से प्रेम-कथाएँ और लोक-कथाएँ कहती है। "
  "ये सभी खुले में, दर्शकों के निकट, खेले जाते हैं, और कथा का बड़ा भाग संगीत ढोता है।",
  SNA, "art-folk-theatre-states-pairs", craft="linkage")

# ================================================================ MCQs (7)
M(MUS, "hard", "Kutiyattam was among the first traditions that UNESCO proclaimed a masterpiece of intangible heritage, in 2001. It is valued above all because it:",
  "कूडियाट्टम उन पहली परंपराओं में था जिन्हें यूनेस्को ने 2001 में अमूर्त धरोहर की उत्कृष्ट कृति घोषित किया। इसे सबसे अधिक इसलिए महत्व दिया जाता है कि यह:",
  ["keeps Sanskrit drama alive on stage in Kerala's temple theatres, with women in the female roles",
   "is the oldest surviving form of Kathakali, from which the masks and make-up of Kathakali developed",
   "is performed in Tamil by village troupes in open squares during the harvest festival",
   "is a shadow-puppet theatre that tells the Ramayana with leather figures"],
  ["केरल के मंदिर-रंगमंचों में संस्कृत नाटक को मंच पर जीवित रखता है, जिसमें स्त्री-भूमिकाएँ स्त्रियाँ निभाती हैं",
   "कथकली का सबसे पुराना बचा रूप है, जिससे कथकली के मुखौटे और रंग-सज्जा विकसित हुए",
   "फ़सल के त्योहार पर खुले चौकों में गाँव की मंडलियों द्वारा तमिल में खेला जाता है",
   "चमड़े की आकृतियों से रामायण कहने वाला छाया-कठपुतली रंगमंच है"],
  0,
  "Kutiyattam, performed by the Chakyar and Nangiar communities in the koothambalams of Kerala's temples, is perhaps the oldest living form of Sanskrit theatre, at least a thousand years old. Its acting is so elaborate -- hand gestures, eye movements and long elaborations of a single verse -- that one act can take many nights, and Nangiar women have long played the female roles, unusual in classical Indian theatre. "
  "Kathakali grew separately, in the seventeenth century; the shadow-puppet theatre of Kerala is the Tholpavakoothu.",
  "केरल के मंदिरों के कूत्तम्बलमों में चाक्यार और नंग्यार समुदायों द्वारा प्रस्तुत कूडियाट्टम संभवतः संस्कृत रंगमंच का सबसे पुराना जीवित रूप है, कम से कम एक हज़ार वर्ष पुराना। इसका अभिनय, यानी हस्त-मुद्राएँ, नेत्र-गतियाँ और एक ही श्लोक का लंबा विस्तार, इतना विस्तृत है कि एक अंक में कई रातें लग सकती हैं, और नंग्यार स्त्रियाँ लंबे समय से स्त्री-भूमिकाएँ निभाती आई हैं, जो शास्त्रीय भारतीय रंगमंच में असामान्य है। "
  "कथकली सत्रहवीं सदी में अलग से विकसित हुई; केरल का छाया-कठपुतली रंगमंच तोलपावकूत्तु है।",
  SNA, "art-kutiyattam-kerala", craft="linkage")

M(MUS, "hard", "The Sangita Ratnakara of Sarngadeva, written in the thirteenth century, is revered as an authority by both Hindustani and Carnatic musicians. This is mainly because:",
  "तेरहवीं सदी में लिखे गए शार्ङ्गदेव के संगीत रत्नाकर को हिंदुस्तानी और कर्नाटक दोनों संगीतकार प्रमाण मानते हैं। यह मुख्यतः इसलिए है कि:",
  ["it was written before music in India divided into the northern and southern systems",
   "it was composed in Persian at the court of Akbar and later translated into Sanskrit",
   "it was commissioned by Krishnadevaraya for the court of Vijayanagara",
   "it set out the 72 melakarta scales that both of the systems still use today"],
  ["यह भारत में संगीत के उत्तरी और दक्षिणी पद्धतियों में बँटने से पहले लिखा गया",
   "इसे अकबर के दरबार में फ़ारसी में रचा गया और संस्कृत में अनूदित किया गया",
   "इसे कृष्णदेवराय ने विजयनगर दरबार के लिए लिखवाया",
   "इसने वे 72 मेलकर्ता स्वरग्राम दिए जिनका दोनों पद्धतियाँ आज भी उपयोग करती हैं"],
  0,
  "Sarngadeva wrote the Sangita Ratnakara at the court of the Yadava king Singhana of Devagiri, drawing together earlier theory on svara, raga, tala, instruments and dance; since the Hindustani and Carnatic traditions drew apart only in the following centuries, both treat it as a common foundation. "
  "Akbar and Krishnadevaraya came three centuries later, and the 72-melakarta system, which belongs to Carnatic music alone, was set out by Venkatamakhi in the seventeenth century.",
  "शार्ङ्गदेव ने देवगिरि के यादव राजा सिंघण के दरबार में संगीत रत्नाकर लिखा, जिसमें स्वर, राग, ताल, वाद्य और नृत्य पर पहले के सिद्धांत को एक साथ लाया गया; चूँकि हिंदुस्तानी और कर्नाटक परंपराएँ अगली सदियों में ही अलग हुईं, इसलिए दोनों इसे साझा नींव मानती हैं। "
  "अकबर और कृष्णदेवराय तीन सदी बाद आए, और 72 मेलकर्ता पद्धति, जो केवल कर्नाटक संगीत की है, सत्रहवीं सदी में वेंकटमखी ने दी।",
  CCRT, "art-sangita-ratnakara-sarngadeva", craft="inference")

M(MUS, "medium", "Dhrupad, the genre with which Tansen is associated, is usually described as austere and meditative. This is mainly because it:",
  "ध्रुपद, जिस शैली से तानसेन जुड़े हैं, को प्रायः गंभीर और ध्यानपूर्ण कहा जाता है। यह मुख्यतः इसलिए कि यह:",
  ["keeps to strict, solemn forms with little ornament, often praising gods or kings",
   "is sung at a fast tempo throughout, with rapid ornamental runs (taans) in every section",
   "is a light, romantic form meant for the courtesans' salons of Lucknow",
   "is a devotional song of the Sufis, sung by a chorus at dargahs"],
  ["कठोर, गंभीर रूपों का पालन करता है जिनमें अलंकरण कम होता है, प्रायः देवताओं या राजाओं की स्तुति में",
   "आद्योपांत तीव्र गति में, हर खंड में तेज़ अलंकारिक तानों के साथ गाया जाता है",
   "लखनऊ की महफ़िलों के लिए बना एक हल्का, शृंगारिक रूप है",
   "सूफ़ियों का भक्ति-गीत है, जो दरगाहों पर समूह में गाया जाता है"],
  0,
  "Dhrupad, the oldest surviving form of Hindustani vocal music, unfolds a raga slowly and with restraint, sets weighty poetry in Braj in a fixed structure of sections, and avoids the light ornaments of later genres; its themes were devotional, heroic or in praise of patrons, which suited temple and court alike. Tansen at Akbar's court and Raja Man Singh Tomar of Gwalior before him are its great names. "
  "Fast taans belong to khayal, the romantic manner to thumri, and the Sufi chorus to qawwali.",
  "हिंदुस्तानी गायन का सबसे पुराना जीवित रूप, ध्रुपद, राग को धीरे और संयम से खोलता है, ब्रज की गंभीर कविता को खंडों की निश्चित संरचना में बाँधता है, और बाद की शैलियों के हल्के अलंकरणों से बचता है; उसके विषय भक्ति, वीरता या संरक्षकों की स्तुति थे, जो मंदिर और दरबार दोनों के अनुकूल थे। अकबर के दरबार में तानसेन और उनसे पहले ग्वालियर के राजा मानसिंह तोमर इसके बड़े नाम हैं। "
  "तेज़ तानें ख़याल की, शृंगारिक ढंग ठुमरी का, और सूफ़ी समूह-गान क़व्वाली का है।",
  CCRT, "art-culture-tansen-dhrupad", craft="linkage")

M(MUS, "medium", "Kathakali's gesture language is based largely on the Hastalakshana Deepika. Bharatanatyam draws more on which of the following texts?",
  "कथकली की मुद्रा-भाषा मुख्यतः हस्तलक्षण दीपिका पर आधारित है। भरतनाट्यम निम्नलिखित में से किस ग्रंथ पर अधिक आधारित है?",
  ["The Abhinaya Darpana of Nandikeshvara",
   "The Sangita Ratnakara of Sarngadeva",
   "The Chitrasutra of the Vishnudharmottara Purana",
   "The Kitab-i-Nauras of Ibrahim Adil Shah II"],
  ["नंदिकेश्वर का अभिनय दर्पण",
   "शार्ङ्गदेव का संगीत रत्नाकर",
   "विष्णुधर्मोत्तर पुराण का चित्रसूत्र",
   "इब्राहीम आदिल शाह द्वितीय की किताब-ए-नौरस"],
  0,
  "The Hastalakshana Deepika gives the 24 basic hand gestures from which Kathakali builds a language able to carry whole sentences, while Bharatanatyam's gestures and expressions draw chiefly on the Abhinaya Darpana ('mirror of gesture') of Nandikeshvara, along with the Natya Shastra. "
  "The Sangita Ratnakara is a treatise on music, the Chitrasutra on painting, and the Kitab-i-Nauras a book of songs in Dakhni.",
  "हस्तलक्षण दीपिका वे 24 मूल हस्त-मुद्राएँ देती है जिनसे कथकली पूरे वाक्य ढो सकने वाली भाषा बनाती है, जबकि भरतनाट्यम की मुद्राएँ और भाव मुख्यतः नाट्यशास्त्र के साथ नंदिकेश्वर के अभिनय दर्पण ('भाव का दर्पण') पर आधारित हैं। "
  "संगीत रत्नाकर संगीत पर, चित्रसूत्र चित्रकला पर ग्रंथ है, और किताब-ए-नौरस दक्खिनी गीतों की पुस्तक है।",
  CCRT, "art-hastalakshana-deepika-kathakali", craft="precision")

M(MUS, "medium", "Purandaradasa is called the 'Pitamaha' (grandfather) of Carnatic music mainly because he:",
  "पुरंदरदास को कर्नाटक संगीत का 'पितामह' मुख्यतः इसलिए कहा जाता है कि उन्होंने:",
  ["devised graded lessons, such as sarali varisai and geetams, still used to teach beginners",
   "composed the Pancharatna kritis that are sung each year at Tiruvaiyaru",
   "set out the 72 melakarta scales from which the other ragas are derived",
   "brought the violin into the Carnatic concert as the main accompanying instrument for singers"],
  ["सरली वरिसै और गीतम जैसे क्रमबद्ध पाठ बनाए, जो आज भी शुरुआती शिष्यों को सिखाए जाते हैं",
   "वे पंचरत्न कृतियाँ रचीं जो हर वर्ष तिरुवैयारु में गाई जाती हैं",
   "वे 72 मेलकर्ता स्वरग्राम दिए जिनसे अन्य राग निकलते हैं",
   "वायलिन को गायकों के मुख्य संगत-वाद्य के रूप में कर्नाटक संगीत-सभा में लाए"],
  0,
  "Purandaradasa (1484-1564), a Haridasa saint of the Vijayanagara period, composed thousands of devotional songs in Kannada and laid down the graded exercises in the raga Mayamalavagowla with which almost every Carnatic student still begins. "
  "The Pancharatna kritis are Tyagaraja's; the 72-melakarta scheme was set out by Venkatamakhi in the seventeenth century; and the violin entered Carnatic music only in the nineteenth.",
  "विजयनगर काल के हरिदास संत पुरंदरदास (1484-1564) ने कन्नड़ में हज़ारों भक्ति-गीत रचे और राग मायामालवगौल में वे क्रमबद्ध अभ्यास निर्धारित किए जिनसे लगभग हर कर्नाटक संगीत विद्यार्थी आज भी आरंभ करता है। "
  "पंचरत्न कृतियाँ त्यागराज की हैं; 72 मेलकर्ता योजना सत्रहवीं सदी में वेंकटमखी ने दी; और वायलिन उन्नीसवीं सदी में ही कर्नाटक संगीत में आया।",
  CCRT, "art-purandaradasa-pitamaha", craft="linkage")

M(MUS, "medium", "The thumri flourished at the court of Wajid Ali Shah of Awadh and grew closely linked with Kathak. This link is best explained by the fact that:",
  "ठुमरी अवध के वाजिद अली शाह के दरबार में फली-फूली और कथक से निकटता से जुड़ गई। इस जुड़ाव की सबसे अच्छी व्याख्या किस तथ्य से होती है?",
  ["both were court arts of Lucknow that put expressive, romantic themes ahead of strict form",
   "both began as temple arts of Tamil Nadu and then travelled north together to the courts of Awadh",
   "the Mughal emperors had banned Dhrupad, leaving only lighter forms at court",
   "both were Sufi forms that grew up at the dargahs of Awadh"],
  ["दोनों लखनऊ की दरबारी कलाएँ थीं जिन्होंने कठोर रूप से अधिक भावपूर्ण, शृंगारिक विषयों को महत्व दिया",
   "दोनों तमिलनाडु की मंदिर-कलाओं के रूप में शुरू हुईं और फिर साथ-साथ उत्तर में अवध के दरबारों तक गईं",
   "मुग़ल सम्राटों ने ध्रुपद पर प्रतिबंध लगा दिया था, जिससे दरबार में केवल हल्के रूप बचे",
   "दोनों सूफ़ी रूप थीं जो अवध की दरगाहों पर पनपीं"],
  0,
  "At Lucknow in the mid-nineteenth century, Wajid Ali Shah, himself a poet, composer and dancer, patronised both: the thumri, with its romantic and devotional lyrics on Radha and Krishna sung with free, expressive phrasing, and Kathak, whose abhinaya (expressive acting) interpreted such songs in dance. The Lucknow gharana of Kathak and the 'purab ang' thumri of Lucknow and Banaras grew up together. "
  "Dhrupad was never banned; it simply gave ground to khayal and lighter forms in the eighteenth and nineteenth centuries.",
  "उन्नीसवीं सदी के मध्य में लखनऊ में स्वयं कवि, संगीतकार और नर्तक वाजिद अली शाह ने दोनों को संरक्षण दिया: राधा-कृष्ण पर शृंगारिक और भक्तिपूर्ण बोलों वाली, मुक्त और भावपूर्ण ढंग से गाई जाने वाली ठुमरी को, और कथक को, जिसका अभिनय ऐसे गीतों की नृत्य में व्याख्या करता था। कथक का लखनऊ घराना और लखनऊ तथा बनारस की 'पूरब अंग' ठुमरी साथ-साथ बढ़े। "
  "ध्रुपद पर कभी प्रतिबंध नहीं लगा; अठारहवीं और उन्नीसवीं सदी में वह बस ख़याल और हल्के रूपों के आगे पीछे हटा।",
  CCRT, "art-thumri-wajid-ali-shah", craft="linkage")

M(MUS, "medium", "A Bharatanatyam recital ends with a brisk piece built mainly on rhythmic syllables, with a short lyric, danced with fast footwork and sculptural poses. The piece is a:",
  "भरतनाट्यम की एक प्रस्तुति एक तेज़ रचना से समाप्त होती है, जो मुख्यतः लयात्मक बोलों पर बनी है और जिसमें एक छोटा गीत है, और जिसे तेज़ पदचाप और मूर्ति जैसी मुद्राओं के साथ नाचा जाता है। यह रचना है:",
  ["tillana", "tarana", "varnam", "alarippu"],
  ["तिल्लाना", "तराना", "वर्णम", "अलारिप्पु"],
  0,
  "The tillana, set to Carnatic music, closes the Bharatanatyam margam with its sparkling rhythms. The tarana is its Hindustani counterpart, sung in khayal concerts and danced in Kathak, so it is the natural trap. "
  "The varnam is the long centrepiece of the recital, combining pure dance with expressive passages, and the alarippu is the opening invocation, an 'unfolding' of the body to rhythm alone.",
  "कर्नाटक संगीत पर आधारित तिल्लाना अपनी चमकदार लयों के साथ भरतनाट्यम के मार्गम को समाप्त करता है। तराना इसका हिंदुस्तानी समकक्ष है, जो ख़याल की सभाओं में गाया और कथक में नाचा जाता है, इसलिए वह स्वाभाविक जाल है। "
  "वर्णम प्रस्तुति का लंबा केंद्रीय भाग है, जिसमें शुद्ध नृत्य और भावपूर्ण अंश मिलते हैं, और अलारिप्पु आरंभिक वंदना है, केवल लय पर शरीर का 'खुलना'।",
  CCRT, "art-tillana", craft="application")

# ================================================================ statements (13)
S(MUS, "easy", "Kathak began in the temples of north India and was later shaped at the Mughal and Rajput courts. Consider the following statements:",
  "कथक उत्तर भारत के मंदिरों में शुरू हुआ और बाद में मुग़ल तथा राजपूत दरबारों में ढला। निम्नलिखित कथनों पर विचार कीजिए:",
  ["This history helps explain why it combines devotional themes with court elements such as the salami (salutation).",
   "Its hallmarks include rapid spins (chakkars) and intricate footwork with ankle bells.",
   "It developed in the temples of Tamil Nadu."],
  ["यह इतिहास बताता है कि यह भक्ति-विषयों को सलामी जैसे दरबारी तत्वों के साथ क्यों जोड़ता है।",
   "तेज़ चक्कर और घुँघरुओं के साथ जटिल पदचाप इसकी पहचान हैं।",
   "यह तमिलनाडु के मंदिरों में विकसित हुआ।"],
  C3, 1,
  "Statements 1 and 2 are correct. The kathakars told stories from the epics and the Puranas in temples; at the Mughal court the dance took on Persian elements such as the salami and themes of court life, while the Rajput courts kept its devotional repertoire, which is why a Kathak recital moves between Krishna stories and pure rhythmic display. Its footwork with ghungroos and its chakkars are its signature. "
  "Statement 3 is wrong: Kathak is a north Indian form; Bharatanatyam grew from the temples of Tamil Nadu.",
  "कथन 1 और 2 सही हैं। कथाकार मंदिरों में महाकाव्यों और पुराणों की कथाएँ कहते थे; मुग़ल दरबार में नृत्य ने सलामी जैसे फ़ारसी तत्व और दरबारी जीवन के विषय अपनाए, जबकि राजपूत दरबारों ने उसका भक्ति-भंडार बनाए रखा, इसीलिए कथक प्रस्तुति कृष्ण-कथाओं और शुद्ध लयात्मक प्रदर्शन के बीच चलती है। घुँघरुओं के साथ पदचाप और चक्कर इसकी पहचान हैं। "
  "कथन 3 गलत है: कथक उत्तर भारत का रूप है; भरतनाट्यम तमिलनाडु के मंदिरों से विकसित हुआ।",
  CCRT, "art-kathak-gharanas", craft="inference")

S(MUS, "hard", "Consider the following composers:",
  "निम्नलिखित संगीतकारों पर विचार कीजिए:",
  ["Tyagaraja", "Muthuswami Dikshitar", "Syama Sastri", "Purandaradasa", "Swathi Thirunal"],
  ["त्यागराज", "मुत्तुस्वामी दीक्षितर", "श्यामा शास्त्री", "पुरंदरदास", "स्वाति तिरुनाल"],
  None, 1,
  "Three of them make up the 'Trinity' of Carnatic music: Tyagaraja, Muthuswami Dikshitar and Syama Sastri, all born in Tiruvarur in the eighteenth century. Tyagaraja composed mostly in Telugu, Dikshitar mostly in Sanskrit and Syama Sastri in Telugu and Sanskrit, and together they shaped much of the concert repertoire. "
  "Purandaradasa, two centuries earlier, is honoured as the 'Pitamaha' of the system, and Swathi Thirunal, the nineteenth-century ruler of Travancore, was a prolific composer in several languages, but neither is counted in the Trinity.",
  "इनमें से तीन कर्नाटक संगीत की 'त्रिमूर्ति' बनाते हैं: त्यागराज, मुत्तुस्वामी दीक्षितर और श्यामा शास्त्री, तीनों अठारहवीं सदी में तिरुवारूर में जन्मे। त्यागराज ने अधिकतर तेलुगु में, दीक्षितर ने अधिकतर संस्कृत में और श्यामा शास्त्री ने तेलुगु और संस्कृत में रचना की, और साथ मिलकर उन्होंने सभा के भंडार का बड़ा भाग गढ़ा। "
  "दो सदी पहले के पुरंदरदास इस पद्धति के 'पितामह' के रूप में सम्मानित हैं, और उन्नीसवीं सदी के त्रावणकोर के शासक स्वाति तिरुनाल कई भाषाओं के विपुल रचनाकार थे, पर दोनों में से कोई त्रिमूर्ति में नहीं गिना जाता।",
  CCRT, "art-carnatic-trinity-languages", opts=FIVE, opts_hi=FIVE_HI,
  closing="How many of the above belong to the 'Trinity' of Carnatic music?", closing_hi="उपर्युक्त में से कितने कर्नाटक संगीत की 'त्रिमूर्ति' में आते हैं?", craft="multi")

S(MUS, "hard", "Consider the following statements about Dhrupad:",
  "ध्रुपद के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Its four traditional styles (banis) are said to derive from the manners of singers at Akbar's court.",
   "The long lineage of the Dagar family helped keep the form alive after khayal became dominant.",
   "It is accompanied on the pakhawaj rather than the tabla."],
  ["इसकी चार पारंपरिक शैलियाँ (बानियाँ) अकबर के दरबार के गायकों के ढंगों से निकली मानी जाती हैं।",
   "डागर परिवार की लंबी परंपरा ने ख़याल के प्रभावी होने के बाद भी इस रूप को जीवित रखा।",
   "इसकी संगत तबले के बजाय पखावज पर होती है।"],
  C3, 2,
  "All three are correct. The Gauhar, Dagur (Dagar), Khandar and Nauhar banis are traced by tradition to singers at Akbar's court. As khayal took over the concert stage from the eighteenth century, Dhrupad survived in a few families, above all the Dagars, whose 'Dagarvani' has been carried on over many generations and revived worldwide in the twentieth century. "
  "A Dhrupad performance opens with an unaccompanied alap, and the composition that follows is set to the deep, open strokes of the barrel-shaped pakhawaj, not the tabla.",
  "तीनों कथन सही हैं। गौहर, डागुर (डागर), खंडार और नौहार बानियों को परंपरा अकबर के दरबार के गायकों से जोड़ती है। अठारहवीं सदी से जब ख़याल ने सभा-मंच सँभाल लिया, तो ध्रुपद कुछ परिवारों में, सबसे अधिक डागरों में, बचा रहा, जिनकी 'डागरवाणी' कई पीढ़ियों तक चली और बीसवीं सदी में संसार भर में पुनर्जीवित हुई। "
  "ध्रुपद प्रस्तुति बिना संगत के आलाप से शुरू होती है, और उसके बाद की बंदिश तबले पर नहीं, ढोलक-आकार के पखावज के गहरे, खुले थापों पर चलती है।",
  CCRT, "art-dhrupad-banis-dagar", craft="linkage")

S(MUS, "medium", "Consider the following statements about Chhau:",
  "छऊ के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It draws on martial practice, and much of its movement reflects mock combat.",
   "Mayurbhanj Chhau dancers wear huge, brightly painted masks.",
   "It is found only in Odisha."],
  ["यह युद्ध-अभ्यास से प्रेरित है, और इसकी अधिकांश गतियाँ नकली युद्ध को दर्शाती हैं।",
   "मयूरभंज छऊ के नर्तक विशाल, चटक रंगों वाले मुखौटे पहनते हैं।",
   "यह केवल ओडिशा में मिलता है।"],
  C3, 0,
  "Only statement 1 is correct. Chhau grew out of the martial exercises of the region, and its leaps, turns and stances draw on mock fighting, with stories from the epics and local legend. "
  "Statement 2 is wrong: Mayurbhanj Chhau is danced without masks; the Seraikela style uses delicate masks, and Purulia Chhau the huge, brightly painted ones. Statement 3 is wrong: its three styles belong to Seraikela in Jharkhand, Mayurbhanj in Odisha and Purulia in West Bengal. UNESCO inscribed Chhau in 2010.",
  "केवल कथन 1 सही है। छऊ क्षेत्र के युद्ध-अभ्यासों से विकसित हुआ, और इसकी छलाँगें, घुमाव और मुद्राएँ महाकाव्यों और स्थानीय कथाओं की कहानियों के साथ नकली युद्ध पर आधारित हैं। "
  "कथन 2 गलत है: मयूरभंज छऊ बिना मुखौटे के नाचा जाता है; सरायकेला शैली नाज़ुक मुखौटे और पुरुलिया छऊ विशाल, चटक रंगों वाले मुखौटे उपयोग करता है। कथन 3 गलत है: इसकी तीन शैलियाँ झारखंड के सरायकेला, ओडिशा के मयूरभंज और पश्चिम बंगाल के पुरुलिया की हैं। यूनेस्को ने 2010 में छऊ को शामिल किया।",
  SNA, "art-chhau", craft="linkage")

S(MUS, "medium", "Consider the following statements about Indian classical music:",
  "भारतीय शास्त्रीय संगीत के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The ten-thaat system of classifying Hindustani ragas was set out by V.N. Bhatkhande in the early twentieth century.",
   "Improvisation, as in the alap and the step-by-step elaboration of a raga, is central to a Hindustani performance.",
   "The thaat system is used to classify the ragas of Carnatic music."],
  ["हिंदुस्तानी रागों के वर्गीकरण की दस-थाट पद्धति वी.एन. भातखंडे ने बीसवीं सदी के आरंभ में दी।",
   "आलाप और राग के क्रमिक विस्तार जैसा तात्कालिक सृजन हिंदुस्तानी प्रस्तुति का केंद्र है।",
   "कर्नाटक संगीत के रागों का वर्गीकरण थाट पद्धति से होता है।"],
  C3, 1,
  "Statements 1 and 2 are correct. Vishnu Narayan Bhatkhande, who also collected compositions and founded music schools, grouped Hindustani ragas under ten parent scales (thaats) such as Bilawal, Kalyan and Bhairav. A raga is a framework, not a fixed tune, so performers build it up through alap, jod and improvised variations on a composition. "
  "Statement 3 is wrong: Carnatic music uses its own system of 72 melakartas (parent scales).",
  "कथन 1 और 2 सही हैं। रचनाएँ एकत्र करने और संगीत विद्यालय स्थापित करने वाले विष्णु नारायण भातखंडे ने हिंदुस्तानी रागों को बिलावल, कल्याण और भैरव जैसे दस जनक स्वरग्रामों (थाटों) में बाँटा। राग एक ढाँचा है, निश्चित धुन नहीं, इसलिए कलाकार उसे आलाप, जोड़ और बंदिश पर तात्कालिक विविधताओं से गढ़ते हैं। "
  "कथन 3 गलत है: कर्नाटक संगीत 72 मेलकर्ताओं (जनक स्वरग्रामों) की अपनी पद्धति का उपयोग करता है।",
  CCRT, "art-classical-music-trinity-thaat", craft="linkage")

S(MUS, "medium", "Consider the following dance forms:",
  "निम्नलिखित नृत्य रूपों पर विचार कीजिए:",
  ["Sattriya", "Mohiniyattam", "Yakshagana", "Kuchipudi", "Garba"],
  ["सत्रिया", "मोहिनीअट्टम", "यक्षगान", "कुचिपुड़ी", "गरबा"],
  None, 1,
  "Three of them are among the eight dance forms that the Sangeet Natak Akademi recognises as classical: Sattriya of Assam, Mohiniyattam of Kerala and Kuchipudi of Andhra Pradesh, along with Bharatanatyam, Kathak, Kathakali, Manipuri and Odissi. "
  "Yakshagana, the dance-theatre of coastal Karnataka, and Garba, the circle dance of Gujarat's Navratri, are celebrated traditional forms but are not on that list.",
  "इनमें से तीन उन आठ नृत्य रूपों में हैं जिन्हें संगीत नाटक अकादमी शास्त्रीय मानती है: असम का सत्रिया, केरल का मोहिनीअट्टम और आंध्र प्रदेश का कुचिपुड़ी, भरतनाट्यम, कथक, कथकली, मणिपुरी और ओडिसी के साथ। "
  "तटीय कर्नाटक का नृत्य-नाट्य यक्षगान और गुजरात की नवरात्रि का घेरा-नृत्य गरबा प्रसिद्ध पारंपरिक रूप हैं, पर उस सूची में नहीं हैं।",
  SNA, "art-culture-classical-dance-forms-origins", opts=FIVE, opts_hi=FIVE_HI,
  closing="How many of the above does the Sangeet Natak Akademi recognise as classical dance forms?",
  closing_hi="उपर्युक्त में से कितने रूपों को संगीत नाटक अकादमी शास्त्रीय नृत्य मानती है?", craft="multi")

S(MUS, "medium", "Consider the following statements about Sattriya:",
  "सत्रिया के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It grew out of the ankiya naat dance-dramas that Sankaradeva created for the Vaishnava monasteries (sattras) of Assam.",
   "For centuries it was performed within the sattras, mainly by male monks (bhokots).",
   "Sankaradeva introduced it as an entertainment for the Ahom court."],
  ["यह उन अंकिया नाट नृत्य-नाटिकाओं से विकसित हुआ जिन्हें शंकरदेव ने असम के वैष्णव मठों (सत्रों) के लिए रचा।",
   "सदियों तक यह सत्रों के भीतर, मुख्यतः पुरुष भिक्षुओं (भोकोतों) द्वारा, प्रस्तुत किया जाता रहा।",
   "शंकरदेव ने इसे अहोम दरबार के मनोरंजन के रूप में शुरू किया।"],
  C3, 1,
  "Statements 1 and 2 are correct. Srimanta Sankaradeva (15th-16th centuries) used drama, music and dance to spread devotion to Krishna, and his ankiya naat plays and their dances became the core of a living tradition in the sattras, kept by celibate monks; it moved onto the public stage and to women dancers in the twentieth century. "
  "Statement 3 is wrong: it was created as a devotional art for the monasteries and the villages, not for the court.",
  "कथन 1 और 2 सही हैं। श्रीमंत शंकरदेव (15वीं-16वीं सदी) ने कृष्ण-भक्ति फैलाने के लिए नाटक, संगीत और नृत्य का उपयोग किया, और उनके अंकिया नाट तथा उनके नृत्य सत्रों में ब्रह्मचारी भिक्षुओं द्वारा सँभाली गई जीवित परंपरा का केंद्र बने; बीसवीं सदी में यह सार्वजनिक मंच और स्त्री नर्तकियों तक पहुँचा। "
  "कथन 3 गलत है: इसे दरबार के लिए नहीं, मठों और गाँवों के लिए भक्ति-कला के रूप में रचा गया।",
  SNA, "art-culture-classical-music-dance-basics", craft="linkage")

S(MUS, "medium", "Consider the following statements about Kathakali:",
  "कथकली के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Its roles, including the female ones, were traditionally performed by men.",
   "The colours of its make-up show each character's nature -- green (pacha) for noble heroes, red-streaked (kathi) for proud villains.",
   "Its music is driven by the chenda and maddalam drums."],
  ["इसकी भूमिकाएँ, स्त्री-भूमिकाओं सहित, परंपरागत रूप से पुरुष निभाते थे।",
   "इसकी रंग-सज्जा के रंग हर पात्र का स्वभाव बताते हैं, जैसे कुलीन नायकों के लिए हरा (पच्चा), घमंडी खलनायकों के लिए लाल धारियों वाला (कत्ति)।",
   "इसका संगीत चेंडा और मद्दलम ढोलों पर चलता है।"],
  C3, 2,
  "All three are correct. Kathakali, which grew in seventeenth-century Kerala from Ramanattam and Krishnanattam, was traditionally an all-male art, demanding years of training in gesture, expression and the vigorous movement drawn from Kalaripayattu. Its make-up types let the audience read a character at a glance -- pacha for heroes and gods, kathi for arrogant villains, thadi (beards) and minukku for women and sages. "
  "The actors do not sing; vocalists carry the text while the chenda and maddalam drive the rhythm.",
  "तीनों कथन सही हैं। सत्रहवीं सदी के केरल में रामनाट्टम और कृष्णनाट्टम से विकसित कथकली परंपरागत रूप से केवल पुरुषों की कला थी, जिसमें मुद्रा, भाव और कलरिपयट्टु से ली गई ज़ोरदार गतियों का वर्षों का प्रशिक्षण लगता है। इसकी रंग-सज्जा के प्रकार दर्शक को एक नज़र में पात्र पहचानने देते हैं: नायकों और देवताओं के लिए पच्चा, घमंडी खलनायकों के लिए कत्ति, ताड़ी (दाढ़ी) और स्त्रियों तथा ऋषियों के लिए मिनुक्कु। "
  "अभिनेता गाते नहीं; गायक पाठ ढोते हैं, जबकि चेंडा और मद्दलम लय चलाते हैं।",
  SNA, "art-kathakali", craft="linkage")

S(MUS, "medium", "Consider the following statements about Manipuri dance:",
  "मणिपुरी नृत्य के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is closely tied to Vaishnava devotion and the Ras Lila of Krishna, shaped in the eighteenth century by King Bhagyachandra.",
   "Its gentle, rounded movements and the absence of ankle bells set it apart from the percussive footwork of other classical forms.",
   "In the Ras Lila the women dancers wear a stiff, barrel-shaped skirt (potloi)."],
  ["यह वैष्णव भक्ति और कृष्ण की रासलीला से निकटता से जुड़ा है, जिसे अठारहवीं सदी में राजा भाग्यचंद्र ने आकार दिया।",
   "इसकी कोमल, गोलाकार गतियाँ और घुँघरुओं का अभाव इसे अन्य शास्त्रीय रूपों के तालवादी पदचाप से अलग करते हैं।",
   "रासलीला में स्त्री नर्तकियाँ कड़ा, ढोल के आकार का घाघरा (पोटलोई) पहनती हैं।"],
  C3, 2,
  "All three are correct. After Vaishnavism spread in Manipur, King Bhagyachandra (Rajarshi) is credited with composing the Ras Lila, in which Krishna and the gopis move in soft, flowing, inward-turned movements that express devotion; dancers do not wear ankle bells, and the feet barely strike the ground. The potloi, a stiff cylindrical skirt with a fine veil, gives the Ras Lila dancers their distinctive look. "
  "Its vigorous counterpart is the pung cholom, in which male drummers leap and whirl while playing.",
  "तीनों कथन सही हैं। मणिपुर में वैष्णव धर्म फैलने के बाद राजा भाग्यचंद्र (राजर्षि) को रासलीला की रचना का श्रेय दिया जाता है, जिसमें कृष्ण और गोपियाँ भक्ति व्यक्त करने वाली कोमल, बहती, भीतर की ओर मुड़ी गतियों में चलते हैं; नर्तक घुँघरू नहीं पहनते, और पैर मुश्किल से ज़मीन पर पड़ते हैं। बारीक घूँघट के साथ कड़ा बेलनाकार घाघरा, पोटलोई, रासलीला की नर्तकियों को उनका विशिष्ट रूप देता है। "
  "इसका ज़ोरदार समकक्ष पुंग चोलोम है, जिसमें पुरुष ढोलवादक बजाते हुए उछलते और घूमते हैं।",
  SNA, "art-manipuri-dance", craft="linkage")

S(MUS, "medium", "Consider the following statements about Mohiniyattam:",
  "मोहिनीअट्टम के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is a vigorous tandava-style dance traditionally performed by men.",
   "It was revived in the twentieth century through the Kalakshetra in Madras.",
   "It is performed to Hindustani music."],
  ["यह परंपरागत रूप से पुरुषों द्वारा किया जाने वाला ज़ोरदार तांडव-शैली का नृत्य है।",
   "बीसवीं सदी में इसका पुनरुद्धार मद्रास के कलाक्षेत्र के माध्यम से हुआ।",
   "यह हिंदुस्तानी संगीत पर प्रस्तुत होता है।"],
  C3, 3,
  "None is correct. Mohiniyattam, named after Mohini, the enchantress form of Vishnu, is a graceful solo in the lasya style, traditionally danced by women, with gentle swaying movements of the torso and a white-and-gold costume. "
  "It was revived by the poet Vallathol through the Kerala Kalamandalam, which he founded in 1930; Kalakshetra in Madras was Rukmini Devi Arundale's institution for Bharatanatyam. Its music is Carnatic, sung in the Sopana style of Kerala's temples.",
  "कोई भी कथन सही नहीं है। विष्णु के मोहक रूप मोहिनी के नाम पर मोहिनीअट्टम लास्य शैली का एक सुंदर एकल नृत्य है, जिसे परंपरागत रूप से स्त्रियाँ करती हैं, धड़ की कोमल डोलती गतियों और सफ़ेद-सुनहरी वेशभूषा के साथ। "
  "इसका पुनरुद्धार कवि वल्लत्तोल ने 1930 में स्थापित केरल कलामंडलम के माध्यम से किया; मद्रास का कलाक्षेत्र भरतनाट्यम के लिए रुक्मिणी देवी अरुंडेल की संस्था थी। इसका संगीत कर्नाटक है, जो केरल के मंदिरों की सोपान शैली में गाया जाता है।",
  SNA, "art-mohiniyattam", craft="precision")

S(MUS, "medium", "Consider the following instruments and the classes to which they are assigned:",
  "निम्नलिखित वाद्यों और उन्हें दिए गए वर्गों पर विचार कीजिए:",
  ["Sitar -- tata (stringed)", "Shehnai -- sushira (wind)", "Mridangam -- avanaddha (covered with skin)", "Manjira (cymbals) -- ghana (solid)"],
  ["सितार -- तत (तार वाद्य)", "शहनाई -- सुषिर (वायु वाद्य)", "मृदंगम -- अवनद्ध (चमड़े से मढ़ा)", "मंजीरा -- घन (ठोस वाद्य)"],
  C4, 3,
  "All four are correctly placed. The Natya Shastra divides instruments into four classes by how sound is produced: tata, where strings vibrate (the sitar, veena, sarod); sushira, where air is blown (the flute, shehnai, nadaswaram); avanaddha, where a stretched skin is struck (the mridangam, tabla, dholak); and ghana, where solid bodies strike each other (cymbals, bells, the jaltarang's cups). "
  "The same fourfold scheme anticipates the modern classification into chordophones, aerophones, membranophones and idiophones.",
  "चारों सही वर्ग में रखे गए हैं। नाट्यशास्त्र ध्वनि उत्पन्न होने के ढंग से वाद्यों को चार वर्गों में बाँटता है: तत, जिनमें तार कंपन करते हैं (सितार, वीणा, सरोद); सुषिर, जिनमें हवा फूँकी जाती है (बाँसुरी, शहनाई, नादस्वरम); अवनद्ध, जिनमें तनी हुई खाल पर थाप दी जाती है (मृदंगम, तबला, ढोलक); और घन, जिनमें ठोस वस्तुएँ आपस में टकराती हैं (मंजीरे, घंटियाँ, जलतरंग के कटोरे)। "
  "यही चार भागों वाली योजना आधुनिक वर्गीकरण, यानी कॉर्डोफ़ोन, एरोफ़ोन, मेम्ब्रेनोफ़ोन और इडियोफ़ोन, का पूर्वाभास है।",
  CCRT, "art-natya-shastra-instrument-classes", closing="In how many of the above is the instrument placed in its correct class of the Natya Shastra?",
  closing_hi="उपर्युक्त में से कितनों में वाद्य को नाट्यशास्त्र के सही वर्ग में रखा गया है?", craft="application")

S(MUS, "medium", "Consider the following statements about Odissi:",
  "ओडिसी के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Its tribhangi posture, with the body bent at the neck, waist and knee, echoes the sculpture on Odisha's temples.",
   "The Gotipua tradition of Odissi is performed by young women.",
   "It developed at the court of the Mughals in Delhi."],
  ["इसकी त्रिभंगी मुद्रा, जिसमें शरीर गर्दन, कमर और घुटने पर मुड़ा होता है, ओडिशा के मंदिरों की मूर्तिकला को दोहराती है।",
   "ओडिसी की गोटीपुआ परंपरा युवा स्त्रियाँ प्रस्तुत करती हैं।",
   "यह दिल्ली के मुग़ल दरबार में विकसित हुई।"],
  C3, 0,
  "Only statement 1 is correct. Odissi's two basic stances, the square, masculine chowk and the curving tribhangi, are the poses of the dancing figures carved on temples such as Konark, from which the twentieth-century revival of the dance drew directly. "
  "Statement 2 is wrong: the gotipuas are boys dressed as girls, who danced when the temple dancers (maharis) declined. Statement 3 is wrong: Odissi grew from the temple dance of the maharis of Puri and the gotipua tradition, and was reconstructed in the 1950s by gurus such as Kelucharan Mohapatra.",
  "केवल कथन 1 सही है। ओडिसी की दो मूल मुद्राएँ, चौकोर, पुरुषोचित चौक और वक्र त्रिभंगी, कोणार्क जैसे मंदिरों पर उकेरी नाचती आकृतियों की मुद्राएँ हैं, जिनसे बीसवीं सदी के पुनरुद्धार ने सीधे प्रेरणा ली। "
  "कथन 2 गलत है: गोटीपुआ लड़कियों के वेश में लड़के होते हैं, जिन्होंने मंदिर-नर्तकियों (महरियों) के पतन के समय नृत्य किया। कथन 3 गलत है: ओडिसी पुरी की महरियों के मंदिर-नृत्य और गोटीपुआ परंपरा से विकसित हुई, और 1950 के दशक में केलुचरण महापात्र जैसे गुरुओं ने इसका पुनर्निर्माण किया।",
  SNA, "art-odissi", craft="linkage")

S(MUS, "medium", "Consider the following statements about the qawwali:",
  "क़व्वाली के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It grew out of the Chishti practice of sama, which treated listening to music as a path to spiritual ecstasy.",
   "Tradition credits Amir Khusrau with shaping it.",
   "The Naqshbandi order also made sama central to its practice."],
  ["यह चिश्तियों की समा प्रथा से निकली, जो संगीत सुनने को आध्यात्मिक आनंद का मार्ग मानती थी।",
   "परंपरा अमीर ख़ुसरो को इसे आकार देने का श्रेय देती है।",
   "नक़्शबंदी सिलसिले ने भी समा को अपने आचरण का केंद्र बनाया।"],
  C3, 1,
  "Statements 1 and 2 are correct. The Chishtis held gatherings of sama at their khanqahs and dargahs, where music and verse were meant to stir the love of God; the qawwali, blending Persian and Indian melody, grew from them, and Amir Khusrau, the disciple of Nizamuddin Auliya, is credited with many of its forms and songs. "
  "Statement 3 is wrong: the Naqshbandis, who stressed strict observance of the sharia, disapproved of music in worship; sama is a mark of the Chishti way.",
  "कथन 1 और 2 सही हैं। चिश्ती अपनी ख़ानक़ाहों और दरगाहों पर समा की महफ़िलें करते थे, जहाँ संगीत और काव्य ईश्वर-प्रेम जगाने के लिए थे; फ़ारसी और भारतीय धुनों को मिलाने वाली क़व्वाली इन्हीं से निकली, और निज़ामुद्दीन औलिया के शिष्य अमीर ख़ुसरो को इसके कई रूपों और गीतों का श्रेय दिया जाता है। "
  "कथन 3 गलत है: शरिया के कड़े पालन पर ज़ोर देने वाले नक़्शबंदी उपासना में संगीत को अनुचित मानते थे; समा चिश्ती मार्ग की पहचान है।",
  CCRT, "art-qawwali-chishti", craft="linkage")

# ================================================================ TAGS for the 42 kept rows (Test 21's 1 is tagged already)
TAGS = {
 "art-monuments-cities-pairs": "recall", "art-culture-stupa-harmika": "recall", "art-gateway-victoria-memorial": "recall",
 "art-jantar-mantar-hawa-mahal": "recall", "art-culture-indo-saracenic-architecture": "precision",
 "art-culture-indo-islamic-architecture-synthesis": "linkage", "art-culture-temple-styles-nagara-dravida-vesara": "precision",
 "culture-pongal-tamil-nadu": "recall", "culture-sangai-festival": "recall", "culture-festivals-hornbill-losar-onam": "recall",
 "art-culture-classical-language-status": "precision",
 "art-images-traditions-pairs": "recall", "art-culture-deity-vahana-pairs": "recall", "art-culture-buddhist-mudras-pairs": "recall",
 "art-durga-vahana-lion": "recall", "art-buddha-ushnisha-urna": "recall", "art-ganesha-kartikeya-attributes": "recall",
 "art-chola-bronze-lost-wax": "precision", "art-culture-jain-iconography-lanchhana": "precision",
 "art-puppetry-states-pairs": "recall", "art-dancers-forms-pairs": "recall", "art-musicians-instruments-pairs": "recall",
 "art-culture-natya-shastra-bharata-muni": "recall", "art-ms-subbulakshmi": "recall", "art-zakir-hussain-tabla": "recall",
 "art-bismillah-khan-shehnai": "recall", "art-bharatanatyam-kathak-basics": "recall", "art-folk-dances-states": "recall",
 "art-lavani": "recall", "art-yakshagana-theyyam": "recall", "art-culture-dhrupad-khayal-history": "precision",
 "art-natya-shastra-rasa": "precision", "art-raga-time-tala-matra": "precision", "art-sangeet-natak-akademi": "precision",
 "art-painting-traditions-states-pairs-2": "recall", "art-pahari-rajasthani-painters-pairs": "recall", "art-kalamkari-medium": "recall",
 "art-kalighat-painting": "recall", "art-tanjore-painting": "recall", "art-bengal-school-modern-painting": "precision",
 "art-culture-mughal-miniature-painting": "precision", "art-culture-pahari-rajput-painting-schools": "precision"}

if __name__ == "__main__":
    write_updates("upg_l2_t08_art_c.sql", statuses=("draft", "published"), tags=TAGS)
