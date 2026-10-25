# -*- coding: utf-8 -*-
"""CSAT Level 4 · Simulator 2 -- Quantitative Aptitude (34 items: 32 in the Quant slots, 2 in the data-sufficiency block).

Layout B, the 2025 shape of the paper. Exam-level mix (6 easy / 16 medium / 12 hard), with none of the shapes of Levels
1-3 or Simulator 1: primes p, p + 10 and p + 14, what a remainder by 12 fixes, squares that end in 6, three-digit
numbers whose digits are in AP, a perfect number, 2^a × 3^b = 144, primes of the form 2^n - 1, a remainder of three
squares, a fraction and its reciprocal; a lorry slowed by its load, a speed that rises each hour, two cars 50 km apart
for the second time, a round trip into and with the wind; oil for a fuel mixture, a range after every number is
changed, the share of a school that plays chess, a cup moved each way between milk and water; oranges bought at two
rates and sold at a third, a price and a cost as fractions of a marked price, two years of growth; squares in an
arithmetic progression, the even terms of a Fibonacci sequence; letters in letter boxes, two pairs kept in order, two
squares of a chessboard that share a side; a cube from its surface area, posts round a square plot; wages with a fine
for absence, a pipe of a larger bore; the third Sunday of a month, ways to make ₹20 in coins, coins turned two at a
time; and two data-sufficiency items. Every key is worked out in code by check()."""
from fractions import Fraction as F
from itertools import combinations, permutations
import math
import csat_common as c
from csat_common import N, T, S2, DS, QA

def _ds(s1, s2, both):
    alone = (len(set(s1)) == 1, len(set(s2)) == 1)
    return "b" if all(alone) else "a" if any(alone) else "c" if len(set(both)) == 1 else "d"

isprime = lambda n: n > 1 and all(n % d for d in range(2, math.isqrt(n) + 1))

# ---------------------------------------------------------------- Number Theory (9)
def _nt1():
    ps = [p for p in range(2, 20000) if isprime(p) and isprime(p + 10) and isprime(p + 14)]
    assert ps == [3]
    return str(len(ps))
N(QA, "Number Theory", "hard",
  "For how many prime numbers p are p + 10 and p + 14 also both prime?",
  "कितनी अभाज्य संख्याओं p के लिए p + 10 और p + 14 दोनों भी अभाज्य हैं?",
  ["1", "2", "3", "Infinitely many"], 0,
  "Look at remainders on division by 3. If p leaves remainder 1, then p + 14 leaves 15, a multiple of 3; if p leaves remainder 2, then p + 10 leaves 12, a multiple of 3. Either way one of the two is divisible by 3 and, being larger than 3, is not prime. "
  "So p itself must be divisible by 3, that is, p = 3 -- and 13 and 17 are indeed prime. Only one such prime exists. 'Infinitely many' assumes that a pattern found once goes on; 2 and 3 have no basis.",
  "3 से भाग देने पर शेषफल देखिए। यदि p का शेष 1 है, तो p + 14 का शेष 15 है, जो 3 का गुणज है; यदि p का शेष 2 है, तो p + 10 का शेष 12 है, जो 3 का गुणज है। दोनों ही स्थितियों में दोनों में से एक 3 से विभाज्य है और, 3 से बड़ी होने के कारण, अभाज्य नहीं। "
  "अतः स्वयं p को 3 से विभाज्य होना चाहिए, यानी p = 3 -- और 13 और 17 सचमुच अभाज्य हैं। ऐसी केवल एक अभाज्य संख्या है। 'अनंत रूप से अनेक' मान लेता है कि एक बार मिला क्रम आगे चलता रहेगा; 2 और 3 का कोई आधार नहीं।",
  "qa-nt-primes-p-p-plus-10-and-p-plus-14", _nt1,
  opts_hi=["1", "2", "3", "अनंत रूप से अनेक"])

def _nt2():
    ns = range(7, 5000, 12)
    one = {n % 6 for n in ns} == {1}
    two = {n % 8 for n in ns} == {3}
    return c.T2[{(True, False): 0, (False, True): 1, (True, True): 2, (False, False): 3}[(one, two)]]
S2(QA, "Number Theory", "medium",
   "A whole number N leaves a remainder of 7 when divided by 12. Which of the following statements is/are always correct?",
   "एक पूर्ण संख्या N को 12 से भाग देने पर शेषफल 7 बचता है। निम्नलिखित में से कौन-सा/से कथन हमेशा सही है/हैं?",
   ["N leaves a remainder of 1 when divided by 6.", "N leaves a remainder of 3 when divided by 8."],
   ["N को 6 से भाग देने पर शेषफल 1 बचता है।", "N को 8 से भाग देने पर शेषफल 3 बचता है।"],
   0,
   "N = 12k + 7 = 6(2k + 1) + 1, so N always leaves remainder 1 on division by 6, since 6 divides 12 -- statement 1 is always correct. "
   "8 does not divide 12, so the remainder by 8 is not fixed: N = 7 leaves 7, N = 19 leaves 3, N = 31 leaves 7. Statement 2 holds for some N but not always.",
   "N = 12k + 7 = 6(2k + 1) + 1, इसलिए N को 6 से भाग देने पर हमेशा शेष 1 बचता है, क्योंकि 6, 12 को विभाजित करता है -- कथन 1 हमेशा सही है। "
   "8, 12 को विभाजित नहीं करता, इसलिए 8 से शेषफल तय नहीं: N = 7 पर शेष 7, N = 19 पर 3, N = 31 पर 7। कथन 2 कुछ N के लिए सही है पर हमेशा नहीं।",
   "qa-nt-what-a-remainder-by-12-fixes", check=_nt2)

def _nt3():
    return str(sum(1 for k in range(1, 32) if (k * k) % 10 == 6))
N(QA, "Number Theory", "medium",
  "How many perfect squares between 1 and 1,000 end in the digit 6?",
  "1 और 1,000 के बीच कितने पूर्ण वर्ग अंक 6 पर समाप्त होते हैं?",
  ["3", "4", "5", "6"], 3,
  "A square ends in 6 exactly when its root ends in 4 or 6 (4² = 16, 6² = 36). The roots run up to 31 (31² = 961, 32² = 1,024), so they are 4, 6, 14, 16, 24 and 26, giving 16, 36, 196, 256, 576 and 676 -- six squares. "
  "3 counts only the roots that end in 4; 4 and 5 drop some of the roots.",
  "कोई वर्ग ठीक तब 6 पर समाप्त होता है जब उसका मूल 4 या 6 पर समाप्त हो (4² = 16, 6² = 36)। मूल 31 तक जाते हैं (31² = 961, 32² = 1,024), इसलिए वे 4, 6, 14, 16, 24 और 26 हैं, जिनसे 16, 36, 196, 256, 576 और 676 -- छह वर्ग मिलते हैं। "
  "3 केवल 4 पर समाप्त होने वाले मूल गिनता है; 4 और 5 कुछ मूल छोड़ देते हैं।",
  "qa-nt-squares-that-end-in-6", _nt3)

