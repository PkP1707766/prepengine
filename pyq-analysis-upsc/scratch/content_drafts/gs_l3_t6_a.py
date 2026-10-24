# -*- coding: utf-8 -*-
"""Level 3 · Test 6 (GS Integrated Test 6) -- part A: Polity (15) (upsc_l3_cell_targets.mjs 6).
Same cell plan as Tests 1-5.
Every fact was searched in the whole UPSC bank (l3_tools/bank_find.py) and is one no row tests: Sukanya Shantha,
Satender Kumar Antil, the coal-block case and Swiss Ribbons; Article 274; the Keralam resolutions, the 2020 merger
of Dadra and Nagar Haveli and Daman and Diu, and Orissa's renaming; the Judges (Inquiry) Act and the 2025 committee;
curative petitions; Article 213; Article 357; the new Parliament building and Samvidhan Sadan; the Cinematograph
(Amendment) Act, 2023; rotation of reserved chairpersons' offices under Article 243D(4); the model bye-laws for
PACS; qualifying dates, Aadhaar linking and the 2025 revision in Bihar; the National Sports Governance Act, 2025;
the 2024 business rules for Jammu and Kashmir; the Uttarakhand Uniform Civil Code. MCQ keys are pinned (pos).
One Statement-I/II/III row (SI3)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write
from polity_common import C3, C4, T2

d.SUBJECT = "Polity"
d.REQUIRE_CRAFT = True
COI = "Constitution of India"
SC = "Supreme Court of India"

# ---------------------------------------------------------------- Judicial-Verdicts (e-pairs)
P("Judicial-Verdicts", "easy", "Consider the following pairs of Supreme Court judgments and what they decided:",
  "सर्वोच्च न्यायालय के निर्णयों और उनमें तय की गई बातों के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Sukanya Shantha v. Union of India (2024) : Struck down prison-manual rules that assigned work to prisoners on the basis of caste",
   "Satender Kumar Antil v. CBI (2022) : Laid down guidelines on bail and urged Parliament to enact a separate law on bail",
   "Manohar Lal Sharma v. Principal Secretary (2014) : Cancelled almost all the coal blocks allotted since 1993",
   "Swiss Ribbons v. Union of India (2019) : Struck down the Insolvency and Bankruptcy Code as unconstitutional"],
  ["सुकन्या शांता बनाम भारत संघ (2024) : जाति के आधार पर क़ैदियों को काम सौंपने वाले जेल-नियमावली के नियम निरस्त किए",
   "सतेंद्र कुमार अंतिल बनाम सीबीआई (2022) : ज़मानत पर दिशानिर्देश तय किए और संसद से ज़मानत पर अलग क़ानून बनाने का आग्रह किया",
   "मनोहर लाल शर्मा बनाम प्रधान सचिव (2014) : 1993 से आवंटित लगभग सभी कोयला ब्लॉक रद्द किए",
   "स्विस रिबन्स बनाम भारत संघ (2019) : दिवाला और शोधन अक्षमता संहिता को असंवैधानिक ठहराकर निरस्त किया"],
  2,
  "The first three pairs are correct. In Sukanya Shantha the Court found that several States' prison manuals gave cleaning and sweeping to prisoners from particular castes and cooking to others, and struck the rules down as violating Articles 14, 15, 17, 21 and 23, directing the manuals to be revised. In Antil the Court classified offences into categories for bail, insisted on compliance with Arnesh Kumar before arrest and on timely disposal of bail pleas, and suggested a dedicated Bail Act. In the coal-block case it held allocations made since 1993 through a screening committee and government dispensation arbitrary, and then cancelled 214 of 218 blocks, leading to auctions under a new law. "
  "The fourth pair is wrong: Swiss Ribbons upheld the Insolvency and Bankruptcy Code as a whole, accepting the different treatment of financial and operational creditors as a reasonable classification and describing the Code as a beneficial law aimed at reviving companies rather than at recovery alone.",
  "पहले तीन युग्म सही हैं। सुकन्या शांता में न्यायालय ने पाया कि कई राज्यों की जेल-नियमावलियाँ विशेष जातियों के क़ैदियों को सफ़ाई और झाड़ू का काम और दूसरों को खाना पकाने का काम देती थीं, और इन नियमों को अनुच्छेद 14, 15, 17, 21 और 23 का उल्लंघन मानकर निरस्त किया तथा नियमावलियों में संशोधन का निर्देश दिया। अंतिल में न्यायालय ने ज़मानत के लिए अपराधों को श्रेणियों में बाँटा, गिरफ़्तारी से पहले अर्नेश कुमार के पालन और ज़मानत याचिकाओं के समय पर निपटारे पर ज़ोर दिया, और एक अलग ज़मानत अधिनियम का सुझाव दिया। कोयला ब्लॉक मामले में उसने 1993 से छानबीन समिति और सरकारी विवेक से किए गए आवंटनों को मनमाना माना, फिर 218 में से 214 ब्लॉक रद्द किए, जिसके बाद नए क़ानून के अंतर्गत नीलामियाँ हुईं। "
  "चौथा युग्म ग़लत है: स्विस रिबन्स ने दिवाला और शोधन अक्षमता संहिता को पूर्ण रूप से बरक़रार रखा, वित्तीय और परिचालन लेनदारों के साथ भिन्न व्यवहार को उचित वर्गीकरण माना, और संहिता को केवल वसूली नहीं बल्कि कंपनियों के पुनरुद्धार के लिए बना लाभकारी क़ानून बताया।",
  f"{SC}: Sukanya Shantha v. Union of India (2024); Satender Kumar Antil v. CBI (2022); Manohar Lal Sharma v. Principal Secretary (2014); Swiss Ribbons v. Union of India (2019).",
  "l3-t6-pol-verdicts-sukanya-antil-coal-swiss-ribbons", craft="recall")

# ---------------------------------------------------------------- Federalism & Special Provisions (h-MCQ, m-stmt)
M("Federalism & Special Provisions", "hard",
  "Under Article 274, which one of the following Bills can be introduced in Parliament only on the recommendation of the President?",
  "अनुच्छेद 274 के अंतर्गत निम्नलिखित में से कौन-सा विधेयक संसद में केवल राष्ट्रपति की सिफ़ारिश पर ही पेश किया जा सकता है?",
  ["A Bill that varies the meaning of 'agricultural income' for income-tax law",
   "A Bill to create or abolish the Legislative Council of a particular State",
   "A Bill to amend the entries of the Concurrent List in the Seventh Schedule",
   "A Bill to give effect to a treaty that India has signed with another country"],
  ["आयकर क़ानून के लिए ‘कृषि आय’ का अर्थ बदलने वाला विधेयक",
   "किसी विशेष राज्य की विधान परिषद का सृजन या उत्सादन करने वाला विधेयक",
   "सातवीं अनुसूची की समवर्ती सूची की प्रविष्टियों में संशोधन करने वाला विधेयक",
   "भारत द्वारा किसी अन्य देश के साथ हस्ताक्षरित संधि को लागू करने वाला विधेयक"],
  0,
  "Article 274 protects the States' fiscal interests: no Bill or amendment may be introduced without the President's recommendation if it imposes or varies a tax or duty in which the States are interested, varies the meaning of 'agricultural income' as defined for income-tax law, affects the principles on which money is or may be distributed to the States, or imposes a surcharge for Union purposes on such taxes. Agricultural income can be taxed only by the States (Entry 46 of the State List), so redefining it for central income tax directly affects their tax base. "
  "None of the others needs such a recommendation: a Legislative Council is created or abolished by an ordinary law after a resolution of the State Assembly (Article 169); amending the Seventh Schedule needs a special majority and ratification by half the States (Article 368(2)); and Parliament legislates to implement treaties under Article 253.",
  "अनुच्छेद 274 राज्यों के राजकोषीय हितों की रक्षा करता है: ऐसा कोई विधेयक या संशोधन राष्ट्रपति की सिफ़ारिश के बिना पेश नहीं किया जा सकता जो किसी ऐसे कर या शुल्क को लगाए या बदले जिसमें राज्यों का हित है, आयकर क़ानून के लिए परिभाषित ‘कृषि आय’ का अर्थ बदले, उन सिद्धांतों को प्रभावित करे जिन पर राज्यों को धन वितरित होता है या हो सकता है, या ऐसे करों पर संघ के प्रयोजनों के लिए अधिभार लगाए। कृषि आय पर कर केवल राज्य लगा सकते हैं (राज्य सूची की प्रविष्टि 46), इसलिए केंद्रीय आयकर के लिए इसे पुनर्परिभाषित करना सीधे उनके कर-आधार को प्रभावित करता है। "
  "अन्य किसी के लिए ऐसी सिफ़ारिश आवश्यक नहीं है: विधान परिषद का सृजन या उत्सादन राज्य विधानसभा के संकल्प के बाद साधारण क़ानून से होता है (अनुच्छेद 169); सातवीं अनुसूची में संशोधन के लिए विशेष बहुमत और आधे राज्यों का अनुसमर्थन आवश्यक है (अनुच्छेद 368(2)); और संधियाँ लागू करने के लिए संसद अनुच्छेद 253 के अंतर्गत क़ानून बनाती है।",
  f"{COI}, Articles 169, 253, 274 and 368; Seventh Schedule, List II, Entry 46.",
  "l3-t6-pol-art274-presidents-recommendation", pos=1, craft="inference")

S("Federalism & Special Provisions", "medium", "With reference to changes in the names and boundaries of States and Union Territories, consider the following statements:",
  "राज्यों और संघ राज्यक्षेत्रों के नामों और सीमाओं में बदलाव के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Kerala Legislative Assembly has passed resolutions asking the Union to change the State's name to 'Keralam'.",
   "The Union Territory of Dadra and Nagar Haveli and Daman and Diu was formed in 2020 by merging two Union Territories.",
   "When Orissa was renamed Odisha in 2011, a constitutional amendment also changed the name of its language in the Eighth Schedule."],
  ["केरल विधानसभा ने संकल्प पारित कर संघ से राज्य का नाम बदलकर ‘केरलम’ करने का आग्रह किया है।",
   "दादरा और नगर हवेली तथा दमन और दीव संघ राज्यक्षेत्र 2020 में दो संघ राज्यक्षेत्रों के विलय से बना।",
   "2011 में जब उड़ीसा का नाम बदलकर ओडिशा किया गया, तब एक संविधान संशोधन ने आठवीं अनुसूची में उसकी भाषा का नाम भी बदला।"],
  C3, 2,
  "All three are correct. A State cannot rename itself: under Article 3 only Parliament can, by a law introduced on the President's recommendation after the Bill is referred to the State Legislature for its views. Kerala's Assembly passed unanimous resolutions in 2023 and 2024 asking that the State's name be changed to Keralam, as it is called in Malayalam; the decision rests with the Union. "
  "The merger of Dadra and Nagar Haveli with Daman and Diu, by an Act of 2019 that took effect in January 2020, was meant to cut duplicated administration in two small, neighbouring territories. Orissa became Odisha under the Orissa (Alteration of Name) Act, 2011, and the Constitution (Ninety-sixth Amendment) Act of the same year replaced 'Oriya' with 'Odia' in the Eighth Schedule -- the name of a language, unlike that of a State, can be changed only by amending the Constitution.",
  "तीनों कथन सही हैं। कोई राज्य स्वयं अपना नाम नहीं बदल सकता: अनुच्छेद 3 के अंतर्गत केवल संसद ऐसा कर सकती है, ऐसे क़ानून द्वारा जो राष्ट्रपति की सिफ़ारिश पर, विधेयक को राज्य विधानमंडल के विचार के लिए भेजने के बाद, पेश किया जाए। केरल विधानसभा ने 2023 और 2024 में सर्वसम्मत संकल्प पारित कर आग्रह किया कि नाम बदलकर केरलम किया जाए, जैसा मलयालम में राज्य को कहा जाता है; निर्णय संघ के हाथ में है। "
  "दादरा और नगर हवेली का दमन और दीव के साथ विलय, 2019 के एक अधिनियम से जो जनवरी 2020 में प्रभावी हुआ, दो छोटे, पड़ोसी क्षेत्रों में दोहरे प्रशासन को घटाने के लिए था। उड़ीसा, उड़ीसा (नाम परिवर्तन) अधिनियम, 2011 के अंतर्गत ओडिशा बना, और उसी वर्ष के संविधान (छियानबेवाँ संशोधन) अधिनियम ने आठवीं अनुसूची में ‘उड़िया’ के स्थान पर ‘ओड़िआ’ किया -- किसी भाषा का नाम, किसी राज्य के नाम के विपरीत, केवल संविधान संशोधन से ही बदला जा सकता है।",
  f"{COI}, Articles 3 and 4, First and Eighth Schedules; Orissa (Alteration of Name) Act, 2011; Constitution (96th Amendment) Act, 2011; Dadra and Nagar Haveli and Daman and Diu (Merger of Union Territories) Act, 2019.",
  "l3-t6-pol-keralam-dnhdd-odisha-names", craft="linkage")

# ---------------------------------------------------------------- Constitutional Framework (h-stmt, m-stmt)
S("Constitutional Framework", "hard", "With reference to the removal of judges of the Supreme Court and the High Courts, consider the following statements:",
  "सर्वोच्च न्यायालय और उच्च न्यायालयों के न्यायाधीशों को हटाने के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Under the Judges (Inquiry) Act, 1968, a notice of motion for removal must be signed by at least 100 members if given in the Lok Sabha, or 50 members if given in the Rajya Sabha.",
   "If the motion is admitted, the presiding officer constitutes a committee of a Supreme Court judge, a High Court Chief Justice and a distinguished jurist to investigate the charges.",
   "In 2025 the Speaker of the Lok Sabha admitted a motion for the removal of Justice Yashwant Varma and constituted such a committee.",
   "Justice Soumitra Sen of the Calcutta High Court was removed by Parliament in 2011, the only judge ever to be removed."],
  ["न्यायाधीश (जाँच) अधिनियम, 1968 के अंतर्गत हटाने के प्रस्ताव की सूचना पर लोकसभा में दी जाने पर कम से कम 100 सदस्यों के, या राज्यसभा में दी जाने पर 50 सदस्यों के हस्ताक्षर आवश्यक हैं।",
   "प्रस्ताव स्वीकार होने पर पीठासीन अधिकारी आरोपों की जाँच के लिए सर्वोच्च न्यायालय के एक न्यायाधीश, एक उच्च न्यायालय के मुख्य न्यायमूर्ति और एक प्रतिष्ठित विधिवेत्ता की समिति गठित करते हैं।",
   "2025 में लोकसभा अध्यक्ष ने न्यायमूर्ति यशवंत वर्मा को हटाने का प्रस्ताव स्वीकार किया और ऐसी समिति गठित की।",
   "कलकत्ता उच्च न्यायालय के न्यायमूर्ति सौमित्र सेन को 2011 में संसद ने हटाया, जो हटाए गए एकमात्र न्यायाधीश हैं।"],
  C4, 2,
  "Statements 1, 2 and 3 are correct. Article 124(4) allows removal only for proved misbehaviour or incapacity, on an address by each House passed by a majority of its total membership and two-thirds of those present and voting; the Judges (Inquiry) Act sets out how the charges are proved. Only if the committee finds the judge guilty can the motion be taken up in the Houses. In the Varma case, after cash was reported found at the judge's official residence in Delhi in March 2025, an in-house inquiry ordered by the Chief Justice of India was followed by a motion in Parliament, and in August 2025 the Speaker admitted it and named a three-member committee. "
  "Statement 4 is wrong: no judge has ever been removed. The motion against Justice V. Ramaswami failed in the Lok Sabha in 1993; the Rajya Sabha voted to remove Justice Soumitra Sen in 2011, but he resigned before the Lok Sabha could vote, and the proceedings ended. The difficulty of removal is a deliberate guarantee of judicial independence.",
  "कथन 1, 2 और 3 सही हैं। अनुच्छेद 124(4) केवल सिद्ध कदाचार या असमर्थता के आधार पर हटाने की अनुमति देता है, हर सदन द्वारा उसकी कुल सदस्य संख्या के बहुमत और उपस्थित तथा मत देने वालों के दो-तिहाई से पारित समावेदन पर; न्यायाधीश (जाँच) अधिनियम बताता है कि आरोप कैसे सिद्ध हों। समिति द्वारा न्यायाधीश को दोषी पाए जाने पर ही प्रस्ताव सदनों में लिया जा सकता है। वर्मा मामले में, मार्च 2025 में दिल्ली में न्यायाधीश के सरकारी आवास पर नक़दी मिलने की सूचना के बाद, भारत के मुख्य न्यायमूर्ति द्वारा कराई गई आंतरिक जाँच के पश्चात संसद में प्रस्ताव आया, और अगस्त 2025 में अध्यक्ष ने उसे स्वीकार कर तीन सदस्यीय समिति नियुक्त की। "
  "कथन 4 ग़लत है: किसी न्यायाधीश को कभी नहीं हटाया गया। न्यायमूर्ति वी. रामास्वामी के विरुद्ध प्रस्ताव 1993 में लोकसभा में गिर गया; राज्यसभा ने 2011 में न्यायमूर्ति सौमित्र सेन को हटाने के पक्ष में मत दिया, पर लोकसभा के मतदान से पहले उन्होंने त्यागपत्र दे दिया और कार्यवाही समाप्त हो गई। हटाने की यह कठिनाई न्यायिक स्वतंत्रता की एक सोची-समझी गारंटी है।",
  f"{COI}, Articles 124(4), 124(5) and 218; Judges (Inquiry) Act, 1968, section 3.",
  "l3-t6-pol-judges-inquiry-act-varma", craft="precision")

S("Constitutional Framework", "medium", "With reference to curative petitions in the Supreme Court, consider the following statements:",
  "सर्वोच्च न्यायालय में उपचारात्मक (क्यूरेटिव) याचिकाओं के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["The remedy was recognised by the Supreme Court in Rupa Ashok Hurra (2002), and can be sought after a review petition has been dismissed.",
   "A curative petition must carry a certificate from a senior advocate that it meets the grounds laid down by the Court.",
   "A curative petition is heard in open court by any two judges of the Supreme Court chosen by the Chief Justice."],
  ["इस उपचार को सर्वोच्च न्यायालय ने रूपा अशोक हुर्रा (2002) में मान्यता दी, और यह पुनर्विलोकन याचिका ख़ारिज होने के बाद माँगा जा सकता है।",
   "उपचारात्मक याचिका पर किसी वरिष्ठ अधिवक्ता का यह प्रमाणपत्र होना चाहिए कि वह न्यायालय द्वारा तय आधारों को पूरा करती है।",
   "उपचारात्मक याचिका की सुनवाई मुख्य न्यायमूर्ति द्वारा चुने गए सर्वोच्च न्यायालय के किन्हीं दो न्यायाधीशों द्वारा खुले न्यायालय में होती है।"],
  C3, 1,
  "Statements 1 and 2 are correct. The Constitution provides for review of the Supreme Court's own judgments under Article 137, but in Rupa Ashok Hurra a Constitution Bench held that, to prevent abuse of process and cure a gross miscarriage of justice, the Court could reconsider a final judgment even after a review was dismissed, drawing on its inherent powers and Article 142. The grounds are narrow -- chiefly a violation of natural justice, such as a party not being heard, or a reasonable apprehension of bias in a judge -- and the senior advocate's certificate is meant to screen out routine attempts at a third hearing. "
  "Statement 3 is wrong: the petition is circulated first to the three senior-most judges and, if available, the judges who gave the judgment, and is usually decided in chambers; it is listed for hearing only if a majority of them think it needs one. The Court may impose exemplary costs on frivolous petitions.",
  "कथन 1 और 2 सही हैं। संविधान अनुच्छेद 137 के अंतर्गत सर्वोच्च न्यायालय के अपने निर्णयों के पुनर्विलोकन का उपबंध करता है, पर रूपा अशोक हुर्रा में संविधान पीठ ने माना कि प्रक्रिया के दुरुपयोग को रोकने और न्याय की गंभीर विफलता को सुधारने के लिए न्यायालय अपनी अंतर्निहित शक्तियों और अनुच्छेद 142 के आधार पर पुनर्विलोकन ख़ारिज होने के बाद भी अंतिम निर्णय पर पुनर्विचार कर सकता है। आधार सीमित हैं -- मुख्यतः नैसर्गिक न्याय का उल्लंघन, जैसे किसी पक्ष को न सुना जाना, या किसी न्यायाधीश के पक्षपात की उचित आशंका -- और वरिष्ठ अधिवक्ता का प्रमाणपत्र तीसरी सुनवाई के सामान्य प्रयासों को छाँटने के लिए है। "
  "कथन 3 ग़लत है: याचिका पहले तीन वरिष्ठतम न्यायाधीशों और, यदि उपलब्ध हों, निर्णय देने वाले न्यायाधीशों के पास भेजी जाती है, और सामान्यतः कक्ष में तय होती है; सुनवाई के लिए तभी सूचीबद्ध होती है जब उनमें से अधिकांश को इसकी आवश्यकता लगे। न्यायालय निरर्थक याचिकाओं पर अनुकरणीय लागत लगा सकता है।",
  f"{SC}: Rupa Ashok Hurra v. Ashok Hurra (2002); {COI}, Articles 137 and 142.",
  "l3-t6-pol-curative-petition-hurra", craft="precision")

# ---------------------------------------------------------------- Parliament & State Legislature (h-stmt, m-MCQ, m-stmt)
S("Parliament & State Legislature", "hard", "With reference to the Governor's power to promulgate ordinances under Article 213, consider the following statements:",
  "अनुच्छेद 213 के अंतर्गत राज्यपाल की अध्यादेश जारी करने की शक्ति के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Governor can promulgate an ordinance only when the Legislative Assembly -- or, in a State with two Houses, both Houses -- is not in session.",
   "Without instructions from the President, the Governor cannot promulgate an ordinance containing provisions that would have needed the President's previous sanction for the introduction of a Bill.",
   "An ordinance ceases to operate six weeks after the Legislature reassembles, unless it is disapproved earlier.",
   "An ordinance is void if it makes a provision that would be invalid in an Act of the State Legislature assented to by the Governor."],
  ["राज्यपाल अध्यादेश तभी जारी कर सकते हैं जब विधानसभा -- या दो सदनों वाले राज्य में दोनों सदन -- सत्र में न हों।",
   "राष्ट्रपति के अनुदेश के बिना राज्यपाल ऐसा अध्यादेश जारी नहीं कर सकते जिसके उपबंधों वाले विधेयक को पेश करने के लिए राष्ट्रपति की पूर्व स्वीकृति आवश्यक होती।",
   "विधानमंडल के पुनः समवेत होने के छह सप्ताह बाद अध्यादेश प्रवृत्त नहीं रहता, जब तक उसे पहले ही अननुमोदित न कर दिया जाए।",
   "यदि अध्यादेश कोई ऐसा उपबंध करे जो राज्यपाल की अनुमति प्राप्त राज्य विधानमंडल के अधिनियम में अमान्य होता, तो वह शून्य है।"],
  C4, 3,
  "All four are correct; they restate the scheme of Article 213, the State counterpart of Article 123. The power exists only when the Legislature is not in session and the Governor is satisfied that immediate action is needed; it is exercised on the advice of the Council of Ministers, and an ordinance has the same force as an Act while it lasts. Statement 2 reflects the provisos to clause (1): where a Bill on the subject would have needed the President's previous sanction, or would have to be reserved for his consideration, or an Act on it would be invalid without his assent, the Governor needs the President's instructions. "
  "Every ordinance must be laid before the Legislature and lapses six weeks after it reassembles, so it cannot replace legislation indefinitely; the Supreme Court has held that repeated re-promulgation without placing ordinances before the Legislature is a fraud on the Constitution. And under clause (3), an ordinance is subject to the same limits as a State law -- legislative competence and fundamental rights included.",
  "चारों कथन सही हैं; ये अनुच्छेद 213 की योजना को दोहराते हैं, जो अनुच्छेद 123 का राज्य-स्तरीय समकक्ष है। यह शक्ति तभी है जब विधानमंडल सत्र में न हो और राज्यपाल संतुष्ट हों कि तुरंत कार्रवाई आवश्यक है; इसका प्रयोग मंत्रिपरिषद की सलाह पर होता है, और अध्यादेश जब तक रहे, अधिनियम जितना ही प्रभावी होता है। कथन 2 खंड (1) के परंतुकों को दर्शाता है: जहाँ उस विषय के विधेयक के लिए राष्ट्रपति की पूर्व स्वीकृति आवश्यक होती, या उसे उनके विचार के लिए आरक्षित करना पड़ता, या उस पर अधिनियम उनकी अनुमति के बिना अमान्य होता, वहाँ राज्यपाल को राष्ट्रपति के अनुदेश चाहिए। "
  "हर अध्यादेश विधानमंडल के सामने रखा जाना चाहिए और उसके पुनः समवेत होने के छह सप्ताह बाद समाप्त हो जाता है, इसलिए यह अनिश्चित काल तक क़ानून का स्थान नहीं ले सकता; सर्वोच्च न्यायालय ने माना है कि अध्यादेशों को विधानमंडल के सामने रखे बिना बार-बार पुनः जारी करना संविधान के साथ छल है। और खंड (3) के अंतर्गत अध्यादेश पर वही सीमाएँ हैं जो राज्य क़ानून पर -- विधायी क्षमता और मौलिक अधिकार सहित।",
  f"{COI}, Articles 123 and 213.", "l3-t6-pol-art213-governor-ordinances", craft="precision")

M("Parliament & State Legislature", "medium",
  "When a State is under President's rule, laws on matters in the State List for that State are ordinarily made by:",
  "जब किसी राज्य में राष्ट्रपति शासन हो, तब उस राज्य के लिए राज्य सूची के विषयों पर क़ानून सामान्यतः कौन बनाता है?",
  ["the Governor, through ordinances issued in his own discretion",
   "the Supreme Court, on a reference made to it by the President",
   "the dissolved State Legislature, reconvened for the purpose by the Governor",
   "Parliament, or the President if Parliament confers that power on him"],
  ["राज्यपाल, अपने विवेक से जारी अध्यादेशों द्वारा",
   "सर्वोच्च न्यायालय, राष्ट्रपति द्वारा किए गए निर्देश (रेफ़रेंस) पर",
   "विघटित राज्य विधानमंडल, जिसे राज्यपाल इस प्रयोजन से फिर बुलाते हैं",
   "संसद, या राष्ट्रपति यदि संसद उन्हें यह शक्ति सौंपे"],
  3,
  "A proclamation under Article 356 can declare that the powers of the State Legislature shall be exercisable by or under the authority of Parliament. Article 357 then lets Parliament make the State's laws itself or confer that power on the President, who may delegate it further; in practice most laws for a State under President's rule are 'President's Acts', and the President may also authorise spending from the State's Consolidated Fund pending Parliament's sanction. "
  "Laws made in this way continue in force after the proclamation ends until the State Legislature alters or repeals them. The Governor administers the State on the President's behalf but does not acquire the Legislature's law-making power, the courts do not legislate, and a dissolved Assembly cannot be reconvened.",
  "अनुच्छेद 356 के अंतर्गत उद्घोषणा यह घोषित कर सकती है कि राज्य विधानमंडल की शक्तियाँ संसद द्वारा या उसके प्राधिकार के अधीन प्रयोग की जाएँगी। अनुच्छेद 357 तब संसद को स्वयं राज्य के क़ानून बनाने या यह शक्ति राष्ट्रपति को सौंपने देता है, जो इसे आगे प्रत्यायोजित कर सकते हैं; व्यवहार में राष्ट्रपति शासन वाले राज्य के अधिकांश क़ानून ‘राष्ट्रपति के अधिनियम’ होते हैं, और राष्ट्रपति संसद की स्वीकृति लंबित रहने तक राज्य की संचित निधि से व्यय की अनुमति भी दे सकते हैं। "
  "इस प्रकार बने क़ानून उद्घोषणा समाप्त होने के बाद भी तब तक प्रवृत्त रहते हैं जब तक राज्य विधानमंडल उन्हें बदल या निरसित न करे। राज्यपाल राष्ट्रपति की ओर से राज्य का प्रशासन चलाते हैं पर विधानमंडल की विधि-निर्माण शक्ति प्राप्त नहीं करते, न्यायालय क़ानून नहीं बनाते, और विघटित विधानसभा फिर नहीं बुलाई जा सकती।",
  f"{COI}, Articles 356 and 357.", "l3-t6-pol-art357-presidents-acts", pos=3, craft="inference")

S("Parliament & State Legislature", "medium", "With reference to the new Parliament building, consider the following statements:",
  "नए संसद भवन के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Its Lok Sabha chamber is designed on the theme of the peacock and its Rajya Sabha chamber on the theme of the lotus.",
   "The old Parliament House has been renamed 'Samvidhan Sadan'.",
   "Its Lok Sabha chamber can seat only the 543 elected members, so joint sittings continue to be held in the old building."],
  ["इसका लोकसभा कक्ष मोर की थीम पर और राज्यसभा कक्ष कमल की थीम पर बना है।",
   "पुराने संसद भवन का नाम बदलकर ‘संविधान सदन’ किया गया है।",
   "इसके लोकसभा कक्ष में केवल 543 निर्वाचित सदस्य बैठ सकते हैं, इसलिए संयुक्त बैठकें पुराने भवन में ही होती हैं।"],
  C3, 1,
  "Statements 1 and 2 are correct. The building, which Parliament began using in September 2023, has chambers themed on the national bird and the national flower; the special session that moved into it also introduced and passed the Constitution amendment on reservation for women in the Lok Sabha and State Assemblies. The old circular building, where the Constituent Assembly met and the Constitution was adopted, was renamed Samvidhan Sadan. "
  "Statement 3 is wrong: the new Lok Sabha chamber has about 888 seats and can hold around 1,272 members for a joint sitting, which is why the new building has no separate Central Hall; the larger chambers also allow for the increase in the number of members expected after the next delimitation.",
  "कथन 1 और 2 सही हैं। सितंबर 2023 से संसद द्वारा प्रयुक्त इस भवन के कक्ष राष्ट्रीय पक्षी और राष्ट्रीय पुष्प की थीम पर हैं; इसमें आए विशेष सत्र ने लोकसभा और राज्य विधानसभाओं में महिलाओं के आरक्षण वाला संविधान संशोधन भी पेश और पारित किया। पुराने गोलाकार भवन, जहाँ संविधान सभा बैठी और संविधान अंगीकृत हुआ, का नाम संविधान सदन रखा गया। "
  "कथन 3 ग़लत है: नए लोकसभा कक्ष में लगभग 888 सीटें हैं और संयुक्त बैठक के लिए लगभग 1,272 सदस्य बैठ सकते हैं, इसीलिए नए भवन में अलग केंद्रीय कक्ष नहीं है; बड़े कक्ष अगले परिसीमन के बाद सदस्यों की अपेक्षित वृद्धि का भी ध्यान रखते हैं।",
  "Lok Sabha Secretariat and Rajya Sabha Secretariat, the new Parliament building (2023).",
  "l3-t6-pol-new-parliament-building", craft="recall")

# ---------------------------------------------------------------- Constitutional & Statutory Bodies (h-SI3)
A("Constitutional & Statutory Bodies", "hard",
  "A film certified by the Central Board of Film Certification no longer needs to have its certificate renewed after ten years.",
  "केंद्रीय फ़िल्म प्रमाणन बोर्ड द्वारा प्रमाणित फ़िल्म के प्रमाणपत्र को अब दस वर्ष बाद नवीनीकृत कराने की आवश्यकता नहीं है।",
  "The Cinematograph (Amendment) Act, 2023 made the certificates issued by the Board valid in perpetuity.",
  "सिनेमैटोग्राफ़ (संशोधन) अधिनियम, 2023 ने बोर्ड द्वारा जारी प्रमाणपत्रों को स्थायी रूप से वैध बना दिया।",
  2,
  "Statements I and II are correct and II explains I; Statement III is wrong, so the answer is (c). Certificates were earlier valid for ten years; the 2023 amendment made them perpetual, and also split the 'UA' category into age-based sub-categories (UA 7+, UA 13+ and UA 16+) and added penalties for film piracy, including unauthorised recording in a cinema hall. The Board is a statutory body under the Cinematograph Act, 1952, functioning under the Ministry of Information and Broadcasting. "
  "Statement III is wrong: the Central Government's power to re-examine a film already certified by the Board had been struck down in K. M. Shankarappa (2000) as an executive override of a quasi-judicial decision, and the 2023 amendment omitted that provision rather than reviving it; appeals against the Board's decisions now go to the High Courts.",
  "कथन I और II सही हैं और II, I की व्याख्या करता है; कथन III ग़लत है, इसलिए उत्तर (ग) है। पहले प्रमाणपत्र दस वर्ष के लिए वैध होते थे; 2023 के संशोधन ने उन्हें स्थायी बनाया, और ‘यूए’ श्रेणी को आयु-आधारित उप-श्रेणियों (यूए 7+, यूए 13+ और यूए 16+) में बाँटा तथा सिनेमा हॉल में अनधिकृत रिकॉर्डिंग सहित फ़िल्म चोरी के लिए दंड जोड़े। बोर्ड सिनेमैटोग्राफ़ अधिनियम, 1952 के अंतर्गत सूचना और प्रसारण मंत्रालय के अधीन कार्य करने वाला सांविधिक निकाय है। "
  "कथन III ग़लत है: बोर्ड द्वारा पहले से प्रमाणित फ़िल्म की पुनः जाँच करने की केंद्र सरकार की शक्ति को के. एम. शंकरप्पा (2000) में अर्ध-न्यायिक निर्णय पर कार्यपालिका के हस्तक्षेप के रूप में निरस्त किया गया था, और 2023 के संशोधन ने उस उपबंध को पुनर्जीवित करने के बजाय हटा दिया; बोर्ड के निर्णयों के विरुद्ध अपीलें अब उच्च न्यायालयों में जाती हैं।",
  f"Cinematograph Act, 1952, as amended by the Cinematograph (Amendment) Act, 2023; {SC}: Union of India v. K. M. Shankarappa (2000).",
  "l3-t6-pol-cbfc-certificates-2023",
  s3="The 2023 amendment also empowered the Central Government to re-examine and revise films that the Board has already certified.",
  s3_hi="2023 के संशोधन ने केंद्र सरकार को बोर्ड द्वारा पहले से प्रमाणित फ़िल्मों की पुनः जाँच और संशोधन करने का अधिकार भी दिया।",
  craft="inference")

# ---------------------------------------------------------------- Panchayati Raj & Local Governance (h-SI)
A("Panchayati Raj & Local Governance", "hard",
  "The office of the sarpanch of a particular gram panchayat may be reserved for a woman in one term and left unreserved in the next.",
  "किसी विशेष ग्राम पंचायत के सरपंच का पद एक कार्यकाल में महिला के लिए आरक्षित और अगले में अनारक्षित हो सकता है।",
  "Article 243D(4) requires the offices of chairpersons reserved under it to be allotted by rotation to different panchayats.",
  "अनुच्छेद 243D(4) अपेक्षा करता है कि उसके अंतर्गत आरक्षित अध्यक्षों के पद अलग-अलग पंचायतों को चक्रानुक्रम (रोटेशन) से आवंटित किए जाएँ।",
  0,
  "Both statements are correct and Statement II explains Statement I. Article 243D(4) reserves the offices of chairpersons at each level for Scheduled Castes, Scheduled Tribes and women in the manner a State law provides -- for SCs and STs in proportion to their population in the State, and for women not less than one-third -- and its last proviso says these reserved offices 'shall be allotted by rotation to different Panchayats at each level'. A State's rules therefore shift the reservation from one panchayat to another at successive elections. "
  "Rotation spreads the opportunity across villages but has a known cost: a woman or SC sarpanch who has done well usually cannot seek a second term from the same seat once it is de-reserved, and studies of 'sarpanch-pati' proxies point to the short horizon as one reason for weak independent leadership. Some States have experimented with longer rotation cycles of two terms.",
  "दोनों कथन सही हैं और कथन II, कथन I की व्याख्या करता है। अनुच्छेद 243D(4) हर स्तर पर अध्यक्षों के पद अनुसूचित जातियों, अनुसूचित जनजातियों और महिलाओं के लिए उस ढंग से आरक्षित करता है जो राज्य का क़ानून तय करे -- अनुसूचित जातियों और जनजातियों के लिए राज्य में उनकी जनसंख्या के अनुपात में, और महिलाओं के लिए कम से कम एक-तिहाई -- और इसका अंतिम परंतुक कहता है कि ये आरक्षित पद ‘हर स्तर पर अलग-अलग पंचायतों को चक्रानुक्रम से आवंटित किए जाएँगे’। इसलिए राज्य के नियम लगातार चुनावों में आरक्षण को एक पंचायत से दूसरी पर ले जाते हैं। "
  "चक्रानुक्रम अवसर को गाँवों में फैलाता है पर इसकी एक ज्ञात क़ीमत है: अच्छा काम करने वाली महिला या अनुसूचित जाति की सरपंच सामान्यतः उसी सीट से दूसरा कार्यकाल नहीं माँग सकती जब वह अनारक्षित हो जाए, और ‘सरपंच-पति’ जैसी प्रॉक्सी व्यवस्था के अध्ययन इस छोटे क्षितिज को कमज़ोर स्वतंत्र नेतृत्व का एक कारण बताते हैं। कुछ राज्यों ने दो कार्यकालों के लंबे चक्र आज़माए हैं।",
  f"{COI}, Article 243D; Ministry of Panchayati Raj.", "l3-t6-pol-art243d4-chairperson-rotation", craft="inference")

# ---------------------------------------------------------------- Governance (m-MCQ, m-stmt)
M("Governance", "medium",
  "Under the model bye-laws circulated by the Ministry of Cooperation for adoption by the States, primary agricultural credit societies (PACS) may:",
  "राज्यों द्वारा अपनाने के लिए सहकारिता मंत्रालय द्वारा परिचालित आदर्श उपनियमों के अंतर्गत प्राथमिक कृषि ऋण समितियाँ (पैक्स) क्या कर सकती हैं?",
  ["take up new businesses such as dairy, Jan Aushadhi Kendras and service centres",
   "accept deposits from the public and lend anywhere in India like scheduled commercial banks",
   "issue Kisan Credit Cards only through the regional rural bank of their district",
   "levy local taxes on the farmers of their area in place of the gram panchayat"],
  ["डेयरी, जन औषधि केंद्र और सेवा केंद्र जैसे नए व्यवसाय करना",
   "अनुसूचित वाणिज्यिक बैंकों की तरह जनता से जमा लेना और भारत में कहीं भी ऋण देना",
   "किसान क्रेडिट कार्ड केवल अपने ज़िले के क्षेत्रीय ग्रामीण बैंक के माध्यम से जारी करना",
   "ग्राम पंचायत के स्थान पर अपने क्षेत्र के किसानों पर स्थानीय कर लगाना"],
  0,
  "PACS, the village-level base of the short-term cooperative credit structure, mostly lent crop loans and distributed fertiliser, and many were dormant or loss-making. The model bye-laws, prepared after consulting the States in 2022-23, let PACS take up more than twenty-five activities -- dairy, fisheries, warehousing and grain storage, LPG and fuel outlets, Jan Aushadhi Kendras, common service centres and others -- and make their membership more inclusive, while the Union is computerising all functional PACS on a common software linked to district and State cooperative banks. "
  "Cooperative societies are a State subject, so the bye-laws work only when States adopt them. PACS are not banks: they cannot take deposits from the public or lend outside their membership like commercial banks, and they have no taxing power.",
  "पैक्स, अल्पकालिक सहकारी ऋण ढाँचे का ग्राम-स्तरीय आधार, अधिकतर फ़सल ऋण देती और उर्वरक बाँटती थीं, और उनमें से अनेक निष्क्रिय या घाटे में थीं। 2022-23 में राज्यों से परामर्श के बाद तैयार आदर्श उपनियम पैक्स को पच्चीस से अधिक गतिविधियाँ करने देते हैं -- डेयरी, मत्स्य पालन, भंडारण और अनाज गोदाम, एलपीजी और ईंधन केंद्र, जन औषधि केंद्र, साझा सेवा केंद्र और अन्य -- और उनकी सदस्यता को अधिक समावेशी बनाते हैं, जबकि संघ सभी कार्यशील पैक्स को ज़िला और राज्य सहकारी बैंकों से जुड़े एक साझा सॉफ़्टवेयर पर कंप्यूटरीकृत कर रहा है। "
  "सहकारी समितियाँ राज्य का विषय हैं, इसलिए उपनियम तभी काम करते हैं जब राज्य उन्हें अपनाएँ। पैक्स बैंक नहीं हैं: वे वाणिज्यिक बैंकों की तरह जनता से जमा नहीं ले सकतीं या अपनी सदस्यता के बाहर ऋण नहीं दे सकतीं, और उनके पास कर लगाने की कोई शक्ति नहीं है।",
  "Ministry of Cooperation, Model Bye-laws for PACS (2023) and Computerisation of PACS; Seventh Schedule, List II, Entry 32.",
  "l3-t6-pol-pacs-model-bye-laws", pos=0, craft="application")

S("Governance", "medium", "With reference to the preparation of electoral rolls, consider the following statements:",
  "मतदाता सूचियाँ तैयार करने के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Since the Election Laws (Amendment) Act, 2021, a person can be enrolled on the basis of four qualifying dates in a year instead of only 1 January.",
   "Linking one's Aadhaar number with one's entry in the electoral roll is voluntary.",
   "Young people aged seventeen can apply in advance so that they are enrolled when they reach eighteen on a qualifying date.",
   "In 2025 the Supreme Court directed that Aadhaar be accepted as one of the documents in the special intensive revision of the rolls in Bihar, as proof of identity but not of citizenship."],
  ["निर्वाचन विधि (संशोधन) अधिनियम, 2021 से किसी व्यक्ति का नामांकन केवल 1 जनवरी के बजाय वर्ष की चार अर्हता तिथियों के आधार पर हो सकता है।",
   "मतदाता सूची में अपनी प्रविष्टि के साथ अपना आधार नंबर जोड़ना स्वैच्छिक है।",
   "सत्रह वर्ष के युवा अग्रिम आवेदन कर सकते हैं ताकि किसी अर्हता तिथि पर अठारह वर्ष के होते ही उनका नामांकन हो जाए।",
   "2025 में सर्वोच्च न्यायालय ने निर्देश दिया कि बिहार में मतदाता सूचियों के विशेष गहन पुनरीक्षण में आधार को पहचान के प्रमाण के रूप में, पर नागरिकता के प्रमाण के रूप में नहीं, दस्तावेज़ों में से एक माना जाए।"],
  C4, 3,
  "All four are correct. The 2021 amendment to the Representation of the People Act, 1950 introduced 1 January, 1 April, 1 July and 1 October as qualifying dates, so that someone turning eighteen need not wait up to a year to be enrolled; it also allowed electoral registration officers to ask for Aadhaar to authenticate entries and weed out duplicates, but the Election Commission has told the Supreme Court that supplying it is voluntary and that no one will be refused enrolment for not giving it. Since 2022 seventeen-year-olds can apply in advance. "
  "In the special intensive revision ordered in Bihar in 2025 -- a fresh verification of the whole roll rather than the usual summary revision -- the Court, hearing challenges, directed that Aadhaar be accepted as an additional document, while noting that it proves identity, not citizenship, which remains a qualification for registration under Article 326.",
  "चारों कथन सही हैं। लोक प्रतिनिधित्व अधिनियम, 1950 में 2021 के संशोधन ने 1 जनवरी, 1 अप्रैल, 1 जुलाई और 1 अक्टूबर को अर्हता तिथियाँ बनाया, ताकि अठारह वर्ष का होने वाला व्यक्ति नामांकन के लिए एक वर्ष तक प्रतीक्षा न करे; इसने निर्वाचक रजिस्ट्रीकरण अधिकारियों को प्रविष्टियों के प्रमाणीकरण और दोहराव हटाने के लिए आधार माँगने की अनुमति भी दी, पर निर्वाचन आयोग ने सर्वोच्च न्यायालय को बताया है कि इसे देना स्वैच्छिक है और न देने पर किसी का नामांकन नहीं रोका जाएगा। 2022 से सत्रह वर्ष के युवा अग्रिम आवेदन कर सकते हैं। "
  "2025 में बिहार में कराए गए विशेष गहन पुनरीक्षण में -- जो सामान्य संक्षिप्त पुनरीक्षण के बजाय पूरी सूची का नया सत्यापन था -- न्यायालय ने चुनौतियों की सुनवाई करते हुए निर्देश दिया कि आधार को अतिरिक्त दस्तावेज़ के रूप में स्वीकार किया जाए, यह ध्यान दिलाते हुए कि यह पहचान सिद्ध करता है, नागरिकता नहीं, जो अनुच्छेद 326 के अंतर्गत पंजीकरण की एक अर्हता बनी रहती है।",
  f"Representation of the People Act, 1950, sections 14 and 23 (as amended by the Election Laws (Amendment) Act, 2021); Election Commission of India; {SC}, orders in the challenge to the Bihar special intensive revision (2025).",
  "l3-t6-pol-electoral-rolls-qualifying-dates-sir", craft="linkage")

# ---------------------------------------------------------------- Statutory-Laws (m-stmt)
S("Statutory-Laws", "medium", "With reference to the National Sports Governance Act, 2025, consider the following statements:",
  "राष्ट्रीय खेल शासन अधिनियम, 2025 के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["It provides for a National Sports Board to grant recognition to national sports federations and to regulate them.",
   "It sets up a National Sports Tribunal to decide sports disputes, with appeals from its decisions lying to the Supreme Court.",
   "It brings every national sports federation, including the Board of Control for Cricket in India, under the Right to Information Act."],
  ["यह राष्ट्रीय खेल महासंघों को मान्यता देने और उन्हें विनियमित करने के लिए राष्ट्रीय खेल बोर्ड का उपबंध करता है।",
   "यह खेल विवादों के निर्णय के लिए राष्ट्रीय खेल अधिकरण स्थापित करता है, जिसके निर्णयों के विरुद्ध अपील सर्वोच्च न्यायालय में होती है।",
   "यह भारतीय क्रिकेट नियंत्रण बोर्ड सहित हर राष्ट्रीय खेल महासंघ को सूचना का अधिकार अधिनियम के अंतर्गत लाता है।"],
  C3, 1,
  "Statements 1 and 2 are correct. The Act, passed in August 2025, makes recognition by the National Sports Board a condition for a federation to use the national name and receive government support, lets the Board suspend or derecognise federations that fail to hold elections or keep accounts, and sets norms on governance such as age and tenure limits for office-bearers and places for athletes on governing bodies. The Tribunal is meant to end the flood of sports disputes reaching the High Courts; its decisions can be challenged only before the Supreme Court, though disputes under the Olympic Charter or international federations' rules go to their own forums. "
  "Statement 3 is wrong: the Act treats a federation as a public authority under the RTI Act only where it receives government funding or other support, which leaves out the BCCI, as it takes no such funding -- although, with cricket now an Olympic sport, the BCCI is expected to come under the Act's recognition scheme.",
  "कथन 1 और 2 सही हैं। अगस्त 2025 में पारित अधिनियम राष्ट्रीय खेल बोर्ड की मान्यता को किसी महासंघ के राष्ट्रीय नाम उपयोग करने और सरकारी सहायता पाने की शर्त बनाता है, बोर्ड को चुनाव न कराने या लेखा न रखने वाले महासंघों को निलंबित या अमान्य करने देता है, और पदाधिकारियों के लिए आयु और कार्यकाल सीमा तथा शासी निकायों में खिलाड़ियों के स्थान जैसे शासन मानदंड तय करता है। अधिकरण का उद्देश्य उच्च न्यायालयों तक पहुँचने वाले खेल विवादों की बाढ़ को रोकना है; इसके निर्णयों को केवल सर्वोच्च न्यायालय में चुनौती दी जा सकती है, हालाँकि ओलंपिक चार्टर या अंतरराष्ट्रीय महासंघों के नियमों से जुड़े विवाद उनके अपने मंचों पर जाते हैं। "
  "कथन 3 ग़लत है: अधिनियम किसी महासंघ को सूचना का अधिकार अधिनियम के अंतर्गत लोक प्राधिकारी तभी मानता है जब उसे सरकारी धन या अन्य सहायता मिलती हो, जिससे बीसीसीआई बाहर रहता है, क्योंकि वह ऐसा धन नहीं लेता -- हालाँकि क्रिकेट के अब ओलंपिक खेल होने से बीसीसीआई के अधिनियम की मान्यता व्यवस्था के अंतर्गत आने की अपेक्षा है।",
  "National Sports Governance Act, 2025; Ministry of Youth Affairs and Sports (PIB, 2025).",
  "l3-t6-pol-national-sports-governance-act", craft="precision")

# ---------------------------------------------------------------- Union & State Executive (m-stmt)
S("Union & State Executive", "medium", "With reference to the government of the Union Territory of Jammu and Kashmir, consider the following statements:",
  "जम्मू और कश्मीर संघ राज्यक्षेत्र की सरकार के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["In 2024 the Union amended the rules of business of the Union Territory to require proposals on police, the All India Services and the appointment of the Advocate-General to be placed before the Lieutenant Governor.",
   "The Legislative Assembly of the Union Territory can make laws on police and public order."],
  ["2024 में संघ ने संघ राज्यक्षेत्र के कार्य-संचालन नियमों में संशोधन कर अपेक्षा की कि पुलिस, अखिल भारतीय सेवाओं और महाधिवक्ता की नियुक्ति से जुड़े प्रस्ताव उपराज्यपाल के सामने रखे जाएँ।",
   "संघ राज्यक्षेत्र की विधानसभा पुलिस और लोक व्यवस्था पर क़ानून बना सकती है।"],
  T2, 0,
  "Only statement 1 is correct. The Jammu and Kashmir Reorganisation Act, 2019 gives the Lieutenant Governor, who acts on the Union's behalf, the final say on police, public order and the All India Services; the 2024 amendments to the Transaction of Business Rules, made under the Act, spelt out that proposals on these matters, on the Anti-Corruption Bureau, on sanction for prosecution and on appointing the Advocate-General and law officers must go to the Lieutenant Governor through the Chief Secretary. "
  "Statement 2 is wrong: section 32 of the Act lets the Assembly legislate on State List matters except public order and police (Entries 1 and 2), which remain with Parliament -- a structure similar to Delhi's under Article 239AA. The elected government formed after the 2024 Assembly election therefore works within narrower limits than a State government until statehood is restored.",
  "केवल कथन 1 सही है। जम्मू और कश्मीर पुनर्गठन अधिनियम, 2019 संघ की ओर से कार्य करने वाले उपराज्यपाल को पुलिस, लोक व्यवस्था और अखिल भारतीय सेवाओं पर अंतिम अधिकार देता है; अधिनियम के अंतर्गत बने कार्य-संचालन नियमों में 2024 के संशोधनों ने स्पष्ट किया कि इन विषयों, भ्रष्टाचार-निरोधक ब्यूरो, अभियोजन की स्वीकृति और महाधिवक्ता तथा विधि अधिकारियों की नियुक्ति से जुड़े प्रस्ताव मुख्य सचिव के माध्यम से उपराज्यपाल के पास जाएँ। "
  "कथन 2 ग़लत है: अधिनियम की धारा 32 विधानसभा को राज्य सूची के विषयों पर क़ानून बनाने देती है, सिवाय लोक व्यवस्था और पुलिस (प्रविष्टि 1 और 2) के, जो संसद के पास रहते हैं -- अनुच्छेद 239AA के अंतर्गत दिल्ली जैसी संरचना। इसलिए 2024 के विधानसभा चुनाव के बाद बनी निर्वाचित सरकार राज्य का दर्जा बहाल होने तक किसी राज्य सरकार से संकरी सीमाओं में काम करती है।",
  "Jammu and Kashmir Reorganisation Act, 2019, sections 32 and 53-55; Ministry of Home Affairs, amendments to the Transaction of Business of the Government of Union Territory of Jammu and Kashmir Rules (2024).",
  "l3-t6-pol-jk-business-rules-lg", craft="precision")

# ---------------------------------------------------------------- Fundamental Rights, DPSP & Duties (m-stmt)
S("Fundamental Rights, DPSP & Duties", "medium", "With reference to the Uniform Civil Code of Uttarakhand, consider the following statements:",
  "उत्तराखंड की समान नागरिक संहिता के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:",
  ["Uttarakhand became the first State to enact and enforce a uniform civil code after Independence.",
   "The code requires live-in relationships to be registered.",
   "The code applies equally to the members of the Scheduled Tribes of the State."],
  ["उत्तराखंड स्वतंत्रता के बाद समान नागरिक संहिता बनाने और लागू करने वाला पहला राज्य बना।",
   "संहिता लिव-इन संबंधों के पंजीकरण को अनिवार्य बनाती है।",
   "संहिता राज्य की अनुसूचित जनजातियों के सदस्यों पर भी समान रूप से लागू होती है।"],
  C3, 1,
  "Statements 1 and 2 are correct. Article 44 directs the State to 'endeavour to secure' a uniform civil code, and Uttarakhand's code, passed in 2024 and in force from January 2025, sets common rules on marriage, divorce, succession and inheritance for its residents, bans polygamy, makes the registration of marriages compulsory and requires couples in live-in relationships to register them. Goa's civil code is older: it is the Portuguese code of 1867, which continued in force after Goa became part of India. "
  "Statement 3 is wrong: the code expressly excludes the Scheduled Tribes, whose customary laws are protected, and the exclusion is often cited in the debate over whether a 'uniform' code can respect the diversity that Articles 371A and the Fifth and Sixth Schedules recognise. Because personal laws fall in the Concurrent List (Entry 5), a State code that departs from central laws on these subjects needs the President's assent under Article 254(2) to prevail in the State -- which the Uttarakhand code received.",
  "कथन 1 और 2 सही हैं। अनुच्छेद 44 राज्य को समान नागरिक संहिता के लिए ‘प्रयास करने’ का निर्देश देता है, और उत्तराखंड की संहिता, जो 2024 में पारित हुई और जनवरी 2025 से लागू है, अपने निवासियों के लिए विवाह, तलाक़, उत्तराधिकार और विरासत पर साझा नियम तय करती है, बहुविवाह पर रोक लगाती है, विवाहों का पंजीकरण अनिवार्य करती है और लिव-इन संबंधों में रहने वाले जोड़ों से उनका पंजीकरण करवाती है। गोवा की नागरिक संहिता पुरानी है: यह 1867 की पुर्तगाली संहिता है, जो गोवा के भारत का भाग बनने के बाद भी लागू रही। "
  "कथन 3 ग़लत है: संहिता अनुसूचित जनजातियों को स्पष्ट रूप से बाहर रखती है, जिनके प्रथागत क़ानून संरक्षित हैं, और यह अपवर्जन अक्सर इस बहस में उद्धृत होता है कि क्या एक ‘समान’ संहिता उस विविधता का सम्मान कर सकती है जिसे अनुच्छेद 371A और पाँचवीं तथा छठी अनुसूचियाँ मान्यता देती हैं। चूँकि व्यक्तिगत क़ानून समवर्ती सूची (प्रविष्टि 5) में हैं, इन विषयों पर केंद्रीय क़ानूनों से भिन्न राज्य संहिता को राज्य में प्रभावी होने के लिए अनुच्छेद 254(2) के अंतर्गत राष्ट्रपति की अनुमति चाहिए -- जो उत्तराखंड की संहिता को मिली।",
  f"Uniform Civil Code, Uttarakhand, 2024; {COI}, Articles 44 and 254, Seventh Schedule, List III, Entry 5.",
  "l3-t6-pol-uttarakhand-ucc", craft="linkage")

write("gs_l3_t6_a.sql")
