# -*- coding: utf-8 -*-
"""CSAT Level 4 · Simulator 9 -- Quantitative Aptitude (37 items: 35 in the Quant slots, 2 in the data-sufficiency block).

Layout C, the 2026 shape of the paper. Exam-level mix (8 easy / 17 medium / 12 hard), with none of the shapes of
Levels 1-3 or Simulators 1-8: a fraction between 3/7 and 4/9, a product reduced before dividing, the largest product
for a fixed sum, five odd numbers added, a cube sum whose bases add to zero, a gap between two roots, the even numbers
less the odd, twice a square and thrice a cube, fractional and negative indices, two odd powers divided by 5; the
distance to the Sun from light's travel time, the tips of two clock hands, two walkers who meet one cyclist; a will
that did not foresee twins, shares that do not measure power, a photograph enlarged, a share given up and passed on; a profit that triples, prices that double, people below a line in a growing town; a wrong
term among n² + 1, n²(n + 1); houses painted with no two neighbours alike, side dishes on a thali, 12 as three different
parts; cubes melted into one, a plot with a corner cut away, triangles of perimeter 12, an open box folded from a sheet; two filling machines started
apart, two taps 10 hours apart; samples tested in pools, two ropes that burn unevenly, a chessboard short of two
corners, 1 to 100 by doubling or adding one; and two data-sufficiency items. Every key is worked out in code by
check()."""
from fractions import Fraction as F
from itertools import combinations, permutations, product
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
    lo, hi = F(3, 7), F(4, 9)
    opts = {"5/12": F(5, 12), "8/19": F(8, 19), "7/16": F(7, 16), "5/11": F(5, 11)}
    inside = [k for k, v in opts.items() if lo < v < hi]
    assert inside == ["7/16"] and F(3 + 4, 7 + 9) == F(7, 16)
    return inside[0]
N(QA, "Number Theory", "medium",
  "Which one of the following fractions lies between 3/7 and 4/9?",
  "निम्नलिखित में से कौन-सी भिन्न 3/7 और 4/9 के बीच स्थित है?",
  ["5/12", "8/19", "7/16", "5/11"], 2,
  "Adding the numerators and the denominators of two fractions always gives a fraction between them: (3 + 4)/(7 + 9) = 7/16. Check: 3/7 ≈ 0.4286, 7/16 = 0.4375 and 4/9 ≈ 0.4444. "
  "5/12 ≈ 0.4167 and 8/19 ≈ 0.4211 are both below 3/7, and 5/11 ≈ 0.4545 is above 4/9.",
  "दो भिन्नों के अंशों और हरों को अलग-अलग जोड़ने से सदा उनके बीच की भिन्न मिलती है: (3 + 4)/(7 + 9) = 7/16। जाँच: 3/7 ≈ 0.4286, 7/16 = 0.4375 और 4/9 ≈ 0.4444। "
  "5/12 ≈ 0.4167 और 8/19 ≈ 0.4211 दोनों 3/7 से कम हैं, और 5/11 ≈ 0.4545, 4/9 से अधिक है।",
  "qa-nt-a-fraction-between-3-over-7-and-4-over-9", _nt1)

def _nt2():
    r = (7001 * 7002 * 7003) % 7000
    assert r == (1 * 2 * 3) % 7000
    return str(r)
N(QA, "Number Theory", "medium",
  "What is the remainder when 7001 × 7002 × 7003 is divided by 7000?",
  "7001 × 7002 × 7003 को 7000 से भाग देने पर शेषफल क्या है?",
  ["1", "3", "6", "24"], 2,
  "Each factor can be replaced by its own remainder on division by 7000: 7001 leaves 1, 7002 leaves 2 and 7003 leaves 3. So the product leaves the same remainder as 1 × 2 × 3 = 6, with no need to multiply the large numbers. "
  "(Adding the remainders, 1 + 2 + 3, also gives 6 here, but only by coincidence: the rule is to multiply them.) 3 is the last remainder alone; 24 = 2 × 3 × 4 takes each remainder one too high; 1 is the first remainder alone.",
  "हर गुणनखंड को 7000 से भाग देने पर बचे उसके अपने शेषफल से बदला जा सकता है: 7001 से 1, 7002 से 2 और 7003 से 3 बचता है। इसलिए गुणनफल का शेषफल वही है जो 1 × 2 × 3 = 6 का, बड़ी संख्याओं का गुणा किए बिना। "
  "(शेषफलों को जोड़ने, 1 + 2 + 3, से भी यहाँ 6 मिलता है, पर केवल संयोग से: नियम उन्हें गुणा करने का है।) 3 केवल अंतिम शेषफल है; 24 = 2 × 3 × 4 हर शेषफल को एक अधिक ले लेता है; 1 केवल पहला शेषफल है।",
  "qa-nt-a-product-reduced-before-dividing", _nt2)

def _nt3():
    best = max(F(k, 10) * (50 - F(k, 10)) for k in range(0, 501))
    assert best == 625 and 24 * 26 == 624
    return str(best)
N(QA, "Number Theory", "easy",
  "Two numbers add up to 50. What is the largest value their product can take?",
  "दो संख्याओं का योग 50 है। उनका गुणनफल अधिक से अधिक कितना हो सकता है?",
  ["576", "600", "624", "625"], 3,
  "For a fixed sum the product is largest when the two numbers are equal: 25 × 25 = 625. Moving them apart by any amount d gives (25 - d)(25 + d) = 625 - d², which is smaller. "
  "624 = 24 × 26 assumes the numbers must be different; 600 = 20 × 30 is just one pair; 576 = 24² has no basis.",
  "स्थिर योग के लिए गुणनफल तब सबसे बड़ा होता है जब दोनों संख्याएँ बराबर हों: 25 × 25 = 625। उन्हें किसी भी मात्रा d से अलग करने पर (25 - d)(25 + d) = 625 - d² मिलता है, जो छोटा है। "
  "624 = 24 × 26 मान लेता है कि संख्याएँ अलग होनी चाहिए; 600 = 20 × 30 केवल एक जोड़ी है; 576 = 24² का कोई आधार नहीं।",
  "qa-nt-the-largest-product-for-a-fixed-sum", _nt3)

def _nt4():
    from itertools import combinations_with_replacement
    totals = {sum(t) for t in combinations_with_replacement(range(1, 52, 2), 5)}
    can = [x for x in (35, 40, 50, 60) if x in totals]
    assert can == [35]
    return "35"
N(QA, "Number Theory", "easy",
  "Five odd numbers, not necessarily different, are added together. Which one of the following could be their total?",
  "पाँच विषम संख्याएँ, आवश्यक नहीं कि अलग-अलग हों, जोड़ी जाती हैं। निम्नलिखित में से कौन-सा उनका योग हो सकता है?",
  ["35", "40", "50", "60"], 0,
  "Two odd numbers make an even number, so four of them make an even total, and the fifth makes it odd again. A sum of five odd numbers is always odd, and of the options only 35 is odd (for example 7 + 7 + 7 + 7 + 7). "
  "40, 50 and 60 are even, so no five odd numbers can add up to any of them.",
  "दो विषम संख्याएँ मिलकर सम बनती हैं, इसलिए चार का योग सम होता है, और पाँचवीं उसे फिर विषम बना देती है। पाँच विषम संख्याओं का योग सदा विषम होता है, और विकल्पों में केवल 35 विषम है (उदाहरण के लिए 7 + 7 + 7 + 7 + 7)। "
  "40, 50 और 60 सम हैं, इसलिए कोई पाँच विषम संख्याएँ जुड़कर इनमें से कोई नहीं बना सकतीं।",
  "qa-nt-five-odd-numbers-added", _nt4)

def _nt5():
    v = 23 ** 3 - 15 ** 3 - 8 ** 3
    assert v == 3 * 23 * 15 * 8 == 8280
    return f"{v:,}"
N(QA, "Number Theory", "hard",
  "What is the value of 23³ - 15³ - 8³?",
  "23³ - 15³ - 8³ का मान क्या है?",
  ["7,920", "8,280", "8,640", "9,000"], 1,
  "Write it as a³ + b³ + c³ with a = 23, b = -15 and c = -8. These add up to 0, and whenever a + b + c = 0, a³ + b³ + c³ = 3abc. So the value is 3 × 23 × (-15) × (-8) = 3 × 23 × 120 = 8,280. (Directly: 12,167 - 3,375 - 512 = 8,280.) "
  "7,920 and 8,640 take 3 × 22 × 120 and 3 × 24 × 120, a base off by one; 9,000 has no basis.",
  "इसे a³ + b³ + c³ के रूप में लिखें, जहाँ a = 23, b = -15 और c = -8। इनका योग 0 है, और जब भी a + b + c = 0 हो, a³ + b³ + c³ = 3abc होता है। अतः मान 3 × 23 × (-15) × (-8) = 3 × 23 × 120 = 8,280 है। (सीधे: 12,167 - 3,375 - 512 = 8,280।) "
  "7,920 और 8,640, 3 × 22 × 120 और 3 × 24 × 120 लेते हैं, एक आधार एक से खिसका हुआ; 9,000 का कोई आधार नहीं।",
  "qa-nt-a-cube-sum-whose-bases-add-to-zero", _nt5)

def _nt6():
    n = sum(1 for k in range(-100, 101) if k * k - 5 * k + 6 < 0)
    assert n == 0
    return str(n)
