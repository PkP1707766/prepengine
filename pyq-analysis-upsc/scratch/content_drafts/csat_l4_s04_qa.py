# -*- coding: utf-8 -*-
"""CSAT Level 4 · Simulator 4 -- Quantitative Aptitude (38 items: 36 in the Quant slots, 2 in the data-sufficiency block).

Layout A again, the 2023/2024 shape: Quant-heavy, number theory the largest bucket (10). Exam-level mix (8 easy /
19 medium / 11 hard), with none of the shapes of Levels 1-3 or Simulators 1-3: the century rule for leap years, a
square that is a multiple of 7, a sum of (-1) powers, the digits of 1 to 99 added, two-digit numbers from 1, 2 and 3,
the LCM over the HCF of three numbers, the largest four-digit number leaving 2 by 13, numbers that are differences of
two squares, a sum of two cubes in two ways, whole-number points on |x| + |y| = 3; a train that passes two walkers, a
race won by the time ratio, swimmers meeting a second time, a kilometre in 45 seconds; a barter chain, pens
against notebooks, mean, median and mode, votes that would switch a result, a committee as young as it was; simple
interest matched to compound, a stake held through a company, a price that covers an agent's commission; a doubling
sum, the first multiple of 9 whose digits do not add to 9; lines through ten points, exactly one six in two rolls,
couples seated alternately; a tree measured by its shadow, sides that can make a triangle; a job finished at double
speed, three days on and one off; chocolates bought with wrappers, a league that follows the groups, palindromic
times, 1 March from 1 January, meetings that need rooms; and two data-sufficiency items. Every key is worked out in
code by check()."""
from fractions import Fraction as F
from itertools import combinations, permutations
import datetime as dt
import math
import csat_common as c
from csat_common import N, T, S2, DS, QA

def _ds(s1, s2, both):
    alone = (len(set(s1)) == 1, len(set(s2)) == 1)
    return "b" if all(alone) else "a" if any(alone) else "c" if len(set(both)) == 1 else "d"

def indian(n):
    t = str(n); head, tail = t[:-3], t[-3:]
    pairs = []
    while head:
        pairs.insert(0, head[-2:]); head = head[:-2]
    return ",".join(pairs + [tail])

# ---------------------------------------------------------------- Number Theory (10)
def _nt1():
    leap = lambda y: y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)
    ys = [y for y in (1700, 1800, 1900, 2000) if leap(y)]
    assert ys == [2000]
    return "2000"
N(QA, "Number Theory", "medium",
  "Which one of the following years was a leap year?",
  "निम्नलिखित में से कौन-सा वर्ष अधिवर्ष (लीप वर्ष) था?",
  ["1700", "1800", "1900", "2000"], 3,
  "A year divisible by 4 is a leap year, except that a century year must be divisible by 400. All four are century years; only 2000 is divisible by 400, so only 2000 was a leap year. 1700, 1800 and 1900 are divisible by 4 and by 100 but not by 400 -- the trap is to stop at the test for 4.",
  "4 से विभाज्य वर्ष अधिवर्ष होता है, इस अपवाद के साथ कि शताब्दी वर्ष को 400 से विभाज्य होना चाहिए। चारों शताब्दी वर्ष हैं; केवल 2000, 400 से विभाज्य है, इसलिए केवल 2000 अधिवर्ष था। 1700, 1800 और 1900, 4 और 100 से विभाज्य हैं पर 400 से नहीं -- जाल 4 की जाँच पर रुक जाना है।",
  "qa-nt-the-century-rule-for-leap-years", _nt1)

def _nt2():
    xs = [n for n in (196, 225, 256, 289) if n % 7 == 0]
    assert xs == [196] and all(math.isqrt(n) ** 2 == n for n in (196, 225, 256, 289))
    return "196"
N(QA, "Number Theory", "easy",
  "Which one of the following perfect squares is divisible by 7?",
  "निम्नलिखित में से कौन-सा पूर्ण वर्ग 7 से विभाज्य है?",
  ["196", "225", "256", "289"], 0,
  "A square is divisible by 7 only if its root is, since 7 is prime. The roots are 14, 15, 16 and 17, and only 14 is a multiple of 7: 196 = 14² = 7 × 28. 225, 256 and 289 have roots 15, 16 and 17, none divisible by 7.",
  "चूँकि 7 अभाज्य है, कोई वर्ग 7 से तभी विभाज्य है जब उसका मूल हो। मूल 14, 15, 16 और 17 हैं, और केवल 14, 7 का गुणज है: 196 = 14² = 7 × 28। 225, 256 और 289 के मूल 15, 16 और 17 हैं, जिनमें से कोई 7 से विभाज्य नहीं।",
  "qa-nt-a-square-that-is-a-multiple-of-7", _nt2)

def _nt3():
    return str(sum((-1) ** k for k in range(1, 100)))
N(QA, "Number Theory", "easy",
  "What is the value of (-1)¹ + (-1)² + (-1)³ + ... + (-1)⁹⁹?",
  "(-1)¹ + (-1)² + (-1)³ + ... + (-1)⁹⁹ का मान क्या है?",
  ["-1", "0", "1", "99"], 0,
  "The terms are -1, +1, -1, +1, ...: each pair of a -1 and the +1 after it adds to 0. The first 98 terms make 49 such pairs, adding to 0, and the 99th term, an odd power, is -1. So the sum is -1. 0 forgets that 99 terms cannot all be paired; 1 and 99 have no basis.",
  "पद -1, +1, -1, +1, ... हैं: हर -1 और उसके बाद का +1 मिलकर 0 बनाते हैं। पहले 98 पद ऐसे 49 जोड़े बनाते हैं, जिनका योग 0 है, और 99वाँ पद, एक विषम घात, -1 है। अतः योग -1 है। 0 यह भूल जाता है कि 99 पदों के सब जोड़े नहीं बन सकते; 1 और 99 का कोई आधार नहीं।",
  "qa-nt-a-sum-of-minus-one-powers", _nt3)

def _nt4():
    s = sum(sum(map(int, str(n))) for n in range(1, 100))
    assert s == 900 and sum(range(1, 100)) == 4950
    return "900"
N(QA, "Number Theory", "medium",
  "What is the sum of all the digits used in writing the numbers from 1 to 99?",
  "1 से 99 तक की संख्याएँ लिखने में प्रयुक्त सभी अंकों का योग क्या है?",
  ["900", "990", "1,000", "4,950"], 0,
  "In the units place each digit 0 to 9 appears 10 times, giving 10 × 45 = 450. In the tens place each digit 1 to 9 appears 10 times (10-19, 20-29, ...), another 450. In all 900. "
  "4,950 adds the numbers themselves, not their digits; 990 and 1,000 have no basis.",
  "इकाई के स्थान पर 0 से 9 तक हर अंक 10 बार आता है, जिससे 10 × 45 = 450 मिलता है। दहाई के स्थान पर 1 से 9 तक हर अंक 10 बार आता है (10-19, 20-29, ...), और 450। कुल 900। "
  "4,950 संख्याओं को जोड़ता है, उनके अंकों को नहीं; 990 और 1,000 का कोई आधार नहीं।",
  "qa-nt-the-digits-of-1-to-99-added", _nt4)

def _nt5():
    return str(sum(10 * a + b for a, b in permutations((1, 2, 3), 2)))
N(QA, "Number Theory", "medium",
  "All the two-digit numbers that can be formed from the digits 1, 2 and 3, without using a digit twice in the same number, are added together. What is the total?",
  "अंकों 1, 2 और 3 से, एक ही संख्या में किसी अंक को दो बार प्रयोग किए बिना, बन सकने वाली दो अंकों की सभी संख्याओं को जोड़ा जाता है। योग क्या है?",
  ["66", "123", "132", "264"], 2,
  "The numbers are 12, 13, 21, 23, 31 and 32. Each digit appears twice in the tens place and twice in the units place, so the total is (1 + 2 + 3) × 2 × (10 + 1) = 6 × 22 = 132. "
  "66 counts each digit only once in each place; 264 doubles the total; 123 has no basis.",
  "संख्याएँ 12, 13, 21, 23, 31 और 32 हैं। हर अंक दहाई के स्थान पर दो बार और इकाई के स्थान पर दो बार आता है, इसलिए योग (1 + 2 + 3) × 2 × (10 + 1) = 6 × 22 = 132 है। "
  "66 हर अंक को हर स्थान पर केवल एक बार गिनता है; 264 योग को दोगुना कर देता है; 123 का कोई आधार नहीं।",
  "qa-nt-two-digit-numbers-from-1-2-and-3", _nt5)

