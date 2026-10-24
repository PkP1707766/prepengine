# -*- coding: utf-8 -*-
"""Level 3 · Test 5 (GS Integrated Test 5) -- part B: History (16) (upsc_l3_cell_targets.mjs 5).
History cells: Modern e-MCQ, e-stmt, h-stmt, m-MCQ, m-stmt x2; Ancient e-MCQ, e-stmt, h-stmt, m-MCQ, m-stmt x2;
Medieval m-MCQ, m-stmt, m-pairs; Music & Dance h-pairs.
Every fact was searched in the whole UPSC bank (l3_tools/bank_find.py) and is one no row tests: Mahendralal Sircar and
the IACS; the Hindu Patriot, Swadesamitran and Som Prakash; the Factory Acts of 1881 and 1891 and N. M. Lokhande;
Badruddin Tyabji; the Ahmadiyya, Nadwat-ul-Ulama and Barelvi movements; Curzon's Ancient Monuments, Universities and
Calcutta Corporation Acts; Assaka; bhukti, uparika and hereditary Gupta offices; the Kushana devakula at Mat;
Mahendravarman I and the Mattavilasa; Vadnagar; Kanganahalli; Alarippu, Tarangam, Batu and Cholkettu; Maneri, Nund
Rishi, Hamadani and Hamiduddin Nagauri; 'Hindu Suratrana'; village artisans, jajmani and women's work in Mughal
India. MCQ keys are pinned."""
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
OP1 = "NCERT Class VI, Our Pasts I"
OP2 = "NCERT Class VII, Our Pasts II"
MUS = "NCERT Class XI, An Introduction to Indian Art; Sangeet Natak Akademi"
ASI = "Archaeological Survey of India"

# ================================================================ MODERN (6)
M("Modern", "easy",
  "The Indian Association for the Cultivation of Science, in whose laboratory C. V. Raman did the work that led to the discovery of the Raman effect, was founded in 1876 by:",
  "इंडियन एसोसिएशन फ़ॉर द कल्टीवेशन ऑफ़ साइंस, जिसकी प्रयोगशाला में सी. वी. रमन ने वह काम किया जिससे रमन प्रभाव की खोज हुई, की स्थापना 1876 में किसने की थी?",
  ["Jagadish Chandra Bose", "Ashutosh Mukherjee", "Prafulla Chandra Ray", "Mahendralal Sircar"],
  ["जगदीश चंद्र बसु", "आशुतोष मुखर्जी", "प्रफुल्ल चंद्र राय", "महेंद्रलाल सरकार"],
  3,
  "Mahendralal Sircar, a Calcutta physician, founded the Association in 1876 so that Indians could pursue science on their own initiative, on the model of the Royal Institution in London. C. V. Raman, then an officer in the Finance Department, began working in its laboratory in 1907 and announced the scattering effect from there in 1928 -- 28 February is now National Science Day -- and won the Nobel Prize in Physics in 1930. "
  "The distractors are close neighbours: Ashutosh Mukherjee set up the University College of Science in Calcutta, where Raman became Palit Professor in 1917; J. C. Bose founded the Bose Institute in 1917; and P. C. Ray founded Bengal Chemicals.",
  "कलकत्ता के चिकित्सक महेंद्रलाल सरकार ने 1876 में इस संस्था की स्थापना की ताकि भारतीय अपनी पहल पर विज्ञान का अध्ययन कर सकें; इसका आदर्श लंदन का रॉयल इंस्टीट्यूशन था। सी. वी. रमन, जो तब वित्त विभाग में अधिकारी थे, ने 1907 में इसकी प्रयोगशाला में काम शुरू किया और 1928 में वहीं से प्रकीर्णन प्रभाव की घोषणा की -- 28 फ़रवरी अब राष्ट्रीय विज्ञान दिवस है -- और 1930 में भौतिकी का नोबेल पुरस्कार जीता। "
  "विकल्प निकट के नाम हैं: आशुतोष मुखर्जी ने कलकत्ता में यूनिवर्सिटी कॉलेज ऑफ़ साइंस स्थापित किया, जहाँ रमन 1917 में पालित प्रोफ़ेसर बने; जे. सी. बसु ने 1917 में बोस इंस्टीट्यूट की स्थापना की; और पी. सी. राय ने बंगाल केमिकल्स की स्थापना की।",
  "Indian Association for the Cultivation of Science, Kolkata (history of the institution); Department of Science and Technology (National Science Day).",
  "l3-t5-his-iacs-mahendralal-sircar", pos=3, craft="linkage")

S("Modern", "easy", "With reference to the Indian-owned press of the nineteenth century, consider the following statements:",
  "उन्नीसवीं शताब्दी के भारतीय स्वामित्व वाले समाचार-पत्रों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Hindu Patriot, edited by Harish Chandra Mukherjee, took up the cause of the indigo cultivators of Bengal.",
   "Swadesamitran, founded by G. Subramania Iyer, was a Tamil newspaper.",
   "Som Prakash, edited by Dwarkanath Vidyabhushan, was an English-language weekly."],
  ["हरिश्चंद्र मुखर्जी द्वारा संपादित हिंदू पैट्रियट ने बंगाल के नील उत्पादकों का पक्ष लिया।",
   "जी. सुब्रमण्य अय्यर द्वारा स्थापित स्वदेशमित्रन एक तमिल समाचार-पत्र था।",
   "द्वारकानाथ विद्याभूषण द्वारा संपादित सोम प्रकाश एक अंग्रेज़ी भाषा का साप्ताहिक था।"],
  C3, 1,
  "Statements 1 and 2 are correct. Harish Chandra Mukherjee made the Hindu Patriot the voice of the peasants during the indigo revolt of 1859-60, reporting the planters' oppression and backing the cultivators' refusal to grow indigo. G. Subramania Iyer, one of the founders of The Hindu (1878), started Swadesamitran in 1882, and it became a leading nationalist daily in Tamil. "
  "Statement 3 is wrong: Som Prakash, started in 1858 with the encouragement of Ishwar Chandra Vidyasagar, was a Bengali weekly -- the kind of Indian-language paper at which the Vernacular Press Act of 1878 was aimed.",
  "कथन 1 और 2 सही हैं। हरिश्चंद्र मुखर्जी ने 1859-60 के नील विद्रोह के दौरान हिंदू पैट्रियट को किसानों की आवाज़ बनाया, बागान मालिकों के अत्याचार की ख़बरें छापीं और नील न उगाने के किसानों के निर्णय का समर्थन किया। द हिंदू (1878) के संस्थापकों में से एक जी. सुब्रमण्य अय्यर ने 1882 में स्वदेशमित्रन शुरू किया, जो तमिल का एक प्रमुख राष्ट्रवादी दैनिक बना। "
  "कथन 3 ग़लत है: ईश्वरचंद्र विद्यासागर के प्रोत्साहन से 1858 में शुरू हुआ सोम प्रकाश एक बांग्ला साप्ताहिक था -- उसी तरह का भारतीय भाषा का पत्र जिसे 1878 का वर्नाक्युलर प्रेस एक्ट निशाना बनाता था।",
  MOD + ".", "l3-t5-his-hindu-patriot-swadesamitran-som-prakash", craft="recall")

