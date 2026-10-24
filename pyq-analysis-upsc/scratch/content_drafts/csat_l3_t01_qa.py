# -*- coding: utf-8 -*-
"""CSAT Level 3 · Test 1 -- Quantitative Aptitude (34 items: 32 in the Quant slots, 2 in the data-sufficiency block).

Level 3 is the harder CSAT tier: the same mix as Level 2 (playbook B.7), a difficulty of 2 easy / 18 medium / 14 hard,
and more steps per item. None of the shapes used in Level 2 Tests 1-7 or Level 1 Minis 1-3: pairs (x, y) on a straight
line, a prime above 3 squared, two-digit numbers with remainder 3 on division by 7, the least multiplier of 7 that gives
a number of ones, the factors of 2^10 - 1, four consecutive numbers with a given product, n^2 + n + 1 divisible by 7,
divisible by 9 but not by 6; a boat timed on two round journeys, a dog and a hare that leap at different rates, two cars
that meet or catch up, a field crossed on its diagonal; a hostel cost that is partly fixed, a three-term ratio after
equal additions, a blend of three teas, a share from equal fractions, two alloys of three metals; two equal
instalments, a fall in price that buys more, money split between two rates; a sum of alternating squares, the 100th
number that is not a square; digits in rising order, letters in the wrong envelopes; a circle in a square in a circle,
a triangle and a hexagon of equal perimeter; two candles, a tap turned on late; the right angles of a clock in a day,
the least moves for five discs, the centre of a magic square, the last person left in a circle; and two
data-sufficiency items. Every key is worked out in code by check()."""
from fractions import Fraction as F
from itertools import permutations
import csat_common as c
from csat_common import N, S2, SC, DS, QA

def _ds(s1, s2, both):
    alone = (len(set(s1)) == 1, len(set(s2)) == 1)
    return "b" if all(alone) else "a" if any(alone) else "c" if len(set(both)) == 1 else "d"

def _two(one, two):
    return c.T2[{(True, False): 0, (False, True): 1, (True, True): 2, (False, False): 3}[(one, two)]]

def _primes(n):
    return [p for p in range(2, n) if all(p % d for d in range(2, int(p ** 0.5) + 1))]

# ---------------------------------------------------------------- Number Theory (8)
def _nt1():
    pairs = [(x, y) for y in range(1, 101) for x in range(1, 101) if 3 * x + 5 * y == 101]
    assert pairs[-1] == (2, 19) and pairs[0] == (32, 1)
    return str(len(pairs))
N(QA, "Number Theory", "medium",
  "How many pairs of natural numbers (x, y) satisfy the equation 3x + 5y = 101?",
  "प्राकृत संख्याओं के कितने युग्म (x, y) समीकरण 3x + 5y = 101 को संतुष्ट करते हैं?",
  ["7", "8", "9", "10"], 0,
  "For x to be a natural number, 101 - 5y must be a positive multiple of 3. 101 leaves remainder 2 on division by 3 and 5y leaves the same remainder as 2y, so 2y must leave remainder 2, that is y = 1, 4, 7, ..., 19 "
  "(y = 22 would make 101 - 5y negative). That is 7 values, giving x = 32, 27, 22, 17, 12, 7 and 2. 8, 9 and 10 count values of y for which x is negative or not a whole number.",
  "x के प्राकृत संख्या होने के लिए 101 - 5y को 3 का धनात्मक गुणज होना चाहिए। 101 को 3 से भाग देने पर शेषफल 2 है और 5y वही शेषफल देता है जो 2y, इसलिए 2y का शेषफल 2 होना चाहिए, यानी y = 1, 4, 7, ..., 19 "
  "(y = 22 पर 101 - 5y ऋणात्मक हो जाता)। ये 7 मान हैं, जिनसे x = 32, 27, 22, 17, 12, 7 और 2 मिलते हैं। 8, 9 और 10, y के उन मानों को भी गिनते हैं जिनके लिए x ऋणात्मक या भिन्नात्मक होता है।",
  "qa-nt-pairs-on-the-line-3x-plus-5y", _nt1)

def _nt2():
    ps = [p for p in _primes(2000) if p > 3]
    return _two(all((p * p - 1) % 24 == 0 for p in ps), all((p * p + 1) % 5 == 0 for p in ps))
S2(QA, "Number Theory", "hard",
  "Let p be any prime number greater than 3. Which of the following statements is/are correct?",
  "मान लीजिए p, 3 से बड़ी कोई भी अभाज्य संख्या है। निम्नलिखित में से कौन-सा/से कथन सही है/हैं?",
  ["p² - 1 is divisible by 24.", "p² + 1 is divisible by 5."],
  ["p² - 1, 24 से विभाज्य है।", "p² + 1, 5 से विभाज्य है।"], 0,
  "Only 1 is correct. p² - 1 = (p - 1)(p + 1). Since p is odd, p - 1 and p + 1 are consecutive even numbers, one of which is a multiple of 4, so their product is a multiple of 8; and of the three consecutive numbers p - 1, p, p + 1 one is a multiple of 3, "
  "which cannot be the prime p. So 8 × 3 = 24 divides p² - 1 for every such prime (5² - 1 = 24, 7² - 1 = 48, 11² - 1 = 120). Statement 2 holds for 7 (50) and 13 (170) but fails for 5 (26) and 11 (122), so it is not true for every such prime.",
  "केवल 1 सही है। p² - 1 = (p - 1)(p + 1)। p विषम है, इसलिए p - 1 और p + 1 क्रमागत सम संख्याएँ हैं, जिनमें से एक 4 का गुणज है, अतः उनका गुणनफल 8 का गुणज है; और तीन क्रमागत संख्याओं p - 1, p, p + 1 में से एक 3 का गुणज है, "
  "जो अभाज्य p नहीं हो सकती। इसलिए हर ऐसी अभाज्य संख्या के लिए 8 × 3 = 24, p² - 1 को विभाजित करता है (5² - 1 = 24, 7² - 1 = 48, 11² - 1 = 120)। कथन 2, 7 (50) और 13 (170) के लिए सही है, पर 5 (26) और 11 (122) के लिए ग़लत, इसलिए वह हर ऐसी अभाज्य संख्या के लिए सही नहीं है।",
  "qa-nt-a-prime-above-three-squared", check=_nt2, craft="inference")

def _nt3():
    xs = [n for n in range(10, 100) if n % 7 == 3]
    assert len(xs) == 13 and xs[0] == 10 and xs[-1] == 94
    return str(sum(xs))
N(QA, "Number Theory", "medium",
  "What is the sum of all the two-digit numbers that leave a remainder of 3 when divided by 7?",
  "उन सभी दो अंकों की संख्याओं का योग क्या है जो 7 से भाग देने पर शेषफल 3 देती हैं?",
  ["572", "624", "650", "676"], 3,
  "The numbers are 10, 17, 24, ..., 94: an arithmetic progression with common difference 7, from 7 + 3 to 91 + 3. It has (94 - 10) ÷ 7 + 1 = 13 terms, so the sum is 13 × (10 + 94) ÷ 2 = 13 × 52 = 676. "
  "572 and 624 count only 11 and 12 of the terms; 650 takes 50 as the average term instead of (10 + 94) ÷ 2 = 52.",
  "संख्याएँ 10, 17, 24, ..., 94 हैं: सार्व अंतर 7 वाली एक समांतर श्रेणी, 7 + 3 से 91 + 3 तक। इसमें (94 - 10) ÷ 7 + 1 = 13 पद हैं, इसलिए योग 13 × (10 + 94) ÷ 2 = 13 × 52 = 676 है। "
  "572 और 624 केवल 11 और 12 पद गिनते हैं; 650 औसत पद को (10 + 94) ÷ 2 = 52 के बजाय 50 मान लेता है।",
  "qa-nt-two-digit-numbers-with-remainder-3-by-7", _nt3)

def _nt4():
    r = 1
    while r % 7:
        r = 10 * r + 1
    assert r == 111111 and [int("1" * k) % 7 for k in range(1, 6)] == [1, 4, 6, 5, 2]
    return f"{r // 7:,}"
