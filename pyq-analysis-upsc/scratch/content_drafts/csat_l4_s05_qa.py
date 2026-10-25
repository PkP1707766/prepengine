# -*- coding: utf-8 -*-
"""CSAT Level 4 · Simulator 5 -- Quantitative Aptitude (34 items: 32 in the Quant slots, 2 in the data-sufficiency block).

Layout B, the 2025 shape of the paper. Exam-level mix (8 easy / 16 medium / 10 hard), with none of the shapes of
Levels 1-3 or Simulators 1-4: the squares between 1,000 and 2,000, 17²³ divided by 16, three-digit multiples of 13, two
sums of square roots compared, 30 as a sum of two primes, 1001/1547 in lowest terms, the product of the factors of 12,
Kaprekar's routine, 1 to 100 without the multiples of 3; a speedometer that reads high, cycling instead of
walking, a moving walkway, stops between the stages; shares that differ by fixed amounts, a scale model's hold, fuel
economy over a mixed trip, teachers needed for a lower ratio; a coupon before or after a discount, water boiled off a
salt solution, a stock sold in three lots; a sequence that describes the term before it, the place of 768 in a GP; a
captain and a vice-captain, triangles inside a hexagon with no side on it, the average result of a dice game; the area
of a ring, the walls of a room; five printers and five pages, longer days at a lower rate; a lift timed between floors,
a magic triangle, three children's ages from their product; and two data-sufficiency items. Every key is worked out in
code by check()."""
from fractions import Fraction as F
from itertools import combinations, permutations, product
import math
import csat_common as c
from csat_common import N, T, DS, QA

def _ds(s1, s2, both):
    alone = (len(set(s1)) == 1, len(set(s2)) == 1)
    return "b" if all(alone) else "a" if any(alone) else "c" if len(set(both)) == 1 else "d"

def indian(n):
    t = str(n); head, tail = t[:-3], t[-3:]
    pairs = []
    while head:
        pairs.insert(0, head[-2:]); head = head[:-2]
    return ",".join(pairs + [tail])

# ---------------------------------------------------------------- Number Theory (9)
def _nt1():
    sq = [k * k for k in range(1, 100) if 1000 < k * k < 2000]
    assert sq[0] == 32 * 32 and sq[-1] == 44 * 44
    return str(len(sq))
N(QA, "Number Theory", "easy",
  "How many perfect squares lie between 1,000 and 2,000?",
  "1,000 और 2,000 के बीच कितने पूर्ण वर्ग हैं?",
  ["13", "14", "15", "16"], 0,
  "31² = 961 is below 1,000 and 32² = 1,024 is the first square above it; 44² = 1,936 is the last below 2,000, since 45² = 2,025. The squares are 32² to 44²: 44 - 32 + 1 = 13 of them. "
  "14 counts 45² = 2,025 as well, which is over 2,000; 15 also counts 31² = 961, which is under 1,000; 16 has no basis.",
  "31² = 961, 1,000 से नीचे है और 32² = 1,024 उसके ऊपर पहला वर्ग है; 44² = 1,936, 2,000 से नीचे अंतिम है, क्योंकि 45² = 2,025। वर्ग 32² से 44² तक हैं: 44 - 32 + 1 = 13। "
  "14, 45² = 2,025 को भी गिनता है, जो 2,000 से ऊपर है; 15, 31² = 961 को भी गिनता है, जो 1,000 से नीचे है; 16 का कोई आधार नहीं।",
  "qa-nt-the-squares-between-1000-and-2000", _nt1)

def _nt2():
    return str(pow(17, 23, 16))
N(QA, "Number Theory", "easy",
  "What is the remainder when 17²³ is divided by 16?",
  "17²³ को 16 से भाग देने पर शेषफल क्या है?",
  ["1", "7", "15", "16"], 0,
  "17 = 16 + 1, so 17 leaves remainder 1 on division by 16, and so does every power of it: 1 × 1 × ... × 1 = 1. "
  "7 is the last digit of 17, which has nothing to do with division by 16; 15 would be right for 15²³ or for an odd power of a number one less than a multiple of 16; and a remainder on division by 16 can never be 16.",
  "17 = 16 + 1, इसलिए 17 को 16 से भाग देने पर शेष 1 बचता है, और उसकी हर घात के साथ भी: 1 × 1 × ... × 1 = 1। "
  "7, 17 का अंतिम अंक है, जिसका 16 से भाग से कोई संबंध नहीं; 15 तब सही होता जब संख्या 16 के गुणज से एक कम हो और घात विषम; और 16 से भाग देने पर शेष कभी 16 नहीं हो सकता।",
  "qa-nt-17-to-the-23rd-divided-by-16", _nt2)

def _nt3():
    n = sum(1 for k in range(100, 1000) if k % 13 == 0)
    assert n == 999 // 13 - 99 // 13
    return str(n)
N(QA, "Number Theory", "medium",
  "How many three-digit numbers are divisible by 13?",
  "तीन अंकों की कितनी संख्याएँ 13 से विभाज्य हैं?",
  ["68", "69", "70", "76"], 1,
  "The multiples of 13 up to 999 number 999 ÷ 13 = 76 (with remainder), and those up to 99 number 7. So the three-digit ones are 76 - 7 = 69, from 104 = 13 × 8 to 988 = 13 × 76. "
  "76 counts the multiples from 13 itself; 68 is (988 - 104) ÷ 13, which forgets to count the first one; 70 has no basis.",
  "999 तक 13 के गुणज 999 ÷ 13 = 76 (शेष सहित) हैं, और 99 तक 7। इसलिए तीन अंकों वाले 76 - 7 = 69 हैं, 104 = 13 × 8 से 988 = 13 × 76 तक। "
  "76, स्वयं 13 से गुणज गिनता है; 68, (988 - 104) ÷ 13 है, जो पहले गुणज को गिनना भूल जाता है; 70 का कोई आधार नहीं।",
  "qa-nt-three-digit-multiples-of-13", _nt3)

def _nt4():
    a = (5 ** 0.5 + 3 ** 0.5) ** 2
    b = (6 ** 0.5 + 2 ** 0.5) ** 2
    assert abs(a - (8 + 2 * 15 ** 0.5)) < 1e-9 and abs(b - (8 + 2 * 12 ** 0.5)) < 1e-9 and a > b
    return "√5 + √3"
T(QA, "Number Theory", "medium",
  "Which is the greater of √5 + √3 and √6 + √2?",
  "√5 + √3 और √6 + √2 में से कौन-सा बड़ा है?",
  ["√5 + √3", "√6 + √2", "They are equal", "It cannot be told without working out each root"],
  ["√5 + √3", "√6 + √2", "दोनों बराबर हैं", "हर मूल निकाले बिना नहीं बताया जा सकता"],
  0,
  "Both sums are positive, so compare their squares. (√5 + √3)² = 5 + 3 + 2√15 = 8 + 2√15, and (√6 + √2)² = 6 + 2 + 2√12 = 8 + 2√12. Since 15 > 12, √5 + √3 is the greater (about 3.97 against 3.86). "
  "Both sums add numbers whose total under the roots is 8, which tempts one to call them equal; and squaring settles it without working out any root.",
  "दोनों योग धनात्मक हैं, इसलिए उनके वर्गों की तुलना कीजिए। (√5 + √3)² = 5 + 3 + 2√15 = 8 + 2√15, और (√6 + √2)² = 6 + 2 + 2√12 = 8 + 2√12। चूँकि 15 > 12, √5 + √3 बड़ा है (लगभग 3.97 बनाम 3.86)। "
  "दोनों योगों में मूलों के भीतर की संख्याओं का जोड़ 8 है, जो उन्हें बराबर कहने को लुभाता है; और वर्ग करने से बिना कोई मूल निकाले बात तय हो जाती है।",
  "qa-nt-two-sums-of-square-roots-compared", pos=3, check=_nt4)