S("Modern", "hard", "With reference to the early factory laws and labour organisation in colonial India, consider the following statements:",
  "औपनिवेशिक भारत में आरंभिक कारख़ाना क़ानूनों और श्रमिक संगठन के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Factory Act of 1881 was passed partly under pressure from Lancashire textile interests, who argued that cheap Indian labour gave Indian mills an unfair advantage.",
   "Most early nationalist leaders supported the Factory Acts of 1881 and 1891 as a protection for workers.",
   "The Factory Act of 1891 limited the working hours of women in factories.",
   "N. M. Lokhande, an associate of Jyotiba Phule, organised the Bombay Mill Hands' Association in 1890."],
  ["1881 का कारख़ाना अधिनियम आंशिक रूप से लंकाशायर के वस्त्र हितों के दबाव में पारित हुआ, जिनका तर्क था कि सस्ता भारतीय श्रम भारतीय मिलों को अनुचित लाभ देता है।",
   "अधिकांश आरंभिक राष्ट्रवादी नेताओं ने 1881 और 1891 के कारख़ाना अधिनियमों का श्रमिकों के संरक्षण के रूप में समर्थन किया।",
   "1891 के कारख़ाना अधिनियम ने कारख़ानों में महिलाओं के काम के घंटे सीमित किए।",
   "ज्योतिबा फुले के सहयोगी एन. एम. लोखंडे ने 1890 में बॉम्बे मिल हैंड्स एसोसिएशन संगठित किया।"],
  C4, 2,
  "Statements 1, 3 and 4 are correct. The Act of 1881 barred children under seven from factories and limited the hours of those aged seven to twelve; the Act of 1891 raised the minimum age to nine, limited women's work to eleven hours a day with a break, and gave a weekly holiday. British mill-owners had pressed for such laws to blunt the cost advantage of the Bombay mills. N. M. Lokhande, a member of Phule's Satyashodhak circle, formed the Bombay Mill Hands' Association and petitioned for shorter hours and a weekly rest day -- an early step in labour organisation in India. "
  "Statement 2 is wrong: many early nationalists opposed these Acts, fearing that they would erode the competitiveness of Indian-owned mills, and saw them as serving Lancashire rather than Indian workers. Their critique of colonial economic policy did not at first extend to the conditions of labour in Indian factories -- a gap that later labour and socialist leaders pointed out.",
  "कथन 1, 3 और 4 सही हैं। 1881 के अधिनियम ने सात वर्ष से कम आयु के बच्चों को कारख़ानों से रोका और सात से बारह वर्ष के बच्चों के घंटे सीमित किए; 1891 के अधिनियम ने न्यूनतम आयु नौ वर्ष की, महिलाओं के काम को विश्राम सहित ग्यारह घंटे प्रतिदिन तक सीमित किया, और साप्ताहिक अवकाश दिया। ब्रिटिश मिल मालिकों ने बंबई की मिलों के लागत-लाभ को कुंद करने के लिए ऐसे क़ानूनों का दबाव बनाया था। फुले के सत्यशोधक समूह के सदस्य एन. एम. लोखंडे ने बॉम्बे मिल हैंड्स एसोसिएशन बनाया और कम घंटों तथा साप्ताहिक विश्राम दिवस के लिए याचिका दी -- भारत में श्रमिक संगठन का एक आरंभिक क़दम। "
  "कथन 2 ग़लत है: अनेक आरंभिक राष्ट्रवादियों ने इन अधिनियमों का विरोध किया, इस भय से कि इनसे भारतीय स्वामित्व वाली मिलों की प्रतिस्पर्धा क्षमता घटेगी, और इन्हें भारतीय श्रमिकों के बजाय लंकाशायर के हित में देखा। औपनिवेशिक आर्थिक नीति की उनकी आलोचना पहले भारतीय कारख़ानों में श्रम की परिस्थितियों तक नहीं पहुँची -- इस कमी की ओर बाद में श्रमिक और समाजवादी नेताओं ने ध्यान दिलाया।",
  MOD + ".", "l3-t5-his-factory-acts-1881-1891-lokhande", craft="inference")

