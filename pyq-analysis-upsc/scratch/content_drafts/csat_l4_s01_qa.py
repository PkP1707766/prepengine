# -*- coding: utf-8 -*-
"""CSAT Level 4 · Simulator 1 -- Quantitative Aptitude (38 items: 36 in the Quant slots, 2 in the data-sufficiency block).

Layout A, the 2023/2024 shape of the paper: Quant-heavy, with number theory the largest bucket (10). Exam-level mix,
none of the shapes of Levels 1-3: three claims about two integers, 2026 in base 5, the numbers 1 to 50 written as one
long number, the LCM of 1 to 12, consecutive numbers that add to 100, when (n + 6)/(n - 2) is an integer, sixtieths
between a quarter and a third, the digits of 2 to the 30th, 5 × 6 × 7 × 8 + 1, the zeros at the end of a product of
primes; buses met on the road, three milestones, the speed needed for the rest of a trip, a flight across time zones;
a median after two additions, an overall percentage from marks out of different totals, a chain of exchange rates,
densities from two ratios, red balls after two removals; a bill after a discount, a service charge and a tax, simple
interest by the day, 45 seconds as a share of an hour; two interleaved series, a sum of fractions that approach 1;
seats with no two side by side, two-digit multiples of 3 or 5, shortest paths along a cube's edges; the longest rod in
a box, a pie-chart sector; a leak halfway up a tank, a gang of workers from two what-ifs; the year whose calendar
matches 2027, two workers sharing five jobs, the weekday pigeonhole, the bag of heavy coins found in one weighing, an
ant crossing a cube; and two data-sufficiency items. Every key is worked out in code by check()."""
from fractions import Fraction as F
from itertools import combinations, permutations, product
import datetime as dt
import math
import csat_common as c
from csat_common import N, SC, DS, QA

def _ds(s1, s2, both):
    alone = (len(set(s1)) == 1, len(set(s2)) == 1)
    return "b" if all(alone) else "a" if any(alone) else "c" if len(set(both)) == 1 else "d"

# ---------------------------------------------------------------- Number Theory (10)
def _nt1():
    pairs = [(p, q) for p in range(2, 60) for q in range(1, p)]
    holds = [all(p * p - q * q > p - q for p, q in pairs), all(F(p, q) > F(p + 1, q + 1) for p, q in pairs),
             all(p * q > p + q for p, q in pairs)]
    assert holds == [True, True, False]
    return "1 and 2 only"
SC(QA, "Number Theory", "medium",
   "If p and q are positive integers with p > q, which of the following statements is/are always correct?",
   "यदि p और q धनात्मक पूर्णांक हैं और p > q, तो निम्नलिखित में से कौन-सा/से कथन हमेशा सही है/हैं?",
   ["p² - q² is greater than p - q.", "p/q is greater than (p + 1)/(q + 1).", "pq is greater than p + q."],
   ["p² - q², p - q से बड़ा है।", "p/q, (p + 1)/(q + 1) से बड़ा है।", "pq, p + q से बड़ा है।"],
   ["1 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"], 1,
   "1: p² - q² = (p - q)(p + q), and p + q is at least 3, so it exceeds p - q -- always true. 2: p(q + 1) - q(p + 1) = p - q > 0, so p/q > (p + 1)/(q + 1) -- always true (adding 1 to the top and bottom of a fraction greater than 1 brings it closer to 1). "
   "3 fails whenever q = 1: then pq = p, which is less than p + 1. It holds for some pairs (p = 3, q = 2 gives 6 > 5) but not always.",
   "1: p² - q² = (p - q)(p + q), और p + q कम से कम 3 है, इसलिए यह p - q से बड़ा है -- हमेशा सही। 2: p(q + 1) - q(p + 1) = p - q > 0, इसलिए p/q > (p + 1)/(q + 1) -- हमेशा सही (1 से बड़े भिन्न के अंश और हर में 1 जोड़ने पर वह 1 के निकट आता है)। "
   "3, q = 1 होने पर हर बार विफल होता है: तब pq = p, जो p + 1 से कम है। यह कुछ जोड़ों के लिए सही है (p = 3, q = 2 से 6 > 5) पर हमेशा नहीं।",
   "qa-nt-three-claims-about-two-integers", check=_nt1)

def _nt2():
    n, s = 2026, ""
    while n:
        s, n = str(n % 5) + s, n // 5
    return s
N(QA, "Number Theory", "medium",
  "When the number 2026 is written in base 5 (using only the digits 0 to 4, with place values 1, 5, 25, 125, 625, ...), it becomes:",
  "जब संख्या 2026 को आधार 5 में लिखा जाता है (केवल 0 से 4 तक के अंकों से, स्थानीय मान 1, 5, 25, 125, 625, ... के साथ), तो वह बनती है:",
  ["30101", "31011", "31101", "32101"], 2,
  "Divide repeatedly by 5 and read the remainders upwards: 2026 = 5 × 405 + 1, 405 = 5 × 81 + 0, 81 = 5 × 16 + 1, 16 = 5 × 3 + 1, 3 = 5 × 0 + 3. So 2026 is 31101 in base 5: 3 × 625 + 1 × 125 + 1 × 25 + 0 × 5 + 1 = 1,875 + 125 + 25 + 1 = 2026. "
  "30101 and 32101 give 1,901 and 2,151; 31011 gives 2,006.",
  "बार-बार 5 से भाग दीजिए और शेषफल नीचे से ऊपर पढ़िए: 2026 = 5 × 405 + 1, 405 = 5 × 81 + 0, 81 = 5 × 16 + 1, 16 = 5 × 3 + 1, 3 = 5 × 0 + 3। अतः आधार 5 में 2026 = 31101: 3 × 625 + 1 × 125 + 1 × 25 + 0 × 5 + 1 = 1,875 + 125 + 25 + 1 = 2026। "
  "30101 और 32101 से 1,901 और 2,151 मिलते हैं; 31011 से 2,006।",
  "qa-nt-2026-written-in-base-5", _nt2)

def _nt3():
    r = int("".join(map(str, range(1, 51)))) % 9
    assert r == sum(range(1, 51)) % 9
    return str(r)
N(QA, "Number Theory", "hard",
  "The numbers 1 to 50 are written one after another to form a single long number, 123456789101112...4950. What is the remainder when this number is divided by 9?",
  "1 से 50 तक की संख्याएँ एक के बाद एक लिखकर एक लंबी संख्या बनाई जाती है, 123456789101112...4950। इस संख्या को 9 से भाग देने पर शेषफल क्या है?",
  ["0", "3", "5", "6"], 3,
  "A number leaves the same remainder on division by 9 as the sum of its digits does, and the digits of the long number are just the digits of 1, 2, ..., 50. The digit sum of each of those numbers leaves the same remainder by 9 as the number itself, so the whole digit sum leaves the same remainder as 1 + 2 + ... + 50 = 1,275. "
  "1,275 = 9 × 141 + 6, so the remainder is 6. 0 would need the total to be a multiple of 9; 3 and 5 come from slips in adding.",
  "किसी संख्या को 9 से भाग देने पर वही शेषफल बचता है जो उसके अंकों के योग को भाग देने पर, और लंबी संख्या के अंक बस 1, 2, ..., 50 के अंक हैं। इनमें से हर संख्या का अंक-योग 9 से भाग देने पर वही शेष छोड़ता है जो स्वयं संख्या, इसलिए पूरा अंक-योग वही शेष छोड़ता है जो 1 + 2 + ... + 50 = 1,275। "
  "1,275 = 9 × 141 + 6, अतः शेषफल 6 है। 0 के लिए योग को 9 का गुणज होना चाहिए; 3 और 5 जोड़ने की भूलों से आते हैं।",
  "qa-nt-the-numbers-1-to-50-as-one-long-number", _nt3)

def _nt4():
    assert math.lcm(*range(1, 11)) == 2520
    return f"{math.lcm(*range(1, 13)):,}"
N(QA, "Number Theory", "easy",
  "The smallest number divisible by every whole number from 1 to 10 is 2,520. What is the smallest number divisible by every whole number from 1 to 12?",
  "1 से 10 तक की हर पूर्ण संख्या से विभाज्य सबसे छोटी संख्या 2,520 है। 1 से 12 तक की हर पूर्ण संख्या से विभाज्य सबसे छोटी संख्या क्या है?",
  ["2,520", "5,040", "13,860", "27,720"], 3,
  "2,520 is already divisible by 12 (12 = 4 × 3, both factors of 2,520), so only 11 is new; 11 is prime, so the LCM becomes 2,520 × 11 = 27,720. "
  "2,520 and 5,040 are not divisible by 11; 13,860 is half the answer and is not divisible by 8.",
  "2,520 पहले से 12 से विभाज्य है (12 = 4 × 3, दोनों 2,520 के गुणनखंड), इसलिए केवल 11 नया है; 11 अभाज्य है, इसलिए LCM = 2,520 × 11 = 27,720। "
  "2,520 और 5,040, 11 से विभाज्य नहीं हैं; 13,860 उत्तर का आधा है और 8 से विभाज्य नहीं है।",
  "qa-nt-the-lcm-of-1-to-12", _nt4)

