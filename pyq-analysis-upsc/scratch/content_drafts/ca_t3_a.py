# -*- coding: utf-8 -*-
"""Current Affairs · Test 3 (July to September 2026) -- part A: international affairs, defence and sports.

Framed as the 2025-26 papers frame current affairs: each item names the grouping, treaty, institution or event and
tests what it is, why it exists and where the wording misleads -- BRICS under India's chair, the SCO at 25, India and
Japan (and the 1951 peace treaty India stayed out of), the 'enemy state' clauses of the UN Charter, Resolution 1373
twenty-five years after 9/11, the CTBT at 30, AUKUS at 5, the Gujral Doctrine at 30, the boundary talks with China, the
Refugee Convention at 75, the quarter's exercises, the seats of international bodies, Javelin, the DAC, cross-border
payment systems, the Commonwealth Games, two world cups, Khelo India, the Magsaysay Award and the Dirac Medal. No stem
carries a date (design doc, section 7). Every fact was searched in the whole UPSC bank and is one no row tests."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2
from ca_common import MX, finish
from ca_t3_format import FORMAT, POS

d.SUBJECT = "Current Affairs"
d.REQUIRE_CRAFT = True
IN, NA, DF, SC, SP = "International", "National", "Defence", "Schemes & Indices", "Sports"

S(IN, "medium", "India chaired BRICS in 2026 and hosted its summit in New Delhi. Consider the following statements:",
  "भारत ने 2026 में ब्रिक्स की अध्यक्षता की और नई दिल्ली में इसके शिखर सम्मेलन की मेज़बानी की। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The theme of India's chairship was framed so that its initials spell BRICS.",
   "This was the third time that India chaired BRICS.",
   "BRICS has a permanent secretariat in Shanghai."],
  ["भारत की अध्यक्षता का विषय इस प्रकार रखा गया कि उसके आद्याक्षर BRICS बनें।",
   "यह तीसरी बार था जब भारत ने ब्रिक्स की अध्यक्षता की।",
   "ब्रिक्स का शंघाई में एक स्थायी सचिवालय है।"],
  C3, 0,
  "Only statement 1 is correct. The theme, 'Building for Resilience, Innovation, Cooperation and Sustainability', spells the group's name, and the summit adopted the New Delhi Declaration by consensus; China takes the chair next. "
  "Statement 2 is wrong: India chaired BRICS in 2012, 2016 and 2021 as well, so 2026 was its fourth turn. Statement 3 is wrong: BRICS has no permanent secretariat -- the rotating chair runs its work, which is one reason its outcomes depend so much on the host's priorities. What sits in Shanghai is the New Development Bank, which the BRICS countries set up but which is a separate institution with its own members.",
  "केवल कथन 1 सही है। विषय, ‘बिल्डिंग फ़ॉर रेज़िलिएंस, इनोवेशन, कोऑपरेशन एंड सस्टेनेबिलिटी’, समूह का नाम बनाता है, और शिखर सम्मेलन ने सर्वसम्मति से नई दिल्ली घोषणा अपनाई; अगली अध्यक्षता चीन की है। "
  "कथन 2 ग़लत है: भारत ने 2012, 2016 और 2021 में भी ब्रिक्स की अध्यक्षता की, इसलिए 2026 उसकी चौथी बारी थी। कथन 3 ग़लत है: ब्रिक्स का कोई स्थायी सचिवालय नहीं है -- घूर्णी अध्यक्ष इसका कार्य चलाता है, इसी कारण इसके परिणाम मेज़बान की प्राथमिकताओं पर बहुत निर्भर करते हैं। शंघाई में न्यू डेवलपमेंट बैंक है, जिसे ब्रिक्स देशों ने स्थापित किया पर जो अपने सदस्यों वाली एक अलग संस्था है।",
  "Ministry of External Affairs, 18th BRICS Summit, New Delhi, and New Delhi Declaration (September 2026); BRICS chairships 2012, 2016, 2021.",
  "ca-t3-ca-brics-new-delhi-theme-fourth-chair-no-secretariat", craft="precision")

S(IN, "medium", "The Shanghai Cooperation Organisation completed 25 years in 2026. Consider the following statements:",
  "शंघाई सहयोग संगठन ने 2026 में 25 वर्ष पूरे किए। निम्नलिखित कथनों पर विचार कीजिए:",
  ["It was founded at Shanghai in 2001.",
   "India became a full member in 2017.",
   "Its Regional Anti-Terrorist Structure is based in Tashkent."],
  ["इसकी स्थापना 2001 में शंघाई में हुई।",
   "भारत 2017 में इसका पूर्ण सदस्य बना।",
   "इसकी क्षेत्रीय आतंकवाद-रोधी संरचना ताशकंद में स्थित है।"],
  C3, 2,
  "All three statements are correct. The SCO grew out of the 'Shanghai Five' of 1996 -- China, Russia, Kazakhstan, Kyrgyzstan and Tajikistan -- and was founded with Uzbekistan in June 2001; India and Pakistan joined as full members at Astana in 2017, Iran in 2023 and Belarus in 2024. Its two permanent bodies are the Secretariat in Beijing and the Regional Anti-Terrorist Structure in Tashkent, which reflects its founding focus on terrorism, separatism and extremism. "
  "At its 25th-year summit the organisation amended its Charter, adopted English as an official language alongside Russian and Chinese, and agreed on a centre for countering security threats; India offered to host its first civilisational dialogue forum.",
  "तीनों कथन सही हैं। एससीओ 1996 के ‘शंघाई फ़ाइव’ -- चीन, रूस, कज़ाख़स्तान, किर्गिज़स्तान और ताजिकिस्तान -- से निकला और जून 2001 में उज़्बेकिस्तान के साथ स्थापित हुआ; भारत और पाकिस्तान 2017 में अस्ताना में पूर्ण सदस्य बने, ईरान 2023 में और बेलारूस 2024 में। इसके दो स्थायी निकाय बीजिंग में सचिवालय और ताशकंद में क्षेत्रीय आतंकवाद-रोधी संरचना हैं, जो आतंकवाद, अलगाववाद और उग्रवाद पर इसके स्थापना-कालीन ध्यान को दर्शाता है। "
  "अपनी 25वीं वर्षगाँठ के शिखर सम्मेलन में संगठन ने अपने चार्टर में संशोधन किया, रूसी और चीनी के साथ अंग्रेज़ी को आधिकारिक भाषा बनाया और सुरक्षा ख़तरों से निपटने के एक केंद्र पर सहमति की; भारत ने इसका पहला सभ्यतागत संवाद मंच आयोजित करने की पेशकश की।",
  "Ministry of External Affairs, 26th SCO Summit (2026); Charter of the Shanghai Cooperation Organisation (2002).",
  "ca-t3-ca-sco-25-shanghai-2001-india-2017-rats-tashkent", craft="precision")

S(IN, "medium", "Japan's Prime Minister visited India for the annual summit, ahead of 75 years of diplomatic relations in 2027. Consider the following statements:",
  "जापान की प्रधानमंत्री वार्षिक शिखर सम्मेलन के लिए भारत आईं, 2027 में राजनयिक संबंधों के 75 वर्षों से पहले। निम्नलिखित कथनों पर विचार कीजिए:",
  ["Japan's present Prime Minister is the first woman to hold the office.",
   "India did not sign the San Francisco Peace Treaty of 1951 and concluded a separate peace treaty with Japan in 1952.",
   "Japan is a member of the Quad along with India, Australia and the United States."],
  ["जापान की वर्तमान प्रधानमंत्री इस पद पर रहने वाली पहली महिला हैं।",
   "भारत ने 1951 की सैन फ़्रांसिस्को शांति संधि पर हस्ताक्षर नहीं किए और 1952 में जापान के साथ एक अलग शांति संधि की।",
   "भारत, ऑस्ट्रेलिया और संयुक्त राज्य अमेरिका के साथ जापान क्वाड का सदस्य है।"],
  C3, 2,
  "All three statements are correct. Sanae Takaichi became Japan's first woman Prime Minister in October 2025; at the 16th annual summit the two countries adopted a Joint Declaration on Economic Security, on supply chains, critical minerals and technology. "
  "India stayed away from the San Francisco conference, holding that the treaty did not restore Japan's full sovereignty and left foreign troops on its soil, and signed its own treaty in June 1952, waiving all reparations; diplomatic relations date from that year, which is why 2027 marks 75 years. Japan, India, Australia and the United States make up the Quad, and Japan has also financed projects such as the Mumbai-Ahmedabad high-speed rail.",
  "तीनों कथन सही हैं। साने ताकाइची अक्टूबर 2025 में जापान की पहली महिला प्रधानमंत्री बनीं; 16वें वार्षिक शिखर सम्मेलन में दोनों देशों ने आपूर्ति शृंखलाओं, महत्त्वपूर्ण खनिजों और प्रौद्योगिकी पर आर्थिक सुरक्षा संबंधी संयुक्त घोषणा अपनाई। "
  "भारत सैन फ़्रांसिस्को सम्मेलन से दूर रहा, यह मानते हुए कि संधि जापान की पूर्ण संप्रभुता बहाल नहीं करती और उसकी भूमि पर विदेशी सेनाएँ छोड़ती है, और जून 1952 में सभी क्षतिपूर्ति छोड़ते हुए अपनी अलग संधि की; राजनयिक संबंध उसी वर्ष से हैं, इसलिए 2027 में 75 वर्ष होंगे। जापान, भारत, ऑस्ट्रेलिया और संयुक्त राज्य अमेरिका क्वाड बनाते हैं, और जापान ने मुंबई-अहमदाबाद हाई-स्पीड रेल जैसी परियोजनाओं का वित्तपोषण भी किया है।",
  "Ministry of External Affairs, 16th India-Japan Annual Summit and Joint Declaration on Economic Security (2026); Treaty of Peace between Japan and India (9 June 1952).",
  "ca-t3-ca-india-japan-takaichi-sf-treaty-1952-quad", craft="linkage")

S(IN, "hard", "At the UN General Assembly, Japan's Prime Minister called for deleting the 'enemy state' clauses of the UN Charter. Consider the following statements:",
  "संयुक्त राष्ट्र महासभा में जापान की प्रधानमंत्री ने संयुक्त राष्ट्र चार्टर के ‘शत्रु राज्य’ खंडों को हटाने की माँग की। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The clauses refer to the countries that were enemies of the Allied powers in the Second World War.",
   "The General Assembly has already declared these clauses obsolete.",
   "The clauses can be deleted by a resolution of the General Assembly alone."],
  ["ये खंड उन देशों से संबंधित हैं जो द्वितीय विश्व युद्ध में मित्र राष्ट्रों के शत्रु थे।",
   "महासभा इन खंडों को पहले ही अप्रचलित घोषित कर चुकी है।",
   "इन खंडों को केवल महासभा के एक संकल्प से हटाया जा सकता है।"],
  C3, 1,
  "Statements 1 and 2 are correct. Articles 53, 77 and 107 of the Charter, written in 1945, mention the 'enemy states' of the war -- chiefly Germany and Japan -- and were once read as allowing action against them without the Security Council's authorisation. The General Assembly called them obsolete in 1995, and the 2005 World Summit resolved to delete them, yet China and North Korea have since cited them against Japan. "
  "Statement 3 is wrong: changing the Charter needs an amendment under Article 108 -- adopted by two-thirds of the General Assembly and ratified by two-thirds of the members, including all five permanent members of the Security Council -- so any one of the P5 can block it, which is why the dead letters survive. The same rule makes reform of the Council itself so hard.",
  "कथन 1 और 2 सही हैं। 1945 में लिखे चार्टर के अनुच्छेद 53, 77 और 107 युद्ध के ‘शत्रु राज्यों’ -- मुख्यतः जर्मनी और जापान -- का उल्लेख करते हैं और कभी इन्हें सुरक्षा परिषद की अनुमति के बिना उनके विरुद्ध कार्रवाई की अनुमति के रूप में पढ़ा जाता था। महासभा ने 1995 में इन्हें अप्रचलित कहा, और 2005 के विश्व शिखर सम्मेलन ने इन्हें हटाने का संकल्प लिया, फिर भी चीन और उत्तर कोरिया ने तब से जापान के विरुद्ध इनका हवाला दिया है। "
  "कथन 3 ग़लत है: चार्टर बदलने के लिए अनुच्छेद 108 के अंतर्गत संशोधन चाहिए -- महासभा के दो-तिहाई द्वारा स्वीकृत और सुरक्षा परिषद के सभी पाँच स्थायी सदस्यों सहित दो-तिहाई सदस्यों द्वारा अनुसमर्थित -- इसलिए पी5 में से कोई एक भी इसे रोक सकता है, इसी कारण ये निष्प्रभावी खंड बने हुए हैं। यही नियम परिषद के सुधार को भी इतना कठिन बनाता है।",
  "Charter of the United Nations, Articles 53, 77, 107 and 108; UN General Assembly resolution 50/52 (1995) and 2005 World Summit Outcome; Government of Japan, address to the UN General Assembly (2026).",
  "ca-t3-ca-un-charter-enemy-state-clauses-art-108", craft="precision")

S(IN, "medium", "Twenty-five years after the 9/11 attacks on the United States, consider the following statements about Security Council Resolution 1373, adopted in response:",
  "संयुक्त राज्य अमेरिका पर 9/11 के हमलों के पच्चीस वर्ष बाद, उनके उत्तर में अपनाए गए सुरक्षा परिषद के संकल्प 1373 के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It was adopted under Chapter VII of the UN Charter and is binding on all member states.",
   "It set up the Counter-Terrorism Committee of the Security Council.",
   "It contains a definition of terrorism agreed by all member states."],
  ["इसे संयुक्त राष्ट्र चार्टर के अध्याय VII के अंतर्गत अपनाया गया और यह सभी सदस्य राज्यों पर बाध्यकारी है।",
   "इसने सुरक्षा परिषद की आतंकवाद-रोधी समिति स्थापित की।",
   "इसमें सभी सदस्य राज्यों द्वारा स्वीकृत आतंकवाद की एक परिभाषा है।"],
  C3, 1,
  "Statements 1 and 2 are correct. Adopted unanimously on 28 September 2001, the resolution obliges every state to criminalise the financing of terrorism, freeze terrorist funds and deny safe haven, and created the Counter-Terrorism Committee to monitor compliance; India chaired the Committee in 2022 and hosted its special meeting in Delhi and Mumbai. "
  "Statement 3 is wrong: the resolution deliberately avoided a definition, because states could not agree on one -- the old dispute over 'freedom fighters' and state terrorism. That gap is why India's proposed Comprehensive Convention on International Terrorism, tabled at the UN in 1996, thirty years ago, is still stuck in negotiation.",
  "कथन 1 और 2 सही हैं। 28 सितंबर 2001 को सर्वसम्मति से अपनाया गया यह संकल्प हर राज्य को आतंकवाद के वित्तपोषण को अपराध बनाने, आतंकवादी धन फ़्रीज़ करने और शरण न देने के लिए बाध्य करता है, और अनुपालन की निगरानी के लिए आतंकवाद-रोधी समिति बनाता है; भारत ने 2022 में समिति की अध्यक्षता की और दिल्ली तथा मुंबई में उसकी विशेष बैठक आयोजित की। "
  "कथन 3 ग़लत है: संकल्प ने जानबूझकर परिभाषा से परहेज़ किया, क्योंकि राज्य एक परिभाषा पर सहमत नहीं हो सके -- ‘स्वतंत्रता सेनानियों’ और राज्य-प्रायोजित आतंकवाद पर पुराना विवाद। इसी कमी के कारण भारत द्वारा प्रस्तावित अंतरराष्ट्रीय आतंकवाद पर व्यापक अभिसमय, जो तीस वर्ष पहले 1996 में संयुक्त राष्ट्र में रखा गया, अब भी वार्ता में अटका है।",
  "UN Security Council resolution 1373 (2001); Counter-Terrorism Committee; Ministry of External Affairs, draft Comprehensive Convention on International Terrorism (1996).",
  "ca-t3-ca-unsc-1373-chapter-vii-ctc-no-definition-ccit", craft="linkage")

S(IN, "medium", "The Comprehensive Nuclear-Test-Ban Treaty was opened for signature thirty years ago. Consider the following statements:",
  "व्यापक परमाणु परीक्षण प्रतिबंध संधि तीस वर्ष पहले हस्ताक्षर के लिए खोली गई थी। निम्नलिखित कथनों पर विचार कीजिए:",
  ["India has neither signed nor ratified the treaty.",
   "The treaty is in force, as more than two-thirds of the world's countries have ratified it.",
   "It bans only nuclear tests in the atmosphere and under water, leaving underground tests outside its scope."],
  ["भारत ने इस संधि पर न हस्ताक्षर किए हैं, न इसका अनुसमर्थन किया है।",
   "संधि लागू है, क्योंकि विश्व के दो-तिहाई से अधिक देशों ने इसका अनुसमर्थन कर दिया है।",
   "यह केवल वायुमंडल और जल के नीचे परमाणु परीक्षणों पर रोक लगाती है, भूमिगत परीक्षणों को इसके दायरे से बाहर छोड़ती है।"],
  C3, 0,
  "Only statement 1 is correct. India refused to sign in 1996, arguing that the treaty did not commit the nuclear-weapon states to disarm within a time frame; it tested in 1998 and has since kept a voluntary moratorium. "
  "Statement 2 is wrong: about 178 states have ratified, but the treaty enters into force only when all 44 states listed in its Annex 2 -- those with nuclear reactors at the time -- have ratified, and India, Pakistan and North Korea have not signed while the United States, China, Iran, Israel and Egypt have not ratified; Russia withdrew its ratification in 2023. Statement 3 is wrong: that describes the Partial Test Ban Treaty of 1963; the CTBT bans all nuclear explosions, underground included, and its verification network of seismic and other stations already runs from Vienna.",
  "केवल कथन 1 सही है। भारत ने 1996 में हस्ताक्षर से इनकार किया, यह तर्क देते हुए कि संधि परमाणु-शस्त्र संपन्न राज्यों को समय-सीमा में निरस्त्रीकरण के लिए प्रतिबद्ध नहीं करती; उसने 1998 में परीक्षण किए और तब से स्वैच्छिक स्थगन रखा है। "
  "कथन 2 ग़लत है: लगभग 178 राज्यों ने अनुसमर्थन किया है, पर संधि तभी लागू होती है जब इसकी अनुसूची 2 में सूचीबद्ध सभी 44 राज्य -- जिनके पास उस समय परमाणु रिएक्टर थे -- अनुसमर्थन कर दें, और भारत, पाकिस्तान तथा उत्तर कोरिया ने हस्ताक्षर नहीं किए जबकि संयुक्त राज्य अमेरिका, चीन, ईरान, इज़रायल और मिस्र ने अनुसमर्थन नहीं किया; रूस ने 2023 में अपना अनुसमर्थन वापस लिया। कथन 3 ग़लत है: यह 1963 की आंशिक परीक्षण प्रतिबंध संधि का वर्णन है; सीटीबीटी भूमिगत सहित सभी परमाणु विस्फोटों पर रोक लगाती है, और भूकंपीय तथा अन्य केंद्रों का इसका सत्यापन नेटवर्क वियना से पहले से चलता है।",
  "Comprehensive Nuclear-Test-Ban Treaty (opened for signature 24 September 1996), Article XIV and Annex 2; CTBTO Preparatory Commission; Ministry of External Affairs.",
  "ca-t3-ca-ctbt-30-india-not-signed-annex-2-all-tests", craft="precision")

S(DF, "medium", "AUKUS, the security partnership of Australia, the United Kingdom and the United States, completed five years in 2026. Consider the following statements:",
  "ऑस्ट्रेलिया, यूनाइटेड किंगडम और संयुक्त राज्य अमेरिका की सुरक्षा साझेदारी ऑकस ने 2026 में पाँच वर्ष पूरे किए। निम्नलिखित कथनों पर विचार कीजिए:",
  ["Under it, Australia is to acquire nuclear-powered submarines armed with conventional weapons.",
   "It requires Australia to become a nuclear-weapon state under the Nuclear Non-Proliferation Treaty.",
   "It replaced the ANZUS treaty of 1951, which has since lapsed."],
  ["इसके अंतर्गत ऑस्ट्रेलिया को पारंपरिक हथियारों से लैस परमाणु-चालित पनडुब्बियाँ प्राप्त करनी हैं।",
   "यह ऑस्ट्रेलिया से परमाणु अप्रसार संधि के अंतर्गत परमाणु-शस्त्र संपन्न राज्य बनने की अपेक्षा करता है।",
   "इसने 1951 की एंज़स संधि का स्थान लिया, जो तब से समाप्त हो गई है।"],
  C3, 0,
  "Only statement 1 is correct. Announced in September 2021, AUKUS's first pillar gives Australia nuclear-powered attack submarines -- first American Virginia-class boats, then a new SSN-AUKUS design -- whose reactors let them stay submerged far longer than diesel boats; its second pillar covers advanced technologies such as AI, hypersonics and quantum. "
  "Statement 2 is wrong: Australia remains a non-nuclear-weapon state under the NPT; the submarines carry conventional arms, and the transfer of naval nuclear fuel is being handled with the IAEA under arrangements for non-explosive military use. Statement 3 is wrong: ANZUS, signed in 1951, still binds Australia and the United States, though the US suspended its obligations to New Zealand in 1986 over New Zealand's nuclear-free policy. India is not part of AUKUS; it works with the same partners through the Quad.",
  "केवल कथन 1 सही है। सितंबर 2021 में घोषित ऑकस का पहला स्तंभ ऑस्ट्रेलिया को परमाणु-चालित आक्रमण पनडुब्बियाँ देता है -- पहले अमेरिकी वर्जीनिया-श्रेणी की, फिर नई एसएसएन-ऑकस डिज़ाइन की -- जिनके रिएक्टर उन्हें डीज़ल पनडुब्बियों से कहीं अधिक समय तक जलमग्न रहने देते हैं; इसका दूसरा स्तंभ एआई, हाइपरसोनिक्स और क्वांटम जैसी उन्नत प्रौद्योगिकियों को समेटता है। "
  "कथन 2 ग़लत है: ऑस्ट्रेलिया एनपीटी के अंतर्गत परमाणु-शस्त्र रहित राज्य बना रहता है; पनडुब्बियाँ पारंपरिक हथियार ले जाती हैं, और नौसैनिक परमाणु ईंधन का हस्तांतरण आईएईए के साथ गैर-विस्फोटक सैन्य उपयोग की व्यवस्थाओं के अंतर्गत हो रहा है। कथन 3 ग़लत है: 1951 में हस्ताक्षरित एंज़स अब भी ऑस्ट्रेलिया और संयुक्त राज्य अमेरिका को बाँधती है, यद्यपि अमेरिका ने न्यूज़ीलैंड की परमाणु-मुक्त नीति के कारण 1986 में उसके प्रति अपने दायित्व निलंबित कर दिए। भारत ऑकस का भाग नहीं है; वह इन्हीं साझेदारों के साथ क्वाड के माध्यम से काम करता है।",
  "Joint Leaders Statement on AUKUS (15 September 2021); International Atomic Energy Agency, Australia's naval nuclear propulsion arrangement; ANZUS Treaty (1951).",
  "ca-t3-ca-aukus-5-ssn-conventional-npt-anzus-in-force", craft="precision")

M(IN, "medium",
  "The Gujral Doctrine, set out thirty years ago, guided India's policy towards its neighbours. Which one of the following was NOT one of its principles?",
  "तीस वर्ष पहले प्रस्तुत गुजराल सिद्धांत ने अपने पड़ोसियों के प्रति भारत की नीति का मार्गदर्शन किया। निम्नलिखित में से कौन-सा उसका सिद्धांत नहीं था?",
  ["Settlement of all disputes through mediation by a third party",
   "Not insisting on reciprocity in dealings with smaller neighbours",
   "Non-interference in one another's internal affairs",
   "Not allowing one's territory to be used against another country of the region"],
  ["सभी विवादों का किसी तीसरे पक्ष की मध्यस्थता से निपटारा",
   "छोटे पड़ोसियों के साथ व्यवहार में पारस्परिकता पर ज़ोर न देना",
   "एक-दूसरे के आंतरिक मामलों में हस्तक्षेप न करना",
   "अपने क्षेत्र का उपयोग क्षेत्र के किसी अन्य देश के विरुद्ध न होने देना"],
  0,
  "The doctrine called for settling disputes through peaceful bilateral negotiations, not third-party mediation, which India has consistently resisted, notably on Kashmir. Set out by I.K. Gujral as External Affairs Minister in 1996, it had five principles: with Bangladesh, Bhutan, the Maldives, Nepal and Sri Lanka, India would give in good faith without asking for reciprocity; no country of the region would let its territory be used against another; none would interfere in another's internal affairs; all would respect one another's territorial integrity and sovereignty; and disputes would be settled bilaterally and peacefully. "
  "The Ganga Waters Treaty with Bangladesh, signed in December 1996, was its best-known result. Pakistan was outside the non-reciprocity principle, which was meant for the smaller neighbours.",
  "सिद्धांत ने विवादों के निपटारे के लिए शांतिपूर्ण द्विपक्षीय वार्ता का आह्वान किया, तीसरे पक्ष की मध्यस्थता का नहीं, जिसका भारत ने लगातार विरोध किया है, विशेषकर कश्मीर पर। 1996 में विदेश मंत्री के रूप में आई.के. गुजराल द्वारा प्रस्तुत इस सिद्धांत के पाँच सूत्र थे: बांग्लादेश, भूटान, मालदीव, नेपाल और श्रीलंका के साथ भारत पारस्परिकता माँगे बिना सद्भाव से देगा; क्षेत्र का कोई देश अपने क्षेत्र का उपयोग दूसरे के विरुद्ध नहीं होने देगा; कोई दूसरे के आंतरिक मामलों में हस्तक्षेप नहीं करेगा; सभी एक-दूसरे की प्रादेशिक अखंडता और संप्रभुता का सम्मान करेंगे; और विवाद द्विपक्षीय और शांतिपूर्ण ढंग से निपटाए जाएँगे। "
  "दिसंबर 1996 में बांग्लादेश के साथ हस्ताक्षरित गंगा जल संधि इसका सबसे प्रसिद्ध परिणाम थी। पाकिस्तान अपारस्परिकता के सिद्धांत से बाहर था, जो छोटे पड़ोसियों के लिए था।",
  "Ministry of External Affairs, speeches of I.K. Gujral on India's neighbourhood policy (1996-97); Treaty on the Sharing of the Ganga Waters at Farakka (1996).",
  "ca-t3-ca-gujral-doctrine-30-not-third-party-mediation", pos=POS.get("ca-t3-ca-gujral-doctrine-30-not-third-party-mediation", 1), craft="precision")

S(IN, "medium", "India and China held a new round of talks between their Special Representatives on the boundary question. Consider the following statements:",
  "भारत और चीन ने सीमा प्रश्न पर अपने विशेष प्रतिनिधियों के बीच वार्ता का एक नया दौर किया। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Special Representatives mechanism on the boundary question was set up in 2003.",
   "In 2005 the two countries agreed on Political Parameters and Guiding Principles for a boundary settlement.",
   "The two countries restored ambassador-level relations in 1976, after the gap that followed the 1962 war."],
  ["सीमा प्रश्न पर विशेष प्रतिनिधि तंत्र 2003 में स्थापित किया गया था।",
   "2005 में दोनों देशों ने सीमा समाधान के लिए राजनीतिक मापदंडों और मार्गदर्शक सिद्धांतों पर सहमति की।",
   "1962 के युद्ध के बाद के अंतराल के पश्चात दोनों देशों ने 1976 में राजदूत-स्तर के संबंध बहाल किए।"],
  C3, 2,
  "All three statements are correct. The mechanism was created during Prime Minister Vajpayee's visit to China in 2003, with India's National Security Adviser and China's Foreign Minister as the representatives; the 2005 agreement set out principles such as taking into account settled populations, and the 25th round was held in Beijing in August 2026, a year after the 24th in New Delhi. "
  "After the 1962 war the two countries kept only chargés d'affaires; ambassadors returned in 1976, fifty years ago, when K.R. Narayanan went to Beijing. The SR talks deal with the overall settlement, while the separate Working Mechanism for Consultation and Coordination and the corps commanders' talks handle the Line of Actual Control.",
  "तीनों कथन सही हैं। यह तंत्र 2003 में प्रधानमंत्री वाजपेयी की चीन यात्रा के दौरान बना, जिसमें भारत के राष्ट्रीय सुरक्षा सलाहकार और चीन के विदेश मंत्री प्रतिनिधि हैं; 2005 के समझौते ने बसी हुई आबादियों का ध्यान रखने जैसे सिद्धांत तय किए, और 25वाँ दौर अगस्त 2026 में बीजिंग में हुआ, नई दिल्ली में 24वें दौर के एक वर्ष बाद। "
  "1962 के युद्ध के बाद दोनों देशों ने केवल कार्यदूत रखे; राजदूत पचास वर्ष पहले 1976 में लौटे, जब के.आर. नारायणन बीजिंग गए। विशेष प्रतिनिधि वार्ता समग्र समाधान से संबंधित है, जबकि परामर्श और समन्वय का अलग कार्य तंत्र और कोर कमांडर वार्ता वास्तविक नियंत्रण रेखा को सँभालते हैं।",
  "Ministry of External Affairs and Ministry of Foreign Affairs of China, 25th round of the Special Representatives' talks on the boundary question (Beijing, August 2026); Agreement on the Political Parameters and Guiding Principles for the Settlement of the India-China Boundary Question (2005).",
  "ca-t3-ca-india-china-sr-2003-parameters-2005-ambassadors-1976", craft="linkage")

S(IN, "medium", "The 1951 Convention relating to the Status of Refugees completed 75 years in 2026. Consider the following statements:",
  "शरणार्थियों की स्थिति से संबंधित 1951 के अभिसमय ने 2026 में 75 वर्ष पूरे किए। निम्नलिखित कथनों पर विचार कीजिए:",
  ["India is not a party to the Convention or to its 1967 Protocol.",
   "The 1967 Protocol restricted the Convention to refugees from Europe.",
   "The Office of the UN High Commissioner for Refugees was created by the Convention."],
  ["भारत न इस अभिसमय का पक्षकार है, न इसके 1967 के प्रोटोकॉल का।",
   "1967 के प्रोटोकॉल ने अभिसमय को यूरोप के शरणार्थियों तक सीमित कर दिया।",
   "संयुक्त राष्ट्र शरणार्थी उच्चायुक्त का कार्यालय इस अभिसमय द्वारा बनाया गया।"],
  C3, 0,
  "Only statement 1 is correct. India has hosted large refugee populations -- from Tibet, Sri Lanka, Bangladesh and Afghanistan -- but deals with them through executive policy and the Foreigners Act rather than a treaty, partly to keep its hands free on porous borders; the courts have read the principle of non-refoulement, not returning a person to persecution, into Article 21 in some cases. "
  "Statement 2 is wrong: the Convention was originally limited to events before 1951 and, at a state's option, to Europe; the 1967 Protocol removed those limits and made it universal. Statement 3 is wrong: UNHCR was set up by the General Assembly in December 1950, before the Convention was adopted in July 1951; it has won the Nobel Peace Prize twice.",
  "केवल कथन 1 सही है। भारत ने तिब्बत, श्रीलंका, बांग्लादेश और अफ़ग़ानिस्तान से बड़ी शरणार्थी आबादियों को आश्रय दिया है, पर उनसे किसी संधि के बजाय कार्यकारी नीति और विदेशी अधिनियम के माध्यम से निपटता है, आंशिक रूप से खुली सीमाओं पर अपने हाथ स्वतंत्र रखने के लिए; न्यायालयों ने कुछ मामलों में नॉन-रिफ़ाउलमेंट, यानी किसी व्यक्ति को उत्पीड़न की ओर न लौटाने, के सिद्धांत को अनुच्छेद 21 में पढ़ा है। "
  "कथन 2 ग़लत है: अभिसमय मूलतः 1951 से पहले की घटनाओं तक और, किसी राज्य के विकल्प पर, यूरोप तक सीमित था; 1967 के प्रोटोकॉल ने ये सीमाएँ हटाकर इसे सार्वभौमिक बनाया। कथन 3 ग़लत है: यूएनएचसीआर दिसंबर 1950 में महासभा द्वारा स्थापित हुआ, जुलाई 1951 में अभिसमय अपनाए जाने से पहले; इसने दो बार नोबेल शांति पुरस्कार जीता है।",
  "Convention relating to the Status of Refugees (28 July 1951) and Protocol (1967); UN General Assembly resolution 428 (V) (1950), Statute of the Office of the UNHCR.",
  "ca-t3-ca-refugee-convention-75-india-not-party-1967-unhcr-1950", craft="precision")

MX(DF, "medium", "Indian forces took part in several exercises during the quarter. Match List-I (exercise) with List-II (its nature):",
   "तिमाही के दौरान भारतीय सेनाओं ने कई अभ्यासों में भाग लिया। सूची-I (अभ्यास) का सूची-II (उसकी प्रकृति) से मिलान कीजिए:",
   ["RIMPAC", "Pitch Black", "Yudh Abhyas", "Maitree"],
   ["रिमपैक", "पिच ब्लैक", "युद्ध अभ्यास", "मैत्री"],
   ["Bilateral army exercise with Thailand", "Multinational maritime exercise hosted by the United States", "Multinational air exercise hosted by Australia", "Bilateral army exercise with the United States"],
   ["थाईलैंड के साथ द्विपक्षीय सेना अभ्यास", "संयुक्त राज्य अमेरिका द्वारा आयोजित बहुराष्ट्रीय समुद्री अभ्यास", "ऑस्ट्रेलिया द्वारा आयोजित बहुराष्ट्रीय वायु अभ्यास", "संयुक्त राज्य अमेरिका के साथ द्विपक्षीय सेना अभ्यास"],
   (2, 3, 4, 1), POS.get("ca-t3-ca-exercises-rimpac-pitch-black-yudh-abhyas-maitree", 0),
   "The correct code is A-2, B-3, C-4, D-1. RIMPAC, off Hawaii, is the world's largest maritime exercise; India sent a P-8I aircraft and, for the first time, served as deputy commander of a task force for theatre anti-submarine warfare. Pitch Black, hosted by the Royal Australian Air Force at Darwin, brought together about 20 air forces; the IAF sent Rafales for the first time, with C-17s. "
   "Yudh Abhyas, the Indian and US armies' exercise, held its 22nd edition at Auli in Uttarakhand and the Mahajan range in Rajasthan, with drones and counter-drone drills; Maitree, with the Royal Thai Army, held its 15th edition in Thailand, on counter-insurgency in jungle and semi-urban terrain. Bilateral names often carry the partner's flavour -- 'maitree' means friendship -- which helps in such matches.",
   "सही कूट A-2, B-3, C-4, D-1 है। हवाई के पास रिमपैक विश्व का सबसे बड़ा समुद्री अभ्यास है; भारत ने एक पी-8आई विमान भेजा और पहली बार रंगमंच-स्तरीय पनडुब्बी-रोधी युद्ध के एक कार्य बल के उप-कमांडर की भूमिका निभाई। डार्विन में रॉयल ऑस्ट्रेलियन एयर फ़ोर्स द्वारा आयोजित पिच ब्लैक में लगभग 20 वायु सेनाएँ एकत्र हुईं; भारतीय वायु सेना ने पहली बार राफ़ेल भेजे, सी-17 के साथ। "
   "भारत और अमेरिका की सेनाओं के अभ्यास युद्ध अभ्यास का 22वाँ संस्करण उत्तराखंड के औली और राजस्थान की महाजन रेंज में ड्रोन और ड्रोन-रोधी अभ्यासों के साथ हुआ; रॉयल थाई आर्मी के साथ मैत्री का 15वाँ संस्करण थाईलैंड में जंगल और अर्ध-शहरी क्षेत्र में उग्रवाद-रोध पर हुआ। द्विपक्षीय नाम प्रायः साझेदारी का भाव लिए होते हैं -- ‘मैत्री’ का अर्थ दोस्ती है -- जो ऐसे मिलानों में सहायक है।",
   "Ministry of Defence and PIB, Indian participation in RIMPAC 2026, Exercise Pitch Black 2026, Exercise Yudh Abhyas 2026 and Exercise Maitree-XV (July-September 2026).",
   "ca-t3-ca-exercises-rimpac-pitch-black-yudh-abhyas-maitree", "precision")

MX(IN, "medium", "Match List-I (organisation) with List-II (the city where it is based):",
   "सूची-I (संगठन) का सूची-II (वह शहर जहाँ वह स्थित है) से मिलान कीजिए:",
   ["World Artificial Intelligence Cooperation Organization", "Preparatory Commission for the CTBT Organization", "Office of the UN High Commissioner for Refugees", "International Centre for Theoretical Physics"],
   ["विश्व कृत्रिम बुद्धिमत्ता सहयोग संगठन", "सीटीबीटी संगठन का तैयारी आयोग", "संयुक्त राष्ट्र शरणार्थी उच्चायुक्त का कार्यालय", "अंतरराष्ट्रीय सैद्धांतिक भौतिकी केंद्र"],
   ["Geneva", "Trieste", "Shanghai", "Vienna"],
   ["जिनेवा", "ट्रिएस्ते", "शंघाई", "वियना"],
   (3, 4, 1, 2), POS.get("ca-t3-ca-seats-waico-ctbto-unhcr-ictp", 2),
   "The correct code is A-3, B-4, C-1, D-2. The World AI Cooperation Organization, proposed by China, was founded at Shanghai by 29 countries in July 2026 and is to be headquartered there, a rival pole in AI governance. The CTBTO Preparatory Commission works from Vienna, alongside the IAEA, running the treaty's monitoring network while the treaty awaits entry into force. "
   "UNHCR is in Geneva, as are the WHO and the ILO. The Abdus Salam International Centre for Theoretical Physics, in Trieste, Italy, run with UNESCO and the IAEA, awards the Dirac Medal, given in 2026 to Deepak Dhar among others. Geneva and Vienna are the usual traps, since both host many UN bodies.",
   "सही कूट A-3, B-4, C-1, D-2 है। चीन द्वारा प्रस्तावित विश्व एआई सहयोग संगठन जुलाई 2026 में 29 देशों द्वारा शंघाई में स्थापित हुआ और वहीं इसका मुख्यालय होना है, जो एआई शासन में एक प्रतिद्वंद्वी ध्रुव है। सीटीबीटीओ का तैयारी आयोग वियना से, आईएईए के साथ, काम करता है और संधि के लागू होने की प्रतीक्षा में उसका निगरानी नेटवर्क चलाता है। "
   "यूएनएचसीआर जिनेवा में है, जैसे डब्ल्यूएचओ और आईएलओ। इटली के ट्रिएस्ते में यूनेस्को और आईएईए के साथ चलने वाला अब्दुस सलाम अंतरराष्ट्रीय सैद्धांतिक भौतिकी केंद्र डिराक पदक देता है, जो 2026 में अन्य लोगों के साथ दीपक धर को मिला। जिनेवा और वियना सामान्य जाल हैं, क्योंकि दोनों में संयुक्त राष्ट्र के कई निकाय हैं।",
   "Government of Shanghai, signing of the agreement establishing the World AI Cooperation Organization (July 2026); CTBTO Preparatory Commission; UNHCR; Abdus Salam International Centre for Theoretical Physics.",
   "ca-t3-ca-seats-waico-ctbto-unhcr-ictp", "precision")

S(DF, "medium", "India has bought Javelin anti-tank missiles from the United States, and an Indian company has agreed to explore producing them in India. Consider the following statements:",
  "भारत ने संयुक्त राज्य अमेरिका से जैवलिन टैंक-रोधी मिसाइलें ख़रीदी हैं, और एक भारतीय कंपनी ने इन्हें भारत में बनाने की संभावना तलाशने पर सहमति दी है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Javelin is a man-portable 'fire-and-forget' missile that can strike a tank from the top, where its armour is thinnest.",
   "India bought it through the US Foreign Military Sales route, a government-to-government channel.",
   "Its production in India is to be undertaken by the Defence Research and Development Organisation alone."],
  ["जैवलिन एक कंधे पर ले जाई जाने वाली ‘फ़ायर-एंड-फ़ॉरगेट’ मिसाइल है जो टैंक पर ऊपर से, जहाँ उसका कवच सबसे पतला होता है, प्रहार कर सकती है।",
   "भारत ने इसे अमेरिका के विदेशी सैन्य बिक्री मार्ग से ख़रीदा, जो सरकार-से-सरकार का माध्यम है।",
   "भारत में इसका उत्पादन केवल रक्षा अनुसंधान और विकास संगठन द्वारा किया जाना है।"],
  C3, 1,
  "Statements 1 and 2 are correct. Once fired, the Javelin's infrared seeker guides it without the operator having to stay exposed, and its top-attack mode hits the thin roof armour of a tank; India signed a Letter of Offer and Acceptance for it under the Foreign Military Sales programme, in which the US government buys from the maker and sells to the partner government. "
  "Statement 3 is wrong: the Javelin Joint Venture of Raytheon and Lockheed Martin signed a memorandum with Tata Advanced Systems to explore final assembly and component production in India; Bharat Dynamics had earlier signed a similar agreement. India's own man-portable anti-tank missile, developed by DRDO, is a separate programme.",
  "कथन 1 और 2 सही हैं। दाग़े जाने के बाद जैवलिन का अवरक्त खोजी उसे दिशा देता है, जिससे संचालक को खुले में रुकना नहीं पड़ता, और इसका ऊपर से प्रहार करने का मोड टैंक की पतली छत के कवच पर चोट करता है; भारत ने इसके लिए विदेशी सैन्य बिक्री कार्यक्रम के अंतर्गत प्रस्ताव और स्वीकृति पत्र पर हस्ताक्षर किए, जिसमें अमेरिकी सरकार निर्माता से ख़रीदकर साझेदार सरकार को बेचती है। "
  "कथन 3 ग़लत है: रेथियॉन और लॉकहीड मार्टिन के जैवलिन संयुक्त उद्यम ने भारत में अंतिम संयोजन और पुर्ज़ों के उत्पादन की संभावना तलाशने के लिए टाटा एडवांस्ड सिस्टम्स के साथ ज्ञापन पर हस्ताक्षर किए; भारत डायनामिक्स ने पहले ऐसा ही समझौता किया था। डीआरडीओ द्वारा विकसित भारत की अपनी कंधे पर ले जाई जाने वाली टैंक-रोधी मिसाइल एक अलग कार्यक्रम है।",
  "Ministry of Defence and US Embassy, Javelin Letter of Offer and Acceptance (August 2026); Lockheed Martin, Javelin Joint Venture and Tata Advanced Systems agreement for co-production in India (August 2026).",
  "ca-t3-ca-javelin-top-attack-fms-tata-co-production", craft="precision")

S(DF, "medium", "The Defence Acquisition Council accorded Acceptance of Necessity to proposals worth about ₹1.10 lakh crore, almost all from Indian sources. Consider the following statements:",
  "रक्षा अधिग्रहण परिषद ने लगभग ₹1.10 लाख करोड़ के प्रस्तावों को आवश्यकता की स्वीकृति दी, लगभग सभी भारतीय स्रोतों से। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Council is chaired by the Defence Minister.",
   "Acceptance of Necessity is the last stage of a procurement, when the contract is signed.",
   "The Council was set up under an Act of Parliament."],
  ["परिषद की अध्यक्षता रक्षा मंत्री करते हैं।",
   "आवश्यकता की स्वीकृति किसी ख़रीद का अंतिम चरण है, जब अनुबंध पर हस्ताक्षर होते हैं।",
   "परिषद संसद के एक अधिनियम के अंतर्गत स्थापित की गई।"],
  C3, 0,
  "Only statement 1 is correct. The Defence Acquisition Council, chaired by the Defence Minister with the service chiefs and the Chief of Defence Staff, is the apex body for capital purchases; its approvals in September 2026 included Arudhra radars, marine gas turbines and vehicles for detecting chemical, biological and nuclear threats, about 98 per cent from Indian sources under the 'Buy (Indian)' categories. "
  "Statement 2 is wrong: Acceptance of Necessity is the first step -- it approves the requirement and the category of purchase, after which requests for proposal, trials, cost negotiation and finally the contract follow, often years later. Statement 3 is wrong: the Council was created by executive decision in 2001, on the recommendation of the Group of Ministers that reviewed national security after the Kargil war.",
  "केवल कथन 1 सही है। रक्षा मंत्री की अध्यक्षता में, सेना प्रमुखों और चीफ़ ऑफ़ डिफ़ेंस स्टाफ़ के साथ, रक्षा अधिग्रहण परिषद पूँजीगत ख़रीद का शीर्ष निकाय है; सितंबर 2026 में इसकी स्वीकृतियों में अरुध्रा रडार, समुद्री गैस टर्बाइन और रासायनिक, जैविक तथा परमाणु ख़तरों का पता लगाने वाले वाहन शामिल थे, ‘बाय (इंडियन)’ श्रेणियों के अंतर्गत लगभग 98 प्रतिशत भारतीय स्रोतों से। "
  "कथन 2 ग़लत है: आवश्यकता की स्वीकृति पहला चरण है -- यह आवश्यकता और ख़रीद की श्रेणी को स्वीकृत करती है, जिसके बाद प्रस्ताव के अनुरोध, परीक्षण, लागत-वार्ता और अंत में अनुबंध आते हैं, प्रायः वर्षों बाद। कथन 3 ग़लत है: परिषद 2001 में कारगिल युद्ध के बाद राष्ट्रीय सुरक्षा की समीक्षा करने वाले मंत्रियों के समूह की सिफ़ारिश पर कार्यकारी निर्णय से बनी।",
  "Ministry of Defence and PIB, Defence Acquisition Council approvals (September 2026); Defence Acquisition Procedure; Report of the Group of Ministers on Reforming the National Security System (2001).",
  "ca-t3-ca-dac-aon-first-step-executive-2001", craft="precision")

M(IN, "medium",
  "CIPS, SPFS and mBridge, often in the news in the context of BRICS, are best described as",
  "ब्रिक्स के संदर्भ में प्रायः समाचारों में रहने वाले सीआईपीएस, एसपीएफ़एस और एमब्रिज का सबसे उपयुक्त वर्णन है",
  ["systems for cross-border payments or payment messaging that offer alternatives to SWIFT",
   "credit rating agencies set up by BRICS countries to rival the agencies based in the United States",
   "stablecoins issued jointly by central banks to settle trade in commodities such as oil and gas",
   "international exchanges for trading carbon credits created under Article 6 of the Paris Agreement"],
  ["सीमा-पार भुगतान या भुगतान-संदेश की प्रणालियाँ जो स्विफ़्ट के विकल्प देती हैं",
   "अमेरिका स्थित एजेंसियों से प्रतिस्पर्धा के लिए ब्रिक्स देशों द्वारा स्थापित क्रेडिट रेटिंग एजेंसियाँ",
   "तेल और गैस जैसी वस्तुओं के व्यापार के निपटान के लिए केंद्रीय बैंकों द्वारा संयुक्त रूप से जारी स्टेबलकॉइन",
   "पेरिस समझौते के अनुच्छेद 6 के अंतर्गत बने कार्बन क्रेडिट व्यापार के अंतरराष्ट्रीय एक्सचेंज"],
  0,
  "CIPS is China's Cross-Border Interbank Payment System for renminbi payments; SPFS is the Bank of Russia's System for Transfer of Financial Messages, built after the 2014 sanctions as an alternative to the SWIFT messaging network; and mBridge is a platform linking central bank digital currencies of China, Hong Kong, Thailand, the UAE and Saudi Arabia, begun with the BIS Innovation Hub, which withdrew in 2024. "
  "SWIFT, a Belgian cooperative, only carries payment messages, but cutting a country off from it -- as with Iran and Russia -- can freeze much of its trade, which is why sanctioned and other countries look for alternatives. India's own options include UPI links and rupee vostro accounts for trade settlement. None of the other options exists as described.",
  "सीआईपीएस रेनमिनबी भुगतानों के लिए चीन की सीमा-पार अंतरबैंक भुगतान प्रणाली है; एसपीएफ़एस बैंक ऑफ़ रशिया की वित्तीय संदेश हस्तांतरण प्रणाली है, जो 2014 के प्रतिबंधों के बाद स्विफ़्ट संदेश नेटवर्क के विकल्प के रूप में बनी; और एमब्रिज चीन, हांगकांग, थाईलैंड, यूएई और सऊदी अरब की केंद्रीय बैंक डिजिटल मुद्राओं को जोड़ने वाला मंच है, जो बीआईएस इनोवेशन हब के साथ शुरू हुआ और जिससे वह 2024 में हट गया। "
  "बेल्जियम की सहकारी संस्था स्विफ़्ट केवल भुगतान संदेश ले जाती है, पर किसी देश को इससे काट देना -- जैसे ईरान और रूस के साथ हुआ -- उसके व्यापार का बड़ा भाग रोक सकता है, इसी कारण प्रतिबंधित और अन्य देश विकल्प खोजते हैं। भारत के अपने विकल्पों में यूपीआई संपर्क और व्यापार निपटान के लिए रुपया वोस्ट्रो खाते शामिल हैं। अन्य कोई विकल्प वर्णित रूप में अस्तित्व में नहीं है।",
  "People's Bank of China, CIPS; Bank of Russia, SPFS; Bank for International Settlements, Project mBridge (2024 update); Reserve Bank of India, rupee vostro accounts.",
  "ca-t3-ca-cips-spfs-mbridge-swift-alternatives", pos=POS.get("ca-t3-ca-cips-spfs-mbridge-swift-alternatives", 3), craft="linkage")

S(SP, "easy", "Consider the following statements about the Commonwealth Games held at Glasgow:",
  "ग्लासगो में हुए राष्ट्रमंडल खेलों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["India finished fourth in the medal table.",
   "Shooting was part of the sports programme.",
   "England topped the medal table."],
  ["भारत पदक तालिका में चौथे स्थान पर रहा।",
   "निशानेबाज़ी खेल कार्यक्रम का भाग थी।",
   "इंग्लैंड पदक तालिका में शीर्ष पर रहा।"],
  C3, 0,
  "Only statement 1 is correct. India won 39 medals, 13 of them gold, with boxers winning ten medals, and more golds came from women than from men. "
  "Statement 2 is wrong: Glasgow cut the programme to ten sports to hold down costs, leaving out shooting -- one of India's strongest -- along with wrestling, hockey and some others; the host chooses the optional sports. Statement 3 is wrong: Australia topped the table, with England second and Canada third. Ahmedabad will host the 2030 Games, the centenary edition.",
  "केवल कथन 1 सही है। भारत ने 39 पदक जीते, जिनमें 13 स्वर्ण थे, मुक्केबाज़ों ने दस पदक जीते, और पुरुषों की तुलना में महिलाओं से अधिक स्वर्ण आए। "
  "कथन 2 ग़लत है: ग्लासगो ने लागत घटाने के लिए कार्यक्रम को दस खेलों तक सीमित किया, जिसमें निशानेबाज़ी -- भारत के सबसे मज़बूत खेलों में से एक -- कुश्ती, हॉकी और कुछ अन्य शामिल नहीं थे; वैकल्पिक खेल मेज़बान चुनता है। कथन 3 ग़लत है: ऑस्ट्रेलिया शीर्ष पर रहा, इंग्लैंड दूसरे और कनाडा तीसरे स्थान पर। 2030 के खेल, शताब्दी संस्करण, अहमदाबाद में होंगे।",
  "Commonwealth Sport, Glasgow 2026 medal table; Ministry of Youth Affairs and Sports, India's performance at the Commonwealth Games 2026.",
  "ca-t3-ca-cwg-glasgow-india-fourth-no-shooting-australia-top", craft="precision")

S(SP, "easy", "Consider the following statements about two world cups held in 2026:",
  "2026 में हुए दो विश्व कपों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Spain won the FIFA World Cup for the first time.",
   "Australia won the ICC Women's T20 World Cup for a record seventh time."],
  ["स्पेन ने पहली बार फ़ीफ़ा विश्व कप जीता।",
   "ऑस्ट्रेलिया ने रिकॉर्ड सातवीं बार आईसीसी महिला टी20 विश्व कप जीता।"],
  T2, 1,
  "Only statement 2 is correct. Australia beat the hosts England by seven wickets in the final at Lord's to take their seventh T20 title, a record in the women's game. "
  "Statement 1 is wrong: Spain, who beat Argentina 1-0 after extra time in the final in New Jersey, had also won in 2010, so this was their second title. The 2026 World Cup was the first with 48 teams and was spread over the United States, Canada and Mexico.",
  "केवल कथन 2 सही है। ऑस्ट्रेलिया ने लॉर्ड्स में फ़ाइनल में मेज़बान इंग्लैंड को सात विकेट से हराकर अपना सातवाँ टी20 ख़िताब जीता, जो महिला क्रिकेट में एक रिकॉर्ड है। "
  "कथन 1 ग़लत है: न्यू जर्सी में फ़ाइनल में अर्जेंटीना को अतिरिक्त समय के बाद 1-0 से हराने वाले स्पेन ने 2010 में भी जीता था, इसलिए यह उसका दूसरा ख़िताब था। 2026 का विश्व कप 48 टीमों वाला पहला था और संयुक्त राज्य अमेरिका, कनाडा और मेक्सिको में फैला था।",
  "FIFA, World Cup 2026 final report (July 2026); International Cricket Council, ICC Women's T20 World Cup 2026 final (July 2026).",
  "ca-t3-ca-world-cups-2026-spain-second-australia-seventh", craft="precision")

S(SC, "medium", "The Union Cabinet approved a revamped Khelo India scheme. Consider the following statements:",
  "केंद्रीय मंत्रिमंडल ने एक नवीकृत खेलो इंडिया योजना को स्वीकृति दी। निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is to run from 2026-27 to 2030-31.",
   "It creates a category of Emerging Khelo India Athletes, as a step towards the Target Olympic Podium Scheme.",
   "The approved outlay also covers enhanced assistance to the National Sports Federations."],
  ["इसे 2026-27 से 2030-31 तक चलना है।",
   "यह टारगेट ओलंपिक पोडियम योजना की ओर एक क़दम के रूप में उभरते खेलो इंडिया एथलीटों की श्रेणी बनाती है।",
   "स्वीकृत परिव्यय राष्ट्रीय खेल महासंघों को बढ़ी हुई सहायता को भी समेटता है।"],
  C3, 2,
  "All three statements are correct. The ₹36,441-crore package, the bulk of it for Khelo India, builds a pathway from school and district competitions to Khelo India athletes and then to the Target Olympic Podium Scheme, which funds elite athletes, with feeder schools for early talent spotting; the rest raises support to the National Sports Federations that run each sport. "
  "Sport is a State subject (Entry 33 of the State List), so the Union works mainly through such schemes of the Ministry of Youth Affairs and Sports, and through the National Sports Governance Act, 2025, for the federations.",
  "तीनों कथन सही हैं। ₹36,441 करोड़ का पैकेज, जिसका अधिकांश खेलो इंडिया के लिए है, विद्यालय और ज़िला प्रतियोगिताओं से खेलो इंडिया एथलीटों और फिर उत्कृष्ट खिलाड़ियों का वित्तपोषण करने वाली टारगेट ओलंपिक पोडियम योजना तक एक मार्ग बनाता है, प्रारंभिक प्रतिभा-पहचान के लिए फ़ीडर विद्यालयों के साथ; शेष हर खेल चलाने वाले राष्ट्रीय खेल महासंघों की सहायता बढ़ाता है। "
  "खेल राज्य का विषय है (राज्य सूची की प्रविष्टि 33), इसलिए संघ मुख्यतः युवा कार्यक्रम और खेल मंत्रालय की ऐसी योजनाओं के माध्यम से, और महासंघों के लिए राष्ट्रीय खेल शासन अधिनियम, 2025 के माध्यम से, काम करता है।",
  "Cabinet decision and PIB, revamped Khelo India Scheme and enhanced Assistance to National Sports Federations (July 2026); Constitution of India, Seventh Schedule, List II, Entry 33.",
  "ca-t3-ca-khelo-india-revamp-2031-ekia-tops-ansf", craft="precision")

S(NA, "easy", "Consider the following statements about the Ramon Magsaysay Award:",
  "रेमन मैग्सेसे पुरस्कार के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is given by the Government of the Philippines.",
   "An Indian was among those who received it in 2026.",
   "It was first given in 2000."],
  ["इसे फ़िलीपींस सरकार देती है।",
   "2026 में इसे पाने वालों में एक भारतीय था।",
   "यह पहली बार 2000 में दिया गया।"],
  C3, 3,
  "None of the statements is correct. The award is given by the Ramon Magsaysay Award Foundation, a private foundation in Manila set up in 1957, with support from the Rockefeller Brothers Fund, in memory of the Philippine President who died in an air crash that year; it is often called Asia's Nobel Prize and was first presented in 1958. "
  "The 2026 awardees -- Tommy Koh of Singapore, Bo Kyi of Myanmar and Runa Khan of Bangladesh -- included no Indian; in 2025 Educate Girls became the first Indian organisation to receive it. Earlier Indian laureates include Vinoba Bhave, Mother Teresa, Satyajit Ray, Kiran Bedi and Arvind Kejriwal.",
  "कोई भी कथन सही नहीं है। पुरस्कार रेमन मैग्सेसे पुरस्कार फ़ाउंडेशन देता है, जो मनीला में 1957 में रॉकफ़ेलर ब्रदर्स फ़ंड के सहयोग से उस वर्ष विमान दुर्घटना में मारे गए फ़िलीपींस के राष्ट्रपति की स्मृति में स्थापित एक निजी संस्था है; इसे प्रायः एशिया का नोबेल कहा जाता है और यह पहली बार 1958 में दिया गया। "
  "2026 के पुरस्कार-विजेताओं -- सिंगापुर के टॉमी कोह, म्यांमार के बो की और बांग्लादेश की रूना ख़ान -- में कोई भारतीय नहीं था; 2025 में एजुकेट गर्ल्स इसे पाने वाली पहली भारतीय संस्था बनी। पहले के भारतीय पुरस्कार-विजेताओं में विनोबा भावे, मदर टेरेसा, सत्यजित राय, किरण बेदी और अरविंद केजरीवाल शामिल हैं।",
  "Ramon Magsaysay Award Foundation, 2026 awardees and history of the award.",
  "ca-t3-ca-magsaysay-2026-foundation-no-indian-1958", craft="precision")

S(NA, "medium", "The physicist Deepak Dhar received the Dirac Medal in 2026. Consider the following statements:",
  "भौतिकविद दीपक धर को 2026 में डिराक पदक मिला। निम्नलिखित कथनों पर विचार कीजिए:",
  ["He is the first Indian to receive the Dirac Medal.",
   "His work is in statistical physics, including the 'abelian sandpile' model.",
   "He had earlier become the first Indian to receive the Boltzmann Medal."],
  ["वे डिराक पदक पाने वाले पहले भारतीय हैं।",
   "उनका कार्य सांख्यिकीय भौतिकी में है, ‘एबेलियन सैंडपाइल’ मॉडल सहित।",
   "वे पहले बोल्ट्ज़मान पदक पाने वाले पहले भारतीय बने थे।"],
  C3, 1,
  "Statements 2 and 3 are correct. Dhar, of the International Centre for Theoretical Sciences, Bengaluru, showed how the 'sandpile' model -- grains added until piles topple in avalanches of every size -- can be solved exactly, a key example of self-organised criticality, the way systems from earthquakes to forest fires settle at the edge of instability; in 2022 he became the first Indian to win the Boltzmann Medal, the highest honour in statistical physics. "
  "Statement 1 is wrong: the string theorist Ashoke Sen received the Dirac Medal in 2014, so Dhar is the second Indian, sharing the 2026 medal with three other physicists.",
  "कथन 2 और 3 सही हैं। अंतरराष्ट्रीय सैद्धांतिक विज्ञान केंद्र, बेंगलुरु, के धर ने दिखाया कि ‘सैंडपाइल’ मॉडल -- जिसमें कण जोड़े जाते हैं जब तक ढेर हर आकार के हिमस्खलनों में ढह न जाएँ -- को सटीक रूप से कैसे हल किया जा सकता है, जो स्व-संगठित क्रांतिकता का प्रमुख उदाहरण है, यानी भूकंपों से वनाग्नियों तक प्रणालियाँ अस्थिरता की कगार पर कैसे टिकती हैं; 2022 में वे सांख्यिकीय भौतिकी के सर्वोच्च सम्मान बोल्ट्ज़मान पदक को जीतने वाले पहले भारतीय बने। "
  "कथन 1 ग़लत है: स्ट्रिंग सिद्धांतकार अशोक सेन को 2014 में डिराक पदक मिला था, इसलिए धर दूसरे भारतीय हैं, जिन्होंने 2026 का पदक तीन अन्य भौतिकविदों के साथ साझा किया।",
  "Abdus Salam International Centre for Theoretical Physics, Dirac Medal 2026; International Centre for Theoretical Sciences (TIFR); IUPAP Boltzmann Medal 2022.",
  "ca-t3-ca-dirac-medal-deepak-dhar-second-indian-sandpile", craft="precision")

finish("ca_t3_a.sql", FORMAT, "2026-Q3", update="--update" in sys.argv)
