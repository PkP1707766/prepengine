# -*- coding: utf-8 -*-
"""CSAT Level 4 · Simulator 7 -- Quantitative Aptitude (38 items: 36 in the Quant slots, 2 in the data-sufficiency block).

Layout A, the 2023/2024 shape: Quant-heavy, number theory the largest bucket (10). Exam-level mix (9 easy / 18 medium /
11 hard), with none of the shapes of Levels 1-3 or Simulators 1-6: the rational one among four numbers, the whole
numbers either side of √200, numbers below 50 co-prime to 50, the factor pairs of 36, the HCF of three decimals,
integers whose squares are below 50, the largest factorial below a million, a remainder when a number is tripled, the
last digit of the odd numbers multiplied, a surd plus its reciprocal; boxes on a conveyor belt, a late
start that ends in a tie, a wheel's turns per minute, speeds whose ratio changes; a percentile from a rank, a see-saw
balanced, a quantity varying with two others, gold mixed by carats, the areas of two circles from their rims; a mobile plan
that is cheaper only past a point, an insurance payout above an excess, the years for a machine to lose half its
value; three numbers in AP from their sum and product, an AP whose fifth term is three times its first; two girls
given at least one, books chosen with two fixed, even three-digit numbers from five digits; turfing a plot, the litres
in a hemispherical bowl; ploughing with more oxen, a tap whose flow halves every hour; heads and legs, the steps from 6
to 1, dates whose day times month is 27, a rope ladder and a rising tide, the next palindrome on an odometer; and two
data-sufficiency items. Every key is worked out in code by check()."""
from fractions import Fraction as F
from itertools import combinations, permutations, product
import datetime as dt
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

# ---------------------------------------------------------------- Number Theory (10)
def _nt1():
    vals = {"√2 × √8": math.sqrt(2) * math.sqrt(8), "√3 + 1": math.sqrt(3) + 1, "√5": math.sqrt(5), "√3 × √5": math.sqrt(15)}
    whole = [k for k, v in vals.items() if abs(v - round(v)) < 1e-12]
    assert whole == ["√2 × √8"]
    return "√2 × √8"
T(QA, "Number Theory", "easy",
  "Which one of the following is a rational number?",
  "निम्नलिखित में से कौन-सी एक परिमेय संख्या है?",
  ["√2 × √8", "√3 + 1", "√5", "√3 × √5"], ["√2 × √8", "√3 + 1", "√5", "√3 × √5"],
  0,
  "√2 × √8 = √16 = 4, a whole number and so rational. √5 is irrational; adding 1 to the irrational √3 keeps it irrational; and √3 × √5 = √15, which is not a perfect square, so it is irrational too.",
  "√2 × √8 = √16 = 4, एक पूर्ण संख्या, इसलिए परिमेय। √5 अपरिमेय है; अपरिमेय √3 में 1 जोड़ने से वह अपरिमेय ही रहता है; और √3 × √5 = √15, जो पूर्ण वर्ग नहीं, इसलिए वह भी अपरिमेय है।",
  "qa-nt-the-rational-one-among-four", pos=2, check=_nt1)

def _nt2():
    n = math.isqrt(200)
    assert n * n < 200 < (n + 1) ** 2
    return f"{n} and {n + 1}"
N(QA, "Number Theory", "easy",
  "Between which two consecutive whole numbers does √200 lie?",
  "√200 किन दो क्रमागत पूर्ण संख्याओं के बीच है?",
  ["13 and 14", "14 and 15", "15 and 16", "99 and 100"], 1,
  "14² = 196 is just below 200 and 15² = 225 is above it, so √200 lies between 14 and 15 (it is about 14.14). "
  "13 and 14 and 15 and 16 are one step off either way; 99 and 100 halve 200 instead of taking its root.",
  "14² = 196, 200 से ठीक नीचे है और 15² = 225 उससे ऊपर, इसलिए √200, 14 और 15 के बीच है (लगभग 14.14)। "
  "13 और 14 तथा 15 और 16 किसी भी ओर एक कदम चूकते हैं; 99 और 100, 200 का मूल लेने के बजाय उसे आधा करते हैं।",
  "qa-nt-the-whole-numbers-either-side-of-root-200", _nt2,
  opts_hi=["13 और 14", "14 और 15", "15 और 16", "99 और 100"])

def _nt3():
    n = sum(1 for k in range(1, 50) if math.gcd(k, 50) == 1)
    assert n == 50 * (1 - F(1, 2)) * (1 - F(1, 5))
    return str(n)
N(QA, "Number Theory", "hard",
  "How many of the whole numbers from 1 to 49 have no factor in common with 50 other than 1?",
  "1 से 49 तक की कितनी पूर्ण संख्याओं का 50 के साथ 1 के अलावा कोई सार्व गुणनखंड नहीं है?",
  ["20", "25", "30", "40"], 0,
  "50 = 2 × 5², so a number shares a factor with 50 exactly when it is even or a multiple of 5. Of the 50 numbers from 1 to 50, half are even, leaving 25 odd ones, and of these the odd multiples of 5 (5, 15, 25, 35, 45) are 5 more to remove: 20 remain (50 itself is not among them). "
  "25 counts all the odd numbers; 40 removes only the multiples of 5 (49 - 9); 30 has no basis.",
  "50 = 2 × 5², इसलिए किसी संख्या का 50 से सार्व गुणनखंड ठीक तब होता है जब वह सम हो या 5 का गुणज। 1 से 50 तक की 50 संख्याओं में आधी सम हैं, जिससे 25 विषम बचती हैं, और इनमें 5 के विषम गुणज (5, 15, 25, 35, 45) 5 और हटाने हैं: 20 बचती हैं (स्वयं 50 उनमें नहीं)। "
  "25 सभी विषम संख्याएँ गिनता है; 40 केवल 5 के गुणज हटाता है (49 - 9); 30 का कोई आधार नहीं।",
  "qa-nt-numbers-below-50-co-prime-to-50", _nt3)

