# -*- coding: utf-8 -*-
"""Current Affairs · Test 2 (April to June 2026) -- part F: History, Art and Culture.

Anniversaries of April-June 2026: five hundred years of the First Battle of Panipat (21 April 1526), 450 years of
Haldighati (18 June 1576), seventy-five years of Bhoodan (18 April 1951), fifty years of Doordarshan as a service
separate from All India Radio (1 April 1976), May Day and Ambedkar's years as Labour Member, and the 'gates of
Somnath' of 1842 recalled in the seventy-fifth year of the temple's reconsecration. Every fact was searched in the
whole UPSC bank and is one no row tests."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, C, write
from polity_common import C3, C4, T2
from ca_common import MX, finish
from ca_t2_format import FORMAT, POS

d.SUBJECT = "History"
d.REQUIRE_CRAFT = True
AN, MD, MO, CU = "Ancient", "Medieval", "Modern", "Culture-Other"

S(MD, "medium", "21 April 2026 marked five hundred years of the First Battle of Panipat. Consider the following statements about Babur:",
  "21 अप्रैल 2026 को पानीपत की पहली लड़ाई के पाँच सौ वर्ष पूरे हुए। बाबर के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["He was descended from Chingiz Khan on his father's side and from Timur on his mother's.",
   "He took the title Padshah only after his victory at Panipat.",
   "He wrote his memoirs in Persian, the court language of the Delhi Sultanate."],
  ["वह पिता की ओर से चंगेज़ ख़ाँ का और माता की ओर से तैमूर का वंशज था।",
   "उसने पादशाह की उपाधि पानीपत की विजय के बाद ही ली।",
   "उसने अपने संस्मरण दिल्ली सल्तनत की दरबारी भाषा फ़ारसी में लिखे।"],
  C3, 3,
  "None of the statements is correct. Statement 1 reverses the lines of descent: the Mughals traced their descent from two great Central Asian rulers -- Timur through Babur's father and Chingiz Khan through his mother -- though they called themselves Timurids, since Chingiz was remembered for his massacres. Statement 2 is wrong too: driven out of Ferghana and Samarkand by the Uzbeks, Babur took Kabul in 1504 and, ruling from there, took the title Padshah in 1507 -- a claim to sovereignty equal to that of the Ottoman Sultan and the Safavid Shah -- long before he defeated Ibrahim Lodi at Panipat on 21 April 1526. "
  "Statement 3 is wrong: the Baburnama was written in Chagatai Turkish, Babur's mother tongue. It was translated into Persian in 1589 at Akbar's order by Abdur Rahim Khan-i-Khanan, and illustrated copies of the translation were made in the imperial workshop.",
  "कोई भी कथन सही नहीं है। कथन 1 वंश-रेखाओं को उलट देता है: मुग़ल अपना वंश मध्य एशिया के दो महान शासकों से जोड़ते थे -- बाबर के पिता के माध्यम से तैमूर से और माता के माध्यम से चंगेज़ ख़ाँ से -- पर वे स्वयं को तैमूरी कहते थे, क्योंकि चंगेज़ को उसके नरसंहारों के लिए याद किया जाता था। कथन 2 भी ग़लत है: उज़बेकों द्वारा फ़रग़ना और समरक़ंद से खदेड़े गए बाबर ने 1504 में काबुल लिया और वहाँ से शासन करते हुए 1507 में पादशाह की उपाधि ली -- उस्मानी सुल्तान और सफ़वी शाह के बराबर संप्रभुता का दावा -- 21 अप्रैल 1526 को पानीपत में इब्राहिम लोदी को हराने से बहुत पहले। "
  "कथन 3 ग़लत है: बाबरनामा बाबर की मातृभाषा चग़ताई तुर्की में लिखा गया। अकबर के आदेश पर 1589 में अब्दुर्रहीम ख़ान-ए-ख़ानाँ ने उसका फ़ारसी में अनुवाद किया, और शाही कार्यशाला में इस अनुवाद की सचित्र प्रतियाँ बनीं।",
  "NCERT, Themes in Indian History Part II (Class XII), Chapter 9 (Kings and Chronicles); NCERT, Our Pasts II (Class VII), Chapter 4 (The Mughal Empire).",
  "ca-t2-his-panipat-500-babur-padshah-chagatai", craft="precision")

S(MD, "medium", "18 June 2026 marked 450 years of the Battle of Haldighati. Consider the following statements:",
  "18 जून 2026 को हल्दीघाटी की लड़ाई के 450 वर्ष पूरे हुए। निम्नलिखित कथनों पर विचार कीजिए:",
  ["Akbar himself commanded the Mughal army in the battle.",
   "An Afghan, Hakim Khan Sur, led a contingent on Maharana Pratap's side.",
   "Before his death Pratap recaptured Chittor, which Akbar had taken in 1568.",
   "In his later years Pratap ruled from Chavand."],
  ["लड़ाई में मुग़ल सेना की कमान स्वयं अकबर के हाथ में थी।",
   "एक अफ़ग़ान, हकीम ख़ाँ सूर, ने महाराणा प्रताप की ओर से एक टुकड़ी का नेतृत्व किया।",
   "अपनी मृत्यु से पहले प्रताप ने चित्तौड़ फिर जीत लिया, जिसे अकबर ने 1568 में लिया था।",
   "अपने अंतिम वर्षों में प्रताप ने चावंड से शासन किया।"],
  C4, 1,
  "Statements 2 and 4 are correct. Statement 1 is wrong: Akbar did not take the field himself but sent Man Singh of Amber, a Kachhwaha Rajput, at the head of the Mughal force, while Pratap's army included the Afghan Hakim Khan Sur, who led its vanguard and fell in the battle, and Bhil archers under Rana Punja -- so the battle of 18 June 1576 was no simple contest of one faith against another. The Mughals held the field but failed to capture Pratap, who withdrew into the hills and kept up the resistance. "
  "Statement 3 is wrong: Chittor, taken by Akbar after the siege of 1567-68, was never recovered by Pratap; he won back much of Mewar and ruled from Chavand, where he died in 1597. Mewar accepted Mughal suzerainty only under his son Amar Singh, by the treaty of 1615 with Jahangir.",
  "कथन 2 और 4 सही हैं। कथन 1 ग़लत है: अकबर स्वयं युद्ध में नहीं उतरा, उसने मुग़ल सेना के प्रमुख के रूप में आमेर के कछवाहा राजपूत मानसिंह को भेजा, जबकि प्रताप की सेना में अफ़ग़ान हकीम ख़ाँ सूर था, जिसने हरावल का नेतृत्व किया और लड़ाई में मारा गया, और राणा पूँजा के अधीन भील तीरंदाज़ थे -- इसलिए 18 जून 1576 की लड़ाई एक धर्म के विरुद्ध दूसरे धर्म का सीधा संघर्ष नहीं थी। मुग़लों ने मैदान तो जीता पर प्रताप को पकड़ नहीं सके, जो पहाड़ियों में हटकर प्रतिरोध जारी रखे रहे। "
  "कथन 3 ग़लत है: 1567-68 के घेरे के बाद अकबर द्वारा लिया गया चित्तौड़ प्रताप कभी वापस नहीं ले सके; उन्होंने मेवाड़ का बड़ा भाग फिर जीता और चावंड से शासन किया, जहाँ 1597 में उनकी मृत्यु हुई। मेवाड़ ने मुग़ल अधिराज्य उनके पुत्र अमर सिंह के समय, 1615 में जहाँगीर के साथ संधि से, स्वीकार किया।",
  "NCERT, Our Pasts II (Class VII), Chapter 4 (The Mughal Empire); NCERT, Themes in Indian History Part II (Class XII), Chapter 9 (Kings and Chronicles).",
  "ca-t2-his-haldighati-450-hakim-khan-chavand", craft="multi")

S(MO, "hard", "18 April 2026 marked seventy-five years of the Bhoodan movement. Consider the following statements:",
  "18 अप्रैल 2026 को भूदान आंदोलन के पचहत्तर वर्ष पूरे हुए। निम्नलिखित कथनों पर विचार कीजिए:",
  ["It began at Pochampally, in a region then in the grip of a communist-led peasant uprising.",
   "Under Gramdan, the ownership of a village's land was to pass to the village community as a whole.",
   "The first village to be given in Gramdan was Mangroth, in Uttar Pradesh."],
  ["यह पोचमपल्ली से शुरू हुआ, जो उस समय कम्युनिस्टों के नेतृत्व वाले किसान विद्रोह की चपेट में आए क्षेत्र में था।",
   "ग्रामदान के अंतर्गत गाँव की भूमि का स्वामित्व पूरे ग्राम समुदाय को जाना था।",
   "ग्रामदान में दिया गया पहला गाँव उत्तर प्रदेश का मंगरौठ था।"],
  C3, 2,
  "All three statements are correct. Vinoba Bhave was touring Telangana, then the scene of the communist-led armed struggle of peasants against landlords, when on 18 April 1951, at Pochampally in Nalgonda district, landless families asked him for land; a local landowner, V. Ramachandra Reddy, offered 100 acres, and the idea of asking landowners to give a share of their land as a gift -- bhoodan -- was born as a non-violent answer to agrarian unrest. "
  "From 1952 the movement grew into Gramdan, the gift of a whole village. Mangroth, in Hamirpur district of Uttar Pradesh, was the first; a village counted as gramdan when at least three-quarters of its residents, holding at least half of its land, agreed in writing to vest ownership in the village community. Several States passed Bhoodan Yagna Acts to receive and distribute the donated land.",
  "तीनों कथन सही हैं। विनोबा भावे तेलंगाना का दौरा कर रहे थे, जो उस समय ज़मींदारों के विरुद्ध कम्युनिस्टों के नेतृत्व वाले किसानों के सशस्त्र संघर्ष का क्षेत्र था, जब 18 अप्रैल 1951 को नलगोंडा ज़िले के पोचमपल्ली में भूमिहीन परिवारों ने उनसे भूमि माँगी; एक स्थानीय भूस्वामी, वी. रामचंद्र रेड्डी, ने 100 एकड़ देने का प्रस्ताव किया, और भूस्वामियों से अपनी भूमि का एक भाग दान में देने को कहने का विचार -- भूदान -- कृषि असंतोष के अहिंसक उत्तर के रूप में जन्मा। "
  "1952 से आंदोलन ग्रामदान, यानी पूरे गाँव के दान, में बढ़ा। उत्तर प्रदेश के हमीरपुर ज़िले का मंगरौठ पहला था; कोई गाँव ग्रामदान तब माना जाता था जब उसके कम से कम तीन-चौथाई निवासी, जिनके पास उसकी कम से कम आधी भूमि हो, स्वामित्व ग्राम समुदाय को सौंपने पर लिखित सहमति दें। कई राज्यों ने दान में मिली भूमि लेने और बाँटने के लिए भूदान यज्ञ अधिनियम बनाए।",
  "Government of Telangana, Bhoodan Pochampally; Gandhi Smriti and Darshan Samiti, on Vinoba Bhave and the Bhoodan and Gramdan movements.",
  "ca-t2-his-bhoodan-75-pochampally-gramdan-mangroth", craft="linkage")

S(CU, "easy", "1 April 2026 marked fifty years of Doordarshan as a service separate from All India Radio. Consider the following statements:",
  "1 अप्रैल 2026 को आकाशवाणी से अलग सेवा के रूप में दूरदर्शन के पचास वर्ष पूरे हुए। निम्नलिखित कथनों पर विचार कीजिए:",
  ["Television in India began in 1959 as an experimental service of All India Radio in Delhi.",
   "Doordarshan was separated from All India Radio when the Prasar Bharati Act came into force.",
   "Prasar Bharati, which runs both Doordarshan and All India Radio, is a statutory body."],
  ["भारत में टेलीविज़न 1959 में दिल्ली में आकाशवाणी की एक प्रायोगिक सेवा के रूप में शुरू हुआ।",
   "दूरदर्शन को आकाशवाणी से तब अलग किया गया जब प्रसार भारती अधिनियम लागू हुआ।",
   "दूरदर्शन और आकाशवाणी दोनों का संचालन करने वाला प्रसार भारती एक सांविधिक निकाय है।"],
  C3, 1,
  "Statements 1 and 3 are correct. Television began on 15 September 1959 as an experimental service from a small studio in Delhi under All India Radio, and a regular daily service followed in 1965. Prasar Bharati is the corporation created by the Prasar Bharati (Broadcasting Corporation of India) Act, 1990, which now runs both broadcasters. "
  "Statement 2 is wrong: Doordarshan became a separate department under its own Director-General on 1 April 1976, still within the Ministry of Information and Broadcasting. The Prasar Bharati Act, passed in 1990 to give public broadcasting autonomy, came into force only on 23 November 1997, when Doordarshan and All India Radio both passed to the new corporation.",
  "कथन 1 और 3 सही हैं। टेलीविज़न 15 सितंबर 1959 को आकाशवाणी के अधीन दिल्ली के एक छोटे स्टूडियो से प्रायोगिक सेवा के रूप में शुरू हुआ, और 1965 में नियमित दैनिक सेवा आई। प्रसार भारती, प्रसार भारती (भारतीय प्रसारण निगम) अधिनियम, 1990 से बना निगम है, जो अब दोनों प्रसारकों का संचालन करता है। "
  "कथन 2 ग़लत है: दूरदर्शन 1 अप्रैल 1976 को अपने महानिदेशक के अधीन एक अलग विभाग बना, फिर भी सूचना और प्रसारण मंत्रालय के भीतर ही। लोक प्रसारण को स्वायत्तता देने के लिए 1990 में पारित प्रसार भारती अधिनियम 23 नवंबर 1997 को ही लागू हुआ, जब दूरदर्शन और आकाशवाणी दोनों नए निगम को सौंपे गए।",
  "Prasar Bharati (Broadcasting Corporation of India) Act, 1990; Ministry of Information and Broadcasting and Prasar Bharati, history of Doordarshan.",
  "ca-t2-his-doordarshan-50-prasar-bharati-1997", craft="precision")

S(MO, "medium", "May Day 2026 brought renewed attention to B. R. Ambedkar's role in Indian labour law. Consider the following statements:",
  "मई दिवस 2026 ने भारतीय श्रम क़ानून में बी. आर. आंबेडकर की भूमिका की ओर फिर ध्यान खींचा। निम्नलिखित कथनों पर विचार कीजिए:",
  ["As Labour Member of the Viceroy's Executive Council, he announced at the Indian Labour Conference of 1942 that working hours would be cut to eight a day.",
   "He held the Labour portfolio in the Interim Government formed in September 1946."],
  ["वायसराय की कार्यकारी परिषद के श्रम सदस्य के रूप में उन्होंने 1942 के भारतीय श्रम सम्मेलन में घोषणा की कि काम के घंटे घटाकर आठ प्रतिदिन किए जाएँगे।",
   "सितंबर 1946 में बनी अंतरिम सरकार में श्रम विभाग उनके पास था।"],
  T2, 0,
  "Only statement 1 is correct. Ambedkar served as Labour Member from July 1942 to 1946. At the seventh session of the Indian Labour Conference, in New Delhi in November 1942, he announced the eight-hour working day; his tenure also brought tripartite labour conferences of government, employers and workers, and his department laid the ground for employment exchanges and for health insurance for industrial workers. "
  "Statement 2 is wrong: in the Interim Government of 2 September 1946, with Jawaharlal Nehru as Vice-President of the Executive Council, the Labour portfolio went to Jagjivan Ram. Ambedkar, elected to the Constituent Assembly from Bengal, became Law Minister in independent India's first cabinet in 1947 and chaired the Drafting Committee.",
  "केवल कथन 1 सही है। आंबेडकर जुलाई 1942 से 1946 तक श्रम सदस्य रहे। नवंबर 1942 में नई दिल्ली में भारतीय श्रम सम्मेलन के सातवें सत्र में उन्होंने आठ घंटे के कार्य-दिवस की घोषणा की; उनके कार्यकाल में सरकार, नियोक्ताओं और श्रमिकों के त्रिपक्षीय श्रम सम्मेलन भी हुए, और उनके विभाग ने रोज़गार कार्यालयों तथा औद्योगिक श्रमिकों के स्वास्थ्य बीमा की नींव रखी। "
  "कथन 2 ग़लत है: 2 सितंबर 1946 की अंतरिम सरकार में, जिसमें जवाहरलाल नेहरू कार्यकारी परिषद के उपाध्यक्ष थे, श्रम विभाग जगजीवन राम को मिला। बंगाल से संविधान सभा में चुने गए आंबेडकर 1947 में स्वतंत्र भारत के पहले मंत्रिमंडल में विधि मंत्री बने और प्रारूप समिति के अध्यक्ष रहे।",
  "Ministry of Labour and Employment, on Dr B. R. Ambedkar and labour reforms; Proceedings of the seventh Indian Labour Conference (November 1942); NCERT, Indian Constitution at Work (Class XI), Chapter 1.",
  "ca-t2-his-ambedkar-labour-member-eight-hour-day", craft="linkage")

S(MO, "hard", "The seventy-fifth anniversary of the reconsecration of the Somnath temple, in May 2026, recalled an episode of 1842. Consider the following statements:",
  "मई 2026 में सोमनाथ मंदिर की पुनर्प्रतिष्ठा की पचहत्तरवीं वर्षगाँठ ने 1842 की एक घटना याद दिलाई। निम्नलिखित कथनों पर विचार कीजिए:",
  ["Governor-General Lord Auckland ordered the 'gates of Somnath' to be brought back from Afghanistan at the end of the First Anglo-Afghan War.",
   "The gates were taken from the tomb of Mahmud of Ghazni.",
   "On examination they proved to be the temple's original sandalwood gates, and they were restored to Somnath."],
  ["गवर्नर-जनरल लॉर्ड ऑकलैंड ने पहले आंग्ल-अफ़ग़ान युद्ध के अंत में ‘सोमनाथ के द्वार’ अफ़ग़ानिस्तान से वापस लाने का आदेश दिया।",
   "ये द्वार महमूद ग़ज़नवी के मक़बरे से लिए गए थे।",
   "जाँच में ये मंदिर के मूल चंदन के द्वार सिद्ध हुए, और इन्हें सोमनाथ में फिर लगा दिया गया।"],
  C3, 0,
  "Only statement 2 is correct. Statement 1 is wrong: Lord Auckland, who had launched the war, was replaced in February 1842 by Lord Ellenborough. After the disastrous retreat from Kabul, a British force under General Nott marched through Ghazni in 1842, and Ellenborough's 'Proclamation of the Gates' announced that the gates of Mahmud's tomb, believed to have been carried off from Somnath in 1026, were being brought home -- an appeal to Indian sentiment that was ridiculed in the British Parliament, notably by Macaulay, and one of the episodes that led to Ellenborough's recall in 1844. "
  "Statement 3 is wrong: the gates were found to be of deodar wood and not of Indian design, so they were not the sandalwood gates of Somnath, and they were never taken to the temple; they still lie in a storeroom of the Agra Fort.",
  "केवल कथन 2 सही है। कथन 1 ग़लत है: युद्ध शुरू करने वाले लॉर्ड ऑकलैंड का स्थान फ़रवरी 1842 में लॉर्ड एलनबरो ने ले लिया था। काबुल से विनाशकारी वापसी के बाद 1842 में जनरल नॉट के अधीन एक ब्रिटिश सेना ग़ज़नी से होकर गुज़री, और एलनबरो की ‘द्वारों की घोषणा’ ने कहा कि महमूद के मक़बरे के द्वार, जिन्हें 1026 में सोमनाथ से ले जाया गया माना जाता था, वापस लाए जा रहे हैं -- भारतीय भावनाओं से की गई यह अपील ब्रिटिश संसद में, विशेषकर मैकाले द्वारा, उपहास का विषय बनी, और 1844 में एलनबरो को वापस बुलाए जाने के कारणों में गिनी गई। "
  "कथन 3 ग़लत है: द्वार देवदार की लकड़ी के और भारतीय शैली से भिन्न पाए गए, इसलिए वे सोमनाथ के चंदन के द्वार नहीं थे, और उन्हें कभी मंदिर नहीं ले जाया गया; वे आज भी आगरा क़िले के एक भंडार-कक्ष में रखे हैं।",
  "Proclamation of Governor-General Lord Ellenborough (1842); Archaeological Survey of India, Agra Fort; NCERT, Our Pasts III (Class VIII), Chapter 2 (From Trade to Territory).",
  "ca-t2-his-somnath-gates-1842-ellenborough", craft="precision")

finish("ca_t2_f.sql", FORMAT, "2026-Q2", update="--update" in sys.argv)
