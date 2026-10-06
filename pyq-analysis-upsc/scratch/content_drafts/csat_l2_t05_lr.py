# -*- coding: utf-8 -*-
"""CSAT Level 2 · Test 5 -- Logical Reasoning (18 items: 15 in the Reasoning slots, 3 in the data-sufficiency block).

Same mix as Tests 1-4 with new traps: the most logical conclusion from two statements, a principle applied to
cases, the assumption a plan depends on, a rectangular table tied to the compass, the order of finishers in a race,
houses painted in a row, the only child of a grandmother, daughters who share a brother, two walkers who end at the
same spot, compass names turned through 135°, a mirror-image alphabet, a rule found from three Pythagorean triples,
paint on at least one face, poets who are not painters, and three speakers of whom only one kind is certain; in the
data-sufficiency block, a stepson who cannot be ruled out, a match that rain would have cancelled, and a shadow in
the morning. Difficulty 3 easy / 10 medium / 5 hard. Arrangement, code, cube, syllogism and truth-teller keys are
found by checking every case."""
from itertools import permutations, product
import csat_common as c
from csat_common import N, T, S2, DS, LR

def _ds(s1, s2, both):
    alone = (len(set(s1)) == 1, len(set(s2)) == 1)
    return "b" if all(alone) else "a" if any(alone) else "c" if len(set(both)) == 1 else "d"

# 1 -- the most logical conclusion
T(LR, "Statement-Conclusion/Assumption", "medium",
  "Statement: Every student who passed the test had attended the coaching class. Some students who attended the coaching class did not pass the test.\n\n"
  "Which one of the following conclusions follows most logically from the statement?",
  "कथन: परीक्षा में उत्तीर्ण हुए हर विद्यार्थी ने कोचिंग कक्षा में भाग लिया था। कोचिंग कक्षा में भाग लेने वाले कुछ विद्यार्थी परीक्षा में उत्तीर्ण नहीं हुए।\n\n"
  "निम्नलिखित में से कौन-सा निष्कर्ष कथन से सबसे तार्किक रूप से निकलता है?",
  ["Attending the coaching class did not ensure that a student passed.",
   "Every student who attended the coaching class passed the test.",
   "Some students passed the test without attending the coaching class.",
   "The coaching class was of no use to any of the students."],
  ["कोचिंग कक्षा में भाग लेना उत्तीर्ण होने की गारंटी नहीं था।",
   "कोचिंग कक्षा में भाग लेने वाला हर विद्यार्थी परीक्षा में उत्तीर्ण हुआ।",
   "कुछ विद्यार्थी कोचिंग कक्षा में भाग लिए बिना परीक्षा में उत्तीर्ण हुए।",
   "कोचिंग कक्षा किसी भी विद्यार्थी के किसी काम की नहीं थी।"], 0,
  "The second sentence says that some students attended the class and still failed, so attending did not guarantee a pass. Saying that every student who attended passed contradicts that sentence; "
  "saying that some passed without attending contradicts the first, by which every student who passed had attended; and nothing shows the class was of no use to anyone -- the statement is silent on how many passed.",
  "दूसरा वाक्य कहता है कि कुछ विद्यार्थी कक्षा में आए और फिर भी अनुत्तीर्ण हुए, इसलिए भाग लेना उत्तीर्ण होने की गारंटी नहीं था। यह कहना कि भाग लेने वाला हर विद्यार्थी उत्तीर्ण हुआ, उस वाक्य का खंडन करता है; "
  "यह कहना कि कुछ बिना भाग लिए उत्तीर्ण हुए, पहले वाक्य का खंडन करता है, जिसके अनुसार हर उत्तीर्ण विद्यार्थी ने भाग लिया था; और कुछ भी नहीं दिखाता कि कक्षा किसी के काम की नहीं थी -- कथन इस पर मौन है कि कितने उत्तीर्ण हुए।",
  "lr-sc-most-logical-conclusion", pos=3)