N(QA, "Number Theory", "hard",
  "What is the smallest natural number which, when multiplied by 7, gives a number written with the digit 1 alone (such as 11, 111, 1111, ...)?",
  "वह सबसे छोटी प्राकृत संख्या कौन-सी है जिसे 7 से गुणा करने पर ऐसी संख्या मिलती है जो केवल अंक 1 से लिखी जाती है (जैसे 11, 111, 1111, ...)?",
  ["15,873", "15,879", "111,111", "158,730"], 0,
  "Divide the numbers 1, 11, 111, ... by 7: the remainders are 1, 4, 6, 5, 2 for one to five ones, and 0 for six ones. So the first such number divisible by 7 is 111,111 = 7 × 15,873, and 15,873 is the answer. "
  "111,111 is the product, not the multiplier; 7 × 15,879 = 111,153; 7 × 158,730 = 1,111,110, which ends in 0.",
  "संख्याओं 1, 11, 111, ... को 7 से भाग दीजिए: एक से पाँच इकाई-अंकों तक शेषफल 1, 4, 6, 5, 2 हैं, और छह अंकों पर 0। अतः 7 से विभाज्य ऐसी पहली संख्या 111,111 = 7 × 15,873 है, और उत्तर 15,873 है। "
  "111,111 गुणनफल है, गुणक नहीं; 7 × 15,879 = 111,153; 7 × 158,730 = 1,111,110, जिसके अंत में 0 है।",
  "qa-nt-the-least-multiplier-of-7-that-gives-only-ones", _nt4)

def _nt5():
    n = 2 ** 10 - 1
    assert n == 31 * 33
    ok = [n % 3 == 0, n % 11 == 0, n % 31 == 0]
    return {(True, True, False): "1 and 2 only", (False, True, True): "2 and 3 only", (True, False, True): "1 and 3 only",
            (True, True, True): "1, 2 and 3"}[tuple(ok)]
SC(QA, "Number Theory", "medium",
  "Consider the following statements about the number 2¹⁰ - 1:",
  "संख्या 2¹⁰ - 1 के बारे में निम्नलिखित कथनों पर विचार कीजिए:",
  ["It is divisible by 3.", "It is divisible by 11.", "It is divisible by 31."],
  ["यह 3 से विभाज्य है।", "यह 11 से विभाज्य है।", "यह 31 से विभाज्य है।"],
  ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"], 3,
  "All three are correct. 2¹⁰ - 1 is a difference of two squares: (2⁵)² - 1² = (2⁵ - 1)(2⁵ + 1) = 31 × 33 = 3 × 11 × 31 = 1,023. "
  "The factorisation answers all three statements at once; testing 1,023 against each divisor separately gives the same result with more work.",
  "तीनों सही हैं। 2¹⁰ - 1 दो वर्गों का अंतर है: (2⁵)² - 1² = (2⁵ - 1)(2⁵ + 1) = 31 × 33 = 3 × 11 × 31 = 1,023। "
  "यह गुणनखंडन तीनों कथनों का उत्तर एक साथ देता है; 1,023 को हर भाजक से अलग-अलग जाँचने पर अधिक श्रम से वही परिणाम मिलता है।",
  "qa-nt-the-factors-of-2-to-the-10-less-1", check=_nt5, craft="inference",
  opts_hi=["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"])

def _nt6():
    n = next(k for k in range(1, 100) if k * (k + 1) * (k + 2) * (k + 3) == 3024)
    assert n == 6 and 5 * 6 * 7 * 8 == 1680 and all((4 * k + 6) % 4 for k in range(1, 50))
    return str(4 * n + 6)
N(QA, "Number Theory", "medium",
  "The product of four consecutive natural numbers is 3,024. What is their sum?",
  "चार क्रमागत प्राकृत संख्याओं का गुणनफल 3,024 है। उनका योग क्या है?",
  ["24", "26", "28", "30"], 3,
  "3,024 = 2⁴ × 3³ × 7. The four numbers must include 7, and 6 × 7 × 8 × 9 = 3,024, so the numbers are 6, 7, 8 and 9 and their sum is 30. "
  "26 is the sum for 5-8, whose product is 1,680; 24 and 28 cannot be the sum of any four consecutive numbers, since such a sum is 4k + 6 and is never a multiple of 4.",
  "3,024 = 2⁴ × 3³ × 7। चारों संख्याओं में 7 होना चाहिए, और 6 × 7 × 8 × 9 = 3,024, इसलिए संख्याएँ 6, 7, 8 और 9 हैं और उनका योग 30 है। "
  "26, 5-8 का योग है, जिसका गुणनफल 1,680 है; 24 और 28 किन्हीं चार क्रमागत संख्याओं का योग हो ही नहीं सकते, क्योंकि ऐसा योग 4k + 6 होता है और कभी 4 का गुणज नहीं होता।",
  "qa-nt-four-consecutive-numbers-with-product-3024", _nt6)

def _nt7():
    assert [(n * n + n + 1) % 7 for n in range(7)] == [1, 3, 0, 6, 0, 3, 1]
    return str(sum(1 for n in range(1, 101) if (n * n + n + 1) % 7 == 0))
N(QA, "Number Theory", "hard",
  "For how many natural numbers n from 1 to 100 is n² + n + 1 divisible by 7?",
  "1 से 100 तक की कितनी प्राकृत संख्याओं n के लिए n² + n + 1, 7 से विभाज्य है?",
  ["14", "15", "28", "29"], 3,
  "Whether 7 divides n² + n + 1 depends only on the remainder of n on division by 7. For remainders 0 to 6 the expression leaves 1, 3, 0, 6, 0, 3, 1, so n must leave remainder 2 or 4. "
  "From 1 to 100 the numbers 2, 9, ..., 100 (remainder 2) are 15, and 4, 11, ..., 95 (remainder 4) are 14: 29 in all. 15 and 14 count only one of the two remainders; 28 assumes 14 of each.",
  "7 से n² + n + 1 की विभाज्यता केवल इस पर निर्भर है कि n को 7 से भाग देने पर क्या शेषफल बचता है। शेषफल 0 से 6 के लिए व्यंजक 1, 3, 0, 6, 0, 3, 1 शेषफल देता है, इसलिए n का शेषफल 2 या 4 होना चाहिए। "
  "1 से 100 तक संख्याएँ 2, 9, ..., 100 (शेषफल 2) 15 हैं, और 4, 11, ..., 95 (शेषफल 4) 14 हैं: कुल 29। 15 और 14 दोनों में से केवल एक शेषफल गिनते हैं; 28 दोनों के 14-14 मान लेता है।",
  "qa-nt-n-squared-plus-n-plus-1-divisible-by-7", _nt7)

def _nt8():
    opts = [1359, 2826, 4302, 5214]
    hit = [n for n in opts if n % 9 == 0 and n % 6 != 0]
    assert hit == [1359]
    return f"{hit[0]:,}"
N(QA, "Number Theory", "easy",
  "Which one of the following numbers is divisible by 9 but not by 6?",
  "निम्नलिखित संख्याओं में से कौन-सी 9 से विभाज्य है पर 6 से नहीं?",
  ["1,359", "2,826", "4,302", "5,214"], 0,
  "A number is divisible by 9 when its digits add up to a multiple of 9, and by 6 when it is even and divisible by 3. The digit sums are 18, 18, 9 and 12, so 5,214 is not divisible by 9. "
  "Of the other three, 2,826 and 4,302 are even, and being divisible by 9 they are also divisible by 3 and so by 6. Only 1,359 is odd: divisible by 9 but not by 6.",
  "कोई संख्या 9 से तब विभाज्य है जब उसके अंकों का योग 9 का गुणज हो, और 6 से तब जब वह सम हो और 3 से विभाज्य हो। अंकों के योग 18, 18, 9 और 12 हैं, इसलिए 5,214, 9 से विभाज्य नहीं है। "
  "बाक़ी तीन में 2,826 और 4,302 सम हैं, और 9 से विभाज्य होने के कारण 3 से भी विभाज्य हैं, अतः 6 से भी। केवल 1,359 विषम है: 9 से विभाज्य पर 6 से नहीं।",
  "qa-nt-divisible-by-9-but-not-by-6", _nt8)

# ---------------------------------------------------------------- Speed-Distance-Time (4)
def _sdt1():
    sols = [(F(b, 2), F(s, 2)) for b in range(1, 60) for s in range(1, 60) if b > s
            and F(30 * 2, b - s) + F(44 * 2, b + s) == 10 and F(40 * 2, b - s) + F(55 * 2, b + s) == 13]
    assert sols == [(8, 3)]
    return f"{sols[0][1]} km/h"
