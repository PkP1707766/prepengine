# -*- coding: utf-8 -*-
"""CSAT Level 2 · Test 2 -- Logical Reasoning (18 items: 15 in the Reasoning slots, 3 in the data-sufficiency block).

Same mix as Test 1 with new traps: a row facing south (its 'right end' is the west end), a flat clock turned
to the north-east, a coding rule found from two examples, a word code solved across sentences, a cube with
opposite faces painted alike, a family puzzle whose gender cannot be fixed, a cause-effect pair, and a
gender-neutral name in a data-sufficiency item. Difficulty 3 easy / 10 medium / 5 hard. Arrangement, code,
cube, syllogism and truth-teller keys are found by checking every case."""
from itertools import permutations, product
import csat_common as c
from csat_common import N, T, S2, DS, LR

def _two(one_follows, two_follows):
    return c.T2R[{(True, False): 0, (False, True): 1, (True, True): 2, (False, False): 3}[(one_follows, two_follows)]]

CONC = "Which of the following conclusions follow(s) from the statement?"
CONC_HI = "निम्नलिखित में से कौन-सा/से निष्कर्ष कथन से निकलता/निकलते है/हैं?"
ASSUMPT = "Which of the following assumptions is/are implicit in the statement?"
ASSUMPT_HI = "निम्नलिखित में से कौन-सी/से पूर्वधारणा/एँ कथन में अंतर्निहित है/हैं?"

# 1 -- assumptions behind a policy
S2(LR, "Statement-Conclusion/Assumption", "medium",
   "Statement: The government has decided to raise the minimum age for buying tobacco products from 18 to 21 years.\n\n" + ASSUMPT,
   "कथन: सरकार ने तंबाकू उत्पाद ख़रीदने की न्यूनतम आयु 18 से बढ़ाकर 21 वर्ष करने का निर्णय लिया है।\n\n" + ASSUMPT_HI,
   ["Raising the minimum age is likely to reduce tobacco use among young people.", "People above 21 years of age do not use tobacco."],
   ["न्यूनतम आयु बढ़ाने से युवाओं में तंबाकू का उपयोग घटने की संभावना है।", "21 वर्ष से अधिक आयु के लोग तंबाकू का उपयोग नहीं करते।"], 0,
   "Only I is implicit: a government raises the age limit only if it expects the change to cut tobacco use among the young; otherwise the decision has no point. "
   "II is not assumed and is plainly false -- the rule leaves older buyers alone because it targets the start of the habit, not because older people do not smoke.",
   "केवल I अंतर्निहित है: सरकार आयु सीमा तभी बढ़ाती है जब उसे उम्मीद हो कि इससे युवाओं में तंबाकू का उपयोग घटेगा; अन्यथा निर्णय का कोई अर्थ नहीं। "
   "II पूर्वधारणा नहीं है और स्पष्ट रूप से असत्य है -- नियम अधिक आयु के ख़रीदारों को इसलिए छोड़ता है कि वह आदत की शुरुआत को लक्ष्य करता है, इसलिए नहीं कि अधिक आयु के लोग धूम्रपान नहीं करते।",
   "lr-sc-tobacco-age-assumptions", roman=True)

# 2 -- row facing south
def _sa1():
    # Seats 1-7 numbered from west to east. Facing south, a person's right is west (lower number).
    sols = []
    for row in permutations("ABCDEFG"):
        pos = {p: i + 1 for i, p in enumerate(row)}
        if pos["D"] != 4 or pos["A"] != pos["D"] - 3 or pos["B"] != pos["D"] + 1:
            continue
        if pos["E"] not in (1, 7) or pos["C"] != pos["B"] - 2 or abs(pos["G"] - pos["E"]) == 1:
            continue
        sols.append(row)
    assert len(sols) == 1, sols
    return sols[0][0]                     # the extreme right end of people facing south is the west end