def _nt6():
    l, h = math.lcm(12, 18, 24), math.gcd(12, 18, 24)
    return str(l // h)
N(QA, "Number Theory", "medium",
  "What is the LCM of 12, 18 and 24 divided by their HCF?",
  "12, 18 और 24 के LCM को उनके HCF से भाग देने पर क्या मिलता है?",
  ["6", "12", "36", "72"], 1,
  "12 = 2² × 3, 18 = 2 × 3², 24 = 2³ × 3. The LCM takes the highest powers, 2³ × 3² = 72; the HCF takes the lowest, 2 × 3 = 6. So 72 ÷ 6 = 12. 72 is the LCM and 6 the HCF; 36 divides the LCM by 2.",
  "12 = 2² × 3, 18 = 2 × 3², 24 = 2³ × 3। LCM सबसे बड़ी घातें लेता है, 2³ × 3² = 72; HCF सबसे छोटी, 2 × 3 = 6। अतः 72 ÷ 6 = 12। 72, LCM है और 6, HCF; 36, LCM को 2 से भाग देता है।",
  "qa-nt-the-lcm-over-the-hcf-of-three-numbers", _nt6)

def _nt7():
    n = max(n for n in range(1000, 10000) if n % 13 == 2)
    assert 9997 == 13 * 769 and n == 9999
    return str(n)
N(QA, "Number Theory", "medium",
  "What is the largest four-digit number that leaves a remainder of 2 when divided by 13?",
  "चार अंकों की वह सबसे बड़ी संख्या कौन-सी है जो 13 से भाग देने पर शेषफल 2 छोड़ती है?",
  ["9984", "9986", "9997", "9999"], 3,
  "Start from the largest four-digit number: 9999 = 13 × 769 + 2, so 9999 itself leaves remainder 2. "
  "9997 is the largest four-digit multiple of 13; 9984 is the multiple before it; 9986 adds the 2 to that smaller multiple, stepping back a whole 13 too far.",
  "चार अंकों की सबसे बड़ी संख्या से शुरू कीजिए: 9999 = 13 × 769 + 2, इसलिए स्वयं 9999 शेष 2 छोड़ती है। "
  "9997, चार अंकों का सबसे बड़ा 13 का गुणज है; 9984 उससे पहले का गुणज है; 9986 उस छोटे गुणज में 2 जोड़ता है, एक पूरा 13 ज़्यादा पीछे जाकर।",
  "qa-nt-the-largest-four-digit-number-leaving-2-by-13", _nt7)

def _nt8():
    ns = [n for n in range(1, 101) if any(a * a - b * b == n for a in range(1, 102) for b in range(a))]
    assert all(n % 4 != 2 for n in ns) and len([n for n in range(1, 101) if n % 4 == 2]) == 25
    return str(len(ns))
N(QA, "Number Theory", "hard",
  "How many of the whole numbers from 1 to 100 can be written as the difference of two perfect squares (counting 0 as a perfect square)?",
  "1 से 100 तक की कितनी पूर्ण संख्याओं को दो पूर्ण वर्गों के अंतर के रूप में लिखा जा सकता है (0 को पूर्ण वर्ग मानते हुए)?",
  ["50", "67", "75", "100"], 2,
  "a² - b² = (a - b)(a + b), and the two factors a - b and a + b are both odd or both even. So the difference is either odd (every odd number n is ((n + 1)/2)² - ((n - 1)/2)²) or a multiple of 4 (4k = (k + 1)² - (k - 1)²). A number that is even but not a multiple of 4 -- 2, 6, 10, ..., 98 -- can never be such a difference. "
  "There are 25 of those, so 100 - 25 = 75 numbers can. 50 counts only the odd numbers; 100 assumes every number can; 67 has no basis.",
  "a² - b² = (a - b)(a + b), और दोनों गुणनखंड a - b और a + b या तो दोनों विषम हैं या दोनों सम। इसलिए अंतर या तो विषम है (हर विषम n = ((n + 1)/2)² - ((n - 1)/2)²) या 4 का गुणज (4k = (k + 1)² - (k - 1)²)। जो संख्या सम है पर 4 का गुणज नहीं -- 2, 6, 10, ..., 98 -- वह कभी ऐसा अंतर नहीं हो सकती। "
  "ऐसी 25 हैं, इसलिए 100 - 25 = 75 संख्याएँ हो सकती हैं। 50 केवल विषम संख्याएँ गिनता है; 100 मान लेता है कि हर संख्या हो सकती है; 67 का कोई आधार नहीं।",
  "qa-nt-numbers-that-are-differences-of-two-squares", _nt8)

def _nt9():
    ways = {}
    for a in range(1, 20):
        for b in range(a, 20):
            ways.setdefault(a ** 3 + b ** 3, []).append((a, b))
    xs = [n for n in (1000, 1728, 1729, 1730) if len(ways.get(n, [])) >= 2]
    assert xs == [1729] and ways[1729] == [(1, 12), (9, 10)]
    assert not any(n in ways for n in (1000, 1728, 1730))
    return "1,729"
N(QA, "Number Theory", "hard",
  "Which one of the following numbers can be written as the sum of two positive cubes in two different ways?",
  "निम्नलिखित में से किस संख्या को दो धनात्मक घनों के योग के रूप में दो अलग-अलग तरीक़ों से लिखा जा सकता है?",
  ["1,000", "1,728", "1,729", "1,730"], 2,
  "1,729 = 1³ + 12³ = 1 + 1,728, and also 9³ + 10³ = 729 + 1,000. It is the smallest number with this property, made famous by the mathematician Srinivasa Ramanujan. "
  "1,000 = 10³ and 1,728 = 12³ are single cubes and not sums of two positive cubes; 1,730 = 1³ + 1³ + 12³ needs three cubes.",
  "1,729 = 1³ + 12³ = 1 + 1,728, और 9³ + 10³ = 729 + 1,000 भी। यह इस गुण वाली सबसे छोटी संख्या है, जिसे गणितज्ञ श्रीनिवास रामानुजन ने प्रसिद्ध किया। "
  "1,000 = 10³ और 1,728 = 12³ अकेले घन हैं, दो धनात्मक घनों के योग नहीं; 1,730 = 1³ + 1³ + 12³ के लिए तीन घन चाहिए।",
  "qa-nt-a-sum-of-two-cubes-in-two-ways", _nt9)

def _nt10():
    return str(sum(1 for x in range(-5, 6) for y in range(-5, 6) if abs(x) + abs(y) == 3))
N(QA, "Number Theory", "hard",
  "How many pairs of integers (x, y), positive, negative or zero, satisfy |x| + |y| = 3?",
  "पूर्णांकों के कितने जोड़े (x, y), धनात्मक, ऋणात्मक या शून्य, |x| + |y| = 3 को संतुष्ट करते हैं?",
  ["4", "8", "12", "16"], 2,
  "With |x| = 0 or 3 one coordinate is 0 and the other ±3: (0, ±3) and (±3, 0), 4 pairs. With |x| = 1 or 2 neither is 0, and each sign can be chosen: (±1, ±2) and (±2, ±1), 8 pairs. In all 12. "
  "4 counts only the pairs with a zero; 8 only those without; 16 counts the zero cases twice.",
  "|x| = 0 या 3 होने पर एक निर्देशांक 0 और दूसरा ±3 है: (0, ±3) और (±3, 0), 4 जोड़े। |x| = 1 या 2 होने पर कोई 0 नहीं, और हर चिह्न चुना जा सकता है: (±1, ±2) और (±2, ±1), 8 जोड़े। कुल 12। "
  "4 केवल शून्य वाले जोड़े गिनता है; 8 केवल बिना शून्य वाले; 16 शून्य वाली स्थितियों को दो बार गिनता है।",
  "qa-nt-whole-number-points-on-a-diamond", _nt10)

# ---------------------------------------------------------------- Speed-Distance-Time (4)
def _sdt1():
    walker = F(36, 10) * 1000 / 3600                # 3.6 km/h in m/s
    v = next(F(k, 10) for k in range(1, 1000) if 12 * (F(k, 10) - walker) == 10 * (F(k, 10) + walker))
    assert walker == 1 and v == 11
    return f"{int(10 * (v + walker))} m"
N(QA, "Speed-Distance-Time", "medium",
  "Two people walk beside a railway line at 3.6 km/h each: one in the same direction as a passing train, the other towards it. The train takes 12 seconds to pass the first and 10 seconds to pass the second. How long is the train?",
  "दो लोग एक रेल लाइन के किनारे 3.6 किमी/घंटा से चल रहे हैं: एक गुज़रती रेलगाड़ी की ही दिशा में, दूसरा उसकी ओर। रेलगाड़ी पहले को पार करने में 12 सेकंड और दूसरे को पार करने में 10 सेकंड लेती है। रेलगाड़ी कितनी लंबी है?",
  ["110 m", "120 m", "132 m", "144 m"], 1,
  "3.6 km/h is 1 m/s. If the train's speed is v m/s, it passes the first walker at v - 1 and the second at v + 1, so its length is 12(v - 1) = 10(v + 1), giving v = 11 m/s and a length of 10 × 12 = 120 m. "
  "110 m multiplies the train's speed by 10 seconds without adding the second walker's speed; 132 m multiplies it by 12 seconds without taking away the first walker's; 144 m has no basis.",
  "3.6 किमी/घंटा = 1 मीटर/सेकंड। यदि रेलगाड़ी की चाल v मीटर/सेकंड है, तो वह पहले को v - 1 और दूसरे को v + 1 की सापेक्ष चाल से पार करती है, इसलिए उसकी लंबाई 12(v - 1) = 10(v + 1) है, जिससे v = 11 मीटर/सेकंड और लंबाई 10 × 12 = 120 मीटर। "
  "110 मीटर रेलगाड़ी की चाल को दूसरे की चाल जोड़े बिना 10 सेकंड से गुणा करता है; 132 मीटर उसे पहले की चाल घटाए बिना 12 सेकंड से गुणा करता है; 144 मीटर का कोई आधार नहीं।",
  "qa-sdt-a-train-that-passes-two-walkers", _sdt1,
  opts_hi=["110 मीटर", "120 मीटर", "132 मीटर", "144 मीटर"])

def _sdt2():
    return f"{int(100 - 100 * F(4, 5))} m"
N(QA, "Speed-Distance-Time", "medium",
  "Two runners take 16 seconds and 20 seconds to run 100 m. In a 100 m race between them, by how many metres does the faster one win?",
  "दो धावक 100 मीटर दौड़ने में 16 सेकंड और 20 सेकंड लेते हैं। उनके बीच 100 मीटर की दौड़ में तेज़ धावक कितने मीटर से जीतता है?",
  ["10 m", "20 m", "25 m", "80 m"], 1,
  "When the faster runner finishes, after 16 seconds, the slower one has run 16/20 of the race, that is 80 m. So the faster wins by 20 m. "
  "25 m divides the 4-second gap by the faster time (4/16 of 100) instead of the slower; 80 m is the slower runner's position, not the margin; 10 m has no basis.",
  "जब तेज़ धावक 16 सेकंड बाद समाप्त करता है, धीमा धावक दौड़ का 16/20, यानी 80 मीटर दौड़ चुका है। अतः तेज़ धावक 20 मीटर से जीतता है। "
  "25 मीटर 4 सेकंड के अंतर को धीमे के बजाय तेज़ समय से भाग देता है (100 का 4/16); 80 मीटर धीमे धावक की स्थिति है, अंतर नहीं; 10 मीटर का कोई आधार नहीं।",
  "qa-sdt-a-race-won-by-the-time-ratio", _sdt2,
  opts_hi=["10 मीटर", "20 मीटर", "25 मीटर", "80 मीटर"])

def _sdt3():
    def pos(start, v, t):                        # a swimmer bouncing between the ends 0 and 100
        x = (start + v * t) % 200
        return x if x <= 100 else 200 - x
    meets, prev = [], None
    for k in range(1, 12001):                    # steps of 1/100 s up to 120 s
        t = F(k, 100)
        d = pos(0, 3, t) - pos(200 - 100, 2, t)   # B starts at 100 heading towards 0
        if d == 0 or (prev is not None and (prev > 0) != (d > 0) and prev != 0):
            meets.append(t)
        prev = d
    assert meets[0] == 20
    return f"{meets[1]} s"
N(QA, "Speed-Distance-Time", "hard",
  "Two swimmers start at the same moment from opposite ends of a 100 m pool, one at 3 m/s and the other at 2 m/s, and swim lengths without stopping, turning instantly at each end. After how long do they meet for the second time?",
  "दो तैराक एक साथ 100 मीटर के तालाब के विपरीत छोरों से तैरना शुरू करते हैं, एक 3 मीटर/सेकंड से और दूसरा 2 मीटर/सेकंड से, और बिना रुके लंबाइयाँ तैरते हैं, हर छोर पर तुरंत मुड़ते हुए। कितने समय बाद वे दूसरी बार मिलते हैं?",
  ["20 s", "40 s", "60 s", "80 s"], 2,
  "Together they cover 5 m every second. They first meet when their combined distance is one length, 100 m, after 20 s. Between one meeting and the next each reaches the far end and comes back, so together they cover two more lengths: the second meeting comes when their combined distance is three lengths, 300 m, after 60 s. "
  "40 s assumes the second meeting needs only two lengths in all; 20 s is the first meeting; 80 s has no basis.",
  "दोनों मिलकर हर सेकंड 5 मीटर तय करते हैं। वे पहली बार तब मिलते हैं जब उनकी कुल दूरी एक लंबाई, 100 मीटर, हो, 20 सेकंड बाद। एक भेंट और अगली के बीच हर एक दूर के छोर तक पहुँचकर लौटता है, इसलिए मिलकर वे दो और लंबाइयाँ तय करते हैं: दूसरी भेंट तब होती है जब कुल दूरी तीन लंबाइयाँ, 300 मीटर, हो, 60 सेकंड बाद। "
  "40 सेकंड मान लेता है कि दूसरी भेंट के लिए कुल दो लंबाइयाँ ही चाहिए; 20 सेकंड पहली भेंट है; 80 सेकंड का कोई आधार नहीं।",
  "qa-sdt-swimmers-meeting-a-second-time", _sdt3)

def _sdt4():
    return f"{3600 // 45} km/h"
N(QA, "Speed-Distance-Time", "easy",
  "A train covers 1 km in 45 seconds. What is its speed?",
  "एक रेलगाड़ी 1 किमी, 45 सेकंड में तय करती है। उसकी चाल क्या है?",
  ["80 km/h", "90 km/h", "120 km/h", "135 km/h"], 0,
  "An hour has 3,600 seconds, so the train covers 3,600 ÷ 45 = 80 km in an hour: 80 km/h. 135 km/h multiplies 45 by 3; 90 and 120 km/h would need 40 and 30 seconds a kilometre.",
  "एक घंटे में 3,600 सेकंड होते हैं, इसलिए रेलगाड़ी एक घंटे में 3,600 ÷ 45 = 80 किमी चलती है: 80 किमी/घंटा। 135 किमी/घंटा, 45 को 3 से गुणा करता है; 90 और 120 किमी/घंटा के लिए प्रति किलोमीटर 40 और 30 सेकंड चाहिए।",
  "qa-sdt-a-kilometre-in-45-seconds", _sdt4,
  opts_hi=["80 किमी/घंटा", "90 किमी/घंटा", "120 किमी/घंटा", "135 किमी/घंटा"])

# ---------------------------------------------------------------- Ratio, Mixtures & Alligation (5)
def _rm1():
    apples_per_orange = F(3, 2)                # 3 apples = 2 oranges
    oranges_per_banana = F(4, 5)               # 4 oranges = 5 bananas
    return str(int(10 * oranges_per_banana * apples_per_orange))
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "In a village market, 3 apples can be exchanged for 2 oranges, and 4 oranges for 5 bananas. How many apples can be exchanged for 10 bananas?",
  "एक गाँव के बाज़ार में 3 सेब के बदले 2 संतरे, और 4 संतरों के बदले 5 केले मिलते हैं। 10 केलों के बदले कितने सेब मिल सकते हैं?",
  ["12", "15", "18", "20"], 0,
  "10 bananas are worth 10 × 4/5 = 8 oranges, and each orange is worth 3/2 of an apple, so 8 oranges are worth 12 apples. "
  "15 multiplies 10 by 3/2 and skips the oranges; 18 and 20 turn one of the ratios upside down.",
  "10 केले 10 × 4/5 = 8 संतरों के बराबर हैं, और हर संतरा 3/2 सेब के बराबर है, इसलिए 8 संतरे 12 सेब के बराबर हैं। "
  "15, 10 को 3/2 से गुणा करता है और संतरों का चरण छोड़ देता है; 18 और 20 किसी एक अनुपात को उलट देते हैं।",
  "qa-rm-a-barter-chain", _rm1)

