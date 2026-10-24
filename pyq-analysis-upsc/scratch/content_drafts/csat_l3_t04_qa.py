# -*- coding: utf-8 -*-
"""CSAT Level 3 · Test 4 -- Quantitative Aptitude (34 items: 32 in the Quant slots, 2 in the data-sufficiency block).

Level 3's harder mix (3 easy / 15 medium / 16 hard) with none of the shapes of Level 2 Tests 1-7, Level 1 Minis 1-3 or
Level 3 Tests 1-3: two co-prime numbers from their LCM, 999 × 999 + 999, consecutive falling digits reversed, the
largest prime factor of 3,003, a root nested for ever, whole numbers within 5 of 3, the sum of three-digit
palindromes, two-digit numbers with exactly one 5; a 25 per cent rise in speed, a goods train at half the speed, two
wheels of different sizes, a walker who must get 2 km ahead; a share in 5 : 7, a price index with weights, apples and
mangoes after two rises, three averages taken in pairs, pupils who move between two schools; the largest discount a
50 per cent mark-up allows, a deposit made at the start of each year, an instalment's hidden interest; a series that
adds its own digit sum, an AP found from two sums; a committee with no couple in it, two books at the ends; the area an hour hand
sweeps, right triangles on a hypotenuse of 25; two typists who finish together, the time of a pair from each one's
extra time; weed that doubles every day, a game of taking coins, the fewest coins for ₹38, the pages on one sheet of a
booklet; and two data-sufficiency items. Every key is worked out in code by check()."""
from fractions import Fraction as F
from itertools import combinations, permutations, product
import math
import csat_common as c
from csat_common import N, DS, QA

def _ds(s1, s2, both):
    alone = (len(set(s1)) == 1, len(set(s2)) == 1)
    return "b" if all(alone) else "a" if any(alone) else "c" if len(set(both)) == 1 else "d"

# ---------------------------------------------------------------- Number Theory (8)
def _nt1():
    xs = [x for x in range(2, 400) if math.gcd(17, x) == 1 and 17 * x == 391]
    assert xs == [23]
    return "23"
N(QA, "Number Theory", "easy",
  "The LCM of two co-prime numbers is 391, and one of them is 17. What is the other?",
  "दो सह-अभाज्य संख्याओं का LCM 391 है, और उनमें से एक 17 है। दूसरी संख्या क्या है?",
  ["11", "13", "19", "23"], 3,
  "Co-prime numbers have no common factor other than 1, so their LCM is simply their product: the other number is 391 ÷ 17 = 23. "
  "With 11, 13 or 19 the product would be 187, 221 or 323, not 391.",
  "सह-अभाज्य संख्याओं का 1 के अलावा कोई उभयनिष्ठ गुणनखंड नहीं होता, इसलिए उनका LCM बस उनका गुणनफल है: दूसरी संख्या 391 ÷ 17 = 23 है। "
  "11, 13 और 19 के साथ 17 का गुणनफल 391 नहीं होता (17 × 11 = 187, 17 × 13 = 221, 17 × 19 = 323)।",
  "qa-nt-two-co-prime-numbers-from-their-lcm", _nt1)

def _nt2():
    v = 999 * 999 + 999
    assert v == 999 * 1000 and 999 * 999 == 998001
    return f"{v:,}"
N(QA, "Number Theory", "medium",
  "What is the value of 999 × 999 + 999?",
  "999 × 999 + 999 का मान क्या है?",
  ["998,001", "999,000", "999,999", "1,000,000"], 1,
  "Take 999 out as a common factor: 999 × 999 + 999 = 999 × (999 + 1) = 999 × 1,000 = 999,000. "
  "998,001 is 999 × 999 alone; 999,999 is 999 × 1,001; 1,000,000 is 1,000 × 1,000.",
  "999 को उभयनिष्ठ गुणनखंड के रूप में बाहर निकालिए: 999 × 999 + 999 = 999 × (999 + 1) = 999 × 1,000 = 999,000। "
  "998,001 केवल 999 × 999 है; 999,999 = 999 × 1,001; 1,000,000 = 1,000 × 1,000।",
  "qa-nt-999-times-999-plus-999", _nt2)

def _nt3():
    diffs = {int(f"{a}{a - 1}{a - 2}") - int(f"{a - 2}{a - 1}{a}") for a in range(3, 10)}
    assert diffs == {198}
    return "198"
N(QA, "Number Theory", "medium",
  "A three-digit number has digits that are consecutive and decrease from left to right, such as 543. When the number formed by reversing its digits is subtracted from it, the result is always:",
  "तीन अंकों की एक संख्या के अंक क्रमागत हैं और बाएँ से दाएँ घटते हैं, जैसे 543। जब उसके अंक उलटकर बनी संख्या को उसमें से घटाया जाता है, तो परिणाम हमेशा होता है:",
  ["198", "297", "396", "495"], 0,
  "Write the digits as a, a - 1 and a - 2. The number is 100a + 10(a - 1) + (a - 2) and its reverse 100(a - 2) + 10(a - 1) + a; the middle digits cancel, and the difference is 99a - 99(a - 2) = 198, whatever a is (543 - 345 = 198, 987 - 789 = 198). "
  "297, 396 and 495 would need the end digits to differ by 3, 4 and 5, not 2.",
  "अंकों को a, a - 1 और a - 2 लिखिए। संख्या 100a + 10(a - 1) + (a - 2) है और उलटी संख्या 100(a - 2) + 10(a - 1) + a; बीच के अंक कट जाते हैं, और अंतर 99a - 99(a - 2) = 198 है, a चाहे जो हो (543 - 345 = 198, 987 - 789 = 198)। "
  "297, 396 और 495 के लिए छोर के अंकों में 2 के बजाय 3, 4 और 5 का अंतर चाहिए।",
  "qa-nt-consecutive-falling-digits-reversed", _nt3)

def _nt4():
    n, f, ps = 3003, 2, []
    while n > 1:
        while n % f == 0:
            ps.append(f); n //= f
        f += 1
    assert ps == [3, 7, 11, 13]
    return str(max(ps))
N(QA, "Number Theory", "medium",
  "What is the largest prime factor of 3,003?",
  "3,003 का सबसे बड़ा अभाज्य गुणनखंड क्या है?",
  ["3", "7", "11", "13"], 3,
  "3,003 = 3 × 1,001, and 1,001 = 7 × 11 × 13, so 3,003 = 3 × 7 × 11 × 13 and its largest prime factor is 13. "
  "3, 7 and 11 are also prime factors of 3,003, but smaller ones.",
  "3,003 = 3 × 1,001, और 1,001 = 7 × 11 × 13, इसलिए 3,003 = 3 × 7 × 11 × 13 और उसका सबसे बड़ा अभाज्य गुणनखंड 13 है। "
  "3, 7 और 11 भी 3,003 के अभाज्य गुणनखंड हैं, पर छोटे।",
  "qa-nt-the-largest-prime-factor-of-3003", _nt4)

def _nt5():
    x = 0.0
    for _ in range(200):
        x = math.sqrt(12 + x)
    assert abs(x - 4) < 1e-12
    return "4"
