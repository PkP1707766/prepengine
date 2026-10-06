# -*- coding: utf-8 -*-
"""CSAT Level 2 · Test 5 -- Quantitative Aptitude (34 items: 32 in the Quant slots, 2 in the data-sufficiency block).

Same mix as Tests 1-4 (playbook B.7) with none of their question shapes: remainder 1 for 2 and for 3, the digit
sum of 10²⁵ - 25, three consecutive even numbers, the smallest square that 6, 8 and 15 divide, an HCF from prime
powers, 2ˣ = 3ʸ = 6ᶻ, a triangular number whose digits are all alike, the least number to subtract for a square;
24 km in 1 hour 20 minutes, a stolen car chased, a car gaining 2 km each hour, speeds from the times after meeting;
a compound ratio, shares as fractions of the others, boys leaving and girls joining, technicians in an average,
inverse-square variation; a gain equal to the price of 11 metres, a pass mark from two candidates, simple interest
from double to triple; squares of primes, a sum of numbers with remainder 1; a password count, 53 Sundays in a leap
year; a wheel's turns, a rhombus from its diagonals; three pairs of workers, wages with a helper; matchsticks in a
row, handshakes, an exact spend on pens and notebooks, and race margins that do not add. The build spreads the
topics through the paper (csat_common.interleave). Difficulty 3 easy / 19 medium / 12 hard; every key is worked out
in code by check()."""
import math
from fractions import Fraction as F
from itertools import permutations, product
import csat_common as c
from csat_common import N, DS, QA

def _only(values):
    values = set(values)
    return str(values.pop()) if len(values) == 1 else "?"

def _ds(s1, s2, both):
    alone = (len(set(s1)) == 1, len(set(s2)) == 1)
    return "b" if all(alone) else "a" if any(alone) else "c" if len(set(both)) == 1 else "d"

# ---------------------------------------------------------------- Number Theory (8)
def _nt1():
    hits = [n for n in range(1, 101) if n % 2 == 1 and n % 3 == 1]
    assert len([n for n in range(1, 101) if n % 3 == 1]) == 34 and 100 // 3 == 33
    return str(len(hits))
N(QA, "Number Theory", "easy",
  "How many of the numbers from 1 to 100 leave a remainder of 1 when divided by 2 and also leave a remainder of 1 when divided by 3?",
  "1 से 100 तक की संख्याओं में से कितनी संख्याएँ 2 से भाग देने पर 1 शेषफल छोड़ती हैं और 3 से भाग देने पर भी 1 शेषफल छोड़ती हैं?",
  ["17", "33", "34", "50"], 0,
  "A number that leaves remainder 1 on division by both 2 and 3 leaves remainder 1 on division by their LCM, 6: 1, 7, 13, ..., 97. That makes (97 - 1)/6 + 1 = 17 numbers. "
  "34 counts only the condition for 3 and 50 only the condition for 2 (the odd numbers); 33 counts the multiples of 3 instead.",
  "जो संख्या 2 और 3 दोनों से भाग देने पर 1 शेषफल छोड़ती है, वह उनके LCM 6 से भाग देने पर भी 1 शेषफल छोड़ती है: 1, 7, 13, ..., 97। ये (97 - 1)/6 + 1 = 17 संख्याएँ हैं। "
  "34 केवल 3 वाली शर्त गिनता है और 50 केवल 2 वाली (विषम संख्याएँ); 33 इसके बजाय 3 के गुणज गिनता है।",
  "qa-nt-remainder-one-for-2-and-3", _nt1)

def _nt2():
    n = 10 ** 25 - 25
    assert str(n).count("9") == 23 and str(n).endswith("75")
    return str(sum(int(d) for d in str(n)))
N(QA, "Number Theory", "hard",
  "What is the sum of the digits of 10²⁵ - 25?",
  "10²⁵ - 25 के अंकों का योग क्या है?",
  ["207", "212", "219", "225"], 2,
  "10²⁵ is 1 followed by 25 zeros, and subtracting 25 leaves a 25-digit number: twenty-three 9s followed by 75. Its digit sum is 23 × 9 + 7 + 5 = 207 + 12 = 219. "
  "207 counts only the 9s; 212 also forgets the 7; 225 treats the number as twenty-five 9s, which is 10²⁵ - 1.",
  "10²⁵ में 1 के बाद 25 शून्य हैं, और 25 घटाने पर 25 अंकों की संख्या बचती है: तेईस 9 और उनके बाद 75। इसके अंकों का योग 23 × 9 + 7 + 5 = 207 + 12 = 219 है। "
  "207 केवल 9 गिनता है; 212 उसके साथ 7 भी भूल जाता है; 225 संख्या को पच्चीस 9 मानता है, जो 10²⁵ - 1 है।",
  "qa-nt-digit-sum-of-ten-to-25-less-25", _nt2)

def _nt3():
    starts = [a for a in range(2, 100, 2) if a * (a + 2) * (a + 4) == 480]
    return _only(3 * a + 6 for a in starts)
N(QA, "Number Theory", "medium",
  "The product of three consecutive even numbers is 480. What is their sum?",
  "तीन क्रमागत सम संख्याओं का गुणनफल 480 है। उनका योग क्या है?",
  ["18", "24", "30", "36"], 1,
  "The cube root of 480 is a little under 8, so try the even numbers around 8: 6 × 8 × 10 = 480. Their sum is 24. "
  "18 and 30 come from the neighbouring triples, 4 × 6 × 8 = 192 and 8 × 10 × 12 = 960; 36 is the sum of 10, 12 and 14.",
  "480 का घनमूल 8 से थोड़ा कम है, इसलिए 8 के आसपास की सम संख्याएँ आज़माइए: 6 × 8 × 10 = 480। उनका योग 24 है। "
  "18 और 30 पड़ोसी तिकड़ियों से आते हैं, 4 × 6 × 8 = 192 और 8 × 10 × 12 = 960; 36, 10, 12 और 14 का योग है।",
  "qa-nt-three-consecutive-even-numbers", _nt3)

def _nt4():
    sq = next(k * k for k in range(1, 1000) if k * k % 6 == 0 and k * k % 8 == 0 and k * k % 15 == 0)
    assert 900 % 8 and math.isqrt(1800) ** 2 != 1800 and math.isqrt(360) ** 2 != 360
    return str(sq)
N(QA, "Number Theory", "medium",
  "What is the smallest perfect square that is divisible by each of 6, 8 and 15?",
  "वह सबसे छोटा पूर्ण वर्ग कौन-सा है जो 6, 8 और 15 में से प्रत्येक से विभाज्य है?",
  ["360", "900", "1800", "3600"], 3,
  "LCM(6, 8, 15) = 120 = 2³ × 3 × 5. A perfect square needs every prime to an even power, so the smallest square that 120 divides is 2⁴ × 3² × 5² = 3600 (= 60²). "
  "900 = 30² is a square divisible by 6 and 15 but not by 8; 360 and 1800 are multiples of 120 that are not squares.",
  "LCM(6, 8, 15) = 120 = 2³ × 3 × 5। पूर्ण वर्ग में हर अभाज्य की घात सम होनी चाहिए, इसलिए 120 से विभाज्य सबसे छोटा वर्ग 2⁴ × 3² × 5² = 3600 (= 60²) है। "
  "900 = 30² एक वर्ग है जो 6 और 15 से विभाज्य है पर 8 से नहीं; 360 और 1800, 120 के गुणज हैं पर वर्ग नहीं।",
  "qa-nt-smallest-square-for-6-8-15", _nt4)

