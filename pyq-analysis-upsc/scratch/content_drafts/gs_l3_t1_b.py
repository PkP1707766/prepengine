# -*- coding: utf-8 -*-
"""Level 3 · Test 1 (GS Integrated Test 1) -- part B: History (16) (upsc_l3_cell_targets.mjs 1).
History cells: Modern e-MCQ, e-stmt, h-stmt, m-MCQ, m-stmt x2; Ancient e-MCQ, e-stmt, h-stmt, m-MCQ, m-stmt x2;
Medieval m-MCQ, m-stmt, m-pairs; Music & Dance h-pairs.
Level 2 holds 417 History rows and Level 1 another 119, covering nearly every standard event, text and site, so every
fact here was grepped against both and is one neither tests: the INA trials at the Red Fort and the naval ratings'
revolt of 1946; Faizpur, Haripura and the States People's Conference; the Wagon Tragedy of the Malabar rising; the Hartog
Committee; Phadke's Ramosis and Bijolia; Puhar; Arretine ware at Arikamedu and the Gatha Saptashati; nigama, sarthavaha
and the karshapana; the Kalabhras of the Velvikudi grant; the Kumaradevi, BODDO and ship-type coins; the Sohgaura and
Mahasthan famine-relief records; Sikandar Lodi's Agra and gaz; Alauddin's dagh and chehra; the revenue methods zabt,
kankut, batai and nasaq; and the khayal gharanas. MCQ keys are pinned (pos)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, write
from polity_common import C3, T2

d.SUBJECT = "History"
d.REQUIRE_CRAFT = True
MOD = "NCERT Class XII, Themes in Indian History III; NCERT (old), Modern India"
OP3 = "NCERT Class VIII, Our Pasts III"
TH1 = "NCERT Class XII, Themes in Indian History I"
OP1 = "NCERT Class VI, Our Pasts I"
OP2 = "NCERT Class VII, Our Pasts II"
TH2 = "NCERT Class XII, Themes in Indian History II"
ASI = "Archaeological Survey of India"
MUS = "NCERT Class XI, An Introduction to Indian Art; Sangeet Natak Akademi"

# ================================================================ MODERN (6)
M("Modern", "easy",
  "The first of the trials of officers of the Indian National Army held at the Red Fort in 1945 was of which three officers?",
  "1945 में लाल क़िले में हुए आज़ाद हिंद फ़ौज के अधिकारियों के मुक़दमों में पहला मुक़दमा किन तीन अधिकारियों का था?",
  ["Mohan Singh, Lakshmi Swaminathan and Subhas Chandra Bose's aide Abid Hasan",
   "Bhagat Singh's associates Batukeshwar Dutt, Jaidev Kapur and Shiv Verma",
   "Rash Behari Bose, Mohan Singh and Prem Kumar Sahgal, the three founders of the army",
   "Shah Nawaz Khan, Prem Kumar Sahgal and Gurbaksh Singh Dhillon"],
  ["मोहन सिंह, लक्ष्मी स्वामीनाथन और सुभाषचंद्र बोस के सहयोगी आबिद हसन",
   "भगत सिंह के साथी बटुकेश्वर दत्त, जयदेव कपूर और शिव वर्मा",
   "रासबिहारी बोस, मोहन सिंह और प्रेम कुमार सहगल, सेना के तीन संस्थापक",
   "शाहनवाज़ ख़ान, प्रेम कुमार सहगल और गुरबख़्श सिंह ढिल्लों"],
  3,
  "Shah Nawaz Khan, Prem Kumar Sahgal and Gurbaksh Singh Dhillon -- a Muslim, a Hindu and a Sikh -- were tried together at the Red Fort from November 1945. The Congress defended them, with Bhulabhai Desai leading the defence, and the trial set off protests across the country that cut across communities; "
  "although they were sentenced to transportation for life, the Commander-in-Chief remitted the sentences in January 1946. The other names belong to the INA's earlier history or to the revolutionaries of the Hindustan Socialist Republican Association.",
  "शाहनवाज़ ख़ान, प्रेम कुमार सहगल और गुरबख़्श सिंह ढिल्लों -- एक मुसलमान, एक हिंदू और एक सिख -- पर नवंबर 1945 से लाल क़िले में एक साथ मुक़दमा चला। कांग्रेस ने उनका बचाव किया, जिसका नेतृत्व भूलाभाई देसाई ने किया, और मुक़दमे ने देश भर में ऐसे विरोध भड़काए जो समुदायों की सीमाएँ लाँघ गए; "
  "यद्यपि उन्हें आजीवन देश-निकाले की सज़ा हुई, प्रधान सेनापति ने जनवरी 1946 में सज़ाएँ माफ़ कर दीं। बाक़ी नाम आज़ाद हिंद फ़ौज के आरंभिक इतिहास या हिंदुस्तान सोशलिस्ट रिपब्लिकन एसोसिएशन के क्रांतिकारियों के हैं।",
  MOD, "l3-t1-his-ina-red-fort-trial", pos=3, craft="recall")

S("Modern", "easy", "With reference to the revolt of the ratings of the Royal Indian Navy in February 1946, consider the following statements:",
  "फ़रवरी 1946 में रॉयल इंडियन नेवी के नाविकों (रेटिंग्स) के विद्रोह के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["It began on HMIS Talwar, a signals training establishment in Bombay, and spread to ships and shore establishments in other ports.",
   "Sardar Vallabhbhai Patel, along with Muhammad Ali Jinnah, persuaded the ratings to surrender."],
  ["यह बंबई में एक सिग्नल प्रशिक्षण प्रतिष्ठान, एचएमआईएस तलवार, पर आरंभ हुआ और दूसरे बंदरगाहों के जहाज़ों और तटीय प्रतिष्ठानों में फैल गया।",
   "सरदार वल्लभभाई पटेल ने मुहम्मद अली जिन्ना के साथ नाविकों को आत्मसमर्पण के लिए राज़ी किया।"],
  T2, 2,
  "Both are correct. On 18 February 1946 ratings of HMIS Talwar struck against poor food, racial insults and the INA trials, and the revolt spread to Karachi, Calcutta and other ports, with the flags of the Congress, the Muslim League and the Communists hoisted together on the ships. "
  "The Congress and League leaders, wary of an uprising they did not control, advised surrender: on 23 February the ratings gave in after assurances from Patel and Jinnah that they would not be victimised.",
  "दोनों सही हैं। 18 फ़रवरी 1946 को एचएमआईएस तलवार के नाविकों ने ख़राब भोजन, नस्ली अपमान और आज़ाद हिंद फ़ौज के मुक़दमों के विरोध में हड़ताल की, और विद्रोह कराची, कलकत्ता और दूसरे बंदरगाहों में फैल गया, जहाँ जहाज़ों पर कांग्रेस, मुस्लिम लीग और कम्युनिस्टों के झंडे एक साथ फहराए गए। "
  "कांग्रेस और लीग के नेताओं ने, उस विद्रोह से सावधान जो उनके नियंत्रण में नहीं था, आत्मसमर्पण की सलाह दी: 23 फ़रवरी को पटेल और जिन्ना के इस आश्वासन के बाद नाविकों ने हथियार डाल दिए कि उन्हें प्रताड़ित नहीं किया जाएगा।",
  MOD, "l3-t1-his-rin-ratings-revolt-1946", craft="recall")

S("Modern", "hard", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Faizpur session of 1936 was the first session of the Indian National Congress to be held in a village.",
   "At Haripura in 1938, the Congress resolved that it would itself launch and lead mass struggles against the rulers of the princely States.",
   "Jawaharlal Nehru presided over the session of the All India States People's Conference held at Ludhiana in 1939."],
  ["1936 का फ़ैज़पुर अधिवेशन भारतीय राष्ट्रीय कांग्रेस का किसी गाँव में होने वाला पहला अधिवेशन था।",
   "1938 में हरिपुरा में कांग्रेस ने संकल्प लिया कि वह स्वयं रियासतों के शासकों के विरुद्ध जन-संघर्ष छेड़ेगी और उनका नेतृत्व करेगी।",
   "जवाहरलाल नेहरू ने 1939 में लुधियाना में हुए अखिल भारतीय देशी राज्य प्रजा परिषद के अधिवेशन की अध्यक्षता की।"],
  C3, 1,
  "Statements 1 and 3 are correct. Faizpur, in Khandesh, hosted the first rural session in December 1936, under Nehru, as the Congress turned towards the peasantry; Nehru later presided over the States People's Conference at Ludhiana in 1939, linking the movements in British India and the princely States. "
  "Statement 2 is wrong: the Haripura resolution declared that the Congress's goal of Purna Swaraj included the princely States, but said that struggles there should be carried on by the people of the States through their own organisations, such as the Praja Mandals, and not in the name of the Congress.",
  "कथन 1 और 3 सही हैं। ख़ानदेश के फ़ैज़पुर में दिसंबर 1936 में नेहरू की अध्यक्षता में पहला ग्रामीण अधिवेशन हुआ, जब कांग्रेस किसानों की ओर मुड़ रही थी; बाद में नेहरू ने 1939 में लुधियाना में प्रजा परिषद की अध्यक्षता की, जिससे ब्रिटिश भारत और रियासतों के आंदोलन जुड़े। "
  "कथन 2 ग़लत है: हरिपुरा प्रस्ताव ने घोषित किया कि कांग्रेस के पूर्ण स्वराज के लक्ष्य में रियासतें शामिल हैं, पर कहा कि वहाँ संघर्ष रियासतों की जनता अपने संगठनों, जैसे प्रजा मंडलों, के माध्यम से चलाए, कांग्रेस के नाम से नहीं।",
  MOD, "l3-t1-his-faizpur-haripura-ludhiana", craft="precision")

M("Modern", "medium",
  "In November 1921, scores of prisoners died of suffocation in a closed railway goods wagon while being taken from Tirur to Podanur. This 'Wagon Tragedy' is associated with which of the following?",
  "नवंबर 1921 में तिरूर से पोदनूर ले जाए जाते समय एक बंद मालगाड़ी के डिब्बे में दर्जनों क़ैदियों की दम घुटने से मृत्यु हो गई। यह 'वैगन त्रासदी' निम्नलिखित में से किससे जुड़ी है?",
  ["The Chauri Chaura incident in the United Provinces", "The Rampa rebellion in the Godavari hills",
   "The Eka movement among the peasants of Awadh", "The Malabar (Mappila) rising in Kerala"],
  ["संयुक्त प्रांत की चौरी चौरा घटना", "गोदावरी पहाड़ियों का रम्पा विद्रोह",
   "अवध के किसानों का एका आंदोलन", "केरल का मालाबार (मप्पिला) विद्रोह"],
  3,
  "The Wagon Tragedy followed the Malabar rising of 1921, when Mappila peasants of the Ernad and Valluvanad taluks, roused by the Khilafat agitation and long-standing grievances against landlords, rose against the British; the prisoners died in a sealed goods wagon on the way to jail. "
  "Chauri Chaura (February 1922) led Gandhi to call off Non-Cooperation, the Rampa rebellion was led by Alluri Sitarama Raju in 1922-24, and the Eka movement arose among Awadh's tenants in 1921-22.",
  "वैगन त्रासदी 1921 के मालाबार विद्रोह के बाद हुई, जब खिलाफ़त आंदोलन और ज़मींदारों के विरुद्ध पुरानी शिकायतों से उत्तेजित एरनाड और वल्लुवनाड तालुकों के मप्पिला किसानों ने अंग्रेज़ों के विरुद्ध विद्रोह किया; क़ैदी जेल ले जाए जाते समय एक बंद मालगाड़ी के डिब्बे में मरे। "
  "चौरी चौरा (फ़रवरी 1922) के कारण गांधीजी ने असहयोग आंदोलन वापस लिया, रम्पा विद्रोह का नेतृत्व 1922-24 में अल्लूरी सीताराम राजू ने किया, और एका आंदोलन 1921-22 में अवध के काश्तकारों में उभरा।",
  MOD, "l3-t1-his-wagon-tragedy-malabar-1921", pos=3, craft="linkage")

S("Modern", "medium", "With reference to the Hartog Committee of 1929, consider the following statements:",
  "1929 की हार्टोग समिति के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["It was set up as an auxiliary committee of the Indian Statutory (Simon) Commission to report on the growth of education.",
   "It recommended a rapid expansion of primary schools in every province rather than a policy of consolidation."],
  ["इसे शिक्षा के विकास पर रिपोर्ट देने के लिए भारतीय सांविधिक (साइमन) आयोग की एक सहायक समिति के रूप में गठित किया गया था।",
   "इसने समेकन की नीति के बजाय हर प्रांत में प्राथमिक विद्यालयों के तीव्र विस्तार की सिफ़ारिश की।"],
  T2, 0,
  "Only statement 1 is correct. The committee under Sir Philip Hartog was appointed in 1928-29 as an auxiliary of the Simon Commission. Its best-known finding was the 'wastage and stagnation' in primary education -- many children left before becoming literate, and many stayed in the same class for years -- "
  "and so it recommended consolidation and better quality rather than hasty expansion, the opposite of statement 2.",
  "केवल कथन 1 सही है। सर फ़िलिप हार्टोग की अध्यक्षता वाली समिति 1928-29 में साइमन आयोग की सहायक के रूप में नियुक्त हुई। उसका सबसे प्रसिद्ध निष्कर्ष प्राथमिक शिक्षा में 'अपव्यय और अवरोधन' था -- बहुत से बच्चे साक्षर होने से पहले पढ़ाई छोड़ देते थे, और बहुत से वर्षों तक एक ही कक्षा में रहते थे -- "
  "इसलिए उसने जल्दबाज़ी के विस्तार के बजाय समेकन और बेहतर गुणवत्ता की सिफ़ारिश की, जो कथन 2 का उलटा है।",
  OP3 + "; Report of the Auxiliary Committee of the Indian Statutory Commission (1929).",
  "l3-t1-his-hartog-committee-1929", craft="precision")

S("Modern", "medium", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Vasudev Balwant Phadke organised the Ramosis and other groups in an armed revolt against British rule in Maharashtra in 1879.",
   "The Bijolia peasant movement in Mewar was led for several years by Vijay Singh Pathik.",
   "The Bijolia movement was directed against the many cesses that the jagirdar levied on the peasants of a princely State."],
  ["वासुदेव बलवंत फड़के ने 1879 में महाराष्ट्र में अंग्रेज़ी शासन के विरुद्ध सशस्त्र विद्रोह के लिए रामोशियों और दूसरे समूहों को संगठित किया।",
   "मेवाड़ के बिजोलिया किसान आंदोलन का नेतृत्व कई वर्षों तक विजय सिंह पथिक ने किया।",
   "बिजोलिया आंदोलन उन अनेक उपकरों के विरुद्ध था जो एक रियासत के जागीरदार किसानों पर लगाता था।"],
  C3, 2,
  "All three are correct. Phadke, a clerk in Poona who blamed British policy for the famines of the 1870s, raised a band of Ramosis, Kolis and Dhangars in 1879; he was captured and transported to Aden, where he died. "
  "Bijolia, a thikana of the princely State of Mewar, saw a long peasant agitation from 1897 against the jagirdar's many cesses and forced labour; Vijay Singh Pathik led it from about 1916, organising a no-revenue campaign. "
  "Movements such as Bijolia, in the States rather than in British India, were what the Congress later had to take a position on.",
  "तीनों सही हैं। फड़के, पूना के एक क्लर्क जो 1870 के दशक के अकालों के लिए अंग्रेज़ी नीति को दोषी मानते थे, ने 1879 में रामोशियों, कोलियों और धनगरों का एक दल खड़ा किया; वे पकड़े गए और अदन भेज दिए गए, जहाँ उनकी मृत्यु हुई। "
  "मेवाड़ रियासत के एक ठिकाने बिजोलिया में 1897 से जागीरदार के अनेक उपकरों और बेगार के विरुद्ध लंबा किसान आंदोलन चला; विजय सिंह पथिक ने लगभग 1916 से उसका नेतृत्व किया और लगान न देने का अभियान संगठित किया। "
  "बिजोलिया जैसे आंदोलन, जो ब्रिटिश भारत के बजाय रियासतों में थे, ऐसे थे जिन पर कांग्रेस को बाद में अपना रुख़ तय करना पड़ा।",
  MOD, "l3-t1-his-phadke-ramosis-bijolia", craft="linkage")

# ================================================================ ANCIENT (6)
M("Ancient", "easy",
  "Puhar, also called Kaveripattinam, the port city in which the Tamil epic Silappadikaram opens, was a port of which kingdom?",
  "पुहार, जिसे कावेरीपट्टिनम भी कहते हैं, वह बंदरगाह नगर जिसमें तमिल महाकाव्य शिलप्पदिकारम आरंभ होता है, किस राज्य का बंदरगाह था?",
  ["The Cholas", "The Cheras", "The Pandyas", "The Satavahanas"],
  ["चोल", "चेर", "पांड्य", "सातवाहन"],
  0,
  "Puhar, at the mouth of the Kaveri, was the chief port of the early Cholas; the Silappadikaram begins there with the story of Kovalan and Kannagi, and Sangam poems describe its warehouses and foreign traders. "
  "The Cheras' best-known port was Muziris on the Malabar coast, the Pandyas' was Korkai, and the Satavahanas ruled the Deccan, not the Kaveri delta.",
  "कावेरी के मुहाने पर स्थित पुहार आरंभिक चोलों का प्रमुख बंदरगाह था; शिलप्पदिकारम वहीं कोवलन और कण्णगी की कथा से आरंभ होता है, और संगम कविताएँ उसके गोदामों और विदेशी व्यापारियों का वर्णन करती हैं। "
  "चेरों का सबसे प्रसिद्ध बंदरगाह मालाबार तट पर मुज़िरिस था, पांड्यों का कोरकई, और सातवाहन दक्कन पर शासन करते थे, कावेरी डेल्टा पर नहीं।",
  OP1 + " (Traders, Kings and Pilgrims); " + TH1,
  "l3-t1-his-puhar-chola-port", pos=0, craft="recall")

S("Ancient", "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Arretine ware -- red-glazed pottery from Italy -- and amphorae found at Arikamedu, near Puducherry, point to trade with the Roman world.",
   "The Gatha Saptashati is a collection of Sanskrit hymns composed at the court of the Gupta kings."],
  ["पुडुचेरी के पास अरिकामेडु में मिले एरेटाइन बर्तन -- इटली के लाल चमकदार मृद्भांड -- और एम्फ़ोरा (मदिरा-पात्र) रोमन जगत के साथ व्यापार की ओर संकेत करते हैं।",
   "गाथा सप्तशती गुप्त राजाओं के दरबार में रचित संस्कृत स्तोत्रों का एक संग्रह है।"],
  T2, 0,
  "Only statement 1 is correct. Excavations at Arikamedu turned up Arretine ware, amphorae for wine and oil, and Roman lamps, evidence of a trading station linked to the Mediterranean in the early centuries CE. "
  "The Gatha Saptashati (Gaha Sattasai) is an anthology of about seven hundred short poems of love and village life in Maharashtri Prakrit, attributed to the Satavahana king Hala -- neither Sanskrit hymns nor Gupta.",
  "केवल कथन 1 सही है। अरिकामेडु की खुदाई में एरेटाइन बर्तन, मदिरा और तेल के एम्फ़ोरा और रोमन दीपक मिले, जो ईसवी सन की आरंभिक शताब्दियों में भूमध्यसागर से जुड़े एक व्यापारिक केंद्र के प्रमाण हैं। "
  "गाथा सप्तशती (गाहा सत्तसई) प्रेम और ग्राम-जीवन की लगभग सात सौ छोटी कविताओं का महाराष्ट्री प्राकृत में संग्रह है, जो सातवाहन राजा हाल के नाम से जुड़ा है -- न संस्कृत स्तोत्र, न गुप्तकालीन।",
  TH1 + "; " + ASI + " (Arikamedu).",
  "l3-t1-his-arikamedu-arretine-gatha-saptashati", craft="precision")

S("Ancient", "hard", "With reference to economic life in early historic India, consider the following statements:",
  "आरंभिक ऐतिहासिक भारत के आर्थिक जीवन के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["'Nigama' denoted an association of merchants, and the word appears on some early coins and seals.",
   "'Sarthavaha' was the term for the leader of a merchant caravan.",
   "'Karshapana' was the name of the gold coin issued by the Kushana kings."],
  ["'निगम' व्यापारियों के संघ को कहते थे, और यह शब्द कुछ आरंभिक सिक्कों और मुहरों पर मिलता है।",
   "'सार्थवाह' व्यापारियों के कारवाँ के नेता के लिए प्रयुक्त शब्द था।",
   "'कार्षापण' कुषाण राजाओं द्वारा जारी सोने के सिक्के का नाम था।"],
  C3, 1,
  "Statements 1 and 2 are correct. Nigama -- a body of merchants or a market town -- appears on coins (some Taxila coins carry the word negama) and on seals, and sarthavaha, the caravan leader, is a common figure in texts and inscriptions of the period. "
  "Statement 3 is wrong: the karshapana was the standard punch-marked coin, usually of silver (or copper), long before the Kushanas; the Kushana gold coin was the dinara, a name borrowed from the Roman denarius.",
  "कथन 1 और 2 सही हैं। निगम -- व्यापारियों का समूह या बाज़ार-नगर -- सिक्कों (तक्षशिला के कुछ सिक्कों पर 'नेगम' शब्द है) और मुहरों पर मिलता है, और सार्थवाह, यानी कारवाँ का नेता, उस काल के ग्रंथों और अभिलेखों में एक आम पात्र है। "
  "कथन 3 ग़लत है: कार्षापण कुषाणों से बहुत पहले का मानक आहत (पंच-मार्क) सिक्का था, प्रायः चाँदी (या ताँबे) का; कुषाणों का सोने का सिक्का दीनार था, जिसका नाम रोमन डेनेरियस से लिया गया।",
  TH1 + " (Kings, Farmers and Towns).",
  "l3-t1-his-nigama-sarthavaha-karshapana", craft="precision")

M("Ancient", "medium",
  "Later inscriptions, such as the Velvikudi grant of the Pandyas, describe as 'evil kings' a people who overran the Tamil country after the Sangam age and ended many grants of land to Brahmanas, until the Pandyas and the Pallavas drove them out. Who were they?",
  "बाद के अभिलेख, जैसे पांड्यों का वेल्विकुडि दानपत्र, एक ऐसे लोगों को 'दुष्ट राजा' कहते हैं जिन्होंने संगम युग के बाद तमिल प्रदेश पर अधिकार कर लिया और ब्राह्मणों को दिए गए अनेक भूमि-दानों को समाप्त कर दिया, जब तक पांड्यों और पल्लवों ने उन्हें बाहर नहीं निकाल दिया। वे कौन थे?",
  ["The Kalabhras", "The Kadambas", "The Ikshvakus", "The Satavahanas"],
  ["कलभ्र", "कदंब", "इक्ष्वाकु", "सातवाहन"],
  0,
  "The Kalabhras ruled much of the Tamil country from about the third to the sixth century CE, the 'Kalabhra interregnum'. The Velvikudi copper-plate grant of the eighth century says that they seized the land and cancelled earlier brahmadeya grants until the Pandya king Kadungon overthrew them; "
  "they seem to have favoured Jainism and Buddhism, which explains the hostile memory. The Kadambas ruled in Karnataka, the Ikshvakus in the Krishna valley (Nagarjunakonda), and the Satavahanas in the Deccan.",
  "कलभ्रों ने लगभग तीसरी से छठी शताब्दी ईसवी तक तमिल प्रदेश के बड़े भाग पर शासन किया, जिसे 'कलभ्र अंतराल' कहते हैं। आठवीं शताब्दी का वेल्विकुडि ताम्रपत्र दानपत्र कहता है कि उन्होंने भूमि छीन ली और पहले के ब्रह्मदेय दान रद्द कर दिए, जब तक पांड्य राजा कडुंगोन ने उन्हें उखाड़ नहीं फेंका; "
  "वे जैन और बौद्ध धर्मों को संरक्षण देते प्रतीत होते हैं, जिससे उनकी यह शत्रुतापूर्ण स्मृति समझ में आती है। कदंब कर्नाटक में, इक्ष्वाकु कृष्णा घाटी (नागार्जुनकोंडा) में, और सातवाहन दक्कन में शासन करते थे।",
  TH1 + "; Velvikudi grant (Epigraphia Indica).",
  "l3-t1-his-kalabhras-velvikudi", pos=0, craft="inference")

S("Ancient", "medium", "Consider the following statements about what coins tell us about early Indian history:",
  "आरंभिक भारतीय इतिहास के बारे में सिक्कों से मिलने वाली जानकारी पर निम्नलिखित कथनों पर विचार कीजिए:",
  ["Gold coins of Chandragupta I show him with his queen Kumaradevi and name the Licchavis, pointing to the importance of that marriage alliance.",
   "Some coins of Kanishka show the Buddha, with his name written in Greek script as 'BODDO'.",
   "Coins of the Satavahana ruler Yajna Sri Satakarni bearing the figure of a ship point to the importance of sea trade."],
  ["चंद्रगुप्त प्रथम के सोने के सिक्कों पर वे अपनी रानी कुमारदेवी के साथ दिखते हैं और उन पर लिच्छवियों का नाम है, जो उस विवाह-संबंध के महत्त्व की ओर संकेत करता है।",
   "कनिष्क के कुछ सिक्कों पर बुद्ध अंकित हैं, जिनका नाम यूनानी लिपि में 'BODDO' लिखा है।",
   "जहाज़ की आकृति वाले सातवाहन शासक यज्ञश्री सातकर्णि के सिक्के समुद्री व्यापार के महत्त्व की ओर संकेत करते हैं।"],
  C3, 2,
  "All three are correct. The 'king and queen' coins of Chandragupta I carry the legend Lichchhavayah, honouring the family of Kumaradevi, whose marriage helped the early Guptas rise. "
  "Kanishka's coins carry many gods -- Iranian, Greek and Indian -- and a few show a standing Buddha labelled BODDO in Greek letters, an early depiction of the Buddha in human form. "
  "The ship-type coins of Yajna Sri Satakarni, found on the Coromandel coast, reflect the Satavahanas' interest in maritime trade.",
  "तीनों सही हैं। चंद्रगुप्त प्रथम के 'राजा-रानी' प्रकार के सिक्कों पर 'लिच्छवयः' लेख है, जो कुमारदेवी के कुल का सम्मान करता है, जिनके विवाह ने आरंभिक गुप्तों के उदय में सहायता की। "
  "कनिष्क के सिक्कों पर अनेक देवता हैं -- ईरानी, यूनानी और भारतीय -- और कुछ पर खड़े बुद्ध हैं जिन पर यूनानी अक्षरों में BODDO लिखा है, यह बुद्ध के मानव रूप में आरंभिक चित्रणों में से है। "
  "कोरोमंडल तट पर मिले यज्ञश्री सातकर्णि के जहाज़-प्रकार के सिक्के सातवाहनों की समुद्री व्यापार में रुचि दर्शाते हैं।",
  TH1 + " (Kings, Farmers and Towns: coins).",
  "l3-t1-his-coins-kumaradevi-boddo-ship", craft="inference")

S("Ancient", "medium", "Consider the following statements about two early inscriptions:",
  "दो आरंभिक अभिलेखों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Sohgaura copper plate, from the Gorakhpur region, refers to storehouses kept for use in times of scarcity.",
   "The Mahasthan inscription, from northern Bangladesh, records an order to give relief to people in distress from a granary.",
   "Both inscriptions are written in the Kharosthi script."],
  ["गोरखपुर क्षेत्र का सोहगौरा ताम्रपत्र अभाव के समय उपयोग के लिए रखे गए भंडारगृहों का उल्लेख करता है।",
   "उत्तरी बांग्लादेश का महास्थान अभिलेख संकट में पड़े लोगों को एक अन्न-भंडार से राहत देने के आदेश को दर्ज करता है।",
   "दोनों अभिलेख खरोष्ठी लिपि में लिखे गए हैं।"],
  C3, 1,
  "Statements 1 and 2 are correct. Both records, usually dated to the Mauryan period, show the state storing grain against famine: the Sohgaura plate refers to storehouses (koshthagara) for emergencies, and the Mahasthan inscription orders an official to give the distressed relief from the granary, to be returned when times improved. "
  "Statement 3 is wrong: both are in Brahmi, the script of eastern and most of India; Kharosthi, written from right to left, was used in the north-west.",
  "कथन 1 और 2 सही हैं। दोनों अभिलेख, जिन्हें प्रायः मौर्य काल का माना जाता है, अकाल के विरुद्ध राज्य द्वारा अन्न भंडारण दिखाते हैं: सोहगौरा ताम्रपत्र आपात के लिए भंडारगृहों (कोष्ठागार) का उल्लेख करता है, और महास्थान अभिलेख एक अधिकारी को संकटग्रस्त लोगों को अन्न-भंडार से राहत देने का आदेश देता है, जो अच्छे समय में लौटाई जानी थी। "
  "कथन 3 ग़लत है: दोनों ब्राह्मी में हैं, जो पूर्वी और अधिकांश भारत की लिपि थी; दाएँ से बाएँ लिखी जाने वाली खरोष्ठी उत्तर-पश्चिम में प्रयुक्त होती थी।",
  TH1 + "; " + ASI + ".",
  "l3-t1-his-sohgaura-mahasthan-famine-relief", craft="linkage")

# ================================================================ MEDIEVAL (3)
M("Medieval", "medium",
  "Which Sultan founded the city of Agra as his capital and introduced a standard yard, named after him, for measuring land?",
  "किस सुल्तान ने आगरा नगर को अपनी राजधानी के रूप में बसाया और भूमि मापने के लिए अपने नाम पर एक मानक गज़ चलाया?",
  ["Bahlul Lodi, who founded the Lodi dynasty after the Sayyids",
   "Ibrahim Lodi, who was defeated by Babur at Panipat in 1526",
   "Sher Shah Suri, who later expelled Humayun from India",
   "Sikandar Lodi, Bahlul's son and successor"],
  ["बहलोल लोदी, जिसने सैयदों के बाद लोदी वंश की स्थापना की",
   "इब्राहीम लोदी, जिसे 1526 में पानीपत में बाबर ने हराया",
   "शेरशाह सूरी, जिसने बाद में हुमायूँ को भारत से निकाल दिया",
   "सिकंदर लोदी, बहलोल का पुत्र और उत्तराधिकारी"],
  3,
  "Sikandar Lodi (1489-1517) founded Agra in 1504 and moved his court there to control the chiefs of the region; his gaz-i-Sikandari, a measure of land, remained in use until Akbar replaced it with the gaz-i-Ilahi. "
  "Bahlul founded the dynasty, Ibrahim lost it at Panipat, and Sher Shah came later and is remembered for his own measurement-based revenue reforms.",
  "सिकंदर लोदी (1489-1517) ने 1504 में आगरा बसाया और क्षेत्र के सरदारों पर नियंत्रण के लिए अपना दरबार वहाँ ले गए; उनका गज़-ए-सिकंदरी, भूमि का एक माप, तब तक प्रयोग में रहा जब तक अकबर ने उसकी जगह गज़-ए-इलाही नहीं चलाया। "
  "बहलोल ने वंश स्थापित किया, इब्राहीम ने उसे पानीपत में खो दिया, और शेरशाह बाद में आए और अपने स्वयं के माप-आधारित राजस्व सुधारों के लिए याद किए जाते हैं।",
  OP2 + "; " + TH2,
  "l3-t1-his-sikandar-lodi-agra-gaz", pos=3, craft="recall")

S("Medieval", "medium", "With reference to the military reforms of Alauddin Khalji, consider the following statements:",
  "अलाउद्दीन ख़लजी के सैन्य सुधारों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["'Dagh' was the descriptive roll in which each soldier's features were recorded.",
   "'Chehra' was the branding of horses so that they could not be replaced by poorer ones at muster.",
   "He paid his soldiers mainly by assigning them iqtas rather than in cash."],
  ["'दाग़' वह हुलिया-पंजी थी जिसमें हर सैनिक की शारीरिक पहचान दर्ज की जाती थी।",
   "'चेहरा' घोड़ों को दाग़ने की प्रथा थी, ताकि निरीक्षण के समय उन्हें घटिया घोड़ों से बदला न जा सके।",
   "वह अपने सैनिकों को नक़द के बजाय मुख्यतः इक्ता देकर वेतन देता था।"],
  C3, 3,
  "None of the statements is correct. Statements 1 and 2 swap the two terms: dagh was the branding of horses, and chehra (huliya) the descriptive roll of soldiers -- both meant to stop soldiers from passing off poor horses or substitutes at the muster. "
  "Statement 3 is wrong as well: Alauddin paid his large standing army in cash from the treasury, which is why he controlled market prices so closely; his reliance on cash salaries, not iqtas, is what made the price controls necessary.",
  "कोई भी कथन सही नहीं है। कथन 1 और 2 दोनों शब्दों को आपस में बदल देते हैं: दाग़ घोड़ों को दाग़ना था, और चेहरा (हुलिया) सैनिकों की पहचान-पंजी -- दोनों का उद्देश्य था कि सैनिक निरीक्षण के समय घटिया घोड़े या अपने बदले दूसरे व्यक्ति पेश न कर सकें। "
  "कथन 3 भी ग़लत है: अलाउद्दीन अपनी विशाल स्थायी सेना को ख़ज़ाने से नक़द वेतन देता था, इसीलिए उसने बाज़ार के भाव इतनी कड़ाई से नियंत्रित किए; इक्ता के बजाय नक़द वेतन पर उसकी निर्भरता ने ही मूल्य-नियंत्रण आवश्यक बनाया।",
  OP2 + " (The Delhi Sultans); " + TH2,
  "l3-t1-his-alauddin-dagh-chehra", craft="precision")

P("Medieval", "medium", "Consider the following pairs of methods of assessing land revenue in medieval India and what they involved:",
  "मध्यकालीन भारत में भू-राजस्व निर्धारण की पद्धतियों और उनमें निहित बातों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Zabt : Measuring the land and fixing cash rates for each crop",
   "Kankut : Estimating the yield by inspecting the standing crop",
   "Batai : Fixing the demand for ten years at a time from past averages",
   "Nasaq : Auctioning the right to collect revenue to the highest bidder"],
  ["ज़ब्त : भूमि मापकर हर फ़सल के लिए नक़द दरें तय करना",
   "कनकूत : खड़ी फ़सल का निरीक्षण करके उपज का अनुमान लगाना",
   "बटाई : पिछले औसतों से एक बार में दस वर्षों के लिए माँग तय करना",
   "नसक़ : राजस्व वसूलने का अधिकार सबसे ऊँची बोली लगाने वाले को नीलाम करना"],
  1,
  "Only the first two pairs are correct. Zabt assessed measured land at fixed cash rates per crop, and kankut estimated the yield from the standing crop. "
  "Batai (ghallabakhsh) was crop-sharing: the harvested produce was divided between the cultivator and the state -- the ten-year averaging belongs to Todar Mal's dahsala within the zabt system. "
  "Nasaq was a rough assessment based on the village's or cultivator's past payments, not revenue-farming by auction, which spread only in the eighteenth century as ijaradari.",
  "केवल पहले दो युग्म सही हैं। ज़ब्त मापी गई भूमि का हर फ़सल के लिए तय नक़द दरों पर निर्धारण करता था, और कनकूत खड़ी फ़सल से उपज का अनुमान लगाता था। "
  "बटाई (ग़ल्लाबख़्शी) फ़सल का बँटवारा थी: कटी हुई उपज खेतिहर और राज्य के बीच बाँटी जाती थी -- दस वर्षों का औसत ज़ब्त व्यवस्था के भीतर टोडरमल की दहसाला पद्धति से जुड़ा है। "
  "नसक़ गाँव या खेतिहर के पिछले भुगतानों पर आधारित एक मोटा निर्धारण था, नीलामी द्वारा राजस्व का ठेका नहीं, जो इजारेदारी के रूप में अठारहवीं शताब्दी में ही फैला।",
  TH2 + " (Peasants, Zamindars and the State); Ain-i-Akbari.",
  "l3-t1-his-revenue-zabt-kankut-batai-nasaq", craft="precision")

# ================================================================ MUSIC & DANCE (1)
P("Music & Dance", "hard", "Consider the following pairs of gharanas of khayal singing and vocalists associated with them:",
  "ख़याल गायकी के घरानों और उनसे जुड़े गायकों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Kirana : Bhimsen Joshi",
   "Jaipur-Atrauli : Kishori Amonkar",
   "Patiala : Bade Ghulam Ali Khan",
   "Mewati : Gangubai Hangal"],
  ["किराना : भीमसेन जोशी",
   "जयपुर-अतरौली : किशोरी आमोणकर",
   "पटियाला : बड़े ग़ुलाम अली ख़ान",
   "मेवाती : गंगूबाई हंगल"],
  2,
  "Three pairs are correct. Bhimsen Joshi belonged to the Kirana gharana founded by Abdul Karim Khan; Kishori Amonkar learnt from her mother Mogubai Kurdikar in the Jaipur-Atrauli gharana of Alladiya Khan; Bade Ghulam Ali Khan was the leading voice of the Patiala gharana. "
  "The fourth pair is wrong: Gangubai Hangal, like Bhimsen Joshi a pupil of Sawai Gandharva, sang in the Kirana gharana; the Mewati gharana is associated above all with Pandit Jasraj.",
  "तीन युग्म सही हैं। भीमसेन जोशी अब्दुल करीम ख़ान द्वारा स्थापित किराना घराने के थे; किशोरी आमोणकर ने अलादिया ख़ान के जयपुर-अतरौली घराने में अपनी माँ मोगूबाई कुर्डीकर से सीखा; बड़े ग़ुलाम अली ख़ान पटियाला घराने की प्रमुख आवाज़ थे। "
  "चौथा युग्म ग़लत है: गंगूबाई हंगल, भीमसेन जोशी की तरह सवाई गंधर्व की शिष्या, किराना घराने में गाती थीं; मेवाती घराना सबसे अधिक पंडित जसराज से जुड़ा है।",
  MUS, "l3-t1-his-khayal-gharanas-vocalists", craft="recall")

write("gs_l3_t1_b.sql")
