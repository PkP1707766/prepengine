# -*- coding: utf-8 -*-
"""Level 2 · Test 21 -- History block, rewritten to the depth standard of October 2026
(docs/upsc-question-design-standard.md §6). It updates the 16 draft rows of gs_l2_t21_history.py in place:
same concepts, same blueprint cells.
  - The Huna row is now the claim-and-evidence form of the 2026 papers. All three statements are true, and
    the student must judge which of them bear on the claim.
  - The saptanga row asks for the theory's logic (interdependent limbs ranked in order) instead of its list.
The rest stay as they are: trap-built precision rows (sites, guilds, Keezhadi, successor states, revolts,
movements) and the attribution recall that History questions rest on. Every row is tagged.
Craft mix: recall 8, precision 6, linkage 1, inference 1."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write_updates, CODE
from polity_common import C3, C4, T2

d.SUBJECT = "History"
d.REQUIRE_CRAFT = True
AN, MD, MO, MU = "Ancient", "Medieval", "Modern", "Music & Dance"
RS = "R.S. Sharma, India's Ancient Past (Oxford University Press)"
US = "Upinder Singh, A History of Ancient and Early Medieval India (Pearson)"
ASI = "Archaeological Survey of India -- excavation reports"
SC_ = "Satish Chandra, History of Medieval India (Orient BlackSwan)"
NCM = "NCERT Class XII, Themes in Indian History"
BC = "Bipan Chandra, History of Modern India (Orient BlackSwan)"
SB = "Sekhar Bandyopadhyay, From Plassey to Partition and After (Orient BlackSwan)"
SNA = "Sangeet Natak Akademi -- folk and traditional music of India"

# ================================================================ ANCIENT (6)
S(AN, "medium", "Consider the following assertion:\n'In the first half of the sixth century, Indian rulers checked the power of the Huna king Mihirakula.'\nWhich of the following statements support this assertion?",
  "निम्नलिखित अभिकथन पर विचार कीजिए:\n'छठी शताब्दी के पूर्वार्ध में भारतीय शासकों ने हूण राजा मिहिरकुल की शक्ति पर अंकुश लगाया।'\nनिम्नलिखित में से कौन-से कथन इस अभिकथन का समर्थन करते हैं?",
  ["Yashodharman's Mandsaur pillar inscription claims that Mihirakula paid homage at his feet.",
   "Xuanzang records that the Gupta king Baladitya defeated Mihirakula.",
   "Inscriptions of Mihirakula describe him as a devotee of Shiva."],
  ["यशोधर्मन का मंदसौर स्तंभ अभिलेख दावा करता है कि मिहिरकुल ने उसके चरणों में सम्मान अर्पित किया।",
   "ह्वेनसांग लिखता है कि गुप्त राजा बालादित्य ने मिहिरकुल को पराजित किया।",
   "मिहिरकुल के अभिलेख उसे शिव का उपासक बताते हैं।"],
  None, 0,
  "Statements 1 and 2 support the assertion. Yashodharman of Malwa, in his Mandsaur pillar inscription (c. 532 CE), boasts that even Mihirakula bowed at his feet, and Xuanzang's account credits the Gupta king Baladitya with defeating and capturing him. "
  "Statement 3 is also true, but it does not support the assertion: Mihirakula's religious leaning says nothing about whether Indian rulers checked him. This is the fact-versus-relevance trap UPSC now sets -- every statement is correct, and the skill lies in judging which of them bear on the claim. "
  "The invaders, called Shveta Hunas in Indian texts, were a branch of the Hephthalites; after Mihirakula their power in India faded.",
  "कथन 1 और 2 अभिकथन का समर्थन करते हैं। मालवा के यशोधर्मन ने अपने मंदसौर स्तंभ अभिलेख (लगभग 532 ई.) में दावा किया कि स्वयं मिहिरकुल ने उसके चरणों में सिर झुकाया, और ह्वेनसांग का वृत्तांत गुप्त राजा बालादित्य को उसे पराजित कर बंदी बनाने का श्रेय देता है। "
  "कथन 3 भी सही है, पर वह अभिकथन का समर्थन नहीं करता: मिहिरकुल का धार्मिक झुकाव यह नहीं बताता कि भारतीय शासकों ने उस पर अंकुश लगाया या नहीं। यही 'तथ्य बनाम प्रासंगिकता' का जाल है जो UPSC अब बिछाता है: सभी कथन सही हैं, और कौशल यह परखने में है कि उनमें से कौन दावे से जुड़ते हैं। "
  "भारतीय ग्रंथों में श्वेत हूण कहे गए ये आक्रमणकारी हेफ़्थलाइट शाखा के थे; मिहिरकुल के बाद भारत में उनकी शक्ति क्षीण हो गई।",
  f"{US} -- the Hunas and Yashodharman; {RS}.",
  "ancient-hunas-mihirakula-yashodharman", opts=["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
  opts_hi=["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"], closing=CODE, craft="linkage")

P(AN, "medium", "Consider the following pairs of archaeological sites and what they are known for:",
  "पुरातात्विक स्थलों और उनकी प्रसिद्धि के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Kumrahar : A major rock edict of Ashoka",
   "Sinauli : Copper Age burials with wooden carts or chariots",
   "Sanghol : Kushana-period sculptures and a Buddhist stupa",
   "Ratnagiri (Odisha) : A large Buddhist monastic complex"],
  ["कुम्हरार : अशोक का एक प्रमुख शिलालेख",
   "सिनौली : ताम्र युग की समाधियाँ, जिनमें लकड़ी की गाड़ियाँ या रथ मिले",
   "संघोल : कुषाण काल की मूर्तियाँ और एक बौद्ध स्तूप",
   "रत्नगिरि (ओडिशा) : एक विशाल बौद्ध विहार परिसर"],
  2,
  "Only the first pair is wrong. Kumrahar, in Patna, is part of ancient Pataliputra; digging there exposed the remains of a great Mauryan pillared hall, not a rock edict. "
  "Sinauli (Baghpat, Uttar Pradesh) yielded burials of about 2000-1800 BCE with carts or chariots, copper-covered coffins and swords. "
  "Sanghol (Punjab) has a stupa and a hoard of carved railing pillars of the Kushana period in the Mathura style. "
  "Ratnagiri, in Jajpur district of Odisha, was a major Buddhist monastic centre with a large stupa and many images.",
  "केवल पहला युग्म गलत है। पटना का कुम्हरार प्राचीन पाटलिपुत्र का भाग है; वहाँ की खुदाई में एक विशाल मौर्य स्तंभयुक्त सभागार के अवशेष मिले, कोई शिलालेख नहीं। "
  "सिनौली (बागपत, उत्तर प्रदेश) में लगभग 2000-1800 ई.पू. की समाधियाँ मिलीं, जिनमें गाड़ियाँ या रथ, तांबे से मढ़े ताबूत और तलवारें थीं। "
  "संघोल (पंजाब) में एक स्तूप और मथुरा शैली के कुषाण कालीन नक्काशीदार वेदिका-स्तंभों का भंडार मिला है। "
  "ओडिशा के जाजपुर ज़िले का रत्नगिरि एक बड़ा बौद्ध विहार केंद्र था, जहाँ एक बड़ा स्तूप और अनेक प्रतिमाएँ हैं।",
  f"{ASI}; {US}.",
  "ancient-sites-kumrahar-sinauli-sanghol-ratnagiri", craft="precision")

M(AN, "medium", "Which one of the following best reflects the logic of the saptanga theory of the state in the Arthashastra?",
  "निम्नलिखित में से कौन-सा अर्थशास्त्र में राज्य के सप्तांग सिद्धांत के तर्क को सबसे सही दर्शाता है?",
  ["The state works like a body whose seven elements depend on one another, so a weakness in one weakens the whole",
   "The king's authority rests on a contract with the people, who may withdraw it if he rules badly",
   "The seven elements are of equal weight, so a loss of the ally is as grave as a loss of the king",
   "The state exists chiefly to uphold the priestly order, which ranks above the king among the seven elements of the state"],
  ["राज्य एक शरीर की तरह काम करता है जिसके सात अंग एक-दूसरे पर निर्भर हैं, इसलिए एक की कमज़ोरी पूरे को कमज़ोर करती है",
   "राजा का अधिकार प्रजा के साथ एक अनुबंध पर टिका है, जिसे बुरे शासन पर प्रजा वापस ले सकती है",
   "सातों अंग बराबर महत्व के हैं, इसलिए सहयोगी को खोना उतना ही गंभीर है जितना राजा को खोना",
   "राज्य मुख्य रूप से पुरोहित वर्ग की रक्षा के लिए है, जो राज्य के सात अंगों में राजा से ऊपर है"],
  0,
  "The seven prakritis -- svamin (king), amatya (ministers), janapada (territory and people), durga (fort), kosha (treasury), danda (army and justice) and mitra (ally) -- are treated as limbs of one body that sustain one another. "
  "They are not of equal weight: Kautilya lists them in order of importance, with the king first, and argues that a calamity striking an earlier element is graver than one striking a later element. "
  "The idea of kingship resting on a compact with the people belongs to other traditions, such as the Buddhist story of the Mahasammata, the 'great elect'. The royal priest is not one of the limbs at all.",
  "सात प्रकृतियाँ, यानी स्वामी (राजा), अमात्य (मंत्री), जनपद (क्षेत्र और प्रजा), दुर्ग, कोश, दंड (सेना और न्याय) और मित्र (सहयोगी), एक ही शरीर के अंग मानी गई हैं जो एक-दूसरे को टिकाए रखते हैं। "
  "ये बराबर महत्व की नहीं हैं: कौटिल्य इन्हें महत्व के क्रम में गिनाता है, सबसे पहले राजा, और तर्क देता है कि पहले वाले अंग पर आई विपत्ति बाद वाले अंग पर आई विपत्ति से अधिक गंभीर होती है। "
  "प्रजा के साथ समझौते पर टिके राजत्व का विचार अन्य परंपराओं का है, जैसे 'महासम्मत' (महान चुना हुआ) की बौद्ध कथा। राजपुरोहित तो इन अंगों में है ही नहीं।",
  f"{RS} -- state and administration in the Arthashastra; {US}.",
  "ancient-saptanga-arthashastra", craft="inference")

S(AN, "hard", "Consider the following statements about guilds (shrenis) in early India:",
  "प्राचीन भारत में श्रेणियों (गिल्ड) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Guilds accepted money deposits and paid interest on them, as recorded in inscriptions at the Nashik caves.",
   "The Dharmashastras asked the king to respect the customary rules of guilds.",
   "Clay seals of guilds and merchant bodies have been found at Vaishali (Basarh)."],
  ["श्रेणियाँ धन जमा के रूप में लेती थीं और उस पर ब्याज देती थीं, जैसा नासिक गुफाओं के अभिलेखों में दर्ज है।",
   "धर्मशास्त्रों ने राजा से श्रेणियों के प्रचलित नियमों का सम्मान करने को कहा।",
   "वैशाली (बसाढ़) से श्रेणियों और व्यापारी संगठनों की मिट्टी की मुहरें मिली हैं।"],
  C3, 2,
  "All three are correct. A Nashik cave inscription of Ushavadata, son-in-law of the Shaka ruler Nahapana, records permanent deposits with weavers' guilds at Govardhana, the interest paying for the monks' robes. "
  "Law books such as those of Manu, Yajnavalkya and Narada tell the king to uphold shreni-dharma, the internal rules of guilds. "
  "Hundreds of Gupta-period seals from Basarh carry the names of a joint body of bankers, caravan traders and artisans (shreshthi-sarthavaha-kulika-nigama). Guilds also acted as trustees for gifts to temples and monasteries.",
  "तीनों कथन सही हैं। शक शासक नहपान के दामाद उषवदात का नासिक गुफा अभिलेख गोवर्धन के बुनकर-श्रेणियों के पास स्थायी जमा का उल्लेख करता है, जिसके ब्याज से भिक्षुओं के वस्त्र का ख़र्च चलता था। "
  "मनु, याज्ञवल्क्य और नारद जैसे धर्मशास्त्र राजा से श्रेणी-धर्म, यानी श्रेणियों के आंतरिक नियमों, की रक्षा करने को कहते हैं। "
  "बसाढ़ से गुप्त काल की सैकड़ों मुहरें मिली हैं जिन पर साहूकारों, सार्थवाहों और कारीगरों के संयुक्त निकाय (श्रेष्ठि-सार्थवाह-कुलिक-निगम) के नाम हैं। श्रेणियाँ मंदिरों और विहारों को मिले दान की न्यासी भी होती थीं।",
  f"{RS} -- crafts, trade and guilds; {US}.",
  "ancient-shreni-guilds-banking", craft="precision")

S(AN, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Halmidi inscription is regarded as the earliest known inscription in Telugu.",
   "Bhaskaravarman, king of Kamarupa, was an ally of Harshavardhana."],
  ["हल्मिडी अभिलेख को तेलुगु का सबसे प्राचीन ज्ञात अभिलेख माना जाता है।",
   "कामरूप के राजा भास्करवर्मन हर्षवर्धन के सहयोगी थे।"],
  T2, 1,
  "Only statement 2 is correct. The Halmidi inscription, found in Hassan district of Karnataka and usually dated to the fifth century, is the earliest known inscription in Kannada, not Telugu. "
  "Bhaskaravarman of Kamarupa, in present-day Assam, allied with Harsha against Shashanka of Gauda; he hosted Xuanzang and attended Harsha's assembly at Kannauj.",
  "केवल कथन 2 सही है। कर्नाटक के हासन ज़िले में मिला हल्मिडी अभिलेख, जिसे सामान्यतः पाँचवीं शताब्दी का माना जाता है, कन्नड़ का सबसे प्राचीन ज्ञात अभिलेख है, तेलुगु का नहीं। "
  "वर्तमान असम में स्थित कामरूप के भास्करवर्मन ने गौड़ के शशांक के विरुद्ध हर्ष से मित्रता की; उन्होंने ह्वेनसांग का सत्कार किया और कन्नौज में हर्ष की सभा में भाग लिया।",
  f"{US} -- early Kannada epigraphy and Kamarupa; {RS}.",
  "ancient-halmidi-kamarupa-bhaskaravarman", craft="recall")

S(AN, "medium", "Consider the following statements about the excavations at Keezhadi:",
  "कीझड़ी (Keezhadi) की खुदाई के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The site lies on the banks of the Kaveri near Thanjavur.",
   "Potsherds bearing Tamil-Brahmi letters have been found there.",
   "It is a Harappan site of the third millennium BCE, like Rakhigarhi."],
  ["यह स्थल तंजावुर के पास कावेरी के तट पर है।",
   "वहाँ तमिल-ब्राह्मी अक्षरों वाले मृद्भांड के टुकड़े मिले हैं।",
   "यह राखीगढ़ी की तरह ई.पू. तीसरी सहस्राब्दी का एक हड़प्पा स्थल है।"],
  C3, 0,
  "Only statement 2 is correct. Keezhadi lies on the Vaigai, about 12 km south-east of Madurai in Sivaganga district, not on the Kaveri. "
  "Its brick structures, ring wells, drains and potsherds inscribed in Tamil-Brahmi point to an urban settlement of the early historic, Sangam-age Tamil country. "
  "It is not a Harappan site: its layers belong to the first millennium BCE, long after the Harappan cities, although some of its graffiti marks have been compared with Indus signs.",
  "केवल कथन 2 सही है। कीझड़ी शिवगंगा ज़िले में मदुरै से लगभग 12 किमी दक्षिण-पूर्व में वैगई नदी के तट पर है, कावेरी पर नहीं। "
  "वहाँ की ईंटों की संरचनाएँ, वलय कूप, नालियाँ और तमिल-ब्राह्मी में अंकित मृद्भांड प्रारंभिक ऐतिहासिक, संगम कालीन तमिल क्षेत्र की एक नगरीय बस्ती की ओर संकेत करते हैं। "
  "यह हड़प्पा स्थल नहीं है: इसकी परतें ई.पू. पहली सहस्राब्दी की हैं, हड़प्पा नगरों से बहुत बाद की, यद्यपि इसके कुछ भित्ति-चिह्नों की तुलना सिंधु लिपि के चिह्नों से की गई है।",
  "Tamil Nadu State Department of Archaeology -- Keeladi excavation reports; Archaeological Survey of India.",
  "ancient-keezhadi-vaigai", craft="precision")

# ================================================================ MEDIEVAL (3)
S(MD, "medium", "Consider the following statements about Guru Tegh Bahadur:",
  "गुरु तेग बहादुर के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["He was executed in Delhi in 1675 on the orders of Aurangzeb.",
   "He founded the settlement of Chak Nanaki, which grew into Anandpur Sahib.",
   "His hymns were added to the Guru Granth Sahib by Guru Gobind Singh."],
  ["1675 में औरंगज़ेब के आदेश पर दिल्ली में उन्हें मृत्युदंड दिया गया।",
   "उन्होंने चक नानकी नामक बस्ती बसाई, जो आगे चलकर आनंदपुर साहिब बनी।",
   "उनकी वाणी को गुरु गोबिंद सिंह ने गुरु ग्रंथ साहिब में जोड़ा।"],
  C3, 2,
  "All three are correct. The ninth Sikh Guru was executed at Chandni Chowk, where Gurdwara Sis Ganj now stands, after he refused to give up his faith and took up the cause of Kashmiri Pandits facing forced conversion. "
  "In 1665 he founded Chak Nanaki, which became Anandpur Sahib. "
  "Guru Gobind Singh included his hymns in the final version of the Adi Granth, prepared at Damdama Sahib, so the scripture carries the words of six Gurus.",
  "तीनों कथन सही हैं। नौवें सिख गुरु को चाँदनी चौक में, जहाँ अब गुरुद्वारा शीश गंज है, मृत्युदंड दिया गया, क्योंकि उन्होंने अपना धर्म छोड़ने से मना किया और जबरन धर्मांतरण झेल रहे कश्मीरी पंडितों का पक्ष लिया। "
  "1665 में उन्होंने चक नानकी बसाया, जो आनंदपुर साहिब बना। "
  "गुरु गोबिंद सिंह ने दमदमा साहिब में तैयार आदि ग्रंथ के अंतिम रूप में उनकी वाणी शामिल की; इसलिए इस ग्रंथ में छह गुरुओं की वाणी है।",
  f"{SC_} -- Aurangzeb and the Sikhs; {NCM}.",
  "medieval-guru-tegh-bahadur", craft="recall")

M(MD, "easy", "Suraj Mal, who built the Lohagarh fort and expanded his kingdom in the mid-eighteenth century, was a ruler of the",
  "सूरजमल, जिन्होंने लोहागढ़ किला बनवाया और अठारहवीं सदी के मध्य में अपने राज्य का विस्तार किया, किसके शासक थे?",
  ["Jats of Bharatpur", "Rohillas of Rampur", "Sikhs of Patiala", "Marathas of Gwalior"],
  ["भरतपुर के जाट", "रामपुर के रोहिल्ला", "पटियाला के सिख", "ग्वालियर के मराठा"],
  0,
  "Suraj Mal (ruled c. 1756-63) built the Jat state of Bharatpur into a strong power around Agra and Mathura; his Lohagarh ('iron fort') at Bharatpur later withstood a long British siege in 1805. "
  "He was killed in 1763 fighting the Rohilla chief Najib-ud-daula. The Rohillas held Rohilkhand, Phulkian Sikh chiefs ruled Patiala, and the Scindias ruled from Gwalior.",
  "सूरजमल (शासन लगभग 1756-63) ने भरतपुर के जाट राज्य को आगरा और मथुरा के आसपास एक मज़बूत शक्ति बनाया; भरतपुर का उनका लोहागढ़ ('लौह दुर्ग') आगे चलकर 1805 में अंग्रेज़ों के लंबे घेरे के सामने भी टिका रहा। "
  "1763 में रोहिल्ला सरदार नजीबुद्दौला से लड़ते हुए वे मारे गए। रोहिल्ला रुहेलखंड पर, फुलकियाँ सिख सरदार पटियाला पर और सिंधिया ग्वालियर से शासन करते थे।",
  f"{SC_} -- the Jats and the regional powers of the eighteenth century.",
  "medieval-suraj-mal-bharatpur", craft="recall")

S(MD, "medium", "Consider the following statements about the regional states of eighteenth-century India:",
  "अठारहवीं सदी के भारत के क्षेत्रीय राज्यों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The autonomous state of Hyderabad was founded by Murshid Quli Khan.",
   "The autonomous state of Awadh was founded by Alivardi Khan.",
   "At the battle of Colachel in 1741, the Dutch East India Company defeated Travancore."],
  ["हैदराबाद के स्वायत्त राज्य की स्थापना मुर्शिद कुली ख़ाँ ने की।",
   "अवध के स्वायत्त राज्य की स्थापना अलीवर्दी ख़ाँ ने की।",
   "1741 में कोलाचेल के युद्ध में डच ईस्ट इंडिया कंपनी ने त्रावणकोर को हराया।"],
  C3, 3,
  "None is correct. Hyderabad was founded by Nizam-ul-Mulk Asaf Jah in 1724; Murshid Quli Khan began the autonomous rule of Bengal. "
  "Awadh's autonomous rule began with Saadat Khan Burhan-ul-Mulk, appointed governor in 1722; Alivardi Khan was a later Nawab of Bengal. "
  "At Colachel it was Marthanda Varma of Travancore who defeated the Dutch -- a rare defeat of a European company by an Indian state in that century -- and the Dutch commander Eustachius De Lannoy later served in Travancore's army.",
  "कोई भी कथन सही नहीं है। हैदराबाद की स्थापना 1724 में निज़ाम-उल-मुल्क आसफ़ जाह ने की; मुर्शिद कुली ख़ाँ ने बंगाल में स्वायत्त शासन की नींव रखी। "
  "अवध में स्वायत्त शासन 1722 में सूबेदार बने सआदत ख़ाँ बुरहान-उल-मुल्क से शुरू हुआ; अलीवर्दी ख़ाँ बंगाल के बाद के नवाब थे। "
  "कोलाचेल में त्रावणकोर के मार्तंड वर्मा ने डचों को हराया, जो उस सदी में किसी भारतीय राज्य के हाथों यूरोपीय कंपनी की दुर्लभ हार थी; डच सेनापति यूस्टेकियस डी लैनॉय बाद में त्रावणकोर की सेना में सेवा करने लगा।",
  f"{SC_} -- the successor states of the Mughal empire; {BC}.",
  "medieval-successor-states-hyderabad-awadh-travancore", craft="precision")

# ================================================================ MUSIC & DANCE (1)
P(MU, "easy", "Consider the following pairs of folk music traditions and the regions they belong to:",
  "लोक संगीत परंपराओं और उनके क्षेत्रों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Pandavani : Chhattisgarh", "Baul : Bengal", "Maand : Rajasthan", "Burrakatha : Andhra Pradesh"],
  ["पंडवानी : छत्तीसगढ़", "बाउल : बंगाल", "मांड : राजस्थान", "बुर्रकथा : आंध्र प्रदेश"],
  3,
  "All four pairs are correct. Pandavani is a sung narration of the Mahabharata from Chhattisgarh, made famous by Teejan Bai. "
  "The Bauls are wandering mystic singers of Bengal; their tradition is on UNESCO's list of intangible cultural heritage. "
  "Maand is a Rajasthani singing style linked with the old royal courts, 'Kesariya Balam' being its best-known song. "
  "Burrakatha is a storytelling form of Andhra Pradesh in which the lead narrator plays a tambura, with two companions on drums.",
  "चारों युग्म सही हैं। पंडवानी छत्तीसगढ़ में महाभारत के गायन-कथन की परंपरा है, जिसे तीजन बाई ने प्रसिद्ध किया। "
  "बाउल बंगाल के घुमक्कड़ रहस्यवादी गायक हैं; उनकी परंपरा यूनेस्को की अमूर्त सांस्कृतिक विरासत सूची में है। "
  "मांड राजस्थान की एक गायन शैली है जो पुराने राजदरबारों से जुड़ी है; 'केसरिया बालम' इसका सबसे प्रसिद्ध गीत है। "
  "बुर्रकथा आंध्र प्रदेश का कथा-वाचन रूप है जिसमें मुख्य कथावाचक तंबूरा बजाता है और दो साथी ढोल बजाते हैं।",
  f"{SNA}; UNESCO -- Representative List of the Intangible Cultural Heritage of Humanity.",
  "art-folk-music-pandavani-baul-maand-burrakatha", craft="recall")

# ================================================================ MODERN (6)
S(MO, "medium", "Consider the following statements about revolts by Indian soldiers and sailors under British rule:",
  "ब्रिटिश शासन के दौरान भारतीय सैनिकों और नौसैनिकों के विद्रोहों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Vellore mutiny of 1806 was provoked partly by new dress rules that banned caste marks and ordered a new turban.",
   "The Barrackpore mutiny of 1824 ended peacefully after the Company withdrew its order to join the war in Burma.",
   "The Royal Indian Navy revolt of 1946 was backed by the Congress leadership, which urged the ratings to continue the strike."],
  ["1806 का वेल्लोर विद्रोह आंशिक रूप से उन नए पहनावा-नियमों के कारण भड़का जिनमें जाति-चिह्नों पर रोक और नई पगड़ी का आदेश था।",
   "1824 का बैरकपुर विद्रोह तब शांति से समाप्त हो गया जब कंपनी ने बर्मा युद्ध में जाने का आदेश वापस ले लिया।",
   "1946 के रॉयल इंडियन नेवी विद्रोह को कांग्रेस नेतृत्व का समर्थन था, जिसने नौसैनिकों से हड़ताल जारी रखने को कहा।"],
  C3, 0,
  "Only statement 1 is correct. At Vellore the sepoys also resented a round turban that looked like a European hat; the sons of Tipu Sultan, held in the fort, became a rallying point, and the revolt was crushed within hours by cavalry from Arcot. "
  "At Barrackpore the 47th Native Infantry refused to go to the Burma war, fearing loss of caste on a sea voyage and lacking transport; the Company answered with artillery fire, killing many, and disbanded the regiment. "
  "The 1946 naval revolt began on HMIS Talwar in Bombay and spread to Karachi and other ports, but the Congress and League leaders did not back it: Sardar Patel and M.A. Jinnah persuaded the ratings to surrender, though Aruna Asaf Ali supported them.",
  "केवल कथन 1 सही है। वेल्लोर में सिपाही यूरोपीय टोप जैसी दिखने वाली एक गोल पगड़ी से भी नाराज़ थे; क़िले में रखे गए टीपू सुल्तान के पुत्र एकजुटता का केंद्र बने, और अर्काट से आई घुड़सवार सेना ने कुछ ही घंटों में विद्रोह कुचल दिया। "
  "बैरकपुर में 47वीं नेटिव इन्फ़ैंट्री ने बर्मा युद्ध में जाने से मना किया, क्योंकि उन्हें समुद्र-यात्रा से जाति छिनने का डर था और परिवहन के साधन भी नहीं थे; कंपनी ने तोपों से गोलियाँ चलवाईं, जिसमें अनेक मारे गए, और रेजिमेंट भंग कर दी। "
  "1946 का नौसैनिक विद्रोह बंबई में HMIS तलवार से शुरू होकर कराची और अन्य बंदरगाहों तक फैला, पर कांग्रेस और लीग के नेताओं ने इसका साथ नहीं दिया: सरदार पटेल और एम.ए. जिन्ना ने नौसैनिकों को आत्मसमर्पण के लिए मनाया, यद्यपि अरुणा आसफ़ अली ने उनका समर्थन किया।",
  f"{BC}; {SB}.",
  "modern-vellore-barrackpore-rin-revolts", craft="precision")

M(MO, "medium", "Which one of the following commissions recommended dividing the civil services into Imperial, Provincial and Subordinate services?",
  "निम्नलिखित में से किस आयोग ने सिविल सेवाओं को इंपीरियल, प्रांतीय और अधीनस्थ सेवाओं में बाँटने की सिफ़ारिश की?",
  ["Aitchison Commission (1886)", "Islington Commission (1912)", "Raleigh Commission (1902)", "Hunter Commission (1882)"],
  ["एचिसन आयोग (1886)", "इस्लिंगटन आयोग (1912)", "रैले आयोग (1902)", "हंटर आयोग (1882)"],
  0,
  "The Public Service Commission under Sir Charles Aitchison (1886-87) proposed the three tiers of Imperial, Provincial and Subordinate services and the end of the short-lived Statutory Civil Service. "
  "The Islington Royal Commission (1912-15) examined how far the services should be opened to Indians; the Raleigh Commission (1902) reviewed the universities; the Hunter Commission (1882) reviewed education.",
  "सर चार्ल्स एचिसन की अध्यक्षता वाले लोक सेवा आयोग (1886-87) ने इंपीरियल, प्रांतीय और अधीनस्थ सेवाओं के तीन स्तरों तथा अल्पकालिक स्टैच्यूटरी सिविल सर्विस को समाप्त करने का प्रस्ताव रखा। "
  "इस्लिंगटन शाही आयोग (1912-15) ने जाँचा कि सेवाएँ भारतीयों के लिए कितनी खोली जाएँ; रैले आयोग (1902) ने विश्वविद्यालयों की और हंटर आयोग (1882) ने शिक्षा की समीक्षा की।",
  f"{BC} -- the civil services under the Crown.",
  "modern-aitchison-commission-services", craft="recall")

S(MO, "hard", "Consider the following statements about nineteenth-century movements in eastern India:",
  "उन्नीसवीं सदी में पूर्वी भारत के आंदोलनों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Wahabi movement in India was led by Syed Ahmad of Rae Bareli, and Patna became one of its main centres.",
   "The Faraizi movement was founded by Haji Shariatullah in eastern Bengal.",
   "The agrarian leagues of Pabna in the 1870s used armed attacks on officials and demanded an end to British rule."],
  ["भारत में वहाबी आंदोलन का नेतृत्व रायबरेली के सैयद अहमद ने किया, और पटना इसका एक प्रमुख केंद्र बना।",
   "फ़राइज़ी आंदोलन की स्थापना हाजी शरीयतुल्लाह ने पूर्वी बंगाल में की।",
   "1870 के दशक में पबना के कृषक संघों ने अधिकारियों पर सशस्त्र हमले किए और ब्रिटिश शासन की समाप्ति की माँग की।"],
  C3, 1,
  "Statements 1 and 2 are correct. Syed Ahmad Barelvi -- not Sir Syed Ahmad Khan -- led a revivalist movement that fought the Sikh kingdom in the north-west and later the British; Patna was its organising centre until the Wahabi trials of the 1860s. "
  "Haji Shariatullah began the Faraizi movement to purify religious practice among Bengal's peasants; under his son Dudu Miyan it turned against zamindars and indigo planters. "
  "Statement 3 is wrong: the Pabna tenants of 1873 relied on rent strikes, petitions and lawsuits, not armed attacks, and declared that they wanted to be the Queen's own ryots; their struggle fed into the Bengal Tenancy Act of 1885.",
  "कथन 1 और 2 सही हैं। सैयद अहमद बरेलवी ने, न कि सर सैयद अहमद ख़ाँ ने, एक पुनरुत्थानवादी आंदोलन चलाया जो उत्तर-पश्चिम में सिख राज्य से और बाद में अंग्रेज़ों से लड़ा; 1860 के दशक के वहाबी मुक़दमों तक पटना इसका संगठन केंद्र रहा। "
  "हाजी शरीयतुल्लाह ने बंगाल के किसानों में धार्मिक आचरण की शुद्धि के लिए फ़राइज़ी आंदोलन शुरू किया; उनके पुत्र दूदू मियाँ के समय यह ज़मींदारों और नील बागान मालिकों के विरुद्ध हो गया। "
  "कथन 3 गलत है: 1873 के पबना के काश्तकारों ने सशस्त्र हमलों के बजाय लगान-हड़ताल, याचिकाओं और मुक़दमों का सहारा लिया और घोषणा की कि वे महारानी के ही रैयत बनना चाहते हैं; उनके संघर्ष ने 1885 के बंगाल काश्तकारी अधिनियम की राह बनाई।",
  f"{BC} -- peasant and religious movements; {SB}.",
  "modern-wahabi-faraizi-pabna", craft="precision")

M(MO, "medium", "Which one of the following institutions was founded by Pandita Ramabai?",
  "निम्नलिखित में से किस संस्था की स्थापना पंडिता रमाबाई ने की?",
  ["Sharada Sadan, a school for widows", "Seva Sadan, a women's welfare society", "Bharat Stree Mahamandal", "Women's Indian Association"],
  ["शारदा सदन, विधवाओं के लिए एक विद्यालय", "सेवा सदन, एक महिला कल्याण संस्था", "भारत स्त्री महामंडल", "विमेंस इंडियन एसोसिएशन"],
  0,
  "Pandita Ramabai opened the Sharada Sadan in Bombay in 1889, later moving it to Pune, to educate widows; she had earlier founded the Arya Mahila Samaj and later set up the Mukti Mission at Kedgaon. "
  "Seva Sadan was started in Bombay by Behramji Malabari and Dayaram Gidumal (1908), the Bharat Stree Mahamandal by Sarala Devi Chaudhurani (1910), and the Women's Indian Association at Madras by Annie Besant, Margaret Cousins and others (1917).",
  "पंडिता रमाबाई ने विधवाओं की शिक्षा के लिए 1889 में बंबई में शारदा सदन खोला, जिसे बाद में पुणे ले जाया गया; इससे पहले उन्होंने आर्य महिला समाज की स्थापना की थी और बाद में केडगाँव में मुक्ति मिशन बनाया। "
  "सेवा सदन बंबई में बहरामजी मालाबारी और दयाराम गिदूमल ने (1908), भारत स्त्री महामंडल सरला देवी चौधुरानी ने (1910) और विमेंस इंडियन एसोसिएशन मद्रास में एनी बेसेंट, मार्गरेट कज़िन्स और अन्य ने (1917) शुरू किया।",
  f"{BC} -- social reform and women's movements; {SB}.",
  "modern-pandita-ramabai-sharada-sadan", craft="recall")

S(MO, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["V.O. Chidambaram Pillai founded the Swadeshi Steam Navigation Company at Tuticorin.",
   "The Bombay Plan of 1944 was drawn up by leaders of the Communist Party of India."],
  ["वी.ओ. चिदंबरम पिल्लई ने तूतीकोरिन में स्वदेशी स्टीम नेविगेशन कंपनी की स्थापना की।",
   "1944 की बॉम्बे योजना भारतीय कम्युनिस्ट पार्टी के नेताओं ने तैयार की थी।"],
  T2, 0,
  "Only statement 1 is correct. The Swadeshi Steam Navigation Company (1906) ran Indian-owned ships between Tuticorin and Colombo in defiance of the British India Steam Navigation Company; Chidambaram Pillai was later jailed for sedition. "
  "The Bombay Plan (1944) was prepared by leading industrialists, among them J.R.D. Tata, G.D. Birla and Purushottamdas Thakurdas, and it proposed a large role for the state in planned industrial growth.",
  "केवल कथन 1 सही है। स्वदेशी स्टीम नेविगेशन कंपनी (1906) ने ब्रिटिश इंडिया स्टीम नेविगेशन कंपनी को चुनौती देते हुए तूतीकोरिन और कोलंबो के बीच भारतीय स्वामित्व वाले जहाज़ चलाए; चिदंबरम पिल्लई को बाद में राजद्रोह के आरोप में जेल हुई। "
  "बॉम्बे योजना (1944) जे.आर.डी. टाटा, जी.डी. बिड़ला और पुरुषोत्तमदास ठाकुरदास जैसे प्रमुख उद्योगपतियों ने तैयार की थी, और इसमें नियोजित औद्योगिक विकास में राज्य की बड़ी भूमिका का प्रस्ताव था।",
  f"{BC} -- the Swadeshi movement and economic nationalism; {SB}.",
  "modern-swadeshi-steam-bombay-plan", craft="recall")

M(MO, "hard", "The Famine Codes framed by the provinces in the 1880s were based on the recommendations of the Famine Commission headed by",
  "1880 के दशक में प्रांतों द्वारा बनाई गई अकाल संहिताएँ (Famine Codes) किसकी अध्यक्षता वाले अकाल आयोग की सिफ़ारिशों पर आधारित थीं?",
  ["Richard Strachey", "Antony MacDonnell", "James Lyall", "Lord Lytton"],
  ["रिचर्ड स्ट्रेची", "एंटनी मैकडॉनेल", "जेम्स लायल", "लॉर्ड लिटन"],
  0,
  "The first Famine Commission (1880), appointed while Lord Lytton was Viceroy after the great famine of 1876-78, was chaired by Sir Richard Strachey. "
  "It laid down the principles of relief -- public works to provide wages, free relief for those unable to work, and suspension of land revenue -- that the provinces turned into Famine Codes from 1883. "
  "Later commissions under James Lyall (1898) and Antony MacDonnell (1901) reviewed the famines of 1896-97 and 1899-1900.",
  "पहला अकाल आयोग (1880), जो 1876-78 के भीषण अकाल के बाद लॉर्ड लिटन के वायसराय रहते नियुक्त हुआ, सर रिचर्ड स्ट्रेची की अध्यक्षता में था। "
  "इसने राहत के सिद्धांत तय किए, जैसे मज़दूरी देने के लिए सार्वजनिक निर्माण कार्य, काम न कर सकने वालों को मुफ़्त राहत और भू-राजस्व की वसूली रोकना, जिन्हें प्रांतों ने 1883 से अकाल संहिताओं का रूप दिया। "
  "बाद में जेम्स लायल (1898) और एंटनी मैकडॉनेल (1901) के आयोगों ने 1896-97 और 1899-1900 के अकालों की समीक्षा की।",
  f"{BC} -- famines and the economic critique of British rule.",
  "modern-famine-commission-strachey", craft="recall")

if __name__ == "__main__":
    write_updates("gs_l2_t21_history_v2.sql")
