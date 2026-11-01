# -*- coding: utf-8 -*-
"""Current Affairs · Test 3 (July to September 2026) -- part F: History and Culture.

The quarter's history items come from a new World Heritage listing and from anniversaries, framed on the history behind
them rather than the day: Sarnath on the World Heritage List, the Non-Aligned Movement at 65, the Indo-Soviet treaty at
55, Pingali Venkayya at 150, the Geological Survey of India at 175 and Syama Prasad Mookerjee at 125. No stem carries a
date (design doc, section 7). Every fact was searched in the whole UPSC bank and is one no row tests."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, C, write
from polity_common import C3, C4, T2
from ca_common import MX, finish
from ca_t3_format import FORMAT, POS

d.SUBJECT = "History"
d.REQUIRE_CRAFT = True
AN, AC, MO, PI = "Ancient India", "Art & Culture", "Modern India", "Post-Independence India"

S(AC, "medium", "Sarnath has been inscribed on the UNESCO World Heritage List. Consider the following statements:",
  "सारनाथ को यूनेस्को की विश्व धरोहर सूची में अंकित किया गया है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The inscribed property includes the Chaukhandi Stupa, whose octagonal brick tower was raised in the reign of Ashoka.",
   "With Sarnath, all four principal sites of the Buddha's life -- Lumbini, Bodh Gaya, Sarnath and Kushinagar -- are now World Heritage properties.",
   "It was inscribed under criteria that include its direct association with ideas and beliefs of outstanding universal significance."],
  ["अंकित संपत्ति में चौखंडी स्तूप शामिल है, जिसका अष्टकोणीय ईंट का मीनार अशोक के शासनकाल में बना था।",
   "सारनाथ के साथ बुद्ध के जीवन के चारों प्रमुख स्थल -- लुंबिनी, बोधगया, सारनाथ और कुशीनगर -- अब विश्व धरोहर संपत्तियाँ हैं।",
   "इसे उन मानदंडों के अंतर्गत अंकित किया गया जिनमें उत्कृष्ट सार्वभौमिक महत्त्व के विचारों और आस्थाओं से इसका प्रत्यक्ष संबंध शामिल है।"],
  C3, 0,
  "Only statement 3 is correct. Sarnath, where the Buddha gave his first sermon to five former companions and founded the Sangha, was inscribed in July 2026 at the 48th session of the World Heritage Committee, in Busan, as India's 45th World Heritage property, under criteria (iii) and (vi); criterion (vi) covers association with events, living traditions, ideas or beliefs. It had been on India's Tentative List since 1998. "
  "Statement 1 is wrong: the Chaukhandi Stupa is an earlier, Gupta-period terraced mound marking where the Buddha met his companions, but the octagonal tower on top was built in 1588, under Akbar, by Govardhan, son of Raja Todar Mal, to mark Humayun's visit, as its Persian inscription records. Statement 2 is wrong: Lumbini (1997, in Nepal), the Mahabodhi Temple at Bodh Gaya (2002) and now Sarnath are listed, but Kushinagar, the place of the Buddha's parinirvana, is not.",
  "केवल कथन 3 सही है। सारनाथ, जहाँ बुद्ध ने पाँच पूर्व साथियों को पहला उपदेश दिया और संघ की स्थापना की, जुलाई 2026 में बुसान में विश्व धरोहर समिति के 48वें सत्र में भारत की 45वीं विश्व धरोहर संपत्ति के रूप में मानदंड (iii) और (vi) के अंतर्गत अंकित हुआ; मानदंड (vi) घटनाओं, जीवंत परंपराओं, विचारों या आस्थाओं से संबंध को समेटता है। यह 1998 से भारत की संभावित सूची में था। "
  "कथन 1 ग़लत है: चौखंडी स्तूप एक पहले का, गुप्तकालीन सीढ़ीदार टीला है जो उस स्थान को चिह्नित करता है जहाँ बुद्ध अपने साथियों से मिले, पर उसके ऊपर का अष्टकोणीय मीनार 1588 में अकबर के समय राजा टोडरमल के पुत्र गोवर्धन ने हुमायूँ के आगमन की स्मृति में बनवाया, जैसा उसका फ़ारसी अभिलेख बताता है। कथन 2 ग़लत है: लुंबिनी (1997, नेपाल में), बोधगया का महाबोधि मंदिर (2002) और अब सारनाथ सूचीबद्ध हैं, पर बुद्ध के परिनिर्वाण का स्थान कुशीनगर नहीं है।",
  "UNESCO World Heritage Centre, decisions of the 48th session of the World Heritage Committee (July 2026) and Tentative List entry for Sarnath (1998); Archaeological Survey of India, Sarnath Circle.",
  "ca-t3-his-sarnath-whs-chaukhandi-1588-kushinagar-not", craft="precision")

S(PI, "medium", "The Non-Aligned Movement completed 65 years in 2026. Consider the following statements:",
  "गुटनिरपेक्ष आंदोलन ने 2026 में 65 वर्ष पूरे किए। निम्नलिखित कथनों पर विचार कीजिए:",
  ["Its first summit was held at Belgrade.",
   "India hosted one of its summits, in New Delhi.",
   "Its founding principles drew on the ten principles adopted at the Asian-African Conference at Bandung."],
  ["इसका पहला शिखर सम्मेलन बेलग्रेड में हुआ था।",
   "भारत ने इसके एक शिखर सम्मेलन की मेज़बानी नई दिल्ली में की।",
   "इसके संस्थापक सिद्धांत बांडुंग में हुए एशियाई-अफ़्रीकी सम्मेलन में अपनाए गए दस सिद्धांतों पर आधारित थे।"],
  C3, 2,
  "All three statements are correct. The first summit, at Belgrade from 1 to 6 September 1961, brought together 25 countries at the initiative of Tito of Yugoslavia, Nehru, Nasser of Egypt, Sukarno of Indonesia and Nkrumah of Ghana; the movement took as its principles the Ten Principles of Bandung (1955), which grew from the Panchsheel of the 1954 India-China agreement. India hosted the seventh summit, in New Delhi in March 1983, under Indira Gandhi. "
  "The movement has no permanent secretariat: the country holding the chair coordinates its work between summits. Its aim was never neutrality in every dispute but freedom to judge each issue on its merits, outside the two Cold War blocs, which is why it drew most newly independent states.",
  "तीनों कथन सही हैं। 1 से 6 सितंबर 1961 तक बेलग्रेड में हुए पहले शिखर सम्मेलन में यूगोस्लाविया के टीटो, नेहरू, मिस्र के नासिर, इंडोनेशिया के सुकर्णो और घाना के न्क्रूमा की पहल पर 25 देश एकत्र हुए; आंदोलन ने बांडुंग (1955) के दस सिद्धांतों को अपने सिद्धांत बनाया, जो 1954 के भारत-चीन समझौते के पंचशील से निकले थे। भारत ने सातवें शिखर सम्मेलन की मेज़बानी मार्च 1983 में नई दिल्ली में इंदिरा गांधी के नेतृत्व में की। "
  "आंदोलन का कोई स्थायी सचिवालय नहीं है: अध्यक्ष देश शिखर सम्मेलनों के बीच इसके कार्य का समन्वय करता है। इसका उद्देश्य कभी हर विवाद में तटस्थता नहीं, बल्कि शीत युद्ध के दोनों गुटों से बाहर रहकर हर विषय को उसके गुण-दोष पर परखने की स्वतंत्रता था, इसी कारण अधिकांश नव-स्वतंत्र राज्य इसमें आए।",
  "Non-Aligned Movement, history and Final Documents of the summits (Belgrade, 1961; New Delhi, 1983); Ministry of External Affairs.",
  "ca-t3-his-nam-65-belgrade-1961-bandung-new-delhi-1983", craft="linkage")

A(PI, "medium",
  "The Treaty of Peace, Friendship and Cooperation that India signed with the Soviet Union in 1971 bound each country to go to war on the other's side if either was attacked.",
  "भारत द्वारा 1971 में सोवियत संघ के साथ की गई शांति, मैत्री और सहयोग संधि ने हर देश को बाध्य किया कि यदि किसी पर आक्रमण हो तो वह दूसरे की ओर से युद्ध करे।",
  "Under the treaty, the two countries agreed to consult each other immediately if either was attacked or threatened with attack.",
  "संधि के अंतर्गत दोनों देश सहमत हुए कि यदि किसी पर आक्रमण हो या आक्रमण की धमकी हो तो वे तुरंत एक-दूसरे से परामर्श करेंगे।",
  3,
  "Statement I is incorrect but Statement II is correct. Signed in New Delhi on 9 August 1971 by Swaran Singh and Andrei Gromyko, for twenty years, the treaty contained no clause of automatic military help: Article IX pledged each side not to aid a third party in an armed conflict with the other and, if either was attacked or threatened, to 'immediately enter into mutual consultations' and take effective measures. In Article IV the Soviet Union said it respected India's policy of non-alignment. "
  "Signed as refugees from East Pakistan poured into India and the United States drew closer to Pakistan and China, it deterred outside intervention in the war of December 1971 that created Bangladesh. It was replaced in 1993 by a treaty of friendship and cooperation with Russia.",
  "कथन I ग़लत है पर कथन II सही है। 9 अगस्त 1971 को नई दिल्ली में स्वर्ण सिंह और आंद्रेई ग्रोमिको द्वारा बीस वर्षों के लिए हस्ताक्षरित इस संधि में स्वतः सैन्य सहायता का कोई खंड नहीं था: अनुच्छेद IX में हर पक्ष ने वचन दिया कि वह दूसरे के साथ सशस्त्र संघर्ष में किसी तीसरे पक्ष की सहायता नहीं करेगा, और यदि किसी पर आक्रमण हो या धमकी हो, तो वे ‘तुरंत पारस्परिक परामर्श करेंगे’ और प्रभावी उपाय करेंगे। अनुच्छेद IV में सोवियत संघ ने कहा कि वह भारत की गुटनिरपेक्षता की नीति का सम्मान करता है। "
  "पूर्वी पाकिस्तान से शरणार्थियों के भारत आने और संयुक्त राज्य अमेरिका के पाकिस्तान तथा चीन के निकट आने के बीच हस्ताक्षरित इस संधि ने दिसंबर 1971 के उस युद्ध में बाहरी हस्तक्षेप को रोका जिससे बांग्लादेश बना। 1993 में इसका स्थान रूस के साथ मैत्री और सहयोग की संधि ने लिया।",
  "Treaty of Peace, Friendship and Cooperation between India and the Union of Soviet Socialist Republics (9 August 1971), Articles IV and IX; Lok Sabha Debates, 9 August 1971.",
  "ca-t3-his-indo-soviet-treaty-55-consultation-no-war-clause", craft="precision")

S(MO, "medium", "2026 marked the 150th birth anniversary of Pingali Venkayya. Consider the following statements:",
  "2026 में पिंगली वेंकैया की 150वीं जयंती मनाई गई। निम्नलिखित कथनों पर विचार कीजिए:",
  ["He presented a design for a national flag to Gandhi at the meeting of the All-India Congress Committee at Bezwada in 1921.",
   "The flag adopted by the Constituent Assembly in July 1947 had a charkha at its centre.",
   "The Flag Code of India now permits the national flag to be made of polyester and by machine."],
  ["उन्होंने 1921 में बेज़वाड़ा में अखिल भारतीय कांग्रेस समिति की बैठक में गांधी के समक्ष राष्ट्रीय ध्वज का एक डिज़ाइन प्रस्तुत किया।",
   "जुलाई 1947 में संविधान सभा द्वारा अपनाए गए ध्वज के केंद्र में चरखा था।",
   "भारतीय ध्वज संहिता अब राष्ट्रीय ध्वज को पॉलिएस्टर से और मशीन से बनाने की अनुमति देती है।"],
  C3, 1,
  "Statements 1 and 3 are correct. Venkayya, born on 2 August 1876 in the Krishna district of Andhra and a geologist and linguist as well as a freedom fighter, showed Gandhi a red-and-green flag for the two major communities at Bezwada (Vijayawada); a white band and the spinning wheel were added, and in 1931 the Congress adopted a saffron, white and green tricolour with the charkha. The Flag Code was amended at the end of 2021 to allow machine-made and polyester flags, which made the 'Har Ghar Tiranga' campaign possible. "
  "Statement 2 is wrong: on 22 July 1947 the Constituent Assembly kept the colours but replaced the charkha with the Ashoka Chakra from the Sarnath lion capital, a symbol without any party association.",
  "कथन 1 और 3 सही हैं। 2 अगस्त 1876 को आंध्र के कृष्णा ज़िले में जन्मे वेंकैया, जो स्वतंत्रता सेनानी के साथ भूविज्ञानी और भाषाविद भी थे, ने बेज़वाड़ा (विजयवाड़ा) में गांधी को दो प्रमुख समुदायों के लिए लाल-हरा ध्वज दिखाया; उसमें सफ़ेद पट्टी और चरखा जोड़े गए, और 1931 में कांग्रेस ने चरखे वाला केसरिया, सफ़ेद और हरा तिरंगा अपनाया। 2021 के अंत में ध्वज संहिता में संशोधन कर मशीन से बने और पॉलिएस्टर के ध्वजों की अनुमति दी गई, जिससे ‘हर घर तिरंगा’ अभियान संभव हुआ। "
  "कथन 2 ग़लत है: 22 जुलाई 1947 को संविधान सभा ने रंग बनाए रखे पर चरखे के स्थान पर सारनाथ के सिंह-शीर्ष से अशोक चक्र रखा, जो किसी दल से जुड़ा प्रतीक नहीं था।",
  "Prime Minister's Office and News on AIR, tributes on the 150th birth anniversary of Pingali Venkayya (2 August 2026); Ministry of Home Affairs, Flag Code of India, 2002, as amended in December 2021; Constituent Assembly Debates, 22 July 1947.",
  "ca-t3-his-pingali-venkayya-150-bezwada-1921-flag-code", craft="linkage")

C(MO, "medium", "The Geological Survey of India, which got its first woman Director-General in 2026, was founded 175 years earlier. Arrange the following in the chronological order of their founding:",
  "भारतीय भूवैज्ञानिक सर्वेक्षण, जिसे 2026 में अपनी पहली महिला महानिदेशक मिली, 175 वर्ष पहले स्थापित हुआ था। निम्नलिखित को उनकी स्थापना के कालानुक्रम में व्यवस्थित कीजिए:",
  ["Botanical Survey of India", "Geological Survey of India", "Zoological Survey of India", "Archaeological Survey of India"],
  ["भारतीय वनस्पति सर्वेक्षण", "भारतीय भूवैज्ञानिक सर्वेक्षण", "भारतीय प्राणी सर्वेक्षण", "भारतीय पुरातत्व सर्वेक्षण"],
  ["4-2-1-3", "2-4-3-1", "2-4-1-3", "4-2-3-1"], 2,
  "The order is 2-4-1-3. The Geological Survey of India was set up in 1851, chiefly to find coal for the steamships and the railways then being planned; the Archaeological Survey followed in 1861, with Alexander Cunningham as its first head; the Botanical Survey in 1890; and the Zoological Survey in 1916, both now in Kolkata under the environment ministry. "
  "The order mirrors the colonial state's priorities: minerals and fuel first, then antiquities, then the cataloguing of plants and animals. Varsha Ashok Aglawe, a palaeontologist who joined the GSI in 1992, became its 54th Director-General, and the first woman to lead it, in August 2026.",
  "क्रम 2-4-1-3 है। भारतीय भूवैज्ञानिक सर्वेक्षण 1851 में मुख्यतः भाप-जहाज़ों और तब नियोजित रेलों के लिए कोयला खोजने हेतु स्थापित हुआ; पुरातत्व सर्वेक्षण 1861 में आया, अलेक्ज़ेंडर कनिंघम इसके पहले प्रमुख थे; वनस्पति सर्वेक्षण 1890 में; और प्राणी सर्वेक्षण 1916 में, दोनों अब कोलकाता में पर्यावरण मंत्रालय के अधीन। "
  "यह क्रम औपनिवेशिक राज्य की प्राथमिकताओं को दिखाता है: पहले खनिज और ईंधन, फिर पुरावशेष, फिर पादपों और प्राणियों की सूची। 1992 में जीएसआई से जुड़ीं जीवाश्म-विज्ञानी वर्षा अशोक अगलावे अगस्त 2026 में इसकी 54वीं महानिदेशक और इसका नेतृत्व करने वाली पहली महिला बनीं।",
  "Ministry of Mines and Geological Survey of India, history of the GSI and appointment of the Director-General (August 2026); Archaeological Survey of India; Botanical Survey of India; Zoological Survey of India.",
  "ca-t3-his-gsi-175-survey-founding-order")
d.ROWS[-1]["question_data"]["craft"] = "precision"

S(PI, "medium", "2026 marked the 125th birth anniversary of Syama Prasad Mookerjee. Consider the following statements:",
  "2026 में श्यामा प्रसाद मुखर्जी की 125वीं जयंती मनाई गई। निम्नलिखित कथनों पर विचार कीजिए:",
  ["He was the Minister for Industry and Supply in the first Union Cabinet after independence.",
   "He resigned from the Cabinet in 1950 in protest against the Nehru-Liaquat Pact.",
   "He founded the Bharatiya Jana Sangh in 1951."],
  ["वे स्वतंत्रता के बाद पहले केंद्रीय मंत्रिमंडल में उद्योग और आपूर्ति मंत्री थे।",
   "उन्होंने नेहरू-लियाक़त समझौते के विरोध में 1950 में मंत्रिमंडल से त्यागपत्र दिया।",
   "उन्होंने 1951 में भारतीय जनसंघ की स्थापना की।"],
  C3, 2,
  "All three statements are correct. Born in Calcutta on 6 July 1901, Mookerjee became Vice-Chancellor of Calcutta University at 33 and served in Nehru's first Cabinet, where the Industrial Policy Resolution of 1948 was framed. The Nehru-Liaquat Pact of April 1950 left the protection of minorities in each country to that country's government; arguing that it would not protect Hindus in East Pakistan, he resigned with K.C. Neogy, and in October 1951 founded the Bharatiya Jana Sangh. "
  "He died in detention in Srinagar in June 1953, after entering Jammu and Kashmir without the permit then required, in a campaign against the State's separate status. The Union government and West Bengal marked the anniversary with public events.",
  "तीनों कथन सही हैं। 6 जुलाई 1901 को कलकत्ता में जन्मे मुखर्जी 33 वर्ष की आयु में कलकत्ता विश्वविद्यालय के कुलपति बने और नेहरू के पहले मंत्रिमंडल में रहे, जहाँ 1948 का औद्योगिक नीति संकल्प बना। अप्रैल 1950 के नेहरू-लियाक़त समझौते ने हर देश में अल्पसंख्यकों की रक्षा उसी देश की सरकार पर छोड़ी; यह तर्क देते हुए कि इससे पूर्वी पाकिस्तान के हिंदुओं की रक्षा नहीं होगी, उन्होंने के.सी. नियोगी के साथ त्यागपत्र दिया, और अक्टूबर 1951 में भारतीय जनसंघ की स्थापना की। "
  "जून 1953 में श्रीनगर में निरोध में उनकी मृत्यु हुई, जब वे राज्य की अलग स्थिति के विरुद्ध अभियान में तब आवश्यक परमिट के बिना जम्मू और कश्मीर में प्रवेश कर गए थे। केंद्र सरकार और पश्चिम बंगाल ने जयंती पर सार्वजनिक कार्यक्रम किए।",
  "Vice-President's Secretariat and Ministry of Culture, observance of the 125th birth anniversary of Dr. Syama Prasad Mookerjee (6 July 2026); Lok Sabha Secretariat, biographical records; Nehru-Liaquat Agreement (8 April 1950).",
  "ca-t3-his-syama-prasad-mookerjee-125-industry-liaquat-bjs", craft="precision")

finish("ca_t3_f.sql", FORMAT, "2026-Q3", update="--update" in sys.argv)
