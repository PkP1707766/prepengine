# -*- coding: utf-8 -*-
"""CSAT Level 3 · Test 1 -- Logical Reasoning (18 items: 15 in the Reasoning slots, 3 in the data-sufficiency block).

Level 3's harder mix (1 easy / 10 medium / 7 hard), with none of the shapes of Level 2 Tests 1-7 or Level 1 Minis 1-3:
successful founders who dropped out of college (the failures nobody studied), accidents near home (exposure read as
danger), the assumption behind translating judgments; two concentric circles facing each other, two flats on each of
four floors, five teachers on five days with two subjects left open; a woman pointing to a photograph, the fewest people for two fathers and
two sons; a walk with three left turns, three villages placed by diagonal directions alone; a code read off a 5 × 5 grid of
letters, a rule found from three examples; six colours on a cube's faces; pens, tools and toys; a speaker who says
'either I am a liar or ...'; and in the data-sufficiency block a birthday's month, whether everyone passed, and two games
in one club. Arrangement, code, cube, syllogism and truth-teller keys are found by checking every case."""
from fractions import Fraction as F
from itertools import permutations, product
import csat_common as c
from csat_common import N, T, S2, SC, DS, LR

def _ds(s1, s2, both):
    alone = (len(set(s1)) == 1, len(set(s2)) == 1)
    return "b" if all(alone) else "a" if any(alone) else "c" if len(set(both)) == 1 else "d"

# 1 -- successful founders who left college: the failures nobody counted
T(LR, "Statement-Conclusion/Assumption", "medium",
  "A magazine studied fifty of the country's most successful start-up founders and found that more than half of them had left college without a degree. It concluded that leaving college early improves a person's chances of building a successful company. "
  "Which one of the following, if true, most seriously weakens this conclusion?",
  "एक पत्रिका ने देश के पचास सबसे सफल स्टार्ट-अप संस्थापकों का अध्ययन किया और पाया कि उनमें से आधे से अधिक ने बिना डिग्री लिए कॉलेज छोड़ दिया था। उसने निष्कर्ष निकाला कि कॉलेज जल्दी छोड़ने से सफल कंपनी बनाने की संभावना बढ़ती है। "
  "निम्नलिखित में से कौन-सा, यदि सत्य हो, इस निष्कर्ष को सबसे गंभीर रूप से कमज़ोर करता है?",
  ["Far more people who left college early started companies that failed, and none of them was studied.",
   "Some of the successful founders went back to college years later and completed their degrees.",
   "Several of the founders said that their college courses had taught them little that was useful in business.",
   "The magazine's list included founders from many different industries and regions of the country."],
  ["कॉलेज जल्दी छोड़ने वाले कहीं अधिक लोगों की कंपनियाँ विफल रहीं, और उनमें से किसी का अध्ययन नहीं हुआ।",
   "कुछ सफल संस्थापक वर्षों बाद कॉलेज लौटे और उन्होंने अपनी डिग्री पूरी की।",
   "कई संस्थापकों ने कहा कि कॉलेज के पाठ्यक्रमों ने उन्हें व्यापार के लिए उपयोगी बहुत कम बातें सिखाई थीं।",
   "पत्रिका की सूची में कई अलग-अलग उद्योगों और देश के क्षेत्रों के संस्थापक शामिल थे।"],
  0,
  "The magazine looked only at successes. If far more people who left college started companies that failed, leaving college may be common among founders of every kind, successful or not, and the fifty tell us nothing about whether it improves the chances; this is the gap the conclusion cannot survive. "
  "That some founders later finished their degrees does not touch the link between leaving and succeeding; the founders' low opinion of their courses, if anything, supports the conclusion; and a list drawn from many industries makes the sample look more representative, not less.",
  "पत्रिका ने केवल सफलताओं को देखा। यदि कॉलेज छोड़ने वाले कहीं अधिक लोगों ने विफल कंपनियाँ शुरू कीं, तो कॉलेज छोड़ना हर तरह के संस्थापकों में, सफल हों या नहीं, आम हो सकता है, और वे पचास यह कुछ नहीं बताते कि इससे संभावना बढ़ती है या नहीं; यही वह कमी है जिसे निष्कर्ष झेल नहीं सकता। "
  "कुछ संस्थापकों का बाद में डिग्री पूरी करना छोड़ने और सफल होने के संबंध को नहीं छूता; अपने पाठ्यक्रमों के बारे में संस्थापकों की कम राय तो निष्कर्ष का कुछ समर्थन ही करती है; और कई उद्योगों से ली गई सूची नमूने को कम नहीं, अधिक प्रतिनिधिक दिखाती है।",
  "lr-sc-founders-who-left-college", pos=3)