M("Modern", "medium",
  "The first Muslim to preside over a session of the Indian National Congress was:",
  "भारतीय राष्ट्रीय कांग्रेस के किसी अधिवेशन की अध्यक्षता करने वाले पहले मुस्लिम कौन थे?",
  ["Badruddin Tyabji", "Rahimtulla M. Sayani", "Nawab Syed Muhammad Bahadur", "Hakim Ajmal Khan"],
  ["बदरुद्दीन तैयबजी", "रहीमतुल्ला एम. सयानी", "नवाब सैयद मुहम्मद बहादुर", "हकीम अजमल ख़ान"],
  0,
  "Badruddin Tyabji, a Bombay barrister and later a judge of the Bombay High Court, presided over the third session, at Madras in 1887; he had helped found the Bombay Presidency Association with Pherozeshah Mehta and K. T. Telang. At the next session, at Allahabad in 1888 under George Yule -- the first Englishman to preside -- the Congress adopted a rule that it would not pass a resolution to which an overwhelming majority of Hindu or Muslim delegates objected, an early attempt to reassure Muslim opinion. "
  "Rahimtulla Sayani presided at Calcutta in 1896, Nawab Syed Muhammad Bahadur at Karachi in 1913, and Hakim Ajmal Khan at Ahmedabad in 1921, in place of C. R. Das, who was in jail.",
  "बंबई के बैरिस्टर और बाद में बंबई उच्च न्यायालय के न्यायाधीश बदरुद्दीन तैयबजी ने 1887 में मद्रास में हुए तीसरे अधिवेशन की अध्यक्षता की; उन्होंने फ़िरोज़शाह मेहता और के. टी. तेलंग के साथ बॉम्बे प्रेसिडेंसी एसोसिएशन की स्थापना में सहायता की थी। अगले अधिवेशन, 1888 में इलाहाबाद में जॉर्ज यूल -- अध्यक्षता करने वाले पहले अंग्रेज़ -- के अधीन कांग्रेस ने नियम अपनाया कि वह ऐसा कोई प्रस्ताव पारित नहीं करेगी जिस पर हिंदू या मुस्लिम प्रतिनिधियों का भारी बहुमत आपत्ति करे; यह मुस्लिम जनमत को आश्वस्त करने का एक आरंभिक प्रयास था। "
  "रहीमतुल्ला सयानी ने 1896 में कलकत्ता में, नवाब सैयद मुहम्मद बहादुर ने 1913 में कराची में, और हकीम अजमल ख़ान ने 1921 में अहमदाबाद में जेल में बंद सी. आर. दास के स्थान पर अध्यक्षता की।",
  MOD + "; Indian National Congress, list of sessions and presidents.",
  "l3-t5-his-badruddin-tyabji-1887", pos=0, craft="recall")

S("Modern", "medium", "With reference to Muslim religious movements in nineteenth-century India, consider the following statements:",
  "उन्नीसवीं शताब्दी के भारत में मुस्लिम धार्मिक आंदोलनों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Ahmadiyya movement was founded by Mirza Ghulam Ahmad at Qadian in Punjab.",
   "The Nadwat-ul-Ulama, in whose founding Shibli Nomani played a leading part, set up its seminary at Aligarh.",
   "The Barelvi movement, led by Ahmad Raza Khan, rejected the veneration of saints and their shrines."],
  ["अहमदिया आंदोलन की स्थापना मिर्ज़ा ग़ुलाम अहमद ने पंजाब के क़ादियान में की थी।",
   "नदवतुल उलेमा, जिसकी स्थापना में शिबली नोमानी ने प्रमुख भूमिका निभाई, ने अपना मदरसा अलीगढ़ में स्थापित किया।",
   "अहमद रज़ा ख़ान के नेतृत्व वाले बरेलवी आंदोलन ने संतों और उनकी दरगाहों की पूजा को अस्वीकार किया।"],
  C3, 0,
  "Only statement 1 is correct. Mirza Ghulam Ahmad founded the Ahmadiyya movement in 1889 at Qadian, in Gurdaspur district; it described itself as a standard-bearer of an Islamic renaissance, set up schools on Western lines and preached a jihad of the pen rather than of the sword. "
  "Statement 2 is wrong: the Nadwat-ul-Ulama, formed in the 1890s to bridge traditional and modern learning, set up its Dar-ul-Uloom at Lucknow; Aligarh was the seat of Sayyid Ahmad Khan's college. Statement 3 is wrong: the movement of Ahmad Raza Khan of Bareilly defended the popular Sufi practices -- the veneration of saints, their intercession and the observances at shrines -- against the reformists of Deoband. It should not be confused with the earlier Wahabi movement of Syed Ahmad of Rae Bareli, sometimes called 'Barelvi' after his town.",
  "केवल कथन 1 सही है। मिर्ज़ा ग़ुलाम अहमद ने 1889 में गुरदासपुर ज़िले के क़ादियान में अहमदिया आंदोलन की स्थापना की; इसने स्वयं को इस्लामी पुनर्जागरण का ध्वजवाहक बताया, पश्चिमी ढंग के विद्यालय खोले और तलवार के बजाय क़लम के जिहाद का उपदेश दिया। "
  "कथन 2 ग़लत है: पारंपरिक और आधुनिक शिक्षा को जोड़ने के लिए 1890 के दशक में बने नदवतुल उलेमा ने अपना दारुल उलूम लखनऊ में स्थापित किया; अलीगढ़ सैयद अहमद ख़ान के कॉलेज का केंद्र था। कथन 3 ग़लत है: बरेली के अहमद रज़ा ख़ान के आंदोलन ने लोकप्रिय सूफ़ी प्रथाओं -- संतों की पूजा, उनकी मध्यस्थता और दरगाहों पर होने वाले अनुष्ठानों -- का देवबंद के सुधारवादियों के विरुद्ध बचाव किया। इसे रायबरेली के सैयद अहमद के पहले वाले वहाबी आंदोलन से नहीं मिलाना चाहिए, जिन्हें उनके नगर के कारण कभी-कभी ‘बरेलवी’ कहा जाता है।",
  MOD + ".", "l3-t5-his-ahmadiyya-nadwa-barelvi", craft="precision")

