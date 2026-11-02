# -*- coding: utf-8 -*-
"""Level 4 · Simulator 3 (GS Paper I full mock, Layout C: the 2026 shape) -- part A: Polity (12)
(upsc_l4_gs_cell_targets.mjs 3).
Layout C follows the 2026 paper: combination codes ('1 and 3 only') for most multi-statement items, List-I/List-II
matching with codes, and only three Statement-I/II items in the whole paper. Every tested proposition was swept
against the whole UPSC bank (5,473 rows after Simulator 2) and no row tests it: the Director of Enforcement under
section 25 of the CVC Act and Jaya Thakur; the Forty-third Amendment; Articles 133, 134 and 136; Article 239AB;
Indian Express Newspapers (1985) and Bennett Coleman; section 218 of the BNSS; sections 3, 4 and 6(2) of the RTI
Act; eGramSwaraj, Gram Manchitra, RGSA and Meri Panchayat; Articles 92 and 119; the Lok Sabha's Committees on
Absence of Members, Private Members' Bills and Rules; the Advocates (Amendment) Act, 2023; Articles 53(3) and 154.
MCQ keys are pinned (pos)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from ca_common import combo, MX
from bilingual import combo_hi

d.SUBJECT = "Polity"
d.REQUIRE_CRAFT = True
COI = "Constitution of India"

def SC(topic, diff, body, body_hi, st, st_hi, truth, pos, expl, expl_hi, cite, cg, craft, closing=None, closing_hi=None):
    """A combination-code statement item (the 2026 form): truth marks the correct statements; pos is the key's slot."""
    opts = combo(truth, pos)
    S(topic, diff, body, body_hi, st, st_hi, None, pos, expl, expl_hi, cite, cg, opts=opts, opts_hi=[combo_hi(o) for o in opts],
      craft=craft, closing=closing, closing_hi=closing_hi)

# ---------------------------------------------------------------- Constitutional & Statutory Bodies (statement, hard)
SC("Constitutional & Statutory Bodies", "hard", "With reference to the Director of Enforcement, consider the following statements:",
   "प्रवर्तन निदेशक के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
   ["The Director is appointed on the recommendation of a committee chaired by the Central Vigilance Commissioner.",
    "In Jaya Thakur (2023), the Supreme Court struck down the law that allows the Director's tenure to be extended.",
    "The Director holds office for a period of not less than two years.",
    "The tenure may be extended, by up to a year at a time, to a total of five years."],
   ["निदेशक की नियुक्ति केंद्रीय सतर्कता आयुक्त की अध्यक्षता वाली एक समिति की संस्तुति पर होती है।",
    "जया ठाकुर (2023) में सर्वोच्च न्यायालय ने निदेशक का कार्यकाल बढ़ाने देने वाली विधि को रद्द कर दिया।",
    "निदेशक कम से कम दो वर्ष की अवधि के लिए पद धारण करते हैं।",
    "कार्यकाल को एक बार में अधिकतम एक वर्ष करके, कुल पाँच वर्ष तक बढ़ाया जा सकता है।"],
   (1, 0, 1, 1), 3,
   "Statements 1, 3 and 4 are correct. Section 25 of the Central Vigilance Commission Act, 2003 provides that the Director of Enforcement is appointed on the recommendation of a committee headed by the Central Vigilance Commissioner, with the Vigilance Commissioners and the Secretaries of the Ministry of Home Affairs, the Department of Personnel and the Department of Revenue, and that the Director holds office for not less than two years -- safeguards for an agency that investigates money laundering and foreign-exchange offences. An amendment of 2021 allowed the tenure to be extended in the public interest by up to one year at a time, to a total of five years, as for the Director of the CBI. "
   "Statement 2 is wrong: in Jaya Thakur (2023) the Supreme Court upheld the amendment, but held the later extensions given to the then Director invalid, because in Common Cause (2021) it had already directed that he should get no further extension; it allowed him to stay briefly for an orderly handover. The case shows the Court protecting the independence of investigating agencies through limits on tenure rather than by striking down the law.",
   "केवल कथन 1, 3 और 4 सही हैं। केंद्रीय सतर्कता आयोग अधिनियम, 2003 की धारा 25 प्रावधान करती है कि प्रवर्तन निदेशक की नियुक्ति केंद्रीय सतर्कता आयुक्त की अध्यक्षता वाली समिति की संस्तुति पर होती है, जिसमें सतर्कता आयुक्त और गृह मंत्रालय, कार्मिक विभाग तथा राजस्व विभाग के सचिव होते हैं, और कि निदेशक कम से कम दो वर्ष पद धारण करते हैं -- धन-शोधन और विदेशी मुद्रा अपराधों की जाँच करने वाली एजेंसी के लिए सुरक्षा-उपाय। 2021 के एक संशोधन ने लोकहित में कार्यकाल को एक बार में अधिकतम एक वर्ष करके, कुल पाँच वर्ष तक बढ़ाने की अनुमति दी, जैसा सीबीआई निदेशक के लिए है। "
   "कथन 2 ग़लत है: जया ठाकुर (2023) में सर्वोच्च न्यायालय ने संशोधन को बरक़रार रखा, पर तत्कालीन निदेशक को दिए गए बाद के विस्तारों को अमान्य ठहराया, क्योंकि कॉमन कॉज़ (2021) में वह पहले ही निर्देश दे चुका था कि उन्हें आगे कोई विस्तार न दिया जाए; उसने व्यवस्थित हस्तांतरण के लिए उन्हें थोड़े समय रहने दिया। यह मामला दिखाता है कि न्यायालय ने विधि को रद्द करने के बजाय कार्यकाल की सीमाओं के माध्यम से जाँच एजेंसियों की स्वतंत्रता की रक्षा की।",
   "Central Vigilance Commission Act, 2003, section 25 (as amended in 2021); Common Cause v. Union of India (2021); Dr. Jaya Thakur v. Union of India (2023).",
   "l4-s03-pol-director-of-enforcement-cvc-act-25-jaya-thakur", "precision")