def _nt5():
    nums = (2 ** 4 * 3 ** 2 * 5, 2 ** 3 * 3 ** 3 * 7, 2 ** 2 * 3 ** 4 * 5 * 7)
    return str(math.gcd(*nums))
N(QA, "Number Theory", "medium",
  "What is the HCF of 2⁴ × 3² × 5, 2³ × 3³ × 7 and 2² × 3⁴ × 5 × 7?",
  "2⁴ × 3² × 5, 2³ × 3³ × 7 और 2² × 3⁴ × 5 × 7 का HCF क्या है?",
  ["12", "18", "24", "36"], 3,
  "The HCF takes each prime to the lowest power found in all three numbers: 2 appears in all of them at least as 2², 3 at least as 3², and 5 and 7 are each missing from one number. So the HCF is 2² × 3² = 36. "
  "18 = 2 × 3² takes too low a power of 2; 24 = 2³ × 3 takes too high a power of 2 and too low a power of 3; 12 = 2² × 3 takes too low a power of 3.",
  "HCF हर अभाज्य को उस सबसे छोटी घात में लेता है जो तीनों संख्याओं में मिलती है: 2 तीनों में कम से कम 2² के रूप में है, 3 कम से कम 3² के रूप में, और 5 तथा 7 एक-एक संख्या में नहीं हैं। अतः HCF = 2² × 3² = 36। "
  "18 = 2 × 3² में 2 की घात बहुत कम है; 24 = 2³ × 3 में 2 की घात अधिक और 3 की कम है; 12 = 2² × 3 में 3 की घात बहुत कम है।",
  "qa-nt-hcf-from-prime-powers", _nt5)

def _nt6():
    for z in (2.0, 0.5, 3.0):                # not z = 1, where z and 1/z coincide
        k = 6 ** z
        x, y = math.log(k, 2), math.log(k, 3)
        vals = {"xy/(x + y)": x * y / (x + y), "(x + y)/xy": (x + y) / (x * y), "x + y": x + y, "√(xy)": math.sqrt(x * y)}
        hits = [name for name, v in vals.items() if abs(v - z) < 1e-9]
        assert len(hits) == 1, (z, hits)
    return hits[0]
N(QA, "Number Theory", "hard",
  "If 2ˣ = 3ʸ = 6ᶻ, where x, y and z are not zero, then z is equal to:",
  "यदि 2ˣ = 3ʸ = 6ᶻ, जहाँ x, y और z शून्य नहीं हैं, तो z बराबर है:",
  ["xy/(x + y)", "(x + y)/xy", "x + y", "√(xy)"], 0,
  "Let 2ˣ = 3ʸ = 6ᶻ = k. Then 2 = k^(1/x), 3 = k^(1/y) and 6 = k^(1/z). Since 6 = 2 × 3, k^(1/z) = k^(1/x) × k^(1/y) = k^(1/x + 1/y), so 1/z = 1/x + 1/y and z = xy/(x + y). "
  "(x + y)/xy is 1/z, the reciprocal of the answer; x + y adds the exponents instead of their reciprocals; √(xy) has no basis.",
  "मान लीजिए 2ˣ = 3ʸ = 6ᶻ = k। तब 2 = k^(1/x), 3 = k^(1/y) और 6 = k^(1/z)। चूँकि 6 = 2 × 3, k^(1/z) = k^(1/x) × k^(1/y) = k^(1/x + 1/y), अतः 1/z = 1/x + 1/y और z = xy/(x + y)। "
  "(x + y)/xy, 1/z है, उत्तर का व्युत्क्रम; x + y घातांकों के व्युत्क्रमों के बजाय घातांकों को जोड़ता है; √(xy) का कोई आधार नहीं।",
  "qa-nt-two-three-six-exponents", _nt6)