S("Modern", "medium", "With reference to measures taken during the viceroyalty of Lord Curzon, consider the following statements:",
  "लॉर्ड कर्ज़न के वायसराय काल में उठाए गए क़दमों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Ancient Monuments Preservation Act, 1904 empowered the government to protect monuments, including those in private ownership, and to regulate excavation.",
   "The Indian Universities Act, 1904 gave the government the power to veto regulations passed by a university's Senate.",
   "The Calcutta Corporation Act, 1899 reduced the number of elected members of the Corporation, and many Indian members resigned in protest."],
  ["प्राचीन स्मारक संरक्षण अधिनियम, 1904 ने सरकार को निजी स्वामित्व वाले स्मारकों सहित स्मारकों का संरक्षण करने और उत्खनन को विनियमित करने का अधिकार दिया।",
   "भारतीय विश्वविद्यालय अधिनियम, 1904 ने सरकार को विश्वविद्यालय की सीनेट द्वारा पारित विनियमों पर वीटो का अधिकार दिया।",
   "कलकत्ता कॉर्पोरेशन अधिनियम, 1899 ने कॉर्पोरेशन के निर्वाचित सदस्यों की संख्या घटाई, और अनेक भारतीय सदस्यों ने विरोध में त्यागपत्र दे दिया।"],
  C3, 2,
  "All three are correct. Curzon revived the Archaeological Survey of India, bringing in John Marshall as its Director-General in 1902, and the 1904 Act gave the State power to protect monuments -- by agreement with owners or by acquisition -- and to control excavation and the trade in antiquities; it was the forerunner of the Ancient Monuments and Archaeological Sites and Remains Act, 1958. "
  "The Universities Act and the Calcutta Corporation Act, by contrast, were read by nationalists as attacks on Indian self-government: the first tightened official control over universities and the colleges affiliated to them, and the second shrank the elected element in the city's corporation. Coming before the partition of Bengal, they sharpened the opposition that the partition of 1905 brought to a head.",
  "तीनों कथन सही हैं। कर्ज़न ने भारतीय पुरातत्व सर्वेक्षण को पुनर्जीवित किया और 1902 में जॉन मार्शल को उसका महानिदेशक बनाया, और 1904 के अधिनियम ने राज्य को स्मारकों का संरक्षण करने -- स्वामियों से समझौते या अधिग्रहण द्वारा -- तथा उत्खनन और पुरावस्तुओं के व्यापार को नियंत्रित करने का अधिकार दिया; यह प्राचीन संस्मारक तथा पुरातत्वीय स्थल और अवशेष अधिनियम, 1958 का पूर्ववर्ती था। "
  "इसके विपरीत, विश्वविद्यालय अधिनियम और कलकत्ता कॉर्पोरेशन अधिनियम को राष्ट्रवादियों ने भारतीय स्वशासन पर प्रहार माना: पहले ने विश्वविद्यालयों और उनसे संबद्ध कॉलेजों पर सरकारी नियंत्रण कड़ा किया, और दूसरे ने शहर के कॉर्पोरेशन में निर्वाचित तत्व को घटाया। बंगाल विभाजन से पहले आए इन क़दमों ने उस विरोध को तीखा किया जो 1905 के विभाजन से चरम पर पहुँचा।",
  MOD + "; " + ASI + ", history of the Survey.", "l3-t5-his-curzon-monuments-universities-corporation", craft="linkage")

# ================================================================ ANCIENT (6)
M("Ancient", "easy",
  "Which one of the following mahajanapadas lay south of the Vindhyas, on the banks of the Godavari?",
  "निम्नलिखित में से कौन-सा महाजनपद विंध्य के दक्षिण में, गोदावरी के तट पर स्थित था?",
  ["Avanti", "Chedi", "Vatsa", "Assaka"],
  ["अवंति", "चेदि", "वत्स", "अस्सक"],
  3,
  "Assaka (Ashmaka), with its capital at Potana or Potali, was the only one of the sixteen mahajanapadas listed in the Buddhist text Anguttara Nikaya that lay in the Deccan, on the Godavari; all the others were in the north, from Gandhara in the north-west to Anga in the east. "
  "Avanti lay in Malwa, with its capital at Ujjayini; Chedi lay in Bundelkhand, between the Yamuna and the Narmada; and Vatsa had its capital at Kaushambi on the Yamuna. Assaka's position shows how far north the early states were concentrated, with the Deccan joining the network of kingdoms and trade routes later.",
  "पोतन या पोतलि राजधानी वाला अस्सक (अश्मक) बौद्ध ग्रंथ अंगुत्तर निकाय में सूचीबद्ध सोलह महाजनपदों में एकमात्र था जो दक्कन में, गोदावरी पर स्थित था; बाक़ी सभी उत्तर में थे, उत्तर-पश्चिम के गांधार से पूर्व के अंग तक। "
  "अवंति मालवा में था, जिसकी राजधानी उज्जयिनी थी; चेदि बुंदेलखंड में, यमुना और नर्मदा के बीच था; और वत्स की राजधानी यमुना पर कौशांबी थी। अस्सक की स्थिति दिखाती है कि आरंभिक राज्य कितने उत्तर में केंद्रित थे, और दक्कन बाद में राज्यों और व्यापार मार्गों के जाल से जुड़ा।",
  OP1 + "; " + TH1 + ".", "l3-t5-his-assaka-godavari", pos=3, craft="recall")

S("Ancient", "easy", "With reference to the administration of the Gupta empire, consider the following statements:",
  "गुप्त साम्राज्य के प्रशासन के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Provinces were called bhuktis and were placed under governors called uparikas.",
   "Officials served only at the king's pleasure, and no office could pass from father to son."],
  ["प्रांतों को भुक्ति कहा जाता था और उन्हें उपरिक नामक शासकों के अधीन रखा जाता था।",
   "अधिकारी केवल राजा की इच्छा पर्यंत सेवा करते थे, और कोई पद पिता से पुत्र को नहीं मिल सकता था।"],
  T2, 0,
  "Only statement 1 is correct. The empire was divided into bhuktis under uparikas, the bhuktis into vishayas (districts) under vishayapatis, and these into smaller units down to the village. "
  "Statement 2 is wrong: Gupta inscriptions show offices becoming hereditary and being combined. Harishena, who composed the Allahabad Prashasti of Samudragupta, calls himself a kumaramatya, a sandhivigrahika (minister of peace and war) and a mahadandanayaka (chief judicial or military officer), and his father Dhruvabhuti had also been a mahadandanayaka. Such hereditary, multiple office-holding gave powerful families a stake in the State but also weakened central control over time.",
  "केवल कथन 1 सही है। साम्राज्य उपरिकों के अधीन भुक्तियों में, भुक्तियाँ विषयपतियों के अधीन विषयों (ज़िलों) में, और ये गाँव तक छोटी इकाइयों में बँटे थे। "
  "कथन 2 ग़लत है: गुप्त अभिलेख दिखाते हैं कि पद वंशानुगत होते जा रहे थे और एक साथ कई पद रखे जाते थे। समुद्रगुप्त की प्रयाग प्रशस्ति के रचयिता हरिषेण स्वयं को कुमारामात्य, सांधिविग्रहिक (युद्ध और शांति का मंत्री) और महादंडनायक (मुख्य न्यायिक या सैन्य अधिकारी) बताते हैं, और उनके पिता ध्रुवभूति भी महादंडनायक थे। ऐसे वंशानुगत और अनेक पदों के धारण ने शक्तिशाली परिवारों को राज्य में भागीदार बनाया, पर समय के साथ केंद्रीय नियंत्रण को कमज़ोर भी किया।",
  TH1 + ", 'Kings, Farmers and Towns'; " + OP1 + ".", "l3-t5-his-gupta-bhukti-uparika-hereditary", craft="recall")

