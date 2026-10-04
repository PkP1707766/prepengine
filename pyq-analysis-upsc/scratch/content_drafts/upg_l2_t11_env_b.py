# -*- coding: utf-8 -*-
"""Level 2 · Test 11 (Environment 3) -- depth audit of 2026-10-04, part B: Protected Areas & Wildlife Protection,
and the craft tags for the 69 kept rows (docs/upsc-question-design-standard.md §6). Part A is
upg_l2_t11_env_a.py.

Part B rewrites 18 recall rows in place with the same concept id, type and difficulty. Location and
date facts now carry the reason behind them:
  - why the hornbill nest programme pays former hunters, what the Soligas' rights inside BRT show, and why
    Silent Valley mattered; India's three biogeographic realms; Keoladeo's dependence on outside water;
  - how a highway through a sanctuary needs the wildlife board; what blindness and barrages mean for river
    dolphins; why rhinos were spread out; the Ithai barrage and the phumdis; leopards at Kuno;
  - why Chipko villagers hugged trees, why the east coast has few reefs, and salinity in the Sundarbans;
    mangroves in the 1999 cyclone, a one-island hornbill, and Hemis' prey base; captive elephants as
    Schedule I property, and Simlipal's black tigers as a sign of isolation.
Test 11 after both parts: analytic 38, precision 36, recall 30.
Leaks avoided while drafting:
  - 'corridors allow gene flow' in a Terai Arc stem (answers the tiger-corridors AR, so that row was left);
  - cheetahs as open-grassland hunters (the cheetah-extinction AR's Statement III states their habitat);
  - Keoladeo on the Montreux Record (supports the Ramsar-Montreux row's statement 3);
  - the Nilgiri Biosphere Reserve reaching Kerala (answers the biosphere-reserves row's statement 3)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write_updates, CODE
from polity_common import C3, C4, T2

d.SUBJECT = "Environment & Ecology"
d.REQUIRE_CRAFT = True
PA = "Protected Areas & Wildlife Protection"
MOEF = "Ministry of Environment, Forest and Climate Change"
WPA = "Wild Life (Protection) Act, 1972, as amended in 2022."

# ================================================================ MCQs (3)
M(PA, "medium", "In the Hornbill Nest Adoption Programme around Pakke Tiger Reserve in Arunachal Pradesh, men of the Nyishi community, who once hunted hornbills, are paid to find and guard nests through the breeding season. The idea behind the programme is that:",
  "अरुणाचल प्रदेश के पक्के बाघ अभयारण्य के आसपास 'हॉर्नबिल नेस्ट एडॉप्शन प्रोग्राम' में न्यीशी समुदाय के वे लोग, जो कभी धनेशों का शिकार करते थे, प्रजनन-काल भर घोंसले खोजने और उनकी रखवाली के लिए भुगतान पाते हैं। इस कार्यक्रम के पीछे विचार यह है कि:",
  ["giving local people a stake in the birds' survival turns former hunters into protectors",
   "fencing off the nesting trees keeps all people out of the forest during the breeding season",
   "hornbills breed better in captivity, so the guarded eggs are later moved to zoos for rearing",
   "paying for nests lets the forest department avoid having to declare the area a protected area"],
  ["स्थानीय लोगों को पक्षियों के बचे रहने में हिस्सेदारी देने से पूर्व शिकारी रक्षक बन जाते हैं",
   "घोंसलों वाले वृक्षों की बाड़बंदी प्रजनन-काल में सभी लोगों को वन से बाहर रखती है",
   "धनेश बंदी अवस्था में बेहतर प्रजनन करते हैं, इसलिए रखवाली वाले अंडे बाद में पालने के लिए चिड़ियाघरों में ले जाए जाते हैं",
   "घोंसलों के लिए भुगतान से वन विभाग को क्षेत्र को संरक्षित क्षेत्र घोषित करने से बचने का अवसर मिलता है"],
  0,
  "Started in 2011 by the Nature Conservation Foundation, the Arunachal Forest Department and the Ghora-Aabhe Society, a council of Nyishi village heads, the programme pays nest protectors -- often former hunters who know where the nest trees are -- and invites people across India to 'adopt' a nest to fund them. "
  "It works because it gives the community an income that depends on the hornbills surviving. It adds to the tiger reserve rather than replacing it, and the birds breed in the wild.",
  "2011 में नेचर कंज़र्वेशन फ़ाउंडेशन, अरुणाचल वन विभाग और न्यीशी ग्राम-प्रधानों की परिषद घोरा-आबे सोसाइटी द्वारा शुरू किया गया यह कार्यक्रम घोंसलों के रक्षकों को भुगतान करता है, जो प्रायः ऐसे पूर्व शिकारी होते हैं जिन्हें घोंसलों वाले वृक्षों का पता होता है, और पूरे भारत के लोगों को उनके ख़र्च के लिए किसी घोंसले को 'गोद लेने' का निमंत्रण देता है। "
  "यह इसलिए सफल है कि समुदाय को ऐसी आय मिलती है जो धनेशों के बचे रहने पर निर्भर है। यह बाघ अभयारण्य का स्थान नहीं लेता, उसका पूरक है, और पक्षी जंगल में ही प्रजनन करते हैं।",
  "Nature Conservation Foundation -- Hornbill Nest Adoption Programme.", "env-hornbill-nest-adoption-pakke", craft="linkage")

M(PA, "medium", "In 2011 the Soliga people of the Biligiri Rangaswamy Temple (BRT) Tiger Reserve in Karnataka became the first community living inside a tiger reserve to have their community forest rights formally recognised, and the reserve's tiger population has since grown. This case is most often cited as evidence that:",
  "2011 में कर्नाटक के बिलिगिरि रंगास्वामी मंदिर (BRT) बाघ अभयारण्य के सोलिगा लोग बाघ अभयारण्य के भीतर रहने वाला ऐसा पहला समुदाय बने जिनके सामुदायिक वन अधिकारों को औपचारिक मान्यता मिली, और तब से अभयारण्य में बाघों की संख्या बढ़ी है। इस मामले को प्रायः किस बात के प्रमाण के रूप में उद्धृत किया जाता है?",
  ["recognising people's forest rights need not undermine tiger conservation",
   "tiger reserves can protect tigers only after all the people living in them are moved out",
   "the Forest Rights Act does not apply to any land that lies inside a notified tiger reserve",
   "tigers do best where tribal communities are allowed to hunt deer and other prey"],
  ["लोगों के वन अधिकारों की मान्यता से बाघ संरक्षण कमज़ोर होना आवश्यक नहीं",
   "बाघ अभयारण्य बाघों की रक्षा तभी कर सकते हैं जब उनमें रहने वाले सभी लोगों को बाहर कर दिया जाए",
   "वन अधिकार अधिनियम अधिसूचित बाघ अभयारण्य के भीतर की किसी भूमि पर लागू नहीं होता",
   "बाघ वहाँ सबसे अच्छी तरह पनपते हैं जहाँ जनजातीय समुदायों को हिरण और अन्य शिकार मारने की अनुमति हो"],
  0,
  "The Soligas, who have lived in the BRT hills for centuries, won rights under the Forest Rights Act to collect minor forest produce, manage their forests and continue traditional practices while remaining inside the reserve. Camera-trap estimates since then have shown tiger numbers rising, so the case is used against the view that conservation requires removing people. "
  "The Forest Rights Act does apply inside tiger reserves, and hunting is not among the rights it recognises.",
  "सोलिगा, जो सदियों से BRT पहाड़ियों में रहते आए हैं, ने वन अधिकार अधिनियम के तहत अभयारण्य के भीतर रहते हुए लघु वनोपज इकट्ठा करने, अपने वनों का प्रबंधन करने और परंपरागत प्रथाएँ जारी रखने के अधिकार पाए। तब से कैमरा-ट्रैप आकलनों ने बाघों की संख्या बढ़ती दिखाई है, इसलिए इस मामले को उस धारणा के विरुद्ध उद्धृत किया जाता है कि संरक्षण के लिए लोगों को हटाना आवश्यक है। "
  "वन अधिकार अधिनियम बाघ अभयारण्यों के भीतर भी लागू होता है, और शिकार उन अधिकारों में नहीं है जिन्हें यह मान्यता देता है।",
  "Ministry of Tribal Affairs -- Forest Rights Act, 2006; National Tiger Conservation Authority -- Status of Tigers in India.", "env-soliga-brt-forest-rights", craft="inference")

M(PA, "easy", "The 'Save Silent Valley' campaign, which in the early 1980s stopped a hydroelectric dam on the Kunthipuzha river in Kerala, won national support mainly because the valley:",
  "'साइलेंट वैली बचाओ' अभियान, जिसने 1980 के दशक के आरंभ में केरल की कुंतिपुझा नदी पर एक जलविद्युत बाँध रुकवाया, को राष्ट्रीय समर्थन मुख्यतः इसलिए मिला कि यह घाटी:",
  ["held one of the last large tracts of undisturbed rainforest in the Western Ghats",
   "was the only surviving home of the Asiatic lion outside the Gir forest of Gujarat",
   "held the main nesting beaches of the olive ridley turtle on India's west coast",
   "lay on an active fault line, so a dam there risked setting off major earthquakes"],
  ["पश्चिमी घाट में अछूते वर्षावन के अंतिम बड़े भूभागों में से एक थी",
   "गुजरात के गिर वन के बाहर एशियाई सिंह का एकमात्र बचा हुआ घर थी",
   "भारत के पश्चिमी तट पर ऑलिव रिडले कछुए के मुख्य घोंसला-तट रखती थी",
   "एक सक्रिय भ्रंश-रेखा पर थी, इसलिए वहाँ बाँध से बड़े भूकंप आने का ख़तरा था"],
  0,
  "Silent Valley, in Palakkad district, is a rare stretch of tropical evergreen forest that had escaped logging and settlement, home to the lion-tailed macaque and many endemic plants. Scientists, the Kerala Sastra Sahitya Parishad and others argued that flooding it would destroy an irreplaceable ecosystem; the project was dropped, and the area was declared a national park in 1984. "
  "Asiatic lions survive in the wild only in Gujarat, olive ridleys come ashore in mass nestings on the east coast, and the campaign was not about earthquakes.",
  "पालक्काड ज़िले की साइलेंट वैली उष्णकटिबंधीय सदाबहार वन का एक दुर्लभ भूभाग है जो कटाई और बसावट से बचा रहा, और जो सिंह-पुच्छ मकाक और कई स्थानिक पौधों का घर है। वैज्ञानिकों, केरल शास्त्र साहित्य परिषद और अन्य लोगों ने तर्क दिया कि इसे डुबोने से एक अपूरणीय पारितंत्र नष्ट हो जाएगा; परियोजना छोड़ दी गई, और 1984 में क्षेत्र को राष्ट्रीय उद्यान घोषित किया गया। "
  "एशियाई सिंह जंगल में केवल गुजरात में बचे हैं, ऑलिव रिडले सामूहिक रूप से पूर्वी तट पर घोंसले बनाते हैं, और अभियान भूकंपों के बारे में नहीं था।",
  "Kerala Forest Department -- Silent Valley National Park.", "env-silent-valley", craft="linkage")

# ================================================================ statements (15)
S(PA, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["India is not counted among the megadiverse countries, since most of its species are also found in neighbouring countries.",
   "Part of the reason for India's rich biodiversity is that it lies where three biogeographic realms meet: the Indo-Malayan, the Palaearctic and the Afrotropical."],
  ["भारत की गिनती महाविविध देशों में नहीं होती, क्योंकि इसकी अधिकांश प्रजातियाँ पड़ोसी देशों में भी पाई जाती हैं।",
   "भारत की समृद्ध जैव विविधता का एक कारण यह है कि यह वहाँ स्थित है जहाँ तीन जैव-भौगोलिक परिमंडल मिलते हैं: इंडो-मलय, पेलिआर्कटिक और एफ़्रोट्रॉपिकल।"],
  T2, 1,
  "Only statement 2 is correct. India is one of the 17 megadiverse countries identified by UNEP's World Conservation Monitoring Centre, with about 2.4 per cent of the world's land and 7-8 per cent of its recorded species; megadiversity counts a country's total richness and endemism, not whether its species are found nowhere else. "
  "Its position where three realms meet -- with Palaearctic species in the Himalaya, Indo-Malayan species in the north-east and the Western Ghats, and African affinities in the dry west -- together with climates that range from the Thar to the rain-soaked Western Ghats, explains much of that richness.",
  "केवल कथन 2 सही है। भारत UNEP के विश्व संरक्षण निगरानी केंद्र द्वारा चिह्नित 17 महाविविध देशों में से एक है, जिसके पास संसार की लगभग 2.4 प्रतिशत भूमि और उसकी दर्ज प्रजातियों का 7-8 प्रतिशत है; महाविविधता किसी देश की कुल समृद्धि और स्थानिकता गिनती है, यह नहीं कि उसकी प्रजातियाँ कहीं और न मिलें। "
  "तीन परिमंडलों के मिलन-बिंदु पर उसकी स्थिति, जिसमें हिमालय में पेलिआर्कटिक प्रजातियाँ, उत्तर-पूर्व और पश्चिमी घाट में इंडो-मलय प्रजातियाँ, और शुष्क पश्चिम में अफ़्रीकी समानताएँ हैं, थार से लेकर वर्षा से भीगे पश्चिमी घाट तक की जलवायु के साथ, उस समृद्धि का बड़ा भाग समझाती है।",
  "Ministry of Environment, Forest and Climate Change -- India's National Biodiversity Strategy and Action Plan.", "env-india-megadiverse", craft="linkage")

S(PA, "easy", "Consider the following statements about Keoladeo National Park:",
  "केवलादेव राष्ट्रीय उद्यान के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It was created as a wetland by the rulers of Bharatpur, who built dykes and canals to flood the land for duck shoots.",
   "Since its water is let in from outside the park through the Ajan Bund, failed monsoons and upstream diversions have left it short of water in some years.",
   "It is a tiger reserve as well as a World Heritage Site."],
  ["इसे भरतपुर के शासकों ने एक आर्द्रभूमि के रूप में बनाया, जिन्होंने बत्तख के शिकार के लिए भूमि को डुबोने हेतु बाँध और नहरें बनवाईं।",
   "चूँकि इसका पानी उद्यान के बाहर से अजान बाँध के माध्यम से छोड़ा जाता है, इसलिए कमज़ोर मानसून और ऊपर की ओर पानी मोड़ने से कुछ वर्षों में इसमें पानी की कमी रही है।",
   "यह बाघ अभयारण्य होने के साथ-साथ विश्व धरोहर स्थल भी है।"],
  C3, 1,
  "Statements 1 and 2 are correct. Keoladeo is a man-made wetland in a semi-arid region: in the 19th century the rulers of Bharatpur flooded a natural depression to create duck-shooting grounds. Because it fills with monsoon water released from the Ajan Bund, fed by the Gambhir and Banganga rivers, it suffers when rain fails or water is held back upstream, which is why pipelines were later laid to supply it. "
  "Statement 3 is wrong: it is a national park and, since 1985, a World Heritage Site, but not a tiger reserve.",
  "कथन 1 और 2 सही हैं। केवलादेव एक अर्ध-शुष्क क्षेत्र की मानव-निर्मित आर्द्रभूमि है: 19वीं सदी में भरतपुर के शासकों ने बत्तख-शिकार के मैदान बनाने के लिए एक प्राकृतिक गर्त को डुबोया। चूँकि यह गंभीर और बाणगंगा नदियों से भरने वाले अजान बाँध से छोड़े गए मानसूनी पानी से भरता है, इसलिए वर्षा न होने या ऊपर पानी रोके जाने पर इसे हानि होती है, इसीलिए बाद में इसकी आपूर्ति के लिए पाइपलाइनें बिछाई गईं। "
  "कथन 3 गलत है: यह राष्ट्रीय उद्यान है और 1985 से विश्व धरोहर स्थल है, पर बाघ अभयारण्य नहीं।",
  "UNESCO World Heritage Centre -- Keoladeo National Park.", "env-keoladeo-history", craft="linkage")

S(PA, "hard", "A State plans to widen a highway that passes through a wildlife sanctuary. Consider the following statements about the National Board for Wildlife (NBWL):",
  "एक राज्य किसी वन्यजीव अभयारण्य से होकर गुज़रने वाले राजमार्ग को चौड़ा करना चाहता है। राष्ट्रीय वन्यजीव बोर्ड (NBWL) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The project needs the recommendation of the NBWL's Standing Committee before it can go ahead.",
   "The NBWL is chaired by the Union Minister for Environment.",
   "Because the NBWL is only advisory, the State Government can alter the boundaries of the sanctuary on its own to take the highway out of it."],
  ["परियोजना आगे बढ़ने से पहले उसे NBWL की स्थायी समिति की सिफ़ारिश चाहिए।",
   "NBWL की अध्यक्षता केंद्रीय पर्यावरण मंत्री करते हैं।",
   "चूँकि NBWL केवल सलाहकारी है, इसलिए राज्य सरकार राजमार्ग को बाहर करने के लिए अभयारण्य की सीमाएँ स्वयं बदल सकती है।"],
  C3, 0,
  "Only statement 1 is correct. The Wild Life (Protection) Act bars destroying or diverting the habitat of a sanctuary or national park except under a permit that may be granted only after consulting the NBWL, and the Supreme Court has required its Standing Committee to clear projects inside protected areas, which is why it meets regularly on roads, power lines and mines. "
  "Statement 2 is wrong: the Board is chaired by the Prime Minister; the Environment Minister is vice-chairperson and chairs its Standing Committee. Statement 3 is wrong: section 26A(3) allows a sanctuary's boundaries to be altered only on a resolution of the State Legislature passed on the NBWL's recommendation, so the Board cannot be bypassed that way.",
  "केवल कथन 1 सही है। वन्यजीव (संरक्षण) अधिनियम किसी अभयारण्य या राष्ट्रीय उद्यान के आवास को नष्ट करने या मोड़ने पर रोक लगाता है, सिवाय ऐसे परमिट के जो NBWL से परामर्श के बाद ही दिया जा सकता है, और सर्वोच्च न्यायालय ने संरक्षित क्षेत्रों के भीतर की परियोजनाओं के लिए इसकी स्थायी समिति की स्वीकृति अनिवार्य की है, इसीलिए वह सड़कों, बिजली-लाइनों और खदानों पर नियमित रूप से बैठती है। "
  "कथन 2 गलत है: बोर्ड की अध्यक्षता प्रधानमंत्री करते हैं; पर्यावरण मंत्री उपाध्यक्ष हैं और इसकी स्थायी समिति की अध्यक्षता करते हैं। कथन 3 गलत है: धारा 26A(3) अभयारण्य की सीमाएँ केवल NBWL की सिफ़ारिश पर पारित राज्य विधानमंडल के संकल्प से बदलने देती है, इसलिए बोर्ड को इस तरह दरकिनार नहीं किया जा सकता।",
  WPA, "env-national-board-for-wildlife", craft="application")

S(PA, "medium", "Consider the following statements about the Ganges river dolphin:",
  "गंगा नदी डॉल्फ़िन के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Since it is nearly blind and finds its prey by echolocation, noise from boats, dredgers and engines disturbs its feeding.",
   "Dams and barrages harm it by splitting its population into isolated stretches of river.",
   "The Vikramshila Gangetic Dolphin Sanctuary is in Bihar."],
  ["चूँकि यह लगभग अंधी है और प्रतिध्वनि-निर्धारण से अपना शिकार खोजती है, इसलिए नावों, ड्रेजरों और इंजनों का शोर इसके भोजन में बाधा डालता है।",
   "बाँध और बराज इसकी समष्टि को नदी के अलग-थलग खंडों में बाँटकर इसे हानि पहुँचाते हैं।",
   "विक्रमशिला गांगेय डॉल्फ़िन अभयारण्य बिहार में है।"],
  C3, 2,
  "All three are correct. Living in muddy water, the Ganges river dolphin has tiny eyes that sense little more than light and hunts with clicks; underwater noise from mechanised boats, dredging for waterways and sand mining masks those signals. Barrages such as Farakka cut rivers into stretches whose small populations cannot mix, and low dry-season flows shrink the deep pools the dolphins need. "
  "The Vikramshila sanctuary lies on a stretch of the Ganga near Bhagalpur in Bihar. The species, the National Aquatic Animal since 2009, is Endangered.",
  "तीनों कथन सही हैं। गंदले पानी में रहने वाली गंगा नदी डॉल्फ़िन की छोटी आँखें प्रकाश से अधिक कुछ नहीं समझ पातीं और यह क्लिक-ध्वनियों से शिकार करती है; यंत्रचालित नावों, जलमार्गों के लिए ड्रेजिंग और रेत-खनन का जलगत शोर इन संकेतों को दबा देता है। फ़रक्का जैसे बराज नदियों को ऐसे खंडों में काट देते हैं जिनकी छोटी समष्टियाँ आपस में नहीं मिल पातीं, और शुष्क ऋतु का कम प्रवाह उन गहरे कुंडों को सिकोड़ देता है जिनकी डॉल्फ़िनों को ज़रूरत है। "
  "विक्रमशिला अभयारण्य बिहार में भागलपुर के पास गंगा के एक खंड पर है। 2009 से राष्ट्रीय जलीय जीव यह प्रजाति संकटग्रस्त (Endangered) है।",
  "Wildlife Institute of India -- Ganges river dolphin.", "env-india-dolphins", craft="linkage")

S(PA, "medium", "Consider the following statements about 'Indian Rhino Vision 2020' in Assam:",
  "असम में 'इंडियन राइनो विज़न 2020' के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Its main aim was to spread rhinos over several protected areas, so that one flood, epidemic or wave of poaching could not destroy most of them.",
   "Rhinos have been translocated under it from Kaziranga and Pobitora to Manas.",
   "It aimed to move all of Assam's rhinos out of Kaziranga."],
  ["इसका मुख्य लक्ष्य गैंडों को कई संरक्षित क्षेत्रों में फैलाना था, ताकि एक बाढ़, महामारी या शिकार की लहर उनमें से अधिकांश को नष्ट न कर सके।",
   "इसके तहत गैंडों को काज़ीरंगा और पोबितोरा से मानस ले जाया गया है।",
   "इसका लक्ष्य असम के सभी गैंडों को काज़ीरंगा से बाहर ले जाना था।"],
  C3, 1,
  "Statements 1 and 2 are correct. With nearly all of Assam's rhinos in Kaziranga and Pobitora, the population was exposed to single-site disasters, so Indian Rhino Vision 2020, a partnership of the Assam Forest Department, WWF-India and the International Rhino Foundation, aimed for about 3,000 wild rhinos spread over seven protected areas, starting with Manas, where poaching during years of unrest had wiped them out. "
  "Statement 3 is wrong: Kaziranga stayed the core population; only some animals were moved to found new ones.",
  "कथन 1 और 2 सही हैं। असम के लगभग सभी गैंडे काज़ीरंगा और पोबितोरा में होने से समष्टि एक ही स्थल की आपदाओं के प्रति असुरक्षित थी, इसलिए असम वन विभाग, WWF-इंडिया और इंटरनेशनल राइनो फ़ाउंडेशन की साझेदारी इंडियन राइनो विज़न 2020 ने सात संरक्षित क्षेत्रों में फैले लगभग 3,000 जंगली गैंडों का लक्ष्य रखा, जिसकी शुरुआत मानस से हुई, जहाँ अशांति के वर्षों में शिकार ने उन्हें समाप्त कर दिया था। "
  "कथन 3 गलत है: काज़ीरंगा मुख्य समष्टि बना रहा; केवल कुछ जानवरों को नई समष्टियाँ बसाने के लिए ले जाया गया।",
  "WWF-India -- Indian Rhino Vision 2020.", "env-indian-rhino-vision-2020", craft="linkage")

S(PA, "medium", "Consider the following statements about Keibul Lamjao National Park:",
  "केइबुल लामजाओ राष्ट्रीय उद्यान के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is a floating national park, made up largely of 'phumdis' on Loktak Lake.",
   "Since the Ithai barrage keeps Loktak's water high all year, the phumdis no longer settle on the lake bed in the dry season to draw nutrients, and they have been thinning.",
   "The sangai, the brow-antlered deer found in the wild only here, is Manipur's State animal."],
  ["यह एक तैरता राष्ट्रीय उद्यान है, जो मुख्यतः लोकटक झील पर 'फुमदियों' से बना है।",
   "चूँकि इथाई बराज लोकटक के पानी को साल भर ऊँचा रखता है, इसलिए फुमदियाँ अब शुष्क ऋतु में पोषक तत्व लेने के लिए झील की तली पर नहीं टिकतीं, और पतली होती जा रही हैं।",
   "संगाई, भौंह-सींग वाला हिरण जो जंगल में केवल यहीं मिलता है, मणिपुर का राज्य पशु है।"],
  C3, 2,
  "All three are correct. Phumdis are floating mats of vegetation, soil and organic matter; the thickest of them carry the weight of the sangai, which walks on them with splayed hooves. "
  "Before the Ithai barrage of the Loktak hydroelectric project was built in the early 1980s, the lake level fell in the dry season and the phumdis rested on the bottom, taking up nutrients; with a constant high level they float all year, grow thinner and bear the deer less well, which is the main long-term threat to the park. The sangai, once thought extinct, numbers only a few hundred.",
  "तीनों कथन सही हैं। फुमदियाँ वनस्पति, मिट्टी और जैविक पदार्थ की तैरती परतें हैं; उनमें से सबसे मोटी संगाई का भार उठाती हैं, जो फैले खुरों से उन पर चलता है। "
  "1980 के दशक के आरंभ में लोकटक जलविद्युत परियोजना का इथाई बराज बनने से पहले शुष्क ऋतु में झील का स्तर गिरता था और फुमदियाँ तली पर टिककर पोषक तत्व लेती थीं; स्थिर ऊँचे स्तर के कारण वे साल भर तैरती हैं, पतली होती हैं और हिरण का भार कम अच्छी तरह उठाती हैं, जो उद्यान के लिए दीर्घकालीन मुख्य ख़तरा है। संगाई, जिसे कभी विलुप्त माना गया था, केवल कुछ सौ बचे हैं।",
  "Manipur Forest Department -- Keibul Lamjao National Park.", "env-keibul-lamjao-sangai", craft="linkage")

S(PA, "medium", "Consider the following statements about Project Cheetah:",
  "प्रोजेक्ट चीता के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Since the Asiatic cheetah now survives only in Iran, in very small numbers, the cheetahs brought to India are of the African subspecies.",
   "The first batch of cheetahs came from Kenya.",
   "Since Kuno has no other large predators, the cheetahs there face no competition from leopards."],
  ["चूँकि एशियाई चीता अब केवल ईरान में, बहुत कम संख्या में, बचा है, इसलिए भारत लाए गए चीते अफ़्रीकी उप-प्रजाति के हैं।",
   "चीतों का पहला दल केन्या से आया।",
   "चूँकि कूनो में कोई अन्य बड़ा शिकारी नहीं है, इसलिए वहाँ के चीतों को तेंदुओं से कोई प्रतिस्पर्धा नहीं झेलनी पड़ती।"],
  C3, 0,
  "Only statement 1 is correct. Iran's tiny population of Asiatic cheetahs could spare no animals, so India brought in African cheetahs, which are genetically close. "
  "Statement 2 is wrong: the first eight came from Namibia in September 2022, followed by twelve from South Africa in 2023; in April 2025 some were moved to Gandhi Sagar Wildlife Sanctuary, the second site. Statement 3 is wrong: Kuno has a sizeable leopard population, and competition with leopards, which kill cheetah cubs and steal kills, is one of the challenges the project has to manage, along with the cheetahs' habit of ranging far beyond the park.",
  "केवल कथन 1 सही है। ईरान की एशियाई चीतों की छोटी-सी समष्टि से कोई जानवर नहीं दिया जा सकता था, इसलिए भारत अफ़्रीकी चीते लाया, जो आनुवंशिक रूप से निकट हैं। "
  "कथन 2 गलत है: पहले आठ सितंबर 2022 में नामीबिया से आए, उसके बाद 2023 में बारह दक्षिण अफ़्रीका से; अप्रैल 2025 में कुछ को दूसरे स्थल, गांधी सागर वन्यजीव अभयारण्य, ले जाया गया। कथन 3 गलत है: कूनो में तेंदुओं की बड़ी समष्टि है, और तेंदुओं से प्रतिस्पर्धा, जो चीतों के शावकों को मारते और उनका शिकार छीनते हैं, उन चुनौतियों में से एक है जिन्हें परियोजना को सँभालना है, साथ ही चीतों का उद्यान से बहुत दूर तक घूमने का स्वभाव भी।",
  "National Tiger Conservation Authority -- Action Plan for Introduction of Cheetah in India.", "env-project-cheetah", craft="inference")

S(PA, "easy", "Consider the following statements about environmental movements in India:",
  "भारत के पर्यावरण आंदोलनों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Chipko villagers resisted commercial felling because the forests supplied their fodder, fuel and water, and felling on the slopes had worsened landslides and floods.",
   "The Appiko movement arose in Kerala.",
   "The Narmada Bachao Andolan was mainly a campaign against the Tehri dam."],
  ["चिपको के ग्रामीणों ने वाणिज्यिक कटाई का विरोध इसलिए किया कि वन उनके चारे, ईंधन और पानी का स्रोत थे, और ढलानों पर कटाई से भूस्खलन और बाढ़ बढ़ी थीं।",
   "अप्पिको आंदोलन केरल में उभरा।",
   "नर्मदा बचाओ आंदोलन मुख्यतः टिहरी बाँध के विरुद्ध अभियान था।"],
  C3, 0,
  "Only statement 1 is correct. Chipko began in 1973 in Chamoli district of present-day Uttarakhand, after the Alaknanda flood of 1970 had been linked to deforestation upstream; villagers, many of them women led by figures such as Gaura Devi, hugged trees to stop contractors, because the forest was their source of fodder, fuel and water. "
  "Statement 2 is wrong: Appiko ('to hug' in Kannada), inspired by Chipko, began in 1983 in Uttara Kannada, Karnataka. Statement 3 is wrong: the Narmada Bachao Andolan opposed the Sardar Sarovar and other Narmada dams; the campaign against the Tehri dam on the Bhagirathi was led by Sunderlal Bahuguna.",
  "केवल कथन 1 सही है। चिपको 1973 में आज के उत्तराखंड के चमोली ज़िले में शुरू हुआ, जब 1970 की अलकनंदा बाढ़ को ऊपरी क्षेत्र के वनोन्मूलन से जोड़ा जा चुका था; ग्रामीणों ने, जिनमें बहुत-सी महिलाएँ गौरा देवी जैसी नेताओं के साथ थीं, ठेकेदारों को रोकने के लिए वृक्षों को गले लगाया, क्योंकि वन उनके चारे, ईंधन और पानी का स्रोत था। "
  "कथन 2 गलत है: चिपको से प्रेरित अप्पिको ('गले लगाना', कन्नड़ में) 1983 में कर्नाटक के उत्तर कन्नड़ में शुरू हुआ। कथन 3 गलत है: नर्मदा बचाओ आंदोलन ने सरदार सरोवर और नर्मदा के अन्य बाँधों का विरोध किया; भागीरथी पर टिहरी बाँध के विरुद्ध अभियान का नेतृत्व सुंदरलाल बहुगुणा ने किया।",
  "NCERT Class XII, Politics in India since Independence -- Rise of Popular Movements.", "env-environmental-movements", craft="linkage")

S(PA, "medium", "Consider the following statements about coral reefs in India:",
  "भारत में प्रवाल भित्तियों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Since reef-building corals need warm, clear, shallow sea water, India's main reefs lie in the Gulf of Mannar, the Gulf of Kutch, Lakshadweep and the Andaman and Nicobar Islands, and not off the mouths of the great rivers of the east coast.",
   "Reef-building corals are listed in Schedule I of the Wild Life (Protection) Act.",
   "Coral mining is permitted in India for making lime, subject to a licence."],
  ["चूँकि भित्ति बनाने वाले प्रवालों को गर्म, साफ़, उथला समुद्री जल चाहिए, इसलिए भारत की मुख्य भित्तियाँ मन्नार की खाड़ी, कच्छ की खाड़ी, लक्षद्वीप और अंडमान-निकोबार में हैं, पूर्वी तट की बड़ी नदियों के मुहानों के पास नहीं।",
   "भित्ति बनाने वाले प्रवाल वन्यजीव (संरक्षण) अधिनियम की अनुसूची I में हैं।",
   "भारत में चूना बनाने के लिए लाइसेंस के अधीन प्रवाल-खनन की अनुमति है।"],
  C3, 1,
  "Statements 1 and 2 are correct. Corals depend on algae in their tissues that need sunlight, so they grow in shallow, clear, warm water; the silt and fresh water that the Ganga, Godavari, Krishna and Kaveri pour into the Bay of Bengal block light and lower salinity, which is why the long east coast has reefs mainly in the Gulf of Mannar and Palk Bay. Reef-building corals, black corals and sea fans are in Schedule I. "
  "Statement 3 is wrong: coral mining, once common for lime and building stone, is banned.",
  "कथन 1 और 2 सही हैं। प्रवाल अपने ऊतकों में रहने वाले उन शैवालों पर निर्भर हैं जिन्हें सूर्य-प्रकाश चाहिए, इसलिए वे उथले, साफ़, गर्म पानी में बढ़ते हैं; गंगा, गोदावरी, कृष्णा और कावेरी द्वारा बंगाल की खाड़ी में डाली जाने वाली गाद और मीठा पानी प्रकाश रोकते और लवणता घटाते हैं, इसीलिए लंबे पूर्वी तट पर भित्तियाँ मुख्यतः मन्नार की खाड़ी और पाक खाड़ी में हैं। भित्ति बनाने वाले प्रवाल, काले प्रवाल और समुद्री पंखे अनुसूची I में हैं। "
  "कथन 3 गलत है: प्रवाल-खनन, जो कभी चूने और भवन-पत्थर के लिए आम था, प्रतिबंधित है।",
  WPA, "env-coral-reefs-india", craft="linkage")

S(PA, "medium", "Consider the following statements about the Sundarbans:",
  "सुंदरबन के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Indian Sundarbans have not been designated a Ramsar site.",
   "As rising sea levels and reduced freshwater flow make the water saltier, the mangroves and the tigers that depend on them are under growing pressure.",
   "The Sundarbans mangroves lie on the delta of the Mahanadi."],
  ["भारतीय सुंदरबन को रामसर स्थल घोषित नहीं किया गया है।",
   "जैसे-जैसे बढ़ता समुद्र-स्तर और घटता मीठे पानी का प्रवाह पानी को अधिक खारा बना रहे हैं, मैंग्रोव और उन पर निर्भर बाघ बढ़ते दबाव में हैं।",
   "सुंदरबन के मैंग्रोव महानदी के डेल्टा पर स्थित हैं।"],
  C3, 0,
  "Only statement 2 is correct. Sea level in the Sundarbans is rising faster than the global average, low islands such as Lohachara and Ghoramara have been lost or have shrunk, and fresh water from upstream has fallen as distributaries silted up and flows were diverted, so salinity is rising; salt-sensitive mangroves such as the sundari are declining, and people and tigers are squeezed onto less land. "
  "Statement 1 is wrong: the Indian Sundarbans became a Ramsar site in 2019, and they are also a World Heritage Site, a tiger reserve and a biosphere reserve. Statement 3 is wrong: they lie on the delta of the Ganga, the Brahmaputra and the Meghna.",
  "केवल कथन 2 सही है। सुंदरबन में समुद्र-स्तर वैश्विक औसत से तेज़ी से बढ़ रहा है, लोहाचारा और घोड़ामारा जैसे निचले द्वीप खो गए हैं या सिकुड़ गए हैं, और वितरिकाओं के गाद से भरने तथा प्रवाह मोड़े जाने से ऊपर से आने वाला मीठा पानी घटा है, इसलिए लवणता बढ़ रही है; सुंदरी जैसे लवण-संवेदी मैंग्रोव घट रहे हैं, और लोग तथा बाघ कम भूमि पर सिमट रहे हैं। "
  "कथन 1 गलत है: भारतीय सुंदरबन 2019 में रामसर स्थल बना, और यह विश्व धरोहर स्थल, बाघ अभयारण्य और जैवमंडल रिज़र्व भी है। कथन 3 गलत है: यह गंगा, ब्रह्मपुत्र और मेघना के डेल्टा पर है।",
  "West Bengal Forest Department -- Sundarban Tiger Reserve.", "env-sundarbans-designations", craft="linkage")

S(PA, "medium", "Consider the following statements about mangrove conservation:",
  "मैंग्रोव संरक्षण के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The MISHTI scheme, launched in 2023, pays for planting and restoring mangroves by pooling money from the rural employment scheme, the compensatory afforestation funds and other sources.",
   "In the Odisha super cyclone of 1999, villages with wider mangrove belts in front of them suffered fewer deaths, showing that mangroves shield coasts from storm surges.",
   "India has joined the Mangrove Alliance for Climate, launched at COP27."],
  ["2023 में शुरू की गई MISHTI योजना ग्रामीण रोज़गार योजना, प्रतिपूरक वनरोपण कोष और अन्य स्रोतों के धन को मिलाकर मैंग्रोव लगाने और बहाल करने का ख़र्च उठाती है।",
   "1999 के ओडिशा महाचक्रवात में जिन गाँवों के सामने मैंग्रोव की चौड़ी पट्टियाँ थीं, वहाँ कम मौतें हुईं, जिससे पता चलता है कि मैंग्रोव तटों को तूफ़ानी लहरों से बचाते हैं।",
   "भारत COP27 में शुरू हुए 'मैंग्रोव एलायंस फ़ॉर क्लाइमेट' में शामिल हुआ है।"],
  C3, 2,
  "All three are correct. MISHTI (Mangrove Initiative for Shoreline Habitats and Tangible Incomes) draws on MGNREGS, CAMPA and other funds to plant and restore mangroves. Studies of the 1999 cyclone found that, other things being equal, villages behind wider mangroves lost fewer lives, because dense roots and stems slow the waves and cut the height and reach of the surge -- a large part of why mangroves are counted as coastal defences. "
  "India joined the Mangrove Alliance for Climate, led by the UAE and Indonesia, at COP27 in 2022. Among the States, West Bengal has the largest mangrove cover, because of the Sundarbans.",
  "तीनों कथन सही हैं। MISHTI (मैंग्रोव इनिशिएटिव फ़ॉर शोरलाइन हैबिटैट्स एंड टैंजिबल इनकम्स) मैंग्रोव लगाने और बहाल करने के लिए मनरेगा, कैम्पा और अन्य कोषों का उपयोग करती है। 1999 के चक्रवात के अध्ययनों ने पाया कि अन्य बातें समान होने पर चौड़े मैंग्रोव के पीछे के गाँवों में कम जानें गईं, क्योंकि घनी जड़ें और तने लहरों को धीमा करते हैं और तूफ़ानी लहर की ऊँचाई तथा पहुँच घटाते हैं; यही बड़ा कारण है कि मैंग्रोव तटीय रक्षा माने जाते हैं। "
  "भारत 2022 में COP27 में संयुक्त अरब अमीरात और इंडोनेशिया के नेतृत्व वाले मैंग्रोव एलायंस फ़ॉर क्लाइमेट में शामिल हुआ। राज्यों में सुंदरबन के कारण पश्चिम बंगाल में सबसे अधिक मैंग्रोव आवरण है।",
  MOEF + " -- MISHTI.", "env-mangrove-initiatives", craft="linkage")

S(PA, "medium", "Consider the following statements about the protected areas of the Andaman and Nicobar Islands:",
  "अंडमान और निकोबार द्वीपसमूह के संरक्षित क्षेत्रों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Great Nicobar is a biosphere reserve.",
   "Campbell Bay and Galathea National Parks lie in the Andaman group of islands.",
   "Since the Narcondam hornbill lives only on one small island, a single disaster or large project there could wipe out the species."],
  ["ग्रेट निकोबार एक जैवमंडल रिज़र्व है।",
   "कैंपबेल बे और गलाथिया राष्ट्रीय उद्यान अंडमान द्वीप-समूह में स्थित हैं।",
   "चूँकि नारकोंडम धनेश केवल एक छोटे द्वीप पर रहता है, इसलिए वहाँ एक ही आपदा या बड़ी परियोजना इस प्रजाति को समाप्त कर सकती है।"],
  C3, 1,
  "Statements 1 and 3 are correct. The Great Nicobar Biosphere Reserve (1989, in UNESCO's network since 2013) protects tropical wet evergreen forest, mangroves and turtle nesting beaches. The Narcondam hornbill is found only on Narcondam, a volcanic island of about 7 square kilometres in the Andaman Sea; with a few hundred birds in one place, the species is exposed to any single threat, such as a cyclone, an introduced predator or construction. "
  "Statement 2 is wrong: Campbell Bay and Galathea National Parks are on Great Nicobar, in the Nicobar group.",
  "कथन 1 और 3 सही हैं। ग्रेट निकोबार जैवमंडल रिज़र्व (1989, 2013 से यूनेस्को के नेटवर्क में) उष्णकटिबंधीय आर्द्र सदाबहार वन, मैंग्रोव और कछुओं के घोंसला-तटों की रक्षा करता है। नारकोंडम धनेश केवल अंडमान सागर के लगभग 7 वर्ग किलोमीटर के ज्वालामुखीय द्वीप नारकोंडम पर मिलता है; एक ही स्थान पर कुछ सौ पक्षियों के कारण यह प्रजाति किसी एक ख़तरे, जैसे चक्रवात, बाहर से लाए गए शिकारी या निर्माण, के प्रति असुरक्षित है। "
  "कथन 2 गलत है: कैंपबेल बे और गलाथिया राष्ट्रीय उद्यान निकोबार समूह के ग्रेट निकोबार पर हैं।",
  "Andaman and Nicobar Forest Department.", "env-andaman-nicobar-protected-areas", craft="inference")

S(PA, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Great Himalayan National Park is in Uttarakhand.",
   "Hemis National Park in Ladakh is known for its snow leopards, which find prey there in the blue sheep and ibex of its high, cold desert.",
   "Namdapha National Park is in Sikkim."],
  ["ग्रेट हिमालयन राष्ट्रीय उद्यान उत्तराखंड में है।",
   "लद्दाख का हेमिस राष्ट्रीय उद्यान अपने हिम तेंदुओं के लिए जाना जाता है, जिन्हें वहाँ के ऊँचे, ठंडे मरुस्थल की भरल (नीली भेड़) और आइबेक्स में शिकार मिलता है।",
   "नामदाफा राष्ट्रीय उद्यान सिक्किम में है।"],
  C3, 0,
  "Only statement 2 is correct. Hemis covers high, dry valleys such as the Markha and the Rumbak, where herds of blue sheep (bharal) and Asiatic ibex support one of the densest snow leopard populations known, which has made it a centre of snow leopard tourism run by local homestays. "
  "Statement 1 is wrong: the Great Himalayan National Park, a World Heritage Site since 2014, is in Kullu district of Himachal Pradesh. Statement 3 is wrong: Namdapha is in Arunachal Pradesh, and is unusual in holding four big cats -- tiger, leopard, snow leopard and clouded leopard.",
  "केवल कथन 2 सही है। हेमिस मार्खा और रुम्बक जैसी ऊँची, शुष्क घाटियों में फैला है, जहाँ भरल (नीली भेड़) और एशियाई आइबेक्स के झुंड हिम तेंदुओं की ज्ञात सबसे घनी समष्टियों में से एक को सहारा देते हैं, जिससे यह स्थानीय होमस्टे द्वारा चलाए जाने वाले हिम तेंदुआ पर्यटन का केंद्र बन गया है। "
  "कथन 1 गलत है: 2014 से विश्व धरोहर स्थल ग्रेट हिमालयन राष्ट्रीय उद्यान हिमाचल प्रदेश के कुल्लू ज़िले में है। कथन 3 गलत है: नामदाफा अरुणाचल प्रदेश में है, और चार बड़ी बिल्लियों, बाघ, तेंदुआ, हिम तेंदुआ और धूमिल तेंदुआ, के होने के कारण अनोखा है।",
  "Wildlife Institute of India.", "env-himalayan-national-parks", craft="linkage")

S(PA, "medium", "Consider the following statements about captive elephants under the Wild Life (Protection) Act:",
  "वन्यजीव (संरक्षण) अधिनियम के तहत बंदी हाथियों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The 2022 amendment allows a person holding a valid ownership certificate to transfer or transport a captive elephant for a religious or any other purpose, subject to conditions.",
   "Since the Asian elephant is in Schedule I, a captive elephant cannot be sold commercially like ordinary property.",
   "A captive elephant used only in temple festivals needs no ownership certificate."],
  ["2022 का संशोधन वैध स्वामित्व प्रमाणपत्र वाले व्यक्ति को धार्मिक या किसी अन्य उद्देश्य के लिए, शर्तों के अधीन, बंदी हाथी के हस्तांतरण या परिवहन की अनुमति देता है।",
   "चूँकि एशियाई हाथी अनुसूची I में है, इसलिए बंदी हाथी को साधारण संपत्ति की तरह व्यावसायिक रूप से बेचा नहीं जा सकता।",
   "केवल मंदिर-उत्सवों में काम आने वाले बंदी हाथी के लिए स्वामित्व प्रमाणपत्र की आवश्यकता नहीं है।"],
  C3, 1,
  "Statements 1 and 2 are correct. For a Schedule I animal the Act bars transfer by sale or for any other commercial consideration; the 2022 amendment carved out a narrow exception that lets certificate holders transfer or move captive elephants, and the Captive Elephant (Transfer or Transport) Rules, 2024 set conditions, such as a check of the animal's health and its genetic profile. "
  "Statement 3 is wrong: anyone who possesses a captive elephant, a temple included, must hold an ownership certificate from the Chief Wild Life Warden.",
  "कथन 1 और 2 सही हैं। अनुसूची I के प्राणी के लिए अधिनियम बिक्री या किसी अन्य व्यावसायिक प्रतिफल से हस्तांतरण पर रोक लगाता है; 2022 के संशोधन ने एक सीमित अपवाद बनाया जो प्रमाणपत्र-धारकों को बंदी हाथियों का हस्तांतरण या परिवहन करने देता है, और बंदी हाथी (हस्तांतरण या परिवहन) नियम, 2024 शर्तें तय करते हैं, जैसे प्राणी के स्वास्थ्य और उसकी आनुवंशिक प्रोफ़ाइल की जाँच। "
  "कथन 3 गलत है: बंदी हाथी रखने वाले हर व्यक्ति को, मंदिर सहित, मुख्य वन्यजीव वार्डन से स्वामित्व प्रमाणपत्र लेना होता है।",
  WPA, "env-captive-elephants-transfer", craft="inference")

S(PA, "medium", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The 'black' tigers of Simlipal are common there because its tigers mix freely with those of other reserves, which has spread the gene behind their colour.",
   "Kawal Tiger Reserve is in Maharashtra.",
   "Dampa Tiger Reserve is in Meghalaya."],
  ["सिमलीपाल के 'काले' बाघ वहाँ इसलिए आम हैं कि उसके बाघ अन्य अभयारण्यों के बाघों से खुलकर मिलते हैं, जिससे उनके रंग के पीछे का जीन फैला है।",
   "कवाल बाघ अभयारण्य महाराष्ट्र में है।",
   "डम्पा बाघ अभयारण्य मेघालय में है।"],
  C3, 3,
  "None is correct. Statement 1 has the reason backwards: Simlipal, in Odisha, holds an isolated tiger population founded by few animals, and inbreeding within it has let a rare variant of one gene (Taqpep), which broadens the dark stripes, spread until a large share of its tigers carry it -- a sign of genetic isolation, not of mixing. "
  "Statement 2 is wrong: Kawal is in Telangana, on the Godavari side of the Deccan. Statement 3 is wrong: Dampa is in Mizoram, on the Bangladesh border. Each statement places a reserve in a neighbouring State.",
  "कोई भी कथन सही नहीं है। कथन 1 कारण को उलट देता है: ओडिशा का सिमलीपाल कुछ ही जानवरों से बसी एक अलग-थलग बाघ समष्टि रखता है, और उसके भीतर अंतःप्रजनन ने एक जीन (Taqpep) के एक दुर्लभ रूप को, जो काली धारियों को चौड़ा करता है, इतना फैलने दिया कि उसके बाघों का बड़ा भाग उसे वहन करता है; यह आनुवंशिक अलगाव का चिह्न है, मेल-जोल का नहीं। "
  "कथन 2 गलत है: कवाल तेलंगाना में, दक्कन के गोदावरी वाले भाग में है। कथन 3 गलत है: डम्पा मिज़ोरम में, बांग्लादेश सीमा पर है। हर कथन किसी अभयारण्य को पड़ोसी राज्य में रखता है।",
  "National Tiger Conservation Authority -- Status of Tigers in India.", "env-tiger-reserve-locations", craft="linkage")

# ================================================================ TAGS for the 69 kept rows (Test 21's 4 are tagged already)
TAGS = {
 "env-right-to-environment-art21-48a": "linkage", "env-environment-laws-years-pairs": "recall", "env-wildlife-institute-dehradun": "recall",
 "env-cpcb-status-functions": "precision", "env-ntca-statutory": "precision", "env-compensatory-afforestation-fund": "precision",
 "env-forest-conservation-amendment-2023": "precision", "env-jan-vishwas-environment": "recall", "env-biodiversity-act-2023": "precision",
 "env-crz-2019": "precision", "env-eia-notification-2006": "precision", "env-epa-1986-basics": "precision",
 "env-ngt-jurisdiction": "precision", "env-water-act-1974": "linkage",
 "env-world-wildlife-day-cites": "recall", "env-ozone-recovery-slow": "linkage", "env-cites-trade-not-habitat": "precision",
 "env-montreal-kigali-climate": "linkage", "env-environment-reports-pairs": "recall", "env-earth-hour-wwf": "recall",
 "env-rio-conventions": "precision", "env-earth-summit-rio": "recall", "env-un-decade-ecosystem-restoration": "recall",
 "env-world-environment-day": "recall", "env-antarctic-treaty-system": "precision", "env-basel-rotterdam-stockholm": "precision",
 "env-cbd-protocols": "precision", "env-cites-appendices": "precision", "env-cms-bonn": "precision",
 "env-global-environment-facility": "precision", "env-global-plastics-treaty": "recall", "env-international-whaling-commission": "precision",
 "env-iucn-traffic-status": "precision", "env-kunming-montreal-gbf": "precision",
 "env-tiger-umbrella-species": "linkage", "env-cheetah-extinction-india": "linkage", "env-elephant-reserves-status": "precision",
 "env-tiger-corridors-gene-flow": "linkage", "env-tiger-reserve-relocation-fra": "precision", "env-national-parks-states-pairs": "recall",
 "env-protected-areas-species-pairs": "recall", "env-kailash-sankhala": "recall", "env-terai-arc-landscape": "recall",
 "env-tiger-reserves-north-south": "precision", "env-first-marine-national-park": "recall", "env-jerdons-courser-cr": "recall",
 "env-kaziranga-whs": "recall", "env-nagar-van-yojana": "recall", "env-dudhwa-satpura-location": "recall",
 "env-project-tiger-corbett": "recall", "env-wildlife-days": "recall", "env-world-wetlands-day": "recall",
 "env-biodiversity-heritage-sites": "precision", "env-biodiversity-hotspots": "precision", "env-iucn-protected-area-categories": "precision",
 "env-iucn-red-list-categories": "precision", "env-marine-protected-areas": "recall", "env-tiger-reserves-estimation": "precision",
 "env-big-cat-cooperation": "recall", "env-biosphere-reserves": "precision", "env-ex-situ-conservation": "precision",
 "env-india-natural-whs": "recall", "env-kanha-barasingha": "precision", "env-np-vs-sanctuary": "precision",
 "env-protected-area-network": "recall", "env-ramsar-montreux-record": "precision", "env-sea-turtle-protection-measures": "recall",
 "env-wetland-rules-amrit-dharohar": "precision", "env-wpa-2022-schedules": "precision"}

if __name__ == "__main__":
    write_updates("upg_l2_t11_env_b.sql", statuses=("draft", "published"), tags=TAGS)
