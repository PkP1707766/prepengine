# -*- coding: utf-8 -*-
"""Level 2 · Test 13 (Geography 2: Indian Physical Geography) -- Indian Rivers, Lakes & Wetlands:
45 new bilingual rows against the live gap report: medium statement 13, medium MCQ 7, easy statement 5,
hard statement 5, medium Statement-I/II 5, easy MCQ 2, hard MCQ 2, hard Statement-I/II 1 + I/II/III 1,
medium pairs 2, easy Statement-I/II 1, hard pairs 1.
The bank already tests the Narmada and Tapi rift valleys, the Mahanadi's source and delta and the
Godavari's mouth, so those facts are left alone. Ramsar sites, Loktak's phumdis, Chilika's dolphins
and the Sundarbans sit in the Environment tests; water-dispute tribunals in Polity Test 4; national
waterways in Test 14. The physiography rows of this test say the Peninsula tilts east, so nothing
here states which sea most peninsular rivers reach, and the Kaveri's two-monsoon regime is left out
because it would point to the Coromandel-rainfall row."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Geography"
RV = "Indian Rivers, Lakes & Wetlands"
NC11I = "NCERT Class XI, India: Physical Environment"
NC9 = "NCERT Class IX, Contemporary India I"
JS = "Ministry of Jal Shakti"

# ================================================================ MEDIUM STATEMENTS (13)
S(RV, "medium", "Consider the following statements about the Indus river system:",
  "सिंधु नदी तंत्र के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Indus rises in Tibet near Lake Mansarovar.",
   "The Chenab is formed by the union of the Chandra and the Bhaga.",
   "The Jhelum joins the Indus directly in Ladakh."],
  ["सिंधु तिब्बत में मानसरोवर झील के पास से निकलती है।",
   "चिनाब चंद्रा और भागा के मिलन से बनती है।",
   "झेलम लद्दाख में सीधे सिंधु से मिल जाती है।"],
  C3, 1,
  "Statements 1 and 2 are correct. The Indus rises near Bokhar Chu in the Kailash range of Tibet and flows north-west through Ladakh between the Ladakh and Zaskar ranges. The Chandra and the Bhaga meet at Tandi near Keylong in Himachal Pradesh to form the Chenab. "
  "Statement 3 is wrong: the Jhelum rises at Verinag, flows through the Kashmir valley and Wular Lake into Pakistan, and joins the Chenab near Jhang; the combined Punjab rivers reach the Indus as the Panjnad, above Mithankot.",
  "कथन 1 और 2 सही हैं। सिंधु तिब्बत की कैलाश श्रेणी में बोखर चू के पास से निकलती है और लद्दाख में लद्दाख तथा ज़ास्कर श्रेणियों के बीच उत्तर-पश्चिम की ओर बहती है। हिमाचल प्रदेश में केलांग के पास तांडी में चंद्रा और भागा मिलकर चिनाब बनाती हैं। "
  "कथन 3 गलत है: झेलम वेरीनाग से निकलकर कश्मीर घाटी और वुलर झील से होते हुए पाकिस्तान जाती है और झंग के पास चिनाब से मिलती है; पंजाब की सभी नदियाँ मिलकर पंचनद के रूप में मिठनकोट के ऊपर सिंधु से मिलती हैं।",
  f"{NC11I} -- Drainage System.",
  "irv-indus-system-chenab-jhelum")

S(RV, "medium", "Consider the following statements about the Indus Waters Treaty, 1960:",
  "सिंधु जल संधि, 1960 के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It allocated the waters of the Ravi, the Beas and the Satluj to India.",
   "It was brokered by the World Bank.",
   "India placed the treaty in abeyance in April 2025.",
   "Under the treaty, India could not use the western rivers for any purpose at all."],
  ["इसने रावी, ब्यास और सतलुज का जल भारत को आवंटित किया।",
   "इसमें विश्व बैंक ने मध्यस्थता की थी।",
   "भारत ने अप्रैल 2025 में इस संधि को स्थगित (in abeyance) कर दिया।",
   "संधि के तहत भारत पश्चिमी नदियों का किसी भी प्रयोजन के लिए कोई उपयोग नहीं कर सकता था।"],
  C4, 2,
  "Statements 1, 2 and 3 are correct. The treaty, signed at Karachi in 1960 with the World Bank as broker and a signatory, gave the eastern rivers to India and the western rivers -- the Indus, the Jhelum and the Chenab -- mainly to Pakistan. After the terrorist attack at Pahalgam, India announced on 23 April 2025 that it was holding the treaty in abeyance. "
  "Statement 4 is wrong: India was allowed limited use of the western rivers -- for domestic and non-consumptive uses, some irrigation, and run-of-the-river hydropower such as the Kishanganga and Ratle projects, within design limits.",
  "कथन 1, 2 और 3 सही हैं। 1960 में कराची में हस्ताक्षरित इस संधि में विश्व बैंक मध्यस्थ और एक हस्ताक्षरकर्ता था; इसने पूर्वी नदियाँ भारत को और पश्चिमी नदियाँ, यानी सिंधु, झेलम और चिनाब, मुख्य रूप से पाकिस्तान को दीं। पहलगाम के आतंकी हमले के बाद भारत ने 23 अप्रैल 2025 को घोषणा की कि वह संधि को स्थगित रख रहा है। "
  "कथन 4 गलत है: भारत को पश्चिमी नदियों के सीमित उपयोग की अनुमति थी, जैसे घरेलू और गैर-उपभोगी उपयोग, कुछ सिंचाई, और डिज़ाइन सीमाओं के भीतर किशनगंगा और रतले जैसी नदी-प्रवाह (run-of-the-river) जलविद्युत परियोजनाएँ।",
  f"Ministry of External Affairs -- Indus Waters Treaty; {JS}.",
  "irv-indus-waters-treaty")

S(RV, "medium", "Consider the following statements about the headstreams of the Ganga:",
  "गंगा की शीर्ष धाराओं के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Bhagirathi and the Alaknanda meet at Devprayag to form the Ganga.",
   "The Mandakini joins the Alaknanda at Rudraprayag.",
   "The Pindar joins the Alaknanda at Karnaprayag."],
  ["भागीरथी और अलकनंदा देवप्रयाग में मिलकर गंगा बनाती हैं।",
   "मंदाकिनी रुद्रप्रयाग में अलकनंदा से मिलती है।",
   "पिंडर कर्णप्रयाग में अलकनंदा से मिलती है।"],
  C3, 2,
  "All three statements are correct. Going down the Alaknanda, the five prayags (confluences) are Vishnuprayag (with the Dhauliganga), Nandprayag (Nandakini), Karnaprayag (Pindar), Rudraprayag (Mandakini) and finally Devprayag, where the Alaknanda meets the Bhagirathi and the river takes the name Ganga.",
  "तीनों कथन सही हैं। अलकनंदा के साथ नीचे की ओर पाँच प्रयाग (संगम) हैं: विष्णुप्रयाग (धौलीगंगा के साथ), नंदप्रयाग (नंदाकिनी), कर्णप्रयाग (पिंडर), रुद्रप्रयाग (मंदाकिनी) और अंत में देवप्रयाग, जहाँ अलकनंदा भागीरथी से मिलती है और नदी गंगा कहलाती है।",
  f"{NC11I} -- Drainage System.",
  "irv-ganga-panch-prayag")

S(RV, "medium", "Consider the following statements about the tributaries of the Ganga:",
  "गंगा की सहायक नदियों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Kosi has shifted its course westwards by more than 100 km over the last two centuries.",
   "The Gomti is a Himalayan river fed by glaciers.",
   "The Ghaghara joins the Ganga upstream of Prayagraj."],
  ["पिछली दो शताब्दियों में कोसी ने अपना मार्ग 100 किमी से अधिक पश्चिम की ओर खिसकाया है।",
   "गोमती हिमनदों से पोषित एक हिमालयी नदी है।",
   "घाघरा प्रयागराज से ऊपर (प्रतिप्रवाह में) गंगा से मिलती है।"],
  C3, 0,
  "Only statement 1 is correct: the Kosi brings down huge amounts of sediment from Nepal and Tibet, raises its own bed and repeatedly breaks out into new channels -- the reason for its floods in north Bihar. "
  "Statement 2 is wrong: the Gomti rises in the plains, near Pilibhit in Uttar Pradesh, and is fed by rain and groundwater. "
  "Statement 3 is wrong: the Ghaghara joins the Ganga in Bihar, near Chhapra, far downstream of Prayagraj.",
  "केवल कथन 1 सही है: कोसी नेपाल और तिब्बत से भारी मात्रा में अवसाद लाती है, अपना तल ऊँचा कर लेती है और बार-बार नए मार्गों में फूट पड़ती है; यही उत्तर बिहार में उसकी बाढ़ों का कारण है। "
  "कथन 2 गलत है: गोमती उत्तर प्रदेश में पीलीभीत के पास मैदानों से निकलती है और वर्षा तथा भूजल से पोषित होती है। "
  "कथन 3 गलत है: घाघरा बिहार में छपरा के पास, प्रयागराज से बहुत नीचे, गंगा से मिलती है।",
  f"{NC11I} -- Drainage System.",
  "irv-ganga-tributaries-kosi-gomti-ghaghara")

S(RV, "medium", "Consider the following statements about rivers of central India:",
  "मध्य भारत की नदियों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Chambal rises in the Aravallis.",
   "The Son rises in the Chotanagpur plateau.",
   "The Son is a tributary of the Yamuna."],
  ["चंबल अरावली से निकलती है।",
   "सोन छोटानागपुर पठार से निकलती है।",
   "सोन यमुना की सहायक नदी है।"],
  C3, 3,
  "None of the statements is correct. "
  "Statement 1 is wrong: the Chambal rises at Janapav near Mhow in the Vindhyan range of the Malwa plateau, and flows north-east through a region of deep ravines into the Yamuna. "
  "Statements 2 and 3 are wrong: the Son rises near Amarkantak in Madhya Pradesh and flows north and then east to join the Ganga itself, near Patna.",
  "कोई भी कथन सही नहीं है। "
  "कथन 1 गलत है: चंबल मालवा पठार की विंध्य श्रेणी में महू के पास जानापाव से निकलती है और गहरे बीहड़ों वाले क्षेत्र से होकर उत्तर-पूर्व की ओर बहते हुए यमुना में मिलती है। "
  "कथन 2 और 3 गलत हैं: सोन मध्य प्रदेश में अमरकंटक के पास से निकलती है और उत्तर तथा फिर पूर्व की ओर बहकर पटना के पास सीधे गंगा से मिलती है।",
  f"{NC11I} -- Drainage System.",
  "irv-chambal-son-origins")

S(RV, "medium", "Consider the following statements about the Brahmaputra:",
  "ब्रह्मपुत्र के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It flows westwards through the Assam valley.",
   "In Bangladesh it is known as the Jamuna.",
   "Majuli, a large island in the river, lies in Arunachal Pradesh."],
  ["यह असम घाटी में पश्चिम की ओर बहती है।",
   "बांग्लादेश में इसे जमुना के नाम से जाना जाता है।",
   "इस नदी का बड़ा द्वीप माजुली अरुणाचल प्रदेश में है।"],
  C3, 1,
  "Statements 1 and 2 are correct. After entering the Assam valley near Sadiya, the Brahmaputra flows west for about 700 km, then turns south into Bangladesh as the Jamuna and joins the Padma (Ganga). "
  "Statement 3 is wrong: Majuli, one of the largest river islands in the world and a centre of Vaishnava satras, lies in Assam and was made a separate district in 2016.",
  "कथन 1 और 2 सही हैं। सदिया के पास असम घाटी में प्रवेश करने के बाद ब्रह्मपुत्र लगभग 700 किमी पश्चिम की ओर बहती है, फिर दक्षिण की ओर मुड़कर जमुना के रूप में बांग्लादेश जाती है और पद्मा (गंगा) से मिलती है। "
  "कथन 3 गलत है: विश्व के सबसे बड़े नदी द्वीपों में से एक और वैष्णव सत्रों का केंद्र माजुली असम में है, और 2016 में इसे एक अलग ज़िला बनाया गया।",
  f"{NC11I} -- Drainage System.",
  "irv-brahmaputra-assam-jamuna-majuli")

S(RV, "medium", "Consider the following statements about the Godavari:",
  "गोदावरी के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It rises at Trimbakeshwar near Nashik.",
   "It has the largest basin among the rivers of the Peninsula.",
   "The Indravati is one of its tributaries."],
  ["यह नासिक के पास त्र्यंबकेश्वर से निकलती है।",
   "प्रायद्वीप की नदियों में इसका बेसिन सबसे बड़ा है।",
   "इंद्रावती इसकी सहायक नदियों में से एक है।"],
  C3, 2,
  "All three statements are correct. The Godavari rises in the Western Ghats at Trimbakeshwar and drains parts of Maharashtra, Telangana, Chhattisgarh, Odisha and Andhra Pradesh -- about a tenth of India's area, the largest peninsular basin. Its tributaries include the Pranhita (formed by the Wainganga and the Wardha), the Indravati from Chhattisgarh, the Manjra and the Sabari.",
  "तीनों कथन सही हैं। गोदावरी पश्चिमी घाट में त्र्यंबकेश्वर से निकलती है और महाराष्ट्र, तेलंगाना, छत्तीसगढ़, ओडिशा और आंध्र प्रदेश के भागों का जल बहाती है; यह भारत के क्षेत्रफल का लगभग दसवाँ भाग है और सबसे बड़ा प्रायद्वीपीय बेसिन है। इसकी सहायक नदियों में प्राणहिता (वैनगंगा और वर्धा से बनी), छत्तीसगढ़ से आने वाली इंद्रावती, मांजरा और सबरी हैं।",
  f"{NC11I} -- Drainage System.",
  "irv-godavari-source-basin")

S(RV, "medium", "Consider the following statements about the Krishna:",
  "कृष्णा के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It rises near Mahabaleshwar in the Western Ghats.",
   "The Tungabhadra is a tributary of the Kaveri.",
   "The Krishna delta lies in Tamil Nadu."],
  ["यह पश्चिमी घाट में महाबलेश्वर के पास से निकलती है।",
   "तुंगभद्रा कावेरी की सहायक नदी है।",
   "कृष्णा का डेल्टा तमिलनाडु में है।"],
  C3, 0,
  "Only statement 1 is correct. "
  "Statement 2 is wrong: the Tungabhadra, formed by the Tunga and the Bhadra in Karnataka and flowing past Hampi, is a tributary of the Krishna, which it joins near Kurnool; the Koyna, the Bhima and the Ghataprabha are other Krishna tributaries. "
  "Statement 3 is wrong: the Krishna forms its delta in Andhra Pradesh, below Vijayawada, before entering the Bay of Bengal.",
  "केवल कथन 1 सही है। "
  "कथन 2 गलत है: कर्नाटक में तुंगा और भद्रा से बनी और हम्पी के पास से बहने वाली तुंगभद्रा कृष्णा की सहायक नदी है, जो कुरनूल के पास उससे मिलती है; कोयना, भीमा और घटप्रभा कृष्णा की अन्य सहायक नदियाँ हैं। "
  "कथन 3 गलत है: कृष्णा बंगाल की खाड़ी में गिरने से पहले आंध्र प्रदेश में, विजयवाड़ा के नीचे, अपना डेल्टा बनाती है।",
  f"{NC11I} -- Drainage System.",
  "irv-krishna-source-tungabhadra-delta")

S(RV, "medium", "Consider the following statements about the Kaveri:",
  "कावेरी के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It rises at Talakaveri in the Brahmagiri hills of Kodagu.",
   "The Kabini is one of its tributaries.",
   "The Shivasamudram falls on the Kaveri lie in Tamil Nadu."],
  ["यह कोडगु की ब्रह्मगिरि पहाड़ियों में तलकावेरी से निकलती है।",
   "काबिनी इसकी सहायक नदियों में से एक है।",
   "कावेरी पर स्थित शिवसमुद्रम जलप्रपात तमिलनाडु में है।"],
  C3, 1,
  "Statements 1 and 2 are correct: the Kaveri rises at Talakaveri in Karnataka's Kodagu district, and its tributaries include the Kabini, the Hemavati, the Bhavani and the Amaravati. "
  "Statement 3 is wrong: the Shivasamudram falls, where one of India's first hydroelectric power stations was built in 1902, are in Karnataka; the Kaveri enters Tamil Nadu further downstream, at Hogenakkal.",
  "कथन 1 और 2 सही हैं: कावेरी कर्नाटक के कोडगु ज़िले में तलकावेरी से निकलती है, और इसकी सहायक नदियों में काबिनी, हेमावती, भवानी और अमरावती हैं। "
  "कथन 3 गलत है: शिवसमुद्रम जलप्रपात, जहाँ 1902 में भारत के पहले जलविद्युत केंद्रों में से एक बना, कर्नाटक में है; कावेरी और नीचे, होगेनक्कल पर, तमिलनाडु में प्रवेश करती है।",
  f"{NC11I} -- Drainage System.",
  "irv-kaveri-source-kabini-shivasamudram")

S(RV, "medium", "Consider the following statements about some west-flowing rivers:",
  "पश्चिम की ओर बहने वाली कुछ नदियों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Sabarmati rises in the Aravallis.",
   "The Sabarmati flows into the Gulf of Kachchh.",
   "The Periyar is the longest river of Kerala."],
  ["साबरमती अरावली से निकलती है।",
   "साबरमती कच्छ की खाड़ी में गिरती है।",
   "पेरियार केरल की सबसे लंबी नदी है।"],
  C3, 1,
  "Statements 1 and 3 are correct: the Sabarmati rises in the Aravallis near Udaipur in Rajasthan, and the Periyar, which feeds the Idukki reservoir, is Kerala's longest river. "
  "Statement 2 is wrong: the Sabarmati flows past Ahmedabad and Gandhinagar into the Gulf of Khambhat.",
  "कथन 1 और 3 सही हैं: साबरमती राजस्थान में उदयपुर के पास अरावली से निकलती है, और इडुक्की जलाशय को जल देने वाली पेरियार केरल की सबसे लंबी नदी है। "
  "कथन 2 गलत है: साबरमती अहमदाबाद और गांधीनगर के पास से बहते हुए खंभात की खाड़ी में गिरती है।",
  f"{NC11I} -- Drainage System.",
  "irv-west-flowing-sabarmati-periyar")

S(RV, "medium", "Consider the following statements about lakes of India:",
  "भारत की झीलों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Wular is the largest freshwater lake in India.",
   "Sambhar is India's largest inland saline lake.",
   "Pulicat lake lies on the Andhra Pradesh-Tamil Nadu border, and Sriharikota island separates it from the sea."],
  ["वुलर भारत की सबसे बड़ी मीठे जल की झील है।",
   "सांभर भारत की सबसे बड़ी अंतर्देशीय लवणीय झील है।",
   "पुलिकट झील आंध्र प्रदेश-तमिलनाडु सीमा पर है, और श्रीहरिकोटा द्वीप उसे समुद्र से अलग करता है।"],
  C3, 2,
  "All three statements are correct. Wular, in Jammu and Kashmir, is fed and drained by the Jhelum and acts as a natural flood reservoir; Sambhar, west of Jaipur, is a major source of salt; and Pulicat, the second-largest brackish lagoon in India, is separated from the Bay of Bengal by the barrier island of Sriharikota, where ISRO's launch centre stands.",
  "तीनों कथन सही हैं। जम्मू-कश्मीर की वुलर झील में झेलम का जल आता-जाता है और यह बाढ़ के प्राकृतिक जलाशय का काम करती है; जयपुर के पश्चिम में स्थित सांभर नमक का बड़ा स्रोत है; और भारत का दूसरा सबसे बड़ा खारे जल का लैगून पुलिकट, श्रीहरिकोटा अवरोधक द्वीप से बंगाल की खाड़ी से अलग होता है, जहाँ इसरो का प्रक्षेपण केंद्र है।",
  f"{NC11I} -- Drainage System; {NC9} -- Drainage.",
  "irv-lakes-wular-sambhar-pulicat")

S(RV, "medium", "Consider the following statements about lakes of India:",
  "भारत की झीलों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Vembanad is the longest lake in India.",
   "Lonar lake in Maharashtra was formed by a volcanic eruption.",
   "Loktak lake lies in Mizoram."],
  ["वेम्बनाड भारत की सबसे लंबी झील है।",
   "महाराष्ट्र की लोणार झील एक ज्वालामुखी उद्गार से बनी।",
   "लोकटक झील मिज़ोरम में है।"],
  C3, 0,
  "Only statement 1 is correct: Vembanad, stretching about 96 km through the backwaters of Kerala from Alappuzha to Kochi, is the longest lake in India. "
  "Statement 2 is wrong: Lonar, a saline and alkaline lake in Buldhana district, fills a crater made by a meteorite that struck the basalt of the Deccan trap -- 'volcanic' is the trap, since the rock itself is volcanic. "
  "Statement 3 is wrong: Loktak, the largest freshwater lake in the north-east, is in Manipur.",
  "केवल कथन 1 सही है: अलप्पुझा से कोच्चि तक केरल के पश्चजल में लगभग 96 किमी तक फैली वेम्बनाड भारत की सबसे लंबी झील है। "
  "कथन 2 गलत है: बुलढाणा ज़िले की लवणीय और क्षारीय लोणार झील उस गड्ढे (क्रेटर) में है जो दक्कन ट्रैप के बेसाल्ट से टकराए एक उल्कापिंड से बना; 'ज्वालामुखी' ही जाल है, क्योंकि वहाँ की चट्टान स्वयं ज्वालामुखीय है। "
  "कथन 3 गलत है: पूर्वोत्तर की सबसे बड़ी मीठे जल की झील लोकटक मणिपुर में है।",
  f"{NC9} -- Drainage; Geological Survey of India -- Lonar Crater.",
  "irv-lakes-vembanad-lonar-loktak")

S(RV, "medium", "Consider the following statements about river projects:",
  "नदी परियोजनाओं के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Ken-Betwa link is the first project under the National Perspective Plan for interlinking rivers to be taken up for implementation.",
   "The Farakka Barrage diverts water from the Ganga into the Hooghly.",
   "The Ken-Betwa link will transfer water from the Betwa basin to the Ken basin."],
  ["केन-बेतवा लिंक नदियों को जोड़ने की राष्ट्रीय परिप्रेक्ष्य योजना के तहत कार्यान्वयन के लिए लिया गया पहला प्रोजेक्ट है।",
   "फ़रक्का बैराज गंगा का जल हुगली में मोड़ता है।",
   "केन-बेतवा लिंक बेतवा बेसिन से केन बेसिन में जल ले जाएगा।"],
  C3, 1,
  "Statements 1 and 2 are correct. The Ken-Betwa project, whose foundation stone was laid in December 2024, will build the Daudhan dam on the Ken in Panna district and carry its surplus water through a canal to the Betwa basin, for Bundelkhand in Madhya Pradesh and Uttar Pradesh. The Farakka Barrage, completed in 1975, sends Ganga water down a feeder canal into the Bhagirathi-Hooghly to flush silt and keep Kolkata port navigable. "
  "Statement 3 is wrong: the transfer is from the Ken to the Betwa, not the other way round.",
  "कथन 1 और 2 सही हैं। केन-बेतवा परियोजना, जिसकी आधारशिला दिसंबर 2024 में रखी गई, पन्ना ज़िले में केन पर दौधन बाँध बनाएगी और इसके अतिरिक्त जल को एक नहर से बेतवा बेसिन तक ले जाएगी, जिससे मध्य प्रदेश और उत्तर प्रदेश के बुंदेलखंड को लाभ होगा। 1975 में पूरा हुआ फ़रक्का बैराज गंगा के जल को एक पोषक नहर से भागीरथी-हुगली में भेजता है, ताकि गाद बह जाए और कोलकाता बंदरगाह नौगम्य बना रहे। "
  "कथन 3 गलत है: जल केन से बेतवा में जाएगा, इसके उलट नहीं।",
  f"{JS} -- National Water Development Agency, Ken-Betwa Link Project.",
  "irv-ken-betwa-farakka")

# ================================================================ HARD STATEMENTS (5)
S(RV, "hard", "Consider the following statements comparing Himalayan and Peninsular rivers:",
  "हिमालयी और प्रायद्वीपीय नदियों की तुलना करने वाले निम्नलिखित कथनों पर विचार कीजिए:",
  ["Several Himalayan rivers, such as the Indus and the Brahmaputra, are antecedent rivers that cut deep gorges across the rising mountains.",
   "Most Peninsular rivers flow in broad, shallow valleys and have almost reached their graded profiles.",
   "Most Peninsular rivers flow through rift valleys."],
  ["सिंधु और ब्रह्मपुत्र जैसी कई हिमालयी नदियाँ पूर्ववर्ती (antecedent) नदियाँ हैं, जिन्होंने उठते पर्वतों के आर-पार गहरे गॉर्ज काटे।",
   "अधिकांश प्रायद्वीपीय नदियाँ चौड़ी, उथली घाटियों में बहती हैं और लगभग अपनी प्रवणित परिच्छेदिका (graded profile) तक पहुँच चुकी हैं।",
   "अधिकांश प्रायद्वीपीय नदियाँ भ्रंश घाटियों से होकर बहती हैं।"],
  C3, 1,
  "Statements 1 and 2 are correct. The Indus, the Satluj and the Brahmaputra are older than the Himalaya: they kept cutting down as the mountains rose, carving gorges thousands of metres deep. The Peninsular rivers are much older, flowing over a stable, worn-down plateau with fixed courses and few meanders. "
  "Statement 3 is wrong: only a few Peninsular rivers, such as the Narmada, the Tapi and the Damodar, follow rift valleys; most flow in ordinary erosional valleys.",
  "कथन 1 और 2 सही हैं। सिंधु, सतलुज और ब्रह्मपुत्र हिमालय से पुरानी हैं: पर्वतों के उठने के साथ-साथ वे नीचे कटाव करती रहीं और हज़ारों मीटर गहरे गॉर्ज बना दिए। प्रायद्वीपीय नदियाँ कहीं अधिक पुरानी हैं, जो स्थिर, घिसे हुए पठार पर निश्चित मार्गों में और बहुत कम विसर्पों के साथ बहती हैं। "
  "कथन 3 गलत है: केवल कुछ प्रायद्वीपीय नदियाँ, जैसे नर्मदा, तापी और दामोदर, भ्रंश घाटियों में बहती हैं; अधिकांश साधारण अपरदन घाटियों में बहती हैं।",
  f"{NC11I} -- Drainage System.",
  "irv-himalayan-vs-peninsular-rivers")

S(RV, "hard", "Consider the following statements about the Brahmaputra system:",
  "ब्रह्मपुत्र तंत्र के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Dibang and the Lohit join the Brahmaputra near Sadiya in Assam.",
   "The Subansiri and the Manas join the Brahmaputra from its north bank.",
   "The Teesta joins the Brahmaputra in Assam."],
  ["दिबांग और लोहित असम में सदिया के पास ब्रह्मपुत्र से मिलती हैं।",
   "सुबनसिरी और मानस उत्तरी किनारे से ब्रह्मपुत्र में मिलती हैं।",
   "तीस्ता असम में ब्रह्मपुत्र से मिलती है।"],
  C3, 1,
  "Statements 1 and 2 are correct. Near Sadiya, the Siang (Dihang), coming down from Tibet through Arunachal Pradesh, is joined by the Dibang and the Lohit, and the river becomes the Brahmaputra. Its north-bank tributaries -- the Subansiri, the Kameng, the Manas and the Sankosh -- come from the Himalaya and carry heavy loads of silt; the south-bank tributaries, such as the Dhansiri and the Kopili, are gentler. "
  "Statement 3 is wrong: the Teesta, rising in Sikkim, flows through north Bengal and joins the Brahmaputra (Jamuna) in Bangladesh.",
  "कथन 1 और 2 सही हैं। सदिया के पास तिब्बत से अरुणाचल प्रदेश होते हुए आने वाली सियांग (दिहांग) में दिबांग और लोहित मिलती हैं, और नदी ब्रह्मपुत्र बन जाती है। इसकी उत्तरी किनारे की सहायक नदियाँ, यानी सुबनसिरी, कामेंग, मानस और संकोश, हिमालय से आती हैं और भारी मात्रा में गाद लाती हैं; दक्षिणी किनारे की सहायक नदियाँ, जैसे धनसिरी और कोपिली, अपेक्षाकृत शांत हैं। "
  "कथन 3 गलत है: सिक्किम से निकलने वाली तीस्ता उत्तर बंगाल से होकर बांग्लादेश में ब्रह्मपुत्र (जमुना) से मिलती है।",
  f"{NC11I} -- Drainage System.",
  "irv-brahmaputra-tributaries")

S(RV, "hard", "Consider the following statements about the sources of peninsular rivers:",
  "प्रायद्वीपीय नदियों के उद्गम के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Tapi rises near Multai in Madhya Pradesh.",
   "The Pennar rises in Karnataka.",
   "The Brahmani is formed by the union of the Sankh and the South Koel.",
   "The Subarnarekha rises in Chhattisgarh."],
  ["तापी मध्य प्रदेश में मुलताई के पास से निकलती है।",
   "पेन्नार कर्नाटक से निकलती है।",
   "ब्राह्मणी शंख और दक्षिण कोयल के मिलन से बनती है।",
   "सुवर्णरेखा छत्तीसगढ़ से निकलती है।"],
  C4, 2,
  "Statements 1, 2 and 3 are correct. The Tapi rises in the Satpura range at Multai in Betul district; the Pennar rises in the Nandi hills of Chikkaballapur district and flows through Andhra Pradesh to the Bay of Bengal; and the Sankh and the South Koel meet at Vedvyas near Rourkela to form the Brahmani. "
  "Statement 4 is wrong: the Subarnarekha rises on the Chotanagpur plateau near Ranchi in Jharkhand and flows through West Bengal and Odisha to the sea.",
  "कथन 1, 2 और 3 सही हैं। तापी बैतूल ज़िले में मुलताई पर सतपुड़ा श्रेणी से निकलती है; पेन्नार चिक्कबल्लापुर ज़िले की नंदी पहाड़ियों से निकलकर आंध्र प्रदेश से होते हुए बंगाल की खाड़ी में गिरती है; और राउरकेला के पास वेदव्यास में शंख और दक्षिण कोयल मिलकर ब्राह्मणी बनाती हैं। "
  "कथन 4 गलत है: सुवर्णरेखा झारखंड में राँची के पास छोटानागपुर पठार से निकलकर पश्चिम बंगाल और ओडिशा से होते हुए समुद्र में गिरती है।",
  f"{NC11I} -- Drainage System.",
  "irv-peninsular-river-sources")

S(RV, "hard", "Consider the following statements about the Ganga basin:",
  "गंगा बेसिन के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Ganga basin is the largest river basin in India.",
   "The Ramganga rises in the Garhwal hills.",
   "The Ganga enters the plains at Haridwar."],
  ["गंगा बेसिन भारत का सबसे बड़ा नदी बेसिन है।",
   "रामगंगा गढ़वाल की पहाड़ियों से निकलती है।",
   "गंगा हरिद्वार में मैदानों में प्रवेश करती है।"],
  C3, 2,
  "All three statements are correct. The Ganga basin covers more than a quarter of India's area, spread over eleven States. The Ramganga rises near Gairsain in the Garhwal hills and joins the Ganga near Kannauj, and the Ganga leaves the Shiwaliks and enters the plains at Haridwar.",
  "तीनों कथन सही हैं। गंगा बेसिन भारत के एक-चौथाई से अधिक क्षेत्रफल में, ग्यारह राज्यों में फैला है। रामगंगा गढ़वाल की पहाड़ियों में गैरसैंण के पास से निकलकर कन्नौज के पास गंगा से मिलती है, और गंगा शिवालिक को छोड़कर हरिद्वार में मैदानों में प्रवेश करती है।",
  f"{NC11I} -- Drainage System.",
  "irv-ganga-basin-ramganga-haridwar")

S(RV, "hard", "Consider the following statements about dams in India:",
  "भारत के बाँधों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Tehri dam is on the Bhagirathi.",
   "The Bhakra dam is on the Beas.",
   "The Nagarjuna Sagar dam is on the Godavari."],
  ["टिहरी बाँध भागीरथी पर है।",
   "भाखड़ा बाँध ब्यास पर है।",
   "नागार्जुन सागर बाँध गोदावरी पर है।"],
  C3, 0,
  "Only statement 1 is correct: the Tehri dam, one of the tallest in India, stands on the Bhagirathi in Uttarakhand. "
  "Statement 2 is wrong: the Bhakra dam is on the Satluj in Himachal Pradesh, holding back the Gobind Sagar; the Pong dam is the one on the Beas. "
  "Statement 3 is wrong: the Nagarjuna Sagar dam is on the Krishna, on the Telangana-Andhra Pradesh border.",
  "केवल कथन 1 सही है: भारत के सबसे ऊँचे बाँधों में से एक, टिहरी बाँध, उत्तराखंड में भागीरथी पर है। "
  "कथन 2 गलत है: भाखड़ा बाँध हिमाचल प्रदेश में सतलुज पर है, जिससे गोविंद सागर बना है; ब्यास पर पोंग बाँध है। "
  "कथन 3 गलत है: नागार्जुन सागर बाँध तेलंगाना-आंध्र प्रदेश सीमा पर कृष्णा पर है।",
  f"{JS} -- Central Water Commission, National Register of Large Dams.",
  "irv-dams-tehri-bhakra-nagarjuna")

# ================================================================ EASY STATEMENTS (5)
S(RV, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["A river basin is the area drained by a river and its tributaries.",
   "The boundary that separates two river basins is called a delta."],
  ["नदी बेसिन वह क्षेत्र है जिसका जल कोई नदी और उसकी सहायक नदियाँ बहाकर ले जाती हैं।",
   "दो नदी बेसिनों को अलग करने वाली सीमा को डेल्टा कहते हैं।"],
  T2, 0,
  "Only statement 1 is correct. Statement 2 is wrong: the high ground separating two river basins is a water divide (watershed); a delta is the low, fan-shaped plain a river builds at its mouth.",
  "केवल कथन 1 सही है। कथन 2 गलत है: दो नदी बेसिनों को अलग करने वाली ऊँची भूमि जल-विभाजक (water divide) कहलाती है; डेल्टा वह निचला, पंखे जैसा मैदान है जो नदी अपने मुहाने पर बनाती है।",
  f"{NC9} -- Drainage.",
  "irv-basin-water-divide-easy")

S(RV, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Sambhar lake lies in Rajasthan.",
   "Vembanad lake lies in Kerala."],
  ["सांभर झील राजस्थान में है।",
   "वेम्बनाड झील केरल में है।"],
  T2, 2,
  "Both statements are correct. Sambhar is a salt lake near Jaipur; Vembanad, in the backwaters of Kerala, hosts the Nehru Trophy boat race on its Punnamada stretch.",
  "दोनों कथन सही हैं। सांभर जयपुर के पास एक खारी झील है; केरल के पश्चजल में स्थित वेम्बनाड के पुन्नमडा भाग में नेहरू ट्रॉफ़ी नौका दौड़ होती है।",
  f"{NC9} -- Drainage.",
  "irv-sambhar-vembanad-easy")

S(RV, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Chilika lake lies in Odisha.",
   "Wular lake lies in Himachal Pradesh."],
  ["चिल्का झील ओडिशा में है।",
   "वुलर झील हिमाचल प्रदेश में है।"],
  T2, 0,
  "Only statement 1 is correct. Statement 2 is wrong: Wular lies in the Kashmir valley of Jammu and Kashmir, on the course of the Jhelum.",
  "केवल कथन 1 सही है। कथन 2 गलत है: वुलर जम्मू-कश्मीर की कश्मीर घाटी में, झेलम के मार्ग पर है।",
  f"{NC9} -- Drainage.",
  "irv-chilika-wular-easy")

S(RV, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Kaveri flows through Karnataka and Tamil Nadu.",
   "The Satluj flows through Punjab."],
  ["कावेरी कर्नाटक और तमिलनाडु से होकर बहती है।",
   "सतलुज पंजाब से होकर बहती है।"],
  T2, 2,
  "Both statements are correct. The Kaveri rises in Karnataka and reaches the sea through a large delta in Tamil Nadu; the Satluj flows through Himachal Pradesh and Punjab before entering Pakistan.",
  "दोनों कथन सही हैं। कावेरी कर्नाटक से निकलती है और तमिलनाडु में एक बड़े डेल्टा से होकर समुद्र तक पहुँचती है; सतलुज पाकिस्तान में प्रवेश करने से पहले हिमाचल प्रदेश और पंजाब से होकर बहती है।",
  f"{NC9} -- Drainage.",
  "irv-kaveri-satluj-easy")

S(RV, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Ox-bow lakes are formed by glaciers.",
   "Glacial lakes are common in the Thar Desert."],
  ["गोखुर झीलें (ox-bow lakes) हिमनदों से बनती हैं।",
   "थार मरुस्थल में हिमनदी झीलें आम हैं।"],
  T2, 3,
  "Neither statement is correct. Ox-bow lakes form when a river cuts across the neck of a meander and the old loop is left behind, as in the Ganga plains. Glacial lakes, left in hollows scoured by ice or dammed by moraines, are found in the high Himalaya -- in Sikkim, Ladakh and Uttarakhand; the Thar has only shallow salt lakes (playas) such as Sambhar and Didwana.",
  "कोई भी कथन सही नहीं है। गोखुर झीलें तब बनती हैं जब नदी किसी विसर्प की गर्दन को काट देती है और पुराना घुमाव पीछे छूट जाता है, जैसे गंगा के मैदानों में। हिमनदी झीलें, जो बर्फ़ से खुरचे गए गड्ढों में या हिमोढ़ों से रुकने पर बनती हैं, ऊँचे हिमालय में, जैसे सिक्किम, लद्दाख और उत्तराखंड में, पाई जाती हैं; थार में केवल सांभर और डीडवाना जैसी उथली खारी झीलें (प्लाया) हैं।",
  f"{NC9} -- Drainage.",
  "irv-oxbow-glacial-lakes-easy")

# ================================================================ MCQs (medium 7, easy 2, hard 2)
M(RV, "medium", "Which one of the following is the largest tributary of the Indus?",
  "निम्नलिखित में से कौन-सी सिंधु की सबसे बड़ी सहायक नदी है?",
  ["The Chenab", "The Jhelum", "The Satluj", "The Ravi"],
  ["चिनाब", "झेलम", "सतलुज", "रावी"],
  0,
  "The Chenab, formed by the Chandra and the Bhaga in Himachal Pradesh, carries the largest volume of water among the Indus tributaries and flows through Jammu into Pakistan. The Satluj is the longest of the Punjab rivers in India, which is why it tempts; the Jhelum joins the Chenab, not the Indus.",
  "हिमाचल प्रदेश में चंद्रा और भागा से बनी चिनाब सिंधु की सहायक नदियों में सबसे अधिक जल लेकर जम्मू से होते हुए पाकिस्तान जाती है। भारत में पंजाब की नदियों में सतलुज सबसे लंबी है, इसलिए वह आकर्षक लगती है; झेलम सिंधु से नहीं, चिनाब से मिलती है।",
  f"{NC11I} -- Drainage System.",
  "irv-largest-indus-tributary-chenab")

M(RV, "medium", "The Jog Falls are formed by which one of the following rivers?",
  "जोग जलप्रपात निम्नलिखित में से किस नदी से बनता है?",
  ["Sharavathi", "Netravati", "Tungabhadra", "Kali"],
  ["शरावती", "नेत्रावती", "तुंगभद्रा", "काली"],
  0,
  "The Sharavathi plunges about 250 m at Jog in Shivamogga district, Karnataka, in four streams known as Raja, Rani, Rover and Rocket, before flowing west to the Arabian Sea. Its flow is now controlled by the Linganamakki dam upstream.",
  "शरावती कर्नाटक के शिवमोग्गा ज़िले में जोग पर लगभग 250 मीटर नीचे चार धाराओं में गिरती है, जिन्हें राजा, रानी, रोवर और रॉकेट कहते हैं, और फिर पश्चिम की ओर बहकर अरब सागर में मिलती है। अब इसके प्रवाह को ऊपर के लिंगनमक्की बाँध से नियंत्रित किया जाता है।",
  f"{NC9} -- Drainage.",
  "irv-jog-falls-sharavathi")

M(RV, "medium", "Which one of the following is a tributary of the Indus that flows through Ladakh?",
  "निम्नलिखित में से कौन-सी सिंधु की ऐसी सहायक नदी है जो लद्दाख से होकर बहती है?",
  ["Shyok", "Beas", "Sharda", "Gandak"],
  ["श्योक", "ब्यास", "शारदा", "गंडक"],
  0,
  "The Shyok rises from the Rimo glacier of the Karakoram, is joined by the Nubra, and meets the Indus in Gilgit-Baltistan; the Zaskar is another Indus tributary in Ladakh. The Beas belongs to the Indus system too, but it flows through Himachal Pradesh and Punjab; the Sharda and the Gandak are tributaries of the Ganga system.",
  "श्योक काराकोरम के रिमो हिमनद से निकलती है, इसमें नुब्रा मिलती है, और यह गिलगित-बाल्टिस्तान में सिंधु से मिलती है; ज़ास्कर लद्दाख में सिंधु की एक और सहायक नदी है। ब्यास भी सिंधु तंत्र की है, पर वह हिमाचल प्रदेश और पंजाब से बहती है; शारदा और गंडक गंगा तंत्र की सहायक नदियाँ हैं।",
  f"{NC11I} -- Drainage System.",
  "irv-shyok-ladakh")

M(RV, "medium", "Which one of the following rivers was known as the 'Sorrow of Bengal' for its destructive floods?",
  "विनाशकारी बाढ़ों के कारण निम्नलिखित में से कौन-सी नदी 'बंगाल का शोक' कहलाती थी?",
  ["Damodar", "Hooghly", "Teesta", "Rupnarayan"],
  ["दामोदर", "हुगली", "तीस्ता", "रूपनारायण"],
  0,
  "The Damodar, flowing east from the Chotanagpur plateau through a rift valley, used to flood the plains of West Bengal; the Damodar Valley Corporation, set up in 1948 on the model of the Tennessee Valley Authority, built dams to control it and generate power. The Kosi was similarly called the 'Sorrow of Bihar'.",
  "छोटानागपुर पठार से एक भ्रंश घाटी में पूर्व की ओर बहने वाली दामोदर पश्चिम बंगाल के मैदानों में बाढ़ लाती थी; टेनेसी घाटी प्राधिकरण के नमूने पर 1948 में बने दामोदर घाटी निगम ने इसे नियंत्रित करने और बिजली बनाने के लिए बाँध बनाए। इसी तरह कोसी को 'बिहार का शोक' कहा जाता था।",
  f"{NC11I} -- Drainage System.",
  "irv-damodar-sorrow-of-bengal")

M(RV, "medium", "Which one of the following is the largest brackish-water lagoon in India?",
  "निम्नलिखित में से कौन-सा भारत का सबसे बड़ा खारे जल का लैगून है?",
  ["Chilika", "Pulicat", "Vembanad", "Kolleru"],
  ["चिल्का", "पुलिकट", "वेम्बनाड", "कोल्लेरू"],
  0,
  "Chilika, on the Odisha coast at the mouth of the Daya river, spreads over about 1,100 sq km in the monsoon and is the largest coastal lagoon in India. Pulicat is the second largest; Vembanad is the longest lake; and Kolleru, between the Godavari and Krishna deltas, is a freshwater lake.",
  "ओडिशा तट पर दया नदी के मुहाने पर स्थित चिल्का मानसून में लगभग 1,100 वर्ग किमी में फैल जाती है और भारत का सबसे बड़ा तटीय लैगून है। पुलिकट दूसरा सबसे बड़ा है; वेम्बनाड सबसे लंबी झील है; और गोदावरी तथा कृष्णा डेल्टाओं के बीच स्थित कोल्लेरू मीठे जल की झील है।",
  f"{NC9} -- Drainage.",
  "irv-chilika-largest-lagoon")

M(RV, "medium", "Which one of the following rivers originates in Tibet?",
  "निम्नलिखित में से कौन-सी नदी तिब्बत से निकलती है?",
  ["The Satluj", "The Beas", "The Ravi", "The Yamuna"],
  ["सतलुज", "ब्यास", "रावी", "यमुना"],
  0,
  "The Satluj rises near Rakas Tal close to Mansarovar in Tibet and enters India through the Shipki La, cutting a deep gorge -- an antecedent river older than the Himalaya it crosses. The Beas rises at Beas Kund near the Rohtang pass, the Ravi in the Kullu hills of Himachal Pradesh, and the Yamuna at the Yamunotri glacier in Uttarakhand.",
  "सतलुज तिब्बत में मानसरोवर के पास राकस ताल के निकट से निकलती है और गहरा गॉर्ज काटते हुए शिपकी ला से भारत में प्रवेश करती है; यह अपने द्वारा पार किए जाने वाले हिमालय से भी पुरानी पूर्ववर्ती नदी है। ब्यास रोहतांग दर्रे के पास ब्यास कुंड से, रावी हिमाचल प्रदेश की कुल्लू पहाड़ियों से, और यमुना उत्तराखंड के यमुनोत्री हिमनद से निकलती है।",
  f"{NC11I} -- Drainage System.",
  "irv-satluj-tibet")

M(RV, "medium", "Which one of the following is the longest west-flowing river of peninsular India?",
  "निम्नलिखित में से कौन-सी प्रायद्वीपीय भारत की पश्चिम की ओर बहने वाली सबसे लंबी नदी है?",
  ["The Narmada", "The Tapi", "The Mahi", "The Sabarmati"],
  ["नर्मदा", "तापी", "माही", "साबरमती"],
  0,
  "The Narmada, about 1,312 km long, rises at Amarkantak and flows west through Madhya Pradesh, Maharashtra and Gujarat to the Gulf of Khambhat; it forms the Dhuandhar falls in the marble gorge at Bhedaghat near Jabalpur. The Tapi (about 724 km) is second.",
  "लगभग 1,312 किमी लंबी नर्मदा अमरकंटक से निकलकर मध्य प्रदेश, महाराष्ट्र और गुजरात से होते हुए पश्चिम की ओर खंभात की खाड़ी तक बहती है; जबलपुर के पास भेड़ाघाट के संगमरमर गॉर्ज में यह धुआँधार जलप्रपात बनाती है। तापी (लगभग 724 किमी) दूसरे स्थान पर है।",
  f"{NC11I} -- Drainage System.",
  "irv-longest-west-flowing-narmada")

M(RV, "easy", "Dal lake is located in:",
  "डल झील कहाँ स्थित है?",
  ["Srinagar", "Shimla", "Nainital", "Udaipur"],
  ["श्रीनगर", "शिमला", "नैनीताल", "उदयपुर"],
  0,
  "Dal lake, with its houseboats and floating gardens, lies in Srinagar, the summer capital of Jammu and Kashmir. Nainital is known for the Naini lake and Udaipur for lakes such as Pichola and Fateh Sagar.",
  "हाउसबोट और तैरते बगीचों वाली डल झील जम्मू-कश्मीर की ग्रीष्मकालीन राजधानी श्रीनगर में है। नैनीताल नैनी झील के लिए और उदयपुर पिछोला तथा फ़तेह सागर जैसी झीलों के लिए जाना जाता है।",
  f"{NC9} -- Drainage.",
  "irv-dal-lake-easy")

M(RV, "easy", "Which one of the following rivers flows the longest distance within India?",
  "निम्नलिखित में से कौन-सी नदी भारत के भीतर सबसे लंबी दूरी तक बहती है?",
  ["The Ganga", "The Godavari", "The Yamuna", "The Brahmaputra"],
  ["गंगा", "गोदावरी", "यमुना", "ब्रह्मपुत्र"],
  0,
  "The Ganga flows about 2,525 km within India, from Gangotri to the Bay of Bengal. The Brahmaputra is longer in total, but most of its course lies in Tibet and only about 900 km is in India; the Godavari, about 1,465 km, is the longest river of the Peninsula.",
  "गंगा भारत के भीतर गंगोत्री से बंगाल की खाड़ी तक लगभग 2,525 किमी बहती है। ब्रह्मपुत्र कुल मिलाकर अधिक लंबी है, पर इसका अधिकांश मार्ग तिब्बत में है और केवल लगभग 900 किमी भारत में है; लगभग 1,465 किमी लंबी गोदावरी प्रायद्वीप की सबसे लंबी नदी है।",
  f"{NC9} -- Drainage.",
  "irv-longest-river-ganga-easy")

M(RV, "hard", "In 2025 China began building a very large hydropower project on the lower reaches of the Yarlung Tsangpo in Tibet. This river enters India as the:",
  "2025 में चीन ने तिब्बत में यारलुंग त्सांगपो के निचले भाग पर एक बहुत बड़ी जलविद्युत परियोजना बनाना शुरू किया। यह नदी भारत में किस नाम से प्रवेश करती है?",
  ["Siang", "Kameng", "Barak", "Sankosh"],
  ["सियांग", "कामेंग", "बराक", "संकोश"],
  0,
  "The Yarlung Tsangpo makes a great U-turn around Namcha Barwa, through one of the deepest gorges on Earth, and enters Arunachal Pradesh as the Siang (Dihang) before becoming the Brahmaputra in Assam. India has raised concerns about the Medog (Motuo) project's effect on flows downstream and is planning its own storage project on the Siang. The Kameng and the Sankosh are north-bank tributaries rising in the Himalaya of Arunachal Pradesh and Bhutan, and the Barak flows to Bangladesh through Manipur, Mizoram and Assam.",
  "यारलुंग त्सांगपो नामचा बरवा के चारों ओर पृथ्वी के सबसे गहरे गॉर्जों में से एक से होकर एक बड़ा U-मोड़ लेती है और सियांग (दिहांग) के रूप में अरुणाचल प्रदेश में प्रवेश करती है, और फिर असम में ब्रह्मपुत्र बन जाती है। भारत ने मेडोग (मोतुओ) परियोजना के निचले प्रवाह पर प्रभाव को लेकर चिंता जताई है और सियांग पर अपनी भंडारण परियोजना की योजना बना रहा है। कामेंग और संकोश अरुणाचल प्रदेश और भूटान के हिमालय से निकलने वाली उत्तरी किनारे की सहायक नदियाँ हैं, और बराक मणिपुर, मिज़ोरम और असम से होकर बांग्लादेश जाती है।",
  f"{NC11I} -- Drainage System; Ministry of External Affairs -- statements on the Yarlung Tsangpo project (2025).",
  "irv-yarlung-tsangpo-siang")

M(RV, "hard", "The Bist-Jalandhar Doab lies between which of the following rivers?",
  "बिस्त-जालंधर दोआब निम्नलिखित में से किन नदियों के बीच स्थित है?",
  ["The Beas and the Satluj", "The Ravi and the Beas", "The Chenab and the Jhelum", "The Ravi and the Chenab"],
  ["ब्यास और सतलुज", "रावी और ब्यास", "चिनाब और झेलम", "रावी और चिनाब"],
  0,
  "A doab is the land between two converging rivers. In Punjab, the Bist-Jalandhar Doab lies between the Beas and the Satluj, and the Bari Doab between the Beas and the Ravi; across the border in Pakistan, the Rechna Doab lies between the Ravi and the Chenab and the Chaj Doab between the Chenab and the Jhelum.",
  "दोआब दो मिलने वाली नदियों के बीच की भूमि को कहते हैं। पंजाब में बिस्त-जालंधर दोआब ब्यास और सतलुज के बीच है, और बारी दोआब ब्यास और रावी के बीच; सीमा पार पाकिस्तान में रचना दोआब रावी और चिनाब के बीच तथा चाज दोआब चिनाब और झेलम के बीच है।",
  f"{NC11I} -- Drainage System.",
  "irv-bist-doab")

# ================================================================ STATEMENT-I/II (medium 5, easy 1, hard 1 + I/II/III 1)
A(RV, "medium",
  "Himalayan rivers are seasonal.",
  "हिमालयी नदियाँ मौसमी हैं।",
  "Himalayan rivers are fed both by melting snow and glaciers and by rainfall.",
  "हिमालयी नदियाँ पिघलती बर्फ़ और हिमनदों, दोनों से और वर्षा से भी पोषित होती हैं।",
  3,
  "Statement-I is incorrect but Statement-II is correct. Because they get meltwater in summer and rain in the monsoon, the Ganga, the Indus and the Brahmaputra flow throughout the year -- they are perennial, which makes them valuable for irrigation. Most Peninsular rivers depend on rain alone, and many shrink greatly in the dry season.",
  "कथन-I गलत है पर कथन-II सही है। ग्रीष्म में पिघला जल और मानसून में वर्षा मिलने से गंगा, सिंधु और ब्रह्मपुत्र पूरे वर्ष बहती हैं, यानी सदावाहिनी (perennial) हैं, जिससे वे सिंचाई के लिए मूल्यवान हैं। अधिकांश प्रायद्वीपीय नदियाँ केवल वर्षा पर निर्भर हैं, और कई शुष्क ऋतु में बहुत सिकुड़ जाती हैं।",
  f"{NC9} -- Drainage.",
  "irv-himalayan-rivers-perennial")

A(RV, "medium",
  "The Ganga-Brahmaputra delta is the largest delta in the world.",
  "गंगा-ब्रह्मपुत्र डेल्टा विश्व का सबसे बड़ा डेल्टा है।",
  "The Ganga was declared India's National River in 2008.",
  "2008 में गंगा को भारत की राष्ट्रीय नदी घोषित किया गया।",
  1,
  "Both statements are correct, but Statement-II does not explain Statement-I. The delta is so large because two of the world's most sediment-laden rivers, together with the Meghna, dump their load into the shallow head of the Bay of Bengal. The National River status, given in November 2008, is a symbolic and administrative recognition that has nothing to do with the delta's size.",
  "दोनों कथन सही हैं, पर कथन-II कथन-I की व्याख्या नहीं करता। डेल्टा इसलिए इतना बड़ा है कि विश्व की सबसे अधिक अवसाद ढोने वाली दो नदियाँ, मेघना के साथ मिलकर, अपना भार बंगाल की खाड़ी के उथले शीर्ष में गिराती हैं। नवंबर 2008 में दिया गया राष्ट्रीय नदी का दर्जा एक प्रतीकात्मक और प्रशासनिक मान्यता है, जिसका डेल्टा के आकार से कोई संबंध नहीं है।",
  f"{NC11I} -- Drainage System; {JS} -- National Mission for Clean Ganga.",
  "irv-ganga-delta-national-river")

A(RV, "medium",
  "Kolleru is a saltwater lagoon.",
  "कोल्लेरू एक खारे जल का लैगून है।",
  "Kolleru lies between the deltas of the Godavari and the Krishna and is fed by seasonal streams.",
  "कोल्लेरू गोदावरी और कृष्णा के डेल्टाओं के बीच स्थित है और मौसमी धाराओं से पोषित होती है।",
  3,
  "Statement-I is incorrect but Statement-II is correct. Kolleru in Andhra Pradesh is one of the largest freshwater lakes in the country, a shallow depression between the two deltas that fills with the monsoon inflow of streams such as the Budameru and the Tammileru and drains to the sea through the Upputeru. Large parts of it were converted into fish tanks, which have since been partly removed to restore the lake.",
  "कथन-I गलत है पर कथन-II सही है। आंध्र प्रदेश की कोल्लेरू देश की सबसे बड़ी मीठे जल की झीलों में से एक है; यह दोनों डेल्टाओं के बीच का एक उथला गर्त है, जो बुडमेरु और तम्मिलेरु जैसी धाराओं के मानसूनी प्रवाह से भरता है और उप्पुटेरु से होकर समुद्र में खाली होता है। इसके बड़े भाग मछली के तालाबों में बदल दिए गए थे, जिन्हें झील को पुनर्जीवित करने के लिए आंशिक रूप से हटाया गया है।",
  f"{NC9} -- Drainage.",
  "irv-kolleru-freshwater")

A(RV, "medium",
  "Many lakes of Ladakh, such as Pangong Tso, are saline.",
  "लद्दाख की कई झीलें, जैसे पैंगोंग त्सो, खारी हैं।",
  "They have no outlet, so water is lost mainly by evaporation in the dry climate.",
  "इनका कोई निकास नहीं है, इसलिए शुष्क जलवायु में जल मुख्य रूप से वाष्पीकरण से ही घटता है।",
  0,
  "Both statements are correct and Statement-II explains Statement-I. In these closed (endorheic) basins the streams bring in dissolved salts, and evaporation removes only the water, so the salts build up. Pangong Tso, about 134 km long and shared with Tibet, is brackish yet freezes over in winter.",
  "दोनों कथन सही हैं और कथन-II कथन-I की व्याख्या करता है। इन बंद (अंतःस्थलीय) बेसिनों में धाराएँ घुले लवण लाती हैं, और वाष्पीकरण केवल जल को हटाता है, इसलिए लवण जमा होते जाते हैं। लगभग 134 किमी लंबी और तिब्बत के साथ साझा पैंगोंग त्सो खारी है, फिर भी शीत ऋतु में जम जाती है।",
  f"{NC11I} -- Drainage System.",
  "irv-ladakh-saline-lakes")

A(RV, "medium",
  "The Yamuna joins the Ganga at Prayagraj.",
  "यमुना प्रयागराज में गंगा से मिलती है।",
  "The Yamuna rises at the Gangotri glacier.",
  "यमुना गंगोत्री हिमनद से निकलती है।",
  2,
  "Statement-I is correct but Statement-II is incorrect. The Yamuna, the longest tributary of the Ganga, rises at the Yamunotri glacier on the slopes of the Bandarpunch range; the Gangotri glacier, ending at Gaumukh, is the source of the Bhagirathi.",
  "कथन-I सही है पर कथन-II गलत है। गंगा की सबसे लंबी सहायक नदी यमुना बंदरपूँछ श्रेणी की ढलानों पर यमुनोत्री हिमनद से निकलती है; गौमुख पर समाप्त होने वाला गंगोत्री हिमनद भागीरथी का उद्गम है।",
  f"{NC11I} -- Drainage System.",
  "irv-yamuna-prayagraj-yamunotri")

A(RV, "easy",
  "Many waterfalls are found along the Western Ghats.",
  "पश्चिमी घाट के साथ बहुत-से जलप्रपात पाए जाते हैं।",
  "Rivers plunge steeply from the edge of the plateau down the western scarp of the Ghats.",
  "नदियाँ पठार के किनारे से घाट की पश्चिमी खड़ी ढलान पर तेज़ी से नीचे गिरती हैं।",
  0,
  "Both statements are correct and Statement-II explains Statement-I. The Western Ghats rise abruptly from the narrow coastal plain, so rivers crossing the edge -- the Sharavathi, the Mandovi, the Varahi and others -- drop in high falls, fed by heavy monsoon rain.",
  "दोनों कथन सही हैं और कथन-II कथन-I की व्याख्या करता है। पश्चिमी घाट संकरे तटीय मैदान से अचानक ऊपर उठते हैं, इसलिए किनारे को पार करने वाली नदियाँ, जैसे शरावती, मांडवी, वाराही और अन्य, भारी मानसूनी वर्षा से पोषित होकर ऊँचे प्रपातों में गिरती हैं।",
  f"{NC9} -- Drainage.",
  "irv-western-ghats-waterfalls-easy")

A(RV, "hard",
  "The Mahi drains into the Arabian Sea through the Gulf of Khambhat.",
  "माही खंभात की खाड़ी से होकर अरब सागर में गिरती है।",
  "The Mahi crosses the Tropic of Cancer twice.",
  "माही कर्क रेखा को दो बार पार करती है।",
  1,
  "Both statements are correct, but Statement-II does not explain Statement-I. The Mahi rises in the Vindhyas in Madhya Pradesh, flows north into Rajasthan, then loops south-west through Gujarat -- crossing the Tropic of Cancer on the way north and again on the way south -- before reaching the Gulf of Khambhat. Its mouth is decided by the slope of the land, not by the latitude it crosses.",
  "दोनों कथन सही हैं, पर कथन-II कथन-I की व्याख्या नहीं करता। माही मध्य प्रदेश में विंध्य से निकलती है, उत्तर की ओर राजस्थान में जाती है, फिर घूमकर दक्षिण-पश्चिम की ओर गुजरात से बहती है, और उत्तर जाते हुए तथा फिर दक्षिण लौटते हुए कर्क रेखा को पार करके खंभात की खाड़ी तक पहुँचती है। इसका मुहाना भूमि की ढलान से तय होता है, उसके द्वारा पार किए जाने वाले अक्षांश से नहीं।",
  f"{NC11I} -- Drainage System.",
  "irv-mahi-tropic-twice")

A(RV, "hard",
  "Floods are a recurring problem in the Brahmaputra valley of Assam.",
  "असम की ब्रह्मपुत्र घाटी में बाढ़ बार-बार आने वाली समस्या है।",
  "The Brahmaputra carries a heavy load of sediment, which raises its bed and reduces the capacity of its channel.",
  "ब्रह्मपुत्र भारी मात्रा में अवसाद ढोती है, जिससे उसका तल ऊँचा होता है और उसकी धारा की क्षमता घटती है।",
  2,
  "Only Statement II is correct, and it explains Statement I. Draining steep, young mountains with very heavy rainfall, the Brahmaputra and its north-bank tributaries bring down enormous amounts of silt, and the 1950 Assam earthquake added more; the braided, aggrading channel overflows every monsoon. "
  "Statement III is wrong: the floods come with the heavy south-west monsoon rain between June and September -- winter is the low-water season, when glaciers barely melt.",
  "केवल कथन II सही है, और वह कथन I की व्याख्या करता है। बहुत भारी वर्षा वाले खड़ी ढलान के नवीन पर्वतों का जल बहाने वाली ब्रह्मपुत्र और उसकी उत्तरी किनारे की सहायक नदियाँ भारी मात्रा में गाद लाती हैं, और 1950 के असम भूकंप ने इसमें और वृद्धि की; गुंफित (braided) और ऊँचा उठता तल हर मानसून में उफन जाता है। "
  "कथन III गलत है: बाढ़ जून से सितंबर के बीच भारी दक्षिण-पश्चिम मानसूनी वर्षा के साथ आती है; शीत ऋतु निम्न जल की ऋतु है, जब हिमनद बहुत कम पिघलते हैं।",
  f"{NC11I} -- Drainage System; Natural Hazards and Disasters.",
  "irv-assam-floods-silt",
  s3="Floods in Assam are caused mainly by glaciers melting in winter.",
  s3_hi="असम में बाढ़ मुख्य रूप से शीत ऋतु में हिमनदों के पिघलने से आती है।")

# ================================================================ PAIRS (medium 2, hard 1)
P(RV, "medium", "Consider the following pairs of waterfalls and the rivers on which they lie:",
  "जलप्रपातों और उन नदियों के निम्नलिखित युग्मों पर विचार कीजिए जिन पर वे स्थित हैं:",
  ["Chitrakote : Indravati", "Hogenakkal : Kaveri", "Dudhsagar : Mandovi", "Athirappilly : Periyar"],
  ["चित्रकोट : इंद्रावती", "होगेनक्कल : कावेरी", "दूधसागर : मांडवी", "अतिरप्पिल्ली : पेरियार"],
  2,
  "Pairs 1, 2 and 3 are correct: Chitrakote, near Jagdalpur in Bastar, is the widest fall in India; Hogenakkal, where the Kaveri enters Tamil Nadu, is known for its coracle rides; and Dudhsagar, on the Goa-Karnataka border, is crossed by the railway. "
  "Pair 4 is wrong: Athirappilly, in Thrissur district, is on the Chalakudy river, not the Periyar.",
  "युग्म 1, 2 और 3 सही हैं: बस्तर में जगदलपुर के पास स्थित चित्रकोट भारत का सबसे चौड़ा प्रपात है; होगेनक्कल, जहाँ कावेरी तमिलनाडु में प्रवेश करती है, अपनी गोल टोकरी-नावों (coracle) के लिए जाना जाता है; और गोवा-कर्नाटक सीमा पर स्थित दूधसागर के पास से रेल लाइन गुज़रती है। "
  "युग्म 4 गलत है: त्रिशूर ज़िले का अतिरप्पिल्ली प्रपात पेरियार पर नहीं, चालाकुडी नदी पर है।",
  f"{NC9} -- Drainage.",
  "irv-waterfalls-rivers-pairs")

P(RV, "medium", "Consider the following pairs of cities and the rivers on which they stand:",
  "नगरों और उन नदियों के निम्नलिखित युग्मों पर विचार कीजिए जिनके किनारे वे बसे हैं:",
  ["Jabalpur : Narmada", "Hyderabad : Musi", "Lucknow : Ghaghara", "Surat : Mahi"],
  ["जबलपुर : नर्मदा", "हैदराबाद : मूसी", "लखनऊ : घाघरा", "सूरत : माही"],
  1,
  "Pairs 1 and 2 are correct: Jabalpur stands near the Narmada, and Hyderabad on the Musi, a tributary of the Krishna. "
  "Pair 3 is wrong: Lucknow stands on the Gomti. "
  "Pair 4 is wrong: Surat stands on the Tapi, near its mouth.",
  "युग्म 1 और 2 सही हैं: जबलपुर नर्मदा के पास और हैदराबाद कृष्णा की सहायक नदी मूसी के किनारे बसा है। "
  "युग्म 3 गलत है: लखनऊ गोमती के किनारे है। "
  "युग्म 4 गलत है: सूरत तापी के किनारे, उसके मुहाने के पास है।",
  f"{NC9} -- Drainage.",
  "irv-cities-rivers-pairs")

P(RV, "hard", "Consider the following pairs of lakes and the States/UTs in which they lie:",
  "झीलों और उन राज्यों/केंद्र शासित प्रदेशों के निम्नलिखित युग्मों पर विचार कीजिए जिनमें वे स्थित हैं:",
  ["Tsomgo : Sikkim", "Rudrasagar : Tripura", "Sasthamkotta : Tamil Nadu", "Tso Moriri : Himachal Pradesh"],
  ["त्सोमगो : सिक्किम", "रुद्रसागर : त्रिपुरा", "शास्थमकोट्टा : तमिलनाडु", "त्सो मोरीरी : हिमाचल प्रदेश"],
  1,
  "Pairs 1 and 2 are correct: Tsomgo (Changu), a glacial lake on the road to Nathu La, is in Sikkim, and Rudrasagar, with the Neermahal water palace, is in Tripura. "
  "Pair 3 is wrong: Sasthamkotta, the largest freshwater lake of Kerala, is in Kollam district. "
  "Pair 4 is wrong: Tso Moriri, a high-altitude brackish lake of the Changthang plateau, is in Ladakh.",
  "युग्म 1 और 2 सही हैं: नाथू ला के रास्ते पर स्थित हिमनदी झील त्सोमगो (छांगू) सिक्किम में है, और नीरमहल जल-महल वाली रुद्रसागर झील त्रिपुरा में है। "
  "युग्म 3 गलत है: केरल की सबसे बड़ी मीठे जल की झील शास्थमकोट्टा कोल्लम ज़िले में है। "
  "युग्म 4 गलत है: चांगथांग पठार की अधिक ऊँचाई वाली खारी झील त्सो मोरीरी लद्दाख में है।",
  f"{NC9} -- Drainage.",
  "irv-lakes-states-pairs")

if __name__ == "__main__":
    write("geo_l2_t13_rivers.sql")
