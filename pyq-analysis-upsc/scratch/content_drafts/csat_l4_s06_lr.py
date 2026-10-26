# -*- coding: utf-8 -*-
"""CSAT Level 4 · Simulator 6 -- Logical Reasoning (20 items: 17 in the Reasoning slots, 3 in the data-sufficiency block).

Layout C, the 2026 shape: the heavier Reasoning section. Exam-level mix (1 easy / 10 medium / 9 hard), with none of
the shapes of Levels 1-3 or Simulators 1-5: the assumptions behind a fire notice, two effects of a rainy week, a
principle behind an intensive-care decision, the role of an objection in an argument, an argument's main conclusion;
five books on a shelf, five friends arriving at a party, tasks that must follow others, five meetings in March 2027;
cousins of a child whose parents are only children, a mother's sister's son; the Roman numerals hidden in a word, a
code of digit sums; a chain of three moves, a turn made facing a school; the lines through the inside of a cube; singers who are
not violinists; and in the data-sufficiency block a pen that follows from a pencil, a room where everyone shook three
hands, and a boy who is tallest in his row. Arrangement, relation, code, direction and syllogism keys are found by
checking every case."""
from itertools import combinations, permutations, product
import datetime as dt
import csat_common as c
from csat_common import N, T, S2, DS, LR

def _ds(s1, s2, both):
    alone = (len(set(s1)) == 1, len(set(s2)) == 1)
    return "b" if all(alone) else "a" if any(alone) else "c" if len(set(both)) == 1 else "d"

# 1 -- the assumptions behind a fire notice
S2(LR, "Statement-Conclusion/Assumption", "medium",
   "Statement: A notice beside the lifts of an office building reads: 'In case of fire, use the stairs. Do not use the lifts.'\n\nWhich of the following assumptions is/are implicit in the statement?",
   "कथन: एक कार्यालय भवन की लिफ़्टों के पास एक सूचना लिखी है: 'आग लगने पर सीढ़ियों का प्रयोग करें। लिफ़्टों का प्रयोग न करें।'\n\nनिम्नलिखित में से कौन-सी पूर्वधारणा/एँ कथन में निहित है/हैं?",
   ["A lift may become unsafe to use during a fire.",
    "Everyone in the building is able to use the stairs without help."],
   ["आग के दौरान लिफ़्ट का प्रयोग असुरक्षित हो सकता है।",
    "भवन का हर व्यक्ति बिना सहायता के सीढ़ियों का प्रयोग कर सकता है।"],
   0,
   "Only I is implicit. Telling people to avoid the lifts in a fire makes sense only if a lift may be dangerous then -- it may stop between floors or open onto a burning floor. "
   "II is not assumed: the notice gives the general rule, and it remains sensible even if some people will need help on the stairs; it says nothing about whether everyone can manage alone.",
   "केवल I निहित है। आग में लोगों से लिफ़्ट से बचने को कहना तभी समझ में आता है जब तब लिफ़्ट ख़तरनाक हो सकती हो -- वह मंज़िलों के बीच रुक सकती है या जलती मंज़िल पर खुल सकती है। "
   "II पूर्वधारणा नहीं है: सूचना सामान्य नियम देती है, और वह तब भी समझदारी भरी है जब कुछ लोगों को सीढ़ियों पर सहायता चाहिए; वह इस बारे में कुछ नहीं कहती कि हर कोई अकेले उतर सकता है या नहीं।",
   "lr-sc-the-assumptions-behind-a-fire-notice", roman=True)

# 2 -- two effects of a rainy week
T(LR, "Statement-Conclusion/Assumption", "medium",
  "Consider the two statements:\nI. Sales of umbrellas in the city rose sharply last week.\nII. Attendance at the city's outdoor cricket matches fell sharply last week.\n\nWhich one of the following best describes the relationship between them?",
  "दो कथनों पर विचार कीजिए:\nI. पिछले सप्ताह शहर में छातों की बिक्री तेज़ी से बढ़ी।\nII. पिछले सप्ताह शहर के खुले मैदान में होने वाले क्रिकेट मैचों में दर्शक तेज़ी से घटे।\n\nनिम्नलिखित में से कौन-सा उनके बीच के संबंध को सबसे अच्छी तरह बताता है?",
  ["Both statements are effects of some common cause",
   "Statement I is the cause and Statement II is its effect",
   "Statement I is the effect and Statement II is its cause",
   "Both statements are independent causes"],
  ["दोनों कथन एक ही कारण के प्रभाव हैं",
   "कथन I कारण है और कथन II उसका प्रभाव",
   "कथन I प्रभाव है और कथन II उसका कारण",
   "दोनों कथन स्वतंत्र कारण हैं"],
  0,
  "Neither event causes the other: people buying umbrellas does not keep them from cricket, and empty stands do not sell umbrellas. Both are just what a spell of heavy rain would bring about in the same week, so they are effects of a common cause. "
  "Reading either as the cause of the other gets the connection wrong; and they are not causes of anything stated here.",
  "कोई भी घटना दूसरी का कारण नहीं: छाते ख़रीदना लोगों को क्रिकेट से दूर नहीं रखता, और ख़ाली दर्शक-दीर्घाएँ छाते नहीं बेचतीं। दोनों ठीक वही हैं जो उसी सप्ताह भारी वर्षा का एक दौर लाता, इसलिए वे एक ही कारण के प्रभाव हैं। "
  "किसी को भी दूसरे का कारण पढ़ना संबंध को ग़लत समझना है; और वे यहाँ बताई गई किसी बात के कारण नहीं हैं।",
  "lr-sc-two-effects-of-a-rainy-week", pos=1)