N(QA, "Number Theory", "medium",
  "How many integers n satisfy n² - 5n + 6 < 0?",
  "कितने पूर्णांक n, n² - 5n + 6 < 0 को संतुष्ट करते हैं?",
  ["0", "1", "2", "4"], 0,
  "n² - 5n + 6 = (n - 2)(n - 3), which is negative only when n lies strictly between 2 and 3. No integer does: at n = 2 and n = 3 the expression is 0, not less than 0, and everywhere else it is positive. So there are none. "
  "2 counts the two roots, where the expression equals 0; 1 and 4 have no basis.",
  "n² - 5n + 6 = (n - 2)(n - 3), जो तभी ऋणात्मक होता है जब n ठीक 2 और 3 के बीच हो। कोई पूर्णांक ऐसा नहीं: n = 2 और n = 3 पर व्यंजक 0 है, 0 से कम नहीं, और बाक़ी हर जगह धनात्मक। अतः कोई नहीं। "
  "2 दोनों मूलों को गिनता है, जहाँ व्यंजक 0 के बराबर है; 1 और 4 का कोई आधार नहीं।",
  "qa-nt-no-integer-in-the-gap-between-two-roots", _nt6)

def _nt7():
    d = sum(range(2, 101, 2)) - sum(range(1, 100, 2))
    assert d == 50
    return str(d)
N(QA, "Number Theory", "easy",
  "What is (2 + 4 + 6 + ... + 100) - (1 + 3 + 5 + ... + 99)?",
  "(2 + 4 + 6 + ... + 100) - (1 + 3 + 5 + ... + 99) का मान क्या है?",
  ["0", "1", "50", "100"], 2,
  "Pair the terms: 2 - 1, 4 - 3, ..., 100 - 99. There are 50 pairs and each is 1, so the difference is 50 -- no need to add up either series. "
  "1 sees only one pair; 100 confuses the number of pairs with the last term; 0 assumes the two sums are equal.",
  "पदों की जोड़ियाँ बनाएँ: 2 - 1, 4 - 3, ..., 100 - 99। 50 जोड़ियाँ हैं और हर एक 1 है, इसलिए अंतर 50 है -- किसी भी श्रेणी को जोड़ने की आवश्यकता नहीं। "
  "1 केवल एक जोड़ी देखता है; 100 जोड़ियों की संख्या को अंतिम पद से भ्रमित करता है; 0 मान लेता है कि दोनों योग बराबर हैं।",
  "qa-nt-the-even-numbers-less-the-odd", _nt7)

def _nt8():
    sq = lambda m: math.isqrt(m) ** 2 == m
    cu = lambda m: round(m ** (1 / 3)) ** 3 == m
    n = next(k for k in range(1, 10000) if sq(2 * k) and cu(3 * k))
    assert n == 72 and 2 * n == 12 ** 2 and 3 * n == 6 ** 3
    return str(n)
N(QA, "Number Theory", "hard",
  "What is the smallest positive integer n such that 2n is a perfect square and 3n is a perfect cube?",
  "वह सबसे छोटा धनात्मक पूर्णांक n कौन-सा है जिसके लिए 2n पूर्ण वर्ग और 3n पूर्ण घन हो?",
  ["72", "108", "144", "216"], 0,
  "n can use only the primes 2 and 3: n = 2ᵃ × 3ᵇ. For 2n to be a square, a + 1 and b must be even; for 3n to be a cube, a and b + 1 must be multiples of 3. The smallest a that is odd and a multiple of 3 is 3; the smallest b that is even and one less than a multiple of 3 is 2. So n = 2³ × 3² = 72: 2n = 144 = 12² and 3n = 216 = 6³. "
  "144 is 2n, not n; 108 gives 2n = 216, not a square; 216 gives 2n = 432, not a square either.",
  "n में केवल अभाज्य 2 और 3 हो सकते हैं: n = 2ᵃ × 3ᵇ। 2n के वर्ग होने के लिए a + 1 और b सम होने चाहिए; 3n के घन होने के लिए a और b + 1, 3 के गुणज होने चाहिए। सबसे छोटा a जो विषम और 3 का गुणज हो, 3 है; सबसे छोटा b जो सम हो और 3 के गुणज से एक कम, 2 है। अतः n = 2³ × 3² = 72: 2n = 144 = 12² और 3n = 216 = 6³। "
  "144, n नहीं बल्कि 2n है; 108 से 2n = 216 मिलता है, जो वर्ग नहीं; 216 से 2n = 432, वह भी वर्ग नहीं।",
  "qa-nt-twice-a-square-and-thrice-a-cube", _nt8)

def _nt9():
    v = F(4) + F(1, 2) * 4                            # 8^(2/3) = 4, 16^(-1/4) = 1/2, 32^(2/5) = 4
    assert round(8 ** (2 / 3), 9) == 4 and round(16 ** (-1 / 4), 9) == 0.5 and round(32 ** (2 / 5), 9) == 4
    assert v == 6 and 4 + F(1, 2) * 2 == 5 and 4 + F(1, 2) == F(9, 2) and F(1, 2) * 4 == 2
    return str(v)
N(QA, "Number Theory", "medium",
  "What is the value of 8^(2/3) + 16^(-1/4) × 32^(2/5)?",
  "8^(2/3) + 16^(-1/4) × 32^(2/5) का मान क्या है?",
  ["2", "4.5", "5", "6"], 3,
  "8^(2/3) = (the cube root of 8)² = 2² = 4. 16^(-1/4) = 1 ÷ (the fourth root of 16) = 1/2. 32^(2/5) = (the fifth root of 32)² = 2² = 4. So the value is 4 + (1/2) × 4 = 6, the multiplication being done before the addition. "
  "5 forgets to square the fifth root of 32 (4 + 1/2 × 2); 4.5 forgets the last factor (4 + 1/2); 2 keeps only the product and drops 8^(2/3).",
  "8^(2/3) = (8 का घनमूल)² = 2² = 4। 16^(-1/4) = 1 ÷ (16 का चौथा मूल) = 1/2। 32^(2/5) = (32 का पाँचवाँ मूल)² = 2² = 4। अतः मान 4 + (1/2) × 4 = 6 है, जोड़ से पहले गुणा करके। "
  "5, 32 के पाँचवें मूल का वर्ग करना भूल जाता है (4 + 1/2 × 2); 4.5 अंतिम गुणनखंड भूल जाता है (4 + 1/2); 2 केवल गुणनफल रखता है और 8^(2/3) छोड़ देता है।",
  "qa-nt-fractional-and-negative-indices", _nt9)

def _nt10():
    r = (pow(2, 2027, 5) + pow(3, 2027, 5)) % 5
    assert r == 0 and all((pow(2, k, 5) + pow(3, k, 5)) % 5 == 0 for k in range(1, 60, 2))
    return str(r)
N(QA, "Number Theory", "hard",
  "What is the remainder when 2²⁰²⁷ + 3²⁰²⁷ is divided by 5?",
  "2²⁰²⁷ + 3²⁰²⁷ को 5 से भाग देने पर शेषफल क्या है?",
  ["0", "1", "2", "3"], 0,
  "For an odd power n, aⁿ + bⁿ is always divisible by a + b (for example a³ + b³ = (a + b)(a² - ab + b²)). Here a + b = 2 + 3 = 5 and 2027 is odd, so 2²⁰²⁷ + 3²⁰²⁷ is a multiple of 5: remainder 0. (Check with a small odd power: 2³ + 3³ = 35.) "
  "The other remainders come from working out only one of the two powers, or from treating the power as even, as in 2² + 3² = 13, which leaves 3.",
  "विषम घात n के लिए aⁿ + bⁿ सदा a + b से विभाज्य होता है (उदाहरण के लिए a³ + b³ = (a + b)(a² - ab + b²))। यहाँ a + b = 2 + 3 = 5 और 2027 विषम है, इसलिए 2²⁰²⁷ + 3²⁰²⁷, 5 का गुणज है: शेषफल 0। (छोटी विषम घात से जाँचें: 2³ + 3³ = 35।) "
  "बाक़ी शेषफल दोनों में से केवल एक घात निकालने से, या घात को सम मानने से आते हैं, जैसे 2² + 3² = 13, जिससे 3 बचता है।",
  "qa-nt-two-odd-powers-divided-by-5", _nt10)

# ---------------------------------------------------------------- Speed-Distance-Time (3)
def _sdt1():
    d = (8 * 60 + 20) * 300000
    assert d == 15 * 10 ** 7 and 820 * 300000 == 246 * 10 ** 6
    return "15 crore km"
N(QA, "Speed-Distance-Time", "easy",
  "Light from the Sun takes about 8 minutes 20 seconds to reach the Earth. If light travels at 3,00,000 km a second, about how far is the Sun from the Earth?",
  "सूर्य से प्रकाश को पृथ्वी तक पहुँचने में लगभग 8 मिनट 20 सेकंड लगते हैं। यदि प्रकाश 3,00,000 किमी प्रति सेकंड चलता है, तो सूर्य पृथ्वी से लगभग कितनी दूर है?",
  ["1.5 crore km", "15 crore km", "24.6 crore km", "150 crore km"], 1,
  "8 minutes 20 seconds is 8 × 60 + 20 = 500 seconds. In 500 seconds light covers 500 × 3,00,000 = 15,00,00,000 km, that is 15 crore km (150 million km). "
  "24.6 crore km reads 8 minutes 20 seconds as 820 seconds; 1.5 crore and 150 crore km each slip a zero.",
  "8 मिनट 20 सेकंड = 8 × 60 + 20 = 500 सेकंड। 500 सेकंड में प्रकाश 500 × 3,00,000 = 15,00,00,000 किमी, यानी 15 करोड़ किमी (15 करोड़ = 150 मिलियन) चलता है। "
  "24.6 करोड़ किमी, 8 मिनट 20 सेकंड को 820 सेकंड पढ़ता है; 1.5 करोड़ और 150 करोड़ किमी में एक-एक शून्य खिसक जाता है।",
  "qa-sdt-the-sun-s-distance-from-light-s-travel-time", _sdt1,
  opts_hi=["1.5 करोड़ किमी", "15 करोड़ किमी", "24.6 करोड़ किमी", "150 करोड़ किमी"])

