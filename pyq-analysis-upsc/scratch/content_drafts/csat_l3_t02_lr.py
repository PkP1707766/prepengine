# -*- coding: utf-8 -*-
"""CSAT Level 3 · Test 2 -- Logical Reasoning (18 items: 15 in the Reasoning slots, 3 in the data-sufficiency block).

Level 3's harder mix (1 easy / 9 medium / 8 hard), with none of the shapes of Level 2 Tests 1-7, Level 1 Minis 1-3 or
Level 3 Test 1: coached schools that were bound to improve (regression to the mean), a word used in two senses, strong
and weak arguments on phones in class; a round-robin table read back into results, six people on a bench of three
rows, six numbers from 1 to 6 placed by clues; a family of six with two married couples, a sister who must be the
only daughter; the straight-line distance after three-quarters of a lap, the direction of a 'north wind'; a code read
off a phone keypad, AB + BA = 121; three dice stacked on a table; 'some doctors are writers' with a possibility
conclusion; three speakers of whom two must be alike; and in the data-sufficiency block a prize in one of three boxes,
a prime defined two ways, and a museum closed on Mondays. Arrangement, code, cube, syllogism and truth-teller keys are
found by checking every case."""
import math
from itertools import permutations, product
import csat_common as c
from csat_common import N, T, S2, DS, LR

def _ds(s1, s2, both):
    alone = (len(set(s1)) == 1, len(set(s2)) == 1)
    return "b" if all(alone) else "a" if any(alone) else "c" if len(set(both)) == 1 else "d"

# 1 -- coached schools that were bound to improve
T(LR, "Statement-Conclusion/Assumption", "hard",
  "Last year the schools with the lowest examination results in a district were given extra coaching for their pupils. This year their results improved more than those of the other schools in the district, and officials concluded that the coaching works. "
  "Which one of the following, if true, most seriously weakens the officials' conclusion?",
  "पिछले वर्ष एक ज़िले के सबसे कम परीक्षा परिणाम वाले विद्यालयों के विद्यार्थियों को अतिरिक्त कोचिंग दी गई। इस वर्ष उनके परिणाम ज़िले के अन्य विद्यालयों से अधिक सुधरे, और अधिकारियों ने निष्कर्ष निकाला कि कोचिंग कारगर है। "
  "निम्नलिखित में से कौन-सा, यदि सत्य हो, अधिकारियों के निष्कर्ष को सबसे गंभीर रूप से कमज़ोर करता है?",
  ["Schools with unusually poor results in one year tend to do better the next year even without help.",
   "The coaching was given by teachers drawn from the best-performing schools in the district.",
   "Many pupils in the coached schools said that they had enjoyed the extra classes a great deal.",
   "The other schools in the district also improved their results slightly over the same year, though by less."],
  ["असामान्य रूप से ख़राब परिणाम वाले विद्यालय अगले वर्ष बिना सहायता के भी प्रायः बेहतर करते हैं।",
   "कोचिंग ज़िले के सबसे अच्छा प्रदर्शन करने वाले विद्यालयों से लिए गए शिक्षकों ने दी थी।",
   "कोचिंग वाले विद्यालयों के कई विद्यार्थियों ने कहा कि उन्हें अतिरिक्त कक्षाएँ सचमुच बहुत अच्छी लगी थीं।",
   "ज़िले के अन्य विद्यालयों ने भी उसी वर्ष अपने परिणामों में थोड़ा सुधार किया।"],
  0,
  "The coached schools were chosen because their results were the lowest, and a year of unusually poor results is partly bad luck that is unlikely to repeat. Such schools tend to move back towards the average on their own, so a larger improvement among them is what one would expect even if the coaching did nothing. "
  "Who gave the coaching and whether pupils enjoyed it say nothing about its effect; and a slight improvement elsewhere leaves the coached schools' larger gain still to be explained, so it weakens the conclusion far less.",
  "कोचिंग वाले विद्यालय इसलिए चुने गए कि उनके परिणाम सबसे कम थे, और असामान्य रूप से ख़राब परिणामों वाला वर्ष आंशिक रूप से दुर्भाग्य होता है जिसके दोहराने की संभावना कम है। ऐसे विद्यालय अपने-आप औसत की ओर लौटते हैं, इसलिए उनमें अधिक सुधार वही है जिसकी अपेक्षा कोचिंग का कोई प्रभाव न होने पर भी होगी। "
  "कोचिंग किसने दी और विद्यार्थियों को वह अच्छी लगी या नहीं, यह उसके प्रभाव के बारे में कुछ नहीं कहता; और अन्यत्र थोड़ा सुधार कोचिंग वाले विद्यालयों के बड़े लाभ को अब भी अव्याख्यायित छोड़ता है, इसलिए वह निष्कर्ष को कहीं कम कमज़ोर करता है।",
  "lr-sc-coached-schools-that-were-bound-to-improve", pos=1)