# 2 -- accidents near home: more driving, not more danger
T(LR, "Statement-Conclusion/Assumption", "hard",
  "A survey of road accidents found that most accidents involving private cars happen within five kilometres of the driver's home. A commentator concluded that the roads near one's home are more dangerous than the roads farther away. "
  "Which one of the following best describes the flaw in this reasoning?",
  "सड़क दुर्घटनाओं के एक सर्वेक्षण में पाया गया कि निजी कारों की अधिकांश दुर्घटनाएँ चालक के घर से पाँच किलोमीटर के भीतर होती हैं। एक टिप्पणीकार ने निष्कर्ष निकाला कि घर के पास की सड़कें दूर की सड़कों से अधिक ख़तरनाक हैं। "
  "निम्नलिखित में से कौन-सा इस तर्क की त्रुटि का सबसे अच्छा वर्णन करता है?",
  ["It overlooks that most driving is done near home, so most accidents would happen there even if all roads were equally safe.",
   "It assumes that drivers are more careful on roads they do not know well than on the roads near their homes every day.",
   "It relies on a survey of accidents involving private cars only and leaves out the buses, trucks and two-wheelers on the road.",
   "It does not say how many of the accidents in the survey were serious enough to injure someone or to damage property badly."],
  ["यह अनदेखा करता है कि अधिकांश गाड़ी घर के पास चलती है, इसलिए सब सड़कें समान सुरक्षित हों तब भी अधिकांश दुर्घटनाएँ वहीं होंगी।",
   "यह मान लेता है कि चालक रोज़ की घर के पास की सड़कों की तुलना में अनजानी सड़कों पर अधिक सावधान रहते हैं।",
   "यह केवल निजी कारों की दुर्घटनाओं के सर्वेक्षण पर टिका है और सड़कों पर चलने वाली बसों, ट्रकों और दोपहिया वाहनों को पूरी तरह छोड़ देता है।",
   "यह नहीं बताता कि सर्वेक्षण की कितनी दुर्घटनाएँ इतनी गंभीर थीं कि किसी को चोट लगे या संपत्ति को बुरी हानि हो।"],
  0,
  "A larger share of accidents in a place shows more danger only if the exposure -- the amount of driving done there -- is the same. Most trips begin and end near home, so most kilometres are driven there, and most accidents would happen there even if every kilometre carried the same risk. "
  "The reasoning compares counts of accidents and ignores the base of driving behind them. The option about drivers being more careful on unfamiliar roads describes a possible reason for danger near home, not a flaw in the argument; leaving out buses and trucks, or not grading the accidents by severity, narrows the survey but does not touch the inference from 'most accidents' to 'more dangerous'.",
  "किसी स्थान पर दुर्घटनाओं का बड़ा हिस्सा अधिक ख़तरा तभी दिखाता है जब वहाँ जोखिम का आधार -- वहाँ चलाई गई गाड़ी की मात्रा -- समान हो। अधिकांश यात्राएँ घर के पास शुरू और समाप्त होती हैं, इसलिए अधिकांश किलोमीटर वहीं चलाए जाते हैं, और हर किलोमीटर का जोखिम समान हो तब भी अधिकांश दुर्घटनाएँ वहीं होंगी। "
  "तर्क दुर्घटनाओं की गिनती की तुलना करता है और उनके पीछे गाड़ी चलाने के आधार को अनदेखा करता है। अनजानी सड़कों पर अधिक सावधानी वाला विकल्प घर के पास ख़तरे का एक संभावित कारण बताता है, तर्क की त्रुटि नहीं; बसों और ट्रकों को छोड़ना, या दुर्घटनाओं को गंभीरता से न आँकना, सर्वेक्षण को संकीर्ण करता है पर 'अधिकांश दुर्घटनाएँ' से 'अधिक ख़तरनाक' तक के अनुमान को नहीं छूता।",
  "lr-sc-accidents-near-home", pos=1)

# 3 -- translating judgments: the unstated premise
S2(LR, "Statement-Conclusion/Assumption", "medium",
   "Statement: 'Court judgments should be translated into the regional languages, so that people can understand the decisions in their own cases.'\n\nWhich of the following assumptions is/are implicit in the statement?",
   "कथन: 'न्यायालयों के निर्णयों का क्षेत्रीय भाषाओं में अनुवाद होना चाहिए, ताकि लोग अपने मामलों में दिए गए निर्णयों को समझ सकें।'\n\nनिम्नलिखित में से कौन-सी पूर्वधारणा/एँ कथन में अंतर्निहित है/हैं?",
   ["Many litigants cannot read the language in which judgments are now written.",
    "Translating judgments will make the courts decide cases faster."],
   ["अनेक वादी उस भाषा को नहीं पढ़ सकते जिसमें अभी निर्णय लिखे जाते हैं।",
    "निर्णयों के अनुवाद से न्यायालय मामलों का निर्णय तेज़ी से करेंगे।"],
   0,
   "Only I is implicit. The proposal is offered so that people can understand the decisions in their own cases; that purpose makes sense only if many of them cannot read judgments in the language in which they are written now. "
   "II is not assumed: translation happens after a judgment is delivered and says nothing about how fast cases are decided; the statement makes no claim about speed.",
   "केवल I अंतर्निहित है। प्रस्ताव इसलिए दिया गया है कि लोग अपने मामलों के निर्णय समझ सकें; यह उद्देश्य तभी सार्थक है जब उनमें से अनेक अभी जिस भाषा में निर्णय लिखे जाते हैं उसमें उन्हें न पढ़ सकते हों। "
   "II पूर्वधारणा नहीं है: अनुवाद निर्णय सुनाए जाने के बाद होता है और यह कुछ नहीं कहता कि मामलों का निर्णय कितनी तेज़ी से होता है; कथन गति के बारे में कोई दावा नहीं करता।",
   "lr-sc-the-assumption-behind-translating-judgments", roman=True)

# 4 -- two concentric circles that face each other
def _sa1():
    out = set()
    for inner in permutations("ABCD"):
        for outer in permutations("PQRS"):
            i = {x: k for k, x in enumerate(inner)}       # positions 0-3 clockwise; inner k faces outer k
            o = {x: k for k, x in enumerate(outer)}
            # facing outwards, a person's left neighbour is anticlockwise (k - 1); facing inwards, clockwise (k + 1)
            if (o["P"] == i["A"] and i["B"] == (i["A"] - 1) % 4 and o["Q"] == (i["A"] + 2) % 4
                    and o["R"] == (o["Q"] - 1) % 4 and i["D"] == (o["P"] + 1) % 4):
                out.add(outer[i["C"]])
    assert len(out) == 1, out
    return out.pop()
