# -*- coding: utf-8 -*-
"""Level 2 · Test 11 (Environment 3: Policies & Conservation) -- International Conventions &
Organisations, 21 new bilingual rows against the live gap report: medium statement 8, easy
statement 3, hard statement 2, medium MCQ 2, easy MCQ 1, hard MCQ 1, medium Statement-I/II 1,
easy Statement-I/II 1, hard Statement-I/II/III 1, medium pairs 1. Concepts already in the bank
(BBNJ, CBD protocols, CMS, Kunming-Montreal GBF, Living Planet Report, Montreal-Kigali, UNEP
and Stockholm) are not repeated or cued."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Environment & Ecology"
I = "International Conventions & Organisations"
CITES = "Convention on International Trade in Endangered Species of Wild Fauna and Flora (CITES, 1973)"

# ---------------------------------------------------------------- medium statements (8)
S(I, "medium", "Consider the following statements about CITES:",
  "CITES के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Commercial international trade in species listed in Appendix I is generally prohibited.",
   "Appendix III lists species protected in at least one country that has asked other Parties for help in controlling the trade.",
   "CITES is legally binding and directly replaces the national laws of its Parties."],
  ["परिशिष्ट I में सूचीबद्ध प्रजातियों का व्यावसायिक अंतरराष्ट्रीय व्यापार सामान्यतः प्रतिबंधित है।",
   "परिशिष्ट III में वे प्रजातियाँ हैं जो कम से कम एक देश में संरक्षित हैं और जिस देश ने व्यापार नियंत्रित करने में दूसरे पक्षकारों से सहायता माँगी है।",
   "CITES कानूनी रूप से बाध्यकारी है और अपने पक्षकारों के राष्ट्रीय कानूनों की सीधे जगह ले लेता है।"],
  C3, 1,
  "Statements 1 and 2 are correct. Appendix I covers species threatened with extinction, where trade is allowed only in exceptional cases such as scientific research; Appendix II covers species that could become threatened unless trade is controlled, traded under permits; and Appendix III is added by a single country for species it protects. Listing in Appendices I and II is decided by the Conference of the Parties, but a country can add species to Appendix III on its own. "
  "Statement 3 is wrong: CITES binds its Parties, but it does not take the place of national laws; each Party must implement it through its own legislation -- in India, through the Wild Life (Protection) Act, whose 2022 amendment added a Schedule for CITES-listed specimens.",
  "कथन 1 और 2 सही हैं। परिशिष्ट I में विलुप्ति के खतरे वाली प्रजातियाँ हैं, जिनका व्यापार केवल वैज्ञानिक शोध जैसे अपवादों में होता है; परिशिष्ट II में वे प्रजातियाँ हैं जो व्यापार नियंत्रित न होने पर संकटग्रस्त हो सकती हैं, और इनका व्यापार परमिट से होता है; और परिशिष्ट III में कोई एक देश अपनी संरक्षित प्रजातियाँ जोड़ता है। परिशिष्ट I और II में सूचीबद्धता पक्षकारों का सम्मेलन तय करता है, पर परिशिष्ट III में कोई देश स्वयं प्रजातियाँ जोड़ सकता है। "
  "कथन 3 गलत है: CITES अपने पक्षकारों को बाध्य करता है, पर राष्ट्रीय कानूनों की जगह नहीं लेता; हर पक्षकार को इसे अपने कानून से लागू करना होता है; भारत में वन्यजीव (संरक्षण) अधिनियम से, जिसके 2022 के संशोधन ने CITES-सूचीबद्ध नमूनों के लिए एक अनुसूची जोड़ी।",
  f"{CITES}, Articles II to V and VIII; Wild Life (Protection) Amendment Act, 2022.",
  "env-cites-appendices")

S(I, "medium", "Consider the following statements about the United Nations Convention to Combat Desertification (UNCCD):",
  "मरुस्थलीकरण से निपटने के लिए संयुक्त राष्ट्र अभिसमय (UNCCD) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Its secretariat is in Bonn, Germany.",
   "India hosted its fourteenth Conference of the Parties (COP14) in 2019.",
   "India has set a target of restoring 26 million hectares of degraded land by 2030."],
  ["इसका सचिवालय जर्मनी के बॉन में है।",
   "भारत ने 2019 में इसके चौदहवें पक्षकार सम्मेलन (COP14) की मेज़बानी की।",
   "भारत ने 2030 तक 2.6 करोड़ हेक्टेयर क्षरित भूमि को पुनर्स्थापित करने का लक्ष्य रखा है।"],
  C3, 2,
  "All three statements are correct. The UNCCD, adopted in 1994, is one of the three 'Rio Conventions' and the only legally binding agreement linking environment and development to sustainable land management. COP14 at Greater Noida in 2019 adopted the New Delhi Declaration, and India raised its restoration target from 21 to 26 million hectares by 2030 in pursuit of 'land degradation neutrality'. "
  "The ISRO Desertification and Land Degradation Atlas estimates that close to a third of India's land is degraded.",
  "तीनों कथन सही हैं। 1994 में अपनाया गया UNCCD तीन 'रियो अभिसमयों' में से एक है और पर्यावरण तथा विकास को सतत भूमि प्रबंधन से जोड़ने वाला एकमात्र कानूनी रूप से बाध्यकारी समझौता है। 2019 में ग्रेटर नोएडा में हुए COP14 ने नई दिल्ली घोषणा अपनाई, और भारत ने 'भूमि-क्षरण तटस्थता' (land degradation neutrality) की दिशा में 2030 तक अपना पुनर्स्थापन लक्ष्य 2.1 करोड़ से बढ़ाकर 2.6 करोड़ हेक्टेयर किया। "
  "ISRO के मरुस्थलीकरण और भूमि-क्षरण एटलस के अनुसार भारत की लगभग एक-तिहाई भूमि क्षरित है।",
  "UNCCD -- COP14, New Delhi Declaration (2019); ISRO Space Applications Centre -- Desertification and Land Degradation Atlas of India.",
  "env-unccd-india")

S(I, "medium", "Consider the following statements about the chemicals and waste conventions:",
  "रसायन और अपशिष्ट संबंधी अभिसमयों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Basel Convention controls the transboundary movement of hazardous wastes and their disposal.",
   "The Rotterdam Convention aims to eliminate persistent organic pollutants.",
   "The Stockholm Convention sets up the 'prior informed consent' procedure for trade in hazardous chemicals."],
  ["बेसल अभिसमय खतरनाक अपशिष्टों की सीमा-पार आवाजाही और उनके निपटान को नियंत्रित करता है।",
   "रॉटरडैम अभिसमय का उद्देश्य स्थायी जैविक प्रदूषकों (persistent organic pollutants) को समाप्त करना है।",
   "स्टॉकहोम अभिसमय खतरनाक रसायनों के व्यापार के लिए 'पूर्व सूचित सहमति' (prior informed consent) प्रक्रिया स्थापित करता है।"],
  C3, 0,
  "Only statement 1 is correct: the Basel Convention (1989) was a response to the dumping of toxic waste from rich countries in poorer ones, and its 2019 plastic amendments brought most plastic waste under its control. "
  "Statements 2 and 3 swap the other two. The Rotterdam Convention (1998) sets up the prior informed consent procedure, under which exporters of listed hazardous pesticides and industrial chemicals must have the importing country's consent. The Stockholm Convention (2001) aims to eliminate or restrict persistent organic pollutants such as DDT, PCBs and dioxins. The three share a joint secretariat -- hence 'BRS Conventions'.",
  "केवल कथन 1 सही है: बेसल अभिसमय (1989) धनी देशों से गरीब देशों में ज़हरीला कचरा फेंके जाने की प्रतिक्रिया था, और इसके 2019 के प्लास्टिक संशोधनों ने अधिकांश प्लास्टिक कचरे को इसके नियंत्रण में ला दिया। "
  "कथन 2 और 3 बाकी दोनों की अदला-बदली करते हैं। रॉटरडैम अभिसमय (1998) पूर्व सूचित सहमति की प्रक्रिया बनाता है, जिसके तहत सूचीबद्ध खतरनाक कीटनाशकों और औद्योगिक रसायनों के निर्यातकों को आयातक देश की सहमति लेनी होती है। स्टॉकहोम अभिसमय (2001) DDT, PCB और डाइऑक्सिन जैसे स्थायी जैविक प्रदूषकों को समाप्त या सीमित करने का लक्ष्य रखता है। तीनों का साझा सचिवालय है; इसीलिए इन्हें 'BRS अभिसमय' कहते हैं।",
  "UNEP -- Secretariat of the Basel, Rotterdam and Stockholm Conventions.",
  "env-basel-rotterdam-stockholm")

S(I, "medium", "Consider the following statements about the Minamata Convention:",
  "मिनामाता अभिसमय के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It aims to protect human health and the environment from mercury.",
   "It is named after a Japanese city where industrial mercury poisoning caused a serious disease.",
   "India has ratified it."],
  ["इसका उद्देश्य मानव स्वास्थ्य और पर्यावरण को पारे (mercury) से बचाना है।",
   "इसका नाम उस जापानी शहर पर रखा गया है जहाँ औद्योगिक पारा-विषाक्तता से एक गंभीर रोग फैला था।",
   "भारत ने इसका अनुसमर्थन कर दिया है।"],
  C3, 2,
  "All three statements are correct. Adopted in 2013 and in force since 2017, the Convention controls mercury mining, trade and emissions and phases out mercury in products such as certain batteries, thermometers and lamps. It takes its name from Minamata, where a chemical factory's mercury waste, turned into methylmercury in the bay, poisoned fish-eating families from the 1950s. "
  "India ratified it in 2018. A student who remembers India's hesitation on many chemical treaties might wrongly pick 'Only two'.",
  "तीनों कथन सही हैं। 2013 में अपनाया गया और 2017 से लागू यह अभिसमय पारे के खनन, व्यापार और उत्सर्जन को नियंत्रित करता है और कुछ बैटरियों, थर्मामीटरों और लैंपों जैसे उत्पादों में पारे को समाप्त करता है। इसका नाम मिनामाता से है, जहाँ एक रासायनिक कारखाने का पारा-अपशिष्ट खाड़ी में मिथाइल-मर्करी बनकर 1950 के दशक से मछली खाने वाले परिवारों को विषाक्त करता रहा। "
  "भारत ने 2018 में इसका अनुसमर्थन किया। जो विद्यार्थी कई रसायन-संधियों पर भारत की झिझक याद रखता है, वह गलती से 'केवल दो' चुन सकता है।",
  "Minamata Convention on Mercury (2013); Ministry of Environment, Forest and Climate Change -- ratification of the Minamata Convention (2018).",
  "env-minamata-convention")

S(I, "medium", "Consider the following statements about the International Whaling Commission (IWC):",
  "अंतरराष्ट्रीय व्हेलिंग आयोग (IWC) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It was set up under the United Nations Convention on the Law of the Sea.",
   "Its moratorium on commercial whaling was lifted in 2019.",
   "India is not a member of the IWC."],
  ["इसकी स्थापना संयुक्त राष्ट्र समुद्री कानून अभिसमय (UNCLOS) के तहत हुई।",
   "व्यावसायिक व्हेल-शिकार पर इसकी रोक (moratorium) 2019 में हटा ली गई।",
   "भारत IWC का सदस्य नहीं है।"],
  C3, 3,
  "None of the statements is correct. The IWC was set up under the International Convention for the Regulation of Whaling of 1946, decades before UNCLOS (1982). Its moratorium on commercial whaling, in effect since 1986, still stands; what happened in 2019 is that Japan left the IWC and resumed commercial whaling in its own waters. "
  "India has been a member since 1981 and has supported the moratorium.",
  "कोई भी कथन सही नहीं है। IWC की स्थापना 1946 के व्हेल-शिकार नियमन अंतरराष्ट्रीय अभिसमय के तहत हुई, UNCLOS (1982) से दशकों पहले। व्यावसायिक व्हेल-शिकार पर इसकी रोक, जो 1986 से लागू है, अब भी बनी हुई है; 2019 में यह हुआ कि जापान IWC से अलग हो गया और अपने जल में व्यावसायिक व्हेल-शिकार फिर शुरू किया। "
  "भारत 1981 से सदस्य है और उसने रोक का समर्थन किया है।",
  "International Whaling Commission -- history and membership; International Convention for the Regulation of Whaling (1946).",
  "env-international-whaling-commission")

S(I, "medium", "Consider the following statements about the Global Environment Facility (GEF):",
  "वैश्विक पर्यावरण सुविधा (GEF) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It serves as a financial mechanism for several conventions, including the CBD, the UNFCCC, the UNCCD, the Stockholm Convention and the Minamata Convention.",
   "The World Bank serves as its trustee.",
   "It provides mainly loans that must be repaid with interest."],
  ["यह CBD, UNFCCC, UNCCD, स्टॉकहोम अभिसमय और मिनामाता अभिसमय सहित कई अभिसमयों के वित्तीय तंत्र के रूप में काम करती है।",
   "विश्व बैंक इसका न्यासी (trustee) है।",
   "यह मुख्य रूप से ऐसे ऋण देती है जिन्हें ब्याज सहित चुकाना होता है।"],
  C3, 1,
  "Statements 1 and 2 are correct. The GEF was set up in 1991, on the eve of the Rio Earth Summit, and now channels money for biodiversity, climate change, land degradation, international waters and chemicals and waste; UNDP, UNEP, the World Bank and other agencies implement its projects, and the World Bank holds its trust fund. "
  "Statement 3 is wrong: the GEF gives mainly grants (and some blended finance) to meet the extra cost of making a project deliver global environmental benefits; it is not a lending bank.",
  "कथन 1 और 2 सही हैं। GEF की स्थापना 1991 में रियो पृथ्वी सम्मेलन से ठीक पहले हुई, और अब यह जैव विविधता, जलवायु परिवर्तन, भूमि-क्षरण, अंतरराष्ट्रीय जल और रसायन तथा अपशिष्ट के लिए धन पहुँचाती है; UNDP, UNEP, विश्व बैंक और दूसरी एजेंसियाँ इसकी परियोजनाएँ लागू करती हैं, और विश्व बैंक इसका न्यास-कोष रखता है। "
  "कथन 3 गलत है: GEF मुख्यतः अनुदान (और कुछ मिश्रित वित्त) देती है, ताकि किसी परियोजना को वैश्विक पर्यावरणीय लाभ देने लायक बनाने का अतिरिक्त खर्च पूरा हो; यह ऋण देने वाला बैंक नहीं है।",
  "Global Environment Facility -- Instrument for the Establishment of the Restructured GEF; GEF Trust Fund (World Bank as trustee).",
  "env-global-environment-facility")

S(I, "medium", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The International Union for Conservation of Nature (IUCN) is headquartered at Gland, Switzerland.",
   "TRAFFIC, the wildlife trade monitoring network, is a United Nations agency.",
   "The IUCN is a specialised agency of the United Nations."],
  ["अंतरराष्ट्रीय प्रकृति संरक्षण संघ (IUCN) का मुख्यालय स्विट्ज़रलैंड के ग्लैंड में है।",
   "वन्यजीव व्यापार की निगरानी करने वाला नेटवर्क TRAFFIC संयुक्त राष्ट्र की एक एजेंसी है।",
   "IUCN संयुक्त राष्ट्र की एक विशिष्ट एजेंसी है।"],
  C3, 0,
  "Only statement 1 is correct. The IUCN, founded in 1948, is a membership union of both governments and non-governmental organisations, which is what makes it unusual; it has observer status at the UN General Assembly but is not a UN agency. It publishes the Red List and advises UNESCO on natural World Heritage Sites. "
  "TRAFFIC is a non-governmental organisation, founded in 1976 by WWF and IUCN, that monitors wildlife trade and supports the implementation of CITES; it has an office in India.",
  "केवल कथन 1 सही है। 1948 में स्थापित IUCN सरकारों और गैर-सरकारी संगठनों, दोनों का सदस्यता-संघ है, और यही इसे असामान्य बनाता है; इसे संयुक्त राष्ट्र महासभा में पर्यवेक्षक का दर्जा है, पर यह UN एजेंसी नहीं है। यह रेड लिस्ट प्रकाशित करता है और प्राकृतिक विश्व धरोहर स्थलों पर UNESCO को सलाह देता है। "
  "TRAFFIC एक गैर-सरकारी संगठन है, जिसे 1976 में WWF और IUCN ने स्थापित किया, और जो वन्यजीव व्यापार की निगरानी करता है और CITES के कार्यान्वयन में सहायता करता है; इसका भारत में भी कार्यालय है।",
  "IUCN -- About IUCN; TRAFFIC -- the wildlife trade monitoring network.",
  "env-iucn-traffic-status")

S(I, "medium", "Consider the following statements about the negotiations for a global treaty on plastic pollution:",
  "प्लास्टिक प्रदूषण पर एक वैश्विक संधि के लिए हुई वार्ताओं के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["They were launched by a resolution of the United Nations Environment Assembly in March 2022.",
   "The negotiations concluded with an agreed treaty text at Busan in 2024.",
   "The treaty has entered into force."],
  ["इनकी शुरुआत मार्च 2022 में संयुक्त राष्ट्र पर्यावरण सभा के एक प्रस्ताव से हुई।",
   "ये वार्ताएँ 2024 में बुसान में एक सहमत संधि-पाठ के साथ पूरी हुईं।",
   "यह संधि लागू हो चुकी है।"],
  C3, 0,
  "Only statement 1 is correct: UNEA resolution 5/14 (Nairobi, March 2022) set up an Intergovernmental Negotiating Committee to draft a legally binding instrument on plastic pollution, covering the full life cycle of plastic. "
  "Statements 2 and 3 are wrong: the fifth session at Busan in late 2024 and its resumed session at Geneva in August 2025 both ended without agreement, mainly over whether to cap the production of new plastic -- pressed by a 'high ambition coalition' and resisted by oil- and plastic-producing countries. There is no treaty in force.",
  "केवल कथन 1 सही है: UNEA प्रस्ताव 5/14 (नैरोबी, मार्च 2022) ने प्लास्टिक के पूरे जीवन-चक्र को शामिल करते हुए प्लास्टिक प्रदूषण पर कानूनी रूप से बाध्यकारी साधन का मसौदा बनाने के लिए एक अंतर-सरकारी वार्ता समिति बनाई। "
  "कथन 2 और 3 गलत हैं: 2024 के अंत में बुसान में हुआ पाँचवाँ सत्र और अगस्त 2025 में जिनेवा में उसका पुनः आरंभ हुआ सत्र, दोनों बिना सहमति के समाप्त हुए, मुख्यतः इस पर कि क्या नए प्लास्टिक के उत्पादन पर सीमा लगाई जाए; 'उच्च महत्त्वाकांक्षा गठबंधन' इस पर ज़ोर दे रहा था और तेल तथा प्लास्टिक उत्पादक देश इसका विरोध कर रहे थे। कोई संधि लागू नहीं है।",
  "UNEP -- UNEA resolution 5/14, End plastic pollution: towards an international legally binding instrument (2022); Intergovernmental Negotiating Committee on Plastic Pollution, INC-5 (Busan, 2024) and INC-5.2 (Geneva, 2025).",
  "env-global-plastics-treaty")

# ---------------------------------------------------------------- easy statements (3)
S(I, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["World Environment Day is observed on 5 June.",
   "The Republic of Korea hosted World Environment Day in 2025, with plastic pollution as its theme."],
  ["विश्व पर्यावरण दिवस 5 जून को मनाया जाता है।",
   "कोरिया गणराज्य ने 2025 में विश्व पर्यावरण दिवस की मेज़बानी की, जिसका विषय प्लास्टिक प्रदूषण था।"],
  T2, 2,
  "Both statements are correct. World Environment Day, led by UNEP, has been observed on 5 June since 1973; each year a host country and a theme are chosen. In 2025 the Republic of Korea hosted it with the theme of ending plastic pollution, the same theme India had led as host in 2018 ('Beat Plastic Pollution').",
  "दोनों कथन सही हैं। UNEP के नेतृत्व में विश्व पर्यावरण दिवस 1973 से 5 जून को मनाया जाता है; हर वर्ष एक मेज़बान देश और एक विषय चुना जाता है। 2025 में कोरिया गणराज्य ने प्लास्टिक प्रदूषण समाप्त करने के विषय के साथ इसकी मेज़बानी की; यही विषय भारत ने 2018 में मेज़बान के रूप में उठाया था ('Beat Plastic Pollution')।",
  "UNEP -- World Environment Day (host countries and themes).",
  "env-world-environment-day")

S(I, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Earth Summit of 1992 was held in Rio de Janeiro.",
   "The Kyoto Protocol was adopted at the Earth Summit."],
  ["1992 का पृथ्वी सम्मेलन रियो डी जनेरियो में हुआ था।",
   "क्योटो प्रोटोकॉल पृथ्वी सम्मेलन में अपनाया गया था।"],
  T2, 0,
  "Only statement 1 is correct. The UN Conference on Environment and Development (Rio, 1992) produced the Rio Declaration, Agenda 21 and the Forest Principles, and opened the UNFCCC and the CBD for signature; the UNCCD followed in 1994. "
  "Statement 2 is wrong: the Kyoto Protocol was adopted five years later, at the third Conference of the Parties to the UNFCCC in Kyoto in 1997.",
  "केवल कथन 1 सही है। संयुक्त राष्ट्र पर्यावरण और विकास सम्मेलन (रियो, 1992) से रियो घोषणा, एजेंडा 21 और वन सिद्धांत निकले, और UNFCCC तथा CBD हस्ताक्षर के लिए खोले गए; UNCCD 1994 में आया। "
  "कथन 2 गलत है: क्योटो प्रोटोकॉल पाँच वर्ष बाद, 1997 में क्योटो में UNFCCC के तीसरे पक्षकार सम्मेलन में अपनाया गया।",
  "United Nations Conference on Environment and Development (Rio de Janeiro, 1992); NCERT Class XII, Political Science -- Contemporary World Politics (Environment and Natural Resources).",
  "env-earth-summit-rio")

S(I, "easy", "Consider the following statements about the UN Decade on Ecosystem Restoration:",
  "पारितंत्र पुनर्स्थापन पर संयुक्त राष्ट्र दशक (UN Decade on Ecosystem Restoration) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It covers the years 2021 to 2030.",
   "It is led by UNEP and the Food and Agriculture Organization.",
   "It was declared by the UN Security Council."],
  ["यह 2021 से 2030 तक के वर्षों को शामिल करता है।",
   "इसका नेतृत्व UNEP और खाद्य और कृषि संगठन (FAO) करते हैं।",
   "इसकी घोषणा संयुक्त राष्ट्र सुरक्षा परिषद ने की थी।"],
  C3, 1,
  "Statements 1 and 2 are correct. The Decade aims to prevent, halt and reverse the degradation of ecosystems -- forests, farmland, wetlands, oceans, cities -- and runs alongside the deadline of the Sustainable Development Goals. "
  "Statement 3 is wrong: it was proclaimed by the UN General Assembly in 2019; environmental matters of this kind do not come before the Security Council.",
  "कथन 1 और 2 सही हैं। यह दशक वनों, खेतों, आर्द्रभूमियों, महासागरों और शहरों जैसे पारितंत्रों के क्षरण को रोकने और उलटने का लक्ष्य रखता है, और सतत विकास लक्ष्यों की समय-सीमा के साथ चलता है। "
  "कथन 3 गलत है: इसकी घोषणा 2019 में संयुक्त राष्ट्र महासभा ने की थी; इस प्रकार के पर्यावरणीय विषय सुरक्षा परिषद के सामने नहीं आते।",
  "UN General Assembly resolution 73/284 (2019), United Nations Decade on Ecosystem Restoration (2021-2030).",
  "env-un-decade-ecosystem-restoration")

# ---------------------------------------------------------------- hard statements (2)
S(I, "hard", "Consider the following statements about the Intergovernmental Science-Policy Platform on Biodiversity and Ecosystem Services (IPBES):",
  "जैव विविधता और पारितंत्र सेवाओं पर अंतर-सरकारी विज्ञान-नीति मंच (IPBES) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is often described as the biodiversity counterpart of the IPCC.",
   "It was established in 2012.",
   "Its secretariat is in Bonn, Germany.",
   "Its 2019 Global Assessment estimated that about one million species are threatened with extinction."],
  ["इसे प्रायः IPCC का जैव विविधता वाला प्रतिरूप कहा जाता है।",
   "इसकी स्थापना 2012 में हुई।",
   "इसका सचिवालय जर्मनी के बॉन में है।",
   "इसके 2019 के वैश्विक आकलन ने अनुमान लगाया कि लगभग दस लाख प्रजातियों पर विलुप्ति का खतरा है।"],
  C4, 3,
  "All four statements are correct. IPBES, set up at Panama City in 2012, does for nature what the IPCC does for climate: it assesses the evidence for governments rather than doing new research. Its 2019 Global Assessment found that about a million animal and plant species face extinction, many within decades, and ranked the direct drivers -- changes in land and sea use, direct exploitation, climate change, pollution and invasive species. "
  "The later 'nexus' and 'transformative change' assessments (2024) link biodiversity with water, food, health and climate. A student who expects one statement in four to be false will fall for 'Only three'.",
  "चारों कथन सही हैं। 2012 में पनामा सिटी में स्थापित IPBES प्रकृति के लिए वही करता है जो IPCC जलवायु के लिए: यह नया शोध करने के बजाय सरकारों के लिए साक्ष्यों का आकलन करता है। इसके 2019 के वैश्विक आकलन ने पाया कि लगभग दस लाख जंतु और पौधा प्रजातियाँ विलुप्ति के खतरे में हैं, कई तो कुछ दशकों में, और प्रत्यक्ष कारकों को क्रम दिया: भूमि और समुद्र के उपयोग में बदलाव, प्रत्यक्ष दोहन, जलवायु परिवर्तन, प्रदूषण और आक्रामक प्रजातियाँ। "
  "बाद के 'नेक्सस' और 'रूपांतरकारी परिवर्तन' आकलन (2024) जैव विविधता को जल, भोजन, स्वास्थ्य और जलवायु से जोड़ते हैं। जो विद्यार्थी मानता है कि चार में से एक कथन गलत होगा ही, वह 'केवल तीन' के जाल में फँसेगा।",
  "IPBES -- Global Assessment Report on Biodiversity and Ecosystem Services (2019); IPBES Nexus and Transformative Change Assessments (2024).",
  "env-ipbes")

S(I, "hard", "Consider the following statements about the Antarctic Treaty system:",
  "अंटार्कटिक संधि प्रणाली के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Antarctic Treaty was signed in 1959.",
   "The Madrid Protocol prohibits any activity relating to mineral resources in Antarctica, other than scientific research.",
   "India's research stations in Antarctica include Maitri and Himadri.",
   "The Antarctic Treaty allows military bases in Antarctica, provided they are used only for defence."],
  ["अंटार्कटिक संधि पर 1959 में हस्ताक्षर हुए।",
   "मैड्रिड प्रोटोकॉल वैज्ञानिक शोध को छोड़कर अंटार्कटिका में खनिज संसाधनों से संबंधित किसी भी गतिविधि पर रोक लगाता है।",
   "अंटार्कटिका में भारत के शोध केंद्रों में मैत्री और हिमाद्रि शामिल हैं।",
   "अंटार्कटिक संधि अंटार्कटिका में सैन्य अड्डों की अनुमति देती है, बशर्ते उनका उपयोग केवल रक्षा के लिए हो।"],
  C4, 1,
  "Statements 1 and 2 are correct. The Treaty, signed in Washington in 1959, sets Antarctica aside for peace and science and freezes territorial claims; the Protocol on Environmental Protection (Madrid, 1991) designates it a 'natural reserve, devoted to peace and science' and bans mining. India, a consultative party since 1983, passed the Indian Antarctic Act in 2022 to give domestic force to these obligations. "
  "Statement 3 is the trap: India's Antarctic stations are Maitri and Bharati (the first, Dakshin Gangotri, is now a supply base); Himadri is India's Arctic station, at Ny-Alesund in Svalbard. "
  "Statement 4 is wrong: the Treaty prohibits military bases, manoeuvres and weapons testing; military personnel and equipment may be used only for scientific or other peaceful purposes.",
  "कथन 1 और 2 सही हैं। 1959 में वॉशिंगटन में हस्ताक्षरित संधि अंटार्कटिका को शांति और विज्ञान के लिए अलग रखती है और क्षेत्रीय दावों को स्थगित करती है; पर्यावरण संरक्षण प्रोटोकॉल (मैड्रिड, 1991) इसे 'शांति और विज्ञान को समर्पित प्राकृतिक आरक्षित क्षेत्र' घोषित करता है और खनन पर रोक लगाता है। 1983 से परामर्शदात्री पक्षकार भारत ने इन दायित्वों को देश के भीतर लागू करने के लिए 2022 में भारतीय अंटार्कटिक अधिनियम पारित किया। "
  "कथन 3 जाल है: अंटार्कटिका में भारत के केंद्र मैत्री और भारती हैं (पहला, दक्षिण गंगोत्री, अब आपूर्ति अड्डा है); हिमाद्रि भारत का आर्कटिक केंद्र है, जो स्वालबार्ड के नी-आलेसुंड में है। "
  "कथन 4 गलत है: संधि सैन्य अड्डों, सैन्य अभ्यासों और हथियार परीक्षण पर रोक लगाती है; सैन्य कर्मियों और उपकरणों का उपयोग केवल वैज्ञानिक या दूसरे शांतिपूर्ण उद्देश्यों के लिए हो सकता है।",
  "Antarctic Treaty (1959), Article I; Protocol on Environmental Protection to the Antarctic Treaty (1991), Articles 2 and 7; Indian Antarctic Act, 2022; National Centre for Polar and Ocean Research.",
  "env-antarctic-treaty-system")

# ---------------------------------------------------------------- MCQs (4)
M(I, "medium", "The 'Bonn Challenge' is a global goal to:",
  "'बॉन चैलेंज' एक वैश्विक लक्ष्य है:",
  ["Restore 350 million hectares of degraded land by 2030", "Protect 30 per cent of the world's oceans as marine reserves by 2030",
   "Phase out unabated coal power in rich countries by 2035", "Halve food loss and waste across the world by 2030"],
  ["2030 तक 35 करोड़ हेक्टेयर क्षरित भूमि को पुनर्स्थापित करना", "2030 तक विश्व के 30 प्रतिशत महासागरों को समुद्री आरक्षित क्षेत्रों के रूप में संरक्षित करना",
   "2035 तक धनी देशों में बिना नियंत्रण वाली कोयला-बिजली को समाप्त करना", "2030 तक पूरे विश्व में भोजन की हानि और बर्बादी को आधा करना"],
  0,
  "Launched by Germany and the IUCN in 2011, the Bonn Challenge set out to bring 150 million hectares of deforested and degraded land into restoration by 2020 and 350 million by 2030. India joined in 2015 and later raised its pledge to 26 million hectares by 2030, the same figure as its land degradation neutrality target. "
  "The distractors echo other goals -- '30x30' of the Kunming-Montreal framework (which covers land as well as sea), coal phase-out debates and SDG 12.3 on food waste.",
  "2011 में जर्मनी और IUCN द्वारा शुरू किए गए बॉन चैलेंज का लक्ष्य 2020 तक 15 करोड़ हेक्टेयर और 2030 तक 35 करोड़ हेक्टेयर वनोन्मूलित और क्षरित भूमि का पुनर्स्थापन शुरू करना था। भारत 2015 में इसमें शामिल हुआ और बाद में अपना संकल्प बढ़ाकर 2030 तक 2.6 करोड़ हेक्टेयर किया, जो उसके भूमि-क्षरण तटस्थता लक्ष्य के बराबर है। "
  "गलत विकल्प दूसरे लक्ष्यों की गूँज हैं: कुनमिंग-मॉन्ट्रियल ढाँचे का '30x30' (जो समुद्र के साथ भूमि को भी शामिल करता है), कोयला समाप्त करने की बहसें और भोजन की बर्बादी पर SDG 12.3।",
  "IUCN -- The Bonn Challenge; Ministry of Environment, Forest and Climate Change -- India's Bonn Challenge pledge.",
  "env-bonn-challenge")

M(I, "medium", "Which one of the following is NOT one of the three 'Rio Conventions'?",
  "निम्नलिखित में से कौन-सा तीन 'रियो अभिसमयों' में से एक नहीं है?",
  ["Ramsar Convention on Wetlands", "UN Framework Convention on Climate Change", "Convention on Biological Diversity", "UN Convention to Combat Desertification"],
  ["आर्द्रभूमियों पर रामसर अभिसमय", "जलवायु परिवर्तन पर संयुक्त राष्ट्र ढाँचा अभिसमय", "जैव विविधता पर अभिसमय", "मरुस्थलीकरण से निपटने के लिए संयुक्त राष्ट्र अभिसमय"],
  0,
  "The three Rio Conventions -- the UNFCCC, the CBD and the UNCCD -- grew directly out of the 1992 Earth Summit, and they share a joint liaison group. The Ramsar Convention is much older (1971) and was negotiated outside the UN system; it is one of the 'biodiversity-related conventions', along with CITES, CMS and the World Heritage Convention.",
  "तीन रियो अभिसमय, यानी UNFCCC, CBD और UNCCD, सीधे 1992 के पृथ्वी सम्मेलन से निकले, और इनका एक संयुक्त संपर्क समूह है। रामसर अभिसमय कहीं पुराना (1971) है और संयुक्त राष्ट्र प्रणाली के बाहर तय हुआ था; यह CITES, CMS और विश्व धरोहर अभिसमय के साथ 'जैव विविधता से संबंधित अभिसमयों' में से एक है।",
  "UNFCCC, CBD and UNCCD -- Joint Liaison Group of the Rio Conventions; Ramsar Convention Secretariat.",
  "env-rio-conventions")

M(I, "easy", "'Earth Hour', during which people switch off non-essential lights for an hour, is an initiative of:",
  "'अर्थ आवर', जिसमें लोग एक घंटे के लिए गैर-ज़रूरी बत्तियाँ बुझाते हैं, किसकी पहल है?",
  ["WWF", "UNEP", "IUCN", "Greenpeace"],
  ["WWF", "UNEP", "IUCN", "ग्रीनपीस"],
  0,
  "Earth Hour was started by WWF in Sydney in 2007 and is held on a Saturday in late March each year; it is meant to draw attention to climate change and nature loss rather than to save much electricity. UNEP leads World Environment Day, and the IUCN publishes the Red List.",
  "अर्थ आवर WWF ने 2007 में सिडनी में शुरू किया था और यह हर वर्ष मार्च के अंत के एक शनिवार को होता है; इसका उद्देश्य बहुत बिजली बचाना नहीं, बल्कि जलवायु परिवर्तन और प्रकृति की हानि की ओर ध्यान खींचना है। विश्व पर्यावरण दिवस का नेतृत्व UNEP करता है, और IUCN रेड लिस्ट प्रकाशित करता है।",
  "WWF -- Earth Hour.",
  "env-earth-hour-wwf")

M(I, "hard", "The 'Cali Fund', set up under the Convention on Biological Diversity at COP16 in 2024, is meant to receive contributions from:",
  "2024 में COP16 में जैव विविधता पर अभिसमय के तहत स्थापित 'काली फ़ंड' (Cali Fund) में किनसे योगदान अपेक्षित है?",
  ["Companies that use digital sequence information on genetic resources", "Countries that fail to meet their national 30-by-30 protected-area targets",
   "Airlines, through a small levy on international air tickets", "Fossil fuel companies, through a tax on windfall profits"],
  ["आनुवंशिक संसाधनों की डिजिटल अनुक्रम सूचना (DSI) का उपयोग करने वाली कंपनियों से", "अपने 30-बाय-30 संरक्षित-क्षेत्र लक्ष्य पूरे न करने वाले देशों से",
   "एयरलाइनों से, अंतरराष्ट्रीय हवाई टिकटों पर छोटे शुल्क के ज़रिए", "जीवाश्म ईंधन कंपनियों से, आकस्मिक लाभ (windfall) पर कर के ज़रिए"],
  0,
  "Digital sequence information -- genetic sequences of plants, animals and microbes stored in online databases -- is used by pharmaceutical, cosmetics, agricultural and biotech firms, often without any benefit going back to the countries and communities from which the organisms came. The Cali Fund, launched in 2025, asks large companies using DSI to contribute a share of their profits or revenue, with at least half of the money meant for Indigenous peoples and local communities. "
  "It extends the 'access and benefit-sharing' idea of the Nagoya Protocol from physical samples to digital data; contributions are voluntary, which critics see as its weakness.",
  "डिजिटल अनुक्रम सूचना, यानी पौधों, जंतुओं और सूक्ष्मजीवों के ऑनलाइन डेटाबेस में रखे आनुवंशिक अनुक्रम, का उपयोग दवा, सौंदर्य-प्रसाधन, कृषि और जैव-प्रौद्योगिकी कंपनियाँ करती हैं, प्रायः उन देशों और समुदायों को कोई लाभ लौटाए बिना जहाँ से वे जीव आए। 2025 में शुरू हुआ काली फ़ंड DSI का उपयोग करने वाली बड़ी कंपनियों से अपने लाभ या राजस्व का एक हिस्सा देने को कहता है, जिसमें से कम से कम आधा धन मूलनिवासी लोगों और स्थानीय समुदायों के लिए है। "
  "यह नागोया प्रोटोकॉल के 'पहुँच और लाभ-साझाकरण' के विचार को भौतिक नमूनों से डिजिटल आँकड़ों तक बढ़ाता है; योगदान स्वैच्छिक हैं, जिसे आलोचक इसकी कमज़ोरी मानते हैं।",
  "Convention on Biological Diversity -- decision 16/2 on digital sequence information (COP16, Cali, 2024); launch of the Cali Fund (2025).",
  "env-cali-fund-dsi")

# ---------------------------------------------------------------- Statement-I/II (medium, easy), I/II/III (hard)
A(I, "medium",
  "CITES does not by itself protect the habitats of the species it lists.",
  "CITES अपने-आप में उन प्रजातियों के आवासों की रक्षा नहीं करता जिन्हें वह सूचीबद्ध करता है।",
  "The CITES Secretariat is administered by UNEP and is located in Geneva.",
  "CITES सचिवालय UNEP द्वारा प्रशासित है और जिनेवा में स्थित है।",
  1,
  "Both statements are correct, but Statement-II does not explain Statement-I. CITES regulates only international trade in specimens -- live animals and plants and products such as ivory, skins and timber; habitat loss, domestic trade and poaching for local markets are outside its reach and must be tackled by national laws and other treaties such as the CBD and Ramsar. "
  "Where its secretariat sits, and who administers it, is a separate fact that says nothing about the Convention's scope.",
  "दोनों कथन सही हैं, पर कथन-II कथन-I की व्याख्या नहीं करता। CITES केवल नमूनों, यानी जीवित जंतुओं और पौधों तथा हाथीदाँत, खाल और लकड़ी जैसे उत्पादों, के अंतरराष्ट्रीय व्यापार को नियंत्रित करता है; आवास की हानि, घरेलू व्यापार और स्थानीय बाज़ारों के लिए शिकार इसकी पहुँच से बाहर हैं और राष्ट्रीय कानूनों तथा CBD और रामसर जैसी दूसरी संधियों से निपटाए जाने चाहिए। "
  "इसका सचिवालय कहाँ है और उसे कौन प्रशासित करता है, यह एक अलग तथ्य है, जो अभिसमय के दायरे के बारे में कुछ नहीं बताता।",
  f"{CITES}, Articles I and II.",
  "env-cites-trade-not-habitat")

A(I, "easy",
  "World Wildlife Day is observed on 3 March.",
  "विश्व वन्यजीव दिवस 3 मार्च को मनाया जाता है।",
  "CITES was signed on 3 March 1973.",
  "CITES पर 3 मार्च 1973 को हस्ताक्षर हुए थे।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I. The UN General Assembly proclaimed World Wildlife Day in 2013 and chose 3 March because it is the anniversary of the signing of CITES; the CITES Secretariat facilitates its observance each year.",
  "दोनों कथन सही हैं, और कथन-II कथन-I की व्याख्या करता है। संयुक्त राष्ट्र महासभा ने 2013 में विश्व वन्यजीव दिवस घोषित किया और 3 मार्च इसलिए चुना कि यह CITES पर हस्ताक्षर की वर्षगाँठ है; हर वर्ष CITES सचिवालय इसके आयोजन में सहायता करता है।",
  "UN General Assembly resolution 68/205 (2013), World Wildlife Day.",
  "env-world-wildlife-day-cites")

A(I, "hard",
  "The Antarctic ozone hole is expected to recover only slowly, over several decades.",
  "अंटार्कटिक ओज़ोन छिद्र के कई दशकों में, धीरे-धीरे ही ठीक होने की आशा है।",
  "Emissions of ozone-depleting substances have fallen sharply under the Montreal Protocol.",
  "मॉन्ट्रियल प्रोटोकॉल के तहत ओज़ोन-क्षयकारी पदार्थों का उत्सर्जन तेज़ी से घटा है।",
  2,
  "Only one of Statements II and III is correct -- Statement II -- and it explains Statement I. Because emissions of CFCs and halons have been cut by about 99 per cent, the ozone layer is recovering; the WMO and UNEP assessment expects the Antarctic ozone hole to close around 2066. "
  "Statement III is wrong, and its opposite is the reason recovery is slow: CFCs are very stable and stay in the atmosphere for decades to a century, so chlorine released decades ago is still destroying ozone today.",
  "कथन-II और कथन-III में से केवल एक, कथन-II, सही है और वह कथन-I की व्याख्या करता है। CFC और हैलॉन के उत्सर्जन में लगभग 99 प्रतिशत कटौती के कारण ओज़ोन परत ठीक हो रही है; WMO और UNEP का आकलन अंटार्कटिक ओज़ोन छिद्र के लगभग 2066 तक भर जाने की आशा करता है। "
  "कथन-III गलत है, और उसका उलटा ही धीमी भरपाई का कारण है: CFC बहुत स्थिर हैं और वायुमंडल में दशकों से सौ वर्ष तक रहते हैं, इसलिए दशकों पहले निकला क्लोरीन आज भी ओज़ोन नष्ट कर रहा है।",
  "WMO/UNEP -- Scientific Assessment of Ozone Depletion: 2022; UNEP Ozone Secretariat -- Montreal Protocol.",
  "env-ozone-recovery-slow",
  s3="Chlorine from these substances leaves the stratosphere within a few months of their release.",
  s3_hi="इन पदार्थों का क्लोरीन निकलने के कुछ महीनों के भीतर समतापमंडल से बाहर चला जाता है।")

# ---------------------------------------------------------------- pairs (1, medium)
P(I, "medium", "Consider the following pairs of reports and the organisations that publish them:",
  "रिपोर्टों और उन्हें प्रकाशित करने वाले संगठनों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Emissions Gap Report : UNEP", "Global Forest Resources Assessment : FAO", "World Energy Outlook : International Energy Agency", "Global Environment Outlook : UNEP"],
  ["उत्सर्जन अंतराल रिपोर्ट (Emissions Gap Report) : UNEP", "वैश्विक वन संसाधन आकलन : FAO", "विश्व ऊर्जा परिदृश्य (World Energy Outlook) : अंतरराष्ट्रीय ऊर्जा एजेंसी", "वैश्विक पर्यावरण परिदृश्य (Global Environment Outlook) : UNEP"],
  3,
  "All four pairs are correct. UNEP's annual Emissions Gap Report measures the gap between the emissions countries have pledged and those needed for 1.5 or 2 degrees; the FAO's Global Forest Resources Assessment, every five years, is the main source on world forest area; the IEA publishes the World Energy Outlook; and UNEP's Global Environment Outlook is its flagship assessment of the state of the global environment. "
  "The pattern of these pairs tempts students to assume one must be a mismatch, and two are by the same body.",
  "चारों युग्म सही हैं। UNEP की वार्षिक उत्सर्जन अंतराल रिपोर्ट देशों के संकल्पित उत्सर्जन और 1.5 या 2 डिग्री के लिए ज़रूरी उत्सर्जन के बीच का अंतर मापती है; FAO का हर पाँच वर्ष पर होने वाला वैश्विक वन संसाधन आकलन विश्व के वन क्षेत्र का मुख्य स्रोत है; IEA विश्व ऊर्जा परिदृश्य प्रकाशित करती है; और UNEP का वैश्विक पर्यावरण परिदृश्य वैश्विक पर्यावरण की स्थिति का उसका प्रमुख आकलन है। "
  "इन युग्मों का पैटर्न विद्यार्थियों को यह मानने के लिए ललचाता है कि एक बेमेल होगा ही, और दो एक ही संस्था के हैं।",
  "UNEP -- Emissions Gap Report and Global Environment Outlook; FAO -- Global Forest Resources Assessment; International Energy Agency -- World Energy Outlook.",
  "env-environment-reports-pairs")

if __name__ == "__main__":
    write("env_l2_t11_conventions.sql")
