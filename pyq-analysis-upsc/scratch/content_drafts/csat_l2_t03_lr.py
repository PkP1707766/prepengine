# -*- coding: utf-8 -*-
"""CSAT Level 2 · Test 3 -- Logical Reasoning (18 items: 15 in the Reasoning slots, 3 in the data-sufficiency block).

Same mix as Tests 1 and 2 with new traps: a course of action, an argument weakened by a rival cause, bounds
forced by numbers, two rows facing each other (right is west for one row and east for the other), a week of
lectures, a 'second lightest' that tempts counting from the wrong end, a chain of relations that folds back on
the speaker, turns by angles, directions with no distances, letters shifted forward and back in turn, swapped
operators, a 4 × 3 × 2 block with no hidden inside, a syllogism with a red herring, a self-referring
truth-teller, and three data-sufficiency items (a bound, a direction either way, a code from two sentences).
Difficulty 3 easy / 10 medium / 5 hard. Arrangement, code, cube, syllogism and truth-teller keys are found by
checking every case."""
from itertools import permutations, product
import csat_common as c
from csat_common import N, T, S2, DS, LR

def _two(one, two):
    return c.T2R[{(True, False): 0, (False, True): 1, (True, True): 2, (False, False): 3}[(one, two)]]

CONC = "Which of the following conclusions follow(s) from the statement?"
CONC_HI = "निम्नलिखित में से कौन-सा/से निष्कर्ष कथन से निकलता/निकलते है/हैं?"
ACTION = "Which of the following courses of action logically follow(s)?"
ACTION_HI = "निम्नलिखित में से कौन-सी कार्यवाही/कार्यवाहियाँ तार्किक रूप से अनुसरणीय है/हैं?"

# 1 -- course of action
S2(LR, "Statement-Conclusion/Assumption", "easy",
   "Statement: Several cases of dengue have been reported from one ward of a town after a spell of heavy rain.\n\n" + ACTION,
   "कथन: भारी वर्षा के एक दौर के बाद एक कस्बे के एक वार्ड से डेंगू के कई मामले सामने आए हैं।\n\n" + ACTION_HI,
   ["The municipality should clear stagnant water in the ward and spray it against mosquitoes.",
    "All the residents of the ward should be moved to another part of the town."],
   ["नगरपालिका को वार्ड में जमा पानी हटाना चाहिए और मच्छरों के विरुद्ध छिड़काव करना चाहिए।",
    "वार्ड के सभी निवासियों को कस्बे के किसी दूसरे भाग में भेज देना चाहिए।"], 0,
   "Only I follows. Dengue spreads through mosquitoes that breed in stagnant water, so clearing the water and spraying deal with the cause where it is. "
   "II does not follow: moving a whole ward is impractical and out of proportion, and it is the mosquitoes, not the place, that carry the disease. A course of action must be practical and must address the problem.",
   "केवल I अनुसरणीय है। डेंगू उन मच्छरों से फैलता है जो जमा पानी में पनपते हैं, इसलिए पानी हटाना और छिड़काव करना कारण से वहीं निपटते हैं जहाँ वह है। "
   "II अनुसरणीय नहीं है: पूरे वार्ड को हटाना अव्यावहारिक और अनुपात से बाहर है, और रोग मच्छर फैलाते हैं, स्थान नहीं। कार्यवाही व्यावहारिक होनी चाहिए और समस्या को सुलझाने वाली होनी चाहिए।",
   "lr-sc-dengue-course-of-action", roman=True)

# 2 -- an argument weakened by a rival cause
T(LR, "Statement-Conclusion/Assumption", "medium",
  "Argument: In the two years since a new metro line opened, road accidents in the city have fallen by 20 per cent. The metro has therefore made the city's roads safer.\n\n"
  "Which one of the following, if true, most weakens the argument?",
  "तर्क: एक नई मेट्रो लाइन खुलने के बाद के दो वर्षों में शहर में सड़क दुर्घटनाएँ 20 प्रतिशत घट गई हैं। अतः मेट्रो ने शहर की सड़कों को अधिक सुरक्षित बना दिया है।\n\n"
  "निम्नलिखित में से कौन-सा, यदि सत्य हो, तो तर्क को सबसे अधिक कमज़ोर करता है?",
  ["The city also lowered speed limits and installed junction cameras in those two years.",
   "Many people who used to drive to work every day now travel to their offices by the metro.",
   "The metro line cost more to build than had been planned.",
   "Most of the road accidents in the city take place on weekday evenings after office hours."],
  ["शहर ने उन्हीं दो वर्षों में गति सीमा भी घटाई और चौराहों पर कैमरे भी लगाए।",
   "जो बहुत-से लोग पहले रोज़ गाड़ी चलाकर काम पर जाते थे, वे अब मेट्रो से अपने दफ़्तर जाते हैं।",
   "मेट्रो लाइन बनाने में योजना से अधिक लागत आई।",
   "शहर की अधिकांश सड़क दुर्घटनाएँ कार्यदिवसों की शाम को दफ़्तर के समय के बाद होती हैं।"], 0,
  "The argument credits the metro with the fall in accidents. The strongest weakener offers another cause for the same fall: lower speed limits and junction cameras in the same period could explain it without the metro. "
  "People leaving their cars for the metro actually supports the argument; the metro's cost, and the hour at which accidents happen, have no bearing on whether the metro caused the fall.",
  "तर्क दुर्घटनाओं में कमी का श्रेय मेट्रो को देता है। सबसे प्रबल कमज़ोर करने वाला कथन उसी कमी का दूसरा कारण देता है: उसी अवधि में घटी गति सीमा और चौराहों के कैमरे मेट्रो के बिना भी इसकी व्याख्या कर सकते हैं। "
  "लोगों का गाड़ी छोड़कर मेट्रो अपनाना तो तर्क का समर्थन करता है; मेट्रो की लागत, और दुर्घटनाएँ किस समय होती हैं, इसका इस बात से कोई संबंध नहीं कि कमी मेट्रो के कारण हुई या नहीं।",
  "lr-sc-metro-rival-cause", pos=2)