S("Ancient", "hard", "With reference to the royal statues of the Kushanas found at Mat, near Mathura, consider the following statements:",
  "मथुरा के पास माट में मिली कुषाणों की राजकीय प्रतिमाओं के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["They stood in a shrine, a devakula, built to house images of the kings.",
   "A headless standing statue among them carries an inscription naming Kanishka.",
   "The kings are shown in the dhoti and uttariya worn by images of Indian deities.",
   "Historians have read the placing of royal images in a shrine as a sign that the Kushanas wished to be seen as god-like."],
  ["वे एक देवालय, देवकुल, में स्थापित थीं, जिसे राजाओं की प्रतिमाएँ रखने के लिए बनाया गया था।",
   "उनमें से एक सिरविहीन खड़ी प्रतिमा पर कनिष्क का नाम लिखा अभिलेख है।",
   "राजाओं को भारतीय देवताओं की प्रतिमाओं जैसी धोती और उत्तरीय में दिखाया गया है।",
   "इतिहासकारों ने देवालय में राजकीय प्रतिमाएँ रखे जाने को इस बात का संकेत माना है कि कुषाण स्वयं को देवतुल्य दिखाना चाहते थे।"],
  C4, 2,
  "Statements 1, 2 and 4 are correct. At Mat, a few kilometres from Mathura, excavations found a devakula with colossal statues of Kushana rulers, among them a seated Vima Kadphises and a standing Kanishka whose head is lost but whose robe bears his name and titles; a similar dynastic shrine stood at Surkh Kotal in Afghanistan. Installing the king's image in a shrine, as one would a deity's, is usually read as a claim to divine status -- the same idea expressed in their titles. "
  "Statement 3 is wrong, and the dress is the clue to the dynasty's origin: the kings wear a long Central Asian tunic or coat, trousers and heavy padded boots, and Kanishka grips a mace and a sword. The Kushanas, a branch of the Yuezhi from Central Asia, kept their steppe dress even as their sculptors worked in the Mathura idiom.",
  "कथन 1, 2 और 4 सही हैं। मथुरा से कुछ किलोमीटर दूर माट में उत्खनन से एक देवकुल मिला जिसमें कुषाण शासकों की विशाल प्रतिमाएँ थीं, उनमें बैठे हुए विम कडफ़िसेस और खड़े कनिष्क की प्रतिमा, जिसका सिर नहीं है पर जिसके वस्त्र पर उसका नाम और उपाधियाँ अंकित हैं; ऐसा ही एक वंशीय देवालय अफ़ग़ानिस्तान के सुर्ख़ कोतल में था। राजा की प्रतिमा को किसी देवता की तरह देवालय में स्थापित करना सामान्यतः दैवी दर्जे का दावा माना जाता है -- वही विचार जो उनकी उपाधियों में व्यक्त होता है। "
  "कथन 3 ग़लत है, और वेशभूषा ही राजवंश के मूल का संकेत है: राजा मध्य एशियाई लंबा अंगरखा या कोट, पायजामा और भारी गद्देदार जूते पहने हैं, और कनिष्क एक गदा और तलवार थामे हैं। मध्य एशिया के युएझी की एक शाखा, कुषाणों ने अपनी स्तेपी वेशभूषा बनाए रखी, जबकि उनके मूर्तिकार मथुरा शैली में काम करते थे।",
  TH1 + ", 'Kings, Farmers and Towns'; Government Museum, Mathura.", "l3-t5-his-kushana-devakula-mat", craft="inference")

M("Ancient", "medium",
  "The Mattavilasa Prahasana, a Sanskrit farce that pokes fun at a Kapalika ascetic and a Buddhist monk, is attributed to:",
  "मत्तविलास प्रहसन, जो एक कापालिक तपस्वी और एक बौद्ध भिक्षु का उपहास करने वाला संस्कृत प्रहसन है, किसकी रचना माना जाता है?",
  ["Narasimhavarman I", "Mahendravarman I", "Harshavardhana", "Narasimhavarman II (Rajasimha)"],
  ["नरसिंहवर्मन प्रथम", "महेंद्रवर्मन प्रथम", "हर्षवर्धन", "नरसिंहवर्मन द्वितीय (राजसिंह)"],
  1,
  "The Pallava king Mahendravarman I (early seventh century) is credited with the Mattavilasa Prahasana, a one-act farce set in Kanchi in which a drunken Kapalika accuses a Buddhist monk of stealing his skull-bowl. He was also a patron of the arts with titles such as Vichitrachitta ('curious-minded'), and his Mandagapattu inscription boasts of a shrine made without brick, timber, metal or mortar -- the start of rock-cut temples in the Tamil country. "
  "Harsha wrote three Sanskrit plays -- Ratnavali, Priyadarshika and Nagananda -- but no farce of this kind; Narasimhavarman I (Mamalla) is linked with the monolithic rathas of Mamallapuram, and Narasimhavarman II (Rajasimha) with the Kailasanatha temple at Kanchi.",
  "पल्लव राजा महेंद्रवर्मन प्रथम (सातवीं शताब्दी का आरंभ) को मत्तविलास प्रहसन का रचयिता माना जाता है, जो कांची में स्थित एक अंकी प्रहसन है जिसमें एक मदमत्त कापालिक एक बौद्ध भिक्षु पर अपना कपाल-पात्र चुराने का आरोप लगाता है। वे कलाओं के संरक्षक भी थे और विचित्रचित्त (‘जिज्ञासु मन वाला’) जैसी उपाधियाँ रखते थे, और उनका मंडगपट्टु अभिलेख ईंट, लकड़ी, धातु या गारे के बिना बने देवालय का गर्व से उल्लेख करता है -- तमिल प्रदेश में शैलकृत मंदिरों की शुरुआत। "
  "हर्ष ने तीन संस्कृत नाटक -- रत्नावली, प्रियदर्शिका और नागानंद -- लिखे पर ऐसा कोई प्रहसन नहीं; नरसिंहवर्मन प्रथम (मामल्ल) मामल्लपुरम के एकाश्म रथों से, और नरसिंहवर्मन द्वितीय (राजसिंह) कांची के कैलासनाथ मंदिर से जुड़े हैं।",
  TH1 + "; NCERT Class XI, An Introduction to Indian Art.", "l3-t5-his-mattavilasa-mahendravarman", pos=1, craft="recall")

