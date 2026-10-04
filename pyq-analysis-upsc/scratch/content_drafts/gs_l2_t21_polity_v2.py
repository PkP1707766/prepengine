# -*- coding: utf-8 -*-
"""Level 2 · Test 21 -- Polity block, rewritten to the depth standard of October 2026
(docs/upsc-question-design-standard.md §6). It updates the 15 draft rows of gs_l2_t21_polity.py in place:
same concepts, same blueprint cells (medium statement 5, hard statement 3, medium MCQ 2, easy statement 1,
hard MCQ 1, hard Statement-I/II 1, medium Statement-I/II 1, medium pairs 1).
What changed: most rows now make the student apply a provision to a case or reason from a holding, instead of
recalling three loose facts about one body.
  - Committees: three situations, each to be routed to its committee.
  - Deputy PM: why Devi Lal's oath survived.
  - Arts 285/289: three tax cases.
  - Art 258: a Union law loading duties on State police.
  - Kaushal Kishor: a minister's remark tested against the holding.
  - NCW: what the Commission can and cannot do on a complaint.
  - Privy purses: why an amendment was unavoidable.
Craft mix: application 5, precision 5, linkage 2, inference 1, recall 2."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write_updates, CODE
from polity_common import C3, C4, T2

d.SUBJECT = "Polity"
d.REQUIRE_CRAFT = True
PL = "Parliament & State Legislature"
EX = "Union & State Executive"
CF = "Constitutional Framework"
FE = "Federalism & Special Provisions"
PR = "Panchayati Raj & Local Governance"
JV = "Judicial-Verdicts"
FR = "Fundamental Rights, DPSP & Duties"
GV = "Governance"
SL = "Statutory-Laws"
BO = "Constitutional & Statutory Bodies"
COI = "Constitution of India"
SC = "Supreme Court of India"
LSR = "Rules of Procedure and Conduct of Business in Lok Sabha"
LSS = "Lok Sabha Secretariat -- Practice and Procedure of Parliament"
MOPA = "Ministry of Parliamentary Affairs"
NC = "NCERT Class XI, Political Science -- Indian Constitution at Work"
MATCHED = "How many of the above are correctly matched?"
MATCHED_HI = "उपर्युक्त में से कितने सही सुमेलित हैं?"

# ================================================================ PARLIAMENT (3)
S(PL, "hard", "Consider the following situations in the Lok Sabha and the committee named against each:",
  "लोकसभा की निम्नलिखित स्थितियों और प्रत्येक के सामने दी गई समिति पर विचार कीजिए:",
  ["A minister's promise on the floor of the House to place a report before it within a month is still unfulfilled six months later -- Committee on Government Assurances.",
   "Rules framed by a ministry under an Act prescribe a penalty that the Act itself does not authorise -- Committee on Government Assurances.",
   "A proposal to change the House's procedure for asking and answering questions -- Business Advisory Committee."],
  ["सदन में एक महीने के भीतर एक रिपोर्ट रखने का मंत्री का वादा छह महीने बाद भी पूरा नहीं हुआ -- सरकारी आश्वासन समिति।",
   "किसी अधिनियम के तहत एक मंत्रालय के बनाए नियम ऐसा दंड तय करते हैं जिसकी अनुमति स्वयं अधिनियम नहीं देता -- सरकारी आश्वासन समिति।",
   "प्रश्न पूछने और उत्तर देने की सदन की प्रक्रिया बदलने का प्रस्ताव -- कार्य मंत्रणा समिति।"],
  C3, 0,
  "Only the first is correctly matched. The Committee on Government Assurances tracks the promises and undertakings ministers give on the floor, and reports on whether they have been kept. "
  "The second situation belongs to the Committee on Subordinate Legislation, which checks whether rules, regulations and bye-laws made under an Act stay within the powers Parliament delegated; a penalty that the parent Act does not authorise is a classic excess. "
  "The third belongs to the Rules Committee, headed by the Speaker, which considers changes to the House's procedure. The Business Advisory Committee only recommends how much time to give to Bills and other business.",
  "केवल पहला सही सुमेलित है। सरकारी आश्वासन समिति मंत्रियों द्वारा सदन में दिए गए वादों और वचनों पर नज़र रखती है और बताती है कि वे पूरे हुए या नहीं। "
  "दूसरी स्थिति अधीनस्थ विधान समिति की है, जो जाँचती है कि अधिनियम के तहत बने नियम, विनियम और उपविधियाँ संसद द्वारा सौंपी गई शक्तियों की सीमा में हैं या नहीं; मूल अधिनियम जिस दंड की अनुमति नहीं देता, वह सीमा लाँघने का सीधा उदाहरण है। "
  "तीसरी स्थिति अध्यक्ष की अध्यक्षता वाली नियम समिति की है, जो सदन की प्रक्रिया में बदलावों पर विचार करती है। कार्य मंत्रणा समिति केवल यह सिफ़ारिश करती है कि विधेयकों और अन्य कार्यों को कितना समय दिया जाए।",
  f"{LSR} -- parliamentary committees; {LSS}.",
  "parl-committees-subleg-assurances-rules", closing=MATCHED, closing_hi=MATCHED_HI, craft="application")

S(PL, "medium", "Consider the following statements about the party whip and the Tenth Schedule:",
  "दलीय सचेतक (व्हिप) और दसवीं अनुसूची के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["A member who votes against the party's direction without its permission escapes disqualification if the party condones the act within fifteen days.",
   "The Tenth Schedule's rule on voting applies only to votes on confidence motions and Money Bills, not to votes on ordinary Bills."],
  ["दल की अनुमति के बिना उसके निर्देश के विरुद्ध मतदान करने वाला सदस्य अयोग्यता से बच जाता है, यदि दल पंद्रह दिनों के भीतर उस कार्य को माफ़ कर दे।",
   "दसवीं अनुसूची का मतदान संबंधी नियम केवल विश्वास प्रस्तावों और धन विधेयकों पर मतदान पर लागू होता है, साधारण विधेयकों पर नहीं।"],
  T2, 0,
  "Only statement 1 is correct. Paragraph 2(1)(b) of the Tenth Schedule makes voting or abstaining against the party's direction, without prior permission, a ground for disqualification, unless the party condones it within fifteen days. "
  "Statement 2 is wrong: the rule applies to any vote in the House, ordinary Bills included. Confining it to confidence motions and Money Bills has been recommended by committees on electoral reform, so that members could vote their conscience on ordinary laws, but it has never been adopted.",
  "केवल कथन 1 सही है। दसवीं अनुसूची का अनुच्छेद 2(1)(ख) दल के निर्देश के विरुद्ध बिना पूर्व अनुमति मतदान करने या मतदान से अलग रहने को अयोग्यता का आधार बनाता है, जब तक दल पंद्रह दिनों के भीतर उसे माफ़ न कर दे। "
  "कथन 2 गलत है: यह नियम सदन के हर मतदान पर लागू होता है, साधारण विधेयकों सहित। इसे विश्वास प्रस्तावों और धन विधेयकों तक सीमित करने की सिफ़ारिश चुनाव सुधार संबंधी समितियाँ कर चुकी हैं, ताकि सदस्य साधारण क़ानूनों पर अपनी अंतरात्मा से मत दे सकें, पर यह कभी अपनाई नहीं गई।",
  f"{COI} -- Tenth Schedule, paragraph 2; {LSS}.",
  "parl-whip-tenth-schedule-condonation", craft="precision")

S(PL, "medium", "Consider the following statements about the Consultative Committees of Members of Parliament attached to Union ministries:",
  "केंद्रीय मंत्रालयों से जुड़ी संसद सदस्यों की परामर्शदात्री समितियों के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["They are constituted by the Ministry of Parliamentary Affairs, and each is chaired by the minister of the ministry concerned.",
   "Their membership is fixed by the Speaker in proportion to party strength, as with the financial committees.",
   "Their reports are presented to the House and discussed like those of other parliamentary committees."],
  ["इनका गठन संसदीय कार्य मंत्रालय करता है, और प्रत्येक की अध्यक्षता संबंधित मंत्रालय के मंत्री करते हैं।",
   "वित्तीय समितियों की तरह इनकी सदस्यता अध्यक्ष दलों की संख्या के अनुपात में तय करते हैं।",
   "अन्य संसदीय समितियों की तरह इनकी रिपोर्टें सदन में प्रस्तुत की जाती हैं और उन पर चर्चा होती है।"],
  C3, 0,
  "Only statement 1 is correct. Because they are set up by a ministry of the Government and chaired by a minister, the Consultative Committees are not parliamentary committees in the strict sense; they are a forum for informal talks between the Government and members of both Houses on a ministry's policies and programmes. "
  "Statement 2 is wrong: membership is voluntary, left to the choice of members and their party leaders. "
  "Statement 3 is wrong: they present no reports to the House. Their value lies in the dialogue itself, and they meet both during and between sessions.",
  "केवल कथन 1 सही है। चूँकि इनका गठन सरकार का एक मंत्रालय करता है और अध्यक्षता एक मंत्री करते हैं, इसलिए परामर्शदात्री समितियाँ कड़े अर्थ में संसदीय समितियाँ नहीं हैं; ये किसी मंत्रालय की नीतियों और कार्यक्रमों पर सरकार और दोनों सदनों के सदस्यों के बीच अनौपचारिक चर्चा का मंच हैं। "
  "कथन 2 गलत है: सदस्यता स्वैच्छिक है और सदस्यों तथा उनके दलों के नेताओं की पसंद पर छोड़ी जाती है। "
  "कथन 3 गलत है: ये सदन में कोई रिपोर्ट प्रस्तुत नहीं करतीं। इनका महत्व संवाद में ही है, और ये सत्र के दौरान तथा दो सत्रों के बीच, दोनों समय बैठती हैं।",
  f"{MOPA} -- Consultative Committees of Members of Parliament; {LSS}.",
  "parl-consultative-committees-mopa", craft="precision")

# ================================================================ EXECUTIVE (1)
M(EX, "hard", "In K.M. Sharma v. Devi Lal (1990), the Supreme Court upheld the oath that Devi Lal took as 'Deputy Prime Minister'. Which one of the following best explains the Court's reasoning?",
  "के.एम. शर्मा बनाम देवी लाल (1990) में सर्वोच्च न्यायालय ने 'उप-प्रधानमंत्री' के रूप में देवी लाल की शपथ को वैध ठहराया। निम्नलिखित में से कौन-सा न्यायालय के तर्क की सबसे सही व्याख्या करता है?",
  ["The title was only descriptive: in substance he took a minister's oath and gained no power beyond a minister's.",
   "The Prime Minister may create offices by convention, and the President must administer whatever oath the Prime Minister advises.",
   "The Third Schedule allows the Council of Ministers to add oaths for new offices that it creates by resolution.",
   "Article 75 implicitly recognises a deputy who heads the Council of Ministers whenever the Prime Minister is absent."],
  ["यह पदनाम केवल वर्णनात्मक था: सार रूप में उन्होंने मंत्री की शपथ ली और उन्हें मंत्री से अधिक कोई शक्ति नहीं मिली।",
   "प्रधानमंत्री परंपरा से पद बना सकते हैं, और राष्ट्रपति को वही शपथ दिलानी होती है जिसकी सलाह प्रधानमंत्री दें।",
   "तीसरी अनुसूची मंत्रिपरिषद को संकल्प द्वारा बनाए गए नए पदों के लिए शपथें जोड़ने की अनुमति देती है।",
   "अनुच्छेद 75 अप्रत्यक्ष रूप से ऐसे उप-प्रमुख को मान्यता देता है जो प्रधानमंत्री की अनुपस्थिति में मंत्रिपरिषद का नेतृत्व करे।"],
  0,
  "The Court held that calling Devi Lal 'Deputy Prime Minister' did not change the substance of what he swore to, which was the oath of a member of the Council of Ministers in the form the Third Schedule prescribes. The title carried no constitutional power, so the oath was valid. "
  "Nothing in the Constitution creates the office, there is no separate oath for it, and it gives no right to head the Council or to succeed the Prime Minister. It has remained a political title, held for example by Sardar Patel, Morarji Desai and L.K. Advani.",
  "न्यायालय ने कहा कि देवी लाल को 'उप-प्रधानमंत्री' कहने से उनकी शपथ का सार नहीं बदला, जो तीसरी अनुसूची में निर्धारित रूप में मंत्रिपरिषद के सदस्य की ही शपथ थी। इस पदनाम के साथ कोई संवैधानिक शक्ति नहीं जुड़ी थी, इसलिए शपथ वैध थी। "
  "संविधान में यह पद कहीं नहीं बनाया गया, इसकी कोई अलग शपथ नहीं है, और इससे मंत्रिपरिषद का नेतृत्व करने या प्रधानमंत्री का उत्तराधिकारी बनने का कोई अधिकार नहीं मिलता। यह एक राजनीतिक पदनाम ही रहा है, जो उदाहरण के लिए सरदार पटेल, मोरारजी देसाई और लालकृष्ण आडवाणी के पास रहा।",
  f"{SC} -- K.M. Sharma v. Devi Lal (1990); {COI}, Articles 74-75 and the Third Schedule.",
  "exec-deputy-pm-devi-lal", craft="inference")

# ================================================================ CONSTITUTIONAL FRAMEWORK (2)
S(CF, "hard", "Consider the following statements about the abolition of privy purses:",
  "प्रिवी पर्स (privy purse) की समाप्ति के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["A constitutional amendment became necessary because the Supreme Court had struck down the executive order derecognising the rulers.",
   "Since privy purses were charged on the Consolidated Fund of India, Parliament could not refuse them through its annual vote on demands for grants.",
   "The 26th Amendment (1971) omitted the Articles that had guaranteed the purses and the rulers' privileges, and inserted a new Article ending their recognition."],
  ["संविधान संशोधन इसलिए आवश्यक हो गया क्योंकि सर्वोच्च न्यायालय ने शासकों की मान्यता समाप्त करने वाला कार्यकारी आदेश रद्द कर दिया था।",
   "चूँकि प्रिवी पर्स भारत की संचित निधि पर भारित थे, इसलिए संसद अनुदान माँगों पर अपने वार्षिक मतदान से उन्हें अस्वीकार नहीं कर सकती थी।",
   "26वें संशोधन (1971) ने पर्स और शासकों के विशेषाधिकारों की गारंटी देने वाले अनुच्छेद हटाए और उनकी मान्यता समाप्त करने वाला एक नया अनुच्छेद जोड़ा।"],
  C3, 2,
  "All three are correct, and they link up. When a Bill to end the purses fell short in the Rajya Sabha in 1970, the President derecognised the rulers by order; in Madhav Rao Scindia v. Union of India (1970) the Supreme Court struck that order down, so only an amendment could end the guarantee. "
  "The purses were charged on the Consolidated Fund under Article 291, which is exactly why they could not be voted down year by year. "
  "The 26th Amendment omitted Articles 291 and 362 and inserted Article 363A, ending both the recognition and the purses.",
  "तीनों कथन सही हैं, और ये आपस में जुड़े हैं। 1970 में पर्स समाप्त करने वाला विधेयक राज्यसभा में पारित नहीं हो सका, तो राष्ट्रपति ने आदेश से शासकों की मान्यता समाप्त की; माधवराव सिंधिया बनाम भारत संघ (1970) में सर्वोच्च न्यायालय ने वह आदेश रद्द कर दिया, इसलिए गारंटी केवल संशोधन से ही समाप्त हो सकती थी। "
  "अनुच्छेद 291 के तहत पर्स संचित निधि पर भारित थे, और ठीक इसी कारण उन्हें हर वर्ष मतदान से अस्वीकार नहीं किया जा सकता था। "
  "26वें संशोधन ने अनुच्छेद 291 और 362 हटाए और अनुच्छेद 363A जोड़ा, जिससे मान्यता और पर्स दोनों समाप्त हुए।",
  f"{COI} -- Articles 291, 362 and 363A; {SC} -- Madhav Rao Scindia v. Union of India (1970).",
  "cf-privy-purses-26th-amendment", craft="linkage")

A(CF, "medium",
  "All provisions of the Constitution of India came into force on 26 January 1950.",
  "भारत के संविधान के सभी प्रावधान 26 जनवरी 1950 को लागू हुए।",
  "Article 394 lists the provisions that came into force on 26 November 1949, the day the Constitution was adopted.",
  "अनुच्छेद 394 उन प्रावधानों को गिनाता है जो 26 नवंबर 1949 को, यानी संविधान अंगीकार किए जाने के दिन ही, लागू हो गए।",
  3,
  "Statement-I is incorrect but Statement-II is correct. Article 394 brought some provisions into force at once on 26 November 1949: those on citizenship (Articles 5-9), the oath of the President (Article 60), elections (Article 324), definitions and interpretation, the provisional Parliament and other transitional provisions, and the short title and commencement themselves. "
  "The rest of the Constitution came into force on 26 January 1950, a date chosen to mark the anniversary of the Purna Swaraj pledge of 1930.",
  "कथन-I गलत है पर कथन-II सही है। अनुच्छेद 394 ने कुछ प्रावधान 26 नवंबर 1949 को ही लागू कर दिए: नागरिकता (अनुच्छेद 5-9), राष्ट्रपति की शपथ (अनुच्छेद 60), चुनाव (अनुच्छेद 324), परिभाषाएँ और निर्वचन, अंतरिम संसद तथा अन्य संक्रमणकालीन प्रावधान, और स्वयं संक्षिप्त नाम तथा प्रारंभ से जुड़े प्रावधान। "
  "संविधान का शेष भाग 26 जनवरी 1950 को लागू हुआ; यह तिथि 1930 की पूर्ण स्वराज प्रतिज्ञा की वर्षगाँठ के रूप में चुनी गई।",
  f"{COI} -- Article 394; {NC}.",
  "cf-art394-commencement", craft="precision")

# ================================================================ FEDERALISM (2)
S(FE, "medium", "Consider the following cases:",
  "निम्नलिखित मामलों पर विचार कीजिए:",
  ["A municipal corporation levies property tax on an office building owned by the Union government, though no law of Parliament permits it.",
   "Parliament taxes the profits of a lottery business run by a State government, and has not declared that business incidental to the ordinary functions of government.",
   "Parliament taxes the rent that a State government earns by letting out its own buildings."],
  ["एक नगर निगम केंद्र सरकार के स्वामित्व वाले कार्यालय भवन पर संपत्ति कर लगाता है, यद्यपि संसद का कोई क़ानून इसकी अनुमति नहीं देता।",
   "संसद एक राज्य सरकार द्वारा चलाए जा रहे लॉटरी कारोबार के लाभ पर कर लगाती है, और उसने उस कारोबार को सरकार के सामान्य कार्यों का आनुषंगिक घोषित नहीं किया है।",
   "संसद उस किराए पर कर लगाती है जो एक राज्य सरकार अपने भवन किराए पर देकर कमाती है।"],
  None, 1,
  "Only case 2 is permitted. Under Article 285, property of the Union is exempt from all taxes imposed by a State or by any authority within a State unless Parliament by law provides otherwise, so the municipal property tax in case 1 cannot be levied; in practice the Union pays service charges instead. "
  "Article 289(1) exempts the property and income of a State from Union taxation, which rules out case 3. "
  "Clause (2) of the same Article, however, lets Parliament tax a trade or business carried on by or on behalf of a State, as in case 2, unless Parliament declares that business incidental to the ordinary functions of government.",
  "केवल मामला 2 अनुमत है। अनुच्छेद 285 के तहत संघ की संपत्ति राज्य या राज्य के भीतर किसी भी प्राधिकरण द्वारा लगाए गए सभी करों से मुक्त है, जब तक संसद क़ानून द्वारा अन्यथा प्रावधान न करे; इसलिए मामला 1 का नगरपालिका संपत्ति कर नहीं लगाया जा सकता, और व्यवहार में संघ इसके बदले सेवा शुल्क चुकाता है। "
  "अनुच्छेद 289(1) राज्य की संपत्ति और आय को संघ के कराधान से मुक्त रखता है, जिससे मामला 3 बाहर हो जाता है। "
  "पर उसी अनुच्छेद का खंड (2) संसद को राज्य द्वारा या उसकी ओर से चलाए गए व्यापार या कारोबार पर कर लगाने देता है, जैसा मामला 2 में है, जब तक संसद उस कारोबार को सरकार के सामान्य कार्यों का आनुषंगिक घोषित न कर दे।",
  f"{COI} -- Articles 285 and 289.",
  "fed-art285-289-290a", opts=["1 only", "2 only", "2 and 3 only", "1, 2 and 3"], opts_hi=["केवल 1", "केवल 2", "केवल 2 और 3", "1, 2 और 3"],
  closing="In which of the above cases is the tax permitted by the Constitution?",
  closing_hi="उपर्युक्त में से किस/किन मामले/मामलों में कर संविधान द्वारा अनुमत है?", craft="application")

S(FE, "hard", "Parliament enacts a law on a subject in the Union List that requires the police of every State to verify applicants for a licence, and one State objects. Consider the following statements:",
  "संसद संघ सूची के एक विषय पर ऐसा क़ानून बनाती है जिसमें हर राज्य की पुलिस को किसी लाइसेंस के आवेदकों का सत्यापन करना होता है, और एक राज्य इस पर आपत्ति करता है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The law can impose this duty on the State's officers even without the State's consent.",
   "The Union must pay the State the extra costs of administration that the duty causes.",
   "If the Union and the State cannot agree on that amount, the President decides it."],
  ["यह क़ानून राज्य की सहमति के बिना भी राज्य के अधिकारियों पर यह कर्तव्य डाल सकता है।",
   "इस कर्तव्य से होने वाला प्रशासन का अतिरिक्त ख़र्च संघ को राज्य को चुकाना होगा।",
   "यदि संघ और राज्य उस राशि पर सहमत न हों, तो राष्ट्रपति उसे तय करते हैं।"],
  C3, 1,
  "Statements 1 and 2 are correct. Article 258(2) lets a law of Parliament on a Union List matter confer powers and impose duties on a State or its officers whether or not the State agrees, and Article 258(3) then requires the Union to pay the extra costs of administration. "
  "Statement 3 is wrong: the amount is settled by agreement or, failing that, by an arbitrator appointed by the Chief Justice of India. "
  "Transfers by consent run both ways: under Article 258(1) the President may entrust Union functions to a willing State, and under Article 258A a Governor may, with the Union's consent, entrust State functions to the Union.",
  "कथन 1 और 2 सही हैं। अनुच्छेद 258(2) संघ सूची के विषय पर संसद के क़ानून को राज्य या उसके अधिकारियों को शक्तियाँ देने और उन पर कर्तव्य डालने देता है, चाहे राज्य सहमत हो या नहीं, और अनुच्छेद 258(3) संघ से प्रशासन का अतिरिक्त ख़र्च चुकाने की अपेक्षा करता है। "
  "कथन 3 गलत है: राशि आपसी सहमति से, और ऐसा न होने पर भारत के मुख्य न्यायाधीश द्वारा नियुक्त मध्यस्थ द्वारा तय होती है। "
  "सहमति से हस्तांतरण दोनों ओर चलता है: अनुच्छेद 258(1) के तहत राष्ट्रपति सहमत राज्य को संघ के कार्य सौंप सकते हैं, और अनुच्छेद 258A के तहत राज्यपाल संघ की सहमति से राज्य के कार्य संघ को सौंप सकते हैं।",
  f"{COI} -- Articles 258 and 258A; {NC}.",
  "fed-art258-258a-entrustment", craft="application")

# ================================================================ LOCAL GOVERNANCE (1)
P(PR, "medium", "Consider the following pairs of urban bodies and their features:",
  "नगरीय निकायों और उनकी विशेषताओं के निम्नलिखित युग्मों पर विचार कीजिए:",
  ["Cantonment board : Works under the Ministry of Defence",
   "Notified area committee : Members elected under a notification of the State Election Commission",
   "Township : Set up by a large public enterprise to run its staff colony",
   "Special purpose agency : Runs all the municipal functions of a large city"],
  ["छावनी बोर्ड : रक्षा मंत्रालय के अधीन कार्य करता है",
   "अधिसूचित क्षेत्र समिति : राज्य निर्वाचन आयोग की अधिसूचना के तहत निर्वाचित सदस्य",
   "टाउनशिप : किसी बड़े सार्वजनिक उपक्रम द्वारा अपनी कर्मचारी बस्ती चलाने के लिए स्थापित",
   "विशेष प्रयोजन अभिकरण : किसी बड़े नगर के सभी नगरपालिका कार्य चलाता है"],
  1,
  "Only the first and third pairs are correct. Cantonment boards, under the Cantonments Act, 2006, govern the civil population of military stations; they have elected as well as ex officio and nominated members and work under the Ministry of Defence. "
  "A notified area committee is set up by a State government notification for a new or fast-growing town that does not yet meet the conditions for a municipality; all its members, including the chairperson, are nominated by the State government. "
  "A township is run by a town administrator appointed by the enterprise that built it, with no elected members. Special purpose agencies, such as housing boards or water supply boards, handle one designated function, not the whole range of municipal work.",
  "केवल पहला और तीसरा युग्म सही है। छावनी अधिनियम, 2006 के तहत छावनी बोर्ड सैन्य स्टेशनों की नागरिक आबादी का प्रशासन करते हैं; इनमें निर्वाचित के साथ पदेन और मनोनीत सदस्य होते हैं और ये रक्षा मंत्रालय के अधीन काम करते हैं। "
  "अधिसूचित क्षेत्र समिति राज्य सरकार की अधिसूचना से किसी नए या तेज़ी से बढ़ते क़स्बे के लिए बनाई जाती है जो अभी नगरपालिका की शर्तें पूरी नहीं करता; इसके अध्यक्ष सहित सभी सदस्य राज्य सरकार द्वारा मनोनीत होते हैं। "
  "टाउनशिप उसे बसाने वाले उपक्रम द्वारा नियुक्त नगर प्रशासक चलाता है और इसमें कोई निर्वाचित सदस्य नहीं होता। आवास बोर्ड या जल आपूर्ति बोर्ड जैसे विशेष प्रयोजन अभिकरण एक निर्धारित कार्य सँभालते हैं, नगरपालिका के सभी कार्य नहीं।",
  f"Cantonments Act, 2006; {NC} -- Local Governments.",
  "ulb-types-cantonment-notified-township-spa", craft="precision")

# ================================================================ VERDICTS (1)
S(JV, "medium", "A State minister makes a public statement disparaging a survivor of sexual assault. In the light of the Supreme Court's judgment in Kaushal Kishor v. State of Uttar Pradesh (2023), consider the following statements:",
  "एक राज्य मंत्री यौन हिंसा की एक पीड़िता के बारे में सार्वजनिक रूप से अपमानजनक बयान देते हैं। कौशल किशोर बनाम उत्तर प्रदेश राज्य (2023) में सर्वोच्च न्यायालय के निर्णय के आलोक में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The minister's speech cannot be restricted on a ground that is not listed in Article 19(2).",
   "The State government becomes vicariously liable for the statement because ministers are collectively responsible.",
   "If officials, acting on the statement, cause harm to the survivor, a claim in constitutional tort may lie."],
  ["मंत्री की अभिव्यक्ति पर ऐसे किसी आधार पर प्रतिबंध नहीं लगाया जा सकता जो अनुच्छेद 19(2) में न हो।",
   "मंत्रियों के सामूहिक उत्तरदायित्व के कारण राज्य सरकार उस बयान के लिए प्रतिनिधिक रूप से (vicariously) उत्तरदायी हो जाती है।",
   "यदि उस बयान पर चलते हुए अधिकारी पीड़िता को हानि पहुँचाएँ, तो संवैधानिक अपकृत्य (constitutional tort) का दावा बन सकता है।"],
  C3, 1,
  "Statements 1 and 3 are correct. The Constitution Bench held by 4:1 that the grounds in Article 19(2) are exhaustive, so no further restriction, for instance on the ground of the dignity of office, can be read in. "
  "It also held that a minister's statement, even one relating to the affairs of the State, cannot be attributed vicariously to the Government by invoking collective responsibility. "
  "A mere statement is not a constitutional tort, but if officials act on it and the person is harmed, a claim in constitutional tort may lie. The Court further held that Articles 19 and 21 can be enforced against private persons too.",
  "कथन 1 और 3 सही हैं। संविधान पीठ ने 4:1 से कहा कि अनुच्छेद 19(2) के आधार संपूर्ण हैं, इसलिए कोई अतिरिक्त प्रतिबंध, जैसे पद की गरिमा के आधार पर, उसमें नहीं जोड़ा जा सकता। "
  "उसने यह भी कहा कि मंत्री का बयान, भले ही राज्य के कामकाज से जुड़ा हो, सामूहिक उत्तरदायित्व के नाम पर सरकार पर प्रतिनिधिक रूप से नहीं डाला जा सकता। "
  "केवल बयान संवैधानिक अपकृत्य नहीं है, पर यदि अधिकारी उस पर चलते हुए किसी को हानि पहुँचाएँ, तो संवैधानिक अपकृत्य का दावा बन सकता है। न्यायालय ने यह भी कहा कि अनुच्छेद 19 और 21 निजी व्यक्तियों के विरुद्ध भी लागू कराए जा सकते हैं।",
  f"{SC} -- Kaushal Kishor v. State of Uttar Pradesh (2023).",
  "verdicts-kaushal-kishor-2023", craft="application")

# ================================================================ FUNDAMENTAL RIGHTS (1)
S(FR, "medium", "Consider the following statements about how far Articles 19 and 21 reach:",
  "अनुच्छेद 19 और 21 की पहुँच के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["In Anuradha Bhasin v. Union of India (2020), the Supreme Court held that orders suspending internet services must be published and reviewed periodically.",
   "In Subramanian Swamy v. Union of India (2016), the Supreme Court struck down criminal defamation as an unreasonable restriction on free speech.",
   "In the Ramlila Maidan case (2012), the Supreme Court treated the right to sleep as part of the right to life under Article 21."],
  ["अनुराधा भसीन बनाम भारत संघ (2020) में सर्वोच्च न्यायालय ने कहा कि इंटरनेट सेवाएँ निलंबित करने वाले आदेश प्रकाशित किए जाएँ और समय-समय पर उनकी समीक्षा हो।",
   "सुब्रमण्यम स्वामी बनाम भारत संघ (2016) में सर्वोच्च न्यायालय ने आपराधिक मानहानि को अभिव्यक्ति की स्वतंत्रता पर अनुचित प्रतिबंध मानकर रद्द कर दिया।",
   "रामलीला मैदान मामले (2012) में सर्वोच्च न्यायालय ने नींद के अधिकार को अनुच्छेद 21 के तहत जीवन के अधिकार का भाग माना।"],
  C3, 1,
  "Statements 1 and 3 are correct. In Anuradha Bhasin the Court held that speech and trade over the internet are protected under Article 19(1)(a) and (g); a shutdown must therefore be necessary and proportionate, cannot be indefinite, and must be published and periodically reviewed so that it can be challenged. "
  "In Ramlila Maidan, a midnight police action against a sleeping crowd was held to violate the right to sleep, part of the right to life and personal liberty. "
  "Statement 2 reverses the holding: Subramanian Swamy upheld criminal defamation (now in the Bharatiya Nyaya Sanhita), reasoning that reputation is itself part of Article 21 and that defamation is a ground of restriction named in Article 19(2).",
  "कथन 1 और 3 सही हैं। अनुराधा भसीन में न्यायालय ने कहा कि इंटरनेट के माध्यम से अभिव्यक्ति और व्यापार अनुच्छेद 19(1)(क) और (छ) के तहत संरक्षित हैं; इसलिए इंटरनेट बंदी आवश्यक और आनुपातिक होनी चाहिए, अनिश्चितकालीन नहीं हो सकती, और उसे प्रकाशित कर समय-समय पर उसकी समीक्षा होनी चाहिए ताकि उसे चुनौती दी जा सके। "
  "रामलीला मैदान मामले में सोती भीड़ पर आधी रात की पुलिस कार्रवाई को नींद के अधिकार का उल्लंघन माना गया, जो प्राण और दैहिक स्वतंत्रता के अधिकार का भाग है। "
  "कथन 2 निर्णय को उलट देता है: सुब्रमण्यम स्वामी मामले में आपराधिक मानहानि (अब भारतीय न्याय संहिता में) को वैध ठहराया गया, इस तर्क पर कि प्रतिष्ठा स्वयं अनुच्छेद 21 का भाग है और मानहानि अनुच्छेद 19(2) में दिया गया प्रतिबंध का एक आधार है।",
  f"{SC} -- Anuradha Bhasin v. Union of India (2020); Subramanian Swamy v. Union of India (2016); In re Ramlila Maidan Incident (2012).",
  "rights-internet-defamation-sleep", craft="precision")

# ================================================================ GOVERNANCE (2)
M(GV, "medium", "'Jeevan Pramaan', a digital public service of the Government of India, is used for",
  "भारत सरकार की डिजिटल सार्वजनिक सेवा 'जीवन प्रमाण' का उपयोग किसके लिए होता है?",
  ["Digital life certificates for pensioners", "Telemedicine consultations with doctors",
   "Single-window green clearances for projects", "Free online courses from school to postgraduate level"],
  ["पेंशनभोगियों के डिजिटल जीवन प्रमाण-पत्र", "डॉक्टरों से टेलीमेडिसिन परामर्श",
   "परियोजनाओं के लिए एकल-खिड़की पर्यावरणीय मंज़ूरी", "स्कूल से स्नातकोत्तर स्तर तक निःशुल्क ऑनलाइन पाठ्यक्रम"],
  0,
  "Jeevan Pramaan (2014) lets pensioners submit their annual life certificate through Aadhaar-based fingerprint or face authentication, instead of appearing in person at a bank or office. "
  "Telemedicine is offered through e-Sanjeevani, environmental, forest and wildlife clearances through PARIVESH, and free online courses through SWAYAM.",
  "जीवन प्रमाण (2014) पेंशनभोगियों को बैंक या कार्यालय में स्वयं उपस्थित होने के बजाय आधार-आधारित फ़िंगरप्रिंट या चेहरा प्रमाणीकरण से वार्षिक जीवन प्रमाण-पत्र जमा करने देता है। "
  "टेलीमेडिसिन ई-संजीवनी के माध्यम से, पर्यावरण, वन और वन्यजीव मंज़ूरी परिवेश (PARIVESH) के माध्यम से, और निःशुल्क ऑनलाइन पाठ्यक्रम स्वयं (SWAYAM) के माध्यम से मिलते हैं।",
  "Department of Pension and Pensioners' Welfare -- Jeevan Pramaan; Ministry of Electronics and Information Technology.",
  "gov-jeevan-pramaan-digital-services", craft="recall")

S(GV, "easy", "Consider the following statements:",
  "निम्नलिखित कथनों पर विचार कीजिए:",
  ["The first phase of the Vibrant Villages Programme covers villages along India's northern land border.",
   "PM-JANMAN is aimed specifically at the Particularly Vulnerable Tribal Groups."],
  ["वाइब्रेंट विलेजेज़ कार्यक्रम का पहला चरण भारत की उत्तरी स्थल सीमा के गाँवों को शामिल करता है।",
   "पीएम-जनमन विशेष रूप से विशेष रूप से कमज़ोर जनजातीय समूहों (PVTGs) के लिए है।"],
  T2, 2,
  "Both statements are correct. The Vibrant Villages Programme (2023) develops thinly populated border villages in Arunachal Pradesh, Sikkim, Uttarakhand, Himachal Pradesh and Ladakh to improve livelihoods and slow outmigration; a second phase (2025) extends it to villages along other land borders. "
  "PM-JANMAN (2023) brings housing, roads, piped water, electricity, health and education facilities to the habitations of the 75 Particularly Vulnerable Tribal Groups, the most marginalised among the Scheduled Tribes.",
  "दोनों कथन सही हैं। वाइब्रेंट विलेजेज़ कार्यक्रम (2023) अरुणाचल प्रदेश, सिक्किम, उत्तराखंड, हिमाचल प्रदेश और लद्दाख के कम आबादी वाले सीमावर्ती गाँवों का विकास करता है ताकि आजीविका सुधरे और पलायन रुके; इसका दूसरा चरण (2025) अन्य स्थल सीमाओं के गाँवों तक इसका विस्तार करता है। "
  "पीएम-जनमन (2023) अनुसूचित जनजातियों में सबसे वंचित, 75 विशेष रूप से कमज़ोर जनजातीय समूहों की बस्तियों तक आवास, सड़क, नल का जल, बिजली, स्वास्थ्य और शिक्षा की सुविधाएँ पहुँचाता है।",
  "Ministry of Home Affairs -- Vibrant Villages Programme; Ministry of Tribal Affairs -- PM-JANMAN.",
  "gov-vibrant-villages-pm-janman", craft="recall")

# ================================================================ STATUTORY LAWS (1)
A(SL, "hard",
  "The Anusandhan National Research Foundation Act, 2023 repealed the Science and Engineering Research Board Act, 2008.",
  "अनुसंधान नेशनल रिसर्च फ़ाउंडेशन अधिनियम, 2023 ने विज्ञान और इंजीनियरी अनुसंधान बोर्ड अधिनियम, 2008 को निरस्त कर दिया।",
  "The Anusandhan National Research Foundation is expected to draw most of its projected funding for its first five years from non-government sources.",
  "अनुसंधान नेशनल रिसर्च फ़ाउंडेशन से अपेक्षा है कि वह अपने पहले पाँच वर्षों के अनुमानित वित्त का अधिकांश भाग ग़ैर-सरकारी स्रोतों से जुटाए।",
  1,
  "Both statements are correct, but Statement-II does not explain Statement-I. The 2023 Act set up the Foundation to fund and steer research across the natural sciences, engineering, social sciences and humanities, and it subsumed the Science and Engineering Research Board (SERB), whose Act was repealed; its governing board is headed by the Prime Minister. "
  "Of the roughly ₹50,000 crore projected for its first five years, about ₹36,000 crore was expected from industry and other non-government sources. SERB was folded in so that one apex body would fund research, not because of where the money would come from.",
  "दोनों कथन सही हैं, पर कथन-II कथन-I की व्याख्या नहीं करता। 2023 के अधिनियम ने प्राकृतिक विज्ञान, इंजीनियरी, सामाजिक विज्ञान और मानविकी में अनुसंधान को वित्त और दिशा देने के लिए फ़ाउंडेशन बनाया, और विज्ञान एवं इंजीनियरी अनुसंधान बोर्ड (SERB) को उसमें मिला दिया, जिसका अधिनियम निरस्त हुआ; इसके शासी बोर्ड के प्रमुख प्रधानमंत्री हैं। "
  "पहले पाँच वर्षों के लिए अनुमानित लगभग ₹50,000 करोड़ में से लगभग ₹36,000 करोड़ उद्योग और अन्य ग़ैर-सरकारी स्रोतों से आने की अपेक्षा थी। SERB को इसलिए मिलाया गया ताकि अनुसंधान को वित्त देने वाली एक शीर्ष संस्था हो, इसलिए नहीं कि पैसा कहाँ से आएगा।",
  "Anusandhan National Research Foundation Act, 2023; Department of Science and Technology.",
  "statute-anrf-act-2023", craft="linkage")

# ================================================================ BODIES (1)
M(BO, "medium", "A woman complains to the National Commission for Women that her employer has denied her maternity benefit. Which one of the following can the Commission itself do while looking into the complaint?",
  "एक महिला राष्ट्रीय महिला आयोग से शिकायत करती है कि उसके नियोक्ता ने उसे मातृत्व लाभ देने से मना कर दिया है। शिकायत की जाँच करते समय आयोग स्वयं निम्नलिखित में से क्या कर सकता है?",
  ["Summon the employer and require documents, using the powers of a civil court",
   "Order the employer to pay the benefit and impose a fine for the denial",
   "Set aside the employer's decision as void under the National Commission for Women Act",
   "Direct the Labour Court to decide the dispute within a fixed time"],
  ["दीवानी न्यायालय की शक्तियों का उपयोग कर नियोक्ता को बुलाना और दस्तावेज़ माँगना",
   "नियोक्ता को लाभ चुकाने का आदेश देना और इनकार के लिए जुर्माना लगाना",
   "राष्ट्रीय महिला आयोग अधिनियम के तहत नियोक्ता के निर्णय को शून्य घोषित कर रद्द करना",
   "श्रम न्यायालय को तय समय में विवाद निपटाने का निर्देश देना"],
  0,
  "While investigating a complaint, the NCW has the powers of a civil court trying a suit: it can summon and examine persons, require documents and receive evidence on affidavits. "
  "But it is a recommendatory statutory body set up under the National Commission for Women Act, 1990. It can take the matter up with the authorities, recommend action and help the woman pursue legal remedies, but it cannot itself award the benefit, fine the employer, quash the employer's decision or direct a court; those remedies lie with the authorities under the maternity benefit law and with the courts.",
  "किसी शिकायत की जाँच करते समय आयोग को वाद की सुनवाई करने वाले दीवानी न्यायालय की शक्तियाँ मिलती हैं: वह व्यक्तियों को बुलाकर उनसे पूछताछ कर सकता है, दस्तावेज़ माँग सकता है और शपथपत्र पर साक्ष्य ले सकता है। "
  "पर यह राष्ट्रीय महिला आयोग अधिनियम, 1990 के तहत बना एक सिफ़ारिशी वैधानिक निकाय है। यह मामले को अधिकारियों के सामने उठा सकता है, कार्रवाई की सिफ़ारिश कर सकता है और महिला को क़ानूनी उपाय अपनाने में मदद कर सकता है, पर स्वयं लाभ नहीं दिला सकता, नियोक्ता पर जुर्माना नहीं लगा सकता, नियोक्ता का निर्णय रद्द नहीं कर सकता और किसी न्यायालय को निर्देश नहीं दे सकता; ये उपाय मातृत्व लाभ क़ानून के तहत अधिकारियों और न्यायालयों के पास हैं।",
  "National Commission for Women Act, 1990; National Commission for Women.",
  "bodies-ncw-statutory-powers", craft="application")

if __name__ == "__main__":
    write_updates("gs_l2_t21_polity_v2.sql", replaces={"rights-internet-defamation-sleep": "rights-art33-34-bhasin"})