def _nt4():
    ap = [n for n in range(100, 1000) if n // 100 + n % 10 == 2 * (n // 10 % 10)]
    same = [n for n in ap if len(set(str(n))) == 1]
    up = [n for n in ap if n // 100 < n % 10]
    assert (len(same), len(up), len(ap) - len(same) - len(up)) == (9, 16, 20)
    return str(len(ap))
N(QA, "Number Theory", "hard",
  "How many three-digit numbers have digits that form an arithmetic progression when read from left to right (for example 135, 975 and 444)?",
  "तीन अंकों की कितनी संख्याओं के अंक बाएँ से दाएँ पढ़ने पर समांतर श्रेणी बनाते हैं (उदाहरण के लिए 135, 975 और 444)?",
  ["25", "36", "41", "45"], 3,
  "Write the digits as b - d, b, b + d. With d = 0 there are 9 numbers (111 to 999). Rising digits (first digit at least 1): d = 1 gives 7 (123 to 789), d = 2 gives 5, d = 3 gives 3 and d = 4 gives 1 -- 16 in all. Falling digits may end in 0: d = 1 gives 8 (210 to 987), d = 2 gives 6, d = 3 gives 4 and d = 4 gives 2 -- 20 in all. "
  "So 9 + 16 + 20 = 45. 36 leaves out the equal-digit numbers; 25 leaves out the falling ones; 41 counts the falling numbers as if, like the rising ones, they could not end in 0.",
  "अंकों को b - d, b, b + d लिखिए। d = 0 पर 9 संख्याएँ हैं (111 से 999)। बढ़ते अंक (पहला अंक कम से कम 1): d = 1 से 7 (123 से 789), d = 2 से 5, d = 3 से 3 और d = 4 से 1 -- कुल 16। घटते अंक 0 पर समाप्त हो सकते हैं: d = 1 से 8 (210 से 987), d = 2 से 6, d = 3 से 4 और d = 4 से 2 -- कुल 20। "
  "अतः 9 + 16 + 20 = 45। 36 समान अंकों वाली संख्याएँ छोड़ देता है; 25 घटते अंकों वाली छोड़ देता है; 41 घटते अंकों वाली संख्याओं को ऐसे गिनता है मानो वे भी बढ़ते अंकों वाली की तरह 0 पर समाप्त न हो सकें।",
  "qa-nt-three-digit-numbers-whose-digits-are-in-ap", _nt4)

def _nt5():
    perfect = [n for n in (12, 18, 28, 36) if sum(d for d in range(1, n) if n % d == 0) == n]
    assert perfect == [28]
    return str(perfect[0])
N(QA, "Number Theory", "easy",
  "A number is called perfect if it equals the sum of all its divisors other than itself (6 is perfect, since 1 + 2 + 3 = 6). Which one of the following numbers is perfect?",
  "किसी संख्या को पूर्ण (परफ़ेक्ट) कहते हैं यदि वह अपने अलावा अपने सभी भाजकों के योग के बराबर हो (6 पूर्ण है, क्योंकि 1 + 2 + 3 = 6)। निम्नलिखित में से कौन-सी संख्या पूर्ण है?",
  ["12", "18", "28", "36"], 2,
  "The divisors of 28 other than itself are 1, 2, 4, 7 and 14, which add up to 28. For 12 they add up to 1 + 2 + 3 + 4 + 6 = 16; for 18 to 1 + 2 + 3 + 6 + 9 = 21; for 36 to 55 -- each more than the number.",
  "28 के अपने अलावा भाजक 1, 2, 4, 7 और 14 हैं, जिनका योग 28 है। 12 के लिए योग 1 + 2 + 3 + 4 + 6 = 16 है; 18 के लिए 1 + 2 + 3 + 6 + 9 = 21; 36 के लिए 55 -- हर बार संख्या से अधिक।",
  "qa-nt-a-perfect-number", _nt5)

def _nt6():
    sols = [(a, b) for a in range(12) for b in range(12) if 2 ** a * 3 ** b == 144]
    assert sols == [(4, 2)]
    return str(sum(sols[0]))
N(QA, "Number Theory", "easy",
  "If a and b are whole numbers and 2ᵃ × 3ᵇ = 144, what is a + b?",
  "यदि a और b पूर्ण संख्याएँ हैं और 2ᵃ × 3ᵇ = 144, तो a + b क्या है?",
  ["6", "8", "12", "16"], 0,
  "144 = 16 × 9 = 2⁴ × 3², and a number has only one factorisation into primes, so a = 4 and b = 2, and a + b = 6. 8 is a × b; 12 is the square root of 144; 16 is 2⁴ itself.",
  "144 = 16 × 9 = 2⁴ × 3², और किसी संख्या का अभाज्य गुणनखंडन एक ही होता है, इसलिए a = 4 और b = 2, और a + b = 6। 8, a × b है; 12, 144 का वर्गमूल है; 16 स्वयं 2⁴ है।",
  "qa-nt-2-to-the-a-times-3-to-the-b-is-144", _nt6)

def _nt7():
    ns = [n for n in range(2, 13) if isprime(2 ** n - 1)]
    assert ns == [2, 3, 5, 7] and not isprime(2 ** 11 - 1)
    return str(len(ns))
N(QA, "Number Theory", "hard",
  "For how many whole numbers n from 2 to 12 is 2ⁿ - 1 a prime number?",
  "2 से 12 तक की कितनी पूर्ण संख्याओं n के लिए 2ⁿ - 1 एक अभाज्य संख्या है?",
  ["3", "4", "5", "6"], 1,
  "If n is composite, 2ⁿ - 1 factorises (for example 2⁶ - 1 = 63 = 7 × 9, divisible by 2² - 1 and 2³ - 1), so only prime n can work: n = 2, 3, 5, 7 and 11. These give 3, 7, 31, 127 and 2,047 -- but 2,047 = 23 × 89. So only four values of n work. "
  "5 assumes that every prime n gives a prime, which 11 disproves; 3 and 6 miscount.",
  "यदि n भाज्य है, तो 2ⁿ - 1 के गुणनखंड होते हैं (जैसे 2⁶ - 1 = 63 = 7 × 9, जो 2² - 1 और 2³ - 1 से विभाज्य है), इसलिए केवल अभाज्य n काम कर सकते हैं: n = 2, 3, 5, 7 और 11। इनसे 3, 7, 31, 127 और 2,047 मिलते हैं -- पर 2,047 = 23 × 89। अतः केवल चार n काम करते हैं। "
  "5 मान लेता है कि हर अभाज्य n से अभाज्य संख्या मिलती है, जिसे 11 ग़लत सिद्ध करता है; 3 और 6 ग़लत गिनते हैं।",
  "qa-nt-primes-of-the-form-2-to-the-n-minus-1", _nt7)

def _nt8():
    return str((19 ** 2 + 21 ** 2 + 23 ** 2) % 20)
N(QA, "Number Theory", "medium",
  "What is the remainder when 19² + 21² + 23² is divided by 20?",
  "19² + 21² + 23² को 20 से भाग देने पर शेषफल क्या है?",
  ["1", "9", "11", "19"], 2,
  "Measure each number from 20: 19 = 20 - 1, 21 = 20 + 1 and 23 = 20 + 3, so their squares leave the same remainders by 20 as (-1)² = 1, 1² = 1 and 3² = 9. The total leaves 1 + 1 + 9 = 11. (Directly: 361 + 441 + 529 = 1,331 = 66 × 20 + 11.) "
  "9 keeps only the last square; 1 and 19 slip in the signs.",
  "हर संख्या को 20 से नापिए: 19 = 20 - 1, 21 = 20 + 1 और 23 = 20 + 3, इसलिए उनके वर्ग 20 से भाग देने पर वही शेष छोड़ते हैं जो (-1)² = 1, 1² = 1 और 3² = 9। योग का शेष 1 + 1 + 9 = 11 है। (सीधे: 361 + 441 + 529 = 1,331 = 66 × 20 + 11।) "
  "9 केवल अंतिम वर्ग रखता है; 1 और 19 चिह्नों में चूकते हैं।",
  "qa-nt-a-remainder-of-three-squares", _nt8)

def _nt9():
    xs = {F(a, b) for b in range(1, 30) for a in range(1, b) if F(a, b) + F(b, a) == F(25, 12)}
    assert xs == {F(3, 4)}
    x = xs.pop()
    return f"{x.numerator}/{x.denominator}"
N(QA, "Number Theory", "medium",
  "The sum of a fraction less than 1 and its reciprocal is 2 1/12. What is the fraction?",
  "1 से छोटे एक भिन्न और उसके व्युत्क्रम का योग 2 1/12 है। वह भिन्न क्या है?",
  ["2/3", "3/4", "4/5", "5/6"], 1,
  "With the fraction x, x + 1/x = 25/12, so 12x² - 25x + 12 = 0, that is (3x - 4)(4x - 3) = 0. The root less than 1 is x = 3/4 (check: 3/4 + 4/3 = 9/12 + 16/12 = 25/12). "
  "2/3 + 3/2 = 2 1/6; 4/5 + 5/4 = 2 1/20; 5/6 + 6/5 = 2 1/30.",
  "भिन्न x लेने पर x + 1/x = 25/12, इसलिए 12x² - 25x + 12 = 0, यानी (3x - 4)(4x - 3) = 0। 1 से छोटा मूल x = 3/4 है (जाँच: 3/4 + 4/3 = 9/12 + 16/12 = 25/12)। "
  "2/3 + 3/2 = 2 1/6; 4/5 + 5/4 = 2 1/20; 5/6 + 6/5 = 2 1/30।",
  "qa-nt-a-fraction-and-its-reciprocal", _nt9)

# ---------------------------------------------------------------- Speed-Distance-Time (4)
def _sdt1():
    load = F(60 - 100 // 2, 4)
    return f"{float(load):g} tonnes"
N(QA, "Speed-Distance-Time", "medium",
  "An empty lorry runs at 60 km/h, and its speed falls by 4 km/h for every tonne of load it carries. With what load does it take exactly 2 hours to cover 100 km?",
  "एक ख़ाली लॉरी 60 किमी/घंटा से चलती है, और वह जितने टन माल ढोती है उसके हर टन पर उसकी चाल 4 किमी/घंटा घट जाती है। कितने माल के साथ उसे 100 किमी तय करने में ठीक 2 घंटे लगते हैं?",
  ["2 tonnes", "2.5 tonnes", "4 tonnes", "10 tonnes"], 1,
  "100 km in 2 hours is 50 km/h, which is 10 km/h below the empty speed. At 4 km/h for each tonne, that is 10 ÷ 4 = 2.5 tonnes. "
  "10 tonnes takes the fall in speed itself as the load; 2 tonnes and 4 tonnes give speeds of 52 and 44 km/h.",
  "100 किमी 2 घंटे में 50 किमी/घंटा है, जो ख़ाली चाल से 10 किमी/घंटा कम है। हर टन पर 4 किमी/घंटा से यह 10 ÷ 4 = 2.5 टन है। "
  "10 टन चाल की कमी को ही माल मान लेता है; 2 टन और 4 टन से चालें 52 और 44 किमी/घंटा होतीं।",
  "qa-sdt-a-lorry-slowed-by-its-load", _sdt1,
  opts_hi=["2 टन", "2.5 टन", "4 टन", "10 टन"])

def _sdt2():
    return f"{sum(40 + 2 * k for k in range(5))} km"
N(QA, "Speed-Distance-Time", "easy",
  "A car travels at 40 km/h for the first hour, and its speed goes up by 2 km/h at the start of each later hour. How far does it travel in 5 hours?",
  "एक गाड़ी पहले घंटे में 40 किमी/घंटा से चलती है, और हर अगले घंटे की शुरुआत में उसकी चाल 2 किमी/घंटा बढ़ जाती है। 5 घंटों में वह कितनी दूरी तय करती है?",
  ["200 km", "208 km", "210 km", "220 km"], 3,
  "The speeds in the five hours are 40, 42, 44, 46 and 48 km/h, so the distance is 40 + 42 + 44 + 46 + 48 = 220 km (five hours at the average speed, 44 km/h). "
  "200 km ignores the rise; 210 km takes 42 km/h, the speed of the second hour, as the average; 208 km has no basis.",
  "पाँच घंटों की चालें 40, 42, 44, 46 और 48 किमी/घंटा हैं, इसलिए दूरी 40 + 42 + 44 + 46 + 48 = 220 किमी है (औसत चाल, 44 किमी/घंटा, से पाँच घंटे)। "
  "200 किमी वृद्धि को अनदेखा करता है; 210 किमी दूसरे घंटे की चाल, 42 किमी/घंटा, को औसत मान लेता है; 208 किमी का कोई आधार नहीं।",
  "qa-sdt-a-speed-that-rises-each-hour", _sdt2,
  opts_hi=["200 किमी", "208 किमी", "210 किमी", "220 किमी"])

def _sdt3():
    t = F(360 + 50, 45 + 75)
    mins = int(t * 60)
    assert mins == 205 and F(360 - 50, 120) * 60 == 155
    h, m = 9 + mins // 60, mins % 60
    return f"{h}:{m:02d} p.m."
N(QA, "Speed-Distance-Time", "hard",
  "Two cars start at 9:00 a.m. from towns 360 km apart and drive towards each other along the same road, one at 45 km/h and the other at 75 km/h. At what time are they 50 km apart for the second time?",
  "दो गाड़ियाँ सुबह 9:00 बजे 360 किमी दूर स्थित नगरों से चलकर एक ही सड़क पर एक-दूसरे की ओर जाती हैं, एक 45 किमी/घंटा से और दूसरी 75 किमी/घंटा से। वे दूसरी बार किस समय 50 किमी दूर होंगी?",
  ["11:35 a.m.", "12:00 noon", "12:25 p.m.", "12:50 p.m."], 2,
  "They close the gap at 45 + 75 = 120 km/h. They are 50 km apart first when they have covered 310 km together, after 2 hours 35 minutes (11:35 a.m.); they meet after 3 hours (12:00 noon); and they are 50 km apart again when the combined distance is 410 km, after 3 hours 25 minutes -- 12:25 p.m. "
  "11:35 a.m. is the first time, before they meet; 12:00 noon is when they meet; 12:50 p.m. is 100 km after meeting.",
  "वे 45 + 75 = 120 किमी/घंटा से दूरी घटाती हैं। वे पहली बार 50 किमी दूर तब होती हैं जब मिलकर 310 किमी चल चुकी हों, 2 घंटे 35 मिनट बाद (सुबह 11:35); वे 3 घंटे बाद मिलती हैं (दोपहर 12:00); और फिर 50 किमी दूर तब होती हैं जब कुल दूरी 410 किमी हो, 3 घंटे 25 मिनट बाद -- दोपहर 12:25। "
  "सुबह 11:35 पहली बार है, मिलने से पहले; दोपहर 12:00 मिलने का समय है; दोपहर 12:50 मिलने के बाद 100 किमी है।",
  "qa-sdt-two-cars-50-km-apart-for-the-second-time", _sdt3,
  opts_hi=["सुबह 11:35", "दोपहर 12:00", "दोपहर 12:25", "दोपहर 12:50"])

def _sdt4():
    t = F(30, 50 - 10) + F(30, 50 + 10)
    assert t == F(5, 4) and F(60, 50) == F(6, 5)
    return "1 hour 15 minutes"
N(QA, "Speed-Distance-Time", "medium",
  "A drone flies at 50 km/h in still air. It flies 30 km straight into a 10 km/h wind and then 30 km straight back with the wind behind it. How long does the round trip take?",
  "एक ड्रोन शांत हवा में 50 किमी/घंटा से उड़ता है। वह 10 किमी/घंटा की हवा के ठीक विरुद्ध 30 किमी उड़ता है और फिर हवा को पीछे रखकर 30 किमी सीधे लौटता है। आने-जाने की पूरी यात्रा में कितना समय लगता है?",
  ["1 hour 6 minutes", "1 hour 10 minutes", "1 hour 12 minutes", "1 hour 15 minutes"], 3,
  "Into the wind it flies at 40 km/h, taking 45 minutes; with the wind at 60 km/h, taking 30 minutes: 1 hour 15 minutes in all. "
  "1 hour 12 minutes assumes that the wind's help on the way back cancels its hindrance on the way out (60 km at 50 km/h); it does not, because more time is spent flying slowly. The other two have no basis.",
  "हवा के विरुद्ध वह 40 किमी/घंटा से उड़ता है, 45 मिनट लगते हैं; हवा के साथ 60 किमी/घंटा से, 30 मिनट: कुल 1 घंटा 15 मिनट। "
  "1 घंटा 12 मिनट मान लेता है कि लौटते समय हवा की सहायता जाते समय की बाधा को काट देती है (60 किमी, 50 किमी/घंटा से); ऐसा नहीं होता, क्योंकि धीमी उड़ान में अधिक समय बीतता है। बाक़ी दो का कोई आधार नहीं।",
  "qa-sdt-a-round-trip-into-and-with-the-wind", _sdt4,
  opts_hi=["1 घंटा 6 मिनट", "1 घंटा 10 मिनट", "1 घंटा 12 मिनट", "1 घंटा 15 मिनट"])

# ---------------------------------------------------------------- Ratio, Mixtures & Alligation (4)
def _rm1():
    return f"{float(F(13, 26)):g} litre"
N(QA, "Ratio, Mixtures & Alligation", "easy",
  "A two-stroke engine runs on a mixture of petrol and oil in the ratio 25 : 1. How much oil is there in 13 litres of the mixture?",
  "एक टू-स्ट्रोक इंजन पेट्रोल और तेल के 25 : 1 के अनुपात वाले मिश्रण पर चलता है। मिश्रण के 13 लीटर में कितना तेल है?",
  ["0.4 litre", "0.5 litre", "0.52 litre", "1 litre"], 1,
  "The mixture has 25 + 1 = 26 parts, of which 1 is oil, so 13 litres hold 13/26 = 0.5 litre of oil. 0.52 litre divides 13 by 25, treating the ratio as oil to mixture; 1 litre and 0.4 litre have no basis.",
  "मिश्रण में 25 + 1 = 26 भाग हैं, जिनमें 1 तेल है, इसलिए 13 लीटर में 13/26 = 0.5 लीटर तेल है। 0.52 लीटर, 13 को 25 से भाग देता है, अनुपात को तेल और मिश्रण का मानकर; 1 लीटर और 0.4 लीटर का कोई आधार नहीं।",
  "qa-rm-oil-for-a-fuel-mixture", _rm1,
  opts_hi=["0.4 लीटर", "0.5 लीटर", "0.52 लीटर", "1 लीटर"])

def _rm2():
    xs = [3, 7, 10, 15, 23]                    # any list with range 20
    ys = [2 * x + 5 for x in xs]
    assert max(xs) - min(xs) == 20
    return str(max(ys) - min(ys))
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "The range (largest minus smallest) of a set of ten numbers is 20. Every number in the set is doubled and then increased by 5. What is the range of the new set?",
  "दस संख्याओं के एक समूह का परिसर (सबसे बड़ी घटा सबसे छोटी) 20 है। समूह की हर संख्या को दोगुना करके फिर 5 बढ़ाया जाता है। नए समूह का परिसर क्या है?",
  ["20", "25", "40", "45"], 2,
  "The largest and smallest numbers are both doubled and both increased by 5, so their difference doubles and the added 5s cancel: 2 × 20 = 40. "
  "45 adds the 5 to the range as well; 25 adds it without doubling; 20 assumes the range does not change.",
  "सबसे बड़ी और सबसे छोटी दोनों संख्याएँ दोगुनी होती हैं और दोनों में 5 जुड़ता है, इसलिए उनका अंतर दोगुना होता है और जोड़े गए 5 कट जाते हैं: 2 × 20 = 40। "
  "45 परिसर में भी 5 जोड़ देता है; 25 दोगुना किए बिना 5 जोड़ता है; 20 मान लेता है कि परिसर नहीं बदलता।",
  "qa-rm-a-range-after-every-number-is-changed", _rm2)

def _rm3():
    f = (F(1, 3) * 3 + F(1, 2) * 2) / 5
    return f"{f.numerator}/{f.denominator}"
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "In a school the ratio of boys to girls is 3 : 2. One-third of the boys and one-half of the girls play chess. What fraction of all the pupils play chess?",
  "एक विद्यालय में लड़कों और लड़कियों का अनुपात 3 : 2 है। एक-तिहाई लड़के और आधी लड़कियाँ शतरंज खेलती हैं। सभी विद्यार्थियों का कितना भाग शतरंज खेलता है?",
  ["1/3", "2/5", "5/12", "5/6"], 1,
  "Take 3 boys and 2 girls for every 5 pupils: 1/3 of 3 is 1 boy and 1/2 of 2 is 1 girl, so 2 of every 5 pupils play -- 2/5. "
  "5/12 is the simple average of 1/3 and 1/2, which ignores that boys outnumber girls; 5/6 adds the two fractions; 1/3 takes the boys' share alone.",
  "हर 5 विद्यार्थियों में 3 लड़के और 2 लड़कियाँ लीजिए: 3 का 1/3, 1 लड़का और 2 का 1/2, 1 लड़की, इसलिए हर 5 में से 2 खेलते हैं -- 2/5। "
  "5/12, 1/3 और 1/2 का साधारण औसत है, जो इसकी अनदेखी करता है कि लड़के लड़कियों से अधिक हैं; 5/6 दोनों भिन्नों को जोड़ता है; 1/3 केवल लड़कों का भाग लेता है।",
  "qa-rm-the-share-of-a-school-that-plays-chess", _rm3)

def _rm4():
    milk, water, cup = F(100), F(100), F(10)          # two jugs and a cup, in any units
    jug_w = {"m": cup, "w": water}                    # a cup of milk poured into the water jug
    take = cup / (jug_w["m"] + jug_w["w"])
    back_m, back_w = jug_w["m"] * take, jug_w["w"] * take
    milk_in_water = jug_w["m"] - back_m
    water_in_milk = back_w
    assert milk_in_water == water_in_milk
    return "The same amount each way"
T(QA, "Ratio, Mixtures & Alligation", "hard",
  "One jug holds milk and another holds the same amount of water. A cup of milk is poured from the first jug into the water and stirred, and then a cup of the mixture is poured back into the milk jug. Is there now more milk in the water jug, or more water in the milk jug?",
  "एक जग में दूध है और दूसरे में उतना ही पानी। पहले जग से एक कप दूध पानी में डालकर हिलाया जाता है, और फिर मिश्रण का एक कप वापस दूध वाले जग में डाला जाता है। अब पानी वाले जग में दूध अधिक है, या दूध वाले जग में पानी?",
  ["The same amount each way", "More milk in the water jug", "More water in the milk jug",
   "It depends on how thoroughly the water jug was stirred"],
  ["दोनों ओर बराबर मात्रा", "पानी वाले जग में दूध अधिक", "दूध वाले जग में पानी अधिक",
   "यह इस पर निर्भर है कि पानी वाले जग को कितनी अच्छी तरह हिलाया गया"],
  0,
  "After the two pourings each jug holds exactly what it started with, one cup having gone each way. Whatever milk is missing from the milk jug must be sitting in the water jug, and the space it left in the milk jug has been filled by exactly that amount of water. So the milk in the water jug equals the water in the milk jug. "
  "This holds however well the mixture was stirred, which only changes how much of each is carried back; the two 'more' answers overlook that the volumes balance.",
  "दोनों बार डालने के बाद हर जग में ठीक उतना ही है जितना आरंभ में था, क्योंकि एक-एक कप दोनों ओर गया। दूध वाले जग से जितना दूध कम है वह पानी वाले जग में होना ही चाहिए, और उससे दूध वाले जग में बनी जगह ठीक उतने ही पानी से भरी है। अतः पानी वाले जग का दूध दूध वाले जग के पानी के बराबर है। "
  "यह इस पर निर्भर नहीं कि मिश्रण कितनी अच्छी तरह हिलाया गया, जिससे केवल यह बदलता है कि हर एक का कितना भाग वापस जाता है; 'अधिक' वाले दोनों उत्तर इसे अनदेखा करते हैं कि मात्राएँ संतुलित रहती हैं।",
  "qa-rm-a-cup-moved-each-way-between-milk-and-water", pos=2, check=_rm4)

# ---------------------------------------------------------------- Percentage & Profit-Loss (3)
def _pp1():
    cost = (F(10, 4) + F(10, 6)) / 2
    r = (F(10, 5) - cost) / cost * 100
    assert r == -4
    return "4 per cent loss"
N(QA, "Percentage & Profit-Loss", "hard",
  "A fruit seller buys a number of oranges at 4 for ₹10 and the same number at 6 for ₹10. He sells all of them at 5 for ₹10. What is his profit or loss per cent?",
  "एक फल-विक्रेता कुछ संतरे 4 के ₹10 की दर से और उतने ही संतरे 6 के ₹10 की दर से ख़रीदता है। वह सभी को 5 के ₹10 की दर से बेचता है। उसका लाभ या हानि प्रतिशत क्या है?",
  ["4 per cent loss", "No profit, no loss", "4 per cent profit", "8 per cent profit"], 0,
  "Buy 12 of each: 12 at 4 for ₹10 cost ₹30, and 12 at 6 for ₹10 cost ₹20, so 24 oranges cost ₹50. Sold at 5 for ₹10 (₹2 each), they fetch ₹48 -- a loss of ₹2 on ₹50, that is 4 per cent. "
  "'No profit, no loss' assumes that the selling rate of 5, halfway between 4 and 6, is also the average cost; but the average cost per orange is (2.50 + 1.67)/2, about ₹2.08, above ₹2.",
  "हर एक के 12 ख़रीदिए: 4 के ₹10 पर 12 के ₹30, और 6 के ₹10 पर 12 के ₹20, इसलिए 24 संतरों की लागत ₹50। 5 के ₹10 (₹2 प्रति संतरा) पर बेचने से ₹48 मिलते हैं -- ₹50 पर ₹2 की हानि, यानी 4 प्रतिशत। "
  "'न लाभ न हानि' मान लेता है कि 4 और 6 के बीचों-बीच 5 की बिक्री दर औसत लागत भी है; पर प्रति संतरा औसत लागत (2.50 + 1.67)/2, लगभग ₹2.08 है, जो ₹2 से अधिक है।",
  "qa-pp-oranges-bought-at-two-rates-sold-at-a-third", _pp1,
  opts_hi=["4 प्रतिशत हानि", "न लाभ न हानि", "4 प्रतिशत लाभ", "8 प्रतिशत लाभ"])

def _pp2():
    r = (F(4, 5) - F(2, 3)) / F(2, 3) * 100
    assert r == 20
    return "20 per cent"
N(QA, "Percentage & Profit-Loss", "medium",
  "An article is sold for four-fifths of its marked price, and its cost is two-thirds of the marked price. What is the profit per cent on the cost?",
  "एक वस्तु अपने अंकित मूल्य के चार-पाँचवें भाग पर बेची जाती है, और उसकी लागत अंकित मूल्य का दो-तिहाई है। लागत पर लाभ प्रतिशत क्या है?",
  ["10 per cent", "13⅓ per cent", "20 per cent", "25 per cent"], 2,
  "Take the marked price as 15: the article sells for 12 and costs 10, a profit of 2 on 10 -- 20 per cent. "
  "13⅓ per cent measures the profit (2) against the marked price (15) instead of the cost; 25 per cent and 10 per cent have no basis.",
  "अंकित मूल्य 15 मानिए: वस्तु 12 में बिकती है और उसकी लागत 10 है, 10 पर 2 का लाभ -- 20 प्रतिशत। "
  "13⅓ प्रतिशत लाभ (2) को लागत के बजाय अंकित मूल्य (15) से नापता है; 25 और 10 प्रतिशत का कोई आधार नहीं।",
  "qa-pp-a-price-and-a-cost-as-fractions-of-a-marked-price", _pp2,
  opts_hi=["10 प्रतिशत", "13⅓ प्रतिशत", "20 प्रतिशत", "25 प्रतिशत"])

def _pp3():
    g = (F(105, 100) * F(106, 100) - 1) * 100
    return f"{float(g):g} per cent"
N(QA, "Percentage & Profit-Loss", "easy",
  "An economy grows by 5 per cent in one year and by 6 per cent in the next. By what percentage is it larger at the end of the two years than at the start?",
  "एक अर्थव्यवस्था एक वर्ष में 5 प्रतिशत और अगले वर्ष 6 प्रतिशत बढ़ती है। दो वर्षों के अंत में वह आरंभ की तुलना में कितने प्रतिशत बड़ी है?",
  ["11 per cent", "11.3 per cent", "11.5 per cent", "12 per cent"], 1,
  "Growth compounds: 1.05 × 1.06 = 1.113, an increase of 11.3 per cent. 11 per cent simply adds the two rates, forgetting that the second year's 6 per cent is earned on an already larger economy; 11.5 and 12 per cent have no basis.",
  "वृद्धि चक्रवृद्धि होती है: 1.05 × 1.06 = 1.113, यानी 11.3 प्रतिशत की वृद्धि। 11 प्रतिशत केवल दोनों दरों को जोड़ता है, यह भूलकर कि दूसरे वर्ष के 6 प्रतिशत पहले से बड़ी अर्थव्यवस्था पर लगते हैं; 11.5 और 12 प्रतिशत का कोई आधार नहीं।",
  "qa-pp-two-years-of-growth", _pp3,
  opts_hi=["11 प्रतिशत", "11.3 प्रतिशत", "11.5 प्रतिशत", "12 प्रतिशत"])

# ---------------------------------------------------------------- Sequences & Series (2)
def _ss1():
    terms = [7 + 5 * k for k in range(100)]
    squares = [t for t in terms if math.isqrt(t) ** 2 == t]
    assert {k * k % 5 for k in range(5)} == {0, 1, 4}
    return str(len(squares))
N(QA, "Sequences & Series", "hard",
  "How many of the first 100 terms of the arithmetic progression 7, 12, 17, 22, ... are perfect squares?",
  "समांतर श्रेणी 7, 12, 17, 22, ... के पहले 100 पदों में से कितने पूर्ण वर्ग हैं?",
  ["0", "1", "5", "10"], 0,
  "Every term leaves remainder 2 on division by 5 (7, 12, 17, ... are 5k + 2). But a perfect square can leave only 0, 1 or 4 on division by 5, since 0², 1², 2², 3² and 4² leave 0, 1, 4, 4 and 1. So no term of the progression, however far it runs, is a square. "
  "1, 5 and 10 assume that squares turn up now and then, as they do in most progressions.",
  "हर पद को 5 से भाग देने पर शेष 2 बचता है (7, 12, 17, ... = 5k + 2)। पर कोई पूर्ण वर्ग 5 से भाग देने पर केवल 0, 1 या 4 छोड़ सकता है, क्योंकि 0², 1², 2², 3² और 4² के शेष 0, 1, 4, 4 और 1 हैं। अतः श्रेणी का कोई भी पद, वह कितनी भी दूर तक चले, वर्ग नहीं है। "
  "1, 5 और 10 मान लेते हैं कि वर्ग बीच-बीच में आते रहेंगे, जैसा अधिकांश श्रेणियों में होता है।",
  "qa-ss-squares-in-an-arithmetic-progression", _ss1)

def _ss2():
    f = [1, 1]
    while len(f) < 30:
        f.append(f[-1] + f[-2])
    return str(sum(1 for x in f if x % 2 == 0))
N(QA, "Sequences & Series", "medium",
  "In the sequence 1, 1, 2, 3, 5, 8, 13, ..., each term after the first two is the sum of the two before it. How many of the first 30 terms are even?",
  "अनुक्रम 1, 1, 2, 3, 5, 8, 13, ... में पहले दो के बाद हर पद अपने से पहले के दो पदों का योग है। पहले 30 पदों में से कितने सम हैं?",
  ["9", "10", "15", "20"], 1,
  "Track only odd (O) and even (E): O, O, E, O, O, E, ... -- odd + odd is even, odd + even is odd, even + odd is odd, and the pattern repeats every three terms. So every third term is even: the 3rd, 6th, ..., 30th, which is 10 terms. "
  "15 assumes every other term is even; 20 takes two terms in every three as even; 9 stops at the 27th term.",
  "केवल विषम (O) और सम (E) देखिए: O, O, E, O, O, E, ... -- विषम + विषम सम है, विषम + सम विषम, सम + विषम विषम, और क्रम हर तीन पदों पर दोहराता है। अतः हर तीसरा पद सम है: तीसरा, छठा, ..., तीसवाँ, यानी 10 पद। "
  "15 मान लेता है कि हर दूसरा पद सम है; 20 हर तीन में से दो पदों को सम मानता है; 9, 27वें पद पर रुक जाता है।",
  "qa-ss-the-even-terms-of-a-fibonacci-sequence", _ss2)

# ---------------------------------------------------------------- Permutation & Combination (3)
def _pc1():
    return str(3 ** 4)
N(QA, "Permutation & Combination", "medium",
  "In how many ways can 4 different letters be posted in 3 letter boxes, if any box may receive any number of letters?",
  "4 अलग-अलग पत्रों को 3 लेटर-बॉक्सों में कितने तरीक़ों से डाला जा सकता है, यदि किसी भी बॉक्स में कितने भी पत्र डाले जा सकते हैं?",
  ["12", "64", "81", "243"], 2,
  "Each of the 4 letters can go into any of the 3 boxes, independently of the others: 3 × 3 × 3 × 3 = 3⁴ = 81. "
  "64 = 4³ reverses the roles, choosing a letter for each box; 12 = 4 × 3 counts one letter and one box; 243 = 3⁵ counts one letter too many.",
  "4 में से हर पत्र 3 में से किसी भी बॉक्स में, दूसरों से स्वतंत्र रूप से, जा सकता है: 3 × 3 × 3 × 3 = 3⁴ = 81। "
  "64 = 4³ भूमिकाएँ उलट देता है, हर बॉक्स के लिए एक पत्र चुनकर; 12 = 4 × 3 एक पत्र और एक बॉक्स गिनता है; 243 = 3⁵ एक पत्र अधिक गिनता है।",
  "qa-pc-letters-in-letter-boxes", _pc1)

def _pc2():
    return str(sum(1 for p in permutations("ABCDEF") if p.index("A") < p.index("B") and p.index("C") < p.index("D")))
N(QA, "Permutation & Combination", "hard",
  "Six people, A, B, C, D, E and F, stand in a queue. In how many orders can they stand if A must be somewhere ahead of B and C somewhere ahead of D (not necessarily next to them)?",
  "छह लोग, A, B, C, D, E और F, एक पंक्ति में खड़े हैं। वे कितने क्रमों में खड़े हो सकते हैं यदि A को B से कहीं आगे और C को D से कहीं आगे होना हो (आवश्यक नहीं कि ठीक बग़ल में)?",
  ["45", "90", "120", "180"], 3,
  "Of the 6! = 720 orders, exactly half have A ahead of B, and among those exactly half have C ahead of D, since the two conditions are independent and each order of a pair is equally likely: 720 ÷ 2 ÷ 2 = 180. "
  "90 divides by 8, as though there were three such conditions; 45 divides by 16; 120 = 5! treats the people as if one of them were removed.",
  "6! = 720 क्रमों में से ठीक आधे में A, B से आगे है, और उनमें से ठीक आधे में C, D से आगे, क्योंकि दोनों शर्तें स्वतंत्र हैं और किसी जोड़े के दोनों क्रम समान रूप से संभव हैं: 720 ÷ 2 ÷ 2 = 180। "
  "90, 8 से भाग देता है, मानो ऐसी तीन शर्तें हों; 45, 16 से भाग देता है; 120 = 5! ऐसे गिनता है मानो एक व्यक्ति हटा दिया गया हो।",
  "qa-pc-two-pairs-kept-in-order", _pc2)

def _pc3():
    cells = [(r, c_) for r in range(8) for c_ in range(8)]
    return str(sum(1 for (r1, c1), (r2, c2) in combinations(cells, 2) if abs(r1 - r2) + abs(c1 - c2) == 1))
N(QA, "Permutation & Combination", "hard",
  "In how many ways can two squares that share a side be chosen from an ordinary 8 × 8 chessboard?",
  "एक सामान्य 8 × 8 शतरंज-पट से एक भुजा साझा करने वाले दो वर्ग कितने तरीक़ों से चुने जा सकते हैं?",
  ["56", "64", "112", "128"], 2,
  "In each of the 8 rows, neighbouring squares form 7 side-by-side pairs, giving 8 × 7 = 56 pairs; in each of the 8 columns another 7 pairs one above the other, giving 56 more. In all 112. "
  "56 counts only the pairs in rows (or only in columns); 64 is the number of squares; 128 counts 8 pairs per row and column.",
  "8 पंक्तियों में से हर एक में पास-पास के वर्ग 7 जोड़े बनाते हैं, जिससे 8 × 7 = 56 जोड़े मिलते हैं; 8 स्तंभों में से हर एक में और 7 जोड़े ऊपर-नीचे, जिससे 56 और। कुल 112। "
  "56 केवल पंक्तियों के (या केवल स्तंभों के) जोड़े गिनता है; 64 वर्गों की संख्या है; 128 हर पंक्ति और स्तंभ में 8 जोड़े गिनता है।",
  "qa-pc-two-squares-of-a-chessboard-that-share-a-side", _pc3)

# ---------------------------------------------------------------- Geometry & Mensuration (2)
def _gm1():
    side = math.isqrt(150 // 6)
    assert 6 * side * side == 150
    return f"{side ** 3} cm³"
N(QA, "Geometry & Mensuration", "medium",
  "The total surface area of a cube is 150 cm². What is its volume?",
  "एक घन का कुल पृष्ठीय क्षेत्रफल 150 वर्ग सेमी है। उसका आयतन क्या है?",
  ["25 cm³", "64 cm³", "100 cm³", "125 cm³"], 3,
  "A cube has 6 equal faces, so each face is 150 ÷ 6 = 25 cm² and the edge is 5 cm; the volume is 5³ = 125 cm³. "
  "25 is the area of one face, not a volume; 64 and 100 cm³ would need edges of 4 cm and about 4.6 cm.",
  "घन के 6 बराबर फलक होते हैं, इसलिए हर फलक 150 ÷ 6 = 25 वर्ग सेमी है और किनारा 5 सेमी; आयतन 5³ = 125 घन सेमी है। "
  "25 एक फलक का क्षेत्रफल है, आयतन नहीं; 64 और 100 घन सेमी के लिए 4 सेमी और लगभग 4.6 सेमी के किनारे चाहिए।",
  "qa-gm-a-cube-from-its-surface-area", _gm1,
  opts_hi=["25 घन सेमी", "64 घन सेमी", "100 घन सेमी", "125 घन सेमी"])

def _gm2():
    posts = {(x, 0) for x in range(0, 21, 4)} | {(x, 20) for x in range(0, 21, 4)} | {(0, y) for y in range(0, 21, 4)} | {(20, y) for y in range(0, 21, 4)}
    return str(len(posts))
N(QA, "Geometry & Mensuration", "medium",
  "Fence posts are to be set along the boundary of a square plot with sides of 20 m, one at every corner and one every 4 m along each side. How many posts are needed?",
  "20 मीटर भुजा वाले एक वर्गाकार भूखंड की सीमा पर बाड़ के खंभे लगाने हैं, हर कोने पर एक और हर भुजा पर हर 4 मीटर पर एक। कितने खंभे चाहिए?",
  ["20", "21", "24", "36"], 0,
  "The boundary is 4 × 20 = 80 m long and closes on itself, so posts every 4 m make 80 ÷ 4 = 20 gaps and 20 posts (each corner post is shared by two sides). "
  "24 counts 6 posts on each side and so counts every corner twice; 21 treats the boundary as a straight line with a post at each end; 36 fills the whole plot with a grid of posts.",
  "सीमा 4 × 20 = 80 मीटर लंबी है और स्वयं पर बंद होती है, इसलिए हर 4 मीटर पर खंभों से 80 ÷ 4 = 20 अंतराल और 20 खंभे बनते हैं (हर कोने का खंभा दो भुजाओं में साझा है)। "
  "24 हर भुजा पर 6 खंभे गिनता है और इस तरह हर कोने को दो बार गिनता है; 21 सीमा को ऐसी सीधी रेखा मानता है जिसके दोनों छोरों पर खंभा हो; 36 पूरे भूखंड को खंभों की जाली से भर देता है।",
  "qa-gm-posts-round-a-square-plot", _gm2)

# ---------------------------------------------------------------- Time & Work (2)
def _tw1():
    xs = [a for a in range(31) if 500 * (30 - a) - 100 * a == 12600]
    assert xs == [4]
    return str(xs[0])
N(QA, "Time & Work", "medium",
  "A worker is paid ₹500 for each day she works and is fined ₹100 for each day she is absent. At the end of 30 days she receives ₹12,600. For how many days was she absent?",
  "एक कामगार को काम के हर दिन के ₹500 मिलते हैं और अनुपस्थिति के हर दिन ₹100 का जुर्माना लगता है। 30 दिनों के अंत में उसे ₹12,600 मिलते हैं। वह कितने दिन अनुपस्थित रही?",
  ["4", "5", "6", "8"], 0,
  "Had she worked all 30 days she would have received ₹15,000. Each day of absence costs her the ₹500 she would have earned and a ₹100 fine -- ₹600 in all. She is ₹2,400 short, so she was absent 2,400 ÷ 600 = 4 days (26 × 500 - 4 × 100 = 12,600). "
  "6 counts only ₹400 a day, subtracting the fine instead of adding it; 5 and 8 have no basis.",
  "यदि वह सभी 30 दिन काम करती तो उसे ₹15,000 मिलते। अनुपस्थिति का हर दिन उससे वे ₹500 छीनता है जो वह कमाती, और ₹100 जुर्माना -- कुल ₹600। उसे ₹2,400 कम मिले, इसलिए वह 2,400 ÷ 600 = 4 दिन अनुपस्थित रही (26 × 500 - 4 × 100 = 12,600)। "
  "6 हर दिन केवल ₹400 गिनता है, जुर्माना जोड़ने के बजाय घटाकर; 5 और 8 का कोई आधार नहीं।",
  "qa-tw-wages-with-a-fine-for-absence", _tw1)

def _tw2():
    t = 36 * F(2 * 2, 3 * 3)              # the flow goes as the cross-section, the square of the bore
    return f"{t} minutes"
N(QA, "Time & Work", "hard",
  "A pipe 2 cm across fills a tank in 36 minutes. If water flows through a pipe 3 cm across at the same speed, how long will that pipe take to fill the tank?",
  "2 सेमी व्यास का एक पाइप एक टंकी को 36 मिनट में भरता है। यदि 3 सेमी व्यास के पाइप से पानी उसी वेग से बहे, तो वह पाइप टंकी को कितने समय में भरेगा?",
  ["16 minutes", "24 minutes", "54 minutes", "81 minutes"], 0,
  "At the same speed, the amount of water a pipe carries each minute goes with the area of its cross-section, which goes with the square of its width. A 3 cm pipe carries (3/2)² = 9/4 times as much as a 2 cm pipe, so it fills the tank in 36 × 4/9 = 16 minutes. "
  "24 minutes scales by the width alone (36 × 2/3); 54 and 81 minutes multiply instead of dividing, as if a wider pipe were slower.",
  "समान वेग पर कोई पाइप हर मिनट जितना पानी ले जाता है वह उसके अनुप्रस्थ काट के क्षेत्रफल के अनुपात में होता है, जो उसके व्यास के वर्ग के अनुपात में है। 3 सेमी का पाइप 2 सेमी के पाइप से (3/2)² = 9/4 गुना पानी ले जाता है, इसलिए वह टंकी को 36 × 4/9 = 16 मिनट में भरता है। "
  "24 मिनट केवल व्यास के अनुपात से बदलता है (36 × 2/3); 54 और 81 मिनट भाग देने के बजाय गुणा करते हैं, मानो चौड़ा पाइप धीमा हो।",
  "qa-tw-a-pipe-of-a-larger-bore", _tw2,
  opts_hi=["16 मिनट", "24 मिनट", "54 मिनट", "81 मिनट"])

# ---------------------------------------------------------------- Puzzle Hybrid (3)
def _ph1():
    sundays = [d for d in range(1, 31) if (d - 1 + 4) % 7 == 6]       # day 1 is a Friday (Mon = 0)
    return f"{sundays[2]}th"
N(QA, "Puzzle Hybrid", "easy",
  "The first day of a month is a Friday. On what date does the third Sunday of that month fall?",
  "किसी महीने का पहला दिन शुक्रवार है। उस महीने का तीसरा रविवार किस तारीख़ को पड़ता है?",
  ["15th", "16th", "17th", "18th"], 2,
  "If the 1st is a Friday, the 2nd is a Saturday and the 3rd the first Sunday; the Sundays fall on the 3rd, 10th and 17th. The third Sunday is the 17th. 15th and 16th are a Friday and a Saturday; 18th is a Monday.",
  "यदि 1 तारीख़ शुक्रवार है, तो 2 शनिवार और 3 पहला रविवार है; रविवार 3, 10 और 17 को पड़ते हैं। तीसरा रविवार 17 तारीख़ है। 15 और 16 शुक्रवार और शनिवार हैं; 18 सोमवार है।",
  "qa-ph-the-third-sunday-of-a-month", _ph1,
  opts_hi=["15 तारीख़", "16 तारीख़", "17 तारीख़", "18 तारीख़"])

def _ph2():
    ways = sum(1 for b in range(11) for c5 in range(5) for d in range(3) if 2 * b + 5 * c5 + 10 * d <= 20)
    no_ten = sum(1 for b in range(11) for c5 in range(5) if 2 * b + 5 * c5 <= 20)
    assert (ways, no_ten) == (40, 29)
    return str(ways)
N(QA, "Puzzle Hybrid", "hard",
  "If the order of the coins does not matter, in how many different ways can exactly ₹20 be paid with ₹1, ₹2, ₹5 and ₹10 coins?",
  "यदि सिक्कों का क्रम मायने नहीं रखता, तो ठीक ₹20 का भुगतान ₹1, ₹2, ₹5 और ₹10 के सिक्कों से कितने अलग-अलग तरीक़ों से किया जा सकता है?",
  ["29", "36", "39", "40"], 3,
  "Fix the number of ₹10 coins. With none, count the ways with ₹1, ₹2 and ₹5 coins: no ₹5 coin gives 11 ways (0 to 10 two-rupee coins, the rest in ₹1 coins), one gives 8, two give 6, three give 3 and four give 1 -- 29. With one ₹10 coin the other ₹10 can be made in 10 ways (6 + 3 + 1), and with two ₹10 coins in 1 way. "
  "In all 29 + 10 + 1 = 40. 29 forgets the ₹10 coin; 39 misses the way with two ₹10 coins; 36 has no basis.",
  "₹10 के सिक्कों की संख्या तय कीजिए। एक भी नहीं हो, तो ₹1, ₹2 और ₹5 के सिक्कों से तरीक़े गिनिए: ₹5 का कोई सिक्का न हो तो 11 तरीक़े (0 से 10 दो रुपये के सिक्के, बाक़ी ₹1 में), एक हो तो 8, दो हों तो 6, तीन हों तो 3 और चार हों तो 1 -- 29। ₹10 का एक सिक्का हो तो बाक़ी ₹10, 10 तरीक़ों से (6 + 3 + 1) बनते हैं, और ₹10 के दो सिक्के हों तो 1 तरीक़े से। "
  "कुल 29 + 10 + 1 = 40। 29, ₹10 का सिक्का भूल जाता है; 39, ₹10 के दो सिक्कों वाला तरीक़ा चूक जाता है; 36 का कोई आधार नहीं।",
  "qa-ph-ways-to-make-20-rupees-in-coins", _ph2)

def _ph3():
    seen, frontier = {3}, [3]                  # heads showing; a move turns over exactly two coins
    while frontier:
        h = frontier.pop()
        for k in range(3):                     # k heads among the two coins turned
            if k <= h and 2 - k <= 3 - h:
                nh = h - k + (2 - k)
                if nh not in seen:
                    seen.add(nh); frontier.append(nh)
    assert 0 not in seen
    return "It cannot be done"
N(QA, "Puzzle Hybrid", "hard",
  "Three coins lie on a table, all showing heads. In each move exactly two of the coins must be turned over. What is the fewest number of moves needed to make all three coins show tails?",
  "मेज़ पर तीन सिक्के रखे हैं, सभी चित दिखाते हुए। हर चाल में ठीक दो सिक्कों को पलटना ही होगा। तीनों सिक्कों को पट दिखाने के लिए कम से कम कितनी चालें चाहिए?",
  ["1", "2", "3", "It cannot be done"], 3,
  "Turning over two coins changes the number of heads by -2, 0 or +2, so the number of heads keeps its parity: it starts at 3, an odd number, and can never become 0, an even one. However many moves are made, at least one coin shows heads. "
  "So no number of moves will do; 3 moves might look natural (turning each coin once), but each move must turn two coins, and 1 or 2 moves leave one or three heads.",
  "दो सिक्के पलटने से चितों की संख्या -2, 0 या +2 बदलती है, इसलिए चितों की संख्या की सम-विषमता बनी रहती है: वह 3 से, एक विषम संख्या से, शुरू होती है और कभी 0, एक सम संख्या, नहीं बन सकती। कितनी भी चालें चली जाएँ, कम से कम एक सिक्का चित रहेगा। "
  "अतः कोई भी संख्या काम नहीं करेगी; 3 चालें स्वाभाविक लग सकती हैं (हर सिक्के को एक बार पलटना), पर हर चाल में दो सिक्के पलटने होते हैं, और 1 या 2 चालें एक या तीन चित छोड़ती हैं।",
  "qa-ph-coins-turned-two-at-a-time", _ph3, opts_hi=["1", "2", "3", "यह संभव ही नहीं"])

# ---------------------------------------------------------------- the data-sufficiency block's two Quant items
def _ds1():
    pi = F(22, 7)
    s1 = {pi * (F(44) / (2 * pi)) ** 2}                         # I: circumference 44 cm gives r = 7
    s2 = {pi * (F(14) / 2) ** 2}                                # II: a chord through the centre is a diameter
    assert s1 == s2 == {154}
    return _ds(s1, s2, s1 & s2)
DS(QA, "easy",
   "What is the area of a circle?",
   "एक वृत्त का क्षेत्रफल क्या है?",
   "Its circumference is 44 cm.", "उसकी परिधि 44 सेमी है।",
   "A chord of the circle 14 cm long passes through its centre.", "वृत्त की 14 सेमी लंबी एक जीवा उसके केंद्र से होकर जाती है।",
   1,
   "Statement I: a circumference of 44 cm gives a radius of 7 cm (taking π as 22/7), and so the area, 154 cm² -- sufficient. Statement II: a chord through the centre is a diameter, so the radius is 7 cm and the area is again found -- sufficient. Either statement alone answers the question.",
   "कथन I: 44 सेमी की परिधि से त्रिज्या 7 सेमी मिलती है (π को 22/7 लेकर), और इस तरह क्षेत्रफल 154 वर्ग सेमी -- पर्याप्त। कथन II: केंद्र से होकर जाने वाली जीवा व्यास है, इसलिए त्रिज्या 7 सेमी है और क्षेत्रफल फिर मिल जाता है -- पर्याप्त। कोई भी एक कथन अकेले प्रश्न का उत्तर देता है।",
   "qa-ds-a-circle-s-area-found-two-ways", _ds1)

def _ds2():
    s1 = {n % 4 for n in range(37, 10000, 100)}              # I: the last two digits are 37
    s2 = {n % 4 for n in range(1, 10000, 2)}                 # II: n is odd
    both = {n % 4 for n in range(37, 10000, 100) if n % 2}
    assert s1 == {1} and s2 == {1, 3}
    return _ds(s1, s2, both)
DS(QA, "medium",
   "What is the remainder when a whole number n is divided by 4?",
   "एक पूर्ण संख्या n को 4 से भाग देने पर शेषफल क्या है?",
   "The last two digits of n are 37.", "n के अंतिम दो अंक 37 हैं।",
   "n is an odd number.", "n एक विषम संख्या है।",
   0,
   "Statement I: 100 is divisible by 4, so n leaves the same remainder by 4 as its last two digits, 37, which leaves 1 -- sufficient. Statement II: an odd number may leave 1 or 3 (5 leaves 1, 7 leaves 3) -- not sufficient. One statement alone answers the question.",
   "कथन I: 100, 4 से विभाज्य है, इसलिए n को 4 से भाग देने पर वही शेष बचता है जो उसके अंतिम दो अंकों, 37, से, यानी 1 -- पर्याप्त। कथन II: विषम संख्या का शेष 1 या 3 हो सकता है (5 का 1, 7 का 3) -- पर्याप्त नहीं। एक कथन अकेले प्रश्न का उत्तर देता है।",
   "qa-ds-a-remainder-by-4-from-the-last-two-digits", _ds2)