def _nt7():
    found = [n for n in range(1, 50) if 100 <= n * (n + 1) // 2 <= 999 and len(set(str(n * (n + 1) // 2))) == 1]
    assert 44 * 45 // 2 == 990 and 45 * 46 // 2 == 1035
    return _only(found)
N(QA, "Number Theory", "hard",
  "The sum 1 + 2 + 3 + ... + n is a three-digit number whose digits are all the same. What is n?",
  "योग 1 + 2 + 3 + ... + n तीन अंकों की एक ऐसी संख्या है जिसके सभी अंक एक जैसे हैं। n क्या है?",
  ["36", "37", "44", "45"], 0,
  "1 + 2 + ... + n = n(n + 1)/2, and a three-digit number with equal digits is 111 × d = 3 × 37 × d. So n(n + 1) = 2 × 3 × 37 × d, and as 37 is prime, n or n + 1 must be a multiple of 37; the sum is below 1000, so n is at most 44, and n or n + 1 is 37 itself. "
  "n = 36 gives 36 × 37/2 = 666, while n = 37 gives 703. So n = 36. 37 is the prime factor, not n; 44 gives 990, whose digits differ; 45 gives 1035, which has four digits.",
  "1 + 2 + ... + n = n(n + 1)/2, और समान अंकों वाली तीन अंकों की संख्या 111 × d = 3 × 37 × d है। अतः n(n + 1) = 2 × 3 × 37 × d, और चूँकि 37 अभाज्य है, n या n + 1, 37 का गुणज होना चाहिए; योग 1000 से कम है, इसलिए n अधिकतम 44 है, और n या n + 1 स्वयं 37 है। "
  "n = 36 से 36 × 37/2 = 666 मिलता है, जबकि n = 37 से 703। अतः n = 36। 37 अभाज्य गुणनखंड है, n नहीं; 44 से 990 मिलता है, जिसके अंक अलग हैं; 45 से 1035, जिसमें चार अंक हैं।",
  "qa-nt-triangular-number-with-equal-digits", _nt7)

def _nt8():
    root = math.isqrt(7000)
    assert (root + 1) ** 2 - 7000 == 56 and 7000 - (root - 1) ** 2 == 276
    return str(7000 - root * root)
N(QA, "Number Theory", "medium",
  "What is the least number that must be subtracted from 7000 to leave a perfect square?",
  "7000 में से कम से कम कौन-सी संख्या घटाई जाए कि एक पूर्ण वर्ग बचे?",
  ["56", "111", "276", "6889"], 1,
  "83² = 6889 and 84² = 7056, so the largest square below 7000 is 6889, and 7000 - 6889 = 111 must be subtracted. "
  "56 is the least number to add, to reach 84² = 7056; 276 subtracts down to 82² = 6724, which is not the nearest square; 6889 is the square that is left, not the number taken away.",
  "83² = 6889 और 84² = 7056, इसलिए 7000 से छोटा सबसे बड़ा वर्ग 6889 है, और 7000 - 6889 = 111 घटाना होगा। "
  "56 जोड़ी जाने वाली सबसे छोटी संख्या है, जिससे 84² = 7056 बनता है; 276 घटाकर 82² = 6724 तक पहुँचता है, जो सबसे पास का वर्ग नहीं; 6889 बचने वाला वर्ग है, घटाई गई संख्या नहीं।",
  "qa-nt-least-subtracted-for-a-square", _nt8)

# ---------------------------------------------------------------- Speed-Distance-Time (4)
def _sdt1():
    speed = F(24) / (1 + F(20, 60))
    assert F(24) / F(12, 10) == 20 and F(24) / F(125, 100) == F(96, 5)
    return str(speed)
N(QA, "Speed-Distance-Time", "easy",
  "A cyclist covers 24 km in 1 hour 20 minutes. What is the cyclist's speed in km/h?",
  "एक साइकिल सवार 24 किमी की दूरी 1 घंटा 20 मिनट में तय करता है। उसकी चाल किमी/घंटा में क्या है?",
  ["18", "19.2", "20", "24"], 0,
  "1 hour 20 minutes is 1⅓ hours, so the speed is 24 ÷ 4/3 = 18 km/h. "
  "20 reads 1 hour 20 minutes as 1.2 hours; 19.2 reads the 20 minutes as a quarter of an hour; 24 ignores the 20 minutes.",
  "1 घंटा 20 मिनट, 1⅓ घंटे हैं, इसलिए चाल 24 ÷ 4/3 = 18 किमी/घंटा है। "
  "20, 1 घंटा 20 मिनट को 1.2 घंटे पढ़ता है; 19.2, 20 मिनट को चौथाई घंटा मानता है; 24, 20 मिनट को अनदेखा करता है।",
  "qa-sdt-24-km-in-an-hour-and-20-minutes", _sdt1)

def _sdt2():
    head_start = F(60) * F(1, 2)            # 2:30 to 3:00 at 60 km/h
    hours = head_start / (75 - 60)
    end = 15 * 60 + hours * 60              # minutes after midnight
    assert end.denominator == 1
    h, m = divmod(int(end), 60)
    return f"{h - 12}:{m:02d} p.m."
N(QA, "Speed-Distance-Time", "medium",
  "A car is stolen at 2:30 p.m. and driven away at 60 km/h. The theft is discovered at 3:00 p.m., and the owner sets off at once in another car at 75 km/h. At what time does the owner catch up?",
  "एक कार दोपहर 2:30 बजे चोरी होती है और 60 किमी/घंटा की चाल से ले जाई जाती है। चोरी का पता दोपहर 3:00 बजे चलता है, और मालिक तुरंत दूसरी कार में 75 किमी/घंटा की चाल से पीछा करता है। मालिक किस समय चोर तक पहुँचेगा?",
  ["3:24 p.m.", "4:30 p.m.", "5:00 p.m.", "7:00 p.m."], 2,
  "By 3:00 p.m. the thief is 30 km ahead (half an hour at 60 km/h). The owner closes the gap at 75 - 60 = 15 km/h, so it takes 30/15 = 2 hours: 5:00 p.m. "
  "3:24 p.m. treats the thief as standing still (30 km at 75 km/h); 4:30 p.m. counts the 2 hours from the theft instead of from the start of the chase; 7:00 p.m. takes the head start as a full hour, 60 km.",
  "दोपहर 3:00 बजे तक चोर 30 किमी आगे है (60 किमी/घंटा पर आधा घंटा)। मालिक 75 - 60 = 15 किमी/घंटा से दूरी घटाता है, इसलिए 30/15 = 2 घंटे लगते हैं: शाम 5:00 बजे। "
  "3:24 बजे चोर को रुका हुआ मानता है (75 किमी/घंटा पर 30 किमी); 4:30 बजे 2 घंटे पीछा शुरू होने के बजाय चोरी के समय से गिनता है; 7:00 बजे आगे होने की दूरी को पूरा एक घंटा, यानी 60 किमी, मानता है।",
  "qa-sdt-stolen-car-chased", _sdt2,
  opts_hi=["दोपहर 3:24 बजे", "शाम 4:30 बजे", "शाम 5:00 बजे", "शाम 7:00 बजे"])

def _sdt3():
    hours = [35 + 2 * k for k in range(12)]
    assert 35 * 12 + 2 * 12 == 444 and 12 * (35 + 2 * 5) == 540
    return f"{sum(hours)} km"
N(QA, "Speed-Distance-Time", "medium",
  "A car covers 35 km in its first hour, and in each later hour it covers 2 km more than in the hour before. How far does it travel in 12 hours?",
  "एक कार पहले घंटे में 35 किमी चलती है, और उसके बाद के हर घंटे में पिछले घंटे से 2 किमी अधिक चलती है। 12 घंटों में वह कितनी दूरी तय करती है?",
  ["420 km", "444 km", "540 km", "552 km"], 3,
  "The hourly distances, 35, 37, ..., 57, form an arithmetic progression of 12 terms, so the total is 12/2 × (35 + 57) = 6 × 92 = 552 km. "
  "420 km ignores the increase; 444 km adds the extra 2 km only once for each hour, not cumulatively; 540 km multiplies 12 by the sixth hour's 45 km instead of by the average, 46 km.",
  "हर घंटे की दूरियाँ, 35, 37, ..., 57, 12 पदों की समांतर श्रेणी बनाती हैं, इसलिए कुल दूरी 12/2 × (35 + 57) = 6 × 92 = 552 किमी है। "
  "420 किमी वृद्धि को अनदेखा करता है; 444 किमी अतिरिक्त 2 किमी को हर घंटे के लिए केवल एक बार जोड़ता है, संचयी रूप से नहीं; 540 किमी, 12 को औसत 46 किमी के बजाय छठे घंटे के 45 किमी से गुणा करता है।",
  "qa-sdt-gaining-2-km-each-hour", _sdt3,
  opts_hi=["420 किमी", "444 किमी", "540 किमी", "552 किमी"])

def _sdt4():
    ratios = [F(a, b) for a in range(1, 20) for b in range(1, 20) if F(a, b) ** 2 == F(9, 4)]
    r = ratios[0]
    assert all(x == r for x in ratios)
    return f"{r.numerator} : {r.denominator}"
N(QA, "Speed-Distance-Time", "hard",
  "Two cars set out at the same time from towns A and B towards each other. After they meet, the car from A takes 4 hours more to reach B, and the car from B takes 9 hours more to reach A. "
  "What is the ratio of the speed of the car from A to the speed of the car from B?",
  "दो कारें एक ही समय पर कस्बों A और B से एक-दूसरे की ओर चलती हैं। मिलने के बाद A वाली कार को B तक पहुँचने में 4 घंटे और लगते हैं, और B वाली कार को A तक पहुँचने में 9 घंटे और। "
  "A वाली कार की चाल का B वाली कार की चाल से अनुपात क्या है?",
  ["4 : 9", "2 : 3", "3 : 2", "9 : 4"], 2,
  "Let them meet after t hours. After meeting, the car from A covers the stretch that the car from B had covered: v_B × t = v_A × 4. In the same way v_A × t = v_B × 9. "
  "Dividing one by the other, (v_A/v_B)² = 9/4, so v_A : v_B = 3 : 2. 9 : 4 and 4 : 9 forget to take the square root; 2 : 3 turns the answer the wrong way round.",
  "मान लीजिए वे t घंटे बाद मिलती हैं। मिलने के बाद A वाली कार वह हिस्सा तय करती है जो B वाली कार तय कर चुकी थी: v_B × t = v_A × 4। इसी तरह v_A × t = v_B × 9। "
  "एक को दूसरे से भाग देने पर (v_A/v_B)² = 9/4, अतः v_A : v_B = 3 : 2। 9 : 4 और 4 : 9 वर्गमूल लेना भूल जाते हैं; 2 : 3 उत्तर को उलट देता है।",
  "qa-sdt-speeds-from-times-after-meeting", _sdt4)

# ---------------------------------------------------------------- Ratio, Mixtures & Alligation (5)
def _rm1():
    a, b1 = F(2), F(3)
    b2, cc = F(4), F(5)
    scale1, scale2 = b2, b1                 # make b the same: 2 : 3 = 8 : 12 and 4 : 5 = 12 : 15
    return f"{a * scale1} : {b1 * scale1} : {cc * scale2}"
N(QA, "Ratio, Mixtures & Alligation", "easy",
  "If a : b = 2 : 3 and b : c = 4 : 5, what is a : b : c?",
  "यदि a : b = 2 : 3 और b : c = 4 : 5, तो a : b : c क्या है?",
  ["2 : 3 : 5", "2 : 4 : 5", "8 : 12 : 15", "8 : 15 : 12"], 2,
  "b must be the same in both ratios: 2 : 3 = 8 : 12 and 4 : 5 = 12 : 15, so a : b : c = 8 : 12 : 15. "
  "2 : 3 : 5 and 2 : 4 : 5 join the ratios without making b the same in both; 8 : 15 : 12 swaps b and c.",
  "दोनों अनुपातों में b एक जैसा होना चाहिए: 2 : 3 = 8 : 12 और 4 : 5 = 12 : 15, अतः a : b : c = 8 : 12 : 15। "
  "2 : 3 : 5 और 2 : 4 : 5 अनुपातों को b को बराबर किए बिना जोड़ देते हैं; 8 : 15 : 12, b और c को आपस में बदल देता है।",
  "qa-rm-joining-two-ratios", _rm1)

def _rm2():
    sols = [(a, b, 4200 - a - b) for a in range(0, 4201, 50) for b in range(0, 4201 - a, 50)
            if 2 * a == b + (4200 - a - b) and 3 * b == a + (4200 - a - b)]
    assert sols == [(1400, 1050, 1750)]
    return f"₹{sols[0][2]:,}"
N(QA, "Ratio, Mixtures & Alligation", "hard",
  "₹4,200 is divided among A, B and C so that A gets half of what B and C get together, and B gets one-third of what A and C get together. How much does C get?",
  "₹4,200 को A, B और C में इस प्रकार बाँटा जाता है कि A को B और C के मिले-जुले हिस्से का आधा मिलता है, और B को A और C के मिले-जुले हिस्से का एक-तिहाई। C को कितना मिलता है?",
  ["₹1,050", "₹1,400", "₹1,750", "₹2,100"], 2,
  "If A gets half of what B and C get together, then A is one part in three of the whole: A = 4200/3 = ₹1,400. If B gets one-third of what A and C get together, B is one part in four: B = 4200/4 = ₹1,050. "
  "C gets the rest, 4200 - 1400 - 1050 = ₹1,750. ₹1,400 and ₹1,050 are A's and B's shares; ₹2,100 reads 'half' as half of the whole sum.",
  "यदि A को B और C के मिले-जुले हिस्से का आधा मिलता है, तो A पूरे का तीन में से एक भाग है: A = 4200/3 = ₹1,400। यदि B को A और C के मिले-जुले हिस्से का एक-तिहाई मिलता है, तो B चार में से एक भाग है: B = 4200/4 = ₹1,050। "
  "C को बाक़ी, 4200 - 1400 - 1050 = ₹1,750, मिलता है। ₹1,400 और ₹1,050, A और B के हिस्से हैं; ₹2,100 'आधे' को पूरी राशि का आधा पढ़ता है।",
  "qa-rm-shares-as-fractions-of-the-others", _rm2)

def _rm3():
    xs = [x for x in range(1, 100) if 5 * x - 10 == 3 * x + 10]
    return _only(8 * x for x in xs)
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "In a class the ratio of boys to girls is 5 : 3. If 10 boys leave and 10 girls join, the numbers of boys and girls become equal. How many students were there in the class at first?",
  "एक कक्षा में लड़कों और लड़कियों का अनुपात 5 : 3 है। यदि 10 लड़के चले जाएँ और 10 लड़कियाँ आ जाएँ, तो लड़कों और लड़कियों की संख्या बराबर हो जाती है। शुरू में कक्षा में कितने विद्यार्थी थे?",
  ["30", "40", "50", "80"], 3,
  "Let there be 5x boys and 3x girls. Then 5x - 10 = 3x + 10, so x = 10: 50 boys and 30 girls, 80 students -- and still 80 afterwards, since 10 left and 10 joined. "
  "50 and 30 are the boys and the girls at first; 40 is the number of each after the change.",
  "मान लीजिए 5x लड़के और 3x लड़कियाँ हैं। तब 5x - 10 = 3x + 10, अतः x = 10: 50 लड़के और 30 लड़कियाँ, कुल 80 विद्यार्थी -- और बाद में भी 80, क्योंकि 10 गए और 10 आए। "
  "50 और 30 शुरू के लड़के और लड़कियाँ हैं; 40 बदलाव के बाद हर एक की संख्या है।",
  "qa-rm-boys-leave-girls-join", _rm3)