# ---------------------------------------------------------------- Constitutional Framework (MCQ, medium)
M("Constitutional Framework", "medium",
  "Articles 32A, 131A, 144A and 226A, which the Forty-second Amendment had inserted to limit the power of the courts to examine the validity of laws, were omitted by the",
  "अनुच्छेद 32क, 131क, 144क और 226क, जिन्हें बयालीसवें संशोधन ने विधियों की वैधता की जाँच करने की न्यायालयों की शक्ति सीमित करने के लिए जोड़ा था, किसके द्वारा हटाए गए?",
  ["Forty-third Amendment Act, 1977", "Forty-fourth Amendment Act, 1978", "Forty-fifth Amendment Act, 1980", "Fifty-second Amendment Act, 1985"],
  ["तैंतालीसवें संशोधन अधिनियम, 1977", "चौवालीसवें संशोधन अधिनियम, 1978", "पैंतालीसवें संशोधन अधिनियम, 1980", "बावनवें संशोधन अधिनियम, 1985"],
  0,
  "During the Emergency the Forty-second Amendment (1976) inserted Article 32A (the Supreme Court not to consider the validity of State laws in writ proceedings unless a central law was also challenged), Article 131A (exclusive Supreme Court jurisdiction over the validity of central laws), Article 144A (at least seven judges and a two-thirds majority to strike down a law) and Article 226A (High Courts barred from deciding the validity of central laws). The Forty-third Amendment, passed by the Janata Government at the end of 1977, omitted all of them, restoring the courts' powers. "
  "The Forty-fourth Amendment (1978) undid other parts of the Forty-second -- replacing 'internal disturbance' with 'armed rebellion' as a ground for Emergency and making the right to property a legal right under Article 300A; the Forty-fifth (1980) extended the reservation of seats for Scheduled Castes and Scheduled Tribes; and the Fifty-second (1985) added the anti-defection Tenth Schedule.",
  "आपातकाल के दौरान बयालीसवें संशोधन (1976) ने अनुच्छेद 32क (रिट कार्यवाहियों में सर्वोच्च न्यायालय राज्य विधियों की वैधता पर विचार न करे जब तक किसी केंद्रीय विधि को भी चुनौती न दी गई हो), अनुच्छेद 131क (केंद्रीय विधियों की वैधता पर सर्वोच्च न्यायालय की अनन्य अधिकारिता), अनुच्छेद 144क (किसी विधि को रद्द करने के लिए कम से कम सात न्यायाधीश और दो-तिहाई बहुमत) और अनुच्छेद 226क (उच्च न्यायालयों को केंद्रीय विधियों की वैधता तय करने से रोक) जोड़े। 1977 के अंत में जनता सरकार द्वारा पारित तैंतालीसवें संशोधन ने इन सभी को हटाकर न्यायालयों की शक्तियाँ बहाल कीं। "
  "चौवालीसवें संशोधन (1978) ने बयालीसवें के अन्य भागों को पलटा -- आपातकाल के आधार के रूप में 'आंतरिक अशांति' के स्थान पर 'सशस्त्र विद्रोह' रखा और संपत्ति के अधिकार को अनुच्छेद 300क के अंतर्गत विधिक अधिकार बनाया; पैंतालीसवें (1980) ने अनुसूचित जातियों और जनजातियों के लिए सीटों का आरक्षण बढ़ाया; और बावनवें (1985) ने दल-बदल विरोधी दसवीं अनुसूची जोड़ी।",
  COI + "; Constitution (Forty-second Amendment) Act, 1976; Constitution (Forty-third Amendment) Act, 1977; Constitution (Forty-fourth Amendment) Act, 1978.",
  "l4-s03-pol-43rd-amendment-omits-32a-131a-144a-226a", pos=0, craft="precision")

