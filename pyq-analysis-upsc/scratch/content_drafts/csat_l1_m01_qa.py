# -*- coding: utf-8 -*-
"""CSAT Level 1 · Mini 1 -- Quantitative Aptitude (17 items: 16 in the Quant slots, 1 in the data-sufficiency block).

The half paper's share of Level 2's Quant mix (number theory 4, speed 2, percentage 2, ratio and averages 2, work 1,
counting 1, geometry 1, series 1, puzzles 2, data sufficiency 1), at the foundation level: difficulty 5 easy /
9 medium / 3 hard. None of Level 2's 238 Quant shapes is reused: three bells that ring together, ropes cut into the
longest equal pieces, the remainder of a square, the largest of four close fractions; laps of a track turned into km/h,
an echo from a cliff; 20 per cent of one number equal to 30 per cent of another, pens sold
at a loss and then at a gain for the same ₹100; two sections' combined average, two gear wheels in mesh;
one worker's time from a pair's; arrangements of EQUAL that begin and end with a vowel; the sides of a regular polygon
from its angle; a cube-plus-one series; the digits used to number a book's pages, the angle between the hands at 3:40;
and a salary that either statement settles. The rows are written in the order they take on the paper, and every key is
worked out in code by check()."""
import math
from fractions import Fraction as F
from itertools import permutations
from csat_common import N, DS, QA

def _ds(s1, s2, both):
    alone = (len(set(s1)) == 1, len(set(s2)) == 1)
    return "b" if all(alone) else "a" if any(alone) else "c" if len(set(both)) == 1 else "d"

# 1 -- three bells ring together again
def _bells():
    gap = math.lcm(15, 20, 25)
    assert gap == 300 and all(m % 15 == 0 and m % 20 == 0 and m % 25 for m in (120, 180, 240))   # the distractors fit two bells, not the third
    h = 9 + gap // 60
    return f"{h - 12}:00 p.m."
N(QA, "Number Theory", "easy",
  "Three bells ring at intervals of 15 minutes, 20 minutes and 25 minutes. If they ring together at 9:00 a.m., at what time will they next ring together?",
  "तीन घंटियाँ क्रमशः 15 मिनट, 20 मिनट और 25 मिनट के अंतराल पर बजती हैं। यदि वे पूर्वाह्न 9:00 बजे एक साथ बजती हैं, तो वे अगली बार एक साथ कितने बजे बजेंगी?",
  ["11:00 a.m.", "12:00 noon", "1:00 p.m.", "2:00 p.m."], 3,
  "The bells ring together again after the least common multiple of 15, 20 and 25 minutes. 15 = 3 × 5, 20 = 2² × 5 and 25 = 5², so the LCM is 2² × 3 × 5² = 300 minutes, or 5 hours: 9:00 a.m. + 5 hours = 2:00 p.m. "
  "11:00 a.m., 12:00 noon and 1:00 p.m. are 120, 180 and 240 minutes after 9:00 a.m.: multiples of 15 and of 20, so the first two bells do ring together then, but not multiples of 25, so the third bell does not.",
  "घंटियाँ 15, 20 और 25 मिनट के लघुत्तम समापवर्त्य (LCM) के बाद फिर एक साथ बजती हैं। 15 = 3 × 5, 20 = 2² × 5 और 25 = 5², अतः LCM = 2² × 3 × 5² = 300 मिनट, यानी 5 घंटे: पूर्वाह्न 9:00 + 5 घंटे = अपराह्न 2:00 बजे। "
  "पूर्वाह्न 11:00, दोपहर 12:00 और अपराह्न 1:00 बजे, पूर्वाह्न 9:00 के क्रमशः 120, 180 और 240 मिनट बाद हैं: ये 15 और 20 के गुणज हैं, इसलिए पहली दो घंटियाँ तब साथ बजती हैं, पर 25 के गुणज नहीं, इसलिए तीसरी घंटी नहीं बजती।",
  "qa-nt-three-bells-ring-together", _bells,
  opts_hi=["पूर्वाह्न 11:00 बजे", "दोपहर 12:00 बजे", "अपराह्न 1:00 बजे", "अपराह्न 2:00 बजे"])

# 2 -- a cube-plus-one series
def _cubes():
    s = [2, 9, 28, 65, 126]
    assert s == [n ** 3 + 1 for n in range(1, 6)]
    return str(6 ** 3 + 1)