def _sdt2():
    minute = 24 * 2 * 7                 # turns in a day x 2 x radius (the common factor pi cancels)
    hour = 2 * 2 * 5
    r = F(minute, hour)
    assert r == F(84, 5) and F(7, 5) != r and F(24 * 7, 1 * 5) == F(168, 5)
    return f"{r.numerator} : {r.denominator}"
N(QA, "Speed-Distance-Time", "medium",
  "The minute hand of a clock is 7 cm long and its hour hand 5 cm long. In a full day, what is the ratio of the distance travelled by the tip of the minute hand to the distance travelled by the tip of the hour hand?",
  "एक घड़ी की मिनट की सुई 7 सेमी लंबी और घंटे की सुई 5 सेमी लंबी है। पूरे दिन में मिनट की सुई की नोक द्वारा तय दूरी और घंटे की सुई की नोक द्वारा तय दूरी का अनुपात क्या है?",
  ["7 : 5", "12 : 1", "84 : 5", "168 : 5"], 2,
  "In a day the minute hand goes round 24 times and the hour hand twice. The tips travel 24 × 2π × 7 and 2 × 2π × 5, so the ratio is (24 × 7) : (2 × 5) = 168 : 10 = 84 : 5. "
  "7 : 5 compares only the lengths, as if both hands turned equally often; 12 : 1 compares only the turns, as if the hands were equally long; 168 : 5 has the hour hand going round only once a day.",
  "एक दिन में मिनट की सुई 24 बार घूमती है और घंटे की सुई दो बार। नोकें 24 × 2π × 7 और 2 × 2π × 5 चलती हैं, इसलिए अनुपात (24 × 7) : (2 × 5) = 168 : 10 = 84 : 5 है। "
  "7 : 5 केवल लंबाइयों की तुलना करता है, मानो दोनों सुइयाँ बराबर बार घूमती हों; 12 : 1 केवल चक्करों की, मानो सुइयाँ बराबर लंबी हों; 168 : 5 में घंटे की सुई दिन में केवल एक बार घूमती है।",
  "qa-sdt-the-tips-of-two-clock-hands", _sdt2)

def _sdt4():
    tb = F(84, 7 + 9)
    ta = F(84, 5 + 9)
    gap = (ta - tb) * 60
    assert tb == F(21, 4) and gap == 45
    assert (7 - 5) * tb == F(21, 2) and F(21, 2) / 9 * 60 == 70 and F(21, 2) / 5 * 60 == 126
    return f"{gap} min"
N(QA, "Speed-Distance-Time", "hard",
  "Two towns, P and Q, are 84 km apart. At 6 am Asha and Bina set out on foot from P towards Q, at 5 km/h and 7 km/h, and at the same moment Chetan sets out on a bicycle from Q towards P at 9 km/h. How long after meeting Bina does Chetan meet Asha?",
  "दो कस्बे, P और Q, 84 किमी दूर हैं। सुबह 6 बजे आशा और बीना P से Q की ओर पैदल 5 किमी/घंटा और 7 किमी/घंटा की चाल से निकलती हैं, और उसी क्षण चेतन Q से P की ओर साइकिल पर 9 किमी/घंटा की चाल से निकलता है। बीना से मिलने के कितनी देर बाद चेतन आशा से मिलता है?",
  ["30 min", "45 min", "1 h 10 min", "2 h 6 min"], 1,
  "Chetan and Bina close the 84 km at 7 + 9 = 16 km/h, so they meet after 5 h 15 min; Chetan and Asha close it at 5 + 9 = 14 km/h, meeting after 6 hours. The gap is 45 minutes. (Or: when Chetan meets Bina, Asha is (7 - 5) × 5.25 = 10.5 km behind, and that gap closes at 5 + 9 = 14 km/h, in 45 minutes.) "
  "1 h 10 min closes the 10.5 km at Chetan's speed alone; 2 h 6 min at Asha's alone; 30 min has no basis.",
  "चेतन और बीना 84 किमी 7 + 9 = 16 किमी/घंटा से घटाते हैं, इसलिए 5 घंटे 15 मिनट बाद मिलते हैं; चेतन और आशा इसे 5 + 9 = 14 किमी/घंटा से घटाते हैं, 6 घंटे बाद मिलते हैं। अंतर 45 मिनट है। (या: जब चेतन बीना से मिलता है, आशा (7 - 5) × 5.25 = 10.5 किमी पीछे है, और यह दूरी 5 + 9 = 14 किमी/घंटा से 45 मिनट में घटती है।) "
  "1 घंटा 10 मिनट 10.5 किमी को केवल चेतन की चाल से घटाता है; 2 घंटे 6 मिनट केवल आशा की चाल से; 30 मिनट का कोई आधार नहीं।",
  "qa-sdt-two-walkers-who-meet-one-cyclist", _sdt4,
  opts_hi=["30 मिनट", "45 मिनट", "1 घंटा 10 मिनट", "2 घंटे 6 मिनट"])

# ---------------------------------------------------------------- Ratio, Mixtures & Alligation (4)
def _rm1():
    son, mother, daughter = 4, 2, 1                     # son = 2 x mother, mother = 2 x daughter
    assert son == 2 * mother and mother == 2 * daughter
    share = F(14, son + mother + daughter) * daughter
    assert share == 2 and F(14, 7) * mother == 4 and F(14, 7) * son == 8
    return f"₹{share} lakh"
N(QA, "Ratio, Mixtures & Alligation", "hard",
  "A man's will said that if his wife gave birth to a son, the son should get twice as much as the mother, and if she gave birth to a daughter, the mother should get twice as much as the daughter. She gave birth to twins, a son and a daughter. If both conditions of the will are kept, how much does the daughter get from an estate of ₹14 lakh?",
  "एक व्यक्ति की वसीयत में लिखा था कि यदि उसकी पत्नी पुत्र को जन्म दे, तो पुत्र को माँ से दोगुना मिले, और यदि पुत्री को जन्म दे, तो माँ को पुत्री से दोगुना मिले। उसने जुड़वाँ, एक पुत्र और एक पुत्री, को जन्म दिया। यदि वसीयत की दोनों शर्तें मानी जाएँ, तो ₹14 लाख की संपत्ति में से पुत्री को कितना मिलेगा?",
  ["₹2 lakh", "₹4 lakh", "about ₹4.7 lakh", "₹8 lakh"], 0,
  "Son : mother = 2 : 1 and mother : daughter = 2 : 1. Joining them through the mother gives son : mother : daughter = 4 : 2 : 1, seven parts in all. ₹14 lakh ÷ 7 = ₹2 lakh a part, so the daughter gets ₹2 lakh, the mother ₹4 lakh and the son ₹8 lakh. "
  "₹4 lakh and ₹8 lakh are the mother's and the son's shares; about ₹4.7 lakh splits the estate equally three ways, ignoring the will.",
  "पुत्र : माँ = 2 : 1 और माँ : पुत्री = 2 : 1। माँ के माध्यम से जोड़ने पर पुत्र : माँ : पुत्री = 4 : 2 : 1, कुल सात भाग। ₹14 लाख ÷ 7 = ₹2 लाख प्रति भाग, इसलिए पुत्री को ₹2 लाख, माँ को ₹4 लाख और पुत्र को ₹8 लाख मिलते हैं। "
  "₹4 लाख और ₹8 लाख माँ और पुत्र के हिस्से हैं; लगभग ₹4.7 लाख वसीयत की अनदेखी कर संपत्ति को तीन बराबर भागों में बाँटता है।",
  "qa-rm-a-will-that-did-not-foresee-twins", _rm1,
  opts_hi=["₹2 लाख", "₹4 लाख", "लगभग ₹4.7 लाख", "₹8 लाख"])

def _rm2():
    hold = {"P": 45, "Q": 35, "R": 20}
    wins = lambda team: sum(hold[x] for x in team) > 50
    from itertools import combinations as comb
    winning = [set(t) for k in (1, 2, 3) for t in comb(hold, k) if wins(t)]
    alone = any(len(w) == 1 for w in winning)
    one = (all(wins(("P", x)) for x in ("Q", "R")) and not any(wins(("R", x)) for x in ("P", "Q")))
    pivotal = {x: sum(1 for w in winning if not wins(tuple(w - {x}))) for x in hold}
    two = pivotal["P"] > 2 * pivotal["R"]
    assert not alone and pivotal["P"] == pivotal["Q"] == pivotal["R"] and not one and not two
    return c.T2[{(True, False): 0, (False, True): 1, (True, True): 2, (False, False): 3}[(one, two)]]