T(LR, "Seating Arrangement", "medium",
  "Seven friends A, B, C, D, E, F and G sit in a row, all facing south. D sits exactly in the middle of the row. A sits third to the right of D, and B sits to the immediate left of D. "
  "E sits at one of the ends, and C sits second to the right of B. G does not sit next to E. Who sits at the extreme right end of the row?",
  "सात मित्र A, B, C, D, E, F और G एक पंक्ति में दक्षिण की ओर मुँह करके बैठे हैं। D पंक्ति के ठीक बीच में बैठा है। A, D के दाएँ से तीसरे स्थान पर है, और B, D के ठीक बाएँ बैठा है। "
  "E किसी एक छोर पर बैठा है, और C, B के दाएँ से दूसरे स्थान पर है। G, E के बगल में नहीं बैठा है। पंक्ति के बिल्कुल दाएँ छोर पर कौन बैठा है?",
  ["A", "E", "G", "F"], ["A", "E", "G", "F"], 0,
  "For people facing south, their right is west. D is in seat 4 of 7. Third to D's right is the westernmost seat, so A is at one end; B is just to D's left, the seat east of D. "
  "E must take the other end, the eastern one. Second to B's right is the seat just west of D, so C sits beside D on that side. F and G take the two remaining seats, and G, not allowed beside E, is next to A. "
  "From west to east: A G C D B F E. The extreme right end of people facing south is the western end, where A sits. E sits at the right end only as seen by someone facing the row -- the usual trap.",
  "दक्षिण की ओर मुँह किए लोगों का दायाँ पश्चिम है। D, 7 में से चौथे स्थान पर है। D के दाएँ से तीसरा स्थान सबसे पश्चिमी है, इसलिए A एक छोर पर है; B, D के ठीक बाएँ, यानी D के पूर्व वाले स्थान पर है। "
  "E को दूसरा, पूर्वी छोर लेना होगा। B के दाएँ से दूसरा स्थान D के ठीक पश्चिम वाला है, इसलिए C उस ओर D के बगल में बैठा है। F और G बचे दो स्थान लेते हैं, और G, जो E के बगल में नहीं बैठ सकता, A के बगल में है। "
  "पश्चिम से पूर्व: A G C D B F E। दक्षिण की ओर मुँह किए लोगों का बिल्कुल दायाँ छोर पश्चिमी छोर है, जहाँ A बैठा है। E केवल पंक्ति की ओर देखने वाले व्यक्ति के दाएँ छोर पर है -- यही सामान्य जाल है।",
  "lr-sa-row-facing-south", check=_sa1)

# 3 -- easy relation
T(LR, "Blood Relation", "easy",
  "Introducing a man, a woman says, 'He is the son of the brother of my mother.' How is the man related to the woman?",
  "एक पुरुष का परिचय देते हुए एक महिला कहती है, 'वह मेरी माँ के भाई का बेटा है।' वह पुरुष महिला का क्या लगता है?",
  ["Cousin", "Nephew", "Brother", "Uncle"], ["ममेरा भाई", "भतीजा", "भाई", "मामा"], 0,
  "Her mother's brother is her maternal uncle, and his son is her cousin (her मामा's son). 'Uncle' stops one step too early, at the brother; 'nephew' would be a sibling's son; 'brother' would need the same parents.",
  "उसकी माँ का भाई उसका मामा है, और मामा का बेटा उसका ममेरा भाई है। 'मामा' एक कदम पहले, भाई पर ही रुक जाता है; 'भतीजा' भाई-बहन का बेटा होता; 'भाई' के लिए माता-पिता एक होने चाहिए।",
  "lr-br-son-of-mothers-brother")

# 4 -- a turned clock
def _dd1():
    twelve = 45                                 # the minute hand at 3:00 points to 12, which faces north-east
    hour_hand = (twelve + 7.5 * 30) % 360
    return {0: "North", 90: "East", 180: "South", 270: "West", 45: "North-east", 135: "South-east", 225: "South-west", 315: "North-west"}[hour_hand]
T(LR, "Direction & Distance", "hard",
  "A clock is laid flat on a table so that at 3:00 p.m. its minute hand points towards the north-east. In which direction will its hour hand point at 7:30 p.m.?",
  "एक घड़ी मेज़ पर सपाट इस प्रकार रखी है कि दोपहर 3:00 बजे उसकी मिनट की सुई उत्तर-पूर्व की ओर है। शाम 7:30 बजे उसकी घंटे की सुई किस दिशा में होगी?",
  ["West", "South-west", "North-west", "South"], ["पश्चिम", "दक्षिण-पश्चिम", "उत्तर-पश्चिम", "दक्षिण"], 0,
  "At 3:00 the minute hand points to 12, so the clock's 12 faces north-east. At 7:30 the hour hand is halfway between 7 and 8, which is 7.5 × 30° = 225° clockwise from 12. "
  "Turning 225° clockwise from north-east (45°) gives 270°, that is west. South-west is where the hour hand would point if the 12 faced north; the other options miscount the half-hour.",
  "3:00 बजे मिनट की सुई 12 पर होती है, इसलिए घड़ी का 12 उत्तर-पूर्व की ओर है। 7:30 बजे घंटे की सुई 7 और 8 के बीच में होती है, जो 12 से 7.5 × 30° = 225° दक्षिणावर्त है। "
  "उत्तर-पूर्व (45°) से 225° दक्षिणावर्त घूमने पर 270°, यानी पश्चिम, आता है। दक्षिण-पश्चिम तब होता जब 12 उत्तर की ओर होता; बाक़ी विकल्प आधे घंटे की ग़लत गिनती करते हैं।",
  "lr-dd-turned-clock-hour-hand", check=_dd1)