# 2 -- a principle applied to cases
T(LR, "Statement-Conclusion/Assumption", "easy",
  "Principle: A public servant must not take part in a decision in which a close relative stands to gain or lose financially.\n\nIn which one of the following situations is the principle violated?",
  "सिद्धांत: किसी लोक सेवक को ऐसे निर्णय में भाग नहीं लेना चाहिए जिसमें किसी निकट संबंधी को आर्थिक लाभ या हानि होने वाली हो।\n\nनिम्नलिखित में से किस स्थिति में इस सिद्धांत का उल्लंघन होता है?",
  ["An officer approves a contract for a firm owned by her brother.",
   "An officer declines to review a tender after learning that her cousin has applied.",
   "An officer grants a licence to a firm in which none of her relatives has any interest.",
   "An officer's son applies for a post, and she hands the file to a colleague."],
  ["एक अधिकारी अपने भाई के स्वामित्व वाली फ़र्म के लिए एक अनुबंध स्वीकृत करती है।",
   "एक अधिकारी यह पता चलने पर कि उसकी चचेरी बहन ने आवेदन किया है, निविदा की समीक्षा करने से मना कर देती है।",
   "एक अधिकारी ऐसी फ़र्म को लाइसेंस देती है जिसमें उसके किसी संबंधी का कोई हित नहीं है।",
   "एक अधिकारी का बेटा किसी पद के लिए आवेदन करता है, और वह फ़ाइल एक सहकर्मी को सौंप देती है।"], 0,
  "The principle bars taking part in a decision in which a close relative stands to gain or lose financially, and approving a contract for her brother's firm is exactly that. "
  "Declining to review the cousin's tender and handing her son's file to a colleague are the conduct the principle asks for; a licence to a firm in which no relative has an interest does not touch the principle at all.",
  "सिद्धांत ऐसे निर्णय में भाग लेने पर रोक लगाता है जिसमें किसी निकट संबंधी को आर्थिक लाभ या हानि हो, और भाई की फ़र्म के लिए अनुबंध स्वीकृत करना ठीक यही है। "
  "चचेरी बहन की निविदा की समीक्षा से मना करना और बेटे की फ़ाइल सहकर्मी को सौंपना वही आचरण है जो सिद्धांत माँगता है; ऐसी फ़र्म को लाइसेंस देना जिसमें किसी संबंधी का हित नहीं, सिद्धांत को छूता ही नहीं।",
  "lr-sc-principle-applied-to-cases", pos=0)

# 3 -- the assumption a plan depends on
T(LR, "Statement-Conclusion/Assumption", "hard",
  "Argument: The city plans to cut the traffic jams in its centre by building a second bridge across the river.\n\nWhich one of the following is an assumption on which the plan depends?",
  "तर्क: शहर अपने केंद्र के यातायात जाम घटाने के लिए नदी पर दूसरा पुल बनाने की योजना बना रहा है।\n\nनिम्नलिखित में से कौन-सी पूर्वधारणा है जिस पर यह योजना निर्भर है?",
  ["Much of the centre's traffic is made up of vehicles crossing the river.",
   "The second bridge will cost less to build than the first one did.",
   "Most of the city's residents live on the far side of the river.",
   "Traffic jams in the centre will disappear entirely once the bridge opens."],
  ["केंद्र के यातायात का बड़ा भाग नदी पार करने वाले वाहनों का है।",
   "दूसरा पुल बनाने में पहले पुल से कम लागत आएगी।",
   "शहर के अधिकांश निवासी नदी के उस पार रहते हैं।",
   "पुल खुलते ही केंद्र के यातायात जाम पूरी तरह समाप्त हो जाएँगे।"], 0,
  "A second bridge can ease the jams in the centre only if a good part of that traffic is crossing the river; otherwise the new bridge carries traffic that was never in the jam. "
  "The plan does not depend on what the bridge costs or on where most residents live, and it aims to cut the jams, not to end them entirely.",
  "दूसरा पुल केंद्र के जाम तभी घटा सकता है जब उस यातायात का अच्छा-ख़ासा भाग नदी पार कर रहा हो; अन्यथा नया पुल वह यातायात ढोएगा जो कभी जाम में था ही नहीं। "
  "योजना इस पर निर्भर नहीं कि पुल कितने में बनेगा या अधिकांश निवासी कहाँ रहते हैं, और उसका लक्ष्य जाम घटाना है, पूरी तरह समाप्त करना नहीं।",
  "lr-sc-assumption-behind-a-second-bridge", pos=3)

# 4 -- a rectangular table tied to the compass
def _sa1():
    # Seats clockwise from above: 0 west end, 1 north side (west), 2 north side (east), 3 east end, 4 south side (east),
    # 5 south side (west). Everyone faces the centre, so a person's right is the next seat anticlockwise (-1).
    opposite = {0: 3, 3: 0, 1: 5, 5: 1, 2: 4, 4: 2}
    names = ["west end", "north side", "north side", "east end", "south side", "south side"]
    sols = []
    for rest in permutations("BCDEF"):
        s = dict(zip(rest, range(1, 6)))
        s["A"] = 0
        if s["F"] != (s["A"] - 1) % 6 or s["B"] != (s["A"] - 2) % 6 or s["C"] != opposite[s["B"]] or names[s["D"]] != "north side":
            continue
        sols.append(s)
    assert len(sols) == 1, sols
    return next(p for p, seat in sols[0].items() if seat == 3)