# 2 -- a word used in two senses
T(LR, "Statement-Conclusion/Assumption", "hard",
  "'Every law has a law-maker. Gravitation is a law of nature. Therefore gravitation has a law-maker.' Which one of the following best describes the flaw in this argument?",
  "'हर क़ानून का कोई क़ानून-निर्माता होता है। गुरुत्वाकर्षण प्रकृति का एक नियम है। इसलिए गुरुत्वाकर्षण का कोई निर्माता है।' निम्नलिखित में से कौन-सा इस तर्क की त्रुटि का सबसे अच्छा वर्णन करता है?",
  ["It assumes in its first statement the very conclusion that it sets out to prove, and so argues in a circle.",
   "It draws a general conclusion about all laws from one example of a law of nature.",
   "It confuses a condition that is necessary for something to be a law with one that is sufficient.",
   "It uses 'law' in two senses: a rule that someone lays down and a regularity found in nature."],
  ["यह अपने पहले कथन में वही निष्कर्ष मान लेता है जिसे सिद्ध करने निकला है, और इसलिए चक्राकार तर्क करता है।",
   "यह प्रकृति के नियम के एक उदाहरण से सभी नियमों के बारे में सामान्य निष्कर्ष निकालता है।",
   "यह किसी चीज़ के नियम होने की आवश्यक शर्त को पर्याप्त शर्त से भ्रमित करता है।",
   "यह 'नियम' शब्द को दो अर्थों में लेता है: किसी का बनाया नियम, और प्रकृति में दिखने वाली नियमितता।"],
  3,
  "The first premise is true of laws in the sense of rules made by a legislature; the second calls gravitation a law in the sense of a regularity that nature is observed to follow. The conclusion borrows the maker from the first sense and attaches it to the second, so the argument only looks valid because one word covers two ideas. "
  "It does not argue in a circle (the conclusion is not stated in the premises), it does not generalise from a single case (it applies a general premise to one case), and no necessary or sufficient condition is confused.",
  "पहला आधार-वाक्य उस अर्थ में सत्य है जिसमें क़ानून विधायिका द्वारा बनाए नियम हैं; दूसरा गुरुत्वाकर्षण को उस अर्थ में नियम कहता है जिसमें वह प्रकृति में देखी गई नियमितता है। निष्कर्ष पहले अर्थ से निर्माता उधार लेकर उसे दूसरे अर्थ से जोड़ देता है, इसलिए तर्क केवल इसलिए वैध दिखता है कि एक ही शब्द दो विचारों को ढकता है। "
  "यह चक्राकार तर्क नहीं करता (निष्कर्ष आधार-वाक्यों में नहीं कहा गया), यह एक उदाहरण से सामान्यीकरण नहीं करता (यह एक सामान्य आधार-वाक्य को एक उदाहरण पर लागू करता है), और इसमें किसी आवश्यक या पर्याप्त शर्त का भ्रम नहीं है।",
  "lr-sc-a-word-used-in-two-senses", pos=3)

# 3 -- strong and weak arguments on phones in class
S2(LR, "Statement-Conclusion/Assumption", "medium",
   "Statement: Should the use of mobile phones be banned inside school classrooms during lessons?\n\nArguments:\nI. Yes. Phones used during lessons distract pupils from what is being taught.\nII. No. Every pupil has a right to own a mobile phone.\n\nWhich of the arguments given above is/are strong?",
   "कथन: क्या पाठ के दौरान विद्यालय की कक्षाओं के भीतर मोबाइल फ़ोन के प्रयोग पर प्रतिबंध लगना चाहिए?\n\nतर्क:\nI. हाँ। पाठ के दौरान प्रयोग किए गए फ़ोन विद्यार्थियों का ध्यान पढ़ाई से भटकाते हैं।\nII. नहीं। हर विद्यार्थी को मोबाइल फ़ोन रखने का अधिकार है।\n\nउपर्युक्त तर्कों में से कौन-सा/से प्रबल है/हैं?",
   ["Phones used during lessons distract pupils from what is being taught.",
    "Every pupil has a right to own a mobile phone."],
   ["पाठ के दौरान प्रयोग किए गए फ़ोन विद्यार्थियों का ध्यान पढ़ाई से भटकाते हैं।",
    "हर विद्यार्थी को मोबाइल फ़ोन रखने का अधिकार है।"],
   0,
   "Only I is strong. It bears directly on the question -- the use of phones during lessons -- and gives a serious reason connected with the purpose of a classroom. "
   "II is weak because it answers a different question: a ban on using phones inside classrooms during lessons does not take away anyone's right to own one, so the argument misses the point at issue.",
   "केवल I प्रबल है। वह सीधे प्रश्न से जुड़ा है -- पाठ के दौरान फ़ोन का प्रयोग -- और कक्षा के उद्देश्य से जुड़ा एक गंभीर कारण देता है। "
   "II दुर्बल है क्योंकि वह किसी दूसरे प्रश्न का उत्तर देता है: पाठ के दौरान कक्षा में फ़ोन के प्रयोग पर प्रतिबंध किसी से फ़ोन रखने का अधिकार नहीं छीनता, इसलिए तर्क मुद्दे से चूक जाता है।",
   "lr-sc-strong-and-weak-arguments-on-phones", roman=True)

# 4 -- a round-robin table read back into results
def _sa1():
    teams = "PQRS"
    matches = [(a, b) for i, a in enumerate(teams) for b in teams[i + 1:]]
    sols = []
    for res in product("WDL", repeat=6):
        pts = dict.fromkeys(teams, 0)
        for (a, b), r in zip(matches, res):
            if r == "W": pts[a] += 2
            elif r == "L": pts[b] += 2
            else: pts[a] += 1; pts[b] += 1
        if [pts[t] for t in teams] == [5, 4, 2, 1] and res.count("D") == 2:
            sols.append(dict(zip(matches, res)))
    assert len(sols) == 2
    claims = {"P beat S.": all(s[("P", "S")] == "W" for s in sols),
              "P and Q drew their match.": all(s[("P", "Q")] == "D" for s in sols),
              "R and S drew their match.": all(s[("R", "S")] == "D" for s in sols),
              "Q beat S.": all(s[("Q", "S")] == "W" for s in sols)}
    must = [k for k, v in claims.items() if v]
    assert must == ["P beat S."]
    return must[0]
