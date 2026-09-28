# -*- coding: utf-8 -*-
"""Level 2 · Test 8 (History 4: Art & Culture) -- Iconography (14) and Culture-Other (9), new
bilingual rows against the live gap report. Iconography: medium statement 4, easy statement 3,
medium MCQ 2, hard statement 2, easy MCQ 1, hard MCQ 1, easy pairs 1. Culture-Other: medium
statement 2, medium MCQ 2, easy MCQ 1, easy statement 1, hard MCQ 1, hard statement 1, medium
pairs 1. The existing rows (Buddhist mudras, deity vahanas, Jain lanchhanas, the Chola Nataraja;
classical languages) are not repeated; no new row names a vahana tested there, says how
Tirthankara images are told apart, or names the demon under Nataraja's foot."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, write
from polity_common import C3, C4, T2

d.SUBJECT = "History"
IC = "Iconography"
CO = "Culture-Other"
NC11 = "NCERT Class XI, An Introduction to Indian Art (Part I)"
CCRT = "Centre for Cultural Resources and Training (CCRT), Ministry of Culture"
UNESCO_ICH = "UNESCO -- Lists of Intangible Cultural Heritage (India)"
GI = "Geographical Indications Registry, Chennai"

# ================================================================ ICONOGRAPHY
S(IC, "medium", "Consider the following statements about the iconography of Vishnu:",
  "विष्णु की प्रतिमा-विद्या के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["In the Varaha avatar, Vishnu is shown as a boar rescuing the Earth goddess from the waters.",
   "In the Narasimha avatar, he is shown as half man, half lion.",
   "Vishnu's four usual attributes are the trident, the drum, the axe and the deer."],
  ["वराह अवतार में विष्णु को जल से पृथ्वी देवी को बचाते वराह (सूअर) के रूप में दिखाया जाता है।",
   "नरसिंह अवतार में उन्हें आधे मनुष्य, आधे सिंह के रूप में दिखाया जाता है।",
   "विष्णु के चार सामान्य आयुध त्रिशूल, डमरू, परशु और मृग हैं।"],
  C3, 1,
  "Statements 1 and 2 are correct. The great Varaha panel at Udayagiri and the Narasimha images of the Pallavas and Hoysalas show how avatar stories were carved. "
  "Statement 3 describes Shiva, not Vishnu: the trident, damaru (drum), axe and deer belong to Shiva's iconography, while Vishnu usually holds the conch (shankha), the discus (chakra), the mace (gada) and the lotus (padma); the order in which he holds them gives his 24 named forms.",
  "कथन 1 और 2 सही हैं। उदयगिरि का महान वराह फलक और पल्लवों तथा होयसलों की नरसिंह प्रतिमाएँ दिखाती हैं कि अवतार-कथाएँ कैसे तराशी गईं। "
  "कथन 3 विष्णु का नहीं, शिव का वर्णन है: त्रिशूल, डमरू, परशु और मृग शिव की प्रतिमा-विद्या के हैं, जबकि विष्णु सामान्यतः शंख, चक्र, गदा और पद्म धारण करते हैं; जिस क्रम में वे इन्हें धारण करते हैं, उससे उनके 24 नामित रूप बनते हैं।",
  f"{NC11} -- Temple Architecture and Sculpture; T.A. Gopinatha Rao, Elements of Hindu Iconography.",
  "art-vishnu-iconography")

S(IC, "medium", "Consider the following statements about images of Shiva:",
  "शिव की प्रतिमाओं के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["As Dakshinamurti, Shiva is shown as a teacher, facing south.",
   "In the Nataraja image, Shiva dances on the back of the bull Nandi.",
   "The Lingodbhava image shows Shiva as the cosmic dancer."],
  ["दक्षिणामूर्ति के रूप में शिव को दक्षिण की ओर मुख किए एक गुरु के रूप में दिखाया जाता है।",
   "नटराज प्रतिमा में शिव नंदी बैल की पीठ पर नृत्य करते हैं।",
   "लिंगोद्भव प्रतिमा शिव को ब्रह्मांडीय नर्तक के रूप में दिखाती है।"],
  C3, 0,
  "Only statement 1 is correct: Dakshinamurti, often placed in a niche on the south wall of Shiva temples in Tamil Nadu, sits under a banyan tree teaching sages in silence. "
  "Statement 2 is wrong: in the Nataraja image Shiva dances within a ring of flames with one foot raised, not on Nandi. "
  "Statement 3 is wrong: Lingodbhava shows Shiva emerging from an endless pillar of fire (the linga), while Brahma as a swan and Vishnu as a boar search in vain for its top and bottom -- a story about Shiva's infinity, not his dance.",
  "केवल कथन 1 सही है: तमिलनाडु के शिव मंदिरों में प्रायः दक्षिणी दीवार के आले में रखे जाने वाले दक्षिणामूर्ति बरगद के पेड़ के नीचे बैठकर मौन में ऋषियों को शिक्षा देते हैं। "
  "कथन 2 गलत है: नटराज प्रतिमा में शिव ज्वालाओं के घेरे में एक पैर उठाकर नृत्य करते हैं, नंदी पर नहीं। "
  "कथन 3 गलत है: लिंगोद्भव में शिव अग्नि के अनंत स्तंभ (लिंग) से प्रकट होते हैं, जबकि हंस के रूप में ब्रह्मा और वराह के रूप में विष्णु उसका शीर्ष और तल व्यर्थ में खोजते हैं; यह शिव की अनंतता की कथा है, उनके नृत्य की नहीं।",
  f"{NC11}; T.A. Gopinatha Rao, Elements of Hindu Iconography.",
  "art-shiva-forms-dakshinamurti-lingodbhava")

S(IC, "medium", "Consider the following statements about Bodhisattvas in Buddhist art:",
  "बौद्ध कला में बोधिसत्वों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Avalokiteshvara, the Bodhisattva of compassion, is often shown holding a lotus (as Padmapani).",
   "Maitreya is the Buddha of the future.",
   "Manjushri, the Bodhisattva of wisdom, is often shown with a sword."],
  ["करुणा के बोधिसत्व अवलोकितेश्वर को प्रायः कमल थामे (पद्मपाणि के रूप में) दिखाया जाता है।",
   "मैत्रेय भविष्य के बुद्ध हैं।",
   "प्रज्ञा के बोधिसत्व मंजुश्री को प्रायः तलवार के साथ दिखाया जाता है।"],
  C3, 2,
  "All three statements are correct. The Padmapani painting in Ajanta Cave 1, with its lowered eyes and lotus, is one of the most famous images in Indian art. Maitreya, who will come when the teaching has been forgotten, is often shown holding a water flask; Manjushri's flaming sword cuts through ignorance, and he often carries a book of wisdom. Bodhisattvas are shown wearing jewellery and crowns, unlike the plain-robed Buddha.",
  "तीनों कथन सही हैं। अजंता की गुफा 1 का झुकी आँखों और कमल वाला पद्मपाणि चित्र भारतीय कला की सबसे प्रसिद्ध छवियों में है। मैत्रेय, जो शिक्षा के भुला दिए जाने पर आएँगे, प्रायः जलपात्र थामे दिखते हैं; मंजुश्री की ज्वलंत तलवार अज्ञान को काटती है, और वे प्रायः प्रज्ञा की पुस्तक भी लिए रहते हैं। सादे वस्त्रों वाले बुद्ध के विपरीत बोधिसत्वों को आभूषण और मुकुट पहने दिखाया जाता है।",
  f"{NC11} -- Arts of the Mauryan period / Later Mural Traditions.",
  "art-bodhisattva-iconography")

S(IC, "medium", "Consider the following statements about images of goddesses:",
  "देवियों की प्रतिमाओं के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Mahishasuramardini images show Durga slaying the buffalo demon.",
   "The vahana of Saraswati is the owl.",
   "In 'Gajalakshmi' images, Lakshmi is shown seated on a lotus while elephants pour water over her."],
  ["महिषासुरमर्दिनी प्रतिमाएँ दुर्गा को भैंसे राक्षस का वध करते दिखाती हैं।",
   "सरस्वती का वाहन उल्लू है।",
   "'गजलक्ष्मी' प्रतिमाओं में लक्ष्मी कमल पर बैठी दिखती हैं और हाथी उन पर जल डालते हैं।"],
  C3, 1,
  "Statements 1 and 3 are correct. The Mahishasuramardini panel at Mamallapuram and countless later images show Durga's battle with Mahisha; Gajalakshmi, one of the oldest goddess images, appears as early as the gateways at Sanchi. "
  "Statement 2 is wrong: Saraswati rides a swan (hamsa), the bird said to separate milk from water, a symbol of discernment; the owl is associated with Lakshmi, especially in Bengal.",
  "कथन 1 और 3 सही हैं। मामल्लपुरम का महिषासुरमर्दिनी फलक और बाद की अनगिनत प्रतिमाएँ महिष के साथ दुर्गा का युद्ध दिखाती हैं; सबसे पुरानी देवी-प्रतिमाओं में से एक गजलक्ष्मी साँची के तोरणों पर भी दिखती हैं। "
  "कथन 2 गलत है: सरस्वती हंस पर सवार होती हैं, जिस पक्षी के बारे में कहा जाता है कि वह दूध को पानी से अलग करता है, जो विवेक का प्रतीक है; उल्लू लक्ष्मी से जुड़ा है, विशेषकर बंगाल में।",
  f"{NC11}; T.A. Gopinatha Rao, Elements of Hindu Iconography.",
  "art-goddess-iconography")

S(IC, "easy", "Consider the following statements about images of the Buddha:",
  "बुद्ध की प्रतिमाओं के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The 'ushnisha' is the protuberance on the top of the Buddha's head.",
   "The 'urna' is the tuft or dot between the Buddha's eyebrows."],
  ["'उष्णीष' बुद्ध के सिर के शीर्ष पर का उभार है।",
   "'ऊर्णा' बुद्ध की भौंहों के बीच का बालों का गुच्छा या बिंदु है।"],
  T2, 2,
  "Both statements are correct. The ushnisha and the urna are among the 32 marks of a 'great man' (mahapurusha lakshanas) that texts ascribe to the Buddha; together with elongated earlobes, a reminder of the heavy earrings of his princely life, they help identify Buddha images in every school, from Gandhara and Mathura to Sarnath.",
  "दोनों कथन सही हैं। उष्णीष और ऊर्णा उन 32 'महापुरुष लक्षणों' में हैं जिन्हें ग्रंथ बुद्ध से जोड़ते हैं; लंबे कर्णपुटों के साथ, जो उनके राजकुमार-जीवन के भारी कुंडलों की याद दिलाते हैं, ये गांधार और मथुरा से सारनाथ तक हर शैली में बुद्ध-प्रतिमाओं को पहचानने में मदद करते हैं।",
  f"{NC11} -- Post-Mauryan trends in Indian art and architecture.",
  "art-buddha-ushnisha-urna")

S(IC, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The vahana of Ganesha is the mouse.",
   "Kartikeya's chief weapon is the noose (pasha)."],
  ["गणेश का वाहन मूषक (चूहा) है।",
   "कार्तिकेय का मुख्य आयुध पाश (फंदा) है।"],
  T2, 0,
  "Only statement 1 is correct: Ganesha rides a mouse (mushaka), and he is usually shown with a broken tusk, a bowl of sweets (modakas), an axe and a noose. Statement 2 is wrong: Kartikeya (Murugan, Skanda), the god of war, carries the spear (vel or shakti), which is why his Tamil devotees' festivals centre on the vel.",
  "केवल कथन 1 सही है: गणेश मूषक पर सवार होते हैं, और उन्हें प्रायः टूटे दाँत, मोदकों के पात्र, परशु और पाश के साथ दिखाया जाता है। कथन 2 गलत है: युद्ध के देवता कार्तिकेय (मुरुगन, स्कंद) भाला (वेल या शक्ति) धारण करते हैं, इसीलिए उनके तमिल भक्तों के उत्सव वेल पर केंद्रित होते हैं।",
  f"{NC11}; T.A. Gopinatha Rao, Elements of Hindu Iconography.",
  "art-ganesha-kartikeya-attributes")

S(IC, "easy", "Consider the following statements about Jain images:",
  "जैन प्रतिमाओं के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Tirthankaras are shown either standing in the 'kayotsarga' posture or seated in meditation.",
   "Digambara images show the Tirthankaras unclothed.",
   "The colossal statue of Gommateshwara at Shravanabelagola depicts Mahavira."],
  ["तीर्थंकरों को या तो 'कायोत्सर्ग' मुद्रा में खड़े या ध्यान में बैठे दिखाया जाता है।",
   "दिगंबर प्रतिमाएँ तीर्थंकरों को निर्वस्त्र दिखाती हैं।",
   "श्रवणबेलगोला की गोमटेश्वर की विशाल प्रतिमा महावीर को दिखाती है।"],
  C3, 1,
  "Statements 1 and 2 are correct. In kayotsarga the figure stands upright with arms hanging straight at the sides, in total detachment from the body; Digambara ('sky-clad') images are nude, while Svetambara images are shown clothed and often with ornaments. "
  "Statement 3 is wrong: the 57-foot monolith at Shravanabelagola (about 983 CE), raised by the Ganga minister Chamundaraya, depicts Bahubali (Gommateshwara), son of the first Tirthankara, who meditated so long that creepers grew around his limbs -- as the statue shows.",
  "कथन 1 और 2 सही हैं। कायोत्सर्ग में आकृति शरीर से पूर्ण विरक्ति में, भुजाएँ सीधे बगल में लटकाए, सीधी खड़ी रहती है; दिगंबर ('आकाश-वस्त्र') प्रतिमाएँ निर्वस्त्र होती हैं, जबकि श्वेतांबर प्रतिमाएँ वस्त्र और प्रायः आभूषणों के साथ दिखाई जाती हैं। "
  "कथन 3 गलत है: गंग मंत्री चामुंडराय द्वारा बनवाई गई श्रवणबेलगोला की 57 फ़ुट की एकाश्म प्रतिमा (लगभग 983 ई.) बाहुबली (गोमटेश्वर) की है, जो पहले तीर्थंकर के पुत्र थे और इतने लंबे समय तक ध्यान में रहे कि उनके अंगों पर लताएँ उग आईं, जैसा प्रतिमा दिखाती है।",
  f"{NC11}; Karnataka Department of Archaeology -- Shravanabelagola.",
  "art-jain-images-kayotsarga-bahubali")

M(IC, "medium", "Which deity is traditionally shown as 'chaturmukha', with four faces?",
  "किस देवता को पारंपरिक रूप से 'चतुर्मुख', यानी चार मुखों वाला, दिखाया जाता है?",
  ["Brahma", "Vishnu", "Indra", "Surya"],
  ["ब्रह्मा", "विष्णु", "इंद्र", "सूर्य"],
  0,
  "Brahma, the creator, is shown with four faces looking in the four directions, often bearded and holding the Vedas, a water pot and a rosary; he has very few temples of his own, Pushkar being the best known. Surya is identified by his two lotuses, boots and chariot, and Indra by the thunderbolt and the elephant Airavata.",
  "सृष्टिकर्ता ब्रह्मा को चारों दिशाओं में देखते चार मुखों के साथ, प्रायः दाढ़ी वाले और वेद, जलपात्र तथा माला थामे दिखाया जाता है; उनके अपने बहुत कम मंदिर हैं, जिनमें पुष्कर सबसे प्रसिद्ध है। सूर्य अपने दो कमलों, जूतों और रथ से, और इंद्र वज्र तथा ऐरावत हाथी से पहचाने जाते हैं।",
  f"{NC11}; T.A. Gopinatha Rao, Elements of Hindu Iconography.",
  "art-brahma-chaturmukha")

M(IC, "medium", "In Buddhist art, the Bodhisattva who holds the thunderbolt (vajra) is:",
  "बौद्ध कला में वज्र धारण करने वाला बोधिसत्व कौन है?",
  ["Vajrapani", "Avalokiteshvara", "Manjushri", "Kshitigarbha"],
  ["वज्रपाणि", "अवलोकितेश्वर", "मंजुश्री", "क्षितिगर्भ"],
  0,
  "Vajrapani ('thunderbolt in hand') is the protector of the Buddha and symbol of his power; in Gandhara art he appears beside the Buddha in a form borrowed from the Greek hero Heracles. In the Ajanta paintings Vajrapani and Padmapani often flank the Buddha together.",
  "वज्रपाणि ('हाथ में वज्र') बुद्ध के रक्षक और उनकी शक्ति के प्रतीक हैं; गांधार कला में वे यूनानी नायक हेराक्लीज़ से लिए गए रूप में बुद्ध के बगल में दिखते हैं। अजंता के चित्रों में वज्रपाणि और पद्मपाणि प्रायः एक साथ बुद्ध के दोनों ओर होते हैं।",
  f"{NC11} -- Post-Mauryan trends (Gandhara).",
  "art-vajrapani")

S(IC, "hard", "Consider the following statements about Chola bronzes:",
  "चोल कांस्य प्रतिमाओं के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["They were made by the lost-wax (cire perdue) method.",
   "Swamimalai in Tamil Nadu is still a centre of this craft.",
   "The mould is broken after casting, so each image is unique."],
  ["ये लुप्त-मोम (cire perdue) विधि से बनाई जाती थीं।",
   "तमिलनाडु का स्वामीमलै आज भी इस शिल्प का केंद्र है।",
   "ढलाई के बाद साँचा तोड़ दिया जाता है, इसलिए हर प्रतिमा अनोखी होती है।"],
  C3, 2,
  "All three statements are correct. The sculptor first models the image in a mixture of beeswax and resin, covers it with layers of fine clay, heats the mould so the wax runs out, and pours in molten metal -- an alloy of copper with some tin and other metals; the mould is then broken, so each image is unique. Swamimalai near Kumbakonam holds a GI tag for such icons. "
  "Because the clay mould is destroyed to release each casting, no two icons are identical -- which is also how experts spot modern copies of stolen Chola bronzes.",
  "तीनों कथन सही हैं। मूर्तिकार पहले मधुमक्खी के मोम और राल के मिश्रण से प्रतिमा गढ़ता है, उसे महीन मिट्टी की परतों से ढकता है, साँचे को गर्म करता है ताकि मोम बह जाए, और उसमें पिघली धातु, यानी कुछ टिन और दूसरी धातुओं के साथ ताँबे की मिश्र धातु, डालता है; फिर साँचा तोड़ दिया जाता है, इसलिए हर प्रतिमा अनोखी होती है। कुंभकोणम के पास स्वामीमलै के पास ऐसी मूर्तियों के लिए GI टैग है। "
  "चूँकि हर ढलाई को निकालने के लिए मिट्टी का साँचा तोड़ दिया जाता है, कोई दो मूर्तियाँ एक-सी नहीं होतीं; इसी से विशेषज्ञ चुराई गई चोल कांस्य प्रतिमाओं की आधुनिक नकलें भी पहचानते हैं।",
  f"{NC11} -- Bronze Sculpture; {GI} -- Swamimalai bronze icons.",
  "art-chola-bronze-lost-wax")

S(IC, "hard", "Consider the following statements about the texts on image-making:",
  "प्रतिमा-निर्माण संबंधी ग्रंथों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["'Talamana' is a system of proportions used in making images.",
   "The Agamas and the Shilpa Shastras lay down the forms of images for worship.",
   "The Chitrasutra, a section of the Vishnudharmottara Purana, deals with painting."],
  ["'तालमान' प्रतिमाएँ बनाने में उपयोग होने वाली अनुपात-प्रणाली है।",
   "आगम और शिल्पशास्त्र उपासना की प्रतिमाओं के रूप निर्धारित करते हैं।",
   "विष्णुधर्मोत्तर पुराण का एक भाग चित्रसूत्र चित्रकला से संबंधित है।"],
  C3, 2,
  "All three statements are correct. In talamana the face length (tala) serves as the unit, and images of gods, humans and demons are given different numbers of talas -- which is why images across a region look consistently proportioned. The Agamas and Shilpa texts prescribe each deity's posture, number of arms, attributes and consort; the Chitrasutra discusses the six limbs of painting, the rendering of emotion and even perspective.",
  "तीनों कथन सही हैं। तालमान में मुख की लंबाई (ताल) इकाई का काम करती है, और देवताओं, मनुष्यों और राक्षसों की प्रतिमाओं को अलग-अलग तालों की संख्या दी जाती है; इसीलिए किसी क्षेत्र की प्रतिमाएँ सुसंगत अनुपात वाली दिखती हैं। आगम और शिल्प ग्रंथ हर देवता की मुद्रा, भुजाओं की संख्या, आयुध और सहचरी निर्धारित करते हैं; चित्रसूत्र चित्रकला के छह अंगों, भाव के चित्रण और परिप्रेक्ष्य तक पर विचार करता है।",
  f"{NC11}; Stella Kramrisch, The Vishnudharmottara (Part III).",
  "art-image-making-texts-talamana")

M(IC, "easy", "The vahana of the goddess Durga is usually shown as the:",
  "देवी दुर्गा का वाहन सामान्यतः किस रूप में दिखाया जाता है?",
  ["Lion", "Swan", "Peacock", "Bull"],
  ["सिंह", "हंस", "मोर", "बैल"],
  0,
  "Durga rides a lion (or sometimes a tiger), symbolising power and courage, as she goes into battle against Mahishasura. The swan belongs to Saraswati, the peacock to Kartikeya and the bull Nandi to Shiva.",
  "महिषासुर के विरुद्ध युद्ध में जाती दुर्गा सिंह (या कभी-कभी बाघ) पर सवार होती हैं, जो शक्ति और साहस का प्रतीक है। हंस सरस्वती का, मोर कार्तिकेय का और नंदी बैल शिव का है।",
  f"{NC11}.",
  "art-durga-vahana-lion")

M(IC, "hard", "'Harihara' images combine the features of:",
  "'हरिहर' प्रतिमाएँ किनकी विशेषताओं को मिलाती हैं?",
  ["Vishnu and Shiva", "Shiva and Parvati", "Vishnu and Lakshmi", "Brahma and Vishnu"],
  ["विष्णु और शिव", "शिव और पार्वती", "विष्णु और लक्ष्मी", "ब्रह्मा और विष्णु"],
  0,
  "In Harihara images, one half of the figure is Vishnu (Hari) -- with his crown, conch or discus -- and the other half Shiva (Hara) -- with matted hair, trident and snake; they express the unity of the two great sects and are well known from Badami and from Cambodia. Shiva and Parvati united in one figure form the Ardhanarishvara, the most common confusion.",
  "हरिहर प्रतिमाओं में आकृति का आधा भाग विष्णु (हरि) का होता है, उनके मुकुट, शंख या चक्र के साथ, और आधा शिव (हर) का, जटाओं, त्रिशूल और सर्प के साथ; ये दोनों बड़े संप्रदायों की एकता व्यक्त करती हैं और बादामी तथा कंबोडिया से प्रसिद्ध हैं। एक आकृति में शिव और पार्वती अर्धनारीश्वर बनाते हैं; यही सबसे आम भ्रम है।",
  f"{NC11}; T.A. Gopinatha Rao, Elements of Hindu Iconography.",
  "art-harihara")

P(IC, "easy", "Consider the following pairs of images and the religious traditions to which they belong:",
  "प्रतिमाओं और उनकी धार्मिक परंपराओं के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Tara : Buddhism", "Ambika : Jainism", "Padmavati : Buddhism", "Hariti : Buddhism"],
  ["तारा : बौद्ध धर्म", "अंबिका : जैन धर्म", "पद्मावती : बौद्ध धर्म", "हारीति : बौद्ध धर्म"],
  2,
  "Three pairs are correct. Tara, the saviour goddess, is central to Mahayana and Vajrayana Buddhism; Ambika is the yakshi (attendant goddess) of the Jain Tirthankara Neminatha, shown with children and a mango tree; and Hariti, once a demoness who devoured children and was converted by the Buddha, is a Buddhist goddess of fertility and protection, often shown with her consort Panchika. "
  "Pair 3 is wrong: Padmavati, shown with a serpent canopy, is the Jain yakshi of the Tirthankara Parshvanatha and is widely worshipped in Karnataka.",
  "तीन युग्म सही हैं। उद्धारक देवी तारा महायान और वज्रयान बौद्ध धर्म में केंद्रीय हैं; अंबिका जैन तीर्थंकर नेमिनाथ की यक्षी (सेविका-देवी) हैं, जिन्हें बच्चों और आम के पेड़ के साथ दिखाया जाता है; और हारीति, जो कभी बच्चों को खाने वाली राक्षसी थीं और बुद्ध ने जिनका मन बदला, उर्वरता और रक्षा की बौद्ध देवी हैं, जो प्रायः अपने सहचर पांचिक के साथ दिखती हैं। "
  "युग्म 3 गलत है: सर्प-छत्र के साथ दिखाई जाने वाली पद्मावती जैन तीर्थंकर पार्श्वनाथ की यक्षी हैं और कर्नाटक में व्यापक रूप से पूजी जाती हैं।",
  f"{NC11}.",
  "art-images-traditions-pairs")

# ================================================================ CULTURE-OTHER
S(CO, "medium", "Consider the following statements about India's elements on UNESCO's intangible cultural heritage lists:",
  "UNESCO की अमूर्त सांस्कृतिक धरोहर सूचियों में भारत के तत्वों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Garba, the devotional dance associated with Navratri, was inscribed in 2023.",
   "Durga Puja in Kolkata was inscribed in 2021.",
   "Yoga was inscribed on the World Heritage List of monuments and sites."],
  ["नवरात्रि से जुड़ा भक्तिपूर्ण नृत्य गरबा 2023 में शामिल किया गया।",
   "कोलकाता की दुर्गा पूजा 2021 में शामिल की गई।",
   "योग को स्मारकों और स्थलों की विश्व धरोहर सूची में शामिल किया गया।"],
  C3, 1,
  "Statements 1 and 2 are correct. Garba (2023) and Durga Puja in Kolkata (2021) are among India's inscriptions on the Representative List of the Intangible Cultural Heritage of Humanity, alongside Vedic chanting, Ramlila, Kutiyattam, Chhau, the Kumbh Mela and others. "
  "Statement 3 is wrong: Yoga was inscribed in 2016 on the intangible heritage list, under the 2003 Convention; the World Heritage List, under the 1972 Convention, covers monuments, sites and landscapes.",
  "कथन 1 और 2 सही हैं। गरबा (2023) और कोलकाता की दुर्गा पूजा (2021) मानवता की अमूर्त सांस्कृतिक धरोहर की प्रतिनिधि सूची में भारत की प्रविष्टियों में हैं, साथ में वैदिक पाठ, रामलीला, कूडियाट्टम, छऊ, कुंभ मेला और दूसरे। "
  "कथन 3 गलत है: योग 2016 में 2003 के अभिसमय के तहत अमूर्त धरोहर सूची में शामिल हुआ; 1972 के अभिसमय के तहत विश्व धरोहर सूची स्मारकों, स्थलों और भू-दृश्यों को शामिल करती है।",
  f"{UNESCO_ICH}; UNESCO Convention for the Safeguarding of the Intangible Cultural Heritage (2003).",
  "culture-unesco-ich-garba-durga-puja")

S(CO, "medium", "Consider the following statements about festivals:",
  "त्योहारों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Hornbill Festival is held in Nagaland.",
   "Losar is the harvest festival of Kerala.",
   "Onam is chiefly celebrated in Assam."],
  ["हॉर्नबिल उत्सव नागालैंड में होता है।",
   "लोसर केरल का फ़सल-उत्सव है।",
   "ओणम मुख्य रूप से असम में मनाया जाता है।"],
  C3, 0,
  "Only statement 1 is correct: the Hornbill Festival, held every December at Kisama near Kohima, brings together the culture of Nagaland's tribes and is named after the bird that figures in their folklore. "
  "Statement 2 is wrong: Losar is the Tibetan Buddhist New Year, celebrated in Ladakh, Sikkim, Arunachal and Himachal. "
  "Statement 3 is wrong: Onam, the harvest festival linked with the legend of King Mahabali, is Kerala's great festival, with boat races and floral carpets (pookalam).",
  "केवल कथन 1 सही है: हर दिसंबर कोहिमा के पास किसामा में होने वाला हॉर्नबिल उत्सव नागालैंड की जनजातियों की संस्कृति को एक साथ लाता है और उस पक्षी पर नामित है जो उनकी लोककथाओं में आता है। "
  "कथन 2 गलत है: लोसर तिब्बती बौद्ध नववर्ष है, जो लद्दाख, सिक्किम, अरुणाचल और हिमाचल में मनाया जाता है। "
  "कथन 3 गलत है: राजा महाबली की कथा से जुड़ा फ़सल-उत्सव ओणम केरल का बड़ा त्योहार है, जिसमें नौका-दौड़ और फूलों के कालीन (पूक्कलम) होते हैं।",
  f"{CCRT} -- fairs and festivals of India.",
  "culture-festivals-hornbill-losar-onam")

S(CO, "easy", "Consider the following statements about the Kumbh Mela:",
  "कुंभ मेले के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["At each of its four sites, the full Kumbh Mela is held every six years.",
   "It is on UNESCO's list of the intangible cultural heritage of humanity."],
  ["अपने चारों स्थलों में से हर एक पर पूर्ण कुंभ मेला हर छह वर्ष में होता है।",
   "यह UNESCO की मानवता की अमूर्त सांस्कृतिक धरोहर सूची में है।"],
  T2, 1,
  "Only statement 2 is correct: the Kumbh Mela was inscribed in 2017. Statement 1 is wrong: the full Kumbh comes round at each of the four sites -- Prayagraj, Haridwar, Ujjain and Nashik -- about every twelve years, following the position of Jupiter; the 'Ardh Kumbh' is held at Prayagraj and Haridwar in the sixth year.",
  "केवल कथन 2 सही है: कुंभ मेला 2017 में शामिल किया गया। कथन 1 गलत है: पूर्ण कुंभ चारों स्थलों, यानी प्रयागराज, हरिद्वार, उज्जैन और नासिक, में से हर एक पर बृहस्पति की स्थिति के अनुसार लगभग हर बारह वर्ष में आता है; 'अर्ध कुंभ' छठे वर्ष में प्रयागराज और हरिद्वार में होता है।",
  f"{UNESCO_ICH} -- Kumbh Mela (2017).",
  "culture-kumbh-mela")

S(CO, "hard", "Consider the following statements about products with a Geographical Indication (GI) tag:",
  "भौगोलिक संकेतक (GI) टैग वाले उत्पादों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Channapatna toys are from Karnataka.",
   "Bidriware, metalwork inlaid with silver, is from Karnataka.",
   "Pochampally ikat is from Telangana.",
   "The Chanderi saree is from Rajasthan."],
  ["चन्नपटना के खिलौने कर्नाटक के हैं।",
   "चाँदी की जड़ाई वाला धातु-शिल्प बिदरी कर्नाटक का है।",
   "पोचमपल्ली इकत तेलंगाना का है।",
   "चंदेरी साड़ी राजस्थान की है।"],
  C4, 2,
  "Statements 1, 2 and 3 are correct. Channapatna's lacquered wooden toys, made near Bengaluru, are coloured with natural dyes; Bidriware, from Bidar, inlays silver into a blackened alloy of zinc and copper, darkened with soil from the Bidar fort; and Pochampally's tie-and-dye ikat, woven in Nalgonda district, was one of India's early GI registrations. "
  "Statement 4 is wrong: Chanderi sarees, light cotton-silk weaves with gold motifs, come from Chanderi in Ashoknagar district, Madhya Pradesh.",
  "कथन 1, 2 और 3 सही हैं। बेंगलुरु के पास बनने वाले चन्नपटना के लाख-रंगे लकड़ी के खिलौने प्राकृतिक रंगों से रँगे जाते हैं; बीदर का बिदरी शिल्प जस्ते और ताँबे की काली की गई मिश्र धातु में चाँदी जड़ता है, जिसे बीदर क़िले की मिट्टी से काला किया जाता है; और नलगोंडा ज़िले में बुना जाने वाला पोचमपल्ली का बाँधकर-रँगा इकत भारत के आरंभिक GI पंजीकरणों में था। "
  "कथन 4 गलत है: सुनहरे अलंकरणों वाली हल्की सूती-रेशमी चंदेरी साड़ियाँ मध्य प्रदेश के अशोकनगर ज़िले के चंदेरी से आती हैं।",
  f"{GI}; {CCRT} -- crafts of India.",
  "culture-gi-crafts")

M(CO, "medium", "The 'Sangai Festival', named after the State animal, is held in:",
  "राज्य पशु के नाम पर 'संगाई महोत्सव' कहाँ होता है?",
  ["Manipur", "Mizoram", "Meghalaya", "Tripura"],
  ["मणिपुर", "मिज़ोरम", "मेघालय", "त्रिपुरा"],
  0,
  "Manipur's Sangai Festival, held every November since 2010, showcases its dances, martial arts, handlooms and cuisine, and takes its name from the endangered brow-antlered deer found only at Keibul Lamjao. Mizoram's Chapchar Kut, Meghalaya's Wangala and Tripura's Kharchi Puja are other north-eastern festivals.",
  "2010 से हर नवंबर होने वाला मणिपुर का संगाई महोत्सव उसके नृत्यों, युद्ध-कलाओं, हथकरघा और व्यंजनों को प्रदर्शित करता है, और इसका नाम उस संकटग्रस्त भौंह-सींग वाले हिरण पर है जो केवल केइबुल लामजाओ में मिलता है। मिज़ोरम का चापचार कुट, मेघालय का वांगला और त्रिपुरा की खर्ची पूजा पूर्वोत्तर के दूसरे त्योहार हैं।",
  "Government of Manipur -- Department of Tourism; " + CCRT + ".",
  "culture-sangai-festival")

M(CO, "medium", "The festival of Chhath, celebrated especially in Bihar and eastern Uttar Pradesh, is dedicated to:",
  "विशेषकर बिहार और पूर्वी उत्तर प्रदेश में मनाया जाने वाला छठ पर्व किसे समर्पित है?",
  ["The Sun god (Surya) and Chhathi Maiya", "The goddess Durga", "Lord Krishna", "The river Ganga alone, as a mother goddess"],
  ["सूर्य देव और छठी मैया", "देवी दुर्गा", "भगवान कृष्ण", "मातृ देवी के रूप में केवल गंगा नदी"],
  0,
  "Chhath is a four-day festival in which devotees fast, stand in rivers or ponds and offer arghya to the setting and then the rising sun, worshipping Surya and Chhathi Maiya; it has no priestly intermediary and is notable for its ritual cleanliness. The river setting is why 'the river Ganga alone' is the trap.",
  "छठ चार दिन का पर्व है, जिसमें भक्त उपवास करते हैं, नदियों या तालाबों में खड़े होकर डूबते और फिर उगते सूर्य को अर्घ्य देते हैं और सूर्य तथा छठी मैया की उपासना करते हैं; इसमें कोई पुरोहित-मध्यस्थ नहीं होता और यह अपनी अनुष्ठानिक शुद्धता के लिए उल्लेखनीय है। नदी का परिवेश ही कारण है कि 'केवल गंगा नदी' जाल है।",
  f"{CCRT} -- fairs and festivals of India.",
  "culture-chhath-surya")

M(CO, "easy", "Pongal is a harvest festival of:",
  "पोंगल किस राज्य का फ़सल-उत्सव है?",
  ["Tamil Nadu", "Punjab", "Assam", "West Bengal"],
  ["तमिलनाडु", "पंजाब", "असम", "पश्चिम बंगाल"],
  0,
  "Pongal, celebrated in mid-January in the Tamil month of Thai, gives thanks to the sun and to cattle for the harvest; it is named after the sweet rice dish boiled until it overflows. It coincides with Makar Sankranti, Lohri in Punjab, Magh Bihu in Assam and Poush Sankranti in West Bengal -- the other options.",
  "तमिल माह थाई में जनवरी के मध्य में मनाया जाने वाला पोंगल फ़सल के लिए सूर्य और मवेशियों का आभार मानता है; इसका नाम उस मीठे चावल पर है जिसे उबलकर बाहर छलकने तक पकाया जाता है। यह मकर संक्रांति, पंजाब में लोहड़ी, असम में माघ बिहू और पश्चिम बंगाल में पौष संक्रांति के साथ पड़ता है, जो बाकी विकल्प हैं।",
  f"{CCRT} -- fairs and festivals of India.",
  "culture-pongal-tamil-nadu")

M(CO, "hard", "'Thang-ta', a traditional martial art that uses the sword and the spear, belongs to:",
  "तलवार और भाले का उपयोग करने वाली पारंपरिक युद्ध-कला 'थांग-ता' कहाँ की है?",
  ["Manipur", "Kerala", "Tamil Nadu", "Punjab"],
  ["मणिपुर", "केरल", "तमिलनाडु", "पंजाब"],
  0,
  "Thang-ta ('sword and spear') is the martial art of the Meitei people of Manipur, performed with ritual, breathing techniques and dance-like movement; it is one of the indigenous games included in the Khelo India programme. Kerala's Kalaripayattu, Tamil Nadu's Silambam (staff fighting) and Punjab's Gatka are the other famous traditions.",
  "थांग-ता ('तलवार और भाला') मणिपुर के मैतेई लोगों की युद्ध-कला है, जो अनुष्ठान, श्वास-तकनीकों और नृत्य जैसी गतियों के साथ की जाती है; यह खेलो इंडिया कार्यक्रम में शामिल देसी खेलों में से एक है। केरल का कलरिपयट्टु, तमिलनाडु का सिलंबम (लाठी-युद्ध) और पंजाब का गतका दूसरी प्रसिद्ध परंपराएँ हैं।",
  f"{CCRT}; Ministry of Youth Affairs and Sports -- Khelo India (indigenous games).",
  "culture-thang-ta-manipur")

P(CO, "medium", "Consider the following pairs of weaving traditions and the States they belong to:",
  "बुनाई परंपराओं और उनके राज्यों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Kanjeevaram silk : Tamil Nadu", "Paithani : Maharashtra", "Baluchari : Odisha", "Muga silk : Kerala"],
  ["कांजीवरम रेशम : तमिलनाडु", "पैठणी : महाराष्ट्र", "बालूचरी : ओडिशा", "मूगा रेशम : केरल"],
  1,
  "Only pairs 1 and 2 are correct. Kanjeevaram sarees are woven in Kanchipuram with heavy silk and gold zari, and Paithani, from Paithan near Aurangabad, is known for its peacock borders. "
  "Pair 3 is wrong: Baluchari sarees, whose pallus show scenes from the epics, come from Bishnupur and Murshidabad in West Bengal. Pair 4 is wrong: Muga, the golden silk produced only in the Brahmaputra valley, is from Assam and has a GI tag.",
  "केवल युग्म 1 और 2 सही हैं। कांजीवरम साड़ियाँ कांचीपुरम में भारी रेशम और सुनहरी ज़री से बुनी जाती हैं, और औरंगाबाद के पास पैठण की पैठणी अपनी मोर वाली किनारियों के लिए जानी जाती है। "
  "युग्म 3 गलत है: पल्लू पर महाकाव्यों के दृश्य दिखाने वाली बालूचरी साड़ियाँ पश्चिम बंगाल के बिष्णुपुर और मुर्शिदाबाद से आती हैं। युग्म 4 गलत है: केवल ब्रह्मपुत्र घाटी में बनने वाला सुनहरा रेशम मूगा असम का है और इसके पास GI टैग है।",
  f"{GI}; {CCRT} -- textile traditions.",
  "culture-weaving-traditions-pairs")

if __name__ == "__main__":
    write("hist_l2_t8_icon_culture.sql")