T(LR, "Seating Arrangement", "hard",
  "Eight people sit in two concentric circles of four. A, B, C and D sit in the inner circle facing outwards, and P, Q, R and S sit in the outer circle facing inwards, so that each person in the inner circle faces exactly one person in the outer circle. "
  "A faces P. B sits to the immediate left of A. Q faces the person who sits opposite A in the inner circle. R sits to the immediate right of Q. D faces the person who sits to the immediate left of P. Who faces C?",
  "आठ व्यक्ति चार-चार के दो संकेंद्री वृत्तों में बैठे हैं। A, B, C और D भीतरी वृत्त में बाहर की ओर मुँह करके बैठे हैं, और P, Q, R और S बाहरी वृत्त में भीतर की ओर मुँह करके, इस तरह कि भीतरी वृत्त का हर व्यक्ति बाहरी वृत्त के ठीक एक व्यक्ति के आमने-सामने है। "
  "A, P के सामने है। B, A के ठीक बाएँ बैठा है। Q उस व्यक्ति के सामने है जो भीतरी वृत्त में A के ठीक विपरीत बैठा है। R, Q के ठीक दाएँ बैठा है। D उस व्यक्ति के सामने है जो P के ठीक बाएँ बैठा है। C के सामने कौन है?",
  ["P", "Q", "R", "S"], ["P", "Q", "R", "S"], 1,
  "Number the places clockwise as seen from above, with A at place 1, so that P is at outer place 1. Someone facing outwards has the anticlockwise neighbour on the left, while someone facing inwards has the clockwise neighbour on the left: the two circles see left and right the opposite way. "
  "So B, on A's left, is at inner place 4. Q faces the inner place opposite A, place 3; R, on Q's right, is at outer place 2 (anticlockwise for someone facing in); S takes outer place 4. P's left is outer place 2, where R sits, so D faces R and is at inner place 2, which leaves C at inner place 3 -- the place opposite A, faced by Q.",
  "ऊपर से देखने पर स्थानों को दक्षिणावर्त क्रम में गिनिए, A को स्थान 1 पर रखकर, ताकि P बाहरी स्थान 1 पर हो। बाहर की ओर मुँह करने वाले के बाएँ वामावर्त पड़ोसी होता है, जबकि भीतर की ओर मुँह करने वाले के बाएँ दक्षिणावर्त पड़ोसी: दोनों वृत्त बाएँ और दाएँ को उलटे ढंग से देखते हैं। "
  "इसलिए A के बाएँ वाला B भीतरी स्थान 4 पर है। Q, A के विपरीत भीतरी स्थान 3 के सामने है; Q के दाएँ वाला R बाहरी स्थान 2 पर है (भीतर मुँह करने वाले के लिए वामावर्त); S बाहरी स्थान 4 लेता है। P के बाएँ बाहरी स्थान 2 है, जहाँ R बैठा है, इसलिए D, R के सामने है और भीतरी स्थान 2 पर है, जिससे C भीतरी स्थान 3 पर बचता है -- A के विपरीत वाला स्थान, जिसके सामने Q है।",
  "lr-sa-two-concentric-circles-facing-each-other", pos=1, check=_sa1)

# 5 -- two flats on each of four floors
def _sa2():
    spots = [(f, s) for f in range(1, 5) for s in "WE"]
    above = lambda x, y: x[1] == y[1] and x[0] == y[0] + 1
    out = set()
    for p in permutations(spots):
        a = dict(zip("ABCDEFGH", p))
        if (a["C"] == (4, "E") and above(a["A"], a["B"]) and a["B"][1] == "W" and a["D"][0] == a["A"][0]
                and above(a["D"], a["H"]) and a["E"][1] == "W" and a["E"][0] < a["B"][0] and a["G"][0] < a["F"][0]):
            out.add(next(k for k, v in a.items() if v == (3, "E")))
    assert len(out) == 1, out
    return out.pop()
T(LR, "Seating Arrangement", "hard",
  "A building has four floors, numbered 1 (the lowest) to 4 (the top), and each floor has two flats, one on the west side and one on the east side. Eight people, A to H, live one in each flat. "
  "C lives on the top floor, on the east side. A lives directly above B, and B lives on the west side. D lives on the same floor as A, and H lives directly below D. E lives on the west side, on a floor below B's. G lives on a lower floor than F. Who lives directly below C?",
  "एक इमारत में चार मंज़िलें हैं, जिन्हें 1 (सबसे नीचे) से 4 (सबसे ऊपर) तक गिना गया है, और हर मंज़िल पर दो फ़्लैट हैं, एक पश्चिम की ओर और एक पूर्व की ओर। आठ व्यक्ति, A से H, हर फ़्लैट में एक-एक रहते हैं। "
  "C सबसे ऊपरी मंज़िल पर पूर्व की ओर रहता है। A, B के ठीक ऊपर रहता है, और B पश्चिम की ओर रहता है। D, A की मंज़िल पर रहता है, और H, D के ठीक नीचे रहता है। E पश्चिम की ओर, B से नीचे की किसी मंज़िल पर रहता है। G, F से नीचे की मंज़िल पर रहता है। C के ठीक नीचे कौन रहता है?",
  ["A", "D", "F", "H"], ["A", "D", "F", "H"], 1,
  "A and D share a floor, and B and H live directly below them, so the four fill two whole floors, one above the other. E lives on the west side below B, so B cannot be on floor 1; and A and D cannot be on floor 4, where C already lives. "
  "So A and D are on floor 3 and B and H on floor 2, with E on floor 1 west. B is on the west side, so A, directly above him, is on 3 west, and D is on 3 east, with H below him on 2 east. The flats left are 4 west and 1 east: G must be the lower, so G is on 1 east and F on 4 west. Directly below C (4 east) is D.",
  "A और D एक मंज़िल पर हैं, और B और H उनके ठीक नीचे रहते हैं, इसलिए ये चार एक के ऊपर एक दो पूरी मंज़िलें भरते हैं। E, B से नीचे पश्चिम की ओर रहता है, इसलिए B मंज़िल 1 पर नहीं हो सकता; और A और D मंज़िल 4 पर नहीं हो सकते, जहाँ C पहले से रहता है। "
  "अतः A और D मंज़िल 3 पर और B और H मंज़िल 2 पर हैं, और E मंज़िल 1 पर पश्चिम में। B पश्चिम की ओर है, इसलिए उसके ठीक ऊपर वाला A, 3 पश्चिम में है, और D, 3 पूर्व में, उसके नीचे H, 2 पूर्व में। बचे फ़्लैट 4 पश्चिम और 1 पूर्व हैं: G को नीचे वाला होना है, इसलिए G, 1 पूर्व में और F, 4 पश्चिम में। C (4 पूर्व) के ठीक नीचे D है।",
  "lr-sa-two-flats-on-each-of-four-floors", pos=2, check=_sa2)