T(LR, "Seating Arrangement", "hard",
  "Four teams, P, Q, R and S, played one another once each. A win earned 2 points, a draw 1 point to each side and a loss nothing. At the end P had 5 points, Q 4, R 2 and S 1, and exactly two of the six matches were drawn. Which one of the following must be true?",
  "चार टीमें, P, Q, R और S, आपस में एक-एक बार खेलीं। जीत पर 2 अंक, बराबरी पर दोनों पक्षों को 1-1 अंक और हार पर कुछ नहीं मिलता था। अंत में P के 5 अंक थे, Q के 4, R के 2 और S का 1, और छह में से ठीक दो मैच बराबरी पर छूटे। निम्नलिखित में से कौन-सा अनिवार्यतः सत्य है?",
  ["P beat S.", "P and Q drew their match.", "R and S drew their match.", "Q beat S."],
  ["P ने S को हराया।", "P और Q का मैच बराबरी पर छूटा।", "R और S का मैच बराबरी पर छूटा।", "Q ने S को हराया।"], 0,
  "S has 1 point, so S drew exactly one match and lost the other two. P has 5 points from three matches, which needs two wins and a draw. Testing the cases leaves exactly two tables with two draws: in one, P drew with R and R drew with S (P beat Q and S; Q beat R and S); in the other, P drew with Q and Q drew with S (P beat R and S; Q beat R; R beat S). "
  "In both, P beat S, so that must be true. 'P and Q drew' and 'R and S drew' each hold in only one table, and Q drew with S in the second, so 'Q beat S' need not be true either.",
  "S का 1 अंक है, इसलिए S ने ठीक एक मैच बराबरी पर खेला और बाक़ी दो हारे। P के तीन मैचों से 5 अंक हैं, जिसके लिए दो जीत और एक बराबरी चाहिए। स्थितियाँ जाँचने पर दो बराबरी वाली ठीक दो तालिकाएँ बचती हैं: एक में P की R से और R की S से बराबरी रही (P ने Q और S को हराया; Q ने R और S को हराया); दूसरी में P की Q से और Q की S से बराबरी रही (P ने R और S को हराया; Q ने R को हराया; R ने S को हराया)। "
  "दोनों में P ने S को हराया, इसलिए वह अनिवार्यतः सत्य है। 'P और Q की बराबरी' और 'R और S की बराबरी' प्रत्येक केवल एक तालिका में सही है, और दूसरी में Q की S से बराबरी रही, इसलिए 'Q ने S को हराया' भी अनिवार्य नहीं।",
  "lr-sa-a-round-robin-table-read-back-into-results", pos=2, check=_sa1)

# 5 -- six people on a bench of three rows
def _sa2():
    seats = [(r, s) for r in (1, 2, 3) for s in "LR"]
    out = []
    for p in permutations(seats):
        a = dict(zip("ABCDEF", p))
        if (a["A"][0] == 1 and a["B"][0] == 2 and a["B"][1] != a["A"][1] and a["C"][1] == "R" and a["D"][0] == 3
                and a["E"] == (2, a["D"][1]) and a["F"][1] == a["B"][1] and a["F"][0] != 1):
            out.append(a)
    assert len(out) == 1, out
    a = out[0]
    behind_b = (a["B"][0] + 1, a["B"][1])
    return next(k for k, v in a.items() if v == behind_b)
T(LR, "Seating Arrangement", "medium",
  "Six people, A to F, sit in a vehicle with three rows of two seats each, a left seat and a right seat, row 1 being the front. A sits in the front row. B sits in the row just behind A, on the other side from A. C sits on the right side. D sits in the back row, and E sits directly in front of D. "
  "F sits on the same side as B, but not in the front row. Who sits directly behind B?",
  "छह व्यक्ति, A से F, एक वाहन में बैठे हैं जिसमें दो-दो सीटों की तीन पंक्तियाँ हैं, एक बाईं सीट और एक दाईं, पंक्ति 1 सबसे आगे। A आगे की पंक्ति में बैठा है। B, A के ठीक पीछे वाली पंक्ति में, A से दूसरी ओर बैठा है। C दाईं ओर बैठा है। D पीछे की पंक्ति में बैठा है, और E, D के ठीक आगे। "
  "F, B वाली ओर बैठा है, पर आगे की पंक्ति में नहीं। B के ठीक पीछे कौन बैठा है?",
  ["C", "D", "E", "F"], ["C", "D", "E", "F"], 3,
  "B is in row 2, on the side opposite A. E is directly in front of D, so E is in row 2 too, on D's side; since B already holds one row-2 seat, E holds the other, which puts D on the side opposite B, and so on A's side. "
  "F is on B's side but not in front, and row 2 is full, so F is in row 3 on B's side -- directly behind B. That leaves C for the front row, on the right, which means A is on the left and B on the right. D (row 3, left) is behind E, not B; C and E are in rows 1 and 2.",
  "B पंक्ति 2 में, A के विपरीत ओर है। E, D के ठीक आगे है, इसलिए E भी पंक्ति 2 में D वाली ओर है; चूँकि पंक्ति 2 की एक सीट B के पास है, E दूसरी सीट पर है, जिससे D, B के विपरीत ओर, यानी A वाली ओर बैठता है। "
  "F, B वाली ओर है पर आगे नहीं, और पंक्ति 2 भरी है, इसलिए F पंक्ति 3 में B वाली ओर है -- B के ठीक पीछे। इससे C के लिए आगे की पंक्ति में दाईं सीट बचती है, अर्थात A बाईं ओर और B दाईं ओर है। D (पंक्ति 3, बाईं) E के पीछे है, B के नहीं; C और E पंक्ति 1 और 2 में हैं।",
  "lr-sa-six-people-on-a-bench-of-three-rows", pos=3, check=_sa2)