def _nt5():
    isprime = lambda n: n > 1 and all(n % d for d in range(2, math.isqrt(n) + 1))
    ways = [(p, 30 - p) for p in range(2, 16) if isprime(p) and isprime(30 - p)]
    assert ways == [(7, 23), (11, 19), (13, 17)]
    return str(len(ways))
N(QA, "Number Theory", "medium",
  "In how many ways can 30 be written as the sum of two prime numbers, if the order of the two does not matter?",
  "30 को दो अभाज्य संख्याओं के योग के रूप में कितने तरीक़ों से लिखा जा सकता है, यदि दोनों का क्रम मायने न रखे?",
  ["1", "2", "3", "6"], 2,
  "Try each prime up to 15 and see whether 30 minus it is prime: 7 + 23, 11 + 19 and 13 + 17 work, while 2, 3 and 5 leave 28, 27 and 25, none of them prime. That is 3 ways. "
  "1 + 29 does not count, since 1 is not a prime, and 15 + 15 fails because 15 is not prime; 6 counts each pair twice, in both orders; 2 misses one pair.",
  "15 तक की हर अभाज्य संख्या लेकर देखिए कि 30 में से उसे घटाने पर अभाज्य बचता है या नहीं: 7 + 23, 11 + 19 और 13 + 17 चलते हैं, जबकि 2, 3 और 5 से 28, 27 और 25 बचते हैं, जिनमें कोई अभाज्य नहीं। यानी 3 तरीक़े। "
  "1 + 29 नहीं गिना जाता, क्योंकि 1 अभाज्य नहीं है, और 15 + 15 विफल है क्योंकि 15 अभाज्य नहीं; 6 हर जोड़े को दोनों क्रमों में दो बार गिनता है; 2 एक जोड़ा छोड़ देता है।",
  "qa-nt-thirty-as-a-sum-of-two-primes", _nt5)

def _nt6():
    f = F(1001, 1547)
    assert 1001 == 7 * 11 * 13 and 1547 == 7 * 13 * 17
    return f"{f.numerator}/{f.denominator}"
N(QA, "Number Theory", "medium",
  "What is the fraction 1001/1547 in its lowest terms?",
  "भिन्न 1001/1547 अपने न्यूनतम रूप में क्या है?",
  ["7/13", "7/11", "11/17", "13/17"], 2,
  "1001 = 7 × 11 × 13 and 1547 = 7 × 13 × 17. Cancelling the common 7 and 13 leaves 11/17. "
  "7/13 and 13/17 cancel the wrong factors; 7/11 keeps a 7 that both numbers share and should have been cancelled. (The options are arranged in order of size.)",
  "1001 = 7 × 11 × 13 और 1547 = 7 × 13 × 17। साझा 7 और 13 को काटने पर 11/17 बचता है। "
  "7/13 और 13/17 ग़लत गुणनखंड काटते हैं; 7/11 उस 7 को बनाए रखता है जो दोनों संख्याओं में साझा है और कटना चाहिए था। (विकल्प आकार के क्रम में रखे गए हैं।)",
  "qa-nt-1001-over-1547-in-lowest-terms", _nt6)

def _nt7():
    divs = [d for d in range(1, 13) if 12 % d == 0]
    prod = 1
    for d in divs:
        prod *= d
    assert divs == [1, 2, 3, 4, 6, 12] and prod == 12 ** 3 and sum(divs) == 28
    return indian(prod)
N(QA, "Number Theory", "hard",
  "What is the product of all the factors of 12, including 1 and 12 itself?",
  "1 और स्वयं 12 सहित, 12 के सभी गुणनखंडों का गुणनफल क्या है?",
  ["28", "144", "864", "1,728"], 3,
  "The factors are 1, 2, 3, 4, 6 and 12. They pair off as 1 × 12, 2 × 6 and 3 × 4, and each pair multiplies to 12, so the product is 12 × 12 × 12 = 1,728. "
  "28 is the sum of the factors, not their product; 144 = 12² counts only two of the three pairs; 864 has no basis.",
  "गुणनखंड 1, 2, 3, 4, 6 और 12 हैं। वे 1 × 12, 2 × 6 और 3 × 4 के जोड़ों में बँटते हैं, और हर जोड़े का गुणनफल 12 है, इसलिए गुणनफल 12 × 12 × 12 = 1,728 है। "
  "28 गुणनखंडों का योग है, गुणनफल नहीं; 144 = 12², तीन में से केवल दो जोड़े गिनता है; 864 का कोई आधार नहीं।",
  "qa-nt-the-product-of-the-factors-of-12", _nt7)

def _nt8():
    n, steps = 3524, 0
    while n != 6174:
        d = f"{n:04d}"
        n = int("".join(sorted(d, reverse=True))) - int("".join(sorted(d)))
        steps += 1
    return str(steps)
N(QA, "Number Theory", "hard",
  "Take a four-digit number whose digits are not all the same. Arrange its digits in descending order and in ascending order, and subtract the smaller of the two numbers from the larger. Repeat this with each result, keeping any zero as a digit (so that 378 is treated as 0378). Starting from 3524, after how many subtractions does the result first become 6174?",
  "चार अंकों की ऐसी संख्या लीजिए जिसके सभी अंक एक जैसे न हों। उसके अंकों को घटते क्रम में और बढ़ते क्रम में रखिए, और दोनों संख्याओं में से छोटी को बड़ी में से घटाइए। हर परिणाम के साथ यही दोहराइए, किसी भी शून्य को अंक मानते हुए (ताकि 378 को 0378 माना जाए)। 3524 से शुरू करने पर कितने घटावों के बाद परिणाम पहली बार 6174 बनता है?",
  ["1", "2", "3", "4"], 2,
  "5432 - 2345 = 3087; then 8730 - 0378 = 8352; then 8532 - 2358 = 6174. So 6174 appears after 3 subtractions -- and stays, since 7641 - 1467 = 6174 again. This is Kaprekar's routine, named after the Indian mathematician D. R. Kaprekar. "
  "2 stops one step short, at 8352; 4 counts one step past 6174; 1 has no basis.",
  "5432 - 2345 = 3087; फिर 8730 - 0378 = 8352; फिर 8532 - 2358 = 6174। अतः 6174, 3 घटावों के बाद आता है -- और बना रहता है, क्योंकि 7641 - 1467 = 6174 फिर से। यह काप्रेकर की प्रक्रिया है, जिसका नाम भारतीय गणितज्ञ द. रा. काप्रेकर के नाम पर है। "
  "2 एक चरण पहले, 8352 पर, रुक जाता है; 4, 6174 के बाद एक चरण और गिनता है; 1 का कोई आधार नहीं।",
  "qa-nt-kaprekar-s-routine", _nt8)

def _nt9():
    s = sum(n for n in range(1, 101) if n % 3)
    assert sum(range(1, 101)) - 3 * sum(range(1, 34)) == s
    return indian(s)
N(QA, "Number Theory", "hard",
  "What is the sum of all the whole numbers from 1 to 100 that are not multiples of 3?",
  "1 से 100 तक की उन सभी पूर्ण संख्याओं का योग क्या है जो 3 के गुणज नहीं हैं?",
  ["1,683", "3,333", "3,367", "5,050"], 2,
  "The numbers from 1 to 100 add up to 5,050. The multiples of 3 among them are 3, 6, ..., 99, that is 3 × (1 + 2 + ... + 33) = 3 × 561 = 1,683. Taking these away leaves 5,050 - 1,683 = 3,367. "
  "1,683 is the sum of the multiples, not of the rest; 5,050 is the sum of all the numbers; 3,333 has no basis.",
  "1 से 100 तक की संख्याओं का योग 5,050 है। उनमें 3 के गुणज 3, 6, ..., 99 हैं, यानी 3 × (1 + 2 + ... + 33) = 3 × 561 = 1,683। इन्हें घटाने पर 5,050 - 1,683 = 3,367 बचता है। "
  "1,683 गुणजों का योग है, बाक़ी का नहीं; 5,050 सभी संख्याओं का योग है; 3,333 का कोई आधार नहीं।",
  "qa-nt-1-to-100-without-the-multiples-of-3", _nt9)