S2(QA, "Ratio, Mixtures & Alligation", "medium",
   "The shares of a company are held by three people: P holds 45%, Q holds 35% and R holds 20%. Every decision needs the support of holders of more than half of the shares. Which of the following statements is/are correct?",
   "एक कंपनी के शेयर तीन लोगों के पास हैं: P के पास 45%, Q के पास 35% और R के पास 20%। हर निर्णय के लिए आधे से अधिक शेयरों के धारकों का समर्थन चाहिए। निम्नलिखित में से कौन-सा/से कथन सही है/हैं?",
   ["P can pass a decision with the support of either of the others, but R cannot pass one with either.",
    "Since P holds more than twice as many shares as R, P has more than twice R's power over decisions."],
   ["P दोनों में से किसी के भी समर्थन से निर्णय पारित कर सकता है, पर R किसी के साथ भी नहीं कर सकता।",
    "चूँकि P के पास R से दोगुने से अधिक शेयर हैं, निर्णयों पर P की शक्ति R से दोगुनी से अधिक है।"],
   3,
   "Neither is correct. No one holds more than half alone, but any two together do: P and Q have 80%, P and R 65%, Q and R 55%. "
   "1 fails because R can pass a decision with either P or Q. 2 fails because every holder is equally placed: each can form a majority with either of the other two and none can act alone, so R's 20% carries as much power over decisions as P's 45%.",
   "कोई भी सही नहीं। अकेले किसी के पास आधे से अधिक नहीं, पर कोई भी दो मिलकर अधिक रखते हैं: P और Q के 80%, P और R के 65%, Q और R के 55%। "
   "1 विफल है क्योंकि R, P या Q में से किसी के भी साथ निर्णय पारित कर सकता है। 2 विफल है क्योंकि हर धारक की स्थिति बराबर है: हर एक बाक़ी दोनों में से किसी के साथ बहुमत बना सकता है और कोई अकेले कुछ नहीं कर सकता, इसलिए निर्णयों पर R के 20% की शक्ति उतनी ही है जितनी P के 45% की।",
   "qa-rm-shares-that-do-not-measure-power", check=_rm2)

def _rm3():
    h = F(15) * F(24, 10)
    assert h == 36
    return f"{h} cm"
N(QA, "Ratio, Mixtures & Alligation", "easy",
  "A photograph 10 cm wide and 15 cm high is enlarged without changing its shape until it is 24 cm wide. How high is it now?",
  "10 सेमी चौड़ी और 15 सेमी ऊँची एक तस्वीर को उसका आकार-अनुपात बदले बिना 24 सेमी चौड़ा होने तक बड़ा किया जाता है। अब वह कितनी ऊँची है?",
  ["29 cm", "30 cm", "36 cm", "40 cm"], 2,
  "Enlarging without changing the shape multiplies every length by the same factor. The width goes from 10 to 24 cm, a factor of 2.4, so the height becomes 15 × 2.4 = 36 cm (height : width stays 3 : 2). "
  "29 cm adds the 14 cm the width grew by, which would distort the picture; 30 cm doubles the height; 40 cm has no basis.",
  "आकार बदले बिना बड़ा करने से हर लंबाई एक ही गुणक से गुणा होती है। चौड़ाई 10 से 24 सेमी होती है, 2.4 गुना, इसलिए ऊँचाई 15 × 2.4 = 36 सेमी हो जाती है (ऊँचाई : चौड़ाई 3 : 2 ही रहता है)। "
  "29 सेमी उतने ही 14 सेमी जोड़ता है जितनी चौड़ाई बढ़ी, जिससे चित्र विकृत हो जाता; 30 सेमी ऊँचाई दोगुनी करता है; 40 सेमी का कोई आधार नहीं।",
  "qa-rm-a-photograph-enlarged", _rm3,
  opts_hi=["29 सेमी", "30 सेमी", "36 सेमी", "40 सेमी"])

def _rm4():
    a, b, c_ = 2, 3, 4
    new_a = F(a, a + b + c_) + F(c_, a + b + c_) * F(a, a + b)
    assert new_a == F(2, 5) == F(a, a + b) and F(a, 9) + F(c_, 9) / 2 == F(4, 9)
    return f"{new_a.numerator}/{new_a.denominator}"
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "A, B and C were to share a prize in the ratio 2 : 3 : 4. C drops out, and C's share is divided between A and B in the ratio of their own shares. What fraction of the prize does A now get?",
  "A, B और C को एक पुरस्कार 2 : 3 : 4 के अनुपात में बाँटना था। C हट जाता है, और C का हिस्सा A और B में उनके अपने हिस्सों के अनुपात में बाँटा जाता है। अब A को पुरस्कार का कितना भाग मिलता है?",
  ["1/3", "2/5", "4/9", "1/2"], 1,
  "Passing C's share on in the ratio 2 : 3 leaves A and B sharing the whole prize in the ratio 2 : 3, so A gets 2/5. (Step by step: A had 2/9 and gets 2/5 of C's 4/9, which is 8/45; 2/9 + 8/45 = 18/45 = 2/5.) "
  "4/9 splits C's share equally between A and B; 1/2 splits the whole prize equally; 1/3 keeps three equal shares.",
  "C का हिस्सा 2 : 3 में आगे बाँटने से A और B पूरा पुरस्कार 2 : 3 में बाँटते हैं, इसलिए A को 2/5 मिलता है। (क़दम-दर-क़दम: A के पास 2/9 था और उसे C के 4/9 का 2/5, यानी 8/45, मिलता है; 2/9 + 8/45 = 18/45 = 2/5।) "
  "4/9, C का हिस्सा A और B में बराबर बाँटता है; 1/2 पूरा पुरस्कार बराबर बाँटता है; 1/3 तीन बराबर हिस्से रखता है।",
  "qa-rm-a-share-given-up-and-passed-on", _rm4)

# ---------------------------------------------------------------- Percentage & Profit-Loss (3)
def _pp1():
    for cp in (40, 100, 250):
        sp = next(s for s in range(cp, 10 * cp) if 2 * s - cp == 3 * (s - cp))
        assert F(sp - cp, cp) == 1
    return "100%"
N(QA, "Percentage & Profit-Loss", "medium",
  "If the selling price of an article were doubled, the profit on it would become three times as large. What is the profit percentage at the present selling price?",
  "यदि किसी वस्तु का विक्रय मूल्य दोगुना कर दिया जाए, तो उस पर लाभ तीन गुना हो जाएगा। वर्तमान विक्रय मूल्य पर लाभ प्रतिशत क्या है?",
  ["50%", "100%", "150%", "200%"], 1,
  "Let the cost be C and the selling price S. Doubling S gives a profit of 2S - C, which equals 3(S - C). So 2S - C = 3S - 3C, giving S = 2C: the article sells for twice its cost, a profit of 100%. "
  "200% confuses the price being twice the cost with the profit being twice the cost; 50% and 150% have no basis.",
  "मान लें लागत C और विक्रय मूल्य S है। S दोगुना करने पर लाभ 2S - C होता है, जो 3(S - C) के बराबर है। अतः 2S - C = 3S - 3C, जिससे S = 2C: वस्तु अपनी लागत के दोगुने पर बिकती है, यानी 100% लाभ। "
  "200%, मूल्य के लागत का दोगुना होने को लाभ के लागत का दोगुना होने से भ्रमित करता है; 50% और 150% का कोई आधार नहीं।",
  "qa-pp-a-profit-that-triples", _pp1)

def _pp2():
    years = math.log(2) / math.log(1.07)
    assert 10 < years < 10.5 and abs(1.07 ** 10 - 2) < 0.05
    return "10"
N(QA, "Percentage & Profit-Loss", "medium",
  "If prices rise by 7% every year, roughly how many years will it take for prices to double?",
  "यदि मूल्य हर वर्ष 7% बढ़ें, तो मूल्यों को दोगुना होने में मोटे तौर पर कितने वर्ष लगेंगे?",
  ["7", "10", "14", "15"], 1,
  "The rise compounds: 1.07 multiplied by itself 10 times is about 1.97, so prices roughly double in 10 years. A handy rule: the doubling time is about 70 divided by the yearly percentage, here 70 ÷ 7 = 10. "
  "14 years assumes the rise does not compound (100 ÷ 7 ≈ 14.3); 7 confuses the rate with the time; 15 has no basis.",
  "बढ़त चक्रवृद्धि होती है: 1.07 को स्वयं से 10 बार गुणा करने पर लगभग 1.97 मिलता है, इसलिए मूल्य मोटे तौर पर 10 वर्ष में दोगुने होते हैं। एक सरल नियम: दोगुना होने का समय लगभग 70 बटा वार्षिक प्रतिशत, यहाँ 70 ÷ 7 = 10। "
  "14 वर्ष मानता है कि बढ़त चक्रवृद्धि नहीं होती (100 ÷ 7 ≈ 14.3); 7 दर को समय से भ्रमित करता है; 15 का कोई आधार नहीं।",
  "qa-pp-prices-that-double", _pp2)

def _pp3():
    before, after = F(30, 100) * 100, F(25, 100) * 110
    change = (after - before) / before * 100
    assert after == F(55, 2) and change == F(-25, 3)
    return "It has fallen by about 8.3%"
