# -*- coding: utf-8 -*-
"""Level 2 · Test 8 (History 4: Art & Culture) -- depth audit of 2026-10-04, part B: Iconography and
Painting (docs/upsc-question-design-standard.md §6). Part A has Architecture and Culture-Other; part C has
Music & Dance and the tags for the kept rows.

Part B rewrites 20 rows in place with the same concept id, type and difficulty:
  - iconography now asks a student to identify a deity from its attributes, to read what an image
    expresses (Harihara, the Nataraja, Vajrapani as Heracles), why Brahma has so few temples, why images
    look alike across centuries, and to judge a five-item list of Bodhisattvas;
  - painting now asks what a tradition shows or does (Ajanta as a source on society, the Phad as a
    portable shrine, Gond art moving onto canvas, Madhubani after the drought of the 1960s), technique
    pairs, and a five-item list of Bihar's folk traditions.
Leaks avoided while drafting:
  - ragas tied to a time of day (answers the raga-and-tala row);
  - Kalamkari in the technique pairs (would knock out a distractor in the Kalamkari MCQ);
  - Nandi and the swan in the iconography options (answer the vahana rows);
  - the Agamas as cast-in-one-mould canons (contradicted by the kept Chola bronze row)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write_updates, CODE
from polity_common import C3, C4, T2

d.SUBJECT = "History"
d.REQUIRE_CRAFT = True
ICO = "Iconography"
PNT = "Painting"
NFA = "NCERT Class XI, An Introduction to Indian Art"
NLH = "NCERT Class XII, Living Craft Traditions of India"
FIVE = ["Only two", "Only three", "Only four", "All five"]
FIVE_HI = ["केवल दो", "केवल तीन", "केवल चार", "सभी पाँच"]

# ================================================================ ICONOGRAPHY: MCQs (4)
M(ICO, "hard", "Images of Harihara, in which one half of the figure is Vishnu and the other half Shiva, are best read as expressing:",
  "हरिहर की प्रतिमाएँ, जिनमें आकृति का आधा भाग विष्णु और आधा शिव है, सबसे अच्छी तरह किसकी अभिव्यक्ति मानी जाती हैं?",
  ["an attempt to reconcile the Vaishnava and Shaiva traditions by showing their gods as one",
   "the victory of the Shaiva tradition over the Vaishnava one in a particular region of the south",
   "a Buddhist borrowing in which two Bodhisattvas were joined in a single figure",
   "a royal portrait in which a king was shown as part god and part human"],
  ["वैष्णव और शैव परंपराओं के देवताओं को एक दिखाकर उनमें मेल कराने का प्रयास",
   "दक्षिण के किसी क्षेत्र विशेष में वैष्णव परंपरा पर शैव परंपरा की विजय",
   "एक बौद्ध उधार, जिसमें दो बोधिसत्वों को एक ही आकृति में जोड़ा गया",
   "एक राजकीय चित्र, जिसमें राजा को आधा देवता और आधा मनुष्य दिखाया गया"],
  0,
  "In Harihara images the Vishnu half carries his crown, conch or discus, and the Shiva half his matted hair, trident and serpent, so the viewer sees two great gods as aspects of one divinity. They appear from the Gupta and early Chalukya periods -- the relief in Cave 1 at Badami is well known -- and in Cambodia, at a time when the two sects competed for followers and patronage. "
  "The same idea of unity in a composite form appears in Ardhanarishvara, half Shiva and half Parvati.",
  "हरिहर प्रतिमाओं में विष्णु का आधा भाग उनका मुकुट, शंख या चक्र और शिव का आधा भाग उनकी जटा, त्रिशूल और सर्प धारण करता है, जिससे दर्शक दो बड़े देवताओं को एक ही दिव्यता के पहलू के रूप में देखता है। ये गुप्त और प्रारंभिक चालुक्य कालों से मिलती हैं, बादामी की गुफा 1 का फलक प्रसिद्ध है, और कंबोडिया में भी, उस समय जब दोनों संप्रदाय अनुयायियों और संरक्षण के लिए होड़ में थे। "
  "एक संयुक्त रूप में एकता का यही विचार अर्धनारीश्वर में दिखता है, जो आधे शिव और आधी पार्वती हैं।",
  NFA, "art-harihara", craft="inference")

M(ICO, "medium", "Brahma is the creator in the Hindu triad, yet he has very few temples of his own, Pushkar being the best known. This is usually linked to:",
  "ब्रह्मा हिंदू त्रिदेव में सृष्टिकर्ता हैं, फिर भी उनके अपने बहुत कम मंदिर हैं, जिनमें पुष्कर सबसे प्रसिद्ध है। इसे प्रायः किससे जोड़ा जाता है?",
  ["the rise of devotional cults centred on Vishnu and Shiva, which overshadowed him",
   "a ban on the worship of Brahma imposed by the Gupta emperors",
   "the fact that Brahma is a Buddhist deity who was adopted only late into Hindu worship",
   "the destruction of all his temples during the Turkish invasions"],
  ["विष्णु और शिव पर केंद्रित भक्ति संप्रदायों के उदय से, जिन्होंने उन्हें पीछे छोड़ दिया",
   "गुप्त सम्राटों द्वारा ब्रह्मा की पूजा पर लगाए गए प्रतिबंध से",
   "इस तथ्य से कि ब्रह्मा एक बौद्ध देवता हैं जिन्हें हिंदू पूजा में देर से अपनाया गया",
   "तुर्क आक्रमणों के दौरान उनके सभी मंदिरों के नष्ट होने से"],
  0,
  "As bhakti grew around Vishnu, Shiva and the Goddess, temples and sects formed around them, while Brahma remained important mainly in creation myths and as a figure in the temples of others, often shown with four faces, a beard, the Vedas, a water pot and a rosary. Puranic legends -- of a curse, or of his lie in the Lingodbhava story -- are often told to explain why he is not worshipped widely. "
  "No such ban existed, and Brahma is a Vedic-Puranic god; Buddhist texts include him only as a lesser deity.",
  "जैसे-जैसे विष्णु, शिव और देवी के इर्द-गिर्द भक्ति बढ़ी, उनके इर्द-गिर्द मंदिर और संप्रदाय बने, जबकि ब्रह्मा मुख्यतः सृष्टि-कथाओं में और दूसरों के मंदिरों में एक आकृति के रूप में महत्वपूर्ण रहे, प्रायः चार मुख, दाढ़ी, वेद, कमंडलु और माला के साथ। उनकी व्यापक पूजा न होने की व्याख्या के लिए प्रायः पौराणिक कथाएँ, जैसे किसी शाप की, या लिंगोद्भव कथा में उनके झूठ की, सुनाई जाती हैं। "
  "ऐसा कोई प्रतिबंध नहीं था, और ब्रह्मा वैदिक-पौराणिक देवता हैं; बौद्ध ग्रंथ उन्हें केवल एक छोटे देवता के रूप में शामिल करते हैं।",
  NFA, "art-brahma-chaturmukha", craft="inference")

M(ICO, "medium", "The Chola bronze of Shiva as Nataraja is read as an image of the cosmic cycle mainly because:",
  "नटराज रूप में शिव की चोल कांस्य प्रतिमा को ब्रह्मांडीय चक्र का प्रतीक मुख्यतः इसलिए माना जाता है कि:",
  ["he dances in a ring of fire, holding the drum of creation and the flame that ends it",
   "it was carried into battle as the war standard of the Chola armies",
   "it shows Shiva seated with Parvati and their son Skanda as a royal family",
   "it was cast from a single block of gold to display the wealth and power of the Chola kingdom"],
  ["वे अग्नि-वलय में नृत्य करते हैं, सृष्टि का डमरू और संहार की ज्वाला धारण किए",
   "इसे चोल सेनाओं की युद्ध-पताका के रूप में युद्ध में ले जाया जाता था",
   "यह शिव को पार्वती और उनके पुत्र स्कंद के साथ एक राजपरिवार के रूप में बैठे दिखाती है",
   "इसे चोल राज्य की संपत्ति और शक्ति दिखाने के लिए सोने के एक ही खंड से ढाला गया था"],
  0,
  "In the Nataraja image Shiva dances the ananda tandava within a ring of flames: one hand holds the damaru, whose beat begins creation, another the fire that ends it; a third is raised in the gesture of protection, and he stands on a dwarf who stands for ignorance, with the raised foot offering release. The image, perfected in Chola bronzes of the tenth and eleventh centuries, sums up creation, preservation, destruction, concealment and grace. "
  "The family group of Shiva, Parvati and Skanda is a different Chola bronze, the Somaskanda; the Nataraja was a processional image carried in temple festivals, not a war standard, and it is cast in bronze.",
  "नटराज प्रतिमा में शिव अग्नि-शिखाओं के वलय में आनंद तांडव करते हैं: एक हाथ में डमरू है, जिसकी ताल से सृष्टि आरंभ होती है, दूसरे में वह अग्नि जो उसका अंत करती है; तीसरा हाथ रक्षा की मुद्रा में उठा है, और वे अज्ञान के प्रतीक एक बौने पर खड़े हैं, जबकि उठा हुआ पैर मुक्ति देता है। दसवीं और ग्यारहवीं सदी के चोल कांस्यों में पूर्ण हुई यह प्रतिमा सृष्टि, स्थिति, संहार, तिरोभाव और अनुग्रह का सार है। "
  "शिव, पार्वती और स्कंद का परिवार-समूह एक अलग चोल कांस्य, सोमास्कंद, है; नटराज मंदिर-उत्सवों में ले जाई जाने वाली उत्सव-प्रतिमा थी, युद्ध-पताका नहीं, और वह कांसे में ढली है।",
  NFA, "art-culture-nataraja-chola-bronze", craft="linkage")

M(ICO, "medium", "In Gandhara reliefs, Vajrapani, the thunderbolt-bearer who stands beside the Buddha, is often shown in the form of the Greek hero Heracles. This best illustrates:",
  "गांधार के फलकों में बुद्ध के पास खड़े वज्रधारी वज्रपाणि को प्रायः यूनानी नायक हेराक्लीज़ के रूप में दिखाया गया है। यह सबसे अच्छी तरह किसे दर्शाता है?",
  ["the blending of Greco-Roman forms with Buddhist themes in the art of the north-west",
   "the conversion of the Greek kings of Bactria to Jainism",
   "the influence of Mughal painting on early Buddhist sculpture",
   "the use of Heracles as a symbol of the Buddha himself before any images of him existed"],
  ["उत्तर-पश्चिम की कला में यूनानी-रोमन रूपों और बौद्ध विषयों के मेल को",
   "बैक्ट्रिया के यूनानी राजाओं के जैन धर्म अपनाने को",
   "प्रारंभिक बौद्ध मूर्तिकला पर मुग़ल चित्रकला के प्रभाव को",
   "बुद्ध की कोई भी प्रतिमा बनने से पहले स्वयं बुद्ध के प्रतीक के रूप में हेराक्लीज़ के उपयोग को"],
  0,
  "Gandhara, under Indo-Greek, Shaka and Kushana rule, sat on routes linking India with Bactria, Iran and the Roman world, so its sculptors gave Buddhist figures Greco-Roman forms: wavy hair, heavy drapery, and a protector modelled on Heracles with his club changed into a thunderbolt. Vajrapani symbolises the Buddha's power and guards him. "
  "Mughal painting is more than a thousand years later, and in the early aniconic phase the Buddha was shown by symbols such as the tree and the wheel, not by a Greek hero.",
  "इंडो-ग्रीक, शक और कुषाण शासन में गांधार भारत को बैक्ट्रिया, ईरान और रोमन संसार से जोड़ने वाले मार्गों पर था, इसलिए उसके मूर्तिकारों ने बौद्ध आकृतियों को यूनानी-रोमन रूप दिए: लहराते बाल, भारी वस्त्र, और हेराक्लीज़ के आदर्श पर बना एक रक्षक, जिसकी गदा वज्र में बदल गई। वज्रपाणि बुद्ध की शक्ति का प्रतीक है और उनकी रक्षा करता है। "
  "मुग़ल चित्रकला एक हज़ार वर्ष से अधिक बाद की है, और प्रारंभिक अप्रतीकात्मक चरण में बुद्ध को यूनानी नायक से नहीं, वृक्ष और चक्र जैसे प्रतीकों से दिखाया जाता था।",
  NFA, "art-vajrapani", craft="linkage")

# ================================================================ ICONOGRAPHY: statements (6)
S(ICO, "easy", "Consider the following statements about Jain images:",
  "जैन प्रतिमाओं के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The 'kayotsarga' posture, standing upright with arms hanging straight at the sides, expresses complete detachment from the body.",
   "Digambara images show the Tirthankaras unclothed, in keeping with that sect's view that monks must give up all clothing.",
   "The colossal statue of Gommateshwara at Shravanabelagola depicts Mahavira."],
  ["'कायोत्सर्ग' मुद्रा, यानी भुजाएँ सीधी नीचे लटकाकर सीधे खड़े होना, शरीर से पूर्ण विरक्ति को व्यक्त करती है।",
   "दिगंबर प्रतिमाएँ तीर्थंकरों को निर्वस्त्र दिखाती हैं, उस संप्रदाय के इस मत के अनुसार कि भिक्षुओं को सभी वस्त्र त्यागने चाहिए।",
   "श्रवणबेलगोला की गोम्मटेश्वर की विशाल प्रतिमा महावीर की है।"],
  C3, 1,
  "Statements 1 and 2 are correct. In kayotsarga the figure stands motionless, often with creepers climbing its legs, showing indifference to the body in deep meditation; the other main posture is seated in meditation. Digambara images are nude, while Svetambara images are shown clothed and often adorned. "
  "Statement 3 is wrong: the 57-foot monolith at Shravanabelagola, set up in about 983 by the Ganga minister Chavundaraya, depicts Bahubali, son of the first Tirthankara Rishabhadeva, who is shown in kayotsarga with creepers on his limbs.",
  "कथन 1 और 2 सही हैं। कायोत्सर्ग में आकृति निश्चल खड़ी रहती है, प्रायः पैरों पर लताएँ चढ़ी होती हैं, जो गहन ध्यान में शरीर के प्रति उदासीनता दिखाती हैं; दूसरी मुख्य मुद्रा ध्यान में बैठी है। दिगंबर प्रतिमाएँ निर्वस्त्र होती हैं, जबकि श्वेतांबर प्रतिमाएँ वस्त्रयुक्त और प्रायः अलंकृत दिखाई जाती हैं। "
  "कथन 3 गलत है: लगभग 983 में गंग मंत्री चामुंडराय द्वारा स्थापित श्रवणबेलगोला की 57 फ़ुट की एकाश्म प्रतिमा पहले तीर्थंकर ऋषभदेव के पुत्र बाहुबली की है, जिन्हें अंगों पर लताओं के साथ कायोत्सर्ग में दिखाया गया है।",
  NFA, "art-jain-images-kayotsarga-bahubali", craft="linkage")

S(ICO, "hard", "Images of the same deity made centuries apart, in different regions, often share very similar proportions and attributes. Consider the following statements:",
  "एक ही देवता की, सदियों के अंतर पर और अलग-अलग क्षेत्रों में बनी प्रतिमाओं के अनुपात और लक्षण प्रायः बहुत मिलते-जुलते होते हैं। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The canons of talamana, which fix proportions in units of the face length, help explain this.",
   "The Agamas are Buddhist texts on monastic discipline that laid down these rules.",
   "It shows that sculptors were forbidden to bring any regional style of their own to their work."],
  ["तालमान के नियम, जो मुख की लंबाई की इकाइयों में अनुपात तय करते हैं, इसकी व्याख्या में सहायक हैं।",
   "आगम भिक्षु-अनुशासन पर बौद्ध ग्रंथ हैं जिन्होंने ये नियम दिए।",
   "यह दिखाता है कि मूर्तिकारों को अपने काम में कोई क्षेत्रीय शैली लाने की मनाही थी।"],
  C3, 0,
  "Only statement 1 follows. Under talamana the length of the face (tala) is the unit, and gods, humans and demons are given different numbers of talas, so a sculptor trained in the canon anywhere would reach similar proportions; the attributes and gestures of each deity were fixed in the same way. "
  "Statement 2 is wrong: the Agamas are Shaiva, Vaishnava and Shakta texts on temple worship which, with the Shilpa Shastras, set out the forms of images. Statement 3 does not follow: within the canon regional schools flourished, which is why a Chola, a Hoysala and a Pala image of the same god are easy to tell apart.",
  "केवल कथन 1 निकलता है। तालमान में मुख (ताल) की लंबाई इकाई है, और देवताओं, मनुष्यों तथा असुरों को अलग-अलग ताल दिए जाते हैं, इसलिए इस नियम में प्रशिक्षित मूर्तिकार कहीं भी मिलते-जुलते अनुपात तक पहुँचता; हर देवता के लक्षण और मुद्राएँ भी इसी तरह तय थीं। "
  "कथन 2 गलत है: आगम मंदिर-पूजा पर शैव, वैष्णव और शाक्त ग्रंथ हैं, जिन्होंने शिल्पशास्त्रों के साथ प्रतिमाओं के रूप तय किए। कथन 3 नहीं निकलता: नियम के भीतर क्षेत्रीय शैलियाँ फलीं, इसीलिए एक ही देवता की चोल, होयसल और पाल प्रतिमा को पहचानना आसान है।",
  NFA, "art-image-making-texts-talamana", craft="inference")

S(ICO, "medium", "Consider the following figures of Buddhist art:",
  "बौद्ध कला की निम्नलिखित आकृतियों पर विचार कीजिए:",
  ["Avalokiteshvara", "Manjushri", "Maitreya", "Kshitigarbha", "Ananda"],
  ["अवलोकितेश्वर", "मंजुश्री", "मैत्रेय", "क्षितिगर्भ", "आनंद"],
  None, 2,
  "Four of them are Bodhisattvas. Avalokiteshvara, the Bodhisattva of compassion, often holds a lotus (as Padmapani, painted in Ajanta Cave 1); Manjushri, of wisdom, holds a sword that cuts through ignorance; Maitreya, the Buddha of the future, often holds a water flask; and Kshitigarbha, popular in East Asia, vows to help beings in the hells. "
  "Ananda was the Buddha's cousin and chief attendant, a disciple who recited the discourses at the First Council, not a Bodhisattva.",
  "इनमें से चार बोधिसत्व हैं। करुणा के बोधिसत्व अवलोकितेश्वर प्रायः कमल धारण करते हैं (पद्मपाणि के रूप में, अजंता गुफा 1 में चित्रित); प्रज्ञा के मंजुश्री अज्ञान को काटने वाली तलवार रखते हैं; भविष्य के बुद्ध मैत्रेय प्रायः जल-पात्र रखते हैं; और पूर्वी एशिया में लोकप्रिय क्षितिगर्भ नरक के प्राणियों की सहायता का व्रत लेते हैं। "
  "आनंद बुद्ध के चचेरे भाई और प्रमुख परिचारक थे, एक शिष्य जिन्होंने पहली संगीति में प्रवचनों का पाठ किया, बोधिसत्व नहीं।",
  NFA, "art-bodhisattva-iconography", opts=FIVE, opts_hi=FIVE_HI,
  closing="How many of the above are Bodhisattvas?", closing_hi="उपर्युक्त में से कितने बोधिसत्व हैं?", craft="multi")

S(ICO, "medium", "An image shows a goddess seated on a lotus while two elephants pour water over her from pots held in their trunks. Consider the following statements:",
  "एक प्रतिमा में एक देवी कमल पर बैठी हैं और दो हाथी अपनी सूँड़ में पकड़े घड़ों से उन पर जल डाल रहे हैं। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The goddess is Gajalakshmi, a form of Lakshmi.",
   "Such images appear as early as the gateways of the Buddhist stupa at Sanchi.",
   "The elephants pouring water stand for abundance and for royal consecration (abhisheka)."],
  ["देवी गजलक्ष्मी हैं, जो लक्ष्मी का एक रूप है।",
   "ऐसी प्रतिमाएँ सांची के बौद्ध स्तूप के तोरणों जितनी पुरानी हैं।",
   "जल डालते हाथी समृद्धि और राजकीय अभिषेक के प्रतीक हैं।"],
  C3, 2,
  "All three are correct. Gajalakshmi is among the oldest goddess images in India: she appears on the gateways and railings of Sanchi and Bharhut and on early coins, long before Lakshmi had temples of her own, which shows that such auspicious symbols were shared across Buddhist and Brahmanical art. "
  "The lotus and the water-pouring elephants stand for fertility, wealth and the consecration of a ruler, which is why the motif also appears over doorways and on royal seals.",
  "तीनों कथन सही हैं। गजलक्ष्मी भारत की सबसे पुरानी देवी-प्रतिमाओं में हैं: वे सांची और भरहुत के तोरणों और वेदिकाओं पर तथा प्रारंभिक सिक्कों पर दिखती हैं, लक्ष्मी के अपने मंदिरों से बहुत पहले, जो दिखाता है कि ऐसे मंगल प्रतीक बौद्ध और ब्राह्मणवादी कला में साझा थे। "
  "कमल और जल डालते हाथी उर्वरता, धन और शासक के अभिषेक के प्रतीक हैं, इसीलिए यह अलंकरण द्वारों के ऊपर और राजकीय मुहरों पर भी मिलता है।",
  NFA, "art-goddess-iconography", craft="application")

S(ICO, "medium", "Consider the following images:",
  "निम्नलिखित प्रतिमाओं पर विचार कीजिए:",
  ["A figure seated under a banyan tree, teaching sages in silence, placed in a niche on the south wall of a temple",
   "A figure emerging from a pillar of fire whose top and bottom Brahma and Vishnu cannot find",
   "A figure reclining on a coiled serpent, with Brahma seated on a lotus that rises from his navel"],
  ["बरगद के नीचे बैठी, मौन रहकर ऋषियों को उपदेश देती, मंदिर की दक्षिणी दीवार के एक आले में रखी आकृति",
   "अग्नि-स्तंभ से निकलती आकृति, जिसके शीर्ष और तल ब्रह्मा और विष्णु नहीं खोज पाते",
   "कुंडली मारे सर्प पर लेटी आकृति, जिसकी नाभि से निकले कमल पर ब्रह्मा बैठे हैं"],
  C3, 1,
  "Two of the images show Shiva. Dakshinamurti ('facing south'), Shiva as the supreme teacher, is placed on the south wall of Tamil temples and sits under a banyan tree with sages at his feet; Lingodbhava shows Shiva appearing from an endless column of fire while Brahma, as a swan, and Vishnu, as a boar, search in vain for its ends -- a story of Shiva's supremacy. "
  "The third is Vishnu as Anantashayana, reclining on the serpent Shesha between cycles of creation, as in the famous panel at Deogarh.",
  "दो प्रतिमाएँ शिव को दिखाती हैं। दक्षिणामूर्ति ('दक्षिणमुखी'), परम गुरु के रूप में शिव, तमिल मंदिरों की दक्षिणी दीवार पर रखे जाते हैं और बरगद के नीचे चरणों में ऋषियों के साथ बैठे होते हैं; लिंगोद्भव शिव को अनंत अग्नि-स्तंभ से प्रकट होते दिखाता है, जबकि हंस रूप में ब्रह्मा और वराह रूप में विष्णु उसके छोर व्यर्थ खोजते हैं, यह शिव की सर्वोच्चता की कथा है। "
  "तीसरी प्रतिमा अनंतशयन विष्णु की है, जो सृष्टि के चक्रों के बीच शेषनाग पर लेटे हैं, जैसा देवगढ़ के प्रसिद्ध फलक में है।",
  NFA, "art-shiva-forms-dakshinamurti-lingodbhava", closing="In how many of the above is Shiva shown?",
  closing_hi="उपर्युक्त में से कितनी प्रतिमाओं में शिव दिखाए गए हैं?", craft="application")

S(ICO, "medium", "An image shows a four-armed god holding a conch, a discus, a mace and a lotus. Consider the following statements:",
  "एक प्रतिमा में चार भुजाओं वाले एक देवता शंख, चक्र, गदा और कमल धारण किए हैं। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The god is Vishnu.",
   "If he were shown as a boar lifting the Earth goddess from the waters, the form would be Narasimha.",
   "If he were shown holding a trident, a drum and a deer, the form would be Narasimha."],
  ["देवता विष्णु हैं।",
   "यदि उन्हें जल से पृथ्वी देवी को उठाते वराह के रूप में दिखाया जाता, तो वह रूप नरसिंह होता।",
   "यदि उन्हें त्रिशूल, डमरू और मृग धारण किए दिखाया जाता, तो वह रूप नरसिंह होता।"],
  C3, 0,
  "Only statement 1 is correct. The conch (shankha), discus (chakra), mace (gada) and lotus (padma) are Vishnu's four standard attributes. "
  "Statement 2 names the wrong avatar: the boar rescuing the Earth is Varaha, as in the great panel at Udayagiri; Narasimha is half man, half lion. Statement 3 is wrong: the trident, drum (damaru), axe and deer are attributes of Shiva, not of any form of Vishnu.",
  "केवल कथन 1 सही है। शंख, चक्र, गदा और पद्म विष्णु के चार मानक लक्षण हैं। "
  "कथन 2 ग़लत अवतार बताता है: पृथ्वी को बचाने वाला वराह है, जैसा उदयगिरि के बड़े फलक में है; नरसिंह आधे मनुष्य, आधे सिंह हैं। कथन 3 गलत है: त्रिशूल, डमरू, परशु और मृग शिव के लक्षण हैं, विष्णु के किसी रूप के नहीं।",
  NFA, "art-vishnu-iconography", craft="application")

# ================================================================ PAINTING (10)
P(PNT, "medium", "Consider the following pairs of painting traditions and the materials or techniques they use:",
  "निम्नलिखित चित्रकला परंपराओं और उनके द्वारा प्रयुक्त सामग्री या तकनीक के युग्मों पर विचार कीजिए:",
  ["Pattachitra : Painted on cloth stiffened with gum and chalk",
   "Warli : White figures painted with rice paste on mud walls",
   "Pithora : Ritual paintings on the walls of homes of the Rathwa and Bhil communities",
   "Madhubani : Carved in relief on wooden panels"],
  ["पट्टचित्र : गोंद और खड़िया से कड़े किए कपड़े पर चित्रित",
   "वारली : मिट्टी की दीवारों पर चावल के लेप से बनाई गई सफ़ेद आकृतियाँ",
   "पिथोरा : राठवा और भील समुदायों के घरों की दीवारों पर अनुष्ठानिक चित्र",
   "मधुबनी : लकड़ी के फलकों पर उभरी नक़्क़ाशी"],
  2,
  "Three pairs are correct. Pattachitra of Odisha is painted on cloth stiffened with gum and chalk, for the Jagannath tradition; Warli painters of Maharashtra draw stick-like figures in white rice paste on red-brown mud walls; and Pithora, painted on the walls of Rathwa and Bhil homes in Gujarat and Madhya Pradesh, is commissioned as a ritual offering to the god Pithora. "
  "Pair 4 is wrong: Madhubani is a painting, not a carving -- done with brushes, twigs and fingers on walls, floors and, later, paper.",
  "तीन युग्म सही हैं। ओडिशा का पट्टचित्र जगन्नाथ परंपरा के लिए गोंद और खड़िया से कड़े किए कपड़े पर चित्रित होता है; महाराष्ट्र के वारली चित्रकार लाल-भूरी मिट्टी की दीवारों पर चावल के सफ़ेद लेप से तीली जैसी आकृतियाँ बनाते हैं; और गुजरात तथा मध्य प्रदेश में राठवा और भील घरों की दीवारों पर बनने वाला पिथोरा देवता पिथोरा को अनुष्ठानिक भेंट के रूप में बनवाया जाता है। "
  "युग्म 4 गलत है: मधुबनी नक़्क़ाशी नहीं, चित्रकला है, जो दीवारों, फ़र्श और बाद में काग़ज़ पर ब्रश, टहनियों और उँगलियों से बनाई जाती है।",
  NLH, "art-culture-painting-traditions-states-pairs", craft="linkage")

M(PNT, "hard", "Which of the following folk painting traditions belong to Bihar?\n1. Manjusha\n2. Madhubani\n3. Tikuli\n4. Pattachitra\n5. Warli\nSelect the correct answer using the code given below.",
  "निम्नलिखित में से कौन-सी लोक चित्रकला परंपराएँ बिहार की हैं?\n1. मंजूषा\n2. मधुबनी\n3. टिकुली\n4. पट्टचित्र\n5. वारली\nनीचे दिए गए कूट का प्रयोग कर सही उत्तर चुनिए।",
  ["1, 2 and 3 only", "1 and 2 only", "2, 3 and 4 only", "1, 2, 3 and 5"],
  ["केवल 1, 2 और 3", "केवल 1 और 2", "केवल 2, 3 और 4", "1, 2, 3 और 5"],
  0,
  "Three of them are from Bihar. Manjusha art of the Bhagalpur (Anga) region is painted on box-like temples of jute and paper for the worship of the snake goddess Bishahari and tells the tale of Bihula; Madhubani comes from Mithila; and Tikuli, from Patna, began as painted glass bindis and is now done in enamel on hardboard. "
  "Pattachitra belongs to Odisha (with a related scroll tradition in Bengal), and Warli to the tribal communities of Maharashtra's Palghar region.",
  "इनमें से तीन बिहार की हैं। भागलपुर (अंग) क्षेत्र की मंजूषा कला जूट और काग़ज़ के डिब्बेनुमा मंदिरों पर सर्प देवी बिषहरी की पूजा के लिए बनाई जाती है और बिहुला की कथा कहती है; मधुबनी मिथिला की है; और पटना की टिकुली कला चित्रित काँच की बिंदियों से शुरू हुई और अब हार्डबोर्ड पर इनैमल से की जाती है। "
  "पट्टचित्र ओडिशा का है (बंगाल में इससे जुड़ी पट-परंपरा के साथ), और वारली महाराष्ट्र के पालघर क्षेत्र के आदिवासी समुदायों की।",
  NLH, "art-manjusha-bihar", craft="multi")

M(PNT, "medium", "The Ajanta murals, though Buddhist in theme, are also valued as a source on the society of their time mainly because:",
  "अजंता के भित्तिचित्र, यद्यपि विषय में बौद्ध हैं, अपने समय के समाज के स्रोत के रूप में भी मुख्यतः इसलिए मूल्यवान हैं कि:",
  ["their stories are set among palaces and streets that show the dress and daily life of the time",
   "they record the names and the dates of accession of every king of the Vakataka and Gupta dynasties",
   "they were painted by Chinese pilgrims who described Indian society as they saw it",
   "they are maps of the trade routes that ran through the western Deccan"],
  ["उनकी कथाएँ महलों और गलियों के बीच घटती हैं, जो उस समय के वस्त्र और दैनिक जीवन दिखाते हैं",
   "वे वाकाटक और गुप्त वंशों के हर राजा के नाम और राज्यारोहण की तिथियाँ दर्ज करते हैं",
   "उन्हें चीनी यात्रियों ने चित्रित किया जिन्होंने भारतीय समाज को जैसा देखा वैसा दिखाया",
   "वे पश्चिमी दक्कन से होकर जाने वाले व्यापार मार्गों के मानचित्र हैं"],
  0,
  "The murals of the fifth century, made largely under Vakataka patronage, tell the Jataka tales and the Buddha's life, but they set them in a richly imagined world of kings and queens, musicians and dancers, merchants, foreigners, houses and animals, so they show costume, ornament, architecture and manners. "
  "They were painted in a tempera technique on dry plaster by Indian artists for the monks, and they name no dynasty of kings in sequence.",
  "पाँचवीं सदी के, मुख्यतः वाकाटक संरक्षण में बने भित्तिचित्र जातक कथाएँ और बुद्ध का जीवन बताते हैं, पर उन्हें राजाओं-रानियों, संगीतकारों और नर्तकियों, व्यापारियों, विदेशियों, घरों और पशुओं के समृद्ध काल्पनिक संसार में रखते हैं, इसलिए वे वेशभूषा, आभूषण, स्थापत्य और रीति-रिवाज़ दिखाते हैं। "
  "उन्हें भारतीय कलाकारों ने भिक्षुओं के लिए सूखे प्लास्टर पर टेम्परा तकनीक से चित्रित किया, और वे राजाओं के किसी वंश का क्रमवार नाम नहीं देते।",
  NFA, "art-culture-ajanta-murals-jataka", craft="inference")

M(PNT, "medium", "Gond art, which fills vivid figures of animals, trees and spirits with dots and dashes, moved from the walls and floors of village homes onto paper and canvas from the 1980s, through artists such as Jangarh Singh Shyam. This mainly:",
  "जानवरों, पेड़ों और आत्माओं की जीवंत आकृतियों को बिंदुओं और रेखाओं से भरने वाली गोंड कला 1980 के दशक से जनगढ़ सिंह श्याम जैसे कलाकारों के माध्यम से गाँव के घरों की दीवारों और फ़र्श से काग़ज़ और कैनवस पर आई। इसका मुख्य परिणाम था:",
  ["carried a ritual wall art of the Pardhan Gonds into galleries and the wider art market",
   "turned Gond art into a court style patronised by the rulers of Mysore",
   "made Gond art the official style for decorating government buildings across central India",
   "ended the practice of Gond painting in the villages of its origin"],
  ["पारधान गोंडों की एक अनुष्ठानिक भित्ति-कला को दीर्घाओं और व्यापक कला बाज़ार तक पहुँचाया",
   "गोंड कला को मैसूर के शासकों द्वारा संरक्षित दरबारी शैली बना दिया",
   "गोंड कला को पूरे मध्य भारत में सरकारी इमारतों की सजावट की आधिकारिक शैली बना दिया",
   "मूल गाँवों में गोंड चित्रकला की प्रथा को समाप्त कर दिया"],
  0,
  "Jangarh Singh Shyam, a Pardhan Gond from Patangarh in Mandla district of Madhya Pradesh, was encouraged by Bharat Bhavan in Bhopal to paint on paper and canvas; his work, and that of the many artists who followed, made 'Jangarh kalam' known in India and abroad. "
  "The tradition still lives in its villages, where homes are painted for festivals, while the new medium gave painters an income and a name.",
  "मध्य प्रदेश के मंडला ज़िले के पाटनगढ़ के पारधान गोंड जनगढ़ सिंह श्याम को भोपाल के भारत भवन ने काग़ज़ और कैनवस पर चित्र बनाने के लिए प्रोत्साहित किया; उनके और उनके बाद आए अनेक कलाकारों के काम ने 'जनगढ़ कलम' को भारत और विदेश में प्रसिद्ध किया। "
  "परंपरा अपने गाँवों में अब भी जीवित है, जहाँ त्योहारों पर घर रँगे जाते हैं, जबकि नए माध्यम ने चित्रकारों को आय और पहचान दी।",
  NLH, "art-gond-painting", craft="linkage")

M(PNT, "medium", "A Phad scroll is unrolled at night by a bhopa, a priest-singer, who sings the epic of the folk deity Pabuji in front of it. This shows that the Phad works mainly as:",
  "फड़ चित्र को रात में एक भोपा, यानी पुजारी-गायक, खोलता है, जो उसके सामने लोक देवता पाबूजी का महाकाव्य गाता है। इससे पता चलता है कि फड़ मुख्यतः किस रूप में काम करता है?",
  ["a portable shrine and a visual guide to a sung epic",
   "a royal record of victories kept in the treasury",
   "a pilgrim's map showing the route to the deity's temple",
   "a decorative hanging made mainly for sale to visitors"],
  ["एक चलित देवालय और गाए जाने वाले महाकाव्य के दृश्य मार्गदर्शक के रूप में",
   "ख़ज़ाने में रखे जाने वाले विजयों के राजकीय अभिलेख के रूप में",
   "देवता के मंदिर तक का मार्ग दिखाने वाले तीर्थयात्री के मानचित्र के रूप में",
   "मुख्यतः आगंतुकों को बेचने के लिए बनी सजावटी लटकन के रूप में"],
  0,
  "Phads, long cloth scrolls painted by the Joshi families of Shahpura and Bhilwara in Rajasthan, show the episodes of the epics of Pabuji or Devnarayan. When a bhopa and his wife perform through the night, the lamp is moved to the scene being sung, so the scroll is both the deity's travelling temple and the illustration of the story; a worn-out phad is ritually immersed. "
  "Phads made for the market are a later development.",
  "राजस्थान के शाहपुरा और भीलवाड़ा के जोशी परिवारों द्वारा चित्रित लंबे कपड़े के फड़ पाबूजी या देवनारायण के महाकाव्यों के प्रसंग दिखाते हैं। जब भोपा और उसकी पत्नी रात भर प्रस्तुति देते हैं, तो दीपक गाए जा रहे दृश्य तक ले जाया जाता है, इसलिए फड़ देवता का चलित मंदिर भी है और कथा का चित्रण भी; पुराना पड़ा फड़ अनुष्ठानपूर्वक विसर्जित किया जाता है। "
  "बाज़ार के लिए बने फड़ बाद का विकास हैं।",
  NLH, "art-phad-rajasthan", craft="inference")

S(PNT, "easy", "Consider the following statements about Raja Ravi Varma:",
  "राजा रवि वर्मा के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["His oil paintings of gods and epic heroines, printed cheaply by his lithographic press, shaped how many Indians pictured their deities.",
   "He brought European oil technique and realism to Indian themes.",
   "He belonged to Bengal."],
  ["देवताओं और महाकाव्य की नायिकाओं के उनके तैलचित्रों ने, जो उनके लिथोग्राफ़िक छापेख़ाने से सस्ते में छपे, कई भारतीयों के अपने देवताओं की कल्पना को आकार दिया।",
   "उन्होंने भारतीय विषयों में यूरोपीय तैल तकनीक और यथार्थवाद को लाया।",
   "वे बंगाल के थे।"],
  C3, 1,
  "Statements 1 and 2 are correct. Ravi Varma (1848-1906) painted Shakuntala, Damayanti, Lakshmi and Saraswati with European oil technique and realistic figures, and the press he set up near Bombay in 1894 turned them into cheap prints that hung in homes across India and influenced calendar art and the early cinema's idea of the gods. "
  "Statement 3 is wrong: he was from Kilimanoor in Travancore, in present-day Kerala.",
  "कथन 1 और 2 सही हैं। रवि वर्मा (1848-1906) ने शकुंतला, दमयंती, लक्ष्मी और सरस्वती को यूरोपीय तैल तकनीक और यथार्थवादी आकृतियों में चित्रित किया, और 1894 में बंबई के पास उनके स्थापित छापेख़ाने ने इन्हें सस्ते प्रिंटों में बदल दिया जो पूरे भारत के घरों में टँगे और जिन्होंने कैलेंडर कला तथा प्रारंभिक सिनेमा की देव-कल्पना को प्रभावित किया। "
  "कथन 3 गलत है: वे त्रावणकोर के किलिमानूर, वर्तमान केरल, के थे।",
  NFA, "art-raja-ravi-varma", craft="linkage")

S(PNT, "medium", "Consider the following statements about painting under Jahangir:",
  "जहाँगीर के समय की चित्रकला के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Jahangir's own curiosity about nature is reflected in Ustad Mansur's precise studies of birds and animals.",
   "Portraiture declined in Jahangir's reign.",
   "The painter Abul Hasan worked only at the court of Shah Jahan."],
  ["प्रकृति के प्रति जहाँगीर की अपनी जिज्ञासा उस्ताद मंसूर के पक्षियों और जानवरों के सटीक अध्ययनों में दिखती है।",
   "जहाँगीर के शासनकाल में व्यक्तिचित्रण का पतन हुआ।",
   "चित्रकार अबुल हसन ने केवल शाहजहाँ के दरबार में काम किया।"],
  C3, 0,
  "Only statement 1 is correct. Jahangir, who recorded plants and animals in his memoirs with a naturalist's eye, gave Mansur the title 'Nadir-ul-Asr' (wonder of the age); his zebra, turkey cock and Siberian crane are painted with scientific precision. "
  "Statement 2 is wrong: portraiture flourished under Jahangir, including allegorical portraits of the emperor with haloes, globes and symbolic figures. Statement 3 is wrong: Abul Hasan, called 'Nadir-uz-Zaman', was one of Jahangir's leading painters.",
  "केवल कथन 1 सही है। अपने संस्मरणों में प्रकृतिविज्ञानी की दृष्टि से पौधे और जानवर दर्ज करने वाले जहाँगीर ने मंसूर को 'नादिर-उल-अस्र' (युग का आश्चर्य) की उपाधि दी; उसका ज़ेबरा, टर्की मुर्ग़ा और साइबेरियाई सारस वैज्ञानिक सटीकता से चित्रित हैं। "
  "कथन 2 गलत है: जहाँगीर के समय व्यक्तिचित्रण फला-फूला, जिसमें प्रभामंडल, ग्लोब और प्रतीकात्मक आकृतियों वाले सम्राट के रूपकात्मक चित्र भी थे। कथन 3 गलत है: 'नादिर-उज़-ज़मान' कहलाने वाले अबुल हसन जहाँगीर के प्रमुख चित्रकारों में से थे।",
  NFA, "art-jahangir-painting-mansur", craft="linkage")

S(PNT, "medium", "Consider the following statements about Madhubani (Mithila) painting:",
  "मधुबनी (मिथिला) चित्रकला के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It was long painted by women on the walls and floors of homes for weddings and festivals.",
   "After the drought of 1966-68, its move onto paper for sale gave many women an income.",
   "Its figures are drawn with double outlines and filled with bright colours."],
  ["इसे लंबे समय तक स्त्रियाँ विवाहों और त्योहारों पर घरों की दीवारों और फ़र्श पर बनाती थीं।",
   "1966-68 के सूखे के बाद बिक्री के लिए इसके काग़ज़ पर आने से कई स्त्रियों को आय मिली।",
   "इसकी आकृतियाँ दोहरी रेखाओं से बनाई जाती हैं और चटक रंगों से भरी जाती हैं।"],
  C3, 2,
  "All three are correct. Mithila painting was a household art of women, passed from mother to daughter and painted for rituals such as the kohbar, the wedding chamber. When drought struck the region in the late 1960s, the All India Handicrafts Board encouraged painters to work on paper, and artists such as Sita Devi, Ganga Devi and Mahasundari Devi became known across the world. "
  "Its style uses double outlines, bright natural colours and filled spaces, with scenes from the epics and from nature; it received a GI tag in 2007.",
  "तीनों कथन सही हैं। मिथिला चित्रकला स्त्रियों की घरेलू कला थी, जो माँ से बेटी को मिलती थी और कोहबर, यानी विवाह-कक्ष, जैसे अनुष्ठानों के लिए बनाई जाती थी। जब 1960 के दशक के अंत में क्षेत्र में सूखा पड़ा, तो अखिल भारतीय हस्तशिल्प बोर्ड ने चित्रकारों को काग़ज़ पर काम करने के लिए प्रोत्साहित किया, और सीता देवी, गंगा देवी तथा महासुंदरी देवी जैसी कलाकार संसार भर में जानी गईं। "
  "इसकी शैली में दोहरी रेखाएँ, चटक प्राकृतिक रंग और भरे हुए स्थान होते हैं, जिनमें महाकाव्यों और प्रकृति के दृश्य हैं; इसे 2007 में GI टैग मिला।",
  NLH, "art-madhubani", craft="linkage")

S(PNT, "medium", "Consider the following statements about mural traditions:",
  "भित्तिचित्र परंपराओं के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The ceiling murals of the Veerabhadra temple at Lepakshi belong to the Chola period.",
   "The Bagh cave paintings are in Maharashtra.",
   "Kerala murals are painted on cloth scrolls."],
  ["लेपाक्षी के वीरभद्र मंदिर की छत के भित्तिचित्र चोल काल के हैं।",
   "बाघ गुफा के चित्र महाराष्ट्र में हैं।",
   "केरल के भित्तिचित्र कपड़े के पटों पर बनाए जाते हैं।"],
  C3, 3,
  "None is correct. The great ceiling at Lepakshi in Andhra Pradesh was painted in the sixteenth century, in the Vijayanagara period, and shows epic scenes and the temple's patrons in their fine textiles. The Bagh caves are in Dhar district of Madhya Pradesh; their fifth-sixth-century paintings are close in style to Ajanta's. "
  "Kerala murals, as at the Mattancheri Palace and in temples such as Ettumanoor, are painted on walls in a bold palette of ochres and greens.",
  "कोई भी कथन सही नहीं है। आंध्र प्रदेश के लेपाक्षी की विशाल छत सोलहवीं सदी में, विजयनगर काल में, चित्रित हुई और महाकाव्यों के दृश्य तथा मंदिर के संरक्षकों को उनके महीन वस्त्रों में दिखाती है। बाघ गुफाएँ मध्य प्रदेश के धार ज़िले में हैं; उनके पाँचवीं-छठी सदी के चित्र शैली में अजंता के निकट हैं। "
  "केरल के भित्तिचित्र, जैसे मट्टनचेरी महल और एट्टुमानूर जैसे मंदिरों में, गेरुए और हरे रंगों की प्रबल रंगपट्टिका में दीवारों पर बनाए जाते हैं।",
  NFA, "art-mural-traditions-lepakshi-kerala-bagh", craft="precision")

S(PNT, "medium", "In a ragamala series each raga or ragini is shown as a lover, a god or a hero in a matching mood and setting. Consider the following statements:",
  "रागमाला श्रृंखला में हर राग या रागिनी को एक मिलती-जुलती भावदशा और परिवेश में प्रेमी, देवता या नायक के रूप में दिखाया जाता है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["Such paintings bring music, poetry and painting together in a single image.",
   "The earliest dated Rajasthani ragamala series was painted at the Mughal court in Delhi.",
   "Rajasthani painting developed entirely without Mughal influence."],
  ["ऐसे चित्र संगीत, काव्य और चित्रकला को एक ही चित्र में साथ लाते हैं।",
   "सबसे पुरानी तिथि वाली राजस्थानी रागमाला श्रृंखला दिल्ली के मुग़ल दरबार में बनी।",
   "राजस्थानी चित्रकला मुग़ल प्रभाव के बिना पूरी तरह स्वतंत्र रूप से विकसित हुई।"],
  C3, 0,
  "Only statement 1 is correct. A ragamala page usually carries a verse describing the raga's mood, so the viewer reads, hears and sees the mode at once -- Megh Malhar, for example, with rain clouds and dancing figures. "
  "Statement 2 is wrong: one of the earliest dated series was painted at Chawand in Mewar in 1605 by the artist Nisardi. Statement 3 is wrong: Rajasthani courts such as Bundi, Kota and Kishangarh drew on Mughal portraiture and finish, even as they kept their bold colours and devotional themes.",
  "केवल कथन 1 सही है। रागमाला के पृष्ठ पर प्रायः राग की भावदशा बताने वाला एक पद होता है, जिससे दर्शक उस राग को एक साथ पढ़ता, सुनता और देखता है, जैसे वर्षा के बादलों और नाचती आकृतियों के साथ मेघ मल्हार। "
  "कथन 2 गलत है: सबसे पुरानी तिथि वाली श्रृंखलाओं में से एक 1605 में मेवाड़ के चावंड में चित्रकार निसारदी ने बनाई। कथन 3 गलत है: बूँदी, कोटा और किशनगढ़ जैसे राजस्थानी दरबारों ने अपने चटक रंग और भक्ति-विषय रखते हुए मुग़ल व्यक्तिचित्रण और परिष्कार से भी प्रेरणा ली।",
  NFA, "art-rajasthani-ragamala-mewar", craft="inference")

if __name__ == "__main__":
    write_updates("upg_l2_t08_art_b.sql", statuses=("draft", "published"))