# 6 -- six numbers from 1 to 6 placed by clues
def _sa3():
    out = []
    for p in permutations(range(1, 7)):
        a = dict(zip("ABCDEF", p))
        if (a["A"] == 2 * a["B"] and a["B"] % 2 == 1 and a["C"] == a["D"] + 1 and a["E"] % 2 == 1
                and a["E"] > a["F"] and a["F"] > a["D"]):
            out.append(a)
    assert len(out) == 1
    return str(out[0]["C"])
N(LR, "Seating Arrangement", "medium",
  "Six friends, A to F, each choose a different whole number from 1 to 6. A's number is twice B's, and B's number is odd. C's number is one more than D's. E's number is odd and greater than F's, and F's number is greater than D's. What is C's number?",
  "छह मित्र, A से F, 1 से 6 तक की एक-एक अलग पूर्ण संख्या चुनते हैं। A की संख्या B की दोगुनी है, और B की संख्या विषम है। C की संख्या D से एक अधिक है। E की संख्या विषम है और F से बड़ी है, और F की संख्या D से बड़ी है। C की संख्या क्या है?",
  ["2", "3", "4", "5"], 0,
  "B is odd and A = 2B is at most 6, so B is 1 or 3 and A is 2 or 6. If B were 1 and A 2, then 3, 4, 5, 6 would be left for C, D, E and F, with C = D + 1 and F > D: D would have to be 3 (C 4), leaving 5 and 6, but E must be odd and greater than F, which 5 and 6 cannot satisfy. "
  "So B = 3 and A = 6, leaving 1, 2, 4, 5. E is odd and greater than F, and F is greater than D: E = 5, F = 4, and D and C take 1 and 2 with C = D + 1, so D = 1 and C = 2.",
  "B विषम है और A = 2B अधिकतम 6 है, इसलिए B, 1 या 3 है और A, 2 या 6। यदि B = 1 और A = 2 होता, तो C, D, E और F के लिए 3, 4, 5, 6 बचते, जहाँ C = D + 1 और F > D: D को 3 (C = 4) होना पड़ता, जिससे 5 और 6 बचते, पर E को विषम और F से बड़ा होना है, जो 5 और 6 से संभव नहीं। "
  "अतः B = 3 और A = 6, और 1, 2, 4, 5 बचते हैं। E विषम है और F से बड़ा, और F, D से बड़ा: E = 5, F = 4, और D तथा C, 1 और 2 लेते हैं जहाँ C = D + 1, इसलिए D = 1 और C = 2।",
  "lr-sa-six-numbers-placed-by-clues", _sa3)

# 7 -- a family of six with two couples: who married in
def _br1():
    from itertools import product as prod
    subsets = [frozenset(x) for x in ((), ("U",), ("S",), ("U", "S"))]
    out = set()
    # the open choices: the other parent X of R and T (Q is one), and the parents of P and of Q among the oldest pair
    for X, pp, pq in prod("PSU", subsets, subsets):
        par = {"R": {"Q", X}, "T": {"Q", X}, "P": set(pp), "Q": set(pq), "S": set(), "U": set()}
        kids = lambda y: sorted(x for x in par if y in par[x])
        if kids("S") != ["P"]: continue                                       # P is the only child of S
        if not any("U" in par[y] for y in par["R"]): continue                 # U is a grandparent of R
        if not any("S" in par[y] for y in par["T"]): continue                 # S is a grandparent of T
        couples = {frozenset(v) for v in par.values() if len(v) == 2}
        if len(couples) != 2: continue                                        # exactly two married couples
        if any(par[a] & par[b] for a, b in couples): continue                 # no couple are brother and sister
        out.add("Son-in-law" if "Q" not in kids("U") and "P" in kids("U") else "other")
    assert out == {"Son-in-law"}, out
    return "Son-in-law"
T(LR, "Blood Relation", "hard",
  "A family of six -- P, Q, R, S, T and U -- spans three generations and includes exactly two married couples. U is the grandfather of R, and S is the grandmother of T. R and T are Q's children. P is the only child of S. How is Q related to U?",
  "छह व्यक्तियों का एक परिवार -- P, Q, R, S, T और U -- तीन पीढ़ियों का है और उसमें ठीक दो विवाहित दंपती हैं। U, R के दादा या नाना हैं, और S, T की दादी या नानी हैं। R और T, Q की संतानें हैं। P, S की इकलौती संतान है। Q, U का क्या लगता है?",
  ["Son-in-law", "Son", "Brother-in-law", "Nephew"], ["दामाद", "पुत्र", "साला", "भतीजा"], 0,
  "T is Q's child and S is T's grandmother, so S is the mother of one of T's parents. S's only child is P, so P is T's other parent, and P and Q are one married couple. The other couple must be the grandparents, U and S. "
  "U is R's grandfather through P, the only child of S and so U's child too; Q is not their child, for then P and Q would be brother and sister. So Q married U's child P, and is U's son-in-law. 'Son' is the trap of reading 'grandfather' as father's father; 'brother-in-law' and 'nephew' put Q in the wrong generation.",
  "T, Q की संतान है और S, T की दादी या नानी है, इसलिए S, T के माता-पिता में से एक की माँ है। S की इकलौती संतान P है, इसलिए P, T का दूसरा अभिभावक है, और P तथा Q एक विवाहित दंपती हैं। दूसरा दंपती दादा-दादी या नाना-नानी, यानी U और S होंगे। "
  "U, R के नाना हैं P के माध्यम से, जो S की इकलौती संतान है और इसलिए U की भी संतान है; Q उनकी संतान नहीं है, वरना P और Q भाई-बहन होते। अतः Q ने U की संतान P से विवाह किया, और वह U का दामाद है। 'पुत्र' 'दादा' को पिता के पिता मानने का जाल है; 'साला' और 'भतीजा' Q को ग़लत पीढ़ी में रखते हैं।",
  "lr-br-a-family-of-six-with-two-couples", pos=0, check=_br1)

