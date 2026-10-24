# -*- coding: utf-8 -*-
"""Level 3 · Test 6 (GS Integrated Test 6) -- part C: Environment & Ecology (15) (upsc_l3_cell_targets.mjs 6).
Same cell plan as Tests 1-5.
Every fact was searched in the whole UPSC bank (l3_tools/bank_find.py) and is one no row tests: mycoheterotrophic
plants; Senna spectabilis in the Nilgiri Biosphere Reserve; musth; India's honeybee species; the kiang; ghost nets;
faecal sludge and septage management; the drought outcome of UNCCD COP16 at Riyadh; the T.S.R. Subramanian committee, the Tiger Task
Force, the Gadgil panel and the Kasturirangan working group; SSP scenario labels; climate feedbacks; Important Bird
and Biodiversity Areas; great Indian bustard conservation breeding; freshwater bioindicators; China's national ETS.
MCQ keys are pinned (pos)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Environment & Ecology"
d.REQUIRE_CRAFT = True
BIO12 = "NCERT Class XII, Biology (Organisms and Populations; Ecosystem; Biodiversity and Conservation)"
MOEF = "Ministry of Environment, Forest and Climate Change"
WII = "Wildlife Institute of India"
IPCC = "IPCC Sixth Assessment Report"

# ---------------------------------------------------------------- Flora, Fungi & Forests (e-MCQ, m-stmt)
M("Flora, Fungi & Forests", "easy",
  "Some flowering plants, such as the 'ghost plant' (Monotropa), have no chlorophyll at all. They obtain their food mainly by:",
  "कुछ पुष्पी पौधों, जैसे ‘घोस्ट प्लांट’ (मोनोट्रोपा), में पर्णहरित बिल्कुल नहीं होता। वे अपना भोजन मुख्यतः कैसे प्राप्त करते हैं?",
  ["drawing on fungi that are linked to the roots of green plants",
   "photosynthesising with red and purple pigments in place of chlorophyll",
   "trapping and digesting small insects caught in the sticky hairs on their leaves",
   "absorbing carbon dioxide at night and storing it as organic acids"],
  ["उन कवकों से भोजन लेकर जो स्वयं हरे पौधों की जड़ों से जुड़े होते हैं",
   "पर्णहरित के स्थान पर लाल और बैंगनी वर्णकों से प्रकाश-संश्लेषण करके",
   "पत्तियों के चिपचिपे रोमों में छोटे कीटों को फँसाकर और पचाकर",
   "रात में कार्बन डाइऑक्साइड सोखकर उसे कार्बनिक अम्लों के रूप में संग्रहीत करके"],
  0,
  "Such plants are mycoheterotrophs. Their roots join the underground network of mycorrhizal fungi, which in turn are connected to nearby trees; sugars made by the trees pass into the fungi, and the ghost plant draws its carbon from the fungi -- in effect, an indirect parasite of the trees. Being free of the need for light, many grow in the deep shade of forest floors, appearing as white or pale pink stems, and they flower only briefly. "
  "The other options describe different strategies: insectivorous plants trap insects to supplement nitrogen while still photosynthesising; CAM plants open their stomata at night to save water; and red-leaved plants still rely on chlorophyll masked by other pigments. Mycoheterotrophs show how much of a forest's life depends on the hidden fungal network.",
  "ऐसे पौधे कवकपोषी (माइकोहेटेरोट्रॉफ़) हैं। इनकी जड़ें कवकमूलीय कवकों के भूमिगत जाल से जुड़ती हैं, जो स्वयं पास के वृक्षों से जुड़े होते हैं; वृक्षों द्वारा बनाई गई शर्कराएँ कवकों में जाती हैं, और घोस्ट प्लांट कवकों से अपना कार्बन लेता है -- वस्तुतः वृक्षों का अप्रत्यक्ष परजीवी। प्रकाश की आवश्यकता न होने से अनेक ऐसे पौधे वन-तल की गहरी छाया में सफ़ेद या हल्के गुलाबी तनों के रूप में उगते हैं, और थोड़े समय के लिए ही फूलते हैं। "
  "अन्य विकल्प भिन्न रणनीतियों का वर्णन करते हैं: कीटभक्षी पौधे प्रकाश-संश्लेषण करते हुए भी नाइट्रोजन की पूर्ति के लिए कीट फँसाते हैं; सीएएम पौधे पानी बचाने के लिए रात में रंध्र खोलते हैं; और लाल पत्तियों वाले पौधे अन्य वर्णकों से ढके पर्णहरित पर ही निर्भर रहते हैं। कवकपोषी पौधे दिखाते हैं कि वन का कितना जीवन छिपे कवक-जाल पर निर्भर है।",
  BIO12 + "; Botanical Survey of India.", "l3-t6-env-mycoheterotroph-ghost-plant", pos=2, craft="inference")

S("Flora, Fungi & Forests", "medium", "With reference to Senna spectabilis in the forests of southern India, consider the following statements:",
  "दक्षिण भारत के वनों में सेन्ना स्पेक्टेबिलिस के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is a tree native to tropical America that has become invasive in the Nilgiri Biosphere Reserve.",
   "By shading out native grasses and undergrowth, it reduces the fodder available to elephants, gaur and deer.",
   "It was introduced into the region as an ornamental and a source of firewood."],
  ["यह उष्णकटिबंधीय अमेरिका का मूल निवासी वृक्ष है जो नीलगिरि जैवमंडल आरक्षित क्षेत्र में आक्रामक बन गया है।",
   "देशी घासों और झाड़ियों को छाया से दबाकर यह हाथियों, गौर और हिरणों के लिए उपलब्ध चारा घटाता है।",
   "इसे इस क्षेत्र में शोभा के पौधे और जलावन लकड़ी के स्रोत के रूप में लाया गया था।"],
  C3, 2,
  "All three are correct. Senna spectabilis, a fast-growing tree with showy yellow flowers, was planted in Wayanad and nearby areas in the 1980s for ornament and firewood; it seeds prolifically, coppices when cut and forms dense stands, and has spread through Wayanad, Mudumalai, Bandipur and Nagarhole -- the core of the Nilgiri Biosphere Reserve, home to Asia's largest population of wild elephants. "
  "Beneath it the grassland and shrubs that herbivores depend on disappear, which pushes elephants out towards farms and adds to conflict. Clearing it is difficult because uprooting disturbs the soil and the seed bank can regenerate for years, so forest departments have tried girdling, uprooting before seeding and, more recently, putting the wood to commercial use. Along with Lantana, it is now treated as one of the most serious threats to the reserve's grasslands.",
  "तीनों कथन सही हैं। आकर्षक पीले फूलों वाला तेज़ी से बढ़ने वाला वृक्ष सेन्ना स्पेक्टेबिलिस 1980 के दशक में वायनाड और आसपास शोभा और जलावन के लिए लगाया गया; यह बहुत बीज देता है, काटने पर फिर उग आता है और घने झुरमुट बनाता है, और वायनाड, मुदुमलाई, बांदीपुर और नागरहोल -- नीलगिरि जैवमंडल आरक्षित क्षेत्र का मूल भाग, जहाँ एशिया की सबसे बड़ी जंगली हाथी आबादी है -- में फैल गया है। "
  "इसके नीचे वह घास और झाड़ियाँ समाप्त हो जाती हैं जिन पर शाकाहारी निर्भर हैं, जिससे हाथी खेतों की ओर जाते हैं और संघर्ष बढ़ता है। इसे हटाना कठिन है क्योंकि उखाड़ने से मिट्टी अशांत होती है और बीज-भंडार वर्षों तक पुनर्जीवित हो सकता है, इसलिए वन विभागों ने छाल-छल्ला काटने, बीज बनने से पहले उखाड़ने और हाल में लकड़ी के व्यावसायिक उपयोग के उपाय आज़माए हैं। लैंटाना के साथ अब इसे आरक्षित क्षेत्र की घासभूमियों के लिए सबसे गंभीर ख़तरों में गिना जाता है।",
  MOEF + "; Kerala Forest Research Institute; Tamil Nadu Forest Department.", "l3-t6-env-senna-spectabilis-nilgiris", craft="linkage")

# ---------------------------------------------------------------- Fauna & Animal Behaviour (e-stmt, h-stmt, m-stmt)
S("Fauna & Animal Behaviour", "easy", "With reference to 'musth' in elephants, consider the following statements:",
  "हाथियों में ‘मस्त’ (मस्थ) के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is a periodic condition of adult bull elephants marked by a sharp rise in testosterone and by aggression.",
   "A bull in musth secretes a dark fluid from the temporal glands between the eye and the ear.",
   "It occurs only in female elephants, during pregnancy."],
  ["यह वयस्क नर हाथियों की एक आवधिक अवस्था है जिसमें टेस्टोस्टेरोन तेज़ी से बढ़ता है और आक्रामकता आती है।",
   "मस्त में आया नर आँख और कान के बीच स्थित शंख-ग्रंथियों से गहरा द्रव स्रावित करता है।",
   "यह केवल मादा हाथियों में, गर्भावस्था के दौरान होता है।"],
  C3, 1,
  "Statements 1 and 2 are correct. Musth recurs roughly once a year in mature bulls and can last weeks; testosterone may rise many times above normal, the temporal glands stream a strong-smelling secretion, and the bull dribbles urine, rumbles and becomes restless and aggressive. Bulls in musth range widely in search of females and usually win contests against larger bulls that are not in musth, so the condition plays a part in mating. "
  "Statement 3 is wrong: musth is a condition of males. It matters for management, because captive bulls in musth are dangerous to handlers, and bulls in musth raiding crops are behind some of the most serious incidents of human-elephant conflict.",
  "कथन 1 और 2 सही हैं। परिपक्व नरों में मस्त लगभग वर्ष में एक बार आता है और सप्ताहों तक चल सकता है; टेस्टोस्टेरोन सामान्य से कई गुना बढ़ सकता है, शंख-ग्रंथियों से तेज़ गंध वाला स्राव बहता है, और नर मूत्र टपकाता, गुर्राता तथा बेचैन और आक्रामक हो जाता है। मस्त में आए नर मादाओं की खोज में दूर तक घूमते हैं और सामान्यतः उन बड़े नरों से भी मुक़ाबला जीत लेते हैं जो मस्त में नहीं हैं, इसलिए इस अवस्था की प्रजनन में भूमिका है। "
  "कथन 3 ग़लत है: मस्त नरों की अवस्था है। यह प्रबंधन के लिए महत्वपूर्ण है, क्योंकि मस्त में आए बंदी नर महावतों के लिए ख़तरनाक होते हैं, और फ़सल पर धावा बोलने वाले मस्त नर मानव-हाथी संघर्ष की कुछ सबसे गंभीर घटनाओं के पीछे होते हैं।",
  WII + "; " + MOEF + " (Project Elephant).", "l3-t6-env-elephant-musth", craft="recall")

S("Fauna & Animal Behaviour", "hard", "With reference to the honeybees of India, consider the following statements:",
  "भारत की मधुमक्खियों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["The rock bee (Apis dorsata) builds a single large comb in the open, on cliffs, tall trees and buildings.",
   "The Indian hive bee (Apis cerana) nests in cavities with several parallel combs and can be kept in boxes.",
   "The little bee (Apis florea) builds a small single comb around a twig in bushes.",
   "Apis mellifera, the bee most widely used in commercial beekeeping in India, is native to the country."],
  ["शैल मधुमक्खी (एपिस डोरसाटा) खुले में, चट्टानों, ऊँचे वृक्षों और इमारतों पर, एक बड़ा अकेला छत्ता बनाती है।",
   "भारतीय मौन मधुमक्खी (एपिस सेराना) अनेक समांतर छत्तों के साथ खोखली जगहों में घोंसला बनाती है और उसे बक्सों में पाला जा सकता है।",
   "लघु मधुमक्खी (एपिस फ़्लोरिया) झाड़ियों में एक टहनी के चारों ओर एक छोटा अकेला छत्ता बनाती है।",
   "भारत में व्यावसायिक मधुमक्खी पालन में सबसे अधिक प्रयुक्त एपिस मेलिफ़ेरा देश की मूल निवासी है।"],
  C4, 2,
  "Statements 1, 2 and 3 are correct. India has three native honeybees of the genus Apis. The giant rock bee, aggressive and migratory, cannot be kept in boxes; much 'wild honey' sold in India comes from its combs, harvested by forest communities. The Asiatic hive bee builds multiple combs in tree hollows, wall cavities or boxes and has been the traditional bee of Indian beekeeping, while the small dwarf bee yields little honey but is an important pollinator in drier areas. "
  "Statement 4 is wrong: Apis mellifera, the western honeybee, was introduced from Europe -- first successfully in Punjab and Himachal Pradesh in the 1960s and 1970s -- because it yields more and is calmer, and it now dominates commercial production under schemes such as the National Beekeeping and Honey Mission. Its spread raises concerns about diseases and competition with native bees, which are often better adapted to local flowers and climate.",
  "कथन 1, 2 और 3 सही हैं। भारत में एपिस वंश की तीन देशी मधुमक्खियाँ हैं। आक्रामक और प्रवासी विशाल शैल मधुमक्खी बक्सों में नहीं पाली जा सकती; भारत में बिकने वाला बहुत सा ‘जंगली शहद’ उसके छत्तों से आता है, जिसे वन समुदाय निकालते हैं। एशियाई मौन मधुमक्खी पेड़ के खोखलों, दीवारों की दरारों या बक्सों में अनेक छत्ते बनाती है और भारतीय मधुमक्खी पालन की पारंपरिक मधुमक्खी रही है, जबकि छोटी बौनी मधुमक्खी कम शहद देती है पर शुष्क क्षेत्रों में एक महत्वपूर्ण परागणकर्ता है। "
  "कथन 4 ग़लत है: पश्चिमी मधुमक्खी एपिस मेलिफ़ेरा यूरोप से लाई गई -- पहली बार सफलतापूर्वक 1960 और 1970 के दशकों में पंजाब और हिमाचल प्रदेश में -- क्योंकि यह अधिक शहद देती है और शांत है, और अब राष्ट्रीय मधुमक्खी पालन और शहद मिशन जैसी योजनाओं के अंतर्गत व्यावसायिक उत्पादन पर इसी का प्रभुत्व है। इसके प्रसार से रोगों और देशी मधुमक्खियों से प्रतिस्पर्धा की चिंता उठती है, जो प्रायः स्थानीय फूलों और जलवायु के अधिक अनुकूल होती हैं।",
  "Ministry of Agriculture and Farmers Welfare, National Beekeeping and Honey Mission; Zoological Survey of India.",
  "l3-t6-env-honeybee-species-india", craft="precision")

S("Fauna & Animal Behaviour", "medium", "With reference to the kiang, consider the following statements:",
  "कियांग के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["The kiang, the largest of the wild asses, lives on the high plateaus of Ladakh and northern Sikkim.",
   "It belongs to the same species as the Indian wild ass of the Little Rann of Kutch."],
  ["कियांग, जंगली गधों में सबसे बड़ा, लद्दाख और उत्तरी सिक्किम के ऊँचे पठारों पर रहता है।",
   "यह कच्छ के छोटे रण के भारतीय जंगली गधे की ही प्रजाति का है।"],
  T2, 0,
  "Only statement 1 is correct. The kiang (Equus kiang) is a Tibetan-plateau animal that, in India, grazes the cold-desert grasslands of Changthang in eastern Ladakh and the high plateau of northern Sikkim at 4,000-5,000 metres; it lives in herds that follow the summer growth of sedges and grasses, and its numbers have at times put it in competition with the pashmina goats and sheep of Changpa herders. "
  "Statement 2 is wrong: the Indian wild ass, or khur, is a subspecies of a different species, Equus hemionus, adapted to the hot, saline flats of the Rann. The two animals, separated by the whole width of north India, show how a single genus has adapted to opposite extremes of cold and heat.",
  "केवल कथन 1 सही है। कियांग (इक्वस कियांग) तिब्बती पठार का जंतु है, जो भारत में पूर्वी लद्दाख के चांगथांग की शीत-मरुस्थलीय घासभूमियों और उत्तरी सिक्किम के ऊँचे पठार पर 4,000-5,000 मीटर की ऊँचाई पर चरता है; यह झुंडों में रहता है जो सेज और घासों की गर्मियों की बढ़त का पीछा करते हैं, और इसकी संख्या कभी-कभी चांगपा चरवाहों की पश्मीना बकरियों और भेड़ों से प्रतिस्पर्धा में आ जाती है। "
  "कथन 2 ग़लत है: भारतीय जंगली गधा, या खुर, एक भिन्न प्रजाति, इक्वस हेमिओनस, की उपप्रजाति है, जो रण के गर्म, लवणीय मैदानों के अनुकूल है। पूरे उत्तर भारत की चौड़ाई से अलग ये दोनों जंतु दिखाते हैं कि एक ही वंश ने ठंड और गर्मी की विपरीत चरम स्थितियों के अनुसार स्वयं को कैसे ढाला।",
  WII + "; Zoological Survey of India.", "l3-t6-env-kiang-ladakh-sikkim", craft="precision")

# ---------------------------------------------------------------- Pollution, Waste & Resources (e-stmt, m-stmt)
S("Pollution, Waste & Resources", "easy", "With reference to 'ghost nets', consider the following statements:",
  "‘घोस्ट नेट’ (प्रेत जाल) के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["They are fishing nets lost, abandoned or discarded at sea that go on trapping marine animals.",
   "Because they are made of natural fibres, they break down harmlessly within a few months."],
  ["ये समुद्र में खोए, छोड़े या फेंके गए मछली पकड़ने के जाल हैं जो समुद्री जीवों को फँसाते रहते हैं।",
   "प्राकृतिक रेशों से बने होने के कारण ये कुछ महीनों में बिना हानि के नष्ट हो जाते हैं।"],
  T2, 0,
  "Only statement 1 is correct. Nets and other gear lost in storms, snagged on reefs or dumped at sea keep 'fishing' for years, entangling turtles, dolphins, dugongs, sharks and seabirds, smothering corals and adding to the debris that washes up on beaches, as on India's Lakshadweep and Andaman coasts. Studies of the Great Pacific Garbage Patch have found that fishing gear makes up a large share of its larger plastic debris by weight. "
  "Statement 2 is wrong: modern nets are made of nylon and other synthetic polymers that persist for decades and break into microplastics. Remedies include marking gear so it can be traced, buy-back and recycling schemes for old nets, and recovery drives by fishing communities.",
  "केवल कथन 1 सही है। तूफ़ानों में खोए, चट्टानों में फँसे या समुद्र में फेंके गए जाल और अन्य उपकरण वर्षों तक ‘मछली पकड़ते’ रहते हैं, कछुओं, डॉल्फ़िनों, डुगोंग, शार्कों और समुद्री पक्षियों को उलझाते हैं, प्रवालों को ढक देते हैं और उस मलबे को बढ़ाते हैं जो तटों पर आता है, जैसे भारत के लक्षद्वीप और अंडमान तटों पर। ग्रेट पैसिफ़िक गार्बेज पैच के अध्ययनों में पाया गया है कि भार के हिसाब से उसके बड़े प्लास्टिक मलबे का बड़ा भाग मछली पकड़ने के उपकरण हैं। "
  "कथन 2 ग़लत है: आधुनिक जाल नायलॉन और अन्य संश्लेषित बहुलकों से बने होते हैं जो दशकों तक बने रहते हैं और सूक्ष्म-प्लास्टिक में टूट जाते हैं। उपायों में उपकरणों पर पहचान चिह्न लगाना, पुराने जालों की वापसी-ख़रीद और पुनर्चक्रण योजनाएँ, और मछुआरा समुदायों के संग्रह अभियान शामिल हैं।",
  "Food and Agriculture Organization, abandoned, lost or otherwise discarded fishing gear; " + MOEF + ".",
  "l3-t6-env-ghost-nets", craft="recall")

S("Pollution, Waste & Resources", "medium", "With reference to faecal sludge and septage management in urban India, consider the following statements:",
  "शहरी भारत में मल-कीचड़ और सेप्टेज प्रबंधन के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["A majority of urban households with toilets depend on on-site systems such as septic tanks and pits rather than on sewers.",
   "The National Policy on Faecal Sludge and Septage Management, 2017 aims at the safe collection, transport, treatment and reuse of sludge from such systems.",
   "Septic tanks never need to be emptied, because the sludge in them decomposes completely."],
  ["शौचालय वाले अधिकांश शहरी परिवार सीवर के बजाय सेप्टिक टैंक और गड्ढों जैसी स्थल-आधारित प्रणालियों पर निर्भर हैं।",
   "मल-कीचड़ और सेप्टेज प्रबंधन पर राष्ट्रीय नीति, 2017 का उद्देश्य ऐसी प्रणालियों से निकले कीचड़ का सुरक्षित संग्रह, परिवहन, उपचार और पुनः उपयोग है।",
   "सेप्टिक टैंकों को कभी ख़ाली करने की आवश्यकता नहीं होती, क्योंकि उनमें कीचड़ पूरी तरह विघटित हो जाता है।"],
  C3, 1,
  "Statements 1 and 2 are correct. Sewer networks reach only a part of India's towns, so the toilets built under the Swachh Bharat Mission mostly drain into septic tanks and pits; the solid sludge that collects in them has to be pumped out and, too often, is dumped untreated into drains, fields and rivers, undoing much of the health gain from building toilets. The 2017 policy, and the Swachh Bharat Mission (Urban) 2.0, therefore push towns to schedule desludging, license vacuum-tanker operators and set up faecal sludge treatment plants, or treat sludge at sewage treatment plants. "
  "Statement 3 is wrong: a septic tank only settles solids and partly digests them; the accumulated sludge must be removed every few years, or the tank overflows and the outflow carries pathogens. Mechanised desludging also matters for dignity and safety, since deaths of workers cleaning tanks by hand remain a grave problem.",
  "कथन 1 और 2 सही हैं। सीवर तंत्र भारत के नगरों के केवल एक भाग तक पहुँचता है, इसलिए स्वच्छ भारत मिशन के अंतर्गत बने शौचालय अधिकतर सेप्टिक टैंकों और गड्ढों में खुलते हैं; उनमें जमा ठोस कीचड़ को पंप से निकालना पड़ता है और प्रायः उसे बिना उपचार के नालों, खेतों और नदियों में डाल दिया जाता है, जिससे शौचालय बनाने से हुआ स्वास्थ्य लाभ काफ़ी हद तक नष्ट हो जाता है। इसलिए 2017 की नीति और स्वच्छ भारत मिशन (शहरी) 2.0 नगरों से समय-सारणी के अनुसार कीचड़ निकलवाने, वैक्यूम-टैंकर संचालकों को लाइसेंस देने और मल-कीचड़ उपचार संयंत्र बनाने, या कीचड़ को सीवेज उपचार संयंत्रों में उपचारित करने को कहते हैं। "
  "कथन 3 ग़लत है: सेप्टिक टैंक केवल ठोस पदार्थ नीचे बैठाता और आंशिक रूप से पचाता है; जमा कीचड़ को हर कुछ वर्षों में निकालना ही होता है, वरना टैंक उफनता है और बहिःस्राव रोगाणु ले जाता है। यंत्रीकृत सफ़ाई गरिमा और सुरक्षा के लिए भी महत्वपूर्ण है, क्योंकि हाथ से टैंक साफ़ करते श्रमिकों की मौतें एक गंभीर समस्या बनी हुई हैं।",
  "Ministry of Housing and Urban Affairs, National Policy on Faecal Sludge and Septage Management (2017) and Swachh Bharat Mission (Urban) 2.0.",
  "l3-t6-env-faecal-sludge-septage", craft="application")

# ---------------------------------------------------------------- International Conventions & Organisations (h-SI)
A("International Conventions & Organisations", "hard",
  "The sixteenth Conference of the Parties to the UN Convention to Combat Desertification, held at Riyadh in 2024, ended without adopting a legally binding protocol on drought.",
  "2024 में रियाद में हुआ मरुस्थलीकरण से निपटने के संयुक्त राष्ट्र अभिसमय के पक्षकारों का सोलहवाँ सम्मेलन सूखे पर क़ानूनी रूप से बाध्यकारी प्रोटोकॉल अपनाए बिना समाप्त हुआ।",
  "The Parties were divided over whether a new drought regime should take the form of a binding protocol or of a non-binding framework.",
  "पक्षकार इस पर बँटे रहे कि सूखे की नई व्यवस्था बाध्यकारी प्रोटोकॉल के रूप में हो या ग़ैर-बाध्यकारी ढाँचे के रूप में।",
  0,
  "Both statements are correct and Statement II explains Statement I. Drought was the headline issue at the first UNCCD COP held in the Middle East: many African countries and Indigenous groups sought a protocol with binding obligations on preparedness and response, while several developed and some other countries preferred a framework that would leave such measures voluntary. With no consensus after an extended session, the decision was deferred to the next conference. "
  "The meeting did launch the Riyadh Global Drought Resilience Partnership, with pledges for drought-prone countries, and reaffirmed the target of restoring degraded land by 2030. For India, which has set itself a target of restoring 26 million hectares of degraded land by 2030 and which hosted COP14 in 2019, drought resilience links land, water and food security.",
  "दोनों कथन सही हैं और कथन II, कथन I की व्याख्या करता है। मध्य पूर्व में हुए यूएनसीसीडी के पहले सम्मेलन का मुख्य विषय सूखा था: अनेक अफ़्रीकी देश और मूलनिवासी समूह तैयारी और प्रतिक्रिया पर बाध्यकारी दायित्वों वाला प्रोटोकॉल चाहते थे, जबकि कई विकसित और कुछ अन्य देश ऐसा ढाँचा पसंद करते थे जो इन उपायों को स्वैच्छिक छोड़ दे। बढ़ाए गए सत्र के बाद भी सर्वसम्मति न होने पर निर्णय अगले सम्मेलन तक टाल दिया गया। "
  "सम्मेलन ने सूखा-प्रवण देशों के लिए प्रतिज्ञाओं के साथ रियाद वैश्विक सूखा लचीलापन साझेदारी शुरू की, और 2030 तक क्षरित भूमि की पुनर्स्थापना के लक्ष्य को दोहराया। भारत के लिए, जिसने 2030 तक 2.6 करोड़ हेक्टेयर क्षरित भूमि की पुनर्स्थापना का लक्ष्य रखा है और जिसने 2019 में कॉप14 की मेज़बानी की, सूखे से निपटने की क्षमता भूमि, जल और खाद्य सुरक्षा को जोड़ती है।",
  "United Nations Convention to Combat Desertification, COP16 (Riyadh, 2024) decisions; " + MOEF + ".",
  "l3-t6-env-unccd-cop16-drought", craft="inference")

# ---------------------------------------------------------------- Indian Environmental Laws & Bodies (h-pairs)
P("Indian Environmental Laws & Bodies", "hard", "Consider the following pairs of committees and the subjects they examined:",
  "समितियों और उनके द्वारा जाँचे गए विषयों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["T. S. R. Subramanian High-Level Committee (2014) : Review of India's environmental laws",
   "Tiger Task Force (2005) : Tiger conservation after tigers vanished from Sariska",
   "Western Ghats Ecology Expert Panel (2011), chaired by Madhav Gadgil : Ecological zoning of the Western Ghats",
   "Kasturirangan High-Level Working Group (2013) : Ecologically sensitive areas of the Western Ghats"],
  ["टी. एस. आर. सुब्रमण्यम उच्च स्तरीय समिति (2014) : भारत के पर्यावरण क़ानूनों की समीक्षा",
   "बाघ कार्यबल (2005) : सरिस्का से बाघों के लुप्त होने के बाद बाघ संरक्षण",
   "माधव गाडगिल की अध्यक्षता वाला पश्चिमी घाट पारिस्थितिकी विशेषज्ञ पैनल (2011) : पश्चिमी घाट का पारिस्थितिक क्षेत्रीकरण",
   "कस्तूरीरंगन उच्च स्तरीय कार्य समूह (2013) : पश्चिमी घाट के पारिस्थितिक रूप से संवेदनशील क्षेत्र"],
  3,
  "All four pairs are correct. The Subramanian committee proposed an umbrella environmental law and new national and State environment management authorities to handle clearances, and an appellate board; Parliament's standing committee criticised its proposals as weakening safeguards, and they were not adopted as a whole. The Tiger Task Force, chaired by Sunita Narain and set up after it emerged in 2005 that Sariska had lost all its tigers, recommended scientific population estimation and a greater role for local communities, leading to the 2006 amendment that created the National Tiger Conservation Authority. "
  "The Gadgil panel classified the entire Western Ghats into three grades of ecological sensitivity with strict limits on mining and construction, which several States opposed; the Kasturirangan group then proposed notifying about 37 per cent of the Ghats -- mainly the 'natural landscape' rather than settled and farmed areas -- as ecologically sensitive. The draft notifications based on it have been reissued several times without being finalised.",
  "चारों युग्म सही हैं। सुब्रमण्यम समिति ने एक व्यापक पर्यावरण क़ानून, स्वीकृतियों के लिए नए राष्ट्रीय और राज्य पर्यावरण प्रबंधन प्राधिकरणों, और एक अपीलीय बोर्ड का प्रस्ताव किया; संसद की स्थायी समिति ने इन प्रस्तावों की सुरक्षा उपायों को कमज़ोर करने वाले के रूप में आलोचना की, और इन्हें पूर्ण रूप से नहीं अपनाया गया। 2005 में सरिस्का के सभी बाघ समाप्त होने की बात सामने आने के बाद गठित, सुनीता नारायण की अध्यक्षता वाले बाघ कार्यबल ने वैज्ञानिक जनसंख्या आकलन और स्थानीय समुदायों की बड़ी भूमिका की सिफ़ारिश की, जिससे 2006 का वह संशोधन आया जिसने राष्ट्रीय बाघ संरक्षण प्राधिकरण बनाया। "
  "गाडगिल पैनल ने पूरे पश्चिमी घाट को पारिस्थितिक संवेदनशीलता की तीन श्रेणियों में बाँटा और खनन तथा निर्माण पर कड़ी सीमाएँ सुझाईं, जिसका कई राज्यों ने विरोध किया; फिर कस्तूरीरंगन समूह ने घाट के लगभग 37 प्रतिशत -- मुख्यतः बसे और खेती वाले क्षेत्रों के बजाय ‘प्राकृतिक भूदृश्य’ -- को पारिस्थितिक रूप से संवेदनशील अधिसूचित करने का प्रस्ताव रखा। इस पर आधारित मसौदा अधिसूचनाएँ कई बार फिर जारी हुई हैं, पर अंतिम रूप नहीं ले सकीं।",
  MOEF + ", reports of the High-Level Committee (2014), the Western Ghats Ecology Expert Panel (2011) and the High-Level Working Group (2013); Tiger Task Force report, 'Joining the Dots' (2005).",
  "l3-t6-env-committees-tsr-ttf-gadgil-kasturirangan", craft="linkage")

# ---------------------------------------------------------------- Climate Science & Mitigation (m-MCQ, m-stmt)
M("Climate Science & Mitigation", "medium",
  "In the IPCC scenario label 'SSP2-4.5', the figure 4.5 refers to:",
  "आईपीसीसी के परिदृश्य नाम ‘एसएसपी2-4.5’ में 4.5 का अंक किसे दर्शाता है?",
  ["the expected rise in global temperature, in degrees Celsius, by 2100",
   "the concentration of carbon dioxide in the air, in hundreds of parts per million",
   "the number of billions of people projected to live in extreme poverty",
   "the approximate radiative forcing in 2100, in watts per square metre"],
  ["2100 तक वैश्विक तापमान में अपेक्षित वृद्धि, डिग्री सेल्सियस में",
   "वायु में कार्बन डाइऑक्साइड की सांद्रता, सैकड़ों भाग प्रति दस लाख में",
   "अत्यधिक ग़रीबी में रहने वाले अनुमानित लोगों की संख्या, अरबों में",
   "2100 में लगभग विकिरण बल, वाट प्रति वर्ग मीटर में"],
  3,
  "The Sixth Assessment Report combined two ideas in its scenarios. The 'SSP' part names one of five Shared Socioeconomic Pathways -- narratives of how population, economic growth, inequality and technology might evolve, from SSP1 'sustainability' to SSP5 'fossil-fuelled development'. The number after the hyphen gives the approximate radiative forcing reached by 2100, in watts per square metre, which is the measure inherited from the earlier Representative Concentration Pathways. "
  "So SSP2-4.5 is a 'middle of the road' world with intermediate emissions, projected to warm about 2.7 deg C by the end of the century, while SSP1-1.9 is the very low pathway consistent with roughly 1.5 deg C and SSP5-8.5 the very high one. Reading the label correctly helps in interpreting projections of warming, rainfall and sea level in national assessments.",
  "छठी आकलन रिपोर्ट ने अपने परिदृश्यों में दो विचार मिलाए। ‘एसएसपी’ भाग पाँच साझा सामाजिक-आर्थिक मार्गों में से एक का नाम है -- जनसंख्या, आर्थिक वृद्धि, असमानता और प्रौद्योगिकी कैसे बदल सकती हैं, इसकी कथाएँ, एसएसपी1 ‘स्थिरता’ से एसएसपी5 ‘जीवाश्म-ईंधन आधारित विकास’ तक। हाइफ़न के बाद का अंक 2100 तक पहुँचने वाला लगभग विकिरण बल, वाट प्रति वर्ग मीटर में, देता है, जो पहले के प्रतिनिधि सांद्रता मार्गों से लिया गया माप है। "
  "इसलिए एसएसपी2-4.5 मध्यम उत्सर्जन वाला ‘बीच का रास्ता’ संसार है, जिसमें शताब्दी के अंत तक लगभग 2.7 डिग्री सेल्सियस तापवृद्धि का अनुमान है, जबकि एसएसपी1-1.9 लगभग 1.5 डिग्री के अनुरूप बहुत निम्न मार्ग है और एसएसपी5-8.5 बहुत उच्च। नाम को सही पढ़ना राष्ट्रीय आकलनों में तापवृद्धि, वर्षा और समुद्र-स्तर के अनुमानों को समझने में मदद करता है।",
  IPCC + ", Working Group I, Summary for Policymakers.", "l3-t6-env-ssp-scenario-labels", pos=3, craft="inference")

S("Climate Science & Mitigation", "medium", "With reference to feedbacks in the climate system, consider the following statements:",
  "जलवायु तंत्र के प्रतिपुष्टि (फ़ीडबैक) प्रभावों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["The water vapour feedback amplifies warming, because a warmer atmosphere holds more water vapour, itself a greenhouse gas.",
   "In the tropics, the lapse-rate feedback offsets part of the warming, because the upper troposphere warms more than the surface.",
   "The IPCC assesses the net feedback from clouds to be strongly negative, so that clouds largely cancel the warming from carbon dioxide."],
  ["जल-वाष्प प्रतिपुष्टि तापवृद्धि को बढ़ाती है, क्योंकि गर्म वायुमंडल में अधिक जल-वाष्प रहती है, जो स्वयं ग्रीनहाउस गैस है।",
   "उष्णकटिबंध में ह्रास-दर प्रतिपुष्टि तापवृद्धि के एक भाग को संतुलित करती है, क्योंकि ऊपरी क्षोभमंडल सतह से अधिक गर्म होता है।",
   "आईपीसीसी बादलों की कुल प्रतिपुष्टि को प्रबल रूप से ऋणात्मक आँकता है, जिससे बादल कार्बन डाइऑक्साइड की तापवृद्धि को लगभग निरस्त कर देते हैं।"],
  C3, 1,
  "Statements 1 and 2 are correct. Air can hold about 7 per cent more water vapour for each degree Celsius of warming, and that extra vapour traps more heat -- the largest single positive feedback, roughly doubling the warming from carbon dioxide alone. In the moist tropics, warming is greatest high in the troposphere, from where heat radiates more easily to space, so the lapse-rate feedback is negative there; in the Arctic the opposite holds and the surface warms most. "
  "Statement 3 is wrong: clouds both reflect sunlight and trap heat, and the IPCC's Sixth Assessment Report judged their net feedback to be likely positive, mainly because of changes in low clouds over the tropical oceans -- clouds were long the largest source of uncertainty in climate sensitivity, and narrowing that range was one of the report's key advances.",
  "कथन 1 और 2 सही हैं। हर डिग्री सेल्सियस तापवृद्धि पर वायु लगभग 7 प्रतिशत अधिक जल-वाष्प रख सकती है, और वह अतिरिक्त वाष्प अधिक ऊष्मा रोकती है -- यह सबसे बड़ी एकल धनात्मक प्रतिपुष्टि है, जो अकेले कार्बन डाइऑक्साइड से होने वाली तापवृद्धि को लगभग दुगना कर देती है। नम उष्णकटिबंध में तापवृद्धि क्षोभमंडल में ऊपर सबसे अधिक होती है, जहाँ से ऊष्मा अंतरिक्ष में आसानी से विकिरित होती है, इसलिए वहाँ ह्रास-दर प्रतिपुष्टि ऋणात्मक है; आर्कटिक में इसका उल्टा होता है और सतह सबसे अधिक गर्म होती है। "
  "कथन 3 ग़लत है: बादल सूर्य का प्रकाश परावर्तित भी करते हैं और ऊष्मा रोकते भी हैं, और आईपीसीसी की छठी आकलन रिपोर्ट ने उनकी कुल प्रतिपुष्टि को संभवतः धनात्मक माना, मुख्यतः उष्णकटिबंधीय महासागरों पर निम्न बादलों में बदलाव के कारण -- बादल लंबे समय तक जलवायु संवेदनशीलता में अनिश्चितता का सबसे बड़ा स्रोत रहे, और उस सीमा को संकरा करना रिपोर्ट की प्रमुख प्रगतियों में था।",
  IPCC + ", Working Group I, Chapter 7.", "l3-t6-env-water-vapour-lapse-rate-cloud-feedbacks", craft="inference")

# ---------------------------------------------------------------- Protected Areas & Wildlife Protection (m-MCQ, m-stmt)
M("Protected Areas & Wildlife Protection", "medium",
  "In India, Important Bird and Biodiversity Areas have been identified by the Bombay Natural History Society as the national partner of:",
  "भारत में महत्वपूर्ण पक्षी और जैव विविधता क्षेत्रों की पहचान बॉम्बे नेचुरल हिस्ट्री सोसाइटी ने किसके राष्ट्रीय साझेदार के रूप में की है?",
  ["the International Union for Conservation of Nature",
   "Wetlands International",
   "the World Wide Fund for Nature",
   "BirdLife International"],
  ["अंतरराष्ट्रीय प्रकृति संरक्षण संघ",
   "वेटलैंड्स इंटरनेशनल",
   "वर्ल्ड वाइड फ़ंड फ़ॉर नेचर",
   "बर्डलाइफ़ इंटरनेशनल"],
  3,
  "BirdLife International, a global partnership of conservation organisations, developed standard criteria for Important Bird and Biodiversity Areas: a site qualifies if it regularly holds significant numbers of a globally threatened species, a species with a restricted range, a biome-restricted species, or large congregations of birds. The BNHS, its Indian partner, identified several hundred such sites across the country. "
  "Many IBAs lie outside the protected-area network -- grasslands, wetlands, farmland and community forests -- so the list helps planners see where clearances, power lines or wetland conversion might harm birds, and it has guided the designation of Ramsar sites and conservation reserves. The IUCN maintains the Red List, Wetlands International works on wetland conservation and waterbird counts, and the WWF runs field conservation programmes.",
  "बर्डलाइफ़ इंटरनेशनल, संरक्षण संगठनों की एक वैश्विक साझेदारी, ने महत्वपूर्ण पक्षी और जैव विविधता क्षेत्रों के लिए मानक मानदंड बनाए: कोई स्थल योग्य होता है यदि वह नियमित रूप से किसी विश्व स्तर पर संकटग्रस्त प्रजाति, सीमित क्षेत्र वाली प्रजाति, जीवोम-सीमित प्रजाति, या पक्षियों के बड़े जमावड़ों की उल्लेखनीय संख्या रखता हो। इसके भारतीय साझेदार बीएनएचएस ने देश भर में ऐसे कई सौ स्थल पहचाने। "
  "अनेक आईबीए संरक्षित क्षेत्र तंत्र के बाहर हैं -- घासभूमियाँ, आर्द्रभूमियाँ, खेत और सामुदायिक वन -- इसलिए यह सूची योजनाकारों को देखने में मदद करती है कि स्वीकृतियाँ, बिजली लाइनें या आर्द्रभूमि का रूपांतरण कहाँ पक्षियों को हानि पहुँचा सकता है, और इसने रामसर स्थलों और संरक्षण आरक्षितों के निर्धारण का मार्गदर्शन किया है। आईयूसीएन रेड लिस्ट रखता है, वेटलैंड्स इंटरनेशनल आर्द्रभूमि संरक्षण और जलपक्षी गणना पर काम करता है, और डब्ल्यूडब्ल्यूएफ़ क्षेत्रीय संरक्षण कार्यक्रम चलाता है।",
  "Bombay Natural History Society, Important Bird and Biodiversity Areas of India; BirdLife International.",
  "l3-t6-env-important-bird-areas-birdlife", pos=3, craft="recall")

S("Protected Areas & Wildlife Protection", "medium", "With reference to the conservation breeding of the great Indian bustard, consider the following statements:",
  "ग्रेट इंडियन बस्टर्ड के संरक्षण प्रजनन के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Under the programme, eggs collected from the wild in Rajasthan have been hatched at breeding centres in Jaisalmer district.",
   "In 2024 a chick was hatched at one of these centres through artificial insemination, a first for the species."],
  ["कार्यक्रम के अंतर्गत राजस्थान में जंगल से एकत्र अंडों से जैसलमेर ज़िले के प्रजनन केंद्रों में चूज़े निकाले गए हैं।",
   "2024 में इनमें से एक केंद्र पर कृत्रिम गर्भाधान से एक चूज़ा निकला, जो इस प्रजाति के लिए पहली बार था।"],
  T2, 2,
  "Both statements are correct. With only about 150 birds left, most of them in and around the Desert National Park, the Rajasthan Forest Department and the Wildlife Institute of India set up breeding centres at Sam and Ramdevra in Jaisalmer district under a programme supported by the Union environment ministry; eggs are collected from wild nests, which face predation and trampling, and hatched under controlled conditions to build a captive 'insurance' flock. "
  "In 2024 the centre achieved the first successful artificial insemination of the species, using semen from a captive male, a technique borrowed from work on the houbara bustard. The aim is to release birds into predator-proof enclosures and the wild once the threats, above all collisions with power lines across the Thar, are reduced.",
  "दोनों कथन सही हैं। केवल लगभग 150 पक्षी बचे होने पर, जिनमें से अधिकांश डेज़र्ट नेशनल पार्क में और उसके आसपास हैं, राजस्थान वन विभाग और भारतीय वन्यजीव संस्थान ने केंद्रीय पर्यावरण मंत्रालय द्वारा समर्थित कार्यक्रम के अंतर्गत जैसलमेर ज़िले के सम और रामदेवरा में प्रजनन केंद्र बनाए; अंडे जंगली घोंसलों से एकत्र किए जाते हैं, जिन्हें शिकारियों और कुचले जाने का ख़तरा रहता है, और नियंत्रित परिस्थितियों में उनसे चूज़े निकाले जाते हैं ताकि एक बंदी ‘बीमा’ झुंड बने। "
  "2024 में केंद्र ने एक बंदी नर के वीर्य का उपयोग कर इस प्रजाति का पहला सफल कृत्रिम गर्भाधान किया, एक तकनीक जो हुबारा बस्टर्ड पर हुए काम से ली गई। उद्देश्य यह है कि ख़तरे, सबसे बढ़कर थार में बिजली लाइनों से टक्कर, घटने पर पक्षियों को शिकारी-रोधी बाड़ों और जंगल में छोड़ा जाए।",
  WII + " and Rajasthan Forest Department, Great Indian Bustard conservation breeding programme; " + MOEF + ".",
  "l3-t6-env-gib-conservation-breeding", craft="recall")

# ---------------------------------------------------------------- Ecosystems & Ecological Processes (m-stmt)
S("Ecosystems & Ecological Processes", "medium", "With reference to animals used as indicators of the health of freshwater ecosystems, consider the following statements:",
  "मीठे जल के पारितंत्रों के स्वास्थ्य के सूचक के रूप में प्रयुक्त जंतुओं के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Larvae of mayflies, stoneflies and caddisflies are sensitive to pollution, so their presence indicates clean, well-oxygenated water.",
   "Amphibians, with permeable skin and lives spent partly in water and partly on land, are sensitive indicators of environmental change.",
   "An abundance of Tubifex worms and red chironomid larvae in a stream indicates heavy organic pollution."],
  ["मेफ़्लाई, स्टोनफ़्लाई और कैडिसफ़्लाई के लार्वा प्रदूषण के प्रति संवेदनशील होते हैं, इसलिए उनकी उपस्थिति स्वच्छ, ऑक्सीजन-युक्त जल का संकेत है।",
   "पारगम्य त्वचा वाले और जीवन का एक भाग जल में तथा एक भाग स्थल पर बिताने वाले उभयचर पर्यावरणीय बदलाव के संवेदनशील सूचक हैं।",
   "किसी धारा में ट्यूबिफ़ेक्स कृमियों और लाल काइरोनोमिड लार्वा की बहुतायत भारी कार्बनिक प्रदूषण का संकेत है।"],
  C3, 2,
  "All three are correct. Biological monitoring uses the organisms living in a water body as a record of conditions over weeks and months, unlike a single chemical test. The insect larvae grouped as 'EPT' need high dissolved oxygen and disappear first as sewage or silt increases; Tubifex worms, which carry haemoglobin, and the red 'bloodworm' larvae of chironomid midges tolerate oxygen-poor water and multiply where organic waste is decomposing. Frogs and other amphibians absorb water and chemicals through their skin, so declines and deformities can signal pollution, disease or habitat change. "
  "India's pollution control boards and researchers have used such biotic indices alongside measures like biological oxygen demand to classify river stretches -- a useful check on whether clean-up programmes are restoring living rivers rather than only meeting chemical standards.",
  "तीनों कथन सही हैं। जैविक निगरानी किसी जलाशय में रहने वाले जीवों को सप्ताहों और महीनों की परिस्थितियों के अभिलेख के रूप में प्रयोग करती है, किसी एक रासायनिक परीक्षण के विपरीत। ‘ईपीटी’ के रूप में समूहित कीट-लार्वा को अधिक घुली ऑक्सीजन चाहिए और मल-जल या गाद बढ़ने पर वे सबसे पहले लुप्त होते हैं; हीमोग्लोबिन रखने वाले ट्यूबिफ़ेक्स कृमि और काइरोनोमिड मच्छरों के लाल ‘ब्लडवर्म’ लार्वा ऑक्सीजन-विहीन जल सह लेते हैं और जहाँ कार्बनिक अपशिष्ट सड़ रहा हो वहाँ बढ़ते हैं। मेंढक और अन्य उभयचर अपनी त्वचा से जल और रसायन सोखते हैं, इसलिए उनकी संख्या में गिरावट और विकृतियाँ प्रदूषण, रोग या आवास परिवर्तन का संकेत दे सकती हैं। "
  "भारत के प्रदूषण नियंत्रण बोर्डों और शोधकर्ताओं ने नदी-खंडों के वर्गीकरण के लिए जैव-रासायनिक ऑक्सीजन माँग जैसे मापों के साथ ऐसे जैविक सूचकांकों का उपयोग किया है -- यह जाँचने का उपयोगी तरीका कि सफ़ाई कार्यक्रम केवल रासायनिक मानक पूरे कर रहे हैं या जीवित नदियाँ भी लौटा रहे हैं।",
  BIO12 + "; Central Pollution Control Board, biological water quality criteria.", "l3-t6-env-freshwater-bioindicators", craft="application")

# ---------------------------------------------------------------- Climate Agreements & Carbon Markets (m-stmt)
S("Climate Agreements & Carbon Markets", "medium", "With reference to China's national emissions trading scheme, consider the following statements:",
  "चीन की राष्ट्रीय उत्सर्जन व्यापार योजना के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Launched in 2021 for the power sector, it is the world's largest carbon market by the volume of emissions covered.",
   "In 2025 it was extended to the steel, cement and aluminium sectors.",
   "From its launch it has set an absolute cap on total emissions, like the European Union's scheme."],
  ["2021 में बिजली क्षेत्र के लिए शुरू हुई यह योजना शामिल उत्सर्जन की मात्रा के हिसाब से विश्व का सबसे बड़ा कार्बन बाज़ार है।",
   "2025 में इसका विस्तार इस्पात, सीमेंट और एल्युमिनियम क्षेत्रों तक किया गया।",
   "शुरुआत से ही यह यूरोपीय संघ की योजना की तरह कुल उत्सर्जन पर पूर्ण सीमा तय करती है।"],
  C3, 1,
  "Statements 1 and 2 are correct. China's scheme began with more than two thousand coal- and gas-fired power plants, covering several billion tonnes of carbon dioxide a year, more than any other market; in 2025 the government added steel, cement and aluminium smelting, bringing in another large slice of the country's emissions. "
  "Statement 3 is wrong: allowances have been allocated on the basis of emission intensity -- carbon dioxide per unit of electricity or product -- so total emissions can grow with output, and prices have stayed far below those in Europe. China has said it will move some sectors to absolute caps later in the decade. The design is close to India's own Carbon Credit Trading Scheme, which also uses intensity targets, which is why China's experience is watched closely in New Delhi.",
  "कथन 1 और 2 सही हैं। चीन की योजना दो हज़ार से अधिक कोयला और गैस आधारित बिजलीघरों से शुरू हुई, जो हर वर्ष कई अरब टन कार्बन डाइऑक्साइड को शामिल करती है, किसी भी अन्य बाज़ार से अधिक; 2025 में सरकार ने इस्पात, सीमेंट और एल्युमिनियम प्रगलन जोड़े, जिससे देश के उत्सर्जन का एक और बड़ा भाग इसमें आ गया। "
  "कथन 3 ग़लत है: भत्ते उत्सर्जन तीव्रता -- बिजली या उत्पाद की प्रति इकाई कार्बन डाइऑक्साइड -- के आधार पर बाँटे गए हैं, इसलिए उत्पादन के साथ कुल उत्सर्जन बढ़ सकता है, और क़ीमतें यूरोप से बहुत नीचे रही हैं। चीन ने कहा है कि वह दशक में आगे कुछ क्षेत्रों को पूर्ण सीमा पर ले जाएगा। यह रूपरेखा भारत की अपनी कार्बन क्रेडिट व्यापार योजना के क़रीब है, जो भी तीव्रता लक्ष्यों का उपयोग करती है, इसीलिए नई दिल्ली में चीन के अनुभव पर नज़र रखी जाती है।",
  "Ministry of Ecology and Environment of the People's Republic of China (2021, 2025); International Carbon Action Partnership, ETS status reports.",
  "l3-t6-env-china-national-ets", craft="linkage")

write("gs_l3_t6_c.sql")