# 5 -- easy ranking with a swap
N(LR, "Seating Arrangement", "easy",
  "In a row of girls, Rita is 9th from the left and Sita is 12th from the right. When they interchange their positions, Rita becomes 15th from the left. How many girls are there in the row?",
  "लड़कियों की एक पंक्ति में रीता बाएँ से 9वें और सीता दाएँ से 12वें स्थान पर है। जब वे अपने स्थान आपस में बदल लेती हैं, तो रीता बाएँ से 15वें स्थान पर आ जाती है। पंक्ति में कितनी लड़कियाँ हैं?",
  ["24", "25", "26", "27"], 2,
  "After the swap Rita stands where Sita stood, so Sita's old place is 15th from the left and 12th from the right. The row therefore has 15 + 12 - 1 = 26 girls. "
  "27 forgets to subtract 1 for counting Sita's place twice; 24 and 25 use Rita's old position, 9th, or subtract twice.",
  "स्थान बदलने के बाद रीता वहाँ है जहाँ सीता थी, इसलिए सीता का पुराना स्थान बाएँ से 15वाँ और दाएँ से 12वाँ है। अतः पंक्ति में 15 + 12 - 1 = 26 लड़कियाँ हैं। "
  "27 में सीता के स्थान को दो बार गिनने के लिए 1 घटाना भूल गए हैं; 24 और 25 रीता का पुराना 9वाँ स्थान लेते हैं या दो बार घटाते हैं।",
  "lr-sa-rank-swap-row-length", lambda: str(15 + 12 - 1))

# 6 -- coding rule from two examples
def _cd1():
    code = lambda w: sum(ord(ch) - 64 for ch in w) * len(w)
    assert code("BAD") == 21 and code("FACE") == 60
    return str(code("CAT"))
N(LR, "Coding-Decoding", "medium",
  "In a certain code, BAD is written as 21 and FACE as 60. How is CAT written in that code?",
  "एक निश्चित कूट में BAD को 21 और FACE को 60 लिखा जाता है। उसी कूट में CAT को कैसे लिखा जाएगा?",
  ["24", "48", "72", "96"], 2,
  "Give each letter its place in the alphabet. BAD: 2 + 1 + 4 = 7, and 7 × 3 letters = 21. FACE: 6 + 1 + 3 + 5 = 15, and 15 × 4 letters = 60. So the code is the sum of the letter values times the number of letters. "
  "CAT: 3 + 1 + 20 = 24, and 24 × 3 = 72. 24 stops at the sum; 48 and 96 multiply by 2 or 4 instead of by the 3 letters.",
  "हर अक्षर को वर्णमाला में उसका स्थान दीजिए। BAD: 2 + 1 + 4 = 7, और 7 × 3 अक्षर = 21। FACE: 6 + 1 + 3 + 5 = 15, और 15 × 4 अक्षर = 60। अतः कूट अक्षरों के मानों का योग गुणा अक्षरों की संख्या है। "
  "CAT: 3 + 1 + 20 = 24, और 24 × 3 = 72। 24 योग पर रुक जाता है; 48 और 96, 3 अक्षरों के बजाय 2 या 4 से गुणा करते हैं।",
  "lr-cd-sum-times-length-rule", _cd1)

