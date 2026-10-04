# -*- coding: utf-8 -*-
"""Level 2 · Test 21 -- Science & Technology block, rewritten to the depth standard of October 2026
(docs/upsc-question-design-standard.md §6). It updates the 11 draft rows of gs_l2_t21_st.py in place,
with the same blueprint cells.
  - The noble-gas row now pairs each use with the property claimed to explain it (helium and narcosis,
    neon's glow, argon in bulbs), so the student must judge the mechanism, not just the gas.
Most of this block was already built on mechanism: SAF's lifecycle gain, the mirage, dry ice's sublimation,
what two-factor authentication protects, and what incognito mode hides. Every row is tagged.
Craft mix: inference 4, recall 4, application 1, linkage 1, precision 1."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write_updates, CODE
from polity_common import C3, C4, T2

d.SUBJECT = "Science & Technology"
d.REQUIRE_CRAFT = True
EN = "Energy & Environmental Technology"
PH = "Physics & Everyday Science"
BI = "Biology, Health & Biotechnology"
ST = "Space Technology & Missions"
CH = "Chemistry & Materials"
IT = "IT, Communication & Emerging Technologies"
AS = "Astronomy & Earth Science"
DF = "Defence, Aerospace & Security Technology"
MOPNG = "Ministry of Petroleum and Natural Gas"
NC10 = "NCERT Class X, Science"
NC11C = "NCERT Class XI, Chemistry"
ISRO = "Indian Space Research Organisation"
DRDO = "Defence Research and Development Organisation"

# ================================================================ ENERGY (2)
S(EN, "medium", "Consider the following statements about sustainable aviation fuel (SAF):",
  "सतत विमानन ईंधन (Sustainable Aviation Fuel, SAF) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It can be produced from feedstocks such as used cooking oil, crop residue and municipal waste.",
   "As a 'drop-in' fuel, it can be blended with conventional jet fuel and used in existing aircraft engines.",
   "Burning it in an aircraft engine releases no carbon dioxide."],
  ["इसे इस्तेमाल हो चुके खाद्य तेल, फ़सल अवशेष और नगरीय कचरे जैसे कच्चे माल से बनाया जा सकता है।",
   "'ड्रॉप-इन' ईंधन होने के कारण इसे पारंपरिक जेट ईंधन में मिलाकर मौजूदा विमान इंजनों में इस्तेमाल किया जा सकता है।",
   "विमान के इंजन में इसे जलाने पर कोई कार्बन डाइऑक्साइड नहीं निकलती।"],
  C3, 1,
  "Statements 1 and 2 are correct. SAF is chemically so close to kerosene-based jet fuel that it can be blended -- up to 50 per cent under current standards -- without changes to aircraft or airport systems. "
  "Statement 3 is wrong: burning SAF still releases carbon dioxide. Its benefit lies over the whole life cycle, because the carbon in its feedstock was recently drawn from the air by plants, or would otherwise have been released from waste, so net emissions can fall by up to about 80 per cent. "
  "India has announced indicative blending targets for international flights of 1 per cent in 2027 and 2 per cent in 2028.",
  "कथन 1 और 2 सही हैं। SAF रासायनिक रूप से केरोसिन-आधारित जेट ईंधन के इतना क़रीब है कि इसे विमानों या हवाई अड्डे की प्रणालियों में बदलाव के बिना, मौजूदा मानकों के तहत 50 प्रतिशत तक, मिलाया जा सकता है। "
  "कथन 3 गलत है: SAF जलाने पर भी कार्बन डाइऑक्साइड निकलती है। इसका लाभ पूरे जीवन-चक्र में है, क्योंकि इसके कच्चे माल का कार्बन हाल ही में पौधों ने हवा से लिया था, या वह कचरे से वैसे भी निकल जाता, इसलिए शुद्ध उत्सर्जन लगभग 80 प्रतिशत तक घट सकता है। "
  "भारत ने अंतरराष्ट्रीय उड़ानों के लिए 2027 में 1 प्रतिशत और 2028 में 2 प्रतिशत मिश्रण के सांकेतिक लक्ष्य घोषित किए हैं।",
  f"{MOPNG} -- National Biofuel Coordination Committee; International Civil Aviation Organization -- CORSIA eligible fuels.",
  "en-sustainable-aviation-fuel", craft="inference")

M(EN, "medium", "In India's fuel programmes, 'M15' refers to",
  "भारत के ईंधन कार्यक्रमों में 'M15' का अर्थ है",
  ["petrol blended with 15 per cent methanol", "petrol blended with 15 per cent ethanol",
   "diesel blended with 15 per cent biodiesel", "compressed natural gas mixed with 15 per cent hydrogen"],
  ["15 प्रतिशत मेथनॉल मिला पेट्रोल", "15 प्रतिशत एथेनॉल मिला पेट्रोल",
   "15 प्रतिशत बायोडीज़ल मिला डीज़ल", "15 प्रतिशत हाइड्रोजन मिली संपीड़ित प्राकृतिक गैस"],
  0,
  "The 'M' stands for methanol: M15 petrol was trialled by Indian Oil, with a pilot launched in Assam in 2023, under NITI Aayog's 'methanol economy' programme. Methanol can be made from high-ash coal, natural gas, biomass or captured carbon dioxide, and it can also be turned into dimethyl ether (DME) for blending with LPG. "
  "Ethanol blends are labelled E, biodiesel blends B, and hydrogen-enriched CNG is called H-CNG.",
  "'M' का अर्थ मेथनॉल है: इंडियन ऑयल ने नीति आयोग के 'मेथनॉल अर्थव्यवस्था' कार्यक्रम के तहत M15 पेट्रोल का परीक्षण किया, जिसकी एक पायलट परियोजना 2023 में असम में शुरू हुई। मेथनॉल उच्च-राख वाले कोयले, प्राकृतिक गैस, बायोमास या पकड़ी गई कार्बन डाइऑक्साइड से बनाया जा सकता है, और इसे LPG में मिलाने के लिए डाइमिथाइल ईथर (DME) में भी बदला जा सकता है। "
  "एथेनॉल मिश्रणों पर E, बायोडीज़ल मिश्रणों पर B लिखा जाता है, और हाइड्रोजन मिली CNG को H-CNG कहते हैं।",
  f"NITI Aayog -- Methanol Economy programme; {MOPNG}.",
  "en-m15-methanol-blend", craft="recall")

# ================================================================ PHYSICS (1)
M(PH, "easy", "On a hot summer day, a stretch of road far ahead often appears to be covered with water. This is mainly due to",
  "गर्मी के दिन में आगे दूर सड़क का एक हिस्सा प्रायः पानी से ढका दिखाई देता है। इसका मुख्य कारण है",
  ["the bending of light through air layers of different temperatures",
   "the reflection of the sky from a thin film of oil left on the road by vehicles",
   "the scattering of blue sunlight by dust particles lying close to the ground",
   "water vapour that condenses into a thin sheet of water just above the road"],
  ["अलग-अलग तापमान वाली वायु परतों से गुज़रते प्रकाश का मुड़ना",
   "वाहनों द्वारा सड़क पर छोड़ी गई तेल की पतली परत से आकाश का परावर्तन",
   "ज़मीन के पास पड़े धूल-कणों द्वारा नीले सूर्य-प्रकाश का प्रकीर्णन",
   "जलवाष्प, जो सड़क के ठीक ऊपर पानी की पतली परत में संघनित हो जाती है"],
  0,
  "This is a mirage. The air just above hot tarmac is much hotter -- and so less dense and less refracting -- than the air above it; light from the sky heading down toward the road bends gradually upward and, at a grazing angle, is turned back toward the eye, much as in total internal reflection. "
  "The brain reads this image of the sky on the ground as a pool of water. The same bending in reverse, over cold seas, can make ships appear to float above the horizon.",
  "यह मरीचिका (mirage) है। गर्म डामर के ठीक ऊपर की वायु अपने ऊपर की वायु से कहीं अधिक गर्म, और इसलिए कम घनी तथा कम अपवर्तक, होती है; आकाश से सड़क की ओर आता प्रकाश धीरे-धीरे ऊपर की ओर मुड़ता है और बहुत तिरछे कोण पर आँख की ओर लौट आता है, लगभग पूर्ण आंतरिक परावर्तन की तरह। "
  "मस्तिष्क ज़मीन पर दिखी आकाश की इस छवि को पानी का तालाब समझ लेता है। ठंडे समुद्रों के ऊपर यही मुड़ना उल्टी दिशा में होता है, जिससे जहाज़ क्षितिज के ऊपर तैरते दिख सकते हैं।",
  f"{NC10} -- The Human Eye and the Colourful World.",
  "ph-mirage-refraction-easy", craft="inference")

# ================================================================ BIOLOGY (1)
S(BI, "medium", "Consider the following statements about public health in India:",
  "भारत में जन स्वास्थ्य के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The World Health Organization has validated India as having eliminated trachoma as a public health problem.",
   "India has been declared free of yaws.",
   "Maternal and neonatal tetanus has been eliminated in India."],
  ["विश्व स्वास्थ्य संगठन ने पुष्टि की है कि भारत ने ट्रेकोमा को जन स्वास्थ्य समस्या के रूप में समाप्त कर दिया है।",
   "भारत को यॉज़ (yaws) से मुक्त घोषित किया जा चुका है।",
   "भारत में मातृ और नवजात टिटनेस का उन्मूलन हो चुका है।"],
  C3, 2,
  "All three are correct. WHO validated India's elimination of trachoma -- an infectious eye disease that can blind -- as a public health problem in 2024, after decades of surgery, antibiotics, facial cleanliness and better sanitation. "
  "India was the first country to be declared free of yaws, a bacterial skin disease, in 2016, and maternal and neonatal tetanus was validated as eliminated in 2015 through immunising pregnant women and promoting clean deliveries. "
  "By contrast, lymphatic filariasis and kala-azar are still being pursued toward formal elimination.",
  "तीनों कथन सही हैं। WHO ने 2024 में पुष्टि की कि भारत ने ट्रेकोमा, यानी अंधा कर सकने वाले आँख के संक्रामक रोग, को जन स्वास्थ्य समस्या के रूप में समाप्त कर दिया है; इसके पीछे दशकों की सर्जरी, एंटीबायोटिक, चेहरे की सफ़ाई और बेहतर स्वच्छता थी। "
  "भारत 2016 में यॉज़, एक जीवाणुजनित त्वचा रोग, से मुक्त घोषित होने वाला पहला देश बना, और गर्भवती महिलाओं के टीकाकरण तथा सुरक्षित प्रसव को बढ़ावा देकर 2015 में मातृ और नवजात टिटनेस का उन्मूलन प्रमाणित हुआ। "
  "इसके विपरीत, लसीका फ़ाइलेरिया और कालाज़ार के औपचारिक उन्मूलन की दिशा में अभी काम चल रहा है।",
  "World Health Organization -- South-East Asia Region elimination validations; Ministry of Health and Family Welfare.",
  "bi-india-eliminated-trachoma-yaws-mnt", craft="recall")

# ================================================================ SPACE (1)
S(ST, "hard", "Consider the following statements about XPoSat, launched by ISRO in January 2024:",
  "जनवरी 2024 में ISRO द्वारा प्रक्षेपित XPoSat के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is India's first satellite dedicated to measuring the polarisation of X-rays from cosmic sources.",
   "It was India's first space-based astronomy observatory of any kind.",
   "It operates from a halo orbit around the Sun-Earth L1 point."],
  ["यह ब्रह्मांडीय स्रोतों से आने वाली एक्स-किरणों के ध्रुवण (polarisation) को मापने के लिए समर्पित भारत का पहला उपग्रह है।",
   "यह किसी भी प्रकार की भारत की पहली अंतरिक्ष-आधारित खगोलीय वेधशाला थी।",
   "यह सूर्य-पृथ्वी L1 बिंदु के चारों ओर प्रभामंडल (halo) कक्षा से काम करता है।"],
  C3, 0,
  "Only statement 1 is correct. XPoSat carries two instruments -- POLIX, which measures X-ray polarisation, and XSPECT, which studies X-ray spectra and their changes over time -- to probe bright sources such as black holes, neutron stars and pulsars. "
  "Statement 2 is wrong: AstroSat, launched in 2015, was India's first multi-wavelength space observatory. "
  "Statement 3 is wrong: XPoSat circles the Earth in a low orbit about 650 km up, placed there by PSLV-C58; NASA's IXPE (2021) is the only earlier mission of its kind.",
  "केवल कथन 1 सही है। XPoSat में दो उपकरण हैं: एक्स-किरण ध्रुवण मापने वाला POLIX, और एक्स-किरण स्पेक्ट्रम तथा समय के साथ उसके बदलाव का अध्ययन करने वाला XSPECT; इनसे ब्लैक होल, न्यूट्रॉन तारे और पल्सर जैसे चमकीले स्रोतों की जाँच होती है। "
  "कथन 2 गलत है: 2015 में प्रक्षेपित एस्ट्रोसैट भारत की पहली बहु-तरंगदैर्ध्य अंतरिक्ष वेधशाला थी। "
  "कथन 3 गलत है: XPoSat पृथ्वी के चारों ओर लगभग 650 किमी ऊँची निचली कक्षा में घूमता है, जहाँ उसे PSLV-C58 ने स्थापित किया; नासा का IXPE (2021) ही इस प्रकार का पहले का एकमात्र मिशन है।",
  f"{ISRO} -- XPoSat mission (PSLV-C58).",
  "st-xposat-polarimetry", craft="precision")

# ================================================================ CHEMISTRY (2)
A(CH, "medium",
  "Dry ice leaves no liquid behind as it warms at normal atmospheric pressure.",
  "सामान्य वायुमंडलीय दाब पर गर्म होने पर शुष्क बर्फ़ (dry ice) पीछे कोई द्रव नहीं छोड़ती।",
  "At normal atmospheric pressure, solid carbon dioxide changes directly into gas without first melting.",
  "सामान्य वायुमंडलीय दाब पर ठोस कार्बन डाइऑक्साइड पहले पिघले बिना सीधे गैस में बदल जाती है।",
  0,
  "Both statements are correct and Statement-II explains Statement-I. Carbon dioxide cannot exist as a liquid below about 5 atmospheres, so at ordinary pressure the solid sublimes, at about -78.5 °C. "
  "That is why dry ice is used to ship frozen food and vaccines without a messy melt, and to make stage fog. It must be handled in ventilated spaces, because the gas it gives off can displace oxygen.",
  "दोनों कथन सही हैं और कथन-II कथन-I की व्याख्या करता है। लगभग 5 वायुमंडल से कम दाब पर कार्बन डाइऑक्साइड द्रव रूप में नहीं रह सकती, इसलिए साधारण दाब पर ठोस लगभग -78.5 °C पर ऊर्ध्वपातित (sublime) हो जाता है। "
  "इसीलिए शुष्क बर्फ़ से जमे हुए भोजन और टीकों को बिना पिघलने की गड़बड़ी के भेजा जाता है, और मंच पर कोहरा बनाया जाता है। इसे हवादार जगह में रखना चाहिए, क्योंकि इससे निकलने वाली गैस ऑक्सीजन को हटा सकती है।",
  f"{NC11C} -- States of Matter.",
  "ch-dry-ice-sublimation", craft="inference")

S(CH, "medium", "Consider the following uses of noble gases and the property said to explain each:",
  "उत्कृष्ट गैसों के निम्नलिखित उपयोगों और प्रत्येक की व्याख्या करने वाले बताए गए गुण पर विचार कीजिए:",
  ["Helium replaces nitrogen in the breathing mixtures of deep-sea divers because, unlike nitrogen, it does not cause narcosis at high pressure.",
   "Neon signs glow red-orange because neon reacts with the metal of the electrodes when a current passes through the tube.",
   "Argon is used to fill incandescent bulbs because, being inert, it does not react with the hot tungsten filament."],
  ["गहरे समुद्र में गोताखोरों के श्वसन मिश्रण में हीलियम नाइट्रोजन की जगह लेती है क्योंकि नाइट्रोजन के विपरीत यह ऊँचे दाब पर नशे जैसी स्थिति (narcosis) पैदा नहीं करती।",
   "नियॉन साइन लाल-नारंगी चमकते हैं क्योंकि नली में धारा गुज़रने पर नियॉन इलेक्ट्रोड की धातु से अभिक्रिया करती है।",
   "तापदीप्त बल्बों में आर्गन भरी जाती है क्योंकि अक्रिय होने के कारण यह गर्म टंगस्टन तंतु से अभिक्रिया नहीं करती।"],
  C3, 1,
  "Statements 1 and 3 are correct. Nitrogen breathed at high pressure dissolves in nerve tissue and acts like an anaesthetic, so deep divers breathe helium-oxygen mixtures instead; helium is far less soluble and does not cause this narcosis. "
  "Argon, the most abundant noble gas, fills bulbs because it is inert: it shields the white-hot filament from oxygen and slows its evaporation. "
  "Statement 2 gives the wrong mechanism. Nothing reacts in a neon tube: the electric discharge excites neon atoms, which give out light of particular wavelengths as they return to lower energy states, and neon's strongest lines are red-orange. That inertness is also why the gases were long thought to form no compounds at all -- until xenon fluorides were made in 1962.",
  "कथन 1 और 3 सही हैं। ऊँचे दाब पर साँस में ली गई नाइट्रोजन तंत्रिका ऊतक में घुलकर निश्चेतक जैसा प्रभाव डालती है, इसलिए गहरे गोताखोर हीलियम-ऑक्सीजन मिश्रण लेते हैं; हीलियम बहुत कम घुलती है और यह नशा पैदा नहीं करती। "
  "सबसे अधिक मात्रा वाली उत्कृष्ट गैस, आर्गन, बल्बों में इसलिए भरी जाती है क्योंकि वह अक्रिय है: वह सफ़ेद-गर्म तंतु को ऑक्सीजन से बचाती है और उसका वाष्पन धीमा करती है। "
  "कथन 2 ग़लत कारण बताता है। नियॉन नली में कोई अभिक्रिया नहीं होती: विद्युत विसर्जन नियॉन परमाणुओं को उत्तेजित करता है, जो निचली ऊर्जा अवस्था में लौटते समय विशेष तरंगदैर्ध्य का प्रकाश छोड़ते हैं, और नियॉन की सबसे प्रबल रेखाएँ लाल-नारंगी हैं। इसी अक्रियता के कारण इन गैसों को लंबे समय तक यौगिक बनाने में पूरी तरह असमर्थ माना गया, जब तक 1962 में ज़ीनॉन फ़्लोराइड नहीं बनाए गए।",
  "NCERT Class XII, Chemistry -- The p-Block Elements (Group 18).",
  "ch-noble-gases-helium-xenon-neon", craft="linkage")

# ================================================================ IT (2)
S(IT, "medium", "Consider the following statements about online fraud and account security:",
  "ऑनलाइन धोखाधड़ी और खाते की सुरक्षा के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["In a SIM-swap fraud, the criminal gets a duplicate SIM issued for the victim's number so as to receive the victim's one-time passwords.",
   "Two-factor authentication offers no protection once a user's password has been stolen.",
   "Phishing requires the attacker to install malware on the victim's device first."],
  ["सिम-स्वैप धोखाधड़ी में अपराधी पीड़ित के नंबर का डुप्लिकेट सिम जारी करवा लेता है ताकि पीड़ित के वन-टाइम पासवर्ड उसे मिलें।",
   "उपयोगकर्ता का पासवर्ड चोरी हो जाने के बाद टू-फ़ैक्टर ऑथेंटिकेशन कोई सुरक्षा नहीं देता।",
   "फ़िशिंग के लिए हमलावर को पहले पीड़ित के डिवाइस पर मैलवेयर इंस्टॉल करना पड़ता है।"],
  C3, 0,
  "Only statement 1 is correct. Once the fraudster controls the number, OTPs and bank alerts go to the new SIM, which is why telecom rules now block SMS on a replaced SIM for 24 hours. "
  "Statement 2 is wrong: the whole point of two-factor authentication is that a stolen password alone is not enough -- the attacker also needs the second factor, such as a code on the user's phone or a fingerprint. "
  "Statement 3 is wrong: phishing works by deceiving the user -- a fake message or website that imitates a bank or a courier -- into handing over passwords or OTPs; no malware is needed, though some phishing links do deliver it.",
  "केवल कथन 1 सही है। नंबर पर क़ब्ज़ा होते ही OTP और बैंक अलर्ट नए सिम पर जाने लगते हैं; इसीलिए दूरसंचार नियम अब बदले गए सिम पर 24 घंटे तक SMS रोकते हैं। "
  "कथन 2 गलत है: टू-फ़ैक्टर ऑथेंटिकेशन का पूरा उद्देश्य यही है कि केवल चोरी हुआ पासवर्ड काफ़ी न हो; हमलावर को दूसरा प्रमाण भी चाहिए, जैसे उपयोगकर्ता के फ़ोन पर आया कोड या फ़िंगरप्रिंट। "
  "कथन 3 गलत है: फ़िशिंग उपयोगकर्ता को धोखा देकर काम करती है, जैसे बैंक या कूरियर की नक़ल करता नक़ली संदेश या वेबसाइट, ताकि वह पासवर्ड या OTP सौंप दे; इसके लिए मैलवेयर की ज़रूरत नहीं होती, यद्यपि कुछ फ़िशिंग लिंक मैलवेयर भी पहुँचाते हैं।",
  "Department of Telecommunications -- SIM replacement rules; Indian Cyber Crime Coordination Centre (I4C) advisories.",
  "it-sim-swap-2fa-phishing", craft="application")

M(IT, "medium", "Which one of the following is true of a web browser's private or 'incognito' mode?",
  "वेब ब्राउज़र के प्राइवेट या 'इनकॉग्निटो' मोड के बारे में निम्नलिखित में से कौन-सा सही है?",
  ["It stops the browser keeping the session's history on the device, but websites can still see the activity",
   "It encrypts all traffic so that neither the internet provider nor the websites can see what the user does",
   "It hides the user's IP address from every website, in the same way as the Tor network",
   "It prevents websites from placing any cookies on the device during the session"],
  ["यह ब्राउज़र को उस सत्र का इतिहास डिवाइस पर रखने से रोकता है, पर वेबसाइटें गतिविधि देख सकती हैं",
   "यह सारा ट्रैफ़िक एन्क्रिप्ट करता है ताकि न इंटरनेट प्रदाता न वेबसाइटें देख सकें कि उपयोगकर्ता क्या करता है",
   "यह टॉर नेटवर्क की तरह हर वेबसाइट से उपयोगकर्ता का IP पता छिपा देता है",
   "यह सत्र के दौरान वेबसाइटों को डिवाइस पर कोई भी कुकी रखने से रोकता है"],
  0,
  "Private browsing only keeps the session off the device: cookies are still set during the session, but when the window is closed its history, cookies and form entries are deleted. Websites, the employer's or school's network and the internet service provider can still see the traffic, and the user's IP address is visible as usual. "
  "A VPN encrypts traffic up to the VPN server and hides the IP address from websites (the VPN provider can then see it), while the Tor network relays traffic through several volunteer servers to hide where it came from.",
  "प्राइवेट ब्राउज़िंग केवल सत्र को डिवाइस से दूर रखती है: सत्र के दौरान कुकीज़ बनती हैं, पर विंडो बंद होते ही उसका इतिहास, कुकीज़ और फ़ॉर्म की प्रविष्टियाँ मिटा दी जाती हैं। वेबसाइटें, दफ़्तर या स्कूल का नेटवर्क और इंटरनेट सेवा प्रदाता फिर भी ट्रैफ़िक देख सकते हैं, और उपयोगकर्ता का IP पता सामान्य रूप से दिखता है। "
  "VPN, VPN सर्वर तक ट्रैफ़िक एन्क्रिप्ट करता है और वेबसाइटों से IP पता छिपाता है (तब VPN प्रदाता उसे देख सकता है), जबकि टॉर नेटवर्क ट्रैफ़िक को कई स्वयंसेवी सर्वरों से घुमाकर उसका स्रोत छिपाता है।",
  "Indian Computer Emergency Response Team (CERT-In) -- online safety advisories; Ministry of Electronics and Information Technology.",
  "it-incognito-private-browsing", craft="inference")

# ================================================================ ASTRONOMY (1)
S(AS, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["At the equinoxes, day and night are nearly equal in length all over the Earth.",
   "A 'supermoon' is a full moon that occurs when the Moon is near perigee, its closest point to the Earth."],
  ["विषुवों (equinoxes) पर पूरी पृथ्वी पर दिन और रात की अवधि लगभग बराबर होती है।",
   "'सुपरमून' वह पूर्णिमा है जो तब होती है जब चंद्रमा उपभू (perigee), यानी पृथ्वी से अपने निकटतम बिंदु, के पास होता है।"],
  T2, 2,
  "Both statements are correct. Around 20-21 March and 22-23 September the Sun is overhead at the Equator, so the circle of illumination passes through both poles and every place gets about 12 hours of daylight -- a little more, because the atmosphere bends sunlight over the horizon. "
  "A supermoon can look up to about 14 per cent larger and 30 per cent brighter than a full moon near apogee.",
  "दोनों कथन सही हैं। लगभग 20-21 मार्च और 22-23 सितंबर को सूर्य विषुवत रेखा पर लंबवत होता है, इसलिए प्रकाश-वृत्त दोनों ध्रुवों से होकर गुज़रता है और हर स्थान पर लगभग 12 घंटे का दिन होता है; वायुमंडल द्वारा सूर्य-प्रकाश को क्षितिज के पार मोड़ने से दिन थोड़ा अधिक होता है। "
  "सुपरमून अपभू (apogee) के पास की पूर्णिमा की तुलना में लगभग 14 प्रतिशत बड़ा और 30 प्रतिशत अधिक चमकीला दिख सकता है।",
  "NCERT Class XI, Fundamentals of Physical Geography -- The Earth in the Solar System; NASA -- Moon facts.",
  "as-equinox-supermoon-easy", craft="recall")

# ================================================================ DEFENCE (1)
S(DF, "hard", "Consider the following statements about indigenous defence systems:",
  "स्वदेशी रक्षा प्रणालियों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Prachand is a light combat helicopter designed to operate at very high altitudes, such as the Siachen region.",
   "Pralay is a surface-to-surface quasi-ballistic missile.",
   "Agni-Prime has been test-fired from a rail-based mobile launcher."],
  ["प्रचंड एक हल्का लड़ाकू हेलिकॉप्टर है जो सियाचिन जैसे बहुत ऊँचाई वाले क्षेत्रों में काम करने के लिए बना है।",
   "प्रलय सतह से सतह पर मार करने वाली एक अर्ध-बैलिस्टिक (quasi-ballistic) मिसाइल है।",
   "अग्नि-प्राइम का परीक्षण रेल-आधारित चलित प्रक्षेपक से किया जा चुका है।"],
  C3, 2,
  "All three are correct. HAL's Prachand, inducted in 2022, is built to take off and land at about 5,000 m with a useful load of weapons and fuel, for missions in the high Himalaya. "
  "DRDO's Pralay is a quasi-ballistic missile with a range of roughly 150-500 km that can change course in flight to defeat interceptors; it is meant for conventional strikes. "
  "Agni-Prime, a new-generation canister-launched missile of the Agni family, was fired in 2025 from a specially designed rail-based launcher, showing that it can move across the rail network and launch at short notice.",
  "तीनों कथन सही हैं। 2022 में शामिल किया गया HAL का प्रचंड ऊँचे हिमालय के अभियानों के लिए लगभग 5,000 मीटर पर हथियारों और ईंधन के उपयोगी भार के साथ उड़ान भरने और उतरने के लिए बना है। "
  "DRDO की प्रलय लगभग 150-500 किमी मारक दूरी वाली अर्ध-बैलिस्टिक मिसाइल है जो इंटरसेप्टर को चकमा देने के लिए उड़ान में दिशा बदल सकती है; यह पारंपरिक प्रहार के लिए है। "
  "अग्नि परिवार की नई पीढ़ी की कनस्तर-प्रक्षेपित मिसाइल अग्नि-प्राइम को 2025 में विशेष रूप से बने रेल-आधारित प्रक्षेपक से दागा गया, जिससे पता चला कि यह रेल नेटवर्क पर घूमकर कम समय में प्रक्षेपित हो सकती है।",
  f"{DRDO}; Hindustan Aeronautics Limited -- Light Combat Helicopter Prachand; Ministry of Defence.",
  "df-prachand-pralay-agni-prime", craft="recall")

if __name__ == "__main__":
    write_updates("gs_l2_t21_st_v2.sql")
