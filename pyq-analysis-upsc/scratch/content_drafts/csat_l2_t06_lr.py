# -*- coding: utf-8 -*-
"""CSAT Level 2 · Test 6 -- Logical Reasoning (18 items: 15 in the Reasoning slots, 3 in the data-sufficiency block).

Same mix as Tests 1-5 with new traps: an assumption behind a council's decision, a course of action that neither
follows, a rise in a share read as a rise in a number, a 3 × 3 block of seats, the order of speakers, a committee
under four conditions, a father's sister's daughter, the only daughter-in-law of a grandfather, a diagonal that
makes a direction exact, two diagonals that make a due-south, letters with the ends exchanged, a code whose rule
depends on whether a word has an odd or even number of letters (three examples, because two leave other rules
open), unpainted faces of a cut cube, four syllogistic conclusions, and a truth-teller, a liar and a trickster;
in the data-sufficiency block, a highest scorer, an eldest of three, and a direction built from two legs.
Difficulty 3 easy / 10 medium / 5 hard. Arrangement, code, cube, syllogism and truth-teller keys are found by
checking every case."""
from fractions import Fraction as F
from itertools import permutations, product
import csat_common as c
from csat_common import N, T, S2, SC, DS, LR

def _two(one, two):
    return c.T2R[{(True, False): 0, (False, True): 1, (True, True): 2, (False, False): 3}[(one, two)]]

def _ds(s1, s2, both):
    alone = (len(set(s1)) == 1, len(set(s2)) == 1)
    return "b" if all(alone) else "a" if any(alone) else "c" if len(set(both)) == 1 else "d"

CONC = "Which of the following conclusions follow(s) from the statement?"
CONC_HI = "निम्नलिखित में से कौन-सा/से निष्कर्ष कथन से निकलता/निकलते है/हैं?"
ASSUMPT = "Which of the following assumptions is/are implicit in the statement?"
ASSUMPT_HI = "निम्नलिखित में से कौन-सी/से पूर्वधारणा/एँ कथन में अंतर्निहित है/हैं?"
ACTION = "Which of the following courses of action logically follow(s)?"
ACTION_HI = "निम्नलिखित में से कौन-सी कार्यवाही/कार्यवाहियाँ तार्किक रूप से अनुसरणीय है/हैं?"

# 1 -- an assumption behind a council's decision
S2(LR, "Statement-Conclusion/Assumption", "easy",
   "Statement: A town council has decided to plant trees along both sides of the town's main road.\n\n" + ASSUMPT,
   "कथन: एक नगर परिषद ने कस्बे की मुख्य सड़क के दोनों ओर पेड़ लगाने का निर्णय लिया है।\n\n" + ASSUMPT_HI,
   ["The main road is the only road in the town.", "Trees along a road can make it cooler and cleaner."],
   ["मुख्य सड़क कस्बे की एकमात्र सड़क है।", "सड़क के किनारे लगे पेड़ उसे अधिक ठंडा और स्वच्छ बना सकते हैं।"], 1,
   "Only II is implicit: a council plants trees along a road because it believes that they will make the road cooler and cleaner; without that belief the decision has no point. "
   "I is not assumed: the decision is about the main road, and it makes sense whether or not the town has other roads.",
   "केवल II अंतर्निहित है: परिषद सड़क के किनारे पेड़ इसलिए लगाती है कि उसे विश्वास है कि वे सड़क को अधिक ठंडा और स्वच्छ बनाएँगे; इस विश्वास के बिना निर्णय का कोई अर्थ नहीं। "
   "I पूर्वधारणा नहीं है: निर्णय मुख्य सड़क के बारे में है, और यह इस बात से स्वतंत्र है कि कस्बे में और सड़कें हैं या नहीं।",
   "lr-sc-trees-along-the-main-road", roman=True)

# 2 -- a course of action that neither follows
S2(LR, "Statement-Conclusion/Assumption", "medium",
   "Statement: The number of students who failed in Mathematics in this year's board examination has risen sharply.\n\n" + ACTION,
   "कथन: इस वर्ष की बोर्ड परीक्षा में गणित में अनुत्तीर्ण होने वाले विद्यार्थियों की संख्या में तेज़ वृद्धि हुई है।\n\n" + ACTION_HI,
   ["Mathematics should be removed from the list of compulsory subjects.", "All the Mathematics teachers in the State should be dismissed."],
   ["गणित को अनिवार्य विषयों की सूची से हटा देना चाहिए।", "राज्य के सभी गणित शिक्षकों को बर्ख़ास्त कर देना चाहिए।"], 3,
   "Neither follows. Dropping a subject because more students failed it does not deal with the cause of the failures and would only lower the standard; dismissing every Mathematics teacher is out of all proportion to the evidence, "
   "which says nothing about how well they teach. A sensible course of action would first look into the reasons -- the paper, the teaching, the preparation -- before changing anything.",
   "कोई भी अनुसरणीय नहीं है। अधिक विद्यार्थी अनुत्तीर्ण हुए, इसलिए विषय को हटा देना अनुत्तीर्णता के कारण को नहीं सुलझाता और केवल स्तर गिराएगा; हर गणित शिक्षक को बर्ख़ास्त करना प्रमाण के अनुपात से कहीं बाहर है, "
   "जो इस बारे में कुछ नहीं कहता कि वे कितना अच्छा पढ़ाते हैं। उचित कार्यवाही पहले कारणों की जाँच करती -- प्रश्नपत्र, शिक्षण, तैयारी -- और तब कुछ बदलती।",
   "lr-sc-failures-in-mathematics-course-of-action", roman=True)