# 7 -- cause and effect
T(LR, "Statement-Conclusion/Assumption", "medium",
  "Consider the two statements:\nI. The price of onions has risen sharply in city markets this month.\nII. Heavy rain damaged the onion crop in the main growing States a few weeks ago.\n\nWhich one of the following best describes the relationship between them?",
  "दो कथनों पर विचार कीजिए:\nI. इस महीने शहरों के बाज़ारों में प्याज़ के दाम तेज़ी से बढ़े हैं।\nII. कुछ सप्ताह पहले मुख्य उत्पादक राज्यों में भारी वर्षा ने प्याज़ की फ़सल को नुक़सान पहुँचाया।\n\nनिम्नलिखित में से कौन-सा उनके बीच के संबंध को सबसे अच्छी तरह बताता है?",
  ["Statement I is the effect and Statement II is its cause",
   "Statement I is the cause and Statement II is its effect",
   "Both statements are effects of some common cause",
   "Both statements are independent causes"],
  ["कथन I प्रभाव है और कथन II उसका कारण",
   "कथन I कारण है और कथन II उसका प्रभाव",
   "दोनों कथन किसी एक ही कारण के प्रभाव हैं",
   "दोनों कथन स्वतंत्र कारण हैं"], 0,
  "Crop damage in the growing areas cuts supply, and a few weeks later scarcer onions sell at higher prices in the cities: II comes first and explains I. "
  "Reading it the other way, rising city prices cannot have damaged the crop; and nothing points to a third cause behind both, since the rain is the cause of the damage itself.",
  "उत्पादक क्षेत्रों में फ़सल की क्षति आपूर्ति घटाती है, और कुछ सप्ताह बाद कम प्याज़ शहरों में ऊँचे दाम पर बिकता है: II पहले आता है और I की व्याख्या करता है। "
  "उलटा पढ़ें तो शहरों के बढ़ते दाम फ़सल को क्षति नहीं पहुँचा सकते; और दोनों के पीछे किसी तीसरे कारण का कोई संकेत नहीं, क्योंकि वर्षा स्वयं क्षति का कारण है।",
  "lr-sc-onion-price-cause-effect")

# 8 -- floors of a building
def _sa2():
    sols = []
    for fl in permutations(range(1, 6)):
        f = dict(zip("ABCDE", fl))
        if not (f["C"] < f["A"] < f["E"]) or f["B"] % 2 or f["D"] != f["B"] + 1 or f["E"] == 5:
            continue
        sols.append(f)
    assert len(sols) == 1, sols
    f = sols[0]
    return next(p for p, v in f.items() if v == f["A"] + 1)
T(LR, "Seating Arrangement", "hard",
  "Five friends A, B, C, D and E live on different floors of a five-storey building, the ground floor being the first. A lives above C but below E. B lives on an even-numbered floor, and D lives on the floor just above B. "
  "E does not live on the top floor. Who lives on the floor just above A?",
  "पाँच मित्र A, B, C, D और E एक पाँच मंज़िला इमारत की अलग-अलग मंज़िलों पर रहते हैं, भूतल पहली मंज़िल है। A, C से ऊपर पर E से नीचे रहता है। B एक सम संख्या वाली मंज़िल पर रहता है, और D, B के ठीक ऊपर वाली मंज़िल पर रहता है। "
  "E सबसे ऊपरी मंज़िल पर नहीं रहता। A के ठीक ऊपर वाली मंज़िल पर कौन रहता है?",
  ["E", "B", "D", "C"], ["E", "B", "D", "C"], 0,
  "B is on floor 2 or 4, with D just above. If B were on 2 and D on 3, then C, A and E would fill floors 1, 4 and 5 in rising order, putting E on the top floor, which is not allowed. "
  "So B is on 4 and D on 5, and C, A, E take floors 1, 2 and 3 in that order. E, on floor 3, is just above A. B and D are higher up; C is below A.",
  "B मंज़िल 2 या 4 पर है, और D उसके ठीक ऊपर। यदि B मंज़िल 2 और D मंज़िल 3 पर होते, तो C, A और E बढ़ते क्रम में मंज़िल 1, 4 और 5 भरते, जिससे E सबसे ऊपर होता, जिसकी अनुमति नहीं है। "
  "अतः B मंज़िल 4 पर और D मंज़िल 5 पर है, और C, A, E इसी क्रम में मंज़िल 1, 2 और 3 पर हैं। मंज़िल 3 पर E, A के ठीक ऊपर है। B और D और ऊपर हैं; C, A से नीचे है।",
  "lr-sa-five-floors", check=_sa2)

# 9 -- syllogism: both follow
def _sy1():
    regions = list(product((0, 1), repeat=4))        # (book, pen, pencil, eraser)
    one = two = True
    for mask in range(1, 1 << 16):
        full = [r for k, r in enumerate(regions) if mask >> k & 1]
        if not any(b and p for b, p, pc, e in full):           # some books are pens
            continue
        if any(p and not pc for b, p, pc, e in full):          # all pens are pencils
            continue
        if any(pc and e for b, p, pc, e in full):              # no pencil is an eraser
            continue
        one &= any(b and not e for b, p, pc, e in full)
        two &= any(pc and b for b, p, pc, e in full)
    return _two(one, two)