# ---------------------------------------------------------------- Constitutional Framework (statement, medium)
SC("Constitutional Framework", "medium", "With reference to the appellate jurisdiction of the Supreme Court, consider the following statements:",
   "सर्वोच्च न्यायालय की अपीलीय अधिकारिता के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
   ["Special leave to appeal under Article 136 cannot be granted against an order of a tribunal.",
    "In a civil case, an appeal lies only if the High Court certifies that the case involves a substantial question of law of general importance that needs to be decided by the Supreme Court.",
    "In a criminal case, an appeal lies as of right where the High Court, on appeal, has reversed an acquittal and sentenced the accused to death."],
   ["अनुच्छेद 136 के अंतर्गत किसी अधिकरण के आदेश के विरुद्ध अपील की विशेष अनुमति नहीं दी जा सकती।",
    "दीवानी मामले में अपील तभी होती है जब उच्च न्यायालय प्रमाणित करे कि मामले में सामान्य महत्त्व का ऐसा सारवान विधि-प्रश्न है जिसका निर्णय सर्वोच्च न्यायालय द्वारा होना आवश्यक है।",
    "आपराधिक मामले में अपील अधिकार के रूप में होती है जहाँ उच्च न्यायालय ने अपील में दोषमुक्ति को उलटकर अभियुक्त को मृत्युदंड दिया हो।"],
   (0, 1, 1), 1,
   "Only statements 2 and 3 are correct. Under Article 133, as amended by the Thirtieth Amendment (1972), which removed the old test of the value of the suit, a civil appeal lies only on a certificate under Article 134A that the case raises a substantial question of law of general importance needing the Supreme Court's decision. Article 134(1) gives an appeal as of right in two kinds of death-sentence cases -- where the High Court on appeal reverses an acquittal and sentences the accused to death, or withdraws a case to itself and sentences the accused to death -- and otherwise needs a certificate. "
   "Statement 1 is wrong: Article 136 lets the Court grant special leave to appeal from any judgment, decree, sentence or order passed by any court or tribunal in India, except a court or tribunal constituted under a law relating to the armed forces. It is a wide, discretionary power, which the Court says it uses only where grave injustice or a substantial question of law is shown -- yet it now generates most of the Court's workload.",
   "केवल कथन 2 और 3 सही हैं। तीसवें संशोधन (1972) द्वारा संशोधित अनुच्छेद 133 के अंतर्गत, जिसने वाद के मूल्य की पुरानी कसौटी हटा दी, दीवानी अपील केवल अनुच्छेद 134क के अंतर्गत इस प्रमाणपत्र पर होती है कि मामले में सामान्य महत्त्व का ऐसा सारवान विधि-प्रश्न है जिस पर सर्वोच्च न्यायालय का निर्णय आवश्यक है। अनुच्छेद 134(1) मृत्युदंड के दो प्रकार के मामलों में अधिकार के रूप में अपील देता है -- जहाँ उच्च न्यायालय अपील में दोषमुक्ति उलटकर अभियुक्त को मृत्युदंड दे, या कोई मामला अपने पास मँगाकर अभियुक्त को मृत्युदंड दे -- और अन्यथा प्रमाणपत्र अपेक्षित करता है। "
   "कथन 1 ग़लत है: अनुच्छेद 136 न्यायालय को भारत में किसी भी न्यायालय या अधिकरण द्वारा पारित किसी भी निर्णय, डिक्री, दंडादेश या आदेश से अपील की विशेष अनुमति देने देता है, सिवाय सशस्त्र बलों से संबंधित किसी विधि के अंतर्गत गठित न्यायालय या अधिकरण के। यह एक व्यापक, विवेकाधीन शक्ति है, जिसका प्रयोग न्यायालय कहता है कि वह केवल गंभीर अन्याय या सारवान विधि-प्रश्न दिखाए जाने पर करता है -- फिर भी अब इसी से न्यायालय का अधिकांश कार्यभार बनता है।",
   COI + ", Articles 132-134A and 136; Constitution (Thirtieth Amendment) Act, 1972.",
   "l4-s03-pol-sc-appellate-133-134-136-tribunals", "precision")

# ---------------------------------------------------------------- Federalism & Special Provisions (statement, medium)
SC("Federalism & Special Provisions", "medium", "With reference to the National Capital Territory of Delhi, consider the following statements:",
   "दिल्ली राष्ट्रीय राजधानी राज्यक्षेत्र के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
   ["Under Article 239AB, the President may suspend the operation of any provision of Article 239AA if the administration of the territory cannot be carried on in accordance with it.",
    "The Legislative Assembly of Delhi can make laws on police and public order.",
    "If the Lieutenant Governor and the ministers differ on any matter, the Lieutenant Governor refers it to the President, and may act on his own in urgent cases until the President decides."],
   ["अनुच्छेद 239कख के अंतर्गत, यदि राज्यक्षेत्र का प्रशासन अनुच्छेद 239कक के अनुसार नहीं चलाया जा सकता, तो राष्ट्रपति उसके किसी भी प्रावधान का प्रवर्तन निलंबित कर सकते हैं।",
    "दिल्ली की विधान सभा पुलिस और लोक व्यवस्था पर विधि बना सकती है।",
    "यदि उपराज्यपाल और मंत्रियों में किसी विषय पर मतभेद हो, तो उपराज्यपाल उसे राष्ट्रपति को भेजते हैं, और राष्ट्रपति के निर्णय तक अत्यावश्यक मामलों में स्वयं कार्य कर सकते हैं।"],
   (1, 0, 1), 2,
   "Only statements 1 and 3 are correct. The Sixty-ninth Amendment (1991) gave Delhi a Legislative Assembly and a Council of Ministers through Article 239AA, and added Article 239AB, Delhi's counterpart of Article 356: on a report from the Lieutenant Governor or otherwise, the President may suspend any provision of Article 239AA or of the law made under it, if the territory cannot be governed in accordance with them. The proviso to Article 239AA(4) lets the Lieutenant Governor refer a difference with the ministers to the President and act meanwhile in urgent cases; in 2018 the Supreme Court read it as meant for exceptional matters, not every disagreement. "
   "Statement 2 is wrong: Article 239AA(3)(a) excludes public order, police and land (entries 1, 2 and 18 of the State List) from the Assembly's power. The long contest over who controls Delhi's administration went on to the Court's 2023 ruling on services and Parliament's law of the same year.",
   "केवल कथन 1 और 3 सही हैं। उनहत्तरवें संशोधन (1991) ने अनुच्छेद 239कक के माध्यम से दिल्ली को विधान सभा और मंत्रिपरिषद दी, और अनुच्छेद 239कख जोड़ा, जो अनुच्छेद 356 का दिल्ली रूप है: उपराज्यपाल के प्रतिवेदन पर या अन्यथा, यदि राज्यक्षेत्र का शासन अनुच्छेद 239कक या उसके अंतर्गत बनी विधि के अनुसार न चल सके, तो राष्ट्रपति उसके किसी भी प्रावधान को निलंबित कर सकते हैं। अनुच्छेद 239कक(4) का परंतुक उपराज्यपाल को मंत्रियों से मतभेद राष्ट्रपति को भेजने और इस बीच अत्यावश्यक मामलों में कार्य करने देता है; 2018 में सर्वोच्च न्यायालय ने इसे हर मतभेद के लिए नहीं, असाधारण विषयों के लिए माना। "
   "कथन 2 ग़लत है: अनुच्छेद 239कक(3)(क) लोक व्यवस्था, पुलिस और भूमि (राज्य सूची की प्रविष्टियाँ 1, 2 और 18) को विधान सभा की शक्ति से बाहर रखता है। दिल्ली के प्रशासन पर नियंत्रण की लंबी खींचतान सेवाओं पर न्यायालय के 2023 के निर्णय और उसी वर्ष संसद की विधि तक पहुँची।",
   COI + ", Articles 239AA and 239AB; Constitution (Sixty-ninth Amendment) Act, 1991; Government of NCT of Delhi v. Union of India (2018).",
   "l4-s03-pol-art239ab-delhi-suspension-lg-reference", "linkage")