N(QA, "Number Theory", "hard",
  "If x = √(12 + √(12 + √(12 + ...))), the roots going on for ever, what is the value of x?",
  "यदि x = √(12 + √(12 + √(12 + ...))), जहाँ मूल अनंत तक चलते जाते हैं, तो x का मान क्या है?",
  ["3", "2√3", "4", "6"], 2,
  "The expression under the first root is 12 plus the whole expression again, so x = √(12 + x). Squaring, x² = x + 12, that is (x - 4)(x + 3) = 0. x is positive, so x = 4 (check: √(12 + 4) = 4). "
  "2√3 = √12 takes only the first root; 3 is the size of the negative root, -3, which a square root cannot equal; 6 has no basis.",
  "पहले मूल के नीचे का व्यंजक 12 और फिर से पूरा व्यंजक है, इसलिए x = √(12 + x)। वर्ग करने पर x² = x + 12, यानी (x - 4)(x + 3) = 0। x धनात्मक है, इसलिए x = 4 (जाँच: √(12 + 4) = 4)। "
  "2√3 = √12 केवल पहला मूल लेता है; 3 ऋणात्मक मूल -3 का परिमाण है, जिसके बराबर कोई वर्गमूल नहीं हो सकता; 6 का कोई आधार नहीं।",
  "qa-nt-a-root-nested-for-ever", _nt5)

def _nt6():
    xs = [x for x in range(-50, 50) if abs(x - 3) < 5]
    assert xs[0] == -1 and xs[-1] == 7
    return str(len(xs))
N(QA, "Number Theory", "medium",
  "How many integers x satisfy |x - 3| < 5, that is, lie less than 5 away from 3 on the number line?",
  "कितने पूर्णांक x, |x - 3| < 5 को संतुष्ट करते हैं, यानी संख्या रेखा पर 3 से 5 से कम दूरी पर हैं?",
  ["6", "7", "8", "9"], 3,
  "|x - 3| < 5 means -5 < x - 3 < 5, that is -2 < x < 8. The integers are -1, 0, 1, ..., 7: nine of them. "
  "8 leaves out -1; 7 counts only the natural numbers 1 to 7; 6 has no basis.",
  "|x - 3| < 5 का अर्थ है -5 < x - 3 < 5, यानी -2 < x < 8। पूर्णांक -1, 0, 1, ..., 7 हैं: कुल नौ। "
  "8, -1 को छोड़ देता है; 7 केवल प्राकृत संख्याएँ 1 से 7 गिनता है; 6 का कोई आधार नहीं।",
  "qa-nt-whole-numbers-within-5-of-3", _nt6)

def _nt7():
    pal = [n for n in range(100, 1000) if str(n) == str(n)[::-1]]
    assert len(pal) == 90
    return f"{sum(pal):,}"
N(QA, "Number Theory", "hard",
  "What is the sum of all the three-digit numbers that read the same forwards and backwards (such as 121 and 707)?",
  "उन सभी तीन अंकों की संख्याओं का योग क्या है जो आगे और पीछे से एक जैसी पढ़ी जाती हैं (जैसे 121 और 707)?",
  ["49,500", "49,950", "50,000", "54,450"], 0,
  "Such a number is aba = 101a + 10b, with a from 1 to 9 and b from 0 to 9: 90 numbers. Each a appears with 10 values of b, so the a-parts add up to 101 × 10 × (1 + ... + 9) = 101 × 450 = 45,450; each b appears with 9 values of a, so the b-parts add up to 10 × 9 × (0 + ... + 9) = 4,050. "
  "The total is 45,450 + 4,050 = 49,500 (equivalently, 90 numbers averaging 550). 49,950 takes the average as 555; 50,000 rounds; 54,450 counts 99 such numbers instead of 90.",
  "ऐसी संख्या aba = 101a + 10b है, जहाँ a 1 से 9 तक और b 0 से 9 तक: 90 संख्याएँ। हर a, b के 10 मानों के साथ आता है, इसलिए a-भागों का योग 101 × 10 × (1 + ... + 9) = 101 × 450 = 45,450 है; हर b, a के 9 मानों के साथ आता है, इसलिए b-भागों का योग 10 × 9 × (0 + ... + 9) = 4,050 है। "
  "कुल 45,450 + 4,050 = 49,500 है (इसी तरह, 550 औसत वाली 90 संख्याएँ)। 49,950 औसत को 555 मानता है; 50,000 पूर्णांकित करता है; 54,450 ऐसी 90 के बजाय 99 संख्याएँ गिनता है।",
  "qa-nt-the-sum-of-three-digit-palindromes", _nt7)

def _nt8():
    xs = [n for n in range(10, 100) if str(n).count("5") == 1]
    assert len([n for n in range(10, 100) if "5" in str(n)]) == 18
    return str(len(xs))
N(QA, "Number Theory", "hard",
  "How many two-digit numbers have exactly one digit equal to 5?",
  "दो अंकों की कितनी संख्याओं में ठीक एक अंक 5 है?",
  ["15", "16", "17", "18"], 2,
  "With 5 in the tens place and not in the units place: 50 to 59 except 55, that is 9 numbers. With 5 in the units place and not in the tens place: 15, 25, ..., 95 except 55, that is 8 numbers. In all 9 + 8 = 17. "
  "18 counts the numbers with at least one 5, which includes 55; 15 and 16 leave out some of the numbers.",
  "दहाई के स्थान पर 5 और इकाई पर नहीं: 50 से 59 तक, 55 को छोड़कर, यानी 9 संख्याएँ। इकाई के स्थान पर 5 और दहाई पर नहीं: 15, 25, ..., 95, 55 को छोड़कर, यानी 8 संख्याएँ। कुल 9 + 8 = 17। "
  "18 कम से कम एक 5 वाली संख्याएँ गिनता है, जिसमें 55 भी है; 15 और 16 कुछ संख्याएँ छोड़ देते हैं।",
  "qa-nt-two-digit-numbers-with-exactly-one-5", _nt8)

# ---------------------------------------------------------------- Speed-Distance-Time (4)
def _sdt1():
    fall = 1 - 1 / F(125, 100)
    assert fall == F(1, 5)
    return "20 per cent"
N(QA, "Speed-Distance-Time", "medium",
  "If a car's speed is increased by 25 per cent, by what percentage does the time it takes for a given journey fall?",
  "यदि किसी कार की चाल 25 प्रतिशत बढ़ा दी जाए, तो किसी दी गई यात्रा में लगने वाला समय कितने प्रतिशत घटता है?",
  ["20 per cent", "25 per cent", "75 per cent", "80 per cent"], 0,
  "For a fixed distance, time varies inversely as speed. The speed becomes 5/4 of what it was, so the time becomes 4/5 of what it was: a fall of 1/5, that is 20 per cent. "
  "25 per cent assumes that time falls by the same percentage as speed rises; 80 per cent is the time that remains, not the fall; 75 per cent has no basis.",
  "निश्चित दूरी के लिए समय चाल के व्युत्क्रमानुपाती होता है। चाल पहले की 5/4 हो जाती है, इसलिए समय पहले का 4/5 हो जाता है: 1/5 की कमी, यानी 20 प्रतिशत। "
  "25 प्रतिशत मान लेता है कि समय उतने ही प्रतिशत घटता है जितनी चाल बढ़ती है; 80 प्रतिशत बचा हुआ समय है, कमी नहीं; 75 प्रतिशत का कोई आधार नहीं।",
  "qa-sdt-a-25-per-cent-rise-in-speed", _sdt1,
  opts_hi=["20 प्रतिशत", "25 प्रतिशत", "75 प्रतिशत", "80 प्रतिशत"])

def _sdt2():
    t = F(3, 4) / F(1, 2) * 4
    assert t == 6
    return "6 h"