# 3 -- a rise in a share is not a rise in a number
def _sc3():
    total0, total1 = 100, 120                       # the number of Class XI students rose by 20 per cent
    sci0, sci1 = F(40, 100) * total0, F(55, 100) * total1
    non0, non1 = total0 - sci0, total1 - sci1
    return _two(sci1 / sci0 > F(3, 2), non1 < non0)
S2(LR, "Statement-Conclusion/Assumption", "hard",
   "Statement: In a State, the share of Class XI students who take science rose from 40 per cent to 55 per cent over ten years, while the total number of Class XI students rose by 20 per cent.\n\n" + CONC,
   "कथन: एक राज्य में दस वर्षों में कक्षा XI के विज्ञान लेने वाले विद्यार्थियों का अनुपात 40 प्रतिशत से बढ़कर 55 प्रतिशत हो गया, जबकि कक्षा XI के कुल विद्यार्थियों की संख्या 20 प्रतिशत बढ़ी।\n\n" + CONC_HI,
   ["The number of students taking science rose by more than 50 per cent.", "The number of students not taking science fell."],
   ["विज्ञान लेने वाले विद्यार्थियों की संख्या 50 प्रतिशत से अधिक बढ़ी।", "विज्ञान न लेने वाले विद्यार्थियों की संख्या घटी।"], 2,
   "Take 100 students at the start: 40 take science and 60 do not. Ten years later there are 120 students, of whom 55% = 66 take science and 54 do not. "
   "The number taking science has risen from 40 to 66, an increase of 65%, which is more than 50% (I), and the number not taking science has fallen from 60 to 54 (II). Both follow. "
   "The trap is to read the rise in the share, 15 percentage points, as if it were the rise in the number.",
   "शुरू में 100 विद्यार्थी मानिए: 40 विज्ञान लेते हैं और 60 नहीं। दस वर्ष बाद 120 विद्यार्थी हैं, जिनमें से 55% = 66 विज्ञान लेते हैं और 54 नहीं। "
   "विज्ञान लेने वालों की संख्या 40 से बढ़कर 66 हो गई, यानी 65% की वृद्धि, जो 50% से अधिक है (I), और विज्ञान न लेने वालों की संख्या 60 से घटकर 54 रह गई (II)। दोनों निकलते हैं। "
   "जाल अनुपात की वृद्धि, 15 प्रतिशत बिंदु, को संख्या की वृद्धि समझ लेना है।",
   "lr-sc-share-up-number-up", roman=True, check=_sc3)

# 4 -- a 3 x 3 block of seats
def _sa1():
    cells = [(r, c_) for r in range(3) for c_ in range(3)]            # row 0 is the northern row, column 0 the western
    sols = []
    for perm in permutations("PQRSTUVWX"):
        pos = dict(zip(perm, cells))
        if pos["P"] != (0, 0) or pos["Q"] != (0, 1):
            continue
        if pos["R"] != (1, 1) or pos["S"] != (2, 2) or pos["V"] != (1, 2):
            continue
        if pos["T"] != (1, 0) or pos["U"] != (2, 0) or pos["W"][0] == 0:
            continue
        sols.append(pos)
    assert len(sols) == 1, sols
    south_of_r = (2, 1)
    return next(p for p, cell in sols[0].items() if cell == south_of_r)
T(LR, "Seating Arrangement", "medium",
  "Nine people -- P, Q, R, S, T, U, V, W and X -- sit in a 3 × 3 square block of seats, three rows of three, all facing north. P sits at the north-west corner and Q sits directly east of P. "
  "R sits directly south of Q. S sits at the south-east corner, and V sits directly north of S. T sits directly west of R, and U sits directly south of T. W does not sit in the northern row. Who sits directly south of R?",
  "नौ व्यक्ति -- P, Q, R, S, T, U, V, W और X -- तीन-तीन की तीन पंक्तियों वाले 3 × 3 के वर्गाकार सीट-खंड में, सभी उत्तर की ओर मुँह करके, बैठे हैं। P उत्तर-पश्चिमी कोने पर बैठा है और Q, P के ठीक पूर्व में। "
  "R, Q के ठीक दक्षिण में बैठा है। S दक्षिण-पूर्वी कोने पर बैठा है, और V, S के ठीक उत्तर में। T, R के ठीक पश्चिम में बैठा है, और U, T के ठीक दक्षिण में। W उत्तरी पंक्ति में नहीं बैठा है। R के ठीक दक्षिण में कौन बैठा है?",
  ["W", "T", "U", "X"], ["W", "T", "U", "X"], 0,
  "Number the rows from north to south and the columns from west to east. P is at the north-west corner and Q beside it, in the middle of the northern row; R, directly south of Q, is at the centre. S is at the south-east corner, so V, directly north of S, "
  "is in the middle of the eastern column. T, west of R, is in the middle of the western column and U, south of T, at the south-west corner. That leaves the north-east corner and the middle of the southern row for W and X; W is not in the northern row, "
  "so W sits in the middle of the southern row, directly south of R, and X at the north-east corner.",
  "पंक्तियों को उत्तर से दक्षिण और स्तंभों को पश्चिम से पूर्व गिनिए। P उत्तर-पश्चिमी कोने पर है और Q उसके बगल में, उत्तरी पंक्ति के बीच में; Q के ठीक दक्षिण में R केंद्र पर है। S दक्षिण-पूर्वी कोने पर है, इसलिए S के ठीक उत्तर में V "
  "पूर्वी स्तंभ के बीच में है। R के पश्चिम में T पश्चिमी स्तंभ के बीच में है और T के दक्षिण में U दक्षिण-पश्चिमी कोने पर। इस प्रकार W और X के लिए उत्तर-पूर्वी कोना और दक्षिणी पंक्ति का बीच बचता है; W उत्तरी पंक्ति में नहीं है, "
  "इसलिए W दक्षिणी पंक्ति के बीच में, R के ठीक दक्षिण में, बैठता है और X उत्तर-पूर्वी कोने पर।",
  "lr-sa-three-by-three-block-of-seats", pos=0, check=_sa1)