def _nt5():
    runs = [(a, k) for k in range(2, 50) for a in range(1, 100) if k * a + k * (k - 1) // 2 == 100]
    assert runs == [(18, 5), (9, 8)]
    return str(max(k for _, k in runs))
N(QA, "Number Theory", "hard",
  "100 is to be written as the sum of two or more consecutive positive integers. What is the largest number of terms such a sum can have?",
  "100 को दो या अधिक क्रमागत धनात्मक पूर्णांकों के योग के रूप में लिखना है। ऐसे योग में अधिकतम कितने पद हो सकते हैं?",
  ["4", "5", "8", "10"], 2,
  "k consecutive integers starting at a add up to ka + k(k - 1)/2, so k(2a + k - 1) = 200, with a ≥ 1. k and 2a + k - 1 have opposite parity, so one of them is odd, and the odd factors of 200 are 1, 5 and 25. "
  "k = 5 gives 2a + 4 = 40, a = 18: 18 + 19 + 20 + 21 + 22. k = 8 (with 2a + 7 = 25, a = 9) gives 9 + 10 + ... + 16. k = 25 would need 2a + 24 = 8, impossible. So the longest sum has 8 terms. 10 terms would need a = 5.5; 4 terms would need a = 23.5.",
  "a से शुरू होने वाले k क्रमागत पूर्णांकों का योग ka + k(k - 1)/2 है, इसलिए k(2a + k - 1) = 200, जहाँ a ≥ 1। k और 2a + k - 1 की समता विपरीत है, इसलिए उनमें से एक विषम है, और 200 के विषम गुणनखंड 1, 5 और 25 हैं। "
  "k = 5 से 2a + 4 = 40, a = 18: 18 + 19 + 20 + 21 + 22। k = 8 (2a + 7 = 25, a = 9) से 9 + 10 + ... + 16। k = 25 के लिए 2a + 24 = 8 चाहिए, असंभव। अतः सबसे लंबे योग में 8 पद हैं। 10 पदों के लिए a = 5.5 चाहिए; 4 पदों के लिए a = 23.5।",
  "qa-nt-consecutive-numbers-that-add-to-100", _nt5)

def _nt6():
    ns = [n for n in range(-100, 100) if n != 2 and (n + 6) % (n - 2) == 0]
    assert ns == [-6, -2, 0, 1, 3, 4, 6, 10]
    return str(len(ns))
N(QA, "Number Theory", "hard",
  "For how many integers n (positive, negative or zero) is (n + 6)/(n - 2) also an integer?",
  "कितने पूर्णांकों n (धनात्मक, ऋणात्मक या शून्य) के लिए (n + 6)/(n - 2) भी एक पूर्णांक है?",
  ["4", "6", "7", "8"], 3,
  "(n + 6)/(n - 2) = 1 + 8/(n - 2), which is an integer exactly when n - 2 divides 8. The divisors of 8 are ±1, ±2, ±4 and ±8 -- eight of them -- giving n = 3, 1, 4, 0, 6, -2, 10 and -6. "
  "4 counts only the positive divisors; 6 and 7 drop the cases that make n zero or negative.",
  "(n + 6)/(n - 2) = 1 + 8/(n - 2), जो ठीक तब पूर्णांक है जब n - 2, 8 को विभाजित करे। 8 के भाजक ±1, ±2, ±4 और ±8 हैं -- आठ -- जिनसे n = 3, 1, 4, 0, 6, -2, 10 और -6 मिलते हैं। "
  "4 केवल धनात्मक भाजक गिनता है; 6 और 7 वे स्थितियाँ छोड़ देते हैं जिनमें n शून्य या ऋणात्मक है।",
  "qa-nt-when-n-plus-6-over-n-minus-2-is-an-integer", _nt6)

def _nt7():
    ks = [k for k in range(1, 60) if F(1, 4) < F(k, 60) < F(1, 3)]
    return str(len(ks))
N(QA, "Number Theory", "easy",
  "How many fractions of the form k/60, where k is a whole number, lie strictly between 1/4 and 1/3?",
  "k/60 के रूप वाले कितने भिन्न, जहाँ k एक पूर्ण संख्या है, 1/4 और 1/3 के ठीक बीच (सीमाओं को छोड़कर) स्थित हैं?",
  ["4", "5", "6", "7"], 0,
  "1/4 = 15/60 and 1/3 = 20/60, so k must lie strictly between 15 and 20: k = 16, 17, 18 or 19 -- four fractions. 5 and 6 include one or both of the end points, which 'strictly between' leaves out; 7 counts from 14 to 20.",
  "1/4 = 15/60 और 1/3 = 20/60, इसलिए k को 15 और 20 के ठीक बीच होना चाहिए: k = 16, 17, 18 या 19 -- चार भिन्न। 5 और 6 एक या दोनों सीमाओं को शामिल करते हैं, जिन्हें 'ठीक बीच' छोड़ देता है; 7, 14 से 20 तक गिनता है।",
  "qa-nt-sixtieths-between-a-quarter-and-a-third", _nt7)

def _nt8():
    assert 2 ** 10 == 1024
    return str(len(str(2 ** 30)))
N(QA, "Number Theory", "medium",
  "How many digits does the number 2³⁰ have?",
  "संख्या 2³⁰ में कितने अंक हैं?",
  ["10", "11", "15", "30"], 0,
  "2¹⁰ = 1,024, a little more than 10³, so 2³⁰ = (2¹⁰)³ is a little more than 10⁹: 1,024³ = 1,073,741,824, which has 10 digits. 11 would need 2³⁰ to reach 10¹⁰; 15 halves the exponent; 30 confuses the exponent with the number of digits.",
  "2¹⁰ = 1,024, जो 10³ से थोड़ा अधिक है, इसलिए 2³⁰ = (2¹⁰)³, 10⁹ से थोड़ा अधिक है: 1,024³ = 1,073,741,824, जिसमें 10 अंक हैं। 11 के लिए 2³⁰ को 10¹⁰ तक पहुँचना होगा; 15 घातांक को आधा कर देता है; 30 घातांक को अंकों की संख्या समझ लेता है।",
  "qa-nt-the-digits-of-2-to-the-30th", _nt8)

def _nt9():
    v = 5 * 6 * 7 * 8 + 1
    assert all(math.isqrt(n * (n + 1) * (n + 2) * (n + 3) + 1) == n * n + 3 * n + 1 for n in range(1, 50))
    return str(math.isqrt(v))
N(QA, "Number Theory", "medium",
  "5 × 6 × 7 × 8 + 1 is a perfect square. What is its square root?",
  "5 × 6 × 7 × 8 + 1 एक पूर्ण वर्ग है। उसका वर्गमूल क्या है?",
  ["39", "40", "41", "43"], 2,
  "The product of four consecutive numbers plus 1 is always a square: n(n + 1)(n + 2)(n + 3) + 1 = (n² + 3n + 1)². With n = 5, the root is 25 + 15 + 1 = 41 (check: 5 × 6 × 7 × 8 = 1,680, and 1,681 = 41²). "
  "40² = 1,600 and 39² = 1,521 are too small; 43² = 1,849 is too large.",
  "चार क्रमागत संख्याओं का गुणनफल धन 1 हमेशा एक वर्ग होता है: n(n + 1)(n + 2)(n + 3) + 1 = (n² + 3n + 1)²। n = 5 पर मूल 25 + 15 + 1 = 41 है (जाँच: 5 × 6 × 7 × 8 = 1,680, और 1,681 = 41²)। "
  "40² = 1,600 और 39² = 1,521 बहुत छोटे हैं; 43² = 1,849 बहुत बड़ा है।",
  "qa-nt-5-times-6-times-7-times-8-plus-1", _nt9)

def _nt10():
    pr = [p for p in range(2, 40) if all(p % q for q in range(2, p))][:10]
    s = str(math.prod(pr))
    return str(len(s) - len(s.rstrip("0")))
N(QA, "Number Theory", "medium",
  "The first ten prime numbers are multiplied together. With how many zeros does the product end?",
  "पहली दस अभाज्य संख्याओं को आपस में गुणा किया जाता है। गुणनफल के अंत में कितने शून्य हैं?",
  ["1", "2", "3", "10"], 0,
  "Each zero at the end needs a factor 10 = 2 × 5. Among the first ten primes (2, 3, 5, 7, 11, 13, 17, 19, 23, 29) the factor 2 and the factor 5 each appear exactly once, so the product (6,469,693,230) ends in exactly one zero. "
  "2 and 3 assume more 2s and 5s than the primes supply; 10 confuses the number of primes with the number of zeros.",
  "अंत के हर शून्य के लिए एक गुणनखंड 10 = 2 × 5 चाहिए। पहली दस अभाज्य संख्याओं (2, 3, 5, 7, 11, 13, 17, 19, 23, 29) में गुणनखंड 2 और गुणनखंड 5 हर एक ठीक एक बार आता है, इसलिए गुणनफल (6,469,693,230) के अंत में ठीक एक शून्य है। "
  "2 और 3 अभाज्य संख्याओं से मिलने वाले 2 और 5 से अधिक मान लेते हैं; 10 अभाज्यों की संख्या को शून्यों की संख्या समझ लेता है।",
  "qa-nt-the-zeros-at-the-end-of-a-product-of-primes", _nt10)

# ---------------------------------------------------------------- Speed-Distance-Time (4)
def _sdt1():
    met = [t for t in range(6 * 60, 12 * 60, 15) if 7 * 60 < t < 9 * 60]
    return str(len(met))
N(QA, "Speed-Distance-Time", "hard",
  "Buses leave town A for town B every 15 minutes from 6:00 a.m., and buses leave B for A every 15 minutes from 6:00 a.m. Every journey takes exactly 1 hour. How many buses coming from B does the 8:00 a.m. bus from A meet on the road, not counting any bus it passes at either bus station?",
  "नगर A से नगर B के लिए बसें सुबह 6:00 बजे से हर 15 मिनट पर चलती हैं, और B से A के लिए बसें भी सुबह 6:00 बजे से हर 15 मिनट पर। हर यात्रा में ठीक 1 घंटा लगता है। A से सुबह 8:00 बजे चली बस सड़क पर B से आने वाली कितनी बसों से मिलती है, किसी भी बस-अड्डे पर मिली बसों को छोड़कर?",
  ["4", "5", "7", "8"], 2,
  "The bus is on the road from 8:00 to 9:00. A bus from B is on the road at some moment in that hour if it left B after 7:00 (the 7:00 bus reaches A at 8:00, just as ours leaves -- at the station) and before 9:00 (the 9:00 bus is still at B when ours arrives). "
  "That is the buses leaving B at 7:15, 7:30, 7:45, 8:00, 8:15, 8:30 and 8:45: seven. 4 counts only the buses that leave B while ours is on the road; 5 and 8 add or drop an end case.",
  "बस 8:00 से 9:00 तक सड़क पर है। B से आने वाली कोई बस उस घंटे में किसी समय सड़क पर है यदि वह B से 7:00 के बाद चली (7:00 वाली बस 8:00 पर A पहुँचती है, ठीक जब हमारी बस चलती है -- अड्डे पर) और 9:00 से पहले (9:00 वाली बस हमारी बस के पहुँचने पर अभी B पर ही है)। "
  "यानी B से 7:15, 7:30, 7:45, 8:00, 8:15, 8:30 और 8:45 पर चली बसें: सात। 4 केवल वे बसें गिनता है जो हमारी बस के सड़क पर रहते B से चलती हैं; 5 और 8 किसी छोर की स्थिति जोड़ते या छोड़ते हैं।",
  "qa-sdt-buses-met-on-the-road", _sdt1)

def _sdt2():
    sols = [(a, b) for a in range(1, 10) for b in range(10) if (10 * b + a) - (10 * a + b) == (100 * a + b) - (10 * b + a) > 0]
    assert sols == [(1, 6)]
    a, b = sols[0]
    return f"{(10 * b + a) - (10 * a + b)} km/h"
N(QA, "Speed-Distance-Time", "hard",
  "A car moves at a steady speed. At noon it passes a milestone showing a two-digit number. At 1:00 p.m. it passes a milestone showing the same two digits in reverse order, and at 2:00 p.m. one showing a three-digit number made of the first two digits with a 0 between them. What is the car's speed?",
  "एक गाड़ी स्थिर चाल से चलती है। दोपहर 12 बजे वह दो अंकों की संख्या वाले एक मील-पत्थर को पार करती है। 1:00 बजे वह उन्हीं दो अंकों को उलटे क्रम में दिखाने वाले मील-पत्थर को पार करती है, और 2:00 बजे ऐसे मील-पत्थर को जिस पर पहले दो अंकों के बीच 0 रखकर बनी तीन अंकों की संख्या है। गाड़ी की चाल क्या है?",
  ["36 km/h", "40 km/h", "42 km/h", "45 km/h"], 3,
  "Let the first number be 10a + b. The second is 10b + a and the third 100a + b. Equal distances in equal times give (10b + a) - (10a + b) = (100a + b) - (10b + a), that is 9b - 9a = 99a - 9b, so 18b = 108a and b = 6a. With digits, a = 1 and b = 6: the milestones read 16, 61 and 106. "
  "The car covers 45 km each hour. 36 km/h would need the readings 15 and 51, but then the third reading, 105, is 54 km further on; 40 and 42 km/h cannot be the gap between a two-digit number and its reverse, which is always a multiple of 9.",
  "मान लीजिए पहली संख्या 10a + b है। दूसरी 10b + a और तीसरी 100a + b है। समान समय में समान दूरी से (10b + a) - (10a + b) = (100a + b) - (10b + a), यानी 9b - 9a = 99a - 9b, अतः 18b = 108a और b = 6a। अंकों के लिए a = 1 और b = 6: मील-पत्थरों पर 16, 61 और 106 हैं। "
  "गाड़ी हर घंटे 45 किमी चलती है। 36 किमी/घंटा के लिए पढ़ाइयाँ 15 और 51 चाहिए, पर तब तीसरी पढ़ाई, 105, 54 किमी आगे है; 40 और 42 किमी/घंटा दो अंकों की संख्या और उसकी उलटी संख्या का अंतर नहीं हो सकते, जो हमेशा 9 का गुणज होता है।",
  "qa-sdt-three-milestones", _sdt2,
  opts_hi=["36 किमी/घंटा", "40 किमी/घंटा", "42 किमी/घंटा", "45 किमी/घंटा"])

def _sdt3():
    left = F(45) - F(10, 30) * 60                 # minutes left after the first 10 km
    v = F(20) / (left / 60)
    assert left == 25
    return f"{v} km/h"
N(QA, "Speed-Distance-Time", "medium",
  "A courier must deliver a parcel to a place 30 km away by 10:00 a.m. She sets off at 9:15 a.m. and, because of traffic, covers the first 10 km at only 30 km/h. At what speed must she cover the rest of the way to arrive exactly on time?",
  "एक कूरियर को 30 किमी दूर एक स्थान पर सुबह 10:00 बजे तक पार्सल पहुँचाना है। वह सुबह 9:15 बजे निकलती है और, यातायात के कारण, पहले 10 किमी केवल 30 किमी/घंटा से तय करती है। ठीक समय पर पहुँचने के लिए उसे बाक़ी रास्ता किस चाल से तय करना होगा?",
  ["40 km/h", "45 km/h", "48 km/h", "50 km/h"], 2,
  "She has 45 minutes in all. The first 10 km at 30 km/h take 20 minutes, leaving 25 minutes for the remaining 20 km: 20 km ÷ 25/60 h = 48 km/h. "
  "40 km/h is the average speed needed for the whole 30 km in 45 minutes, which ignores the slow start; 45 and 50 km/h have no basis.",
  "उसके पास कुल 45 मिनट हैं। पहले 10 किमी, 30 किमी/घंटा से, 20 मिनट लेते हैं, जिससे बाक़ी 20 किमी के लिए 25 मिनट बचते हैं: 20 किमी ÷ 25/60 घंटा = 48 किमी/घंटा। "
  "40 किमी/घंटा पूरे 30 किमी को 45 मिनट में तय करने की औसत चाल है, जो धीमी शुरुआत को अनदेखा करती है; 45 और 50 किमी/घंटा का कोई आधार नहीं।",
  "qa-sdt-the-speed-needed-for-the-rest-of-a-trip", _sdt3,
  opts_hi=["40 किमी/घंटा", "45 किमी/घंटा", "48 किमी/घंटा", "50 किमी/घंटा"])

def _sdt4():
    ist = dt.datetime(2027, 1, 10, 10, 0)
    gmt_arrival = ist - dt.timedelta(hours=5, minutes=30) + dt.timedelta(hours=9)
    h, m = gmt_arrival.hour, gmt_arrival.minute
    assert (h, m) == (13, 30)
    return f"{h - 12 if h > 12 else h}:{m:02d} " + ("p.m." if h >= 12 else "a.m.")
N(QA, "Speed-Distance-Time", "medium",
  "A flight leaves Delhi at 10:00 a.m. Indian Standard Time and lands in London after 9 hours in the air. London keeps Greenwich Mean Time, which is 5 hours 30 minutes behind Indian Standard Time. What is the local time in London when the flight lands?",
  "एक उड़ान दिल्ली से भारतीय मानक समय के अनुसार सुबह 10:00 बजे चलती है और हवा में 9 घंटे बिताकर लंदन में उतरती है। लंदन ग्रीनविच माध्य समय मानता है, जो भारतीय मानक समय से 5 घंटे 30 मिनट पीछे है। उड़ान के उतरने पर लंदन का स्थानीय समय क्या है?",
  ["1:30 p.m.", "2:00 p.m.", "7:00 p.m.", "8:30 p.m."], 0,
  "10:00 a.m. in Delhi is 4:30 a.m. in London. Nine hours later it is 1:30 p.m. in London. 7:00 p.m. is the time in Delhi when the flight lands; 8:30 p.m. adds the time difference instead of subtracting it; 2:00 p.m. has no basis.",
  "दिल्ली में सुबह 10:00 बजे लंदन में सुबह 4:30 होते हैं। नौ घंटे बाद लंदन में दोपहर 1:30 होते हैं। शाम 7:00 बजे उड़ान उतरने के समय दिल्ली का समय है; रात 8:30 समय-अंतर को घटाने के बजाय जोड़ देता है; दोपहर 2:00 का कोई आधार नहीं।",
  "qa-sdt-a-flight-across-time-zones", _sdt4,
  opts_hi=["दोपहर 1:30", "दोपहर 2:00", "शाम 7:00", "रात 8:30"])

# ---------------------------------------------------------------- Ratio, Mixtures & Alligation (5)
def _rm1():
    import random
    rng = random.Random(7)
    meds = set()
    for _ in range(3000):
        xs = sorted(rng.sample(range(11, 90), 6))
        if xs[2] < 40 < xs[3]:
            data = sorted(xs[:3] + [40] + xs[3:] + [10, 90])
            meds.add(data[4])
    return str(meds.pop()) if len(meds) == 1 else "?"
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "The median of seven different numbers is 40. Two more numbers are added to the list: 10, which is smaller than all seven, and 90, which is larger than all seven. What is the median of the nine numbers?",
  "सात अलग-अलग संख्याओं की माध्यिका 40 है। सूची में दो और संख्याएँ जोड़ी जाती हैं: 10, जो सातों से छोटी है, और 90, जो सातों से बड़ी है। नौ संख्याओं की माध्यिका क्या है?",
  ["40", "45", "50", "It cannot be found without the seven numbers"], 0,
  "The median of seven numbers in order is the fourth, which is 40, with three numbers below it and three above. Adding one number below all of them and one above all of them gives four below 40 and four above it, so 40 is now the fifth of nine -- still the median. "
  "50 is the average of 10 and 90; 45 averages 40 with 50; and the median can be found, because only the order of the numbers matters, not their values.",
  "क्रम में रखी सात संख्याओं की माध्यिका चौथी संख्या है, जो 40 है, जिसके नीचे तीन और ऊपर तीन संख्याएँ हैं। सबसे नीचे एक और सबसे ऊपर एक संख्या जोड़ने पर 40 के नीचे चार और ऊपर चार हो जाती हैं, इसलिए 40 अब नौ में पाँचवीं है -- अब भी माध्यिका। "
  "50, 10 और 90 का औसत है; 45, 40 और 50 का औसत लेता है; और माध्यिका निकाली जा सकती है, क्योंकि केवल संख्याओं का क्रम मायने रखता है, उनके मान नहीं।",
  "qa-rm-a-median-after-two-additions", _rm1,
  opts_hi=["40", "45", "50", "सातों संख्याओं के बिना यह ज्ञात नहीं किया जा सकता"])