# ---------------------------------------------------------------- Fundamental Rights, DPSP & Duties (statement, medium)
SC("Fundamental Rights, DPSP & Duties", "medium", "With reference to the freedom of the press, consider the following statements:",
   "प्रेस की स्वतंत्रता के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
   ["In Indian Express Newspapers (1985), the Supreme Court held that newspapers are not immune from taxation.",
    "The same judgment held that a tax so heavy that it curtails circulation can violate the freedom of speech and expression.",
    "In Bennett Coleman (1972), the Court upheld a newsprint policy that limited the number of pages a newspaper could print."],
   ["इंडियन एक्सप्रेस न्यूज़पेपर्स (1985) में सर्वोच्च न्यायालय ने कहा कि समाचार पत्र कराधान से मुक्त नहीं हैं।",
    "उसी निर्णय ने कहा कि इतना भारी कर जो प्रसार घटा दे, वाक् और अभिव्यक्ति की स्वतंत्रता का उल्लंघन कर सकता है।",
    "बेनेट कोलमैन (1972) में न्यायालय ने उस अख़बारी काग़ज़ नीति को बरक़रार रखा जिसने समाचार पत्र द्वारा छापे जा सकने वाले पृष्ठों की संख्या सीमित की।"],
   (1, 1, 0), 0,
   "Only statements 1 and 2 are correct. Freedom of the press is not named in Article 19(1)(a) but is part of the freedom of speech and expression. In Indian Express Newspapers (1985), on the import duty on newsprint, the Court held that newspapers must pay taxes like any business, but that a levy which, by its weight, curbs circulation or the spread of ideas can be struck down; it asked the Government to reconsider the duty. "
   "Statement 3 is wrong: in Bennett Coleman (1972) the Court struck down the parts of the newsprint control policy that fixed the maximum number of pages and barred new editions, rejecting the argument that they were only economic regulation -- limiting pages limits the circulation of news and views. The line from these cases is that indirect controls on the means of publishing are tested as restrictions on speech, and must fit the grounds in Article 19(2).",
   "केवल कथन 1 और 2 सही हैं। प्रेस की स्वतंत्रता का अनुच्छेद 19(1)(क) में नाम नहीं है, पर यह वाक् और अभिव्यक्ति की स्वतंत्रता का भाग है। अख़बारी काग़ज़ पर आयात शुल्क से जुड़े इंडियन एक्सप्रेस न्यूज़पेपर्स (1985) में न्यायालय ने कहा कि समाचार पत्रों को किसी भी व्यवसाय की तरह कर देने होंगे, पर जो शुल्क अपने भार से प्रसार या विचारों के प्रचार को रोके उसे रद्द किया जा सकता है; उसने सरकार से शुल्क पर पुनर्विचार करने को कहा। "
   "कथन 3 ग़लत है: बेनेट कोलमैन (1972) में न्यायालय ने अख़बारी काग़ज़ नियंत्रण नीति के उन भागों को रद्द किया जो पृष्ठों की अधिकतम संख्या तय करते और नए संस्करणों पर रोक लगाते थे, इस तर्क को अस्वीकार करते हुए कि वे केवल आर्थिक विनियमन थे -- पृष्ठ सीमित करना समाचारों और विचारों का प्रसार सीमित करना है। इन मामलों से निकली दिशा यह है कि प्रकाशन के साधनों पर अप्रत्यक्ष नियंत्रणों को वाक् पर प्रतिबंध के रूप में परखा जाता है, और उन्हें अनुच्छेद 19(2) के आधारों में बैठना होगा।",
   COI + ", Article 19(1)(a) and (2); Bennett Coleman and Co. v. Union of India (1972); Indian Express Newspapers v. Union of India (1985).",
   "l4-s03-pol-press-freedom-indian-express-bennett-coleman", "precision")