# 8 -- a sister who must be the only daughter
def _br2():
    out = set()
    for sa, sb in product("MF", repeat=2):
        daughters = [x for x, s in (("A", sa), ("B", sb)) if s == "F"]
        # C's children include A and B; C has exactly one daughter, D, who is not A; B is A's sister
        if sb == "F" and len(daughters) <= 1 and "A" not in daughters:
            out.add(sa)
    assert out == {"M"}
    return "A is C's son."
T(LR, "Blood Relation", "medium",
  "A and B are children of C. C has only one daughter, D. A is not D, and B is A's sister. Which one of the following is correct?",
  "A और B, C की संतानें हैं। C की केवल एक बेटी है, D। A, D नहीं है, और B, A की बहन है। निम्नलिखित में से कौन-सा सही है?",
  ["A is C's daughter.", "B is C's son.", "A is C's son.", "A's sex cannot be determined."],
  ["A, C की बेटी है।", "B, C का बेटा है।", "A, C का बेटा है।", "A का लिंग निर्धारित नहीं किया जा सकता।"], 2,
  "B is A's sister and a child of C, so B is a daughter of C. C has only one daughter, so B is D. A is also C's child but is not D, the only daughter, so A must be a son. "
  "'A's sex cannot be determined' overlooks that C has only one daughter; 'A is C's daughter' would give C two daughters; and B, being a sister, cannot be a son.",
  "B, A की बहन और C की संतान है, इसलिए B, C की बेटी है। C की केवल एक बेटी है, इसलिए B ही D है। A भी C की संतान है पर इकलौती बेटी D नहीं है, इसलिए A बेटा ही होगा। "
  "'A का लिंग निर्धारित नहीं' वाला विकल्प यह अनदेखा करता है कि C की केवल एक बेटी है; 'A, C की बेटी है' से C की दो बेटियाँ हो जातीं; और B, बहन होने के कारण, बेटा नहीं हो सकता।",
  "lr-br-a-sister-who-must-be-the-only-daughter", pos=2, check=_br2)

# 9 -- the straight-line distance after three-quarters of a lap
def _dd1():
    r = 70
    ang = 2 * math.pi * 3 / 4
    d = math.dist((r, 0), (r * math.cos(ang), r * math.sin(ang)))
    assert abs(d - 70 * 2 ** 0.5) < 1e-9
    return f"{round(d)} m"
N(LR, "Direction & Distance", "hard",
  "A runner starts at a point on a circular track of radius 70 m and runs three-quarters of the way round it. How far is she then from the starting point, measured in a straight line? (Take √2 = 1.414.)",
  "एक धाविका 70 मीटर त्रिज्या वाले एक वृत्ताकार पथ के एक बिंदु से चलकर उसका तीन-चौथाई चक्कर लगाती है। तब वह आरंभ बिंदु से सीधी रेखा में कितनी दूर है? (√2 = 1.414 लीजिए।)",
  ["70 m", "99 m", "140 m", "330 m"], 1,
  "Three-quarters of a lap leaves her a quarter of a lap short of the start, so the straight line from her to the start cuts off a quarter of the circle: the two radii to the ends meet at a right angle. The distance is the hypotenuse of a right triangle with both sides 70 m: 70√2 ≈ 99 m. "
  "330 m is the distance run along the track (three-quarters of 2 × 22/7 × 70 = 440 m); 140 m, the diameter, is how far she would be after half a lap; 70 m is the radius.",
  "तीन-चौथाई चक्कर के बाद वह आरंभ से एक-चौथाई चक्कर पीछे रहती है, इसलिए उससे आरंभ तक की सीधी रेखा वृत्त का एक-चौथाई भाग काटती है: दोनों सिरों तक की त्रिज्याएँ समकोण पर मिलती हैं। दूरी उस समकोण त्रिभुज का कर्ण है जिसकी दोनों भुजाएँ 70 मीटर हैं: 70√2 ≈ 99 मीटर। "
  "330 मीटर पथ पर दौड़ी गई दूरी है (2 × 22/7 × 70 = 440 मीटर का तीन-चौथाई); 140 मीटर, व्यास, वह दूरी है जो आधे चक्कर के बाद होती; 70 मीटर त्रिज्या है।",
  "lr-dd-three-quarters-of-a-lap", _dd1,
  opts_hi=["70 मीटर", "99 मीटर", "140 मीटर", "330 मीटर"])

# 10 -- the direction of a 'north wind'
N(LR, "Direction & Distance", "easy",
  "A wind is named after the direction from which it blows: a north wind blows from the north. A cyclist rides with a north wind directly behind her. In which direction is she riding?",
  "हवा का नाम उस दिशा पर रखा जाता है जिधर से वह चलती है: उत्तरी हवा उत्तर से चलती है। एक साइकिल सवार ऐसे चल रही है कि उत्तरी हवा ठीक उसकी पीठ की ओर से आ रही है। वह किस दिशा में जा रही है?",
  ["East", "West", "North", "South"], 3,
  "A north wind comes from the north and blows towards the south. If it is directly behind her, she is moving the way it blows: south. North is the direction the wind comes from, the trap the naming sets; east and west would put the wind at her side.",
  "उत्तरी हवा उत्तर से आती है और दक्षिण की ओर बहती है। यदि वह ठीक उसकी पीठ की ओर से आ रही है, तो वह उसी दिशा में जा रही है जिधर हवा बहती है: दक्षिण। उत्तर वह दिशा है जहाँ से हवा आती है, यही नामकरण का जाल है; पूर्व और पश्चिम में हवा उसकी बग़ल से आती।",
  "lr-dd-the-direction-of-a-north-wind", lambda: "South", opts_hi=["पूर्व", "पश्चिम", "उत्तर", "दक्षिण"])