def _rm2():
    p = F(45 + 20 + 60, 50 + 40 + 80) * 100
    assert round(float(p), 1) == 73.5 and round((90 + 50 + 75) / 3, 1) == 71.7
    return "About 73.5 per cent"
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "A student scores 45 out of 50 in a quiz, 20 out of 40 in a project and 60 out of 80 in an examination. Taking all the marks together, what is her overall percentage?",
  "एक विद्यार्थी एक प्रश्नोत्तरी में 50 में से 45, एक परियोजना में 40 में से 20 और एक परीक्षा में 80 में से 60 अंक पाती है। सभी अंकों को एक साथ लेने पर उसका कुल प्रतिशत क्या है?",
  ["About 71.7 per cent", "About 73.5 per cent", "75 per cent", "About 76.7 per cent"], 1,
  "Overall, she scored 45 + 20 + 60 = 125 out of 50 + 40 + 80 = 170, which is 125/170, about 73.5 per cent. "
  "71.7 per cent is the simple average of her three percentages (90, 50 and 75), which gives each part equal weight although the parts carry different totals; 75 per cent is the examination alone; 76.7 per cent has no basis.",
  "कुल मिलाकर उसने 50 + 40 + 80 = 170 में से 45 + 20 + 60 = 125 अंक पाए, जो 125/170, लगभग 73.5 प्रतिशत है। "
  "71.7 प्रतिशत उसके तीन प्रतिशतों (90, 50 और 75) का साधारण औसत है, जो हर भाग को बराबर भार देता है यद्यपि भागों के कुल अंक अलग हैं; 75 प्रतिशत केवल परीक्षा का है; 76.7 प्रतिशत का कोई आधार नहीं।",
  "qa-rm-an-overall-percentage-from-marks-out-of-different-totals", _rm2,
  opts_hi=["लगभग 71.7 प्रतिशत", "लगभग 73.5 प्रतिशत", "75 प्रतिशत", "लगभग 76.7 प्रतिशत"])