# 3 -- bounds forced by the numbers
def _sc3():
    both = range(max(0, 120 + 150 - 200), min(120, 150) + 1)
    return _two(min(both) >= 70, max(both) <= 120)
S2(LR, "Statement-Conclusion/Assumption", "hard",
   "Statement: Of the 200 students in a school, 120 passed in Mathematics and 150 passed in Science.\n\n" + CONC,
   "कथन: एक विद्यालय के 200 विद्यार्थियों में से 120 गणित में और 150 विज्ञान में उत्तीर्ण हुए।\n\n" + CONC_HI,
   ["At least 70 students passed in both subjects.", "At most 120 students passed in both subjects."],
   ["कम से कम 70 विद्यार्थी दोनों विषयों में उत्तीर्ण हुए।", "अधिक से अधिक 120 विद्यार्थी दोनों विषयों में उत्तीर्ण हुए।"], 2,
   "Both follow. Those who passed in at least one subject cannot be more than 200, so those who passed in both are at least 120 + 150 - 200 = 70 (I). "
   "And no more students can have passed in both than passed in Mathematics, so the overlap is at most 120 (II), which happens if every Mathematics pass also passed in Science. "
   "The trap is to think that a statement with 'at least' or 'at most' cannot be certain; both bounds are forced by the numbers.",
   "दोनों निकलते हैं। कम से कम एक विषय में उत्तीर्ण विद्यार्थी 200 से अधिक नहीं हो सकते, इसलिए दोनों में उत्तीर्ण कम से कम 120 + 150 - 200 = 70 हैं (I)। "
   "और दोनों में उत्तीर्ण विद्यार्थी गणित में उत्तीर्ण विद्यार्थियों से अधिक नहीं हो सकते, इसलिए यह संख्या अधिक से अधिक 120 है (II), जो तब होता है जब गणित में उत्तीर्ण हर विद्यार्थी विज्ञान में भी उत्तीर्ण हो। "
   "जाल यह सोचना है कि 'कम से कम' या 'अधिक से अधिक' वाला कथन निश्चित नहीं हो सकता; दोनों सीमाएँ संख्याओं से ही तय होती हैं।",
   "lr-sc-pass-overlap-bounds", roman=True, check=_sc3)

# 4 -- two rows facing each other
def _sa1():
    # Seats 1-4 from west to east in both rows. The northern row faces south (its right is west, lower number);
    # the southern row faces north (its right is east, higher number).
    sols = []
    for north in permutations("PQRS"):
        n = {p: i + 1 for i, p in enumerate(north)}
        if n["Q"] not in (1, 4) or n["R"] != n["Q"] - 2:
            continue
        for south in permutations("WXYZ"):
            s = {p: i + 1 for i, p in enumerate(south)}
            if s["X"] != n["Q"] or s["Y"] != s["X"] - 1 or s["Z"] != n["R"] or n["S"] == s["Y"]:
                continue
            sols.append((north, south))
    assert len(sols) == 1, sols
    north, south = sols[0]
    return south[north.index("P")]