# ---------------------------------------------------------------- Speed-Distance-Time (4)
def _sdt1():
    true_speed = F(66) / F(11, 10)
    assert true_speed == 60
    return f"{int(true_speed * 2)} km"
N(QA, "Speed-Distance-Time", "hard",
  "A car's speedometer shows a speed 10 per cent higher than the car's true speed. The driver keeps the needle steady at 66 km/h for 2 hours. How far does the car actually travel?",
  "एक गाड़ी का स्पीडोमीटर गाड़ी की वास्तविक चाल से 10 प्रतिशत अधिक चाल दिखाता है। चालक 2 घंटे तक सुई को 66 किमी/घंटा पर स्थिर रखता है। गाड़ी वास्तव में कितनी दूरी तय करती है?",
  ["118.8 km", "120 km", "132 km", "145.2 km"], 1,
  "The reading is 110 per cent of the true speed, so the true speed is 66 ÷ 1.1 = 60 km/h, and in 2 hours the car covers 120 km. "
  "118.8 km takes 10 per cent off the reading (66 × 0.9 = 59.4), but the 10 per cent is of the true speed, not of the reading; 132 km trusts the reading; 145.2 km adds 10 per cent instead of removing it.",
  "पाठ्यांक वास्तविक चाल का 110 प्रतिशत है, इसलिए वास्तविक चाल 66 ÷ 1.1 = 60 किमी/घंटा है, और 2 घंटों में गाड़ी 120 किमी चलती है। "
  "118.8 किमी पाठ्यांक में से 10 प्रतिशत घटाता है (66 × 0.9 = 59.4), पर 10 प्रतिशत वास्तविक चाल का है, पाठ्यांक का नहीं; 132 किमी पाठ्यांक पर भरोसा करता है; 145.2 किमी 10 प्रतिशत हटाने के बजाय जोड़ता है।",
  "qa-sdt-a-speedometer-that-reads-high", _sdt1,
  opts_hi=["118.8 किमी", "120 किमी", "132 किमी", "145.2 किमी"])

def _sdt2():
    km = F(4) * F(30, 60)
    cycle_min = km / 12 * 60
    assert km == 2 and cycle_min == 10
    return f"{int(30 - cycle_min)} minutes"
N(QA, "Speed-Distance-Time", "easy",
  "A clerk who walks at 4 km/h takes 30 minutes to reach the office. How much time would the clerk save by cycling there at 12 km/h instead?",
  "4 किमी/घंटा से चलने वाला एक लिपिक दफ़्तर पहुँचने में 30 मिनट लेता है। यदि वह इसके बजाय 12 किमी/घंटा से साइकिल चलाकर जाए, तो कितना समय बचाएगा?",
  ["5 minutes", "10 minutes", "15 minutes", "20 minutes"], 3,
  "Half an hour at 4 km/h is 2 km. At 12 km/h, 2 km takes 2 ÷ 12 of an hour, that is 10 minutes, so cycling saves 30 - 10 = 20 minutes. "
  "10 minutes is the time taken by cycle, not the time saved; 5 and 15 minutes have no basis.",
  "4 किमी/घंटा से आधा घंटा यानी 2 किमी। 12 किमी/घंटा से 2 किमी में घंटे का 2 ÷ 12 भाग, यानी 10 मिनट लगते हैं, इसलिए साइकिल से 30 - 10 = 20 मिनट बचते हैं। "
  "10 मिनट साइकिल से लगने वाला समय है, बचा हुआ समय नहीं; 5 और 15 मिनट का कोई आधार नहीं।",
  "qa-sdt-cycling-instead-of-walking", _sdt2,
  opts_hi=["5 मिनट", "10 मिनट", "15 मिनट", "20 मिनट"])

def _sdt3():
    floor, belt = F(120, F(3, 2)), F(120, F(3, 2) + 1)
    assert (floor, belt) == (80, 48)
    return f"{floor - belt} s"
N(QA, "Speed-Distance-Time", "medium",
  "A moving walkway at an airport is 120 m long and moves at 1 m/s. A traveller who walks at 1.5 m/s walks along it. How many seconds does the traveller save, compared with walking the same distance on the floor beside it?",
  "एक हवाई अड्डे पर चलने वाला पथ (मूविंग वॉकवे) 120 मीटर लंबा है और 1 मीटर/सेकंड से चलता है। 1.5 मीटर/सेकंड से चलने वाला एक यात्री उस पर चलता है। उसके बगल के फ़र्श पर उतनी ही दूरी चलने की तुलना में यात्री कितने सेकंड बचाता है?",
  ["32 s", "40 s", "48 s", "80 s"], 0,
  "On the floor the traveller takes 120 ÷ 1.5 = 80 seconds. On the walkway the speeds add, 1.5 + 1 = 2.5 m/s, so it takes 120 ÷ 2.5 = 48 seconds. The saving is 80 - 48 = 32 seconds. "
  "48 s and 80 s are the two times, not the saving; 40 s compares standing still on the walkway (120 s) with walking on the floor.",
  "फ़र्श पर यात्री को 120 ÷ 1.5 = 80 सेकंड लगते हैं। चलने वाले पथ पर चालें जुड़ जाती हैं, 1.5 + 1 = 2.5 मीटर/सेकंड, इसलिए 120 ÷ 2.5 = 48 सेकंड लगते हैं। बचत 80 - 48 = 32 सेकंड है। "
  "48 और 80 सेकंड दोनों समय हैं, बचत नहीं; 40 सेकंड पथ पर खड़े रहने (120 सेकंड) की तुलना फ़र्श पर चलने से करता है।",
  "qa-sdt-a-moving-walkway", _sdt3,
  opts_hi=["32 सेकंड", "40 सेकंड", "48 सेकंड", "80 सेकंड"])

def _sdt4():
    legs, stop = 200 // 50, 10
    minutes = 200 * 60 // 50 + (legs - 1) * stop
    return f"{minutes // 60} h {minutes % 60} min"
N(QA, "Speed-Distance-Time", "medium",
  "A bus travels 200 km at a steady 50 km/h. It stops for 10 minutes after every 50 km, but not at the end of the journey. How long does the whole journey take?",
  "एक बस 200 किमी की दूरी स्थिर 50 किमी/घंटा से तय करती है। वह हर 50 किमी के बाद 10 मिनट रुकती है, पर यात्रा के अंत में नहीं। पूरी यात्रा में कितना समय लगता है?",
  ["4 h 10 min", "4 h 20 min", "4 h 30 min", "4 h 40 min"], 2,
  "Driving takes 200 ÷ 50 = 4 hours. The 200 km fall into four stretches of 50 km, and the bus stops between them -- after 50, 100 and 150 km -- but not after the last, so there are 3 stops, 30 minutes. In all 4 h 30 min. "
  "4 h 40 min adds a fourth stop at the end; 4 h 20 min and 4 h 10 min count only two stops or one.",
  "गाड़ी चलाने में 200 ÷ 50 = 4 घंटे लगते हैं। 200 किमी, 50 किमी के चार हिस्सों में बँटते हैं, और बस उनके बीच रुकती है -- 50, 100 और 150 किमी के बाद -- पर अंतिम के बाद नहीं, इसलिए 3 ठहराव, 30 मिनट। कुल 4 घंटे 30 मिनट। "
  "4 घंटे 40 मिनट अंत में चौथा ठहराव जोड़ता है; 4 घंटे 20 मिनट और 4 घंटे 10 मिनट केवल दो या एक ठहराव गिनते हैं।",
  "qa-sdt-stops-between-the-stages", _sdt4,
  opts_hi=["4 घंटे 10 मिनट", "4 घंटे 20 मिनट", "4 घंटे 30 मिनट", "4 घंटे 40 मिनट"])

# ---------------------------------------------------------------- Ratio, Mixtures & Alligation (4)
def _rm1():
    c_ = next(x for x in range(0, 7001) if x + (x + 200) + (x + 800) == 7000)
    return f"₹{indian(c_ + 800)}"
