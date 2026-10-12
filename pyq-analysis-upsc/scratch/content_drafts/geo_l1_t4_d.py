# -*- coding: utf-8 -*-
"""Level 1 · Test 4 (Geography, NCERT Foundation) -- part D: Indian Rivers, Lakes & Wetlands (14) and
Geomorphology & Earth's Interior (11) (upsc_l1_cell_targets.mjs 4).
Rivers: easy MCQ 1, easy statement 2, easy Statement-I/II 1, medium MCQ 2, medium statement 4, medium Statement-I/II 1,
hard MCQ 1, hard statement 1, hard Statement-I/II 1. Geomorphology: easy MCQ 1, easy statement 2, easy pairs 1,
easy Statement-I/II 1, medium MCQ 1, medium statement 3, medium Statement-I/II 1, hard statement 1.
The angle is NCERT's drainage chapters (Contemporary India I, India: Physical Environment), water resources
(Contemporary India II, India: People and Economy) and the landform chapters of Our Environment (VII) and
Fundamentals of Physical Geography. Level-2 facts are not repeated: river sources, tributaries, dams, lakes by
State, waterfalls, the Indus treaty, Farakka, Ken-Betwa, the Himalayan-Peninsular contrast, Kosi, Damodar, Chilika;
the interior's layers and discontinuities, seismic waves, plate boundaries, Wegener, volcano types, karst, the
landform-agent pairs, exfoliation and marble. MCQ keys are pinned (pos)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Geography"
d.REQUIRE_CRAFT = True
RV = "Indian Rivers, Lakes & Wetlands"
GM = "Geomorphology & Earth's Interior"
CI1 = "NCERT Class IX, Geography -- Contemporary India I"
CI2 = "NCERT Class X, Geography -- Contemporary India II"
IPE = "NCERT Class XI, Geography -- India: Physical Environment"
IPR = "NCERT Class XII, Geography -- India: People and Economy"
GE7 = "NCERT Class VII, Geography -- Our Environment"
FPG = "NCERT Class XI, Geography -- Fundamentals of Physical Geography"

# ================================================================ RIVERS (14)
# ---------------------------------------------------------------- easy MCQ (1)
M(RV, "easy", "The 'Marble Rocks', where a river flows through a deep gorge, and the Dhuandhar falls, where it plunges over steep rocks, are found near Jabalpur along the",
  "'संगमरमर की चट्टानें' (Marble Rocks), जहाँ एक नदी गहरी कंदरा से बहती है, और धुआँधार जलप्रपात, जहाँ वह खड़ी चट्टानों से नीचे गिरती है, जबलपुर के पास किस नदी पर मिलते हैं?",
  ["Narmada", "Tapi", "Son", "Mahanadi"],
  ["नर्मदा", "तापी", "सोन", "महानदी"],
  0,
  "The Narmada rises near Amarkantak in Madhya Pradesh and, flowing west, creates many picturesque places: the Marble Rocks at Bhedaghat, where it cuts a deep gorge through marble, and the Dhuandhar falls, named for the 'smoke' of spray it throws up. "
  "The Son also rises on the Amarkantak plateau but flows north-east to the Ganga, while the Tapi rises in the Satpura ranges and the Mahanadi in the highlands of Chhattisgarh.",
  "नर्मदा मध्य प्रदेश में अमरकंटक के निकट से निकलकर पश्चिम की ओर बहते हुए कई मनोरम स्थल बनाती है: भेड़ाघाट की संगमरमर की चट्टानें, जहाँ वह संगमरमर को काटकर गहरी कंदरा बनाती है, और धुआँधार जलप्रपात, जिसका नाम उससे उठने वाली फुहार के 'धुएँ' से पड़ा। "
  "सोन भी अमरकंटक पठार से निकलती है पर उत्तर-पूर्व की ओर गंगा में जाती है, जबकि तापी सतपुड़ा श्रेणी से और महानदी छत्तीसगढ़ की उच्चभूमि से निकलती है।",
  f"{CI1} (Drainage).",
  "l1-geo-narmada-marble-rocks-dhuandhar", pos=3, craft="recall")

# ---------------------------------------------------------------- easy statement (2)
S(RV, "easy", "Consider the following statements about drainage patterns:",
  "अपवाह प्रतिरूपों (drainage patterns) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["A pattern resembling the branches of a tree is called dendritic; the rivers of the northern plains are examples.",
   "When rivers rise on a hill and flow out in all directions, the pattern is radial, as with the rivers of the Amarkantak range.",
   "In a trellis pattern, primary tributaries run parallel to each other and secondary tributaries join them at right angles."],
  ["पेड़ की शाखाओं जैसा प्रतिरूप वृक्षाकार (dendritic) कहलाता है; उत्तरी मैदानों की नदियाँ इसके उदाहरण हैं।",
   "जब नदियाँ किसी पहाड़ी से निकलकर सभी दिशाओं में बहती हैं, तो प्रतिरूप अरीय (radial) होता है, जैसे अमरकंटक श्रेणी की नदियाँ।",
   "जालीनुमा (trellis) प्रतिरूप में प्राथमिक सहायक नदियाँ एक-दूसरे के समानांतर बहती हैं और द्वितीयक सहायक नदियाँ उनसे समकोण पर मिलती हैं।"],
  C3, 2,
  "All three statements are correct. The pattern a river system takes depends on the slope, the structure of the rocks and the climate: a dendritic pattern develops where the channel simply follows the slope of the terrain, and a trellis pattern where hard and soft rocks lie parallel to each other. "
  "Two more patterns complete the set -- rectangular, on strongly jointed rocky terrain, and centripetal, where rivers drain from all sides into a lake or a depression.",
  "तीनों कथन सही हैं। किसी नदी तंत्र का प्रतिरूप ढाल, शैलों की संरचना और जलवायु पर निर्भर करता है: वृक्षाकार प्रतिरूप वहाँ बनता है जहाँ धारा केवल भूभाग के ढाल का अनुसरण करती है, और जालीनुमा वहाँ जहाँ कठोर और कोमल शैलें एक-दूसरे के समानांतर हों। "
  "दो और प्रतिरूप यह सूची पूरी करते हैं -- आयताकार, जो अत्यधिक जोड़ों वाले चट्टानी भूभाग पर बनता है, और अभिकेंद्री (centripetal), जहाँ नदियाँ सभी ओर से किसी झील या गर्त में गिरती हैं।",
  f"{IPE} (Drainage System); {CI1} (Drainage).",
  "l1-geo-drainage-patterns", craft="precision")

S(RV, "easy", "Consider the following statements about lakes of India:",
  "भारत की झीलों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Wular lake in Jammu and Kashmir is the result of tectonic activity.",
   "Guru Gobind Sagar is a natural lake of glacial origin."],
  ["जम्मू-कश्मीर की वुलर झील विवर्तनिक (tectonic) गतिविधि का परिणाम है।",
   "गुरु गोबिंद सागर हिमनद से बनी एक प्राकृतिक झील है।"],
  T2, 0,
  "Only statement 1 is correct. Most freshwater lakes of the Himalayan region are of glacial origin, formed where glaciers dug out basins that later filled with melted snow, but Wular, in contrast, owes its origin to movements of the Earth's crust. "
  "Statement 2 is wrong: Guru Gobind Sagar is an artificial lake, the reservoir created by the Bhakra Nangal project; lakes also help regulate river flow, store water for hydel power and moderate the local climate.",
  "केवल कथन 1 सही है। हिमालयी क्षेत्र की अधिकांश मीठे पानी की झीलें हिमनदीय उत्पत्ति की हैं, जो वहाँ बनीं जहाँ हिमनदों ने बेसिन खोदे जो बाद में पिघली बर्फ़ से भर गए, पर इसके विपरीत वुलर की उत्पत्ति पृथ्वी की भूपर्पटी की हलचलों से हुई। "
  "कथन 2 गलत है: गुरु गोबिंद सागर एक कृत्रिम झील है, भाखड़ा नांगल परियोजना से बना जलाशय; झीलें नदियों के प्रवाह को नियंत्रित करने, जलविद्युत के लिए जल संग्रह करने और स्थानीय जलवायु को सम बनाने में भी सहायक हैं।",
  f"{CI1} (Drainage).",
  "l1-geo-wular-tectonic-gobind-sagar", craft="precision")

# ---------------------------------------------------------------- easy Statement-I/II (1)
A(RV, "easy",
  "The Ganga develops large meanders as it flows across the northern plains.",
  "उत्तरी मैदानों में बहते हुए गंगा बड़े विसर्प (meanders) बनाती है।",
  "Across the plain, the land falls by only about one metre for every six kilometres.",
  "पूरे मैदान में भूमि हर छह किलोमीटर पर केवल लगभग एक मीटर नीचे जाती है।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I. From Ambala to the Sundarbans the Ganga plain stretches about 1,800 km but falls hardly 300 m; on so gentle a slope the river loses the energy to cut down, and instead swings from side to side in wide loops. "
  "Meanders, cut-off oxbow lakes, flood plains and braided channels are the typical features of the middle and lower courses of the Himalayan rivers.",
  "दोनों कथन सही हैं, और कथन-II कथन-I की व्याख्या करता है। अंबाला से सुंदरवन तक गंगा का मैदान लगभग 1,800 किमी फैला है पर मुश्किल से 300 मीटर नीचे जाता है; इतने मंद ढाल पर नदी में नीचे की ओर काटने की ऊर्जा नहीं रहती, और वह चौड़े फंदों में इधर-उधर झूलती है। "
  "विसर्प, कटकर बनी गोखुर झीलें, बाढ़ के मैदान और गुंफित धाराएँ हिमालयी नदियों के मध्य और निचले मार्गों की विशिष्ट आकृतियाँ हैं।",
  f"{CI1} (Drainage).",
  "l1-geo-ganga-meanders-gentle-slope", craft="inference")

# ---------------------------------------------------------------- medium MCQ (2)
M(RV, "medium", "Which one of the following cities lies on the water divide between the Indus and the Ganga river systems?",
  "निम्नलिखित में से कौन-सा नगर सिंधु और गंगा नदी तंत्रों के बीच जल-विभाजक पर स्थित है?",
  ["Ambala", "Ludhiana", "Meerut", "Jalandhar"],
  ["अंबाला", "लुधियाना", "मेरठ", "जालंधर"],
  0,
  "A water divide is the upland that separates two drainage basins, and Ambala stands on the low divide between the Indus system to the west and the Ganga system to the east. "
  "Ludhiana and Jalandhar lie in the Punjab plains drained by the Satluj and the Beas, which belong to the Indus system; Meerut lies in the Ganga-Yamuna doab.",
  "जल-विभाजक वह उच्चभूमि है जो दो अपवाह बेसिनों को अलग करती है, और अंबाला पश्चिम के सिंधु तंत्र और पूर्व के गंगा तंत्र के बीच के निचले जल-विभाजक पर स्थित है। "
  "लुधियाना और जालंधर सतलुज और ब्यास द्वारा अपवाहित पंजाब के मैदानों में हैं, जो सिंधु तंत्र की नदियाँ हैं; मेरठ गंगा-यमुना दोआब में है।",
  f"{CI1} (Drainage).",
  "l1-geo-ambala-water-divide", pos=1, craft="application")

M(RV, "medium", "Before it enters the Bay of Bengal, the combined stream of the Ganga and the Brahmaputra is known as the",
  "बंगाल की खाड़ी में गिरने से पहले गंगा और ब्रह्मपुत्र की संयुक्त धारा किस नाम से जानी जाती है?",
  ["Meghna", "Padma", "Jamuna", "Hooghly"],
  ["मेघना", "पद्मा", "जमुना", "हुगली"],
  0,
  "At Farakka the Ganga splits: the Bhagirathi-Hooghly flows south through West Bengal, while the main stream, the Padma, flows into Bangladesh and is joined by the Brahmaputra, there called the Jamuna. "
  "Further downstream the united waters are known as the Meghna, which flows into the Bay of Bengal; the delta these rivers build is the Sundarbans, named after the Sundari tree of its tidal forests.",
  "फरक्का पर गंगा विभाजित होती है: भागीरथी-हुगली पश्चिम बंगाल से दक्षिण की ओर बहती है, जबकि मुख्य धारा, पद्मा, बांग्लादेश में जाती है और उसमें ब्रह्मपुत्र मिलती है, जिसे वहाँ जमुना कहते हैं। "
  "आगे चलकर संयुक्त जल मेघना कहलाता है, जो बंगाल की खाड़ी में गिरता है; ये नदियाँ जो डेल्टा बनाती हैं वह सुंदरवन है, जिसका नाम उसके ज्वारीय वनों के सुंदरी वृक्ष पर पड़ा है।",
  f"{CI1} (Drainage).",
  "l1-geo-ganga-brahmaputra-meghna", pos=3, craft="precision")

# ---------------------------------------------------------------- medium statement (4)
S(RV, "medium", "Consider the following statements about traditional methods of rainwater harvesting in India:",
  "भारत में वर्षा-जल संग्रहण की परंपरागत विधियों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["In the hill regions of the western Himalaya, people built diversion channels called 'guls' or 'kuls' for agriculture.",
   "'Khadins' in Jaisalmer are underground tanks for storing drinking water.",
   "In Meghalaya, a system about 200 years old taps stream and spring water through bamboo pipes for drip irrigation.",
   "Tamil Nadu has made rooftop rainwater harvesting structures compulsory for all houses across the State."],
  ["पश्चिमी हिमालय के पहाड़ी क्षेत्रों में लोगों ने खेती के लिए 'गुल' या 'कुल' कहलाने वाली मोड़ नालियाँ (diversion channels) बनाईं।",
   "जैसलमेर में 'खडीन' पीने का पानी जमा करने के लिए भूमिगत टाँके हैं।",
   "मेघालय में लगभग 200 वर्ष पुरानी एक प्रणाली बाँस की नलियों से नालों और झरनों का पानी लेकर टपक सिंचाई करती है।",
   "तमिलनाडु ने राज्य भर के सभी घरों के लिए छत पर वर्षा-जल संग्रहण की संरचना अनिवार्य कर दी है।"],
  C4, 2,
  "Statements 1, 3 and 4 are correct. Statement 2 is wrong: khadins in Jaisalmer, like johads elsewhere in Rajasthan, are fields turned into rain-fed storage structures, whose stored moisture lets crops grow; the underground tanks for drinking water are 'tankas', found in almost every traditional house of Bikaner, Phalodi and Barmer, filled by pipes from the rooftop. "
  "In Meghalaya, some 18-20 litres of water entering the bamboo pipe system get reduced to 20-80 drops a minute at the site of the plant.",
  "कथन 1, 3 और 4 सही हैं। कथन 2 गलत है: जैसलमेर के खडीन, राजस्थान में अन्यत्र जोहड़ों की तरह, वर्षा-जल संग्रह की संरचनाओं में बदले गए खेत हैं, जिनकी संचित नमी से फ़सलें उगती हैं; पीने के पानी के भूमिगत टाँके 'टाँका' कहलाते हैं, जो बीकानेर, फलोदी और बाड़मेर के लगभग हर परंपरागत घर में मिलते थे और छत से नलियों द्वारा भरे जाते थे। "
  "मेघालय में बाँस की नलियों के तंत्र में प्रवेश करने वाला लगभग 18-20 लीटर पानी पौधे के स्थान पर घटकर 20-80 बूँद प्रति मिनट रह जाता है।",
  f"{CI2} (Water Resources).",
  "l1-geo-traditional-water-harvesting", craft="precision")

S(RV, "medium", "Consider the following statements about multi-purpose river projects:",
  "बहुउद्देशीय नदी परियोजनाओं के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Jawaharlal Nehru proudly called the dams 'the temples of modern India'.",
   "Damming a river can cause poor sediment flow downstream and excessive sedimentation at the bottom of the reservoir.",
   "Dams fragment rivers, making it difficult for aquatic fauna to migrate, especially for spawning."],
  ["जवाहरलाल नेहरू ने गर्व से बाँधों को 'आधुनिक भारत के मंदिर' कहा था।",
   "नदी पर बाँध बनाने से नीचे की ओर तलछट का प्रवाह कम हो सकता है और जलाशय के तल पर अत्यधिक तलछट जमा हो सकती है।",
   "बाँध नदियों को खंडित करते हैं, जिससे जलीय जीवों के लिए, विशेषकर अंडे देने के लिए, प्रवास करना कठिन हो जाता है।"],
  C3, 2,
  "All three statements are correct. Multi-purpose projects were expected to integrate agriculture with industry and the urban economy, providing irrigation, power, flood control and water supply together. "
  "They have also been criticised: the reservoir's bed starves the river of the silt that renews the flood plains downstream, the submergence of land displaces local communities, and the regulated flow and fragmentation harm the river's ecosystem.",
  "तीनों कथन सही हैं। बहुउद्देशीय परियोजनाओं से कृषि को उद्योग और नगरीय अर्थव्यवस्था से जोड़ने की अपेक्षा थी, जो एक साथ सिंचाई, बिजली, बाढ़ नियंत्रण और जल आपूर्ति दें। "
  "उनकी आलोचना भी हुई है: जलाशय का तल नदी को उस गाद से वंचित कर देता है जो नीचे के बाढ़ के मैदानों को नवीकृत करती है, भूमि के डूबने से स्थानीय समुदाय विस्थापित होते हैं, और नियंत्रित प्रवाह तथा खंडन नदी के पारितंत्र को हानि पहुँचाते हैं।",
  f"{CI2} (Water Resources).",
  "l1-geo-multipurpose-projects-critique", craft="linkage")

S(RV, "medium", "Consider the following statements about India's water resources:",
  "भारत के जल संसाधनों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["India has about 4 per cent of the world's water resources, far less than its share of the world's population.",
   "The Ganga, Brahmaputra and Barak basins cover about one-third of the country's area but hold about 60 per cent of its surface water resources.",
   "Rivers of the Peninsula such as the Godavari, the Krishna and the Kaveri have had a much smaller share of their flow harnessed than the Ganga and the Brahmaputra."],
  ["भारत के पास विश्व के जल संसाधनों का लगभग 4 प्रतिशत है, जो विश्व जनसंख्या में उसके हिस्से से बहुत कम है।",
   "गंगा, ब्रह्मपुत्र और बराक बेसिन देश के लगभग एक-तिहाई क्षेत्र पर फैले हैं, पर उनमें सतही जल संसाधनों का लगभग 60 प्रतिशत है।",
   "गोदावरी, कृष्णा और कावेरी जैसी प्रायद्वीपीय नदियों के प्रवाह का गंगा और ब्रह्मपुत्र की तुलना में बहुत कम हिस्सा उपयोग में लाया गया है।"],
  C3, 1,
  "Statements 1 and 2 are correct. Statement 3 reverses the position: much of the annual flow of the south Indian rivers, including the Godavari, the Krishna and the Kaveri, has already been harnessed, while this is yet to be done in the Brahmaputra and Ganga basins, where most of the surface water lies. "
  "Groundwater use, too, is uneven: it is very high in Punjab, Haryana, Rajasthan and Tamil Nadu, and comparatively low in States such as Chhattisgarh, Odisha and Kerala.",
  "कथन 1 और 2 सही हैं। कथन 3 स्थिति को उलट देता है: गोदावरी, कृष्णा और कावेरी सहित दक्षिण भारत की नदियों के वार्षिक प्रवाह का बड़ा भाग पहले ही उपयोग में लाया जा चुका है, जबकि ब्रह्मपुत्र और गंगा बेसिनों में, जहाँ अधिकांश सतही जल है, यह अभी होना बाकी है। "
  "भूजल का उपयोग भी असमान है: पंजाब, हरियाणा, राजस्थान और तमिलनाडु में यह बहुत अधिक है, और छत्तीसगढ़, ओडिशा तथा केरल जैसे राज्यों में अपेक्षाकृत कम।",
  f"{IPR} (Water Resources).",
  "l1-geo-india-water-resources-share", craft="linkage")

S(RV, "medium", "Consider the following statements about watershed management in India:",
  "भारत में जलसंभर (watershed) प्रबंधन के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["'Neeru-Meeru' (Water and You) is a water-harvesting programme of Andhra Pradesh.",
   "The 'Arvary Pani Sansad' of Alwar in Rajasthan has built water-harvesting structures through people's participation.",
   "'Haryali' is a watershed development project sponsored by the Central Government and carried out through Gram Panchayats.",
   "Ralegan Siddhi, a village in the Ahmednagar district of Maharashtra, has become an example of watershed development."],
  ["'नीरू-मीरू' (जल और आप) आंध्र प्रदेश का एक जल-संग्रहण कार्यक्रम है।",
   "राजस्थान के अलवर की 'अरवरी पानी संसद' ने जनभागीदारी से जल-संग्रहण संरचनाएँ बनाई हैं।",
   "'हरियाली' केंद्र सरकार द्वारा प्रायोजित जलसंभर विकास परियोजना है, जिसे ग्राम पंचायतों के माध्यम से चलाया जाता है।",
   "महाराष्ट्र के अहमदनगर ज़िले का गाँव रालेगण सिद्धि जलसंभर विकास का उदाहरण बन गया है।"],
  C4, 3,
  "All four statements are correct. Watershed management means the efficient management and conservation of surface and groundwater, together with all the resources of a watershed -- land, vegetation, animals and people. "
  "Haryali aims to help rural people conserve water for drinking, irrigation, fisheries and afforestation, and Ralegan Siddhi showed how a village could revive its land and water through community effort, voluntary labour and a ban on practices that waste water.",
  "चारों कथन सही हैं। जलसंभर प्रबंधन का अर्थ है सतही और भूजल का, जलसंभर के सभी संसाधनों -- भूमि, वनस्पति, पशु और लोग -- के साथ कुशल प्रबंधन और संरक्षण। "
  "हरियाली का उद्देश्य ग्रामीण लोगों को पीने, सिंचाई, मत्स्य पालन और वनरोपण के लिए जल संरक्षित करने में सहायता देना है, और रालेगण सिद्धि ने दिखाया कि सामुदायिक प्रयास, स्वैच्छिक श्रम और पानी बर्बाद करने वाली प्रथाओं पर रोक से कोई गाँव अपनी भूमि और जल को कैसे पुनर्जीवित कर सकता है।",
  f"{IPR} (Water Resources).",
  "l1-geo-watershed-neeru-arvary-haryali", craft="recall")

# ---------------------------------------------------------------- medium Statement-I/II (1)
A(RV, "medium",
  "In Tibet, the Brahmaputra carries a smaller volume of water and less silt than it does in India.",
  "तिब्बत में ब्रह्मपुत्र भारत की तुलना में कम जल और कम गाद (silt) ले जाती है।",
  "In Tibet it flows through a cold, dry region, while in India it crosses a region of very high rainfall.",
  "तिब्बत में वह एक ठंडे, शुष्क क्षेत्र से बहती है, जबकि भारत में वह बहुत अधिक वर्षा वाले क्षेत्र से गुज़रती है।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I. The Brahmaputra rises in Tibet east of Lake Mansarovar and runs a long course through the dry rain shadow of the Himalaya; once it turns south into India, monsoon rain and many tributaries swell it. "
  "In Assam it becomes a braided river, dividing into channels around islands of silt, and its bed keeps changing as it drops the heavy load it carries.",
  "दोनों कथन सही हैं, और कथन-II कथन-I की व्याख्या करता है। ब्रह्मपुत्र तिब्बत में मानसरोवर झील के पूर्व से निकलकर हिमालय की शुष्क वृष्टि-छाया से लंबी दूरी तय करती है; दक्षिण की ओर मुड़कर भारत में आते ही मानसूनी वर्षा और अनेक सहायक नदियाँ उसे विशाल बना देती हैं। "
  "असम में वह गुंफित नदी बन जाती है, जो गाद के द्वीपों के चारों ओर कई धाराओं में बँटती है, और भारी बोझ जमा करते रहने से उसका तल बदलता रहता है।",
  f"{CI1} (Drainage).",
  "l1-geo-brahmaputra-tibet-less-silt", craft="inference")

# ---------------------------------------------------------------- hard MCQ (1)
M(RV, "hard", "Geologists believe that a mighty river, called the Indo-Brahma or the Shiwalik, once flowed along the whole length of the Himalaya, from Assam to Punjab. Its break-up into the Indus, Ganga and Brahmaputra systems is attributed mainly to the Pleistocene uplift of the",
  "भूवैज्ञानिक मानते हैं कि इंडो-ब्रह्म या शिवालिक कहलाने वाली एक विशाल नदी कभी असम से पंजाब तक हिमालय की पूरी लंबाई के साथ बहती थी। सिंधु, गंगा और ब्रह्मपुत्र तंत्रों में उसके बँट जाने का मुख्य कारण प्लीस्टोसीन काल में किसके उत्थान को माना जाता है?",
  ["Potwar plateau", "Aravalli range", "Shillong plateau", "Malwa plateau"],
  ["पोटवार पठार", "अरावली श्रेणी", "शिलांग पठार", "मालवा पठार"],
  0,
  "The dismemberment of the Indo-Brahma river is linked to the Pleistocene upheaval in the western Himalaya, including the uplift of the Potwar plateau (the Delhi Ridge), which became the water divide between the Indus and the Ganga systems. "
  "Likewise, the down-thrusting of the Malda gap area, between the Rajmahal hills and the Meghalaya plateau, in the mid-Pleistocene diverted the Ganga and the Brahmaputra to flow towards the Bay of Bengal.",
  "इंडो-ब्रह्म नदी के विखंडन को पश्चिमी हिमालय में प्लीस्टोसीन उथल-पुथल से जोड़ा जाता है, जिसमें पोटवार पठार (दिल्ली रिज) का उत्थान भी था, जो सिंधु और गंगा तंत्रों के बीच जल-विभाजक बन गया। "
  "इसी प्रकार, मध्य प्लीस्टोसीन में राजमहल पहाड़ियों और मेघालय पठार के बीच मालदा अंतराल क्षेत्र के नीचे धँसने से गंगा और ब्रह्मपुत्र बंगाल की खाड़ी की ओर बहने लगीं।",
  f"{IPE} (Drainage System).",
  "l1-geo-indo-brahma-potwar-uplift", pos=2, craft="linkage")

# ---------------------------------------------------------------- hard statement (1)
S(RV, "hard", "Consider the following statements about the regimes (seasonal flow patterns) of Indian rivers:",
  "भारतीय नदियों के प्रवाह-प्रतिरूप (regime) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Ganga has its minimum flow during January-June and its maximum in August or September.",
   "The Narmada has a very low discharge from January to July, rises suddenly in August, and falls as sharply in October.",
   "The Godavari reaches its maximum discharge in May, when snow melts in its upper catchment."],
  ["गंगा का न्यूनतम प्रवाह जनवरी-जून के दौरान और अधिकतम अगस्त या सितंबर में होता है।",
   "नर्मदा का प्रवाह जनवरी से जुलाई तक बहुत कम रहता है, अगस्त में अचानक बढ़ता है और अक्टूबर में उतनी ही तेज़ी से घटता है।",
   "गोदावरी का अधिकतम प्रवाह मई में होता है, जब उसके ऊपरी जलग्रहण क्षेत्र में बर्फ़ पिघलती है।"],
  C3, 1,
  "Statements 1 and 2 are correct: the Himalayan rivers are perennial, fed by snowmelt and rain, while the Peninsular rivers are rain-fed, so the Narmada's flow swings from a few cusecs to a flood with the monsoon. "
  "Statement 3 is wrong: the Godavari has no snow-fed catchment; it has its minimum discharge in May and its maximum in July-August, with a sharp fall after August, though its October-November flow is still higher than in any month from January to May.",
  "कथन 1 और 2 सही हैं: हिमालयी नदियाँ बारहमासी हैं, जिन्हें हिम के पिघलने और वर्षा दोनों से जल मिलता है, जबकि प्रायद्वीपीय नदियाँ वर्षा पर निर्भर हैं, इसलिए मानसून के साथ नर्मदा का प्रवाह कुछ क्यूसेक से बाढ़ तक झूलता है। "
  "कथन 3 गलत है: गोदावरी का कोई हिम-पोषित जलग्रहण क्षेत्र नहीं है; उसका न्यूनतम प्रवाह मई में और अधिकतम जुलाई-अगस्त में होता है, अगस्त के बाद तेज़ गिरावट आती है, यद्यपि अक्टूबर-नवंबर का प्रवाह जनवरी से मई के किसी भी महीने से अधिक रहता है।",
  f"{IPE} (Drainage System).",
  "l1-geo-river-regimes-ganga-narmada-godavari", craft="precision")

# ---------------------------------------------------------------- hard Statement-I/II (1)
A(RV, "hard",
  "The Kaveri shows sharper seasonal swings in flow than most other Peninsular rivers.",
  "कावेरी के प्रवाह में अधिकांश अन्य प्रायद्वीपीय नदियों की तुलना में अधिक तीव्र मौसमी उतार-चढ़ाव होते हैं।",
  "Its upper catchment receives rain from the south-west monsoon in summer, and its lower catchment from the north-east monsoon in winter.",
  "इसके ऊपरी जलग्रहण क्षेत्र को गर्मियों में दक्षिण-पश्चिम मानसून से, और निचले जलग्रहण क्षेत्र को सर्दियों में उत्तर-पूर्वी मानसून से वर्षा मिलती है।",
  3,
  "Statement-I is incorrect but Statement-II is correct. Because its two halves are fed in different seasons, the Kaveri carries water throughout the year with comparatively less fluctuation than the other Peninsular rivers, which is why it is among the most fully used rivers of the south. "
  "It rises in the Brahmagiri range of the Western Ghats in Karnataka and reaches the Bay of Bengal in Tamil Nadu.",
  "कथन-I गलत है, पर कथन-II सही है। चूँकि इसके दोनों भागों को अलग-अलग ऋतुओं में जल मिलता है, कावेरी में वर्ष भर पानी रहता है और अन्य प्रायद्वीपीय नदियों की तुलना में उतार-चढ़ाव अपेक्षाकृत कम होता है, इसीलिए यह दक्षिण की सबसे अधिक उपयोग की जाने वाली नदियों में है। "
  "यह कर्नाटक में पश्चिमी घाट की ब्रह्मगिरि श्रेणी से निकलकर तमिलनाडु में बंगाल की खाड़ी तक पहुँचती है।",
  f"{IPE} (Drainage System).",
  "l1-geo-kaveri-even-flow-two-monsoons", craft="inference")

# ================================================================ GEOMORPHOLOGY (11)
# ---------------------------------------------------------------- easy MCQ (1)
M(GM, "easy", "Which one of the following landforms is produced by exogenic forces?",
  "निम्नलिखित में से कौन-सी भू-आकृति बहिर्जात (exogenic) बलों से बनती है?",
  ["a sand dune", "a fold mountain", "a volcano", "a rift valley"],
  ["रेत का टीला", "वलित पर्वत", "ज्वालामुखी", "भ्रंश घाटी"],
  0,
  "Exogenic forces work on the Earth's surface -- running water, wind, ice and waves wear the land down and build landforms such as sand dunes from what they carry. "
  "Endogenic forces act from the interior: they fold and fault the crust, raising fold mountains and opening rift valleys, and they cause sudden movements such as volcanic eruptions and earthquakes.",
  "बहिर्जात बल पृथ्वी की सतह पर काम करते हैं -- बहता जल, पवन, हिम और लहरें भूमि को घिसते हैं और अपने साथ लाए पदार्थ से रेत के टीलों जैसी भू-आकृतियाँ बनाते हैं। "
  "अंतर्जात बल भीतर से काम करते हैं: वे भूपर्पटी में वलन और भ्रंशन करके वलित पर्वत उठाते और भ्रंश घाटियाँ बनाते हैं, और ज्वालामुखी विस्फोट तथा भूकंप जैसी आकस्मिक हलचलें लाते हैं।",
  f"{GE7} (Our Changing Earth).",
  "l1-geo-exogenic-endogenic-forces", pos=1, craft="application")

# ---------------------------------------------------------------- easy statement (2)
S(GM, "easy", "Consider the following statements about rocks:",
  "शैलों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Sedimentary rocks such as sandstone form when loose sediments are compressed and hardened into layers.",
   "Under great heat and pressure, clay changes into slate.",
   "Once formed, a rock cannot change from one type into another."],
  ["बलुआ पत्थर जैसी अवसादी शैलें तब बनती हैं जब ढीले अवसाद दबकर परतों में कठोर हो जाते हैं।",
   "अत्यधिक ताप और दबाव में मृत्तिका (clay) स्लेट में बदल जाती है।",
   "एक बार बन जाने के बाद कोई शैल एक प्रकार से दूसरे प्रकार में नहीं बदल सकती।"],
  C3, 1,
  "Statements 1 and 2 are correct: rocks broken down into small fragments are carried and deposited, and the compressed layers form sedimentary rock; igneous and sedimentary rocks changed by heat and pressure become metamorphic rocks, as clay becomes slate. "
  "Statement 3 is wrong: rocks keep changing from one type to another in a cyclic process called the rock cycle -- even metamorphic rocks can melt into magma and cool again into igneous rock.",
  "कथन 1 और 2 सही हैं: छोटे टुकड़ों में टूटी शैलें बहकर जमा होती हैं, और दबी हुई परतें अवसादी शैल बनाती हैं; ताप और दबाव से बदली आग्नेय और अवसादी शैलें कायांतरित शैलें बन जाती हैं, जैसे मृत्तिका स्लेट बनती है। "
  "कथन 3 गलत है: शैलें एक चक्रीय प्रक्रिया, शैल चक्र (rock cycle), में एक प्रकार से दूसरे प्रकार में बदलती रहती हैं -- कायांतरित शैलें भी पिघलकर मैग्मा बन सकती हैं और ठंडी होकर फिर आग्नेय शैल बन सकती हैं।",
  f"{GE7} (Inside Our Earth).",
  "l1-geo-rock-cycle-slate-sandstone", craft="precision")

S(GM, "easy", "Consider the following statements about the Earth's crust:",
  "पृथ्वी की भूपर्पटी के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The continental crust is much thicker than the oceanic crust -- about 35 km against about 5 km.",
   "The oceanic crust is made mainly of silica and alumina."],
  ["महाद्वीपीय भूपर्पटी महासागरीय भूपर्पटी से बहुत मोटी है -- लगभग 35 किमी बनाम लगभग 5 किमी।",
   "महासागरीय भूपर्पटी मुख्यतः सिलिका और एल्युमिना से बनी है।"],
  T2, 0,
  "Only statement 1 is correct. Statement 2 describes the continental crust, whose main mineral constituents, silica and alumina, give it the name sial; the oceanic crust consists mainly of silica and magnesium, and is therefore called sima. "
  "The crust is the thinnest of the Earth's layers; beneath it lies the mantle, extending to a depth of about 2,900 km.",
  "केवल कथन 1 सही है। कथन 2 महाद्वीपीय भूपर्पटी का वर्णन करता है, जिसके मुख्य खनिज घटक, सिलिका और एल्युमिना, उसे सियाल (sial) नाम देते हैं; महासागरीय भूपर्पटी मुख्यतः सिलिका और मैग्नीशियम से बनी है, इसलिए उसे सीमा (sima) कहते हैं। "
  "भूपर्पटी पृथ्वी की सबसे पतली परत है; उसके नीचे लगभग 2,900 किमी की गहराई तक मेंटल फैला है।",
  f"{GE7} (Inside Our Earth).",
  "l1-geo-sial-sima-crust-thickness", craft="precision")

# ---------------------------------------------------------------- easy pairs (1)
P(GM, "easy", "Consider the following pairs of landforms and the agents that mainly form them:",
  "भू-आकृतियों और उन्हें मुख्यतः बनाने वाले कारकों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Sea stack : sea waves",
   "Loess : wind",
   "Moraine : running water",
   "Delta : river"],
  ["समुद्री स्तंभ (stack) : समुद्री लहरें",
   "लोयस (Loess) : पवन",
   "हिमोढ़ (Moraine) : बहता जल",
   "डेल्टा : नदी"],
  2,
  "Pairs 1, 2 and 4 are correctly matched. Waves erode hollows into sea caves, which widen into arches and then leave stacks standing as the roofs collapse; fine, light grains of sand carried far by the wind settle as loess, of which China has large deposits; and a river slowing at its mouth drops sediment that builds a delta. "
  "Pair 3 is wrong: moraines are formed by glaciers, from the rocks, sand and silt they carry and deposit when they melt.",
  "युग्म 1, 2 और 4 सही सुमेलित हैं। लहरें खोखलों को अपरदित करके समुद्री गुफाएँ बनाती हैं, जो चौड़ी होकर मेहराब बनती हैं और छत गिरने पर स्तंभ खड़े रह जाते हैं; पवन द्वारा दूर तक ले जाए गए रेत के बारीक, हल्के कण लोयस के रूप में जमते हैं, जिसके बड़े निक्षेप चीन में हैं; और मुहाने पर धीमी पड़ती नदी अवसाद गिराकर डेल्टा बनाती है। "
  "युग्म 3 गलत है: हिमोढ़ हिमनदों से बनते हैं, उन चट्टानों, रेत और गाद से जिन्हें वे ढोते हैं और पिघलने पर जमा करते हैं।",
  f"{GE7} (Our Changing Earth).",
  "l1-geo-stack-loess-moraine-delta-pairs", craft="recall")

# ---------------------------------------------------------------- easy Statement-I/II (1)
A(GM, "easy",
  "Basalt, an extrusive igneous rock, has very fine grains.",
  "बेसाल्ट, एक बहिर्वेधी (extrusive) आग्नेय शैल, के कण बहुत महीन होते हैं।",
  "Lava cools very rapidly when it comes out onto the Earth's surface.",
  "पृथ्वी की सतह पर आने पर लावा बहुत तेज़ी से ठंडा होता है।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I: crystals have little time to grow when lava cools quickly in the open air, so extrusive rocks are fine-grained -- the Deccan plateau is made of basalt. "
  "Magma that cools slowly deep inside the crust forms intrusive igneous rocks such as granite, whose large grains had time to develop.",
  "दोनों कथन सही हैं, और कथन-II कथन-I की व्याख्या करता है: खुली हवा में लावा के तेज़ी से ठंडा होने पर क्रिस्टलों को बढ़ने का समय नहीं मिलता, इसलिए बहिर्वेधी शैलें महीन कणों वाली होती हैं -- दक्कन का पठार बेसाल्ट से बना है। "
  "भूपर्पटी के भीतर गहराई में धीरे-धीरे ठंडा होने वाला मैग्मा ग्रेनाइट जैसी अंतर्वेधी आग्नेय शैलें बनाता है, जिनके बड़े कणों को विकसित होने का समय मिला।",
  f"{GE7} (Inside Our Earth).",
  "l1-geo-basalt-fine-grains-rapid-cooling", craft="inference")

# ---------------------------------------------------------------- medium MCQ (1)
M(GM, "medium", "Which one of the following is a process of chemical weathering?",
  "निम्नलिखित में से कौन-सी रासायनिक अपक्षय (weathering) की प्रक्रिया है?",
  ["oxidation", "frost wedging", "exfoliation", "salt crystal growth"],
  ["ऑक्सीकरण", "तुषार अपक्षय (frost wedging)", "अपशल्कन (exfoliation)", "लवण क्रिस्टलों की वृद्धि"],
  0,
  "In oxidation, minerals combine with oxygen -- iron in rocks, for instance, rusts and weakens; solution, carbonation, hydration and reduction are the other chemical processes, all helped by water and air. "
  "Frost wedging, exfoliation and salt crystal growth are physical processes: they break rocks apart by repeated freezing and thawing, by expansion and contraction with heat, and by the pressure of growing crystals, without changing the minerals.",
  "ऑक्सीकरण में खनिज ऑक्सीजन से मिलते हैं -- जैसे शैलों में लोहे पर जंग लगता है और वे कमज़ोर हो जाती हैं; विलयन, कार्बोनेटीकरण, जलयोजन और अपचयन अन्य रासायनिक प्रक्रियाएँ हैं, जिन्हें जल और वायु से सहायता मिलती है। "
  "तुषार अपक्षय, अपशल्कन और लवण क्रिस्टलों की वृद्धि भौतिक प्रक्रियाएँ हैं: वे खनिजों को बदले बिना शैलों को बार-बार जमने और पिघलने, ताप से फैलने-सिकुड़ने और बढ़ते क्रिस्टलों के दबाव से तोड़ती हैं।",
  f"{FPG} (Geomorphic Processes).",
  "l1-geo-chemical-weathering-oxidation", pos=3, craft="application")

# ---------------------------------------------------------------- medium statement (3)
S(GM, "medium", "Consider the following statements about the evidence for sea-floor spreading:",
  "सागर-नितल प्रसरण (sea-floor spreading) के प्रमाणों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Volcanic eruptions are common all along the mid-oceanic ridges.",
   "Rocks at equal distances on either side of a ridge crest are remarkably similar in age, chemical composition and magnetic properties.",
   "The sediments on the ocean floor are unexpectedly thin.",
   "Earthquakes along the mid-oceanic ridges are shallow, while deep-seated earthquakes occur along the oceanic trenches."],
  ["मध्य-महासागरीय कटकों के साथ-साथ ज्वालामुखी विस्फोट सामान्य हैं।",
   "किसी कटक-शिखर के दोनों ओर समान दूरी पर स्थित शैलें आयु, रासायनिक संघटन और चुंबकीय गुणों में आश्चर्यजनक रूप से समान हैं।",
   "महासागरीय तल पर अवसाद अप्रत्याशित रूप से पतले हैं।",
   "मध्य-महासागरीय कटकों के साथ भूकंप उथले होते हैं, जबकि गहरे उद्गम वाले भूकंप महासागरीय गर्तों के साथ होते हैं।"],
  C4, 3,
  "All four statements are correct. These observations, gathered from mapping the ocean floor after the Second World War, led Harry Hess to propose in 1961 that the crust keeps forming along the ridges, where magma rises and spreads the floor apart on either side, and is consumed where it sinks back into the mantle at the trenches. "
  "That is why the ocean floor is young and lightly covered with sediment, and why the youngest rocks lie nearest the ridge crest.",
  "चारों कथन सही हैं। द्वितीय विश्वयुद्ध के बाद महासागरीय तल के मानचित्रण से मिले इन प्रेक्षणों के आधार पर हैरी हेस ने 1961 में प्रस्तावित किया कि भूपर्पटी कटकों के साथ बनती रहती है, जहाँ मैग्मा ऊपर उठकर तल को दोनों ओर फैलाता है, और गर्तों पर मेंटल में वापस धँसकर नष्ट होती है। "
  "इसीलिए महासागरीय तल नवीन है और उस पर अवसाद की पतली परत है, और सबसे नवीन शैलें कटक-शिखर के सबसे निकट हैं।",
  f"{FPG} (Distribution of Oceans and Continents).",
  "l1-geo-sea-floor-spreading-evidence", craft="multi")

S(GM, "medium", "Consider the following statements about the sources of information on the Earth's interior:",
  "पृथ्वी के आंतरिक भाग की जानकारी के स्रोतों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The deepest drill so far, at Kola in the Arctic region, has reached a depth of about 12 km.",
   "Gravity anomalies give information about the distribution of mass in the crust.",
   "Meteors that reach the Earth are made of materials similar to those of the Earth's interior.",
   "Volcanic eruptions are counted among the indirect sources of information about the interior."],
  ["अब तक का सबसे गहरा वेधन, आर्कटिक क्षेत्र में कोला पर, लगभग 12 किमी की गहराई तक पहुँचा है।",
   "गुरुत्व विसंगतियाँ भूपर्पटी में द्रव्यमान के वितरण की जानकारी देती हैं।",
   "पृथ्वी तक पहुँचने वाले उल्काएँ पृथ्वी के आंतरिक भाग जैसे पदार्थों से बने होते हैं।",
   "ज्वालामुखी विस्फोटों को आंतरिक भाग की जानकारी के अप्रत्यक्ष स्रोतों में गिना जाता है।"],
  C4, 2,
  "Statements 1, 2 and 3 are correct. Statement 4 is wrong: since an eruption brings material from within the Earth to the surface, NCERT counts volcanic eruptions, with mining and deep drilling, among the direct sources. "
  "Most of what we know comes indirectly -- from the rise of temperature, pressure and density with depth, from meteors, from gravity and magnetic surveys, and above all from how earthquake waves travel through the Earth.",
  "कथन 1, 2 और 3 सही हैं। कथन 4 गलत है: चूँकि विस्फोट पृथ्वी के भीतर से पदार्थ सतह पर लाता है, NCERT ज्वालामुखी विस्फोटों को खनन और गहरे वेधन के साथ प्रत्यक्ष स्रोतों में गिनता है। "
  "हमारी अधिकांश जानकारी अप्रत्यक्ष रूप से आती है -- गहराई के साथ तापमान, दबाव और घनत्व के बढ़ने से, उल्काओं से, गुरुत्व और चुंबकीय सर्वेक्षणों से, और सबसे बढ़कर इससे कि भूकंपीय तरंगें पृथ्वी में कैसे चलती हैं।",
  f"{FPG} (The Interior of the Earth).",
  "l1-geo-interior-direct-indirect-sources", craft="precision")

S(GM, "medium", "Consider the following statements about mass movements:",
  "बृहत् संचलन (mass movements) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Mass movements transfer rock debris down slopes under the direct influence of gravity.",
   "Like erosion, mass movements need an agent such as running water, wind or ice to carry the debris.",
   "Solifluction is the slow downslope flow of soil saturated with water, common where the surface of frozen ground thaws."],
  ["बृहत् संचलन गुरुत्व के प्रत्यक्ष प्रभाव से शैल-मलबे को ढलानों से नीचे ले जाते हैं।",
   "अपरदन की तरह, बृहत् संचलन को मलबा ढोने के लिए बहते जल, पवन या हिम जैसे किसी कारक की आवश्यकता होती है।",
   "मृदा-सर्पण (solifluction) जल से संतृप्त मिट्टी का ढलान से नीचे धीमा प्रवाह है, जो वहाँ सामान्य है जहाँ जमी हुई भूमि की सतह पिघलती है।"],
  C3, 1,
  "Statements 1 and 3 are correct. Statement 2 is wrong: in mass movements air, water or ice do not carry the debris from place to place -- the debris may carry them along with it -- and for this reason mass movements do not come under erosion. "
  "They range from slow movements such as creep and solifluction to rapid ones such as landslides, slumps and debris avalanches, which are common in the Himalaya; weak, weathered material on steep slopes and heavy rain make them more likely.",
  "कथन 1 और 3 सही हैं। कथन 2 गलत है: बृहत् संचलन में वायु, जल या हिम मलबे को एक स्थान से दूसरे स्थान तक नहीं ढोते -- बल्कि मलबा उन्हें अपने साथ ले जा सकता है -- और इसी कारण बृहत् संचलन अपरदन में नहीं गिने जाते। "
  "ये विसर्पण (creep) और मृदा-सर्पण जैसी धीमी हलचलों से लेकर भूस्खलन, अवसर्पण और मलबा-अवधाव जैसी तेज़ हलचलों तक होते हैं, जो हिमालय में आम हैं; खड़ी ढलानों पर कमज़ोर, अपक्षयित पदार्थ और भारी वर्षा इनकी संभावना बढ़ाते हैं।",
  f"{FPG} (Geomorphic Processes).",
  "l1-geo-mass-movement-gravity-solifluction", craft="precision")

# ---------------------------------------------------------------- medium Statement-I/II (1)
A(GM, "medium",
  "The Himalaya are still rising.",
  "हिमालय अब भी ऊपर उठ रहे हैं।",
  "The Indian plate continues to move north and push against the Eurasian plate.",
  "भारतीय प्लेट अब भी उत्तर की ओर खिसक रही है और यूरेशियाई प्लेट को धकेल रही है।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I. India, once separated from Asia by the Tethys Sea, began its northward journey after Pangaea broke up and collided with Asia about 40-50 million years ago, crumpling the sediments between them into the Himalaya. "
  "The plate is still moving, so the process continues: the mountains are still gaining height, and the Himalayan belt remains one of the most earthquake-prone regions of the country.",
  "दोनों कथन सही हैं, और कथन-II कथन-I की व्याख्या करता है। कभी टेथिस सागर द्वारा एशिया से अलग भारत ने पैंजिया के टूटने के बाद उत्तर की ओर यात्रा आरंभ की और लगभग 4-5 करोड़ वर्ष पहले एशिया से टकराया, जिससे दोनों के बीच के अवसाद मुड़कर हिमालय बन गए। "
  "प्लेट अब भी खिसक रही है, इसलिए प्रक्रिया जारी है: पर्वत अब भी ऊँचे हो रहे हैं, और हिमालयी पट्टी देश के सबसे अधिक भूकंप-प्रवण क्षेत्रों में बनी हुई है।",
  f"{FPG} (Distribution of Oceans and Continents).",
  "l1-geo-himalaya-still-rising-indian-plate", craft="inference")

# ---------------------------------------------------------------- hard statement (1)
S(GM, "hard", "Consider the following statements about intrusive igneous landforms:",
  "अंतर्वेधी आग्नेय भू-आकृतियों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Dykes, wall-like intrusions that cut almost perpendicular to the ground, are common in western Maharashtra and are regarded as feeders of the Deccan Traps.",
   "Sills are near-vertical sheets of igneous rock that cut across the layers of the surrounding rock.",
   "Many domal hills of granite on the Karnataka plateau are examples of laccoliths or batholiths."],
  ["डाइक, यानी भूमि को लगभग लंबवत काटने वाली दीवार जैसी अंतर्वेधी संरचनाएँ, पश्चिमी महाराष्ट्र में आम हैं और दक्कन ट्रैप की पोषक मानी जाती हैं।",
   "सिल आग्नेय शैल की लगभग ऊर्ध्वाधर परतें हैं जो आसपास की शैल की परतों को काटती हैं।",
   "कर्नाटक पठार की ग्रेनाइट की कई गुंबदाकार पहाड़ियाँ लैकोलिथ या बैथोलिथ के उदाहरण हैं।"],
  C3, 1,
  "Statements 1 and 3 are correct. Lava that rises through cracks and fissures and solidifies there forms dykes, and large dome-shaped intrusive bodies -- laccoliths, with a level base and a pipe-like conduit from below, and the still larger batholiths -- are exposed when the rocks above are eroded, as on the Karnataka plateau. "
  "Statement 2 is wrong: sills are near-horizontal bodies of igneous rock, thinner ones being called sheets; it is dykes that are near-vertical.",
  "कथन 1 और 3 सही हैं। दरारों और विदरों से ऊपर उठकर वहीं जमने वाला लावा डाइक बनाता है, और बड़े गुंबदाकार अंतर्वेधी पिंड -- समतल आधार और नीचे से नली जैसे मार्ग वाले लैकोलिथ, और उनसे भी बड़े बैथोलिथ -- ऊपर की शैलों के अपरदित होने पर दिखने लगते हैं, जैसे कर्नाटक पठार पर। "
  "कथन 2 गलत है: सिल आग्नेय शैल के लगभग क्षैतिज पिंड हैं, पतले पिंड शीट कहलाते हैं; लगभग ऊर्ध्वाधर तो डाइक होते हैं।",
  f"{FPG} (The Interior of the Earth).",
  "l1-geo-dykes-sills-laccoliths", craft="precision")

write("geo_l1_t4_d.sql")