def _rm3():
    return f"₹{float(F(8325, 100) * F(108, 100)):.2f}"
N(QA, "Ratio, Mixtures & Alligation", "easy",
  "On a certain day one US dollar buys ₹83.25, and one euro buys 1.08 US dollars. At these rates, how many rupees does one euro buy?",
  "किसी दिन एक अमेरिकी डॉलर से ₹83.25 मिलते हैं, और एक यूरो से 1.08 अमेरिकी डॉलर। इन दरों पर एक यूरो से कितने रुपये मिलेंगे?",
  ["₹77.08", "₹82.17", "₹84.33", "₹89.91"], 3,
  "One euro buys 1.08 dollars, and each dollar buys ₹83.25, so one euro buys 1.08 × 83.25 = ₹89.91. ₹77.08 divides by 1.08 instead of multiplying; ₹84.33 adds 1.08 to the rupee rate; ₹82.17 subtracts it.",
  "एक यूरो से 1.08 डॉलर मिलते हैं, और हर डॉलर से ₹83.25, इसलिए एक यूरो से 1.08 × 83.25 = ₹89.91 मिलते हैं। ₹77.08, 1.08 से गुणा करने के बजाय भाग देता है; ₹84.33 रुपये की दर में 1.08 जोड़ देता है; ₹82.17 उसे घटा देता है।",
  "qa-rm-a-chain-of-exchange-rates", _rm3)

def _rm4():
    r = F(4, 3) / F(7, 5)
    return f"{r.numerator} : {r.denominator}"
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "The areas of two districts are in the ratio 3 : 5 and their populations in the ratio 4 : 7. What is the ratio of their population densities (persons per square kilometre)?",
  "दो ज़िलों के क्षेत्रफल 3 : 5 के अनुपात में हैं और उनकी जनसंख्याएँ 4 : 7 के अनुपात में। उनके जनसंख्या घनत्वों (प्रति वर्ग किलोमीटर व्यक्ति) का अनुपात क्या है?",
  ["21 : 20", "12 : 35", "35 : 12", "20 : 21"], 3,
  "Density is population divided by area: (4/3) : (7/5) = 20/15 : 21/15 = 20 : 21. "
  "21 : 20 divides the other way round (area by population); 12 : 35 multiplies the two ratios, and 35 : 12 is that product turned over.",
  "घनत्व जनसंख्या को क्षेत्रफल से भाग देने पर मिलता है: (4/3) : (7/5) = 20/15 : 21/15 = 20 : 21। "
  "21 : 20 उलटे ढंग से भाग देता है (क्षेत्रफल को जनसंख्या से); 12 : 35 दोनों अनुपातों को गुणा करता है, और 35 : 12 उसी गुणनफल को उलट देता है।",
  "qa-rm-densities-from-two-ratios", _rm4)

def _rm5():
    sols = [(r, b) for r in range(3, 100) for b in range(5, 200) if F(r - 2, r + b - 2) == F(1, 5) and F(r, r + b - 4) == F(1, 4)]
    assert sols == [(12, 40)]
    return str(sum(sols[0]))