N(QA, "Ratio, Mixtures & Alligation", "easy",
  "₹7,000 is divided among A, B and C so that A gets ₹600 more than B, and B gets ₹200 more than C. How much does A get?",
  "₹7,000 को A, B और C में इस प्रकार बाँटा जाता है कि A को B से ₹600 अधिक और B को C से ₹200 अधिक मिलता है। A को कितना मिलता है?",
  ["₹2,000", "₹2,200", "₹2,800", "₹3,000"], 2,
  "If C gets x, B gets x + 200 and A gets x + 800, so 3x + 1,000 = 7,000 and x = 2,000. A gets 2,000 + 800 = ₹2,800. "
  "₹2,000 is C's share and ₹2,200 is B's; ₹3,000 has no basis.",
  "यदि C को x मिलता है, तो B को x + 200 और A को x + 800, इसलिए 3x + 1,000 = 7,000 और x = 2,000। A को 2,000 + 800 = ₹2,800 मिलते हैं। "
  "₹2,000, C का हिस्सा है और ₹2,200, B का; ₹3,000 का कोई आधार नहीं।",
  "qa-rm-shares-that-differ-by-fixed-amounts", _rm1)

def _rm2():
    litres = 2 * 100 ** 3
    return f"{indian(litres)} litres"
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "A model of a ship is built to a scale of 1 : 100. When full, the model's hold carries 2 litres of water. How much would the hold of the real ship carry?",
  "एक जहाज़ का मॉडल 1 : 100 के पैमाने पर बनाया गया है। भरा होने पर मॉडल के माल-कक्ष (होल्ड) में 2 लीटर पानी आता है। असली जहाज़ के माल-कक्ष में कितना आएगा?",
  ["200 litres", "20,000 litres", "2,00,000 litres", "20,00,000 litres"], 3,
  "Every length of the real ship is 100 times the model's, so every volume is 100 × 100 × 100 = 10,00,000 times as large: 2 × 10,00,000 = 20,00,000 litres (2,000 cubic metres). "
  "200 litres scales by length alone and 20,000 litres by area; 2,00,000 litres has no basis.",
  "असली जहाज़ की हर लंबाई मॉडल की 100 गुना है, इसलिए हर आयतन 100 × 100 × 100 = 10,00,000 गुना है: 2 × 10,00,000 = 20,00,000 लीटर (2,000 घन मीटर)। "
  "200 लीटर केवल लंबाई से और 20,000 लीटर क्षेत्रफल से बढ़ाता है; 2,00,000 लीटर का कोई आधार नहीं।",
  "qa-rm-a-scale-model-s-hold", _rm2,
  opts_hi=["200 लीटर", "20,000 लीटर", "2,00,000 लीटर", "20,00,000 लीटर"])

def _rm3():
    fuel = F(60, 15) + F(240, 20)
    r = F(300) / fuel
    assert r == F(75, 4)
    return "18.75 km per litre"
N(QA, "Ratio, Mixtures & Alligation", "hard",
  "A car runs 15 km on a litre of petrol in the city and 20 km on a litre on the highway. On a trip of 60 km in the city and 240 km on the highway, how many kilometres does it run per litre for the trip as a whole?",
  "एक गाड़ी शहर में एक लीटर पेट्रोल में 15 किमी और राजमार्ग पर एक लीटर में 20 किमी चलती है। शहर में 60 किमी और राजमार्ग पर 240 किमी की एक यात्रा में, पूरी यात्रा के लिए वह प्रति लीटर कितने किलोमीटर चलती है?",
  ["17.5 km per litre", "18.75 km per litre", "19 km per litre", "20 km per litre"], 1,
  "Find the petrol used: 60 ÷ 15 = 4 litres in the city and 240 ÷ 20 = 12 litres on the highway, 16 litres for 300 km. That is 300 ÷ 16 = 18.75 km per litre. "
  "17.5 averages the two figures as if the trip were split evenly; 19 weights them by distance (0.2 × 15 + 0.8 × 20), but the figures must be weighted by petrol used, not by kilometres; 20 is the highway figure alone.",
  "उपयोग हुआ पेट्रोल निकालिए: शहर में 60 ÷ 15 = 4 लीटर और राजमार्ग पर 240 ÷ 20 = 12 लीटर, 300 किमी के लिए 16 लीटर। यानी 300 ÷ 16 = 18.75 किमी प्रति लीटर। "
  "17.5 दोनों आँकड़ों का ऐसा औसत लेता है मानो यात्रा बराबर बँटी हो; 19 उन्हें दूरी से भारित करता है (0.2 × 15 + 0.8 × 20), पर आँकड़ों को किलोमीटर से नहीं, उपयोग हुए पेट्रोल से भारित करना होता है; 20 केवल राजमार्ग का आँकड़ा है।",
  "qa-rm-fuel-economy-over-a-mixed-trip", _rm3,
  opts_hi=["17.5 किमी प्रति लीटर", "18.75 किमी प्रति लीटर", "19 किमी प्रति लीटर", "20 किमी प्रति लीटर"])

def _rm4():
    now = 1200 // 30
    need = math.ceil(F(1500, 24))
    return str(need - now)
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "A school has 1,200 students and one teacher for every 30 of them. If 300 more students join, how many more teachers must be appointed so that there are no more than 24 students for each teacher?",
  "एक विद्यालय में 1,200 विद्यार्थी हैं और हर 30 विद्यार्थियों पर एक शिक्षक। यदि 300 और विद्यार्थी आ जाएँ, तो कितने और शिक्षक नियुक्त करने होंगे ताकि हर शिक्षक पर 24 से अधिक विद्यार्थी न हों?",
  ["10", "20", "22", "23"], 3,
  "There are now 1,200 ÷ 30 = 40 teachers. 1,500 students at no more than 24 a teacher need at least 1,500 ÷ 24 = 62.5 teachers -- that is, 63, since 62 would leave more than 24 to some teacher. So 63 - 40 = 23 more. "
  "22 rounds 62.5 down; 10 keeps the old ratio of 30 for the 300 new students; 20 has no basis.",
  "अभी 1,200 ÷ 30 = 40 शिक्षक हैं। प्रति शिक्षक 24 से अधिक नहीं की दर से 1,500 विद्यार्थियों को कम से कम 1,500 ÷ 24 = 62.5 शिक्षक चाहिए -- यानी 63, क्योंकि 62 होने पर किसी शिक्षक के पास 24 से अधिक रह जाएँगे। अतः 63 - 40 = 23 और। "
  "22, 62.5 को नीचे की ओर पूर्णांकित करता है; 10, 300 नए विद्यार्थियों के लिए पुराना 30 का अनुपात रखता है; 20 का कोई आधार नहीं।",
  "qa-rm-teachers-needed-for-a-lower-ratio", _rm4)

# ---------------------------------------------------------------- Percentage & Profit-Loss (3)
def _pp1():
    a = 1000 * F(9, 10) - 100
    b = (1000 - 100) * F(9, 10)
    return f"₹{int(b - a)}"
N(QA, "Percentage & Profit-Loss", "medium",
  "A shirt marked ₹1,000 can be bought with a 10 per cent discount and a coupon worth ₹100 off. The shop applies the two in whichever order the customer chooses. How much does the customer save by choosing the better order?",
  "₹1,000 अंकित मूल्य की एक कमीज़ 10 प्रतिशत छूट और ₹100 की कटौती वाले एक कूपन के साथ ख़रीदी जा सकती है। दुकान दोनों को उस क्रम में लागू करती है जो ग्राहक चुने। बेहतर क्रम चुनकर ग्राहक कितना बचाता है?",
  ["₹0", "₹10", "₹90", "₹100"], 1,
  "Discount first: 10 per cent off ₹1,000 gives ₹900, and the coupon then brings it to ₹800. Coupon first: ₹900, and 10 per cent off that gives ₹810. Taking the discount first is better, by ₹10 -- because the discount then applies to the larger amount. "
  "₹0 assumes the order cannot matter; ₹90 and ₹100 have no basis.",
  "पहले छूट: ₹1,000 पर 10 प्रतिशत छूट से ₹900, और फिर कूपन से ₹800। पहले कूपन: ₹900, और उस पर 10 प्रतिशत छूट से ₹810। पहले छूट लेना ₹10 से बेहतर है -- क्योंकि तब छूट बड़ी राशि पर लगती है। "
  "₹0 मान लेता है कि क्रम से कोई फ़र्क़ नहीं पड़ता; ₹90 और ₹100 का कोई आधार नहीं।",
  "qa-pp-a-coupon-before-or-after-a-discount", _pp1)