def _rm4():
    n = next(n for n in range(8, 200) if 7 * 12000 + (n - 7) * 6000 == 8000 * n)
    avg = lambda m: F(7 * 12000 + (m - 7) * 6000, m)
    assert avg(28) == 7500 and avg(24) == 7750
    return str(n)
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "The average salary of all the workers in a workshop is ₹8,000 a month. The average salary of its 7 technicians is ₹12,000 and that of the other workers is ₹6,000. How many workers are there in all?",
  "एक कार्यशाला के सभी कर्मचारियों का औसत मासिक वेतन ₹8,000 है। उसके 7 तकनीशियनों का औसत वेतन ₹12,000 और बाक़ी कर्मचारियों का ₹6,000 है। कुल कितने कर्मचारी हैं?",
  ["14", "21", "24", "28"], 1,
  "Each technician is ₹4,000 above the average and each of the others ₹2,000 below it, and the gaps must balance: 7 × 4,000 = (others) × 2,000, so there are 14 others and 21 workers in all. "
  "14 is the number of other workers only; with 24 workers the average would be ₹7,750, and with 28 it would be ₹7,500.",
  "हर तकनीशियन औसत से ₹4,000 ऊपर है और बाक़ी हर कर्मचारी ₹2,000 नीचे, और ये अंतर बराबर होने चाहिए: 7 × 4,000 = (बाक़ी) × 2,000, इसलिए बाक़ी 14 हैं और कुल 21 कर्मचारी। "
  "14 केवल बाक़ी कर्मचारियों की संख्या है; 24 कर्मचारियों पर औसत ₹7,750 होता, और 28 पर ₹7,500।",
  "qa-rm-technicians-in-an-average", _rm4)