def _rm2():
    r = F(8, 12)                                # 12 pens cost as much as 8 notebooks: pen / notebook = 8 / 12
    return f"{r.numerator} : {r.denominator}"
N(QA, "Ratio, Mixtures & Alligation", "easy",
  "12 pens cost as much as 8 notebooks. What is the ratio of the price of a pen to the price of a notebook?",
  "12 पेनों का मूल्य 8 नोटबुकों के बराबर है। एक पेन के मूल्य और एक नोटबुक के मूल्य का अनुपात क्या है?",
  ["2 : 3", "3 : 2", "3 : 4", "4 : 5"], 0,
  "If 12 pens cost as much as 8 notebooks, a pen costs 8/12 = 2/3 of a notebook: the ratio is 2 : 3. More pens are needed to match fewer notebooks, so each pen is cheaper. "
  "3 : 2 reads the counts straight across, which turns the ratio upside down; 3 : 4 and 4 : 5 have no basis.",
  "यदि 12 पेनों का मूल्य 8 नोटबुकों के बराबर है, तो एक पेन का मूल्य एक नोटबुक का 8/12 = 2/3 है: अनुपात 2 : 3 है। कम नोटबुकों के बराबर होने के लिए अधिक पेन चाहिए, इसलिए हर पेन सस्ता है। "
  "3 : 2 संख्याओं को सीधे पढ़ता है, जो अनुपात को उलट देता है; 3 : 4 और 4 : 5 का कोई आधार नहीं।",
  "qa-rm-pens-against-notebooks", _rm2)