def _pp2():
    salt = F(40) * F(10, 100)
    return f"{int(40 - salt / F(16, 100))} litres"
N(QA, "Percentage & Profit-Loss", "medium",
  "40 litres of a solution are 10 per cent salt. How much water must be boiled off for the solution to become 16 per cent salt?",
  "40 लीटर के एक घोल में 10 प्रतिशत नमक है। घोल में 16 प्रतिशत नमक होने के लिए कितना पानी उबालकर उड़ाना होगा?",
  ["6 litres", "10 litres", "15 litres", "24 litres"], 2,
  "The salt stays at 10 per cent of 40 = 4 litres. For 4 litres to be 16 per cent of the solution, the solution must be 4 ÷ 0.16 = 25 litres, so 40 - 25 = 15 litres of water must go. "
  "6 litres takes the 6 percentage points as litres; 24 litres scales 40 up in the ratio 16 : 10 and subtracts, as if water were being added; 10 litres has no basis.",
  "नमक 40 का 10 प्रतिशत = 4 लीटर ही रहता है। 4 लीटर घोल का 16 प्रतिशत हो, इसके लिए घोल 4 ÷ 0.16 = 25 लीटर होना चाहिए, इसलिए 40 - 25 = 15 लीटर पानी जाना चाहिए। "
  "6 लीटर 6 प्रतिशत बिंदुओं को लीटर मान लेता है; 24 लीटर 40 को 16 : 10 के अनुपात में बढ़ाकर घटाता है, मानो पानी मिलाया जा रहा हो; 10 लीटर का कोई आधार नहीं।",
  "qa-pp-water-boiled-off-a-salt-solution", _pp2,
  opts_hi=["6 लीटर", "10 लीटर", "15 लीटर", "24 लीटर"])

def _pp3():
    cost = 120
    revenue = 40 * F(12, 10) + 60 * F(9, 10) + 20 * F(13, 10)
    p = (revenue - cost) / cost * 100
    assert p == F(20, 3)
    return "A profit of 6⅔ per cent"
N(QA, "Percentage & Profit-Loss", "hard",
  "A dealer buys 120 identical items at the same price. A third of them are sold at a profit of 20 per cent, half of them at a loss of 10 per cent, and the rest at a profit of 30 per cent. What is the dealer's overall result?",
  "एक व्यापारी एक ही मूल्य पर 120 एक जैसी वस्तुएँ ख़रीदता है। उनमें से एक-तिहाई 20 प्रतिशत लाभ पर, आधी 10 प्रतिशत हानि पर, और बाक़ी 30 प्रतिशत लाभ पर बेची जाती हैं। व्यापारी का कुल परिणाम क्या है?",
  ["A loss of 6⅔ per cent", "A profit of 5 per cent", "A profit of 6⅔ per cent", "A profit of 13⅓ per cent"], 2,
  "Take each item to cost ₹1. 40 items sell for 40 × 1.2 = 48, 60 for 60 × 0.9 = 54, and 20 for 20 × 1.3 = 26: ₹128 in all against a cost of ₹120. The profit is 8 on 120, that is 6⅔ per cent. "
  "13⅓ per cent averages 20, -10 and 30 without weighting them by the number of items; a loss of 6⅔ per cent gets the sign wrong; 5 per cent has no basis.",
  "हर वस्तु का मूल्य ₹1 मानिए। 40 वस्तुएँ 40 × 1.2 = 48 में, 60 वस्तुएँ 60 × 0.9 = 54 में, और 20 वस्तुएँ 20 × 1.3 = 26 में बिकती हैं: कुल ₹128, लागत ₹120 के मुक़ाबले। लाभ 120 पर 8, यानी 6⅔ प्रतिशत। "
  "13⅓ प्रतिशत 20, -10 और 30 का वस्तुओं की संख्या से भारित किए बिना औसत लेता है; 6⅔ प्रतिशत हानि चिह्न ग़लत कर देता है; 5 प्रतिशत का कोई आधार नहीं।",
  "qa-pp-a-stock-sold-in-three-lots", _pp3,
  opts_hi=["6⅔ प्रतिशत हानि", "5 प्रतिशत लाभ", "6⅔ प्रतिशत लाभ", "13⅓ प्रतिशत लाभ"])

# ---------------------------------------------------------------- Sequences & Series (2)
def _ss1():
    def say(s):
        out, i = "", 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] == s[i]:
                j += 1
            out += str(j - i) + s[i]
            i = j
        return out
    seq = ["1"]
    while len(seq) < 6:
        seq.append(say(seq[-1]))
    assert seq[:5] == ["1", "11", "21", "1211", "111221"]
    return seq[5]
T(QA, "Sequences & Series", "hard",
  "In the sequence 1, 11, 21, 1211, 111221, ..., each term describes the term before it: 1 is 'one 1', written 11; 11 is 'two 1s', written 21; 21 is 'one 2, one 1', written 1211; and so on. What is the next term?",
  "अनुक्रम 1, 11, 21, 1211, 111221, ... में हर पद अपने से पहले वाले पद का वर्णन करता है: 1 है 'एक 1', लिखा गया 11; 11 है 'दो 1', लिखा गया 21; 21 है 'एक 2, एक 1', लिखा गया 1211; और इसी तरह। अगला पद क्या है?",
  ["312211", "311221", "3112211", "1321211"], ["312211", "311221", "3112211", "1321211"],
  0,
  "111221 reads as three 1s, two 2s and one 1: 31 22 11, that is 312211. "
  "311221 writes 'three 1s, one 2, two 1s', miscounting the 2s; 3112211 treats the two 2s as separate groups; 1321211 describes 111221 digit by digit in the wrong order.",
  "111221 को पढ़ते हैं तीन 1, दो 2 और एक 1: 31 22 11, यानी 312211। "
  "311221 लिखता है 'तीन 1, एक 2, दो 1', जो 2 को ग़लत गिनता है; 3112211 दोनों 2 को अलग-अलग समूह मानता है; 1321211, 111221 का अंक-दर-अंक ग़लत क्रम में वर्णन करता है।",
  "qa-ss-a-sequence-that-describes-the-term-before-it", pos=3, check=_ss1)

def _ss2():
    n = next(k for k in range(1, 30) if 3 * 2 ** (k - 1) == 768)
    return f"{n}th"
N(QA, "Sequences & Series", "medium",
  "In the series 3, 6, 12, 24, ..., in which each term is double the one before it, which term is 768?",
  "श्रेणी 3, 6, 12, 24, ... में, जिसमें हर पद पिछले पद का दोगुना है, 768 कौन-सा पद है?",
  ["8th", "9th", "10th", "256th"], 1,
  "The n-th term is 3 × 2ⁿ⁻¹. 768 = 3 × 256 = 3 × 2⁸, so n - 1 = 8 and n = 9: 768 is the 9th term. "
  "8th takes the power of 2 for the place, forgetting that the first term is 3 × 2⁰; 256th takes the multiplier for the place; 10th has no basis.",
  "n-वाँ पद 3 × 2ⁿ⁻¹ है। 768 = 3 × 256 = 3 × 2⁸, इसलिए n - 1 = 8 और n = 9: 768, 9वाँ पद है। "
  "8वाँ, 2 की घात को स्थान मान लेता है, यह भूलकर कि पहला पद 3 × 2⁰ है; 256वाँ गुणक को स्थान मान लेता है; 10वें का कोई आधार नहीं।",
  "qa-ss-the-place-of-768-in-a-doubling-series", _ss2,
  opts_hi=["8वाँ", "9वाँ", "10वाँ", "256वाँ"])

