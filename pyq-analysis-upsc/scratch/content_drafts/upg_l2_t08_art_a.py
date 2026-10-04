# -*- coding: utf-8 -*-
"""Level 2 · Test 8 (History 4: Art & Culture) -- depth audit of 2026-10-04, part A: Architecture and
Culture-Other (docs/upsc-question-design-standard.md §6). Part B (upg_l2_t08_art_b.py) has Iconography
and Painting; part C (upg_l2_t08_art_c.py) has Music & Dance and the tags for the kept rows.

Before the audit the test had analytic 1, precision 12, recall 89. Part A rewrites 18 rows in place with
the same concept id, type and difficulty:
  - architecture now asks a student to identify a style or a part from a description, to say what a
    feature does or why it was built, and to judge a five-item list (Buddhist rock-cut sites);
  - culture-other now asks five-item judgements (martial arts and their regions, Karnataka's GI
    products, India's UNESCO intangible heritage), what sets Chhath apart, and textile techniques.
Leaks avoided while drafting:
  - the shape of the tower in the south Indian temple stem (answers the temple-styles row);
  - the Alai Darwaza's true arch (repeats the Indo-Islamic synthesis row);
  - Kalamkari as anything but cloth painting (would knock out a distractor in the Kalamkari MCQ)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write_updates, CODE
from polity_common import C3, C4, T2

d.SUBJECT = "History"
d.REQUIRE_CRAFT = True
ARC = "Architecture"
CUL = "Culture-Other"
NFA = "NCERT Class XI, An Introduction to Indian Art"
NLH = "NCERT Class XII, Living Craft Traditions of India"
MOC = "Ministry of Culture, Government of India"
FIVE = ["Only two", "Only three", "Only four", "All five"]
FIVE_HI = ["केवल दो", "केवल तीन", "केवल चार", "सभी पाँच"]

# ================================================================ ARCHITECTURE: pairs (2)
P(ARC, "hard", "Consider the following pairs of temples and features for which they are notable:",
  "निम्नलिखित मंदिरों और उन विशेषताओं के युग्मों पर विचार कीजिए जिनके लिए वे उल्लेखनीय हैं:",
  ["Brihadeshwara temple, Thanjavur : A towering vimana over the sanctum, far taller than its gateways",
   "Kailasa temple, Ellora : A structural temple built of dressed stone blocks",
   "Virupaksha temple, Pattadakal : A curvilinear Nagara shikhara over the sanctum",
   "Sun temple, Modhera : A great stepped tank (kund) in front of the temple"],
  ["बृहदेश्वर मंदिर, तंजावुर : गर्भगृह के ऊपर एक विशाल विमान, जो अपने प्रवेश-द्वारों से कहीं ऊँचा है",
   "कैलास मंदिर, एलोरा : गढ़े गए पत्थर के खंडों से बना एक संरचनात्मक मंदिर",
   "विरूपाक्ष मंदिर, पट्टदकल : गर्भगृह के ऊपर एक वक्ररेखीय नागर शिखर",
   "सूर्य मंदिर, मोढेरा : मंदिर के सामने एक विशाल सीढ़ीदार कुंड"],
  1,
  "Only pairs 1 and 4 are correct. Rajaraja I's temple at Thanjavur raised a vimana about 66 metres high over the sanctum; in later Dravida temples the gopurams outgrew the shrine, as at Madurai. The Solanki Sun temple at Modhera, of the eleventh century, stands behind the Surya Kund, a tank lined with small shrines on its steps. "
  "Pair 2 is wrong: the Kailasa temple was cut out of the living rock, from the top downwards. Pair 3 is wrong: the Virupaksha at Pattadakal, built by Queen Lokamahadevi for Vikramaditya II of the Badami Chalukyas, has a Dravida vimana; Pattadakal is known for having temples of both styles side by side.",
  "केवल युग्म 1 और 4 सही हैं। तंजावुर में राजराज प्रथम के मंदिर ने गर्भगृह के ऊपर लगभग 66 मीटर ऊँचा विमान खड़ा किया; बाद के द्रविड़ मंदिरों में गोपुरम गर्भगृह से ऊँचे हो गए, जैसे मदुरै में। ग्यारहवीं सदी का सोलंकी सूर्य मंदिर मोढेरा सूर्य कुंड के पीछे खड़ा है, जिसकी सीढ़ियों पर छोटे देवालय बने हैं। "
  "युग्म 2 गलत है: कैलास मंदिर जीवित चट्टान को ऊपर से नीचे की ओर काटकर बनाया गया। युग्म 3 गलत है: बादामी चालुक्य विक्रमादित्य द्वितीय के लिए रानी लोकमहादेवी द्वारा बनवाए गए पट्टदकल के विरूपाक्ष का विमान द्रविड़ शैली का है; पट्टदकल दोनों शैलियों के मंदिरों के साथ-साथ होने के लिए जाना जाता है।",
  NFA, "art-culture-temples-dynasties-pairs", craft="precision")

P(ARC, "medium", "Consider the following pairs of features of Indo-Islamic architecture and what they do:",
  "हिंद-इस्लामी स्थापत्य की निम्नलिखित विशेषताओं और उनके कार्य के युग्मों पर विचार कीजिए:",
  ["Mihrab : Shows the direction of prayer, towards Mecca",
   "Jali : Lets in light and air while screening the interior",
   "Pishtaq : Gives a building a monumental entrance, as a tall arch set in a rectangular frame",
   "Squinch : A tower from which the call to prayer is given"],
  ["मिहराब : नमाज़ की दिशा, मक्का की ओर, दिखाता है",
   "जाली : भीतरी भाग को ओट देते हुए प्रकाश और हवा आने देती है",
   "पिश्ताक़ : आयताकार ढाँचे में बने ऊँचे मेहराब के रूप में इमारत को भव्य प्रवेश देता है",
   "स्क्विंच : एक मीनार जिससे अज़ान दी जाती है"],
  2,
  "Three pairs are correct. The mihrab, a niche in the qibla wall, shows worshippers which way to face; carved stone jalis, as at Sidi Saiyyed's mosque in Ahmedabad or Salim Chishti's tomb, filter light and air in a hot climate while giving privacy; and the pishtaq, the tall framed arch of Mughal gateways and tombs, marks the entrance. "
  "Pair 4 is wrong: a squinch is an arch built across the corner of a square room so that a round dome can sit on it; the tower for the call to prayer is the minaret.",
  "तीन युग्म सही हैं। क़िबला दीवार में बना आला, मिहराब, नमाज़ियों को दिशा बताता है; अहमदाबाद की सीदी सैयद मस्जिद या सलीम चिश्ती के मक़बरे जैसी पत्थर की नक़्क़ाशीदार जालियाँ गर्म जलवायु में प्रकाश और हवा छानती हैं और निजता देती हैं; और मुग़ल प्रवेश-द्वारों तथा मक़बरों का ऊँचा ढाँचेदार मेहराब, पिश्ताक़, प्रवेश को चिह्नित करता है। "
  "युग्म 4 गलत है: स्क्विंच वर्गाकार कक्ष के कोने के आर-पार बना मेहराब है, ताकि उस पर गोल गुंबद टिक सके; अज़ान की मीनार मीनार ही कहलाती है।",
  NFA, "art-indo-islamic-terms-pairs", craft="linkage")

# ================================================================ ARCHITECTURE: MCQs (3)
M(ARC, "hard", "The Dilwara temples at Mount Abu, built of white marble between the eleventh and thirteenth centuries by Jain ministers of the Gujarat kings, best show:",
  "ग्यारहवीं से तेरहवीं सदी के बीच गुजरात के राजाओं के जैन मंत्रियों द्वारा सफ़ेद संगमरमर से बनवाए गए आबू पर्वत के दिलवाड़ा मंदिर सबसे अच्छी तरह क्या दिखाते हैं?",
  ["the wealth of the Jain merchant and official class of western India and its patronage of temples",
   "the royal patronage of Buddhism by the Solanki kings of Gujarat in the face of Brahmanical opposition",
   "the influence of Persian tile-work brought to Gujarat by the Delhi Sultans",
   "the replacement of stone by brick in the temple architecture of the period"],
  ["पश्चिमी भारत के जैन व्यापारी और अधिकारी वर्ग की संपत्ति और मंदिरों के लिए उसके संरक्षण को",
   "ब्राह्मणवादी विरोध के बीच गुजरात के सोलंकी राजाओं द्वारा बौद्ध धर्म के राजकीय संरक्षण को",
   "दिल्ली सुल्तानों द्वारा गुजरात लाई गई फ़ारसी टाइल-कला के प्रभाव को",
   "उस काल के मंदिर स्थापत्य में पत्थर के स्थान पर ईंट के उपयोग को"],
  0,
  "The Vimala Vasahi was built by Vimala Shah, a minister of the Solanki king Bhima I, and the Luna Vasahi by the brothers Vastupala and Tejapala, ministers of the Vaghelas. Jain merchants and officials of Gujarat and Rajasthan, wealthy from trade and office, poured their resources into temples whose marble ceilings, pillars and brackets are carved as finely as lace. "
  "The temples are Jain, not Buddhist; they owe nothing to Persian tile-work; and they are of marble brought up the mountain, not brick.",
  "विमल वसही सोलंकी राजा भीम प्रथम के मंत्री विमल शाह ने और लूण वसही वाघेलों के मंत्री भाइयों वस्तुपाल और तेजपाल ने बनवाया। व्यापार और पद से समृद्ध गुजरात और राजस्थान के जैन व्यापारियों और अधिकारियों ने अपने संसाधन ऐसे मंदिरों में लगाए जिनकी संगमरमर की छतें, स्तंभ और टोड़े लेस जितनी बारीकी से तराशे गए हैं। "
  "मंदिर जैन हैं, बौद्ध नहीं; उन पर फ़ारसी टाइल-कला का कोई प्रभाव नहीं; और वे ईंट के नहीं, पहाड़ पर ऊपर लाए गए संगमरमर के हैं।",
  NFA, "art-dilwara-jain-temples", craft="linkage")

M(ARC, "medium", "A temple has a tall curvilinear tower over the sanctum (a rekha deul) and, in front of it, a hall with a pyramid-shaped roof built in receding tiers (a pidha deul). The temple is most likely to be found at:",
  "एक मंदिर के गर्भगृह के ऊपर एक ऊँचा वक्ररेखीय शिखर (रेखा देउल) है और उसके सामने पीछे हटते स्तरों में बनी पिरामिडनुमा छत वाला मंडप (पीढ़ा देउल) है। ऐसा मंदिर सबसे अधिक संभावना से कहाँ मिलेगा?",
  ["Bhubaneswar, as in the Lingaraja temple",
   "Mamallapuram, as in the Shore Temple",
   "Halebidu, as in the Hoysaleswara temple",
   "Madurai, as in the Meenakshi temple"],
  ["भुवनेश्वर में, जैसे लिंगराज मंदिर",
   "मामल्लपुरम में, जैसे तट मंदिर",
   "हलेबिडु में, जैसे होयसलेश्वर मंदिर",
   "मदुरै में, जैसे मीनाक्षी मंदिर"],
  0,
  "The pairing of a rekha deul over the sanctum with a pidha deul as the hall (jagamohana) defines the Kalinga style, a regional form of the Nagara tradition. It reached its high point in the eleventh-century Lingaraja temple at Bhubaneswar, the 'temple city', and later at Puri and Konark. "
  "The Shore Temple and the Meenakshi temple are Dravida, with stepped vimanas and, at Madurai, towering gopurams, while the Hoysaleswara at Halebidu stands on a star-shaped platform in the Hoysala style.",
  "गर्भगृह के ऊपर रेखा देउल और मंडप (जगमोहन) के रूप में पीढ़ा देउल का यह मेल कलिंग शैली की पहचान है, जो नागर परंपरा का एक क्षेत्रीय रूप है। यह ग्यारहवीं सदी के भुवनेश्वर, 'मंदिरों के नगर', के लिंगराज मंदिर में और बाद में पुरी तथा कोणार्क में अपने चरम पर पहुँची। "
  "तट मंदिर और मीनाक्षी मंदिर द्रविड़ शैली के हैं, जिनमें सीढ़ीदार विमान और मदुरै में विशाल गोपुरम हैं, जबकि हलेबिडु का होयसलेश्वर होयसल शैली में तारे के आकार के चबूतरे पर खड़ा है।",
  NFA, "art-lingaraja-bhubaneswar", craft="application")

M(ARC, "medium", "Stepwells such as Rani ki Vav at Patan were built in large numbers in Gujarat and Rajasthan mainly because:",
  "पाटन की रानी की वाव जैसी बावड़ियाँ गुजरात और राजस्थान में बड़ी संख्या में मुख्यतः इसलिए बनाई गईं कि:",
  ["in a dry region with seasonal rain they gave access to groundwater all year, and cool places to rest",
   "the Delhi Sultans required every town in the two regions to build a public bath for ritual purification",
   "they were royal swimming pools reserved for the use of the queens of the court",
   "they stored the water of canals cut from the Indus for irrigation"],
  ["मौसमी वर्षा वाले सूखे क्षेत्र में वे साल भर भूजल तक पहुँच और विश्राम के ठंडे स्थान देती थीं",
   "दिल्ली सुल्तानों ने दोनों क्षेत्रों के हर नगर को अनुष्ठानिक शुद्धि के लिए सार्वजनिक स्नानागार बनाने का आदेश दिया था",
   "वे दरबार की रानियों के उपयोग के लिए आरक्षित शाही तरणताल थीं",
   "वे सिंचाई के लिए सिंधु से काटी गई नहरों का पानी जमा करती थीं"],
  0,
  "Stepwells let people walk down many storeys to a water table that rose and fell with the seasons, so water could be drawn even in the dry months; their shaded galleries were cool in the heat and served as places to meet, rest and worship. Rani ki Vav, built in the eleventh century in memory of the Solanki king Bhima I, has seven levels lined with some 500 sculptures, many of Vishnu's avatars, and is a World Heritage Site. "
  "They were built by queens, merchants and communities for public use, long before and apart from any Sultanate rule.",
  "बावड़ियाँ लोगों को कई मंज़िल नीचे उस जल-स्तर तक जाने देती थीं जो मौसम के साथ ऊपर-नीचे होता था, जिससे सूखे महीनों में भी पानी निकाला जा सके; उनकी छायादार दीर्घाएँ गर्मी में ठंडी रहती थीं और मिलने, विश्राम और उपासना की जगह थीं। सोलंकी राजा भीम प्रथम की स्मृति में ग्यारहवीं सदी में बनी रानी की वाव के सात स्तर लगभग 500 मूर्तियों से सजे हैं, जिनमें कई विष्णु के अवतारों की हैं, और यह विश्व धरोहर स्थल है। "
  "इन्हें रानियों, व्यापारियों और समुदायों ने सार्वजनिक उपयोग के लिए बनवाया, किसी सल्तनत शासन से बहुत पहले और उससे अलग।",
  NFA, "art-rani-ki-vav", craft="linkage")

# ================================================================ ARCHITECTURE: statements (7)
S(ARC, "easy", "A visitor to a large south Indian temple first passes through a tall gateway tower, crosses a pillared hall and reaches the sanctum, over which rises the main tower. Consider the following statements:",
  "दक्षिण भारत के एक बड़े मंदिर में आगंतुक पहले एक ऊँचे प्रवेश-द्वार के शिखर से गुज़रता है, एक स्तंभयुक्त मंडप पार करता है और गर्भगृह तक पहुँचता है, जिसके ऊपर मुख्य शिखर उठता है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The gateway tower is called the gopuram.",
   "The main tower over the sanctum is called the vimana.",
   "The pillared hall is called the garbhagriha."],
  ["प्रवेश-द्वार का शिखर गोपुरम कहलाता है।",
   "गर्भगृह के ऊपर का मुख्य शिखर विमान कहलाता है।",
   "स्तंभयुक्त मंडप गर्भगृह कहलाता है।"],
  C3, 1,
  "Statements 1 and 2 are correct. In the Dravida temple the gopuram marks the gateway in the enclosure wall, and in later temples such as Madurai the gopurams grew taller than the vimana, the tower over the sanctum. "
  "Statement 3 is wrong: the pillared hall is the mandapa; the garbhagriha ('womb-house') is the small, dark sanctum that holds the main image.",
  "कथन 1 और 2 सही हैं। द्रविड़ मंदिर में गोपुरम परकोटे की दीवार में प्रवेश-द्वार को चिह्नित करता है, और मदुरै जैसे बाद के मंदिरों में गोपुरम गर्भगृह के ऊपर के शिखर, विमान, से ऊँचे हो गए। "
  "कथन 3 गलत है: स्तंभयुक्त मंडप मंडप ही कहलाता है; गर्भगृह मुख्य प्रतिमा वाला छोटा, अँधेरा देवालय है।",
  NFA, "art-temple-parts-gopuram-vimana", craft="application")

S(ARC, "hard", "A north Indian temple's tower is crowned by a ribbed stone disc and a pot-shaped finial, a vestibule links the sanctum to the hall, and the whole temple stands on a broad raised terrace. Consider the following statements:",
  "उत्तर भारत के एक मंदिर के शिखर के शीर्ष पर एक धारीदार पत्थर की चकरी और घड़े के आकार का कलश है, एक अंतराल गर्भगृह को मंडप से जोड़ता है, और पूरा मंदिर एक चौड़े ऊँचे चबूतरे पर खड़ा है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The ribbed disc is the amalaka.",
   "The pot-shaped finial is the kalasha.",
   "The vestibule is the antarala.",
   "The raised terrace is the mandapa."],
  ["धारीदार चकरी आमलक है।",
   "घड़े के आकार का शीर्ष कलश है।",
   "अंतराल को अंतराल ही कहते हैं।",
   "ऊँचा चबूतरा मंडप है।"],
  C4, 2,
  "Statements 1, 2 and 3 are correct. The amalaka, named after the ribbed amla fruit, and the kalasha above it crown the Nagara shikhara; the antarala is the passage between the garbhagriha and the mandapa. "
  "Statement 4 is wrong: the raised terrace is the jagati, which in temples such as those at Khajuraho lifts the building and provides a path round it; the mandapa is the hall in front of the sanctum.",
  "कथन 1, 2 और 3 सही हैं। धारीदार आँवले के नाम पर आमलक और उसके ऊपर कलश नागर शिखर के शीर्ष हैं; अंतराल गर्भगृह और मंडप के बीच का मार्ग है। "
  "कथन 4 गलत है: ऊँचा चबूतरा जगती है, जो खजुराहो जैसे मंदिरों में इमारत को ऊपर उठाती और उसके चारों ओर मार्ग देती है; मंडप गर्भगृह के सामने का मंडप-कक्ष है।",
  NFA, "art-temple-terms-amalaka-jagati", craft="application")

S(ARC, "medium", "Consider the following statements about Hoysala temples:",
  "होयसल मंदिरों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Their builders used soft soapstone (chloritic schist), which hardens on exposure, and this made their extremely fine carving possible.",
   "Many of them stand on a star-shaped (stellate) platform.",
   "The Hoysaleswara temple at Halebidu has twin shrines."],
  ["उनके निर्माताओं ने मुलायम सोपस्टोन (क्लोराइटिक शिस्ट) का उपयोग किया, जो खुले में कड़ा हो जाता है, और इसी ने उनकी अत्यंत बारीक नक़्क़ाशी संभव की।",
   "उनमें से कई तारे के आकार के (तारकाकार) चबूतरे पर खड़े हैं।",
   "हलेबिडु के होयसलेश्वर मंदिर में दो गर्भगृह हैं।"],
  C3, 2,
  "All three are correct. Soapstone can be carved almost like wood when freshly quarried and then hardens, which explains the jewellery-like detail of the figures, the lathe-turned pillars and the bands of elephants, horses and epic scenes at Belur and Halebidu. The star-shaped plan multiplies the projecting angles and the play of light and shade. "
  "The twelfth-century Hoysaleswara at Halebidu, the old capital Dwarasamudra, has two shrines side by side, and the Chennakeshava at Belur is dedicated to Vishnu.",
  "तीनों कथन सही हैं। ताज़ा निकाला गया सोपस्टोन लगभग लकड़ी की तरह तराशा जा सकता है और फिर कड़ा हो जाता है, जो बेलूर और हलेबिडु की मूर्तियों के आभूषण-जैसे विवरण, ख़राद पर बने से लगते स्तंभों और हाथियों, घोड़ों तथा महाकाव्यों के दृश्यों की पट्टियों की व्याख्या करता है। तारकाकार योजना उभरे हुए कोनों और प्रकाश-छाया के खेल को कई गुना बढ़ा देती है। "
  "पुरानी राजधानी द्वारसमुद्र, हलेबिडु, के बारहवीं सदी के होयसलेश्वर मंदिर में दो गर्भगृह साथ-साथ हैं, और बेलूर का चेन्नकेशव मंदिर विष्णु को समर्पित है।",
  NFA, "art-hoysala-temples", craft="linkage")

S(ARC, "medium", "Consider the following statements about Khajuraho and Konark:",
  "खजुराहो और कोणार्क के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Sun temple at Konark was designed as the chariot of the Sun god, with carved wheels and horses.",
   "The temples at Khajuraho include Jain temples as well as Hindu ones.",
   "The temples at Khajuraho were built under the Eastern Gangas."],
  ["कोणार्क का सूर्य मंदिर सूर्य देव के रथ के रूप में बनाया गया, जिसमें तराशे गए पहिए और घोड़े हैं।",
   "खजुराहो के मंदिरों में हिंदू मंदिरों के साथ जैन मंदिर भी हैं।",
   "खजुराहो के मंदिर पूर्वी गंगों के समय बने।"],
  C3, 1,
  "Statements 1 and 2 are correct. Narasimhadeva I of the Eastern Gangas built Konark in the thirteenth century as a colossal chariot with twenty-four carved wheels drawn by seven horses -- the idea of the Sun's daily journey given architectural form. At Khajuraho the Chandellas and their subjects built Jain temples, such as the Parshvanatha, alongside the Hindu ones, a sign of shared patronage. "
  "Statement 3 is wrong: Khajuraho was the work of the Chandellas, between about 950 and 1050, with the Kandariya Mahadeva as the high point of the Nagara style.",
  "कथन 1 और 2 सही हैं। पूर्वी गंग नरसिंहदेव प्रथम ने तेरहवीं सदी में कोणार्क को सात घोड़ों द्वारा खींचे जाने वाले चौबीस तराशे पहियों वाले विशाल रथ के रूप में बनवाया, यानी सूर्य की दैनिक यात्रा के विचार को स्थापत्य रूप दिया। खजुराहो में चंदेलों और उनकी प्रजा ने हिंदू मंदिरों के साथ पार्श्वनाथ जैसे जैन मंदिर बनवाए, जो साझा संरक्षण का संकेत है। "
  "कथन 3 गलत है: खजुराहो लगभग 950 से 1050 के बीच चंदेलों का काम था, जिसमें कंदरिया महादेव नागर शैली का शिखर है।",
  NFA, "art-khajuraho-konark", craft="linkage")

S(ARC, "medium", "Consider the following statements about Humayun's tomb in Delhi:",
  "दिल्ली के हुमायूँ के मक़बरे के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["With its charbagh garden and double dome, it set the model that the Taj Mahal later perfected.",
   "It is faced entirely in white marble.",
   "It was designed by Ustad Ahmad Lahori."],
  ["अपने चारबाग़ उद्यान और दोहरे गुंबद के साथ इसने वह आदर्श रखा जिसे बाद में ताजमहल ने पूर्णता दी।",
   "इसका पूरा बाहरी भाग सफ़ेद संगमरमर का है।",
   "इसकी रूपरेखा उस्ताद अहमद लाहौरी ने बनाई।"],
  C3, 0,
  "Only statement 1 is correct. Commissioned by Humayun's widow Haji Begum in the 1560s and designed by the Persian architect Mirak Mirza Ghiyas, it placed the tomb on a high platform at the centre of a four-part garden divided by water channels, and used a double dome to give height outside while keeping the inner ceiling in proportion -- the scheme the Taj Mahal refined. "
  "Statement 2 is wrong: it is built of red sandstone with white marble used for contrast; the first Mughal tomb faced wholly in white marble was I'timad-ud-Daula's. Statement 3 is wrong: Ustad Ahmad Lahori is associated with the Taj Mahal.",
  "केवल कथन 1 सही है। 1560 के दशक में हुमायूँ की विधवा हाजी बेगम द्वारा बनवाए गए और फ़ारसी वास्तुकार मीरक मिर्ज़ा ग़ियास द्वारा रूपित मक़बरे ने उसे जल-नालियों से बँटे चार भागों वाले उद्यान के बीच ऊँचे चबूतरे पर रखा, और भीतरी छत को अनुपात में रखते हुए बाहर ऊँचाई देने के लिए दोहरे गुंबद का उपयोग किया, वही योजना जिसे ताजमहल ने निखारा। "
  "कथन 2 गलत है: यह लाल बलुआ पत्थर का है, जिसमें विरोधाभास के लिए सफ़ेद संगमरमर लगा है; पूरी तरह सफ़ेद संगमरमर से ढका पहला मुग़ल मक़बरा एतमादुद्दौला का था। कथन 3 गलत है: उस्ताद अहमद लाहौरी ताजमहल से जुड़े हैं।",
  NFA, "art-mughal-humayun-tomb-taj", craft="linkage")

S(ARC, "medium", "Consider the following rock-cut sites:",
  "निम्नलिखित शैलकृत स्थलों पर विचार कीजिए:",
  ["Karle", "Bhaja", "Udayagiri and Khandagiri", "Elephanta", "Ajanta"],
  ["कार्ले", "भाजा", "उदयगिरि और खंडगिरि", "एलीफ़ेंटा", "अजंता"],
  None, 1,
  "Three of them are primarily Buddhist. The great chaitya hall at Karle (first century CE), with its horseshoe-shaped window and rows of pillars, and the earlier caves at Bhaja are among the finest Buddhist rock-cut halls of the western Deccan, and Ajanta's caves are Buddhist chaityas and viharas. "
  "The Udayagiri and Khandagiri caves near Bhubaneswar were cut for Jain monks under Kharavela, and the main cave at Elephanta, of about the sixth century, is a Shiva temple famous for the three-headed Maheshamurti.",
  "इनमें से तीन मुख्यतः बौद्ध हैं। घोड़े की नाल के आकार की खिड़की और स्तंभों की पंक्तियों वाला कार्ले (पहली सदी ई.) का महान चैत्य-कक्ष और भाजा की पहले की गुफाएँ पश्चिमी दक्कन के सबसे सुंदर बौद्ध शैलकृत कक्षों में हैं, और अजंता की गुफाएँ बौद्ध चैत्य और विहार हैं। "
  "भुवनेश्वर के पास उदयगिरि और खंडगिरि की गुफाएँ खारवेल के समय जैन भिक्षुओं के लिए काटी गईं, और लगभग छठी सदी की एलीफ़ेंटा की मुख्य गुफा शिव मंदिर है, जो त्रिमुखी महेशमूर्ति के लिए प्रसिद्ध है।",
  NFA, "art-rock-cut-caves-elephanta-karle", opts=FIVE, opts_hi=FIVE_HI,
  closing="How many of the above are primarily Buddhist?", closing_hi="उपर्युक्त में से कितने मुख्यतः बौद्ध हैं?", craft="multi")

S(ARC, "medium", "Consider the following statements about the architecture of the Delhi Sultanate:",
  "दिल्ली सल्तनत के स्थापत्य के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Quwwat-ul-Islam mosque reused carved pillars from demolished temples, so its early parts show the work of Indian craftsmen.",
   "The buildings of the Tughlaqs are known for their lavish marble inlay.",
   "The Qutub Minar was built as a watch-tower for the Tughlaq army."],
  ["क़ुव्वत-उल-इस्लाम मस्जिद में ध्वस्त मंदिरों के तराशे गए स्तंभ फिर से लगाए गए, इसलिए इसके प्रारंभिक भागों में भारतीय कारीगरों का काम दिखता है।",
   "तुग़लक़ों की इमारतें अपनी भव्य संगमरमर जड़ाई के लिए जानी जाती हैं।",
   "क़ुतुब मीनार तुग़लक़ सेना के लिए प्रहरी-मीनार के रूप में बनी।"],
  C3, 0,
  "Only statement 1 is correct. The first mosque in Delhi, begun in the 1190s under Qutb-ud-din Aibak, was raised on a temple plinth with pillars taken from temples; the carving on them, and on the great screen in front of the prayer hall, is the work of local craftsmen who were still learning the new forms. "
  "Statement 2 is wrong: Tughlaq buildings, such as Tughlaqabad and Ghiyasuddin's tomb, are massive and austere, with sloping walls and little decoration. Statement 3 is wrong: the Qutub Minar was begun by Aibak as a tower of victory and a minaret for the mosque, and completed by Iltutmish.",
  "केवल कथन 1 सही है। 1190 के दशक में क़ुतुबुद्दीन ऐबक के समय शुरू हुई दिल्ली की पहली मस्जिद एक मंदिर के चबूतरे पर, मंदिरों से लिए गए स्तंभों के साथ खड़ी की गई; उन पर, और नमाज़-कक्ष के सामने के बड़े परदे पर, की नक़्क़ाशी उन स्थानीय कारीगरों का काम है जो नए रूप अभी सीख रहे थे। "
  "कथन 2 गलत है: तुग़लक़ाबाद और ग़यासुद्दीन के मक़बरे जैसी तुग़लक़ इमारतें विशाल और सादी हैं, जिनकी दीवारें ढलवाँ हैं और सजावट कम है। कथन 3 गलत है: क़ुतुब मीनार ऐबक ने विजय-स्तंभ और मस्जिद की मीनार के रूप में शुरू की, और इल्तुतमिश ने उसे पूरा किया।",
  NFA, "art-sultanate-architecture-quwwat-alai", craft="linkage")

# ================================================================ CULTURE-OTHER (6)
P(CUL, "medium", "Consider the following pairs of textile traditions and their distinctive techniques:",
  "निम्नलिखित वस्त्र परंपराओं और उनकी विशिष्ट तकनीकों के युग्मों पर विचार कीजिए:",
  ["Ikat of Pochampally : Yarns tie-dyed before they are woven",
   "Jamdani : Motifs woven into the fabric on the loom with an extra weft",
   "Bandhani : Cloth tie-dyed after it is woven",
   "Patola of Patan : Both warp and weft tie-dyed before weaving (double ikat)"],
  ["पोचमपल्ली इकत : बुनाई से पहले धागों को बाँधकर रँगा जाता है",
   "जामदानी : करघे पर अतिरिक्त बाने से कपड़े में नमूने बुने जाते हैं",
   "बंधनी : बुनाई के बाद कपड़े को बाँधकर रँगा जाता है",
   "पाटन का पटोला : बुनाई से पहले ताना और बाना दोनों बाँधकर रँगे जाते हैं (दोहरा इकत)"],
  3,
  "All four pairs are correct. In ikat the pattern is dyed into the yarn before weaving, which gives its soft, blurred edges; Pochampally in Telangana is a leading centre. Jamdani, once the muslin of Dhaka, has motifs inserted by hand with an extra weft as the cloth is woven. Bandhani of Gujarat and Rajasthan is made by tying tiny points of finished cloth before dyeing. "
  "Patola of Patan is the most demanding of all: both the warp and the weft are resist-dyed so that the pattern meets exactly on the loom.",
  "चारों युग्म सही हैं। इकत में नमूना बुनाई से पहले धागे में रँगा जाता है, जिससे उसके किनारे कोमल और धुँधले होते हैं; तेलंगाना का पोचमपल्ली इसका प्रमुख केंद्र है। कभी ढाका की मलमल रही जामदानी में कपड़ा बुनते समय अतिरिक्त बाने से हाथ से नमूने डाले जाते हैं। गुजरात और राजस्थान की बंधनी तैयार कपड़े के छोटे-छोटे बिंदु बाँधकर रँगने से बनती है। "
  "पाटन का पटोला सबसे कठिन है: ताना और बाना दोनों प्रतिरोध-रँगाई से रँगे जाते हैं ताकि करघे पर नमूना ठीक मिल जाए।",
  NLH, "culture-weaving-traditions-pairs", craft="linkage")

M(CUL, "hard", "Consider the following traditional martial arts and the regions to which they belong:\n1. Kalaripayattu -- Kerala\n2. Silambam -- Tamil Nadu\n3. Thang-ta -- Manipur\n4. Gatka -- Punjab\n5. Mardani Khel -- Assam\nWhich of the pairs given above are correctly matched?",
  "निम्नलिखित पारंपरिक युद्ध-कलाओं और उनके क्षेत्रों पर विचार कीजिए:\n1. कलरिपयट्टु -- केरल\n2. सिलंबम -- तमिलनाडु\n3. थांग-ता -- मणिपुर\n4. गतका -- पंजाब\n5. मर्दानी खेल -- असम\nउपर्युक्त में से कौन-से युग्म सही सुमेलित हैं?",
  ["1, 2, 3 and 4 only", "1, 3 and 5 only", "2, 3, 4 and 5 only", "1, 2, 3, 4 and 5"],
  ["केवल 1, 2, 3 और 4", "केवल 1, 3 और 5", "केवल 2, 3, 4 और 5", "1, 2, 3, 4 और 5"],
  0,
  "Pairs 1 to 4 are correct. Kalaripayattu, taught in the kalari of Kerala, combines strikes, weapons and healing; Silambam of Tamil Nadu is a bamboo-staff art; Thang-ta ('sword and spear') is the martial art of the Meitei of Manipur, performed with ritual and breathing techniques; and Gatka is the Sikh art of stick and sword fighting, often shown at gurpurab processions. "
  "Pair 5 is wrong: Mardani Khel, using the sword and the long-bladed patta, is a Maratha martial art of Maharashtra, associated with Kolhapur.",
  "युग्म 1 से 4 सही हैं। केरल के कलरी में सिखाई जाने वाली कलरिपयट्टु प्रहार, शस्त्र और उपचार को जोड़ती है; तमिलनाडु का सिलंबम बाँस की लाठी की कला है; थांग-ता ('तलवार और भाला') मणिपुर के मैतेई लोगों की युद्ध-कला है, जो अनुष्ठान और श्वास-तकनीकों के साथ की जाती है; और गतका लाठी और तलवार से लड़ने की सिख कला है, जो प्रायः गुरपुरब की शोभायात्राओं में दिखाई जाती है। "
  "युग्म 5 गलत है: तलवार और लंबे फल वाले पट्टे से खेला जाने वाला मर्दानी खेल महाराष्ट्र की, कोल्हापुर से जुड़ी, मराठा युद्ध-कला है।",
  MOC, "culture-thang-ta-manipur", craft="multi")

M(CUL, "medium", "Which one of the following best describes what sets the festival of Chhath apart?",
  "निम्नलिखित में से कौन-सा सबसे अच्छी तरह बताता है कि छठ पर्व को क्या अलग बनाता है?",
  ["Devotees offer arghya to the setting and rising sun at rivers and ponds, with no priest needed",
   "It is a festival of lamps celebrating the return of Rama to Ayodhya after his fourteen years of exile",
   "It honours the goddess Durga's victory over the buffalo demon Mahishasura",
   "It is celebrated by flying kites to mark the sun's entry into Capricorn"],
  ["भक्त नदियों और तालाबों पर डूबते और उगते सूर्य को अर्घ्य देते हैं, किसी पुरोहित की ज़रूरत नहीं होती",
   "यह चौदह वर्ष के वनवास के बाद राम के अयोध्या लौटने का उत्सव मनाने वाला दीपों का पर्व है",
   "यह भैंसासुर महिषासुर पर देवी दुर्गा की विजय का सम्मान करता है",
   "यह सूर्य के मकर राशि में प्रवेश को पतंगें उड़ाकर मनाया जाता है"],
  0,
  "Chhath, celebrated over four days especially in Bihar, Jharkhand and eastern Uttar Pradesh, is addressed to Surya and Chhathi Maiya. Devotees, very often women, fast strictly, stand in rivers or ponds and offer arghya first to the setting and then to the rising sun; there is no priestly intermediary, and the ritual stresses cleanliness and the community's shared labour at the ghats. "
  "The other options describe Diwali, Durga Puja and Makar Sankranti (Uttarayan in Gujarat).",
  "बिहार, झारखंड और पूर्वी उत्तर प्रदेश में विशेष रूप से चार दिन मनाया जाने वाला छठ सूर्य और छठी मैया को समर्पित है। भक्त, अक्सर स्त्रियाँ, कठोर उपवास रखते हैं, नदियों या तालाबों में खड़े होते हैं और पहले डूबते फिर उगते सूर्य को अर्घ्य देते हैं; कोई पुरोहित मध्यस्थ नहीं होता, और अनुष्ठान स्वच्छता तथा घाटों पर समुदाय के साझा श्रम पर ज़ोर देता है। "
  "अन्य विकल्प दीपावली, दुर्गा पूजा और मकर संक्रांति (गुजरात में उत्तरायण) का वर्णन करते हैं।",
  MOC, "culture-chhath-surya", craft="inference")

S(CUL, "easy", "Consider the following statements about the Kumbh Mela:",
  "कुंभ मेले के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The full Kumbh comes round at each of its four sites about every twelve years, following the position of Jupiter.",
   "The Ardh Kumbh is held at all four sites every six years."],
  ["पूर्ण कुंभ अपने चारों स्थलों में से हर एक पर लगभग हर बारह वर्ष में, बृहस्पति की स्थिति के अनुसार, आता है।",
   "अर्धकुंभ चारों स्थलों पर हर छह वर्ष में होता है।"],
  T2, 0,
  "Only statement 1 is correct. The Kumbh rotates among Prayagraj, Haridwar, Ujjain and Nashik according to the positions of Jupiter and the Sun, so each site hosts it about every twelve years; at Prayagraj the Maha Kumbh comes after twelve Kumbhs. "
  "Statement 2 is wrong: the Ardh ('half') Kumbh is held only at Prayagraj and Haridwar, about six years after the full Kumbh there. UNESCO inscribed the Kumbh Mela on its intangible heritage list in 2017.",
  "केवल कथन 1 सही है। कुंभ बृहस्पति और सूर्य की स्थितियों के अनुसार प्रयागराज, हरिद्वार, उज्जैन और नासिक के बीच घूमता है, इसलिए हर स्थल लगभग हर बारह वर्ष में इसका आयोजन करता है; प्रयागराज में बारह कुंभों के बाद महाकुंभ आता है। "
  "कथन 2 गलत है: अर्ध ('आधा') कुंभ केवल प्रयागराज और हरिद्वार में, वहाँ के पूर्ण कुंभ के लगभग छह वर्ष बाद, होता है। यूनेस्को ने 2017 में कुंभ मेले को अपनी अमूर्त धरोहर सूची में शामिल किया।",
  MOC, "culture-kumbh-mela", craft="precision")

S(CUL, "hard", "Consider the following products:",
  "निम्नलिखित उत्पादों पर विचार कीजिए:",
  ["Channapatna toys", "Bidriware", "Mysore silk", "Kasuti embroidery", "Pochampally ikat"],
  ["चन्नपटना खिलौने", "बिदरी कारीगरी", "मैसूर सिल्क", "कसूती कढ़ाई", "पोचमपल्ली इकत"],
  None, 2,
  "Four of them hold a Geographical Indication registered for Karnataka. Channapatna's lacquered wooden toys are made near Bengaluru; Bidriware, from Bidar, inlays silver into a blackened alloy of zinc and copper; Mysore silk, woven with pure silk and gold zari, comes from the Mysore region; and Kasuti is a fine counted-thread embroidery of north Karnataka, often worked on Ilkal sarees. "
  "Pochampally ikat holds a GI for Telangana. A GI tag protects a product whose quality or reputation comes from its place of origin.",
  "इनमें से चार के पास कर्नाटक के लिए पंजीकृत भौगोलिक संकेतक है। चन्नपटना के लाखदार लकड़ी के खिलौने बेंगलुरु के पास बनते हैं; बीदर की बिदरी कारीगरी जस्ते और ताँबे की काली की गई मिश्रधातु में चाँदी जड़ती है; शुद्ध रेशम और सुनहरी ज़री से बुना मैसूर सिल्क मैसूर क्षेत्र का है; और कसूती उत्तर कर्नाटक की धागे गिनकर की जाने वाली बारीक कढ़ाई है, जो प्रायः इलकल साड़ियों पर होती है। "
  "पोचमपल्ली इकत के पास तेलंगाना का भौगोलिक संकेतक है। भौगोलिक संकेतक उस उत्पाद की रक्षा करता है जिसकी गुणवत्ता या प्रतिष्ठा उसके उद्गम-स्थान से आती है।",
  NLH, "culture-gi-crafts", opts=FIVE, opts_hi=FIVE_HI,
  closing="How many of the above have a GI tag registered for Karnataka?", closing_hi="उपर्युक्त में से कितनों के पास कर्नाटक के लिए पंजीकृत GI टैग है?", craft="multi")

S(CUL, "medium", "Consider the following:",
  "निम्नलिखित पर विचार कीजिए:",
  ["Garba of Gujarat", "Durga Puja in Kolkata", "Yoga", "Kumbh Mela", "Kathakali"],
  ["गुजरात का गरबा", "कोलकाता की दुर्गा पूजा", "योग", "कुंभ मेला", "कथकली"],
  None, 2,
  "Four of them are on UNESCO's Representative List of the Intangible Cultural Heritage of Humanity: Garba (2023), Durga Puja in Kolkata (2021), Yoga (2016) and the Kumbh Mela (2017), alongside Vedic chanting, Ramlila, Kutiyattam, Chhau, Kalbelia and others. "
  "Kathakali, though one of the best-known Indian dance-dramas, is not separately inscribed; Kerala's inscription is Kutiyattam, the Sanskrit theatre. Intangible heritage lists living practices; monuments and sites go on the separate World Heritage List.",
  "इनमें से चार यूनेस्को की मानवता की अमूर्त सांस्कृतिक धरोहर की प्रतिनिधि सूची में हैं: गरबा (2023), कोलकाता की दुर्गा पूजा (2021), योग (2016) और कुंभ मेला (2017), वैदिक मंत्रोच्चार, रामलीला, कूडियाट्टम, छऊ, कालबेलिया और अन्य के साथ। "
  "कथकली, यद्यपि भारत की सबसे प्रसिद्ध नृत्य-नाटिकाओं में से है, अलग से शामिल नहीं है; केरल का अंकन संस्कृत रंगमंच कूडियाट्टम है। अमूर्त धरोहर सूची जीवित परंपराओं की है; स्मारक और स्थल अलग विश्व धरोहर सूची में जाते हैं।",
  MOC, "culture-unesco-ich-garba-durga-puja", opts=FIVE, opts_hi=FIVE_HI,
  closing="How many of the above are on UNESCO's Representative List of the Intangible Cultural Heritage of Humanity?",
  closing_hi="उपर्युक्त में से कितने यूनेस्को की मानवता की अमूर्त सांस्कृतिक धरोहर की प्रतिनिधि सूची में हैं?", craft="multi")

if __name__ == "__main__":
    write_updates("upg_l2_t08_art_a.sql", statuses=("draft", "published"))