# 6 -- five teachers on five days: the arrangement is open, the asked fact is not
def _sa3():
    subs = ["History", "Geography", "Polity", "Economy", "Science"]
    out, n = set(), 0
    for dp in permutations(range(5)):
        day = dict(zip("PQRST", dp))
        for sp in permutations(subs):
            sub = dict(zip("PQRST", sp))
            sd = {sub[t]: day[t] for t in "PQRST"}
            if (sd["Polity"] == 2 and day["Q"] == sd["History"] + 1 and sub["R"] == "Science" and day["R"] not in (0, 4)
                    and day["S"] == sd["Economy"] + 1 and day["T"] == 4 and day["P"] == 0):
                n += 1
                out.add(next(t for t in "PQRST" if sub[t] == "Geography"))
    assert n == 2 and len(out) == 1, (n, out)
    return out.pop()
T(LR, "Seating Arrangement", "medium",
  "Five teachers -- P, Q, R, S and T -- each teach one of five subjects (History, Geography, Polity, Economy and Science), one class a day from Monday to Friday. P teaches on Monday and T on Friday. Polity is taught on Wednesday. "
  "R teaches Science, but not on Monday or Friday. Q teaches on the day after the History class, and S teaches on the day after the Economy class. Who teaches Geography?",
  "पाँच शिक्षक -- P, Q, R, S और T -- पाँच विषयों (इतिहास, भूगोल, राजव्यवस्था, अर्थव्यवस्था और विज्ञान) में से एक-एक पढ़ाते हैं, सोमवार से शुक्रवार तक प्रतिदिन एक कक्षा। P सोमवार को और T शुक्रवार को पढ़ाता है। राजव्यवस्था बुधवार को पढ़ाई जाती है। "
  "R विज्ञान पढ़ाता है, पर सोमवार या शुक्रवार को नहीं। Q इतिहास की कक्षा के अगले दिन पढ़ाता है, और S अर्थव्यवस्था की कक्षा के अगले दिन। भूगोल कौन पढ़ाता है?",
  ["P", "Q", "S", "T"], ["P", "Q", "S", "T"], 3,
  "R teaches Science on Tuesday, Wednesday or Thursday, and Wednesday is Polity, so R is on Tuesday or Thursday. If R were on Tuesday, Q would be on Wednesday or Thursday, with History the day before -- Tuesday (Science) or Wednesday (Polity) -- which is impossible. So R is on Thursday, and Q and S teach on Tuesday and Wednesday. "
  "Either Q is on Tuesday (History Monday, P) and S on Wednesday (Economy Tuesday, Q; S teaches Polity), or Q is on Wednesday (History Tuesday, S; Q teaches Polity) and S on Tuesday (Economy Monday, P). The full timetable is not fixed, but in both cases the subject left for T on Friday is Geography.",
  "R विज्ञान मंगलवार, बुधवार या गुरुवार को पढ़ाता है, और बुधवार राजव्यवस्था का है, इसलिए R मंगलवार या गुरुवार को है। यदि R मंगलवार को होता, तो Q बुधवार या गुरुवार को होता और इतिहास उससे एक दिन पहले -- मंगलवार (विज्ञान) या बुधवार (राजव्यवस्था) -- जो असंभव है। अतः R गुरुवार को है, और Q और S मंगलवार और बुधवार को पढ़ाते हैं। "
  "या तो Q मंगलवार को है (इतिहास सोमवार, P) और S बुधवार को (अर्थव्यवस्था मंगलवार, Q; S राजव्यवस्था पढ़ाता है), या Q बुधवार को है (इतिहास मंगलवार, S; Q राजव्यवस्था पढ़ाता है) और S मंगलवार को (अर्थव्यवस्था सोमवार, P)। पूरी समय-सारणी तय नहीं होती, पर दोनों स्थितियों में शुक्रवार को T के लिए बचा विषय भूगोल है।",
  "lr-sa-five-teachers-with-two-timetables-open", pos=3, check=_sa3)

# 7 -- pointing to a photograph
def _br1():
    # the man M; his mother's only daughter is his sister Z; the woman W's mother is Z
    return "Niece"
T(LR, "Blood Relation", "medium",
  "Pointing to the man in a photograph, a woman says, 'His mother's only daughter is my mother.' How is the woman related to the man?",
  "एक तस्वीर में एक पुरुष की ओर इशारा करते हुए एक महिला कहती है, 'इनकी माँ की इकलौती बेटी मेरी माँ है।' वह महिला उस पुरुष की क्या लगती है?",
  ["Niece", "Daughter", "Sister", "Cousin"], ["भांजी", "पुत्री", "बहन", "ममेरी बहन"], 0,
  "The man's mother's only daughter is the man's sister, since he himself is a son. That sister is the woman's mother, so the woman is the daughter of the man's sister -- his niece, and he is her maternal uncle. "
  "She would be his daughter only if the speaker's mother were his wife, and his sister only if 'my mother' were their common mother; 'cousin' would need one more generation sideways.",
  "पुरुष की माँ की इकलौती बेटी पुरुष की बहन है, क्योंकि वह स्वयं बेटा है। वही बहन महिला की माँ है, इसलिए महिला पुरुष की बहन की बेटी है -- उसकी भांजी, और वह उसका मामा है। "
  "वह उसकी पुत्री तभी होती जब बोलने वाली की माँ उसकी पत्नी होती, और बहन तभी जब 'मेरी माँ' दोनों की साझी माँ होती; 'ममेरी बहन' के लिए एक पीढ़ी और बग़ल में जाना पड़ता।",
  "lr-br-a-woman-pointing-to-a-photograph", pos=0, check=_br1)

# 8 -- two fathers, two sons and a grandfather: the fewest people
def _br2():
    # a family as a set of father -> son links along one male line; count roles for chains of length n
    for n in range(1, 8):
        fathers, sons = n - 1, n - 1           # in a line of n males, everyone but the last is a father, everyone but the first a son
        grandfathers = max(0, n - 2)
        if fathers >= 2 and sons >= 2 and grandfathers >= 1:
            return str(n)