# 3 -- a principle behind an intensive-care decision
T(LR, "Statement-Conclusion/Assumption", "medium",
  "A hospital has one bed left in its intensive care unit and two patients who need it. It gives the bed not to the patient who arrived first, but to the one who is far more likely to survive with intensive care. Which one of the following principles, if accepted, best justifies the decision?",
  "एक अस्पताल की गहन चिकित्सा इकाई में एक बिस्तर बचा है और दो रोगियों को उसकी आवश्यकता है। वह बिस्तर पहले आए रोगी को नहीं, बल्कि उसे देता है जिसके गहन चिकित्सा से बचने की संभावना कहीं अधिक है। निम्नलिखित में से कौन-सा सिद्धांत, यदि स्वीकार किया जाए, इस निर्णय को सबसे अच्छी तरह उचित ठहराता है?",
  ["Scarce care should go where it is likely to do the most good.",
   "Patients should always be treated in the order in which they arrive.",
   "A hospital should prefer the patient who is able to pay the most.",
   "When two patients need one bed, the choice should be left to chance."],
  ["दुर्लभ देखभाल वहाँ जाए जहाँ उससे सबसे अधिक भलाई की संभावना हो।",
   "रोगियों का उपचार हमेशा उनके आने के क्रम में होना चाहिए।",
   "अस्पताल को उस रोगी को वरीयता देनी चाहिए जो सबसे अधिक भुगतान कर सके।",
   "जब दो रोगियों को एक बिस्तर चाहिए, तो चुनाव संयोग पर छोड़ा जाना चाहिए।"],
  0,
  "The hospital chose the patient whom the bed is more likely to save. The principle that scarce care should go where it does the most good is exactly what makes that the right choice. "
  "'First come, first served' would have given the bed to the other patient; ability to pay plays no part in the decision described; and leaving it to chance would not favour the likelier survivor.",
  "अस्पताल ने वह रोगी चुना जिसे बिस्तर से बचने की अधिक संभावना है। यह सिद्धांत कि दुर्लभ देखभाल वहाँ जाए जहाँ वह सबसे अधिक भलाई करे, ठीक वही है जो इसे सही चुनाव बनाता है। "
  "'पहले आओ, पहले पाओ' बिस्तर दूसरे रोगी को देता; वर्णित निर्णय में भुगतान की क्षमता की कोई भूमिका नहीं; और संयोग पर छोड़ना अधिक संभावित जीवित रहने वाले को वरीयता नहीं देता।",
  "lr-sc-a-principle-behind-an-intensive-care-decision", pos=3)

# 4 -- the role of an objection in an argument
T(LR, "Statement-Conclusion/Assumption", "hard",
  "'Cities should charge drivers a fee for entering the centre at busy hours. Such fees have cut traffic in other cities. Some say the fee would hurt poorer drivers most, but the money it raises can pay for better buses, which poorer people use most.' Which one of the following best describes the role played in the argument by the claim that the fee would hurt poorer drivers most?",
  "'शहरों को व्यस्त समय में केंद्र में प्रवेश करने वाले चालकों से शुल्क लेना चाहिए। ऐसे शुल्कों ने दूसरे शहरों में यातायात घटाया है। कुछ कहते हैं कि शुल्क सबसे अधिक निर्धन चालकों को चोट पहुँचाएगा, पर उससे मिलने वाला पैसा बेहतर बसों पर लगाया जा सकता है, जिनका उपयोग निर्धन लोग सबसे अधिक करते हैं।' निम्नलिखित में से कौन-सा तर्क में इस दावे की भूमिका का सबसे अच्छा वर्णन करता है कि शुल्क सबसे अधिक निर्धन चालकों को चोट पहुँचाएगा?",
  ["It is the main conclusion that the argument sets out to establish.",
   "It is a piece of evidence offered in support of charging the fee.",
   "It is an objection that the argument goes on to answer.",
   "It is an assumption on which the argument's conclusion depends."],
  ["यह वह मुख्य निष्कर्ष है जिसे तर्क स्थापित करना चाहता है।",
   "यह शुल्क लेने के समर्थन में दिया गया एक प्रमाण है।",
   "यह एक आपत्ति है जिसका उत्तर तर्क आगे देता है।",
   "यह एक पूर्वधारणा है जिस पर तर्क का निष्कर्ष निर्भर है।"],
  2,
  "The argument concludes that cities should charge the fee, supports this with the fall in traffic elsewhere, and then raises a point against it -- 'some say' it would hurt poorer drivers -- only to answer it with the buses the money can buy. "
  "The claim is not the conclusion, which is that the fee should be charged; it counts against the fee, so it is not evidence for it; and the argument does not depend on it being true -- it tries to meet it.",
  "तर्क का निष्कर्ष है कि शहरों को शुल्क लेना चाहिए, वह इसका समर्थन दूसरी जगहों पर यातायात घटने से करता है, और फिर उसके विरुद्ध एक बात उठाता है -- 'कुछ कहते हैं' कि वह निर्धन चालकों को चोट पहुँचाएगा -- केवल उसका उत्तर उन बसों से देने के लिए जो पैसे से ख़रीदी जा सकती हैं। "
  "यह दावा निष्कर्ष नहीं है, जो यह है कि शुल्क लिया जाए; वह शुल्क के विरुद्ध जाता है, इसलिए उसका प्रमाण नहीं; और तर्क उसके सत्य होने पर निर्भर नहीं -- वह उससे निपटने का प्रयास करता है।",
  "lr-sc-the-role-of-an-objection-in-an-argument", pos=2)