N(QA, "Speed-Distance-Time", "medium",
  "A passenger train covers the distance between two cities in 4 hours. A goods train runs at half the passenger train's speed. How long does the goods train take to cover three-quarters of that distance?",
  "एक सवारी गाड़ी दो शहरों के बीच की दूरी 4 घंटे में तय करती है। एक मालगाड़ी सवारी गाड़ी की आधी चाल से चलती है। मालगाड़ी को उस दूरी का तीन-चौथाई तय करने में कितना समय लगेगा?",
  ["3 h", "4 h 30 min", "6 h", "8 h"], 2,
  "At half the speed the goods train would take twice as long for the whole distance, 8 hours; for three-quarters of it, it takes 3/4 × 8 = 6 hours. "
  "8 h is the time for the whole distance; 3 h is three-quarters of the passenger train's time; 4 h 30 min has no basis.",
  "आधी चाल पर मालगाड़ी को पूरी दूरी में दोगुना, यानी 8 घंटे लगते; उसके तीन-चौथाई के लिए 3/4 × 8 = 6 घंटे लगते हैं। "
  "8 घंटे पूरी दूरी का समय है; 3 घंटे सवारी गाड़ी के समय का तीन-चौथाई है; 4 घंटे 30 मिनट का कोई आधार नहीं।",
  "qa-sdt-a-goods-train-at-half-the-speed", _sdt2,
  opts_hi=["3 घंटे", "4 घंटे 30 मिनट", "6 घंटे", "8 घंटे"])

def _sdt3():
    ds = [d for d in range(1, 500) if F(d, 2) - F(d, 3) == 10]
    assert ds == [60]
    return f"{ds[0]} m"
N(QA, "Speed-Distance-Time", "hard",
  "The front wheel of a cart has a circumference of 2 m and the rear wheel a circumference of 3 m. Over what distance does the front wheel make 10 more revolutions than the rear wheel?",
  "एक गाड़ी के अगले पहिये की परिधि 2 मीटर और पिछले पहिये की परिधि 3 मीटर है। कितनी दूरी में अगला पहिया पिछले पहिये से 10 चक्कर अधिक लगाता है?",
  ["20 m", "30 m", "45 m", "60 m"], 3,
  "Over a distance d the front wheel turns d/2 times and the rear wheel d/3 times. The difference is d/2 - d/3 = d/6 = 10, so d = 60 m (30 turns against 20). "
  "20 m and 30 m are the distances covered by 10 turns of the front and of the rear wheel; 45 m has no basis.",
  "दूरी d में अगला पहिया d/2 बार और पिछला d/3 बार घूमता है। अंतर d/2 - d/3 = d/6 = 10, इसलिए d = 60 मीटर (30 चक्कर बनाम 20)। "
  "20 मीटर और 30 मीटर अगले और पिछले पहिये के 10 चक्करों में तय दूरियाँ हैं; 45 मीटर का कोई आधार नहीं।",
  "qa-sdt-two-wheels-of-different-sizes", _sdt3,
  opts_hi=["20 मीटर", "30 मीटर", "45 मीटर", "60 मीटर"])

def _sdt4():
    t = next(F(k, 10) for k in range(1, 200) if 5 * F(k, 10) - (4 + 3 * F(k, 10)) == 2)
    assert t == 3 and F(4, 2) == 2
    return f"{t} h"
N(QA, "Speed-Distance-Time", "hard",
  "A starts walking 4 km ahead of B, and both walk in the same direction along a road, A at 3 km/h and B at 5 km/h, starting at the same time. After how long will B be 2 km ahead of A?",
  "A, B से 4 किमी आगे से चलना शुरू करता है, और दोनों एक ही समय पर एक सड़क पर एक ही दिशा में चलते हैं, A 3 किमी/घंटा से और B 5 किमी/घंटा से। कितने समय बाद B, A से 2 किमी आगे होगा?",
  ["2 h", "3 h", "4 h", "6 h"], 1,
  "B gains 5 - 3 = 2 km on A every hour. To be 2 km ahead, B must first make up the 4 km by which A started ahead and then gain 2 km more: 6 km in all, which takes 3 hours. "
  "2 h is only the time to catch up with A; 4 h and 6 h overshoot.",
  "B हर घंटे A पर 5 - 3 = 2 किमी की बढ़त बनाता है। 2 किमी आगे होने के लिए B को पहले वे 4 किमी पाटने होंगे जिनसे A आगे से चला, और फिर 2 किमी और बढ़त बनानी होगी: कुल 6 किमी, जिसमें 3 घंटे लगते हैं। "
  "2 घंटे केवल A तक पहुँचने का समय है; 4 और 6 घंटे आगे निकल जाते हैं।",
  "qa-sdt-a-walker-who-must-get-2-km-ahead", _sdt4,
  opts_hi=["2 घंटे", "3 घंटे", "4 घंटे", "6 घंटे"])

# ---------------------------------------------------------------- Ratio, Mixtures & Alligation (5)
def _rm1():
    b = F(840) * F(7, 12)
    assert b == 490
    return "₹490"
N(QA, "Ratio, Mixtures & Alligation", "easy",
  "₹840 is divided between A and B in the ratio 5 : 7. How much does B get?",
  "₹840 को A और B में 5 : 7 के अनुपात में बाँटा जाता है। B को कितना मिलता है?",
  ["₹350", "₹420", "₹490", "₹588"], 2,
  "The ratio has 5 + 7 = 12 parts, each worth 840 ÷ 12 = ₹70, so B gets 7 × 70 = ₹490 (and A ₹350). "
  "₹350 is A's share; ₹420 divides the money equally; ₹588 takes 7/10 of 840.",
  "अनुपात में 5 + 7 = 12 भाग हैं, हर एक 840 ÷ 12 = ₹70 का, इसलिए B को 7 × 70 = ₹490 मिलते हैं (और A को ₹350)। "
  "₹350, A का हिस्सा है; ₹420 राशि को बराबर बाँटता है; ₹588, 840 का 7/10 लेता है।",
  "qa-rm-a-share-in-5-to-7", _rm1)

def _rm2():
    rise = F(60, 100) * 10 + F(40, 100) * 25
    assert rise == 16
    return "16 per cent"
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "A household's price index is built from two goods, food with a weight of 60 and fuel with a weight of 40. Over a year the price of food rises by 10 per cent and that of fuel by 25 per cent. By how much does the index rise?",
  "किसी परिवार का मूल्य सूचकांक दो वस्तुओं से बना है, भोजन जिसका भार 60 है और ईंधन जिसका भार 40। एक वर्ष में भोजन का मूल्य 10 प्रतिशत और ईंधन का 25 प्रतिशत बढ़ता है। सूचकांक कितना बढ़ता है?",
  ["16 per cent", "17.5 per cent", "25 per cent", "35 per cent"], 0,
  "The index rises by the weighted average of the two rises: (60 × 10 + 40 × 25) ÷ 100 = (600 + 1,000) ÷ 100 = 16 per cent. "
  "17.5 per cent is the simple average, which ignores the weights; 35 per cent adds the two rises; 25 per cent takes only the larger one.",
  "सूचकांक दोनों वृद्धियों के भारित औसत जितना बढ़ता है: (60 × 10 + 40 × 25) ÷ 100 = (600 + 1,000) ÷ 100 = 16 प्रतिशत। "
  "17.5 प्रतिशत साधारण औसत है, जो भारों को अनदेखा करता है; 35 प्रतिशत दोनों वृद्धियाँ जोड़ता है; 25 प्रतिशत केवल बड़ी वृद्धि लेता है।",
  "qa-rm-a-price-index-with-weights", _rm2,
  opts_hi=["16 प्रतिशत", "17.5 प्रतिशत", "25 प्रतिशत", "35 प्रतिशत"])

