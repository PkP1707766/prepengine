# -*- coding: utf-8 -*-
"""Level 4 · Simulator 1 (GS Paper I full mock, Layout A: the 2023/24 shape) -- part C: Environment & Ecology (15)
(upsc_l4_gs_cell_targets.mjs 1).
Drawn from a whole-bank sweep of species, sites, treaties and concepts that no row tests: the Paris rulebook;
sulphur hexafluoride; methane hydrates; bioaccumulation and Lindeman's ten per cent law; the nilgai; the
stump-tailed macaque, capped langur and Nilgiri langur; the vulture-toxic painkillers after diclofenac; Mikania;
bioluminescent fungi; deemed forests, community forest resource rights, eco-sensitive zones and the compensatory
afforestation fund; the Bunker Convention; HCFC-141b; ocean deoxygenation; Khijadia, Deepor Beel, Ashtamudi and
Pichavaram; Melghat, Sathyamangalam and Kali tiger reserves. MCQ keys are pinned (pos)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Environment & Ecology"
d.REQUIRE_CRAFT = True

# ---------------------------------------------------------------- Climate Agreements & Carbon Markets (AR, medium)
A("Climate Agreements & Carbon Markets", "medium",
  "One of the aims of the Paris Agreement is to make finance flows consistent with a pathway towards low greenhouse gas emissions and climate-resilient development.",
  "पेरिस समझौते के लक्ष्यों में से एक वित्त प्रवाहों को कम ग्रीनहाउस गैस उत्सर्जन और जलवायु-सहनशील विकास के मार्ग के अनुरूप बनाना है।",
  "This aim obliges developed countries to stop all public financing of coal-fired power within five years of ratifying the Agreement.",
  "यह लक्ष्य विकसित देशों को समझौते के अनुसमर्थन के पाँच वर्ष के भीतर कोयला-आधारित बिजली के सभी सार्वजनिक वित्तपोषण को रोकने के लिए बाध्य करता है।",
  2,
  "Statement I is correct, but Statement II is incorrect. Article 2.1 of the Paris Agreement sets three aims: holding warming well below 2 °C and pursuing 1.5 °C (2.1(a)); increasing the ability to adapt (2.1(b)); and 'making finance flows consistent with a pathway towards low greenhouse gas emissions and climate-resilient development' (2.1(c)). The third goes beyond the transfer of climate finance from rich to poor countries: it asks that all finance, public and private, be aligned with the transition, which is why central banks, regulators and development banks now speak of 'Paris alignment'. "
  "Statement II is wrong: the Agreement sets no sector-specific obligations or deadlines; what each country does is left to its nationally determined contribution, and commitments to end public finance for coal abroad were made separately, as political pledges, by groups of countries. Developing countries have argued that 2.1(c) must not be read as a condition on their access to finance.",
  "कथन I सही है, पर कथन II ग़लत है। पेरिस समझौते का अनुच्छेद 2.1 तीन लक्ष्य रखता है: तापन को 2 °C से काफ़ी नीचे रखना और 1.5 °C का प्रयास करना (2.1(क)); अनुकूलन की क्षमता बढ़ाना (2.1(ख)); और ‘वित्त प्रवाहों को कम ग्रीनहाउस गैस उत्सर्जन और जलवायु-सहनशील विकास के मार्ग के अनुरूप बनाना’ (2.1(ग))। तीसरा लक्ष्य अमीर देशों से ग़रीब देशों को जलवायु वित्त के हस्तांतरण से आगे जाता है: यह अपेक्षा करता है कि सभी वित्त, सार्वजनिक और निजी, संक्रमण के अनुरूप हों, इसीलिए केंद्रीय बैंक, नियामक और विकास बैंक अब ‘पेरिस संरेखण’ की बात करते हैं। "
  "कथन II ग़लत है: समझौता किसी क्षेत्र-विशेष के दायित्व या समय-सीमाएँ तय नहीं करता; हर देश क्या करे, यह उसके राष्ट्रीय स्तर पर निर्धारित योगदान पर छोड़ा गया है, और विदेश में कोयले के सार्वजनिक वित्त को समाप्त करने की प्रतिबद्धताएँ देशों के समूहों ने अलग से, राजनीतिक संकल्पों के रूप में, कीं। विकासशील देशों ने तर्क दिया है कि 2.1(ग) को वित्त तक उनकी पहुँच पर शर्त के रूप में नहीं पढ़ा जाना चाहिए।",
  "Paris Agreement (2015), Article 2.1; UNFCCC Standing Committee on Finance, reports on Article 2.1(c).",
  "l4-s01-env-paris-art2-1c-finance-flows-no-coal-mandate", craft="inference")

# ---------------------------------------------------------------- Climate Science & Mitigation (MCQ, medium)
M("Climate Science & Mitigation", "medium",
  "Which one of the following is NOT usually counted among the 'short-lived climate pollutants'?",
  "निम्नलिखित में से किसे सामान्यतः ‘अल्पकालिक जलवायु प्रदूषकों’ में नहीं गिना जाता?",
  ["Carbon dioxide", "Methane", "Black carbon", "Tropospheric ozone"],
  ["कार्बन डाइऑक्साइड", "मीथेन", "ब्लैक कार्बन", "क्षोभमंडलीय ओज़ोन"],
  0,
  "Short-lived climate pollutants are warming agents that stay in the atmosphere for a much shorter time than carbon dioxide: black carbon (soot) for days to weeks, tropospheric ozone for weeks, methane for about a decade, and many HFCs for a few years to a few decades. Because they disappear quickly, cutting them slows warming within years, and because several of them -- soot and ground-level ozone -- also damage health and crops, the cuts bring local benefits; UNEP and the Climate and Clean Air Coalition, which India joined in 2019, estimate that fast action could avoid about 0.6 °C of warming by mid-century. "
  "Carbon dioxide is the long-lived gas: a large share of each emission remains for centuries, so its warming accumulates, which is why deep cuts in carbon dioxide remain essential even if short-lived pollutants are tackled.",
  "अल्पकालिक जलवायु प्रदूषक वे तापनकारी कारक हैं जो वायुमंडल में कार्बन डाइऑक्साइड की तुलना में बहुत कम समय रहते हैं: ब्लैक कार्बन (कालिख) कुछ दिनों से सप्ताहों तक, क्षोभमंडलीय ओज़ोन कुछ सप्ताह, मीथेन लगभग एक दशक, और अनेक एचएफ़सी कुछ वर्षों से कुछ दशकों तक। चूँकि ये शीघ्र समाप्त हो जाते हैं, इन्हें घटाने से कुछ ही वर्षों में तापन धीमा होता है, और चूँकि इनमें से कई -- कालिख और भू-स्तरीय ओज़ोन -- स्वास्थ्य और फ़सलों को भी हानि पहुँचाते हैं, इसलिए कटौती से स्थानीय लाभ भी मिलते हैं; यूएनईपी और जलवायु एवं स्वच्छ वायु गठबंधन, जिससे भारत 2019 में जुड़ा, का अनुमान है कि त्वरित कार्रवाई से सदी के मध्य तक लगभग 0.6 °C तापन टल सकता है। "
  "कार्बन डाइऑक्साइड दीर्घजीवी गैस है: हर उत्सर्जन का बड़ा भाग सदियों तक रहता है, इसलिए इसका तापन संचित होता जाता है, इसीलिए अल्पकालिक प्रदूषकों से निपटने के बाद भी कार्बन डाइऑक्साइड में गहरी कटौती आवश्यक बनी रहती है।",
  "UNEP and WMO, Integrated Assessment of Black Carbon and Tropospheric Ozone (2011); Climate and Clean Air Coalition; IPCC, AR6 Working Group I, Chapter 6.",
  "l4-s01-env-slcp-not-co2-methane-black-carbon-ozone", pos=3, craft="application")

# ---------------------------------------------------------------- Climate Science & Mitigation (statement, medium)
S("Climate Science & Mitigation", "medium", "With reference to methane hydrates, consider the following statements:",
  "मीथेन हाइड्रेट के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["They are ice-like solids in which molecules of methane are trapped in a cage of water molecules.",
   "They remain stable only at low temperatures and high pressures, as in permafrost and in sediments beneath the sea floor.",
   "Hydrate deposits have been found in the Krishna-Godavari basin off India's east coast."],
  ["ये बर्फ़ जैसे ठोस हैं जिनमें मीथेन के अणु पानी के अणुओं के पिंजरे में फँसे होते हैं।",
   "ये केवल निम्न तापमान और उच्च दाब पर, जैसे पर्माफ़्रॉस्ट में और समुद्र तल के नीचे के अवसादों में, स्थिर रहते हैं।",
   "भारत के पूर्वी तट के पास कृष्णा-गोदावरी बेसिन में हाइड्रेट निक्षेप पाए गए हैं।"],
  C3, 2,
  "All three statements are correct. Methane hydrates (clathrates) hold large amounts of methane in a lattice of frozen water; a cubic metre of hydrate releases about 160 cubic metres of gas. They form where it is cold and the pressure is high -- in Arctic permafrost and in the sediments of continental margins below a few hundred metres of water. India's National Gas Hydrate Programme found substantial deposits in the Krishna-Godavari basin, as well as in the Mahanadi basin and off the Andamans, which is why hydrates are studied as a possible future source of gas. "
  "They also matter for climate: warming of the oceans and of permafrost can destabilise them and release methane, a strong greenhouse gas -- a possible feedback that would add to warming -- and their sudden break-up can trigger undersea landslides.",
  "तीनों कथन सही हैं। मीथेन हाइड्रेट (क्लैथ्रेट) जमे पानी की जाली में मीथेन की बड़ी मात्रा रखते हैं; एक घन मीटर हाइड्रेट से लगभग 160 घन मीटर गैस निकलती है। ये वहाँ बनते हैं जहाँ ठंड हो और दाब अधिक हो -- आर्कटिक पर्माफ़्रॉस्ट में और कुछ सौ मीटर पानी के नीचे महाद्वीपीय सीमांतों के अवसादों में। भारत के राष्ट्रीय गैस हाइड्रेट कार्यक्रम ने कृष्णा-गोदावरी बेसिन में, और महानदी बेसिन तथा अंडमान के पास भी, बड़े निक्षेप पाए, इसलिए हाइड्रेटों का अध्ययन गैस के संभावित भावी स्रोत के रूप में होता है। "
  "जलवायु के लिए भी ये महत्त्वपूर्ण हैं: महासागरों और पर्माफ़्रॉस्ट के गर्म होने से ये अस्थिर होकर मीथेन छोड़ सकते हैं, जो एक प्रबल ग्रीनहाउस गैस है -- तापन को बढ़ाने वाला एक संभावित प्रतिपुष्टि चक्र -- और इनके अचानक टूटने से समुद्र के नीचे भूस्खलन हो सकते हैं।",
  "Ministry of Petroleum and Natural Gas and Directorate General of Hydrocarbons, National Gas Hydrate Programme (NGHP-01 and NGHP-02); IPCC, AR6 Working Group I, permafrost and methane.",
  "l4-s01-env-methane-hydrates-clathrate-kg-basin", craft="linkage")

# ---------------------------------------------------------------- Ecosystems & Ecological Processes (statement, medium)
S("Ecosystems & Ecological Processes", "medium", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Bioaccumulation refers to the rise in the concentration of a substance from one trophic level to the next.",
   "Biomagnification is most marked for substances that are persistent and soluble in fat.",
   "Methylmercury does not biomagnify in aquatic food chains, because it is not soluble in fat."],
  ["जैव-संचयन किसी पदार्थ की सांद्रता के एक पोषण स्तर से अगले पोषण स्तर तक बढ़ने को कहते हैं।",
   "जैव-आवर्धन उन पदार्थों में सबसे स्पष्ट होता है जो स्थायी और वसा में घुलनशील हैं।",
   "मिथाइल-पारा जलीय खाद्य शृंखलाओं में जैव-आवर्धित नहीं होता, क्योंकि यह वसा में घुलनशील नहीं है।"],
  C3, 0,
  "Only statement 2 is correct. Biomagnification -- the rise in concentration up the food chain -- is strongest for substances that the body cannot break down or excrete easily and that dissolve in fat, such as DDT, PCBs and methylmercury; this is why top predators such as fish-eating birds and orcas carry the highest loads. "
  "Statement 1 is wrong: it describes biomagnification. Bioaccumulation is the build-up of a substance within a single organism over its lifetime, because it is taken in faster than it is lost; biomagnification is what happens when bioaccumulating substances pass up the trophic levels. Statement 3 is wrong: methylmercury binds to proteins in muscle and is retained, so it does biomagnify -- which is why large, long-lived predatory fish such as tuna and swordfish carry the highest levels and health agencies advise pregnant women to limit them; the Minamata disaster in Japan was caused this way.",
  "केवल कथन 2 सही है। जैव-आवर्धन -- खाद्य शृंखला में ऊपर की ओर सांद्रता का बढ़ना -- उन पदार्थों में सबसे प्रबल होता है जिन्हें शरीर आसानी से तोड़ या बाहर नहीं निकाल सकता और जो वसा में घुलते हैं, जैसे डीडीटी, पीसीबी और मिथाइल-पारा; इसीलिए मछली खाने वाले पक्षी और ओर्का जैसे शीर्ष परभक्षियों में इनकी मात्रा सबसे अधिक होती है। "
  "कथन 1 ग़लत है: यह जैव-आवर्धन का वर्णन है। जैव-संचयन किसी एक जीव के भीतर उसके जीवनकाल में किसी पदार्थ का जमा होना है, क्योंकि वह जितनी तेज़ी से निकलता है उससे अधिक तेज़ी से ग्रहण होता है; जैव-आवर्धन तब होता है जब ऐसे संचयी पदार्थ पोषण स्तरों में ऊपर जाते हैं। कथन 3 ग़लत है: मिथाइल-पारा मांसपेशियों के प्रोटीनों से बँधकर रुका रहता है, इसलिए यह जैव-आवर्धित होता है -- इसीलिए टूना और स्वोर्डफ़िश जैसी बड़ी, दीर्घजीवी परभक्षी मछलियों में इसकी मात्रा सबसे अधिक होती है और स्वास्थ्य एजेंसियाँ गर्भवती महिलाओं को इन्हें सीमित करने की सलाह देती हैं; जापान की मिनामाता त्रासदी इसी प्रकार हुई थी।",
  "NCERT, Biology (Class XII), Chapter 16 of the earlier edition (Environmental Issues); UNEP, Global Mercury Assessment (2018).",
  "l4-s01-env-bioaccumulation-vs-biomagnification-methylmercury", craft="precision")

# ---------------------------------------------------------------- Fauna & Animal Behaviour (statement, easy)
S("Fauna & Animal Behaviour", "easy", "With reference to the nilgai, consider the following statements:",
  "नीलगाय के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is the largest antelope of Asia.",
   "It lives mainly in the dense evergreen forests of north-eastern India.",
   "It is listed as Endangered on the IUCN Red List."],
  ["यह एशिया का सबसे बड़ा मृग है।",
   "यह मुख्यतः उत्तर-पूर्वी भारत के घने सदाबहार वनों में रहती है।",
   "यह आईयूसीएन की रेड लिस्ट में संकटग्रस्त सूचीबद्ध है।"],
  C3, 0,
  "Only statement 1 is correct. The nilgai, or blue bull, is Asia's largest antelope; adult males are bluish-grey and females tawny. "
  "Statement 2 is wrong: it prefers open forests, scrub and grasslands and has adapted to farmland across northern and central India and the Terai, avoiding dense forest. Statement 3 is wrong: it is listed as Least Concern, because it is common and widespread; indeed in several States it is a major crop pest, and some have had it declared vermin in specified areas under the Wildlife (Protection) Act so that it can be culled -- a striking contrast with its relatives the four-horned antelope and the blackbuck, which are far more restricted.",
  "केवल कथन 1 सही है। नीलगाय, या ब्लू बुल, एशिया का सबसे बड़ा मृग है; वयस्क नर नीले-भूरे और मादाएँ हल्के भूरे रंग की होती हैं। "
  "कथन 2 ग़लत है: यह खुले वनों, झाड़ियों और घास के मैदानों को पसंद करती है और उत्तरी तथा मध्य भारत और तराई के खेतों के अनुरूप ढल गई है, घने वनों से बचती है। कथन 3 ग़लत है: यह न्यूनतम चिंता की श्रेणी में है, क्योंकि यह सामान्य और व्यापक है; वस्तुतः कई राज्यों में यह फ़सलों की बड़ी हानिकारक है, और कुछ ने वन्यजीव (संरक्षण) अधिनियम के अंतर्गत इसे निर्दिष्ट क्षेत्रों में पीड़क घोषित कराया है ताकि इसकी संख्या घटाई जा सके -- इसके संबंधी चौसिंगा और काले हिरण से यह बड़ा अंतर है, जो कहीं अधिक सीमित हैं।",
  "IUCN Red List, Boselaphus tragocamelus; Wildlife (Protection) Act, 1972, section 62.",
  "l4-s01-env-nilgai-largest-antelope-open-habitat-least-concern", craft="recall")

# ---------------------------------------------------------------- Fauna & Animal Behaviour (statement, hard)
S("Fauna & Animal Behaviour", "hard", "Consider the following statements about primates of India:",
  "भारत के प्राइमेट के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The stump-tailed macaque is found in India only in the north-eastern States.",
   "The capped langur occurs in India mainly in the north-eastern States.",
   "The Nilgiri langur is endemic to the Eastern Ghats."],
  ["भारत में स्टंप-टेल्ड मकाक केवल उत्तर-पूर्वी राज्यों में पाया जाता है।",
   "भारत में कैप्ड लंगूर मुख्यतः उत्तर-पूर्वी राज्यों में पाया जाता है।",
   "नीलगिरि लंगूर पूर्वी घाट का स्थानिक है।"],
  C3, 1,
  "Statements 1 and 2 are correct. North-east India, at the meeting point of the Indian, Himalayan and Indo-Malayan biogeographic realms, has the country's richest primate fauna: besides the western hoolock gibbon, India's only ape, it holds the stump-tailed macaque, the pig-tailed and Assamese macaques, the capped langur and Gee's golden langur, as well as the Bengal slow loris. "
  "Statement 3 is wrong: the Nilgiri langur, a glossy black leaf monkey with a brown head, is endemic to the Western Ghats of Tamil Nadu, Kerala and Karnataka, which it shares with the lion-tailed macaque. The pattern -- distinct primate assemblages in the north-east and the Western Ghats -- mirrors the two regions' status as biodiversity hotspots.",
  "कथन 1 और 2 सही हैं। भारतीय, हिमालयी और इंडो-मलय जैव-भौगोलिक परिमंडलों के मिलन-बिंदु पर स्थित उत्तर-पूर्वी भारत में देश का सबसे समृद्ध प्राइमेट जीवन है: भारत के एकमात्र कपि पश्चिमी हूलॉक गिबन के अलावा यहाँ स्टंप-टेल्ड मकाक, पिग-टेल्ड और असमिया मकाक, कैप्ड लंगूर और गी का सुनहरा लंगूर, तथा बंगाल स्लो लोरिस भी हैं। "
  "कथन 3 ग़लत है: भूरे सिर वाला चमकीला काला पत्ती-भक्षी बंदर नीलगिरि लंगूर तमिलनाडु, केरल और कर्नाटक के पश्चिमी घाट का स्थानिक है, जिसे यह शेर-पूँछ मकाक के साथ साझा करता है। यह प्रतिरूप -- उत्तर-पूर्व और पश्चिमी घाट में अलग-अलग प्राइमेट समूह -- दोनों क्षेत्रों के जैव-विविधता हॉटस्पॉट होने को दर्शाता है।",
  "Zoological Survey of India, primates of India; IUCN Red List: Macaca arctoides, Trachypithecus pileatus, Semnopithecus johnii.",
  "l4-s01-env-ne-primates-stump-tailed-capped-nilgiri-langur", craft="precision")

# ---------------------------------------------------------------- Fauna & Animal Behaviour (statement, medium)
S("Fauna & Animal Behaviour", "medium", "With reference to the decline of vultures in India, consider the following statements:",
  "भारत में गिद्धों की संख्या घटने के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Besides diclofenac, the veterinary use of the painkillers ketoprofen and aceclofenac has been banned because they too are toxic to vultures.",
   "Meloxicam is considered safe for vultures and is recommended as an alternative for treating livestock.",
   "Vultures are poisoned mainly by eating grain treated with pesticides."],
  ["डाइक्लोफ़ेनाक के अतिरिक्त दर्दनिवारक कीटोप्रोफ़ेन और एसिक्लोफ़ेनाक का पशु-चिकित्सीय उपयोग भी प्रतिबंधित किया गया है क्योंकि वे भी गिद्धों के लिए विषैले हैं।",
   "मेलॉक्सिकैम को गिद्धों के लिए सुरक्षित माना जाता है और पशुओं के उपचार के विकल्प के रूप में इसकी संस्तुति की जाती है।",
   "गिद्ध मुख्यतः कीटनाशक लगे अनाज खाने से विषाक्त होते हैं।"],
  C3, 1,
  "Statements 1 and 2 are correct. India's vulture populations crashed by more than 95 per cent in the 1990s and 2000s because the birds fed on carcasses of cattle treated with diclofenac, which causes kidney failure in Gyps vultures; its veterinary use was banned in 2006. Studies showed that other non-steroidal painkillers were also lethal, so the Health Ministry banned ketoprofen and aceclofenac for animal use in 2023 under the Drugs and Cosmetics Act, and nimesulide followed; meloxicam, which vultures tolerate, is the recommended substitute. "
  "Statement 3 is wrong: vultures are scavengers that feed on carcasses, and the drug residues in dead livestock -- not grain -- poisoned them. Their loss allowed carcasses to rot and feral dog populations to grow, with costs to public health; a 2024 study estimated that the collapse led to about half a million additional human deaths between 2000 and 2005.",
  "कथन 1 और 2 सही हैं। 1990 और 2000 के दशकों में भारत में गिद्धों की संख्या 95 प्रतिशत से अधिक घट गई, क्योंकि वे डाइक्लोफ़ेनाक से उपचारित पशुओं के शव खाते थे, जो जिप्स गिद्धों में गुर्दे की विफलता करता है; 2006 में इसका पशु-चिकित्सीय उपयोग प्रतिबंधित हुआ। अध्ययनों ने दिखाया कि अन्य गैर-स्टेरॉयडी दर्दनिवारक भी घातक थे, इसलिए स्वास्थ्य मंत्रालय ने 2023 में औषधि और प्रसाधन सामग्री अधिनियम के अंतर्गत कीटोप्रोफ़ेन और एसिक्लोफ़ेनाक को पशु-उपयोग के लिए प्रतिबंधित किया, और फिर निमेसुलाइड पर भी रोक लगी; गिद्ध जिसे सह लेते हैं वह मेलॉक्सिकैम अनुशंसित विकल्प है। "
  "कथन 3 ग़लत है: गिद्ध शव खाने वाले मृतोपजीवी हैं, और उन्हें अनाज ने नहीं, मृत पशुओं में बची दवाओं ने विषाक्त किया। उनके घटने से शव सड़ने लगे और आवारा कुत्तों की संख्या बढ़ी, जिसकी जन-स्वास्थ्य को क़ीमत चुकानी पड़ी; 2024 के एक अध्ययन का अनुमान है कि इस गिरावट से 2000 से 2005 के बीच लगभग पाँच लाख अतिरिक्त मानवीय मौतें हुईं।",
  "Ministry of Health and Family Welfare, notification under section 26A of the Drugs and Cosmetics Act, 1940 (31 July 2023); MoEFCC, Action Plan for Vulture Conservation in India 2020-25.",
  "l4-s01-env-vultures-ketoprofen-aceclofenac-meloxicam-carcass", craft="linkage")

# ---------------------------------------------------------------- Flora, Fungi & Forests (MCQ, easy)
M("Flora, Fungi & Forests", "easy",
  "Which one of the following invasive plants, known as the 'mile-a-minute weed', smothers native vegetation in the forests of north-east India and Kerala?",
  "निम्नलिखित में से कौन-सा आक्रामक पौधा, जिसे ‘माइल-ए-मिनट वीड’ कहा जाता है, उत्तर-पूर्वी भारत और केरल के वनों में देशी वनस्पति को ढक लेता है?",
  ["Mikania micrantha", "Lantana camara", "Prosopis juliflora", "Parthenium hysterophorus"],
  ["माइकेनिया माइक्रांथा", "लैंटाना कैमारा", "प्रोसोपिस जूलीफ़्लोरा", "पार्थेनियम हिस्टेरोफ़ोरस"],
  0,
  "Mikania micrantha, a creeper from Central and South America, grows so fast -- its name comes from the claim that it can spread a mile a minute -- that it climbs over shrubs and young trees and cuts off their light. It is a serious weed in plantations, in tiger reserves such as Kaziranga and in Kerala's forests, and it spread widely after it was introduced in the Second World War to camouflage airfields. "
  "Lantana camara, a shrub from tropical America, is the most widespread invader of India's dry forests; Prosopis juliflora, a thorny tree brought in to green deserts, has taken over grasslands such as Banni in Kutch; Parthenium, the 'congress grass', is a weed of wasteland that causes allergies. All four show how species introduced for a purpose, or by accident, escape and spread without the natural enemies of their native range.",
  "मध्य और दक्षिण अमेरिका की लता माइकेनिया माइक्रांथा इतनी तेज़ी से बढ़ती है -- इसका नाम इस दावे से आया कि यह एक मिनट में एक मील फैल सकती है -- कि यह झाड़ियों और नए पेड़ों पर चढ़कर उनका प्रकाश रोक देती है। यह बाग़ानों में, काज़ीरंगा जैसे बाघ अभयारण्यों में और केरल के वनों में गंभीर खरपतवार है, और द्वितीय विश्व युद्ध में हवाई अड्डों को छिपाने के लिए लाए जाने के बाद यह व्यापक रूप से फैली। "
  "उष्णकटिबंधीय अमेरिका की झाड़ी लैंटाना कैमारा भारत के शुष्क वनों की सबसे व्यापक आक्रामक प्रजाति है; मरुस्थलों को हरा करने के लिए लाया गया कँटीला पेड़ प्रोसोपिस जूलीफ़्लोरा कच्छ के बन्नी जैसे घास के मैदानों पर छा गया है; ‘कांग्रेस घास’ पार्थेनियम बंजर भूमि की खरपतवार है जो एलर्जी करती है। चारों दिखाती हैं कि किसी उद्देश्य से या दुर्घटनावश लाई गई प्रजातियाँ अपने मूल क्षेत्र के प्राकृतिक शत्रुओं के बिना कैसे फैल जाती हैं।",
  "Botanical Survey of India, invasive alien flora of India; Kerala Forest Research Institute, Mikania micrantha in Kerala's forests.",
  "l4-s01-env-mikania-mile-a-minute-weed", pos=2, craft="recall")

# ---------------------------------------------------------------- Flora, Fungi & Forests (statement, medium)
S("Flora, Fungi & Forests", "medium", "Some fungi found in the forests of the Western Ghats and north-east India glow in the dark. Consider the following statements:",
  "पश्चिमी घाट और उत्तर-पूर्वी भारत के वनों में पाई जाने वाली कुछ कवक अँधेरे में चमकती हैं। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The light is produced by a chemical reaction in which an enzyme oxidises a light-emitting molecule.",
   "The light is produced by bacteria living inside the fungus, not by the fungus itself.",
   "The glow depends on sunlight absorbed during the day and given off slowly at night."],
  ["प्रकाश एक रासायनिक अभिक्रिया से उत्पन्न होता है जिसमें एक एंज़ाइम प्रकाश उत्सर्जित करने वाले अणु का ऑक्सीकरण करता है।",
   "प्रकाश कवक स्वयं नहीं, उसके भीतर रहने वाले जीवाणु उत्पन्न करते हैं।",
   "चमक दिन में अवशोषित सूर्य-प्रकाश पर निर्भर करती है जो रात में धीरे-धीरे निकलता है।"],
  C3, 0,
  "Only statement 1 is correct. Fungal bioluminescence is a chemical reaction: an enzyme, luciferase, oxidises a luciferin molecule (in fungi a compound derived from caffeic acid) and the energy is released as greenish light. Species of Mycena and related genera glow in India's wet forests, and a new glowing mushroom, Roridomyces phyllostachydis, was described from Meghalaya in 2020. "
  "Statement 2 is wrong: unlike many glowing marine animals, which host luminous bacteria, these fungi make the light themselves. Statement 3 is wrong: the glow is not phosphorescence and needs no stored sunlight; it is chemical and continuous, and one hypothesis is that it attracts insects that spread the spores at night.",
  "केवल कथन 1 सही है। कवकीय जैव-संदीप्ति एक रासायनिक अभिक्रिया है: एक एंज़ाइम, ल्यूसिफ़ेरेज़, ल्यूसिफ़ेरिन अणु (कवकों में कैफ़ीक अम्ल से बना एक यौगिक) का ऑक्सीकरण करता है और ऊर्जा हरे प्रकाश के रूप में निकलती है। भारत के नम वनों में माइसीना और संबंधित वंशों की प्रजातियाँ चमकती हैं, और मेघालय से 2020 में एक नया चमकने वाला मशरूम, रोरिडोमाइसीस फ़ाइलोस्टैकिडिस, वर्णित हुआ। "
  "कथन 2 ग़लत है: अनेक चमकने वाले समुद्री जीवों के विपरीत, जिनमें संदीप्त जीवाणु रहते हैं, ये कवक प्रकाश स्वयं बनाते हैं। कथन 3 ग़लत है: चमक स्फुरदीप्ति नहीं है और इसे संचित सूर्य-प्रकाश की आवश्यकता नहीं; यह रासायनिक और निरंतर है, और एक परिकल्पना यह है कि यह उन कीटों को आकर्षित करती है जो रात में बीजाणु फैलाते हैं।",
  "Botanical Survey of India; Karunarathna, S. C. et al., 'Roridomyces phyllostachydis, a new bioluminescent fungus from India', Phytotaxa (2020); Kotlobay, A. A. et al., 'Genetically encodable bioluminescent system from fungi', PNAS (2018).",
  "l4-s01-env-bioluminescent-fungi-luciferase-not-bacteria", craft="inference")

# ---------------------------------------------------------------- Indian Environmental Laws & Bodies (pairs, hard)
P("Indian Environmental Laws & Bodies", "hard", "Consider the following pairs of concepts in Indian environmental law and their source:",
  "भारतीय पर्यावरण विधि की अवधारणाओं और उनके स्रोत के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["'Forest' in its dictionary meaning, whatever the ownership of the land : The Supreme Court's orders in T. N. Godavarman Thirumulpad",
   "Community forest resource rights of gram sabhas : The Forest Rights Act, 2006",
   "Eco-sensitive zones around protected areas : Notifications under the Environment (Protection) Act, 1986",
   "The fund into which compensatory afforestation levies are paid : The Wild Life (Protection) Act, 1972"],
  ["भूमि के स्वामित्व से निरपेक्ष, शब्दकोशीय अर्थ में ‘वन’ : टी. एन. गोदावर्मन थिरुमुलपाद में सर्वोच्च न्यायालय के आदेश",
   "ग्राम सभाओं के सामुदायिक वन संसाधन अधिकार : वन अधिकार अधिनियम, 2006",
   "संरक्षित क्षेत्रों के चारों ओर पारिस्थितिकी-संवेदी क्षेत्र : पर्यावरण (संरक्षण) अधिनियम, 1986 के अंतर्गत अधिसूचनाएँ",
   "वह कोष जिसमें प्रतिपूरक वनीकरण की राशियाँ जमा होती हैं : वन्यजीव (संरक्षण) अधिनियम, 1972"],
  2,
  "Only three pairs are correct. In 1996 the Supreme Court held in T. N. Godavarman Thirumulpad that the Forest Conservation Act applies to all forests in the dictionary sense and to areas recorded as forest, whatever their ownership -- the origin of the term 'deemed forests'. The Forest Rights Act, 2006 recognises the right of gram sabhas to protect, regenerate and manage their community forest resources. Eco-sensitive zones around national parks and sanctuaries are notified by the Environment Ministry under the Environment (Protection) Act and its rules, as buffers regulating activities rather than banning them outright. "
  "Pair 4 is wrong: compensatory afforestation money, which users of forest land pay for diversion, goes into the National and State Compensatory Afforestation Funds under the Compensatory Afforestation Fund Act, 2016, which gave statutory form to the ad hoc CAMPA set up on the Court's orders. Many of India's forest rules thus come from a mix of statute and judicial orders.",
  "केवल तीन युग्म सही हैं। 1996 में टी. एन. गोदावर्मन थिरुमुलपाद में सर्वोच्च न्यायालय ने कहा कि वन संरक्षण अधिनियम शब्दकोशीय अर्थ वाले सभी वनों और वन के रूप में अभिलिखित क्षेत्रों पर, स्वामित्व से निरपेक्ष, लागू होता है -- यही ‘मानित वनों’ शब्द का स्रोत है। वन अधिकार अधिनियम, 2006 ग्राम सभाओं के अपने सामुदायिक वन संसाधनों की रक्षा, पुनर्जनन और प्रबंधन के अधिकार को मान्यता देता है। राष्ट्रीय उद्यानों और अभयारण्यों के चारों ओर पारिस्थितिकी-संवेदी क्षेत्र पर्यावरण मंत्रालय पर्यावरण (संरक्षण) अधिनियम और उसके नियमों के अंतर्गत अधिसूचित करता है, जो गतिविधियों को पूरी तरह रोकने के बजाय विनियमित करने वाले मध्यवर्ती क्षेत्र हैं। "
  "युग्म 4 ग़लत है: वन भूमि के उपयोगकर्ता उसके अपवर्तन के लिए जो प्रतिपूरक वनीकरण राशि देते हैं, वह प्रतिपूरक वनीकरण कोष अधिनियम, 2016 के अंतर्गत राष्ट्रीय और राज्य प्रतिपूरक वनीकरण कोषों में जाती है, जिसने न्यायालय के आदेशों पर बने तदर्थ कैम्पा को सांविधिक रूप दिया। इस प्रकार भारत के अनेक वन नियम क़ानून और न्यायिक आदेशों के मेल से बने हैं।",
  "T. N. Godavarman Thirumulpad v. Union of India (1996) 2 SCC 267; Scheduled Tribes and Other Traditional Forest Dwellers (Recognition of Forest Rights) Act, 2006, section 3(1)(i); Environment (Protection) Act, 1986; Compensatory Afforestation Fund Act, 2016.",
  "l4-s01-env-laws-deemed-forest-cfr-esz-caf-pairs", craft="linkage")

# ---------------------------------------------------------------- International Conventions & Organisations (AR, hard)
A("International Conventions & Organisations", "hard",
  "Owners of large ships can be held liable for pollution caused by a spill of the ship's own fuel oil, even when the ship is not an oil tanker.",
  "बड़े जहाज़ों के स्वामियों को जहाज़ के अपने ईंधन तेल के रिसाव से हुए प्रदूषण के लिए उत्तरदायी ठहराया जा सकता है, भले ही जहाज़ तेल टैंकर न हो।",
  "The International Maritime Organization's Bunker Convention requires the registered owners of ships above 1,000 gross tonnage to keep insurance against pollution damage caused by bunker oil.",
  "अंतरराष्ट्रीय समुद्री संगठन का बंकर अभिसमय 1,000 सकल टन भार से बड़े जहाज़ों के पंजीकृत स्वामियों से बंकर तेल के कारण होने वाली प्रदूषण-क्षति के विरुद्ध बीमा रखने की अपेक्षा करता है।",
  0,
  "Both statements are correct, and Statement II explains Statement I. The older civil liability conventions covered oil carried as cargo by tankers; but every large ship -- container ship, bulk carrier or passenger vessel -- carries hundreds or thousands of tonnes of heavy fuel ('bunkers'), and spills of it from groundings are frequent. The Bunker Convention (2001, in force 2008) closed this gap: it makes the shipowner strictly liable for such pollution, requires ships over 1,000 gross tonnage to carry insurance and lets victims claim directly against the insurer. "
  "India is a party and gives it effect through its merchant shipping law, which matters for a coast where cargo ships have run aground or sunk in the monsoon, as off Mumbai and Kerala.",
  "दोनों कथन सही हैं, और कथन II कथन I की व्याख्या करता है। पुराने नागरिक दायित्व अभिसमय टैंकरों द्वारा माल के रूप में ढोए गए तेल को कवर करते थे; पर हर बड़ा जहाज़ -- कंटेनर पोत, थोक वाहक या यात्री पोत -- सैकड़ों या हज़ारों टन भारी ईंधन (‘बंकर’) ले जाता है, और ज़मीन पर चढ़ने से इसके रिसाव आम हैं। बंकर अभिसमय (2001, 2008 से प्रवृत्त) ने यह कमी दूर की: यह ऐसे प्रदूषण के लिए जहाज़-स्वामी को कठोर रूप से उत्तरदायी बनाता है, 1,000 सकल टन भार से बड़े जहाज़ों के लिए बीमा अनिवार्य करता है और पीड़ितों को सीधे बीमाकर्ता से दावा करने देता है। "
  "भारत इसका पक्षकार है और अपनी वाणिज्य पोत परिवहन विधि से इसे प्रभावी करता है, जो ऐसे तट के लिए महत्त्वपूर्ण है जहाँ मानसून में मालवाहक जहाज़ ज़मीन पर चढ़े या डूबे हैं, जैसे मुंबई और केरल के पास।",
  "International Maritime Organization, International Convention on Civil Liability for Bunker Oil Pollution Damage, 2001; Merchant Shipping Act, 2025.",
  "l4-s01-env-bunker-convention-fuel-oil-liability-insurance", craft="inference")

# ---------------------------------------------------------------- Pollution, Waste & Resources (statement, easy)
S("Pollution, Waste & Resources", "easy", "With reference to hydrochlorofluorocarbons (HCFCs), consider the following statements:",
  "हाइड्रोक्लोरोफ़्लोरोकार्बन (एचसीएफ़सी) के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["They deplete the ozone layer, though less than chlorofluorocarbons do.",
   "They are being phased out under the Montreal Protocol.",
   "India completed the phase-out of HCFC-141b, used to make foam, in 2020."],
  ["ये ओज़ोन परत का क्षय करते हैं, यद्यपि क्लोरोफ़्लोरोकार्बन से कम।",
   "मॉन्ट्रियल प्रोटोकॉल के अंतर्गत इन्हें चरणबद्ध रूप से समाप्त किया जा रहा है।",
   "भारत ने फ़ोम बनाने में प्रयुक्त एचसीएफ़सी-141बी का चरणबद्ध उन्मूलन 2020 में पूरा किया।"],
  C3, 2,
  "All three statements are correct. HCFCs were introduced as 'transitional' substitutes for CFCs: because their molecules contain hydrogen, most of them break down in the lower atmosphere, so far less chlorine reaches the stratosphere, but they still deplete ozone and are potent greenhouse gases. Under the Montreal Protocol developed countries have almost eliminated them, and developing countries, India among them, are phasing them out by about 2030. "
  "India eliminated HCFC-141b, a foam-blowing agent and its most-used HCFC, on 1 January 2020, among the first developing countries to do so; its HCFC Phase-out Management Plan now targets refrigeration and air-conditioning, where the substitutes must avoid both ozone depletion and high warming potential.",
  "तीनों कथन सही हैं। एचसीएफ़सी को सीएफ़सी के ‘संक्रमणकालीन’ विकल्प के रूप में लाया गया था: इनके अणुओं में हाइड्रोजन होने से अधिकांश निचले वायुमंडल में टूट जाते हैं, इसलिए समताप मंडल तक बहुत कम क्लोरीन पहुँचती है, पर ये फिर भी ओज़ोन का क्षय करते हैं और प्रबल ग्रीनहाउस गैसें हैं। मॉन्ट्रियल प्रोटोकॉल के अंतर्गत विकसित देशों ने इन्हें लगभग समाप्त कर दिया है, और भारत सहित विकासशील देश इन्हें लगभग 2030 तक समाप्त कर रहे हैं। "
  "भारत ने अपने सबसे अधिक प्रयुक्त एचसीएफ़सी, फ़ोम बनाने वाले एचसीएफ़सी-141बी, को 1 जनवरी 2020 को समाप्त किया, ऐसा करने वाले पहले विकासशील देशों में; उसकी एचसीएफ़सी उन्मूलन प्रबंधन योजना अब प्रशीतन और वातानुकूलन पर केंद्रित है, जहाँ विकल्पों को ओज़ोन-क्षय और उच्च तापन क्षमता दोनों से बचना है।",
  "MoEFCC (Ozone Cell), HCFC Phase-out Management Plan and the phase-out of HCFC-141b (PIB, January 2020); UNEP Ozone Secretariat, Montreal Protocol control schedules.",
  "l4-s01-env-hcfc-transitional-phaseout-141b-2020", craft="recall")

# ---------------------------------------------------------------- Pollution, Waste & Resources (statement, medium)
S("Pollution, Waste & Resources", "medium", "With reference to the loss of oxygen in the oceans, consider the following statements:",
  "महासागरों में ऑक्सीजन की कमी के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["The loss of oxygen in the open ocean is caused only by nutrients washed in from the land.",
   "Warming of the surface weakens the stratification of the ocean and so increases the mixing of oxygen into deeper layers.",
   "The largest oxygen minimum zones are found in the surface waters of the polar seas."],
  ["खुले महासागर में ऑक्सीजन की कमी केवल भूमि से बहकर आए पोषक तत्वों से होती है।",
   "सतह के गर्म होने से महासागर का स्तरीकरण कमज़ोर होता है और इस प्रकार गहरी परतों में ऑक्सीजन का मिश्रण बढ़ता है।",
   "सबसे बड़े ऑक्सीजन-न्यूनतम क्षेत्र ध्रुवीय समुद्रों के सतही जल में पाए जाते हैं।"],
  C3, 3,
  "None of the statements is correct. Statement 1 is wrong: nutrient run-off creates coastal 'dead zones', but in the open ocean the main driver is warming -- gases dissolve less in warmer water, so warming alone lowers the oxygen content of the sea. Statement 2 reverses the effect: a warmer, lighter surface layer sits more firmly on the colder water below, so warming strengthens stratification and reduces the mixing that carries oxygen down. Together with nutrient run-off near coasts, which fuels algal blooms whose decay uses up oxygen, these processes have cut the ocean's oxygen by about two per cent since 1960. "
  "Statement 3 is wrong: the largest oxygen minimum zones lie at intermediate depths in the tropical oceans -- the eastern Pacific and the northern Indian Ocean, where the Arabian Sea and the Bay of Bengal hold some of the most intense. They are expanding, squeezing the habitat of fish and changing the nitrogen cycle.",
  "कोई भी कथन सही नहीं है। कथन 1 ग़लत है: पोषक तत्वों का बहाव तटीय ‘मृत क्षेत्र’ बनाता है, पर खुले महासागर में मुख्य कारक तापन है -- गर्म पानी में गैसें कम घुलती हैं, इसलिए केवल गर्म होने से ही समुद्र की ऑक्सीजन घटती है। कथन 2 प्रभाव को उलट देता है: गर्म, हल्की सतही परत नीचे के ठंडे पानी पर और दृढ़ता से टिकती है, इसलिए गर्म होना स्तरीकरण को मज़बूत करता है और ऑक्सीजन को नीचे ले जाने वाले मिश्रण को घटाता है। तटों के पास पोषक तत्वों के बहाव के साथ, जो शैवाल प्रस्फुटन को बढ़ाता है जिनका क्षय ऑक्सीजन खपाता है, इन प्रक्रियाओं ने 1960 से महासागर की ऑक्सीजन लगभग दो प्रतिशत घटा दी है। "
  "कथन 3 ग़लत है: सबसे बड़े ऑक्सीजन-न्यूनतम क्षेत्र उष्णकटिबंधीय महासागरों में मध्यवर्ती गहराइयों पर हैं -- पूर्वी प्रशांत और उत्तरी हिंद महासागर, जहाँ अरब सागर और बंगाल की खाड़ी में कुछ सबसे तीव्र क्षेत्र हैं। ये फैल रहे हैं, जिससे मछलियों का आवास सिकुड़ रहा है और नाइट्रोजन चक्र बदल रहा है।",
  "IPCC, Special Report on the Ocean and Cryosphere in a Changing Climate (2019); IUCN, Ocean deoxygenation: everyone's problem (2019).",
  "l4-s01-env-ocean-deoxygenation-stratification-omz-tropics", craft="inference")

# ---------------------------------------------------------------- Protected Areas & Wildlife Protection (MCQ, medium)
M("Protected Areas & Wildlife Protection", "medium",
  "Which one of the following Ramsar sites is in Gujarat?",
  "निम्नलिखित में से कौन-सा रामसर स्थल गुजरात में है?",
  ["Khijadia", "Deepor Beel", "Ashtamudi", "Pichavaram"],
  ["खिजड़िया", "दीपोर बील", "अष्टमुडी", "पिचावरम"],
  0,
  "Khijadia, near Jamnagar on the Gulf of Kutch, is a freshwater wetland separated from the sea by a bund, so it holds both freshwater and saline habitats close together and draws large numbers of migratory waterbirds; it became a Ramsar site in 2021, along with Thol and Wadhvana, joining Nalsarovar. "
  "Deepor Beel is a lake of the Brahmaputra floodplain at Guwahati, Assam's only Ramsar site for many years; Ashtamudi is an estuarine backwater of Kerala at Kollam; Pichavaram, in Tamil Nadu between the Vellar and Kollidam estuaries, is among India's largest mangrove forests and was designated in 2022. Ramsar designation obliges the country to promote the 'wise use' of the wetland, but it is not a protected-area category under Indian law.",
  "जामनगर के पास कच्छ की खाड़ी पर स्थित खिजड़िया एक मीठे पानी की आर्द्रभूमि है जो एक बाँध से समुद्र से अलग है, इसलिए इसमें मीठे और खारे पानी के आवास पास-पास हैं और यह बड़ी संख्या में प्रवासी जल-पक्षियों को आकर्षित करती है; यह 2021 में थोल और वढवाणा के साथ रामसर स्थल बनी, नलसरोवर से जुड़ते हुए। "
  "दीपोर बील गुवाहाटी में ब्रह्मपुत्र के बाढ़ के मैदान की एक झील है, जो लंबे समय तक असम का एकमात्र रामसर स्थल रही; अष्टमुडी कोल्लम में केरल का एक ज्वारनदमुखी पश्चजल है; वेल्लार और कोल्लिडम ज्वारनदमुखों के बीच तमिलनाडु का पिचावरम भारत के सबसे बड़े मैंग्रोव वनों में है और 2022 में नामित हुआ। रामसर नामांकन देश को आर्द्रभूमि के ‘विवेकपूर्ण उपयोग’ को बढ़ावा देने के लिए बाध्य करता है, पर यह भारतीय विधि में संरक्षित क्षेत्र की कोई श्रेणी नहीं है।",
  "Ramsar Sites Information Service: Khijadia Wildlife Sanctuary (2021), Deepor Beel (2002), Ashtamudi Wetland (2002), Pichavaram Mangrove (2022); MoEFCC, Ramsar sites of India.",
  "l4-s01-env-ramsar-khijadia-gujarat-deepor-ashtamudi-pichavaram", pos=1, craft="precision")

# ---------------------------------------------------------------- Protected Areas & Wildlife Protection (statement, medium)
S("Protected Areas & Wildlife Protection", "medium", "With reference to tiger reserves of India, consider the following statements:",
  "भारत के बाघ अभयारण्यों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Melghat tiger reserve lies in the Satpura range in Maharashtra.",
   "Sathyamangalam tiger reserve links the Western Ghats with the Eastern Ghats.",
   "The Kali tiger reserve lies in the Eastern Ghats of Andhra Pradesh."],
  ["मेलघाट बाघ अभयारण्य महाराष्ट्र में सतपुड़ा श्रेणी में स्थित है।",
   "सत्यमंगलम बाघ अभयारण्य पश्चिमी घाट को पूर्वी घाट से जोड़ता है।",
   "काली बाघ अभयारण्य आंध्र प्रदेश के पूर्वी घाट में स्थित है।"],
  C3, 1,
  "Statements 1 and 2 are correct. Melghat, in Amravati district, lies in the Gawilgarh hills of the Satpura range and was among the first nine reserves under Project Tiger in 1973-74. Sathyamangalam, in Erode district of Tamil Nadu, sits at the junction of the Western and Eastern Ghats, so it forms a corridor between the tiger populations of the Nilgiri Biosphere Reserve and the forests of the Eastern Ghats -- which is why it was notified as a tiger reserve in 2013. "
  "Statement 3 is wrong: the Kali tiger reserve (formerly Dandeli-Anshi) is in Uttara Kannada district of Karnataka, in the Western Ghats, named after the Kali river that flows through it. Corridors such as Sathyamangalam matter because tiger populations confined to isolated reserves lose genetic diversity.",
  "कथन 1 और 2 सही हैं। अमरावती ज़िले का मेलघाट सतपुड़ा श्रेणी की गाविलगढ़ पहाड़ियों में है और 1973-74 में प्रोजेक्ट टाइगर के पहले नौ अभयारण्यों में था। तमिलनाडु के ईरोड ज़िले का सत्यमंगलम पश्चिमी और पूर्वी घाट के संगम पर है, इसलिए यह नीलगिरि जैवमंडल आरक्षित क्षेत्र और पूर्वी घाट के वनों की बाघ आबादियों के बीच गलियारा बनाता है -- इसी कारण 2013 में इसे बाघ अभयारण्य अधिसूचित किया गया। "
  "कथन 3 ग़लत है: काली बाघ अभयारण्य (पहले दांडेली-अंशी) कर्नाटक के उत्तर कन्नड़ ज़िले में, पश्चिमी घाट में है, और इसका नाम इससे होकर बहने वाली काली नदी पर है। सत्यमंगलम जैसे गलियारे इसलिए महत्त्वपूर्ण हैं कि अलग-थलग अभयारण्यों में सीमित बाघ आबादियाँ आनुवंशिक विविधता खो देती हैं।",
  "National Tiger Conservation Authority, tiger reserves of India; Tamil Nadu Forest Department, Sathyamangalam Tiger Reserve (2013).",
  "l4-s01-env-tiger-reserves-melghat-sathyamangalam-kali", craft="precision")

write("gs_l4_s01_c.sql")