# 5 -- the order of speakers
def _sa2():
    sols = []
    for rest in permutations("ABDE"):
        order = ("C",) + rest
        i = {p: k for k, p in enumerate(order)}
        if i["A"] < i["B"] and i["D"] == i["B"] + 1 and i["E"] > i["D"]:
            sols.append(order)
    assert len(sols) == 1, sols
    return sols[0][2]
T(LR, "Seating Arrangement", "easy",
  "Five speakers -- A, B, C, D and E -- address a meeting one after another, each speaking once. C speaks first. A speaks before B, and B speaks immediately before D. E speaks after D. Who speaks third?",
  "पाँच वक्ता -- A, B, C, D और E -- एक सभा को एक के बाद एक संबोधित करते हैं, हर एक एक बार बोलता है। C सबसे पहले बोलता है। A, B से पहले बोलता है, और B, D से ठीक पहले। E, D के बाद बोलता है। तीसरे स्थान पर कौन बोलता है?",
  ["B", "A", "D", "E"], ["B", "A", "D", "E"], 0,
  "C is first. A must come before B, and B must be immediately followed by D, with E after D. The only order that meets all of these is C, A, B, D, E, so the third speaker is B. "
  "A is second, D fourth and E last.",
  "C पहले है। A, B से पहले होना चाहिए, और B के ठीक बाद D, तथा D के बाद E। सभी शर्तें पूरी करने वाला एकमात्र क्रम C, A, B, D, E है, इसलिए तीसरा वक्ता B है। "
  "A दूसरा, D चौथा और E अंतिम है।",
  "lr-sa-order-of-speakers", pos=3, check=_sa2)

# 6 -- a committee under four conditions
def _sa3():
    def ok(team):
        t = set(team)
        return not ("P" in t and "Q" in t) and ("R" not in t or "S" in t) and ("T" not in t or "P" in t) and not ("S" in t and "U" in t)
    opts = ["P, Q, U", "P, S, T", "Q, T, U", "R, S, U"]
    good = [o for o in opts if ok(o.split(", "))]
    assert good == ["P, S, T"]
    return good[0]
N(LR, "Seating Arrangement", "medium",
  "A committee of three is to be chosen from six people -- P, Q, R, S, T and U -- subject to these conditions: P and Q cannot both be chosen; R can be chosen only if S is chosen; T can be chosen only if P is chosen; S and U cannot both be chosen. "
  "Which one of the following can be the committee?",
  "छह व्यक्तियों -- P, Q, R, S, T और U -- में से तीन की एक समिति इन शर्तों के अधीन चुनी जानी है: P और Q दोनों नहीं चुने जा सकते; R तभी चुना जा सकता है जब S चुना गया हो; T तभी चुना जा सकता है जब P चुना गया हो; S और U दोनों नहीं चुने जा सकते। "
  "निम्नलिखित में से कौन-सी समिति बन सकती है?",
  ["P, Q, U", "P, S, T", "Q, T, U", "R, S, U"], 1,
  "Check each option against the four conditions. P, Q, U has both P and Q. Q, T, U has T without P. R, S, U has both S and U. P, S, T breaks none of them: T is accompanied by P, there is no R, and S is not with U, nor is P with Q. "
  "So it is the only committee that can be formed from the options.",
  "हर विकल्प को चारों शर्तों पर जाँचिए। P, Q, U में P और Q दोनों हैं। Q, T, U में P के बिना T है। R, S, U में S और U दोनों हैं। P, S, T इनमें से कोई शर्त नहीं तोड़ता: T के साथ P है, R नहीं है, S के साथ U नहीं है, और P के साथ Q नहीं है। "
  "अतः विकल्पों में यही एकमात्र समिति है जो बन सकती है।",
  "lr-sa-a-committee-under-four-conditions", _sa3)

# 7 -- a father's sister's daughter
T(LR, "Blood Relation", "easy",
  "Introducing a woman, a man says, 'Her mother is the only sister of my father.' How is the woman related to the man?",
  "एक महिला का परिचय देते हुए एक पुरुष कहता है, 'इसकी माँ मेरे पिता की इकलौती बहन है।' वह महिला उस पुरुष की क्या लगती है?",
  ["Cousin", "Sister", "Niece", "Aunt"], ["फुफेरी बहन", "बहन", "भतीजी", "बुआ"], 0,
  "The woman's mother is the only sister of the man's father: the man's aunt on the father's side (बुआ). The woman is that aunt's daughter, so she is the man's cousin (फुफेरी बहन). "
  "'Sister' would need the same parents; 'niece' would be the daughter of the man's brother or sister; 'aunt' is the woman's mother's relation to the man, not hers.",
  "महिला की माँ पुरुष के पिता की इकलौती बहन है: पुरुष की बुआ। महिला उसी बुआ की बेटी है, इसलिए वह पुरुष की फुफेरी बहन है। "
  "'बहन' के लिए माता-पिता एक होने चाहिए; 'भतीजी' पुरुष के भाई या बहन की बेटी होती; 'बुआ' महिला की माँ का पुरुष से संबंध है, महिला का नहीं।",
  "lr-br-father-s-sister-s-daughter", pos=0)