# ---------------------------------------------------------------- Permutation & Combination (3)
def _pc1():
    return str(len(list(permutations(range(11), 2))))
N(QA, "Permutation & Combination", "easy",
  "In how many ways can a captain and a vice-captain be chosen from a team of 11 players?",
  "11 खिलाड़ियों की एक टीम में से एक कप्तान और एक उप-कप्तान कितने तरीक़ों से चुने जा सकते हैं?",
  ["55", "110", "121", "220"], 1,
  "Any of the 11 can be captain, and then any of the other 10 vice-captain: 11 × 10 = 110. The two posts are different, so the order of choosing matters. "
  "55 counts pairs of players without saying who holds which post; 121 lets one player hold both posts; 220 has no basis.",
  "11 में से कोई भी कप्तान हो सकता है, और फिर बाक़ी 10 में से कोई भी उप-कप्तान: 11 × 10 = 110। दोनों पद अलग हैं, इसलिए चुनने का क्रम मायने रखता है। "
  "55 खिलाड़ियों के जोड़े गिनता है, यह बताए बिना कि कौन-सा पद किसके पास है; 121 एक ही खिलाड़ी को दोनों पद दे देता है; 220 का कोई आधार नहीं।",
  "qa-pc-a-captain-and-a-vice-captain", _pc1)

def _pc2():
    sides = {frozenset((i, (i + 1) % 6)) for i in range(6)}
    tris = list(combinations(range(6), 3))
    none = [t for t in tris if not any(frozenset(p) in sides for p in combinations(t, 2))]
    assert len(tris) == 20 and sorted(none) == [(0, 2, 4), (1, 3, 5)]
    return str(len(none))
N(QA, "Permutation & Combination", "hard",
  "Triangles are drawn by joining three of the six corners of a regular hexagon. How many of these triangles have no side in common with the hexagon?",
  "एक सम षट्भुज के छह कोनों में से तीन को जोड़कर त्रिभुज बनाए जाते हैं। इनमें से कितने त्रिभुजों की कोई भी भुजा षट्भुज की भुजा नहीं है?",
  ["2", "4", "6", "8"], 0,
  "A triangle avoids every side of the hexagon only if no two of its corners are next to each other on the hexagon. With six corners round a ring, that means taking every other corner: corners 1, 3, 5 or corners 2, 4, 6. So there are just 2. "
  "Check by counting the rest: of the 6C3 = 20 triangles, 6 use two sides (three corners in a row) and 12 use exactly one (a side, plus one of the two corners not next to it), leaving 20 - 18 = 2. 6 and 8 miscount these groups; 4 has no basis.",
  "कोई त्रिभुज षट्भुज की हर भुजा से तभी बचता है जब उसके कोई दो कोने षट्भुज पर पास-पास न हों। एक घेरे में छह कोनों के साथ इसका अर्थ है एक छोड़कर एक कोना लेना: कोने 1, 3, 5 या कोने 2, 4, 6। अतः केवल 2। "
  "बाक़ी को गिनकर जाँचिए: 6C3 = 20 त्रिभुजों में से 6 दो भुजाएँ लेते हैं (लगातार तीन कोने) और 12 ठीक एक (एक भुजा, और उससे सटे न होने वाले दो कोनों में से एक), जिससे 20 - 18 = 2 बचते हैं। 6 और 8 इन समूहों को ग़लत गिनते हैं; 4 का कोई आधार नहीं।",
  "qa-pc-triangles-in-a-hexagon-with-no-side-on-it", _pc2)

def _pc3():
    ev = F(10, 6) - 2
    assert ev == F(-1, 3)
    return "A loss of about 33 paise"
T(QA, "Permutation & Combination", "medium",
  "A game costs ₹2 to play. A fair die is rolled once, and the player wins ₹10 if it shows a six and nothing otherwise. Over many games, what happens to a player on average in each game?",
  "एक खेल खेलने के ₹2 लगते हैं। एक निष्पक्ष पासा एक बार फेंका जाता है, और छह आने पर खिलाड़ी ₹10 जीतता है, अन्यथा कुछ नहीं। बहुत-से खेलों में, हर खेल में औसतन खिलाड़ी के साथ क्या होता है?",
  ["A loss of about 33 paise", "A gain of about ₹1.67", "Neither a gain nor a loss", "A loss of the full ₹2"],
  ["लगभग 33 पैसे की हानि", "लगभग ₹1.67 का लाभ", "न लाभ न हानि", "हर खेल में पूरे ₹2 की हानि"],
  0,
  "A six comes up in 1 game in 6 on average, so the average winnings are ₹10 ÷ 6 ≈ ₹1.67 a game. Against the ₹2 paid, the player loses about ₹0.33 -- 33 paise -- a game on average. "
  "₹1.67 is the average winnings before the cost of playing is taken off; 'neither a gain nor a loss' would need a prize of ₹12; the full ₹2 is lost only in games without a six.",
  "औसतन 6 में से 1 खेल में छह आता है, इसलिए औसत जीत ₹10 ÷ 6 ≈ ₹1.67 प्रति खेल है। चुकाए गए ₹2 के मुक़ाबले खिलाड़ी औसतन हर खेल में लगभग ₹0.33 -- 33 पैसे -- हारता है। "
  "₹1.67 खेलने का मूल्य घटाने से पहले की औसत जीत है; 'न लाभ न हानि' के लिए ₹12 का इनाम चाहिए; पूरे ₹2 केवल उन खेलों में जाते हैं जिनमें छह नहीं आता।",
  "qa-pc-the-average-result-of-a-dice-game", pos=1, check=_pc3)

# ---------------------------------------------------------------- Geometry & Mensuration (2)
def _gm1():
    a = F(22, 7) * (14 ** 2 - 7 ** 2)
    return f"{int(a)} cm²"
N(QA, "Geometry & Mensuration", "easy",
  "Two circles have the same centre and radii of 7 cm and 14 cm. What is the area of the ring between them? (Take π = 22/7.)",
  "दो वृत्तों का केंद्र एक ही है और उनकी त्रिज्याएँ 7 सेमी और 14 सेमी हैं। उनके बीच के वलय का क्षेत्रफल क्या है? (π = 22/7 लीजिए।)",
  ["154 cm²", "308 cm²", "462 cm²", "616 cm²"], 2,
  "The ring is the larger circle minus the smaller: 22/7 × (14² - 7²) = 22/7 × 147 = 462 cm². "
  "616 cm² is the larger circle and 154 cm² the smaller; 308 cm² multiplies π by the two radii (22/7 × 7 × 14).",
  "वलय बड़े वृत्त में से छोटे वृत्त को घटाकर बनता है: 22/7 × (14² - 7²) = 22/7 × 147 = 462 वर्ग सेमी। "
  "616 वर्ग सेमी बड़ा वृत्त है और 154 वर्ग सेमी छोटा; 308 वर्ग सेमी, π को दोनों त्रिज्याओं से गुणा करता है (22/7 × 7 × 14)।",
  "qa-gm-the-area-of-a-ring", _gm1,
  opts_hi=["154 वर्ग सेमी", "308 वर्ग सेमी", "462 वर्ग सेमी", "616 वर्ग सेमी"])

def _gm2():
    walls = 2 * 3 * (5 + 4)
    area = F(walls) - 2 * 1 - F(3, 2) * 1
    return f"{float(area)} m²"
