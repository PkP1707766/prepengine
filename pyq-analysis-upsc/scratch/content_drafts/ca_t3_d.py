# -*- coding: utf-8 -*-
"""Current Affairs · Test 3 (July to September 2026) -- part D: Environment and Ecology.

Framed as the 2025-26 papers frame environment news: each item names the issue (clearance after the fact, the
documentation of India's species, mining near wetland reserves, transmission for renewables, stubble burning, watching
forest fires from space, the trade in great apes) and asks what it is, why it matters and where the wording misleads.
No stem carries a date (design doc, section 7). Every fact was searched in the whole UPSC bank and is one no row
tests."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write, CODE
from polity_common import C3, C4, T2
from ca_common import MX, finish
from ca_t3_format import FORMAT, POS

d.SUBJECT = "Environment & Ecology"
d.REQUIRE_CRAFT = True
PA, IC, CM = "Protected Areas & Wildlife Protection", "International Conventions & Organisations", "Climate Science & Mitigation"
CA, FF, EP = "Climate Agreements & Carbon Markets", "Flora, Fungi & Forests", "Ecosystems & Ecological Processes"
PO = "Pollution & Waste Management"
CODE_HI = "नीचे दिए गए कूट का प्रयोग कर सही उत्तर चुनिए:"

A(EP, "hard",
  "The Supreme Court has quashed an office memorandum that allowed projects begun without environmental clearance to obtain it afterwards, without any cut-off date.",
  "सर्वोच्च न्यायालय ने वह कार्यालय ज्ञापन रद्द कर दिया है जो बिना पर्यावरणीय स्वीकृति के शुरू हुई परियोजनाओं को, बिना किसी अंतिम तिथि के, बाद में स्वीकृति लेने देता था।",
  "Environmental clearance is meant to assess a project's likely impacts before they occur, so that the project can be refused or modified in time.",
  "पर्यावरणीय स्वीकृति का उद्देश्य किसी परियोजना के संभावित प्रभावों का आकलन उनके घटित होने से पहले करना है, ताकि परियोजना समय रहते अस्वीकार या संशोधित की जा सके।",
  0,
  "Both statements are correct, and Statement II explains Statement I. Deciding the Vanashakti review in July 2026, the Court quashed, with prospective effect, the 2021 office memorandum that gave an open-ended route to regularise projects begun without clearance, and reaffirmed that prior clearance under the EIA Notification, 2006 is mandatory: an assessment made after the damage is done defeats the precautionary principle the clearance exists to serve. It upheld the 2017 notification only as a narrow, one-time window for violations that existed on 14 March 2017. "
  "The litigation had swung: a bench struck down both instruments in May 2025, and a larger bench recalled that judgment by 2:1 in November 2025 before the matter was decided afresh. The Court kept its own power under Article 142 to allow clearance after the fact in exceptional cases, and left the government free to frame a lawful mechanism, with safeguards, for legacy violations.",
  "दोनों कथन सही हैं, और कथन II कथन I की व्याख्या करता है। जुलाई 2026 में वनशक्ति पुनर्विलोकन पर निर्णय देते हुए न्यायालय ने 2021 का वह कार्यालय ज्ञापन, जिसने बिना स्वीकृति शुरू हुई परियोजनाओं को नियमित करने का खुला रास्ता दिया था, भावी प्रभाव से रद्द किया, और दोहराया कि ईआईए अधिसूचना, 2006 के अंतर्गत पूर्व स्वीकृति अनिवार्य है: क्षति हो जाने के बाद किया गया आकलन उस एहतियाती सिद्धांत को विफल करता है जिसके लिए स्वीकृति है। इसने 2017 की अधिसूचना को केवल 14 मार्च 2017 को विद्यमान उल्लंघनों के लिए एक संकीर्ण, एक-बारगी अवसर के रूप में बरकरार रखा। "
  "मुक़दमा उतार-चढ़ाव से गुज़रा: मई 2025 में एक पीठ ने दोनों को रद्द किया, और नवंबर 2025 में एक बड़ी पीठ ने 2:1 से वह निर्णय वापस लिया, जिसके बाद मामले पर नए सिरे से निर्णय हुआ। न्यायालय ने असाधारण मामलों में घटना-पश्चात स्वीकृति देने की अनुच्छेद 142 के अंतर्गत अपनी शक्ति बनाए रखी, और सरकार को पुराने उल्लंघनों के लिए सुरक्षा उपायों सहित वैध तंत्र बनाने के लिए स्वतंत्र छोड़ा।",
  "Supreme Court of India, Vanashakti v. Union of India, review judgment (July 2026); Ministry of Environment, Forest and Climate Change, EIA Notification, 2006.",
  "ca-t3-env-vanashakti-review-prior-ec-2021-om-art-142", craft="inference")

S(FF, "medium", "The Zoological Survey of India and the Botanical Survey of India publish yearly accounts of the species added to India's fauna and flora. Consider the following statements about the editions for 2025:",
  "भारतीय प्राणी सर्वेक्षण और भारतीय वनस्पति सर्वेक्षण भारत के प्राणिजात और वनस्पतिजात में जोड़ी गई प्रजातियों का वार्षिक लेखा प्रकाशित करते हैं। 2025 के संस्करणों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["All the 709 animals added to India's fauna in 2025 were species new to science.",
   "Kerala accounted for the largest number of the animal additions.",
   "Most of the 353 plant taxa added in 2025 were new distribution records for India rather than new to science."],
  ["2025 में भारत के प्राणिजात में जोड़े गए सभी 709 प्राणी विज्ञान के लिए नई प्रजातियाँ थे।",
   "प्राणी जोड़ों की सबसे बड़ी संख्या केरल से आई।",
   "2025 में जोड़े गए 353 पादप वर्गकों में अधिकांश विज्ञान के लिए नए होने के बजाय भारत के लिए नए वितरण अभिलेख थे।"],
  C3, 0,
  "Only statement 2 is correct. Kerala led with 98 additions, followed by West Bengal, Karnataka and Arunachal Pradesh, and the insect order Hymenoptera contributed the most; India's recorded fauna rose to 105,953 species. "
  "Statement 1 is wrong: of the 709, 483 were new to science and 226 were recorded in India for the first time, a distinction the reports keep because a 'new record' extends a known species' range while a 'new species' is described for the first time anywhere. Statement 3 is wrong: of the 353 plant taxa, 221 were new to science and 132 were new records, with Arunachal Pradesh, Uttarakhand and Kerala leading. Both surveys, based in Kolkata, are subordinate offices of the Ministry of Environment, Forest and Climate Change; the volumes were released on the ZSI's 111th Foundation Day.",
  "केवल कथन 2 सही है। 98 जोड़ों के साथ केरल आगे रहा, उसके बाद पश्चिम बंगाल, कर्नाटक और अरुणाचल प्रदेश, और कीट गण हाइमेनोप्टेरा ने सबसे अधिक योगदान दिया; भारत का अभिलिखित प्राणिजात बढ़कर 1,05,953 प्रजातियों का हो गया। "
  "कथन 1 ग़लत है: 709 में से 483 विज्ञान के लिए नए थे और 226 भारत में पहली बार दर्ज हुए, यह भेद रिपोर्टें इसलिए रखती हैं कि ‘नया अभिलेख’ किसी ज्ञात प्रजाति का क्षेत्र बढ़ाता है, जबकि ‘नई प्रजाति’ का वर्णन कहीं भी पहली बार होता है। कथन 3 ग़लत है: 353 पादप वर्गकों में से 221 विज्ञान के लिए नए और 132 नए अभिलेख थे, जिनमें अरुणाचल प्रदेश, उत्तराखंड और केरल आगे रहे। कोलकाता स्थित दोनों सर्वेक्षण पर्यावरण, वन और जलवायु परिवर्तन मंत्रालय के अधीनस्थ कार्यालय हैं; खंड भारतीय प्राणी सर्वेक्षण के 111वें स्थापना दिवस पर जारी हुए।",
  "Zoological Survey of India, Animal Discoveries 2025, and Botanical Survey of India, Plant Discoveries 2025 (July 2026); Ministry of Environment, Forest and Climate Change.",
  "ca-t3-env-animal-plant-discoveries-2025-kerala-new-records", craft="precision")

S(PA, "medium", "With reference to the protection of wetlands and reserves in India, consider the following statements:",
  "भारत में आर्द्रभूमियों और रिज़र्वों के संरक्षण के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Ramsar Convention prescribes a no-mining buffer of 10 km around every listed wetland.",
   "Conservation reserves and community reserves are categories of protected areas under the Wild Life (Protection) Act, 1972.",
   "The Supreme Court requires the prior permission of the Standing Committee of the National Board for Wildlife or the environment ministry for mining within 10 km of wetland and community conservation reserves."],
  ["रामसर अभिसमय हर सूचीबद्ध आर्द्रभूमि के चारों ओर 10 किमी का खनन-निषिद्ध बफ़र निर्धारित करता है।",
   "संरक्षण रिज़र्व और सामुदायिक रिज़र्व वन्यजीव (संरक्षण) अधिनियम, 1972 के अंतर्गत संरक्षित क्षेत्रों की श्रेणियाँ हैं।",
   "सर्वोच्च न्यायालय आर्द्रभूमि और सामुदायिक संरक्षण रिज़र्वों के 10 किमी के भीतर खनन के लिए राष्ट्रीय वन्यजीव बोर्ड की स्थायी समिति या पर्यावरण मंत्रालय की पूर्व अनुमति अपेक्षित करता है।"],
  C3, 1,
  "Statements 2 and 3 are correct. Conservation and community reserves were added to the Wild Life (Protection) Act by the 2002 amendment, for areas adjoining sanctuaries and parks or on community land. The Court laid down the 10-km rule in February 2024 for the Asan reserve on the Yamuna near Dehradun, Uttarakhand's first Ramsar site, and in August 2026 said that, for parity, it applies to similar reserves across the country. "
  "Statement 1 is wrong: neither the Ramsar Convention nor the Wetlands (Conservation and Management) Rules, 2017 fixes a buffer or bans mining at a set distance; the Convention relies on 'wise use' and on the measures of the listing country. That gap is why the protection had to come from a court order rather than from the treaty.",
  "कथन 2 और 3 सही हैं। संरक्षण और सामुदायिक रिज़र्व 2002 के संशोधन द्वारा वन्यजीव (संरक्षण) अधिनियम में जोड़े गए, अभयारण्यों और उद्यानों से सटे क्षेत्रों या सामुदायिक भूमि के लिए। न्यायालय ने फ़रवरी 2024 में देहरादून के पास यमुना पर स्थित आसन रिज़र्व, उत्तराखंड के पहले रामसर स्थल, के लिए 10 किमी का नियम बनाया, और अगस्त 2026 में कहा कि समानता के लिए यह देश भर के समान रिज़र्वों पर लागू होता है। "
  "कथन 1 ग़लत है: न तो रामसर अभिसमय और न आर्द्रभूमि (संरक्षण और प्रबंधन) नियम, 2017 कोई बफ़र तय करते हैं या निश्चित दूरी पर खनन पर रोक लगाते हैं; अभिसमय ‘विवेकपूर्ण उपयोग’ और सूचीबद्ध करने वाले देश के उपायों पर निर्भर है। इसी कमी के कारण संरक्षण संधि से नहीं, न्यायालय के आदेश से आना पड़ा।",
  "Supreme Court of India, orders on mining near the Asan Wetland Conservation Reserve (February 2024, clarified August 2026); Wild Life (Protection) Act, 1972, sections 36A and 36C; Wetlands (Conservation and Management) Rules, 2017.",
  "ca-t3-env-wetland-reserves-10-km-mining-ramsar-no-buffer", craft="precision")

S(CM, "medium", "India is building dedicated 'Green Energy Corridors' of transmission lines for renewable power, and has approved a third phase with an outlay of ₹1,86,405 crore. Which of the following explain why such corridors are needed?",
  "भारत नवीकरणीय बिजली के लिए पारेषण लाइनों के समर्पित ‘हरित ऊर्जा गलियारे’ बना रहा है, और ₹1,86,405 करोड़ के परिव्यय के साथ तीसरे चरण को स्वीकृति दी है। ऐसे गलियारों की आवश्यकता क्यों है, इसे निम्नलिखित में से कौन-से कारण स्पष्ट करते हैं?",
  ["The best wind and solar resources lie in a few States, often far from the main centres of demand.",
   "Without enough transmission capacity, renewable power has to be curtailed even when it is being generated.",
   "Power from renewable sources cannot be carried on the same lines as power from thermal plants."],
  ["सर्वोत्तम पवन और सौर संसाधन कुछ ही राज्यों में हैं, प्रायः माँग के मुख्य केंद्रों से दूर।",
   "पर्याप्त पारेषण क्षमता के बिना नवीकरणीय बिजली उत्पन्न होते हुए भी उसमें कटौती करनी पड़ती है।",
   "नवीकरणीय स्रोतों की बिजली ताप संयंत्रों की बिजली वाली लाइनों पर नहीं ले जाई जा सकती।"],
  C3, 1,
  "Statements 1 and 2 are correct. Solar and wind potential is concentrated in Rajasthan, Gujarat, the southern States and Ladakh, and generating capacity can be built in a year or two while lines take longer, so plants have been left waiting or curtailed for want of evacuation. The third phase, approved in September 2026, is meant to evacuate about 135 GW of renewable capacity by 2032-33; most of its outlay, about ₹1.36 lakh crore, strengthens the States' own networks, and it adds 50 GWh of battery storage at the generators' end, so that midday solar can be stored and released after sunset. "
  "Statement 3 is wrong: electricity is the same whatever its source, and renewable power flows on the common grid; the corridors are needed because of where the generation is and how much new capacity must be connected, not because of any difference in the power itself.",
  "कथन 1 और 2 सही हैं। सौर और पवन क्षमता राजस्थान, गुजरात, दक्षिणी राज्यों और लद्दाख में केंद्रित है, और उत्पादन क्षमता एक-दो वर्ष में बन जाती है जबकि लाइनों में अधिक समय लगता है, इसलिए निकासी के अभाव में संयंत्र प्रतीक्षा में रहे या उनमें कटौती हुई। सितंबर 2026 में स्वीकृत तीसरे चरण का उद्देश्य 2032-33 तक लगभग 135 गीगावाट नवीकरणीय क्षमता की निकासी है; इसके परिव्यय का अधिकांश, लगभग ₹1.36 लाख करोड़, राज्यों के अपने नेटवर्क को सुदृढ़ करता है, और यह उत्पादकों के छोर पर 50 गीगावाट-घंटे का बैटरी भंडारण जोड़ता है, ताकि दोपहर का सौर संचित कर सूर्यास्त के बाद दिया जा सके। "
  "कथन 3 ग़लत है: बिजली का स्रोत कोई भी हो, बिजली एक ही है, और नवीकरणीय बिजली साझा ग्रिड पर बहती है; गलियारों की आवश्यकता उत्पादन के स्थान और जोड़ी जाने वाली नई क्षमता की मात्रा के कारण है, बिजली में किसी अंतर के कारण नहीं।",
  "Cabinet decision and PIB, Green Energy Corridor Phase-III (30 September 2026); Ministry of Power and Ministry of New and Renewable Energy.",
  "ca-t3-env-gec-3-135-gw-50-gwh-generator-end", closing=CODE, closing_hi=CODE_HI, craft="application")

S(PO, "medium", "With reference to the measures against stubble burning in the National Capital Region and adjoining areas, consider the following statements:",
  "राष्ट्रीय राजधानी क्षेत्र और आसपास के क्षेत्रों में पराली जलाने के विरुद्ध उपायों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Draft rules provide for a 'red entry' in the land revenue records of a field where stubble is burnt.",
   "The environmental compensation payable rises with the size of the farmer's holding.",
   "The short gap between the paddy harvest and the sowing of wheat is one reason farmers burn the straw."],
  ["प्रारूप नियम उस खेत के भू-राजस्व अभिलेखों में ‘लाल प्रविष्टि’ का उपबंध करते हैं जहाँ पराली जलाई जाए।",
   "देय पर्यावरणीय क्षतिपूर्ति किसान की जोत के आकार के साथ बढ़ती है।",
   "धान की कटाई और गेहूँ की बुवाई के बीच का छोटा अंतराल किसानों के पुआल जलाने का एक कारण है।"],
  C3, 2,
  "All three statements are correct. The draft rules of September 2026, framed under the Commission for Air Quality Management Act, 2021, add a red entry that stays for 15 months and can be extended if burning continues or the compensation is unpaid, a record that follows the land rather than a one-time fine. Compensation is graded by holding, the smallest farmers paying least, and the rates were doubled in 2024 after the Supreme Court criticised weak enforcement. "
  "The burning has a structural cause: Punjab's Preservation of Subsoil Water Act, 2009 and Haryana's similar law delay paddy transplanting to save groundwater, which pushes the harvest into late October and leaves only two or three weeks to clear the fields for wheat; machines for in-situ management, ex-situ use in biomass and CBG plants, and shorter-duration varieties are the other answers.",
  "तीनों कथन सही हैं। वायु गुणवत्ता प्रबंधन आयोग अधिनियम, 2021 के अंतर्गत सितंबर 2026 के प्रारूप नियम एक लाल प्रविष्टि जोड़ते हैं जो 15 महीने रहती है और पराली जलाना जारी रहने या क्षतिपूर्ति न चुकाए जाने पर बढ़ाई जा सकती है, ऐसा अभिलेख जो एक-बारगी जुर्माने के बजाय भूमि के साथ चलता है। क्षतिपूर्ति जोत के अनुसार श्रेणीबद्ध है, सबसे छोटे किसान सबसे कम चुकाते हैं, और सर्वोच्च न्यायालय द्वारा कमज़ोर प्रवर्तन की आलोचना के बाद 2024 में दरें दोगुनी की गईं। "
  "पराली जलाने का एक संरचनात्मक कारण है: पंजाब का उप-भूमि जल संरक्षण अधिनियम, 2009 और हरियाणा का ऐसा ही कानून भूजल बचाने के लिए धान की रोपाई देर से कराते हैं, जिससे कटाई अक्टूबर के अंत तक खिसकती है और गेहूँ के लिए खेत साफ़ करने को केवल दो-तीन सप्ताह बचते हैं; स्व-स्थाने प्रबंधन की मशीनें, बायोमास और सीबीजी संयंत्रों में बाह्य-स्थाने उपयोग, और कम अवधि की किस्में अन्य उत्तर हैं।",
  "Ministry of Environment, Forest and Climate Change, draft rules on environmental compensation for stubble burning (September 2026); Commission for Air Quality Management in National Capital Region and Adjoining Areas Act, 2021; Punjab Preservation of Subsoil Water Act, 2009.",
  "ca-t3-env-stubble-red-entry-15-months-ncr", craft="linkage")

S(FF, "hard", "Forest fires in India are detected mostly from polar-orbiting satellites, and a parliamentary committee has recommended a dedicated geostationary satellite for the purpose. Which of the following explain the recommendation?",
  "भारत में वनाग्नि का पता मुख्यतः ध्रुवीय कक्षा वाले उपग्रहों से लगाया जाता है, और एक संसदीय समिति ने इसके लिए एक समर्पित भूस्थिर उपग्रह की सिफ़ारिश की है। निम्नलिखित में से कौन-से कथन इस सिफ़ारिश की व्याख्या करते हैं?",
  ["A polar-orbiting satellite passes over a given place only a few times a day, so a fire can spread unseen between passes.",
   "A geostationary satellite stays above the same region and can watch it continuously.",
   "Geostationary satellites orbit much closer to the Earth than polar-orbiting satellites, so they give finer images."],
  ["ध्रुवीय कक्षा वाला उपग्रह किसी स्थान के ऊपर से दिन में केवल कुछ बार गुज़रता है, इसलिए दो गुज़रों के बीच आग बिना दिखे फैल सकती है।",
   "भूस्थिर उपग्रह उसी क्षेत्र के ऊपर बना रहता है और उस पर लगातार नज़र रख सकता है।",
   "भूस्थिर उपग्रह ध्रुवीय कक्षा वाले उपग्रहों से पृथ्वी के बहुत निकट परिक्रमा करते हैं, इसलिए वे अधिक बारीक चित्र देते हैं।"],
  C3, 1,
  "Statements 1 and 2 are correct. A geostationary satellite circles above the equator at the Earth's rate of rotation and so appears fixed over one region, giving continuous coverage; polar-orbiting satellites such as those carrying the MODIS and VIIRS sensors, on which the Forest Survey of India's fire alerts largely rely, see a place only a few times a day. The Rajya Sabha committee on science, environment and forests, reporting in August 2026, noted that the Western and Eastern Himalaya, about 17 per cent of India's land, saw about 57 per cent of its fire incidents, and also urged that forest fire be notified as a disaster under the Disaster Management Act, 2005. "
  "Statement 3 is wrong: geostationary satellites are about 36,000 km up, while polar-orbiting ones are a few hundred kilometres up; their images are coarser, and their value lies in watching constantly, not in seeing finely.",
  "कथन 1 और 2 सही हैं। भूस्थिर उपग्रह भूमध्य रेखा के ऊपर पृथ्वी के घूर्णन की दर से परिक्रमा करता है और इसलिए एक क्षेत्र के ऊपर स्थिर दिखता है, जिससे लगातार कवरेज मिलती है; मोडिस और वीआईआईआरएस संवेदकों वाले ध्रुवीय कक्षा के उपग्रह, जिन पर भारतीय वन सर्वेक्षण की अग्नि-चेतावनियाँ बहुत हद तक टिकी हैं, किसी स्थान को दिन में कुछ ही बार देखते हैं। अगस्त 2026 में रिपोर्ट देने वाली विज्ञान, पर्यावरण और वन संबंधी राज्यसभा समिति ने पाया कि भारत की लगभग 17 प्रतिशत भूमि वाले पश्चिमी और पूर्वी हिमालय में लगभग 57 प्रतिशत आग की घटनाएँ हुईं, और यह आग्रह भी किया कि वनाग्नि को आपदा प्रबंधन अधिनियम, 2005 के अंतर्गत आपदा अधिसूचित किया जाए। "
  "कथन 3 ग़लत है: भूस्थिर उपग्रह लगभग 36,000 किमी ऊपर हैं, जबकि ध्रुवीय कक्षा वाले कुछ सौ किलोमीटर ऊपर; उनके चित्र मोटे होते हैं, और उनका मूल्य बारीक देखने में नहीं, लगातार देखने में है।",
  "Department-related Parliamentary Standing Committee on Science and Technology, Environment, Forests and Climate Change, report on forest fires in the Himalayan region (August 2026); Forest Survey of India, forest fire alert system.",
  "ca-t3-env-himalayan-forest-fires-geostationary-dm-act", closing=CODE, closing_hi=CODE_HI, craft="inference")

S(PA, "easy", "Five baby orangutans, smuggled into India, were rescued from a forest in Odisha. Consider the following statements about orangutans:",
  "भारत में तस्करी कर लाए गए पाँच शिशु ओरांगुटान ओडिशा के एक जंगल से बचाए गए। ओरांगुटान के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["They occur naturally in the forests of north-east India.",
   "They are listed as Least Concern on the IUCN Red List.",
   "They are monkeys of the same genus as the rhesus macaque."],
  ["ये प्राकृतिक रूप से पूर्वोत्तर भारत के वनों में पाए जाते हैं।",
   "ये आईयूसीएन रेड लिस्ट में ‘कम चिंतनीय’ के रूप में सूचीबद्ध हैं।",
   "ये रीसस मकाक के ही वंश के बंदर हैं।"],
  C3, 3,
  "None of the statements is correct. Orangutans are great apes of the genus Pongo, found in the wild only on Borneo and Sumatra; all three species are Critically Endangered, and their international trade is banned under Appendix I of CITES. "
  "Since the animals could not have reached Odisha on their own, they were moved to the Nandankanan zoo while the Wildlife Crime Control Bureau and the State police investigated the smuggling route, and Indonesia sought their return; exotic animals held in India must be declared and registered under the Wild Life (Protection) Act as amended in 2022, which brought CITES-listed species into its schedules.",
  "कोई भी कथन सही नहीं है। ओरांगुटान पोंगो वंश के बड़े कपि हैं, जो प्राकृतिक रूप से केवल बोर्नियो और सुमात्रा पर पाए जाते हैं; तीनों प्रजातियाँ ‘गंभीर रूप से संकटग्रस्त’ हैं, और साइटीज़ के परिशिष्ट I के अंतर्गत उनका अंतरराष्ट्रीय व्यापार प्रतिबंधित है। "
  "चूँकि पशु अपने-आप ओडिशा नहीं पहुँच सकते थे, उन्हें नंदनकानन चिड़ियाघर ले जाया गया जबकि वन्यजीव अपराध नियंत्रण ब्यूरो और राज्य पुलिस ने तस्करी के मार्ग की जाँच की, और इंडोनेशिया ने उनकी वापसी माँगी; भारत में रखे विदेशी पशुओं की घोषणा और पंजीकरण 2022 में संशोधित वन्यजीव (संरक्षण) अधिनियम के अंतर्गत आवश्यक है, जिसने साइटीज़-सूचीबद्ध प्रजातियों को अपनी अनुसूचियों में लाया।",
  "Government of Odisha, Forest and Environment Department, rescue of orangutans in Balasore (September 2026); IUCN Red List; CITES Appendix I; Wild Life (Protection) Amendment Act, 2022.",
  "ca-t3-env-orangutans-balasore-pongo-critically-endangered", craft="precision")

finish("ca_t3_d.sql", FORMAT, "2026-Q3", update="--update" in sys.argv)