N(LR, "Blood Relation", "medium",
  "A family has two fathers, two sons and one grandfather among its members, and no other relationships are stated. What is the least number of people the family can have?",
  "एक परिवार के सदस्यों में दो पिता, दो पुत्र और एक दादा हैं, और कोई अन्य संबंध नहीं बताया गया है। परिवार में कम से कम कितने व्यक्ति हो सकते हैं?",
  ["3", "4", "5", "6"], 0,
  "One person can hold several roles. In a line of three men -- grandfather, father and son -- the grandfather and the father are both fathers, the father and the son are both sons, and the grandfather is the one grandfather: two fathers, two sons and one grandfather with only three people. "
  "Two people cannot be enough, since a grandfather needs a grandson two generations below him. 4, 5 and 6 count each role as a separate person.",
  "एक व्यक्ति कई भूमिकाएँ निभा सकता है। तीन पुरुषों की एक पंक्ति में -- दादा, पिता और पुत्र -- दादा और पिता दोनों पिता हैं, पिता और पुत्र दोनों पुत्र हैं, और दादा अकेला दादा है: केवल तीन व्यक्तियों में दो पिता, दो पुत्र और एक दादा। "
  "दो व्यक्ति पर्याप्त नहीं हो सकते, क्योंकि दादा के लिए उससे दो पीढ़ी नीचे एक पोता चाहिए। 4, 5 और 6 हर भूमिका को अलग व्यक्ति गिनते हैं।",
  "lr-br-the-fewest-people-for-two-fathers-and-two-sons", _br2)

# 9 -- a walk with three left turns
def _dd1():
    x, y, h = 0, 0, (1, 0)                     # start at P facing east
    q = None
    for k, (dist, turn) in enumerate([(4, None), (3, "L"), (4, "L"), (6, "L")]):
        if turn == "L":
            h = (-h[1], h[0])
        x, y = x + dist * h[0], y + dist * h[1]
        if k == 0:
            q = (x, y)
    dx, dy = x - q[0], y - q[1]
    assert (dx, dy) == (-4, -3)
    return f"{int((dx * dx + dy * dy) ** 0.5)} km, south-west"
T(LR, "Direction & Distance", "medium",
  "A person starts from village P and walks 4 km east to village Q. There the person turns left and walks 3 km to village R, turns left again and walks 4 km to village S, and turns left once more and walks 6 km to village T. How far is T from Q, and in which direction?",
  "एक व्यक्ति गाँव P से चलकर 4 किमी पूर्व में गाँव Q पहुँचता है। वहाँ वह बाएँ मुड़कर 3 किमी चलकर गाँव R पहुँचता है, फिर बाएँ मुड़कर 4 किमी चलकर गाँव S, और एक बार फिर बाएँ मुड़कर 6 किमी चलकर गाँव T पहुँचता है। T, Q से कितनी दूर है और किस दिशा में?",
  ["3 km, south", "5 km, north-west", "7 km, south-west", "5 km, south-west"],
  ["3 किमी, दक्षिण", "5 किमी, उत्तर-पश्चिम", "7 किमी, दक्षिण-पश्चिम", "5 किमी, दक्षिण-पश्चिम"], 3,
  "Facing east at Q, a left turn means north, so R is 3 km north of Q; the next left turn means west, so S is 4 km west of R, directly north of P; the third left turn means south, so T is 6 km south of S -- 3 km south of P. "
  "From Q, T is 4 km west and 3 km south: √(4² + 3²) = 5 km, to the south-west. 3 km south is T's position from P, not from Q; north-west reverses the north-south part; 7 km adds the two legs instead of combining them.",
  "Q पर पूर्व की ओर मुँह होने से बाएँ मुड़ने का अर्थ उत्तर है, इसलिए R, Q से 3 किमी उत्तर में है; अगला बाएँ मोड़ पश्चिम है, इसलिए S, R से 4 किमी पश्चिम में, P के ठीक उत्तर में है; तीसरा बाएँ मोड़ दक्षिण है, इसलिए T, S से 6 किमी दक्षिण में -- P से 3 किमी दक्षिण में है। "
  "Q से T, 4 किमी पश्चिम और 3 किमी दक्षिण है: √(4² + 3²) = 5 किमी, दक्षिण-पश्चिम में। 3 किमी दक्षिण T की स्थिति P से है, Q से नहीं; उत्तर-पश्चिम उत्तर-दक्षिण भाग को उलट देता है; 7 किमी दोनों भागों को मिलाने के बजाय जोड़ देता है।",
  "lr-dd-a-walk-with-three-left-turns", pos=3, check=_dd1)

# 10 -- three villages placed by diagonal directions alone
def _dd2():
    a = 3                                    # any positive distance gives the same answer
    q, p, r = (0, 0), (-a, a), (-a, -a)      # P north-west of Q, R south-west of Q, P due north of R
    mid = ((p[0] + r[0]) / 2, (p[1] + r[1]) / 2)
    dx, dy = q[0] - mid[0], q[1] - mid[1]
    assert dx > 0 and dy == 0
    return "East"
N(LR, "Direction & Distance", "easy",
  "Village P is to the north-west of village Q, and village R is to the south-west of Q. P is due north of R. In which direction is Q from the point midway between P and R?",
  "गाँव P, गाँव Q के उत्तर-पश्चिम में है, और गाँव R, Q के दक्षिण-पश्चिम में। P, R के ठीक उत्तर में है। P और R के ठीक बीच वाले बिंदु से Q किस दिशा में है?",
  ["East", "West", "North-east", "South-east"], 0,
  "Put Q at the centre. North-west of Q means as far west as north, and south-west means as far west as south; since P is due north of R, the two are equally far west of Q, so P is as far north of Q as R is south of it. "
  "The point midway between P and R is then level with Q and to its west, so Q is due east of it. North-east and south-east would need the midpoint to lie south or north of Q; west turns the answer round.",
  "Q को केंद्र में रखिए। Q के उत्तर-पश्चिम का अर्थ है जितना पश्चिम उतना उत्तर, और दक्षिण-पश्चिम का अर्थ जितना पश्चिम उतना दक्षिण; चूँकि P, R के ठीक उत्तर में है, दोनों Q से समान दूरी पर पश्चिम में हैं, इसलिए P, Q से जितना उत्तर में है R उतना ही दक्षिण में। "
  "तब P और R के बीच का बिंदु Q की सीध में और उसके पश्चिम में है, इसलिए Q उसके ठीक पूर्व में है। उत्तर-पूर्व और दक्षिण-पूर्व के लिए बीच के बिंदु को Q के दक्षिण या उत्तर में होना पड़ता; पश्चिम उत्तर को उलट देता है।",
  "lr-dd-three-villages-placed-by-diagonal-directions", _dd2, opts_hi=["पूर्व", "पश्चिम", "उत्तर-पूर्व", "दक्षिण-पूर्व"])

