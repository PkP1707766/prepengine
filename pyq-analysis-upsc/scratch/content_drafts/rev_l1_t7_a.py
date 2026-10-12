# -*- coding: utf-8 -*-
"""Level 1 · Test 7 (GS Foundation Revision, NCERT Foundation) -- part A: Polity (18) (upsc_l1_cell_targets.mjs 7).
Test 7 spans all six static subjects (Polity 18, History 19, Environment 18, Geography 12, Economy 20, S&T 13).
Polity cells: Federalism e-MCQ, m-stmt; Governance e-stmt, m-stmt; Constitutional Framework e-stmt, m-MCQ, m-stmt;
Parliament e-stmt, m-MCQ, m-stmt; Statutory-Laws e-SI, m-stmt; Executive m-stmt; Bodies m-stmt; Rights m-stmt, h-SI;
Judicial-Verdicts h-pairs; Panchayati Raj h-pairs.
Level 2 holds 418 Polity rows and Level-1 Test 1 another 100, so this part draws on what neither used: NCERT Politics
in India since Independence (Manipur's 1948 election, the first general election, 'Aaya Ram Gaya Ram', the JP
movement and the Shah Commission, popular movements, the Mizo accord), NCERT Social and Political Life (the patwari,
village functionaries, accommodation of religion), and provisions and laws not yet asked (Articles 252, 78 and
25(2)(b), the kirpan, the Good Samaritan protection, the Whistle Blowers Act, the Press Council, Vineet Narain,
Bandhua Mukti Morcha, Shafin Jahan, T.M.A. Pai). MCQ keys are pinned (pos)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Polity"
d.REQUIRE_CRAFT = True
POL12 = "NCERT Class XII, Political Science -- Politics in India since Independence"
POL11 = "NCERT Class XI, Political Science -- Indian Constitution at Work"
SPL6 = "NCERT Class VI, Social and Political Life I"
SPL8 = "NCERT Class VIII, Social and Political Life III"
COI = "Constitution of India"

# ---------------------------------------------------------------- Federalism & Special Provisions (e-MCQ, m-stmt)
M("Federalism & Special Provisions", "easy",
  "The legislatures of two States pass resolutions asking Parliament to make a law on a subject in the State List for them. Under which Article can Parliament then legislate for those States?",
  "दो राज्यों के विधानमंडल संकल्प पारित करके संसद से उनके लिए राज्य सूची के किसी विषय पर क़ानून बनाने को कहते हैं। संसद तब किस अनुच्छेद के अंतर्गत उन राज्यों के लिए क़ानून बना सकती है?",
  ["Article 252", "Article 249", "Article 253", "Article 356"],
  ["अनुच्छेद 252", "अनुच्छेद 249", "अनुच्छेद 253", "अनुच्छेद 356"],
  0,
  "Article 252 lets Parliament legislate on a State subject for two or more States that consent by resolutions of their legislatures; any other State may adopt the law later by its own resolution, but only Parliament can then amend or repeal it. "
  "Laws such as the Wild Life (Protection) Act, 1972 and the Water (Prevention and Control of Pollution) Act, 1974 were made this way. Article 249 works through a Rajya Sabha resolution in the national interest, and Article 253 to implement international agreements.",
  "अनुच्छेद 252 संसद को उन दो या अधिक राज्यों के लिए राज्य विषय पर क़ानून बनाने देता है जो अपने विधानमंडलों के संकल्पों द्वारा सहमति दें; कोई अन्य राज्य बाद में अपने संकल्प से उस क़ानून को अपना सकता है, पर फिर उसका संशोधन या निरसन केवल संसद कर सकती है। "
  "वन्यजीव (संरक्षण) अधिनियम, 1972 और जल (प्रदूषण निवारण एवं नियंत्रण) अधिनियम, 1974 जैसे क़ानून इसी तरह बने। अनुच्छेद 249 राष्ट्रीय हित में राज्यसभा के संकल्प से, और अनुच्छेद 253 अंतरराष्ट्रीय समझौतों को लागू करने के लिए काम करता है।",
  f"{COI} (Article 252); {POL11} (Federalism).",
  "l1-rev-art252-consent-of-states", pos=0, craft="application")

S("Federalism & Special Provisions", "medium", "Consider the following statements about Mizoram:",
  "मिज़ोरम के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Mizo National Front, led by Laldenga, began an armed struggle for independence in 1966.",
   "A peace accord between Laldenga and Prime Minister Rajiv Gandhi was signed in 1986.",
   "Mizoram became a full State in 1987.",
   "Laldenga became the Chief Minister of Mizoram after the accord."],
  ["लालडेंगा के नेतृत्व में मिज़ो नेशनल फ़्रंट ने 1966 में स्वतंत्रता के लिए सशस्त्र संघर्ष आरंभ किया।",
   "1986 में लालडेंगा और प्रधानमंत्री राजीव गांधी के बीच एक शांति समझौता हुआ।",
   "मिज़ोरम 1987 में पूर्ण राज्य बना।",
   "समझौते के बाद लालडेंगा मिज़ोरम के मुख्यमंत्री बने।"],
  C4, 3,
  "All four statements are correct. Resentment over the government's poor response to the 'mautam' famine of 1959 in the Mizo hills helped drive the movement; after two decades of insurgency, the accord granted statehood with special powers, and the MNF gave up its armed struggle. "
  "NCERT presents Mizoram as an example of how accommodating regional aspirations through negotiation can turn an insurgency into one of the more peaceful States.",
  "चारों कथन सही हैं। 1959 में मिज़ो पहाड़ियों के 'मौतम' अकाल पर सरकार की ढीली प्रतिक्रिया से उपजी नाराज़गी ने आंदोलन को बल दिया; दो दशकों के विद्रोह के बाद समझौते ने विशेष शक्तियों के साथ राज्य का दर्जा दिया, और MNF ने सशस्त्र संघर्ष छोड़ दिया। "
  "NCERT मिज़ोरम को इस उदाहरण के रूप में प्रस्तुत करता है कि बातचीत द्वारा क्षेत्रीय आकांक्षाओं को समायोजित करके कैसे एक विद्रोह को अधिक शांत राज्यों में बदला जा सकता है।",
  f"{POL12} (Regional Aspirations).",
  "l1-rev-mizo-accord-1986", craft="recall")

# ---------------------------------------------------------------- Governance (e-stmt, m-stmt)
S("Governance", "easy", "Consider the following statements about land administration in a district:",
  "किसी ज़िले के भूमि प्रशासन के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The patwari measures land and keeps the land records of a group of villages.",
   "The tehsildar supervises the work of the patwaris and hears land disputes."],
  ["पटवारी भूमि मापता है और गाँवों के एक समूह के भू-अभिलेख रखता है।",
   "तहसीलदार पटवारियों के काम की देखरेख करता है और भूमि विवाद सुनता है।"],
  T2, 2,
  "Both statements are correct. The patwari -- known in different States as lekhpal, karamchari, village officer and by other names -- also collects land revenue and keeps a record of the crops grown, and farmers need an extract of the land records to prove ownership, get loans or settle disputes. "
  "The tehsildar's office also issues certificates such as caste and income certificates, which is why it is one of the busiest public offices for rural people.",
  "दोनों कथन सही हैं। पटवारी -- जिसे अलग-अलग राज्यों में लेखपाल, कर्मचारी, ग्राम अधिकारी आदि नामों से जाना जाता है -- भू-राजस्व भी वसूलता है और उगाई गई फ़सलों का अभिलेख रखता है, और किसानों को स्वामित्व सिद्ध करने, ऋण पाने या विवाद सुलझाने के लिए भू-अभिलेख की प्रति चाहिए होती है। "
  "तहसीलदार का कार्यालय जाति और आय प्रमाणपत्र जैसे प्रमाणपत्र भी जारी करता है, इसीलिए यह ग्रामीण लोगों के लिए सबसे व्यस्त सार्वजनिक कार्यालयों में है।",
  f"{SPL6} (Rural Administration).",
  "l1-rev-patwari-tehsildar", craft="recall")

S("Governance", "medium", "Consider the following statements about popular movements in India:",
  "भारत के जन आंदोलनों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Dalit Panthers was formed in 1972 by young Dalit writers and activists in Maharashtra.",
   "The Bharatiya Kisan Union, led by Mahendra Singh Tikait, organised a large farmers' agitation at Meerut in 1988.",
   "The anti-arrack movement was led mainly by men's associations in the cities of Kerala."],
  ["दलित पैंथर्स का गठन 1972 में महाराष्ट्र में युवा दलित लेखकों और कार्यकर्ताओं ने किया।",
   "महेंद्र सिंह टिकैत के नेतृत्व में भारतीय किसान यूनियन ने 1988 में मेरठ में किसानों का बड़ा आंदोलन किया।",
   "शराब-विरोधी (anti-arrack) आंदोलन का नेतृत्व मुख्यतः केरल के नगरों के पुरुष संगठनों ने किया।"],
  C3, 1,
  "Statements 1 and 2 are correct: the Dalit Panthers fought caste atrocities and the non-implementation of reservations, and the BKU pressed for better prices for crops and lower electricity charges, drawing on caste and clan networks of farmers in western Uttar Pradesh. "
  "Statement 3 is wrong: the anti-arrack movement began in the early 1990s among rural women of Nellore district in Andhra Pradesh, who linked liquor to domestic violence and debt -- one of the movements NCERT uses to show non-party politics at the grassroots.",
  "कथन 1 और 2 सही हैं: दलित पैंथर्स ने जातिगत अत्याचारों और आरक्षण के लागू न होने के विरुद्ध संघर्ष किया, और BKU ने पश्चिमी उत्तर प्रदेश के किसानों के जाति और कुल नेटवर्क के सहारे फ़सलों के बेहतर दाम और बिजली की कम दरों की माँग उठाई। "
  "कथन 3 गलत है: शराब-विरोधी आंदोलन 1990 के दशक के आरंभ में आंध्र प्रदेश के नेल्लोर ज़िले की ग्रामीण महिलाओं में शुरू हुआ, जिन्होंने शराब को घरेलू हिंसा और कर्ज़ से जोड़ा -- यह उन आंदोलनों में है जिनसे NCERT ज़मीनी स्तर पर ग़ैर-दलीय राजनीति को दिखाता है।",
  f"{POL12} (Rise of Popular Movements).",
  "l1-rev-dalit-panthers-bku-anti-arrack", craft="precision")

# ---------------------------------------------------------------- Constitutional Framework (e-stmt, m-MCQ, m-stmt)
S("Constitutional Framework", "easy", "Consider the following statements about Manipur in the early years after Independence:",
  "स्वतंत्रता के बाद के आरंभिक वर्षों में मणिपुर के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Manipur held elections on the basis of universal adult franchise in 1948, the first part of India to do so.",
   "The Merger Agreement of 1949 was approved by Manipur's elected Legislative Assembly before it was signed."],
  ["मणिपुर ने 1948 में सार्वभौमिक वयस्क मताधिकार के आधार पर चुनाव कराए, और ऐसा करने वाला वह भारत का पहला भाग था।",
   "1949 के विलय समझौते पर हस्ताक्षर से पहले उसे मणिपुर की निर्वाचित विधानसभा ने स्वीकृति दी थी।"],
  T2, 0,
  "Only statement 1 is correct: Maharaja Bodhachandra Singh had signed the Instrument of Accession on the assurance that Manipur's internal autonomy would be kept, and under popular pressure held elections in June 1948, making the State a constitutional monarchy. "
  "Statement 2 is wrong: the Government of India pressed the Maharaja into signing the Merger Agreement in September 1949 without consulting the elected Assembly, which caused much anger in Manipur that is still felt.",
  "केवल कथन 1 सही है: महाराजा बोधचंद्र सिंह ने इस आश्वासन पर विलय-पत्र पर हस्ताक्षर किए थे कि मणिपुर की आंतरिक स्वायत्तता बनी रहेगी, और जनता के दबाव में जून 1948 में चुनाव कराकर राज्य को संवैधानिक राजतंत्र बनाया। "
  "कथन 2 गलत है: भारत सरकार ने निर्वाचित विधानसभा से परामर्श किए बिना सितंबर 1949 में महाराजा पर दबाव डालकर विलय समझौते पर हस्ताक्षर कराए, जिससे मणिपुर में बड़ा रोष हुआ जो आज भी महसूस होता है।",
  f"{POL12} (Challenges of Nation Building).",
  "l1-rev-manipur-1948-adult-franchise", craft="precision")

M("Constitutional Framework", "medium", "The call for 'Total Revolution' (Sampoorna Kranti) in 1974, which grew out of the student movement in Bihar, was given by",
  "1974 में बिहार के छात्र आंदोलन से उपजा 'संपूर्ण क्रांति' का आह्वान किसने किया?",
  ["Jayaprakash Narayan", "Ram Manohar Lohia", "Morarji Desai", "Acharya Vinoba Bhave"],
  ["जयप्रकाश नारायण", "राम मनोहर लोहिया", "मोरारजी देसाई", "आचार्य विनोबा भावे"],
  0,
  "Jayaprakash Narayan (JP), a veteran of the national movement who had withdrawn from party politics, agreed to lead the Bihar students' agitation against corruption and rising prices, and called for a 'total revolution' in the social, economic and political spheres; the movement spread nationally and culminated in a huge rally in Delhi in June 1975. "
  "Its confrontation with the government was one of the immediate settings of the Emergency declared that month.",
  "स्वतंत्रता आंदोलन के वरिष्ठ नेता जयप्रकाश नारायण (जेपी), जो दलीय राजनीति से अलग हो चुके थे, भ्रष्टाचार और बढ़ती कीमतों के विरुद्ध बिहार के छात्र आंदोलन का नेतृत्व करने को तैयार हुए और सामाजिक, आर्थिक और राजनीतिक क्षेत्रों में 'संपूर्ण क्रांति' का आह्वान किया; आंदोलन राष्ट्रव्यापी हुआ और जून 1975 में दिल्ली की विशाल रैली तक पहुँचा। "
  "सरकार से इसका टकराव उसी महीने घोषित आपातकाल की तात्कालिक पृष्ठभूमि में था।",
  f"{POL12} (The Crisis of Democratic Order).",
  "l1-rev-jp-total-revolution", pos=3, craft="recall")

S("Constitutional Framework", "medium", "Consider the following statements about the Emergency of 1975-77:",
  "1975-77 के आपातकाल के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["After it ended, the Shah Commission was appointed to inquire into excesses committed during the Emergency.",
   "Press censorship was imposed during the Emergency.",
   "The Emergency lasted for about six months."],
  ["इसके समाप्त होने के बाद आपातकाल के दौरान हुई ज़्यादतियों की जाँच के लिए शाह आयोग नियुक्त किया गया।",
   "आपातकाल के दौरान प्रेस पर सेंसरशिप लगाई गई।",
   "आपातकाल लगभग छह महीने चला।"],
  C3, 1,
  "Statements 1 and 2 are correct: the commission, headed by a retired Chief Justice, J.C. Shah, examined matters such as arrests, forced sterilisations and slum demolitions, and newspapers had to get permission before publishing. "
  "Statement 3 is wrong: the Emergency was declared in June 1975 and lifted only in March 1977, after about 21 months. NCERT draws from it the lessons that democracy needs an independent judiciary, a free press and vigilant citizens -- and later amendments made a future emergency much harder to declare.",
  "कथन 1 और 2 सही हैं: सेवानिवृत्त मुख्य न्यायाधीश जे.सी. शाह की अध्यक्षता वाले आयोग ने गिरफ़्तारियों, जबरन नसबंदी और झुग्गियों को ढहाने जैसे मामलों की जाँच की, और समाचार पत्रों को छापने से पहले अनुमति लेनी पड़ती थी। "
  "कथन 3 गलत है: आपातकाल जून 1975 में घोषित हुआ और लगभग 21 महीने बाद मार्च 1977 में ही हटाया गया। NCERT इससे ये सबक़ निकालता है कि लोकतंत्र को स्वतंत्र न्यायपालिका, स्वतंत्र प्रेस और सजग नागरिक चाहिए -- और बाद के संशोधनों ने भविष्य में आपातकाल घोषित करना बहुत कठिन बना दिया।",
  f"{POL12} (The Crisis of Democratic Order).",
  "l1-rev-emergency-shah-commission", craft="precision")

# ---------------------------------------------------------------- Parliament & State Legislature (e-stmt, m-MCQ, m-stmt)
S("Parliament & State Legislature", "easy", "Consider the following statements about the phrase 'Aaya Ram, Gaya Ram':",
  "'आया राम, गया राम' वाक्यांश के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It arose in 1967 from a member of the Haryana Legislative Assembly, Gaya Lal, who changed his party three times within a fortnight.",
   "It described a minister who changed portfolios frequently."],
  ["यह 1967 में हरियाणा विधानसभा के एक सदस्य, गया लाल, से उपजा, जिन्होंने एक पखवाड़े में तीन बार दल बदला।",
   "यह बार-बार विभाग बदलने वाले मंत्री का वर्णन करता था।"],
  T2, 0,
  "Only statement 1 is correct: the phrase came to describe legislators who defect from one party to another for office or gain, a practice that brought down several State governments after the 1967 elections. "
  "Statement 2 is wrong: it refers to changing parties, not portfolios. Such defections eventually led to the anti-defection provisions of the Tenth Schedule, under which a legislator who voluntarily gives up party membership can be disqualified.",
  "केवल कथन 1 सही है: यह वाक्यांश पद या लाभ के लिए एक दल से दूसरे दल में जाने वाले विधायकों का वर्णन करने लगा, ऐसी प्रथा जिसने 1967 के चुनावों के बाद कई राज्य सरकारें गिराईं। "
  "कथन 2 गलत है: इसका संबंध दल बदलने से है, विभाग बदलने से नहीं। ऐसे दल-बदलों से अंततः दसवीं अनुसूची के दल-बदल विरोधी प्रावधान बने, जिनके अंतर्गत स्वेच्छा से दल की सदस्यता छोड़ने वाला विधायक अयोग्य ठहराया जा सकता है।",
  f"{POL12} (Challenges to and Restoration of the Congress System).",
  "l1-rev-aaya-ram-gaya-ram-1967", craft="recall")

M("Parliament & State Legislature", "medium", "Who was the first Speaker of the Lok Sabha?",
  "लोकसभा के पहले अध्यक्ष (स्पीकर) कौन थे?",
  ["G.V. Mavalankar", "M.A. Ayyangar", "Hukam Singh", "N. Sanjiva Reddy"],
  ["जी.वी. मावलंकर", "एम.ए. अय्यंगार", "हुकम सिंह", "एन. संजीव रेड्डी"],
  0,
  "Ganesh Vasudev Mavalankar, who had been President of the Central Legislative Assembly before Independence, was elected the first Speaker of the Lok Sabha in 1952 and set many of the conventions of the office, such as the Speaker's impartiality. "
  "M. Ananthasayanam Ayyangar succeeded him in 1956, followed by Hukam Singh and Neelam Sanjiva Reddy, who later became President of India.",
  "स्वतंत्रता से पहले केंद्रीय विधानसभा के अध्यक्ष रहे गणेश वासुदेव मावलंकर 1952 में लोकसभा के पहले अध्यक्ष चुने गए और उन्होंने इस पद की कई परंपराएँ स्थापित कीं, जैसे अध्यक्ष की निष्पक्षता। "
  "1956 में एम. अनंतशयनम अय्यंगार उनके उत्तराधिकारी बने, उनके बाद हुकम सिंह और नीलम संजीव रेड्डी, जो बाद में भारत के राष्ट्रपति बने।",
  "Lok Sabha Secretariat (Speakers of the Lok Sabha).",
  "l1-rev-mavalankar-first-speaker", pos=1, craft="recall")

S("Parliament & State Legislature", "medium", "Consider the following statements about India's first general election:",
  "भारत के पहले आम चुनाव के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Sukumar Sen, the first Chief Election Commissioner, conducted it.",
   "Only about 15 per cent of the roughly 17 crore eligible voters were literate.",
   "The whole election was completed on a single day."],
  ["पहले मुख्य चुनाव आयुक्त सुकुमार सेन ने इसे संपन्न कराया।",
   "लगभग 17 करोड़ पात्र मतदाताओं में से केवल लगभग 15 प्रतिशत साक्षर थे।",
   "पूरा चुनाव एक ही दिन में संपन्न हुआ।"],
  C3, 1,
  "Statements 1 and 2 are correct: to let voters who could not read take part, each candidate was given a ballot box marked with a symbol, into which voters dropped their ballot; the method was later replaced by marked ballot papers and, much later, voting machines. "
  "Statement 3 is wrong: polling stretched from October 1951 to February 1952. Many abroad doubted that elections could work in a poor, largely illiterate country; their success was hailed as a landmark for democracy.",
  "कथन 1 और 2 सही हैं: पढ़ न सकने वाले मतदाताओं को भाग लेने देने के लिए हर उम्मीदवार को चिह्न लगी एक मतपेटी दी गई, जिसमें मतदाता अपना मतपत्र डालते थे; यह तरीक़ा बाद में चिह्नित मतपत्रों और, बहुत बाद, मतदान मशीनों से बदला गया। "
  "कथन 3 गलत है: मतदान अक्टूबर 1951 से फ़रवरी 1952 तक चला। विदेश में कई लोगों को संदेह था कि एक ग़रीब, अधिकतर निरक्षर देश में चुनाव सफल हो सकते हैं; इनकी सफलता को लोकतंत्र के लिए एक ऐतिहासिक उपलब्धि माना गया।",
  f"{POL12} (Era of One-Party Dominance).",
  "l1-rev-first-general-election-sukumar-sen", craft="precision")

# ---------------------------------------------------------------- Statutory-Laws (e-SI, m-stmt)
A("Statutory-Laws", "easy",
  "A bystander who takes a road accident victim to hospital cannot be compelled to disclose their identity, and is protected from being held liable for helping.",
  "सड़क दुर्घटना के घायल को अस्पताल ले जाने वाले राहगीर को अपनी पहचान बताने के लिए बाध्य नहीं किया जा सकता, और सहायता करने के लिए उसे उत्तरदायी ठहराए जाने से संरक्षण है।",
  "The law aims to encourage people to help accident victims quickly, during the critical 'golden hour' after an accident.",
  "क़ानून का उद्देश्य लोगों को दुर्घटना के बाद के महत्त्वपूर्ण 'स्वर्णिम घंटे' (golden hour) में घायलों की शीघ्र सहायता के लिए प्रोत्साहित करना है।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I. The 'Good Samaritan' protection, added to the Motor Vehicles Act by the 2019 amendment after Supreme Court directions, answers the fear of police questioning and court visits that long kept bystanders from helping; hospitals also may not detain a Good Samaritan or demand payment from them. "
  "Prompt treatment in the first hour after serious injury greatly improves the chances of survival.",
  "दोनों कथन सही हैं, और कथन-II कथन-I की व्याख्या करता है। सर्वोच्च न्यायालय के निर्देशों के बाद 2019 के संशोधन द्वारा मोटर वाहन अधिनियम में जोड़ा गया 'नेक मददगार' (Good Samaritan) संरक्षण पुलिस पूछताछ और अदालती चक्करों के उस भय का उत्तर है जो लंबे समय से राहगीरों को सहायता से रोकता था; अस्पताल भी नेक मददगार को रोक नहीं सकते या उससे भुगतान नहीं माँग सकते। "
  "गंभीर चोट के बाद पहले घंटे में शीघ्र उपचार जीवित बचने की संभावना बहुत बढ़ाता है।",
  "Motor Vehicles (Amendment) Act, 2019 (section 134A); Ministry of Road Transport and Highways.",
  "l1-rev-good-samaritan-protection", craft="inference")

S("Statutory-Laws", "medium", "Consider the following statements about the Whistle Blowers Protection Act, 2014:",
  "व्हिसल ब्लोअर्स संरक्षण अधिनियम, 2014 के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It provides for receiving complaints that disclose corruption or wilful misuse of power by public servants.",
   "For complaints about officials of the Central Government, the Central Vigilance Commission is the competent authority.",
   "It requires the identity of the complainant to be kept confidential and protects them against victimisation."],
  ["यह लोक सेवकों के भ्रष्टाचार या शक्ति के जान-बूझकर दुरुपयोग को उजागर करने वाली शिकायतें प्राप्त करने का प्रावधान करता है।",
   "केंद्र सरकार के अधिकारियों से संबंधित शिकायतों के लिए केंद्रीय सतर्कता आयोग सक्षम प्राधिकारी है।",
   "यह शिकायतकर्ता की पहचान गोपनीय रखने की अपेक्षा करता है और उसे उत्पीड़न से संरक्षण देता है।"],
  C3, 2,
  "All three statements are correct. The law arose from cases in which people who exposed wrongdoing in public projects were harassed or even killed, and from India's commitments under the UN Convention against Corruption. "
  "It applies to disclosures about public servants; a complaint must be made in good faith, and making a knowingly false complaint is itself punishable.",
  "तीनों कथन सही हैं। यह क़ानून उन मामलों से उपजा जिनमें सार्वजनिक परियोजनाओं में गड़बड़ी उजागर करने वालों को परेशान किया गया या उनकी हत्या तक कर दी गई, और भ्रष्टाचार के विरुद्ध संयुक्त राष्ट्र अभिसमय के अंतर्गत भारत की प्रतिबद्धताओं से भी। "
  "यह लोक सेवकों के बारे में प्रकटीकरण पर लागू होता है; शिकायत सद्भाव से की जानी चाहिए, और जान-बूझकर झूठी शिकायत करना स्वयं दंडनीय है।",
  "Whistle Blowers Protection Act, 2014; Central Vigilance Commission.",
  "l1-rev-whistle-blowers-act-2014", craft="recall")

# ---------------------------------------------------------------- Union & State Executive (m-stmt)
S("Union & State Executive", "medium", "Under Article 78 of the Constitution, it is the duty of the Prime Minister to:",
  "संविधान के अनुच्छेद 78 के अंतर्गत प्रधानमंत्री का यह कर्तव्य है कि वह:",
  ["communicate to the President all decisions of the Council of Ministers about the administration of the Union and proposals for legislation.",
   "furnish such information about the administration and proposals for legislation as the President may call for.",
   "submit for the consideration of the Council of Ministers, if the President so requires, any matter decided by a single minister but not considered by the Council."],
  ["संघ के प्रशासन और विधान के प्रस्तावों से संबंधित मंत्रिपरिषद के सभी निर्णयों की सूचना राष्ट्रपति को दे।",
   "प्रशासन और विधान के प्रस्तावों के बारे में ऐसी जानकारी दे जो राष्ट्रपति माँगे।",
   "यदि राष्ट्रपति अपेक्षा करे, तो किसी एक मंत्री द्वारा तय पर परिषद द्वारा विचार न किए गए किसी मामले को मंत्रिपरिषद के विचार के लिए रखे।"],
  C3, 2,
  "All three are duties under Article 78. The Prime Minister is the link between the President and the Council of Ministers; though the President must act on the Council's advice, these duties keep the head of state informed and give the President a way to ask for collective consideration of a matter. "
  "Article 167 places the same duties on a Chief Minister towards the Governor.",
  "तीनों अनुच्छेद 78 के अंतर्गत कर्तव्य हैं। प्रधानमंत्री राष्ट्रपति और मंत्रिपरिषद के बीच की कड़ी है; यद्यपि राष्ट्रपति को परिषद की सलाह पर कार्य करना होता है, ये कर्तव्य राष्ट्राध्यक्ष को सूचित रखते और उसे किसी मामले पर सामूहिक विचार माँगने का रास्ता देते हैं। "
  "अनुच्छेद 167 मुख्यमंत्री पर राज्यपाल के प्रति यही कर्तव्य डालता है।",
  f"{COI} (Articles 78 and 167); {POL11} (Executive).",
  "l1-rev-art78-pm-duties", craft="recall")

# ---------------------------------------------------------------- Constitutional & Statutory Bodies (m-stmt)
S("Constitutional & Statutory Bodies", "medium", "Consider the following statements about the Press Council of India:",
  "भारतीय प्रेस परिषद के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is a statutory body, now functioning under the Press Council Act, 1978.",
   "By convention, its chairperson is a retired judge of the Supreme Court.",
   "It can impose fines on newspapers and cancel their registration."],
  ["यह एक सांविधिक निकाय है, जो अब प्रेस परिषद अधिनियम, 1978 के अंतर्गत कार्य करती है।",
   "परंपरा से इसका अध्यक्ष सर्वोच्च न्यायालय का सेवानिवृत्त न्यायाधीश होता है।",
   "यह समाचार पत्रों पर जुर्माना लगा सकती है और उनका पंजीकरण रद्द कर सकती है।"],
  C3, 1,
  "Statements 1 and 2 are correct: the Council aims to preserve the freedom of the press and to maintain and improve the standards of newspapers and news agencies, and most of its members are drawn from the press itself. "
  "Statement 3 is wrong: after an inquiry it can only warn, admonish or censure a newspaper, editor or journalist, or disapprove of their conduct -- its strength is moral, not penal.",
  "कथन 1 और 2 सही हैं: परिषद का उद्देश्य प्रेस की स्वतंत्रता की रक्षा और समाचार पत्रों तथा समाचार एजेंसियों के स्तर को बनाए रखना और सुधारना है, और इसके अधिकांश सदस्य स्वयं प्रेस से आते हैं। "
  "कथन 3 गलत है: जाँच के बाद यह किसी समाचार पत्र, संपादक या पत्रकार को केवल चेतावनी दे सकती, भर्त्सना या निंदा कर सकती, या उनके आचरण को अनुचित ठहरा सकती है -- इसकी शक्ति नैतिक है, दंडात्मक नहीं।",
  "Press Council Act, 1978; Press Council of India.",
  "l1-rev-press-council-powers", craft="precision")

# ---------------------------------------------------------------- Fundamental Rights, DPSP & Duties (m-stmt, h-SI)
S("Fundamental Rights, DPSP & Duties", "medium", "Consider the following statements about how the law accommodates religious practice:",
  "क़ानून धार्मिक आचरण को कैसे समायोजित करता है, इस बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Constitution deems the wearing and carrying of kirpans to be included in the profession of the Sikh religion.",
   "Sikh men who wear turbans are exempt from compulsory helmet rules for two-wheeler riders.",
   "Article 25 bars the State from regulating any economic or political activity connected with religious practice."],
  ["संविधान कृपाण धारण करने और ले जाने को सिख धर्म को मानने का भाग मानता है।",
   "पगड़ी पहनने वाले सिख पुरुषों को दोपहिया चालकों के लिए अनिवार्य हेलमेट नियमों से छूट है।",
   "अनुच्छेद 25 राज्य को धार्मिक आचरण से जुड़ी किसी भी आर्थिक या राजनीतिक गतिविधि को विनियमित करने से रोकता है।"],
  C3, 1,
  "Statements 1 and 2 are correct: Explanation I to Article 25 covers the kirpan, and the exemption from helmets reflects the respect NCERT describes Indian secularism as showing for the turban as central to Sikh practice. "
  "Statement 3 is wrong: Article 25(2) expressly allows the State to regulate or restrict economic, financial, political or other secular activities associated with religious practice, and to provide for social welfare and reform.",
  "कथन 1 और 2 सही हैं: अनुच्छेद 25 का स्पष्टीकरण I कृपाण को शामिल करता है, और हेलमेट से छूट उस सम्मान को दर्शाती है जो NCERT के अनुसार भारतीय पंथनिरपेक्षता पगड़ी को सिख आचरण का केंद्रीय अंग मानते हुए दिखाती है। "
  "कथन 3 गलत है: अनुच्छेद 25(2) राज्य को धार्मिक आचरण से जुड़ी आर्थिक, वित्तीय, राजनीतिक या अन्य लौकिक गतिविधियों को विनियमित या प्रतिबंधित करने, और सामाजिक कल्याण तथा सुधार का प्रावधान करने की स्पष्ट अनुमति देता है।",
  f"{COI} (Article 25); {SPL8} (Understanding Secularism).",
  "l1-rev-kirpan-helmet-art25-2", craft="precision")

A("Fundamental Rights, DPSP & Duties", "hard",
  "A Hindu temple of a public character cannot lawfully keep out worshippers on the ground of their caste.",
  "सार्वजनिक प्रकृति का कोई हिंदू मंदिर जाति के आधार पर श्रद्धालुओं को वैधानिक रूप से बाहर नहीं रख सकता।",
  "Article 25(2)(b) allows the State to make laws throwing open Hindu religious institutions of a public character to all classes and sections of Hindus.",
  "अनुच्छेद 25(2)(ख) राज्य को सार्वजनिक प्रकृति की हिंदू धार्मिक संस्थाओं को हिंदुओं के सभी वर्गों और अनुभागों के लिए खोलने वाले क़ानून बनाने की अनुमति देता है।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I. The temple-entry clause, together with the abolition of untouchability in Article 17, overrides any custom that excludes castes from public temples; for this purpose 'Hindus' includes Sikhs, Jains and Buddhists. "
  "It reflects the reformist side of Indian secularism, which allows the State to intervene in religion to end discrimination, unlike a strict separation of State and religion.",
  "दोनों कथन सही हैं, और कथन-II कथन-I की व्याख्या करता है। मंदिर-प्रवेश का यह खंड, अनुच्छेद 17 द्वारा अस्पृश्यता के उन्मूलन के साथ, किसी भी ऐसी प्रथा पर प्रभावी है जो जातियों को सार्वजनिक मंदिरों से बाहर रखती हो; इस प्रयोजन के लिए 'हिंदुओं' में सिख, जैन और बौद्ध भी आते हैं। "
  "यह भारतीय पंथनिरपेक्षता के सुधारवादी पक्ष को दर्शाता है, जो राज्य और धर्म के कठोर अलगाव के विपरीत, भेदभाव समाप्त करने के लिए राज्य को धर्म में हस्तक्षेप करने देता है।",
  f"{COI} (Articles 17 and 25(2)(b)).",
  "l1-rev-temple-entry-art25-2b", craft="inference")

# ---------------------------------------------------------------- Judicial-Verdicts (h-pairs)
P("Judicial-Verdicts", "hard", "Consider the following pairs of Supreme Court judgments and what they are known for:",
  "सर्वोच्च न्यायालय के निर्णयों और जिनके लिए वे जाने जाते हैं, उनके निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Vineet Narain (1997) : insulating the CBI from interference and placing it under the supervision of the Central Vigilance Commission",
   "Bandhua Mukti Morcha (1984) : the identification, release and rehabilitation of bonded labourers",
   "Shafin Jahan (2018) : an adult's right to marry a person of their choice as part of personal liberty",
   "T.M.A. Pai Foundation (2002) : holding that linguistic minorities have no right to set up educational institutions"],
  ["विनीत नारायण (1997) : CBI को हस्तक्षेप से बचाना और उसे केंद्रीय सतर्कता आयोग के पर्यवेक्षण में रखना",
   "बंधुआ मुक्ति मोर्चा (1984) : बंधुआ मज़दूरों की पहचान, मुक्ति और पुनर्वास",
   "शफ़िन जहाँ (2018) : वैयक्तिक स्वतंत्रता के अंग के रूप में किसी वयस्क का अपनी पसंद के व्यक्ति से विवाह का अधिकार",
   "टी.एम.ए. पाई फ़ाउंडेशन (2002) : यह मानना कि भाषाई अल्पसंख्यकों को शिक्षण संस्थान स्थापित करने का अधिकार नहीं है"],
  2,
  "Pairs 1, 2 and 3 are correctly matched. Vineet Narain arose from the Jain hawala diaries case and led to statutory status for the CVC; Bandhua Mukti Morcha, a public interest case, read the right to live with dignity into the plight of bonded quarry workers; and in the Hadiya case the Court held that the choice of a partner lies with the adult concerned. "
  "Pair 4 is wrong: T.M.A. Pai upheld the right of both religious and linguistic minorities under Article 30 to establish and administer educational institutions, holding that minority status is to be decided State by State, and allowed reasonable regulation of them.",
  "युग्म 1, 2 और 3 सही सुमेलित हैं। विनीत नारायण जैन हवाला डायरी मामले से उपजा और इससे CVC को सांविधिक दर्जा मिला; जनहित मामले बंधुआ मुक्ति मोर्चा ने खदानों के बंधुआ मज़दूरों की दुर्दशा पर गरिमा के साथ जीने के अधिकार को लागू किया; और हादिया मामले में न्यायालय ने माना कि जीवनसाथी का चुनाव संबंधित वयस्क का अधिकार है। "
  "युग्म 4 गलत है: टी.एम.ए. पाई ने अनुच्छेद 30 के अंतर्गत धार्मिक और भाषाई, दोनों अल्पसंख्यकों के शिक्षण संस्थान स्थापित करने और चलाने के अधिकार को बनाए रखा, यह माना कि अल्पसंख्यक दर्जा राज्यवार तय होगा, और उनके उचित विनियमन की अनुमति दी।",
  "Supreme Court of India (judgments as named).",
  "l1-rev-vineet-narain-bandhua-shafin-pai", craft="precision")

# ---------------------------------------------------------------- Panchayati Raj & Local Governance (h-pairs)
P("Panchayati Raj & Local Governance", "hard", "Consider the following pairs of village functionaries and bodies and how they are chosen or what they do:",
  "ग्राम स्तर के पदाधिकारियों और निकायों तथा उनके चुने जाने के तरीक़े या कार्य के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Sarpanch (Panchayat President) : elected head of the Gram Panchayat",
   "Panchayat Secretary : appointed by the government; calls Gram Sabha meetings and keeps their records",
   "Gram Sabha : all the adults registered as voters in the panchayat area",
   "Ward member (Panch) : elected by the voters of a ward"],
  ["सरपंच (पंचायत प्रधान) : ग्राम पंचायत का निर्वाचित प्रमुख",
   "पंचायत सचिव : सरकार द्वारा नियुक्त; ग्राम सभा की बैठकें बुलाता और उनके अभिलेख रखता है",
   "ग्राम सभा : पंचायत क्षेत्र के मतदाता के रूप में पंजीकृत सभी वयस्क",
   "वार्ड सदस्य (पंच) : किसी वार्ड के मतदाताओं द्वारा निर्वाचित"],
  3,
  "All four pairs are correctly matched. The panchayat area is divided into wards, each electing a ward member; the Gram Panchayat -- the sarpanch and ward members -- is accountable to the Gram Sabha, which approves its plans and reviews its work. "
  "The secretary, being a government employee rather than an elected person, provides continuity and keeps records, but the decisions rest with the elected body and the Gram Sabha.",
  "चारों युग्म सही सुमेलित हैं। पंचायत क्षेत्र वार्डों में बँटा होता है, जिनमें से हर एक वार्ड सदस्य चुनता है; ग्राम पंचायत -- सरपंच और वार्ड सदस्य -- ग्राम सभा के प्रति उत्तरदायी है, जो उसकी योजनाओं को स्वीकृति देती और उसके काम की समीक्षा करती है। "
  "सचिव, निर्वाचित व्यक्ति नहीं बल्कि सरकारी कर्मचारी होने के कारण, निरंतरता देता और अभिलेख रखता है, पर निर्णय निर्वाचित निकाय और ग्राम सभा के होते हैं।",
  f"{SPL6} (Panchayati Raj).",
  "l1-rev-village-functionaries-pairs", craft="recall")

write("rev_l1_t7_a.sql")
