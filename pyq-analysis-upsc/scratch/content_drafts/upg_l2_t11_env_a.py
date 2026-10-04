# -*- coding: utf-8 -*-
"""Level 2 · Test 11 (Environment 3: Laws, Conventions and Protected Areas) -- depth audit of 2026-10-04, part A:
Indian Environmental Laws & Bodies and International Conventions & Organisations
(docs/upsc-question-design-standard.md §6). Part B (upg_l2_t11_env_b.py) has Protected Areas & Wildlife
Protection and the tags for the kept rows.

Before the audit the test had analytic 7, precision 36, recall 61. Part A rewrites 13 recall rows in place
with the same concept id, type and difficulty:
  - laws now put a case: a resort near a sanctuary (what an Eco-Sensitive Zone bars), a polluted river
    (who pays, after Vellore), a community's bamboo claim under the Forest Rights Act; the Ranjitsinh case
    as a clash of two green goals; why the Wildlife Crime Control Bureau works across borders;
  - conventions now ask what a 73 per cent Living Planet decline does and does not mean, what the Cali Fund
    corrects, what counts towards the Bonn Challenge, and why the high seas needed a treaty. They also ask
    how IPBES differs from a treaty body, why mercury needed a global convention, what land degradation
    neutrality means and why UNEP depends on voluntary money.
Leaks avoided while drafting:
  - the UNCCD as a 'Rio Convention' (answers the Rio-conventions MCQ);
  - India's 26-million-hectare restoration pledge (the old UNCCD statement, also the Bonn explanation);
  - CITES' trade-only scope in a new stem (answers the CITES-habitat AR)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write_updates, CODE
from polity_common import C3, C4, T2

d.SUBJECT = "Environment & Ecology"
d.REQUIRE_CRAFT = True
LAW = "Indian Environmental Laws & Bodies"
CON = "International Conventions & Organisations"
MOEF = "Ministry of Environment, Forest and Climate Change"

# ================================================================ LAWS & BODIES (5)
M(LAW, "hard", "In M.K. Ranjitsinh v. Union of India (2024), a plea to save the Great Indian Bustard from power lines led the Supreme Court to recognise a right to be free from the adverse effects of climate change. The difficulty the Court had to resolve was:",
  "एम.के. रणजीतसिंह बनाम भारत संघ (2024) में सोन चिरैया को बिजली की लाइनों से बचाने की याचिका पर सर्वोच्च न्यायालय ने जलवायु परिवर्तन के प्रतिकूल प्रभावों से मुक्त रहने के अधिकार को मान्यता दी। न्यायालय को जिस कठिनाई को सुलझाना था, वह थी:",
  ["saving an endangered bird while building power lines for renewable energy, a defence against climate change",
   "recognising tribal forest rights inside a tiger reserve while keeping its core area free of all people and their livestock",
   "linking two rivers for irrigation while keeping enough flow in them for river dolphins and gharials downstream",
   "allowing coal mining in central India while keeping the elephant corridors that run through the coalfields open"],
  ["एक संकटग्रस्त पक्षी को बचाना, और साथ ही नवीकरणीय ऊर्जा के लिए बिजली की लाइनें बनाना, जो स्वयं जलवायु परिवर्तन से बचाव है",
   "बाघ अभयारण्य के भीतर जनजातीय वन अधिकारों को मान्यता देना, और साथ ही उसके कोर क्षेत्र को लोगों और पशुओं से मुक्त रखना",
   "सिंचाई के लिए दो नदियों को जोड़ना, और साथ ही नीचे की ओर डॉल्फ़िन और घड़ियालों के लिए पर्याप्त प्रवाह बनाए रखना",
   "मध्य भारत में कोयला खनन की अनुमति देना, और साथ ही कोयला क्षेत्रों से गुज़रने वाले हाथी गलियारों को खुला रखना"],
  0,
  "In 2021 the Court had ordered overhead lines in the bustard's habitat in Rajasthan and Gujarat to be laid underground. The Union Government pointed out that this would hold up the solar and wind projects needed to meet India's climate commitments, which also protect people from climate harm. "
  "In 2024 the Court modified the blanket order, set up an expert committee to identify priority areas for undergrounding and bird diverters, and in doing so read a right against the adverse effects of climate change into Articles 14 and 21. The other options describe real conflicts, but not this case.",
  "2021 में न्यायालय ने राजस्थान और गुजरात में सोन चिरैया के आवास की ऊपरी लाइनों को भूमिगत करने का आदेश दिया था। केंद्र सरकार ने बताया कि इससे भारत की जलवायु प्रतिबद्धताओं के लिए आवश्यक सौर और पवन परियोजनाएँ रुकेंगी, जो लोगों को जलवायु-हानि से भी बचाती हैं। "
  "2024 में न्यायालय ने व्यापक आदेश में संशोधन किया, भूमिगत लाइनों और पक्षी-विचलकों के प्राथमिक क्षेत्र चिह्नित करने के लिए एक विशेषज्ञ समिति बनाई, और ऐसा करते हुए अनुच्छेद 14 और 21 में जलवायु परिवर्तन के प्रतिकूल प्रभावों के विरुद्ध अधिकार पढ़ा। अन्य विकल्प वास्तविक टकरावों का वर्णन करते हैं, पर इस मामले का नहीं।",
  "Supreme Court of India -- M.K. Ranjitsinh v. Union of India (2024).", "env-ranjitsinh-climate-right", craft="linkage")

M(LAW, "medium", "An Eco-Sensitive Zone has been notified around a national park. Which one of the following would generally be prohibited in it?",
  "एक राष्ट्रीय उद्यान के चारों ओर पर्यावरण-संवेदी क्षेत्र (इको-सेंसिटिव ज़ोन) अधिसूचित किया गया है। उसमें सामान्यतः निम्नलिखित में से किस पर रोक होगी?",
  ["A new stone quarry with a crushing unit",
   "Farming already carried on by local villagers",
   "Rainwater harvesting by the village panchayat",
   "A switch to organic farming by local growers"],
  ["पत्थर-पिसाई इकाई सहित एक नई पत्थर खदान",
   "स्थानीय ग्रामीणों द्वारा पहले से की जा रही खेती",
   "ग्राम पंचायत द्वारा वर्षा-जल संचयन",
   "स्थानीय उत्पादकों द्वारा जैविक खेती अपनाना"],
  0,
  "Eco-Sensitive Zones are buffers around protected areas, notified by the Environment Ministry under the Environment (Protection) Act, 1986. They do not empty the land of people; they sort activities into three lists. "
  "Commercial mining, stone quarrying and crushing, polluting industries, major hydroelectric projects, saw mills and brick kilns are generally prohibited. Activities such as hotels, felling of trees and new roads are regulated. Ongoing farming by local communities, rainwater harvesting, organic farming and renewable energy are permitted, and are even encouraged.",
  "पर्यावरण-संवेदी क्षेत्र संरक्षित क्षेत्रों के चारों ओर के बफ़र हैं, जिन्हें पर्यावरण मंत्रालय पर्यावरण (संरक्षण) अधिनियम, 1986 के तहत अधिसूचित करता है। वे भूमि को लोगों से ख़ाली नहीं करते; वे गतिविधियों को तीन सूचियों में बाँटते हैं। "
  "वाणिज्यिक खनन, पत्थर उत्खनन और पिसाई, प्रदूषणकारी उद्योग, बड़ी जलविद्युत परियोजनाएँ, आरा मिलें और ईंट-भट्ठे सामान्यतः प्रतिबंधित हैं। होटल, वृक्ष-कटाई और नई सड़कें जैसी गतिविधियाँ विनियमित हैं। स्थानीय समुदायों की चल रही खेती, वर्षा-जल संचयन, जैविक खेती और नवीकरणीय ऊर्जा अनुमत हैं, बल्कि उन्हें प्रोत्साहित किया जाता है।",
  MOEF + " -- Guidelines for declaration of Eco-Sensitive Zones around National Parks and Wildlife Sanctuaries (2011).", "env-eco-sensitive-zones", craft="application")

M(LAW, "medium", "A cluster of tanneries has polluted a river so badly that farmland downstream is ruined. Under the principle that the Supreme Court read into Indian law in Vellore Citizens' Welfare Forum (1996), the cost of restoring the damaged environment must be borne by:",
  "चमड़ा-शोधन इकाइयों (टैनरी) के एक समूह ने एक नदी को इतना प्रदूषित कर दिया है कि नीचे की ओर की कृषि-भूमि नष्ट हो गई है। वेल्लोर सिटिज़न्स वेलफ़ेयर फ़ोरम (1996) में सर्वोच्च न्यायालय ने जिस सिद्धांत को भारतीय क़ानून का भाग माना, उसके अनुसार क्षतिग्रस्त पर्यावरण की बहाली की लागत किसे उठानी होगी?",
  ["the tanneries that caused it",
   "the State Pollution Control Board, which failed to stop them",
   "the downstream farmers, who benefit from a restored river",
   "the Union Government, from the National Clean Energy Fund"],
  ["उन टैनरियों को जिन्होंने इसे किया",
   "राज्य प्रदूषण नियंत्रण बोर्ड को, जो उन्हें रोकने में विफल रहा",
   "नीचे के किसानों को, जिन्हें बहाल नदी से लाभ होगा",
   "केंद्र सरकार को, राष्ट्रीय स्वच्छ ऊर्जा कोष से"],
  0,
  "In Vellore Citizens' Welfare Forum, about tanneries polluting the Palar river in Tamil Nadu, the Court held that the precautionary principle and the polluter pays principle are part of the law of India. Under polluter pays, the polluter's liability covers compensating the victims and also the cost of restoring the environment it has degraded. "
  "Regulators may be faulted for failing to act, but that does not shift the bill onto the public or onto the victims.",
  "वेल्लोर सिटिज़न्स वेलफ़ेयर फ़ोरम में, जो तमिलनाडु की पालार नदी को प्रदूषित करने वाली टैनरियों से जुड़ा था, न्यायालय ने माना कि एहतियाती सिद्धांत और 'प्रदूषक भुगतान करे' सिद्धांत भारत के क़ानून का भाग हैं। इसके तहत प्रदूषक का दायित्व पीड़ितों को क्षतिपूर्ति देने के साथ-साथ उसके द्वारा क्षरित पर्यावरण की बहाली की लागत तक जाता है। "
  "नियामकों को कार्रवाई न करने के लिए दोषी ठहराया जा सकता है, पर इससे बोझ जनता या पीड़ितों पर नहीं जाता।",
  "Supreme Court of India -- Vellore Citizens' Welfare Forum v. Union of India (1996).", "env-vellore-precautionary-polluter-pays", craft="application")

S(LAW, "easy", "Consider the following statements about the Wildlife Crime Control Bureau:",
  "वन्यजीव अपराध नियंत्रण ब्यूरो के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Because organised wildlife crime crosses State and national borders, the Bureau gathers intelligence and works with customs, the police of different States and international bodies such as Interpol.",
   "It works under the Ministry of Home Affairs."],
  ["चूँकि संगठित वन्यजीव अपराध राज्यों और देशों की सीमाएँ पार करता है, इसलिए ब्यूरो आसूचना जुटाता है और सीमा-शुल्क, विभिन्न राज्यों की पुलिस तथा इंटरपोल जैसी अंतरराष्ट्रीय संस्थाओं के साथ काम करता है।",
   "यह गृह मंत्रालय के अधीन काम करता है।"],
  T2, 0,
  "Only statement 1 is correct. Poached tiger parts, pangolin scales, ivory and red sanders move through networks that span several States and end in markets abroad, beyond the reach of any one State's forest department; so the 2006 amendment to the Wild Life (Protection) Act created a statutory bureau to collect intelligence, help States and customs, and coordinate with Interpol and the CITES Secretariat. "
  "Statement 2 is wrong: it works under the Ministry of Environment, Forest and Climate Change.",
  "केवल कथन 1 सही है। शिकार किए गए बाघ के अंग, पैंगोलिन के शल्क, हाथीदाँत और लाल चंदन ऐसे तंत्रों से होकर जाते हैं जो कई राज्यों में फैले हैं और विदेशी बाज़ारों में ख़त्म होते हैं, किसी एक राज्य के वन विभाग की पहुँच से बाहर; इसलिए वन्यजीव (संरक्षण) अधिनियम के 2006 के संशोधन ने आसूचना जुटाने, राज्यों और सीमा-शुल्क की सहायता करने तथा इंटरपोल और CITES सचिवालय से समन्वय के लिए एक वैधानिक ब्यूरो बनाया। "
  "कथन 2 गलत है: यह पर्यावरण, वन और जलवायु परिवर्तन मंत्रालय के अधीन काम करता है।",
  "Wild Life (Protection) Act, 1972, Chapter IVC.", "env-wildlife-crime-control-bureau", craft="linkage")

S(LAW, "medium", "A forest-dwelling community in central India wants its right to collect and sell bamboo from the forest it has used for generations recognised under the Forest Rights Act, 2006. Consider the following statements:",
  "मध्य भारत का एक वनवासी समुदाय चाहता है कि जिस वन का वह पीढ़ियों से उपयोग करता आया है, उससे बाँस इकट्ठा करने और बेचने के उसके अधिकार को वन अधिकार अधिनियम, 2006 के तहत मान्यता मिले। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The process of determining the right begins with the Gram Sabha.",
   "Bamboo counts as minor forest produce under the Act, so the community can claim the right to own and sell it.",
   "The claim can succeed only if the community's members are Scheduled Tribes."],
  ["अधिकार निर्धारित करने की प्रक्रिया ग्राम सभा से शुरू होती है।",
   "अधिनियम के तहत बाँस लघु वनोपज में गिना जाता है, इसलिए समुदाय उस पर स्वामित्व और उसे बेचने के अधिकार का दावा कर सकता है।",
   "दावा तभी सफल हो सकता है जब समुदाय के सदस्य अनुसूचित जनजाति के हों।"],
  C3, 1,
  "Statements 1 and 2 are correct. Under the Act the Gram Sabha receives and verifies claims and passes them to the sub-divisional and district committees. The Act defines minor forest produce to include bamboo, tendu leaves, honey, lac and medicinal plants, and it gives forest dwellers the right to own, collect, use and sell it; villages such as Mendha Lekha in Maharashtra used this to take bamboo out of the forest department's monopoly. "
  "Statement 3 is wrong: 'other traditional forest dwellers' can also claim, if they show that they have lived in and depended on the forest for three generations (75 years) before December 2005.",
  "कथन 1 और 2 सही हैं। अधिनियम के तहत ग्राम सभा दावे प्राप्त कर उनका सत्यापन करती है और उन्हें उप-मंडल और ज़िला समितियों को भेजती है। अधिनियम लघु वनोपज में बाँस, तेंदू पत्ता, शहद, लाख और औषधीय पौधों को शामिल करता है, और वनवासियों को उस पर स्वामित्व, संग्रह, उपयोग और बिक्री का अधिकार देता है; महाराष्ट्र के मेंढा लेखा जैसे गाँवों ने इसी से बाँस को वन विभाग के एकाधिकार से निकाला। "
  "कथन 3 गलत है: 'अन्य परंपरागत वनवासी' भी दावा कर सकते हैं, यदि वे दिखाएँ कि वे दिसंबर 2005 से पहले तीन पीढ़ियों (75 वर्ष) से वन में रहते और उस पर निर्भर रहे हैं।",
  "Ministry of Tribal Affairs -- Scheduled Tribes and Other Traditional Forest Dwellers (Recognition of Forest Rights) Act, 2006.", "env-forest-rights-act-2006", craft="application")

# ================================================================ CONVENTIONS & ORGANISATIONS (8)
M(CON, "hard", "At COP16 of the Convention on Biological Diversity (2024), countries set up the 'Cali Fund', into which companies that use digital sequence information on genetic resources are expected to pay. The fund is meant to correct the problem that:",
  "जैव विविधता अभिसमय के COP16 (2024) में देशों ने 'काली फ़ंड' बनाया, जिसमें आनुवंशिक संसाधनों की डिजिटल अनुक्रम सूचना का उपयोग करने वाली कंपनियों से योगदान की अपेक्षा है। यह कोष जिस समस्या को सुधारने के लिए है, वह यह है कि:",
  ["firms profit from genetic data from biodiverse countries without sharing the benefits",
   "genetic sequences stored in open online databases can be stolen or altered by hackers",
   "genetically modified crops can spread their new genes into the wild relatives of crop plants",
   "seed banks in poorer countries lack the money to store duplicate samples of their crops"],
  ["कंपनियाँ जैव-विविधता-समृद्ध देशों से प्राप्त आनुवंशिक आँकड़ों से लाभ कमाती हैं, पर लाभ साझा नहीं करतीं",
   "खुले ऑनलाइन डेटाबेस में रखे आनुवंशिक अनुक्रम हैकरों द्वारा चुराए या बदले जा सकते हैं",
   "आनुवंशिक रूप से संशोधित फ़सलें अपने जीन फ़सलों के जंगली संबंधियों में फैला सकती हैं",
   "ग़रीब देशों के बीज बैंकों के पास अपनी फ़सलों के दोहरे नमूने रखने का पैसा नहीं है"],
  0,
  "The CBD and its Nagoya Protocol require that benefits from using genetic resources be shared fairly with the countries and communities they come from. But once a plant's or microbe's genome is sequenced and uploaded, companies can use the data for drugs, cosmetics or seeds without ever touching the physical sample, so access-and-benefit-sharing rules are bypassed. "
  "The Cali Fund asks large users of such data to contribute -- a suggested 1 per cent of profits or 0.1 per cent of revenue -- with half of the money meant for Indigenous peoples and local communities. Gene flow from GM crops is a biosafety issue, and data theft and seed-bank funding are separate concerns.",
  "जैव विविधता अभिसमय और उसका नागोया प्रोटोकॉल अपेक्षा करते हैं कि आनुवंशिक संसाधनों के उपयोग के लाभ उन देशों और समुदायों के साथ न्यायपूर्ण ढंग से बाँटे जाएँ जहाँ से वे आते हैं। पर किसी पौधे या सूक्ष्मजीव के जीनोम का अनुक्रम बनकर ऑनलाइन चढ़ जाने के बाद कंपनियाँ भौतिक नमूने को छुए बिना उसका उपयोग दवाओं, सौंदर्य-प्रसाधनों या बीजों में कर सकती हैं, जिससे पहुँच और लाभ-साझेदारी के नियम दरकिनार हो जाते हैं। "
  "काली फ़ंड ऐसे आँकड़ों के बड़े उपयोगकर्ताओं से योगदान माँगता है, सुझाव के रूप में लाभ का 1 प्रतिशत या राजस्व का 0.1 प्रतिशत, और उसका आधा धन मूलनिवासी लोगों और स्थानीय समुदायों के लिए है। GM फ़सलों से जीन-प्रवाह जैव-सुरक्षा का विषय है, और डेटा-चोरी तथा बीज-बैंकों का धन अलग चिंताएँ हैं।",
  "Convention on Biological Diversity -- COP16 decision on digital sequence information (2024).", "env-cali-fund-dsi", craft="linkage")

M(CON, "medium", "WWF's Living Planet Report 2024 found that the Living Planet Index -- which tracks thousands of monitored populations of wild vertebrates -- fell by 73 per cent on average between 1970 and 2020. Which one of the following can be correctly concluded from this?",
  "WWF की 'लिविंग प्लैनेट रिपोर्ट 2024' ने पाया कि 'लिविंग प्लैनेट इंडेक्स', जो जंगली कशेरुकी जीवों की हज़ारों निगरानी वाली समष्टियों पर नज़र रखता है, 1970 और 2020 के बीच औसतन 73 प्रतिशत गिरा। इससे निम्नलिखित में से कौन-सा निष्कर्ष सही रूप से निकाला जा सकता है?",
  ["The monitored populations shrank by 73 per cent on average",
   "73 per cent of all vertebrate species have gone extinct since 1970",
   "The total number of wild animals fell by exactly 73 per cent",
   "Freshwater populations declined less than those on land"],
  ["निगरानी वाली समष्टियाँ औसतन 73 प्रतिशत छोटी हुईं",
   "1970 के बाद से सभी कशेरुकी प्रजातियों में से 73 प्रतिशत विलुप्त हो चुकी हैं",
   "जंगली जीवों की कुल संख्या ठीक 73 प्रतिशत गिरी",
   "मीठे पानी की समष्टियाँ स्थल की समष्टियों से कम घटीं"],
  0,
  "The index averages the relative change in the size of about 35,000 tracked populations of some 5,500 species. A 73 per cent fall means that, on average, those populations are about a quarter of their 1970 size; it does not mean that 73 per cent of species are extinct, and because it averages percentage changes, it is not a head-count of all wild animals. "
  "Freshwater populations showed the steepest fall, about 85 per cent, followed by land and then marine populations; by region, Latin America and the Caribbean declined most.",
  "यह सूचकांक लगभग 5,500 प्रजातियों की लगभग 35,000 निगरानी वाली समष्टियों के आकार में सापेक्ष परिवर्तन का औसत है। 73 प्रतिशत की गिरावट का अर्थ है कि औसतन वे समष्टियाँ अपने 1970 के आकार की लगभग एक-चौथाई रह गई हैं; इसका अर्थ यह नहीं कि 73 प्रतिशत प्रजातियाँ विलुप्त हो गईं, और चूँकि यह प्रतिशत परिवर्तनों का औसत है, यह सभी जंगली जीवों की गिनती नहीं है। "
  "मीठे पानी की समष्टियों में सबसे तीव्र गिरावट, लगभग 85 प्रतिशत, दिखी, उसके बाद स्थलीय और फिर समुद्री समष्टियाँ; क्षेत्रवार लैटिन अमेरिका और कैरिबियन में सबसे अधिक गिरावट हुई।",
  "WWF -- Living Planet Report 2024.", "env-living-planet-report", craft="inference")

M(CON, "medium", "Which one of the following would count towards a country's pledge under the 'Bonn Challenge'?",
  "निम्नलिखित में से कौन-सा कार्य 'बॉन चैलेंज' के तहत किसी देश के संकल्प में गिना जाएगा?",
  ["Bringing degraded farmland back into use through agroforestry",
   "Declaring a new marine protected area on the high seas off its coast",
   "Retiring its oldest coal-fired power plants well before the year 2035",
   "Halving the amount of food wasted in its shops, hotels and homes"],
  ["कृषि-वानिकी के माध्यम से क्षरित कृषि-भूमि को फिर उपयोग में लाना",
   "अपने तट से दूर खुले समुद्र में एक नया समुद्री संरक्षित क्षेत्र घोषित करना",
   "2035 से काफ़ी पहले अपने सबसे पुराने कोयला-बिजलीघरों को बंद करना",
   "अपनी दुकानों, होटलों और घरों में बर्बाद होने वाले भोजन को आधा करना"],
  0,
  "The Bonn Challenge, launched by Germany and the IUCN in 2011, aims to bring 350 million hectares of deforested and degraded land into restoration by 2030. It follows the forest landscape restoration approach, so it counts not only new forests but also trees on farms, agroforestry, regenerated woodland and restored watersheds that make degraded land productive again. "
  "Marine reserves, coal retirement and food waste belong to other global goals.",
  "बॉन चैलेंज, जो 2011 में जर्मनी और IUCN ने शुरू किया, 2030 तक 35 करोड़ हेक्टेयर वनरहित और क्षरित भूमि को पुनर्स्थापन में लाना चाहता है। यह वन-भूदृश्य पुनर्स्थापन की दृष्टि अपनाता है, इसलिए इसमें केवल नए वन नहीं, बल्कि खेतों पर वृक्ष, कृषि-वानिकी, पुनर्जीवित वनभूमि और बहाल जलागम भी गिने जाते हैं जो क्षरित भूमि को फिर उत्पादक बनाते हैं। "
  "समुद्री रिज़र्व, कोयला-बिजलीघर बंद करना और भोजन की बर्बादी अन्य वैश्विक लक्ष्यों से जुड़े हैं।",
  "IUCN -- The Bonn Challenge.", "env-bonn-challenge", craft="application")

S(CON, "hard", "Consider the following statements about the Agreement on Marine Biological Diversity of Areas beyond National Jurisdiction (the 'High Seas Treaty'):",
  "राष्ट्रीय अधिकार-क्षेत्र से परे क्षेत्रों की समुद्री जैव विविधता पर समझौते ('हाई सीज़ ट्रीटी') के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It was needed because about two-thirds of the ocean lies beyond national jurisdiction, where no single country can set up a marine protected area that binds others.",
   "It is an implementing agreement under the United Nations Convention on the Law of the Sea.",
   "Under it, a coastal State needs the treaty's approval to set up a marine protected area inside its own exclusive economic zone.",
   "India has stayed out of it."],
  ["इसकी आवश्यकता इसलिए थी कि महासागर का लगभग दो-तिहाई भाग राष्ट्रीय अधिकार-क्षेत्र से परे है, जहाँ कोई एक देश ऐसा समुद्री संरक्षित क्षेत्र नहीं बना सकता जो दूसरों पर बाध्यकारी हो।",
   "यह संयुक्त राष्ट्र समुद्री क़ानून अभिसमय (UNCLOS) के तहत एक कार्यान्वयन समझौता है।",
   "इसके तहत किसी तटीय देश को अपने ही अनन्य आर्थिक क्षेत्र के भीतर समुद्री संरक्षित क्षेत्र बनाने के लिए संधि की स्वीकृति चाहिए।",
   "भारत इससे बाहर रहा है।"],
  C4, 1,
  "Statements 1 and 2 are correct. The high seas begin 200 nautical miles out, and until now there was no legal means of protecting them as a whole: fishing, shipping and seabed mining were each governed by separate bodies. The Agreement, adopted in 2023 as the third implementing agreement under UNCLOS, sets up area-based tools including marine protected areas there, requires environmental impact assessments, and provides for sharing the benefits of marine genetic resources. "
  "Statement 3 is wrong: it applies only beyond national jurisdiction, so a State's own exclusive economic zone stays under that State's laws. Statement 4 is wrong: India signed it in September 2024.",
  "कथन 1 और 2 सही हैं। खुला समुद्र 200 समुद्री मील के बाद शुरू होता है, और अब तक उसे समग्र रूप से संरक्षित करने का कोई क़ानूनी साधन नहीं था: मत्स्यन, नौवहन और समुद्र-तल खनन अलग-अलग निकायों के अधीन थे। 2023 में UNCLOS के तीसरे कार्यान्वयन समझौते के रूप में अपनाया गया यह समझौता वहाँ समुद्री संरक्षित क्षेत्रों सहित क्षेत्र-आधारित साधन बनाता है, पर्यावरणीय प्रभाव आकलन अनिवार्य करता है, और समुद्री आनुवंशिक संसाधनों के लाभ बाँटने का प्रावधान करता है। "
  "कथन 3 गलत है: यह केवल राष्ट्रीय अधिकार-क्षेत्र से परे लागू होता है, इसलिए किसी देश का अपना अनन्य आर्थिक क्षेत्र उसी देश के क़ानूनों के अधीन रहता है। कथन 4 गलत है: भारत ने सितंबर 2024 में इस पर हस्ताक्षर किए।",
  "United Nations -- Agreement under UNCLOS on the conservation and sustainable use of marine biological diversity of areas beyond national jurisdiction (2023).", "env-bbnj-high-seas", craft="inference")

S(CON, "hard", "Consider the following statements about the Intergovernmental Science-Policy Platform on Biodiversity and Ecosystem Services (IPBES):",
  "जैव विविधता और पारितंत्र सेवाओं पर अंतरसरकारी विज्ञान-नीति मंच (IPBES) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Like the IPCC, it assesses the published evidence for governments rather than carrying out its own research.",
   "Its 2019 Global Assessment found that changes in the use of land and sea have been the largest direct driver of nature's decline, ahead of climate change.",
   "Since it was set up under the Convention on Biological Diversity, its assessments are binding on the Parties to that Convention.",
   "Its secretariat is in Bonn, Germany."],
  ["IPCC की तरह यह अपना शोध करने के बजाय सरकारों के लिए प्रकाशित साक्ष्यों का आकलन करता है।",
   "इसके 2019 के वैश्विक आकलन ने पाया कि भूमि और समुद्र के उपयोग में परिवर्तन प्रकृति के ह्रास का सबसे बड़ा प्रत्यक्ष कारक रहे हैं, जलवायु परिवर्तन से आगे।",
   "चूँकि इसे जैव विविधता अभिसमय के तहत बनाया गया, इसलिए इसके आकलन उस अभिसमय के पक्षकारों पर बाध्यकारी हैं।",
   "इसका सचिवालय बॉन, जर्मनी में है।"],
  C4, 2,
  "Statements 1, 2 and 4 are correct. IPBES, set up at Panama City in 2012, does for nature what the IPCC does for climate: experts review the evidence, and governments approve the summaries. Its 2019 Global Assessment ranked the direct drivers as changes in land and sea use, then direct exploitation of organisms, climate change, pollution and invasive alien species, and estimated that about a million species face extinction. "
  "Statement 3 is wrong on both counts: IPBES is an independent intergovernmental body, with UNEP providing its secretariat in Bonn, and its assessments inform conventions such as the CBD but bind no one.",
  "कथन 1, 2 और 4 सही हैं। 2012 में पनामा सिटी में बना IPBES प्रकृति के लिए वही करता है जो IPCC जलवायु के लिए: विशेषज्ञ साक्ष्यों की समीक्षा करते हैं, और सरकारें सारांश स्वीकृत करती हैं। इसके 2019 के वैश्विक आकलन ने प्रत्यक्ष कारकों को इस क्रम में रखा: भूमि और समुद्र के उपयोग में परिवर्तन, फिर जीवों का प्रत्यक्ष दोहन, जलवायु परिवर्तन, प्रदूषण और आक्रामक विदेशी प्रजातियाँ, और अनुमान लगाया कि लगभग दस लाख प्रजातियाँ विलुप्ति के ख़तरे में हैं। "
  "कथन 3 दोनों दृष्टियों से गलत है: IPBES एक स्वतंत्र अंतरसरकारी निकाय है, जिसका सचिवालय UNEP बॉन में चलाता है, और इसके आकलन जैव विविधता अभिसमय जैसे अभिसमयों को जानकारी देते हैं पर किसी पर बाध्यकारी नहीं हैं।",
  "IPBES -- Global Assessment Report on Biodiversity and Ecosystem Services (2019).", "env-ipbes", craft="linkage")

S(CON, "medium", "Consider the following statements about the Minamata Convention:",
  "मिनामाता अभिसमय के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["A global treaty was needed because mercury released by burning coal and by small-scale gold mining travels long distances in the air and builds up in fish far from its source.",
   "It is named after a Japanese city where industrial mercury poisoning caused a serious disease.",
   "India has ratified it."],
  ["एक वैश्विक संधि इसलिए आवश्यक थी कि कोयला जलाने और छोटे पैमाने पर सोने के खनन से निकला पारा वायु में लंबी दूरी तय करता है और अपने स्रोत से बहुत दूर मछलियों में जमा होता है।",
   "इसका नाम उस जापानी शहर पर है जहाँ औद्योगिक पारा-विषाक्तता से एक गंभीर रोग हुआ।",
   "भारत ने इसका अनुसमर्थन किया है।"],
  C3, 2,
  "All three are correct. Mercury from coal combustion and from artisanal and small-scale gold mining, the largest source, rises as vapour, crosses borders and oceans, and is turned by microbes into methylmercury, which concentrates in large fish; no country can protect its people by acting alone. "
  "Adopted in 2013 and in force since 2017, the Convention controls mercury mining, trade and emissions and phases out or phases down its use in products such as certain batteries, thermometers, lamps and dental fillings. It takes its name from Minamata, where methylmercury in factory waste poisoned people who ate the bay's fish. India ratified it in 2018.",
  "तीनों कथन सही हैं। कोयला जलाने और कारीगर तथा छोटे पैमाने के सोने के खनन, जो सबसे बड़ा स्रोत है, से निकला पारा वाष्प बनकर उठता है, सीमाएँ और महासागर पार करता है, और सूक्ष्मजीव उसे मिथाइलमर्करी में बदल देते हैं, जो बड़ी मछलियों में सांद्र होता है; कोई देश अकेले कार्रवाई करके अपने लोगों की रक्षा नहीं कर सकता। "
  "2013 में अपनाया गया और 2017 से लागू यह अभिसमय पारे के खनन, व्यापार और उत्सर्जन को नियंत्रित करता है और कुछ बैटरियों, थर्मामीटरों, लैंपों और दाँतों की भराई जैसे उत्पादों में उसके उपयोग को समाप्त या कम करता है। इसका नाम मिनामाता पर है, जहाँ कारख़ाने के कचरे के मिथाइलमर्करी ने खाड़ी की मछली खाने वाले लोगों को विषाक्त किया। भारत ने 2018 में इसका अनुसमर्थन किया।",
  "UNEP -- Minamata Convention on Mercury.", "env-minamata-convention", craft="linkage")

S(CON, "medium", "Consider the following statements about the United Nations Convention to Combat Desertification (UNCCD):",
  "मरुस्थलीकरण से निपटने के संयुक्त राष्ट्र अभिसमय (UNCCD) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Under the goal of 'land degradation neutrality' that it promotes, losses of healthy land are to be balanced by restoring degraded land, so that the total amount of healthy land stays stable or grows.",
   "Its secretariat is in Nairobi.",
   "Since desertification occurs only in deserts, the Convention applies only to countries that have hot deserts."],
  ["इसके द्वारा बढ़ावा दिए गए 'भूमि क्षरण तटस्थता' के लक्ष्य के तहत स्वस्थ भूमि की हानियों को क्षरित भूमि की बहाली से संतुलित किया जाना है, ताकि स्वस्थ भूमि की कुल मात्रा स्थिर रहे या बढ़े।",
   "इसका सचिवालय नैरोबी में है।",
   "चूँकि मरुस्थलीकरण केवल मरुस्थलों में होता है, इसलिए यह अभिसमय केवल उन्हीं देशों पर लागू होता है जिनमें गर्म मरुस्थल हैं।"],
  C3, 0,
  "Only statement 1 is correct. Land degradation neutrality, also SDG target 15.3, accepts that some land will be degraded or built over, but requires that this be offset by restoring land elsewhere, so the stock of healthy, productive land does not shrink. "
  "Statement 2 is wrong: the secretariat is in Bonn. Statement 3 is wrong: desertification means land degradation in drylands -- arid, semi-arid and dry sub-humid areas -- caused by climatic variation and human activity; it is not the spread of existing deserts, and most of India's degraded land lies outside the Thar.",
  "केवल कथन 1 सही है। भूमि क्षरण तटस्थता, जो SDG लक्ष्य 15.3 भी है, यह मानती है कि कुछ भूमि क्षरित होगी या उस पर निर्माण होगा, पर अपेक्षा करती है कि इसकी भरपाई अन्यत्र भूमि की बहाली से हो, ताकि स्वस्थ, उत्पादक भूमि का भंडार न घटे। "
  "कथन 2 गलत है: सचिवालय बॉन में है। कथन 3 गलत है: मरुस्थलीकरण का अर्थ शुष्क भूमि, यानी शुष्क, अर्ध-शुष्क और शुष्क उप-आर्द्र क्षेत्रों, में जलवायु-परिवर्तनशीलता और मानवीय गतिविधियों से होने वाला भूमि-क्षरण है; यह मौजूदा मरुस्थलों का फैलाव नहीं है, और भारत की अधिकांश क्षरित भूमि थार के बाहर है।",
  "UNCCD -- Land Degradation Neutrality.", "env-unccd-india", craft="linkage")

S(CON, "easy", "Consider the following statements about the United Nations Environment Programme (UNEP):",
  "संयुक्त राष्ट्र पर्यावरण कार्यक्रम (UNEP) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It was set up after the 1972 United Nations Conference on the Human Environment at Stockholm.",
   "Since it is a programme of the UN rather than a specialised agency, it depends largely on voluntary contributions from countries."],
  ["इसे 1972 के स्टॉकहोम में हुए संयुक्त राष्ट्र मानव पर्यावरण सम्मेलन के बाद बनाया गया।",
   "चूँकि यह विशिष्ट एजेंसी के बजाय संयुक्त राष्ट्र का एक कार्यक्रम है, इसलिए यह मुख्यतः देशों के स्वैच्छिक योगदान पर निर्भर है।"],
  T2, 2,
  "Both statements are correct. UNEP was created by the UN General Assembly in December 1972, following the Stockholm Conference, and is based in Nairobi. Specialised agencies such as the WHO or the FAO have their own member States and assessed contributions; UNEP is a subsidiary programme of the General Assembly, so apart from a small share of the UN regular budget it relies on its voluntary Environment Fund and on earmarked contributions, which is why its budget is modest compared with its mandate.",
  "दोनों कथन सही हैं। UNEP को स्टॉकहोम सम्मेलन के बाद दिसंबर 1972 में संयुक्त राष्ट्र महासभा ने बनाया, और यह नैरोबी में स्थित है। WHO या FAO जैसी विशिष्ट एजेंसियों के अपने सदस्य-देश और निर्धारित अंशदान होते हैं; UNEP महासभा का एक सहायक कार्यक्रम है, इसलिए संयुक्त राष्ट्र के नियमित बजट के एक छोटे हिस्से के अलावा यह अपने स्वैच्छिक पर्यावरण कोष और निर्धारित-उद्देश्य वाले योगदानों पर निर्भर है, इसीलिए इसका बजट इसके दायित्व की तुलना में मामूली है।",
  "United Nations Environment Programme.", "env-unep-stockholm", craft="linkage")

if __name__ == "__main__":
    write_updates("upg_l2_t11_env_a.sql", statuses=("draft", "published"))