def _rm3():
    sols = [(a, m) for a in range(1, 200) for m in range(1, 200)
            if 3 * a + 4 * m == 520 and F(33, 10) * a + F(48, 10) * m == 600]
    assert sols == [(80, 70)]
    return "₹80"
N(QA, "Ratio, Mixtures & Alligation", "hard",
  "3 kg of apples and 4 kg of mangoes together cost ₹520. If the price of apples rises by 10 per cent and that of mangoes by 20 per cent, the same quantities cost ₹600. What is the original price of apples per kg?",
  "3 किग्रा सेब और 4 किग्रा आम मिलकर ₹520 के हैं। यदि सेब का मूल्य 10 प्रतिशत और आम का 20 प्रतिशत बढ़े, तो वही मात्राएँ ₹600 की होती हैं। सेब का मूल मूल्य प्रति किग्रा क्या है?",
  ["₹70", "₹80", "₹90", "₹100"], 1,
  "With apples at a and mangoes at m a kg: 3a + 4m = 520 and 3.3a + 4.8m = 600. Multiplying the first by 1.1 gives 3.3a + 4.4m = 572; subtracting, 0.4m = 28, so m = ₹70 and then 3a = 240, a = ₹80. "
  "₹70 is the price of mangoes; ₹90 and ₹100 do not satisfy both equations.",
  "सेब a और आम m रुपये प्रति किग्रा मानिए: 3a + 4m = 520 और 3.3a + 4.8m = 600। पहले को 1.1 से गुणा करने पर 3.3a + 4.4m = 572; घटाने पर 0.4m = 28, अतः m = ₹70 और फिर 3a = 240, a = ₹80। "
  "₹70 आम का मूल्य है; ₹90 और ₹100 दोनों समीकरण पूरे नहीं करते।",
  "qa-rm-apples-and-mangoes-after-two-rises", _rm3)

def _rm4():
    a, b, c_ = 2 * 30, 2 * 40, 2 * 35          # A + B, B + C, C + A
    total = F(a + b + c_, 2)
    assert total == 105
    return str(int(total / 3))
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "The average of A and B is 30, the average of B and C is 40, and the average of C and A is 35. What is the average of A, B and C?",
  "A और B का औसत 30 है, B और C का औसत 40 है, और C और A का औसत 35 है। A, B और C का औसत क्या है?",
  ["21", "28", "30", "35"], 3,
  "The pair sums are A + B = 60, B + C = 80 and C + A = 70. Adding them counts each number twice: 2(A + B + C) = 210, so A + B + C = 105 and the average is 35. "
  "It is also the average of the three pair averages, since each number appears in two of the pairs. 30 and 28 do not use all three pairs; 21 divides 105 by 5.",
  "जोड़ों के योग A + B = 60, B + C = 80 और C + A = 70 हैं। इन्हें जोड़ने पर हर संख्या दो बार गिनी जाती है: 2(A + B + C) = 210, अतः A + B + C = 105 और औसत 35 है। "
  "यह तीनों जोड़ों के औसतों का औसत भी है, क्योंकि हर संख्या दो जोड़ों में आती है। 30 और 28 तीनों जोड़ों का प्रयोग नहीं करते; 21, 105 को 5 से भाग देता है।",
  "qa-rm-three-averages-taken-in-pairs", _rm4)

def _rm5():
    ks = [k for k in range(6, 200) if F(5 * k + 30, 6 * k - 30) == F(6, 5)]
    assert ks == [30]
    return str(11 * ks[0])
N(QA, "Ratio, Mixtures & Alligation", "hard",
  "The numbers of pupils in two schools are in the ratio 5 : 6. If 30 pupils move from the second school to the first, the ratio becomes 6 : 5. How many pupils are there in the two schools together?",
  "दो विद्यालयों में विद्यार्थियों की संख्याएँ 5 : 6 के अनुपात में हैं। यदि 30 विद्यार्थी दूसरे विद्यालय से पहले में चले जाएँ, तो अनुपात 6 : 5 हो जाता है। दोनों विद्यालयों में कुल कितने विद्यार्थी हैं?",
  ["220", "264", "330", "396"], 2,
  "Let the schools have 5k and 6k pupils. After the move they have 5k + 30 and 6k - 30, and (5k + 30)/(6k - 30) = 6/5 gives 25k + 150 = 36k - 180, so k = 30: the schools had 150 and 180, which become 180 and 150. The total, unchanged by the move, is 330. "
  "220, 264 and 396 take 20, 24 and 36 as the size of a part, and none of them gives 6 : 5 after the move.",
  "मान लीजिए विद्यालयों में 5k और 6k विद्यार्थी हैं। जाने के बाद उनमें 5k + 30 और 6k - 30 हैं, और (5k + 30)/(6k - 30) = 6/5 से 25k + 150 = 36k - 180, अतः k = 30: विद्यालयों में 150 और 180 थे, जो 180 और 150 हो जाते हैं। कुल, जो जाने से नहीं बदलता, 330 है। "
  "220, 264 और 396 एक भाग का आकार 20, 24 और 36 मानते हैं, और इनमें से कोई भी जाने के बाद 6 : 5 नहीं देता।",
  "qa-rm-pupils-who-move-between-two-schools", _rm5)

# ---------------------------------------------------------------- Percentage & Profit-Loss (3)
def _pp1():
    d = 1 - F(100, 150)
    assert d == F(1, 3)
    return "33⅓ per cent"
N(QA, "Percentage & Profit-Loss", "medium",
  "A shopkeeper marks his goods 50 per cent above cost. What is the largest discount on the marked price that he can give without making a loss?",
  "एक दुकानदार अपने सामान का अंकित मूल्य लागत से 50 प्रतिशत अधिक रखता है। बिना हानि के वह अंकित मूल्य पर अधिकतम कितनी छूट दे सकता है?",
  ["25 per cent", "33⅓ per cent", "50 per cent", "66⅔ per cent"], 1,
  "Take the cost as 100; the marked price is 150. He can come down to 100 without loss, a cut of 50 on 150, which is 1/3, or 33⅓ per cent of the marked price. "
  "50 per cent assumes the discount can equal the mark-up, but half of 150 is 75, below cost: the discount is measured on the larger marked price, so it is smaller than the mark-up. 66⅔ per cent is the part of the marked price he must still receive, not the discount; 25 per cent leaves some profit but is not the largest discount.",
  "लागत 100 मानिए; अंकित मूल्य 150 है। वह बिना हानि के 100 तक आ सकता है, 150 पर 50 की कटौती, जो 1/3, यानी अंकित मूल्य का 33⅓ प्रतिशत है। "
  "50 प्रतिशत मान लेता है कि छूट वृद्धि के बराबर हो सकती है, पर 150 का आधा 75 है, जो लागत से कम है: छूट बड़े अंकित मूल्य पर मापी जाती है, इसलिए वह वृद्धि से छोटी है। 66⅔ प्रतिशत अंकित मूल्य का वह भाग है जो उसे अब भी मिलना चाहिए, छूट नहीं; 25 प्रतिशत कुछ लाभ छोड़ता है, पर अधिकतम छूट नहीं है।",
  "qa-pp-the-largest-discount-a-50-per-cent-mark-up-allows", _pp1,
  opts_hi=["25 प्रतिशत", "33⅓ प्रतिशत", "50 प्रतिशत", "66⅔ प्रतिशत"])

def _pp2():
    amt = sum(1000 + 1000 * F(10, 100) * years for years in (3, 2, 1))
    assert amt == 3600 and round(1000 * (1.1 ** 3 + 1.1 ** 2 + 1.1)) == 3641
    return "₹3,600"