# ---------------------------------------------------------------- Governance (MCQ, hard)
M("Governance", "hard",
  "Under the Bharatiya Nagarik Suraksha Sanhita, 2023, if the government does not decide on a request for sanction to prosecute a public servant for an act done in the discharge of official duty,",
  "भारतीय नागरिक सुरक्षा संहिता, 2023 के अंतर्गत, यदि सरकार किसी लोक सेवक के विरुद्ध पदीय कर्तव्य के निर्वहन में किए गए कार्य के लिए अभियोजन की स्वीकृति के अनुरोध पर निर्णय नहीं लेती, तो",
  ["the sanction is deemed to have been given after 120 days",
   "the request lapses after 90 days and must be made again by the court",
   "the matter goes to the Lokpal, whose decision on the sanction is final",
   "the court may take cognizance only with the leave of the High Court"],
  ["120 दिन के बाद स्वीकृति दी गई मानी जाती है",
   "अनुरोध 90 दिन बाद व्यपगत हो जाता है और न्यायालय को उसे फिर से करना पड़ता है",
   "मामला लोकपाल के पास जाता है, जिसका स्वीकृति पर निर्णय अंतिम होता है",
   "न्यायालय केवल उच्च न्यायालय की अनुमति से ही संज्ञान ले सकता है"],
  0,
  "Section 218 of the BNSS, which replaced section 197 of the Code of Criminal Procedure, keeps the rule that a court cannot take cognizance of an offence alleged against a judge or a public servant removable only by the government, for an act done in the discharge of official duty, without the government's previous sanction. Its new second proviso requires the government to decide within 120 days of receiving the request, and says that if it fails to do so the sanction shall be deemed to have been accorded -- a provision the old Code did not have, meant to end indefinite delays that shielded officials. "
  "This sanction to prosecute is distinct from the prior approval needed to begin an investigation under section 17A of the Prevention of Corruption Act. Courts are still working out how the deemed sanction is to be applied in individual cases.",
  "बीएनएसएस की धारा 218, जिसने दंड प्रक्रिया संहिता की धारा 197 का स्थान लिया, यह नियम बनाए रखती है कि कोई न्यायालय किसी न्यायाधीश या केवल सरकार द्वारा हटाए जा सकने वाले लोक सेवक के विरुद्ध, पदीय कर्तव्य के निर्वहन में किए गए कार्य के लिए आरोपित अपराध का संज्ञान सरकार की पूर्व स्वीकृति के बिना नहीं ले सकता। इसका नया दूसरा परंतुक सरकार से अनुरोध प्राप्त होने के 120 दिन के भीतर निर्णय लेने की अपेक्षा करता है, और कहता है कि ऐसा न करने पर स्वीकृति दी गई मानी जाएगी -- ऐसा प्रावधान जो पुरानी संहिता में नहीं था, और जिसका उद्देश्य अधिकारियों को बचाने वाले अनिश्चित विलंब को समाप्त करना है। "
  "अभियोजन की यह स्वीकृति भ्रष्टाचार निवारण अधिनियम की धारा 17क के अंतर्गत जाँच आरंभ करने के लिए आवश्यक पूर्व अनुमोदन से अलग है। न्यायालय अभी यह तय कर रहे हैं कि अलग-अलग मामलों में मानी गई स्वीकृति को कैसे लागू किया जाए।",
  "Bharatiya Nagarik Suraksha Sanhita, 2023, section 218; Code of Criminal Procedure, 1973, section 197; Prevention of Corruption Act, 1988, section 17A.",
  "l4-s03-pol-bnss-218-deemed-sanction-120-days", pos=3, craft="precision")

# ---------------------------------------------------------------- Governance (statement, medium)
SC("Governance", "medium", "With reference to the Right to Information Act, 2005, consider the following statements:",
   "सूचना का अधिकार अधिनियम, 2005 के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
   ["Only persons resident in the State where a public authority is located may seek information from it.",
    "Every public authority must publish, on its own, particulars of its organisation, functions and duties and the powers of its officers.",
    "A person seeking information is not required to give any reason for the request."],
   ["केवल उस राज्य के निवासी ही किसी लोक प्राधिकारी से सूचना माँग सकते हैं जिसमें वह स्थित है।",
    "हर लोक प्राधिकारी को अपने संगठन, कार्यों और कर्तव्यों तथा अपने अधिकारियों की शक्तियों का विवरण स्वयं प्रकाशित करना होता है।",
    "सूचना माँगने वाले व्यक्ति को अनुरोध का कोई कारण बताने की आवश्यकता नहीं है।"],
   (0, 1, 1), 2,
   "Only statements 2 and 3 are correct. Section 4(1)(b) lists particulars that every public authority must publish on its own -- its organisation and functions, the powers and duties of its officers, its decision-making procedure, norms, rules and manuals, budgets, the details of its subsidy programmes and the names of its information officers -- and section 4(2) asks it to keep disclosing so much that the public need use the Act as little as possible. Section 6(2) says an applicant need not give any reason for the request or any personal details except those needed to contact him. "
   "Statement 1 is wrong: section 3 gives the right to all citizens, wherever they live, so a citizen in Kerala can seek information from a body in Assam. Weak compliance with section 4 is one reason so many applications are filed for information that should already be public.",
   "केवल कथन 2 और 3 सही हैं। धारा 4(1)(ख) वे विवरण गिनाती है जो हर लोक प्राधिकारी को स्वयं प्रकाशित करने होते हैं -- उसका संगठन और कार्य, उसके अधिकारियों की शक्तियाँ और कर्तव्य, उसकी निर्णय-प्रक्रिया, मानदंड, नियम और नियमावलियाँ, बजट, उसकी सब्सिडी योजनाओं के विवरण और उसके सूचना अधिकारियों के नाम -- और धारा 4(2) उससे इतना प्रकटीकरण करते रहने को कहती है कि जनता को अधिनियम का यथासंभव कम उपयोग करना पड़े। धारा 6(2) कहती है कि आवेदक को अनुरोध का कोई कारण या उससे संपर्क के लिए आवश्यक विवरण के अलावा कोई निजी विवरण देने की आवश्यकता नहीं है। "
   "कथन 1 ग़लत है: धारा 3 यह अधिकार सभी नागरिकों को देती है, वे कहीं भी रहते हों, इसलिए केरल का कोई नागरिक असम के किसी निकाय से सूचना माँग सकता है। धारा 4 का कमज़ोर पालन एक कारण है कि इतने आवेदन ऐसी सूचना के लिए दायर होते हैं जो पहले से सार्वजनिक होनी चाहिए थी।",
   "Right to Information Act, 2005, sections 3, 4 and 6.",
   "l4-s03-pol-rti-section-3-4-6-2-proactive-no-reasons", "precision")