T(QA, "Percentage & Profit-Loss", "hard",
  "In a town, 30% of the people were below the poverty line. Five years later the town's population is 10% larger, and 25% of the people are below the line. How has the number of people below the line changed?",
  "एक कस्बे में 30% लोग ग़रीबी रेखा के नीचे थे। पाँच वर्ष बाद कस्बे की जनसंख्या 10% अधिक है, और 25% लोग रेखा के नीचे हैं। रेखा के नीचे के लोगों की संख्या कैसे बदली है?",
  ["It has fallen by about 8.3%", "It has fallen by 5%", "It has fallen by about 16.7%", "It has risen by 10%"],
  ["यह लगभग 8.3% घटी है", "यह 5% घटी है", "यह लगभग 16.7% घटी है", "यह 10% बढ़ी है"],
  0,
  "Take 100 people at first: 30 below the line. Five years later there are 110 people, and 25% of 110 = 27.5 are below it. The number has fallen from 30 to 27.5, by 2.5 ÷ 30 ≈ 8.3%. "
  "'Fallen by 5%' mistakes the drop of 5 percentage points for a 5% drop; 16.7% (5 ÷ 30) ignores the growth in population; 'risen by 10%' ignores the fall in the share.",
  "आरंभ में 100 लोग लें: 30 रेखा के नीचे। पाँच वर्ष बाद 110 लोग हैं, और 110 का 25% = 27.5 रेखा के नीचे हैं। संख्या 30 से घटकर 27.5 हुई, यानी 2.5 ÷ 30 ≈ 8.3%। "
  "'5% घटी' 5 प्रतिशत अंक की गिरावट को 5% की गिरावट समझ लेता है; 16.7% (5 ÷ 30) जनसंख्या की वृद्धि की अनदेखी करता है; '10% बढ़ी' हिस्से में गिरावट की अनदेखी करता है।",
  "qa-pp-people-below-a-line-in-a-growing-town", pos=0, check=_pp3)

# ---------------------------------------------------------------- Sequences & Series (2)
def _ss1():
    given = [2, 5, 10, 17, 26, 38, 50]
    wrong = [g for n, g in enumerate(given, 1) if g != n * n + 1]
    assert wrong == [38]
    return "38"
N(QA, "Sequences & Series", "easy",
  "Which number in the series 2, 5, 10, 17, 26, 38, 50 does not fit the pattern?",
  "श्रेणी 2, 5, 10, 17, 26, 38, 50 में कौन-सी संख्या पैटर्न में नहीं बैठती?",
  ["10", "17", "26", "38"], 3,
  "The terms are one more than the squares: 1 + 1, 4 + 1, 9 + 1, 16 + 1, 25 + 1, then 36 + 1 = 37 and 49 + 1 = 50. So 38 should be 37. (The gaps 3, 5, 7, 9 should go on 11, 13; the given gaps 12 and 12 break the pattern at 38.) "
  "10, 17 and 26 all fit as 3² + 1, 4² + 1 and 5² + 1.",
  "पद वर्गों से एक अधिक हैं: 1 + 1, 4 + 1, 9 + 1, 16 + 1, 25 + 1, फिर 36 + 1 = 37 और 49 + 1 = 50। इसलिए 38 को 37 होना चाहिए। (अंतर 3, 5, 7, 9 के बाद 11, 13 आने चाहिए; दिए गए अंतर 12 और 12, 38 पर पैटर्न तोड़ते हैं।) "
  "10, 17 और 26, 3² + 1, 4² + 1 और 5² + 1 के रूप में ठीक बैठते हैं।",
  "qa-ss-a-wrong-term-among-n-squared-plus-1", _ss1)

def _ss2():
    s = [n * n * (n + 1) for n in range(1, 7)]
    assert s[:5] == [2, 12, 36, 80, 150]
    return str(s[5])
N(QA, "Sequences & Series", "medium",
  "What is the next number in the series 2, 12, 36, 80, 150, ...?",
  "श्रेणी 2, 12, 36, 80, 150, ... की अगली संख्या क्या है?",
  ["210", "225", "240", "252"], 3,
  "The terms are n² × (n + 1): 1 × 2, 4 × 3, 9 × 4, 16 × 5, 25 × 6. The next is 36 × 7 = 252. (The gaps 10, 24, 44, 70 grow by 14, 20, 26, so the next gap is 70 + 32 = 102, and 150 + 102 = 252.) "
  "240 lets the gaps grow by 20 again (150 + 90); 210 = 5 × 6 × 7 belongs to a different pattern; 225 = 15² has no basis here.",
  "पद n² × (n + 1) हैं: 1 × 2, 4 × 3, 9 × 4, 16 × 5, 25 × 6। अगला 36 × 7 = 252 है। (अंतर 10, 24, 44, 70, 14, 20, 26 से बढ़ते हैं, इसलिए अगला अंतर 70 + 32 = 102 है, और 150 + 102 = 252।) "
  "240 अंतरों को फिर 20 से बढ़ाता है (150 + 90); 210 = 5 × 6 × 7 किसी दूसरे पैटर्न का है; 225 = 15² का यहाँ कोई आधार नहीं।",
  "qa-ss-n-squared-times-n-plus-1", _ss2)

# ---------------------------------------------------------------- Permutation & Combination (3)
def _pc1():
    n = sum(1 for p in product(range(3), repeat=4) if all(p[i] != p[i + 1] for i in range(3)))
    assert n == 3 * 2 ** 3 and 3 ** 4 == 81
    return str(n)
N(QA, "Permutation & Combination", "medium",
  "Four houses stand in a row. Each is to be painted in one of 3 colours so that no two neighbouring houses have the same colour. In how many ways can this be done?",
  "चार मकान एक पंक्ति में हैं। हर एक को 3 में से किसी एक रंग में ऐसे रंगना है कि कोई दो पड़ोसी मकान एक रंग के न हों। यह कितने प्रकार से किया जा सकता है?",
  ["24", "27", "48", "81"], 0,
  "The first house can take any of the 3 colours. Each house after it can take any colour except its left neighbour's: 2 choices each. So 3 × 2 × 2 × 2 = 24. "
  "81 = 3⁴ ignores the rule; 27 = 3 × 3 × 3 paints only three houses and ignores the rule for them; 48 doubles the answer for no reason.",
  "पहला मकान 3 में से कोई भी रंग ले सकता है। उसके बाद का हर मकान अपने बाएँ पड़ोसी के रंग को छोड़कर कोई भी रंग ले सकता है: हर बार 2 विकल्प। अतः 3 × 2 × 2 × 2 = 24। "
  "81 = 3⁴ नियम की अनदेखी करता है; 27 = 3 × 3 × 3 केवल तीन मकान रंगता है और उन पर भी नियम छोड़ देता है; 48 उत्तर को बिना कारण दोगुना करता है।",
  "qa-pc-houses-with-no-two-neighbours-alike", _pc1)

def _pc2():
    n = sum(1 for k in range(1, 7) for _ in combinations(range(6), k))
    assert n == 2 ** 6 - 1
    return str(n)
N(QA, "Permutation & Combination", "easy",
  "A thali comes with a choice of 6 different side dishes. A diner may take any number of them, but must take at least one. How many different selections are possible?",
  "एक थाली के साथ 6 अलग-अलग सहायक व्यंजनों का विकल्प है। भोजन करने वाला उनमें से कितने भी ले सकता है, पर कम से कम एक लेना आवश्यक है। कितने अलग-अलग चयन संभव हैं?",
  ["36", "63", "64", "720"], 1,
  "Each dish is either taken or left: 2 × 2 × 2 × 2 × 2 × 2 = 64 ways, one of which takes nothing. Leaving that out gives 63. "
  "64 forgets to remove the empty selection; 720 = 6! counts orders of serving, not selections; 36 has no basis.",
  "हर व्यंजन या तो लिया जाता है या छोड़ा जाता है: 2 × 2 × 2 × 2 × 2 × 2 = 64 प्रकार, जिनमें एक में कुछ नहीं लिया जाता। उसे छोड़ने पर 63। "
  "64 ख़ाली चयन हटाना भूल जाता है; 720 = 6! परोसने के क्रम गिनता है, चयन नहीं; 36 का कोई आधार नहीं।",
  "qa-pc-side-dishes-on-a-thali", _pc2)

def _pc3():
    distinct = [t for t in combinations(range(1, 12), 3) if sum(t) == 12]
    any3 = [t for t in product(range(1, 11), repeat=3) if sum(t) == 12 and t[0] <= t[1] <= t[2]]
    assert len(distinct) == 7 and len(any3) == 12
    return str(len(distinct))
N(QA, "Permutation & Combination", "hard",
  "In how many ways can 12 be written as the sum of three different positive whole numbers, if the order of the numbers does not matter?",
  "12 को तीन अलग-अलग धनात्मक पूर्ण संख्याओं के योग के रूप में कितने प्रकार से लिखा जा सकता है, यदि संख्याओं का क्रम मायने नहीं रखता?",
  ["5", "7", "12", "42"], 1,
  "List them with the smallest first: 1 + 2 + 9, 1 + 3 + 8, 1 + 4 + 7, 1 + 5 + 6; 2 + 3 + 7, 2 + 4 + 6; 3 + 4 + 5. Starting with 4 or more is impossible, since 4 + 5 + 6 = 15. That makes 7. "
  "12 also lets numbers repeat, adding 1 + 1 + 10, 2 + 2 + 8, 2 + 5 + 5, 3 + 3 + 6 and 4 + 4 + 4; 42 counts each of the 7 in all 6 orders; 5 has no basis.",
  "सबसे छोटी संख्या पहले रखकर सूची बनाएँ: 1 + 2 + 9, 1 + 3 + 8, 1 + 4 + 7, 1 + 5 + 6; 2 + 3 + 7, 2 + 4 + 6; 3 + 4 + 5। 4 या अधिक से शुरू करना असंभव है, क्योंकि 4 + 5 + 6 = 15। कुल 7। "
  "12 संख्याओं को दोहराने भी देता है, और 1 + 1 + 10, 2 + 2 + 8, 2 + 5 + 5, 3 + 3 + 6 तथा 4 + 4 + 4 जोड़ लेता है; 42 हर एक को सभी 6 क्रमों में गिनता है; 5 का कोई आधार नहीं।",
  "qa-pc-12-as-three-different-parts", _pc3)