N(LR, "Seating Arrangement", "hard",
  "Six people, A, B, C, D, E and F, sit around a rectangular table that runs from west to east, all facing the centre. There is one seat at each end and two seats along each side, the north side and the south side. "
  "A sits at the west end. F sits to the immediate right of A, and B sits second to the right of A. C sits directly opposite B. D sits on the north side. Who sits at the east end?",
  "छह लोग, A, B, C, D, E और F, पश्चिम से पूर्व की ओर फैली एक आयताकार मेज़ के चारों ओर केंद्र की ओर मुँह करके बैठे हैं। हर छोर पर एक सीट है और हर लंबी भुजा, उत्तरी और दक्षिणी, पर दो-दो सीटें। "
  "A पश्चिमी छोर पर बैठा है। F, A के ठीक दाएँ बैठा है, और B, A के दाएँ से दूसरे स्थान पर। C, B के ठीक सामने बैठा है। D उत्तरी भुजा पर बैठा है। पूर्वी छोर पर कौन बैठा है?",
  ["B", "C", "D", "E"], 3,
  "A sits at the west end facing east, so A's right hand points south. The seat to A's immediate right is the western seat on the south side, F's; second to A's right is the next one along, the eastern seat on the south side, B's. "
  "C, directly opposite B, takes the eastern seat on the north side, and D, on the north side, the western one. That leaves the east end for E. "
  "Taking A's right to be the north side puts F and B on the north side, leaves no seat there for D, and so cannot be right.",
  "A पश्चिमी छोर पर पूर्व की ओर मुँह करके बैठा है, इसलिए A का दायाँ हाथ दक्षिण की ओर है। A के ठीक दाएँ की सीट दक्षिणी भुजा की पश्चिमी सीट है, F की; A के दाएँ से दूसरी उसके आगे वाली, दक्षिणी भुजा की पूर्वी सीट है, B की। "
  "B के ठीक सामने वाला C उत्तरी भुजा की पूर्वी सीट लेता है, और उत्तरी भुजा वाला D पश्चिमी सीट। इससे पूर्वी छोर E के लिए बचता है। "
  "A के दाएँ को उत्तरी भुजा मानने से F और B उत्तरी भुजा पर पहुँच जाते हैं, D के लिए वहाँ कोई सीट नहीं बचती, इसलिए वह पढ़ना सही नहीं हो सकता।",
  "lr-sa-rectangular-table-on-the-compass", _sa1)

# 5 -- the order of finishers in a race
def _sa2():
    sols = [o for o in permutations("PQRSTU")
            if o.index("S") == 5 and o.index("U") == 2 and o.index("U") < o.index("R") < o.index("T") and o.index("P") == o.index("Q") + 1]
    assert len(sols) == 1, sols
    return sols[0][0]
N(LR, "Seating Arrangement", "medium",
  "Six runners, P, Q, R, S, T and U, finished a race, no two of them together. S finished last. U finished third. R finished after U but before T. P finished immediately after Q. Who finished first?",
  "छह धावक, P, Q, R, S, T और U, एक दौड़ में पहुँचे, कोई भी दो एक साथ नहीं। S अंतिम रहा। U तीसरे स्थान पर रहा। R, U के बाद पर T से पहले पहुँचा। P, Q के ठीक बाद पहुँचा। पहले स्थान पर कौन रहा?",
  ["P", "Q", "R", "U"], 1,
  "S is sixth and U third. R finishes after U and before T, and after U only places 4 and 5 are left for them, so R is fourth and T fifth. That leaves places 1 and 2 for Q and P, "
  "and since P finishes immediately after Q, Q is first and P second. P is the usual slip, from reading 'immediately after' as 'just ahead of'.",
  "S छठा और U तीसरा है। R, U के बाद और T से पहले पहुँचता है, और U के बाद उनके लिए केवल स्थान 4 और 5 बचते हैं, इसलिए R चौथा और T पाँचवाँ है। इससे Q और P के लिए स्थान 1 और 2 बचते हैं, "
  "और चूँकि P, Q के ठीक बाद पहुँचता है, Q पहला और P दूसरा है। P सामान्य भूल है, 'ठीक बाद' को 'ठीक आगे' पढ़ने से।",
  "lr-sa-order-of-finishers", _sa2)

# 6 -- houses painted in a row
def _sa3():
    sols = []
    for row in permutations(["Red", "Blue", "Green", "White", "Yellow"]):   # houses 1-5, left to right
        p = {col: i for i, col in enumerate(row)}
        if p["Green"] != p["White"] + 1 or p["Red"] not in (0, 4) or abs(p["Blue"] - p["Red"]) != 1:
            continue
        if abs(p["Yellow"] - p["Blue"]) == 1 or p["White"] > p["Blue"]:
            continue
        sols.append(row)
    assert len(sols) == 1, sols
    return sols[0][2]