# 5 -- an argument's main conclusion
T(LR, "Statement-Conclusion/Assumption", "hard",
  "'Children who read for pleasure do better in every subject, not only in languages. Yet many schools set aside reading time only for their weakest readers, as a remedy. A daily period of free reading for every child would therefore do more for a school's results than extra coaching for a few.' Which one of the following best expresses the main conclusion of the argument?",
  "'जो बच्चे आनंद के लिए पढ़ते हैं वे केवल भाषाओं में नहीं, हर विषय में बेहतर करते हैं। फिर भी कई विद्यालय पढ़ने का समय केवल अपने सबसे कमज़ोर पाठकों के लिए, उपचार के रूप में, रखते हैं। अतः हर बच्चे के लिए मुक्त पठन का एक दैनिक कालांश कुछ बच्चों की अतिरिक्त कोचिंग की तुलना में विद्यालय के परिणामों के लिए अधिक करेगा।' निम्नलिखित में से कौन-सा तर्क के मुख्य निष्कर्ष को सबसे अच्छी तरह व्यक्त करता है?",
  ["Children who read for pleasure do better in every subject, not only in languages.",
   "Many schools set aside reading time only for their weakest readers.",
   "Extra coaching for a few children does nothing at all for a school's results.",
   "Free reading every day for all would help results more than coaching a few."],
  ["जो बच्चे आनंद के लिए पढ़ते हैं वे केवल भाषाओं में नहीं, हर विषय में बेहतर करते हैं।",
   "कई विद्यालय पढ़ने का समय केवल अपने सबसे कमज़ोर पाठकों के लिए रखते हैं।",
   "कुछ बच्चों की अतिरिक्त कोचिंग विद्यालय के परिणामों के लिए कुछ भी नहीं करती।",
   "सबके लिए रोज़ मुक्त पठन, कुछ की कोचिंग से अधिक परिणाम सुधारेगा।"],
  3,
  "The word 'therefore' marks the conclusion: a daily free-reading period for every child would do more for results than extra coaching for a few. The first two sentences are the reasons offered for it. "
  "The benefit of reading for pleasure and the schools' current practice are premises, not the conclusion; and the argument says free reading would do more than coaching, not that coaching does nothing.",
  "'अतः' शब्द निष्कर्ष को चिह्नित करता है: हर बच्चे के लिए मुक्त पठन का दैनिक कालांश कुछ की अतिरिक्त कोचिंग से अधिक परिणामों के लिए करेगा। पहले दो वाक्य उसके लिए दिए गए कारण हैं। "
  "आनंद के लिए पढ़ने का लाभ और विद्यालयों का वर्तमान व्यवहार आधार-वाक्य हैं, निष्कर्ष नहीं; और तर्क कहता है कि मुक्त पठन कोचिंग से अधिक करेगा, यह नहीं कि कोचिंग कुछ नहीं करती।",
  "lr-sc-an-argument-s-main-conclusion", pos=1)

# 6 -- five books on a shelf
def _sa6():
    subs, cols = ["History", "Physics", "Poetry", "Law", "Music"], ["red", "blue", "green", "white", "black"]
    sols = []
    for sp in permutations(subs):
        S = {s: i + 1 for i, s in enumerate(sp)}
        for cp in permutations(cols):
            C = {x: i + 1 for i, x in enumerate(cp)}
            if (S["Poetry"] == 3 and C["red"] == 1 and abs(S["History"] - S["Poetry"]) == 1 and S["Law"] == C["green"]
                    and C["white"] == C["green"] + 1 and S["Physics"] == C["blue"]):
                sols.append((S, C))
    assert len(sols) == 1
    S, C = sols[0]
    facts = [S["History"] == C["black"], S["Music"] == C["green"], S["Physics"] == 1, S["Law"] == C["white"]]
    assert facts == [True, False, False, False]
    return "The History book is black."
T(LR, "Seating Arrangement", "hard",
  "Five books stand in a row on a shelf, one each on History, Physics, Poetry, Law and Music, each with a cover of a different colour: red, blue, green, white or black. The Poetry book is in the middle. The red book is at the left end. The History book is next to the Poetry book. The Law book is green, and the white book is immediately to the right of the green one. The blue book is the Physics book. Which one of the following is correct?",
  "एक शेल्फ़ पर पाँच पुस्तकें एक पंक्ति में खड़ी हैं, इतिहास, भौतिकी, कविता, विधि और संगीत पर एक-एक, हर एक का आवरण अलग रंग का: लाल, नीला, हरा, सफ़ेद या काला। कविता की पुस्तक बीच में है। लाल पुस्तक बाएँ छोर पर है। इतिहास की पुस्तक कविता की पुस्तक के बगल में है। विधि की पुस्तक हरी है, और सफ़ेद पुस्तक हरी पुस्तक के ठीक दाईं ओर है। नीली पुस्तक भौतिकी की पुस्तक है। निम्नलिखित में से कौन-सा सही है?",
  ["The History book is black.", "The Music book is green.", "The Physics book is at the left end.", "The white book is the Law book."],
  ["इतिहास की पुस्तक काली है।", "संगीत की पुस्तक हरी है।", "भौतिकी की पुस्तक बाएँ छोर पर है।", "सफ़ेद पुस्तक विधि की पुस्तक है।"],
  0,
  "Poetry is 3rd and red is 1st. Law is green with white just to its right, so green and white are a neighbouring pair in places 2-3, 3-4 or 4-5 -- but green cannot be 3rd, which is Poetry's place and not Law's; and if green were 4th, History (next to Poetry) would be 2nd and blue Physics would have to be 1st, which is red. So Law is green in place 2 and Poetry is white in place 3. History then takes place 4, Physics, being blue and not red, takes place 5, and Music is the red book in place 1. The last colour, black, goes to History. "
  "Music is red, not green; Physics is at the right end, not the left; and the white book is Poetry, not Law.",
  "कविता तीसरी है और लाल पहली। विधि हरी है और सफ़ेद ठीक उसके दाईं ओर, इसलिए हरी और सफ़ेद स्थान 2-3, 3-4 या 4-5 में पड़ोसी जोड़ा हैं -- पर हरी तीसरी नहीं हो सकती, जो कविता का स्थान है, विधि का नहीं; और यदि हरी चौथी होती, तो इतिहास (कविता के बगल में) दूसरी होती और नीली भौतिकी को पहली होना पड़ता, जो लाल है। अतः विधि स्थान 2 में हरी है और कविता स्थान 3 में सफ़ेद। तब इतिहास स्थान 4 लेती है, भौतिकी, नीली होने और लाल न होने के कारण, स्थान 5, और संगीत स्थान 1 की लाल पुस्तक है। अंतिम रंग, काला, इतिहास को जाता है। "
  "संगीत लाल है, हरी नहीं; भौतिकी दाएँ छोर पर है, बाएँ नहीं; और सफ़ेद पुस्तक कविता है, विधि नहीं।",
  "lr-sa-five-books-on-a-shelf", pos=3, check=_sa6)

