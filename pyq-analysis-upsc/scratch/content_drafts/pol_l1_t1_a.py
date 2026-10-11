# -*- coding: utf-8 -*-
"""Level 1 · Test 1 (Polity, NCERT Foundation) -- part A: Constitutional Framework (15) and Fundamental
Rights, DPSP & Duties (9). 24 new bilingual rows on the Level-1 cell targets (upsc_l1_cell_targets.mjs 1):
  Constitutional Framework: easy MCQ 1, easy statement 3, easy Statement-I/II 1, medium MCQ 1, medium
    statement 5, medium Statement-I/II 1, medium pairs 1, hard MCQ 1, hard statement 1.
  Rights: easy MCQ 1, easy statement 2, medium MCQ 1, medium statement 3, medium Statement-I/II 1,
    hard statement 1.
Level 1 tests what the NCERT books teach -- the functions and authority of a constitution, the ideas behind
liberty, equality, rights and the rule of law, the Constitution's philosophy -- in the UPSC formats. The
Level-2 rows are not repeated: no row here turns on the Constituent Assembly's composition, the Preamble's
words, Articles 14-18 or 23-24 as such, the judgments in the Level-2 pairs, or Article 253."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Polity"
d.REQUIRE_CRAFT = True
CF = "Constitutional Framework"
FR = "Fundamental Rights, DPSP & Duties"
COI = "Constitution of India"
NC11 = "NCERT Class XI, Political Science -- Indian Constitution at Work"
PT11 = "NCERT Class XI, Political Science -- Political Theory"
DP9 = "NCERT Class IX, Democratic Politics"
FIVE = ["Only two", "Only three", "Only four", "All five"]
FIVE_HI = ["केवल दो", "केवल तीन", "केवल चार", "सभी पाँच"]

# ================================================================ CONSTITUTIONAL FRAMEWORK (15)
# ---------------------------------------------------------------- easy (5)
M(CF, "easy", "Which one of the following best describes 'constitutionalism'?",
  "निम्नलिखित में से कौन-सा 'संविधानवाद' का सबसे अच्छा वर्णन करता है?",
  ["A system in which the powers of government are limited by a higher law that ordinary laws cannot override",
   "The practice of writing down every law of the country, old or new, in a single codified document",
   "The rule that a party with a majority in the legislature may enact any law it chooses, on any subject",
   "The belief that the customs and traditions of a people should always prevail over laws made by the legislature"],
  ["ऐसी व्यवस्था जिसमें सरकार की शक्तियाँ एक उच्चतर विधि से सीमित हों जिसे साधारण कानून लाँघ नहीं सकते",
   "देश के हर कानून को, पुराना हो या नया, एक ही संहिताबद्ध दस्तावेज़ में लिखने की प्रथा",
   "यह नियम कि विधायिका में बहुमत वाला दल किसी भी विषय पर अपनी पसंद का कोई भी कानून बना सकता है",
   "यह मान्यता कि किसी जनता के रीति-रिवाज और परंपराएँ विधायिका के बनाए कानूनों पर सदा भारी पड़नी चाहिए"],
  0,
  "Constitutionalism is the idea of limited government: those who hold power are bound by a higher law, and an ordinary law or a passing majority cannot set it aside. "
  "Codifying laws in one document is not the point -- Britain has constitutional government without a single written constitution. Unlimited majority rule is the opposite of constitutionalism, and putting custom above enacted law is a different idea altogether.",
  "संविधानवाद सीमित सरकार का विचार है: सत्ता रखने वाले एक उच्चतर विधि से बँधे होते हैं, और कोई साधारण कानून या अस्थायी बहुमत उसे दरकिनार नहीं कर सकता। "
  "कानूनों को एक दस्तावेज़ में संहिताबद्ध करना इसका मूल नहीं है -- ब्रिटेन में एक लिखित संविधान के बिना भी संवैधानिक सरकार है। असीमित बहुमत-शासन संविधानवाद का उलटा है, और प्रथा को बनाए गए कानून से ऊपर रखना बिल्कुल अलग विचार है।",
  f"{NC11}, Chapter 1 (Constitution: Why and How?).",
  "l1-pol-constitutionalism-limited-government", craft="precision")

S(CF, "easy", "Consider the following statements about the functions of a constitution:",
  "संविधान के कार्यों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The only purpose of a constitution is to limit the powers of the government.",
   "Unlike an ordinary law, a constitution cannot express the aspirations of a society or set goals for its government."],
  ["संविधान का एकमात्र उद्देश्य सरकार की शक्तियों को सीमित करना है।",
   "साधारण कानून के विपरीत, संविधान किसी समाज की आकांक्षाएँ व्यक्त नहीं कर सकता या उसकी सरकार के लिए लक्ष्य तय नहीं कर सकता।"],
  T2, 3,
  "Neither statement is correct. A constitution does several things: it sets the basic rules that let members of a society coordinate, it specifies who has the power to make decisions and how the government is formed, it limits what the government may do, and it enables the government to fulfil the society's aspirations -- the Directive Principles are India's example. "
  "So limiting power is one function, not the only one (statement 1), and setting goals is precisely what many constitutions do (statement 2).",
  "कोई भी कथन सही नहीं है। संविधान कई काम करता है: वह ऐसे बुनियादी नियम तय करता है जिनसे समाज के सदस्य आपस में तालमेल बिठा सकें, वह बताता है कि निर्णय लेने की शक्ति किसके पास है और सरकार कैसे बनती है, वह सीमित करता है कि सरकार क्या कर सकती है, और वह सरकार को समाज की आकांक्षाएँ पूरी करने में सक्षम बनाता है -- राज्य की नीति के निदेशक तत्व भारत का उदाहरण हैं। "
  "अतः शक्ति सीमित करना एक कार्य है, एकमात्र नहीं (कथन 1), और लक्ष्य तय करना ठीक वही है जो कई संविधान करते हैं (कथन 2)।",
  f"{NC11}, Chapter 1.",
  "l1-pol-functions-of-a-constitution", craft="inference")

S(CF, "easy", "Consider the following statements about the Constitution of India as a living document:",
  "एक जीवंत दस्तावेज़ के रूप में भारत के संविधान के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Judicial interpretation has changed the way some provisions work without any change in their text.",
   "Many amendments have dealt with technical or administrative matters, such as raising the retirement age of High Court judges."],
  ["न्यायिक व्याख्या ने कुछ प्रावधानों के काम करने का तरीका उनके पाठ में कोई बदलाव किए बिना बदला है।",
   "कई संशोधन तकनीकी या प्रशासनिक विषयों से जुड़े रहे हैं, जैसे उच्च न्यायालय के न्यायाधीशों की सेवानिवृत्ति आयु बढ़ाना।"],
  T2, 2,
  "Both statements are correct. A constitution stays alive in two ways: by formal amendment and by interpretation. Courts have read new meaning into existing words -- the right to life in Article 21 now covers a dignified life, though its text is unchanged. "
  "And a large share of the amendments have been technical: the Fifteenth Amendment (1963), for instance, raised the retirement age of High Court judges from 60 to 62. Few amendments have altered the Constitution's basic philosophy.",
  "दोनों कथन सही हैं। संविधान दो तरह से जीवंत रहता है: औपचारिक संशोधन से और व्याख्या से। न्यायालयों ने मौजूदा शब्दों में नए अर्थ पढ़े हैं -- अनुच्छेद 21 का जीवन का अधिकार अब गरिमापूर्ण जीवन तक फैला है, यद्यपि उसका पाठ नहीं बदला। "
  "और संशोधनों का बड़ा हिस्सा तकनीकी रहा है: उदाहरण के लिए पंद्रहवें संशोधन (1963) ने उच्च न्यायालय के न्यायाधीशों की सेवानिवृत्ति आयु 60 से बढ़ाकर 62 की। बहुत कम संशोधनों ने संविधान के मूल दर्शन को बदला है।",
  f"{NC11}, Chapter 9 (Constitution as a Living Document).",
  "l1-pol-living-document-interpretation-technical-amendments", craft="inference")

S(CF, "easy", "Consider the following statements about democracy:",
  "लोकतंत्र के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["A government chosen in a free and fair election can still act undemocratically if it does not respect the rule of law and the rights of citizens.",
   "In a democracy, a government elected by the majority may set aside the rights of a minority if the majority so wishes."],
  ["स्वतंत्र और निष्पक्ष चुनाव में चुनी गई सरकार भी अलोकतांत्रिक ढंग से काम कर सकती है, यदि वह विधि के शासन और नागरिकों के अधिकारों का सम्मान न करे।",
   "लोकतंत्र में बहुमत द्वारा चुनी गई सरकार बहुमत चाहे तो अल्पसंख्यकों के अधिकारों को दरकिनार कर सकती है।"],
  T2, 0,
  "Only statement 1 is correct. Elections are necessary but not sufficient: a democracy also needs the rule of law and respect for rights, so an elected government that ignores them is not acting democratically. "
  "Statement 2 describes majoritarianism, which is what a constitutional democracy guards against: rights are placed beyond the reach of a passing majority, and the courts can strike down laws that violate them.",
  "केवल कथन 1 सही है। चुनाव आवश्यक हैं पर पर्याप्त नहीं: लोकतंत्र को विधि का शासन और अधिकारों का सम्मान भी चाहिए, इसलिए इन्हें अनदेखा करने वाली निर्वाचित सरकार लोकतांत्रिक ढंग से काम नहीं कर रही। "
  "कथन 2 बहुसंख्यकवाद का वर्णन करता है, जिससे संवैधानिक लोकतंत्र बचाव करता है: अधिकार किसी अस्थायी बहुमत की पहुँच से बाहर रखे जाते हैं, और न्यायालय उनका उल्लंघन करने वाले कानूनों को रद्द कर सकते हैं।",
  f"{DP9}, Chapter 1 (What is Democracy? Why Democracy?).",
  "l1-pol-democracy-beyond-elections", craft="inference")

A(CF, "easy",
  "A written constitution makes judicial review of laws easier to exercise.",
  "लिखित संविधान कानूनों की न्यायिक समीक्षा करना आसान बनाता है।",
  "Courts can measure an ordinary law against the text of a written constitution that has a higher status than that law.",
  "न्यायालय किसी साधारण कानून को उस लिखित संविधान के पाठ पर परख सकते हैं जिसका दर्जा उस कानून से ऊँचा है।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I. Judicial review means testing a law against a higher norm; a written constitution supplies that norm in a definite text, ranked above ordinary legislation. "
  "In Britain, which has no single written constitution, courts cannot strike down an Act of Parliament; in India, the written Constitution is the standard by which courts test laws.",
  "दोनों कथन सही हैं, और कथन-II कथन-I की व्याख्या करता है। न्यायिक समीक्षा का अर्थ है किसी कानून को एक उच्चतर मानक पर परखना; लिखित संविधान वह मानक एक निश्चित पाठ में देता है, जो साधारण कानून से ऊपर होता है। "
  "ब्रिटेन में, जहाँ कोई एक लिखित संविधान नहीं है, न्यायालय संसद के किसी अधिनियम को रद्द नहीं कर सकते; भारत में लिखित संविधान ही वह कसौटी है जिस पर न्यायालय कानूनों को परखते हैं।",
  f"{NC11}, Chapters 1 and 6 (Judiciary).",
  "l1-pol-written-constitution-judicial-review", craft="linkage")

# ---------------------------------------------------------------- medium (8)
M(CF, "medium", "Which one of the following best describes the idea of 'principled distance' that characterises Indian secularism?",
  "निम्नलिखित में से कौन-सा भारतीय पंथनिरपेक्षता की विशेषता 'सैद्धांतिक दूरी' के विचार का सबसे अच्छा वर्णन करता है?",
  ["The State may engage with a religion or keep away from it, as liberty and equality require",
   "The State keeps an equal distance from all religions and never intervenes in any religious matter",
   "The State adopts the religion of the majority but allows the minorities to worship freely",
   "The State gives every religion funds in exact proportion to the number of its followers"],
  ["राज्य स्वतंत्रता और समानता की ज़रूरत के अनुसार किसी धर्म से जुड़ सकता है या उससे दूर रह सकता है",
   "राज्य सभी धर्मों से बराबर दूरी रखता है और किसी भी धार्मिक मामले में कभी भी कोई हस्तक्षेप नहीं करता",
   "राज्य बहुसंख्यकों का धर्म अपनाता है पर अल्पसंख्यकों को स्वतंत्र रूप से उपासना करने देता है",
   "राज्य हर धर्म को उसके अनुयायियों की संख्या के ठीक अनुपात में धन देता है"],
  0,
  "Indian secularism does not erect a wall between State and religion. The State may intervene in a religion to end a practice that violates liberty or equality -- untouchability is abolished and Hindu temples were opened to all castes -- and it may also support religious communities, for example through aid to minority educational institutions. "
  "Whether it engages or stays away depends on the values at stake: that is 'principled distance'. Strict non-intervention is the model of strict separation, a State religion is ruled out by the Constitution, and the Constitution provides for no funding by headcount.",
  "भारतीय पंथनिरपेक्षता राज्य और धर्म के बीच दीवार नहीं खड़ी करती। राज्य स्वतंत्रता या समानता का उल्लंघन करने वाली किसी प्रथा को समाप्त करने के लिए धर्म में हस्तक्षेप कर सकता है -- अस्पृश्यता समाप्त की गई है और हिंदू मंदिर सभी जातियों के लिए खोले गए -- और वह धार्मिक समुदायों की सहायता भी कर सकता है, जैसे अल्पसंख्यक शिक्षण संस्थानों को अनुदान देकर। "
  "वह जुड़े या दूर रहे, यह दाँव पर लगे मूल्यों पर निर्भर करता है: यही 'सैद्धांतिक दूरी' है। पूर्ण अहस्तक्षेप कठोर पृथक्करण का मॉडल है, राज्य-धर्म संविधान में वर्जित है, और संविधान संख्या के आधार पर धन देने का कोई प्रावधान नहीं करता।",
  f"{PT11}, Chapter 8 (Secularism); {NC11}, Chapter 10 (The Philosophy of the Constitution).",
  "l1-pol-principled-distance-secularism", craft="precision")

S(CF, "medium", "Consider the following statements about how the Constituent Assembly worked:",
  "संविधान सभा की कार्यप्रणाली के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It worked through committees, and most of its decisions were reached by consensus rather than by votes along party lines.",
   "Its debates were held in secret so that members could speak frankly.",
   "The draft constitution was published so that the public could discuss it and propose changes before it was finalised."],
  ["वह समितियों के माध्यम से काम करती थी, और उसके अधिकांश निर्णय दलगत मतदान के बजाय सर्वसम्मति से लिए गए।",
   "उसकी बहसें गुप्त रखी जाती थीं ताकि सदस्य खुलकर बोल सकें।",
   "संविधान का प्रारूप प्रकाशित किया गया ताकि अंतिम रूप देने से पहले जनता उस पर चर्चा करे और बदलाव सुझाए।"],
  C3, 1,
  "Statements 1 and 3 are correct. The Assembly divided its work among committees and tried to carry everyone with it; most provisions were settled by deliberation and broad agreement. The draft constitution was published in early 1948 and people had months to comment on it, and the Assembly considered thousands of amendments. "
  "Statement 2 is wrong: the debates were open and recorded, and the Constituent Assembly Debates were printed in twelve volumes -- which is why the reasoning behind each provision can still be read.",
  "कथन 1 और 3 सही हैं। सभा ने अपना काम समितियों में बाँटा और सबको साथ लेकर चलने की कोशिश की; अधिकांश प्रावधान विचार-विमर्श और व्यापक सहमति से तय हुए। संविधान का प्रारूप 1948 के आरंभ में प्रकाशित हुआ और लोगों को उस पर टिप्पणी करने के लिए महीनों मिले, और सभा ने हज़ारों संशोधनों पर विचार किया। "
  "कथन 2 गलत है: बहसें खुली थीं और दर्ज की गईं, और संविधान सभा की बहसें बारह खंडों में छपीं -- इसीलिए हर प्रावधान के पीछे का तर्क आज भी पढ़ा जा सकता है।",
  f"{NC11}, Chapter 1; {DP9}, Chapter 2 (Constitutional Design).",
  "l1-pol-constituent-assembly-working-method", craft="recall")

S(CF, "medium", "Consider the following statements about India's sovereignty and its treaties:",
  "भारत की संप्रभुता और उसकी संधियों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["India's membership of the United Nations does not make the UN Charter superior to the Constitution of India.",
   "A treaty signed by India becomes enforceable in Indian courts automatically, without any legislation, in every case.",
   "A treaty can be ratified only after it has been approved by a two-thirds majority in both Houses of Parliament."],
  ["संयुक्त राष्ट्र की सदस्यता से संयुक्त राष्ट्र चार्टर भारत के संविधान से ऊपर नहीं हो जाता।",
   "भारत द्वारा हस्ताक्षरित संधि हर स्थिति में बिना किसी कानून के अपने आप भारतीय न्यायालयों में प्रवर्तनीय हो जाती है।",
   "किसी संधि का अनुसमर्थन संसद के दोनों सदनों में दो-तिहाई बहुमत से अनुमोदन के बाद ही हो सकता है।"],
  C3, 0,
  "Only statement 1 is correct. A sovereign State can accept international obligations by its own choice; doing so does not place any external authority above its Constitution. "
  "Statement 2 is wrong: where a treaty affects rights or requires a change in the law, Parliament has to legislate to give it effect -- courts may use a treaty to interpret the law where there is no conflict, but it is not self-executing in every case. "
  "Statement 3 is wrong: making and ratifying treaties is an executive act of the Union government; the Constitution requires no parliamentary vote, let alone a special majority, for ratification.",
  "केवल कथन 1 सही है। एक संप्रभु राज्य अपनी इच्छा से अंतरराष्ट्रीय दायित्व स्वीकार कर सकता है; ऐसा करने से कोई बाहरी सत्ता उसके संविधान से ऊपर नहीं हो जाती। "
  "कथन 2 गलत है: जहाँ कोई संधि अधिकारों को प्रभावित करती हो या कानून में बदलाव माँगती हो, वहाँ उसे लागू करने के लिए संसद को कानून बनाना पड़ता है -- टकराव न होने पर न्यायालय कानून की व्याख्या में संधि का सहारा ले सकते हैं, पर वह हर स्थिति में स्वतः लागू नहीं होती। "
  "कथन 3 गलत है: संधियाँ करना और उनका अनुसमर्थन संघ सरकार का कार्यपालिका-कार्य है; संविधान अनुसमर्थन के लिए संसद के किसी मतदान की, विशेष बहुमत की तो बात ही क्या, अपेक्षा नहीं करता।",
  f"{COI}, Articles 51, 73 and 253; {PT11}, Chapter 7 (Nationalism).",
  "l1-pol-sovereignty-treaties-dualism", craft="inference")

S(CF, "medium", "Consider the following statements about the philosophy of the Constitution of India:",
  "भारत के संविधान के दर्शन के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It adopted universal adult franchise at once, without any qualification of property or education.",
   "It recognises some rights of religious and linguistic minorities as rights of communities, not only of individuals.",
   "It allows different States to have different relations with the Union through special provisions."],
  ["उसने संपत्ति या शिक्षा की किसी योग्यता के बिना एक ही बार में सार्वभौमिक वयस्क मताधिकार अपनाया।",
   "वह धार्मिक और भाषाई अल्पसंख्यकों के कुछ अधिकारों को केवल व्यक्तियों के ही नहीं, समुदायों के अधिकार के रूप में मान्यता देता है।",
   "वह विशेष प्रावधानों के माध्यम से अलग-अलग राज्यों को संघ के साथ अलग-अलग संबंध रखने देता है।"],
  C3, 2,
  "All three statements are correct. Many Western democracies extended the vote in stages, by property, sex or education; India gave it to every adult from the first election. "
  "The rights of minorities to conserve their culture and to set up their own educational institutions (Articles 29 and 30) belong to communities, which sets Indian liberalism apart from purely individualist versions. "
  "And the special provisions for several States (Article 371 onwards) make Indian federalism asymmetric.",
  "तीनों कथन सही हैं। कई पश्चिमी लोकतंत्रों ने मताधिकार संपत्ति, लिंग या शिक्षा के आधार पर चरणों में बढ़ाया; भारत ने पहले चुनाव से ही हर वयस्क को यह दिया। "
  "अल्पसंख्यकों के अपनी संस्कृति को बनाए रखने और अपने शिक्षण संस्थान स्थापित करने के अधिकार (अनुच्छेद 29 और 30) समुदायों के हैं, जो भारतीय उदारवाद को विशुद्ध व्यक्तिवादी रूपों से अलग करता है। "
  "और कई राज्यों के लिए विशेष प्रावधान (अनुच्छेद 371 से आगे) भारतीय संघवाद को असममित बनाते हैं।",
  f"{NC11}, Chapter 10 (The Philosophy of the Constitution).",
  "l1-pol-philosophy-franchise-group-rights-asymmetry", craft="precision")

S(CF, "medium", "Consider the following in the context of political theory:",
  "राजनीतिक सिद्धांत के संदर्भ में निम्नलिखित पर विचार कीजिए:",
  ["A definite territory", "A government elected by the people", "A written constitution", "Sovereignty"],
  ["एक निश्चित भू-भाग", "जनता द्वारा चुनी गई सरकार", "एक लिखित संविधान", "संप्रभुता"],
  C4, 1,
  "Two are essential: a definite territory and sovereignty -- the other two classic elements being a population and a government that exercises authority. "
  "The government need not be elected: a monarchy or a dictatorship is still a State. Nor is a written constitution an element -- the United Kingdom is a State without a single written constitution, and States existed long before the first written constitutions.",
  "दो अनिवार्य हैं: एक निश्चित भू-भाग और संप्रभुता -- बाकी दो पारंपरिक तत्व हैं जनसंख्या और सत्ता का प्रयोग करने वाली सरकार। "
  "सरकार का निर्वाचित होना ज़रूरी नहीं: राजतंत्र या तानाशाही भी राज्य ही है। न ही लिखित संविधान कोई तत्व है -- यूनाइटेड किंगडम एक ऐसा राज्य है जिसका कोई एक लिखित संविधान नहीं है, और पहले लिखित संविधानों से बहुत पहले भी राज्य मौजूद थे।",
  f"{PT11}, Chapter 1 (Political Theory: An Introduction).",
  "l1-pol-elements-of-a-state", craft="precision", closing="How many of the above are essential elements of a State?",
  closing_hi="उपर्युक्त में से कितने राज्य के अनिवार्य तत्व हैं?")

S(CF, "medium", "Consider the following statements about B.R. Ambedkar's closing speech in the Constituent Assembly (25 November 1949):",
  "संविधान सभा में बी.आर. अंबेडकर के समापन भाषण (25 नवंबर 1949) के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["He warned that political democracy would not last unless it rested on social democracy.",
   "He urged that methods such as civil disobedience and satyagraha be given up once constitutional methods were available.",
   "He welcomed hero-worship in politics as a way of building national unity."],
  ["उन्होंने चेताया कि राजनीतिक लोकतंत्र तब तक नहीं टिकेगा जब तक वह सामाजिक लोकतंत्र पर आधारित न हो।",
   "उन्होंने आग्रह किया कि संवैधानिक तरीके उपलब्ध होने पर सविनय अवज्ञा और सत्याग्रह जैसे तरीके छोड़ दिए जाएँ।",
   "उन्होंने राष्ट्रीय एकता बनाने के तरीके के रूप में राजनीति में नायक-पूजा का स्वागत किया।"],
  C3, 1,
  "Statements 1 and 2 are correct. Ambedkar said that India was entering a life of contradictions -- equality in politics ('one man, one vote, one value') and inequality in social and economic life -- and that the contradiction had to be removed. "
  "He called unconstitutional methods, once constitutional ones were open, 'the grammar of anarchy'. "
  "Statement 3 reverses his third warning: he cautioned against laying one's liberties at the feet of a great man, because hero-worship in politics leads to degradation and dictatorship.",
  "कथन 1 और 2 सही हैं। अंबेडकर ने कहा कि भारत विरोधाभासों के जीवन में प्रवेश कर रहा है -- राजनीति में समानता ('एक व्यक्ति, एक वोट, एक मूल्य') और सामाजिक-आर्थिक जीवन में असमानता -- और इस विरोधाभास को दूर करना होगा। "
  "संवैधानिक तरीके खुले होने पर असंवैधानिक तरीकों को उन्होंने 'अराजकता का व्याकरण' कहा। "
  "कथन 3 उनकी तीसरी चेतावनी को उलट देता है: उन्होंने अपनी स्वतंत्रताएँ किसी महापुरुष के चरणों में रख देने से सावधान किया, क्योंकि राजनीति में नायक-पूजा पतन और तानाशाही की ओर ले जाती है।",
  "Constituent Assembly Debates, Volume XI (25 November 1949); NCERT Class XI, Political Science -- Indian Constitution at Work, Chapter 10.",
  "l1-pol-ambedkar-closing-speech-warnings", craft="recall")

A(CF, "medium",
  "The Parliament of India is sovereign in the same way as the British Parliament.",
  "भारत की संसद ब्रिटिश संसद की तरह ही संप्रभु है।",
  "Laws made by the Parliament of India can be struck down by the courts if they violate the Constitution.",
  "भारत की संसद के बनाए कानूनों को न्यायालय रद्द कर सकते हैं यदि वे संविधान का उल्लंघन करते हों।",
  3,
  "Statement-I is incorrect and Statement-II is correct. In Britain, Parliament is sovereign: no court can set aside an Act of Parliament. India chose constitutional supremacy instead: Parliament is bound by a written Constitution, its laws are subject to judicial review, and even its power to amend the Constitution cannot touch the basic structure. "
  "Statement-II is the very reason Statement-I is false.",
  "कथन-I गलत है और कथन-II सही है। ब्रिटेन में संसद संप्रभु है: कोई न्यायालय संसद के अधिनियम को रद्द नहीं कर सकता। भारत ने इसके बजाय संविधान की सर्वोच्चता चुनी: संसद एक लिखित संविधान से बँधी है, उसके कानून न्यायिक समीक्षा के अधीन हैं, और संविधान संशोधन की उसकी शक्ति भी मूल ढाँचे को नहीं छू सकती। "
  "कथन-II ही वह कारण है जिससे कथन-I गलत है।",
  f"{NC11}, Chapters 5 (Legislature) and 6 (Judiciary).",
  "l1-pol-parliament-not-sovereign-like-britain", craft="linkage")

P(CF, "medium", "Consider the following pairs of a provision of the Constitution of India and the function of a constitution it serves:",
  "भारत के संविधान के किसी प्रावधान और उसके द्वारा पूरे किए जाने वाले संविधान के कार्य के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Article 79 (Parliament consists of the President and two Houses) : Specifies who has the power to make laws",
   "Article 19 (freedoms, subject to reasonable restrictions) : Limits what a government may do to its citizens",
   "Article 38 (State to secure a social order based on justice) : Enables a government to fulfil a society's aspirations",
   "Article 1 (India, that is Bharat, shall be a Union of States) : Specifies how the government is to be constituted"],
  ["अनुच्छेद 79 (संसद में राष्ट्रपति और दो सदन होते हैं) : बताता है कि कानून बनाने की शक्ति किसके पास है",
   "अनुच्छेद 19 (स्वतंत्रताएँ, युक्तियुक्त निर्बंधनों के अधीन) : सीमित करता है कि सरकार अपने नागरिकों के साथ क्या कर सकती है",
   "अनुच्छेद 38 (राज्य न्याय पर आधारित सामाजिक व्यवस्था सुनिश्चित करेगा) : सरकार को समाज की आकांक्षाएँ पूरी करने में सक्षम बनाता है",
   "अनुच्छेद 1 (भारत, अर्थात् इंडिया, राज्यों का संघ होगा) : बताता है कि सरकार का गठन कैसे होगा"],
  2,
  "Pairs 1, 2 and 3 are correctly matched. Article 79 sets up the law-making body, so it allocates decision-making power; Article 19's freedoms mark out what the State may not do, except within reasonable restrictions; and Article 38 sets a goal for the State, which is the 'aspirational' function. "
  "Pair 4 is wrong: Article 1 names the country and describes it as a Union of States, which defines the political community and its territory -- it says nothing about how the government is to be constituted, which Parts V and VI do.",
  "युग्म 1, 2 और 3 सही सुमेलित हैं। अनुच्छेद 79 कानून बनाने वाली संस्था गठित करता है, अतः वह निर्णय की शक्ति बाँटता है; अनुच्छेद 19 की स्वतंत्रताएँ बताती हैं कि राज्य युक्तियुक्त निर्बंधनों के सिवा क्या नहीं कर सकता; और अनुच्छेद 38 राज्य के लिए एक लक्ष्य तय करता है, जो 'आकांक्षा' वाला कार्य है। "
  "युग्म 4 गलत है: अनुच्छेद 1 देश का नाम बताता है और उसे राज्यों का संघ कहता है, जो राजनीतिक समुदाय और उसके भू-भाग को परिभाषित करता है -- वह यह नहीं बताता कि सरकार का गठन कैसे होगा, जो भाग V और VI बताते हैं।",
  f"{NC11}, Chapter 1; {COI}, Articles 1, 19, 38 and 79.",
  "l1-pol-provisions-and-functions-pairs", craft="linkage")

# ---------------------------------------------------------------- hard (2)
M(CF, "hard", "Which one of the following is the best example of 'positive liberty' as distinct from 'negative liberty'?",
  "निम्नलिखित में से कौन-सा 'नकारात्मक स्वतंत्रता' से भिन्न 'सकारात्मक स्वतंत्रता' का सबसे अच्छा उदाहरण है?",
  ["Free and compulsory schooling that helps every child develop his or her abilities",
   "A rule that the police may not search a person's home without a warrant from a court",
   "The absence of any censorship of what newspapers may print about the government",
   "A bar on the State compelling anyone to take part in a religious ceremony against his will"],
  ["निःशुल्क और अनिवार्य शिक्षा जो हर बच्चे को अपनी क्षमताएँ विकसित करने में मदद करे",
   "यह नियम कि पुलिस न्यायालय के वारंट के बिना किसी व्यक्ति के घर की तलाशी नहीं ले सकती",
   "सरकार के बारे में समाचार-पत्र क्या छापें, इस पर किसी भी प्रकार की सेंसरशिप का न होना",
   "राज्य द्वारा किसी को उसकी इच्छा के विरुद्ध किसी धार्मिक अनुष्ठान में भाग लेने के लिए बाध्य करने पर रोक"],
  0,
  "Negative liberty is an area of non-interference: freedom from restraint. Positive liberty is the freedom to develop oneself, which may need the State to act and create enabling conditions. "
  "Free and compulsory schooling is such a condition -- it expands what a child is actually able to become. A ban on warrantless searches, the absence of censorship and a bar on compelled worship all protect a person by keeping the State out, which is negative liberty.",
  "नकारात्मक स्वतंत्रता अहस्तक्षेप का क्षेत्र है: बंधन से मुक्ति। सकारात्मक स्वतंत्रता स्वयं को विकसित करने की स्वतंत्रता है, जिसके लिए राज्य को सक्रिय होकर अनुकूल परिस्थितियाँ बनानी पड़ सकती हैं। "
  "निःशुल्क और अनिवार्य शिक्षा ऐसी ही परिस्थिति है -- वह बढ़ाती है कि बच्चा वास्तव में क्या बन सकता है। बिना वारंट तलाशी पर रोक, सेंसरशिप का अभाव और बलपूर्वक उपासना पर रोक, ये सब राज्य को दूर रखकर व्यक्ति की रक्षा करते हैं, जो नकारात्मक स्वतंत्रता है।",
  f"{PT11}, Chapter 2 (Freedom).",
  "l1-pol-positive-negative-liberty", craft="application")

S(CF, "hard", "Consider the following statements about the 'rule of law':",
  "'विधि के शासन' के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["No one is above the law, including those who make it.",
   "Laws must be known in advance, and no one may be punished under a criminal law made after the act was done.",
   "The rule of law is satisfied whenever an action is authorised by some law, whatever that law says.",
   "The Supreme Court has held the rule of law to be a part of the basic structure of the Constitution."],
  ["कोई भी कानून से ऊपर नहीं है, कानून बनाने वाले भी नहीं।",
   "कानून पहले से ज्ञात होने चाहिए, और किसी को भी कृत्य होने के बाद बने आपराधिक कानून के तहत दंडित नहीं किया जा सकता।",
   "जब भी कोई कार्य किसी कानून द्वारा अधिकृत हो, उस कानून में चाहे जो लिखा हो, विधि का शासन संतुष्ट हो जाता है।",
   "सर्वोच्च न्यायालय ने विधि के शासन को संविधान के मूल ढाँचे का भाग माना है।"],
  C4, 2,
  "Statements 1, 2 and 4 are correct. The rule of law means that power is exercised under known, general laws that bind rulers too; Article 20(1) bars ex post facto criminal punishment; and in Indira Nehru Gandhi v. Raj Narain (1975) the rule of law was treated as a basic feature. "
  "Statement 3 describes 'rule by law', not the rule of law: a law that is arbitrary, secret or retrospective in punishment can authorise an act and still violate the rule of law, which is why Indian courts test laws for arbitrariness and reasonableness as well as for authority.",
  "कथन 1, 2 और 4 सही हैं। विधि के शासन का अर्थ है कि शक्ति का प्रयोग ज्ञात, सामान्य कानूनों के तहत हो जो शासकों को भी बाँधें; अनुच्छेद 20(1) भूतलक्षी आपराधिक दंड पर रोक लगाता है; और इंदिरा नेहरू गांधी बनाम राज नारायण (1975) में विधि के शासन को मूल विशेषता माना गया। "
  "कथन 3 'कानून द्वारा शासन' का वर्णन करता है, विधि के शासन का नहीं: मनमाना, गुप्त या भूतलक्षी दंड वाला कानून किसी कार्य को अधिकृत करके भी विधि के शासन का उल्लंघन कर सकता है, इसीलिए भारतीय न्यायालय कानूनों को अधिकार के साथ-साथ मनमानेपन और युक्तियुक्तता की कसौटी पर भी परखते हैं।",
  f"{COI}, Article 20(1); Supreme Court of India, Indira Nehru Gandhi v. Raj Narain (1975).",
  "l1-pol-rule-of-law-elements", craft="inference")

# ================================================================ RIGHTS, DPSP & DUTIES (9)
# ---------------------------------------------------------------- easy (3)
M(FR, "easy", "In political theory, which one of the following best describes a 'right'?",
  "राजनीतिक सिद्धांत में निम्नलिखित में से कौन-सा 'अधिकार' का सबसे अच्छा वर्णन करता है?",
  ["A claim that society recognises as justified and that others are obliged to respect",
   "Anything that a person wishes to do, whether or not it affects other people at all",
   "A privilege that a ruler grants to his subjects and may withdraw whenever he likes",
   "A duty that every individual owes to the State and that the State can enforce by law"],
  ["ऐसा दावा जिसे समाज उचित मानता है और जिसका सम्मान करने के लिए दूसरे बाध्य हैं",
   "कोई भी काम जो व्यक्ति करना चाहे, चाहे वह दूसरों को प्रभावित करे या बिल्कुल न करे",
   "ऐसा विशेषाधिकार जो शासक अपनी प्रजा को देता है और जब चाहे वापस ले सकता है",
   "ऐसा कर्तव्य जो हर व्यक्ति राज्य के प्रति रखता है और जिसे राज्य कानून से लागू करा सकता है"],
  0,
  "A right is a justified claim: something a person is entitled to, which society recognises -- in law or in morality -- and which places others, including the State, under an obligation to respect it. "
  "A mere wish is not a right, especially when it harms others; a revocable favour of a ruler is the opposite of a right; and a duty owed to the State is the correlative of a right, not a right itself.",
  "अधिकार एक उचित दावा है: ऐसी चीज़ जिसका व्यक्ति हकदार है, जिसे समाज -- कानून में या नैतिकता में -- मान्यता देता है, और जो दूसरों पर, राज्य सहित, उसका सम्मान करने का दायित्व डालता है। "
  "केवल इच्छा अधिकार नहीं है, विशेषकर जब वह दूसरों को हानि पहुँचाए; शासक की वापस ली जा सकने वाली कृपा अधिकार का उलटा है; और राज्य के प्रति कर्तव्य अधिकार का सहवर्ती है, स्वयं अधिकार नहीं।",
  f"{PT11}, Chapter 5 (Rights).",
  "l1-pol-what-is-a-right", pos=3, craft="precision")

S(FR, "easy", "Consider the following statements about equality:",
  "समानता के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Formal equality before the law can exist alongside large inequalities of wealth.",
   "Treating everyone in exactly the same way always promotes equality.",
   "The Constitution of India permits special provisions for the advancement of socially and educationally backward classes."],
  ["कानून के समक्ष औपचारिक समानता संपत्ति की बड़ी असमानताओं के साथ भी मौजूद रह सकती है।",
   "हर किसी के साथ बिल्कुल एक जैसा व्यवहार करना सदा समानता को बढ़ावा देता है।",
   "भारत का संविधान सामाजिक और शैक्षिक रूप से पिछड़े वर्गों की उन्नति के लिए विशेष प्रावधानों की अनुमति देता है।"],
  C3, 1,
  "Statements 1 and 3 are correct. Equal legal status does not by itself remove inequalities of wealth or opportunity, which is why formal equality is distinguished from equality of opportunity and outcome. "
  "For the same reason statement 2 is wrong: identical treatment of people who start from unequal positions can keep the inequality in place, and some differential treatment may be needed to make equality real. "
  "The Constitution accepts this: Article 15(4) allows special provisions for socially and educationally backward classes and for Scheduled Castes and Scheduled Tribes.",
  "कथन 1 और 3 सही हैं। समान कानूनी दर्जा अपने आप संपत्ति या अवसर की असमानताएँ दूर नहीं करता, इसीलिए औपचारिक समानता को अवसर और परिणाम की समानता से अलग किया जाता है। "
  "इसी कारण कथन 2 गलत है: असमान स्थिति से शुरुआत करने वाले लोगों के साथ एक जैसा व्यवहार असमानता को बनाए रख सकता है, और समानता को वास्तविक बनाने के लिए कुछ विभेदक व्यवहार ज़रूरी हो सकता है। "
  "संविधान यह स्वीकार करता है: अनुच्छेद 15(4) सामाजिक और शैक्षिक रूप से पिछड़े वर्गों तथा अनुसूचित जातियों और अनुसूचित जनजातियों के लिए विशेष प्रावधानों की अनुमति देता है।",
  f"{PT11}, Chapter 3 (Equality); {COI}, Article 15(4).",
  "l1-pol-formal-and-substantive-equality", craft="inference")

S(FR, "easy", "Consider the following statements about the Fundamental Rights in the Constitution of India:",
  "भारत के संविधान में मौलिक अधिकारों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Fundamental Rights are absolute and can never be limited by any law.",
   "The Fundamental Rights can be claimed only against the State, never against private persons."],
  ["मौलिक अधिकार निरपेक्ष हैं और किसी भी कानून द्वारा कभी सीमित नहीं किए जा सकते।",
   "मौलिक अधिकारों का दावा केवल राज्य के विरुद्ध किया जा सकता है, निजी व्यक्तियों के विरुद्ध कभी नहीं।"],
  T2, 3,
  "Neither statement is correct. Most Fundamental Rights can be limited: the freedoms of Article 19, for example, are subject to reasonable restrictions on grounds such as public order, morality and the security of the State. "
  "And while most rights are guarantees against the State, a few also bind private persons -- the abolition of untouchability, the bar on forced labour and the prohibition of child labour in factories apply whoever the wrongdoer is.",
  "कोई भी कथन सही नहीं है। अधिकांश मौलिक अधिकार सीमित किए जा सकते हैं: उदाहरण के लिए अनुच्छेद 19 की स्वतंत्रताएँ लोक व्यवस्था, सदाचार और राज्य की सुरक्षा जैसे आधारों पर युक्तियुक्त निर्बंधनों के अधीन हैं। "
  "और यद्यपि अधिकांश अधिकार राज्य के विरुद्ध गारंटियाँ हैं, कुछ निजी व्यक्तियों पर भी लागू होते हैं -- अस्पृश्यता का अंत, बलात् श्रम पर रोक और कारखानों में बाल श्रम का निषेध, ये ग़लती करने वाला कोई भी हो, लागू होते हैं।",
  f"{NC11}, Chapter 2 (Rights in the Indian Constitution).",
  "l1-pol-rights-not-absolute-some-horizontal", craft="precision")

# ---------------------------------------------------------------- medium (5)
M(FR, "medium", "A State government reserves seats for women in its government colleges. Which one of the following provisions of the Constitution of India most directly permits this?",
  "एक राज्य सरकार अपने सरकारी महाविद्यालयों में महिलाओं के लिए सीटें आरक्षित करती है। भारत के संविधान का निम्नलिखित में से कौन-सा प्रावधान इसकी सबसे सीधी अनुमति देता है?",
  ["Article 15(3)", "Article 15(4)", "Article 16(4)", "Article 29(2)"],
  ["अनुच्छेद 15(3)", "अनुच्छेद 15(4)", "अनुच्छेद 16(4)", "अनुच्छेद 29(2)"],
  0,
  "Article 15(3) allows the State to make special provisions for women and children, despite the bar on discrimination on the ground of sex in Article 15(1); reserving college seats for women is such a provision. "
  "Article 15(4) covers socially and educationally backward classes, Scheduled Castes and Scheduled Tribes, not women as such; Article 16(4) concerns reservation in public appointments, not admissions; and Article 29(2) forbids denying admission to State-aided institutions on grounds of religion, race, caste or language.",
  "अनुच्छेद 15(3) राज्य को महिलाओं और बच्चों के लिए विशेष प्रावधान करने देता है, यद्यपि अनुच्छेद 15(1) लिंग के आधार पर भेदभाव पर रोक लगाता है; महाविद्यालय की सीटें महिलाओं के लिए आरक्षित करना ऐसा ही प्रावधान है। "
  "अनुच्छेद 15(4) सामाजिक और शैक्षिक रूप से पिछड़े वर्गों, अनुसूचित जातियों और अनुसूचित जनजातियों के लिए है, महिलाओं के लिए उस रूप में नहीं; अनुच्छेद 16(4) सार्वजनिक नियुक्तियों में आरक्षण से जुड़ा है, प्रवेश से नहीं; और अनुच्छेद 29(2) राज्य-सहायता प्राप्त संस्थाओं में धर्म, मूलवंश, जाति या भाषा के आधार पर प्रवेश से इनकार पर रोक लगाता है।",
  f"{COI}, Articles 15, 16 and 29.",
  "l1-pol-art15-3-seats-for-women", pos=0, craft="application")

S(FR, "medium", "Consider the following rights:",
  "निम्नलिखित अधिकारों पर विचार कीजिए:",
  ["The right to clean water and a pollution-free environment",
   "The right to shelter",
   "The right to emergency medical treatment",
   "The right to vote in elections"],
  ["स्वच्छ जल और प्रदूषण-मुक्त पर्यावरण का अधिकार",
   "आश्रय का अधिकार",
   "आपातकालीन चिकित्सा उपचार का अधिकार",
   "चुनावों में मतदान का अधिकार"],
  C4, 2,
  "The first three have been read into Article 21: a pollution-free environment and clean water (Subhash Kumar, 1991), shelter (Chameli Singh, 1996) and emergency medical aid, which no hospital may refuse to an injured person (Parmanand Katara, 1989). "
  "The right to vote is not a Fundamental Right: it rests on Article 326 and the Representation of the People Act, and the Supreme Court has described it as a statutory right.",
  "पहले तीन को अनुच्छेद 21 में पढ़ा गया है: प्रदूषण-मुक्त पर्यावरण और स्वच्छ जल (सुभाष कुमार, 1991), आश्रय (चमेली सिंह, 1996) और आपातकालीन चिकित्सा सहायता, जिसे कोई अस्पताल किसी घायल व्यक्ति को देने से इनकार नहीं कर सकता (परमानंद कटारा, 1989)। "
  "मतदान का अधिकार मौलिक अधिकार नहीं है: वह अनुच्छेद 326 और लोक प्रतिनिधित्व अधिनियम पर आधारित है, और सर्वोच्च न्यायालय ने उसे सांविधिक अधिकार कहा है।",
  "Supreme Court of India: Subhash Kumar (1991), Chameli Singh (1996), Parmanand Katara (1989); NCERT Class VIII, Social and Political Life -- III, Chapter 8 (Public Facilities).",
  "l1-pol-art21-water-shelter-medical-not-vote", craft="multi",
  closing="How many of the above has the Supreme Court read into the right to life and personal liberty under Article 21?", closing_hi="उपर्युक्त में से कितनों को सर्वोच्च न्यायालय ने अनुच्छेद 21 के तहत प्राण और दैहिक स्वतंत्रता के अधिकार में पढ़ा है?")

S(FR, "medium", "Consider the following statements about John Rawls's theory of justice:",
  "जॉन रॉल्स के न्याय के सिद्धांत के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["Fair rules, he argued, are those that people would choose if they did not know what position they would occupy in society.",
   "People choosing behind such a 'veil of ignorance' would favour rules that make the worst-off as well off as possible.",
   "He held that justice requires every person to receive exactly the same income."],
  ["उन्होंने तर्क दिया कि उचित नियम वे हैं जिन्हें लोग तब चुनेंगे जब उन्हें पता न हो कि समाज में उनकी स्थिति क्या होगी।",
   "ऐसे 'अज्ञानता के पर्दे' के पीछे चुनने वाले लोग ऐसे नियम पसंद करेंगे जो सबसे वंचित लोगों को यथासंभव बेहतर स्थिति में रखें।",
   "उनका मत था कि न्याय के लिए हर व्यक्ति को ठीक एक जैसी आय मिलनी चाहिए।"],
  C3, 1,
  "Statements 1 and 2 are correct. Rawls asked us to imagine choosing the rules of society without knowing whether we would be rich or poor, able or disabled; rational people in that position would protect themselves against the worst outcome, and so would accept inequalities only if they benefit the least advantaged. "
  "Statement 3 is wrong: Rawls allowed inequalities that work to the advantage of the worst-off; his theory is a case for fair distribution, not for identical incomes. The Directive Principles in Articles 38 and 39 rest on a similar idea of social justice.",
  "कथन 1 और 2 सही हैं। रॉल्स ने कहा कि कल्पना कीजिए हम समाज के नियम यह जाने बिना चुन रहे हैं कि हम अमीर होंगे या ग़रीब, सक्षम या अक्षम; उस स्थिति में तर्कशील लोग सबसे बुरे परिणाम से अपनी रक्षा करेंगे, और इसलिए असमानताएँ तभी स्वीकार करेंगे जब वे सबसे कम सुविधा वालों को लाभ दें। "
  "कथन 3 गलत है: रॉल्स ने ऐसी असमानताओं की अनुमति दी जो सबसे वंचितों के हित में हों; उनका सिद्धांत न्यायपूर्ण वितरण का पक्ष है, एक जैसी आय का नहीं। अनुच्छेद 38 और 39 के निदेशक तत्व सामाजिक न्याय के ऐसे ही विचार पर टिके हैं।",
  f"{PT11}, Chapter 4 (Social Justice).",
  "l1-pol-rawls-veil-of-ignorance", craft="inference")

S(FR, "medium", "Consider the following statements about J.S. Mill's 'harm principle':",
  "जे.एस. मिल के 'हानि सिद्धांत' के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It allows the State to restrict a person's action only to prevent harm to others.",
   "Under it, the State may restrict any action that other people find offensive.",
   "Under it, actions that affect only the person concerned should be regulated by law for that person's own good."],
  ["यह राज्य को किसी व्यक्ति के कार्य को केवल दूसरों को हानि से बचाने के लिए सीमित करने देता है।",
   "इसके अनुसार राज्य हर उस कार्य को सीमित कर सकता है जिसे दूसरे लोग आपत्तिजनक पाते हैं।",
   "इसके अनुसार केवल संबंधित व्यक्ति को प्रभावित करने वाले कार्यों का, उसी व्यक्ति के भले के लिए, कानून से नियमन होना चाहिए।"],
  C3, 0,
  "Only statement 1 is correct. Mill distinguished self-regarding actions, which affect only the person concerned and should be left free, from other-regarding actions, which may be restrained only if they cause harm to others. "
  "Offence is not harm in this sense, so statement 2 is wrong; and statement 3 is the paternalism that Mill rejected -- a person's own good is no sufficient warrant for coercing him. Even for minor harms he preferred social disapproval to the force of law.",
  "केवल कथन 1 सही है। मिल ने स्व-संबंधी कार्यों, जो केवल संबंधित व्यक्ति को प्रभावित करते हैं और स्वतंत्र छोड़े जाने चाहिए, को पर-संबंधी कार्यों से अलग किया, जिन्हें तभी रोका जा सकता है जब वे दूसरों को हानि पहुँचाएँ। "
  "इस अर्थ में आपत्ति हानि नहीं है, इसलिए कथन 2 गलत है; और कथन 3 वही पितृसत्तावाद है जिसे मिल ने अस्वीकार किया -- किसी व्यक्ति का अपना भला उसे बाध्य करने का पर्याप्त आधार नहीं है। छोटी हानियों के लिए भी उन्होंने कानून के बल से अधिक सामाजिक नापसंदगी को उचित माना।",
  f"{PT11}, Chapter 2 (Freedom).",
  "l1-pol-mill-harm-principle", craft="inference")

A(FR, "medium",
  "Rights place obligations on others, including the State.",
  "अधिकार दूसरों पर, राज्य सहित, दायित्व डालते हैं।",
  "A right exists only when it can be enforced in a court of law.",
  "अधिकार तभी अस्तित्व में होता है जब उसे न्यायालय में लागू कराया जा सके।",
  2,
  "Statement-I is correct and Statement-II is incorrect. A right is a claim that others must respect: it may oblige the State to refrain from acting (free speech) or to act (free education), and it obliges other people not to violate it. "
  "But rights are not only legal: moral rights and human rights are claimed before they are enforceable, and the Directive Principles in India express rights-like goals -- the right to work, to an adequate livelihood -- that no court can enforce.",
  "कथन-I सही है और कथन-II गलत है। अधिकार ऐसा दावा है जिसका सम्मान दूसरों को करना होता है: वह राज्य को कोई काम न करने (अभिव्यक्ति की स्वतंत्रता) या करने (निःशुल्क शिक्षा) के लिए बाध्य कर सकता है, और दूसरे लोगों को उसका उल्लंघन न करने के लिए बाध्य करता है। "
  "पर अधिकार केवल कानूनी नहीं होते: नैतिक अधिकारों और मानवाधिकारों का दावा उनके प्रवर्तनीय होने से पहले किया जाता है, और भारत में निदेशक तत्व अधिकार जैसे लक्ष्य व्यक्त करते हैं -- काम का अधिकार, पर्याप्त आजीविका का अधिकार -- जिन्हें कोई न्यायालय लागू नहीं कराता।",
  f"{PT11}, Chapter 5 (Rights); {COI}, Articles 37, 39 and 41.",
  "l1-pol-rights-obligations-not-only-legal", craft="inference")

# ---------------------------------------------------------------- hard (1)
S(FR, "hard", "Consider the following:",
  "निम्नलिखित पर विचार कीजिए:",
  ["The Constitution (Seventy-third Amendment) Act, 1992",
   "The Legal Services Authorities Act, 1987",
   "The Maternity Benefit Act, 1961",
   "The Protection of Civil Rights Act, 1955",
   "The Environment (Protection) Act, 1986"],
  ["संविधान (तिहत्तरवाँ संशोधन) अधिनियम, 1992",
   "विधिक सेवा प्राधिकरण अधिनियम, 1987",
   "मातृत्व लाभ अधिनियम, 1961",
   "सिविल अधिकार संरक्षण अधिनियम, 1955",
   "पर्यावरण (संरक्षण) अधिनियम, 1986"],
  None, 2,
  "Four give effect mainly to a Directive Principle: the Seventy-third Amendment to Article 40 (organisation of village panchayats), the Legal Services Authorities Act to Article 39A (free legal aid), the Maternity Benefit Act to Article 42 (maternity relief) and the Environment (Protection) Act to Article 48A (protection of the environment). "
  "The Protection of Civil Rights Act enforces a Fundamental Right: it punishes the practice of untouchability, which Article 17 abolishes and Article 35 requires Parliament to make punishable.",
  "चार मुख्यतः किसी निदेशक तत्व को लागू करते हैं: तिहत्तरवाँ संशोधन अनुच्छेद 40 (ग्राम पंचायतों का संगठन) को, विधिक सेवा प्राधिकरण अधिनियम अनुच्छेद 39A (निःशुल्क विधिक सहायता) को, मातृत्व लाभ अधिनियम अनुच्छेद 42 (प्रसूति सहायता) को और पर्यावरण (संरक्षण) अधिनियम अनुच्छेद 48A (पर्यावरण का संरक्षण) को। "
  "सिविल अधिकार संरक्षण अधिनियम एक मौलिक अधिकार को लागू करता है: वह अस्पृश्यता के आचरण को दंडित करता है, जिसे अनुच्छेद 17 समाप्त करता है और अनुच्छेद 35 संसद से दंडनीय बनवाने की अपेक्षा करता है।",
  f"{COI}, Articles 17, 35, 39A, 40, 42 and 48A.",
  "l1-pol-laws-giving-effect-to-dpsp", opts=FIVE, opts_hi=FIVE_HI,
  closing="How many of the above give effect mainly to a Directive Principle of State Policy?",
  closing_hi="उपर्युक्त में से कितने मुख्यतः राज्य की नीति के किसी निदेशक तत्व को लागू करते हैं?", craft="multi")

write("pol_l1_t1_a.sql")