N(LR, "Seating Arrangement", "medium",
  "Five houses in a row, numbered 1 to 5 from left to right, are painted red, blue, green, white and yellow, one colour each. The green house is immediately to the right of the white house. "
  "The red house is at one end of the row, and the blue house is next to it. The yellow house is not next to the blue house. The white house is to the left of the blue house. What colour is the middle house?",
  "एक पंक्ति में बाएँ से दाएँ 1 से 5 तक क्रमांकित पाँच मकान लाल, नीले, हरे, सफ़ेद और पीले रंग से रँगे हैं, हर एक एक रंग से। हरा मकान सफ़ेद मकान के ठीक दाएँ है। "
  "लाल मकान पंक्ति के एक छोर पर है, और नीला मकान उसके बगल में है। पीला मकान नीले मकान के बगल में नहीं है। सफ़ेद मकान नीले मकान के बाईं ओर है। बीच वाला मकान किस रंग का है?",
  ["Blue", "Green", "White", "Yellow"], 1,
  "The red house is at an end with blue beside it. If red were house 1 and blue house 2, white could not be to the left of blue, so red is house 5 and blue house 4. White and green must stand side by side, "
  "green on the right, in houses 1 to 3, and yellow, kept away from blue, cannot be house 3: so yellow is house 1, white 2 and green 3. The middle house is green. "
  "White is the answer if the last clue is overlooked, which allows red, blue, white, green, yellow from the left.",
  "लाल मकान एक छोर पर है और नीला उसके बगल में। यदि लाल मकान 1 और नीला मकान 2 होता, तो सफ़ेद नीले के बाईं ओर नहीं हो सकता, इसलिए लाल मकान 5 और नीला मकान 4 है। सफ़ेद और हरा अगल-बगल होने चाहिए, "
  "हरा दाईं ओर, मकान 1 से 3 में, और नीले से दूर रखा गया पीला मकान 3 नहीं हो सकता: अतः पीला मकान 1, सफ़ेद 2 और हरा 3 है। बीच वाला मकान हरा है। "
  "यदि अंतिम सूत्र अनदेखा हो, तो बाएँ से लाल, नीला, सफ़ेद, हरा, पीला भी संभव होता है, और उत्तर सफ़ेद आता।",
  "lr-sa-houses-painted-in-a-row", _sa3,
  opts_hi=["नीला", "हरा", "सफ़ेद", "पीला"])

# 7 -- the only child of a grandmother
T(LR, "Blood Relation", "medium",
  "Pointing to a woman, a man says, 'She is the daughter of the only child of my grandmother.' How is the woman related to the man?",
  "एक महिला की ओर इशारा करते हुए एक पुरुष कहता है, 'वह मेरी दादी की इकलौती संतान की बेटी है।' वह महिला उस पुरुष की क्या लगती है?",
  ["Sister", "Cousin", "Niece", "Aunt"], ["बहन", "चचेरी बहन", "भतीजी", "बुआ"], 0,
  "The grandmother's only child must be one of the man's own parents, since she has no other child. The woman is that parent's daughter, so she is the man's sister. "
  "'Cousin' and 'aunt' assume that the grandmother had other children; a niece would be the daughter of the man's brother or sister.",
  "दादी की इकलौती संतान पुरुष के पिता ही हो सकते हैं, क्योंकि दादी की कोई दूसरी संतान नहीं है। महिला उन्हीं की बेटी है, इसलिए वह पुरुष की बहन है। "
  "'चचेरी बहन' और 'बुआ' मान लेते हैं कि दादी की दूसरी संतानें भी थीं; भतीजी पुरुष के भाई की बेटी होती।",
  "lr-br-only-child-of-a-grandmother", pos=0)

# 8 -- daughters who share a brother
def _br2():
    daughters, sons = 3, 1                  # 'each daughter has exactly one brother': the same brother for all
    assert all(sons == 1 for _ in range(daughters))
    return str(daughters + sons)
N(LR, "Blood Relation", "easy",
  "A man has three daughters, and each of the daughters has exactly one brother. How many children does the man have?",
  "एक व्यक्ति की तीन बेटियाँ हैं, और हर बेटी का ठीक एक भाई है। उस व्यक्ति के कितने बच्चे हैं?",
  ["3", "4", "6", "7"], 1,
  "Every daughter has the same single brother -- the man's only son -- so he has 3 daughters and 1 son: 4 children. 6 gives each daughter a brother of her own; 7 counts the man as well; 3 forgets the son.",
  "हर बेटी का एक ही भाई है -- उस व्यक्ति का इकलौता बेटा -- इसलिए उसकी 3 बेटियाँ और 1 बेटा है: 4 बच्चे। 6 हर बेटी को अलग भाई देता है; 7 उस व्यक्ति को भी गिन लेता है; 3 बेटे को भूल जाता है।",
  "lr-br-daughters-share-a-brother", _br2)