N(LR, "Seating Arrangement", "hard",
  "Eight people sit in two rows of four, each person directly facing one person in the other row. P, Q, R and S sit in the northern row, facing south; W, X, Y and Z sit in the southern row, facing north. "
  "Q sits at one end of the northern row, and X faces Q. R sits second to the right of Q. Y sits to the immediate left of X. Z faces R, and S does not face Y. Who faces P?",
  "आठ लोग चार-चार की दो पंक्तियों में इस प्रकार बैठे हैं कि हर व्यक्ति दूसरी पंक्ति के ठीक एक व्यक्ति के सामने है। P, Q, R और S उत्तरी पंक्ति में दक्षिण की ओर मुँह करके बैठे हैं; W, X, Y और Z दक्षिणी पंक्ति में उत्तर की ओर मुँह करके बैठे हैं। "
  "Q उत्तरी पंक्ति के एक छोर पर बैठा है, और X, Q के सामने है। R, Q के दाएँ से दूसरे स्थान पर है। Y, X के ठीक बाएँ बैठा है। Z, R के सामने है, और S, Y के सामने नहीं है। P के सामने कौन है?",
  ["W", "X", "Y", "Z"], 2,
  "Number the seats 1 to 4 from west to east. The northern row faces south, so its right is west; the southern row faces north, so its right is east. Second to Q's right means two seats to the west, "
  "which is possible only if Q is at the eastern end, seat 4: so R is in seat 2, and X, facing Q, is in seat 4 of the southern row. Y, to X's immediate left, is in seat 3, and Z, facing R, in seat 2, leaving W in seat 1. "
  "S may not face Y, so S takes seat 1 and P seat 3, opposite Y. W faces S, X faces Q and Z faces R. Taking 'right' as east for the northern row puts Q at the wrong end.",
  "सीटों को पश्चिम से पूर्व 1 से 4 तक गिनिए। उत्तरी पंक्ति दक्षिण की ओर देखती है, इसलिए उसका दायाँ पश्चिम है; दक्षिणी पंक्ति उत्तर की ओर देखती है, इसलिए उसका दायाँ पूर्व है। Q के दाएँ से दूसरे का अर्थ है दो सीट पश्चिम, "
  "जो तभी संभव है जब Q पूर्वी छोर, सीट 4, पर हो: अतः R सीट 2 पर है, और Q के सामने वाला X दक्षिणी पंक्ति की सीट 4 पर। X के ठीक बाएँ Y सीट 3 पर है, और R के सामने Z सीट 2 पर, जिससे W सीट 1 पर बचता है। "
  "S, Y के सामने नहीं हो सकता, इसलिए S सीट 1 और P सीट 3 लेता है, Y के सामने। W, S के सामने है, X, Q के सामने और Z, R के सामने। उत्तरी पंक्ति के लिए 'दायाँ' पूर्व मानने से Q ग़लत छोर पर पहुँच जाता है।",
  "lr-sa-two-rows-facing", _sa1)

# 5 -- a week of lectures
def _sa2():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    sols = []
    for order in permutations(["History", "Geography", "Polity", "Economy", "Ethics"]):
        d = {sub: i for i, sub in enumerate(order)}
        if d["Polity"] != 2 or d["History"] != d["Economy"] - 1 or d["Ethics"] in (0, 4) or d["Geography"] <= d["Economy"]:
            continue
        sols.append(d)
    assert len(sols) == 1, sols
    return days[sols[0]["Geography"]]
N(LR, "Seating Arrangement", "medium",
  "Five lectures -- on History, Geography, Polity, Economy and Ethics -- are held on the five working days from Monday to Friday, one lecture a day. Polity is held on Wednesday. "
  "History is held on the day just before Economy. Ethics is held neither on Monday nor on Friday. Geography is held on a later day than Economy. On which day is the Geography lecture held?",
  "पाँच व्याख्यान -- इतिहास, भूगोल, राजव्यवस्था, अर्थव्यवस्था और नीतिशास्त्र पर -- सोमवार से शुक्रवार तक के पाँच कार्यदिवसों पर, एक दिन में एक, होते हैं। राजव्यवस्था बुधवार को है। "
  "इतिहास, अर्थव्यवस्था से ठीक पहले वाले दिन है। नीतिशास्त्र न सोमवार को है, न शुक्रवार को। भूगोल, अर्थव्यवस्था के बाद के किसी दिन है। भूगोल का व्याख्यान किस दिन है?",
  ["Monday", "Tuesday", "Thursday", "Friday"], 3,
  "With Wednesday taken by Polity, History and Economy, on consecutive days, are either Monday and Tuesday or Thursday and Friday. If Economy were on Friday, Geography could not come later, "
  "so History is on Monday and Economy on Tuesday. Ethics, kept off Monday and Friday, must be on Thursday, which leaves Friday for Geography. Monday is History's day, Tuesday Economy's and Thursday Ethics's.",
  "बुधवार राजव्यवस्था का होने से, लगातार दिनों वाले इतिहास और अर्थव्यवस्था या तो सोमवार-मंगलवार को हैं या गुरुवार-शुक्रवार को। यदि अर्थव्यवस्था शुक्रवार को होती, तो भूगोल उसके बाद नहीं आ सकता, "
  "इसलिए इतिहास सोमवार और अर्थव्यवस्था मंगलवार को है। सोमवार और शुक्रवार से बाहर रखा गया नीतिशास्त्र गुरुवार को ही होगा, जिससे शुक्रवार भूगोल के लिए बचता है। सोमवार इतिहास का, मंगलवार अर्थव्यवस्था का और गुरुवार नीतिशास्त्र का दिन है।",
  "lr-sa-week-of-lectures", _sa2,
  opts_hi=["सोमवार", "मंगलवार", "गुरुवार", "शुक्रवार"])