N(QA, "Speed-Distance-Time", "hard",
  "A boat goes 30 km upstream and 44 km downstream in 10 hours. In 13 hours it can go 40 km upstream and 55 km downstream. What is the speed of the stream?",
  "एक नाव 10 घंटे में धारा के विरुद्ध 30 किमी और धारा के साथ 44 किमी जाती है। 13 घंटे में वह धारा के विरुद्ध 40 किमी और धारा के साथ 55 किमी जा सकती है। धारा की चाल क्या है?",
  ["3 km/h", "5 km/h", "6 km/h", "8 km/h"], 0,
  "Let the upstream and downstream speeds be u and d. Then 30/u + 44/d = 10 and 40/u + 55/d = 13. Multiply the first by 4 and the second by 3: 120/u + 176/d = 40 and 120/u + 165/d = 39, so 11/d = 1 and d = 11 km/h; then 30/u = 6 and u = 5 km/h. "
  "The stream's speed is half the difference, (11 - 5) ÷ 2 = 3 km/h, and the boat's speed in still water is (11 + 5) ÷ 2 = 8 km/h. 8 km/h is the boat's own speed, 5 km/h the upstream speed and 6 km/h the difference before it is halved.",
  "मान लीजिए धारा के विरुद्ध और धारा के साथ चालें u और d हैं। तब 30/u + 44/d = 10 और 40/u + 55/d = 13। पहले को 4 से और दूसरे को 3 से गुणा कीजिए: 120/u + 176/d = 40 और 120/u + 165/d = 39, अतः 11/d = 1 और d = 11 किमी/घंटा; फिर 30/u = 6 और u = 5 किमी/घंटा। "
  "धारा की चाल अंतर की आधी, (11 - 5) ÷ 2 = 3 किमी/घंटा है, और शांत जल में नाव की चाल (11 + 5) ÷ 2 = 8 किमी/घंटा। 8 किमी/घंटा नाव की अपनी चाल है, 5 किमी/घंटा धारा के विरुद्ध चाल और 6 किमी/घंटा आधा करने से पहले का अंतर।",
  "qa-sdt-a-boat-timed-on-two-journeys", _sdt1,
  opts_hi=["3 किमी/घंटा", "5 किमी/घंटा", "6 किमी/घंटा", "8 किमी/घंटा"])

def _sdt2():
    dog = 3 * F(3, 2)                        # 3 dog leaps in the time of 4 hare leaps; a dog leap = 3/2 hare leap
    r = dog / 4
    assert r == F(9, 8)
    return f"{r.numerator} : {r.denominator}"
N(QA, "Speed-Distance-Time", "hard",
  "A dog is chasing a hare. The hare takes 4 leaps in the time the dog takes 3, but 2 of the dog's leaps cover as much ground as 3 of the hare's. What is the ratio of the dog's speed to the hare's speed?",
  "एक कुत्ता एक खरगोश का पीछा कर रहा है। जितने समय में कुत्ता 3 छलाँगें लगाता है उतने में खरगोश 4 छलाँगें लगाता है, पर कुत्ते की 2 छलाँगें उतनी दूरी तय करती हैं जितनी खरगोश की 3। कुत्ते की चाल और खरगोश की चाल का अनुपात क्या है?",
  ["9 : 8", "3 : 4", "8 : 9", "3 : 2"], 0,
  "Measure distance in hare leaps. One dog leap = 3/2 hare leaps, so in the time the hare covers 4 hare leaps the dog covers 3 × 3/2 = 9/2 hare leaps. The ratio of speeds is 9/2 : 4 = 9 : 8, and the dog gains slowly. "
  "3 : 4 compares only the numbers of leaps, 3 : 2 only their lengths, and 8 : 9 is the right ratio turned upside down.",
  "दूरी को खरगोश की छलाँगों में मापिए। कुत्ते की एक छलाँग = 3/2 खरगोश-छलाँग, इसलिए जितने समय में खरगोश 4 छलाँगें तय करता है उतने में कुत्ता 3 × 3/2 = 9/2 खरगोश-छलाँगें तय करता है। चालों का अनुपात 9/2 : 4 = 9 : 8 है, और कुत्ता धीरे-धीरे पास आता है। "
  "3 : 4 केवल छलाँगों की संख्या की, 3 : 2 केवल उनकी लंबाई की तुलना करता है, और 8 : 9 सही अनुपात को उलट देता है।",
  "qa-sdt-a-dog-and-a-hare-that-leap-at-different-rates", _sdt2)

def _sdt3():
    sols = [(a, b) for a in range(1, 101) for b in range(1, a) if a + b == 100 and 5 * (a - b) == 100]
    assert sols == [(60, 40)]
    return f"{sols[0][0]} km/h"
N(QA, "Speed-Distance-Time", "medium",
  "Two cars start at the same time from two towns 100 km apart. If they drive towards each other, they meet after 1 hour; if they drive in the same direction, the faster car, starting behind, catches the slower one after 5 hours. What is the speed of the faster car?",
  "दो कारें एक ही समय पर 100 किमी दूर स्थित दो कस्बों से चलती हैं। यदि वे एक-दूसरे की ओर चलें तो 1 घंटे बाद मिलती हैं; यदि वे एक ही दिशा में चलें तो पीछे से चली तेज़ कार 5 घंटे बाद धीमी कार को पकड़ लेती है। तेज़ कार की चाल क्या है?",
  ["40 km/h", "50 km/h", "60 km/h", "80 km/h"], 2,
  "Moving towards each other they close the 100 km at the sum of their speeds in 1 hour, so a + b = 100. Moving the same way the gap closes at the difference of the speeds, 100 km in 5 hours, so a - b = 20. Then a = 60 km/h and b = 40 km/h. "
  "40 km/h is the slower car; 50 km/h halves the sum and ignores the difference; 80 km/h is the sum less the difference, twice the slower car's speed.",
  "एक-दूसरे की ओर चलते हुए वे 100 किमी की दूरी अपनी चालों के योग से 1 घंटे में पाटती हैं, इसलिए a + b = 100। एक ही दिशा में चलते हुए दूरी चालों के अंतर से घटती है, 5 घंटे में 100 किमी, इसलिए a - b = 20। तब a = 60 किमी/घंटा और b = 40 किमी/घंटा। "
  "40 किमी/घंटा धीमी कार की चाल है; 50 किमी/घंटा योग को आधा करता है और अंतर को अनदेखा करता है; 80 किमी/घंटा योग में से अंतर घटाता है, जो धीमी कार की चाल का दोगुना है।",
  "qa-sdt-two-cars-that-meet-or-catch-up", _sdt3,
  opts_hi=["40 किमी/घंटा", "50 किमी/घंटा", "60 किमी/घंटा", "80 किमी/घंटा"])

def _sdt4():
    diag = F(6000, 60) * 2                   # metres in 2 minutes at 6 km/h
    assert diag == 200
    return f"{int(diag * diag / 2):,} m²"
N(QA, "Speed-Distance-Time", "medium",
  "A man walking at 6 km/h crosses a square field along its diagonal in 2 minutes. What is the area of the field?",
  "6 किमी/घंटा की चाल से चलता एक व्यक्ति एक वर्गाकार खेत को उसके विकर्ण के अनुदिश 2 मिनट में पार करता है। खेत का क्षेत्रफल क्या है?",
  ["10,000 m²", "20,000 m²", "28,284 m²", "40,000 m²"], 1,
  "At 6 km/h he walks 100 m a minute, so the diagonal is 200 m. A square's area is half the square of its diagonal: 200² ÷ 2 = 20,000 m² (2 hectares); its side is 200/√2 ≈ 141.4 m. "
  "40,000 m² treats the diagonal as a side; 10,000 m² takes half the diagonal as the side; 28,284 m² multiplies the diagonal by the side.",
  "6 किमी/घंटा पर वह प्रति मिनट 100 मीटर चलता है, इसलिए विकर्ण 200 मीटर है। वर्ग का क्षेत्रफल उसके विकर्ण के वर्ग का आधा होता है: 200² ÷ 2 = 20,000 वर्ग मीटर (2 हेक्टेयर); उसकी भुजा 200/√2 ≈ 141.4 मीटर है। "
  "40,000 वर्ग मीटर विकर्ण को भुजा मान लेता है; 10,000 वर्ग मीटर विकर्ण के आधे को भुजा मानता है; 28,284 वर्ग मीटर विकर्ण को भुजा से गुणा करता है।",
  "qa-sdt-a-field-crossed-on-its-diagonal", _sdt4,
  opts_hi=["10,000 वर्ग मीटर", "20,000 वर्ग मीटर", "28,284 वर्ग मीटर", "40,000 वर्ग मीटर"])

