# -*- coding: utf-8 -*-
"""Level 2 · Test 5 (History 1: Modern India) -- 53 new bilingual rows against the live gap
report: easy statement 13, medium statement 10, hard statement 5, medium MCQ 8, easy MCQ 6,
hard MCQ 3, medium pairs 4, easy pairs 3, hard pairs 1. The 47 existing Modern rows (1857,
Doctrine of Lapse, Brahmo and Arya Samaj, INC founding, Swadeshi, revolutionaries, Gandhian
movements, constitutional acts, missions of the 1940s and others) are not repeated, and the
new rows were checked so that none states a fact another row tests (for example, no Kakori
item, since the HRA's 1925 existence would give away the HSRA-naming row)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, write
from polity_common import C3, C4, T2

d.SUBJECT = "History"
H = "Modern"
BC = "Bipan Chandra, History of Modern India (Orient BlackSwan)"
ISI = "Bipan Chandra et al., India's Struggle for Independence (Penguin)"
SB = "Sekhar Bandyopadhyay, From Plassey to Partition and After (Orient BlackSwan)"
NC8 = "NCERT Class VIII, Our Pasts III"
NC12 = "NCERT Class XII, Themes in Indian History III"

# ---------------------------------------------------------------- easy statements (13)
S(H, "easy", "Consider the following statements about Dadabhai Naoroji:",
  "दादाभाई नौरोजी के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["He was the first Indian to be elected to the British House of Commons.",
   "He was elected as a candidate of the Conservative Party."],
  ["वे ब्रिटिश हाउस ऑफ़ कॉमन्स के लिए चुने जाने वाले पहले भारतीय थे।",
   "वे कंज़र्वेटिव पार्टी के उम्मीदवार के रूप में चुने गए थे।"],
  T2, 0,
  "Only statement 1 is correct. Naoroji won Finsbury Central in London in 1892 as a Liberal, by a margin of only five votes, and used his seat to press for Indian reforms and simultaneous civil service examinations. The first Conservative of Indian origin in the Commons was Mancherjee Bhownaggree, elected in 1895.",
  "केवल कथन 1 सही है। नौरोजी 1892 में लंदन की फ़िन्सबरी सेंट्रल सीट से लिबरल उम्मीदवार के रूप में केवल पाँच मतों के अंतर से जीते, और अपनी सीट का उपयोग भारतीय सुधारों और सिविल सेवा की एक साथ परीक्षाओं की माँग के लिए किया। कॉमन्स में भारतीय मूल के पहले कंज़र्वेटिव मंचेरजी भावनगरी थे, जो 1895 में चुने गए।",
  f"{BC} -- early nationalists; {ISI} -- the Moderates.",
  "modern-naoroji-house-of-commons")

S(H, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The first railway line in India, opened in 1853, ran from Calcutta to Delhi.",
   "The first telegraph lines in India were laid during the governor-generalship of Lord Dalhousie."],
  ["1853 में खुली भारत की पहली रेल लाइन कलकत्ता से दिल्ली तक थी।",
   "भारत में पहली टेलीग्राफ़ लाइनें लॉर्ड डलहौज़ी के गवर्नर-जनरल रहते बिछाई गईं।"],
  T2, 1,
  "Only statement 2 is correct. Under Dalhousie, telegraph lines linking Calcutta, Agra, Bombay, Madras and Peshawar were laid from 1853, and they proved decisive for the British in 1857. "
  "Statement 1 is wrong: the first passenger train ran from Bombay (Bori Bunder) to Thane, about 34 km, on 16 April 1853; lines in the east, from Howrah, followed in 1854.",
  "केवल कथन 2 सही है। डलहौज़ी के समय 1853 से कलकत्ता, आगरा, बंबई, मद्रास और पेशावर को जोड़ने वाली टेलीग्राफ़ लाइनें बिछाई गईं, जो 1857 में अंग्रेज़ों के लिए निर्णायक सिद्ध हुईं। "
  "कथन 1 गलत है: पहली यात्री रेलगाड़ी 16 अप्रैल 1853 को बंबई (बोरी बंदर) से ठाणे तक, लगभग 34 किमी, चली; पूर्व में हावड़ा से लाइनें 1854 में आईं।",
  f"{BC} -- Lord Dalhousie and the economic impact of British rule; {NC8} -- From Trade to Territory.",
  "modern-first-railway-telegraph")

S(H, "easy", "Consider the following statements about social reform organisations:",
  "समाज-सुधार संगठनों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Satyashodhak Samaj was founded by Jyotiba Phule.",
   "The Prarthana Samaj was founded by Keshab Chandra Sen.",
   "The Ramakrishna Mission was founded by Ramakrishna Paramahamsa."],
  ["सत्यशोधक समाज की स्थापना ज्योतिबा फुले ने की थी।",
   "प्रार्थना समाज की स्थापना केशव चंद्र सेन ने की थी।",
   "रामकृष्ण मिशन की स्थापना रामकृष्ण परमहंस ने की थी।"],
  C3, 0,
  "Only statement 1 is correct: Phule founded the Satyashodhak Samaj in 1873 in Pune to fight caste and Brahminical dominance. "
  "Statement 2 is the trap: the Prarthana Samaj (Bombay, 1867) was founded by Atmaram Pandurang, inspired by a visit of Keshab Chandra Sen; M.G. Ranade and R.G. Bhandarkar later led it. "
  "Statement 3 is wrong: the Ramakrishna Mission was founded in 1897 by Swami Vivekananda, eleven years after Ramakrishna's death, to carry his teaching into social service.",
  "केवल कथन 1 सही है: फुले ने जाति और ब्राह्मणवादी प्रभुत्व से लड़ने के लिए 1873 में पुणे में सत्यशोधक समाज की स्थापना की। "
  "कथन 2 जाल है: प्रार्थना समाज (बंबई, 1867) की स्थापना आत्माराम पांडुरंग ने की थी, जो केशव चंद्र सेन की एक यात्रा से प्रेरित थे; बाद में एम.जी. रानडे और आर.जी. भंडारकर ने इसका नेतृत्व किया। "
  "कथन 3 गलत है: रामकृष्ण मिशन की स्थापना 1897 में, रामकृष्ण की मृत्यु के ग्यारह वर्ष बाद, स्वामी विवेकानंद ने उनकी शिक्षाओं को समाज-सेवा में उतारने के लिए की।",
  f"{BC} -- religious and social reform movements; {SB}, chapter 4.",
  "modern-reform-bodies-founders")

S(H, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Hindu Widows' Remarriage Act, 1856 was passed largely because of the campaign of Ishwar Chandra Vidyasagar.",
   "The Child Marriage Restraint Act of 1929, known as the Sarda Act, fixed the minimum age of marriage for girls at 14."],
  ["हिंदू विधवा पुनर्विवाह अधिनियम, 1856 मुख्यतः ईश्वरचंद्र विद्यासागर के अभियान के कारण पारित हुआ।",
   "शारदा अधिनियम के नाम से जाने जाने वाले बाल विवाह निरोधक अधिनियम, 1929 ने लड़कियों के विवाह की न्यूनतम आयु 14 वर्ष तय की।"],
  T2, 2,
  "Both statements are correct. Vidyasagar collected petitions and argued from the shastras that widow remarriage was permitted; he also arranged such marriages himself, at great personal cost. The Sarda Act, moved by Harbilas Sarda, set the minimum marriage age at 14 for girls and 18 for boys -- the first all-India law of its kind, though it was poorly enforced.",
  "दोनों कथन सही हैं। विद्यासागर ने याचिकाएँ इकट्ठी कीं और शास्त्रों से तर्क दिया कि विधवा पुनर्विवाह की अनुमति है; उन्होंने बड़ी व्यक्तिगत कीमत पर ऐसे विवाह स्वयं भी करवाए। हरबिलास शारदा द्वारा प्रस्तुत शारदा अधिनियम ने विवाह की न्यूनतम आयु लड़कियों के लिए 14 और लड़कों के लिए 18 वर्ष तय की; यह अपने प्रकार का पहला अखिल भारतीय कानून था, हालाँकि इसका पालन कमज़ोर रहा।",
  f"{BC} -- social reform; {NC8} -- Women, Caste and Reform.",
  "modern-widow-remarriage-sarda-act")

S(H, "easy", "Consider the following statements about the Indian National Army (INA):",
  "आज़ाद हिंद फ़ौज (INA) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Rash Behari Bose handed over the leadership of the movement in South-East Asia to Subhas Chandra Bose in 1943.",
   "The Provisional Government of Free India (Azad Hind) was proclaimed in Singapore in October 1943.",
   "INA officers were tried at the Red Fort in 1945-46."],
  ["रासबिहारी बोस ने 1943 में दक्षिण-पूर्व एशिया में आंदोलन का नेतृत्व सुभाष चंद्र बोस को सौंपा।",
   "स्वतंत्र भारत की अस्थायी सरकार (आज़ाद हिंद) की घोषणा अक्टूबर 1943 में सिंगापुर में हुई।",
   "INA के अधिकारियों पर 1945-46 में लाल किले में मुकदमा चला।"],
  C3, 2,
  "All three statements are correct. Rash Behari Bose, who had built the Indian Independence League in Japan, handed over to Subhas Bose at Singapore in July 1943; the Azad Hind government was proclaimed on 21 October 1943. "
  "The Red Fort trials of Shah Nawaz Khan, P.K. Sahgal and G.S. Dhillon -- a Muslim, a Hindu and a Sikh -- set off protests across the country; Bhulabhai Desai and Nehru appeared for the defence, and the sentences were remitted.",
  "तीनों कथन सही हैं। जापान में इंडियन इंडिपेंडेंस लीग बनाने वाले रासबिहारी बोस ने जुलाई 1943 में सिंगापुर में सुभाष बोस को नेतृत्व सौंपा; आज़ाद हिंद सरकार की घोषणा 21 अक्टूबर 1943 को हुई। "
  "शाहनवाज़ ख़ान, पी.के. सहगल और जी.एस. ढिल्लों, यानी एक मुसलमान, एक हिंदू और एक सिख, पर लाल किले में चले मुकदमों ने पूरे देश में विरोध भड़का दिया; भूलाभाई देसाई और नेहरू ने बचाव पक्ष की पैरवी की, और सज़ाएँ माफ़ कर दी गईं।",
  f"{ISI} -- the post-war upsurge; {BC} -- the INA.",
  "modern-ina-azad-hind")

S(H, "easy", "Consider the following statements about tribal uprisings:",
  "जनजातीय विद्रोहों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Santhal Hul of 1855 was led by Sidhu and Kanhu.",
   "Birsa Munda led the Ulgulan ('great tumult') in the Chota Nagpur region.",
   "The Rampa rebellion led by Alluri Sitarama Raju took place in Bengal."],
  ["1855 के संथाल हूल का नेतृत्व सिद्धू और कान्हू ने किया।",
   "बिरसा मुंडा ने छोटानागपुर क्षेत्र में उलगुलान ('महान हलचल') का नेतृत्व किया।",
   "अल्लूरी सीताराम राजू के नेतृत्व वाला रंपा विद्रोह बंगाल में हुआ।"],
  C3, 1,
  "Statements 1 and 2 are correct. The Santhals rose in the Rajmahal hills against moneylenders, zamindars and the police who protected them, and a separate Santhal Parganas district followed. Birsa Munda's movement (1899-1900) sought to restore Munda control over land and drew on a new religious message; the Chota Nagpur Tenancy Act of 1908 was one outcome. "
  "Statement 3 is wrong: the Rampa rebellion (1922-24) took place in the Godavari agency of the Madras Presidency, in present-day Andhra Pradesh, against forest laws that curbed shifting cultivation and forced labour.",
  "कथन 1 और 2 सही हैं। संथालों ने राजमहल पहाड़ियों में साहूकारों, ज़मींदारों और उन्हें बचाने वाली पुलिस के विरुद्ध विद्रोह किया, जिसके बाद अलग संथाल परगना ज़िला बना। बिरसा मुंडा का आंदोलन (1899-1900) भूमि पर मुंडाओं का नियंत्रण लौटाना चाहता था और एक नए धार्मिक संदेश पर आधारित था; 1908 का छोटानागपुर काश्तकारी अधिनियम इसका एक परिणाम था। "
  "कथन 3 गलत है: रंपा विद्रोह (1922-24) मद्रास प्रेसिडेंसी की गोदावरी एजेंसी में, वर्तमान आंध्र प्रदेश में, उन वन कानूनों के विरुद्ध हुआ जो झूम खेती और बेगार पर अंकुश लगाते थे।",
  f"{BC} -- tribal movements; {NC8} -- Tribals, Dikus and the Vision of a Golden Age.",
  "modern-tribal-uprisings-santhal-munda-rampa")

S(H, "easy", "Consider the following statements about peasant movements:",
  "किसान आंदोलनों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Indigo Revolt of 1859-60 took place mainly in Bihar.",
   "The Moplah rebellion of 1921 took place in Tamil Nadu.",
   "The Bardoli Satyagraha of 1928 was led by Mahatma Gandhi."],
  ["1859-60 का नील विद्रोह मुख्यतः बिहार में हुआ।",
   "1921 का मोपला विद्रोह तमिलनाडु में हुआ।",
   "1928 के बारदोली सत्याग्रह का नेतृत्व महात्मा गांधी ने किया।"],
  C3, 3,
  "None of the statements is correct. The Indigo Revolt was in Bengal, especially Nadia and Jessore, where ryots refused to grow indigo for European planters; it was the Champaran movement of 1917 that concerned indigo in Bihar. The Moplah (Mappila) rising of 1921 was in Malabar, in present-day Kerala. "
  "The Bardoli Satyagraha in Gujarat, against a 22 per cent revenue increase, was led by Vallabhbhai Patel, and its success earned him the title 'Sardar'. Each statement moves a real event to a neighbouring place or leader.",
  "कोई भी कथन सही नहीं है। नील विद्रोह बंगाल में, विशेषकर नदिया और जेस्सोर में, हुआ, जहाँ रैयतों ने यूरोपीय बागान-मालिकों के लिए नील उगाने से इनकार कर दिया; बिहार में नील से जुड़ा आंदोलन 1917 का चंपारण था। 1921 का मोपला (मप्पिला) विद्रोह मालाबार में, वर्तमान केरल में, हुआ। "
  "22 प्रतिशत लगान-वृद्धि के विरुद्ध गुजरात के बारदोली सत्याग्रह का नेतृत्व वल्लभभाई पटेल ने किया, और इसकी सफलता से उन्हें 'सरदार' की उपाधि मिली। हर कथन किसी वास्तविक घटना को पड़ोसी स्थान या नेता से जोड़ देता है।",
  f"{BC} -- peasant movements; {ISI}.",
  "modern-peasant-movements-places")

S(H, "easy", "Consider the following statements about Gopal Krishna Gokhale:",
  "गोपाल कृष्ण गोखले के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["He founded the Servants of India Society in 1905.",
   "Mahatma Gandhi regarded him as his political guru."],
  ["उन्होंने 1905 में सर्वेंट्स ऑफ़ इंडिया सोसाइटी की स्थापना की।",
   "महात्मा गांधी उन्हें अपना राजनीतिक गुरु मानते थे।"],
  T2, 2,
  "Both statements are correct. Gokhale, a leading Moderate and president of the Congress in 1905, founded the Servants of India Society in Pune to train dedicated workers for public service. Gandhi met him in South Africa and India, took his advice to spend a year travelling across India before entering politics, and called him his political guru.",
  "दोनों कथन सही हैं। प्रमुख नरमपंथी और 1905 में कांग्रेस के अध्यक्ष गोखले ने सार्वजनिक सेवा के लिए समर्पित कार्यकर्ता तैयार करने हेतु पुणे में सर्वेंट्स ऑफ़ इंडिया सोसाइटी की स्थापना की। गांधी उनसे दक्षिण अफ़्रीका और भारत में मिले, राजनीति में आने से पहले एक वर्ष भारत-भ्रमण करने की उनकी सलाह मानी, और उन्हें अपना राजनीतिक गुरु कहा।",
  f"{ISI} -- the Moderates; M.K. Gandhi, An Autobiography.",
  "modern-gokhale-servants-of-india")

S(H, "easy", "Consider the following statements about the early press in India:",
  "भारत के आरंभिक समाचार-पत्रों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Hicky's Bengal Gazette, started in 1780, was the first newspaper published in India.",
   "The play 'Nil Darpan', which exposed the oppression of indigo cultivators, was written by Bankim Chandra Chattopadhyay.",
   "Raja Ram Mohan Roy published the Persian journal 'Mirat-ul-Akhbar'."],
  ["1780 में शुरू हुआ हिकीज़ बंगाल गज़ट भारत में प्रकाशित पहला समाचार-पत्र था।",
   "नील किसानों पर हो रहे अत्याचार को उजागर करने वाला नाटक 'नील दर्पण' बंकिम चंद्र चट्टोपाध्याय ने लिखा था।",
   "राजा राममोहन राय ने फ़ारसी पत्रिका 'मिरात-उल-अख़बार' प्रकाशित की।"],
  C3, 1,
  "Statements 1 and 3 are correct. James Augustus Hicky's weekly was shut down within two years for attacking Warren Hastings. Ram Mohan Roy's Mirat-ul-Akhbar (1822), along with the Bengali Sambad Kaumudi, was among the first Indian-owned journals, and he protested when press regulations closed it. "
  "Statement 2 is wrong: 'Nil Darpan' (1860) was written by Dinabandhu Mitra; its English translation, published by Rev. James Long, led to his conviction for libel.",
  "कथन 1 और 3 सही हैं। जेम्स ऑगस्टस हिकी का साप्ताहिक वॉरेन हेस्टिंग्स पर हमलों के कारण दो वर्ष में बंद कर दिया गया। राममोहन राय का मिरात-उल-अख़बार (1822), बांग्ला संवाद कौमुदी के साथ, भारतीयों के स्वामित्व वाली पहली पत्रिकाओं में था, और प्रेस नियमों के कारण इसके बंद होने पर उन्होंने विरोध किया। "
  "कथन 2 गलत है: 'नील दर्पण' (1860) दीनबंधु मित्र ने लिखा था; इसका अंग्रेज़ी अनुवाद छापने वाले पादरी जेम्स लॉन्ग को मानहानि का दोषी ठहराया गया।",
  f"{BC} -- the press; {ISI} -- the struggle for civil rights.",
  "modern-early-press")

S(H, "easy", "Consider the following statements about the Government of India Act, 1858:",
  "भारत सरकार अधिनियम, 1858 के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It transferred the government of India from the East India Company to the British Crown.",
   "It abolished the post of Secretary of State for India."],
  ["इसने भारत का शासन ईस्ट इंडिया कंपनी से ब्रिटिश क्राउन को हस्तांतरित किया।",
   "इसने भारत सचिव (Secretary of State for India) का पद समाप्त कर दिया।"],
  T2, 0,
  "Only statement 1 is correct. Passed after the Revolt of 1857, the Act ended Company rule. Statement 2 reverses it: the Act created the office of Secretary of State for India, a member of the British cabinet, assisted by a Council of India, in place of the Board of Control and the Court of Directors; the Governor-General also became the Viceroy, the Crown's representative.",
  "केवल कथन 1 सही है। 1857 के विद्रोह के बाद पारित इस अधिनियम ने कंपनी का शासन समाप्त किया। कथन 2 इसे उलट देता है: अधिनियम ने बोर्ड ऑफ़ कंट्रोल और कोर्ट ऑफ़ डायरेक्टर्स की जगह ब्रिटिश मंत्रिमंडल के सदस्य भारत सचिव का पद बनाया, जिसकी सहायता के लिए भारत परिषद थी; गवर्नर-जनरल क्राउन का प्रतिनिधि, यानी वायसराय, भी बन गया।",
  f"{BC} -- administrative changes after 1858; NCERT Class XI, Political Science -- Indian Constitution at Work (historical background).",
  "modern-goi-act-1858")

S(H, "easy", "Consider the following statements about education under British rule:",
  "ब्रिटिश शासन में शिक्षा के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Macaulay's Minute of 1835 argued for education in English.",
   "Wood's Despatch of 1854 has been called the 'Magna Carta of English education in India'.",
   "The universities of Calcutta, Bombay and Madras were set up in 1857."],
  ["1835 के मैकाले के विवरण-पत्र (Minute) ने अंग्रेज़ी में शिक्षा के पक्ष में तर्क दिया।",
   "1854 के वुड के डिस्पैच को 'भारत में अंग्रेज़ी शिक्षा का मैग्ना कार्टा' कहा गया है।",
   "कलकत्ता, बंबई और मद्रास विश्वविद्यालय 1857 में स्थापित हुए।"],
  C3, 2,
  "All three statements are correct. Macaulay's Minute sided with the 'Anglicists' against the 'Orientalists', and Bentinck's resolution of 1835 made English the medium of higher education. Wood's Despatch proposed a full system from vernacular primary schools to universities, grants-in-aid and departments of public instruction, and the three universities, modelled on the University of London, followed in 1857 -- the year of the Revolt.",
  "तीनों कथन सही हैं। मैकाले के विवरण-पत्र ने 'प्राच्यवादियों' के विरुद्ध 'आंग्लवादियों' का पक्ष लिया, और बेंटिक के 1835 के प्रस्ताव ने अंग्रेज़ी को उच्च शिक्षा का माध्यम बनाया। वुड के डिस्पैच ने देशी भाषा के प्राथमिक विद्यालयों से विश्वविद्यालयों तक पूरी व्यवस्था, सहायता-अनुदान और लोक-शिक्षा विभागों का प्रस्ताव रखा, और लंदन विश्वविद्यालय के नमूने पर तीनों विश्वविद्यालय 1857 में, यानी विद्रोह के वर्ष, बने।",
  f"{BC} -- development of education; {NC8} -- Civilising the 'Native', Educating the Nation.",
  "modern-education-macaulay-wood")

S(H, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Annie Besant was the first woman to preside over the Indian National Congress.",
   "Sarojini Naidu presided over the Kanpur session of the Congress in 1925.",
   "Usha Mehta ran a secret Congress Radio during the Civil Disobedience Movement."],
  ["एनी बेसेंट भारतीय राष्ट्रीय कांग्रेस की अध्यक्षता करने वाली पहली महिला थीं।",
   "सरोजिनी नायडू ने 1925 में कांग्रेस के कानपुर अधिवेशन की अध्यक्षता की।",
   "उषा मेहता ने सविनय अवज्ञा आंदोलन के दौरान एक गुप्त कांग्रेस रेडियो चलाया।"],
  C3, 1,
  "Statements 1 and 2 are correct. Annie Besant presided at Calcutta in 1917, at the height of the Home Rule agitation, and Sarojini Naidu became the first Indian woman to preside, at Kanpur in 1925. "
  "Statement 3 is wrong about the movement: Usha Mehta, a student, ran the underground Congress Radio from Bombay in 1942, during the Quit India movement, until she was arrested.",
  "कथन 1 और 2 सही हैं। एनी बेसेंट ने होम रूल आंदोलन के चरम पर 1917 में कलकत्ता में अध्यक्षता की, और सरोजिनी नायडू 1925 में कानपुर में अध्यक्षता करने वाली पहली भारतीय महिला बनीं। "
  "कथन 3 आंदोलन के बारे में गलत है: छात्रा उषा मेहता ने भारत छोड़ो आंदोलन के दौरान 1942 में बंबई से भूमिगत कांग्रेस रेडियो चलाया, जब तक वे गिरफ़्तार नहीं हो गईं।",
  f"{ISI} -- the Quit India movement; Indian National Congress -- list of presidents.",
  "modern-women-congress-leaders")

S(H, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["At the Battle of Plassey in 1757, Robert Clive defeated Siraj-ud-Daulah.",
   "The Battle of Buxar was fought against Tipu Sultan.",
   "The Treaty of Allahabad of 1765 gave the East India Company the Nizamat of Bengal, Bihar and Orissa."],
  ["1757 में प्लासी के युद्ध में रॉबर्ट क्लाइव ने सिराजुद्दौला को हराया।",
   "बक्सर का युद्ध टीपू सुल्तान के विरुद्ध लड़ा गया।",
   "1765 की इलाहाबाद की संधि ने ईस्ट इंडिया कंपनी को बंगाल, बिहार और उड़ीसा की निज़ामत दी।"],
  C3, 0,
  "Only statement 1 is correct: Plassey, won largely through Mir Jafar's defection, made the Company the kingmaker in Bengal. "
  "Statement 2 is wrong: at Buxar (1764) the Company defeated the combined forces of Mir Qasim, Shuja-ud-Daula of Awadh and the Mughal emperor Shah Alam II. "
  "Statement 3 is the finer trap: by the Treaty of Allahabad Shah Alam granted the Company the Diwani -- the right to collect revenue -- while the Nizamat, the police and judicial administration, stayed nominally with the Nawab; this split is the 'dual government' of Bengal.",
  "केवल कथन 1 सही है: मुख्यतः मीर जाफ़र के दलबदल से जीते गए प्लासी के युद्ध ने कंपनी को बंगाल में राजा बनाने वाली शक्ति बना दिया। "
  "कथन 2 गलत है: बक्सर (1764) में कंपनी ने मीर क़ासिम, अवध के शुजाउद्दौला और मुग़ल बादशाह शाह आलम द्वितीय की संयुक्त सेनाओं को हराया। "
  "कथन 3 बारीक जाल है: इलाहाबाद की संधि से शाह आलम ने कंपनी को दीवानी, यानी राजस्व वसूलने का अधिकार, दी, जबकि निज़ामत, यानी पुलिस और न्याय प्रशासन, नाममात्र के लिए नवाब के पास रही; यही बंटवारा बंगाल की 'द्वैध शासन' व्यवस्था है।",
  f"{BC} -- British conquest of India; {NC8} -- From Trade to Territory.",
  "modern-plassey-buxar-allahabad")

# ---------------------------------------------------------------- medium statements (10)
S(H, "medium", "Consider the following statements about the Subsidiary Alliance:",
  "सहायक संधि (Subsidiary Alliance) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It was devised as a system by Lord Wellesley.",
   "Hyderabad was the first State to accept it.",
   "A ruler who accepted it remained free to employ Europeans of other nationalities in his service."],
  ["इसे एक प्रणाली के रूप में लॉर्ड वेलेज़ली ने तैयार किया।",
   "हैदराबाद इसे स्वीकार करने वाला पहला राज्य था।",
   "इसे स्वीकार करने वाला शासक अपनी सेवा में दूसरी राष्ट्रीयताओं के यूरोपीयों को रखने के लिए स्वतंत्र रहता था।"],
  C3, 1,
  "Statements 1 and 2 are correct. Under Wellesley's system the Indian ruler accepted a British force stationed in his territory, paid for it in cash or by ceding territory, accepted a British Resident, and gave up the right to make war or alliances without the Company's consent; the Nizam of Hyderabad signed first, followed by Mysore, Awadh and, after 1802, the Peshwa. "
  "Statement 3 is wrong: the ruler had to expel and not employ any Europeans other than the British -- a clause aimed squarely at French influence at Indian courts.",
  "कथन 1 और 2 सही हैं। वेलेज़ली की प्रणाली में भारतीय शासक अपने राज्य में तैनात ब्रिटिश सेना स्वीकार करता, उसका खर्च नकद या भू-भाग देकर चुकाता, एक ब्रिटिश रेज़िडेंट स्वीकार करता, और कंपनी की सहमति के बिना युद्ध या गठबंधन का अधिकार छोड़ देता था; हैदराबाद के निज़ाम ने सबसे पहले हस्ताक्षर किए, फिर मैसूर, अवध और 1802 के बाद पेशवा ने। "
  "कथन 3 गलत है: शासक को अंग्रेज़ों के अलावा किसी भी यूरोपीय को निकालना और न रखना होता था; यह शर्त सीधे भारतीय दरबारों में फ़्रांसीसी प्रभाव के विरुद्ध थी।",
  f"{BC} -- British conquest of India; {SB}, chapter 2.",
  "modern-subsidiary-alliance")

S(H, "medium", "Consider the following statements about the land revenue systems of British India:",
  "ब्रिटिश भारत की भू-राजस्व व्यवस्थाओं के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Under the Permanent Settlement, the revenue demand on the zamindars was fixed in perpetuity.",
   "The Ryotwari system was first introduced in Bengal.",
   "Under the Mahalwari system, the settlement was made with individual peasants rather than with the village community."],
  ["स्थायी बंदोबस्त के तहत ज़मींदारों पर राजस्व की माँग सदा के लिए तय कर दी गई।",
   "रैयतवाड़ी व्यवस्था सबसे पहले बंगाल में लागू की गई।",
   "महालवाड़ी व्यवस्था में बंदोबस्त ग्राम समुदाय के बजाय अलग-अलग किसानों के साथ किया गया।"],
  C3, 0,
  "Only statement 1 is correct: the Permanent Settlement of 1793 fixed the zamindars' revenue in perpetuity, which gave the Company a steady income but left the peasants at the mercy of the zamindars. "
  "Statement 2 is wrong: Ryotwari, a settlement made directly with each cultivator (ryot), was worked out by Alexander Read and Thomas Munro in the Madras Presidency, and later extended to Bombay. "
  "Statement 3 reverses Mahalwari: in the North-Western Provinces and Punjab the settlement was made with the village community or 'mahal' as a whole, which was jointly responsible for the revenue.",
  "केवल कथन 1 सही है: 1793 के स्थायी बंदोबस्त ने ज़मींदारों का राजस्व सदा के लिए तय किया, जिससे कंपनी को स्थिर आय मिली, पर किसान ज़मींदारों की दया पर छूट गए। "
  "कथन 2 गलत है: रैयतवाड़ी, यानी हर कृषक (रैयत) के साथ सीधा बंदोबस्त, मद्रास प्रेसिडेंसी में अलेक्ज़ेंडर रीड और टॉमस मुनरो ने तैयार किया, और बाद में इसे बंबई तक बढ़ाया गया। "
  "कथन 3 महालवाड़ी को उलट देता है: उत्तर-पश्चिमी प्रांतों और पंजाब में बंदोबस्त पूरे ग्राम समुदाय या 'महाल' के साथ किया गया, जो राजस्व के लिए संयुक्त रूप से ज़िम्मेदार था।",
  f"{BC} -- economic policies; {NC8} -- Ruling the Countryside; {NC12} -- Colonialism and the Countryside.",
  "modern-land-revenue-systems")

S(H, "medium", "Consider the following statements about the Charter Acts:",
  "चार्टर अधिनियमों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Charter Act of 1813 ended the East India Company's monopoly of trade with India, except in tea and the trade with China.",
   "The Charter Act of 1833 made the Governor-General of Bengal the Governor-General of India.",
   "The Charter Act of 1853 introduced open competition for recruitment to the civil services."],
  ["1813 के चार्टर अधिनियम ने चाय और चीन के साथ व्यापार को छोड़कर भारत के साथ व्यापार पर ईस्ट इंडिया कंपनी का एकाधिकार समाप्त किया।",
   "1833 के चार्टर अधिनियम ने बंगाल के गवर्नर-जनरल को भारत का गवर्नर-जनरल बनाया।",
   "1853 के चार्टर अधिनियम ने सिविल सेवाओं में भर्ती के लिए खुली प्रतियोगिता शुरू की।"],
  C3, 2,
  "All three statements are correct. The 1813 Act, pressed by British manufacturers, opened India to private British traders and also set aside a lakh of rupees a year for education. The 1833 Act made Lord William Bentinck the first Governor-General of India, ended the Company's commercial functions altogether and added a law member (Macaulay) to the council. "
  "The 1853 Act threw the Indian Civil Service open to competition, though the examinations were held only in London, which kept most Indians out for decades.",
  "तीनों कथन सही हैं। ब्रिटिश निर्माताओं के दबाव में बने 1813 के अधिनियम ने भारत को निजी ब्रिटिश व्यापारियों के लिए खोल दिया, और शिक्षा के लिए हर वर्ष एक लाख रुपये भी अलग रखे। 1833 के अधिनियम ने लॉर्ड विलियम बेंटिक को भारत का पहला गवर्नर-जनरल बनाया, कंपनी के व्यापारिक काम पूरी तरह समाप्त किए और परिषद में एक विधि सदस्य (मैकाले) जोड़ा। "
  "1853 के अधिनियम ने भारतीय सिविल सेवा को प्रतियोगिता के लिए खोला, हालाँकि परीक्षाएँ केवल लंदन में होती थीं, जिससे दशकों तक अधिकांश भारतीय बाहर रहे।",
  f"{BC} -- administrative structure, 1757-1857; NCERT Class XI, Political Science -- Indian Constitution at Work.",
  "modern-charter-acts")

S(H, "medium", "Consider the following statements about social movements in South India:",
  "दक्षिण भारत के सामाजिक आंदोलनों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Sri Narayana Guru's movement led to the founding of the Sri Narayana Dharma Paripalana (SNDP) Yogam in 1903.",
   "The Vaikom Satyagraha of 1924-25 was fought for the right of lower castes to use the roads around a temple.",
   "E.V. Ramasamy 'Periyar' founded the Justice Party."],
  ["श्री नारायण गुरु के आंदोलन से 1903 में श्री नारायण धर्म परिपालन (SNDP) योगम की स्थापना हुई।",
   "1924-25 का वैकोम सत्याग्रह निम्न जातियों के लिए एक मंदिर के आसपास की सड़कों के उपयोग के अधिकार के लिए लड़ा गया।",
   "ई.वी. रामासामी 'पेरियार' ने जस्टिस पार्टी की स्थापना की।"],
  C3, 1,
  "Statements 1 and 2 are correct. Narayana Guru's call of 'one caste, one religion, one god for man' inspired the Ezhavas of Kerala, and the SNDP Yogam spread education and temple-building among them. At Vaikom in Travancore, satyagrahis led by T.K. Madhavan, K.P. Kesava Menon and others -- joined by Periyar -- won the opening of the approach roads to the temple. "
  "Statement 3 is wrong: the Justice Party (South Indian Liberal Federation) was founded in 1916 by T.M. Nair and P. Theagaraya Chetty; Periyar founded the Self-Respect Movement in 1925 and led the Justice Party only from 1938.",
  "कथन 1 और 2 सही हैं। नारायण गुरु के 'मनुष्य के लिए एक जाति, एक धर्म, एक ईश्वर' के आह्वान ने केरल के एझवाओं को प्रेरित किया, और SNDP योगम ने उनमें शिक्षा और मंदिर-निर्माण फैलाया। त्रावणकोर के वैकोम में टी.के. माधवन, के.पी. केशव मेनन और दूसरों के नेतृत्व में, और पेरियार के साथ, सत्याग्रहियों ने मंदिर तक जाने वाली सड़कें खुलवाईं। "
  "कथन 3 गलत है: जस्टिस पार्टी (साउथ इंडियन लिबरल फ़ेडरेशन) की स्थापना 1916 में टी.एम. नायर और पी. त्यागराय चेट्टी ने की; पेरियार ने 1925 में आत्म-सम्मान आंदोलन शुरू किया और 1938 से ही जस्टिस पार्टी का नेतृत्व किया।",
  f"{BC} -- social reform movements; {SB}, chapter 7.",
  "modern-south-india-social-movements")

S(H, "medium", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Sir Syed Ahmad Khan founded the Muhammadan Anglo-Oriental College at Aligarh in 1875.",
   "The Deoband school strongly supported the loyalist politics of the Aligarh movement.",
   "The Aligarh movement under Sir Syed supported the Indian National Congress from its founding."],
  ["सर सैयद अहमद ख़ान ने 1875 में अलीगढ़ में मोहम्मडन एंग्लो-ओरिएंटल कॉलेज की स्थापना की।",
   "देवबंद स्कूल ने अलीगढ़ आंदोलन की राजभक्त राजनीति का प्रबल समर्थन किया।",
   "सर सैयद के नेतृत्व में अलीगढ़ आंदोलन ने अपनी स्थापना से ही भारतीय राष्ट्रीय कांग्रेस का समर्थन किया।"],
  C3, 0,
  "Only statement 1 is correct: the college, later Aligarh Muslim University, aimed to give Muslims modern, English education while keeping their faith. "
  "Statement 2 is wrong: the Deoband seminary (1866), founded by orthodox ulema, opposed both British rule and Sir Syed's loyalism, and welcomed the Congress. "
  "Statement 3 is wrong: Sir Syed urged Muslims to stay away from the Congress, fearing that representative government would mean rule by the Hindu majority -- an early source of the politics that later took shape in the Muslim League.",
  "केवल कथन 1 सही है: यह कॉलेज, जो बाद में अलीगढ़ मुस्लिम विश्वविद्यालय बना, मुसलमानों को अपनी आस्था बनाए रखते हुए आधुनिक, अंग्रेज़ी शिक्षा देना चाहता था। "
  "कथन 2 गलत है: रूढ़िवादी उलेमा द्वारा स्थापित देवबंद मदरसे (1866) ने ब्रिटिश शासन और सर सैयद की राजभक्ति, दोनों का विरोध किया और कांग्रेस का स्वागत किया। "
  "कथन 3 गलत है: सर सैयद ने मुसलमानों से कांग्रेस से दूर रहने का आग्रह किया, इस डर से कि प्रतिनिधि सरकार का अर्थ हिंदू बहुमत का शासन होगा; यह उस राजनीति का एक शुरुआती स्रोत था जिसने बाद में मुस्लिम लीग का रूप लिया।",
  f"{BC} -- religious reform among Muslims; {SB}, chapter 6.",
  "modern-aligarh-deoband")

S(H, "medium", "Consider the following statements about the Swaraj Party:",
  "स्वराज पार्टी के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It was formed in 1923 by C.R. Das and Motilal Nehru.",
   "It wanted to enter the legislative councils and obstruct the government from within.",
   "Leaders such as C. Rajagopalachari and Vallabhbhai Patel, known as the 'No-changers', opposed council entry."],
  ["इसका गठन 1923 में सी.आर. दास और मोतीलाल नेहरू ने किया।",
   "यह विधान परिषदों में प्रवेश करके भीतर से सरकार के काम में बाधा डालना चाहती थी।",
   "'अपरिवर्तनवादी' (No-changers) कहे जाने वाले सी. राजगोपालाचारी और वल्लभभाई पटेल जैसे नेताओं ने परिषद-प्रवेश का विरोध किया।"],
  C3, 2,
  "All three statements are correct. After the Non-Cooperation Movement was withdrawn, the Congress split between the 'pro-changers', who wanted to contest the elections under the 1919 Act, and the 'No-changers', who wanted to continue the constructive programme of khadi, national education and Hindu-Muslim unity. "
  "Das and Motilal formed the Congress-Khilafat Swaraj Party within the Congress, and Gandhi allowed both lines to coexist. The Swarajists won many seats in 1923 and defeated several government measures in the Central Assembly, where Vithalbhai Patel became the first Indian President of the Assembly in 1925.",
  "तीनों कथन सही हैं। असहयोग आंदोलन वापस लेने के बाद कांग्रेस 'परिवर्तनवादियों', जो 1919 के अधिनियम के तहत चुनाव लड़ना चाहते थे, और 'अपरिवर्तनवादियों' में बँट गई, जो खादी, राष्ट्रीय शिक्षा और हिंदू-मुस्लिम एकता का रचनात्मक कार्यक्रम जारी रखना चाहते थे। "
  "दास और मोतीलाल ने कांग्रेस के भीतर ही कांग्रेस-ख़िलाफ़त स्वराज पार्टी बनाई, और गांधी ने दोनों धाराओं को साथ चलने दिया। स्वराजवादियों ने 1923 में कई सीटें जीतीं और केंद्रीय विधानसभा में सरकार के कई प्रस्ताव गिराए, जहाँ 1925 में विट्ठलभाई पटेल विधानसभा के पहले भारतीय अध्यक्ष बने।",
  f"{ISI} -- the Swarajists and the No-changers.",
  "modern-swaraj-party-1923")

S(H, "medium", "Consider the following statements about the Nehru Report of 1928:",
  "1928 की नेहरू रिपोर्ट के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It proposed Dominion Status for India.",
   "It recommended separate electorates for Muslims.",
   "Muhammad Ali Jinnah accepted it without amendment."],
  ["इसने भारत के लिए डोमिनियन स्टेटस (अधिराज्य) का प्रस्ताव रखा।",
   "इसने मुसलमानों के लिए पृथक निर्वाचक-मंडल की सिफ़ारिश की।",
   "मुहम्मद अली जिन्ना ने इसे बिना संशोधन के स्वीकार कर लिया।"],
  C3, 0,
  "Only statement 1 is correct. Drafted by a committee under Motilal Nehru as an Indian answer to the all-white Simon Commission, the report proposed Dominion Status, a list of fundamental rights and linguistic provinces. "
  "Statement 2 is wrong: it rejected separate electorates and proposed joint electorates, with seats reserved for Muslims only where they were a minority. "
  "Statement 3 is wrong: at the All Parties Convention in Calcutta, Jinnah's amendments were rejected, and in 1929 he put forward his 'Fourteen Points'; the younger Congress radicals, too, rejected Dominion Status in favour of complete independence.",
  "केवल कथन 1 सही है। पूरी तरह श्वेत साइमन कमीशन के भारतीय उत्तर के रूप में मोतीलाल नेहरू की अध्यक्षता वाली समिति द्वारा तैयार रिपोर्ट ने डोमिनियन स्टेटस, मौलिक अधिकारों की सूची और भाषाई प्रांतों का प्रस्ताव रखा। "
  "कथन 2 गलत है: इसने पृथक निर्वाचक-मंडल को अस्वीकार किया और संयुक्त निर्वाचक-मंडल का प्रस्ताव रखा, जिसमें केवल वहीं मुसलमानों के लिए सीटें आरक्षित थीं जहाँ वे अल्पसंख्यक थे। "
  "कथन 3 गलत है: कलकत्ता के सर्वदलीय सम्मेलन में जिन्ना के संशोधन अस्वीकार हुए, और 1929 में उन्होंने अपने 'चौदह सूत्र' रखे; कांग्रेस के युवा उग्रवादियों ने भी डोमिनियन स्टेटस को छोड़कर पूर्ण स्वतंत्रता का पक्ष लिया।",
  f"{ISI} -- the Simon Commission and the Nehru Report.",
  "modern-nehru-report-1928")

S(H, "medium", "Consider the following statements about the Lahore session of the Indian National Congress (1929):",
  "भारतीय राष्ट्रीय कांग्रेस के लाहौर अधिवेशन (1929) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It adopted 'Purna Swaraj' (complete independence) as the goal of the Congress.",
   "It authorised the Working Committee to launch a programme of civil disobedience.",
   "It decided that the first Independence Day would be celebrated on 15 August 1930."],
  ["इसने 'पूर्ण स्वराज' को कांग्रेस का लक्ष्य स्वीकार किया।",
   "इसने कार्यसमिति को सविनय अवज्ञा का कार्यक्रम शुरू करने का अधिकार दिया।",
   "इसने तय किया कि पहला स्वतंत्रता दिवस 15 अगस्त 1930 को मनाया जाएगा।"],
  C3, 1,
  "Statements 1 and 2 are correct. With the one-year deadline set in 1928 for Dominion Status having passed, the Lahore Congress declared complete independence the goal, boycotted the Round Table Conference and left it to the Working Committee -- in effect to Gandhi -- to choose the moment and form of civil disobedience, which began with the Salt March. "
  "Statement 3 is wrong: the first 'Independence Day' was observed on 26 January 1930, when the independence pledge was read out across the country -- the date later chosen for the Constitution to come into force.",
  "कथन 1 और 2 सही हैं। डोमिनियन स्टेटस के लिए 1928 में तय की गई एक वर्ष की समय-सीमा बीत जाने पर लाहौर कांग्रेस ने पूर्ण स्वतंत्रता को लक्ष्य घोषित किया, गोलमेज़ सम्मेलन का बहिष्कार किया और सविनय अवज्ञा का समय और रूप चुनने का काम कार्यसमिति, यानी व्यवहार में गांधी, पर छोड़ा, जो नमक यात्रा से शुरू हुई। "
  "कथन 3 गलत है: पहला 'स्वतंत्रता दिवस' 26 जनवरी 1930 को मनाया गया, जब पूरे देश में स्वतंत्रता की प्रतिज्ञा पढ़ी गई; यही तिथि बाद में संविधान लागू करने के लिए चुनी गई।",
  f"{ISI} -- Purna Swaraj and civil disobedience.",
  "modern-lahore-session-1929")

S(H, "medium", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The All India Trade Union Congress was founded in 1920, with Lala Lajpat Rai as its first president.",
   "The Congress Socialist Party, formed in 1934, was a separate party that worked outside the Congress.",
   "The Meerut Conspiracy Case of 1929 was brought against Ghadar revolutionaries returning from North America."],
  ["अखिल भारतीय ट्रेड यूनियन कांग्रेस की स्थापना 1920 में हुई, और लाला लाजपत राय इसके पहले अध्यक्ष थे।",
   "1934 में बनी कांग्रेस सोशलिस्ट पार्टी एक अलग दल थी जो कांग्रेस के बाहर काम करती थी।",
   "1929 का मेरठ षड्यंत्र मामला उत्तरी अमेरिका से लौटे ग़दर क्रांतिकारियों के विरुद्ध चलाया गया।"],
  C3, 0,
  "Only statement 1 is correct: the AITUC was founded in Bombay in 1920, and Lajpat Rai, its first president, linked labour's rights to the national movement. "
  "Statement 2 is wrong: the Congress Socialist Party, formed by Jayaprakash Narayan, Acharya Narendra Dev, Minoo Masani and others, worked within the Congress to push it to the left. "
  "Statement 3 is wrong: the Meerut case was brought against communist and trade union leaders, including some British communists, after the wave of strikes of 1928-29; the long trial gave them a public platform.",
  "केवल कथन 1 सही है: AITUC की स्थापना 1920 में बंबई में हुई, और इसके पहले अध्यक्ष लाजपत राय ने मज़दूरों के अधिकारों को राष्ट्रीय आंदोलन से जोड़ा। "
  "कथन 2 गलत है: जयप्रकाश नारायण, आचार्य नरेंद्र देव, मीनू मसानी और दूसरों द्वारा बनाई गई कांग्रेस सोशलिस्ट पार्टी कांग्रेस को वामपंथ की ओर धकेलने के लिए उसके भीतर काम करती थी। "
  "कथन 3 गलत है: मेरठ मामला 1928-29 की हड़तालों की लहर के बाद कम्युनिस्ट और ट्रेड यूनियन नेताओं, कुछ ब्रिटिश कम्युनिस्टों सहित, के विरुद्ध चलाया गया; लंबे मुकदमे ने उन्हें एक सार्वजनिक मंच दे दिया।",
  f"{ISI} -- the growth of the left; {BC} -- workers' movements.",
  "modern-aituc-csp-meerut")

S(H, "medium", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Ghadar Party was founded in London in 1913.",
   "The Komagata Maru carried Indian migrants who were refused entry into Australia.",
   "The party's journal 'Ghadar' was published only in English."],
  ["ग़दर पार्टी की स्थापना 1913 में लंदन में हुई।",
   "कोमागाटा मारू जहाज़ उन भारतीय प्रवासियों को ले जा रहा था जिन्हें ऑस्ट्रेलिया में प्रवेश नहीं दिया गया।",
   "पार्टी की पत्रिका 'ग़दर' केवल अंग्रेज़ी में प्रकाशित होती थी।"],
  C3, 3,
  "None of the statements is correct. The Ghadar Party was founded in 1913 on the Pacific coast of North America, with its headquarters (Yugantar Ashram) in San Francisco; Sohan Singh Bhakna was its president and Lala Har Dayal a leading figure. "
  "The Komagata Maru (1914) carried mostly Punjabi passengers to Vancouver, where Canada refused to let them land; on return, police fired on them at Budge Budge near Calcutta. "
  "The 'Ghadar' was published in Urdu, Punjabi (Gurmukhi) and other Indian languages, because it was meant for Indian workers and soldiers, most of whom did not read English.",
  "कोई भी कथन सही नहीं है। ग़दर पार्टी की स्थापना 1913 में उत्तरी अमेरिका के प्रशांत तट पर हुई, और इसका मुख्यालय (युगांतर आश्रम) सैन फ़्रांसिस्को में था; सोहन सिंह भकना इसके अध्यक्ष और लाला हरदयाल एक प्रमुख व्यक्ति थे। "
  "कोमागाटा मारू (1914) अधिकतर पंजाबी यात्रियों को वैंकूवर ले गया, जहाँ कनाडा ने उन्हें उतरने नहीं दिया; लौटने पर कलकत्ता के पास बजबज में पुलिस ने उन पर गोली चलाई। "
  "'ग़दर' उर्दू, पंजाबी (गुरमुखी) और दूसरी भारतीय भाषाओं में छपता था, क्योंकि यह भारतीय मज़दूरों और सैनिकों के लिए था, जिनमें से अधिकांश अंग्रेज़ी नहीं पढ़ते थे।",
  f"{ISI} -- the Ghadar movement; {BC} -- revolutionaries abroad.",
  "modern-ghadar-komagata-maru")

# ---------------------------------------------------------------- hard statements (5)
S(H, "hard", "Consider the following statements about the Regulating Act, 1773 and Pitt's India Act, 1784:",
  "रेगुलेटिंग एक्ट, 1773 और पिट्स इंडिया एक्ट, 1784 के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Regulating Act made the Governor of Bengal the Governor-General of Bengal.",
   "The Regulating Act provided for a Supreme Court at Calcutta.",
   "Pitt's India Act abolished the Board of Control.",
   "Pitt's India Act ended the 'dual control' of the Company's affairs by the Company and the British government."],
  ["रेगुलेटिंग एक्ट ने बंगाल के गवर्नर को बंगाल का गवर्नर-जनरल बनाया।",
   "रेगुलेटिंग एक्ट ने कलकत्ता में एक सर्वोच्च न्यायालय का प्रावधान किया।",
   "पिट्स इंडिया एक्ट ने बोर्ड ऑफ़ कंट्रोल को समाप्त कर दिया।",
   "पिट्स इंडिया एक्ट ने कंपनी और ब्रिटिश सरकार द्वारा कंपनी के मामलों के 'द्वैध नियंत्रण' को समाप्त किया।"],
  C4, 1,
  "Statements 1 and 2 are correct. The Regulating Act, the British Parliament's first attempt to control the Company, made Warren Hastings Governor-General of Bengal with a council of four and led to the Supreme Court at Calcutta (1774). "
  "Statements 3 and 4 reverse Pitt's India Act: it created the Board of Control, a body of the British government, to supervise the Company's civil, military and revenue affairs, while the Court of Directors kept commercial matters and patronage. That arrangement is the 'dual control' it set up, not ended; it lasted until 1858.",
  "कथन 1 और 2 सही हैं। कंपनी को नियंत्रित करने के ब्रिटिश संसद के इस पहले प्रयास ने वॉरेन हेस्टिंग्स को चार सदस्यों की परिषद के साथ बंगाल का गवर्नर-जनरल बनाया और कलकत्ता में सर्वोच्च न्यायालय (1774) बनवाया। "
  "कथन 3 और 4 पिट्स इंडिया एक्ट को उलट देते हैं: इसने कंपनी के नागरिक, सैन्य और राजस्व मामलों की देखरेख के लिए ब्रिटिश सरकार का निकाय बोर्ड ऑफ़ कंट्रोल बनाया, जबकि कोर्ट ऑफ़ डायरेक्टर्स के पास व्यापारिक मामले और नियुक्तियाँ रहीं। यही वह 'द्वैध नियंत्रण' है जिसे इसने स्थापित किया, समाप्त नहीं; यह 1858 तक चला।",
  f"{BC} -- administrative structure; NCERT Class XI, Political Science -- Indian Constitution at Work.",
  "modern-regulating-pitts-india-act")

S(H, "hard", "Consider the following statements about the Mountbatten Plan of 3 June 1947:",
  "3 जून 1947 की माउंटबेटन योजना के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It provided for the partition of India into two dominions.",
   "It provided for referendums in the North-West Frontier Province and in Sylhet district.",
   "The Radcliffe boundary awards were made public before 15 August 1947."],
  ["इसने भारत को दो डोमिनियनों में विभाजित करने का प्रावधान किया।",
   "इसने उत्तर-पश्चिमी सीमांत प्रांत और सिलहट ज़िले में जनमत-संग्रह का प्रावधान किया।",
   "रैडक्लिफ़ सीमा-निर्णय 15 अगस्त 1947 से पहले सार्वजनिक कर दिए गए।"],
  C3, 1,
  "Statements 1 and 2 are correct. The plan let the legislators of Punjab and Bengal vote on partitioning their provinces, and put the choice of the NWFP and Sylhet to referendums; both went to Pakistan, the NWFP despite the Khudai Khidmatgars' boycott of the vote. The date of transfer was advanced to 15 August 1947. "
  "Statement 3 is wrong: Cyril Radcliffe's awards were ready but kept back and published only on 17 August, two days after independence, so millions did not know on which side of the border they lived -- which worsened the violence and migration.",
  "कथन 1 और 2 सही हैं। योजना ने पंजाब और बंगाल के विधायकों को अपने प्रांतों के विभाजन पर मत देने दिया, और NWFP तथा सिलहट का निर्णय जनमत-संग्रह पर छोड़ा; दोनों पाकिस्तान में गए, NWFP ख़ुदाई ख़िदमतगारों के मतदान-बहिष्कार के बावजूद। हस्तांतरण की तिथि आगे खिसकाकर 15 अगस्त 1947 कर दी गई। "
  "कथन 3 गलत है: सिरिल रैडक्लिफ़ के निर्णय तैयार थे पर रोक लिए गए और स्वतंत्रता के दो दिन बाद, 17 अगस्त को, ही प्रकाशित हुए, जिससे लाखों लोग नहीं जानते थे कि वे सीमा के किस ओर हैं; इससे हिंसा और पलायन और बढ़े।",
  f"{ISI} -- freedom and partition; {SB}, chapter 9.",
  "modern-mountbatten-plan-radcliffe")

S(H, "hard", "Consider the following statements about the Congress ministries formed after the elections of 1937:",
  "1937 के चुनावों के बाद बने कांग्रेस मंत्रिमंडलों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The elections were held under the Government of India Act, 1935.",
   "The Congress formed ministries in all eleven provinces.",
   "The ministries left office because the Governors used their special powers to dismiss them."],
  ["चुनाव भारत सरकार अधिनियम, 1935 के तहत हुए।",
   "कांग्रेस ने सभी ग्यारह प्रांतों में मंत्रिमंडल बनाए।",
   "मंत्रिमंडलों ने इसलिए पद छोड़ा क्योंकि गवर्नरों ने अपनी विशेष शक्तियों का उपयोग करके उन्हें बर्खास्त कर दिया।"],
  C3, 0,
  "Only statement 1 is correct: the 1937 elections were held for the provincial legislatures under the provincial autonomy of the 1935 Act. "
  "Statement 2 is wrong: the Congress formed ministries in eight of the eleven provinces (at first six, later also in the NWFP and Assam); Bengal and Punjab had non-Congress governments. "
  "Statement 3 is wrong: the ministries resigned of their own accord in October-November 1939, in protest at the Viceroy declaring India a party to the Second World War without consulting Indian opinion. The experience of these 28 months, including the record of the ministries, shaped the politics of the 1940s.",
  "केवल कथन 1 सही है: 1937 के चुनाव 1935 के अधिनियम की प्रांतीय स्वायत्तता के तहत प्रांतीय विधानमंडलों के लिए हुए। "
  "कथन 2 गलत है: कांग्रेस ने ग्यारह में से आठ प्रांतों में मंत्रिमंडल बनाए (पहले छह में, बाद में NWFP और असम में भी); बंगाल और पंजाब में गैर-कांग्रेसी सरकारें थीं। "
  "कथन 3 गलत है: मंत्रिमंडलों ने अक्टूबर-नवंबर 1939 में स्वयं त्यागपत्र दिया, इस विरोध में कि वायसराय ने भारतीय मत से परामर्श किए बिना भारत को द्वितीय विश्वयुद्ध में शामिल घोषित कर दिया। इन 28 महीनों के अनुभव ने, मंत्रिमंडलों के कामकाज सहित, 1940 के दशक की राजनीति को आकार दिया।",
  f"{ISI} -- the Congress ministries, 1937-39.",
  "modern-congress-ministries-1937")

S(H, "hard", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The resolution that came to be known as the Pakistan Resolution was passed by the Muslim League at Lahore in March 1940.",
   "The word 'Pakistan' was coined by Choudhry Rahmat Ali.",
   "In his presidential address to the Muslim League at Allahabad in 1930, Muhammad Iqbal spoke of a consolidated Muslim state in north-western India."],
  ["जिस प्रस्ताव को पाकिस्तान प्रस्ताव कहा जाने लगा, वह मार्च 1940 में लाहौर में मुस्लिम लीग ने पारित किया।",
   "'पाकिस्तान' शब्द चौधरी रहमत अली ने गढ़ा।",
   "1930 में इलाहाबाद में मुस्लिम लीग के अपने अध्यक्षीय भाषण में मुहम्मद इक़बाल ने उत्तर-पश्चिमी भारत में एक संगठित मुस्लिम राज्य की बात कही।"],
  C3, 2,
  "All three statements are correct. The Lahore resolution demanded that Muslim-majority areas in the north-west and east be grouped into 'independent states', without using the word Pakistan; the press soon named it the Pakistan Resolution. "
  "Rahmat Ali, a student at Cambridge, coined the name in his 1933 pamphlet 'Now or Never'. Iqbal's Allahabad address of 1930 spoke of a Muslim state in the north-west, within or outside the British Empire -- an idea still vague at the time. A student who expects one of three famous names to be misattributed will pick 'Only two'.",
  "तीनों कथन सही हैं। लाहौर प्रस्ताव ने माँग की कि उत्तर-पश्चिम और पूर्व के मुस्लिम-बहुल क्षेत्रों को 'स्वतंत्र राज्यों' में संगठित किया जाए, पर उसमें पाकिस्तान शब्द नहीं था; प्रेस ने जल्दी ही इसे पाकिस्तान प्रस्ताव नाम दे दिया। "
  "कैम्ब्रिज के छात्र रहमत अली ने यह नाम 1933 की अपनी पुस्तिका 'नाउ ऑर नेवर' में गढ़ा। इक़बाल के 1930 के इलाहाबाद भाषण ने उत्तर-पश्चिम में ब्रिटिश साम्राज्य के भीतर या बाहर एक मुस्लिम राज्य की बात कही; तब यह विचार अस्पष्ट था। जो विद्यार्थी मानता है कि तीन प्रसिद्ध नामों में से एक गलत जोड़ा गया होगा, वह 'केवल दो' चुन लेगा।",
  f"{ISI} -- communalism; {SB}, chapter 9.",
  "modern-pakistan-resolution-idea")

S(H, "hard", "Consider the following statements about commissions and schemes on education:",
  "शिक्षा से संबंधित आयोगों और योजनाओं के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Hunter Commission of 1882 dealt mainly with university education.",
   "The Sadler Commission of 1917 was appointed to review the University of Bombay.",
   "The Wardha scheme of basic education was put forward by the Sargent Plan."],
  ["1882 का हंटर आयोग मुख्यतः विश्वविद्यालय शिक्षा से संबंधित था।",
   "1917 का सैडलर आयोग बंबई विश्वविद्यालय की समीक्षा के लिए नियुक्त किया गया।",
   "बुनियादी शिक्षा की वर्धा योजना सार्जेंट योजना ने प्रस्तुत की।"],
  C3, 3,
  "None of the statements is correct. The Hunter Commission, appointed under Ripon, looked mainly at primary and secondary education and recommended handing primary schools to the new local boards. The Sadler Commission examined the University of Calcutta, though its recommendations -- such as a separate intermediate stage and a board for secondary education -- shaped universities across India. "
  "The Wardha scheme (1937), learning through productive handicraft in the mother tongue, came from Gandhi and was worked out by a committee under Zakir Husain; the Sargent Plan (1944) was a later, official post-war plan for a national system of education.",
  "कोई भी कथन सही नहीं है। रिपन के समय नियुक्त हंटर आयोग ने मुख्यतः प्राथमिक और माध्यमिक शिक्षा को देखा और प्राथमिक विद्यालयों को नए स्थानीय बोर्डों को सौंपने की सिफ़ारिश की। सैडलर आयोग ने कलकत्ता विश्वविद्यालय की जाँच की, हालाँकि अलग इंटरमीडिएट स्तर और माध्यमिक शिक्षा बोर्ड जैसी इसकी सिफ़ारिशों ने पूरे भारत के विश्वविद्यालयों को प्रभावित किया। "
  "वर्धा योजना (1937), यानी मातृभाषा में उत्पादक हस्तशिल्प के माध्यम से शिक्षा, गांधी से आई और ज़ाकिर हुसैन की अध्यक्षता वाली समिति ने इसे विस्तार दिया; सार्जेंट योजना (1944) बाद की, युद्धोत्तर सरकारी योजना थी, जो शिक्षा की राष्ट्रीय व्यवस्था के लिए थी।",
  f"{BC} -- development of education; {NC8} -- Civilising the 'Native', Educating the Nation.",
  "modern-education-commissions")

# ---------------------------------------------------------------- medium MCQs (8)
M(H, "medium", "The Battle of Wandiwash (1760) was fought between:",
  "वांडिवाश का युद्ध (1760) किनके बीच लड़ा गया?",
  ["The English and the French", "The English and the Marathas", "The Marathas and the Afghans", "The French and the Dutch"],
  ["अंग्रेज़ों और फ़्रांसीसियों", "अंग्रेज़ों और मराठों", "मराठों और अफ़ग़ानों", "फ़्रांसीसियों और डचों"],
  0,
  "At Wandiwash in the Carnatic, Sir Eyre Coote defeated the French under Count de Lally in the Third Carnatic War; with the fall of Pondicherry in 1761, French power in India was broken. "
  "The Marathas and the Afghans fought the Third Battle of Panipat in 1761 -- the distractor that shares the period -- and the Dutch had been defeated by the English at Bedara (Chinsura) in 1759.",
  "कर्नाटक के वांडिवाश में सर आयर कूट ने तीसरे कर्नाटक युद्ध में काउंट द लाली के नेतृत्व वाले फ़्रांसीसियों को हराया; 1761 में पांडिचेरी के पतन के साथ भारत में फ़्रांसीसी शक्ति टूट गई। "
  "मराठों और अफ़ग़ानों ने 1761 में पानीपत का तीसरा युद्ध लड़ा, जो उसी दौर का गलत विकल्प है, और डचों को अंग्रेज़ों ने 1759 में बेदारा (चिनसुरा) में हराया था।",
  f"{BC} -- the Anglo-French struggle.",
  "modern-battle-of-wandiwash")

M(H, "medium", "The 'Bahishkrit Hitakarini Sabha' was founded in 1924 by:",
  "'बहिष्कृत हितकारिणी सभा' की स्थापना 1924 में किसने की?",
  ["B.R. Ambedkar", "Jyotiba Phule", "E.V. Ramasamy 'Periyar'", "Sri Narayana Guru"],
  ["बी.आर. आंबेडकर", "ज्योतिबा फुले", "ई.वी. रामासामी 'पेरियार'", "श्री नारायण गुरु"],
  0,
  "Ambedkar founded the Bahishkrit Hitakarini Sabha in Bombay to spread education and culture among the 'excluded' (bahishkrit) classes and to voice their grievances; it prepared the ground for the Mahad Satyagraha of 1927 over the use of a public water tank. "
  "Phule, who died in 1890, belongs to an earlier generation of anti-caste reform, while Periyar and Narayana Guru led movements in the south.",
  "आंबेडकर ने 'बहिष्कृत' वर्गों में शिक्षा और संस्कृति फैलाने और उनकी शिकायतें उठाने के लिए बंबई में बहिष्कृत हितकारिणी सभा की स्थापना की; इसने एक सार्वजनिक तालाब के उपयोग को लेकर 1927 के महाड सत्याग्रह की भूमि तैयार की। "
  "1890 में दिवंगत फुले जाति-विरोधी सुधार की पहले की पीढ़ी के हैं, जबकि पेरियार और नारायण गुरु ने दक्षिण में आंदोलनों का नेतृत्व किया।",
  f"{SB}, chapter 7; {BC} -- the struggle against caste.",
  "modern-bahishkrit-hitakarini-sabha")

M(H, "medium", "Who among the following threw bombs in the Central Legislative Assembly along with Bhagat Singh in April 1929?",
  "अप्रैल 1929 में भगत सिंह के साथ केंद्रीय विधानसभा में बम किसने फेंके?",
  ["Batukeshwar Dutt", "Sukhdev Thapar", "Shivaram Rajguru", "Chandrashekhar Azad"],
  ["बटुकेश्वर दत्त", "सुखदेव थापर", "शिवराम राजगुरु", "चंद्रशेखर आज़ाद"],
  0,
  "Bhagat Singh and Batukeshwar Dutt threw harmless bombs into the Assembly on 8 April 1929, as the Public Safety and Trade Disputes Bills were being pushed through, shouted 'Inquilab Zindabad' and courted arrest, to use the trial as a platform. "
  "Sukhdev and Rajguru were hanged with Bhagat Singh in 1931 for the Saunders killing in the Lahore Conspiracy Case; Chandrashekhar Azad led the organisation and died in a police encounter in Allahabad in 1931.",
  "भगत सिंह और बटुकेश्वर दत्त ने 8 अप्रैल 1929 को, जब पब्लिक सेफ़्टी और ट्रेड डिस्प्यूट्स बिल पारित कराए जा रहे थे, विधानसभा में हानिरहित बम फेंके, 'इंक़लाब ज़िंदाबाद' के नारे लगाए और मुकदमे को मंच बनाने के लिए गिरफ़्तारी दी। "
  "सुखदेव और राजगुरु को सॉन्डर्स की हत्या के लिए लाहौर षड्यंत्र मामले में 1931 में भगत सिंह के साथ फाँसी दी गई; चंद्रशेखर आज़ाद संगठन का नेतृत्व करते थे और 1931 में इलाहाबाद में पुलिस मुठभेड़ में शहीद हुए।",
  f"{ISI} -- Bhagat Singh, Surya Sen and the revolutionary terrorists.",
  "modern-assembly-bomb-1929")

M(H, "medium", "The Deccan riots of 1875 were directed mainly against:",
  "1875 के दक्कन दंगे मुख्य रूप से किनके विरुद्ध थे?",
  ["Moneylenders", "Indigo planters", "Zamindars", "British revenue officials"],
  ["साहूकारों", "नील बागान-मालिकों", "ज़मींदारों", "ब्रिटिश राजस्व अधिकारियों"],
  0,
  "In Poona and Ahmednagar districts, ryots burdened by high Ryotwari revenue and the collapse of cotton prices after the American Civil War attacked Marwari and Gujarati moneylenders, seizing and burning the bonds and account books that recorded their debts. "
  "The government responded with the Deccan Agriculturists' Relief Act of 1879. Zamindars are the trap: there were few of them in the Ryotwari Deccan, which is why the anger fell on the moneylender.",
  "पूना और अहमदनगर ज़िलों में ऊँचे रैयतवाड़ी राजस्व और अमेरिकी गृहयुद्ध के बाद कपास के दामों के गिरने से दबे रैयतों ने मारवाड़ी और गुजराती साहूकारों पर हमला किया, और उनके कर्ज़ दर्ज करने वाले बंधपत्र और बही-खाते छीनकर जला दिए। "
  "सरकार ने 1879 के दक्कन कृषक राहत अधिनियम से इसका उत्तर दिया। ज़मींदार जाल हैं: रैयतवाड़ी दक्कन में वे बहुत कम थे, इसीलिए गुस्सा साहूकार पर उतरा।",
  f"{NC12} -- Colonialism and the Countryside (the Deccan Riots Commission).",
  "modern-deccan-riots-1875")

M(H, "medium", "The Poona Sarvajanik Sabha, founded in 1870, is associated above all with:",
  "1870 में स्थापित पूना सार्वजनिक सभा मुख्य रूप से किससे जुड़ी है?",
  ["M.G. Ranade", "B.G. Tilak", "G.K. Gokhale", "Pherozeshah Mehta"],
  ["एम.जी. रानडे", "बी.जी. तिलक", "जी.के. गोखले", "फ़िरोज़शाह मेहता"],
  0,
  "Mahadev Govind Ranade, with G.V. Joshi and others, built the Poona Sarvajanik Sabha into one of the most active pre-Congress associations, which studied land revenue and famine and petitioned the government; it published a quarterly journal. "
  "Tilak and Gokhale were later associated with it -- Tilak's group took it over in 1895 -- which is why they are the tempting distractors; Pherozeshah Mehta led the Bombay Presidency Association.",
  "महादेव गोविंद रानडे ने जी.वी. जोशी और दूसरों के साथ पूना सार्वजनिक सभा को कांग्रेस से पहले के सबसे सक्रिय संगठनों में बनाया, जिसने भू-राजस्व और अकाल का अध्ययन किया और सरकार को याचिकाएँ दीं; यह एक त्रैमासिक पत्रिका भी निकालती थी। "
  "तिलक और गोखले बाद में इससे जुड़े; तिलक के समूह ने 1895 में इसे अपने हाथ में ले लिया; इसीलिए वे आकर्षक गलत विकल्प हैं; फ़िरोज़शाह मेहता ने बॉम्बे प्रेसिडेंसी एसोसिएशन का नेतृत्व किया।",
  f"{ISI} -- the foundation of the Indian National Congress (pre-Congress associations).",
  "modern-poona-sarvajanik-sabha")

M(H, "medium", "The first session of the All India Kisan Sabha, held at Lucknow in 1936, was presided over by:",
  "1936 में लखनऊ में हुए अखिल भारतीय किसान सभा के पहले अधिवेशन की अध्यक्षता किसने की?",
  ["Sahajanand Saraswati", "Acharya Narendra Dev", "N.G. Ranga", "Indulal Yagnik"],
  ["सहजानंद सरस्वती", "आचार्य नरेंद्र देव", "एन.जी. रंगा", "इंदुलाल याज्ञिक"],
  0,
  "Swami Sahajanand Saraswati, who had built the Bihar Provincial Kisan Sabha, presided, and N.G. Ranga became the general secretary; the Kisan Manifesto of 1936 demanded the abolition of zamindari and the cancellation of debts, and it influenced the Congress's Faizpur agrarian programme. "
  "Narendra Dev was a Congress Socialist leader active in the Kisan Sabha, and Indulal Yagnik a peasant leader from Gujarat -- all plausible names from the same movement.",
  "बिहार प्रांतीय किसान सभा बनाने वाले स्वामी सहजानंद सरस्वती ने अध्यक्षता की, और एन.जी. रंगा महासचिव बने; 1936 के किसान घोषणा-पत्र ने ज़मींदारी उन्मूलन और कर्ज़ माफ़ी की माँग की, और इसने कांग्रेस के फ़ैज़पुर कृषि कार्यक्रम को प्रभावित किया। "
  "नरेंद्र देव किसान सभा में सक्रिय कांग्रेस समाजवादी नेता थे, और इंदुलाल याज्ञिक गुजरात के किसान नेता; सभी उसी आंदोलन के विश्वसनीय नाम हैं।",
  f"{ISI} -- peasant movements in the 1930s.",
  "modern-all-india-kisan-sabha-1936")

M(H, "medium", "The Indian Association, founded in Calcutta in 1876, was founded by:",
  "1876 में कलकत्ता में स्थापित इंडियन एसोसिएशन की स्थापना किसने की?",
  ["Surendranath Banerjee and Anand Mohan Bose", "Womesh Chandra Bonnerjee and Dadabhai Naoroji",
   "A.O. Hume and Dinshaw Wacha", "K.T. Telang and Pherozeshah Mehta"],
  ["सुरेंद्रनाथ बनर्जी और आनंद मोहन बोस", "व्योमेश चंद्र बनर्जी और दादाभाई नौरोजी",
   "ए.ओ. ह्यूम और दिनशॉ वाचा", "के.टी. तेलंग और फ़िरोज़शाह मेहता"],
  0,
  "Surendranath Banerjee and Anand Mohan Bose founded the Indian Association to draw the educated middle class, not just landlords, into politics; it campaigned against the lowering of the maximum age for the civil service examination, and its All India National Conference (1883, 1885) was a forerunner of the Congress, into which it later merged. "
  "Telang and Mehta founded the Bombay Presidency Association (1885), and Hume and Bonnerjee were among the founders of the Congress itself.",
  "सुरेंद्रनाथ बनर्जी और आनंद मोहन बोस ने केवल ज़मींदारों को नहीं, शिक्षित मध्यवर्ग को राजनीति में लाने के लिए इंडियन एसोसिएशन की स्थापना की; इसने सिविल सेवा परीक्षा की अधिकतम आयु घटाए जाने के विरुद्ध अभियान चलाया, और इसका अखिल भारतीय राष्ट्रीय सम्मेलन (1883, 1885) कांग्रेस का अग्रदूत था, जिसमें बाद में यह विलीन हो गया। "
  "तेलंग और मेहता ने बॉम्बे प्रेसिडेंसी एसोसिएशन (1885) बनाई, और ह्यूम तथा बनर्जी स्वयं कांग्रेस के संस्थापकों में थे।",
  f"{ISI} -- the foundation of the Indian National Congress.",
  "modern-indian-association-1876")

M(H, "medium", "The Permanent Settlement of Bengal was introduced during the governor-generalship of:",
  "बंगाल का स्थायी बंदोबस्त किसके गवर्नर-जनरल रहते लागू किया गया?",
  ["Lord Cornwallis", "Warren Hastings", "Lord Wellesley", "Lord Hastings"],
  ["लॉर्ड कॉर्नवॉलिस", "वॉरेन हेस्टिंग्स", "लॉर्ड वेलेज़ली", "लॉर्ड हेस्टिंग्स"],
  0,
  "Lord Cornwallis introduced the Permanent Settlement in 1793, after the decennial (ten-year) settlement of 1789-90; he also reorganised the civil services and the courts ('Cornwallis Code'). "
  "Warren Hastings had experimented with auctioning revenue rights to the highest bidder in five-year farms, Wellesley is associated with the Subsidiary Alliance, and Lord Hastings with the defeat of the Marathas and the Pindaris.",
  "लॉर्ड कॉर्नवॉलिस ने 1789-90 के दस-वर्षीय बंदोबस्त के बाद 1793 में स्थायी बंदोबस्त लागू किया; उन्होंने सिविल सेवाओं और न्यायालयों का भी पुनर्गठन किया ('कॉर्नवॉलिस कोड')। "
  "वॉरेन हेस्टिंग्स ने राजस्व अधिकार पाँच वर्ष के ठेकों में सबसे ऊँची बोली लगाने वाले को नीलाम करने का प्रयोग किया था, वेलेज़ली सहायक संधि से जुड़े हैं, और लॉर्ड हेस्टिंग्स मराठों और पिंडारियों की पराजय से।",
  f"{BC} -- land revenue policy; {NC8} -- Ruling the Countryside.",
  "modern-cornwallis-permanent-settlement")

# ---------------------------------------------------------------- easy MCQs (6)
M(H, "easy", "The Kheda Satyagraha of 1918 was a campaign by peasants against:",
  "1918 का खेड़ा सत्याग्रह किसानों का किसके विरुद्ध अभियान था?",
  ["Collection of land revenue despite crop failure", "Forced cultivation of indigo",
   "The Rowlatt Act", "Rents charged by zamindars far above the legal rate"],
  ["फ़सल खराब होने के बावजूद भू-राजस्व की वसूली", "नील की ज़बरन खेती",
   "रॉलेट एक्ट", "ज़मींदारों द्वारा कानूनी दर से कहीं अधिक लगान वसूलना"],
  0,
  "In Kheda district of Gujarat the crops had failed, and under the revenue code the peasants were entitled to remission if the yield fell below a quarter of normal; when the government refused, Gandhi and Vallabhbhai Patel led a no-revenue campaign, and a compromise followed. "
  "Forced indigo cultivation was the issue at Champaran (1917), and Kheda was a Ryotwari area without zamindars.",
  "गुजरात के खेड़ा ज़िले में फ़सलें खराब हो गई थीं, और राजस्व संहिता के अनुसार उपज सामान्य के चौथाई से कम होने पर किसान छूट के हक़दार थे; सरकार के इनकार पर गांधी और वल्लभभाई पटेल ने लगान न देने का अभियान चलाया, और एक समझौता हुआ। "
  "नील की ज़बरन खेती चंपारण (1917) का मुद्दा थी, और खेड़ा बिना ज़मींदारों वाला रैयतवाड़ी क्षेत्र था।",
  f"{ISI} -- Gandhi's early career; M.K. Gandhi, An Autobiography.",
  "modern-kheda-satyagraha-1918")

M(H, "easy", "The salt march to Vedaranyam on the Tamil Nadu coast in 1930 was led by:",
  "1930 में तमिलनाडु तट पर वेदारण्यम तक नमक यात्रा का नेतृत्व किसने किया?",
  ["C. Rajagopalachari", "K. Kamaraj", "E.V. Ramasamy 'Periyar'", "S. Satyamurti"],
  ["सी. राजगोपालाचारी", "के. कामराज", "ई.वी. रामासामी 'पेरियार'", "एस. सत्यमूर्ति"],
  0,
  "C. Rajagopalachari led a march from Trichinopoly (Tiruchirappalli) to Vedaranyam in April 1930 to break the salt law, in step with Gandhi's Dandi March; salt marches were also led by K. Kelappan in Malabar and by others elsewhere. Kamaraj and Satyamurti were Tamil Nadu Congress leaders of the same period, and Periyar had left the Congress by then.",
  "सी. राजगोपालाचारी ने गांधी की दांडी यात्रा के साथ-साथ अप्रैल 1930 में नमक कानून तोड़ने के लिए त्रिचिनापल्ली (तिरुचिरापल्ली) से वेदारण्यम तक यात्रा का नेतृत्व किया; मालाबार में के. केलप्पन और दूसरे स्थानों पर दूसरों ने भी नमक यात्राओं का नेतृत्व किया। कामराज और सत्यमूर्ति उसी दौर के तमिलनाडु कांग्रेस के नेता थे, और पेरियार तब तक कांग्रेस छोड़ चुके थे।",
  f"{ISI} -- civil disobedience, 1930-31.",
  "modern-vedaranyam-salt-march")

M(H, "easy", "Who was the first Governor-General of independent India?",
  "स्वतंत्र भारत के पहले गवर्नर-जनरल कौन थे?",
  ["Lord Mountbatten", "C. Rajagopalachari", "Lord Wavell", "Lord Linlithgow"],
  ["लॉर्ड माउंटबेटन", "सी. राजगोपालाचारी", "लॉर्ड वेवेल", "लॉर्ड लिनलिथगो"],
  0,
  "Lord Mountbatten, the last Viceroy, stayed on at India's request as the first Governor-General of the Dominion of India until June 1948. C. Rajagopalachari succeeded him and was the first and only Indian Governor-General, until the post was abolished when the Constitution came into force in 1950 -- which is why his name tempts students. Wavell and Linlithgow were earlier Viceroys.",
  "अंतिम वायसराय लॉर्ड माउंटबेटन भारत के अनुरोध पर जून 1948 तक भारत डोमिनियन के पहले गवर्नर-जनरल रहे। उनके बाद सी. राजगोपालाचारी आए, जो 1950 में संविधान लागू होने पर पद समाप्त होने तक पहले और एकमात्र भारतीय गवर्नर-जनरल रहे; इसीलिए उनका नाम विद्यार्थियों को ललचाता है। वेवेल और लिनलिथगो पहले के वायसराय थे।",
  f"{ISI} -- freedom and partition; {SB}, chapter 9.",
  "modern-first-governor-general-independent")

M(H, "easy", "Who among the following declared 'Swaraj is my birthright and I shall have it'?",
  "'स्वराज मेरा जन्मसिद्ध अधिकार है और मैं इसे लेकर रहूँगा' की घोषणा किसने की?",
  ["Bal Gangadhar Tilak", "Bipin Chandra Pal", "Lala Lajpat Rai", "Gopal Krishna Gokhale"],
  ["बाल गंगाधर तिलक", "बिपिन चंद्र पाल", "लाला लाजपत राय", "गोपाल कृष्ण गोखले"],
  0,
  "Tilak made the declaration during the Home Rule agitation (1916-17), after his release from six years' imprisonment in Mandalay. Pal and Lajpat Rai were his fellow Extremists ('Lal-Bal-Pal'), which makes them the close distractors; Gokhale, the Moderate, favoured constitutional methods.",
  "तिलक ने छह वर्ष के मांडले कारावास से छूटने के बाद होम रूल आंदोलन (1916-17) के दौरान यह घोषणा की। पाल और लाजपत राय उनके साथी उग्रवादी ('लाल-बाल-पाल') थे, जो उन्हें निकट के गलत विकल्प बनाता है; नरमपंथी गोखले संवैधानिक तरीकों के पक्षधर थे।",
  f"{ISI} -- the Home Rule movement.",
  "modern-tilak-swaraj-birthright")

M(H, "easy", "The 'Day of Deliverance' of 22 December 1939 was observed by:",
  "22 दिसंबर 1939 का 'मुक्ति दिवस' (Day of Deliverance) किसने मनाया?",
  ["The Muslim League", "The Hindu Mahasabha", "The Justice Party", "The Unionist Party"],
  ["मुस्लिम लीग", "हिंदू महासभा", "जस्टिस पार्टी", "यूनियनिस्ट पार्टी"],
  0,
  "Jinnah called on Muslims to observe a 'Day of Deliverance' from what the League called 'Congress rule' after the Congress ministries resigned in 1939; B.R. Ambedkar also supported the call. It marked the deepening rift that led to the Lahore resolution a few months later.",
  "कांग्रेस मंत्रिमंडलों के 1939 में त्यागपत्र देने के बाद जिन्ना ने मुसलमानों से लीग के शब्दों में 'कांग्रेस शासन' से 'मुक्ति दिवस' मनाने का आह्वान किया; बी.आर. आंबेडकर ने भी इसका समर्थन किया। इसने उस बढ़ती दरार को दिखाया जो कुछ महीने बाद लाहौर प्रस्ताव तक पहुँची।",
  f"{ISI} -- communalism, 1937-40.",
  "modern-day-of-deliverance-1939")

M(H, "easy", "The Theosophical Society was founded in New York in 1875 by:",
  "थियोसॉफ़िकल सोसाइटी की स्थापना 1875 में न्यूयॉर्क में किसने की?",
  ["Madame Blavatsky and Colonel Olcott", "Annie Besant and A.O. Hume",
   "Swami Vivekananda and Sister Nivedita", "Keshab Chandra Sen and Debendranath Tagore"],
  ["मैडम ब्लावात्स्की और कर्नल ऑल्कॉट", "एनी बेसेंट और ए.ओ. ह्यूम",
   "स्वामी विवेकानंद और सिस्टर निवेदिता", "केशव चंद्र सेन और देवेंद्रनाथ टैगोर"],
  0,
  "Helena Petrovna Blavatsky and Henry Steel Olcott founded the Society, which moved its headquarters to Adyar, near Madras, in 1882 and praised ancient Hindu and Buddhist thought, boosting Indians' cultural self-confidence. Annie Besant joined later and led it in India, which is why she tempts; Hume, a founder of the Congress, was briefly a Theosophist.",
  "हेलेना पेत्रोव्ना ब्लावात्स्की और हेनरी स्टील ऑल्कॉट ने सोसाइटी की स्थापना की, जिसने 1882 में अपना मुख्यालय मद्रास के पास अड्यार में स्थानांतरित किया और प्राचीन हिंदू तथा बौद्ध चिंतन की प्रशंसा करके भारतीयों का सांस्कृतिक आत्मविश्वास बढ़ाया। एनी बेसेंट बाद में जुड़ीं और भारत में इसका नेतृत्व किया, इसीलिए उनका नाम ललचाता है; कांग्रेस के संस्थापक ह्यूम भी कुछ समय थियोसॉफ़िस्ट रहे।",
  f"{BC} -- religious and social reform movements.",
  "modern-theosophical-society-1875")

# ---------------------------------------------------------------- hard MCQs (3)
M(H, "hard", "The Kuka (Namdhari) movement in Punjab, which clashed with the British in the 1870s, was led by:",
  "पंजाब का कूका (नामधारी) आंदोलन, जिसका 1870 के दशक में अंग्रेज़ों से टकराव हुआ, किसके नेतृत्व में था?",
  ["Baba Ram Singh", "Baba Dayal Das", "Baba Kharak Singh", "Baba Sohan Singh Bhakna"],
  ["बाबा राम सिंह", "बाबा दयाल दास", "बाबा खड़क सिंह", "बाबा सोहन सिंह भकना"],
  0,
  "Baba Ram Singh turned the Namdhari sect into a movement of Sikh religious purification that also boycotted British institutions, courts and goods -- an early form of non-cooperation; after Kukas attacked Malerkotla in 1872, dozens were blown from cannon and Ram Singh was deported to Rangoon. "
  "Baba Dayal Das founded the Nirankari movement, Baba Kharak Singh led the Akali movement of the 1920s, and Sohan Singh Bhakna was the first president of the Ghadar Party.",
  "बाबा राम सिंह ने नामधारी संप्रदाय को सिख धार्मिक शुद्धि के आंदोलन में बदला, जिसने ब्रिटिश संस्थाओं, अदालतों और माल का बहिष्कार भी किया; यह असहयोग का एक शुरुआती रूप था; 1872 में कूकाओं के मलेरकोटला पर हमले के बाद दर्जनों को तोप से उड़ा दिया गया और राम सिंह को रंगून निर्वासित कर दिया गया। "
  "बाबा दयाल दास ने निरंकारी आंदोलन शुरू किया, बाबा खड़क सिंह ने 1920 के दशक के अकाली आंदोलन का नेतृत्व किया, और सोहन सिंह भकना ग़दर पार्टी के पहले अध्यक्ष थे।",
  f"{BC} -- religious reform among the Sikhs; {SB}, chapter 6.",
  "modern-kuka-movement-ram-singh")

M(H, "hard", "The Tebhaga movement of 1946-47 in Bengal demanded:",
  "बंगाल के 1946-47 के तेभागा आंदोलन ने क्या माँग की?",
  ["That sharecroppers keep two-thirds of the crop", "Abolition of the zamindari system without any compensation",
   "Reduction of the land revenue by one-third", "An end to the forced cultivation of indigo"],
  ["कि बटाईदार फ़सल का दो-तिहाई भाग रखें", "बिना किसी मुआवज़े के ज़मींदारी व्यवस्था का उन्मूलन",
   "भू-राजस्व में एक-तिहाई की कमी", "नील की ज़बरन खेती का अंत"],
  0,
  "Tebhaga means 'three shares': the bargadars (sharecroppers), who had to give half or more of the crop to the jotedars (landholders), demanded that they keep two-thirds, as the Floud Commission of 1940 had recommended. Organised by the Bengal Provincial Kisan Sabha under communist leadership, the movement spread across north and east Bengal before it was put down. "
  "The 'one-third' in two distractors plays on the same fraction.",
  "तेभागा का अर्थ है 'तीन भाग': बरगादार (बटाईदार), जिन्हें फ़सल का आधा या अधिक भाग जोतदारों (भूधारकों) को देना पड़ता था, माँग कर रहे थे कि वे दो-तिहाई भाग रखें, जैसी 1940 के फ़्लाउड आयोग ने सिफ़ारिश की थी। कम्युनिस्ट नेतृत्व में बंगाल प्रांतीय किसान सभा द्वारा संगठित यह आंदोलन दबाए जाने से पहले उत्तर और पूर्व बंगाल में फैल गया। "
  "दो गलत विकल्पों में 'एक-तिहाई' उसी भिन्न से खेलता है।",
  f"{ISI} -- peasant movements; {SB}, chapter 9.",
  "modern-tebhaga-movement")

M(H, "hard", "The Eka ('unity') movement of 1921-22, led by Madari Pasi among others, took place in:",
  "1921-22 का एका ('एकता') आंदोलन, जिसका नेतृत्व दूसरों के साथ मदारी पासी ने किया, कहाँ हुआ?",
  ["Awadh, in the United Provinces", "Malabar, in the Madras Presidency", "Kheda district of Gujarat", "Midnapore district of Bengal"],
  ["संयुक्त प्रांत का अवध", "मद्रास प्रेसिडेंसी का मालाबार", "गुजरात का खेड़ा ज़िला", "बंगाल का मिदनापुर ज़िला"],
  0,
  "In Hardoi, Bahraich and Sitapur districts of Awadh, peasants protested against rents often 50 per cent above the recorded amount, forced labour and illegal cesses, taking an oath of unity ('eka') to pay only the recorded rent; led by low-caste leaders like Madari Pasi, it moved away from the Congress's non-violence and was suppressed in 1922. "
  "It grew out of the Awadh Kisan Sabha movement of 1920, in which Baba Ramchandra and Jawaharlal Nehru were active.",
  "अवध के हरदोई, बहराइच और सीतापुर ज़िलों में किसानों ने दर्ज लगान से प्रायः 50 प्रतिशत अधिक लगान, बेगार और अवैध उपकरों का विरोध किया और केवल दर्ज लगान चुकाने की एकता ('एका') की शपथ ली; मदारी पासी जैसे निम्न-जाति नेताओं के नेतृत्व में यह कांग्रेस की अहिंसा से दूर हटा और 1922 में दबा दिया गया। "
  "यह 1920 के अवध किसान सभा आंदोलन से निकला, जिसमें बाबा रामचंद्र और जवाहरलाल नेहरू सक्रिय थे।",
  f"{ISI} -- peasant movements and nationalism in the 1920s.",
  "modern-eka-movement-awadh")

# ---------------------------------------------------------------- medium pairs (4)
P(H, "medium", "Consider the following pairs of uprisings and regions:",
  "विद्रोहों और क्षेत्रों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Paika rebellion : Odisha", "Kol uprising : Chota Nagpur", "Pagal Panthi movement : Kerala", "Ahom revolt : Assam"],
  ["पाइक विद्रोह : ओडिशा", "कोल विद्रोह : छोटानागपुर", "पागल पंथी आंदोलन : केरल", "अहोम विद्रोह : असम"],
  2,
  "Three pairs are correct. The Paika rebellion of 1817, led by Bakshi Jagabandhu, was a revolt of the traditional militia of Khurda against the loss of their rent-free lands; the Kols of Chota Nagpur rose in 1831-32 against outsiders who took their lands; and the Ahom nobles revolted in 1828 when the British stayed on in Assam after the Burmese war. "
  "Pair 3 is wrong: the Pagal Panthis, a semi-religious sect led by Karam Shah and his son Tipu, organised the peasants of the Mymensingh (Sherpur) area of Bengal against zamindars' demands in the 1820s-30s.",
  "तीन युग्म सही हैं। बख़्शी जगबंधु के नेतृत्व में 1817 का पाइक विद्रोह खुर्दा की पारंपरिक मिलिशिया का अपनी लगान-मुक्त भूमि छिनने के विरुद्ध विद्रोह था; छोटानागपुर के कोलों ने 1831-32 में अपनी भूमि छीनने वाले बाहरी लोगों के विरुद्ध विद्रोह किया; और बर्मा युद्ध के बाद अंग्रेज़ों के असम में बने रहने पर 1828 में अहोम सरदारों ने विद्रोह किया। "
  "युग्म 3 गलत है: करम शाह और उनके पुत्र टीपू के नेतृत्व वाले अर्ध-धार्मिक संप्रदाय पागल पंथियों ने 1820-30 के दशक में ज़मींदारों की माँगों के विरुद्ध बंगाल के मैमनसिंह (शेरपुर) क्षेत्र के किसानों को संगठित किया।",
  f"{BC} -- civil rebellions and tribal uprisings.",
  "modern-uprisings-regions-pairs")

P(H, "medium", "Consider the following pairs of books and their authors:",
  "पुस्तकों और उनके लेखकों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Hind Swaraj : M.K. Gandhi", "Gita Rahasya : B.G. Tilak", "Gulamgiri : B.R. Ambedkar", "The Discovery of India : Subhas Chandra Bose"],
  ["हिंद स्वराज : एम.के. गांधी", "गीता रहस्य : बी.जी. तिलक", "गुलामगिरी : बी.आर. आंबेडकर", "द डिस्कवरी ऑफ़ इंडिया : सुभाष चंद्र बोस"],
  1,
  "Only pairs 1 and 2 are correct. Gandhi wrote Hind Swaraj (1909) on the voyage from London to South Africa, criticising modern civilisation; Tilak wrote Gita Rahasya in Mandalay jail, reading the Gita as a call to action (karma yoga). "
  "Pair 3 is wrong: Gulamgiri ('Slavery', 1873) was written by Jyotiba Phule, who compared the condition of the lower castes with that of slaves in America. Pair 4 is wrong: The Discovery of India was written by Jawaharlal Nehru in Ahmednagar Fort prison (1942-46); Subhas Bose wrote 'The Indian Struggle'.",
  "केवल युग्म 1 और 2 सही हैं। गांधी ने आधुनिक सभ्यता की आलोचना करते हुए लंदन से दक्षिण अफ़्रीका की समुद्री यात्रा में हिंद स्वराज (1909) लिखी; तिलक ने मांडले जेल में गीता रहस्य लिखा, जिसमें गीता को कर्म (कर्मयोग) का आह्वान माना। "
  "युग्म 3 गलत है: गुलामगिरी (1873) ज्योतिबा फुले ने लिखी, जिन्होंने निम्न जातियों की दशा की तुलना अमेरिका के दासों से की। युग्म 4 गलत है: द डिस्कवरी ऑफ़ इंडिया जवाहरलाल नेहरू ने अहमदनगर क़िला जेल (1942-46) में लिखी; सुभाष बोस ने 'द इंडियन स्ट्रगल' लिखी।",
  f"{ISI}; {SB}.",
  "modern-books-authors-pairs")

P(H, "medium", "Consider the following pairs of associations and the years in which they were founded:",
  "संगठनों और उनकी स्थापना के वर्षों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["British Indian Association : 1851", "East India Association : 1866", "Madras Mahajan Sabha : 1884", "Bombay Presidency Association : 1905"],
  ["ब्रिटिश इंडियन एसोसिएशन : 1851", "ईस्ट इंडिया एसोसिएशन : 1866", "मद्रास महाजन सभा : 1884", "बॉम्बे प्रेसिडेंसी एसोसिएशन : 1905"],
  2,
  "Three pairs are correct. The British Indian Association (Calcutta, 1851) represented mainly the zamindars of Bengal; Dadabhai Naoroji organised the East India Association in London (1866) to inform British opinion about India; and the Madras Mahajan Sabha (1884) was founded by M. Viraraghavachariar, G. Subramania Iyer and P. Anandacharlu. "
  "Pair 4 is wrong: the Bombay Presidency Association was founded in 1885 by Pherozeshah Mehta, K.T. Telang and Badruddin Tyabji, the same year as the Congress, whose first session it helped to host.",
  "तीन युग्म सही हैं। ब्रिटिश इंडियन एसोसिएशन (कलकत्ता, 1851) मुख्यतः बंगाल के ज़मींदारों का प्रतिनिधित्व करती थी; दादाभाई नौरोजी ने ब्रिटिश जनमत को भारत के बारे में बताने के लिए लंदन में ईस्ट इंडिया एसोसिएशन (1866) बनाई; और मद्रास महाजन सभा (1884) एम. वीरराघवाचारियर, जी. सुब्रमण्य अय्यर और पी. आनंदचार्लु ने स्थापित की। "
  "युग्म 4 गलत है: बॉम्बे प्रेसिडेंसी एसोसिएशन 1885 में फ़िरोज़शाह मेहता, के.टी. तेलंग और बदरुद्दीन तैयबजी ने स्थापित की, उसी वर्ष जिस वर्ष कांग्रेस बनी, जिसके पहले अधिवेशन की मेज़बानी में इसने मदद की।",
  f"{ISI} -- the foundation of the Indian National Congress.",
  "modern-pre-congress-associations-pairs")

P(H, "medium", "Consider the following pairs of revolutionary cases or incidents and the provinces in which they took place:",
  "क्रांतिकारी मामलों या घटनाओं और जिन प्रांतों में वे हुए, उनके निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Muzaffarpur bomb attack (1908) : Bihar", "Alipore bomb case (1908) : Punjab", "Lahore conspiracy case : Punjab", "Nasik conspiracy case (1909-10) : Bengal"],
  ["मुज़फ़्फ़रपुर बम हमला (1908) : बिहार", "अलीपुर बम मामला (1908) : पंजाब", "लाहौर षड्यंत्र मामला : पंजाब", "नासिक षड्यंत्र मामला (1909-10) : बंगाल"],
  1,
  "Only pairs 1 and 3 are correct. At Muzaffarpur, Khudiram Bose and Prafulla Chaki threw a bomb at a carriage they believed carried the judge Kingsford, killing two British women; the Lahore conspiracy cases (1915, against Ghadarites, and 1929-30, against Bhagat Singh and his comrades) were tried in Punjab. "
  "Pair 2 is wrong: the Alipore bomb case, which followed Muzaffarpur, was tried at Alipore near Calcutta, in Bengal; Aurobindo Ghosh was acquitted. Pair 4 is wrong: the Nasik case arose from the killing of the collector Jackson at Nasik in the Bombay Presidency by Anant Kanhere of the Abhinav Bharat.",
  "केवल युग्म 1 और 3 सही हैं। मुज़फ़्फ़रपुर में खुदीराम बोस और प्रफुल्ल चाकी ने एक बग्घी पर बम फेंका, जिसमें उन्हें न्यायाधीश किंग्सफ़ोर्ड के होने का विश्वास था, और दो ब्रिटिश महिलाएँ मारी गईं; लाहौर षड्यंत्र मामले (1915 में ग़दर क्रांतिकारियों के विरुद्ध, और 1929-30 में भगत सिंह और उनके साथियों के विरुद्ध) पंजाब में चले। "
  "युग्म 2 गलत है: मुज़फ़्फ़रपुर के बाद हुआ अलीपुर बम मामला बंगाल में कलकत्ता के पास अलीपुर में चला; अरविंद घोष बरी हुए। युग्म 4 गलत है: नासिक मामला बंबई प्रेसिडेंसी के नासिक में अभिनव भारत के अनंत कन्हेरे द्वारा कलेक्टर जैक्सन की हत्या से निकला।",
  f"{ISI} -- the growth of revolutionary terrorism.",
  "modern-revolutionary-cases-places-pairs")

# ---------------------------------------------------------------- easy pairs (3)
P(H, "easy", "Consider the following pairs of popular titles and the leaders known by them:",
  "लोकप्रिय उपाधियों और उनसे जाने जाने वाले नेताओं के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Lokmanya : Bal Gangadhar Tilak", "Deshbandhu : Chittaranjan Das", "Punjab Kesari : Lala Lajpat Rai", "Netaji : Subhas Chandra Bose"],
  ["लोकमान्य : बाल गंगाधर तिलक", "देशबंधु : चित्तरंजन दास", "पंजाब केसरी : लाला लाजपत राय", "नेताजी : सुभाष चंद्र बोस"],
  3,
  "All four pairs are correct. These titles were given by the people, not by any government, and reflect how each leader was seen: Tilak as 'accepted by the people', C.R. Das as the 'friend of the country', Lajpat Rai as the 'lion of Punjab' -- who died after the lathi charge during the Simon Commission protest in Lahore -- and Subhas Bose as 'the leader'. "
  "A student who expects at least one mismatch in every pairs question will fall for 'Only three pairs'.",
  "चारों युग्म सही हैं। ये उपाधियाँ किसी सरकार ने नहीं, जनता ने दीं, और बताती हैं कि हर नेता को कैसे देखा गया: तिलक 'लोगों द्वारा स्वीकृत', सी.आर. दास 'देश के मित्र', लाजपत राय 'पंजाब के शेर', जिनकी लाहौर में साइमन कमीशन विरोध के दौरान लाठीचार्ज के बाद मृत्यु हुई, और सुभाष बोस 'नेता'। "
  "जो विद्यार्थी मानता है कि हर युग्म-प्रश्न में कम से कम एक बेमेल होगा ही, वह 'केवल तीन युग्म' के जाल में फँसेगा।",
  f"{ISI}.",
  "modern-leaders-titles-pairs")

P(H, "easy", "Consider the following pairs of newspapers or journals and the persons who founded them:",
  "समाचार-पत्रों या पत्रिकाओं और उनके संस्थापकों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Bombay Chronicle : Pherozeshah Mehta", "Al-Hilal : Maulana Abul Kalam Azad", "Comrade : Maulana Abul Kalam Azad", "The Hindu : Sarojini Naidu"],
  ["बॉम्बे क्रॉनिकल : फ़िरोज़शाह मेहता", "अल-हिलाल : मौलाना अबुल कलाम आज़ाद", "कॉमरेड : मौलाना अबुल कलाम आज़ाद", "द हिंदू : सरोजिनी नायडू"],
  1,
  "Only pairs 1 and 2 are correct. Pherozeshah Mehta started the Bombay Chronicle in 1910, and Azad's Urdu weekly Al-Hilal (1912) called on Muslims to join the national movement until the government banned it. "
  "Pair 3 is wrong: the English weekly Comrade (1911) was founded by Maulana Mohammad Ali (Jauhar), later a Khilafat leader -- a trap because Azad has already appeared once. Pair 4 is wrong: The Hindu was started in Madras in 1878 by G. Subramania Iyer and M. Veeraraghavachariar.",
  "केवल युग्म 1 और 2 सही हैं। फ़िरोज़शाह मेहता ने 1910 में बॉम्बे क्रॉनिकल शुरू किया, और आज़ाद के उर्दू साप्ताहिक अल-हिलाल (1912) ने सरकार द्वारा प्रतिबंधित किए जाने तक मुसलमानों से राष्ट्रीय आंदोलन में शामिल होने का आह्वान किया। "
  "युग्म 3 गलत है: अंग्रेज़ी साप्ताहिक कॉमरेड (1911) मौलाना मोहम्मद अली (जौहर) ने स्थापित किया, जो बाद में ख़िलाफ़त के नेता बने; यह जाल इसलिए है कि आज़ाद पहले ही एक बार आ चुके हैं। युग्म 4 गलत है: द हिंदू 1878 में मद्रास में जी. सुब्रमण्य अय्यर और एम. वीरराघवाचारियर ने शुरू किया।",
  f"{BC} -- the press and nationalism.",
  "modern-newspapers-founders-pairs")

P(H, "easy", "Consider the following pairs of institutions and their founders:",
  "संस्थाओं और उनके संस्थापकों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Asiatic Society of Bengal : William Jones", "Fort William College : Lord Wellesley",
   "Hindu College, Calcutta : David Hare and others", "Banaras Hindu University : Annie Besant"],
  ["एशियाटिक सोसाइटी ऑफ़ बंगाल : विलियम जोन्स", "फ़ोर्ट विलियम कॉलेज : लॉर्ड वेलेज़ली",
   "हिंदू कॉलेज, कलकत्ता : डेविड हेयर और अन्य", "बनारस हिंदू विश्वविद्यालय : एनी बेसेंट"],
  2,
  "Three pairs are correct. William Jones founded the Asiatic Society in 1784 to study Asian languages and texts; Wellesley set up Fort William College (1800) to train Company officials in Indian languages; and Hindu College (1817), later Presidency College, was started by David Hare with Radhakanta Deb and other Calcutta citizens. "
  "Pair 4 is the trap: Annie Besant founded the Central Hindu College at Banaras in 1898, which became the nucleus of the university, but Banaras Hindu University itself was founded in 1916 by Madan Mohan Malaviya.",
  "तीन युग्म सही हैं। विलियम जोन्स ने एशियाई भाषाओं और ग्रंथों के अध्ययन के लिए 1784 में एशियाटिक सोसाइटी स्थापित की; वेलेज़ली ने कंपनी के अधिकारियों को भारतीय भाषाएँ सिखाने के लिए फ़ोर्ट विलियम कॉलेज (1800) बनाया; और हिंदू कॉलेज (1817), जो बाद में प्रेसिडेंसी कॉलेज बना, डेविड हेयर ने राधाकांत देब और कलकत्ता के दूसरे नागरिकों के साथ शुरू किया। "
  "युग्म 4 जाल है: एनी बेसेंट ने 1898 में बनारस में सेंट्रल हिंदू कॉलेज की स्थापना की, जो विश्वविद्यालय का केंद्र बना, पर बनारस हिंदू विश्वविद्यालय की स्थापना स्वयं 1916 में मदन मोहन मालवीय ने की।",
  f"{BC} -- development of education; {NC8} -- Civilising the 'Native', Educating the Nation.",
  "modern-institutions-founders-pairs")

# ---------------------------------------------------------------- hard pairs (1)
P(H, "hard", "Consider the following pairs of treaties and the wars they ended:",
  "संधियों और उनसे समाप्त हुए युद्धों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Treaty of Mangalore : Second Anglo-Mysore War", "Treaty of Seringapatam : Third Anglo-Mysore War",
   "Treaty of Salbai : Third Anglo-Maratha War", "Treaty of Bassein : First Anglo-Maratha War"],
  ["मंगलौर की संधि : दूसरा आंग्ल-मैसूर युद्ध", "श्रीरंगपट्टनम की संधि : तीसरा आंग्ल-मैसूर युद्ध",
   "सालबाई की संधि : तीसरा आंग्ल-मराठा युद्ध", "बसीन की संधि : पहला आंग्ल-मराठा युद्ध"],
  1,
  "Only pairs 1 and 2 are correct. The Treaty of Mangalore (1784), signed by Tipu Sultan after Haidar Ali's death, restored conquests on both sides; the Treaty of Seringapatam (1792) forced Tipu to give up half his kingdom to the Company and its allies. "
  "Pair 3 is wrong: the Treaty of Salbai (1782) ended the First Anglo-Maratha War, with Mahadji Sindhia as mediator, and kept the peace for twenty years. Pair 4 is wrong on two counts: the Treaty of Bassein (1802) was not a peace treaty ending a war but a subsidiary alliance signed by the fugitive Peshwa Baji Rao II, and it provoked the Second Anglo-Maratha War.",
  "केवल युग्म 1 और 2 सही हैं। हैदर अली की मृत्यु के बाद टीपू सुल्तान द्वारा हस्ताक्षरित मंगलौर की संधि (1784) ने दोनों ओर के जीते क्षेत्र लौटाए; श्रीरंगपट्टनम की संधि (1792) ने टीपू को अपना आधा राज्य कंपनी और उसके सहयोगियों को देने पर विवश किया। "
  "युग्म 3 गलत है: सालबाई की संधि (1782) ने महादजी सिंधिया की मध्यस्थता से पहला आंग्ल-मराठा युद्ध समाप्त किया और बीस वर्ष तक शांति रखी। युग्म 4 दो तरह से गलत है: बसीन की संधि (1802) किसी युद्ध को समाप्त करने वाली शांति-संधि नहीं, बल्कि भागे हुए पेशवा बाजीराव द्वितीय द्वारा हस्ताक्षरित सहायक संधि थी, और इसी ने दूसरा आंग्ल-मराठा युद्ध भड़काया।",
  f"{BC} -- British conquest of India.",
  "modern-treaties-wars-pairs")

if __name__ == "__main__":
    write("hist_l2_t5_modern.sql")