# 7 -- five friends arriving at a party
def _sa7():
    names = ["Asha", "Bilal", "Chitra", "Dinesh", "Esha"]
    sols = []
    for p in permutations(range(0, 70, 10), 5):
        w = dict(zip(names, p))
        if w["Chitra"] == w["Bilal"] + 20 and 2 * w["Esha"] == w["Asha"] + w["Bilal"] and w["Dinesh"] == w["Esha"] - 10:
            sols.append(w)
    assert len(sols) == 1
    w = sols[0]
    facts = [w["Esha"] == 20, w["Asha"] == 10, w["Bilal"] == 30, w["Dinesh"] == 20]
    assert facts == [True, False, False, False]
    return "Esha arrived at 6:20."
T(LR, "Seating Arrangement", "hard",
  "Five friends -- Asha, Bilal, Chitra, Dinesh and Esha -- arrived at a party at different times, each at one of 6:00, 6:10, 6:20, 6:30, 6:40, 6:50 and 7:00. Chitra arrived 20 minutes after Bilal. Esha arrived exactly midway in time between Asha and Bilal. Dinesh arrived 10 minutes before Esha. Which one of the following is correct?",
  "पाँच मित्र -- आशा, बिलाल, चित्रा, दिनेश और ईशा -- एक दावत में अलग-अलग समय पर पहुँचे, हर एक 6:00, 6:10, 6:20, 6:30, 6:40, 6:50 और 7:00 में से किसी एक समय पर। चित्रा, बिलाल के 20 मिनट बाद पहुँची। ईशा समय में आशा और बिलाल के ठीक बीच पहुँची। दिनेश, ईशा से 10 मिनट पहले पहुँचा। निम्नलिखित में से कौन-सा सही है?",
  ["Asha arrived at 6:10.", "Esha arrived at 6:20.", "Bilal arrived at 6:30.", "Dinesh arrived at 6:20."],
  ["आशा 6:10 पर पहुँची।", "ईशा 6:20 पर पहुँची।", "बिलाल 6:30 पर पहुँचा।", "दिनेश 6:20 पर पहुँचा।"],
  1,
  "Chitra came 20 minutes after Bilal, so Bilal came no later than 6:40. Esha came midway between Asha and Bilal, and Dinesh 10 minutes before Esha. If Asha and Bilal were only 20 minutes apart, Dinesh would arrive at the same time as the earlier of them, so they must be 40 or 60 minutes apart. If Bilal came before Asha, Chitra, 20 minutes after Bilal, would arrive at the same time as Esha or as Dinesh. So Asha came first, 40 minutes before Bilal -- 60 minutes would put Bilal at 7:00, with no time left for Chitra: Asha 6:00, Dinesh 6:10, Esha 6:20, Bilal 6:40 and Chitra 7:00. "
  "So Esha arrived at 6:20. Asha came at 6:00, not 6:10; Bilal at 6:40, not 6:30; and Dinesh at 6:10, not 6:20.",
  "चित्रा, बिलाल के 20 मिनट बाद आई, इसलिए बिलाल 6:40 के बाद नहीं आया। ईशा, आशा और बिलाल के ठीक बीच आई, और दिनेश, ईशा से 10 मिनट पहले। यदि आशा और बिलाल केवल 20 मिनट दूर होते, तो दिनेश उनमें से पहले वाले के ही समय पर पहुँचता, इसलिए वे 40 या 60 मिनट दूर होने चाहिए। यदि बिलाल, आशा से पहले आता, तो बिलाल के 20 मिनट बाद आने वाली चित्रा, ईशा या दिनेश के ही समय पर पहुँचती। अतः आशा पहले आई, बिलाल से 40 मिनट पहले -- 60 मिनट बिलाल को 7:00 पर रख देते, चित्रा के लिए कोई समय न छोड़ते: आशा 6:00, दिनेश 6:10, ईशा 6:20, बिलाल 6:40 और चित्रा 7:00। "
  "अतः ईशा 6:20 पर पहुँची। आशा 6:00 पर आई, 6:10 पर नहीं; बिलाल 6:40 पर, 6:30 पर नहीं; और दिनेश 6:10 पर, 6:20 पर नहीं।",
  "lr-sa-five-friends-arriving-at-a-party", pos=1, check=_sa7)

# 8 -- tasks that must follow others
def _sa8():
    rules = [("P", "Q"), ("Q", "R"), ("R", "T"), ("S", "T"), ("T", "U")]
    ok = [o for o in permutations("PQRSTU") if all(o.index(a) < o.index(b) for a, b in rules)]
    claims = {"T is done fifth.": lambda o: o[4] == "T", "S is done first.": lambda o: o[0] == "S",
              "R is done fourth.": lambda o: o[3] == "R", "P is done first.": lambda o: o[0] == "P"}
    must = [k for k, f in claims.items() if all(f(o) for o in ok)]
    assert len(ok) == 4 and must == ["T is done fifth."]
    return must[0]
T(LR, "Seating Arrangement", "hard",
  "Six tasks, P, Q, R, S, T and U, are done one at a time. Q cannot be started until P is finished, and R cannot be started until Q is finished. T needs both R and S to be finished first, and U needs T to be finished first. Which one of the following must be true?",
  "छह काम, P, Q, R, S, T और U, एक-एक करके किए जाते हैं। Q तब तक शुरू नहीं हो सकता जब तक P पूरा न हो, और R तब तक शुरू नहीं हो सकता जब तक Q पूरा न हो। T के लिए पहले R और S दोनों का पूरा होना आवश्यक है, और U के लिए पहले T का पूरा होना। निम्नलिखित में से कौन-सा अवश्य सत्य है?",
  ["S is done first.", "R is done fourth.", "T is done fifth.", "P is done first."],
  ["S सबसे पहले किया जाता है।", "R चौथा किया जाता है।", "T पाँचवाँ किया जाता है।", "P सबसे पहले किया जाता है।"],
  2,
  "P, Q and R must come in that order, and T needs R and S, so all four of P, Q, R and S come before T; U comes after T. That fixes T in 5th place and U in 6th. S can go anywhere before T -- first, second, third or fourth -- which gives four possible orders. "
  "So S need not be first, R is fourth only when S comes earlier, and P is first only when S is not.",
  "P, Q और R उसी क्रम में आने चाहिए, और T को R और S चाहिए, इसलिए P, Q, R और S चारों T से पहले आते हैं; U, T के बाद आता है। इससे T पाँचवें और U छठे स्थान पर तय हो जाते हैं। S, T से पहले कहीं भी जा सकता है -- पहला, दूसरा, तीसरा या चौथा -- जिससे चार संभव क्रम बनते हैं। "
  "अतः S का पहला होना आवश्यक नहीं, R चौथा तभी है जब S पहले आए, और P पहला तभी है जब S न हो।",
  "lr-sa-tasks-that-must-follow-others", pos=2, check=_sa8)