S("Ancient", "medium", "With reference to Vadnagar in Gujarat, consider the following statements:",
  "गुजरात के वडनगर के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Excavations there have exposed the remains of a Buddhist monastery.",
   "It has been identified with Anandapura, which Hiuen Tsang described in the seventh century.",
   "Its Kirti Toran, a pair of carved pillars joined by an arch, dates from the Mauryan period."],
  ["वहाँ हुए उत्खनन से एक बौद्ध विहार के अवशेष सामने आए हैं।",
   "इसकी पहचान आनंदपुर से की गई है, जिसका वर्णन ह्वेनसांग ने सातवीं शताब्दी में किया।",
   "इसका कीर्ति तोरण, तोरण से जुड़े नक्काशीदार स्तंभों का एक जोड़ा, मौर्य काल का है।"],
  C3, 1,
  "Statements 1 and 2 are correct. Excavations by the Archaeological Survey of India and the Gujarat government have exposed a Buddhist monastery with votive stupas and a long sequence of fortified settlement. Hiuen Tsang's account of Anandapura, a town with Buddhist monasteries in western India, is generally identified with Vadnagar, and a recent study by IIT Kharagpur, the ASI and other institutions reported continuous habitation there from about 800 BCE, through Mauryan, Indo-Greek, Shaka and later phases. "
  "Statement 3 is wrong: the twin Kirti Torans belong to the Solanki (Chaulukya) period of the twelfth century, the age of the Rani-ki-Vav and the Modhera sun temple. The town's long, unbroken occupation is what makes it a valuable site for studying how urban life adjusted to changes in climate and political power.",
  "कथन 1 और 2 सही हैं। भारतीय पुरातत्व सर्वेक्षण और गुजरात सरकार के उत्खनन से मनौती स्तूपों सहित एक बौद्ध विहार और क़िलेबंद बस्ती का लंबा क्रम सामने आया है। ह्वेनसांग द्वारा वर्णित आनंदपुर, पश्चिमी भारत का बौद्ध विहारों वाला नगर, सामान्यतः वडनगर माना जाता है, और आईआईटी खड़गपुर, एएसआई और अन्य संस्थानों के एक हालिया अध्ययन ने वहाँ लगभग 800 ईसा पूर्व से मौर्य, हिंद-यवन, शक और बाद के चरणों से होते हुए निरंतर बसावट बताई। "
  "कथन 3 ग़लत है: जुड़वाँ कीर्ति तोरण बारहवीं शताब्दी के सोलंकी (चालुक्य) काल के हैं, जो रानी की वाव और मोढेरा सूर्य मंदिर का युग था। नगर की लंबी, अटूट बसावट ही उसे यह अध्ययन करने के लिए मूल्यवान स्थल बनाती है कि नगरीय जीवन जलवायु और राजनीतिक सत्ता के परिवर्तनों के साथ कैसे ढला।",
  ASI + ", Vadnagar excavations; Ministry of Culture (PIB), Archaeological Experiential Museum, Vadnagar (2025).",
  "l3-t5-his-vadnagar-anandapura", craft="precision")

S("Ancient", "medium", "With reference to the relief at Kanganahalli that shows a king labelled 'Raya Asoko', consider the following statements:",
  "कनगनहल्ली के उस उत्कीर्ण फलक के संदर्भ में जिसमें ‘राय असोको’ अंकित एक राजा दिखाया गया है, निम्नलिखित कथनों पर विचार कीजिए:",
  ["It was carved during Ashoka's own lifetime, as a portrait made for the emperor.",
   "Kanganahalli lies on the banks of the Krishna in Andhra Pradesh."],
  ["इसे स्वयं अशोक के जीवनकाल में सम्राट के लिए बनाए गए चित्र के रूप में उकेरा गया था।",
   "कनगनहल्ली आंध्र प्रदेश में कृष्णा नदी के तट पर स्थित है।"],
  T2, 3,
  "Neither statement is correct. The panel, from the great stupa at Kanganahalli, is the only known image of Ashoka with a label naming him, showing a king with his queens; but the stupa's carved casing belongs to the Satavahana period, broadly between the first century BCE and the third century CE -- so the 'portrait' was made long after his death, by a Buddhist community that remembered him as a patron of the faith. "
  "Kanganahalli is on the Bhima river in Kalaburagi district of Karnataka, close to the site of Sannati, where Ashokan edicts have also been found. The panel is a reminder that an image or label is evidence of how a ruler was remembered, not necessarily of how he looked.",
  "कोई भी कथन सही नहीं है। कनगनहल्ली के महास्तूप का यह फलक अशोक की एकमात्र ज्ञात प्रतिमा है जिस पर उनका नाम अंकित है, जिसमें एक राजा अपनी रानियों के साथ दिखाया गया है; पर स्तूप का उत्कीर्ण आवरण सातवाहन काल का है, मोटे तौर पर पहली शताब्दी ईसा पूर्व और तीसरी शताब्दी ईसवी के बीच -- अर्थात यह ‘चित्र’ उनकी मृत्यु के बहुत बाद एक बौद्ध समुदाय ने बनाया जो उन्हें धर्म के संरक्षक के रूप में याद करता था। "
  "कनगनहल्ली कर्नाटक के कलबुर्गी ज़िले में भीमा नदी पर है, सन्नति स्थल के निकट, जहाँ अशोक के अभिलेख भी मिले हैं। यह फलक याद दिलाता है कि कोई प्रतिमा या अभिलेख इस बात का साक्ष्य है कि किसी शासक को कैसे याद किया गया, न कि आवश्यक रूप से इसका कि वह कैसा दिखता था।",
  ASI + ", Kanganahalli excavations; " + TH1 + ".", "l3-t5-his-kanganahalli-raya-asoko", craft="inference")