# ---------------------------------------------------------------- Ratio, Mixtures & Alligation (5)
def _rm1():
    k = F(24000 - 18000, 40 - 25)
    fixed = 18000 - 25 * k
    assert k == 400 and fixed == 8000
    return f"₹{int(fixed + 50 * k):,}"
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "The monthly cost of running a hostel is partly fixed and partly proportional to the number of residents. It is ₹18,000 for 25 residents and ₹24,000 for 40 residents. What will it be for 50 residents?",
  "एक छात्रावास चलाने की मासिक लागत का एक भाग स्थिर है और एक भाग निवासियों की संख्या के अनुपात में बदलता है। 25 निवासियों के लिए यह ₹18,000 और 40 निवासियों के लिए ₹24,000 है। 50 निवासियों के लिए यह कितनी होगी?",
  ["₹27,000", "₹28,000", "₹30,000", "₹36,000"], 1,
  "15 more residents add ₹6,000, so each resident adds ₹400, and the fixed part is 18,000 - 25 × 400 = ₹8,000. For 50 residents the cost is 8,000 + 50 × 400 = ₹28,000. "
  "₹36,000 and ₹30,000 scale the costs for 25 and 40 residents as if all of the cost varied; ₹27,000 adds only half of the ₹6,000 rise for the next 10 residents.",
  "15 अधिक निवासी ₹6,000 जोड़ते हैं, इसलिए हर निवासी ₹400 जोड़ता है, और स्थिर भाग 18,000 - 25 × 400 = ₹8,000 है। 50 निवासियों के लिए लागत 8,000 + 50 × 400 = ₹28,000 है। "
  "₹36,000 और ₹30,000, 25 और 40 निवासियों की लागतों को ऐसे बढ़ाते हैं मानो पूरी लागत बदलती हो; ₹27,000 अगले 10 निवासियों के लिए ₹6,000 की वृद्धि का केवल आधा जोड़ता है।",
  "qa-rm-a-hostel-cost-that-is-partly-fixed", _rm1)

def _rm2():
    ks = [k for k in range(1, 200) if F(2 * k + 20, 3 * k + 20) == F(4, 5) and F(3 * k + 20, 5 * k + 20) == F(5, 7)]
    assert ks == [10]
    return str(10 * ks[0])
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "The numbers of students in three classes are in the ratio 2 : 3 : 5. If 20 students are added to each class, the ratio becomes 4 : 5 : 7. How many students were there in the three classes together at first?",
  "तीन कक्षाओं में विद्यार्थियों की संख्याएँ 2 : 3 : 5 के अनुपात में हैं। यदि हर कक्षा में 20 विद्यार्थी जोड़ दिए जाएँ, तो अनुपात 4 : 5 : 7 हो जाता है। आरंभ में तीनों कक्षाओं में कुल कितने विद्यार्थी थे?",
  ["60", "100", "140", "160"], 1,
  "Let the classes have 2k, 3k and 5k students. Then (2k + 20)/(3k + 20) = 4/5 gives 10k + 100 = 12k + 80, so k = 10: the classes had 20, 30 and 50, which become 40, 50 and 70 -- indeed 4 : 5 : 7. The total at first was 100. "
  "160 is the total after the additions, 60 the number of students added, and 140 adds 20 students to only two of the three classes.",
  "मान लीजिए कक्षाओं में 2k, 3k और 5k विद्यार्थी हैं। तब (2k + 20)/(3k + 20) = 4/5 से 10k + 100 = 12k + 80, अतः k = 10: कक्षाओं में 20, 30 और 50 थे, जो 40, 50 और 70 हो जाते हैं -- सचमुच 4 : 5 : 7। आरंभ में कुल 100 थे। "
  "160 जोड़ने के बाद का कुल है, 60 जोड़े गए विद्यार्थियों की संख्या, और 140 तीन में से केवल दो कक्षाओं में 20-20 विद्यार्थी जोड़ता है।",
  "qa-rm-a-three-term-ratio-after-equal-additions", _rm2)

def _rm3():
    cost = F(2 * 100 + 3 * 120 + 5 * 150, 10)
    assert cost == 131 and F(100 + 120 + 150, 3) * F(6, 5) == 148
    p = cost * F(6, 5)
    return f"₹{float(p):.2f}"
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "Three kinds of tea costing ₹100, ₹120 and ₹150 a kg are mixed in the ratio 2 : 3 : 5 by weight. At what price per kg must the mixture be sold to make a profit of 20 per cent?",
  "₹100, ₹120 और ₹150 प्रति किग्रा वाली तीन प्रकार की चाय भार के अनुसार 2 : 3 : 5 के अनुपात में मिलाई जाती है। 20 प्रतिशत लाभ कमाने के लिए मिश्रण को किस मूल्य प्रति किग्रा पर बेचना होगा?",
  ["₹144.00", "₹148.00", "₹157.20", "₹180.00"], 2,
  "10 kg of the mixture costs 2 × 100 + 3 × 120 + 5 × 150 = ₹1,310, so 1 kg costs ₹131, and a 20 per cent profit needs 131 × 1.2 = ₹157.20 a kg. "
  "₹148.00 is 20 per cent above the simple average of the three prices, which ignores the ratio; ₹144.00 is 20 per cent above the middle price; ₹180.00 is 20 per cent above the dearest tea.",
  "मिश्रण के 10 किग्रा की लागत 2 × 100 + 3 × 120 + 5 × 150 = ₹1,310 है, इसलिए 1 किग्रा की लागत ₹131 है, और 20 प्रतिशत लाभ के लिए 131 × 1.2 = ₹157.20 प्रति किग्रा चाहिए। "
  "₹148.00 तीनों मूल्यों के साधारण औसत से 20 प्रतिशत अधिक है, जो अनुपात को अनदेखा करता है; ₹144.00 बीच वाले मूल्य से 20 प्रतिशत अधिक है; ₹180.00 सबसे महँगी चाय से 20 प्रतिशत अधिक है।",
  "qa-rm-a-blend-of-three-teas", _rm3)

def _rm4():
    bs = [b for b in range(1, 1210) if F(4, 15) * (1210 - b) == F(2, 5) * b]
    assert bs == [484]
    return f"₹{bs[0]}"
N(QA, "Ratio, Mixtures & Alligation", "easy",
  "A and B together have ₹1,210. If 4/15 of A's amount is equal to 2/5 of B's amount, how much does B have?",
  "A और B के पास कुल ₹1,210 हैं। यदि A की राशि का 4/15, B की राशि के 2/5 के बराबर है, तो B के पास कितने हैं?",
  ["₹440", "₹484", "₹605", "₹726"], 1,
  "4A/15 = 2B/5 gives A/B = (2/5) ÷ (4/15) = 3/2, so A : B = 3 : 2 and B has 2/5 of 1,210 = ₹484 (A has ₹726). "
  "₹726 is A's share; ₹605 splits the money equally; ₹440 splits it 4 : 7, a ratio the condition does not give.",
  "4A/15 = 2B/5 से A/B = (2/5) ÷ (4/15) = 3/2, अतः A : B = 3 : 2 और B के पास 1,210 का 2/5 = ₹484 है (A के पास ₹726)। "
  "₹726, A का हिस्सा है; ₹605 राशि को बराबर बाँटता है; ₹440 उसे 4 : 7 में बाँटता है, जो अनुपात शर्त से नहीं निकलता।",
  "qa-rm-a-share-from-equal-fractions", _rm4)

def _rm5():
    cu = F(2, 5) + F(3, 7)
    zn, sn = F(3, 5), F(4, 7)
    m = 35
    assert (cu * m, zn * m, sn * m) == (29, 21, 20)
    return "29 : 21 : 20"
N(QA, "Ratio, Mixtures & Alligation", "hard",
  "One alloy, P, is copper and zinc in the ratio 2 : 3; another, Q, is copper and tin in the ratio 3 : 4. If equal weights of P and Q are melted together, what is the ratio of copper, zinc and tin in the new alloy?",
  "एक मिश्रधातु P, ताँबे और जस्ते से 2 : 3 के अनुपात में बनी है; दूसरी, Q, ताँबे और टिन से 3 : 4 के अनुपात में। यदि P और Q के बराबर भार एक साथ पिघलाए जाएँ, तो नई मिश्रधातु में ताँबे, जस्ते और टिन का अनुपात क्या होगा?",
  ["5 : 3 : 4", "14 : 21 : 20", "29 : 20 : 21", "29 : 21 : 20"], 3,
  "Take 35 kg of each alloy, 35 being divisible by both 5 and 7. P gives 14 kg copper and 21 kg zinc; Q gives 15 kg copper and 20 kg tin. Together: copper 29, zinc 21, tin 20. "
  "5 : 3 : 4 adds the ratio terms as if each alloy were divided into the same number of parts (5 and 7 parts are not equal weights); 14 : 21 : 20 forgets Q's copper; 29 : 20 : 21 swaps zinc and tin.",
  "हर मिश्रधातु का 35 किग्रा लीजिए, क्योंकि 35, 5 और 7 दोनों से विभाज्य है। P से 14 किग्रा ताँबा और 21 किग्रा जस्ता मिलता है; Q से 15 किग्रा ताँबा और 20 किग्रा टिन। कुल मिलाकर: ताँबा 29, जस्ता 21, टिन 20। "
  "5 : 3 : 4 अनुपात के पदों को ऐसे जोड़ता है मानो हर मिश्रधातु बराबर भागों में बँटी हो (5 और 7 भाग बराबर भार नहीं हैं); 14 : 21 : 20, Q का ताँबा भूल जाता है; 29 : 20 : 21 जस्ते और टिन को उलट देता है।",
  "qa-rm-two-alloys-of-three-metals", _rm5)