N(QA, "Sequences & Series", "medium",
  "What is the next term of the series 2, 9, 28, 65, 126, ... ?",
  "श्रेणी 2, 9, 28, 65, 126, ... का अगला पद क्या है?",
  ["215", "216", "217", "343"], 2,
  "Each term is one more than a cube: 1³ + 1, 2³ + 1, 3³ + 1, 4³ + 1, 5³ + 1. The next term is 6³ + 1 = 217. (The differences 7, 19, 37, 61 grow by 12, 18, 24, so the next difference is 61 + 30 = 91, and 126 + 91 = 217.) "
  "215 is 6³ - 1 and 216 is 6³ itself, each missing the + 1 that every term carries; 343 is 7³, which skips a cube.",
  "हर पद किसी घन से एक अधिक है: 1³ + 1, 2³ + 1, 3³ + 1, 4³ + 1, 5³ + 1। अगला पद 6³ + 1 = 217 है। (अंतर 7, 19, 37, 61 क्रमशः 12, 18, 24 से बढ़ते हैं, अतः अगला अंतर 61 + 30 = 91 है, और 126 + 91 = 217।) "
  "215, 6³ - 1 है और 216 स्वयं 6³ है, दोनों में वह + 1 छूट जाता है जो हर पद में है; 343, 7³ है, जो एक घन छोड़ देता है।",
  "qa-ss-one-more-than-the-cubes", _cubes)

# 4 -- the angle between the hands at 3:40
def _clock():
    minute = 40 * 6                      # 6° a minute
    hour = 3 * 30 + 40 * F(1, 2)         # 30° an hour, plus 0.5° a minute
    a = abs(minute - hour)
    a = min(a, 360 - a)
    assert hour == 110 and abs(minute - 90) == 150
    return f"{a}°"
N(QA, "Puzzle Hybrid", "medium",
  "What is the smaller angle between the hour hand and the minute hand of a clock at 3:40?",
  "3:40 बजे घड़ी की घंटे की सुई और मिनट की सुई के बीच छोटा कोण कितना है?",
  ["110°", "130°", "150°", "230°"], 1,
  "The minute hand moves 6° a minute, so at 40 minutes it is at 240° from 12. The hour hand moves 30° an hour and 0.5° a minute, so at 3:40 it is at 90° + 20° = 110°. The angle between them is 240° - 110° = 130°. "
  "150° leaves the hour hand on the 3, forgetting that it moves on through the hour; 230° is the larger angle (360° - 130°); 110° is the position of the hour hand, not the angle between the hands.",
  "मिनट की सुई प्रति मिनट 6° चलती है, अतः 40 मिनट पर वह 12 से 240° पर है। घंटे की सुई प्रति घंटा 30° और प्रति मिनट 0.5° चलती है, अतः 3:40 पर वह 90° + 20° = 110° पर है। दोनों के बीच का कोण 240° - 110° = 130° है। "
  "150° घंटे की सुई को 3 पर ही मान लेता है, यह भूलकर कि वह घंटे भर आगे बढ़ती रहती है; 230° बड़ा कोण है (360° - 130°); 110° घंटे की सुई की स्थिति है, सुइयों के बीच का कोण नहीं।",
  "qa-ph-the-angle-between-the-hands-at-3-40", _clock)

# 8 -- pens sold at a loss, then at a gain, for the same ₹100
def _pens():
    cost = F(100) / F(80, 100) / 12          # selling 12 for ₹100 is 80% of their cost
    price = cost * F(120, 100)
    gain = {n: F(100, n) / cost - 1 for n in (8, 9, 10, 12)}
    assert gain[8] == F(1, 5) and gain[9] == F(1, 15) and gain[10] == F(-1, 25) and gain[12] == F(-1, 5)
    return str(F(100) / price)