def _rm3():
    data = [3, 5, 5, 7, 10]
    mean, median = F(sum(data), 5), sorted(data)[2]
    mode = max(set(data), key=data.count)
    one, two = mean > median, median == mode
    return c.T2[{(True, False): 0, (False, True): 1, (True, True): 2, (False, False): 3}[(one, two)]]
S2(QA, "Ratio, Mixtures & Alligation", "medium",
   "Consider the five marks 3, 5, 5, 7 and 10. Which of the following statements is/are correct?",
   "पाँच अंकों 3, 5, 5, 7 और 10 पर विचार कीजिए। निम्नलिखित में से कौन-सा/से कथन सही है/हैं?",
   ["The mean of the marks is greater than their median.", "The median of the marks is equal to their mode."],
   ["अंकों का माध्य उनकी माध्यिका से बड़ा है।", "अंकों की माध्यिका उनके बहुलक के बराबर है।"],
   2,
   "Both are correct. The mean is 30 ÷ 5 = 6, and the median, the middle mark in order, is 5, so the mean is greater (1). The mode, the most frequent mark, is also 5, equal to the median (2). The single high mark of 10 pulls the mean above the middle.",
   "दोनों सही हैं। माध्य 30 ÷ 5 = 6 है, और माध्यिका, क्रम में बीच का अंक, 5 है, इसलिए माध्य बड़ा है (1)। बहुलक, सबसे अधिक बार आने वाला अंक, भी 5 है, माध्यिका के बराबर (2)। 10 का अकेला ऊँचा अंक माध्य को बीच से ऊपर खींच लेता है।",
   "qa-rm-mean-median-and-mode", check=_rm3)

def _rm4():
    ks = [k for k in range(1, 5000) if (3 * k + 1200) - (5 * k - 1200) == 400]
    assert ks == [1000]
    return indian(8 * ks[0])
N(QA, "Ratio, Mixtures & Alligation", "hard",
  "In an election between two candidates, A and B, their votes were in the ratio 5 : 3. Had 1,200 of A's voters voted for B instead, B would have won by 400 votes. How many votes were cast in all?",
  "दो उम्मीदवारों, A और B, के बीच एक चुनाव में उनके मत 5 : 3 के अनुपात में थे। यदि A के 1,200 मतदाताओं ने इसके बजाय B को मत दिया होता, तो B 400 मतों से जीत जाता। कुल कितने मत डाले गए?",
  ["4,800", "6,400", "8,000", "9,600"], 2,
  "Let the votes be 5k and 3k. After the switch A has 5k - 1,200 and B has 3k + 1,200, and B leads by 400: (3k + 1,200) - (5k - 1,200) = 400, so 2,400 - 2k = 400 and k = 1,000. The votes were 5,000 and 3,000: 8,000 in all. "
  "Check: after the switch A has 3,800 and B 4,200. 4,800, 6,400 and 9,600 take a part of the ratio as 600, 800 and 1,200.",
  "मान लीजिए मत 5k और 3k थे। बदलाव के बाद A के 5k - 1,200 और B के 3k + 1,200 होते, और B 400 से आगे होता: (3k + 1,200) - (5k - 1,200) = 400, अतः 2,400 - 2k = 400 और k = 1,000। मत 5,000 और 3,000 थे: कुल 8,000। "
  "जाँच: बदलाव के बाद A के 3,800 और B के 4,200। 4,800, 6,400 और 9,600 अनुपात के एक भाग को 600, 800 और 1,200 मानते हैं।",
  "qa-rm-votes-that-would-switch-a-result", _rm4)

def _rm5():
    members, years = 8, 4
    return f"{members * years} years"
N(QA, "Ratio, Mixtures & Alligation", "hard",
  "The average age of an 8-member committee is the same today as it was 4 years ago, because in the meantime one member was replaced by a new one. How much younger is the new member than the member replaced (comparing their ages at the time of the change)?",
  "8 सदस्यों वाली एक समिति की औसत आयु आज भी उतनी ही है जितनी 4 वर्ष पहले थी, क्योंकि इस बीच एक सदस्य की जगह एक नया सदस्य आया। नया सदस्य हटाए गए सदस्य से कितना छोटा है (बदलाव के समय उनकी आयु की तुलना करते हुए)?",
  ["4 years", "8 years", "28 years", "32 years"], 3,
  "In 4 years each of the 8 members would have grown 4 years older, raising the total age by 8 × 4 = 32 years and the average by 4. For the average to stay the same, the new member must have been 32 years younger than the one replaced. "
  "4 years is the rise in the average, not in the total; 8 years and 28 years have no basis.",
  "4 वर्षों में 8 में से हर सदस्य 4 वर्ष बड़ा हो जाता, जिससे कुल आयु 8 × 4 = 32 वर्ष और औसत 4 बढ़ता। औसत वही रहने के लिए नए सदस्य को हटाए गए सदस्य से 32 वर्ष छोटा होना चाहिए। "
  "4 वर्ष औसत की वृद्धि है, कुल की नहीं; 8 वर्ष और 28 वर्ष का कोई आधार नहीं।",
  "qa-rm-a-committee-as-young-as-it-was", _rm5,
  opts_hi=["4 वर्ष", "8 वर्ष", "28 वर्ष", "32 वर्ष"])