N(QA, "Percentage & Profit-Loss", "medium",
  "A person deposits ₹1,000 at the start of each year for three years in a scheme that pays 10 per cent simple interest a year on every deposit. How much is in the account at the end of the third year?",
  "एक व्यक्ति तीन वर्षों तक हर वर्ष के आरंभ में ₹1,000 एक ऐसी योजना में जमा करता है जो हर जमा पर 10 प्रतिशत वार्षिक साधारण ब्याज देती है। तीसरे वर्ष के अंत में खाते में कितनी राशि है?",
  ["₹3,300", "₹3,310", "₹3,600", "₹3,641"], 2,
  "The first deposit earns interest for 3 years (₹300), the second for 2 (₹200) and the third for 1 (₹100). The account holds 3,000 + 600 = ₹3,600. "
  "₹3,300 gives every deposit only one year's interest; ₹3,641 compounds the interest, which the scheme does not do; ₹3,310 has no basis.",
  "पहली जमा पर 3 वर्ष (₹300), दूसरी पर 2 (₹200) और तीसरी पर 1 वर्ष (₹100) का ब्याज मिलता है। खाते में 3,000 + 600 = ₹3,600 हैं। "
  "₹3,300 हर जमा को केवल एक वर्ष का ब्याज देता है; ₹3,641 ब्याज को चक्रवृद्धि करता है, जो योजना नहीं करती; ₹3,310 का कोई आधार नहीं।",
  "qa-pp-a-deposit-made-at-the-start-of-each-year", _pp2)

def _pp3():
    borrowed = 20000 - 5000
    r = F(16000 - borrowed, borrowed)
    assert r == F(1, 15)
    return "6⅔ per cent"
N(QA, "Percentage & Profit-Loss", "hard",
  "A television costs ₹20,000 in cash. It can instead be bought for ₹5,000 down and ₹16,000 paid one year later. What rate of interest a year is hidden in the instalment offer?",
  "एक टेलीविज़न नक़द में ₹20,000 का है। उसे इसके बजाय ₹5,000 अग्रिम और एक वर्ष बाद ₹16,000 देकर भी ख़रीदा जा सकता है। किस्त वाले प्रस्ताव में कितनी वार्षिक ब्याज दर छिपी है?",
  ["5 per cent", "6⅔ per cent", "8 per cent", "10 per cent"], 1,
  "After the down payment the buyer in effect borrows the rest of the cash price, 20,000 - 5,000 = ₹15,000, and repays ₹16,000 a year later. The interest is ₹1,000 on ₹15,000, that is 1/15 or 6⅔ per cent a year. "
  "5 per cent divides the ₹1,000 by the full cash price of ₹20,000, though only ₹15,000 is borrowed; 8 and 10 per cent have no basis.",
  "अग्रिम भुगतान के बाद ख़रीदार वास्तव में नक़द मूल्य का शेष, 20,000 - 5,000 = ₹15,000 उधार लेता है, और एक वर्ष बाद ₹16,000 चुकाता है। ब्याज ₹15,000 पर ₹1,000 है, यानी 1/15 या 6⅔ प्रतिशत वार्षिक। "
  "5 प्रतिशत ₹1,000 को पूरे नक़द मूल्य ₹20,000 से भाग देता है, यद्यपि उधार केवल ₹15,000 लिया गया; 8 और 10 प्रतिशत का कोई आधार नहीं।",
  "qa-pp-an-instalment-s-hidden-interest", _pp3,
  opts_hi=["5 प्रतिशत", "6⅔ प्रतिशत", "8 प्रतिशत", "10 प्रतिशत"])

# ---------------------------------------------------------------- Sequences & Series (2)
def _ss1():
    t = [13]
    while len(t) < 8:
        t.append(t[-1] + sum(map(int, str(t[-1]))))
    assert t[:7] == [13, 17, 25, 32, 37, 47, 58]
    return str(t[7])
N(QA, "Sequences & Series", "hard",
  "What is the next number in the series 13, 17, 25, 32, 37, 47, 58, ...?",
  "श्रेणी 13, 17, 25, 32, 37, 47, 58, ... की अगली संख्या क्या है?",
  ["65", "67", "69", "71"], 3,
  "The differences 4, 8, 7, 5, 10, 11 follow no arithmetic pattern; they are the digit sums of the terms. Each term is the previous term plus the sum of its own digits: 13 + (1 + 3) = 17, 17 + 8 = 25, 25 + 7 = 32, 32 + 5 = 37, 37 + 10 = 47, 47 + 11 = 58, so the next is 58 + (5 + 8) = 71. "
  "69 repeats the last step of 11; 65 and 67 come from guessing at a pattern in the differences.",
  "अंतर 4, 8, 7, 5, 10, 11 किसी अंकगणितीय क्रम में नहीं हैं; वे पदों के अंकों के योग हैं। हर पद पिछले पद और उसके अपने अंकों के योग का जोड़ है: 13 + (1 + 3) = 17, 17 + 8 = 25, 25 + 7 = 32, 32 + 5 = 37, 37 + 10 = 47, 47 + 11 = 58, इसलिए अगला 58 + (5 + 8) = 71 है। "
  "69 अंतिम चरण 11 को दोहराता है; 65 और 67 अंतरों में कोई क्रम अनुमानित करने से आते हैं।",
  "qa-ss-a-series-that-adds-its-own-digit-sum", _ss1)

def _ss2():
    sols = [(a, d) for a in range(-20, 21) for d in range(-10, 11) if 5 * (2 * a + 9 * d) == 155 and 10 * (2 * a + 19 * d) == 610]
    assert sols == [(2, 3)]
    return "2"
N(QA, "Sequences & Series", "hard",
  "In an arithmetic progression, the sum of the first 10 terms is 155 and the sum of the first 20 terms is 610. What is the first term?",
  "एक समांतर श्रेणी में पहले 10 पदों का योग 155 और पहले 20 पदों का योग 610 है। पहला पद क्या है?",
  ["2", "3", "4", "5"], 0,
  "The sum of n terms is (n/2)(2a + (n - 1)d). So 5(2a + 9d) = 155, giving 2a + 9d = 31, and 10(2a + 19d) = 610, giving 2a + 19d = 61. Subtracting, 10d = 30 and d = 3; then 2a = 31 - 27 = 4 and a = 2 (the progression is 2, 5, 8, ...). "
  "3 is the common difference, not the first term; 4 is 2a; 5 is the second term.",
  "n पदों का योग (n/2)(2a + (n - 1)d) है। अतः 5(2a + 9d) = 155, जिससे 2a + 9d = 31, और 10(2a + 19d) = 610, जिससे 2a + 19d = 61। घटाने पर 10d = 30 और d = 3; तब 2a = 31 - 27 = 4 और a = 2 (श्रेणी 2, 5, 8, ... है)। "
  "3 सार्व अंतर है, पहला पद नहीं; 4, 2a है; 5 दूसरा पद है।",
  "qa-ss-an-ap-found-from-two-sums", _ss2)

# ---------------------------------------------------------------- Permutation & Combination (2)
def _pc1():
    people = [(cp, s) for cp in range(4) for s in range(2)]
    n = sum(1 for t in combinations(people, 3) if len({p[0] for p in t}) == 3)
    assert n == 32 and math.comb(8, 3) == 56
    return str(n)