# 6 -- second lightest
def _sa3():
    sols = [o for o in permutations("PQRST")        # heaviest first
            if o.index("R") < o.index("P") < o.index("Q") and o.index("Q") < o.index("S") and o.index("T") < o.index("R")]
    assert len(sols) == 1, sols
    return sols[0][-2]
N(LR, "Seating Arrangement", "easy",
  "Of five boxes P, Q, R, S and T, each of a different weight, P is heavier than Q but lighter than R, S is lighter than Q, and T is heavier than R. Which box is the second lightest?",
  "पाँच डिब्बों P, Q, R, S और T में से, जिनका हर एक का भार अलग है, P, Q से भारी पर R से हल्का है, S, Q से हल्का है, और T, R से भारी है। दूसरा सबसे हल्का डिब्बा कौन-सा है?",
  ["Q", "R", "S", "T"], 0,
  "Joining the clues from heaviest to lightest: T is heavier than R, R than P, P than Q, and Q than S, giving T, R, P, Q, S. The second lightest is Q. "
  "R is the second heaviest, the answer from counting at the wrong end; S is the lightest and T the heaviest.",
  "भारी से हल्के की ओर सूत्र जोड़ने पर: T, R से भारी है, R, P से, P, Q से, और Q, S से, यानी T, R, P, Q, S। दूसरा सबसे हल्का Q है। "
  "R दूसरा सबसे भारी है, जो ग़लत छोर से गिनने पर आता है; S सबसे हल्का और T सबसे भारी है।",
  "lr-sa-second-lightest-box", _sa3)

# 7 -- easy relation
T(LR, "Blood Relation", "easy",
  "A is the brother of B. B is the daughter of C, and C is the only son of D. How is A related to D?",
  "A, B का भाई है। B, C की बेटी है, और C, D का इकलौता बेटा है। A, D का क्या लगता है?",
  ["Grandson", "Son", "Nephew", "Son-in-law"], ["पोता", "पुत्र", "भतीजा", "दामाद"], 0,
  "C is D's son and B is C's daughter, so B is D's granddaughter; A, B's brother, is C's son and so D's grandson (पोता, through D's son). "
  "'Son' stops a generation short, at C; a nephew would need A's parent to be D's brother or sister; a son-in-law would be married to D's daughter.",
  "C, D का बेटा है और B, C की बेटी, इसलिए B, D की पोती है; B का भाई A, C का बेटा है और इसलिए D का पोता (D के बेटे के माध्यम से)। "
  "'पुत्र' एक पीढ़ी पहले, C पर, रुक जाता है; भतीजा होने के लिए A के माता-पिता में से कोई D का भाई या बहन होना चाहिए; दामाद D की बेटी का पति होता।",
  "lr-br-only-son-of-d", pos=3)

# 8 -- a chain that folds back on the speaker
T(LR, "Blood Relation", "hard",
  "Pointing to a photograph, a man says, 'She is the only daughter of the father of my brother's wife's husband.' How is the woman in the photograph related to the man?",
  "एक तस्वीर की ओर इशारा करते हुए एक पुरुष कहता है, 'वह मेरे भाई की पत्नी के पति के पिता की इकलौती बेटी है।' तस्वीर वाली महिला उस पुरुष की क्या लगती है?",
  ["Sister", "Sister-in-law", "Mother", "Cousin"], ["बहन", "भाभी", "माँ", "चचेरी बहन"], 0,
  "Unwind it from the inside. The man's brother's wife's husband is the brother himself; the father of his brother is the man's own father; and the only daughter of his father is his sister. "
  "'Sister-in-law' stops at the brother's wife and forgets that her husband brings the chain back to the man's own family; 'mother' is his father's wife, not his daughter; a cousin would have a different father.",
  "भीतर से खोलिए। पुरुष के भाई की पत्नी का पति स्वयं वह भाई है; भाई के पिता पुरुष के अपने पिता हैं; और पिता की इकलौती बेटी उसकी बहन है। "
  "'भाभी' भाई की पत्नी पर रुक जाता है और भूल जाता है कि उसका पति शृंखला को पुरुष के अपने परिवार में लौटा देता है; 'माँ' पिता की पत्नी है, बेटी नहीं; चचेरी बहन के पिता अलग होते।",
  "lr-br-chain-folds-back", pos=3)

# 9 -- turns by angles
def _dd1():
    heading = (0 + 135 - 270 + 45) % 360
    return {0: "North", 90: "East", 180: "South", 225: "South-west", 270: "West"}[heading]
