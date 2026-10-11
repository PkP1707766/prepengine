# -*- coding: utf-8 -*-
"""Level 1 · Test 3 (Environment & Ecology, NCERT Foundation) -- part E: Protected Areas & Wildlife Protection (12)
and International Conventions & Organisations (6) (upsc_l1_cell_targets.mjs 3).
The angle is conservation as NCERT teaches it -- biosphere reserves and sanctuaries (Science VIII), the
consequences of deforestation, community conservation, development projects and endangered and endemic
species (Geography X), the tiger's decline -- and the ideas behind the international environmental order:
Brundtland, the Club of Rome and Schumacher, Rio's Agenda 21, the ozone conventions and Stockholm 1972.
Level-2 facts are not repeated (the biosphere zones, MAB and Nilgiri, Project Tiger's year and Hailey NP, the
Narcondam hornbill, the mithun, Chipko, Appiko and the NBA, the sacred groves' names, the Ramsar dates, World
Environment Day, the Earth Summit's place, UNEP's founding, the chemicals conventions). MCQ keys are pinned."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Environment & Ecology"
d.REQUIRE_CRAFT = True
PA, IC = "Protected Areas & Wildlife Protection", "International Conventions & Organisations"
SC8 = "NCERT Class VIII, Science (Conservation of Plants and Animals)"
GE10 = "NCERT Class X, Geography -- Contemporary India II"
BI12 = "NCERT Class XII, Biology (Biodiversity and Conservation)"

# ================================================================ PROTECTED AREAS & WILDLIFE PROTECTION (12)
M(PA, "easy", "The Pachmarhi Biosphere Reserve includes which one of the following national parks?",
  "पचमढ़ी जीवमंडल आरक्षित क्षेत्र (Biosphere Reserve) में निम्नलिखित में से कौन-सा राष्ट्रीय उद्यान शामिल है?",
  ["Satpura", "Kanha", "Panna", "Bandhavgarh"],
  ["सतपुड़ा", "कान्हा", "पन्ना", "बांधवगढ़"],
  0,
  "The Pachmarhi Biosphere Reserve consists of one national park, Satpura, and two wildlife sanctuaries, Bori and Pachmarhi; its plants and animals resemble those of the Himalayan foothills and the lower Western Ghats, and the rock shelters of Satpura hold evidence of prehistoric human life. "
  "Biosphere reserves are meant to conserve the biodiversity and culture of an area, and a reserve may contain other protected areas within it.",
  "पचमढ़ी जीवमंडल आरक्षित क्षेत्र में एक राष्ट्रीय उद्यान, सतपुड़ा, और दो वन्यजीव अभयारण्य, बोरी और पचमढ़ी, हैं; इसके पौधे और जंतु हिमालय की तलहटी और निचले पश्चिमी घाट के समान हैं, और सतपुड़ा की शैलाश्रयों (rock shelters) में प्रागैतिहासिक मानव जीवन के साक्ष्य हैं। "
  "जीवमंडल आरक्षित क्षेत्रों का उद्देश्य किसी क्षेत्र की जैव-विविधता और संस्कृति का संरक्षण है, और एक आरक्षित क्षेत्र में अन्य संरक्षित क्षेत्र भी शामिल हो सकते हैं।",
  SC8 + ".",
  "l1-env-pachmarhi-br-satpura", pos=3, craft="recall")

S(PA, "easy", "Consider the following statements about protected areas:",
  "संरक्षित क्षेत्रों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Biosphere reserves are meant to conserve biodiversity along with the culture and traditional ways of life of the people who live there.",
   "A wildlife sanctuary is set up mainly to protect plants, and the animals in it receive no special protection."],
  ["जीवमंडल आरक्षित क्षेत्रों का उद्देश्य जैव-विविधता के साथ-साथ वहाँ रहने वाले लोगों की संस्कृति और परंपरागत जीवन-शैली का संरक्षण है।",
   "वन्यजीव अभयारण्य मुख्य रूप से पौधों की रक्षा के लिए बनाया जाता है, और उसमें जंतुओं को कोई विशेष सुरक्षा नहीं मिलती।"],
  T2, 0,
  "Only statement 1 is correct: a biosphere reserve is a large protected area for the conservation of wildlife, plant and animal resources and the traditional life of the tribal people living there. "
  "Statement 2 is wrong: a wildlife sanctuary is an area where animals are protected from any disturbance to them and their habitat; a national park is a larger area reserved for wildlife, where the animals can freely use the habitat and natural resources.",
  "केवल कथन 1 सही है: जीवमंडल आरक्षित क्षेत्र वन्यजीवों, पादप और जंतु संसाधनों और वहाँ रहने वाले आदिवासियों के परंपरागत जीवन के संरक्षण के लिए एक बड़ा संरक्षित क्षेत्र है। "
  "कथन 2 गलत है: वन्यजीव अभयारण्य वह क्षेत्र है जहाँ जंतुओं और उनके आवास को किसी भी बाधा से बचाया जाता है; राष्ट्रीय उद्यान वन्यजीवों के लिए आरक्षित एक बड़ा क्षेत्र है, जहाँ जंतु आवास और प्राकृतिक संसाधनों का मुक्त रूप से उपयोग कर सकते हैं।",
  SC8 + ".",
  "l1-env-biosphere-reserve-sanctuary-meaning", craft="precision")

S(PA, "easy", "Consider the following statements about communities and conservation in India:",
  "भारत में समुदायों और संरक्षण के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["In the Sariska Tiger Reserve, villagers have fought against mining by citing the Wild Life (Protection) Act.",
   "In many areas, local communities protect habitats themselves, seeing them as the basis of their long-term livelihood.",
   "Community conservation in India began only with the Forest Rights Act, 2006."],
  ["सरिस्का बाघ आरक्षित क्षेत्र में ग्रामीणों ने वन्यजीव (संरक्षण) अधिनियम का हवाला देकर खनन के विरुद्ध संघर्ष किया है।",
   "कई क्षेत्रों में स्थानीय समुदाय आवासों की स्वयं रक्षा करते हैं, उन्हें अपनी दीर्घकालिक आजीविका का आधार मानते हुए।",
   "भारत में सामुदायिक संरक्षण केवल वन अधिकार अधिनियम, 2006 से ही शुरू हुआ।"],
  C3, 1,
  "Statements 1 and 2 are correct: conservation is not only the work of the government -- communities that depend on forests have often been their strongest defenders, sometimes using the law itself, as at Sariska. "
  "Statement 3 is wrong: community protection of forests and wildlife is centuries old -- sacred groves, the Bishnois' protection of trees and animals, and movements such as Chipko long predate the 2006 Act, which recognised such rights in law.",
  "कथन 1 और 2 सही हैं: संरक्षण केवल सरकार का काम नहीं है -- वनों पर निर्भर समुदाय प्रायः उनके सबसे सशक्त रक्षक रहे हैं, कभी-कभी स्वयं क़ानून का उपयोग करते हुए, जैसे सरिस्का में। "
  "कथन 3 गलत है: वनों और वन्यजीवों की सामुदायिक रक्षा सदियों पुरानी है -- पवित्र उपवन, बिश्नोइयों द्वारा वृक्षों और जंतुओं की रक्षा, और चिपको जैसे आंदोलन 2006 के अधिनियम से बहुत पहले के हैं, जिसने ऐसे अधिकारों को क़ानूनी मान्यता दी।",
  f"{GE10} (Forest and Wildlife Resources).",
  "l1-env-sariska-community-conservation", craft="inference")

M(PA, "medium", "The Mundas and the Santhals of the Chota Nagpur region traditionally worship which trees?",
  "छोटानागपुर क्षेत्र के मुंडा और संथाल परंपरागत रूप से किन वृक्षों की पूजा करते हैं?",
  ["Mahua and kadamba", "Tamarind and mango", "Sal and teak", "Deodar and pine"],
  ["महुआ और कदंब", "इमली और आम", "साल और सागौन", "देवदार और चीड़"],
  0,
  "The Mundas and the Santhals worship the mahua and the kadamba, while the tribal peoples of Odisha and Bihar worship the tamarind and the mango during weddings; to many people the peepal and the banyan are sacred. "
  "Such traditions of nature worship -- which also protect whole patches of forest as sacred groves -- have helped conserve trees and the wildlife around them for generations.",
  "मुंडा और संथाल महुआ और कदंब की पूजा करते हैं, जबकि ओडिशा और बिहार के आदिवासी विवाह के समय इमली और आम की पूजा करते हैं; बहुत-से लोगों के लिए पीपल और बरगद पवित्र हैं। "
  "प्रकृति-पूजा की ऐसी परंपराओं ने -- जो पवित्र उपवनों के रूप में वनों के पूरे टुकड़ों की भी रक्षा करती हैं -- पीढ़ियों से वृक्षों और उनके आसपास के वन्यजीवों के संरक्षण में मदद की है।",
  f"{GE10} (Forest and Wildlife Resources).",
  "l1-env-mahua-kadamba-munda-santhal", pos=3, craft="precision")

S(PA, "medium", "Consider the following statements about the consequences of deforestation:",
  "वनों की कटाई के परिणामों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Deforestation increases the amount of carbon dioxide in the air.",
   "It lowers the level of groundwater.",
   "It makes soil erosion, floods and droughts more likely.",
   "It can gradually turn fertile land into desert."],
  ["वनों की कटाई वायु में कार्बन डाइऑक्साइड की मात्रा बढ़ाती है।",
   "यह भूजल का स्तर घटाती है।",
   "यह मिट्टी के कटाव, बाढ़ और सूखे की संभावना बढ़ाती है।",
   "यह उपजाऊ भूमि को धीरे-धीरे मरुस्थल में बदल सकती है।"],
  C4, 3,
  "All four statements are correct. With fewer trees to take it up, carbon dioxide builds up in the air; without the cover and roots of trees, rainwater runs off instead of soaking in, the water table falls, the topsoil is washed or blown away, and both floods and droughts become more frequent. "
  "Over time, the loss of soil fertility and moisture can turn land into desert -- the process of desertification -- and the reduced transpiration may also mean less rainfall in the area.",
  "चारों कथन सही हैं। उसे सोखने वाले वृक्ष कम होने से वायु में कार्बन डाइऑक्साइड बढ़ती है; वृक्षों के आवरण और जड़ों के बिना वर्षा का पानी रिसने के बजाय बह जाता है, भूजल-स्तर गिरता है, ऊपरी मिट्टी बह या उड़ जाती है, और बाढ़ तथा सूखा, दोनों अधिक होते हैं। "
  "समय के साथ मिट्टी की उर्वरता और नमी खोने से भूमि मरुस्थल बन सकती है -- यही मरुस्थलीकरण है -- और वाष्पोत्सर्जन घटने से क्षेत्र में वर्षा भी कम हो सकती है।",
  SC8 + ".",
  "l1-env-deforestation-consequences", craft="linkage")

S(PA, "medium", "Consider the following statements about the effect of development projects on forests and wildlife:",
  "वनों और वन्यजीवों पर विकास परियोजनाओं के प्रभाव के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Dolomite mining has seriously threatened the Buxa Tiger Reserve, disturbing habitats and blocking the migration route of elephants.",
   "Since independence, thousands of square kilometres of forest have been cleared for river valley projects.",
   "The Buxa Tiger Reserve lies in Madhya Pradesh."],
  ["डोलोमाइट खनन ने बक्सा बाघ आरक्षित क्षेत्र को गंभीर ख़तरे में डाला है, जिससे आवास बाधित हुए और हाथियों का प्रवास-मार्ग रुक गया।",
   "स्वतंत्रता के बाद से नदी घाटी परियोजनाओं के लिए हज़ारों वर्ग किलोमीटर वन साफ़ किए गए हैं।",
   "बक्सा बाघ आरक्षित क्षेत्र मध्य प्रदेश में है।"],
  C3, 1,
  "Statements 1 and 2 are correct: since 1951 over 5,000 square kilometres of forest were cleared for river valley projects, and mining continues to destroy habitats -- the dolomite mining at Buxa disturbed the natural habitat of many species and blocked the migration route of others, including the elephant. "
  "Statement 3 is wrong: the Buxa Tiger Reserve is in West Bengal, in the Duars at the foot of the Himalaya near the border with Bhutan.",
  "कथन 1 और 2 सही हैं: 1951 के बाद नदी घाटी परियोजनाओं के लिए 5,000 वर्ग किलोमीटर से अधिक वन साफ़ किए गए, और खनन आवासों को नष्ट करता रहा है -- बक्सा में डोलोमाइट खनन ने कई प्रजातियों के प्राकृतिक आवास को बाधित किया और हाथी सहित अन्य के प्रवास-मार्ग को रोक दिया। "
  "कथन 3 गलत है: बक्सा बाघ आरक्षित क्षेत्र पश्चिम बंगाल में, भूटान की सीमा के पास हिमालय की तलहटी के द्वार (Duars) क्षेत्र में है।",
  f"{GE10} (Forest and Wildlife Resources).",
  "l1-env-buxa-dolomite-river-projects", craft="precision")

S(PA, "medium", "Consider the following animals:",
  "निम्नलिखित जंतुओं पर विचार कीजिए:",
  ["Andaman teal", "Nicobar pigeon", "Andaman wild pig"],
  ["अंडमान टील", "निकोबार कबूतर", "अंडमान जंगली सूअर"],
  C3, 2,
  "All three are endemic species of the islands -- found there and nowhere else -- which NCERT uses as examples of endemism. "
  "Island species are especially vulnerable: their small, isolated populations cannot easily be replaced from elsewhere, so the loss of habitat, the arrival of predators or competitors, or a single disaster can drive them towards extinction.",
  "तीनों द्वीपों की स्थानिक प्रजातियाँ हैं -- जो वहीं मिलती हैं और कहीं नहीं -- जिन्हें NCERT स्थानिकता के उदाहरणों के रूप में देता है। "
  "द्वीपीय प्रजातियाँ विशेष रूप से असुरक्षित होती हैं: उनकी छोटी, अलग-थलग आबादियाँ कहीं और से आसानी से नहीं भरी जा सकतीं, इसलिए आवास का ह्रास, शिकारियों या प्रतिस्पर्धियों का आगमन, या एक ही आपदा उन्हें विलुप्ति की ओर ले जा सकती है।",
  f"{GE10} (Forest and Wildlife Resources).",
  "l1-env-andaman-nicobar-endemics", craft="recall",
  closing="How many of the above are endemic species of the Andaman and Nicobar Islands?",
  closing_hi="उपर्युक्त में से कितनी अंडमान और निकोबार द्वीपसमूह की स्थानिक प्रजातियाँ हैं?")

S(PA, "medium", "Consider the following statements about saving paper:",
  "काग़ज़ बचाने के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Paper can be recycled five to seven times before it becomes unusable.",
   "Recycling paper saves no trees, since recycled paper needs as much fresh wood pulp as new paper.",
   "Making one tonne of paper needs only a single full-grown tree."],
  ["काग़ज़ को अनुपयोगी होने से पहले पाँच से सात बार पुनर्चक्रित किया जा सकता है।",
   "काग़ज़ के पुनर्चक्रण से कोई वृक्ष नहीं बचता, क्योंकि पुनर्चक्रित काग़ज़ को भी नए काग़ज़ जितनी ही ताज़ा लुगदी चाहिए।",
   "एक टन काग़ज़ बनाने के लिए केवल एक पूर्ण विकसित वृक्ष चाहिए।"],
  C3, 0,
  "Only statement 1 is correct. Statement 2 is wrong: recycled fibre replaces fresh wood pulp, so every tonne of paper recycled reduces the number of trees that must be felled, and also saves water and energy. "
  "Statement 3 is wrong: about 17 full-grown trees are needed to make one tonne of paper -- which is why saving even one sheet a day per student, and recycling used paper, can save many trees in a year.",
  "केवल कथन 1 सही है। कथन 2 गलत है: पुनर्चक्रित रेशा ताज़ा लकड़ी की लुगदी का स्थान लेता है, इसलिए पुनर्चक्रित हर टन काग़ज़ काटे जाने वाले वृक्षों की संख्या घटाता है, और पानी तथा ऊर्जा भी बचाता है। "
  "कथन 3 गलत है: एक टन काग़ज़ बनाने में लगभग 17 पूर्ण विकसित वृक्ष लगते हैं -- इसीलिए हर विद्यार्थी द्वारा दिन में एक पन्ना भी बचाना, और प्रयुक्त काग़ज़ का पुनर्चक्रण, वर्ष भर में बहुत-से वृक्ष बचा सकता है।",
  SC8 + ".",
  "l1-env-paper-recycling-trees", craft="application")

A(PA, "medium",
  "Large dams can lead to a loss of forests and wildlife.",
  "बड़े बाँध वनों और वन्यजीवों की हानि का कारण बन सकते हैं।",
  "Their reservoirs submerge large areas of forest and break up the habitats of animals.",
  "उनके जलाशय वनों के बड़े क्षेत्र डुबो देते हैं और जंतुओं के आवासों को टुकड़ों में बाँट देते हैं।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I. River valley projects have been among the major causes of forest loss in India since independence; besides drowning forests, they fragment habitats and cut migration routes, and they also displace forest-dwelling communities. "
  "This is why large projects in forest areas need environmental clearance and, under the forest law, compensatory afforestation elsewhere.",
  "दोनों कथन सही हैं, और कथन-II कथन-I की व्याख्या करता है। स्वतंत्रता के बाद से नदी घाटी परियोजनाएँ भारत में वन-ह्रास के प्रमुख कारणों में रही हैं; वनों को डुबोने के साथ-साथ वे आवासों को खंडित करती हैं, प्रवास-मार्ग काटती हैं, और वनवासी समुदायों को विस्थापित भी करती हैं। "
  "इसीलिए वन क्षेत्रों में बड़ी परियोजनाओं के लिए पर्यावरणीय स्वीकृति और, वन क़ानून के तहत, कहीं और प्रतिपूरक वनीकरण आवश्यक है।",
  f"{GE10} (Forest and Wildlife Resources).",
  "l1-env-dams-forest-wildlife-loss", craft="inference")

S(PA, "hard", "Consider the following statements about the decline of the tiger in India before Project Tiger:",
  "प्रोजेक्ट टाइगर से पहले भारत में बाघों की संख्या में गिरावट के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The tiger census of 1973 counted about 1,800 tigers, far fewer than at the start of the twentieth century.",
   "Poaching for trade, shrinking habitat, the depletion of prey and a growing human population were among the major threats.",
   "Trade in tiger skins and the use of tiger bones in traditional medicines, especially in Asian countries, drove much of the poaching."],
  ["1973 की बाघ गणना में लगभग 1,800 बाघ गिने गए, जो बीसवीं सदी के आरंभ से बहुत कम थे।",
   "व्यापार के लिए अवैध शिकार, सिकुड़ते आवास, शिकार-प्राणियों की कमी और बढ़ती मानव जनसंख्या प्रमुख ख़तरों में थे।",
   "बाघ की खाल के व्यापार और विशेषकर एशियाई देशों में पारंपरिक औषधियों में बाघ की हड्डियों के उपयोग ने अधिकांश अवैध शिकार को बढ़ावा दिया।"],
  C3, 2,
  "All three statements are correct. NCERT records that the tiger population fell from an estimated 55,000 at the turn of the twentieth century to 1,827 in 1973. "
  "Since India and Nepal hold most of the world's tigers, they became prime targets for poaching and illegal trade -- skins for decoration, and bones and other parts for traditional medicines -- which is why protecting the tiger needs both habitat protection and action against the trade.",
  "तीनों कथन सही हैं। NCERT के अनुसार बाघों की संख्या बीसवीं सदी के आरंभ के अनुमानित 55,000 से घटकर 1973 में 1,827 रह गई। "
  "चूँकि विश्व के अधिकांश बाघ भारत और नेपाल में हैं, वे अवैध शिकार और अवैध व्यापार के प्रमुख निशाने बने -- सजावट के लिए खालें, और पारंपरिक औषधियों के लिए हड्डियाँ और अन्य अंग -- इसीलिए बाघ की रक्षा के लिए आवास-संरक्षण और व्यापार के विरुद्ध कार्रवाई, दोनों चाहिए।",
  f"{GE10} (Forest and Wildlife Resources).",
  "l1-env-tiger-decline-1973-threats", craft="precision")

P(PA, "hard", "Consider the following pairs of community efforts and what they are known for:",
  "सामुदायिक प्रयासों और उनकी पहचान के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Bhairodev Dakav 'Sonchuri' : Forest declared by villagers of Alwar district, with their own rules banning hunting",
   "Beej Bachao Andolan : Movement in Tehri showing that diverse crops can be grown without synthetic chemicals",
   "Navdanya : Network conserving the seeds of traditional crop varieties",
   "Sacred groves of the Khasi and Jaintia Hills : Meghalaya"],
  ["भैरोदेव डाकव 'सोनचुरी' : अलवर ज़िले के ग्रामीणों द्वारा घोषित वन, जिसमें उनके अपने नियम शिकार पर रोक लगाते हैं",
   "बीज बचाओ आंदोलन : टिहरी का आंदोलन, जिसने दिखाया कि संश्लिष्ट रसायनों के बिना विविध फ़सलें उगाई जा सकती हैं",
   "नवधान्य : पारंपरिक फ़सल किस्मों के बीज बचाने वाला नेटवर्क",
   "खासी और जयंतिया पहाड़ियों के पवित्र उपवन : मेघालय"],
  3,
  "All four pairs are correctly matched. The inhabitants of five villages in Alwar district declared 1,200 hectares of forest the Bhairodev Dakav 'Sonchuri' and protect its wildlife against outside encroachment; farmers and citizens' groups such as the Beej Bachao Andolan and Navdanya have shown that diversified crop production without synthetic chemicals is possible and economically viable. "
  "In Meghalaya, the sacred groves of the Khasi and Jaintia Hills are the last refuges of many rare and threatened plants.",
  "चारों युग्म सही सुमेलित हैं। अलवर ज़िले के पाँच गाँवों के निवासियों ने 1,200 हेक्टेयर वन को भैरोदेव डाकव 'सोनचुरी' घोषित किया और उसके वन्यजीवों की बाहरी अतिक्रमण से रक्षा करते हैं; बीज बचाओ आंदोलन और नवधान्य जैसे किसानों और नागरिकों के समूहों ने दिखाया है कि संश्लिष्ट रसायनों के बिना विविध फ़सल उत्पादन संभव और आर्थिक रूप से व्यवहार्य है। "
  "मेघालय में खासी और जयंतिया पहाड़ियों के पवित्र उपवन अनेक दुर्लभ और संकटग्रस्त पौधों के अंतिम आश्रय हैं।",
  f"{GE10} (Forest and Wildlife Resources); {BI12}.",
  "l1-env-community-conservation-pairs", craft="precision")

P(PA, "hard", "Consider the following pairs of biosphere reserves and the States in which they lie:",
  "जीवमंडल आरक्षित क्षेत्रों और उन राज्यों के निम्नलिखित युग्मों पर विचार कीजिए जिनमें वे स्थित हैं:",
  ["Nokrek : Meghalaya", "Similipal : Odisha", "Agasthyamalai : Kerala and Tamil Nadu", "Cold Desert : Rajasthan"],
  ["नोकरेक : मेघालय", "सिमलीपाल : ओडिशा", "अगस्त्यमलाई : केरल और तमिलनाडु", "कोल्ड डेज़र्ट (शीत मरुस्थल) : राजस्थान"],
  2,
  "Pairs 1, 2 and 3 are correctly matched: Nokrek lies in the Garo Hills of Meghalaya, Similipal in the Mayurbhanj district of Odisha, and Agasthyamalai at the southern end of the Western Ghats, across Kerala and Tamil Nadu. "
  "Pair 4 is wrong: the Cold Desert Biosphere Reserve is in Himachal Pradesh, in the high, dry Trans-Himalayan region of Spiti and Lahaul, and includes the Pin Valley National Park; the Thar of Rajasthan is a hot desert.",
  "युग्म 1, 2 और 3 सही सुमेलित हैं: नोकरेक मेघालय की गारो पहाड़ियों में, सिमलीपाल ओडिशा के मयूरभंज ज़िले में, और अगस्त्यमलाई पश्चिमी घाट के दक्षिणी छोर पर केरल और तमिलनाडु में फैला है। "
  "युग्म 4 गलत है: कोल्ड डेज़र्ट जीवमंडल आरक्षित क्षेत्र हिमाचल प्रदेश में, स्पीति और लाहौल के ऊँचे, शुष्क पार-हिमालयी क्षेत्र में है, और इसमें पिन वैली राष्ट्रीय उद्यान शामिल है; राजस्थान का थार एक गर्म मरुस्थल है।",
  "Ministry of Environment, Forest and Climate Change (Biosphere Reserves of India); NCERT Class XI, Geography -- India: Physical Environment (Natural Vegetation).",
  "l1-env-biosphere-reserves-states-pairs", craft="precision")

# ================================================================ INTERNATIONAL CONVENTIONS & ORGANISATIONS (6)
M(IC, "easy", "The concept of 'sustainable development' was introduced and popularised by",
  "'सतत विकास' (sustainable development) की अवधारणा किसने प्रस्तुत की और लोकप्रिय बनाई?",
  ["the report Our Common Future (1987) of the Brundtland Commission",
   "the Stockholm Declaration adopted by the UN Conference on the Human Environment (1972)",
   "the First Assessment Report of the Intergovernmental Panel on Climate Change (1990)",
   "the Kyoto Protocol adopted in 1997"],
  ["ब्रंटलैंड आयोग की रिपोर्ट 'अवर कॉमन फ़्यूचर' (1987)",
   "मानव पर्यावरण पर संयुक्त राष्ट्र सम्मेलन द्वारा अपनाई गई स्टॉकहोम घोषणा (1972)",
   "जलवायु परिवर्तन पर अंतर-सरकारी पैनल की पहली आकलन रिपोर्ट (1990)",
   "1997 में अपनाया गया क्योटो प्रोटोकॉल"],
  0,
  "The World Commission on Environment and Development, chaired by Gro Harlem Brundtland, introduced the concept in its 1987 report, published as Our Common Future, and advocated it as a means of conserving resources; it defined sustainable development as development that meets the needs of the present without compromising the ability of future generations to meet their own needs. "
  "The idea shaped the Rio Earth Summit of 1992 and the international agenda that followed.",
  "ग्रो हार्लेम ब्रंटलैंड की अध्यक्षता वाले पर्यावरण और विकास पर विश्व आयोग ने 1987 की अपनी रिपोर्ट में, जो 'अवर कॉमन फ़्यूचर' के रूप में प्रकाशित हुई, यह अवधारणा प्रस्तुत की और इसे संसाधन संरक्षण के साधन के रूप में आगे रखा; इसने सतत विकास को ऐसा विकास बताया जो भावी पीढ़ियों की अपनी ज़रूरतें पूरी करने की क्षमता से समझौता किए बिना वर्तमान की ज़रूरतें पूरी करे। "
  "इस विचार ने 1992 के रियो पृथ्वी सम्मेलन और उसके बाद के अंतरराष्ट्रीय एजेंडे को आकार दिया।",
  f"{GE10} (Resources and Development).",
  "l1-env-brundtland-our-common-future", pos=3, craft="precision")

S(IC, "easy", "Consider the following statements about the Earth Summit held at Rio de Janeiro in 1992:",
  "1992 में रियो डी जनेरियो में हुए पृथ्वी सम्मेलन के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It adopted Agenda 21, an agenda for achieving sustainable development in the twenty-first century.",
   "It also adopted a set of 'Forest Principles' on the management of forests."],
  ["इसने एजेंडा 21 अपनाया, जो इक्कीसवीं सदी में सतत विकास प्राप्त करने का एक एजेंडा है।",
   "इसने वनों के प्रबंधन पर 'वन सिद्धांतों' (Forest Principles) का एक समूह भी अपनाया।"],
  T2, 2,
  "Both statements are correct. More than a hundred heads of state met at Rio to address urgent problems of environmental protection and socio-economic development; Agenda 21 aims at combating environmental damage, poverty and disease through global cooperation on common interests, mutual needs and shared responsibilities. "
  "One of its main ideas is that every local government should draw up its own local Agenda 21.",
  "दोनों कथन सही हैं। सौ से अधिक राष्ट्राध्यक्ष रियो में पर्यावरण संरक्षण और सामाजिक-आर्थिक विकास की तात्कालिक समस्याओं पर मिले; एजेंडा 21 का उद्देश्य साझा हितों, पारस्परिक ज़रूरतों और साझा ज़िम्मेदारियों पर वैश्विक सहयोग से पर्यावरणीय क्षति, ग़रीबी और रोगों से लड़ना है। "
  "इसका एक मुख्य विचार यह है कि हर स्थानीय सरकार अपना स्थानीय एजेंडा 21 बनाए।",
  f"{GE10} (Resources and Development).",
  "l1-env-rio-agenda-21-forest-principles", craft="recall")

M(IC, "medium", "The framework convention for the protection of the ozone layer, under which the Montreal Protocol was later adopted, is the",
  "ओज़ोन परत की रक्षा के लिए वह ढाँचागत अभिसमय (framework convention), जिसके तहत बाद में मॉन्ट्रियल प्रोटोकॉल अपनाया गया, कौन-सा है?",
  ["Vienna Convention (1985)", "Basel Convention (1989)", "Stockholm Convention (2001)", "Rotterdam Convention (1998)"],
  ["वियना अभिसमय (1985)", "बेसल अभिसमय (1989)", "स्टॉकहोम अभिसमय (2001)", "रॉटरडैम अभिसमय (1998)"],
  0,
  "The Vienna Convention for the Protection of the Ozone Layer (1985) set up a framework for cooperation and research without binding cuts; the Montreal Protocol (1987) under it laid down the controls on ozone-depleting substances. "
  "The Basel Convention deals with the transboundary movement of hazardous wastes, the Stockholm Convention with persistent organic pollutants and the Rotterdam Convention with prior informed consent for trade in certain hazardous chemicals.",
  "ओज़ोन परत की रक्षा के लिए वियना अभिसमय (1985) ने बाध्यकारी कटौती के बिना सहयोग और शोध का ढाँचा बनाया; इसके तहत मॉन्ट्रियल प्रोटोकॉल (1987) ने ओज़ोन-क्षयकारी पदार्थों पर नियंत्रण निर्धारित किए। "
  "बेसल अभिसमय ख़तरनाक अपशिष्टों के सीमापार आवागमन से, स्टॉकहोम अभिसमय स्थायी कार्बनिक प्रदूषकों से और रॉटरडैम अभिसमय कुछ ख़तरनाक रसायनों के व्यापार के लिए पूर्व सूचित सहमति से संबंधित है।",
  "United Nations Environment Programme (Ozone Secretariat).",
  "l1-env-vienna-convention-ozone", pos=3, craft="precision")

S(IC, "medium", "Consider the following statements about the history of resource conservation:",
  "संसाधन संरक्षण के इतिहास के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["In 1968 the Club of Rome advocated the conservation of resources in a more systematic way at the international level.",
   "E.F. Schumacher's book Small is Beautiful (1974) presented Gandhian ideas on conserving resources.",
   "Gandhiji held that resources were being depleted mainly because the poor consumed too much."],
  ["1968 में क्लब ऑफ़ रोम ने अंतरराष्ट्रीय स्तर पर अधिक व्यवस्थित ढंग से संसाधन संरक्षण की वकालत की।",
   "ई.एफ़. शूमाकर की पुस्तक 'स्मॉल इज़ ब्यूटीफ़ुल' (1974) ने संसाधन संरक्षण पर गांधीवादी विचार प्रस्तुत किए।",
   "गांधीजी मानते थे कि संसाधन मुख्यतः इसलिए घट रहे थे कि ग़रीब बहुत अधिक उपभोग करते थे।"],
  C3, 1,
  "Statements 1 and 2 are correct: international concern for conservation grew from the 1960s, leading to the Brundtland report and the Rio Summit. "
  "Statement 3 is wrong: Gandhiji placed the blame on greedy and selfish individuals and the exploitative nature of modern technology -- 'There is enough for everybody's need and not for anybody's greed' -- and wanted to replace mass production with production by the masses.",
  "कथन 1 और 2 सही हैं: संरक्षण के लिए अंतरराष्ट्रीय चिंता 1960 के दशक से बढ़ी, जो ब्रंटलैंड रिपोर्ट और रियो सम्मेलन तक पहुँची। "
  "कथन 3 गलत है: गांधीजी ने दोष लालची और स्वार्थी व्यक्तियों तथा आधुनिक प्रौद्योगिकी की शोषक प्रकृति पर रखा -- 'सबकी ज़रूरत के लिए पर्याप्त है, पर किसी के लालच के लिए नहीं' -- और वे बड़े पैमाने के उत्पादन के स्थान पर जनसाधारण द्वारा उत्पादन चाहते थे।",
  f"{GE10} (Resources and Development).",
  "l1-env-club-of-rome-schumacher-gandhi", craft="precision")

S(IC, "medium", "Consider the following statements about international days related to the environment:",
  "पर्यावरण से संबंधित अंतरराष्ट्रीय दिवसों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The International Day for Biological Diversity is observed on 22 May.",
   "The International Day of Forests is observed on 21 March.",
   "The International Day for the Preservation of the Ozone Layer is observed on 16 September.",
   "Earth Day is observed on 22 April."],
  ["अंतरराष्ट्रीय जैव-विविधता दिवस 22 मई को मनाया जाता है।",
   "अंतरराष्ट्रीय वन दिवस 21 मार्च को मनाया जाता है।",
   "अंतरराष्ट्रीय ओज़ोन परत संरक्षण दिवस 16 सितंबर को मनाया जाता है।",
   "पृथ्वी दिवस 22 अप्रैल को मनाया जाता है।"],
  C4, 3,
  "All four statements are correct. 22 May marks the adoption of the text of the Convention on Biological Diversity in 1992; 16 September marks the signing of the Montreal Protocol in 1987; the International Day of Forests was declared by the UN General Assembly in 2012; and Earth Day began in the United States in 1970 and is now observed worldwide. "
  "Such days are used by governments and the UN to draw public attention to particular environmental problems.",
  "चारों कथन सही हैं। 22 मई 1992 में जैव-विविधता अभिसमय का पाठ अपनाए जाने का दिन है; 16 सितंबर 1987 में मॉन्ट्रियल प्रोटोकॉल पर हस्ताक्षर का दिन है; अंतरराष्ट्रीय वन दिवस संयुक्त राष्ट्र महासभा ने 2012 में घोषित किया; और पृथ्वी दिवस 1970 में संयुक्त राज्य अमेरिका में शुरू होकर अब विश्व भर में मनाया जाता है। "
  "सरकारें और संयुक्त राष्ट्र ऐसे दिवसों का उपयोग विशेष पर्यावरणीय समस्याओं की ओर जनता का ध्यान खींचने के लिए करते हैं।",
  "United Nations (International Days); United Nations Environment Programme.",
  "l1-env-international-environment-days", craft="recall")

S(IC, "hard", "Consider the following statements about India at the UN Conference on the Human Environment, Stockholm, 1972:",
  "स्टॉकहोम में 1972 के मानव पर्यावरण पर संयुक्त राष्ट्र सम्मेलन में भारत के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Prime Minister Indira Gandhi addressed the conference, the only head of government apart from the host to attend.",
   "In her speech she linked poverty and environmental degradation, asking whether poverty and need were not the greatest polluters.",
   "The conference led directly to the creation of the Global Environment Facility."],
  ["प्रधानमंत्री इंदिरा गांधी ने सम्मेलन को संबोधित किया; मेज़बान के अलावा उसमें भाग लेने वाली वे एकमात्र शासनाध्यक्ष थीं।",
   "अपने भाषण में उन्होंने ग़रीबी और पर्यावरणीय क्षरण को जोड़ा और पूछा कि क्या ग़रीबी और अभाव ही सबसे बड़े प्रदूषक नहीं हैं।",
   "सम्मेलन से सीधे वैश्विक पर्यावरण सुविधा (GEF) की स्थापना हुई।"],
  C3, 1,
  "Statements 1 and 2 are correct. Indira Gandhi's speech put the concerns of developing countries at the centre of the environmental debate: environmental protection, she argued, could not be separated from the removal of poverty, and the developing world could not be asked to bear the costs of a problem created largely by industrialised countries. "
  "Statement 3 is wrong: the Stockholm conference led to the United Nations Environment Programme; the Global Environment Facility was set up only in 1991, on the eve of the Rio Earth Summit.",
  "कथन 1 और 2 सही हैं। इंदिरा गांधी के भाषण ने विकासशील देशों की चिंताओं को पर्यावरणीय बहस के केंद्र में रखा: उनका तर्क था कि पर्यावरण संरक्षण को ग़रीबी हटाने से अलग नहीं किया जा सकता, और विकासशील देशों से उस समस्या की लागत उठाने को नहीं कहा जा सकता जो मुख्यतः औद्योगिक देशों ने पैदा की। "
  "कथन 3 गलत है: स्टॉकहोम सम्मेलन से संयुक्त राष्ट्र पर्यावरण कार्यक्रम बना; वैश्विक पर्यावरण सुविधा की स्थापना 1991 में, रियो पृथ्वी सम्मेलन से ठीक पहले, हुई।",
  "Ministry of External Affairs; United Nations Environment Programme.",
  "l1-env-indira-stockholm-1972", craft="linkage")

write("env_l1_t3_e.sql")