S2(LR, "Syllogism", "medium",
   "Statements: Some books are pens. All pens are pencils. No pencil is an eraser.\n\nWhich of the following conclusions follow(s) from the statements?",
   "कथन: कुछ किताबें पेन हैं। सभी पेन पेंसिल हैं। कोई भी पेंसिल रबड़ नहीं है।\n\nनिम्नलिखित में से कौन-सा/से निष्कर्ष कथनों से निकलता/निकलते है/हैं?",
   ["Some books are not erasers.", "Some pencils are books."],
   ["कुछ किताबें रबड़ नहीं हैं।", "कुछ पेंसिल किताबें हैं।"], 2,
   "Both follow. The books that are pens are pencils (all pens are pencils), so some pencils are books (II); and since no pencil is an eraser, those same books are not erasers (I). "
   "The trap is to reject I because some other books might be erasers -- they might, but I claims only that some books are not.",
   "दोनों निकलते हैं। जो किताबें पेन हैं वे पेंसिल हैं (सभी पेन पेंसिल हैं), इसलिए कुछ पेंसिल किताबें हैं (II); और चूँकि कोई पेंसिल रबड़ नहीं है, वही किताबें रबड़ नहीं हैं (I)। "
   "जाल यह है कि I को इस आधार पर नकारा जाए कि कुछ दूसरी किताबें रबड़ हो सकती हैं -- हो सकती हैं, पर I केवल इतना कहता है कि कुछ किताबें रबड़ नहीं हैं।",
   "lr-sy-books-pens-pencils", roman=True, check=_sy1)

# 10 -- cube with opposite faces alike
def _cp1():
    n = 3
    colours = lambda x, y, z: ({"red"} if x in (0, n - 1) else set()) | ({"blue"} if y in (0, n - 1) else set()) | ({"green"} if z in (0, n - 1) else set())
    return str(sum(1 for x in range(n) for y in range(n) for z in range(n) if colours(x, y, z) == {"red", "blue"}))
N(LR, "Cube Painting", "hard",
  "A cube is painted red on two opposite faces, blue on two other opposite faces and green on the remaining two. It is then cut into 27 equal smaller cubes. How many of the small cubes have red and blue paint but no green?",
  "एक घन के दो आमने-सामने के फलक लाल, दो अन्य आमने-सामने के फलक नीले और शेष दो हरे रंगे जाते हैं। फिर उसे 27 बराबर छोटे घनों में काटा जाता है। कितने छोटे घनों पर लाल और नीला रंग है, पर हरा नहीं?",
  ["4", "8", "12", "16"], 0,
  "A small cube with exactly two painted faces sits in the middle of an edge, and the two faces meeting at an edge are always different colours, since alike faces are opposite. "
  "The cube's 12 edges divide equally among the three colour pairs, 4 red-blue, 4 red-green and 4 blue-green, and each edge has one middle cube, so 4 cubes show red and blue only. "
  "12 counts every two-coloured cube; 8 counts the corners, which carry all three colours.",
  "ठीक दो रंगे फलकों वाला छोटा घन किसी किनारे के बीच में होता है, और किसी किनारे पर मिलने वाले दोनों फलक सदा अलग रंग के होते हैं, क्योंकि एक जैसे फलक आमने-सामने हैं। "
  "घन के 12 किनारे तीन रंग-जोड़ियों में बराबर बँटते हैं, 4 लाल-नीले, 4 लाल-हरे और 4 नीले-हरे, और हर किनारे पर बीच का एक घन है, इसलिए केवल लाल और नीले वाले 4 घन हैं। "
  "12 हर दो रंगों वाले घन को गिनता है; 8 कोनों को गिनता है, जिन पर तीनों रंग हैं।",
  "lr-cp-opposite-faces-same-colour", _cp1)

# 11 -- distance and direction
def _dd2():
    a, cc = (0, 15), (8, 0)
    dx, dy = a[0] - cc[0], a[1] - cc[1]
    d = (dx * dx + dy * dy) ** 0.5
    return f"{d:g} km to the north-west" if dx < 0 < dy else "?"