# ---------------------------------------------------------------- Percentage & Profit-Loss (3)
def _pp1():
    x = F(210000) / (F(10, 11) + F(100, 121))
    assert x == 121000
    return "₹1,21,000"
N(QA, "Percentage & Profit-Loss", "hard",
  "A loan of ₹2,10,000 is to be repaid in two equal annual instalments, the first at the end of the first year, with interest at 10 per cent a year compounded annually. What is the amount of each instalment?",
  "₹2,10,000 का एक ऋण दो बराबर वार्षिक किस्तों में चुकाया जाना है, पहली किस्त पहले वर्ष के अंत में, 10 प्रतिशत वार्षिक चक्रवृद्धि ब्याज के साथ। हर किस्त कितनी है?",
  ["₹1,05,000", "₹1,15,500", "₹1,21,000", "₹1,27,050"], 2,
  "Each instalment x is worth x/1.1 today if paid after one year and x/1.21 if paid after two. The two together must equal the loan: x(1/1.1 + 1/1.21) = 2,10,000, that is x × 2.1/1.21 = 2,10,000, so x = ₹1,21,000. "
  "(Check: after a year the debt is 2,31,000; paying 1,21,000 leaves 1,10,000, which grows to 1,21,000 by the end of the second year.) ₹1,05,000 is half the loan with no interest; ₹1,15,500 and ₹1,27,050 add one and two years' interest to that half.",
  "हर किस्त x का आज का मूल्य x/1.1 है यदि वह एक वर्ष बाद चुकाई जाए, और x/1.21 यदि दो वर्ष बाद। दोनों मिलकर ऋण के बराबर होनी चाहिए: x(1/1.1 + 1/1.21) = 2,10,000, यानी x × 2.1/1.21 = 2,10,000, अतः x = ₹1,21,000। "
  "(जाँच: एक वर्ष बाद ऋण 2,31,000 है; 1,21,000 चुकाने पर 1,10,000 बचते हैं, जो दूसरे वर्ष के अंत तक 1,21,000 हो जाते हैं।) ₹1,05,000 बिना ब्याज के ऋण का आधा है; ₹1,15,500 और ₹1,27,050 उसी आधे में एक और दो वर्षों का ब्याज जोड़ते हैं।",
  "qa-pp-two-equal-instalments-at-compound-interest", _pp1)

def _pp2():
    ps = [p for p in range(1, 401) if F(400, F(4, 5) * p) - F(400, p) == 5]
    assert ps == [20]
    return f"₹{ps[0]}"
N(QA, "Percentage & Profit-Loss", "medium",
  "A fall of 20 per cent in the price of rice lets a family buy 5 kg more rice for ₹400. What was the original price of rice per kg?",
  "चावल के मूल्य में 20 प्रतिशत की गिरावट से एक परिवार ₹400 में 5 किग्रा अधिक चावल ख़रीद पाता है। चावल का मूल मूल्य प्रति किग्रा क्या था?",
  ["₹16", "₹20", "₹25", "₹80"], 1,
  "The fall saves 20 per cent of ₹400 = ₹80, and ₹80 now buys the extra 5 kg, so the new price is ₹16 a kg and the original price 16 ÷ 0.8 = ₹20 a kg (₹400 bought 20 kg before and 25 kg now). "
  "₹16 is the new price, ₹80 the saving and 25 the number of kilograms now bought.",
  "गिरावट से ₹400 का 20 प्रतिशत = ₹80 बचता है, और ₹80 से अब अतिरिक्त 5 किग्रा आता है, इसलिए नया मूल्य ₹16 प्रति किग्रा है और मूल मूल्य 16 ÷ 0.8 = ₹20 प्रति किग्रा (पहले ₹400 में 20 किग्रा आता था, अब 25 किग्रा)। "
  "₹16 नया मूल्य है, ₹80 बचत और 25 अब ख़रीदे जाने वाले किलोग्राम।",
  "qa-pp-a-fall-in-price-that-buys-more", _pp2)

def _pp3():
    xs = [x for x in range(0, 50001, 500) if F(8, 100) * (50000 - x) + F(12, 100) * x == 5400]
    assert xs == [35000]
    return f"₹{xs[0]:,}"
N(QA, "Percentage & Profit-Loss", "medium",
  "₹50,000 is invested, part at 8 per cent and the rest at 12 per cent simple interest a year. If the total interest for one year is ₹5,400, how much was invested at 12 per cent?",
  "₹50,000 का निवेश किया जाता है, कुछ भाग 8 प्रतिशत और शेष 12 प्रतिशत वार्षिक साधारण ब्याज पर। यदि एक वर्ष का कुल ब्याज ₹5,400 है, तो 12 प्रतिशत पर कितना निवेश किया गया?",
  ["₹15,000", "₹25,000", "₹30,000", "₹35,000"], 3,
  "The interest is 5,400/50,000 = 10.8 per cent of the whole. By alligation the two parts are in the ratio (12 - 10.8) : (10.8 - 8) = 1.2 : 2.8 = 3 : 7 between 8 and 12 per cent, so ₹35,000 is at 12 per cent and ₹15,000 at 8 per cent "
  "(check: 1,200 + 4,200 = 5,400). ₹15,000 is the part at 8 per cent; ₹25,000 would give an average of exactly 10 per cent; ₹30,000 gives ₹5,200.",
  "ब्याज पूरी राशि का 5,400/50,000 = 10.8 प्रतिशत है। मिश्रण-नियम (एलिगेशन) से 8 और 12 प्रतिशत वाले भाग (12 - 10.8) : (10.8 - 8) = 1.2 : 2.8 = 3 : 7 के अनुपात में हैं, इसलिए ₹35,000, 12 प्रतिशत पर और ₹15,000, 8 प्रतिशत पर है "
  "(जाँच: 1,200 + 4,200 = 5,400)। ₹15,000, 8 प्रतिशत वाला भाग है; ₹25,000 से औसत ठीक 10 प्रतिशत होता; ₹30,000 से ₹5,200 मिलते हैं।",
  "qa-pp-money-split-between-two-rates", _pp3)

# ---------------------------------------------------------------- Sequences & Series (2)
N(QA, "Sequences & Series", "medium",
  "What is the value of 1² - 2² + 3² - 4² + ... + 19² - 20²?",
  "1² - 2² + 3² - 4² + ... + 19² - 20² का मान क्या है?",
  ["-420", "-210", "-200", "210"], 1,
  "Pair the terms: (2k - 1)² - (2k)² = -(4k - 1) = -[(2k - 1) + 2k]. Adding the ten pairs gives -(1 + 2 + 3 + ... + 20) = -(20 × 21 ÷ 2) = -210. "
  "210 has the wrong sign, since every pair is negative; -420 doubles the sum; -200 counts each pair as -20.",
  "पदों को जोड़ों में लीजिए: (2k - 1)² - (2k)² = -(4k - 1) = -[(2k - 1) + 2k]। दस जोड़ों को जोड़ने पर -(1 + 2 + 3 + ... + 20) = -(20 × 21 ÷ 2) = -210 मिलता है। "
  "210 का चिह्न ग़लत है, क्योंकि हर जोड़ा ऋणात्मक है; -420 योग को दोगुना करता है; -200 हर जोड़े को -20 गिनता है।",
  "qa-ss-a-sum-of-alternating-squares", lambda: str(sum((-1) ** (k + 1) * k * k for k in range(1, 21))))

def _ss2():
    xs = [n for n in range(1, 200) if int(n ** 0.5) ** 2 != n]
    assert 110 - 10 == 100
    return str(xs[99])
