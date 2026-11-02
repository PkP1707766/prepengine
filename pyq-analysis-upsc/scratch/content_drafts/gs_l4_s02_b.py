# -*- coding: utf-8 -*-
"""Level 4 · Simulator 2 (GS Paper I full mock, Layout B: the 2025 shape) -- part B: History (17)
(upsc_l4_gs_cell_targets.mjs 2).
Every tested proposition was swept against the whole UPSC bank (bank_dump.json after Simulator 1) and no row tests
it: Kumarila and the Mimamsa doctrine of the authorless Veda; Attirampakkam, Lahuradewa, Jwalapuram and Pattanam;
the Gwalior prashasti; the Talagunda inscription; Shortugai, Alamgirpur and Surkotada; the Valabhi canon in
Ardhamagadhi; the diwan-i-kohi; Banda Singh Bahadur; Shah Abdul Latif, Waris Shah and Bulleh Shah; the Landholders'
Society, the Hindustan Republican Association, the Berlin Committee and Jugantar; Mooknayak; the Indian Councils Act, 1892;
Natal Indian Congress and Tolstoy Farm; the women's franchise campaign of 1917-21; Amrita Bazar Patrika; the reserved
and transferred subjects of 1919; Ramman, Mudiyettu, Hojagiri and Cheraw. MCQ keys are pinned (pos)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "History"
d.REQUIRE_CRAFT = True

# ---------------------------------------------------------------- Ancient (AR, hard)
A("Ancient", "hard",
  "Kumarila Bhatta defended the authority of the Vedas against the Buddhist critics of Vedic ritual.",
  "कुमारिल भट्ट ने वैदिक कर्मकांड के बौद्ध आलोचकों के विरुद्ध वेदों के प्रामाण्य का समर्थन किया।",
  "Kumarila belonged to the Purva Mimamsa school, which held the Vedas to be eternal and not composed by any author, human or divine.",
  "कुमारिल पूर्व मीमांसा दर्शन से जुड़े थे, जो वेदों को नित्य और किसी भी रचयिता -- मानव या दैवी -- द्वारा अरचित मानता था।",
  0,
  "Both statements are correct, and Statement II explains Statement I. Purva Mimamsa, systematised in Jaimini's Mimamsa Sutra, set out to interpret the Vedic injunctions on ritual. It held the Veda to be apaurusheya -- eternal and authorless -- so that it is a valid source of knowledge on dharma that no flaw of an author can taint; it needed no creator god, and later Mimamsakas argued against one. "
  "On this ground Kumarila, writing around the seventh century, attacked the Buddhist view that no scripture is authoritative in itself and that ritual has no value, and he is remembered with Shankara as a leading figure in the revival of Vedic orthodoxy. His school (Bhatta) and that of Prabhakara (Guru) are the two main schools of Mimamsa, whose rules of interpretation also shaped later Hindu law.",
  "दोनों कथन सही हैं, और कथन II कथन I की व्याख्या करता है। जैमिनि के मीमांसा सूत्र में व्यवस्थित पूर्व मीमांसा का उद्देश्य कर्मकांड संबंधी वैदिक विधियों की व्याख्या करना था। वह वेद को अपौरुषेय -- नित्य और रचयिता-रहित -- मानती थी, ताकि वह धर्म के विषय में ज्ञान का ऐसा प्रामाणिक स्रोत हो जिसे किसी रचयिता का दोष दूषित न कर सके; उसे किसी स्रष्टा ईश्वर की आवश्यकता नहीं थी, और बाद के मीमांसकों ने उसके विरुद्ध तर्क दिए। "
  "इसी आधार पर लगभग सातवीं सदी में लिखने वाले कुमारिल ने इस बौद्ध मत पर प्रहार किया कि कोई भी शास्त्र अपने-आप में प्रामाणिक नहीं है और कर्मकांड का कोई मूल्य नहीं है, और उन्हें शंकर के साथ वैदिक रूढ़िवाद के पुनरुत्थान के प्रमुख व्यक्ति के रूप में याद किया जाता है। उनका संप्रदाय (भाट्ट) और प्रभाकर का (गुरु) मीमांसा के दो मुख्य संप्रदाय हैं, जिनके व्याख्या-नियमों ने बाद की हिंदू विधि को भी आकार दिया।",
  "Jaimini, Mimamsa Sutra; Kumarila Bhatta, Shlokavarttika; NCERT, Class XII, Themes in Indian History Part I.",
  "l4-s02-his-kumarila-mimamsa-apaurusheya", craft="linkage")

# ---------------------------------------------------------------- Ancient (pairs, hard)
P("Ancient", "hard", "Consider the following pairs of archaeological sites and what they are known for:",
  "पुरातात्त्विक स्थलों और उनकी पहचान के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Attirampakkam : Acheulian stone tools dated to about one and a half million years ago",
   "Lahuradewa : Early evidence of rice in the middle Ganga plain",
   "Jwalapuram : Stone tools found both below and above ash from the Toba super-eruption",
   "Pattanam : A Harappan dockyard"],
  ["अत्तिरमपक्कम : लगभग पंद्रह लाख वर्ष पुराने ऐश्यूलियन पाषाण उपकरण",
   "लहुरादेवा : मध्य गंगा मैदान में चावल के आरंभिक साक्ष्य",
   "ज्वालापुरम : टोबा महाविस्फोट की राख के नीचे और ऊपर दोनों ओर मिले पाषाण उपकरण",
   "पट्टणम : एक हड़प्पाई गोदीवाड़ा"],
  2,
  "Only the first three pairs are correct. Attirampakkam, near Chennai, has given Acheulian handaxes dated to about 1.5 million years ago -- among the oldest known outside Africa -- and later Middle Palaeolithic tools of about 385,000 years ago. Lahuradewa, in Sant Kabir Nagar district of Uttar Pradesh, has given some of the earliest evidence of rice in the Ganga plain, from early village settlement. "
  "At Jwalapuram, in Kurnool district of Andhra Pradesh, stone tools lie both below and above the ash of the Toba eruption in Sumatra, about 74,000 years ago, suggesting that people in India lived through that catastrophe. Pair 4 is wrong: Pattanam, near Kochi in Kerala, is an early historic port with Roman amphorae and other imports, and is often identified with Muziris; the brick basin taken to be a Harappan dockyard is at Lothal in Gujarat.",
  "केवल पहले तीन युग्म सही हैं। चेन्नई के निकट अत्तिरमपक्कम से लगभग 15 लाख वर्ष पुरानी ऐश्यूलियन हस्त-कुल्हाड़ियाँ मिली हैं -- अफ़्रीका के बाहर ज्ञात सबसे पुरानी में से -- और बाद के लगभग 3,85,000 वर्ष पुराने मध्य पुरापाषाण उपकरण भी। उत्तर प्रदेश के संत कबीर नगर ज़िले में लहुरादेवा ने आरंभिक ग्राम-बस्ती से गंगा मैदान में चावल के कुछ सबसे पुराने साक्ष्य दिए हैं। "
  "आंध्र प्रदेश के कुर्नूल ज़िले के ज्वालापुरम में पाषाण उपकरण लगभग 74,000 वर्ष पहले सुमात्रा में हुए टोबा विस्फोट की राख के नीचे और ऊपर दोनों ओर मिले हैं, जिससे लगता है कि भारत में लोग उस आपदा से बचे रहे। युग्म 4 ग़लत है: केरल में कोच्चि के निकट पट्टणम रोमन मद्यकलशों (एम्फ़ोरा) और अन्य आयातित वस्तुओं वाला एक आरंभिक ऐतिहासिक बंदरगाह है, जिसे प्रायः मुज़िरिस माना जाता है; हड़प्पाई गोदीवाड़ा माना जाने वाला ईंटों का बेसिन गुजरात में लोथल में है।",
  "Archaeological Survey of India and Indian Archaeology -- A Review; published excavation reports on Attirampakkam, Lahuradewa, Jwalapuram and Pattanam; NCERT, Class XII, Themes in Indian History Part I.",
  "l4-s02-his-prehistoric-attirampakkam-lahuradewa-jwalapuram-pattanam", craft="precision")

# ---------------------------------------------------------------- Ancient (MCQ, hard)
M("Ancient", "hard",
  "The Gwalior prashasti, which traces the genealogy of the Gurjara-Pratiharas and praises Nagabhata I for defeating invaders from the west, was issued by",
  "गुर्जर-प्रतिहारों की वंशावली देने वाली और पश्चिम से आए आक्रमणकारियों को हराने के लिए नागभट प्रथम की प्रशंसा करने वाली ग्वालियर प्रशस्ति किसके द्वारा जारी की गई थी?",
  ["Mihira Bhoja", "Dharmapala of the Pala dynasty", "Dhruva of the Rashtrakuta dynasty", "Yashovarman of Kannauj"],
  ["मिहिर भोज", "पाल वंश के धर्मपाल", "राष्ट्रकूट वंश के ध्रुव", "कन्नौज के यशोवर्मन"],
  0,
  "The Gwalior prashasti in Sanskrit verse was issued by Mihira Bhoja, the most powerful Gurjara-Pratihara king, who ruled in the ninth century from Kannauj. It traces his line from its founder and praises Nagabhata I for crushing the armies of the mlechchhas -- taken to be the Arabs of Sind, who had advanced into western India in the eighth century -- and records the victories of Vatsaraja and Nagabhata II. "
  "It is the main source for the Pratiharas' claim to have shielded north India from the Arabs. Dharmapala of the Palas and Dhruva of the Rashtrakutas were their rivals in the Tripartite Struggle for Kannauj, and Yashovarman ruled Kannauj in the eighth century, before the Pratiharas took it.",
  "संस्कृत पद्य में ग्वालियर प्रशस्ति सबसे शक्तिशाली गुर्जर-प्रतिहार राजा मिहिर भोज ने जारी की, जिन्होंने नौवीं सदी में कन्नौज से शासन किया। यह उनके वंश को उसके संस्थापक से जोड़ती है और म्लेच्छों की सेनाओं को कुचलने के लिए नागभट प्रथम की प्रशंसा करती है -- जिन्हें सिंध के अरब माना जाता है, जो आठवीं सदी में पश्चिमी भारत में बढ़ आए थे -- और वत्सराज और नागभट द्वितीय की विजयें दर्ज करती है। "
  "उत्तर भारत को अरबों से बचाने के प्रतिहारों के दावे का यही मुख्य स्रोत है। पालों के धर्मपाल और राष्ट्रकूटों के ध्रुव कन्नौज के लिए त्रिपक्षीय संघर्ष में उनके प्रतिद्वंद्वी थे, और यशोवर्मन ने प्रतिहारों के अधिकार से पहले आठवीं सदी में कन्नौज पर शासन किया।",
  "Gwalior Prashasti of Mihira Bhoja (Epigraphia Indica, Vol. XVIII); NCERT, Class VII, Our Pasts II.",
  "l4-s02-his-gwalior-prashasti-mihira-bhoja-nagabhata", pos=1, craft="precision")

M("Ancient", "hard",
  "The Talagunda pillar inscription, composed in Sanskrit in the fifth century, is an important source for",
  "पाँचवीं सदी में संस्कृत में रचित तालगुंडा स्तंभ अभिलेख किसके लिए एक महत्त्वपूर्ण स्रोत है?",
  ["the rise of the Kadamba dynasty of Banavasi",
   "the conquests of the Chalukya king Pulakeshin II",
   "the village assemblies of the Chola kingdom",
   "the campaigns of Kharavela of Kalinga"],
  ["बनवासी के कदंब राजवंश का उदय",
   "चालुक्य राजा पुलकेशिन द्वितीय की विजयें",
   "चोल राज्य की ग्राम सभाएँ",
   "कलिंग के खारवेल के अभियान"],
  0,
  "The inscription on a pillar at Talagunda in Shivamogga district of Karnataka was composed in the reign of the Kadamba king Shantivarman. It tells how the dynasty's founder, a Brahmana who had gone to the Pallava capital Kanchi for Vedic study, was insulted there, took up arms, and won a kingdom with Banavasi as its centre; his successors took the Kshatriya ending 'varman'. "
  "It is among the earliest Sanskrit inscriptions in Karnataka and an example of how Brahmana and other new families legitimised their rule. The other options belong to other records: Pulakeshin II's conquests to the Aihole inscription, the Chola village assemblies to the Uttaramerur inscriptions, and Kharavela's campaigns to the Hathigumpha inscription.",
  "कर्नाटक के शिवमोग्गा ज़िले में तालगुंडा के एक स्तंभ पर लिखा अभिलेख कदंब राजा शांतिवर्मन के शासन में रचा गया। यह बताता है कि वंश का संस्थापक, एक ब्राह्मण जो वैदिक अध्ययन के लिए पल्लव राजधानी कांची गया था, वहाँ अपमानित हुआ, उसने शस्त्र उठाए और बनवासी को केंद्र बनाकर एक राज्य जीता; उसके उत्तराधिकारियों ने क्षत्रिय उपनाम 'वर्मन' अपनाया। "
  "यह कर्नाटक के सबसे पुराने संस्कृत अभिलेखों में से है और इसका उदाहरण है कि ब्राह्मण और अन्य नए परिवारों ने अपने शासन को कैसे वैध ठहराया। अन्य विकल्प अन्य अभिलेखों से जुड़े हैं: पुलकेशिन द्वितीय की विजयें ऐहोल अभिलेख से, चोल ग्राम सभाएँ उत्तरमेरूर अभिलेखों से, और खारवेल के अभियान हाथीगुंफा अभिलेख से।",
  "Talagunda Pillar Inscription of Shantivarman (Epigraphia Indica, Vol. VIII); NCERT, Class VII, Our Pasts II.",
  "l4-s02-his-talagunda-inscription-kadamba-origin", pos=3, craft="precision")

# ---------------------------------------------------------------- Ancient (statement, hard)
S("Ancient", "hard", "With reference to sites of the Harappan civilisation, consider the following statements:",
  "हड़प्पा सभ्यता के स्थलों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Shortugai, a Harappan trading settlement, lies in present-day Iran.",
   "Alamgirpur is the westernmost known Harappan site.",
   "Surkotada is known for the earliest evidence of rice cultivation in the subcontinent."],
  ["हड़प्पाई व्यापारिक बस्ती शोर्तुगई वर्तमान ईरान में स्थित है।",
   "आलमगीरपुर सबसे पश्चिमी ज्ञात हड़प्पाई स्थल है।",
   "सुरकोटडा उपमहाद्वीप में चावल की खेती के सबसे पुराने साक्ष्य के लिए जाना जाता है।"],
  C3, 3,
  "None of the statements is correct. Shortugai lies in northern Afghanistan, on the Amu Darya (Oxus), near the lapis lazuli mines of Badakhshan; it was a Harappan outpost for this blue stone, which reached the Indus cities and Mesopotamia. Alamgirpur, on the Hindon in Meerut district of Uttar Pradesh, is the easternmost Harappan site; the westernmost is Sutkagen Dor, near the Iran border on the Makran coast of Pakistan. "
  "Surkotada, in Kachchh in Gujarat, is known for its fortified settlement and for bones that some excavators identified as those of the horse -- a claim that remains disputed. The rice evidence of the Harappan world comes from sites such as Lothal and Rangpur in Gujarat, and the oldest rice in the subcontinent from the Ganga valley, as at Lahuradewa.",
  "कोई भी कथन सही नहीं है। शोर्तुगई उत्तरी अफ़ग़ानिस्तान में अमु दरिया (ऑक्सस) पर, बदख़्शाँ की लाजवर्द खानों के निकट स्थित है; यह इस नीले पत्थर के लिए एक हड़प्पाई चौकी थी, जो सिंधु नगरों और मेसोपोटामिया तक पहुँचता था। उत्तर प्रदेश के मेरठ ज़िले में हिंडन नदी पर आलमगीरपुर सबसे पूर्वी हड़प्पाई स्थल है; सबसे पश्चिमी पाकिस्तान के मकरान तट पर ईरान सीमा के निकट सुत्कागेन डोर है। "
  "गुजरात के कच्छ में सुरकोटडा अपनी क़िलेबंद बस्ती के लिए और उन हड्डियों के लिए जाना जाता है जिन्हें कुछ उत्खननकर्ताओं ने घोड़े की माना -- एक ऐसा दावा जो विवादित है। हड़प्पाई संसार में चावल के साक्ष्य गुजरात के लोथल और रंगपुर जैसे स्थलों से आते हैं, और उपमहाद्वीप में सबसे पुराना चावल गंगा घाटी से, जैसे लहुरादेवा से।",
  "Archaeological Survey of India, excavation reports; NCERT, Class XII, Themes in Indian History Part I, Theme 1.",
  "l4-s02-his-harappan-shortugai-alamgirpur-surkotada", craft="precision")

# ---------------------------------------------------------------- Ancient (statement, medium)
S("Ancient", "medium", "With reference to the canon of the Svetambara Jains, consider the following statements:",
  "श्वेतांबर जैनों के आगम-ग्रंथों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["It was finally written down at a council held at Valabhi.",
   "It is written in Pali.",
   "The Digambaras accept it as the authentic word of Mahavira."],
  ["इन्हें अंतिम रूप से वलभी में हुई एक परिषद में लिपिबद्ध किया गया।",
   "ये पालि भाषा में लिखे गए हैं।",
   "दिगंबर इन्हें महावीर के प्रामाणिक वचन के रूप में स्वीकार करते हैं।"],
  C3, 0,
  "Only statement 1 is correct. The teachings of Mahavira were handed down orally for centuries; tradition records an early council at Pataliputra, and the canon of the Svetambaras was finally written down at a council at Valabhi in Gujarat in the fifth century CE, under Devarddhi Kshamashramana. Statement 2 is wrong: the canon, made up of the Angas and other texts, is in Ardhamagadhi, a Prakrit; Pali is the language of the Buddhist Tipitaka of the Theravada tradition. "
  "Statement 3 is wrong: the Digambaras hold that the original texts were lost and do not accept the Valabhi canon; they treat later works such as the Shatkhandagama as their scriptures. The dispute over the canon thus deepened the older division between the two sects.",
  "केवल कथन 1 सही है। महावीर की शिक्षाएँ सदियों तक मौखिक रूप से चलती रहीं; परंपरा पाटलिपुत्र में एक आरंभिक परिषद का उल्लेख करती है, और श्वेतांबरों के आगम अंततः ईसा की पाँचवीं सदी में गुजरात के वलभी में देवर्द्धि क्षमाश्रमण के अधीन हुई एक परिषद में लिपिबद्ध किए गए। कथन 2 ग़लत है: अंगों और अन्य ग्रंथों से बने ये आगम एक प्राकृत, अर्धमागधी, में हैं; पालि थेरवाद परंपरा के बौद्ध तिपिटक की भाषा है। "
  "कथन 3 ग़लत है: दिगंबर मानते हैं कि मूल ग्रंथ लुप्त हो गए, और वलभी आगमों को स्वीकार नहीं करते; वे षट्खंडागम जैसी बाद की रचनाओं को अपने शास्त्र मानते हैं। इस प्रकार आगमों पर विवाद ने दोनों संप्रदायों के पुराने विभाजन को और गहरा किया।",
  "NCERT, Class XII, Themes in Indian History Part I, Theme 4; NCERT, Class XI, An Introduction to Indian Art.",
  "l4-s02-his-jain-canon-valabhi-ardhamagadhi-digambara", craft="precision")

# ---------------------------------------------------------------- Medieval (MCQ, medium)
M("Medieval", "medium",
  "The diwan-i-kohi set up by Muhammad bin Tughlaq was meant to",
  "मुहम्मद बिन तुग़लक़ द्वारा स्थापित दीवान-ए-कोही का उद्देश्य था",
  ["extend cultivation and improve crops with advances from the state",
   "collect the arrears of land revenue from the iqtadars of the Doab",
   "organise the transfer of the capital from Delhi to Daulatabad",
   "recruit and pay the cavalry for a planned expedition to Khurasan"],
  ["राज्य की ओर से अग्रिम देकर खेती का विस्तार और फ़सलों में सुधार करना",
   "दोआब के इक़्तादारों से भू-राजस्व का बकाया वसूल करना",
   "राजधानी को दिल्ली से दौलताबाद ले जाने की व्यवस्था करना",
   "ख़ुरासान के प्रस्तावित अभियान के लिए घुड़सवार सेना भर्ती कर वेतन देना"],
  0,
  "After the revenue demand in the Doab had driven peasants away and famine had struck, Muhammad bin Tughlaq set up a separate department of agriculture, the diwan-i-amir-i-kohi. It took a large tract of land under direct management and gave advances to cultivators to bring it under the plough and to grow better crops in rotation. "
  "The experiment failed: the land chosen was poor, the officials misused the money, and the advances did not come back. With the token currency, the transfer of the capital and the Khurasan army -- the other options, each a separate measure -- it is part of the record of bold schemes that failed in execution, which Barani describes.",
  "दोआब में राजस्व की माँग से किसानों के भाग जाने और अकाल पड़ने के बाद मुहम्मद बिन तुग़लक़ ने कृषि का एक अलग विभाग, दीवान-ए-अमीर-ए-कोही, स्थापित किया। इसने भूमि का एक बड़ा क्षेत्र सीधे प्रबंध में लिया और किसानों को उसे जोत में लाने और बारी-बारी से बेहतर फ़सलें उगाने के लिए अग्रिम दिए। "
  "यह प्रयोग विफल रहा: चुनी गई भूमि कमज़ोर थी, अधिकारियों ने धन का दुरुपयोग किया, और अग्रिम वापस नहीं आए। सांकेतिक मुद्रा, राजधानी के स्थानांतरण और ख़ुरासान सेना के साथ -- जो अन्य विकल्प हैं, हर एक अलग उपाय -- यह उन साहसिक योजनाओं में से है जो क्रियान्वयन में विफल रहीं, जिनका वर्णन बरनी करता है।",
  "Ziauddin Barani, Tarikh-i-Firoz Shahi; NCERT, Class VII, Our Pasts II.",
  "l4-s02-his-diwan-i-kohi-tughlaq-agriculture", pos=2, craft="recall")

# ---------------------------------------------------------------- Medieval (statement, hard)
S("Medieval", "hard", "With reference to Banda Singh Bahadur, consider the following statements:",
  "बंदा सिंह बहादुर के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["He made Lohgarh, in the Shivalik foothills, his stronghold and capital.",
   "He issued coins and a seal in the names of Guru Nanak and Guru Gobind Singh.",
   "He was captured and executed at Delhi in the reign of Farrukhsiyar.",
   "Guru Gobind Singh named him the eleventh Guru of the Sikhs."],
  ["उन्होंने शिवालिक की तलहटी में लोहगढ़ को अपना गढ़ और राजधानी बनाया।",
   "उन्होंने गुरु नानक और गुरु गोबिंद सिंह के नाम पर सिक्के और मुहर जारी की।",
   "फ़र्रुख़सियर के शासनकाल में उन्हें पकड़कर दिल्ली में मृत्युदंड दिया गया।",
   "गुरु गोबिंद सिंह ने उन्हें सिखों का ग्यारहवाँ गुरु घोषित किया।"],
  C4, 2,
  "The first three statements are correct. Sent to Punjab by Guru Gobind Singh, Banda Singh Bahadur raised the peasantry, defeated the faujdar of Sirhind in 1710, and made Mukhlisgarh, renamed Lohgarh, his capital. He struck coins and used a seal in the names of Guru Nanak and Guru Gobind Singh, claiming sovereignty in the name of the Gurus, and is remembered for giving land to the tillers. "
  "The Mughals besieged him at Gurdas Nangal; he was captured in 1715 and executed at Delhi in 1716, under Farrukhsiyar. Statement 4 is wrong: before his death in 1708 Guru Gobind Singh ended the line of personal Gurus, vesting the Guruship in the Granth Sahib and the Khalsa Panth, so there was no eleventh human Guru -- one reason why some Sikhs later questioned Banda's authority.",
  "पहले तीन कथन सही हैं। गुरु गोबिंद सिंह द्वारा पंजाब भेजे गए बंदा सिंह बहादुर ने किसानों को संगठित किया, 1710 में सरहिंद के फ़ौजदार को हराया, और मुख़लिसगढ़ को, जिसका नाम लोहगढ़ रखा गया, अपनी राजधानी बनाया। उन्होंने गुरुओं के नाम पर संप्रभुता का दावा करते हुए गुरु नानक और गुरु गोबिंद सिंह के नाम पर सिक्के ढाले और मुहर का प्रयोग किया, और उन्हें जोतने वालों को भूमि देने के लिए याद किया जाता है। "
  "मुग़लों ने उन्हें गुरदास नंगल में घेरा; वे 1715 में पकड़े गए और 1716 में फ़र्रुख़सियर के अधीन दिल्ली में मार दिए गए। कथन 4 ग़लत है: 1708 में अपनी मृत्यु से पहले गुरु गोबिंद सिंह ने व्यक्तिगत गुरुओं की परंपरा समाप्त कर गुरुत्व को ग्रंथ साहिब और ख़ालसा पंथ में निहित कर दिया, इसलिए कोई ग्यारहवाँ मानव गुरु नहीं था -- एक कारण कि कुछ सिखों ने बाद में बंदा के अधिकार पर प्रश्न उठाए।",
  "NCERT, Class VII, Our Pasts II, chapter on eighteenth-century political formations.",
  "l4-s02-his-banda-singh-lohgarh-coins-farrukhsiyar", craft="multi")

# ---------------------------------------------------------------- Medieval (statement, medium)
S("Medieval", "medium", "With reference to the Sufi poetry of Sindh and Punjab, consider the following statements:",
  "सिंध और पंजाब की सूफ़ी कविता के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["The verses of Shah Abdul Latif are collected in the Shah Jo Risalo, in Sindhi.",
   "Waris Shah wrote the best-known version of Heer in Punjabi.",
   "Bulleh Shah belonged to the Naqshbandi order and rejected music in worship.",
   "The shrine of Shah Abdul Latif is at Kasur."],
  ["शाह अब्दुल लतीफ़ की कविताएँ सिंधी में शाह जो रिसालो में संकलित हैं।",
   "वारिस शाह ने पंजाबी में हीर का सबसे प्रसिद्ध रूप लिखा।",
   "बुल्ले शाह नक़्शबंदी सिलसिले से जुड़े थे और उपासना में संगीत को अस्वीकार करते थे।",
   "शाह अब्दुल लतीफ़ की दरगाह क़सूर में है।"],
  C4, 1,
  "Only statements 1 and 2 are correct. Shah Abdul Latif Bhittai (1689-1752), the greatest poet of Sindhi, left verses that were collected as the Shah Jo Risalo and are still sung at his shrine at Bhit Shah in Sindh. Waris Shah's Heer (1766) is the classic Punjabi telling of the love of Heer and Ranjha, used as a Sufi allegory of the soul's longing for God. "
  "Statement 3 is wrong: Bulleh Shah was a disciple of Shah Inayat of the Qadiri order, and his kafis were meant to be sung -- they remain part of qawwali and folk music; it was the Naqshbandis who, under Shaikh Ahmad Sirhindi, opposed music and stressed strict observance. Statement 4 is wrong: Kasur, in Pakistani Punjab, holds the shrine of Bulleh Shah, not of Shah Abdul Latif. These poets wrote in the spoken languages of the people, which spread Sufi ideas well beyond Persian-reading elites.",
  "केवल कथन 1 और 2 सही हैं। सिंधी के सबसे बड़े कवि शाह अब्दुल लतीफ़ भिटाई (1689-1752) की कविताएँ शाह जो रिसालो के रूप में संकलित हुईं और आज भी सिंध में भिट शाह स्थित उनकी दरगाह पर गाई जाती हैं। वारिस शाह की हीर (1766) हीर और रांझा के प्रेम की शास्त्रीय पंजाबी कथा है, जिसे आत्मा की ईश्वर के प्रति तड़प के सूफ़ी रूपक के रूप में पढ़ा जाता है। "
  "कथन 3 ग़लत है: बुल्ले शाह क़ादिरी सिलसिले के शाह इनायत के शिष्य थे, और उनकी काफ़ियाँ गाने के लिए थीं -- वे आज भी क़व्वाली और लोक संगीत का भाग हैं; शेख़ अहमद सरहिंदी के अधीन नक़्शबंदियों ने संगीत का विरोध किया और कठोर पालन पर बल दिया। कथन 4 ग़लत है: पाकिस्तानी पंजाब के क़सूर में बुल्ले शाह की दरगाह है, शाह अब्दुल लतीफ़ की नहीं। इन कवियों ने जनता की बोलचाल की भाषाओं में लिखा, जिससे सूफ़ी विचार फ़ारसी पढ़ने वाले अभिजात वर्ग से बहुत आगे फैले।",
  "NCERT, Class XII, Themes in Indian History Part II, Theme 6 (Bhakti-Sufi Traditions); Sahitya Akademi histories of Sindhi and Punjabi literature.",
  "l4-s02-his-sufi-poets-latif-waris-bulleh-kasur", craft="precision")

# ---------------------------------------------------------------- Modern (pairs, medium)
P("Modern", "medium", "Consider the following pairs of organisations and persons associated with their founding:",
  "संगठनों और उनकी स्थापना से जुड़े व्यक्तियों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Landholders' Society (1838) : Raja Rammohan Roy",
   "Hindustan Republican Association (1924) : Sachindra Nath Sanyal",
   "Berlin Committee (1915) : Virendranath Chattopadhyaya",
   "Jugantar, the Bengali weekly (1906) : Lala Har Dayal"],
  ["लैंडहोल्डर्स सोसाइटी (1838) : राजा राममोहन राय",
   "हिंदुस्तान रिपब्लिकन एसोसिएशन (1924) : शचींद्रनाथ सान्याल",
   "बर्लिन समिति (1915) : वीरेंद्रनाथ चट्टोपाध्याय",
   "बांग्ला साप्ताहिक युगांतर (1906) : लाला हरदयाल"],
  1,
  "Only pairs 2 and 3 are correct. The Hindustan Republican Association was founded at Kanpur in 1924 by Sachindra Nath Sanyal, with Jogesh Chandra Chatterjee and Ram Prasad Bismil; its members carried out the Kakori train action of 1925, and in 1928 it was renamed the Hindustan Socialist Republican Association under Bhagat Singh and Chandrashekhar Azad. The Berlin Committee (Indian Independence Committee), set up in 1915 with German support during the First World War, was led by Virendranath Chattopadhyaya, with Bhupendranath Dutta and others, and sent missions to Kabul and elsewhere. "
  "Pair 1 is wrong: the Landholders' Society (Zamindari Association) of 1838, the first political association in Bengal to defend landlords' interests, was founded by Dwarkanath Tagore, Prasanna Kumar Tagore and Radhakanta Deb; Rammohan Roy had died in Bristol in 1833. Pair 4 is wrong: Jugantar was started by Barindra Kumar Ghosh and Bhupendranath Dutta and gave its name to a revolutionary group in Bengal; Har Dayal later founded the Ghadar Party in the United States.",
  "केवल युग्म 2 और 3 सही हैं। हिंदुस्तान रिपब्लिकन एसोसिएशन की स्थापना 1924 में कानपुर में शचींद्रनाथ सान्याल ने जोगेशचंद्र चटर्जी और राम प्रसाद बिस्मिल के साथ की; इसके सदस्यों ने 1925 की काकोरी ट्रेन कार्रवाई की, और 1928 में भगत सिंह और चंद्रशेखर आज़ाद के अधीन इसका नाम हिंदुस्तान सोशलिस्ट रिपब्लिकन एसोसिएशन हो गया। प्रथम विश्व युद्ध में जर्मन सहायता से 1915 में बनी बर्लिन समिति (इंडियन इंडिपेंडेंस कमेटी) का नेतृत्व वीरेंद्रनाथ चट्टोपाध्याय ने भूपेंद्रनाथ दत्त और अन्य के साथ किया, और उसने काबुल और अन्य स्थानों पर मिशन भेजे। "
  "युग्म 1 ग़लत है: 1838 की लैंडहोल्डर्स सोसाइटी (ज़मींदारी एसोसिएशन), ज़मींदारों के हितों की रक्षा के लिए बंगाल का पहला राजनीतिक संगठन, द्वारकानाथ टैगोर, प्रसन्न कुमार टैगोर और राधाकांत देब ने बनाई थी; राममोहन राय की 1833 में ब्रिस्टल में मृत्यु हो चुकी थी। युग्म 4 ग़लत है: युगांतर बारींद्र कुमार घोष और भूपेंद्रनाथ दत्त ने आरंभ किया और इसी के नाम पर बंगाल का एक क्रांतिकारी समूह जाना गया; हरदयाल ने बाद में संयुक्त राज्य अमेरिका में ग़दर पार्टी बनाई।",
  "NCERT, Class VIII, Our Pasts III; National Archives of India, records of the Kakori and Lahore conspiracy cases.",
  "l4-s02-his-landholders-hra-berlin-jugantar-pairs", craft="precision")

# ---------------------------------------------------------------- Modern (MCQ, medium)
M("Modern", "medium",
  "Mooknayak, a Marathi fortnightly started in 1920 with the support of Shahu Maharaj of Kolhapur, was founded by",
  "कोल्हापुर के शाहू महाराज के सहयोग से 1920 में आरंभ हुए मराठी पाक्षिक मूकनायक की स्थापना किसने की थी?",
  ["B. R. Ambedkar", "Jyotirao Phule", "Gopal Ganesh Agarkar", "Vitthal Ramji Shinde"],
  ["बी. आर. आंबेडकर", "ज्योतिराव फुले", "गोपाल गणेश आगरकर", "विट्ठल रामजी शिंदे"],
  0,
  "Ambedkar launched Mooknayak ('leader of the voiceless') in January 1920, soon after his return from Columbia, with Shahu Maharaj's financial help, to voice the grievances of the untouchables. It was followed by Bahishkrit Bharat (1927), Janata and Prabuddha Bharat. "
  "The other options are also Maharashtrian reformers but of other periods or papers: Jyotirao Phule (died 1890) founded the Satyashodhak Samaj in 1873; Agarkar edited Sudharak and, earlier, Kesari; and Vitthal Ramji Shinde founded the Depressed Classes Mission of India in 1906.",
  "आंबेडकर ने कोलंबिया से लौटने के कुछ ही बाद जनवरी 1920 में शाहू महाराज की आर्थिक सहायता से अछूतों की शिकायतों को स्वर देने के लिए मूकनायक ('बेज़ुबानों का नायक') आरंभ किया। इसके बाद बहिष्कृत भारत (1927), जनता और प्रबुद्ध भारत आए। "
  "अन्य विकल्प भी महाराष्ट्र के सुधारक हैं, पर दूसरे कालों या पत्रों से जुड़े: ज्योतिराव फुले (मृत्यु 1890) ने 1873 में सत्यशोधक समाज बनाया; आगरकर ने सुधारक का और उससे पहले केसरी का संपादन किया; और विट्ठल रामजी शिंदे ने 1906 में डिप्रेस्ड क्लासेस मिशन ऑफ़ इंडिया की स्थापना की।",
  "Dr. Babasaheb Ambedkar: Writings and Speeches (Government of Maharashtra); NCERT, Class VIII, Our Pasts III.",
  "l4-s02-his-mooknayak-ambedkar-1920", pos=0, craft="recall")

M("Modern", "medium", "Which one of the following was a feature of the Indian Councils Act, 1892?",
  "निम्नलिखित में से कौन-सी भारतीय परिषद अधिनियम, 1892 की एक विशेषता थी?",
  ["Members could discuss the budget but could not vote on it",
   "Separate electorates were created for Muslims in elections to the legislative councils",
   "Subjects in the provinces were divided into reserved and transferred subjects",
   "Members could ask supplementary questions and move resolutions on the budget"],
  ["सदस्य बजट पर चर्चा कर सकते थे पर उस पर मतदान नहीं कर सकते थे",
   "विधान परिषदों के चुनावों में मुसलमानों के लिए पृथक निर्वाचक मंडल बनाए गए",
   "प्रांतों में विषयों को आरक्षित और हस्तांतरित विषयों में बाँटा गया",
   "सदस्य अनुपूरक प्रश्न पूछ सकते थे और बजट पर संकल्प प्रस्तुत कर सकते थे"],
  0,
  "The Act of 1892 enlarged the legislative councils and, without using the word 'election', let bodies such as district boards, municipalities, universities and chambers of commerce recommend members whom the Governor-General or Governors nominated -- the first, indirect step towards elected members. Members could discuss the annual financial statement and ask questions, but could not vote on the budget or ask supplementary questions. "
  "The other options belong to later Acts: separate electorates for Muslims came with the Morley-Minto Reforms of 1909, which also let members move resolutions and ask supplementary questions, and the division into reserved and transferred subjects (dyarchy) with the Government of India Act, 1919. The Congress criticised the 1892 Act as inadequate, and the demand for elected majorities grew.",
  "1892 के अधिनियम ने विधान परिषदों को बड़ा किया और 'चुनाव' शब्द का प्रयोग किए बिना ज़िला बोर्डों, नगरपालिकाओं, विश्वविद्यालयों और वाणिज्य मंडलों जैसे निकायों को ऐसे सदस्यों की संस्तुति करने दी जिन्हें गवर्नर-जनरल या गवर्नर मनोनीत करते थे -- निर्वाचित सदस्यों की ओर पहला, अप्रत्यक्ष क़दम। सदस्य वार्षिक वित्तीय विवरण पर चर्चा कर सकते थे और प्रश्न पूछ सकते थे, पर बजट पर मतदान या अनुपूरक प्रश्न नहीं कर सकते थे। "
  "अन्य विकल्प बाद के अधिनियमों के हैं: मुसलमानों के लिए पृथक निर्वाचक मंडल 1909 के मॉर्ले-मिंटो सुधारों से आए, जिन्होंने सदस्यों को संकल्प प्रस्तुत करने और अनुपूरक प्रश्न पूछने की अनुमति भी दी, और आरक्षित तथा हस्तांतरित विषयों का विभाजन (द्वैध शासन) भारत सरकार अधिनियम, 1919 से। कांग्रेस ने 1892 के अधिनियम को अपर्याप्त बताया, और निर्वाचित बहुमत की माँग बढ़ी।",
  "Indian Councils Act, 1892; Indian Councils Act, 1909; Government of India Act, 1919.",
  "l4-s02-his-indian-councils-act-1892-budget-recommend", pos=3, craft="precision")

# ---------------------------------------------------------------- Modern (statement, easy)
S("Modern", "easy", "With reference to Gandhi's years in South Africa, consider the following statements:",
  "दक्षिण अफ़्रीका में गांधी के वर्षों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["He founded the Natal Indian Congress in 1894.",
   "He set up Tolstoy Farm near Durban in 1904."],
  ["उन्होंने 1894 में नेटाल इंडियन कांग्रेस की स्थापना की।",
   "उन्होंने 1904 में डरबन के निकट टॉल्सटॉय फ़ार्म बनाया।"],
  T2, 0,
  "Only statement 1 is correct. Gandhi, who had gone to South Africa in 1893 for a legal case, founded the Natal Indian Congress in 1894 to fight discrimination against Indians, and started the paper Indian Opinion in 1903. Statement 2 confuses his two settlements: the Phoenix Settlement, set up in 1904, was near Durban, while Tolstoy Farm was founded in 1910 near Johannesburg, on land given by his friend Hermann Kallenbach, to house the families of satyagrahis. "
  "These communities were his first experiments in collective living and self-reliance, which he later carried to the Sabarmati and Sevagram ashrams.",
  "केवल कथन 1 सही है। एक क़ानूनी मामले के लिए 1893 में दक्षिण अफ़्रीका गए गांधी ने भारतीयों के विरुद्ध भेदभाव से लड़ने के लिए 1894 में नेटाल इंडियन कांग्रेस बनाई, और 1903 में इंडियन ओपिनियन पत्र आरंभ किया। कथन 2 उनकी दो बस्तियों को मिला देता है: 1904 में बनी फ़ीनिक्स बस्ती डरबन के निकट थी, जबकि टॉल्सटॉय फ़ार्म 1910 में जोहान्सबर्ग के निकट, उनके मित्र हरमन कालेनबाख द्वारा दी गई भूमि पर, सत्याग्रहियों के परिवारों को रखने के लिए बना। "
  "ये समुदाय सामूहिक जीवन और आत्मनिर्भरता के उनके पहले प्रयोग थे, जिन्हें वे बाद में साबरमती और सेवाग्राम आश्रमों तक ले गए।",
  "M. K. Gandhi, Satyagraha in South Africa and An Autobiography; Collected Works of Mahatma Gandhi (Publications Division).",
  "l4-s02-his-gandhi-south-africa-nic-tolstoy-farm", craft="recall")

# ---------------------------------------------------------------- Modern (statement, hard)
S("Modern", "hard", "With reference to the campaign for women's franchise in India, consider the following statements:",
  "भारत में महिलाओं के मताधिकार के अभियान के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Women's India Association was founded at Adyar in 1917.",
   "In 1917 a deputation of women led by Sarojini Naidu met Edwin Montagu to demand the vote for women.",
   "The Government of India Act, 1919 itself gave women the vote in every province.",
   "The All India Women's Conference was founded in 1927."],
  ["वीमेन्स इंडियन एसोसिएशन की स्थापना 1917 में अड्यार में हुई।",
   "1917 में सरोजिनी नायडू के नेतृत्व में महिलाओं का एक प्रतिनिधिमंडल महिलाओं के लिए मताधिकार माँगने एडविन मॉन्टेग्यू से मिला।",
   "भारत सरकार अधिनियम, 1919 ने स्वयं प्रत्येक प्रांत में महिलाओं को मताधिकार दिया।",
   "अखिल भारतीय महिला सम्मेलन की स्थापना 1927 में हुई।"],
  C4, 2,
  "Statements 1, 2 and 4 are correct. The Women's India Association was founded at Adyar, Madras, in 1917 by Annie Besant, Margaret Cousins, Dorothy Jinarajadasa and others, and that December a deputation led by Sarojini Naidu put the demand for the vote before Montagu and Chelmsford during their inquiry into reforms. The All India Women's Conference, founded at Poona in 1927, first worked on women's education and soon took up franchise and legal reform. "
  "Statement 3 is wrong: the Act of 1919 left the question to the provincial legislatures. Madras was the first province to enfranchise women, in 1921, and others followed during the 1920s; the vote still depended on property and education, so few women qualified until the 1935 Act widened it, and adult franchise came only with the Constitution.",
  "कथन 1, 2 और 4 सही हैं। वीमेन्स इंडियन एसोसिएशन की स्थापना 1917 में मद्रास के अड्यार में एनी बेसेंट, मार्गरेट कज़िन्स, डोरोथी जिनराजदास और अन्य ने की, और उसी दिसंबर में सरोजिनी नायडू के नेतृत्व में एक प्रतिनिधिमंडल ने सुधारों की जाँच के दौरान मॉन्टेग्यू और चेम्सफ़ोर्ड के समक्ष मताधिकार की माँग रखी। 1927 में पूना में स्थापित अखिल भारतीय महिला सम्मेलन ने पहले महिलाओं की शिक्षा पर काम किया और शीघ्र ही मताधिकार और विधिक सुधार को उठाया। "
  "कथन 3 ग़लत है: 1919 के अधिनियम ने यह प्रश्न प्रांतीय विधानमंडलों पर छोड़ दिया। मद्रास 1921 में महिलाओं को मताधिकार देने वाला पहला प्रांत था, और 1920 के दशक में अन्य ने अनुसरण किया; मताधिकार फिर भी संपत्ति और शिक्षा पर निर्भर था, इसलिए 1935 के अधिनियम द्वारा इसके विस्तार तक बहुत कम महिलाएँ पात्र थीं, और वयस्क मताधिकार संविधान के साथ ही आया।",
  "Government of India Act, 1919; Report on Indian Constitutional Reforms (1918); NCERT, Class VIII, Our Pasts III.",
  "l4-s02-his-women-franchise-wia-montagu-1919-aiwc", craft="multi")

# ---------------------------------------------------------------- Modern (statement, medium)
S("Modern", "medium", "With reference to the Amrita Bazar Patrika, consider the following statements:",
  "अमृत बाज़ार पत्रिका के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["It was started in 1868 as a Bengali weekly in Jessore district.",
   "In 1878 it turned into an English-language paper almost overnight.",
   "It was the paper that Surendranath Banerjea edited for most of his public life."],
  ["इसे 1868 में जेसोर ज़िले में एक बांग्ला साप्ताहिक के रूप में आरंभ किया गया।",
   "1878 में यह लगभग रातोंरात एक अंग्रेज़ी पत्र बन गई।",
   "यही वह पत्र था जिसका संपादन सुरेंद्रनाथ बनर्जी ने अपने सार्वजनिक जीवन के अधिकांश समय किया।"],
  C3, 1,
  "Only statements 1 and 2 are correct. Sisir Kumar Ghosh and Motilal Ghosh started the Patrika in 1868 at their village, Amrita Bazar, in Jessore district, and moved it to Calcutta in 1871. When Lord Lytton's Vernacular Press Act of 1878 put Indian-language papers under heavy restraint, the Patrika escaped it by turning into an English paper almost overnight; it became a daily in 1891 and was a strong critic of British rule. "
  "Statement 3 is wrong: Surendranath Banerjea edited The Bengalee, which he took over in 1879. The episode shows how the Act, by leaving English-language papers alone, exposed its purpose of silencing the vernacular press, and it was repealed under Ripon in 1882.",
  "केवल कथन 1 और 2 सही हैं। शिशिर कुमार घोष और मोतीलाल घोष ने 1868 में जेसोर ज़िले में अपने गाँव अमृत बाज़ार से पत्रिका आरंभ की, और 1871 में उसे कलकत्ता ले गए। जब लॉर्ड लिटन के 1878 के वर्नाक्युलर प्रेस एक्ट ने भारतीय भाषाओं के पत्रों पर कड़े प्रतिबंध लगाए, तो पत्रिका लगभग रातोंरात अंग्रेज़ी पत्र बनकर उससे बच गई; 1891 में यह दैनिक बनी और ब्रिटिश शासन की प्रबल आलोचक रही। "
  "कथन 3 ग़लत है: सुरेंद्रनाथ बनर्जी ने द बंगाली का संपादन किया, जिसे उन्होंने 1879 में संभाला। यह घटना दिखाती है कि अंग्रेज़ी पत्रों को छोड़कर अधिनियम ने देशी भाषा के प्रेस को चुप कराने का अपना उद्देश्य उजागर कर दिया, और 1882 में रिपन के अधीन उसे निरस्त कर दिया गया।",
  "Vernacular Press Act, 1878; NCERT, Class VIII, Our Pasts III.",
  "l4-s02-his-amrita-bazar-patrika-english-overnight-1878", craft="precision")

S("Modern", "medium", "With reference to the provincial government under the Government of India Act, 1919, consider the following statements:",
  "भारत सरकार अधिनियम, 1919 के अंतर्गत प्रांतीय शासन के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Education, public health and local self-government were transferred subjects.",
   "Police, justice and land revenue were reserved subjects.",
   "The ministers in charge of transferred subjects were responsible to the provincial legislative council.",
   "The Act also introduced dyarchy at the Centre."],
  ["शिक्षा, लोक स्वास्थ्य और स्थानीय स्वशासन हस्तांतरित विषय थे।",
   "पुलिस, न्याय और भू-राजस्व आरक्षित विषय थे।",
   "हस्तांतरित विषयों के प्रभारी मंत्री प्रांतीय विधान परिषद के प्रति उत्तरदायी थे।",
   "अधिनियम ने केंद्र में भी द्वैध शासन लागू किया।"],
  C4, 2,
  "The first three statements are correct. The Act of 1919 divided provincial subjects into transferred subjects -- such as education, public health, local self-government, agriculture and industries -- run by ministers responsible to the legislative council, and reserved subjects -- such as police, justice, land revenue, irrigation and finance -- run by the Governor and his executive councillors, who were not responsible to the council. "
  "Because finance stayed reserved, ministers often lacked the money to run their departments, and the Governor could overrule them, which is why dyarchy was widely judged a failure. Statement 4 is wrong: the Centre stayed without responsible government under the 1919 Act; the Government of India Act, 1935 provided for dyarchy at the Centre, and that part never came into force.",
  "पहले तीन कथन सही हैं। 1919 के अधिनियम ने प्रांतीय विषयों को हस्तांतरित विषयों -- जैसे शिक्षा, लोक स्वास्थ्य, स्थानीय स्वशासन, कृषि और उद्योग -- में बाँटा, जिन्हें विधान परिषद के प्रति उत्तरदायी मंत्री चलाते थे, और आरक्षित विषयों -- जैसे पुलिस, न्याय, भू-राजस्व, सिंचाई और वित्त -- में, जिन्हें गवर्नर और उसके कार्यकारी पार्षद चलाते थे, जो परिषद के प्रति उत्तरदायी नहीं थे। "
  "वित्त आरक्षित रहने के कारण मंत्रियों के पास प्रायः अपने विभाग चलाने के लिए धन नहीं होता था, और गवर्नर उन्हें अस्वीकार कर सकता था, इसी कारण द्वैध शासन को व्यापक रूप से विफल माना गया। कथन 4 ग़लत है: 1919 के अधिनियम में केंद्र में उत्तरदायी शासन नहीं था; भारत सरकार अधिनियम, 1935 ने केंद्र में द्वैध शासन का प्रावधान किया, और वह भाग कभी लागू नहीं हुआ।",
  "Government of India Act, 1919; Government of India Act, 1935; NCERT, Class XII, Political Science, Indian Constitution at Work.",
  "l4-s02-his-goi-1919-reserved-transferred-centre", craft="linkage")

# ---------------------------------------------------------------- Music & Dance (pairs, hard)
P("Music & Dance", "hard", "Consider the following pairs of performance traditions and the States with which they are associated:",
  "प्रदर्शन परंपराओं और उनसे जुड़े राज्यों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Ramman : Uttarakhand",
   "Mudiyettu : Kerala",
   "Hojagiri : Tripura",
   "Cheraw : Mizoram"],
  ["रम्माण : उत्तराखंड",
   "मुडियेट्टु : केरल",
   "होजागिरी : त्रिपुरा",
   "चेराव : मिज़ोरम"],
  3,
  "All four pairs are correct. Ramman is the religious festival and masked ritual theatre of the villages of Saloor-Dungra in Chamoli district of Uttarakhand, honouring the local deity Bhumiyal Devta; UNESCO inscribed it on the list of the Intangible Cultural Heritage of Humanity in 2009. Mudiyettu is a ritual dance-drama of the temples of central Kerala, enacting the goddess Kali's battle with the demon Darika, and was inscribed in 2010. "
  "Hojagiri is the dance of the Reang (Bru) community of Tripura, in which women balance pitchers and lamps while moving only the lower body. Cheraw, the bamboo dance of Mizoram, has dancers stepping in and out between bamboo staves that are clapped together in rhythm.",
  "चारों युग्म सही हैं। रम्माण उत्तराखंड के चमोली ज़िले के सलूड़-डुंग्रा गाँवों का धार्मिक उत्सव और मुखौटा-युक्त अनुष्ठानिक रंगमंच है, जो स्थानीय देवता भूमियाल देवता को समर्पित है; यूनेस्को ने इसे 2009 में मानवता की अमूर्त सांस्कृतिक विरासत की सूची में अंकित किया। मुडियेट्टु मध्य केरल के मंदिरों का अनुष्ठानिक नृत्य-नाटक है, जिसमें देवी काली का दानव दारिका से युद्ध दिखाया जाता है, और इसे 2010 में अंकित किया गया। "
  "होजागिरी त्रिपुरा के रियांग (ब्रू) समुदाय का नृत्य है, जिसमें स्त्रियाँ केवल शरीर के निचले भाग को हिलाते हुए घड़े और दीपक संतुलित करती हैं। मिज़ोरम का बाँस नृत्य चेराव है, जिसमें नर्तक लय में आपस में टकराई जाने वाली बाँस की छड़ों के बीच अंदर-बाहर क़दम रखते हैं।",
  "UNESCO, Lists of Intangible Cultural Heritage (Ramman, 2009; Mudiyettu, 2010); Sangeet Natak Akademi; Ministry of Culture, Government of India.",
  "l4-s02-his-ramman-mudiyettu-hojagiri-cheraw", craft="recall")

write("gs_l4_s02_b.sql")