# 11 -- a code read off a phone keypad
def _cd1():
    keypad = {d: s for d, s in zip("23456789", ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"])}
    pad = {ch: d for d, s in keypad.items() for ch in s}
    threes = {chr(65 + i): str(2 + i // 3) for i in range(26)}            # a naive 'three letters to a key' rule
    code = lambda w, m: "".join(m[ch] for ch in w)
    ex = {"CAB": "222", "DOG": "364", "FISH": "3474"}
    assert all(code(k, pad) == v for k, v in ex.items())
    assert code("FISH", threes) != ex["FISH"]                             # the S in FISH rules the naive rule out
    return code("CODE", pad)
N(LR, "Coding-Decoding", "medium",
  "In a certain code, CAB is written as 222, DOG as 364 and FISH as 3474. How is CODE written in that code?",
  "एक निश्चित कूट में CAB को 222, DOG को 364 और FISH को 3474 लिखा जाता है। उस कूट में CODE को कैसे लिखा जाएगा?",
  ["2363", "2633", "2643", "3633"], 1,
  "Each letter is replaced by the key that carries it on a telephone keypad: ABC on 2, DEF on 3, GHI on 4, JKL on 5, MNO on 6, PQRS on 7, TUV on 8, WXYZ on 9. FISH settles the rule: S is on 7 with P, Q and R, whereas simply counting three letters to a key would put it on 8. "
  "So C = 2, O = 6, D = 3 and E = 3, and CODE is 2633. 2363 and 2643 misplace O or D; 3633 puts C on 3.",
  "हर अक्षर को टेलीफ़ोन कीपैड की उस कुंजी से बदला जाता है जिस पर वह है: 2 पर ABC, 3 पर DEF, 4 पर GHI, 5 पर JKL, 6 पर MNO, 7 पर PQRS, 8 पर TUV, 9 पर WXYZ। FISH नियम तय करता है: S, P, Q और R के साथ 7 पर है, जबकि हर कुंजी पर केवल तीन अक्षर गिनने से वह 8 पर आता। "
  "अतः C = 2, O = 6, D = 3 और E = 3, और CODE = 2633। 2363 और 2643, O या D को ग़लत रखते हैं; 3633, C को 3 पर रखता है।",
  "lr-cd-a-code-read-off-a-phone-keypad", _cd1)

# 12 -- AB + BA = 121
def _cd2():
    ns = [10 * a + b for a in range(1, 10) for b in range(1, 10) if a != b and (10 * a + b) + (10 * b + a) == 121]
    assert len({tuple(sorted(divmod(n, 10))) for n in ns}) == 4
    return str(len(ns))
N(LR, "Coding-Decoding", "hard",
  "In the addition AB + BA = 121, A and B stand for two different non-zero digits, so that AB and BA are two-digit numbers. How many different numbers AB are possible?",
  "जोड़ AB + BA = 121 में A और B दो अलग-अलग शून्येतर अंकों के लिए हैं, जिससे AB और BA दो अंकों की संख्याएँ हैं। कितनी अलग-अलग संख्याएँ AB संभव हैं?",
  ["4", "6", "8", "9"], 2,
  "AB + BA = (10A + B) + (10B + A) = 11(A + B), so 11(A + B) = 121 and A + B = 11. The digit pairs are 2 and 9, 3 and 8, 4 and 7, 5 and 6, each in either order: 29, 92, 38, 83, 47, 74, 56 and 65 -- 8 numbers (A and B cannot be equal, since 11 is odd). "
  "4 counts each pair of digits once instead of in both orders; 9 and 6 do not match the pairs.",
  "AB + BA = (10A + B) + (10B + A) = 11(A + B), इसलिए 11(A + B) = 121 और A + B = 11। अंकों के जोड़े 2 और 9, 3 और 8, 4 और 7, 5 और 6 हैं, हर एक दोनों क्रमों में: 29, 92, 38, 83, 47, 74, 56 और 65 -- 8 संख्याएँ (A और B बराबर नहीं हो सकते, क्योंकि 11 विषम है)। "
  "4 हर अंक-जोड़े को दोनों क्रमों के बजाय एक बार गिनता है; 9 और 6 जोड़ों से मेल नहीं खाते।",
  "lr-cd-ab-plus-ba-equals-121", _cd2)

# 13 -- three dice stacked on a table
def _cp1():
    top = 5
    hidden = (7 - top) + 7 + 7                 # the top die's underside, then both faces of the middle and bottom dice
    return str(hidden)
N(LR, "Cube Painting", "hard",
  "Three standard dice, on each of which the opposite faces add up to 7, are stacked one on top of another on a table. The top face of the stack shows 5. What is the total of the numbers on the faces that are hidden -- the faces where the dice touch each other and the face resting on the table?",
  "तीन सामान्य पासे, जिनमें से हर एक पर आमने-सामने के फलकों का योग 7 है, एक मेज़ पर एक के ऊपर एक रखे हैं। ढेर का सबसे ऊपरी फलक 5 दिखाता है। छिपे हुए फलकों -- जहाँ पासे एक-दूसरे को छूते हैं और जो फलक मेज़ पर टिका है -- पर लिखी संख्याओं का योग क्या है?",
  ["16", "19", "21", "23"], 0,
  "Five faces are hidden: the underside of the top die, the top and underside of the middle die, and the top and underside of the bottom die. The top die shows 5, so its underside is 7 - 5 = 2. For each of the other two dice, the two hidden faces are opposite each other and add up to 7. The hidden total is 2 + 7 + 7 = 16. "
  "21 is the sum of all the faces of one die; 19 and 23 do not follow from the opposite-faces rule.",
  "पाँच फलक छिपे हैं: ऊपरी पासे का निचला फलक, बीच वाले पासे का ऊपरी और निचला फलक, और सबसे नीचे वाले पासे का ऊपरी और निचला फलक। ऊपरी पासा 5 दिखाता है, इसलिए उसका निचला फलक 7 - 5 = 2 है। बाक़ी दोनों पासों में से हर एक के दोनों छिपे फलक आमने-सामने हैं और उनका योग 7 है। छिपा हुआ योग 2 + 7 + 7 = 16 है। "
  "21 एक पासे के सभी फलकों का योग है; 19 और 23 आमने-सामने के फलकों वाले नियम से नहीं निकलते।",
  "lr-cp-three-dice-stacked-on-a-table", _cp1)

# 14 -- 'some doctors are writers' with a possibility conclusion
def _sy1():
    regions = list(product((0, 1), repeat=3))          # (doctor, writer, lazy)
    one = True
    two_possible = False
    for mask in range(1, 1 << 8):
        world = [r for k, r in enumerate(regions) if mask >> k & 1]
        if not any(d and w for d, w, l in world): continue        # some doctors are writers
        if any(w and l for d, w, l in world): continue            # no writer is lazy
        one = one and any(d and not l for d, w, l in world)
        if all(l for d, w, l in world if d):
            two_possible = True
    return c.T2R[{(True, False): 0, (False, True): 1, (True, True): 2, (False, False): 3}[(one, two_possible)]]
S2(LR, "Syllogism", "medium",
   "Statements: Some doctors are writers. No writer is lazy.\n\nWhich of the following conclusions follow(s) from the statements?",
   "कथन: कुछ डॉक्टर लेखक हैं। कोई भी लेखक आलसी नहीं है।\n\nनिम्नलिखित में से कौन-सा/से निष्कर्ष कथनों से निकलता/निकलते है/हैं?",
   ["Some doctors are not lazy.", "That all doctors are lazy is a possibility."],
   ["कुछ डॉक्टर आलसी नहीं हैं।", "सभी डॉक्टरों का आलसी होना एक संभावना है।"],
   0,
   "I follows: the doctors who are writers cannot be lazy, since no writer is, so some doctors are not lazy. "
   "II does not follow: for all doctors to be lazy, the doctors who are writers would have to be lazy too, which the second statement forbids. A 'possibility' conclusion follows only if it is consistent with the statements, and this one contradicts them.",
   "I निकलता है: जो डॉक्टर लेखक हैं वे आलसी नहीं हो सकते, क्योंकि कोई लेखक आलसी नहीं है, इसलिए कुछ डॉक्टर आलसी नहीं हैं। "
   "II नहीं निकलता: सभी डॉक्टरों के आलसी होने के लिए लेखक डॉक्टरों को भी आलसी होना पड़ता, जिसे दूसरा कथन वर्जित करता है। 'संभावना' वाला निष्कर्ष तभी निकलता है जब वह कथनों से संगत हो, और यह उनका खंडन करता है।",
   "lr-sy-some-doctors-are-writers-with-a-possibility", roman=True, check=_sy1)

# 15 -- three speakers of whom two must be alike
def _tl1():
    sols = []
    for a, b, cc in product("TL", repeat=3):
        says = {"A": b == "L" and cc == "L", "B": a == "L", "C": b == "T"}
        if all(says[p] == (r == "T") for p, r in zip("ABC", (a, b, cc))):
            sols.append((a, b, cc))
    assert sorted(sols) == [("L", "T", "T"), ("T", "L", "L")]
    claims = {"A tells the truth, and B is a liar.": all(s[0] == "T" and s[1] == "L" for s in sols),
              "B and C are of the same kind.": all(s[1] == s[2] for s in sols),
              "B is a liar, and C tells the truth.": all(s[1] == "L" and s[2] == "T" for s in sols),
              "C is a liar, whatever A may be.": all(s[2] == "L" for s in sols)}
    must = [k for k, v in claims.items() if v]
    assert must == ["B and C are of the same kind."]
    return must[0]
T(LR, "Truth-Liar", "hard",
  "Each of three people, A, B and C, either always tells the truth or always lies. A says, 'B and C are both liars.' B says, 'A is a liar.' C says, 'B tells the truth.' Which one of the following must be true?",
  "तीन व्यक्तियों, A, B और C, में से प्रत्येक या तो हमेशा सच बोलता है या हमेशा झूठ। A कहता है, 'B और C दोनों झूठे हैं।' B कहता है, 'A झूठा है।' C कहता है, 'B सच बोलता है।' निम्नलिखित में से कौन-सा अनिवार्यतः सत्य है?",
  ["A tells the truth, and B is a liar.", "B and C are of the same kind.", "B is a liar, and C tells the truth.", "C is a liar, whatever A may be."],
  ["A सच बोलता है, और B झूठा है।", "B और C एक ही प्रकार के हैं।", "B झूठा है, और C सच बोलता है।", "A जो भी हो, C झूठा है।"], 1,
  "If A tells the truth, B and C both lie: B's 'A is a liar' is then false, as it should be, and C's 'B tells the truth' is false too -- consistent. If A lies, B's 'A is a liar' is true, so B tells the truth, and then C's 'B tells the truth' is true, so C tells the truth; A's claim that both are liars is then false, as it must be -- also consistent. "
  "So there are two possibilities, A truthful with B and C liars, or A a liar with B and C truthful. In both, B and C are of the same kind. 'A tells the truth, and B is a liar' and 'C is a liar' hold in only the first possibility, and 'B is a liar, and C tells the truth' holds in neither.",
  "यदि A सच बोलता है, तो B और C दोनों झूठ बोलते हैं: तब B का 'A झूठा है' असत्य है, जैसा होना चाहिए, और C का 'B सच बोलता है' भी असत्य है -- संगत। यदि A झूठ बोलता है, तो B का 'A झूठा है' सत्य है, इसलिए B सच बोलता है, और तब C का 'B सच बोलता है' सत्य है, इसलिए C सच बोलता है; तब A का यह दावा कि दोनों झूठे हैं असत्य है, जैसा होना ही चाहिए -- यह भी संगत। "
  "अतः दो संभावनाएँ हैं: A सत्यवादी और B तथा C झूठे, या A झूठा और B तथा C सत्यवादी। दोनों में B और C एक ही प्रकार के हैं। 'A सच बोलता है, और B झूठा है' और 'C झूठा है' केवल पहली संभावना में सही हैं, और 'B झूठा है, और C सच बोलता है' किसी में नहीं।",
  "lr-tl-three-speakers-of-whom-two-must-be-alike", pos=1, check=_tl1)

# ---- the data-sufficiency block's three Reasoning items
def _ds1():
    boxes = (1, 2, 3)
    s1 = [b for b in boxes if b != 1]
    s2 = [b for b in boxes if b != 2]
    both = [b for b in boxes if b not in (1, 2)]
    return _ds(s1, s2, both)
DS(LR, "medium",
   "A prize has been put in exactly one of three boxes, numbered 1, 2 and 3. Which box holds the prize?",
   "एक इनाम तीन बक्सों, जिन पर 1, 2 और 3 लिखा है, में से ठीक एक में रखा गया है। इनाम किस बक्से में है?",
   "The prize is not in box 1.", "इनाम बक्सा 1 में नहीं है।",
   "The prize is not in box 2.", "इनाम बक्सा 2 में नहीं है।",
   2,
   "Statement I leaves boxes 2 and 3, and Statement II leaves boxes 1 and 3, so neither alone settles the question. Together they rule out boxes 1 and 2, so the prize is in box 3. Both statements are needed.",
   "कथन I बक्से 2 और 3 छोड़ता है, और कथन II बक्से 1 और 3, इसलिए कोई भी अकेला प्रश्न तय नहीं करता। दोनों मिलकर बक्से 1 और 2 को बाहर करते हैं, इसलिए इनाम बक्सा 3 में है। दोनों कथन ज़रूरी हैं।",
   "lr-ds-a-prize-in-one-of-three-boxes", _ds1)

def _ds2():
    divisors = lambda n: [d for d in range(1, n + 1) if n % d == 0]
    ns = range(1, 300)
    s1 = {all(n % d for d in range(2, n)) and n > 1 for n in ns if len(divisors(n)) == 2}
    s2 = {len(divisors(n)) == 2 for n in ns if n > 1 and all(n % d for d in range(2, n))}
    both = s1 & s2
    assert s1 == {True} and s2 == {True}
    return _ds(s1, s2, both)
DS(LR, "medium",
   "Is the natural number x a prime number?",
   "क्या प्राकृत संख्या x एक अभाज्य संख्या है?",
   "x has exactly two factors.", "x के ठीक दो गुणनखंड हैं।",
   "x is greater than 1 and has no factor between 1 and x.", "x, 1 से बड़ी है और उसका 1 और x के बीच कोई गुणनखंड नहीं है।",
   1,
   "A prime is a natural number with exactly two factors, 1 and itself. Statement I says exactly that, so it answers the question (yes). Statement II says the same thing in other words -- a number above 1 with no factor other than 1 and itself -- so it too answers the question alone. Either statement is sufficient.",
   "अभाज्य संख्या वह प्राकृत संख्या है जिसके ठीक दो गुणनखंड हों, 1 और स्वयं वह। कथन I ठीक यही कहता है, इसलिए वह प्रश्न का उत्तर देता है (हाँ)। कथन II यही बात दूसरे शब्दों में कहता है -- 1 से बड़ी ऐसी संख्या जिसका 1 और स्वयं के सिवा कोई गुणनखंड नहीं -- इसलिए वह भी अकेले उत्तर देता है। कोई भी एक कथन पर्याप्त है।",
   "lr-ds-a-prime-defined-two-ways", _ds2)

def _ds3():
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    s1 = [d for d in days if d != "Mon"]
    s2 = [d for i, d in enumerate(days) if i < 3]
    both = [d for d in s1 if d in s2]
    assert both == ["Tue", "Wed"]
    return _ds(s1, s2, both)
DS(LR, "medium",
   "In a week that runs from Monday to Sunday, on which day did Asha visit the museum?",
   "सोमवार से रविवार तक के एक सप्ताह में आशा किस दिन संग्रहालय गई?",
   "The museum is closed on Mondays, and she visited it on a day when it was open.", "संग्रहालय सोमवार को बंद रहता है, और वह उस दिन गई जब वह खुला था।",
   "She visited it before Thursday.", "वह गुरुवार से पहले गई।",
   3,
   "Statement I rules out Monday only. Statement II leaves Monday, Tuesday and Wednesday. Together they leave Tuesday and Wednesday, so the day still cannot be fixed. The question cannot be answered even with both statements.",
   "कथन I केवल सोमवार को बाहर करता है। कथन II सोमवार, मंगलवार और बुधवार छोड़ता है। दोनों मिलकर मंगलवार और बुधवार छोड़ते हैं, इसलिए दिन अब भी तय नहीं होता। दोनों कथनों के साथ भी प्रश्न का उत्तर नहीं दिया जा सकता।",
   "lr-ds-a-museum-closed-on-mondays", _ds3)