N(QA, "Permutation & Combination", "hard",
  "A committee of 3 is to be chosen from 4 married couples. In how many ways can it be chosen if no husband and wife may both be on the committee?",
  "4 विवाहित दंपतियों में से 3 सदस्यों की एक समिति चुननी है। यदि कोई पति और पत्नी दोनों समिति में न हो सकें, तो समिति कितने तरीक़ों से चुनी जा सकती है?",
  ["24", "32", "48", "56"], 1,
  "The three members must come from three different couples. Choose the couples in 4C3 = 4 ways, and then one of the two people from each chosen couple in 2 × 2 × 2 = 8 ways: 4 × 8 = 32 committees. "
  "56 = 8C3 ignores the condition; subtracting the 4 × 6 = 24 committees that contain a couple also gives 32, and 24 is that subtracted count; 48 has no basis.",
  "तीनों सदस्यों को तीन अलग-अलग दंपतियों से आना होगा। दंपती 4C3 = 4 तरीक़ों से चुनिए, और फिर हर चुने दंपती के दो व्यक्तियों में से एक को 2 × 2 × 2 = 8 तरीक़ों से: 4 × 8 = 32 समितियाँ। "
  "56 = 8C3 शर्त को अनदेखा करता है; किसी दंपती वाली 4 × 6 = 24 समितियाँ घटाने पर भी 32 आता है, और 24 वही घटाई गई संख्या है; 48 का कोई आधार नहीं।",
  "qa-pc-a-committee-with-no-couple-in-it", _pc1)

def _pc2():
    n = sum(1 for p in permutations("ABCDE") if {p[0], p[-1]} == {"A", "B"})
    assert n == 12
    return str(n)
N(QA, "Permutation & Combination", "medium",
  "In how many ways can 5 different books be arranged in a row on a shelf if two particular books must be at the two ends?",
  "5 अलग-अलग पुस्तकें एक शेल्फ़ पर एक पंक्ति में कितने तरीक़ों से रखी जा सकती हैं, यदि दो विशेष पुस्तकें दोनों छोरों पर होनी चाहिए?",
  ["12", "24", "48", "120"], 0,
  "The two particular books can take the two ends in 2 ways (either one on the left), and the other 3 books fill the middle in 3! = 6 ways: 2 × 6 = 12. "
  "120 = 5! ignores the condition; 24 = 4! and 48 have no basis in the condition.",
  "दोनों विशेष पुस्तकें दोनों छोरों पर 2 तरीक़ों से आ सकती हैं (दोनों में से कोई भी बाईं ओर), और बाक़ी 3 पुस्तकें बीच में 3! = 6 तरीक़ों से: 2 × 6 = 12। "
  "120 = 5! शर्त को अनदेखा करता है; 24 = 4! और 48 का शर्त में कोई आधार नहीं।",
  "qa-pc-two-books-at-the-ends", _pc2)

# ---------------------------------------------------------------- Geometry & Mensuration (2)
def _gm1():
    angle = F(2, 12)                           # two hours: a sixth of the dial
    assert angle * 36 == 6                     # (1/6) π r² with r = 6
    return "6π cm²"
N(QA, "Geometry & Mensuration", "medium",
  "The hour hand of a clock is 6 cm long. What area does it sweep out in 2 hours?",
  "एक घड़ी की घंटे की सुई 6 सेमी लंबी है। 2 घंटों में वह कितना क्षेत्रफल पार करती है?",
  ["3π cm²", "6π cm²", "12π cm²", "36π cm²"], 1,
  "The hour hand goes once round the dial in 12 hours, so in 2 hours it turns through 2/12 = 1/6 of a full turn and sweeps 1/6 of the circle of radius 6 cm: (1/6) × π × 6² = 6π cm² (about 18.9 cm²). "
  "36π cm² is the whole circle; 12π cm² is the area swept in 4 hours; 3π cm² is the area swept in 1 hour.",
  "घंटे की सुई 12 घंटे में डायल का एक पूरा चक्कर लगाती है, इसलिए 2 घंटे में वह पूरे चक्कर का 2/12 = 1/6 घूमती है और 6 सेमी त्रिज्या वाले वृत्त का 1/6 भाग पार करती है: (1/6) × π × 6² = 6π वर्ग सेमी (लगभग 18.9 वर्ग सेमी)। "
  "36π वर्ग सेमी पूरा वृत्त है; 12π वर्ग सेमी 4 घंटों में पार किया क्षेत्रफल है; 3π वर्ग सेमी 1 घंटे में पार किया क्षेत्रफल है।",
  "qa-gm-the-area-an-hour-hand-sweeps", _gm1,
  opts_hi=["3π वर्ग सेमी", "6π वर्ग सेमी", "12π वर्ग सेमी", "36π वर्ग सेमी"])

def _gm2():
    tri = {tuple(sorted((a, b))) for a in range(1, 25) for b in range(1, 25) if a * a + b * b == 625}
    assert tri == {(7, 24), (15, 20)}
    return str(len(tri))
N(QA, "Geometry & Mensuration", "hard",
  "How many different right-angled triangles have whole-number sides and a hypotenuse of 25 units?",
  "पूर्ण संख्या वाली भुजाओं और 25 इकाई कर्ण वाले कितने अलग-अलग समकोण त्रिभुज हैं?",
  ["0", "1", "2", "3"], 2,
  "We need whole numbers a ≤ b with a² + b² = 625. Testing a from 1 to 17 leaves two pairs: 7² + 24² = 49 + 576 = 625 and 15² + 20² = 225 + 400 = 625. So there are two triangles, with sides 7, 24, 25 and 15, 20, 25. "
  "1 stops at the scaled-up 3-4-5 triangle (15, 20, 25) and misses 7, 24, 25; 3 counts a pair that does not work; 0 overlooks both.",
  "हमें ऐसी पूर्ण संख्याएँ a ≤ b चाहिए जिनमें a² + b² = 625 हो। a को 1 से 17 तक जाँचने पर दो जोड़े बचते हैं: 7² + 24² = 49 + 576 = 625 और 15² + 20² = 225 + 400 = 625। अतः दो त्रिभुज हैं, भुजाओं 7, 24, 25 और 15, 20, 25 वाले। "
  "1, 3-4-5 त्रिभुज के बढ़े रूप (15, 20, 25) पर रुककर 7, 24, 25 को चूक जाता है; 3 एक ऐसा जोड़ा गिनता है जो नहीं बैठता; 0 दोनों को अनदेखा करता है।",
  "qa-gm-right-triangles-on-a-hypotenuse-of-25", _gm2)

# ---------------------------------------------------------------- Time & Work (2)
def _tw1():
    fast = F(100) * F(3, 5)
    assert fast == 60
    return "60"
N(QA, "Time & Work", "medium",
  "Two typists type 2 and 3 pages a minute respectively. A 100-page document is to be divided between them so that they start together and finish together. How many pages should the faster typist be given?",
  "दो टाइपिस्ट क्रमशः 2 और 3 पृष्ठ प्रति मिनट टाइप करते हैं। 100 पृष्ठों के एक दस्तावेज़ को उनमें ऐसे बाँटना है कि वे एक साथ शुरू करें और एक साथ समाप्त करें। तेज़ टाइपिस्ट को कितने पृष्ठ दिए जाने चाहिए?",
  ["40", "50", "60", "75"], 2,
  "To finish together in the same time, each must get pages in proportion to speed, 2 : 3. The faster typist gets 3/5 of 100 = 60 pages and the other 40; both take 20 minutes. "
  "40 is the slower typist's share; 50 splits the pages equally, so the faster one would finish first; 75 has no basis.",
  "समान समय में साथ समाप्त करने के लिए हर एक को चाल के अनुपात 2 : 3 में पृष्ठ मिलने चाहिए। तेज़ टाइपिस्ट को 100 का 3/5 = 60 पृष्ठ मिलते हैं और दूसरे को 40; दोनों को 20 मिनट लगते हैं। "
  "40 धीमे टाइपिस्ट का हिस्सा है; 50 पृष्ठ बराबर बाँटता है, जिससे तेज़ वाला पहले समाप्त कर लेता; 75 का कोई आधार नहीं।",
  "qa-tw-two-typists-who-finish-together", _tw1)