N(QA, "Geometry & Mensuration", "medium",
  "A room is 5 m long, 4 m wide and 3 m high. Its four walls are to be painted, but not the ceiling or the floor, leaving out one door of 2 m × 1 m and one window of 1.5 m × 1 m. What area is to be painted?",
  "एक कमरा 5 मीटर लंबा, 4 मीटर चौड़ा और 3 मीटर ऊँचा है। उसकी चारों दीवारें रँगी जानी हैं, पर छत या फ़र्श नहीं, और 2 मीटर × 1 मीटर का एक दरवाज़ा तथा 1.5 मीटर × 1 मीटर की एक खिड़की छोड़नी है। कितना क्षेत्रफल रँगा जाना है?",
  ["50.5 m²", "54 m²", "57.5 m²", "70.5 m²"], 0,
  "The four walls together are the room's height times its perimeter: 3 × 2 × (5 + 4) = 54 m². Taking off the door (2 m²) and the window (1.5 m²) leaves 50.5 m². "
  "54 m² forgets the door and window; 57.5 m² adds them instead of taking them off; 70.5 m² paints the ceiling (20 m²) too.",
  "चारों दीवारें मिलकर कमरे की ऊँचाई गुणा उसका परिमाप हैं: 3 × 2 × (5 + 4) = 54 वर्ग मीटर। दरवाज़ा (2 वर्ग मीटर) और खिड़की (1.5 वर्ग मीटर) घटाने पर 50.5 वर्ग मीटर बचता है। "
  "54 वर्ग मीटर दरवाज़े और खिड़की को भूल जाता है; 57.5 वर्ग मीटर उन्हें घटाने के बजाय जोड़ता है; 70.5 वर्ग मीटर छत (20 वर्ग मीटर) को भी रँगता है।",
  "qa-gm-the-walls-of-a-room-to-be-painted", _gm2,
  opts_hi=["50.5 वर्ग मीटर", "54 वर्ग मीटर", "57.5 वर्ग मीटर", "70.5 वर्ग मीटर"])

# ---------------------------------------------------------------- Time & Work (2)
def _tw1():
    per_printer_per_min = F(5, 5 * 5)                # 5 pages by 5 printers in 5 minutes
    n = F(100) / (per_printer_per_min * 5)
    return str(int(n))
N(QA, "Time & Work", "easy",
  "5 printers, working at the same steady rate, print 5 pages in 5 minutes. How many such printers are needed to print 100 pages in 5 minutes?",
  "एक ही स्थिर दर से काम करने वाले 5 प्रिंटर 5 मिनट में 5 पृष्ठ छापते हैं। 5 मिनट में 100 पृष्ठ छापने के लिए ऐसे कितने प्रिंटर चाहिए?",
  ["5", "20", "25", "100"], 3,
  "5 printers make 5 pages in 5 minutes, so each printer makes one page in 5 minutes. To make 100 pages in those 5 minutes, 100 printers are needed. "
  "5 keeps the number of printers unchanged; 20 divides 100 by 5; 25 has no basis.",
  "5 प्रिंटर 5 मिनट में 5 पृष्ठ बनाते हैं, इसलिए हर प्रिंटर 5 मिनट में एक पृष्ठ बनाता है। उन्हीं 5 मिनट में 100 पृष्ठ बनाने के लिए 100 प्रिंटर चाहिए। "
  "5 प्रिंटरों की संख्या नहीं बदलता; 20, 100 को 5 से भाग देता है; 25 का कोई आधार नहीं।",
  "qa-tw-five-printers-and-five-pages", _tw1)

def _tw2():
    work = 8 * 15
    days = F(work) / (9 * F(8, 10))
    assert days == F(50, 3)
    return "16⅔ days"
N(QA, "Time & Work", "medium",
  "A worker who works 8 hours a day finishes a job in 15 days. How many days would the job take if the worker worked 9 hours a day, but got through only 80 per cent as much in each hour as before?",
  "8 घंटे प्रतिदिन काम करने वाला एक कामगार एक काम 15 दिनों में पूरा करता है। यदि कामगार 9 घंटे प्रतिदिन काम करे, पर हर घंटे में पहले का केवल 80 प्रतिशत काम कर पाए, तो काम कितने दिनों में होगा?",
  ["13⅓ days", "15 days", "16⅔ days", "18¾ days"], 2,
  "The job needs 8 × 15 = 120 hours at the old rate. Each new day gives 9 × 0.8 = 7.2 such hours, so the job takes 120 ÷ 7.2 = 16⅔ days. "
  "13⅓ days counts the longer days but not the slower rate (120 ÷ 9); 18¾ days counts the slower rate but not the longer days (15 ÷ 0.8); 15 days assumes the two cancel out.",
  "पुरानी दर पर काम के लिए 8 × 15 = 120 घंटे चाहिए। हर नया दिन ऐसे 9 × 0.8 = 7.2 घंटे देता है, इसलिए काम 120 ÷ 7.2 = 16⅔ दिनों में होता है। "
  "13⅓ दिन लंबे दिनों को गिनता है पर धीमी दर को नहीं (120 ÷ 9); 18¾ दिन धीमी दर को गिनता है पर लंबे दिनों को नहीं (15 ÷ 0.8); 15 दिन मान लेता है कि दोनों एक-दूसरे को काट देते हैं।",
  "qa-tw-longer-days-at-a-lower-rate", _tw2,
  opts_hi=["13⅓ दिन", "15 दिन", "16⅔ दिन", "18¾ दिन"])

# ---------------------------------------------------------------- Puzzle Hybrid (3)
def _ph1():
    per_floor = F(30, 4 - 1)
    return f"{int(per_floor * (10 - 1))} s"
N(QA, "Puzzle Hybrid", "easy",
  "A lift rises at a steady rate and takes 30 seconds to go from the 1st floor to the 4th. How long does it take to go from the 1st floor to the 10th?",
  "एक लिफ़्ट स्थिर दर से ऊपर जाती है और पहली मंज़िल से चौथी मंज़िल तक जाने में 30 सेकंड लेती है। पहली मंज़िल से दसवीं मंज़िल तक जाने में उसे कितना समय लगता है?",
  ["67.5 s", "75 s", "80 s", "90 s"], 3,
  "From the 1st floor to the 4th the lift climbs 3 floors, not 4, so it takes 10 seconds a floor. From the 1st to the 10th it climbs 9 floors: 90 seconds. "
  "75 s and 67.5 s divide the 30 seconds among 4 floors (7.5 seconds each) and then count 10 or 9 floors; 80 s has no basis.",
  "पहली से चौथी मंज़िल तक लिफ़्ट 4 नहीं, 3 मंज़िलें चढ़ती है, इसलिए प्रति मंज़िल 10 सेकंड लेती है। पहली से दसवीं तक वह 9 मंज़िलें चढ़ती है: 90 सेकंड। "
  "75 और 67.5 सेकंड, 30 सेकंड को 4 मंज़िलों में बाँटते हैं (हर एक के 7.5 सेकंड) और फिर 10 या 9 मंज़िलें गिनते हैं; 80 सेकंड का कोई आधार नहीं।",
  "qa-ph-a-lift-timed-between-floors", _ph1,
  opts_hi=["67.5 सेकंड", "75 सेकंड", "80 सेकंड", "90 सेकंड"])

def _ph2():
    sums = set()
    for p in permutations(range(1, 7)):
        a, b, c_, ab, bc, ca = p                       # three corners, then the middle of each side
        if a + ab + b == b + bc + c_ == c_ + ca + a == 9:
            sums.add(a + b + c_)
    assert sums == {6}
    return "6"
N(QA, "Puzzle Hybrid", "medium",
  "The numbers 1 to 6 are written once each, one at every corner of a triangle and one at the middle of every side, so that the three numbers along each side add up to 9. What do the three numbers at the corners add up to?",
  "संख्याएँ 1 से 6 एक-एक बार लिखी जाती हैं, एक त्रिभुज के हर कोने पर एक और हर भुजा के मध्य में एक, ऐसे कि हर भुजा की तीनों संख्याओं का योग 9 हो। कोनों की तीनों संख्याओं का योग क्या है?",
  ["6", "9", "12", "15"], 0,
  "Add the three side totals: 3 × 9 = 27. This counts every number once and each corner twice, since a corner lies on two sides. All six numbers add up to 21, so the corners add up to 27 - 21 = 6 -- which forces them to be 1, 2 and 3 (with 6, 4 and 5 in the middles). "
  "9 is a side total, not the corners'; 12 and 15 would make the side totals larger than 9.",
  "तीनों भुजाओं के योग जोड़िए: 3 × 9 = 27। इसमें हर संख्या एक बार और हर कोना दो बार गिना जाता है, क्योंकि कोना दो भुजाओं पर होता है। छहों संख्याओं का योग 21 है, इसलिए कोनों का योग 27 - 21 = 6 है -- जिससे वे 1, 2 और 3 ही हो सकते हैं (मध्य में 6, 4 और 5)। "
  "9 एक भुजा का योग है, कोनों का नहीं; 12 और 15 भुजाओं के योग को 9 से बड़ा कर देंगे।",
  "qa-ph-a-magic-triangle", _ph2)