T(LR, "Direction & Distance", "medium",
  "Village A is 15 km to the north of village B, and village C is 8 km to the east of B. How far is A from C, and in which direction?",
  "गाँव A, गाँव B से 15 किमी उत्तर में है, और गाँव C, B से 8 किमी पूर्व में है। A, C से कितनी दूर और किस दिशा में है?",
  ["17 km to the north-west", "17 km to the north-east", "23 km to the north-west", "7 km to the north"],
  ["उत्तर-पश्चिम में 17 किमी", "उत्तर-पूर्व में 17 किमी", "उत्तर-पश्चिम में 23 किमी", "उत्तर में 7 किमी"], 0,
  "B, A and C form a right angle at B, so AC = √(15² + 8²) = √289 = 17 km. From C, A lies to the north (15 km up) and to the west (8 km back), so it is to the north-west. "
  "North-east reverses the east-west part of the answer; 23 km adds the two legs instead of using the right triangle; 7 km subtracts them.",
  "B, A और C, B पर समकोण बनाते हैं, इसलिए AC = √(15² + 8²) = √289 = 17 किमी। C से देखने पर A उत्तर में (15 किमी ऊपर) और पश्चिम में (8 किमी पीछे) है, इसलिए उत्तर-पश्चिम में है। "
  "उत्तर-पूर्व, पूर्व-पश्चिम वाले भाग को उलट देता है; 23 किमी दोनों भुजाएँ जोड़ता है; 7 किमी उन्हें घटाता है।",
  "lr-dd-pythagoras-north-west", check=_dd2)

# 12 -- family puzzle with unknown gender
T(LR, "Blood Relation", "hard",
  "In a family of six -- A, B, C, D, E and F -- there are two married couples. D is the grandmother of A and the mother of B. C is the wife of B and the mother of F. F is the granddaughter of E. How is A related to F?",
  "छह सदस्यों -- A, B, C, D, E और F -- वाले एक परिवार में दो विवाहित दंपती हैं। D, A की दादी और B की माँ है। C, B की पत्नी और F की माँ है। F, E की पोती है। A का F से क्या संबंध है?",
  ["Brother or sister", "Brother only", "Sister only", "Cousin on the father's side"],
  ["भाई या बहन", "केवल भाई", "केवल बहन", "चचेरा भाई या बहन"], 0,
  "B is D's son and is married to C; their child F is the granddaughter of E, so E is D's husband -- the two couples are D-E and B-C. A is D's grandchild, and D's only child named is B, so A is also a child of B and C. "
  "A and F are therefore siblings. A's gender is never stated, so A may be F's brother or sister -- the trap is to assume one. A is not a cousin, because A and F share both parents.",
  "B, D का बेटा है और उसका विवाह C से हुआ है; उनकी संतान F, E की पोती है, इसलिए E, D का पति है -- दोनों दंपती D-E और B-C हैं। A, D का पोता या पोती है, और D की बताई गई एकमात्र संतान B है, इसलिए A भी B और C की संतान है। "
  "अतः A और F भाई-बहन हैं। A का लिंग कहीं नहीं बताया गया, इसलिए A, F का भाई या बहन हो सकता है -- जाल यह है कि कोई एक मान लिया जाए। A चचेरा नहीं है, क्योंकि A और F के माता-पिता एक ही हैं।",
  "lr-br-family-gender-unknown")

# 13 -- word code across sentences
def _cd2():
    msgs = {("sweet", "ripe", "mango"): {"pit", "nak", "sod"}, ("ripe", "red", "apple"): {"nak", "lot", "dum"}, ("mango", "and", "apple"): {"sod", "mor", "lot"}}
    words = sorted({w for m in msgs for w in m})
    codes = sorted({x for v in msgs.values() for x in v})
    sols = []
    for perm in permutations(codes, len(words)):
        code = dict(zip(words, perm))
        if all({code[w] for w in m} == v for m, v in msgs.items()):
            sols.append(code["red"])
    assert len(set(sols)) == 1, sols
    return sols[0]
