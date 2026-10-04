# -*- coding: utf-8 -*-
"""Level 2 · Test 9 (Environment 1: Ecosystems, Fauna and Flora) -- depth audit of 2026-10-04
(docs/upsc-question-design-standard.md §6).

All 108 rows were read and classified. Before: analytic 24, precision 28, recall 56 (6 rows are Test 21's,
already tagged). 26 rows are rewritten in place with the same concept id, type and difficulty:
  - fauna rows that asked a species' range or status now ask why it is threatened or what follows from its
    biology: tuskless bulls, ivory poaching and corridors for the elephant; the rhino's recovery and the
    floodplain; plastic for the leatherback; natal homing for the olive ridley; the pangolin's defence; the
    horseshoe crab's blood; Nipah and fruit bats; the dugong's seagrass; the Amur falcon at Pangti; the
    bustard and power lines; the purple frog's Gondwana link. A koel's nesting is classified as an
    interaction, a shahtoosh shawl is tested against the law, and a crocodilian is identified from its snout;
  - ecosystem and flora rows now apply the levels of organisation to a pond, explain what keeps savanna and
    tundra treeless and read Costanza's valuation. They also explain bryophytes, invasive plants, Khejri,
    forest produce, Neelakurinji, and sacred groves and village springs.
After: analytic 49, precision 29, recall 30. The other 76 rows keep their content and get their craft tag.
Keys were chosen up front: 3-statement rows have 5 Only one, 5 Only two, 5 All three and 1 None.
Leaks and repeats avoided while drafting:
  - the Great Indian Bustard as Rajasthan's State bird (answers the rediscovered-birds row);
  - fire in the savanna stem (the shola row tests frost and fire);
  - Bishnoi in the Khejarli stem (the blackbuck row);
  - 'Critically Endangered' and 'fallen steadily' stems (repeat the red panda and wild ass templates);
  - Rhino Vision 2020 translocations, turtle excluder devices, hatchlings and beach lights, the tundra's
    short growing season, and who declares reserves: these are tested in env-indian-rhino-vision-2020,
    env-sea-turtle-protection-measures, env-light-pollution, geo-deserts-tundra-easy and
    env-protected-area-network."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write_updates, CODE
from polity_common import C3, C4, T2

d.SUBJECT = "Environment & Ecology"
d.REQUIRE_CRAFT = True
ECO = "Ecosystems & Ecological Processes"
FAU = "Fauna & Animal Behaviour"
FLO = "Flora, Fungi & Forests"
NB12 = "NCERT Class XII, Biology"
NB11 = "NCERT Class XI, Biology"
IUCN = "IUCN Red List of Threatened Species"
WPA = "Wild Life (Protection) Act, 1972, as amended in 2022"
WII = "Wildlife Institute of India"

# ================================================================ ECOSYSTEMS (3)
S(ECO, "easy", "A village pond holds many frogs of one species, along with fish, water plants and microbes, living in water warmed by the sun and fed by rain. Consider the following statements:",
  "एक गाँव के तालाब में एक ही प्रजाति के बहुत से मेंढक, मछलियों, जलीय पौधों और सूक्ष्मजीवों के साथ, सूर्य से गर्म और वर्षा से भरे पानी में रहते हैं। निम्नलिखित कथनों पर विचार कीजिए:",
  ["All the frogs of that one species in the pond form a population.",
   "The frogs, fish, plants and microbes together form a community.",
   "The community together with the water, mud, sunlight and nutrients forms an ecosystem."],
  ["तालाब में उस एक प्रजाति के सभी मेंढक एक समष्टि बनाते हैं।",
   "मेंढक, मछलियाँ, पौधे और सूक्ष्मजीव मिलकर एक समुदाय बनाते हैं।",
   "समुदाय पानी, कीचड़, धूप और पोषक तत्वों के साथ मिलकर एक पारितंत्र बनाता है।"],
  C3, 2,
  "All three are correct, and they show the levels of ecological organisation. A population is the group of individuals of one species in an area; a community is all the populations of different species living and interacting there; and an ecosystem is the community together with its non-living (abiotic) environment, through which energy flows and nutrients cycle. "
  "The pond is the textbook example of a small, self-sustaining ecosystem.",
  "तीनों कथन सही हैं, और पारिस्थितिक संगठन के स्तर दिखाते हैं। समष्टि किसी क्षेत्र में एक प्रजाति के जीवों का समूह है; समुदाय वहाँ रहने और परस्पर क्रिया करने वाली अलग-अलग प्रजातियों की सभी समष्टियाँ हैं; और पारितंत्र समुदाय के साथ उसका अजैव पर्यावरण है, जिसमें ऊर्जा बहती है और पोषक तत्वों का चक्र चलता है। "
  "तालाब एक छोटे, आत्मनिर्भर पारितंत्र का पाठ्यपुस्तकीय उदाहरण है।",
  NB12, "env-population-community-ecosystem", craft="application")

S(ECO, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Savannas occur where rainfall is too low or too seasonal for closed forest but enough for a continuous cover of grass.",
   "Permafrost, which stops roots from going deep and water from draining, is one reason the tundra is largely treeless."],
  ["सवाना वहाँ मिलते हैं जहाँ वर्षा बंद वन के लिए बहुत कम या बहुत मौसमी हो, पर घास के लगातार आवरण के लिए पर्याप्त हो।",
   "स्थायी तुषार-भूमि (पर्माफ़्रॉस्ट), जो जड़ों को गहरा जाने और पानी को निकलने से रोकती है, टुंड्रा के लगभग वृक्षहीन होने का एक कारण है।"],
  T2, 2,
  "Both statements are correct. In tropical savannas, as in East Africa, a long dry season limits trees, and regular grass fires kill their seedlings while grasses regrow from their roots, so the landscape stays open with scattered fire-tolerant trees such as acacias. "
  "In the tundra, the ground below the surface stays frozen all year, so roots cannot go deep and water cannot drain, and the growing season lasts only a few weeks; only mosses, lichens, sedges and dwarf shrubs survive. Tall conifers belong to the taiga just to the south.",
  "दोनों कथन सही हैं। पूर्वी अफ़्रीका जैसे उष्णकटिबंधीय सवाना में लंबा शुष्क मौसम वृक्षों को सीमित करता है, और नियमित घास की आग उनके अंकुर मार देती है, जबकि घास अपनी जड़ों से फिर उग आती है, इसलिए परिदृश्य बबूल जैसे आग-सहिष्णु बिखरे वृक्षों के साथ खुला रहता है। "
  "टुंड्रा में सतह के नीचे की भूमि साल भर जमी रहती है, इसलिए जड़ें गहरी नहीं जा सकतीं और पानी निकल नहीं पाता, और वृद्धि-काल कुछ ही सप्ताह का होता है; केवल काई, लाइकेन, मोथा और बौनी झाड़ियाँ बचती हैं। ऊँचे शंकुधारी वृक्ष उसके ठीक दक्षिण के टैगा के हैं।",
  NB12, "env-tundra-savanna-biomes", craft="linkage")

S(ECO, "hard", "In 1997 Robert Costanza and colleagues put the value of the world's ecosystem services at about US$ 33 trillion a year -- nearly twice the world's gross national product at the time. Consider the following statements:",
  "1997 में रॉबर्ट कोस्टांज़ा और साथियों ने संसार की पारितंत्र सेवाओं का मूल्य लगभग 33 ट्रिलियन अमेरिकी डॉलर प्रति वर्ष आँका, जो उस समय संसार के सकल राष्ट्रीय उत्पाद का लगभग दोगुना था। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The estimate implies that conventional national accounts leave out much of nature's contribution to human welfare.",
   "Recreation accounted for about half of the total value.",
   "The study showed that these services could be replaced by technology at a lower cost."],
  ["यह अनुमान इंगित करता है कि पारंपरिक राष्ट्रीय लेखे मानव कल्याण में प्रकृति के योगदान का बड़ा भाग छोड़ देते हैं।",
   "कुल मूल्य का लगभग आधा भाग मनोरंजन का था।",
   "अध्ययन ने दिखाया कि इन सेवाओं को तकनीक से कम लागत पर बदला जा सकता है।"],
  C3, 0,
  "Only statement 1 is correct. The study priced services that nature provides free -- purifying air and water, pollination, flood control, soil formation, nutrient cycling, climate regulation -- and found that they would cost more than the whole world economy produced, which is why the services are said to be invisible in GDP and easily lost. "
  "Statement 2 is wrong: the largest single item was soil formation, about half; recreation and nutrient cycling were each under 10 per cent. Statement 3 is the opposite of the point: most of these services have no practical technological substitute at any comparable cost.",
  "केवल कथन 1 सही है। अध्ययन ने उन सेवाओं का मूल्य लगाया जो प्रकृति मुफ़्त देती है, जैसे वायु और जल शुद्धि, परागण, बाढ़ नियंत्रण, मृदा-निर्माण, पोषक चक्र और जलवायु नियमन, और पाया कि उनकी लागत पूरी विश्व अर्थव्यवस्था के उत्पादन से अधिक होगी, इसीलिए कहा जाता है कि ये सेवाएँ GDP में अदृश्य हैं और आसानी से खो जाती हैं। "
  "कथन 2 गलत है: सबसे बड़ा एकल भाग, लगभग आधा, मृदा-निर्माण था; मनोरंजन और पोषक चक्र प्रत्येक 10 प्रतिशत से कम थे। कथन 3 मूल बात का उलटा है: इनमें से अधिकांश सेवाओं का किसी तुलनीय लागत पर कोई व्यावहारिक तकनीकी विकल्प नहीं है।",
  NB12, "env-ecosystem-services-value", craft="inference")

# ================================================================ FAUNA: MCQs (3)
M(FAU, "medium", "The Asian koel lays its eggs in the nests of crows, which then raise its chicks. This relationship is best classified as:",
  "एशियाई कोयल अपने अंडे कौओं के घोंसलों में देती है, और फिर कौए उसके चूज़ों को पालते हैं। इस संबंध को सबसे अच्छी तरह किस रूप में वर्गीकृत किया जाता है?",
  ["brood parasitism, a form of parasitism",
   "mutualism, since both species gain",
   "commensalism, since the crow is unaffected",
   "amensalism, since the koel is harmed"],
  ["अंड-परजीविता, जो परजीविता का एक रूप है",
   "सहोपकारिता, क्योंकि दोनों प्रजातियों को लाभ होता है",
   "सहभोजिता, क्योंकि कौए पर कोई प्रभाव नहीं पड़ता",
   "असहभोजिता, क्योंकि कोयल को हानि होती है"],
  0,
  "The koel gains, because another bird does the costly work of incubating and feeding its young, and the crow loses, because it spends its effort on chicks that are not its own and often loses some of its own brood; so the interaction is parasitism of a particular kind, brood parasitism. "
  "Natural selection has made the koel's eggs resemble the host's, so the host is less likely to reject them. Mutualism benefits both, commensalism benefits one and leaves the other unaffected, and amensalism harms one without benefit to the other.",
  "कोयल को लाभ होता है, क्योंकि दूसरा पक्षी उसके बच्चों को सेने और खिलाने का महँगा काम करता है, और कौए को हानि होती है, क्योंकि वह अपनी मेहनत उन चूज़ों पर लगाता है जो उसके अपने नहीं हैं और प्रायः अपने कुछ बच्चे खो देता है; इसलिए यह परस्पर क्रिया एक विशेष प्रकार की परजीविता, अंड-परजीविता, है। "
  "प्राकृतिक चयन ने कोयल के अंडों को परपोषी के अंडों जैसा बना दिया है, ताकि परपोषी उन्हें अस्वीकार न करे। सहोपकारिता में दोनों को लाभ, सहभोजिता में एक को लाभ और दूसरे पर कोई प्रभाव नहीं, और असहभोजिता में एक को हानि होती है बिना दूसरे को लाभ के।",
  NB12, "env-koel-brood-parasite", craft="application")

M(FAU, "medium", "The 'big four' -- the spectacled cobra, the common krait, Russell's viper and the saw-scaled viper -- cause most snakebite deaths in India mainly because they:",
  "'बड़े चार' -- चश्मेवाला नाग, सामान्य करैत, रसेल वाइपर और सॉ-स्केल्ड वाइपर -- भारत में साँप के काटने से होने वाली अधिकांश मौतों का कारण मुख्यतः इसलिए हैं कि वे:",
  ["are common around farms and homes, where people work barefoot and sleep on the floor",
   "are the most venomous snakes in the world, far more so than any of the snakes of Australia",
   "attack people without provocation, chasing them over long distances",
   "are found only in the forests, where treatment cannot reach the victims"],
  ["खेतों और गाँवों के आसपास आम हैं, जहाँ लोग नंगे पैर काम करते और फ़र्श पर सोते हैं",
   "संसार के सबसे विषैले साँप हैं, ऑस्ट्रेलिया के किसी भी साँप से कहीं अधिक",
   "बिना उकसावे के लोगों पर हमला करते हैं और लंबी दूरी तक उनका पीछा करते हैं",
   "केवल वनों में मिलते हैं, जहाँ पीड़ितों तक उपचार नहीं पहुँच पाता"],
  0,
  "These four are widespread in fields, grain stores and homes, drawn by the rats that farming attracts; farm workers in fields and paddies, and families sleeping on the floor -- where the nocturnal krait often bites -- come into frequent contact with them, and delays in reaching antivenom add to deaths. India's polyvalent antivenom is raised against these four species. "
  "Several Australian snakes have more potent venom, and snakes generally bite in defence; the problem is one of exposure and access to treatment.",
  "ये चारों खेतों, अनाज-भंडारों और घरों में व्यापक रूप से मिलते हैं, खेती से आकर्षित होने वाले चूहों के कारण; खेतों और धान के खेतों के मज़दूर, और फ़र्श पर सोने वाले परिवार, जहाँ रात में सक्रिय करैत प्रायः काटता है, इनके लगातार संपर्क में आते हैं, और प्रतिविष तक पहुँचने में देरी मौतें बढ़ाती है। भारत का बहुसंयोजी प्रतिविष इन्हीं चार प्रजातियों के विरुद्ध बनाया जाता है। "
  "ऑस्ट्रेलिया के कई साँपों का विष अधिक तीव्र है, और साँप प्रायः बचाव में काटते हैं; समस्या संपर्क और उपचार तक पहुँच की है।",
  "Ministry of Health and Family Welfare -- National Action Plan for Prevention and Control of Snakebite Envenoming (2024).",
  "env-big-four-snakes", craft="linkage")

M(FAU, "medium", "A trader offers a tourist a fine 'ring shawl' of shahtoosh, saying the wool was collected from hair the animals shed on bushes. Under Indian law:",
  "एक व्यापारी एक पर्यटक को शाहतूश का बारीक 'रिंग शॉल' यह कहकर देता है कि ऊन जानवरों द्वारा झाड़ियों पर छोड़े गए बालों से इकट्ठा की गई। भारतीय क़ानून के तहत:",
  ["selling or buying it is an offence, since shahtoosh comes from the chiru, which is killed for it",
   "the sale is legal, since wool gathered from hair the animals have shed does not harm them in any way",
   "the sale is legal, since shahtoosh comes from the domesticated pashmina goat",
   "the sale is legal if the shawl is exported abroad with a CITES permit issued for Appendix II species"],
  ["इसे बेचना या ख़रीदना अपराध है, क्योंकि शाहतूश चिरू से आता है, जिसे इसके लिए मारा जाता है",
   "बिक्री वैध है, क्योंकि जानवरों के झड़े बालों से इकट्ठी ऊन से उन्हें किसी तरह की हानि नहीं होती",
   "बिक्री वैध है, क्योंकि शाहतूश पालतू पश्मीना बकरी से आता है",
   "शॉल परिशिष्ट II की प्रजातियों के CITES परमिट के साथ निर्यात हो, तो बिक्री वैध है"],
  0,
  "Shahtoosh is woven from the fine underwool of the Tibetan antelope, or chiru, and the 'shed hair' story is a myth used to sell it: the animal must be killed, about three to five for a single shawl, which drove a steep fall in its numbers. The chiru is in Schedule I of the Wild Life (Protection) Act and in Appendix I of CITES, which bans commercial international trade, so making, selling or buying shahtoosh is illegal. "
  "Pashmina comes from the domesticated Changthangi goat of Ladakh and is legal.",
  "शाहतूश तिब्बती मृग, चिरू, की बारीक भीतरी ऊन से बुना जाता है, और 'झड़े बाल' की कहानी इसे बेचने के लिए गढ़ा गया मिथक है: जानवर को मारना पड़ता है, एक शॉल के लिए लगभग तीन से पाँच, जिससे इसकी संख्या तेज़ी से घटी। चिरू वन्यजीव (संरक्षण) अधिनियम की अनुसूची I और CITES के परिशिष्ट I में है, जो वाणिज्यिक अंतरराष्ट्रीय व्यापार पर रोक लगाता है, इसलिए शाहतूश बनाना, बेचना या ख़रीदना अवैध है। "
  "पश्मीना लद्दाख की पालतू चांगथांगी बकरी से आती है और वैध है।",
  WPA, "env-chiru-shahtoosh", craft="application")

# ================================================================ FAUNA: statements (14)
S(FAU, "easy", "Consider the following statements about the Asian elephant:",
  "एशियाई हाथी के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["A herd is usually led by the oldest female, whose memory of water and food sources guides the group in hard seasons.",
   "Since only some Asian bulls carry tusks, poaching for ivory has skewed the sex ratio in some populations.",
   "Because a herd needs a large home range, the loss of corridors linking forest patches pushes elephants into fields and villages."],
  ["झुंड का नेतृत्व प्रायः सबसे बूढ़ी मादा करती है, जिसकी जल और भोजन के स्रोतों की स्मृति कठिन मौसम में समूह का मार्गदर्शन करती है।",
   "चूँकि केवल कुछ एशियाई नर हाथियों के दाँत होते हैं, हाथीदाँत के लिए शिकार ने कुछ समष्टियों में लिंगानुपात बिगाड़ दिया है।",
   "चूँकि एक झुंड को बड़ा आवास-क्षेत्र चाहिए, इसलिए वन-खंडों को जोड़ने वाले गलियारों के नष्ट होने से हाथी खेतों और गाँवों में धकेले जाते हैं।"],
  C3, 2,
  "All three are correct. Elephant herds are family groups of related females and young, led by the matriarch, while adult males live alone or in loose groups. Among Asian elephants females have no tusks and many males (makhnas) lack them too, so ivory poachers kill the tusked bulls; in parts of southern India, such as Periyar, this left very few adult males in the population. "
  "Herds move over hundreds of square kilometres through the year, and when roads, canals, mines and settlements cut the corridors between forests, they raid crops and come into conflict with people; the Elephant Corridors of India report of 2023 identified 150 corridors. The Asian elephant is listed as Endangered.",
  "तीनों कथन सही हैं। हाथी के झुंड संबंधित मादाओं और बच्चों के पारिवारिक समूह होते हैं, जिनका नेतृत्व मुखिया मादा करती है, जबकि वयस्क नर अकेले या ढीले समूहों में रहते हैं। एशियाई हाथियों में मादाओं के दाँत नहीं होते और कई नर (मखना) भी बिना दाँत के होते हैं, इसलिए हाथीदाँत के शिकारी दाँत वाले नरों को मारते हैं; दक्षिण भारत के कुछ भागों, जैसे पेरियार, में इससे समष्टि में बहुत कम वयस्क नर बचे। "
  "झुंड साल भर में सैकड़ों वर्ग किलोमीटर में घूमते हैं, और जब सड़कें, नहरें, खदानें और बस्तियाँ वनों के बीच के गलियारे काट देती हैं, तो वे फ़सलों पर धावा बोलते हैं और मनुष्यों से संघर्ष में आते हैं; 2023 की 'एलिफ़ेंट कॉरिडोर्स ऑफ़ इंडिया' रिपोर्ट ने 150 गलियारे चिह्नित किए। एशियाई हाथी संकटग्रस्त (Endangered) श्रेणी में है।",
  IUCN, "env-asian-elephant-biology", craft="linkage")

S(FAU, "easy", "Consider the following statements about the greater one-horned rhinoceros:",
  "बड़े एक-सींग वाले गैंडे के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Poaching for its horn, which is made of keratin and wrongly valued as medicine, is the chief direct threat to it.",
   "Its wild population today is smaller than it was in the early twentieth century.",
   "Since it browses in dense hill forests, the annual floods of the Brahmaputra plain pose little risk to it."],
  ["इसके सींग के लिए शिकार, जो केराटिन से बना है और ग़लत ढंग से दवा के रूप में मूल्यवान माना जाता है, इसके लिए मुख्य प्रत्यक्ष ख़तरा है।",
   "इसकी जंगली समष्टि आज बीसवीं सदी के आरंभ की तुलना में छोटी है।",
   "चूँकि यह घने पहाड़ी वनों में पत्तियाँ चरता है, इसलिए ब्रह्मपुत्र के मैदान की वार्षिक बाढ़ इसके लिए बहुत कम ख़तरा है।"],
  C3, 0,
  "Only statement 1 is correct. The horn, of keratin like our hair and nails, has no proven medical value but fetches high prices, which drives poaching. "
  "Statement 2 is wrong: from fewer than 200 animals in the early 1900s, strict protection in Kaziranga, Orang, Pobitora, Jaldapara and Nepal's Chitwan brought the species back to more than 4,000, one of Asia's great conservation recoveries; it is now listed as Vulnerable. Statement 3 is wrong on both counts: the rhino is a grazer of the tall wet grasslands of the floodplain, and the floods that renew those grasslands also drown animals and drive them onto high ground and across the highway, where they are exposed to vehicles and poachers -- which is why artificial highlands have been raised inside Kaziranga.",
  "केवल कथन 1 सही है। हमारे बालों और नाख़ूनों की तरह केराटिन से बने सींग का कोई सिद्ध चिकित्सीय मूल्य नहीं है, पर इसकी ऊँची क़ीमत मिलती है, जो शिकार को बढ़ावा देती है। "
  "कथन 2 गलत है: 1900 के दशक के आरंभ में 200 से कम जानवरों से, काज़ीरंगा, ओरंग, पोबितोरा, जलदापारा और नेपाल के चितवन में कठोर संरक्षण ने इस प्रजाति को 4,000 से अधिक तक पहुँचाया, जो एशिया की बड़ी संरक्षण सफलताओं में से एक है; अब यह 'सुभेद्य' (Vulnerable) श्रेणी में है। कथन 3 दोनों दृष्टियों से गलत है: गैंडा बाढ़ के मैदान की ऊँची नम घासभूमियों में घास चरता है, और वही बाढ़ जो इन घासभूमियों को नया करती है, जानवरों को डुबोती भी है और उन्हें ऊँची भूमि की ओर तथा राजमार्ग के पार धकेलती है, जहाँ वाहनों और शिकारियों का ख़तरा रहता है; इसीलिए काज़ीरंगा के भीतर कृत्रिम ऊँचे टीले बनाए गए हैं।",
  IUCN, "env-one-horned-rhino", craft="linkage")

S(FAU, "hard", "Consider the following statements about bird migration through India:",
  "भारत से होकर पक्षियों के प्रवास के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["India lies on the Central Asian Flyway, which links breeding grounds in Siberia and Central Asia with wintering grounds in the subcontinent.",
   "The loss and degradation of wetlands along the route is a major threat to the migrants that depend on them.",
   "The western population of the Siberian crane still winters regularly at Keoladeo National Park.",
   "The demoiselle cranes that winter at Khichan in Rajasthan breed in the Arctic tundra."],
  ["भारत मध्य एशियाई उड़ान-मार्ग पर स्थित है, जो साइबेरिया और मध्य एशिया के प्रजनन क्षेत्रों को उपमहाद्वीप के शीतकालीन क्षेत्रों से जोड़ता है।",
   "मार्ग के साथ आर्द्रभूमियों की हानि और क्षरण उन पर निर्भर प्रवासी पक्षियों के लिए बड़ा ख़तरा है।",
   "साइबेरियाई सारस की पश्चिमी समष्टि अब भी नियमित रूप से केवलादेव राष्ट्रीय उद्यान में सर्दियाँ बिताती है।",
   "राजस्थान के खीचन में सर्दियाँ बिताने वाले कुरजाँ (डेमोइसेल क्रेन) आर्कटिक टुंड्रा में प्रजनन करते हैं।"],
  C4, 1,
  "Statements 1 and 2 are correct. The Central Asian Flyway carries ducks, waders, cranes and raptors between Siberia, Central Asia and the Indian subcontinent, and the birds depend on a chain of wetlands to rest and feed; when those are drained or polluted, the whole route weakens, which is why India drew up a national action plan for the flyway. "
  "Statement 3 is wrong: the western Siberian cranes have not been seen at Keoladeo since 2002. Statement 4 is wrong: the demoiselle cranes that the villagers of Khichan feed breed on the steppes of Central Asia and Mongolia, not in the tundra.",
  "कथन 1 और 2 सही हैं। मध्य एशियाई उड़ान-मार्ग बत्तखों, जलचर पक्षियों, सारसों और शिकारी पक्षियों को साइबेरिया, मध्य एशिया और भारतीय उपमहाद्वीप के बीच ले जाता है, और पक्षी विश्राम और भोजन के लिए आर्द्रभूमियों की एक शृंखला पर निर्भर रहते हैं; जब वे सुखाई या प्रदूषित की जाती हैं, तो पूरा मार्ग कमज़ोर होता है, इसीलिए भारत ने इस उड़ान-मार्ग के लिए एक राष्ट्रीय कार्य-योजना बनाई। "
  "कथन 3 गलत है: पश्चिमी साइबेरियाई सारस 2002 के बाद से केवलादेव में नहीं दिखे। कथन 4 गलत है: खीचन के ग्रामीण जिन कुरजाँ को दाना डालते हैं, वे टुंड्रा में नहीं, मध्य एशिया और मंगोलिया के स्टेपी में प्रजनन करते हैं।",
  "Ministry of Environment, Forest and Climate Change -- National Action Plan for Conservation of Migratory Birds and their Habitats along the Central Asian Flyway (2018).",
  "env-central-asian-flyway-birds", craft="linkage")

S(FAU, "hard", "Consider the following statements about fruit bats (flying foxes) in India:",
  "भारत में फल चमगादड़ों (फ़्लाइंग फ़ॉक्स) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["By pollinating flowers and carrying seeds over long distances, they help tropical forests regenerate.",
   "Fruit bats of the genus Pteropus are natural reservoirs of the Nipah virus, and spillover to people has been linked to fruit or date-palm sap contaminated by bats.",
   "Bats and flying squirrels are the only mammals capable of true, powered flight."],
  ["फूलों का परागण कर और बीजों को लंबी दूरी तक ले जाकर वे उष्णकटिबंधीय वनों के पुनर्जनन में मदद करते हैं।",
   "टेरोपस वंश के फल चमगादड़ निपाह वायरस के प्राकृतिक भंडार हैं, और मनुष्यों तक इसके पहुँचने को चमगादड़ों से दूषित फलों या खजूर के रस से जोड़ा गया है।",
   "चमगादड़ और उड़न गिलहरियाँ ही वास्तविक, संचालित उड़ान में सक्षम स्तनधारी हैं।"],
  C3, 1,
  "Statements 1 and 2 are correct. Fruit bats pollinate trees such as the silk cotton and wild banana and drop seeds far from the parent tree, often across cleared land, which makes them important for forest regeneration. The Indian flying fox carries the Nipah virus without falling ill; outbreaks in Kerala and Bangladesh have been linked to eating fruit bitten by bats or drinking raw date-palm sap, so the answer lies in managing contact, not in killing bats, whose dispersal can spread the virus further. "
  "Statement 3 is wrong: bats are the only mammals that truly fly; flying squirrels only glide on skin flaps stretched between their limbs.",
  "कथन 1 और 2 सही हैं। फल चमगादड़ सेमल और जंगली केले जैसे वृक्षों का परागण करते हैं और बीज मूल वृक्ष से दूर, प्रायः साफ़ की गई भूमि के पार, गिराते हैं, जो उन्हें वन-पुनर्जनन के लिए महत्वपूर्ण बनाता है। भारतीय फ़्लाइंग फ़ॉक्स बिना बीमार हुए निपाह वायरस वहन करता है; केरल और बांग्लादेश में प्रकोपों को चमगादड़ों द्वारा कुतरे गए फल खाने या कच्चा खजूर-रस पीने से जोड़ा गया है, इसलिए उपाय संपर्क को सँभालने में है, चमगादड़ों को मारने में नहीं, जिससे उनके बिखरने से वायरस और फैल सकता है। "
  "कथन 3 गलत है: चमगादड़ ही वास्तव में उड़ने वाले स्तनधारी हैं; उड़न गिलहरियाँ अपने अंगों के बीच फैली त्वचा की झिल्लियों पर केवल फिसलती (ग्लाइड करती) हैं।",
  "Indian Council of Medical Research -- Nipah virus surveillance.",
  "env-fruit-bats-nipah", craft="linkage")

S(FAU, "medium", "Consider the following statements about the Amur falcon:",
  "अमूर बाज़ के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Its migration from breeding grounds in south-eastern Siberia and northern China to southern Africa passes through north-eastern India, where huge flocks rest in autumn.",
   "After large-scale trapping of the birds at the Doyang reservoir in Nagaland came to light in 2012, community action turned villages such as Pangti into centres of their protection.",
   "During its stay in India it feeds mainly on insects such as termites."],
  ["दक्षिण-पूर्वी साइबेरिया और उत्तरी चीन के प्रजनन क्षेत्रों से दक्षिणी अफ़्रीका तक इसका प्रवास उत्तर-पूर्वी भारत से होकर गुज़रता है, जहाँ शरद ऋतु में विशाल झुंड विश्राम करते हैं।",
   "2012 में नागालैंड के दोयांग जलाशय पर इन पक्षियों को बड़े पैमाने पर पकड़े जाने का पता चलने के बाद सामुदायिक प्रयासों ने पांगती जैसे गाँवों को इनके संरक्षण के केंद्र बना दिया।",
   "भारत में अपने ठहराव के दौरान यह मुख्यतः दीमक जैसे कीटों पर भोजन करता है।"],
  C3, 2,
  "All three are correct. The Amur falcon makes one of the longest migrations of any raptor, including a non-stop crossing of the Arabian Sea, and in October-November flocks of hundreds of thousands gather around Doyang in Wokha district. When reports in 2012 showed tens of thousands being trapped for meat, the Naga villagers, churches and the State government turned to protection, and the falcons are now celebrated and studied with satellite tags. "
  "They fatten on the swarms of winged termites and other insects of the season, which fuel the ocean crossing.",
  "तीनों कथन सही हैं। अमूर बाज़ किसी भी शिकारी पक्षी के सबसे लंबे प्रवासों में से एक करता है, जिसमें अरब सागर की बिना रुके यात्रा भी है, और अक्टूबर-नवंबर में वोखा ज़िले के दोयांग के आसपास लाखों के झुंड जमा होते हैं। जब 2012 की रिपोर्टों ने दिखाया कि दसियों हज़ार पक्षी मांस के लिए पकड़े जा रहे हैं, तो नगा ग्रामीण, चर्च और राज्य सरकार संरक्षण की ओर मुड़े, और अब इन बाज़ों का उत्सव मनाया जाता है और उपग्रह-टैग से इनका अध्ययन होता है। "
  "वे मौसम के पंखदार दीमकों और अन्य कीटों के झुंडों पर पलकर मोटे होते हैं, जो समुद्र पार करने की ऊर्जा देते हैं।",
  WII, "env-amur-falcon", craft="linkage")

S(FAU, "medium", "Consider the following statements about the dugong:",
  "डुगोंग के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Because it feeds only on seagrass, its survival in India depends on the seagrass meadows of the Gulf of Mannar, Palk Bay, the Gulf of Kutch and the Andamans.",
   "It breeds slowly, with a single calf every few years, so even small losses are hard to make good.",
   "India's first Dugong Conservation Reserve was notified in Palk Bay, off Tamil Nadu.",
   "Its closest living relatives are the dolphins and whales."],
  ["चूँकि यह केवल समुद्री घास खाता है, इसलिए भारत में इसका अस्तित्व मन्नार की खाड़ी, पाक खाड़ी, कच्छ की खाड़ी और अंडमान के समुद्री घास के मैदानों पर निर्भर है।",
   "यह धीरे प्रजनन करता है, कुछ वर्षों में एक बच्चा, इसलिए छोटी हानियाँ भी भरना कठिन है।",
   "भारत का पहला डुगोंग संरक्षण रिज़र्व तमिलनाडु के तट पर पाक खाड़ी में अधिसूचित किया गया।",
   "इसके सबसे निकट के जीवित संबंधी डॉल्फ़िन और व्हेल हैं।"],
  C4, 2,
  "Statements 1, 2 and 3 are correct. The dugong, or 'sea cow', grazes seagrass meadows, so trawling, dredging and pollution that destroy seagrass also starve it; a female produces a single calf only every few years, so accidental drowning in nets and poaching quickly push numbers down. Tamil Nadu notified the Dugong Conservation Reserve in Palk Bay in 2022, and the species is in Schedule I. "
  "Statement 4 is wrong: dugongs and manatees (the sirenians) are most closely related to elephants, not to the whales and dolphins.",
  "कथन 1, 2 और 3 सही हैं। 'समुद्री गाय' डुगोंग समुद्री घास के मैदान चरता है, इसलिए समुद्री घास को नष्ट करने वाले ट्रॉलिंग, ड्रेजिंग और प्रदूषण उसे भूखा भी मारते हैं; मादा कुछ वर्षों में केवल एक बच्चा देती है, इसलिए जालों में दुर्घटनावश डूबना और शिकार संख्या को जल्दी घटा देते हैं। तमिलनाडु ने 2022 में पाक खाड़ी में डुगोंग संरक्षण रिज़र्व अधिसूचित किया, और यह प्रजाति अनुसूची I में है। "
  "कथन 4 गलत है: डुगोंग और मैनेटी (साइरेनियन) व्हेल और डॉल्फ़िन से नहीं, बल्कि हाथियों से सबसे निकट से संबंधित हैं।",
  IUCN, "env-dugong", craft="linkage")

S(FAU, "medium", "Consider the following statements about the great hornbill:",
  "बड़े धनेश (ग्रेट हॉर्नबिल) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Because the female seals herself inside a cavity in a large old tree to nest, the felling of big trees hits its breeding hard.",
   "As a disperser of the seeds of large-fruited forest trees, its decline affects the regeneration of those trees.",
   "In India it is found both in the Western Ghats and in north-eastern India.",
   "It is listed as Vulnerable on the IUCN Red List."],
  ["चूँकि घोंसला बनाने के लिए मादा स्वयं को एक बड़े पुराने वृक्ष की खोह में बंद कर लेती है, इसलिए बड़े वृक्षों की कटाई इसके प्रजनन पर भारी पड़ती है।",
   "बड़े फलों वाले वन-वृक्षों के बीज फैलाने वाला होने के कारण इसके घटने से उन वृक्षों का पुनर्जनन प्रभावित होता है।",
   "भारत में यह पश्चिमी घाट और उत्तर-पूर्वी भारत दोनों में मिलता है।",
   "यह IUCN रेड लिस्ट में 'सुभेद्य' (Vulnerable) है।"],
  C4, 3,
  "All four are correct. The female walls herself into a natural cavity with mud and droppings, moults and depends on the male, who feeds her through a slit, until the chicks are half-grown; only big old trees have cavities large enough, so logging removes nest sites. Eating figs and other large fruits and flying long distances, hornbills carry seeds that few other birds can swallow, so they are called 'farmers of the forest'. "
  "The great hornbill lives in the Western Ghats and the north-east, and is Vulnerable, threatened by habitat loss and hunting for its casque and feathers.",
  "चारों कथन सही हैं। मादा मिट्टी और बीट से स्वयं को एक प्राकृतिक खोह में बंद कर लेती है, पंख झाड़ती है और नर पर निर्भर रहती है, जो एक दरार से उसे खिलाता है, जब तक बच्चे आधे बड़े न हो जाएँ; केवल बड़े पुराने वृक्षों में पर्याप्त बड़ी खोहें होती हैं, इसलिए कटाई घोंसले के स्थान छीन लेती है। अंजीर और अन्य बड़े फल खाकर और लंबी दूरी उड़कर धनेश वे बीज ले जाते हैं जिन्हें कुछ ही अन्य पक्षी निगल सकते हैं, इसलिए इन्हें 'वन के किसान' कहा जाता है। "
  "बड़ा धनेश पश्चिमी घाट और उत्तर-पूर्व में रहता है, और 'सुभेद्य' है, जिसे आवास-हानि और उसकी चोंच-कलगी तथा पंखों के लिए शिकार से ख़तरा है।",
  IUCN, "env-great-hornbill", craft="linkage")

S(FAU, "medium", "A solar park with overhead transmission lines is planned across the Thar grasslands where the Great Indian Bustard lives. Consider the following statements:",
  "थार के उन घास के मैदानों में, जहाँ सोन चिरैया (ग्रेट इंडियन बस्टर्ड) रहती है, ऊपरी पारेषण लाइनों वाला एक सौर पार्क प्रस्तावित है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The power lines would be a serious danger, since the heavy, low-flying bustard, with poor frontal vision, often collides with them.",
   "Since the bustard lays large clutches of eggs, such losses would quickly be made good."],
  ["बिजली की लाइनें गंभीर ख़तरा होंगी, क्योंकि भारी, नीची उड़ान भरने वाली और सामने कम देख पाने वाली यह चिड़िया प्रायः उनसे टकरा जाती है।",
   "चूँकि यह चिड़िया एक बार में कई अंडे देती है, इसलिए ऐसी हानियाँ जल्दी भर जाएँगी।"],
  T2, 0,
  "Only statement 1 is correct. Studies by the Wildlife Institute of India found collisions with power lines to be a leading cause of death of the Great Indian Bustard, which cannot see wires ahead in time and cannot manoeuvre quickly; this has made the routing of lines a central issue in planning renewable energy in its habitat. "
  "Statement 2 is wrong: a female usually lays a single egg, and the bird matures slowly, so with a population of only around 150, every adult lost is hard to replace -- which is why it is Critically Endangered and the focus of a captive-breeding programme.",
  "केवल कथन 1 सही है। भारतीय वन्यजीव संस्थान के अध्ययनों ने बिजली की लाइनों से टकराव को सोन चिरैया की मृत्यु का प्रमुख कारण पाया, जो सामने के तार समय पर नहीं देख पाती और जल्दी मुड़ नहीं पाती; इसी कारण उसके आवास में नवीकरणीय ऊर्जा की योजना में लाइनों का मार्ग एक केंद्रीय मुद्दा बना है। "
  "कथन 2 गलत है: मादा प्रायः एक ही अंडा देती है, और पक्षी धीरे परिपक्व होता है, इसलिए लगभग 150 की आबादी में हर खोया वयस्क भरना कठिन है; इसीलिए यह 'गंभीर रूप से संकटग्रस्त' है और बंदी-प्रजनन कार्यक्रम का केंद्र है।",
  WII, "env-great-indian-bustard-powerlines", craft="application")

S(FAU, "medium", "Consider the following statements about horseshoe crabs:",
  "हॉर्सशू केकड़ों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["They are more closely related to spiders and scorpions than to true crabs.",
   "Their blue, copper-based blood yields an extract used to test vaccines and medical devices for bacterial toxins, so large-scale harvesting is a conservation concern.",
   "In India they are found only around the Andaman and Nicobar Islands."],
  ["वे असली केकड़ों की तुलना में मकड़ियों और बिच्छुओं से अधिक निकट से संबंधित हैं।",
   "उनके नीले, ताँबा-आधारित रक्त से एक अर्क मिलता है जिससे टीकों और चिकित्सा उपकरणों में जीवाणु-विष की जाँच होती है, इसलिए बड़े पैमाने पर उनका संग्रह संरक्षण की चिंता है।",
   "भारत में वे केवल अंडमान और निकोबार द्वीपसमूह के आसपास मिलते हैं।"],
  C3, 1,
  "Statements 1 and 2 are correct. Horseshoe crabs are chelicerates, 'living fossils' little changed for some 450 million years. Their blood carries oxygen with haemocyanin, a copper protein, which makes it blue, and the amoebocyte lysate made from it clots in the presence of bacterial endotoxins, which made it the standard purity test for injectable drugs and vaccines; crabs are bled and returned, but many die, and synthetic substitutes are being promoted. "
  "Statement 3 is wrong: in India they breed mainly on the coasts of Odisha and West Bengal, as at Balasore.",
  "कथन 1 और 2 सही हैं। हॉर्सशू केकड़े कीलेसेरेट हैं, लगभग 45 करोड़ वर्षों से बहुत कम बदले 'जीवित जीवाश्म'। उनका रक्त ताँबे के प्रोटीन हीमोसायनिन से ऑक्सीजन ढोता है, जिससे वह नीला होता है, और उससे बना अमीबोसाइट लाइसेट जीवाणु-एंडोटॉक्सिन की उपस्थिति में जम जाता है, जिससे यह इंजेक्शन वाली दवाओं और टीकों की शुद्धता की मानक जाँच बना; केकड़ों का रक्त निकालकर उन्हें लौटा दिया जाता है, पर कई मर जाते हैं, और कृत्रिम विकल्पों को बढ़ावा दिया जा रहा है। "
  "कथन 3 गलत है: भारत में वे मुख्यतः ओडिशा और पश्चिम बंगाल के तटों पर, जैसे बालासोर में, प्रजनन करते हैं।",
  IUCN, "env-horseshoe-crab", craft="linkage")

S(FAU, "medium", "A crocodilian with a long, narrow snout lined with small interlocking teeth feeds on fish in fast-flowing rivers; the adult male has a pot-like knob at the tip of its snout. Consider the following statements:",
  "छोटे गुँथे दाँतों वाली लंबी, पतली थूथन वाला एक मगरमच्छ-वर्गीय जीव तेज़ बहती नदियों में मछली खाता है; वयस्क नर की थूथन के सिरे पर घड़े जैसा उभार होता है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The animal is the gharial.",
   "Its largest wild population is in the National Chambal Sanctuary, spread across Rajasthan, Madhya Pradesh and Uttar Pradesh.",
   "It is the crocodilian of the mangrove creeks of Bhitarkanika in Odisha."],
  ["यह जीव घड़ियाल है।",
   "इसकी सबसे बड़ी जंगली समष्टि राजस्थान, मध्य प्रदेश और उत्तर प्रदेश में फैले राष्ट्रीय चंबल अभयारण्य में है।",
   "यह ओडिशा के भितरकनिका की मैंग्रोव खाड़ियों का मगरमच्छ है।"],
  C3, 1,
  "Statements 1 and 2 are correct. The slender snout is an adaptation for catching fish with a sideways sweep, and the 'ghara' (pot) on the male's snout gives the gharial its name. It is Critically Endangered, and the Chambal, one of India's least polluted large rivers, holds most of the surviving wild population, with smaller groups in the Girwa, the Son and Nepal's rivers. "
  "Statement 3 is wrong: the mangrove creeks of Bhitarkanika, the Sundarbans and the Andamans are home to the saltwater crocodile; the third Indian species, the mugger, lives in lakes, rivers and marshes across the country.",
  "कथन 1 और 2 सही हैं। पतली थूथन एक ओर से झटके में मछली पकड़ने का अनुकूलन है, और नर की थूथन पर 'घड़ा' घड़ियाल को उसका नाम देता है। यह 'गंभीर रूप से संकटग्रस्त' है, और भारत की सबसे कम प्रदूषित बड़ी नदियों में से एक, चंबल, बची हुई जंगली समष्टि का अधिकांश भाग रखती है, और छोटे समूह गिरवा, सोन और नेपाल की नदियों में हैं। "
  "कथन 3 गलत है: भितरकनिका, सुंदरबन और अंडमान की मैंग्रोव खाड़ियाँ खारे पानी के मगरमच्छ का घर हैं; तीसरी भारतीय प्रजाति, मगर, पूरे देश की झीलों, नदियों और दलदलों में रहती है।",
  IUCN, "env-indian-crocodilians", craft="application")

S(FAU, "medium", "Consider the following statements about the Indian pangolin:",
  "भारतीय पैंगोलिन के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Its habit of rolling into a ball, which protects it from big cats, makes it easy for poachers to pick up.",
   "Pangolins are found only in Africa.",
   "It feeds mainly on fruits and seeds."],
  ["गेंद की तरह लिपट जाने की इसकी आदत, जो इसे बड़ी बिल्लियों से बचाती है, शिकारियों के लिए इसे उठाना आसान बना देती है।",
   "पैंगोलिन केवल अफ़्रीका में मिलते हैं।",
   "यह मुख्यतः फल और बीज खाता है।"],
  C3, 0,
  "Only statement 1 is correct. The overlapping keratin scales and the tight ball defeat a leopard's teeth but not a human hand, so pangolins are simply picked up; demand for scales in traditional medicine and for meat has made them among the most trafficked mammals, and all eight species were moved to CITES Appendix I in 2016. "
  "Statement 2 is wrong: four species live in Asia, including the Indian and Chinese pangolins found in India, and four in Africa. Statement 3 is wrong: pangolins eat ants and termites, tearing open nests with their claws and licking up the insects with a long sticky tongue.",
  "केवल कथन 1 सही है। एक-दूसरे पर चढ़े केराटिन के शल्क और कसी हुई गेंद तेंदुए के दाँतों को तो हरा देते हैं, पर मनुष्य के हाथ को नहीं, इसलिए पैंगोलिन बस उठा लिए जाते हैं; पारंपरिक औषधि के लिए शल्कों और मांस की माँग ने उन्हें सबसे अधिक तस्करी वाले स्तनधारियों में ला दिया है, और 2016 में सभी आठ प्रजातियाँ CITES परिशिष्ट I में ले जाई गईं। "
  "कथन 2 गलत है: चार प्रजातियाँ एशिया में रहती हैं, जिनमें भारत में मिलने वाले भारतीय और चीनी पैंगोलिन हैं, और चार अफ़्रीका में। कथन 3 गलत है: पैंगोलिन चींटियाँ और दीमक खाते हैं, पंजों से घोंसले फाड़कर लंबी चिपचिपी जीभ से कीट चाटते हैं।",
  IUCN, "env-indian-pangolin", craft="linkage")

S(FAU, "medium", "Consider the following statements about the leatherback turtle:",
  "लेदरबैक कछुए के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Because it feeds mainly on jellyfish, it is harmed by floating plastic bags, which it mistakes for food.",
   "In India it nests on the beaches of the Andaman and Nicobar Islands, including Great Nicobar.",
   "It has the hardest shell of all turtles."],
  ["चूँकि यह मुख्यतः जेलीफ़िश खाता है, इसलिए तैरते प्लास्टिक के थैले इसे हानि पहुँचाते हैं, जिन्हें यह भोजन समझ लेता है।",
   "भारत में यह ग्रेट निकोबार सहित अंडमान और निकोबार द्वीपसमूह के समुद्र-तटों पर घोंसले बनाता है।",
   "इसका कवच सभी कछुओं में सबसे कठोर है।"],
  C3, 1,
  "Statements 1 and 2 are correct. The leatherback, the largest living turtle, lives almost entirely on jellyfish, and plastic bags drifting in the sea look much like them; swallowed plastic blocks the gut. Its Indian nesting beaches are in the Andaman and Nicobar Islands, such as Galathea Bay on Great Nicobar, which is why development plans there raise concern. "
  "Statement 3 is wrong: unlike other sea turtles it has no hard shell; its carapace is a leathery skin over a mosaic of small bones, which gives it its name.",
  "कथन 1 और 2 सही हैं। सबसे बड़ा जीवित कछुआ, लेदरबैक, लगभग पूरी तरह जेलीफ़िश पर जीता है, और समुद्र में बहते प्लास्टिक के थैले उनके जैसे ही दिखते हैं; निगला गया प्लास्टिक आँत रोक देता है। इसके भारतीय घोंसला-तट अंडमान और निकोबार द्वीपसमूह में हैं, जैसे ग्रेट निकोबार का गलाथिया खाड़ी, इसीलिए वहाँ की विकास योजनाएँ चिंता जगाती हैं। "
  "कथन 3 गलत है: अन्य समुद्री कछुओं के विपरीत इसका कोई कठोर कवच नहीं है; इसका पृष्ठ-कवच छोटी हड्डियों के जाल पर चमड़े जैसी त्वचा है, जिससे इसे यह नाम मिला।",
  IUCN, "env-leatherback-turtle", craft="linkage")

S(FAU, "medium", "Consider the following statements about the olive ridley turtle:",
  "ऑलिव रिडले कछुए के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is known for 'arribada', a synchronised mass nesting in which thousands of females come ashore together.",
   "Since females return to nest on or near the beach where they hatched, the loss of a mass-nesting beach is not easily replaced by other sites.",
   "Gahirmatha in Odisha is among its largest mass-nesting sites in the world."],
  ["यह 'अरिबाडा' के लिए जाना जाता है, एक साथ सामूहिक घोंसला-निर्माण जिसमें हज़ारों मादाएँ एक साथ तट पर आती हैं।",
   "चूँकि मादाएँ उसी तट पर या उसके निकट घोंसला बनाने लौटती हैं जहाँ वे जन्मी थीं, इसलिए किसी सामूहिक घोंसला-तट की हानि की भरपाई अन्य स्थल जल्दी नहीं कर पाते।",
   "ओडिशा का गहिरमाथा संसार में इसके सबसे बड़े सामूहिक घोंसला-स्थलों में से है।"],
  C3, 2,
  "All three are correct. Olive ridleys gather offshore from November and come ashore en masse, usually in February and March, at Gahirmatha, the mouth of the Rushikulya and the Devi river mouth in Odisha, among the largest such rookeries in the world. Sea turtles show natal homing: after years at sea, females navigate back to the stretch of coast where they hatched, so a rookery lost to erosion, sand-mining, ports or lights is not simply replaced by another beach; this is why the few Odisha rookeries are guarded so closely, and fishing is banned close to the nesting coast from November to May. "
  "Like every sea turtle in Indian waters, it is in Schedule I of the Wild Life (Protection) Act.",
  "तीनों कथन सही हैं। ऑलिव रिडले नवंबर से समुद्र में एकत्र होकर, प्रायः फ़रवरी और मार्च में, ओडिशा के गहिरमाथा, रुशिकुल्या के मुहाने और देवी नदी के मुहाने पर सामूहिक रूप से तट पर आते हैं, जो संसार के सबसे बड़े ऐसे स्थलों में हैं। समुद्री कछुओं में जन्म-स्थल पर लौटने की प्रवृत्ति (नेटल होमिंग) होती है: वर्षों समुद्र में रहने के बाद मादाएँ उसी तट-खंड पर लौटती हैं जहाँ वे जन्मी थीं, इसलिए कटाव, रेत-खनन, बंदरगाहों या रोशनी से नष्ट हुआ घोंसला-स्थल किसी अन्य तट से सहज ही नहीं बदला जाता; इसीलिए ओडिशा के गिने-चुने घोंसला-स्थलों की इतनी कड़ी रक्षा होती है, और नवंबर से मई तक घोंसला-तट के निकट मछली पकड़ने पर रोक रहती है। "
  "भारतीय जल के हर समुद्री कछुए की तरह यह वन्यजीव (संरक्षण) अधिनियम की अनुसूची I में है।",
  WPA, "env-olive-ridley-arribada", craft="linkage")

S(FAU, "medium", "Consider the following statements about the purple frog (Nasikabatrachus sahyadrensis):",
  "बैंगनी मेंढक (नासिकाबैट्रेकस सह्याद्रेंसिस) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Its closest living relatives are found in the Seychelles, a relic of the time when India and the Seychelles were joined.",
   "It spends most of the year in tree holes high in the forest canopy.",
   "It is endemic to the eastern Himalaya."],
  ["इसके सबसे निकट के जीवित संबंधी सेशेल्स में मिलते हैं, जो उस समय का अवशेष है जब भारत और सेशेल्स जुड़े थे।",
   "यह वर्ष का अधिकांश भाग वन-छत्र में ऊँचे वृक्षों की खोहों में बिताता है।",
   "यह पूर्वी हिमालय का स्थानिक है।"],
  C3, 0,
  "Only statement 1 is correct. Described only in 2003, the purple frog belongs to a lineage that split from its Seychelles relatives when the land masses separated after the break-up of Gondwana, so it is a 'living fossil' of that geological history. "
  "Statement 2 is wrong: it lives several metres underground for most of the year, feeding on termites with its pointed snout, and emerges for only a few days in the monsoon to breed in seasonal streams. Statement 3 is wrong: it is endemic to the Western Ghats, which is why it is cited as an example of the region's ancient, unique fauna.",
  "केवल कथन 1 सही है। केवल 2003 में वर्णित बैंगनी मेंढक उस वंश का है जो गोंडवाना के टूटने के बाद भू-भागों के अलग होने पर अपने सेशेल्स के संबंधियों से अलग हुआ, इसलिए यह उस भूगर्भीय इतिहास का 'जीवित जीवाश्म' है। "
  "कथन 2 गलत है: यह वर्ष का अधिकांश भाग कई मीटर भूमिगत रहता है, अपनी नुकीली थूथन से दीमक खाता है, और मानसून में केवल कुछ दिनों के लिए मौसमी धाराओं में प्रजनन करने निकलता है। कथन 3 गलत है: यह पश्चिमी घाट का स्थानिक है, इसीलिए इसे इस क्षेत्र के प्राचीन, अनोखे जीव-जगत के उदाहरण के रूप में उद्धृत किया जाता है।",
  IUCN, "env-purple-frog", craft="linkage")

# ================================================================ FLORA (6)
S(FLO, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Bryophytes need water for fertilisation because their sperm must swim to the egg, which is why they are called the amphibians of the plant kingdom.",
   "Ferns reproduce by seeds."],
  ["ब्रायोफ़ाइट को निषेचन के लिए जल चाहिए क्योंकि उनके शुक्राणुओं को तैरकर अंड तक पहुँचना होता है, इसीलिए उन्हें पादप-जगत के उभयचर कहा जाता है।",
   "फ़र्न बीजों से प्रजनन करते हैं।"],
  T2, 0,
  "Only statement 1 is correct. Mosses and liverworts live on land but depend on a film of water for their swimming sperm to reach the egg, much as frogs return to water to breed; with lichens they are among the first colonisers of bare rock. "
  "Statement 2 is wrong: ferns, like other pteridophytes, reproduce by spores, which are carried on the underside of their leaves; seeds belong to gymnosperms and flowering plants.",
  "केवल कथन 1 सही है। मॉस और लिवरवर्ट भूमि पर रहते हैं, पर उनके तैरने वाले शुक्राणुओं को अंड तक पहुँचने के लिए जल की परत चाहिए, ठीक वैसे ही जैसे मेंढक प्रजनन के लिए जल में लौटते हैं; लाइकेन के साथ वे नंगी चट्टान पर बसने वाले पहले जीवों में हैं। "
  "कथन 2 गलत है: अन्य टेरिडोफ़ाइट की तरह फ़र्न बीजाणुओं से प्रजनन करते हैं, जो उनकी पत्तियों के नीचे होते हैं; बीज अनावृतबीजियों और पुष्पी पौधों के होते हैं।",
  NB11, "env-bryophytes-ferns", craft="linkage")

S(FLO, "easy", "Consider the following statements about the Khejri tree (Prosopis cineraria):",
  "खेजड़ी वृक्ष (प्रोसोपिस सिनेरेरिया) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is the State tree of Gujarat.",
   "It was introduced into the Thar Desert from Mexico.",
   "The sacrifice of 1730 at Khejarli, in which more than 360 villagers died, was made to protect sal trees."],
  ["यह गुजरात का राज्य वृक्ष है।",
   "इसे मेक्सिको से थार मरुस्थल में लाया गया।",
   "1730 में खेजड़ली का बलिदान, जिसमें 360 से अधिक ग्रामीण मारे गए, साल वृक्षों की रक्षा के लिए था।"],
  C3, 3,
  "None is correct. Khejri is the State tree of Rajasthan (Gujarat's is the banyan). It is native to the Thar, where its deep roots, nitrogen-fixing ability, fodder leaves and edible pods make farmers keep it standing in their fields; the species brought in from the Americas is a different Prosopis, P. juliflora. "
  "The Khejarli sacrifice of 1730, in which Amrita Devi and 363 Bishnois gave their lives, was to save khejri trees from being cut for the Maharaja of Jodhpur.",
  "कोई भी कथन सही नहीं है। खेजड़ी राजस्थान का राज्य वृक्ष है (गुजरात का बरगद है)। यह थार का मूल वृक्ष है, जहाँ इसकी गहरी जड़ें, नाइट्रोजन-स्थिरीकरण की क्षमता, चारे वाली पत्तियाँ और खाने योग्य फलियाँ किसानों को इसे खेतों में खड़ा रखने को प्रेरित करती हैं; अमेरिका से लाई गई प्रजाति एक अलग प्रोसोपिस, पी. जूलीफ़्लोरा, है। "
  "1730 का खेजड़ली बलिदान, जिसमें अमृता देवी और 363 बिश्नोइयों ने प्राण दिए, जोधपुर के महाराजा के लिए खेजड़ी के वृक्ष कटने से बचाने के लिए था।",
  "Rajasthan Forest Department.",
  "env-khejri", craft="precision")

S(FLO, "hard", "Consider the following statements about invasive plants in India:",
  "भारत में आक्रामक पौधों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Lantana camara, brought in as a garden plant, now covers large areas of forest, suppressing native plants and the grasses that herbivores need.",
   "Prosopis juliflora, planted to green dry lands and supply fuelwood, has spread aggressively over grasslands such as Banni in Kutch.",
   "Water hyacinth chokes lakes and rivers, cutting off light and oxygen for aquatic life.",
   "Parthenium hysterophorus is native to South-East Asia."],
  ["बगीचे के पौधे के रूप में लाया गया लैंटाना कैमारा अब वनों के बड़े क्षेत्रों पर छाया है, जो देशी पौधों और शाकाहारी जीवों के लिए आवश्यक घासों को दबाता है।",
   "शुष्क भूमि को हरा करने और ईंधन-लकड़ी के लिए लगाया गया प्रोसोपिस जूलीफ़्लोरा कच्छ के बन्नी जैसे घास के मैदानों पर आक्रामक रूप से फैल गया है।",
   "जलकुंभी झीलों और नदियों को अवरुद्ध करती है, जलीय जीवों के लिए प्रकाश और ऑक्सीजन रोक देती है।",
   "पार्थेनियम हिस्टेरोफ़ोरस दक्षिण-पूर्व एशिया का मूल पौधा है।"],
  C4, 2,
  "Statements 1, 2 and 3 are correct, and they show why invasive species are a leading driver of biodiversity loss: freed from the enemies of their home range, they spread fast and crowd out native species. Lantana, from tropical America, forms dense thickets in tiger reserves and elephant habitat; Prosopis juliflora (vilayati babul), from Mexico and Central America, has overrun the Banni grasslands and the Delhi Ridge; and water hyacinth, from South America, forms mats that block light, deplete oxygen and clog channels. "
  "Statement 4 is wrong: Parthenium (congress grass), a cause of allergies and crop losses, came from tropical America, probably with imported grain in the 1950s.",
  "कथन 1, 2 और 3 सही हैं, और दिखाते हैं कि आक्रामक प्रजातियाँ जैव विविधता की हानि का प्रमुख कारण क्यों हैं: अपने मूल क्षेत्र के शत्रुओं से मुक्त होकर वे तेज़ी से फैलती हैं और देशी प्रजातियों को बाहर कर देती हैं। उष्णकटिबंधीय अमेरिका का लैंटाना बाघ अभयारण्यों और हाथियों के आवासों में घनी झाड़ियाँ बनाता है; मेक्सिको और मध्य अमेरिका का प्रोसोपिस जूलीफ़्लोरा (विलायती बबूल) बन्नी के घास के मैदानों और दिल्ली रिज पर छा गया है; और दक्षिण अमेरिका की जलकुंभी ऐसी परतें बनाती है जो प्रकाश रोकती, ऑक्सीजन घटाती और नालियाँ अवरुद्ध करती हैं। "
  "कथन 4 गलत है: एलर्जी और फ़सल-हानि का कारण पार्थेनियम (कांग्रेस घास) उष्णकटिबंधीय अमेरिका से, संभवतः 1950 के दशक में आयातित अनाज के साथ, आया।",
  NB12, "env-invasive-plants", craft="linkage")

S(FLO, "medium", "Consider the following statements about forest produce in India:",
  "भारत में वन उपज के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Lac is secreted by a tiny insect that lives on host trees such as palash, kusum and ber, so lac cultivation depends on keeping those trees.",
   "Tendu leaves, used to roll bidis, come from the mahua tree.",
   "Kattha, eaten with paan, is obtained from the bark of the neem tree."],
  ["लाख एक छोटे कीट द्वारा स्रावित होती है जो पलाश, कुसुम और बेर जैसे परपोषी वृक्षों पर रहता है, इसलिए लाख की खेती उन वृक्षों को बचाए रखने पर निर्भर है।",
   "बीड़ी बनाने में प्रयुक्त तेंदू पत्ते महुआ वृक्ष से आते हैं।",
   "पान के साथ खाया जाने वाला कत्था नीम की छाल से प्राप्त होता है।"],
  C3, 0,
  "Only statement 1 is correct. Lac is the resinous secretion of the insect Kerria lacca, which is 'inoculated' onto host trees; Jharkhand is the largest producer, and lac gives forest-dwelling families an income that depends on the host trees staying healthy. "
  "Statement 2 is wrong: tendu leaves come from the tendu tree (Diospyros melanoxylon), whose leaf collection is a major seasonal livelihood in central India; mahua is valued for its flowers and seeds. Statement 3 is wrong: kattha (catechu) is extracted from the heartwood of the khair tree (Acacia catechu).",
  "केवल कथन 1 सही है। लाख केरिया लक्का कीट का राल-जैसा स्राव है, जिसे परपोषी वृक्षों पर 'बोया' जाता है; झारखंड सबसे बड़ा उत्पादक है, और लाख वनवासी परिवारों को ऐसी आय देती है जो परपोषी वृक्षों के स्वस्थ रहने पर निर्भर है। "
  "कथन 2 गलत है: तेंदू पत्ते तेंदू वृक्ष (डायोस्पायरोस मेलानॉक्सिलॉन) से आते हैं, जिनका संग्रह मध्य भारत में एक बड़ी मौसमी आजीविका है; महुआ अपने फूलों और बीजों के लिए मूल्यवान है। कथन 3 गलत है: कत्था खैर वृक्ष (अकेसिया कैटेचू) के अंतःकाष्ठ से निकाला जाता है।",
  "Indian Council of Forestry Research and Education.",
  "env-forest-produce-lac-kattha-tendu", craft="linkage")

S(FLO, "medium", "Consider the following statements about Neelakurinji (Strobilanthes kunthiana):",
  "नीलकुरिंजी (स्ट्रोबिलैंथेस कुंथियाना) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Because the plants flower together only about once in twelve years and then die, its mass blooms are rare events.",
   "Its mass flowering supports a surge in the production of a prized honey.",
   "It grows mainly in the sand dunes of the Thar Desert."],
  ["चूँकि पौधे लगभग बारह वर्ष में एक बार ही एक साथ फूलते हैं और फिर मर जाते हैं, इसलिए इसका सामूहिक खिलना दुर्लभ घटना है।",
   "इसका सामूहिक खिलना एक प्रसिद्ध शहद के उत्पादन में उछाल को सहारा देता है।",
   "यह मुख्यतः थार मरुस्थल के रेत के टीलों पर उगता है।"],
  C3, 1,
  "Statements 1 and 2 are correct. Like many Strobilanthes, Neelakurinji is monocarpic: whole populations grow for about twelve years, bloom together, set seed and die, so the hills turn blue only rarely -- the last great bloom around Munnar was in 2018. The flowering brings a burst of 'kurinji honey', long valued by the hill communities. "
  "Statement 3 is wrong: it grows in the shola-grassland landscape of the southern Western Ghats, around Munnar and in the Nilgiris, and the Kurinjimala Sanctuary in Kerala protects its habitat.",
  "कथन 1 और 2 सही हैं। कई स्ट्रोबिलैंथेस की तरह नीलकुरिंजी एकफली (मोनोकार्पिक) है: पूरी समष्टियाँ लगभग बारह वर्ष बढ़ती हैं, एक साथ खिलती हैं, बीज बनाती हैं और मर जाती हैं, इसलिए पहाड़ियाँ कभी-कभार ही नीली होती हैं; मुन्नार के आसपास पिछला बड़ा खिलना 2018 में हुआ। फूलने से 'कुरिंजी शहद' की बहुतायत होती है, जिसे पहाड़ी समुदाय लंबे समय से मूल्यवान मानते हैं। "
  "कथन 3 गलत है: यह दक्षिणी पश्चिमी घाट के शोला-घास भूदृश्य में, मुन्नार के आसपास और नीलगिरि में, उगता है, और केरल का कुरिंजीमला अभयारण्य इसके आवास की रक्षा करता है।",
  "Kerala Forest Department -- Kurinjimala Sanctuary.",
  "env-neelakurinji", craft="linkage")

S(FLO, "medium", "Consider the following statements about sacred groves in India:",
  "भारत में पवित्र उपवनों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Because they have been left uncut for generations for religious reasons, they often shelter plants and animals lost from the surrounding landscape.",
   "They are known by local names such as 'devrai' in Maharashtra, 'kavu' in Kerala and 'oran' in Rajasthan.",
   "Because many groves hold springs and streams at their heart, their loss can dry up the water sources of nearby villages."],
  ["चूँकि धार्मिक कारणों से इन्हें पीढ़ियों से नहीं काटा गया, इसलिए वे प्रायः ऐसे पौधों और जीवों को आश्रय देते हैं जो आसपास के भूदृश्य से लुप्त हो चुके हैं।",
   "इन्हें महाराष्ट्र में 'देवराई', केरल में 'कावु' और राजस्थान में 'ओरण' जैसे स्थानीय नामों से जाना जाता है।",
   "चूँकि कई उपवनों के मध्य में झरने और धाराएँ होती हैं, इसलिए उनके नष्ट होने से आसपास के गाँवों के जल-स्रोत सूख सकते हैं।"],
  C3, 2,
  "All three are correct. Sacred groves, dedicated to a local deity, have been protected by taboos on cutting or hunting, so in the Khasi and Jaintia Hills of Meghalaya, the Western Ghats and elsewhere they are often the last patches of old forest and hold rare and relict species. "
  "Their dense cover and deep leaf litter hold rainwater and feed springs and streams, so groves are often the water source of the villages around them; when they are cleared or encroached, those springs can fail.",
  "तीनों कथन सही हैं। स्थानीय देवता को समर्पित पवित्र उपवन काटने या शिकार पर निषेधों से सुरक्षित रहे हैं, इसलिए मेघालय की खासी और जयंतिया पहाड़ियों, पश्चिमी घाट और अन्यत्र वे प्रायः पुराने वन के अंतिम टुकड़े होते हैं और दुर्लभ तथा अवशेष प्रजातियाँ रखते हैं। "
  "उनका घना आवरण और पत्तियों की मोटी परत वर्षा-जल को रोककर झरनों और धाराओं को पोषित करते हैं, इसलिए उपवन प्रायः आसपास के गाँवों के जल-स्रोत होते हैं; उनके कटने या अतिक्रमण होने पर वे झरने सूख सकते हैं।",
  "C.P.R. Environmental Education Centre -- ENVIS Resource Partner on Conservation of Ecological Heritage and Sacred Sites of India.", "env-sacred-groves", craft="linkage")

# ================================================================ TAGS for the 76 kept rows (Test 21's 6 are tagged already)
TAGS = {
 "env-rainforest-soil-nutrients": "linkage", "env-ecology-terms-pairs": "precision", "env-seres-pairs": "precision",
 "env-species-interactions-pairs": "application", "env-ecosystem-term-tansley": "recall", "env-trophic-level-frog": "application",
 "env-species-area-relationship": "precision", "env-competitive-exclusion": "precision", "env-r-k-selection": "application",
 "env-phosphorus-nitrogen-cycles": "precision", "env-productivity-npp": "precision", "env-regulators-conformers-responses": "linkage",
 "env-age-pyramids": "inference", "env-decomposition-factors": "precision", "env-ecological-pyramids": "linkage",
 "env-ecotone-keystone": "precision", "env-energy-flow-food-chains": "precision", "env-latitudinal-diversity-gradient": "linkage",
 "env-limiting-factors-tolerance": "precision", "env-succession-hydrarch": "precision",
 "env-camel-hump-fat": "precision", "env-bar-headed-goose": "linkage", "env-arctic-fox-allens-rule": "linkage",
 "env-asiatic-lion-kuno": "precision", "env-sexual-dimorphism-birds": "linkage", "env-state-birds-pairs": "recall",
 "env-state-animals-pairs": "recall", "env-elephant-heritage-animal": "recall", "env-marsupials": "recall",
 "env-hangul-dachigam": "recall", "env-jacana-polyandry": "recall", "env-animal-tool-use": "recall",
 "env-clownfish-sex-change": "recall", "env-blackbuck": "recall", "env-echolocation": "precision",
 "env-indian-giant-squirrel": "recall", "env-indian-peafowl": "recall", "env-slender-loris-owls": "recall",
 "env-vultures-diclofenac": "linkage", "env-anadromous-catadromous": "precision", "env-bergmann-rule-adaptations": "linkage",
 "env-king-cobra": "recall", "env-rediscovered-birds": "recall", "env-aestivation-hibernation": "precision",
 "env-batesian-mullerian-mimicry": "precision", "env-hoolock-gibbon": "recall", "env-indian-wild-ass": "recall",
 "env-nilgiri-tahr-habitat": "recall", "env-red-panda": "recall", "env-sea-turtle-biology": "precision",
 "env-seahorse-male-pregnancy": "recall", "env-sloth-bear": "recall", "env-snow-leopard-spai": "recall",
 "env-lichen-pioneer": "linkage", "env-himalayan-yew-taxol": "linkage", "env-deciduous-leaf-fall-teak": "linkage",
 "env-venus-flytrap": "recall", "env-medicinal-plants-pairs": "recall", "env-brahma-kamal": "recall",
 "env-largest-flower-rafflesia": "recall", "env-gymnosperm-groups": "application", "env-not-a-fungus-spirulina": "application",
 "env-seagrass-angiosperm": "precision", "env-pollination-dispersal": "precision", "env-xerophyte-adaptations": "linkage",
 "env-c3-c4-cam-plants": "precision", "env-forest-fire-ecology": "linkage", "env-sandalwood-cycas": "precision",
 "env-bamboo-mautam": "precision", "env-epiphyte-vs-parasite": "precision", "env-fungi-mycorrhiza-trichoderma": "precision",
 "env-himalayan-vegetation-zones": "precision", "env-insectivorous-plants": "linkage", "env-mangrove-adaptations": "linkage",
 "env-shola-grasslands": "linkage", "env-tropical-evergreen-forests": "precision"}

if __name__ == "__main__":
    write_updates("upg_l2_t09_env.sql", statuses=("draft", "published"), tags=TAGS)