def _tw2():
    sols = [t for t in [F(k, 4) for k in range(1, 200)] if F(1, t + 10) + F(1, t + F(5, 2)) == F(1, t)]
    assert sols == [5]
    return "5 days"
N(QA, "Time & Work", "hard",
  "Working alone, A takes 10 days more to finish a job than A and B take working together, and B alone takes 2.5 days more than they take together. How long do A and B take together?",
  "अकेले काम करते हुए A किसी काम को पूरा करने में A और B के साथ मिलकर लगने वाले समय से 10 दिन अधिक लेता है, और अकेला B, साथ मिलकर लगने वाले समय से 2.5 दिन अधिक लेता है। A और B साथ मिलकर कितना समय लेते हैं?",
  ["5 days", "6.25 days", "7.5 days", "12.5 days"], 0,
  "Let them take t days together, so A alone takes t + 10 and B alone t + 2.5. Then 1/(t + 10) + 1/(t + 2.5) = 1/t, which simplifies to t² = 10 × 2.5 = 25, so t = 5 days (A alone 15 days, B alone 7.5: 1/15 + 1/7.5 = 1/5). "
  "7.5 days is B's time alone; 12.5 days adds the two extra times; 6.25 days averages them.",
  "मान लीजिए वे साथ मिलकर t दिन लेते हैं, इसलिए अकेला A, t + 10 और अकेला B, t + 2.5 दिन लेता है। तब 1/(t + 10) + 1/(t + 2.5) = 1/t, जो सरल होकर t² = 10 × 2.5 = 25 बनता है, अतः t = 5 दिन (अकेला A 15 दिन, अकेला B 7.5: 1/15 + 1/7.5 = 1/5)। "
  "7.5 दिन B का अकेले का समय है; 12.5 दिन दोनों अतिरिक्त समय जोड़ता है; 6.25 दिन उनका औसत लेता है।",
  "qa-tw-a-pair-s-time-from-each-one-s-extra-time", _tw2,
  opts_hi=["5 दिन", "6.25 दिन", "7.5 दिन", "12.5 दिन"])

# ---------------------------------------------------------------- Puzzle Hybrid (4)
def _ph1():
    area = {30: 1.0}
    for d in range(29, 0, -1):
        area[d] = area[d + 1] / 2
    return str(next(d for d in range(1, 31) if area[d] == 0.5))
N(QA, "Puzzle Hybrid", "medium",
  "A weed spreads over a pond, doubling the area it covers every day. It covers the whole pond on the 30th day. On which day did it cover half the pond?",
  "एक खरपतवार तालाब पर फैलती है, जो हर दिन अपना ढका क्षेत्रफल दोगुना कर लेती है। वह 30वें दिन पूरा तालाब ढक लेती है। उसने किस दिन आधा तालाब ढका?",
  ["15th", "20th", "28th", "29th"], 3,
  "Since the covered area doubles each day, the pond was half covered one day before it was fully covered: on the 29th day. "
  "The 15th day halves the number of days instead of the area -- on that day the weed covered only a tiny fraction of the pond; the 28th day is when a quarter was covered.",
  "चूँकि ढका क्षेत्रफल हर दिन दोगुना होता है, तालाब पूरा ढकने से एक दिन पहले आधा ढका था: 29वें दिन। "
  "15वाँ दिन क्षेत्रफल के बजाय दिनों की संख्या को आधा करता है -- उस दिन खरपतवार ने तालाब का केवल एक बहुत छोटा अंश ढका था; 28वाँ दिन तब है जब चौथाई ढका था।",
  "qa-ph-weed-that-doubles-every-day", lambda: _ph1() + "th",
  opts_hi=["15वाँ", "20वाँ", "28वाँ", "29वाँ"])

def _ph2():
    win = {0: False}
    for n in range(1, 22):
        win[n] = any(not win[n - k] for k in (1, 2, 3) if k <= n)
    moves = [k for k in (1, 2, 3) if not win[21 - k]]
    assert moves == [1]
    return "1"
N(QA, "Puzzle Hybrid", "hard",
  "Two players take turns removing 1, 2 or 3 coins from a pile of 21 coins, and the player who takes the last coin wins. How many coins should the first player take on the first turn to be sure of winning?",
  "दो खिलाड़ी बारी-बारी से 21 सिक्कों के ढेर से 1, 2 या 3 सिक्के उठाते हैं, और जो खिलाड़ी अंतिम सिक्का उठाता है वह जीतता है। पहले खिलाड़ी को निश्चित जीत के लिए पहली बारी में कितने सिक्के उठाने चाहिए?",
  ["1", "2", "3", "The first player cannot be sure of winning"], 0,
  "Whoever leaves the other a multiple of 4 can always win: whatever the opponent takes (1, 2 or 3), the reply makes the pair add up to 4, and the pile falls 20, 16, ..., 4, 0. 21 = 4 × 5 + 1, so the first player should take 1 coin, leave 20, and then always make each round add up to 4. "
  "Taking 2 or 3 leaves 19 or 18, from which the opponent can restore a multiple of 4 and win; and since a winning first move exists, the claim that the first player cannot be sure of winning is wrong.",
  "जो दूसरे के लिए 4 का गुणज छोड़ता है वह हमेशा जीत सकता है: प्रतिद्वंद्वी जो भी उठाए (1, 2 या 3), उत्तर में इतना उठाया जाए कि जोड़ा 4 बने, और ढेर 20, 16, ..., 4, 0 होता जाता है। 21 = 4 × 5 + 1, इसलिए पहले खिलाड़ी को 1 सिक्का उठाना चाहिए, 20 छोड़ने चाहिए, और फिर हर दौर का योग 4 बनाना चाहिए। "
  "2 या 3 उठाने से 19 या 18 बचते हैं, जिनसे प्रतिद्वंद्वी फिर 4 का गुणज बनाकर जीत सकता है; और चूँकि जीत वाली पहली चाल है, यह दावा ग़लत है कि पहला खिलाड़ी जीत के प्रति निश्चित नहीं हो सकता।",
  "qa-ph-a-game-of-taking-coins", _ph2,
  opts_hi=["1", "2", "3", "पहला खिलाड़ी जीत के प्रति निश्चित नहीं हो सकता"])

def _ph3():
    best = min(sum(t) for t in product(range(39), range(20), range(8), range(4)) if t[0] + 2 * t[1] + 5 * t[2] + 10 * t[3] == 38)
    assert best == 6
    return str(best)