# ---------------------------------------------------------------- Geometry & Mensuration (4)
def _gm1():
    v = 3 ** 3 + 4 ** 3 + 5 ** 3
    e = round(v ** (1 / 3))
    assert e ** 3 == v == 216
    return f"{e} cm"
N(QA, "Geometry & Mensuration", "medium",
  "Three solid metal cubes with edges of 3 cm, 4 cm and 5 cm are melted and recast into a single cube, with no metal lost. What is the edge of the new cube?",
  "3 सेमी, 4 सेमी और 5 सेमी किनारों वाले धातु के तीन ठोस घनों को पिघलाकर, बिना धातु गँवाए, एक घन में ढाला जाता है। नए घन का किनारा क्या है?",
  ["6 cm", "8 cm", "12 cm", "216 cm"], 0,
  "Melting keeps the volume: 3³ + 4³ + 5³ = 27 + 64 + 125 = 216 cm³, and 216 = 6³, so the new edge is 6 cm. "
  "12 cm adds the edges, as if lengths rather than volumes were kept; 216 is the volume in cm³, not an edge; 8 cm has no basis.",
  "पिघलाने से आयतन वही रहता है: 3³ + 4³ + 5³ = 27 + 64 + 125 = 216 घन सेमी, और 216 = 6³, इसलिए नया किनारा 6 सेमी है। "
  "12 सेमी किनारों को जोड़ता है, मानो आयतन के बजाय लंबाइयाँ बनी रहती हों; 216 घन सेमी में आयतन है, किनारा नहीं; 8 सेमी का कोई आधार नहीं।",
  "qa-gm-cubes-melted-into-one", _gm1,
  opts_hi=["6 सेमी", "8 सेमी", "12 सेमी", "216 सेमी"])

def _gm2():
    # walk the boundary of a 40 x 30 rectangle with a 10 x 10 corner removed
    pts = [(0, 0), (40, 0), (40, 20), (30, 20), (30, 30), (0, 30), (0, 0)]
    per = sum(abs(pts[i + 1][0] - pts[i][0]) + abs(pts[i + 1][1] - pts[i][1]) for i in range(len(pts) - 1))
    assert per == 140 == 2 * (40 + 30)
    return f"{per} m"
N(QA, "Geometry & Mensuration", "easy",
  "A plot is a 40 m × 30 m rectangle with a 10 m × 10 m square cut away from one corner. How long a fence is needed to go right round the plot that remains?",
  "एक भूखंड 40 मी × 30 मी का आयत है, जिसके एक कोने से 10 मी × 10 मी का वर्ग काट दिया गया है। बचे हुए भूखंड के चारों ओर पूरी बाड़ के लिए कितनी लंबाई चाहिए?",
  ["120 m", "140 m", "160 m", "1,100 m"], 1,
  "Cutting the corner removes 10 m from two sides but adds two new edges of 10 m each, so the perimeter is unchanged: 2 × (40 + 30) = 140 m. "
  "120 m subtracts the two lost pieces without adding the new edges; 160 m adds the new edges without subtracting; 1,100 m² is the remaining area, not a length.",
  "कोना काटने से दो भुजाओं से 10 मी घटते हैं पर 10-10 मी के दो नए किनारे जुड़ जाते हैं, इसलिए परिमाप वही रहता है: 2 × (40 + 30) = 140 मी। "
  "120 मी दोनों घटे टुकड़े घटाता है पर नए किनारे नहीं जोड़ता; 160 मी नए किनारे जोड़ता है पर घटाता नहीं; 1,100 वर्ग मी बचा हुआ क्षेत्रफल है, लंबाई नहीं।",
  "qa-gm-a-plot-with-a-corner-cut-away", _gm2,
  opts_hi=["120 मी", "140 मी", "160 मी", "1,100 मी"])

def _gm3():
    parts = [t for t in product(range(1, 11), repeat=3) if sum(t) == 12 and t[0] <= t[1] <= t[2]]
    tri = [t for t in parts if t[0] + t[1] > t[2]]
    flat_too = [t for t in parts if t[0] + t[1] >= t[2]]
    assert tri == [(2, 5, 5), (3, 4, 5), (4, 4, 4)] and len(flat_too) == 6 and len(parts) == 12
    return str(len(tri))
N(QA, "Geometry & Mensuration", "hard",
  "How many different triangles have whole-number sides (in cm) and a perimeter of 12 cm? (Triangles with the same three side lengths count once.)",
  "पूर्ण संख्या वाली भुजाओं (सेमी में) और 12 सेमी परिमाप वाले कितने अलग-अलग त्रिभुज हैं? (एक जैसी तीन भुजाओं वाले त्रिभुज एक बार गिने जाते हैं।)",
  ["1", "3", "6", "12"], 1,
  "The longest side must be less than half the perimeter, that is, less than 6 cm, or the other two could not reach round it. With the longest side 5: 2, 5, 5 and 3, 4, 5; with the longest side 4: 4, 4, 4. That makes 3. "
  "6 also counts 'flat' triangles such as 2, 4, 6, whose sides lie in a straight line; 12 counts every way of splitting 12 into three parts; 1 counts only the equilateral 4, 4, 4.",
  "सबसे लंबी भुजा परिमाप के आधे, यानी 6 सेमी, से कम होनी चाहिए, वरना बाक़ी दो उसके चारों ओर नहीं पहुँच सकतीं। सबसे लंबी भुजा 5 हो तो: 2, 5, 5 और 3, 4, 5; सबसे लंबी 4 हो तो: 4, 4, 4। कुल 3। "
  "6, 2, 4, 6 जैसे 'चपटे' त्रिभुज भी गिनता है, जिनकी भुजाएँ एक सीधी रेखा में होती हैं; 12, 12 को तीन भागों में बाँटने के हर ढंग को गिनता है; 1 केवल समबाहु 4, 4, 4 गिनता है।",
  "qa-gm-triangles-with-a-perimeter-of-12", _gm3)

def _gm4():
    v = (20 - 2 * 3) * (12 - 2 * 3) * 3
    assert v == 252 and (20 - 3) * (12 - 3) * 3 == 459 and (20 - 6) * (12 - 6) * 6 == 504 and 20 * 12 * 3 == 720
    return f"{v} cm³"
N(QA, "Geometry & Mensuration", "medium",
  "A square of side 3 cm is cut from each corner of a rectangular sheet measuring 20 cm × 12 cm, and the sides are then folded up to make an open box. What is the volume of the box?",
  "20 सेमी × 12 सेमी माप की एक आयताकार शीट के हर कोने से 3 सेमी भुजा का एक वर्ग काटा जाता है, और फिर किनारों को मोड़कर एक खुला डिब्बा बनाया जाता है। डिब्बे का आयतन क्या है?",
  ["252 cm³", "459 cm³", "504 cm³", "720 cm³"], 0,
  "Cutting 3 cm from both ends of each side leaves a base of (20 - 6) × (12 - 6) = 14 cm × 6 cm, and the folded flaps make the box 3 cm deep. Volume = 14 × 6 × 3 = 252 cm³. "
  "459 cm³ = 17 × 9 × 3 takes 3 cm off each length only once, forgetting that there are corners at both ends; 504 cm³ makes the box 6 cm deep, adding the two cuts together; 720 cm³ = 20 × 12 × 3 forgets that the corners were cut away.",
  "हर भुजा के दोनों सिरों से 3 सेमी काटने पर (20 - 6) × (12 - 6) = 14 सेमी × 6 सेमी का आधार बचता है, और मोड़े गए किनारे डिब्बे को 3 सेमी गहरा बनाते हैं। आयतन = 14 × 6 × 3 = 252 घन सेमी। "
  "459 घन सेमी = 17 × 9 × 3 हर लंबाई से 3 सेमी केवल एक बार घटाता है, यह भूलकर कि दोनों सिरों पर कोने हैं; 504 घन सेमी दोनों कटों को जोड़कर डिब्बे को 6 सेमी गहरा बना देता है; 720 घन सेमी = 20 × 12 × 3 भूल जाता है कि कोने काटे गए थे।",
  "qa-gm-an-open-box-folded-from-a-sheet", _gm4,
  opts_hi=["252 घन सेमी", "459 घन सेमी", "504 घन सेमी", "720 घन सेमी"])

# ---------------------------------------------------------------- Time & Work (2)
def _tw1():
    t = next(m for m in range(5, 120) if 20 * m == 30 * (m - 5))
    assert t == 15
    return f"9:{t:02d} am"