# ---------------------------------------------------------------- Panchayati Raj & Local Governance (List-I/List-II, easy)
MX("Panchayati Raj & Local Governance", "easy", "Match List-I (digital tool or programme for panchayats) with List-II (its main purpose):",
   "सूची-I (पंचायतों के लिए डिजिटल साधन या कार्यक्रम) को सूची-II (उसका मुख्य उद्देश्य) से सुमेलित कीजिए:",
   ["eGramSwaraj", "Gram Manchitra", "Rashtriya Gram Swaraj Abhiyan", "Meri Panchayat"],
   ["ई-ग्रामस्वराज", "ग्राम मानचित्र", "राष्ट्रीय ग्राम स्वराज अभियान", "मेरी पंचायत"],
   ["Capacity building and training of elected representatives of panchayats",
    "Online planning, accounting and payments of panchayats",
    "Citizens' access to information about their panchayat on a mobile phone",
    "Map-based spatial planning of gram panchayat development plans"],
   ["पंचायतों के निर्वाचित प्रतिनिधियों का क्षमता-निर्माण और प्रशिक्षण",
    "पंचायतों की ऑनलाइन योजना, लेखांकन और भुगतान",
    "मोबाइल फ़ोन पर नागरिकों की अपनी पंचायत संबंधी सूचना तक पहुँच",
    "ग्राम पंचायत विकास योजनाओं की मानचित्र-आधारित स्थानिक योजना"],
   [2, 4, 1, 3], 1,
   "The correct code is A-2, B-4, C-1, D-3. These are tools of the Ministry of Panchayati Raj. eGramSwaraj is a single work-based application through which panchayats prepare their plans, keep accounts and make payments, linked to the Public Financial Management System so that funds can be tracked. Gram Manchitra is a geographic information system application that lets panchayats plan works on maps, showing assets, resources and needs, as part of the Gram Panchayat Development Plan. "
   "The Rashtriya Gram Swaraj Abhiyan funds the training and capacity building of elected representatives and functionaries, and some infrastructure, so that panchayats can use the powers devolved to them. Meri Panchayat is a mobile application for citizens, showing their panchayat's budgets, works and services, which supports social audit and accountability.",
   "सही कूट क-2, ख-4, ग-1, घ-3 है। ये पंचायती राज मंत्रालय के साधन हैं। ई-ग्रामस्वराज एक एकल कार्य-आधारित अनुप्रयोग है जिसके माध्यम से पंचायतें अपनी योजनाएँ बनाती हैं, लेखे रखती हैं और भुगतान करती हैं, और जो लोक वित्तीय प्रबंधन प्रणाली से जुड़ा है ताकि धन पर नज़र रखी जा सके। ग्राम मानचित्र एक भौगोलिक सूचना प्रणाली अनुप्रयोग है जो पंचायतों को ग्राम पंचायत विकास योजना के भाग के रूप में मानचित्रों पर, परिसंपत्तियाँ, संसाधन और आवश्यकताएँ दिखाते हुए, कार्यों की योजना बनाने देता है। "
   "राष्ट्रीय ग्राम स्वराज अभियान निर्वाचित प्रतिनिधियों और कर्मियों के प्रशिक्षण और क्षमता-निर्माण, और कुछ अवसंरचना, के लिए धन देता है, ताकि पंचायतें उन्हें सौंपी गई शक्तियों का उपयोग कर सकें। मेरी पंचायत नागरिकों के लिए एक मोबाइल अनुप्रयोग है, जो उनकी पंचायत के बजट, कार्य और सेवाएँ दिखाता है, और सामाजिक अंकेक्षण तथा उत्तरदायित्व में सहायक है।",
   "Ministry of Panchayati Raj, Annual Report; eGramSwaraj, Gram Manchitra and Meri Panchayat portals; Rashtriya Gram Swaraj Abhiyan guidelines.",
   "l4-s03-pol-egramswaraj-gram-manchitra-rgsa-meri-panchayat", "recall")

# ---------------------------------------------------------------- Parliament & State Legislature (statement, hard)
SC("Parliament & State Legislature", "hard", "With reference to the Rajya Sabha and the procedure of Parliament, consider the following statements:",
   "राज्य सभा और संसद की प्रक्रिया के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
   ["While a resolution for the removal of the Vice-President is under consideration, the Deputy Chairman presides over the Rajya Sabha.",
    "During that time the Chairman may speak and take part in the proceedings, but cannot vote at all, even in the first instance.",
    "A resolution for the removal of the Vice-President can be moved in the Rajya Sabha without any prior notice.",
    "Parliament may by law regulate the procedure for its financial business, and such a law prevails over the rules of either House."],
   ["जब उपराष्ट्रपति को हटाने का संकल्प विचाराधीन हो, तब राज्य सभा की अध्यक्षता उपसभापति करते हैं।",
    "उस दौरान सभापति बोल सकते हैं और कार्यवाही में भाग ले सकते हैं, पर पहली बार में भी मत बिल्कुल नहीं दे सकते।",
    "उपराष्ट्रपति को हटाने का संकल्प राज्य सभा में बिना किसी पूर्व सूचना के प्रस्तुत किया जा सकता है।",
    "संसद विधि द्वारा अपने वित्तीय कार्य की प्रक्रिया को विनियमित कर सकती है, और ऐसी विधि किसी भी सदन के नियमों पर अभिभावी होती है।"],
   (1, 1, 0, 1), 1,
   "Statements 1, 2 and 4 are correct. Under Article 92(1) the Chairman does not preside while a resolution to remove the Vice-President is under consideration; the Deputy Chairman, or another person under the rules, does. Article 92(2) lets the Chairman speak and take part, but says that he shall not be entitled to vote at all on the resolution or any other matter during those proceedings -- unlike the Speaker under Article 96, who may vote in the first instance, because the Speaker is a member of the House and the Vice-President is not a member of the Rajya Sabha. "
   "Statement 3 is wrong: Article 67(b) requires at least fourteen days' notice of the intention to move the resolution. Article 119 lets Parliament regulate by law the procedure of financial business for its timely completion, and says that such a law prevails over the rules each House makes under Article 118; Parliament has so far relied on its rules instead.",
   "केवल कथन 1, 2 और 4 सही हैं। अनुच्छेद 92(1) के अंतर्गत जब उपराष्ट्रपति को हटाने का संकल्प विचाराधीन हो तब सभापति अध्यक्षता नहीं करते; उपसभापति, या नियमों के अनुसार कोई अन्य व्यक्ति, करता है। अनुच्छेद 92(2) सभापति को बोलने और भाग लेने देता है, पर कहता है कि उस कार्यवाही में संकल्प या किसी अन्य विषय पर उन्हें मत देने का बिल्कुल अधिकार नहीं होगा -- अनुच्छेद 96 के अंतर्गत अध्यक्ष के विपरीत, जो पहली बार में मत दे सकते हैं, क्योंकि अध्यक्ष सदन के सदस्य होते हैं और उपराष्ट्रपति राज्य सभा के सदस्य नहीं होते। "
   "कथन 3 ग़लत है: अनुच्छेद 67(ख) संकल्प प्रस्तुत करने के आशय की कम से कम चौदह दिन की सूचना अपेक्षित करता है। अनुच्छेद 119 संसद को समय पर पूरा करने के लिए वित्तीय कार्य की प्रक्रिया विधि द्वारा विनियमित करने देता है, और कहता है कि ऐसी विधि अनुच्छेद 118 के अंतर्गत हर सदन द्वारा बनाए गए नियमों पर अभिभावी होगी; संसद अब तक इसके बजाय अपने नियमों पर निर्भर रही है।",
   COI + ", Articles 67(b), 92, 96, 118 and 119.",
   "l4-s03-pol-art92-chairman-no-vote-art119-financial-business", "linkage")