def _rm5():
    k = F(9) * 2 ** 2                      # x = k / y²
    assert F(18, 3) == 6 and F(9, 2) * 3 == F(27, 2) and F(9, 4) * 9 == F(81, 4)
    return str(k / 3 ** 2)
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "x varies inversely as the square of y. When y = 2, x = 9. What is the value of x when y = 3?",
  "x, y के वर्ग के व्युत्क्रमानुपाती है। जब y = 2, तब x = 9। जब y = 3, तब x का मान क्या है?",
  ["4", "6", "13.5", "20.25"], 0,
  "x × y² stays the same: 9 × 2² = 36, so when y = 3, x = 36/9 = 4. "
  "6 treats x as inversely proportional to y itself (x × y = 18); 13.5 treats it as directly proportional to y; 20.25 as directly proportional to y².",
  "x × y² स्थिर रहता है: 9 × 2² = 36, इसलिए y = 3 होने पर x = 36/9 = 4। "
  "6, x को स्वयं y के व्युत्क्रमानुपाती मानता है (x × y = 18); 13.5 उसे y के समानुपाती मानता है; 20.25, y² के समानुपाती।",
  "qa-rm-inverse-square-variation", _rm5)

# ---------------------------------------------------------------- Percentage & Profit-Loss (3)
def _pp1():
    sp = F(1)                               # selling price of one metre
    cp33 = 33 * sp - 11 * sp                # gain on 33 m equals the price of 11 m
    gain = (33 * sp - cp33) / cp33 * 100
    assert F(11, 33) * 100 == F(100, 3) and F(22, 33) * 100 == F(200, 3)
    return f"{gain}%"
N(QA, "Percentage & Profit-Loss", "hard",
  "By selling 33 metres of cloth, a trader gains the selling price of 11 metres. What is his gain per cent?",
  "33 मीटर कपड़ा बेचकर एक व्यापारी 11 मीटर के विक्रय मूल्य के बराबर लाभ कमाता है। उसका लाभ प्रतिशत क्या है?",
  ["25%", "33⅓%", "50%", "66⅔%"], 2,
  "The gain on 33 metres equals the price of 11, so the cost of 33 metres equals the price of 22. The selling price is therefore 33/22 = 1.5 times the cost: a gain of 50%. "
  "33⅓% = 11/33 measures the gain against the selling price instead of the cost; 66⅔% = 22/33 is the cost as a share of the price; 25% = 11/44 adds the 11 metres to the 33.",
  "33 मीटर पर लाभ 11 मीटर के मूल्य के बराबर है, इसलिए 33 मीटर की लागत 22 मीटर के मूल्य के बराबर है। अतः विक्रय मूल्य लागत का 33/22 = 1.5 गुना है: 50% लाभ। "
  "33⅓% = 11/33 लाभ को लागत के बजाय विक्रय मूल्य से मापता है; 66⅔% = 22/33 लागत को मूल्य के अंश के रूप में दिखाता है; 25% = 11/44, 11 मीटर को 33 में जोड़ देता है।",
  "qa-pp-gain-equals-price-of-11-metres", _pp1)

def _pp2():
    m = next(m for m in range(10, 2000) if F(30, 100) * m + 15 == F(40, 100) * m - 35)
    return str(int(F(30, 100) * m + 15))
N(QA, "Percentage & Profit-Loss", "medium",
  "A candidate who scores 30% of the maximum marks fails by 15 marks. Another candidate who scores 40% gets 35 marks more than the pass mark. What is the pass mark?",
  "अधिकतम अंकों का 30% पाने वाला एक परीक्षार्थी 15 अंकों से अनुत्तीर्ण होता है। 40% पाने वाला दूसरा परीक्षार्थी उत्तीर्ण अंक से 35 अंक अधिक पाता है। उत्तीर्ण अंक क्या है?",
  ["150", "165", "185", "200"], 1,
  "The pass mark is both 30% + 15 and 40% - 35 of the maximum, so 10% of the maximum is 50 marks and the maximum is 500. The pass mark is 150 + 15 = 165. "
  "150 is 30% of 500, forgetting the 15 marks; 200 is 40% of 500; 185 adds the 35 to 150.",
  "उत्तीर्ण अंक अधिकतम अंकों का 30% + 15 भी है और 40% - 35 भी, इसलिए अधिकतम का 10% = 50 अंक और अधिकतम अंक 500 हैं। उत्तीर्ण अंक 150 + 15 = 165 है। "
  "150, 500 का 30% है, 15 अंक भूलकर; 200, 500 का 40% है; 185, 150 में 35 जोड़ देता है।",
  "qa-pp-pass-mark-from-two-candidates", _pp2)

def _pp3():
    rate = F(100, 8)                        # % a year, from doubling in 8 years
    return str(F(200) / rate)
N(QA, "Percentage & Profit-Loss", "medium",
  "At simple interest, a sum of money doubles itself in 8 years. In how many years will it become three times itself?",
  "साधारण ब्याज पर कोई धनराशि 8 वर्षों में दोगुनी हो जाती है। वह कितने वर्षों में तीन गुनी हो जाएगी?",
  ["8", "12", "16", "24"], 2,
  "Doubling means the interest equals the sum, 100%, in 8 years: 12.5% a year. To become three times itself the sum must earn 200%, which takes 200 ÷ 12.5 = 16 years. "
  "8 is the extra time after the first 8 years, not the total; 12 scales the 8 years by 3/2; 24 scales them by 3, as if the sum itself had to be earned three times.",
  "दोगुना होने का अर्थ है कि 8 वर्षों में ब्याज धनराशि के बराबर, यानी 100%, हुआ: 12.5% प्रति वर्ष। तीन गुना होने के लिए 200% ब्याज चाहिए, जिसमें 200 ÷ 12.5 = 16 वर्ष लगेंगे। "
  "8, पहले 8 वर्षों के बाद का अतिरिक्त समय है, कुल नहीं; 12, 8 वर्षों को 3/2 से गुणा करता है; 24 उन्हें 3 से गुणा करता है, मानो धनराशि को तीन बार कमाना हो।",
  "qa-pp-simple-interest-double-to-triple", _pp3)

# ---------------------------------------------------------------- Sequences & Series (2)
def _ss1():
    primes = [p for p in range(2, 20) if all(p % d for d in range(2, p))]
    series = [p * p for p in primes[:6]]
    assert series[:4] == [4, 9, 25, 49] and series[5] == 169
    return str(series[4])
N(QA, "Sequences & Series", "medium",
  "What number should replace the question mark in the series 4, 9, 25, 49, ?, 169?",
  "श्रेणी 4, 9, 25, 49, ?, 169 में प्रश्नचिह्न के स्थान पर कौन-सी संख्या आएगी?",
  ["64", "81", "100", "121"], 3,
  "The terms are the squares of the prime numbers in order: 2², 3², 5², 7², 11², 13². The missing term is 11² = 121. "
  "64, 81 and 100 are 8², 9² and 10², the squares that follow 7² if the series is mistaken for one of consecutive squares.",
  "पद क्रम से अभाज्य संख्याओं के वर्ग हैं: 2², 3², 5², 7², 11², 13²। लुप्त पद 11² = 121 है। "
  "64, 81 और 100, 8², 9² और 10² हैं, वे वर्ग जो श्रेणी को लगातार संख्याओं के वर्गों की श्रेणी समझने पर 7² के बाद आते।",
  "qa-ss-squares-of-primes", _ss1)