T(LR, "Coding-Decoding", "medium",
  "In a certain code language, 'pit nak sod' means 'sweet ripe mango', 'nak lot dum' means 'ripe red apple', and 'sod mor lot' means 'mango and apple'. Which word means 'red'?",
  "एक निश्चित कूट भाषा में 'pit nak sod' का अर्थ 'sweet ripe mango', 'nak lot dum' का अर्थ 'ripe red apple', और 'sod mor lot' का अर्थ 'mango and apple' है। 'red' का अर्थ कौन-सा शब्द है?",
  ["dum", "nak", "lot", "pit"], ["dum", "nak", "lot", "pit"], 0,
  "Words common to two sentences share a code: 'ripe' is in the first two, so ripe = nak; 'mango' is in the first and third, so mango = sod; 'apple' is in the second and third, so apple = lot. "
  "In 'ripe red apple' = 'nak lot dum', the code left for 'red' is dum. nak is 'ripe' and lot is 'apple'; pit is 'sweet'.",
  "दो वाक्यों में साझा शब्दों का कूट साझा होता है: 'ripe' पहले दो में है, इसलिए ripe = nak; 'mango' पहले और तीसरे में है, इसलिए mango = sod; 'apple' दूसरे और तीसरे में है, इसलिए apple = lot। "
  "'ripe red apple' = 'nak lot dum' में 'red' के लिए बचा कूट dum है। nak 'ripe' है और lot 'apple'; pit 'sweet' है।",
  "lr-cd-word-code-red", check=_cd2)

# 14 -- easy conclusion: II only
def _sc3():
    one = two = True
    for priya, other in product(product((0, 1), repeat=2), repeat=2):    # (late, allowed in)
        if any(late and allowed for late, allowed in (priya, other)) or not priya[1]:
            continue                                          # premise: late -> not allowed; Priya allowed in
        one &= all(allowed for late, allowed in (priya, other) if not late)
        two &= not priya[0]
    return _two(one, two)
S2(LR, "Statement-Conclusion/Assumption", "easy",
   "Statement: No one who arrived late was allowed into the examination hall. Priya was allowed into the hall.\n\n" + CONC,
   "कथन: देर से पहुँचने वाले किसी भी व्यक्ति को परीक्षा भवन में प्रवेश नहीं दिया गया। प्रिया को भवन में प्रवेश दिया गया।\n\n" + CONC_HI,
   ["Everyone who arrived on time was allowed into the hall.", "Priya did not arrive late."],
   ["समय पर पहुँचने वाले हर व्यक्ति को भवन में प्रवेश दिया गया।", "प्रिया देर से नहीं पहुँची।"], 1,
   "Only II follows: had Priya arrived late she would have been kept out, and she was let in, so she was not late. "
   "I does not follow: the statement says who was kept out, not that everyone else got in -- someone on time may have been refused for another reason, such as a missing admit card.",
   "केवल II निकलता है: यदि प्रिया देर से पहुँचती तो उसे रोका जाता, और उसे प्रवेश मिला, इसलिए वह देर से नहीं पहुँची। "
   "I नहीं निकलता: कथन बताता है कि किसे रोका गया, यह नहीं कि बाक़ी सबको प्रवेश मिला -- समय पर पहुँचे किसी व्यक्ति को किसी और कारण से, जैसे प्रवेश-पत्र न होने पर, रोका गया हो सकता है।",
   "lr-sc-late-entry-contrapositive", roman=True, check=_sc3)

# 15 -- truth-tellers and liars
def _tl1():
    sols = []
    for a, b, cc in product((True, False), repeat=3):
        says = {"A": not b, "B": not cc, "C": (not a) and (not b)}
        if says["A"] == a and says["B"] == b and says["C"] == cc:
            sols.append((a, b, cc))
    assert len(sols) == 1, sols
    names = tuple(n for n, t in zip("ABC", sols[0]) if t)
    return {("A",): "A only", ("B",): "B only", ("C",): "C only", ("A", "C"): "A and C"}[names]
T(LR, "Truth-Liar", "hard",
  "Each of A, B and C either always tells the truth or always lies. A says, 'B is a liar.' B says, 'C is a liar.' C says, 'A and B are both liars.' Who tells the truth?",
  "A, B और C में से हर एक या तो सदा सच बोलता है या सदा झूठ। A कहता है, 'B झूठा है।' B कहता है, 'C झूठा है।' C कहता है, 'A और B दोनों झूठे हैं।' कौन सच बोलता है?",
  ["B only", "A only", "C only", "A and C"], ["केवल B", "केवल A", "केवल C", "A और C"], 0,
  "Suppose A tells the truth. Then B lies, so B's 'C is a liar' is false and C tells the truth -- but C's 'A and B are both liars' would then be false, since A is truthful. Contradiction, so A lies. "
  "Then 'B is a liar' is false, so B tells the truth, and C is a liar as B says. Check C: 'A and B are both liars' is false because B is truthful, as a liar's statement must be. Only B tells the truth.",
  "मान लीजिए A सच बोलता है। तब B झूठ बोलता है, इसलिए B का 'C झूठा है' असत्य है और C सच बोलता है -- पर तब C का 'A और B दोनों झूठे हैं' असत्य होगा, क्योंकि A सच्चा है। विरोधाभास, अतः A झूठ बोलता है। "
  "तब 'B झूठा है' असत्य है, इसलिए B सच बोलता है, और B के कहे अनुसार C झूठा है। C की जाँच: 'A और B दोनों झूठे हैं' असत्य है क्योंकि B सच्चा है, जैसा झूठे का कथन होना चाहिए। केवल B सच बोलता है।",
  "lr-tl-chain-of-accusations", check=_tl1)