# ---------------------------------------------------------------- Percentage & Profit-Loss (3)
def _pp1():
    ci = 5000 * (F(11, 10) ** 2 - 1)
    r = ci / (5000 * 2) * 100
    assert ci == 1050 and r == F(21, 2)
    return "10.5 per cent"
N(QA, "Percentage & Profit-Loss", "medium",
  "₹5,000 earns compound interest at 10 per cent a year for 2 years. At what rate of simple interest would the same sum earn the same interest in the same 2 years?",
  "₹5,000 पर 2 वर्षों के लिए 10 प्रतिशत वार्षिक चक्रवृद्धि ब्याज मिलता है। साधारण ब्याज की किस दर पर वही राशि उन्हीं 2 वर्षों में उतना ही ब्याज कमाएगी?",
  ["10.5 per cent", "11 per cent", "12 per cent", "21 per cent"], 0,
  "Compound interest for 2 years at 10 per cent is 5,000 × (1.1² - 1) = 5,000 × 0.21 = ₹1,050. Simple interest of ₹1,050 on ₹5,000 over 2 years means ₹525 a year, that is 10.5 per cent. "
  "21 per cent is the total over the two years, not a yearly rate; 11 and 12 per cent have no basis.",
  "10 प्रतिशत पर 2 वर्षों का चक्रवृद्धि ब्याज 5,000 × (1.1² - 1) = 5,000 × 0.21 = ₹1,050 है। ₹5,000 पर 2 वर्षों में ₹1,050 साधारण ब्याज का अर्थ है प्रति वर्ष ₹525, यानी 10.5 प्रतिशत। "
  "21 प्रतिशत दोनों वर्षों का कुल है, वार्षिक दर नहीं; 11 और 12 प्रतिशत का कोई आधार नहीं।",
  "qa-pp-simple-interest-matched-to-compound", _pp1,
  opts_hi=["10.5 प्रतिशत", "11 प्रतिशत", "12 प्रतिशत", "21 प्रतिशत"])

def _pp2():
    return f"{int(F(60, 100) * F(40, 100) * 100)} per cent"
N(QA, "Percentage & Profit-Loss", "medium",
  "A person owns 60 per cent of a company, and that company owns 40 per cent of a second company. What share of the second company does the person own indirectly?",
  "एक व्यक्ति किसी कंपनी का 60 प्रतिशत स्वामी है, और वह कंपनी एक दूसरी कंपनी की 40 प्रतिशत स्वामी है। दूसरी कंपनी में उस व्यक्ति का अप्रत्यक्ष हिस्सा कितना है?",
  ["20 per cent", "24 per cent", "40 per cent", "100 per cent"], 1,
  "The person owns 60 per cent of the company's 40 per cent stake: 0.6 × 0.4 = 0.24, that is 24 per cent. "
  "40 per cent treats the person as owning the whole of the company's stake; 100 per cent assumes control means full ownership; 20 per cent subtracts 40 from 60.",
  "व्यक्ति कंपनी के 40 प्रतिशत हिस्से का 60 प्रतिशत स्वामी है: 0.6 × 0.4 = 0.24, यानी 24 प्रतिशत। "
  "40 प्रतिशत व्यक्ति को कंपनी के पूरे हिस्से का स्वामी मानता है; 100 प्रतिशत मान लेता है कि नियंत्रण का अर्थ पूर्ण स्वामित्व है; 20 प्रतिशत, 60 में से 40 घटाता है।",
  "qa-pp-a-stake-held-through-a-company", _pp2,
  opts_hi=["20 प्रतिशत", "24 प्रतिशत", "40 प्रतिशत", "100 प्रतिशत"])

def _pp3():
    markup = (F(12, 10) / F(9, 10) - 1) * 100
    assert markup == F(100, 3)
    return "33⅓ per cent"
N(QA, "Percentage & Profit-Loss", "hard",
  "A producer sells through an agent who keeps 10 per cent of the selling price as commission. By what percentage above the cost must the selling price be set so that the producer still makes a profit of 20 per cent on the cost?",
  "एक उत्पादक एक एजेंट के माध्यम से बेचता है जो बिक्री मूल्य का 10 प्रतिशत कमीशन के रूप में रखता है। बिक्री मूल्य लागत से कितने प्रतिशत ऊपर रखा जाए ताकि उत्पादक को लागत पर फिर भी 20 प्रतिशत लाभ हो?",
  ["20 per cent", "30 per cent", "32 per cent", "33⅓ per cent"], 3,
  "The producer keeps 90 per cent of the selling price and wants this to be 120 per cent of the cost: 0.9 × SP = 1.2 × cost, so SP = 4/3 of the cost -- 33⅓ per cent above it. "
  "30 per cent simply adds the 10 per cent commission to the 20 per cent profit; 32 per cent adds 10 per cent on top of the target (1.2 × 1.1 = 1.32) -- both forget that the commission is a tenth of the selling price, which is larger than either; 20 per cent ignores the commission.",
  "उत्पादक बिक्री मूल्य का 90 प्रतिशत रखता है और चाहता है कि यह लागत का 120 प्रतिशत हो: 0.9 × बिक्री मूल्य = 1.2 × लागत, अतः बिक्री मूल्य लागत का 4/3 -- उससे 33⅓ प्रतिशत ऊपर। "
  "30 प्रतिशत बस 10 प्रतिशत कमीशन को 20 प्रतिशत लाभ में जोड़ता है; 32 प्रतिशत लक्ष्य के ऊपर 10 प्रतिशत जोड़ता है (1.2 × 1.1 = 1.32) -- दोनों भूल जाते हैं कि कमीशन बिक्री मूल्य का दसवाँ भाग है, जो दोनों से बड़ा है; 20 प्रतिशत कमीशन को अनदेखा करता है।",
  "qa-pp-a-price-that-covers-an-agent-s-commission", _pp3,
  opts_hi=["20 प्रतिशत", "30 प्रतिशत", "32 प्रतिशत", "33⅓ प्रतिशत"])

# ---------------------------------------------------------------- Sequences & Series (2)
def _ss1():
    return indian(sum(2 ** k for k in range(10)))
N(QA, "Sequences & Series", "easy",
  "What is the sum 1 + 2 + 4 + 8 + ... + 512, in which each term is double the one before?",
  "योग 1 + 2 + 4 + 8 + ... + 512 क्या है, जिसमें हर पद पिछले पद का दोगुना है?",
  ["256", "511", "512", "1,023"], 3,
  "Each partial sum is one less than the next power of 2 (1 = 2 - 1, 1 + 2 = 4 - 1, 1 + 2 + 4 = 8 - 1, ...), so the sum up to 512 is 1,024 - 1 = 1,023. "
  "512 is the last term alone; 511 is the sum up to 256; 256 has no basis.",
  "हर आंशिक योग 2 की अगली घात से एक कम है (1 = 2 - 1, 1 + 2 = 4 - 1, 1 + 2 + 4 = 8 - 1, ...), इसलिए 512 तक का योग 1,024 - 1 = 1,023 है। "
  "512 केवल अंतिम पद है; 511, 256 तक का योग है; 256 का कोई आधार नहीं।",
  "qa-ss-a-doubling-sum", _ss1)

def _ss2():
    return str(next(9 * k for k in range(1, 100) if sum(map(int, str(9 * k))) != 9))
N(QA, "Sequences & Series", "medium",
  "In the series 9, 18, 27, 36, ..., of multiples of 9, which is the first term whose digits do not add up to 9?",
  "9 के गुणजों की श्रेणी 9, 18, 27, 36, ... में वह पहला पद कौन-सा है जिसके अंकों का योग 9 नहीं है?",
  ["99", "108", "117", "189"], 0,
  "The digit sum of a multiple of 9 is always a multiple of 9, and for the two-digit terms 18 to 90 it is 9. The first term whose digits add up to more is 99, with digit sum 18. "
  "108 and 117 come later and their digits add up to 9 again; 189 (digit sum 18) also comes later.",
  "9 के किसी गुणज का अंक-योग हमेशा 9 का गुणज होता है, और 18 से 90 तक के दो अंकों वाले पदों के लिए वह 9 है। पहला पद जिसके अंकों का योग इससे अधिक है, 99 है, अंक-योग 18। "
  "108 और 117 बाद में आते हैं और उनके अंकों का योग फिर 9 है; 189 (अंक-योग 18) भी बाद में आता है।",
  "qa-ss-the-first-multiple-of-9-whose-digits-do-not-add-to-9", _ss2)