N(QA, "Time & Work", "medium",
  "Machine A fills 20 bottles a minute and machine B fills 30 bottles a minute. A starts at 9:00 am and B at 9:05 am. At what time will the two machines have filled equal numbers of bottles?",
  "मशीन A एक मिनट में 20 बोतलें भरती है और मशीन B एक मिनट में 30। A सुबह 9:00 बजे और B 9:05 बजे शुरू होती है। किस समय दोनों मशीनें बराबर बोतलें भर चुकी होंगी?",
  ["9:07 am", "9:10 am", "9:15 am", "9:25 am"], 2,
  "By 9:05 A has filled 100 bottles. B then gains 30 - 20 = 10 bottles a minute, so it catches up in 100 ÷ 10 = 10 minutes, at 9:15. Check: A has 15 × 20 = 300 and B 10 × 30 = 300. "
  "9:07 divides A's lead by both rates added (100 ÷ 50); 9:10 has B run only as long as A's head start; 9:25 has no basis.",
  "9:05 तक A 100 बोतलें भर चुकी है। फिर B हर मिनट 30 - 20 = 10 बोतलें आगे बढ़ती है, इसलिए वह 100 ÷ 10 = 10 मिनट में बराबर आ जाती है, 9:15 पर। जाँच: A ने 15 × 20 = 300 और B ने 10 × 30 = 300 भरीं। "
  "9:07, A की बढ़त को दोनों दरों के योग से भाग देता है (100 ÷ 50); 9:10 में B केवल A की बढ़त के समय जितना चलती है; 9:25 का कोई आधार नहीं।",
  "qa-tw-two-filling-machines-started-apart", _tw1,
  opts_hi=["सुबह 9:07", "सुबह 9:10", "सुबह 9:15", "सुबह 9:25"])

def _tw2():
    fast = next(x for x in range(1, 200) if F(1, x) + F(1, x + 10) == F(1, 12))
    assert fast == 20 and F(1, 24) + F(1, 24) == F(1, 12)
    return f"{fast} h"
N(QA, "Time & Work", "hard",
  "Two taps together fill a tank in 12 hours. One tap alone takes 10 hours longer than the other alone. How long does the faster tap take to fill the tank on its own?",
  "दो नल मिलकर एक टंकी 12 घंटे में भरते हैं। एक नल अकेले दूसरे से 10 घंटे अधिक लेता है। तेज़ नल अकेले टंकी भरने में कितना समय लेता है?",
  ["15 h", "18 h", "20 h", "24 h"], 2,
  "If the faster tap takes x hours, the slower takes x + 10, and 1/x + 1/(x + 10) = 1/12. Trying the options: 1/20 + 1/30 = 3/60 + 2/60 = 5/60 = 1/12, so x = 20 (the slower tap takes 30 hours). "
  "24 h treats the taps as equal (each would then take twice the joint time), which the 10-hour gap rules out; 15 h and 18 h fail the check (1/15 + 1/25 and 1/18 + 1/28 are not 1/12).",
  "यदि तेज़ नल x घंटे लेता है, तो धीमा x + 10 लेता है, और 1/x + 1/(x + 10) = 1/12। विकल्प आज़माएँ: 1/20 + 1/30 = 3/60 + 2/60 = 5/60 = 1/12, इसलिए x = 20 (धीमा नल 30 घंटे लेता है)। "
  "24 घंटे नलों को बराबर मान लेता है (तब हर एक संयुक्त समय का दोगुना लेता), जिसे 10 घंटे का अंतर नकारता है; 15 और 18 घंटे जाँच में विफल हैं (1/15 + 1/25 और 1/18 + 1/28, 1/12 नहीं हैं)।",
  "qa-tw-two-taps-ten-hours-apart", _tw2,
  opts_hi=["15 घंटे", "18 घंटे", "20 घंटे", "24 घंटे"])

# ---------------------------------------------------------------- Puzzle Hybrid (4)
def _ph1():
    n = 1000
    k = next(t for t in range(1, 20) if 2 ** t >= n)
    # binary pooling: test j holds every sample whose number has bit j set; the results spell out the bad sample
    for bad in (0, 1, 517, 999):
        res = [(bad >> j) & 1 for j in range(k)]
        assert sum(b << j for j, b in enumerate(res)) == bad
    assert k == 10 and 2 ** 9 < n
    return str(k)
N(QA, "Puzzle Hybrid", "medium",
  "Exactly one of 1,000 blood samples is contaminated. A test can be run on a pool made by mixing drops from any number of samples, and shows only whether the pool contains the contaminated sample. Results take a day, so all the tests must be run at the same time. What is the least number of tests that can always identify the contaminated sample?",
  "1,000 रक्त नमूनों में से ठीक एक दूषित है। किसी भी संख्या में नमूनों की बूँदें मिलाकर बने एक मिश्रण पर परीक्षण किया जा सकता है, जो केवल यह बताता है कि मिश्रण में दूषित नमूना है या नहीं। परिणाम एक दिन में आते हैं, इसलिए सभी परीक्षण एक साथ करने होंगे। कम से कम कितने परीक्षण सदा दूषित नमूना पहचान सकते हैं?",
  ["10", "20", "32", "500"], 0,
  "Number the samples 0 to 999 and write each number in binary, which needs 10 digits since 2¹⁰ = 1,024. Test 1 pools every sample whose first binary digit is 1, test 2 those whose second digit is 1, and so on. The ten results, positive or negative, spell out the contaminated sample's number. Nine tests give only 2⁹ = 512 patterns, too few for 1,000 samples. "
  "20 runs a second test beside each one for the opposite digit, which adds nothing; 32 comes from a grid of rows and columns, which would need even more tests; 500 tests half the samples one by one.",
  "नमूनों को 0 से 999 तक क्रमांक दें और हर संख्या को द्विआधारी (बाइनरी) में लिखें, जिसमें 10 अंक लगते हैं क्योंकि 2¹⁰ = 1,024। परीक्षण 1 में वे सभी नमूने मिलाएँ जिनका पहला बाइनरी अंक 1 है, परीक्षण 2 में जिनका दूसरा अंक 1 है, इत्यादि। दस परिणाम, धनात्मक या ऋणात्मक, दूषित नमूने का क्रमांक बता देते हैं। नौ परीक्षणों से केवल 2⁹ = 512 पैटर्न बनते हैं, जो 1,000 नमूनों के लिए कम हैं। "
  "20 हर परीक्षण के साथ उलटे अंक के लिए दूसरा परीक्षण चलाता है, जिससे कुछ नहीं जुड़ता; 32 पंक्तियों और स्तंभों के ग्रिड से आता है, जिसमें और भी अधिक परीक्षण लगते; 500 आधे नमूनों को एक-एक करके जाँचता है।",
  "qa-ph-samples-tested-in-pools", _ph1)

def _ph2():
    # Burn-out events reachable with two 60-minute ropes: at time 0 and at each burn-out, light any unlit ends.
    times = set()
    def go(t, ropes):
        # ropes: list of (remaining burn time from one end, lit ends); remaining None = burnt out
        live = [(r, k) for r, k in ropes if r is not None]
        if not live:
            return
        burning = [(r / k, i) for i, (r, k) in enumerate(ropes) if r is not None and k > 0]
        if not burning:
            return
        dt, i = min(burning)
        t2 = t + dt
        times.add(t2)
        nxt = []
        for j, (r, k) in enumerate(ropes):
            if r is None:
                nxt.append((None, 0))
            elif k == 0:
                nxt.append((r, 0))
            else:
                left = r - dt * k
                nxt.append((None, 0) if abs(left) < 1e-9 else (left, k))
        for adds in product(range(3), repeat=len(nxt)):
            new = []
            ok = True
            for (r, k), a in zip(nxt, adds):
                if r is None and a:
                    ok = False
                new.append((r, min(2, k + a)) if r is not None else (None, 0))
            if ok:
                go(t2, new)
    for a, b in product(range(3), repeat=2):
        if a or b:
            go(0, [(60, a), (60, b)])
    diffs = {round(abs(x - y), 6) for x in times | {0} for y in times | {0}}
    assert {15, 30, 45} <= diffs and 40 not in diffs and all(d % 15 == 0 for d in diffs)
    return "40 minutes"
T(QA, "Puzzle Hybrid", "medium",
  "Each of two ropes takes exactly 60 minutes to burn from one end to the other, but each burns unevenly, so half a rope need not take 30 minutes. With the two ropes and a lighter, and no clock, which one of the following intervals can NOT be measured?",
  "दो रस्सियों में से हर एक को एक सिरे से दूसरे तक जलने में ठीक 60 मिनट लगते हैं, पर हर एक असमान रूप से जलती है, इसलिए आधी रस्सी के लिए 30 मिनट लगना आवश्यक नहीं। दोनों रस्सियों और एक लाइटर से, बिना घड़ी के, निम्नलिखित में से कौन-सा अंतराल नहीं मापा जा सकता?",
  ["40 minutes", "15 minutes", "30 minutes", "45 minutes"],
  ["40 मिनट", "15 मिनट", "30 मिनट", "45 मिनट"],
  0,
  "Lighting a rope at both ends burns it in 30 minutes, however unevenly it burns. Light rope 1 at both ends and rope 2 at one end: when rope 1 is gone, 30 minutes have passed and rope 2 has 30 minutes left; lighting rope 2's other end then burns it out in 15 more minutes -- 45 minutes in all, with 15 and 30 marked along the way. Every time the ropes can mark is a multiple of 15 minutes, so 40 minutes cannot be measured. "
  "15, 30 and 45 minutes are all marked by the method above.",
  "रस्सी को दोनों सिरों से जलाने पर वह 30 मिनट में जल जाती है, चाहे जितनी असमान जले। रस्सी 1 को दोनों सिरों से और रस्सी 2 को एक सिरे से जलाएँ: रस्सी 1 ख़त्म होने पर 30 मिनट बीत चुके हैं और रस्सी 2 में 30 मिनट बचे हैं; तब रस्सी 2 का दूसरा सिरा जलाने से वह 15 मिनट और में जल जाती है -- कुल 45 मिनट, रास्ते में 15 और 30 चिह्नित होते हुए। रस्सियाँ जो भी समय चिह्नित कर सकती हैं वह 15 मिनट का गुणज होता है, इसलिए 40 मिनट नहीं मापे जा सकते। "
  "15, 30 और 45 मिनट ऊपर के तरीक़े से चिह्नित होते हैं।",
  "qa-ph-two-ropes-that-burn-unevenly", pos=3, check=_ph2)

