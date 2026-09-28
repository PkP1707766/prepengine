# -*- coding: utf-8 -*-
"""History audit rewrite, part 2: Medieval India and Art & Culture (same rules as part 1,
see history_rewrite_ancient.py). Rewritten in place, with Hindi; none of these rows is in
a published test."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from rewrite_common import S, M, C, P, write
from polity_common import C3

SC = "Satish Chandra, Medieval India (NCERT, old edition)"
THEMES2 = "NCERT Class XII, Themes in Indian History Part II"
ART = "NCERT Class XI, An Introduction to Indian Art (Part I)"

# ---------------------------------------------------------------- Medieval ------------
S("fda164df-0146-4f61-8797-384656d8c5ac", "Medieval", "hard",
  "Consider the following statements regarding Muhammad bin Tughlaq:",
  "मुहम्मद बिन तुगलक के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
  ["He shifted his capital from Delhi to Lahore.",
   "His 'token currency' consisted of paper notes backed by the royal treasury.",
   "The Moroccan traveller Ibn Battuta, who served him as the qazi of Delhi, wrote his account of India in Persian."],
  ["उसने अपनी राजधानी दिल्ली से लाहौर स्थानांतरित की।",
   "उसकी 'सांकेतिक मुद्रा' (token currency) शाही खज़ाने द्वारा समर्थित कागज़ के नोट थे।",
   "मोरक्को के यात्री इब्न बतूता ने, जो उसके समय में दिल्ली का काज़ी रहा, भारत का अपना विवरण फ़ारसी में लिखा।"],
  C3, 3,
  "None of the statements is correct. The capital was shifted from Delhi to Daulatabad (Devagiri) in the Deccan in 1327, not to Lahore. "
  "The token currency (1329-30) was of bronze or copper coins to be accepted at the value of silver tankas; it failed because the coins were easily forged. Paper money was a Chinese and Mongol practice that may have inspired the idea, but it was not used here. "
  "Ibn Battuta did serve as qazi of Delhi, but his travel account, the Rihla, is in Arabic. "
  "Each statement carries one real element with one wrong detail.",
  "कोई भी कथन सही नहीं है। राजधानी 1327 में दिल्ली से दक्कन के दौलताबाद (देवगिरि) ले जाई गई थी, लाहौर नहीं। "
  "सांकेतिक मुद्रा (1329-30) काँसे या ताँबे के सिक्कों की थी, जिन्हें चाँदी के टंके के बराबर मूल्य पर स्वीकार करना था; सिक्कों की आसानी से नकल हो जाने के कारण यह प्रयोग विफल हुआ। कागज़ी मुद्रा चीनी और मंगोल प्रथा थी, जिससे यह विचार प्रेरित हुआ हो सकता है, पर यहाँ उसका प्रयोग नहीं हुआ। "
  "इब्न बतूता सचमुच दिल्ली का काज़ी रहा, पर उसका यात्रा-वृत्तांत 'रिहला' अरबी में है। "
  "हर कथन में एक वास्तविक तत्व के साथ एक गलत विवरण जोड़ा गया है।",
  f"{SC} -- chapter on the Tughlaqs; {THEMES2} -- 'Through the Eyes of Travellers'.",
  "medieval-muhammad-bin-tughlaq-experiments")

S("a8ad7c5f-a081-410c-80aa-357a86b1e637", "Medieval", "hard",
  "Consider the following statements regarding the administration of Akbar:",
  "अकबर के प्रशासन के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Under the mansabdari system, the 'sawar' rank indicated a mansabdar's personal status and salary, while the 'zat' rank fixed the number of horsemen he had to maintain.",
   "Under the dahsala system worked out by Raja Todar Mal, the revenue demand was based on the average produce and prices of the previous ten years.",
   "Akbar reimposed the jizya and the pilgrim tax in the later part of his reign."],
  ["मनसबदारी व्यवस्था में 'सवार' पद मनसबदार की व्यक्तिगत हैसियत और वेतन बताता था, जबकि 'ज़ात' पद यह तय करता था कि उसे कितने घुड़सवार रखने हैं।",
   "राजा टोडरमल द्वारा बनाई गई दहसाला (दहसाला) व्यवस्था में राजस्व की माँग पिछले दस वर्षों की औसत उपज और कीमतों पर आधारित थी।",
   "अकबर ने अपने शासन के बाद के भाग में जज़िया और तीर्थयात्रा कर फिर से लगा दिए।"],
  C3, 0,
  "Only statement 2 is correct. The dahsala (ain-i-dahsala, 1580) fixed cash rates on the basis of the average produce and prices of the previous ten years, for land measured under the zabt system. "
  "Statement 1 reverses the two ranks: zat fixed personal rank and salary, and sawar the number of cavalrymen to be maintained. "
  "Statement 3 is incorrect: Akbar abolished the pilgrim tax (1563) and the jizya (1564); it was Aurangzeb who reimposed the jizya in 1679.",
  "केवल कथन 2 सही है। दहसाला (आईन-ए-दहसाला, 1580) व्यवस्था में ज़ब्त प्रणाली के अंतर्गत नापी गई भूमि के लिए पिछले दस वर्षों की औसत उपज और कीमतों के आधार पर नकद दरें तय की गईं। "
  "कथन 1 दोनों पदों को उलट देता है: ज़ात व्यक्तिगत पद और वेतन तय करता था, और सवार रखे जाने वाले घुड़सवारों की संख्या। "
  "कथन 3 गलत है: अकबर ने तीर्थयात्रा कर (1563) और जज़िया (1564) समाप्त किए; जज़िया 1679 में औरंगज़ेब ने फिर से लगाया।",
  f"{SC} -- chapters on Akbar's administration; {THEMES2} -- 'Kings and Chronicles: The Mughal Courts' and 'Peasants, Zamindars and the State'.",
  "medieval-akbar-administration")

S("a0b6e03c-cb83-4d10-8fe8-827fde5b40a2", "Medieval", "hard",
  "Consider the following statements regarding Alauddin Khalji's economic measures:",
  "अलाउद्दीन खिलजी के आर्थिक उपायों के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
  ["He fixed the prices of essential commodities, partly to maintain a large standing army at low cost.",
   "The Diwan-i-Bandagan was the department he set up to enforce his market regulations.",
   "He fixed the land revenue in the doab at half of the produce, assessed on the basis of measurement."],
  ["उसने आवश्यक वस्तुओं की कीमतें तय कीं, जिसका एक उद्देश्य कम खर्च में एक बड़ी स्थायी सेना रखना था।",
   "दीवान-ए-बंदगान वह विभाग था जो उसने अपने बाज़ार नियमों को लागू करने के लिए बनाया।",
   "उसने दोआब में भू-राजस्व उपज का आधा तय किया, जिसका निर्धारण भूमि की नाप के आधार पर होता था।"],
  C3, 1,
  "Statements 1 and 3 are correct. Barani links the price controls to the need to pay a large army, raised against the Mongols, on fixed salaries. "
  "Alauddin also raised the land revenue in the doab to half of the produce, assessed by measurement, and brought the rural intermediaries (khuts, muqaddams) under control. "
  "Statement 2 is incorrect: the markets were supervised by the Diwan-i-Riyasat under a Naib-i-Riyasat, with a Shahna-i-Mandi for each market. The Diwan-i-Bandagan was Firuz Shah Tughlaq's department for his large body of slaves.",
  "कथन 1 और 3 सही हैं। बरनी मूल्य-नियंत्रण को मंगोलों के विरुद्ध खड़ी की गई बड़ी सेना को निश्चित वेतन पर रखने की ज़रूरत से जोड़ता है। "
  "अलाउद्दीन ने दोआब में भू-राजस्व बढ़ाकर उपज का आधा कर दिया, जिसका निर्धारण नाप से होता था, और ग्रामीण बिचौलियों (खूत, मुकद्दम) पर नियंत्रण किया। "
  "कथन 2 गलत है: बाज़ारों की देखरेख दीवान-ए-रियासत करता था, जिसके प्रमुख नायब-ए-रियासत थे, और हर बाज़ार के लिए एक शहना-ए-मंडी था। दीवान-ए-बंदगान फ़िरोज़ शाह तुगलक का विभाग था, जो उसके बड़ी संख्या में रखे गए गुलामों के लिए था।",
  f"{SC} -- chapter on the Khaljis; Ziauddin Barani, Tarikh-i-Firuz Shahi (on the market regulations).",
  "medieval-alauddin-khalji-economic-measures")

S("48245681-aa81-46f5-8edd-545fde93b06f", "Medieval", "medium",
  "Consider the following statements regarding the Bhakti movement:",
  "भक्ति आंदोलन के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Kabir emphasised devotion to a formless (nirguna) God and criticised the rituals of both Hindus and Muslims.",
   "In the Tamil region, the Alvars were devotees of Vishnu and the Nayanars were devotees of Shiva.",
   "According to tradition, Mirabai regarded the saint Ravidas as her guru."],
  ["कबीर ने निर्गुण (निराकार) ईश्वर की भक्ति पर बल दिया और हिंदुओं तथा मुसलमानों, दोनों के कर्मकांडों की आलोचना की।",
   "तमिल क्षेत्र में आलवार विष्णु के भक्त थे और नायनार शिव के भक्त थे।",
   "परंपरा के अनुसार, मीराबाई संत रैदास (रविदास) को अपना गुरु मानती थीं।"],
  C3, 2,
  "All three statements are correct. Kabir addressed the Supreme Being as Rama, Hari or Allah but as formless, and mocked idol worship, pilgrimage and ritual on both sides. "
  "The Alvars (Vaishnava) and Nayanars (Shaiva) of the 6th to 9th centuries were the earliest Bhakti saints; their hymns were compiled as the Nalayira Divyaprabandham and the Tevaram respectively. "
  "Tradition holds that Mirabai, the Rajput princess of Merta, accepted Ravidas, a saint from a 'leather-worker' caste, as her guru -- a sign of how Bhakti cut across caste. "
  "A solver who assumes one statement must be false will miss this.",
  "तीनों कथन सही हैं। कबीर ने परम सत्ता को राम, हरि या अल्लाह कहकर पुकारा, पर निराकार माना, और दोनों ओर की मूर्ति-पूजा, तीर्थयात्रा और कर्मकांड का उपहास किया। "
  "6ठी से 9वीं शताब्दी के आलवार (वैष्णव) और नायनार (शैव) सबसे आरंभिक भक्ति संत थे; उनके भजन क्रमशः नालायिर दिव्यप्रबंधम और तेवारम में संकलित हुए। "
  "परंपरा के अनुसार मेड़ता की राजपूत राजकुमारी मीराबाई ने चर्मकार जाति के संत रैदास को अपना गुरु माना; यह दिखाता है कि भक्ति ने जाति की सीमाएँ कैसे तोड़ीं। "
  "जो विद्यार्थी मानकर चलता है कि एक कथन गलत होगा ही, वह यह बात चूक जाएगा।",
  f"{THEMES2} -- 'Bhakti-Sufi Traditions'; {SC} -- chapter on the Bhakti movement.",
  "medieval-bhakti-movement")

S("b4c254dd-31e8-4b58-9ab5-e422cce8d9a2", "Medieval", "hard",
  "Consider the following statements regarding Kabir and the meeting of Bhakti and Sufi ideas:",
  "कबीर और भक्ति तथा सूफ़ी विचारों के मेल के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Kabir's religious identity is debated, and one tradition holds that he was raised in a family of Muslim weavers (julahas).",
   "The Sufi idea of 'wahdat-ul-wujud' (unity of being), associated with Ibn Arabi, found followers among Indian Sufis and is often compared with Bhakti ideas of divine unity.",
   "Verses attributed to Kabir are included in the Guru Granth Sahib."],
  ["कबीर की धार्मिक पहचान पर मतभेद है, और एक परंपरा के अनुसार उनका पालन-पोषण मुसलमान जुलाहों के परिवार में हुआ।",
   "इब्न अरबी से जुड़े सूफ़ी विचार 'वहदत-उल-वुजूद' (अस्तित्व की एकता) के भारतीय सूफ़ियों में अनुयायी थे, और इसकी तुलना प्रायः ईश्वर की एकता के भक्ति विचारों से की जाती है।",
   "कबीर के नाम से प्रचलित पद गुरु ग्रंथ साहिब में शामिल हैं।"],
  C3, 2,
  "All three statements are correct. Kabir's life is known mainly through later traditions; the common account places him in a julaha (weaver) family of Benares, while Hindu traditions link him with the teacher Ramananda. "
  "Wahdat-ul-wujud, developed from Ibn Arabi's thought, was influential among Indian Sufis; it was later opposed by Shaikh Ahmad Sirhindi's wahdat-ul-shuhud. "
  "Guru Arjan included the compositions of Kabir, Ravidas, Namdev and Shaikh Farid among others in the Adi Granth (1604).",
  "तीनों कथन सही हैं। कबीर का जीवन मुख्य रूप से बाद की परंपराओं से ज्ञात है; प्रचलित विवरण उन्हें बनारस के जुलाहा परिवार से जोड़ता है, जबकि हिंदू परंपराएँ उन्हें गुरु रामानंद से जोड़ती हैं। "
  "इब्न अरबी के चिंतन से विकसित वहदत-उल-वुजूद भारतीय सूफ़ियों में प्रभावशाली था; बाद में शेख अहमद सरहिंदी ने इसके विरुद्ध वहदत-उल-शुहूद का विचार रखा। "
  "गुरु अर्जन ने आदि ग्रंथ (1604) में दूसरों के साथ कबीर, रैदास, नामदेव और शेख फ़रीद की रचनाएँ शामिल कीं।",
  f"{THEMES2} -- 'Bhakti-Sufi Traditions'; {SC} -- chapter on religious movements.",
  "medieval-kabir-bhakti-sufi-confluence")

S("d552e5fc-7b33-4da4-b598-b3cbe0b0ff7c", "Medieval", "hard",
  "Consider the following statements regarding Akbar's religious policy:",
  "अकबर की धार्मिक नीति के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
  ["'Sulh-i-kul' (peace with all), the broad principle of his policy, is distinct from the Din-i-Ilahi, a narrow order of disciples he later formed.",
   "The Ain-i-Akbari, the administrative and statistical account of his empire, was compiled by Abdul Qadir Badauni.",
   "The mahzar of 1579, which recognised Akbar as the final arbiter in disputes on religious law, was drafted by Abul Fazl."],
  ["'सुलह-ए-कुल' (सबके साथ शांति), उसकी नीति का व्यापक सिद्धांत, दीन-ए-इलाही से अलग है, जो उसने बाद में शिष्यों का एक छोटा समूह बनाकर शुरू किया।",
   "आईन-ए-अकबरी, उसके साम्राज्य का प्रशासनिक और सांख्यिकीय विवरण, अब्दुल कादिर बदायूँनी ने संकलित की।",
   "1579 का महज़र, जिसने धार्मिक कानून से जुड़े विवादों में अकबर को अंतिम निर्णायक माना, अबुल फ़ज़ल ने तैयार किया था।"],
  C3, 0,
  "Only statement 1 is correct. Sulh-i-kul was a principle of governance -- toleration of all faiths -- while the Din-i-Ilahi (Tauhid-i-Ilahi, 1582) was a small order of disciples, not a state religion. "
  "Statement 2 is incorrect: the Ain-i-Akbari is the third volume of Abul Fazl's Akbarnama; Badauni wrote the Muntakhab-ut-Tawarikh, which is critical of Akbar's religious views. "
  "Statement 3 is incorrect: the mahzar was drafted by Shaikh Mubarak, Abul Fazl's father, and signed by the leading ulama.",
  "केवल कथन 1 सही है। सुलह-ए-कुल शासन का एक सिद्धांत था, यानी सभी धर्मों के प्रति सहिष्णुता, जबकि दीन-ए-इलाही (तौहीद-ए-इलाही, 1582) शिष्यों का एक छोटा समूह था, राज्य-धर्म नहीं। "
  "कथन 2 गलत है: आईन-ए-अकबरी अबुल फ़ज़ल के अकबरनामा का तीसरा खंड है; बदायूँनी ने मुंतखब-उत-तवारीख लिखी, जो अकबर के धार्मिक विचारों की आलोचक है। "
  "कथन 3 गलत है: महज़र अबुल फ़ज़ल के पिता शेख मुबारक ने तैयार किया था, और प्रमुख उलेमा ने उस पर हस्ताक्षर किए।",
  f"{SC} -- chapter on Akbar's religious views; {THEMES2} -- 'Kings and Chronicles: The Mughal Courts'.",
  "medieval-akbar-religious-policy")

S("b688d755-0158-4ac9-b234-02bdb3e8d154", "Medieval", "hard",
  "Consider the following statements regarding Shivaji and the Maratha state:",
  "शिवाजी और मराठा राज्य के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Shivaji's coronation at Raigad in 1674 was performed by his Peshwa, Moropant Pingle.",
   "Aurangzeb's long campaigns in the Deccan are generally seen by historians as a heavy drain on Mughal resources.",
   "Shivaji preferred to pay his officers in cash rather than grant them jagirs, and did not make the posts of the Ashtapradhan hereditary."],
  ["1674 में रायगढ़ में शिवाजी का राज्याभिषेक उनके पेशवा मोरोपंत पिंगले ने संपन्न कराया।",
   "इतिहासकार प्रायः मानते हैं कि दक्कन में औरंगज़ेब के लंबे अभियानों ने मुगल संसाधनों को भारी नुकसान पहुँचाया।",
   "शिवाजी अपने अधिकारियों को जागीर देने के बजाय नकद वेतन देना पसंद करते थे, और उन्होंने अष्टप्रधान के पदों को वंशानुगत नहीं बनाया।"],
  C3, 1,
  "Statements 2 and 3 are correct. Aurangzeb spent the last quarter-century of his reign in the Deccan, and the costs, the disruption of revenue and the jagir crisis are standard explanations of Mughal decline. "
  "Shivaji avoided jagirs where he could, paid in cash, and kept the Ashtapradhan posts non-hereditary (they became hereditary later, under his successors). "
  "Statement 1 is incorrect: the Vedic coronation was performed by Gaga Bhatta, a Brahmana from Benares; Moropant Pingle was the Peshwa (chief minister) of the Ashtapradhan.",
  "कथन 2 और 3 सही हैं। औरंगज़ेब ने अपने शासन के अंतिम पच्चीस वर्ष दक्कन में बिताए, और इसका खर्च, राजस्व में रुकावट और जागीर संकट मुगल पतन की मानक व्याख्याएँ हैं। "
  "शिवाजी जहाँ संभव हो जागीर देने से बचते थे, नकद वेतन देते थे, और अष्टप्रधान के पदों को वंशानुगत नहीं रखा (उनके उत्तराधिकारियों के समय वे बाद में वंशानुगत हो गए)। "
  "कथन 1 गलत है: वैदिक राज्याभिषेक बनारस के ब्राह्मण गागा भट्ट ने कराया था; मोरोपंत पिंगले अष्टप्रधान के पेशवा (प्रधानमंत्री) थे।",
  f"{SC} -- chapters on the rise of the Marathas and on the Mughal decline; NCERT Class VII, Our Pasts II -- 'Eighteenth-Century Political Formations'.",
  "medieval-shivaji-maratha-administration")

S("cec9cd21-c62d-4481-9409-920370e6e7e0", "Medieval", "medium",
  "Consider the following statements regarding the administration of Sher Shah Suri:",
  "शेरशाह सूरी के प्रशासन के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
  ["He issued a silver coin called the 'rupiya'.",
   "He rebuilt the road running from Sonargaon in Bengal to the Indus, later called the Grand Trunk Road, with sarais along it.",
   "His land revenue system was based on the measurement of cultivated land, with the state's share fixed at one-third of the produce."],
  ["उसने 'रुपया' नामक चाँदी का सिक्का जारी किया।",
   "उसने बंगाल के सोनारगाँव से सिंधु तक जाने वाली सड़क का पुनर्निर्माण कराया, जिसे बाद में ग्रैंड ट्रंक रोड कहा गया, और उसके किनारे सराएँ बनवाईं।",
   "उसकी भू-राजस्व व्यवस्था खेती वाली भूमि की नाप पर आधारित थी, और राज्य का हिस्सा उपज का एक-तिहाई तय था।"],
  C3, 2,
  "All three statements are correct. Sher Shah's silver rupiya (about 178 grains) set a standard that lasted through Mughal and British times. "
  "He rebuilt the old highway from Sonargaon to the Indus and built sarais that served as post stations. "
  "He had cultivated land measured and fixed the state's share at one-third of the produce, using crop rates (rai); Akbar's revenue system built directly on this.",
  "तीनों कथन सही हैं। शेरशाह का चाँदी का रुपया (लगभग 178 ग्रेन) एक ऐसा मानक बना जो मुगल और ब्रिटिश काल तक चला। "
  "उसने सोनारगाँव से सिंधु तक के पुराने राजमार्ग का पुनर्निर्माण कराया और सराएँ बनवाईं जो डाक-चौकियों का भी काम करती थीं। "
  "उसने खेती वाली भूमि की नाप कराई और फ़सल-दरों (राय) के आधार पर राज्य का हिस्सा उपज का एक-तिहाई तय किया; अकबर की राजस्व व्यवस्था सीधे इसी पर आधारित थी।",
  f"{SC} -- chapter on Sher Shah and the Sur empire.",
  "medieval-sher-shah-suri-administration")

M("e4fe1f44-73ce-4e93-a6b5-e4674af84358", "Medieval", "hard",
  "In which battle did Babur defeat the Afghans of Bihar and Bengal, led by Mahmud Lodi, in 1529?",
  "1529 में बाबर ने महमूद लोदी के नेतृत्व में बिहार और बंगाल के अफ़ग़ानों को किस युद्ध में हराया?",
  ["The battle of Ghaghra", "The battle of Khanwa", "The battle of Chanderi", "The battle of Chausa"],
  ["घाघरा का युद्ध", "खानवा का युद्ध", "चंदेरी का युद्ध", "चौसा का युद्ध"],
  0,
  "At the battle of Ghaghra (1529), near the confluence of the Ghaghra and the Ganga, Babur defeated the Afghans under Mahmud Lodi, supported by Nusrat Shah of Bengal -- his last major battle. "
  "Khanwa (1527) was against Rana Sanga of Mewar, and Chanderi (1528) against Medini Rai. Chausa (1539) was fought later, between Humayun and Sher Shah. "
  "Three of the options are Babur's own battles, which forces the solver to know which enemy each was fought against.",
  "घाघरा के युद्ध (1529) में, घाघरा और गंगा के संगम के पास, बाबर ने बंगाल के नुसरत शाह के समर्थन वाले महमूद लोदी के अधीन अफ़ग़ानों को हराया; यह उसका अंतिम बड़ा युद्ध था। "
  "खानवा (1527) मेवाड़ के राणा साँगा के विरुद्ध था, और चंदेरी (1528) मेदिनी राय के विरुद्ध। चौसा (1539) बाद में हुमायूँ और शेरशाह के बीच लड़ा गया। "
  "तीन विकल्प बाबर के ही युद्ध हैं, इसलिए विद्यार्थी को जानना होगा कि कौन-सा युद्ध किस शत्रु के विरुद्ध था।",
  f"{SC} -- chapter on the foundation of the Mughal empire; Baburnama, tr. A.S. Beveridge (1922).",
  "medieval-babur-battle-of-ghaghra")

M("4dd0a856-bb63-4803-8666-ebbbc16e545c", "Medieval", "hard",
  "The inlay of semi-precious stones into white marble (pietra dura) was first used on a large scale in Mughal architecture in:",
  "सफ़ेद संगमरमर में अर्ध-कीमती पत्थरों की जड़ाई (पच्चीकारी या पिएत्रा दुरा) का बड़े पैमाने पर प्रयोग मुगल स्थापत्य में सबसे पहले कहाँ हुआ?",
  ["the tomb of I'timad-ud-Daula at Agra", "Humayun's tomb at Delhi", "the Buland Darwaza at Fatehpur Sikri", "Akbar's tomb at Sikandra"],
  ["आगरा में एतमाद-उद-दौला का मकबरा", "दिल्ली में हुमायूँ का मकबरा", "फ़तेहपुर सीकरी में बुलंद दरवाज़ा", "सिकंदरा में अकबर का मकबरा"],
  0,
  "The tomb of I'timad-ud-Daula, built by Nur Jahan for her father (1622-28), is the first Mughal building faced entirely in white marble and decorated with pietra dura on a large scale -- the technique later perfected in the Taj Mahal. "
  "Humayun's tomb (1560s-70s), the Buland Darwaza and Akbar's tomb are mainly red sandstone with white marble inlay, not pietra dura.",
  "नूरजहाँ द्वारा अपने पिता के लिए बनवाया गया एतमाद-उद-दौला का मकबरा (1622-28) पहली मुगल इमारत है जो पूरी तरह सफ़ेद संगमरमर से ढकी है और जिसमें बड़े पैमाने पर पच्चीकारी की गई है; यही तकनीक बाद में ताजमहल में पूर्णता तक पहुँची। "
  "हुमायूँ का मकबरा (1560-70 का दशक), बुलंद दरवाज़ा और अकबर का मकबरा मुख्य रूप से लाल बलुआ पत्थर के हैं, जिनमें सफ़ेद संगमरमर की जड़ाई है, पच्चीकारी नहीं।",
  f"{THEMES2} -- 'Kings and Chronicles: The Mughal Courts'; NCERT Class XII, An Introduction to Indian Art (Part II) -- Indo-Islamic architecture.",
  "medieval-mughal-pietra-dura-itimad-ud-daula")

M("686c7ede-cd03-4780-8e31-104034391dd6", "Medieval", "medium",
  "Guru Arjan Dev, the fifth Sikh Guru, is credited with:",
  "पाँचवें सिख गुरु, गुरु अर्जन देव को किसका श्रेय दिया जाता है?",
  ["compiling the Adi Granth", "founding the Khalsa", "founding the town of Ramdaspur", "composing the Zafarnama"],
  ["आदि ग्रंथ के संकलन का", "खालसा की स्थापना का", "रामदासपुर नगर बसाने का", "ज़फ़रनामा की रचना का"],
  0,
  "Guru Arjan Dev compiled the Adi Granth in 1604, bringing together the hymns of the first five Gurus and of saints such as Kabir, Ravidas, Namdev and Shaikh Farid, and completed the Harmandir Sahib at Amritsar. He was executed on Jahangir's orders in 1606. "
  "Ramdaspur (later Amritsar) was founded by his father, Guru Ram Das; the Khalsa (1699) was founded, and the Zafarnama (a letter to Aurangzeb) written, by Guru Gobind Singh.",
  "गुरु अर्जन देव ने 1604 में आदि ग्रंथ का संकलन किया, जिसमें पहले पाँच गुरुओं और कबीर, रैदास, नामदेव तथा शेख फ़रीद जैसे संतों की वाणी है, और अमृतसर में हरमंदिर साहिब का निर्माण पूरा कराया। 1606 में जहाँगीर के आदेश पर उन्हें मृत्युदंड दिया गया। "
  "रामदासपुर (बाद में अमृतसर) उनके पिता गुरु रामदास ने बसाया था; खालसा (1699) की स्थापना और ज़फ़रनामा (औरंगज़ेब को लिखा पत्र) की रचना गुरु गोबिंद सिंह ने की।",
  f"{SC} -- chapter on religious movements (the Sikh Gurus); {THEMES2} -- 'Bhakti-Sufi Traditions'.",
  "medieval-guru-arjan-dev-adi-granth")

C("402aae9a-ac93-4477-829a-809719d668da", "Medieval", "medium",
  "Consider the following battles:",
  "निम्नलिखित युद्धों पर विचार कीजिए:",
  ["Battle of Haldighati", "Battle of Khanwa", "Second Battle of Panipat", "Battle of Chausa"],
  ["हल्दीघाटी का युद्ध", "खानवा का युद्ध", "पानीपत का दूसरा युद्ध", "चौसा का युद्ध"],
  ["2-4-3-1", "2-3-4-1", "4-2-3-1", "2-4-1-3"], 0,
  "The order is Khanwa (1527, Babur against Rana Sanga), Chausa (1539, Sher Shah against Humayun), the Second Battle of Panipat (1556, Akbar's forces under Bairam Khan against Hemu) and Haldighati (1576, Mughal forces under Man Singh against Maharana Pratap): 2-4-3-1. "
  "The distractors keep Khanwa first but misplace the three that follow, which is where solvers who remember only the reigns go wrong.",
  "सही क्रम है: खानवा (1527, बाबर बनाम राणा साँगा), चौसा (1539, शेरशाह बनाम हुमायूँ), पानीपत का दूसरा युद्ध (1556, बैरम खाँ के नेतृत्व में अकबर की सेना बनाम हेमू) और हल्दीघाटी (1576, मानसिंह के नेतृत्व में मुगल सेना बनाम महाराणा प्रताप): 2-4-3-1। "
  "गलत विकल्प खानवा को पहले ही रखते हैं, पर बाकी तीन का क्रम बिगाड़ देते हैं; केवल शासनकाल याद रखने वाले विद्यार्थी यहीं भूल करते हैं।",
  f"{SC} -- chapters on the Mughal empire and the Sur interlude.",
  "medieval-battles-chronology")

P("026b12f3-08b3-4165-a117-2042f18e6511", "Medieval", "medium",
  "Consider the following pairs of Mughal rulers and what is associated with them:",
  "मुगल शासकों और उनसे जुड़ी चीज़ों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Jahangir : Zanjir-i-Adl (the chain of justice)", "Shah Jahan : The Peacock Throne", "Akbar : Fatehpur Sikri", "Humayun : Din Panah"],
  ["जहाँगीर : ज़ंजीर-ए-अद्ल (न्याय की ज़ंजीर)", "शाहजहाँ : तख़्त-ए-ताऊस (मयूर सिंहासन)", "अकबर : फ़तेहपुर सीकरी", "हुमायूँ : दीनपनाह"],
  3,
  "All four pairs are correct. Jahangir describes the golden chain of justice hung at Agra fort; Shah Jahan commissioned the Peacock Throne (taken away by Nadir Shah in 1739); Akbar built Fatehpur Sikri in the 1570s; and Humayun founded the city of Din Panah at Delhi in 1533, on the site Sher Shah later rebuilt as the Purana Qila. "
  "The last pair is the one most solvers doubt.",
  "चारों युग्म सही हैं। जहाँगीर आगरा किले में लटकाई गई सोने की न्याय की ज़ंजीर का वर्णन करता है; शाहजहाँ ने मयूर सिंहासन बनवाया (जिसे 1739 में नादिरशाह ले गया); अकबर ने 1570 के दशक में फ़तेहपुर सीकरी बनवाई; और हुमायूँ ने 1533 में दिल्ली में दीनपनाह नगर बसाया, जिस स्थान पर बाद में शेरशाह ने पुराना किला बनवाया। "
  "अधिकांश विद्यार्थी अंतिम युग्म पर संदेह करते हैं।",
  f"{SC} -- chapters on the Mughal empire; {THEMES2} -- 'Kings and Chronicles: The Mughal Courts'.",
  "medieval-mughal-rulers-pairs")

P("c7e383f6-c3bb-4804-bca6-8a66d4c5eab7", "Medieval", "medium",
  "Consider the following pairs of saint-poets and their works:",
  "संत-कवियों और उनकी रचनाओं के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Kabir : Bijak", "Tulsidas : Ramcharitmanas", "Surdas : Sursagar", "Raskhan : Padmavat"],
  ["कबीर : बीजक", "तुलसीदास : रामचरितमानस", "सूरदास : सूरसागर", "रसखान : पद्मावत"],
  2,
  "Three pairs are correct. The Bijak is the Kabirpanthi collection of Kabir's verses; Tulsidas wrote the Ramcharitmanas in Awadhi; Surdas's Sursagar sings of Krishna's childhood in Braj bhasha. "
  "Pair 4 is wrong: the Padmavat (1540) is by the Sufi poet Malik Muhammad Jayasi; Raskhan, a Muslim devotee of Krishna, wrote the Prem Vatika and the verses collected as Sujan Raskhan.",
  "तीन युग्म सही हैं। बीजक कबीरपंथियों द्वारा संकलित कबीर की वाणी है; तुलसीदास ने अवधी में रामचरितमानस लिखा; सूरदास का सूरसागर ब्रजभाषा में कृष्ण के बचपन का गान है। "
  "युग्म 4 गलत है: पद्मावत (1540) सूफ़ी कवि मलिक मुहम्मद जायसी की रचना है; कृष्ण के मुसलमान भक्त रसखान ने प्रेमवाटिका लिखी और उनके पद सुजान रसखान में संकलित हैं।",
  f"{SC} -- chapter on religious movements and literature; {THEMES2} -- 'Bhakti-Sufi Traditions'.",
  "medieval-saint-poets-works-pairs")

P("6e9e1c00-32a7-4d00-9442-d117b58d6b35", "Medieval", "hard",
  "Consider the following pairs of medieval works and their authors:",
  "मध्यकालीन रचनाओं और उनके लेखकों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Tabaqat-i-Nasiri : Minhaj-us-Siraj", "Fatawa-i-Jahandari : Amir Khusrau", "Khazain-ul-Futuh : Ziauddin Barani", "Tuzuk-i-Jahangiri : Jahangir"],
  ["तबकात-ए-नासिरी : मिनहाज-उस-सिराज", "फ़तवा-ए-जहाँदारी : अमीर खुसरो", "खज़ाइन-उल-फ़ुतूह : ज़ियाउद्दीन बरनी", "तुज़ुक-ए-जहाँगीरी : जहाँगीर"],
  1,
  "Two pairs are correct: Minhaj-us-Siraj wrote the Tabaqat-i-Nasiri, dedicated to Sultan Nasiruddin Mahmud, and Jahangir wrote his own memoirs, the Tuzuk-i-Jahangiri. "
  "Pairs 2 and 3 swap the authors: the Fatawa-i-Jahandari, a treatise on statecraft, is by Ziauddin Barani, and the Khazain-ul-Futuh, an account of Alauddin Khalji's campaigns, is by Amir Khusrau.",
  "दो युग्म सही हैं: मिनहाज-उस-सिराज ने सुल्तान नासिरुद्दीन महमूद को समर्पित तबकात-ए-नासिरी लिखी, और जहाँगीर ने अपने संस्मरण तुज़ुक-ए-जहाँगीरी स्वयं लिखे। "
  "युग्म 2 और 3 लेखकों को आपस में बदल देते हैं: राजनीति पर ग्रंथ फ़तवा-ए-जहाँदारी ज़ियाउद्दीन बरनी का है, और अलाउद्दीन खिलजी के अभियानों का विवरण खज़ाइन-उल-फ़ुतूह अमीर खुसरो का।",
  f"{SC} -- sources of medieval Indian history; {THEMES2} -- 'Kings and Chronicles: The Mughal Courts'.",
  "medieval-chronicles-authors-pairs")

# ------------------------------------------------------------- Art & Culture ----------
M("bee4858e-ed68-4e37-8b8a-cc4964c1d7d9", "Architecture", "medium",
  "The 'Indo-Saracenic' style of colonial buildings such as the Gateway of India and the Madras High Court is best described as:",
  "गेटवे ऑफ़ इंडिया और मद्रास उच्च न्यायालय जैसी औपनिवेशिक इमारतों की 'इंडो-सारसेनिक' शैली को सबसे सही रूप में किस तरह वर्णित किया जा सकता है?",
  ["Indian (Mughal and Rajput) forms combined with Gothic and neoclassical elements",
   "Persian Timurid forms combined with Central Asian Seljuk elements",
   "Portuguese Baroque forms combined with Konkan temple elements",
   "Dravida temple forms combined with Art Deco elements"],
  ["भारतीय (मुगल और राजपूत) रूपों के साथ गोथिक और नव-शास्त्रीय तत्वों का मेल",
   "फ़ारसी तैमूरी रूपों के साथ मध्य एशियाई सेल्जुक तत्वों का मेल",
   "पुर्तगाली बरोक रूपों के साथ कोंकण मंदिर तत्वों का मेल",
   "द्रविड़ मंदिर रूपों के साथ आर्ट डेको तत्वों का मेल"],
  0,
  "Indo-Saracenic architecture, developed by British architects in the late 19th century, placed Indian features -- domes, chhatris, jalis, pointed arches -- on buildings planned on Gothic and neoclassical lines. "
  "The Gateway of India (1924) and the Madras High Court (1892) are standard examples. The other options pair real styles that did not combine into this colonial idiom.",
  "इंडो-सारसेनिक स्थापत्य, जिसे ब्रिटिश वास्तुकारों ने 19वीं सदी के अंत में विकसित किया, गोथिक और नव-शास्त्रीय योजना वाली इमारतों पर भारतीय विशेषताएँ (गुंबद, छतरियाँ, जालियाँ, नुकीले मेहराब) जोड़ता था। "
  "गेटवे ऑफ़ इंडिया (1924) और मद्रास उच्च न्यायालय (1892) इसके मानक उदाहरण हैं। बाकी विकल्प वास्तविक शैलियों को जोड़ते हैं, पर उनके मेल से यह औपनिवेशिक शैली नहीं बनी।",
  "NCERT Class XII, Themes in Indian History Part III -- 'Colonial Cities: Urbanisation, Planning and Architecture'.",
  "art-culture-indo-saracenic-architecture")

S("275588f9-048f-4d4e-a335-f9a7fae97b9a", "Architecture", "medium",
  "Consider the following statements regarding the styles of Indian temple architecture:",
  "भारतीय मंदिर स्थापत्य की शैलियों के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Nagara style is marked by a pyramidal vimana and is chiefly found in South India.",
   "The Dravida style is marked by a curvilinear shikhara and is chiefly found in North India.",
   "The Vesara style developed chiefly under the Pallavas of Kanchi."],
  ["नागर शैली की पहचान पिरामिडनुमा विमान है और यह मुख्य रूप से दक्षिण भारत में मिलती है।",
   "द्रविड़ शैली की पहचान वक्र-रेखीय शिखर है और यह मुख्य रूप से उत्तर भारत में मिलती है।",
   "वेसर शैली का विकास मुख्य रूप से कांची के पल्लवों के अधीन हुआ।"],
  C3, 3,
  "None of the statements is correct. Statements 1 and 2 swap the two styles: the Nagara temple of North India has a curvilinear (rekha-prasada) shikhara, while the Dravida temple of the South has a stepped, pyramidal vimana and, later, towering gopurams. "
  "Statement 3 is incorrect: Vesara, a hybrid of Nagara and Dravida features, developed in the Deccan under the Later Chalukyas of Kalyani and the Hoysalas (for example at Lakkundi, Belur and Halebidu); the Pallavas built in the Dravida style.",
  "कोई भी कथन सही नहीं है। कथन 1 और 2 दोनों शैलियों को आपस में बदल देते हैं: उत्तर भारत के नागर मंदिर का शिखर वक्र-रेखीय (रेखा-प्रासाद) होता है, जबकि दक्षिण के द्रविड़ मंदिर में सीढ़ीनुमा, पिरामिड जैसा विमान और बाद में ऊँचे गोपुरम होते हैं। "
  "कथन 3 गलत है: नागर और द्रविड़ विशेषताओं की मिश्रित वेसर शैली दक्कन में कल्याणी के उत्तरकालीन चालुक्यों और होयसलों के अधीन विकसित हुई (जैसे लक्कुंडी, बेलूर और हलेबिडु में); पल्लवों ने द्रविड़ शैली में निर्माण किया।",
  f"{ART} -- temple architecture and sculpture.",
  "art-culture-temple-styles-nagara-dravida-vesara")

S("c22acb2f-d68b-490c-887a-44a2572026c7", "Culture-Other", "medium",
  "Consider the following statements regarding the status of 'Classical Language' in India:",
  "भारत में 'शास्त्रीय भाषा' के दर्जे के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Tamil was the first language to be declared a Classical Language, in 2004.",
   "In 2024, Marathi, Pali, Prakrit, Assamese and Bengali were declared Classical Languages, taking the total to eleven.",
   "A language is declared a Classical Language by an amendment to the Eighth Schedule of the Constitution."],
  ["2004 में शास्त्रीय भाषा घोषित होने वाली पहली भाषा तमिल थी।",
   "2024 में मराठी, पालि, प्राकृत, असमिया और बांग्ला को शास्त्रीय भाषा घोषित किया गया, जिससे इनकी कुल संख्या ग्यारह हो गई।",
   "किसी भाषा को संविधान की आठवीं अनुसूची में संशोधन द्वारा शास्त्रीय भाषा घोषित किया जाता है।"],
  C3, 1,
  "Statements 1 and 2 are correct. Tamil (2004) was followed by Sanskrit (2005), Telugu and Kannada (2008), Malayalam (2013) and Odia (2014); on 3 October 2024 the Union Cabinet added Marathi, Pali, Prakrit, Assamese and Bengali, making eleven. "
  "Statement 3 is incorrect: the status is an executive decision of the Government of India (the Ministry of Culture, on the advice of a linguistic experts committee), not a constitutional amendment -- Pali and Prakrit are not even in the Eighth Schedule.",
  "कथन 1 और 2 सही हैं। तमिल (2004) के बाद संस्कृत (2005), तेलुगु और कन्नड़ (2008), मलयालम (2013) और ओड़िया (2014) आईं; 3 अक्टूबर 2024 को केंद्रीय मंत्रिमंडल ने मराठी, पालि, प्राकृत, असमिया और बांग्ला को जोड़ा, जिससे संख्या ग्यारह हुई। "
  "कथन 3 गलत है: यह दर्जा भारत सरकार का एक कार्यकारी निर्णय है (भाषा विशेषज्ञ समिति की सलाह पर संस्कृति मंत्रालय द्वारा), संविधान संशोधन नहीं; पालि और प्राकृत तो आठवीं अनुसूची में हैं भी नहीं।",
  "Press Information Bureau, Cabinet decision on classical language status (3 October 2024); Ministry of Culture -- classical languages of India.",
  "art-culture-classical-language-status")

P("a99c156b-cabf-44e4-9da6-4d1f0c0434a7", "Iconography", "medium",
  "Consider the following pairs of mudras in Buddhist images and what they signify:",
  "बौद्ध प्रतिमाओं की मुद्राओं और उनके अर्थ के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Bhumisparsha mudra : Calling the earth to witness", "Dharmachakra mudra : Turning the wheel of the law", "Abhaya mudra : Fearlessness and protection", "Dhyana mudra : Victory over Mara"],
  ["भूमिस्पर्श मुद्रा : पृथ्वी को साक्षी बनाना", "धर्मचक्र मुद्रा : धर्म का चक्र घुमाना", "अभय मुद्रा : निर्भयता और रक्षा", "ध्यान मुद्रा : मार पर विजय"],
  2,
  "Three pairs are correct. In the bhumisparsha mudra the Buddha touches the earth with his right hand, calling it to witness his enlightenment at Bodh Gaya; the dharmachakra mudra marks the first sermon at Sarnath; the raised open palm of the abhaya mudra grants fearlessness. "
  "Pair 4 is wrong: the dhyana mudra, both hands resting in the lap, signifies meditation. The victory over Mara is expressed by the bhumisparsha mudra itself, which is why the pair is tempting.",
  "तीन युग्म सही हैं। भूमिस्पर्श मुद्रा में बुद्ध दाहिने हाथ से पृथ्वी को छूते हैं और उसे बोधगया में अपनी ज्ञान-प्राप्ति का साक्षी बनाते हैं; धर्मचक्र मुद्रा सारनाथ के पहले उपदेश को दर्शाती है; अभय मुद्रा की उठी हुई खुली हथेली निर्भयता देती है। "
  "युग्म 4 गलत है: ध्यान मुद्रा, जिसमें दोनों हाथ गोद में टिके होते हैं, ध्यान को दर्शाती है। मार पर विजय स्वयं भूमिस्पर्श मुद्रा से व्यक्त होती है, इसीलिए यह युग्म आकर्षक लगता है।",
  f"{ART} -- Buddhist sculpture; NCERT Class XII, Themes in Indian History Part I -- 'Thinkers, Beliefs and Buildings'.",
  "art-culture-buddhist-mudras-pairs")

S("a94ab5f7-c214-4f72-ae51-80b6639a79f1", "Music & Dance", "medium",
  "Consider the following statements regarding the classical dance forms of India:",
  "भारत के शास्त्रीय नृत्यों के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Bharatanatyam developed from the temple dance traditions of Tamil Nadu.",
   "Kuchipudi takes its name from a village in the Krishna district of Andhra Pradesh.",
   "Kathak developed as a temple dance at the court of the Vijayanagara empire."],
  ["भरतनाट्यम तमिलनाडु की मंदिर नृत्य परंपराओं से विकसित हुआ।",
   "कुचिपुड़ी का नाम आंध्र प्रदेश के कृष्णा ज़िले के एक गाँव से लिया गया है।",
   "कथक विजयनगर साम्राज्य के दरबार में मंदिर नृत्य के रूप में विकसित हुआ।"],
  C3, 1,
  "Statements 1 and 2 are correct. Bharatanatyam grew out of the sadir performed in Tamil temples and was reconstructed in the 20th century; Kuchipudi is named after the village of Kuchelapuram (Kuchipudi) in Krishna district. "
  "Statement 3 is incorrect: Kathak is a North Indian form that grew from the kathakars, the storytellers of the temples, and developed in the Mughal and later Awadh and Rajput courts, giving the Lucknow, Jaipur and Benares gharanas.",
  "कथन 1 और 2 सही हैं। भरतनाट्यम तमिल मंदिरों में होने वाले सदिर से विकसित हुआ और 20वीं सदी में इसका पुनर्गठन हुआ; कुचिपुड़ी का नाम कृष्णा ज़िले के कुचेलपुरम (कुचिपुड़ी) गाँव से पड़ा है। "
  "कथन 3 गलत है: कथक उत्तर भारत का नृत्य है, जो मंदिरों के कथावाचक कथकों से निकला और मुगल तथा बाद में अवध और राजपूत दरबारों में विकसित हुआ; इसी से लखनऊ, जयपुर और बनारस घराने बने।",
  "Sangeet Natak Akademi -- classical dance forms of India; NCERT Class XI, An Introduction to Indian Art -- the performing arts.",
  "art-culture-classical-dance-forms-origins")

S("97267155-a21b-4b3f-b972-6d44ade4aa79", "Music & Dance", "medium",
  "Consider the following statements regarding Indian classical music and dance:",
  "भारतीय शास्त्रीय संगीत और नृत्य के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Sattriya was introduced by the Vaishnava saint Srimanta Sankaradeva in the monasteries (sattras) of Assam.",
   "The Sangeet Natak Akademi recognised Sattriya as a classical dance form in 2000.",
   "In Carnatic music, the 72 melakarta ragas are the parent scales from which other ragas are derived."],
  ["सत्रिया की शुरुआत वैष्णव संत श्रीमंत शंकरदेव ने असम के मठों (सत्रों) में की।",
   "संगीत नाटक अकादमी ने 2000 में सत्रिया को शास्त्रीय नृत्य के रूप में मान्यता दी।",
   "कर्नाटक संगीत में 72 मेलकर्ता राग वे जनक स्वर-क्रम (स्केल) हैं जिनसे अन्य राग बनते हैं।"],
  C3, 2,
  "All three statements are correct. Sankaradeva (15th-16th century) created Sattriya as part of the ankiya naat dance-dramas of the Assamese Vaishnava sattras; the Sangeet Natak Akademi recognised it as classical in 2000. "
  "The 72 melakarta (janaka) ragas, systematised by Venkatamakhin in the 17th century, are the parent scales from which the janya ragas are derived.",
  "तीनों कथन सही हैं। शंकरदेव (15वीं-16वीं सदी) ने असम के वैष्णव सत्रों के अंकिया नाट नृत्य-नाटकों के अंग के रूप में सत्रिया की रचना की; संगीत नाटक अकादमी ने 2000 में इसे शास्त्रीय माना। "
  "17वीं सदी में वेंकटमखी द्वारा व्यवस्थित 72 मेलकर्ता (जनक) राग वे जनक स्वर-क्रम हैं जिनसे जन्य राग बनते हैं।",
  "Sangeet Natak Akademi -- classical dance forms of India; NCERT Class XI, An Introduction to Indian Art -- the performing arts.",
  "art-culture-classical-music-dance-basics")

S("056b1cd9-fbde-42ce-bb23-9bed7d23854f", "Painting", "hard",
  "Consider the following statements regarding Mughal painting:",
  "मुगल चित्रकला के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Persian masters Mir Sayyid Ali and Abd al-Samad, who came to India with Humayun, led the early Mughal studio.",
   "Akbar set up a large royal painting workshop (tasvir khana) employing many artists.",
   "The Hamzanama, one of the first projects of Akbar's studio, was painted on paper in a small miniature format."],
  ["हुमायूँ के साथ भारत आए फ़ारसी उस्ताद मीर सैयद अली और अब्दुस्समद ने आरंभिक मुगल चित्रशाला का नेतृत्व किया।",
   "अकबर ने एक बड़ी शाही चित्रशाला (तस्वीरख़ाना) स्थापित की, जिसमें अनेक चित्रकार काम करते थे।",
   "अकबर की चित्रशाला की आरंभिक परियोजनाओं में से एक, हम्ज़ानामा, कागज़ पर छोटे लघुचित्र आकार में बनाया गया था।"],
  C3, 1,
  "Statements 1 and 2 are correct. Mir Sayyid Ali and Abd al-Samad joined Humayun in Kabul and came with him to India; under Akbar they trained a large team of Indian artists such as Daswanth and Basawan, which fused Persian and Indian styles. "
  "Statement 3 is incorrect: the Hamzanama (c. 1562-77) was painted on cotton cloth in unusually large folios (about 69 x 54 cm), roughly 1,400 of them, so that they could be shown while the tales were recited.",
  "कथन 1 और 2 सही हैं। मीर सैयद अली और अब्दुस्समद काबुल में हुमायूँ के साथ आए और उसके साथ भारत पहुँचे; अकबर के समय उन्होंने दसवंत और बसावन जैसे अनेक भारतीय चित्रकारों को प्रशिक्षित किया, जिससे फ़ारसी और भारतीय शैलियों का मेल हुआ। "
  "कथन 3 गलत है: हम्ज़ानामा (लगभग 1562-77) सूती कपड़े पर असामान्य रूप से बड़े पन्नों (लगभग 69 x 54 से.मी.) में बनाया गया, जिनकी संख्या लगभग 1,400 थी, ताकि कथाएँ सुनाते समय इन्हें दिखाया जा सके।",
  f"NCERT Class XII, An Introduction to Indian Art (Part II) -- Mughal painting; {THEMES2} -- 'Kings and Chronicles: The Mughal Courts'.",
  "art-culture-mughal-miniature-painting")

P("ba4ad740-6b8b-4286-8046-802ee46ffbae", "Painting", "medium",
  "Consider the following pairs of painting traditions and the States they are chiefly associated with:",
  "चित्रकला परंपराओं और उन राज्यों के निम्नलिखित युग्मों पर विचार कीजिए जिनसे वे मुख्य रूप से जुड़ी हैं:",
  ["Pattachitra : Odisha", "Warli : Maharashtra", "Pithora : Kerala", "Kalamkari : Madhya Pradesh"],
  ["पट्टचित्र : ओडिशा", "वारली : महाराष्ट्र", "पिथोरा : केरल", "कलमकारी : मध्य प्रदेश"],
  1,
  "Two pairs are correct. Pattachitra, painted on cloth for the Jagannath tradition, belongs to Odisha (with a related scroll tradition in West Bengal); Warli is the ritual wall painting of the Warli tribe of Maharashtra's Palghar region. "
  "Pair 3 is wrong: Pithora is the ritual wall painting of the Rathwa and Bhilala communities of central Gujarat and western Madhya Pradesh. Pair 4 is wrong: Kalamkari, pen-drawn and block-printed textile painting, belongs to Andhra Pradesh (Srikalahasti and Machilipatnam).",
  "दो युग्म सही हैं। जगन्नाथ परंपरा के लिए कपड़े पर बनाया जाने वाला पट्टचित्र ओडिशा का है (पश्चिम बंगाल में इससे जुड़ी पट-चित्र परंपरा भी है); वारली महाराष्ट्र के पालघर क्षेत्र की वारली जनजाति की अनुष्ठानिक भित्ति-चित्रकला है। "
  "युग्म 3 गलत है: पिथोरा मध्य गुजरात और पश्चिमी मध्य प्रदेश के राठवा और भिलाला समुदायों की अनुष्ठानिक भित्ति-चित्रकला है। युग्म 4 गलत है: कलम से बनाई और छापे से छपी वस्त्र-चित्रकला कलमकारी आंध्र प्रदेश (श्रीकालहस्ती और मछलीपट्टनम) की है।",
  "NCERT Class XI, Living Craft Traditions of India; Geographical Indications Registry -- Pattachitra, Warli and Kalamkari entries.",
  "art-culture-painting-traditions-states-pairs")

if __name__ == "__main__":
    write("history_rewrite_medieval_culture.sql")