# 11 -- a code read off a 5 x 5 grid of letters
def _cd1():
    ex = {"CAB": "13 11 12", "FIG": "21 24 22", "KEY": "31 15 55"}
    fits = []
    for w in range(3, 9):
        for transpose in (False, True):
            def code(word):
                out = []
                for ch in word:
                    n = ord(ch) - 65
                    r, cc = n // w + 1, n % w + 1
                    out.append(f"{cc}{r}" if transpose else f"{r}{cc}")
                return " ".join(out)
            if all(code(k) == v for k, v in ex.items()):
                fits.append(code("LOW"))
    assert len(set(fits)) == 1, fits
    return fits[0]
N(LR, "Coding-Decoding", "medium",
  "In a certain code, CAB is written as 13 11 12, FIG as 21 24 22 and KEY as 31 15 55. How is LOW written in that code?",
  "एक निश्चित कूट में CAB को 13 11 12, FIG को 21 24 22 और KEY को 31 15 55 लिखा जाता है। उस कूट में LOW को कैसे लिखा जाएगा?",
  ["12 15 23", "32 35 53", "32 35 54", "35 32 53"], 1,
  "The letters A to Y are written row by row in a 5 × 5 grid -- A to E in row 1, F to J in row 2, K to O in row 3, and so on -- and each letter becomes its row number followed by its column number: C = 13, F = 21, K = 31, Y = 55. "
  "L is in row 3, column 2 (32); O in row 3, column 5 (35); W in row 5, column 3 (53). So LOW is 32 35 53. 12 15 23 gives the letters' places in the alphabet; 32 35 54 is off by one column for W; 35 32 53 swaps the codes of L and O.",
  "अक्षर A से Y एक 5 × 5 जाल में पंक्ति-दर-पंक्ति लिखे गए हैं -- पंक्ति 1 में A से E, पंक्ति 2 में F से J, पंक्ति 3 में K से O, इत्यादि -- और हर अक्षर अपनी पंक्ति संख्या के बाद स्तंभ संख्या बन जाता है: C = 13, F = 21, K = 31, Y = 55। "
  "L पंक्ति 3, स्तंभ 2 (32) में है; O पंक्ति 3, स्तंभ 5 (35) में; W पंक्ति 5, स्तंभ 3 (53) में। अतः LOW = 32 35 53। 12 15 23 अक्षरों का वर्णमाला में स्थान देता है; 32 35 54 में W का स्तंभ एक से खिसका है; 35 32 53, L और O के कूट उलट देता है।",
  "lr-cd-a-code-read-off-a-five-by-five-grid", _cd1)

# 12 -- a rule found from three examples
def _cd2():
    ex = [(2, 3, 10), (4, 5, 36), (6, 7, 78)]
    answers = set()
    R = range(-3, 4)
    for p, q, r, s, t, u in product(R, R, R, R, R, R):
        f = lambda a, b: p * a * a + q * b * b + r * a * b + s * a + t * b + u
        if all(f(a, b) == v for a, b, v in ex):
            answers.add(f(8, 9))
    assert answers == {136}, answers
    return "136"
N(LR, "Coding-Decoding", "hard",
  "If 2 # 3 = 10, 4 # 5 = 36 and 6 # 7 = 78, what is the value of 8 # 9?",
  "यदि 2 # 3 = 10, 4 # 5 = 36 और 6 # 7 = 78, तो 8 # 9 का मान क्या है?",
  ["128", "136", "144", "145"], 1,
  "In each example a # b = a × (a + b): 2 × 5 = 10, 4 × 9 = 36 and 6 × 13 = 78. So 8 # 9 = 8 × 17 = 136. The same answer comes from a² + ab, the same rule written out; any rule built from a², b², ab, a, b and a constant that fits all three examples gives 136. "
  "144 = 8 × 18 and 128 = 8 × 16 miss the sum a + b by one; 145 = 8² + 9² is the sum of the squares, which gives 13, 41 and 85 for the examples.",
  "हर उदाहरण में a # b = a × (a + b): 2 × 5 = 10, 4 × 9 = 36 और 6 × 13 = 78। अतः 8 # 9 = 8 × 17 = 136। यही उत्तर a² + ab से भी आता है, जो इसी नियम का विस्तार है; a², b², ab, a, b और एक अचर से बना कोई भी नियम जो तीनों उदाहरणों पर ठीक बैठे, 136 देता है। "
  "144 = 8 × 18 और 128 = 8 × 16, योग a + b में एक से चूकते हैं; 145 = 8² + 9² वर्गों का योग है, जो उदाहरणों के लिए 13, 41 और 85 देता है।",
  "lr-cd-a-rule-found-from-three-examples", _cd2)

# 13 -- six colours on a cube's faces
def _cp1():
    # faces: 0 top, 1 bottom, 2 front, 3 back, 4 left, 5 right; a rotation maps the colour on face i to face g[i]
    turn_v = (0, 1, 5, 4, 2, 3)              # about the vertical axis: front -> right -> back -> left -> front
    turn_h = (2, 3, 1, 0, 4, 5)              # about the left-right axis: top -> front -> bottom -> back -> top
    group, frontier = {tuple(range(6))}, [tuple(range(6))]
    while frontier:
        g = frontier.pop()
        for m in (turn_v, turn_h):
            h = tuple(m[g[i]] for i in range(6))
            if h not in group:
                group.add(h)
                frontier.append(h)
    assert len(group) == 24
    seen = set()
    for col in permutations(range(6)):
        seen.add(min(tuple(col[[g[i] for i in range(6)].index(k)] for k in range(6)) for g in group))
    return str(len(seen))