N(QA, "Sequences & Series", "hard",
  "The natural numbers that are not perfect squares are written in increasing order: 2, 3, 5, 6, 7, 8, 10, 11, ... What is the 100th number in this list?",
  "वे प्राकृत संख्याएँ जो पूर्ण वर्ग नहीं हैं, बढ़ते क्रम में लिखी जाती हैं: 2, 3, 5, 6, 7, 8, 10, 11, ... इस सूची में 100वीं संख्या कौन-सी है?",
  ["100", "109", "110", "111"], 2,
  "Up to a number N, the list holds N less the number of squares up to N. Up to 110 there are 10 squares (1² to 10²), so the list holds 110 - 10 = 100 numbers, and 110 is not itself a square: it is the 100th. "
  "109 is the 99th (109 - 10 = 99); 100 is a square and so not in the list; 111 is the 101st.",
  "किसी संख्या N तक, सूची में N में से N तक के वर्गों की संख्या घटाने जितनी संख्याएँ होती हैं। 110 तक 10 वर्ग हैं (1² से 10²), इसलिए सूची में 110 - 10 = 100 संख्याएँ हैं, और 110 स्वयं वर्ग नहीं है: वही 100वीं है। "
  "109, 99वीं है (109 - 10 = 99); 100 वर्ग है और इसलिए सूची में नहीं; 111, 101वीं है।",
  "qa-ss-the-100th-number-that-is-not-a-square", _ss2)

# ---------------------------------------------------------------- Permutation & Combination (2)
def _pc1():
    n = sum(1 for k in range(100, 1000) if str(k)[0] < str(k)[1] < str(k)[2])
    assert n == 84 and 9 * 8 * 7 == 504
    return str(n)
N(QA, "Permutation & Combination", "medium",
  "How many three-digit numbers have digits that strictly increase from left to right (such as 147)?",
  "तीन अंकों की कितनी संख्याओं के अंक बाएँ से दाएँ सख़्ती से बढ़ते हैं (जैसे 147)?",
  ["84", "120", "504", "720"], 0,
  "Any choice of three different digits from 1 to 9 can be written in only one increasing order, so the count is the number of such choices: 9C3 = 84. 0 cannot be used, because in increasing order it would come first and leave a two-digit number. "
  "120 = 10C3 wrongly allows 0; 504 = 9 × 8 × 7 counts every order of three different digits, not only the increasing one; 720 = 10 × 9 × 8 also counts orders and allows 0.",
  "1 से 9 तक के तीन अलग अंकों का हर चयन केवल एक बढ़ते क्रम में लिखा जा सकता है, इसलिए संख्या ऐसे चयनों के बराबर है: 9C3 = 84। 0 नहीं लिया जा सकता, क्योंकि बढ़ते क्रम में वह सबसे पहले आएगा और संख्या दो अंकों की रह जाएगी। "
  "120 = 10C3 ग़लती से 0 को शामिल करता है; 504 = 9 × 8 × 7 तीन अलग अंकों के हर क्रम को गिनता है, केवल बढ़ते क्रम को नहीं; 720 = 10 × 9 × 8 क्रम भी गिनता है और 0 भी।",
  "qa-pc-three-digit-numbers-with-rising-digits", _pc1)

def _pc2():
    n = sum(1 for p in permutations(range(4)) if all(p[i] != i for i in range(4)))
    assert n == 9
    return str(n)
N(QA, "Permutation & Combination", "hard",
  "Four letters are written to four different people, and their four envelopes are addressed. In how many ways can the letters be put into the envelopes, one in each, so that no letter goes into its own envelope?",
  "चार अलग-अलग व्यक्तियों को चार पत्र लिखे गए हैं और उनके चार लिफ़ाफ़ों पर पते लिखे गए हैं। पत्रों को लिफ़ाफ़ों में, हर लिफ़ाफ़े में एक, कितने तरीक़ों से रखा जा सकता है कि कोई भी पत्र अपने लिफ़ाफ़े में न जाए?",
  ["6", "8", "9", "23"], 2,
  "Letter A can go into any of the 3 wrong envelopes, say B's. If B's letter then goes into A's envelope, the remaining two must swap: 1 way. If it does not, letters B, C and D must fill envelopes A, C and D with B kept out of A and C, D out of their own: 2 ways. "
  "So each of A's 3 choices allows 1 + 2 = 3 arrangements: 9 in all (by inclusion-exclusion, 24 - 24 + 12 - 4 + 1 = 9). 23 removes only the one arrangement in which every letter is right; 6 = 3! and 8 do not count the cases.",
  "पत्र A, 3 ग़लत लिफ़ाफ़ों में से किसी में भी जा सकता है, मान लीजिए B के लिफ़ाफ़े में। यदि तब B का पत्र A के लिफ़ाफ़े में जाए, तो बचे दो पत्रों को आपस में बदलना होगा: 1 तरीक़ा। यदि न जाए, तो पत्र B, C और D को लिफ़ाफ़े A, C और D भरने हैं, B को A से बाहर और C, D को अपने-अपने से बाहर रखते हुए: 2 तरीक़े। "
  "अतः A के 3 विकल्पों में से हर एक से 1 + 2 = 3 व्यवस्थाएँ बनती हैं: कुल 9 (समावेश-अपवर्जन से, 24 - 24 + 12 - 4 + 1 = 9)। 23 केवल उस एक व्यवस्था को हटाता है जिसमें हर पत्र सही हो; 6 = 3! और 8 स्थितियों को नहीं गिनते।",
  "qa-pc-letters-in-the-wrong-envelopes", _pc2)

# ---------------------------------------------------------------- Geometry & Mensuration (2)
def _gm1():
    R = F(10)
    side_sq = 2 * R * R                      # the square's diagonal is the circle's diameter: side² = 2R²
    r_sq = side_sq / 4                       # the inner circle's radius is half the side
    return f"{int(R * R / r_sq)} : 1"
N(QA, "Geometry & Mensuration", "medium",
  "A square is drawn inside a circle of radius 10 cm with all four of its corners on the circle, and a second circle is drawn inside the square touching all four of its sides. What is the ratio of the area of the larger circle to that of the smaller circle?",
  "10 सेमी त्रिज्या वाले एक वृत्त के भीतर एक वर्ग इस तरह खींचा जाता है कि उसके चारों कोने वृत्त पर हों, और वर्ग के भीतर दूसरा वृत्त उसकी चारों भुजाओं को छूता हुआ खींचा जाता है। बड़े वृत्त के क्षेत्रफल और छोटे वृत्त के क्षेत्रफल का अनुपात क्या है?",
  ["√2 : 1", "2 : 1", "4 : 1", "π : 2"], 1,
  "The square's diagonal is the larger circle's diameter, 20 cm, so its side is 20/√2 = 10√2 cm. The smaller circle's diameter is the side, so its radius is 5√2 cm. The areas are in the ratio of the squares of the radii: 100 : 50 = 2 : 1, whatever the first radius. "
  "√2 : 1 is the ratio of the radii, not of the areas; 4 : 1 takes the smaller radius as half the larger; π : 2 is the ratio of the larger circle's area to the square's.",
  "वर्ग का विकर्ण बड़े वृत्त का व्यास, 20 सेमी है, इसलिए उसकी भुजा 20/√2 = 10√2 सेमी है। छोटे वृत्त का व्यास यही भुजा है, इसलिए उसकी त्रिज्या 5√2 सेमी है। क्षेत्रफल त्रिज्याओं के वर्गों के अनुपात में होते हैं: 100 : 50 = 2 : 1, पहली त्रिज्या चाहे जो हो। "
  "√2 : 1 त्रिज्याओं का अनुपात है, क्षेत्रफलों का नहीं; 4 : 1 छोटी त्रिज्या को बड़ी का आधा मान लेता है; π : 2 बड़े वृत्त और वर्ग के क्षेत्रफलों का अनुपात है।",
  "qa-gm-a-circle-in-a-square-in-a-circle", _gm1)

def _gm2():
    a = 1                                    # the hexagon's side; the triangle's side is 2a for the same perimeter
    tri = F(4 * a * a, 4)                    # area / √3 for an equilateral triangle of side 2a: (√3/4)(2a)²
    hexa = 6 * F(a * a, 4)                   # six equilateral triangles of side a
    r = tri / hexa
    assert r == F(2, 3)
    return f"{r.numerator} : {r.denominator}"