N(QA, "Percentage & Profit-Loss", "hard",
  "By selling 12 pens for ₹100, a shopkeeper loses 20 per cent. How many pens must be sold for ₹100 to gain 20 per cent?",
  "₹100 में 12 पेन बेचने पर एक दुकानदार को 20 प्रतिशत की हानि होती है। 20 प्रतिशत लाभ कमाने के लिए ₹100 में कितने पेन बेचने होंगे?",
  ["8", "9", "10", "12"], 0,
  "At a 20 per cent loss the ₹100 is 80 per cent of the cost, so 12 pens cost 100 ÷ 0.8 = ₹125, or ₹125/12 each. A 20 per cent gain needs a price of 1.2 × 125/12 = ₹12.50 a pen, and ₹100 buys 100 ÷ 12.5 = 8 pens at that price. "
  "Check the others against the cost of ₹125/12 a pen: 9 pens for ₹100 is ₹11.11 a pen, a gain of only 6⅔ per cent; 10 pens is ₹10 a pen, still a loss of 4 per cent; and 12 pens is the 20 per cent loss the question starts from.",
  "20 प्रतिशत हानि पर ₹100 लागत का 80 प्रतिशत है, अतः 12 पेन की लागत 100 ÷ 0.8 = ₹125, यानी प्रति पेन ₹125/12 है। 20 प्रतिशत लाभ के लिए प्रति पेन 1.2 × 125/12 = ₹12.50 का मूल्य चाहिए, और इस मूल्य पर ₹100 में 100 ÷ 12.5 = 8 पेन आते हैं। "
  "बाक़ी को प्रति पेन ₹125/12 की लागत से जाँचिए: ₹100 में 9 पेन यानी प्रति पेन ₹11.11, केवल 6⅔ प्रतिशत लाभ; 10 पेन यानी प्रति पेन ₹10, अब भी 4 प्रतिशत हानि; और 12 पेन वही 20 प्रतिशत हानि है जिससे प्रश्न शुरू होता है।",
  "qa-pp-pens-sold-for-a-hundred-rupees", _pens)