N(QA, "Ratio, Mixtures & Alligation", "hard",
  "A bag holds red and blue balls. If 2 red balls are taken out, one-fifth of the balls left are red. If instead 4 blue balls are taken out, one-quarter of the balls left are red. How many balls are in the bag?",
  "एक थैले में लाल और नीली गेंदें हैं। यदि 2 लाल गेंदें निकाली जाएँ, तो बची गेंदों में से पाँचवाँ भाग लाल है। यदि इसके बजाय 4 नीली गेंदें निकाली जाएँ, तो बची गेंदों में से चौथाई लाल हैं। थैले में कितनी गेंदें हैं?",
  ["48", "50", "52", "56"], 2,
  "With r red balls and n balls in all: r - 2 = (n - 2)/5 and r = (n - 4)/4. From the second, n = 4r + 4; putting this into the first, 5r - 10 = 4r + 2, so r = 12 and n = 52 (12 red, 40 blue). "
  "Check: removing 2 red leaves 10 red of 50, one-fifth; removing 4 blue leaves 12 red of 48, one-quarter. 50 and 48 are the numbers left after each removal, not the total; 56 does not fit.",
  "मान लीजिए r लाल गेंदें और कुल n गेंदें हैं: r - 2 = (n - 2)/5 और r = (n - 4)/4। दूसरे से n = 4r + 4; इसे पहले में रखने पर 5r - 10 = 4r + 2, अतः r = 12 और n = 52 (12 लाल, 40 नीली)। "
  "जाँच: 2 लाल निकालने पर 50 में से 10 लाल बचती हैं, पाँचवाँ भाग; 4 नीली निकालने पर 48 में से 12 लाल, चौथाई। 50 और 48 हर निकासी के बाद बची संख्याएँ हैं, कुल नहीं; 56 ठीक नहीं बैठता।",
  "qa-rm-red-balls-after-two-removals", _rm5)

# ---------------------------------------------------------------- Percentage & Profit-Loss (3)
def _pp1():
    return f"₹{float(2000 * F(90, 100) * F(105, 100) * F(105, 100)):,.2f}"
N(QA, "Percentage & Profit-Loss", "medium",
  "A restaurant bill of ₹2,000 first gets a 10 per cent discount. A 5 per cent service charge is then added on the discounted amount, and finally a 5 per cent tax is charged on the total so far. What is the final amount payable?",
  "एक रेस्तराँ के ₹2,000 के बिल पर पहले 10 प्रतिशत छूट मिलती है। फिर छूट के बाद की राशि पर 5 प्रतिशत सेवा शुल्क जोड़ा जाता है, और अंत में अब तक के कुल पर 5 प्रतिशत कर लगाया जाता है। देय अंतिम राशि क्या है?",
  ["₹1,980.00", "₹1,984.50", "₹2,000.00", "₹2,005.00"], 1,
  "Each step multiplies the amount: 2,000 × 0.90 = 1,800; × 1.05 = 1,890; × 1.05 = ₹1,984.50. "
  "₹2,000 assumes that a 10 per cent cut and two 5 per cent additions cancel, but each percentage applies to a different base; ₹1,980 and ₹2,005 come from applying the steps to the wrong amounts.",
  "हर चरण राशि को गुणा करता है: 2,000 × 0.90 = 1,800; × 1.05 = 1,890; × 1.05 = ₹1,984.50। "
  "₹2,000 मान लेता है कि 10 प्रतिशत की कटौती और 5 प्रतिशत के दो जोड़ एक-दूसरे को काट देते हैं, पर हर प्रतिशत अलग आधार पर लगता है; ₹1,980 और ₹2,005 चरणों को ग़लत राशियों पर लगाने से आते हैं।",
  "qa-pp-a-bill-after-a-discount-a-service-charge-and-a-tax", _pp1)

def _pp2():
    d = (dt.date(2027, 4, 15) - dt.date(2027, 2, 1)).days
    assert d == 73
    return f"₹{int(73000 * F(10, 100) * F(d, 365)):,}"
N(QA, "Percentage & Profit-Loss", "hard",
  "₹73,000 is lent at simple interest of 10 per cent a year from 1 February 2027 to 15 April 2027, interest being charged for each day after the day of lending up to and including the day of repayment, on a 365-day year. How much interest is due?",
  "₹73,000, 10 प्रतिशत वार्षिक साधारण ब्याज पर 1 फ़रवरी 2027 से 15 अप्रैल 2027 तक उधार दिए जाते हैं; ब्याज उधार देने के दिन के बाद से चुकाने के दिन तक (उसे मिलाकर) हर दिन के लिए, 365 दिनों के वर्ष पर लगता है। कितना ब्याज देय है?",
  ["₹1,400", "₹1,460", "₹1,500", "₹1,520"], 1,
  "The days counted are the remaining 27 days of February (2027 is not a leap year, so February has 28), all 31 of March and the first 15 of April: 27 + 31 + 15 = 73 days. "
  "Interest = 73,000 × 10/100 × 73/365 = 7,300 × 1/5 = ₹1,460. ₹1,500 treats the period as two and a half months of a twelve-month year; ₹1,520 counts 76 days; ₹1,400 counts 70.",
  "गिने जाने वाले दिन फ़रवरी के बचे 27 दिन (2027 अधिवर्ष नहीं है, इसलिए फ़रवरी में 28 दिन हैं), मार्च के सभी 31 और अप्रैल के पहले 15 हैं: 27 + 31 + 15 = 73 दिन। "
  "ब्याज = 73,000 × 10/100 × 73/365 = 7,300 × 1/5 = ₹1,460। ₹1,500 अवधि को बारह महीनों के वर्ष के ढाई महीने मानता है; ₹1,520, 76 दिन गिनता है; ₹1,400, 70।",
  "qa-pp-simple-interest-by-the-day", _pp2)

def _pp3():
    return f"{float(F(45, 3600) * 100)} per cent"
N(QA, "Percentage & Profit-Loss", "easy",
  "What percentage of one hour is 45 seconds?",
  "45 सेकंड एक घंटे का कितना प्रतिशत है?",
  ["0.0125 per cent", "0.125 per cent", "0.75 per cent", "1.25 per cent"], 3,
  "One hour is 3,600 seconds, and 45/3,600 = 1/80 = 0.0125, which is 1.25 per cent. 0.0125 per cent reads the fraction 0.0125 as a percentage; 0.75 per cent treats the hour as 6,000 seconds; 0.125 per cent treats it as 36,000 seconds.",
  "एक घंटा 3,600 सेकंड है, और 45/3,600 = 1/80 = 0.0125, जो 1.25 प्रतिशत है। 0.0125 प्रतिशत, भिन्न 0.0125 को ही प्रतिशत पढ़ लेता है; 0.75 प्रतिशत घंटे को 6,000 सेकंड मानता है; 0.125 प्रतिशत उसे 36,000 सेकंड मानता है।",
  "qa-pp-45-seconds-as-a-share-of-an-hour", _pp3,
  opts_hi=["0.0125 प्रतिशत", "0.125 प्रतिशत", "0.75 प्रतिशत", "1.25 प्रतिशत"])

# ---------------------------------------------------------------- Sequences & Series (2)
def _ss1():
    a = [2 ** k for k in range(1, 6)]; b = [3 ** k for k in range(1, 6)]
    s = [x for pair in zip(a, b) for x in pair]
    assert s[:7] == [2, 3, 4, 9, 8, 27, 16]
    return str(s[7])
N(QA, "Sequences & Series", "easy",
  "What is the next number in the series 2, 3, 4, 9, 8, 27, 16, ...?",
  "श्रेणी 2, 3, 4, 9, 8, 27, 16, ... की अगली संख्या क्या है?",
  ["32", "54", "64", "81"], 3,
  "Two series are interleaved: the terms in odd places are powers of 2 (2, 4, 8, 16) and those in even places powers of 3 (3, 9, 27). The next term is in an even place, so it is 3⁴ = 81. "
  "32 continues the powers of 2, which comes one place later; 54 doubles 27; 64 is 4³.",
  "दो श्रेणियाँ आपस में गुँथी हैं: विषम स्थानों के पद 2 की घातें हैं (2, 4, 8, 16) और सम स्थानों के 3 की घातें (3, 9, 27)। अगला पद सम स्थान पर है, इसलिए वह 3⁴ = 81 है। "
  "32, 2 की घातों को आगे बढ़ाता है, जो एक स्थान बाद आता है; 54, 27 को दोगुना करता है; 64 = 4³।",
  "qa-ss-two-interleaved-series", _ss1)

def _ss2():
    s = sum(1 - F(1, 2 ** k) for k in range(1, 6))
    assert s == 4 + F(1, 32)
    return "4 1/32"