# ================================================================ MUSIC & DANCE (1)
P("Music & Dance", "hard", "Consider the following pairs of items of a dance repertoire and the classical dance to which they belong:",
  "नृत्य प्रस्तुति के अंशों और उनसे संबंधित शास्त्रीय नृत्य के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Alarippu : Bharatanatyam", "Tarangam : Kuchipudi", "Batu : Kathak", "Cholkettu : Kathakali"],
  ["अलारिप्पु : भरतनाट्यम", "तरंगम : कुचिपुड़ी", "बटु : कथक", "चोलकेट्टु : कथकली"],
  1,
  "Pairs 1 and 2 are correct. Alarippu ('flowering') is the invocatory opening of a Bharatanatyam recital, pure dance in which the body is gradually 'opened up'. Tarangam, from Narayana Tirtha's Krishna Leela Tarangini, is the Kuchipudi showpiece in which the dancer performs on the rim of a brass plate, sometimes balancing a pot of water on the head. "
  "Pair 3 is wrong: Batu (Batu nritya) is a pure-dance item of Odissi, built on the sculpturesque poses of the temple tradition and associated with Batukeshwar Bhairava; Kathak's signature is tatkar, its rhythmic footwork. Pair 4 is wrong: Cholkettu is the opening item of Mohiniyattam, the other classical dance of Kerala; a Kathakali performance opens with the drumming of Kelikottu and the Todayam and Purappad.",
  "युग्म 1 और 2 सही हैं। अलारिप्पु (‘खिलना’) भरतनाट्यम प्रस्तुति का आह्वान वाला आरंभिक अंश है, शुद्ध नृत्य जिसमें शरीर क्रमशः ‘खुलता’ है। नारायण तीर्थ की कृष्ण लीला तरंगिणी से लिया गया तरंगम कुचिपुड़ी का वह प्रदर्शन-अंश है जिसमें नर्तक पीतल की थाली के किनारे पर नृत्य करता है, कभी-कभी सिर पर पानी का घड़ा संतुलित करते हुए। "
  "युग्म 3 ग़लत है: बटु (बटु नृत्य) ओडिसी का शुद्ध नृत्य अंश है, जो मंदिर परंपरा की मूर्तिवत मुद्राओं पर आधारित है और बटुकेश्वर भैरव से जुड़ा है; कथक की पहचान उसका लयबद्ध पदसंचालन तत्कार है। युग्म 4 ग़लत है: चोलकेट्टु मोहिनीअट्टम का आरंभिक अंश है, जो केरल का दूसरा शास्त्रीय नृत्य है; कथकली प्रस्तुति केलिकोट्टु के ढोल-वादन और तोडयम तथा पुरप्पाड से शुरू होती है।",
  MUS + ".", "l3-t5-his-dance-items-alarippu-tarangam-batu-cholkettu", craft="precision")

# ================================================================ MEDIEVAL (3)
P("Medieval", "medium", "Consider the following pairs of Sufi saints and the orders or regions with which they are associated:",
  "सूफ़ी संतों और उनसे जुड़े सिलसिलों या क्षेत्रों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Sharafuddin Yahya Maneri : Firdausi order in Bihar",
   "Nuruddin (Nund Rishi) : Rishi order of Kashmir",
   "Mir Sayyid Ali Hamadani : Kubrawi order in Kashmir",
   "Hamiduddin Nagauri : Chishti order in Rajasthan"],
  ["शरफ़ुद्दीन यह्या मनेरी : बिहार में फ़िरदौसी सिलसिला",
   "नूरुद्दीन (नुंद ऋषि) : कश्मीर का ऋषि सिलसिला",
   "मीर सैयद अली हमदानी : कश्मीर में कुब्रवी सिलसिला",
   "हमीदुद्दीन नागौरी : राजस्थान में चिश्ती सिलसिला"],
  3,
  "All four pairs are correct. Sharafuddin Yahya Maneri (fourteenth century) made the Firdausi order the leading Sufi tradition of Bihar, and his letters, the Maktubat, are among the classics of Sufi guidance. Nuruddin, revered as Nund Rishi or Sheikh Noor-ud-din Wali, founded the Rishi order, which drew on local ascetic traditions and on Lal Ded; his shrine is at Charar-i-Sharif. "
  "Mir Sayyid Ali Hamadani, 'Shah-i-Hamadan', brought the Kubrawi order from Iran to Kashmir and is remembered at the Khanqah-i-Mualla in Srinagar, along with the craftsmen said to have come with his followers. Hamiduddin Nagauri, a disciple of Muinuddin Chishti, lived as a simple cultivator at Nagaur and became known for his austerity. Together they show how Sufi orders took regional roots far from Delhi.",
  "चारों युग्म सही हैं। शरफ़ुद्दीन यह्या मनेरी (चौदहवीं शताब्दी) ने फ़िरदौसी सिलसिले को बिहार की प्रमुख सूफ़ी परंपरा बनाया, और उनके पत्र, मक्तूबात, सूफ़ी मार्गदर्शन की श्रेष्ठ रचनाओं में हैं। नुंद ऋषि या शेख़ नूरुद्दीन वली के रूप में पूजित नूरुद्दीन ने ऋषि सिलसिले की स्थापना की, जिसने स्थानीय तपस्वी परंपराओं और ललद्यद से प्रेरणा ली; उनकी दरगाह चरार-ए-शरीफ़ में है। "
  "‘शाह-ए-हमदान’ मीर सैयद अली हमदानी ईरान से कुब्रवी सिलसिला कश्मीर लाए और श्रीनगर की ख़ानक़ाह-ए-मुअल्ला में याद किए जाते हैं, साथ ही उन शिल्पियों के लिए भी जिनके बारे में कहा जाता है कि वे उनके अनुयायियों के साथ आए। मुईनुद्दीन चिश्ती के शिष्य हमीदुद्दीन नागौरी नागौर में एक साधारण किसान की तरह रहे और अपनी तपस्या के लिए प्रसिद्ध हुए। मिलकर ये दिखाते हैं कि सूफ़ी सिलसिलों ने दिल्ली से दूर क्षेत्रीय जड़ें कैसे जमाईं।",
  TH2 + ", 'Bhakti-Sufi Traditions'; " + OP2 + ".", "l3-t5-his-sufi-maneri-nund-rishi-hamadani-nagauri", craft="precision")