# ---------------------------------------------------------------- Permutation & Combination (3)
def _pc1():
    return str(math.comb(10, 2))
N(QA, "Permutation & Combination", "easy",
  "Ten points are marked on a sheet so that no three of them lie on one straight line. How many different straight lines can be drawn, each through two of the points?",
  "एक काग़ज़ पर दस बिंदु ऐसे अंकित हैं कि उनमें से कोई तीन एक सीधी रेखा पर नहीं हैं। कितनी अलग-अलग सीधी रेखाएँ खींची जा सकती हैं, हर एक दो बिंदुओं से होकर?",
  ["10", "20", "36", "45"], 3,
  "Each line is fixed by a pair of points, and no two pairs give the same line, since no three points are in a line. The number of pairs is 10C2 = 45. "
  "36 counts the lines through 9 points; 10 and 20 have no basis.",
  "हर रेखा बिंदुओं के एक जोड़े से तय होती है, और कोई दो जोड़े एक ही रेखा नहीं देते, क्योंकि कोई तीन बिंदु एक रेखा पर नहीं। जोड़ों की संख्या 10C2 = 45 है। "
  "36, 9 बिंदुओं से होकर जाने वाली रेखाएँ गिनता है; 10 और 20 का कोई आधार नहीं।",
  "qa-pc-lines-through-ten-points", _pc1)

def _pc2():
    p = F(sum(1 for a in range(1, 7) for b in range(1, 7) if (a == 6) + (b == 6) == 1), 36)
    return f"{p.numerator}/{p.denominator}"
N(QA, "Permutation & Combination", "medium",
  "A fair die is rolled twice. What is the probability of getting exactly one six?",
  "एक निष्पक्ष पासे को दो बार फेंका जाता है। ठीक एक छह आने की प्रायिकता क्या है?",
  ["1/6", "5/18", "11/36", "1/3"], 1,
  "The six can come on the first roll and not the second (1/6 × 5/6 = 5/36) or on the second and not the first (another 5/36): 10/36 = 5/18. "
  "11/36 is the chance of at least one six, which includes two sixes; 1/3 adds 1/6 twice; 1/6 is the chance on one roll.",
  "छह पहली बार में आए और दूसरी में नहीं (1/6 × 5/6 = 5/36) या दूसरी में आए और पहली में नहीं (और 5/36): 10/36 = 5/18। "
  "11/36 कम से कम एक छह की संभावना है, जिसमें दो छह भी शामिल हैं; 1/3, 1/6 को दो बार जोड़ता है; 1/6 एक बार फेंकने की संभावना है।",
  "qa-pc-exactly-one-six-in-two-rolls", _pc2)

def _pc3():
    def circ(seq):                               # distinct seatings round a table: fix person M1 in seat 0
        return seq[0] == "M1"
    n = 0
    for p in permutations(["M1", "M2", "M3", "M4", "W1", "W2", "W3", "W4"]):
        if circ(p) and all((p[i][0] == "M") != (p[(i + 1) % 8][0] == "M") for i in range(8)):
            n += 1
    assert n == math.factorial(3) * math.factorial(4)
    return str(n)
N(QA, "Permutation & Combination", "hard",
  "Four men and four women are to sit at a round table with eight chairs so that men and women sit in alternate chairs. In how many ways can this be done, if seatings that differ only by everyone moving round the same number of places are counted as the same?",
  "चार पुरुष और चार महिलाएँ आठ कुर्सियों वाली एक गोल मेज़ पर ऐसे बैठने हैं कि पुरुष और महिलाएँ बारी-बारी की कुर्सियों पर हों। यदि वे व्यवस्थाएँ जिनमें केवल सब लोग समान स्थान घूम जाते हैं, एक ही मानी जाएँ, तो यह कितने तरीक़ों से किया जा सकता है?",
  ["72", "96", "120", "144"], 3,
  "Seat the men first. Round a table, the four men can be arranged in (4 - 1)! = 6 ways. That fixes four alternate chairs between them, and the four women can fill those in 4! = 24 ways, since the chairs are now distinguishable. In all 6 × 24 = 144. "
  "72 halves the count, as if mirror images were the same; 120 and 96 have no basis.",
  "पहले पुरुषों को बैठाइए। गोल मेज़ पर चार पुरुष (4 - 1)! = 6 तरीक़ों से बैठ सकते हैं। इससे उनके बीच चार बारी-बारी की कुर्सियाँ तय हो जाती हैं, और चार महिलाएँ उन्हें 4! = 24 तरीक़ों से भर सकती हैं, क्योंकि अब कुर्सियाँ अलग-अलग पहचानी जा सकती हैं। कुल 6 × 24 = 144। "
  "72 गिनती को आधा कर देता है, मानो दर्पण-प्रतिबिंब एक ही हों; 120 और 96 का कोई आधार नहीं।",
  "qa-pc-couples-seated-alternately", _pc3)

# ---------------------------------------------------------------- Geometry & Mensuration (2)
def _gm1():
    return f"{int(F(15, 10) * F(24, 2))} m"
N(QA, "Geometry & Mensuration", "easy",
  "At a certain time of day a girl 1.5 m tall casts a shadow 2 m long, and a tree nearby casts a shadow 24 m long. How tall is the tree?",
  "दिन के किसी समय 1.5 मीटर लंबी एक लड़की की छाया 2 मीटर लंबी है, और पास के एक पेड़ की छाया 24 मीटर लंबी है। पेड़ कितना ऊँचा है?",
  ["12 m", "16 m", "18 m", "32 m"], 2,
  "At the same moment the sun's rays make the same angle everywhere nearby, so height and shadow are in the same ratio for both: 1.5 : 2 = h : 24, giving h = 24 × 1.5 ÷ 2 = 18 m. "
  "32 m inverts the ratio (24 × 2 ÷ 1.5); 12 m halves the shadow; 16 m has no basis.",
  "एक ही क्षण पर पास के हर स्थान पर सूर्य की किरणें एक ही कोण बनाती हैं, इसलिए दोनों के लिए ऊँचाई और छाया एक ही अनुपात में हैं: 1.5 : 2 = h : 24, जिससे h = 24 × 1.5 ÷ 2 = 18 मीटर। "
  "32 मीटर अनुपात को उलट देता है (24 × 2 ÷ 1.5); 12 मीटर छाया को आधा करता है; 16 मीटर का कोई आधार नहीं।",
  "qa-gm-a-tree-measured-by-its-shadow", _gm1,
  opts_hi=["12 मीटर", "16 मीटर", "18 मीटर", "32 मीटर"])

def _gm2():
    sets = [(10, 12, 25), (3, 4, 8), (1, 2, 3), (5, 6, 10)]
    ok = [t for t in sets if t[0] + t[1] > t[2]]
    assert ok == [(5, 6, 10)]
    return "5 cm, 6 cm and 10 cm"