N(QA, "Sequences & Series", "medium",
  "What is the sum of the first five terms of the series 1/2, 3/4, 7/8, 15/16, ...?",
  "श्रेणी 1/2, 3/4, 7/8, 15/16, ... के पहले पाँच पदों का योग क्या है?",
  ["3 31/32", "4 1/32", "4 31/32", "5"], 1,
  "Each term is 1 less a power of one-half: 1 - 1/2, 1 - 1/4, 1 - 1/8, 1 - 1/16, and the fifth is 1 - 1/32 = 31/32. The sum is 5 - (1/2 + 1/4 + 1/8 + 1/16 + 1/32) = 5 - 31/32 = 4 1/32. "
  "5 ignores the parts taken away; 4 31/32 takes away only 1/32; 3 31/32 sums only the first four terms and adds back a fraction.",
  "हर पद 1 में से आधे की कोई घात घटाने पर मिलता है: 1 - 1/2, 1 - 1/4, 1 - 1/8, 1 - 1/16, और पाँचवाँ 1 - 1/32 = 31/32 है। योग 5 - (1/2 + 1/4 + 1/8 + 1/16 + 1/32) = 5 - 31/32 = 4 1/32 है। "
  "5 घटाए गए भागों की अनदेखी करता है; 4 31/32 केवल 1/32 घटाता है; 3 31/32 केवल पहले चार पद जोड़कर एक भिन्न वापस जोड़ देता है।",
  "qa-ss-a-sum-of-fractions-that-approach-1", _ss2)

# ---------------------------------------------------------------- Permutation & Combination (3)
def _pc1():
    return str(sum(1 for a, b in combinations(range(10), 2) if b - a > 1))
N(QA, "Permutation & Combination", "hard",
  "Two friends are to be seated in a row of 10 empty chairs so that they are not next to each other. In how many ways can the two chairs be chosen?",
  "दो मित्रों को 10 ख़ाली कुर्सियों की एक पंक्ति में ऐसे बैठाना है कि वे एक-दूसरे के बग़ल में न हों। दोनों कुर्सियाँ कितने तरीक़ों से चुनी जा सकती हैं?",
  ["36", "40", "45", "72"], 0,
  "There are 10C2 = 45 ways to choose any two chairs, and 9 of these pairs are next to each other (chairs 1-2, 2-3, ..., 9-10). That leaves 45 - 9 = 36. "
  "45 ignores the condition; 72 counts each pair twice, once for each friend in each chair, though the question asks only for the chairs; 40 subtracts only 5 adjacent pairs.",
  "किन्हीं दो कुर्सियों को चुनने के 10C2 = 45 तरीक़े हैं, और इनमें से 9 जोड़े एक-दूसरे के बग़ल में हैं (कुर्सियाँ 1-2, 2-3, ..., 9-10)। इससे 45 - 9 = 36 बचते हैं। "
  "45 शर्त को अनदेखा करता है; 72 हर जोड़े को दो बार गिनता है, हर मित्र को हर कुर्सी पर रखकर, यद्यपि प्रश्न केवल कुर्सियाँ पूछता है; 40 केवल 5 सटे जोड़े घटाता है।",
  "qa-pc-two-chairs-that-are-not-side-by-side", _pc1)

def _pc2():
    p = F(sum(1 for x in range(10, 100) if x % 3 == 0 or x % 5 == 0), 90)
    return f"{p.numerator}/{p.denominator}"
N(QA, "Permutation & Combination", "medium",
  "A two-digit number is chosen at random. What is the probability that it is a multiple of 3 or of 5 (or of both)?",
  "दो अंकों की एक संख्या यादृच्छिक रूप से चुनी जाती है। इसकी प्रायिकता क्या है कि वह 3 का या 5 का (या दोनों का) गुणज हो?",
  ["7/15", "8/15", "1/2", "8/9"], 0,
  "There are 90 two-digit numbers. Multiples of 3 among them: 12 to 99, 30 numbers; multiples of 5: 10 to 95, 18 numbers; multiples of both (that is, of 15): 15 to 90, 6 numbers. So 30 + 18 - 6 = 42 qualify, and 42/90 = 7/15. "
  "8/15 adds 30 and 18 without removing the 6 counted twice; 1/2 and 8/9 have no basis.",
  "दो अंकों की 90 संख्याएँ हैं। उनमें 3 के गुणज: 12 से 99, 30 संख्याएँ; 5 के गुणज: 10 से 95, 18 संख्याएँ; दोनों के (यानी 15 के) गुणज: 15 से 90, 6 संख्याएँ। अतः 30 + 18 - 6 = 42 संख्याएँ योग्य हैं, और 42/90 = 7/15। "
  "8/15, 30 और 18 को जोड़ता है पर दो बार गिनी गई 6 को नहीं घटाता; 1/2 और 8/9 का कोई आधार नहीं।",
  "qa-pc-two-digit-multiples-of-3-or-5", _pc2)

def _pc3():
    return str(len(set(permutations("xyz"))))
N(QA, "Permutation & Combination", "medium",
  "An ant walks along the edges of a cube from one corner to the corner diagonally opposite it, using the fewest possible edges. How many different routes can it take?",
  "एक चींटी एक घन के किनारों के साथ एक कोने से उसके ठीक विपरीत (विकर्णतः सामने वाले) कोने तक, कम से कम किनारों का प्रयोग करते हुए, चलती है। वह कितने अलग-अलग रास्ते ले सकती है?",
  ["3", "6", "8", "12"], 1,
  "The shortest route uses three edges, one in each of the three directions (length, breadth and height), and they can be taken in any order: 3 × 2 × 1 = 6 routes. "
  "3 counts only the choice of the first edge; 8 is the number of corners; 12 is the number of edges.",
  "सबसे छोटा रास्ता तीन किनारों का है, तीनों दिशाओं (लंबाई, चौड़ाई और ऊँचाई) में एक-एक, और उन्हें किसी भी क्रम में लिया जा सकता है: 3 × 2 × 1 = 6 रास्ते। "
  "3 केवल पहले किनारे का चुनाव गिनता है; 8 कोनों की संख्या है; 12 किनारों की संख्या है।",
  "qa-pc-shortest-routes-along-a-cube-s-edges", _pc3)

# ---------------------------------------------------------------- Geometry & Mensuration (2)
def _gm1():
    return f"{int(math.sqrt(4 ** 2 + 3 ** 2 + 12 ** 2))} cm"
N(QA, "Geometry & Mensuration", "medium",
  "What is the length of the longest straight rod that can be placed inside a closed box measuring 12 cm × 4 cm × 3 cm?",
  "12 सेमी × 4 सेमी × 3 सेमी माप वाले एक बंद डिब्बे के भीतर रखी जा सकने वाली सबसे लंबी सीधी छड़ की लंबाई क्या है?",
  ["5 cm", "12.6 cm", "13 cm", "19 cm"], 2,
  "The longest rod runs from one corner to the opposite corner through the box: √(12² + 4² + 3²) = √(144 + 16 + 9) = √169 = 13 cm. "
  "12.6 cm is the diagonal of the largest face (√160), which a rod lying flat on the floor of the box would take; 5 cm is the diagonal of the 4 × 3 face; 19 cm adds the three edges.",
  "सबसे लंबी छड़ डिब्बे के भीतर एक कोने से सामने वाले कोने तक जाती है: √(12² + 4² + 3²) = √(144 + 16 + 9) = √169 = 13 सेमी। "
  "12.6 सेमी सबसे बड़े फलक का विकर्ण (√160) है, जो डिब्बे के तल पर लेटी छड़ लेगी; 5 सेमी, 4 × 3 फलक का विकर्ण है; 19 सेमी तीनों किनारों को जोड़ता है।",
  "qa-gm-the-longest-rod-in-a-box", _gm1,
  opts_hi=["5 सेमी", "12.6 सेमी", "13 सेमी", "19 सेमी"])

def _gm2():
    return f"{F(15, 100) * 360}°"
N(QA, "Geometry & Mensuration", "easy",
  "In a pie chart of a family's monthly spending, rent takes 15 per cent of the total. What angle does the rent sector make at the centre?",
  "किसी परिवार के मासिक व्यय के एक पाई-चार्ट में किराया कुल का 15 प्रतिशत है। किराये वाला क्षेत्र केंद्र पर कितना कोण बनाता है?",
  ["15°", "36°", "54°", "60°"], 2,
  "The whole pie is 360°, so 15 per cent of it is 0.15 × 360° = 54°. 15° reads the percentage as degrees; 36° is 10 per cent; 60° is about 16.7 per cent.",
  "पूरा पाई 360° है, इसलिए उसका 15 प्रतिशत 0.15 × 360° = 54° है। 15° प्रतिशत को अंश पढ़ लेता है; 36°, 10 प्रतिशत है; 60° लगभग 16.7 प्रतिशत है।",
  "qa-gm-a-pie-chart-sector", _gm2)

# ---------------------------------------------------------------- Time & Work (2)
def _tw1():
    t = F(1, 2) / F(1, 4) + F(1, 2) / (F(1, 4) - F(1, 8))
    return f"{t} hours"