# 9 -- five meetings in March 2027
def _sa9():
    wd = lambda d: dt.date(2027, 3, d).weekday()            # 0 = Monday
    assert wd(1) == 0
    sols = []
    for P in range(1, 32):
        Q, R = P + 7, P + 8
        for S in range(1, 32):
            for Tm in range(1, 32):
                if (wd(P) == 2 and P <= 7 and wd(S) == 4 and S + 7 > 31 and wd(Tm) == 0 and 0 < Tm - R < 7
                        and len({P, Q, R, S, Tm}) == 5):
                    sols.append((P, Q, R, S, Tm))
    assert sols == [(3, 10, 11, 26, 15)]
    return "T's meeting is on 15 March."
T(LR, "Seating Arrangement", "hard",
  "Five meetings, P, Q, R, S and T, are held on five different dates in March 2027; 1 March 2027 is a Monday. P is on the first Wednesday of the month, and Q exactly one week after P. R is on the day after Q. S is on the last Friday of the month. T is on a Monday, less than a week after R. Which one of the following is correct?",
  "पाँच बैठकें, P, Q, R, S और T, मार्च 2027 की पाँच अलग-अलग तारीख़ों पर होती हैं; 1 मार्च 2027 सोमवार है। P महीने के पहले बुधवार को है, और Q, P के ठीक एक सप्ताह बाद। R, Q के अगले दिन है। S महीने के अंतिम शुक्रवार को है। T एक सोमवार को है, R के एक सप्ताह से कम बाद। निम्नलिखित में से कौन-सा सही है?",
  ["T's meeting is on 15 March.", "S's meeting is on 19 March.", "R's meeting is on 10 March.", "P's meeting is on 6 March."],
  ["T की बैठक 15 मार्च को है।", "S की बैठक 19 मार्च को है।", "R की बैठक 10 मार्च को है।", "P की बैठक 6 मार्च को है।"],
  0,
  "With 1 March a Monday, the Wednesdays are the 3rd, 10th, 17th, 24th and 31st, the Fridays the 5th, 12th, 19th and 26th, and the Mondays the 1st, 8th, 15th, 22nd and 29th. So P is on 3 March, Q on 10 March, R on 11 March and S on 26 March. The only Monday less than a week after the 11th is the 15th. "
  "19 March is a Friday but not the last; 10 March is Q's date, not R's; and 6 March is a Saturday, not P's Wednesday.",
  "1 मार्च सोमवार होने पर बुधवार 3, 10, 17, 24 और 31 तारीख़ हैं, शुक्रवार 5, 12, 19 और 26, और सोमवार 1, 8, 15, 22 और 29। अतः P, 3 मार्च को, Q, 10 मार्च को, R, 11 मार्च को और S, 26 मार्च को है। 11 तारीख़ के एक सप्ताह से कम बाद का एकमात्र सोमवार 15 तारीख़ है। "
  "19 मार्च शुक्रवार है पर अंतिम नहीं; 10 मार्च Q की तारीख़ है, R की नहीं; और 6 मार्च शनिवार है, P का बुधवार नहीं।",
  "lr-sa-five-meetings-in-march-2027", pos=0, check=_sa9)

# 10 -- cousins of a child whose parents are only children
def _br10():
    parents_siblings = {"father": [], "mother": []}           # both parents are only children
    cousins = [child for sibs in parents_siblings.values() for s in sibs for child in s]
    return str(len(cousins))
N(LR, "Blood Relation", "easy",
  "Both of Ravi's parents are only children: neither his father nor his mother has a brother or a sister. How many first cousins does Ravi have?",
  "रवि के माता-पिता दोनों अपने माता-पिता की इकलौती संतान हैं: न उसके पिता का कोई भाई या बहन है, न उसकी माँ का। रवि के कितने सगे चचेरे, ममेरे, फुफेरे या मौसेरे भाई-बहन हैं?",
  ["0", "1", "2", "4"], 0,
  "A first cousin is a child of one's parent's brother or sister. Ravi's parents have no brothers or sisters, so there is no one whose child could be his first cousin: he has none. "
  "The other numbers would each need at least one uncle or aunt by birth.",
  "सगा चचेरा, ममेरा, फुफेरा या मौसेरा भाई-बहन माता या पिता के भाई या बहन की संतान होता है। रवि के माता-पिता के कोई भाई या बहन नहीं, इसलिए कोई ऐसा नहीं जिसकी संतान उसकी ऐसी भाई-बहन हो सके: उसके कोई नहीं हैं। "
  "बाक़ी संख्याओं में से हर एक के लिए जन्म से कम से कम एक चाचा, मामा, बुआ या मौसी चाहिए।",
  "lr-br-cousins-of-a-child-whose-parents-are-only-children", _br10)

# 11 -- a mother's sister's son
def _br11():
    mother = {"Asha": "M"}
    sister = {"M": "Bela"}
    son = {"Bela": "Chand"}
    assert son[sister[mother["Asha"]]] == "Chand"
    return "Cousin"
