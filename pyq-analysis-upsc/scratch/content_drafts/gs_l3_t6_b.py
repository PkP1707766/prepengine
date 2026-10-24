# -*- coding: utf-8 -*-
"""Level 3 · Test 6 (GS Integrated Test 6) -- part B: History (16) (upsc_l3_cell_targets.mjs 6).
History cells: Modern e-MCQ, e-stmt, h-stmt, m-MCQ, m-stmt x2; Ancient e-MCQ, e-stmt, h-stmt, m-MCQ, m-stmt x2;
Medieval m-MCQ, m-stmt, m-pairs; Music & Dance h-pairs.
Every fact was searched in the whole UPSC bank (l3_tools/bank_find.py) and is one no row tests: Govind Guru and
Mangarh; Gujarat Vidyapith, Jamia Millia and Bihar Vidyapith; Pritilata Waddedar, Bina Das, Kalpana Dutt and the
Writers' Building raid; M. N. Roy and Tashkent; the Industrial and Fiscal Commissions, the Tariff Board and steel
protection; Lokahitawadi, Muthulakshmi Reddy and D. K. Karve; the ratnins; the Bower Manuscript and Vagbhata;
Kodumanal, Porunthal and Sivagalai; the Damodarpur plates; Bhattiprolu; Chandraketugarh; Kajri, Chaiti, Hori and
Dadra; the Sultanate's Diwan-i-Wizarat, Diwan-i-Insha, Barid-i-Mumalik and Diwan-i-Risalat; the ayagars;
Kamban, the 'three gems' of Kannada and the Periya Puranam. MCQ keys are pinned."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, write
from polity_common import C3, C4, T2

d.SUBJECT = "History"
d.REQUIRE_CRAFT = True
MOD = "NCERT Class XII, Themes in Indian History III; NCERT (old), Modern India"
TH1 = "NCERT Class XII, Themes in Indian History I"
TH2 = "NCERT Class XII, Themes in Indian History II"
ANC = "NCERT (old), Ancient India"
MED = "NCERT (old), Medieval India"
OP2 = "NCERT Class VII, Our Pasts II"
MUS = "NCERT Class XI, An Introduction to Indian Art; Sangeet Natak Akademi"
ASI = "Archaeological Survey of India"

# ================================================================ MODERN (6)
M("Modern", "easy",
  "The firing on a gathering of Bhils at Mangarh hill in 1913, sometimes called the 'Jallianwala of the tribals', is associated with the movement led by:",
  "1913 में मानगढ़ पहाड़ी पर भीलों की एक सभा पर हुई गोलीबारी, जिसे कभी-कभी ‘आदिवासियों का जलियाँवाला’ कहा जाता है, किसके नेतृत्व वाले आंदोलन से जुड़ी है?",
  ["Alluri Sitarama Raju", "Birsa Munda", "Tantya Bhil", "Govind Guru"],
  ["अल्लूरी सीताराम राजू", "बिरसा मुंडा", "टंट्या भील", "गोविंद गुरु"],
  3,
  "Govind Guru, a reformer who worked among the Bhils of the hill country where the present Rajasthan, Gujarat and Madhya Pradesh meet, led the Bhagat movement: he urged the Bhils to give up liquor and animal sacrifice and to resist forced labour and the heavy demands of the princely states of Banswara, Dungarpur and Santrampur. In November 1913 thousands gathered with him on Mangarh hill; troops of the British and of the princely states opened fire, killing a large number, and Govind Guru was imprisoned. The site, Mangarh Dham, is now a memorial. "
  "The others led movements elsewhere: Alluri Sitarama Raju the Rampa rebellion in the Godavari hills (1922-24), Birsa Munda the Ulgulan in Chota Nagpur (1899-1900), and Tantya Bhil a long resistance in the Nimar region of central India until his execution in 1889.",
  "गोविंद गुरु, एक सुधारक जिन्होंने उस पहाड़ी क्षेत्र के भीलों के बीच काम किया जहाँ आज के राजस्थान, गुजरात और मध्य प्रदेश मिलते हैं, ने भगत आंदोलन का नेतृत्व किया: उन्होंने भीलों से शराब और पशु-बलि छोड़ने तथा बांसवाड़ा, डूंगरपुर और संतरामपुर की रियासतों के बेगार और भारी माँगों का विरोध करने का आग्रह किया। नवंबर 1913 में हज़ारों लोग उनके साथ मानगढ़ पहाड़ी पर इकट्ठा हुए; ब्रिटिश और रियासतों की सेनाओं ने गोली चलाई, जिसमें बड़ी संख्या में लोग मारे गए, और गोविंद गुरु को बंदी बनाया गया। यह स्थल, मानगढ़ धाम, अब एक स्मारक है। "
  "अन्य ने दूसरी जगह आंदोलन चलाए: अल्लूरी सीताराम राजू ने गोदावरी की पहाड़ियों में रंपा विद्रोह (1922-24), बिरसा मुंडा ने छोटा नागपुर में उलगुलान (1899-1900), और टंट्या भील ने 1889 में फाँसी दिए जाने तक मध्य भारत के निमाड़ क्षेत्र में लंबा प्रतिरोध।",
  MOD + "; Ministry of Culture (PIB), Mangarh Dham (2022).", "l3-t6-his-govind-guru-mangarh", pos=3, craft="recall")

S("Modern", "easy", "With reference to the national educational institutions set up during the Non-Cooperation Movement, consider the following statements:",
  "असहयोग आंदोलन के दौरान स्थापित राष्ट्रीय शैक्षिक संस्थाओं के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Gujarat Vidyapith was founded by Gandhi at Ahmedabad in 1920.",
   "Jamia Millia Islamia was founded at Aligarh in 1920 and later moved to Delhi.",
   "Bihar Vidyapith was founded at Calcutta."],
  ["गुजरात विद्यापीठ की स्थापना गांधीजी ने 1920 में अहमदाबाद में की थी।",
   "जामिया मिल्लिया इस्लामिया की स्थापना 1920 में अलीगढ़ में हुई और बाद में यह दिल्ली चला गया।",
   "बिहार विद्यापीठ की स्थापना कलकत्ता में हुई थी।"],
  C3, 1,
  "Statements 1 and 2 are correct. The boycott of government schools and colleges was part of the Non-Cooperation programme, and 'national' institutions were set up to take in the students who left: Gandhi founded Gujarat Vidyapith in October 1920; Jamia Millia Islamia was started at Aligarh in the same year by nationalist Muslims, among them Maulana Mohammad Ali and Hakim Ajmal Khan, and moved to Delhi in 1925; Kashi Vidyapith opened at Varanasi in 1921. "
  "Statement 3 is wrong: Bihar Vidyapith was founded at Patna in 1921, at Sadaqat Ashram, with Mazharul Haque and Rajendra Prasad among its leaders. Many of these institutions taught in Indian languages and combined academic study with spinning and village work, in line with the idea of national education.",
  "कथन 1 और 2 सही हैं। सरकारी स्कूलों और कॉलेजों का बहिष्कार असहयोग कार्यक्रम का भाग था, और छोड़कर आए विद्यार्थियों के लिए ‘राष्ट्रीय’ संस्थाएँ स्थापित की गईं: गांधीजी ने अक्टूबर 1920 में गुजरात विद्यापीठ की स्थापना की; जामिया मिल्लिया इस्लामिया उसी वर्ष अलीगढ़ में राष्ट्रवादी मुसलमानों, जिनमें मौलाना मोहम्मद अली और हकीम अजमल ख़ान थे, द्वारा शुरू की गई और 1925 में दिल्ली चली गई; काशी विद्यापीठ 1921 में वाराणसी में खुली। "
  "कथन 3 ग़लत है: बिहार विद्यापीठ की स्थापना 1921 में पटना में सदाक़त आश्रम में हुई, जिसके नेताओं में मज़हरुल हक़ और राजेंद्र प्रसाद थे। इनमें से अनेक संस्थाएँ भारतीय भाषाओं में पढ़ाती थीं और राष्ट्रीय शिक्षा के विचार के अनुरूप शैक्षिक अध्ययन को कताई और ग्राम-कार्य से जोड़ती थीं।",
  MOD + ".", "l3-t6-his-national-universities-1920", craft="recall")

S("Modern", "hard", "With reference to revolutionaries in Bengal in the early 1930s, consider the following statements:",
  "1930 के दशक के आरंभ में बंगाल के क्रांतिकारियों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Pritilata Waddedar led an attack on the Pahartali European Club in Chittagong in 1932 and took poison to avoid capture.",
   "Bina Das fired at the Governor of Bengal, Stanley Jackson, at a convocation of Calcutta University in 1932.",
   "Kalpana Dutt, a member of Surya Sen's group, was sentenced to transportation for life.",
   "Benoy, Badal and Dinesh raided the Writers' Building in Calcutta in 1930 and killed the Governor of Bengal."],
  ["प्रीतिलता वादेदार ने 1932 में चटगाँव के पहाड़तली यूरोपियन क्लब पर हमले का नेतृत्व किया और पकड़े जाने से बचने के लिए विष खा लिया।",
   "बीना दास ने 1932 में कलकत्ता विश्वविद्यालय के दीक्षांत समारोह में बंगाल के गवर्नर स्टैनली जैक्सन पर गोली चलाई।",
   "सूर्य सेन के समूह की सदस्य कल्पना दत्त को आजीवन कालापानी (देशनिकाला) की सज़ा दी गई।",
   "बिनय, बादल और दिनेश ने 1930 में कलकत्ता के राइटर्स बिल्डिंग पर धावा बोला और बंगाल के गवर्नर की हत्या की।"],
  C4, 2,
  "Statements 1, 2 and 3 are correct. After the Chittagong armoury raid of 1930, Surya Sen's Indian Republican Army drew young women into armed action: Pritilata, a schoolteacher, led the attack on a club known for barring Indians and swallowed cyanide when wounded; Kalpana Dutt was arrested soon after Sen, and while he was hanged in 1934 she was transported for life, later becoming active in the Communist Party. Bina Das, a student, fired at Jackson as he spoke at the convocation; she missed and was sentenced to nine years. "
  "Statement 4 is wrong in its target: in December 1930 Benoy Basu, Badal Gupta and Dinesh Gupta, of the Bengal Volunteers, entered the Writers' Building and shot dead Colonel N. S. Simpson, the Inspector-General of Prisons, notorious for the treatment of political prisoners; the square in front of it is now named B.B.D. Bagh after them. Women's part in this phase marked a break from earlier revolutionary groups, which had largely excluded them.",
  "कथन 1, 2 और 3 सही हैं। 1930 के चटगाँव शस्त्रागार छापे के बाद सूर्य सेन की इंडियन रिपब्लिकन आर्मी ने युवतियों को सशस्त्र कार्रवाई में शामिल किया: अध्यापिका प्रीतिलता ने भारतीयों को प्रवेश न देने के लिए कुख्यात एक क्लब पर हमले का नेतृत्व किया और घायल होने पर साइनाइड निगल लिया; कल्पना दत्त सेन के कुछ समय बाद गिरफ़्तार हुईं, और जहाँ सेन को 1934 में फाँसी दी गई, उन्हें आजीवन देशनिकाले की सज़ा मिली, जो बाद में कम्युनिस्ट पार्टी में सक्रिय रहीं। छात्रा बीना दास ने दीक्षांत समारोह में बोलते जैक्सन पर गोली चलाई; निशाना चूका और उन्हें नौ वर्ष की सज़ा हुई। "
  "कथन 4 अपने लक्ष्य में ग़लत है: दिसंबर 1930 में बंगाल वॉलंटियर्स के बिनय बसु, बादल गुप्ता और दिनेश गुप्ता ने राइटर्स बिल्डिंग में घुसकर जेलों के महानिरीक्षक कर्नल एन. एस. सिम्पसन को गोली मारी, जो राजनीतिक बंदियों के साथ व्यवहार के लिए कुख्यात थे; उसके सामने का चौक अब उनके नाम पर बी.बी.डी. बाग़ कहलाता है। इस चरण में महिलाओं की भागीदारी पहले के क्रांतिकारी समूहों से अलग थी, जिन्होंने उन्हें अधिकतर बाहर रखा था।",
  MOD + ".", "l3-t6-his-bengal-women-revolutionaries", craft="precision")

M("Modern", "medium",
  "The émigré Communist Party of India, formed by M. N. Roy and others in October 1920, was founded at:",
  "एम. एन. रॉय और अन्य द्वारा अक्टूबर 1920 में बनाई गई प्रवासी भारतीय कम्युनिस्ट पार्टी की स्थापना कहाँ हुई थी?",
  ["Tashkent", "Petrograd", "Berlin", "Kanpur"],
  ["ताशकंद", "पेत्रोग्राद", "बर्लिन", "कानपुर"],
  0,
  "M. N. Roy (Narendra Nath Bhattacharya), a revolutionary who had left India during the First World War, debated colonial strategy with Lenin at the Second Congress of the Communist International, which opened at Petrograd in 1920, and then, with Abani Mukherji and a few others, founded the Communist Party of India at Tashkent, where he was also training Indian muhajirs who had left for Afghanistan and Soviet Central Asia during the Khilafat agitation. "
  "Kanpur is the trap: a Communist conference held there in December 1925 is the date that one strand of the Indian communist movement treats as its founding. Inside India the early communists faced the Peshawar, Kanpur and Meerut conspiracy cases; Roy himself later broke with the Comintern and founded the Radical Democratic Party in 1940.",
  "एम. एन. रॉय (नरेंद्र नाथ भट्टाचार्य), एक क्रांतिकारी जो प्रथम विश्वयुद्ध के दौरान भारत छोड़ चुके थे, ने 1920 में पेत्रोग्राद में आरंभ हुई कम्युनिस्ट इंटरनेशनल की दूसरी कांग्रेस में लेनिन से औपनिवेशिक रणनीति पर बहस की और फिर अबनी मुखर्जी और कुछ अन्य के साथ ताशकंद में भारतीय कम्युनिस्ट पार्टी की स्थापना की, जहाँ वे उन भारतीय मुहाजिरों को प्रशिक्षण भी दे रहे थे जो ख़िलाफ़त आंदोलन के दौरान अफ़ग़ानिस्तान और सोवियत मध्य एशिया चले गए थे। "
  "कानपुर भ्रामक विकल्प है: दिसंबर 1925 में वहाँ हुआ एक कम्युनिस्ट सम्मेलन वह तिथि है जिसे भारतीय कम्युनिस्ट आंदोलन की एक धारा अपनी स्थापना मानती है। भारत के भीतर आरंभिक कम्युनिस्टों को पेशावर, कानपुर और मेरठ षड्यंत्र मामलों का सामना करना पड़ा; स्वयं रॉय ने बाद में कॉमिन्टर्न से नाता तोड़ा और 1940 में रैडिकल डेमोक्रेटिक पार्टी बनाई।",
  MOD + ".", "l3-t6-his-mn-roy-tashkent-1920", pos=0, craft="precision")

S("Modern", "medium", "With reference to industrial policy in colonial India after the First World War, consider the following statements:",
  "प्रथम विश्वयुद्ध के बाद औपनिवेशिक भारत में औद्योगिक नीति के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Indian Industrial Commission of 1916-18 recommended that the government take an active part in the industrial development of the country.",
   "The Fiscal Commission of 1921-22 recommended a policy of 'discriminating protection' for selected industries.",
   "A Tariff Board was set up in 1923 to examine claims of particular industries to protection.",
   "The steel industry received tariff protection under an Act passed in 1924."],
  ["1916-18 के भारतीय औद्योगिक आयोग ने सिफ़ारिश की कि सरकार देश के औद्योगिक विकास में सक्रिय भाग ले।",
   "1921-22 के राजकोषीय आयोग ने चुनिंदा उद्योगों के लिए ‘विभेदकारी संरक्षण’ की नीति की सिफ़ारिश की।",
   "विशेष उद्योगों के संरक्षण के दावों की जाँच के लिए 1923 में एक प्रशुल्क बोर्ड स्थापित किया गया।",
   "इस्पात उद्योग को 1924 में पारित एक अधिनियम के अंतर्गत प्रशुल्क संरक्षण मिला।"],
  C4, 3,
  "All four are correct. The war exposed how much India depended on imports for basic goods, and the Industrial Commission under Sir Thomas Holland proposed that the State promote industries, technical education and industrial departments in the provinces. The Fiscal Commission, chaired by Ibrahim Rahimtoola, rejected both free trade and blanket protection in favour of 'discriminating protection': an industry would qualify only if it had natural advantages, could not grow without help, and could eventually face world competition unaided. "
  "The Tariff Board applied these tests case by case, and steel -- the Tata works at Jamshedpur, hit by cheap imports after the war -- was the first to gain protection, under the Steel Industry (Protection) Act, 1924; cotton textiles, paper, sugar and others followed. Nationalists welcomed the shift but criticised how cautiously it was applied, and the policy was tied up with 'imperial preference' for British goods in the 1930s.",
  "चारों कथन सही हैं। युद्ध ने दिखाया कि भारत बुनियादी वस्तुओं के लिए आयात पर कितना निर्भर था, और सर थॉमस हॉलैंड के अधीन औद्योगिक आयोग ने प्रस्ताव किया कि राज्य उद्योगों, तकनीकी शिक्षा और प्रांतों में उद्योग विभागों को बढ़ावा दे। इब्राहिम रहमतुल्ला की अध्यक्षता वाले राजकोषीय आयोग ने मुक्त व्यापार और सर्वव्यापी संरक्षण दोनों को अस्वीकार कर ‘विभेदकारी संरक्षण’ अपनाया: कोई उद्योग तभी योग्य होता जब उसके पास प्राकृतिक लाभ हों, वह सहायता के बिना न बढ़ सके, और अंततः बिना सहायता के विश्व प्रतिस्पर्धा का सामना कर सके। "
  "प्रशुल्क बोर्ड ने इन कसौटियों को मामले-दर-मामले लागू किया, और इस्पात -- जमशेदपुर का टाटा कारख़ाना, जो युद्ध के बाद सस्ते आयात से प्रभावित हुआ था -- इस्पात उद्योग (संरक्षण) अधिनियम, 1924 के अंतर्गत संरक्षण पाने वाला पहला था; सूती वस्त्र, काग़ज़, चीनी और अन्य उसके बाद आए। राष्ट्रवादियों ने इस बदलाव का स्वागत किया पर इसके सतर्क क्रियान्वयन की आलोचना की, और 1930 के दशक में यह नीति ब्रिटिश वस्तुओं के लिए ‘साम्राज्यीय वरीयता’ से जुड़ गई।",
  MOD + ".", "l3-t6-his-fiscal-commission-discriminating-protection", craft="linkage")

S("Modern", "medium", "With reference to social reformers of the nineteenth and early twentieth centuries, consider the following statements:",
  "उन्नीसवीं और बीसवीं शताब्दी के आरंभ के समाज सुधारकों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Gopal Hari Deshmukh, known as 'Lokahitawadi', attacked caste and religious orthodoxy in his Marathi letters, the Shatapatre.",
   "Muthulakshmi Reddy campaigned against the dedication of girls to temples as devadasis.",
   "D. K. Karve founded India's first university for women at Calcutta."],
  ["‘लोकहितवादी’ के नाम से प्रसिद्ध गोपाल हरि देशमुख ने अपने मराठी पत्रों, शतपत्रे, में जाति और धार्मिक रूढ़िवाद पर प्रहार किया।",
   "मुथुलक्ष्मी रेड्डी ने लड़कियों को देवदासी के रूप में मंदिरों को समर्पित करने के विरुद्ध अभियान चलाया।",
   "डी. के. कर्वे ने कलकत्ता में महिलाओं के लिए भारत का पहला विश्वविद्यालय स्थापित किया।"],
  C3, 1,
  "Statements 1 and 2 are correct. Lokahitawadi's 'hundred letters', published in the weekly Prabhakar in the 1840s, argued for rational thought, the education of women and the end of the Brahmins' monopoly of learning, and he later supported the Prarthana Samaj. Muthulakshmi Reddy, a doctor and the first woman member of the Madras Legislative Council (1927), pressed for laws to end the devadasi system, which the Madras Devadasis (Prevention of Dedication) Act finally abolished in 1947; she also founded the Cancer Institute at Adyar. "
  "Statement 3 is wrong: Dhondo Keshav Karve founded the Indian Women's University in 1916 near Poona, at Hingne -- later the SNDT Women's University, now in Mumbai -- after earlier founding a home for widows; he was awarded the Bharat Ratna in 1958.",
  "कथन 1 और 2 सही हैं। लोकहितवादी के ‘सौ पत्र’, जो 1840 के दशक में साप्ताहिक प्रभाकर में छपे, तर्कसंगत विचार, स्त्री शिक्षा और ज्ञान पर ब्राह्मणों के एकाधिकार की समाप्ति के पक्ष में थे, और उन्होंने बाद में प्रार्थना समाज का समर्थन किया। चिकित्सक और मद्रास विधान परिषद की पहली महिला सदस्य (1927) मुथुलक्ष्मी रेड्डी ने देवदासी प्रथा समाप्त करने वाले क़ानूनों के लिए दबाव डाला, जिसे अंततः 1947 में मद्रास देवदासी (समर्पण निवारण) अधिनियम ने समाप्त किया; उन्होंने अड्यार में कैंसर संस्थान भी स्थापित किया। "
  "कथन 3 ग़लत है: धोंडो केशव कर्वे ने 1916 में पूना के पास हिंगणे में भारतीय महिला विश्वविद्यालय की स्थापना की -- बाद में एसएनडीटी महिला विश्वविद्यालय, अब मुंबई में -- इससे पहले उन्होंने विधवाओं के लिए एक आश्रम बनाया था; उन्हें 1958 में भारत रत्न मिला।",
  MOD + ".", "l3-t6-his-lokahitawadi-muthulakshmi-karve", craft="precision")

# ================================================================ ANCIENT (6)
M("Ancient", "easy",
  "In the later Vedic period, the 'ratnins' were:",
  "उत्तर वैदिक काल में ‘रत्नी’ कौन थे?",
  ["officials in whose houses the king made offerings at the Rajasuya",
   "guilds of jewellers and gem-cutters in the towns of the Ganga valley",
   "senior Buddhist monks who presided over the councils of the Sangha",
   "priests who chanted the hymns of the Sama Veda at the sacrifices"],
  ["अधिकारी जिनके घरों में राजा राजसूय पर आहुति देता था",
   "गंगा घाटी के नगरों में जौहरियों और रत्न काटने वालों के संघ",
   "संघ की परिषदों की अध्यक्षता करने वाले वरिष्ठ बौद्ध भिक्षु",
   "यज्ञों में सामवेद की ऋचाओं का गान करने वाले पुरोहित"],
  0,
  "As kingship grew stronger in the later Vedic period, the king came to rely on a set of high functionaries called ratnins, 'jewels' of the realm -- among them the purohita (chief priest), the senani (commander), the suta (charioteer and chronicler), the sangrahitri (treasurer), the bhagadugha (collector of the king's share), the gramani (village headman) and the chief queen. At the Rajasuya, the king visited the house of each ratnin to make an offering, a ritual that bound these figures to the king's consecration. "
  "The list shows a royal household and administration taking shape, though without a standing bureaucracy of the kind seen later. Sama Veda chanters were the udgatri priests, and guilds and monastic councils belong to the later age of towns and of Buddhism.",
  "उत्तर वैदिक काल में राजपद के मज़बूत होने के साथ राजा उच्च अधिकारियों के एक समूह पर निर्भर होने लगा जिन्हें रत्नी, राज्य के ‘रत्न’, कहा जाता था -- जिनमें पुरोहित (मुख्य पुरोहित), सेनानी (सेनापति), सूत (सारथी और वृत्तांतकार), संग्रहीतृ (कोषाध्यक्ष), भागदुघ (राजा का भाग वसूलने वाला), ग्रामणी (ग्राम-मुखिया) और पटरानी थे। राजसूय के समय राजा आहुति देने के लिए हर रत्नी के घर जाता था, एक अनुष्ठान जो इन व्यक्तियों को राजा के अभिषेक से बाँधता था। "
  "यह सूची राजकीय परिवार और प्रशासन को आकार लेते दिखाती है, यद्यपि बाद में दिखने वाली स्थायी नौकरशाही के बिना। सामवेद का गान करने वाले उद्गाता पुरोहित थे, और संघ तथा बौद्ध परिषदें नगरों और बौद्ध धर्म के बाद के युग की हैं।",
  ANC + "; " + TH1 + ".", "l3-t6-his-ratnins-rajasuya", pos=0, craft="recall")

S("Ancient", "easy", "With reference to early Indian medical texts, consider the following statements:",
  "प्राचीन भारतीय चिकित्सा ग्रंथों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Bower Manuscript, written on birch bark and containing medical texts, was found in Central Asia.",
   "Vagbhata's Ashtanga Hridaya is a treatise on astronomy and the calendar."],
  ["भोजपत्र पर लिखी और चिकित्सा ग्रंथों वाली बावर पांडुलिपि मध्य एशिया में मिली थी।",
   "वाग्भट का अष्टांग हृदय खगोल विज्ञान और पंचांग पर एक ग्रंथ है।"],
  T2, 0,
  "Only statement 1 is correct. The Bower Manuscript is named after Hamilton Bower, a British officer who bought it near Kucha in Xinjiang in 1890; written in the Gupta-period Brahmi script, it is among the oldest surviving Indian manuscripts, and includes medical treatises and charms, evidence of how Indian learning travelled along the Silk Road. "
  "Statement 2 is wrong: the Ashtanga Hridaya, attributed to Vagbhata (around the seventh century), is a compendium of Ayurveda covering its eight branches -- from general medicine and surgery to paediatrics and toxicology -- and together with the Charaka and Sushruta Samhitas it is counted among the 'great three' classics of Ayurveda; it was translated into Tibetan and Arabic.",
  "केवल कथन 1 सही है। बावर पांडुलिपि का नाम हैमिल्टन बावर पर है, एक ब्रिटिश अधिकारी जिन्होंने 1890 में शिनजियांग में कूचा के पास इसे ख़रीदा; गुप्तकालीन ब्राह्मी लिपि में लिखी यह सबसे पुरानी बची भारतीय पांडुलिपियों में है, और इसमें चिकित्सा ग्रंथ और मंत्र हैं, जो दिखाते हैं कि भारतीय ज्ञान रेशम मार्ग पर कैसे यात्रा करता था। "
  "कथन 2 ग़लत है: वाग्भट (लगभग सातवीं शताब्दी) को माना जाने वाला अष्टांग हृदय आयुर्वेद का संग्रह-ग्रंथ है, जो उसके आठ अंगों -- काय-चिकित्सा और शल्य से लेकर बाल-चिकित्सा और विष-विज्ञान तक -- को समेटता है, और चरक तथा सुश्रुत संहिताओं के साथ आयुर्वेद के ‘बृहत्त्रयी’ में गिना जाता है; इसका तिब्बती और अरबी में अनुवाद हुआ।",
  ANC + "; Ministry of Ayush.", "l3-t6-his-bower-manuscript-vagbhata", craft="recall")

S("Ancient", "hard", "With reference to archaeological sites in Tamil Nadu, consider the following statements:",
  "तमिलनाडु के पुरातात्विक स्थलों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Kodumanal, on the Noyyal river, was a centre of bead-making from gemstones and of iron working, and has yielded potsherds inscribed in Tamil-Brahmi.",
   "At Porunthal, near Palani, rice grains found in a megalithic burial have been dated to about the fifth century BCE.",
   "A report of the Tamil Nadu Archaeology Department in 2025 claimed dates in the fourth millennium BCE for iron objects from Sivagalai.",
   "All three sites lie in the Kaveri delta."],
  ["नोय्यल नदी पर कोडुमनल रत्न-पत्थरों से मनके बनाने और लौह-कर्म का केंद्र था, और यहाँ तमिल-ब्राह्मी में अंकित मृद्भांड-खंड मिले हैं।",
   "पलनी के पास पोरुंथल में एक महापाषाणिक समाधि में मिले चावल के दानों का काल लगभग पाँचवीं शताब्दी ईसा पूर्व आँका गया है।",
   "2025 में तमिलनाडु पुरातत्व विभाग की एक रिपोर्ट ने शिवगलई से मिली लोहे की वस्तुओं के लिए ईसा पूर्व चौथी सहस्राब्दी के काल का दावा किया।",
   "तीनों स्थल कावेरी डेल्टा में स्थित हैं।"],
  C4, 2,
  "Statements 1, 2 and 3 are correct. Kodumanal, in Erode district, is identified with the Kodumanam of the Sangam text Patirruppattu; its workshops processed beryl, quartz and carnelian into beads for trade and smelted iron, and its Tamil-Brahmi graffiti help date the script's spread. At Porunthal the paddy found in a jar in a megalithic grave, along with a Tamil-Brahmi inscription, was dated by AMS radiocarbon to around 490 BCE, pushing back the evidence for the script and for rice farming in the region. "
  "The Sivagalai results, announced in 2025, would place iron use in the region far earlier than elsewhere in India, and other archaeologists have urged caution until the dates are independently replicated -- a reminder that a scientific date is a claim to be tested, not a final fact. Statement 4 is wrong: Kodumanal is in the Kongu region on a tributary of the Kaveri, Porunthal is in the Palani hills area of Dindigul district, and Sivagalai lies in Thoothukudi district in the Tamirabarani basin.",
  "कथन 1, 2 और 3 सही हैं। इरोड ज़िले के कोडुमनल की पहचान संगम ग्रंथ पतिट्रुप्पत्तु के कोडुमणम से की जाती है; इसकी कार्यशालाएँ व्यापार के लिए बेरिल, क्वार्ट्ज़ और कार्नेलियन से मनके बनाती और लोहा गलाती थीं, और इसके तमिल-ब्राह्मी अंकन लिपि के प्रसार का काल तय करने में मदद करते हैं। पोरुंथल में एक महापाषाणिक समाधि के पात्र में मिले धान का, एक तमिल-ब्राह्मी अभिलेख के साथ, एएमएस रेडियोकार्बन से लगभग 490 ईसा पूर्व का काल आँका गया, जिससे क्षेत्र में लिपि और धान की खेती के प्रमाण पीछे गए। "
  "2025 में घोषित शिवगलई के परिणाम क्षेत्र में लोहे के उपयोग को भारत में अन्यत्र से बहुत पहले रखेंगे, और अन्य पुरातत्वविदों ने तिथियों की स्वतंत्र पुष्टि होने तक सावधानी की सलाह दी है -- यह याद दिलाता है कि वैज्ञानिक तिथि एक परखा जाने वाला दावा है, अंतिम तथ्य नहीं। कथन 4 ग़लत है: कोडुमनल कोंगु क्षेत्र में कावेरी की एक सहायक नदी पर है, पोरुंथल डिंडीगुल ज़िले के पलनी पहाड़ियों वाले क्षेत्र में है, और शिवगलई थूथुकुडी ज़िले में ताम्रपर्णी बेसिन में है।",
  "Tamil Nadu State Department of Archaeology, excavation reports (Kodumanal, Porunthal) and 'Antiquity of Iron' (2025); " + ASI + ".",
  "l3-t6-his-kodumanal-porunthal-sivagalai", craft="inference")

M("Ancient", "medium",
  "The Damodarpur copper plates of the Gupta period are an important source mainly because they record:",
  "गुप्तकालीन दामोदरपुर ताम्रपत्र मुख्यतः किस कारण एक महत्वपूर्ण स्रोत हैं? वे दर्ज करते हैं:",
  ["the military campaigns and conquests of Samudragupta across India",
   "the repair of the Sudarshana lake by a governor in Saurashtra",
   "Skandagupta's defence of the empire against the invading Hunas",
   "land sales approved by district officials in Gupta Bengal"],
  ["पूरे भारत में समुद्रगुप्त के सैन्य अभियान और विजय",
   "सौराष्ट्र में एक राज्यपाल द्वारा सुदर्शन झील की मरम्मत",
   "आक्रमणकारी हूणों के विरुद्ध स्कंदगुप्त द्वारा साम्राज्य की रक्षा",
   "गुप्तकालीन बंगाल में ज़िला अधिकारियों द्वारा स्वीकृत भूमि-विक्रय"],
  3,
  "The five plates from Damodarpur, in the north of present-day Bangladesh, span the reigns of Kumaragupta I to Budhagupta and record purchases of land -- often for religious gifts -- in the province (bhukti) of Pundravardhana. They show the procedure: an application to the district office (adhikarana) at Kotivarsha, consultation of the record-keepers, measurement of the plot and payment at a standard rate, and they name the members of the district council. "
  "That makes them rare evidence of how Gupta local administration actually worked and of the spread of land grants in Bengal. The distractors are other Gupta-era inscriptions: Samudragupta's campaigns are in the Allahabad Prashasti, the repair of the Sudarshana lake under Skandagupta in the Junagadh rock inscription, and the war against the Hunas in the Bhitari pillar inscription.",
  "दामोदरपुर, आज के बांग्लादेश के उत्तर में, के पाँच ताम्रपत्र कुमारगुप्त प्रथम से बुधगुप्त तक के शासनकाल के हैं और पुंड्रवर्धन भुक्ति (प्रांत) में भूमि की ख़रीद दर्ज करते हैं -- प्रायः धार्मिक दान के लिए। वे प्रक्रिया दिखाते हैं: कोटिवर्ष के ज़िला कार्यालय (अधिकरण) में आवेदन, अभिलेखपालों से परामर्श, भूखंड की नाप और मानक दर पर भुगतान, और वे ज़िला परिषद के सदस्यों के नाम देते हैं। "
  "इसलिए वे इस बात के दुर्लभ प्रमाण हैं कि गुप्तकालीन स्थानीय प्रशासन वास्तव में कैसे काम करता था और बंगाल में भूमि-अनुदान कैसे फैले। भ्रामक विकल्प अन्य गुप्तकालीन अभिलेख हैं: समुद्रगुप्त के अभियान प्रयाग प्रशस्ति में, स्कंदगुप्त के अधीन सुदर्शन झील की मरम्मत जूनागढ़ शिलालेख में, और हूणों के विरुद्ध युद्ध भितरी स्तंभ लेख में है।",
  ANC + "; " + TH1 + ", 'Kings, Farmers and Towns'.", "l3-t6-his-damodarpur-plates", pos=3, craft="inference")

S("Ancient", "medium", "With reference to the Buddhist site of Bhattiprolu, consider the following statements:",
  "भट्टिप्रोलु के बौद्ध स्थल के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Bhattiprolu, in the Krishna delta of Andhra Pradesh, has a Buddhist stupa dating from about the third or second century BCE.",
   "The inscriptions on the relic caskets found in its stupa are written in a variant of the Brahmi script.",
   "The caskets were found to contain relics of Mahavira."],
  ["आंध्र प्रदेश के कृष्णा डेल्टा में स्थित भट्टिप्रोलु में लगभग तीसरी या दूसरी शताब्दी ईसा पूर्व का एक बौद्ध स्तूप है।",
   "इसके स्तूप में मिले अस्थि-मंजूषाओं के अभिलेख ब्राह्मी लिपि के एक रूप में लिखे हैं।",
   "मंजूषाओं में महावीर के अवशेष पाए गए।"],
  C3, 1,
  "Statements 1 and 2 are correct. Excavated in the 1870s and 1890s, the stupa at Bhattiprolu yielded crystal and stone caskets whose inscriptions record the deposit of relics of the Buddha by local guilds and a king named Kubiraka; the script is a regional form of Brahmi -- sometimes called the Bhattiprolu script -- with distinctive ways of writing vowels that suit Dravidian sounds, and it is discussed in debates on how Tamil-Brahmi and the scripts of the south developed. "
  "Statement 3 is wrong: the relics are of the Buddha. Bhattiprolu belongs to the cluster of early stupas in the lower Krishna valley -- with Amaravati and, later, Nagarjunakonda -- that made Andhra a major centre of Buddhism, supported by merchants trading across the Bay of Bengal.",
  "कथन 1 और 2 सही हैं। 1870 और 1890 के दशकों में उत्खनित भट्टिप्रोलु के स्तूप से स्फटिक और पत्थर की मंजूषाएँ मिलीं जिनके अभिलेख स्थानीय संघों और कुबिरक नामक राजा द्वारा बुद्ध के अवशेष रखे जाने को दर्ज करते हैं; लिपि ब्राह्मी का एक क्षेत्रीय रूप है -- जिसे कभी-कभी भट्टिप्रोलु लिपि कहा जाता है -- जिसमें स्वर लिखने के विशिष्ट ढंग द्रविड़ ध्वनियों के अनुकूल हैं, और यह इस बहस में आती है कि तमिल-ब्राह्मी और दक्षिण की लिपियाँ कैसे विकसित हुईं। "
  "कथन 3 ग़लत है: अवशेष बुद्ध के हैं। भट्टिप्रोलु निचली कृष्णा घाटी के आरंभिक स्तूपों के समूह का भाग है -- अमरावती और बाद में नागार्जुनकोंडा के साथ -- जिन्होंने बंगाल की खाड़ी के पार व्यापार करने वाले व्यापारियों के सहयोग से आंध्र को बौद्ध धर्म का प्रमुख केंद्र बनाया।",
  ASI + ", Bhattiprolu stupa; " + TH1 + ".", "l3-t6-his-bhattiprolu-stupa-script", craft="precision")

S("Ancient", "medium", "With reference to Chandraketugarh in West Bengal, consider the following statements:",
  "पश्चिम बंगाल के चंद्रकेतुगढ़ के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is known for its finely made terracotta plaques, many of the Shunga-Kushana period.",
   "It lies near the Bidyadhari river in North 24 Parganas district.",
   "Excavations show that it was occupied over a long span, from the pre-Mauryan to the Pala period."],
  ["यह अपनी सुंदर टेराकोटा पट्टिकाओं के लिए प्रसिद्ध है, जिनमें से अनेक शुंग-कुषाण काल की हैं।",
   "यह उत्तर 24 परगना ज़िले में विद्याधरी नदी के पास स्थित है।",
   "उत्खनन दिखाते हैं कि यहाँ मौर्य-पूर्व से पाल काल तक लंबी अवधि तक बसावट रही।"],
  C3, 2,
  "All three are correct. Chandraketugarh, about 35 km north-east of Kolkata, has produced thousands of terracotta plaques and figurines -- yakshis, scenes of daily life, animals and ships -- along with seals, beads and coins, and its rampart and ceramics point to a large town. Excavations by the Asutosh Museum of Calcutta University and the ASI found a sequence of occupation from the pre-Mauryan period to the Pala-Sena age. "
  "Its location on a river close to the Ganga delta, and finds of seals showing ships, have led some scholars to identify it with the 'Gange' or 'Gangaridai' of Greek and Roman writers, a port trading with South-East Asia and the Mediterranean world -- a link that remains a hypothesis. Much of the site's material has been dispersed through illegal digging, which is why many plaques are known only from private collections.",
  "तीनों कथन सही हैं। कोलकाता से लगभग 35 किलोमीटर उत्तर-पूर्व में चंद्रकेतुगढ़ से हज़ारों टेराकोटा पट्टिकाएँ और मूर्तियाँ मिली हैं -- यक्षियाँ, दैनिक जीवन के दृश्य, पशु और जहाज़ -- साथ ही मुहरें, मनके और सिक्के, और इसका प्राचीर तथा मृद्भांड एक बड़े नगर की ओर संकेत करते हैं। कलकत्ता विश्वविद्यालय के आशुतोष संग्रहालय और एएसआई के उत्खनन में मौर्य-पूर्व काल से पाल-सेन युग तक बसावट का क्रम मिला। "
  "गंगा डेल्टा के पास नदी पर इसकी स्थिति, और जहाज़ दिखाने वाली मुहरों की प्राप्ति ने कुछ विद्वानों को इसे यूनानी और रोमन लेखकों के ‘गंगे’ या ‘गंगरिदाई’ से जोड़ने को प्रेरित किया है, एक बंदरगाह जो दक्षिण-पूर्व एशिया और भूमध्यसागरीय संसार से व्यापार करता था -- यह संबंध अब भी परिकल्पना है। स्थल की बहुत सी सामग्री अवैध खुदाई से बिखर गई है, इसीलिए अनेक पट्टिकाएँ केवल निजी संग्रहों से ज्ञात हैं।",
  ASI + ", Chandraketugarh; NCERT Class XI, An Introduction to Indian Art.", "l3-t6-his-chandraketugarh-terracotta", craft="precision")

# ================================================================ MUSIC & DANCE (1)
P("Music & Dance", "hard", "Consider the following pairs of semi-classical and folk-based forms of Hindustani music and the seasons, festivals or features with which they are associated:",
  "हिंदुस्तानी संगीत के उपशास्त्रीय और लोक-आधारित रूपों तथा उनसे जुड़ी ऋतुओं, पर्वों या विशेषताओं के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Kajri : The rainy season", "Chaiti : The month of Chaitra", "Hori : The festival of Holi", "Dadra : The six-beat tala of the same name"],
  ["कजरी : वर्षा ऋतु", "चैती : चैत्र मास", "होरी : होली का पर्व", "दादरा : इसी नाम का छह मात्राओं का ताल"],
  3,
  "All four pairs are correct. Kajri, from the region of Mirzapur and Banaras, is sung in the rains, often voicing a woman's longing for an absent husband; Chaiti is sung in Chaitra, the first month of spring, its verses often ending with the refrain 'Rama'; and Hori celebrates the play of colours of Radha and Krishna at Holi, in a dhamar or lighter rhythm. Singers of the Banaras tradition such as Siddheshwari Devi and Girija Devi brought these forms into the concert repertoire alongside thumri. "
  "Dadra is a light classical form usually set to dadra tala of six beats, lighter and quicker than thumri. The common thread is that these forms are defined by season, festival or rhythm rather than by raga alone, which is why they are classed as semi-classical.",
  "चारों युग्म सही हैं। मिर्ज़ापुर और बनारस क्षेत्र की कजरी वर्षा में गाई जाती है, जो प्रायः अनुपस्थित पति के लिए स्त्री की विरह-वेदना व्यक्त करती है; चैती वसंत के पहले महीने चैत्र में गाई जाती है, जिसके पद प्रायः ‘रामा’ टेक पर समाप्त होते हैं; और होरी होली पर राधा और कृष्ण के रंग-खेल का उत्सव मनाती है, धमार या हल्की लय में। सिद्धेश्वरी देवी और गिरिजा देवी जैसी बनारस परंपरा की गायिकाओं ने इन रूपों को ठुमरी के साथ संगीत-सभाओं में पहुँचाया। "
  "दादरा एक हल्का शास्त्रीय रूप है जो सामान्यतः छह मात्राओं के दादरा ताल में होता है, ठुमरी से हल्का और तेज़। साझा सूत्र यह है कि ये रूप केवल राग से नहीं बल्कि ऋतु, पर्व या लय से परिभाषित होते हैं, इसीलिए इन्हें उपशास्त्रीय माना जाता है।",
  MUS + ".", "l3-t6-his-kajri-chaiti-hori-dadra", craft="precision")

# ================================================================ MEDIEVAL (3)
P("Medieval", "medium", "Consider the following pairs of departments of the Delhi Sultanate and their functions:",
  "दिल्ली सल्तनत के विभागों और उनके कार्यों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Diwan-i-Wizarat : Finance and revenue", "Diwan-i-Insha : Royal correspondence",
   "Barid-i-Mumalik : Intelligence and news-reporting", "Diwan-i-Risalat : Public works"],
  ["दीवान-ए-विज़ारत : वित्त और राजस्व", "दीवान-ए-इंशा : शाही पत्राचार",
   "बरीद-ए-मुमालिक : गुप्तचर और समाचार-संग्रह", "दीवान-ए-रिसालत : लोक निर्माण कार्य"],
  2,
  "The first three pairs are correct. The wazir headed the Diwan-i-Wizarat, which assessed and collected revenue and supervised expenditure; the Diwan-i-Insha, under the dabir-i-mumalik, drafted the Sultan's farmans and handled correspondence with governors and other rulers; and the barid-i-mumalik ran a network of news-writers (barids) posted in the provinces, a system that rulers such as Balban and Alauddin used to keep nobles and officials in check. "
  "The fourth pair is wrong: the Diwan-i-Risalat dealt with religious matters -- pious foundations and stipends to scholars and holy men -- and was linked to the office of the chief sadr. Public works had no separate central department of this name, though Firuz Shah Tughlaq was known for building canals, towns and sarais.",
  "पहले तीन युग्म सही हैं। वज़ीर दीवान-ए-विज़ारत का प्रमुख था, जो राजस्व का आकलन और संग्रह करता तथा व्यय की निगरानी करता था; दबीर-ए-मुमालिक के अधीन दीवान-ए-इंशा सुल्तान के फ़रमान तैयार करता और सूबेदारों तथा अन्य शासकों से पत्राचार करता था; और बरीद-ए-मुमालिक प्रांतों में नियुक्त समाचार-लेखकों (बरीदों) का जाल चलाता था, एक व्यवस्था जिसका प्रयोग बलबन और अलाउद्दीन जैसे शासकों ने सरदारों और अधिकारियों पर नियंत्रण रखने के लिए किया। "
  "चौथा युग्म ग़लत है: दीवान-ए-रिसालत धार्मिक विषयों -- धार्मिक न्यासों और विद्वानों तथा संतों को वृत्तियों -- से संबंधित था और मुख्य सद्र के पद से जुड़ा था। लोक निर्माण का इस नाम का कोई अलग केंद्रीय विभाग नहीं था, यद्यपि फ़िरोज़ शाह तुग़लक़ नहरें, नगर और सराएँ बनवाने के लिए प्रसिद्ध था।",
  MED + "; " + OP2 + ".", "l3-t6-his-sultanate-departments-wizarat-insha-barid", craft="precision")

M("Medieval", "medium",
  "In the Vijayanagara empire, the 'ayagars' were:",
  "विजयनगर साम्राज्य में ‘आयगार’ कौन थे?",
  ["village functionaries who held tax-free land for serving the village",
   "military chiefs who held territories in return for maintaining troops",
   "temple priests who managed the endowments of the great temples",
   "merchants who imported horses from Arabia and Central Asia"],
  ["ग्राम-सेवा के बदले कर-मुक्त भूमि रखने वाले गाँव के पदाधिकारी",
   "सेना रखने के बदले क्षेत्र प्राप्त करने वाले सैन्य सरदार",
   "बड़े मंदिरों के दान-न्यासों का प्रबंध करने वाले मंदिर-पुरोहित",
   "अरब और मध्य एशिया से घोड़े आयात करने वाले व्यापारी"],
  0,
  "Under the ayagar system, each village had a set of hereditary functionaries -- usually twelve -- such as the headman, the accountant (karnam), the watchman (talari), the blacksmith, carpenter, potter and washerman, who served the village and were paid with plots of tax-free land (manyam) or a share of the produce; they could not sell their office. The arrangement made the village a largely self-managing unit under the oversight of the nayakas. "
  "Option (b) describes the amara-nayakas, the military chiefs at the heart of the empire's political system, and option (d) the horse merchants (kudirai chettis) on whom the empire's cavalry depended; the temples were run by their own trustees and priests.",
  "आयगार व्यवस्था में हर गाँव में वंशानुगत पदाधिकारियों का एक समूह -- प्रायः बारह -- होता था, जैसे मुखिया, लेखाकार (कर्णम), चौकीदार (तलारी), लोहार, बढ़ई, कुम्हार और धोबी, जो गाँव की सेवा करते और उन्हें कर-मुक्त भूमि के टुकड़े (मान्यम) या उपज का हिस्सा मिलता था; वे अपना पद बेच नहीं सकते थे। इस व्यवस्था ने नायकों की निगरानी में गाँव को काफ़ी हद तक स्वशासी इकाई बनाया। "
  "विकल्प (ख) अमर-नायकों का वर्णन करता है, जो साम्राज्य की राजनीतिक व्यवस्था के केंद्र में सैन्य सरदार थे, और विकल्प (घ) उन घोड़ा व्यापारियों (कुदिरै चेट्टी) का जिन पर साम्राज्य की घुड़सेना निर्भर थी; मंदिर अपने न्यासियों और पुरोहितों द्वारा चलाए जाते थे।",
  MED + "; " + TH2 + ", 'An Imperial Capital: Vijayanagara'.", "l3-t6-his-vijayanagara-ayagars", pos=0, craft="recall")

S("Medieval", "medium", "With reference to literature in Tamil and Kannada in the early medieval period, consider the following statements:",
  "आरंभिक मध्यकाल में तमिल और कन्नड़ साहित्य के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Kamban composed a Tamil version of the Ramayana in the Chola period.",
   "Pampa, Ponna and Ranna, honoured as the 'three gems', wrote in Kannada.",
   "Sekkizhar's Periya Puranam is a Kannada work on the lives of the Alvars."],
  ["कंबन ने चोल काल में रामायण का तमिल रूप रचा।",
   "‘तीन रत्न’ के रूप में सम्मानित पम्प, पोन्न और रन्न ने कन्नड़ में लिखा।",
   "सेक्किलार का पेरिय पुराणम् आलवारों के जीवन पर एक कन्नड़ कृति है।"],
  C3, 1,
  "Statements 1 and 2 are correct. Kamban's Ramavataram, of the twelfth century, retells Valmiki's story with a Tamil sensibility and is counted among the greatest works of Tamil literature. Pampa (author of the Vikramarjuna Vijaya and the Jain Adipurana), Ponna and Ranna, poets of the tenth century patronised by the Rashtrakutas and later Chalukyas, set the classical style of Kannada poetry. "
  "Statement 3 is wrong twice: the Periya Puranam, written by Sekkizhar at the court of the Chola king Kulottunga II, is in Tamil, and it tells the lives of the sixty-three Nayanars, the Shaiva saints, not of the Alvars, who were Vaishnava. Royal patronage of such works shows how bhakti and court culture reinforced each other under the Cholas.",
  "कथन 1 और 2 सही हैं। बारहवीं शताब्दी का कंबन का रामावतारम् वाल्मीकि की कथा को तमिल संवेदना के साथ पुनः कहता है और तमिल साहित्य की महानतम कृतियों में गिना जाता है। पम्प (विक्रमार्जुन विजय और जैन आदिपुराण के रचयिता), पोन्न और रन्न, राष्ट्रकूटों और बाद के चालुक्यों द्वारा संरक्षित दसवीं शताब्दी के कवियों, ने कन्नड़ काव्य की शास्त्रीय शैली तय की। "
  "कथन 3 दो कारणों से ग़लत है: चोल राजा कुलोत्तुंग द्वितीय के दरबार में सेक्किलार द्वारा लिखा पेरिय पुराणम् तमिल में है, और यह शैव संतों, तिरसठ नायनारों, के जीवन का वर्णन करता है, वैष्णव आलवारों का नहीं। ऐसी कृतियों का राजकीय संरक्षण दिखाता है कि चोलों के अधीन भक्ति और दरबारी संस्कृति एक-दूसरे को कैसे सुदृढ़ करती थीं।",
  OP2 + "; " + MED + ".", "l3-t6-his-kamban-kannada-gems-periya-puranam", craft="precision")

write("gs_l3_t6_b.sql")
