# -*- coding: utf-8 -*-
"""Level 2 · Test 2 (Polity 2: Parliament & Executive) -- depth audit of 2026-10-04
(docs/upsc-question-design-standard.md §6).

All 104 rows in the test's two sub-topics were read and classified. Before: analytic 12, precision 58,
recall 34 (4 rows are Test 21's, already tagged). 23 rows are rewritten in place with the same concept id,
type and difficulty, so the cells do not change.
  - 7 recall rows become cases or inferences:
      testing a coalition's majority; why seats are frozen on the 1971 Census; undiscussed demands on the last
      day; members who vote before the oath or resign; Maru Ram on pardon; the Attorney General and a private
      brief; a non-member Chief Minister.
  - 16 precision rows become cases:
      which Bill is a Money Bill; who rules on an office of profit; excess, token and credit grants; Tenth
      Schedule cases; a Council rejecting a Bill; what is charged on the Consolidated Fund; an Article 117(1)
      Bill; a State Bill touching the High Court; a voided presidential election; ordinance dates; the Speaker
      after dissolution; Article 122, Raja Ram Pal and Sita Soren; abolishing a Council; prorogation; the
      Appropriation Bill; court-martial and State death sentences.
After: analytic 35, precision 42, recall 27. The other 77 rows keep their content and get their craft tag.
Leaks avoided while drafting:
  - a '550 seats' distractor (answers the Lok Sabha-strength row);
  - 'decided by the presiding officer' for defection (answers the Tenth Schedule row);
  - the Speaker's first-instance vote (answers the casting-vote row);
  - cut motions and sine die in distractors (answer the cut-motion and prorogation rows)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write_updates, CODE
from polity_common import C3, C4, T2

d.SUBJECT = "Polity"
d.REQUIRE_CRAFT = True
PL = "Parliament & State Legislature"
EX = "Union & State Executive"
COI = "Constitution of India"
SC = "Supreme Court of India"
LSR = "Rules of Procedure and Conduct of Business in Lok Sabha"
LSS = "Lok Sabha Secretariat -- Practice and Procedure of Parliament"
NC = "NCERT Class XI, Political Science -- Indian Constitution at Work"
MATCHED = "How many of the above are correctly matched?"
MATCHED_HI = "उपर्युक्त में से कितने सही सुमेलित हैं?"

# ================================================================ PARLIAMENT -- MCQs (4)
M(PL, "medium", "A party withdraws its support from the coalition government at the Centre. The Opposition wants the Lok Sabha to decide whether the Council of Ministers still enjoys its confidence. Which one of the following is the appropriate course?",
  "एक दल केंद्र की गठबंधन सरकार से समर्थन वापस ले लेता है। विपक्ष चाहता है कि लोकसभा तय करे कि मंत्रिपरिषद को अब भी उसका विश्वास प्राप्त है या नहीं। निम्नलिखित में से कौन-सा उपयुक्त रास्ता है?",
  ["Move a motion of no-confidence, which needs the support of at least fifty members to be taken up",
   "Give notice of a calling attention motion asking the Prime Minister to explain the withdrawal",
   "Move an adjournment motion, whose adoption forces the Council of Ministers to resign",
   "Seek a direction from the Supreme Court requiring the Government to prove its majority within a week"],
  ["अविश्वास प्रस्ताव लाना, जिस पर विचार के लिए कम से कम पचास सदस्यों का समर्थन चाहिए",
   "प्रधानमंत्री से समर्थन वापसी पर वक्तव्य माँगने के लिए ध्यानाकर्षण प्रस्ताव की सूचना देना",
   "स्थगन प्रस्ताव लाना, जिसके स्वीकृत होने पर मंत्रिपरिषद को त्यागपत्र देना पड़ता है",
   "सर्वोच्च न्यायालय से निर्देश माँगना कि सरकार एक सप्ताह में अपना बहुमत सिद्ध करे"],
  0,
  "The Council of Ministers is collectively responsible to the Lok Sabha (Article 75(3)), and the device the rules provide for testing that confidence is the no-confidence motion. Under Rule 198 the Speaker grants leave if at least fifty members rise in support; if the motion is carried, the Council must resign. "
  "A calling attention motion only draws a minister's statement on a matter of urgent public importance, with no vote. An adjournment motion carries an element of censure but does not oblige the Government to resign. Courts have ordered floor tests in disputes over State governments, but that is no substitute for the House's own remedy.",
  "मंत्रिपरिषद सामूहिक रूप से लोकसभा के प्रति उत्तरदायी है (अनुच्छेद 75(3)), और इस विश्वास को परखने के लिए नियमों में दिया गया उपाय अविश्वास प्रस्ताव है। नियम 198 के तहत यदि कम से कम पचास सदस्य समर्थन में खड़े हों तो अध्यक्ष अनुमति देते हैं; प्रस्ताव पारित होने पर मंत्रिपरिषद को त्यागपत्र देना होता है। "
  "ध्यानाकर्षण प्रस्ताव से केवल किसी अविलंबनीय लोक महत्व के विषय पर मंत्री का वक्तव्य आता है, कोई मतदान नहीं होता। स्थगन प्रस्ताव में निंदा का भाव होता है, पर इससे सरकार पर त्यागपत्र की बाध्यता नहीं आती। न्यायालयों ने राज्य सरकारों के विवादों में शक्ति-परीक्षण के आदेश दिए हैं, पर वह सदन के अपने उपाय का विकल्प नहीं है।",
  f"{COI} -- Article 75(3); {LSR} -- Rule 198.",
  "parl-no-confidence-50-members", craft="application")

M(PL, "hard", "The allocation of Lok Sabha seats among the States is still based on the 1971 Census, and the freeze has been extended until the first Census taken after 2026. Which one of the following best explains why the freeze was adopted?",
  "राज्यों के बीच लोकसभा सीटों का आवंटन अब भी 1971 की जनगणना पर आधारित है, और यह रोक 2026 के बाद होने वाली पहली जनगणना तक बढ़ा दी गई है। निम्नलिखित में से कौन-सा इस रोक का सबसे सही कारण है?",
  ["To avoid penalising States that slowed their population growth by giving them fewer seats",
   "Because the Censuses after 1971 left out several States and could not be relied upon",
   "To keep the strength of the Lok Sabha from rising above its present number of seats",
   "Because a fresh delimitation cannot be held until every State has the same population per seat"],
  ["ताकि जनसंख्या वृद्धि धीमी करने वाले राज्यों को कम सीटें देकर दंडित न किया जाए",
   "क्योंकि 1971 के बाद की जनगणनाओं में कई राज्य छूट गए और वे विश्वसनीय नहीं थीं",
   "ताकि लोकसभा की सदस्य संख्या अपनी मौजूदा सीटों से ऊपर न बढ़े",
   "क्योंकि परिसीमन तब तक नहीं हो सकता जब तक हर राज्य में प्रति सीट जनसंख्या बराबर न हो"],
  0,
  "Reallocating seats by population would shift seats from the southern and other States that had brought their birth rates down to the States whose populations were still growing fast, which would punish the very success that national population policy sought. "
  "So the 42nd Amendment (1976) froze the inter-State allocation on the 1971 figures until 2000, and the 84th Amendment (2001) extended the freeze until the first Census after 2026. Boundaries within each State were, however, redrawn on the 2001 Census. The question of what happens after the freeze ends is now one of the live debates of Indian federalism.",
  "जनसंख्या के अनुसार सीटों का पुनः आवंटन उन दक्षिणी और अन्य राज्यों से सीटें छीन लेता जिन्होंने अपनी जन्म दर घटाई थी, और उन्हें उन राज्यों को दे देता जिनकी आबादी अब भी तेज़ी से बढ़ रही थी; इससे वही सफलता दंडित होती जिसे राष्ट्रीय जनसंख्या नीति चाहती थी। "
  "इसलिए 42वें संशोधन (1976) ने राज्यों के बीच आवंटन को 2000 तक 1971 के आँकड़ों पर रोक दिया, और 84वें संशोधन (2001) ने इस रोक को 2026 के बाद की पहली जनगणना तक बढ़ा दिया। हालाँकि हर राज्य के भीतर की सीमाएँ 2001 की जनगणना पर फिर से खींची गईं। रोक समाप्त होने के बाद क्या होगा, यह अब भारतीय संघवाद की एक जीवंत बहस है।",
  f"{COI} -- Article 82 and the 42nd and 84th Amendments; {NC} -- Election and Representation.",
  "polity-lok-sabha-seat-freeze-1971", craft="inference")

M(PL, "medium", "On the last of the days allotted for the demands for grants in the Lok Sabha, forty demands have still not been discussed. What happens to them?",
  "लोकसभा में अनुदान माँगों के लिए तय दिनों में से अंतिम दिन तक चालीस माँगों पर अभी चर्चा नहीं हुई है। उनका क्या होता है?",
  ["The Speaker puts all of them to the vote together, without discussion",
   "They lapse and have to be presented afresh in the next session",
   "They are sent to the Department-related Standing Committees for a report before voting",
   "They are treated as passed, since demands not discussed are deemed to be voted"],
  ["अध्यक्ष बिना चर्चा के सबको एक साथ मतदान के लिए रख देते हैं",
   "वे व्यपगत हो जाती हैं और अगले सत्र में नए सिरे से रखनी पड़ती हैं",
   "मतदान से पहले उन्हें विभाग-संबंधित स्थायी समितियों के पास रिपोर्ट के लिए भेजा जाता है",
   "उन्हें पारित मान लिया जाता है, क्योंकि जिन माँगों पर चर्चा न हो वे स्वीकृत मानी जाती हैं"],
  0,
  "This is the 'guillotine'. At the appointed hour on the last allotted day, the Speaker puts all the outstanding demands to the vote at once, whether or not they have been discussed, so that the budget is passed before the financial year begins. "
  "The demands do not lapse and are not deemed passed: they are actually voted, only without debate, which is why critics say that much of the spending escapes scrutiny. The standing committees examine the demands earlier, during the budget recess, not on the last day.",
  "यह 'गिलोटिन' है। अंतिम तय दिन के निर्धारित समय पर अध्यक्ष सभी बची हुई माँगों को एक साथ मतदान के लिए रख देते हैं, चाहे उन पर चर्चा हुई हो या नहीं, ताकि बजट वित्त वर्ष शुरू होने से पहले पारित हो जाए। "
  "माँगें न व्यपगत होती हैं और न पारित मानी जाती हैं: उन पर वास्तव में मतदान होता है, केवल बिना बहस के; इसीलिए आलोचक कहते हैं कि बहुत-सा व्यय जाँच से बच जाता है। स्थायी समितियाँ माँगों की जाँच पहले, बजट अवकाश के दौरान, करती हैं, अंतिम दिन नहीं।",
  f"{LSR} -- demands for grants; {LSS}.",
  "polity-budget-guillotine", craft="application")

M(PL, "medium", "Each of the following Bills contains only the provision stated. Which one of them is a Money Bill under Article 110?",
  "निम्नलिखित में से प्रत्येक विधेयक में केवल बताया गया प्रावधान है। इनमें से कौन-सा अनुच्छेद 110 के तहत धन विधेयक है?",
  ["A Bill imposing a new cess on crude oil",
   "A Bill raising the fees charged for issuing passports",
   "A Bill imposing fines for the misuse of government land",
   "A Bill allowing municipalities to levy a tax on hoardings"],
  ["कच्चे तेल पर नया उपकर लगाने वाला विधेयक",
   "पासपोर्ट जारी करने की फ़ीस बढ़ाने वाला विधेयक",
   "सरकारी भूमि के दुरुपयोग पर जुर्माना लगाने वाला विधेयक",
   "नगरपालिकाओं को होर्डिंग पर कर लगाने की अनुमति देने वाला विधेयक"],
  0,
  "A cess is a tax, and a Bill dealing only with the imposition of a tax falls under Article 110(1)(a). Article 110(2) then lists what does not by itself make a Bill a Money Bill: provisions for fines or other pecuniary penalties, for fees for licences or for services rendered (such as passport fees), and for taxes imposed by any local authority or body for local purposes (such as a municipal tax on hoardings). "
  "Each of the other three Bills is therefore an ordinary Bill, which the Rajya Sabha can amend or reject.",
  "उपकर एक कर है, और केवल कर लगाने से जुड़ा विधेयक अनुच्छेद 110(1)(क) के अंतर्गत आता है। अनुच्छेद 110(2) बताता है कि कौन-से प्रावधान अपने आप में किसी विधेयक को धन विधेयक नहीं बनाते: जुर्माना या अन्य आर्थिक दंड, लाइसेंस की फ़ीस या दी गई सेवाओं की फ़ीस (जैसे पासपोर्ट फ़ीस), और किसी स्थानीय प्राधिकरण या निकाय द्वारा स्थानीय प्रयोजनों के लिए लगाए गए कर (जैसे होर्डिंग पर नगरपालिका कर)। "
  "इसलिए बाक़ी तीनों साधारण विधेयक हैं, जिनमें राज्यसभा संशोधन कर सकती है या उन्हें अस्वीकार कर सकती है।",
  f"{COI} -- Article 110.",
  "parl-money-bill-fines-not", craft="application")

M(PL, "medium", "A Member of Parliament is alleged to have become disqualified by accepting a paid post as chairman of a government-owned corporation. Who decides whether he has become disqualified?",
  "आरोप है कि एक संसद सदस्य सरकारी स्वामित्व वाले निगम के अध्यक्ष का वेतनभोगी पद स्वीकार करके अयोग्य हो गया है। यह कौन तय करता है कि वह अयोग्य हुआ है या नहीं?",
  ["The President, acting according to the opinion of the Election Commission",
   "The Speaker or Chairman of the House to which he belongs",
   "The High Court of the State from which he was elected, on an election petition",
   "The Election Commission, whose decision is final and binding on the President"],
  ["राष्ट्रपति, निर्वाचन आयोग की राय के अनुसार",
   "उस सदन के अध्यक्ष या सभापति जिसका वह सदस्य है",
   "जिस राज्य से वह चुना गया, उसका उच्च न्यायालय, चुनाव याचिका पर",
   "निर्वाचन आयोग, जिसका निर्णय अंतिम है और राष्ट्रपति पर बाध्यकारी है"],
  0,
  "Holding an office of profit under the Government is a disqualification under Article 102(1)(a), unless Parliament has exempted that office by law. Under Article 103 the question is decided by the President, whose decision is final, but the President must first obtain the opinion of the Election Commission and act according to it. "
  "The decision is formally the President's, which is why the option making the Commission's own decision final is wrong; the High Courts come in only through election petitions about the election itself. Disqualification for defection is handled under a different procedure, in the Tenth Schedule.",
  "सरकार के अधीन लाभ का पद धारण करना अनुच्छेद 102(1)(क) के तहत अयोग्यता है, जब तक संसद ने क़ानून द्वारा उस पद को छूट न दी हो। अनुच्छेद 103 के तहत यह प्रश्न राष्ट्रपति तय करते हैं, जिनका निर्णय अंतिम है, पर उन्हें पहले निर्वाचन आयोग की राय लेनी होती है और उसके अनुसार कार्य करना होता है। "
  "निर्णय औपचारिक रूप से राष्ट्रपति का है, इसलिए आयोग के अपने निर्णय को अंतिम बताने वाला विकल्प गलत है; उच्च न्यायालय केवल चुनाव से जुड़ी चुनाव याचिकाओं के ज़रिए आते हैं। दल-बदल से अयोग्यता दसवीं अनुसूची की एक अलग प्रक्रिया से निपटाई जाती है।",
  f"{COI} -- Articles 102 and 103.",
  "polity-art103-disqualification-president-ec", craft="application")

# ================================================================ PARLIAMENT -- statements (12)
S(PL, "hard", "Consider the following situations involving members of Parliament:",
  "संसद सदस्यों से जुड़ी निम्नलिखित स्थितियों पर विचार कीजिए:",
  ["A newly elected member who sits and votes in the Lok Sabha before taking the oath is liable to a penalty of five hundred rupees for each such day.",
   "A member's resignation takes effect only when the President accepts it.",
   "Members of Parliament take their oath before the Chief Justice of India."],
  ["शपथ लेने से पहले लोकसभा में बैठने और मतदान करने वाला नवनिर्वाचित सदस्य हर ऐसे दिन के लिए पाँच सौ रुपये के दंड का भागी है।",
   "किसी सदस्य का त्यागपत्र तभी प्रभावी होता है जब राष्ट्रपति उसे स्वीकार करें।",
   "संसद सदस्य भारत के मुख्य न्यायाधीश के समक्ष शपथ लेते हैं।"],
  C3, 0,
  "Only statement 1 is correct: Article 104 imposes the penalty, recoverable as a debt due to the Union. "
  "Statement 2 is wrong: under Article 101(3)(b) a member resigns by writing to the Speaker or the Chairman, and the seat falls vacant when the presiding officer accepts it. Since the 33rd Amendment (1974) the presiding officer may refuse a resignation that he finds, after inquiry, is not voluntary or genuine -- a safeguard against resignations extracted by pressure. "
  "Statement 3 is wrong: under Article 99 members take the oath before the President or a person he appoints, in practice the Speaker pro tem.",
  "केवल कथन 1 सही है: अनुच्छेद 104 यह दंड लगाता है, जो संघ को देय ऋण के रूप में वसूला जाता है। "
  "कथन 2 गलत है: अनुच्छेद 101(3)(ख) के तहत सदस्य अध्यक्ष या सभापति को लिखकर त्यागपत्र देता है, और पीठासीन अधिकारी के स्वीकार करने पर सीट रिक्त होती है। 33वें संशोधन (1974) से पीठासीन अधिकारी ऐसा त्यागपत्र अस्वीकार कर सकते हैं जो जाँच के बाद स्वैच्छिक या वास्तविक न लगे; यह दबाव में लिए गए त्यागपत्रों के विरुद्ध सुरक्षा है। "
  "कथन 3 गलत है: अनुच्छेद 99 के तहत सदस्य राष्ट्रपति या उनके द्वारा नियुक्त व्यक्ति, व्यवहार में अस्थायी अध्यक्ष (प्रोटेम स्पीकर), के समक्ष शपथ लेते हैं।",
  f"{COI} -- Articles 99, 101 and 104; {LSS}.",
  "parl-members-oath-penalty-resignation", craft="application")

S(PL, "hard", "Consider the following situations and the grant named against each:",
  "निम्नलिखित स्थितियों और प्रत्येक के सामने दिए गए अनुदान पर विचार कीजिए:",
  ["A ministry has spent more in a year than Parliament granted for a service -- excess grant, presented after the Public Accounts Committee has examined the excess",
   "The Government wants to begin a new scheme in mid-year and can find the money by savings elsewhere in the same grant -- token grant",
   "War breaks out and the Government needs money whose amount and purpose it cannot yet state in the usual detail -- supplementary grant"],
  ["किसी मंत्रालय ने वर्ष में किसी सेवा के लिए संसद द्वारा दिए गए अनुदान से अधिक ख़र्च किया -- अधिक अनुदान, जो लोक लेखा समिति द्वारा अधिकता की जाँच के बाद रखा जाता है",
   "सरकार वर्ष के बीच में एक नई योजना शुरू करना चाहती है और उसी अनुदान में कहीं और की बचत से पैसा निकाल सकती है -- सांकेतिक अनुदान",
   "युद्ध छिड़ जाता है और सरकार को ऐसी राशि चाहिए जिसकी मात्रा और प्रयोजन वह अभी सामान्य विस्तार से नहीं बता सकती -- अनुपूरक अनुदान"],
  C3, 1,
  "The first two are correctly matched. Excess grants regularise spending beyond what was voted, so the House waits for the Public Accounts Committee to examine the excess. A token grant, usually of one rupee, lets the House approve a new service while the money comes by re-appropriation. "
  "The third is wrong: an unexpected demand of indefinite size or character, as in a war, is met by a vote of credit (Article 116), a kind of blank cheque. A supplementary grant (Article 115) is for a known service whose original grant has proved insufficient for the year -- the near-miss device that the situation tempts one to pick.",
  "पहले दो सही सुमेलित हैं। अधिक अनुदान स्वीकृत राशि से अधिक ख़र्च को नियमित करते हैं, इसलिए सदन लोक लेखा समिति द्वारा अधिकता की जाँच की प्रतीक्षा करता है। सांकेतिक अनुदान, प्रायः एक रुपये का, सदन को नई सेवा मंज़ूर करने देता है जबकि पैसा पुनर्विनियोग से आता है। "
  "तीसरा गलत है: युद्ध जैसी अनिश्चित मात्रा या स्वरूप की अप्रत्याशित माँग प्रत्यय अनुदान (vote of credit, अनुच्छेद 116) से पूरी होती है, जो एक तरह का खुला चेक है। अनुपूरक अनुदान (अनुच्छेद 115) किसी ज्ञात सेवा के लिए है जिसका मूल अनुदान वर्ष के लिए अपर्याप्त निकला; यही वह मिलता-जुलता उपाय है जिसे चुनने का लालच यह स्थिति देती है।",
  f"{COI} -- Articles 115 and 116; {LSS}.",
  "parl-excess-token-credit-grants", closing=MATCHED, closing_hi=MATCHED_HI, craft="application")

S(PL, "hard", "Consider the following cases involving members of a House of Parliament:",
  "संसद के किसी सदन के सदस्यों से जुड़े निम्नलिखित मामलों पर विचार कीजिए:",
  ["A nominated member joins a political party four months after taking his seat.",
   "An independent member joins a political party a year after his election.",
   "Two-thirds of the members of a legislature party agree to merge their party with another party.",
   "One-third of the members of a legislature party break away to form a separate group."],
  ["एक मनोनीत सदस्य अपनी सीट ग्रहण करने के चार महीने बाद एक राजनीतिक दल में शामिल होता है।",
   "एक निर्दलीय सदस्य अपने निर्वाचन के एक वर्ष बाद एक राजनीतिक दल में शामिल होता है।",
   "किसी विधायक दल के दो-तिहाई सदस्य अपने दल का दूसरे दल में विलय करने पर सहमत होते हैं।",
   "किसी विधायक दल के एक-तिहाई सदस्य अलग होकर एक पृथक समूह बना लेते हैं।"],
  C4, 1,
  "Only two -- cases 1 and 3 -- are protected. A nominated member may join a party within six months of taking his seat (paragraph 2(3)). A merger supported by at least two-thirds of the legislature party is exempt (paragraph 4). "
  "An independent who joins a party after the election is disqualified (paragraph 2(2)): he was elected as an independent, and the law holds him to it. The 'split' exception for one-third of a legislature party, in the original 1985 Schedule, was deleted by the 91st Amendment (2003) because it encouraged defections in instalments.",
  "केवल दो, मामले 1 और 3, सुरक्षित हैं। मनोनीत सदस्य अपनी सीट ग्रहण करने के छह महीने के भीतर किसी दल में शामिल हो सकता है (अनुच्छेद 2(3))। विधायक दल के कम से कम दो-तिहाई सदस्यों के समर्थन वाला विलय छूट पाता है (अनुच्छेद 4)। "
  "चुनाव के बाद किसी दल में शामिल होने वाला निर्दलीय अयोग्य होता है (अनुच्छेद 2(2)): वह निर्दलीय के रूप में चुना गया था, और क़ानून उसे उसी पर टिकाए रखता है। विधायक दल के एक-तिहाई की 'टूट' वाला अपवाद, जो 1985 की मूल अनुसूची में था, 91वें संशोधन (2003) ने हटा दिया, क्योंकि उससे किस्तों में दल-बदल को बढ़ावा मिलता था।",
  f"{COI} -- Tenth Schedule, paragraphs 2 and 4; Constitution (Ninety-first Amendment) Act, 2003.",
  "parl-tenth-schedule-members-split", closing="In how many of the above cases are the members concerned protected from disqualification under the Tenth Schedule?",
  closing_hi="उपर्युक्त में से कितने मामलों में संबंधित सदस्य दसवीं अनुसूची के तहत अयोग्यता से सुरक्षित हैं?", craft="multi")

S(PL, "hard", "In a State with a bicameral legislature, the Legislative Assembly passes an ordinary Bill and the Legislative Council rejects it. Consider the following statements:",
  "द्विसदनीय विधानमंडल वाले एक राज्य में विधानसभा एक साधारण विधेयक पारित करती है और विधान परिषद उसे अस्वीकार कर देती है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["If the Assembly passes the Bill again and sends it back, the Council can hold it up for at most one more month, after which it is deemed passed.",
   "The Governor can summon a joint sitting of the two Houses to resolve the deadlock.",
   "Had the Bill been a Money Bill, the Council could have held it up for three months."],
  ["यदि विधानसभा विधेयक को फिर से पारित कर वापस भेजे, तो परिषद उसे अधिकतम एक महीने और रोक सकती है, जिसके बाद उसे पारित मान लिया जाता है।",
   "गतिरोध दूर करने के लिए राज्यपाल दोनों सदनों की संयुक्त बैठक बुला सकते हैं।",
   "यदि वह धन विधेयक होता, तो परिषद उसे तीन महीने तक रोक सकती थी।"],
  C3, 0,
  "Only statement 1 is correct. Under Article 197 the Council can delay an ordinary Bill from the Assembly by up to three months the first time and one month the second time, after which the Assembly's version is deemed passed by both Houses -- the Council can delay, but not defeat. "
  "Statement 2 is wrong: there is no joint sitting in a State Legislature; the Assembly simply prevails. Statement 3 is wrong: under Article 198 a Money Bill must be returned within fourteen days, and the Assembly may accept or reject the Council's recommendations.",
  "केवल कथन 1 सही है। अनुच्छेद 197 के तहत परिषद विधानसभा से आए साधारण विधेयक को पहली बार अधिकतम तीन महीने और दूसरी बार एक महीने तक रोक सकती है, जिसके बाद विधानसभा का रूप दोनों सदनों द्वारा पारित माना जाता है; परिषद देर कर सकती है, हरा नहीं सकती। "
  "कथन 2 गलत है: राज्य विधानमंडल में संयुक्त बैठक का प्रावधान नहीं है; विधानसभा ही प्रबल रहती है। कथन 3 गलत है: अनुच्छेद 198 के तहत धन विधेयक चौदह दिनों के भीतर लौटाना होता है, और विधानसभा परिषद की सिफ़ारिशें मान या ठुकरा सकती है।",
  f"{COI} -- Articles 197 and 198.",
  "polity-state-legislative-council-powers", craft="application")

S(PL, "medium", "Which of the following items of expenditure are charged on the Consolidated Fund of India, and so are not put to the vote of Parliament?",
  "निम्नलिखित में से कौन-से व्यय भारत की संचित निधि पर भारित हैं, और इसलिए उन पर संसद में मतदान नहीं होता?",
  ["The salaries and allowances of the judges of the Supreme Court",
   "The salary of the Comptroller and Auditor-General of India",
   "The salaries of the Union ministers",
   "The expenditure on the Prime Minister's Office"],
  ["सर्वोच्च न्यायालय के न्यायाधीशों के वेतन और भत्ते",
   "भारत के नियंत्रक-महालेखापरीक्षक का वेतन",
   "केंद्रीय मंत्रियों के वेतन",
   "प्रधानमंत्री कार्यालय पर व्यय"],
  C4, 1,
  "Only the first two are charged. Article 112(3) charges, among other items, the emoluments of the President, the presiding officers of the two Houses, the judges of the Supreme Court and the CAG, and the debt charges of the Government of India -- offices whose independence must not depend on a yearly vote. "
  "Ministers' salaries and the running of the Prime Minister's Office are voted expenditure, granted through the demands for grants like other spending of the Government. Charged expenditure is kept out of the vote, but it can still be discussed in Parliament (Article 113(1)).",
  "केवल पहले दो भारित हैं। अनुच्छेद 112(3) अन्य मदों के साथ राष्ट्रपति, दोनों सदनों के पीठासीन अधिकारियों, सर्वोच्च न्यायालय के न्यायाधीशों और नियंत्रक-महालेखापरीक्षक के वेतन-भत्तों तथा भारत सरकार के ऋण-भार को भारित करता है; ये ऐसे पद हैं जिनकी स्वतंत्रता किसी वार्षिक मतदान पर निर्भर नहीं होनी चाहिए। "
  "मंत्रियों के वेतन और प्रधानमंत्री कार्यालय का ख़र्च मतदान योग्य व्यय हैं, जो सरकार के अन्य ख़र्च की तरह अनुदान माँगों के ज़रिए मिलते हैं। भारित व्यय पर मतदान नहीं होता, पर संसद में उस पर चर्चा हो सकती है (अनुच्छेद 113(1))।",
  f"{COI} -- Articles 112 and 113.",
  "parl-charged-expenditure", closing="How many of the above are charged on the Consolidated Fund of India?",
  closing_hi="उपर्युक्त में से कितने भारत की संचित निधि पर भारित हैं?", craft="multi")

S(PL, "medium", "A Bill proposes a new tax and also amends several laws unrelated to taxation, so it is not a Money Bill. Consider the following statements about it:",
  "एक विधेयक नया कर प्रस्तावित करता है और साथ में कराधान से असंबद्ध कई क़ानूनों में संशोधन भी करता है, इसलिए वह धन विधेयक नहीं है। इसके बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It can be introduced only in the Lok Sabha, and only on the recommendation of the President.",
   "The Rajya Sabha can reject it.",
   "If the two Houses disagree on it, the President can summon a joint sitting."],
  ["इसे केवल लोकसभा में, और केवल राष्ट्रपति की सिफ़ारिश पर, पेश किया जा सकता है।",
   "राज्यसभा इसे अस्वीकार कर सकती है।",
   "यदि दोनों सदन इस पर असहमत हों, तो राष्ट्रपति संयुक्त बैठक बुला सकते हैं।"],
  C3, 2,
  "All three are correct. Such a Bill is a Financial Bill under Article 117(1): because it contains a Money Bill matter, it shares the Money Bill's two entry conditions -- introduction only in the Lok Sabha and only on the President's recommendation. "
  "Once introduced, however, it is treated like an ordinary Bill: the Rajya Sabha can amend or reject it, and a deadlock can be resolved at a joint sitting under Article 108, which is not available for a Money Bill. A Financial Bill of the other kind, under Article 117(3), merely involves spending from the Consolidated Fund and can be introduced in either House.",
  "तीनों कथन सही हैं। ऐसा विधेयक अनुच्छेद 117(1) के तहत वित्त विधेयक है: क्योंकि इसमें धन विधेयक का विषय है, इसलिए इस पर धन विधेयक की दोनों प्रवेश-शर्तें लागू होती हैं, यानी केवल लोकसभा में और केवल राष्ट्रपति की सिफ़ारिश पर पेश होना। "
  "पर पेश होने के बाद इसे साधारण विधेयक की तरह माना जाता है: राज्यसभा इसमें संशोधन कर सकती है या इसे अस्वीकार कर सकती है, और गतिरोध अनुच्छेद 108 के तहत संयुक्त बैठक से सुलझ सकता है, जो धन विधेयक के लिए उपलब्ध नहीं है। दूसरे प्रकार का वित्त विधेयक, अनुच्छेद 117(3) वाला, केवल संचित निधि से व्यय से जुड़ा होता है और किसी भी सदन में पेश हो सकता है।",
  f"{COI} -- Articles 108, 110 and 117.",
  "parl-financial-bills-117", craft="application")

S(PL, "medium", "The Lok Sabha is dissolved on 1 March, and the newly elected House first meets on 24 June. Consider the following statements about the Speaker:",
  "लोकसभा 1 मार्च को भंग होती है, और नवनिर्वाचित सदन की पहली बैठक 24 जून को होती है। अध्यक्ष के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Speaker continues in office until immediately before 24 June.",
   "Between 1 March and 24 June, the Deputy Speaker performs the functions of the Speaker.",
   "The Speaker vacates office if he ceases to be a member of the Lok Sabha."],
  ["अध्यक्ष 24 जून से ठीक पहले तक पद पर बने रहते हैं।",
   "1 मार्च से 24 जून के बीच उपाध्यक्ष, अध्यक्ष के कार्य करते हैं।",
   "यदि अध्यक्ष लोकसभा के सदस्य नहीं रहते, तो वे पद रिक्त कर देते हैं।"],
  C3, 1,
  "Statements 1 and 3 are correct. Under the proviso to Article 94, the Speaker does not vacate office on dissolution but continues until immediately before the first meeting of the new House -- so the Lok Sabha Secretariat and its work always have a head, even when there is no House. "
  "Statement 2 is wrong: because the Speaker continues, nobody needs to stand in; and the Deputy Speaker's own office, unlike the Speaker's, ends with the House. Under Article 94(a) the Speaker vacates office on ceasing to be a member, for example on resigning his seat.",
  "कथन 1 और 3 सही हैं। अनुच्छेद 94 के परंतुक के तहत अध्यक्ष भंग होने पर पद रिक्त नहीं करते, बल्कि नए सदन की पहली बैठक से ठीक पहले तक बने रहते हैं; इसलिए लोकसभा सचिवालय और उसके काम का हमेशा एक प्रमुख रहता है, तब भी जब सदन नहीं होता। "
  "कथन 2 गलत है: अध्यक्ष के बने रहने के कारण किसी को उनकी जगह लेने की ज़रूरत नहीं; और अध्यक्ष के विपरीत उपाध्यक्ष का पद सदन के साथ ही समाप्त हो जाता है। अनुच्छेद 94(क) के तहत सदस्य न रहने पर, उदाहरण के लिए अपनी सीट से त्यागपत्र देने पर, अध्यक्ष पद रिक्त कर देते हैं।",
  f"{COI} -- Articles 93 and 94; {LSS}.",
  "parl-speaker-continuity-removal-quorum", craft="application")

S(PL, "hard", "Consider the following situations involving Parliament and the courts:",
  "संसद और न्यायालयों से जुड़ी निम्नलिखित स्थितियों पर विचार कीजिए:",
  ["A member expelled by the House challenges the expulsion as unconstitutional, and the court examines the claim on limited grounds such as illegality.",
   "A member who took a bribe to vote in a particular way in the House escapes prosecution for the bribery by claiming parliamentary immunity.",
   "A court strikes down an Act because the Speaker did not follow one of the House's rules of procedure while it was being passed."],
  ["सदन द्वारा निष्कासित एक सदस्य निष्कासन को असंवैधानिक बताकर चुनौती देता है, और न्यायालय अवैधता जैसे सीमित आधारों पर दावे की जाँच करता है।",
   "सदन में एक विशेष ढंग से मतदान करने के लिए रिश्वत लेने वाला सदस्य संसदीय उन्मुक्ति का दावा करके रिश्वतख़ोरी के अभियोजन से बच जाता है।",
   "एक न्यायालय किसी अधिनियम को इसलिए रद्द कर देता है क्योंकि उसे पारित करते समय अध्यक्ष ने सदन के प्रक्रिया-नियमों में से एक का पालन नहीं किया।"],
  C3, 0,
  "Only the first is consistent with the law. In Raja Ram Pal (2007) the Supreme Court upheld the expulsion of MPs caught in a cash-for-questions sting, but held that expulsion is open to judicial review on limited grounds such as illegality or unconstitutionality. "
  "The second is wrong: in Sita Soren (2024) a seven-judge bench overruled P.V. Narasimha Rao (1998) and held that bribery is not protected by parliamentary privilege, because taking the bribe is complete before any speech or vote. "
  "The third is wrong: Article 122 bars courts from questioning the validity of proceedings in Parliament on the ground of any alleged irregularity of procedure.",
  "केवल पहली स्थिति क़ानून के अनुरूप है। राजा राम पाल (2007) में सर्वोच्च न्यायालय ने 'प्रश्न के बदले नक़दी' स्टिंग में पकड़े गए सांसदों के निष्कासन को वैध माना, पर कहा कि अवैधता या असंवैधानिकता जैसे सीमित आधारों पर निष्कासन की न्यायिक समीक्षा हो सकती है। "
  "दूसरी गलत है: सीता सोरेन (2024) में सात न्यायाधीशों की पीठ ने पी.वी. नरसिंह राव (1998) को पलटते हुए कहा कि रिश्वतख़ोरी संसदीय विशेषाधिकार से संरक्षित नहीं है, क्योंकि रिश्वत लेने का अपराध किसी भाषण या मतदान से पहले ही पूरा हो जाता है। "
  "तीसरी गलत है: अनुच्छेद 122 न्यायालयों को प्रक्रिया की किसी कथित अनियमितता के आधार पर संसद की कार्यवाही की वैधता पर प्रश्न उठाने से रोकता है।",
  f"{COI} -- Articles 105 and 122; {SC} -- Raja Ram Pal v. Hon'ble Speaker (2007), Sita Soren v. Union of India (2024).",
  "parl-courts-122-raja-ram-pal-sita-soren", craft="application")

S(PL, "medium", "The Legislative Assembly of a State wishes to abolish the State's Legislative Council. Consider the following statements:",
  "एक राज्य की विधानसभा राज्य की विधान परिषद को समाप्त करना चाहती है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["Parliament must pass the law abolishing the Council by a special majority under Article 368.",
   "The Assembly's resolution needs only a simple majority of the members present and voting.",
   "Once the Assembly has passed its resolution, the President can abolish the Council by order."],
  ["संसद को परिषद समाप्त करने वाला क़ानून अनुच्छेद 368 के तहत विशेष बहुमत से पारित करना होगा।",
   "विधानसभा के संकल्प के लिए केवल उपस्थित और मतदान करने वाले सदस्यों का साधारण बहुमत चाहिए।",
   "विधानसभा द्वारा संकल्प पारित होने के बाद राष्ट्रपति आदेश से परिषद समाप्त कर सकते हैं।"],
  C3, 3,
  "None is correct. Under Article 169 the Assembly must pass the resolution by a special majority -- a majority of its total membership and two-thirds of the members present and voting. Parliament then abolishes the Council by an ordinary law, passed by a simple majority, and Article 169(3) says such a law is not deemed an amendment of the Constitution for the purposes of Article 368. "
  "The President has no power to abolish a Council by order; it takes a law of Parliament. Andhra Pradesh, for instance, abolished its Council in 1985 and revived it in 2007 in this way.",
  "कोई भी कथन सही नहीं है। अनुच्छेद 169 के तहत विधानसभा को संकल्प विशेष बहुमत से पारित करना होता है, यानी उसकी कुल सदस्य संख्या का बहुमत और उपस्थित तथा मतदान करने वाले सदस्यों का दो-तिहाई। इसके बाद संसद साधारण बहुमत से पारित साधारण क़ानून द्वारा परिषद समाप्त करती है, और अनुच्छेद 169(3) कहता है कि ऐसा क़ानून अनुच्छेद 368 के प्रयोजन के लिए संविधान का संशोधन नहीं माना जाएगा। "
  "राष्ट्रपति को आदेश से परिषद समाप्त करने की शक्ति नहीं है; इसके लिए संसद का क़ानून चाहिए। उदाहरण के लिए, आंध्र प्रदेश ने इसी तरह 1985 में अपनी परिषद समाप्त की और 2007 में फिर से बनाई।",
  f"{COI} -- Article 169.",
  "polity-legislative-council-art169", craft="application")

S(PL, "medium", "At the end of a session, a House of Parliament is prorogued while some Bills are still pending before it. Consider the following statements:",
  "एक सत्र के अंत में संसद के एक सदन का सत्रावसान कर दिया जाता है, जबकि कुछ विधेयक अब भी उसके समक्ष लंबित हैं। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Bills pending before the House do not lapse because of the prorogation.",
   "The House is prorogued by the President, on the advice of the Government.",
   "Adjournment sine die, which ends the sittings of the session, is ordered by the presiding officer."],
  ["सत्रावसान के कारण सदन के समक्ष लंबित विधेयक व्यपगत नहीं होते।",
   "सदन का सत्रावसान राष्ट्रपति सरकार की सलाह पर करते हैं।",
   "अनिश्चितकाल के लिए स्थगन, जो सत्र की बैठकों को समाप्त करता है, पीठासीन अधिकारी करते हैं।"],
  C3, 2,
  "All three are correct. Prorogation ends a session but not the House, so Bills pending before it survive and can be taken up in the next session; only the dissolution of the Lok Sabha makes certain Bills lapse. "
  "Prorogation is an act of the President under Article 85(2)(a), on the Council of Ministers' advice, usually a few days after the House has been adjourned sine die by its presiding officer. Keeping the two steps -- and the two authorities -- apart is the point of the question.",
  "तीनों कथन सही हैं। सत्रावसान सत्र को समाप्त करता है, सदन को नहीं, इसलिए उसके समक्ष लंबित विधेयक बने रहते हैं और अगले सत्र में लिए जा सकते हैं; केवल लोकसभा के भंग होने से कुछ विधेयक व्यपगत होते हैं। "
  "सत्रावसान अनुच्छेद 85(2)(क) के तहत मंत्रिपरिषद की सलाह पर राष्ट्रपति का कार्य है, जो प्रायः पीठासीन अधिकारी द्वारा सदन को अनिश्चितकाल के लिए स्थगित करने के कुछ दिन बाद होता है। दोनों चरणों और दोनों प्राधिकारियों को अलग-अलग पहचानना ही इस प्रश्न का मर्म है।",
  f"{COI} -- Article 85; {LSS}.",
  "parl-adjournment-prorogation", craft="application")

S(PL, "medium", "The Lok Sabha has voted the demands for grants, and the Appropriation Bill is now before it. Consider the following statements:",
  "लोकसभा अनुदान माँगें स्वीकृत कर चुकी है, और अब विनियोग विधेयक उसके समक्ष है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["A member can move an amendment to the Bill to increase the amount of a grant already voted.",
   "Until the Bill becomes law, money cannot be withdrawn from the Consolidated Fund even for the grants that have been voted.",
   "To meet expenditure before the Bill is passed, the Lok Sabha can make a grant in advance through a vote on account."],
  ["कोई सदस्य पहले से स्वीकृत अनुदान की राशि बढ़ाने के लिए विधेयक में संशोधन प्रस्तुत कर सकता है।",
   "विधेयक के क़ानून बनने तक स्वीकृत अनुदानों के लिए भी संचित निधि से पैसा नहीं निकाला जा सकता।",
   "विधेयक पारित होने से पहले के व्यय के लिए लोकसभा लेखानुदान के ज़रिए अग्रिम अनुदान दे सकती है।"],
  C3, 1,
  "Statements 2 and 3 are correct. Article 114(3) says no money may be withdrawn from the Consolidated Fund except under an appropriation made by law, which is the core of Parliament's control of the purse. Since passing the full budget takes weeks, Article 116 lets the Lok Sabha grant money in advance for part of the year through a vote on account. "
  "Statement 1 is wrong: Article 114(2) bars any amendment to the Appropriation Bill that would vary the amount, or alter the purpose, of a grant already voted or of any charged expenditure. The debate on the Bill is confined to matters of public importance within the grants.",
  "कथन 2 और 3 सही हैं। अनुच्छेद 114(3) कहता है कि क़ानून द्वारा किए गए विनियोग के बिना संचित निधि से कोई पैसा नहीं निकाला जा सकता; यही संसद के धन-नियंत्रण का मूल है। चूँकि पूरा बजट पारित होने में हफ़्ते लगते हैं, इसलिए अनुच्छेद 116 लोकसभा को लेखानुदान के ज़रिए वर्ष के एक भाग के लिए अग्रिम धन देने देता है। "
  "कथन 1 गलत है: अनुच्छेद 114(2) विनियोग विधेयक में ऐसे किसी संशोधन पर रोक लगाता है जो पहले से स्वीकृत अनुदान या किसी भारित व्यय की राशि बदले या उसका प्रयोजन बदले। विधेयक पर बहस अनुदानों के भीतर सार्वजनिक महत्व के विषयों तक सीमित रहती है।",
  f"{COI} -- Articles 114 and 116.",
  "parl-appropriation-bill", craft="application")

# ================================================================ EXECUTIVE (7)
M(EX, "hard", "A convict's mercy petition reaches the President. The Union Council of Ministers advises that it be rejected, but the President personally feels that the sentence should be commuted. In the light of Maru Ram v. Union of India (1980), which one of the following states the constitutional position?",
  "एक दोषी की दया याचिका राष्ट्रपति के पास पहुँचती है। केंद्रीय मंत्रिपरिषद उसे अस्वीकार करने की सलाह देती है, पर राष्ट्रपति व्यक्तिगत रूप से मानते हैं कि सज़ा कम की जानी चाहिए। मारू राम बनाम भारत संघ (1980) के आलोक में निम्नलिखित में से कौन-सा संवैधानिक स्थिति बताता है?",
  ["The President must act on the advice of the Council of Ministers, as with his other executive powers",
   "The President may decide alone, since the power of pardon is a judicial power vested in him personally",
   "The President must refer the petition to the Supreme Court and act on its opinion under Article 143",
   "The President may commute the sentence on his own, and needs the Council's advice only to grant a full pardon"],
  ["राष्ट्रपति को अपनी अन्य कार्यपालिका शक्तियों की तरह मंत्रिपरिषद की सलाह पर कार्य करना होगा",
   "राष्ट्रपति अकेले निर्णय ले सकते हैं, क्योंकि क्षमा की शक्ति उनमें व्यक्तिगत रूप से निहित न्यायिक शक्ति है",
   "राष्ट्रपति को याचिका सर्वोच्च न्यायालय को भेजनी होगी और अनुच्छेद 143 के तहत उसकी राय पर कार्य करना होगा",
   "राष्ट्रपति स्वयं सज़ा कम कर सकते हैं, और पूर्ण क्षमा देने के लिए ही उन्हें मंत्रिपरिषद की सलाह चाहिए"],
  0,
  "In Maru Ram a Constitution Bench held that the power under Article 72 (and Article 161 for Governors) is exercised on the advice of the Council of Ministers, like the other executive powers of the Head of State; the decision is the Government's, taken in the President's name. "
  "Pardon is an executive act, not a judicial one -- Kehar Singh (1989) said the President may examine the record and differ with the courts' view of the evidence, but still on advice. There is no reference to the Supreme Court under Article 143, and no split between commutation and full pardon. Courts can review the decision only on narrow grounds.",
  "मारू राम में संविधान पीठ ने कहा कि अनुच्छेद 72 (और राज्यपालों के लिए अनुच्छेद 161) की शक्ति राष्ट्राध्यक्ष की अन्य कार्यपालिका शक्तियों की तरह मंत्रिपरिषद की सलाह पर प्रयोग होती है; निर्णय सरकार का होता है, जो राष्ट्रपति के नाम से लिया जाता है। "
  "क्षमा एक कार्यपालिका कार्य है, न्यायिक नहीं; केहर सिंह (1989) ने कहा कि राष्ट्रपति अभिलेख की जाँच कर साक्ष्य पर न्यायालयों के मत से भिन्न राय रख सकते हैं, पर फिर भी सलाह पर ही। अनुच्छेद 143 के तहत सर्वोच्च न्यायालय को कोई संदर्भ नहीं भेजा जाता, और सज़ा कम करने तथा पूर्ण क्षमा में ऐसा कोई बँटवारा नहीं है। न्यायालय इस निर्णय की समीक्षा केवल सीमित आधारों पर कर सकते हैं।",
  f"{SC} -- Maru Ram v. Union of India (1980), Kehar Singh v. Union of India (1989); {COI} -- Article 72.",
  "exec-maru-ram-pardon-advice", craft="application")

S(EX, "medium", "A soldier is sentenced to death by a court martial, and a civilian is sentenced to death by a court in a State for an offence against a law of that State. Consider the following statements:",
  "एक सैनिक को कोर्ट मार्शल मृत्युदंड देता है, और एक नागरिक को एक राज्य का न्यायालय उस राज्य के क़ानून के विरुद्ध अपराध के लिए मृत्युदंड देता है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["Only the President can pardon the soldier.",
   "The Governor of the State can commute the civilian's death sentence.",
   "The courts can review a President's decision on a mercy petition on limited grounds, such as mala fides or the ignoring of relevant material."],
  ["सैनिक को केवल राष्ट्रपति क्षमा कर सकते हैं।",
   "राज्य के राज्यपाल नागरिक के मृत्युदंड को लघुकृत (commute) कर सकते हैं।",
   "न्यायालय दया याचिका पर राष्ट्रपति के निर्णय की सीमित आधारों पर समीक्षा कर सकते हैं, जैसे दुर्भावना या प्रासंगिक सामग्री की अनदेखी।"],
  C3, 2,
  "All three are correct. Article 72 alone reaches sentences passed by a court martial, so the Governor has no role in the soldier's case. "
  "For the civilian, Article 161 lets the Governor suspend, remit or commute the sentence for an offence against a law to which the State's executive power extends, and Article 72(3) preserves that power even where the sentence is death. "
  "In Epuru Sudhakar (2006) the Supreme Court held that pardon decisions are open to judicial review on narrow grounds -- mala fides, irrelevant or extraneous considerations, or the failure to consider relevant material -- though the courts do not sit in appeal over the merits.",
  "तीनों कथन सही हैं। कोर्ट मार्शल द्वारा दिए गए दंड तक केवल अनुच्छेद 72 पहुँचता है, इसलिए सैनिक के मामले में राज्यपाल की कोई भूमिका नहीं है। "
  "नागरिक के मामले में अनुच्छेद 161 राज्यपाल को उस क़ानून के विरुद्ध अपराध के दंड को निलंबित करने, घटाने या लघुकृत करने देता है जिस तक राज्य की कार्यपालिका शक्ति पहुँचती है, और अनुच्छेद 72(3) मृत्युदंड के मामले में भी यह शक्ति सुरक्षित रखता है। "
  "एपुरु सुधाकर (2006) में सर्वोच्च न्यायालय ने कहा कि क्षमा के निर्णयों की सीमित आधारों पर न्यायिक समीक्षा हो सकती है, जैसे दुर्भावना, अप्रासंगिक या बाहरी विचार, या प्रासंगिक सामग्री पर विचार न करना; यद्यपि न्यायालय गुण-दोष पर अपील की तरह नहीं बैठते।",
  f"{COI} -- Articles 72 and 161; {SC} -- Epuru Sudhakar v. Government of Andhra Pradesh (2006).",
  "exec-pardon-court-martial-death-review", craft="application")

S(EX, "hard", "A State Legislature passes a Bill that would curtail the powers of the High Court. Consider the following statements:",
  "एक राज्य विधानमंडल ऐसा विधेयक पारित करता है जो उच्च न्यायालय की शक्तियों में कटौती करेगा। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Governor may give his own assent to the Bill instead of reserving it for the President.",
   "If the President returns the Bill and the Legislature passes it again, the President is bound to give assent.",
   "Had the Governor instead returned an ordinary Bill for reconsideration, he would be bound to assent if the Legislature passed it again."],
  ["राज्यपाल विधेयक को राष्ट्रपति के लिए आरक्षित करने के बजाय स्वयं उस पर अनुमति दे सकते हैं।",
   "यदि राष्ट्रपति विधेयक लौटा दें और विधानमंडल उसे फिर से पारित कर दे, तो राष्ट्रपति अनुमति देने को बाध्य हैं।",
   "यदि राज्यपाल ने इसके बजाय किसी साधारण विधेयक को पुनर्विचार के लिए लौटाया होता, तो विधानमंडल द्वारा उसे फिर पारित करने पर वे अनुमति देने को बाध्य होते।"],
  C3, 0,
  "Only statement 3 is correct. The second proviso to Article 200 says the Governor 'shall not assent to, but shall reserve' a Bill that would derogate from the powers of the High Court, since the High Court is part of a judicial system that stands above any one State; statement 1 is therefore wrong. "
  "Statement 2 is wrong: under Article 201 the President may return a reserved Bill for reconsideration, but even if the Legislature passes it again within six months, the President is not bound to assent. "
  "Statement 3 is the contrast: when the Governor himself returns an ordinary Bill, the first proviso to Article 200 obliges him to assent if it is passed again.",
  "केवल कथन 3 सही है। अनुच्छेद 200 का दूसरा परंतुक कहता है कि राज्यपाल उच्च न्यायालय की शक्तियों को कम करने वाले विधेयक पर 'अनुमति नहीं देंगे, बल्कि उसे आरक्षित करेंगे', क्योंकि उच्च न्यायालय एक ऐसी न्याय-व्यवस्था का अंग है जो किसी एक राज्य से ऊपर है; इसलिए कथन 1 गलत है। "
  "कथन 2 गलत है: अनुच्छेद 201 के तहत राष्ट्रपति आरक्षित विधेयक को पुनर्विचार के लिए लौटा सकते हैं, पर विधानमंडल के छह महीने में उसे फिर पारित करने पर भी राष्ट्रपति अनुमति देने को बाध्य नहीं हैं। "
  "कथन 3 इसका विरोधाभास दिखाता है: जब राज्यपाल स्वयं किसी साधारण विधेयक को लौटाते हैं, तो अनुच्छेद 200 का पहला परंतुक उसे फिर पारित किए जाने पर उन्हें अनुमति देने को बाध्य करता है।",
  f"{COI} -- Articles 200 and 201.",
  "exec-governor-bills-reservation-repassed", craft="application")

S(EX, "hard", "Two years into a President's term, the Supreme Court declares his election void. Consider the following statements:",
  "किसी राष्ट्रपति के कार्यकाल के दो वर्ष बाद सर्वोच्च न्यायालय उसका निर्वाचन शून्य घोषित कर देता है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The acts he performed as President before the declaration remain valid.",
   "The election could have been challenged on the ground that several State Assemblies stood dissolved when it was held.",
   "Only the Supreme Court could have decided the dispute about his election."],
  ["घोषणा से पहले राष्ट्रपति के रूप में उसके द्वारा किए गए कार्य वैध बने रहते हैं।",
   "निर्वाचन को इस आधार पर चुनौती दी जा सकती थी कि उसके समय कई राज्य विधानसभाएँ भंग थीं।",
   "उसके निर्वाचन से जुड़े विवाद का निर्णय केवल सर्वोच्च न्यायालय ही कर सकता था।"],
  C3, 1,
  "Statements 1 and 3 are correct. Article 71(2) protects the acts done by a President before his election is declared void, so that the State's business is not unsettled. Article 71(1) gives the Supreme Court exclusive jurisdiction over doubts and disputes about the election, and its decision is final. "
  "Statement 2 is wrong: clause (4), added by the 11th Amendment (1961), says the election cannot be challenged on the ground of any vacancy in the electoral college -- otherwise dissolved Assemblies could be used to stall or upset an election.",
  "कथन 1 और 3 सही हैं। अनुच्छेद 71(2) राष्ट्रपति द्वारा उसका निर्वाचन शून्य घोषित होने से पहले किए गए कार्यों की रक्षा करता है, ताकि राज्य का कामकाज डगमगाए नहीं। अनुच्छेद 71(1) निर्वाचन से जुड़ी शंकाओं और विवादों पर सर्वोच्च न्यायालय को अनन्य अधिकार देता है, और उसका निर्णय अंतिम है। "
  "कथन 2 गलत है: 11वें संशोधन (1961) द्वारा जोड़ा गया खंड (4) कहता है कि निर्वाचक मंडल में किसी रिक्ति के आधार पर निर्वाचन को चुनौती नहीं दी जा सकती; अन्यथा भंग विधानसभाओं के सहारे चुनाव को रोका या पलटा जा सकता था।",
  f"{COI} -- Article 71.",
  "exec-president-election-disputes-71", craft="application")

S(EX, "medium", "Parliament's Budget session ends in April. On 1 May the President promulgates an ordinance, and both Houses reassemble on 20 July. Consider the following statements:",
  "संसद का बजट सत्र अप्रैल में समाप्त होता है। 1 मई को राष्ट्रपति एक अध्यादेश जारी करते हैं, और दोनों सदन 20 जुलाई को फिर से बैठते हैं। निम्नलिखित कथनों पर विचार कीजिए:",
  ["Unless Parliament approves it earlier, the ordinance will cease to operate at the end of 31 August.",
   "The ordinance could also have been promulgated on a day when only the Rajya Sabha was in session.",
   "Re-promulgating the ordinance again and again without placing it before Parliament would be a fraud on the Constitution."],
  ["यदि संसद उसे पहले स्वीकृत न करे, तो अध्यादेश 31 अगस्त की समाप्ति पर प्रभावहीन हो जाएगा।",
   "अध्यादेश उस दिन भी जारी किया जा सकता था जब केवल राज्यसभा का सत्र चल रहा हो।",
   "अध्यादेश को संसद के समक्ष रखे बिना बार-बार फिर से जारी करना संविधान के साथ धोखा होगा।"],
  C3, 2,
  "All three are correct. Under Article 123(2)(a) an ordinance ceases six weeks after Parliament reassembles; from 20 July that is 31 August, unless resolutions disapproving it are passed earlier. "
  "Article 123(1) lets the President promulgate an ordinance 'except when both Houses of Parliament are in session', so it is possible when only one House is sitting, though the ordinance must still be laid before both. "
  "In Krishna Kumar Singh (2017) a seven-judge bench, examining ordinances that Bihar had kept alive for years, held that re-promulgation without placing them before the legislature is a fraud on the Constitution.",
  "तीनों कथन सही हैं। अनुच्छेद 123(2)(क) के तहत अध्यादेश संसद के फिर से बैठने के छह सप्ताह बाद प्रभावहीन हो जाता है; 20 जुलाई से यह 31 अगस्त होता है, जब तक उससे पहले उसे अस्वीकार करने वाले संकल्प पारित न हों। "
  "अनुच्छेद 123(1) राष्ट्रपति को 'सिवाय उस समय जब संसद के दोनों सदन सत्र में हों' अध्यादेश जारी करने देता है, इसलिए केवल एक सदन की बैठक चलते समय भी यह संभव है, यद्यपि अध्यादेश को दोनों सदनों के समक्ष रखना होगा। "
  "कृष्ण कुमार सिंह (2017) में सात न्यायाधीशों की पीठ ने बिहार में वर्षों तक जीवित रखे गए अध्यादेशों की जाँच कर कहा कि विधानमंडल के समक्ष रखे बिना उन्हें फिर से जारी करना संविधान के साथ धोखा है।",
  f"{COI} -- Article 123; {SC} -- Krishna Kumar Singh v. State of Bihar (2017).",
  "exec-ordinance-conditions-repromulgation", craft="application")

S(EX, "medium", "A private company asks the Attorney General of India to appear for it in a dispute. Consider the following statements:",
  "एक निजी कंपनी भारत के महान्यायवादी से किसी विवाद में अपनी ओर से पेश होने का अनुरोध करती है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["He may take up private briefs, since he is not a full-time counsel of the Government.",
   "He may appear for the company even in a dispute against the Government of India, provided he discloses his office.",
   "He holds office for a fixed term of five years."],
  ["वे निजी मामले ले सकते हैं, क्योंकि वे सरकार के पूर्णकालिक वकील नहीं हैं।",
   "वे भारत सरकार के विरुद्ध विवाद में भी कंपनी की ओर से पेश हो सकते हैं, बशर्ते अपना पद बताएँ।",
   "वे पाँच वर्ष के निश्चित कार्यकाल के लिए पद धारण करते हैं।"],
  C3, 0,
  "Only statement 1 is correct. The Attorney General (Article 76) is not a full-time counsel or a government servant, and may take private briefs. "
  "Statement 2 is wrong: the conditions of his engagement bar him from advising or holding a brief against the Government of India, or in any case in which he is likely to be called upon to advise it; disclosure does not cure the conflict. "
  "Statement 3 is wrong: the Constitution fixes no term -- he holds office during the pleasure of the President, and by convention resigns when the government changes. He must be qualified to be appointed a judge of the Supreme Court.",
  "केवल कथन 1 सही है। महान्यायवादी (अनुच्छेद 76) न पूर्णकालिक वकील हैं और न सरकारी सेवक, और वे निजी मामले ले सकते हैं। "
  "कथन 2 गलत है: उनकी नियुक्ति की शर्तें उन्हें भारत सरकार के विरुद्ध सलाह देने या मुक़दमा लेने से, या ऐसे किसी मामले से रोकती हैं जिसमें उनसे सरकार को सलाह देने को कहा जा सकता है; पद बता देने से यह हितों का टकराव दूर नहीं होता। "
  "कथन 3 गलत है: संविधान कोई कार्यकाल तय नहीं करता; वे राष्ट्रपति के प्रसादपर्यंत पद धारण करते हैं, और परंपरा से सरकार बदलने पर त्यागपत्र दे देते हैं। उन्हें सर्वोच्च न्यायालय का न्यायाधीश नियुक्त होने के योग्य होना चाहिए।",
  f"{COI} -- Article 76.",
  "exec-attorney-general-status", craft="application")

S(EX, "medium", "After an Assembly election, the Governor appoints as Chief Minister a person who is not a member of the State Legislature. Consider the following statements:",
  "विधानसभा चुनाव के बाद राज्यपाल ऐसे व्यक्ति को मुख्यमंत्री नियुक्त करते हैं जो राज्य विधानमंडल का सदस्य नहीं है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The appointment is made by the Governor, and not by the President.",
   "The person must become a member of the State Legislature within six months, or cease to be Chief Minister.",
   "Membership of the State's Legislative Council, where there is one, would meet this requirement."],
  ["नियुक्ति राज्यपाल करते हैं, राष्ट्रपति नहीं।",
   "उस व्यक्ति को छह महीने के भीतर राज्य विधानमंडल का सदस्य बनना होगा, अन्यथा वह मुख्यमंत्री नहीं रहेगा।",
   "जहाँ राज्य में विधान परिषद है, वहाँ उसकी सदस्यता से भी यह शर्त पूरी हो जाएगी।"],
  C3, 2,
  "All three are correct. Article 164(1) gives the appointment to the Governor, who by convention invites the leader who can command a majority in the Assembly. "
  "Article 164(4) allows a non-member to hold office for up to six consecutive months, within which he must enter the State Legislature. Either House will do, so a Chief Minister may sit in the Legislative Council, as several have; the Council of Ministers remains collectively responsible to the Assembly all the same. Article 164(1A) separately caps the ministry at 15 per cent of the Assembly's strength, with a minimum of twelve.",
  "तीनों कथन सही हैं। अनुच्छेद 164(1) नियुक्ति राज्यपाल को देता है, जो परंपरा से उस नेता को आमंत्रित करते हैं जो विधानसभा में बहुमत का समर्थन रखता हो। "
  "अनुच्छेद 164(4) किसी ग़ैर-सदस्य को लगातार अधिकतम छह महीने तक पद पर रहने देता है, जिसके भीतर उसे राज्य विधानमंडल में आना होगा। कोई भी सदन चलेगा, इसलिए मुख्यमंत्री विधान परिषद का सदस्य हो सकता है, जैसा कई रहे हैं; फिर भी मंत्रिपरिषद सामूहिक रूप से विधानसभा के प्रति उत्तरदायी रहती है। अनुच्छेद 164(1क) अलग से मंत्रिपरिषद को विधानसभा की संख्या के 15 प्रतिशत तक सीमित करता है, न्यूनतम बारह के साथ।",
  f"{COI} -- Article 164.",
  "executive-chief-minister-council-state", craft="application")

# ================================================================ TAGS for the 77 kept rows (Test 21's 4 are tagged already)
TAGS = {
 "parl-speaker-presides-elected-easy": "linkage", "parl-kihoto-paragraph-7": "linkage", "parl-lapse-of-bills-dissolution": "linkage",
 "polity-house-term-extension-emergency": "linkage", "parl-art121-judges-conduct": "precision", "parl-art249-rajya-sabha-states": "linkage",
 "parl-dual-membership-both-houses": "precision", "parl-sixty-days-absence": "linkage", "polity-rajya-sabha-dissolution-election": "linkage",
 "polity-speaker-party-casting-vote": "precision", "parl-committees-years-pairs": "recall", "polity-parliamentary-motions-features-pairs": "precision",
 "parl-articles-85-100-116-pairs": "recall", "parl-devices-questions-discussions-pairs": "precision", "parl-majorities-purposes-pairs": "precision",
 "polity-parliament-articles-pairs": "recall", "parl-joint-sitting-art108-easy": "recall", "parl-first-joint-sitting-dowry": "recall",
 "parl-leader-of-opposition-committees": "precision", "parl-rajya-sabha-chairman-not-member": "precision", "parl-consolidated-fund-266": "recall",
 "parl-question-hour-first-hour": "recall", "parl-lok-sabha-direct-rajya-term-easy": "recall", "polity-mp-qualification-age": "recall",
 "parl-budget-term-railway-revenue": "recall", "parl-closure-privilege-motions": "precision", "parl-deputy-speaker-position": "precision",
 "parl-money-bill-certificate-aadhaar": "precision", "parl-president-addresses-86-87": "precision", "parl-states-with-legislative-council": "recall",
 "polity-cut-motions-types": "precision", "polity-department-related-standing-committees": "recall", "polity-parliamentary-privileges-scope": "precision",
 "parl-adjournment-motion-features": "precision", "parl-committees-petitions-jpc-ethics": "recall", "parl-contingency-fund-public-account": "precision",
 "parl-houses-art88-demands-impeachment": "precision", "parl-legislative-council-size-chairman": "precision", "parl-lok-sabha-strength-ut-reservation": "recall",
 "parl-panel-of-chairpersons": "precision", "parl-private-members-bills": "recall", "parl-rajya-sabha-312-no-confidence": "precision",
 "parl-rajya-sabha-elections-domicile-open-ballot": "precision", "parl-rajya-sabha-strength-nomination": "precision", "parl-rules-language": "precision",
 "parl-state-assembly-strength": "recall", "polity-financial-committees-composition": "recall", "polity-joint-sitting-art108": "recall",
 "polity-parliamentary-devices-zero-hour": "precision", "polity-presiding-officers-lok-sabha": "precision", "polity-public-accounts-committee": "recall",
 "polity-quorum-sessions-secretariat": "precision", "exec-advice-nonjusticiable-74-2-361": "linkage", "exec-council-continues-after-dissolution": "linkage",
 "exec-nominal-executive-indirect-election": "linkage", "executive-pm-pleasure-collective-responsibility": "precision", "exec-presidents-distinctions-pairs": "recall",
 "exec-oath-authorities-pairs": "recall", "executive-articles-74-78-164-167-pairs": "recall", "executive-president-discharge-functions-cji": "recall",
 "exec-governor-not-discretionary": "precision", "exec-president-qualifications-not": "precision", "executive-governor-powers-not-hc-judges": "precision",
 "exec-president-head-pm-not-direct-easy": "recall", "exec-cabinet-secretariat-committees-countersign": "precision", "exec-governor-immunity-outsider-ut": "precision",
 "exec-ordinance-review-limits": "precision", "executive-presidential-reference-2025-assent": "precision", "executive-vice-president-election-term": "precision",
 "exec-council-of-ministers-size-cabinet": "recall", "exec-governor-discretion-163-nabam-rebia": "precision", "exec-president-electoral-college": "precision",
 "exec-president-impeachment": "precision", "exec-president-reconsideration-situational-discretion": "precision", "executive-governor-appointment-removal": "recall",
 "executive-presidential-veto-types": "precision", "executive-prime-minister-appointment": "recall"}

if __name__ == "__main__":
    write_updates("upg_l2_t02_polity.sql", statuses=("draft", "published"), tags=TAGS)
