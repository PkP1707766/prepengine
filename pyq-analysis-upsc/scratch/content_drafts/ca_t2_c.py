# -*- coding: utf-8 -*-
"""Current Affairs · Test 2 (April to June 2026) -- part C: Polity & Governance.

Polity in the news in April-June 2026: the ordinance raising the strength of the Supreme Court, the right to walk on
footpaths, the Delhi High Court on the right to be forgotten, the defeat of the Constitution (131st Amendment) Bill,
the law naming Amaravati the capital of Andhra Pradesh, the clarification on pending sedition trials, the FCRA
Amendment Rules, a deity as a juristic person, the draft regulations on AI in courts, prisoners with disabilities,
passports and citizenship, a woman judge elevated directly from the Bar, the Sabarimala reference before nine judges
and acid-attack survivors under the disability law. Every fact was searched in the whole UPSC bank and is one no row
tests."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2
from ca_common import MX, finish
from ca_t2_format import FORMAT, POS

d.SUBJECT = "Polity"
d.REQUIRE_CRAFT = True
COI = "Constitution of India"
GV, FD, EX, JV = "Governance", "Federalism & Special Provisions", "Union & State Executive", "Judicial-Verdicts"
CB, SL, EL, FR, CF = "Constitutional & Statutory Bodies", "Statutory-Laws", "Elections", "Fundamental Rights, DPSP & Duties", "Constitutional Framework"

S(JV, "hard", "On 16 May 2026 the President promulgated an ordinance to increase the number of judges of the Supreme Court. Consider the following statements:",
  "16 मई 2026 को राष्ट्रपति ने सर्वोच्च न्यायालय के न्यायाधीशों की संख्या बढ़ाने के लिए एक अध्यादेश प्रख्यापित किया। निम्नलिखित कथनों पर विचार कीजिए:",
  ["It raised the sanctioned strength of the Court to 38, including the Chief Justice of India.",
   "The previous increase, in 2019, had also been made by an ordinance.",
   "The number of judges of each High Court is likewise fixed by an Act of Parliament."],
  ["इसने न्यायालय की स्वीकृत संख्या भारत के मुख्य न्यायाधीश सहित 38 कर दी।",
   "2019 की पिछली वृद्धि भी एक अध्यादेश द्वारा की गई थी।",
   "प्रत्येक उच्च न्यायालय के न्यायाधीशों की संख्या भी इसी तरह संसद के एक अधिनियम से निर्धारित होती है।"],
  C3, 0,
  "Only statement 1 is correct. Article 124(1) lets Parliament fix the number of Supreme Court judges by law, and the Supreme Court (Number of Judges) Act, 1956 does so; the Supreme Court (Number of Judges) Amendment Ordinance, 2026 substituted 'thirty-seven' for 'thirty-three' in it, so that with the Chief Justice the Court has 38 judges, citing pendency. An ordinance has the same force as an Act, and a Bill to replace this one was introduced in the Lok Sabha in July 2026. "
  "Statement 2 is wrong: the increase from 31 to 34 in 2019 was made by an amending Act passed by Parliament in its regular session. Statement 3 is wrong: under Article 216 a High Court consists of a Chief Justice and such other judges as the President may from time to time deem necessary to appoint, so the strength of each High Court is fixed by the Union executive, not by Parliament.",
  "केवल कथन 1 सही है। अनुच्छेद 124(1) संसद को विधि द्वारा सर्वोच्च न्यायालय के न्यायाधीशों की संख्या तय करने देता है, और सर्वोच्च न्यायालय (न्यायाधीश संख्या) अधिनियम, 1956 यही करता है; सर्वोच्च न्यायालय (न्यायाधीश संख्या) संशोधन अध्यादेश, 2026 ने लंबित मामलों का हवाला देते हुए उसमें ‘तैंतीस’ के स्थान पर ‘सैंतीस’ रखा, जिससे मुख्य न्यायाधीश सहित न्यायालय में 38 न्यायाधीश हैं। अध्यादेश का बल अधिनियम के समान होता है, और इसका स्थान लेने के लिए जुलाई 2026 में लोकसभा में एक विधेयक पेश हुआ। "
  "कथन 2 ग़लत है: 2019 में 31 से 34 की वृद्धि संसद द्वारा उसके नियमित सत्र में पारित एक संशोधन अधिनियम से हुई थी। कथन 3 ग़लत है: अनुच्छेद 216 के अंतर्गत उच्च न्यायालय एक मुख्य न्यायाधीश और ऐसे अन्य न्यायाधीशों से मिलकर बनता है जिन्हें राष्ट्रपति समय-समय पर नियुक्त करना आवश्यक समझे, इसलिए हर उच्च न्यायालय की संख्या संघ की कार्यपालिका तय करती है, संसद नहीं।",
  "Supreme Court (Number of Judges) Amendment Ordinance, 2026 (16 May 2026) and the Supreme Court (Number of Judges) Amendment Act, 2019; Constitution of India, Articles 123, 124(1) and 216.",
  "ca-t2-pol-sc-strength-ordinance-38-art-216", craft="precision")

S(FR, "medium", "On 19 June 2026 the Supreme Court held that walking on safe footpaths is a fundamental right. Consider the following statements:",
  "19 जून 2026 को सर्वोच्च न्यायालय ने निर्णय दिया कि सुरक्षित फ़ुटपाथ पर चलना एक मौलिक अधिकार है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Court grounded the right in the freedom of movement under Article 19(1)(d), read with Article 21.",
   "It held that the existence of a road places a duty on municipal bodies and other local authorities to provide safe footpaths.",
   "It held that pedestrians can pursue their claims only under the Motor Vehicles Act, 1988."],
  ["न्यायालय ने इस अधिकार का आधार अनुच्छेद 21 के साथ पठित अनुच्छेद 19(1)(घ) के अंतर्गत संचरण की स्वतंत्रता को बनाया।",
   "इसने कहा कि सड़क के होने मात्र से नगर निकायों और अन्य स्थानीय प्राधिकरणों पर सुरक्षित फ़ुटपाथ उपलब्ध कराने का दायित्व आता है।",
   "इसने कहा कि पैदल यात्री अपने दावे केवल मोटर यान अधिनियम, 1988 के अंतर्गत उठा सकते हैं।"],
  C3, 1,
  "Statements 1 and 2 are correct. In a case arising from a five-year-old child struck by a tanker on a road without a footpath, a bench of Justices P.S. Narasimha and A.S. Chandurkar read a right to walk safely into the freedom to move freely throughout India (Article 19(1)(d)), with the other freedoms of Article 19(1) and the right to life (Article 21), and gave it priority over the movement of motor vehicles. It held that urban development authorities, municipalities and panchayats are bound to demarcate, build and keep footpaths free of encroachment, and turned the wider question into a continuing suo motu case. "
  "Statement 3 is wrong: the Court held that this constitutional right can be enforced independently of the remedies under the Motor Vehicles Act, 1988.",
  "कथन 1 और 2 सही हैं। बिना फ़ुटपाथ वाली सड़क पर एक टैंकर की चपेट में आए पाँच वर्ष के बच्चे के मामले में न्यायमूर्ति पी.एस. नरसिम्हा और ए.एस. चांदुरकर की पीठ ने सुरक्षित चलने के अधिकार को भारत भर में स्वतंत्र संचरण की स्वतंत्रता (अनुच्छेद 19(1)(घ)) में, अनुच्छेद 19(1) की अन्य स्वतंत्रताओं और जीवन के अधिकार (अनुच्छेद 21) के साथ, पढ़ा और इसे मोटर वाहनों की आवाजाही पर प्राथमिकता दी। इसने कहा कि शहरी विकास प्राधिकरण, नगरपालिकाएँ और पंचायतें फ़ुटपाथ चिह्नित करने, बनाने और उन्हें अतिक्रमण से मुक्त रखने के लिए बाध्य हैं, और व्यापक प्रश्न को एक सतत स्वतः संज्ञान मामले में बदल दिया। "
  "कथन 3 ग़लत है: न्यायालय ने कहा कि इस संवैधानिक अधिकार को मोटर यान अधिनियम, 1988 के उपचारों से स्वतंत्र रूप से लागू कराया जा सकता है।",
  "Supreme Court of India, Maniyar Iliyaz alias Shaik Riyaz v. P. Ayyappan (19 June 2026); Constitution of India, Articles 19(1)(d) and 21.",
  "ca-t2-pol-right-to-walk-footpaths-19-1-d", craft="application")

S(FR, "medium", "On 29 May 2026 the Delhi High Court recognised a right to be forgotten in respect of judicial records available online. Consider the following statements:",
  "29 मई 2026 को दिल्ली उच्च न्यायालय ने ऑनलाइन उपलब्ध न्यायिक अभिलेखों के संबंध में भुलाए जाने के अधिकार को मान्यता दी। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Court treated the right as a facet of the freedom of speech and expression under Article 19(1)(a).",
   "The reliefs it set out include de-indexing judgments from search results on a person's name and masking personal identifiers.",
   "The right allows a person to have the judgment itself deleted from the court's records."],
  ["न्यायालय ने इस अधिकार को अनुच्छेद 19(1)(क) के अंतर्गत वाक् और अभिव्यक्ति की स्वतंत्रता का एक पहलू माना।",
   "इसके द्वारा बताए गए उपचारों में किसी व्यक्ति के नाम पर आधारित खोज-परिणामों से निर्णयों को हटाना और व्यक्तिगत पहचान-चिह्नों को छिपाना शामिल है।",
   "यह अधिकार किसी व्यक्ति को न्यायालय के अभिलेखों से स्वयं निर्णय को मिटवाने देता है।"],
  C3, 0,
  "Only statement 2 is correct. Statement 1 is wrong, since the right rests on privacy rather than on free speech, which is the interest weighed against it. Deciding petitions from people who had been acquitted or discharged, or were parties to matrimonial disputes, the Court held that the right to be forgotten flows from the informational privacy recognised under Article 21 since the nine-judge ruling of 2017, and set out two reliefs: de-indexing the judgment from results of a search on the person's name, and masking names and other identifiers in digital copies. It held these enforceable against search engines and legal databases, which as intermediaries must observe the IT Rules, 2021. "
  "Statement 3 is wrong: the record of the court stays intact -- open justice requires that judgments remain available -- and what is restricted is how easily the person's name leads to it online. A later bench has questioned whether blanket directions are needed, suggesting relief case by case.",
  "केवल कथन 2 सही है। कथन 1 ग़लत है, क्योंकि यह अधिकार वाक्-स्वतंत्रता पर नहीं, निजता पर आधारित है; वाक्-स्वतंत्रता तो वह हित है जिसके विरुद्ध इसे तौला जाता है। उन लोगों की याचिकाओं पर, जो दोषमुक्त या उन्मोचित हुए थे या वैवाहिक विवादों के पक्षकार थे, न्यायालय ने कहा कि भुलाए जाने का अधिकार 2017 के नौ न्यायाधीशों के निर्णय से अनुच्छेद 21 के अंतर्गत मान्य सूचनात्मक निजता से निकलता है, और दो उपचार बताए: व्यक्ति के नाम की खोज के परिणामों से निर्णय को हटाना, और डिजिटल प्रतियों में नाम तथा अन्य पहचान-चिह्नों को छिपाना। इसने इन्हें सर्च इंजनों और विधिक डेटाबेस के विरुद्ध लागू करने योग्य माना, जिन्हें मध्यस्थ के रूप में आईटी नियम, 2021 का पालन करना होता है। "
  "कथन 3 ग़लत है: न्यायालय का अभिलेख अक्षुण्ण रहता है -- खुले न्याय के लिए निर्णयों का उपलब्ध रहना आवश्यक है -- और सीमित केवल यह होता है कि व्यक्ति का नाम ऑनलाइन कितनी आसानी से उस तक ले जाता है। बाद में एक पीठ ने प्रश्न उठाया है कि क्या व्यापक निर्देश आवश्यक हैं, और मामला-दर-मामला राहत का सुझाव दिया है।",
  "Delhi High Court, judgment on the right to be forgotten and de-indexing of judicial records (29 May 2026); Information Technology (Intermediary Guidelines and Digital Media Ethics Code) Rules, 2021; Constitution of India, Article 21.",
  "ca-t2-pol-delhi-hc-right-to-be-forgotten-de-indexing", craft="application")

A(COI, "hard",
  "On 17 April 2026 the Lok Sabha rejected the Constitution (131st Amendment) Bill, although more members voted for it than against it.",
  "17 अप्रैल 2026 को लोकसभा ने संविधान (131वाँ संशोधन) विधेयक अस्वीकार कर दिया, यद्यपि इसके पक्ष में विपक्ष से अधिक सदस्यों ने मत दिया।",
  "A Bill to amend the Constitution must be passed in each House by a majority of its total membership and by not less than two-thirds of the members present and voting.",
  "संविधान संशोधन विधेयक को प्रत्येक सदन में उसकी कुल सदस्यता के बहुमत और उपस्थित तथा मत देने वाले सदस्यों के कम से कम दो-तिहाई बहुमत से पारित होना चाहिए।",
  0,
  "Both statements are correct, and Statement-II explains Statement-I. The Bill sought to enlarge the Lok Sabha from 543 to 816 seats and to bring the one-third reservation for women into effect in 2029, with delimitation on the 2011 Census. In the division 298 members voted for it and 230 against: more than half the House's total membership, but short of the 352 votes -- two-thirds of the 528 present and voting -- that Article 368(2) demands, so it fell. "
  "The government then withdrew the Delimitation Bill and the Union Territories Laws (Amendment) Bill introduced with it. The 106th Amendment of 2023, under which women's reservation takes effect after the first delimitation following a new census, is unaffected.",
  "दोनों कथन सही हैं, और कथन-II कथन-I की सही व्याख्या है। विधेयक लोकसभा को 543 से 816 सीटों तक बढ़ाना और 2011 की जनगणना पर परिसीमन के साथ महिलाओं के लिए एक-तिहाई आरक्षण 2029 में लागू करना चाहता था। मत-विभाजन में 298 सदस्यों ने पक्ष में और 230 ने विरोध में मत दिया: सदन की कुल सदस्यता के आधे से अधिक, पर उन 352 मतों से कम -- उपस्थित और मत देने वाले 528 का दो-तिहाई -- जिनकी माँग अनुच्छेद 368(2) करता है, इसलिए विधेयक गिर गया। "
  "इसके बाद सरकार ने इसके साथ पेश परिसीमन विधेयक और संघ राज्यक्षेत्र विधि (संशोधन) विधेयक वापस ले लिए। 2023 का 106वाँ संशोधन, जिसके अंतर्गत महिला आरक्षण नई जनगणना के बाद पहले परिसीमन के उपरांत लागू होता है, अप्रभावित है।",
  "Lok Sabha debates (17 April 2026) on the Constitution (131st Amendment) Bill, 2026; Constitution of India, Article 368(2), and the Constitution (106th Amendment) Act, 2023.",
  "ca-t2-pol-131st-amendment-bill-defeated-special-majority", craft="application")

A(FD, "medium",
  "The law that in 2026 named Amaravati the capital of Andhra Pradesh was enacted by Parliament, not by the State Legislature.",
  "2026 में अमरावती को आंध्र प्रदेश की राजधानी घोषित करने वाला क़ानून राज्य विधानमंडल ने नहीं, संसद ने बनाया।",
  "The capital of each State is specified in the First Schedule to the Constitution.",
  "प्रत्येक राज्य की राजधानी संविधान की पहली अनुसूची में निर्दिष्ट है।",
  2,
  "Statement-I is correct but Statement-II is incorrect. The Andhra Pradesh Reorganisation Act, 2014, made by Parliament under Articles 3 and 4 when Telangana was carved out, made Hyderabad the common capital of both States for up to ten years and left the new capital of Andhra Pradesh to be settled; so it took an Act of Parliament -- the Andhra Pradesh Reorganisation (Amendment) Act, 2026, passed in April after a resolution of the State Assembly -- to write Amaravati into section 5 as the capital, with effect from 2 June 2024, when the ten years ended. It settled the State's earlier move towards three capitals. "
  "Statement-II is wrong: the First Schedule lists the States and Union territories and their territories, not their capitals; the Constitution names no State capital, which is usually fixed by the State government.",
  "कथन-I सही है, पर कथन-II ग़लत है। तेलंगाना के गठन के समय संसद द्वारा अनुच्छेद 3 और 4 के अंतर्गत बनाए गए आंध्र प्रदेश पुनर्गठन अधिनियम, 2014 ने हैदराबाद को अधिकतम दस वर्षों के लिए दोनों राज्यों की साझा राजधानी बनाया और आंध्र प्रदेश की नई राजधानी का प्रश्न बाद के लिए छोड़ा; इसलिए अमरावती को धारा 5 में राजधानी के रूप में लिखने के लिए संसद का अधिनियम -- राज्य विधानसभा के संकल्प के बाद अप्रैल में पारित आंध्र प्रदेश पुनर्गठन (संशोधन) अधिनियम, 2026 -- आवश्यक था, जो दस वर्ष पूरे होने की तिथि 2 जून 2024 से प्रभावी है। इसने राज्य के तीन राजधानियों की ओर पहले के क़दम का पटाक्षेप कर दिया। "
  "कथन-II ग़लत है: पहली अनुसूची राज्यों और संघ राज्यक्षेत्रों तथा उनके राज्यक्षेत्रों की सूची देती है, उनकी राजधानियों की नहीं; संविधान किसी राज्य की राजधानी का नाम नहीं देता, जो प्रायः राज्य सरकार तय करती है।",
  "Andhra Pradesh Reorganisation Act, 2014, section 5, and the Andhra Pradesh Reorganisation (Amendment) Act, 2026; Constitution of India, Articles 3 and 4 and the First Schedule.",
  "ca-t2-pol-amaravati-capital-parliament-first-schedule-si", craft="inference")

S(FR, "hard", "On 21 May 2026 the Supreme Court clarified how pending cases under Section 124A of the Indian Penal Code (sedition) may proceed. Consider the following statements:",
  "21 मई 2026 को सर्वोच्च न्यायालय ने स्पष्ट किया कि भारतीय दंड संहिता की धारा 124ए (राजद्रोह) के अंतर्गत लंबित मामले कैसे आगे बढ़ सकते हैं। निम्नलिखित कथनों पर विचार कीजिए:",
  ["In 1962 the Supreme Court upheld Section 124A but confined it to words or acts that tend to incite violence or public disorder.",
   "The 2026 order allows trials and appeals under Section 124A to proceed where the accused does not object.",
   "By the 2026 order the Court decided the challenge to the validity of Section 124A and upheld the section afresh."],
  ["1962 में सर्वोच्च न्यायालय ने धारा 124ए को वैध ठहराया पर उसे हिंसा या लोक अव्यवस्था भड़काने की प्रवृत्ति वाले शब्दों या कृत्यों तक सीमित कर दिया।",
   "2026 का आदेश धारा 124ए के अंतर्गत विचारण और अपीलों को वहाँ आगे बढ़ने देता है जहाँ अभियुक्त को आपत्ति न हो।",
   "2026 के आदेश द्वारा न्यायालय ने धारा 124ए की वैधता की चुनौती का निर्णय कर धारा को नए सिरे से वैध ठहराया।"],
  C3, 1,
  "Statements 1 and 2 are correct. In Kedar Nath Singh v. State of Bihar (1962) a Constitution Bench upheld the section only by reading it down to speech that incites violence or tends to create public disorder. In May 2022, in S.G. Vombatkere, the Court put the section in abeyance and stayed pending proceedings while its validity was re-examined; the order of 21 May 2026, in Kamran v. State of Madhya Pradesh, clarified that courts may go on with trials or appeals where the accused has no objection. "
  "Statement 3 is wrong: the 2026 order expressly said nothing on the merits; the challenge to the section under Articles 14, 19 and 21 is still pending. The question matters for cases begun before 1 July 2024, since Section 124A still governs offences committed before the Bharatiya Nyaya Sanhita replaced the Indian Penal Code; section 152 of the new code punishes acts endangering the sovereignty, unity and integrity of India.",
  "कथन 1 और 2 सही हैं। केदारनाथ सिंह बनाम बिहार राज्य (1962) में एक संविधान पीठ ने धारा को केवल हिंसा भड़काने वाली या लोक अव्यवस्था पैदा करने की प्रवृत्ति वाली वाणी तक सीमित पढ़कर वैध ठहराया। मई 2022 में एस.जी. वोम्बटकेरे मामले में न्यायालय ने धारा की वैधता की पुनर्परीक्षा तक उसे स्थगित रखा और लंबित कार्यवाहियाँ रोक दीं; 21 मई 2026 के आदेश ने, कामरान बनाम मध्य प्रदेश राज्य में, स्पष्ट किया कि जहाँ अभियुक्त को आपत्ति न हो वहाँ न्यायालय विचारण या अपीलें आगे बढ़ा सकते हैं। "
  "कथन 3 ग़लत है: 2026 के आदेश ने स्पष्ट रूप से गुण-दोष पर कुछ नहीं कहा; अनुच्छेद 14, 19 और 21 के आधार पर धारा की चुनौती अब भी लंबित है। यह प्रश्न 1 जुलाई 2024 से पहले शुरू हुए मामलों के लिए महत्त्वपूर्ण है, क्योंकि भारतीय न्याय संहिता द्वारा भारतीय दंड संहिता का स्थान लेने से पहले किए गए अपराधों पर धारा 124ए अब भी लागू होती है; नई संहिता की धारा 152 भारत की संप्रभुता, एकता और अखंडता को ख़तरे में डालने वाले कृत्यों को दंडित करती है।",
  "Supreme Court of India, Kedar Nath Singh v. State of Bihar (1962), S.G. Vombatkere v. Union of India (order of 11 May 2022) and Kamran v. State of Madhya Pradesh (order of 21 May 2026).",
  "ca-t2-pol-sedition-kedar-nath-2026-clarification-pending", craft="multi")

S(SL, "medium", "On 22 June 2026 the Ministry of Home Affairs notified the Foreign Contribution (Regulation) Amendment Rules, 2026. Consider the following statements:",
  "22 जून 2026 को गृह मंत्रालय ने विदेशी अंशदान (विनियमन) संशोधन नियम, 2026 अधिसूचित किए। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Rules bar the use of foreign contribution for religious conversion.",
   "Organisations seeking registration must now specify their activities from a prescribed list.",
   "The Foreign Contribution (Regulation) Amendment Bill, 2026 had been enacted by Parliament before the Rules were notified."],
  ["ये नियम धर्मांतरण के लिए विदेशी अंशदान के उपयोग पर रोक लगाते हैं।",
   "पंजीकरण चाहने वाले संगठनों को अब एक निर्धारित सूची से अपनी गतिविधियाँ बतानी होंगी।",
   "नियमों की अधिसूचना से पहले विदेशी अंशदान (विनियमन) संशोधन विधेयक, 2026 संसद द्वारा अधिनियमित हो चुका था।"],
  C3, 1,
  "Statements 1 and 2 are correct. The Rules, amending the Foreign Contribution (Regulation) Rules, 2011 made under the Act of 2010, allow foreign funds for worship, religious education, heritage and community kitchens but not for proselytisation, and require each organisation to choose its activities from a list of 105 in five categories; existing registrants have a year to file afresh. The Supreme Court had held in 2022 that receiving foreign contributions is not a fundamental right and upheld the curbs added in 2020. "
  "Statement 3 is wrong: the Amendment Bill, introduced in the Lok Sabha in March 2026 to let a designated authority take control of assets created with foreign funds, was still pending; the Rules were made under the existing Act.",
  "कथन 1 और 2 सही हैं। 2010 के अधिनियम के अंतर्गत बने विदेशी अंशदान (विनियमन) नियम, 2011 में संशोधन करने वाले ये नियम विदेशी धन को उपासना, धार्मिक शिक्षा, धरोहर और सामुदायिक रसोई के लिए अनुमत करते हैं पर धर्म-प्रचार द्वारा धर्मांतरण के लिए नहीं, और हर संगठन से पाँच श्रेणियों की 105 गतिविधियों की सूची से अपनी गतिविधियाँ चुनने को कहते हैं; पहले से पंजीकृत संगठनों को नए सिरे से आवेदन के लिए एक वर्ष मिला है। सर्वोच्च न्यायालय ने 2022 में कहा था कि विदेशी अंशदान पाना मौलिक अधिकार नहीं है और 2020 में जोड़े गए प्रतिबंधों को वैध ठहराया था। "
  "कथन 3 ग़लत है: मार्च 2026 में लोकसभा में पेश संशोधन विधेयक, जो एक नामित प्राधिकारी को विदेशी धन से बनी संपत्तियों का नियंत्रण लेने देता, अभी लंबित था; नियम मौजूदा अधिनियम के अंतर्गत बनाए गए।",
  "Ministry of Home Affairs, Foreign Contribution (Regulation) Amendment Rules, 2026, S.O. 3272(E) (22 June 2026); Foreign Contribution (Regulation) Amendment Bill, 2026 (Lok Sabha, March 2026); Supreme Court of India, Noel Harper v. Union of India (2022).",
  "ca-t2-pol-fcra-rules-2026-conversion-activity-list", craft="precision")

S(JV, "hard", "In June 2026 a case of alleged misappropriation of temple funds at Ayodhya drew attention to the idea of a deity as a 'juristic person'. Consider the following statements:",
  "जून 2026 में अयोध्या में मंदिर निधि के कथित दुरुपयोग के एक मामले ने देवता के ‘विधिक व्यक्ति’ होने की अवधारणा की ओर ध्यान खींचा। निम्नलिखित कथनों पर विचार कीजिए:",
  ["Indian courts have long treated a consecrated Hindu idol as a juristic person able to own property.",
   "In the Ayodhya judgment of 2019 the Supreme Court treated Ram Lalla Virajman as a juristic person but did not give that status to the birthplace itself.",
   "The Supreme Court has held the Guru Granth Sahib to be a juristic person."],
  ["भारतीय न्यायालय लंबे समय से प्रतिष्ठित हिंदू मूर्ति को संपत्ति रखने में सक्षम विधिक व्यक्ति मानते आए हैं।",
   "2019 के अयोध्या निर्णय में सर्वोच्च न्यायालय ने रामलला विराजमान को विधिक व्यक्ति माना पर जन्मस्थान को स्वयं यह दर्जा नहीं दिया।",
   "सर्वोच्च न्यायालय ने गुरु ग्रंथ साहिब को विधिक व्यक्ति माना है।"],
  C3, 2,
  "All three statements are correct. A juristic person is an entity the law treats as able to hold rights and duties, though it is not a human being -- a company or a trust, for instance. Since the colonial period courts have held that an idol consecrated for worship is a juristic person whose property is managed by a shebait or trustee on its behalf, which is why temple assets belong in law to the deity. "
  "In M. Siddiq v. Mahant Suresh Das (2019) the Court accepted the deity Ram Lalla Virajman as a juristic person but declined to treat the land, the Ram Janmasthan, as one, since that would make land immune from claims of title. In Shiromani Gurdwara Prabandhak Committee v. Som Nath Dass (2000) it held the Guru Granth Sahib to be a juristic person, able to hold property of a gurdwara.",
  "तीनों कथन सही हैं। विधिक व्यक्ति ऐसी इकाई है जिसे विधि अधिकार और कर्तव्य रखने में सक्षम मानती है, यद्यपि वह मनुष्य नहीं है -- जैसे कोई कंपनी या न्यास। औपनिवेशिक काल से न्यायालयों ने माना है कि पूजा के लिए प्रतिष्ठित मूर्ति एक विधिक व्यक्ति है, जिसकी संपत्ति का प्रबंध उसकी ओर से सेवायत या न्यासी करता है, इसीलिए मंदिर की संपत्ति विधि में देवता की होती है। "
  "एम. सिद्दीक बनाम महंत सुरेश दास (2019) में न्यायालय ने देवता रामलला विराजमान को विधिक व्यक्ति स्वीकार किया पर भूमि, रामजन्मस्थान, को ऐसा मानने से इनकार किया, क्योंकि इससे भूमि स्वामित्व के दावों से परे हो जाती। शिरोमणि गुरुद्वारा प्रबंधक कमेटी बनाम सोम नाथ दास (2000) में इसने गुरु ग्रंथ साहिब को गुरुद्वारे की संपत्ति रखने में सक्षम विधिक व्यक्ति माना।",
  "Supreme Court of India, M. Siddiq (D) through LRs v. Mahant Suresh Das (2019) and Shiromani Gurdwara Prabandhak Committee v. Som Nath Dass (2000).",
  "ca-t2-pol-juristic-person-deity-ram-lalla-guru-granth", craft="linkage")

S(JV, "medium", "On 3 June 2026 a committee of the Supreme Court released draft Regulations for Use of Artificial Intelligence in Courts. Consider the following statements:",
  "3 जून 2026 को सर्वोच्च न्यायालय की एक समिति ने न्यायालयों में कृत्रिम बुद्धिमत्ता के उपयोग के विनियमों का प्रारूप जारी किया। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The draft allows AI to decide the outcome of minor cases, subject to review by a judge.",
   "It bars the use of AI even for legal research and the translation of judgments.",
   "The draft was issued by the Ministry of Electronics and Information Technology under the Information Technology Act, 2000."],
  ["प्रारूप न्यायाधीश की समीक्षा के अधीन छोटे मामलों का परिणाम तय करने के लिए एआई के उपयोग की अनुमति देता है।",
   "यह विधिक शोध और निर्णयों के अनुवाद के लिए भी एआई के उपयोग पर रोक लगाता है।",
   "प्रारूप इलेक्ट्रॉनिकी और सूचना प्रौद्योगिकी मंत्रालय ने सूचना प्रौद्योगिकी अधिनियम, 2000 के अंतर्गत जारी किया।"],
  C3, 3,
  "None of the statements is correct; the first two reverse what the draft says. The draft, released for comment by the Supreme Court's committee on AI, rests on human primacy: in absolute terms it bars AI from determining outcomes, producing risk scores, predicting bail, judging the credibility of witnesses or profiling them, and bars undisclosed or unexplainable systems in matters touching personal liberty. It permits assistive and administrative uses -- research, translation of judgments, transcription, summaries, case-flow management -- under an apex body at the Supreme Court, with litigants told when AI is used in a material way. "
  "Statement 3 is wrong: the draft comes from the judiciary itself, as part of the Supreme Court's control over the practice and procedure of the courts; it is not a rule made by the Union ministry under the IT Act.",
  "कोई भी कथन सही नहीं है; पहले दो कथन प्रारूप की बात को उलट देते हैं। सर्वोच्च न्यायालय की एआई समिति द्वारा टिप्पणी के लिए जारी प्रारूप मनुष्य की प्रधानता पर टिका है: यह पूर्ण रूप से एआई को परिणाम तय करने, जोखिम-अंक बनाने, ज़मानत का अनुमान लगाने, गवाहों की विश्वसनीयता आँकने या उनकी प्रोफ़ाइलिंग करने से रोकता है, और व्यक्तिगत स्वतंत्रता से जुड़े मामलों में अप्रकट या अव्याख्येय प्रणालियों पर रोक लगाता है। यह सहायक और प्रशासनिक उपयोग -- शोध, निर्णयों का अनुवाद, प्रतिलेखन, सारांश, मामलों का प्रवाह-प्रबंधन -- सर्वोच्च न्यायालय में एक शीर्ष निकाय के अधीन अनुमत करता है, और महत्त्वपूर्ण रूप से एआई के उपयोग पर वादकारियों को सूचित करना होगा। "
  "कथन 3 ग़लत है: प्रारूप स्वयं न्यायपालिका से आया है, न्यायालयों की प्रथा और प्रक्रिया पर सर्वोच्च न्यायालय के नियंत्रण के अंग के रूप में; यह आईटी अधिनियम के अंतर्गत केंद्रीय मंत्रालय द्वारा बनाया गया नियम नहीं है।",
  "Supreme Court of India, draft Regulations for Use of Artificial Intelligence in Courts, 2026 (3 June 2026).",
  "ca-t2-pol-sc-draft-ai-regulations-courts", craft="precision")

S(GV, "medium", "On 21 April 2026 the Supreme Court asked a high-powered committee to draw up an action plan for the rights of prisoners with disabilities. Consider the following statements:",
  "21 अप्रैल 2026 को सर्वोच्च न्यायालय ने एक उच्चाधिकार समिति से दिव्यांग क़ैदियों के अधिकारों के लिए कार्ययोजना बनाने को कहा। निम्नलिखित कथनों पर विचार कीजिए:",
  ["'Prisons' is a subject in the Concurrent List of the Seventh Schedule.",
   "The Model Prisons and Correctional Services Act, 2023, prepared by the Ministry of Home Affairs, is meant to replace the colonial Prisons Act, 1894 in the States.",
   "The Model Act was passed by Parliament and binds all the States directly."],
  ["‘कारागार’ सातवीं अनुसूची की समवर्ती सूची का विषय है।",
   "गृह मंत्रालय द्वारा तैयार आदर्श कारागार और सुधारात्मक सेवाएँ अधिनियम, 2023 राज्यों में औपनिवेशिक कारागार अधिनियम, 1894 का स्थान लेने के लिए है।",
   "आदर्श अधिनियम संसद ने पारित किया है और यह सभी राज्यों पर सीधे बाध्यकारी है।"],
  C3, 0,
  "Only statement 2 is correct. Statement 1 is wrong: prisons and the persons detained in them are Entry 4 of the State List -- only the removal of prisoners from one State to another is in the Concurrent List -- so prison administration and law belong to the States, with the Centre offering guidance and funds. In 2023 the Ministry of Home Affairs prepared the Model Prisons and Correctional Services Act as a template for States to replace the Prisons Act, 1894 and related colonial laws, with provisions on reform, open and semi-open prisons, technology and separate facilities for vulnerable prisoners. "
  "Statement 3 is wrong: the Model Act is a guidance document, not a law of Parliament; it takes effect only where a State enacts it. The Court's order, in a petition that cited the cases of G.N. Saibaba and Stan Swamy, entrusted the committee chaired by a former Supreme Court judge, S. Ravindra Bhat, with a plan under the Rights of Persons with Disabilities Act, 2016.",
  "केवल कथन 2 सही है। कथन 1 ग़लत है: कारागार और उनमें निरुद्ध व्यक्ति राज्य सूची की प्रविष्टि 4 हैं -- समवर्ती सूची में केवल क़ैदियों को एक राज्य से दूसरे राज्य ले जाना है -- इसलिए कारागार प्रशासन और विधि राज्यों के विषय हैं, जबकि केंद्र मार्गदर्शन और धन देता है। 2023 में गृह मंत्रालय ने कारागार अधिनियम, 1894 और संबंधित औपनिवेशिक क़ानूनों का स्थान लेने के लिए राज्यों के आदर्श के रूप में आदर्श कारागार और सुधारात्मक सेवाएँ अधिनियम तैयार किया, जिसमें सुधार, खुली और अर्ध-खुली जेलों, प्रौद्योगिकी और संवेदनशील क़ैदियों के लिए अलग सुविधाओं के प्रावधान हैं। "
  "कथन 3 ग़लत है: आदर्श अधिनियम एक मार्गदर्शक दस्तावेज़ है, संसद का क़ानून नहीं; यह वहीं प्रभावी होता है जहाँ कोई राज्य इसे अधिनियमित करे। जी.एन. साईबाबा और स्टैन स्वामी के मामलों का उल्लेख करने वाली याचिका पर न्यायालय के आदेश ने सर्वोच्च न्यायालय के पूर्व न्यायाधीश एस. रवींद्र भट की अध्यक्षता वाली समिति को दिव्यांगजन अधिकार अधिनियम, 2016 के अंतर्गत योजना बनाने का कार्य सौंपा।",
  "Constitution of India, Seventh Schedule, List II, Entry 4; Ministry of Home Affairs, Model Prisons and Correctional Services Act, 2023; Supreme Court of India, Sathyan Naravoor v. Union of India (21 April 2026).",
  "ca-t2-pol-prisons-state-list-model-act-2023", craft="linkage")

S(GV, "easy", "On 24 June 2026 the Ministry of External Affairs said that a passport is a travel document, not proof of citizenship. Consider the following statements:",
  "24 जून 2026 को विदेश मंत्रालय ने कहा कि पासपोर्ट यात्रा दस्तावेज़ है, नागरिकता का प्रमाण नहीं। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Passports Act, 1967 allows the Central Government to issue a passport to a person who is not a citizen of India.",
   "The deletion of a person's name from the electoral roll in a revision amounts to a loss of Indian citizenship."],
  ["पासपोर्ट अधिनियम, 1967 केंद्र सरकार को किसी ऐसे व्यक्ति को पासपोर्ट जारी करने देता है जो भारत का नागरिक नहीं है।",
   "पुनरीक्षण में मतदाता सूची से किसी व्यक्ति का नाम हटना भारतीय नागरिकता खोने के समान है।"],
  T2, 0,
  "Only statement 1 is correct. Section 20 of the Passports Act lets the government issue a passport or travel document to a non-citizen in the public interest, so holding a passport does not by itself settle citizenship, which is governed by the Citizenship Act, 1955 -- by birth, descent, registration or naturalisation -- and is decided, where disputed, by the Union. "
  "Statement 2 is wrong: in upholding the Election Commission's special intensive revision of electoral rolls in May 2026, the Supreme Court held that deletion from the roll does not strip anyone of citizenship; doubtful cases go to the Ministry of Home Affairs for decision under the Citizenship Act.",
  "केवल कथन 1 सही है। पासपोर्ट अधिनियम की धारा 20 सरकार को लोकहित में किसी गैर-नागरिक को पासपोर्ट या यात्रा दस्तावेज़ जारी करने देती है, इसलिए पासपोर्ट होने मात्र से नागरिकता तय नहीं होती, जो नागरिकता अधिनियम, 1955 से -- जन्म, वंश, पंजीकरण या देशीयकरण द्वारा -- शासित होती है और विवाद होने पर संघ द्वारा तय की जाती है। "
  "कथन 2 ग़लत है: मई 2026 में निर्वाचन आयोग के मतदाता सूचियों के विशेष गहन पुनरीक्षण को वैध ठहराते हुए सर्वोच्च न्यायालय ने कहा कि सूची से नाम हटने से किसी की नागरिकता नहीं छिनती; संदिग्ध मामले नागरिकता अधिनियम के अंतर्गत निर्णय के लिए गृह मंत्रालय को जाते हैं।",
  "Passports Act, 1967, section 20; Citizenship Act, 1955; Ministry of External Affairs, statement of 24 June 2026; Supreme Court of India, judgment on the special intensive revision of electoral rolls (May 2026).",
  "ca-t2-pol-passport-not-citizenship-section-20", craft="precision")

S(JV, "medium", "In June 2026 senior advocate V. Mohana became a judge of the Supreme Court, elevated directly from the Bar. Consider the following statements:",
  "जून 2026 में वरिष्ठ अधिवक्ता वी. मोहना सीधे बार से पदोन्नत होकर सर्वोच्च न्यायालय की न्यायाधीश बनीं। निम्नलिखित कथनों पर विचार कीजिए:",
  ["A person who has been an advocate of a High Court for at least seven years is eligible to be appointed a judge of the Supreme Court.",
   "She is only the second woman to be appointed to the Supreme Court directly from the Bar.",
   "A distinguished jurist can be appointed to the Supreme Court only on the recommendation of the Bar Council of India."],
  ["जो व्यक्ति कम से कम सात वर्ष तक किसी उच्च न्यायालय का अधिवक्ता रहा हो, वह सर्वोच्च न्यायालय का न्यायाधीश नियुक्त होने के योग्य है।",
   "वे सीधे बार से सर्वोच्च न्यायालय में नियुक्त होने वाली केवल दूसरी महिला हैं।",
   "किसी प्रतिष्ठित विधिवेत्ता को केवल भारतीय विधिज्ञ परिषद की सिफ़ारिश पर ही सर्वोच्च न्यायालय में नियुक्त किया जा सकता है।"],
  C3, 0,
  "Only statement 2 is correct. Statement 1 is wrong: Article 124(3) makes a citizen of India eligible if he or she has been a High Court judge for five years, or an advocate of a High Court for ten years, or is, in the opinion of the President, a distinguished jurist; seven years' practice is the qualification for a district judge under Article 233. Recommended by the collegium in May 2026 along with four High Court Chief Justices, Justice Mohana follows Justice Indu Malhotra, appointed from the Bar in 2018, and is the first woman appointed to the Court since 2021. "
  "Statement 3 is wrong: the 'distinguished jurist' route depends on the opinion of the President, acting on the usual advice, and the Bar Council has no role in it; no one has yet been appointed by that route.",
  "केवल कथन 2 सही है। कथन 1 ग़लत है: अनुच्छेद 124(3) भारत के उस नागरिक को योग्य बनाता है जो पाँच वर्ष उच्च न्यायालय का न्यायाधीश रहा हो, या दस वर्ष उच्च न्यायालय का अधिवक्ता रहा हो, या राष्ट्रपति की राय में प्रतिष्ठित विधिवेत्ता हो; सात वर्ष की वकालत अनुच्छेद 233 के अंतर्गत ज़िला न्यायाधीश की योग्यता है। मई 2026 में चार उच्च न्यायालयों के मुख्य न्यायाधीशों के साथ कॉलेजियम द्वारा अनुशंसित न्यायमूर्ति मोहना 2018 में बार से नियुक्त न्यायमूर्ति इंदु मल्होत्रा के बाद आती हैं, और 2021 के बाद न्यायालय में नियुक्त होने वाली पहली महिला हैं। "
  "कथन 3 ग़लत है: ‘प्रतिष्ठित विधिवेत्ता’ का मार्ग सामान्य परामर्श पर कार्य करने वाले राष्ट्रपति की राय पर निर्भर है, और विधिज्ञ परिषद की इसमें कोई भूमिका नहीं है; इस मार्ग से अब तक किसी की नियुक्ति नहीं हुई है।",
  "Constitution of India, Article 124(3); Supreme Court of India, collegium resolutions of May 2026; Department of Justice, notification of appointment (June 2026).",
  "ca-t2-pol-mohana-direct-from-bar-art-124-3", craft="precision")

S(JV, "medium", "From 7 April 2026 a nine-judge bench of the Supreme Court heard the reference arising from the Sabarimala case. Consider the following statements:",
  "7 अप्रैल 2026 से सर्वोच्च न्यायालय की नौ न्यायाधीशों की पीठ ने सबरीमला मामले से उत्पन्न संदर्भ की सुनवाई की। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The questions referred include the 'essential religious practices' test and the interplay of Articles 25 and 26 with Article 14.",
   "One question is whether a person who does not belong to a religious denomination can challenge its practice through a public interest litigation.",
   "A nine-judge bench is the largest bench the Supreme Court has ever constituted."],
  ["संदर्भित प्रश्नों में ‘अनिवार्य धार्मिक प्रथाएँ’ कसौटी और अनुच्छेद 14 के साथ अनुच्छेद 25 और 26 का संबंध शामिल है।",
   "एक प्रश्न यह है कि क्या किसी धार्मिक संप्रदाय से न जुड़ा व्यक्ति जनहित याचिका के माध्यम से उसकी प्रथा को चुनौती दे सकता है।",
   "नौ न्यायाधीशों की पीठ सर्वोच्च न्यायालय द्वारा अब तक गठित सबसे बड़ी पीठ है।"],
  C3, 1,
  "Statements 1 and 2 are correct. Hearing review petitions against the 2018 judgment that opened the Sabarimala temple to women of all ages, the Court in November 2019 referred wider questions to a larger bench, framed in 2020: the scope of religious freedom, the interplay of Articles 25 and 26 with each other and with Article 14, whether denominations' practices may be tested by courts for being 'essential', the meaning of 'sections of Hindus' in Article 25(2)(b), and whether outsiders may bring public interest petitions against a faith's practices. The answers will bear on cases about women's entry into mosques, female genital cutting among the Dawoodi Bohras and Parsi women married outside the faith. "
  "Statement 3 is wrong: the largest bench so far was the thirteen-judge bench of Kesavananda Bharati (1973), which laid down the basic structure doctrine.",
  "कथन 1 और 2 सही हैं। सबरीमला मंदिर को सभी आयु की महिलाओं के लिए खोलने वाले 2018 के निर्णय के विरुद्ध पुनर्विचार याचिकाओं की सुनवाई करते हुए न्यायालय ने नवंबर 2019 में व्यापक प्रश्न एक बड़ी पीठ को सौंपे, जो 2020 में तय हुए: धार्मिक स्वतंत्रता का दायरा, अनुच्छेद 25 और 26 का परस्पर तथा अनुच्छेद 14 के साथ संबंध, क्या न्यायालय संप्रदायों की प्रथाओं को ‘अनिवार्य’ होने की कसौटी पर परख सकते हैं, अनुच्छेद 25(2)(ख) में ‘हिंदुओं के वर्गों’ का अर्थ, और क्या बाहरी व्यक्ति किसी आस्था की प्रथाओं के विरुद्ध जनहित याचिका ला सकते हैं। इनके उत्तर मस्जिदों में महिलाओं के प्रवेश, दाऊदी बोहराओं में स्त्री ख़तना और धर्म से बाहर विवाह करने वाली पारसी महिलाओं से जुड़े मामलों पर असर डालेंगे। "
  "कथन 3 ग़लत है: अब तक की सबसे बड़ी पीठ केशवानंद भारती (1973) की तेरह न्यायाधीशों की पीठ थी, जिसने मूल ढाँचे का सिद्धांत दिया।",
  "Supreme Court of India, Kantaru Rajeevaru v. Indian Young Lawyers Association (reference orders of November 2019 and February 2020) and hearings of the nine-judge bench (April 2026); Kesavananda Bharati v. State of Kerala (1973).",
  "ca-t2-pol-sabarimala-nine-judge-reference-largest-bench", craft="linkage")

S(SL, "easy", "In May 2026 the Supreme Court held that survivors who were forced to swallow acid are covered by the term 'acid attack victim' in the Rights of Persons with Disabilities Act, 2016. Consider the following statements:",
  "मई 2026 में सर्वोच्च न्यायालय ने निर्णय दिया कि जिन्हें तेज़ाब पीने के लिए विवश किया गया, वे दिव्यांगजन अधिकार अधिनियम, 2016 में ‘तेज़ाब हमले के पीड़ित’ शब्द के अंतर्गत आते हैं। निम्नलिखित कथनों पर विचार कीजिए:",
  ["Before this ruling, the term had been read to cover mainly those disfigured by acid thrown on them.",
   "The 2016 Act was enacted to give effect to the United Nations Convention on the Rights of Persons with Disabilities."],
  ["इस निर्णय से पहले इस शब्द को मुख्यतः उन लोगों तक पढ़ा जाता था जो अपने ऊपर फेंके गए तेज़ाब से विरूपित हुए।",
   "2016 का अधिनियम विकलांग व्यक्तियों के अधिकारों पर संयुक्त राष्ट्र अभिसमय को प्रभावी करने के लिए बनाया गया था।"],
  T2, 2,
  "Both statements are correct. The Act defines an acid attack victim as a person disfigured by violent assaults involving acid or a similar corrosive substance, and in practice it had been applied to visible disfigurement from acid thrown on the body; the Court read it purposively to include survivors whose internal organs were damaged after being made to swallow acid, so that they too can claim the Act's benefits. "
  "The Act replaced the Persons with Disabilities Act, 1995 to bring Indian law in line with the UN Convention, which India ratified in 2007, moving from a welfare approach to one based on rights, equality and dignity.",
  "दोनों कथन सही हैं। अधिनियम तेज़ाब हमले के पीड़ित को तेज़ाब या वैसे ही संक्षारक पदार्थ से जुड़े हिंसक हमलों से विरूपित व्यक्ति के रूप में परिभाषित करता है, और व्यवहार में इसे शरीर पर फेंके गए तेज़ाब से हुई दृश्य विरूपता पर लागू किया जाता रहा था; न्यायालय ने इसे प्रयोजनपरक ढंग से पढ़कर उन पीड़ितों को भी शामिल किया जिनके आंतरिक अंग तेज़ाब पिलाए जाने से क्षतिग्रस्त हुए, ताकि वे भी अधिनियम के लाभ पा सकें। "
  "इस अधिनियम ने भारतीय विधि को संयुक्त राष्ट्र अभिसमय के अनुरूप लाने के लिए विकलांग व्यक्ति अधिनियम, 1995 का स्थान लिया, जिसे भारत ने 2007 में अनुसमर्थित किया था, और कल्याण के दृष्टिकोण से अधिकार, समानता और गरिमा पर आधारित दृष्टिकोण की ओर बढ़ा।",
  "Supreme Court of India, judgment on acid-ingestion survivors under the Rights of Persons with Disabilities Act (May 2026); Rights of Persons with Disabilities Act, 2016, Schedule; United Nations Convention on the Rights of Persons with Disabilities (2006).",
  "ca-t2-pol-rpwd-acid-ingestion-uncrpd", craft="precision")

finish("ca_t2_c.sql", FORMAT, "2026-Q2", update="--update" in sys.argv)
