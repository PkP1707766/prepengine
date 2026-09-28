# -*- coding: utf-8 -*-
"""Audit fixes for Environment, Polity and one Geography row (2026-09-28).

1. Answer spread. In the Environment bank, 12 of 17 three-statement "how many" rows
   answered "Only two", no four-statement row answered "Only one", and no two-statement
   row answered "Neither 1 nor 2". A student who sits several papers learns such a skew.
   Sixteen rows are re-seeded (one or two statements changed, explanation rewritten).
2. Two trivial one-liners are replaced by questions on a real distinction.
3. MCQs whose correct option was the longest or most qualified get balanced options.
4. Polity: the MGNREGA question is out of date -- the Viksit Bharat-Guarantee for Rozgar
   and Ajeevika Mission (Gramin) Act, 2025 repealed the MGNREGA -- and one veto
   statement is reworded so it stays true after the 2025 Presidential Reference.
Every rewritten row carries Hindi."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from rewrite_common import S, M, O, A, write
from polity_common import C3, C4, T2

BIO12 = "NCERT Class XII, Biology"
IUCN = "IUCN Red List of Threatened Species"

# ---------------------------------------------------------------- C3 re-seeds ---------
S("d365a160-125c-47df-87f8-a6e8f9df47b1", "Fauna & Animal Behaviour", "medium",
  "Consider the following statements about the Nilgiri tahr:",
  "नीलगिरि तहर के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is chiefly a browser of dense evergreen forest interiors and avoids open grassland.",
   "Silent Valley National Park in Kerala holds the largest single population of the species.",
   "It is endemic to the Western Ghats and is the State animal of Tamil Nadu."],
  ["यह मुख्य रूप से घने सदाबहार वनों के भीतर पत्तियाँ चरने वाला जीव है और खुले घास के मैदानों से दूर रहता है।",
   "केरल के साइलेंट वैली राष्ट्रीय उद्यान में इस प्रजाति की सबसे बड़ी एकल आबादी है।",
   "यह पश्चिमी घाट का स्थानिक (endemic) जीव है और तमिलनाडु का राज्य पशु है।"],
  C3, 0,
  "Only statement 3 is correct. The Nilgiri tahr (Nilgiritragus hylocrius), an Endangered mountain goat, is found only in the southern Western Ghats of Kerala and Tamil Nadu, and is Tamil Nadu's State animal. "
  "Statement 1 is incorrect: it grazes the open montane grasslands of the shola-grassland landscape and keeps close to cliffs, rather than living inside dense forest. "
  "Statement 2 is incorrect: the largest single population is in Eravikulam National Park near Munnar, which was set up largely to protect it.",
  "केवल कथन 3 सही है। नीलगिरि तहर (Nilgiritragus hylocrius), एक संकटग्रस्त (Endangered) पहाड़ी बकरी, केवल केरल और तमिलनाडु के दक्षिणी पश्चिमी घाट में मिलती है, और तमिलनाडु का राज्य पशु है। "
  "कथन 1 गलत है: यह शोला-घास के मैदान वाले भू-दृश्य के खुले पहाड़ी घास के मैदानों में चरती है और खड़ी चट्टानों के पास रहती है, घने वन के भीतर नहीं। "
  "कथन 2 गलत है: इसकी सबसे बड़ी एकल आबादी मुन्नार के पास एराविकुलम राष्ट्रीय उद्यान में है, जिसकी स्थापना मुख्य रूप से इसी की रक्षा के लिए हुई थी।",
  f"{IUCN}: Nilgiritragus hylocrius; Kerala Forest Department -- Eravikulam National Park.",
  "env-nilgiri-tahr-habitat")

S("c66d3445-41e9-4b2e-a09f-97b88f2e9ea6", "Fauna & Animal Behaviour", "medium",
  "Consider the following statements about the red panda:",
  "लाल पांडा के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It belongs to the same family as the giant panda.",
   "It is the State animal of Sikkim.",
   "It is listed as Critically Endangered on the IUCN Red List."],
  ["यह विशाल पांडा (giant panda) के ही कुल (family) का सदस्य है।",
   "यह सिक्किम का राज्य पशु है।",
   "IUCN रेड लिस्ट में इसे गंभीर रूप से संकटग्रस्त (Critically Endangered) श्रेणी में रखा गया है।"],
  C3, 0,
  "Only statement 2 is correct: the red panda is Sikkim's State animal, and the Padmaja Naidu Himalayan Zoological Park at Darjeeling runs a breeding programme for it. "
  "Statement 1 is incorrect: it is the only living member of its own family, Ailuridae; the giant panda is a bear (Ursidae), and the two share only a false 'thumb' and a bamboo diet. "
  "Statement 3 is incorrect: the IUCN lists it as Endangered, not Critically Endangered.",
  "केवल कथन 2 सही है: लाल पांडा सिक्किम का राज्य पशु है, और दार्जिलिंग का पद्मजा नायडू हिमालयन प्राणी उद्यान इसके प्रजनन का कार्यक्रम चलाता है। "
  "कथन 1 गलत है: यह अपने ही कुल, एलुरिडी (Ailuridae), का एकमात्र जीवित सदस्य है; विशाल पांडा एक भालू (Ursidae) है, और दोनों में केवल एक नकली 'अंगूठा' और बाँस का आहार समान है। "
  "कथन 3 गलत है: IUCN इसे संकटग्रस्त (Endangered) मानता है, गंभीर रूप से संकटग्रस्त नहीं।",
  f"{IUCN}: Ailurus fulgens; Sikkim Forest Department -- State symbols.",
  "env-red-panda")

S("3b1d04b7-2809-4844-bc49-0e76290a9820", "Fauna & Animal Behaviour", "hard",
  "Consider the following statements about the king cobra:",
  "किंग कोबरा (नागराज) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is the longest venomous snake in the world.",
   "The female is the only snake known to build a nest for its eggs.",
   "It feeds mainly on other snakes."],
  ["यह विश्व का सबसे लंबा विषैला साँप है।",
   "इसकी मादा एकमात्र ऐसी साँप है जो अपने अंडों के लिए घोंसला बनाने के लिए जानी जाती है।",
   "यह मुख्य रूप से दूसरे साँपों को खाता है।"],
  C3, 2,
  "All three statements are correct. King cobras can exceed five metres, the longest of all venomous snakes. The female gathers leaf litter into a mound-nest and guards the eggs, which no other snake is known to do. "
  "Its genus name, Ophiophagus, means 'snake-eater': rat snakes and other snakes are its main prey. It is not a 'true' cobra of the genus Naja. "
  "(A 2024 study split the king cobra into four species, including Ophiophagus kaalinga of the Western Ghats.)",
  "तीनों कथन सही हैं। किंग कोबरा पाँच मीटर से भी लंबा हो सकता है, जो सभी विषैले साँपों में सबसे लंबा है। मादा पत्तियों को इकट्ठा करके टीले जैसा घोंसला बनाती है और अंडों की रखवाली करती है; कोई और साँप ऐसा करता नहीं जाना गया। "
  "इसके वंश का नाम ओफ़ियोफ़ैगस (Ophiophagus) का अर्थ है 'साँप खाने वाला': धामन और दूसरे साँप इसका मुख्य शिकार हैं। यह नाजा (Naja) वंश का 'असली' कोबरा नहीं है। "
  "(2024 के एक अध्ययन ने किंग कोबरा को चार प्रजातियों में बाँटा, जिनमें पश्चिमी घाट की Ophiophagus kaalinga भी है।)",
  f"{IUCN}: Ophiophagus hannah; Zoological Survey of India -- reptiles of India.",
  "env-king-cobra")

S("a49ffc71-9cf4-46f4-bd2e-6b1a0753b5ba", "Pollution, Waste & Resources", "medium",
  "Consider the following statements about eutrophication:",
  "सुपोषण (eutrophication) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Algal blooms caused by eutrophication raise the dissolved oxygen of the water at night.",
   "It is the enrichment of a water body with nutrients, chiefly sulphates and chlorides.",
   "Accelerated (cultural) eutrophication is caused by human activities such as the discharge of sewage and the run-off of fertilisers."],
  ["सुपोषण से होने वाले शैवाल प्रस्फुटन (algal bloom) रात में पानी की घुली हुई ऑक्सीजन बढ़ा देते हैं।",
   "यह किसी जलाशय में पोषक तत्वों, मुख्यतः सल्फ़ेट और क्लोराइड, की वृद्धि है।",
   "त्वरित (सांस्कृतिक) सुपोषण मानवीय गतिविधियों, जैसे सीवेज के बहाव और उर्वरकों के बहकर आने, से होता है।"],
  C3, 0,
  "Only statement 3 is correct: sewage, detergents and fertiliser run-off speed up the natural, slow ageing of a lake many times over. "
  "Statement 2 is incorrect: the nutrients that drive it are chiefly nitrates and phosphates. "
  "Statement 1 is incorrect: at night the algae respire and consume oxygen, and when the bloom dies, bacteria decomposing it use up still more, so dissolved oxygen falls -- leading to fish kills and 'dead zones'.",
  "केवल कथन 3 सही है: सीवेज, डिटर्जेंट और उर्वरकों का बहाव झील के प्राकृतिक, धीमे बूढ़े होने की प्रक्रिया को कई गुना तेज़ कर देता है। "
  "कथन 2 गलत है: इसे बढ़ाने वाले पोषक तत्व मुख्यतः नाइट्रेट और फ़ॉस्फ़ेट हैं। "
  "कथन 1 गलत है: रात में शैवाल श्वसन करते हैं और ऑक्सीजन लेते हैं, और प्रस्फुटन के नष्ट होने पर उसे सड़ाने वाले जीवाणु और अधिक ऑक्सीजन खर्च करते हैं, इसलिए घुली ऑक्सीजन घटती है; इससे मछलियाँ मरती हैं और 'मृत क्षेत्र' (dead zones) बनते हैं।",
  f"{BIO12} -- Environmental Issues (water pollution and its control).",
  "env-eutrophication")

S("3e3864f8-9751-42f0-8e7b-46e98919b5b7", "Pollution, Waste & Resources", "medium",
  "Consider the following statements about Bharat Stage VI (BS-VI) emission norms:",
  "भारत स्टेज VI (BS-VI) उत्सर्जन मानकों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["They apply only to diesel vehicles.",
   "India moved to them directly from BS-IV, skipping BS-V, from 1 April 2020.",
   "BS-VI fuel has a maximum sulphur content of 50 parts per million."],
  ["ये केवल डीज़ल वाहनों पर लागू होते हैं।",
   "भारत 1 अप्रैल 2020 से BS-V को छोड़कर सीधे BS-IV से इन मानकों पर आ गया।",
   "BS-VI ईंधन में गंधक (सल्फ़र) की अधिकतम मात्रा 50 पार्ट्स पर मिलियन (ppm) है।"],
  C3, 0,
  "Only statement 2 is correct: India leapfrogged from BS-IV to BS-VI nationwide on 1 April 2020, and the Supreme Court barred the sale of BS-IV vehicles after 31 March 2020. "
  "Statement 1 is incorrect: the norms cover petrol and diesel vehicles alike (they cut NOx sharply for diesel vehicles and particulate limits apply to petrol direct-injection engines too). "
  "Statement 3 is incorrect: BS-VI fuel is limited to 10 ppm of sulphur; 50 ppm was the BS-IV limit.",
  "केवल कथन 2 सही है: भारत 1 अप्रैल 2020 को पूरे देश में BS-IV से सीधे BS-VI पर पहुँचा, और उच्चतम न्यायालय ने 31 मार्च 2020 के बाद BS-IV वाहनों की बिक्री पर रोक लगा दी। "
  "कथन 1 गलत है: ये मानक पेट्रोल और डीज़ल, दोनों वाहनों पर लागू हैं (इनसे डीज़ल वाहनों का NOx बहुत घटता है, और कणिका सीमाएँ पेट्रोल डायरेक्ट-इंजेक्शन इंजनों पर भी लागू हैं)। "
  "कथन 3 गलत है: BS-VI ईंधन में सल्फ़र की सीमा 10 ppm है; 50 ppm BS-IV की सीमा थी।",
  "Ministry of Road Transport and Highways, notification on BS-VI norms (G.S.R. 889(E), 2016); M.C. Mehta v. Union of India, order of 24 October 2018.",
  "env-bs-vi-norms")

S("efd53e85-cc10-4dda-876a-1e173343c285", "Protected Areas & Wildlife Protection", "hard",
  "Consider the following statements about Biodiversity Heritage Sites:",
  "जैव विविधता विरासत स्थलों (Biodiversity Heritage Sites) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["They are notified by the Central Government under the Environment (Protection) Act, 1986.",
   "Ameenpur Lake in Telangana was India's first Biodiversity Heritage Site.",
   "Notifying an area as a Biodiversity Heritage Site bans all use of it by local communities."],
  ["इन्हें केंद्र सरकार पर्यावरण (संरक्षण) अधिनियम, 1986 के तहत अधिसूचित करती है।",
   "तेलंगाना की अमीनपुर झील भारत का पहला जैव विविधता विरासत स्थल थी।",
   "किसी क्षेत्र को जैव विविधता विरासत स्थल घोषित करने से स्थानीय समुदायों द्वारा उसके हर प्रकार के उपयोग पर रोक लग जाती है।"],
  C3, 3,
  "None of the statements is correct. Biodiversity Heritage Sites are notified by State Governments, in consultation with local bodies, under Section 37 of the Biological Diversity Act, 2002. "
  "The first was the Nallur Tamarind Grove near Bengaluru (2007); Ameenpur Lake (2016) was the first water body to be declared one. "
  "The guidelines say the notification should not restrict the prevailing practices and uses of local communities, beyond what they themselves agree to -- unlike a national park.",
  "कोई भी कथन सही नहीं है। जैव विविधता विरासत स्थल राज्य सरकारें, स्थानीय निकायों से परामर्श करके, जैव विविधता अधिनियम, 2002 की धारा 37 के तहत अधिसूचित करती हैं। "
  "पहला ऐसा स्थल बेंगलुरु के पास नल्लूर इमली उपवन (2007) था; अमीनपुर झील (2016) इस रूप में घोषित होने वाला पहला जलाशय थी। "
  "दिशानिर्देशों के अनुसार अधिसूचना से स्थानीय समुदायों की चली आ रही प्रथाओं और उपयोगों पर, उनकी अपनी सहमति से आगे, कोई रोक नहीं लगनी चाहिए; राष्ट्रीय उद्यान से यही इसका अंतर है।",
  "Biological Diversity Act, 2002, section 37; National Biodiversity Authority -- Guidelines for the selection and management of Biodiversity Heritage Sites (2009).",
  "env-biodiversity-heritage-sites")

# ---------------------------------------------------------------- C4 re-seeds ---------
S("61d59b2e-13a9-4944-992e-7c12e9282fda", "Climate Science & Mitigation", "hard",
  "Consider the following statements about the 'Keeling Curve':",
  "'कीलिंग वक्र' (Keeling Curve) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It records the atmospheric carbon dioxide concentration measured at Mauna Loa, Hawaii, since 1958.",
   "It shows a seasonal cycle in which carbon dioxide falls during the Northern Hemisphere summer, as land plants take it up.",
   "The pre-industrial concentration of carbon dioxide it is compared with was about 350 parts per million.",
   "The annual average concentration it records has been above 450 parts per million every year since 2020."],
  ["यह 1958 से हवाई के मौना लोआ में मापी गई वायुमंडलीय कार्बन डाइऑक्साइड की सांद्रता दर्ज करता है।",
   "इसमें एक मौसमी चक्र दिखता है, जिसमें उत्तरी गोलार्ध की गर्मियों में स्थलीय पौधों द्वारा अवशोषण के कारण कार्बन डाइऑक्साइड घटती है।",
   "जिस पूर्व-औद्योगिक सांद्रता से इसकी तुलना की जाती है, वह लगभग 350 पार्ट्स पर मिलियन थी।",
   "इसमें दर्ज वार्षिक औसत सांद्रता 2020 से हर वर्ष 450 पार्ट्स पर मिलियन से ऊपर रही है।"],
  C4, 1,
  "Statements 1 and 2 are correct. Charles David Keeling began continuous measurements at Mauna Loa in 1958; the curve's yearly zig-zag reflects the Northern Hemisphere's vegetation drawing down CO2 in summer and releasing it in winter. "
  "Statement 3 is incorrect: the pre-industrial level was about 280 ppm (350 ppm is the level some scientists propose as a safe upper limit). "
  "Statement 4 is incorrect: the annual mean crossed 400 ppm in 2015-16 and was in the low-to-mid 420s by 2024-25, well below 450 ppm.",
  "कथन 1 और 2 सही हैं। चार्ल्स डेविड कीलिंग ने 1958 में मौना लोआ पर लगातार माप शुरू किए; वक्र का वार्षिक टेढ़ा-मेढ़ा रूप उत्तरी गोलार्ध की वनस्पति द्वारा गर्मियों में CO2 सोखने और सर्दियों में छोड़ने को दर्शाता है। "
  "कथन 3 गलत है: पूर्व-औद्योगिक स्तर लगभग 280 ppm था (350 ppm वह स्तर है जिसे कुछ वैज्ञानिक सुरक्षित ऊपरी सीमा मानते हैं)। "
  "कथन 4 गलत है: वार्षिक औसत 2015-16 में 400 ppm के पार गया और 2024-25 तक 420 के दशक के निचले-मध्य भाग में था, यानी 450 ppm से काफ़ी नीचे।",
  "NOAA Global Monitoring Laboratory -- Trends in atmospheric carbon dioxide (Mauna Loa); Scripps Institution of Oceanography -- The Keeling Curve.",
  "env-keeling-curve")

S("7c1bc8b3-136e-4f62-bd13-48a33e71a5af", "Fauna & Animal Behaviour", "hard",
  "Consider the following statements about birds of India:",
  "भारत के पक्षियों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The forest owlet, once thought extinct, was rediscovered in 1997 in the forests of Maharashtra.",
   "Jerdon's courser was rediscovered in 1986 in Kerala.",
   "The pink-headed duck has not been reliably recorded in the wild since the late 1940s.",
   "The Great Indian Bustard is the State bird of Gujarat."],
  ["कभी विलुप्त मान लिया गया वन उल्लू (forest owlet) 1997 में महाराष्ट्र के वनों में फिर से खोजा गया।",
   "जर्डन कोर्सर 1986 में केरल में फिर से खोजा गया।",
   "गुलाबी सिर वाली बतख (pink-headed duck) 1940 के दशक के अंत के बाद से जंगल में विश्वसनीय रूप से दर्ज नहीं हुई है।",
   "सोन चिरैया (Great Indian Bustard) गुजरात का राज्य पक्षी है।"],
  C4, 1,
  "Statements 1 and 3 are correct. The forest owlet was rediscovered in 1997 near Shahada, in the Satpura foothills of Maharashtra, after 113 years without a confirmed record; the pink-headed duck has not been confirmed since 1949 and may be extinct. "
  "Statement 2 is incorrect: Jerdon's courser was rediscovered in 1986 in Andhra Pradesh, in the scrub around the Lankamalleswara Wildlife Sanctuary. "
  "Statement 4 is incorrect: the Great Indian Bustard is the State bird of Rajasthan; Gujarat's is the greater flamingo.",
  "कथन 1 और 3 सही हैं। वन उल्लू 113 वर्षों तक बिना पुष्ट रिकॉर्ड के रहने के बाद 1997 में महाराष्ट्र की सतपुड़ा तलहटी में शहादा के पास फिर से खोजा गया; गुलाबी सिर वाली बतख 1949 के बाद से पुष्ट रूप से नहीं देखी गई और संभवतः विलुप्त हो चुकी है। "
  "कथन 2 गलत है: जर्डन कोर्सर 1986 में आंध्र प्रदेश में, लंकामल्लेश्वर वन्यजीव अभयारण्य के आसपास की झाड़ियों में, फिर से खोजा गया। "
  "कथन 4 गलत है: सोन चिरैया राजस्थान का राज्य पक्षी है; गुजरात का राज्य पक्षी बड़ा राजहंस (greater flamingo) है।",
  f"{IUCN}: Athene blewitti, Rhinoptilus bitorquatus, Rhodonessa caryophyllacea; Bombay Natural History Society -- threatened birds of India.",
  "env-rediscovered-birds")

S("69819611-1d38-45f9-821d-fb7704cbba3a", "Flora, Fungi & Forests", "hard",
  "Consider the following statements about invasive plants in India:",
  "भारत में आक्रामक (invasive) पौधों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Lantana camara was brought to India as an ornamental plant.",
   "Prosopis juliflora, native to Australia, was introduced into India.",
   "Parthenium hysterophorus is native to South-East Asia.",
   "Water hyacinth (Eichhornia crassipes) is native to tropical Africa."],
  ["लैंटाना कैमरा को भारत में एक सजावटी पौधे के रूप में लाया गया था।",
   "ऑस्ट्रेलिया का मूल निवासी प्रोसोपिस जूलीफ़्लोरा भारत में लाया गया।",
   "पार्थेनियम हिस्टेरोफ़ोरस (गाजर घास) दक्षिण-पूर्व एशिया का मूल निवासी है।",
   "जलकुंभी (Eichhornia crassipes) उष्णकटिबंधीय अफ़्रीका की मूल निवासी है।"],
  C4, 0,
  "Only statement 1 is correct: Lantana, native to tropical America, was introduced by the British in the early 19th century as a garden hedge and now covers huge areas of India's forests. "
  "The other three get the origin wrong. Prosopis juliflora (vilayati babul) is native to Mexico, Central and South America; it was introduced to stabilise dry land and now spreads through the Kachchh grasslands. "
  "Parthenium (congress grass) is native to tropical America and is believed to have come with imported wheat in the 1950s. Water hyacinth is native to the Amazon basin of South America.",
  "केवल कथन 1 सही है: उष्णकटिबंधीय अमेरिका का मूल निवासी लैंटाना 19वीं सदी के आरंभ में अंग्रेज़ों द्वारा बगीचे की बाड़ के रूप में लाया गया था और अब भारत के वनों के विशाल क्षेत्र में फैला है। "
  "बाकी तीनों कथन मूल स्थान गलत बताते हैं। प्रोसोपिस जूलीफ़्लोरा (विलायती बबूल) मेक्सिको, मध्य और दक्षिण अमेरिका का मूल निवासी है; इसे शुष्क भूमि को स्थिर करने के लिए लाया गया और अब यह कच्छ के घास के मैदानों में फैल रहा है। "
  "पार्थेनियम (गाजर घास/कांग्रेस घास) उष्णकटिबंधीय अमेरिका का है और माना जाता है कि यह 1950 के दशक में आयातित गेहूँ के साथ आया। जलकुंभी दक्षिण अमेरिका के अमेज़न बेसिन की है।",
  "Botanical Survey of India -- invasive alien flora of India; CABI Invasive Species Compendium (Lantana camara, Prosopis juliflora, Parthenium hysterophorus, Eichhornia crassipes).",
  "env-invasive-plants")

S("55f53856-852e-43fa-a402-67ba44cc08c5", "Pollution, Waste & Resources", "hard",
  "Consider the following statements about radioactive pollutants:",
  "रेडियोधर्मी प्रदूषकों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Strontium-90 tends to accumulate in bones, because the body treats it like calcium.",
   "Iodine-131 has a half-life of about 30 years.",
   "Caesium-137 concentrates mainly in the thyroid gland.",
   "Radon-222 is formed in the decay chain of uranium-238."],
  ["स्ट्रॉन्शियम-90 हड्डियों में जमा होता है, क्योंकि शरीर इसे कैल्शियम की तरह लेता है।",
   "आयोडीन-131 का अर्ध-आयु काल (half-life) लगभग 30 वर्ष है।",
   "सीज़ियम-137 मुख्य रूप से थायरॉइड ग्रंथि में जमा होता है।",
   "रेडॉन-222 यूरेनियम-238 की क्षय-शृंखला (decay chain) में बनता है।"],
  C4, 1,
  "Statements 1 and 4 are correct. Strontium-90 behaves like calcium and lodges in bone; radon-222, a gas, arises from radium-226 in the decay chain of uranium-238. "
  "Statements 2 and 3 swap the properties of the two fission products: iodine-131 has a half-life of about 8 days and concentrates in the thyroid (hence potassium iodide tablets after a nuclear accident), while caesium-137 has a half-life of about 30 years and spreads through the soft tissues and muscles, like potassium.",
  "कथन 1 और 4 सही हैं। स्ट्रॉन्शियम-90 कैल्शियम की तरह व्यवहार करता है और हड्डियों में बैठ जाता है; रेडॉन-222 गैस यूरेनियम-238 की क्षय-शृंखला में रेडियम-226 से बनती है। "
  "कथन 2 और 3 दो विखंडन उत्पादों के गुणों को आपस में बदल देते हैं: आयोडीन-131 का अर्ध-आयु काल लगभग 8 दिन है और यह थायरॉइड में जमा होता है (इसीलिए परमाणु दुर्घटना के बाद पोटैशियम आयोडाइड की गोलियाँ दी जाती हैं), जबकि सीज़ियम-137 का अर्ध-आयु काल लगभग 30 वर्ष है और यह पोटैशियम की तरह कोमल ऊतकों और मांसपेशियों में फैलता है।",
  "World Health Organization -- Radiation: health consequences of the Chernobyl accident; U.S. EPA -- radionuclide fact sheets (iodine, caesium, strontium, radon).",
  "env-radioactive-pollutants")

S("aa0f40fc-443d-48d8-ae9e-dfcc83839572", "Protected Areas & Wildlife Protection", "hard",
  "Consider the following statements about tiger conservation in India:",
  "भारत में बाघ संरक्षण के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Tiger reserves are notified by State Governments on the recommendation of the National Tiger Conservation Authority.",
   "Under the Wildlife (Protection) Act, a tiger reserve consists only of a core or critical tiger habitat, and buffer areas lie outside it.",
   "The 2022 cycle of the All India Tiger Estimation put India's tiger population at about 2,967.",
   "Karnataka had the largest number of tigers in the 2022 estimate."],
  ["बाघ अभयारण्य (tiger reserve) राज्य सरकारें राष्ट्रीय बाघ संरक्षण प्राधिकरण की सिफ़ारिश पर अधिसूचित करती हैं।",
   "वन्यजीव (संरक्षण) अधिनियम के अनुसार बाघ अभयारण्य में केवल कोर या क्रांतिक बाघ आवास होता है, और बफ़र क्षेत्र उसके बाहर होते हैं।",
   "अखिल भारतीय बाघ आकलन के 2022 चक्र में भारत में बाघों की संख्या लगभग 2,967 आँकी गई।",
   "2022 के आकलन में सबसे अधिक बाघ कर्नाटक में थे।"],
  C4, 0,
  "Only statement 1 is correct: under Section 38V of the Wildlife (Protection) Act, a State notifies a tiger reserve on the NTCA's recommendation. "
  "Statement 2 is incorrect: the same section defines a tiger reserve as the core or critical tiger habitat together with the buffer or peripheral area. "
  "Statement 3 is incorrect: 2,967 was the 2018 figure; the 2022 cycle estimated a minimum of 3,167 and a mean of about 3,682. "
  "Statement 4 is incorrect: Madhya Pradesh had the most tigers in 2022 (785), followed by Karnataka (563) and Uttarakhand (560).",
  "केवल कथन 1 सही है: वन्यजीव (संरक्षण) अधिनियम की धारा 38V के तहत राज्य NTCA की सिफ़ारिश पर बाघ अभयारण्य अधिसूचित करता है। "
  "कथन 2 गलत है: वही धारा बाघ अभयारण्य को कोर या क्रांतिक बाघ आवास और बफ़र या परिधीय क्षेत्र, दोनों को मिलाकर परिभाषित करती है। "
  "कथन 3 गलत है: 2,967 का आँकड़ा 2018 का था; 2022 के चक्र में न्यूनतम 3,167 और औसत लगभग 3,682 का अनुमान लगाया गया। "
  "कथन 4 गलत है: 2022 में सबसे अधिक बाघ मध्य प्रदेश में थे (785), उसके बाद कर्नाटक (563) और उत्तराखंड (560)।",
  "Wildlife (Protection) Act, 1972, section 38V; NTCA and Wildlife Institute of India -- Status of Tigers, Co-predators and Prey in India, 2022.",
  "env-tiger-reserves-estimation")

S("144e0734-895d-4dbd-b669-13e0e00816ca", "Pollution, Waste & Resources", "medium",
  "Consider the following statements about the E-Waste (Management) Rules, 2022:",
  "ई-अपशिष्ट (प्रबंधन) नियम, 2022 के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["They came into force on 1 April 2022.",
   "They make producers responsible, through Extended Producer Responsibility, for getting a set share of their e-waste recycled.",
   "They do not cover solar photovoltaic modules, panels and cells.",
   "They are administered by the Bureau of Indian Standards."],
  ["ये 1 अप्रैल 2022 से लागू हुए।",
   "ये विस्तारित उत्पादक उत्तरदायित्व (EPR) के ज़रिए उत्पादकों को अपने ई-अपशिष्ट के एक तय हिस्से का पुनर्चक्रण करवाने के लिए ज़िम्मेदार बनाते हैं।",
   "ये सौर फ़ोटोवोल्टिक मॉड्यूल, पैनल और सेलों पर लागू नहीं होते।",
   "इनका संचालन भारतीय मानक ब्यूरो करता है।"],
  C4, 0,
  "Only statement 2 is correct: producers must meet annual recycling targets by buying EPR certificates generated by registered recyclers. "
  "Statement 1 is incorrect: the Rules were notified in November 2022 and came into force on 1 April 2023. "
  "Statement 3 is incorrect: they have a separate chapter for solar photovoltaic modules, panels and cells, which must be stored and handled as the Rules prescribe. "
  "Statement 4 is incorrect: they are framed under the Environment (Protection) Act, 1986, and the Central Pollution Control Board runs the EPR portal and registration.",
  "केवल कथन 2 सही है: उत्पादकों को पंजीकृत पुनर्चक्रणकर्ताओं द्वारा बनाए गए EPR प्रमाणपत्र खरीदकर वार्षिक पुनर्चक्रण लक्ष्य पूरे करने होते हैं। "
  "कथन 1 गलत है: नियम नवंबर 2022 में अधिसूचित हुए और 1 अप्रैल 2023 से लागू हुए। "
  "कथन 3 गलत है: इनमें सौर फ़ोटोवोल्टिक मॉड्यूल, पैनल और सेलों के लिए अलग अध्याय है, जिनका भंडारण और संचालन नियमों के अनुसार करना होता है। "
  "कथन 4 गलत है: ये पर्यावरण (संरक्षण) अधिनियम, 1986 के तहत बने हैं, और EPR पोर्टल तथा पंजीकरण केंद्रीय प्रदूषण नियंत्रण बोर्ड चलाता है।",
  "Ministry of Environment, Forest and Climate Change -- E-Waste (Management) Rules, 2022 (G.S.R. 801(E), 2 November 2022); CPCB -- EPR portal for e-waste.",
  "env-ewaste-rules-2022")

S("eaff9ba4-9e97-4d27-bb1a-b36f1e4234f6", "Ecosystems & Ecological Processes", "medium",
  "Consider the following statements about ecological succession:",
  "पारिस्थितिक अनुक्रमण (ecological succession) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["In hydrarch succession, the series progresses from hydric towards mesic conditions.",
   "Primary succession begins where no soil existed before, such as on bare rock or newly cooled lava.",
   "Secondary succession is usually faster than primary succession, because soil is already present.",
   "The community that is in near-equilibrium with the environment at the end of a succession is called the climax community."],
  ["जलक्रमक (hydrarch) अनुक्रमण में क्रम जलीय (hydric) अवस्था से मध्यम नमी (mesic) की अवस्था की ओर बढ़ता है।",
   "प्राथमिक अनुक्रमण वहाँ शुरू होता है जहाँ पहले मिट्टी नहीं थी, जैसे नंगी चट्टान या हाल में ठंडा हुआ लावा।",
   "द्वितीयक अनुक्रमण आम तौर पर प्राथमिक अनुक्रमण से तेज़ होता है, क्योंकि मिट्टी पहले से मौजूद होती है।",
   "अनुक्रमण के अंत में पर्यावरण के साथ लगभग संतुलन में रहने वाले समुदाय को चरम समुदाय (climax community) कहते हैं।"],
  C4, 3,
  "All four statements are correct. Hydrarch succession begins in water and moves towards mesic (moderately moist) conditions, while xerarch succession begins in dry areas and also ends in mesic conditions. "
  "Primary succession starts on newly exposed surfaces with no soil, where pioneers such as lichens begin soil formation; secondary succession, after a fire, flood or abandoned farming, is faster because soil and seeds remain. "
  "The stable end stage is the climax community.",
  "चारों कथन सही हैं। जलक्रमक अनुक्रमण पानी में शुरू होकर मध्यम नमी वाली अवस्था की ओर जाता है, जबकि शुष्कक्रमक (xerarch) अनुक्रमण शुष्क क्षेत्रों में शुरू होकर भी मध्यम नमी वाली अवस्था पर ही समाप्त होता है। "
  "प्राथमिक अनुक्रमण बिना मिट्टी वाली नई सतहों पर शुरू होता है, जहाँ लाइकेन जैसे अग्रणी जीव मिट्टी बनाना शुरू करते हैं; आग, बाढ़ या छोड़ी गई खेती के बाद होने वाला द्वितीयक अनुक्रमण तेज़ होता है, क्योंकि मिट्टी और बीज बचे रहते हैं। "
  "स्थिर अंतिम अवस्था चरम समुदाय कहलाती है।",
  f"{BIO12} -- Ecosystem (ecological succession).",
  "env-succession-hydrarch")

# ---------------------------------------------------------------- T2 re-seeds ---------
S("067658a0-d3a7-42de-a968-acd5c48a2118", "Climate Agreements & Carbon Markets", "easy",
  "Consider the following statements about the Kyoto Protocol:",
  "क्योटो प्रोटोकॉल के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It entered into force in 1997.",
   "It set binding emission-reduction targets for developing countries such as India and China."],
  ["यह 1997 में लागू हुआ।",
   "इसने भारत और चीन जैसे विकासशील देशों के लिए बाध्यकारी उत्सर्जन-कटौती लक्ष्य तय किए।"],
  T2, 3,
  "Neither statement is correct. The Protocol was adopted at COP3 in Kyoto in December 1997, but entered into force only on 16 February 2005, after Russia's ratification brought in enough industrialised-country emissions. "
  "Binding targets applied only to the developed and transition economies listed in Annex B; developing countries such as India and China had no binding targets but could host Clean Development Mechanism projects.",
  "कोई भी कथन सही नहीं है। प्रोटोकॉल दिसंबर 1997 में क्योटो में COP3 में अपनाया गया, पर रूस के अनुसमर्थन से औद्योगिक देशों के उत्सर्जन का पर्याप्त हिस्सा शामिल होने के बाद ही 16 फ़रवरी 2005 को लागू हुआ। "
  "बाध्यकारी लक्ष्य केवल अनुलग्नक B (Annex B) में सूचीबद्ध विकसित और संक्रमणशील अर्थव्यवस्थाओं पर लागू थे; भारत और चीन जैसे विकासशील देशों पर कोई बाध्यकारी लक्ष्य नहीं था, पर वे स्वच्छ विकास तंत्र (CDM) की परियोजनाएँ चला सकते थे।",
  "UNFCCC -- What is the Kyoto Protocol?; Kyoto Protocol, Articles 3 and 25 and Annex B.",
  "env-kyoto-protocol-targets")

S("79cb53fd-f693-45d1-b72f-efa6924bab8f", "Fauna & Animal Behaviour", "easy",
  "Consider the following statements about echolocation:",
  "प्रतिध्वनि-निर्धारण (echolocation) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Bats and owls both use echolocation to find their prey in the dark.",
   "Echolocation is used only by nocturnal animals."],
  ["चमगादड़ और उल्लू, दोनों अँधेरे में शिकार ढूँढ़ने के लिए प्रतिध्वनि-निर्धारण का उपयोग करते हैं।",
   "प्रतिध्वनि-निर्धारण का उपयोग केवल निशाचर जीव करते हैं।"],
  T2, 3,
  "Neither statement is correct. Most bats echolocate, but owls hunt by extremely acute hearing (their offset ear openings locate the rustle of prey) and vision in low light, not by emitting sounds; among birds, only a few cave-dwelling species such as swiftlets and oilbirds echolocate. "
  "Dolphins and other toothed whales echolocate by day and by night, so the ability is not limited to nocturnal animals.",
  "कोई भी कथन सही नहीं है। अधिकांश चमगादड़ प्रतिध्वनि-निर्धारण करते हैं, पर उल्लू ध्वनि छोड़कर नहीं, बल्कि बहुत तेज़ सुनने की क्षमता (उनके कानों के छेद आगे-पीछे होने से शिकार की सरसराहट की दिशा पता चलती है) और कम रोशनी में देखने की क्षमता से शिकार करते हैं; पक्षियों में केवल स्विफ़्टलेट और ऑयलबर्ड जैसी गुफाओं में रहने वाली कुछ प्रजातियाँ प्रतिध्वनि-निर्धारण करती हैं। "
  "डॉल्फ़िन और दूसरी दाँत वाली व्हेलें दिन और रात, दोनों में प्रतिध्वनि-निर्धारण करती हैं, इसलिए यह क्षमता केवल निशाचर जीवों तक सीमित नहीं है।",
  f"{BIO12} -- Organisms and Populations (adaptations); Zoological Survey of India -- bats of India.",
  "env-echolocation")

S("25d6eaa7-9aab-4c78-a00a-af4f539bab85", "Ecosystems & Ecological Processes", "easy",
  "Consider the following statements about nutrient cycles:",
  "पोषक चक्रों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The atmosphere is the main reservoir of phosphorus.",
   "Denitrifying bacteria convert atmospheric nitrogen into ammonia."],
  ["फ़ॉस्फ़ोरस का मुख्य भंडार वायुमंडल है।",
   "विनाइट्रीकारी (denitrifying) जीवाणु वायुमंडलीय नाइट्रोजन को अमोनिया में बदलते हैं।"],
  T2, 3,
  "Neither statement is correct. Phosphorus has a sedimentary cycle: its main reservoir is phosphate rock, and there is almost no gaseous phase, unlike carbon or nitrogen. "
  "Statement 2 describes nitrogen fixation, carried out by bacteria such as Rhizobium, Azotobacter and cyanobacteria (and, in small amounts, by lightning). Denitrifying bacteria do the reverse, converting nitrates back into free nitrogen gas.",
  "कोई भी कथन सही नहीं है। फ़ॉस्फ़ोरस का चक्र अवसादी (sedimentary) है: इसका मुख्य भंडार फ़ॉस्फ़ेट चट्टानें हैं, और कार्बन या नाइट्रोजन की तरह इसकी लगभग कोई गैसीय अवस्था नहीं होती। "
  "कथन 2 नाइट्रोजन स्थिरीकरण (nitrogen fixation) का वर्णन करता है, जो राइज़ोबियम, एज़ोटोबैक्टर और नील-हरित शैवाल (cyanobacteria) जैसे जीवाणु करते हैं (और थोड़ी मात्रा में बिजली भी)। विनाइट्रीकारी जीवाणु इसका उलटा करते हैं: वे नाइट्रेट को वापस मुक्त नाइट्रोजन गैस में बदलते हैं।",
  f"{BIO12} -- Ecosystem (nutrient cycling); NCERT Class XI, Biology -- Mineral Nutrition (nitrogen cycle).",
  "env-phosphorus-nitrogen-cycles")

# ---------------------------------------------------------------- one-liners replaced --
M("801a5f1d-d008-477a-ae35-76894dca6848", "Climate Science & Mitigation", "medium",
  "'Blue carbon' refers to the carbon captured and stored by:",
  "'ब्लू कार्बन' से किसके द्वारा ग्रहण और संचित किए गए कार्बन का बोध होता है?",
  ["mangroves, seagrass meadows and tidal salt marshes", "phytoplankton drifting far out in the open ocean",
   "the ice sheets of Greenland and Antarctica", "high-altitude freshwater lakes and their sediments"],
  ["मैंग्रोव, समुद्री घास के मैदान और ज्वारीय लवण दलदल", "खुले समुद्र में दूर तक तैरते पादपप्लवक (phytoplankton)",
   "ग्रीनलैंड और अंटार्कटिका की हिम-चादरें", "अधिक ऊँचाई वाली मीठे पानी की झीलें और उनके अवसाद"],
  0,
  "'Blue carbon' is the carbon stored by coastal vegetated ecosystems -- mangroves, seagrass meadows and tidal salt marshes -- most of it in their waterlogged soils, where it can stay locked away for centuries. "
  "Open-ocean phytoplankton do take up carbon, but the IPCC's blue carbon category is limited to coastal ecosystems that people can manage and protect. "
  "India's MISHTI programme (2023) for mangrove planting on the coasts is one blue carbon measure.",
  "'ब्लू कार्बन' तटीय वनस्पति पारितंत्रों, यानी मैंग्रोव, समुद्री घास के मैदानों और ज्वारीय लवण दलदलों, द्वारा संचित कार्बन है; इसका अधिकांश भाग उनकी जलभराव वाली मिट्टी में रहता है, जहाँ यह सदियों तक बंद रह सकता है। "
  "खुले समुद्र के पादपप्लवक भी कार्बन ग्रहण करते हैं, पर IPCC की ब्लू कार्बन श्रेणी उन तटीय पारितंत्रों तक सीमित है जिनका प्रबंधन और संरक्षण मनुष्य कर सकता है। "
  "तटों पर मैंग्रोव लगाने का भारत का मिष्टी (MISHTI) कार्यक्रम (2023) ब्लू कार्बन का एक उपाय है।",
  "IPCC Special Report on the Ocean and Cryosphere in a Changing Climate (2019), chapter 5; Ministry of Environment, Forest and Climate Change -- MISHTI (2023).",
  "env-blue-carbon")

M("66ece49f-90ae-44b5-b563-4ae133bde4c2", "Flora, Fungi & Forests", "medium",
  "In which one of the following groups are all three plants gymnosperms?",
  "निम्नलिखित में से किस समूह में तीनों पौधे अनावृतबीजी (gymnosperms) हैं?",
  ["Pine, Cycas and Ginkgo", "Pine, fern and Ginkgo", "Cycas, neem and pine", "Deodar, moss and Cycas"],
  ["चीड़ (पाइन), साइकस और जिन्को", "चीड़, फ़र्न और जिन्को", "साइकस, नीम और चीड़", "देवदार, मॉस और साइकस"],
  0,
  "Gymnosperms bear naked seeds that are not enclosed in a fruit: conifers such as pine and deodar, Cycas and Ginkgo all belong here. "
  "Ferns are pteridophytes and mosses are bryophytes -- neither produces seeds at all -- while neem is a flowering plant (angiosperm). Each distractor slips in one plant from a different group.",
  "अनावृतबीजी पौधों के बीज फल में बंद नहीं होते: चीड़ और देवदार जैसे शंकुधारी, साइकस और जिन्को, सभी इसी वर्ग में आते हैं। "
  "फ़र्न टेरिडोफ़ाइट और मॉस ब्रायोफ़ाइट हैं, जो बीज बनाते ही नहीं, जबकि नीम एक फूलदार पौधा (आवृतबीजी) है। हर गलत विकल्प में किसी दूसरे वर्ग का एक पौधा जोड़ दिया गया है।",
  "NCERT Class XI, Biology -- Plant Kingdom (gymnosperms, pteridophytes, bryophytes).",
  "env-gymnosperm-groups")

# ---------------------------------------------------------------- length cues ---------
O("3455fdee-f876-4d56-a20e-86a8d7341c7b",
  ["predators keep the population of their prey below the carrying capacity of its habitat",
   "two species competing for the same limiting resources cannot coexist indefinitely",
   "only about ten per cent of the energy at one trophic level passes to the next level",
   "a species with a broad niche always outcompetes a species with a narrow niche"],
  ["शिकारी अपने शिकार की आबादी को उसके आवास की धारण क्षमता से नीचे रखते हैं",
   "एक ही सीमित संसाधन के लिए प्रतिस्पर्धा करने वाली दो प्रजातियाँ अनिश्चित काल तक साथ नहीं रह सकतीं",
   "एक पोषी स्तर की केवल लगभग दस प्रतिशत ऊर्जा अगले स्तर तक पहुँचती है",
   "व्यापक निकेत (niche) वाली प्रजाति हमेशा संकीर्ण निकेत वाली प्रजाति को पीछे छोड़ देती है"], 1)
O("a4daa638-19d0-40c9-a038-371e37cdfec6",
  ["a country's annual public spending on climate adaptation and mitigation",
   "the carbon dioxide that can still be emitted for warming to stay within a limit",
   "the amount of carbon stored in a country's forests, soils and grasslands",
   "the market price of one tonne of carbon dioxide under an emissions trading scheme"],
  ["किसी देश का जलवायु अनुकूलन और शमन पर वार्षिक सार्वजनिक खर्च",
   "कार्बन डाइऑक्साइड की वह मात्रा जो तापन को एक सीमा में रखते हुए अभी और उत्सर्जित की जा सकती है",
   "किसी देश के वनों, मिट्टी और घास के मैदानों में संचित कार्बन की मात्रा",
   "उत्सर्जन व्यापार योजना में एक टन कार्बन डाइऑक्साइड का बाज़ार मूल्य"], 1)
O("5029fc61-903b-469b-af34-9746d4dfeabf",
  ["remove carbon dioxide from the air and store it deep underground",
   "fertilise the oceans with iron so that plankton take up more carbon",
   "seed clouds with silver iodide to increase rainfall over farmland",
   "reflect a small fraction of incoming sunlight back to space"],
  ["हवा से कार्बन डाइऑक्साइड हटाकर उसे ज़मीन के बहुत नीचे संचित करना",
   "समुद्रों में लोहा डालना ताकि प्लवक (plankton) अधिक कार्बन ग्रहण करें",
   "खेतों पर वर्षा बढ़ाने के लिए बादलों में सिल्वर आयोडाइड डालना",
   "आने वाले सूर्य-प्रकाश के एक छोटे हिस्से को वापस अंतरिक्ष में परावर्तित करना"], 3)
O("01c1b03b-f1d5-4d02-b5f8-068eedcb8b50",
  ["The ozone hole over the Arctic lets more ultraviolet radiation reach the surface",
   "The Arctic Ocean absorbs more carbon dioxide than the tropical oceans do",
   "Heat released by volcanic activity under the Arctic seabed warms the water",
   "Melting snow and sea ice expose darker surfaces that absorb more sunlight"],
  ["आर्कटिक के ऊपर ओज़ोन छिद्र से अधिक पराबैंगनी विकिरण सतह तक पहुँचता है",
   "आर्कटिक महासागर उष्णकटिबंधीय महासागरों से अधिक कार्बन डाइऑक्साइड सोखता है",
   "आर्कटिक समुद्र-तल के नीचे ज्वालामुखीय गतिविधि से निकली गर्मी पानी को गर्म करती है",
   "पिघलती बर्फ़ और समुद्री हिम गहरे रंग की सतहों को खोल देते हैं, जो अधिक सूर्य-प्रकाश सोखती हैं"], 3)
O("29c1f42a-a126-4516-961d-a2b6b9dce538",
  ["Chiru (Tibetan antelope)", "Bharal (blue sheep)", "Markhor (screw-horned goat)", "Himalayan tahr"],
  ["चिरू (तिब्बती मृग)", "भरल (नीली भेड़)", "मारख़ोर (पेचदार सींग वाली बकरी)", "हिमालयी तहर"], 0)
O("7cfc9d0e-4a34-4673-ae45-8a687db8126e",
  ["Carbon monoxide from vehicles", "Sulphur dioxide from smelters", "Soot from burning biomass", "Peroxyacetyl nitrate (PAN)"],
  ["वाहनों से निकली कार्बन मोनोऑक्साइड", "धातु-गलाने की भट्ठियों से निकली सल्फ़र डाइऑक्साइड", "जैव ईंधन जलने से निकली कालिख", "पेरॉक्सीएसिटिल नाइट्रेट (PAN)"], 3)
O("4649a5a5-3d76-48be-bfda-0e6441461d3b",
  ["voting on all remaining demands for grants on the last allotted day, discussed or not",
   "the Speaker's power to close the debate on a Bill and put it to the vote at once",
   "the suspension of a member from the House for the remainder of the session",
   "a motion to cut the amount of a demand for grants by a token sum of one hundred rupees"],
  ["अंतिम निर्धारित दिन सभी बची हुई अनुदान माँगों को, चर्चा हुई हो या नहीं, मतदान के लिए रखना",
   "किसी बिल पर बहस बंद कर उसे तुरंत मतदान के लिए रखने की अध्यक्ष की शक्ति",
   "किसी सदस्य को सत्र की बची हुई अवधि के लिए सदन से निलंबित करना",
   "किसी अनुदान माँग की राशि में सौ रुपये की सांकेतिक कटौती का प्रस्ताव"], 0)
O("946bb8a0-1499-4592-a13d-8f1b07de751a",
  ["The Speaker or Chairman of the House concerned", "The Supreme Court, on an election petition",
   "The President, on the Election Commission's opinion", "The Election Commission, subject to review by courts"],
  ["संबंधित सदन का अध्यक्ष या सभापति", "उच्चतम न्यायालय, चुनाव याचिका पर",
   "राष्ट्रपति, निर्वाचन आयोग की राय के अनुसार", "निर्वाचन आयोग, न्यायालयों की समीक्षा के अधीन"], 2)
O("46f7e342-7b01-418d-92f8-0bb15a962f71",
  ["Stamp duties on bills of exchange and cheques", "Taxes on the income of companies (corporation tax)",
   "Duties of customs, including export duties", "Taxes on agricultural income and on land"],
  ["विनिमय-पत्रों और चेकों पर स्टांप शुल्क", "कंपनियों की आय पर कर (निगम कर)",
   "सीमा शुल्क, निर्यात शुल्क सहित", "कृषि आय और भूमि पर कर"], 0)
O("ec96412e-d646-4c45-810b-8ade62d1f0e6",
  ["Appointing the Advocate General of the State", "Nominating members to the State Legislative Council",
   "Summoning and proroguing the State Legislature", "Appointing the judges of the State's High Court"],
  ["राज्य के महाधिवक्ता की नियुक्ति", "राज्य विधान परिषद में सदस्यों का मनोनयन",
   "राज्य विधानमंडल का सत्र बुलाना और सत्रावसान करना", "राज्य के उच्च न्यायालय के न्यायाधीशों की नियुक्ति"], 3)
O("f70e6048-ed4d-470f-ba52-839437106c17",
  ["A tax levied on non-Muslim subjects in return for their protection", "Land revenue of an area assigned to an officer in lieu of pay",
   "A grant of permanent, hereditary land ownership to peasants", "A military rank that fixed the number of cavalry to be kept"],
  ["सुरक्षा के बदले गैर-मुसलमान प्रजा पर लगाया गया कर", "वेतन के बदले किसी अधिकारी को दिया गया भू-राजस्व का अधिकार",
   "किसानों को स्थायी, वंशानुगत भू-स्वामित्व का अनुदान", "एक सैनिक पद जो रखे जाने वाले घुड़सवारों की संख्या तय करता था"], 1)
O("4c2aaef5-57df-4dcd-bd92-909265371adf",
  ["adopting Purna Swaraj as the stated goal of the Congress", "its resolutions on Fundamental Rights and the economy",
   "launching the Non-Cooperation programme of 1920", "the reunion of the Moderates and the Extremists"],
  ["पूर्ण स्वराज को कांग्रेस का लक्ष्य बनाने के लिए", "मौलिक अधिकारों और अर्थव्यवस्था पर अपने प्रस्तावों के लिए",
   "1920 के असहयोग कार्यक्रम की शुरुआत के लिए", "नरमपंथियों और गरमपंथियों के पुनर्मिलन के लिए"], 1)
O("bee4858e-ed68-4e37-8b8a-cc4964c1d7d9",
  ["Mughal and Rajput forms blended with Gothic and classical design", "Persian Timurid forms combined with Central Asian Seljuk design",
   "Portuguese Baroque forms combined with Konkan temple design", "Dravida temple forms combined with Art Deco and modernist design"],
  ["मुगल और राजपूत रूपों के साथ गोथिक और नव-शास्त्रीय रूपरेखा का मेल", "फ़ारसी तैमूरी रूपों के साथ मध्य एशियाई सेल्जुक रूपरेखा का मेल",
   "पुर्तगाली बरोक रूपों के साथ कोंकण मंदिर रूपरेखा का मेल", "द्रविड़ मंदिर रूपों के साथ आर्ट डेको और आधुनिकतावादी रूपरेखा का मेल"], 0)
O("ee38ee90-2f3a-41f8-97c1-601e572d781e",
  ["Episodes from the Ramayana and the Mahabharata", "Jataka tales and the life of the Buddha",
   "Scenes of court life and royal hunts", "Puranic legends of Shiva and Vishnu"],
  ["रामायण और महाभारत के प्रसंग", "जातक कथाएँ और बुद्ध का जीवन", "दरबारी जीवन और शाही शिकार के दृश्य", "शिव और विष्णु की पौराणिक कथाएँ"], 1)
O("4415dc51-5698-44cd-8e86-652d80d3395e",
  ["Equatorial (rainforest)", "Mediterranean", "Tropical savanna", "Sub-arctic (taiga)"],
  ["भूमध्यरेखीय (वर्षा-वन)", "भूमध्यसागरीय", "उष्णकटिबंधीय सवाना", "उप-आर्कटिक (टैगा)"], 3)

# ---------------------------------------------------------------- Polity -----------------
A("f798f333-4df8-4042-ac7c-289bee43317c", "Governance", "medium",
  "The Viksit Bharat-Guarantee for Rozgar and Ajeevika Mission (Gramin) Act, 2025, which replaced the MGNREGA, guarantees 125 days of wage employment in a financial year to every rural household whose adult members volunteer to do unskilled manual work.",
  "मनरेगा (MGNREGA) का स्थान लेने वाला विकसित भारत-रोज़गार और आजीविका गारंटी मिशन (ग्रामीण) अधिनियम, 2025 हर उस ग्रामीण परिवार को एक वित्तीय वर्ष में 125 दिन के मज़दूरी रोज़गार की गारंटी देता है जिसके वयस्क सदस्य अकुशल शारीरिक श्रम करने के इच्छुक हों।",
  "Under the Act, the Central Government continues to bear the entire cost of wages for unskilled work, as it did under the MGNREGA.",
  "इस अधिनियम के तहत, अकुशल कार्य की मज़दूरी का पूरा खर्च केंद्र सरकार ही उठाती रहती है, जैसा मनरेगा के तहत होता था।",
  2,
  "Statement-I is correct: the VB-G RAM G Act, 2025 (Presidential assent in December 2025) repealed the MGNREGA and raised the guarantee from 100 to 125 days. "
  "Statement-II is incorrect, and this is the Act's main change in fiscal federalism: the scheme becomes a centrally sponsored scheme, with wages, material and administrative costs shared 60:40 between the Centre and most States (90:10 for the North-eastern and Himalayan States). "
  "The Centre also fixes a normative allocation for each State every year, and a State bears any spending beyond it; States continue to pay the unemployment allowance if work is not given within 15 days, and must notify a pause of up to 60 days in peak sowing and harvesting seasons.",
  "कथन-I सही है: विकसित भारत-जी राम जी अधिनियम, 2025 (दिसंबर 2025 में राष्ट्रपति की स्वीकृति) ने मनरेगा को निरस्त किया और गारंटी 100 दिन से बढ़ाकर 125 दिन कर दी। "
  "कथन-II गलत है, और राजकोषीय संघवाद की दृष्टि से यही इस अधिनियम का मुख्य बदलाव है: योजना अब केंद्र प्रायोजित योजना है, जिसमें मज़दूरी, सामग्री और प्रशासनिक खर्च केंद्र और अधिकांश राज्यों के बीच 60:40 के अनुपात में बँटते हैं (पूर्वोत्तर और हिमालयी राज्यों के लिए 90:10)। "
  "केंद्र हर वर्ष प्रत्येक राज्य के लिए एक मानक आवंटन (normative allocation) भी तय करता है, और उससे अधिक खर्च राज्य उठाता है; 15 दिन में काम न मिलने पर बेरोज़गारी भत्ता राज्य ही देते रहेंगे, और उन्हें बुवाई तथा कटाई के व्यस्त मौसम में 60 दिन तक काम रोकने की अवधि अधिसूचित करनी होगी।",
  "Viksit Bharat-Guarantee for Rozgar and Ajeevika Mission (Gramin) Act, 2025; PRS Legislative Research, Bill Summary (16 December 2025); PIB release on Presidential assent to the VB-G RAM G Bill, 2025.",
  "governance-vb-g-ram-g-act-2025")

S("790bd52c-8a00-46b1-9c4d-47eb5bb9a689", "Union & State Executive", "medium",
  "Consider the following statements regarding the President's veto power over Bills passed by Parliament:",
  "संसद द्वारा पारित विधेयकों पर राष्ट्रपति की वीटो शक्ति के संबंध में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The President can exercise an absolute veto over a private member's Bill.",
   "The President can exercise a suspensive veto by returning a Money Bill to the Lok Sabha for reconsideration.",
   "The Constitution does not prescribe a time limit within which the President must act on a Bill presented for assent.",
   "The President has no veto power over a Constitution Amendment Bill."],
  ["राष्ट्रपति किसी गैर-सरकारी सदस्य के विधेयक (private member's Bill) पर आत्यंतिक वीटो (absolute veto) का प्रयोग कर सकता है।",
   "राष्ट्रपति किसी धन विधेयक को पुनर्विचार के लिए लोकसभा को लौटाकर निलंबनकारी वीटो (suspensive veto) का प्रयोग कर सकता है।",
   "संविधान यह समय-सीमा निर्धारित नहीं करता कि स्वीकृति के लिए प्रस्तुत विधेयक पर राष्ट्रपति को कितने समय में निर्णय लेना है।",
   "संविधान संशोधन विधेयक पर राष्ट्रपति के पास कोई वीटो शक्ति नहीं है।"],
  C4, 2,
  "Statements 1, 3 and 4 are correct. The absolute veto is typically used on private members' Bills or when a ministry falls before assent. "
  "Article 111 sets no time limit for the President's decision; in its opinion of November 2025 on the Presidential Reference under Article 143, the Supreme Court held that courts cannot impose timelines on the President or Governors, though prolonged inaction is open to limited review. "
  "Since the 24th Amendment (1971) the President must assent to a Constitution Amendment Bill. "
  "Statement 2 is incorrect: a Money Bill, introduced only with the President's prior recommendation, cannot be returned for reconsideration; the President may only give or withhold assent.",
  "कथन 1, 3 और 4 सही हैं। आत्यंतिक वीटो का प्रयोग प्रायः गैर-सरकारी सदस्यों के विधेयकों पर, या स्वीकृति से पहले मंत्रिपरिषद के गिर जाने पर, होता है। "
  "अनुच्छेद 111 राष्ट्रपति के निर्णय के लिए कोई समय-सीमा तय नहीं करता; अनुच्छेद 143 के तहत राष्ट्रपतीय संदर्भ पर नवंबर 2025 की अपनी राय में उच्चतम न्यायालय ने माना कि न्यायालय राष्ट्रपति या राज्यपालों पर समय-सीमा नहीं थोप सकते, यद्यपि लंबे समय तक निष्क्रियता की सीमित समीक्षा हो सकती है। "
  "24वें संशोधन (1971) के बाद से राष्ट्रपति के लिए संविधान संशोधन विधेयक पर स्वीकृति देना अनिवार्य है। "
  "कथन 2 गलत है: धन विधेयक, जो राष्ट्रपति की पूर्व सिफ़ारिश से ही पेश होता है, पुनर्विचार के लिए लौटाया नहीं जा सकता; राष्ट्रपति केवल स्वीकृति दे सकता है या रोक सकता है।",
  "Constitution of India, Articles 111, 117 and 368(2); Supreme Court, In Re: Assent, Withholding or Reservation of Bills by the Governor and the President (Special Reference No. 1 of 2025), opinion of November 2025; M. Laxmikanth, Indian Polity -- the President.",
  "executive-presidential-veto-types")

if __name__ == "__main__":
    write("env_polity_audit_fixes.sql")