T(QA, "Geometry & Mensuration", "medium",
  "Which one of the following sets of lengths can be the three sides of a triangle?",
  "निम्नलिखित में से लंबाइयों का कौन-सा समूह किसी त्रिभुज की तीन भुजाएँ हो सकता है?",
  ["5 cm, 6 cm and 10 cm", "10 cm, 12 cm and 25 cm", "3 cm, 4 cm and 8 cm", "1 cm, 2 cm and 3 cm"],
  ["5 सेमी, 6 सेमी और 10 सेमी", "10 सेमी, 12 सेमी और 25 सेमी", "3 सेमी, 4 सेमी और 8 सेमी", "1 सेमी, 2 सेमी और 3 सेमी"],
  0,
  "Three lengths make a triangle only if the two shorter ones together are longer than the longest. 5 + 6 = 11 > 10, so 5, 6 and 10 work. "
  "10 + 12 = 22 < 25 and 3 + 4 = 7 < 8 fall short; 1 + 2 = 3 only equals 3, which flattens the 'triangle' into a straight line.",
  "तीन लंबाइयाँ त्रिभुज तभी बनाती हैं जब दो छोटी मिलकर सबसे लंबी से अधिक हों। 5 + 6 = 11 > 10, इसलिए 5, 6 और 10 काम करती हैं। "
  "10 + 12 = 22 < 25 और 3 + 4 = 7 < 8 कम पड़ते हैं; 1 + 2 = 3 केवल 3 के बराबर है, जो 'त्रिभुज' को एक सीधी रेखा में चपटा कर देता है।",
  "qa-gm-sides-that-can-make-a-triangle", pos=3, check=_gm2)

# ---------------------------------------------------------------- Time & Work (2)
def _tw1():
    return f"{6 + 6 // 2} days"
N(QA, "Time & Work", "medium",
  "A worker finishes half of a job in 6 days, and then works twice as fast as before. How many days does the whole job take?",
  "एक कामगार किसी काम का आधा भाग 6 दिनों में पूरा करता है, और फिर पहले से दोगुनी तेज़ी से काम करता है। पूरा काम कितने दिनों में होता है?",
  ["8 days", "9 days", "10 days", "12 days"], 1,
  "The second half is the same amount of work as the first; at twice the speed it takes half the time, 3 days. The whole job takes 6 + 3 = 9 days. "
  "12 days ignores the speed-up; 8 and 10 days have no basis.",
  "दूसरा आधा भाग पहले जितना ही काम है; दोगुनी तेज़ी से उसमें आधा समय, 3 दिन लगता है। पूरा काम 6 + 3 = 9 दिनों में होता है। "
  "12 दिन तेज़ी को अनदेखा करता है; 8 और 10 दिन का कोई आधार नहीं।",
  "qa-tw-a-job-finished-at-double-speed", _tw1,
  opts_hi=["8 दिन", "9 दिन", "10 दिन", "12 दिन"])

def _tw2():
    day = worked = 0
    while worked < 30:
        day += 1
        if day % 4:
            worked += 1
    return str(day)
N(QA, "Time & Work", "hard",
  "A job needs 30 days of work. The worker works for 3 days and then rests for 1 day, over and over, starting with a working day. On which day, counting from the first, is the job finished?",
  "एक काम के लिए 30 दिनों का काम चाहिए। कामगार 3 दिन काम करता है और फिर 1 दिन विश्राम करता है, बार-बार, काम के दिन से शुरू करते हुए। पहले दिन से गिनने पर काम किस दिन पूरा होता है?",
  ["37th", "39th", "40th", "42nd"], 1,
  "Every block of 4 days gives 3 days of work. Ten blocks would give 30 days of work in 40 days -- but the 40th day is a rest day, and the 30th working day is the 39th day. So the job is finished on the 39th day. "
  "The 40th counts the final rest day; the 42nd and the 37th miscount the blocks.",
  "हर 4 दिनों के खंड में 3 दिन काम होता है। दस खंड 40 दिनों में 30 दिन का काम देते -- पर 40वाँ दिन विश्राम का है, और काम का 30वाँ दिन 39वाँ दिन है। अतः काम 39वें दिन पूरा होता है। "
  "40वाँ अंतिम विश्राम-दिवस भी गिन लेता है; 42वाँ और 37वाँ खंडों को ग़लत गिनते हैं।",
  "qa-tw-three-days-on-and-one-off", lambda: _tw2() + "th",
  opts_hi=["37वें", "39वें", "40वें", "42वें"])

# ---------------------------------------------------------------- Puzzle Hybrid (5)
def _ph1():
    total, wrappers = 15, 15
    while wrappers >= 3:
        new = wrappers // 3
        total += new
        wrappers = wrappers % 3 + new
    return str(total)
N(QA, "Puzzle Hybrid", "hard",
  "A shop gives one chocolate in exchange for every 3 empty wrappers. A child buys 15 chocolates, eats them all, and keeps exchanging the wrappers -- including those of the chocolates got in exchange -- for as long as she can. How many chocolates does she eat in all?",
  "एक दुकान हर 3 ख़ाली रैपरों के बदले एक चॉकलेट देती है। एक बच्ची 15 चॉकलेट ख़रीदती है, सब खा लेती है, और जब तक हो सके रैपर बदलती रहती है -- बदले में मिली चॉकलेटों के रैपर भी। वह कुल कितनी चॉकलेट खाती है?",
  ["20", "21", "22", "23"], 2,
  "15 wrappers buy 5 chocolates, leaving 5 wrappers; those buy 1 more, leaving 2 + 1 = 3 wrappers; those buy 1 more, leaving 1. In all 15 + 5 + 1 + 1 = 22. "
  "20 stops after the first exchange; 21 after the second; 23 assumes the last single wrapper can still be used.",
  "15 रैपरों से 5 चॉकलेट मिलती हैं, 5 रैपर बचते हैं; उनसे 1 और, 2 + 1 = 3 रैपर बचते हैं; उनसे 1 और, 1 बचता है। कुल 15 + 5 + 1 + 1 = 22। "
  "20 पहले बदलाव के बाद रुक जाता है; 21 दूसरे के बाद; 23 मान लेता है कि अंतिम अकेला रैपर भी काम आ सकता है।",
  "qa-ph-chocolates-bought-with-wrappers", _ph1)

def _ph2():
    groups = [list(range(4 * g, 4 * g + 4)) for g in range(4)]
    group_matches = sum(len(list(combinations(g, 2))) for g in groups)
    league = [t for g in groups for t in g[:2]]             # the top two of each group
    group_of = {t: i for i, g in enumerate(groups) for t in g}
    league_matches = sum(1 for a, b in combinations(league, 2) if group_of[a] != group_of[b])
    assert (group_matches, league_matches) == (24, 24)
    return str(group_matches + league_matches)
N(QA, "Puzzle Hybrid", "medium",
  "Sixteen teams are split into four groups of four, and in each group every team plays every other team once. The top two teams of each group then form a league of eight, in which every team plays every other team once -- except that two teams from the same group do not meet again. How many matches are played in all?",
  "सोलह टीमें चार-चार के चार समूहों में बाँटी जाती हैं, और हर समूह में हर टीम हर दूसरी टीम से एक बार खेलती है। फिर हर समूह की शीर्ष दो टीमें आठ टीमों की एक लीग बनाती हैं, जिसमें हर टीम हर दूसरी टीम से एक बार खेलती है -- सिवाय इसके कि एक ही समूह की दो टीमें फिर नहीं भिड़तीं। कुल कितने मैच खेले जाते हैं?",
  ["48", "52", "56", "96"], 0,
  "Each group plays 4C2 = 6 matches, so the groups play 4 × 6 = 24. The league of eight would have 8C2 = 28 matches, but the 4 pairs who came from the same group have already met, leaving 24. In all 24 + 24 = 48. "
  "52 forgets that teams from the same group do not meet again; 96 counts every match twice, once for each team; 56 has no basis.",
  "हर समूह 4C2 = 6 मैच खेलता है, इसलिए समूह 4 × 6 = 24 मैच खेलते हैं। आठ टीमों की लीग में 8C2 = 28 मैच होते, पर एक ही समूह से आए 4 जोड़े पहले ही भिड़ चुके हैं, इसलिए 24 बचते हैं। कुल 24 + 24 = 48। "
  "52 भूल जाता है कि एक ही समूह की टीमें फिर नहीं भिड़तीं; 96 हर मैच को दो बार गिनता है, हर टीम के लिए एक बार; 56 का कोई आधार नहीं।",
  "qa-ph-a-league-that-follows-the-groups", _ph2)

def _ph3():
    times = [f"{h:02d}{m:02d}" for h in range(24) for m in range(60)]
    return str(sum(1 for t in times if t == t[::-1]))