def _nt4():
    pairs = [(a, 36 // a) for a in range(1, 37) if 36 % a == 0 and a <= 36 // a]
    assert pairs == [(1, 36), (2, 18), (3, 12), (4, 9), (6, 6)]
    return str(len(pairs))
N(QA, "Number Theory", "medium",
  "In how many ways can 36 be written as the product of two whole numbers, if the order of the two does not matter (so that 4 × 9 and 9 × 4 count once)?",
  "36 को दो पूर्ण संख्याओं के गुणनफल के रूप में कितने तरीक़ों से लिखा जा सकता है, यदि दोनों का क्रम मायने न रखे (ताकि 4 × 9 और 9 × 4 एक बार गिने जाएँ)?",
  ["5", "8", "9", "18"], 0,
  "36 has 9 factors: 1, 2, 3, 4, 6, 9, 12, 18, 36. They pair off as 1 × 36, 2 × 18, 3 × 12 and 4 × 9, and 6 pairs with itself: 5 ways in all. "
  "9 counts the factors, not the pairs; 8 counts the four unequal pairs twice, once in each order, and leaves out 6 × 6; 18 simply halves 36.",
  "36 के 9 गुणनखंड हैं: 1, 2, 3, 4, 6, 9, 12, 18, 36। वे 1 × 36, 2 × 18, 3 × 12 और 4 × 9 के जोड़ों में बँटते हैं, और 6 स्वयं से जोड़ा बनाता है: कुल 5 तरीक़े। "
  "9 गुणनखंड गिनता है, जोड़े नहीं; 8 चार असमान जोड़ों को दोनों क्रमों में दो बार गिनता है और 6 × 6 को छोड़ देता है; 18 बस 36 को आधा करता है।",
  "qa-nt-the-factor-pairs-of-36", _nt4)

def _nt5():
    vals = [F(12, 100), F(30, 100), F(45, 100)]
    g = F(math.gcd(12, 30, 45), 100)
    assert all((v / g).denominator == 1 for v in vals)
    return str(float(g))
N(QA, "Number Theory", "medium",
  "What is the HCF of 0.12, 0.3 and 0.45?",
  "0.12, 0.3 और 0.45 का HCF क्या है?",
  ["0.03", "0.3", "0.6", "3"], 0,
  "Write them with the same number of decimal places: 0.12, 0.30 and 0.45, that is 12, 30 and 45 hundredths. The HCF of 12, 30 and 45 is 3, so the HCF of the decimals is 3 hundredths, 0.03 -- which goes into 0.12, 0.3 and 0.45 exactly 4, 10 and 15 times. "
  "3 forgets to put the decimal point back; 0.3 does not go into 0.12 or 0.45 a whole number of times; 0.6 is larger than 0.12 and 0.45.",
  "उन्हें दशमलव के बराबर स्थानों के साथ लिखिए: 0.12, 0.30 और 0.45, यानी 12, 30 और 45 सौवें भाग। 12, 30 और 45 का HCF 3 है, इसलिए दशमलवों का HCF 3 सौवें भाग, 0.03, है -- जो 0.12, 0.3 और 0.45 में ठीक 4, 10 और 15 बार जाता है। "
  "3 दशमलव बिंदु वापस लगाना भूल जाता है; 0.3, 0.12 या 0.45 में पूर्ण संख्या बार नहीं जाता; 0.6, 0.12 और 0.45 से बड़ा है।",
  "qa-nt-the-hcf-of-three-decimals", _nt5)

def _nt6():
    return str(sum(1 for n in range(-20, 21) if n * n < 50))
N(QA, "Number Theory", "medium",
  "How many integers -- positive, negative or zero -- have a square less than 50?",
  "कितने पूर्णांकों -- धनात्मक, ऋणात्मक या शून्य -- का वर्ग 50 से कम है?",
  ["7", "8", "14", "15"], 3,
  "7² = 49 < 50 but 8² = 64 is too big, so the integers are -7, -6, ..., -1, 0, 1, ..., 7: fifteen of them. "
  "7 counts only the positive ones; 14 leaves out 0, whose square, 0, is certainly less than 50; 8 counts 0 and the positive ones.",
  "7² = 49 < 50 पर 8² = 64 बहुत बड़ा है, इसलिए पूर्णांक -7, -6, ..., -1, 0, 1, ..., 7 हैं: पंद्रह। "
  "7 केवल धनात्मक गिनता है; 14, 0 को छोड़ देता है, जिसका वर्ग 0 निश्चित रूप से 50 से कम है; 8, 0 और धनात्मक गिनता है।",
  "qa-nt-integers-whose-squares-are-below-50", _nt6)

def _nt7():
    n = max(k for k in range(1, 20) if math.factorial(k) < 10 ** 6)
    assert math.factorial(9) == 362880 and math.factorial(10) == 3628800
    return str(n)
N(QA, "Number Theory", "hard",
  "What is the largest whole number n for which n! (the product 1 × 2 × ... × n) is less than 10,00,000?",
  "वह सबसे बड़ी पूर्ण संख्या n कौन-सी है जिसके लिए n! (गुणनफल 1 × 2 × ... × n) 10,00,000 से कम है?",
  ["7", "8", "9", "10"], 2,
  "Build it up: 6! = 720, 7! = 5,040, 8! = 40,320, 9! = 3,62,880 -- still below 10,00,000 -- and 10! = 36,28,800, which is above. So n = 9. "
  "10 overshoots, as 10! is more than 36 lakh; 8 and 7 stop a step or two early.",
  "बढ़ाते जाइए: 6! = 720, 7! = 5,040, 8! = 40,320, 9! = 3,62,880 -- अब भी 10,00,000 से नीचे -- और 10! = 36,28,800, जो ऊपर है। अतः n = 9। "
  "10 आगे निकल जाता है, क्योंकि 10!, 36 लाख से अधिक है; 8 और 7 एक या दो कदम पहले रुकते हैं।",
  "qa-nt-the-largest-factorial-below-ten-lakh", _nt7)

def _nt8():
    rs = {(3 * n) % 7 for n in range(3, 700, 7)}
    assert rs == {2}
    return "2"
N(QA, "Number Theory", "medium",
  "A number leaves a remainder of 3 when divided by 7. What remainder does three times the number leave when divided by 7?",
  "एक संख्या 7 से भाग देने पर शेषफल 3 छोड़ती है। उस संख्या का तिगुना 7 से भाग देने पर कितना शेषफल छोड़ता है?",
  ["2", "3", "6", "9"], 0,
  "Write the number as 7k + 3. Three times it is 21k + 9 = 7(3k + 1) + 2, so the remainder is 2 (for example, 10 leaves 3, and 30 leaves 2). "
  "9 forgets that a remainder must be less than 7; 3 assumes multiplying leaves the remainder unchanged; 6 doubles the remainder instead of tripling it.",
  "संख्या को 7k + 3 लिखिए। उसका तिगुना 21k + 9 = 7(3k + 1) + 2 है, इसलिए शेषफल 2 है (उदाहरण के लिए, 10 शेष 3 छोड़ता है, और 30 शेष 2)। "
  "9 भूल जाता है कि शेषफल 7 से कम होना चाहिए; 3 मान लेता है कि गुणा करने से शेषफल नहीं बदलता; 6 शेषफल को तिगुना करने के बजाय दोगुना करता है।",
  "qa-nt-a-remainder-when-a-number-is-tripled", _nt8)

def _nt9():
    p = 1
    for k in range(1, 100, 2):
        p *= k
    return str(p % 10)
N(QA, "Number Theory", "medium",
  "What is the last digit of the product of all the odd numbers from 1 to 99?",
  "1 से 99 तक की सभी विषम संख्याओं के गुणनफल का अंतिम अंक क्या है?",
  ["0", "1", "3", "5"], 3,
  "The product includes 5, so it is a multiple of 5, and since every factor is odd it is odd: an odd multiple of 5 always ends in 5. "
  "0 would need a factor 2, and every factor here is odd; 1 comes from looking only at the last digits 1, 3, 7 and 9 and forgetting the multiples of 5; 3 has no basis.",
  "गुणनफल में 5 शामिल है, इसलिए वह 5 का गुणज है, और चूँकि हर गुणनखंड विषम है, वह विषम है: 5 का विषम गुणज हमेशा 5 पर समाप्त होता है। "
  "0 के लिए गुणनखंड 2 चाहिए, और यहाँ हर गुणनखंड विषम है; 1 केवल अंतिम अंकों 1, 3, 7 और 9 को देखने और 5 के गुणजों को भूलने से आता है; 3 का कोई आधार नहीं।",
  "qa-nt-the-last-digit-of-the-odd-numbers-multiplied", _nt9)

def _nt10():
    x = 2 + math.sqrt(3)
    assert abs((x + 1 / x) - 4) < 1e-12
    return "4"
N(QA, "Number Theory", "hard",
  "If x = 2 + √3, what is the value of x + 1/x?",
  "यदि x = 2 + √3, तो x + 1/x का मान क्या है?",
  ["2√3", "4", "2√3 + 1", "4 + 2√3"], 1,
  "1/x = 1/(2 + √3). Multiplying top and bottom by 2 - √3 gives (2 - √3)/(4 - 3) = 2 - √3. So x + 1/x = (2 + √3) + (2 - √3) = 4. "
  "2√3 subtracts instead of adding; 4 + 2√3 adds x to itself; 2√3 + 1 has no basis. (The options are in order of size.)",
  "1/x = 1/(2 + √3)। अंश और हर को 2 - √3 से गुणा करने पर (2 - √3)/(4 - 3) = 2 - √3 मिलता है। अतः x + 1/x = (2 + √3) + (2 - √3) = 4। "
  "2√3 जोड़ने के बजाय घटाता है; 4 + 2√3, x को स्वयं में जोड़ता है; 2√3 + 1 का कोई आधार नहीं। (विकल्प आकार के क्रम में हैं।)",
  "qa-nt-a-surd-plus-its-reciprocal", _nt10)

# ---------------------------------------------------------------- Speed-Distance-Time (4)
def _sdt1():
    per_min = F(40) * F(3, 2)                       # 40 boxes a minute, 1.5 m apart
    return f"{int(per_min / 60)} m/s"
N(QA, "Speed-Distance-Time", "easy",
  "Boxes on a factory's conveyor belt are placed 1.5 m apart, and 40 of them pass a checking point every minute. How fast is the belt moving?",
  "एक कारख़ाने की कन्वेयर बेल्ट पर डिब्बे 1.5 मीटर की दूरी पर रखे हैं, और उनमें से 40 हर मिनट एक जाँच-बिंदु से गुज़रते हैं। बेल्ट कितनी तेज़ चल रही है?",
  ["0.5 m/s", "0.67 m/s", "1 m/s", "1.5 m/s"], 2,
  "Each box that passes carries 1.5 m of belt with it, so in a minute 40 × 1.5 = 60 m of belt goes by: 60 m a minute is 1 m a second. "
  "0.67 m/s divides 40 by 60 and forgets the spacing; 1.5 m/s takes the spacing as the distance moved each second; 0.5 m/s has no basis.",
  "हर गुज़रने वाला डिब्बा अपने साथ 1.5 मीटर बेल्ट ले जाता है, इसलिए एक मिनट में 40 × 1.5 = 60 मीटर बेल्ट गुज़रती है: एक मिनट में 60 मीटर यानी एक सेकंड में 1 मीटर। "
  "0.67 मीटर/सेकंड, 40 को 60 से भाग देता है और दूरी को भूल जाता है; 1.5 मीटर/सेकंड दूरी को हर सेकंड तय दूरी मान लेता है; 0.5 मीटर/सेकंड का कोई आधार नहीं।",
  "qa-sdt-boxes-on-a-conveyor-belt", _sdt1,
  opts_hi=["0.5 मीटर/सेकंड", "0.67 मीटर/सेकंड", "1 मीटर/सेकंड", "1.5 मीटर/सेकंड"])

def _sdt2():
    asha = 8 + F(12, 3)
    bina = 9 + F(12, 4)
    assert asha == bina == 12
    return "They arrive at the same time."
T(QA, "Speed-Distance-Time", "medium",
  "Asha and Bina both walk the same 12 km route. Asha walks at 3 km/h and sets off at 8:00 a.m.; Bina walks at 4 km/h and sets off an hour later, at 9:00 a.m. Who arrives first?",
  "आशा और बीना दोनों एक ही 12 किमी का रास्ता चलती हैं। आशा 3 किमी/घंटा से चलती है और सुबह 8:00 बजे निकलती है; बीना 4 किमी/घंटा से चलती है और एक घंटा बाद, सुबह 9:00 बजे, निकलती है। पहले कौन पहुँचती है?",
  ["They arrive at the same time.", "Asha arrives first, by a whole hour.", "Bina arrives first, by half an hour.", "Bina arrives first, by a whole hour."],
  ["दोनों एक ही समय पहुँचती हैं।", "आशा पूरे एक घंटे पहले पहुँचती है।", "बीना आधा घंटा पहले पहुँचती है।", "बीना पूरे एक घंटे पहले पहुँचती है।"],
  0,
  "Asha takes 12 ÷ 3 = 4 hours and arrives at 12:00 noon. Bina takes 12 ÷ 4 = 3 hours, and starting at 9:00 she too arrives at 12:00 noon. They arrive together. "
  "Bina an hour early forgets her late start; Asha an hour early counts the late start but not Bina's faster pace; Bina half an hour early has no basis.",
  "आशा को 12 ÷ 3 = 4 घंटे लगते हैं और वह दोपहर 12:00 बजे पहुँचती है। बीना को 12 ÷ 4 = 3 घंटे लगते हैं, और 9:00 बजे चलकर वह भी दोपहर 12:00 बजे पहुँचती है। दोनों साथ पहुँचती हैं। "
  "बीना का एक घंटा पहले पहुँचना उसकी देर से शुरुआत भूल जाता है; आशा का एक घंटा पहले पहुँचना देर से शुरुआत गिनता है पर बीना की तेज़ चाल नहीं; बीना के आधा घंटा पहले पहुँचने का कोई आधार नहीं।",
  "qa-sdt-a-late-start-that-ends-in-a-tie", pos=0, check=_sdt2)

def _sdt3():
    circ = F(22, 7) * F(70, 100)                  # metres per turn
    kmh = circ * 200 * 60 / 1000
    return f"{float(kmh)} km/h"
N(QA, "Speed-Distance-Time", "medium",
  "A bicycle wheel 70 cm across turns 200 times a minute. How fast is the bicycle going? (Take π = 22/7.)",
  "एक साइकिल का 70 सेमी व्यास का पहिया एक मिनट में 200 बार घूमता है। साइकिल कितनी तेज़ चल रही है? (π = 22/7 लीजिए।)",
  ["13.2 km/h", "26.4 km/h", "44 km/h", "52.8 km/h"], 1,
  "Each turn carries the bicycle one circumference, π × 70 cm = 220 cm = 2.2 m. 200 turns a minute is 440 m a minute, and 440 × 60 = 26,400 m an hour: 26.4 km/h. "
  "13.2 km/h uses π × 35 cm, half the circumference; 52.8 km/h takes 70 cm as the radius; 44 km/h has no basis.",
  "हर चक्कर साइकिल को एक परिधि, π × 70 सेमी = 220 सेमी = 2.2 मीटर, आगे ले जाता है। एक मिनट में 200 चक्कर यानी एक मिनट में 440 मीटर, और 440 × 60 = 26,400 मीटर प्रति घंटा: 26.4 किमी/घंटा। "
  "13.2 किमी/घंटा π × 35 सेमी, आधी परिधि, लेता है; 52.8 किमी/घंटा 70 सेमी को त्रिज्या मानता है; 44 किमी/घंटा का कोई आधार नहीं।",
  "qa-sdt-a-wheel-s-turns-per-minute", _sdt3,
  opts_hi=["13.2 किमी/घंटा", "26.4 किमी/घंटा", "44 किमी/घंटा", "52.8 किमी/घंटा"])

def _sdt4():
    k = next(x for x in range(1, 100) if 4 * x == 3 * x + 15)
    return f"{4 * k} km/h"
N(QA, "Speed-Distance-Time", "medium",
  "The speeds of a car and a bus are in the ratio 4 : 3. If the bus went 15 km/h faster, the two would travel at the same speed. What is the car's speed?",
  "एक कार और एक बस की चालें 4 : 3 के अनुपात में हैं। यदि बस 15 किमी/घंटा तेज़ चलती, तो दोनों एक ही चाल से चलते। कार की चाल क्या है?",
  ["15 km/h", "30 km/h", "45 km/h", "60 km/h"], 3,
  "Let the speeds be 4k and 3k. The extra 15 km/h closes the gap of one part, so k = 15: the car goes at 4 × 15 = 60 km/h and the bus at 45 km/h. "
  "45 km/h is the bus's speed; 15 km/h is the size of one part; 30 km/h has no basis.",
  "चालें 4k और 3k मानिए। अतिरिक्त 15 किमी/घंटा एक भाग का अंतर पाट देता है, इसलिए k = 15: कार 4 × 15 = 60 किमी/घंटा से और बस 45 किमी/घंटा से चलती है। "
  "45 किमी/घंटा बस की चाल है; 15 किमी/घंटा एक भाग का आकार है; 30 किमी/घंटा का कोई आधार नहीं।",
  "qa-sdt-speeds-whose-ratio-changes", _sdt4,
  opts_hi=["15 किमी/घंटा", "30 किमी/घंटा", "45 किमी/घंटा", "60 किमी/घंटा"])

# ---------------------------------------------------------------- Ratio, Mixtures & Alligation (5)
def _rm1():
    below = 50 - 11
    return f"{int(F(below, 50) * 100)} per cent"
N(QA, "Ratio, Mixtures & Alligation", "easy",
  "In a class of 50 students with no two scores equal, a student ranks 11th from the top. What percentage of the class scored less than this student?",
  "50 विद्यार्थियों की एक कक्षा में, जहाँ कोई दो अंक बराबर नहीं, एक विद्यार्थी ऊपर से 11वें स्थान पर है। कक्षा के कितने प्रतिशत विद्यार्थियों ने इस विद्यार्थी से कम अंक पाए?",
  ["22 per cent", "39 per cent", "78 per cent", "80 per cent"], 2,
  "Ten students are above the student, so 50 - 11 = 39 are below, which is 39/50 = 78 per cent of the class. "
  "39 is the number below, not the percentage; 80 per cent counts the student among those below; 22 per cent is the share at or above the student.",
  "दस विद्यार्थी उससे ऊपर हैं, इसलिए 50 - 11 = 39 नीचे हैं, जो कक्षा का 39/50 = 78 प्रतिशत है। "
  "39 नीचे वालों की संख्या है, प्रतिशत नहीं; 80 प्रतिशत उस विद्यार्थी को भी नीचे वालों में गिनता है; 22 प्रतिशत उसके बराबर या ऊपर वालों का भाग है।",
  "qa-rm-a-percentile-from-a-rank", _rm1,
  opts_hi=["22 प्रतिशत", "39 प्रतिशत", "78 प्रतिशत", "80 प्रतिशत"])

def _rm2():
    d = F(30 * 2, 40)
    return f"{float(d)} m"
N(QA, "Ratio, Mixtures & Alligation", "easy",
  "A child weighing 30 kg sits 2 m from the centre of a see-saw. How far from the centre, on the other side, must a child weighing 40 kg sit for the see-saw to balance?",
  "30 किग्रा भार का एक बच्चा एक सी-सॉ के केंद्र से 2 मीटर दूर बैठा है। सी-सॉ के संतुलित होने के लिए 40 किग्रा भार के बच्चे को दूसरी ओर केंद्र से कितनी दूर बैठना होगा?",
  ["1.5 m", "2 m", "2.5 m", "2.67 m"], 0,
  "A see-saw balances when weight times distance is the same on both sides: 30 × 2 = 40 × d, so d = 60 ÷ 40 = 1.5 m. The heavier child sits nearer the centre. "
  "2 m ignores the difference in weight; 2.67 m (2 × 40/30) puts the heavier child farther out, the wrong way round; 2.5 m has no basis.",
  "सी-सॉ तब संतुलित होता है जब दोनों ओर भार गुणा दूरी बराबर हो: 30 × 2 = 40 × d, इसलिए d = 60 ÷ 40 = 1.5 मीटर। भारी बच्चा केंद्र के निकट बैठता है। "
  "2 मीटर भार के अंतर को अनदेखा करता है; 2.67 मीटर (2 × 40/30) भारी बच्चे को और दूर, उलटी ओर, रखता है; 2.5 मीटर का कोई आधार नहीं।",
  "qa-rm-a-see-saw-balanced", _rm2,
  opts_hi=["1.5 मीटर", "2 मीटर", "2.5 मीटर", "2.67 मीटर"])

def _rm3():
    k = F(6) * 2 / 4
    return str(int(k * 12 / 3))
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "x varies directly as y and inversely as z, and x = 6 when y = 4 and z = 2. What is x when y = 12 and z = 3?",
  "x, y के अनुक्रमानुपाती और z के व्युत्क्रमानुपाती है, और y = 4 तथा z = 2 होने पर x = 6 है। y = 12 और z = 3 होने पर x क्या है?",
  ["4", "6", "8", "12"], 3,
  "x = k × y/z, and 6 = k × 4/2 gives k = 3. Then x = 3 × 12/3 = 12. "
  "6 leaves x unchanged; 4 multiplies by y/z without the constant 3 (12/3); 8 has no basis.",
  "x = k × y/z, और 6 = k × 4/2 से k = 3 मिलता है। तब x = 3 × 12/3 = 12। "
  "6, x को अपरिवर्तित छोड़ता है; 4, अचर 3 के बिना y/z (12/3) लेता है; 8 का कोई आधार नहीं।",
  "qa-rm-a-quantity-varying-with-two-others", _rm3)

def _rm4():
    carat = F(10 * 22 + 20 * 18, 30)
    assert carat == F(58, 3)
    return "19⅓ carat"
N(QA, "Ratio, Mixtures & Alligation", "hard",
  "Pure gold is called 24 carat, so 18-carat gold is 18/24 pure. A goldsmith melts 10 g of 22-carat gold with 20 g of 18-carat gold. What is the carat of the mixture?",
  "शुद्ध सोना 24 कैरेट कहलाता है, इसलिए 18 कैरेट सोना 18/24 शुद्ध है। एक सुनार 10 ग्राम 22 कैरेट सोने को 20 ग्राम 18 कैरेट सोने के साथ पिघलाता है। मिश्रण कितने कैरेट का है?",
  ["19⅓ carat", "20 carat", "20⅔ carat", "21 carat"], 0,
  "Carats are a measure of purity, so they average by weight: (10 × 22 + 20 × 18) ÷ 30 = (220 + 360) ÷ 30 = 580 ÷ 30 = 19⅓ carat. "
  "20 carat takes the plain average of 22 and 18, ignoring that there is twice as much of the 18-carat gold; 20⅔ carat swaps the weights; 21 carat has no basis.",
  "कैरेट शुद्धता का माप हैं, इसलिए उनका औसत भार से लिया जाता है: (10 × 22 + 20 × 18) ÷ 30 = (220 + 360) ÷ 30 = 580 ÷ 30 = 19⅓ कैरेट। "
  "20 कैरेट 22 और 18 का सीधा औसत लेता है, यह अनदेखा करते हुए कि 18 कैरेट सोना दोगुना है; 20⅔ कैरेट भारों को उलट देता है; 21 कैरेट का कोई आधार नहीं।",
  "qa-rm-gold-mixed-by-carats", _rm4,
  opts_hi=["19⅓ कैरेट", "20 कैरेट", "20⅔ कैरेट", "21 कैरेट"])

def _rm5():
    r = (F(3, 4)) ** 2
    return f"{r.numerator} : {r.denominator}"
N(QA, "Ratio, Mixtures & Alligation", "medium",
  "The circumferences of two circles are in the ratio 3 : 4. What is the ratio of their areas?",
  "दो वृत्तों की परिधियाँ 3 : 4 के अनुपात में हैं। उनके क्षेत्रफलों का अनुपात क्या है?",
  ["9 : 16", "3 : 4", "4 : 3", "16 : 9"], 0,
  "A circle's circumference is in proportion to its radius, so the radii are also in the ratio 3 : 4. Area goes with the square of the radius, so the areas are in the ratio 3² : 4² = 9 : 16. "
  "3 : 4 treats area like circumference; 16 : 9 and 4 : 3 turn the ratio round. (The options are in order of size.)",
  "वृत्त की परिधि उसकी त्रिज्या के अनुपात में होती है, इसलिए त्रिज्याएँ भी 3 : 4 के अनुपात में हैं। क्षेत्रफल त्रिज्या के वर्ग के साथ चलता है, इसलिए क्षेत्रफल 3² : 4² = 9 : 16 के अनुपात में हैं। "
  "3 : 4 क्षेत्रफल को परिधि की तरह मानता है; 16 : 9 और 4 : 3 अनुपात को उलट देते हैं। (विकल्प आकार के क्रम में हैं।)",
  "qa-rm-the-areas-of-two-circles-from-their-rims", _rm5)

# ---------------------------------------------------------------- Percentage & Profit-Loss (3)
def _pp1():
    g = next(x for x in range(30, 200) if 300 + 20 * (x - 30) > 500)
    assert g == 41
    return "40 GB"
N(QA, "Percentage & Profit-Loss", "medium",
  "Plan X costs ₹300 a month for the first 30 GB of data and ₹20 for each further GB. Plan Y costs ₹500 a month for unlimited data. Above what monthly use does Plan Y become cheaper?",
  "प्लान X में पहले 30 GB डेटा के लिए ₹300 प्रति माह और हर अतिरिक्त GB के लिए ₹20 लगते हैं। प्लान Y में असीमित डेटा के लिए ₹500 प्रति माह लगते हैं। किस मासिक उपयोग से ऊपर प्लान Y सस्ता हो जाता है?",
  ["10 GB", "25 GB", "40 GB", "50 GB"], 2,
  "Plan X costs ₹500 when the extra data costs ₹200, that is 10 GB beyond the first 30: at 40 GB both plans cost ₹500, and above 40 GB Plan Y is cheaper. "
  "10 GB is the extra data alone, forgetting the 30 GB already included; 25 GB divides ₹500 by ₹20; 50 GB has no basis.",
  "प्लान X का ख़र्च ₹500 तब होता है जब अतिरिक्त डेटा का ख़र्च ₹200 हो, यानी पहले 30 के बाद 10 GB: 40 GB पर दोनों प्लान ₹500 के हैं, और 40 GB से ऊपर प्लान Y सस्ता है। "
  "10 GB केवल अतिरिक्त डेटा है, पहले से शामिल 30 GB को भूलकर; 25 GB, ₹500 को ₹20 से भाग देता है; 50 GB का कोई आधार नहीं।",
  "qa-pp-a-plan-that-is-cheaper-only-past-a-point", _pp1)

def _pp2():
    claim, excess = 25000, 5000
    return f"₹{indian(int((claim - excess) * F(8, 10)))}"
N(QA, "Percentage & Profit-Loss", "medium",
  "A health insurance policy pays 80 per cent of the part of any claim that is above ₹5,000. How much does it pay on a claim of ₹25,000?",
  "एक स्वास्थ्य बीमा पॉलिसी किसी भी दावे के ₹5,000 से ऊपर वाले भाग का 80 प्रतिशत चुकाती है। ₹25,000 के दावे पर वह कितना चुकाती है?",
  ["₹4,000", "₹12,000", "₹15,000", "₹16,000"], 3,
  "The part above ₹5,000 is ₹20,000, and 80 per cent of that is ₹16,000. "
  "₹15,000 takes 80 per cent of the whole claim (₹20,000) and then removes ₹5,000 again; ₹4,000 is the 20 per cent of the ₹20,000 that the policy does not pay; ₹12,000 has no basis.",
  "₹5,000 से ऊपर का भाग ₹20,000 है, और उसका 80 प्रतिशत ₹16,000 है। "
  "₹15,000 पूरे दावे का 80 प्रतिशत (₹20,000) लेकर फिर ₹5,000 घटाता है; ₹4,000, ₹20,000 का वह 20 प्रतिशत है जो पॉलिसी नहीं चुकाती; ₹12,000 का कोई आधार नहीं।",
  "qa-pp-an-insurance-payout-above-an-excess", _pp2)

def _pp3():
    v, years = F(1), 0
    while v >= F(1, 2):
        v *= F(9, 10); years += 1
    assert years == 7
    return str(years)
N(QA, "Percentage & Profit-Loss", "hard",
  "A machine loses 10 per cent of its value every year, each year's loss worked out on its value at the start of that year. After how many whole years is it first worth less than half its price when new?",
  "एक मशीन हर वर्ष अपने मूल्य का 10 प्रतिशत खोती है, हर वर्ष की हानि उस वर्ष की शुरुआत के मूल्य पर निकाली जाती है। कितने पूरे वर्षों बाद वह पहली बार अपने नए मूल्य के आधे से कम की रह जाती है?",
  ["5", "6", "7", "10"], 2,
  "Each year leaves 0.9 of the value: after 5 years 0.59, after 6 years 0.53, after 7 years 0.48. So it first falls below half after 7 years. "
  "5 years treats the loss as 10 per cent of the new price every year (5 × 10 per cent = 50 per cent); 10 years would wipe out the value altogether on that same mistake; 6 years still leaves 53 per cent.",
  "हर वर्ष मूल्य का 0.9 बचता है: 5 वर्ष बाद 0.59, 6 वर्ष बाद 0.53, 7 वर्ष बाद 0.48। अतः वह पहली बार 7 वर्ष बाद आधे से नीचे जाती है। "
  "5 वर्ष हानि को हर वर्ष नए मूल्य का 10 प्रतिशत मानता है (5 × 10 प्रतिशत = 50 प्रतिशत); उसी भूल से 10 वर्ष पूरा मूल्य मिटा देते; 6 वर्ष बाद अभी 53 प्रतिशत बचता है।",
  "qa-pp-the-years-for-a-machine-to-lose-half-its-value", _pp3)

# ---------------------------------------------------------------- Sequences & Series (2)
def _ss1():
    sols = [(5 - d, 5, 5 + d) for d in range(0, 10) if (5 - d) * 5 * (5 + d) == 80]
    assert sols == [(2, 5, 8)]
    return "8"
N(QA, "Sequences & Series", "hard",
  "Three numbers in arithmetic progression add up to 15, and their product is 80. What is the largest of them?",
  "समांतर श्रेणी में तीन संख्याओं का योग 15 है, और उनका गुणनफल 80 है। उनमें सबसे बड़ी कौन-सी है?",
  ["2", "5", "8", "11"], 2,
  "Write the numbers as 5 - d, 5 and 5 + d, since three numbers in AP adding to 15 have 5 in the middle. Their product is 5(25 - d²) = 80, so 25 - d² = 16 and d = 3: the numbers are 2, 5 and 8. The largest is 8. "
  "5 is the middle number; 2 is the smallest; 11 adds the difference twice.",
  "संख्याओं को 5 - d, 5 और 5 + d लिखिए, क्योंकि 15 योग वाली समांतर श्रेणी की तीन संख्याओं के बीच में 5 होता है। उनका गुणनफल 5(25 - d²) = 80 है, इसलिए 25 - d² = 16 और d = 3: संख्याएँ 2, 5 और 8 हैं। सबसे बड़ी 8 है। "
  "5 बीच की संख्या है; 2 सबसे छोटी; 11 अंतर को दो बार जोड़ता है।",
  "qa-ss-three-numbers-in-ap-from-their-sum-and-product", _ss1)

def _ss2():
    sols = [(a, d) for a in range(1, 50) for d in range(1, 50) if a + 4 * d == 3 * a and a + 9 * d == 44]
    assert sols == [(8, 4)]
    return "8"
N(QA, "Sequences & Series", "medium",
  "In an arithmetic progression, the 5th term is three times the 1st term, and the 10th term is 44. What is the 1st term?",
  "एक समांतर श्रेणी में 5वाँ पद पहले पद का तीन गुना है, और 10वाँ पद 44 है। पहला पद क्या है?",
  ["4", "8", "12", "16"], 1,
  "With first term a and common difference d, a + 4d = 3a gives a = 2d, and a + 9d = 44 then gives 11d = 44, so d = 4 and a = 8. Check: the 5th term is 8 + 16 = 24 = 3 × 8. "
  "4 is the common difference; 12 and 16 are the 2nd and 3rd terms.",
  "पहला पद a और सार्व अंतर d लेने पर a + 4d = 3a से a = 2d मिलता है, और फिर a + 9d = 44 से 11d = 44, इसलिए d = 4 और a = 8। जाँच: 5वाँ पद 8 + 16 = 24 = 3 × 8। "
  "4 सार्व अंतर है; 12 और 16 दूसरा और तीसरा पद हैं।",
  "qa-ss-an-ap-whose-fifth-term-is-three-times-its-first", _ss2)

# ---------------------------------------------------------------- Permutation & Combination (3)
def _pc1():
    fams = list(product("BG", repeat=2))                       # older child, younger child, equally likely
    some_girl = [f for f in fams if "G" in f]
    p = F(sum(1 for f in some_girl if f == ("G", "G")), len(some_girl))
    return f"{p.numerator}/{p.denominator}"
N(QA, "Permutation & Combination", "hard",
  "A family has two children, and it is known that at least one of them is a girl. If each child is equally likely to be a boy or a girl, what is the probability that both are girls?",
  "एक परिवार में दो बच्चे हैं, और यह ज्ञात है कि उनमें से कम से कम एक लड़की है। यदि हर बच्चे के लड़का या लड़की होने की संभावना बराबर हो, तो दोनों के लड़कियाँ होने की प्रायिकता क्या है?",
  ["1/4", "1/3", "1/2", "2/3"], 1,
  "Two children can be, in order of birth, boy-boy, boy-girl, girl-boy or girl-girl, all equally likely. 'At least one girl' rules out only boy-boy, leaving three cases, of which one is girl-girl: 1/3. "
  "1/2 treats the other child as a separate coin toss, but we are not told which child is the girl; 1/4 ignores the information given; 2/3 is the chance that the family has one boy and one girl.",
  "दो बच्चे, जन्म के क्रम में, लड़का-लड़का, लड़का-लड़की, लड़की-लड़का या लड़की-लड़की हो सकते हैं, सब समान संभावित। 'कम से कम एक लड़की' केवल लड़का-लड़का को ख़ारिज करता है, जिससे तीन स्थितियाँ बचती हैं, जिनमें एक लड़की-लड़की है: 1/3। "
  "1/2 दूसरे बच्चे को एक अलग सिक्का-उछाल मानता है, पर यह नहीं बताया गया कि कौन-सा बच्चा लड़की है; 1/4 दी गई जानकारी को अनदेखा करता है; 2/3 परिवार में एक लड़का और एक लड़की होने की संभावना है।",
  "qa-pc-two-girls-given-at-least-one", _pc1)

def _pc2():
    return str(sum(1 for t in combinations(range(8), 3) if 0 in t and 1 in t))
N(QA, "Permutation & Combination", "easy",
  "In how many ways can 3 books be chosen from 8 different books if 2 particular books must always be among those chosen?",
  "8 अलग-अलग पुस्तकों में से 3 पुस्तकें कितने तरीक़ों से चुनी जा सकती हैं, यदि 2 विशेष पुस्तकें चुनी गई पुस्तकों में हमेशा हों?",
  ["3", "6", "20", "56"], 1,
  "With the 2 particular books already in, only the third book is left to choose, from the other 6: 6 ways. "
  "56 = 8C3 ignores the condition; 20 = 6C3 chooses all three from the other six; 3 has no basis.",
  "2 विशेष पुस्तकें पहले से शामिल होने पर केवल तीसरी पुस्तक चुननी है, बाक़ी 6 में से: 6 तरीक़े। "
  "56 = 8C3 शर्त को अनदेखा करता है; 20 = 6C3 तीनों को बाक़ी छह में से चुनता है; 3 का कोई आधार नहीं।",
  "qa-pc-books-chosen-with-two-fixed", _pc2)

def _pc3():
    return str(sum(1 for p in permutations("12345", 3) if int(p[2]) % 2 == 0))
N(QA, "Permutation & Combination", "medium",
  "How many even three-digit numbers can be formed from the digits 1, 2, 3, 4 and 5, using no digit more than once in a number?",
  "अंकों 1, 2, 3, 4 और 5 से, किसी संख्या में किसी अंक को एक से अधिक बार प्रयोग किए बिना, तीन अंकों की कितनी सम संख्याएँ बनाई जा सकती हैं?",
  ["6", "12", "18", "24"], 3,
  "An even number must end in 2 or 4: 2 choices for the last digit. The first digit can then be any of the 4 digits left, and the middle digit any of the remaining 3: 2 × 4 × 3 = 24. "
  "12 allows only numbers ending in 2; 6 and 18 have no basis.",
  "सम संख्या 2 या 4 पर समाप्त होनी चाहिए: अंतिम अंक के 2 विकल्प। तब पहला अंक बचे 4 अंकों में से कोई भी हो सकता है, और बीच का अंक शेष 3 में से कोई भी: 2 × 4 × 3 = 24। "
  "12 केवल 2 पर समाप्त होने वाली संख्याएँ गिनता है; 6 और 18 का कोई आधार नहीं।",
  "qa-pc-even-three-digit-numbers-from-five-digits", _pc3)

# ---------------------------------------------------------------- Geometry & Mensuration (2)
def _gm1():
    return f"₹{indian(25 * 16 * 50)}"
N(QA, "Geometry & Mensuration", "easy",
  "A rectangular plot 25 m long and 16 m wide is to be covered with turf costing ₹50 a square metre. What will the turf cost?",
  "25 मीटर लंबे और 16 मीटर चौड़े एक आयताकार भूखंड पर ₹50 प्रति वर्ग मीटर की घास की परत (टर्फ़) बिछानी है। टर्फ़ पर कितना ख़र्च होगा?",
  ["₹2,050", "₹4,100", "₹20,000", "₹40,000"], 2,
  "The plot's area is 25 × 16 = 400 square metres, and 400 × ₹50 = ₹20,000. "
  "₹4,100 prices the perimeter (82 m) instead of the area; ₹2,050 prices half the perimeter; ₹40,000 doubles the area.",
  "भूखंड का क्षेत्रफल 25 × 16 = 400 वर्ग मीटर है, और 400 × ₹50 = ₹20,000। "
  "₹4,100 क्षेत्रफल के बजाय परिमाप (82 मीटर) का मूल्य लगाता है; ₹2,050 आधे परिमाप का; ₹40,000 क्षेत्रफल को दोगुना करता है।",
  "qa-gm-turfing-a-plot", _gm1)

def _gm2():
    cm3 = F(2, 3) * F(22, 7) * 21 ** 3
    assert cm3 == 19404
    return f"{float(cm3 / 1000)} litres"
N(QA, "Geometry & Mensuration", "medium",
  "A bowl is in the shape of a hemisphere with an inner radius of 21 cm. How many litres does it hold when full? (Take π = 22/7.)",
  "एक कटोरा 21 सेमी भीतरी त्रिज्या वाले अर्धगोले के आकार का है। भरा होने पर उसमें कितने लीटर आते हैं? (π = 22/7 लीजिए।)",
  ["9.702 litres", "19.404 litres", "38.808 litres", "58.212 litres"], 1,
  "A hemisphere holds half of a sphere: ½ × 4/3 × πr³ = 2/3 × 22/7 × 21 × 21 × 21 = 19,404 cubic centimetres. A litre is 1,000 cubic centimetres, so the bowl holds 19.404 litres. "
  "38.808 litres is the whole sphere; 9.702 litres halves the hemisphere again; 58.212 litres has no basis.",
  "अर्धगोला एक गोले का आधा रखता है: ½ × 4/3 × πr³ = 2/3 × 22/7 × 21 × 21 × 21 = 19,404 घन सेमी। एक लीटर 1,000 घन सेमी है, इसलिए कटोरे में 19.404 लीटर आते हैं। "
  "38.808 लीटर पूरा गोला है; 9.702 लीटर अर्धगोले को फिर आधा करता है; 58.212 लीटर का कोई आधार नहीं।",
  "qa-gm-the-litres-in-a-hemispherical-bowl", _gm2,
  opts_hi=["9.702 लीटर", "19.404 लीटर", "38.808 लीटर", "58.212 लीटर"])

# ---------------------------------------------------------------- Time & Work (2)
def _tw1():
    return f"{int(F(2 * 6, 3))} days"
N(QA, "Time & Work", "easy",
  "Two oxen plough a field in 6 days. Working at the same rate, how long would 3 oxen take to plough it?",
  "दो बैल एक खेत को 6 दिनों में जोतते हैं। उसी दर से काम करते हुए 3 बैल उसे जोतने में कितना समय लेंगे?",
  ["3 days", "4 days", "9 days", "12 days"], 1,
  "The field needs 2 × 6 = 12 ox-days of work, so 3 oxen take 12 ÷ 3 = 4 days. "
  "9 days treats more oxen as taking longer (6 × 3/2); 12 days counts the ox-days themselves; 3 days has no basis.",
  "खेत के लिए 2 × 6 = 12 बैल-दिन का काम चाहिए, इसलिए 3 बैल 12 ÷ 3 = 4 दिन लेते हैं। "
  "9 दिन अधिक बैलों को अधिक समय लेने वाला मानता है (6 × 3/2); 12 दिन स्वयं बैल-दिन गिनता है; 3 दिन का कोई आधार नहीं।",
  "qa-tw-ploughing-with-more-oxen", _tw1,
  opts_hi=["3 दिन", "4 दिन", "9 दिन", "12 दिन"])

def _tw2():
    filled = sum(F(1, 2 ** k) for k in range(1, 60))
    assert filled < 1
    return "It never quite fills the tank."
T(QA, "Time & Work", "hard",
  "A tap fills half of an empty tank in its first hour. In each later hour its flow is half what it was the hour before, so it adds half as much water. How long does it take to fill the tank?",
  "एक नल पहले घंटे में एक ख़ाली टंकी का आधा भाग भरता है। हर अगले घंटे में उसका बहाव पिछले घंटे का आधा रह जाता है, इसलिए वह आधा पानी जोड़ता है। टंकी भरने में कितना समय लगता है?",
  ["It never quite fills the tank.", "It fills the tank in exactly 2 hours.", "It fills the tank in about 4 hours.", "It fills the tank in about 8 hours."],
  ["वह टंकी को कभी पूरा नहीं भर पाता।", "वह टंकी को ठीक 2 घंटे में भर देता है।", "वह टंकी को लगभग 4 घंटे में भर देता है।", "वह टंकी को लगभग 8 घंटे में भर देता है।"],
  0,
  "After one hour the tank is 1/2 full, after two hours 3/4, after three 7/8, and so on: each hour fills half of what is still empty. The empty part halves every hour but never reaches zero, so the tank never quite fills. "
  "2 hours assumes the second hour adds another half; 4 and 8 hours stop at a point where a sixteenth or a 256th is still empty.",
  "एक घंटे बाद टंकी 1/2 भरी है, दो घंटे बाद 3/4, तीन के बाद 7/8, और इसी तरह: हर घंटा अभी ख़ाली भाग का आधा भरता है। ख़ाली भाग हर घंटे आधा होता है पर कभी शून्य नहीं होता, इसलिए टंकी कभी पूरी नहीं भरती। "
  "2 घंटे मान लेता है कि दूसरा घंटा एक और आधा जोड़ता है; 4 और 8 घंटे ऐसे बिंदु पर रुकते हैं जहाँ अभी सोलहवाँ या 256वाँ भाग ख़ाली है।",
  "qa-tw-a-tap-whose-flow-halves-every-hour", pos=3, check=_tw2)

# ---------------------------------------------------------------- Puzzle Hybrid (5)
def _ph1():
    goats = next(g for g in range(0, 31) if 4 * g + 2 * (30 - g) == 100)
    return str(goats)
N(QA, "Puzzle Hybrid", "easy",
  "A farmyard has only hens and goats. Together they have 30 heads and 100 legs. How many goats are there?",
  "एक बाड़े में केवल मुर्गियाँ और बकरियाँ हैं। सबके मिलाकर 30 सिर और 100 पैर हैं। कितनी बकरियाँ हैं?",
  ["10", "15", "20", "25"], 2,
  "If all 30 were hens there would be 60 legs. Each goat adds 2 legs more than a hen, and there are 40 legs too many, so there are 40 ÷ 2 = 20 goats (and 10 hens): 80 + 20 = 100 legs. "
  "10 is the number of hens; 25 divides 100 by 4, as if every animal were a goat; 15 splits the heads evenly.",
  "यदि सभी 30 मुर्गियाँ होतीं तो 60 पैर होते। हर बकरी मुर्गी से 2 पैर अधिक जोड़ती है, और 40 पैर अधिक हैं, इसलिए 40 ÷ 2 = 20 बकरियाँ हैं (और 10 मुर्गियाँ): 80 + 20 = 100 पैर। "
  "10 मुर्गियों की संख्या है; 25, 100 को 4 से भाग देता है, मानो हर पशु बकरी हो; 15 सिरों को बराबर बाँटता है।",
  "qa-ph-heads-and-legs", _ph1)

def _ph2():
    n, steps = 6, 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
    return str(steps)
N(QA, "Puzzle Hybrid", "medium",
  "Start with 6. At each step, if the number is even, halve it; if it is odd, multiply it by 3 and add 1. How many steps does it take to reach 1?",
  "6 से शुरू कीजिए। हर चरण में, यदि संख्या सम हो तो उसे आधा कीजिए; यदि विषम हो तो उसे 3 से गुणा करके 1 जोड़िए। 1 तक पहुँचने में कितने चरण लगते हैं?",
  ["5", "8", "9", "16"], 1,
  "6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1: 8 steps. "
  "9 counts the numbers in the chain, including the 6 you start with, rather than the steps between them; 16 is the largest number reached; 5 has no basis.",
  "6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1: 8 चरण। "
  "9 चरणों के बजाय शृंखला की संख्याएँ गिनता है, शुरुआती 6 सहित; 16 पहुँची गई सबसे बड़ी संख्या है; 5 का कोई आधार नहीं।",
  "qa-ph-the-steps-from-6-to-1", _ph2)

def _ph3():
    d, n = dt.date(2027, 1, 1), 0
    while d.year == 2027:
        if d.day * d.month == 27:
            n += 1
        d += dt.timedelta(days=1)
    return str(n)
N(QA, "Puzzle Hybrid", "hard",
  "On how many dates in 2027 does the day of the month multiplied by the number of the month give 27, the last two digits of the year (as on 9 March, 9 × 3 = 27)?",
  "2027 की कितनी तारीख़ों पर महीने की तारीख़ को महीने की संख्या से गुणा करने पर 27 मिलता है, जो वर्ष के अंतिम दो अंक हैं (जैसे 9 मार्च को, 9 × 3 = 27)?",
  ["0", "1", "2", "3"], 3,
  "27 = 1 × 27 = 3 × 9 = 9 × 3 = 27 × 1. The month must be 1 to 12, so the pairs that work are day 27 of month 1 (27 January), day 9 of month 3 (9 March) and day 3 of month 9 (3 September); day 1 of a 27th month does not exist. That is 3 dates. "
  "2 misses one of the three -- usually 27 January; 1 counts only the example; 0 has no basis.",
  "27 = 1 × 27 = 3 × 9 = 9 × 3 = 27 × 1। महीना 1 से 12 तक होना चाहिए, इसलिए चलने वाले जोड़े हैं महीने 1 की 27 तारीख़ (27 जनवरी), महीने 3 की 9 तारीख़ (9 मार्च) और महीने 9 की 3 तारीख़ (3 सितंबर); 27वें महीने की 1 तारीख़ होती ही नहीं। यानी 3 तारीख़ें। "
  "2 तीन में से एक छोड़ देता है -- प्रायः 27 जनवरी; 1 केवल उदाहरण गिनता है; 0 का कोई आधार नहीं।",
  "qa-ph-dates-whose-day-times-month-is-27", _ph3)

def _ph4():
    rise_of_water, rise_of_ship = F(12, 10), F(12, 10)       # the ship floats, so it rises with the tide
    under = (rise_of_water - rise_of_ship) / F(3, 10)
    assert under == 0
    return "None"
T(QA, "Puzzle Hybrid", "medium",
  "A rope ladder hangs over the side of a ship at anchor, with its lowest rung just touching the water and the rungs 30 cm apart. The tide then rises by 1.2 m. How many rungs are now under water?",
  "लंगर डाले एक जहाज़ के किनारे पर एक रस्सी की सीढ़ी लटक रही है, जिसका सबसे निचला डंडा ठीक पानी को छू रहा है और डंडे 30 सेमी की दूरी पर हैं। फिर ज्वार 1.2 मीटर ऊपर उठता है। अब कितने डंडे पानी के नीचे हैं?",
  ["None", "Three", "Four", "Five"], ["कोई नहीं", "तीन", "चार", "पाँच"],
  0,
  "The ship floats, so it rises with the tide, and the ladder hanging from it rises too. The lowest rung still just touches the water, and no rung goes under. "
  "Four divides 1.2 m by 30 cm as if the ladder were fixed to the shore; five also counts the rung that was touching to begin with; three has no basis.",
  "जहाज़ तैरता है, इसलिए वह ज्वार के साथ ऊपर उठता है, और उससे लटकी सीढ़ी भी उठती है। सबसे निचला डंडा अब भी ठीक पानी को छूता है, और कोई डंडा नीचे नहीं जाता। "
  "चार, 1.2 मीटर को 30 सेमी से भाग देता है मानो सीढ़ी किनारे से बँधी हो; पाँच उस डंडे को भी गिनता है जो शुरू से पानी छू रहा था; तीन का कोई आधार नहीं।",
  "qa-ph-a-rope-ladder-and-a-rising-tide", pos=3, check=_ph4)

def _ph5():
    pal = lambda n: str(n) == str(n)[::-1]
    nxt = next(n for n in range(15952, 20000) if pal(n))
    assert pal(15951) and nxt == 16061
    return f"{(nxt - 15951) // 2} km/h"
N(QA, "Puzzle Hybrid", "hard",
  "A car's odometer reads 15951 km, a number that reads the same backwards. Exactly 2 hours later it shows the next such number. What was the car's average speed?",
  "एक कार का ओडोमीटर 15951 किमी दिखाता है, एक ऐसी संख्या जो उलटी पढ़ने पर भी वही रहती है। ठीक 2 घंटे बाद वह अगली ऐसी संख्या दिखाता है। कार की औसत चाल क्या थी?",
  ["50 km/h", "55 km/h", "60 km/h", "110 km/h"], 1,
  "The next number reading the same backwards cannot keep 159 as its first three digits (15951 is the largest such), so it starts 160..., giving 16061. The car went 16061 - 15951 = 110 km in 2 hours: 55 km/h. "
  "110 km/h forgets to divide by the 2 hours; 50 and 60 km/h have no basis.",
  "उलटी पढ़ने पर वही रहने वाली अगली संख्या पहले तीन अंक 159 नहीं रख सकती (15951 ऐसी सबसे बड़ी है), इसलिए वह 160... से शुरू होती है, जिससे 16061 मिलता है। कार ने 2 घंटों में 16061 - 15951 = 110 किमी तय किए: 55 किमी/घंटा। "
  "110 किमी/घंटा 2 घंटों से भाग देना भूल जाता है; 50 और 60 किमी/घंटा का कोई आधार नहीं।",
  "qa-ph-the-next-palindrome-on-an-odometer", _ph5,
  opts_hi=["50 किमी/घंटा", "55 किमी/घंटा", "60 किमी/घंटा", "110 किमी/घंटा"])

# ---------------------------------------------------------------- the data-sufficiency block's two Quant items
def _ds1():
    s1 = {F(a + b + cc, 3) for a in range(0, 11) for b in [10 - a] for cc in range(0, 20)}
    s2 = {F(a + b + 5, 3) for a in range(0, 20) for b in range(0, 20)}
    both = {F(a + (10 - a) + 5, 3) for a in range(0, 11)}
    assert both == {5}
    return _ds(s1, s2, both)
DS(QA, "medium",
   "What is the average of the three numbers a, b and c?",
   "तीन संख्याओं a, b और c का औसत क्या है?",
   "a + b = 10.", "a + b = 10।",
   "c = 5.", "c = 5।",
   2,
   "Statement I gives a + b but says nothing about c; Statement II gives c but says nothing about a and b. Together, a + b + c = 15 and the average is 5, whatever a and b are separately. Both statements are needed.",
   "कथन I, a + b देता है पर c के बारे में कुछ नहीं कहता; कथन II, c देता है पर a और b के बारे में कुछ नहीं। दोनों मिलकर a + b + c = 15 और औसत 5 है, a और b अलग-अलग चाहे जो हों। दोनों कथन आवश्यक हैं।",
   "qa-ds-an-average-of-three-from-two-facts", _ds1)

def _ds2():
    xs = range(-20, 21)
    s1 = {x + y for x in xs for y in xs if 2 * x + 2 * y == 18}
    s2 = {x + y for x in xs for y in xs if x - y == 3}
    both = {x + y for x in xs for y in xs if 2 * x + 2 * y == 18 and x - y == 3}
    assert s1 == {9} and len(s2) > 1
    return _ds(s1, s2, both)
DS(QA, "hard",
   "What is the value of x + y?",
   "x + y का मान क्या है?",
   "2x + 2y = 18.", "2x + 2y = 18।",
   "x - y = 3.", "x - y = 3।",
   0,
   "Statement I alone settles it: dividing by 2 gives x + y = 9, even though x and y themselves stay unknown. Statement II alone gives only their difference. The trap is to think both are needed because finding x and y separately would need both; the question asks only for their sum.",
   "कथन I अकेले इसे तय कर देता है: 2 से भाग देने पर x + y = 9 मिलता है, यद्यपि स्वयं x और y अज्ञात रहते हैं। कथन II अकेले केवल उनका अंतर देता है। जाल यह सोचना है कि दोनों चाहिए क्योंकि x और y को अलग-अलग निकालने के लिए दोनों चाहिए होते; प्रश्न केवल उनका योग पूछता है।",
   "qa-ds-a-sum-found-from-one-equation", _ds2)
