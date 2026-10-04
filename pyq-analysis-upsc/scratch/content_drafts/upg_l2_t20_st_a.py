# -*- coding: utf-8 -*-
"""Level 2 · Test 20 (Science & Technology 2: defence, energy, IT, space) -- depth audit of 2026-10-05, part A:
Defence, Aerospace & Security Technology and Energy & Environmental Technology (docs/upsc-question-design-standard.md
§6). Part B (upg_l2_t20_st_b.py) has IT, Communication & Emerging Technologies, Space Technology & Missions and the
tags for the kept rows.

Before the audit the test had analytic 17, precision 23, recall 66. Part A rewrites 20 recall rows in place
with the same concept id, type and difficulty:
  - cases and sums: a train running a red signal in fog, an LED left on for ten hours, a hydro plant's head
    and flow, storage technologies matched to jobs;
  - mechanisms: how a submarine dives, why stealth fighters carry weapons inside, why satellite launchers
    and missiles share technology, what a scramjet can and cannot do, why nuclear submarines stay down,
    how hydrogen cuts steel emissions, where OTEC works, why coal's carbon adds to the air, why swapping
    suits fleets, why hot panels underperform, why Indian waste burns poorly;
  - precision: the positive indigenisation lists, the doctrine's chemical/biological exception and the
    Nuclear Command Authority, Tejas's engine, fusion against fission and ITER's purpose, pumped storage as
    a store rather than a source.
Leaks avoided while drafting:
  - 'stealth aircraft are invisible to the eye' (old aircraft row) once the AMCA row tied stealth to radar,
    so the aircraft row now tests the Tejas engine;
  - flywheels 'steadying grid frequency' (the grid-inertia row's statement 2);
  - EVs' fewer moving parts (the e-bus AR's statement II), so the vehicle row was left;
  - methane in biogas (the compressed-biogas row's statement 2), so the geothermal-biogas row was left;
  - low-flying cruise missiles (the hypersonic-glide MCQ's key), so the missile-types row was left."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write_updates, CODE
from polity_common import C3, C4, T2

d.SUBJECT = "Science & Technology"
d.REQUIRE_CRAFT = True
DF = "Defence, Aerospace & Security Technology"
EN = "Energy & Environmental Technology"
MOD = "Ministry of Defence -- Annual Report."
MNRE = "Ministry of New and Renewable Energy."

# ================================================================ MCQs, defence (3)
M(DF, "easy", "A submarine dives below the surface mainly by:",
  "पनडुब्बी सतह से नीचे मुख्यतः किस प्रकार गोता लगाती है?",
  ["letting sea water into its ballast tanks to make it heavier for its size",
   "switching off all of its engines, so that it simply sinks to the depth it needs",
   "pumping extra compressed air into its tanks, which pushes the hull down",
   "folding its fins so that the water around it pushes it under"],
  ["अपनी गिट्टी टंकियों (बैलास्ट टैंक) में समुद्री पानी भरकर, ताकि वह अपने आकार के अनुपात में भारी हो जाए",
   "अपने इंजन बंद करके, ताकि वह अपने आप आवश्यक गहराई तक डूब जाए",
   "अपनी टंकियों में अतिरिक्त संपीडित हवा भरकर, जो पतवार को नीचे धकेलती है",
   "अपने पंख मोड़कर, ताकि आसपास का पानी उसे नीचे धकेल दे"],
  0,
  "A submarine floats when it weighs less than the water it displaces. Flooding the ballast tanks with sea water makes it heavier for its volume, so it sinks; to surface, compressed air blows the water out and it rises -- Archimedes' principle at work. Once under way, diving planes and the propeller fine-tune its depth.",
  "पनडुब्बी तब तैरती है जब उसका भार उसके द्वारा हटाए गए पानी से कम हो। गिट्टी टंकियों में समुद्री पानी भरने से वह अपने आयतन के अनुपात में भारी हो जाती है, इसलिए डूबती है; ऊपर आने के लिए संपीडित हवा पानी को बाहर निकाल देती है और वह उठती है; यही आर्किमिडीज़ का सिद्धांत है। चलते समय गोता-पंख और प्रणोदक उसकी गहराई को ठीक करते हैं।",
  "NCERT Class IX Science (Gravitation: Archimedes' principle).", "df-navy-submarines-easy", craft="linkage")

M(DF, "medium", "Fifth-generation fighters such as India's planned Advanced Medium Combat Aircraft (AMCA) carry their missiles in internal bays rather than under the wings mainly because:",
  "भारत के प्रस्तावित एडवांस्ड मीडियम कॉम्बैट एयरक्राफ़्ट (AMCA) जैसे पाँचवीं पीढ़ी के लड़ाकू विमान अपनी मिसाइलें पंखों के नीचे के बजाय भीतरी खानों में मुख्यतः इसलिए रखते हैं क्योंकि:",
  ["weapons hung outside the body reflect radar waves and spoil its stealth",
   "internal bays let the aircraft carry more weapons than wing pylons do",
   "missiles carried outside would freeze solid at high cruising altitudes",
   "international law forbids fighters to show weapons on peacetime patrols"],
  ["ढाँचे के बाहर लटके हथियार रडार तरंगें परावर्तित करते हैं और उसकी गुप्तता बिगाड़ देते हैं",
   "भीतरी खाने विमान को पंखों के तोरणों से अधिक हथियार ले जाने देते हैं",
   "बाहर ले जाई गई मिसाइलें ऊँचाई पर उड़ते समय पूरी तरह जम जाएँगी",
   "अंतरराष्ट्रीय क़ानून शांतिकाल की गश्त में लड़ाकू विमानों को हथियार दिखाने से रोकता है"],
  0,
  "Stealth comes mainly from shaping and coatings that scatter or absorb radar waves instead of sending them back to the radar; bombs, missiles and fuel tanks hung under the wings are strong reflectors. So stealth fighters carry weapons inside, at the cost of carrying fewer, and use external pylons only when stealth matters less. "
  "The twin-engine AMCA is being developed by the Aeronautical Development Agency, with private industry invited to partner in building it.",
  "गुप्तता (स्टेल्थ) मुख्यतः ऐसे आकार और लेपों से आती है जो रडार तरंगों को रडार की ओर लौटाने के बजाय बिखेर या सोख लेते हैं; पंखों के नीचे लटके बम, मिसाइलें और ईंधन टंकियाँ प्रबल परावर्तक हैं। इसलिए स्टेल्थ लड़ाकू विमान हथियार भीतर रखते हैं, भले ही कम ले जा सकें, और बाहरी तोरणों का उपयोग तभी करते हैं जब गुप्तता कम महत्त्वपूर्ण हो। "
  "दो इंजन वाला AMCA वैमानिकी विकास एजेंसी विकसित कर रही है, और निजी उद्योग को उसके निर्माण में साझेदार बनने के लिए आमंत्रित किया गया है।",
  "Ministry of Defence -- Aeronautical Development Agency (AMCA programme).", "df-amca", craft="linkage")

M(DF, "medium", "In thick fog, the loco pilot of a train fitted with 'Kavach' fails to slow down for a red signal ahead. The system will:",
  "घने कोहरे में 'कवच' से युक्त एक रेलगाड़ी का लोको पायलट आगे के लाल सिग्नल के लिए गति कम नहीं करता। यह प्रणाली:",
  ["apply the brakes on its own to stop the train before the signal",
   "only record the event, so that it can be examined in an inquiry later",
   "alert the station master, who must then cut off power to the line",
   "sound a warning to passengers so that they can brace themselves"],
  ["अपने आप ब्रेक लगाकर रेलगाड़ी को सिग्नल से पहले रोक देगी",
   "केवल घटना दर्ज करेगी, ताकि बाद में जाँच में उसकी पड़ताल हो सके",
   "स्टेशन मास्टर को सचेत करेगी, जिसे तब लाइन की बिजली काटनी होगी",
   "यात्रियों के लिए चेतावनी बजाएगी ताकि वे सँभल सकें"],
  0,
  "Kavach, India's indigenous automatic train protection system developed by the Research Designs and Standards Organisation with Indian firms, links locomotives, stations and track-side equipment by radio. It shows signal aspects in the cab and, if the pilot passes a red signal or overspeeds, brakes the train automatically; it also stops two trains on the same line from closing in on each other. "
  "It is certified to Safety Integrity Level 4, the highest, and is being rolled out across the network.",
  "अनुसंधान अभिकल्प एवं मानक संगठन द्वारा भारतीय फ़र्मों के साथ विकसित भारत की स्वदेशी स्वचालित रेल सुरक्षा प्रणाली कवच इंजनों, स्टेशनों और पटरी के उपकरणों को रेडियो से जोड़ती है। यह केबिन में सिग्नल दिखाती है और यदि पायलट लाल सिग्नल पार करे या अधिक गति से चले, तो अपने आप ब्रेक लगा देती है; यह एक ही लाइन पर दो रेलगाड़ियों को एक-दूसरे के पास आने से भी रोकती है। "
  "इसे सर्वोच्च सुरक्षा अखंडता स्तर 4 का प्रमाण मिला है और इसे पूरे नेटवर्क में लगाया जा रहा है।",
  "Ministry of Railways -- Kavach.", "df-kavach", craft="application")

# ================================================================ MCQs, energy (3)
M(EN, "easy", "A hydroelectric plant will generate more electricity when:",
  "जलविद्युत संयंत्र अधिक बिजली कब उत्पन्न करेगा?",
  ["more water falls through its turbines from a greater height",
   "the water stored in its reservoir is much warmer than it usually is",
   "the river brings more silt into its reservoir",
   "the sun shines more strongly on the dam's walls"],
  ["जब अधिक पानी अधिक ऊँचाई से उसके टरबाइनों से होकर गिरे",
   "जब उसके जलाशय में भरा पानी सामान्य से बहुत अधिक गर्म हो",
   "जब नदी उसके जलाशय में अधिक गाद लाए",
   "जब बाँध की दीवारों पर धूप अधिक तेज़ पड़े"],
  0,
  "A hydro plant turns the energy of falling water into electricity, so its output depends on how much water flows through the turbines each second and on the 'head', the height it falls -- which is why plants are built in hills with steep drops, and why output falls in dry years. "
  "Warm water makes no difference; silt fills reservoirs and wears turbines, cutting output; sunlight plays no direct part.",
  "जलविद्युत संयंत्र गिरते पानी की ऊर्जा को बिजली में बदलता है, इसलिए उसका उत्पादन इस पर निर्भर है कि प्रति सेकंड कितना पानी टरबाइनों से बहता है और 'हेड', यानी वह कितनी ऊँचाई से गिरता है; इसीलिए संयंत्र तीखे ढलानों वाली पहाड़ियों में बनते हैं, और सूखे वर्षों में उत्पादन घटता है। "
  "गर्म पानी से कोई अंतर नहीं पड़ता; गाद जलाशय भरती है और टरबाइनों को घिसती है, जिससे उत्पादन घटता है; धूप की कोई सीधी भूमिका नहीं है।",
  "NCERT Class X Science (Sources of Energy).", "en-hydro-easy", craft="inference")

M(EN, "medium", "Making iron with hydrogen instead of coal can cut the carbon dioxide emitted by steel plants mainly because:",
  "कोयले के बजाय हाइड्रोजन से लोहा बनाने से इस्पात संयंत्रों का कार्बन डाइऑक्साइड उत्सर्जन मुख्यतः इसलिए घट सकता है क्योंकि:",
  ["hydrogen removes oxygen from iron ore and forms water instead of CO2",
   "hydrogen absorbs the carbon dioxide given off by the blast furnace",
   "hydrogen lowers the melting point of iron, so less fuel needs to be burnt",
   "steel made with hydrogen needs no iron ore at all"],
  ["हाइड्रोजन लौह अयस्क से ऑक्सीजन हटाकर CO2 के बजाय पानी बनाती है",
   "हाइड्रोजन वात्या भट्टी से निकलने वाली कार्बन डाइऑक्साइड सोख लेती है",
   "हाइड्रोजन लोहे का गलनांक घटाती है, इसलिए कम ईंधन जलाना पड़ता है",
   "हाइड्रोजन से बने इस्पात में लौह अयस्क की आवश्यकता ही नहीं होती"],
  0,
  "In a blast furnace, carbon from coke takes the oxygen out of iron ore and leaves as CO2 -- around two tonnes of it for each tonne of steel. In hydrogen-based direct reduction, hydrogen does the same job and the by-product is water vapour. "
  "The cut is real only if the hydrogen is itself made with clean electricity and the furnace runs on clean power; recycling scrap in electric arc furnaces is the other main route. India's green steel taxonomy of 2024 grades steel by its emissions per tonne.",
  "वात्या भट्टी में कोक का कार्बन लौह अयस्क से ऑक्सीजन निकालता है और CO2 बनकर निकलता है, हर टन इस्पात पर लगभग दो टन। हाइड्रोजन-आधारित प्रत्यक्ष अपचयन में हाइड्रोजन यही काम करती है और उप-उत्पाद जलवाष्प होता है। "
  "कटौती तभी वास्तविक है जब हाइड्रोजन स्वयं स्वच्छ बिजली से बने और भट्टी स्वच्छ ऊर्जा से चले; विद्युत आर्क भट्टियों में स्क्रैप का पुनर्चक्रण दूसरा मुख्य मार्ग है। भारत की 2024 की हरित इस्पात वर्गीकरण-पद्धति इस्पात को प्रति टन उत्सर्जन के आधार पर श्रेणीबद्ध करती है।",
  "Ministry of Steel -- Greening the Steel Sector; Green Steel Taxonomy, 2024.", "en-green-steel", craft="linkage")

M(EN, "medium", "Ocean thermal energy conversion (OTEC) plants, which use the temperature difference between surface and deep water, are best sited in:",
  "सतही और गहरे पानी के तापमान-अंतर का उपयोग करने वाले महासागरीय तापीय ऊर्जा रूपांतरण (OTEC) संयंत्र सबसे उपयुक्त कहाँ हैं?",
  ["tropical seas, where surface water is far warmer than deep water",
   "polar seas, where the water is coldest all year round",
   "shallow bays that have the greatest difference between high and low tide",
   "coasts that are swept by the strongest and steadiest winds"],
  ["उष्णकटिबंधीय समुद्रों में, जहाँ सतही पानी गहरे पानी से कहीं अधिक गर्म है",
   "ध्रुवीय समुद्रों में, जहाँ पानी साल भर सबसे ठंडा रहता है",
   "उथली खाड़ियों में जहाँ ज्वार और भाटे का अंतर सबसे अधिक है",
   "उन तटों पर जहाँ सबसे तेज़ और स्थिर हवाएँ चलती हैं"],
  0,
  "OTEC needs a temperature gap of about 20 °C, which exists only in the tropics, where the sun keeps surface water warm while water below about 1,000 m stays cold everywhere. Warm water boils a working fluid such as ammonia to spin a turbine, and cold deep water condenses it again; deep water close to the coast helps, as off Lakshadweep, where the National Institute of Ocean Technology is building an OTEC-powered desalination plant at Kavaratti. "
  "Tidal range matters for tidal barrages and wind for wind farms, not for OTEC.",
  "OTEC को लगभग 20 °C का तापमान-अंतर चाहिए, जो केवल उष्णकटिबंध में है, जहाँ सूर्य सतही पानी को गर्म रखता है जबकि लगभग 1,000 मीटर से नीचे का पानी हर जगह ठंडा रहता है। गर्म पानी अमोनिया जैसे कार्यकारी द्रव को उबालकर टरबाइन घुमाता है, और ठंडा गहरा पानी उसे फिर संघनित करता है; तट के पास गहरा पानी सहायक है, जैसे लक्षद्वीप के पास, जहाँ राष्ट्रीय समुद्र प्रौद्योगिकी संस्थान कवरत्ती में OTEC-चालित विलवणीकरण संयंत्र बना रहा है। "
  "ज्वार का अंतर ज्वारीय बैराजों के लिए और हवा पवन फ़ार्मों के लिए मायने रखती है, OTEC के लिए नहीं।",
  "Ministry of Earth Sciences -- National Institute of Ocean Technology.", "en-otec", craft="inference")

# ================================================================ two-statement rows (3)
S(DF, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["DRDO develops technologies for the armed forces.",
   "A country that can launch satellites into orbit already has much of the rocket technology needed for long-range missiles."],
  ["DRDO सशस्त्र बलों के लिए प्रौद्योगिकियाँ विकसित करता है।",
   "जो देश उपग्रहों को कक्षा में प्रक्षेपित कर सकता है, उसके पास लंबी दूरी की मिसाइलों के लिए आवश्यक रॉकेट प्रौद्योगिकी का बड़ा भाग पहले से होता है।"],
  T2, 2,
  "Both statements are correct. DRDO, under the Ministry of Defence, designs missiles, radars, electronic-warfare systems and much else for the forces. Rockets that put satellites in orbit and long-range missiles share propulsion, guidance and staging technology -- which is why launchers fall under export controls such as the Missile Technology Control Regime, which India joined in 2016. "
  "The difference lies in payload and path: a satellite is placed in orbit, while a missile carries a warhead back down to a target.",
  "दोनों कथन सही हैं। रक्षा मंत्रालय के अधीन DRDO बलों के लिए मिसाइलें, रडार, इलेक्ट्रॉनिक युद्ध प्रणालियाँ और बहुत कुछ बनाता है। उपग्रहों को कक्षा में पहुँचाने वाले रॉकेट और लंबी दूरी की मिसाइलें प्रणोदन, मार्गदर्शन और चरणबद्धता की प्रौद्योगिकी साझा करते हैं; इसीलिए प्रक्षेपक मिसाइल प्रौद्योगिकी नियंत्रण व्यवस्था जैसे निर्यात नियंत्रणों के अधीन हैं, जिसमें भारत 2016 में शामिल हुआ। "
  "अंतर नीतभार और पथ में है: उपग्रह कक्षा में रखा जाता है, जबकि मिसाइल आयुध लेकर लक्ष्य पर लौटती है।",
  MOD, "df-drdo-missile-satellite-easy", craft="linkage")

S(EN, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["A 9 W LED bulb left on for 10 hours uses 0.9 units (kWh) of electricity.",
   "Wind turbines burn coal to turn their blades."],
  ["10 घंटे जलता छोड़ा गया 9 W का LED बल्ब 0.9 यूनिट (kWh) बिजली ख़र्च करता है।",
   "पवन टरबाइन अपने ब्लेड घुमाने के लिए कोयला जलाते हैं।"],
  T2, 3,
  "Neither statement is correct. Energy = power x time: 9 W x 10 h = 90 watt-hours, or 0.09 kWh -- a tenth of the figure in statement 1, which slips a decimal place; one 'unit' on an electricity bill is one kilowatt-hour. "
  "Statement 2 is wrong: moving air turns the blades, which drive a generator; no fuel is burnt.",
  "दोनों में से कोई कथन सही नहीं है। ऊर्जा = शक्ति x समय: 9 W x 10 घंटे = 90 वाट-घंटे, यानी 0.09 kWh, जो कथन 1 के आँकड़े का दसवाँ भाग है; कथन 1 में दशमलव एक स्थान खिसक गया है; बिजली के बिल की एक 'यूनिट' एक किलोवाट-घंटा है। "
  "कथन 2 गलत है: चलती हवा ब्लेड घुमाती है, जो जनित्र चलाते हैं; कोई ईंधन नहीं जलता।",
  "NCERT Class IX Science (Work and Energy); Bureau of Energy Efficiency.", "en-led-wind-easy", craft="application")

S(EN, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Solar and wind are renewable sources of energy.",
   "Since coal formed from plants that took carbon dioxide out of the air long ago, burning it adds no extra carbon dioxide to today's atmosphere."],
  ["सौर और पवन ऊर्जा के नवीकरणीय स्रोत हैं।",
   "चूँकि कोयला उन पौधों से बना है जिन्होंने बहुत पहले हवा से कार्बन डाइऑक्साइड ली थी, इसलिए उसे जलाने से आज के वायुमंडल में कोई अतिरिक्त कार्बन डाइऑक्साइड नहीं जुड़ती।"],
  T2, 0,
  "Only statement 1 is correct. Statement 2 is wrong: the carbon in coal was locked away underground for millions of years, so burning it returns long-buried carbon to the air within years, raising the amount of CO2 in the atmosphere. "
  "That is the difference from burning wood or crop waste, whose carbon was taken from the air recently and can be taken up again as plants regrow.",
  "केवल कथन 1 सही है। कथन 2 गलत है: कोयले का कार्बन लाखों वर्षों से भूमिगत बंद था, इसलिए उसे जलाना लंबे समय से दबे कार्बन को कुछ ही वर्षों में हवा में लौटा देता है, जिससे वायुमंडल में CO2 की मात्रा बढ़ती है। "
  "लकड़ी या फ़सल अवशेष जलाने से यही अंतर है, जिनका कार्बन हाल ही में हवा से लिया गया था और पौधों के फिर उगने पर फिर से लिया जा सकता है।",
  "NCERT Class VIII Science (Coal and Petroleum); NCERT Class XI Geography.", "en-renewables-coal-easy", craft="inference")

# ================================================================ three- and four-statement rows, defence (5)
S(DF, "hard", "Consider the following statements about India's defence industry:",
  "भारत के रक्षा उद्योग के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["India's defence exports crossed ₹20,000 crore in 2023-24.",
   "The iDEX programme funds start-ups and innovators to develop defence technology.",
   "Items on the Ministry of Defence's 'positive indigenisation lists' may be bought only from Indian industry once the deadlines set for them have passed."],
  ["2023-24 में भारत का रक्षा निर्यात ₹20,000 करोड़ से अधिक हो गया।",
   "iDEX कार्यक्रम रक्षा प्रौद्योगिकी विकसित करने के लिए स्टार्ट-अप और नवप्रवर्तकों को वित्त देता है।",
   "रक्षा मंत्रालय की 'सकारात्मक स्वदेशीकरण सूचियों' की वस्तुएँ उनके लिए तय समय-सीमाएँ बीतने के बाद केवल भारतीय उद्योग से ख़रीदी जा सकती हैं।"],
  C3, 2,
  "All three statements are correct. Exports -- of BrahMos missiles, artillery, radars, patrol vessels and components -- reached about ₹21,000 crore in 2023-24 and over ₹23,000 crore in 2024-25. iDEX (Innovations for Defence Excellence), launched in 2018, gives grants through open challenges. "
  "The positive indigenisation lists, issued since 2020 for the services and for defence PSUs, set dates after which hundreds of weapons, platforms and components may no longer be imported -- an import embargo meant to give Indian firms an assured market.",
  "तीनों कथन सही हैं। ब्रह्मोस मिसाइलों, तोपों, रडारों, गश्ती पोतों और पुर्ज़ों का निर्यात 2023-24 में लगभग ₹21,000 करोड़ और 2024-25 में ₹23,000 करोड़ से अधिक हो गया। 2018 में शुरू हुआ iDEX (रक्षा उत्कृष्टता के लिए नवाचार) खुली चुनौतियों के माध्यम से अनुदान देता है। "
  "2020 से सेनाओं और रक्षा सार्वजनिक उपक्रमों के लिए जारी सकारात्मक स्वदेशीकरण सूचियाँ ऐसी तिथियाँ तय करती हैं जिनके बाद सैकड़ों हथियार, प्लेटफ़ॉर्म और पुर्ज़े आयात नहीं किए जा सकते; यह आयात-प्रतिबंध भारतीय फ़र्मों को सुनिश्चित बाज़ार देने के लिए है।",
  MOD, "df-defence-industry", craft="precision")

S(DF, "hard", "Consider the following statements about India's nuclear deterrent:",
  "भारत के परमाणु प्रतिरोध के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["India's nuclear doctrine includes a commitment to 'no first use'.",
   "The doctrine keeps open the option of nuclear retaliation against a major attack on India with biological or chemical weapons.",
   "The decision to use nuclear weapons rests with the commander of the Strategic Forces Command."],
  ["भारत के परमाणु सिद्धांत में 'पहले उपयोग न करने' की प्रतिबद्धता शामिल है।",
   "सिद्धांत भारत पर जैविक या रासायनिक हथियारों से बड़े हमले के विरुद्ध परमाणु प्रतिशोध का विकल्प खुला रखता है।",
   "परमाणु हथियारों के उपयोग का निर्णय सामरिक बल कमान के कमांडर के पास है।"],
  C3, 1,
  "Statements 1 and 2 are correct. Under the doctrine of January 2003, India will not use nuclear weapons first, keeps a 'credible minimum deterrent' and promises massive retaliation if attacked; the one stated exception to no first use is a major biological or chemical attack. "
  "Statement 3 is the near-miss: the Strategic Forces Command manages and operates the weapons, but the authority to order their use lies with the Political Council of the Nuclear Command Authority, chaired by the Prime Minister. India also has a triad of land-based missiles, aircraft and submarines.",
  "कथन 1 और 2 सही हैं। जनवरी 2003 के सिद्धांत के तहत भारत परमाणु हथियारों का पहले उपयोग नहीं करेगा, 'विश्वसनीय न्यूनतम प्रतिरोध' रखता है और हमला होने पर व्यापक प्रतिशोध का वचन देता है; पहले उपयोग न करने का एकमात्र घोषित अपवाद बड़ा जैविक या रासायनिक हमला है। "
  "कथन 3 निकट-भ्रम है: सामरिक बल कमान हथियारों का प्रबंधन और संचालन करती है, पर उनके उपयोग का आदेश देने का अधिकार प्रधानमंत्री की अध्यक्षता वाली परमाणु कमान प्राधिकरण की राजनीतिक परिषद के पास है। भारत के पास भूमि-आधारित मिसाइलों, विमानों और पनडुब्बियों की त्रयी भी है।",
  "Cabinet Committee on Security -- review of the nuclear doctrine, January 2003.", "df-nuclear-doctrine", craft="precision")

S(DF, "medium", "Consider the following statements about military aircraft:",
  "सैन्य विमानों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Tejas is a light combat aircraft designed by the Aeronautical Development Agency and built by HAL.",
   "The Rafale jets flown by the Indian Air Force were built by Dassault Aviation of France.",
   "The Tejas Mk1A is powered by the indigenous Kaveri engine."],
  ["तेजस वैमानिकी विकास एजेंसी द्वारा अभिकल्पित और HAL द्वारा निर्मित एक हल्का लड़ाकू विमान है।",
   "भारतीय वायु सेना के राफ़ेल विमान फ़्रांस की डसॉल्ट एविएशन ने बनाए थे।",
   "तेजस Mk1A स्वदेशी कावेरी इंजन से चलता है।"],
  C3, 1,
  "Statements 1 and 2 are correct. Statement 3 is the near-miss: the Kaveri engine, under development by DRDO's Gas Turbine Research Establishment since the 1980s, did not reach the thrust the fighter needs, so Tejas flies on the American GE F404, and delays in its supply slowed Mk1A deliveries; the Mk2 is to use the more powerful GE F414, to be made in India by HAL. "
  "Engines remain the largest gap in India's aerospace industry.",
  "कथन 1 और 2 सही हैं। कथन 3 निकट-भ्रम है: DRDO के गैस टरबाइन अनुसंधान प्रतिष्ठान द्वारा 1980 के दशक से विकसित किया जा रहा कावेरी इंजन लड़ाकू विमान के लिए आवश्यक प्रणोद तक नहीं पहुँचा, इसलिए तेजस अमेरिकी GE F404 इंजन से उड़ता है, और उसकी आपूर्ति में देरी ने Mk1A की डिलीवरी धीमी की; Mk2 में अधिक शक्तिशाली GE F414 लगेगा, जिसे HAL भारत में बनाएगा। "
  "इंजन भारत के वैमानिकी उद्योग की सबसे बड़ी कमी बने हुए हैं।",
  MOD, "df-aircraft-none", craft="precision")

S(DF, "medium", "Consider the following statements about hypersonic technology:",
  "हाइपरसोनिक प्रौद्योगिकी के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Hypersonic speeds are those above five times the speed of sound.",
   "Because a scramjet takes its oxygen from the air, it cannot work in space.",
   "A scramjet cannot start from rest; a rocket must first boost the vehicle to very high speed."],
  ["हाइपरसोनिक गतियाँ ध्वनि की गति के पाँच गुना से अधिक की गतियाँ हैं।",
   "चूँकि स्क्रैमजेट अपनी ऑक्सीजन हवा से लेता है, इसलिए वह अंतरिक्ष में काम नहीं कर सकता।",
   "स्क्रैमजेट स्थिर अवस्था से चालू नहीं हो सकता; पहले एक रॉकेट को वाहन को बहुत ऊँची गति तक पहुँचाना होता है।"],
  C3, 2,
  "All three statements are correct. A scramjet -- a supersonic-combustion ramjet -- has no compressor or turbine: air rammed in at supersonic speed is squeezed by the shape of the intake and burns with the fuel while still moving faster than sound. "
  "Using atmospheric oxygen saves the weight of an oxidiser tank, but it means the engine works only within the atmosphere, and only once the vehicle is already flying at around Mach 4-5. DRDO tested a long-range hypersonic missile in November 2024 and has run scramjet combustors for long durations in ground tests.",
  "तीनों कथन सही हैं। स्क्रैमजेट, यानी सुपरसोनिक-दहन रैमजेट, में न कंप्रेसर होता है न टरबाइन: सुपरसोनिक गति से भीतर घुसी हवा अंतर्ग्रहण के आकार से दबती है और ध्वनि से तेज़ चलते-चलते ही ईंधन के साथ जलती है। "
  "वायुमंडल की ऑक्सीजन का उपयोग ऑक्सीकारक टंकी का भार बचाता है, पर इसका अर्थ है कि इंजन केवल वायुमंडल के भीतर काम करता है, और तभी जब वाहन पहले से लगभग मैक 4-5 पर उड़ रहा हो। DRDO ने नवंबर 2024 में लंबी दूरी की हाइपरसोनिक मिसाइल का परीक्षण किया और भूमि परीक्षणों में स्क्रैमजेट दहन-कक्षों को लंबी अवधि तक चलाया है।",
  "Defence Research and Development Organisation.", "df-hypersonic-scramjet", craft="linkage")

S(DF, "medium", "Consider the following statements about the Indian Navy:",
  "भारतीय नौसेना के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["INS Vikrant is India's first indigenously built aircraft carrier.",
   "INS Arihant is a nuclear-powered submarine that carries ballistic missiles.",
   "Diesel-electric submarines can stay submerged as long as nuclear-powered ones, since their batteries never need recharging."],
  ["INS विक्रांत भारत का पहला स्वदेशी रूप से निर्मित विमानवाहक पोत है।",
   "INS अरिहंत बैलिस्टिक मिसाइलें ले जाने वाली परमाणु-चालित पनडुब्बी है।",
   "डीज़ल-विद्युत पनडुब्बियाँ परमाणु-चालित पनडुब्बियों जितनी देर जलमग्न रह सकती हैं, क्योंकि उनकी बैटरियों को कभी चार्ज करने की आवश्यकता नहीं होती।"],
  C3, 1,
  "Statements 1 and 2 are correct: Vikrant, built at Cochin Shipyard and commissioned in 2022, made India one of the few countries able to design and build a carrier, and Arihant gives the sea-based leg of the nuclear deterrent. "
  "Statement 3 is wrong: a diesel-electric boat such as the Kalvari class runs underwater on batteries that its diesel engines must recharge, which needs air, so it must come near the surface every few days unless fitted with air-independent propulsion; a nuclear reactor needs no air, so a nuclear submarine's time submerged is limited mainly by food and crew.",
  "कथन 1 और 2 सही हैं: कोचीन शिपयार्ड में बना और 2022 में सेवा में आया विक्रांत भारत को विमानवाहक पोत अभिकल्पित और निर्मित कर सकने वाले गिने-चुने देशों में ले आया, और अरिहंत परमाणु प्रतिरोध का समुद्र-आधारित भाग है। "
  "कथन 3 गलत है: कलवरी श्रेणी जैसी डीज़ल-विद्युत पनडुब्बी पानी के नीचे बैटरियों से चलती है जिन्हें उसके डीज़ल इंजन चार्ज करते हैं, जिसके लिए हवा चाहिए, इसलिए उसे हर कुछ दिनों में सतह के पास आना पड़ता है, जब तक उसमें वायु-निरपेक्ष प्रणोदन न हो; परमाणु रिएक्टर को हवा नहीं चाहिए, इसलिए परमाणु पनडुब्बी के जलमग्न रहने की अवधि मुख्यतः भोजन और चालक दल से सीमित होती है।",
  "Ministry of Defence -- Indian Navy.", "df-navy-platforms", craft="linkage")

# ================================================================ three- and four-statement rows, energy (6)
S(EN, "medium", "Consider the following statements about electric mobility:",
  "विद्युत गतिशीलता के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Battery swapping suits e-rickshaws and delivery fleets, because the vehicles need not sit idle while a battery charges.",
   "The PM E-DRIVE scheme of 2024 took over from FAME-II as the Centre's main scheme for EV incentives.",
   "Most electric two-wheelers in India run on hydrogen fuel cells."],
  ["बैटरी अदला-बदली ई-रिक्शा और डिलीवरी बेड़ों के लिए उपयुक्त है, क्योंकि बैटरी चार्ज होते समय वाहनों को खड़ा नहीं रहना पड़ता।",
   "2024 की PM E-DRIVE योजना ने FAME-II का स्थान केंद्र की EV प्रोत्साहन की मुख्य योजना के रूप में लिया।",
   "भारत के अधिकांश विद्युत दोपहिया वाहन हाइड्रोजन ईंधन सेलों से चलते हैं।"],
  C3, 1,
  "Statements 1 and 2 are correct. A rickshaw or delivery scooter earns only while moving, so swapping a flat battery for a charged one in minutes beats waiting hours to recharge; batteries can then be charged centrally and owned by the swapping operator, cutting the vehicle's price. "
  "PM E-DRIVE supports two- and three-wheelers, e-buses, e-ambulances, e-trucks and charging stations. Statement 3 is wrong: electric two-wheelers run on lithium-ion batteries; fuel cells are being tried in buses and trucks.",
  "कथन 1 और 2 सही हैं। रिक्शा या डिलीवरी स्कूटर चलते समय ही कमाता है, इसलिए कुछ मिनटों में ख़ाली बैटरी को चार्ज बैटरी से बदलना घंटों चार्ज की प्रतीक्षा से बेहतर है; बैटरियाँ फिर केंद्रीय रूप से चार्ज होकर अदला-बदली संचालक के स्वामित्व में रह सकती हैं, जिससे वाहन का मूल्य घटता है। "
  "PM E-DRIVE दोपहिया और तिपहिया वाहनों, ई-बसों, ई-एम्बुलेंसों, ई-ट्रकों और चार्जिंग स्टेशनों को सहायता देती है। कथन 3 गलत है: विद्युत दोपहिया लिथियम-आयन बैटरियों से चलते हैं; ईंधन सेलों का परीक्षण बसों और ट्रकों में हो रहा है।",
  "Ministry of Heavy Industries -- PM E-DRIVE; NITI Aayog -- battery swapping.", "en-electric-mobility", craft="linkage")

S(EN, "medium", "Consider the following statements about storing energy:",
  "ऊर्जा भंडारण के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Flywheels and supercapacitors suit very short, fast bursts of power lasting seconds or minutes.",
   "Compressed-air storage in underground caverns suits storing energy for several hours.",
   "Supercapacitors are the cheapest way to store energy from summer for use in winter.",
   "Green hydrogen can hold surplus renewable energy for weeks or seasons, though much of the energy is lost in converting it."],
  ["फ़्लाईव्हील और सुपरकैपेसिटर कुछ सेकंड या मिनट चलने वाले बहुत छोटे, तेज़ शक्ति-झोंकों के लिए उपयुक्त हैं।",
   "भूमिगत गुफाओं में संपीडित-वायु भंडारण कई घंटों तक ऊर्जा संचित रखने के लिए उपयुक्त है।",
   "गर्मी की ऊर्जा को सर्दी में उपयोग के लिए संचित करने का सबसे सस्ता तरीका सुपरकैपेसिटर हैं।",
   "हरित हाइड्रोजन अतिरिक्त नवीकरणीय ऊर्जा को सप्ताहों या मौसमों तक संचित रख सकती है, यद्यपि रूपांतरण में ऊर्जा का बड़ा भाग नष्ट होता है।"],
  C4, 2,
  "Statements 1, 2 and 4 are correct; each technology suits a different job. Flywheels store energy as spinning motion and supercapacitors as electric charge; both deliver it in seconds but hold little. Compressed air and pumped water store energy for hours, covering the evening peak. "
  "Statement 3 is wrong: supercapacitors hold far too little energy, and lose charge too quickly, for seasonal storage; for that, hydrogen is the leading candidate, even though only about a third of the electricity used to make it comes back.",
  "कथन 1, 2 और 4 सही हैं; हर प्रौद्योगिकी अलग काम के लिए उपयुक्त है। फ़्लाईव्हील ऊर्जा को घूर्णन गति के रूप में और सुपरकैपेसिटर विद्युत आवेश के रूप में संचित करते हैं; दोनों उसे सेकंडों में देते हैं पर थोड़ी ही रखते हैं। संपीडित हवा और पंप किया गया पानी ऊर्जा को घंटों तक संचित रखते हैं, जो शाम की चरम माँग पूरी करता है। "
  "कथन 3 गलत है: सुपरकैपेसिटर मौसमी भंडारण के लिए बहुत कम ऊर्जा रखते हैं और बहुत जल्दी आवेश खोते हैं; इसके लिए हाइड्रोजन प्रमुख विकल्प है, यद्यपि उसे बनाने में लगी बिजली का लगभग एक-तिहाई ही वापस मिलता है।",
  "Central Electricity Authority -- energy storage; " + MNRE, "en-energy-storage-types", craft="application")

S(EN, "medium", "Consider the following statements about nuclear fusion:",
  "नाभिकीय संलयन के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["ITER, the international fusion experiment, is being built in France, and India is one of its members.",
   "Fusion releases energy by splitting heavy nuclei such as uranium.",
   "ITER is designed to supply electricity to the French grid."],
  ["अंतरराष्ट्रीय संलयन प्रयोग ITER फ़्रांस में बनाया जा रहा है, और भारत उसका एक सदस्य है।",
   "संलयन यूरेनियम जैसे भारी नाभिकों को तोड़कर ऊर्जा छोड़ता है।",
   "ITER फ़्रांस के ग्रिड को बिजली देने के लिए अभिकल्पित है।"],
  C3, 0,
  "Only statement 1 is correct. Statement 2 is the near-miss: splitting heavy nuclei is fission, used in today's reactors; fusion joins light nuclei, such as the hydrogen isotopes deuterium and tritium, the process that powers the Sun. "
  "Statement 3 is wrong: ITER is an experiment meant to show that a fusion plasma can give out about ten times the heating power put into it; it will not generate electricity, which is left to later demonstration plants. India, a member since 2005 along with the EU, China, Japan, Korea, Russia and the United States, supplies components such as the cryostat, the giant steel vessel around the machine.",
  "केवल कथन 1 सही है। कथन 2 निकट-भ्रम है: भारी नाभिकों को तोड़ना विखंडन है, जो आज के रिएक्टरों में होता है; संलयन ड्यूटेरियम और ट्रिटियम जैसे हाइड्रोजन समस्थानिकों जैसे हल्के नाभिकों को जोड़ता है, यही प्रक्रिया सूर्य को ऊर्जा देती है। "
  "कथन 3 गलत है: ITER एक प्रयोग है जिसका उद्देश्य यह दिखाना है कि संलयन प्लाज़्मा उसमें डाली गई ताप-शक्ति से लगभग दस गुना शक्ति दे सकता है; यह बिजली नहीं बनाएगा, जो बाद के प्रदर्शन संयंत्रों पर छोड़ा गया है। 2005 से सदस्य भारत, यूरोपीय संघ, चीन, जापान, कोरिया, रूस और अमेरिका के साथ, क्रायोस्टैट जैसे पुर्ज़े देता है, जो मशीन के चारों ओर का विशाल इस्पाती पात्र है।",
  "Department of Atomic Energy -- ITER-India, Institute for Plasma Research.", "en-fusion-iter", craft="precision")

S(EN, "medium", "Consider the following statements about pumped storage:",
  "पंप भंडारण के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["A pumped storage plant pumps water to an upper reservoir when power is cheap and releases it through turbines when power is needed.",
   "Over a full cycle, a pumped storage plant generates more electricity than it uses for pumping.",
   "It can switch from pumping to generating within minutes, which helps to balance the grid."],
  ["पंप भंडारण संयंत्र बिजली सस्ती होने पर पानी ऊपरी जलाशय में पंप करता है और बिजली की आवश्यकता होने पर उसे टरबाइनों से छोड़ता है।",
   "एक पूरे चक्र में पंप भंडारण संयंत्र पंपिंग में लगी बिजली से अधिक बिजली उत्पन्न करता है।",
   "यह कुछ ही मिनटों में पंपिंग से उत्पादन पर जा सकता है, जिससे ग्रिड को संतुलित करने में सहायता मिलती है।"],
  C3, 1,
  "Statements 1 and 3 are correct. Statement 2 is the near-miss: friction and turbine losses mean the plant gives back only about three-quarters of the energy it uses, so it is a store, not a source; it earns its keep by buying cheap surplus power, often solar at midday, and supplying the evening peak. "
  "It is a mature technology, in use for over a century, and India is building many more such projects to firm up renewable power.",
  "कथन 1 और 3 सही हैं। कथन 2 निकट-भ्रम है: घर्षण और टरबाइन हानियों के कारण संयंत्र उपयोग की गई ऊर्जा का केवल लगभग तीन-चौथाई लौटाता है, इसलिए यह भंडार है, स्रोत नहीं; यह सस्ती अतिरिक्त बिजली, प्रायः दोपहर की सौर बिजली, ख़रीदकर और शाम की चरम माँग पूरी करके लाभ कमाता है। "
  "यह एक सदी से अधिक समय से प्रयुक्त परिपक्व प्रौद्योगिकी है, और भारत नवीकरणीय बिजली को स्थिर करने के लिए ऐसी अनेक और परियोजनाएँ बना रहा है।",
  "Central Electricity Authority; Ministry of Power -- guidelines for pumped storage projects.", "en-pumped-storage", craft="precision")

S(EN, "medium", "Consider the following statements about solar power technologies:",
  "सौर ऊर्जा प्रौद्योगिकियों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Bifacial solar panels can capture sunlight on both their front and back surfaces.",
   "On very hot afternoons, silicon solar panels produce less than their rated output, partly because they lose efficiency as they heat up.",
   "Concentrated solar power plants can store heat in molten salt and keep generating after sunset."],
  ["द्विमुखी सौर पैनल अपनी आगे और पीछे दोनों सतहों पर धूप ग्रहण कर सकते हैं।",
   "बहुत गर्म दोपहरों में सिलिकॉन सौर पैनल अपनी निर्धारित क्षमता से कम उत्पादन करते हैं, आंशिक रूप से इसलिए कि गर्म होने पर उनकी दक्षता घटती है।",
   "संकेंद्रित सौर ऊर्जा संयंत्र पिघले लवण में ऊष्मा संचित करके सूर्यास्त के बाद भी बिजली बना सकते हैं।"],
  C3, 2,
  "All three statements are correct. Bifacial panels gain from light reflected off the ground, especially over pale surfaces such as sand. Silicon cells lose roughly 0.4 per cent of their output for each degree above 25 °C, so panels in hot deserts are mounted to let air cool them. "
  "Concentrated solar power uses mirrors to focus sunlight into heat that drives a turbine; because heat is easier to store than electricity, CSP plants can run into the night.",
  "तीनों कथन सही हैं। द्विमुखी पैनल भूमि से परावर्तित प्रकाश से लाभ पाते हैं, विशेषकर रेत जैसी हल्के रंग की सतहों पर। सिलिकॉन सेल 25 °C से ऊपर हर अंश पर अपने उत्पादन का लगभग 0.4 प्रतिशत खोते हैं, इसलिए गर्म रेगिस्तानों में पैनल इस तरह लगाए जाते हैं कि हवा उन्हें ठंडा कर सके। "
  "संकेंद्रित सौर ऊर्जा दर्पणों से सूर्य के प्रकाश को ऊष्मा में केंद्रित करती है जो टरबाइन चलाती है; चूँकि ऊष्मा को बिजली की तुलना में संचित करना आसान है, CSP संयंत्र रात तक चल सकते हैं।",
  MNRE, "en-solar-technologies", craft="linkage")

S(EN, "medium", "Consider the following statements about energy from waste:",
  "कचरे से ऊर्जा के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Many waste-to-energy plants in India struggle because unsegregated municipal waste is wet and has a low calorific value.",
   "Refuse-derived fuel is made from the dry, combustible part of municipal waste.",
   "Cement kilns can use refuse-derived fuel as a partial substitute for coal."],
  ["भारत के अनेक कचरे-से-ऊर्जा संयंत्र इसलिए कठिनाई में हैं क्योंकि बिना छँटा नगरीय कचरा गीला होता है और उसका ऊष्मीय मान कम होता है।",
   "कचरा-व्युत्पन्न ईंधन (RDF) नगरीय कचरे के सूखे, ज्वलनशील भाग से बनता है।",
   "सीमेंट भट्टियाँ RDF को कोयले के आंशिक विकल्प के रूप में उपयोग कर सकती हैं।"],
  C3, 2,
  "All three statements are correct. Indian municipal waste is often more than half wet kitchen and garden waste, which burns poorly; unless waste is segregated at source, plants need extra fuel, run below capacity and draw complaints about emissions. "
  "Refuse-derived fuel -- shredded, dried paper, plastic and textiles -- burns well, and the very high temperatures and long residence times in cement kilns destroy most pollutants, while the ash becomes part of the clinker.",
  "तीनों कथन सही हैं। भारत का नगरीय कचरा प्रायः आधे से अधिक गीला रसोई और बाग़ का कचरा होता है, जो ठीक से नहीं जलता; स्रोत पर छँटाई न होने पर संयंत्रों को अतिरिक्त ईंधन चाहिए होता है, वे क्षमता से कम चलते हैं और उत्सर्जन की शिकायतें होती हैं। "
  "RDF, यानी कतरा और सुखाया गया काग़ज़, प्लास्टिक और कपड़ा, अच्छी तरह जलता है, और सीमेंट भट्टियों का बहुत ऊँचा तापमान और लंबा ठहराव-समय अधिकांश प्रदूषकों को नष्ट कर देता है, जबकि राख क्लिंकर का भाग बन जाती है।",
  "Ministry of Housing and Urban Affairs -- Swachh Bharat Mission (Urban); Central Pollution Control Board.", "en-waste-to-energy-rdf", craft="linkage")

if __name__ == "__main__":
    write_updates("upg_l2_t20_st_a.sql", statuses=("draft", "published"))