def _ph3():
    trips = [t for t in product(range(1, 37), repeat=3) if t[0] <= t[1] <= t[2] and t[0] * t[1] * t[2] == 36]
    by_sum = {}
    for t in trips:
        by_sum.setdefault(sum(t), []).append(t)
    ambiguous = [ts for ts in by_sum.values() if len(ts) > 1]
    assert ambiguous == [[(1, 6, 6), (2, 2, 9)]]
    one_eldest = [t for t in ambiguous[0] if t[2] > t[1]]
    assert one_eldest == [(2, 2, 9)]
    return "2, 2 and 9"
T(QA, "Puzzle Hybrid", "hard",
  "A census officer asks a woman the ages of her three children, in whole years. She says that the product of their ages is 36, and that the sum of their ages is the number on the house next door. The officer looks at that number and says that this is still not enough. She adds, 'My eldest child, who is older than the other two, is learning the flute.' What are the children's ages?",
  "एक जनगणना अधिकारी एक महिला से उसके तीन बच्चों की आयु, पूरे वर्षों में, पूछता है। वह बताती है कि उनकी आयु का गुणनफल 36 है, और उनकी आयु का योग पड़ोस के घर का नंबर है। अधिकारी वह नंबर देखकर कहता है कि यह अब भी पर्याप्त नहीं है। वह जोड़ती है, 'मेरा सबसे बड़ा बच्चा, जो बाक़ी दोनों से बड़ा है, बाँसुरी सीख रहा है।' बच्चों की आयु क्या है?",
  ["2, 2 and 9", "1, 6 and 6", "3, 3 and 4", "1, 4 and 9"], ["2, 2 और 9", "1, 6 और 6", "3, 3 और 4", "1, 4 और 9"],
  0,
  "The sets of three ages with product 36 have the sums 38 (1, 1, 36), 21 (1, 2, 18), 16 (1, 3, 12), 14 (1, 4, 9), 13 (1, 6, 6 and 2, 2, 9), 11 (2, 3, 6) and 10 (3, 3, 4). The officer knows the sum and still cannot tell, so the sum must be 13, the only one shared by two sets. "
  "Of 1, 6, 6 and 2, 2, 9, only the second has a single eldest child older than the other two. So the ages are 2, 2 and 9. 1, 6 and 6 has two eldest of the same age; 3, 3 and 4 and 1, 4 and 9 have sums the officer could have settled at once.",
  "36 गुणनफल वाले तीन आयुओं के समूहों के योग हैं 38 (1, 1, 36), 21 (1, 2, 18), 16 (1, 3, 12), 14 (1, 4, 9), 13 (1, 6, 6 और 2, 2, 9), 11 (2, 3, 6) और 10 (3, 3, 4)। अधिकारी योग जानता है और फिर भी तय नहीं कर पाता, इसलिए योग 13 होना चाहिए, जो अकेला दो समूहों में साझा है। "
  "1, 6, 6 और 2, 2, 9 में से केवल दूसरे में एक ऐसा सबसे बड़ा बच्चा है जो बाक़ी दोनों से बड़ा हो। अतः आयु 2, 2 और 9 है। 1, 6 और 6 में एक ही आयु के दो सबसे बड़े हैं; 3, 3 और 4 तथा 1, 4 और 9 के योगों से अधिकारी तुरंत तय कर लेता।",
  "qa-ph-three-children-s-ages-from-their-product", pos=3, check=_ph3)

# ---------------------------------------------------------------- the data-sufficiency block's two Quant items
def _ds1():
    def median(xs): return sorted(xs)[2]
    s1 = {median([a, b, c_, d, 70 - a - b - c_ - d]) for a in (1, 5, 14) for b in (2, 14, 20) for c_ in (3, 14) for d in (9, 14)}
    s2 = {median([8, 10, 12, x, y]) for x in range(13, 40) for y in range(13, 40)}
    both = {median([8, 10, 12, x, 40 - x]) for x in range(13, 28) if 40 - x > 12}
    assert s2 == both == {12} and len(s1) > 1
    return _ds(s1, s2, both)
DS(QA, "medium",
   "What is the median of a set of five numbers?",
   "पाँच संख्याओं के एक समूह की माध्यिका क्या है?",
   "The mean of the five numbers is 14.", "पाँचों संख्याओं का माध्य 14 है।",
   "Three of the numbers are 8, 10 and 12, and the other two are both greater than 12.", "तीन संख्याएँ 8, 10 और 12 हैं, और बाक़ी दोनों 12 से बड़ी हैं।",
   0,
   "Statement II alone settles it: in order the numbers are 8, 10, 12 and then the two larger ones, so the middle number is 12, whatever the two larger ones are. "
   "Statement I alone does not: a mean of 14 allows many different sets with different middle numbers. So one statement alone is enough, but not the other.",
   "कथन II अकेले इसे तय कर देता है: क्रम में संख्याएँ 8, 10, 12 और फिर दोनों बड़ी संख्याएँ हैं, इसलिए बीच की संख्या 12 है, बड़ी संख्याएँ चाहे जो हों। "
   "कथन I अकेले नहीं: 14 का माध्य अलग-अलग बीच की संख्या वाले कई समूहों की अनुमति देता है। अतः एक कथन अकेले पर्याप्त है, पर दूसरा नहीं।",
   "qa-ds-a-median-from-part-of-the-data", _ds1)

def _ds2():
    import math as m
    s1 = {5 * 5 + 12 * 12 == 13 * 13}
    s2 = set()
    for k in range(1, 180):                          # the angle between the 5 cm and 12 cm sides, in degrees
        area = 0.5 * 5 * 12 * m.sin(m.radians(k))
        if abs(area - 30) < 1e-9:
            s2.add(k == 90)
    assert s1 == {True} and s2 == {True}
    return _ds(s1, s2, s1 & s2)
DS(QA, "hard",
   "Is triangle PQR right-angled?",
   "क्या त्रिभुज PQR समकोण त्रिभुज है?",
   "Its sides are 5 cm, 12 cm and 13 cm.", "उसकी भुजाएँ 5 सेमी, 12 सेमी और 13 सेमी हैं।",
   "Two of its sides are 5 cm and 12 cm, and its area is 30 cm².", "उसकी दो भुजाएँ 5 सेमी और 12 सेमी हैं, और उसका क्षेत्रफल 30 वर्ग सेमी है।",
   1,
   "Statement I alone: 5² + 12² = 25 + 144 = 169 = 13², so the triangle is right-angled. Statement II alone: the area is ½ × 5 × 12 × (the sine of the angle between those sides), and this reaches 30 only when that angle is 90° -- at any other angle the area is less. So it is right-angled again. Either statement alone answers the question.",
   "कथन I अकेले: 5² + 12² = 25 + 144 = 169 = 13², इसलिए त्रिभुज समकोण है। कथन II अकेले: क्षेत्रफल ½ × 5 × 12 × (उन भुजाओं के बीच के कोण की ज्या) है, और यह 30 तभी होता है जब वह कोण 90° हो -- किसी और कोण पर क्षेत्रफल कम होता है। अतः फिर समकोण। कोई भी एक कथन अकेले प्रश्न का उत्तर देता है।",
   "qa-ds-a-right-angle-from-the-sides-or-the-area", _ds2)