T(LR, "Blood Relation", "medium",
  "Asha's mother is Bela's sister, and Chand is Bela's only son. How is Chand related to Asha?",
  "आशा की माँ, बेला की बहन है, और चाँद, बेला का इकलौता बेटा है। चाँद, आशा का क्या लगता है?",
  ["Cousin", "Uncle", "Brother", "Nephew"], ["मौसेरा भाई", "मामा", "भाई", "भतीजा"],
  0,
  "Bela is the sister of Asha's mother, that is, Asha's mother's sister. Chand, Bela's son, is therefore the son of Asha's mother's sister: her cousin. "
  "An uncle would be her mother's brother, not her aunt's son; Chand is not her mother's son, so not her brother; and a nephew would be her sibling's son.",
  "बेला, आशा की माँ की बहन है, यानी आशा की मौसी। इसलिए चाँद, बेला का बेटा, आशा की मौसी का बेटा है: उसका मौसेरा भाई। "
  "मामा उसकी माँ का भाई होता, मौसी का बेटा नहीं; चाँद उसकी माँ का बेटा नहीं, इसलिए भाई नहीं; और भतीजा उसके भाई का बेटा होता।",
  "lr-br-a-mother-s-sister-s-son", pos=3, check=_br11)

# 12 -- the Roman numerals hidden in a word
def _cd12():
    val = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    return str(sum(val.get(ch, 0) for ch in "CIVIL"))
N(LR, "Coding-Decoding", "medium",
  "In a code, every letter of a word that is also a Roman numeral (I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1,000) is replaced by its value, every other letter by 0, and the values are added. What is the code for CIVIL?",
  "एक कूट में किसी शब्द का हर ऐसा अक्षर जो रोमन अंक भी है (I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1,000) उसके मान से, बाक़ी हर अक्षर 0 से बदला जाता है, और मान जोड़े जाते हैं। CIVIL का कूट क्या है?",
  ["107", "156", "157", "166"], 2,
  "Every letter of CIVIL is a Roman numeral: C = 100, I = 1, V = 5, I = 1, L = 50. Added, they give 157. "
  "107 leaves out the L; 156 counts only one of the two Is; 166 has no basis. (The code adds the values; it does not read CIVIL as a Roman number, which it is not.)",
  "CIVIL का हर अक्षर रोमन अंक है: C = 100, I = 1, V = 5, I = 1, L = 50। जोड़ने पर 157 मिलता है। "
  "107, L को छोड़ देता है; 156 दोनों I में से केवल एक गिनता है; 166 का कोई आधार नहीं। (कूट मानों को जोड़ता है; वह CIVIL को रोमन संख्या की तरह नहीं पढ़ता, जो वह है भी नहीं।)",
  "lr-cd-the-roman-numerals-hidden-in-a-word", _cd12)

# 13 -- a code of digit sums
def _cd13():
    code = lambda w: "".join(str(sum(map(int, str(ord(ch) - 64)))) for ch in w)
    assert code("J") == "1" and code("Z") == "8"
    return code("ZEBRA")
T(LR, "Coding-Decoding", "medium",
  "In a code, each letter is replaced by the sum of the digits of its position in the alphabet: A to I become 1 to 9, J (10) becomes 1, K (11) becomes 2, and so on, so that Z (26) becomes 8. How is ZEBRA written in this code?",
  "एक कूट में हर अक्षर को वर्णमाला में उसके स्थान के अंकों के योग से बदला जाता है: A से I, 1 से 9 बनते हैं, J (10), 1 बनता है, K (11), 2, और इसी तरह, ताकि Z (26), 8 बने। इस कूट में ZEBRA कैसे लिखा जाता है?",
  ["85291", "2652181", "85281", "86291"], ["85291", "2652181", "85281", "86291"],
  0,
  "Z is 26, and 2 + 6 = 8; E is 5; B is 2; R is 18, and 1 + 8 = 9; A is 1. So ZEBRA becomes 85291. "
  "2652181 writes the positions themselves without adding their digits; 85281 slips on R; 86291 slips on E.",
  "Z, 26 है, और 2 + 6 = 8; E, 5 है; B, 2; R, 18 है, और 1 + 8 = 9; A, 1 है। अतः ZEBRA, 85291 बनता है। "
  "2652181 स्थानों को उनके अंक जोड़े बिना ही लिख देता है; 85281, R पर चूकता है; 86291, E पर।",
  "lr-cd-a-code-of-digit-sums", pos=1, check=_cd13)

# 14 -- a chain of three moves
def _dd14():
    B = (0, 0)
    A = (B[0], B[1] - 5)                          # A is 5 km south of B
    C = (A[0] + 5, A[1])                          # C is 5 km east of A
    D = (C[0], C[1] + 5)                          # D is 5 km north of C
    assert D == (5, 0)
    return "5 km to the east"
T(LR, "Direction & Distance", "medium",
  "Village A is 5 km due south of village B. Village C is 5 km due east of A, and village D is 5 km due north of C. Where is D from B?",
  "गाँव A, गाँव B से 5 किमी ठीक दक्षिण में है। गाँव C, A से 5 किमी ठीक पूर्व में है, और गाँव D, C से 5 किमी ठीक उत्तर में। D, B से कहाँ है?",
  ["5 km to the east", "5 km to the west", "5√2 km to the north-east", "10 km to the east"],
  ["5 किमी पूर्व में", "5 किमी पश्चिम में", "5√2 किमी उत्तर-पूर्व में", "10 किमी पूर्व में"],
  0,
  "Going from B: 5 km south to A, 5 km east to C, then 5 km north to D. The south and north legs cancel, leaving only the 5 km east: D is 5 km due east of B. "
  "West reverses the east leg; 5√2 km to the north-east treats two of the legs as a single diagonal; 10 km adds a leg twice.",
  "B से चलिए: 5 किमी दक्षिण A तक, 5 किमी पूर्व C तक, फिर 5 किमी उत्तर D तक। दक्षिण और उत्तर के चरण एक-दूसरे को काट देते हैं, केवल 5 किमी पूर्व बचता है: D, B से 5 किमी ठीक पूर्व में है। "
  "पश्चिम पूर्व वाले चरण को उलट देता है; 5√2 किमी उत्तर-पूर्व दो चरणों को एक विकर्ण मान लेता है; 10 किमी एक चरण को दो बार जोड़ता है।",
  "lr-dd-a-chain-of-three-moves", pos=3, check=_dd14)

