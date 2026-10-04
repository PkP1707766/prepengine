# -*- coding: utf-8 -*-
"""Level 2 · Test 14 (Geography 3) -- depth audit of 2026-10-04, part B: Transport, Ports & Human Geography, and the
craft tags for the 65 kept rows (docs/upsc-question-design-standard.md §6). Part A is upg_l2_t14_geo_a.py.

Part B rewrites 18 recall rows in place with the same concept id, type and difficulty:
  - analytic: why Mumbai became a great port and why towns keep growing; schemes identified from what a
    State wants (Sagarmala, UDAN); why a crude pipeline starts on the Gulf of Kachchh; why roads win over
    short distances; what Chabahar and Kaladan bypass; what three new works make possible; why freight
    corridors and dredging matter; what suits Vizhinjam for transshipment; what Haryana's sex ratio
    points to; and what squeezes the Maasai;
  - precision: near-miss versions of the Census facts, the HDI's origin, the waterways count, the west-coast
    ports and the Golden Quadrilateral's corners.
Three kept rows are tagged on their honest content: the Kochi-Kandla-New Mangalore row states why each port
was built (linkage); the Census-2027 row turns on the statute it is held under, and the capacity-mix row on a
dated change (precision).
Test 14 after both parts: analytic 47, precision 25, recall 30.
Leaks avoided while drafting:
  - Ennore as a near-miss (repeats the ports pairs' pair 4);
  - Ankleshwar in a pipeline distractor (answers the oil-fields row's statement 4);
  - the North-South corridor's ends in a Golden Quadrilateral distractor (the road-corridors row);
  - Africa's high birth rate as a reason (answers the demographic-transition row's statement 2)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write_updates, CODE
from polity_common import C3, C4, T2

d.SUBJECT = "Geography"
d.REQUIRE_CRAFT = True
TH = "Transport, Ports & Human Geography"
NC10 = "NCERT Class X, Contemporary India II"
NC12 = "NCERT Class XII, India: People and Economy"
NCH = "NCERT Class XII, Fundamentals of Human Geography"

# ================================================================ ARs (2)
A(TH, "easy",
  "Mumbai grew into one of India's leading ports.",
  "मुंबई भारत के प्रमुख बंदरगाहों में से एक बना।",
  "It has a large, deep natural harbour sheltered between the island city and the mainland.",
  "इसके पास द्वीपीय नगर और मुख्य भूमि के बीच सुरक्षित एक बड़ा, गहरा प्राकृतिक बंदरगाह है।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I. Mumbai's harbour, protected between the island city and the mainland, gave ships deep, calm anchorage on the Arabian Sea coast; with the opening of the Suez Canal and rail links to the cotton districts of the Deccan, it became India's gateway to the West. "
  "Jawaharlal Nehru Port, across the harbour, was built later to share the load.",
  "दोनों कथन सही हैं, और कथन-II कथन-I की व्याख्या करता है। द्वीपीय नगर और मुख्य भूमि के बीच सुरक्षित मुंबई के बंदरगाह ने अरब सागर तट पर जहाज़ों को गहरा, शांत लंगरगाह दिया; स्वेज़ नहर खुलने और दक्कन के कपास ज़िलों से रेल संपर्क के साथ यह पश्चिम के लिए भारत का द्वार बन गया। "
  "बंदरगाह के पार जवाहरलाल नेहरू पोर्ट बाद में भार बाँटने के लिए बनाया गया।",
  NC12, "tr-mumbai-port-easy", craft="linkage")

A(TH, "medium",
  "The share of India's population living in towns and cities has been rising over the decades.",
  "भारत की जनसंख्या में नगरों और शहरों में रहने वालों का अनुपात दशकों से बढ़ रहा है।",
  "Jobs in industry and services, which are concentrated in towns, have grown faster than jobs in farming.",
  "उद्योग और सेवाओं की नौकरियाँ, जो नगरों में केंद्रित हैं, खेती की नौकरियों से तेज़ी से बढ़ी हैं।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I. The urban share rose from about 17 per cent in 1951 to about 31 per cent in 2011 and has kept rising, as people move to towns for work in manufacturing, construction and services, and as large villages that turn non-agricultural are reclassified as towns. "
  "Even so, most Indians still live in villages.",
  "दोनों कथन सही हैं, और कथन-II कथन-I की व्याख्या करता है। नगरीय अनुपात 1951 के लगभग 17 प्रतिशत से 2011 में लगभग 31 प्रतिशत हो गया और बढ़ता रहा है, क्योंकि लोग विनिर्माण, निर्माण और सेवाओं के काम के लिए नगरों में आते हैं, और जो बड़े गाँव ग़ैर-कृषि बन जाते हैं, उन्हें नगर के रूप में पुनर्वर्गीकृत किया जाता है। "
  "फिर भी अधिकांश भारतीय अब भी गाँवों में रहते हैं।",
  NC12, "hum-urban-share-rising", craft="linkage")

# ================================================================ MCQs (6)
M(TH, "medium", "A coastal State plans to modernise a port, build new rail and road links to its hinterland, promote coastal shipping and set up a coastal economic zone around the port. The Union programme designed for this is:",
  "एक तटीय राज्य एक बंदरगाह का आधुनिकीकरण करने, उसके पृष्ठ-प्रदेश तक नई रेल और सड़कें बनाने, तटीय नौवहन को बढ़ावा देने और बंदरगाह के चारों ओर तटीय आर्थिक क्षेत्र बनाने की योजना बनाता है। इसके लिए बनाया गया केंद्रीय कार्यक्रम है:",
  ["Sagarmala", "Bharatmala Pariyojana", "Jal Marg Vikas Project", "Pradhan Mantri Gram Sadak Yojana"],
  ["सागरमाला", "भारतमाला परियोजना", "जल मार्ग विकास परियोजना", "प्रधानमंत्री ग्राम सड़क योजना"],
  0,
  "Sagarmala, launched in 2015 under the Ministry of Ports, Shipping and Waterways, is the programme of port-led development: modernising ports and building new ones, connecting them to the hinterland, promoting coastal shipping and port-linked industry through coastal economic zones, and developing coastal communities. "
  "Bharatmala is the national highway programme, Jal Marg Vikas upgrades National Waterway 1 on the Ganga, and the Pradhan Mantri Gram Sadak Yojana builds rural roads.",
  "2015 में बंदरगाह, नौवहन और जलमार्ग मंत्रालय के अधीन शुरू हुआ सागरमाला बंदरगाह-आधारित विकास का कार्यक्रम है: बंदरगाहों का आधुनिकीकरण और नए बंदरगाह बनाना, उन्हें पृष्ठ-प्रदेश से जोड़ना, तटीय आर्थिक क्षेत्रों के माध्यम से तटीय नौवहन और बंदरगाह-आधारित उद्योग को बढ़ावा देना, और तटीय समुदायों का विकास। "
  "भारतमाला राष्ट्रीय राजमार्ग कार्यक्रम है, जल मार्ग विकास गंगा पर राष्ट्रीय जलमार्ग 1 का उन्नयन करता है, और प्रधानमंत्री ग्राम सड़क योजना ग्रामीण सड़कें बनाती है।",
  "Ministry of Ports, Shipping and Waterways -- Sagarmala Programme.", "tr-sagarmala", craft="application")

M(TH, "medium", "A State wants to start flights at capped fares from an unused airstrip in a hill district to its capital, with the Centre and the State sharing the cost through viability gap funding. The scheme designed for this is:",
  "एक राज्य एक पर्वतीय ज़िले की अप्रयुक्त हवाई पट्टी से अपनी राजधानी तक सीमित किराए वाली उड़ानें शुरू करना चाहता है, जिसकी लागत केंद्र और राज्य व्यवहार्यता अंतर निधि से बाँटें। इसके लिए बनाई गई योजना है:",
  ["the UDAN regional air scheme", "the Sagarmala programme", "the Bharatmala Pariyojana", "the Pradhan Mantri Gram Sadak Yojana"],
  ["उड़ान क्षेत्रीय संपर्क योजना", "सागरमाला कार्यक्रम", "भारतमाला परियोजना", "प्रधानमंत्री ग्राम सड़क योजना"],
  0,
  "UDAN ('Ude Desh ka Aam Nagrik'), launched in 2016, revives under-served airports, airstrips, heliports and water aerodromes: airlines bid for routes, fares on part of the seats are capped, and the Centre and the States pay viability gap funding so that people in smaller towns can afford to fly. "
  "The other three are port, highway and rural-road programmes.",
  "2016 में शुरू हुई उड़ान ('उड़े देश का आम नागरिक') कम उपयोग वाले हवाई अड्डों, हवाई पट्टियों, हेलीपोर्ट और जल-हवाई अड्डों को पुनर्जीवित करती है: एयरलाइनें मार्गों के लिए बोली लगाती हैं, कुछ सीटों का किराया सीमित रहता है, और केंद्र तथा राज्य व्यवहार्यता अंतर निधि देते हैं ताकि छोटे नगरों के लोग उड़ान का ख़र्च उठा सकें। "
  "अन्य तीन बंदरगाह, राजमार्ग और ग्रामीण सड़क कार्यक्रम हैं।",
  "Ministry of Civil Aviation -- UDAN Regional Connectivity Scheme.", "tr-udan-regional-air", craft="application")

M(TH, "medium", "The Salaya-Mathura pipeline begins on the Gulf of Kachchh coast of Gujarat and carries crude oil to refineries at Koyali, Panipat and Mathura. It begins there mainly because:",
  "सलाया-मथुरा पाइपलाइन गुजरात के कच्छ की खाड़ी के तट से शुरू होकर कोयली, पानीपत और मथुरा की रिफ़ाइनरियों तक कच्चा तेल ले जाती है। यह वहाँ से मुख्यतः इसलिए शुरू होती है कि:",
  ["crude imported by tanker from West Asia is landed there, close to the Gulf",
   "natural gas from Mumbai High is converted into crude oil there before being sent north",
   "the Gulf of Kachchh is the only stretch of India's coastline that is free of cyclones",
   "the inland refineries need sea water carried from the Gulf to cool their plants"],
  ["पश्चिम एशिया से टैंकरों द्वारा आयातित कच्चा तेल वहीं उतारा जाता है, खाड़ी देशों के निकट",
   "मुंबई हाई की प्राकृतिक गैस को उत्तर भेजने से पहले वहाँ कच्चे तेल में बदला जाता है",
   "कच्छ की खाड़ी भारत की तटरेखा का एकमात्र चक्रवात-मुक्त भाग है",
   "भीतरी रिफ़ाइनरियों को अपने संयंत्र ठंडे करने के लिए खाड़ी से लाया गया समुद्री जल चाहिए"],
  0,
  "India imports most of the crude it refines, much of it from West Asia, and the Gulf of Kachchh is the stretch of India's coast nearest to the Strait of Hormuz; single-point moorings at Vadinar and Salaya let very large tankers discharge offshore. From there the pipeline carries crude inland to refineries in Gujarat, Haryana and Uttar Pradesh, which is cheaper and safer than moving it by rail or road. "
  "Natural gas is not turned into crude, the Gujarat coast is hit by cyclones too, and refineries are cooled locally.",
  "भारत जितना कच्चा तेल शोधित करता है उसका अधिकांश आयात करता है, उसका बड़ा भाग पश्चिम एशिया से, और कच्छ की खाड़ी भारत के तट का होर्मुज़ जलडमरूमध्य से निकटतम भाग है; वाडिनार और सलाया पर एकल-बिंदु लंगर बहुत बड़े टैंकरों को अपतट पर तेल उतारने देते हैं। वहाँ से पाइपलाइन कच्चा तेल गुजरात, हरियाणा और उत्तर प्रदेश की रिफ़ाइनरियों तक ले जाती है, जो रेल या सड़क से ले जाने से सस्ता और सुरक्षित है। "
  "प्राकृतिक गैस कच्चे तेल में नहीं बदली जाती, गुजरात तट पर भी चक्रवात आते हैं, और रिफ़ाइनरियाँ स्थानीय रूप से ठंडी की जाती हैं।",
  NC12, "tr-salaya-mathura-crude", craft="linkage")

M(TH, "easy", "The Golden Quadrilateral highway network links:",
  "स्वर्णिम चतुर्भुज राजमार्ग नेटवर्क जोड़ता है:",
  ["Delhi, Mumbai, Chennai and Kolkata", "Delhi, Mumbai, Bengaluru and Kolkata", "Delhi, Kolkata, Chennai and Hyderabad", "Mumbai, Chennai, Kolkata and Guwahati"],
  ["दिल्ली, मुंबई, चेन्नई और कोलकाता", "दिल्ली, मुंबई, बेंगलुरु और कोलकाता", "दिल्ली, कोलकाता, चेन्नई और हैदराबाद", "मुंबई, चेन्नई, कोलकाता और गुवाहाटी"],
  0,
  "Built by the National Highways Authority of India under the National Highways Development Project from 1999, the Golden Quadrilateral joins the four metropolitan cities -- Delhi, Mumbai, Chennai and Kolkata -- with about 5,800 km of four- and six-lane highways. Bengaluru lies on its Mumbai-Chennai side and Hyderabad near it, but neither is a corner; Guwahati is not on it at all.",
  "भारतीय राष्ट्रीय राजमार्ग प्राधिकरण द्वारा 1999 से राष्ट्रीय राजमार्ग विकास परियोजना के तहत बनाया गया स्वर्णिम चतुर्भुज चार महानगरों, दिल्ली, मुंबई, चेन्नई और कोलकाता, को लगभग 5,800 किमी के चार और छह लेन वाले राजमार्गों से जोड़ता है। बेंगलुरु इसकी मुंबई-चेन्नई भुजा पर और हैदराबाद इसके पास है, पर दोनों में से कोई कोना नहीं है; गुवाहाटी इस पर है ही नहीं।",
  "National Highways Authority of India -- National Highways Development Project.", "tr-golden-quadrilateral-easy", craft="precision")

M(TH, "medium", "In the 2011 Census, Haryana had the lowest sex ratio among the States -- 879 women per 1,000 men -- and an even lower child sex ratio. The most likely main cause is:",
  "2011 की जनगणना में हरियाणा का लिंगानुपात राज्यों में सबसे कम था, प्रति 1,000 पुरुषों पर 879 महिलाएँ, और बाल लिंगानुपात इससे भी कम। इसका सबसे संभावित मुख्य कारण है:",
  ["sex-selective abortion arising from a strong preference for sons",
   "women in Haryana living much longer on average than its men do",
   "large numbers of young women leaving the State to work in other States",
   "the Census failing to count a large share of the men in the State"],
  ["पुत्रों के प्रति प्रबल वरीयता से उपजा लिंग-चयनात्मक गर्भपात",
   "हरियाणा की महिलाओं का औसतन पुरुषों से कहीं अधिक जीवित रहना",
   "बड़ी संख्या में युवा महिलाओं का काम के लिए दूसरे राज्यों में जाना",
   "जनगणना में राज्य के पुरुषों के बड़े भाग की गिनती न हो पाना"],
  0,
  "A low child sex ratio -- 834 girls per 1,000 boys aged 0-6 in Haryana in 2011 -- cannot be explained by migration for work, since young children do not migrate on their own; and women living longer, or men being missed by the Census, would raise the ratio of women to men, not lower it. "
  "It points to sex-selective abortion and the neglect of girls, driven by son preference and dowry and made easier by ultrasound scanning -- which is why the Pre-Conception and Pre-Natal Diagnostic Techniques Act bans sex determination, and why 'Beti Bachao Beti Padhao' was launched from Panipat in 2015.",
  "कम बाल लिंगानुपात, 2011 में हरियाणा में 0-6 वर्ष के प्रति 1,000 लड़कों पर 834 लड़कियाँ, काम के लिए प्रवास से नहीं समझाया जा सकता, क्योंकि छोटे बच्चे अपने आप प्रवास नहीं करते; और महिलाओं का अधिक जीना, या जनगणना में पुरुषों का छूट जाना, महिलाओं का अनुपात बढ़ाएगा, घटाएगा नहीं। "
  "यह लिंग-चयनात्मक गर्भपात और लड़कियों की उपेक्षा की ओर संकेत करता है, जो पुत्र-वरीयता और दहेज से प्रेरित है और अल्ट्रासाउंड जाँच से आसान हुई है; इसीलिए गर्भधारण-पूर्व और प्रसव-पूर्व निदान तकनीक अधिनियम लिंग-निर्धारण पर रोक लगाता है, और 2015 में पानीपत से 'बेटी बचाओ बेटी पढ़ाओ' शुरू किया गया।",
  "Office of the Registrar General and Census Commissioner, India -- Census 2011.", "hum-lowest-sex-ratio-haryana", craft="inference")

M(TH, "medium", "The Maasai of southern Kenya and northern Tanzania have long moved with their cattle across the savanna in search of grass and water. Their pastoral way of life is under growing pressure mainly because:",
  "दक्षिणी केन्या और उत्तरी तंज़ानिया के मसाई लंबे समय से घास और पानी की खोज में अपने मवेशियों के साथ सवाना में घूमते आए हैं। उनका पशुपालक जीवन मुख्यतः किस कारण बढ़ते दबाव में है?",
  ["grazing land has been taken for farms, towns and fenced wildlife parks",
   "the savanna is turning into dense tropical rainforest as rainfall rises",
   "the Sahara has advanced far south across the whole of Kenya and Tanzania",
   "all their cattle have been wiped out by a disease carried by tsetse flies"],
  ["चराई की भूमि खेतों, नगरों और बाड़बंद वन्यजीव उद्यानों के लिए ले ली गई है",
   "बढ़ती वर्षा के साथ सवाना घने उष्णकटिबंधीय वर्षावन में बदल रहा है",
   "सहारा पूरे केन्या और तंज़ानिया में दूर दक्षिण तक फैल गया है",
   "त्सेत्से मक्खियों से फैले एक रोग ने उनके सभी मवेशियों को समाप्त कर दिया है"],
  0,
  "Pastoralists need large, open ranges to move between wet-season and dry-season pastures. Across Maasailand, communal grazing land has been divided into private plots, ploughed for crops, built over by growing towns, and enclosed in parks and reserves such as the Serengeti and the Maasai Mara, where grazing is restricted; droughts add to the strain. "
  "So many Maasai have settled, taken up farming or tourism work, or moved to towns. The savanna is not turning into rainforest, and the Sahara lies far to the north.",
  "पशुपालकों को आर्द्र और शुष्क ऋतु के चरागाहों के बीच घूमने के लिए बड़े, खुले क्षेत्र चाहिए। मसाई क्षेत्र में सामुदायिक चराई भूमि निजी भूखंडों में बँट गई है, खेती के लिए जोती गई है, बढ़ते नगरों से भर गई है, और सेरेंगेटी तथा मसाई मारा जैसे उद्यानों और आरक्षित क्षेत्रों में घेर ली गई है जहाँ चराई सीमित है; सूखा दबाव और बढ़ाता है। "
  "इसलिए बहुत-से मसाई बस गए हैं, खेती या पर्यटन का काम अपनाया है, या नगरों में चले गए हैं। सवाना वर्षावन में नहीं बदल रहा, और सहारा बहुत उत्तर में है।",
  NCH, "hum-maasai-kenya-tanzania", craft="linkage")

# ================================================================ statements (10)
S(TH, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Over short distances roads are more economical than railways, because they cost less to build and give door-to-door service without loading and unloading at stations.",
   "Air transport is the cheapest way to carry passengers."],
  ["कम दूरी के लिए सड़कें रेलों से अधिक किफ़ायती हैं, क्योंकि उन्हें बनाना सस्ता है और वे स्टेशनों पर माल चढ़ाए-उतारे बिना घर-घर तक सेवा देती हैं।",
   "यात्रियों को ले जाने का सबसे सस्ता साधन वायु परिवहन है।"],
  T2, 0,
  "Only statement 1 is correct: a truck or bus picks up and delivers at the door, so for short trips it saves the time and cost of reaching a station and transferring the load, while railways become cheaper over long distances and for bulk goods. "
  "Statement 2 is wrong: air transport is the fastest but also the costliest mode, because aircraft, fuel and airports are expensive; it pays for passengers and for light, valuable or urgent goods.",
  "केवल कथन 1 सही है: ट्रक या बस दरवाज़े पर माल उठाते और पहुँचाते हैं, इसलिए छोटी यात्राओं में स्टेशन तक पहुँचने और माल बदलने का समय और ख़र्च बचता है, जबकि लंबी दूरी और भारी माल के लिए रेल सस्ती पड़ती है। "
  "कथन 2 गलत है: वायु परिवहन सबसे तेज़ पर सबसे महँगा साधन है, क्योंकि विमान, ईंधन और हवाई अड्डे महँगे हैं; यह यात्रियों और हल्के, मूल्यवान या तात्कालिक माल के लिए उपयोगी है।",
  NC10, "tr-roads-short-air-cost-easy", craft="linkage")

S(TH, "hard", "Consider the following statements about India's overseas connectivity projects:",
  "भारत की विदेशी संपर्क परियोजनाओं के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Chabahar port in Iran gives India a route to Afghanistan and Central Asia that bypasses Pakistan.",
   "The Kaladan project, through Sittwe port in Myanmar, gives the north-eastern States a route to the sea that avoids the narrow Siliguri corridor.",
   "The International North-South Transport Corridor is meant to link India with Russia through Iran."],
  ["ईरान का चाबहार बंदरगाह भारत को अफ़ग़ानिस्तान और मध्य एशिया तक ऐसा मार्ग देता है जो पाकिस्तान से बचकर निकलता है।",
   "म्यांमार के सित्तवे बंदरगाह के माध्यम से कालादान परियोजना उत्तर-पूर्वी राज्यों को समुद्र तक ऐसा मार्ग देती है जो सँकरे सिलीगुड़ी गलियारे से बचता है।",
   "अंतरराष्ट्रीय उत्तर-दक्षिण परिवहन गलियारा भारत को ईरान के रास्ते रूस से जोड़ने के लिए है।"],
  C3, 2,
  "All three are correct, and each is about avoiding a bottleneck. In May 2024 India Ports Global signed a ten-year contract to run the Shahid Beheshti terminal at Chabahar, India's gateway to Afghanistan and Central Asia that does not depend on transit through Pakistan. "
  "The Kaladan project links Kolkata by sea to Sittwe, then by river and road through Myanmar's Chin and Rakhine areas to Mizoram, so that the north-east is not wholly dependent on the 'chicken's neck' near Siliguri. The INSTC combines sea, rail and road routes from Mumbai through Iran and the Caspian region to Russia.",
  "तीनों कथन सही हैं, और प्रत्येक किसी अवरोध से बचने के बारे में है। मई 2024 में इंडिया पोर्ट्स ग्लोबल ने चाबहार के शहीद बहेश्ती टर्मिनल को चलाने के लिए दस वर्षीय अनुबंध किया, जो अफ़ग़ानिस्तान और मध्य एशिया तक भारत का ऐसा द्वार है जो पाकिस्तान के रास्ते पारगमन पर निर्भर नहीं। "
  "कालादान परियोजना कोलकाता को समुद्र से सित्तवे और फिर नदी और सड़क से म्यांमार के चिन और रखाइन क्षेत्रों से होकर मिज़ोरम तक जोड़ती है, ताकि उत्तर-पूर्व पूरी तरह सिलीगुड़ी के पास की 'चिकन नेक' पर निर्भर न रहे। INSTC मुंबई से ईरान और कैस्पियन क्षेत्र होते हुए रूस तक समुद्री, रेल और सड़क मार्गों को मिलाता है।",
  "Ministry of External Affairs -- Connectivity projects.", "tr-chabahar-sittwe-instc", craft="linkage")

S(TH, "medium", "Consider the following statements based on the Census of 2011:",
  "2011 की जनगणना पर आधारित निम्नलिखित कथनों पर विचार कीजिए:",
  ["Kerala had the highest sex ratio among the States.",
   "Mizoram had the lowest population density among the States.",
   "Goa was the least populous State.",
   "Uttar Pradesh was the most populous State."],
  ["राज्यों में केरल का लिंगानुपात सबसे अधिक था।",
   "राज्यों में मिज़ोरम का जनसंख्या घनत्व सबसे कम था।",
   "गोवा सबसे कम आबादी वाला राज्य था।",
   "उत्तर प्रदेश सबसे अधिक आबादी वाला राज्य था।"],
  C4, 1,
  "Statements 1 and 4 are correct: Kerala had 1,084 women per 1,000 men against a national 943, and Uttar Pradesh, with about 20 crore people, had a sixth of India's population. Statements 2 and 3 are near-misses: the lowest density was Arunachal Pradesh's, only 17 persons per sq km (Mizoram, at 52, was second lowest), and the least populous State was Sikkim, with about 6.1 lakh people; Goa, with about 14.6 lakh, was second smallest.",
  "कथन 1 और 4 सही हैं: केरल में राष्ट्रीय 943 के मुक़ाबले प्रति 1,000 पुरुषों पर 1,084 महिलाएँ थीं, और लगभग 20 करोड़ लोगों के साथ उत्तर प्रदेश में भारत की जनसंख्या का छठा भाग था। कथन 2 और 3 निकट-भ्रम हैं: सबसे कम घनत्व अरुणाचल प्रदेश का था, केवल 17 व्यक्ति प्रति वर्ग किमी (52 के साथ मिज़ोरम दूसरा सबसे कम था), और सबसे कम आबादी वाला राज्य लगभग 6.1 लाख लोगों वाला सिक्किम था; लगभग 14.6 लाख के साथ गोवा दूसरा सबसे छोटा था।",
  "Office of the Registrar General and Census Commissioner, India -- Census 2011.", "hum-census-2011-state-facts", craft="precision")

S(TH, "medium", "Consider the following statements about the Human Development Index (HDI):",
  "मानव विकास सूचकांक (HDI) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It combines measures of health, education and per capita income.",
   "It is published by the United Nations Development Programme.",
   "The first Human Development Report, in 1990, was conceived by Amartya Sen."],
  ["यह स्वास्थ्य, शिक्षा और प्रति व्यक्ति आय के मापों को मिलाता है।",
   "इसे संयुक्त राष्ट्र विकास कार्यक्रम प्रकाशित करता है।",
   "1990 की पहली मानव विकास रिपोर्ट की परिकल्पना अमर्त्य सेन ने की थी।"],
  C3, 1,
  "Statements 1 and 2 are correct. The HDI uses life expectancy at birth, mean and expected years of schooling, and gross national income per head, and the UNDP has published it in the Human Development Report since 1990. "
  "Statement 3 is the near-miss: the report was conceived and led by the Pakistani economist Mahbub ul Haq; Amartya Sen worked with him and shaped its idea of development as the widening of people's capabilities.",
  "कथन 1 और 2 सही हैं। HDI जन्म के समय जीवन-प्रत्याशा, स्कूली शिक्षा के औसत और अपेक्षित वर्ष, और प्रति व्यक्ति सकल राष्ट्रीय आय का उपयोग करता है, और UNDP इसे 1990 से मानव विकास रिपोर्ट में प्रकाशित करता है। "
  "कथन 3 निकट-भ्रम है: रिपोर्ट की परिकल्पना और नेतृत्व पाकिस्तानी अर्थशास्त्री महबूब-उल-हक़ ने किया; अमर्त्य सेन ने उनके साथ काम किया और लोगों की क्षमताओं के विस्तार के रूप में विकास के उसके विचार को आकार दिया।",
  "United Nations Development Programme -- Human Development Report.", "hum-hdi-basics", craft="precision")

S(TH, "medium", "Consider the following statements about some recent transport works:",
  "हाल के कुछ परिवहन निर्माणों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Chenab bridge, the world's highest railway arch bridge, completed the rail link that joins the Kashmir valley to the national network.",
   "The new Pamban bridge has a vertical-lift span, so that ships can still pass through the channel beneath it.",
   "The Atal Tunnel connects Srinagar with Leh."],
  ["संसार का सबसे ऊँचा रेलवे आर्च पुल, चिनाब पुल, उस रेल संपर्क को पूरा करता है जो कश्मीर घाटी को राष्ट्रीय नेटवर्क से जोड़ता है।",
   "नए पंबन पुल में एक ऊर्ध्वाधर-उत्थापन भाग है, ताकि जहाज़ अब भी उसके नीचे की नहर से गुज़र सकें।",
   "अटल सुरंग श्रीनगर को लेह से जोड़ती है।"],
  C3, 1,
  "Statements 1 and 2 are correct. The Chenab bridge, about 359 m above the river in Reasi district, opened in June 2025 on the Udhampur-Srinagar-Baramulla line, so trains now run from the plains into the Kashmir valley. The new Pamban bridge, opened in April 2025, links Rameswaram with the mainland, and its lift span rises to let vessels through the Pamban channel. "
  "Statement 3 is wrong: the Atal Tunnel, under the Rohtang pass, connects Manali with the Lahaul-Spiti valley and keeps it reachable when snow closes the pass; the Srinagar-Leh road crosses the Zoji La.",
  "कथन 1 और 2 सही हैं। रियासी ज़िले में नदी से लगभग 359 मीटर ऊपर चिनाब पुल जून 2025 में उधमपुर-श्रीनगर-बारामूला लाइन पर खुला, जिससे अब रेलें मैदानों से कश्मीर घाटी तक जाती हैं। अप्रैल 2025 में खुला नया पंबन पुल रामेश्वरम को मुख्य भूमि से जोड़ता है, और इसका उत्थापन भाग पंबन नहर से जहाज़ों को निकलने देने के लिए ऊपर उठता है। "
  "कथन 3 गलत है: रोहतांग दर्रे के नीचे की अटल सुरंग मनाली को लाहौल-स्पीति घाटी से जोड़ती है और बर्फ़ से दर्रा बंद होने पर भी उस तक पहुँच बनाए रखती है; श्रीनगर-लेह सड़क ज़ोजी ला पार करती है।",
  "Ministry of Railways; Border Roads Organisation.", "tr-chenab-pamban-atal", craft="linkage")

S(TH, "medium", "Consider the following statements about the Dedicated Freight Corridors (DFCs):",
  "समर्पित माल-ढुलाई गलियारों (DFC) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Eastern DFC runs from Ludhiana in Punjab to Sonnagar in Bihar.",
   "The Western DFC connects Kolkata with Mumbai.",
   "The DFCs are meant to take freight trains off the crowded mixed-use lines, so that both goods and passenger trains can run faster."],
  ["पूर्वी DFC पंजाब के लुधियाना से बिहार के सोननगर तक जाता है।",
   "पश्चिमी DFC कोलकाता को मुंबई से जोड़ता है।",
   "DFC का उद्देश्य मालगाड़ियों को भीड़भाड़ वाली मिश्रित लाइनों से हटाना है, ताकि माल और यात्री दोनों गाड़ियाँ तेज़ चल सकें।"],
  C3, 1,
  "Statements 1 and 3 are correct. On the old trunk routes slow freight trains and fast passenger trains share the same tracks, so each delays the other; the DFCs carry only freight, with heavier, longer and double-stacked container trains, freeing the old lines for passenger traffic. The Eastern corridor, about 1,337 km long, carries coal and other bulk freight across the Indo-Gangetic plain. "
  "Statement 2 is wrong: the Western DFC runs about 1,500 km from Dadri near Delhi to the Jawaharlal Nehru Port near Mumbai, carrying containers from the west-coast ports.",
  "कथन 1 और 3 सही हैं। पुराने मुख्य मार्गों पर धीमी मालगाड़ियाँ और तेज़ यात्री गाड़ियाँ एक ही पटरी बाँटती हैं, इसलिए एक-दूसरे को देर कराती हैं; DFC केवल माल ढोते हैं, अधिक भारी, लंबी और दोहरी परत वाली कंटेनर गाड़ियों के साथ, जिससे पुरानी लाइनें यात्री यातायात के लिए ख़ाली होती हैं। लगभग 1,337 किमी लंबा पूर्वी गलियारा सिंधु-गंगा मैदान के पार कोयला और अन्य भारी माल ले जाता है। "
  "कथन 2 गलत है: पश्चिमी DFC दिल्ली के पास दादरी से मुंबई के पास जवाहरलाल नेहरू पोर्ट तक लगभग 1,500 किमी चलता है, और पश्चिमी तट के बंदरगाहों से कंटेनर ढोता है।",
  "Dedicated Freight Corridor Corporation of India.", "tr-dedicated-freight-corridors", craft="linkage")

S(TH, "medium", "Consider the following statements about ports on the east coast:",
  "पूर्वी तट के बंदरगाहों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Visakhapatnam is a deep, landlocked and well-protected port.",
   "Paradip port in Odisha handles large exports of iron ore and coal.",
   "Kolkata port has to be dredged constantly, because the Hooghly brings down heavy loads of silt."],
  ["विशाखापत्तनम एक गहरा, भू-आबद्ध और सुरक्षित बंदरगाह है।",
   "ओडिशा का पारादीप बंदरगाह लौह अयस्क और कोयले का बड़ा निर्यात सँभालता है।",
   "कोलकाता बंदरगाह की लगातार ड्रेजिंग करनी पड़ती है, क्योंकि हुगली भारी मात्रा में गाद लाती है।"],
  C3, 2,
  "All three are correct. Visakhapatnam, the deepest landlocked port in the country, was cut into the land behind a headland, which shelters it. Paradip, on the Mahanadi delta, ships iron ore, coal and other bulk cargo from the mineral belt of Odisha and Jharkhand. "
  "Kolkata (the Syama Prasad Mookerjee Port), about 128 km up the Hooghly, has to be dredged all the time because the river drops its silt in the channel; Haldia, downstream, was built for larger ships.",
  "तीनों कथन सही हैं। देश का सबसे गहरा भू-आबद्ध बंदरगाह विशाखापत्तनम एक अंतरीप के पीछे भूमि में काटकर बनाया गया, जो उसे सुरक्षा देता है। महानदी डेल्टा पर पारादीप ओडिशा और झारखंड की खनिज पट्टी से लौह अयस्क, कोयला और अन्य भारी माल भेजता है। "
  "हुगली में लगभग 128 किमी भीतर कोलकाता (श्यामा प्रसाद मुखर्जी पोर्ट) की हर समय ड्रेजिंग करनी पड़ती है क्योंकि नदी अपनी गाद नहर में छोड़ती है; नीचे की ओर हल्दिया बड़े जहाज़ों के लिए बनाया गया।",
  NC12, "tr-east-coast-ports", craft="linkage")

S(TH, "medium", "Consider the following statements about National Waterways:",
  "राष्ट्रीय जलमार्गों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["National Waterway 1 is on the Ganga-Bhagirathi-Hooghly river system.",
   "National Waterway 2 is on the Brahmaputra from Dhubri to Sadiya.",
   "National Waterway 3 is the West Coast Canal in Kerala.",
   "The National Waterways Act, 2016 declared 106 new National Waterways, raising the total to 111."],
  ["राष्ट्रीय जलमार्ग 1 गंगा-भागीरथी-हुगली नदी तंत्र पर है।",
   "राष्ट्रीय जलमार्ग 2 धुबरी से सदिया तक ब्रह्मपुत्र पर है।",
   "राष्ट्रीय जलमार्ग 3 केरल की पश्चिमी तट नहर है।",
   "राष्ट्रीय जलमार्ग अधिनियम, 2016 ने 106 नए राष्ट्रीय जलमार्ग घोषित किए, जिससे कुल संख्या 111 हो गई।"],
  C4, 3,
  "All four are correct. NW-1 runs about 1,620 km from Haldia to Prayagraj and is being upgraded under the Jal Marg Vikas project; NW-2 covers 891 km of the Brahmaputra; and NW-3 links Kottapuram and Kollam through the Kerala backwaters. "
  "Until 2016 there were only five National Waterways; the National Waterways Act of that year added 106 more, for a total of 111, though only some of them carry regular cargo.",
  "चारों कथन सही हैं। NW-1 हल्दिया से प्रयागराज तक लगभग 1,620 किमी चलता है और जल मार्ग विकास परियोजना के तहत उन्नत किया जा रहा है; NW-2 ब्रह्मपुत्र के 891 किमी में है; और NW-3 केरल के बैकवॉटर्स से कोट्टापुरम और कोल्लम को जोड़ता है। "
  "2016 तक केवल पाँच राष्ट्रीय जलमार्ग थे; उस वर्ष के राष्ट्रीय जलमार्ग अधिनियम ने 106 और जोड़कर कुल 111 कर दिए, यद्यपि उनमें से कुछ ही पर नियमित माल ढुलाई होती है।",
  "Inland Waterways Authority of India -- National Waterways Act, 2016.", "tr-national-waterways", craft="precision")

S(TH, "medium", "Consider the following statements about India's ports:",
  "भारत के बंदरगाहों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Vizhinjam suits container transshipment because it lies close to the main east-west shipping route and has deep water near the shore.",
   "Vadhavan has been approved as a new major port in Gujarat.",
   "Kamarajar port at Ennore was India's first major port to be set up as a company."],
  ["विझिंजम कंटेनर ट्रांसशिपमेंट के लिए उपयुक्त है क्योंकि यह मुख्य पूर्व-पश्चिम नौवहन मार्ग के पास है और तट के निकट गहरा पानी है।",
   "वधावन को गुजरात में एक नए प्रमुख बंदरगाह के रूप में स्वीकृति मिली है।",
   "एन्नोर का कामराजर बंदरगाह कंपनी के रूप में स्थापित होने वाला भारत का पहला प्रमुख बंदरगाह था।"],
  C3, 1,
  "Statements 1 and 3 are correct. Vizhinjam, near Thiruvananthapuram, commissioned in 2025, lies only a few nautical miles from the international route between the Suez Canal and East Asia and has a natural depth of about 18-20 m close to the coast, so the largest container ships can call without heavy dredging -- and Indian containers need not be transshipped at Colombo or Singapore. "
  "Statement 2 is wrong: the deep-draught Vadhavan port, approved by the Union Cabinet in 2024, is in Palghar district of Maharashtra.",
  "कथन 1 और 3 सही हैं। 2025 में चालू हुआ तिरुवनंतपुरम के पास विझिंजम स्वेज़ नहर और पूर्वी एशिया के बीच के अंतरराष्ट्रीय मार्ग से कुछ ही समुद्री मील दूर है और तट के पास लगभग 18-20 मीटर की प्राकृतिक गहराई रखता है, इसलिए सबसे बड़े कंटेनर जहाज़ भारी ड्रेजिंग के बिना आ सकते हैं, और भारतीय कंटेनरों को कोलंबो या सिंगापुर में ट्रांसशिप नहीं करना पड़ता। "
  "कथन 2 गलत है: 2024 में केंद्रीय मंत्रिमंडल द्वारा स्वीकृत गहरे ड्राफ़्ट वाला वधावन बंदरगाह महाराष्ट्र के पालघर ज़िले में है।",
  "Ministry of Ports, Shipping and Waterways.", "tr-vizhinjam-vadhavan-kamarajar", craft="linkage")

S(TH, "medium", "Consider the following statements about ports on the west coast:",
  "पश्चिमी तट के बंदरगाहों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Deendayal port (Kandla) is a tidal port.",
   "Jawaharlal Nehru Port is India's largest port by total cargo handled.",
   "Mormugao port in Goa is known mainly for exporting coffee."],
  ["दीनदयाल बंदरगाह (कांडला) एक ज्वारीय बंदरगाह है।",
   "कुल माल-ढुलाई के आधार पर जवाहरलाल नेहरू पोर्ट भारत का सबसे बड़ा बंदरगाह है।",
   "गोवा का मोरमुगाओ बंदरगाह मुख्यतः कॉफ़ी के निर्यात के लिए जाना जाता है।"],
  C3, 0,
  "Only statement 1 is correct: Deendayal, at the head of the Gulf of Kachchh, depends on the tides for its depth. Statement 2 is the near-miss: Jawaharlal Nehru Port (Nhava Sheva) is India's largest container port, but ports such as Deendayal and Paradip handle more cargo in total, much of it petroleum, coal and ore. "
  "Statement 3 is wrong: Mormugao is known mainly for exporting iron ore from Goa's mines.",
  "केवल कथन 1 सही है: कच्छ की खाड़ी के शीर्ष पर दीनदयाल अपनी गहराई के लिए ज्वार पर निर्भर है। कथन 2 निकट-भ्रम है: जवाहरलाल नेहरू पोर्ट (न्हावा शेवा) भारत का सबसे बड़ा कंटेनर बंदरगाह है, पर दीनदयाल और पारादीप जैसे बंदरगाह कुल मिलाकर अधिक माल सँभालते हैं, जिसका बड़ा भाग पेट्रोलियम, कोयला और अयस्क है। "
  "कथन 3 गलत है: मोरमुगाओ मुख्यतः गोवा की खदानों से लौह अयस्क के निर्यात के लिए जाना जाता है।",
  NC12, "tr-west-coast-ports", craft="precision")

# ================================================================ TAGS for the 65 kept rows (Test 21's 2 are tagged already)
TAGS = {
 "res-solar-potential-easy": "linkage", "res-terrace-farming-easy": "linkage", "res-chotanagpur-steel-location": "linkage",
 "res-natural-gas-lng-imports": "precision", "res-crude-imports-refining": "linkage", "res-jute-growing-conditions": "linkage",
 "res-mica-insulator": "precision", "res-tea-slopes-drainage": "linkage", "res-thermal-plants-pit-head": "linkage",
 "res-solar-parks-pairs": "recall", "res-nuclear-plants-pairs": "recall", "res-shifting-cultivation-names-pairs": "recall",
 "res-aluminium-smelter-power": "linkage", "res-jute-mills-hooghly": "linkage", "res-sugar-mills-shift-south": "linkage",
 "res-groundnut-gujarat": "recall", "res-khetri-copper": "recall", "res-neyveli-lignite": "recall",
 "res-tea-assam": "recall", "res-mustard-wheat-easy": "recall", "res-petroleum-uranium-easy": "recall",
 "res-rice-cotton-easy": "recall", "res-solar-coal-easy": "recall", "res-cropping-intensity": "precision",
 "res-mineral-distribution-rocks": "linkage", "res-plantation-spices-coffee-rubber-conditions": "linkage", "res-bauxite-manganese-limestone": "recall",
 "res-cotton-groundnut-sugarcane": "precision", "res-cropping-seasons-aus-aman-boro": "recall", "res-electricity-capacity-mix": "precision",
 "res-farming-types": "precision", "res-oil-fields-digboi-bombay-high-barmer": "recall", "res-rice-wheat-climate": "linkage",
 "tr-air-transport-north-east-easy": "linkage", "hum-gaddi-transhumance": "precision", "hum-ganga-plains-density": "linkage",
 "hum-bihar-literacy-density": "inference", "hum-thar-clustered-villages": "linkage", "tr-pipelines-undersea": "precision",
 "tr-railway-density-hills": "linkage", "hum-world-peoples-pairs": "recall", "hum-tribes-regions-pairs": "recall",
 "tr-ports-states-pairs": "recall", "tr-waterways-cheapest-easy": "recall", "hum-demographic-dividend": "precision",
 "tr-east-coast-fewer-harbours": "linkage", "tr-konkan-railway-challenge": "linkage", "hum-khasi-matrilineal": "recall",
 "tr-busiest-airport-delhi": "recall", "hum-census-decennial-easy": "recall", "hum-mother-tongues-easy": "recall",
 "tr-indian-railways-easy": "recall", "hum-demographic-transition": "precision", "hum-tribes-andaman-nicobar-bhotia": "recall",
 "tr-ports-kochi-kandla-new-mangalore": "linkage", "tr-transcontinental-railways": "recall", "hum-census-2027": "precision",
 "hum-census-town-urbanisation": "precision", "hum-economic-activity-sectors": "precision", "hum-migration-streams": "precision",
 "hum-rural-settlement-types": "linkage", "hum-world-population-facts": "recall", "tr-pipelines-hvj-naharkatiya-motihari": "recall",
 "tr-railways-1853-gauges": "recall", "tr-road-corridors-bro": "recall"}

if __name__ == "__main__":
    write_updates("upg_l2_t14_geo_b.sql", statuses=("draft", "published"), tags=TAGS)
