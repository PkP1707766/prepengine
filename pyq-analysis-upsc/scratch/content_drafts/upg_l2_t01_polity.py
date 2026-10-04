# -*- coding: utf-8 -*-
"""Level 2 · Test 1 (Polity 1: Constitutional Framework & Rights) -- depth audit of 2026-10-04
(docs/upsc-question-design-standard.md §6).

All 104 rows in the test's two sub-topics were read and classified. Before: analytic 17, precision 48,
recall 39 (3 rows are Test 21's and were already tagged). That is 9 recall rows over the cap and 18 analytic
short, so 18 rows are rewritten in place (plus one precision row, below), keeping their concept ids, types and difficulties (the cells are
unchanged):
  - 9 recall rows become inference, linkage or application. Examples: why the Commonwealth could keep a
    republic; why Golaknath ruled only for the future; what else the 42nd Amendment did; where India departs
    from Westminster; Parts of the Constitution for real situations; the early linguistic-States debate; the
    Objectives Resolution's residuary powers; why the creamy layer is excluded; the basis of Vishaka.
  - 9 precision rows become cases. Examples: which bodies are 'the State' (BCCI is the trap); a Telugu school
    in Karnataka; where religious instruction is allowed; a citizen who takes Canadian citizenship; what a
    detainee can still enforce in an emergency; three Article 20 cases; a contractor and a child worker;
    police recruitment rules; what has widened the Article 19(2) grounds.
After: analytic 35, precision 39, recall 30. The other 83 rows keep their content and get their craft tag.
One planned conversion (which Schedules a new-State Act amends) was dropped: Test 1's own Berubari row
states the answer. The cue scan then caught three leaks into kept rows, all fixed here:
  - the 42nd-Amendment MCQ named the Preamble words and the Fundamental Duties in its stem, and had distractors
    that the 44th-Amendment and amendment-pairs rows answer;
  - the Vishaka MCQ had an option spelling out Article 42;
  - the Objectives Resolution's residuary-powers statement would answer the salient-features row, so that
    row's residuary statement is replaced by one on State constitutions."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write_updates, CODE
from polity_common import C3, C4, T2

d.SUBJECT = "Polity"
d.REQUIRE_CRAFT = True
CF = "Constitutional Framework"
FR = "Fundamental Rights, DPSP & Duties"
COI = "Constitution of India"
SC = "Supreme Court of India"
NC = "NCERT Class XI, Political Science -- Indian Constitution at Work"
GA = "Granville Austin, The Indian Constitution: Cornerstone of a Nation"
CAD = "Constituent Assembly Debates (Lok Sabha Secretariat)"
MATCHED = "How many of the above are correctly matched?"
MATCHED_HI = "उपर्युक्त में से कितने सही सुमेलित हैं?"

# ================================================================ CONSTITUTIONAL FRAMEWORK (7 rewritten)
M(CF, "hard", "In 1949 India decided to remain a member of the Commonwealth after it became a republic. Which one of the following made this possible without compromising India's sovereignty?",
  "1949 में भारत ने गणराज्य बनने के बाद भी राष्ट्रमंडल का सदस्य बने रहने का निर्णय लिया। निम्नलिखित में से किसने भारत की संप्रभुता से समझौता किए बिना इसे संभव बनाया?",
  ["The London Declaration, under which members accepted the British monarch only as the symbol of their free association and Head of the Commonwealth",
   "The Statute of Westminster, 1931, which had already opened Commonwealth membership to republics outside the British Crown",
   "A clause of the Indian Independence Act, 1947 under which India would keep the Governor-General as its formal head of State",
   "An agreement under which India accepted the British monarch as its own head of State, while keeping full control of its defence and foreign policy"],
  ["लंदन घोषणा, जिसके तहत सदस्यों ने ब्रिटिश सम्राट को केवल अपने स्वतंत्र संघ के प्रतीक और राष्ट्रमंडल के प्रमुख के रूप में स्वीकार किया",
   "वेस्टमिंस्टर संविधि, 1931, जिसने पहले ही ब्रिटिश ताज से बाहर के गणराज्यों के लिए राष्ट्रमंडल की सदस्यता खोल दी थी",
   "भारतीय स्वतंत्रता अधिनियम, 1947 का एक खंड, जिसके तहत भारत गवर्नर-जनरल को अपना औपचारिक राष्ट्राध्यक्ष बनाए रखता",
   "एक समझौता, जिसके तहत भारत ने ब्रिटिश सम्राट को अपना राष्ट्राध्यक्ष माना, पर रक्षा और विदेश नीति पर पूरा नियंत्रण अपने पास रखा"],
  0,
  "Until 1949 Commonwealth membership meant owing allegiance to the Crown, which a republic could not do. The London Declaration of April 1949 solved this: members would accept the British monarch only as the symbol of their free association and as Head of the Commonwealth, with no allegiance and no role in their governments. "
  "India could thus have its own elected head of State and remain a member voluntarily. The Constituent Assembly ratified the decision in May 1949. The Statute of Westminster (1931) had given the dominions legislative independence, but they still owed allegiance to the Crown. The last option describes the very arrangement that a republic had to avoid.",
  "1949 तक राष्ट्रमंडल की सदस्यता का अर्थ था ब्रिटिश ताज के प्रति निष्ठा, जो कोई गणराज्य नहीं रख सकता था। अप्रैल 1949 की लंदन घोषणा ने इसका हल निकाला: सदस्य ब्रिटिश सम्राट को केवल अपने स्वतंत्र संघ के प्रतीक और राष्ट्रमंडल के प्रमुख के रूप में मानेंगे, बिना निष्ठा के और उनकी सरकारों में बिना किसी भूमिका के। "
  "इस तरह भारत अपना निर्वाचित राष्ट्राध्यक्ष रखते हुए स्वेच्छा से सदस्य बना रह सका; संविधान सभा ने मई 1949 में इस निर्णय की पुष्टि की। वेस्टमिंस्टर संविधि (1931) ने डोमिनियनों को विधायी स्वतंत्रता दी थी, पर वे तब भी ताज के प्रति निष्ठावान थे। अंतिम विकल्प ठीक वही व्यवस्था बताता है जिससे किसी गणराज्य को बचना था।",
  f"{CAD} -- ratification of the Commonwealth decision, May 1949; {GA}.",
  "polity-commonwealth-ratification-1949", craft="inference")

M(CF, "hard", "In I.C. Golaknath v. State of Punjab (1967), the Supreme Court held that Parliament could not abridge Fundamental Rights, yet it applied the doctrine of 'prospective overruling'. Which one of the following best explains why?",
  "आई.सी. गोलकनाथ बनाम पंजाब राज्य (1967) में सर्वोच्च न्यायालय ने कहा कि संसद मौलिक अधिकारों को कम नहीं कर सकती, फिर भी उसने 'भावी प्रभाव से निरसन' (prospective overruling) का सिद्धांत लागू किया। निम्नलिखित में से कौन-सा इसका सबसे सही कारण है?",
  ["Applying it to the past would have voided earlier amendments and the land reforms resting on them, so it bound only future amendments",
   "The Court wished to give Parliament time to pass a new amendment that would restore its power to amend Fundamental Rights",
   "The doctrine let the Court strike down the First, Fourth and Seventeenth Amendments while keeping the laws made under them",
   "The Court was bound by Article 141 to follow the earlier Shankari Prasad and Sajjan Singh rulings for all past cases, whatever its own view"],
  ["इसे अतीत पर लागू करने से पहले के संशोधन और उन पर टिके भूमि सुधार शून्य हो जाते, इसलिए यह केवल भविष्य के संशोधनों पर लागू हुआ",
   "न्यायालय संसद को एक नया संशोधन पारित करने का समय देना चाहता था, जिससे मौलिक अधिकारों में संशोधन की उसकी शक्ति लौट आए",
   "इस सिद्धांत से न्यायालय पहला, चौथा और सत्रहवाँ संशोधन रद्द कर सका, जबकि उनके तहत बने क़ानून बने रहे",
   "अनुच्छेद 141 के कारण न्यायालय अपने मत के बावजूद सभी पुराने मामलों में शंकरी प्रसाद और सज्जन सिंह के निर्णयों से बँधा था"],
  0,
  "By then the First, Fourth and Seventeenth Amendments had already validated a mass of land-reform laws. Declaring them void would have unsettled agrarian reform across the country, so Chief Justice Subba Rao, borrowing the American doctrine, made the ruling operate only for the future: past amendments stood, and future ones could not abridge Fundamental Rights. "
  "The Court did not strike those amendments down, and it was not seeking to invite a new amendment, though Parliament responded with the 24th. Article 141 binds the courts below the Supreme Court, not the Supreme Court itself, which is why Golaknath could depart from Shankari Prasad and Sajjan Singh.",
  "तब तक पहला, चौथा और सत्रहवाँ संशोधन ढेरों भूमि-सुधार क़ानूनों को वैध बना चुके थे। उन्हें शून्य घोषित करने से पूरे देश में कृषि सुधार डगमगा जाते, इसलिए मुख्य न्यायाधीश सुब्बा राव ने अमेरिकी सिद्धांत अपनाकर निर्णय को केवल भविष्य पर लागू किया: पुराने संशोधन बने रहे, पर आगे के संशोधन मौलिक अधिकारों को कम नहीं कर सकते थे। "
  "न्यायालय ने वे संशोधन रद्द नहीं किए, और वह किसी नए संशोधन को आमंत्रित भी नहीं कर रहा था, यद्यपि संसद ने 24वें संशोधन से जवाब दिया। अनुच्छेद 141 सर्वोच्च न्यायालय के नीचे के न्यायालयों को बाँधता है, स्वयं सर्वोच्च न्यायालय को नहीं; इसीलिए गोलकनाथ मामला शंकरी प्रसाद और सज्जन सिंह से अलग जा सका।",
  f"{SC} -- I.C. Golaknath v. State of Punjab (1967); {GA}.",
  "polity-prospective-overruling-golaknath", craft="inference")

M(CF, "medium", "One Constitution Amendment Act, passed during the Emergency on the lines recommended by the Swaran Singh Committee, moved five subjects -- among them education and forests -- from the State List to the Concurrent List. Which one of the following was also done by the same Act?",
  "आपातकाल के दौरान स्वर्ण सिंह समिति की सिफ़ारिशों की दिशा में पारित एक संविधान संशोधन अधिनियम ने शिक्षा और वन सहित पाँच विषय राज्य सूची से समवर्ती सूची में डाले। उसी अधिनियम ने निम्नलिखित में से और क्या किया?",
  ["It extended the protection of Article 31C to laws giving effect to any of the Directive Principles",
   "It created the National Judicial Appointments Commission to appoint judges",
   "It gave constitutional status to the National Commission for Backward Classes",
   "It made free and compulsory education for all children from six to fourteen years of age a Fundamental Right"],
  ["इसने अनुच्छेद 31C का संरक्षण किसी भी नीति-निदेशक तत्व को लागू करने वाले क़ानूनों तक बढ़ाया",
   "इसने न्यायाधीशों की नियुक्ति के लिए राष्ट्रीय न्यायिक नियुक्ति आयोग बनाया",
   "इसने राष्ट्रीय पिछड़ा वर्ग आयोग को संवैधानिक दर्जा दिया",
   "इसने छह से चौदह वर्ष के सभी बच्चों के लिए निःशुल्क और अनिवार्य शिक्षा को मौलिक अधिकार बनाया"],
  0,
  "The Act is the 42nd Amendment (1976), called the 'mini-Constitution' for the sheer number of its changes; it also amended the Preamble and added the Fundamental Duties. Among its changes, it widened Article 31C, which had shielded laws under Article 39(b) and (c), to cover laws giving effect to any Directive Principle against challenge under Articles 14 and 19. "
  "In Minerva Mills (1980) the Supreme Court struck down that extension. The other options belong to other amendments: the 99th (2014) created the National Judicial Appointments Commission, which the Supreme Court struck down in 2015; the 102nd (2018) gave the National Commission for Backward Classes constitutional status under Article 338B; and the 86th (2002) inserted Article 21A.",
  "यह अधिनियम 42वाँ संशोधन (1976) है, जो अपने बदलावों की भारी संख्या के कारण 'लघु संविधान' कहलाया; इसने प्रस्तावना में भी संशोधन किया और मौलिक कर्तव्य जोड़े। अपने बदलावों में इसने अनुच्छेद 31C का दायरा बढ़ाया: जो संरक्षण पहले अनुच्छेद 39(ख) और (ग) के क़ानूनों को मिलता था, वह अब किसी भी नीति-निदेशक तत्व को लागू करने वाले क़ानूनों को अनुच्छेद 14 और 19 की चुनौती से मिलने लगा। "
  "मिनर्वा मिल्स (1980) में सर्वोच्च न्यायालय ने यह विस्तार रद्द कर दिया। बाक़ी विकल्प अन्य संशोधनों के हैं: 99वें (2014) ने राष्ट्रीय न्यायिक नियुक्ति आयोग बनाया, जिसे सर्वोच्च न्यायालय ने 2015 में रद्द कर दिया; 102वें (2018) ने अनुच्छेद 338B के तहत राष्ट्रीय पिछड़ा वर्ग आयोग को संवैधानिक दर्जा दिया; और 86वें (2002) ने अनुच्छेद 21A जोड़ा।",
  f"{COI} -- Constitution (Forty-second Amendment) Act, 1976; {SC} -- Minerva Mills v. Union of India (1980).",
  "polity-42nd-amendment-mini-constitution", craft="linkage")

M(CF, "medium", "India's parliamentary system is modelled on the British (Westminster) one. In which one of the following respects does it depart most clearly from that model?",
  "भारत की संसदीय प्रणाली ब्रिटिश (वेस्टमिंस्टर) प्रणाली पर आधारित है। निम्नलिखित में से किस संदर्भ में यह उस मॉडल से सबसे स्पष्ट रूप से अलग है?",
  ["Courts can strike down laws made by Parliament for violating the Constitution",
   "The Council of Ministers is collectively responsible to the lower House",
   "The head of State is nominal, and real power lies with the Council of Ministers",
   "The Prime Minister is normally the leader of the majority in the lower House"],
  ["न्यायालय संविधान का उल्लंघन करने वाले संसद के क़ानूनों को रद्द कर सकते हैं",
   "मंत्रिपरिषद सामूहिक रूप से निचले सदन के प्रति उत्तरदायी है",
   "राष्ट्राध्यक्ष नाममात्र का है, और वास्तविक शक्ति मंत्रिपरिषद के पास है",
   "प्रधानमंत्री सामान्यतः निचले सदन में बहुमत के नेता होते हैं"],
  0,
  "Britain follows parliamentary sovereignty: no court can invalidate an Act of Parliament. India has a written Constitution that is supreme, so under Articles 13, 32 and 226 the courts can strike down laws that violate it -- a feature closer to the American system, and the reason Indian parliamentary government is described as limited, not sovereign. "
  "Collective responsibility to the lower House, a nominal head of State with real power in the Council of Ministers, and a Prime Minister who leads the majority are exactly the Westminster features India adopted. India's other departure, an elected head of State instead of a hereditary monarch, is not among the options.",
  "ब्रिटेन में संसदीय संप्रभुता है: कोई न्यायालय संसद के अधिनियम को अमान्य नहीं कर सकता। भारत का लिखित संविधान सर्वोच्च है, इसलिए अनुच्छेद 13, 32 और 226 के तहत न्यायालय उसका उल्लंघन करने वाले क़ानून रद्द कर सकते हैं; यह विशेषता अमेरिकी प्रणाली के अधिक क़रीब है, और इसी कारण भारतीय संसदीय शासन को संप्रभु नहीं, सीमित कहा जाता है। "
  "निचले सदन के प्रति सामूहिक उत्तरदायित्व, वास्तविक शक्ति मंत्रिपरिषद के पास रखते हुए नाममात्र का राष्ट्राध्यक्ष, और बहुमत का नेतृत्व करने वाले प्रधानमंत्री, ठीक वे वेस्टमिंस्टर विशेषताएँ हैं जो भारत ने अपनाईं। भारत का दूसरा अंतर, वंशानुगत सम्राट के बजाय निर्वाचित राष्ट्राध्यक्ष, विकल्पों में नहीं है।",
  f"{NC} -- Constitution: Why and How?; {COI} -- Articles 13, 32 and 226.",
  "polity-not-a-feature-presidential", craft="inference")

S(CF, "medium", "Consider the following situations and the Part of the Constitution named against each:",
  "निम्नलिखित स्थितियों और प्रत्येक के सामने दिए गए संविधान के भाग पर विचार कीजिए:",
  ["Whether Parliament may make a law on a subject in the State List after a resolution of the Rajya Sabha -- Part XI (Relations between the Union and the States)",
   "The conditions of service of an officer of the Indian Administrative Service -- Part XIV (Services under the Union and the States)",
   "The bar on courts questioning a law on the delimitation of constituencies -- Part XV (Elections)"],
  ["क्या राज्यसभा के संकल्प के बाद संसद राज्य सूची के किसी विषय पर क़ानून बना सकती है -- भाग XI (संघ और राज्यों के बीच संबंध)",
   "भारतीय प्रशासनिक सेवा के किसी अधिकारी की सेवा शर्तें -- भाग XIV (संघ और राज्यों के अधीन सेवाएँ)",
   "परिसीमन से जुड़े किसी क़ानून पर न्यायालयों द्वारा प्रश्न उठाने पर रोक -- भाग XV (निर्वाचन)"],
  C3, 2,
  "All three are correctly matched. The power to legislate on a State subject in the national interest (Article 249) sits in Part XI, Articles 245-263, with the rest of Union-State relations. "
  "The All-India Services and the Public Service Commissions are in Part XIV, Articles 308-323. "
  "Article 329, which bars the courts from questioning laws on delimitation and the allotment of seats, is in Part XV on elections, Articles 324-329A. Knowing which Part a provision sits in is how a lawyer finds the rule that governs a dispute -- and how UPSC tests whether the map of the Constitution is clear.",
  "तीनों सही सुमेलित हैं। राष्ट्रीय हित में राज्य के विषय पर क़ानून बनाने की शक्ति (अनुच्छेद 249) भाग XI, अनुच्छेद 245-263 में, संघ-राज्य संबंधों के शेष प्रावधानों के साथ है। "
  "अखिल भारतीय सेवाएँ और लोक सेवा आयोग भाग XIV, अनुच्छेद 308-323 में हैं। "
  "अनुच्छेद 329, जो परिसीमन और सीटों के आवंटन से जुड़े क़ानूनों पर न्यायालयों को प्रश्न उठाने से रोकता है, निर्वाचन वाले भाग XV, अनुच्छेद 324-329A में है। कोई प्रावधान किस भाग में है, यह जानना ही बताता है कि किसी विवाद पर कौन-सा नियम लागू होगा; UPSC इसी से परखता है कि संविधान का नक़्शा स्पष्ट है या नहीं।",
  f"{COI} -- Parts XI, XIV and XV.",
  "polity-constitution-parts-xi-xiv-xv", closing=MATCHED, closing_hi=MATCHED_HI, craft="application")

S(CF, "medium", "Consider the following statements about the early debate on linguistic States:",
  "भाषाई राज्यों पर आरंभिक बहस के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Dar Commission and the JVP Committee both advised caution, fearing that linguistic States might weaken national unity so soon after Partition.",
   "Andhra State was carved out in 1953 after the death of Potti Sriramulu, who had fasted for a separate Telugu-speaking State.",
   "The States Reorganisation Commission rejected language as a basis for reorganising States."],
  ["दार आयोग और जेवीपी समिति, दोनों ने सावधानी की सलाह दी, क्योंकि उन्हें डर था कि विभाजन के इतने जल्दी बाद भाषाई राज्य राष्ट्रीय एकता को कमज़ोर कर सकते हैं।",
   "आंध्र राज्य 1953 में पोट्टि श्रीरामुलु की मृत्यु के बाद बनाया गया, जिन्होंने अलग तेलुगु-भाषी राज्य के लिए अनशन किया था।",
   "राज्य पुनर्गठन आयोग ने राज्यों के पुनर्गठन के आधार के रूप में भाषा को अस्वीकार कर दिया।"],
  C3, 1,
  "Statements 1 and 2 are correct, and they explain each other. With Partition fresh, the Dar Commission (1948) and the Congress's JVP Committee (Nehru, Patel and Pattabhi Sitaramayya) put security and administrative convenience before language. Popular pressure overtook them when Potti Sriramulu died after a 58-day fast in December 1952, and Andhra State followed in 1953. "
  "Statement 3 is wrong: the States Reorganisation Commission (Fazl Ali, 1955) accepted language as an important factor but rejected 'one language, one State' as the sole test; the States Reorganisation Act, 1956 then redrew most boundaries on largely linguistic lines.",
  "कथन 1 और 2 सही हैं, और ये एक-दूसरे की व्याख्या करते हैं। विभाजन की ताज़ा स्मृति में दार आयोग (1948) और कांग्रेस की जेवीपी समिति (नेहरू, पटेल और पट्टाभि सीतारमैया) ने भाषा से पहले सुरक्षा और प्रशासनिक सुविधा को रखा। जनदबाव तब भारी पड़ा जब दिसंबर 1952 में 58 दिन के अनशन के बाद पोट्टि श्रीरामुलु की मृत्यु हुई, और 1953 में आंध्र राज्य बना। "
  "कथन 3 गलत है: राज्य पुनर्गठन आयोग (फ़ज़ल अली, 1955) ने भाषा को एक महत्वपूर्ण कारक माना, पर 'एक भाषा, एक राज्य' को एकमात्र कसौटी के रूप में अस्वीकार किया; इसके बाद राज्य पुनर्गठन अधिनियम, 1956 ने अधिकांश सीमाएँ मुख्यतः भाषाई आधार पर फिर से खींचीं।",
  f"{NC} -- Federalism; States Reorganisation Commission Report (1955).",
  "polity-states-reorganisation-dar-jvp", craft="linkage")

S(CF, "medium", "Consider the following statements about the Objectives Resolution that Jawaharlal Nehru moved in the Constituent Assembly in December 1946:",
  "दिसंबर 1946 में जवाहरलाल नेहरू द्वारा संविधान सभा में प्रस्तुत उद्देश्य प्रस्ताव के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It declared that all power and authority of independent India would be derived from the people.",
   "It envisaged that the units of the Union would retain the residuary powers.",
   "Its scheme for dividing powers between the Union and the units was carried into the Constitution unchanged."],
  ["इसने घोषित किया कि स्वतंत्र भारत की सारी शक्ति और प्राधिकार जनता से प्राप्त होंगे।",
   "इसमें परिकल्पना थी कि संघ की इकाइयाँ अवशिष्ट शक्तियाँ अपने पास रखेंगी।",
   "संघ और इकाइयों के बीच शक्तियों के बँटवारे की इसकी योजना संविधान में बिना बदले अपनाई गई।"],
  C3, 1,
  "Statements 1 and 2 are correct. Adopted on 22 January 1947, the Resolution promised a sovereign republic whose power came from the people, with justice, equality, freedoms and safeguards for minorities -- ideas the Preamble later carried. "
  "Drafted while the Cabinet Mission plan's weak Centre was still on the table and the Muslim League's participation was hoped for, it left the residuary powers with the autonomous units. "
  "Statement 3 is wrong: once Partition was announced in June 1947, the Assembly chose a strong Centre, and the Constitution vests residuary powers in Parliament (Article 248 and Entry 97 of the Union List). Seeing how the scheme changed is the point of the question.",
  "कथन 1 और 2 सही हैं। 22 जनवरी 1947 को स्वीकृत इस प्रस्ताव ने ऐसे संप्रभु गणराज्य का वचन दिया जिसकी शक्ति जनता से आती हो, जिसमें न्याय, समानता, स्वतंत्रताएँ और अल्पसंख्यकों के लिए सुरक्षा हो; बाद में प्रस्तावना ने यही विचार अपनाए। "
  "यह तब लिखा गया जब कैबिनेट मिशन योजना का कमज़ोर केंद्र अभी विचाराधीन था और मुस्लिम लीग की भागीदारी की आशा थी, इसलिए इसने अवशिष्ट शक्तियाँ स्वायत्त इकाइयों के पास छोड़ीं। "
  "कथन 3 गलत है: जून 1947 में विभाजन की घोषणा के बाद सभा ने मज़बूत केंद्र चुना, और संविधान अवशिष्ट शक्तियाँ संसद को देता है (अनुच्छेद 248 और संघ सूची की प्रविष्टि 97)। योजना कैसे बदली, यह समझना ही प्रश्न का मर्म है।",
  f"{CAD} -- Objectives Resolution, 13 December 1946; {GA}.",
  "polity-objectives-resolution", craft="linkage")

S(CF, "medium", "Consider the following statements about the Constitution of India:",
  "भारत के संविधान के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It provides for a single citizenship for the whole of India.",
   "It allows each State to frame and adopt a constitution of its own.",
   "If a Union law and a State law on a Concurrent List subject conflict, the Union law generally prevails."],
  ["यह पूरे भारत के लिए एकल नागरिकता का प्रावधान करता है।",
   "यह हर राज्य को अपना अलग संविधान बनाने और अपनाने की अनुमति देता है।",
   "यदि समवर्ती सूची के किसी विषय पर संघ और राज्य के क़ानून में टकराव हो, तो सामान्यतः संघ का क़ानून प्रभावी होता है।"],
  C3, 1,
  "Statements 1 and 3 are correct. Unlike the United States, India has no separate State citizenship. Under Article 254(1) a Union law prevails over a repugnant State law on a Concurrent subject; the exception in Article 254(2) lets a State law reserved for and assented to by the President prevail in that State, subject to later Union law. "
  "Statement 2 is wrong: one Constitution provides the framework for the Union and every State, which is one of the unitary strands in Indian federalism. Jammu and Kashmir alone had a constitution of its own, under Article 370, until the changes of 2019.",
  "कथन 1 और 3 सही हैं। संयुक्त राज्य अमेरिका के विपरीत भारत में अलग राज्य नागरिकता नहीं है। अनुच्छेद 254(1) के तहत समवर्ती विषय पर संघ का क़ानून विरोधी राज्य क़ानून पर प्रभावी होता है; अनुच्छेद 254(2) का अपवाद राष्ट्रपति के विचार के लिए आरक्षित और उनकी अनुमति पाए राज्य क़ानून को उस राज्य में प्रभावी होने देता है, बाद के संघीय क़ानून के अधीन। "
  "कथन 2 गलत है: एक ही संविधान संघ और हर राज्य का ढाँचा तय करता है, जो भारतीय संघवाद के एकात्मक तत्वों में से एक है। केवल जम्मू और कश्मीर का, अनुच्छेद 370 के तहत, 2019 के बदलावों तक अपना संविधान था।",
  f"{COI} -- Articles 5-11, 254 and 370; {NC} -- Federalism.",
  "polity-salient-features-citizenship-residuary", craft="precision")

# ================================================================ FUNDAMENTAL RIGHTS (11 rewritten)
M(FR, "hard", "In Indra Sawhney v. Union of India (1992), the Supreme Court upheld reservation for the Other Backward Classes in Central Government posts but required the 'creamy layer' to be excluded. Which one of the following best explains the reasoning behind the exclusion?",
  "इंद्रा साहनी बनाम भारत संघ (1992) में सर्वोच्च न्यायालय ने केंद्र सरकार के पदों में अन्य पिछड़ा वर्गों के आरक्षण को वैध ठहराया, पर 'क्रीमी लेयर' को बाहर रखने की शर्त लगाई। निम्नलिखित में से कौन-सा इस बहिष्कार के तर्क की सबसे सही व्याख्या करता है?",
  ["Advanced members of a backward class no longer share its backwardness, and including them would crowd out those who still do",
   "Reservation under Article 16(4) must rest on economic criteria alone, so that the better-off among all castes are treated alike",
   "The creamy layer belongs to the forward castes by definition, and Article 16(4) bars reservation for any forward caste",
   "Excluding the creamy layer was needed to keep total reservation within the 50 per cent ceiling, which the Court set in the same judgment"],
  ["पिछड़े वर्ग के उन्नत सदस्य अब उसके पिछड़ेपन में साझीदार नहीं रहे, और उन्हें शामिल करने से वे बाहर हो जाते जो अब भी पिछड़े हैं",
   "अनुच्छेद 16(4) के तहत आरक्षण केवल आर्थिक मानदंड पर टिका होना चाहिए, ताकि सभी जातियों के संपन्न लोगों से एक-सा व्यवहार हो",
   "क्रीमी लेयर परिभाषा से ही अगड़ी जातियों का भाग है, और अनुच्छेद 16(4) किसी अगड़ी जाति के लिए आरक्षण की मनाही करता है",
   "कुल आरक्षण को 50 प्रतिशत की सीमा में रखने के लिए क्रीमी लेयर को बाहर करना ज़रूरी था, जो सीमा न्यायालय ने उसी निर्णय में तय की"],
  0,
  "The Court accepted caste as a valid starting point for identifying backward classes under Article 16(4), but held that the members of such a class who have risen socially and economically -- children of senior officers, large landholders and the like -- are no longer 'backward' in the sense the Article intends. Letting them in would let the best-off corner the benefits meant for the rest. "
  "The exclusion is not an economic test replacing caste, and the creamy layer is not a forward caste. The 50 per cent ceiling, also laid down in Indra Sawhney, is a separate rule; the creamy-layer exclusion would apply even under the ceiling.",
  "न्यायालय ने अनुच्छेद 16(4) के तहत पिछड़े वर्गों की पहचान के लिए जाति को एक मान्य आरंभ-बिंदु माना, पर कहा कि ऐसे वर्ग के जो सदस्य सामाजिक और आर्थिक रूप से आगे बढ़ चुके हैं, जैसे वरिष्ठ अधिकारियों और बड़े भूस्वामियों की संतानें, वे उस अर्थ में 'पिछड़े' नहीं रहे जो अनुच्छेद चाहता है। उन्हें शामिल करने से सबसे संपन्न लोग बाक़ियों के लिए बने लाभ हथिया लेते। "
  "यह बहिष्कार जाति की जगह कोई आर्थिक कसौटी नहीं है, और क्रीमी लेयर कोई अगड़ी जाति नहीं है। 50 प्रतिशत की सीमा, जो इंद्रा साहनी में ही तय हुई, एक अलग नियम है; क्रीमी लेयर का बहिष्कार इस सीमा के भीतर भी लागू होता।",
  f"{SC} -- Indra Sawhney v. Union of India (1992).",
  "rights-indra-sawhney-obc-jobs", craft="inference")

M(FR, "medium", "In Vishaka v. State of Rajasthan (1997), the Supreme Court laid down binding guidelines against sexual harassment at the workplace although no law on the subject existed. Which one of the following best describes the basis on which it acted?",
  "विशाखा बनाम राजस्थान राज्य (1997) में सर्वोच्च न्यायालय ने कार्यस्थल पर यौन उत्पीड़न के विरुद्ध बाध्यकारी दिशानिर्देश बनाए, जबकि इस विषय पर कोई क़ानून नहीं था। निम्नलिखित में से कौन-सा उस आधार का सबसे सही वर्णन करता है जिस पर न्यायालय ने कार्य किया?",
  ["It read the rights to equality, to work and to life together with India's obligations under CEDAW, filling a gap until Parliament acted",
   "It exercised, on Parliament's behalf, the power under Article 253 to make laws for implementing international treaties, conventions and agreements",
   "It enforced one of the Directive Principles directly, as if it were a Fundamental Right",
   "It enforced the Fundamental Duty in Article 51A(e) to renounce practices derogatory to the dignity of women as a legal command"],
  ["इसने समानता, काम और जीवन के अधिकारों को CEDAW के तहत भारत के दायित्वों के साथ पढ़ा, और संसद के क़ानून बनाने तक की कमी भरी",
   "इसने संसद की ओर से अनुच्छेद 253 के तहत अंतरराष्ट्रीय संधियों, अभिसमयों और समझौतों को लागू करने के लिए क़ानून बनाने की शक्ति का उपयोग किया",
   "इसने नीति-निदेशक तत्वों में से एक को सीधे मौलिक अधिकार की तरह लागू किया",
   "इसने महिलाओं की गरिमा के विरुद्ध प्रथाओं को त्यागने वाले अनुच्छेद 51A(ङ) के मौलिक कर्तव्य को क़ानूनी आदेश की तरह लागू किया"],
  0,
  "The Court treated sexual harassment as a violation of Articles 14, 15, 19(1)(g) and 21, and held that, in the absence of domestic law, international conventions consistent with Fundamental Rights -- here CEDAW, which India had ratified -- can be read into them. Acting under Article 32, it framed guidelines that would bind until Parliament legislated, which it did in the Sexual Harassment of Women at Workplace Act, 2013. "
  "The Court did not exercise Article 253, which is Parliament's power, and it did not enforce a Directive Principle or a Fundamental Duty directly. Both remain non-justiciable, though they shape how rights are read.",
  "न्यायालय ने यौन उत्पीड़न को अनुच्छेद 14, 15, 19(1)(छ) और 21 का उल्लंघन माना, और कहा कि घरेलू क़ानून न होने पर मौलिक अधिकारों से मेल खाने वाले अंतरराष्ट्रीय अभिसमय, यहाँ भारत द्वारा अनुसमर्थित CEDAW, उनमें पढ़े जा सकते हैं। अनुच्छेद 32 के तहत उसने ऐसे दिशानिर्देश बनाए जो संसद के क़ानून बनाने तक बाध्यकारी रहें; संसद ने 2013 में कार्यस्थल पर महिलाओं का यौन उत्पीड़न अधिनियम बनाया। "
  "न्यायालय ने अनुच्छेद 253 का उपयोग नहीं किया, जो संसद की शक्ति है, और न ही किसी नीति-निदेशक तत्व या मौलिक कर्तव्य को सीधे लागू किया। ये दोनों अप्रवर्तनीय रहते हैं, यद्यपि अधिकारों की व्याख्या को प्रभावित करते हैं।",
  f"{SC} -- Vishaka v. State of Rajasthan (1997).",
  "rights-vishaka-guidelines", craft="inference")

S(FR, "medium", "Which of the following are 'the State' within the meaning of Article 12 of the Constitution?",
  "निम्नलिखित में से कौन संविधान के अनुच्छेद 12 के अर्थ में 'राज्य' हैं?",
  ["A municipal corporation",
   "A company wholly owned by the Union government and functioning under its control",
   "A private unaided school",
   "The Board of Control for Cricket in India"],
  ["एक नगर निगम",
   "केंद्र सरकार के पूर्ण स्वामित्व वाली और उसके नियंत्रण में काम करने वाली एक कंपनी",
   "एक निजी ग़ैर-सहायता प्राप्त विद्यालय",
   "भारतीय क्रिकेट कंट्रोल बोर्ड (BCCI)"],
  C4, 1,
  "Only two -- the first two. Article 12 expressly includes local authorities such as municipalities. A government company is an 'other authority' when it is financially, functionally and administratively dominated by the Government (Ajay Hasia, 1981; Pradeep Kumar Biswas, 2002). "
  "A private unaided school is not the State, though a writ may lie against it under Article 226 for a public duty. The BCCI is the trap: in Zee Telefilms v. Union of India (2005) the Supreme Court held that it is not 'the State' under Article 12, because the Government does not control it financially, functionally or administratively, though it performs public functions and can be reached through Article 226.",
  "केवल दो, पहले दो। अनुच्छेद 12 स्पष्ट रूप से नगरपालिकाओं जैसे स्थानीय प्राधिकरणों को शामिल करता है। सरकारी कंपनी 'अन्य प्राधिकरण' तब है जब उस पर सरकार का वित्तीय, कार्यात्मक और प्रशासनिक प्रभुत्व हो (अजय हसिया, 1981; प्रदीप कुमार बिस्वास, 2002)। "
  "निजी ग़ैर-सहायता प्राप्त विद्यालय 'राज्य' नहीं है, यद्यपि किसी सार्वजनिक कर्तव्य के लिए अनुच्छेद 226 के तहत उसके विरुद्ध रिट जा सकती है। BCCI जाल है: ज़ी टेलीफ़िल्म्स बनाम भारत संघ (2005) में सर्वोच्च न्यायालय ने कहा कि यह अनुच्छेद 12 के तहत 'राज्य' नहीं है, क्योंकि सरकार इस पर वित्तीय, कार्यात्मक या प्रशासनिक नियंत्रण नहीं रखती, यद्यपि यह सार्वजनिक कार्य करता है और अनुच्छेद 226 के ज़रिए इस तक पहुँचा जा सकता है।",
  f"{COI} -- Article 12; {SC} -- Zee Telefilms v. Union of India (2005), Pradeep Kumar Biswas v. Indian Institute of Chemical Biology (2002).",
  "rights-art12-state-other-authorities", closing="How many of the above are 'the State' under Article 12?",
  closing_hi="उपर्युक्त में से कितने अनुच्छेद 12 के तहत 'राज्य' हैं?", craft="multi")

S(FR, "medium", "A society of Telugu-speaking people in Karnataka sets up a school, which later receives aid from the State government. Consider the following statements:",
  "कर्नाटक में तेलुगु-भाषी लोगों की एक संस्था एक विद्यालय स्थापित करती है, जिसे बाद में राज्य सरकार से सहायता मिलने लगती है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The society can claim the protection of Article 30 as a linguistic minority, even though Telugu speakers are not a minority in India as a whole.",
   "Since it receives State aid, the school may refuse admission to children who do not speak Telugu.",
   "The State government may take over the management of the school if it disapproves of the society's choice of headmaster."],
  ["संस्था भाषाई अल्पसंख्यक के रूप में अनुच्छेद 30 के संरक्षण का दावा कर सकती है, भले ही पूरे भारत में तेलुगु-भाषी अल्पसंख्यक न हों।",
   "राज्य सहायता मिलने के कारण विद्यालय तेलुगु न बोलने वाले बच्चों को प्रवेश देने से मना कर सकता है।",
   "यदि राज्य सरकार को संस्था द्वारा प्रधानाध्यापक का चयन पसंद न हो, तो वह विद्यालय का प्रबंधन अपने हाथ में ले सकती है।"],
  C3, 0,
  "Only statement 1 is correct. In T.M.A. Pai Foundation (2002) the Supreme Court held that, since States were reorganised on linguistic lines, minority status for State laws is judged State by State; Telugu speakers are a linguistic minority in Karnataka. "
  "Statement 2 is wrong: under Article 29(2) no citizen may be denied admission to an institution that receives State aid on grounds only of religion, race, caste or language. A minority institution may keep a reasonable share of seats for its own community, but it cannot shut out others. "
  "Statement 3 is wrong: the right to administer includes choosing staff. The State may lay down qualifications and standards, but taking over management would destroy the right that Article 30 protects.",
  "केवल कथन 1 सही है। टी.एम.ए. पाई फ़ाउंडेशन (2002) में सर्वोच्च न्यायालय ने कहा कि चूँकि राज्यों का पुनर्गठन भाषाई आधार पर हुआ, इसलिए राज्य के क़ानूनों के लिए अल्पसंख्यक दर्जा राज्य-वार तय होता है; कर्नाटक में तेलुगु-भाषी भाषाई अल्पसंख्यक हैं। "
  "कथन 2 गलत है: अनुच्छेद 29(2) के तहत राज्य सहायता पाने वाली किसी संस्था में किसी नागरिक को केवल धर्म, मूलवंश, जाति या भाषा के आधार पर प्रवेश से वंचित नहीं किया जा सकता। अल्पसंख्यक संस्था अपने समुदाय के लिए सीटों का उचित हिस्सा रख सकती है, पर दूसरों को पूरी तरह बाहर नहीं कर सकती। "
  "कथन 3 गलत है: प्रशासन के अधिकार में कर्मचारियों का चयन भी शामिल है। राज्य योग्यताएँ और मानक तय कर सकता है, पर प्रबंधन अपने हाथ में लेना उसी अधिकार को नष्ट कर देगा जिसे अनुच्छेद 30 संरक्षित करता है।",
  f"{COI} -- Articles 29 and 30; {SC} -- T.M.A. Pai Foundation v. State of Karnataka (2002).",
  "rights-art29-30-minorities", craft="application")

S(FR, "medium", "Consider the following educational institutions:",
  "निम्नलिखित शिक्षा संस्थानों पर विचार कीजिए:",
  ["A school wholly maintained out of State funds",
   "A school administered by the State but set up under a trust that requires religious instruction to be given in it",
   "A private school recognised by the State, where a pupil's guardian has consented to religious instruction"],
  ["पूरी तरह राज्य निधि से चलने वाला एक विद्यालय",
   "राज्य द्वारा प्रशासित पर ऐसे न्यास के तहत स्थापित विद्यालय, जिसकी शर्त है कि उसमें धार्मिक शिक्षा दी जाए",
   "राज्य से मान्यता प्राप्त एक निजी विद्यालय, जहाँ किसी विद्यार्थी के अभिभावक ने धार्मिक शिक्षा के लिए सहमति दी है"],
  None, 1,
  "Religious instruction is permitted in the second and third. Article 28(1) bars religious instruction in any institution wholly maintained out of State funds. Clause (2) exempts an institution administered by the State but established under an endowment or trust that requires such instruction. Clause (3) allows it in recognised or State-aided institutions, provided no one is compelled to attend -- a minor needs the guardian's consent. "
  "The scheme protects the conscience of pupils without banning religious teaching outright. Article 25, which it complements, is available to all persons, citizens or not.",
  "धार्मिक शिक्षा दूसरे और तीसरे संस्थान में अनुमत है। अनुच्छेद 28(1) पूरी तरह राज्य निधि से चलने वाली किसी भी संस्था में धार्मिक शिक्षा पर रोक लगाता है। खंड (2) उस संस्था को छूट देता है जो राज्य द्वारा प्रशासित है पर ऐसे धर्मस्व या न्यास के तहत स्थापित है जिसकी शर्त ऐसी शिक्षा है। खंड (3) मान्यता प्राप्त या राज्य सहायता पाने वाली संस्थाओं में इसकी अनुमति देता है, बशर्ते किसी को उपस्थित होने के लिए बाध्य न किया जाए; अवयस्क के लिए अभिभावक की सहमति चाहिए। "
  "यह व्यवस्था धार्मिक शिक्षा पर पूरी रोक लगाए बिना विद्यार्थियों की अंतरात्मा की रक्षा करती है। इसका पूरक अनुच्छेद 25 सभी व्यक्तियों को, नागरिक हों या नहीं, उपलब्ध है।",
  f"{COI} -- Articles 25-28; {NC} -- Rights in the Indian Constitution.",
  "rights-freedom-of-religion-25-28", opts=["1 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
  opts_hi=["केवल 1", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
  closing="In which of the above may religious instruction be imparted under Article 28?",
  closing_hi="अनुच्छेद 28 के तहत उपर्युक्त में से किसमें/किनमें धार्मिक शिक्षा दी जा सकती है?", craft="application")

S(CF, "medium", "An Indian citizen voluntarily acquires the citizenship of Canada. Consider the following statements:",
  "एक भारतीय नागरिक स्वेच्छा से कनाडा की नागरिकता ले लेता है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["He ceases to be a citizen of India under the Citizenship Act, 1955.",
   "Since the Constitution itself lists the grounds on which citizenship is lost, Parliament could not have provided for this by an ordinary law.",
   "He can keep his Indian citizenship by declaring that he wishes to hold dual citizenship."],
  ["नागरिकता अधिनियम, 1955 के तहत वह भारत का नागरिक नहीं रहता।",
   "चूँकि संविधान स्वयं नागरिकता समाप्त होने के आधार गिनाता है, इसलिए संसद साधारण क़ानून से इसका प्रावधान नहीं कर सकती थी।",
   "वह दोहरी नागरिकता रखने की इच्छा घोषित कर अपनी भारतीय नागरिकता बनाए रख सकता है।"],
  C3, 0,
  "Only statement 1 is correct. Under section 9 of the Citizenship Act, 1955, an Indian citizen who voluntarily acquires another country's citizenship ceases to be an Indian citizen. "
  "Statement 2 is wrong: Part II of the Constitution (Articles 5-11) settled only who was a citizen at its commencement, and Article 11 leaves the acquisition and termination of citizenship after that to Parliament. That is why the Citizenship Act, an ordinary law, governs these questions. "
  "Statement 3 is wrong: India does not permit dual citizenship. Persons of Indian origin who hold foreign citizenship may instead be eligible for other statuses under the Act.",
  "केवल कथन 1 सही है। नागरिकता अधिनियम, 1955 की धारा 9 के तहत जो भारतीय नागरिक स्वेच्छा से दूसरे देश की नागरिकता लेता है, वह भारतीय नागरिक नहीं रहता। "
  "कथन 2 गलत है: संविधान के भाग II (अनुच्छेद 5-11) ने केवल यह तय किया कि उसके प्रारंभ पर कौन नागरिक था, और अनुच्छेद 11 उसके बाद नागरिकता के अर्जन और समाप्ति का विषय संसद पर छोड़ता है; इसीलिए एक साधारण क़ानून, नागरिकता अधिनियम, इन प्रश्नों को नियंत्रित करता है। "
  "कथन 3 गलत है: भारत दोहरी नागरिकता की अनुमति नहीं देता। विदेशी नागरिकता रखने वाले भारतीय मूल के लोग इसके बजाय अधिनियम के तहत अन्य दर्जों के पात्र हो सकते हैं।",
  f"{COI} -- Articles 5-11; Citizenship Act, 1955, section 9.",
  "polity-citizenship-part-ii", craft="application")

M(FR, "medium", "During a national emergency proclaimed on the ground of external aggression, the President issues an order under Article 359 suspending the right to move the courts for the enforcement of Fundamental Rights. A person detained during this period can still move a court to enforce which one of the following?",
  "बाह्य आक्रमण के आधार पर घोषित राष्ट्रीय आपातकाल के दौरान राष्ट्रपति अनुच्छेद 359 के तहत मौलिक अधिकारों के प्रवर्तन के लिए न्यायालय जाने के अधिकार को निलंबित करने का आदेश जारी करते हैं। इस अवधि में हिरासत में लिया गया व्यक्ति फिर भी निम्नलिखित में से किसे लागू कराने के लिए न्यायालय जा सकता है?",
  ["The protection of life and personal liberty under Article 21",
   "The safeguards against arbitrary arrest and detention under Article 22",
   "The right to equality before the law under Article 14",
   "The freedom of movement throughout India under Article 19"],
  ["अनुच्छेद 21 के तहत प्राण और दैहिक स्वतंत्रता का संरक्षण",
   "अनुच्छेद 22 के तहत मनमानी गिरफ़्तारी और निरोध के विरुद्ध सुरक्षा",
   "अनुच्छेद 14 के तहत विधि के समक्ष समता का अधिकार",
   "अनुच्छेद 19 के तहत पूरे भारत में आवागमन की स्वतंत्रता"],
  0,
  "Since the 44th Amendment (1978), an order under Article 359 cannot suspend the enforcement of Articles 20 and 21, so the detenu can still seek habeas corpus on the ground that his life or personal liberty has been taken away without lawful procedure. The amendment was Parliament's answer to ADM Jabalpur (1976), where the Court had held the opposite during the Emergency. "
  "Articles 22 and 14 can be suspended by such an order. Article 19 is a double trap: during an emergency declared on the ground of war or external aggression it is suspended automatically under Article 358, without any order.",
  "44वें संशोधन (1978) के बाद अनुच्छेद 359 का आदेश अनुच्छेद 20 और 21 के प्रवर्तन को निलंबित नहीं कर सकता, इसलिए निरुद्ध व्यक्ति फिर भी इस आधार पर बंदी प्रत्यक्षीकरण माँग सकता है कि उसका जीवन या दैहिक स्वतंत्रता विधिसम्मत प्रक्रिया के बिना छीनी गई। यह संशोधन ए.डी.एम. जबलपुर (1976) का संसद का जवाब था, जिसमें आपातकाल के दौरान न्यायालय ने उल्टा माना था। "
  "अनुच्छेद 22 और 14 ऐसे आदेश से निलंबित हो सकते हैं। अनुच्छेद 19 दोहरा जाल है: युद्ध या बाह्य आक्रमण के आधार पर घोषित आपातकाल में यह अनुच्छेद 358 के तहत बिना किसी आदेश के अपने आप निलंबित हो जाता है।",
  f"{COI} -- Articles 358 and 359; Constitution (Forty-fourth Amendment) Act, 1978.",
  "rights-art20-21-non-suspendable", craft="application")

S(FR, "hard", "Consider the following cases:",
  "निम्नलिखित मामलों पर विचार कीजिए:",
  ["A person is punished under a criminal law enacted after he committed the act it punishes.",
   "A government servant dismissed after a departmental inquiry is also prosecuted in court for the same misconduct.",
   "The police require an accused person to give specimens of his fingerprints and handwriting."],
  ["किसी व्यक्ति को ऐसे आपराधिक क़ानून के तहत दंड दिया जाता है जो उसके द्वारा वह कार्य किए जाने के बाद बना।",
   "विभागीय जाँच के बाद बर्ख़ास्त किए गए एक सरकारी कर्मचारी पर उसी कदाचार के लिए न्यायालय में मुक़दमा भी चलाया जाता है।",
   "पुलिस एक अभियुक्त से उसकी उँगलियों के निशान और हस्तलेख के नमूने देने को कहती है।"],
  None, 0,
  "Article 20 is violated only in the first case. Article 20(1) bars conviction under an ex post facto criminal law; it does not reach retrospective civil or tax laws. "
  "In the second case there is no double jeopardy, because Article 20(2) protects against being prosecuted and punished twice by a court, and a departmental inquiry is not a prosecution. "
  "In the third case there is no self-incrimination, because Article 20(3) bars testimonial compulsion -- being made a witness against oneself -- and the Supreme Court held in Kathi Kalu Oghad (1961) that giving fingerprints or specimen handwriting is not testimony. Forcing a narco-analysis test without consent, by contrast, does violate it (Selvi, 2010).",
  "अनुच्छेद 20 का उल्लंघन केवल पहले मामले में है। अनुच्छेद 20(1) भूतलक्षी आपराधिक क़ानून के तहत दोषसिद्धि पर रोक लगाता है; यह भूतलक्षी सिविल या कर क़ानूनों पर लागू नहीं होता। "
  "दूसरे मामले में दोहरा दंड नहीं है, क्योंकि अनुच्छेद 20(2) न्यायालय द्वारा दो बार अभियोजन और दंड से बचाता है, और विभागीय जाँच अभियोजन नहीं है। "
  "तीसरे मामले में आत्म-अभिशंसन नहीं है, क्योंकि अनुच्छेद 20(3) साक्षीय विवशता, यानी स्वयं के विरुद्ध गवाह बनने के लिए बाध्य किए जाने, पर रोक लगाता है, और सर्वोच्च न्यायालय ने काठी कालू ओघड़ (1961) में कहा कि उँगलियों के निशान या हस्तलेख के नमूने देना गवाही नहीं है। इसके विपरीत, बिना सहमति नार्को-विश्लेषण परीक्षण कराना इसका उल्लंघन है (सेल्वी, 2010)।",
  f"{COI} -- Article 20; {SC} -- State of Bombay v. Kathi Kalu Oghad (1961), Selvi v. State of Karnataka (2010).",
  "rights-article-20-21a-scope", opts=["1 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"],
  opts_hi=["केवल 1", "केवल 1 और 2", "केवल 2 और 3", "1, 2 और 3"],
  closing="In which of the above cases is Article 20 of the Constitution violated?",
  closing_hi="उपर्युक्त में से किस/किन मामले/मामलों में संविधान के अनुच्छेद 20 का उल्लंघन होता है?", craft="application")

S(FR, "medium", "A contractor building a road for a State government pays his labourers less than the minimum wage, and a 13-year-old boy works in a private factory nearby. Consider the following statements:",
  "राज्य सरकार के लिए सड़क बना रहा एक ठेकेदार अपने मज़दूरों को न्यूनतम मज़दूरी से कम देता है, और पास के एक निजी कारख़ाने में 13 वर्ष का एक लड़का काम करता है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["Paying less than the minimum wage can amount to 'forced labour' prohibited by Article 23.",
   "Employing the boy in the factory violates Article 24.",
   "Article 23 can be enforced against the contractor even though he is a private person and not the State."],
  ["न्यूनतम मज़दूरी से कम भुगतान अनुच्छेद 23 द्वारा प्रतिबंधित 'बलात् श्रम' के बराबर हो सकता है।",
   "उस लड़के को कारख़ाने में काम पर रखना अनुच्छेद 24 का उल्लंघन है।",
   "अनुच्छेद 23 ठेकेदार के विरुद्ध लागू कराया जा सकता है, भले ही वह निजी व्यक्ति है, राज्य नहीं।"],
  C3, 2,
  "All three are correct. In People's Union for Democratic Rights v. Union of India (1982), the Asiad workers' case, the Supreme Court held that labour extracted by paying less than the minimum wage is 'forced labour': economic compulsion can force a person as surely as physical force. "
  "Article 24 bars the employment of children below fourteen in any factory, mine or other hazardous employment, so the boy's employment is unlawful. "
  "Articles 23 and 24 are among the few Fundamental Rights that operate against private persons as well as the State, which is why the contractor and the factory owner are both bound.",
  "तीनों कथन सही हैं। पीपल्स यूनियन फ़ॉर डेमोक्रेटिक राइट्स बनाम भारत संघ (1982), यानी एशियाड मज़दूर मामले में सर्वोच्च न्यायालय ने कहा कि न्यूनतम मज़दूरी से कम देकर लिया गया श्रम 'बलात् श्रम' है: आर्थिक विवशता भी उतनी ही बाध्य करती है जितना शारीरिक बल। "
  "अनुच्छेद 24 चौदह वर्ष से कम आयु के बच्चों को किसी कारख़ाने, खान या अन्य ख़तरनाक रोज़गार में लगाने पर रोक लगाता है, इसलिए लड़के का रोज़गार अवैध है। "
  "अनुच्छेद 23 और 24 उन गिने-चुने मौलिक अधिकारों में हैं जो राज्य के साथ निजी व्यक्तियों पर भी लागू होते हैं; इसीलिए ठेकेदार और कारख़ाना मालिक दोनों बँधे हैं।",
  f"{COI} -- Articles 23 and 24; {SC} -- People's Union for Democratic Rights v. Union of India (1982).",
  "rights-art23-24-exploitation", craft="application")

S(FR, "medium", "A State government frames the following rules for recruitment to its police:",
  "एक राज्य सरकार अपनी पुलिस में भर्ती के लिए निम्नलिखित नियम बनाती है:",
  ["One-third of the posts are reserved for women.",
   "Only persons who have lived in the State for ten years may apply, under a condition laid down by the State Legislature.",
   "Every candidate must pass a test of physical fitness."],
  ["एक-तिहाई पद महिलाओं के लिए आरक्षित हैं।",
   "राज्य विधानमंडल द्वारा तय शर्त के तहत केवल वे लोग आवेदन कर सकते हैं जो दस वर्ष से राज्य में रह रहे हैं।",
   "हर उम्मीदवार को शारीरिक दक्षता परीक्षा पास करनी होगी।"],
  None, 1,
  "Rules 1 and 3 are consistent with the Constitution. Reservation for women in public posts has been upheld under Article 15(3), which permits special provisions for women (Government of Andhra Pradesh v. P.B. Vijayakumar, 1995). A fitness test is a reasonable qualification linked to the job and does not discriminate on any forbidden ground. "
  "Rule 2 fails: Article 16(2) forbids discrimination in public employment on grounds that include residence, and Article 16(3) lets only Parliament, not a State Legislature, prescribe residence as a condition for posts under a State. Note the difference between the two Articles: Article 15(1) does not list residence or descent, but Article 16(2) does.",
  "नियम 1 और 3 संविधान के अनुरूप हैं। सार्वजनिक पदों पर महिलाओं के लिए आरक्षण को अनुच्छेद 15(3) के तहत वैध माना गया है, जो महिलाओं के लिए विशेष उपबंध की अनुमति देता है (आंध्र प्रदेश सरकार बनाम पी.बी. विजयकुमार, 1995)। शारीरिक दक्षता परीक्षा नौकरी से जुड़ी उचित योग्यता है और किसी वर्जित आधार पर भेदभाव नहीं करती। "
  "नियम 2 टिकता नहीं: अनुच्छेद 16(2) सार्वजनिक रोज़गार में निवास सहित कुछ आधारों पर भेदभाव की मनाही करता है, और अनुच्छेद 16(3) केवल संसद को, न कि राज्य विधानमंडल को, राज्य के अधीन पदों के लिए निवास की शर्त तय करने देता है। दोनों अनुच्छेदों का अंतर ध्यान दें: अनुच्छेद 15(1) में निवास या वंश नहीं है, पर अनुच्छेद 16(2) में है।",
  f"{COI} -- Articles 15 and 16; {SC} -- Government of Andhra Pradesh v. P.B. Vijayakumar (1995).",
  "rights-art15-16-grounds-residence", opts=["1 only", "1 and 3 only", "2 and 3 only", "1, 2 and 3"],
  opts_hi=["केवल 1", "केवल 1 और 3", "केवल 2 और 3", "1, 2 और 3"],
  closing="Which of the above rules are consistent with the Constitution?",
  closing_hi="उपर्युक्त में से कौन-से नियम संविधान के अनुरूप हैं?", craft="application")

S(FR, "medium", "Consider the following assertion:\n'The grounds on which free speech may be restricted have been widened by constitutional amendment since 1950.'\nWhich of the following statements support this assertion?",
  "निम्नलिखित अभिकथन पर विचार कीजिए:\n'1950 के बाद संविधान संशोधन द्वारा उन आधारों का विस्तार किया गया है जिन पर अभिव्यक्ति की स्वतंत्रता पर प्रतिबंध लगाया जा सकता है।'\nनिम्नलिखित में से कौन-से कथन इस अभिकथन का समर्थन करते हैं?",
  ["The First Amendment (1951) added new grounds of restriction after the courts had struck down early curbs on the press.",
   "The 16th Amendment (1963) added 'the sovereignty and integrity of India' as a ground of restriction.",
   "The courts have read freedom of the press into the freedom of speech and expression."],
  ["पहले संशोधन (1951) ने प्रेस पर आरंभिक अंकुशों को न्यायालयों द्वारा रद्द किए जाने के बाद प्रतिबंध के नए आधार जोड़े।",
   "16वें संशोधन (1963) ने 'भारत की संप्रभुता और अखंडता' को प्रतिबंध के एक आधार के रूप में जोड़ा।",
   "न्यायालयों ने प्रेस की स्वतंत्रता को वाक् और अभिव्यक्ति की स्वतंत्रता में शामिल माना है।"],
  None, 0,
  "Statements 1 and 2 support the assertion. After Romesh Thappar and Brij Bhushan (1950) struck down curbs on the press, the First Amendment rewrote Article 19(2) and added new grounds. After the war with China and secessionist demands of the early 1960s, the 16th Amendment added 'the sovereignty and integrity of India'. "
  "Statement 3 is also true, but it widens the right, not the restrictions, so it does not support the assertion. Judging which true facts bear on a claim is the skill being tested.",
  "कथन 1 और 2 अभिकथन का समर्थन करते हैं। रोमेश थापर और बृज भूषण (1950) में प्रेस पर अंकुश रद्द होने के बाद पहले संशोधन ने अनुच्छेद 19(2) को फिर से लिखा और नए आधार जोड़े; 1960 के दशक की शुरुआत में चीन से युद्ध और अलगाववादी माँगों के बाद 16वें संशोधन ने 'भारत की संप्रभुता और अखंडता' जोड़ी। "
  "कथन 3 भी सही है, पर वह प्रतिबंधों का नहीं, अधिकार का विस्तार करता है, इसलिए अभिकथन का समर्थन नहीं करता। कौन-से सही तथ्य किसी दावे से जुड़ते हैं, यह परखना ही वह कौशल है जिसकी जाँच हो रही है।",
  f"{COI} -- Article 19(2) and the First and Sixteenth Amendments; {GA}.",
  "rights-art19-press-assembly-16th", opts=["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
  opts_hi=["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"], closing=CODE, craft="linkage")

# ================================================================ TAGS for the 83 kept rows (Test 21's 3 are tagged already)
TAGS = {
 "polity-living-document-easy": "inference", "polity-preamble-amendability-kesavananda": "precision",
 "polity-preamble-enacted-last-nonjusticiable": "linkage", "polity-rajya-sabha-veto-amendment": "linkage",
 "polity-citizenship-by-descent-registration": "precision", "polity-goi-act-1919-electorates-psc": "linkage",
 "polity-integrated-judiciary-hc-not-subordinate": "precision", "polity-quasi-federal-wheare": "linkage",
 "polity-rigid-flexible-amendment-modes": "linkage", "polity-princely-states-integration-pairs": "recall",
 "polity-scholars-descriptions-pairs": "recall", "polity-amendment-acts-subject-pairs": "recall",
 "polity-ca-persons-roles-pairs": "recall", "polity-preamble-terms-pairs": "precision",
 "polity-preamble-source-of-authority": "recall", "polity-constituent-assembly-committees-chairs": "recall",
 "polity-bn-rau-constitutional-adviser": "recall", "polity-ca-temporary-chairman-sinha": "recall",
 "polity-fourth-schedule-rajya-sabha-seats": "recall", "polity-instrument-of-accession": "precision",
 "polity-constitution-length-schedules": "recall", "polity-judicial-review-president-election": "recall",
 "polity-44th-amendment": "precision", "polity-amendments-7th-69th-100th": "recall",
 "polity-basic-structure-later-cases": "precision", "polity-ca-numbers-duration": "recall",
 "polity-ca-sovereign-drafting-hyderabad": "recall", "polity-caa-2019-cutoff-naturalisation": "precision",
 "polity-goi-act-1935-lists-residuary": "precision", "polity-official-language-part-xvii": "precision",
 "polity-schedules-first-second-third": "precision", "polity-schedules-ninth-eleventh-twelfth": "recall",
 "polity-simple-majority-amendments": "multi", "polity-sources-australia-japan": "recall",
 "polity-union-territory-art3-berubari": "precision", "polity-104th-106th-amendments": "precision",
 "polity-amendment-procedure-initiation": "precision", "polity-amendment-ratification-art368": "precision",
 "polity-borrowed-features-sources": "recall", "polity-british-acts-1833-1853-1861": "recall",
 "polity-ca-composition-election": "recall", "polity-ca-other-functions-symbols": "recall",
 "polity-citizenship-articles-6-8": "precision", "polity-federal-features": "application",
 "polity-golaknath-kesavananda": "precision", "polity-making-of-constitution": "recall",
 "polity-oci-cardholders": "precision", "polity-parts-iva-ix-vi": "recall",
 "polity-preamble-amendment-cases": "precision", "polity-preamble-text-justice-liberty": "precision",
 "polity-schedules-tenth-eighth": "recall",
 "polity-union-territory-art1-sikkim": "precision", "polity-unitary-features": "multi",
 "rights-art31c-minerva-harmony": "linkage", "rights-promotion-reservation-16-4a": "linkage",
 "rights-champakam-15-4": "linkage", "rights-dpsp-non-justiciable-art37": "linkage",
 "rights-privacy-puttaswamy": "linkage", "rights-judgments-pairs": "recall",
 "rights-citizens-vs-all-persons-pairs": "precision", "rights-dpsp-articles-pairs": "recall",
 "rights-writs-features-pairs": "precision", "rights-article-32-heart-and-soul": "recall",
 "rights-dpsp-97th-amendment-43b": "recall", "rights-art19-2-grounds-not": "precision",
 "rights-art22-enemy-alien": "precision", "rights-duties-citizens-vote-easy": "recall",
 "rights-art13-eclipse-severability": "precision", "rights-art19-tribes-state-trade-strike": "precision",
 "rights-art22-preventive-detention": "precision", "rights-art33-34-forces-martial-law": "precision",
 "rights-directives-outside-part-iv": "precision", "rights-dpsp-vs-duties-which": "multi",
 "rights-ews-reservation-103rd": "precision", "rights-art14-origins-classification": "precision",
 "rights-art21-gopalan-dignity-euthanasia": "precision", "rights-articles-15-17-18": "precision",
 "rights-dpsp-41-42-43-living-wage": "precision", "rights-dpsp-articles-40-44-45-50": "recall",
 "rights-fundamental-duties-origin": "recall", "rights-fundamental-duties-which": "multi",
 "rights-writ-jurisdiction-32-226": "precision"}

if __name__ == "__main__":
    write_updates("upg_l2_t01_polity.sql", statuses=("draft", "published"), tags=TAGS)