def _ss2():
    terms = [n for n in range(10, 100) if n % 4 == 1]
    assert sum(n for n in terms if n <= 93) == 1113 and sum(terms) + 101 == 1311 and sum(n for n in range(10, 100) if n % 2) == 2475
    return str(sum(terms))
N(QA, "Sequences & Series", "hard",
  "What is the sum of all the two-digit numbers that leave a remainder of 1 when divided by 4?",
  "उन सभी दो अंकों वाली संख्याओं का योग क्या है जो 4 से भाग देने पर 1 शेषफल छोड़ती हैं?",
  ["1113", "1210", "1311", "2475"], 1,
  "The numbers are 13, 17, 21, ..., 97, an arithmetic progression with common difference 4. There are (97 - 13)/4 + 1 = 22 of them, so the sum is 22 × (13 + 97)/2 = 22 × 55 = 1210. "
  "1113 stops at 93 and misses the last term; 1311 runs on to 101, which has three digits; 2475 adds all the odd two-digit numbers.",
  "संख्याएँ 13, 17, 21, ..., 97 हैं, 4 के सार्व अंतर वाली समांतर श्रेणी। इनकी संख्या (97 - 13)/4 + 1 = 22 है, इसलिए योग 22 × (13 + 97)/2 = 22 × 55 = 1210 है। "
  "1113, 93 पर रुककर अंतिम पद छोड़ देता है; 1311, 101 तक चला जाता है, जिसमें तीन अंक हैं; 2475 दो अंकों की सभी विषम संख्याओं को जोड़ता है।",
  "qa-ss-sum-with-remainder-one-by-four", _ss2)

# ---------------------------------------------------------------- Permutation & Combination (2)
def _pc1():
    letters = sum(1 for _ in permutations("ABCDE", 3))
    total = letters * 10 * 10
    assert letters == 60 and letters * 10 == 600 and letters * 10 * 9 == 5400
    return f"{total:,}"
N(QA, "Permutation & Combination", "medium",
  "A password is made of 3 different letters chosen from A, B, C, D and E, followed by 2 digits from 0 to 9, which may be the same. How many such passwords are possible?",
  "एक पासवर्ड A, B, C, D और E में से चुने गए 3 अलग-अलग अक्षरों और उसके बाद 0 से 9 तक के 2 अंकों से बनता है, जो एक जैसे भी हो सकते हैं। ऐसे कितने पासवर्ड संभव हैं?",
  ["60", "600", "5,400", "6,000"], 3,
  "The letters can be arranged in 5 × 4 × 3 = 60 ways, and each of the 2 digits has 10 choices, so there are 60 × 10 × 10 = 6,000 passwords. "
  "60 counts the letters alone; 600 allows only one digit; 5,400 = 60 × 10 × 9 wrongly makes the two digits different.",
  "अक्षर 5 × 4 × 3 = 60 तरीकों से रखे जा सकते हैं, और 2 अंकों में से हर एक के 10 विकल्प हैं, इसलिए 60 × 10 × 10 = 6,000 पासवर्ड बनते हैं। "
  "60 केवल अक्षर गिनता है; 600 केवल एक अंक लेता है; 5,400 = 60 × 10 × 9 ग़लती से दोनों अंकों को अलग-अलग कर देता है।",
  "qa-pc-password-letters-then-digits", _pc1)

def _pc2():
    good = sum(1 for start in range(7) if 0 in (start, (start + 1) % 7))   # 0 = Sunday; a leap year has 52 weeks + 2 days
    p = F(good, 7)
    return f"{p.numerator}/{p.denominator}"
N(QA, "Permutation & Combination", "hard",
  "A leap year is chosen at random. What is the probability that it has 53 Sundays?",
  "यादृच्छिक रूप से एक लीप वर्ष चुना जाता है। उसमें 53 रविवार होने की प्रायिकता क्या है?",
  ["52/366", "1/7", "53/366", "2/7"], 3,
  "A leap year has 366 days: 52 full weeks, which give 52 Sundays, plus 2 extra days in a row. There is a 53rd Sunday when one of those two days is a Sunday. "
  "The pair can be Sunday-Monday, Monday-Tuesday, ..., Saturday-Sunday, 7 cases equally likely, and 2 of them contain a Sunday: 2/7. "
  "1/7 is the answer for an ordinary year, which has only one extra day; 52/366 and 53/366 count days instead of weeks.",
  "लीप वर्ष में 366 दिन होते हैं: 52 पूरे सप्ताह, जिनसे 52 रविवार मिलते हैं, और लगातार 2 अतिरिक्त दिन। 53वाँ रविवार तब होता है जब उन दो दिनों में से एक रविवार हो। "
  "यह जोड़ी रविवार-सोमवार, सोमवार-मंगलवार, ..., शनिवार-रविवार हो सकती है, 7 समान संभावना वाली स्थितियाँ, और उनमें से 2 में रविवार है: 2/7। "
  "1/7 साधारण वर्ष का उत्तर है, जिसमें केवल एक अतिरिक्त दिन होता है; 52/366 और 53/366 सप्ताहों के बजाय दिन गिनते हैं।",
  "qa-pc-fifty-three-sundays", _pc2)

# ---------------------------------------------------------------- Geometry & Mensuration (2)
def _gm1():
    circumference = 2 * F(22, 7) * 35       # cm
    turns = F(110000) / circumference
    assert circumference == 220 and F(110000) / (2 * F(22, 7) * 70) == 250 and F(110000) / (F(22, 7) * 35) == 1000
    return str(turns)
N(QA, "Geometry & Mensuration", "medium",
  "A wheel of radius 35 cm rolls along a road without slipping. How many complete turns does it make in covering 1.1 km? (Take π = 22/7.)",
  "35 सेमी त्रिज्या वाला एक पहिया बिना फिसले सड़क पर लुढ़कता है। 1.1 किमी तय करने में वह कितने पूरे चक्कर लगाता है? (π = 22/7 लीजिए।)",
  ["250", "500", "1000", "5000"], 1,
  "In one turn the wheel moves its circumference, 2 × 22/7 × 35 = 220 cm. 1.1 km = 110,000 cm, so it makes 110,000 ÷ 220 = 500 turns. "
  "250 uses the diameter, 70 cm, as if it were the radius; 1000 uses πr, half the circumference; 5000 slips a decimal place in converting 1.1 km to centimetres.",
  "एक चक्कर में पहिया अपनी परिधि जितना, 2 × 22/7 × 35 = 220 सेमी, चलता है। 1.1 किमी = 110,000 सेमी, इसलिए वह 110,000 ÷ 220 = 500 चक्कर लगाता है। "
  "250, व्यास 70 सेमी को त्रिज्या मान लेता है; 1000, πr, यानी आधी परिधि, लेता है; 5000, 1.1 किमी को सेंटीमीटर में बदलते समय दशमलव का एक स्थान खिसका देता है।",
  "qa-gm-turns-of-a-wheel", _gm1)

def _gm2():
    side = math.isqrt(8 ** 2 + 6 ** 2)
    assert side * side == 100 and math.isqrt(16 ** 2 + 12 ** 2) == 20
    return f"{4 * side} cm"
