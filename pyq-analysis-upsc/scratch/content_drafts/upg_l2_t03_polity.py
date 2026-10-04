# -*- coding: utf-8 -*-
"""Level 2 · Test 3 (Polity 3: Judiciary, Bodies, Elections & Laws) -- depth audit of 2026-10-04
(docs/upsc-question-design-standard.md §6).

All 105 rows in the test's five sub-topics were read and classified. Before: analytic 13, precision 54,
recall 38 (3 rows are Test 21's, already tagged). 22 rows are rewritten in place, keeping their concept ids,
types and difficulties.
  - 12 recall rows become cases:
      a paid surrogacy deal; RTE seats in a school of 80; which game the 2025 Act bans; an NGO's foreign grant;
      a priority household's NFSA ration; disability quota in 1,000 posts; which party qualifies as national;
      dissolving a dead marriage under Article 142; a UPSC member's tenure; a scheme announced after the MCC;
      a robbery reported at a police station; instant triple talaq in 2025.
  - 10 precision rows become cases:
      an online-purchase injury; a childless widow and her nephew; a suit to convert a mosque; an ED arrest;
      a bribe paid under pressure; a leaked SSC paper; a convicted MLA; withdrawn consent to the CBI; a foreign
      firm and Indian data; a 17-year-old accused.
After: analytic 35, precision 44, recall 26. The other 80 rows keep their content and get their craft tag,
except that pair 3 of the judgments pairs row loses the words 'Article 142', which answered the
complete-justice row (PAIR_FIX below).
Leaks avoided while drafting:
  - an 'Article 32' distractor (answers the Article 32 pair of the judiciary Articles row);
  - 'Article 324' in the Model Code row (answers the Part XV Articles row);
  - 'below eighteen' in a juvenile-justice distractor (answers the POCSO age row)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft_common as d
from draft_common import S, M, P, A, write_updates, CODE
from polity_common import C3, C4, T2

d.SUBJECT = "Polity"
d.REQUIRE_CRAFT = True
BO = "Constitutional & Statutory Bodies"
EL = "Elections"
JV = "Judicial-Verdicts"
JU = "Judiciary"
SL = "Statutory-Laws"
COI = "Constitution of India"
SC = "Supreme Court of India"
ECI = "Election Commission of India"
RPA = "Representation of the People Act, 1951"

# ================================================================ MCQs (7)
M(SL, "medium", "An Indian married couple holding a certificate of medical necessity agrees to pay a woman ₹10 lakh, over and above her medical expenses and insurance, to carry their child. Under the Surrogacy (Regulation) Act, 2021, which one of the following is correct?",
  "चिकित्सीय आवश्यकता का प्रमाण-पत्र रखने वाला एक भारतीय विवाहित दंपती एक महिला को, उसके चिकित्सा व्यय और बीमा के ऊपर, अपना बच्चा जन्म देने के लिए ₹10 लाख देने पर सहमत होता है। सरोगेसी (विनियमन) अधिनियम, 2021 के तहत निम्नलिखित में से कौन-सा सही है?",
  ["The arrangement is unlawful, because only altruistic surrogacy, with no payment beyond medical expenses and insurance, is allowed",
   "The arrangement is lawful, because the couple holds a certificate of medical necessity",
   "The arrangement is lawful as long as the payment is declared to the appropriate authority and the agreement is registered in advance",
   "The arrangement would be lawful if the couple were foreign nationals living in India"],
  ["यह व्यवस्था अवैध है, क्योंकि केवल परोपकारी सरोगेसी की अनुमति है, जिसमें चिकित्सा व्यय और बीमा से अधिक कोई भुगतान नहीं होता",
   "यह व्यवस्था वैध है, क्योंकि दंपती के पास चिकित्सीय आवश्यकता का प्रमाण-पत्र है",
   "यह व्यवस्था तब तक वैध है जब तक भुगतान उपयुक्त प्राधिकारी को बताया जाए और समझौता पहले से पंजीकृत हो",
   "यदि दंपती भारत में रह रहे विदेशी नागरिक होते, तो यह व्यवस्था वैध होती"],
  0,
  "The 2021 Act bans commercial surrogacy outright. It allows only altruistic surrogacy, in which the surrogate receives nothing beyond her medical expenses and insurance cover, for intending couples or women who meet the eligibility conditions and hold the required certificates. "
  "Paying ₹10 lakh on top makes this commercial surrogacy, which is an offence whatever certificates the couple holds or whatever paperwork is filed. India had become a hub of commercial surrogacy for foreign couples before the law; the Act ended that, so foreign nationals do not get a different rule.",
  "2021 का अधिनियम व्यावसायिक सरोगेसी पर पूरी रोक लगाता है। यह केवल परोपकारी सरोगेसी की अनुमति देता है, जिसमें सरोगेट माँ को उसके चिकित्सा व्यय और बीमा के सिवा कुछ नहीं मिलता, और वह भी उन दंपतियों या महिलाओं के लिए जो पात्रता की शर्तें पूरी करते हैं और आवश्यक प्रमाण-पत्र रखते हैं। "
  "ऊपर से ₹10 लाख देना इसे व्यावसायिक सरोगेसी बना देता है, जो अपराध है, चाहे दंपती के पास कोई भी प्रमाण-पत्र हो या कोई भी काग़ज़ी कार्रवाई की गई हो। क़ानून से पहले भारत विदेशी दंपतियों के लिए व्यावसायिक सरोगेसी का केंद्र बन गया था; अधिनियम ने इसे समाप्त किया, इसलिए विदेशी नागरिकों के लिए कोई अलग नियम नहीं है।",
  "Surrogacy (Regulation) Act, 2021.",
  "laws-surrogacy-altruistic", craft="application")

M(SL, "medium", "A private unaided school has 80 seats in Class 1. Under section 12(1)(c) of the Right of Children to Free and Compulsory Education Act, 2009, which one of the following is correct?",
  "एक निजी ग़ैर-सहायता प्राप्त विद्यालय में कक्षा 1 में 80 सीटें हैं। निःशुल्क और अनिवार्य बाल शिक्षा का अधिकार अधिनियम, 2009 की धारा 12(1)(ग) के तहत निम्नलिखित में से कौन-सा सही है?",
  ["At least 20 seats must go to children from weaker and disadvantaged groups, with the government reimbursing the school",
   "At least 16 seats must go to children from weaker and disadvantaged groups, with the parents paying a reduced fee",
   "At least 20 seats must go to children from weaker and disadvantaged groups, with the school bearing the whole cost itself",
   "At least 27 seats must go to children from weaker and disadvantaged groups, with the government reimbursing the school"],
  ["कम से कम 20 सीटें कमज़ोर और वंचित वर्गों के बच्चों को देनी होंगी, और सरकार विद्यालय को प्रतिपूर्ति करेगी",
   "कम से कम 16 सीटें कमज़ोर और वंचित वर्गों के बच्चों को देनी होंगी, और अभिभावक घटी हुई फ़ीस देंगे",
   "कम से कम 20 सीटें कमज़ोर और वंचित वर्गों के बच्चों को देनी होंगी, और पूरा ख़र्च विद्यालय स्वयं उठाएगा",
   "कम से कम 27 सीटें कमज़ोर और वंचित वर्गों के बच्चों को देनी होंगी, और सरकार विद्यालय को प्रतिपूर्ति करेगी"],
  0,
  "Section 12(1)(c) requires at least 25 per cent of entry-level seats -- 20 of 80 -- to be filled with children from weaker sections and disadvantaged groups, who study free until they complete elementary education. Under section 12(2) the government reimburses the school at its own per-child cost of education or the fee charged, whichever is less. "
  "The trap is the third option: the school does not bear the cost, which is why the Supreme Court upheld the provision as a reasonable restriction in Society for Unaided Private Schools of Rajasthan (2012).",
  "धारा 12(1)(ग) प्रवेश-स्तर की कम से कम 25 प्रतिशत सीटें, यानी 80 में से 20, कमज़ोर वर्गों और वंचित समूहों के बच्चों से भरने की अपेक्षा करती है, जो प्रारंभिक शिक्षा पूरी होने तक निःशुल्क पढ़ते हैं। धारा 12(2) के तहत सरकार विद्यालय को प्रति बच्चे अपने शिक्षा व्यय या ली जाने वाली फ़ीस में से जो कम हो, उसकी प्रतिपूर्ति करती है। "
  "जाल तीसरा विकल्प है: ख़र्च विद्यालय नहीं उठाता, और इसीलिए सर्वोच्च न्यायालय ने सोसाइटी फ़ॉर अनएडेड प्राइवेट स्कूल्स ऑफ़ राजस्थान (2012) में इस प्रावधान को उचित प्रतिबंध मानकर वैध ठहराया।",
  "Right of Children to Free and Compulsory Education Act, 2009, section 12.",
  "laws-rte-25-per-cent", craft="application")

M(SL, "medium", "Which one of the following would be prohibited under the Promotion and Regulation of Online Gaming Act, 2025?",
  "ऑनलाइन गेमिंग संवर्धन और विनियमन अधिनियम, 2025 के तहत निम्नलिखित में से क्या प्रतिबंधित होगा?",
  ["A fantasy-sports app in which users pay an entry fee in the hope of winning cash prizes",
   "An e-sports tournament recognised under the Act, in which the prize money comes only from sponsors",
   "A free quiz game for school students run by an educational trust",
   "A multiplayer game in which players buy decorative items but can never win money"],
  ["एक फ़ैंटेसी-स्पोर्ट्स ऐप जिसमें उपयोगकर्ता नक़द इनाम जीतने की आशा में प्रवेश शुल्क देते हैं",
   "अधिनियम के तहत मान्यता प्राप्त एक ई-स्पोर्ट्स प्रतियोगिता, जिसमें इनामी राशि केवल प्रायोजकों से आती है",
   "एक शैक्षिक न्यास द्वारा स्कूली विद्यार्थियों के लिए चलाया जाने वाला निःशुल्क क्विज़ गेम",
   "एक मल्टीप्लेयर गेम जिसमें खिलाड़ी सजावटी वस्तुएँ ख़रीदते हैं पर कभी पैसा नहीं जीत सकते"],
  0,
  "The Act bans 'online money games' -- games in which a user pays or stakes money in the expectation of winning money or other stakes -- whether they are based on skill or on chance. It also bars their advertisement and the processing of payments for them. "
  "A fantasy-sports contest with a cash entry fee and cash prizes is exactly that. The Act does the opposite for e-sports and for social and educational games, which it seeks to promote. Buying cosmetic items without any chance of winning money is not a money game.",
  "अधिनियम 'ऑनलाइन मनी गेम' पर प्रतिबंध लगाता है, यानी ऐसे खेल जिनमें उपयोगकर्ता पैसा या अन्य दाँव जीतने की अपेक्षा से पैसा देता या दाँव लगाता है, चाहे वे कौशल पर आधारित हों या संयोग पर। यह उनके विज्ञापन और उनके लिए भुगतान की प्रक्रिया पर भी रोक लगाता है। "
  "नक़द प्रवेश शुल्क और नक़द इनाम वाली फ़ैंटेसी-स्पोर्ट्स प्रतियोगिता ठीक यही है। ई-स्पोर्ट्स और सामाजिक तथा शैक्षिक खेलों के लिए अधिनियम उल्टा करता है, उन्हें बढ़ावा देना चाहता है। पैसा जीतने की किसी संभावना के बिना सजावटी वस्तुएँ ख़रीदना मनी गेम नहीं है।",
  "Promotion and Regulation of Online Gaming Act, 2025.",
  "laws-online-gaming-2025", craft="application")

M(EL, "medium", "Under the Election Symbols (Reservation and Allotment) Order, 1968, which one of the following parties would qualify for recognition as a national party?",
  "चुनाव चिह्न (आरक्षण और आवंटन) आदेश, 1968 के तहत निम्नलिखित में से कौन-सा दल राष्ट्रीय दल की मान्यता के योग्य होगा?",
  ["A party recognised as a State party in four States",
   "A party that won 2 per cent of the Lok Sabha seats, all of them from two States",
   "A party that polled 6 per cent of the valid votes in three States and won four Lok Sabha seats",
   "A party that won eleven Lok Sabha seats, all of them from a single State"],
  ["चार राज्यों में राज्य दल के रूप में मान्यता प्राप्त दल",
   "ऐसा दल जिसने लोकसभा की 2 प्रतिशत सीटें जीतीं, पर सभी केवल दो राज्यों से",
   "ऐसा दल जिसने तीन राज्यों में 6 प्रतिशत वैध मत पाए और लोकसभा की चार सीटें जीतीं",
   "ऐसा दल जिसने लोकसभा की ग्यारह सीटें जीतीं, पर सभी एक ही राज्य से"],
  0,
  "Paragraph 6B gives three alternative routes. A party qualifies if it is recognised as a State party in four or more States; or if it polls at least 6 per cent of the valid votes in four or more States at a general election to the Lok Sabha or the Assemblies and also wins four Lok Sabha seats; or if it wins at least 2 per cent of the Lok Sabha seats (11 of 543) from at least three States. "
  "Each distractor falls one condition short: two States instead of three, three States instead of four, or a single State. The spread across States is the point -- a national party must have a footing beyond one region.",
  "पैरा 6ख तीन वैकल्पिक रास्ते देता है। कोई दल तब योग्य है जब वह चार या अधिक राज्यों में राज्य दल के रूप में मान्य हो; या लोकसभा या विधानसभा के आम चुनाव में चार या अधिक राज्यों में कम से कम 6 प्रतिशत वैध मत पाए और साथ ही लोकसभा की चार सीटें जीते; या कम से कम तीन राज्यों से लोकसभा की कम से कम 2 प्रतिशत सीटें (543 में से 11) जीते। "
  "हर विकल्प एक शर्त से चूकता है: तीन की जगह दो राज्य, चार की जगह तीन राज्य, या केवल एक राज्य। राज्यों में फैलाव ही मूल बात है; राष्ट्रीय दल का आधार एक क्षेत्र से आगे होना चाहिए।",
  f"{ECI} -- Election Symbols (Reservation and Allotment) Order, 1968, paragraph 6B.",
  "elections-national-party-four-states", craft="application")

M(JU, "medium", "A couple has lived apart for many years and their marriage has irretrievably broken down, but one spouse refuses to agree to a divorce. Under which provision has the Supreme Court held that it can dissolve such a marriage?",
  "एक दंपती कई वर्षों से अलग रह रहा है और उनका विवाह पूरी तरह टूट चुका है, पर एक पक्ष तलाक़ पर सहमत होने से मना करता है। सर्वोच्च न्यायालय ने किस प्रावधान के तहत कहा है कि वह ऐसा विवाह भंग कर सकता है?",
  ["Article 142, to do complete justice in the case before it",
   "Article 141, since the law it declares binds all courts",
   "Article 136, since it can grant special leave to appeal from any court",
   "Article 137, as a review of the family court's order"],
  ["अनुच्छेद 142, अपने समक्ष मामले में पूर्ण न्याय करने के लिए",
   "अनुच्छेद 141, क्योंकि उसका घोषित क़ानून सभी न्यायालयों को बाँधता है",
   "अनुच्छेद 136, क्योंकि वह किसी भी न्यायालय से अपील की विशेष अनुमति दे सकता है",
   "अनुच्छेद 137, परिवार न्यायालय के आदेश के पुनर्विलोकन के रूप में"],
  0,
  "In Shilpa Sailesh v. Varun Sreenivasan (2023) a Constitution Bench held that, under Article 142, it can dissolve a marriage on the ground of irretrievable breakdown -- a ground the Hindu Marriage Act does not provide -- to do complete justice, even if one party opposes it. Each case is weighed on factors such as the length of separation and failed attempts at reconciliation. "
  "Article 141 makes the Court's law binding, Article 137 is its power to review its own judgments, and Article 136 lets it hear appeals by special leave -- none of them lets it grant relief that the statute does not provide. Article 142 is the Court's broad power to fill gaps, and its use is debated for that reason.",
  "शिल्पा शैलेश बनाम वरुण श्रीनिवासन (2023) में संविधान पीठ ने कहा कि वह अनुच्छेद 142 के तहत पूर्ण न्याय करने के लिए विवाह के पूरी तरह टूट जाने के आधार पर उसे भंग कर सकती है, भले ही एक पक्ष विरोध करे; यह आधार हिंदू विवाह अधिनियम में नहीं है। हर मामले को अलगाव की अवधि और सुलह के विफल प्रयासों जैसे कारकों पर तौला जाता है। "
  "अनुच्छेद 141 न्यायालय के क़ानून को बाध्यकारी बनाता है, अनुच्छेद 137 उसके अपने निर्णयों के पुनर्विलोकन की शक्ति है, और अनुच्छेद 136 उसे विशेष अनुमति से अपील सुनने देता है; इनमें से कोई उसे वह राहत देने नहीं देता जो क़ानून में नहीं है। अनुच्छेद 142 कमियाँ भरने की न्यायालय की व्यापक शक्ति है, और इसी कारण इसके उपयोग पर बहस होती है।",
  f"{SC} -- Shilpa Sailesh v. Varun Sreenivasan (2023); {COI} -- Article 142.",
  "judiciary-art142-complete-justice", craft="application")

M(BO, "medium", "A person aged 60 is appointed a member of the Union Public Service Commission. For how long can he hold office?",
  "60 वर्ष की आयु के एक व्यक्ति को संघ लोक सेवा आयोग का सदस्य नियुक्त किया जाता है। वह कितने समय तक पद धारण कर सकता है?",
  ["Until he turns 65, that is, for five years",
   "Until he turns 62, that is, for two years",
   "For the full term of six years, whatever his age",
   "Until he turns 65, and then for one more year if the President extends it"],
  ["65 वर्ष का होने तक, यानी पाँच वर्ष",
   "62 वर्ष का होने तक, यानी दो वर्ष",
   "आयु चाहे जो हो, पूरे छह वर्ष के कार्यकाल तक",
   "65 वर्ष का होने तक, और फिर राष्ट्रपति के बढ़ाने पर एक वर्ष और"],
  0,
  "Under Article 316(2), a member of the UPSC holds office for six years or until the age of 65, whichever comes first -- here the age limit bites after five years. Members of a State Public Service Commission retire at 62 instead, which is the trap in the second option. "
  "The Constitution provides no extension. A member may resign earlier, or be removed by the President in the manner Article 317 lays down -- for misbehaviour, only after an inquiry by the Supreme Court.",
  "अनुच्छेद 316(2) के तहत संघ लोक सेवा आयोग का सदस्य छह वर्ष या 65 वर्ष की आयु तक, जो भी पहले हो, पद धारण करता है; यहाँ आयु-सीमा पाँच वर्ष बाद लागू हो जाती है। राज्य लोक सेवा आयोग के सदस्य इसके बजाय 62 पर सेवानिवृत्त होते हैं, यही दूसरे विकल्प का जाल है। "
  "संविधान में कोई विस्तार का प्रावधान नहीं है। सदस्य पहले त्यागपत्र दे सकता है, या राष्ट्रपति उसे अनुच्छेद 317 में बताए ढंग से हटा सकते हैं; कदाचार के आधार पर केवल सर्वोच्च न्यायालय की जाँच के बाद।",
  f"{COI} -- Articles 316 and 317.",
  "bodies-upsc-tenure-age", craft="application")

M(SL, "medium", "A 17-year-old is accused of an offence punishable with a minimum of seven years' imprisonment. Under the Juvenile Justice (Care and Protection of Children) Act, 2015, which one of the following is correct?",
  "एक 17 वर्षीय किशोर पर ऐसे अपराध का आरोप है जिसकी न्यूनतम सज़ा सात वर्ष का कारावास है। किशोर न्याय (बालकों की देखरेख और संरक्षण) अधिनियम, 2015 के तहत निम्नलिखित में से कौन-सा सही है?",
  ["The Juvenile Justice Board may, after assessing him, send the case to the Children's Court",
   "He must be tried as an adult in an ordinary Sessions Court, since the offence is heinous",
   "He cannot be tried as an adult in any case, since the Act treats every juvenile alike",
   "He will be tried as an adult only if the victim's family applies for it within thirty days"],
  ["किशोर न्याय बोर्ड उसका मूल्यांकन करके मामला बाल न्यायालय को भेज सकता है",
   "अपराध जघन्य होने के कारण उस पर सामान्य सत्र न्यायालय में वयस्क की तरह मुक़दमा चलाना अनिवार्य है",
   "उस पर किसी भी स्थिति में वयस्क की तरह मुक़दमा नहीं चल सकता, क्योंकि अधिनियम सभी किशोरों से एक जैसा व्यवहार करता है",
   "उस पर वयस्क की तरह मुक़दमा तभी चलेगा जब पीड़ित का परिवार तीस दिनों में इसके लिए आवेदन करे"],
  0,
  "An offence carrying a minimum of seven years is a 'heinous offence' under the Act. For a child aged 16 to 18 accused of one, the Juvenile Justice Board makes a preliminary assessment of his mental and physical capacity, his ability to understand the consequences and the circumstances of the offence. It may then transfer the case to the Children's Court, which can try him as an adult. "
  "This is not automatic, and the victim's family has no such trigger. Even if he is convicted, he is kept in a place of safety until 21 and cannot be sentenced to death or to life imprisonment without the possibility of release. The 2015 Act introduced this route after the Delhi gang-rape case of 2012.",
  "न्यूनतम सात वर्ष की सज़ा वाला अपराध अधिनियम के तहत 'जघन्य अपराध' है। ऐसे अपराध के आरोपी 16 से 18 वर्ष के बालक के लिए किशोर न्याय बोर्ड उसकी मानसिक और शारीरिक क्षमता, परिणाम समझने की योग्यता और अपराध की परिस्थितियों का प्रारंभिक मूल्यांकन करता है, और फिर मामला बाल न्यायालय को भेज सकता है, जो उस पर वयस्क की तरह मुक़दमा चला सकता है। "
  "यह स्वचालित नहीं है, और पीड़ित के परिवार के पास ऐसा कोई अधिकार नहीं। दोषी ठहराए जाने पर भी उसे 21 वर्ष तक सुरक्षित स्थान में रखा जाता है, और उसे मृत्युदंड या रिहाई की संभावना के बिना आजीवन कारावास नहीं दिया जा सकता। 2015 के अधिनियम ने यह रास्ता 2012 के दिल्ली सामूहिक बलात्कार मामले के बाद जोड़ा।",
  "Juvenile Justice (Care and Protection of Children) Act, 2015, sections 15 and 18.",
  "statute-juvenile-justice-heinous-offences", craft="application")

# ================================================================ STATEMENTS (15)
S(SL, "hard", "An NGO registered under the Foreign Contribution (Regulation) Act receives ₹1 crore from a foreign foundation. Consider the following statements:",
  "विदेशी अंशदान (विनियमन) अधिनियम के तहत पंजीकृत एक NGO को एक विदेशी प्रतिष्ठान से ₹1 करोड़ मिलते हैं। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The money must first be received in its designated FCRA account at the State Bank of India, New Delhi Main Branch.",
   "It may pass ₹20 lakh of it to a smaller partner NGO working in tribal areas.",
   "It may spend up to ₹50 lakh of it on administrative expenses."],
  ["पैसा पहले भारतीय स्टेट बैंक की नई दिल्ली मुख्य शाखा में उसके निर्धारित FCRA खाते में आना चाहिए।",
   "वह इसमें से ₹20 लाख आदिवासी क्षेत्रों में काम करने वाले एक छोटे सहयोगी NGO को दे सकता है।",
   "वह इसमें से ₹50 लाख तक प्रशासनिक व्यय पर ख़र्च कर सकता है।"],
  C3, 0,
  "Only statement 1 is correct. The 2020 amendment requires every foreign contribution to be received first in the 'FCRA account' in the State Bank of India's New Delhi Main Branch, from which it may be moved to other accounts for use. "
  "Statement 2 is wrong: the amendment prohibits transferring foreign contribution to any other person or organisation, ending the practice of sub-granting to smaller NGOs. "
  "Statement 3 is wrong: administrative expenses are now capped at 20 per cent of the contribution -- ₹20 lakh here -- down from 50 per cent. The Supreme Court upheld the amendment in Noel Harper (2022).",
  "केवल कथन 1 सही है। 2020 का संशोधन हर विदेशी अंशदान को पहले भारतीय स्टेट बैंक की नई दिल्ली मुख्य शाखा के 'FCRA खाते' में प्राप्त करना अनिवार्य करता है, जहाँ से उसे उपयोग के लिए अन्य खातों में ले जाया जा सकता है। "
  "कथन 2 गलत है: संशोधन विदेशी अंशदान को किसी अन्य व्यक्ति या संगठन को हस्तांतरित करने पर रोक लगाता है, जिससे छोटे NGOs को उप-अनुदान देने की प्रथा समाप्त हुई। "
  "कथन 3 गलत है: प्रशासनिक व्यय अब अंशदान के 20 प्रतिशत तक सीमित है, यहाँ ₹20 लाख, जो पहले 50 प्रतिशत था। सर्वोच्च न्यायालय ने नोएल हार्पर (2022) में संशोधन को वैध ठहराया।",
  "Foreign Contribution (Regulation) Amendment Act, 2020; Supreme Court of India -- Noel Harper v. Union of India (2022).",
  "laws-fcra-2020", craft="application")

S(SL, "medium", "A rural household of five, in which the eldest woman is 42, holds a priority household ration card under the National Food Security Act, 2013. Consider the following statements:",
  "पाँच सदस्यों का एक ग्रामीण परिवार, जिसमें सबसे बड़ी महिला 42 वर्ष की है, राष्ट्रीय खाद्य सुरक्षा अधिनियम, 2013 के तहत प्राथमिकता परिवार का राशन कार्ड रखता है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The household is entitled to 25 kg of foodgrains a month.",
   "The ration card is issued in the name of the eldest woman as head of the household.",
   "The household now receives this grain free of cost.",
   "Had it been an Antyodaya Anna Yojana household, it would be entitled to 35 kg a month whatever its size."],
  ["परिवार हर महीने 25 किग्रा अनाज का हक़दार है।",
   "राशन कार्ड परिवार की मुखिया के रूप में सबसे बड़ी महिला के नाम पर जारी होता है।",
   "परिवार को अब यह अनाज निःशुल्क मिलता है।",
   "यदि यह अंत्योदय अन्न योजना का परिवार होता, तो आकार चाहे जो हो, यह हर महीने 35 किग्रा का हक़दार होता।"],
  C4, 3,
  "All four are correct. Priority households get 5 kg per person per month, so 25 kg for five, while Antyodaya households -- the poorest -- get a fixed 35 kg per household. The Act makes the eldest woman aged 18 or above the head of the household for the ration card, to strengthen women's control over food. "
  "Since 1 January 2023 the Centre has supplied NFSA foodgrains free, and from 1 January 2024 this was extended for five years. The Act also provides maternity benefit and meals for children, and it covers up to 75 per cent of the rural and 50 per cent of the urban population.",
  "चारों कथन सही हैं। प्राथमिकता परिवारों को प्रति व्यक्ति प्रति माह 5 किग्रा मिलता है, यानी पाँच के लिए 25 किग्रा, जबकि सबसे ग़रीब अंत्योदय परिवारों को प्रति परिवार निश्चित 35 किग्रा मिलता है। अधिनियम राशन कार्ड के लिए 18 वर्ष या उससे अधिक की सबसे बड़ी महिला को परिवार का मुखिया बनाता है, ताकि भोजन पर महिलाओं का नियंत्रण बढ़े। "
  "1 जनवरी 2023 से केंद्र NFSA का अनाज निःशुल्क दे रहा है, और 1 जनवरी 2024 से इसे पाँच वर्ष के लिए बढ़ाया गया। अधिनियम मातृत्व लाभ और बच्चों के लिए भोजन भी देता है, और ग्रामीण आबादी के 75 प्रतिशत तथा शहरी आबादी के 50 प्रतिशत तक को शामिल करता है।",
  "National Food Security Act, 2013; Department of Food and Public Distribution.",
  "laws-national-food-security-act", craft="application")

S(SL, "medium", "A State government advertises 1,000 posts in its departments. Consider the following statements in the light of the Rights of Persons with Disabilities Act, 2016:",
  "एक राज्य सरकार अपने विभागों में 1,000 पदों का विज्ञापन देती है। दिव्यांगजन अधिकार अधिनियम, 2016 के आलोक में निम्नलिखित कथनों पर विचार कीजिए:",
  ["At least 40 of the posts must be reserved for persons with benchmark disabilities.",
   "A candidate assessed with a 30 per cent disability counts as a person with a benchmark disability.",
   "A survivor of an acid attack can be among the persons with disabilities covered by the Act."],
  ["कम से कम 40 पद मानक दिव्यांगता वाले व्यक्तियों के लिए आरक्षित होने चाहिए।",
   "30 प्रतिशत दिव्यांगता वाला उम्मीदवार मानक दिव्यांगता वाला व्यक्ति माना जाता है।",
   "एसिड हमले की पीड़िता अधिनियम में शामिल दिव्यांगजनों में से हो सकती है।"],
  C3, 1,
  "Statements 1 and 3 are correct. Section 34 requires at least 4 per cent of vacancies in government establishments to be reserved for persons with benchmark disabilities -- 40 of 1,000 -- up from 3 per cent under the 1995 law. Acid-attack victims are one of the 21 specified disabilities that the 2016 Act recognises, up from seven earlier. "
  "Statement 2 is wrong: a 'benchmark disability' means not less than 40 per cent of a specified disability, as certified by the authority, so a 30 per cent assessment falls short.",
  "कथन 1 और 3 सही हैं। धारा 34 सरकारी प्रतिष्ठानों में कम से कम 4 प्रतिशत रिक्तियाँ मानक दिव्यांगता वाले व्यक्तियों के लिए आरक्षित करने की अपेक्षा करती है, यानी 1,000 में से 40, जो 1995 के क़ानून में 3 प्रतिशत थी। एसिड हमले के पीड़ित उन 21 निर्दिष्ट दिव्यांगताओं में से एक हैं जिन्हें 2016 का अधिनियम मान्यता देता है, जो पहले सात थीं। "
  "कथन 2 गलत है: 'मानक दिव्यांगता' का अर्थ है किसी निर्दिष्ट दिव्यांगता का कम से कम 40 प्रतिशत, जैसा प्राधिकारी प्रमाणित करे, इसलिए 30 प्रतिशत का आकलन कम पड़ता है।",
  "Rights of Persons with Disabilities Act, 2016, sections 2 and 34.",
  "laws-rpwd-2016", craft="application")

S(EL, "medium", "Two weeks after the Election Commission announces the schedule for the Lok Sabha election, the Union Government plans to announce a new cash-transfer scheme. Consider the following statements:",
  "निर्वाचन आयोग द्वारा लोकसभा चुनाव का कार्यक्रम घोषित करने के दो सप्ताह बाद केंद्र सरकार एक नई नक़द-हस्तांतरण योजना घोषित करने की योजना बनाती है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Model Code of Conduct is already in force.",
   "Breaching the Model Code is in itself a criminal offence punishable under the Code.",
   "The Election Commission can direct that the announcement be held back until polling is over."],
  ["आदर्श आचार संहिता पहले ही लागू है।",
   "आदर्श आचार संहिता का उल्लंघन अपने आप में संहिता के तहत दंडनीय आपराधिक अपराध है।",
   "निर्वाचन आयोग निर्देश दे सकता है कि घोषणा मतदान पूरा होने तक रोकी जाए।"],
  C3, 1,
  "Statements 1 and 3 are correct. The Model Code comes into force the moment the Commission announces the schedule, and one of its rules bars the party in power from announcing new schemes or financial grants that could influence voters. "
  "Statement 2 is wrong: the Code has no statutory backing -- it is a consensus document of the parties -- so a breach is not an offence under the Code itself. The Commission enforces it through its constitutional power of superintendence of elections under Article 324: it can issue directions, censure, bar campaigning, or stop the scheme until polling ends. Some conduct it covers is separately an offence under the criminal law or the RPA.",
  "कथन 1 और 3 सही हैं। आदर्श आचार संहिता आयोग द्वारा कार्यक्रम घोषित करते ही लागू हो जाती है, और इसका एक नियम सत्ताधारी दल को मतदाताओं को प्रभावित कर सकने वाली नई योजनाएँ या वित्तीय अनुदान घोषित करने से रोकता है। "
  "कथन 2 गलत है: संहिता को वैधानिक आधार नहीं है; यह दलों की सहमति से बना दस्तावेज़ है, इसलिए उल्लंघन संहिता के तहत अपराध नहीं है। आयोग इसे अनुच्छेद 324 के तहत चुनावों के अधीक्षण की अपनी संवैधानिक शक्ति से लागू करता है: वह निर्देश दे सकता है, निंदा कर सकता है, प्रचार पर रोक लगा सकता है, या मतदान तक योजना रुकवा सकता है। इसके दायरे के कुछ आचरण आपराधिक क़ानून या जनप्रतिनिधित्व अधिनियम के तहत अलग से अपराध हैं।",
  f"{ECI} -- Model Code of Conduct; {COI} -- Article 324.",
  "elections-model-code-of-conduct", craft="application")

S(JV, "medium", "A woman goes to a police station to report a robbery at her house, and the man she accuses is later arrested. Consider the following statements in the light of Supreme Court judgments:",
  "एक महिला अपने घर में हुई लूट की रिपोर्ट करने पुलिस थाने जाती है, और जिस व्यक्ति पर वह आरोप लगाती है उसे बाद में गिरफ़्तार किया जाता है। सर्वोच्च न्यायालय के निर्णयों के आलोक में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The police must register an FIR, since robbery is a cognisable offence.",
   "At the arrest, an arrest memo must be prepared and a relative or friend of the arrested man informed.",
   "The State's Director General of Police, who oversees the case, is entitled to a minimum tenure of two years."],
  ["पुलिस को FIR दर्ज करनी होगी, क्योंकि लूट संज्ञेय अपराध है।",
   "गिरफ़्तारी के समय गिरफ़्तारी ज्ञापन बनाना होगा और गिरफ़्तार व्यक्ति के किसी रिश्तेदार या मित्र को सूचित करना होगा।",
   "मामले की देखरेख करने वाले राज्य के पुलिस महानिदेशक को न्यूनतम दो वर्ष के कार्यकाल का अधिकार है।"],
  C3, 2,
  "All three are correct, each from a different judgment. Lalita Kumari (2013) held that registering an FIR is mandatory when the information discloses a cognisable offence, leaving a preliminary inquiry only for a few categories such as matrimonial disputes; the BNSS now also allows one for offences punishable with three to seven years, which robbery exceeds. "
  "D.K. Basu (1997) laid down guidelines for every arrest -- identifiable officers, an arrest memo signed by a witness, informing a relative or friend, medical examination -- that are now largely written into criminal procedure law. "
  "Prakash Singh (2006) directed police reforms, including a minimum tenure of two years for the DGP irrespective of the date of superannuation, so that police leadership is not shuffled at will.",
  "तीनों कथन सही हैं, और हर एक अलग निर्णय से है। ललिता कुमारी (2013) ने कहा कि सूचना से संज्ञेय अपराध का खुलासा होने पर FIR दर्ज करना अनिवार्य है; प्रारंभिक जाँच केवल वैवाहिक विवाद जैसी कुछ श्रेणियों के लिए है; BNSS अब तीन से सात वर्ष की सज़ा वाले अपराधों में भी इसकी अनुमति देती है, और लूट की सज़ा इससे अधिक है। "
  "डी.के. बसु (1997) ने हर गिरफ़्तारी के लिए दिशानिर्देश दिए, जैसे पहचान योग्य अधिकारी, गवाह द्वारा हस्ताक्षरित गिरफ़्तारी ज्ञापन, किसी रिश्तेदार या मित्र को सूचना और चिकित्सा जाँच; ये अब बड़े पैमाने पर आपराधिक प्रक्रिया क़ानून में लिखे जा चुके हैं। "
  "प्रकाश सिंह (2006) ने पुलिस सुधारों का निर्देश दिया, जिनमें सेवानिवृत्ति की तिथि से अलग DGP के लिए न्यूनतम दो वर्ष का कार्यकाल शामिल है, ताकि पुलिस नेतृत्व को मनमाने ढंग से बदला न जाए।",
  f"{SC} -- Lalita Kumari (2013), D.K. Basu (1997), Prakash Singh (2006).",
  "verdicts-dk-basu-lalita-kumari-prakash-singh", craft="application")

S(JV, "medium", "In 2025 a man pronounces instant triple talaq (talaq-e-biddat) to his wife. Consider the following statements:",
  "2025 में एक व्यक्ति अपनी पत्नी को तत्काल तीन तलाक़ (तलाक़-ए-बिद्दत) देता है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The pronouncement is void, and he can be punished with imprisonment for making it.",
   "His wife is entitled to claim a subsistence allowance for herself and their dependent children.",
   "Had he instead accused her of adultery, adultery would not be a crime, though it could be a ground for divorce."],
  ["यह घोषणा शून्य है, और इसे करने के लिए उसे कारावास से दंडित किया जा सकता है।",
   "उसकी पत्नी अपने और आश्रित बच्चों के लिए निर्वाह भत्ता माँगने की हक़दार है।",
   "यदि उसने इसके बजाय उस पर व्यभिचार का आरोप लगाया होता, तो व्यभिचार अपराध नहीं होता, यद्यपि वह तलाक़ का आधार हो सकता था।"],
  C3, 2,
  "All three are correct. In Shayara Bano (2017) the Supreme Court held instant triple talaq unconstitutional by 3:2, and the Muslim Women (Protection of Rights on Marriage) Act, 2019 declared it void and illegal, punishable with up to three years' imprisonment, and entitled the wife to a subsistence allowance and custody of minor children. "
  "In Joseph Shine (2018) the Court struck down the offence of adultery under Section 497 of the IPC as treating the wife as her husband's property; adultery remains a civil wrong and a ground for divorce, and the Bharatiya Nyaya Sanhita does not make it an offence.",
  "तीनों कथन सही हैं। शायरा बानो (2017) में सर्वोच्च न्यायालय ने 3:2 से तत्काल तीन तलाक़ को असंवैधानिक माना, और मुस्लिम महिला (विवाह अधिकार संरक्षण) अधिनियम, 2019 ने इसे शून्य और अवैध घोषित कर तीन वर्ष तक के कारावास से दंडनीय बनाया तथा पत्नी को निर्वाह भत्ते और अवयस्क बच्चों की अभिरक्षा का अधिकार दिया। "
  "जोसेफ़ शाइन (2018) में न्यायालय ने भारतीय दंड संहिता की धारा 497 के व्यभिचार अपराध को पत्नी को पति की संपत्ति मानने वाला बताकर रद्द किया; व्यभिचार एक सिविल दोष और तलाक़ का आधार बना रहता है, और भारतीय न्याय संहिता इसे अपराध नहीं बनाती।",
  f"{SC} -- Shayara Bano v. Union of India (2017), Joseph Shine v. Union of India (2018); Muslim Women (Protection of Rights on Marriage) Act, 2019.",
  "verdicts-triple-talaq-adultery-marriage", craft="application")

S(SL, "medium", "A buyer living in Patna orders a mobile phone online from a seller based in Bengaluru. The battery explodes and injures him. Consider the following statements in the light of the Consumer Protection Act, 2019:",
  "पटना में रहने वाला एक ख़रीदार बेंगलुरु के एक विक्रेता से ऑनलाइन मोबाइल फ़ोन मँगवाता है। बैटरी फट जाती है और वह घायल हो जाता है। उपभोक्ता संरक्षण अधिनियम, 2019 के आलोक में निम्नलिखित कथनों पर विचार कीजिए:",
  ["He can file his complaint in the consumer commission within whose jurisdiction he lives.",
   "Since he bought the phone online, the Act does not apply to the purchase.",
   "He can claim only against the seller, not against the manufacturer, since he bought from the seller."],
  ["वह उस उपभोक्ता आयोग में शिकायत कर सकता है जिसके क्षेत्राधिकार में वह रहता है।",
   "चूँकि उसने फ़ोन ऑनलाइन ख़रीदा, इसलिए अधिनियम इस ख़रीद पर लागू नहीं होता।",
   "वह केवल विक्रेता के विरुद्ध दावा कर सकता है, निर्माता के विरुद्ध नहीं, क्योंकि उसने विक्रेता से ख़रीदा।"],
  C3, 0,
  "Only statement 1 is correct. The 2019 Act lets a consumer file where he resides or works for gain, not only where the seller is based, and allows e-filing. "
  "Statement 2 is wrong: the definition of 'consumer' expressly covers goods and services bought through electronic means, and e-commerce rules under the Act place duties on platforms and sellers. "
  "Statement 3 is wrong: the Act's new chapter on 'product liability' lets the injured consumer claim compensation from the manufacturer, the service provider or the seller for harm caused by a defective product -- the manufacturer is usually the one primarily liable for a manufacturing defect.",
  "केवल कथन 1 सही है। 2019 का अधिनियम उपभोक्ता को वहाँ शिकायत करने देता है जहाँ वह रहता है या लाभ के लिए काम करता है, न कि केवल वहाँ जहाँ विक्रेता है, और ई-फ़ाइलिंग की सुविधा देता है। "
  "कथन 2 गलत है: 'उपभोक्ता' की परिभाषा इलेक्ट्रॉनिक माध्यम से ख़रीदी गई वस्तुओं और सेवाओं को स्पष्ट रूप से शामिल करती है, और अधिनियम के तहत ई-कॉमर्स नियम प्लेटफ़ॉर्म और विक्रेताओं पर कर्तव्य डालते हैं। "
  "कथन 3 गलत है: अधिनियम का नया 'उत्पाद दायित्व' अध्याय घायल उपभोक्ता को दोषपूर्ण उत्पाद से हुई हानि के लिए निर्माता, सेवा प्रदाता या विक्रेता से मुआवज़ा माँगने देता है; निर्माण दोष के लिए प्रायः निर्माता ही मुख्य रूप से उत्तरदायी होता है।",
  "Consumer Protection Act, 2019.",
  "laws-consumer-protection-2019", craft="application")

S(SL, "medium", "A childless 70-year-old widow is refused support by her nephew, who will inherit her house. Consider the following statements in the light of the Maintenance and Welfare of Parents and Senior Citizens Act, 2007:",
  "70 वर्ष की एक निःसंतान विधवा को उसका भतीजा, जो उसका घर विरासत में पाएगा, सहारा देने से मना करता है। माता-पिता और वरिष्ठ नागरिकों का भरण-पोषण तथा कल्याण अधिनियम, 2007 के आलोक में निम्नलिखित कथनों पर विचार कीजिए:",
  ["She can claim maintenance from the nephew before a Maintenance Tribunal.",
   "She may engage a lawyer to argue her case before the Tribunal.",
   "Had she transferred her house to him on the condition that he would look after her, the transfer could be declared void on his failure to do so."],
  ["वह भरण-पोषण अधिकरण के समक्ष भतीजे से भरण-पोषण माँग सकती है।",
   "वह अधिकरण के समक्ष अपना मामला लड़ने के लिए वकील रख सकती है।",
   "यदि उसने अपना घर इस शर्त पर उसे हस्तांतरित किया होता कि वह उसकी देखभाल करेगा, तो ऐसा न करने पर हस्तांतरण शून्य घोषित किया जा सकता था।"],
  C3, 1,
  "Statements 1 and 3 are correct. For a childless senior citizen, the duty to maintain falls on a relative who possesses or would inherit the senior citizen's property, and the claim goes to a Maintenance Tribunal, which must ordinarily decide within 90 days. "
  "Section 23 lets a senior citizen have a transfer of property declared void if it was made on the condition of care and the transferee fails to provide it. "
  "Statement 2 is wrong: section 17 bars legal practitioners from appearing before the Tribunal, so that elderly claimants are not outmatched; the senior citizen may be represented by the Maintenance Officer instead.",
  "कथन 1 और 3 सही हैं। निःसंतान वरिष्ठ नागरिक के मामले में भरण-पोषण का दायित्व उस रिश्तेदार पर है जिसके पास उसकी संपत्ति है या जो उसे विरासत में पाएगा, और दावा भरण-पोषण अधिकरण में जाता है, जिसे सामान्यतः 90 दिनों में निर्णय करना होता है। "
  "धारा 23 वरिष्ठ नागरिक को ऐसा संपत्ति-हस्तांतरण शून्य घोषित कराने देती है जो देखभाल की शर्त पर किया गया हो और जिसे पाने वाला देखभाल न करे। "
  "कथन 2 गलत है: धारा 17 अधिकरण के समक्ष विधि व्यवसायियों के पेश होने पर रोक लगाती है, ताकि बुज़ुर्ग दावेदार कमज़ोर न पड़ें; वरिष्ठ नागरिक की ओर से भरण-पोषण अधिकारी पेश हो सकता है।",
  "Maintenance and Welfare of Parents and Senior Citizens Act, 2007, sections 4, 17 and 23.",
  "laws-senior-citizens-maintenance", craft="application")

S(SL, "medium", "In 2025 a suit is filed seeking to convert a mosque into a temple, on the ground that a temple stood at the site in the eighteenth century. Consider the following statements in the light of the Places of Worship (Special Provisions) Act, 1991:",
  "2025 में एक मस्जिद को मंदिर में बदलने के लिए यह कहते हुए मुक़दमा दायर किया जाता है कि अठारहवीं सदी में उस स्थान पर एक मंदिर था। उपासना स्थल (विशेष उपबंध) अधिनियम, 1991 के आलोक में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The Act bars proceedings that seek to change the religious character of a place of worship.",
   "If the mosque were a monument protected under the Ancient Monuments and Archaeological Sites and Remains Act, 1958, the Act would still apply to it.",
   "The religious character to be preserved is the one that existed on 26 January 1950."],
  ["अधिनियम ऐसी कार्यवाही पर रोक लगाता है जो किसी उपासना स्थल का धार्मिक स्वरूप बदलना चाहती हो।",
   "यदि वह मस्जिद प्राचीन संस्मारक तथा पुरातत्वीय स्थल और अवशेष अधिनियम, 1958 के तहत संरक्षित स्मारक होती, तब भी अधिनियम उस पर लागू होता।",
   "जिस धार्मिक स्वरूप को बनाए रखना है, वह 26 जनवरी 1950 को विद्यमान स्वरूप है।"],
  C3, 0,
  "Only statement 1 is correct. The Act freezes the religious character of every place of worship as it existed on 15 August 1947 -- not 26 January 1950 -- and section 4(2) bars suits and proceedings to change it, abating those pending on the date it came into force. "
  "Statement 2 is wrong: section 4(3) exempts ancient and historical monuments and archaeological sites covered by the 1958 Act, which is why disputes over such sites have taken a different route. The Ayodhya site alone was excluded by section 5. The Act's validity is under challenge before the Supreme Court.",
  "केवल कथन 1 सही है। अधिनियम हर उपासना स्थल के धार्मिक स्वरूप को उसी रूप में स्थिर करता है जैसा वह 15 अगस्त 1947 को था, न कि 26 जनवरी 1950 को, और धारा 4(2) उसे बदलने के मुक़दमों और कार्यवाहियों पर रोक लगाती है, तथा अधिनियम लागू होने की तिथि पर लंबित कार्यवाहियाँ समाप्त करती है। "
  "कथन 2 गलत है: धारा 4(3) 1958 के अधिनियम के दायरे वाले प्राचीन और ऐतिहासिक स्मारकों तथा पुरातात्विक स्थलों को छूट देती है, इसीलिए ऐसे स्थलों के विवाद अलग रास्ते से चले हैं। अकेले अयोध्या स्थल को धारा 5 ने बाहर रखा था। अधिनियम की वैधता को सर्वोच्च न्यायालय में चुनौती दी गई है।",
  "Places of Worship (Special Provisions) Act, 1991, sections 3-5.",
  "laws-places-of-worship-1991", craft="application")

S(SL, "hard", "The Enforcement Directorate arrests a businessman under the Prevention of Money-laundering Act, 2002, and provisionally attaches his property. Consider the following statements:",
  "प्रवर्तन निदेशालय धन-शोधन निवारण अधिनियम, 2002 के तहत एक व्यवसायी को गिरफ़्तार करता है और उसकी संपत्ति को अनंतिम रूप से कुर्क करता है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["He must be given the grounds of his arrest in writing.",
   "The provisional attachment must be confirmed by the Adjudicating Authority, or it lapses after 180 days.",
   "He can be prosecuted for money laundering even if no scheduled offence lies behind the money."],
  ["उसे गिरफ़्तारी के आधार लिखित रूप में दिए जाने चाहिए।",
   "अनंतिम कुर्की की पुष्टि न्यायनिर्णायक प्राधिकारी को करनी होगी, अन्यथा वह 180 दिनों बाद समाप्त हो जाती है।",
   "धन के पीछे कोई अनुसूचित अपराध न होने पर भी उस पर धन-शोधन का मुक़दमा चल सकता है।"],
  C3, 1,
  "Statements 1 and 2 are correct. In Pankaj Bansal (2023) the Supreme Court held that the grounds of arrest under the Act must be furnished to the arrested person in writing, so that he can seek legal advice and bail. A provisional attachment lasts up to 180 days unless the Adjudicating Authority confirms it under section 8. "
  "Statement 3 is wrong: money laundering is defined around the 'proceeds of crime' from a scheduled offence. In Vijay Madanlal Choudhary (2022) the Court held that if the person is acquitted of the scheduled offence, or it is quashed, there can be no money-laundering case on that basis.",
  "कथन 1 और 2 सही हैं। पंकज बंसल (2023) में सर्वोच्च न्यायालय ने कहा कि अधिनियम के तहत गिरफ़्तारी के आधार गिरफ़्तार व्यक्ति को लिखित रूप में दिए जाएँ, ताकि वह क़ानूनी सलाह और ज़मानत माँग सके। अनंतिम कुर्की 180 दिनों तक रहती है, जब तक न्यायनिर्णायक प्राधिकारी धारा 8 के तहत उसकी पुष्टि न करे। "
  "कथन 3 गलत है: धन-शोधन की परिभाषा किसी अनुसूचित अपराध से प्राप्त 'अपराध की आय' पर टिकी है। विजय मदनलाल चौधरी (2022) में न्यायालय ने कहा कि यदि व्यक्ति अनुसूचित अपराध से बरी हो जाए या वह रद्द हो जाए, तो उस आधार पर धन-शोधन का मामला नहीं बन सकता।",
  f"Prevention of Money-laundering Act, 2002; {SC} -- Pankaj Bansal v. Union of India (2023), Vijay Madanlal Choudhary v. Union of India (2022).",
  "laws-pmla-arrest-attachment", craft="application")

S(SL, "hard", "An official forces a businessman to pay him a bribe. The businessman reports the matter to the police within a week. Consider the following statements in the light of the Prevention of Corruption Act, 1988, as amended in 2018:",
  "एक अधिकारी एक व्यवसायी को रिश्वत देने के लिए मजबूर करता है। व्यवसायी एक सप्ताह के भीतर पुलिस को मामले की सूचना देता है। 2018 में संशोधित भ्रष्टाचार निवारण अधिनियम, 1988 के आलोक में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The businessman is not liable for the offence of giving a bribe.",
   "An investigation into a decision that the official took in the discharge of his duties needs the prior approval of the authority competent to remove him.",
   "No such prior approval is needed to arrest the official on the spot while he is accepting the bribe."],
  ["व्यवसायी रिश्वत देने के अपराध के लिए उत्तरदायी नहीं है।",
   "अधिकारी द्वारा अपने कर्तव्यों के निर्वहन में लिए गए किसी निर्णय की जाँच के लिए उसे हटाने में सक्षम प्राधिकारी की पूर्व अनुमति चाहिए।",
   "अधिकारी को रिश्वत लेते समय मौक़े पर गिरफ़्तार करने के लिए ऐसी पूर्व अनुमति की ज़रूरत नहीं है।"],
  C3, 2,
  "All three are correct. The 2018 amendment made bribe-giving a specific offence (section 8), but exempted a person who was compelled to give the bribe and reported it to the police or an investigating agency within seven days. "
  "Section 17A requires prior approval before any inquiry or investigation into an offence relatable to a recommendation made or decision taken by a public servant in the discharge of official functions, to protect honest decision-making. Its proviso exempts cases in which the public servant is arrested on the spot for accepting or attempting to accept an undue advantage.",
  "तीनों कथन सही हैं। 2018 के संशोधन ने रिश्वत देने को एक विशिष्ट अपराध (धारा 8) बनाया, पर उस व्यक्ति को छूट दी जिसे रिश्वत देने के लिए मजबूर किया गया हो और जिसने सात दिनों के भीतर पुलिस या जाँच एजेंसी को सूचना दी हो। "
  "धारा 17A किसी लोक सेवक द्वारा आधिकारिक कार्यों के निर्वहन में की गई सिफ़ारिश या लिए गए निर्णय से जुड़े अपराध की किसी भी जाँच से पहले पूर्व अनुमति की अपेक्षा करती है, ताकि ईमानदार निर्णय-प्रक्रिया सुरक्षित रहे। इसका परंतुक उन मामलों को छूट देता है जिनमें लोक सेवक को अनुचित लाभ लेते या लेने का प्रयास करते समय मौक़े पर गिरफ़्तार किया जाए।",
  "Prevention of Corruption Act, 1988, as amended in 2018, sections 8 and 17A.",
  "laws-prevention-of-corruption-2018", craft="application")

S(SL, "medium", "A gang leaks the question paper of an examination conducted by the Staff Selection Commission. Consider the following statements in the light of the Public Examinations (Prevention of Unfair Means) Act, 2024:",
  "एक गिरोह कर्मचारी चयन आयोग द्वारा आयोजित एक परीक्षा का प्रश्न-पत्र लीक कर देता है। लोक परीक्षा (अनुचित साधन निवारण) अधिनियम, 2024 के आलोक में निम्नलिखित कथनों पर विचार कीजिए:",
  ["The offences under the Act are bailable and can be compounded with the consent of the examination authority.",
   "The Act does not cover examinations conducted by the Staff Selection Commission.",
   "The Act applies directly to the recruitment examinations of every State Public Service Commission."],
  ["अधिनियम के तहत अपराध ज़मानती हैं और परीक्षा प्राधिकारी की सहमति से उनका शमन हो सकता है।",
   "अधिनियम कर्मचारी चयन आयोग की परीक्षाओं को शामिल नहीं करता।",
   "अधिनियम हर राज्य लोक सेवा आयोग की भर्ती परीक्षाओं पर सीधे लागू होता है।"],
  C3, 3,
  "None is correct. Every offence under the Act is cognisable, non-bailable and non-compoundable, with imprisonment of three to five years for unfair means and five to ten years with heavy fines for organised paper leaks by a group or institution. "
  "The Act covers the public examination authorities listed in its Schedule -- the UPSC, the Staff Selection Commission, the Railway Recruitment Boards, IBPS and the National Testing Agency -- along with central ministries and departments. It does not apply directly to State Public Service Commissions; the States may adopt it or pass their own laws, as several have.",
  "कोई भी कथन सही नहीं है। अधिनियम के तहत हर अपराध संज्ञेय, अजमानती और अशमनीय है; अनुचित साधनों के लिए तीन से पाँच वर्ष, और किसी समूह या संस्था द्वारा संगठित प्रश्न-पत्र लीक के लिए पाँच से दस वर्ष का कारावास तथा भारी जुर्माना है। "
  "अधिनियम अपनी अनुसूची में सूचीबद्ध लोक परीक्षा प्राधिकारियों को शामिल करता है, जैसे संघ लोक सेवा आयोग, कर्मचारी चयन आयोग, रेलवे भर्ती बोर्ड, IBPS और राष्ट्रीय परीक्षा एजेंसी, साथ ही केंद्रीय मंत्रालय और विभाग। यह राज्य लोक सेवा आयोगों पर सीधे लागू नहीं होता; राज्य इसे अपना सकते हैं या अपने क़ानून बना सकते हैं, जैसा कई ने किया है।",
  "Public Examinations (Prevention of Unfair Means) Act, 2024.",
  "statute-public-examinations-act-2024", craft="application")

S(EL, "medium", "A sitting member of a State Legislative Assembly is convicted of an offence and sentenced to three years' imprisonment. He files an appeal the next week. Consider the following statements:",
  "राज्य विधानसभा के एक वर्तमान सदस्य को एक अपराध में दोषी ठहराकर तीन वर्ष के कारावास की सज़ा दी जाती है। वह अगले सप्ताह अपील दायर करता है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["He is disqualified from the date of his conviction, despite the appeal.",
   "Once released, he remains disqualified for a further six years.",
   "If the appellate court stays his conviction, the disqualification ceases to operate."],
  ["अपील के बावजूद वह दोषसिद्धि की तिथि से अयोग्य हो जाता है।",
   "रिहा होने के बाद वह छह वर्ष और अयोग्य रहता है।",
   "यदि अपीलीय न्यायालय उसकी दोषसिद्धि पर रोक लगा दे, तो अयोग्यता प्रभावी नहीं रहती।"],
  C3, 2,
  "All three are correct. Section 8(3) of the Representation of the People Act disqualifies a person sentenced to two years or more from the date of conviction and for six years after release. Section 8(4) used to let sitting legislators continue while an appeal was pending, but Lily Thomas (2013) struck it down, so the disqualification now takes effect at once. "
  "If an appellate court stays the conviction itself -- not merely the sentence -- the disqualification is suspended and the member's seat is restored, as the Supreme Court has held and as happened to a sitting Lok Sabha member in 2023.",
  "तीनों कथन सही हैं। जनप्रतिनिधित्व अधिनियम की धारा 8(3) दो वर्ष या अधिक की सज़ा पाने वाले व्यक्ति को दोषसिद्धि की तिथि से और रिहाई के बाद छह वर्ष तक अयोग्य करती है। धारा 8(4) पहले वर्तमान विधायकों को अपील लंबित रहने तक बने रहने देती थी, पर लिली थॉमस (2013) ने उसे रद्द कर दिया, इसलिए अयोग्यता अब तुरंत लागू होती है। "
  "यदि अपीलीय न्यायालय केवल सज़ा नहीं, बल्कि दोषसिद्धि पर ही रोक लगा दे, तो अयोग्यता निलंबित हो जाती है और सदस्य की सीट बहाल हो जाती है, जैसा सर्वोच्च न्यायालय ने कहा है और जैसा 2023 में लोकसभा के एक वर्तमान सदस्य के साथ हुआ।",
  f"{RPA}, section 8; {SC} -- Lily Thomas v. Union of India (2013).",
  "elections-rpa-disqualification-two-seats", craft="application")

S(BO, "hard", "A State government withdraws its general consent for the Central Bureau of Investigation to operate in the State. Consider the following statements:",
  "एक राज्य सरकार केंद्रीय अन्वेषण ब्यूरो (CBI) को राज्य में काम करने के लिए दी गई अपनी सामान्य सहमति वापस ले लेती है। निम्नलिखित कथनों पर विचार कीजिए:",
  ["The CBI now needs the State's consent case by case before it can take up a fresh investigation there.",
   "A High Court can still direct the CBI to investigate a case in the State.",
   "The Union Government can override the withdrawal by an executive order."],
  ["अब वहाँ कोई नई जाँच शुरू करने से पहले CBI को हर मामले में राज्य की सहमति चाहिए।",
   "उच्च न्यायालय फिर भी CBI को राज्य के किसी मामले की जाँच का निर्देश दे सकता है।",
   "केंद्र सरकार कार्यकारी आदेश से इस वापसी को निष्प्रभावी कर सकती है।"],
  C3, 1,
  "Statements 1 and 2 are correct. The CBI draws its powers from the Delhi Special Police Establishment Act, 1946, and section 6 lets it operate in a State only with that State's consent, general or case-specific; once general consent is withdrawn, it must seek consent for each new case. "
  "The constitutional courts are not bound by this: in State of West Bengal v. Committee for Protection of Democratic Rights (2010), the Supreme Court held that the Supreme Court and the High Courts can direct the CBI to investigate without the State's consent. "
  "Statement 3 is wrong: the consent requirement is statutory and protects the States' power over policing, so an executive order of the Union cannot override it.",
  "कथन 1 और 2 सही हैं। CBI अपनी शक्तियाँ दिल्ली विशेष पुलिस स्थापना अधिनियम, 1946 से पाती है, और धारा 6 उसे किसी राज्य में केवल उस राज्य की सामान्य या मामले-विशेष सहमति से काम करने देती है; सामान्य सहमति वापस होने पर उसे हर नए मामले के लिए सहमति लेनी होती है। "
  "संवैधानिक न्यायालय इससे बँधे नहीं हैं: पश्चिम बंगाल राज्य बनाम लोकतांत्रिक अधिकार संरक्षण समिति (2010) में सर्वोच्च न्यायालय ने कहा कि सर्वोच्च न्यायालय और उच्च न्यायालय राज्य की सहमति के बिना CBI को जाँच का निर्देश दे सकते हैं। "
  "कथन 3 गलत है: सहमति की शर्त वैधानिक है और पुलिस पर राज्यों की शक्ति की रक्षा करती है, इसलिए केंद्र का कार्यकारी आदेश इसे निष्प्रभावी नहीं कर सकता।",
  f"Delhi Special Police Establishment Act, 1946, section 6; {SC} -- State of West Bengal v. Committee for Protection of Democratic Rights (2010).",
  "bodies-cbi-origin-consent-director", craft="application")

S(SL, "medium", "Consider the following cases in the light of the Digital Personal Data Protection Act, 2023:",
  "डिजिटल व्यक्तिगत डेटा संरक्षण अधिनियम, 2023 के आलोक में निम्नलिखित मामलों पर विचार कीजिए:",
  ["A company in Singapore processes the personal data of customers in India in order to sell them products.",
   "A hospital in India collects patients' details on paper forms and later scans them into a database.",
   "A firm in Dubai processes the personal data of Dubai residents, with no link to India."],
  ["सिंगापुर की एक कंपनी भारत के ग्राहकों को उत्पाद बेचने के लिए उनके व्यक्तिगत डेटा का प्रसंस्करण करती है।",
   "भारत का एक अस्पताल रोगियों का विवरण काग़ज़ी फ़ॉर्मों पर लेता है और बाद में उसे स्कैन कर डेटाबेस में डालता है।",
   "दुबई की एक फ़र्म दुबई के निवासियों के व्यक्तिगत डेटा का प्रसंस्करण करती है, जिसका भारत से कोई संबंध नहीं है।"],
  None, 0,
  "The Act applies in cases 1 and 2. Under section 3 it covers digital personal data processed within India -- including data collected in non-digital form and digitised later, as in the hospital's case -- and processing outside India if it is connected with offering goods or services to Data Principals in India, as with the Singapore company. "
  "Case 3 has no connection with India, so the Act does not reach it. Breaches are adjudicated by the Data Protection Board of India.",
  "अधिनियम मामले 1 और 2 पर लागू होता है। धारा 3 के तहत यह भारत के भीतर संसाधित डिजिटल व्यक्तिगत डेटा को शामिल करता है, जिसमें ग़ैर-डिजिटल रूप में एकत्र और बाद में डिजिटल बनाया गया डेटा भी है, जैसा अस्पताल के मामले में; और भारत के बाहर उस प्रसंस्करण को भी, जो भारत के डेटा प्रिंसिपलों को वस्तुएँ या सेवाएँ देने से जुड़ा हो, जैसा सिंगापुर की कंपनी के साथ। "
  "मामले 3 का भारत से कोई संबंध नहीं है, इसलिए अधिनियम उस तक नहीं पहुँचता। उल्लंघनों पर निर्णय भारतीय डेटा संरक्षण बोर्ड करता है।",
  "Digital Personal Data Protection Act, 2023, section 3.",
  "statute-dpdp-act-2023-scope", opts=["1 and 2 only", "2 only", "1 and 3 only", "1, 2 and 3"],
  opts_hi=["केवल 1 और 2", "केवल 2", "केवल 1 और 3", "1, 2 और 3"],
  closing="To which of the above does the Act apply?", closing_hi="उपर्युक्त में से किस/किन पर अधिनियम लागू होता है?", craft="application")

# ================================================================ TAGS for the 80 kept rows (Test 21's 3 are tagged already)
TAGS = {
 "bodies-nhrc-recommendatory": "linkage", "bodies-cag-appointment-service-conditions": "precision", "bodies-law-commission-nonbinding": "linkage",
 "bodies-committees-subjects-pairs": "recall", "bodies-articles-pairs": "recall", "bodies-cvc-santhanam": "recall",
 "bodies-lokpal-selection-committee": "precision", "bodies-constitutional-ncst": "precision", "polity-constitutional-statutory-nonstatutory-bodies": "precision",
 "bodies-ssc-niti-easy": "recall", "bodies-national-commissions-338-338a-338b": "precision", "bodies-special-officer-linguistic-minorities": "precision",
 "bodies-tribunals-323a-323b": "precision", "polity-finance-commission-art280": "precision", "bodies-advocate-general": "recall",
 "bodies-cvc-status-removal-report": "precision", "bodies-joint-state-psc": "precision", "bodies-law-commission": "recall",
 "bodies-lokpal-structure-pm": "precision", "bodies-nhrc-status-chair-limitation": "precision", "bodies-state-psc-removal-eligibility": "precision",
 "bodies-upsc-functions-art320": "precision", "polity-cag-independence-reports": "precision", "elections-nota-pucl-2013": "precision",
 "elections-deregistration-recognition": "linkage", "elections-president-vp-eci-mandate": "linkage", "elections-part-xv-articles-pairs": "recall",
 "elections-reforms-years-pairs": "recall", "elections-corrupt-practice-vs-offence": "precision", "polity-election-commission-vs-state-ec": "recall",
 "elections-cec-appointment-act-2023": "precision", "elections-expenditure-ceiling-account": "precision", "elections-vvpat-judgments": "precision",
 "elections-delimitation-commission": "precision", "elections-eci-multimember-majority": "precision", "elections-overseas-electors-proxy": "precision",
 "verdicts-demonetisation-2023": "linkage", "verdicts-arnesh-kumar-arrest": "linkage", "verdicts-recent-judgments-pairs": "recall",
 "verdicts-kihoto-hollohan-tenth-schedule": "recall", "verdicts-shirur-mutt-essential-practices": "recall", "verdicts-shah-bano-sarla-mudgal-easy": "recall",
 "verdicts-2024-poa-mada-sita-soren-amu": "precision", "verdicts-anuradha-bhasin-internet": "precision", "verdicts-nalsa-vineeta-sabarimala": "precision",
 "verdicts-2023-2024-bonds-subclassification-370": "recall", "verdicts-basic-structure-sequence": "recall", "verdicts-criminalisation-of-politics": "precision",
 "judiciary-court-of-record-129": "linkage", "judiciary-articles-124-214-226-143-pairs": "recall", "judiciary-original-advisory-jurisdiction": "precision",
 "judiciary-collegium-njac": "precision", "judiciary-high-courts-age-ut-common": "precision", "judiciary-supreme-court-strength-removal": "precision",
 "laws-pmla-bail-twin-conditions": "linkage", "statute-rti-section-24-22": "linkage", "laws-mhca-suicide-presumption": "precision",
 "laws-places-of-worship-ayodhya-exemption": "linkage", "laws-posh-domestic-workers": "precision", "statute-pocso-gender-neutral-age": "precision",
 "laws-social-legislation-years-pairs": "recall", "statute-recent-laws-replaced-pairs": "recall", "laws-acts-bodies-pairs": "recall",
 "statute-acts-2023-subject-pairs": "recall", "laws-code-on-wages-subsumed": "recall", "statute-dpdp-penalty-schedule": "recall",
 "laws-dowry-senior-citizen-easy": "recall", "laws-bns-lynching-organised-crime-snatching": "precision", "laws-labour-codes": "recall",
 "laws-uapa-2019-individuals": "precision", "statute-bns-bnss-new-features": "precision", "statute-telecommunications-act-2023": "precision",
 "laws-disaster-management-authorities": "recall", "laws-domestic-violence-2005": "precision", "laws-mental-healthcare-rights": "precision",
 "laws-mtp-amendment-2021": "precision", "laws-rte-detention-minority-screening": "precision", "laws-transgender-persons-2019": "precision",
 "statute-new-criminal-laws-replacements": "recall", "statute-rti-48-hours-2019-amendment": "precision"}

# pair 3 of verdicts-recent-judgments-pairs, without the Article number (the pair stays correct)
PAIR_FIX = ("Set aside the returning officer's result and declared the other candidate Mayor of Chandigarh",
            "निर्वाचन अधिकारी का घोषित परिणाम रद्द कर दूसरे उम्मीदवार को चंडीगढ़ का महापौर घोषित किया")

if __name__ == "__main__":
    write_updates("upg_l2_t03_polity.sql", statuses=("draft", "published"), tags=TAGS)
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "upg_l2_t03_polity.sql")
    sql = open(path, encoding="utf-8").read()
    q = lambda v: "'" + v.replace("'", "''") + "'"
    fix = ("update public.questions set question_data = jsonb_set(jsonb_set(question_data, '{list_2,2}', to_jsonb(" + q(PAIR_FIX[0])
           + "::text)), '{list_2_hi,2}', to_jsonb(" + q(PAIR_FIX[1]) + "::text)), updated_at = now() where exam_category = 'upsc'"
           + " and concept_group_id = 'verdicts-recent-judgments-pairs' and question_data->'list_2'->>2 like '%Article 142%' returning concept_group_id;")
    assert sql.endswith("commit;" + chr(10))
    open(path, "w", encoding="utf-8").write(sql[:-len("commit;" + chr(10))] + fix + chr(10) + "commit;" + chr(10))