M("Medieval", "medium",
  "The rulers of Vijayanagara sometimes called themselves 'Hindu Suratrana'. The title is best understood as showing that they:",
  "विजयनगर के शासक कभी-कभी स्वयं को ‘हिंदू सुरत्राण’ कहते थे। इस उपाधि को सबसे सही रूप में किस बात का सूचक माना जाता है?",
  ["borrowed the idiom of kingship used by the neighbouring sultanates",
   "had acknowledged the overlordship of the Bahmani sultans for a time",
   "claimed descent from the Yadava rulers of Devagiri and their line",
   "ruled the Tungabhadra region as governors on behalf of the Tughlaqs"],
  ["पड़ोसी सल्तनतों की राजत्व की शब्दावली अपनाई थी",
   "कुछ समय के लिए बहमनी सुल्तानों का आधिपत्य स्वीकार किया था",
   "देवगिरि के यादव शासकों और उनकी वंश-परंपरा से उत्पत्ति का दावा किया",
   "तुगलकों की ओर से राज्यपाल के रूप में तुंगभद्रा क्षेत्र पर शासन किया"],
  0,
  "Suratrana is a Sanskritised form of the Arabic-Persian 'sultan', so 'Hindu Suratrana' meant a Hindu sultan. The Vijayanagara kings, who fought and traded with the Bahmani kingdom and its successors, borrowed concepts of kingship and courtly style from them, and their builders used arches, domes and vaults of sultanate origin -- visible in the Lotus Mahal and the elephant stables at Hampi. Deva Raya II recruited Muslim archers and horsemen into his army. "
  "The title therefore warns against reading the conflict between Vijayanagara and the sultanates as a purely religious one: the wars were driven above all by control of the fertile Raichur doab and the trade of the west coast. None of the other options follows from the title itself.",
  "सुरत्राण अरबी-फ़ारसी ‘सुल्तान’ का संस्कृतीकृत रूप है, इसलिए ‘हिंदू सुरत्राण’ का अर्थ था हिंदू सुल्तान। विजयनगर के राजा, जो बहमनी राज्य और उसके उत्तराधिकारियों से लड़ते और व्यापार करते थे, उनसे राजत्व की अवधारणाएँ और दरबारी शैली उधार लेते थे, और उनके निर्माताओं ने सल्तनत मूल के मेहराब, गुंबद और छतें प्रयोग कीं -- जो हम्पी के कमल महल और हाथीशाला में दिखती हैं। देवराय द्वितीय ने अपनी सेना में मुस्लिम धनुर्धर और घुड़सवार भर्ती किए। "
  "इसलिए यह उपाधि विजयनगर और सल्तनतों के संघर्ष को केवल धार्मिक मानने से सावधान करती है: युद्ध मुख्यतः उपजाऊ रायचूर दोआब और पश्चिमी तट के व्यापार पर नियंत्रण के लिए होते थे। अन्य कोई विकल्प स्वयं उपाधि से नहीं निकलता।",
  TH2 + ", 'An Imperial Capital: Vijayanagara'.", "l3-t5-his-hindu-suratrana-vijayanagara", pos=0, craft="inference")

S("Medieval", "medium", "With reference to village society in Mughal India, consider the following statements:",
  "मुग़लकालीन भारत के ग्रामीण समाज के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Village artisans were often paid with a share of the harvest or a plot of land rather than in cash.",
   "In eighteenth-century Bengal, zamindars paid blacksmiths, carpenters and even goldsmiths a small daily allowance and diet money, an arrangement later described as the jajmani system.",
   "In parts of western India, menstruating women were not allowed to touch the plough or the potter's wheel.",
   "Spinning yarn, sifting and kneading clay for pottery, and embroidery were done almost entirely by men."],
  ["गाँव के कारीगरों को प्रायः नक़द के बजाय फ़सल का हिस्सा या ज़मीन का एक टुकड़ा देकर भुगतान किया जाता था।",
   "अठारहवीं शताब्दी के बंगाल में ज़मींदार लोहारों, बढ़इयों और सुनारों तक को छोटा दैनिक भत्ता और भोजन के लिए पैसा देते थे, जिसे बाद में जजमानी व्यवस्था कहा गया।",
   "पश्चिमी भारत के कुछ भागों में रजस्वला महिलाओं को हल या कुम्हार के चाक को छूने की अनुमति नहीं थी।",
   "सूत कातना, बर्तनों के लिए मिट्टी छानना और गूँधना, और कढ़ाई लगभग पूरी तरह पुरुष करते थे।"],
  C4, 2,
  "Statements 1, 2 and 3 are correct. Village artisans -- potters, blacksmiths, carpenters, barbers -- served the cultivators and were paid in kind, by a share of the harvest or an allotment of land, often decided by the village panchayat; the Bengal arrangement of daily allowance and diet money is the one later called the jajmani system. Women worked alongside men in the fields, sowing, weeding, threshing and winnowing, but biases tied to their biological functions kept them from touching the plough or the potter's wheel in parts of western India. "
  "Statement 4 is wrong: these very tasks -- spinning, sifting and kneading clay, embroidery -- depended largely on women's labour, and the more commercial the production, the greater the demand for it. This is also why, among many peasant and artisan groups, marriage involved a bride-price paid to the bride's family rather than a dowry.",
  "कथन 1, 2 और 3 सही हैं। गाँव के कारीगर -- कुम्हार, लोहार, बढ़ई, नाई -- किसानों की सेवा करते थे और उन्हें वस्तु के रूप में, फ़सल के हिस्से या ज़मीन के आवंटन से भुगतान मिलता था, जो प्रायः ग्राम पंचायत तय करती थी; दैनिक भत्ते और भोजन-राशि की बंगाल वाली व्यवस्था को ही बाद में जजमानी व्यवस्था कहा गया। महिलाएँ खेतों में पुरुषों के साथ काम करती थीं -- बुवाई, निराई, गहाई और ओसाई -- पर उनके जैविक कार्यों से जुड़े पूर्वाग्रह पश्चिमी भारत के कुछ भागों में उन्हें हल या कुम्हार का चाक छूने से रोकते थे। "
  "कथन 4 ग़लत है: यही काम -- कताई, मिट्टी छानना और गूँधना, कढ़ाई -- बड़े पैमाने पर महिलाओं के श्रम पर निर्भर थे, और उत्पादन जितना व्यावसायिक होता, उसकी माँग उतनी ही बढ़ती। इसी कारण अनेक किसान और कारीगर समूहों में विवाह पर दहेज के बजाय वधू के परिवार को वधू-मूल्य दिया जाता था।",
  TH2 + ", 'Peasants, Zamindars and the State'.", "l3-t5-his-mughal-village-artisans-jajmani-women", craft="precision")

write("gs_l3_t5_b.sql")