N(LR, "Direction & Distance", "medium",
  "A man is facing north. He turns 135° clockwise, then 270° anticlockwise, and then 45° clockwise. In which direction is he facing now?",
  "एक व्यक्ति उत्तर की ओर मुँह करके खड़ा है। वह 135° दक्षिणावर्त घूमता है, फिर 270° वामावर्त, और फिर 45° दक्षिणावर्त। अब उसका मुँह किस दिशा में है?",
  ["East", "South", "South-west", "West"], 3,
  "Measure clockwise from north: 0 + 135 = 135° (south-east); 135 - 270 = -135°, which is 225° (south-west); 225 + 45 = 270°, which is west. "
  "East comes from making the 270° turn clockwise; south-west stops before the last turn; south makes the last 45° turn anticlockwise.",
  "उत्तर से दक्षिणावर्त मापिए: 0 + 135 = 135° (दक्षिण-पूर्व); 135 - 270 = -135°, यानी 225° (दक्षिण-पश्चिम); 225 + 45 = 270°, यानी पश्चिम। "
  "पूर्व तब आता है जब 270° का मोड़ दक्षिणावर्त लिया जाए; दक्षिण-पश्चिम अंतिम मोड़ से पहले रुक जाता है; दक्षिण अंतिम 45° का मोड़ वामावर्त ले लेता है।",
  "lr-dd-turns-by-angles", _dd1,
  opts_hi=["पूर्व", "दक्षिण", "दक्षिण-पश्चिम", "पश्चिम"])