N(LR, "Cube Painting", "hard",
  "Each face of a cube is to be painted a different colour, using six given colours. How many different-looking cubes can be made? (Two cubes look the same if one can be turned so that it looks exactly like the other.)",
  "छह दिए गए रंगों का प्रयोग करके एक घन के हर फलक को अलग रंग से रँगना है। कितने अलग दिखने वाले घन बनाए जा सकते हैं? (दो घन एक जैसे दिखते हैं यदि एक को घुमाकर ठीक दूसरे जैसा बनाया जा सके।)",
  ["6", "24", "30", "720"], 2,
  "Turn any cube so that the first colour is at the bottom. Its top can then be any of the other 5 colours. The remaining 4 colours go round the sides, and since the cube can still be spun about its vertical axis, only their order round the ring matters: (4 - 1)! = 6 ways. "
  "So there are 5 × 6 = 30 different cubes. 720 = 6! counts every painting without allowing for turning the cube; 24 is the number of ways a cube can be turned; 6 is the number of colours.",
  "किसी भी घन को ऐसे घुमाइए कि पहला रंग नीचे हो। तब ऊपर शेष 5 रंगों में से कोई भी हो सकता है। बचे 4 रंग चारों ओर की भुजाओं पर जाते हैं, और चूँकि घन को अब भी अपनी ऊर्ध्व अक्ष पर घुमाया जा सकता है, केवल घेरे में उनका क्रम मायने रखता है: (4 - 1)! = 6 तरीक़े। "
  "अतः 5 × 6 = 30 अलग घन बनते हैं। 720 = 6! घन को घुमाने की छूट दिए बिना हर रँगाई गिनता है; 24 वह संख्या है जितने तरीक़ों से घन घुमाया जा सकता है; 6 रंगों की संख्या है।",
  "lr-cp-six-colours-on-a-cube-s-faces", _cp1)

# 14 -- pens, tools and toys
def _sy1():
    regions = list(product((0, 1), repeat=4))          # (pen, tool, toy, costly)
    follows = [True, True, True]
    for mask in range(1, 1 << 16):
        world = [r for k, r in enumerate(regions) if mask >> k & 1]
        if any(p and not t for p, t, y, cst in world): continue          # all pens are tools
        if not any(t and y for p, t, y, cst in world): continue          # some tools are toys
        if any(y and cst for p, t, y, cst in world): continue            # no toy is costly
        concl = [any(t and not cst for p, t, y, cst in world),
                 any(p and not cst for p, t, y, cst in world),
                 not any(p and y for p, t, y, cst in world)]
        follows = [f and k for f, k in zip(follows, concl)]
    return {(True, False, False): "1 only", (True, True, False): "1 and 2 only", (True, False, True): "1 and 3 only",
            (False, False, False): "None of the above"}[tuple(follows)]
SC(LR, "Syllogism", "medium",
   "Statements: All pens are tools. Some tools are toys. No toy is costly.\n\nWhich of the following conclusions follow(s) from the statements?",
   "कथन: सभी क़लमें औज़ार हैं। कुछ औज़ार खिलौने हैं। कोई भी खिलौना महँगा नहीं है।\n\nनिम्नलिखित में से कौन-सा/से निष्कर्ष कथनों से निकलता/निकलते है/हैं?",
   ["Some tools are not costly.", "Some pens are not costly.", "No pen is a toy."],
   ["कुछ औज़ार महँगे नहीं हैं।", "कुछ क़लमें महँगी नहीं हैं।", "कोई भी क़लम खिलौना नहीं है।"],
   ["1 only", "1 and 2 only", "1 and 3 only", "None of the above"], 0,
   "1 follows: some tools are toys, and no toy is costly, so those tools are not costly. 2 does not follow: the tools that are toys need not include any pen, and every pen may be one of the costly tools. "
   "3 does not follow either: nothing rules out a pen that is also a toy, since pens are tools and some tools are toys. Only 1 follows.",
   "1 निकलता है: कुछ औज़ार खिलौने हैं, और कोई खिलौना महँगा नहीं है, इसलिए वे औज़ार महँगे नहीं हैं। 2 नहीं निकलता: जो औज़ार खिलौने हैं उनमें कोई क़लम होना ज़रूरी नहीं, और हर क़लम महँगे औज़ारों में से हो सकती है। "
   "3 भी नहीं निकलता: कुछ भी ऐसी क़लम को नहीं रोकता जो खिलौना भी हो, क्योंकि क़लमें औज़ार हैं और कुछ औज़ार खिलौने हैं। केवल 1 निकलता है।",
   "lr-sy-pens-tools-and-toys", check=_sy1)

# 15 -- a speaker who says 'either I am a liar or ...'
def _tl1():
    sols = []
    for a_, b_, c_ in product("TL", repeat=3):
        says_a = a_ == "L" or b_ == "T"          # 'Either I am a liar or B is a truth-teller.'
        says_b = c_ == "L"                       # 'C is a liar.'
        if says_a == (a_ == "T") and says_b == (b_ == "T"):
            sols.append((a_, b_, c_))
    assert sols == [("T", "T", "L")], sols
    return "A and B are truth-tellers, and C is a liar."
T(LR, "Truth-Liar", "hard",
  "On an island every inhabitant is either a truth-teller, who always tells the truth, or a liar, who always lies. A visitor meets three inhabitants, A, B and C. A says, 'Either I am a liar or B is a truth-teller.' B says, 'C is a liar.' Which one of the following is correct?",
  "एक द्वीप का हर निवासी या तो सत्यवादी है, जो हमेशा सच बोलता है, या झूठा, जो हमेशा झूठ बोलता है। एक आगंतुक तीन निवासियों A, B और C से मिलता है। A कहता है, 'या तो मैं झूठा हूँ या B सत्यवादी है।' B कहता है, 'C झूठा है।' निम्नलिखित में से कौन-सा सही है?",
  ["A and B are truth-tellers, and C is a liar.", "A is a truth-teller, and B and C are liars.",
   "A is a liar, B is a truth-teller and C is a liar.", "The three cannot all be classified from what they say."],
  ["A और B सत्यवादी हैं, और C झूठा है।", "A सत्यवादी है, और B तथा C झूठे हैं।",
   "A झूठा है, B सत्यवादी है और C झूठा है।", "उनके कथनों से तीनों को वर्गीकृत नहीं किया जा सकता।"], 0,
  "Suppose A is a liar. Then 'either I am a liar or B is a truth-teller' is true, because its first part is true -- but a liar cannot say something true. So A is a truth-teller, and his statement is true; since he is not a liar, its second part must hold: B is a truth-teller. "
  "B's statement is then true, so C is a liar. Everything is fixed: A and B tell the truth and C lies. The options that make A a liar, or B a liar, fail at the first step, and since every person is fixed, the claim that they cannot all be classified is wrong.",
  "मान लीजिए A झूठा है। तब 'या तो मैं झूठा हूँ या B सत्यवादी है' सत्य हो जाता है, क्योंकि उसका पहला भाग सत्य है -- पर झूठा कोई सत्य बात नहीं कह सकता। अतः A सत्यवादी है, और उसका कथन सत्य है; चूँकि वह झूठा नहीं है, कथन का दूसरा भाग सत्य होना चाहिए: B सत्यवादी है। "
  "तब B का कथन सत्य है, इसलिए C झूठा है। सब कुछ तय है: A और B सच बोलते हैं और C झूठ। A को या B को झूठा बनाने वाले विकल्प पहले ही चरण में विफल होते हैं, और चूँकि हर व्यक्ति तय है, यह दावा ग़लत है कि तीनों को वर्गीकृत नहीं किया जा सकता।",
  "lr-tl-either-i-am-a-liar-or", pos=3, check=_tl1)