# 8 -- the only daughter-in-law of a grandfather
T(LR, "Blood Relation", "hard",
  "Pointing to a man, Seema says, 'He is the son of the only daughter-in-law of my father's father.' How is the man related to Seema?",
  "एक पुरुष की ओर इशारा करते हुए सीमा कहती है, 'वह मेरे पिता के पिता की इकलौती बहू का बेटा है।' वह पुरुष सीमा का क्या लगता है?",
  ["Brother", "Cousin", "Nephew", "Maternal uncle"], ["भाई", "चचेरा भाई", "भतीजा", "मामा"], 0,
  "Seema's father's father is her paternal grandfather. His only daughter-in-law must be the wife of Seema's father -- Seema's own mother. The man is her son, so he is Seema's brother. "
  "A cousin would be the child of an uncle or an aunt, not of Seema's own mother; a nephew would be the child of Seema's brother or sister; a maternal uncle would be her mother's brother.",
  "सीमा के पिता के पिता उसके दादा हैं। उनकी इकलौती बहू सीमा के पिता की पत्नी -- यानी सीमा की अपनी माँ -- ही हो सकती है। वह पुरुष उसी का बेटा है, इसलिए वह सीमा का भाई है। "
  "चचेरा भाई चाचा या बुआ का बच्चा होता, सीमा की अपनी माँ का नहीं; भतीजा सीमा के भाई या बहन का बच्चा होता; मामा उसकी माँ का भाई होता।",
  "lr-br-the-only-daughter-in-law-of-a-grandfather", pos=3)

