# -*- coding: utf-8 -*-
"""Current Affairs · Test 2 (April to June 2026) -- part A: Current Affairs (international, defence, indices, sports,
awards).

Events of April-June 2026: the postponed fourth India-Africa Forum Summit, the India-Russia logistics agreement, the
SIPRI Yearbook, the India-Italy Special Strategic Partnership, the Navy's new ships and the NASM-SR salvo, the NCRB's
Crime in India 2024, the World Press Freedom Index, Exercises Dustlik and Pragati, the Candidates tournaments, the
Thomas and Uber Cups, the FIFA World Cup, the Vietnamese leader's visit, the Prime Minister's visit to the UAE,
CBSE's three-language rule and the International Booker Prize. Every fact was searched in the whole UPSC bank and is
one no row tests."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2
from ca_common import MX, finish
from ca_t2_format import FORMAT, POS

d.SUBJECT = "Current Affairs"
d.REQUIRE_CRAFT = True
IN, NA, DF, SC, SP = "International", "National", "Defence", "Schemes & Indices", "Sports"

# ================================================================ INTERNATIONAL
S(IN, "medium", "On 21 May 2026 India and the African Union postponed the fourth India-Africa Forum Summit, which was to be held in New Delhi at the end of May. Consider the following statements:",
  "21 मई 2026 को भारत और अफ़्रीकी संघ ने चौथा भारत-अफ़्रीका फ़ोरम शिखर सम्मेलन स्थगित कर दिया, जो मई के अंत में नई दिल्ली में होना था। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The summit was postponed because of the Ebola outbreak in Africa.",
   "The first India-Africa Forum Summit was held in New Delhi in 2008.",
   "The second summit was held in Addis Ababa in 2011."],
  ["शिखर सम्मेलन अफ़्रीका में इबोला प्रकोप के कारण स्थगित हुआ।",
   "पहला भारत-अफ़्रीका फ़ोरम शिखर सम्मेलन 2008 में नई दिल्ली में हुआ था।",
   "दूसरा शिखर सम्मेलन 2011 में अदीस अबाबा में हुआ था।"],
  C3, 2,
  "All three statements are correct. The summit, planned for 28-31 May with meetings of senior officials and foreign ministers before the leaders' session, was put off after India consulted the Chairperson of the African Union and the AU Commission on the Ebola outbreak in the Democratic Republic of the Congo; new dates were to be fixed later. The series began in New Delhi in April 2008, and the third summit, in New Delhi in October 2015, was the first to bring together all 54 African states. "
  "The second summit was held in May 2011 in Addis Ababa, where the African Union has its headquarters.",
  "तीनों कथन सही हैं। 28-31 मई के लिए नियोजित यह शिखर सम्मेलन, जिसमें नेताओं के सत्र से पहले वरिष्ठ अधिकारियों और विदेश मंत्रियों की बैठकें होनी थीं, कांगो लोकतांत्रिक गणराज्य में इबोला प्रकोप पर अफ़्रीकी संघ के अध्यक्ष और एयू आयोग से भारत के परामर्श के बाद टाल दिया गया; नई तिथियाँ बाद में तय होनी थीं। यह शृंखला अप्रैल 2008 में नई दिल्ली से शुरू हुई, और अक्टूबर 2015 में नई दिल्ली में हुआ तीसरा शिखर सम्मेलन सभी 54 अफ़्रीकी देशों को साथ लाने वाला पहला था। "
  "दूसरा शिखर सम्मेलन मई 2011 में अदीस अबाबा में हुआ, जहाँ अफ़्रीकी संघ का मुख्यालय है।",
  "Ministry of External Affairs, press release on the postponement of the fourth India-Africa Forum Summit (21 May 2026) and records of the India-Africa Forum Summits (2008, 2011, 2015).",
  "ca-t2-ca-iafs-iv-postponed-2008-addis-2011", craft="precision")

S(IN, "medium", "In June 2026 attention turned to what the India-Russia Reciprocal Exchange of Logistics Support (RELOS) agreement, in force since early 2026, allows. Consider the following statements:",
  "जून 2026 में इस पर ध्यान गया कि 2026 के आरंभ से लागू भारत-रूस रेसिप्रोकल एक्सचेंज ऑफ़ लॉजिस्टिक्स सपोर्ट (रिलोस) समझौता क्या अनुमति देता है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["It lets each side's forces use the other's ports and airfields for refuelling, repairs and supplies on agreed visits and exercises.",
   "It allows Russian troops to be stationed permanently at Indian bases.",
   "India's first such logistics agreement was the one signed with the United States in 2016."],
  ["यह प्रत्येक पक्ष की सेनाओं को सहमत यात्राओं और अभ्यासों में दूसरे पक्ष के बंदरगाहों और हवाई अड्डों का ईंधन भरने, मरम्मत और आपूर्ति के लिए उपयोग करने देता है।",
   "यह रूसी सैनिकों को भारतीय अड्डों पर स्थायी रूप से तैनात रहने देता है।",
   "भारत का ऐसा पहला लॉजिस्टिक्स समझौता 2016 में संयुक्त राज्य अमेरिका के साथ हुआ था।"],
  C3, 1,
  "Statements 1 and 3 are correct. Signed in Moscow in February 2025 and ratified by Russia in December 2025, RELOS gives the two militaries reciprocal access to ports, airfields, fuel, repair and maintenance, berthing, storage and medical support during agreed deployments, exercises and humanitarian missions, for an initial five years, with limits on the numbers of ships, troops and aircraft at a time. India's first logistics support agreement was the Logistics Exchange Memorandum of Agreement (LEMOA) with the United States in 2016; similar pacts followed with France, Singapore, South Korea, Australia, Japan, the United Kingdom and others. "
  "Statement 2 is wrong: logistics support agreements do not confer basing rights, permanent deployments or any territorial control; every use is by mutual agreement for a specific visit or exercise.",
  "कथन 1 और 3 सही हैं। फ़रवरी 2025 में मॉस्को में हस्ताक्षरित और दिसंबर 2025 में रूस द्वारा अनुसमर्थित रिलोस दोनों सेनाओं को सहमत तैनातियों, अभ्यासों और मानवीय अभियानों के दौरान बंदरगाहों, हवाई अड्डों, ईंधन, मरम्मत और रखरखाव, लंगर, भंडारण और चिकित्सा सहायता तक पारस्परिक पहुँच देता है, आरंभ में पाँच वर्षों के लिए, एक समय में जहाज़ों, सैनिकों और विमानों की संख्या की सीमाओं के साथ। भारत का पहला लॉजिस्टिक्स सहायता समझौता 2016 में संयुक्त राज्य अमेरिका के साथ लॉजिस्टिक्स एक्सचेंज मेमोरेंडम ऑफ़ एग्रीमेंट (लेमोआ) था; फिर फ़्रांस, सिंगापुर, दक्षिण कोरिया, ऑस्ट्रेलिया, जापान, यूनाइटेड किंगडम और अन्य के साथ ऐसे समझौते हुए। "
  "कथन 2 ग़लत है: लॉजिस्टिक्स सहायता समझौते अड्डे के अधिकार, स्थायी तैनाती या कोई क्षेत्रीय नियंत्रण नहीं देते; हर उपयोग किसी विशेष यात्रा या अभ्यास के लिए आपसी सहमति से होता है।",
  "Ministry of Defence, India's logistics support agreements; Ministry of External Affairs, India-Russia Reciprocal Exchange of Logistics Support agreement (signed February 2025).",
  "ca-t2-ca-relos-access-not-basing-lemoa-2016", craft="linkage")

S(IN, "medium", "In June 2026 the Stockholm International Peace Research Institute (SIPRI) released its Yearbook with estimates of nuclear arsenals as of January 2026. Consider the following statements:",
  "जून 2026 में स्टॉकहोम अंतरराष्ट्रीय शांति अनुसंधान संस्थान (सिपरी) ने जनवरी 2026 तक के परमाणु शस्त्रागारों के अनुमानों के साथ अपनी वार्षिकी जारी की। निम्नलिखित कथनों पर विचार कीजिए:",
  ["It estimated that India has more nuclear warheads than Pakistan.",
   "For the first time, it classed some of India's warheads as deployed rather than held in storage.",
   "It estimated that China has fewer nuclear warheads than India."],
  ["इसके अनुमान के अनुसार भारत के पास पाकिस्तान से अधिक परमाणु आयुध हैं।",
   "पहली बार इसने भारत के कुछ आयुधों को भंडार में रखे के बजाय तैनात श्रेणी में रखा।",
   "इसके अनुमान के अनुसार चीन के पास भारत से कम परमाणु आयुध हैं।"],
  C3, 1,
  "Statements 1 and 2 are correct. SIPRI put India's arsenal at about 190 warheads, up from 180 a year earlier, against about 170 for Pakistan, and for the first time counted 12 Indian warheads as deployed -- mounted on missiles or held at bases with operational forces -- a sign of a more ready posture as the land, air and sea legs of India's deterrent mature. "
  "Statement 3 is wrong: China has the fastest-growing arsenal, estimated at about 620 warheads. The nine nuclear-armed states are the United States, Russia, the United Kingdom, France, China, India, Pakistan, North Korea and Israel, together holding about 12,000 warheads.",
  "कथन 1 और 2 सही हैं। सिपरी ने भारत के शस्त्रागार को लगभग 190 आयुधों का आँका, एक वर्ष पहले के 180 से अधिक, जबकि पाकिस्तान के लगभग 170, और पहली बार 12 भारतीय आयुधों को तैनात गिना -- मिसाइलों पर लगे या परिचालन बलों वाले अड्डों पर रखे -- जो भारत के प्रतिरोध के स्थल, वायु और समुद्री अंगों के परिपक्व होने के साथ अधिक तत्पर मुद्रा का संकेत है। "
  "कथन 3 ग़लत है: चीन का शस्त्रागार सबसे तेज़ी से बढ़ रहा है, लगभग 620 आयुधों का अनुमानित। नौ परमाणु-सशस्त्र देश संयुक्त राज्य अमेरिका, रूस, यूनाइटेड किंगडम, फ़्रांस, चीन, भारत, पाकिस्तान, उत्तर कोरिया और इज़रायल हैं, जिनके पास मिलाकर लगभग 12,000 आयुध हैं।",
  "Stockholm International Peace Research Institute, SIPRI Yearbook 2026 (June 2026), chapter on world nuclear forces.",
  "ca-t2-ca-sipri-2026-india-190-deployed-china-620", craft="precision")

S(IN, "medium", "On 20 May 2026 India and Italy raised their relationship to a Special Strategic Partnership during the Prime Minister's visit to Rome. Consider the following statements:",
  "20 मई 2026 को प्रधानमंत्री की रोम यात्रा के दौरान भारत और इटली ने अपने संबंधों को विशेष रणनीतिक साझेदारी तक बढ़ाया। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The two sides follow a Joint Strategic Action Plan for 2025-2029.",
   "Italy is among the signatories of the 2023 memorandum on the India-Middle East-Europe Economic Corridor (IMEC).",
   "IMEC was announced on the sidelines of the G20 summit held in New Delhi in 2023."],
  ["दोनों पक्ष 2025-2029 की एक संयुक्त रणनीतिक कार्ययोजना का अनुसरण करते हैं।",
   "इटली भारत-मध्य पूर्व-यूरोप आर्थिक गलियारे (आईमेक) पर 2023 के समझौता ज्ञापन के हस्ताक्षरकर्ताओं में है।",
   "आईमेक की घोषणा 2023 में नई दिल्ली में हुए जी20 शिखर सम्मेलन के अवसर पर हुई थी।"],
  C3, 2,
  "All three statements are correct. The upgrade builds on the Joint Strategic Action Plan 2025-2029, with defence manufacturing, technology, clean energy, connectivity and security as priorities and a target of raising trade from about €14 billion to €20 billion in three years. Italy signed the IMEC memorandum alongside India, the United States, Saudi Arabia, the UAE, the European Union, France and Germany; the corridor is to link India by sea to the Gulf, by rail across Arabia and onward to Europe. "
  "IMEC was announced on the sidelines of the G20 summit in New Delhi in September 2023; it is often wrongly linked with the G7 summit that Italy hosted in Apulia in 2024, to which India was invited.",
  "तीनों कथन सही हैं। यह उन्नयन संयुक्त रणनीतिक कार्ययोजना 2025-2029 पर आधारित है, जिसकी प्राथमिकताएँ रक्षा विनिर्माण, प्रौद्योगिकी, स्वच्छ ऊर्जा, संपर्क और सुरक्षा हैं, और तीन वर्षों में व्यापार को लगभग 14 अरब यूरो से 20 अरब यूरो तक ले जाने का लक्ष्य है। इटली ने भारत, संयुक्त राज्य अमेरिका, सऊदी अरब, संयुक्त अरब अमीरात, यूरोपीय संघ, फ़्रांस और जर्मनी के साथ आईमेक समझौता ज्ञापन पर हस्ताक्षर किए; गलियारा भारत को समुद्र से खाड़ी, अरब के पार रेल से और आगे यूरोप से जोड़ेगा। "
  "आईमेक की घोषणा सितंबर 2023 में नई दिल्ली में जी20 शिखर सम्मेलन के अवसर पर हुई; इसे अक्सर ग़लती से 2024 में अपूलिया में इटली द्वारा आयोजित जी7 शिखर सम्मेलन से जोड़ा जाता है, जिसमें भारत आमंत्रित था।",
  "Ministry of External Affairs, India-Italy Joint Statement on the Special Strategic Partnership (May 2026) and Joint Strategic Action Plan 2025-2029; MoU on the India-Middle East-Europe Economic Corridor (September 2023).",
  "ca-t2-ca-india-italy-ssp-imec-g20-not-g7", craft="linkage")

S(IN, "medium", "During the state visit of Vietnam's top leader To Lam to India on 5-7 May 2026, the two countries upgraded their ties. Consider the following statements:",
  "5-7 मई 2026 को वियतनाम के शीर्ष नेता तो लाम की भारत की राजकीय यात्रा के दौरान दोनों देशों ने अपने संबंधों का उन्नयन किया। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The two countries raised their ties to an Enhanced Comprehensive Strategic Partnership.",
   "Vietnam joined India's Indo-Pacific Oceans Initiative.",
   "India's Act East Policy, announced in 2014, grew out of the Look East Policy of the early 1990s."],
  ["दोनों देशों ने अपने संबंधों को संवर्धित व्यापक रणनीतिक साझेदारी तक बढ़ाया।",
   "वियतनाम भारत की हिंद-प्रशांत महासागर पहल में शामिल हुआ।",
   "2014 में घोषित भारत की एक्ट ईस्ट नीति 1990 के दशक के आरंभ की लुक ईस्ट नीति से विकसित हुई।"],
  C3, 2,
  "All three statements are correct. Building on the Comprehensive Strategic Partnership of 2016, the leaders upgraded ties, set a trade target of $25 billion by 2030, signed agreements including one between IREL (India) Ltd and Vietnam's rare-earth research institute, discussed defence supplies and maintenance support, and called for freedom of navigation and a binding code of conduct in the South China Sea; Vietnam joined the Indo-Pacific Oceans Initiative that India launched in 2019. "
  "The 'Look East' policy began in the early 1990s under P.V. Narasimha Rao; it was upgraded to the 'Act East' Policy, with a sharper strategic and security edge, in 2014, announced at the ASEAN-India and East Asia summits in Naypyidaw.",
  "तीनों कथन सही हैं। 2016 की व्यापक रणनीतिक साझेदारी पर आगे बढ़ते हुए नेताओं ने संबंधों का उन्नयन किया, 2030 तक 25 अरब डॉलर के व्यापार का लक्ष्य रखा, आईआरईएल (इंडिया) लिमिटेड और वियतनाम के दुर्लभ मृदा अनुसंधान संस्थान के बीच समझौते सहित कई समझौते किए, रक्षा आपूर्ति और रखरखाव सहायता पर चर्चा की, और दक्षिण चीन सागर में नौवहन की स्वतंत्रता तथा बाध्यकारी आचार संहिता की माँग की; वियतनाम 2019 में भारत द्वारा शुरू की गई हिंद-प्रशांत महासागर पहल में शामिल हुआ। "
  "‘लुक ईस्ट’ नीति 1990 के दशक के आरंभ में पी.वी. नरसिंह राव के समय शुरू हुई; इसे अधिक धारदार रणनीतिक और सुरक्षा पक्ष के साथ 2014 में ‘एक्ट ईस्ट’ नीति में बदला गया, जिसकी घोषणा नेपीडॉ में आसियान-भारत और पूर्वी एशिया शिखर सम्मेलनों में हुई।",
  "Ministry of External Affairs, India-Vietnam Joint Statement (6 May 2026); President's Secretariat, banquet for the President of Viet Nam (May 2026).",
  "ca-t2-ca-vietnam-enhanced-csp-ipoi-act-east-2014", craft="linkage")

S(IN, "medium", "On 15 May 2026 India and the United Arab Emirates signed several agreements during the Prime Minister's visit to Abu Dhabi. Consider the following statements:",
  "15 मई 2026 को प्रधानमंत्री की अबू धाबी यात्रा के दौरान भारत और संयुक्त अरब अमीरात ने कई समझौतों पर हस्ताक्षर किए। निम्नलिखित कथनों पर विचार कीजिए:",
  ["They agreed to set up a ship-repair cluster at Vizhinjam in Kerala.",
   "They agreed on a framework for a Strategic Defence Partnership.",
   "They signed a memorandum of understanding on strategic petroleum reserves."],
  ["वे केरल के विझिंजम में जहाज़-मरम्मत क्लस्टर स्थापित करने पर सहमत हुए।",
   "वे एक रणनीतिक रक्षा साझेदारी के ढाँचे पर सहमत हुए।",
   "उन्होंने रणनीतिक पेट्रोलियम भंडार पर एक समझौता ज्ञापन पर हस्ताक्षर किए।"],
  C3, 1,
  "Statements 2 and 3 are correct. With Gulf supplies disrupted by the West Asian conflict, the visit produced a framework for a Strategic Defence Partnership -- covering defence production, exercises, maritime security and cyber defence -- an MoU on strategic petroleum reserves and an agreement on LPG supply, a ship-repair cluster and about $5 billion of UAE investment in India. "
  "Statement 1 is wrong: the ship-repair cluster is to come up at Vadinar in Gujarat, on the Gulf of Kachchh near the Jamnagar refining hub; Vizhinjam in Kerala is India's deep-water container transhipment port. The UAE is also India's partner, with Israel and the United States, in the I2U2 grouping formed in 2022.",
  "कथन 2 और 3 सही हैं। पश्चिम एशियाई संघर्ष से खाड़ी की आपूर्ति बाधित होने के बीच इस यात्रा से रणनीतिक रक्षा साझेदारी का एक ढाँचा -- रक्षा उत्पादन, अभ्यास, समुद्री सुरक्षा और साइबर रक्षा को समेटते हुए -- रणनीतिक पेट्रोलियम भंडार पर समझौता ज्ञापन और एलपीजी आपूर्ति पर समझौता, जहाज़-मरम्मत क्लस्टर और भारत में लगभग 5 अरब डॉलर का यूएई निवेश निकला। "
  "कथन 1 ग़लत है: जहाज़-मरम्मत क्लस्टर गुजरात में कच्छ की खाड़ी पर जामनगर रिफ़ाइनिंग केंद्र के पास वाडिनार में बनना है; केरल का विझिंजम भारत का गहरे पानी का कंटेनर ट्रांसशिपमेंट बंदरगाह है। संयुक्त अरब अमीरात इज़रायल और संयुक्त राज्य अमेरिका के साथ 2022 में बने आई2यू2 समूह में भी भारत का साझेदार है।",
  "Ministry of External Affairs, list of outcomes of the Prime Minister's visit to the UAE (15 May 2026).",
  "ca-t2-ca-india-uae-defence-framework-spr-vadinar", craft="precision")

# ================================================================ DEFENCE
MX(DF, "medium", "In April-June 2026 the Indian Navy added several vessels to its fleet. Match List-I (vessel) with List-II (type of vessel):",
   "अप्रैल-जून 2026 में भारतीय नौसेना ने अपने बेड़े में कई पोत जोड़े। सूची-I (पोत) का सूची-II (पोत का प्रकार) से मिलान कीजिए:",
   ["INS Aridhaman", "INS Dunagiri", "INS Sanshodhak", "INS Agray"],
   ["आईएनएस अरिधमन", "आईएनएस दूनागिरि", "आईएनएस संशोधक", "आईएनएस अग्रय"],
   ["Anti-submarine warfare shallow water craft", "Nuclear-powered ballistic missile submarine", "Stealth frigate of Project 17A", "Large survey vessel"],
   ["पनडुब्बी-रोधी युद्ध हेतु उथले जल का पोत", "परमाणु-चालित बैलिस्टिक मिसाइल पनडुब्बी", "प्रोजेक्ट 17ए का स्टेल्थ फ़्रिगेट", "बड़ा सर्वेक्षण पोत"],
   (2, 3, 4, 1), POS.get("ca-t2-ca-navy-vessels-aridhaman-dunagiri-sanshodhak-agray", 3),
   "The correct code is A-2, B-3, C-4, D-1. INS Aridhaman, commissioned in April 2026, is the third Arihant-class nuclear-powered ballistic missile submarine (SSBN), after Arihant (2016) and Arighaat (2024), with more missile tubes than her sisters; SSBNs give the sea leg of India's nuclear triad. On 21 June 2026 three ships built by Garden Reach Shipbuilders and Engineers were commissioned together at Kolkata: Dunagiri, the fifth Nilgiri-class (Project 17A) stealth frigate; Sanshodhak, a Sandhayak-class large survey vessel for hydrographic work; and Agray, an Arnala-class anti-submarine warfare shallow water craft. "
   "The names give hints -- 'Sanshodhak' means researcher, and frigates of Project 17A are named after hill ranges -- which is how a candidate can reason through such a match.",
   "सही कूट A-2, B-3, C-4, D-1 है। अप्रैल 2026 में कमीशन हुआ आईएनएस अरिधमन अरिहंत (2016) और अरिघात (2024) के बाद तीसरी अरिहंत-श्रेणी की परमाणु-चालित बैलिस्टिक मिसाइल पनडुब्बी (एसएसबीएन) है, जिसमें अपनी पूर्ववर्ती पनडुब्बियों से अधिक मिसाइल-नलिकाएँ हैं; एसएसबीएन भारत के परमाणु त्रिक का समुद्री अंग हैं। 21 जून 2026 को गार्डन रीच शिपबिल्डर्स एंड इंजीनियर्स द्वारा निर्मित तीन जहाज़ कोलकाता में एक साथ कमीशन हुए: दूनागिरि, पाँचवाँ नीलगिरि-श्रेणी (प्रोजेक्ट 17ए) स्टेल्थ फ़्रिगेट; संशोधक, जल-सर्वेक्षण के लिए संधायक-श्रेणी का बड़ा सर्वेक्षण पोत; और अग्रय, अर्नाला-श्रेणी का पनडुब्बी-रोधी युद्ध हेतु उथले जल का पोत। "
   "नाम संकेत देते हैं -- ‘संशोधक’ का अर्थ शोधकर्ता है, और प्रोजेक्ट 17ए के फ़्रिगेट पर्वत-श्रेणियों के नाम पर रखे जाते हैं -- इस तरह अभ्यर्थी ऐसे मिलान को तर्क से हल कर सकता है।",
   "Ministry of Defence and Indian Navy, commissioning of INS Dunagiri, INS Sanshodhak and INS Agray at Kolkata (21 June 2026); Indian Navy, Arihant-class submarines.",
   "ca-t2-ca-navy-vessels-aridhaman-dunagiri-sanshodhak-agray", "precision")

M(DF, "medium",
  "In May 2026 the Indian Navy and DRDO carried out the first salvo launch of the NASM-SR. The NASM-SR is:",
  "मई 2026 में भारतीय नौसेना और डीआरडीओ ने एनएएसएम-एसआर का पहला साल्वो प्रक्षेपण किया। एनएएसएम-एसआर है:",
  ["a short-range anti-ship missile fired from a naval helicopter",
   "a submarine-launched ballistic missile of the K series",
   "a long-range surface-to-air missile developed with Israel",
   "a ramjet-powered beyond-visual-range air-to-air missile for fighters"],
  ["नौसैनिक हेलीकॉप्टर से दागी जाने वाली कम दूरी की जहाज़-रोधी मिसाइल",
   "के-शृंखला की पनडुब्बी से प्रक्षेपित बैलिस्टिक मिसाइल",
   "इज़रायल के साथ विकसित लंबी दूरी की सतह-से-हवा मिसाइल",
   "लड़ाकू विमानों के लिए रैमजेट-चालित, दृष्टि-सीमा से परे मार करने वाली हवा-से-हवा मिसाइल"],
  0,
  "The NASM-SR (Naval Anti-Ship Missile - Short Range) is an indigenous missile developed by DRDO for the Navy's helicopters, with a solid-propellant booster and a long-burning sustainer; in early May 2026 two were fired in quick succession from a helicopter over the Bay of Bengal off Odisha, showing that a single platform can launch a salvo to saturate a ship's defences. "
  "The other options describe different systems: the K-series (K-15, K-4) are submarine-launched ballistic missiles for the Arihant-class boats; the long-range surface-to-air missile developed with Israel is the Barak-8 (MRSAM/LRSAM) family; and the ramjet-powered air-to-air missile is the Astra Mk III, which uses solid-fuel ducted ramjet technology.",
  "एनएएसएम-एसआर (नेवल एंटी-शिप मिसाइल - शॉर्ट रेंज) डीआरडीओ द्वारा नौसेना के हेलीकॉप्टरों के लिए विकसित स्वदेशी मिसाइल है, जिसमें ठोस-नोदक बूस्टर और देर तक जलने वाला सस्टेनर है; मई 2026 के आरंभ में ओडिशा तट के पास बंगाल की खाड़ी के ऊपर एक हेलीकॉप्टर से दो मिसाइलें तेज़ी से एक के बाद एक दागी गईं, जिससे दिखा कि एक ही मंच किसी जहाज़ की सुरक्षा को पस्त करने के लिए साल्वो छोड़ सकता है। "
  "अन्य विकल्प भिन्न प्रणालियाँ बताते हैं: के-शृंखला (के-15, के-4) अरिहंत-श्रेणी की पनडुब्बियों के लिए पनडुब्बी-प्रक्षेपित बैलिस्टिक मिसाइलें हैं; इज़रायल के साथ विकसित लंबी दूरी की सतह-से-हवा मिसाइल बराक-8 (एमआरएसएएम/एलआरएसएएम) परिवार है; और रैमजेट-चालित हवा-से-हवा मिसाइल अस्त्र एमके III है, जो ठोस-ईंधन डक्टेड रैमजेट प्रौद्योगिकी का उपयोग करती है।",
  "Ministry of Defence and PIB, maiden salvo launch of NASM-SR from a naval helicopter (May 2026); Defence Research and Development Organisation, missile programmes.",
  "ca-t2-ca-nasm-sr-salvo-helicopter", pos=POS.get("ca-t2-ca-nasm-sr-salvo-helicopter", 0), craft="precision")

S(DF, "medium", "In April-May 2026 the Indian Army took part in Exercise Dustlik abroad and hosted Exercise Pragati at home. Consider the following statements:",
  "अप्रैल-मई 2026 में भारतीय सेना ने विदेश में अभ्यास दुस्तलिक में भाग लिया और देश में अभ्यास प्रगति की मेज़बानी की। निम्नलिखित कथनों पर विचार कीजिए:",
  ["Dustlik is India's joint military exercise with Kazakhstan.",
   "Pragati 2026, held in Meghalaya, brought together the Indian Army and troops from twelve friendly countries.",
   "Bangladesh was among the countries taking part in Pragati 2026."],
  ["दुस्तलिक कज़ाख़स्तान के साथ भारत का संयुक्त सैन्य अभ्यास है।",
   "मेघालय में हुआ प्रगति 2026 भारतीय सेना और बारह मित्र देशों की सेनाओं को साथ लाया।",
   "बांग्लादेश प्रगति 2026 में भाग लेने वाले देशों में था।"],
  C3, 0,
  "Only statement 2 is correct. Statement 1 is wrong: Dustlik ('friendship' in Uzbek) is India's exercise with Uzbekistan, not with Kazakhstan, with which India holds KAZIND; its 2026 edition was held at Gurumsaray in Uzbekistan's Namangan region in April, focusing on joint operations against unlawful armed groups in semi-mountainous terrain. Pragati 2026, a multinational exercise hosted at Umroi in Meghalaya from 20 May, trained troops of Bhutan, Cambodia, Indonesia, Laos, Malaysia, the Maldives, Myanmar, Nepal, the Philippines, Seychelles, Sri Lanka and Vietnam with the Indian Army in counter-terrorism in jungle and hill terrain. "
  "Statement 3 is wrong: Bangladesh was not among the twelve participants.",
  "केवल कथन 2 सही है। कथन 1 ग़लत है: दुस्तलिक (उज़्बेक में ‘मित्रता’) उज़्बेकिस्तान के साथ भारत का अभ्यास है, कज़ाख़स्तान के साथ नहीं, जिसके साथ भारत काज़िंद करता है; इसका 2026 संस्करण अप्रैल में उज़्बेकिस्तान के नमनगान क्षेत्र के गुरुमसराय में हुआ, जिसमें अर्ध-पर्वतीय भूभाग में अवैध सशस्त्र समूहों के विरुद्ध संयुक्त अभियानों पर ध्यान था। 20 मई से मेघालय के उमरोई में आयोजित बहुराष्ट्रीय अभ्यास प्रगति 2026 ने भूटान, कंबोडिया, इंडोनेशिया, लाओस, मलेशिया, मालदीव, म्यांमार, नेपाल, फ़िलीपींस, सेशेल्स, श्रीलंका और वियतनाम की सेनाओं को भारतीय सेना के साथ जंगल और पहाड़ी भूभाग में आतंकवाद-रोधी अभियानों का प्रशिक्षण दिया। "
  "कथन 3 ग़लत है: बांग्लादेश बारह प्रतिभागियों में नहीं था।",
  "Ministry of Defence and PIB, Exercise Dustlik 2026 (April 2026) and Exercise Pragati 2026 (May 2026).",
  "ca-t2-ca-exercises-dustlik-uzbekistan-pragati-12", craft="precision")

# ================================================================ INDICES, SPORTS, AWARDS
S(SC, "easy", "On 30 April 2026 the World Press Freedom Index 2026 was released. Consider the following statements:",
  "30 अप्रैल 2026 को विश्व प्रेस स्वतंत्रता सूचकांक 2026 जारी हुआ। निम्नलिखित कथनों पर विचार कीजिए:",
  ["India was ranked 157th of 180 countries, lower than in 2025.",
   "The index is compiled by UNESCO."],
  ["भारत को 180 देशों में 157वाँ स्थान मिला, जो 2025 से नीचे है।",
   "यह सूचकांक यूनेस्को संकलित करता है।"],
  T2, 0,
  "Only statement 1 is correct. India fell from 151st in 2025 to 157th, in the 'very serious' category, with the publisher pointing to violence against journalists, the concentration of media ownership and the political alignment of outlets. "
  "Statement 2 is wrong: the index is compiled by Reporters Without Borders (RSF), a non-governmental organisation based in Paris, from a survey of journalists and experts and counts of abuses; UNESCO, for its part, leads the UN's work on the safety of journalists and marks World Press Freedom Day on 3 May.",
  "केवल कथन 1 सही है। भारत 2025 के 151वें से गिरकर 157वें स्थान पर आया, ‘अत्यंत गंभीर’ श्रेणी में, और प्रकाशक ने पत्रकारों के विरुद्ध हिंसा, मीडिया स्वामित्व के संकेंद्रण और माध्यमों के राजनीतिक झुकाव की ओर इशारा किया। "
  "कथन 2 ग़लत है: सूचकांक पेरिस स्थित ग़ैर-सरकारी संगठन रिपोर्टर्स विदाउट बॉर्डर्स (आरएसएफ़) पत्रकारों और विशेषज्ञों के सर्वेक्षण और उत्पीड़न के मामलों की गणना से संकलित करता है; यूनेस्को संयुक्त राष्ट्र में पत्रकारों की सुरक्षा का कार्य संभालता है और 3 मई को विश्व प्रेस स्वतंत्रता दिवस मनाता है।",
  "Reporters Without Borders, World Press Freedom Index 2026 (30 April 2026); UNESCO, World Press Freedom Day.",
  "ca-t2-ca-press-freedom-index-157-rsf-not-unesco", craft="precision")

S(SP, "medium", "The FIDE Candidates tournaments of 2026 were held in Cyprus from late March to mid-April. Consider the following statements:",
  "2026 के फ़िडे कैंडिडेट्स टूर्नामेंट मार्च के अंत से अप्रैल के मध्य तक साइप्रस में हुए। निम्नलिखित कथनों पर विचार कीजिए:",
  ["R. Vaishali became the first Indian woman to win the Women's Candidates tournament.",
   "The open Candidates tournament was won by an Indian player.",
   "The winner of the open tournament earned the right to challenge D. Gukesh, the reigning world champion."],
  ["आर. वैशाली महिला कैंडिडेट्स टूर्नामेंट जीतने वाली पहली भारतीय महिला बनीं।",
   "ओपन कैंडिडेट्स टूर्नामेंट एक भारतीय खिलाड़ी ने जीता।",
   "ओपन टूर्नामेंट के विजेता ने वर्तमान विश्व चैंपियन डी. गुकेश को चुनौती देने का अधिकार पाया।"],
  C3, 1,
  "Statements 1 and 3 are correct. Vaishali Rameshbabu won the Women's Candidates and so meets the women's world champion in a title match. The open Candidates was won by Javokhir Sindarov of Uzbekistan with 10 points from 14 games, a record score for the event; he plays Gukesh, who became the youngest undisputed world champion in December 2024, for the title. "
  "Statement 2 is wrong: the open event was won by the Uzbek player, not by an Indian.",
  "कथन 1 और 3 सही हैं। वैशाली रमेशबाबू ने महिला कैंडिडेट्स जीता और इस तरह खिताबी मुक़ाबले में महिला विश्व चैंपियन से भिड़ेंगी। ओपन कैंडिडेट्स उज़्बेकिस्तान के जावोखिर सिंदारोव ने 14 खेलों में 10 अंकों के साथ जीता, जो इस प्रतियोगिता का रिकॉर्ड स्कोर है; वे खिताब के लिए गुकेश से खेलेंगे, जो दिसंबर 2024 में सबसे कम उम्र के निर्विवाद विश्व चैंपियन बने। "
  "कथन 2 ग़लत है: ओपन प्रतियोगिता उज़्बेक खिलाड़ी ने जीती, किसी भारतीय ने नहीं।",
  "International Chess Federation (FIDE), Candidates Tournament and Women's Candidates Tournament 2026 (Cyprus, March-April 2026); Ministry of Youth Affairs and Sports, congratulatory releases.",
  "ca-t2-ca-candidates-2026-vaishali-sindarov-gukesh", craft="precision")

S(SP, "easy", "The Thomas and Uber Cup Finals, badminton's world team championships, were held at Horsens in Denmark from 24 April to 3 May 2026. Consider the following statements:",
  "बैडमिंटन की विश्व टीम चैंपियनशिप, थॉमस और उबेर कप फ़ाइनल्स, 24 अप्रैल से 3 मई 2026 तक डेनमार्क के हॉर्सेंस में हुए। निम्नलिखित कथनों पर विचार कीजिए:",
  ["China won the Thomas Cup in 2026.",
   "The Uber Cup is the men's team championship."],
  ["2026 में चीन ने थॉमस कप जीता।",
   "उबेर कप पुरुषों की टीम चैंपियनशिप है।"],
  T2, 0,
  "Only statement 1 is correct. China beat France 3-1 in the final of the Thomas Cup; India, champions for the first time in 2022, lost to France in the semi-final. "
  "Statement 2 is wrong: the Thomas Cup is the men's world team championship and the Uber Cup the women's; South Korea won the 2026 Uber Cup, beating China 3-1 for their third title.",
  "केवल कथन 1 सही है। थॉमस कप के फ़ाइनल में चीन ने फ़्रांस को 3-1 से हराया; 2022 में पहली बार चैंपियन बना भारत सेमीफ़ाइनल में फ़्रांस से हार गया। "
  "कथन 2 ग़लत है: थॉमस कप पुरुषों और उबेर कप महिलाओं की विश्व टीम चैंपियनशिप है; 2026 का उबेर कप दक्षिण कोरिया ने चीन को 3-1 से हराकर अपने तीसरे खिताब के रूप में जीता।",
  "Badminton World Federation, Thomas and Uber Cup Finals 2026 (Horsens); Ministry of Youth Affairs and Sports.",
  "ca-t2-ca-thomas-cup-2026-china-uber-women", craft="precision")

S(SP, "easy", "The FIFA World Cup 2026 began on 11 June 2026. Consider the following statements:",
  "फ़ीफ़ा विश्व कप 2026 11 जून 2026 को शुरू हुआ। निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is the first World Cup with 48 teams.",
   "It is the first World Cup hosted jointly by three countries.",
   "Its opening match was played in Mexico City."],
  ["यह 48 टीमों वाला पहला विश्व कप है।",
   "यह तीन देशों द्वारा संयुक्त रूप से आयोजित पहला विश्व कप है।",
   "इसका उद्घाटन मैच मेक्सिको सिटी में खेला गया।"],
  C3, 2,
  "All three statements are correct. The tournament grew from 32 to 48 teams and from 64 to 104 matches, played across the United States, Canada and Mexico -- the first time three nations have shared the hosting. The opening match was played at the Estadio Azteca in Mexico City on 11 June, making it the first stadium to stage matches at three World Cups (1970, 1986 and 2026); the final is on 19 July in New Jersey.",
  "तीनों कथन सही हैं। प्रतियोगिता 32 से 48 टीमों और 64 से 104 मैचों तक बढ़ी, जो संयुक्त राज्य अमेरिका, कनाडा और मेक्सिको में खेले गए -- पहली बार तीन देशों ने मेज़बानी साझा की। उद्घाटन मैच 11 जून को मेक्सिको सिटी के एस्टाडियो एज़्टेका में खेला गया, जो तीन विश्व कपों (1970, 1986 और 2026) के मैच आयोजित करने वाला पहला स्टेडियम बना; फ़ाइनल 19 जुलाई को न्यू जर्सी में है।",
  "Fédération Internationale de Football Association (FIFA), FIFA World Cup 26: format, hosts and match schedule.",
  "ca-t2-ca-fifa-2026-48-teams-three-hosts-azteca", craft="precision")

S(SC, "medium", "On 19 May 2026 the International Booker Prize was awarded to 'Taiwan Travelogue' by Yáng Shuāng-zǐ, translated by Lin King. Consider the following statements:",
  "19 मई 2026 को अंतरराष्ट्रीय बुकर पुरस्कार यांग शुआंग-ज़ी की ‘ताइवान ट्रैवलॉग’ को दिया गया, जिसका अनुवाद लिन किंग ने किया। निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is the first book written in Mandarin Chinese to win the prize.",
   "The entire prize money goes to the author.",
   "The 2025 prize was won by a novel translated from Hindi."],
  ["यह पुरस्कार जीतने वाली मंदारिन चीनी में लिखी पहली पुस्तक है।",
   "पूरी पुरस्कार राशि लेखक को मिलती है।",
   "2025 का पुरस्कार हिंदी से अनूदित एक उपन्यास ने जीता था।"],
  C3, 0,
  "Only statement 1 is correct: 'Taiwan Travelogue' is the first winner written in Mandarin Chinese. Statement 2 is wrong: the International Booker, for a work of fiction translated into English and published in the UK or Ireland, carries £50,000 divided equally between author and translator, recognising translation as a creative act. "
  "Statement 3 is wrong: the 2025 prize went to 'Heart Lamp', a collection of short stories by Banu Mushtaq translated from Kannada by Deepa Bhasthi -- the first Kannada book and the first short-story collection to win; in 2022 Geetanjali Shree's 'Tomb of Sand', translated from Hindi by Daisy Rockwell, became the first Indian-language winner.",
  "केवल कथन 1 सही है: ‘ताइवान ट्रैवलॉग’ मंदारिन चीनी में लिखी पहली विजेता कृति है। कथन 2 ग़लत है: अंग्रेज़ी में अनूदित और यूके या आयरलैंड में प्रकाशित कथा-कृति के लिए दिया जाने वाला अंतरराष्ट्रीय बुकर 50,000 पाउंड का है, जो अनुवाद को रचनात्मक कर्म मानते हुए लेखक और अनुवादक में बराबर बँटता है। "
  "कथन 3 ग़लत है: 2025 का पुरस्कार बानू मुश्ताक की लघु कहानियों के संग्रह ‘हार्ट लैंप’ को मिला, जिसका कन्नड़ से अनुवाद दीपा भष्टी ने किया -- पुरस्कार जीतने वाली पहली कन्नड़ पुस्तक और पहला कहानी-संग्रह; 2022 में गीतांजलि श्री का ‘टूम ऑफ़ सैंड’, जिसका हिंदी से अनुवाद डेज़ी रॉकवेल ने किया, पहली भारतीय भाषा की विजेता कृति बना था।",
  "The Booker Prize Foundation, International Booker Prize 2026, 2025 and 2022 winners.",
  "ca-t2-ca-international-booker-2026-mandarin-heart-lamp", craft="linkage")

# ================================================================ NATIONAL
S(NA, "medium", "In May 2026 the National Crime Records Bureau released 'Crime in India 2024', which showed a fall of about 6 per cent in registered cognisable crimes and a rise of about 17 per cent in cybercrime. Consider the following statements:",
  "मई 2026 में राष्ट्रीय अपराध रिकॉर्ड ब्यूरो ने ‘भारत में अपराध 2024’ जारी किया, जिसमें दर्ज संज्ञेय अपराधों में लगभग 6 प्रतिशत की कमी और साइबर अपराध में लगभग 17 प्रतिशत की वृद्धि दिखी। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The National Crime Records Bureau functions under the Ministry of Statistics and Programme Implementation.",
   "Part of the fall was attributed to the Bharatiya Nyaya Sanhita making simple hurt a non-cognisable offence.",
   "The Bureau's tables count every offence named in a First Information Report as a separate crime."],
  ["राष्ट्रीय अपराध रिकॉर्ड ब्यूरो सांख्यिकी और कार्यक्रम कार्यान्वयन मंत्रालय के अधीन कार्य करता है।",
   "कमी का एक भाग भारतीय न्याय संहिता द्वारा साधारण चोट को असंज्ञेय अपराध बनाए जाने को दिया गया।",
   "ब्यूरो की तालिकाएँ प्रथम सूचना रिपोर्ट में उल्लिखित हर अपराध को अलग अपराध गिनती हैं।"],
  C3, 0,
  "Only statement 2 is correct. Statement 1 is wrong: set up in 1986 under the Ministry of Home Affairs, not the statistics ministry, the Bureau publishes Crime in India, Accidental Deaths and Suicides in India and Prison Statistics India, and runs national databases such as the crime and criminal tracking network. Registered cognisable crimes fell from about 62.4 lakh in 2023 to about 58.9 lakh in 2024, but much of the drop reflects definitions: under the new code simple hurt became non-cognisable, so fewer such cases are registered as FIRs. Crimes against children and senior citizens and cybercrime, mostly fraud, rose. "
  "Statement 3 is wrong: the Bureau follows the 'principal offence rule' -- where an FIR names several offences, only the most serious is counted -- which is one reason its figures understate the number of offences committed.",
  "केवल कथन 2 सही है। कथन 1 ग़लत है: सांख्यिकी मंत्रालय के नहीं, 1986 में गृह मंत्रालय के अधीन स्थापित ब्यूरो भारत में अपराध, भारत में आकस्मिक मृत्यु और आत्महत्या तथा भारत के कारागार आँकड़े प्रकाशित करता है, और अपराध एवं अपराधी ट्रैकिंग नेटवर्क जैसे राष्ट्रीय डेटाबेस चलाता है। दर्ज संज्ञेय अपराध 2023 के लगभग 62.4 लाख से घटकर 2024 में लगभग 58.9 लाख रह गए, पर इस कमी का बड़ा भाग परिभाषाओं को दर्शाता है: नई संहिता में साधारण चोट असंज्ञेय हो गई, इसलिए ऐसे कम मामले प्राथमिकी के रूप में दर्ज होते हैं। बच्चों और वरिष्ठ नागरिकों के विरुद्ध अपराध तथा साइबर अपराध, मुख्यतः धोखाधड़ी, बढ़े। "
  "कथन 3 ग़लत है: ब्यूरो ‘मुख्य अपराध नियम’ का पालन करता है -- जहाँ किसी प्राथमिकी में कई अपराध हों, केवल सबसे गंभीर गिना जाता है -- यह एक कारण है कि उसके आँकड़े किए गए अपराधों की संख्या को कम दर्शाते हैं।",
  "National Crime Records Bureau, Crime in India 2024 (May 2026), including its note on methodology; Ministry of Home Affairs.",
  "ca-t2-ca-ncrb-2024-bns-simple-hurt-principal-offence", craft="inference")

S(NA, "medium", "A circular of the Central Board of Secondary Education (CBSE) issued in May 2026 made the study of three languages compulsory in Class IX from 1 July 2026. Consider the following statements:",
  "मई 2026 में जारी केंद्रीय माध्यमिक शिक्षा बोर्ड (सीबीएसई) के एक परिपत्र ने 1 जुलाई 2026 से कक्षा IX में तीन भाषाओं का अध्ययन अनिवार्य कर दिया। निम्नलिखित कथनों पर विचार कीजिए:",
  ["At least two of the three languages must be native Indian languages.",
   "The third language is to be assessed by the school rather than in the Class X board examination.",
   "The three-language formula was part of the National Policy on Education, 1968."],
  ["तीन भाषाओं में से कम से कम दो मूल भारतीय भाषाएँ होनी चाहिए।",
   "तीसरी भाषा का मूल्यांकन कक्षा X की बोर्ड परीक्षा के बजाय विद्यालय करेगा।",
   "त्रिभाषा सूत्र राष्ट्रीय शिक्षा नीति, 1968 का अंग था।"],
  C3, 2,
  "All three statements are correct. Following NEP 2020 and the National Curriculum Framework for School Education, 2023, the circular requires three languages (R1, R2, R3), at least two native to India, and treats English as a foreign language; the third language is assessed internally by schools, and passing it is needed for the Class X certificate. Petitions against the rule were taken up by the Supreme Court. "
  "The three-language formula goes back to the National Policy on Education of 1968, which followed the Education Commission headed by D.S. Kothari (1964-66); NEP 2020 kept the formula but gave States and students more flexibility in choosing the languages.",
  "तीनों कथन सही हैं। राष्ट्रीय शिक्षा नीति 2020 और विद्यालयी शिक्षा के राष्ट्रीय पाठ्यचर्या ढाँचे, 2023 के अनुसरण में परिपत्र तीन भाषाएँ (आर1, आर2, आर3) अनिवार्य करता है, जिनमें कम से कम दो भारत की मूल भाषाएँ हों, और अंग्रेज़ी को विदेशी भाषा मानता है; तीसरी भाषा का मूल्यांकन विद्यालय आंतरिक रूप से करते हैं, और कक्षा X का प्रमाणपत्र पाने के लिए उसमें उत्तीर्ण होना आवश्यक है। नियम के विरुद्ध याचिकाओं पर सर्वोच्च न्यायालय ने सुनवाई की। "
  "त्रिभाषा सूत्र 1968 की राष्ट्रीय शिक्षा नीति से चला आ रहा है, जो डी.एस. कोठारी की अध्यक्षता वाले शिक्षा आयोग (1964-66) के बाद आई; राष्ट्रीय शिक्षा नीति 2020 ने सूत्र बनाए रखा पर राज्यों और विद्यार्थियों को भाषाएँ चुनने में अधिक लचीलापन दिया।",
  "Central Board of Secondary Education, circular on the study of three languages in Class IX (May 2026); Ministry of Education, National Education Policy 2020 and National Policy on Education, 1968.",
  "ca-t2-ca-cbse-three-languages-npe-1968", craft="linkage")

finish("ca_t2_a.sql", FORMAT, "2026-Q2", update="--update" in sys.argv)