N(QA, "Time & Work", "hard",
  "A pipe fills an empty tank in 4 hours. Halfway up the side of the tank there is a hole which, whenever the water is above it, lets water out at a rate that would empty a full tank in 8 hours. With the hole open, how long does the pipe take to fill the empty tank?",
  "एक पाइप ख़ाली टंकी को 4 घंटे में भरता है। टंकी की दीवार पर आधी ऊँचाई पर एक छेद है, जो पानी के उसके ऊपर होने पर ऐसी दर से पानी निकालता है जो भरी टंकी को 8 घंटे में ख़ाली कर दे। छेद खुला रहते पाइप ख़ाली टंकी को कितने समय में भरेगा?",
  ["6 hours", "7 hours", "8 hours", "10 hours"], 0,
  "Below the hole nothing leaks, so the lower half fills at the pipe's full rate in 2 hours. Above the hole the net rate is 1/4 - 1/8 = 1/8 of the tank an hour, so the upper half takes 4 hours. In all, 2 + 4 = 6 hours. "
  "8 hours applies the leak for the whole time; 7 and 10 hours have no basis.",
  "छेद के नीचे कुछ नहीं रिसता, इसलिए निचला आधा भाग पाइप की पूरी दर से 2 घंटे में भरता है। छेद के ऊपर शुद्ध दर 1/4 - 1/8 = प्रति घंटे टंकी का 1/8 है, इसलिए ऊपरी आधा भाग 4 घंटे लेता है। कुल 2 + 4 = 6 घंटे। "
  "8 घंटे रिसाव को पूरे समय पर लागू करता है; 7 और 10 घंटे का कोई आधार नहीं।",
  "qa-tw-a-leak-halfway-up-a-tank", _tw1,
  opts_hi=["6 घंटे", "7 घंटे", "8 घंटे", "10 घंटे"])

def _tw2():
    sols = [(n, d) for n in range(5, 100) for d in range(3, 100) if (n + 4) * (d - 2) == n * d and (n - 4) * (d + 3) == n * d]
    assert sols == [(20, 12)]
    return str(sols[0][0])
N(QA, "Time & Work", "medium",
  "A gang of workers can finish a job in a certain number of days. With 4 more workers it would finish 2 days sooner; with 4 fewer it would take 3 days longer. How many workers are in the gang? (All the workers work at the same rate.)",
  "मज़दूरों की एक टोली एक काम कुछ निश्चित दिनों में पूरा कर सकती है। 4 और मज़दूरों के साथ वह 2 दिन पहले पूरा करती; 4 कम मज़दूरों के साथ 3 दिन अधिक लगते। टोली में कितने मज़दूर हैं? (सभी मज़दूर एक ही दर से काम करते हैं।)",
  ["12", "16", "20", "24"], 2,
  "With n workers taking d days, the job is nd worker-days. (n + 4)(d - 2) = nd gives 4d - 2n = 8, and (n - 4)(d + 3) = nd gives 3n - 4d = 12. Adding the two, n = 20, and then d = 12. "
  "Check: 24 workers take 10 days and 16 workers take 15 days, both 240 worker-days. 12 is the number of days; 16 and 24 are the gang sizes in the two what-ifs.",
  "n मज़दूरों के d दिन लेने पर काम nd मज़दूर-दिन का है। (n + 4)(d - 2) = nd से 4d - 2n = 8, और (n - 4)(d + 3) = nd से 3n - 4d = 12। दोनों को जोड़ने पर n = 20, और तब d = 12। "
  "जाँच: 24 मज़दूर 10 दिन और 16 मज़दूर 15 दिन लेते हैं, दोनों 240 मज़दूर-दिन। 12 दिनों की संख्या है; 16 और 24 दोनों 'यदि' स्थितियों में टोली के आकार हैं।",
  "qa-tw-a-gang-of-workers-from-two-what-ifs", _tw2)

# ---------------------------------------------------------------- Puzzle Hybrid (5)
def _ph1():
    same = lambda y: dt.date(y, 1, 1).weekday() == dt.date(2027, 1, 1).weekday() and (y % 4 == 0) == (2027 % 4 == 0)
    return str(next(y for y in range(2028, 2100) if same(y)))
N(QA, "Puzzle Hybrid", "hard",
  "1 January 2027 is a Friday. In which year after 2027 will the calendar first be exactly the same as that of 2027 (every date falling on the same day of the week)?",
  "1 जनवरी 2027 शुक्रवार है। 2027 के बाद किस वर्ष में कैलेंडर पहली बार ठीक 2027 जैसा होगा (हर तारीख़ सप्ताह के उसी दिन पड़े)?",
  ["2033", "2034", "2035", "2038"], 3,
  "The new year must also start on a Friday and must not be a leap year. A common year moves 1 January on by one weekday, a leap year by two. From 2027: 2028 starts on Saturday, 2029 Monday (2028 was a leap year), 2030 Tuesday, 2031 Wednesday, 2032 Thursday, 2033 Saturday (2032 was a leap year), 2034 Sunday, 2035 Monday, 2036 Tuesday, 2037 Thursday (2036 was a leap year), 2038 Friday. "
  "2038 is not a leap year, so it matches. 2033 is the answer for those who add 6 years and forget the leap days; 2034 and 2035 start on Sunday and Monday.",
  "नए वर्ष को भी शुक्रवार से शुरू होना चाहिए और अधिवर्ष नहीं होना चाहिए। साधारण वर्ष 1 जनवरी को एक दिन आगे खिसकाता है, अधिवर्ष दो दिन। 2027 से: 2028 शनिवार से शुरू होता है, 2029 सोमवार (2028 अधिवर्ष था), 2030 मंगलवार, 2031 बुधवार, 2032 गुरुवार, 2033 शनिवार (2032 अधिवर्ष था), 2034 रविवार, 2035 सोमवार, 2036 मंगलवार, 2037 गुरुवार (2036 अधिवर्ष था), 2038 शुक्रवार। "
  "2038 अधिवर्ष नहीं है, इसलिए वह मेल खाता है। जो 6 वर्ष जोड़कर अधिवर्ष के दिन भूल जाए, उसके लिए 2033 उत्तर है; 2034 और 2035 रविवार और सोमवार से शुरू होते हैं।",
  "qa-ph-the-year-whose-calendar-matches-2027", _ph1)

def _ph2():
    tasks = [5, 4, 3, 3, 3]
    best = min(max(sum(t for i, t in enumerate(tasks) if m >> i & 1), sum(t for i, t in enumerate(tasks) if not m >> i & 1)) for m in range(32))
    return f"{best} hours"
N(QA, "Puzzle Hybrid", "medium",
  "Five jobs take 5, 4, 3, 3 and 3 hours. Two workers share them, each job being done wholly by one worker, and both start at the same time. What is the least time in which all five jobs can be finished?",
  "पाँच कामों में 5, 4, 3, 3 और 3 घंटे लगते हैं। दो कामगार उन्हें बाँट लेते हैं, हर काम पूरी तरह एक ही कामगार करता है, और दोनों एक साथ शुरू करते हैं। सभी पाँच काम कम से कम कितने समय में पूरे हो सकते हैं?",
  ["8 hours", "9 hours", "10 hours", "11 hours"], 1,
  "The jobs add up to 18 hours, so one worker must do at least 9. Nine is reached exactly: one worker takes the 5- and 4-hour jobs, the other the three 3-hour jobs. "
  "8 hours is impossible, since 18 hours of work cannot fit into 2 × 8 = 16; 10 and 11 hours come from less even splits, such as 5 + 3 + 3 against 4 + 3.",
  "कामों का योग 18 घंटे है, इसलिए किसी एक कामगार को कम से कम 9 घंटे का काम करना होगा। नौ ठीक-ठीक संभव है: एक कामगार 5 और 4 घंटे वाले काम लेता है, दूसरा तीनों 3 घंटे वाले। "
  "8 घंटे असंभव है, क्योंकि 18 घंटे का काम 2 × 8 = 16 में नहीं समा सकता; 10 और 11 घंटे कम समान बँटवारों से आते हैं, जैसे 5 + 3 + 3 बनाम 4 + 3।",
  "qa-ph-two-workers-sharing-five-jobs", _ph2,
  opts_hi=["8 घंटे", "9 घंटे", "10 घंटे", "11 घंटे"])

def _ph3():
    days = 7
    n = next(k for k in range(1, 30) if k > days)       # k people can all differ only while k <= 7
    return str(n)