N(QA, "Geometry & Mensuration", "hard",
  "An equilateral triangle and a regular hexagon have the same perimeter. What is the ratio of the area of the triangle to the area of the hexagon?",
  "एक समबाहु त्रिभुज और एक सम षट्भुज का परिमाप समान है। त्रिभुज के क्षेत्रफल और षट्भुज के क्षेत्रफल का अनुपात क्या है?",
  ["1 : 1", "1 : 2", "3 : 2", "2 : 3"], 3,
  "If the hexagon's side is a, the triangle's side is 2a (6a = 3 × 2a). The triangle's area is (√3/4)(2a)² = √3a². The hexagon is six equilateral triangles of side a, so its area is 6 × (√3/4)a² = (3√3/2)a². "
  "The ratio is √3 : 3√3/2 = 2 : 3. 1 : 1 assumes that equal perimeters mean equal areas; 1 : 2 compares the sides; 3 : 2 turns the right ratio round.",
  "यदि षट्भुज की भुजा a है, तो त्रिभुज की भुजा 2a है (6a = 3 × 2a)। त्रिभुज का क्षेत्रफल (√3/4)(2a)² = √3a² है। षट्भुज भुजा a वाले छह समबाहु त्रिभुजों से बना है, इसलिए उसका क्षेत्रफल 6 × (√3/4)a² = (3√3/2)a² है। "
  "अनुपात √3 : 3√3/2 = 2 : 3 है। 1 : 1 मान लेता है कि बराबर परिमाप का अर्थ बराबर क्षेत्रफल है; 1 : 2 भुजाओं की तुलना करता है; 3 : 2 सही अनुपात को उलट देता है।",
  "qa-gm-a-triangle-and-a-hexagon-of-equal-perimeter", _gm2)

# ---------------------------------------------------------------- Time & Work (2)
def _tw1():
    t = next(F(k, 60) for k in range(1, 300) if 1 - F(k, 60) / 5 == 2 * (1 - F(k, 60) / 4))
    assert t == F(10, 3)
    h, m = divmod(int(t * 60), 60)
    return f"{h} h {m} min"
N(QA, "Time & Work", "hard",
  "Two candles of the same length are lit at the same time. The first burns out in 4 hours and the second in 5 hours, each at a steady rate. After how long will the second candle be twice as long as the first?",
  "समान लंबाई की दो मोमबत्तियाँ एक ही समय पर जलाई जाती हैं। पहली 4 घंटे में और दूसरी 5 घंटे में पूरी जल जाती है, दोनों एक समान दर से। कितने समय बाद दूसरी मोमबत्ती की लंबाई पहली की दोगुनी होगी?",
  ["2 h 30 min", "3 h", "3 h 20 min", "3 h 45 min"], 2,
  "After t hours the lengths left are L(1 - t/4) and L(1 - t/5). Setting 1 - t/5 = 2(1 - t/4) gives t/2 - t/5 = 1, so 3t/10 = 1 and t = 10/3 hours = 3 h 20 min. Then the first candle has 1/6 of its length left and the second 1/3. "
  "3 h leaves 1/4 and 2/5, a ratio of 8 : 5; 2 h 30 min and 3 h 45 min do not give 2 : 1 either.",
  "t घंटे बाद बची लंबाइयाँ L(1 - t/4) और L(1 - t/5) हैं। 1 - t/5 = 2(1 - t/4) रखने पर t/2 - t/5 = 1, अतः 3t/10 = 1 और t = 10/3 घंटे = 3 घंटे 20 मिनट। तब पहली मोमबत्ती की 1/6 लंबाई बचती है और दूसरी की 1/3। "
  "3 घंटे पर 1/4 और 2/5 बचते हैं, अनुपात 8 : 5; 2 घंटे 30 मिनट और 3 घंटे 45 मिनट भी 2 : 1 नहीं देते।",
  "qa-tw-two-candles-that-burn-at-different-rates", _tw1,
  opts_hi=["2 घंटे 30 मिनट", "3 घंटे", "3 घंटे 20 मिनट", "3 घंटे 45 मिनट"])

def _tw2():
    ts = [t for t in range(1, 200) if F(15, 20) + F(10, t) == 1]
    assert ts == [40]
    return f"{ts[0]} min"
N(QA, "Time & Work", "medium",
  "A tap fills an empty tank in 20 minutes. Five minutes after it is turned on, a second tap is also turned on, and the tank is full 5 minutes sooner than the first tap alone would have filled it. How long would the second tap alone take to fill the tank?",
  "एक नल ख़ाली टंकी को 20 मिनट में भरता है। उसे खोलने के पाँच मिनट बाद दूसरा नल भी खोल दिया जाता है, और टंकी उससे 5 मिनट पहले भर जाती है जितने में अकेला पहला नल उसे भरता। अकेला दूसरा नल टंकी को कितने समय में भरेगा?",
  ["30 min", "40 min", "45 min", "60 min"], 1,
  "The tank is full after 15 minutes, so the first tap runs for 15 minutes and fills 15/20 = 3/4 of it. The second tap runs for the last 10 minutes and fills the other 1/4, so alone it would take 40 minutes. "
  "30 min assumes that the second tap runs for 15 minutes; 60 min assumes that it fills 1/4 in 15 minutes; 45 min has no basis.",
  "टंकी 15 मिनट में भर जाती है, इसलिए पहला नल 15 मिनट चलता है और उसका 15/20 = 3/4 भाग भरता है। दूसरा नल अंतिम 10 मिनट चलता है और बचा 1/4 भाग भरता है, इसलिए अकेले उसे 40 मिनट लगेंगे। "
  "30 मिनट मान लेता है कि दूसरा नल 15 मिनट चलता है; 60 मिनट मान लेता है कि वह 15 मिनट में 1/4 भरता है; 45 मिनट का कोई आधार नहीं।",
  "qa-tw-a-second-tap-turned-on-late", _tw2,
  opts_hi=["30 मिनट", "40 मिनट", "45 मिनट", "60 मिनट"])

# ---------------------------------------------------------------- Puzzle Hybrid (4)
def _ph1():
    n = 0
    for s in range(0, 24 * 3600 * 2):                       # half-second steps through a day
        t = s / 2
        m = (t / 10) % 360                                    # minute hand: 360° in 3600 s
        h = (t / 120) % 360                                   # hour hand: 360° in 43200 s
        prev = ((t - 0.5) / 10 - (t - 0.5) / 120) % 180
        cur = (t / 10 - t / 120) % 180
        if prev < 90 <= cur:
            n += 1
    assert n == 44 and m >= 0 and h >= 0
    return str(n)
N(QA, "Puzzle Hybrid", "medium",
  "How many times in a day of 24 hours are the hour hand and the minute hand of a clock at right angles to each other?",
  "24 घंटे के एक दिन में घड़ी की घंटे की सुई और मिनट की सुई कितनी बार एक-दूसरे से समकोण पर होती हैं?",
  ["22", "24", "44", "48"], 2,
  "The minute hand gains a full turn on the hour hand 11 times in 12 hours, not 12 times, because the hour hand moves too. In each such turn the hands are at right angles twice, so there are 22 right angles in 12 hours and 44 in a day. "
  "48 assumes two in every hour; it overcounts because, for example, the right angle of 3 o'clock serves both the hour from 2 to 3 and the hour from 3 to 4. 22 is the count for 12 hours; 24 has no basis.",
  "मिनट की सुई 12 घंटे में घंटे की सुई से 11 बार पूरा चक्कर आगे निकलती है, 12 बार नहीं, क्योंकि घंटे की सुई भी चलती है। हर ऐसे चक्कर में सुइयाँ दो बार समकोण पर होती हैं, इसलिए 12 घंटे में 22 समकोण होते हैं और एक दिन में 44। "
  "48 हर घंटे में दो मान लेता है; यह अधिक गिनता है क्योंकि, उदाहरण के लिए, 3 बजे का समकोण 2 से 3 और 3 से 4 दोनों घंटों में गिन लिया जाता है। 22, 12 घंटों की संख्या है; 24 का कोई आधार नहीं।",
  "qa-ph-right-angles-of-a-clock-in-a-day", _ph1)

def _ph2():
    m = [0]
    for _ in range(5):
        m.append(2 * m[-1] + 1)
    return str(m[5])