N(QA, "Puzzle Hybrid", "easy",
  "Using coins of ₹1, ₹2, ₹5 and ₹10, as many of each as needed, what is the fewest number of coins that make exactly ₹38?",
  "₹1, ₹2, ₹5 और ₹10 के सिक्कों से, हर प्रकार के जितने चाहिए, ठीक ₹38 बनाने के लिए कम से कम कितने सिक्के चाहिए?",
  ["3", "4", "5", "6"], 3,
  "Use the largest coins first: three ₹10 coins make ₹30, a ₹5 coin makes ₹35, a ₹2 coin ₹37 and a ₹1 coin ₹38 -- 6 coins. No 5 coins can reach ₹38: four ₹10 coins already exceed it, three ₹10 coins leave ₹8, which needs at least three more coins, and with two or fewer ₹10 coins at least ₹18 is left for coins of ₹5 or less, which needs at least four more. "
  "3, 4 and 5 coins cannot make ₹38 exactly.",
  "पहले सबसे बड़े सिक्के लीजिए: ₹10 के तीन सिक्के ₹30 बनाते हैं, ₹5 का एक सिक्का ₹35, ₹2 का एक ₹37 और ₹1 का एक ₹38 -- 6 सिक्के। 5 सिक्कों से ₹38 नहीं बन सकता: ₹10 के चार सिक्के पहले ही उससे अधिक हैं, ₹10 के तीन सिक्के ₹8 छोड़ते हैं, जिसके लिए कम से कम तीन और सिक्के चाहिए, और ₹10 के दो या कम सिक्कों पर कम से कम ₹18 ₹5 या छोटे सिक्कों के लिए बचते हैं, जिनके लिए कम से कम चार और चाहिए। "
  "3, 4 और 5 सिक्कों से ठीक ₹38 नहीं बन सकता।",
  "qa-ph-the-fewest-coins-for-38", _ph3)

def _ph4():
    pages = 60
    sheet = lambda p: frozenset({p, p + 1 if p % 2 else p - 1, pages + 1 - p, pages + 1 - (p + 1 if p % 2 else p - 1)})
    s = sheet(7)
    assert s == {7, 8, 53, 54}
    return "8, 53 and 54"
N(QA, "Puzzle Hybrid", "hard",
  "A booklet of 60 pages is made by stacking sheets of paper, folding the stack in half and stapling it along the fold, so that each sheet carries four pages. Which other pages are printed on the same sheet as page 7?",
  "60 पृष्ठों की एक पुस्तिका काग़ज़ की शीटों को एक के ऊपर एक रखकर, उन्हें बीच से मोड़कर और मोड़ पर नत्थी करके बनाई जाती है, जिससे हर शीट पर चार पृष्ठ आते हैं। पृष्ठ 7 वाली शीट पर कौन-से अन्य पृष्ठ छपे हैं?",
  ["8, 53 and 54", "6, 54 and 55", "8, 52 and 53", "8, 54 and 55"], 0,
  "Page 7 is on one side of a leaf whose other side is page 8. When a stack is folded in half, each leaf at the front is joined at the fold to a leaf at the back, and the pages on a sheet pair up so that each pair adds up to 60 + 1 = 61. "
  "So page 7 shares its side of the sheet with page 61 - 7 = 54, and page 8 shares the other side with 61 - 8 = 53: the sheet carries 7, 8, 53 and 54. '6, 54 and 55' keeps the sums at 61 but puts page 6 on page 7's leaf, though a leaf carries an odd page and the even page after it (5 with 6, 7 with 8); the other two break the rule that the pairs add up to 61.",
  "पृष्ठ 7 एक पत्ते के एक ओर है, जिसके दूसरी ओर पृष्ठ 8 है। जब शीटों का ढेर बीच से मोड़ा जाता है, तो आगे का हर पत्ता मोड़ पर पीछे के एक पत्ते से जुड़ा होता है, और एक शीट के पृष्ठ ऐसे जोड़ों में आते हैं जिनमें हर जोड़े का योग 60 + 1 = 61 है। "
  "अतः पृष्ठ 7 शीट की अपनी ओर पृष्ठ 61 - 7 = 54 के साथ है, और पृष्ठ 8 दूसरी ओर 61 - 8 = 53 के साथ: शीट पर 7, 8, 53 और 54 हैं। '6, 54 और 55' योग 61 बनाए रखता है पर पृष्ठ 6 को पृष्ठ 7 के पत्ते पर रखता है, जबकि एक पत्ते पर एक विषम पृष्ठ और उसके बाद का सम पृष्ठ होता है (5 के साथ 6, 7 के साथ 8); बाक़ी दो जोड़ों का योग 61 होने का नियम तोड़ते हैं।",
  "qa-ph-the-pages-on-one-sheet-of-a-booklet", _ph4,
  opts_hi=["8, 53 और 54", "6, 54 और 55", "8, 52 और 53", "8, 54 और 55"])

# ---------------------------------------------------------------- the data-sufficiency block's two Quant items
def _ds1():
    pairs = [(a, b) for a in range(-20, 21) for b in range(-20, 21)]
    s1 = {(a * b) % 2 == 0 for a, b in pairs if a % 2 == 0}
    s2 = {(a * b) % 2 == 0 for a, b in pairs if (a + b) % 2 == 1}
    both = s1 & s2
    assert s1 == {True} and s2 == {True}
    return _ds(s1, s2, both)
DS(QA, "hard",
   "Is the product ab of two integers a and b even?",
   "क्या दो पूर्णांकों a और b का गुणनफल ab सम है?",
   "a is even.", "a सम है।",
   "a + b is odd.", "a + b विषम है।",
   1,
   "Statement I: an even number times any integer is even, so ab is even -- sufficient. Statement II: if a + b is odd, one of a and b is even and the other odd, and the even one makes the product even -- also sufficient, although it does not say which of the two is even. "
   "Either statement alone answers the question. The trap is to think that II needs I to say which number is even.",
   "कथन I: सम संख्या को किसी भी पूर्णांक से गुणा करने पर गुणनफल सम होता है, इसलिए ab सम है -- पर्याप्त। कथन II: यदि a + b विषम है, तो a और b में से एक सम और दूसरा विषम है, और सम वाला गुणनफल को सम बना देता है -- यह भी पर्याप्त, यद्यपि यह नहीं बताता कि दोनों में से कौन सम है। "
   "कोई भी एक कथन अकेले प्रश्न का उत्तर देता है। जाल यह सोचना है कि II को यह जानने के लिए I चाहिए कि कौन-सी संख्या सम है।",
   "qa-ds-is-a-product-even", _ds1)

def _ds2():
    a_days = [F(k) for k in range(2, 60)]
    s1 = {F(1) / (F(1, 12) + F(1, b)) for b in a_days}                              # I: A takes 12 days; B unknown
    s2 = {F(1) / (F(1, a) + F(1, 2 * a)) for a in a_days}                          # II: A twice as efficient as B
    both = {F(1) / (F(1, 12) + F(1, 24))}
    assert both == {8}
    return _ds(s1, s2, both)
DS(QA, "medium",
   "How many days do A and B take to finish a job working together?",
   "A और B साथ मिलकर किसी काम को पूरा करने में कितने दिन लेते हैं?",
   "A alone can finish the job in 12 days.", "अकेला A काम को 12 दिनों में पूरा कर सकता है।",
   "A is twice as efficient as B.", "A, B से दोगुना कुशल है।",
   2,
   "Statement I gives A's rate but nothing about B, and Statement II gives only the ratio of their rates. Together, B takes twice as long as A, 24 days, and the two finish 1/12 + 1/24 = 1/8 of the job a day: 8 days. Both statements are needed.",
   "कथन I, A की दर देता है पर B के बारे में कुछ नहीं, और कथन II केवल उनकी दरों का अनुपात देता है। दोनों साथ: B को A से दोगुना, यानी 24 दिन लगते हैं, और दोनों मिलकर प्रतिदिन काम का 1/12 + 1/24 = 1/8 भाग करते हैं: 8 दिन। दोनों कथन ज़रूरी हैं।",
   "qa-ds-a-pair-s-time-from-a-time-and-a-ratio", _ds2)
