# -*- coding: utf-8 -*-
"""Level 2 · Test 12 (Geography 1: World Physical Geography) -- World Regions, Water Bodies & Places:
36 new bilingual rows against the live gap report: medium statement 11, medium MCQ 5, hard statement 4,
medium Statement-I/II 4, easy statement 3, easy MCQ 2, hard MCQ 2, medium pairs 2, easy
Statement-I/II 1, hard I/II/III 1, hard pairs 1.
The bank already asks which countries border the Caspian (Azerbaijan, Georgia, Iran, Uzbekistan), so
Georgia and the Caspian coast are left alone; Kazakhstan appears only once for the same reason.
West-coast deserts and ocean salinity are tested in the Oceanography rows, so the desert row avoids
the Namib and Atacama and nothing here turns on river water diluting the sea."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Geography"
WR = "World Regions, Water Bodies & Places"
NC11 = "NCERT Class XI, Fundamentals of Physical Geography"
NC7 = "NCERT Class VII, Our Environment"
NC6 = "NCERT Class VI, The Earth: Our Habitat"
ATLAS = "Oxford School Atlas"
HOW_MANY_C = "How many of the above countries"

# ================================================================ MEDIUM STATEMENTS (11)
S(WR, "medium", "Consider the following countries:",
  "निम्नलिखित देशों पर विचार कीजिए:",
  ["Bulgaria", "Romania", "Moldova", "Serbia"],
  ["बुल्गारिया", "रोमानिया", "मोल्दोवा", "सर्बिया"],
  C4, 1,
  "Only Bulgaria and Romania have a Black Sea coast; the other countries on it are Turkey, Georgia, Russia and Ukraine. "
  "Moldova is the trap: it lies between Romania and Ukraine and very close to the sea, but it is landlocked -- its only outlet is a few hundred metres of bank on the Danube. Serbia is landlocked too; the Danube carries its trade to the Black Sea.",
  "केवल बुल्गारिया और रोमानिया की तटरेखा काला सागर पर है; इस पर स्थित अन्य देश तुर्किये, जॉर्जिया, रूस और यूक्रेन हैं। "
  "मोल्दोवा ही जाल है: यह रोमानिया और यूक्रेन के बीच और समुद्र के बहुत पास है, पर स्थलरुद्ध (landlocked) है; उसका एकमात्र निकास डेन्यूब के किनारे का कुछ सौ मीटर का भाग है। सर्बिया भी स्थलरुद्ध है; उसका व्यापार डेन्यूब के रास्ते काला सागर तक जाता है।",
  f"{ATLAS} -- Europe (political).",
  "geo-black-sea-coast-countries",
  closing=f"{HOW_MANY_C} have a coastline on the Black Sea?",
  closing_hi="उपर्युक्त में से कितने देशों की तटरेखा काला सागर पर है?")

S(WR, "medium", "Consider the following statements about seas of Europe:",
  "यूरोप के सागरों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Adriatic Sea lies between Italy and the Balkan Peninsula.",
   "The Aegean Sea lies between Greece and Turkey.",
   "The Sea of Azov is connected to the Black Sea by the Kerch Strait."],
  ["एड्रियाटिक सागर इटली और बाल्कन प्रायद्वीप के बीच स्थित है।",
   "एजियन सागर यूनान (ग्रीस) और तुर्किये के बीच स्थित है।",
   "अज़ोव सागर केर्च जलडमरूमध्य द्वारा काला सागर से जुड़ा है।"],
  C3, 2,
  "All three statements are correct. The Adriatic separates Italy from the Balkan coast of Slovenia, Croatia, Montenegro and Albania; the island-dotted Aegean lies between Greece and Turkey; and the shallow Sea of Azov, the shallowest sea in the world, opens into the Black Sea through the Kerch Strait, between Crimea and Russia's Taman Peninsula.",
  "तीनों कथन सही हैं। एड्रियाटिक इटली को स्लोवेनिया, क्रोएशिया, मोंटेनेग्रो और अल्बानिया के बाल्कन तट से अलग करता है; द्वीपों से भरा एजियन यूनान और तुर्किये के बीच है; और उथला अज़ोव सागर, जो विश्व का सबसे उथला सागर है, क्रीमिया और रूस के तामान प्रायद्वीप के बीच केर्च जलडमरूमध्य से होकर काला सागर में खुलता है।",
  f"{ATLAS} -- Europe (physical).",
  "geo-europe-seas-adriatic-aegean-azov")

S(WR, "medium", "Consider the following statements about rivers of Europe:",
  "यूरोप की नदियों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Danube flows through more countries than any other river in the world.",
   "The Rhine flows into the Baltic Sea.",
   "The Tagus flows into the Mediterranean Sea."],
  ["डेन्यूब विश्व की किसी भी अन्य नदी की तुलना में अधिक देशों से होकर बहती है।",
   "राइन बाल्टिक सागर में गिरती है।",
   "टैगस भूमध्य सागर में गिरती है।"],
  C3, 0,
  "Only statement 1 is correct: the Danube rises in Germany's Black Forest and flows through or along ten countries -- Germany, Austria, Slovakia, Hungary, Croatia, Serbia, Romania, Bulgaria, Moldova and Ukraine -- before reaching the Black Sea. "
  "Statement 2 is wrong: the Rhine rises in the Swiss Alps and enters the North Sea through the Netherlands, where Rotterdam stands on its delta. "
  "Statement 3 is wrong: the Tagus, the longest river of the Iberian Peninsula, flows west across Spain and Portugal into the Atlantic at Lisbon.",
  "केवल कथन 1 सही है: डेन्यूब जर्मनी के ब्लैक फ़ॉरेस्ट से निकलकर काला सागर तक पहुँचने से पहले दस देशों, यानी जर्मनी, ऑस्ट्रिया, स्लोवाकिया, हंगरी, क्रोएशिया, सर्बिया, रोमानिया, बुल्गारिया, मोल्दोवा और यूक्रेन, से होकर या उनकी सीमा के साथ बहती है। "
  "कथन 2 गलत है: राइन स्विस आल्प्स से निकलकर नीदरलैंड्स से होते हुए उत्तरी सागर में गिरती है, जहाँ इसके डेल्टा पर रॉटरडैम बसा है। "
  "कथन 3 गलत है: इबेरियाई प्रायद्वीप की सबसे लंबी नदी टैगस स्पेन और पुर्तगाल से पश्चिम की ओर बहकर लिस्बन के पास अटलांटिक में गिरती है।",
  f"{ATLAS} -- Europe (physical).",
  "geo-europe-rivers-danube-rhine-tagus")

S(WR, "medium", "Consider the following statements about rivers of Africa:",
  "अफ़्रीका की नदियों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Nile flows northwards into the Mediterranean Sea.",
   "The Congo crosses the Equator twice.",
   "The Zambezi flows into the Atlantic Ocean."],
  ["नील नदी उत्तर की ओर बहकर भूमध्य सागर में गिरती है।",
   "कांगो नदी विषुवत रेखा को दो बार पार करती है।",
   "ज़ाम्बेज़ी नदी अटलांटिक महासागर में गिरती है।"],
  C3, 1,
  "Statements 1 and 2 are correct. The Nile flows north through Sudan and Egypt to a delta on the Mediterranean. The Congo first flows north across the Equator and then curves west and south-west, crossing it again before entering the Atlantic -- and, with rain on both sides of the Equator in different seasons, it flows strongly all year. "
  "Statement 3 is wrong: the Zambezi flows east over the Victoria Falls and through Mozambique into the Indian Ocean.",
  "कथन 1 और 2 सही हैं। नील उत्तर की ओर सूडान और मिस्र से होकर भूमध्य सागर पर डेल्टा बनाती है। कांगो पहले उत्तर की ओर विषुवत रेखा पार करती है और फिर पश्चिम तथा दक्षिण-पश्चिम की ओर मुड़कर अटलांटिक में मिलने से पहले उसे दोबारा पार करती है; विषुवत रेखा के दोनों ओर अलग-अलग ऋतुओं में वर्षा होने से इसमें पूरे वर्ष भरपूर जल रहता है। "
  "कथन 3 गलत है: ज़ाम्बेज़ी पूर्व की ओर विक्टोरिया जलप्रपात से गिरते हुए मोज़ाम्बिक से होकर हिंद महासागर में मिलती है।",
  f"{ATLAS} -- Africa (physical).",
  "geo-africa-rivers-nile-congo-zambezi")

S(WR, "medium", "Consider the following statements about lakes of the world:",
  "विश्व की झीलों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Lake Baikal is the deepest lake in the world.",
   "Lake Victoria is the largest lake in Africa by area.",
   "Lake Titicaca is often described as the highest navigable lake in the world."],
  ["बैकाल झील विश्व की सबसे गहरी झील है।",
   "क्षेत्रफल के अनुसार विक्टोरिया झील अफ़्रीका की सबसे बड़ी झील है।",
   "टिटिकाका झील को प्रायः विश्व की सबसे ऊँची नौगम्य (navigable) झील कहा जाता है।"],
  C3, 2,
  "All three statements are correct. Baikal in Siberia, a rift lake more than 1,600 m deep, holds about a fifth of the world's unfrozen surface fresh water; Victoria, shared by Uganda, Kenya and Tanzania, is the largest lake in Africa and the largest tropical lake in the world; and Titicaca, at about 3,800 m in the Andes, carries regular boat traffic.",
  "तीनों कथन सही हैं। साइबेरिया की बैकाल, 1,600 मीटर से अधिक गहरी एक भ्रंश झील, में विश्व के जमे हुए न रहने वाले सतही मीठे जल का लगभग पाँचवाँ भाग है; युगांडा, केन्या और तंज़ानिया में फैली विक्टोरिया अफ़्रीका की सबसे बड़ी और विश्व की सबसे बड़ी उष्णकटिबंधीय झील है; और एंडीज़ में लगभग 3,800 मीटर की ऊँचाई पर स्थित टिटिकाका में नियमित नौका-यातायात होता है।",
  f"{ATLAS} -- World (physical).",
  "geo-world-lakes-baikal-victoria-titicaca")

S(WR, "medium", "Consider the following statements about deserts:",
  "मरुस्थलों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Gobi Desert lies in Mongolia and China.",
   "The Kalahari Desert lies mainly in Botswana.",
   "The Karakum Desert lies mainly in Iran."],
  ["गोबी मरुस्थल मंगोलिया और चीन में स्थित है।",
   "कालाहारी मरुस्थल मुख्य रूप से बोत्सवाना में स्थित है।",
   "काराकुम मरुस्थल मुख्य रूप से ईरान में स्थित है।"],
  C3, 1,
  "Statements 1 and 2 are correct. The Gobi is a cold desert of the Mongolian plateau and northern China, with bitter winters; the Kalahari, a semi-desert of red sand, covers most of Botswana and extends into Namibia and South Africa. "
  "Statement 3 is wrong: the Karakum ('black sand') covers most of Turkmenistan, east of the Caspian; Iran's great deserts are the Dasht-e Kavir and the Dasht-e Lut.",
  "कथन 1 और 2 सही हैं। गोबी मंगोलियाई पठार और उत्तरी चीन का एक ठंडा मरुस्थल है, जहाँ कड़ाके की सर्दी पड़ती है; लाल रेत वाला अर्ध-मरुस्थल कालाहारी बोत्सवाना के अधिकांश भाग में फैला है और नामीबिया तथा दक्षिण अफ़्रीका तक जाता है। "
  "कथन 3 गलत है: काराकुम ('काली रेत') कैस्पियन के पूर्व में तुर्कमेनिस्तान के अधिकांश भाग में फैला है; ईरान के बड़े मरुस्थल दश्त-ए-कवीर और दश्त-ए-लूत हैं।",
  f"{ATLAS} -- Asia and Africa (physical); {NC7} -- Life in the Deserts.",
  "geo-deserts-gobi-kalahari-karakum")

S(WR, "medium", "Consider the following statements about mountain ranges:",
  "पर्वत श्रेणियों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Andes are the longest continental mountain range in the world.",
   "The Atlas Mountains lie in East Africa.",
   "The Appalachians are young fold mountains."],
  ["एंडीज़ विश्व की सबसे लंबी महाद्वीपीय पर्वत श्रेणी है।",
   "एटलस पर्वत पूर्वी अफ़्रीका में स्थित हैं।",
   "अप्लेशियन नवीन वलित पर्वत हैं।"],
  C3, 0,
  "Only statement 1 is correct: the Andes run about 7,000 km along the western edge of South America, from Venezuela to Tierra del Fuego. "
  "Statement 2 is wrong: the Atlas Mountains lie in north-west Africa, across Morocco, Algeria and Tunisia, and were raised by the same collision of Africa with Europe that built the Alps. "
  "Statement 3 is wrong: the Appalachians of eastern North America are very old fold mountains, formed hundreds of millions of years ago and worn down to rounded ridges; the Rockies, the Alps and the Himalayas are the young ones.",
  "केवल कथन 1 सही है: एंडीज़ दक्षिण अमेरिका के पश्चिमी किनारे पर वेनेज़ुएला से टिएरा डेल फ़्यूगो तक लगभग 7,000 किमी तक फैली हैं। "
  "कथन 2 गलत है: एटलस पर्वत उत्तर-पश्चिमी अफ़्रीका में मोरक्को, अल्जीरिया और ट्यूनीशिया में फैले हैं, और अफ़्रीका तथा यूरोप की उसी टक्कर से उठे हैं जिससे आल्प्स बने। "
  "कथन 3 गलत है: पूर्वी उत्तरी अमेरिका के अप्लेशियन बहुत पुराने वलित पर्वत हैं, जो करोड़ों वर्ष पहले बने और घिसकर गोल कटकें रह गए; रॉकी, आल्प्स और हिमालय नवीन वलित पर्वत हैं।",
  f"{ATLAS} -- World (physical); {NC11} -- Distribution of Oceans and Continents.",
  "geo-mountain-ranges-andes-atlas-appalachians")

S(WR, "medium", "Consider the following countries:",
  "निम्नलिखित देशों पर विचार कीजिए:",
  ["Bolivia", "Ethiopia", "Eritrea", "Paraguay"],
  ["बोलीविया", "इथियोपिया", "इरिट्रिया", "पराग्वे"],
  C4, 2,
  "Bolivia, Ethiopia and Paraguay are landlocked. Bolivia lost its Pacific coast to Chile in the War of the Pacific (1879-84); Paraguay reaches the sea only by the Paraguay-Paraná river system. "
  "Eritrea is the trap: it has a long Red Sea coast with the ports of Massawa and Assab, and it was Eritrea's independence in 1993 that left Ethiopia landlocked.",
  "बोलीविया, इथियोपिया और पराग्वे स्थलरुद्ध हैं। बोलीविया ने प्रशांत युद्ध (1879-84) में अपना प्रशांत तट चिली के हाथों खो दिया; पराग्वे केवल पराग्वे-पराना नदी तंत्र के रास्ते समुद्र तक पहुँचता है। "
  "इरिट्रिया ही जाल है: उसकी लाल सागर पर लंबी तटरेखा है, जिस पर मस्सावा और असब बंदरगाह हैं, और 1993 में इरिट्रिया की स्वतंत्रता से ही इथियोपिया स्थलरुद्ध हुआ।",
  f"{ATLAS} -- Africa and South America (political).",
  "geo-landlocked-countries",
  closing=f"{HOW_MANY_C} are landlocked?",
  closing_hi="उपर्युक्त में से कितने देश स्थलरुद्ध (landlocked) हैं?")

S(WR, "medium", "Consider the following countries:",
  "निम्नलिखित देशों पर विचार कीजिए:",
  ["Indonesia", "Malaysia", "Singapore", "Somalia"],
  ["इंडोनेशिया", "मलेशिया", "सिंगापुर", "सोमालिया"],
  C4, 1,
  "The Equator passes through Indonesia (across Sumatra, Borneo, Sulawesi and Halmahera) and southern Somalia. "
  "Malaysia and Singapore are the traps: both are often called 'equatorial', and Singapore lies only about 137 km north of the Equator, but the line itself passes south of them, through the Indonesian islands.",
  "विषुवत रेखा इंडोनेशिया (सुमात्रा, बोर्नियो, सुलावेसी और हलमाहेरा से होकर) और दक्षिणी सोमालिया से गुज़रती है। "
  "मलेशिया और सिंगापुर ही जाल हैं: दोनों को प्रायः 'विषुवतीय' कहा जाता है, और सिंगापुर विषुवत रेखा से केवल लगभग 137 किमी उत्तर में है, पर रेखा स्वयं उनके दक्षिण से, इंडोनेशियाई द्वीपों से होकर गुज़रती है।",
  f"{ATLAS} -- World (political).",
  "geo-equator-countries",
  closing=f"{HOW_MANY_C} does the Equator pass through?",
  closing_hi="विषुवत रेखा उपर्युक्त में से कितने देशों से होकर गुज़रती है?")

S(WR, "medium", "Consider the following countries:",
  "निम्नलिखित देशों पर विचार कीजिए:",
  ["Iran", "Pakistan", "Nepal"],
  ["ईरान", "पाकिस्तान", "नेपाल"],
  C3, 3,
  "The Tropic of Cancer passes through none of them. Across Asia it runs through Saudi Arabia, the UAE and Oman, then India, Bangladesh, Myanmar, China and Taiwan. "
  "Pakistan is the closest trap -- its southern tip near the Sir Creek lies just north of the Tropic -- and Iran's southern coast and Nepal's southern plains also lie north of it.",
  "कर्क रेखा इनमें से किसी से होकर नहीं गुज़रती। एशिया में यह सऊदी अरब, संयुक्त अरब अमीरात और ओमान, फिर भारत, बांग्लादेश, म्यांमार, चीन और ताइवान से गुज़रती है। "
  "पाकिस्तान सबसे निकट का जाल है, उसका दक्षिणी छोर सर क्रीक के पास कर्क रेखा से ठीक उत्तर में है, और ईरान का दक्षिणी तट तथा नेपाल के दक्षिणी मैदान भी उसके उत्तर में हैं।",
  f"{ATLAS} -- Asia (political).",
  "geo-tropic-of-cancer-countries",
  closing=f"{HOW_MANY_C} does the Tropic of Cancer pass through?",
  closing_hi="कर्क रेखा उपर्युक्त में से कितने देशों से होकर गुज़रती है?")

S(WR, "medium", "Consider the following statements about regions often in the news:",
  "प्रायः चर्चा में रहने वाले क्षेत्रों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Golan Heights were captured by Israel from Syria in 1967.",
   "The Donbas region lies in eastern Ukraine.",
   "Nagorno-Karabakh is internationally recognised as part of Armenia."],
  ["गोलान पहाड़ियों को इज़राइल ने 1967 में सीरिया से छीना था।",
   "डोनबास क्षेत्र पूर्वी यूक्रेन में स्थित है।",
   "नागोर्नो-काराबाख को अंतरराष्ट्रीय स्तर पर आर्मेनिया के भाग के रूप में मान्यता प्राप्त है।"],
  C3, 1,
  "Statements 1 and 2 are correct. Israel took the Golan Heights, a basalt plateau overlooking the Sea of Galilee, in the 1967 war; the Donbas, the coal-mining basin of the Donets river, covers the Donetsk and Luhansk regions of eastern Ukraine. "
  "Statement 3 is wrong: Nagorno-Karabakh, though long held by ethnic Armenian forces, is internationally recognised as part of Azerbaijan, which took full control of it in September 2023.",
  "कथन 1 और 2 सही हैं। इज़राइल ने 1967 के युद्ध में गैलिली सागर के ऊपर स्थित बेसाल्ट पठार गोलान पहाड़ियों पर कब्ज़ा किया; डोनेत्स नदी का कोयला खनन बेसिन डोनबास पूर्वी यूक्रेन के दोनेत्स्क और लुहान्स्क क्षेत्रों में फैला है। "
  "कथन 3 गलत है: नागोर्नो-काराबाख लंबे समय तक आर्मेनियाई मूल के सशस्त्र बलों के नियंत्रण में रहा, पर अंतरराष्ट्रीय स्तर पर इसे अज़रबैजान का भाग माना जाता है, जिसने सितंबर 2023 में इस पर पूरा नियंत्रण कर लिया।",
  f"{ATLAS} -- Asia and Europe (political); Ministry of External Affairs -- country briefs.",
  "geo-regions-in-news-golan-donbas-karabakh")

# ================================================================ HARD STATEMENTS (4)
S(WR, "hard", "Consider the following statements about dams:",
  "बाँधों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Grand Ethiopian Renaissance Dam is on the Blue Nile.",
   "The Three Gorges Dam is on the Yellow River (Huang He).",
   "The Kariba Dam is on the Limpopo."],
  ["ग्रैंड इथियोपियन रेनेसां बाँध ब्लू नील पर है।",
   "थ्री गॉर्जेस बाँध पीली नदी (ह्वांग हो) पर है।",
   "करीबा बाँध लिम्पोपो नदी पर है।"],
  C3, 0,
  "Only statement 1 is correct: the Grand Ethiopian Renaissance Dam, Africa's largest hydroelectric project, stands on the Blue Nile near Ethiopia's border with Sudan, and Egypt and Sudan fear its effect on their share of the Nile. "
  "Statement 2 is wrong: the Three Gorges Dam, the world's largest power station by capacity, is on the Yangtze in Hubei province. "
  "Statement 3 is wrong: the Kariba Dam is on the Zambezi, on the Zambia-Zimbabwe border, and holds back one of the largest artificial lakes in the world.",
  "केवल कथन 1 सही है: अफ़्रीका की सबसे बड़ी जलविद्युत परियोजना, ग्रैंड इथियोपियन रेनेसां बाँध, सूडान से लगी इथियोपिया की सीमा के पास ब्लू नील पर है, और मिस्र तथा सूडान को नील के जल में अपने हिस्से पर इसके प्रभाव की चिंता है। "
  "कथन 2 गलत है: क्षमता के अनुसार विश्व का सबसे बड़ा बिजलीघर, थ्री गॉर्जेस बाँध, हुबेई प्रांत में यांग्त्सी नदी पर है। "
  "कथन 3 गलत है: करीबा बाँध ज़ाम्बिया-ज़िम्बाब्वे सीमा पर ज़ाम्बेज़ी नदी पर है, और इससे विश्व की सबसे बड़ी कृत्रिम झीलों में से एक बनी है।",
  f"{ATLAS} -- Africa and Asia (physical).",
  "geo-world-dams-gerd-three-gorges-kariba")

S(WR, "hard", "Consider the following statements about the polar regions:",
  "ध्रुवीय क्षेत्रों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Arctic is an ocean largely surrounded by land, whereas Antarctica is a landmass surrounded by ocean.",
   "The Antarctic Treaty was signed in 1959.",
   "The Svalbard archipelago in the Arctic belongs to Denmark."],
  ["आर्कटिक मुख्य रूप से स्थल से घिरा एक महासागर है, जबकि अंटार्कटिका महासागर से घिरा एक भूभाग है।",
   "अंटार्कटिक संधि पर 1959 में हस्ताक्षर किए गए थे।",
   "आर्कटिक में स्वालबार्ड द्वीपसमूह डेनमार्क का है।"],
  C3, 1,
  "Statements 1 and 2 are correct. The Arctic Ocean is ringed by Eurasia, North America and Greenland, while Antarctica is a continent, mostly under an ice sheet, surrounded by the Southern Ocean. The Antarctic Treaty, signed in 1959 and in force from 1961, keeps the continent for peaceful and scientific use and freezes territorial claims; India joined it in 1983. "
  "Statement 3 is wrong: Svalbard belongs to Norway under the Svalbard Treaty of 1920, which lets other signatories carry on economic activity there -- India's Arctic station Himadri is at Ny-Ålesund. Denmark is the trap because Greenland, an autonomous territory, belongs to the Danish realm.",
  "कथन 1 और 2 सही हैं। आर्कटिक महासागर यूरेशिया, उत्तरी अमेरिका और ग्रीनलैंड से घिरा है, जबकि अंटार्कटिका एक महाद्वीप है, जो अधिकतर एक हिम-चादर के नीचे है और दक्षिणी महासागर से घिरा है। 1959 में हस्ताक्षरित और 1961 से लागू अंटार्कटिक संधि इस महाद्वीप को शांतिपूर्ण और वैज्ञानिक उपयोग के लिए सुरक्षित रखती है और क्षेत्रीय दावों को स्थगित करती है; भारत 1983 में इसमें शामिल हुआ। "
  "कथन 3 गलत है: स्वालबार्ड 1920 की स्वालबार्ड संधि के तहत नॉर्वे का है, जो अन्य हस्ताक्षरकर्ताओं को वहाँ आर्थिक गतिविधियाँ करने देती है; भारत का आर्कटिक केंद्र हिमाद्रि न्यू-एलेसुंड में है। डेनमार्क इसलिए जाल है कि स्वायत्त क्षेत्र ग्रीनलैंड डेनमार्क के राज्य-क्षेत्र का भाग है।",
  "Ministry of Earth Sciences -- Polar and Cryosphere programme; Secretariat of the Antarctic Treaty.",
  "geo-polar-regions-treaty-svalbard")

S(WR, "hard", "Consider the following statements about plateaus:",
  "पठारों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Tibetan Plateau is the highest and largest plateau in the world.",
   "The Patagonian plateau lies mainly in Argentina.",
   "The Altiplano is a high plateau in the Andes shared mainly by Bolivia and Peru."],
  ["तिब्बत का पठार विश्व का सबसे ऊँचा और सबसे बड़ा पठार है।",
   "पैटागोनिया का पठार मुख्य रूप से अर्जेंटीना में स्थित है।",
   "अल्टिप्लानो एंडीज़ में स्थित एक ऊँचा पठार है, जो मुख्य रूप से बोलीविया और पेरू में फैला है।"],
  C3, 2,
  "All three statements are correct. The Tibetan Plateau, averaging over 4,500 m, is an intermontane plateau lifted by the collision of India with Asia and is the source of the Indus, the Brahmaputra, the Yangtze and the Mekong. Patagonia's dry, windswept plateau lies east of the Andes in southern Argentina, in the rain shadow of the mountains; Chile's part of Patagonia is mountains and fjords. The Altiplano, at about 3,750 m, lies between two ranges of the Andes and holds Lake Titicaca.",
  "तीनों कथन सही हैं। औसतन 4,500 मीटर से अधिक ऊँचा तिब्बत का पठार भारत और एशिया की टक्कर से उठा एक अंतरापर्वतीय पठार है, और सिंधु, ब्रह्मपुत्र, यांग्त्सी तथा मेकांग का उद्गम क्षेत्र है। पैटागोनिया का शुष्क, हवादार पठार दक्षिणी अर्जेंटीना में एंडीज़ के पूर्व में, पर्वतों के वृष्टि-छाया क्षेत्र में है; चिली वाला पैटागोनिया पर्वतों और फ़्योर्डों का क्षेत्र है। लगभग 3,750 मीटर ऊँचा अल्टिप्लानो एंडीज़ की दो श्रेणियों के बीच है और इसी पर टिटिकाका झील है।",
  f"{ATLAS} -- Asia and South America (physical); {NC11} -- Landforms and their Evolution.",
  "geo-plateaus-tibet-patagonia-altiplano")

S(WR, "hard", "Consider the following statements about islands of the Mediterranean Sea:",
  "भूमध्य सागर के द्वीपों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Sicily is a part of Italy.",
   "Corsica is a part of Italy.",
   "Crete is a part of Greece.",
   "Sardinia is a part of Italy."],
  ["सिसिली इटली का भाग है।",
   "कोर्सिका इटली का भाग है।",
   "क्रीट यूनान (ग्रीस) का भाग है।",
   "सार्डिनिया इटली का भाग है।"],
  C4, 2,
  "Statements 1, 3 and 4 are correct: Sicily and Sardinia, the two largest islands of the Mediterranean, are regions of Italy, and Crete is the largest Greek island. "
  "Statement 2 is wrong, and it is the trap: Corsica lies just north of Sardinia and its people speak a language close to Italian, but it has belonged to France since 1768 and was the birthplace of Napoleon.",
  "कथन 1, 3 और 4 सही हैं: भूमध्य सागर के दो सबसे बड़े द्वीप सिसिली और सार्डिनिया इटली के क्षेत्र हैं, और क्रीट यूनान का सबसे बड़ा द्वीप है। "
  "कथन 2 गलत है, और यही जाल है: कोर्सिका सार्डिनिया के ठीक उत्तर में है और वहाँ के लोग इतालवी से मिलती-जुलती भाषा बोलते हैं, पर यह 1768 से फ़्रांस का है और नेपोलियन की जन्मभूमि है।",
  f"{ATLAS} -- Europe (political).",
  "geo-mediterranean-islands")

# ================================================================ EASY STATEMENTS (3)
S(WR, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Asia is the smallest continent.",
   "Australia is both a country and a continent."],
  ["एशिया सबसे छोटा महाद्वीप है।",
   "ऑस्ट्रेलिया एक देश भी है और एक महाद्वीप भी।"],
  T2, 1,
  "Only statement 2 is correct. Statement 1 is wrong: Asia is the largest continent, covering about a third of the Earth's land; Australia is the smallest.",
  "केवल कथन 2 सही है। कथन 1 गलत है: एशिया सबसे बड़ा महाद्वीप है, जो पृथ्वी के स्थल भाग के लगभग एक-तिहाई भाग में फैला है; सबसे छोटा महाद्वीप ऑस्ट्रेलिया है।",
  f"{NC6} -- Major Domains of the Earth.",
  "geo-continents-asia-australia-easy")

S(WR, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Pacific is the largest ocean.",
   "The Amazon flows into the Pacific Ocean."],
  ["प्रशांत सबसे बड़ा महासागर है।",
   "अमेज़न नदी प्रशांत महासागर में गिरती है।"],
  T2, 0,
  "Only statement 1 is correct: the Pacific covers about a third of the Earth's surface -- more than all the land put together. Statement 2 is wrong: the Amazon rises in the Andes of Peru, less than 200 km from the Pacific, but flows east across Brazil into the Atlantic.",
  "केवल कथन 1 सही है: प्रशांत पृथ्वी की सतह के लगभग एक-तिहाई भाग में फैला है, यानी सारे स्थल भाग को मिलाकर भी उससे अधिक। कथन 2 गलत है: अमेज़न पेरू की एंडीज़ में प्रशांत से 200 किमी से भी कम दूरी पर निकलती है, पर पूर्व की ओर ब्राज़ील से होकर अटलांटिक में गिरती है।",
  f"{NC6} -- Major Domains of the Earth; {ATLAS} -- South America (physical).",
  "geo-pacific-amazon-easy")

S(WR, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["Antarctica is the coldest continent.",
   "The Mississippi-Missouri is the longest river system of North America."],
  ["अंटार्कटिका सबसे ठंडा महाद्वीप है।",
   "मिसिसिपी-मिसौरी उत्तरी अमेरिका का सबसे लंबा नदी तंत्र है।"],
  T2, 2,
  "Both statements are correct. Antarctica is also the windiest, driest and highest continent on average; the lowest natural temperature on record, about -89 °C, was measured at Vostok station. The Mississippi and its longest tributary, the Missouri, drain most of the central United States into the Gulf of Mexico.",
  "दोनों कथन सही हैं। अंटार्कटिका औसतन सबसे अधिक हवादार, सबसे शुष्क और सबसे ऊँचा महाद्वीप भी है; अब तक का सबसे कम प्राकृतिक तापमान, लगभग -89 °C, वोस्तोक केंद्र पर मापा गया था। मिसिसिपी और उसकी सबसे लंबी सहायक नदी मिसौरी मध्य संयुक्त राज्य अमेरिका के अधिकांश भाग का जल मेक्सिको की खाड़ी तक ले जाती हैं।",
  f"{NC6} -- Major Domains of the Earth; {ATLAS} -- North America (physical).",
  "geo-antarctica-mississippi-easy")

# ================================================================ MCQs (medium 5, easy 2, hard 2)
M(WR, "medium", "The Strait of Malacca separates:",
  "मलक्का जलडमरूमध्य किन्हें अलग करता है?",
  ["Sumatra and the Malay Peninsula", "Java and Sumatra", "the island of Taiwan and mainland China", "Borneo and Sulawesi"],
  ["सुमात्रा और मलय प्रायद्वीप", "जावा और सुमात्रा", "ताइवान द्वीप और मुख्य भूमि चीन", "बोर्नियो और सुलावेसी"],
  0,
  "The Strait of Malacca, between Indonesia's Sumatra and the Malay Peninsula, links the Andaman Sea with the South China Sea and is one of the busiest shipping lanes in the world, carrying much of East Asia's oil. The Sunda Strait separates Java and Sumatra, the Makassar Strait separates Borneo and Sulawesi, and the Taiwan Strait separates Taiwan from mainland China.",
  "इंडोनेशिया के सुमात्रा और मलय प्रायद्वीप के बीच स्थित मलक्का जलडमरूमध्य अंडमान सागर को दक्षिण चीन सागर से जोड़ता है और विश्व के सबसे व्यस्त जहाज़ी मार्गों में से एक है, जिससे पूर्वी एशिया का बहुत-सा तेल गुज़रता है। सुंडा जलडमरूमध्य जावा और सुमात्रा को, मकास्सर जलडमरूमध्य बोर्नियो और सुलावेसी को, और ताइवान जलडमरूमध्य ताइवान को मुख्य भूमि चीन से अलग करता है।",
  f"{ATLAS} -- Asia (physical).",
  "geo-strait-of-malacca")

M(WR, "medium", "Which one of the following is the longest river of Europe?",
  "निम्नलिखित में से कौन-सी यूरोप की सबसे लंबी नदी है?",
  ["The Volga", "The Danube", "The Rhine", "The Dnieper"],
  ["वोल्गा", "डेन्यूब", "राइन", "नीपर"],
  0,
  "The Volga, about 3,530 km long, flows entirely within Russia into the Caspian Sea. The Danube, about 2,850 km, is second and is the tempting answer because it is the best known and crosses the most countries; the Dnieper and the Rhine are shorter still.",
  "लगभग 3,530 किमी लंबी वोल्गा पूरी तरह रूस में बहकर कैस्पियन सागर में गिरती है। लगभग 2,850 किमी लंबी डेन्यूब दूसरे स्थान पर है और आकर्षक उत्तर इसलिए लगती है कि वह सबसे प्रसिद्ध है और सबसे अधिक देशों से गुज़रती है; नीपर और राइन और भी छोटी हैं।",
  f"{ATLAS} -- Europe (physical).",
  "geo-longest-river-europe-volga")

M(WR, "medium", "Which one of the following countries has coastlines on both the Atlantic and the Indian Ocean?",
  "निम्नलिखित में से किस देश की तटरेखा अटलांटिक और हिंद महासागर, दोनों पर है?",
  ["South Africa", "Namibia", "Mozambique", "Equatorial Guinea"],
  ["दक्षिण अफ़्रीका", "नामीबिया", "मोज़ाम्बिक", "इक्वेटोरियल गिनी"],
  0,
  "South Africa's coast runs from the Atlantic on the west, past Cape Town and the Cape of Good Hope, to the Indian Ocean on the east at Durban; Cape Agulhas, its southernmost point, is taken as the meeting point of the two oceans. Namibia and Equatorial Guinea face only the Atlantic, and Mozambique only the Indian Ocean.",
  "दक्षिण अफ़्रीका का तट पश्चिम में अटलांटिक से, केप टाउन और केप ऑफ़ गुड होप के पास से होते हुए, पूर्व में डरबन पर हिंद महासागर तक जाता है; इसका सबसे दक्षिणी बिंदु केप अगुलहास दोनों महासागरों का मिलन-बिंदु माना जाता है। नामीबिया और इक्वेटोरियल गिनी केवल अटलांटिक के सामने हैं, और मोज़ाम्बिक केवल हिंद महासागर के।",
  f"{ATLAS} -- Africa (political).",
  "geo-south-africa-two-oceans")

M(WR, "medium", "Which one of the following seas has the highest salinity?",
  "निम्नलिखित में से किस सागर की लवणता सबसे अधिक है?",
  ["The Red Sea", "The Black Sea", "The North Sea", "The Caribbean Sea"],
  ["लाल सागर", "काला सागर", "उत्तरी सागर", "कैरिबियन सागर"],
  0,
  "The Red Sea, at about 40 parts per thousand, is one of the saltiest seas: it lies in a hot, dry belt with intense evaporation, almost no rain and no permanent rivers, and it exchanges water with the ocean only through the narrow Bab-el-Mandeb. The Black Sea is among the least salty (about 17-18) because large rivers pour into it.",
  "लगभग 40 भाग प्रति हज़ार वाला लाल सागर सबसे खारे सागरों में से एक है: यह तेज़ वाष्पीकरण वाली गर्म, शुष्क पेटी में है, वहाँ लगभग वर्षा नहीं होती और कोई स्थायी नदी नहीं गिरती, और यह महासागर से केवल संकरे बाब-अल-मंदेब से होकर जल का आदान-प्रदान करता है। बड़ी नदियाँ गिरने के कारण काला सागर सबसे कम खारे सागरों (लगभग 17-18) में है।",
  f"{NC11} -- Water (Oceans); {ATLAS} -- World (physical).",
  "geo-red-sea-salinity")

M(WR, "medium", "Mount Kilimanjaro, the highest peak in Africa, lies in:",
  "अफ़्रीका की सबसे ऊँची चोटी माउंट किलिमंजारो कहाँ स्थित है?",
  ["Tanzania", "Kenya", "Uganda", "Ethiopia"],
  ["तंज़ानिया", "केन्या", "युगांडा", "इथियोपिया"],
  0,
  "Kilimanjaro (about 5,895 m), a dormant volcano with a snow-capped summit only about 3 degrees south of the Equator, stands in north-eastern Tanzania close to the Kenyan border. Kenya is the tempting answer because the best-known views of the mountain are from Kenya's Amboseli National Park; Kenya's own highest peak is Mount Kenya.",
  "किलिमंजारो (लगभग 5,895 मीटर), विषुवत रेखा से केवल लगभग 3 अंश दक्षिण में हिमाच्छादित शिखर वाला एक सुप्त ज्वालामुखी, केन्या की सीमा के पास उत्तर-पूर्वी तंज़ानिया में है। केन्या आकर्षक उत्तर इसलिए है कि इस पर्वत के सबसे प्रसिद्ध दृश्य केन्या के अम्बोसेली राष्ट्रीय उद्यान से दिखते हैं; केन्या की अपनी सबसे ऊँची चोटी माउंट केन्या है।",
  f"{ATLAS} -- Africa (physical).",
  "geo-kilimanjaro-tanzania")

M(WR, "easy", "Which one of the following continents is crossed by the Equator, the Tropic of Cancer and the Tropic of Capricorn?",
  "निम्नलिखित में से किस महाद्वीप से विषुवत रेखा, कर्क रेखा और मकर रेखा, तीनों गुज़रती हैं?",
  ["Africa", "South America", "Asia", "Australia"],
  ["अफ़्रीका", "दक्षिण अमेरिका", "एशिया", "ऑस्ट्रेलिया"],
  0,
  "Africa is the only continent crossed by all three lines: the Tropic of Cancer passes through the Sahara, the Equator through Gabon, the Congo basin, Uganda, Kenya and Somalia, and the Tropic of Capricorn through Namibia, Botswana, South Africa and Mozambique. South America is crossed by the Equator and the Tropic of Capricorn but not the Tropic of Cancer, and Asia by the Equator and the Tropic of Cancer only.",
  "अफ़्रीका ही एकमात्र महाद्वीप है जिससे ये तीनों रेखाएँ गुज़रती हैं: कर्क रेखा सहारा से, विषुवत रेखा गैबॉन, कांगो बेसिन, युगांडा, केन्या और सोमालिया से, और मकर रेखा नामीबिया, बोत्सवाना, दक्षिण अफ़्रीका तथा मोज़ाम्बिक से। दक्षिण अमेरिका से विषुवत और मकर रेखा गुज़रती हैं पर कर्क रेखा नहीं, और एशिया से केवल विषुवत और कर्क रेखा।",
  f"{NC6} -- Globe: Latitudes and Longitudes; {ATLAS} -- World (political).",
  "geo-africa-three-latitudes-easy")

M(WR, "easy", "The Great Lakes of North America lie along the border between:",
  "उत्तरी अमेरिका की महान झीलें (Great Lakes) किनकी सीमा के साथ स्थित हैं?",
  ["the United States and Canada", "the United States and Mexico", "Canada and Greenland", "Mexico and Guatemala"],
  ["संयुक्त राज्य अमेरिका और कनाडा", "संयुक्त राज्य अमेरिका और मेक्सिको", "कनाडा और ग्रीनलैंड", "मेक्सिको और ग्वाटेमाला"],
  0,
  "Lakes Superior, Huron, Erie and Ontario are shared by the United States and Canada; Lake Michigan lies wholly in the United States. Together they form the largest group of freshwater lakes on Earth and, with the St Lawrence Seaway, carry ocean shipping deep into the continent.",
  "सुपीरियर, ह्यूरन, ईरी और ओंटारियो झीलें संयुक्त राज्य अमेरिका और कनाडा में साझा हैं; मिशिगन झील पूरी तरह संयुक्त राज्य अमेरिका में है। ये मिलकर पृथ्वी पर मीठे जल की झीलों का सबसे बड़ा समूह बनाती हैं, और सेंट लॉरेंस सीवे के साथ समुद्री जहाज़ों को महाद्वीप के भीतर तक ले जाती हैं।",
  f"{ATLAS} -- North America (physical).",
  "geo-great-lakes-border-easy")

M(WR, "hard", "Which one of the following islands lies on the Mid-Atlantic Ridge?",
  "निम्नलिखित में से कौन-सा द्वीप मध्य-अटलांटिक कटक (Mid-Atlantic Ridge) पर स्थित है?",
  ["Iceland", "Greenland", "Bermuda", "The Canary Islands"],
  ["आइसलैंड", "ग्रीनलैंड", "बरमूडा", "कैनरी द्वीपसमूह"],
  0,
  "The Mid-Atlantic Ridge, where the North American and Eurasian plates move apart, rises above the sea in Iceland; there a hotspot adds extra magma, and the rift valley can be walked across at Thingvellir. Greenland is part of the North American continental landmass, while Bermuda and the Canary Islands are volcanic islands that lie well away from the ridge.",
  "मध्य-अटलांटिक कटक, जहाँ उत्तरी अमेरिकी और यूरेशियाई प्लेटें एक-दूसरे से दूर जा रही हैं, आइसलैंड में समुद्र से ऊपर उठी है; वहाँ एक तप्त स्थल (hotspot) अतिरिक्त मैग्मा देता है, और थिंगवेलिर में भ्रंश घाटी को पैदल पार किया जा सकता है। ग्रीनलैंड उत्तरी अमेरिकी महाद्वीपीय भूभाग का भाग है, जबकि बरमूडा और कैनरी द्वीपसमूह ज्वालामुखी द्वीप हैं जो कटक से काफ़ी दूर हैं।",
  f"{NC11} -- Distribution of Oceans and Continents.",
  "geo-mid-atlantic-ridge-iceland")

M(WR, "hard", "Which one of the following seas has no land boundary?",
  "निम्नलिखित में से किस सागर की कोई स्थलीय सीमा नहीं है?",
  ["The Sargasso Sea", "The Caribbean Sea", "The Arabian Sea", "The Coral Sea"],
  ["सारगैसो सागर", "कैरिबियन सागर", "अरब सागर", "कोरल सागर"],
  0,
  "The Sargasso Sea, in the North Atlantic, is the only sea with no coastline: it is bounded by ocean currents -- the Gulf Stream on the west, the North Atlantic Drift on the north, the Canary Current on the east and the North Equatorial Current on the south -- which make it a calm, slowly turning gyre full of floating sargassum seaweed. Bermuda lies on its western edge.",
  "उत्तरी अटलांटिक का सारगैसो सागर ही एकमात्र ऐसा सागर है जिसकी कोई तटरेखा नहीं है: यह महासागरीय धाराओं से घिरा है, यानी पश्चिम में गल्फ़ स्ट्रीम, उत्तर में उत्तरी अटलांटिक प्रवाह, पूर्व में कैनरी धारा और दक्षिण में उत्तरी विषुवतीय धारा; ये इसे तैरती सारगैसम समुद्री घास से भरा एक शांत, धीरे घूमता भँवर (gyre) बनाती हैं। बरमूडा इसके पश्चिमी किनारे पर है।",
  f"{NC11} -- Movements of Ocean Water.",
  "geo-sargasso-sea-no-coast")

# ================================================================ STATEMENT-I/II (medium 4, easy 1, hard I/II/III 1)
A(WR, "medium",
  "The shore of the Dead Sea is the lowest point on land on the Earth's surface.",
  "मृत सागर का तट पृथ्वी की सतह पर स्थल का सबसे निचला बिंदु है।",
  "The Dead Sea occupies the crater of an extinct volcano.",
  "मृत सागर एक विलुप्त ज्वालामुखी के क्रेटर में स्थित है।",
  2,
  "Statement-I is correct but Statement-II is incorrect. The Dead Sea's shore lies about 430 m below sea level. It fills part of a rift valley along a great fault -- the Dead Sea Transform, where the Arabian plate slides past the African -- not a volcanic crater. With no outlet and intense evaporation, its water is nearly ten times as salty as the ocean, so bathers float easily.",
  "कथन-I सही है पर कथन-II गलत है। मृत सागर का तट समुद्र तल से लगभग 430 मीटर नीचे है। यह किसी ज्वालामुखी क्रेटर में नहीं, बल्कि एक बड़े भ्रंश के साथ बनी भ्रंश घाटी के एक भाग में है, जहाँ अरब प्लेट अफ़्रीकी प्लेट के पास से सरकती है (डेड सी ट्रांसफ़ॉर्म)। कोई निकास न होने और तेज़ वाष्पीकरण के कारण इसका जल महासागर से लगभग दस गुना खारा है, इसलिए इसमें नहाने वाले आसानी से तैरते रहते हैं।",
  f"{ATLAS} -- Asia (physical).",
  "geo-dead-sea-lowest-rift")

A(WR, "medium",
  "Norway's coastline is deeply indented by fjords.",
  "नॉर्वे की तटरेखा फ़्योर्डों (fjords) से गहराई तक कटी-फटी है।",
  "Norway is one of Europe's leading producers of oil and natural gas.",
  "नॉर्वे यूरोप के प्रमुख तेल और प्राकृतिक गैस उत्पादकों में से एक है।",
  1,
  "Both statements are correct, but Statement-II does not explain Statement-I. Fjords are deep, steep-sided valleys carved by glaciers during the Ice Age and later drowned by the sea as the ice melted and sea level rose. Norway's oil and gas come from fields beneath the North Sea -- an unrelated fact that a student may link to the coast simply because both are about Norway's sea.",
  "दोनों कथन सही हैं, पर कथन-II कथन-I की व्याख्या नहीं करता। फ़्योर्ड हिमयुग में हिमनदों द्वारा काटी गई गहरी, खड़ी ढलान वाली घाटियाँ हैं, जो बाद में बर्फ़ पिघलने और समुद्र तल ऊपर उठने से समुद्र में डूब गईं। नॉर्वे का तेल और गैस उत्तरी सागर के नीचे के क्षेत्रों से आता है; यह असंबद्ध तथ्य है, जिसे विद्यार्थी केवल इसलिए तट से जोड़ सकता है कि दोनों नॉर्वे के समुद्र से जुड़े हैं।",
  f"{NC11} -- Landforms and their Evolution; {ATLAS} -- Europe (economic).",
  "geo-norway-fjords-oil")

A(WR, "medium",
  "Ships passing through the Panama Canal are raised and lowered by locks, whereas the Suez Canal has no locks.",
  "पनामा नहर से गुज़रने वाले जहाज़ों को लॉक (जलपाश) द्वारा ऊपर उठाया और नीचे उतारा जाता है, जबकि स्वेज़ नहर में कोई लॉक नहीं है।",
  "The Panama Canal crosses land that rises well above sea level, whereas the Suez Canal runs through flat, low-lying land.",
  "पनामा नहर समुद्र तल से काफ़ी ऊँची उठी भूमि को पार करती है, जबकि स्वेज़ नहर समतल, निचली भूमि से होकर जाती है।",
  0,
  "Both statements are correct and Statement-II explains Statement-I. The Panama Canal lifts ships about 26 m to the artificial Gatun Lake to cross the hilly isthmus and lowers them again at the other end. The Suez Canal crosses the flat desert of the Isthmus of Suez, where the Mediterranean and the Red Sea are at nearly the same level, so it is a sea-level canal.",
  "दोनों कथन सही हैं और कथन-II कथन-I की व्याख्या करता है। पहाड़ी स्थलडमरूमध्य को पार करने के लिए पनामा नहर जहाज़ों को लगभग 26 मीटर ऊपर कृत्रिम गाटुन झील तक उठाती है और दूसरे छोर पर फिर नीचे उतारती है। स्वेज़ नहर स्वेज़ स्थलडमरूमध्य के समतल मरुस्थल से होकर जाती है, जहाँ भूमध्य सागर और लाल सागर लगभग एक ही तल पर हैं, इसलिए यह समुद्र-तल वाली नहर है।",
  f"{ATLAS} -- World (transport).",
  "geo-panama-locks-suez")

A(WR, "medium",
  "Mount Everest is the tallest mountain on the Earth when measured from its base to its summit.",
  "आधार से शिखर तक मापने पर माउंट एवरेस्ट पृथ्वी का सबसे ऊँचा पर्वत है।",
  "Mauna Kea in Hawaii rises more than 10,000 m from its base on the ocean floor.",
  "हवाई का मौना की (Mauna Kea) समुद्र तल पर स्थित अपने आधार से 10,000 मीटर से अधिक ऊँचा उठता है।",
  3,
  "Statement-I is incorrect but Statement-II is correct. Everest (8,849 m) has the highest summit above sea level, but it rises from the already high Tibetan Plateau. Mauna Kea, a volcano, stands only about 4,200 m above sea level, yet most of it is under water: measured from its base on the Pacific floor it is over 10,000 m -- taller than Everest.",
  "कथन-I गलत है पर कथन-II सही है। एवरेस्ट (8,849 मीटर) का शिखर समुद्र तल से सबसे ऊँचा है, पर यह पहले से ऊँचे तिब्बती पठार से उठता है। ज्वालामुखी मौना की समुद्र तल से केवल लगभग 4,200 मीटर ऊँचा है, पर इसका अधिकांश भाग जल के नीचे है: प्रशांत महासागर के तल पर स्थित आधार से मापने पर यह 10,000 मीटर से अधिक है, यानी एवरेस्ट से भी ऊँचा।",
  f"{ATLAS} -- World (physical).",
  "geo-everest-mauna-kea-base")

A(WR, "easy",
  "The Sahara has very little natural vegetation.",
  "सहारा में प्राकृतिक वनस्पति बहुत कम है।",
  "The Sahara lies entirely in the Northern Hemisphere.",
  "सहारा पूरी तरह उत्तरी गोलार्ध में स्थित है।",
  1,
  "Both statements are correct, but Statement-II does not explain Statement-I. The Sahara is bare because it gets very little rain and has extreme temperatures and high evaporation, not because of which hemisphere it is in -- the Kalahari and the Australian deserts are in the Southern Hemisphere, while many Northern Hemisphere lands are forested.",
  "दोनों कथन सही हैं, पर कथन-II कथन-I की व्याख्या नहीं करता। सहारा इसलिए वनस्पतिहीन है कि वहाँ बहुत कम वर्षा होती है, तापमान अत्यधिक रहता है और वाष्पीकरण तेज़ होता है, इसलिए नहीं कि वह किस गोलार्ध में है; कालाहारी और ऑस्ट्रेलिया के मरुस्थल दक्षिणी गोलार्ध में हैं, जबकि उत्तरी गोलार्ध के बहुत-से भूभाग वनों से ढके हैं।",
  f"{NC7} -- Life in the Deserts.",
  "geo-sahara-vegetation-hemisphere-easy")

A(WR, "hard",
  "The Aral Sea has shrunk to a small fraction of its former size since the 1960s.",
  "1960 के दशक से अरल सागर सिकुड़कर अपने पुराने आकार का एक छोटा-सा भाग रह गया है।",
  "The Amu Darya and Syr Darya rivers that fed it were diverted on a large scale to irrigate cotton fields.",
  "इसे जल देने वाली अमु दरिया और सिर दरिया नदियों का जल कपास के खेतों की सिंचाई के लिए बड़े पैमाने पर मोड़ दिया गया।",
  2,
  "Only Statement II is correct, and it explains Statement I. Once the fourth-largest lake in the world, the Aral Sea began to dry up after Soviet planners diverted its two feeder rivers for cotton; it has split into separate bodies, leaving a salty, dusty seabed and a ruined fishing industry. A dam built by Kazakhstan has partly revived the small northern part. "
  "Statement III is wrong: the Aral Sea lies between Kazakhstan and Uzbekistan; Turkmenistan lies to the south, along the lower Amu Darya.",
  "केवल कथन II सही है, और वह कथन I की व्याख्या करता है। कभी विश्व की चौथी सबसे बड़ी झील रहा अरल सागर तब सूखने लगा जब सोवियत योजनाकारों ने कपास के लिए इसकी दोनों पोषक नदियों का जल मोड़ दिया; यह अलग-अलग जलाशयों में बँट गया है, और पीछे खारा, धूल भरा तल और उजड़ा मत्स्य उद्योग रह गया है। कज़ाख़स्तान द्वारा बनाए एक बाँध से इसका छोटा उत्तरी भाग आंशिक रूप से फिर भरा है। "
  "कथन III गलत है: अरल सागर कज़ाख़स्तान और उज़्बेकिस्तान के बीच है; तुर्कमेनिस्तान इसके दक्षिण में, अमु दरिया के निचले भाग के साथ है।",
  f"{ATLAS} -- Asia (physical); United Nations Environment Programme -- The Aral Sea crisis.",
  "geo-aral-sea-shrinking",
  s3="The Aral Sea lies on the border between Kazakhstan and Turkmenistan.",
  s3_hi="अरल सागर कज़ाख़स्तान और तुर्कमेनिस्तान की सीमा पर स्थित है।")

# ================================================================ PAIRS (medium 2, hard 1)
P(WR, "medium", "Consider the following pairs of straits and the water bodies they connect:",
  "जलडमरूमध्यों और उनके द्वारा जोड़े जाने वाले जल निकायों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Bosporus : Black Sea and Sea of Marmara", "Dardanelles : Sea of Marmara and Aegean Sea",
   "Strait of Dover : English Channel and North Sea", "Bering Strait : Arctic Ocean and Atlantic Ocean"],
  ["बॉस्पोरस : काला सागर और मरमरा सागर", "डार्डनेल्स : मरमरा सागर और एजियन सागर",
   "डोवर जलडमरूमध्य : इंग्लिश चैनल और उत्तरी सागर", "बेरिंग जलडमरूमध्य : आर्कटिक महासागर और अटलांटिक महासागर"],
  2,
  "Pairs 1, 2 and 3 are correct. The Bosporus (at Istanbul) and the Dardanelles, with the Sea of Marmara between them, form the Turkish Straits -- the Black Sea's only link to the Mediterranean. The Strait of Dover, the narrowest part of the English Channel, separates England from France. "
  "Pair 4 is wrong: the Bering Strait, between Russia and Alaska, connects the Arctic Ocean with the Pacific; the Arctic meets the Atlantic through the waters between Greenland and Norway.",
  "युग्म 1, 2 और 3 सही हैं। बॉस्पोरस (इस्तांबुल पर) और डार्डनेल्स, जिनके बीच मरमरा सागर है, मिलकर तुर्की जलडमरूमध्य बनाते हैं, जो काला सागर का भूमध्य सागर से एकमात्र संपर्क है। इंग्लिश चैनल का सबसे संकरा भाग, डोवर जलडमरूमध्य, इंग्लैंड को फ़्रांस से अलग करता है। "
  "युग्म 4 गलत है: रूस और अलास्का के बीच स्थित बेरिंग जलडमरूमध्य आर्कटिक महासागर को प्रशांत महासागर से जोड़ता है; आर्कटिक, ग्रीनलैंड और नॉर्वे के बीच के जल से होकर अटलांटिक से मिलता है।",
  f"{ATLAS} -- World (physical).",
  "geo-straits-pairs")

P(WR, "medium", "Consider the following pairs of rivers and the countries in which they reach the sea:",
  "नदियों और उन देशों के निम्नलिखित युग्मों पर विचार कीजिए जहाँ वे समुद्र में मिलती हैं:",
  ["Mekong : Vietnam", "Irrawaddy : Thailand", "Indus : Pakistan", "Amur : China"],
  ["मेकांग : वियतनाम", "इरावदी : थाईलैंड", "सिंधु : पाकिस्तान", "आमूर : चीन"],
  1,
  "Pairs 1 and 3 are correct: the Mekong, after flowing through or along China, Myanmar, Laos, Thailand and Cambodia, forms a vast delta in southern Vietnam; the Indus reaches the Arabian Sea south of Karachi. "
  "Pair 2 is wrong: the Irrawaddy flows entirely through Myanmar to a delta on the Andaman Sea. "
  "Pair 4 is wrong: the Amur forms a long stretch of the China-Russia border, but its lower course and mouth, on the Strait of Tartary, are in Russia.",
  "युग्म 1 और 3 सही हैं: मेकांग चीन, म्यांमार, लाओस, थाईलैंड और कंबोडिया से होकर या उनकी सीमा के साथ बहने के बाद दक्षिणी वियतनाम में एक विशाल डेल्टा बनाती है; सिंधु कराची के दक्षिण में अरब सागर में मिलती है। "
  "युग्म 2 गलत है: इरावदी पूरी तरह म्यांमार से होकर बहती है और अंडमान सागर पर डेल्टा बनाती है। "
  "युग्म 4 गलत है: आमूर चीन-रूस सीमा का लंबा भाग बनाती है, पर उसका निचला मार्ग और मुहाना, तातार जलडमरूमध्य पर, रूस में है।",
  f"{ATLAS} -- Asia (physical).",
  "geo-river-mouths-pairs")

P(WR, "hard", "Consider the following pairs of lakes and the countries in which they lie:",
  "झीलों और उन देशों के निम्नलिखित युग्मों पर विचार कीजिए जिनमें वे स्थित हैं:",
  ["Lake Maracaibo : Venezuela", "Lake Balkhash : Kazakhstan", "Lake Tanganyika : Ethiopia", "Great Bear Lake : United States"],
  ["माराकाइबो झील : वेनेज़ुएला", "बल्खश झील : कज़ाख़स्तान", "तांगानिका झील : इथियोपिया", "ग्रेट बेयर झील : संयुक्त राज्य अमेरिका"],
  1,
  "Pairs 1 and 2 are correct: Lake Maracaibo, open to the Caribbean through a narrow channel, lies over one of Venezuela's great oilfields; Lake Balkhash in Kazakhstan is unusual in being fresh in its western half and salty in its eastern half. "
  "Pair 3 is wrong: Lake Tanganyika, the second-deepest lake in the world, lies in the western arm of the East African Rift, shared by Tanzania, the Democratic Republic of the Congo, Burundi and Zambia. "
  "Pair 4 is wrong: Great Bear Lake, the largest lake entirely within Canada, lies in the Northwest Territories -- the 'Great' in its name tempts students to link it with the Great Lakes.",
  "युग्म 1 और 2 सही हैं: एक संकरी जलधारा से कैरिबियन से जुड़ी माराकाइबो झील वेनेज़ुएला के एक बड़े तेल क्षेत्र के ऊपर है; कज़ाख़स्तान की बल्खश झील इस बात में अनोखी है कि इसका पश्चिमी आधा भाग मीठा और पूर्वी आधा भाग खारा है। "
  "युग्म 3 गलत है: विश्व की दूसरी सबसे गहरी झील तांगानिका पूर्वी अफ़्रीकी भ्रंश की पश्चिमी शाखा में है और तंज़ानिया, कांगो लोकतांत्रिक गणराज्य, बुरुंडी तथा ज़ाम्बिया में साझा है। "
  "युग्म 4 गलत है: पूरी तरह कनाडा में स्थित सबसे बड़ी झील ग्रेट बेयर झील नॉर्थवेस्ट टेरिटरीज़ में है; इसके नाम का 'ग्रेट' विद्यार्थियों को इसे महान झीलों (Great Lakes) से जोड़ने के लिए ललचाता है।",
  f"{ATLAS} -- World (physical).",
  "geo-lakes-countries-pairs")

if __name__ == "__main__":
    write("geo_l2_t12_world_regions.sql")