# ---------------------------------------------------------------- Parliament & State Legislature (statement, medium)
SC("Parliament & State Legislature", "medium", "With reference to the committees of the Lok Sabha, consider the following statements:",
   "लोक सभा की समितियों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
   ["The Committee on Absence of Members considers the applications of members for leave of absence from the sittings of the House.",
    "The Committee on Private Members' Bills and Resolutions is a committee of the Rajya Sabha alone.",
    "The Rules Committee of the Lok Sabha is chaired by the Speaker."],
   ["सदस्यों की अनुपस्थिति संबंधी समिति सदन की बैठकों से अनुपस्थिति की अनुमति के लिए सदस्यों के आवेदनों पर विचार करती है।",
    "ग़ैर-सरकारी सदस्यों के विधेयकों और संकल्पों संबंधी समिति केवल राज्य सभा की समिति है।",
    "लोक सभा की नियम समिति की अध्यक्षता अध्यक्ष करते हैं।"],
   (1, 0, 1), 0,
   "Only statements 1 and 3 are correct. Article 101(4) says a member's seat may be declared vacant if he is absent from all meetings of the House for sixty days without its permission; in the Lok Sabha the Committee on Absence of Members examines members' applications for leave and cases of absence, and recommends whether leave should be granted. The Rules Committee, which considers changes to the Rules of Procedure, is chaired by the Speaker, as the Rajya Sabha's is by its Chairman. "
   "Statement 2 is wrong: the Committee on Private Members' Bills and Resolutions is a Lok Sabha committee, presided over by the Deputy Speaker; it classifies private members' Bills by their urgency and importance and allots time to them and to private members' resolutions. Such smaller committees do much of the routine work through which the House manages its own business.",
   "केवल कथन 1 और 3 सही हैं। अनुच्छेद 101(4) कहता है कि यदि कोई सदस्य सदन की अनुमति के बिना साठ दिन तक उसकी सभी बैठकों से अनुपस्थित रहे तो उसका स्थान रिक्त घोषित किया जा सकता है; लोक सभा में सदस्यों की अनुपस्थिति संबंधी समिति अनुमति के आवेदनों और अनुपस्थिति के मामलों की जाँच करती है, और संस्तुति करती है कि अनुमति दी जाए या नहीं। प्रक्रिया नियमों में परिवर्तनों पर विचार करने वाली नियम समिति की अध्यक्षता अध्यक्ष करते हैं, जैसे राज्य सभा की समिति की उसके सभापति। "
   "कथन 2 ग़लत है: ग़ैर-सरकारी सदस्यों के विधेयकों और संकल्पों संबंधी समिति लोक सभा की समिति है, जिसकी अध्यक्षता उपाध्यक्ष करते हैं; यह ग़ैर-सरकारी सदस्यों के विधेयकों को उनकी तात्कालिकता और महत्त्व के अनुसार वर्गीकृत करती है और उन्हें तथा ग़ैर-सरकारी सदस्यों के संकल्पों को समय आवंटित करती है। ऐसी छोटी समितियाँ बहुत-सा नियमित कार्य करती हैं जिससे सदन अपने कार्य का प्रबंध करता है।",
   COI + ", Article 101(4); Rules of Procedure and Conduct of Business in Lok Sabha; Lok Sabha Secretariat, Parliamentary Committees.",
   "l4-s03-pol-lok-sabha-committees-absence-pmbr-rules", "precision")