N(QA, "Geometry & Mensuration", "medium",
  "The diagonals of a rhombus are 16 cm and 12 cm long. What is its perimeter?",
  "एक समचतुर्भुज के विकर्ण 16 सेमी और 12 सेमी लंबे हैं। उसका परिमाप क्या है?",
  ["40 cm", "56 cm", "80 cm", "112 cm"], 0,
  "The diagonals of a rhombus bisect each other at right angles, so each side is the hypotenuse of a right triangle with legs 8 cm and 6 cm: √(64 + 36) = 10 cm. The perimeter is 4 × 10 = 40 cm. "
  "80 cm uses the whole diagonals as the legs (√(16² + 12²) = 20); 56 cm adds the diagonals and doubles; 112 cm takes 16 + 12 = 28 as a side.",
  "समचतुर्भुज के विकर्ण एक-दूसरे को समकोण पर समद्विभाजित करते हैं, इसलिए हर भुजा 8 सेमी और 6 सेमी आधार-लंब वाले समकोण त्रिभुज का कर्ण है: √(64 + 36) = 10 सेमी। परिमाप 4 × 10 = 40 सेमी है। "
  "80 सेमी पूरे विकर्णों को भुजाएँ मानता है (√(16² + 12²) = 20); 56 सेमी विकर्णों को जोड़कर दोगुना करता है; 112 सेमी, 16 + 12 = 28 को भुजा मानता है।",
  "qa-gm-rhombus-from-its-diagonals", _gm2,
  opts_hi=["40 सेमी", "56 सेमी", "80 सेमी", "112 सेमी"])

# ---------------------------------------------------------------- Time & Work (2)
def _tw1():
    pairs = F(1, 10) + F(1, 15) + F(1, 12)  # (A+B) + (B+C) + (A+C) = 2(A+B+C)
    assert pairs == F(1, 4) and F(10 + 15 + 12, 3) == F(37, 3)
    return str(1 / (pairs / 2))
N(QA, "Time & Work", "medium",
  "A and B together can finish a job in 10 days, B and C together in 15 days, and A and C together in 12 days. In how many days can A, B and C together finish it?",
  "A और B मिलकर एक काम 10 दिनों में, B और C मिलकर 15 दिनों में, और A और C मिलकर 12 दिनों में पूरा कर सकते हैं। A, B और C मिलकर उसे कितने दिनों में पूरा करेंगे?",
  ["4", "8", "12⅓", "37"], 1,
  "Adding the three pairs counts each person twice: 1/10 + 1/15 + 1/12 = 15/60 = 1/4 of the job a day is twice what A, B and C do together. So the three together do 1/8 a day and finish in 8 days. "
  "4 forgets that each person was counted twice; 12⅓ averages the three times; 37 adds them.",
  "तीनों जोड़ियों को जोड़ने पर हर व्यक्ति दो बार गिना जाता है: 1/10 + 1/15 + 1/12 = 15/60 = प्रतिदिन काम का 1/4, जो A, B और C के मिले-जुले काम का दोगुना है। अतः तीनों मिलकर प्रतिदिन 1/8 काम करते हैं और 8 दिनों में पूरा करते हैं। "
  "4 भूल जाता है कि हर व्यक्ति दो बार गिना गया; 12⅓ तीनों समयों का औसत लेता है; 37 उन्हें जोड़ देता है।",
  "qa-tw-three-pairs-of-workers", _tw1)

def _tw2():
    a, b = F(3, 6), F(3, 8)                 # work done in the 3 days
    cpart = 1 - a - b
    assert 3200 * a == 1600 and 3200 * b == 1200
    return f"₹{int(3200 * cpart):,}"
N(QA, "Time & Work", "hard",
  "A can do a job in 6 days and B in 8 days. With C's help they finish it in 3 days and are paid ₹3,200 for it. If the money is shared in proportion to the work done, how much should C get?",
  "A किसी काम को 6 दिनों में और B 8 दिनों में कर सकता है। C की मदद से वे उसे 3 दिनों में पूरा करते हैं और उसके लिए ₹3,200 पाते हैं। यदि धन किए गए काम के अनुपात में बाँटा जाए, तो C को कितना मिलना चाहिए?",
  ["₹400", "₹1,067", "₹1,200", "₹1,600"], 0,
  "In the 3 days A does 3/6 = 1/2 of the job and B does 3/8, together 7/8, so C does the remaining 1/8 and gets 1/8 of ₹3,200 = ₹400. "
  "₹1,600 and ₹1,200 are A's and B's shares; ₹1,067 splits the money equally among the three.",
  "3 दिनों में A काम का 3/6 = 1/2 और B, 3/8 करता है, मिलकर 7/8, इसलिए C बाक़ी 1/8 करता है और ₹3,200 का 1/8 = ₹400 पाता है। "
  "₹1,600 और ₹1,200, A और B के हिस्से हैं; ₹1,067 धन को तीनों में बराबर बाँट देता है।",
  "qa-tw-wages-with-a-helper", _tw2)

# ---------------------------------------------------------------- Puzzle Hybrid (4)
def _ph1():
    sticks = lambda n: 4 + 3 * (n - 1)
    assert sticks(1) == 4 and sticks(2) == 7
    return str(sticks(10))
N(QA, "Puzzle Hybrid", "medium",
  "Squares are made from matchsticks in a single row, each new square sharing one side with the square before it. How many matchsticks are needed for a row of 10 squares?",
  "माचिस की तीलियों से एक ही पंक्ति में वर्ग बनाए जाते हैं, हर नया वर्ग पिछले वर्ग के साथ एक भुजा साझा करता है। 10 वर्गों की पंक्ति के लिए कितनी तीलियाँ चाहिए?",
  ["11", "30", "31", "40"], 2,
  "The first square needs 4 sticks, and each of the other 9 needs only 3 more, because it shares a side with the one before: 4 + 9 × 3 = 31. "
  "40 gives every square its own 4 sticks; 30 forgets the first square's extra side; 11 counts only the upright sticks.",
  "पहले वर्ग को 4 तीलियाँ चाहिए, और बाक़ी 9 में से हर एक को केवल 3 और, क्योंकि वह पिछले वर्ग के साथ एक भुजा साझा करता है: 4 + 9 × 3 = 31। "
  "40 हर वर्ग को अपनी 4 तीलियाँ देता है; 30 पहले वर्ग की अतिरिक्त भुजा भूल जाता है; 11 केवल खड़ी तीलियाँ गिनता है।",
  "qa-ph-matchsticks-for-a-row-of-squares", _ph1)