# 15 -- a turn made facing a school
def _dd15():
    school, post = (0, 0), (1, 0)                # the post office is due east of the school
    facing = (school[0] - post[0], school[1] - post[1])     # facing the school: west
    right = (facing[1], -facing[0])                         # a right turn
    names = {(0, 1): "North", (0, -1): "South", (1, 0): "East", (-1, 0): "West"}
    assert names[facing] == "West"
    return names[right]
T(LR, "Direction & Distance", "medium",
  "From a school, a temple lies due north and a post office due east. A man standing at the post office faces the school and then turns to his right. In which direction is he now facing?",
  "एक विद्यालय से एक मंदिर ठीक उत्तर में और एक डाकघर ठीक पूर्व में है। डाकघर पर खड़ा एक व्यक्ति विद्यालय की ओर मुख करता है और फिर अपनी दाईं ओर मुड़ता है। अब वह किस दिशा की ओर मुख किए है?",
  ["North", "South", "East", "West"], ["उत्तर", "दक्षिण", "पूर्व", "पश्चिम"],
  0,
  "The post office is east of the school, so a man at the post office who faces the school faces west. A right turn from west faces north. "
  "South would be a left turn; west is the way he faced before turning; east would mean turning right round. The temple is not needed.",
  "डाकघर विद्यालय के पूर्व में है, इसलिए डाकघर पर विद्यालय की ओर मुख किया व्यक्ति पश्चिम की ओर मुख किए है। पश्चिम से दाईं ओर मुड़ने पर मुख उत्तर की ओर होता है। "
  "दक्षिण बाईं ओर मुड़ने पर होता; पश्चिम मुड़ने से पहले की दिशा है; पूर्व पूरा पीछे घूमने पर। मंदिर की आवश्यकता नहीं।",
  "lr-dd-a-turn-made-facing-a-school", pos=2, check=_dd15)

# 16 -- the lines through the inside of a cube
def _cp16():
    corners = list(product((0, 1), repeat=3))
    pairs = list(combinations(corners, 2))
    differ = lambda a, b: sum(x != y for x, y in zip(a, b))
    edges = sum(1 for a, b in pairs if differ(a, b) == 1)
    face_diagonals = sum(1 for a, b in pairs if differ(a, b) == 2)
    inside = sum(1 for a, b in pairs if differ(a, b) == 3)
    assert (len(pairs), edges, face_diagonals) == (28, 12, 12)
    return str(inside)
N(LR, "Cube Painting", "medium",
  "Straight lines are drawn joining every pair of corners of a cube. How many of these lines pass through the inside of the cube, rather than along an edge or across a face?",
  "एक घन के हर दो कोनों को जोड़ती सीधी रेखाएँ खींची जाती हैं। इनमें से कितनी रेखाएँ किसी किनारे के साथ या किसी फलक के आर-पार जाने के बजाय घन के भीतर से होकर जाती हैं?",
  ["2", "4", "8", "12"], 1,
  "A cube has 8 corners, so there are 8C2 = 28 lines in all. 12 of them are the edges, and each of the 6 faces has 2 diagonals, another 12. That leaves 28 - 24 = 4, the lines from each corner to the one diagonally opposite it through the centre. "
  "12 is the number of edges, or of face diagonals; 8 counts each inside line twice, once from each end; 2 has no basis.",
  "घन के 8 कोने हैं, इसलिए कुल 8C2 = 28 रेखाएँ हैं। उनमें से 12 किनारे हैं, और 6 फलकों में से हर एक के 2 विकर्ण हैं, और 12। इससे 28 - 24 = 4 बचती हैं, हर कोने से केंद्र होकर ठीक सामने वाले कोने तक की रेखाएँ। "
  "12 किनारों की, या फलक-विकर्णों की, संख्या है; 8 भीतर की हर रेखा को दो बार गिनता है, दोनों सिरों से; 2 का कोई आधार नहीं।",
  "lr-cp-the-lines-through-the-inside-of-a-cube", _cp16)

# 17 -- singers who are not violinists
def _sy17():
    regions = [r for r in product((0, 1), repeat=3) if any(r)]     # (violinist, tone-deaf, singer)
    one = two = True
    for present in product((0, 1), repeat=len(regions)):
        filled = {r for r, p in zip(regions, present) if p}
        if any(v and t for v, t, s in filled):                     # no violinist is tone-deaf
            continue
        if not any(t and s for v, t, s in filled):                 # some singers are tone-deaf
            continue
        if not any(v for v, t, s in filled):                       # there are violinists
            continue
        one &= any(s and not v for v, t, s in filled)
        two &= any(v and not s for v, t, s in filled)
    return c.T2R[{(True, True): 2, (True, False): 0, (False, True): 1, (False, False): 3}[(one, two)]]
S2(LR, "Syllogism", "hard",
   "Statements: No violinist is tone-deaf. Some singers are tone-deaf.\n\nWhich of the following conclusions follow(s) from the statements?",
   "कथन: कोई भी वायलिन-वादक सुर-बधिर नहीं है। कुछ गायक सुर-बधिर हैं।\n\nनिम्नलिखित में से कौन-सा/से निष्कर्ष कथनों से निकलता/निकलते है/हैं?",
   ["Some singers are not violinists.", "Some violinists are not singers."],
   ["कुछ गायक वायलिन-वादक नहीं हैं।", "कुछ वायलिन-वादक गायक नहीं हैं।"],
   0,
   "Only I follows. The tone-deaf singers cannot be violinists, since no violinist is tone-deaf; so those singers are not violinists (I). "
   "II does not follow: nothing prevents every violinist from also being a singer -- the statements are equally true if all the violinists sing. Reading I backwards as II is the trap.",
   "केवल I निकलता है। सुर-बधिर गायक वायलिन-वादक नहीं हो सकते, क्योंकि कोई वायलिन-वादक सुर-बधिर नहीं; इसलिए वे गायक वायलिन-वादक नहीं हैं (I)। "
   "II नहीं निकलता: कुछ भी हर वायलिन-वादक के गायक होने से नहीं रोकता -- यदि सभी वायलिन-वादक गाते हों तो भी कथन उतने ही सत्य हैं। I को उलटकर II पढ़ना ही जाल है।",
   "lr-sy-singers-who-are-not-violinists", roman=True, check=_sy17)