# ---- the data-sufficiency block's three Reasoning items
def _ds1():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    thirty = {"Apr", "Jun", "Sep", "Nov"}
    s1 = [m for i, m in enumerate(months) if 4 < i < 8]
    s2 = [m for m in months if m in thirty]
    both = [m for m in s1 if m in thirty]
    assert both == ["Jun"]
    return _ds(s1, s2, both)
DS(LR, "medium",
   "In which month is Priya's birthday?",
   "प्रिया का जन्मदिन किस महीने में है?",
   "It falls after May but before September.", "वह मई के बाद पर सितंबर से पहले पड़ता है।",
   "It falls in a month that has 30 days.", "वह ऐसे महीने में पड़ता है जिसमें 30 दिन होते हैं।",
   2,
   "Statement I leaves June, July and August. Statement II leaves April, June, September and November. Neither alone fixes the month, but together only June is left. Both statements are needed.",
   "कथन I से जून, जुलाई और अगस्त बचते हैं। कथन II से अप्रैल, जून, सितंबर और नवंबर बचते हैं। कोई भी अकेला महीना तय नहीं करता, पर दोनों साथ लेने पर केवल जून बचता है। दोनों कथन ज़रूरी हैं।",
   "lr-ds-the-month-of-a-birthday", _ds1)

def _ds2():
    worlds = [(sc, m) for sc in product(range(6), repeat=3) for m in range(6)]
    passed = lambda sc, m: all(x >= m for x in sc)
    s1 = {passed(sc, m) for sc, m in worlds if sum(x >= m for x in sc) >= 2}
    s2 = {passed(sc, m) for sc, m in worlds if min(sc) >= m}
    both = {passed(sc, m) for sc, m in worlds if sum(x >= m for x in sc) >= 2 and min(sc) >= m}
    assert s1 == {True, False} and s2 == {True}
    return _ds(s1, s2, both)
DS(LR, "hard",
   "Three candidates took a test, and a candidate passes if and only if the score is at least the pass mark. Did all three candidates pass?",
   "तीन उम्मीदवारों ने एक परीक्षा दी, और कोई उम्मीदवार तभी और केवल तभी उत्तीर्ण होता है जब उसके अंक उत्तीर्णांक के बराबर या उससे अधिक हों। क्या तीनों उम्मीदवार उत्तीर्ण हुए?",
   "At least two of them passed.", "उनमें से कम से कम दो उत्तीर्ण हुए।",
   "The candidate with the lowest score passed.", "सबसे कम अंक वाला उम्मीदवार उत्तीर्ण हुआ।",
   0,
   "Statement I allows either two or three passes, so it does not settle the question. Statement II settles it alone: every candidate scored at least as much as the lowest scorer, who reached the pass mark, so all three passed. "
   "So one statement alone is sufficient and the other is not.",
   "कथन I दो या तीन, दोनों के उत्तीर्ण होने की अनुमति देता है, इसलिए प्रश्न तय नहीं करता। कथन II अकेला इसे तय करता है: हर उम्मीदवार के अंक कम से कम सबसे कम अंक वाले जितने हैं, जो उत्तीर्णांक तक पहुँचा, इसलिए तीनों उत्तीर्ण हुए। "
   "अतः एक कथन अकेला पर्याप्त है और दूसरा नहीं।",
   "lr-ds-whether-everyone-passed", _ds2)

def _ds3():
    s1 = {b for b in range(0, 26) for total in range(55 - b, 200)}          # I: 30 chess, 25 carrom; the club size is open
    s2 = {b for b in range(0, 51)}                                          # II: 50 members; the games are open
    both = {b for b in range(0, 26) if 55 - b <= 50}                         # both: at least 5, at most 25
    assert both == set(range(5, 26))
    return _ds(s1, s2, both)
DS(LR, "medium",
   "How many members of a club play both chess and carrom?",
   "एक क्लब के कितने सदस्य शतरंज और कैरम दोनों खेलते हैं?",
   "30 members play chess and 25 members play carrom.", "30 सदस्य शतरंज खेलते हैं और 25 सदस्य कैरम।",
   "The club has 50 members.", "क्लब में 50 सदस्य हैं।",
   3,
   "Even together the statements do not fix the number. If every member played at least one of the two games, 30 + 25 - 50 = 5 would play both; but nothing says that every member plays a game, and the number could be anything from 5 to 25 "
   "(25 if every carrom player also plays chess, leaving 20 members who play neither). The question cannot be answered even with both statements.",
   "दोनों कथन मिलकर भी संख्या तय नहीं करते। यदि हर सदस्य दोनों में से कम से कम एक खेल खेलता, तो 30 + 25 - 50 = 5 दोनों खेलते; पर कहीं नहीं कहा गया कि हर सदस्य कोई खेल खेलता है, और संख्या 5 से 25 तक कुछ भी हो सकती है "
   "(25 यदि हर कैरम खिलाड़ी शतरंज भी खेले, जिससे 20 सदस्य कोई खेल न खेलें)। दोनों कथनों के साथ भी प्रश्न का उत्तर नहीं दिया जा सकता।",
   "lr-ds-two-games-in-one-club", _ds3)
