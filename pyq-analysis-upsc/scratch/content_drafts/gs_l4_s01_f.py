# -*- coding: utf-8 -*-
"""Level 4 · Simulator 1 (GS Paper I full mock, Layout A: the 2023/24 shape) -- part F: Science & Technology (10)
(upsc_l4_gs_cell_targets.mjs 1).
From a whole-bank sweep of technologies and diseases no row tests: the Devasthal telescopes and the liquid-mirror
telescope; Kyasanur Forest Disease; superhydrophobic surfaces, metamaterials and self-healing polymers; the Zorawar
light tank, QRSAM and Agni-5; wave energy; TOPCon cells, Bharat Small Reactors and waste-heat recovery; LiDAR and
SLAM; Open RAN, massive MIMO, chiplets and haptics; tokamaks, SST-1 and ITER; orbital decay of space debris. MCQ
keys are pinned (pos); answer letters close the paper's balance."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Science & Technology"
d.REQUIRE_CRAFT = True

# ---------------------------------------------------------------- Astronomy & Earth Science (statement, medium)
S("Astronomy & Earth Science", "medium", "With reference to the telescopes at Devasthal near Nainital, consider the following statements:",
  "नैनीताल के पास देवस्थल की दूरबीनों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["The 3.6-metre Devasthal Optical Telescope is among the largest optical telescopes in India.",
   "The International Liquid Mirror Telescope there uses a spinning pool of mercury as its mirror and can be pointed at any part of the sky.",
   "Sites for optical telescopes are best chosen near the coast, where the air is moist."],
  ["3.6 मीटर का देवस्थल प्रकाशीय दूरबीन भारत की सबसे बड़ी प्रकाशीय दूरबीनों में है।",
   "वहाँ की अंतरराष्ट्रीय द्रव दर्पण दूरबीन दर्पण के रूप में पारे के घूमते कुंड का उपयोग करती है और आकाश के किसी भी भाग की ओर मोड़ी जा सकती है।",
   "प्रकाशीय दूरबीनों के लिए स्थल तट के पास चुने जाते हैं, जहाँ वायु नम होती है।"],
  C3, 0,
  "Only statement 1 is correct. The Aryabhatta Research Institute of Observational Sciences (ARIES) runs the 3.6-metre Devasthal Optical Telescope, commissioned in 2016 with Belgian collaboration, at about 2,450 metres in the Kumaon hills. "
  "Statement 2 is wrong in its second half: in a liquid-mirror telescope, a pool of mercury spun at a steady rate takes the shape of a perfect paraboloid, giving a large mirror cheaply, but the liquid must stay level, so the telescope can only stare straight up and survey the strip of sky that the Earth's rotation carries overhead each night; the 4-metre ILMT at Devasthal, which began observing in 2022 with Belgium and Canada, is used to catch transient objects such as supernovae and space debris. Statement 3 is wrong: optical observatories are sited on high, dry, dark sites with steady air, above much of the water vapour and turbulence of the atmosphere -- hence Devasthal, Hanle in Ladakh and Mauna Kea.",
  "केवल कथन 1 सही है। आर्यभट्ट प्रेक्षण विज्ञान शोध संस्थान (एरीज़) कुमाऊँ की पहाड़ियों में लगभग 2,450 मीटर पर 3.6 मीटर का देवस्थल प्रकाशीय दूरबीन चलाता है, जो 2016 में बेल्जियम के सहयोग से आरंभ हुआ। "
  "कथन 2 अपने दूसरे भाग में ग़लत है: द्रव दर्पण दूरबीन में स्थिर गति से घुमाया गया पारे का कुंड पूर्ण परवलयज का आकार ले लेता है, जिससे सस्ते में बड़ा दर्पण मिलता है, पर द्रव को समतल रहना होता है, इसलिए दूरबीन केवल सीधे ऊपर देख सकती है और आकाश की वह पट्टी सर्वेक्षित करती है जिसे पृथ्वी का घूर्णन हर रात ऊपर से ले जाता है; 2022 में बेल्जियम और कनाडा के साथ प्रेक्षण आरंभ करने वाली देवस्थल की 4 मीटर की आईएलएमटी का उपयोग सुपरनोवा और अंतरिक्ष मलबे जैसे क्षणिक पिंडों को पकड़ने में होता है। कथन 3 ग़लत है: प्रकाशीय वेधशालाएँ ऊँचे, शुष्क, अँधेरे और स्थिर वायु वाले स्थलों पर बनती हैं, जो वायुमंडल के अधिकांश जलवाष्प और विक्षोभ से ऊपर हों -- इसीलिए देवस्थल, लद्दाख का हानले और मौना किया।",
  "Aryabhatta Research Institute of Observational Sciences (Department of Science and Technology): Devasthal Optical Telescope (2016) and International Liquid Mirror Telescope (PIB, 2022).",
  "l4-s01-sci-devasthal-dot-ilmt-zenith-dry-sites", craft="inference")

# ---------------------------------------------------------------- Biology, Health & Biotechnology (MCQ, hard)
M("Biology, Health & Biotechnology", "hard",
  "Kyasanur Forest Disease, which recurs in parts of the Western Ghats, is",
  "पश्चिमी घाट के कुछ भागों में बार-बार होने वाला क्यासानूर वन रोग क्या है?",
  ["a mosquito-borne bacterial disease that mainly affects farmers working in flooded paddy fields",
   "a fungal infection spread through the droppings of fruit bats in forest caves and villages",
   "a prion disease of cattle that spreads to people who eat beef from infected animals",
   "a tick-borne viral disease whose outbreaks are often signalled by deaths among monkeys"],
  ["जलमग्न धान के खेतों में काम करने वाले किसानों को मुख्यतः प्रभावित करने वाला मच्छर-जनित जीवाणु रोग",
   "वन गुफाओं और गाँवों में फल-चमगादड़ों की बीट से फैलने वाला कवक संक्रमण",
   "मवेशियों का प्रायन रोग जो संक्रमित पशुओं का गोमांस खाने वालों में फैलता है",
   "किलनी-जनित विषाणु रोग जिसके प्रकोप का संकेत प्रायः बंदरों की मौतों से मिलता है"],
  3,
  "Kyasanur Forest Disease, popularly called monkey fever, is caused by a flavivirus carried by forest ticks; it was first identified in 1957 in the Kyasanur forest of Shivamogga district in Karnataka, after a wave of deaths among langurs and macaques, which remain the first warning of an outbreak. People are infected when bitten by infected ticks while collecting firewood, cashew or other forest produce or grazing cattle in the dry season; the disease causes high fever and can lead to bleeding and neurological illness. "
  "It has spread from Karnataka to Kerala, Goa and Maharashtra as forests have been cleared and land use has changed -- a textbook example of a zoonosis emerging where people press into wildlife habitat. A vaccine exists but gives limited, short-lived protection, so prevention relies on tick repellents and surveillance of monkey deaths.",
  "क्यासानूर वन रोग, जिसे आम बोलचाल में मंकी फ़ीवर कहते हैं, वन की किलनियों द्वारा ले जाए जाने वाले एक फ़्लेविवायरस से होता है; इसकी पहचान पहली बार 1957 में कर्नाटक के शिवमोग्गा ज़िले के क्यासानूर वन में लंगूरों और मकाकों की मौतों की लहर के बाद हुई, जो आज भी प्रकोप की पहली चेतावनी हैं। शुष्क ऋतु में जलाऊ लकड़ी, काजू या अन्य वनोपज इकट्ठा करते या मवेशी चराते समय संक्रमित किलनियों के काटने से लोग संक्रमित होते हैं; रोग से तेज़ बुख़ार होता है और रक्तस्राव तथा तंत्रिका संबंधी बीमारी हो सकती है। "
  "वनों के कटने और भूमि-उपयोग बदलने के साथ यह कर्नाटक से केरल, गोवा और महाराष्ट्र तक फैल गया है -- यह वन्यजीव आवास में मनुष्यों के घुसने पर उभरने वाले पशुजन्य रोग का पाठ्यपुस्तकीय उदाहरण है। टीका उपलब्ध है पर सीमित और अल्पकालिक सुरक्षा देता है, इसलिए रोकथाम किलनी-रोधी उपायों और बंदरों की मौतों की निगरानी पर निर्भर है।",
  "Indian Council of Medical Research (National Institute of Virology), Kyasanur Forest Disease; National Centre for Disease Control, KFD guidelines.",
  "l4-s01-sci-kyasanur-forest-disease-tick-monkey-deaths", pos=3, craft="linkage")

# ---------------------------------------------------------------- Chemistry & Materials (statement, medium)
S("Chemistry & Materials", "medium", "With reference to advanced materials, consider the following statements:",
  "उन्नत पदार्थों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Superhydrophobic surfaces, like a lotus leaf, make water form beads that roll off and carry dirt away.",
   "Metamaterials get unusual properties, such as bending light in unnatural ways, from their engineered structure rather than from their chemical composition.",
   "Some self-healing polymers repair cracks by releasing a healing agent stored in tiny capsules within them."],
  ["कमल के पत्ते जैसी अतिजलविरागी सतहें पानी को बूँदों में बदल देती हैं जो लुढ़ककर गंदगी साथ ले जाती हैं।",
   "मेटामटेरियल प्रकाश को अप्राकृतिक ढंग से मोड़ने जैसे असामान्य गुण अपनी रासायनिक संरचना के बजाय अपनी अभियांत्रिक बनावट से पाते हैं।",
   "कुछ स्व-उपचारी बहुलक अपने भीतर छोटे कैप्सूलों में रखा उपचारक पदार्थ छोड़कर दरारें भरते हैं।"],
  C3, 2,
  "All three statements are correct. A lotus leaf repels water because microscopic bumps coated with wax trap air beneath a drop, so the drop touches very little solid, stays nearly spherical and rolls off, picking up dust -- the 'lotus effect' copied in self-cleaning glass and textiles. Metamaterials are assemblies of structures smaller than the wavelength of the waves they act on; by their geometry they can give a negative refractive index, focus beyond the usual limits or steer radar and sound, with uses in antennas and stealth. "
  "Self-healing polymers mimic the way skin heals: in one design, a crack ruptures embedded microcapsules that release a monomer, which polymerises on contact with a catalyst and seals the crack, extending the life of coatings and composites. In each case the property comes from structure designed at the micro or nano scale, a theme running through modern materials science.",
  "तीनों कथन सही हैं। कमल का पत्ता पानी को इसलिए दूर रखता है कि मोम से लिपटे सूक्ष्म उभार बूँद के नीचे वायु फँसा लेते हैं, जिससे बूँद बहुत कम ठोस को छूती है, लगभग गोल रहती है और धूल उठाते हुए लुढ़क जाती है -- यही ‘लोटस प्रभाव’ स्व-सफ़ाई वाले काँच और वस्त्रों में अपनाया गया है। मेटामटेरियल उन तरंगों की तरंगदैर्ध्य से छोटी संरचनाओं के समूह हैं जिन पर वे कार्य करते हैं; अपनी ज्यामिति से वे ऋणात्मक अपवर्तनांक दे सकते हैं, सामान्य सीमाओं से आगे फ़ोकस कर सकते हैं या रडार और ध्वनि को मोड़ सकते हैं, जिनका उपयोग एंटेना और रडार-अदृश्यता में है। "
  "स्व-उपचारी बहुलक त्वचा के भरने की नक़ल करते हैं: एक रचना में दरार भीतर रखे सूक्ष्म कैप्सूलों को तोड़ देती है जो एक एकलक छोड़ते हैं, जो उत्प्रेरक के संपर्क में आकर बहुलकित होता है और दरार भर देता है, जिससे लेपों और मिश्रित पदार्थों की आयु बढ़ती है। हर उदाहरण में गुण सूक्ष्म या नैनो स्तर पर बनाई गई संरचना से आता है, जो आधुनिक पदार्थ विज्ञान का एक सूत्र है।",
  "Department of Science and Technology, Nano Mission; NCERT, Chemistry (Class XII), polymers.",
  "l4-s01-sci-superhydrophobic-metamaterials-self-healing", craft="inference")

# ---------------------------------------------------------------- Defence, Aerospace & Security Technology (statement, medium)
S("Defence, Aerospace & Security Technology", "medium", "With reference to India's defence systems, consider the following statements:",
  "भारत की रक्षा प्रणालियों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Zorawar is a light tank developed for operations in high-altitude areas such as eastern Ladakh.",
   "QRSAM is a ballistic missile with a range of more than 5,000 km.",
   "Agni-5 is a cruise missile that flies at low altitude throughout its flight."],
  ["ज़ोरावर पूर्वी लद्दाख जैसे ऊँचाई वाले क्षेत्रों में अभियानों के लिए विकसित हल्का टैंक है।",
   "क्यूआरसैम 5,000 किमी से अधिक मारक दूरी वाली बैलिस्टिक मिसाइल है।",
   "अग्नि-5 एक क्रूज़ मिसाइल है जो अपनी पूरी उड़ान में कम ऊँचाई पर उड़ती है।"],
  C3, 0,
  "Only statement 1 is correct. The stand-off in eastern Ladakh from 2020 showed the need for a tank light enough to be moved by air and to manoeuvre in thin air on high plateaus, where heavy main battle tanks struggle; Zorawar, of about 25 tonnes, was developed by DRDO with Larsen & Toubro and began trials in 2024. "
  "Statement 2 is wrong: QRSAM is a Quick Reaction Surface-to-Air Missile, a mobile air-defence system with a range of about 30 km, meant to protect moving army columns from aircraft and drones. Statement 3 is wrong: Agni-5 is a ballistic missile with a range of over 5,000 km, which climbs out of the atmosphere and descends on a ballistic path; it has been tested with multiple independently targetable re-entry vehicles. Cruise missiles such as BrahMos and Nirbhay, by contrast, fly within the atmosphere, powered throughout, often low to evade radar.",
  "केवल कथन 1 सही है। 2020 से पूर्वी लद्दाख के गतिरोध ने ऐसे टैंक की आवश्यकता दिखाई जो हवाई मार्ग से ले जाया जा सके और ऊँचे पठारों की विरल वायु में चल सके, जहाँ भारी मुख्य युद्धक टैंक कठिनाई में रहते हैं; लगभग 25 टन का ज़ोरावर डीआरडीओ ने लार्सन एंड टुब्रो के साथ विकसित किया और 2024 में इसके परीक्षण आरंभ हुए। "
  "कथन 2 ग़लत है: क्यूआरसैम त्वरित प्रतिक्रिया सतह-से-हवा मिसाइल है, लगभग 30 किमी मारक दूरी वाली एक चलती वायु-रक्षा प्रणाली, जो चलते सैन्य दस्तों को विमानों और ड्रोनों से बचाने के लिए है। कथन 3 ग़लत है: अग्नि-5 5,000 किमी से अधिक मारक दूरी वाली बैलिस्टिक मिसाइल है, जो वायुमंडल से बाहर चढ़ती है और बैलिस्टिक मार्ग से उतरती है; इसका कई स्वतंत्र लक्ष्य-योग्य पुनःप्रवेश वाहनों के साथ परीक्षण हुआ है। इसके विपरीत ब्रह्मोस और निर्भय जैसी क्रूज़ मिसाइलें वायुमंडल के भीतर, पूरी उड़ान में इंजन के बल पर, प्रायः रडार से बचने के लिए नीची उड़ती हैं।",
  "Ministry of Defence and DRDO (PIB): Zorawar light tank trials (2024), QRSAM flight tests, Mission Divyastra (2024).",
  "l4-s01-sci-zorawar-qrsam-agni5-ballistic", craft="precision")

# ---------------------------------------------------------------- Energy & Environmental Technology (MCQ, easy)
M("Energy & Environmental Technology", "easy",
  "Which one of the following forms of energy is obtained from the up-and-down motion of the sea surface raised by the wind?",
  "निम्नलिखित में से ऊर्जा का कौन-सा रूप पवन द्वारा उठाई गई समुद्र सतह की ऊपर-नीचे की गति से प्राप्त होता है?",
  ["Wave energy", "Tidal energy", "Ocean thermal energy", "Geothermal energy"],
  ["तरंग ऊर्जा", "ज्वारीय ऊर्जा", "महासागरीय तापीय ऊर्जा", "भूतापीय ऊर्जा"],
  0,
  "Wave energy is captured from the motion of waves, which are raised by wind blowing over the sea -- so it is ultimately a form of solar energy; devices such as oscillating water columns use the rise and fall of water to push air through a turbine, and India tested one at Vizhinjam in the 1990s. "
  "Tidal energy comes instead from the rise and fall of tides caused by the pull of the Moon and the Sun, and is most promising where the tidal range is large, as in the Gulf of Khambhat and the Sundarbans; ocean thermal energy conversion uses the temperature difference between warm surface water and cold deep water, suited to tropical seas such as those around Lakshadweep; geothermal energy comes from the Earth's internal heat, as at Puga in Ladakh.",
  "तरंग ऊर्जा तरंगों की गति से प्राप्त होती है, जो समुद्र पर बहती पवन से उठती हैं -- इसलिए यह अंततः सौर ऊर्जा का ही रूप है; दोलायमान जल-स्तंभ जैसे उपकरण पानी के उठने-गिरने से वायु को टरबाइन से होकर धकेलते हैं, और भारत ने 1990 के दशक में विझिंजम में ऐसा एक परीक्षण किया था। "
  "इसके विपरीत ज्वारीय ऊर्जा चंद्रमा और सूर्य के खिंचाव से आने वाले ज्वार के उठने-गिरने से आती है, और सबसे संभावनापूर्ण वहाँ है जहाँ ज्वारीय परास बड़ा हो, जैसे खंभात की खाड़ी और सुंदरबन; महासागरीय तापीय ऊर्जा रूपांतरण गर्म सतही जल और ठंडे गहरे जल के तापांतर का उपयोग करता है, जो लक्षद्वीप के आसपास जैसे उष्णकटिबंधीय समुद्रों के लिए उपयुक्त है; भूतापीय ऊर्जा पृथ्वी की आंतरिक ऊष्मा से आती है, जैसे लद्दाख के पूगा में।",
  "Ministry of New and Renewable Energy, ocean energy; National Institute of Ocean Technology, wave energy and OTEC; NCERT, Science (Class X), sources of energy.",
  "l4-s01-sci-wave-energy-vs-tidal-otec-geothermal", pos=0, craft="recall")

# ---------------------------------------------------------------- Energy & Environmental Technology (statement, medium)
S("Energy & Environmental Technology", "medium", "With reference to clean-energy technologies, consider the following statements:",
  "स्वच्छ-ऊर्जा प्रौद्योगिकियों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["TOPCon solar cells are made of perovskite instead of crystalline silicon.",
   "The Bharat Small Reactors being developed in India are fast breeder reactors cooled by liquid sodium.",
   "Waste-heat recovery systems in cement plants make electricity by burning additional fuel in the kiln's exhaust gases."],
  ["टॉपकॉन सौर सेल क्रिस्टलीय सिलिकॉन के बजाय पेरोव्स्काइट से बने होते हैं।",
   "भारत में विकसित किए जा रहे भारत लघु रिएक्टर द्रव सोडियम से ठंडे होने वाले फ़ास्ट ब्रीडर रिएक्टर हैं।",
   "सीमेंट संयंत्रों में अपशिष्ट-ऊष्मा पुनर्प्राप्ति प्रणालियाँ भट्ठे की निकास गैसों में अतिरिक्त ईंधन जलाकर बिजली बनाती हैं।"],
  C3, 3,
  "None of the statements is correct. Statement 1 is wrong: TOPCon (tunnel oxide passivated contact) cells are crystalline-silicon cells with an ultra-thin oxide layer and doped polysilicon at the rear contact, which cuts the loss of charge carriers and lifts efficiency; they are replacing the older PERC design and are a focus of India's solar manufacturing incentives. Perovskites are a different, newer class of materials, still being made durable. "
  "Statement 2 is wrong: the Bharat Small Reactors are 220 MWe reactors adapted from India's proven pressurised heavy water reactor design, proposed for industries that want captive low-carbon power, under the Nuclear Energy Mission announced in the 2025-26 Budget; India's sodium-cooled fast breeder is the separate 500 MWe prototype at Kalpakkam. Statement 3 is wrong: waste-heat recovery burns no extra fuel -- it passes the hot exhaust gases from the kiln's preheater and the clinker cooler through boilers to raise steam for a turbine, turning heat that would otherwise be lost into electricity; that cuts a plant's grid power use and emissions, and it counts towards the energy-saving targets of energy-intensive industries.",
  "कोई भी कथन सही नहीं है। कथन 1 ग़लत है: टॉपकॉन (टनल ऑक्साइड पैसिवेटेड कॉन्टैक्ट) सेल क्रिस्टलीय-सिलिकॉन सेल हैं, जिनके पिछले संपर्क पर अति-पतली ऑक्साइड परत और मिश्रित पॉलीसिलिकॉन होता है, जो आवेश-वाहकों की हानि घटाकर दक्षता बढ़ाता है; ये पुरानी पर्क रचना का स्थान ले रहे हैं और भारत के सौर विनिर्माण प्रोत्साहनों के केंद्र में हैं। पेरोव्स्काइट पदार्थों का एक अलग, नया वर्ग है, जिसे अभी टिकाऊ बनाया जा रहा है। "
  "कथन 2 ग़लत है: भारत लघु रिएक्टर भारत की सिद्ध दाबित भारी जल रिएक्टर रचना से रूपांतरित 220 मेगावाट (विद्युत) के रिएक्टर हैं, जो 2025-26 के बजट में घोषित नाभिकीय ऊर्जा मिशन के अंतर्गत निजी कम-कार्बन बिजली चाहने वाले उद्योगों के लिए प्रस्तावित हैं; भारत का सोडियम-शीतित फ़ास्ट ब्रीडर कलपक्कम का अलग 500 मेगावाट का प्रोटोटाइप है। कथन 3 ग़लत है: अपशिष्ट-ऊष्मा पुनर्प्राप्ति कोई अतिरिक्त ईंधन नहीं जलाती -- यह भट्ठे के प्रीहीटर और क्लिंकर कूलर की गर्म निकास गैसों को बॉयलरों से गुज़ारकर टरबाइन के लिए भाप बनाती है, और अन्यथा व्यर्थ जाने वाली ऊष्मा को बिजली में बदलती है; इससे संयंत्र की ग्रिड बिजली की खपत और उत्सर्जन घटते हैं, और यह ऊर्जा-गहन उद्योगों के ऊर्जा-बचत लक्ष्यों में गिनी जाती है।",
  "Ministry of New and Renewable Energy, PLI scheme for high-efficiency solar PV modules; Union Budget 2025-26, Nuclear Energy Mission; Department of Atomic Energy and NPCIL, Bharat Small Reactors; Bureau of Energy Efficiency, Perform, Achieve and Trade scheme (cement sector).",
  "l4-s01-sci-topcon-bharat-small-reactor-waste-heat-recovery", craft="precision")

# ---------------------------------------------------------------- IT, Communication & Emerging Technologies (statement, easy)
S("IT, Communication & Emerging Technologies", "easy", "With reference to technologies used in self-driving vehicles, consider the following statements:",
  "स्वचालित वाहनों में प्रयुक्त प्रौद्योगिकियों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["LiDAR measures distances by timing laser pulses reflected from surrounding objects.",
   "SLAM techniques work only when a detailed map of the area has been loaded in advance.",
   "Satellite positioning alone is accurate enough for a car to keep to its lane on any road."],
  ["लाइडार आसपास की वस्तुओं से परावर्तित लेज़र स्पंदों का समय मापकर दूरियाँ मापता है।",
   "स्लैम तकनीकें तभी काम करती हैं जब क्षेत्र का विस्तृत मानचित्र पहले से लोड हो।",
   "उपग्रह स्थिति-निर्धारण अकेले किसी भी सड़क पर कार को अपनी लेन में रखने के लिए पर्याप्त सटीक है।"],
  C3, 0,
  "Only statement 1 is correct. LiDAR (light detection and ranging) sends out laser pulses and times their echoes to build a three-dimensional 'point cloud' of the surroundings; it is also used to map forests, terrain and archaeological sites from the air. "
  "Statement 2 is wrong: SLAM -- simultaneous localisation and mapping -- is precisely the technique by which a robot or vehicle builds a map of an unknown place while working out its own position within it, which is why it is used by robot vacuum cleaners, drones and planetary rovers. Statement 3 is wrong: ordinary satellite positioning is accurate only to a few metres and fails in tunnels and between tall buildings, so self-driving systems fuse it with cameras, radar, LiDAR, inertial sensors and detailed maps, and correction systems such as GAGAN and NavIC improve accuracy.",
  "केवल कथन 1 सही है। लाइडार (प्रकाश संसूचन और परास-मापन) लेज़र स्पंद भेजकर उनकी प्रतिध्वनि का समय मापता है और आसपास का त्रि-आयामी ‘बिंदु-मेघ’ बनाता है; इसका उपयोग हवा से वनों, भू-भाग और पुरातात्त्विक स्थलों का मानचित्रण करने में भी होता है। "
  "कथन 2 ग़लत है: स्लैम -- एक साथ स्थानीकरण और मानचित्रण -- ठीक वह तकनीक है जिससे कोई रोबोट या वाहन किसी अनजान स्थान का मानचित्र बनाते हुए उसमें अपनी स्थिति निकालता है, इसीलिए रोबोट वैक्यूम क्लीनर, ड्रोन और ग्रहीय रोवर इसका उपयोग करते हैं। कथन 3 ग़लत है: सामान्य उपग्रह स्थिति-निर्धारण केवल कुछ मीटर तक सटीक होता है और सुरंगों तथा ऊँची इमारतों के बीच विफल हो जाता है, इसलिए स्वचालित प्रणालियाँ इसे कैमरों, रडार, लाइडार, जड़त्वीय संवेदकों और विस्तृत मानचित्रों से जोड़ती हैं, और गगन तथा नाविक जैसी सुधार प्रणालियाँ सटीकता बढ़ाती हैं।",
  "Department of Science and Technology, National Mission on Interdisciplinary Cyber-Physical Systems; Survey of India, LiDAR mapping.",
  "l4-s01-sci-lidar-slam-gnss-autonomous", craft="application")

# ---------------------------------------------------------------- IT, Communication & Emerging Technologies (statement, medium)
S("IT, Communication & Emerging Technologies", "medium", "Consider the following statements about communication and computing technologies:",
  "संचार और संगणन प्रौद्योगिकियों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Open RAN separates the hardware and software of a mobile radio network so that operators can combine equipment from different vendors.",
   "Massive MIMO uses many antennas at a base station to serve several users at once on the same frequency.",
   "Chiplets allow a large processor to be built from several smaller dies packaged together.",
   "Haptic technology conveys the sense of touch through vibrations or forces, as in remote surgery."],
  ["ओपन रैन मोबाइल रेडियो नेटवर्क के हार्डवेयर और सॉफ़्टवेयर को अलग करता है ताकि ऑपरेटर विभिन्न विक्रेताओं के उपकरण जोड़ सकें।",
   "मैसिव माइमो एक बेस स्टेशन पर अनेक एंटेना से एक ही आवृत्ति पर एक साथ कई उपयोगकर्ताओं को सेवा देता है।",
   "चिपलेट एक बड़े प्रोसेसर को एक साथ पैकेज की गई कई छोटी डाई से बनाने देते हैं।",
   "हैप्टिक प्रौद्योगिकी कंपन या बलों द्वारा स्पर्श का बोध कराती है, जैसे दूरस्थ शल्य चिकित्सा में।"],
  C4, 3,
  "All four statements are correct. Open RAN breaks the radio access network into interoperable parts with open interfaces, so that an operator need not buy the whole network from one vendor; India sees it as a route for domestic telecom makers into 5G and 6G. Massive MIMO, a core 5G technology, uses dozens of antennas to form narrow beams towards individual users, multiplying capacity on the same spectrum. "
  "Chiplets -- smaller dies, possibly made on different processes and by different firms, joined by advanced packaging -- improve yields and lower costs as single giant chips become hard to make; packaging is a step in which India is investing through its semiconductor mission. Haptics adds touch to digital systems, from phone vibrations to surgical robots that let a surgeon feel tissue resistance at a distance.",
  "चारों कथन सही हैं। ओपन रैन रेडियो एक्सेस नेटवर्क को खुले इंटरफ़ेस वाले अंतःप्रचालनीय भागों में बाँटता है, ताकि ऑपरेटर को पूरा नेटवर्क एक ही विक्रेता से न ख़रीदना पड़े; भारत इसे 5जी और 6जी में घरेलू दूरसंचार निर्माताओं के प्रवेश का मार्ग मानता है। 5जी की मूल प्रौद्योगिकी मैसिव माइमो दर्जनों एंटेना से अलग-अलग उपयोगकर्ताओं की ओर संकरी किरणें बनाकर उसी स्पेक्ट्रम पर क्षमता कई गुना करता है। "
  "चिपलेट -- छोटी डाई, जो अलग-अलग प्रक्रियाओं और कंपनियों से बनी हो सकती हैं और उन्नत पैकेजिंग से जोड़ी जाती हैं -- एकल विशाल चिप बनाना कठिन होने पर उपज बढ़ाते और लागत घटाते हैं; पैकेजिंग वह चरण है जिसमें भारत अपने सेमीकंडक्टर मिशन से निवेश कर रहा है। हैप्टिक्स डिजिटल प्रणालियों में स्पर्श जोड़ता है, फ़ोन के कंपन से लेकर ऐसे शल्य रोबोटों तक जो सर्जन को दूर से ऊतक का प्रतिरोध अनुभव कराते हैं।",
  "Department of Telecommunications, Bharat 6G Vision (2023); India Semiconductor Mission (assembly, testing and packaging units).",
  "l4-s01-sci-open-ran-massive-mimo-chiplets-haptics", craft="precision")

# ---------------------------------------------------------------- Physics & Everyday Science (statement, medium)
S("Physics & Everyday Science", "medium", "With reference to nuclear fusion research, consider the following statements:",
  "नाभिकीय संलयन अनुसंधान के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["A tokamak confines a hot plasma with magnetic fields inside a doughnut-shaped chamber.",
   "A fusion reactor would produce long-lived high-level waste of the kind found in spent fission fuel.",
   "India has no tokamak of its own and takes part in ITER only as an observer."],
  ["टोकामैक डोनट-आकार के कक्ष के भीतर चुंबकीय क्षेत्रों से गर्म प्लाज़्मा को बाँधे रखता है।",
   "संलयन रिएक्टर विखंडन के प्रयुक्त ईंधन जैसा दीर्घजीवी उच्च-स्तरीय अपशिष्ट उत्पन्न करेगा।",
   "भारत के पास अपना कोई टोकामैक नहीं है और वह आईटीईआर में केवल पर्यवेक्षक के रूप में भाग लेता है।"],
  C3, 0,
  "Only statement 1 is correct. Fusion needs hydrogen isotopes heated to well over 100 million °C, at which no material wall can hold them; a tokamak, a Soviet design of the 1950s, uses powerful magnetic fields in a torus to keep the plasma away from the walls long enough for fusion to occur. "
  "Statement 2 is wrong: fusion of deuterium and tritium yields helium, not fission products; neutrons do make the reactor's structure radioactive, but this material is far shorter-lived than spent fission fuel, and there is no risk of a runaway chain reaction. Statement 3 is wrong: the Institute for Plasma Research at Gandhinagar runs the ADITYA tokamak and the Steady State Superconducting Tokamak (SST-1), and India has been a full member of ITER, the international fusion project in France, since 2005, supplying components such as the cryostat.",
  "केवल कथन 1 सही है। संलयन के लिए हाइड्रोजन समस्थानिकों को 10 करोड़ °C से कहीं अधिक गर्म करना होता है, जिस पर कोई भौतिक दीवार उन्हें नहीं रोक सकती; 1950 के दशक की सोवियत रचना टोकामैक एक टोरस में प्रबल चुंबकीय क्षेत्रों से प्लाज़्मा को दीवारों से इतनी देर दूर रखता है कि संलयन हो सके। "
  "कथन 2 ग़लत है: ड्यूटेरियम और ट्रिटियम के संलयन से हीलियम बनती है, विखंडन उत्पाद नहीं; न्यूट्रॉन रिएक्टर की संरचना को रेडियोधर्मी अवश्य बनाते हैं, पर यह पदार्थ विखंडन के प्रयुक्त ईंधन से कहीं कम समय तक सक्रिय रहता है, और अनियंत्रित शृंखला अभिक्रिया का कोई जोखिम नहीं है। कथन 3 ग़लत है: गांधीनगर का प्लाज़्मा अनुसंधान संस्थान आदित्य टोकामैक और स्थिर अवस्था अतिचालक टोकामैक (एसएसटी-1) चलाता है, और भारत 2005 से फ़्रांस में स्थित अंतरराष्ट्रीय संलयन परियोजना आईटीईआर का पूर्ण सदस्य है, जो क्रायोस्टैट जैसे घटक दे रहा है।",
  "Department of Atomic Energy, Institute for Plasma Research (ADITYA, SST-1) and ITER-India.",
  "l4-s01-sci-tokamak-fusion-waste-sst1-iter-member", craft="precision")

# ---------------------------------------------------------------- Space Technology & Missions (AR, hard)
A("Space Technology & Missions", "hard",
  "Debris left in low Earth orbit stays there permanently, whatever its altitude.",
  "निम्न भू-कक्षा में छोड़ा गया मलबा, ऊँचाई कुछ भी हो, स्थायी रूप से वहीं रहता है।",
  "The lower an object orbits, the more drag it experiences from the thin upper atmosphere, and the sooner it falls back and burns up.",
  "कोई पिंड जितनी नीची कक्षा में हो, उतना ही अधिक वह विरल ऊपरी वायुमंडल का कर्षण अनुभव करता है, और उतनी ही जल्दी वह नीचे गिरकर जल जाता है।",
  3,
  "Statement I is incorrect, but Statement II is correct. Even at a few hundred kilometres the atmosphere is not a perfect vacuum; its faint drag slowly lowers an object's orbit until it re-enters. Debris at around 300-400 km usually comes down within months to a few years -- faster when solar activity heats and swells the upper atmosphere -- while at 800 km and above it can stay for decades or centuries. "
  "That is why India's anti-satellite test of 2019 struck a target at about 300 km, so that the fragments would decay quickly, and why guidelines ask operators to bring satellites down within a set period after their mission ends. The danger is the Kessler syndrome: in crowded higher orbits, each collision creates fragments that cause more collisions, a cascade that could make some orbits unusable.",
  "कथन I ग़लत है, पर कथन II सही है। कुछ सौ किलोमीटर पर भी वायुमंडल पूर्ण निर्वात नहीं है; इसका क्षीण कर्षण धीरे-धीरे पिंड की कक्षा नीची करता है जब तक वह पुनः प्रवेश न कर ले। लगभग 300-400 किमी पर मलबा प्रायः कुछ महीनों से कुछ वर्षों में नीचे आ जाता है -- जब सौर सक्रियता ऊपरी वायुमंडल को गर्म कर फुला देती है तब और जल्दी -- जबकि 800 किमी और उससे ऊपर यह दशकों या सदियों तक रह सकता है। "
  "इसीलिए 2019 के भारत के उपग्रह-रोधी परीक्षण ने लगभग 300 किमी पर लक्ष्य भेदा, ताकि टुकड़े जल्दी नष्ट हों, और इसीलिए दिशानिर्देश संचालकों से मिशन समाप्त होने के बाद एक तय अवधि में उपग्रहों को नीचे लाने को कहते हैं। ख़तरा केसलर सिंड्रोम है: भीड़ भरी ऊँची कक्षाओं में हर टक्कर ऐसे टुकड़े बनाती है जो और टक्करें करते हैं, एक ऐसा क्रम जो कुछ कक्षाओं को अनुपयोगी बना सकता है।",
  "ISRO, Indian Space Situational Assessment Report and Debris-Free Space Missions; Inter-Agency Space Debris Coordination Committee, mitigation guidelines; Ministry of External Affairs, Mission Shakti (2019).",
  "l4-s01-sci-debris-orbital-decay-drag-kessler", craft="inference")

write("gs_l4_s01_f.sql")