# ---- the data-sufficiency block's three Reasoning items
def _ds18():
    worlds = list(product((True, False), repeat=3))           # (Meena in the class with a pencil, rule holds, has pen)
    ok1 = lambda inclass, rule, pen: rule and (not inclass or pen)
    ok2 = lambda inclass, rule, pen: inclass
    s1 = {pen for w in worlds for pen in [w[2]] if ok1(*w)}
    s2 = {pen for w in worlds for pen in [w[2]] if ok2(*w)}
    both = {pen for w in worlds for pen in [w[2]] if ok1(*w) and ok2(*w)}
    assert both == {True} and s1 == s2 == {True, False}
    return _ds(s1, s2, both)
DS(LR, "medium",
   "Does Meena have a pen?",
   "क्या मीना के पास पेन है?",
   "Everyone in Meena's class who has a pencil also has a pen.", "मीना की कक्षा में जिसके पास पेंसिल है, उसके पास पेन भी है।",
   "Meena is in that class, and she has a pencil.", "मीना उसी कक्षा में है, और उसके पास पेंसिल है।",
   2,
   "Statement I alone gives a rule but does not say whether Meena has a pencil. Statement II alone says she has a pencil but gives no rule linking pencils to pens. Together: she is in the class and has a pencil, and everyone there with a pencil has a pen, so she has a pen. Both statements are needed.",
   "कथन I अकेले एक नियम देता है पर यह नहीं बताता कि मीना के पास पेंसिल है या नहीं। कथन II अकेले कहता है कि उसके पास पेंसिल है पर पेंसिल को पेन से जोड़ने वाला कोई नियम नहीं देता। दोनों मिलकर: वह कक्षा में है और उसके पास पेंसिल है, और वहाँ पेंसिल वाले हर व्यक्ति के पास पेन है, इसलिए उसके पास पेन है। दोनों कथन आवश्यक हैं।",
   "lr-ds-a-pen-that-follows-from-a-pencil", _ds18)

def _ds19():
    # Counting each handshake from both ends gives twice the number of handshakes, so 3n must be even.
    s1 = {n % 2 == 0 for n in range(2, 60) if (3 * n) % 2 == 0}
    s2 = {n % 2 == 0 for n in range(11, 60)}
    both = {n % 2 == 0 for n in range(11, 60) if (3 * n) % 2 == 0}
    assert s1 == {True}
    return _ds(s1, s2, both)
DS(LR, "hard",
   "At a meeting, is the number of people present an even number?",
   "एक बैठक में, क्या उपस्थित लोगों की संख्या सम है?",
   "Every person present shook hands with exactly three of the others.", "हर उपस्थित व्यक्ति ने बाक़ी में से ठीक तीन से हाथ मिलाया।",
   "More than ten people were present.", "दस से अधिक लोग उपस्थित थे।",
   0,
   "Statement I alone settles it. If there are n people and each shook three hands, counting from every person gives 3n -- but that counts each handshake twice, once from each end, so 3n must be an even number, and n must be even. Statement II alone says nothing about evenness. So one statement alone is enough, but not the other.",
   "कथन I अकेले इसे तय कर देता है। यदि n लोग हैं और हर एक ने तीन हाथ मिलाए, तो हर व्यक्ति से गिनने पर 3n मिलता है -- पर इसमें हर हाथ मिलाना दो बार, दोनों ओर से, गिना जाता है, इसलिए 3n सम संख्या होनी चाहिए, और n सम होना चाहिए। कथन II अकेले सम होने के बारे में कुछ नहीं कहता। अतः एक कथन अकेले पर्याप्त है, पर दूसरा नहीं।",
   "lr-ds-a-room-where-everyone-shook-three-hands", _ds19)

def _ds20():
    # A class of two rows of two; heights 1-4; Ravi is student 0, in row 0 with student 1; row 1 holds 2 and 3.
    worlds = []
    for h in permutations(range(1, 5)):
        for front in (0, 1):                                  # which row is the front row
            worlds.append((h, front))
    ok1 = lambda h, f: h[0] > h[1]                             # taller than everyone else in his row
    ok2 = lambda h, f: f == 0                                  # his row is the front row
    tallest = lambda h: h[0] == max(h)
    s1 = {tallest(h) for h, f in worlds if ok1(h, f)}
    s2 = {tallest(h) for h, f in worlds if ok2(h, f)}
    both = {tallest(h) for h, f in worlds if ok1(h, f) and ok2(h, f)}
    assert both == {True, False}
    return _ds(s1, s2, both)
DS(LR, "hard",
   "Is Ravi the tallest student in his class?",
   "क्या रवि अपनी कक्षा का सबसे लंबा विद्यार्थी है?",
   "Ravi is taller than every other student in his row.", "रवि अपनी पंक्ति के हर अन्य विद्यार्थी से लंबा है।",
   "Ravi's row is the front row of the class.", "रवि की पंक्ति कक्षा की पहली पंक्ति है।",
   3,
   "Statement I makes Ravi the tallest in his row, but a student in another row could be taller still. Statement II only says where his row is, which has nothing to do with height. Even together, a taller student may sit in another row, so the question cannot be answered.",
   "कथन I रवि को उसकी पंक्ति में सबसे लंबा बनाता है, पर किसी दूसरी पंक्ति का विद्यार्थी उससे भी लंबा हो सकता है। कथन II केवल यह बताता है कि उसकी पंक्ति कहाँ है, जिसका लंबाई से कोई संबंध नहीं। दोनों मिलकर भी कोई अधिक लंबा विद्यार्थी दूसरी पंक्ति में हो सकता है, इसलिए प्रश्न का उत्तर नहीं दिया जा सकता।",
   "lr-ds-a-boy-who-is-tallest-in-his-row", _ds20)