N(QA, "Puzzle Hybrid", "medium",
  "A time such as 12:21 on a 24-hour clock that shows hours and minutes reads the same backwards as forwards. How many such times are there in one day, counting from midnight, 00:00, to 23:59?",
  "घंटे और मिनट दिखाने वाली 24-घंटे की घड़ी पर 12:21 जैसा समय आगे और पीछे से एक जैसा पढ़ा जाता है। आधी रात, 00:00, से 23:59 तक गिनने पर एक दिन में ऐसे कितने समय होते हैं?",
  ["6", "10", "15", "16"], 3,
  "For HH:MM to read the same backwards, the minutes must be the hour's digits reversed, and that reversed number must be a valid minute (below 60). Hours 00 to 05 give 00:00, 01:10, 02:20, 03:30, 04:40, 05:50 (6); hours 06 to 09 would need minutes 60 to 90; 10 to 15 give 10:01 to 15:51 (6); 16 to 19 fail; 20 to 23 give 20:02 to 23:32 (4). "
  "In all 16. 15 leaves out 00:00; 6 and 10 stop part of the way.",
  "HH:MM के पीछे से एक जैसा पढ़े जाने के लिए मिनट घंटे के अंकों का उलटा होने चाहिए, और वह उलटी संख्या एक वैध मिनट (60 से कम) होनी चाहिए। घंटे 00 से 05 देते हैं 00:00, 01:10, 02:20, 03:30, 04:40, 05:50 (6); घंटे 06 से 09 के लिए मिनट 60 से 90 चाहिए; 10 से 15 देते हैं 10:01 से 15:51 (6); 16 से 19 विफल; 20 से 23 देते हैं 20:02 से 23:32 (4)। "
  "कुल 16। 15, 00:00 को छोड़ देता है; 6 और 10 बीच में रुक जाते हैं।",
  "qa-ph-palindromic-times", _ph3)

def _ph4():
    d = dt.date(2028, 3, 1)
    assert dt.date(2028, 1, 1).strftime("%A") == "Saturday"
    return d.strftime("%A")
N(QA, "Puzzle Hybrid", "medium",
  "1 January 2028 is a Saturday. On which day of the week does 1 March 2028 fall?",
  "1 जनवरी 2028 शनिवार है। 1 मार्च 2028 सप्ताह के किस दिन पड़ता है?",
  ["Tuesday", "Wednesday", "Thursday", "Saturday"], 1,
  "2028 is a leap year, so January has 31 days and February 29: 1 March is 31 + 29 = 60 days after 1 January. 60 = 8 weeks and 4 days, so it falls four days after Saturday -- on a Wednesday. "
  "Tuesday comes from giving February only 28 days; Thursday and Saturday have no basis.",
  "2028 अधिवर्ष है, इसलिए जनवरी में 31 और फ़रवरी में 29 दिन हैं: 1 मार्च, 1 जनवरी से 31 + 29 = 60 दिन बाद है। 60 = 8 सप्ताह और 4 दिन, इसलिए वह शनिवार के चार दिन बाद -- बुधवार को पड़ता है। "
  "मंगलवार फ़रवरी को केवल 28 दिन देने से आता है; गुरुवार और शनिवार का कोई आधार नहीं।",
  "qa-ph-1-march-from-1-january", _ph4,
  opts_hi=["मंगलवार", "बुधवार", "गुरुवार", "शनिवार"])

def _ph5():
    iv = [(540, 600), (570, 660), (600, 690), (645, 720), (690, 750)]
    return str(max(sum(1 for a, b in iv if a <= t < b) for t in range(540, 780)))
N(QA, "Puzzle Hybrid", "hard",
  "Five meetings are held in one morning: 9:00-10:00, 9:30-11:00, 10:00-11:30, 10:45-12:00 and 11:30-12:30. A room can hold only one meeting at a time, and a meeting that ends at a given time leaves its room free for one starting then. What is the least number of rooms needed?",
  "एक सुबह पाँच बैठकें होती हैं: 9:00-10:00, 9:30-11:00, 10:00-11:30, 10:45-12:00 और 11:30-12:30। एक कमरे में एक समय में एक ही बैठक हो सकती है, और किसी समय समाप्त होने वाली बैठक उसी समय शुरू होने वाली बैठक के लिए अपना कमरा ख़ाली कर देती है। कम से कम कितने कमरे चाहिए?",
  ["2", "3", "4", "5"], 1,
  "The rooms needed equal the largest number of meetings in progress at one moment. From 10:45 to 11:00 three meetings run together (9:30-11:00, 10:00-11:30 and 10:45-12:00), and at no time are there four. So three rooms are enough -- for example, room 1 for 9:00-10:00, 10:00-11:30 and 11:30-12:30; room 2 for 9:30-11:00; room 3 for 10:45-12:00. "
  "2 rooms cannot hold the three overlapping meetings; 4 and 5 are more than needed.",
  "आवश्यक कमरों की संख्या किसी एक क्षण पर चल रही बैठकों की सबसे बड़ी संख्या के बराबर है। 10:45 से 11:00 तक तीन बैठकें साथ चलती हैं (9:30-11:00, 10:00-11:30 और 10:45-12:00), और किसी समय चार नहीं होतीं। अतः तीन कमरे पर्याप्त हैं -- उदाहरण के लिए, कमरा 1 में 9:00-10:00, 10:00-11:30 और 11:30-12:30; कमरा 2 में 9:30-11:00; कमरा 3 में 10:45-12:00। "
  "2 कमरे तीन साथ-साथ चलने वाली बैठकों को नहीं सँभाल सकते; 4 और 5 आवश्यकता से अधिक हैं।",
  "qa-ph-meetings-that-need-rooms", _ph5)

# ---------------------------------------------------------------- the data-sufficiency block's two Quant items
def _ds1():
    xs = range(-30, 31)
    s1 = {x for x in xs if 3 * x + 2 == 17}
    s2 = {x for x in xs if x * x == 25 and x > 0}
    assert s1 == s2 == {5}
    return _ds(s1, s2, s1 & s2)
DS(QA, "easy",
   "What is the value of x?",
   "x का मान क्या है?",
   "3x + 2 = 17.", "3x + 2 = 17।",
   "x² = 25, and x is positive.", "x² = 25, और x धनात्मक है।",
   1,
   "Statement I gives 3x = 15, so x = 5 -- sufficient. Statement II allows x = 5 or x = -5, but x is positive, so x = 5 -- also sufficient. Either statement alone answers the question.",
   "कथन I से 3x = 15, इसलिए x = 5 -- पर्याप्त। कथन II, x = 5 या x = -5 की अनुमति देता है, पर x धनात्मक है, इसलिए x = 5 -- यह भी पर्याप्त। कोई भी एक कथन अकेले प्रश्न का उत्तर देता है।",
   "qa-ds-a-value-found-from-a-line-or-a-square", _ds1)

def _ds2():
    isprime = lambda n: n > 1 and all(n % d for d in range(2, math.isqrt(n) + 1))
    s1 = {isprime(n) for n in range(1, 100, 2)}
    s2 = {isprime(n) for n in range(1, 20)}
    both = {isprime(n) for n in range(1, 20, 2)}
    assert both == {True, False}
    return _ds(s1, s2, both)
DS(QA, "medium",
   "Is the positive integer n a prime number?",
   "क्या धनात्मक पूर्णांक n एक अभाज्य संख्या है?",
   "n is odd.", "n विषम है।",
   "n is less than 20.", "n, 20 से कम है।",
   3,
   "Even together the statements allow odd numbers below 20 that are prime (3, 5, 7, 11, 13, 17, 19) and some that are not (1, 9, 15). So the question cannot be answered. The trap is to treat 'odd' as if it meant 'prime'.",
   "दोनों कथन साथ मिलकर भी 20 से कम ऐसी विषम संख्याओं की अनुमति देते हैं जो अभाज्य हैं (3, 5, 7, 11, 13, 17, 19) और कुछ जो नहीं हैं (1, 9, 15)। अतः प्रश्न का उत्तर नहीं दिया जा सकता। जाल 'विषम' को 'अभाज्य' के अर्थ में ले लेना है।",
   "qa-ds-an-odd-number-below-20", _ds2)