# 9 -- a diagonal that makes the direction exact
def _dd1():
    q = (0, 0)
    p = (0, 4)
    r = (6, 0)
    t = (6, -2)
    dx, dy = t[0] - p[0], t[1] - p[1]
    assert abs(dx) == abs(dy)
    return {(1, -1): "South-east", (1, 1): "North-east", (-1, -1): "South-west", (-1, 1): "North-west"}[(dx // abs(dx), dy // abs(dy))]
T(LR, "Direction & Distance", "medium",
  "P is 4 m north of Q. R is 6 m east of Q. T is 2 m south of R. In which direction is T from P?",
  "P, Q से 4 मीटर उत्तर में है। R, Q से 6 मीटर पूर्व में है। T, R से 2 मीटर दक्षिण में है। T, P से किस दिशा में है?",
  ["South-east", "East", "South", "South-west"], ["दक्षिण-पूर्व", "पूर्व", "दक्षिण", "दक्षिण-पश्चिम"], 0,
  "Take Q as the starting point: P is 4 m north of it; R is 6 m east of it; T, 2 m south of R, is 6 m east and 2 m south of Q. From P, T is 6 m towards the east and 4 + 2 = 6 m towards the south. "
  "Equal distances to the east and the south make the direction exactly south-east. East would need T to be level with P, and south would need T to lie on P's north-south line.",
  "Q को आरंभ बिंदु मानिए: P उससे 4 मीटर उत्तर में है; R उससे 6 मीटर पूर्व में है; R से 2 मीटर दक्षिण में T, Q से 6 मीटर पूर्व और 2 मीटर दक्षिण में है। P से T पूर्व की ओर 6 मीटर और दक्षिण की ओर 4 + 2 = 6 मीटर है। "
  "पूर्व और दक्षिण की बराबर दूरियाँ दिशा को ठीक दक्षिण-पूर्व बनाती हैं। पूर्व के लिए T को P के समान स्तर पर होना होता, और दक्षिण के लिए T को P की उत्तर-दक्षिण रेखा पर।",
  "lr-dd-a-diagonal-that-makes-the-direction-exact", pos=2, check=_dd1)

# 10 -- two diagonals that make a due-south
def _dd2():
    school = (0, 0)
    temple = (1, 1)                    # 2 km north-east: equal east and north components
    market = (1, -1)                   # 2 km south-east: equal east and south components
    dx, dy = market[0] - temple[0], market[1] - temple[1]
    assert dx == 0 and dy < 0
    return "South"
T(LR, "Direction & Distance", "medium",
  "The temple is 2 km north-east of the school, and the market is 2 km south-east of the school. In which direction is the market from the temple?",
  "मंदिर विद्यालय से 2 किमी उत्तर-पूर्व में है, और बाज़ार विद्यालय से 2 किमी दक्षिण-पूर्व में। बाज़ार मंदिर से किस दिशा में है?",
  ["South", "North", "South-east", "West"], ["दक्षिण", "उत्तर", "दक्षिण-पूर्व", "पश्चिम"], 0,
  "Put the school at the centre. Going 2 km north-east takes the temple √2 km east and √2 km north of the school; going 2 km south-east takes the market √2 km east and √2 km south. "
  "The two are the same distance east of the school, so the market lies directly south of the temple, 2√2 km away. South-east would need the market to be further east than the temple.",
  "विद्यालय को केंद्र में रखिए। 2 किमी उत्तर-पूर्व जाने पर मंदिर विद्यालय से √2 किमी पूर्व और √2 किमी उत्तर में पहुँचता है; 2 किमी दक्षिण-पूर्व जाने पर बाज़ार √2 किमी पूर्व और √2 किमी दक्षिण में। "
  "दोनों विद्यालय से एक ही दूरी पूर्व में हैं, इसलिए बाज़ार मंदिर के ठीक दक्षिण में, 2√2 किमी दूर, है। दक्षिण-पूर्व के लिए बाज़ार को मंदिर से और पूर्व में होना होता।",
  "lr-dd-two-diagonals-that-make-a-due-south", pos=0, check=_dd2)

# 11 -- the ends exchanged, the middle moved forward
def _cd1():
    rule = lambda w: w[-1] + "".join(chr(ord(ch) + 1) for ch in w[1:-1]) + w[0]
    assert rule("STONE") == "EUPOS" and rule("BRAIN") == "NSBJB"
    mv = lambda w, k: "".join(chr((ord(ch) - 65 + k) % 26 + 65) for ch in w)
    assert mv("PLANT", 1) == "QMBOU"                                                                # shifted, ends not exchanged
    assert "PLANT"[-1] + mv("PLANT"[1:-1], -1) + "PLANT"[0] == "TKZMP"                              # middle moved back
    assert "PLANT"[-1] + "PLANT"[1:-1] + "PLANT"[0] == "TLANP"                                      # ends exchanged only
    return rule("PLANT")
N(LR, "Coding-Decoding", "medium",
  "In a certain code, STONE is written as EUPOS and BRAIN as NSBJB. How is PLANT written in that code?",
  "एक निश्चित कूट में STONE को EUPOS और BRAIN को NSBJB लिखा जाता है। उसी कूट में PLANT को कैसे लिखा जाएगा?",
  ["QMBOU", "TKZMP", "TLANP", "TMBOP"], 3,
  "In STONE → EUPOS the first and last letters, S and E, change places, and each of the other letters moves one place forward in the alphabet: T → U, O → P, N → O. BRAIN → NSBJB follows the same rule: N and B change places, R → S, A → B, I → J. "
  "For PLANT, T and P change places and L → M, A → B, N → O, giving TMBOP. QMBOU moves every letter forward without exchanging the ends; TKZMP moves the middle letters backward; TLANP only exchanges the ends.",
  "STONE → EUPOS में पहला और अंतिम अक्षर, S और E, आपस में बदलते हैं, और बाक़ी हर अक्षर वर्णमाला में एक स्थान आगे जाता है: T → U, O → P, N → O। BRAIN → NSBJB भी यही नियम मानता है: N और B बदलते हैं, R → S, A → B, I → J। "
  "PLANT में T और P बदलते हैं और L → M, A → B, N → O, जिससे TMBOP बनता है। QMBOU सिरों को बदले बिना हर अक्षर को आगे ले जाता है; TKZMP बीच के अक्षरों को पीछे ले जाता है; TLANP केवल सिरों को बदलता है।",
  "lr-cd-the-ends-exchanged-the-middle-moved-on", _cd1)

# 12 -- a rule that depends on the length of the word
def _cd2():
    shift = lambda w, k: "".join(chr((ord(ch) - 65 + k) % 26 + 65) for ch in w)
    rule = lambda w: shift(w, 1 if len(w) % 2 == 0 else -1)
    ex = {"FAN": "EZM", "GAME": "HBNF", "TOWER": "SNVDQ"}
    assert all(rule(w) == v for w, v in ex.items())
    vowels = lambda w: sum(ch in "AEIOU" for ch in w)
    value = lambda w: sum(ord(ch) - 64 for ch in w)
    # Every simple condition on the word that fits the three examples, in either direction, must give the same
    # answer for the query. Two examples were not enough, and neither were two other query words: WINDOW (a repeated
    # W) and BRIDGE (letter sum 45) each let a rule that fits the examples -- 'the last letter is before M', 'an even
    # number of distinct letters', 'the letter values add up to an even number' -- disagree with the parity of length.
    conditions = [lambda w: len(w) % 2 == 0, lambda w: vowels(w) % 2 == 0, lambda w: "E" in w, lambda w: w[0] < "M",
                  lambda w: w[-1] < "M", lambda w: w[0] in "AEIOU", lambda w: w[-1] in "AEIOU", lambda w: len(set(w)) % 2 == 0,
                  lambda w: len(w) > 4, lambda w: len(w) > 3, lambda w: "A" in w, lambda w: "O" in w,
                  lambda w: value(w) % 2 == 0, lambda w: (len(w) - vowels(w)) % 2 == 0, lambda w: w[0] < w[-1],
                  lambda w: len(set(w)) == len(w), lambda w: w[len(w) // 2] < "M"]
    answers, fitting = set(), 0
    for cond in conditions:
        for forward_if in (True, False):
            h = lambda w, cond=cond, forward_if=forward_if: shift(w, 1 if cond(w) == forward_if else -1)
            if all(h(w) == v for w, v in ex.items()):
                fitting += 1
                answers.add(h("CASTLE"))
    assert fitting >= 1 and answers == {"DBTUMF"}, (fitting, answers)
    other = lambda w: "".join(chr(ord(ch) + 1) if i % 2 == 0 else ch for i, ch in enumerate(w))
    assert shift("CASTLE", -1) == "BZRSKD" and other("CASTLE") == "DATTME"
    assert shift("CAS", 1) + shift("TLE", -1) == "DBTSKD"
    return rule("CASTLE")
N(LR, "Coding-Decoding", "hard",
  "In a certain code, FAN is written as EZM, GAME as HBNF and TOWER as SNVDQ. How is CASTLE written in that code?",
  "एक निश्चित कूट में FAN को EZM, GAME को HBNF और TOWER को SNVDQ लिखा जाता है। उसी कूट में CASTLE को कैसे लिखा जाएगा?",
  ["BZRSKD", "DATTME", "DBTSKD", "DBTUMF"], 3,
  "FAN → EZM moves every letter one place back (F → E, A → Z, N → M); GAME → HBNF moves every letter one place forward; TOWER → SNVDQ moves back again. Words with an odd number of letters (3 and 5) go back, and the word with an even number "
  "of letters (4) goes forward. CASTLE has 6 letters, an even number, so each letter moves one place forward: D, B, T, U, M, F. The other options apply the odd-word rule (BZRSKD), move only alternate letters (DATTME) "
  "or apply the odd-word rule to the second half only (DBTSKD).",
  "FAN → EZM हर अक्षर को एक स्थान पीछे ले जाता है (F → E, A → Z, N → M); GAME → HBNF हर अक्षर को एक स्थान आगे ले जाता है; TOWER → SNVDQ फिर पीछे ले जाता है। विषम संख्या में अक्षरों वाले शब्द (3 और 5) पीछे जाते हैं, और सम संख्या "
  "(4) वाला शब्द आगे। CASTLE में 6 अक्षर हैं, जो सम संख्या है, इसलिए हर अक्षर एक स्थान आगे जाता है: D, B, T, U, M, F। बाक़ी विकल्प विषम शब्द वाला नियम लगाते हैं (BZRSKD), केवल एक-एक छोड़कर अक्षर आगे ले जाते हैं (DATTME) "
  "या उस नियम को केवल दूसरे आधे पर लगाते हैं (DBTSKD)।",
  "lr-cd-a-rule-that-depends-on-the-length-of-the-word", _cd2)

# 13 -- the faces of the small cubes that are not painted
def _cp1():
    n = 5
    unpainted = 0
    for x, y, z in product(range(n), repeat=3):
        for axis, v in enumerate((x, y, z)):
            for side in (0, 1):                      # the face on the low side or on the high side of this axis
                on_surface = v == 0 if side == 0 else v == n - 1
                unpainted += 0 if on_surface else 1  # a face on the surface of the big cube is painted
    assert unpainted == n ** 3 * 6 - 6 * n * n == 600
    return str(unpainted)
N(LR, "Cube Painting", "medium",
  "A solid cube of side 5 cm is painted red on all six faces and then cut into 125 cubes, each of side 1 cm. What is the total area, in cm², of the faces of all the small cubes that are not painted?",
  "5 सेमी भुजा वाले एक ठोस घन के छहों फलकों पर लाल रंग किया जाता है और फिर उसे 1 सेमी भुजा वाले 125 घनों में काट दिया जाता है। उन सभी छोटे घनों के बिना रँगे फलकों का कुल क्षेत्रफल, वर्ग सेमी में, क्या है?",
  ["150", "600", "750", "900"], 1,
  "Each small cube has 6 faces of 1 cm², so all the small cubes together have 125 × 6 = 750 cm² of faces. The painted faces are exactly the surface of the original cube: 6 × 5 × 5 = 150 cm². "
  "So 750 - 150 = 600 cm² are not painted. 150 is the painted area, 750 is the area of all the faces, and 900 adds the painted area instead of taking it away.",
  "हर छोटे घन के 1 वर्ग सेमी के 6 फलक हैं, इसलिए सभी छोटे घनों के कुल 125 × 6 = 750 वर्ग सेमी फलक हैं। रँगे फलक ठीक मूल घन की सतह हैं: 6 × 5 × 5 = 150 वर्ग सेमी। "
  "अतः 750 - 150 = 600 वर्ग सेमी बिना रँगे हैं। 150 रँगा क्षेत्रफल है, 750 सभी फलकों का क्षेत्रफल, और 900 रँगे क्षेत्रफल को घटाने के बजाय जोड़ देता है।",
  "lr-cp-unpainted-faces-of-the-small-cubes", _cp1)

# 14 -- four conclusions from three statements
def _sy1():
    regions = list(product((0, 1), repeat=4))        # (pen, book, pencil, notebook)
    follow = [True] * 4
    for mask in range(1, 1 << 16):
        full = [r for k, r in enumerate(regions) if mask >> k & 1]
        if any(pn and not bk for pn, bk, pc, nb in full):                 # all pens are books
            continue
        if not any(bk and pc for pn, bk, pc, nb in full):                 # some books are pencils
            continue
        if any(pc and nb for pn, bk, pc, nb in full):                     # no pencil is a notebook
            continue
        follow[0] &= any(pc and bk for pn, bk, pc, nb in full)            # 1. some pencils are books
        follow[1] &= any(bk and not nb for pn, bk, pc, nb in full)        # 2. some books are not notebooks
        follow[2] &= any(pn and pc for pn, bk, pc, nb in full)            # 3. some pens are pencils
        follow[3] &= not any(pn and nb for pn, bk, pc, nb in full)        # 4. no pen is a notebook
    assert follow == [True, True, False, False], follow
    return "1 and 2 only"
SC(LR, "Syllogism", "hard",
   "Statements: All pens are books. Some books are pencils. No pencil is a notebook.\n\nWhich of the following conclusions follow(s) from the statements?",
   "कथन: सभी पेन किताबें हैं। कुछ किताबें पेंसिल हैं। कोई भी पेंसिल नोटबुक नहीं है।\n\nनिम्नलिखित में से कौन-सा/से निष्कर्ष कथनों से निकलता/निकलते है/हैं?",
   ["Some pencils are books.", "Some books are not notebooks.", "Some pens are pencils.", "No pen is a notebook."],
   ["कुछ पेंसिलें किताबें हैं।", "कुछ किताबें नोटबुक नहीं हैं।", "कुछ पेन पेंसिल हैं।", "कोई भी पेन नोटबुक नहीं है।"],
   ["1 and 2 only", "1 and 3 only", "2 and 4 only", "1, 2 and 4"], 0,
   "1 follows: 'some books are pencils' can be turned round. 2 follows: the books that are pencils are not notebooks (no pencil is a notebook), so some books are not notebooks. "
   "3 does not follow: every pen is a book, but the books that are pencils need not be pens. 4 does not follow: a pen is a book, and a book that is not a pencil may well be a notebook. So the conclusions that follow are 1 and 2.",
   "1 निकलता है: 'कुछ किताबें पेंसिल हैं' को पलटा जा सकता है। 2 निकलता है: जो किताबें पेंसिल हैं वे नोटबुक नहीं हैं (कोई पेंसिल नोटबुक नहीं), इसलिए कुछ किताबें नोटबुक नहीं हैं। "
   "3 नहीं निकलता: हर पेन किताब है, पर जो किताबें पेंसिल हैं वे पेन हों, यह ज़रूरी नहीं। 4 नहीं निकलता: पेन किताब है, और जो किताब पेंसिल नहीं है वह नोटबुक हो भी सकती है। अतः 1 और 2 निकलते हैं।",
   "lr-sy-four-conclusions-from-three-statements", check=_sy1)

# 15 -- a truth-teller, a liar and a trickster
def _tl1():
    stmts = {"A": lambda r: r["B"] == "L", "B": lambda r: r["B"] != "T", "C": lambda r: r["A"] == "L"}
    sols = []
    for perm in permutations("TLX"):
        r = dict(zip("ABC", perm))
        ok = True
        for p in "ABC":
            v = stmts[p](r)
            if (r[p] == "T" and not v) or (r[p] == "L" and v):
                ok = False
        if ok:
            sols.append(r)
    assert len(sols) == 1, sols
    return next(p for p, role in sols[0].items() if role == "T")
T(LR, "Truth-Liar", "hard",
  "Among three people A, B and C, one is a truth-teller who always speaks the truth, one is a liar who always lies, and one is a trickster who may speak the truth or lie. "
  "A says, 'B is the liar.' B says, 'I am not the truth-teller.' C says, 'A is the liar.' Who is the truth-teller?",
  "तीन व्यक्तियों A, B और C में से एक सत्यवादी है जो सदा सच बोलता है, एक झूठा है जो सदा झूठ बोलता है, और एक चालबाज़ है जो सच या झूठ कुछ भी बोल सकता है। "
  "A कहता है, 'B झूठा है।' B कहता है, 'मैं सत्यवादी नहीं हूँ।' C कहता है, 'A झूठा है।' सत्यवादी कौन है?",
  ["A", "B", "C", "Cannot be determined"], ["A", "B", "C", "निर्धारित नहीं किया जा सकता"], 2,
  "Suppose A were the truth-teller. Then 'B is the liar' is true, so B is the liar and C the trickster; but B, a liar, would be saying 'I am not the truth-teller', which is true -- and a liar cannot say anything true. "
  "Suppose B were the truth-teller: 'I am not the truth-teller' would be false, which is impossible. So C is the truth-teller, and 'A is the liar' is true. Then B is the trickster, and everything fits: A, the liar, says that B is the liar -- false; "
  "B, the trickster, says that he is not the truth-teller -- true, which a trickster may do.",
  "मान लीजिए A सत्यवादी है। तब 'B झूठा है' सत्य है, इसलिए B झूठा और C चालबाज़ है; पर तब झूठा B कह रहा होता कि 'मैं सत्यवादी नहीं हूँ', जो सत्य है -- और झूठा कोई सच्ची बात नहीं कह सकता। "
  "मान लीजिए B सत्यवादी है: 'मैं सत्यवादी नहीं हूँ' असत्य होता, जो असंभव है। अतः C सत्यवादी है, और 'A झूठा है' सत्य है। तब B चालबाज़ है, और सब कुछ बैठ जाता है: झूठा A कहता है कि B झूठा है -- असत्य; "
  "चालबाज़ B कहता है कि वह सत्यवादी नहीं है -- सत्य, जो चालबाज़ कर सकता है।",
  "lr-tl-a-truth-teller-a-liar-and-a-trickster", pos=2, check=_tl1)

# ---- the data-sufficiency block's three Reasoning items
def _ds1():
    scores = list(permutations((1, 2, 3)))                       # (A, B, C)
    top = lambda s: "ABC"[s.index(max(s))]
    s1 = [top(s) for s in scores if s[0] > s[1]]
    s2 = [top(s) for s in scores if s[2] < s[0]]
    both = [top(s) for s in scores if s[0] > s[1] and s[2] < s[0]]
    return _ds(s1, s2, both)
DS(LR, "medium",
   "Who scored the highest among A, B and C?",
   "A, B और C में से सबसे अधिक अंक किसने पाए?",
   "A scored more than B.", "A ने B से अधिक अंक पाए।",
   "C scored less than A.", "C ने A से कम अंक पाए।",
   2,
   "Statement I alone: A beat B, but C may have scored more than A -- not sufficient. Statement II alone: A beat C, but B may have scored more than A -- not sufficient. "
   "Together, A scored more than both B and C, so A scored the highest. Both statements are needed.",
   "कथन I अकेला: A ने B को हराया, पर C ने A से अधिक अंक पाए हो सकते हैं -- पर्याप्त नहीं। कथन II अकेला: A ने C को हराया, पर B ने A से अधिक अंक पाए हो सकते हैं -- पर्याप्त नहीं। "
   "दोनों साथ: A के अंक B और C दोनों से अधिक हैं, इसलिए A ने सबसे अधिक अंक पाए। दोनों कथन ज़रूरी हैं।",
   "lr-ds-the-highest-scorer-of-three", _ds1)

def _ds2():
    ages = list(permutations((1, 2, 3)))                         # (P, Q, R); a larger number is older
    eldest = lambda a: "PQR"[a.index(max(a))]
    s1 = [eldest(a) for a in ages if a[0] > a[1] > a[2]]
    s2 = [eldest(a) for a in ages if a[2] == min(a) and a[1] != max(a)]
    both = [eldest(a) for a in ages if a[0] > a[1] > a[2] and a[2] == min(a) and a[1] != max(a)]
    return _ds(s1, s2, both)
DS(LR, "medium",
   "Who is the eldest among P, Q and R?",
   "P, Q और R में सबसे बड़ा कौन है?",
   "P is older than Q, and Q is older than R.", "P, Q से बड़ा है, और Q, R से बड़ा है।",
   "R is the youngest, and Q is not the eldest.", "R सबसे छोटा है, और Q सबसे बड़ा नहीं है।",
   1,
   "Statement I alone: P is older than Q, who is older than R, so P is the eldest -- sufficient. Statement II alone: R is the youngest and Q is not the eldest, so only P can be the eldest -- also sufficient. "
   "Either statement alone answers the question. The trap is to feel that II names no one as the eldest and so cannot be enough.",
   "कथन I अकेला: P, Q से बड़ा है, जो R से बड़ा है, इसलिए P सबसे बड़ा है -- पर्याप्त। कथन II अकेला: R सबसे छोटा है और Q सबसे बड़ा नहीं है, इसलिए केवल P ही सबसे बड़ा हो सकता है -- यह भी पर्याप्त। "
   "कोई भी एक कथन अकेले प्रश्न का उत्तर दे देता है। जाल यह सोचना है कि II किसी को सबसे बड़ा नहीं बताता, इसलिए पर्याप्त नहीं हो सकता।",
   "lr-ds-the-eldest-of-three", _ds2)

def _ds3():
    names = {(1, 1): "north-east", (1, -1): "south-east", (-1, 1): "north-west", (-1, -1): "south-west",
             (0, 1): "north", (0, -1): "south", (1, 0): "east", (-1, 0): "west", (0, 0): "same place"}
    sign = lambda v: (v > 0) - (v < 0)
    dir_of = lambda p: names[(sign(p[0]), sign(p[1]))]           # the direction of P from Q, who stands at the origin
    grid = range(-8, 9)
    s1 = [dir_of((rx + 5, ry)) for rx in grid for ry in grid]    # I: P is 5 km east of R; R can be anywhere
    s2 = [dir_of((px, py)) for px in grid for py in grid]        # II: R is 5 km north of Q; P can be anywhere
    both = [dir_of((0 + 5, 5))]                                  # R = (0, 5) and P = R + (5, 0)
    return _ds(s1, s2, both)
DS(LR, "medium",
   "In which direction is P from Q?",
   "P, Q से किस दिशा में है?",
   "P is 5 km east of R.", "P, R से 5 किमी पूर्व में है।",
   "R is 5 km north of Q.", "R, Q से 5 किमी उत्तर में है।",
   2,
   "Statement I alone relates P to R, and says nothing about where R is from Q. Statement II alone relates R to Q, and says nothing about P. "
   "Together, R is 5 km north of Q and P is 5 km east of R, so P is 5 km east and 5 km north of Q: north-east. Both statements are needed.",
   "कथन I अकेला P को R से जोड़ता है, और यह नहीं बताता कि R, Q से कहाँ है। कथन II अकेला R को Q से जोड़ता है, और P के बारे में कुछ नहीं कहता। "
   "दोनों साथ: R, Q से 5 किमी उत्तर में है और P, R से 5 किमी पूर्व में, इसलिए P, Q से 5 किमी पूर्व और 5 किमी उत्तर में है: उत्तर-पूर्व। दोनों कथन ज़रूरी हैं।",
   "lr-ds-a-direction-built-from-two-legs", _ds3)