N(QA, "Puzzle Hybrid", "hard",
  "Five discs of different sizes are stacked on one of three pegs, the largest at the bottom and each disc smaller than the one below it. They must be moved to another peg one disc at a time, and a disc may never be placed on a smaller one. What is the least number of moves needed?",
  "अलग-अलग आकार की पाँच चकतियाँ तीन खूँटियों में से एक पर रखी हैं, सबसे बड़ी नीचे और हर चकती अपने नीचे वाली से छोटी। उन्हें एक बार में एक चकती करके दूसरी खूँटी पर ले जाना है, और कोई चकती कभी अपने से छोटी चकती पर नहीं रखी जा सकती। कम से कम कितनी चालें चाहिए?",
  ["15", "16", "31", "32"], 2,
  "To move the largest disc, the four above it must first be moved to the third peg; then the largest moves once; then the four go back on top of it. So m(n) = 2m(n - 1) + 1, with m(1) = 1: m(2) = 3, m(3) = 7, m(4) = 15, m(5) = 31 = 2⁵ - 1. "
  "32 = 2⁵ forgets the minus one; 15 is the number for four discs, and 16 = 2⁴.",
  "सबसे बड़ी चकती को हटाने के लिए पहले उसके ऊपर की चार चकतियों को तीसरी खूँटी पर ले जाना होगा; फिर सबसे बड़ी एक बार चलती है; फिर चारों उसके ऊपर लौटती हैं। अतः m(n) = 2m(n - 1) + 1, जहाँ m(1) = 1: m(2) = 3, m(3) = 7, m(4) = 15, m(5) = 31 = 2⁵ - 1। "
  "32 = 2⁵ में एक घटाना भूल जाता है; 15 चार चकतियों की संख्या है, और 16 = 2⁴।",
  "qa-ph-the-least-moves-for-five-discs", _ph2)

def _ph3():
    centres = set()
    for p in permutations(range(1, 10)):
        g = [p[0:3], p[3:6], p[6:9]]
        lines = [sum(r) for r in g] + [sum(g[i][j] for i in range(3)) for j in range(3)] + [p[0] + p[4] + p[8], p[2] + p[4] + p[6]]
        if len(set(lines)) == 1:
            centres.add(p[4])
    assert centres == {5}
    return "5"
N(QA, "Puzzle Hybrid", "medium",
  "The numbers 1 to 9 are placed in a 3 × 3 grid, one in each cell, so that every row, every column and both diagonals add up to the same total. Which number must be in the centre cell?",
  "1 से 9 तक की संख्याएँ एक 3 × 3 जाल में, हर खाने में एक, इस तरह रखी जाती हैं कि हर पंक्ति, हर स्तंभ और दोनों विकर्णों का योग समान हो। बीच के खाने में कौन-सी संख्या होनी चाहिए?",
  ["1", "3", "5", "9"], 2,
  "The nine numbers add up to 45, so each of the three rows adds up to 15. The middle row, the middle column and the two diagonals all pass through the centre; together they cover every cell once and the centre three extra times, so 4 × 15 = 45 + 3c and c = 5. "
  "No other number can be in the centre of such a square, which is why 1, 3 and 9 are ruled out.",
  "नौ संख्याओं का योग 45 है, इसलिए तीनों पंक्तियों में से हर एक का योग 15 है। बीच की पंक्ति, बीच का स्तंभ और दोनों विकर्ण केंद्र से होकर जाते हैं; मिलकर वे हर खाने को एक बार और केंद्र को तीन बार अतिरिक्त ढकते हैं, इसलिए 4 × 15 = 45 + 3c और c = 5। "
  "ऐसे वर्ग के केंद्र में कोई और संख्या नहीं हो सकती, इसीलिए 1, 3 और 9 बाहर हो जाते हैं।",
  "qa-ph-the-centre-of-a-magic-square", _ph3)

def _ph4():
    people, i = list(range(1, 11)), 1
    while len(people) > 1:
        people.pop(i)
        i = (i + 1) % len(people)
    return str(people[0])
N(QA, "Puzzle Hybrid", "hard",
  "Ten people stand in a circle, numbered 1 to 10 in order. Going round the circle from person 1, every second person is asked to leave -- first 2, then 4, and so on, the counting continuing round the circle -- until only one person is left. What is that person's number?",
  "दस व्यक्ति एक घेरे में क्रम से 1 से 10 तक की संख्याओं के साथ खड़े हैं। व्यक्ति 1 से घेरे में आगे बढ़ते हुए हर दूसरे व्यक्ति को बाहर जाने को कहा जाता है -- पहले 2, फिर 4, और इसी तरह, गिनती घेरे में घूमती रहती है -- जब तक केवल एक व्यक्ति न बचे। उस व्यक्ति की संख्या क्या है?",
  ["1", "3", "4", "5"], 3,
  "In the first round 2, 4, 6, 8 and 10 leave. The count then passes 1, so the next to leave are 3 and 7, leaving 1, 5 and 9; it passes 9 and removes 1, then passes 5 and removes 9. Person 5 is left. "
  "1 and 3 leave in the second round, and 4 in the first.",
  "पहले दौर में 2, 4, 6, 8 और 10 बाहर जाते हैं। फिर गिनती 1 को छोड़ती है, इसलिए अगले बाहर जाने वाले 3 और 7 हैं, और 1, 5 और 9 बचते हैं; गिनती 9 को छोड़कर 1 को हटाती है, फिर 5 को छोड़कर 9 को। व्यक्ति 5 बचता है। "
  "1 और 3 दूसरे दौर में बाहर जाते हैं, और 4 पहले दौर में।",
  "qa-ph-the-last-person-left-in-a-circle", _ph4)

# ---------------------------------------------------------------- the data-sufficiency block's two Quant items
def _ds1():
    costs = range(1, 1200)
    s1 = {F(1200 - c_, c_) for c_ in costs}                                      # I: sold for ₹1,200; cost unknown
    s2 = {F(F(9, 8) * c_ + 75 - c_, c_) for c_ in range(1, 3000)}                # II: 1.125 C = S - 75
    both = {F(1200 - c_, c_) for c_ in costs if F(9, 8) * c_ == 1200 - 75}
    assert both == {F(1, 5)}
    return _ds(s1, s2, both)
DS(QA, "hard",
   "What was the shopkeeper's percentage profit on an article?",
   "एक वस्तु पर दुकानदार का प्रतिशत लाभ क्या था?",
   "He sold it for ₹1,200.", "उसने उसे ₹1,200 में बेचा।",
   "Had he bought it for 10 per cent less and sold it for ₹75 less, his profit would have been 25 per cent.",
   "यदि उसने उसे 10 प्रतिशत कम में ख़रीदा होता और ₹75 कम में बेचा होता, तो उसका लाभ 25 प्रतिशत होता।",
   2,
   "Statement I gives the selling price but not the cost. Statement II gives one equation in two unknowns: 0.9C × 1.25 = S - 75, that is 1.125C = S - 75, which many pairs satisfy. "
   "Together, 1.125C = 1,125, so C = ₹1,000 and the profit is 200/1,000 = 20 per cent. Both statements are needed.",
   "कथन I विक्रय मूल्य देता है पर लागत नहीं। कथन II दो अज्ञातों में एक समीकरण देता है: 0.9C × 1.25 = S - 75, यानी 1.125C = S - 75, जिसे कई युग्म संतुष्ट करते हैं। "
   "दोनों साथ: 1.125C = 1,125, अतः C = ₹1,000 और लाभ 200/1,000 = 20 प्रतिशत। दोनों कथन ज़रूरी हैं।",
   "qa-ds-a-profit-from-a-price-and-a-what-if", _ds1)

def _ds2():
    ns = range(1, 3001)
    s1 = {n % 15 for n in ns if n % 30 == 7}
    s2 = {n % 15 for n in ns if n % 3 == 1}
    both = {n % 15 for n in ns if n % 30 == 7 and n % 3 == 1}
    assert s1 == {7} and s2 == {1, 4, 7, 10, 13}
    return _ds(s1, s2, both)
DS(QA, "medium",
   "What is the remainder when the natural number N is divided by 15?",
   "प्राकृत संख्या N को 15 से भाग देने पर शेषफल क्या है?",
   "When N is divided by 30, the remainder is 7.", "N को 30 से भाग देने पर शेषफल 7 है।",
   "When N is divided by 3, the remainder is 1.", "N को 3 से भाग देने पर शेषफल 1 है।",
   0,
   "Statement I: N = 30k + 7, and since 30 is a multiple of 15, N leaves the same remainder as 7 on division by 15 -- sufficient. Statement II alone allows remainders 1, 4, 7, 10 and 13 (N = 1, 4, 7, 10, 13, ...) -- not sufficient. "
   "So one statement alone answers the question and the other does not.",
   "कथन I: N = 30k + 7, और चूँकि 30, 15 का गुणज है, 15 से भाग देने पर N वही शेषफल देता है जो 7 -- पर्याप्त। कथन II अकेला शेषफल 1, 4, 7, 10 और 13 की अनुमति देता है (N = 1, 4, 7, 10, 13, ...) -- पर्याप्त नहीं। "
   "अतः एक कथन अकेले प्रश्न का उत्तर देता है और दूसरा नहीं।",
   "qa-ds-a-remainder-by-15-from-a-remainder-by-30", _ds2)