N(QA, "Puzzle Hybrid", "easy",
  "What is the smallest number of people that must be in a room to be sure that at least two of them were born on the same day of the week?",
  "किसी कमरे में कम से कम कितने लोग होने चाहिए ताकि यह निश्चित हो कि उनमें से कम से कम दो का जन्म सप्ताह के एक ही दिन हुआ था?",
  ["8", "9", "14", "15"], 0,
  "There are seven days of the week, so seven people could all have been born on different days. An eighth person must share a day with one of them. So 8 is the least number that makes it certain. "
  "9 is one more than needed; 15 is the number needed to be sure that three people share a day; 14 merely doubles 7.",
  "सप्ताह में सात दिन हैं, इसलिए सात लोग सब अलग-अलग दिनों में जन्मे हो सकते हैं। आठवें व्यक्ति को उनमें से किसी के साथ दिन साझा करना ही होगा। अतः 8 वह न्यूनतम संख्या है जो इसे निश्चित करती है। "
  "9 आवश्यकता से एक अधिक है; 15 यह निश्चित करने के लिए चाहिए कि तीन लोग एक दिन साझा करें; 14 केवल 7 को दोगुना करता है।",
  "qa-ph-the-weekday-pigeonhole", _ph3)

def _ph4():
    bags = [k for k in range(1, 11) if 10 * 55 + k == 553]
    assert sum(range(1, 11)) == 55
    return f"Bag {bags[0]}"
N(QA, "Puzzle Hybrid", "medium",
  "Ten bags, numbered 1 to 10, each hold many coins. Genuine coins weigh 10 g each, but every coin in one of the bags weighs 11 g. One coin is taken from bag 1, two from bag 2, three from bag 3, and so on up to ten from bag 10, and all these coins are weighed together once. The total is 553 g. Which bag holds the heavy coins?",
  "1 से 10 तक क्रमांकित दस थैलों में से हर एक में बहुत-से सिक्के हैं। असली सिक्के 10 ग्राम के हैं, पर एक थैले का हर सिक्का 11 ग्राम का है। थैले 1 से एक सिक्का, थैले 2 से दो, थैले 3 से तीन, और इसी तरह थैले 10 से दस सिक्के निकालकर सबको एक साथ एक बार तौला जाता है। कुल भार 553 ग्राम है। भारी सिक्के किस थैले में हैं?",
  ["Bag 3", "Bag 5", "Bag 7", "Bag 10"], 0,
  "1 + 2 + ... + 10 = 55 coins are weighed. If all were genuine they would weigh 550 g. Each heavy coin adds 1 g, and the heavy bag contributed as many coins as its number, so the extra 3 g means bag 3. "
  "Bag 5 and bag 7 would give 555 g and 557 g; bag 10 would give 560 g.",
  "1 + 2 + ... + 10 = 55 सिक्के तौले जाते हैं। यदि सब असली होते तो उनका भार 550 ग्राम होता। हर भारी सिक्का 1 ग्राम जोड़ता है, और भारी थैले ने अपने क्रमांक जितने सिक्के दिए, इसलिए अतिरिक्त 3 ग्राम का अर्थ है थैला 3। "
  "थैला 5 और थैला 7 से 555 और 557 ग्राम मिलते; थैला 10 से 560 ग्राम।",
  "qa-ph-the-bag-of-heavy-coins-found-in-one-weighing", _ph4,
  opts_hi=["थैला 3", "थैला 5", "थैला 7", "थैला 10"])

def _ph5():
    best = min(math.hypot(1, 1 + 1), math.hypot(1 + 1, 1))          # unfold two faces into a 2 × 1 rectangle
    assert abs(best ** 2 - 5) < 1e-12 and best < 1 + math.sqrt(2) < 3
    return "√5 m"
N(QA, "Puzzle Hybrid", "hard",
  "An ant at one corner of a cube with edges 1 m long crawls over the surface of the cube to the corner diagonally opposite. What is the shortest distance it can crawl?",
  "1 मीटर लंबे किनारों वाले एक घन के एक कोने पर बैठी चींटी घन की सतह पर रेंगते हुए ठीक विपरीत (विकर्णतः सामने वाले) कोने तक जाती है। वह कम से कम कितनी दूरी रेंगकर पहुँच सकती है?",
  ["√3 m", "√5 m", "(1 + √2) m", "3 m"], 1,
  "Unfold the two faces the ant crosses so that they lie flat side by side: they form a 2 m × 1 m rectangle, with the two corners at opposite ends of its diagonal. The straight line across it is √(2² + 1²) = √5 m, about 2.24 m, crossing the shared edge at its midpoint. "
  "√3 m (about 1.73 m) goes through the inside of the cube, which the ant cannot; (1 + √2) m, about 2.41 m, goes along one edge and then diagonally across a face; 3 m follows three edges.",
  "चींटी जिन दो फलकों को पार करती है उन्हें खोलकर समतल पर साथ-साथ रखिए: वे 2 मीटर × 1 मीटर का आयत बनाते हैं, जिसके विकर्ण के दोनों छोरों पर दोनों कोने हैं। उसके आर-पार सीधी रेखा √(2² + 1²) = √5 मीटर, लगभग 2.24 मीटर है, जो साझे किनारे को उसके मध्य-बिंदु पर काटती है। "
  "√3 मीटर (लगभग 1.73 मीटर) घन के भीतर से जाता है, जहाँ चींटी नहीं जा सकती; (1 + √2) मीटर, लगभग 2.41 मीटर, एक किनारे के साथ और फिर एक फलक के विकर्ण पर जाता है; 3 मीटर तीन किनारों के साथ चलता है।",
  "qa-ph-an-ant-crossing-a-cube", _ph5,
  opts_hi=["√3 मीटर", "√5 मीटर", "(1 + √2) मीटर", "3 मीटर"])

# ---------------------------------------------------------------- the data-sufficiency block's two Quant items
def _ds1():
    pairs = [(F(b, 2), F(s, 2)) for b in range(1, 60) for s in range(1, 60) if s < b]   # (boat, stream) in km/h
    s1 = {b for b, s in pairs if b + s == 12}
    s2 = {b for b, s in pairs if b - s == 8}
    both = {b for b, s in pairs if b + s == 12 and b - s == 8}
    assert both == {10}
    return _ds(s1, s2, both)
DS(QA, "medium",
   "What is the speed of a boat in still water?",
   "शांत जल में एक नाव की चाल क्या है?",
   "The boat covers 12 km downstream in 1 hour.", "नाव धारा के साथ 1 घंटे में 12 किमी तय करती है।",
   "The boat covers 8 km upstream in 1 hour.", "नाव धारा के विरुद्ध 1 घंटे में 8 किमी तय करती है।",
   2,
   "Statement I gives only the sum of the boat's speed and the stream's (12 km/h), and Statement II only their difference (8 km/h); neither alone fixes the boat's speed. Together, the boat's speed is half their sum, (12 + 8)/2 = 10 km/h (and the stream's 2 km/h). Both are needed.",
   "कथन I केवल नाव और धारा की चालों का योग (12 किमी/घंटा) देता है, और कथन II केवल उनका अंतर (8 किमी/घंटा); अकेले कोई भी नाव की चाल तय नहीं करता। दोनों साथ: नाव की चाल उनके योग का आधा है, (12 + 8)/2 = 10 किमी/घंटा (और धारा की 2 किमी/घंटा)। दोनों आवश्यक हैं।",
   "qa-ds-a-boat-s-speed-from-two-runs", _ds1)

def _ds2():
    times = [(h, m) for h in range(1, 13) for m in range(60)]
    hour_angle = lambda h, m: (h % 12) * 30 + m / 2
    s1 = {(h, m) for h, m in times if hour_angle(h, m) == 3 * 30 + 15}         # I: hour hand halfway between 3 and 4
    s2 = {(h, m) for h, m in times if m == 30 and h == 3}                       # II: minute hand at 6, between 3 and 4 o'clock
    assert s1 == s2 == {(3, 30)}
    return _ds(s1, s2, s1 & s2)
DS(QA, "medium",
   "What time does a clock show?",
   "एक घड़ी क्या समय दिखा रही है?",
   "The hour hand is exactly halfway between 3 and 4.", "घंटे की सुई 3 और 4 के ठीक बीच में है।",
   "The minute hand points exactly at 6, and the time is between 3 o'clock and 4 o'clock.", "मिनट की सुई ठीक 6 पर है, और समय 3 बजे और 4 बजे के बीच है।",
   1,
   "Statement I: the hour hand moves steadily from 3 to 4 during that hour, so being exactly halfway means half the hour has passed -- 3:30. Statement II: between 3 and 4, the minute hand at 6 means 30 minutes past -- 3:30. Each statement alone gives the time.",
   "कथन I: घंटे की सुई उस घंटे में 3 से 4 तक समान रूप से चलती है, इसलिए ठीक बीच में होने का अर्थ है कि आधा घंटा बीत चुका -- 3:30। कथन II: 3 और 4 के बीच, मिनट की सुई का 6 पर होना 30 मिनट बीतने का अर्थ है -- 3:30। हर कथन अकेले समय बता देता है।",
   "qa-ds-a-clock-time-found-two-ways", _ds2)