def _ph3():
    cells = [(r, c_) for r in range(8) for c_ in range(8) if (r, c_) not in ((0, 0), (7, 7))]
    black = [p for p in cells if (p[0] + p[1]) % 2 == 0]
    white = [p for p in cells if (p[0] + p[1]) % 2 == 1]
    assert (len(black), len(white)) == (30, 32)
    # maximum matching between neighbouring squares (augmenting paths): fewer than 31 dominoes fit
    wset = set(white)
    match = {}
    def aug(b, seen):
        for d in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            w = (b[0] + d[0], b[1] + d[1])
            if w in wset and w not in seen:
                seen.add(w)
                if w not in match or aug(match[w], seen):
                    match[w] = b
                    return True
        return False
    size = sum(aug(b, set()) for b in black)
    assert size == 30 < 31
    return "No: the removed squares share a colour, leaving 30 of one colour and 32 of the other"
T(QA, "Puzzle Hybrid", "hard",
  "Two diagonally opposite corner squares are cut from a chessboard, leaving 62 squares. Can the remaining board be covered exactly by 31 dominoes, each domino covering two squares that share a side?",
  "एक शतरंज-बोर्ड से तिरछे आमने-सामने के दो कोने वाले खाने काट दिए जाते हैं, जिससे 62 खाने बचते हैं। क्या बचे बोर्ड को ठीक 31 डोमिनो से ढका जा सकता है, जिनमें हर डोमिनो एक भुजा साझा करने वाले दो खानों को ढकता है?",
  ["No: the removed squares share a colour, leaving 30 of one colour and 32 of the other",
   "Yes: the 62 squares that remain are exactly enough for 31 dominoes of two squares each",
   "Yes, but only if some of the dominoes are allowed to lie diagonally across squares",
   "No: a board can be covered by dominoes only if its number of squares is a multiple of 4"],
  ["नहीं: हटाए गए खाने एक ही रंग के हैं, जिससे एक रंग के 30 और दूसरे के 32 बचते हैं",
   "हाँ: बचे हुए 62 खाने दो-दो खानों वाले 31 डोमिनो के लिए ठीक पर्याप्त हैं",
   "हाँ, पर केवल तब जब कुछ डोमिनो खानों पर तिरछे रखने की अनुमति हो",
   "नहीं: बोर्ड को डोमिनो से तभी ढका जा सकता है जब उसके खानों की संख्या 4 का गुणज हो"],
  0,
  "Diagonally opposite corners of a chessboard are the same colour, so removing them leaves 30 squares of that colour and 32 of the other. Every domino covers two neighbouring squares, which are always of opposite colours, so 31 dominoes would cover 31 of each colour. The counts do not match, so it cannot be done. "
  "Having the right number of squares is not enough, as the colours show; a domino on a diagonal does not cover two squares that share a side; and a multiple of 4 is not required -- a 2 × 3 board of 6 squares is easily covered.",
  "शतरंज-बोर्ड के तिरछे आमने-सामने के कोने एक ही रंग के होते हैं, इसलिए उन्हें हटाने से उस रंग के 30 और दूसरे रंग के 32 खाने बचते हैं। हर डोमिनो दो पड़ोसी खानों को ढकता है, जो सदा विपरीत रंगों के होते हैं, इसलिए 31 डोमिनो हर रंग के 31 खाने ढकते। संख्याएँ मेल नहीं खातीं, इसलिए यह असंभव है। "
  "जैसा रंग दिखाते हैं, खानों की सही संख्या पर्याप्त नहीं; तिरछा डोमिनो भुजा साझा करने वाले दो खाने नहीं ढकता; और 4 का गुणज होना आवश्यक नहीं -- 6 खानों वाला 2 × 3 बोर्ड आसानी से ढक जाता है।",
  "qa-ph-a-chessboard-short-of-two-corners", pos=3, check=_ph3)

def _ph4():
    seen, frontier, steps = {1}, [1], 0
    while 100 not in seen:
        nxt = []
        for x in frontier:
            for y in (2 * x, x + 1):
                if y <= 200 and y not in seen:
                    seen.add(y); nxt.append(y)
        frontier, steps = nxt, steps + 1
    assert steps == 8
    return str(steps)
N(QA, "Puzzle Hybrid", "hard",
  "Starting from the number 1, at each step you may either double the number or add 1 to it. What is the least number of steps needed to reach exactly 100?",
  "संख्या 1 से शुरू करके, हर क़दम पर आप या तो संख्या को दोगुना कर सकते हैं या उसमें 1 जोड़ सकते हैं। ठीक 100 तक पहुँचने के लिए कम से कम कितने क़दम चाहिए?",
  ["7", "8", "9", "10"], 1,
  "Work backwards from 100, halving whenever the number is even and taking 1 away when it is odd: 100, 50, 25, 24, 12, 6, 3, 2, 1. That is 8 steps, and going forward: 1, 2, 3, 6, 12, 24, 25, 50, 100. Halving whenever possible is never worse, so 8 is the least. "
  "Seven steps are one too few: even doubling every time gives 1, 2, 4, ..., 128, and each 'add 1' used instead of a doubling lands well below 100. 9 and 10 steps are possible but not the least.",
  "100 से पीछे की ओर चलें, संख्या सम हो तो आधी करें और विषम हो तो 1 घटाएँ: 100, 50, 25, 24, 12, 6, 3, 2, 1। यह 8 क़दम हैं, और आगे की ओर: 1, 2, 3, 6, 12, 24, 25, 50, 100। जहाँ संभव हो आधा करना कभी बदतर नहीं, इसलिए 8 सबसे कम है। "
  "सात क़दम एक कम हैं: हर बार दोगुना करने पर भी 1, 2, 4, ..., 128 मिलता है, और दोगुना करने के बदले लिया गया हर '1 जोड़ो' 100 से काफ़ी नीचे रह जाता है। 9 और 10 क़दम संभव हैं पर सबसे कम नहीं।",
  "qa-ph-1-to-100-by-doubling-or-adding-one", _ph4)

# ---------------------------------------------------------------- the data-sufficiency block's two Quant items
def _ds1():
    s1 = {n for n in range(1, 200) if n % 6 == 0 and n % 8 == 0}
    s2 = set(range(41, 60))
    both = s1 & s2
    assert both == {48}
    return _ds(s1, s2, both)
DS(QA, "medium",
   "How many students are there in the class?",
   "कक्षा में कितने विद्यार्थी हैं?",
   "The students can be split exactly into groups of 6, and also exactly into groups of 8.", "विद्यार्थियों को ठीक 6-6 के समूहों में भी बाँटा जा सकता है, और ठीक 8-8 के समूहों में भी।",
   "There are more than 40 and fewer than 60 students.", "विद्यार्थी 40 से अधिक और 60 से कम हैं।",
   2,
   "Statement I alone: the number is a multiple of both 6 and 8, so a multiple of their LCM, 24 -- 24, 48, 72 and so on. Statement II alone allows any number from 41 to 59. Together, the only multiple of 24 between 40 and 60 is 48. Both statements are needed.",
   "कथन I अकेले: संख्या 6 और 8 दोनों की गुणज है, इसलिए उनके ल.स. 24 की गुणज -- 24, 48, 72 इत्यादि। कथन II अकेले 41 से 59 तक कोई भी संख्या होने देता है। दोनों मिलकर, 40 और 60 के बीच 24 का एकमात्र गुणज 48 है। दोनों कथन आवश्यक हैं।",
   "qa-ds-a-class-split-two-ways-and-bounded", _ds1)

def _ds2():
    s1 = {F(120 * 60, m) for m in range(91, 120)}                  # journey time in minutes, strictly between 90 and 120
    s2 = {v for v in range(5, 200, 5)}
    both = {v for v in s2 if 60 < v < 80}
    assert len(s1) > 1 and len(s2) > 1 and both == {65, 70, 75}
    return _ds(s1, s2, both)
DS(QA, "hard",
   "A car makes a journey of 120 km. What was its average speed?",
   "एक कार 120 किमी की यात्रा करती है। उसकी औसत चाल क्या थी?",
   "The journey took more than 1 hour 30 minutes but less than 2 hours.", "यात्रा में 1 घंटा 30 मिनट से अधिक पर 2 घंटे से कम समय लगा।",
   "The average speed, in km/h, was a whole number that is a multiple of 5.", "औसत चाल, किमी/घंटा में, एक पूर्ण संख्या थी जो 5 की गुणज है।",
   3,
   "Statement I alone puts the speed between 120 ÷ 2 = 60 and 120 ÷ 1.5 = 80 km/h, not including the ends. Statement II alone allows any multiple of 5. Together, the speed could be 65, 70 or 75 km/h -- still more than one value. So even both statements together are not enough.",
   "कथन I अकेले चाल को 120 ÷ 2 = 60 और 120 ÷ 1.5 = 80 किमी/घंटा के बीच रखता है, सिरों को छोड़कर। कथन II अकेले 5 का कोई भी गुणज होने देता है। दोनों मिलकर चाल 65, 70 या 75 किमी/घंटा हो सकती है -- फिर भी एक से अधिक मान। अतः दोनों कथन मिलकर भी पर्याप्त नहीं।",
   "qa-ds-a-speed-boxed-in-but-not-fixed", _ds2)