# 10 -- ropes cut into the longest equal pieces
def _ropes():
    ls = (84, 126, 210)
    g = math.gcd(*ls)
    assert g == 42 and all(x % 21 == 0 and x % 14 == 0 for x in ls) and sum(ls) // 21 == 20 and sum(ls) // 14 == 30
    return str(sum(x // g for x in ls))
N(QA, "Number Theory", "medium",
  "Three ropes, 84 m, 126 m and 210 m long, are to be cut into pieces that are all of the same length, with nothing left over. If each piece is to be as long as possible, how many pieces will there be in all?",
  "84 मी, 126 मी और 210 मी लंबी तीन रस्सियों को ऐसे टुकड़ों में काटना है जो सभी एक ही लंबाई के हों और कुछ भी न बचे। यदि हर टुकड़ा यथासंभव लंबा हो, तो कुल कितने टुकड़े होंगे?",
  ["10", "20", "30", "42"], 0,
  "The longest piece that divides all three lengths exactly is their HCF: 84 = 2² × 3 × 7, 126 = 2 × 3² × 7 and 210 = 2 × 3 × 5 × 7, so the HCF is 2 × 3 × 7 = 42 m. The ropes give 84/42 + 126/42 + 210/42 = 2 + 3 + 5 = 10 pieces. "
  "20 and 30 are the counts for pieces of 21 m and 14 m, which also divide all three lengths but are not the longest possible; 42 is the length of a piece, not the number of pieces.",
  "तीनों लंबाइयों को पूरा-पूरा बाँटने वाला सबसे लंबा टुकड़ा उनका महत्तम समापवर्तक (HCF) है: 84 = 2² × 3 × 7, 126 = 2 × 3² × 7 और 210 = 2 × 3 × 5 × 7, अतः HCF = 2 × 3 × 7 = 42 मी। रस्सियों से 84/42 + 126/42 + 210/42 = 2 + 3 + 5 = 10 टुकड़े बनते हैं। "
  "20 और 30, 21 मी और 14 मी के टुकड़ों की संख्याएँ हैं, जो तीनों लंबाइयों को बाँटते तो हैं पर सबसे लंबे नहीं; 42 एक टुकड़े की लंबाई है, टुकड़ों की संख्या नहीं।",
  "qa-nt-ropes-cut-into-the-longest-equal-pieces", _ropes)

# 11 -- two sections' combined average
def _avg():
    total = 30 * 60 + 20 * 70
    assert F(60 + 70, 2) == 65 and F(30 * 70 + 20 * 60, 50) == 66
    return str(F(total, 50))
N(QA, "Ratio, Mixtures & Alligation", "easy",
  "Section A of a class has 30 students, whose average mark in a test is 60; section B has 20 students, whose average mark is 70. What is the average mark of all 50 students?",
  "एक कक्षा के अनुभाग A में 30 विद्यार्थी हैं, जिनके एक परीक्षा में औसत अंक 60 हैं; अनुभाग B में 20 विद्यार्थी हैं, जिनके औसत अंक 70 हैं। सभी 50 विद्यार्थियों के औसत अंक क्या हैं?",
  ["64", "65", "66", "70"], 0,
  "The marks add up to 30 × 60 + 20 × 70 = 1,800 + 1,400 = 3,200, so the average of all 50 students is 3,200 ÷ 50 = 64. It lies nearer to 60 because section A is the larger. "
  "65 is the plain average of 60 and 70, which ignores the sizes of the sections; 66 weights them the wrong way round (30 × 70 + 20 × 60, divided by 50); 70 is section B's own average.",
  "अंकों का योग 30 × 60 + 20 × 70 = 1,800 + 1,400 = 3,200 है, अतः सभी 50 विद्यार्थियों का औसत 3,200 ÷ 50 = 64 है। यह 60 के अधिक निकट है क्योंकि अनुभाग A बड़ा है। "
  "65, 60 और 70 का सीधा औसत है, जो अनुभागों के आकार की अनदेखी करता है; 66 उन्हें उलटा भार देता है (30 × 70 + 20 × 60, भाग 50); 70 केवल अनुभाग B का औसत है।",
  "qa-rm-two-sections-combined-average", _avg)

# 16 -- one worker's time from a pair's
def _work():
    b = 1 / (F(1, 12) - F(1, 20))
    return str(b)
N(QA, "Time & Work", "medium",
  "A and B together can finish a job in 12 days, and A alone can finish it in 20 days. In how many days can B alone finish it?",
  "A और B मिलकर एक काम 12 दिनों में पूरा कर सकते हैं, और A अकेला उसे 20 दिनों में पूरा कर सकता है। B अकेला उसे कितने दिनों में पूरा कर सकता है?",
  ["8", "16", "30", "32"], 2,
  "Together they do 1/12 of the job a day and A does 1/20, so B does 1/12 - 1/20 = (5 - 3)/60 = 1/30 of it a day: B alone takes 30 days. "
  "8 subtracts the days (20 - 12) and 32 adds them, but days cannot be added or subtracted like rates; 16 is the average of 12 and 20.",
  "दोनों मिलकर प्रतिदिन काम का 1/12 करते हैं और A अकेला 1/20, अतः B प्रतिदिन 1/12 - 1/20 = (5 - 3)/60 = 1/30 करता है: B अकेले 30 दिन लेता है। "
  "8 दिनों को घटाता है (20 - 12) और 32 उन्हें जोड़ता है, पर दिनों को दरों की तरह जोड़ा-घटाया नहीं जा सकता; 16, 12 और 20 का औसत है।",
  "qa-tw-one-worker-s-time-from-the-pair-s", _work)

# 17 -- the sides of a regular polygon from its interior angle
def _poly():
    n = [k for k in range(3, 50) if F(180 * (k - 2), k) == 140]
    assert n == [9]
    return str(n[0])
N(QA, "Geometry & Mensuration", "easy",
  "Each interior angle of a regular polygon is 140°. How many sides does the polygon have?",
  "एक सम बहुभुज का प्रत्येक अंतः कोण 140° है। बहुभुज की कितनी भुजाएँ हैं?",
  ["6", "7", "8", "9"], 3,
  "Each exterior angle is 180° - 140° = 40°, and the exterior angles of any polygon add up to 360°, so the polygon has 360 ÷ 40 = 9 sides (check: (9 - 2) × 180° ÷ 9 = 140°). "
  "A regular polygon of 6 sides has interior angles of 120°, one of 7 sides about 128.6° and one of 8 sides 135°.",
  "प्रत्येक बाह्य कोण 180° - 140° = 40° है, और किसी भी बहुभुज के बाह्य कोणों का योग 360° होता है, अतः बहुभुज की 360 ÷ 40 = 9 भुजाएँ हैं (जाँच: (9 - 2) × 180° ÷ 9 = 140°)। "
  "6 भुजाओं वाले सम बहुभुज का अंतः कोण 120°, 7 भुजाओं वाले का लगभग 128.6° और 8 भुजाओं वाले का 135° होता है।",
  "qa-gm-sides-of-a-regular-polygon-from-its-angle", _poly)

# 21 -- the largest of four close fractions
def _frac():
    fs = {"5/7": F(5, 7), "7/10": F(7, 10), "11/15": F(11, 15), "13/18": F(13, 18)}
    assert sorted(fs, key=fs.get) == ["7/10", "5/7", "13/18", "11/15"]
    return max(fs, key=fs.get)
N(QA, "Number Theory", "medium",
  "Which one of the following fractions is the largest?",
  "निम्नलिखित भिन्नों में से कौन-सी सबसे बड़ी है?",
  ["7/10", "5/7", "13/18", "11/15"], 3,
  "Each fraction falls short of 1 by a small part: 5/7 by 2/7, 7/10 by 3/10, 11/15 by 4/15 and 13/18 by 5/18. The largest fraction is the one with the smallest shortfall. Over the common denominator 630: "
  "2/7 = 180/630, 3/10 = 189/630, 4/15 = 168/630 and 5/18 = 175/630, so 11/15 falls short by the least and is the largest (about 0.733, against 13/18 ≈ 0.722, 5/7 ≈ 0.714 and 7/10 = 0.7).",
  "हर भिन्न 1 से एक छोटे भाग से कम है: 5/7, 2/7 से; 7/10, 3/10 से; 11/15, 4/15 से और 13/18, 5/18 से। सबसे बड़ी भिन्न वह है जिसकी कमी सबसे छोटी है। सार्व हर 630 पर: "
  "2/7 = 180/630, 3/10 = 189/630, 4/15 = 168/630 और 5/18 = 175/630, अतः 11/15 की कमी सबसे कम है और वही सबसे बड़ी है (लगभग 0.733, जबकि 13/18 ≈ 0.722, 5/7 ≈ 0.714 और 7/10 = 0.7)।",
  "qa-nt-the-largest-of-four-close-fractions", _frac)

# 22 -- arrangements of EQUAL that begin and end with a vowel
def _equal():
    vowels = set("EUA")
    good = {p for p in permutations("EQUAL") if p[0] in vowels and p[-1] in vowels}
    assert 3 * 6 == 18 and 3 * 3 * 6 == 54
    return str(len(good))
N(QA, "Permutation & Combination", "hard",
  "In how many ways can the letters of the word EQUAL be arranged so that the arrangement begins with a vowel and also ends with a vowel?",
  "शब्द EQUAL के अक्षरों को कितने प्रकार से व्यवस्थित किया जा सकता है कि व्यवस्था स्वर से आरंभ हो और स्वर पर ही समाप्त भी हो?",
  ["18", "36", "54", "72"], 1,
  "EQUAL has three vowels (E, U, A) and two consonants (Q, L). The first place can take any of the 3 vowels and the last place either of the 2 vowels left: 3 × 2 = 6 ways. The three letters left -- one vowel and two consonants -- fill the middle in 3! = 6 ways. "
  "In all, 6 × 6 = 36. 18 counts only the 3 ways of choosing which two vowels go to the ends, forgetting that they can swap; 54 lets the same vowel stand at both ends (3 × 3 × 6), which is impossible since each letter is used once; 72 doubles the count.",
  "EQUAL में तीन स्वर (E, U, A) और दो व्यंजन (Q, L) हैं। पहले स्थान पर 3 में से कोई भी स्वर आ सकता है और अंतिम स्थान पर बचे 2 स्वरों में से कोई एक: 3 × 2 = 6 प्रकार। बचे तीन अक्षर -- एक स्वर और दो व्यंजन -- बीच के स्थान 3! = 6 प्रकार से भरते हैं। "
  "कुल 6 × 6 = 36। 18 केवल यह चुनने के 3 प्रकार गिनता है कि कौन-से दो स्वर सिरों पर जाएँ, यह भूलकर कि वे आपस में जगह बदल सकते हैं; 54 एक ही स्वर को दोनों सिरों पर आने देता है (3 × 3 × 6), जो असंभव है क्योंकि हर अक्षर एक बार ही आता है; 72 गिनती को दुगुना कर देता है।",
  "qa-pc-equal-begins-and-ends-with-a-vowel", _equal)

# 24 -- an echo from a cliff
def _echo():
    one_way = F(340) * F(3, 2) / 2
    assert one_way == 255 and F(340) * F(3, 2) == 510 and one_way / 2 == F(255, 2)
    return f"{one_way} m"
N(QA, "Speed-Distance-Time", "medium",
  "A person standing in front of a cliff shouts and hears the echo 1.5 seconds later. If sound travels at 340 metres a second, how far away is the cliff?",
  "एक चट्टान के सामने खड़ा एक व्यक्ति आवाज़ लगाता है और 1.5 सेकंड बाद उसकी प्रतिध्वनि सुनता है। यदि ध्वनि 340 मीटर प्रति सेकंड की चाल से चलती है, तो चट्टान कितनी दूर है?",
  ["127.5 m", "226.7 m", "255 m", "510 m"], 2,
  "In 1.5 seconds the sound goes to the cliff and comes back, travelling 340 × 1.5 = 510 m in all. The cliff is half of that away: 255 m. "
  "510 m is the whole journey there and back; 127.5 m halves it twice; 226.7 m divides 340 by 1.5 instead of multiplying.",
  "1.5 सेकंड में ध्वनि चट्टान तक जाती है और लौट आती है, यानी कुल 340 × 1.5 = 510 मी चलती है। चट्टान उसकी आधी दूरी पर है: 255 मी। "
  "510 मी आने-जाने की पूरी दूरी है; 127.5 मी उसे दो बार आधा करता है; 226.7 मी, 340 को 1.5 से गुणा करने के बजाय भाग देता है।",
  "qa-sdt-an-echo-from-a-cliff", _echo,
  opts_hi=["127.5 मी", "226.7 मी", "255 मी", "510 मी"])

# 30 -- two gear wheels in mesh
def _gears():
    teeth_a, turns_a, teeth_b = 24, 30, 40
    turns_b = F(teeth_a * turns_a, teeth_b)          # teeth passing the point of contact each minute are the same for both
    assert turns_b == 18 and F(turns_a * teeth_b, teeth_a) == 50 and turns_a + (teeth_b - teeth_a) == 46
    return str(turns_b)
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "Two gear wheels are in mesh. The smaller has 24 teeth and makes 30 turns a minute; the larger has 40 teeth. How many turns a minute does the larger wheel make?",
  "दो दाँतेदार पहिए (गियर) आपस में फँसे हुए हैं। छोटे पहिए में 24 दाँत हैं और वह प्रति मिनट 30 चक्कर लगाता है; बड़े पहिए में 40 दाँत हैं। बड़ा पहिया प्रति मिनट कितने चक्कर लगाता है?",
  ["18", "30", "46", "50"], 0,
  "Where the wheels touch, the teeth of one pass at the same rate as the teeth of the other: 24 × 30 = 720 teeth a minute. The larger wheel turns once for every 40 teeth, so it makes 720 ÷ 40 = 18 turns a minute -- turns vary inversely with the number of teeth. "
  "50 scales the turns up in the ratio 40 : 24 instead of down; 30 assumes both wheels turn equally often; 46 adds the 16 extra teeth to the 30 turns.",
  "जहाँ पहिए मिलते हैं, वहाँ एक के दाँत उसी दर से गुज़रते हैं जिस दर से दूसरे के: प्रति मिनट 24 × 30 = 720 दाँत। बड़ा पहिया हर 40 दाँतों पर एक चक्कर लगाता है, इसलिए वह प्रति मिनट 720 ÷ 40 = 18 चक्कर लगाता है -- चक्कर दाँतों की संख्या के व्युत्क्रमानुपाती होते हैं। "
  "50 चक्करों को 40 : 24 के अनुपात में घटाने के बजाय बढ़ा देता है; 30 मान लेता है कि दोनों पहिए बराबर चक्कर लगाते हैं; 46, 30 चक्करों में 16 अतिरिक्त दाँत जोड़ देता है।",
  "qa-rm-two-gear-wheels-in-mesh", _gears)

# 32 -- 20 per cent of A equals 30 per cent of B
def _pct():
    a = F(300)
    b = F(20, 100) * a / F(30, 100)
    assert b / a == F(2, 3) and a / b == F(3, 2)
    return "66⅔%"
N(QA, "Percentage & Profit-Loss", "easy",
  "If 20 per cent of A is equal to 30 per cent of B, then B is what per cent of A?",
  "यदि A का 20 प्रतिशत, B के 30 प्रतिशत के बराबर है, तो B, A का कितना प्रतिशत है?",
  ["10%", "50%", "66⅔%", "150%"], 2,
  "0.2A = 0.3B, so B = (0.2/0.3)A = (2/3)A, which is 66⅔% of A. 150% is the other way round: A is 150% of B. 10% is the difference between the two percentages, and 50% has no basis in the data.",
  "0.2A = 0.3B, अतः B = (0.2/0.3)A = (2/3)A, जो A का 66⅔% है। 150% उलटी दिशा का उत्तर है: A, B का 150% है। 10% दोनों प्रतिशतों का अंतर है, और 50% का आँकड़ों में कोई आधार नहीं।",
  "qa-pp-twenty-per-cent-of-one-is-thirty-of-another", _pct)

# 37 -- the digits used to number a book's pages
def _pages():
    used = lambda n: sum(len(str(k)) for k in range(1, n + 1))
    n = [k for k in range(1, 2000) if used(k) == 1002]
    assert n == [370] and 1002 // 3 == 334 and used(369) == 999 and used(371) == 1005
    return str(n[0])
N(QA, "Puzzle Hybrid", "hard",
  "The pages of a book are numbered 1, 2, 3, ... and so on to the last page. If 1,002 digits are used in all, how many pages does the book have?",
  "एक पुस्तक के पृष्ठ 1, 2, 3, ... से अंतिम पृष्ठ तक क्रमांकित हैं। यदि कुल 1,002 अंक प्रयोग हुए हैं, तो पुस्तक में कितने पृष्ठ हैं?",
  ["334", "369", "370", "371"], 2,
  "Pages 1-9 use 9 digits and pages 10-99 use 90 × 2 = 180, which makes 189. The remaining 1,002 - 189 = 813 digits number three-digit pages, 813 ÷ 3 = 271 of them, starting at 100: the last page is 99 + 271 = 370. "
  "334 divides 1,002 by 3 as if every page had three digits; 369 would use 999 digits and 371 would use 1,005.",
  "पृष्ठ 1-9 में 9 अंक लगते हैं और पृष्ठ 10-99 में 90 × 2 = 180, कुल 189। बचे 1,002 - 189 = 813 अंक तीन अंकों वाले पृष्ठों के हैं, यानी 813 ÷ 3 = 271 पृष्ठ, जो 100 से शुरू होते हैं: अंतिम पृष्ठ 99 + 271 = 370 है। "
  "334, 1,002 को 3 से ऐसे भाग देता है मानो हर पृष्ठ पर तीन अंक हों; 369 पृष्ठों में 999 अंक लगेंगे और 371 में 1,005।",
  "qa-ph-digits-used-to-number-a-book-s-pages", _pages)

# 38 -- the remainder of a square
def _square():
    rs = {n * n % 7 for n in range(3, 400, 7)}
    assert rs == {2}
    return str(rs.pop())
N(QA, "Number Theory", "medium",
  "When a natural number is divided by 7, the remainder is 3. What is the remainder when the square of the number is divided by 7?",
  "किसी प्राकृत संख्या को 7 से भाग देने पर शेषफल 3 आता है। उस संख्या के वर्ग को 7 से भाग देने पर शेषफल क्या होगा?",
  ["2", "3", "4", "6"], 0,
  "Write the number as 7k + 3. Its square is 49k² + 42k + 9 = 7(7k² + 6k + 1) + 2, so the remainder is 2 -- the remainder of 3² = 9 on division by 7. For example, 10 leaves 3 and 100 = 14 × 7 + 2 leaves 2. "
  "3 assumes that squaring keeps the remainder; 6 doubles it; 4 is the remainder for a number that leaves 2 (2² = 4).",
  "संख्या को 7k + 3 लिखिए। उसका वर्ग 49k² + 42k + 9 = 7(7k² + 6k + 1) + 2 है, अतः शेषफल 2 है -- यानी 3² = 9 को 7 से भाग देने का शेषफल। उदाहरण के लिए, 10 शेष 3 छोड़ता है और 100 = 14 × 7 + 2 शेष 2। "
  "3 मान लेता है कि वर्ग करने पर शेषफल वही रहता है; 6 उसे दुगुना करता है; 4 उस संख्या का शेषफल है जो शेष 2 छोड़ती है (2² = 4)।",
  "qa-nt-the-remainder-of-a-square", _square)

# 40 -- laps of a track turned into km/h
def _laps():
    ms = F(400, 80)
    assert ms == 5
    return str(ms * 3600 / 1000)
N(QA, "Speed-Distance-Time", "easy",
  "A runner completes each 400-metre lap of a track in 80 seconds. At this speed, how many kilometres would the runner cover in one hour?",
  "एक धावक ट्रैक का हर 400 मीटर का चक्कर 80 सेकंड में पूरा करता है। इस चाल से धावक एक घंटे में कितने किलोमीटर तय करेगा?",
  ["15", "18", "20", "24"], 1,
  "The speed is 400 ÷ 80 = 5 metres a second. An hour has 3,600 seconds, so the runner covers 5 × 3,600 = 18,000 metres, or 18 km (multiplying metres a second by 18/5 gives km/h). "
  "20 and 15 multiply 5 metres a second by 4 or by 3 in place of 3.6; 24 treats each lap as if it took a minute (400 m × 60 = 24 km).",
  "चाल 400 ÷ 80 = 5 मीटर प्रति सेकंड है। एक घंटे में 3,600 सेकंड होते हैं, अतः धावक 5 × 3,600 = 18,000 मीटर, यानी 18 किमी तय करता है (मीटर प्रति सेकंड को 18/5 से गुणा करने पर किमी प्रति घंटा मिलता है)। "
  "20 और 15, 5 मीटर प्रति सेकंड को 3.6 की जगह 4 या 3 से गुणा करते हैं; 24 हर चक्कर को ऐसे मानता है मानो वह एक मिनट में पूरा हुआ हो (400 मी × 60 = 24 किमी)।",
  "qa-sdt-laps-of-a-track-in-an-hour", _laps)

# ---- the data-sufficiency block's Quant item
def _ds1():
    salaries = range(1000, 100001, 1000)
    s1 = [s for s in salaries if s * F(20, 100) == 6000]                       # spends 80%, saves ₹6,000
    s2 = [s for s in salaries if s - s * F(2, 3) == 10000]                     # ₹10,000 more than a sister who earns 2/3 of it
    both = [s for s in s1 if s in s2]
    assert s1 == s2 == both == [30000]
    return _ds(s1, s2, both)
DS(QA, "medium",
   "What is Ravi's monthly salary?",
   "रवि का मासिक वेतन कितना है?",
   "Ravi spends 80 per cent of his monthly salary and saves the rest, which comes to ₹6,000 a month.",
   "रवि अपने मासिक वेतन का 80 प्रतिशत ख़र्च करता है और शेष बचाता है, जो प्रति माह ₹6,000 होता है।",
   "Ravi's monthly salary is ₹10,000 more than his sister's, and his sister's monthly salary is two-thirds of his.",
   "रवि का मासिक वेतन उसकी बहन के वेतन से ₹10,000 अधिक है, और उसकी बहन का मासिक वेतन उसके वेतन का दो-तिहाई है।",
   1,
   "Statement I: Ravi saves 20 per cent of his salary, and that is ₹6,000, so the salary is ₹6,000 ÷ 0.2 = ₹30,000 -- sufficient. "
   "Statement II: if Ravi earns S, his sister earns 2S/3, and S - 2S/3 = S/3 = ₹10,000, so S = ₹30,000 -- also sufficient. Either statement alone answers the question.",
   "कथन I: रवि अपने वेतन का 20 प्रतिशत बचाता है, और वह ₹6,000 है, अतः वेतन ₹6,000 ÷ 0.2 = ₹30,000 है -- पर्याप्त। "
   "कथन II: यदि रवि का वेतन S है, तो उसकी बहन का 2S/3 है, और S - 2S/3 = S/3 = ₹10,000, अतः S = ₹30,000 -- यह भी पर्याप्त। कोई भी एक कथन अकेले प्रश्न का उत्तर दे देता है।",
   "qa-ds-a-salary-either-statement-settles", _ds1)