# 10 -- directions with no distances
def _dd2():
    # Y at the origin; X due south-west of Y; Z due east of X and due south of Y.
    found = set()
    for k in range(1, 6):
        x = (-k, -k)
        z = (0, x[1])                               # due east of X and due south of Y
        dx, dy = 0 - z[0], 0 - z[1]                 # Y seen from Z
        found.add({(0, 1): "North"}.get((dx and dx // abs(dx), dy and dy // abs(dy)), "?"))
    return found.pop() if len(found) == 1 else "?"
N(LR, "Direction & Distance", "medium",
  "Town X lies due south-west of town Y. Town Z lies due east of X and due south of Y. In which direction is Y from Z?",
  "कस्बा X, कस्बे Y के ठीक दक्षिण-पश्चिम में है। कस्बा Z, X के ठीक पूर्व में और Y के ठीक दक्षिण में है। Z से Y किस दिशा में है?",
  ["North", "North-east", "East", "North-west"], 0,
  "Put Y at the centre. X is south-west of Y -- say a km west and a km south of it. Z is due east of X, so it is also a km south of Y, and it is due south of Y, so it lies directly below Y. Y is therefore due north of Z. "
  "North-east is the direction of Y from X; east is the direction of Z from X; north-west would need Z to lie to the east of Y.",
  "Y को केंद्र में रखिए। X, Y के दक्षिण-पश्चिम में है -- मान लीजिए उससे a किमी पश्चिम और a किमी दक्षिण। Z, X के ठीक पूर्व में है, इसलिए वह भी Y से a किमी दक्षिण में है, और वह Y के ठीक दक्षिण में है, इसलिए Y के ठीक नीचे है। अतः Y, Z के ठीक उत्तर में है। "
  "उत्तर-पूर्व, X से Y की दिशा है; पूर्व, X से Z की दिशा है; उत्तर-पश्चिम के लिए Z को Y के पूर्व में होना चाहिए था।",
  "lr-dd-towns-without-distances", _dd2,
  opts_hi=["उत्तर", "उत्तर-पूर्व", "पूर्व", "उत्तर-पश्चिम"])

# 11 -- letters forward and back in turn
def _cd1():
    shift = lambda w: "".join(chr((ord(ch) - 65 + (1 if i % 2 == 0 else -1)) % 26 + 65) for i, ch in enumerate(w))
    assert shift("GARDEN") == "HZSCFM"
    return shift("FLOWER")
N(LR, "Coding-Decoding", "medium",
  "In a certain code, GARDEN is written as HZSCFM. How is FLOWER written in that code?",
  "एक निश्चित कूट में GARDEN को HZSCFM लिखा जाता है। उसी कूट में FLOWER को कैसे लिखा जाएगा?",
  ["EKNVDQ", "GKPVFQ", "GKPXFQ", "GMPXFS"], 1,
  "Compare letter by letter: G → H (+1), A → Z (-1, going round the alphabet), R → S (+1), D → C (-1), E → F (+1), N → M (-1): the letters move one step forward and one step back in turn. "
  "FLOWER becomes F + 1 = G, L - 1 = K, O + 1 = P, W - 1 = V, E + 1 = F, R - 1 = Q: GKPVFQ. GMPXFS moves every letter forward; EKNVDQ moves every letter back; GKPXFQ moves the W forward instead of back.",
  "अक्षर-दर-अक्षर तुलना कीजिए: G → H (+1), A → Z (-1, वर्णमाला में घूमकर), R → S (+1), D → C (-1), E → F (+1), N → M (-1): अक्षर बारी-बारी से एक कदम आगे और एक कदम पीछे जाते हैं। "
  "FLOWER बनता है F + 1 = G, L - 1 = K, O + 1 = P, W - 1 = V, E + 1 = F, R - 1 = Q: GKPVFQ। GMPXFS हर अक्षर को आगे ले जाता है; EKNVDQ हर अक्षर को पीछे; GKPXFQ, W को पीछे के बजाय आगे ले जाता है।",
  "lr-cd-forward-and-back-in-turn", _cd1)

# 12 -- swapped operators
def _cd2():
    table = str.maketrans({"+": "*", "-": "+", "×": "/", "÷": "-"})
    expr = "8 + 6 - 4 ÷ 12 × 3"
    value = eval(expr.translate(table))
    assert eval("8 * 6 - 4 - 12 / 3") == 40 and eval("8 * 6 + 4 - 12 * 3") == 16 and eval("8 * 6 + 4 + 12 / 3") == 56
    return str(int(value)) if value == int(value) else "?"
N(LR, "Coding-Decoding", "medium",
  "If '+' means '×', '-' means '+', '×' means '÷' and '÷' means '-', what is the value of 8 + 6 - 4 ÷ 12 × 3?",
  "यदि '+' का अर्थ '×', '-' का अर्थ '+', '×' का अर्थ '÷' और '÷' का अर्थ '-' हो, तो 8 + 6 - 4 ÷ 12 × 3 का मान क्या है?",
  ["16", "40", "48", "56"], 2,
  "Rewrite with the true signs: 8 × 6 + 4 - 12 ÷ 3. Doing division and multiplication first, 48 + 4 - 4 = 48. "
  "16 forgets that × stands for ÷ (it subtracts 12 × 3 = 36); 40 leaves the '-' as a minus sign; 56 turns the ÷ into + instead of -.",
  "सही चिह्नों के साथ फिर लिखिए: 8 × 6 + 4 - 12 ÷ 3। पहले भाग और गुणा करने पर 48 + 4 - 4 = 48। "
  "16 भूल जाता है कि × का अर्थ ÷ है (वह 12 × 3 = 36 घटाता है); 40, '-' को घटाने का चिह्न ही रहने देता है; 56, ÷ को - के बजाय + बना देता है।",
  "lr-cd-swapped-operators", _cd2)

# 13 -- a block with no hidden inside
def _cp1():
    a, b, h = 4, 3, 2
    count = {k: 0 for k in range(4)}
    for x, y, z in product(range(a), range(b), range(h)):
        count[(x in (0, a - 1)) + (y in (0, b - 1)) + (z in (0, h - 1))] += 1
    assert count[0] == 0 and count[2] == 12 and count[3] == 8
    return str(count[1])
N(LR, "Cube Painting", "hard",
  "A wooden block 4 cm long, 3 cm wide and 2 cm high is painted on all its faces and then cut into 1 cm cubes. How many of the small cubes have exactly one painted face?",
  "4 सेमी लंबे, 3 सेमी चौड़े और 2 सेमी ऊँचे लकड़ी के एक गुटके को सभी फलकों पर रँगकर 1 सेमी के घनों में काटा जाता है। कितने छोटे घनों का ठीक एक फलक रँगा है?",
  ["0", "4", "8", "12"], 1,
  "The block gives 4 × 3 × 2 = 24 cubes. A cube has exactly one painted face only if it lies inside a face, away from all its edges. On each of the two 4 × 3 faces that leaves (4 - 2)(3 - 2) = 2 cubes; "
  "the 4 × 2 and 3 × 2 faces leave none, because a face only 2 cm across is all edge. So 2 + 2 = 4. 12 is the number with exactly two painted faces and 8 the corners, with three; "
  "0 is the number with no painted face, since a block only 2 cm high has no hidden inside.",
  "गुटके से 4 × 3 × 2 = 24 घन बनते हैं। किसी घन का ठीक एक फलक तभी रँगा होता है जब वह किसी फलक के भीतर, उसके सभी किनारों से दूर, हो। दोनों 4 × 3 फलकों में से हर एक पर ऐसे (4 - 2)(3 - 2) = 2 घन बचते हैं; "
  "4 × 2 और 3 × 2 फलकों पर कोई नहीं, क्योंकि केवल 2 सेमी चौड़ा फलक पूरा किनारा ही है। अतः 2 + 2 = 4। 12 ठीक दो रँगे फलकों वाले घनों की संख्या है और 8 कोनों की, जिनके तीन फलक रँगे हैं; "
  "0 बिना रँगे घनों की संख्या है, क्योंकि केवल 2 सेमी ऊँचे गुटके का कोई छिपा भीतरी भाग नहीं होता।",
  "lr-cp-block-4-by-3-by-2", _cp1)

# 14 -- syllogism with a red herring
def _sy1():
    regions = list(product((0, 1), repeat=4))        # (rose, flower, stone, red)
    one = two = True
    for mask in range(1, 1 << 16):
        full = [r for k, r in enumerate(regions) if mask >> k & 1]
        if any(ro and not fl for ro, fl, st, rd in full):           # all roses are flowers
            continue
        if any(fl and st for ro, fl, st, rd in full):               # no flower is a stone
            continue
        if not any(st and rd for ro, fl, st, rd in full):           # some stones are red
            continue
        one &= any(rd and ro for ro, fl, st, rd in full)
        two &= not any(st and ro for ro, fl, st, rd in full)
    return _two(one, two)
S2(LR, "Syllogism", "medium",
   "Statements: All roses are flowers. No flower is a stone. Some stones are red.\n\nWhich of the following conclusions follow(s) from the statements?",
   "कथन: सभी गुलाब फूल हैं। कोई भी फूल पत्थर नहीं है। कुछ पत्थर लाल हैं।\n\nनिम्नलिखित में से कौन-सा/से निष्कर्ष कथनों से निकलता/निकलते है/हैं?",
   ["Some red things are roses.", "No stone is a rose."],
   ["कुछ लाल वस्तुएँ गुलाब हैं।", "कोई भी पत्थर गुलाब नहीं है।"], 1,
   "Only II follows: every rose is a flower and no flower is a stone, so no rose can be a stone. I does not follow: the only red things the statements mention are stones, and no stone is a rose; "
   "roses may or may not be red, so 'some red things are roses' is possible but not certain. The red stones are a red herring for I.",
   "केवल II निकलता है: हर गुलाब फूल है और कोई फूल पत्थर नहीं है, इसलिए कोई गुलाब पत्थर नहीं हो सकता। I नहीं निकलता: कथनों में जिन लाल वस्तुओं का उल्लेख है वे केवल पत्थर हैं, और कोई पत्थर गुलाब नहीं है; "
   "गुलाब लाल हो भी सकते हैं और नहीं भी, इसलिए 'कुछ लाल वस्तुएँ गुलाब हैं' संभव है पर निश्चित नहीं। लाल पत्थर I के लिए केवल भटकाने वाली बात हैं।",
   "lr-sy-roses-flowers-stones", roman=True, check=_sy1)

# 15 -- a truth-teller who refers to both
def _tl1():
    sols = [(a, b) for a, b in product((True, False), repeat=2) if a == (not (a and b))]   # A: 'at least one of us is a liar'
    assert len(sols) == 1, sols
    a, b = sols[0]
    return {(True, True): "Both are truth-tellers", (True, False): "A is a truth-teller and B is a liar",
            (False, True): "A is a liar and B is a truth-teller", (False, False): "Both are liars"}[(a, b)]
N(LR, "Truth-Liar", "hard",
  "Each of two people, A and B, is either a truth-teller, who always tells the truth, or a liar, who always lies. A says, 'At least one of us is a liar.' Which of the following must be true?",
  "दो व्यक्तियों, A और B, में से हर एक या तो सत्यवादी है, जो सदा सच बोलता है, या झूठा, जो सदा झूठ बोलता है। A कहता है, 'हम दोनों में से कम से कम एक झूठा है।' निम्नलिखित में से क्या अवश्य सत्य है?",
  ["Both are truth-tellers", "A is a truth-teller and B is a liar", "A is a liar and B is a truth-teller", "Both are liars"], 1,
  "Suppose A is a liar. Then 'at least one of us is a liar' is true, because A is one -- but a liar cannot say anything true. So A is a truth-teller, and the statement is true: one of the two is a liar, and it can only be B. "
  "'Both are liars' fails in the same way as A being a liar; 'both are truth-tellers' would make A's statement false.",
  "मान लीजिए A झूठा है। तब 'हम दोनों में से कम से कम एक झूठा है' सत्य है, क्योंकि A स्वयं झूठा है -- पर झूठा कोई सच्ची बात नहीं कह सकता। अतः A सत्यवादी है, और कथन सत्य है: दोनों में से एक झूठा है, और वह केवल B हो सकता है। "
  "'दोनों झूठे हैं' उसी तरह विफल होता है जैसे A का झूठा होना; 'दोनों सत्यवादी हैं' A के कथन को असत्य बना देता।",
  "lr-tl-at-least-one-liar", _tl1,
  opts_hi=["दोनों सत्यवादी हैं", "A सत्यवादी है और B झूठा", "A झूठा है और B सत्यवादी", "दोनों झूठे हैं"])

# ---- the data-sufficiency block's three Reasoning items
def _ds1():
    ns = range(1, 100)
    s1 = {n > 40 for n in ns if n + 5 > 45}
    s2 = {n > 40 for n in ns if n < 50}
    both = {n > 40 for n in ns if n + 5 > 45 and n < 50}
    alone = (len(s1) == 1, len(s2) == 1)
    return "b" if all(alone) else "a" if any(alone) else "c" if len(both) == 1 else "d"
DS(LR, "medium",
   "Are there more than 40 students in the class?",
   "क्या कक्षा में 40 से अधिक विद्यार्थी हैं?",
   "If 5 more students joined the class, it would have more than 45 students.", "यदि कक्षा में 5 और विद्यार्थी आ जाएँ, तो उसमें 45 से अधिक विद्यार्थी होंगे।",
   "The class has fewer than 50 students.", "कक्षा में 50 से कम विद्यार्थी हैं।",
   0,
   "Statement I: if n + 5 is more than 45, then n is more than 40 -- the answer is yes, from I alone. Statement II: fewer than 50 allows 45 students (yes) or 30 (no) -- not sufficient. "
   "So the question can be answered using I alone but not using II alone.",
   "कथन I: यदि n + 5, 45 से अधिक है, तो n, 40 से अधिक है -- उत्तर हाँ है, केवल I से। कथन II: 50 से कम में 45 विद्यार्थी (हाँ) भी हो सकते हैं और 30 (नहीं) भी -- पर्याप्त नहीं। "
   "अतः प्रश्न का उत्तर केवल I से दिया जा सकता है, केवल II से नहीं।",
   "lr-ds-more-than-forty", _ds1)

def _ds2():
    dirs = lambda pts: {("north" if y > 0 else "south" if y < 0 else "same") if x == 0 else "off-line" for x, y in pts}
    gaps = range(1, 6)
    s1 = dirs((0, t + s) for t in gaps for s in gaps)            # house (0, 0) -> temple (0, t) -> school (0, t + s)
    s2 = dirs((0, m + s) for m in gaps for s in gaps)            # house -> market (0, m) -> school (0, m + s)
    alone = (len(s1) == 1, len(s2) == 1)
    return "b" if all(alone) else "a" if any(alone) else "c"
DS(LR, "medium",
   "In which direction is the school from Ramesh's house?",
   "रमेश के घर से विद्यालय किस दिशा में है?",
   "The school is due north of the temple, and the temple is due north of the house.", "विद्यालय मंदिर के ठीक उत्तर में है, और मंदिर घर के ठीक उत्तर में है।",
   "The market is due south of the school, and the house is due south of the market.", "बाज़ार विद्यालय के ठीक दक्षिण में है, और घर बाज़ार के ठीक दक्षिण में है।",
   1,
   "Statement I: going due north from the house you reach the temple and then the school, so the school is due north of the house. Statement II: going due north from the house you reach the market and then the school -- "
   "again due north. Either statement alone answers the question. The trap is to think that each statement fixes only part of the route, so that both are needed.",
   "कथन I: घर से ठीक उत्तर जाने पर पहले मंदिर और फिर विद्यालय आता है, इसलिए विद्यालय घर के ठीक उत्तर में है। कथन II: घर से ठीक उत्तर जाने पर पहले बाज़ार और फिर विद्यालय आता है -- "
   "फिर से ठीक उत्तर। कोई भी एक कथन अकेले प्रश्न का उत्तर दे देता है। जाल यह सोचना है कि हर कथन रास्ते का केवल एक भाग बताता है, इसलिए दोनों चाहिए।",
   "lr-ds-school-due-north", _ds2)

def _ds3():
    def codes_for_sky(sentences):
        found = set()
        for maps in product(*[permutations(codes) for words, codes in sentences]):
            m = {}
            ok = True
            for (words, _), assigned in zip(sentences, maps):
                for w, cd in zip(words, assigned):
                    if m.get(w, cd) != cd or (cd in m.values() and m.get(w) != cd):
                        ok = False
                    m[w] = cd
            if ok:
                found.add(m["sky"])
        return found
    one = (["blue", "sky", "above"], ["ka", "pa", "ta"])
    two = (["sky", "is", "clear"], ["na", "pa", "ri"])
    alone = (len(codes_for_sky([one])) == 1, len(codes_for_sky([two])) == 1)
    both = codes_for_sky([one, two])
    return "b" if all(alone) else "a" if any(alone) else "c" if len(both) == 1 else "d"
DS(LR, "medium",
   "In a certain code language, what is the code for 'sky'?",
   "एक निश्चित कूट भाषा में 'sky' का कूट क्या है?",
   "'blue sky above' is written as 'ka pa ta'.", "'blue sky above' को 'ka pa ta' लिखा जाता है।",
   "'sky is clear' is written as 'na pa ri'.", "'sky is clear' को 'na pa ri' लिखा जाता है।",
   2,
   "Each sentence alone matches three words with three codes in an unknown order, so 'sky' could be any of them. Together, 'sky' is the only word common to both sentences and 'pa' the only code common to both, so 'sky' is 'pa'. "
   "A code need not keep the order of the words, which is why neither statement alone is enough.",
   "हर वाक्य अकेले तीन शब्दों को तीन कूटों से किसी अज्ञात क्रम में मिलाता है, इसलिए 'sky' उनमें से कोई भी हो सकता है। दोनों साथ: 'sky' दोनों वाक्यों में अकेला साझा शब्द है और 'pa' अकेला साझा कूट, इसलिए 'sky' का कूट 'pa' है। "
   "कूट में शब्दों का क्रम बना रहना ज़रूरी नहीं, इसीलिए कोई भी कथन अकेले पर्याप्त नहीं है।",
   "lr-ds-code-for-sky", _ds3)