# ---- the data-sufficiency block's three Reasoning items
DS(LR, "medium",
   "How many brothers does Kiran have?",
   "किरण के कितने भाई हैं?",
   "Kiran's father has three children.", "किरण के पिता की तीन संतानें हैं।",
   "Kiran's mother has two daughters.", "किरण की माँ की दो बेटियाँ हैं।",
   3,
   "Statement I gives three children but not their sexes. Statement II gives two daughters. Together (assuming the same parents) there are three children, two of them daughters and one a son -- "
   "but the name Kiran is used for both girls and boys. If Kiran is the son, Kiran has no brother; if Kiran is a daughter, Kiran has one brother. So even both statements do not settle it.",
   "कथन I तीन संतानें बताता है पर उनका लिंग नहीं। कथन II दो बेटियाँ बताता है। दोनों साथ (एक ही माता-पिता मानकर) तीन संतानें हैं, जिनमें दो बेटियाँ और एक बेटा है -- "
   "पर किरण नाम लड़कियों और लड़कों दोनों का होता है। यदि किरण बेटा है, तो उसका कोई भाई नहीं; यदि किरण बेटी है, तो उसका एक भाई है। अतः दोनों कथन भी उत्तर तय नहीं करते।",
   "lr-ds-kiran-brothers")

DS(LR, "medium",
   "Is Mohan older than Sohan?",
   "क्या मोहन, सोहन से बड़ा है?",
   "Mohan is younger than Rohan, and Rohan is younger than Sohan.", "मोहन, रोहन से छोटा है, और रोहन, सोहन से छोटा है।",
   "Sohan was born in 2004.", "सोहन का जन्म 2004 में हुआ था।",
   0,
   "Statement I orders the three: Mohan is younger than Rohan, who is younger than Sohan, so Mohan is younger than Sohan and the answer is 'no' -- a definite answer, which is all that sufficiency needs. "
   "Statement II gives Sohan's year of birth but says nothing about Mohan. So I alone answers the question and II alone does not.",
   "कथन I तीनों का क्रम बताता है: मोहन, रोहन से छोटा है, जो सोहन से छोटा है, इसलिए मोहन, सोहन से छोटा है और उत्तर 'नहीं' है -- एक निश्चित उत्तर, जो पर्याप्तता के लिए काफ़ी है। "
   "कथन II सोहन के जन्म का वर्ष बताता है पर मोहन के बारे में कुछ नहीं कहता। अतः I अकेला प्रश्न का उत्तर देता है और II अकेला नहीं।",
   "lr-ds-mohan-sohan-older")

DS(LR, "medium",
   "What is Ravi's rank from the top in his class?",
   "अपनी कक्षा में ऊपर से रवि का स्थान क्या है?",
   "Ravi is 10th from the bottom in a class of 40 students.", "40 विद्यार्थियों की कक्षा में रवि नीचे से 10वें स्थान पर है।",
   "Exactly 30 students rank above Ravi.", "ठीक 30 विद्यार्थी रवि से ऊपर हैं।",
   1,
   "Statement I: rank from the top = 40 - 10 + 1 = 31. Statement II: with 30 students above him, Ravi is 31st. Each statement alone fixes the rank, so the question can be answered by either alone. "
   "The trap is to think that II needs the class size from I.",
   "कथन I: ऊपर से स्थान = 40 - 10 + 1 = 31। कथन II: उससे ऊपर 30 विद्यार्थी होने पर रवि 31वाँ है। हर कथन अकेला स्थान तय करता है, इसलिए प्रश्न का उत्तर किसी भी एक कथन से अकेले दिया जा सकता है। "
   "जाल यह सोचना है कि II को I से कक्षा का आकार चाहिए।",
   "lr-ds-ravi-rank-from-top")