# 9 -- two walkers who end at the same spot
def _dd1():
    p = (0 - 5, 10)                          # 10 km north, then left (west) 5 km
    q = (-5, 0 + 10)                         # 5 km west, then right (north) 10 km
    d2 = (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2
    return f"{round(d2 ** 0.5)} km"
N(LR, "Direction & Distance", "medium",
  "P walks 10 km north, turns left and walks 5 km. Q starts from the same point, walks 5 km west, turns right and walks 10 km. How far apart are P and Q at the end?",
  "P, 10 किमी उत्तर चलता है, बाएँ मुड़ता है और 5 किमी चलता है। Q उसी स्थान से चलकर 5 किमी पश्चिम जाता है, दाएँ मुड़ता है और 10 किमी चलता है। अंत में P और Q एक-दूसरे से कितनी दूर हैं?",
  ["0 km", "5 km", "10 km", "15 km"], 0,
  "P goes 10 km north and then, turning left, 5 km west. Q goes 5 km west and then, turning right, 10 km north. Both end 10 km north and 5 km west of the start -- at the same spot. "
  "15 km adds up the legs; 10 km and 5 km take one leg or the other as the gap.",
  "P, 10 किमी उत्तर और फिर बाएँ मुड़कर 5 किमी पश्चिम जाता है। Q, 5 किमी पश्चिम और फिर दाएँ मुड़कर 10 किमी उत्तर जाता है। दोनों आरंभ स्थान से 10 किमी उत्तर और 5 किमी पश्चिम पर पहुँचते हैं -- एक ही स्थान पर। "
  "15 किमी हिस्सों को जोड़ता है; 10 किमी और 5 किमी किसी एक हिस्से को ही दूरी मान लेते हैं।",
  "lr-dd-two-walkers-meet-again", _dd1,
  opts_hi=["0 किमी", "5 किमी", "10 किमी", "15 किमी"])

# 10 -- compass names turned through 135°
def _dd2():
    names = {0: "North", 45: "North-east", 90: "East", 135: "South-east", 180: "South", 225: "South-west", 270: "West", 315: "North-west"}
    turn = 135
    assert names[(0 + turn) % 360] == "South-east" and names[(90 + turn) % 360] == "South-west"
    assert names[(270 - turn) % 360] == "South-east"         # the wrong-way slip
    return names[(270 + turn) % 360]
N(LR, "Direction & Distance", "hard",
  "In a certain code, the directions are renamed: north is called south-east, east is called south-west, and every other direction is renamed in the same way. What is west called in this code?",
  "एक निश्चित कूट में दिशाओं के नाम बदल दिए गए हैं: उत्तर को दक्षिण-पूर्व कहा जाता है, पूर्व को दक्षिण-पश्चिम, और बाक़ी हर दिशा का नाम इसी तरह बदला गया है। इस कूट में पश्चिम को क्या कहा जाता है?",
  ["North", "North-east", "South-east", "North-west"], 1,
  "Each name moves 135° clockwise: north (0°) becomes south-east (135°), and east (90°) becomes south-west (225°). West, at 270°, becomes 270° + 135° = 405°, that is 45°: north-east. "
  "South-east comes from turning the names the other way; north and north-west use a turn of 90° or 45° instead of 135°.",
  "हर नाम 135° दक्षिणावर्त खिसकता है: उत्तर (0°) दक्षिण-पूर्व (135°) बन जाता है, और पूर्व (90°) दक्षिण-पश्चिम (225°)। पश्चिम, 270° पर, 270° + 135° = 405°, यानी 45°, बन जाता है: उत्तर-पूर्व। "
  "दक्षिण-पूर्व नामों को उलटी दिशा में घुमाने से आता है; उत्तर और उत्तर-पश्चिम 135° के बजाय 90° या 45° का मोड़ लेते हैं।",
  "lr-dd-compass-names-turned", _dd2,
  opts_hi=["उत्तर", "उत्तर-पूर्व", "दक्षिण-पूर्व", "उत्तर-पश्चिम"])

# 11 -- a mirror-image alphabet
def _cd1():
    mirror = lambda w: "".join(chr(155 - ord(ch)) for ch in w)     # A <-> Z, B <-> Y, ...
    assert mirror("GOLD") == "TLOW"
    return mirror("CODE")
N(LR, "Coding-Decoding", "easy",
  "In a certain code, GOLD is written as TLOW. How is CODE written in that code?",
  "एक निश्चित कूट में GOLD को TLOW लिखा जाता है। उसी कूट में CODE को कैसे लिखा जाएगा?",
  ["DPEF", "XKWV", "XLVW", "XLWV"], 3,
  "G → T, O → L, L → O and D → W: each letter is swapped with the one in the same place counted from the other end of the alphabet (A ↔ Z, B ↔ Y, ...), so the positions of each pair add up to 27. "
  "CODE becomes X (for C), L (for O), W (for D) and V (for E): XLWV. DPEF moves each letter one place forward; XKWV writes O as K; XLVW swaps the last two letters.",
  "G → T, O → L, L → O और D → W: हर अक्षर वर्णमाला के दूसरे छोर से गिनने पर उसी स्थान वाले अक्षर से बदला गया है (A ↔ Z, B ↔ Y, ...), इसलिए हर जोड़ी के स्थानों का योग 27 है। "
  "CODE बनता है X (C के लिए), L (O के लिए), W (D के लिए) और V (E के लिए): XLWV। DPEF हर अक्षर को एक स्थान आगे खिसकाता है; XKWV, O को K लिखता है; XLVW अंतिम दो अक्षर आपस में बदल देता है।",
  "lr-cd-mirror-alphabet", _cd1)

# 12 -- a rule found from three Pythagorean triples
def _cd2():
    # Two examples are not enough: 6 # 8 = 100 and 5 # 12 = 169 also fit (a + b - 4)², which gives 361 for 8 # 15.
    # With three, search both families -- (p a + q b + r)² and u a² + v b² + w a b + z, small whole-number
    # coefficients -- and require that every rule that fits all three examples gives the same value for 7 # 24.
    ex = [((6, 8), 100), ((5, 12), 169), ((8, 15), 289)]
    fits = []
    for p in range(-3, 4):
        for q in range(-3, 4):
            for r in range(-12, 13):
                if all((p * a + q * b + r) ** 2 == v for (a, b), v in ex):
                    fits.append(lambda a, b, p=p, q=q, r=r: (p * a + q * b + r) ** 2)
    for u in range(-3, 4):
        for v_ in range(-3, 4):
            for w in range(-3, 4):
                for z in range(-12, 13):
                    if all(u * a * a + v_ * b * b + w * a * b + z == v for (a, b), v in ex):
                        fits.append(lambda a, b, u=u, v_=v_, w=w, z=z: u * a * a + v_ * b * b + w * a * b + z)
    answers = {f(7, 24) for f in fits}
    assert fits and len(answers) == 1, answers
    return str(answers.pop())
N(LR, "Coding-Decoding", "medium",
  "In a certain code, 6 # 8 = 100, 5 # 12 = 169 and 8 # 15 = 289. Following the same rule, what is 7 # 24?",
  "एक निश्चित कूट में 6 # 8 = 100, 5 # 12 = 169 और 8 # 15 = 289। उसी नियम से 7 # 24 क्या होगा?",
  ["168", "576", "625", "961"], 2,
  "6² + 8² = 36 + 64 = 100, 5² + 12² = 25 + 144 = 169 and 8² + 15² = 64 + 225 = 289, so a # b = a² + b². Then 7 # 24 = 49 + 576 = 625. "
  "168 is the product 7 × 24; 576 squares only the larger number; 961 = 31² squares the sum instead of adding the squares.",
  "6² + 8² = 36 + 64 = 100, 5² + 12² = 25 + 144 = 169 और 8² + 15² = 64 + 225 = 289, इसलिए a # b = a² + b²। तब 7 # 24 = 49 + 576 = 625। "
  "168 गुणनफल 7 × 24 है; 576 केवल बड़ी संख्या का वर्ग लेता है; 961 = 31² वर्गों को जोड़ने के बजाय योग का वर्ग लेता है।",
  "lr-cd-rule-from-pythagorean-triples", _cd2)

# 13 -- paint on at least one face
def _cp1():
    n = 5
    painted = sum(1 for x, y, z in product(range(n), repeat=3) if 0 in (x, y, z) or n - 1 in (x, y, z))
    assert n ** 3 - painted == 27 and 6 * (n - 2) ** 2 == 54
    return str(painted)
N(LR, "Cube Painting", "medium",
  "A wooden cube is painted on all its faces and then cut into 125 equal smaller cubes. How many of the smaller cubes have paint on at least one face?",
  "लकड़ी के एक घन को सभी फलकों पर रँगकर 125 बराबर छोटे घनों में काटा जाता है। कितने छोटे घनों के कम से कम एक फलक पर रंग है?",
  ["27", "54", "98", "125"], 2,
  "125 = 5 × 5 × 5, so the big cube is 5 small cubes along each edge. The cubes with no paint form the hidden inner block, 3 × 3 × 3 = 27, and all the others, 125 - 27 = 98, have paint on at least one face. "
  "27 is the number with no paint; 54 = 6 × 9 counts only the cubes with exactly one painted face; 125 counts every cube.",
  "125 = 5 × 5 × 5, इसलिए बड़े घन की हर कोर पर 5 छोटे घन हैं। बिना रंग वाले घन भीतर छिपा खंड बनाते हैं, 3 × 3 × 3 = 27, और बाक़ी सभी, 125 - 27 = 98, के कम से कम एक फलक पर रंग है। "
  "27 बिना रंग वाले घनों की संख्या है; 54 = 6 × 9 केवल ठीक एक रँगे फलक वाले घन गिनता है; 125 हर घन गिनता है।",
  "lr-cp-paint-on-at-least-one-face", _cp1)

# 14 -- poets who are not painters
def _sy1():
    regions = list(product((0, 1), repeat=3))        # (pilot, painter, poet)
    one = two = True
    for mask in range(1, 1 << 8):
        full = [r for k, r in enumerate(regions) if mask >> k & 1]
        if any(pl and pa for pl, pa, po in full) or any(pa and not po for pl, pa, po in full) or not any(pl and po for pl, pa, po in full):
            continue
        one &= any(po and not pa for pl, pa, po in full)
        two &= not any(pl and po for pl, pa, po in full)
    return c.T2R[{(True, False): 0, (False, True): 1, (True, True): 2, (False, False): 3}[(one, two)]]
S2(LR, "Syllogism", "medium",
   "Statements: No pilot is a painter. All painters are poets. Some pilots are poets.\n\nWhich of the following conclusions follow(s) from the statements?",
   "कथन: कोई भी पायलट चित्रकार नहीं है। सभी चित्रकार कवि हैं। कुछ पायलट कवि हैं।\n\nनिम्नलिखित में से कौन-सा/से निष्कर्ष कथनों से निकलता/निकलते है/हैं?",
   ["Some poets are not painters.", "No pilot is a poet."],
   ["कुछ कवि चित्रकार नहीं हैं।", "कोई भी पायलट कवि नहीं है।"], 0,
   "Only I follows. The pilots who are poets cannot be painters, since no pilot is a painter, so they are poets who are not painters (I). II contradicts the third statement. "
   "The trap is to read 'all painters are poets' as 'all poets are painters', which would seem to rule out I.",
   "केवल I निकलता है। जो पायलट कवि हैं, वे चित्रकार नहीं हो सकते, क्योंकि कोई पायलट चित्रकार नहीं है, इसलिए वे ऐसे कवि हैं जो चित्रकार नहीं हैं (I)। II तीसरे कथन का खंडन करता है। "
   "जाल 'सभी चित्रकार कवि हैं' को 'सभी कवि चित्रकार हैं' पढ़ना है, जिससे I असंभव लगने लगता।",
   "lr-sy-poets-who-are-not-painters", roman=True, check=_sy1)

# 15 -- three speakers, only one kind certain
def _tl1():
    worlds = [(a, b, cc) for a, b, cc in product((True, False), repeat=3) if a == (not b) and b == (a == cc)]
    claims = {"A is a truth-teller": lambda w: w[0], "B is a truth-teller": lambda w: w[1],
              "C is a liar": lambda w: not w[2], "C is a truth-teller": lambda w: w[2]}
    sure = [name for name, test in claims.items() if all(test(w) for w in worlds)]
    assert len(worlds) == 2
    return sure[0] if len(sure) == 1 else "?"
N(LR, "Truth-Liar", "hard",
  "Each of A, B and C is either a truth-teller, who always tells the truth, or a liar, who always lies. A says, 'B is a liar.' B says, 'A and C are of the same kind.' Which one of the following must be true?",
  "A, B और C में से हर एक या तो सत्यवादी है, जो सदा सच बोलता है, या झूठा, जो सदा झूठ बोलता है। A कहता है, 'B झूठा है।' B कहता है, 'A और C एक ही प्रकार के हैं।' निम्नलिखित में से क्या अवश्य सत्य है?",
  ["A is a truth-teller", "B is a truth-teller", "C is a liar", "C is a truth-teller"], 2,
  "A's remark makes A and B opposite kinds: if A tells the truth, B lies, and if A lies, B tells the truth. B's statement then settles C either way. If B lies, A and C differ; A is truthful, so C is a liar. "
  "If B tells the truth, A and C are alike; A lies, so C is a liar. C is a liar in both cases, while A's and B's kinds stay open, so neither 'A is a truth-teller' nor 'B is a truth-teller' must hold.",
  "A की बात A और B को उलटे प्रकार का बनाती है: यदि A सच बोलता है तो B झूठ बोलता है, और यदि A झूठ बोलता है तो B सच। फिर B का कथन दोनों ही स्थितियों में C तय कर देता है। यदि B झूठ बोलता है, तो A और C अलग हैं; A सत्यवादी है, इसलिए C झूठा है। "
  "यदि B सच बोलता है, तो A और C एक जैसे हैं; A झूठा है, इसलिए C झूठा है। दोनों स्थितियों में C झूठा है, जबकि A और B का प्रकार खुला रहता है, इसलिए न 'A सत्यवादी है' अवश्य सत्य है न 'B सत्यवादी है'।",
  "lr-tl-only-c-is-certain", _tl1,
  opts_hi=["A सत्यवादी है", "B सत्यवादी है", "C झूठा है", "C सत्यवादी है"])

# ---- the data-sufficiency block's three Reasoning items
def _ds1():
    # Worlds: is N M's own child (else a stepson through M's husband), and who is M's one child.
    worlds = [{"n_is_ms_child": own} for own in (True, False)]
    s1 = [w["n_is_ms_child"] for w in worlds]                       # I: N is the son of M's husband -- either way
    s2 = [w["n_is_ms_child"] for w in worlds]                       # II: M has one child -- N or someone else
    both = [w["n_is_ms_child"] for w in worlds]                     # still either way
    return _ds(s1, s2, both)
DS(LR, "hard",
   "Is M the mother of N?",
   "क्या M, N की माँ है?",
   "N is the son of M's husband.", "N, M के पति का बेटा है।",
   "M has only one child.", "M की केवल एक संतान है।",
   3,
   "Statement I allows N to be M's son or her husband's son from another marriage. Statement II says M has one child but not who that child is. Even together, N may be M's one child or a stepson while her one child is someone else. "
   "So the question cannot be answered. The trap is to assume that a husband's son must also be his wife's son.",
   "कथन I के अनुसार N, M का बेटा भी हो सकता है और उसके पति की दूसरी शादी से हुआ बेटा भी। कथन II कहता है कि M की एक संतान है, पर यह नहीं कि वह कौन है। दोनों साथ लेकर भी N, M की वह एक संतान हो सकता है या सौतेला बेटा, जबकि उसकी अपनी संतान कोई और हो। "
   "अतः प्रश्न का उत्तर नहीं दिया जा सकता। जाल यह मान लेना है कि पति का बेटा उसकी पत्नी का भी बेटा होगा।",
   "lr-ds-a-stepson-not-ruled-out", _ds1)

def _ds2():
    worlds = list(product((True, False), repeat=2))                  # (rained on Monday, match played on Monday)
    rule = lambda rain, played: not (rain and played)               # I: rain cancels the match
    s1 = [rain for rain, played in worlds if rule(rain, played)]
    s2 = [rain for rain, played in worlds if played]
    both = [rain for rain, played in worlds if rule(rain, played) and played]
    return _ds(s1, s2, both)
DS(LR, "medium",
   "Did it rain in the town on Monday?",
   "क्या सोमवार को कस्बे में वर्षा हुई?",
   "Whenever it rains in the town, the evening football match there is cancelled.", "जब भी कस्बे में वर्षा होती है, वहाँ शाम का फ़ुटबॉल मैच रद्द कर दिया जाता है।",
   "The evening football match in the town was played on Monday.", "सोमवार को कस्बे में शाम का फ़ुटबॉल मैच खेला गया।",
   2,
   "Statement I alone says nothing about Monday, and Statement II alone says nothing about rain. Together: rain would have cancelled the match, but the match was played, so it did not rain on Monday. Both statements are needed.",
   "कथन I अकेला सोमवार के बारे में कुछ नहीं कहता, और कथन II अकेला वर्षा के बारे में कुछ नहीं। दोनों साथ: वर्षा होती तो मैच रद्द हो जाता, पर मैच खेला गया, इसलिए सोमवार को वर्षा नहीं हुई। दोनों कथन ज़रूरी हैं।",
   "lr-ds-a-match-rain-would-cancel", _ds2)

def _ds3():
    s1 = ["east"]                                                    # facing the rising sun
    s2 = ["east"]                                                    # morning sun in the east casts shadows west; shadow behind her
    return _ds(s1, s2, s1)
DS(LR, "medium",
   "In which direction is Asha facing?",
   "आशा किस दिशा की ओर मुँह किए है?",
   "At sunrise, Asha is facing the rising sun.", "सूर्योदय के समय आशा उगते सूर्य की ओर मुँह किए है।",
   "It is morning, and Asha's shadow falls directly behind her.", "सुबह का समय है, और आशा की छाया ठीक उसके पीछे पड़ती है।",
   1,
   "Statement I: the sun rises in the east, so she faces east. Statement II: in the morning the sun is in the east and shadows point west; a shadow directly behind her means she faces away from it, towards the east. "
   "Either statement alone answers the question.",
   "कथन I: सूर्य पूर्व में उगता है, इसलिए वह पूर्व की ओर मुँह किए है। कथन II: सुबह सूर्य पूर्व में होता है और छायाएँ पश्चिम की ओर पड़ती हैं; छाया ठीक उसके पीछे होने का अर्थ है कि वह उससे उलटी ओर, यानी पूर्व की ओर, मुँह किए है। "
   "कोई भी एक कथन अकेले प्रश्न का उत्तर दे देता है।",
   "lr-ds-a-morning-shadow", _ds3)