def _ph2():
    return _only(n for n in range(2, 100) if n * (n - 1) // 2 == 28)
N(QA, "Puzzle Hybrid", "medium",
  "At a meeting, every person shook hands once with every other person, and there were 28 handshakes in all. How many people were at the meeting?",
  "एक बैठक में हर व्यक्ति ने हर दूसरे व्यक्ति से एक बार हाथ मिलाया, और कुल 28 बार हाथ मिलाए गए। बैठक में कितने लोग थे?",
  ["8", "14", "28", "56"], 0,
  "With n people there are n(n - 1)/2 handshakes, since each pair shakes hands once. n(n - 1) = 56 = 8 × 7, so there were 8 people. "
  "56 forgets to halve, counting every handshake twice; 14 halves the 28; 28 counts one person for each handshake.",
  "n लोगों में n(n - 1)/2 बार हाथ मिलाए जाते हैं, क्योंकि हर जोड़ी एक बार हाथ मिलाती है। n(n - 1) = 56 = 8 × 7, अतः 8 लोग थे। "
  "56 आधा करना भूल जाता है और हर हाथ मिलाना दो बार गिनता है; 14, 28 का आधा है; 28 हर बार हाथ मिलाने पर एक व्यक्ति गिनता है।",
  "qa-ph-twenty-eight-handshakes", _ph2)

def _ph3():
    sols = [(p, n) for p in range(1, 15) for n in range(1, 10) if 7 * p + 11 * n == 100]
    assert sols == [(8, 4)]
    return str(sols[0][1])
N(QA, "Puzzle Hybrid", "hard",
  "Pens cost ₹7 each and notebooks ₹11 each. A student spends exactly ₹100 on pens and notebooks, buying at least one of each. How many notebooks does the student buy?",
  "पेन ₹7 प्रति नग और नोटबुक ₹11 प्रति नग हैं। एक विद्यार्थी पेन और नोटबुक पर ठीक ₹100 ख़र्च करता है, और हर एक कम से कम एक ख़रीदता है। विद्यार्थी कितनी नोटबुक ख़रीदता है?",
  ["1", "2", "3", "4"], 3,
  "Whatever the notebooks cost, the rest must be a multiple of 7. Trying each number: 1 notebook leaves ₹89, 2 leave ₹78, 3 leave ₹67 -- none a multiple of 7 -- while 4 leave ₹56 = 8 × 7. "
  "So the student buys 4 notebooks and 8 pens, and no other combination makes exactly ₹100.",
  "नोटबुक पर जितना भी ख़र्च हो, बाक़ी राशि 7 का गुणज होनी चाहिए। हर संख्या आज़माइए: 1 नोटबुक से ₹89 बचते हैं, 2 से ₹78, 3 से ₹67 -- इनमें से कोई 7 का गुणज नहीं -- जबकि 4 से ₹56 = 8 × 7 बचते हैं। "
  "अतः विद्यार्थी 4 नोटबुक और 8 पेन ख़रीदता है, और कोई दूसरा मेल ठीक ₹100 नहीं बनाता।",
  "qa-ph-exact-spend-on-pens-and-notebooks", _ph3)

def _ph4():
    b_when_a_finishes = F(90)
    c_when_a_finishes = b_when_a_finishes * F(90, 100)
    return str(100 - c_when_a_finishes)
N(QA, "Puzzle Hybrid", "hard",
  "In a 100 m race A beats B by 10 m, and in another 100 m race B beats C by 10 m. Running at the same speeds, by how many metres would A beat C in a 100 m race?",
  "100 मीटर की एक दौड़ में A, B को 10 मीटर से हराता है, और 100 मीटर की दूसरी दौड़ में B, C को 10 मीटर से हराता है। उन्हीं चालों से दौड़ते हुए A, 100 मीटर की दौड़ में C को कितने मीटर से हराएगा?",
  ["18", "19", "20", "21"], 1,
  "When A runs 100 m, B runs 90 m. C runs 90 m for every 100 m that B runs, so while B runs 90 m, C runs 81 m. A therefore beats C by 100 - 81 = 19 m. "
  "Adding the two margins gives 20, but B's 10 m lead over C is over a full 100 m, while in A's race B covers only 90 m; 18 and 21 are near misses with no such basis.",
  "जब A, 100 मीटर दौड़ता है, B, 90 मीटर दौड़ता है। B के हर 100 मीटर पर C, 90 मीटर दौड़ता है, इसलिए जब B, 90 मीटर दौड़ता है, C, 81 मीटर दौड़ता है। अतः A, C को 100 - 81 = 19 मीटर से हराता है। "
  "दोनों अंतर जोड़ने पर 20 आता है, पर C पर B की 10 मीटर की बढ़त पूरे 100 मीटर पर है, जबकि A की दौड़ में B केवल 90 मीटर तय करता है; 18 और 21 ऐसे निकट उत्तर हैं जिनका कोई आधार नहीं।",
  "qa-ph-race-margins-do-not-add", _ph4)

# ---------------------------------------------------------------- the data-sufficiency block's two Quant items
def _ds1():
    xs = [F(k, 4) for k in range(-40, 41)]
    return _ds([x * x > x for x in xs if x > 1], [x * x > x for x in xs if x < 0], [])
DS(QA, "medium",
   "Is x² greater than x? (x is a real number.)",
   "क्या x², x से बड़ा है? (x एक वास्तविक संख्या है।)",
   "x > 1", "x > 1",
   "x < 0", "x < 0",
   1,
   "Statement I: for x greater than 1, x² = x × x is more than x -- yes. Statement II: for a negative x, x² is positive and so more than x -- yes. Either statement alone answers the question. "
   "The trap is to expect a 'no' among the negative numbers; the 'no' cases lie from 0 to 1, which neither statement allows.",
   "कथन I: 1 से बड़े x के लिए x² = x × x, x से अधिक है -- हाँ। कथन II: ऋणात्मक x के लिए x² धनात्मक है और इसलिए x से अधिक -- हाँ। कोई भी एक कथन अकेले प्रश्न का उत्तर दे देता है। "
   "जाल ऋणात्मक संख्याओं में 'नहीं' की अपेक्षा करना है; 'नहीं' वाली स्थितियाँ 0 से 1 के बीच हैं, जिन्हें कोई भी कथन अनुमति नहीं देता।",
   "qa-ds-is-x-squared-more-than-x", _ds1)

def _ds2():
    lengths = range(10, 400, 10)
    speeds1 = [F(l + 200, 20) for l in lengths]                 # I: (length + 200) = 20 v
    speeds2 = [F(l, 10) for l in lengths]                       # II: length = 10 v
    both = [F(l, 10) for l in lengths if F(l + 200, 20) == F(l, 10)]
    return _ds(speeds1, speeds2, both)
DS(QA, "hard",
   "What is the speed of the train?",
   "रेलगाड़ी की चाल क्या है?",
   "It crosses a platform 200 m long in 20 seconds.", "वह 200 मीटर लंबे प्लेटफ़ॉर्म को 20 सेकंड में पार करती है।",
   "It passes a pole in 10 seconds.", "वह एक खंभे को 10 सेकंड में पार करती है।",
   2,
   "Statement I gives (length + 200) = 20 × speed, two unknowns -- not sufficient. Statement II gives length = 10 × speed -- not sufficient. "
   "Together, 10 × speed + 200 = 20 × speed, so the speed is 20 m/s (72 km/h). Each statement needs the train's length, which only the other supplies.",
   "कथन I से (लंबाई + 200) = 20 × चाल मिलता है, दो अज्ञात -- पर्याप्त नहीं। कथन II से लंबाई = 10 × चाल -- पर्याप्त नहीं। "
   "दोनों साथ: 10 × चाल + 200 = 20 × चाल, इसलिए चाल 20 मीटर/सेकंड (72 किमी/घंटा) है। हर कथन को रेलगाड़ी की लंबाई चाहिए, जो केवल दूसरा देता है।",
   "qa-ds-speed-of-the-train", _ds2)