# ---------------------------------------------------------------- Statutory-Laws (statement, medium)
SC("Statutory-Laws", "medium", "With reference to the Advocates (Amendment) Act, 2023, consider the following statements:",
   "अधिवक्ता (संशोधन) अधिनियम, 2023 के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
   ["It repealed the Legal Practitioners Act, 1879.",
    "It empowers High Courts and district judges to frame and publish lists of touts.",
    "It allows foreign law firms to appear for clients in Indian courts."],
   ["इसने विधि व्यवसायी अधिनियम, 1879 को निरस्त किया।",
    "यह उच्च न्यायालयों और ज़िला न्यायाधीशों को दलालों (टाउट) की सूचियाँ बनाने और प्रकाशित करने का अधिकार देता है।",
    "यह विदेशी विधि फ़र्मों को भारतीय न्यायालयों में मुवक्किलों की ओर से उपस्थित होने देता है।"],
   (1, 1, 0), 3,
   "Only statements 1 and 2 are correct. As part of clearing out obsolete colonial laws, the 2023 Act repealed the Legal Practitioners Act, 1879, but carried its provision on touts -- people who procure clients for lawyers in return for payment -- into a new section 45A of the Advocates Act, 1961. Every High Court, district judge, sessions judge, district magistrate and certain revenue officers may frame and publish lists of touts, and anyone who acts as a tout while on such a list can be punished with imprisonment of up to three months, a fine of up to ₹500, or both. "
   "Statement 3 is wrong: the right to practise before courts belongs to advocates enrolled under the 1961 Act. Rules framed by the Bar Council of India from 2023 allow foreign lawyers and law firms, on a reciprocal basis, to advise on foreign and international law and on international arbitration, but not to appear in Indian courts.",
   "केवल कथन 1 और 2 सही हैं। अप्रचलित औपनिवेशिक विधियों को हटाने के भाग के रूप में 2023 के अधिनियम ने विधि व्यवसायी अधिनियम, 1879 को निरस्त किया, पर उसके दलालों -- जो भुगतान लेकर वकीलों के लिए मुवक्किल जुटाते हैं -- संबंधी प्रावधान को अधिवक्ता अधिनियम, 1961 की नई धारा 45क में ले आया। हर उच्च न्यायालय, ज़िला न्यायाधीश, सत्र न्यायाधीश, ज़िला मजिस्ट्रेट और कुछ राजस्व अधिकारी दलालों की सूचियाँ बना और प्रकाशित कर सकते हैं, और ऐसी सूची में रहते हुए दलाली करने वाले को तीन माह तक के कारावास, ₹500 तक के जुर्माने, या दोनों से दंडित किया जा सकता है। "
   "कथन 3 ग़लत है: न्यायालयों के समक्ष विधि-व्यवसाय का अधिकार 1961 के अधिनियम के अंतर्गत नामांकित अधिवक्ताओं का है। भारतीय विधिज्ञ परिषद द्वारा 2023 से बनाए गए नियम विदेशी वकीलों और विधि फ़र्मों को, पारस्परिकता के आधार पर, विदेशी और अंतरराष्ट्रीय विधि तथा अंतरराष्ट्रीय मध्यस्थता पर परामर्श देने देते हैं, पर भारतीय न्यायालयों में उपस्थित होने नहीं।",
   "Advocates (Amendment) Act, 2023; Advocates Act, 1961, section 45A; Bar Council of India Rules for Registration and Regulation of Foreign Lawyers and Foreign Law Firms in India (2022, notified 2023).",
   "l4-s03-pol-advocates-amendment-2023-touts-1879-repeal", "precision")

# ---------------------------------------------------------------- Union & State Executive (AR, hard)
A("Union & State Executive", "hard",
  "A law made by a State Legislature can confer functions directly on authorities subordinate to the Governor, such as a District Magistrate.",
  "राज्य विधानमंडल द्वारा बनाई गई विधि राज्यपाल के अधीनस्थ प्राधिकारियों, जैसे ज़िला मजिस्ट्रेट, को सीधे कार्य सौंप सकती है।",
  "Article 154 vests the executive power of the State in the Governor, but provides that this does not prevent Parliament or the State Legislature from conferring functions by law on authorities subordinate to the Governor.",
  "अनुच्छेद 154 राज्य की कार्यपालिका शक्ति राज्यपाल में निहित करता है, पर प्रावधान करता है कि इससे संसद या राज्य विधानमंडल को विधि द्वारा राज्यपाल के अधीनस्थ प्राधिकारियों को कार्य सौंपने से नहीं रोका जाता।",
  0,
  "Both statements are correct, and Statement II explains Statement I. Article 154(1) vests the State's executive power in the Governor, to be exercised by him directly or through officers subordinate to him. Article 154(2) adds that this does not transfer to the Governor functions that an existing law gives to another authority, and does not prevent Parliament or the State Legislature from conferring functions by law on authorities subordinate to him. That is why statutes give powers directly to Collectors, District Magistrates, Commissioners and other officers, who exercise them under the law itself. "
   "Article 53(3) makes the same provision for the Union. And because the Governor generally acts on the advice of the Council of Ministers, as the Supreme Court held in Shamsher Singh (1974), the executive power vested in him is in practice exercised by the elected government.",
  "दोनों कथन सही हैं, और कथन II कथन I की व्याख्या करता है। अनुच्छेद 154(1) राज्य की कार्यपालिका शक्ति राज्यपाल में निहित करता है, जिसका प्रयोग वे स्वयं या अपने अधीनस्थ अधिकारियों के माध्यम से करते हैं। अनुच्छेद 154(2) जोड़ता है कि इससे किसी विद्यमान विधि द्वारा किसी अन्य प्राधिकारी को दिए गए कार्य राज्यपाल को हस्तांतरित नहीं होते, और संसद या राज्य विधानमंडल को विधि द्वारा उनके अधीनस्थ प्राधिकारियों को कार्य सौंपने से नहीं रोका जाता। इसी कारण क़ानून सीधे कलेक्टरों, ज़िला मजिस्ट्रेटों, आयुक्तों और अन्य अधिकारियों को शक्तियाँ देते हैं, जो उनका प्रयोग स्वयं विधि के अंतर्गत करते हैं। "
  "अनुच्छेद 53(3) संघ के लिए यही प्रावधान करता है। और क्योंकि राज्यपाल सामान्यतः मंत्रिपरिषद की सलाह पर कार्य करते हैं, जैसा सर्वोच्च न्यायालय ने शमशेर सिंह (1974) में कहा, इसलिए उनमें निहित कार्यपालिका शक्ति का प्रयोग व्यवहार में निर्वाचित सरकार करती है।",
  COI + ", Articles 53(3) and 154; Shamsher Singh v. State of Punjab (1974).",
  "l4-s03-pol-art154-functions-on-subordinate-authorities", craft="linkage")

write("gs_l4_s03_a.sql")
